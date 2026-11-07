"""fs_run.py -- the span test for an exceptional tuple xi_q in degree d (a multiple of q).

  Lambda_d = D_d + sum_{d'|d} S_{d'} + sum_{q' known} Z[G_d] xi_{q'} + span_Z{Hodge tuples of length <= 6 in R_d}

Method (all exact; see docs/fermat/01-span-test.md):
 1. L0 = D_d + sum_{d'|d} S_{d'} (standard tuples of MMRV Def. 3.7 of every divisor, lifted).  In folded
    coordinates Z^h (h = floor((d-1)/2), kernel D_d) compute the Smith form U L0 V = diag.  Check that
    rank L0 = rank K_d (K_d = pi(B_d) = kernel of the Hodge functionals), so that K_d/L0 = torsion of Z^h/L0,
    and that every elementary divisor is 1 or 2.  The rows of U with elementary divisor 2, reduced mod 2,
    are functionals Phi_j : Z^h -> F_2 inducing K_d/L0 = F_2^{e}.
 2. Classes of xi_{q'} (q' in Q, q' | d) and of all their G_d-conjugates; check that the xi_{q'} form an
    F_2-basis of K_d/L0 (an exact check of the consequence B_d = L0 + T_d of Aoki's Theorem 4.2 and of
    Kubert-Aoki's Theorem 4.3 in degree d) and change basis to the dual basis f_{q'} of the xi's.
 3. fs_enum (C) enumerates every reduced Hodge tuple of length <= 6 and records its class ('signature').
 4. F_2 linear algebra: xi_q in Lambda_d  <=>  e_q in span(signatures, e_{q'} for known q').
 5. Certificates: an explicit integer identity (member) or a symmetric subset U of (Z/d)-{0} (a mod-2
    functional) vanishing on every generator and odd on xi_q (non-member).
Usage: python3 fs_run.py q d [known q' list comma-separated] [--outdir DIR] [--enum PATH]
"""
import argparse
import json
import os
import subprocess
import sys
import time

import fs_lattice as L

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DEFAULT_OUT = os.path.join(REPO, "results", "fermat_span")


# ----------------------------------------------------------------------------- F_2 helpers (ints as bit vectors)
def f2_rank(vecs):
    basis = {}
    for v in vecs:
        while v:
            p = v.bit_length() - 1
            if p in basis:
                v ^= basis[p]
            else:
                basis[p] = v
                break
    return len(basis)


def f2_solve_combination(gens, target):
    """gens: list of (vec, label). Return list of labels whose vecs XOR to target, or None."""
    basis = {}          # pivot -> (vec, set of gen indices)
    for idx, (v, _) in enumerate(gens):
        comb = {idx}
        while v:
            p = v.bit_length() - 1
            if p in basis:
                bv, bc = basis[p]
                v ^= bv
                comb ^= bc
            else:
                basis[p] = (v, comb)
                break
    v, comb = target, set()
    while v:
        p = v.bit_length() - 1
        if p not in basis:
            return None
        bv, bc = basis[p]
        v ^= bv
        comb ^= bc
    return sorted(comb)


def f2_dual_vector(vecs, n, target):
    """f in F_2^n (int) with f.v = 0 for all v in vecs and f.target = 1, or None."""
    # solve the linear system rows = vecs (f.v = 0) plus target (f.target = 1); unknown f (n bits)
    rows = [(v, 0) for v in vecs] + [(target, 1)]
    piv = []
    for v, b in rows:
        for pv, pb, pbit in piv:
            if v >> pbit & 1:
                v ^= pv
                b ^= pb
        if v == 0:
            if b:
                return None
            continue
        pbit = v.bit_length() - 1
        piv = [(pv ^ v, pb ^ b, pp) if pv >> pbit & 1 else (pv, pb, pp) for pv, pb, pp in piv]
        piv.append((v, b, pbit))
    f = 0
    for pv, pb, pbit in piv:
        if pb:
            f |= 1 << pbit
    for v, b in rows:
        assert bin(f & v).count("1") % 2 == b
    return f


def parity(u, x):
    """u: list of 0/1 over Z^h coordinates; x: integer vector in Z^h."""
    return sum(ui * xi for ui, xi in zip(u, x) if ui) % 2


# ----------------------------------------------------------------------------- main analysis
def analyze(q, d, known, outdir, enum_bin, log=print):
    t0 = time.time()
    X = L.read_tuples()
    h = (d - 1) // 2
    Qd = L.Q_divisors(d)
    assert q in Qd, f"{q} does not divide {d} or is not in Q"
    res = {"q": q, "d": d, "Q_divisors": Qd}
    # -- Hodge kernel rank
    A = L.hodge_matrix(d)
    rA = int(L.pari.matrank(L.pari.matrix(len(A), h, [x for r in A for x in r])))
    res["rank_K"] = h - rA
    # -- L0 = D_d + sum_{d'|d} S_{d'} (folded), Smith form
    std = L.standard_gens(d, "div")
    cols = [L.fold_tuple(t, d) for _, t in std]
    for lab, t in std:
        assert L.is_hodge(t, d), ("standard tuple not Hodge", lab, t)
    lat = L.SNFLattice(cols, h)
    ed = lat.elementary_divisors()
    res.update({"h": h, "n_standard": len(std), "rank_L0": lat.r, "eldiv_gt1": [e for e in ed if e > 1]})
    assert lat.r == h - rA, "rank L0 != rank K_d: K_d/L0 infinite"
    assert all(e in (1, 2) for e in ed), f"elementary divisors not in {{1,2}}: {ed}"
    rows2 = lat.torsion_rows(2)
    e = len(rows2)
    assert e <= 20, "quotient too large for the C class encoding"
    Phi = [[x % 2 for x in lat.Ul[j]] for j in rows2]          # e functionals Z^h -> F_2, vanishing on L0

    def phivec(x):
        return sum(parity(Phi[j], x) << j for j in range(e))
    for c in cols:
        assert phivec(c) == 0
    # -- classes of the available xi_{q'} and of all their G_d-conjugates
    avail = [qp for qp in Qd if qp in X]
    missing = [qp for qp in Qd if qp not in X]
    xi_cls, orbit_ok = {}, True
    for qp in avail:
        base = L.lift(X[qp], qp, d)
        x0 = L.fold_tuple(base, d)
        assert all(sum(r[a] * x0[a] for a in range(h)) == 0 for r in A), "xi not Hodge"
        xi_cls[qp] = phivec(x0)
        for t in L.half_units(d):
            if phivec(L.fold_tuple(L.act(t, base, d), d)) != xi_cls[qp]:
                orbit_ok = False
    rk = f2_rank(list(xi_cls.values()))
    basis_ok = (rk == e == len(avail) and not missing)
    res.update({"dim_V": e, "xi_available": avail, "xi_missing_from_csv": missing, "rank_xi_classes": rk,
                "xi_orbits_trivial_mod_L0": orbit_ok, "xi_basis_of_K_mod_L0": basis_ok})
    if not missing:
        assert rk == e, f"xi classes do not span K/L0 (rank {rk} < {e}): Aoki's Theorem 4.2 check fails"
    log(f"[q={q} d={d}] h={h} rank K={h - rA} #std={len(std)} rank L0={lat.r} dim_F2 K/L0={e} Q(d)={Qd} "
        f"xi-basis={basis_ok} missing={missing} ({time.time()-t0:.1f}s)")

    def names(c):
        """class vector -> 'xi12+xi33' (when the xi's form a basis) or raw hex."""
        if not basis_ok:
            return f"raw:{c:x}"
        comb = f2_solve_combination([(xi_cls[qp], qp) for qp in avail], c)
        return "+".join(f"xi{avail[i]}" for i in comb) or "0"
    # -- class file for fs_enum: bit j of (a) = Phi_j at min(a, d-a)
    workdir = os.path.join(outdir, "work")
    os.makedirs(workdir, exist_ok=True)
    cls_path = os.path.join(workdir, f"classes_d{d}.txt")
    with open(cls_path, "w") as f:
        f.write(f"{e}\n")
        for a in range(1, d):
            b = 0
            if 2 * a != d:
                aa = min(a, d - a)
                for j in range(e):
                    if Phi[j][aa - 1]:
                        b |= 1 << j
            f.write(f"{a} {b:x}\n")
    t1 = time.time()
    out = subprocess.run([enum_bin, str(d), cls_path, "--reduced"], capture_output=True, text=True, check=True)
    sigs, counts = [], {}
    for line in out.stdout.splitlines():
        w = line.split()
        if w[0] == "count":
            counts[int(w[1])] = int(w[2])
        elif w[0] == "sig":
            sigs.append((int(w[1]), int(w[2], 16), int(w[3]), tuple(int(x) for x in w[4:])))
    res["reduced_hodge_counts"] = counts
    res["enum_seconds"] = round(time.time() - t1, 2)
    for Lw, sg, cnt, wit in sigs:                    # witnesses re-verified in Python
        assert len(wit) == Lw and L.is_hodge(wit, d)
        assert phivec(L.fold_tuple(wit, d)) == sg
    res["signatures"] = [{"length": Lw, "class": names(sg), "count": cnt, "witness": list(wit)} for Lw, sg, cnt, wit in sigs]
    kn = [qp for qp in avail if qp != q and qp in known]
    gens = [(xi_cls[qp], ("xi", qp)) for qp in kn] + [(sg, ("hodge", wit)) for Lw, sg, cnt, wit in sigs if sg]
    short_span = f2_rank([sg for _, sg, _, _ in sigs])
    full_span = f2_rank([g for g, _ in gens])
    orbit_dim = 1 if xi_cls[q] else 0
    comb = f2_solve_combination(gens, xi_cls[q])
    member = comb is not None
    res.update({"known_used": kn, "dim_short_span": short_span, "dim_Lambda_image": full_span,
                "dim_orbit_xi_q": orbit_dim if orbit_ok else None, "member": member,
                "dim_orbit_cap_Lambda": (1 if member else 0) if orbit_ok else None,
                "short_classes": sorted({names(sg) for _, sg, _, _ in sigs})})
    lifted = L.lift(X[q], q, d)
    if member:
        chosen = [gens[i][1] for i in comb]
        cert = build_positive(q, d, lifted, chosen, std, cols, lat, h, X)
        path = os.path.join(outdir, f"cert_q{q}_d{d}.txt")
        write_positive(path, q, d, X[q], cert, kn)
        res["certificate"] = os.path.relpath(path, REPO)
    else:
        fsel = f2_dual_vector([sg for _, sg, _, _ in sigs] + [xi_cls[qp] for qp in kn], e, xi_cls[q])
        assert fsel is not None
        u = [0] * h
        for j in range(e):
            if fsel >> j & 1:
                u = [(a + b) % 2 for a, b in zip(u, Phi[j])]
        Uset = sorted(a for a in range(1, d) if 2 * a != d and u[min(a, d - a) - 1])
        assert parity(u, L.fold_tuple(lifted, d)) == 1
        for c in cols:
            assert parity(u, c) == 0
        for qp in kn:
            for t in L.units(d):
                assert parity(u, L.fold_tuple(L.act(t, L.lift(X[qp], qp, d), d), d)) == 0
        for Lw, sg, cnt, wit in sigs:
            assert parity(u, L.fold_tuple(wit, d)) == 0
        vals = {qp: parity(u, L.fold_tuple(L.lift(X[qp], qp, d), d)) for qp in avail}
        fname = "chi(xi_q')=1 exactly for q' in {" + ",".join(str(qp) for qp in avail if vals[qp]) + "}"
        res["dual_functional"] = fname
        res["dual_kills_all_other_xi"] = all(vals[qp] == 0 for qp in avail if qp != q)
        path = os.path.join(outdir, f"dual_q{q}_d{d}.txt")
        write_dual(path, q, d, X[q], Uset, kn, fname)
        res["certificate"] = os.path.relpath(path, REPO)
    res["seconds"] = round(time.time() - t0, 2)
    with open(os.path.join(outdir, f"run_q{q}_d{d}.json"), "w") as f:
        json.dump(res, f, indent=1)
    log(f"[q={q} d={d}] member={member} dim K/L0={e} dim short span={short_span} dim Lambda/L0={full_span} "
        f"known={kn} short classes={res['short_classes']} counts={counts} cert={res['certificate']} ({res['seconds']}s)")
    return res


# ----------------------------------------------------------------------------- certificates
def build_positive(q, d, lifted, chosen, std, cols, lat, h, X):
    target = L.to_vec(lifted, d)
    terms = []
    r = list(target)
    for lab in chosen:
        if lab[0] == "xi":
            tup = L.lift(X[lab[1]], lab[1], d)
            terms.append((1, ("xi", lab[1], 1), tup))
        else:
            tup = tuple(lab[1])
            terms.append((1, ("hodge",), tup))
        for a in tup:
            r[a - 1] -= 1
    x = L.fold(r, d)
    assert lat.contains(x), "remainder not in L0 (inconsistent class computation)"
    c = L.solve_in_lattice(cols, h, x)
    assert c is not None
    for ci, (lab, tup) in zip(c, std):
        if ci:
            terms.append((ci, lab, tup))
            for a in tup:
                r[a - 1] -= ci
    for a in range(1, (d + 1) // 2):
        assert r[a - 1] == r[d - a - 1]
        if r[a - 1]:
            terms.append((r[a - 1], ("lin", a), (a, d - a)))
    if d % 2 == 0 and r[d // 2 - 1]:
        terms.append((r[d // 2 - 1], ("eps",), (d // 2,)))
    # exact verification of the identity
    s = [0] * (d - 1)
    for coef, lab, tup in terms:
        for a in tup:
            s[a - 1] += coef
    assert s == target, "certificate identity fails"
    return terms


def write_positive(path, q, d, xi, terms, known):
    with open(path, "w") as f:
        f.write("# fermat_span certificate (MEMBER): xi_q lies in Lambda_d (MMRV arXiv:2609.27301 notation)\n")
        f.write("# identity in R_d:  lift_{q->d}(xi_q) = sum over 'gen' lines of coef * (tuple)\n")
        f.write("# check: python3 scripts/fermat_span/fs_check.py <this file>\n")
        f.write(f"type member\nq {q}\nd {d}\nxi_q {' '.join(map(str, xi))}\n")
        f.write(f"known {','.join(map(str, known)) if known else '-'}\n")
        for coef, lab, tup in terms:
            if lab[0] == "hodge":
                f.write(f"gen {coef} hodge {' '.join(map(str, tup))}\n")
            elif lab[0] == "xi":
                f.write(f"gen {coef} xi {lab[1]} {lab[2]} {' '.join(map(str, tup))}\n")
            elif lab[0] == "std":
                f.write(f"gen {coef} std {lab[1]} {lab[2]} {lab[3]} {' '.join(map(str, tup))}\n")
            elif lab[0] == "lin":
                f.write(f"gen {coef} lin {lab[1]} {' '.join(map(str, tup))}\n")
            else:
                f.write(f"gen {coef} eps {' '.join(map(str, tup))}\n")
        f.write("end\n")


def write_dual(path, q, d, xi, Uset, known, fname):
    with open(path, "w") as f:
        f.write("# fermat_span DUAL certificate (NON-MEMBER): xi_q does not lie in Lambda_d (MMRV notation)\n")
        f.write("# U is a subset of (Z/d)-{0} with U = -U and d/2 not in U; chi(v) = #(entries of v in U) mod 2 is a\n")
        f.write("# homomorphism R_d -> Z/2 (y = chi/2 is a rational vector with y.v integral for every generator v).\n")
        f.write("# claim: chi = 0 on (a)+(-a), eps_d, every lifted standard tuple of every divisor of d, every G_d-conjugate\n")
        f.write("# of every known xi_q' and EVERY Hodge tuple of length <= 6 in degree d; chi(lift(xi_q)) = 1.\n")
        f.write("# check: python3 scripts/fermat_span/fs_check.py <this file>   (runs the independent C enumeration)\n")
        f.write(f"type nonmember\nq {q}\nd {d}\nxi_q {' '.join(map(str, xi))}\n")
        f.write(f"known {','.join(map(str, known)) if known else '-'}\n")
        f.write(f"modulus 2\nfunctional {fname}\n")
        f.write(f"U {' '.join(map(str, Uset))}\nend\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("q", type=int)
    ap.add_argument("d", type=int)
    ap.add_argument("known", nargs="?", default="")
    ap.add_argument("--outdir", default=DEFAULT_OUT)
    ap.add_argument("--enum", default=os.path.join(HERE, "fs_enum"))
    a = ap.parse_args()
    known = [int(x) for x in a.known.split(",") if x.strip()]
    analyze(a.q, a.d, known, a.outdir, a.enum)


if __name__ == "__main__":
    main()
