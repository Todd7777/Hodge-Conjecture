# 6. Report on the attack drafts (refereed 2026-11-13)

**Status.** No draft proves the Hodge conjecture or a new major case, and none claims to. Three of the sixteen needed major revision (01, 04, 12); the other thirteen needed minor revision. All sixteen drafts
`docs/attacks/01`–`16` were refereed by independent referee runs. Each run was an AI model instructed to be
adversarial, to check every labelled claim, and to read the primary sources where it could. Their full reports
are in `docs/attacks/referee-reports/`. Every correction they listed has been applied to the drafts, and each draft
carries a one-line referee note under its status paragraph. Attack 17 was not refereed in this way. It was
re-derived by independent code and completed (§4).

These referee runs are not a substitute for expert human refereeing. They did read a substantial part of the cited
literature, listed in each report. Where a source could not be checked, the report marks the claim UNVERIFIABLE.

## 1. Verdicts

| Draft | Strategy | Verdict | What the referee found |
|---|---|---|---|
| 01 semiregularity | S1 | **major** | Bloch–Esnault–Kerz's theorem was applied over C without its Chow–Künneth hypothesis, so the formal-lift step of "Theorem D" is unproved for general families (now a remark). Buchweitz–Flenner's hypothesis was misstated. Theorem B and Prop. 3.1 are known (BF Thm 5.1, BEK App. A). |
| 02 motivic | S2 | minor | One invalid inference in a gap discussion: abelian threefolds give a counterexample. Remark 5.2 is now labelled heuristic. Theorems A–D are correct. |
| 03 Hodge loci + arithmetic | S3 | minor | No false proof. Prop. 4.1 (an isolated Hodge point with Mumford–Tate group GL₂) shows that special points need not be CM, which corrected `docs/03`. Theorem 4.2 contradicts the literal Klingler–Otwinowska–Urbanik Conjecture 1.5(a) of arXiv v1, through a VHS "defined over Q" in the de Rham sense. Corollary 4.3 is a heuristic. |
| 04 derived K3 | S1/S7 | **major** (structure) | The mathematics is correct. Approval by "round-1 referees" was unsupported. Sections 7–9 and the references had been lost in the 2026-11-07 snapshot. Floccari 2025 (Kuga–Satake and HC for all powers on every RM surface with ρ = 16 and Witt index 2) was missing. |
| 05 Kuga–Satake | S1 | minor | Sound. One claimed equivalence is proved in one direction only. The gap G5 is closed by Floccari 2025, Thm 5.11. |
| 06 Weil classes | S1/S7 | minor | No wrong claim. The quaternionic discriminant formula and the classification of Hodge classes on simple non-CM sixfolds were re-verified. Several results are known (Brosnan, Lemma 9; Schoen's product argument). |
| 07 tropical degeneration | S5 | minor | Its §5 case, "Weil sixfolds of discriminant +1", is empty under its own normalization δ(h) = det h. The proofs give the intended non-split case δ ≠ −1. Theorem A is correct but its lifting criterion is generic algebraicity spread over a base change. §4 is sound. Cor. 4.6 depends on the unproved hypothesis (H-trop), and its n = 3 consequence is already in Brosnan. A misattributed reference was fixed. |
| 08 p-adic | S6/S3 | minor | No false step. The hypothesis (Cont₀), continuity of K-theory for proper W(k)-schemes, carries most of the weight. With Milne's rationality conjecture it gives HC for CM abelian varieties, so the headline is a reduction between open problems. |
| 09 K₂ / exponential | M1 | minor | Correct and almost entirely classical. A result of Colliot-Thélène–Voisin was quoted as conditional, but it is unconditional, since Bloch–Kato is a theorem. |
| 10 hypersurfaces / Jacobian ring | S6 | minor | No wrong claim. Every explicit number was recomputed: Jacobian-ring dimensions 426 and 1751, plane rank 19, Gram determinant 125, the codimensions of Cor. 7.2, the Macaulay bound and all 14 rows of Table 2. Two statements credited to the 2024 Fermat-sextic paper are not in its abstract, and part of Theorem 5.3 is in Movasati's abstract. |
| 11 Mumford–Tate / powers | S3 | minor | Prop. 2.5 proves de Rham-absoluteness, not absoluteness. An unverified report of a withdrawn manuscript was removed. Theorem B (Kuga–Satake implies algebraicity of the orientation class via one endomorphism) is correct and plausibly new, but gives no new unconditional case. |
| 12 counterexample hunt | S7 | **major** | Its candidate family, "Weil sixfolds of discriminant +1", is empty under its own normalization disc = det H. The family is now the non-split one. Its "sign condition", whose failure "would disprove HC", always holds: it is the Hodge standard conjecture for Lefschetz classes, which Milne proved (Ann. Math. 155 (2002), Remark 3.7). |
| 13 Lefschetz induction | — | minor | No errors. Example 5.3 reproduces. A one-line proof of b₄ = 6 for the Segre cubic closes gap G5. One overstatement was qualified. |
| 14 Lawson homology / Chow | — | minor | §2.3 contradicted §7: as written, it would make the Friedlander–Mazur conjecture a theorem. Hu's implication needs a stronger, open form of Suslin's conjecture. The "discriminant +1" wording is fixed. Theorems A and B are correct and classical. |
| 15 Hodge-theoretic structure | — | minor | Prop. 4.2 and the §4.5 table claimed all of condition (CM2), but the isogeny clause is not proved. Remark 1.4 conflated the target with HC. Theorem D is plausible, but it rests on the Klingler–Otwinowska–Urbanik theorem (abstract only) and on canonical-model facts quoted from memory. Its novelty is unclear. |
| 16 formal reduction | — | minor | Correct. The advertised "new exact equivalence" HC ⟺ HC(Q̄) ∧ (G₀) is known in substance: Voisin 2007, Prop. 0.7 = Charles–Schnell, Thm 50. The slicing step, Prop. 1.2, is the single-class analogue of KOU's reduction to special points. |

## 2. What the drafts contribute, after refereeing

* **Correct and plausibly new, but with no new unconditional case:** 11, Theorem B. 16, Prop. 1.2 (elementary).
  03, Theorem 4.2, which shows that the de Rham notion "VHS defined over Q" admits transcendental special points.
* **Correct reductions between open problems:** 01 (VHC along curves, modulo BEK's hypothesis), 08 (modulo
  (Cont₀)), 05 and 04 (RM classes on K3 surfaces modulo Kuga–Satake or Hodge similitudes).
* **Correct and classical:** most of 02, 05, 06, 09, 13.
* **Withdrawn as stated:** the counterexample route of 12 (the family was empty and the test vacuous), the
  formal-lift claim of 01 over C, the discriminant-+1 case of 07, and the claim of 14 that would have made the
  Friedlander–Mazur conjecture a theorem.
* **Recomputed and confirmed:** every explicit number of 10 (Jacobian rings and Noether–Lefschetz codimensions), the
  quaternionic discriminant formula of 06, the Clifford-algebra step of 11, Lemma 4.1 of 07, and Example 5.3 of 13.

## 3. Corrections to the core documents found by the referees

* `docs/01` and `docs/03` (M6) said that Klingler–Otwinowska–Urbanik settle the field-of-definition problem for all
  positive-dimensional components. They prove it under a monodromy condition and reduce the rest to special points.
* `docs/03` (C3) said that special points have CM Hodge structures. They need not (attack 03, Prop. 4.1).
* `docs/02` and `docs/03` (S1, S7, P1) named "Weil sixfolds of discriminant +1" as the open case. That set is empty
  under the normalization of Markman and Brosnan. The open case is the non-split one, disc ≠ −1.

## 4. Attack 17 and the Fermat notes

Attack 17 (the open Fermat degrees 44, 51, 52) was re-derived by code that shares nothing with the original
python-flint and PARI scripts (`hodge/formal_module.py`, `tests/test_formal_module.py`). Every number agrees. Its
missing sections were written (§§4–8). Two new notes go beyond it:

* `docs/fermat/02-exceptional-lengths.md` (Theorem D): the exact Aoki–Shioda length of ξ_q for the infinite families
  every q = 4p and q = 3p (Theorems D and D′). It matches all 58 entries of this form in MMRV's Table 1.
* `docs/fermat/03-galois-obstruction.md` (Theorems G and L): no cycle defined over the field of the known cycles,
  nor over any field generated by roots of unity and radicals of the primes dividing 2q, reaches the open classes
  ξ_44, ξ_51, ξ_52. The missing field is a quadratic extension generated by the square root of an explicit product
  of sines and radicals.

## 5. Files

* Full reports: `docs/attacks/referee-reports/2026-11-13-*.md`. The "old → new" corrections they list were applied
  in commits 75f2be6, 0c53b11 and the commit that added this file, so their quotations describe the drafts as they
  were before.
* Machine-readable verdicts: `docs/attacks/_referee-verdicts.json`.
