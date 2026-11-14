#!/usr/bin/env python3
"""Regenerate results/weil_route.md: how far Markman's theorems on Weil classes reach on the Fermat varieties of
degree 44, 51 and 52.  Statements and proofs: docs/fermat/04-weil-route.md.

Part 1 (degree q, exact, pure Python, a few seconds): the simple CM factors of the Fermat Jacobian J(C_q); the parity
invariant on every Weil generator for every imaginary quadratic field and on every Hodge element supported on factors
of dimension <= 5 (Theorem W1); for every CM subfield E of Q(mu_q), whether an E-Weil element of odd parity exists
(Theorem W3), and the explicit realizations of hodge/weil.py REALIZATIONS.
Part 3 (lifts, needs numpy and a C compiler): for D = q k, are the Galois characters of all Weil generators and
small-factor Hodge elements of degree D already in <eps(Lambda_D)>, and is the lift of xi_q reached (Theorem W2)?
Part 2 (only with --search, needs scipy): MILP search for the smallest realization for each CM subfield.

Usage:
    python3 scripts/weil_route.py [MAX_DEGREE] [--search] [OUTPUT]     (defaults: 572, results/weil_route.md)
The full run takes about 30 minutes, almost all of it in Part 3 for degrees 528 and 572 (the length-6 enumeration).
"""
import os
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from hodge import formal_module as F  # noqa: E402
from hodge import galois as GA  # noqa: E402
from hodge import weil as W  # noqa: E402

QS = (44, 51, 52)
PLAN = {44: [44 * k for k in range(1, 14)], 51: [51, 102, 153, 204], 52: [52, 104, 156, 208, 260]}


def part1(lines):
    lines.append("## 1. Degree q (exact)\n")
    lines.append("### 1.1 Simple CM factors of J(C_q)\n")
    lines.append("For each orbit of curve characters β: dimension of the simple factor A′ (= [G : H]/2), dimension of "
                 "A_β, and the number of eigencharacters with odd parity. Rows are grouped by these data.\n")
    for q in QS:
        fac = W.simple_factors(q)
        groups = {}
        for f in fac:
            nodd = sum(W.parity(v, q) for v in f.eigencharacters())
            key = (f.simple_dim, f.dim, len(f.h), nodd > 0)
            groups.setdefault(key, []).append(f.beta)
        lines.append(f"**q = {q}** ({len(fac)} orbits)\n")
        lines.append("| dim A′ | dim A_β | \\|H\\| | odd-parity eigencharacters | orbits (representatives) |")
        lines.append("|---|---|---|---|---|")
        for key in sorted(groups):
            reps = groups[key]
            shown = ", ".join(str(b) for b in reps[:6]) + (f", … ({len(reps)} in all)" if len(reps) > 6 else "")
            lines.append(f"| {key[0]} | {key[1]} | {key[2]} | {'yes' if key[3] else 'no'} | {shown} |")
        lines.append("")
    lines.append("### 1.2 Theorem W1 checks\n")
    lines.append("| q | imaginary quadratic K | Weil generators | odd parity | Hodge elements on factors of dim ≤ 5 "
                 "(basis) | odd parity |")
    lines.append("|---|---|---|---|---|---|")
    for q in QS:
        fac = W.simple_factors(q)
        Ks = W.imaginary_quadratic(q)
        gens = [g for N in Ks for g in W.weil_generators(q, N, fac)]
        assert all(W.is_hodge_counts(g, q) for g in gens)
        odd = sum(W.parity(W.counts_to_tuple(g), q) for g in gens)
        sg = W.small_factor_generators(q, 5, fac)
        assert all(W.is_hodge_counts(g, q) for g in sg)
        odd_s = sum(W.parity(W.counts_to_tuple(g), q) for g in sg)
        lines.append(f"| {q} | {len(Ks)} | {len(gens)} | {odd} | {len(sg)} | {odd_s} |")
    lines.append("")
    lines.append("### 1.3 Theorem W3: E-Weil elements of odd parity, for every CM subfield E of Q(μ_q)\n")
    lines.append("N = Gal(Q(μ_q)/E). *odd element* is the exact lattice test `weil.odd_e_weil_exists`.\n")
    lines.append("| q | [E : Q] | [Q(μ_q) : E] | N | odd element |")
    lines.append("|---|---|---|---|---|")
    for q in QS:
        fac = W.simple_factors(q)
        phi = len(W.units(q))
        for N in W.cm_subgroups(q):
            ex = W.odd_e_weil_exists(q, N, fac)
            assert ex == (len(N) % 2 == 1)
            Ns = "{" + ", ".join(map(str, sorted(N))) + "}" if len(N) <= 6 else f"order {len(N)}"
            lines.append(f"| {q} | {phi // len(N)} | {len(N)} | {Ns} | {'**yes**' if ex else 'no'} |")
    lines.append("")
    lines.append("### 1.4 All exceptional classes ξ_q with q < 70 (MMRV's list)\n")
    lines.append("Parity = a mod-2 functional killing D_q + S_q (`weil.parity_functional`; λ for 44, 51, 52). "
                 "*criterion* = odd E-Weil elements exist exactly for [Q(μ_q) : E] odd. *small* = odd Hodge "
                 "element supported on factors of dim ≤ 5. *im. quadr.* = odd Weil element for an imaginary quadratic "
                 "K ⊂ Q(μ_q). *E×E′* = a divisor class on a product of two CM elliptic-curve factors congruent to "
                 "ξ_q (`weil.elliptic_divisor_realization`).\n")
    lines.append("| q | status of ξ_q | [B:D+S] | criterion | small | im. quadr. | E×E′ |")
    lines.append("|---|---|---|---|---|---|---|")
    import galois_obstruction as GO
    from hodge import exceptional_length as EL
    for q in sorted(GO.XI):
        idx = EL.index_B_over_DS(q)
        fac = W.simple_factors(q)
        res = [(len(N), W.odd_e_weil_exists(q, N, fac)) for N in W.cm_subgroups(q)]
        crit = all(odd == (n % 2 == 1) for n, odd in res)
        small = any(W.parity(W.counts_to_tuple(g), q) for g in W.small_factor_generators(q, 5, fac))
        half = len(W.units(q)) // 2
        iq = any(odd for n, odd in res if n == half)
        ell = W.elliptic_divisor_realization(q)
        lines.append(f"| {q} | {GO.STATUS[q]} | {idx} | {'holds' if crit else 'fails'} | {'yes' if small else 'no'} | "
                     f"{'yes' if iq else 'no'} | {ell[0] + ell[1] if ell else '—'} |")
    lines.append("")
    lines.append("### 1.5 Explicit realizations (hodge/weil.py `REALIZATIONS`)\n")
    lines.append("| key | E-Weil type: dim of the abelian variety | degree of the class | element of R_q | Hodge | parity |")
    lines.append("|---|---|---|---|---|---|")
    for key in W.REALIZATIONS:
        q = W.REALIZATIONS[key][0]
        el, dim, deg = W.realization(key)
        lines.append(f"| {key} | {dim} | {deg} | {el} | {F.is_hodge_tuple(el, q)} | {W.parity(el, q)} |")
    lines.append("")


def part2(lines, dmax):
    import galois_obstruction as GO
    lines.append("## 3. Lifts (Galois characters, Theorem W2)\n")
    lines.append("Characters compared exactly at the first 24 primes l ≡ 1 (mod 2D). *new* = generators whose "
                 "character is not in ⟨ε(Λ_D)⟩. *reached* = is ε(lift of ξ_q) in the group generated by ε(Λ_D), the "
                 "Weil generators of all imaginary quadratic K and the small-factor Hodge elements?\n")
    lines.append("| q | D | simple factors | K | Weil generators | new | small-factor generators | new | reached | "
                 "seconds |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    with tempfile.TemporaryDirectory() as tmp:
        exe = GO.build_enumerator(tmp)
        for q in QS:
            for D in PLAN[q]:
                if D > dmax:
                    continue
                t0 = time.time()
                data, lat, _, _ = GO.lambda_group(D, exe)
                fac = W.simple_factors(D)
                Ks = W.imaginary_quadratic(D)
                wg = [g for N in Ks for g in W.weil_generators(D, N, fac)]
                sg = W.small_factor_generators(D, 5, fac)
                new_w = new_s = 0
                for gens, kind in ((wg, "w"), (sg, "s")):
                    for g in gens:
                        v = [W.exponent_counts(g, pd) for pd in data]
                        if not lat.contains(v):
                            if kind == "w":
                                new_w += 1
                            else:
                                new_s += 1
                            lat.add(v)
                target = GA.even_form(F.lift(GO.XI[q], q, D), D)
                reached = lat.contains([GA.exponent_exact(target, pd) for pd in data])
                dt = time.time() - t0
                print(f"q={q} D={D}: factors {len(fac)}, Weil {len(wg)} (new {new_w}), small {len(sg)} (new {new_s}), "
                      f"reached {reached} ({dt:.0f}s)", flush=True)
                lines.append(f"| {q} | {D} | {len(fac)} | {len(Ks)} | {len(wg)} | {new_w} | {len(sg)} | {new_s} | "
                             f"{'**no**' if not reached else 'yes'} | {dt:.0f} |")
    lines.append("")


def part3(lines):
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp
    lines.append("## 2. Smallest realizations (MILP, scipy/HiGHS)\n")
    lines.append("Minimise the dimension of an abelian variety of Weil type relative to E built from J(C_q) whose "
                 "E-Weil element has odd parity. Optimality is the solver's claim (Numerical); the solutions are "
                 "verified exactly.\n")
    lines.append("| q | [E : Q] | min dim | degree | units used (factor, twist, multiplicity) |")
    lines.append("|---|---|---|---|---|")
    for q in QS:
        fac = W.simple_factors(q)
        phi = len(W.units(q))
        for N in W.cm_subgroups(q):
            if len(N) % 2 == 0:
                continue
            us = W.e_weil_units(q, N, fac)
            els = [u.element() for u in us]
            rows = W.hodge_rows(q, els)
            par = [W.parity(e, q) for e in els]
            n = len(us)
            cons = [LinearConstraint(np.array([r + [0] for r in rows], dtype=float), 0, 0),
                    LinearConstraint(np.array([par + [-2]], dtype=float), 1, 1)]
            res = milp(np.array([u.cost for u in us] + [0], dtype=float), constraints=cons,
                       integrality=np.ones(n + 1), bounds=Bounds(0, 60), options={"time_limit": 120})
            if res.status != 0:
                lines.append(f"| {q} | {phi // len(N)} | solver status {res.status} | | |")
                continue
            x = [int(round(v)) for v in res.x[:n]]
            el = tuple(sorted(a for xi, e in zip(x, els) for _ in range(xi) for a in e))
            assert F.is_hodge_tuple(el, q) and W.parity(el, q) == 1
            used = "; ".join(f"{us[i].factor.beta}, {us[i].twist}, {x[i]}" for i in range(n) if x[i])
            deg = sum(x[i] * len(us[i].eig) for i in range(n))
            lines.append(f"| {q} | {phi // len(N)} | {sum(x[i] * us[i].cost for i in range(n))} | {deg} | {used} |")
    lines.append("")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dmax = int(args[0]) if args else 572
    out = args[1] if len(args) > 1 else os.path.join(ROOT, "results", "weil_route.md")
    lines = ["# Markman's theorems and the open Fermat degrees 44, 51, 52", "",
             f"Generated by `python3 scripts/weil_route.py {dmax}{' --search' if '--search' in sys.argv else ''}`. "
             "Statements and proofs: `docs/fermat/04-weil-route.md`. Code: `hodge/weil.py`.", ""]
    t0 = time.time()
    part1(lines)
    print(f"part 1 done ({time.time() - t0:.0f}s)", flush=True)
    if "--search" in sys.argv:
        part3(lines)
        print(f"part 3 done ({time.time() - t0:.0f}s)", flush=True)
    part2(lines, dmax)
    with open(out, "w") as f:
        f.write("\n".join(lines))
    print("wrote", out)


if __name__ == "__main__":
    main()
