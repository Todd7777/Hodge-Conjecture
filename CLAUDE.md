# CLAUDE.md

Guidance for Claude Code sessions in this repository, local or cloud.

## What this is

A research repository on the Hodge conjecture: the precise statement and its variants (several are false),
known cases through 2026, the obstructions every strategy meets, and exact, test-covered computations that
verify the conjecture for Fermat varieties through Shioda's inductive structure. The conjecture is open, and
this repository does not prove it.

## Ground rules

- Do not claim or imply that the conjecture is proved. Label every new claim as **Theorem** (complete proof
  here), **Machine-checked**, **Cited** (only after reading the source), **Numerical**, or **Conjecture/Heuristic**.
- A computation verifies the conjecture for a variety only together with the theorem that turns it into a
  proof, as `hodge.fermat` does with Shioda–Katsura and Lefschetz (1,1). Name that theorem every time.
- A pattern in computations is evidence, not proof. Try to construct a counterexample before building on it.
- Run the checks before and after every change. A new failure is a regression until shown otherwise.
- Commit verified work in small steps and push before the session ends. Work left only inside a cloud
  session can be lost with it.

## Setup and checks

```bash
pip install pytest
python3 -m pytest -q tests      # 2026-11-08: 68 pass (the README still says 61)
```

The C helpers in `scripts/` give their build line in their header comment (`gcc -O2 ...`).
`scripts/fermat_span/ilp_short_hodge.c` also needs `-fopenmp`.

## State on 2026-11-08

- `docs/attacks/` holds proof-attempt drafts with the status "drafts, not yet refereed" (2026-11-07).
  `04-derived-K3.md` was mid-repair after its first referee round.
- `docs/fermat/01-span-test.md`, `results/fermat_span/` and `scripts/fermat_span/` are the span-test campaign,
  in progress when last committed.
- The last commit (2026-11-07) snapshotted agents that were still running. Nothing later was pushed.

## Where the next steps are

`docs/03-strategies-and-obstructions.md`, Section 3.5 "Concrete open problems where progress is realistic",
and `docs/04-fermat-computations.md` (where the classical method stops).
