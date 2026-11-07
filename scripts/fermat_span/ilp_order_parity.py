"""ilp_order_parity.py -- checks for section 7 of results/fermat_span/ilp.md.
(1) psi_p (parity of the number of entries of exact order p) on every generator of D_d + S~'_d and on
    every xi_{q'}, for the lifted degrees d <= 1300 of q = 44 (p=11), 52 (p=13), 51 (p=17), 68 (p=17);
(2) the Legendre-character identity for p = 11 (lambda odd since 11 = 3 mod 4):
      sum_{a: 11 | ord a} lambda(u_a) / phi(k_a) * prod_{l | k_a} (1 - lambda(l)) = 0
    (ord a = 11 k_a, a = (d/ord a) w, u_a = w mod 11) on Hodge tuples found by the exhaustive search.
Exact arithmetic (fractions).  Output: results/fermat_span/ilp_order_parity.txt"""
import os
from fractions import Fraction
from math import gcd, lcm

import ilp_core as C

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                                    "results", "fermat_span", "ilp_order_parity.txt"))


def order(a, d):
    return d // gcd(a % d, d)


def psi(t, d, p):
    return sum(1 for a in t if order(a, d) == p) % 2


def phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def legendre(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


def lam_sum(t, d, p=11):
    s = Fraction(0)
    for a in t:
        n = order(a, d)
        if n % p:
            continue
        k = n // p
        assert k % p, "p^2 | ord"
        w = (a % d) // (d // n)
        f = Fraction(legendre(w, p), phi(k))
        for l in C.prime_divisors(k):
            f *= (1 - legendre(l, p))
        s += f
    return s


def main():
    X = C.read_tuples(C.EXC_CSV)
    lines = []
    for q, p in ((44, 11), (52, 13), (51, 17), (68, 17)):
        ds = sorted({lcm(q, e) for e in list(range(2, 31)) + [33, 34, 35, 38, 39, 46, 51, 55, 57, 58]})
        ds = [d for d in ds if d <= 1300]
        for d in ds:
            gens = C.generator_tuples(d)
            odd_gens = sum(psi(g, d, p) for g in gens)
            vals = {qq: psi(C.lift(X[qq], qq, d), d, p) for qq in X if d % qq == 0}
            lines.append("q=%d p=%d d=%d: generators with odd psi_p: %d / %d; psi_p(xi_q)=%d; other xi with psi_p=1: %s"
                         % (q, p, d, odd_gens, len(gens), vals[q], sorted(k for k, v in vals.items() if v and k != q)))
    # (2) Legendre identity on Hodge tuples: reps of xi_44 and all short tuples at d=132, 220, 660
    import ilp_classes as CL
    for d in (44, 132, 220, 660):
        sp = CL.ClassSpace(d, check=False)
        res, _ = sp.short_search(7, nthreads=1)
        n = bad = 0
        for lab, byL in res.items():
            for L, (cnt, exs) in byL.items():
                for t in exs:
                    n += 1
                    if lam_sum(t, d) != 0:
                        bad += 1
        lines.append("d=%d: Legendre identity checked on %d example Hodge tuples (all classes, L<=7): failures %d" % (d, n, bad))
    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
