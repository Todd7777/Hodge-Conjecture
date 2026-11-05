"""Render results/*.json into results/README.md (markdown tables)."""
import glob
import json
import os
import sys

sys.path.insert(0, ".")

records = {}
for f in sorted(glob.glob("results/fermat_n*.json")):
    for r in json.load(open(f)):
        records[(r["n"], r["m"])] = r

out = ["# Fermat varieties X^n_m: Hodge classes vs. the inductive structure", "",
       "Columns: `b_prim` = primitive middle Betti number; `dim Hdg` = dim_Q of rational Hodge classes in H^n "
       "(= |B^n_m| + 1); `decomposable` = dimension of the span of Hodge characters reachable from points and "
       "surfaces by the Shioda-Katsura operations (N)/(Z) (see docs/04-fermat-computations.md); "
       "`indecomposable` = the rest; `orbits` = number of Galois-and-permutation orbits of indecomposable "
       "characters; `verified` = HC for X^n_m follows from the inductive structure + Lefschetz (1,1) alone.", ""]
for n in sorted({k[0] for k in records}):
    out.append(f"## n = {n}")
    out.append("")
    out.append("| m | b_prim | h^{p,q}_prim (q = 0..n) | dim Hdg | decomposable | indecomposable | orbits | verified | s |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    for (nn, m), r in sorted(records.items()):
        if nn != n:
            continue
        out.append(f"| {m} | {r['b_prim']} | {r['hodge_numbers_prim']} | {r['dim_hodge_classes']} | "
                   f"{r['dim_decomposable']} | {r['dim_indecomposable']} | {len(r['indecomposable_orbits'])} | "
                   f"{'yes' if r['hodge_conjecture_verified_by_inductive_structure'] else 'NO'} | {r.get('seconds', '')} |")
    out.append("")
    bad = [(m, r) for (nn, m), r in sorted(records.items()) if nn == n and r["dim_indecomposable"]]
    if bad:
        out.append(f"### Indecomposable Hodge characters for n = {n} (one representative per orbit, entries mod m)")
        out.append("")
        for m, r in bad:
            orbs = r["indecomposable_orbits"]
            shown = ", ".join("(" + ",".join(map(str, o)) + ")" for o in orbs[:8])
            more = "" if len(orbs) <= 8 else f", ... ({len(orbs)} orbits)"
            out.append(f"* m = {m}: {shown}{more}")
        out.append("")
with open("results/README.md", "w") as f:
    f.write("\n".join(out))
print("wrote results/README.md with", len(records), "records")
