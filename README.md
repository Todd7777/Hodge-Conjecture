# Hodge Conjecture — an honest research repository

**Status: the Hodge conjecture is open. This repository does not contain a proof, and the AI session that produced it did not find one.** Nobody has one as of November 2026; the best short status reports are the guest posts by B. Totaro (11 Sept 2026) and C. Voisin (12 Sept 2026) on T. Tao's blog.

What *is* here is meant to be useful to anyone who wants to work on the problem seriously:

| Part | What it is | Where |
|---|---|---|
| Precise statement, reformulations, and every variant with its status (several variants are **false**) | survey | [`docs/01-statement-and-variants.md`](docs/01-statement-and-variants.md) |
| Everything that is actually known, with references, including the 2025–26 results (Markman: all abelian varieties of dimension ≤ 5; Fermat varieties of degree < 65 except 44, 51, 52; …) | survey | [`docs/02-known-cases.md`](docs/02-known-cases.md) |
| Why the problem is hard: the six mechanisms that have ever produced cycles, the constraints imposed by the counterexamples, a strategy-by-strategy assessment, a checklist for evaluating claimed proofs, and six concrete open problems | analysis | [`docs/03-strategies-and-obstructions.md`](docs/03-strategies-and-obstructions.md) |
| Exact, test-covered computations verifying the conjecture for concrete families (Fermat varieties via Shioda's inductive structure; Fermat surfaces via explicit lines) and locating exactly where the classical method stops working | code + data | [`docs/04-fermat-computations.md`](docs/04-fermat-computations.md), [`hodge/`](hodge/), [`results/`](results/) |
| Bibliography | — | [`docs/05-references.md`](docs/05-references.md) |

## The conjecture in one paragraph

For a smooth projective complex variety $X$, every class in $H^{2p}(X,\mathbb{Q})$ whose complex representative is of Hodge type $(p,p)$ is a rational linear combination of fundamental classes of algebraic subvarieties of codimension $p$. Known for $p=1$ (Lefschetz, 1924), hence for $p=n-1$ and for all varieties of dimension $\le 3$; the first open case is codimension-2 cycles on fourfolds. The integral version is false (Atiyah–Hirzebruch 1962, Kollár 1992, …), the Kähler version is false (Voisin 2002), and the conjecture implies that Hodge classes are stable under $\mathrm{Aut}(\mathbb{C})$ — a transcendence statement that is itself open.

## What the code proves

`hodge/` is a dependency-free Python package (exact integer arithmetic only).

* `hodge.griffiths` — Hodge numbers of smooth hypersurfaces from the Jacobian ring (Griffiths).
* `hodge.fermat` — Hodge classes of the Fermat variety $X^n_m$ as *Hodge characters*, and Shioda's inductive-structure criterion. For each $(n,m)$ it decides whether every Hodge class is reachable from points and surfaces by the Shioda–Katsura operations; if so, **the Hodge conjecture for $X^n_m$ is verified** (given the Shioda–Katsura theorem and Lefschetz (1,1)); if not, it lists the Hodge classes for which a different construction is needed.
* `hodge.fermat_lines` — the $3m^2$ lines on the Fermat surface, their exact intersection matrix and its rank, compared with the Picard number.

Headline results (details and tables in `results/`):

* Fermat fourfolds: the inductive structure alone proves HC for every degree $m\le 64$ **except** $m\in\{25,32,33,35,36,39,40,42,44,45,48,50,52,54,55,56,60,62,64\}$, where specific "exceptional" Hodge classes appear (e.g. $(1,6,11,16,21,-5)$ mod 25, Aoki's arithmetic-progression type). This reproduces, from scratch, the boundaries found in the literature (Shioda's $m\le20$, da Silva's $21,27$ and failure at $33$, Aoki's $p^2$, and the open degrees $44, 52$).
* Fermat sixfolds: all degrees $m\le32$ except $25$ and $32$; eightfolds: all $m\le20$.
* Fermat surfaces: lines span a sublattice of rank $3(m-1)(m-2)+1+[m\ \mathrm{even}]$ (Shioda's formula, recomputed exactly), which equals the Picard number iff $m\le4$ or $\gcd(m,6)=1$; e.g. $\rho(S_6)=86$ with only 62 from lines.

## Quick start

```bash
pip install pytest
python3 -m pytest -q tests          # 61 tests: published values + internal cross-checks
python3 -c "from hodge import fermat; print(fermat.analyze(4, 25))"
python3 scripts/scan_fermat.py 4 3 40 results/fermat_n4.json
python3 scripts/fermat_surfaces.py 8 12
python3 scripts/make_tables.py
```

## Caveats, stated plainly

* The computations verify the conjecture only for the specific varieties listed, and only modulo the cited theorems (Shioda–Katsura 1979, Lefschetz (1,1)). They prove nothing about the general conjecture.
* The 2025–26 literature was consulted through search-engine excerpts because the sandbox blocked arxiv.org and journal sites; see the note at the end of `docs/05-references.md`.
* Claims marked **[unverified]** in the docs (including an October 2026 AI-generated manuscript on CM abelian varieties and a 2026 preprint on Fermat degrees 44, 51, 52) have not been independently confirmed.
