# 14. Spaces of cycles: Chow varieties, Lawson homology, Friedlander–Mazur filtrations

*Attack 14, second run, 2026-11-07. Draft for refereeing. No proof of the Hodge conjecture is claimed.*

## 0. Summary

**Top target (a): not reached.** In Lawson homology, $\mathrm{HC}(X,2)$ for a smooth projective fourfold $X$ turns out to be **equivalent** to one homotopy-theoretic statement (Corollary 2.3):

> **H(X).** Every Hodge class in $H_4(X,\mathbb{Q})$ is a $\mathbb{Q}$-linear combination of cycle classes $\Phi[g]$ of continuous maps $g\colon S^2\to Z_1(X)$, i.e. of 2-sphere families of algebraic 1-cycles.

Statements about $Z_2(X)$ itself only reach $H_4$ through $\pi_0 Z_2(X)$, which is the group of algebraic 2-cycles. Knowing it *is* the problem. The complex suspension theorem carries the problem over to the cone without changing it (Proposition 2.2). H(X) is equivalent to the coniveau form of $\mathrm{HC}(X,2)$, and I cannot prove it for any fourfold where $\mathrm{HC}(X,2)$ is open (GAP 1, §5).

**What is proved (rung (b)).**
* **Theorem A.** For every smooth projective $X$ and every $p\ge 1$,
 $$\mathrm{Hdg}_{2p}(X)\cap T_{p-1}H_{2p}(X,\mathbb{Q})\;=\;T_pH_{2p}(X,\mathbb{Q})\;=\;A_p(X).$$
 In words: a Hodge class in the image of $L_{p-1}H_{2p}(X)=\pi_2 Z_{p-1}(X)$ is algebraic. The last step of the $s$-tower never obstructs HC. Equivalently, the Friedlander–Mazur (FM) conjecture holds *on Hodge classes* in bidegree $(p-1,2p)$.
* **Theorem B** is an unconditional graded version. **Theorem B′** is a sharper graded version, conditional on a named correspondence hypothesis **FMC** that I attribute to [FM94] but could not check.
* **Corollary A.1.** The "Lawson level" of a Hodge class is never $p-1$. For 2-cycles (homological degree 4) a Hodge class has level $0$ or $2$.

All of this follows quickly from the Friedlander–Mazur inclusion $T_rH_k\subseteq G_rH_k$ and classical Hodge theory. I did not find these statements in the literature, but I expect experts know them. **I claim no mathematical novelty, only these precise formulations.**

**Obstruction mechanism (rung (c)), §4.**
* Integral coefficients: Kollár's threefolds show that the integral analogue of Theorem A fails, and the proof breaks exactly at the rational Hodge-splitting step.
* Non-projective Kähler tori: two separate ingredients fail. The FM inclusion fails (Example 4.5). The divisor form of Lefschetz (1,1) fails (Example 4.4).
* The open test cases (RM classes on $K3\times K3$, Weil classes on sixfolds of discriminant $+1$) are restated as "Lawson level 0 or top".

**Honest status:** `no_proof_obstruction_identified`.

## 1. Setup, conventions, cited facts

$X$ is a complex projective variety with $n=\dim X$. Homology means singular homology of $X(\mathbb{C})$. For $X$ smooth projective, $H_k(X,\mathbb{Q})\cong H^{2n-k}(X,\mathbb{Q})(n)$ is a polarizable pure Hodge structure of weight $-k$. We write:
* $\mathrm{Hdg}_{2p}(X)\subset H_{2p}(X,\mathbb{Q})$ for the classes of type $(-p,-p)$, the Poincaré duals of $\mathrm{Hdg}^{n-p}(X)$;
* $A_p(X)\subset H_{2p}(X,\mathbb{Q})$ for the $\mathbb{Q}$-span of the classes $[V]$ of $p$-dimensional subvarieties.

$\mathrm{HC}_p(X)$ denotes the statement $A_p(X)=\mathrm{Hdg}_{2p}(X)$. This is $\mathrm{HC}(X,n-p)$ in the notation of `docs/01`.

**Cycle spaces.** Fix an embedding $X\subset\mathbb{P}^N$.
* $\mathcal{C}_{r,d}(X)$ is the Chow variety of effective $r$-cycles of degree $d$. It is a projective algebraic set.
* $\mathcal{C}_r(X)=\coprod_d\mathcal{C}_{r,d}(X)$ is an abelian topological monoid.
* $Z_r(X)$ is its naive group completion, with the quotient topology.
* Lawson homology is $L_rH_k(X):=\pi_{k-2r}(Z_r(X))$ for $k\ge 2r$.

**Cited facts.**
* **(L1)** [La89, Fr91] $Z_r(X)$ is a topological abelian group whose homotopy type does not depend on the embedding. Proper morphisms $f$ induce continuous homomorphisms $f_*$.
* **(L2)** [Dold–Thom; La89] $L_0H_k(X)=\pi_k Z_0(X)\cong H_k(X;\mathbb{Z})$.
* **(L3)** [Fr91] $L_rH_{2r}(X)=\pi_0Z_r(X)$ is the group of $r$-cycles modulo algebraic equivalence. Its cycle map (L4) is the classical cycle class map [FM94].
* **(L4)** [FM94] There is an $s$-operation $s\colon L_rH_k(X)\to L_{r-1}H_k(X)$. The cycle map is $\Phi_{r,k}:=\Phi_{0,k}\circ s^r\colon L_rH_k(X)\to H_k(X;\mathbb{Z})$, where $\Phi_{0,k}$ is the isomorphism of (L2). Hence $\Phi_{r,k}=\Phi_{r-1,k}\circ s$.
* **(L5)** [FM94], as quoted in [Te05] and in Friedlander's survey notes. For $X$ smooth projective, $T_rH_k(X,\mathbb{Q})\subseteq G_rH_k(X,\mathbb{Q})$, with the notation defined below. Cohomologically, [Te05] states this as $T^{l-p}H^l\subseteq N^pH^l$.
* **(L6)** [La89, complex suspension theorem] For $\Sigma X\subset\mathbb{P}^{N+1}$ the projective cone, the suspension $\Sigma\colon Z_r(X)\to Z_{r+1}(\Sigma X)$ is a homotopy equivalence.
* **(L7)** [FM94] $\Phi$ commutes with proper push-forward. This is used only in Remark 3.5.

**Filtrations** [FM94].
* $T_rH_k(X,\mathbb{Q}):=\Phi_{r,k}(L_rH_k(X))\otimes\mathbb{Q}$ (the *topological* filtration). Its integral version is $T_rH_k(X;\mathbb{Z}):=\mathrm{im}\,\Phi_{r,k}$.
* $G_rH_k(X,\mathbb{Q}):=\sum_Y \mathrm{im}\big(H_k(Y,\mathbb{Q})\to H_k(X,\mathbb{Q})\big)$, summed over closed $Y\subseteq X$ with $\dim Y\le k-r$ (the *geometric* filtration: homological coniveau).
* By (L4), (L2) and (L3), $H_k=T_0H_k\supseteq T_1H_k\supseteq\cdots$, and $T_pH_{2p}(X,\mathbb{Q})=A_p(X)$.

**Hodge-theoretic inputs.**
* **(H1)** For a morphism $f\colon Y\to X$ of smooth projective varieties, $f_*\colon H_k(Y,\mathbb{Q})\to H_k(X,\mathbb{Q})$ is a morphism of Hodge structures. More generally, an algebraic cycle $\Gamma$ of dimension $\dim Y+r$ on $Y\times X$ acts by $\Gamma_*\colon H_j(Y)\to H_{j+2r}(X)(-r)$, a morphism of Hodge structures sending algebraic classes to algebraic classes [Fulton, Ch. 16, 19].
* **(H2)** Polarizable pure $\mathbb{Q}$-Hodge structures form a semisimple category [De71]. Lemma 3.2 below is the form used.
* **(H3)** [De74, Prop. 8.2.5] Let $Y$ be proper and $\pi\colon\tilde Y\to Y$ surjective with $\tilde Y$ smooth proper. Then $W_{k-1}H^k(Y,\mathbb{Q})=\ker\pi^*$, and morphisms of mixed Hodge structures are strict for $W$.
* **(H4)** Lefschetz (1,1): on a smooth *projective* $W$, $\mathrm{Hdg}^1(W)$ is spanned by classes of divisors.

**Verification note.** The network policy blocked numdam.org, the author pages at usc.edu and the Tsinghua archive. The search budget of this run was used up before every statement could be checked. Facts (L3)–(L5) and (L7) are therefore taken from how [Te05], [Hu06], [CH19], [CH21] and Friedlander's lecture notes state them, and from my own knowledge of [FM94] and [Fr91]. I did not read them in the primary sources. If (L5) needed an extra hypothesis, Theorem A would inherit it.

## 2. The top target: $\mathrm{HC}(X,2)$ for fourfolds from cycle spaces

### 2.1 Which Lawson groups see $H_4$

$\Phi_{r,k}$ lands in $H_k$. So the only Lawson groups that map to $H_4(X)$ are:
* $L_0H_4=\pi_4Z_0(X)$;
* $L_1H_4=\pi_2Z_1(X)$;
* $L_2H_4=\pi_0Z_2(X)$.

By (L2), $\Phi_{0,4}$ is an isomorphism. It sees every class, Hodge or not.

By (L3), $\Phi(\pi_0Z_2(X))\otimes\mathbb{Q}=A_2(X)$. So a "computation of $\pi_0Z_2(X)$" that detects Hodge classes is just a determination of the algebraic 2-cycles, and no homotopy theory enters.

The groups $\pi_jZ_2(X)$ with $j>0$ map to $H_{4+j}(X)$, so they say nothing about $H_4$.

Hence a non-tautological Lawson-homological route to $\mathrm{HC}(X,2)$ has to pass through $\pi_2Z_1(X)$, via $s\colon\pi_0Z_2(X)\to\pi_2Z_1(X)$.

### 2.2 The complex suspension theorem is inert

**Proposition 2.2.** Let $X\subset\mathbb{P}^N$ be projective and let $\Sigma X\subset\mathbb{P}^{N+1}$ be its projective cone. $\Sigma X$ is the one-point compactification (at the vertex) of the total space of $\mathcal{O}_X(1)$, i.e. its Thom space. Let $\tau\colon H_k(X;\mathbb{Z})\xrightarrow{\cong}\tilde H_{k+2}(\Sigma X;\mathbb{Z})$ be the Thom isomorphism. Then:
1. $V\mapsto\Sigma V$ induces an isomorphism from $r$-cycles on $X$ modulo algebraic equivalence to $(r+1)$-cycles on $\Sigma X$ modulo algebraic equivalence.
2. $\tau[V]=[\Sigma V]$ for every irreducible $V\subseteq X$.
3. Hence $\tau$ maps the algebraic classes in $H_{2r}(X)$ onto the algebraic classes in $H_{2r+2}(\Sigma X)$. In particular $\alpha\in H_{2r}(X,\mathbb{Q})$ is algebraic if and only if $\tau\alpha$ is.

*Proof.*
1. This is the $\pi_0$-part of (L6), combined with (L3).
2. Let $V$ be irreducible of dimension $r$. Then $\Sigma V$ is irreducible of dimension $r+1$, and it is the Thom space of $\mathcal{O}_V(1)$. The Thom isomorphism $H_{2r}(V)=\mathbb{Z}[V]\to\tilde H_{2r+2}(\Sigma V)=\mathbb{Z}[\Sigma V]$ is an isomorphism of infinite cyclic groups that respects the complex orientations, so it sends $[V]$ to $[\Sigma V]$. Naturality of $\tau$ for $V\subseteq X$ then gives the statement in $X$.
3. Combine 1 and 2. $\square$

Iterated suspension therefore replaces $(X,r)$ by $(\Sigma^mX,r+m)$ and the algebraic classes by their Thom images. The problem is transported, not simplified. Any proof "via the suspension theorem and a computation of $\pi_0$" has to compute $\pi_0Z_{2+m}(\Sigma^mX)$. That is the same problem as computing $A_2(X)$.

### 2.3 Reduction to H(X), and the exact gap

**Corollary 2.3** (of Theorem A, §3). Let $X$ be smooth projective of any dimension $n$, and let $\alpha\in\mathrm{Hdg}_4(X)$. The following are equivalent:
* (i) $\alpha\in A_2(X)$;
* (ii) $\alpha\in T_1H_4(X,\mathbb{Q})=\Phi(\pi_2Z_1(X))\otimes\mathbb{Q}$;
* (iii) $\alpha\in G_1H_4(X,\mathbb{Q})$, i.e. $\alpha$ is supported on a closed subvariety of dimension $\le 3$.

If $n=4$, (iii) is also equivalent to (iv): the Poincaré dual of $\alpha$ restricts to $0$ in $H^4(U,\mathbb{Q})$ for some nonempty Zariski-open $U\subseteq X$. Consequently $\mathrm{HC}(X,2)$ is equivalent to H(X).

*Proof.*
* (i)$\Rightarrow$(ii): $A_2=T_2H_4\subseteq T_1H_4$.
* (ii)$\Rightarrow$(i): Theorem A with $p=2$.
* (ii)$\Rightarrow$(iii): this is (L5).
* (iii)$\Rightarrow$(i): this is the second half of the proof of Theorem A, which uses only (iii).
* (iii)$\Leftrightarrow$(iv) for $n=4$: use the exact sequence $H_4(Y)\cong H^4_Y(X)\to H^4(X)\to H^4(X\setminus Y)$ for a closed $Y$ of dimension $\le3$. $\square$

**The gap (GAP 1).** The top target is precisely the statement H(X) for all smooth projective fourfolds. I cannot prove it for any fourfold on which $\mathrm{HC}(X,2)$ is open, for four reasons.

1. *Families sweep only coniveau-one classes.* By (L5), every $g\colon S^2\to Z_1(X)$ has $\Phi[g]\in G_1H_4$: its class is supported on a threefold. Producing $g$ for a given Hodge class $\alpha$ is therefore at least as hard as finding a threefold $Y\subset X$ with $\alpha\in\mathrm{im}\,H_4(\tilde Y)$. That is the coniveau form (iv) of $\mathrm{HC}(X,2)$, which is open, for example for Hodge classes on sextic fourfolds at special points of moduli and for real-multiplication classes on $S\times S$.
2. *The structural theorems only decompose.* The structural theorems of Lawson homology include the suspension theorem (L6), homotopy invariance, localization [LF92], projective-bundle and blow-up formulas [HL11], and Friedlander–Lawson duality and moving [FL97, FL98]. To my knowledge each expresses the Lawson homology of a variety built from simpler ones (cones, bundles, blow-ups, complements) in terms of the pieces. On Hodge classes they reproduce classical reductions. For instance, a uniruled fourfold is dominated by a blow-up of $\mathbb{P}^1\times Y$, and the cylinder classes $\beta\times[\mathbb{P}^1]$ with $\beta\in H_2(Y)=\pi_2Z_0(Y)$ give the Conte–Murre argument. None of them creates elements of $\pi_2Z_1(X)$ on a fourfold that is not built from lower-dimensional pieces.
3. *The deep comparison results are out of range.* With finite coefficients, Suslin's conjecture asserts that $L_rH_k(X;\mathbb{Z}/m)\to H_k(X;\mathbb{Z}/m)$ is an isomorphism for $k\ge n+r$. It is reported to follow from the Beilinson–Lichtenbaum theorem and to imply FM [Hu06]. Its range $k\ge n+r$ never contains $k=2r$ when $r<n$. For H(X) we have $(r,k,n)=(1,4,4)$ and $4<n+r=5$.
4. *Neither FM conjecture helps on Hodge classes.* The FM conjecture in bidegree $(1,4)$, i.e. $T_1H_4=G_1H_4$, adds nothing on Hodge classes, because there it is already Theorem A. What would suffice is the *strong* FM conjecture $T_1H_4=\tilde F_1H_4$, where $\tilde F_1H_4$ is the largest sub-Hodge structure of level $\le2$. But it contains Grothendieck's generalized Hodge conjecture for $H^4$ in coniveau 1, which already implies $\mathrm{HC}(X,2)$ and is open.

## 3. What is proved

### 3.1 Three lemmas

**Lemma 3.1 (support lemma; standard).** Let $V\subseteq\mathbb{P}^N$ be a closed algebraic subset, possibly reducible and singular, and let $j\ge0$. Then there is a closed algebraic $W\subseteq V$ with $\dim W\le j$ such that $H_j(W;\mathbb{Z})\to H_j(V;\mathbb{Z})$ is surjective.

*Proof.* Induct on $e(V)$, the largest dimension of a component of $V$ of dimension $>j$. Set $e(V)=-\infty$, and take $W=V$, if there is no such component.

Assume $e(V)>j$.
* Let $V'$ be the union of the components of dimension $>j$ and $V''$ the union of the others. Put $F=V_{\rm sing}\cup V''$. It is closed and contains no component of $V'$.
* Pick a point $x_i\notin F$ on each component of $V'$, and a hypersurface $D\subset\mathbb{P}^N$ with $D\supseteq F$ and $x_i\notin D$ for all $i$.
* Then $U=V\setminus D$ is smooth and closed in the affine variety $\mathbb{P}^N\setminus D$. Its connected components $U_\lambda$ are smooth affine of dimension $c_\lambda>j$.
* Triangulate the pair $(V,V\cap D)$ (Łojasiewicz). Then $H_j(V,V\cap D;\mathbb{Z})\cong H^{BM}_j(U;\mathbb{Z})\cong\bigoplus_\lambda H^{2c_\lambda-j}(U_\lambda;\mathbb{Z})$, the second isomorphism being Poincaré duality.
* These groups vanish: $2c_\lambda-j>c_\lambda$, and a smooth affine variety of dimension $c$ has the homotopy type of a CW complex of dimension $\le c$ (Andreotti–Frankel; Milnor, *Morse theory*, §7).
* Hence $H_j(V\cap D)\to H_j(V)$ is onto.
* Each component of $V\cap D$ of dimension $>j$ is a proper closed subset of a component of $V'$, so $e(V\cap D)<e(V)$. Induction finishes the proof. $\square$

The step that uses projectivity is the existence of $D$ with affine complement. Example 4.5 shows that this step genuinely fails on non-algebraic compact Kähler manifolds.

**Lemma 3.2 (Hodge splitting).** Let $\phi\colon H\to H'$ be a morphism of polarizable pure $\mathbb{Q}$-Hodge structures of even weight $2w$. Write $\mathrm{Hdg}(\cdot)$ for the rational classes of type $(w,w)$. Then $\phi(H)\cap\mathrm{Hdg}(H')=\phi(\mathrm{Hdg}(H))$.

*Proof.* The inclusion "$\supseteq$" is clear. For the other:
* $K=\ker\phi$ is a sub-Hodge structure.
* For a polarization $Q$ of $H$, the Hodge–Riemann relations make $Q|_K$ nondegenerate. So $H=K\oplus K^{\perp}$ with $K^\perp$ a sub-Hodge structure.
* $\phi|_{K^\perp}\colon K^\perp\to\phi(H)$ is a bijective morphism of Hodge structures. Its complexification preserves types and is bijective, so it is bijective on each $(a,b)$-piece, and its inverse is a morphism.
* Hence $y\in\phi(H)\cap\mathrm{Hdg}(H')$ equals $\phi(c)$ with $c=(\phi|_{K^\perp})^{-1}(y)$, which is rational of type $(w,w)$. $\square$

Over $\mathbb{Z}$ the lemma is false; see Example 4.1.

**Lemma 3.3 (images from singular subvarieties).** Let $X$ be smooth projective and $Y\subseteq X$ closed with inclusion $i$. Let $\pi\colon\tilde Y\to Y$ be the disjoint union of resolutions of the components of $Y$, and $f=i\circ\pi$. Then $i_*H_k(Y,\mathbb{Q})=f_*H_k(\tilde Y,\mathbb{Q})$.

*Proof.* Only "$\subseteq$" needs proof.
* Under the perfect pairing $H^k(X,\mathbb{Q})\times H_k(X,\mathbb{Q})\to\mathbb{Q}$ we have $i_*H_k(Y)=(\ker i^*)^\perp$ and $f_*H_k(\tilde Y)=(\ker f^*)^\perp$, since $i_*$ and $f_*$ are the transposes of $i^*$ and $f^*$. So it suffices to show $\ker f^*\subseteq\ker i^*$.
* Let $f^*a=\pi^*(i^*a)=0$. Then $i^*a\in W_{k-1}H^k(Y)$ by (H3).
* On the other hand $i^*a$ lies in the image of the pure weight-$k$ structure $H^k(X)$ under a morphism of mixed Hodge structures. By strictness that image meets $W_{k-1}$ in $i^*(W_{k-1}H^k(X))=0$.
* Hence $i^*a=0$. $\square$

### 3.2 Theorem A

**Theorem A.** Let $X$ be smooth projective and $p\ge1$. Then
$$\mathrm{Hdg}_{2p}(X)\cap T_{p-1}H_{2p}(X,\mathbb{Q})\;=\;\mathrm{Hdg}_{2p}(X)\cap G_{p-1}H_{2p}(X,\mathbb{Q})\;=\;A_p(X)\;=\;T_pH_{2p}(X,\mathbb{Q}).$$

*Proof.*
* By (L3), (L4) and (L5), $A_p=T_pH_{2p}\subseteq T_{p-1}H_{2p}\subseteq G_{p-1}H_{2p}$. Also $A_p\subseteq\mathrm{Hdg}_{2p}$. So it suffices to show $\mathrm{Hdg}_{2p}\cap G_{p-1}H_{2p}\subseteq A_p$.
* Let $\alpha$ lie in the left side. By Lemma 3.3 there are finitely many (since $H_{2p}(X,\mathbb{Q})$ is finite-dimensional) smooth projective connected $\tilde Y_j$ of dimension $d_j\le p+1$ and morphisms $f_j\colon\tilde Y_j\to X$ with $\alpha\in\phi\big(\bigoplus_jH_{2p}(\tilde Y_j,\mathbb{Q})\big)$, where $\phi=\sum_jf_{j*}$.
* By (H1), $\phi$ is a morphism of polarizable Hodge structures of weight $-2p$. By Lemma 3.2, $\alpha=\sum_jf_{j*}\beta_j$ with $\beta_j\in\mathrm{Hdg}_{2p}(\tilde Y_j)$.
* Each term is algebraic:
  * If $d_j<p$, then $\beta_j=0$.
  * If $d_j=p$, then $\beta_j\in\mathbb{Q}[\tilde Y_j]$, and $f_{j*}[\tilde Y_j]$ is a multiple of $[f_j(\tilde Y_j)]$.
  * If $d_j=p+1$, then $\beta_j$ is Poincaré dual to a class in $\mathrm{Hdg}^1(\tilde Y_j)$. By (H4) it is a $\mathbb{Q}$-combination of prime divisors $D$, and $f_{j*}[D]=\deg(D/f_j(D))\,[f_j(D)]$ or $0$.
* Hence $\alpha\in A_p(X)$. $\square$

The only input from cycle-space theory beyond the definitions is the Friedlander–Mazur inclusion (L5). The rest is the classical proof that Hodge classes of coniveau one less than maximal are algebraic.

**Corollary A.1 (Lawson level).** For $\alpha\in\mathrm{Hdg}_{2p}(X)$ put $\lambda(\alpha)=\max\{j\le p:\alpha\in T_jH_{2p}(X,\mathbb{Q})\}$. This exists because $T_0H_{2p}=H_{2p}$. Then $\lambda(\alpha)\in\{0,\dots,p-2\}\cup\{p\}$, and $\lambda(\alpha)=p$ if and only if $\alpha$ is algebraic.
* For $p=1$, every Hodge class has $\lambda=1$; this recovers HC for 1-cycles.
* For $p=2$, $\lambda\in\{0,2\}$. $\square$

**Corollary A.2.** HC holds for all smooth projective varieties if and only if $\mathrm{Hdg}_{2p}(X)\subseteq\Phi(\pi_2Z_{p-1}(X))\otimes\mathbb{Q}$ for all smooth projective $X$ and all $p\ge1$. $\square$

**Corollary A.3 (FM on Hodge classes).** For all smooth projective $X$ and $p\ge1$, $\mathrm{Hdg}\cap T_{p-1}H_{2p}=\mathrm{Hdg}\cap G_{p-1}H_{2p}$. This is the first equality of Theorem A. $\square$

**Remark 3.4 (morphic form; not claimed).** Friedlander–Lawson duality $L^qH^k(X)\cong L_{n-q}H_{2n-k}(X)$ [FL97] lets one translate Theorem A, provided the duality is compatible with cycle maps and Poincaré duality. I recall that it is but have not checked it. The translation reads: a Hodge class in $H^{2q}(X,\mathbb{Q})$ lying in the image of $L^{q+1}H^{2q}(X)$ ($\pi_2$ of the space of codimension-$(q+1)$ algebraic cocycles) is algebraic.

### 3.3 Graded versions

**Theorem B.** Let $1\le m\le p$. Suppose HC holds for codimension-$m$ classes on every smooth projective variety of dimension $p+m$. Then $\mathrm{Hdg}_{2p}(X)\cap T_{p-m}H_{2p}(X,\mathbb{Q})=A_p(X)$ for every smooth projective $X$. For $m=1$ the hypothesis is (H4), and Theorem B is Theorem A.

*Proof.*
* The inclusion "$\supseteq$" holds because $A_p=T_pH_{2p}\subseteq T_{p-m}H_{2p}$.
* For "$\subseteq$", argue as in Theorem A, using (L5) in the form $T_{p-m}\subseteq G_{p-m}$. This gives $\alpha=\sum_jf_{j*}\beta_j$ with $\beta_j\in\mathrm{Hdg}_{2p}(\tilde Y_j)$ and $d_j\le p+m$.
* Put $W_j=\tilde Y_j\times\mathbb{P}^{p+m-d_j}$ and $\beta_j'=\beta_j\times[\mathrm{pt}]$. This is a codimension-$m$ Hodge class on the $(p+m)$-fold $W_j$, and $\beta_j=\mathrm{pr}_*\beta'_j$.
* By hypothesis $\beta_j'$ is algebraic. Hence $\beta_j$ and $\alpha$ are algebraic. $\square$

**Hypothesis FMC (correspondence form).** For $X$ smooth projective and $r,j\ge0$,
$$T_rH_{2r+j}(X,\mathbb{Q})\subseteq\sum_{(Y,\Gamma)}\Gamma_*H_j(Y,\mathbb{Q}),$$
where $Y$ runs over smooth projective varieties and $\Gamma$ over algebraic cycles on $Y\times X$ of dimension $\dim Y+r$, acting as in (H1).

*Status of FMC.* [FM94] identify $T_\bullet$ with a "correspondence filtration". It is built from Chow correspondences $f\colon Y\to\mathcal{C}_r(X)$ and their homomorphisms $H_*(Y)\to H_{*+2r}(X)$. These are extended to singular $Y$ and to integral coefficients in [FM94b]. I could not check the precise formulation. FMC follows from that theorem if it is stated with $Y$ smooth, or with $Y$ singular and homomorphisms that are morphisms of mixed Hodge structures (by the weight argument of Lemma 3.3). **FMC is treated as a hypothesis.**

**Theorem B′ (conditional on FMC).** Let $1\le m\le p$. Suppose HC holds for middle-dimensional classes on all smooth projective $2m$-folds. Then $\mathrm{Hdg}_{2p}(X)\cap T_{p-m}H_{2p}(X,\mathbb{Q})=A_p(X)$ for every smooth projective $X$.

*Proof.* Put $r=p-m$ and $j=2m$.
* By FMC, $\alpha=\sum_i\Gamma_{i*}\gamma_i$ with $\gamma_i\in H_{2m}(Y_i,\mathbb{Q})$.
* The map $\bigoplus_i\Gamma_{i*}\colon\bigoplus_iH_{2m}(Y_i)\to H_{2p}(X)(-r)$ is a morphism of polarizable Hodge structures of weight $-2m$. The Hodge classes of the target are those of $\mathrm{Hdg}_{2p}(X)$. By Lemma 3.2 we may take each $\gamma_i$ to be Hodge.
* *If $\dim Y_i>2m$:* Lemmas 3.1 and 3.3 (in the smooth projective $Y_i$) and Lemma 3.2 give $\gamma_i=\sum_lg_{l*}\delta_l$. Here $g_l\colon\tilde W_l\to Y_i$, $\tilde W_l$ is smooth projective of dimension $\le2m$, and $\delta_l$ is Hodge. Moreover $\Gamma_{i*}g_{l*}=(\Gamma_i\circ[\mathrm{graph}\,g_l])_*$ [Fulton, 16.1].
* *If $\dim\tilde W_l<2m$:* replace $\tilde W_l$ by $\tilde W_l\times\mathbb{P}^e$ with $e=2m-\dim\tilde W_l$, replace $\delta_l$ by $\delta_l\times[\mathrm{pt}]$, and compose the correspondence with the graph of the projection.
* This writes $\alpha=\sum_l\Lambda_{l*}\epsilon_l$, with $\epsilon_l$ middle-dimensional Hodge classes on smooth projective $2m$-folds and $\Lambda_l$ algebraic correspondences.
* By hypothesis each $\epsilon_l$ is algebraic. So $\alpha$ is algebraic by (H1). $\square$

The hypothesis of B′ follows from that of B. Indeed, if $\beta$ is a middle Hodge class on a $2m$-fold $W$, then $\beta\times[\mathbb{P}^{p-m}]$ is a codimension-$m$ Hodge class on $W\times\mathbb{P}^{p-m}$. Intersecting with $W\times\mathrm{pt}$ recovers $\beta$. So B′ is the stronger statement. Example: given FMC and HC for codimension-2 classes on fourfolds, every Hodge class in $T_1H_6(X)$ (classes swept out by 4-sphere families of curves) is algebraic, for every $X$.

**Remark 3.5 (HC implies FM; known in essence).** The argument goes in three steps.
* HC for $Y\times Y$ implies the Lefschetz standard conjecture B for $Y$ (Kleiman).
* [Te05, Cor. 5.1], as I read it, says that B for $Y$ gives $T^tH^k(Y;\mathbb{Q})=H^k(Y;\mathbb{Q})$ for $t\ge k$. In homological terms: $T_rH_k(\tilde Y)=H_k(\tilde Y)$ whenever $\dim\tilde Y\le k-r$.
* Lemma 3.3 and (L7) then give FM in bidegree $(r,k)$ for every $X$, provided B holds in dimensions $\le k-r$.

This is the implication "B $\Rightarrow$ FM" that [CH21] attribute to Friedlander. Cao–Hu prove the converse for threefolds [CH21]. So the FM conjecture is implied by HC on all classes, and it holds unconditionally on Hodge classes in bidegree $(p-1,2p)$ (Corollary A.3).

## 4. Rung (c): explicit examples and the mechanism

### 4.1 Integral coefficients

**Example 4.1 (Kollár: the integral analogue of Theorem A fails for $p=1$).** Let $X\subset\mathbb{P}^4$ be a very general hypersurface of degree $d$ with $q^3\mid d$ for a prime $q$ [Ko92], as stated in `docs/01`.
* By the Lefschetz theorem, $H_2(X;\mathbb{Z})=\mathbb{Z}\ell$, with $\ell$ mapping to the class of a line.
* $H^4(X,\mathbb{C})=H^{2,2}$, so $\ell$ is an integral Hodge class.
* Kollár: every curve on $X$ has degree divisible by $q$. Hence $T_1H_2(X;\mathbb{Z})=\mathrm{im}\,(\text{curves})\subseteq q\mathbb{Z}\ell$.
* By (L2), $\ell\in T_0H_2(X;\mathbb{Z})=H_2(X;\mathbb{Z})$.

So the integral form of Theorem A fails: an integral Hodge class in $T_{p-1}H_{2p}(X;\mathbb{Z})$ need not be an integral combination of cycle classes. Rationally all is well: $d\ell$ is the class of a plane section.

The failure sits exactly at Lemma 3.2. For a smooth hyperplane section $S\subset X$, $H_2(S;\mathbb{Z})\to H_2(X;\mathbb{Z})$ is onto, so $\ell=i_*\beta$ with $\beta$ integral. No such $\beta$ can be Hodge: it would be a divisor class on $S$, and then $\ell$ would be algebraic.

**Remark 4.2 (the same failure for 2-cycles on a fourfold; conditional).** Put $X'=X\times\mathbb{P}^1$ and consider the integral Hodge class $\ell\times[\mathbb{P}^1]\in H_4(X';\mathbb{Z})$.
* It is not algebraic. For a surface $\Sigma\subset X'$, write $[\Sigma]=a\otimes[\mathrm{pt}]+b\otimes[\mathbb{P}^1]$ in the integral Künneth decomposition. Intersecting with $X\times\{t\}$ for general $t$ gives $b=[\Sigma\cap(X\times t)]$, a curve class, or $b=0$ if $\Sigma$ lies in a fibre. So $b\in q\mathbb{Z}\ell$, whereas $\ell\times[\mathbb{P}^1]$ has $b=\ell$.
* It is plausibly in $T_1H_4$. The map $z\mapsto z\times\mathbb{P}^1$ is a continuous homomorphism $Z_0(X)\to Z_1(X')$. *If* $\Phi$ is compatible with this exterior product (I believe this is in [FM94] but did not verify it), then $\ell\times[\mathbb{P}^1]\in T_1H_4(X';\mathbb{Z})\setminus T_2H_4(X';\mathbb{Z})$.

Under that assumption, the integral Lawson tower for $\mathrm{HC}(X',2)$ has a genuine obstruction at its last step, and the obstruction disappears rationally.

### 4.2 Non-projective compact Kähler manifolds

Let $M$ be a compact complex manifold. Put $\mathcal{C}_0(M)=\coprod_dSP^d(M)$, the Barlet space of 0-cycles, and let $Z_0(M)$ be its group completion. Dold–Thom gives $\pi_kZ_0(M)\cong H_k(M;\mathbb{Z})$, so $T_0H_k(M)=H_k(M)$ still holds. $G_rH_k(M)$ is defined using analytic subsets.

**Lemma 4.3.** A simple, non-algebraic complex torus $T$ of dimension $\ge2$ contains no curve.

*Proof.*
* Let $C\subset T$ be an irreducible curve, with normalization $\nu\colon\tilde C\to C$, and pick $c_0\in\tilde C$.
* By the universal property of the Jacobian, $c\mapsto\nu(c)-\nu(c_0)$ factors through a homomorphism of complex tori $h\colon J(\tilde C)\to T$.
* $h(J(\tilde C))$ is a subtorus of positive dimension, so $h$ is onto by simplicity.
* A complex torus that is a quotient of an abelian variety is abelian (Poincaré reducibility [BL]). This contradicts non-algebraicity. $\square$

**Example 4.4 (the projective input (H4)).** Let $T$ be a complex 2-torus with $NS(T)=\mathbb{Z}\omega$ and $\omega^2<0$.
* *Existence.* In the Plücker description, the periods $\sigma=dz_1\wedge dz_2$ range over $\{\sigma\wedge\sigma=0,\ \sigma\wedge\bar\sigma>0\}$, and $NS=\sigma^\perp\cap H^2(T,\mathbb{Z})$. Take $\sigma$ very general in $v^\perp$ for a primitive $v$ with $v^2<0$. Such $\sigma$ exist because $v^\perp_{\mathbb{R}}$ has signature $(3,2)$ [BL].
* *$T$ contains no curve $C$.* Otherwise $[C]=a\omega$ with $a\neq0$, since $\int_C\kappa>0$ for a Kähler form $\kappa$; so $C^2<0$. But $C\ne C+t$ for general $t$, and $C\cdot(C+t)=C^2$, so $C^2\ge0$. Contradiction.
* *Conclusion.* $0\ne\mathrm{Hdg}_2(T)=\mathbb{Q}\,\mathrm{PD}(\omega)\subset T_0H_2(T)$, but no nonzero class is a combination of curve classes. So the Barlet analogue of Theorem A fails for $p=1$.
* *The failing step.* (L5) holds trivially here: $G_0H_2(T)=H_2(T)$, taking $Y=T$. The step that fails is (H4). The class $\omega$ is $c_1(L)$ for a line bundle $L$, but no nonzero power of $L$ (positive or negative) has a nonzero section.

**Example 4.5 (the projective input (L5)).** Let $T$ be a complex 3-torus with $NS(T)=0$ and with $H^1(T,\mathbb{Q})$ an irreducible Hodge structure; this holds for very general $T$ [BL].
* $T$ is simple and non-algebraic, so it has no curves (Lemma 4.3).
* It has no surfaces either: a surface would be an effective divisor with nonzero class in $NS(T)=0$.
* Hence $G_0H_2(T)=0$, while $T_0H_2(T)=H_2(T;\mathbb{Z})\cong\mathbb{Z}^{15}$.

So the Barlet analogue of (L5) fails, and so does Lemma 3.1 for $V=T$: there is no hypersurface with affine complement.

### 4.3 The mechanism

1. **Sweeping.** A class in $T_rH_k$ is swept out by a $(k-2r)$-sphere of $r$-cycles. By (L5), whose proof I take to rest on Lemma 3.1 applied to Chow varieties, it is supported in dimension $k-r$. Hence it has Hodge level $\le k-2r$ (geometric coniveau implies Hodge coniveau). In short, $T_rH_k\subseteq G_rH_k\subseteq\tilde F_rH_k$.
2. **Collapse on Hodge classes.** For Hodge classes, $\mathrm{Hdg}\cap G_{p-1}=A_p$ (Lefschetz (1,1) plus splitting). So Lawson homology sees a Hodge class only at levels $0,\dots,p-2$, or else as an algebraic class. In degree 4 a Hodge class is either algebraic or invisible to every Lawson group except $L_0H_4$.
3. **Where the false variants break.** Rational coefficients enter through splitting (Example 4.1). Projectivity enters through algebraic cycle spaces and Lemma 3.1 (Example 4.5) and through divisors (Example 4.4).
4. **The open test cases in Lawson language (no claims).**
   * *RM classes on $S\times S$, with $S$ a K3 surface with real multiplication* (P2 of `docs/03`): Lawson level $0$ or $2$.
   * *Hodge classes on sextic fourfolds at special points*: level $0$ or $2$.
   * *Weil classes on abelian fourfolds*: level $2$. This comes from Markman's theorem, which deforms sheaves; no Lawson mechanism is involved.
   * *Weil classes on Weil-type sixfolds of discriminant $+1$, and Hodge classes on the degree-44 Fermat sixfold* ($p=3$): level $\in\{0,1,3\}$. Level 2 is excluded by Corollary A.1. Given FMC and HC for codimension-2 classes on fourfolds, level 1 would force level 3 (Theorem B′).

## 5. GAPS

**GAP 1 (the top target).** I do not prove statement H(X) for any fourfold on which $\mathrm{HC}(X,2)$ is open.
* *What is needed:* for every smooth projective fourfold $X$ and every $\alpha\in\mathrm{Hdg}_4(X)$, a finite set of maps $g_i\colon S^2\to Z_1(X)$ and rationals $c_i$ with $\alpha=\sum c_i\Phi[g_i]$.
* *Why it is needed:* by §2.1 it is the only non-tautological Lawson-homological route, and by Corollary 2.3 it is equivalent to $\mathrm{HC}(X,2)$.
* *Why I cannot prove it:* every such $g$ sweeps a class supported on a threefold (L5). So H(X) is the coniveau-one form of $\mathrm{HC}(X,2)$ (Corollary 2.3(iv)). No tool of the theory creates such families on a fourfold not built from simpler pieces (§2.3, items 2–4).
* No conditional proof is offered either. The only hypotheses I know that would give H(X) are the strong FM conjecture in bidegree $(1,4)$ and the generalized Hodge conjecture for $H^4$ in coniveau 1. Each of them already implies $\mathrm{HC}(X,2)$ by itself.

**GAP 2 (Hypothesis FMC).** Theorem B′ is proved only conditionally on FMC (§3.3). FMC would also give a self-contained proof of (L5):
* by FMC, Lemma 3.1 in $Y$ and Lemma 3.3, a class in $T_rH_k$ is $\sum\Lambda_*\gamma$ with $\Lambda$ a cycle of dimension $\le(k-2r)+r$ on $\tilde W\times X$;
* such a class is supported on $\mathrm{pr}_X|\Lambda|$, of dimension $\le k-r$.

Remark 4.2 needs a further unverified compatibility: $\Phi$ commutes with $-\times[\mathbb{P}^1]$.

**GAP 3 (primary sources).** The following were taken from secondary statements or from memory, and not checked in the original papers:
* (L3)–(L5) and (L7) [FM94, Fr91];
* [Te05, Cor. 5.1];
* the results of [Hu06, CH19, CH21] (from their abstracts);
* the exact hypotheses of Kollár's theorem (as in `docs/01`).

Theorem A depends only on (L3), (L4), (L5) together with classical Hodge theory.

**GAP 4 (literature question).** See §7. I could not settle whether some conjecture of [FM94] was "disproved by Friedlander".

## 6. Checklist (`docs/03`, §3.4)

* **Rational coefficients.** These are used in exactly one place, Lemma 3.2 (splitting of polarizable Hodge structures). It enters Theorem A, Theorem B and Theorem B′. The integral analogue of Theorem A is false (Example 4.1, $p=1$), and the proof breaks exactly at Lemma 3.2. Remark 4.2 indicates the same for 2-cycles on fourfolds. (L2) and Proposition 2.2 hold integrally; they do not touch Hodge classes.
* **Projectivity.** It is used in three places:
  1. (L5), through Chow varieties being projective algebraic sets and Lemma 3.1, whose proof needs a hypersurface $D$ with affine complement;
  2. (H4), through Hodge classes in $H^2$ being divisor classes;
  3. Proposition 2.2 (cones, Chow varieties).

  The Kähler (Barlet) analogues fail. Example 4.5 shows (L5) failing on very general 3-tori. Example 4.4 shows the conclusion of Theorem A failing for $p=1$ on a 2-torus with $NS=\mathbb{Z}\omega$, $\omega^2<0$.
* **Does anything here "prove" a false variant?** No.
  * No case of HC, integral HC or Kähler HC is claimed.
  * The integral and Kähler analogues of the proved statements are false.
  * The proofs fail at the identified steps: Lemma 3.2 over $\mathbb{Z}$, and (H4) or (L5) without projectivity.
* **Items 1–4 of §3.4** (absoluteness, the Lefschetz standard conjecture B, the variational HC, the open special cases) are not delivered, since HC is not proved.
  * A proof of H(X) would deliver absoluteness for Hodge classes on fourfolds. Coniveau one is defined algebraically, and coniveau-one Hodge classes are algebraic.
  * Lawson homology contains no input that could do this. Its theorems compare the analytic topology of algebraically defined spaces of cycles with singular homology. They say nothing about which rational $(p,p)$-classes are geometric. This is obstruction C3 of `docs/03` seen from the cycle-space side.
* **Item 5 (a visible break with the false variants)** is identified above, but only for the partial results.

## 7. Status of the Friedlander–Mazur conjectures (literature check)

**The FM conjecture** $T_rH_k(X,\mathbb{Q})=G_rH_k(X,\mathbb{Q})$ for smooth projective $X$ [FM94] is open in general. Known cases:
* $k=2r$ (trivial);
* $k=2r+1$ [Hu06];
* $\dim X\le2$;
* threefolds except bidegree $(1,4)$ [Hu06];
* products of a curve and a surface, stability under surjective morphisms, uniruled threefolds, and unirational varieties in a range [CH19].

Known implications:
* for threefolds, FM in bidegree $(1,4)$ is equivalent to the standard conjectures [CH21]: FM implies them (Cao–Hu), and B implies FM (Friedlander, as cited there);
* Suslin's conjecture implies FM [Hu06];
* the edge case follows from B [Te05].

Corollary A.3 says FM holds unconditionally *on Hodge classes* in bidegree $(p-1,2p)$.

**The strong FM conjecture** $T_rH_k=\tilde F_rH_k$, where $\tilde F_rH_k$ is the largest sub-Hodge structure of level $\le k-2r$, is attributed to Friedlander–Walker (as reported in [Hu11]). For $k=2r$ it is HC. In general it is FM together with Grothendieck's generalized Hodge conjecture. §4.3(1) records the easy inclusions $T\subseteq G\subseteq\tilde F$. The second one is "geometric coniveau implies Hodge coniveau": a class supported on $Y$ with $\dim Y=k-r$ comes from $H_k(\tilde Y)$, whose Hodge types $(a,b)$ satisfy $a,b\ge-(k-r)$.

**"Disproved?"** I found no disproof of the complex FM conjecture. What has been disproved is Teh's analogue for real varieties, which relates the niveau filtration to images of reduced real Lawson homology. This is in *Remarks on filtrations of the homology of real varieties*, Doc. Math. 17 (2012) 641–661, arXiv:1110.1836, by J. Heller and M. Voineagu to my recollection; I did not confirm the authorship. The same authors prove a vanishing analogue of FM for real varieties (Amer. J. Math., "Vanishing theorems for real algebraic cycles").

A version of a Hodge-theoretic conjecture phrased with the Hodge filtration $F$ instead of maximal sub-Hodge structures would be refuted for Grothendieck's "trivial reasons" (1969). I could not check whether such a version appears in [FM94] and was later corrected. This is left open (GAP 4).

Recent work, not affecting the above:
* Chen–Hu compute the rational Lawson homology of Chow varieties of $\mathbb{P}^n$ in a range (arXiv:2603.16252, 2026).
* Tian relates spaces of 1-cycles to coniveau filtrations (arXiv:2211.15911).

## 8. References

* [La89] H. B. Lawson, *Algebraic cycles and homotopy theory*, Ann. of Math. 129 (1989), 253–291.
* [Fr91] E. M. Friedlander, *Algebraic cycles, Chow varieties, and Lawson homology*, Compositio Math. 77 (1991), 55–93.
* [LF92] P. Lima-Filho, *Lawson homology for quasiprojective varieties*, Compositio Math. 84 (1992), 1–23.
* [LF93] P. Lima-Filho, *On the generalized cycle map*, J. Differential Geom. 38 (1993), 105–129.
* [FM94] E. M. Friedlander, B. Mazur, *Filtrations on the homology of algebraic varieties*, Mem. AMS 110 (1994), no. 529.
* [FM94b] E. M. Friedlander, B. Mazur, *Correspondence homomorphisms for singular varieties*, Ann. Inst. Fourier 44 (1994), 703–727.
* [Fr95] E. M. Friedlander, *Filtrations on algebraic cycles and homology*, Ann. Sci. ÉNS (4) 28 (1995), 317–343.
* [FL92] E. M. Friedlander, H. B. Lawson, *A theory of algebraic cocycles*, Ann. of Math. 136 (1992), 361–428.
* [FL97] E. M. Friedlander, H. B. Lawson, *Duality relating spaces of algebraic cocycles and cycles*, Topology 36 (1997), 533–565.
* [FL98] E. M. Friedlander, H. B. Lawson, *Moving algebraic cycles of bounded degree*, Invent. Math. 132 (1998), 91–119.
* [FW05] E. M. Friedlander, M. E. Walker, *Semi-topological K-theory*, Handbook of K-theory, Springer 2005.
* [Te05] J.-H. Teh, *Grothendieck standard conjectures, morphic cohomology and Hodge index theorem*, arXiv:math/0512232.
* [Hu06] W. Hu, *Some relations between the topological and geometric filtration for smooth projective varieties*, arXiv:math/0603203.
* [HL11] W. Hu, L. Li, *Lawson homology, morphic cohomology and Chow motives*, Math. Nachr. 284 (2011); arXiv:0711.0383.
* [Hu11] W. Hu, *Lawson homology for abelian varieties*, arXiv:1110.3505.
* [CH19] J. Cao, W. Hu, *Topological and geometric filtration for products*, arXiv:1901.06633.
* [CH21] J. Cao, W. Hu, *The equivalence of Friedlander–Mazur and standard conjectures for threefolds*, arXiv:2111.02669 (Izv. Math.).
* [Ko92] J. Kollár, *Trento examples*, LNM 1515 (1992), 134–135.
* [De71], [De74] P. Deligne, *Théorie de Hodge II, III*, Publ. Math. IHÉS 40 (1971), 44 (1974).
* [AF59] A. Andreotti, T. Frankel, *The Lefschetz theorem on hyperplane sections*, Ann. of Math. 69 (1959), 713–717.
* [Fulton] W. Fulton, *Intersection Theory*, 2nd ed., Springer 1998.
* [BL] C. Birkenhake, H. Lange, *Complex Tori*, Birkhäuser 1999; *Complex Abelian Varieties*, 2nd ed., Springer 2004.
* [Vo02] C. Voisin, *A counterexample to the Hodge conjecture extended to Kähler varieties*, IMRN 2002, no. 20.

## 9. Claimed results

| Label | Statement (one line) | Status |
|---|---|---|
| Prop. 2.2 | The suspension theorem transports algebraic classes via the Thom isomorphism ($A_r(X)\cong A_{r+1}(\Sigma X)$, $\tau[V]=[\Sigma V]$) | proved here (elementary, from (L6), (L3)) |
| Cor. 2.3 | For $\alpha\in\mathrm{Hdg}_4(X)$: algebraic $\iff\alpha\in T_1H_4\iff\alpha\in G_1H_4$ ($\iff$ vanishes on a Zariski-open set if $\dim X=4$); hence $\mathrm{HC}(X,2)\iff$ H(X) | proved here from Theorem A (the coniveau part is classical) |
| Lemma 3.1 | $H_j$ of a projective algebraic set is the image of $H_j$ of a closed subset of dimension $\le j$ | known/standard; proof included |
| Lemma 3.2 | Rational Hodge classes in the image of a morphism of polarizable Hodge structures lift to Hodge classes | known (Deligne); proof included |
| Lemma 3.3 | Images of $H_k(Y)$ and of $H_k(\tilde Y)$ in $H_k(X)$ coincide (weights) | known (Deligne); proof included |
| Theorem A | $\mathrm{Hdg}_{2p}\cap T_{p-1}H_{2p}=\mathrm{Hdg}_{2p}\cap G_{p-1}H_{2p}=A_p=T_pH_{2p}$ | proved here from (L3)–(L5) [FM94, Fr91]; probably known to experts, not found stated |
| Cor. A.1 | The Lawson level of a Hodge class lies in $\{0,\dots,p-2\}\cup\{p\}$ | proved here (from Theorem A) |
| Cor. A.2 | HC $\iff\mathrm{Hdg}_{2p}(X)\subseteq\Phi(\pi_2Z_{p-1}(X))_{\mathbb{Q}}$ for all $X,p$ | proved here (from Theorem A) |
| Cor. A.3 | The FM conjecture holds on Hodge classes in bidegree $(p-1,2p)$ | proved here (restatement of Theorem A) |
| Theorem B | HC in codimension $m$ on $(p+m)$-folds $\Rightarrow\mathrm{Hdg}\cap T_{p-m}H_{2p}=A_p$ | proved here from (L5) |
| Theorem B′ | HC for middle classes on $2m$-folds $\Rightarrow\mathrm{Hdg}\cap T_{p-m}H_{2p}=A_p$ | proved here conditionally on Hypothesis FMC |
| Rem. 3.4 | Morphic-cohomology form of Theorem A | not claimed (duality compatibility unchecked) |
| Rem. 3.5 | HC $\Rightarrow$ B $\Rightarrow$ FM | known in essence (Kleiman; [Te05]; Friedlander as cited in [CH21]) |
| Ex. 4.1 | The integral analogue of Theorem A fails for $p=1$ (Kollár) | proved here from [Ko92] and (L2) |
| Rem. 4.2 | Integral failure for 2-cycles on $X\times\mathbb{P}^1$ | non-algebraicity proved; membership in $T_1H_4$ conditional on $\Phi$ commuting with $-\times[\mathbb{P}^1]$ |
| Lemma 4.3 | Simple non-algebraic tori contain no curves | known (standard); proof included |
| Ex. 4.4 | The Barlet analogue of Theorem A fails for $p=1$ on a 2-torus with $NS=\mathbb{Z}\omega$, $\omega^2<0$ | proved here (existence of the torus standard [BL]) |
| Ex. 4.5 | The Barlet analogue of (L5) fails on very general 3-tori | proved here (genericity facts standard [BL]) |
