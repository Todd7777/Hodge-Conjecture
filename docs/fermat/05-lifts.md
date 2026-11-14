# Lifts of the exceptional classes: how far MMRV's length reduction reaches

**Status (2026-11-14).** MMRV prove the Hodge conjecture for a Fermat degree q by finding a representative of ξ_q of
length ≤ 6 modulo linear and standard classes, in degree q or after lifting to a multiple D = kq. That is their
Prop. 4.3 together with Kang's theorem for Fermat fourfolds (Cited, through MMRV). They settle 35, 55 and 57 this
way in degree 2q. Their Table 3 gives heuristic upper bounds for one lift of each q. This note asks whether lifts can
settle anything beyond degree 64.

* **Theorem L2 (doubling).** For every odd q = p_1 p_2 (distinct primes),
  ℓ_{2,2q}(ξ_q) ≥ g(q) ≥ ⌈f_0(q)/2⌉, where g(q) is an explicit cycle count. Among all such q ≤ 1000,
  g(q) ≤ 6 only for q ∈ {15, 21, 33, 35, 39, 51, 55, 57}; for q > 1000, g(q) ≥ φ(q)/8 > 6. So **lifting to
  degree 2q settles no odd two-factor degree beyond 57**, in particular none of 65, 69, 77, 85, 87, 91, 93, 95.
* **Other multipliers (Numerical).** For every two-factor q ∈ Q with 65 ≤ q < 100 and every k ≤ 8 with
  kq ≤ 560, a MILP finds the shortest representative of the lifted class. The class is allowed to differ from ξ_q
  by settled classes, and must have no component on another open class. In every case the minimum is at least 8
  (§4). With these lifts, MMRV's method settles none of the open degrees between 65 and 100.
* **What is already settled (Corollary, docs/02).** MMRV's Theorem 1.1, their Cor. 4.1 and Prop. 3.2, and Aoki's
  generation theorem settle every degree whose divisors in Q are all settled. That adds 24 degrees between 65 and
  100 to MMRV's stated range (`hodge/fermat_degrees.py`). The open degrees up to 100 are 44, 51, 52, 65, 68, 69,
  76, 77, 85, 87, 88, 91, 92, 93, 95.

Labels follow `CLAUDE.md`. **Theorem** means a complete proof here, from Theorem T of
`docs/fermat/02-exceptional-lengths.md` §6. **Numerical** means a MILP optimum (HiGHS via scipy). Its
representatives are verified exactly, but its optimality claims are the solver's.

---

## 1. Setting

For D = kq the lift R_q → R_D, (a) ↦ (ka), sends ξ_q to lift_D(ξ_q). It preserves and reflects algebraicity (MMRV
Prop. 3.2, Cited). Put ℓ_{2,D}(α) = min{ℓ(α′) : α − α′ ∈ D_D + S_D}. If some α′ in the class of lift_D(ξ_q), modulo
D_D + S_D and the lifts of classes already known to be algebraic, has length ≤ 6, then ξ_q is algebraic. The reason:
α′ lives on a Fermat fourfold, where every Hodge class is algebraic (Kang, as cited by MMRV Prop. 4.3). This is the
whole method of MMRV §4.3–4.4. The settled classes are the ξ_q with q ∈ Q, q < 65, q ∉ {44, 51, 52}
(MMRV Theorem 1.1).

## 2. The push-down to degree q

Let q be odd and D = 2q. Every residue x mod 2q is odd or even, and x ↦ x mod q is a bijection from the odd residues
to Z/q. Define the Z-linear map

  π : R_{2q} → R_q,   (x) ↦ (u) + (−2^{−1}u)  if x is odd (u = x mod q, u ≠ 0),
                      (2b) ↦ (b),   (q) ↦ 0.

*Where it comes from.* By the distribution relation B̄_1(u/q) = B̄_1(u′/2q) + B̄_1(u″/2q), where u′ and u″ are the
odd and the even lift of u. An odd entry of degree 2q therefore enters the Hodge condition like (u) − (2^{−1}u) in
degree q, and (−z) ≡ −(z) modulo D_q. We only use the following two properties.

**Proposition L1 (Theorem).** Let q = p_1 p_2 be odd. Then π(D_{2q}) ⊆ D_q, π(S_{2q}) ⊆ D_q + S_q, and
π(lift_{2q} ξ_q) = ξ_q.

*Proof.* A pair (x) + (−x) goes to a sum of pairs, and (q) goes to 0. The lift has only even entries 2x, which go
to (x). For S_{2q}, take the standard tuples s_{p,i} (MMRV Def. 3.7) of each degree d′ | 2q with k = d′/p ≥ 3,
lifted to degree 2q by m = 2q/d′.

* *d′ odd* (d′ | q). All entries are even, and π gives back the lift of s_{p,i} to degree q, which lies in S_q.
* *d′ = 2e, p = 2, k = e.* The tuple is (i, e + i, 2e − 2i, e) with i odd, lifted by the odd m = q/e. Write
  u = mi mod q. The entries go to (u) + (−u/2), to (u/2) (because m(e + i)/2 ≡ u/2), to (−u), and to 0. The image
  is two pairs, so it lies in D_q.
* *d′ = 2e, p odd, k = 2e/p even.* All p + 1 entries have the parity of i. If i is even, π gives the standard tuple
  s_{p, mi/2} of degree q. If i is odd, the p block entries m(i + jk) are odd. Their residues mod q are the
  u ≡ mi (mod q/p), which is the block of s_{p, mi} in degree q, because jmk = j·2q/p runs over the multiples of
  q/p. The images (−u/2) form the block of s_{p, −mi/2}. The last entry −pmi goes to (−pu) + (pu/2). So
  π(s) = s_{p,u} + s_{p,−u/2}, a sum of two standard tuples of degree q (q/p ≥ 3). ∎

`lifts.pushdown_respects_standard` checks the second inclusion exactly, by lattice membership, for
q = 15, 21, 33, 35, 39, 55, 65, 69 (`tests/test_lifts.py`).

## 3. Theorem L2

Recall the coset functionals of Theorem T: the supports are the cosets of H = {t² = 1} in (Z/q)^×, and the cosets of
⟨p_1⟩ in (Z/p_2)^× (multiplied by p_1) when ord_{p_2}(p_1) is even, and symmetrically for p_2. They kill D_q + S_q
and are odd on ξ_q. Multiplication by 2^{−1} permutes the supports of each kind, since every support is closed under
negation. Let g(q) be the sum, over the cycles of this permutation, of ⌈length/2⌉ (`lifts.doubling_bound`).

**Theorem L2.** For q = p_1 p_2 odd, ℓ_{2,2q}(lift ξ_q) ≥ g(q) ≥ ⌈f_0(q)/2⌉.

*Proof.* Let α′ ≡ lift ξ_q modulo D_{2q} + S_{2q}. By L1, π(α′) ≡ ξ_q modulo D_q + S_q, so every coset functional
N is odd on π(α′).

* An odd entry x of α′ contributes to N(π(α′)) through u and −u/2. If u lies in the support C, then −u/2 lies
  in 2^{−1}C, because every support is closed under negation.
* An even entry 2b contributes through b, so to one support.
* The entry q contributes nothing.

So on a cycle of length o, an odd entry is an edge {C, 2^{−1}C}. For o = 1 the two contributions cancel mod 2. An
even entry is a vertex. Each support must be covered an odd number of times. Every entry with an odd coefficient
covers at most two supports, and entries on different cycles or of different kinds are different. So a cycle needs
at least ⌈o/2⌉ entries, and ℓ(α′) ≥ g(q). Finally, each cycle of length o has o supports and contributes
⌈o/2⌉ ≥ o/2. The number of supports is f_0(q) (Theorem T), so g(q) ≥ ⌈f_0(q)/2⌉. ∎

**Corollary L3.** Among odd q = p_1 p_2 ≤ 1000, g(q) ≤ 6 exactly for q ∈ {15, 21, 33, 35, 39, 51, 55, 57}
(`test_doubling_never_reaches_six_beyond_57`). For q > 1000, g(q) ≥ φ(q)/8 > 6. So for every odd two-factor q > 57,
no representative of lift_{2q}(ξ_q) modulo D_{2q} + S_{2q} has length ≤ 6. Degree 2q has no other element of Q,
since 2 ∉ P.

| q | f_0(q) (Thm T) | g(q) (Thm L2) | ℓ_{2,2q} (MILP) | MMRV Table 3 |
|---|---|---|---|---|
| 15 | 4 | 3 | 3 | — |
| 21 | 4 | 3 | 3 | — |
| 33 | 6 | 4 | 4 | 4 |
| 35 | 8 | 5 | 6 | 6 |
| 39 | 6 | 3 | 3 | 3 |
| 51 | 10 | 6 | 7 | 7 |
| 55 | 10 | 5 | 5 | 5 |
| 57 | 10 | 6 | 6 | 6 |
| 65 | 16 | 9 | 10 | 10 |
| 69 | 12 | 7 | 9 | 9 |
| 77 | 16 | 9 | 12 | 12 |
| 85 | 18 | 10 | 12 | 12 |
| 87 | 16 | 9 | 10 | 10 |
| 91 | 22 | 12 | 17 | 17 |
| 93 | 16 | 10 | 10 | 10 |
| 95 | 20 | 10 | 10 | 10 |
| 111 | 20 | 10 | 10 | 10 |

The MILP values agree with every entry of MMRV's Table 3 for odd q, so their doubled representatives are optimal.
The bound g(q) is attained for 15, 21, 33, 39, 55, 57, 93, 95, 111, 123 and 129, but not always. The gap
(35, 51, 65, 69, 77, 85, 87, 91, …) means degree 2q has invariants beyond the pushed-down coset functionals.

## 4. Other multipliers (Numerical)

For every two-factor q ∈ Q with 65 ≤ q < 100 (65, 68, 69, 76, 77, 85, 87, 91, 92, 93, 95) and every k ≤ 8 with
D = kq ≤ 560, the MILP of `scripts/lift_lengths.py` minimises the length of a Hodge tuple of degree D. The tuple must
lie in lift_D(ξ_q) plus D_D + S_D. It may differ from lift_D(ξ_q) by lifts of settled classes. It may have no
component on the other open classes dividing D, such as 51 in degree 204. The classes are separated by mod-2
functionals computed from the standard tuples and the explicit representatives of each ξ_{q′}
(Theorems D, D′ and T). Every tuple found is checked exactly: it is Hodge, and lattice membership confirms its
class. `results/lift_lengths.md` §2 lists every case with the solver status and dual bound.

**What the runs show (Numerical).**

* No representative of length ≤ 6 exists in any case where the solver proved optimality.
* The smallest optimum found anywhere is 8, for q = 68 at k = 3 and k = 6.
* For odd q the optima follow a pattern. Even k gives ℓ_{2,2q}(ξ_q): for q = 69 the value is 9 for k = 2, 4, 6, 8,
  and for 65 it is 10. Odd k gives f_0(q): for 69 the value is 12 for k = 3, 5, 7, and for 65 it is 16.
* For q = 4p the multiplier 3 shortens only 68 (10 → 8). For 76 and 92 every k gives f_0(q) = 11 and 12.
* Some runs stop at the 300-second time limit, mostly odd k with D ≥ 255. Their lengths are upper bounds, and the
  table gives the dual bound. Where the dual bound is below 7, the claim "no length ≤ 6" is not proved for that pair.
  It then rests on the pattern above, or on the Galois test of `docs/fermat/03` where that test was run (65, 68, 69
  for k ≤ 3).

## 5. What this means

Lifting is the only tool MMRV's method has beyond degree q, and for the two-factor degrees between 65 and 100 it does
not reach length 6. For lifts by 2 this is a theorem for every odd q > 57. For the other lifts tested it is a solver
result. To settle these degrees one needs cycles that are not linear, standard or fourfold cycles of any multiple
degree, which is the same conclusion as `docs/fermat/03-galois-obstruction.md` (fields of definition) and
`docs/fermat/04-weil-route.md` (Markman's theorems).

**Open questions.**

1. Exact formula for ℓ_{2,2q}(ξ_q). Find the invariants of degree 2q that the push-down misses (the gap in §3).
2. Is ℓ_{2,kq}(ξ_q) = f_0(q) for every odd k coprime to q, and ℓ_{2,kq}(ξ_q) = ℓ_{2,2q}(ξ_q) for every even k? The
   data of §4 say yes for k ≤ 8. A push-down for odd prime k would need to divide by k − 1, which is even, so
   another argument is needed.
3. For q = 4p only 68 is shortened by a lift (10 → 8 in degree 3q). Explain this.

## 6. Reproduction

```bash
python3 -m pytest -q tests/test_lifts.py tests/test_fermat_degrees.py
python3 scripts/lift_lengths.py          # the MILP tables of §3–4 (scipy; about an hour for §4)
```

Code: `hodge/lifts.py`, `hodge/fermat_degrees.py`, `hodge/two_prime.py`.
