"""ilp_report.py -- markdown tables for results/fermat_span/ilp.md from the JSONL records."""
import json
import os
import sys

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                                    "results", "fermat_span"))


def load(name):
    p = os.path.join(OUT, name)
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []


def next_len(Lmax, d):
    """smallest length > Lmax that a Hodge tuple of degree d can have (even only, if d is odd)"""
    n = Lmax + 1
    return n + 1 if (d % 2 == 1 and n % 2 == 1) else n


def fmt_t(t):
    return "(" + ", ".join(str(x) for x in t) + ")"


def ilp_cell(r):
    if r.get("length") is None:
        st = r.get("status") or ""
        return "skip" if st.startswith("skipped") else ("killed" if st.startswith("killed") else "--")
    tag = "opt" if r.get("proven") else "TL"
    return "%d %s" % (r["length"], tag)


def validation_table():
    rows = load("ilp_validation.jsonl")
    out = ["| table | q | d | MMRV bound | MMRV rep Hodge & in class | exhaustive min (<= %s) | F1 \\|x\\|<=1 | F1 \\|x\\|<=3 | F2 \\|z\\|<=3 | F2 free | ours |" % (rows[0]["exhaustive_Lmax"] if rows else 7),
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        ok = "--" if r.get("mmrv_rep") is None else ("yes" if r.get("mmrv_rep_hodge") and r.get("mmrv_rep_in_class") else "NO")
        ex = r["exhaustive_min"]
        lb = "%d" % ex if ex is not None else (">= %d" % next_len(r["exhaustive_Lmax"], r["d"]))
        cells = [ilp_cell(x) for x in r["ilp"]]
        best = min([x["length"] for x in r["ilp"] if x.get("length") is not None] + ([ex] if ex else []))
        proven = (ex is not None and best == ex) or any(x.get("proven") and x.get("bound") is None and x.get("length") == best for x in r["ilp"])
        out.append("| %s | %d | %d | %s | %s | %s | %s | %d%s |" % (
            r["table"], r["q"], r["d"], r["mmrv_len"], ok, lb, " | ".join(cells), best,
            " (optimal)" if proven else ""))
    return "\n".join(out)


def main_table(name="ilp_main.jsonl"):
    rows = load(name)
    rows.sort(key=lambda r: (r["q"], r["d"]))
    out = ["| q | d | dim V_d | exh. depth | min len. mod D+S~ | min len. mod D+S~+alg | best | optimal? | F1 \\|x\\|<=1 | F2 \\|z\\|<=3 | F2 \\|z\\|<=10 | F2 free | span(len<=6) contains xi_q | representative |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        def ex(e):
            if e is None:
                return ">= %d" % next_len(r["Lmax"], r["d"])
            return str(e[0])
        cells = {(x["form"], x["bound"]): ilp_cell(x) for x in r["ilp"]}
        best = r.get("best") or {}
        out.append("| %d | %d | %d | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            r["q"], r["d"], r["dimV"], r["Lmax"], ex(r["exh_pure"]), ex(r["exh_alg"]),
            r.get("best_length"), "yes" if r.get("proven_optimal") else "no (>= %s)" % r.get("lower_bound"),
            cells.get(("F1", 1), "--"), cells.get(("F2", 3), "--"), cells.get(("F2", 10), "--"),
            cells.get(("F2", None), "--"), "yes" if r["span_short_contains_target"] else "no",
            fmt_t(best["beta"]) + "_%d" % r["d"] if best.get("beta") else "--"))
    return "\n".join(out)


def profile_table(name="ilp_main.jsonl"):
    rows = load(name)
    rows.sort(key=lambda r: (r["q"], r["d"]))
    out = ["| q | d | basis of V_d | classes reached by Hodge tuples of length <= 6 (min length) |", "|---|---|---|---|"]
    for r in rows:
        prof = r["profile"]
        short = sorted(((v["min"], k) for k, v in prof.items() if v["min"] <= 6 and k != "0"))
        out.append("| %d | %d | %s | %s |" % (r["q"], r["d"], ", ".join(r["labels"]),
                                             "; ".join("%s: %d" % (k, m) for m, k in short) or "--"))
    return "\n".join(out)


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("validation", "all"):
        print(validation_table())
        print()
    if what in ("main", "all"):
        print(main_table())
        print()
    if what in ("profile", "all"):
        print(profile_table())
