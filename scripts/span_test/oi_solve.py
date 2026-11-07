"""Solve for order-parity invariants phi using cached constraints from degrees 3..N (oicache/d*.json)."""
import json, sys
from math import gcd
N = int(sys.argv[1])
TUP = {12: [1, 4, 9, 10], 15: [1, 7, 10, 12], 20: [1, 6, 8, 17, 18], 21: [1, 10, 15, 16], 28: [1, 8, 9, 10, 12, 17, 21, 22, 26],
       33: [1, 4, 13, 16, 19, 22, 27, 30], 35: [1, 2, 16, 17, 21, 22, 30, 31], 39: [1, 4, 15, 16, 19, 21, 27, 28, 30, 34],
       44: [1, 5, 6, 13, 14, 18, 20, 33, 34, 37, 41, 42], 51: [1, 10, 13, 18, 22, 28, 34, 37, 43, 49],
       52: [1, 10, 14, 17, 18, 21, 22, 24, 29, 41, 45, 46, 50], 55: [1, 2, 12, 15, 16, 26, 27, 30, 35, 37, 41, 45, 46, 52],
       57: [1, 4, 7, 9, 13, 16, 28, 33, 40, 45, 46, 51, 52, 54], 68: [1, 4, 5, 9, 12, 13, 14, 37, 38, 42, 45, 46, 49, 50, 58, 61, 62, 66]}
KNOWN = [12, 15, 20, 21, 28, 33, 35, 39, 55, 57]
def profile(entries, deg):
    odd = set()
    for a in entries:
        m = deg // gcd(a, deg)
        if m > 2: odd ^= {m}
    return frozenset(odd)
cons = set()
for d in range(3, N + 1):
    for c in json.load(open(f"oicache/d{d}.json")): cons.add(frozenset(c))
for k in KNOWN: cons.add(profile(TUP[k], k))
cons.discard(frozenset())
orders = sorted({m for s in cons for m in s} | {m for q in TUP for m in profile(TUP[q], q)})
idx = {m: i for i, m in enumerate(orders)}
basis = {}
for s in cons:
    mask = sum(1 << idx[m] for m in s)
    while mask:
        h = mask.bit_length() - 1
        if h in basis: mask ^= basis[h]
        else: basis[h] = mask; break
print(f"N={N}: {len(cons)} constraints over {len(orders)} orders, rank {len(basis)}; free directions {len(orders) - len(basis)}")
def reduce(mask):
    while mask:
        h = mask.bit_length() - 1
        if h in basis: mask ^= basis[h]
        else: return mask
    return 0
for q in (44, 51, 52, 68):
    r = reduce(sum(1 << idx[m] for m in profile(TUP[q], q)))
    print(f"  xi_{q}: profile {sorted(profile(TUP[q], q))} -> order-parity obstruction {'SURVIVES' if r else 'killed'} for all degrees <= {N}")
# orders not in the constraint span as single coordinates (candidate 'free' orders)
free = [m for m in orders if reduce(1 << idx[m])]
print("orders whose indicator is outside the constraint span (first 40):", free[:40])
