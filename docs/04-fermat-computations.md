# 4. Computations on Fermat varieties: what was verified, how, and what it means

All code is in `hodge/` (pure Python, exact integer arithmetic, no dependencies); tests in `tests/`; raw output in `results/`. Nothing here is new mathematics: it is an independent, reproducible re-derivation of the classical machinery of Shioda, Katsura and Aoki, pushed through by computer, with every intermediate number checked against a published value or against a second independent computation.

## 4.1 Hodge classes of $X^n_m$ as characters

Let $X = X^n_m = \{x_0^m+\dots+x_{n+1}^m = 0\}\subset\mathbb{P}^{n+1}$ and let $G = \mu_m^{\,n+2}/\mu_m$ act by scaling coordinates. The primitive middle cohomology splits into one-dimensional eigenspaces

$$H^n_{\mathrm{prim}}(X,\mathbb{C}) = \bigoplus_{\alpha\in A^n_m} V(\alpha),\qquad A^n_m = \Big\{\alpha=(a_0,\dots,a_{n+1})\in(\mathbb{Z}/m)^{n+2}: a_i\neq0,\ \textstyle\sum a_i = 0\Big\}.$$

(Shioda–Katsura 1979, following Weil.) Writing each $a_i$ by its representative in $\{1,\dots,m-1\}$ and $|\alpha| = \tfrac1m\sum a_i\in\{1,\dots,n+1\}$, Griffiths' residue description gives $V(\alpha)\subset H^{n-q,q}(X)$ with $q = |\alpha|-1$ (the eigenvector is the residue of $x^{\alpha-\mathbf 1}\,\Omega/F^{\,q+1}$).

*Check 1 (`test_fermat_characters_reproduce_griffiths`).* Counting characters by $|\alpha|$ reproduces the primitive Hodge numbers computed independently from the Jacobian ring, $h^{n-q,q}_{\mathrm{prim}} = \dim R_{(q+1)m-(n+2)}$, for all $(n,m)$ tested; e.g. $(1,19,1)$ for the quartic surface, $(0,1,20,1,0)$ for the cubic fourfold, $(1,101,101,1)$ for the quintic threefold. Both totals equal $|A^n_m| = \big((m-1)^{n+2}+(-1)^{n}(m-1)\big)/m$.

The Galois group $(\mathbb{Z}/m)^\times$ acts on characters by $\alpha\mapsto t\alpha$, and the $\mathbb{Q}$-structure of $H^n(X,\mathbb{Q})$ mixes exactly the Galois conjugates: the smallest $\mathbb{Q}$-rational subspace containing $V(\alpha)$ is $W_\alpha = \big(\bigoplus_t V(t\alpha)\big)\cap H^n(X,\mathbb{Q})$. Hence for $n = 2p$:

$$\mathrm{Hdg}^p(X) = \mathbb{Q}h^p \oplus \bigoplus_{[\alpha]} W_\alpha,\qquad B^n_m = \{\alpha\in A^n_m : |t\alpha| = p+1\ \text{for all } t\in(\mathbb{Z}/m)^\times\},\qquad \dim\mathrm{Hdg}^p(X) = 1+|B^n_m|.$$

Elements of $B^n_m$ are the **Hodge characters**. The code enumerates $A^n_m$ and $B^n_m$ up to permutation (sorted tuples) and reweights by multiplicities.

*Check 2 (`test_picard_numbers_of_fermat_surfaces`).* For $n=2$, $\dim\mathrm{Hdg}^1 = \rho(S_m)$ is the Picard number (Lefschetz (1,1)); the computed values $\rho = 7, 20, 37, 86, 91, 176, 217, 362, 271, 644$ for $m = 3,\dots,12$ agree with Shioda's and Aoki–Shioda's published values where I know them ($m\le 8$) and with the closed formula $3(m-1)(m-2)+1$ whenever $\gcd(m,6)=1$. For $m=3,4,6$ the Galois group is $\{\pm1\}$ and $|{-\alpha}| = n+2-|\alpha|$, so *every* $(p,p)$-class is Hodge: the Fermat cubic fourfold has $\dim\mathrm{Hdg}^2 = 21 = h^{2,2}$.

## 4.2 The inductive structure and when it makes a Hodge class algebraic

**Theorem (Shioda–Katsura 1979, Shioda 1979).** Let $r,s\ge1$, $\varepsilon^m=-1$. The rational map

$$\varphi\colon X^r_m\times X^s_m\dashrightarrow X^{r+s}_m,\quad (x,y)\mapsto (x_0y_{s+1},\dots,x_ry_{s+1},\ \varepsilon x_{r+1}y_0,\dots,\varepsilon x_{r+1}y_s)$$

becomes a morphism after blowing up $X^{r-1}_m\times X^{s-1}_m = \{x_{r+1}=y_{s+1}=0\}$, is invariant under a $\mu_m$-action, and the induced correspondences give an isomorphism of Hodge structures

$$H^{r+s}_{\mathrm{prim}}(X^{r+s}_m) \;\cong\; \big[H^r_{\mathrm{prim}}(X^r_m)\otimes H^s_{\mathrm{prim}}(X^s_m)\big]^{\mu_m}\ \oplus\ H^{r-1}_{\mathrm{prim}}(X^{r-1}_m)\otimes H^{s-1}_{\mathrm{prim}}(X^{s-1}_m)(-1),$$

which carries algebraic classes to algebraic classes. On characters (read off from how $\varphi$ pulls back monomials: $z_i = x_iy_{s+1}$ for $i\le r$, $z_{r+1+j} = \varepsilon x_{r+1}y_j$ for $j\le s$):

* **(N)** $\beta = (b_0,\dots,b_r,\,c)\in A^r_m$ and $\gamma = (g_0,\dots,g_s,\,-c)\in A^s_m$ with $c\neq0$ give $\beta\#\gamma = (b_0,\dots,b_r,g_0,\dots,g_s)\in A^{r+s}_m$, and $V(\beta)\otimes V(\gamma)\mapsto V(\beta\#\gamma)$;
* **(Z)** $\beta'\in A^{r-1}_m$, $\gamma'\in A^{s-1}_m$ give the concatenation $(\beta',\gamma')\in A^{r+s}_m$ (this is the exceptional-divisor summand; $c=0$).

**Lemma 4.3 (decomposable $\Rightarrow$ algebraic).** Say $W_\alpha$ is *algebraic* if it is spanned by algebraic classes. If $\beta\in B^r_m$ and $\gamma\in B^s_m$ are Hodge characters with $W_\beta$, $W_\gamma$ algebraic and $\alpha = \beta\#\gamma$ (resp. $\alpha = (\beta',\gamma')$ with $W_{\beta'}, W_{\gamma'}$ algebraic), then $\alpha\in B^{r+s}_m$ and $W_\alpha$ is algebraic.

*Proof.* (This is Shioda's Theorem II [Shioda 1979], restated as in da Silva 2021, Thm 2.2 and Cor 2.3. The proof below was corrected on 2026-11-07 after two independent referees of the attack found that an earlier version wrongly claimed that the correspondence kills every component with $t\neq t'$.) First, $|t(\beta\#\gamma)| = |t\beta|+|t\gamma|-1 = (r/2+1)+(s/2+1)-1 = (r+s)/2+1$ for every unit $t$, so $\alpha$ is Hodge; in case (Z), $|t(\beta',\gamma')| = |t\beta'|+|t\gamma'|$ gives the same conclusion.

*Nonvanishing.* $W_\beta$ is a $\mathbb{Q}$-rational subspace spanned by algebraic classes, and $\mathrm{Gal}(\mathbb{Q}(\zeta_m)/\mathbb{Q})$ permutes its eigenlines $V(t\beta)$ transitively while fixing rational classes. A rational class in $W_\beta$ with a nonzero component on one line therefore has a nonzero component on every line. Choose algebraic classes $z_\beta\in W_\beta$ and $z_\gamma\in W_\gamma$ of this kind.

*Case (N).* The Shioda–Katsura map $X^r_m\times X^s_m \dashrightarrow X^{r+s}_m$ factors through the quotient by the diagonal $\mu_m$, which acts on the junction coordinates. The component $V(\beta_1)\otimes V(\gamma_1)$ of $z_\beta\times z_\gamma$ survives the quotient iff the junction entries cancel. For $\beta_1 = t\beta$ and $\gamma_1 = t'\gamma$ this means $(t-t')c\equiv 0 \pmod m$. When $\gcd(c,m)>1$ this allows $t\neq t'$: for example $m=51$, $c=17$, $t=1$, $t'=4$. A surviving cross term maps to $V(t\beta_S,\,t'\gamma_T)$. That is a Hodge character, but it never lies in the Galois orbit of $\alpha$. Indeed, $t\beta_S = t''\beta_S$ forces $t\beta = t''\beta$, since the junction entry is $-\sum\beta_S$, so pull-back along the map is injective on characters and each line $V(u\alpha)$ receives exactly one pair, namely $(u\beta, u\gamma)$. Hence no cancellation occurs on $W_\alpha$. The image of $z_\beta\times z_\gamma$ is an algebraic class whose component on each $V(u\alpha)$ is nonzero, with other components lying outside $W_\alpha$.

*Case (Z).* Here the classes come from $X^{r-1}_m\times X^{s-1}_m$ through the exceptional divisor $E$ of the blow-up: one uses $\tilde\varphi_*\, j_*\, \pi^*$, where $\pi: E\to X^{r-1}_m\times X^{s-1}_m$ is the projective bundle and $j: E\hookrightarrow$ the blow-up. The group $\mu_m$ acts trivially there, so every cross term $V(t\beta')\otimes V(t'\gamma')$ survives. These cross terms land in Hodge characters $(t\beta', t'\gamma')$ of other orbits, and the same injectivity argument shows that the component on each $V(u\alpha)$ comes from $(u\beta',u\gamma')$ alone.

*Projection.* The $\mathbb{Q}$-span of algebraic classes is stable under $G$ (automorphisms of $X^{r+s}_m$) and under the $\mathbb{Q}[G]$-idempotent projecting onto $W_\alpha$, which is an algebraic correspondence $\sum c_g\Gamma_g$. Applying it removes all cross terms and leaves a nonzero algebraic class in $W_\alpha$. A nonzero $G$-stable $\mathbb{Q}$-rational subspace of $W_\alpha$ contains a Galois-stable nonempty set of the lines $V(u\alpha)$, hence all of $W_\alpha$. $\square$

**Definition.** A Hodge character $\alpha\in B^n_m$ is **decomposable** (in the restricted sense implemented in `hodge.fermat.is_decomposable`) if $n\in\{0,2\}$, or if after a permutation of coordinates $\alpha = \beta\#\gamma$ or $\alpha=(\beta',\gamma')$ with both factors *Hodge characters of even-dimensional Fermat varieties* which are themselves decomposable.

Base cases: $X^0_m$ is $m$ points (every class algebraic); $X^2_m$ is a surface (Lefschetz (1,1)). By Lemma 4.3 and induction,

> **if every $\alpha\in B^n_m$ is decomposable, the Hodge conjecture holds for $X^n_m$.**

Two remarks on what is *not* used. (i) Decompositions through odd-dimensional factors (e.g. $H^1(C)\otimes H^{n-1}$) or through pairs of non-Hodge characters whose tensor product is Hodge are not allowed, because the Hodge conjecture for such "non-product" Hodge classes on $X^r\times X^s$ is not known in general. (ii) Aoki's explicit cycles (1983, 1987) and the closure criteria of the 2026 papers are not implemented; they make further characters algebraic. So "indecomposable" below means exactly: *not reachable by the inductive structure from points and surfaces*; it never means "not algebraic".

**Algorithm.** For $\alpha$ of length $k = n+2$, loop over subsets $S\ni 0$ with $2\le|S|\le k-2$; let $c = \sum_{i\in S}a_i$. If $c = 0$ and $|S|$ is even, test (Z) with $\beta' = \alpha_S$, $\gamma' = \alpha_{S^c}$ ($\gamma'$ is automatically Hodge when $\beta'$ is, since $|t\beta'|+|t\gamma'| = |t\alpha|$). If $c\neq0$ and $|S|$ is odd, test (N) with $\beta = (\alpha_S,-c)$, $\gamma = (\alpha_{S^c},c)$. Results are memoised on the canonical form of $\alpha$ under permutations and the Galois action, both of which preserve decomposability. For $n=4$ the test reduces to: *$\alpha$ has a zero-sum pair, or some 3-subset $S$ has $(\alpha_S,-c)$ Hodge*, which is why fourfolds up to $m=64$ take seconds.

## 4.3 Results

Full tables (Hodge numbers, $\dim\mathrm{Hdg}$, decomposable/indecomposable dimensions, orbit representatives, timings) are in [`results/README.md`](../results/README.md); raw JSON in `results/fermat_n*.json`; regenerate with `scripts/scan_fermat.py` and `scripts/make_tables.py`.

| $n$ | range of $m$ | degrees with indecomposable Hodge characters | all other degrees |
|---|---|---|---|
| 4 | $3\le m\le 64$ | 25, 32, 33, 35, 36, 39, 40, 42, 44, 45, 48, 50, 52, 54, 55, 56, 60, 62, 64 | **HC for $X^4_m$ verified** by the inductive structure alone |
| 6 | $3\le m\le 32$ | 25, 32 | **HC for $X^6_m$ verified** |
| 8 | $3\le m\le 20$ | none | **HC for $X^8_m$ verified** |

Representative indecomposable orbits (entries mod $m$):

* $n=4$, $m=25$: $(1,6,11,16,21,20) = (1,\,1{+}5,\,1{+}10,\,1{+}15,\,1{+}20,\,-5)$ — an arithmetic progression of length $p$ with difference $p$ plus $-p$. This is exactly the shape of the classes for which Aoki (1983, 1987) constructed new cycles on $X^n_{p^2}$. (For $p=7$ the analogous character has 8 entries, i.e. lives on the sixfold $X^6_{49}$, beyond the scanned range; for $p=3$ it lives on the surface $X^2_9$.)
* $n=4$, $m=33$: $(1,4,16,22,25,31)$ — da Silva (2021) reports that Shioda's condition $(P_{33})$ fails; $m=33$ is the first odd degree where our restricted criterion fails as well, while $m = 21, 27$ pass (da Silva verified $(P_{21}),(P_{27})$).
* $n=4$, $m=44$: $(1,12,23,26,34,36)$; $m=52$: $(1,14,27,30,40,44)$ — the degrees 44 and 52 are two of the three degrees ($44, 51, 52$) left open in all dimensions by Miranda–Movasati–Rufino–Villaflor (2026). Degree 51 passes our fourfold test; its difficulty must come from higher dimension.
* $n=6$, $m=25$: $(1,1,6,11,16,20,21,24)$ — contains the zero-sum pair $(1,24)$ and the fourfold character above: indecomposability is inherited from $n=4$ (the (Z) decomposition exists but one factor is indecomposable, and no other decomposition works).

Consistency with the literature, as a whole:

1. Every $m\le 20$ passes for $n = 4, 6, 8$ (Shioda 1979 verified $(P_m)$, $m\le20$, by hand).
2. Every prime $m$ passes in the scanned ranges (Shioda 1979, Ran 1980). Note that for prime $m$ this restricted criterion suffices, which is consistent with Shioda's proof.
3. $m=21, 27$ pass and $m = 33$ fails for $n = 4$ (da Silva 2021).
4. $m = 25 = 5^2$ fails for $n=4$ and $n=6$ with an Aoki-type character (Aoki 1987 proves HC for $m=p^2$ with extra cycles — the computation shows those extra cycles are genuinely needed).
5. The two open degrees $44, 52$ appear in the fourfold failure list; $51$ does not.

None of the failures is a counterexample: for $n=4$ all of them are covered by Kang's theorem (as cited by the 2026 authors) and by the computer-assisted census of arXiv:2608.18134 for odd degrees; they are simply the Hodge classes that need something beyond the 1979 inductive structure.

## 4.4 Fermat surfaces: lines versus the full Néron–Severi group

For $S_m = X^2_m\subset\mathbb{P}^3$ the $3m^2$ lines $\{x_i = \zeta x_j,\ x_k = \eta x_l\}$ ($\zeta^m=\eta^m=-1$) have an intersection matrix determined by congruences (`hodge.fermat_lines`): $L^2 = 2-m$ by adjunction; two lines of the same splitting meet iff they share $\zeta$ or $\eta$; two lines of different splittings meet iff one multiplicative relation among their parameters holds (derived by solving the four linear equations, which force all $x_i\neq0$ at a common point). The rank of the $3m^2\times3m^2$ Gram matrix is computed exactly over $\mathbb{Q}$ for $m\le8$ and modulo two primes for $m\le12$:

| $m$ | rank of line lattice | $\rho(S_m)$ | gap |
|---|---|---|---|
| 3 | 7 | 7 | 0 |
| 4 | 20 | 20 | 0 |
| 5 | 37 | 37 | 0 |
| 6 | 62 | 86 | 24 |
| 7 | 91 | 91 | 0 |
| 8 | 128 | 176 | 48 |
| 9 | 169 | 217 | 48 |
| 10 | 218 | 362 | 144 |
| 11 | 271 | 271 | 0 |
| 12 | 332 | 644 | 312 |

The line rank equals Shioda's formula $3(m-1)(m-2)+1+[m\ \text{even}]$ in every case, and equals $\rho(S_m)$ exactly when $m\le4$ or $\gcd(m,6)=1$ (Shioda 1981; Schütt–Shioda–van Luijk 2010; over $\mathbb{Z}$: Degtyarev 2015). The gap is the part of $NS(S_m)\otimes\mathbb{Q}$ that Lefschetz (1,1) guarantees but lines do not reach; Aoki–Shioda (1983) wrote down explicit curves for it. In the character picture, lines span exactly the "standard" characters $(a,-a,b,-b)$, and the gap consists of the non-standard Hodge characters — the surface analogue of the fourfold phenomenon in 4.3.

## 4.5 Reproduction

```bash
python3 -m pytest -q tests                                   # ~2 s
python3 scripts/scan_fermat.py 4 3 64 results/fermat_n4.json  # ~5 min total
python3 scripts/scan_fermat.py 6 3 32 results/fermat_n6.json  # ~2 min
python3 scripts/scan_fermat.py 8 3 20 results/fermat_n8.json  # ~30 s
python3 scripts/fermat_surfaces.py 8 12                      # ~30 s
python3 scripts/make_tables.py
```

Timings are for one core of the sandbox. The enumeration of $B^n_m$ is $O\big(\binom{m+n}{n+2}\cdot\varphi(m)\big)$ in the worst case; the sixfold of degree 44 (the smallest open case in the literature) has $\binom{49}{8}\approx 4.5\cdot10^8$ sorted tuples and would need a compiled implementation or a smarter enumeration (restricting to characters with no zero-sum pair, as the 2026 papers do).

## 4.6 Limitations

* The verification is *relative*: it assumes the Shioda–Katsura theorem and Lefschetz (1,1). Both are classical and I checked the character bookkeeping against two independent computations (Hodge numbers; Picard numbers), but I have not re-proved the Shioda–Katsura isomorphism.
* "Decomposable" is the restricted notion of 4.2. Shioda's own condition $(P_m)$ and the 2026 closure criteria are stronger (they use more known cycles); where this repository reports an indecomposable character, those methods may still succeed, and in the scanned fourfold range they all do.
* No claim is made about $X^n_m$ outside the scanned ranges.

## 4.7 Beyond the inductive structure: the open degrees 44, 51, 52

The degrees where the classical method stops for good are treated in separate files.

* `docs/attacks/17-fermat-open-cases.md` reduces HC for all Fermat varieties of degree 44 (resp. 51, 52), in every
  dimension, to the algebraicity of one Hodge class. The reduction uses only Lefschetz (1,1) and the
  Shioda–Katsura structure. Its lattice statements are re-derived by independent code in `hodge/formal_module.py`.
* `docs/fermat/01-span-test.md` shows that the known cycles, combined in any Z-linear way in any degree up to 1000,
  never reach the open classes.
* `docs/fermat/02-exceptional-lengths.md` computes the exact Aoki–Shioda length of the exceptional tuple ξ_q for
  every q = 4p (p an odd prime) and q = 3p (p a prime ≥ 5). It equals 7 for q = 44 and 52, and 10 for q = 51.
* `docs/fermat/03-galois-obstruction.md` shows that no cycle defined over the field of the known cycles, or over any
  field generated by roots of unity and radicals of the primes dividing 2q, reaches the open classes. The field a
  new cycle must be defined over is identified, through Deligne's Γ-value theorem, as an explicit quadratic
  extension.
