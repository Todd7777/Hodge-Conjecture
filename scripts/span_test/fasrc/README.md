# Running the span test on FASRC

The span test asks whether the exceptional tuples $\xi_{44}, \xi_{51}, \xi_{52}, \xi_{68}$ of
Miranda–Movasati–Rufino–Villaflor lie in the lattice spanned by every currently known algebraic tuple
(linear, standard, all Hodge tuples of length $\le 6$, known exceptional tuples) in degree $d$.
See `docs/fermat/` and `scripts/span_test/span_big.py` for the method.

From a FASRC login node:

```bash
git clone -b claude/eloquent-ride-rw4eoa https://github.com/Todd7777/Hodge-Conjecture.git
cd Hodge-Conjecture/scripts/span_test/fasrc
bash submit.sh
```

`submit.sh` first runs a one-minute validation on the login node (four reference cases that must
reproduce known results), then submits one SLURM array task per degree (8 cores, 32 GB, 12 h each).
Results arrive in `out/d<degree>/results.jsonl` (one JSON line per exceptional tuple tested) and the
logs in `logs/`. To collect them:

```bash
cat out/d*/results.jsonl > span_results_fasrc.jsonl
```

A line with `"verdict": "not_member"` and `"certificate_checked": true` is a proof, given complete
enumeration, that the tuple is not reachable in that degree; the dual certificate is saved as
`out/d<degree>/cert_<q>_<d>.json`. A line with `"verdict": "member"` would make that exceptional tuple
algebraic (conditional on Kang's theorem for Fermat fourfolds) and must be re-verified independently.

Cost: the enumeration scales like $d^3$ and the exact Hermite normal form of the standard lattice is the
bottleneck above $d \approx 2500$ (about one minute at $d=1320$ on one core, much longer at $d \ge 3000$).
