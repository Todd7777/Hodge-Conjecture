import json, sys
from math import gcd
exec(open("oi_solve.py").read().split("basis = {}")[0].replace("N = int(sys.argv[1])", f"N = {int(sys.argv[1])}"))
n = len(orders)
rows = [sum(1 << idx[m] for m in s) for s in cons]
# RREF over F_2 with columns = orders
piv = {}
for r in rows:
    for c, row in piv.items():
        if (r >> c) & 1: r ^= row
    if r:
        c = r.bit_length() - 1
        for c2 in list(piv):
            if (piv[c2] >> c) & 1: piv[c2] ^= r
        piv[c] = r
free = [c for c in range(n) if c not in piv]
null = []
for f in free:
    v = 1 << f
    for c, row in piv.items():
        if (row >> f) & 1: v |= 1 << c
    null.append(v)
print(f"N={N}: null space dimension {len(null)}")
def sup(v): return [orders[i] for i in range(n) if (v >> i) & 1]
for v in null: print("  phi supported on orders", sup(v))
for q in (44, 51, 52):
    t = sum(1 << idx[m] for m in profile(TUP[q], q))
    good = [v for v in null if bin(v & t).count("1") % 2]
    print(f"xi_{q}: {len(good)} basis invariants detect it; smallest support:", min((sup(v) for v in good), key=len) if good else None)
