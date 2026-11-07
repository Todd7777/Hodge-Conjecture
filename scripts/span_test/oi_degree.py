import os, subprocess, sys, json
from math import gcd
d = int(sys.argv[1])
def profile(entries, deg):
    odd = set()
    for a in entries:
        m = deg // gcd(a, deg)
        if m > 2: odd ^= {m}
    return sorted(odd)
def standard(dd):
    out = []
    for p in range(2, dd + 1):
        if dd % p or any(p % r == 0 for r in range(2, p)): continue
        k = dd // p
        for i in range(1, dd):
            if p >= 5 and i % p == 0: continue
            if k < 3 * gcd(i, k): continue
            ent = [i % dd, (i + k) % dd, (dd - 2 * i) % dd, k % dd] if p == 2 else [(i + j * k) % dd for j in range(p)] + [(dd - p * i) % dd]
            if 0 in ent: continue
            out.append(ent)
    return out
cons = set()
for ent in standard(d): cons.add(tuple(profile(ent, d)))
here = os.path.dirname(os.path.abspath(__file__))
for L in (4, 6):
    f = os.path.join(here, f"oicache/tmp_{d}_{L}.txt")
    subprocess.run([os.path.join(here, "hodge_mitm"), str(d), str(L), f], stderr=subprocess.DEVNULL, check=True)
    for line in open(f): cons.add(tuple(profile([abs(int(x)) for x in line.split()], d)))
    os.remove(f)
cons.discard(())
json.dump(sorted(cons), open(os.path.join(here, f"oicache/d{d}.json"), "w"))
