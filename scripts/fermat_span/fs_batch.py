"""fs_batch.py -- driver for the span-test computations recorded in results/fermat_span/.

  python3 fs_batch.py validate            validations (i)-(iv) + Definition 4.8 cross-check -> validation.md/.json
  python3 fs_batch.py main DMAX [q,...]   main runs: q in {44,51,52,68}, every multiple d = q k <= DMAX
  python3 fs_batch.py summary             summary.md from the run_q*_d*.json records
Binaries are compiled into $FS_BUILD (default: a scratch directory) -- nothing compiled is written to the repo.
"""
import glob
import json
import os
import subprocess
import sys
import tempfile
import time

import fs_lattice as L
import fs_run as R
from fs_def48 import check_primitive, check_recursion

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, "results", "fermat_span")
BUILD = os.environ.get("FS_BUILD", "/tmp/claude-0/-home-user/449337f7-e47b-5016-b39e-f1ecd6549c95/scratchpad/spanw/build")
KNOWN_RUNS = [(12, 12), (15, 15), (20, 20), (21, 21), (28, 28), (33, 33), (39, 39), (35, 70), (55, 110), (57, 114)]
TABLE4 = {(33, 66): (19, 26, 43, 44), (35, 70): (10, 12, 13, 53, 56, 66), (39, 78): (25, 43, 49),
          (44, 132): (3, 37, 39, 75, 84, 99, 125), (51, 102): (7, 19, 25, 60, 68, 87, 91),
          (52, 156): (24, 51, 63, 75, 87, 97, 149), (55, 110): (19, 29, 39, 79, 109),
          (57, 114): (23, 41, 64, 66, 71, 77)}
TABLE2 = {12: (1, 8, 9), 15: (1, 7, 10, 12), 20: (3, 8, 19), 21: (1, 10, 15, 16), 28: (5, 13, 17, 21),
          33: (1, 4, 16, 22, 25, 31), 35: (1, 2, 16, 17, 21, 22, 30, 31), 39: (1, 16, 19, 22, 28, 31),
          44: (8, 11, 15, 19, 27, 31, 43)}


def build():
    os.makedirs(BUILD, exist_ok=True)
    exe = os.path.join(BUILD, "fs_enum")
    subprocess.run(["gcc", "-O2", "-march=native", "-o", exe, os.path.join(HERE, "fs_enum.c")], check=True)
    return exe


def log_to(path):
    f = open(path, "a")

    def log(msg):
        print(msg, flush=True)
        f.write(msg + "\n")
        f.flush()
    return log


# ----------------------------------------------------------------------------- degree-d class machinery
def xi_functionals(d):
    """(Qd, fvec, lat, std, cols): fvec[i] = mod-2 functional on Z^h dual to xi_{Qd[i]} (vanishing on L0)."""
    X = L.read_tuples()
    h = (d - 1) // 2
    Qd = L.Q_divisors(d)
    std = L.standard_gens(d, "div")
    cols = [L.fold_tuple(t, d) for _, t in std]
    lat = L.SNFLattice(cols, h)
    rows2 = lat.torsion_rows(2)
    Phi = [[x % 2 for x in lat.Ul[j]] for j in rows2]
    e = len(Phi)
    M = [sum(R.parity(Phi[j], L.fold_tuple(L.lift(X[qp], qp, d), d)) << j for j in range(e)) for qp in Qd]
    assert R.f2_rank(M) == e == len(Qd)
    fvec = []
    for i in range(len(Qd)):
        rows = [(M[j], 1 if j == i else 0) for j in range(len(Qd))]
        g = R.f2_dual_vector([v for v, b in rows if b == 0], e, M[i])
        u = [0] * h
        for j in range(e):
            if g >> j & 1:
                u = [(a + b) % 2 for a, b in zip(u, Phi[j])]
        fvec.append(u)
    return Qd, fvec, lat, std, cols


def signature(tup, d, Qd, fvec):
    x = L.fold_tuple(tup, d)
    s = [qp for i, qp in enumerate(Qd) if R.parity(fvec[i], x)]
    return "+".join(f"xi{qp}" for qp in s) or "0"


# ----------------------------------------------------------------------------- validations
def kubert_certificate(q, X):
    """2 xi_q = explicit Z-combination of D_q + S_q generators (authors' S_q = lifted Def 3.7 standards)."""
    d, h = q, (q - 1) // 2
    std = L.standard_gens(q, "div")
    cols = [L.fold_tuple(t, d) for _, t in std]
    lat = L.SNFLattice(cols, h)
    target = [2 * c for c in L.to_vec(X[q], d)]
    x = L.fold(target, d)
    ok2 = lat.contains(x)
    ok1 = lat.contains(L.fold(L.to_vec(X[q], d), d))
    lit = L.SNFLattice([L.fold_tuple(t, d) for _, t in L.standard_gens(q, "deg")], h)
    lit2 = lit.contains(x)
    path_i = path_ii = None
    if ok2:
        c = L.solve_in_lattice(cols, h, x)
        r = list(target)
        terms = []
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
        path_i = os.path.join(OUT, f"kubert_q{q}.txt")
        with open(path_i, "w") as f:
            f.write("# Validation (i), Kubert-Aoki (MMRV Theorem 4.3): 2 xi_q is an explicit Z-combination of linear tuples\n")
            f.write("# and standard tuples of degree q (S_q read as in the authors' code: s_{p,i} of every divisor of q, lifted).\n")
            f.write("# check: python3 scripts/fermat_span/fs_check.py <this file>\n")
            f.write(f"type member\nmultiple 2\nscope DS\nq {q}\nd {d}\nxi_q {' '.join(map(str, X[q]))}\nknown -\n")
            for coef, lab, tup in terms:
                if lab[0] == "std":
                    f.write(f"gen {coef} std {lab[1]} {lab[2]} {lab[3]} {' '.join(map(str, tup))}\n")
                elif lab[0] == "lin":
                    f.write(f"gen {coef} lin {lab[1]} {' '.join(map(str, tup))}\n")
                else:
                    f.write(f"gen {coef} eps {' '.join(map(str, tup))}\n")
            f.write("end\n")
    if not ok1:
        # mod-2 functional vanishing on L0, odd on xi_q
        rows2 = lat.torsion_rows(2)
        xq = L.fold(L.to_vec(X[q], d), d)
        for j in rows2:
            u = [v % 2 for v in lat.Ul[j]]
            if R.parity(u, xq):
                break
        else:
            raise AssertionError("no mod-2 functional separates xi_q")
        for cvec in cols:
            assert R.parity(u, cvec) == 0
        Uset = sorted(a for a in range(1, d) if 2 * a != d and u[min(a, d - a) - 1])
        path_ii = os.path.join(OUT, f"notDS_q{q}.txt")
        with open(path_ii, "w") as f:
            f.write("# Validation (ii): xi_q is NOT in D_q + S_q.  chi(v) = #(entries of v in U) mod 2 vanishes on every linear\n")
            f.write("# and every (lifted) standard tuple of degree q and is odd on xi_q.\n")
            f.write("# check: python3 scripts/fermat_span/fs_check.py <this file>\n")
            f.write(f"type nonmember\nscope DS\nq {q}\nd {d}\nxi_q {' '.join(map(str, X[q]))}\nknown -\nmodulus 2\n")
            f.write(f"U {' '.join(map(str, Uset))}\nend\n")
    return {"q": q, "2xi_in_DS": ok2, "xi_in_DS": ok1, "2xi_in_DS_literal": lit2,
            "rank_L0": lat.r, "rank_literal": lit.r, "cert_i": path_i and os.path.relpath(path_i, REPO),
            "cert_ii": path_ii and os.path.relpath(path_ii, REPO)}


def validate():
    exe = build()
    os.makedirs(OUT, exist_ok=True)
    log = log_to(os.path.join(OUT, "validation.log"))
    X = L.read_tuples()
    rec = {"date": time.strftime("%Y-%m-%d %H:%M:%S")}
    # Definition 4.8 cross-check
    d48 = []
    for q in [12, 15, 20, 21, 28, 33, 35, 39, 44, 51, 52, 55, 57, 65, 68, 69]:
        prim = check_primitive(q, X[q])
        recur = check_recursion(q, X[q])
        d48.append({"q": q, "hodge": L.is_hodge(X[q], q), "primitive_matches": [(s, m) for s, m in prim],
                    "recursion_conventions_ok": [list(k) for k, v in recur.items() if v]})
        log(f"[def4.8] q={q} Hodge={L.is_hodge(X[q], q)} primitive={prim} recursion ok for (eps,s,x)={[k for k, v in recur.items() if v]}")
    rec["def48"] = d48
    # (i), (ii)
    Qs = [q for q in range(2, 71) if L.in_Q(q)]
    rec["kubert"] = []
    for q in Qs:
        r = kubert_certificate(q, X)
        rec["kubert"].append(r)
        log(f"[i/ii] q={q} 2xi in D+S: {r['2xi_in_DS']} xi in D+S: {r['xi_in_DS']} (literal Def 3.7 S_q: 2xi in D+S_lit: {r['2xi_in_DS_literal']}, rank {r['rank_literal']} vs {r['rank_L0']})")
    # (iii)
    rec["known_runs"] = []
    for q, d in KNOWN_RUNS + [(35, 35)]:
        res = R.analyze(q, d, [], OUT, exe, log)
        rec["known_runs"].append({k: res[k] for k in ("q", "d", "member", "certificate", "reduced_hodge_counts", "signatures")})
    # Aoki check for a range of degrees: B_d = L0 + T_d and K/L0 = F_2^{|Q(d)|}
    rec["aoki"] = []
    for d in [12, 24, 36, 48, 60, 66, 84, 88, 90, 102, 104, 120, 132, 136, 156, 176, 180, 204, 208, 220, 264, 272, 308, 312, 330, 390, 462]:
        Qd, fvec, lat, std, cols = xi_functionals(d)
        ok = True
        for i, qp in enumerate(Qd):
            base = L.lift(X[qp], qp, d)
            for t in L.half_units(d):
                v = L.fold_tuple(L.act(t, base, d), d)
                if any(R.parity(fvec[j], v) != (1 if j == i else 0) for j in range(len(Qd))):
                    ok = False
        rec["aoki"].append({"d": d, "Q": Qd, "dim": len(Qd), "orbits_trivial_mod_L0": ok})
        log(f"[aoki] d={d} Q(d)={Qd}: K_d = L0 + T_d, K_d/L0 = F_2^{len(Qd)} with basis the xi classes; every G_d-conjugate t.xi_q' == xi_q' mod L0: {ok}")
    # (iv) Table 4 / Table 2 representatives
    rec["tables"] = []
    for (q, d), tup in sorted(TABLE4.items()) + [((q, q), t) for q, t in sorted(TABLE2.items())]:
        Qd, fvec, lat, std, cols = xi_functionals(d)
        sig = signature(tup, d, Qd, fvec)
        diff = [a - b for a, b in zip(L.to_vec(tup, d), L.to_vec(L.lift(X[q], q, d), d))]
        exact = lat.contains(L.fold(diff, d))
        r = {"q": q, "d": d, "tuple": tup, "length": len(tup), "hodge": L.is_hodge(tup, d), "class": sig,
             "congruent_to_xi_mod_D+S": exact}
        rec["tables"].append(r)
        log(f"[iv] q={q} d={d} {tup} (length {len(tup)}) Hodge={r['hodge']} class in K/L0 = {sig}; tuple - xi_q in D_d+S_d: {exact}")
    with open(os.path.join(OUT, "validation.json"), "w") as f:
        json.dump(rec, f, indent=1, default=str)


def main_runs(dmax, qs):
    exe = build()
    log = log_to(os.path.join(OUT, "main.log"))
    known_all = [q for q, d in KNOWN_RUNS]
    for q in qs:
        for d in range(q, dmax + 1, q):
            if os.path.exists(os.path.join(OUT, f"run_q{q}_d{d}.json")):
                continue
            known = [qp for qp in L.Q_divisors(d) if qp in known_all and qp != q]
            try:
                R.analyze(q, d, known, OUT, exe, log)
            except Exception as ex:          # record and continue
                log(f"[q={q} d={d}] ERROR {type(ex).__name__}: {ex}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "validate":
        validate()
    elif cmd == "main":
        dmax = int(sys.argv[2])
        qs = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else [44, 51, 52, 68]
        main_runs(dmax, qs)
