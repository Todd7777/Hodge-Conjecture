"""fs_parity.py -- test the 'order-p parity' property of short Hodge tuples.

N_p(alpha) = number of entries a of alpha whose order in Z/d is exactly p (a = (d/p) u, p !| u).
Property P(p, d): every Hodge tuple of length <= 6 in degree d has N_p(alpha) even.
(Reducible tuples need not be enumerated: (a)+(-a) has two entries of the same order and eps_d has order 2.)
For each d the reduced Hodge tuples of length <= 6 are enumerated by fs_enum with the one-bit class
'order(a) == p'; a tuple with odd N_p is printed as a counterexample.
Usage: python3 fs_parity.py p dmax [enum_binary]
"""
import os
import subprocess
import sys
import tempfile
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))


def run(p, d, exe, workdir):
    path = os.path.join(workdir, f"parity_p{p}_d{d}.txt")
    with open(path, "w") as f:
        f.write("1\n")
        for a in range(1, d):
            f.write(f"{a} {1 if d // gcd(a, d) == p else 0:x}\n")
    out = subprocess.run([exe, str(d), path, "--reduced"], capture_output=True, text=True, check=True).stdout
    os.unlink(path)
    bad = [line.split() for line in out.splitlines() if line.startswith("sig ") and line.split()[2] == "1"]
    counts = {int(w[1]): int(w[2]) for w in (l.split() for l in out.splitlines()) if w[0] == "count"}
    return bad, counts


if __name__ == "__main__":
    p, dmax = int(sys.argv[1]), int(sys.argv[2])
    exe = sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, "fs_enum")
    workdir = tempfile.mkdtemp(prefix="fs_parity_", dir=os.environ.get("FS_BUILD"))
    ok = []
    for d in range(p, dmax + 1, p):
        bad, counts = run(p, d, exe, workdir)
        if bad:
            ex = [(int(w[1]), int(w[3]), tuple(map(int, w[4:]))) for w in bad]
            print(f"p={p} d={d}: FAILS -- (length, #tuples, example) with odd N_p: {ex}", flush=True)
        else:
            ok.append(d)
    print(f"p={p}: property holds for d in {ok}" if ok else f"p={p}: holds for no d", flush=True)
