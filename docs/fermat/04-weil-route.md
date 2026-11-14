# Markman's theorems and the open Fermat classes ξ_44, ξ_51, ξ_52

**Status (2026-11-14).** Markman's theorems prove the Hodge conjecture for every abelian variety of dimension ≤ 5. They
also show that Weil classes are algebraic on all abelian fourfolds of Weil type and on all abelian sixfolds of split
Weil type, for every imaginary quadratic field. Fermat varieties are dominated by products of Fermat curves, whose
Jacobians are CM abelian varieties. So it is natural to ask whether these theorems settle the open degrees 44, 51 and
52. This note answers that question.

* **No, through the Fermat Jacobians in degree q (Theorem W1).** For q = 44, 51, 52, every Hodge class on an abelian
  variety of dimension ≤ 5 built from J(C_q), and every Weil class for an imaginary quadratic field on such an
  abelian variety of any dimension, corresponds to an element of D_q + S_q. These are the classes already known to
  be algebraic.
* **No, through lifts either, in the degrees tested (Theorem W2).** The same holds for J(C_D) with D = 44k, k ≤ 13,
  D = 51k, k ≤ 4, and D = 52k, k ≤ 5. The proof uses the Galois characters of `docs/fermat/03-galois-obstruction.md`.
* **What ξ_q is instead (Theorem W3).** For a CM subfield E of Q(ζ_q), ξ_q is congruent modulo D_q + S_q to a Weil
  class relative to E, on an abelian variety built from J(C_q), if and only if [Q(ζ_q) : E] is odd. The case
  E = Q(ζ_q) gives a **codimension-2** Hodge class on C_q^4, a product of four Fermat curves. The smallest
  realizations are a 16-dimensional abelian variety of Weil type relative to the biquadratic field Q(i, √−11)
  (q = 44, classes of degree 8) and one relative to a CM field of degree 8 (q = 52, classes of degree 4).
* **Control: all exceptional classes with q < 70 (Table 4).** The same route, in degree q, reaches ξ_q exactly for
  q ∈ {12, 15, 20, 21, 39}. In each of these cases ξ_q is congruent to a divisor class on a product of two CM
  elliptic curves, so it is algebraic by Lefschetz (1,1). It fails for the other eleven, which include all six open
  ones: 44, 51, 52, 65, 68 and 69.

The open Fermat degrees are therefore instances of Weil classes relative to **non-quadratic** CM fields. Markman's
general program (arXiv:2509.23403) is set up for any CM field, but its semi-regularity step is carried out only for
imaginary quadratic ones. The realizations in §5 are concrete targets just beyond that range.

Labels follow `CLAUDE.md`. **Theorem** means a complete proof here from the stated inputs, with finite computations
done exactly by `hodge/weil.py` and checked in `tests/test_weil.py`. **Cited** means the source was read for this
note. **Numerical** means an observation at finitely many primes or a solver's optimality claim.

---

## 1. Setting and inputs

R_d is Aoki's formal module: the free Z-module on the nonzero residues mod d. B_d ⊂ R_d is the lattice of Hodge
elements, D_d is spanned by the pairs (a) + (−a) and by (d/2), and S_d by the standard tuples. See
`docs/fermat/02-exceptional-lengths.md` §1 for the conventions. For q ∈ {44, 51, 52}, B_q/(D_q + S_q) has order 2.
Its nonzero class is ξ_q, and it is detected by the parity of λ_44 = n_11 − n_33, λ_51 = n_17 − n_34 and
λ′_52 = n_1 + n_25 − n_27 − n_51 (Theorems D and D′ of `docs/fermat/02`, given the cited index). Write
"parity" for this invariant mod 2.

**Curve characters and the factors of J(C_d).** A curve character is β = (a, b, c) with a + b + c ≡ 0 (mod d) and
a, b, c ≢ 0. Let G = (Z/d)^×. Units act by t·β = (ta, tb, tc).

* (I1, Cited: Deligne, *Hodge cycles on abelian varieties*, §7, Prop. 7.4, 7.6, Cor. 7.7, read for
  `docs/fermat/03`.) H^1 of the Fermat curve C_d splits over C into lines indexed by the curve characters. The line
  of β has type (1,0) or (0,1) according as ⟨a/d⟩ + ⟨b/d⟩ + ⟨c/d⟩ is 1 or 2, up to the global convention
  a ↦ −a, which changes nothing below.
* (I2, Cited: J. S. Milne, *Complex Multiplication*, course notes, Prop. 1.9, 3.12, 3.13 and the proof of 3.13, read
  for this note.) A G-orbit of curve characters spans H^1 of an abelian subvariety A_β of J(C_d), up to isogeny. A_β
  has CM by Q(ζ_d)^{Stab(β)} with CM type Φ_β = {t : t·β of type (1,0)}. Let H = {h ∈ G : Φ_β h = Φ_β}. Then
  (Q(ζ_d)^H, Φ_β) is the primitive CM pair from which Φ_β is induced (Milne 1.9), and A_β is isogenous to
  A′^{[H : Stab]}. Here A′ is simple, of dimension [G : H]/2, with End^0(A′) = Q(ζ_d)^H (Milne 3.13). The eigenlines
  of A′ are the H-cosets tH, and t·β represents the coset.
* (I3, elementary.) Let B be isogenous to a product of such factors. Its cohomology H^k(B) = ∧^k H^1(B) splits into
  eigenlines indexed by k-element multisets of eigencharacters. Send such a line to the element v_1 + … + v_k of R_d,
  the sum of the triples. The line consists of Hodge classes if and only if that element is Hodge. If a Hodge class
  has a nonzero component on such a line, say the class *corresponds to* that element.
* (T, transfer, Cited with a caveat.) The eigenclass of type (v_1, …, v_k) on C_d^k is algebraic if and only if
  the join v_1 ∗ ⋯ ∗ v_k is algebraic on X^{3k−2}_d. An element is algebraic if and only if its class modulo the
  span of algebraic elements is. Lifting to degree dk preserves and reflects algebraicity. These are Shioda's
  inductive structure (Shioda 1979, Theorem II) and MMRV Prop. 3.2 and 3.5 with Remarks 3.5–3.6 (read). MMRV
  state the join for characters of Fermat varieties and prove it through Shioda's blow-up correspondence. For curve
  characters (odd n) we use the same correspondence without re-proving it. Only the interpretations below (the
  Corollaries) use (T). Theorems W1–W3 are statements about elements of B_q and use only (I1)–(I3).

**Markman's results (Cited: arXiv:2502.03415 abstract; arXiv:2509.23403 abstract, §1.1, §1.2, §11, read via the
arXiv HTML).** The Weil classes are algebraic on every abelian sixfold of Weil type with discriminant −1 (split), for
every imaginary quadratic field. By Schoen's degeneration argument they are algebraic on every abelian fourfold of
Weil type. The Hodge conjecture holds for all abelian varieties of dimension ≤ 5. The general framework of
arXiv:2509.23403 is described in §6.

## 2. The simple factors

`scripts/weil_route.py` §1.1 lists all orbits. In summary:

| q | dim A′ = 1 | dim A′ = 2 | dim A′ = 5, 6, 8 | top dimension φ(q)/2 | factors with odd-parity eigencharacters |
|---|---|---|---|---|---|
| 44 | E_i from (11,11,22); E_{√−11} from (2,6,36), as A_β ≅ E^5 | — | ten of dimension 5: eight with CM by Q(ζ_11), two by Q(i)·Q(ζ_11)^+ | ten of dimension 10 | only (1,10,33), (1,11,32), both of dimension 10 |
| 51 | E_ω from (17,17,17), CM by Q(√−3) | — | five of dimension 8 | eleven of dimension 16 | (17,17,17), (1,16,34) (dim 8), (1,17,33) (dim 16) |
| 52 | E_i from (13,13,26) | two, from (4,12,36) and (2,14,36) | eleven of dimension 6 | twelve of dimension 12 | the twelve factors of dimension 12 |

**Table 1.** Simple factors A′ of J(C_q) up to isogeny (Computation, exact).

## 3. Theorem W1: degree q

**Theorem W1.** Let q ∈ {44, 51, 52}, and let B be an abelian variety isogenous to a quotient of J(C_q)^m.

1. If dim B ≤ 5, every Hodge class of B corresponds only to elements of D_q + S_q.
2. If B is of Weil type relative to an imaginary quadratic field K ⊂ End^0(B), its Weil classes correspond only to
   elements of D_q + S_q.

*Proof.* (1) B is isogenous to a product of simple factors of dimension ≤ 5 (Poincaré reducibility, I2). By (I3) a
Hodge class of B corresponds to Hodge elements supported on the eigencharacters of those factors.
`weil.small_factor_generators` computes a Z-basis of all Hodge elements supported on the eigencharacters of all
simple factors of dimension ≤ 5, with every representative t·β and every multiplicity. That gives 112, 1 and 15 basis
elements for q = 44, 51, 52, and each has even parity. By Theorems D and D′ they lie in D_q + S_q.
For q = 44 and 52 one can see this directly: no eigencharacter of a small factor has odd parity (Table 1). For
q = 51 the only small factor is E_ω. A Hodge element on E_ω^a uses its two eigencharacters (17,17,17) and
(34,34,34) equally often, so λ_51 = 3n − 3n = 0.

(2) This is the case [Q(ζ_q) : K] = φ(q)/2, which is even, of Theorem W3 below. A direct check: by Lemma 5.1 the Weil
elements relative to K are, modulo D_q, the sums Σ c_j h_j of the K-halves h_j of the factors whose CM field
contains K, with Σ c_j m_j = 0, where m_j is the signature defect of h_j. `weil.weil_generators` computes a basis of
these. There are 30, 23 and 27 generators over both imaginary quadratic fields of each Q(ζ_q). All are Hodge and all
have even parity. ∎

For q = 44 the reason is visible. On the eigencharacters of A_β, λ_44(t·β) = χ_4(t)·λ_44(β), and λ_44(β) is odd
only for the two 10-dimensional factors. A K-half of such a factor is a sum over a coset of a group of order 10. Over
that coset χ_4 is constant (K = Q(i)) or balanced (K = Q(√−11)). Either way the sum is even.

**Corollary W1′ (given T and MMRV).** Markman's theorems, applied to abelian varieties built from J(C_q), give only
classes in D_q + S_q. MMRV prove those algebraic with linear and standard cycles. They therefore add no case of HC
for X^n_q, q = 44, 51, 52.

## 4. Theorem W2: lifts

Through the lift R_q → R_D, (a) ↦ (ka) with D = qk, the open class can also be attacked with the factors of J(C_D).
There are many more small factors there, such as those with CM by Q(ζ_8) or Q(√−2) when 8 | D.

**Theorem W2.** For (q, D) with D = 44k (1 ≤ k ≤ 13), 51k (k ≤ 4) or 52k (k ≤ 5), lift_D(ξ_q) is not in
Λ_D + W_D + H_D. Here Λ_D is the lattice of `docs/fermat/03` (linear and standard tuples, all Hodge tuples of length
≤ 6). W_D is spanned by the Weil elements relative to all imaginary quadratic fields in Q(ζ_D) of abelian varieties
built from J(C_D). H_D is spanned by the Hodge elements supported on simple factors of J(C_D) of dimension ≤ 5.

*Proof.* ε is a homomorphism on even-length Hodge elements (`docs/fermat/03` §1). Compute ε exactly, by
Stickelberger's congruence, at the first 24 primes l ≡ 1 (mod 2D) for: the generators of Λ_D, the Weil generators
of every imaginary quadratic field (`weil.weil_generators`), and a Z-basis of H_D (`weil.small_factor_generators`).
In every case the exponent vector of lift_D(ξ_q) is not in the lattice they generate together with 2D·Z^24
(`results/weil_route.md` §3). A relation in the character group would hold at every prime. ∎

*Observation (Numerical).* In every degree tested, every Weil generator and every small-factor generator already has
its character in ⟨ε(Λ_D)⟩ at these 24 primes, so W_D and H_D add no new characters. This fits Theorem L′. The open
classes need Anderson's square root for the pair {2, 11}, {3, 17} or {2, 13}. A Weil class relative to an imaginary
quadratic field K has a character that is the restriction of a character of Gal(Q̄/K), with values in μ(K). None
of the classes tested produces the needed root.

**Corollary W2′ (given T).** For these D, Markman's theorems applied to abelian varieties built from J(C_D) do not
reach ξ_q either.

## 5. Theorem W3: relative to which CM fields ξ_q is a Weil class

Let E ⊂ Q(ζ_q) be a CM subfield and N = Gal(Q(ζ_q)/E) ⊂ G, so −1 ∉ N. Fix a factor A′ = A′_β with group H. The
field E acts on A′^{[H : N∩H]} through E·E′ = Q(ζ_q)^{N∩H}, since E ⊗ E′ is a product of copies of that field. For
each embedding τ of E, the τ-part of H^1 is spanned by [N : N∩H] eigencharacters: the t·β with t running over the
H-cosets inside one coset g·NH. Call this sum an **E-half unit** u = u(β, g). It has cost [H : N∩H]·dim A′, the
dimension of the abelian variety on which E acts this way (`weil.e_weil_units`).

**Lemma 5.1.** Let B be built from J(C_q) and of Weil type relative to E (in the sense of §6). Then each τ-part of
its Weil classes corresponds to a sum of E-half units with non-negative coefficients. Conversely, a non-negative sum
of units that is a Hodge element is the τ_0-part of the Weil classes of such a B. The Weil-type condition, that
dim H^{1,0}_σ = dim H^{0,1}_σ for every σ, is exactly the Hodge condition on the τ-parts, one for each embedding τ
of E.

*Proof.* End^0(B) = ∏ M_{m_j}(E′_j) (I2), so E′_j^{m_j} is a module over E ⊗ E′_j. That ring is a product of fields
isomorphic to E·E′_j, of degree [H_j : N∩H_j] over E′_j. So the isotypic part A′_j^{m_j} is isogenous, compatibly
with E, to a product of pieces A′_j^{[H_j : N∩H_j]}. On each piece E acts through one factor field. The τ-part of a
piece consists of the eigenlines of the embeddings of E·E′_j that extend τ. These are the [N : N∩H_j] cosets of N∩H_j
in τ's coset, and they restrict to distinct eigencharacters of A′_j. The Weil classes for τ are the top exterior power
of the τ-part (I3). For the converse, take B to be the product of the pieces. ∎

**Theorem W3.** Let q ∈ {44, 51, 52} and E ⊂ Q(ζ_q) a CM subfield. Some integer combination of E-half units is a
Hodge element of odd parity if and only if [Q(ζ_q) : E] is odd. For these E, Table 3 gives a non-negative
realization, so the Weil classes of an explicit abelian variety of Weil type relative to E correspond to an element
congruent to ξ_q modulo D_q + S_q. For [Q(ζ_q) : E] even, no abelian variety of Weil type relative to E built from
J(C_q) has Weil classes reaching ξ_q.

*Proof.* `weil.odd_e_weil_exists` computes, for each of the 6, 9 and 10 CM subfields of Q(ζ_44), Q(ζ_51) and
Q(ζ_52), a Z-basis of the lattice of Hodge integer combinations of all E-half units, and evaluates the parity on it.
A negative coefficient stands for the complex-conjugate unit, which is again a unit. The parity is odd somewhere
exactly when |N| is odd (`results/weil_route.md` §1.3, `tests/test_weil.py::test_theorem_W3`). The realizations of
Table 3 are verified to be Hodge, with odd parity (`test_realizations`), and are non-negative sums of units. By
Lemma 5.1 they are Weil classes of the stated abelian varieties. ∎

| q | E | [E : Q] | abelian variety B of Weil type relative to E | dim B | d = dim_E H^1 (degree of the Weil classes) | element of R_q (one τ-part) |
|---|---|---|---|---|---|---|
| 44 | Q(i, √−11) | 4 | A′_(1,11,32) × E_i^6 | 16 | 8 | (4,7,11,11,11,11,11,11,12,16,19,20,22,22,22,33,33,33,33,33,35,36,39,43) |
| 44 | Q(ζ_44) | 20 | A′_(1,6,37) × A′_(1,10,33) × A′_(1,12,31) × A′_(1,13,30) | 40 | 4 | (3,7,11,18,18,21,23,26,27,32,35,43) |
| 51 | Q(ζ_51) | 32 | A′_(1,4,46)^2 × A′_(1,7,43) × A′_(1,17,33) | 64 | 4 | (5,5,8,11,14,17,32,38,39,41,46,50) |
| 52 | Q(ζ_52)^{⟨9⟩}, the compositum of Q(i) and the quartic CM subfield of Q(ζ_13) | 8 | A′_(1,5,46) × A′_(4,12,36)^2 | 16 | 4 | (8,14,15,19,20,22,23,24,31,42,43,51) |
| 52 | Q(ζ_52) | 24 | A′_(1,4,47) × A′_(1,6,45)^2 × A′_(1,9,42) | 48 | 4 | (1,6,8,15,17,21,29,37,37,45,46,50) |

**Table 3.** Realizations of ξ_q (mod D_q + S_q) as Weil classes relative to E. The table lists one realization for
every E with [Q(ζ_q) : E] odd. The units, with twists, are `weil.REALIZATIONS`. The dimensions are the minimum found
by a MILP search over all non-negative unit combinations (`scripts/weil_route.py --search`). Optimality is the
solver's claim (Numerical). The realizations themselves are verified exactly.

For q = 44 and E = Q(i, √−11), E acts on A′_(1,11,32) (dimension 10, CM by Q(ζ_44) ⊃ E) through the embedding
twisted by 7. It acts on each E_i^2 through E ↪ M_2(Q(i)). The four embeddings of E give four Hodge τ-parts, each
with 5 + 3 eigencharacters (`test_realization_44_c5_is_e_weil`). There is a polarization compatible with E. On E_i^2
take the product polarization and send √11 to a matrix S ∈ M_2(Q(i)) with S̄^T = S and S^2 = 11, for instance
S = [[1, 1+3i], [1−3i, −1]]. Its Rosati involution then restricts to complex conjugation on E.

**Corollary W4 (given T and MMRV's reduction).** The Hodge conjecture for all Fermat varieties of degree 44 (any
dimension) is equivalent to each of the following.

1. The Weil classes of the 16-dimensional abelian variety A′_(1,11,32) × E_i^6, relative to E = Q(i, √−11), are
   algebraic.
2. The Hodge classes of type (β_1, β_2, β_3, β_4) on C_44^4 are algebraic, with β_1 = (3,18,23), β_2 = (7,11,26),
   β_3 = (21,32,35), β_4 = (18,27,43). These are codimension-2 classes on a product of four Fermat curves.

The analogous statements hold for 52 (the 16-dimensional variety of Table 3, or four curve characters) and for 51
(four curve characters on C_51^4).

*Proof.* MMRV (Theorem 4.1 with Aoki's Theorem 4.2) reduce HC for all degree-44 Fermat varieties to ξ_44 ∈ C_44.
The elements of Table 3 have odd λ_44, so they are congruent to ξ_44 modulo D_44 + S_44 ⊂ C_44 (Theorem D). By (T)
they are algebraic exactly when ξ_44 is. By (I3) and (T), each is algebraic exactly when the corresponding
eigenclass on B, respectively on C_44^4, is. ∎

*Remark (fields of definition).* The character of each element in Table 3 is ε(ξ_q) times a character of
D_q + S_q. By Theorem L′ of `docs/fermat/03`, a cycle realizing any of these Weil classes must be defined over a
field containing Anderson's square root for the pair {2, 11} (q = 44), {3, 17} (q = 51) or {2, 13} (q = 52).

### 5.1 Control: all exceptional classes with q < 70

MMRV list sixteen exceptional classes ξ_q with q < 70, each with [B_q : D_q + S_q] = 2. For q ∉ {44, 51, 52} the
parity is the mod-2 functional of `weil.parity_functional`, which kills D_q + S_q and is 1 on B_q \ (D_q + S_q). For
44, 51 and 52 it agrees with λ on every element tested.

| q | status of ξ_q (MMRV) | odd-index criterion | odd element on factors of dim ≤ 5 | odd Weil element, K imaginary quadratic | divisor on E × E′ congruent to ξ_q |
|---|---|---|---|---|---|
| 12 | algebraic | fails | yes | yes | (1,1,10) + (4,9,11) |
| 15 | algebraic | fails | yes | yes | (1,2,12) + (5,11,14) |
| 20 | algebraic | fails | yes | yes | (1,1,18) + (4,17,19) |
| 21 | algebraic | fails | yes | yes | (1,4,16) + (5,18,19) |
| 28 | algebraic | holds | no | no | — |
| 33 | algebraic | holds | no | no | — |
| 35 | algebraic (via degree 70) | holds | no | no | — |
| 39 | algebraic | fails | yes | yes | (1,16,22) + (7,34,37) |
| 44 | **open** | holds | no | no | — |
| 51 | **open** | holds | no | no | — |
| 52 | **open** | holds | no | no | — |
| 55 | algebraic (via degree 110) | holds | no | no | — |
| 57 | algebraic (via degree 114) | holds | no | no | — |
| 65 | **open** (q > 64) | holds | no | no (Q(ζ_65) has no imaginary quadratic subfield) | — |
| 68 | **open** (q > 64) | holds | no | no | — |
| 69 | **open** (q > 64) | holds | no | no | — |

**Table 4** (Computation, exact; `results/weil_route.md` §1.4, `tests/test_weil.py`). The last column shows two
eigencharacters of CM elliptic-curve factors of J(C_q) whose sum is a Hodge element of odd parity. That sum is a
divisor class on E × E′, algebraic by Lefschetz (1,1). For q = 39 both lie on the same curve, so the divisor is the
graph of a complex multiplication.

**Observation.** For q < 70 the dichotomy is sharp. When the odd-index criterion fails, ξ_q is already a divisor
class on a product of two CM elliptic curves. When it holds, no Hodge class on a factor of dimension ≤ 5, and no
imaginary-quadratic Weil class built from J(C_q), reaches ξ_q. So in degree q, Markman's theorems reach exactly the
classes that Lefschetz (1,1) already gives. The degrees 28, 33, 35, 55 and 57 show that the criterion does not decide
algebraicity: those ξ_q are algebraic by MMRV's explicit cycles, in degree q or after lifting, although the Weil
route misses them.

**The open degrees beyond MMRV's range (Numerical: MILP minima, solutions verified exactly; `results/weil_route.md`
§2).** For q = 65, 68 and 69 the smallest realizations are larger than for 44, 51 and 52.

* q = 69: Weil classes of degree 12 relative to the biquadratic field Q(√−3, √−23), on A′_(1,19,49) × E_ω^2
  (dimension 24). This is the analogue of Q(i, √−11) for q = 44. Relative to Q(ζ_69), there is one of degree 6 on a
  132-fold.
* q = 65: degree 10 relative to the CM field of degree 16 fixed by the subgroup of order 3, on an 80-fold. Relative
  to Q(ζ_65), degree 6 on a 144-fold.
* q = 68: degree 6 relative to Q(ζ_68), on a 96-fold. Here (Z/68)^× has no nontrivial subgroup of odd order.

## 6. Relation to Markman's program and to André's theorem

In arXiv:2509.23403 (§1.1, read), K is a CM field with totally real subfield F and [K : Q] = e. X is an abelian
variety with F ⊂ End^0(X), and the construction gives η : K → End^0(X × X̂). With d = dim_K H^1 = 4 dim X/e, the pair
is of Weil type if dim H^{1,0}_σ = dim H^{0,1}_σ = d/2 for every embedding σ of K. The Weil classes are
∧^d_K H^1(A, Q), Hodge classes of degree d, a K-line. It is of *split* Weil type if the hermitian form has an
isotropic subspace of half the dimension. Theorem 1.4 there (André) states that every Hodge class on a CM abelian
variety is a sum of pullbacks of Weil classes of abelian varieties of split Weil type. The three-step strategy of §4
is described for general K. The semi-regularity step is "currently able to handle it only for dim(X)≤3", which
"forces K … to be a quadratic imaginary number field" (§11).

In this language, Table 3 gives explicit cases of André's theorem for the open Fermat classes:

| realization | e = [K : Q] | d | dim A | dim X = dim A / 2 |
|---|---|---|---|---|
| 44, K = Q(i, √−11) | 4 | 8 | 16 | 8 |
| 52, K of degree 8 | 8 | 4 | 16 | 8 |
| 44, K = Q(ζ_44) | 20 | 4 | 40 | 20 |
| 52, K = Q(ζ_52) | 24 | 4 | 48 | 24 |
| 51, K = Q(ζ_51) | 32 | 4 | 64 | 32 |

Theorem W3 shows that the imaginary quadratic case cannot occur. The smallest cases need the strategy for
non-quadratic K with dim X = 8.

*Remark (split type, Heuristic; not verified here).* Whether these B can be polarized to be of split Weil type is not
checked. Each realization has a piece of odd E-dimension. Rescaling its polarization by a totally positive element u
of F multiplies the discriminant of the hermitian form by u, modulo norms from E, and keeps the signatures. By the
classification of hermitian forms over CM fields (Landherr; not re-read), this should reach the split class. Whether
B can also be written as X × X̂ with η of Markman's form is a separate question.

## 7. Open questions

1. **(Main.)** Prove that the Weil classes of A′_(1,11,32) × E_i^6, relative to Q(i, √−11), are algebraic. Or do the
   same for the 16-dimensional variety for q = 52. Either would settle the corresponding degree, by Corollary W4.
2. Is dimension 16 minimal among all abelian varieties carrying a class congruent to ξ_44, including those built from
   lifts J(C_{44k})? Theorem W3 concerns only J(C_q). The MILP minimum is Numerical.
3. Does Theorem W2 hold for every k? A proof for all k would need a degree-free argument, like Theorem L′ for the
   fields of definition.
4. Explain the dichotomy of §5.1 conceptually. Why does the odd-index criterion fail exactly when ξ_q is a divisor
   class on a product of two CM elliptic curves? Does this persist for every q ∈ Q? For the open degrees 65, 68, 69,
   compute the smallest realizations and run the lift test of Theorem W2.

## 8. Reproduction

```bash
python3 -m pytest -q tests/test_weil.py
python3 scripts/weil_route.py 572 --search    # writes results/weil_route.md (about 30 minutes; --search needs scipy)
python3 scripts/weil_route.py 572 --search --skip-lifts   # sections 1-2 only, keeping section 3 (a few minutes)
```

Code: `hodge/weil.py`, pure Python with exact integers. The script also uses `scripts/galois_obstruction.py` (numpy
and the C enumerator) for Λ_D in §4.
