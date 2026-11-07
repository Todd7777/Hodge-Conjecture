"""ilp_validate.py -- reproduce/improve MMRV Tables 2 and 4 (and Table 1 entries for q = 51,52,55,
57,68 at d = q) with the unrestricted ILP, and certify optimality by exhaustive search.
Writes JSON lines to results/fermat_span/ilp_validation.jsonl."""
import json
import os
import sys
import time

import ilp_core as C
import ilp_classes as CL
import ilp_solve as S

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "results", "fermat_span")
CONFIGS = [("F1", 1), ("F1", 3), ("F2", 3), ("F2", None)]

INSTANCES = [("T2", q, q, C.MMRV_TABLE2[q]) for q in sorted(C.MMRV_TABLE2)]
INSTANCES += [("T4", q, d, t) for (q, d), t in sorted(C.MMRV_TABLE4.items())]
INSTANCES += [("T1", q, q, None) for q in (51, 52, 55, 57, 68)]
TABLE1 = {51: 10, 52: 7, 55: 10, 57: 10, 68: 10}


def run(tl=120.0, Lmax=7, only=None):
    path = os.path.join(OUT, "ilp_validation.jsonl")
    X = C.read_tuples(C.EXC_CSV)
    done = set()
    if os.path.exists(path):
        for line in open(path):
            r = json.loads(line)
            done.add((r["table"], r["q"], r["d"]))
    for tab, q, d, mmrv in INSTANCES:
        if only and (q, d) not in only:
            continue
        if (tab, q, d) in done:
            continue
        rec = {"table": tab, "q": q, "d": d, "mmrv_rep": mmrv,
               "mmrv_len": len(mmrv) if mmrv else TABLE1.get(q)}
        xi = C.lift(X[q], q, d)
        extra = S.extra_generators(q, d, "E4")
        rec["extra_E4"] = [list(t) for t in extra]
        # exhaustive search with the same lattice (D_d + S~_d + E4 lifts)
        t0 = time.time()
        sp = CL.ClassSpace(d, extra=extra)
        rec["verify"] = sp.verify
        rec["dimV"], rec["labels"], rec["galois_trivial"] = sp.dimV, sp.labels, sp.galois_trivial
        target = sp.decode[sp.code_of_tuple(xi)]
        rec["target_label"] = list(target)
        if mmrv:  # MMRV's published representative: Hodge and in the class of xi?
            rec["mmrv_rep_hodge"] = C.is_hodge(mmrv, d)
            rec["mmrv_rep_in_class"] = sp.decode[sp.code_of_tuple(mmrv)] == target
        res, _ = sp.short_search(Lmax)
        found = res.get(target, {})
        rec["exhaustive_Lmax"] = Lmax
        rec["exhaustive_min"] = min(found) if found else None
        rec["exhaustive_example"] = list(found[min(found)][1][0]) if found else None
        rec["exhaustive_count_at_min"] = found[min(found)][0] if found else 0
        rec["exhaustive_time"] = round(time.time() - t0, 1)
        rec["ilp"] = []
        for form, bound in CONFIGS:
            r = S.solve_guarded(q, d, form, bound, tl if bound is not None else min(tl, 60.0), "E4")
            rec["ilp"].append({k: r.get(k) for k in ("form", "bound", "status", "time", "nodes",
                                                      "length", "dual_bound_length", "proven", "beta",
                                                      "hodge", "certificate_ok", "max_abs_coeff")})
        with open(path, "a") as f:
            f.write(json.dumps(rec) + "\n")
        best = min(x["length"] for x in rec["ilp"] if x["length"] is not None)
        print(tab, q, d, "mmrv", rec["mmrv_len"], "exh_min", rec["exhaustive_min"], "ilp_best", best,
              [(x["form"], x["bound"], x["length"], x["status"][:8], x["time"]) for x in rec["ilp"]],
              flush=True)


if __name__ == "__main__":
    tl = float(sys.argv[1]) if len(sys.argv) > 1 else 120.0
    run(tl)
