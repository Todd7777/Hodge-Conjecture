"""Scan Fermat varieties X^n_m for Hodge characters that are not decomposable via the inductive structure.

Usage: python3 scripts/scan_fermat.py N M_MIN M_MAX OUT.json
Writes one JSON record per m with Hodge numbers, dim Hdg, number of indecomposable classes and their orbits.
"""
import json
import sys
import time

sys.path.insert(0, ".")
from hodge import fermat

n, m0, m1, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
records = []
for m in range(m0, m1 + 1):
    t = time.time()
    a = fermat.analyze(n, m)
    a["seconds"] = round(time.time() - t, 2)
    a["indecomposable_orbits"] = [list(o) for o in a["indecomposable_orbits"]]
    records.append(a)
    print(f"n={n} m={m:3d} b_prim={a['b_prim']:9d} dimHdg={a['dim_hodge_classes']:7d} "
          f"indec={a['dim_indecomposable']:5d} orbits={len(a['indecomposable_orbits']):4d} "
          f"verified={a['hodge_conjecture_verified_by_inductive_structure']} ({a['seconds']}s)", flush=True)
    with open(out, "w") as f:
        json.dump(records, f, indent=1)
