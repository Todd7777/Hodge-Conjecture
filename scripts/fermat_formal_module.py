#!/usr/bin/env python3
"""Formal-module (Aoki) lattice computations for the open Fermat degrees 44, 51, 52.

Companion to docs/attacks/17-fermat-open-cases.md.  New file; uses nothing from the repository except the
orbit lists in results/fermat_fast_<n>_<m>.txt.  Requires python-flint (exact HNF/SNF over Z).

Notation (Aoki 1983; Miranda-Movasati-Rufino-Villaflor 2026, section 4):
  R_d   = Z^{d-1}, basis e_a (a = 1..d-1); a tuple (a_1..a_L) is the vector sum_i e_{a_i}.
  B_d   = {v in R_d : sum_a v_a (t a mod d) = sum_a v_a a  for all units t}   (Hodge tuples; saturated).
  D_d   = span{e_a + e_{d-a}} (+ e_{d/2} if d even)            (characters of X^0 = points).
  B2_d  = span of Hodge 4-tuples (surface characters), B4_d = Hodge 6-tuples (fourfold characters).
  S_d   = Aoki's standard characters s_{p,i} of degree d and lifts from divisors (p prime, k = d'/p >= 3).
Commands:
  structure d            lattice structure for d in {44, 51, 52}
  orbits d FILE          classify the orbit representatives listed in FILE
  certificates           verify the explicit join/deletion certificates used in the attack file
  lift D q ENUM          lifted obstruction in degree D (multiple of q); ENUM = compiled
                         scripts/fermat_hodge_tuples.c (enumerates Hodge 4- and 6-tuples of degree D)
  inherited d FILE four  splittings of each orbit into Hodge factors (rung (a) of the attack)
  chi                    the character sums f_q(a) used in Proposition 5.1
  aoki_support           characters admissible for the class of the Aoki-Shioda variety A_(11,44)
  all ENUM               everything (this is what was run for the attack file)
"""
import subprocess
import sys
import time
from collections import Counter
from math import gcd

import flint

LAMBDA = {44: ({11: 1, 33: -1}), 51: ({17: 1, 34: -1}), 52: ({1: 1, 25: 1, 27: -1, 51: -1})}
EXCEPTIONAL = {44: (1, 5, 13, 22, 24, 33, 37, 41), 51: (1, 4, 7, 19, 24, 34, 37, 40, 43, 46),
               52: (1, 4, 17, 21, 29, 41, 45, 50)}


def units(d):
    return [t for t in range(1, d) if gcd(t, d) == 1]


def sorted_tuples_with_sum(length, total, lo, hi):
    if length == 0:
        if total == 0:
            yield ()
        return
    for a in range(max(lo, total - (length - 1) * hi), min(hi, total // length) + 1):
        for rest in sorted_tuples_with_sum(length - 1, total - a, a, hi):
            yield (a,) + rest


def is_hodge_tuple(t, d):
    s = sum(x % d for x in t)
    return all(sum((u * x) % d for x in t) == s for u in units(d))


def hodge_tuples(d, length, enum=None):
    """All sorted Hodge characters of the given (even) length and degree d."""
    if enum:
        out = subprocess.run([enum, str(d), str(length)], capture_output=True, text=True, check=True).stdout
        return [tuple(map(int, line.split())) for line in out.splitlines() if line.strip()]
    us = [t for t in units(d) if 1 < t <= d - t]
    tab = {t: [(t * a) % d for a in range(d)] for t in us}
    target = (length // 2) * d
    return [al for al in sorted_tuples_with_sum(length, target, 1, d - 1)
            if all(sum(tab[t][a] for a in al) == target for t in us)]


def vec(tup, d):
    v = [0] * (d - 1)
    for a in tup:
        a %= d
        assert a != 0, tup
        v[a - 1] += 1
    return v


def hnf_rows(rows, ncols):
    if not rows:
        return []
    M = flint.fmpz_mat(rows).hnf()
    out = []
    for i in range(M.nrows()):
        r = [int(M[i, j]) for j in range(ncols)]
        if any(r):
            out.append(r)
    return out


def hodge_lattice(d):
    """Z-basis (HNF) of B_d as the integer kernel of K, K[t][a] = (t a mod d) - a."""
    n = d - 1
    K = [[(t * a) % d - a for a in range(1, d)] for t in units(d) if t != 1]
    s = len(K)
    A = [[K[j][i] for j in range(s)] + [1 if k == i else 0 for k in range(n)] for i in range(n)]
    H = flint.fmpz_mat(A).hnf()
    ker = []
    for i in range(H.nrows()):
        row = [int(H[i, j]) for j in range(s + n)]
        if not any(row[:s]) and any(row[s:]):
            ker.append(row[s:])
    return hnf_rows(ker, n), K


def pivots(H):
    return [next(j for j, x in enumerate(r) if x) for r in H]


def member(H, v):
    v = list(v)
    for r in H:
        p = next(j for j, x in enumerate(r) if x)
        if v[p] % r[p]:
            return False
        q = v[p] // r[p]
        if q:
            v = [a - q * b for a, b in zip(v, r)]
    return not any(v)


def D_gens(d):
    g = [vec((a, d - a), d) for a in range(1, d) if a < d - a]
    if d % 2 == 0:
        g.append(vec((d // 2,), d))
    return g


def is_prime(p):
    return p > 1 and all(p % q for q in range(2, int(p ** 0.5) + 1))


def standard_chars(d):
    """Aoki standard characters of degree d' | d (lifted to degree d), d' = p k, k >= 3, i a unit mod d'."""
    out = []
    for dp in range(2, d + 1):
        if d % dp:
            continue
        for p in range(2, dp + 1):
            if dp % p or not is_prime(p) or dp // p < 3:
                continue
            k = dp // p
            for i in units(dp):
                tup = (i, k + i, dp - 2 * i, k) if p == 2 else tuple(i + j * k for j in range(p)) + (-p * i,)
                out.append(tuple((x % dp) * (d // dp) for x in tup))
    return out


def index_in(Bb, H):
    """[B : L] for L (HNF rows H) a full-rank sublattice of B (HNF rows Bb)."""
    pB, pH = pivots(Bb), pivots(H)
    assert len(Bb) == len(H) and pB == pH
    num = den = 1
    for i in range(len(H)):
        num *= H[i][pH[i]]
        den *= Bb[i][pB[i]]
    assert num % den == 0
    return num // den


def coords(Bb, v):
    piv = pivots(Bb)
    c, v = [0] * len(Bb), list(v)
    for i, r in enumerate(Bb):
        q, rem = divmod(v[piv[i]], r[piv[i]])
        assert rem == 0
        c[i] = q
        if q:
            v = [a - q * b for a, b in zip(v, r)]
    assert not any(v)
    return c


def quotient_invariants(Bb, H):
    """Invariant factors of B/L and the free rank, L = row span of H inside B."""
    X = flint.fmpz_mat([coords(Bb, v) for v in H])
    snf = X.snf()
    diag = [int(snf[i, i]) for i in range(min(snf.nrows(), snf.ncols()))]
    return len(Bb) - len(H), [x for x in diag if x not in (0, 1)]


def lam(tup, d):
    c = Counter(a % d for a in tup)
    return sum(w * c[a] for a, w in LAMBDA[d].items())


# ---------------------------------------------------------------------------------------------- mod-2 machinery
def mask(tup):
    m = 0
    for a in tup:
        m ^= 1 << (a - 1)
    return m


def f2_insert(basis, m):
    while m:
        lb = m.bit_length() - 1
        if lb in basis:
            m ^= basis[lb]
        else:
            basis[lb] = m
            return True
    return False


def f2_reduce(basis, m):
    while m:
        lb = m.bit_length() - 1
        if lb not in basis:
            return m
        m ^= basis[lb]
    return 0


def rowmask(r):
    m = 0
    for j, x in enumerate(r):
        if x & 1:
            m |= 1 << j
    return m


# ---------------------------------------------------------------------------------------------- commands
def cmd_structure(d, enum=None):
    n = d - 1
    t0 = time.time()
    Bb, K = hodge_lattice(d)
    r = len(Bb)
    B2 = hodge_tuples(d, 4, enum)
    B4 = hodge_tuples(d, 6, enum)
    D = D_gens(d)
    S = standard_chars(d)
    for t in S:
        assert is_hodge_tuple(t, d)
    print(f"## structure d={d}: rank B_d = {r}; #sorted surface chars {len(B2)}, fourfold chars {len(B4)}, "
          f"standard chars {len(S)}")
    LKF = hnf_rows(D + [vec(x, d) for x in B2], n)
    free, tors = quotient_invariants(Bb, LKF)
    print(f"   B/(D+B2): free rank {free}, torsion invariant factors {tors}")
    bad = [x for x in B2 + B4 if lam(x, d)]
    print(f"   lambda_{d} = {LAMBDA[d]}: vanishes on D: {all(lam((a, d - a), d) == 0 for a in range(1, d))}"
          f" and on every surface and fourfold character: {not bad}")
    print(f"   lambda_{d}(alpha_{d}) = {lam(EXCEPTIONAL[d], d)} for alpha_{d} = {EXCEPTIONAL[d]};"
          f" alpha_{d} Hodge: {is_hodge_tuple(EXCEPTIONAL[d], d)}")
    L4 = hnf_rows(LKF + [vec(x, d) for x in B4], n)
    print(f"   rank(D+B2+B4) = {len(L4)} (= rank(D+B2) = {len(LKF)})")
    LS = hnf_rows(D + [vec(x, d) for x in S], n)
    LS2 = hnf_rows(LS + [vec(x, d) for x in B2 + B4], n)
    two = all(member(LS, [2 * x for x in b]) for b in Bb)
    print(f"   [B : D+S] = {index_in(Bb, LS)}, [B : D+S+B2+B4] = {index_in(Bb, LS2)}, 2B in D+S: {two}")
    print(f"   lambda on standard chars: {sorted(set(lam(t, d) for t in S))}  ({time.time() - t0:.1f}s)")
    return Bb, LKF, LS2


def read_orbits(path):
    out = []
    for line in open(path):
        p = line.split()
        if len(p) >= 3 and all(x.isdigit() for x in p):
            out.append(tuple(map(int, p)))
    return out


def cmd_orbits(d, path, enum=None, quiet=False):
    n = d - 1
    Bb, _ = hodge_lattice(d)
    D = D_gens(d)
    B2 = [vec(x, d) for x in hodge_tuples(d, 4, enum)]
    LKF = hnf_rows(D + B2, n)
    LA = hnf_rows(LKF + [vec(x, d) for x in standard_chars(d)], n)
    orbs = read_orbits(path)
    stats = Counter()
    print(f"## orbits in {path}: {len(orbs)}")
    for al in orbs:
        v = vec(al, d)
        a, b, l = member(LKF, v), member(LA, v), lam(al, d)
        assert a == (l == 0) and b == (l % 2 == 0)
        stats[(l, a, b)] += 1
        if not quiet:
            print(f"   {al}  lambda={l:+d}  in D+B2: {a}  in D+S+B2: {b}")
    print("   summary (lambda, in D+B2, in D+S+B2) -> count:", dict(stats))


CERTS = [  # (degree, left-hand characters, right-hand characters): concatenation of left ~ concatenation of right
    (44, [(1, 12, 23, 26, 34, 36), (4, 20, 21, 43), (8, 18, 22, 40), (10, 22, 24, 32)],
     [(1, 43), (4, 40), (8, 36), (10, 34), (12, 32), (18, 26), (20, 24), (21, 23), (22, 22)]),
    (44, [(1, 6, 17, 23, 26, 28, 36, 39), (4, 20, 21, 43), (5, 22, 27, 34), (8, 18, 22, 40), (10, 16, 24, 38)],
     [(1, 43), (4, 40), (5, 39), (6, 38), (8, 36), (10, 34), (16, 28), (17, 27), (18, 26), (20, 24), (21, 23),
      (22, 22)]),
    (52, [(1, 14, 27, 30, 40, 44), (4, 24, 25, 51), (8, 22, 26, 48), (12, 26, 28, 38)],
     [(1, 51), (4, 48), (8, 44), (12, 40), (14, 38), (22, 30), (24, 28), (25, 27), (26, 26)]),
    (52, [(1, 7, 20, 27, 30, 33, 44, 46), (4, 24, 25, 51), (6, 26, 32, 40), (8, 22, 26, 48), (12, 19, 28, 45)],
     [(1, 51), (4, 48), (6, 46), (7, 45), (8, 44), (12, 40), (19, 33), (20, 32), (22, 30), (24, 28), (25, 27),
      (26, 26)]),
    (44, [(1, 4, 5, 13, 33, 37, 41, 42), (2, 22, 24, 40)], [(1, 5, 13, 22, 24, 33, 37, 41), (2, 42), (4, 40)]),
    (44, [(1, 5, 8, 9, 33, 37, 41, 42), (2, 24, 26, 36), (13, 18, 22, 35)],
     [(1, 5, 13, 22, 24, 33, 37, 41), (2, 42), (8, 36), (9, 35), (18, 26)]),
    (44, [(1, 5, 9, 16, 29, 33, 41, 42), (2, 22, 24, 40), (4, 13, 35, 36), (8, 15, 28, 37)],
     [(1, 5, 13, 22, 24, 33, 37, 41), (2, 42), (4, 40), (8, 36), (9, 35), (15, 29), (16, 28)]),
    (44, [(1, 5, 9, 24, 26, 33, 37, 41), (13, 18, 22, 35)], [(1, 5, 13, 22, 24, 33, 37, 41), (9, 35), (18, 26)]),
    (44, [(1, 5, 12, 13, 33, 34, 37, 41), (10, 22, 24, 32)], [(1, 5, 13, 22, 24, 33, 37, 41), (10, 34), (12, 32)]),
]


def cmd_certificates():
    print("## certificates: each line is an identity  alpha * gamma_1 * ... ~ delta_1 * ... (multisets)")
    for d, lhs, rhs in CERTS:
        L = Counter(a for t in lhs for a in t)
        R = Counter(a for t in rhs for a in t)
        kinds = []
        for t in lhs[1:] + rhs:
            assert sum(t) % d == 0 and is_hodge_tuple(t, d), t
            kinds.append(len(t))
        ok = (L == R) and is_hodge_tuple(lhs[0], d)
        print(f"   d={d}: {' * '.join(map(str, lhs))}  ~  {' * '.join(map(str, rhs))}   valid: {ok};"
              f" auxiliary lengths {sorted(set(kinds))}")
        assert ok


def cmd_lift(D, q, enum):
    """Is the lift of the exceptional character of degree q in D_D + S_D + B2_D + B4_D (D a multiple of q)?"""
    t0 = time.time()
    n = D - 1
    Bb, _ = hodge_lattice(D)
    r = len(Bb)
    L0 = hnf_rows(D_gens(D) + [vec(x, D) for x in standard_chars(D)], n)
    idx = index_in(Bb, L0)
    basis = {}
    for row in L0:
        f2_insert(basis, rowmask(row))
    k0 = r - len(basis)
    assert idx == 2 ** k0 and all(member(L0, [2 * x for x in b]) for b in Bb)   # B/(D+S) elementary abelian
    dims = [k0]
    for L in (4, 6):
        for tup in hodge_tuples(D, L, enum):
            f2_insert(basis, mask(tup))
        dims.append(r - len(basis))
    k = D // q
    tgt = tuple(k * a for a in EXCEPTIONAL[q])
    inside = f2_reduce(basis, mask(tgt)) == 0
    print(f"## lift D={D} (q={q}): rank B={r}; dim_F2 B/(D+S) = {k0} ([B:D+S]={idx}); after +B2: {dims[1]}; "
          f"after +B4: {dims[2]}; lift of alpha_{q} in D+S+B2+B4: {inside}  ({time.time() - t0:.1f}s)")


# ---------------------------------------------------------------------------------------------- further checks
def canon(t, d):
    return min(tuple(sorted((u * x) % d for x in t)) for u in units(d))


def splittings(alpha, d):
    """All splittings of alpha into two Hodge characters by the operations (N), (Z) of docs/04, section 4.2."""
    k = len(alpha)
    for m in range(1, 1 << (k - 1)):
        S = [0] + [i + 1 for i in range(k - 1) if m >> i & 1]
        T = [i for i in range(k) if i not in S]
        aS, aT = [alpha[i] for i in S], [alpha[i] for i in T]
        c = sum(aS) % d
        if c == 0 and len(S) % 2 == 0 and len(S) >= 2 and len(T) >= 2 and is_hodge_tuple(aS, d):
            yield "Z", tuple(sorted(aS)), tuple(sorted(aT))
        if c and len(S) % 2 == 1 and len(S) >= 3 and len(T) >= 3:
            b, g = tuple(sorted(aS + [(-c) % d])), tuple(sorted(aT + [c]))
            if is_hodge_tuple(b, d) and is_hodge_tuple(g, d):
                yield "N", b, g


def cmd_inherited(d, path, four):
    """For each orbit: does a splitting exist whose factors are decomposable or in the orbit of `four`?"""
    sys.path.insert(0, ".")
    from hodge.fermat import is_decomposable
    cf = canon(four, d)
    print(f"## inherited check for {path}; fourfold orbit {four} (canonical {cf})")
    for al in read_orbits(path):
        good = None
        for typ, b, g in splittings(al, d):
            facs = [b, g]
            if all(len(x) <= 4 or canon(x, d) == cf or is_decomposable(x, d) for x in facs):
                good = (typ, b, g)
                if any(len(x) == 6 and canon(x, d) == cf for x in facs):
                    break
        print(f"   {al}: {'splitting ' + str(good) if good else 'no Hodge splitting (primitive)'}")


def cmd_chi():
    """f_q(a) = sum_t chi_q(t) <t a/d>; for Hodge alpha, sum_i f_q(a_i) = 0 (proof of Proposition 5.1)."""
    from fractions import Fraction
    for d, q in ((44, 4), (51, 3), (52, 4)):
        ch = {4: {1: 1, 3: -1}, 3: {1: 1, 2: -1}}[q]
        f = {a: sum(ch.get(t % q, 0) * Fraction((t * a) % d, d) for t in units(d)) for a in range(1, d)}
        unit_ok = all(f[a] == f[1] * ch.get(a % q, 0) for a in units(d))
        other = {a: str(v) for a, v in f.items() if v and gcd(a, d) != 1}
        print(f"## chi_{q}, d={d}: f(unit a) = ({f[1]})*chi_{q}(a): {unit_ok}; nonzero f on non-units: {other}")


def cmd_aoki_support():
    """Characters of X^10_44 invariant under the diagonal stabilizer of A_(11,44): 11 entries in one class r mod 4
    and last entry 11*(-r mod 4).  Report lambda_44 on the Hodge ones."""
    from itertools import combinations_with_replacement
    d = 44
    for r in (1, 2, 3):
        last = (11 * ((-r) % 4)) % d
        vals = Counter()
        for c in combinations_with_replacement([a for a in range(1, d) if a % 4 == r], 11):
            t = c + (last,)
            if sum(t) % d == 0 and is_hodge_tuple(t, d):
                vals[lam(t, d)] += 1
        print(f"## A_(11,44) admissible characters, class {r} mod 4, last entry {last}: lambda -> count {dict(vals)}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd == "structure":
        cmd_structure(int(sys.argv[2]))
    elif cmd == "orbits":
        cmd_orbits(int(sys.argv[2]), sys.argv[3])
    elif cmd == "certificates":
        cmd_certificates()
    elif cmd == "lift":
        cmd_lift(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    elif cmd == "inherited":
        cmd_inherited(int(sys.argv[2]), sys.argv[3], tuple(map(int, sys.argv[4].split(","))))
    elif cmd == "chi":
        cmd_chi()
    elif cmd == "aoki_support":
        cmd_aoki_support()
    elif cmd == "all":
        enum = sys.argv[2] if len(sys.argv) > 2 else None
        R = "results/fermat_fast_{}_{}.txt"
        for d in (44, 52, 51):
            cmd_structure(d, enum)
        cmd_orbits(44, R.format(6, 44), enum)
        cmd_orbits(52, R.format(6, 52), enum)
        cmd_orbits(51, R.format(8, 51), enum)
        cmd_orbits(44, R.format(8, 44), enum, quiet=True)
        cmd_orbits(52, R.format(8, 52), enum, quiet=True)
        cmd_certificates()
        cmd_chi()
        cmd_inherited(44, R.format(6, 44), (1, 12, 23, 26, 34, 36))
        cmd_inherited(52, R.format(6, 52), (1, 14, 27, 30, 40, 44))
        cmd_aoki_support()
        if enum:
            for D, q in ((88, 44), (132, 44), (176, 44), (220, 44), (104, 52), (156, 52), (102, 51), (153, 51)):
                cmd_lift(D, q, enum)
    else:
        print(__doc__)
