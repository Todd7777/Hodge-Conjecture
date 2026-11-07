"""run_degrees.py -- driver for the span test on many degrees (one machine, all cores).

  python3 scripts/span_test/run_degrees.py --validate
  python3 scripts/span_test/run_degrees.py --degrees 572 1320 2244 --outdir span_out [--procs 8] [--keep]

For each degree d it enumerates all Hodge tuples of length 4 and 6 (hodge_mitm.c, exact), reduces them
modulo D_d, and runs span_big.py for every open exceptional tuple xi_q with q | d, q in TARGETS.
Results: one JSON line per (q, d) in OUTDIR/results.jsonl, plus RESULT lines on stdout.

The exceptional tuples xi_q below are those of Miranda-Movasati-Rufino-Villaflor, arXiv:2609.27301,
Definition 4.8, as listed in their repository github.com/mmiirandaaaa/length-reduction-functions
(exceptional_tuples.csv).  KNOWN are the q < 65 for which MMRV prove xi_q algebraic (35, 55 and 57
through fourfold reductions, i.e. through Kang's theorem); they are added to Lambda_d as known
algebraic generators.  TARGETS are the open ones.
"""
import argparse
import json
import os
import subprocess
import sys
import time

TUPLES = {
    12: [1, 4, 9, 10], 15: [1, 7, 10, 12], 20: [1, 6, 8, 17, 18], 21: [1, 10, 15, 16],
    28: [1, 8, 9, 10, 12, 17, 21, 22, 26], 33: [1, 4, 13, 16, 19, 22, 27, 30],
    35: [1, 2, 16, 17, 21, 22, 30, 31], 39: [1, 4, 15, 16, 19, 21, 27, 28, 30, 34],
    44: [1, 5, 6, 13, 14, 18, 20, 33, 34, 37, 41, 42], 51: [1, 10, 13, 18, 22, 28, 34, 37, 43, 49],
    52: [1, 10, 14, 17, 18, 21, 22, 24, 29, 41, 45, 46, 50],
    55: [1, 2, 12, 15, 16, 26, 27, 30, 35, 37, 41, 45, 46, 52],
    57: [1, 4, 7, 9, 13, 16, 28, 33, 40, 45, 46, 51, 52, 54],
    68: [1, 4, 5, 9, 12, 13, 14, 37, 38, 42, 45, 46, 49, 50, 58, 61, 62, 66],
}
KNOWN = [12, 15, 20, 21, 28, 33, 35, 39, 55, 57]
TARGETS = [44, 51, 52, 68]
HERE = os.path.dirname(os.path.abspath(__file__))


def build(outdir):
    exe = os.path.join(outdir, "hodge_mitm")
    if not os.path.exists(exe):
        subprocess.run(["gcc", "-O2", "-o", exe, os.path.join(HERE, "hodge_mitm.c")], check=True)
    return exe


def enumerate_classes(exe, d, L, procs, outdir):
    parts = [os.path.join(outdir, f"c_{d}_{L}_{r}.txt") for r in range(procs)]
    ps = [subprocess.Popen([exe, str(d), str(L), parts[r], str(r), str(procs)], stderr=subprocess.PIPE, text=True) for r in range(procs)]
    for p in ps:
        _, err = p.communicate()
        if p.returncode:
            sys.exit(f"hodge_mitm failed: {err}")
    seen = set()
    for f in parts:
        with open(f) as fh:
            for line in fh:
                seen.add(line.strip())
        os.remove(f)
    out = os.path.join(outdir, f"c_{d}_{L}.txt")
    with open(out, "w") as fh:
        for s in seen:
            if s:
                fh.write(s + "\n")
    return out, len(seen)


def run_span(q, d, files, outdir):
    extra = [f"{k}:{','.join(map(str, TUPLES[k]))}" for k in KNOWN if k != q and d % k == 0]
    cmd = [sys.executable, "-I", os.path.join(HERE, "span_big.py"), "--q", str(q), "--d", str(d),
           "--xi", ",".join(map(str, TUPLES[q])), "--classes", *files,
           "--cert", os.path.join(outdir, f"cert_{q}_{d}.json")]
    if extra:
        cmd += ["--extra", *extra]
    p = subprocess.run(cmd, capture_output=True, text=True)
    res = None
    for line in p.stdout.splitlines():
        if line.startswith("RESULT "):
            res = json.loads(line[7:])
    if res is None:
        res = {"q": q, "d": d, "verdict": "error", "stderr": p.stderr[-2000:], "stdout": p.stdout[-2000:]}
    res["extras"] = [int(e.split(":")[0]) for e in extra]
    return res


def do_degree(d, procs, outdir, keep, targets):
    exe = build(outdir)
    t0 = time.time()
    f4, n4 = enumerate_classes(exe, d, 4, 1, outdir)
    f6, n6 = enumerate_classes(exe, d, 6, procs, outdir)
    t1 = time.time()
    out = []
    for q in targets:
        if d % q == 0:
            r = run_span(q, d, [f4, f6], outdir)
            r.update({"classes4": n4, "classes6": n6, "enum_seconds": round(t1 - t0, 1), "span_seconds": round(time.time() - t1, 1)})
            out.append(r)
            print("RESULT " + json.dumps(r), flush=True)
            with open(os.path.join(outdir, "results.jsonl"), "a") as fh:
                fh.write(json.dumps(r) + "\n")
    if not keep:
        for f in (f4, f6):
            os.remove(f)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--degrees", type=int, nargs="*", default=[])
    ap.add_argument("--procs", type=int, default=os.cpu_count() or 4)
    ap.add_argument("--outdir", default="span_out")
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--validate", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    if a.validate:
        expect = {(35, 70): ("member", 1), (44, 132): ("not_member", 2), (52, 156): ("not_member", 2), (51, 204): ("not_member", 1)}
        ok = True
        for (q, d), (verdict, dim) in expect.items():
            r = do_degree(d, a.procs, a.outdir, False, [q])[0]
            good = r.get("verdict") == verdict and r.get("dim_projected_span") == dim and (verdict == "member" or r.get("certificate_checked"))
            ok &= good
            print(f"validate q={q} d={d}: {r.get('verdict')} dim={r.get('dim_projected_span')} expected {verdict} dim={dim}: {'ok' if good else 'MISMATCH'}")
        print("VALIDATION OK" if ok else "VALIDATION FAILED")
        sys.exit(0 if ok else 1)
    for d in a.degrees:
        do_degree(d, a.procs, a.outdir, a.keep, TARGETS)
    print("ALL DONE", flush=True)


if __name__ == "__main__":
    main()
