# The span test for the open exceptional tuples ξ_44, ξ_51, ξ_52 (and ξ_68)

**Status (2026-11-07).** The span test does **not** make ξ_44, ξ_51, ξ_52 or ξ_68 algebraic. For each
of these q and **every** multiple d = qk ≤ 1000 there is an independently checked dual certificate. It is
a homomorphism χ: R_d → Z/2 that vanishes on every generator of Λ_d and takes the value 1 on ξ_q. So the
known cycles cannot reach ξ_q in degree d: linear cycles, Aoki–Shioda (standard) cycles of every degree
dividing d, the conjugates of the exceptional tuples already known to be algebraic, and every Hodge class
coming from Fermat surfaces and fourfolds of degree d. These cycles may be combined by join, deletion,
lift and permutation, and arbitrary Z-linear combinations are allowed. **This is a negative result about
one method, not about the Hodge conjecture.**

Behind the failure there is a simple invariant. For q = 44 (resp. 52, resp. 51), the number of entries
of exact order 11 (resp. 13, resp. 17), taken mod 2, vanishes on every Hodge tuple of length ≤ 6 in
every degree we tested. It is odd on ξ_q (section 7). The same procedure, used as a control,
re-proves the algebraicity of every ξ_q that MMRV settle with q < 65 (section 4). Each of those proofs
comes with an explicit, independently checked integer identity.

Paper: M. Miranda, H. Movasati, L. Rufino, R. Villaflor, *Lengths of Hodge characters in Fermat
varieties*, arXiv:2609.27301 (v2, 26 Sept 2026), below **MMRV**. Code: `scripts/fermat_span/`. Data and
certificates: `results/fermat_span/`. Run summary: `results/fermat_span/summary.md`.

## 1. Setting

We use MMRV's notation (section 4).

* **The modules.** R_d is the free Z-module on (Z/d) − {0}. A tuple (a_1, …, a_L) is identified with
  the formal sum Σ(a_i)_d, so join is sum, deletion is difference and permutation is the identity.
  Lifting R_{d'} → R_d, (a)_{d'} ↦ (ka)_d with k = d/d', is an identification inside R = lim R_d.
  The group G_d = (Z/d)^× acts by t·(a) = (ta).
* **The Hodge functionals.** h_t(Σ n_a (a)) = Σ n_a (⟨ta⟩_d − d/2), for t ∈ G_d.
* **Hodge tuples.** A tuple of length L is a Hodge tuple of degree d (MMRV Def. 3.9) if
  h_t = 0 for every t ∈ G_d, i.e. Σ_i ⟨t a_i⟩ = dL/2 for every t. Odd L is possible only for even d.
* **The submodules.** D (linear), S̃ (standard tuples and their lifts), C (algebraic) and B (Hodge) are
  the submodules of MMRV Defs. 4.3–4.5. We write X_d = X ∩ R_d.
* **Λ_d.** For q ∈ Q and a multiple d of q, Λ_d is the Z-span in R_d of the following generators:
  * (a) + (−a) for a ≠ 0, and ε_d = (d/2) when d is even;
  * the standard tuples s_{p,i} of Def. 3.7 in every degree d' | d (d' = pk', k' ≥ 3, p ∤ i, all
    entries nonzero), lifted to degree d. This is a superset of what `standards()` in the authors'
    `utils.py` produces; modulo D_d the two are equal (section 3.2);
  * t·ξ_{q'} for t ∈ G_d, where q' ∈ Q, q' | d, q' ≠ q, and ξ_{q'} has its own certificate of
    algebraicity (the set K_0 = {12, 15, 20, 21, 28, 33, 35, 39, 55, 57}, certified in section 4);
  * every Hodge tuple of length 2, …, 6 in degree d (lengths 3 and 5 only for d even).

  Weighted Fermat varieties of degree d' | d need no separate treatment: their Hodge tuples lift to
  degree-d Hodge tuples of the same length (Prop. 3.2), so they are already among the generators.

## 2. Logical chain

Each step is tagged by what it rests on:

* **[MMRV]** proved in MMRV (their proof may itself cite a paper; the paper is then named).
* **[CITED: …]** a theorem MMRV cite without proof and which we have not re-proved.
* **[HERE]** proved in this note, or verified by an exact computation with a checkable certificate.

**Lemma 1 [HERE].** For every d, B_d equals the kernel lattice
K_d := {v ∈ R_d : h_t(v) = 0 for all t ∈ G_d}. Under the folding map π: R_d → Z^h, h = ⌊(d−1)/2⌋, given
by π((a)) = e_a (a < d/2), −e_{d−a} (a > d/2), 0 (a = d/2), whose kernel is exactly D_d, we have
π(B_d) = {x ∈ Z^h : Σ_a x_a (2⟨ta⟩_d − d) = 0 for all t}.

*Proof.* "⊆": every Hodge tuple of degree d satisfies h_t = 0, the h_t are linear, and a Hodge tuple of
another degree that lies in R_d is a lift of a degree-d one with the same h_t up to a positive factor
(Prop. 3.2). "⊇": let v = Σ n_a (a) ∈ K_d. Add Σ_{n_a<0} (−n_a)((a)+(−a)), which lies in D_d ⊆ B_d
and is killed by every h_t. The result v' has non-negative coefficients, so it is a tuple of some length
L with entries in [1, d−1], and h_t(v') = 0 means Σ⟨t a⟩ = dL/2 for every t. So v' is a Hodge tuple
(Def. 3.9) or zero, and v = v' − (element of D_d) ∈ B_d. Finally, π kills exactly the span of
(a)+(−a) and ε_d (that span is D_d, Remark 4.6), and h_t descends through π because
⟨−ta⟩ = d − ⟨ta⟩. ∎

So B_d is computable exactly. In every degree we used, we checked the consequence of Aoki's theorem that
the argument needs (step 7) directly. We also found that V_d := B_d/L_0, with
L_0 := D_d + Σ_{d'|d} S_{d'}, is (Z/2)^{|Q(d)|}, with basis the classes of the ξ_{q'} (section 4).

**The chain.** Fix q ∈ Q and a multiple d of q.

1. **Hodge tuples of length ≤ 6 are algebraic.** Every Hodge tuple α of length L ≤ 6 in degree d lies in
   C, case by case:
   * L = 2: α = (a, −a) is linear. **[MMRV]** Prop. 3.6 and Remark 3.7 (B⁰_d = C⁰_d = D⁰_d).
   * L = 4: α ∈ B²_d = C²_d, the Fermat surface of degree d.
     **[CITED: Lefschetz (1,1)]** via MMRV Remark 3.9.
   * L = 6: α ∈ B⁴_d = C⁴_d, the Fermat fourfold of degree d.
     **[CITED: Kang, Bull. Aust. Math. Soc. 93 (2016), Cor. 3.2]** as quoted in MMRV Remark 3.9.
     *We have not checked Kang's argument; every positive conclusion below that uses a length-6 tuple
     inherits this dependence.*
   * L odd: α ∗ ε_d is a Hodge tuple of length L + 1 ∈ {2, 4, 6} (Remark 3.11, eq. (21)), hence
     algebraic by the cases above. So α is algebraic by **definition** (Def. 3.11). L = 1 is
     ε_d ∈ C^{−1}_d (Remark 3.12).
2. **Linear and standard cycles.** D ⊆ C: **[MMRV]** Prop. 3.6, whose proof uses
   **[CITED: Villaflor Loyola 2022, Cor. 8.3]** for the class of a linear cycle. Every s_{p,i} of Def. 3.7
   is algebraic: MMRV Prop. 3.7, whose proof MMRV leave out ("quite tedious") and refer to
   **[CITED: Aoki 1987]** (Aoki–Shioda varieties A_{p,d}). Lifts stay algebraic: **[MMRV]** Prop. 3.2.
   Hence D_d + Σ_{d'|d} S_{d'} ⊆ C_d.
3. **Galois stability.** For every t ∈ G_d, tC_d = C_d. **[MMRV]** Remark 3.2 (from Prop. 3.1) for even
   length; for odd length through Def. 3.11 and tε_d = ε_d (units of Z/d are odd when d is even).
4. **Known exceptional tuples.** For each q' ∈ K_0, ξ_{q'} ∈ C. **[HERE]** For each such q' there is an
   explicit integer identity in `results/fermat_span/cert_q<q'>_d<d'>.txt`, independently checked
   (section 4). It writes ξ_{q'} as a combination of generators of the first, second and fourth kinds
   (no ξ's), so it rests only on steps 1–3 and 5. With step 3, every t·ξ_{q'} lies in C.
5. **C is a Z-module.** C is by definition the Z-submodule generated by all algebraic tuples
   (**[MMRV]** Def. 4.3). So Λ_d ⊆ C_d, and **if ξ_q ∈ Λ_d then ξ_q ∈ C.**

   The geometric content of "C is closed under Z-combinations" is Theorem 4.1's proof: a Z-relation
   between algebraic tuples is turned into an equality of joins, and Prop. 3.5(ii) and Prop. 3.8
   (join/deletion) then give algebraicity of the actual character. **[MMRV]** Theorem 4.1 uses
   Props. 3.1, 3.2, 3.4, 3.5. MMRV's proof quotes only Props. 3.2, 3.4, 3.5, but when some α_i has odd
   length the join/deletion step needs Prop. 3.8. Prop. 3.5(ii) in turn rests on
   **[CITED: Duque Franco–Villaflor Loyola, arXiv:2312.17222, Thm. 1.2]** (periods of join cycles) and
   on **[CITED: Shioda 1979, Thm. II]** (inductive structure; MMRV only sketch this step: "one can
   show that this is equivalent to …").
6. **From characters to the Hodge conjecture.** If C_d = B_d, the Hodge conjecture holds for every
   weighted Fermat variety of degree d, and (Remark 4.5) of every degree dividing d.
   **[MMRV]** Theorem 4.1 with Prop. 3.1.
7. **Aoki's generation theorem.** B_d = D_d + S_d + Σ_{q'∈Q, q'|d} Z[G_d] ξ_{q'}.
   **[CITED: Aoki 1983, Theorem C]** = MMRV Theorem 4.2, read with S_d as in the authors' code
   (standard tuples of every divisor of d, lifted). Section 9 explains why the literal reading of
   Def. 3.7 gives a false statement when 4 | d. With steps 2, 3, 6 this is MMRV Corollary 4.1:
   **if ξ_{q'} ∈ C for every q' ∈ Q dividing d, then the Hodge conjecture holds for all weighted Fermat
   varieties of degree d.** **[HERE]** For each individual degree in our tables we verified step 7's
   conclusion directly: B_d = K_d (Lemma 1) = L_0 + Σ Z[G_d]ξ_{q'}, via the Smith form of L_0 and the
   classes of the ξ's. For those degrees, Aoki's theorem is not needed; for the infinite family below it
   is.
8. **Kubert–Aoki is not used.** 2ξ_q ∈ D_q + S_q (**[CITED: Kubert 1979; Aoki 1983]** = MMRV
   Theorem 4.3) is not needed for any implication. It only explains why the question is mod 2. We
   verified it for every q ∈ Q, q ≤ 70, with explicit identities, and it holds implicitly in every
   tested degree because V_d is elementary abelian.

**What a positive outcome would prove.** Suppose ξ_q ∈ Λ_d for some d (none of q = 44, 51, 52, 68 is in
this case). By steps 1–5, ξ_q ∈ C. By step 7, the Hodge conjecture would then hold for every Fermat and
weighted Fermat variety X^n_m, of every dimension, whose degree lcm(m) = D satisfies: every q' ∈ Q
dividing D is either q or in K_0 ∪ {12, 15, 20, 21, 28, 33, 35, 39, 55, 57}. That is, q is the only open
Q-divisor of D. This is conditional on Lefschetz (1,1) and Kang [step 1], Aoki 1987 [step 2],
Aoki 1983 [step 7] and the cited ingredients of Prop. 3.5 [step 5].

**What a negative outcome proves.** A dual certificate is a set U ⊂ (Z/d) − {0} with U = −U and
d/2 ∉ U. It defines χ_U(v) = Σ_{a∈U} v_a mod 2, a homomorphism R_d → Z/2; y = χ_U/2 is a rational vector
with y·v ∈ Z for every generator v. The certificate claims χ_U = 0 on every generator of Λ_d and
χ_U(ξ_q) = 1. Then ξ_q ∉ Λ_d **unconditionally**: no cited theorem is involved, since this is a
statement about an explicit lattice. In words: in degree d, no Z-linear combination of the following
equals ξ_q:
* linear tuples;
* lifted standard tuples of degrees dividing d;
* G_d-conjugates of the certified exceptional tuples;
* Hodge tuples of length ≤ 6, i.e. Hodge characters of Fermat surfaces and fourfolds of degree d (and
  of weighted ones of degree dividing d), together with their odd-length relatives.

In most degrees χ_U also vanishes on the conjugates of every *other* ξ_{q'}, including uncertified ones
such as ξ_77 or ξ_143. In those degrees ξ_q stays out of reach even if all other exceptional classes of
degree dividing d were algebraic. Both statements concern the **method**: they say nothing about
whether ξ_q ∈ C.
