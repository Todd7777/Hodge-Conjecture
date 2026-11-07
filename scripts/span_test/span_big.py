"""span_big.py -- the span test for an exceptional tuple xi_q in degree d (any d up to a few thousand).

Lambda_d = D_d + S~_d + span_Z(Hodge tuples of length <= 6 in R_d) + (known-algebraic xi_{q'}),
all algebraic by Ran-Shioda (linear), Aoki (standard), Lefschetz (1,1) and Kang (fourfolds) as cited in
Miranda-Movasati-Rufino-Villaflor (arXiv:2609.27301).  Question: is xi_q in Lambda_d?

Method.  Work in R_d/D_d = Z^H.  L0 = (D_d + S~_d)/D_d has a Z-basis (exact HNF, python-flint) with pivot
columns J and upper-triangular pivot block A.  For v in B_d we have 2v in L0 (Kubert-Aoki), so
c(v) = v_J A^{-1} lies in (1/2)Z^rho and phi(v) = 2c(v) mod 2 is the class of v in B_d/L0.  We evaluate a
projection of phi on a set S of coordinates through the exact rational functionals y_j = 2 A^{-1} e_j.
* NEGATIVE verdicts are always valid: if the projected class of xi is not in the span of the projected
  classes of the generators, then xi is not in Lambda_d; the certificate is a rational vector y on the
  coordinates J with y.g an even integer for every generator g and y.xi an odd integer.
* POSITIVE verdicts are re-checked exactly: the F_2 combination is turned into an integer vector
  xi - sum(tuples), whose membership in L0 is tested by exact reduction against the HNF basis.

Usage: python3 -I span_big.py --q Q --d D --xi a,b,... --classes F4 [F6 ...] [--extra q:a,b,...]
       [--extra-coords N] [--cert OUT.json]
The classes files are outputs of hodge_mitm (one reduced class per line, signed entries).
"""
import argparse
import json
import sys
import time
from math import gcd

import flint
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--q", type=int, required=True)
ap.add_argument("--d", type=int, required=True)
ap.add_argument("--xi", required=True)
ap.add_argument("--classes", nargs="+", required=True)
ap.add_argument("--extra", nargs="*", default=[])
ap.add_argument("--extra-coords", type=int, default=24)
ap.add_argument("--cert", default=None)
args = ap.parse_args()
q, d = args.q, args.d
assert d % q == 0
H = (d - 1) // 2
T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def red(entries, deg):
    """Sparse class mod D_d (dict index -> coefficient) of a tuple of degree deg, lifted to degree d."""
    k = d // deg
    v = {}
    for a in entries:
        a = (a * k) % d
        assert a != 0
        if 2 * a == d:
            continue
        i, c = (a - 1, 1) if a <= H else (d - a - 1, -1)
        v[i] = v.get(i, 0) + c
    return {i: c for i, c in v.items() if c}


def is_hodge(ent, deg):
    ell = len(ent)
    return all(2 * sum((t * a) % deg for a in ent) == ell * deg for t in range(1, deg) if gcd(t, deg) == 1)


def standard(dd):
    """Standard tuples s_{p,i} of MMRV Definition 3.7 in degree dd (p | dd prime, k = dd/p, k/gcd(i,k) >= 3;
    p not dividing i for p >= 5; for p = 2, 3 the tuples have length 4 and are Hodge-checked, hence
    algebraic by Lefschetz (1,1) in any case)."""
    out = []
    for p in range(2, dd + 1):
        if dd % p or any(p % r == 0 for r in range(2, p)):
            continue
        k = dd // p
        for i in range(1, dd):
            if p >= 5 and i % p == 0:
                continue
            if k < 3 * gcd(i, k):
                continue
            ent = [i % dd, (i + k) % dd, (dd - 2 * i) % dd, k % dd] if p == 2 else [(i + j * k) % dd for j in range(p)] + [(dd - p * i) % dd]
            if 0 in ent:
                continue
            out.append(ent)
    return out


# ---------------- L0 = (D + S~)/D : exact HNF basis
gens = set()
for dd in range(2, d + 1):
    if d % dd:
        continue
    for ent in standard(dd):
        if not is_hodge(ent, dd):
            sys.exit(f"non-Hodge standard tuple {ent} in degree {dd}: definition error")
        v = red(ent, dd)
        if v:
            gens.add(tuple(sorted(v.items())))
dense = []
for g in gens:
    row = [0] * H
    for i, c in g:
        row[i] = c
    dense.append(row)
Hn = flint.fmpz_mat(dense).hnf()
basis = []
for i in range(Hn.nrows()):
    row = [int(Hn[i, j]) for j in range(H)]
    if any(row):
        basis.append(row)
rho = len(basis)
piv = [next(j for j in range(H) if r[j]) for r in basis]
assert piv == sorted(piv) and len(set(piv)) == rho
pos = {c: i for i, c in enumerate(piv)}
A = flint.fmpq_mat([[basis[i][piv[k]] for k in range(rho)] for i in range(rho)])  # rows i, cols k (upper triangular)
log(f"q={q} d={d} H={H}: {len(gens)} distinct standard generators mod D, rank(L0) = {rho}")

At = A.transpose()


def full_class(vs):
    """Exact: list of sparse vectors -> list of (bits over rho coords, c vector). Raises if 2v not in L0."""
    out = []
    for v in vs:
        vJ = flint.fmpq_mat(rho, 1, [v.get(piv[k], 0) for k in range(rho)])
        c = At.solve(vJ)
        cs = [c[k, 0] for k in range(rho)]
        # check v lies in the Q-span: sum c_k basis_k == v
        recon = [0] * H
        for k, ck in enumerate(cs):
            if ck != 0:
                for j in range(piv[k], H):
                    if basis[k][j]:
                        recon[j] += ck * basis[k][j]
        if any(recon[j] != v.get(j, 0) for j in range(H)):
            raise ValueError("vector not in the Q-span of L0")
        two = [2 * ck for ck in cs]
        if any(x.q != 1 for x in two):
            raise ValueError("2v not in L0")
        out.append(([int(x.p) % 2 for x in two], cs))
    return out


xi_entries = [int(x) for x in args.xi.split(",")]
assert is_hodge(xi_entries, q), "xi_q is not a Hodge tuple"
xi = red(xi_entries, q)
units_d = [t for t in range(1, d) if gcd(t, d) == 1]
probe_ts = [t for t in units_d if gcd(t, q) == 1][:6]
orbit = [red([(t * a) % q for a in xi_entries], q) for t in probe_ts]
extras = []
for e in args.extra:
    qq, ent = e.split(":")
    ent = [int(x) for x in ent.split(",")]
    assert is_hodge(ent, int(qq))
    for t in [t for t in units_d if gcd(t, int(qq)) == 1][:6]:
        extras.append(red([(t * a) % int(qq) for a in ent], int(qq)))
fc = full_class([xi] + orbit + extras)
xi_bits = fc[0][0]
log(f"xi in L0: {not any(xi_bits)}; orbit classes equal to xi's: {all(b == xi_bits for b, _ in fc[1:1 + len(orbit)])}")

# coordinate set S: pivots of span{xi, extras} plus random extra coordinates
rows_f2 = [b for b, _ in fc]
S = []
work = [list(r) for r in rows_f2]
for r in work:
    j = next((j for j in range(rho) if r[j]), None)
    if j is None:
        continue
    S.append(j)
    for r2 in work:
        if r2 is not r and r2[j]:
            for t in range(rho):
                r2[t] ^= r[t]
rng = np.random.default_rng(12345)
for j in rng.permutation(rho)[: args.extra_coords]:
    if int(j) not in S:
        S.append(int(j))
E = flint.fmpq_mat(rho, len(S), [1 if k == S[c] else 0 for k in range(rho) for c in range(len(S))])
Z = A.solve(E)  # columns of A^{-1}
# per column: numerators mod 2^(e+1) where den = 2^e * odd
cols = []
for c in range(len(S)):
    ys = [2 * Z[k, c] for k in range(rho)]
    den = 1
    for y in ys:
        den = den * int(y.q) // gcd(den, int(y.q))
    e = (den & -den).bit_length() - 1
    if e > 60:
        sys.exit("2-adic valuation of a denominator too large for int64 evaluation")
    nums = [int(y.p) * (den // int(y.q)) for y in ys]
    cols.append((e, np.array([n % (1 << (e + 1)) for n in nums], dtype=np.uint64)))
log(f"{len(S)} coordinates; max 2-adic denominator exponent {max(e for e, _ in cols)}")


def classes_of(spvs):
    """Projected classes (int bitmask over S) for sparse vectors, via the y_j (exact mod 2^(e+1))."""
    n = len(spvs)
    if n == 0:
        return []
    maxlen = max(len(v) for v in spvs)
    idx = np.zeros((n, maxlen), dtype=np.int64)
    coef = np.zeros((n, maxlen), dtype=np.int64)
    valid = np.zeros((n, maxlen), dtype=bool)
    for r, v in enumerate(spvs):
        for t, (i, c) in enumerate(v.items()):
            if i in pos:
                idx[r, t] = pos[i]
                coef[r, t] = c
                valid[r, t] = True
    out = np.zeros(n, dtype=object)
    out[:] = 0
    for b, (e, col) in enumerate(cols):
        mod = np.uint64(1 << (e + 1))
        vals = col[idx]  # n x maxlen
        cu = (coef % (1 << (e + 1))).astype(np.uint64)
        s = (vals * cu * valid).sum(axis=1) % mod
        if np.any(s & np.uint64((1 << e) - 1)):
            raise ValueError("class evaluation not integral: vector not in B or arithmetic error")
        bit = (s >> np.uint64(e)) & np.uint64(1)
        for r in np.nonzero(bit)[0]:
            out[r] |= 1 << b
    return list(out)


# F_2 span with provenance
basisF = {}  # pivot bit -> (mask, provenance list of generator ids)
gen_store = []


def f2_add(mask, prov):
    while mask:
        h = mask.bit_length() - 1
        if h in basisF:
            m2, p2 = basisF[h]
            mask ^= m2
            prov = prov ^ p2
        else:
            basisF[h] = (mask, prov)
            return True
    return False


def f2_reduce(mask):
    prov = frozenset()
    while mask:
        h = mask.bit_length() - 1
        if h not in basisF:
            return mask, prov
        m2, p2 = basisF[h]
        mask ^= m2
        prov = prov ^ p2
    return 0, prov


proj = lambda bits: sum(1 << b for b, j in enumerate(S) if bits[j])
for k, (bits, _) in enumerate(fc[1 + len(orbit):]):
    gen_store.append(("extra", extras[k]))
    f2_add(proj(bits), frozenset([len(gen_store) - 1]))
xi_mask = proj(xi_bits)
total = 0
for fn in args.classes:
    batch = []
    with open(fn) as f:
        for line in f:
            parts = line.split()
            if not parts:
                continue
            v = {}
            for x in parts:
                x = int(x)
                i, c = (x - 1, 1) if x > 0 else (-x - 1, -1)
                v[i] = v.get(i, 0) + c
            v = {i: c for i, c in v.items() if c}
            if v:
                batch.append(v)
    for start in range(0, len(batch), 20000):
        chunk = batch[start:start + 20000]
        for v, m in zip(chunk, classes_of(chunk)):
            gen_store.append(("hodge", v))
            if m:
                f2_add(m, frozenset([len(gen_store) - 1]))
    total += len(batch)
    log(f"{fn}: {len(batch)} classes; dim of projected span so far {len(basisF)}")

rest, prov = f2_reduce(xi_mask)
result = {"q": q, "d": d, "rank_L0": rho, "coords": len(S), "short_classes": total, "dim_projected_span": len(basisF)}
if rest:
    # negative: find lambda over S with lambda . basis = 0 and lambda . xi = 1  (rest is the reduced xi)
    # lambda = indicator of the highest bit of rest, made orthogonal: solve small F_2 system
    nb = len(S)
    rowsB = [m for m, _ in basisF.values()] + [xi_mask]
    # find lambda in F_2^nb with <lambda, b> = 0 for b in span, <lambda, xi> = 1
    # Gaussian elimination on the transposed system
    M = [[(r >> j) & 1 for j in range(nb)] + [0] for r in rowsB[:-1]] + [[(xi_mask >> j) & 1 for j in range(nb)] + [1]]
    nr = len(M)
    pivcols, rr = [], 0
    for cidx in range(nb):
        p = next((i for i in range(rr, nr) if M[i][cidx]), None)
        if p is None:
            continue
        M[rr], M[p] = M[p], M[rr]
        for i in range(nr):
            if i != rr and M[i][cidx]:
                M[i] = [a ^ b for a, b in zip(M[i], M[rr])]
        pivcols.append(cidx)
        rr += 1
    if any(all(x == 0 for x in M[i][:nb]) and M[i][nb] for i in range(nr)):
        sys.exit("internal error: inconsistent certificate system")
    lam = [0] * nb
    for i, cidx in enumerate(pivcols):
        lam[cidx] = M[i][nb]
    # certificate y = sum lam_b * y_{S[b]} (exact rationals on the pivot coordinates)
    y = [flint.fmpq(0)] * rho
    for b in range(nb):
        if lam[b]:
            for k in range(rho):
                y[k] += 2 * Z[k, b]
    def ydot(v):
        s = flint.fmpq(0)
        for i, c in v.items():
            if i in pos:
                s += c * y[pos[i]]
        return s
    vx = ydot(xi)
    ok_xi = vx.q == 1 and int(vx.p) % 2 == 1
    bad = 0
    for kind, v in gen_store:
        val = ydot(v)
        if not (val.q == 1 and int(val.p) % 2 == 0):
            bad += 1
    for g in gens:
        val = ydot(dict(g))
        if not (val.q == 1 and int(val.p) % 2 == 0):
            bad += 1
    result.update({"verdict": "not_member", "certificate_checked": ok_xi and bad == 0, "bad_generators": bad})
    log(f"VERDICT: xi_{q} NOT in Lambda_{d}; dual certificate check: xi odd={ok_xi}, generators failing evenness={bad}")
    if args.cert:
        dens = 1
        for t in y:
            dens = dens * int(t.q) // gcd(dens, int(t.q))
        json.dump({"q": q, "d": d, "xi": xi_entries, "denominator": dens,
                   "functional": {str(piv[k] + 1): int(y[k].p) * (dens // int(y[k].q)) for k in range(rho) if y[k] != 0},
                   "convention": "y((a)_d) = functional[a]/denominator for 1 <= a < d/2, y((d-a)) = -y((a)), y((d/2)) = 0; y is an even integer on every generator of Lambda_d and odd on xi_q"},
                  open(args.cert, "w"))
else:
    # positive candidate: exact check of xi - sum(prov tuples) in L0
    resid = [0] * H
    for i, c in xi.items():
        resid[i] += c
    for gid in prov:
        for i, c in gen_store[gid][1].items():
            resid[i] -= c
    w = list(resid)
    okL0 = True
    for k in range(rho):
        c0 = piv[k]
        if w[c0] % basis[k][c0]:
            okL0 = False
            break
        f = w[c0] // basis[k][c0]
        if f:
            w = [x - f * y_ for x, y_ in zip(w, basis[k])]
    okL0 = okL0 and not any(w)
    result.update({"verdict": "member" if okL0 else "projection_collision_increase_coords", "tuples_used": len(prov)})
    log(f"VERDICT: candidate membership; exact L0 check of residual: {okL0}; tuples used {len(prov)}")
    if args.cert and okL0:
        json.dump({"q": q, "d": d, "xi": xi_entries, "tuples": [sorted(gen_store[g][1].items()) for g in prov]}, open(args.cert, "w"))
print("RESULT " + json.dumps(result), flush=True)
