"""ilp_certify.py -- exact congruence certificates (with generator origins) for every best
representative in results/fermat_span/ilp_main.jsonl and for the validation instances; writes
results/fermat_span/ilp_certificates.json, then run ilp_verify_cert.py on it (independent check).

Certificate terms: [["std", d', p, i], c] = c times the lift to degree d of s_{p,i} (Def. 3.7) of
degree d', or [["xi", q'], c] = c times xi_{q'} (CSV) for q' proven algebraic by MMRV.  The integer
solution is computed by PARI (matsolvemod over Z) on the folded system and re-checked unfolded.
"""
import json
import os
import sys

import ilp_core as C
import ilp_solve as S

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                                    "results", "fermat_span"))


def certificate(q, d, beta, use_alg=True):
    X = C.read_tuples(C.EXC_CSV)
    xi = C.lift(X[q], q, d)
    keys, origins = C.lifted_standard_tuples(d, with_origin=True)
    gens = list(keys)
    orig = [["std", dp, p, i] for (dp, p, i) in origins]
    if use_alg:
        for qq in sorted(S.ALG_REPS):
            if qq != q and d % qq == 0:
                gens.append(C.lift(X[qq], qq, d))
                orig.append(["xi", qq])
    diff = [a - b for a, b in zip(C.fold(xi, d), C.fold(beta, d))]
    x = C.integer_certificate(d, gens, diff)
    if x is None:
        return None
    assert C.check_certificate(d, xi, tuple(beta), gens, x)
    return [[orig[j], c] for j, c in enumerate(x) if c]


def main():
    certs = []
    seen = set()
    for fname, kind in (("ilp_validation.jsonl", "validation"), ("ilp_main.jsonl", "main")):
        path = os.path.join(OUT, fname)
        if not os.path.exists(path):
            continue
        for line in open(path):
            r = json.loads(line)
            q, d = r["q"], r["d"]
            reps = []
            if kind == "validation":
                if r.get("mmrv_rep"):
                    reps.append(("mmrv", r["mmrv_rep"]))
                if r.get("exhaustive_example"):
                    reps.append(("exhaustive", r["exhaustive_example"]))
                for x in r["ilp"]:
                    if x.get("beta") and x.get("length") is not None:
                        reps.append(("ilp %s %s" % (x["form"], x["bound"]), x["beta"]))
            else:
                if r.get("best"):
                    reps.append((r["best"]["source"], r["best"]["beta"]))
            for src, beta in reps:
                key = (q, d, tuple(beta))
                if key in seen:
                    continue
                seen.add(key)
                # generators: lifted standard tuples + xi_q' for q' | d proven algebraic by MMRV
                # (the E4 lifts of the validation runs are congruent to these xi_q' mod D + S~)
                terms = certificate(q, d, beta, use_alg=True)
                certs.append({"q": q, "d": d, "beta": list(beta), "length": len(beta), "kind": kind,
                              "source": src, "terms": terms})
                print(kind, q, d, src, beta, "certificate terms:", None if terms is None else len(terms),
                      flush=True)
    with open(os.path.join(OUT, "ilp_certificates.json"), "w") as f:
        json.dump([c for c in certs if c["terms"] is not None], f)
    missing = [c for c in certs if c["terms"] is None]
    print("written", len(certs) - len(missing), "certificates; no certificate:", [(c["q"], c["d"], c["beta"]) for c in missing])


if __name__ == "__main__":
    main()
