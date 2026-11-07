"""ilp_main.py -- main run: xi_q for q in {44, 51, 52, 68} at lifted degrees d = lcm(q, e).

For each (q, d):
  1. exact class space V_d = B_d/(D_d + S~_d)  (ilp_classes.ClassSpace; validity checked exactly);
  2. exhaustive search of ALL reduced Hodge tuples of length <= Lmax: minimal length in every
     class of V_d (exact when <= Lmax, otherwise the lower bound Lmax + 1);
  3. targets: xi_q modulo D_d + S~_d ('pure'), and xi_q modulo D_d + S~_d + <xi_q' : q' | d, q' != q
     proven algebraic by MMRV> ('alg', = MMRV's lifted algorithm with reduced exceptionals);
     plus the span test: is xi_q in the F_2-span of the classes of Hodge tuples of length <= 6
     (all algebraic by Lefschetz (1,1) / Kang) and of the algebraic xi_q'?
  4. HiGHS (ilp_solve.solve) with general integer bounds, extra = 'alg';
  5. an exact integer certificate for the best representative (PARI), re-checked unfolded.
Writes one JSON line per (q, d) to results/fermat_span/ilp_main.jsonl.
"""
import argparse
import json
import os
import time

import ilp_core as C
import ilp_classes as CL
import ilp_solve as S

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                                    "results", "fermat_span"))


def f2_span_contains(vectors, target):
    """vectors/target: sets of basis labels (an F_2 vector = the set of basis elements in its
    support).  True iff target lies in the F_2-span of vectors (Gaussian elimination)."""
    labels = sorted(set(target).union(*[set(v) for v in vectors]))
    idx = {l: i for i, l in enumerate(labels)}
    def vec(v):
        r = 0
        for l in v:
            r ^= 1 << idx[l]
        return r
    piv = {}
    for v in vectors:
        r = vec(v)
        for p, b in sorted(piv.items(), reverse=True):
            if r >> p & 1:
                r ^= b
        if r:
            piv[r.bit_length() - 1] = r
    tv = vec(target)
    for p, b in sorted(piv.items(), reverse=True):
        if tv >> p & 1:
            tv ^= b
    return tv == 0


def run_one(q, d, Lmax, ilp_configs, ilp_time, threads, alg_set):
    t0 = time.time()
    X = C.read_tuples(C.EXC_CSV)
    xi = C.lift(X[q], q, d)
    rec = {"q": q, "d": d, "Lmax": Lmax}
    sp = CL.ClassSpace(d)
    rec.update(verify=sp.verify, dimV=sp.dimV, labels=sp.labels, galois_trivial=sp.galois_trivial)
    target = frozenset(sp.decode[sp.code_of_tuple(xi)])
    rec["target"] = sorted(target)
    alg_labels = [frozenset(["xi%d" % qq]) for qq in sorted(alg_set)
                  if qq != q and d % qq == 0 and "xi%d" % qq in sp.labels]
    rec["alg_labels"] = sorted(min(a) for a in alg_labels)
    t1 = time.time()
    res, err = sp.short_search(Lmax, nthreads=threads)
    rec["enum_time"] = round(time.time() - t1, 1)
    rec["enum_log"] = err.strip().splitlines()
    profile = {}
    for lab, byL in res.items():
        Lm = min(byL)
        profile["+".join(lab) if lab else "0"] = {"min": Lm, "count": byL[Lm][0],
                                                  "example": list(byL[Lm][1][0])}
    rec["profile"] = profile
    # coset target + span(alg)
    coset = set()
    for mask in range(1 << len(alg_labels)):
        s = set(target)
        for i, a in enumerate(alg_labels):
            if mask >> i & 1:
                s ^= set(a)
        coset.add(frozenset(s))
    def best_in(classes):
        best = None
        for lab, byL in res.items():
            if frozenset(lab) in classes:
                Lm = min(byL)
                if best is None or Lm < best[0]:
                    best = (Lm, list(byL[Lm][1][0]), sorted(lab))
        return best
    bp, ba = best_in({target}), best_in(coset)
    rec["exh_pure"] = bp
    rec["exh_alg"] = ba
    short = [frozenset(lab) for lab, byL in res.items() if min(byL) <= 6 and lab]
    rec["span_short_contains_target"] = f2_span_contains(short + alg_labels, target)
    rec["classes_reached_le6"] = sorted("+".join(sorted(s)) for s in set(short))
    # ILP runs (extra = alg)
    rec["ilp"] = []
    lb_exh = ba[0] if ba is not None else Lmax + 1
    for form, bound in ilp_configs:
        best_now = min([r["length"] for r in rec["ilp"] if r.get("length") is not None] + [10**9])
        if form == "F2" and bound is not None and bound > 3 and best_now <= lb_exh:
            rec["ilp"].append({"form": form, "bound": bound, "status": "skipped (F2:3 already optimal by exhaustive search)",
                               "length": None})
            continue
        try:
            if bound is None:   # free bounds: LP bound ~0 (2 xi in the lattice); short runs only
                tl = min(ilp_time, 120.0 if d <= 100 else 30.0)
                r = S.solve_guarded(q, d, form, bound, tl, "alg", hard_factor=1.5, hard_extra=30.0)
            else:
                r = S.solve_guarded(q, d, form, bound, ilp_time, "alg")
        except Exception as e:  # keep going; record the failure
            r = {"form": form, "bound": bound, "status": "error: %r" % (e,), "length": None}
        rec["ilp"].append({k: r.get(k) for k in ("form", "bound", "status", "time", "nodes", "length",
                                                  "dual_bound_length", "proven", "beta", "hodge",
                                                  "certificate_ok", "max_abs_coeff")})
    # best known representative of xi_q modulo D + S~ + alg, with exact certificate
    cands = []
    if ba:
        cands.append((ba[0], tuple(ba[1]), "exhaustive"))
    for r in rec["ilp"]:
        if r.get("length") is not None and r.get("hodge") and r.get("certificate_ok"):
            cands.append((r["length"], tuple(r["beta"]), "ilp %s %s" % (r["form"], r["bound"])))
    cands.sort()
    if cands:
        L, beta, src = cands[0]
        gens = C.generator_tuples(d, S.extra_generators(q, d, "alg"))
        diff = [a - b for a, b in zip(C.fold(xi, d), C.fold(beta, d))]
        x = C.integer_certificate(d, gens, diff)
        ok = x is not None and C.check_certificate(d, xi, beta, gens, x)
        rec["best"] = {"length": L, "beta": list(beta), "source": src, "hodge": C.is_hodge(beta, d),
                       "certificate_ok": ok,
                       "certificate": [[list(gens[j]), c] for j, c in enumerate(x) if c] if x else None}
    # proof status for the 'alg' target
    best_len = cands[0][0] if cands else None
    if ba is not None:
        rec["proven_optimal"], rec["lower_bound"] = (best_len == ba[0]), ba[0]
    else:
        nl = Lmax + 1 + (1 if (d % 2 == 1 and (Lmax + 1) % 2 == 1) else 0)  # odd d: even lengths only
        rec["lower_bound"] = nl
        rec["proven_optimal"] = best_len is not None and best_len == nl
    if not rec["proven_optimal"]:
        for r in rec["ilp"]:
            if r.get("bound") is None and r.get("proven") and r.get("length") == best_len:
                rec["proven_optimal"] = True
                rec["lower_bound"] = best_len
    rec["best_length"] = best_len
    rec["total_time"] = round(time.time() - t0, 1)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--q", type=int, required=True)
    ap.add_argument("--d", type=str, required=True, help="comma list of degrees")
    ap.add_argument("--lmax", type=int, default=7)
    ap.add_argument("--ilp-time", type=float, default=180)
    ap.add_argument("--configs", default="F1:1,F2:3,F2:10,F2:none")
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--out", default=os.path.join(OUT, "ilp_main.jsonl"))
    ap.add_argument("--odd-deep-max", type=int, default=0,
                    help="for odd d up to this bound, search exhaustively up to length 8")
    a = ap.parse_args()
    cfgs = []
    for c in ([] if a.configs == "none" else a.configs.split(",")):
        f, b = c.split(":")
        cfgs.append((f, None if b == "none" else int(b)))
    done = set()
    if os.path.exists(a.out):
        for line in open(a.out):
            r0 = json.loads(line)
            done.add((r0["q"], r0["d"]))
    for d in [int(x) for x in a.d.split(",")]:
        if (a.q, d) in done:
            continue
        # exhaustive depth: 8 for d <= 240, 7 for d <= 720 (memory of the triple table), else 6
        lmax = min(a.lmax, 8 if d <= 240 else (7 if d <= 720 else 6))
        if d % 2 == 1 and d <= a.odd_deep_max:   # odd d: only even lengths; go to 8
            lmax = max(lmax, 8)
        rec = run_one(a.q, d, lmax, cfgs, a.ilp_time, a.threads, S.ALG_REPS.keys())
        with open(a.out, "a") as f:
            f.write(json.dumps(rec) + "\n")
        print("q=%d d=%d dimV=%d exh_pure=%s exh_alg=%s span_short=%s best=%s proven=%s lb=%s ilp=%s (%.0fs)" % (
            a.q, d, rec["dimV"], rec["exh_pure"] and rec["exh_pure"][0], rec["exh_alg"] and rec["exh_alg"][0],
            rec["span_short_contains_target"], rec["best_length"], rec["proven_optimal"], rec["lower_bound"],
            [(r["form"], r["bound"], r["length"], (r["status"] or "")[:8]) for r in rec["ilp"]],
            rec["total_time"]), flush=True)


if __name__ == "__main__":
    main()
