"""ilp_solve.py -- MMRV's (lifted) Aoki-Shioda integer program WITHOUT the {-1,0,1} restriction.

Two equivalent formulations, both solved with HiGHS (highspy), general integer variables:
  F1 (MMRV (32), unfolded):  max sum_j c_j x_j  s.t.  A x <= v,  x integer, |x_j| <= B,
      A = [linear tuples | lifted standard tuples (Def. 3.7) | extra algebraic tuples],
      v = count vector of xi_q lifted to degree d, c_j = column sums; length = |xi| - c.x
  F2 (folded L1):  min sum_i u_i  s.t.  -u <= fold(xi) - M z <= u,  z integer, |z_j| <= B
      (or free), M = folded [standard | extra] generators.  The linear generators are absorbed
      exactly by folding (MMRV Remark 4.11 and eps_d = (d/2) in D_d), so F2 has no bound on them.
Every solution is turned into exact integers and re-checked: residual >= 0 (F1), Hodge test,
and the certificate  xi - beta - sum_j x_j g_j  in D_d  (ilp_core.check_certificate).
"""
import argparse
import json
import time

import highspy
import numpy as np

import ilp_core as C

ALG_REPS = {  # MMRV Tables 2/4 representatives of length <= 6 (Prop. 4.3: xi_q algebraic)
    12: ((1, 8, 9), 12), 15: ((1, 7, 10, 12), 15), 20: ((3, 8, 19), 20),
    21: ((1, 10, 15, 16), 21), 28: ((5, 13, 17, 21), 28), 33: ((19, 26, 43, 44), 66),
    35: ((10, 12, 13, 53, 56, 66), 70), 39: ((25, 43, 49), 78),
    55: ((19, 29, 39, 79, 109), 110), 57: ((23, 41, 64, 66, 71, 77), 114)}


def extra_generators(q, d, mode):
    """Extra algebraic tuples of degree d.
    mode 'none'  : nothing (Aoki-Shioda / lifted Aoki-Shioda on D_d + S~_d only)
    mode 'E4'    : MMRV Algorithm 1: lifts of the reduced exceptional tuples of length <= 4
                   found earlier (representatives of xi_12,15,20,21,28 at degree q', of xi_33 at
                   66 and xi_39 at 78), whenever their degree divides d
    mode 'alg'   : xi_{q'} (lifted) for every q' | d, q' != q, that MMRV proved algebraic
                   (q' in ALG_REPS); legitimate since then xi_{q'} is in C."""
    if mode == "none":
        return []
    out = []
    if mode == "E4":
        for qq, (rep, dd) in ALG_REPS.items():
            if qq != q and len(rep) <= 4 and d % dd == 0:
                out.append(C.lift(rep, dd, d))
        return out
    if mode == "alg":
        X = C.read_tuples(C.EXC_CSV)
        for qq in ALG_REPS:
            if qq != q and d % qq == 0:
                out.append(C.lift(X[qq], qq, d))
        return out
    raise ValueError(mode)


def _highs(time_limit, threads, seed, verbose):
    h = highspy.Highs()
    h.setOptionValue("output_flag", bool(verbose))
    h.setOptionValue("time_limit", float(time_limit))
    h.setOptionValue("mip_rel_gap", 0.0)
    h.setOptionValue("mip_abs_gap", 0.999)   # objective is integral: gap < 1 proves optimality
    h.setOptionValue("threads", int(threads))
    h.setOptionValue("random_seed", int(seed))
    return h


def _pass(h, cost, lo, up, cols, rlo, rup, integer):
    """cols: list of (row_indices, values) per column (column-wise sparse)."""
    lp = highspy.HighsLp()
    n, mrows = len(cost), len(rlo)
    lp.num_col_, lp.num_row_ = n, mrows
    lp.col_cost_ = np.array(cost, dtype=float)
    lp.col_lower_ = np.array(lo, dtype=float)
    lp.col_upper_ = np.array(up, dtype=float)
    lp.row_lower_ = np.array(rlo, dtype=float)
    lp.row_upper_ = np.array(rup, dtype=float)
    start, index, value = [0], [], []
    for ri, vi in cols:
        index += list(ri)
        value += list(vi)
        start.append(len(index))
    lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_ = np.array(start, dtype=np.int32)
    lp.a_matrix_.index_ = np.array(index, dtype=np.int32)
    lp.a_matrix_.value_ = np.array(value, dtype=float)
    lp.integrality_ = [highspy.HighsVarType.kInteger if f else highspy.HighsVarType.kContinuous
                       for f in integer]
    h.passModel(lp)


def _status(h):
    info = h.getInfo()
    st = h.modelStatusToString(h.getModelStatus())
    return st, info


def solve(q, d, form="F2", bound=3, time_limit=60.0, extra_mode="alg", threads=1, seed=0,
          verbose=False, xi=None):
    """Solve one instance; returns a dict with exact, re-checked results."""
    X = C.read_tuples(C.EXC_CSV)
    xi = xi if xi is not None else C.lift(X[q], q, d)
    gens = C.generator_tuples(d, extra_generators(q, d, extra_mode))
    INF = highspy.kHighsInf
    lo_b = -INF if bound is None else -bound
    up_b = INF if bound is None else bound
    h = _highs(time_limit, threads, seed, verbose)
    t0 = time.time()
    if form == "F1":
        cols_t = C.linear_tuples(d) + gens
        v = C.counts(xi, d)
        cols, cost = [], []
        for t in cols_t:
            cnt = {}
            for a in t:
                cnt[a - 1] = cnt.get(a - 1, 0) + 1
            ri = sorted(cnt)
            cols.append((ri, [cnt[i] for i in ri]))
            cost.append(-sum(cnt.values()))
        n = len(cols)
        _pass(h, cost, [lo_b] * n, [up_b] * n, cols, [-INF] * (d - 1), v, [True] * n)
    elif form == "F2":
        m = C.fdim(d)
        cvec = C.fold(xi, d)
        cols_t = gens
        cols, cost = [], []
        for t in gens:
            y = C.fold(t, d)
            ri = [i for i in range(m) if y[i]]
            cols.append(([i for i in ri] + [m + i for i in ri], [y[i] for i in ri] + [-y[i] for i in ri]))
            cost.append(0)
        n = len(gens)
        for i in range(m):
            cols.append(([i, m + i], [1, 1]))
            cost.append(1)
        lo = [lo_b] * n + [0] * m
        up = [up_b] * n + [INF] * m
        _pass(h, cost, lo, up, cols, cvec + [-c for c in cvec], [INF] * (2 * m), [True] * (n + m))
    else:
        raise ValueError(form)
    h.run()
    st, info = _status(h)
    res = {"q": q, "d": d, "form": form, "bound": bound, "extra": extra_mode, "time_limit": time_limit,
           "status": st, "time": round(time.time() - t0, 2), "nodes": int(info.mip_node_count),
           "ncols": len(cols_t), "len_xi": len(xi)}
    sol = h.getSolution()
    if not (info.primal_solution_status == 2 or st == "Optimal"):
        res.update(length=None, proven=False)
        return res
    xs = np.array(sol.col_value)
    x = [int(round(v)) for v in xs[:len(cols_t)]]
    if form == "F1":
        v = C.counts(xi, d)
        r = list(v)
        for t, c in zip(cols_t, x):
            if c:
                for a in t:
                    r[a - 1] -= c
        assert min(r) >= 0, "negative residual"
        beta = C.to_tuple(r) if hasattr(C, "to_tuple") else tuple(a for a in range(1, d) for _ in range(r[a - 1]))
        dual_len = len(xi) + info.mip_dual_bound
    else:
        y = list(C.fold(xi, d))
        for t, c in zip(cols_t, x):
            if c:
                for j, w in enumerate(C.fold(t, d)):
                    y[j] -= c * w
        beta = C.unfold(y, d)
        dual_len = info.mip_dual_bound
    beta = tuple(sorted(beta))
    L = len(beta)
    cert_ok = C.check_certificate(d, xi, beta, cols_t, x)
    hodge_ok = C.is_hodge(beta, d)
    import math
    lb = math.ceil(dual_len - 1e-6) if dual_len is not None and dual_len > -1e300 else 0
    res.update(length=L, beta=list(beta), hodge=hodge_ok, certificate_ok=cert_ok,
               dual_bound_length=lb, proven=(st == "Optimal"),
               coeffs={str(i): c for i, c in enumerate(x) if c},
               max_abs_coeff=max([abs(c) for c in x] + [0]),
               gens_used=[list(cols_t[i]) for i, c in enumerate(x) if c])
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--q", type=int, required=True)
    ap.add_argument("--d", type=int, required=True)
    ap.add_argument("--form", default="F2")
    ap.add_argument("--bound", default="3")
    ap.add_argument("--time", type=float, default=60)
    ap.add_argument("--extra", default="alg")
    ap.add_argument("--threads", type=int, default=1)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    bound = None if a.bound in ("none", "free", "inf") else int(a.bound)
    r = solve(a.q, a.d, a.form, bound, a.time, a.extra, a.threads, a.seed, a.verbose)
    s = json.dumps(r)
    print(s)
    if a.out:
        with open(a.out, "a") as f:
            f.write(s + "\n")


if __name__ == "__main__":
    main()


def solve_guarded(q, d, form="F2", bound=3, time_limit=60.0, extra_mode="alg", threads=1, seed=0,
                  hard_factor=2.0, hard_extra=60.0):
    """Run `solve` in a child process with a hard wall-clock limit (HiGHS does not always honour
    its own time_limit on the free-bound models).  On a kill, returns status 'killed'."""
    import subprocess
    import sys
    cmd = [sys.executable, __file__, "--q", str(q), "--d", str(d), "--form", form,
           "--bound", "none" if bound is None else str(bound), "--time", str(time_limit),
           "--extra", extra_mode, "--threads", str(threads), "--seed", str(seed)]
    hard = time_limit * hard_factor + hard_extra
    t0 = time.time()
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=hard)
        lines = [l for l in out.stdout.splitlines() if l.startswith("{")]
        if not lines:
            return {"q": q, "d": d, "form": form, "bound": bound, "status": "error: " + out.stderr[-300:],
                    "length": None, "time": round(time.time() - t0, 1)}
        return json.loads(lines[-1])
    except subprocess.TimeoutExpired:
        return {"q": q, "d": d, "form": form, "bound": bound, "status": "killed (hard limit %.0fs)" % hard,
                "length": None, "proven": False, "time": round(time.time() - t0, 1)}
