"""fs_invariant.py -- search for Galois-invariant dual certificates.

Certificates are required to vanish on the conjugates of EVERY other xi_q' (q' in Q, q' | d, available in the CSV),
not only on the certified ones.  A G_d-invariant mod-2 functional on R_d is chi_S(alpha) = #{entries a of alpha with gcd(a, d) in S} mod 2 for a set
S of divisors g of d with g != d, g != d/2 (the G_d-orbits on (Z/d)-{0} are the sets {a : gcd(a,d) = g}; the orbit
{d/2} must be excluded because eps_d is a generator).  For a finished run (q, d) we list every S such that chi_S
vanishes on all lifted standard tuples, on the known xi_q', and on one witness of every class of reduced Hodge tuples
of length <= 6 (enough, because chi_S then factors through K_d/L0 on B_d), and is odd on xi_q.
Usage: python3 fs_invariant.py q d [q d ...]
"""
import json
import os
import sys
from itertools import combinations
from math import gcd

import fs_lattice as L

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "results", "fermat_span")


def invariant_certificates(q, d):
    X = L.read_tuples()
    run = json.load(open(os.path.join(OUT, f"run_q{q}_d{d}.json")))
    gs = [g for g in L.divisors(d) if g != d and 2 * g != d]
    tests = [t for _, t in L.standard_gens(d, "div")]
    # all OTHER available exceptional tuples (not only the certified ones): the stronger statement
    tests += [L.lift(X[qp], qp, d) for qp in run["Q_divisors"] if qp != q and qp in X]
    tests += [tuple(s["witness"]) for s in run["signatures"]]
    target = L.lift(X[q], q, d)
    # chi_S(v) = sum_{g in S} n_g(v) mod 2, n_g(v) = #entries with gcd = g: linear algebra over F_2 in the
    # indicator vector of S.
    def gvec(tup):
        v = 0
        for a in tup:
            g = gcd(a, d)
            if g in gs:
                v ^= 1 << gs.index(g)
        return v
    rows = [gvec(t) for t in tests]
    tv = gvec(target)
    sols = []
    n = len(gs)
    if n <= 22:
        for m in range(1 << n):
            if bin(m & tv).count("1") % 2 == 1 and all(bin(m & r).count("1") % 2 == 0 for r in rows):
                sols.append(sorted(gs[i] for i in range(n) if m >> i & 1))
    return gs, sols


def describe(q, d):
    gs, sols = invariant_certificates(q, d)
    orders = [sorted(d // g for g in S) for S in sols]
    return gs, orders


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "all":
        import glob
        runs = sorted((json.load(open(f))["q"], json.load(open(f))["d"]) for f in glob.glob(os.path.join(OUT, "run_q*_d*.json")))
        runs = [(q, d) for q, d in runs if q in (44, 51, 52, 68)]
    else:
        a = [int(x) for x in args]
        runs = list(zip(a[::2], a[1::2]))
    for q, d in runs:
        gs, orders = describe(q, d)
        best = sorted(orders, key=lambda o: (len(o), o))[:4]
        print(f"q={q} d={d}: {len(orders)} Galois-invariant certificates (as sets of element orders); smallest: {best}", flush=True)
