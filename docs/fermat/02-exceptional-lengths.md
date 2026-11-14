# Exact lengths of the exceptional tuples ξ_q for q = 4p and q = 3p

**Status (2026-11-14).** This note proves a closed formula for the Aoki–Shioda length ℓ_{2,q}(ξ_q) of the exceptional
tuple ξ_q for every q = 4p with p an odd prime and every q = 3p with p a prime ≥ 5:

  ℓ_{2,q}(ξ_q) = (p − χ_m(p))/2 + c_r(p),   (m, r) = (4, 2) or (3, 3),

where χ_m is the odd quadratic character of conductor m (Theorem D for χ_m(p) = −1, Theorem D′ for χ_m(p) = +1).
The lower bound is a complete proof here. The upper bound is an explicit tuple. The identification of the minimum
with ℓ_{2,q}(ξ_q) uses the Kubert–Aoki index theorem, which this repository recomputes for every q ≤ 420 in the
families. The formula reproduces all 58 entries of Miranda–Movasati–Rufino–Villaflor's Table 1 of this form, so
those upper bounds are optimal.

**Addendum (2026-11-14, §6).** For q = p_1 p_2 with p_1, p_2 distinct odd primes, Theorem F proves the lower bound

  ℓ_{2,q}(ξ_q) ≥ φ(q)/4 + c_{p_1}(p_2) + c_{p_2}(p_1)

for every such q, by mod-2 functionals that count entries in cosets. Equality holds for all 47 such degrees in MMRV's
Table 1 (q ≤ 415, p_1 ≥ 5): for q ≤ 300 by our own explicit tuples, beyond by MMRV's. With p_1 = 3 the formula is
Theorem D′, and with 4 in place of p_1 it is Theorem D, so one formula covers every two-factor degree checked
(Conjecture F).

**What this is not.** It says nothing about whether ξ_q is algebraic, so it proves no new case of the Hodge conjecture.
It is a statement about one method: in degree q, the length-reduction method of MMRV (§4.3–4.4 of arXiv:2609.27301)
cannot settle ξ_q unless the formula gives at most 6. For q = 4p and 3p that happens only for
q ∈ {12, 15, 20, 21, 28, 33, 39}.
Lifts to multiples of q are not covered (§5).

Labels follow `CLAUDE.md`: **Theorem** = complete proof in this note; **Cited** = used as a black box, source read;
**Computation** = exact integer computation reproducible by the commands in §7.

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

**Corollary E (Theorem, given the cited index).** f_0(q) ≥ (q − m)/(2m) for all q = 4p and 3p (Theorems D, D′). So f_0 restricted to
these degrees has finite fibres: MMRV Conjecture 4.1 holds along the two families (for d = q; the conjecture asks for
all d).

**Corollary F.** In degree q, Kang's theorem plus length reduction (MMRV Prop. 4.3) can only reach ξ_q if
f_0(q) ≤ 6. With Theorem D′ this means exactly q ∈ {12, 15, 20, 21, 28, 33, 39} among q = 4p and 3p. For
q = 44, 51, 52, 57, 68 and all larger such q, every representative of ξ_q modulo linear and standard tuples has
length 7 or more in degree q. A proof in degree q therefore needs genuinely new cycles, or lifts to multiples of q
(as MMRV use for q = 57, via degree 114).

## 4′. The second case: χ_m(p) = +1

Let (m, r) be as before and let p be an odd prime, p ≠ 3, with χ_m(p) = +1, that is, p ≡ 1 (mod 4) for m = 4 and
p ≡ 1 (mod 3) for m = 3. Put q = m p; again q ∈ Q and ξ_q is defined. With g, h, P, Q, G as in §1, put

  λ′(v) = g(1) + g(−1)  (the signed count, with signs χ_m, of the unit entries congruent to ±1 mod p).

For q = 52 this is the invariant λ_52 = n_1 + n_25 − n_27 − n_51 of Attack 17.

**Proposition 3′ (Theorem).** For every v ∈ B_q: λ(v) = 0.

*Proof.* As in Proposition 3, the character χ_m gives (p − 1)λ(v)B_{1,χ_m} + U(v)B_{1,χ_m}(1 − χ_m(p)) = 0, and now
1 − χ_m(p) = 0. ∎

**Proposition 4′ (Theorem).** For every v ∈ B_q and every x ∈ (Z/p)^×: g(x) + g(−x) = 2U(v)/(p − 1) = λ′(v).

*Proof.* As in Proposition 4, ĝ(ψ) = 0 for every nontrivial even ψ mod p, so g^+ is constant, equal to its mean
U/(p − 1). ∎

Proposition 5 holds unchanged, since its proof does not use χ_m(p). The odd characters mod q are the same three
kinds as in §3, so v ∈ B_q if and only if Propositions 3′, 4′ and 5 hold for v.

**Theorem D′.** Let q = m p with χ_m(p) = +1.

1. **(Lower bound; Theorem.)** Every Hodge tuple α of degree q with λ′(α) odd has at least (p − 1)/2 entries that are
   units and, when o = ord_p(r) is even, at least (p − 1)/o entries of order p. Hence ℓ(α) ≥ (p − 1)/2 + c_r(p).
2. **(Attained; Theorem.)** The tuple τ_q of Theorem D(2) without the entry (m − 1)p is a Hodge tuple with
   λ′(τ_q) = 1 and ℓ(τ_q) = (p − 1)/2 + c_r(p).
3. **(Parity; Theorem.)** λ′ is even on D_q and on every standard tuple of degree q.
4. **(Exact value.)** If [B_q : D_q + S_q] ≤ 2 (Kubert–Aoki, Cited; Computation for every q ≤ 420), then
   D_q + S_q = {v ∈ B_q : λ′(v) even} and f_0(q) = ℓ_{2,q}(ξ_q) = (p − 1)/2 + c_r(p).

*Proof of 1.* For each of the (p − 1)/2 pairs {x, −x}, Proposition 4′ gives |g(x)| + |g(−x)| ≥ |λ′| ≥ 1, so each pair
carries a unit entry. Since h ≡ g (mod 2), h(x) − h(−x) ≡ g(x) + g(−x) = λ′ ≡ 1 (mod 2), so G^−(x) ∈ ½ + Z. The rest is
the proof of Theorem D(1): when o is even, every coset of ⟨r⟩ carries an entry of order p. ∎

*Proof of 2.* There is no entry of order m, so λ = 0 (Proposition 3′). Here g = h = 1_H with g(x) + g(−x) = 1 for all x,
and U = (p − 1)/2, so Proposition 4′ holds with λ′ = 1. Proposition 5 is checked exactly as in Theorem D(2). ∎

*Proof of 3.* The entries a and −a of a pair are both units or both not, and χ_m(−a) = −χ_m(a). So a pair adds χ_m(a)
to g(x) and −χ_m(a) to g(−x), and leaves g(x) + g(−x) unchanged. The entry ε is not a unit. Standard tuples:

* m = 4. s_{p,i} of degree 4p (k = 4), i odd: the entries i + 4j are all ≡ i (mod 4) and run once through the residues
  mod p. The one divisible by p is not a unit, and −pi is not a unit. So g(x) = χ_4(i) for every x ≠ 0, and
  λ′ = 2χ_4(i). If i is even, no entry is a unit. s_{2,i} of degree 4p (k = 2p), i odd: if p ∤ i, the units i and
  i + 2p are congruent mod p, with χ_4(i + 2p) = −χ_4(i) because 2p ≡ 2 (mod 4), so they cancel; if p | i, they are not
  units. The other entries are even. Lifts from degree 2p have even entries.
* m = 3. s_{3,i} of degree 3p (k = p), 3 ∤ i, p ∤ i: of i, i + p, i + 2p exactly one is divisible by 3. The other two
  are units, congruent mod p, with χ_3-values +1 and −1, so they cancel. The entry −3i is not a unit. s_{p,i} of
  degree 3p (k = 3), p ∤ i: if 3 ∤ i the entries i + 3j are ≡ i (mod 3), and as for m = 4, λ′ = 2χ_3(i). If 3 | i,
  no entry is a unit.

So λ′ ∈ {0, ±2} on standard tuples. ∎

*Proof of 4.* As for Theorem D(4), with λ′ in place of λ. ∎

**Corollary D″ (Theorem, given the cited index).** For every q = 4p (p an odd prime) and every q = 3p (p a prime ≥ 5),

  ℓ_{2,q}(ξ_q) = f_0(q) = (p − χ_m(p))/2 + c_r(p).

In particular ℓ_{2,52}(ξ_52) = 7, ℓ_{2,57}(ξ_57) = 10 and ℓ_{2,68}(ξ_68) = 10. Attack 17 obtained the value for 52
only by computation (its Corollary 4.3).

For q = 52 this also gives a conceptual proof of Attack 17, Theorem A(2): λ_52 = 0 on Hodge tuples of length ≤ 6.
If |λ′| ≥ 2, every pair needs two units, so there are at least p − 1 = 12 entries. If |λ′| = 1, part 1 gives at
least 7.

**Agreement with MMRV Table 1 (Computation).** MMRV list upper bounds for ℓ_{2,q}(ξ_q), obtained by an integer program
restricted to coefficients in {−1, 0, 1}. 58 of their entries have the form q = 4p or 3p: 31 with χ_m(p) = −1 and 27
with χ_m(p) = +1. The formula equals each of them (`results/exceptional_lengths.md`). Examples: 44 → 7, 51 → 10,
123 → 26 (c_3(41) = 5), 172 → 25 (c_2(43) = 3), 183 → 36 (c_3(61) = 6), 292 → 36 (ord_73(2) = 9 is odd), 411 → 70.
For q = 33 the tuple τ_33 = (1, 4, 16, 22, 25, 31) is MMRV's Table 2 representative.

**Exhaustive confirmation (Computation).** For q ∈ {12, 15, 20, 21, 28, 33, 39, 44, 51, 52}, all Hodge tuples of
degree q shorter than the formula were enumerated, and none has odd λ (resp. λ′). For q = 44 there are exactly 20 sorted odd-λ Hodge tuples of
length 7.

## 5. Remarks and open questions

* **Where the λ-obstruction of Attack 17 comes from.** For q = 44, Proposition 3 reads 5λ_44 + U = 0, and the
  exhaustive check of Attack 17 (λ_44 = 0 on Hodge tuples of length ≤ 6) is the case q = 44 of part 1. Likewise
  16λ_51 + 2U = 0 for q = 51. The exact values ℓ_{2,44}(ξ_44) = 7 and ℓ_{2,51}(ξ_51) = 10, stated there as
  consequences of the computation, now follow from Theorem D. The degree 52 = 4·13 falls under Theorem D′: there
  χ_4(13) = +1, Proposition 3 degenerates to λ = 0, and the invariant is λ′ = λ_52. So ℓ_{2,52}(ξ_52) = 7 is now a
  theorem too, given the index.
* **Shape of the shortest tuples.** The units of τ_q form a "half system" mod p cut out by the cycles of
  multiplication by r. One cycle is broken at the order-p entry w, much as in Stickelberger-type constructions. Whether
  this has a geometric meaning (for example a subvariety of a Fermat variety whose class is τ_q) is open.
* **Lifts (open).** MMRV Table 3 shows that lifting can shorten ξ_q: 51 → 7 in degree 102, 69 → 9 in degree 138,
  87 → 10 in degree 174. For q = 4p it does not in their data: 44 → 7 in degree 132, 76 → 11 in degree 228,
  92 → 12 in degree 276. **Question:** is ℓ_2(ξ_{4p}) = ℓ_{2,4p}(ξ_{4p}) for p ≡ 3 (mod 4)? A positive answer for p = 11
  would show that no combination of linear, standard, surface and fourfold classes of any degree can reach (H44),
  which `docs/fermat/01-span-test.md` verifies only for degrees ≤ 1000. The Galois obstruction
  (`docs/fermat/03-galois-obstruction.md`, Theorem G) gives ℓ_{2,D}(ξ_44) ≥ 7 for every D = 44k with k ≤ 13, by a
  different argument. A representative of length ≤ 6 in degree D would put the lift of ξ_44 in Λ_D, and hence its
  Galois character in E_D.
* **Other degrees.** The two-factor degrees not covered by Theorems D and D′ are q = p_1 p_2 with both primes ≥ 5:
  35, 55, 65, 77, 85, 91, 95, … §6 gives the formula and proves the lower bound in general (Theorem F).

## 6. Two odd primes: q = p_1 p_2

Let q = p_1 p_2 with p_1 < p_2 odd primes. Here p_1 ≥ 5 is the new case (35, 55, 65, 77, 85, 91, 95, …), and p_1 = 3
reproduces the lower bound of Theorem D′, as a check. The only element of Q dividing q is q, and
[B_q : D_q + S_q] = 2 (Kubert–Aoki, as in §1; recomputed for every q ≤ 300 by `index_B_over_DS`). Write
G = (Z/q)^×. For distinct primes r, p put c_r(p) = (p − 1)/ord_p(r) if ord_p(r) is even, and 0 otherwise.

**Coset functionals.** Let H = {t ∈ G : t² = 1} = {±1, ±e}, where e ≡ 1 (mod p_1) and e ≡ −1 (mod p_2). For
α = Σ n_a (a) ∈ R_q define:

* N_{tH}(α) = Σ_{a ∈ tH} n_a, one functional for each of the φ(q)/4 cosets of H;
* if ord_{p_2}(p_1) is even, N^{(1)}_C(α) = Σ_{y ∈ C} n_{p_1 y}, one for each of the c_{p_1}(p_2) cosets C of ⟨p_1⟩
  in (Z/p_2)^×. These count the entries of order p_2;
* symmetrically N^{(2)}_C, one for each of the c_{p_2}(p_1) cosets of ⟨p_2⟩ in (Z/p_1)^×, if ord_{p_1}(p_2) is
  even.

The supports are disjoint. Each is closed under a ↦ −a: −1 ∈ H, and −1 ∈ ⟨p_1⟩ modulo p_2 when the order is even,
because −1 is the only element of order 2 in a cyclic group.

**Proposition F1 (Theorem).** Every coset functional is even on D_q + S_q.

*Proof.* On a pair (a) + (−a) a functional takes the value 0 or 2, since its support is closed under negation. Since
q is odd, S_q is spanned by the standard tuples s_{p,i} of degree q with p ∈ {p_1, p_2} (MMRV Def. 3.7 needs
k = q/p ≥ 3; the proper divisors p_1, p_2 of q give k = 1). Consider

  s = s_{p_1,i} = (i, i + p_2, …, i + (p_1 − 1)p_2, −p_1 i),   with p_1 ∤ i and all entries nonzero.

Then i ≢ 0 (mod p_2), since otherwise some i + j p_2 ≡ 0. The first p_1 entries are all the x ≡ i (mod p_2), one
for each residue mod p_1.

* *Units.* These are the p_1 − 1 entries with x ≢ 0 (mod p_1). In coordinates (Z/p_1)^× × (Z/p_2)^×, a coset tH is
  {(±t_1, ±t_2)}. It contains no unit of s, or exactly the two units (±t_1, i). The count is even.
* *Multiples of p_1.* There are two: the entry p_1 y of the first block, with y ≡ p_1^{−1} i (mod p_2), and the last
  entry −p_1 i, with y ≡ −i. Their ratio −p_1^{−1} lies in ⟨p_1⟩ when ord_{p_2}(p_1) is even. Then both lie in the
  same coset, and the count is 0 or 2.
* *Multiples of p_2.* There are none.

The tuples s_{p_2,i} are symmetric. ∎

**The element ξ′_q.** Fix primitive roots μ_1 mod p_1 and μ_2 mod p_2, and the half systems
hs(p) = {μ^j : 0 ≤ j < (p − 1)/2}. Put

  ξ′_q = Σ_{x : x mod p_1 ∈ hs(p_1), x mod p_2 ∈ hs(p_2)} (x)
        + Σ_{y ∈ hs(p_2), w = p_1^{−1}y ∉ hs(p_2)} (p_1 w)  +  Σ_{y ∈ hs(p_1), w = p_2^{−1}y ∉ hs(p_1)} (p_2 w).

This is MMRV's Definition 4.8 of Aoki's ξ_q, computed for q = p_1 p_2. The primitive part is the product of the two
half systems. The p_1-part solves (p_1 − 1) ξ_{q,p_1} = τ_{p_1}(ξ_{q,1}) modulo D_{p_2}. In the extracted text of
Definition 4.8 the sign in τ is ambiguous. The sign used here is the one for which the result is Hodge (Proposition F3,
as MMRV Prop. 4.2 requires). It reproduces MMRV's representative (1, 2, 16, 17, 21, 22, 30, 31) of ξ_35.

**Proposition F2 (Theorem).** ξ′_q is odd on every coset functional.

*Proof.* *Units.* ξ′_q has exactly one unit in each coset tH, because a half system contains one element of each pair
{±x}.

*Multiples of p_1.* Let C be a coset of ⟨p_1⟩ in (Z/p_2)^×, of even order o. Write it as a cycle
w_k = p_1^{−k} w_0 (k mod o), so that w_{k+o/2} = −w_k. Put σ_k = +1 if w_k ∈ hs(p_2) and −1 otherwise, so
σ_{k+o/2} = −σ_k. The entries of ξ′_q in p_1·C are the p_1 w_{k+1} with σ_k = +1 and σ_{k+1} = −1, one for each
change of sign from + to −. Between k = 0 and k = o/2 the sign goes from σ_0 to −σ_0, so it changes an odd number of
times. By the antisymmetry, the full cycle has twice that many changes, and half of them go from + to −. So there is
an odd number of such changes.

*Multiples of p_2.* The same argument applies. ∎

**Proposition F3 (Theorem).** ξ′_q is a Hodge tuple.

*Proof.* Write B̄_1(x) = {x} − 1/2. A tuple α = Σ n_a (a) is Hodge if and only if F_α(t) = Σ_a n_a B̄_1(ta/q)
vanishes on G. Since B̄_1 is odd, so is F_α, so this holds if and only if Σ_t χ̄(t) F_α(t) = 0 for every odd character
χ of G. Write χ = χ_1 ⊗ χ_2 on (Z/p_1)^× × (Z/p_2)^×, and put B(χ̄_2) = Σ_{u ∈ (Z/p_2)^×} χ̄_2(u) B̄_1(u/p_2).

* A unit a contributes χ(a)·S(χ̄), where S(χ̄) = Σ_{t ∈ G} χ̄(t) B̄_1(t/q).
* An entry a = p_1 w has B̄_1(ta/q) = B̄_1(tw/p_2), which depends only on t mod p_2. Its contribution vanishes unless
  χ_1 = 1, and then it is (p_1 − 1) χ_2(w) B(χ̄_2). Entries p_2 w behave symmetrically.
* If χ_1 = 1, the distribution relation Σ_{j=0}^{p_1−1} B̄_1(x + j/p_1) = B̄_1(p_1 x) gives
  Σ_{t ∈ G, t ≡ u (p_2)} B̄_1(t/q) = B̄_1(u/p_2) − B̄_1(p_1^{−1}u/p_2). The second term is the one excluded t, the
  multiple of p_1. Hence S(χ̄) = (1 − χ̄_2(p_1)) B(χ̄_2).

Now let χ be odd.

(a) *χ_1 and χ_2 both nontrivial.* Exactly one of them is even, and a nontrivial even character sums to 0 over a half
system. So the primitive part contributes S(χ̄)·Σ_{hs(p_1)} χ_1 · Σ_{hs(p_2)} χ_2 = 0. The other parts contribute
nothing.

(b) *χ = 1 ⊗ χ_2 with χ_2 odd.* Let W = {p_1^{−1}y : y ∈ hs, p_1^{−1}y ∉ hs}, with hs = hs(p_2). The condition is

  (p_1 − 1) B(χ̄_2) · [ ½ (1 − χ̄_2(p_1)) Σ_{hs} χ_2 + Σ_{W} χ_2 ] = 0.

Here p_1^{−1}·hs is again a half system. With A = hs ∩ p_1^{−1}hs we get hs = A ⊔ (−W) and p_1^{−1}hs = A ⊔ W. For
odd χ_2 this gives Σ_{hs} χ_2 = Σ_A χ_2 − Σ_W χ_2 and χ̄_2(p_1) Σ_{hs} χ_2 = Σ_A χ_2 + Σ_W χ_2. Subtracting,
2 Σ_W χ_2 = (χ̄_2(p_1) − 1) Σ_{hs} χ_2, so the bracket vanishes.

(c) *χ = χ_1 ⊗ 1.* Symmetric to (b). ∎

**Theorem F.** Let q = p_1 p_2 with p_1, p_2 distinct odd primes. Then

  f_0(q) = ℓ_{2,q}(ξ_q) ≥ φ(q)/4 + c_{p_1}(p_2) + c_{p_2}(p_1).

The bound is attained for every such q ≤ 415 with p_1 ≥ 5 (47 degrees). In particular f_0 = 8, 10, 16, 16, 18, 22, 20
for q = 35, 55, 65, 77, 85, 91, 95.

*Proof.* By F2 and F3, ξ′_q lies in B_q and every coset functional is odd on it. By F1, ξ′_q ∉ D_q + S_q, so
ξ′_q ≡ ξ_q because the index is 2. Let α′ ≡ ξ′_q modulo D_q + S_q. Each functional N is odd on α′, so
Σ_{a ∈ supp N} |n_a| ≥ 1. The supports are disjoint, so ℓ(α′) is at least the number of functionals.

For attainment: for q ≤ 300, `hodge/two_prime.py` stores a Hodge tuple of exactly this length, found by a MILP and
verified exactly. Each such tuple is odd on every functional and lies outside D_q + S_q, by an exact lattice test. For
300 < q ≤ 415, MMRV's Table 1 lengths (Cited) equal the formula (`results/two_prime_lengths.md`). ∎

**Computation.** `results/two_prime_lengths.md` checks F1–F3 exactly for every q = p_1 p_2 ≤ 415, and
`tests/test_two_prime.py` checks F2–F3 for every q ≤ 1200, p_1 ≥ 3. The shortest tuples have exactly one entry in each
support and no other entries. That is the analogue of the "half systems" of §5.

**Conjecture F (unified formula; Numerical evidence).** Let q = q_1 q_2 ∈ Q have two P-factors (P = {4} ∪ {odd
primes}). For a factor a, let r_a be its prime (r_4 = 2), and let b be the other factor. Put
c(a → b) = φ(b)/ord_b(r_a) if ord_b(r_a) is even, and 0 otherwise. Then

  f_0(q) = φ(q)/4 + c(q_1 → q_2) + c(q_2 → q_1).

For {4, p} this is (p − χ_4(p))/2 + c_2(p), which is Theorems D and D′. For {3, p} it is (p − χ_3(p))/2 + c_3(p),
again Theorems D and D′. For two primes ≥ 5 it is Theorem F, proved up to q = 415. The lower bound holds for every
q = p_1 p_2. In general, what is missing is a Hodge tuple with exactly one entry in each support. The MILP finds one
in every case tried.

## 7. Reproduction

```bash
python3 -m pytest -q tests/test_exceptional_length.py tests/test_formal_module.py tests/test_two_prime.py
python3 scripts/exceptional_lengths.py 420        # writes results/exceptional_lengths.md (about 25 s)
python3 scripts/two_prime_lengths.py 415          # writes results/two_prime_lengths.md (§6; --search re-runs the MILP)
```

The code is `hodge/exceptional_length.py`, `hodge/two_prime.py` and `hodge/formal_module.py`, pure Python with exact
integers. It shares no code with the python-flint and PARI scripts used for Attack 17 and the span test. The MILP of
`scripts/two_prime_lengths.py --search` needs scipy; its output is stored and verified without it.
