# Exact lengths of the exceptional tuples ξ_q for q = 4p and q = 3p

**Status (2026-11-09).** This note proves a closed formula for the Aoki–Shioda length ℓ_{2,q}(ξ_q) of the exceptional
tuple ξ_q for two infinite families of degrees, q = 4p with p ≡ 3 (mod 4) prime and q = 3p with p ≡ 2 (mod 3) prime
(Theorem D). The lower bound is a complete proof here. The upper bound is an explicit tuple. The identification of the
minimum with ℓ_{2,q}(ξ_q) uses the Kubert–Aoki index theorem, which this repository recomputes for every q ≤ 420 in the
families. The formula reproduces all 31 entries of Miranda–Movasati–Rufino–Villaflor's Table 1 that lie in these
families, so those upper bounds are optimal.

**What this is not.** It says nothing about whether ξ_q is algebraic, so it proves no new case of the Hodge conjecture.
It is a statement about one method: in degree q, the length-reduction method of MMRV (§4.3–4.4 of arXiv:2609.27301)
cannot settle ξ_q unless the formula gives at most 6. In the two families that happens only for q ∈ {12, 15, 28, 33}.
Lifts to multiples of q are not covered (§5).

Labels follow `CLAUDE.md`: **Theorem** = complete proof in this note; **Cited** = used as a black box, source read;
**Computation** = exact integer computation reproducible by the commands in §6.

Sources. MMRV = M. Miranda, H. Movasati, L. Rufino, R. Villaflor, *Lengths of Hodge characters in Fermat varieties*,
arXiv:2609.27301v2 (read in full for this note: Definitions 3.7, 4.1–4.10, Theorems 4.1–4.3, Proposition 4.4,
Conjecture 4.1, Tables 1–4). For generalized Bernoulli numbers: L. Washington, *Introduction to Cyclotomic Fields*,
2nd ed., Ch. 4. Everything about Bernoulli numbers that the proofs use is proved below, except that B_{1,χ} ≠ 0 for a
primitive odd character χ (Washington, Cor. 4.4 together with Thm 4.9 and L(1, χ̄) ≠ 0).

---

## 1. Setting

R_q is the free Z-module on the residues a ∈ Z/q, a ≠ 0. A tuple (a_1, …, a_L) is the element Σ_i (a_i); its
length is ℓ = L, and for a general element ℓ(Σ n_a (a)) = Σ |n_a| (MMRV Def. 4.10). A tuple is a **Hodge tuple** of
degree q if Σ_i {t a_i / q} = L/2 for every t ∈ (Z/q)^×, where {x} is the fractional part. B_q ⊂ R_q is the lattice they
span, D_q the span of the pairs (a) + (−a) and of ε = (q/2) when q is even, and S_q the span of the standard tuples of
MMRV Def. 3.7 of every degree dividing q, lifted to degree q (as in the authors' code, which is the reading that MMRV
Theorem 4.2 needs; see `docs/fermat/01-span-test.md`, step 7). Then

  ℓ_{2,q}(α) = min{ ℓ(α′) : α − α′ ∈ D_q + S_q },   f_0(q) = min{ ℓ_{2,q}(α) : α ∈ B_q \ (D_q + S_q) }

(MMRV (29) and Remark 4.14). By MMRV Remark 4.11, α′ can be taken with non-negative coefficients; if α ∈ B_q it is then
a Hodge tuple.

**The two families.** Fix (m, r) = (4, 2) or (3, 3). Let p be a prime with χ_m(p) = −1, where χ_4 and χ_3 are the odd
quadratic characters of conductor 4 and 3; that is, p ≡ 3 (mod 4), respectively p ≡ 2 (mod 3) and p ≥ 5. Put
q = m p. These are the elements of MMRV's set Q with two prime factors, one of them 4 or 3, for which χ_m(p) = −1. The
only element of Q dividing q is q itself.

**Invariants.** For α = Σ n_a (a) ∈ R_q and x ∈ (Z/p)^× put

* λ(α) = n_p − n_{(m−1)p}: the signed count of the two entries of order m (they are p·1 and p·(m−1));
* U(α) = Σ_{a unit} n_a χ_m(a);
* g(x) = Σ_{a unit, a ≡ x (p)} n_a χ_m(a) and h(x) = Σ_{a unit, a ≡ x (p)} n_a;
* P(x) = Σ n_a over the entries of order p with a/m ≡ x (mod p) (these are a = m·x̃);
* for m = 4 only, Q(x) = Σ n_a over the entries of order 2p with a/2 ≡ x (mod p).

For a function F on (Z/p)^× write F^±(x) = (F(x) ± F(−x))/2 and F̂(ψ) = Σ_x F(x) ψ̄(x). The order of r in (Z/p)^×
is o = ord_p(r), and

  c_r(p) = (p − 1)/o if o is even (equivalently −1 ∈ ⟨r⟩),   c_r(p) = 0 if o is odd.

For q = 44 this λ is the invariant λ_44 = n_11 − n_33 of `docs/attacks/17-fermat-open-cases.md`; for q = 51 it is
λ_51 = n_17 − n_34.

## 2. The Hodge condition through odd characters

For a Dirichlet character χ mod q put S_χ(a) = Σ_{t ∈ (Z/q)^×} χ(t) {t a / q}.

**Lemma 1 (Theorem).** v = Σ v_a (a) ∈ R_q lies in B_q if and only if Σ_a v_a S_χ(a) = 0 for every odd character χ
mod q.

*Proof.* B_q is the kernel lattice {v : F_v(t) = 0 for all units t}, F_v(t) = Σ_a v_a ({ta/q} − 1/2)
(`docs/fermat/01-span-test.md`, Lemma 1). Since {−x} = 1 − {x} for x ∉ Z, F_v is an odd function on the finite abelian
group (Z/q)^×. An odd function vanishes iff its Fourier coefficients Σ_t χ(t) F_v(t) vanish for all odd χ; the even ones
vanish automatically. Finally Σ_t χ(t) = 0 for χ ≠ 1, so Σ_t χ(t) F_v(t) = Σ_a v_a S_χ(a). ∎

**Lemma 2 (Theorem).** Let χ have conductor f and associated primitive character χ_0. Let a ≠ 0 have order e, and
write a = (q/e) a′ with a′ ∈ (Z/e)^×. If f ∤ e then S_χ(a) = 0. If f | e then

  S_χ(a) = (φ(q)/φ(e)) · χ̄_0(a′) · B_{1,χ_0} · ∏_{ℓ | e prime, ℓ ∤ f} (1 − χ_0(ℓ)),   B_{1,χ_0} = (1/f) Σ_{s=1}^{f} χ_0(s) s.

*Proof.* {ta/q} = {ta′/e} depends only on t mod e. The reduction (Z/q)^× → (Z/e)^× is onto with kernel K of order
φ(q)/φ(e), and χ is trivial on K iff it factors through (Z/e)^×, iff f | e. If not, the sum over each coset of K
vanishes. If so, S_χ(a) = (φ(q)/φ(e)) Σ_{s ∈ (Z/e)^×} χ_0(s){s a′/e} = (φ(q)/φ(e)) χ̄_0(a′) Σ_{s ∈ (Z/e)^×} χ_0(s) s/e.
For the last sum, let e′ be the product of the primes dividing e but not f. Since χ_0(s) = 0 when gcd(s, f) > 1,
Möbius inversion over the divisors d | e′ gives Σ_{s ∈ (Z/e)^×} χ_0(s) s/e = Σ_{d | e′} μ(d) χ_0(d) (1/M) Σ_{s=1}^{M} χ_0(s) s
with M = e/d. M is a multiple of f, and for any multiple M of f the inner average equals B_{1,χ_0}: split 1..M into
M/f blocks and use Σ_{s=1}^{f} χ_0(s) = 0. So the sum is B_{1,χ_0} Σ_{d|e′} μ(d) χ_0(d) = B_{1,χ_0} ∏_{ℓ|e′}(1 − χ_0(ℓ)). ∎

B_{1,χ_4} = −1/2 and B_{1,χ_3} = −1/3; for every primitive odd χ_0, B_{1,χ_0} ≠ 0 (**Cited**: Washington, Thm 4.9 and
Cor. 4.4, from L(1, χ̄_0) ≠ 0). Lemma 2 was also checked numerically against the definition of S_χ for every odd
character and every a, for q ∈ {12, 15, 28, 33, 44, 51, 52, 69, 76}; the largest discrepancy was about 10^{-13}.

## 3. Three consequences of the Hodge condition

The odd characters mod q = m p are, through (Z/q)^× ≅ (Z/m)^× × (Z/p)^×: χ_m; χ_m ψ with ψ even and nontrivial mod p;
and ψ with ψ odd mod p. Lemmas 3–5 apply Lemmas 1 and 2 to each kind in turn. Since B_{1,·} ≠ 0, each
equation is equivalent to the vanishing of Σ_a v_a S_χ(a) for the characters of that kind. Hence:

> v ∈ B_q **if and only if** the identities of Propositions 3, 4 and 5 hold for v.

**Proposition 3 (Theorem).** For every v ∈ B_q: (p − 1) λ(v) + 2 U(v) = 0.

*Proof.* Take χ = χ_m (conductor m). By Lemma 2 only entries whose order is divisible by m contribute, that is, orders m
and q. For a = p a′ of order m: S = (p − 1) χ_m(a′) B_{1,χ_m}, since φ(q)/φ(m) = p − 1 and there is no Euler factor;
χ_m(a′) = +1 for a = p and −1 for a = (m−1)p. For a unit a: S = χ_m(a) B_{1,χ_m} (1 − χ_m(p)) = 2 χ_m(a) B_{1,χ_m}.
(For m = 4 the prime 2 divides the conductor, so p is the only Euler factor.) Divide by B_{1,χ_m} ≠ 0. ∎

**Proposition 4 (Theorem).** For every v ∈ B_q and every x ∈ (Z/p)^×: g(x) + g(−x) = −λ(v).

*Proof.* For ψ even and nontrivial mod p, χ = χ_m ψ is primitive of conductor q, so by Lemma 2 only units contribute,
with S_χ(a) = χ̄(a) B_{1,χ}. Hence ĝ(ψ) = Σ_{units} n_a χ_m(a) ψ̄(a) = 0 for every nontrivial even ψ. The even part g^+
then has vanishing Fourier coefficients at every nontrivial character, so it is constant, equal to its mean
Σ_x g(x)/(p − 1) = U/(p − 1) = −λ/2 by Proposition 3. ∎

**Proposition 5 (Theorem).** For every v ∈ B_q, put G = h + 2Q if m = 4 and G = h if m = 3. Then for every x:

  G^−(x) − G^−(r x) = −(P(x) − P(−x)).

*Proof.* Let ψ be odd mod p and χ = ψ composed with Z/q → Z/p; it is odd of conductor p, so only entries of order
divisible by p contribute. For m = 4 these have order p, 2p or 4p, and Lemma 2 gives S = 2ψ̄(a′)B, 2(1 − ψ(2))ψ̄(a′)B and
(1 − ψ(2))ψ̄(a)B, with B = B_{1,ψ} (φ(4p)/φ(p) = φ(4p)/φ(2p) = 2; the Euler factor at 2 appears for e = 2p, 4p). So
2P̂(ψ) + (1 − ψ(2))(2Q̂(ψ) + ĥ(ψ)) = 0. For m = 3 the orders are p and 3p, and 2P̂(ψ) + (1 − ψ(3)) ĥ(ψ) = 0. In both cases
2P̂(ψ) + (1 − ψ(r)) Ĝ(ψ) = 0. Now ψ(r) Ĝ(ψ) = Σ_x G(rx) ψ̄(x), so the function 2P + G − G∘r has vanishing Fourier
coefficients at every odd ψ. Its odd part therefore vanishes, and taking odd parts commutes with x ↦ rx. ∎

## 4. The theorem

**Theorem D.** Let q = m p be in one of the two families, with r and c_r(p) as in §1.

1. **(Lower bound; Theorem.)** Every Hodge tuple α of degree q with λ(α) odd has at least (p − 1)/2 entries that are
   units, at least one entry of order m, and, when o = ord_p(r) is even, at least (p − 1)/o entries of order p. Hence
   ℓ(α) ≥ (p + 1)/2 + c_r(p).
2. **(Attained; Theorem.)** Let H ⊂ (Z/p)^× and P be defined as follows. If o is odd, H is a union of cosets of ⟨r⟩
   containing exactly one of each pair of cosets C, −C, and P = 0. If o is even, choose one w in each coset C of ⟨r⟩ (then
   C = −C), put H ∩ C = {r w, r² w, …, r^{o/2} w}, and add the entry m·w of order p. The tuple τ_q consists of these
   entries, the units u ≡ 1 (mod m) with u mod p ∈ H, and the entry (m − 1)p. It is a Hodge tuple with λ(τ_q) = −1
   and ℓ(τ_q) = (p + 1)/2 + c_r(p).
3. **(Parity; Theorem.)** λ is even on D_q and on every standard tuple of degree q, so λ(D_q + S_q) ⊂ 2Z.
4. **(Exact value.)** Suppose [B_q : D_q + S_q] ≤ 2. This holds by Kubert–Aoki (MMRV Thm 4.3 with Thm 4.2, **Cited**),
   and by **Computation** for every q ≤ 420 in the families. Then D_q + S_q = {v ∈ B_q : λ(v) even} and

     f_0(q) = ℓ_{2,q}(ξ_q) = (p + 1)/2 + c_r(p).

   The equality with ℓ_{2,q}(ξ_q) uses ξ_q ∉ D_q + S_q. This follows from Aoki's generation theorem (MMRV Thm 4.2,
   **Cited**): B_q/(D_q + S_q) is generated by ξ_q, and by part 2 and part 3 it is not zero.

*Proof of 1.* Entries of order m: n_p + n_{(m−1)p} ≥ |λ| ≥ 1. Units: for each of the (p − 1)/2 pairs {x, −x},
Proposition 4 gives |g(x)| + |g(−x)| ≥ |λ| ≥ 1, and h(x) + h(−x) ≥ |g(x)| + |g(−x)|. So every pair carries a unit entry.
Entries of order p: since g and h count the same entries with signs ±1, h ≡ g (mod 2), and so
h(x) − h(−x) ≡ g(x) + g(−x) = −λ ≡ 1 (mod 2). Thus h^−(x) ∈ ½ + Z, and G^−(x) ∈ ½ + Z because 2Q^−(x) ∈ Z. In particular
G^− never vanishes. Let o be even, let C = x⟨r⟩, and put x_j = r^j x, so that x_{o/2} = −x. Summing Proposition 5 over
j = 0, …, o/2 − 1 gives

  Σ_j (P(x_j) − P(−x_j)) = −(G^−(x_0) − G^−(x_{o/2})) = −2 G^−(x) ≠ 0,

so some x_j or −x_j, both in C, has P > 0. Each of the (p − 1)/o cosets therefore carries an entry of order p. The
three kinds of entries have different orders, so they are distinct. ∎

*Proof of 2.* By the boxed equivalence of §3, it suffices to check Propositions 3–5 for τ_q. λ = −1, and the
(p − 1)/2 units all have χ_m = 1, so U = (p − 1)/2 and Proposition 3 holds. Here g = h = 1_H with g(x) + g(−x) = 1 for
all x, which is Proposition 4. For Proposition 5 (with Q = 0), G^− = 1_H − ½. If o is odd, 1_H is ⟨r⟩-invariant and
P = 0. If o is even, on the coset of w we have 1_H(r^j w) = 1 exactly for j ≡ 1, …, o/2 (mod o). So
G^−(x) − G^−(rx) equals −1 at x = w, +1 at x = r^{o/2}w = −w, and 0 elsewhere on the coset. That is −(P(x) − P(−x))
for P = δ_w. ∎

*Proof of 3.* For a pair, λ((a) + (−a)) = 0 because −p = (m − 1)p, and λ(ε) = 0. Standard tuples of degree d′ | q
with d′ = p′k, k ≥ 3 (MMRV Def. 3.7):

* m = 4. (i) s_{p,i} of degree 4p (k = 4): (i, i+4, …, i+4(p−1), −p i) with p ∤ i. The progression hits every residue mod p
  once, so exactly one of its terms, z, is divisible by p, and z ≡ i (mod 4). If i is odd, z = p·(i p⁻¹ mod 4) =
  p·(−i mod 4) because p ≡ −1 (mod 4). This is the last entry −p i, so λ = ±2. If i ≡ 2 (mod 4), both multiples of p
  equal 2p and λ = 0. If 4 | i, an entry vanishes. (ii) s_{2,i} of degree 4p (k = 2p): (i, i+2p, −2i, 2p) with i odd.
  If i ∈ {p, 3p}, the first two entries are p and 3p and cancel. Otherwise no entry has order 4 (−2i ≡ 2 mod 4). So
  λ = 0. (iii) s_{2,i} of degree 2p (k = p) lifts to even entries, which never have order 4.
* m = 3. (i) s_{3,i} of degree 3p (k = p): (i, i+p, i+2p, −3i) with 3 ∤ i. If p ∤ i, no entry is divisible by p
  (the entries are ≡ i and −3i mod p), so none has order 3 and λ = 0. If p | i, an entry vanishes. (ii) s_{p,i} of degree 3p (k = 3):
  (i, i+3, …, i+3(p−1), −p i) with p ∤ i. If 3 ∤ i, the unique term divisible by p is p·(i p⁻¹ mod 3) =
  p·(−i mod 3), which equals −p i, so λ = ±2. If 3 | i, the entry −p i vanishes.

No other divisor d′ of q has the form p′k with k ≥ 3. ∎

*Proof of 4.* By parts 2 and 3, τ_q ∈ B_q \ (D_q + S_q), so the index is exactly 2 and
D_q + S_q = B_q ∩ {λ even}. Every α ∈ B_q \ (D_q + S_q) then has λ odd, and so does every α′ with α − α′ ∈ D_q + S_q.
Normalise α′ to non-negative coefficients (MMRV Remark 4.11); it is a Hodge tuple, so part 1 gives
ℓ(α′) ≥ (p+1)/2 + c_r(p). Part 2 gives equality. ∎

**Corollary E (Theorem, given the cited index).** f_0(q) ≥ (q + m)/(2m) on both families. So f_0 restricted to
these degrees has finite fibres: MMRV Conjecture 4.1 holds along the two families (for d = q; the conjecture asks for
all d).

**Corollary F.** In degree q, Kang's theorem plus length reduction (MMRV Prop. 4.3) can only reach ξ_q if
f_0(q) ≤ 6. In the families this means exactly q ∈ {12, 15, 28, 33}. For q = 44 and q = 51, and for all larger q in
the families, every representative of ξ_q modulo linear and standard tuples has length 7 or more in degree q. A proof
in degree q therefore needs genuinely new cycles, or lifts to multiples of q.

**Agreement with MMRV Table 1 (Computation).** MMRV list upper bounds for ℓ_{2,q}(ξ_q), obtained by an integer program
restricted to coefficients in {−1, 0, 1}. 31 of their entries lie in the families, and the formula equals each of them
(`results/exceptional_lengths.md`). Examples: 44 → 7, 51 → 10, 123 → 26 (c_3(41) = 5), 172 → 25 (c_2(43) = 3),
411 → 70. For q = 33 the tuple τ_33 = (1, 4, 16, 22, 25, 31) is MMRV's Table 2 representative.

**Exhaustive confirmation (Computation).** For q ∈ {12, 15, 28, 33, 44, 51}, all Hodge tuples of degree q shorter
than the formula were enumerated, and none has odd λ. For q = 44 there are exactly 20 sorted odd-λ Hodge tuples of
length 7.

## 5. Remarks and open questions

* **Where the λ-obstruction of Attack 17 comes from.** For q = 44, Proposition 3 reads 5λ_44 + U = 0, and the
  exhaustive check of Attack 17 (λ_44 = 0 on Hodge tuples of length ≤ 6) is the case q = 44 of part 1. Likewise
  16λ_51 + 2U = 0 for q = 51. The exact values ℓ_{2,44}(ξ_44) = 7 and ℓ_{2,51}(ξ_51) = 10, stated there as
  consequences of the computation, now follow from Theorem D. The degree 52 = 4·13 is *not* covered (13 ≡ 1 mod 4,
  so χ_4(13) = 1 and Proposition 3 degenerates). There ℓ_{2,52}(ξ_52) = 7 rests on computation alone: λ_52 vanishes
  on Hodge tuples of length ≤ 6, and MMRV give the upper bound 7.
* **Shape of the shortest tuples.** The units of τ_q form a "half system" mod p cut out by the cycles of
  multiplication by r. One cycle is broken at the order-p entry w, much as in Stickelberger-type constructions. Whether
  this has a geometric meaning (for example a subvariety of a Fermat variety whose class is τ_q) is open.
* **Lifts (open).** MMRV Table 3 shows that lifting can shorten ξ_q: 51 → 7 in degree 102, 69 → 9 in degree 138,
  87 → 10 in degree 174. For q = 4p it does not in their data: 44 → 7 in degree 132, 76 → 11 in degree 228,
  92 → 12 in degree 276. **Question:** is ℓ_2(ξ_{4p}) = ℓ_{2,4p}(ξ_{4p}) for p ≡ 3 (mod 4)? A positive answer for p = 11
  would show that no combination of linear, standard, surface and fourfold classes of any degree can reach (H44),
  which `docs/fermat/01-span-test.md` verifies only for degrees ≤ 1000. The Galois obstruction
  (`docs/fermat/03-galois-obstruction.md`, Theorem G) gives ℓ_{2,D}(ξ_44) ≥ 7 for every D = 44k with k ≤ 11, by a
  different argument. A representative of length ≤ 6 in degree D would put the lift of ξ_44 in Λ_D, and hence its
  Galois character in E_D.
* **Other degrees.** For q = 4p with p ≡ 1 (mod 4), q = 3p with p ≡ 1 (mod 3), and q = p_1 p_2 with both primes odd,
  the analogue of Proposition 3 degenerates and another invariant is needed. For q = 52 that invariant is
  λ_52 = Σ_{a ≡ ±1 (13)} χ_4(a) n_a. MMRV's Table 1 values for q = 4p with p ≡ 1 (mod 4) are (p + 1)/2 for
  p ≡ 5 (mod 8) and differ by ±1 for p ≡ 1 (mod 8) (for example 68 → 10, 89·4 = 356 → 44). Explaining them is a natural
  next step.

## 6. Reproduction

```bash
python3 -m pytest -q tests/test_exceptional_length.py tests/test_formal_module.py
python3 scripts/exceptional_lengths.py 420        # writes results/exceptional_lengths.md (about 15 s)
```

The code is `hodge/exceptional_length.py` and `hodge/formal_module.py`, pure Python with exact integers. It shares no
code with the python-flint and PARI scripts used for Attack 17 and the span test.
