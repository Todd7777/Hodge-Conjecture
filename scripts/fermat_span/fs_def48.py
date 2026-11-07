"""fs_def48.py -- cross-check of the exceptional tuples in the authors' exceptional_tuples.csv
against MMRV Definition 4.8 (primitive part = CRT product of half-systems; d-parts by the tau-recursion).

For each q we test:
 (P) the primitive part of the CSV tuple equals, modulo D_q, +- prod_{p in P, p | q} (1, mu_p, ..., mu_p^{phi(p)/2-1})_p
     for some choice of primitive roots mu_p (all choices tried);
 (R) for every d | q, 1 < d < q:  phi(d) xi_{q,d} == eps * sum_{e | d, e < d} tau_d(xi_{q,e}^{(q)})  in R_{q/d}/D_{q/d},
     with tau_d((a)_q) = phi(q)/phi(q') * g_{q,d} . (a')_{q/d},  g_{q,d} = prod_{p | d', p !| q/d} ([1] + [s p^{x}]),
     q' = q/gcd(q,a), d' = d/gcd(q,a), a' = a/gcd(q,a); conventions eps in {+1,-1}, s in {+1,-1}, x in {-1,+1}.
     The literal reading of the paper is eps = +1, s = -1, x = -1.
Usage: python3 fs_def48.py [q ...]
"""
import sys
from itertools import product
from math import gcd

import fs_lattice as L


def phi(n):
    return sum(1 for t in range(1, n + 1) if gcd(t, n) == 1)


def parts(tup, q):
    """d-parts: {d: list of residues a/d mod q/d} for entries a with gcd(a, q) = d."""
    out = {}
    for a in tup:
        g = gcd(a, q)
        out.setdefault(g, []).append(a // g)
    return out


def foldm(vec_dict, m):
    """element of R_m given as {residue: coeff} -> folded vector in R_m/D_m (length floor((m-1)/2))."""
    h = (m - 1) // 2
    x = [0] * h
    for a, c in vec_dict.items():
        a %= m
        if a == 0:
            raise ValueError("zero entry")
        if 2 * a < m:
            x[a - 1] += c
        elif 2 * a > m:
            x[m - a - 1] -= c
    return x


def tau(a, q, d, s, xexp):
    """tau_d((a)_q) as {residue mod q/d: coeff}."""
    g = gcd(q, a)
    qp, dp, ap = q // g, d // g, a // g
    m = q // d
    fac = phi(q) // phi(qp)
    assert phi(q) % phi(qp) == 0
    elems = {ap % m: 1}
    for p in L.prime_divisors(dp) if dp > 1 else []:
        if m % p == 0:
            continue
        pinv = pow(p, -1, m) if m > 1 else 0
        mult = (s * (pinv if xexp == -1 else p)) % m
        new = {}
        for r, c in elems.items():
            new[r] = new.get(r, 0) + c
            r2 = (r * mult) % m
            new[r2] = new.get(r2, 0) + c
        elems = new
    return {r: fac * c for r, c in elems.items()}


def primitive_roots(p):
    if p == 4:
        return [3]
    return [g for g in range(2, p) if all(pow(g, (p - 1) // r, p) != 1 for r in L.prime_divisors(p - 1))]


def half_system(p, mu):
    if p == 4:
        return [1]
    return [pow(mu, j, p) for j in range((p - 1) // 2)]


def crt(residues, moduli):
    x, M = 0, 1
    for r, m in zip(residues, moduli):
        # solve x' = x mod M, x' = r mod m
        t = ((r - x) * pow(M, -1, m)) % m
        x, M = x + M * t, M * m
    return x % M


def check_primitive(q, xi):
    P = L.P_elements(q)
    prim = foldm({a: 1 for a in []}, q)
    pr = {}
    for a in xi:
        if gcd(a, q) == 1:
            pr[a] = pr.get(a, 0) + 1
    target = foldm(pr, q)
    found = []
    for mus in product(*[primitive_roots(p) for p in P]):
        elems = {}
        for combo in product(*[half_system(p, mu) for p, mu in zip(P, mus)]):
            c = crt(list(combo), P)
            elems[c] = elems.get(c, 0) + 1
        v = foldm(elems, q)
        if v == target:
            found.append(("+", dict(zip(P, mus))))
        if [-x for x in v] == target:
            found.append(("-", dict(zip(P, mus))))
    return found


def check_recursion(q, xi):
    pts = parts(xi, q)
    lifted = {e: [e * r for r in pts.get(e, [])] for e in L.divisors(q)}   # e-part lifted to R_q
    results = {}
    for eps, s, xexp in product((1, -1), (1, -1), (-1, 1)):
        ok = True
        for d in L.divisors(q):
            if d == 1 or d == q:
                continue
            m = q // d
            if m < 2:
                continue
            rhs = {}
            for e in L.divisors(d):
                if e == d:
                    continue
                for a in lifted[e]:
                    for r, c in tau(a, q, d, s, xexp).items():
                        if r % m == 0:
                            continue
                        rhs[r] = rhs.get(r, 0) + eps * c
            lhs = {}
            for r in pts.get(d, []):
                lhs[r % m] = lhs.get(r % m, 0) + phi(d)
            if m <= 2:
                continue                                  # R_2/D_2 = 0
            if foldm(lhs, m) != foldm(rhs, m):
                ok = False
                break
        results[(eps, s, xexp)] = ok
    return results


def main(qs):
    X = L.read_tuples()
    for q in qs:
        xi = X[q]
        prim = check_primitive(q, xi)
        rec = check_recursion(q, xi)
        good = [k for k, v in rec.items() if v]
        print(f"q={q} xi={xi} Hodge={L.is_hodge(xi, q)} primitive-part matches: {prim[:3]}{' ...' if len(prim) > 3 else ''} "
              f"| recursion holds for (eps,s,x) in {good}")


if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]] or [12, 15, 20, 21, 28, 33, 35, 39, 44, 51, 52, 55, 57, 65, 68])
