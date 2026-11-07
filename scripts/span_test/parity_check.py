"""parity_check.py -- check the order-parity barrier invariants in many degrees.

For a prime p, phi_p(alpha) = number of entries of alpha whose order in Q/Z is a power of p, mod 2.
phi_p is additive, vanishes on linear tuples, and is compatible with lifts.  Conjecture (computationally
supported): phi_p vanishes on every standard tuple and every Hodge tuple of length <= 6 in every degree, for
p = 11, 13, 17.  Since phi_11(xi_44) = phi_13(xi_52) = phi_17(xi_51) = 1, this would show that no Z-combination
of linear, standard, surface and fourfold classes (joins, deletions, lifts) reaches xi_44, xi_52, xi_51.

Usage: python3 scripts/span_test/parity_check.py --p 11 --kmin 61 --kmax 120 [--procs 4] [--outdir parity_out]
       (checks the degrees d = p*k, kmin <= k <= kmax; checking (K/2, K] covers every multiple p*k, k <= K,
        because each such degree divides a checked one and lifting preserves everything)
"""
import argparse
import os
import subprocess
import sys
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))


def is_ppower(m, p):
    if m < p:
        return False
    while m % p == 0:
        m //= p
    return m == 1


def standard(dd):
    out = []
    for q in range(2, dd + 1):
        if dd % q or any(q % r == 0 for r in range(2, q)):
            continue
        k = dd // q
        for i in range(1, dd):
            if q >= 5 and i % q == 0:
                continue
            if k < 3 * gcd(i, k):
                continue
            ent = [i % dd, (i + k) % dd, (dd - 2 * i) % dd, k % dd] if q == 2 else [(i + j * k) % dd for j in range(q)] + [(dd - q * i) % dd]
            if 0 in ent:
                continue
            out.append(ent)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, required=True)
    ap.add_argument("--kmin", type=int, required=True)
    ap.add_argument("--kmax", type=int, required=True)
    ap.add_argument("--procs", type=int, default=os.cpu_count() or 4)
    ap.add_argument("--outdir", default="parity_out")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    exe = os.path.join(a.outdir, "hodge_mitm")
    if not os.path.exists(exe):
        subprocess.run(["gcc", "-O2", "-o", exe, os.path.join(HERE, "hodge_mitm.c")], check=True)
    p = a.p
    total_viol = 0
    for k in range(a.kmax, a.kmin - 1, -1):
        d = p * k
        viol = []
        # standard tuples of every divisor of d
        nstd = 0
        for dd in range(2, d + 1):
            if d % dd:
                continue
            for ent in standard(dd):
                nstd += 1
                if sum(1 for x in ent if is_ppower(dd // gcd(x, dd), p)) % 2:
                    viol.append(("standard", dd, ent))
        counts = {}
        for L in (4, 6):
            parts = [os.path.join(a.outdir, f"c_{d}_{L}_{r}.txt") for r in range(a.procs)]
            ps = [subprocess.Popen([exe, str(d), str(L), parts[r], str(r), str(a.procs)], stderr=subprocess.DEVNULL) for r in range(a.procs)]
            for pr in ps:
                if pr.wait():
                    sys.exit("hodge_mitm failed")
            n = 0
            for f in parts:
                with open(f) as fh:
                    for line in fh:
                        xs = [abs(int(x)) for x in line.split()]
                        if not xs:
                            continue
                        n += 1
                        if sum(1 for x in xs if is_ppower(d // gcd(x, d), p)) % 2:
                            viol.append(("hodge", L, xs))
                os.remove(f)
            counts[L] = n
        total_viol += len(viol)
        print(f"PARITY p={p} d={d} standard={nstd} classes4={counts[4]} classes6={counts[6]} violations={len(viol)}"
              + (f" first={viol[:3]}" if viol else ""), flush=True)
    print(f"PARITY_DONE p={p} k={a.kmin}..{a.kmax} total_violations={total_viol}", flush=True)


if __name__ == "__main__":
    main()
