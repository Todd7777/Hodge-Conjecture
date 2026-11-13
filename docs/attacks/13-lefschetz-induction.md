# Attack 13: induction on dimension via hyperplane sections, Lefschetz pencils and Nori connectivity

**Status (read this first).** The top target is **not** achieved. That target was a proof of $\mathrm{HC}(X,p)$ in the *middle degree* $2p=\dim X$ from the Hodge conjecture for hyperplane sections plus a condition on Gysin maps, with the condition verified for a *new* class of varieties. What this file proves completely, and where it stops:

1. **Below the middle degree the induction works (§2, §3.1).** *Theorem A:* let $2p\le\dim X-1$ and $\alpha\in\mathrm{Hdg}^p(X)$. If $\alpha$ restricts to an algebraic class on uncountably many smooth members of one pencil with smooth base locus, then $e\alpha\in A^p(X)+c_1(L)\cdot\mathrm{Hdg}^{p-1}(X)$ for some integer $e\ge1$. *Theorem B:* HC for all $2m$-folds is equivalent to HC for all $(2m+1)$-folds. HC for all varieties of dimension $\le2m+1$ is equivalent to HC for primitive middle-degree classes on varieties of even dimension $\le2m$. Both are **known in substance**. The reduction of HC to primitive middle-degree classes on even-dimensional varieties is stated as part of Griffiths' program in [KP11] and with Hilbert-scheme arguments in [dS21]. I give complete proofs because everything later depends on their exact form.
2. **Exactly why the induction does not reduce HC to fourfolds (§3.2).** From odd dimension $2m+1$ to even dimension $2m+2$ the induction breaks on primitive middle-degree Hodge classes.
   - They restrict to zero on every smooth member of $|L^k|$, and smooth ample divisors produce only the decomposable classes $\mathrm{NS}\cdot\mathrm{Hdg}^{p-1}$ under Gysin maps (Proposition 3.1).
   - Only the total space of a Lefschetz pencil detects them faithfully, through the classes that vanish on every fibre (Proposition 3.2).
   - The missing step, a cohomological form of Griffiths–Zucker "Jacobi inversion" for families of homologically trivial cycles on the members, is *equivalent* to the class being algebraic (Proposition 3.3). HC in dimension $2m+1$, a statement modulo homological equivalence, contributes nothing to it.

   Concretely, a reduction to fourfolds would have to prove that Weil classes on Weil-type abelian sixfolds of non-split discriminant ($\neq-1$ with $\mathrm{disc}=\det H$, the normalization of Markman and Brosnan) are algebraic. That case is open, and those classes lie entirely in the part the method cannot see (Proposition 3.4).
3. **The invariant measuring the failure, and an explicit computation (§4, §5).**
   - The cokernel on Hodge classes of the Gysin maps from smooth ample divisors is $\mathcal D(X)=\mathrm{Hdg}^p(X)/\mathrm{NS}(X)_{\mathbb Q}\cdot\mathrm{Hdg}^{p-1}(X)$ (Proposition 5.1).
   - A single divisor $D\in|L|$ with only isolated singularities lowers it by at most the total Milnor number $\mu(D)$ (Proposition 4.2; believed new in this form, but elementary).
   - For the Fermat cubic fourfold, $\mathcal D(X)\cong\mathbb Q^{20}$. Each of its 243 Segre-cubic hyperplane sections (10 nodes) lowers it by at least 5, and by exactly 5 given the classical $b_4(S_3)=6$. Four suitable sections lower it to 0 (Example 5.3, an exact computation done by computer).
   - Nori's connectivity theorem is used as a black box. It shows that on very general members of a sufficiently ample linear system, algebraic classes come from the ambient variety. Consequently the induction step is there an *equivalence* that cannot create cycles for "new" Hodge classes (Propositions 5.2, 5.4).

**Referee (2026-11-13):** minor revision; corrections applied. Report summary: docs/06-attack-report.md.

No step uses more than rational cohomology, an ample class and Hilbert schemes. Nothing here can prove the integral or the Kähler Hodge conjecture; §7 checks this.

*Network note.* arxiv.org and journal sites were blocked. Statements from the literature were checked by web search against secondary sources only, and each one is flagged where it is used.

## 0. Notation and conventions

Varieties are over $\mathbb C$. Cohomology is singular cohomology with $\mathbb Q$-coefficients unless stated otherwise. $X$ is smooth projective with $n=\dim X$.

- $\mathrm{Hdg}^p(X)=H^{2p}(X,\mathbb Q)\cap H^{p,p}$, and $A^p(X)\subseteq\mathrm{Hdg}^p(X)$ is the $\mathbb Q$-span of classes of codimension-$p$ subvarieties.
- $\mathrm{HC}(X,p)$ means $A^p(X)=\mathrm{Hdg}^p(X)$. $\mathrm{HC}(X)$ means $\mathrm{HC}(X,p)$ for all $p$. $\mathrm{HC}(k)$ means $\mathrm{HC}(X)$ for every $X$ of dimension $k$.
- For $L$ ample, $h=c_1(L)$. For $2p\le n$, the primitive classes are $P^{2p}_L(X)=\ker\big(h^{n-2p+1}\colon H^{2p}(X)\to H^{2n-2p+2}(X)\big)$, and $\mathrm{Hdg}^p_{\rm prim}=\mathrm{Hdg}^p\cap P^{2p}_L$.

**Pencils.** A pencil in $|L|$ is a 2-dimensional subspace $\langle s_0,s_1\rangle\subseteq H^0(X,L)$. Its members are $Y_t=\{t_1s_0-t_0s_1=0\}$ for $t=[t_0:t_1]\in\mathbb P^1$, and its base locus is $B=Y_0\cap Y_\infty$. The pencil is *admissible* if $B$ is smooth of pure codimension 2 and some member is smooth. In that case:

- $U=\{t:Y_t\text{ smooth}\}$ is a nonempty Zariski open subset of $\mathbb P^1$;
- every member is smooth along $B$, since a member singular at $b\in B$ would make $B$ singular at $b$;
- $\tilde X=\{(x,t):x\in Y_t\}\subseteq X\times\mathbb P^1$ is smooth and equals $\mathrm{Bl}_BX$, with projections $\sigma\colon\tilde X\to X$ and $f\colon\tilde X\to\mathbb P^1$;
- the fibre $F_t=f^{-1}(t)$ maps isomorphically to $Y_t$;
- the exceptional divisor is $E=B\times\mathbb P^1$ (because $N_{B/X}\cong L|_B^{\oplus2}$), with $f|_E=\mathrm{pr}_2$.

$j_t\colon Y_t\hookrightarrow X$ denotes the inclusion. A general pencil in a very ample $|L|$ is admissible (Bertini). A *Lefschetz pencil* is an admissible pencil whose singular members each have exactly one ordinary double point, not on $B$ [La81], [Vo03, Ch. 2].

## 1. Inputs, stated as used

**(L) Lefschetz hyperplane theorem** [Vo03, Ch. 1], [La81]. Let $Y\subset X$ be a smooth ample divisor with inclusion $j$.
- $j^*\colon H^k(X)\to H^k(Y)$ is an isomorphism for $k\le n-2$ and injective for $k=n-1$.
- Dually, $j_*\colon H^k(Y)\to H^{k+2}(X)$ is an isomorphism for $k\ge n$ and surjective for $k=n-1$.
- Both maps are morphisms of Hodge structures; $j_*$ has type $(1,1)$.

**(HL) Hard Lefschetz.** $h^{n-k}\colon H^k(X)\to H^{2n-k}(X)$ is an isomorphism for $k\le n$. Consequences:
- $h\colon H^k\to H^{k+2}$ is injective for $k\le n-1$;
- for $2p\le n$ there is a decomposition of Hodge structures $H^{2p}=P^{2p}_L\oplus h\,H^{2p-2}$;
- if $n=2p$, then $P^{2p}_L=\ker(h)$ and $\dim P^{2p}_L=b_{2p}-b_{2p-2}$.

**(Bl) Blow-up formula** [Vo02, §7.3.3]. Let $\tilde X=\mathrm{Bl}_BX$ with $B$ smooth of codimension 2, exceptional divisor $i_E\colon E\hookrightarrow\tilde X$ and projection $\pi\colon E\to B$. Then
$$H^k(\tilde X)=\sigma^*H^k(X)\oplus i_{E*}\pi^*H^{k-2}(B)$$
is a decomposition of Hodge structures. Moreover $\sigma_*\sigma^*=\mathrm{id}$ and $\sigma_*i_{E*}\pi^*=0$, because $\sigma i_E=\iota_B\pi$ and $\pi_*\pi^*=0$ for a $\mathbb P^1$-bundle.

**(SS) Semisimplicity.** Polarizable pure $\mathbb Q$-Hodge structures form a semisimple abelian category. Hence:
- if $\phi$ is a morphism of such structures and $x\in\mathrm{Im}\,\phi$ is a Hodge class, then $x=\phi(y)$ for some Hodge class $y$;
- the components of a Hodge class in a direct sum of sub-Hodge structures are Hodge classes.

**(Hilb) Hilbert schemes and Chern characters.**
- For a projective morphism $\mathcal Y\to S$, the relative Hilbert scheme is a countable disjoint union of $S$-schemes projective over $S$ [FGA].
- On a smooth quasi-projective $M$, every coherent sheaf $\mathcal G$ has a finite locally free resolution, hence a Chern character in $H^*(M,\mathbb Q)$.
- If $\mathrm{codim}\,\mathrm{Supp}\,\mathcal G\ge p$, then $\mathrm{ch}_p(\mathcal G)=\mathrm{cl}([\mathcal G]_p)$, the class of the codimension-$p$ cycle of $\mathcal G$ ([Fu, Ex. 15.3.6] together with Newton's identities; attack 01 uses the same input).

**(Top) Topology of degenerations** [Mi68], [La81, §§5–6], [Di92, Ch. 3]. Let $f\colon\tilde X\to\Delta$ be a proper holomorphic map from an $N$-dimensional complex manifold to a disc. Assume $f$ is submersive except at finitely many points $x_1,\dots,x_k$ of $f^{-1}(0)$, each an isolated critical point with Milnor number $\mu_i$.
- **(T1)** For $\Delta$ small, $f^{-1}(\Delta)$ deformation-retracts onto $f^{-1}(0)$.
- **(T2)** For $t\in\Delta^*$, $H^q(f^{-1}(\Delta),F_t)\cong\bigoplus_i\tilde H^{q-1}(\mathbb F_i)$, and the same holds in homology. Here $\mathbb F_i$ is the Milnor fibre at $x_i$, homotopy equivalent to a bouquet of $\mu_i$ spheres of dimension $N-1$. So these groups vanish for $q\ne N$ and have dimension $\mu=\sum_i\mu_i$ for $q=N$.
- **(T3)** For a Lefschetz pencil on an $N$-fold, the vanishing cycles $\delta_s\in H_{N-1}(Y_t)$ are conjugate up to sign under monodromy and span the vanishing homology [Vo03, Ch. 2–3]. So they are all nonzero as soon as $H^{N-1}(Y_t)_{\rm van}:=\ker j_{t*}\neq0$. In that case the exact sequence of the pair $(f^{-1}(\Delta_s),F_t)$ and (T2), with $\mu=1$ and the boundary of the thimble equal to $\delta_s$, show that $H_N(F_t)\to H_N(f^{-1}(\Delta_s))=H_N(Y_s)$ is surjective.

**(N) Nori's connectivity theorem** [No93]. I use the form stated in [Vo02N, Thm 1] and in arXiv:2209.13683, checked only against these secondary sources. Let $M$ be smooth projective and $A$ ample on $M$. There is $d_0$ such that for $L=A^{\otimes d}$, $d\ge d_0$, the following holds. Let $B\subseteq|L|$ be the open set of smooth members, $\mathcal Y\to B$ the universal hypersurface and $n=\dim Y_b$. (In (N) and in Proposition 5.2, $n$ is the dimension of the members, not of the ambient variety.) For every smooth quasi-projective $T$ with a smooth morphism $T\to B$, the restriction $H^k(M\times T)\to H^k(\mathcal Y_T)$ is an isomorphism for $k<2n$ and injective for $k=2n$. I call such $L$ **Nori-ample**. Nori's theorem covers complete intersections of any codimension; only hypersurfaces are used here.

## 2. Target (a) below the middle degree: lifting through a pencil

**Lemma 2.1 (structure of the algebraic locus).** Let $\pi\colon\mathcal Y\to S$ be a smooth projective morphism of relative dimension $m$ over a smooth connected quasi-projective $S$, and let $\lambda$ be a global section of $R^{2p}\pi_*\mathbb Q$. The set $S^{\rm alg}_\lambda=\{s:\lambda_s\in A^p(Y_s)\}$ is the union of a countable family of closed irreducible subsets $f_i(\tilde H_i)$. Each $f_i\colon\tilde H_i\to S$ is a proper morphism from a smooth irreducible quasi-projective variety $\tilde H_i$, and comes with:
- closed subschemes $\mathcal Z_{i,1},\dots,\mathcal Z_{i,m_i}\subseteq\mathcal Y_{\tilde H_i}:=\mathcal Y\times_S\tilde H_i$, flat over $\tilde H_i$, whose fibres have dimension $\le m-p$;
- rationals $a_{i,1},\dots,a_{i,m_i}$;

such that $\sum_ja_{i,j}\,\mathrm{cl}[\mathcal Z_{i,j,h}]_{p}=\lambda_{f_i(h)}$ for **every** $h\in\tilde H_i$. Here $[\ ]_p$ denotes the codimension-$p$ part of the fundamental cycle.

*Proof.* The data consist of:
- Hilbert polynomials $P_1,\dots,P_k$ of degree $m-p$ (for a fixed relatively ample class);
- a vector $a\in\mathbb Q^k$;
- an irreducible component $H'$ of $(\mathrm{Hilb}^{P_1}\times_S\cdots\times_S\mathrm{Hilb}^{P_k})_{\rm red}$.

There are countably many such data. Each $H'$ is projective over $S$. Let $\rho\colon\tilde H\to H'$ be a resolution and $f\colon\tilde H\to S$ the composite, which is proper.

The pulled-back universal subschemes $\mathcal Z_j\subseteq\mathcal Y_{\tilde H}$ are flat over $\tilde H$. The total space $\mathcal Y_{\tilde H}$ is smooth (smooth over smooth) and quasi-projective. Put $\gamma_j=\mathrm{ch}_p(\mathcal O_{\mathcal Z_j})\in H^{2p}(\mathcal Y_{\tilde H})$ by (Hilb).

For $h\in\tilde H$ let $i_h\colon Y_{f(h)}\hookrightarrow\mathcal Y_{\tilde H}$ be the fibre. Choose a regular system of parameters at $h$; its pull-back is a regular sequence on $\mathcal O_{\mathcal Y_{\tilde H}}$, and it remains regular on $\mathcal O_{\mathcal Z_j}$ by flatness. So the Koszul complex computes $Li_h^*\mathcal O_{\mathcal Z_j}=\mathcal O_{\mathcal Z_{j,h}}$, and therefore
$$i_h^*\gamma_j=\mathrm{ch}_p(\mathcal O_{\mathcal Z_{j,h}})=\mathrm{cl}[\mathcal Z_{j,h}]_p .$$

Now $h\mapsto i_h^*\gamma_j$ is the restriction of a global class to the fibres, hence a flat section of $f^{-1}R^{2p}\pi_*\mathbb Q$; so is $f^*\lambda$. Two flat sections on the connected $\tilde H$ agree everywhere or nowhere. Keep exactly those data for which $\sum_ja_ji_h^*\gamma_j=\lambda_{f(h)}$ for all $h$. Each $f(\tilde H)$ is closed (as $f$ is proper) and irreducible.

Conversely, let $\lambda_s=\sum_ja_j[W_j]$ with $W_j\subset Y_s$ integral of codimension $p$. Then $(W_1,\dots,W_k)$ is a point of the fibre product of Hilbert schemes over $s$. It lies on some $H'$ and lifts to some $h\in\tilde H$, and that datum is kept. $\square$

**Theorem A (lifting below the middle degree).** Let $X$ be smooth projective of dimension $n$, $L$ ample, $h=c_1(L)$, and $\{Y_t\}$ an admissible pencil in $|L|$ with base locus $B$. Let $p\ge1$ with $2p\le n-1$ and $\alpha\in\mathrm{Hdg}^p(X)$. Suppose $j_t^*\alpha\in A^p(Y_t)$ for uncountably many $t\in U$. Then:
1. $j_t^*\alpha\in A^p(Y_t)$ for every $t\in U$;
2. there are an integer $e\ge1$, a codimension-$p$ cycle $W$ on $X$ and $\gamma_X\in\mathrm{Hdg}^{p-1}(X)$ such that
$$e\,\alpha=\mathrm{cl}(W)+h\cdot\gamma_X ,$$
and the restriction $\gamma_X|_B$ lies in $A^{p-1}(B)$.

*Proof.* **Step 1: a family of cycles over a finite cover of the pencil.** Apply Lemma 2.1 to $\mathcal Y_U:=f^{-1}(U)\to U$ and the flat section $\lambda_t=j_t^*\alpha$. Then $U^{\rm alg}_\lambda=\bigcup_if_i(\tilde H_i)$ is a countable union of closed irreducible subsets of the curve $U$. Each is either finite or all of $U$. Since $U^{\rm alg}_\lambda$ is uncountable, some $f(\tilde H):=f_i(\tilde H_i)$ equals $U$; this gives item 1.

Choose an irreducible curve $C_0\subseteq\tilde H$ with $f(C_0)$ dense in $U$. If $\dim\tilde H=1$ take $C_0=\tilde H$. Otherwise take a general complete intersection of $\dim\tilde H-1$ hyperplane sections of a projective compactification. By Bertini it is irreducible, and it meets the general fibre of $f$ (of dimension $\dim\tilde H-1$) in finitely many points, so it is not contained in a fibre.

Let $C'$ be the smooth projective model of $C_0$ and $\phi\colon C'\to\mathbb P^1$ the extension of $f|_{C_0}$; it is finite, of degree $e\ge1$. Choose a nonempty Zariski open $V\subseteq U$ such that:
- $V'=\phi^{-1}(V)$ maps into the locus of $C'$ where $C'\dashrightarrow\tilde H$ is defined;
- $\phi|_{V'}\colon V'\to V$ is finite étale.

Pull back the subschemes $\mathcal Z_j$ along $V'\to\tilde H$. The result is a family of subschemes of $\mathcal Y_{V'}:=f^{-1}(V)\times_VV'$, flat over $V'$, with fibre classes $\sum_ja_j\mathrm{cl}[\mathcal Z_{j,v'}]_p=j_{\phi(v')}^*\alpha$. The total space $\mathcal Y_{V'}$ is smooth, and the class $\Gamma=\sum_ja_j\mathrm{ch}_p(\mathcal O_{\mathcal Z_j})=\mathrm{cl}(\mathcal Z)$, where $\mathcal Z:=\sum_ja_j[\mathcal Z_j]_p$, restricts to $j^*_{\phi(v')}\alpha$ on the fibre over each $v'$, exactly as in the proof of Lemma 2.1.

**Step 2: sweeping.** The projection $g\colon\mathcal Y_{V'}\to f^{-1}(V)\subseteq\tilde X$ is finite étale of degree $e$. Let $\tilde W$ be the closure in $\tilde X$ of the cycle $g_*\mathcal Z$, component by component and with the same multiplicities; it is a codimension-$p$ cycle on $\tilde X$.

Fix $t_0\in V$ and $F=F_{t_0}\cong Y_{t_0}$. Three facts:
- restriction of cycle classes to the open set $f^{-1}(V)$ is compatible with cycle classes;
- $\mathrm{cl}\circ g_*=g_*\circ\mathrm{cl}$ for the finite map $g$;
- for the finite étale $g$, base change gives $i_F^*g_*=\sum_{v'\in\phi^{-1}(t_0)}i_{F_{v'}}^*$.

Together they give
$$i_F^*\,\mathrm{cl}(\tilde W)=\sum_{v'\mapsto t_0}j_{t_0}^*\alpha=e\,j^*_{t_0}\alpha .\tag{2.1}$$

**Step 3: the blow-up formula.** By (Bl) write $\mathrm{cl}(\tilde W)=\sigma^*\beta+i_{E*}\pi^*\gamma$ with $\beta\in H^{2p}(X)$ and $\gamma\in H^{2p-2}(B)$. By (SS) both are Hodge classes. Moreover $\beta=\sigma_*\mathrm{cl}(\tilde W)=\mathrm{cl}(\sigma_*\tilde W)$, so $\beta\in A^p(X)$.

Since $E=B\times\mathbb P^1$ with $f|_E=\mathrm{pr}_2$, the fibre $F$ meets $E$ transversally along $B\times\{t_0\}$. Transverse base change gives $i_F^*i_{E*}\pi^*\gamma=i_{B*}\gamma$, where $i_B\colon B\hookrightarrow Y_{t_0}$. With (2.1):
$$e\,j_{t_0}^*\alpha=j^*_{t_0}\beta+i_{B*}\gamma\qquad\text{in }H^{2p}(Y_{t_0}).\tag{2.2}$$

**Step 4: Lefschetz twice.** $B$ is a smooth ample divisor in $Y_{t_0}$, of dimension $n-2$.
- By (L) on $Y_{t_0}$ (dimension $n-1$), $i_B^*\colon H^{2p-2}(Y_{t_0})\to H^{2p-2}(B)$ is an isomorphism, because $2p-2\le n-3$. So $\gamma=i_B^*\gamma_Y$ for a Hodge class $\gamma_Y$.
- By (L) on $X$, $j_{t_0}^*\colon H^{2p-2}(X)\to H^{2p-2}(Y_{t_0})$ is an isomorphism. So $\gamma_Y=j_{t_0}^*\gamma_X$ with $\gamma_X\in\mathrm{Hdg}^{p-1}(X)$.

Hence $i_{B*}\gamma=i_{B*}i_B^*\gamma_Y=\gamma_Y\cdot h|_{Y_{t_0}}=j_{t_0}^*(h\gamma_X)$, and (2.2) becomes $j^*_{t_0}(e\alpha-\beta-h\gamma_X)=0$. Since $2p\le n-1$, $j^*_{t_0}$ is injective on $H^{2p}(X)$ by (L). Therefore $e\alpha=\beta+h\gamma_X$; take $W=\sigma_*\tilde W$.

Finally, $i_{E*}\pi^*\gamma=\mathrm{cl}(\tilde W)-\sigma^*\beta$ is algebraic. Because $i_E^*i_{E*}(x)=x\cdot c_1(\mathcal O_E(E))$ and $\pi_*c_1(\mathcal O_E(E))=-1$, we get $\gamma=-\pi_*i_E^*(\mathrm{cl}(\tilde W)-\sigma^*\beta)\in A^{p-1}(B)$. As $\gamma=\gamma_X|_B$, this proves the last claim. $\square$

**Corollary A.1.** In the situation of Theorem A, $\alpha\in A^p(X)$ as soon as $h\cdot\mathrm{Hdg}^{p-1}(X)\subseteq A^p(X)$. This holds in each of the following cases:
- $p\le2$ (Lefschetz (1,1));
- $\mathrm{HC}(X,p-1)$ holds;
- $\mathrm{HC}(Y_t,p-1)$ holds for one $t\in U$, because $h\gamma=j_{t*}j_t^*\gamma$ and $j_t^*\gamma\in\mathrm{Hdg}^{p-1}(Y_t)$.

*Proof.* Immediate from $e\alpha=\mathrm{cl}(W)+h\gamma_X$. $\square$

**Remarks.**
1. *Status.* Theorem A is the standard "spreading plus Lefschetz" argument behind the reduction in [KP11, dS21]. Three details of the formulation are mine: uncountably many members of a *single* pencil suffice; Lefschetz-ness of the pencil is not needed; and the error term is explicit, $h\gamma_X$ with $\gamma_X|_B$ algebraic.
2. *Not a case of the variational Hodge conjecture.* Algebraicity is assumed at uncountably many points; the countability of Hilbert schemes then does all the work.
3. *Where $2p\le n-1$ enters.* It enters exactly twice: the injectivity of $j_{t_0}^*$ on $H^{2p}(X)$ at the end of Step 4, and $H^{2p-2}(B)=i_B^*H^{2p-2}(Y_{t_0})$. Both fail at $2p=n$, and §3.2 analyses what replaces them there.
4. *Where coefficients enter.* The integer $e$ is the degree of a multisection and cannot be avoided in general, since monodromy may permute the components of the cycles. The $a_j$ are rational as soon as $\mathrm{HC}(Y_t)$ is only known rationally.

## 3. Target (b): from dimension $n$ to dimension $n+1$

### 3.1 The even-to-odd step is a theorem

**Lemma 3.0.** $\mathrm{HC}(Z\times\mathbb P^k)\Rightarrow\mathrm{HC}(Z)$. Moreover, if $\mathrm{HC}(Z\times\mathbb P^{2r},m)$ holds for a $2k$-fold $Z$ with $m=k+r$, then $\mathrm{HC}(Z,k)$ holds.

*Proof.* For the first claim, if $\mathrm{pr}_1^*\alpha=\mathrm{cl}(w)$, restrict to $Z\times\{\mathrm{pt}\}$ (Gysin pull-back of cycles along a regular embedding is compatible with cycle classes). For the second, let $H$ be the hyperplane class of $\mathbb P^{2r}$ and $\alpha\in\mathrm{Hdg}^k(Z)$. Then $\beta=\mathrm{pr}_1^*\alpha\cdot\mathrm{pr}_2^*H^{r}\in\mathrm{Hdg}^{m}(Z\times\mathbb P^{2r})$, which is the middle degree. If $\beta$ is algebraic, then so is $\mathrm{pr}_{1*}(\beta\cdot\mathrm{pr}_2^*H^r)=\alpha$. $\square$

**Theorem B.** Let $m\ge0$.
1. $\mathrm{HC}(2m)\iff\mathrm{HC}(2m+1)$.
2. The following are equivalent:
   - (a) $\mathrm{HC}(k)$ for all $k\le 2m+1$;
   - (b) $\mathrm{HC}(Z,m)$ for every $2m$-fold $Z$ (middle degree only);
   - (c) for every $k\le m$, every $2k$-fold $Z$ and some very ample $L$ on $Z$: $\mathrm{Hdg}^k_{\rm prim}(Z)\subseteq A^k(Z)$.

*Proof.* **(1), $\Leftarrow$.** Lemma 3.0 with $Z\times\mathbb P^1$.

**(1), $\Rightarrow$.** By Lemma 3.0, $\mathrm{HC}(k)$ holds for all $k\le2m$. Let $X$ have dimension $2m+1$ and let $L$ be very ample, with a general (admissible) pencil.
- For $p\le m$ we have $2p\le n-1$. Every smooth $Y_t$ has dimension $2m$, so $\mathrm{HC}(Y_t)$ holds, and Theorem A with Corollary A.1 (via $\mathrm{HC}(Y_t,p-1)$) gives $\mathrm{HC}(X,p)$.
- For $p\ge m+1$, $q:=n-p\le m$ and $\mathrm{HC}(X,q)$ holds. Since $h^{n-2q}$ is an isomorphism of Hodge structures carrying $A^q$ into $A^{n-q}$ (HL), $\mathrm{HC}(X,p)$ follows.

**(2).** (a)$\Rightarrow$(b) is trivial. (b)$\Rightarrow$(c) by Lemma 3.0, second part, with $r=m-k$.

(c)$\Rightarrow$(a): let $\mathcal P(k)$ be the statement "$\mathrm{HC}(j)$ for all $j\le2k+1$". $\mathcal P(0)$ is trivial. Assume $\mathcal P(k-1)$ with $k\le m$, and let $Z$ be a $2k$-fold.
- For $q<k$: $2q\le 2k-1=\dim Z-1$, and hyperplane sections satisfy HC by $\mathcal P(k-1)$, so Theorem A with Corollary A.1 gives $\mathrm{HC}(Z,q)$.
- For $q=k$: by (HL), $\mathrm{Hdg}^k=\mathrm{Hdg}^k_{\rm prim}\oplus h\,\mathrm{Hdg}^{k-1}$ (components of Hodge classes are Hodge by (SS), and $h$ is injective on $H^{2k-2}$). The first summand is algebraic by (c), the second by $\mathrm{HC}(Z,k-1)$.
- For $q>k$: (HL) as in (1).

So $\mathrm{HC}(2k)$ holds; by (1), $\mathrm{HC}(2k+1)$ holds; and $\mathrm{HC}(j)$ for $j<2k$ follows by Lemma 3.0. Hence $\mathcal P(k)$, and $\mathcal P(m)$ is (a). $\square$

Status. This is known in substance [KP11, dS21]. I have not seen the dimension-by-dimension equivalence (1) stated explicitly, but it is implicit in their reductions. Two corollaries:
- HC for fourfolds would imply HC for fivefolds;
- since HC holds for surfaces, Theorem B(1) with $m=1$ recovers HC for threefolds.

### 3.2 Why the odd-to-even step fails, exactly

Let $\dim X=2p$, $L$ ample, $h=c_1(L)$, and $\alpha\in\mathrm{Hdg}^p_{\rm prim}(X)$ (primitive with respect to $L$).

**Proposition 3.1 (blindness of restriction and Gysin).**
1. For every smooth $Y\in|L^k|$ ($k\ge1$), $j_Y^*\alpha=0$. More generally, for a smooth ample divisor $Y$ of class $y$ and any $\beta\in H^{2p}(X)$: $j_Y^*\beta=0$ if and only if $y\cdot\beta=0$.
2. For every smooth ample divisor $Y$, $j_{Y*}H^{2p-2}(Y)=y\cdot H^{2p-2}(X)$ and $j_{Y*}\mathrm{Hdg}^{p-1}(Y)=y\cdot\mathrm{Hdg}^{p-1}(X)$. If $y=kh$, this image meets $P^{2p}_L(X)$ only in $0$.
3. The same holds for complete intersections $V=D_1\cap\dots\cap D_c$ of ample divisors with $\dim V<2p$ whose partial intersections $D_1\cap\dots\cap D_i$ are all smooth (for instance general members of very ample systems):
   - restriction to $V$ kills every $\beta$ with $D_1\cdots D_c\cdot\beta=0$, in particular $P^{2p}_L$ when all $D_i\in|L^{k_i}|$;
   - $j_{V*}H^{2p-2c}(V)=D_1\cdots D_c\cdot H^{2p-2c}(X)\subseteq\mathrm{NS}_{\mathbb Q}\cdot H^{2p-2}(X)$.

*Proof.* (1): by (L), $j_{Y*}$ is an isomorphism on $H^{2p}(Y)$ (degree $2p\ge n$), and $j_{Y*}j_Y^*\beta=y\beta$; if $y=kh$, then $h\alpha=0$.

(2): by (L), $H^{2p-2}(Y)=j_Y^*H^{2p-2}(X)$ (degree $2p-2\le n-2$), and the same holds for Hodge classes by (SS). Now apply the projection formula. For the last assertion use $H^{2p}=P^{2p}_L\oplus hH^{2p-2}$ (HL).

(3): induct on $c$, applying (L) to the smooth ample divisor $D_1\cap\dots\cap D_i$ of $D_1\cap\dots\cap D_{i-1}$ at each step. $H^{2p-2c}(V)=j_V^*H^{2p-2c}(X)$ because $2p-2c<\dim V=2p-c$. For the restriction statement: $H^{2p}(V)$ is Poincaré dual to $H^{2p-2c}(V)=j_V^*H^{2p-2c}(X)$, and $\int_Vj_V^*\beta\cdot j_V^*\eta=\int_X\beta\,\eta\,D_1\cdots D_c$. $\square$

So in the middle degree the two operations driving Theorem A, restricting to smooth members and pushing forward from them, carry **no information** about $\mathrm{Hdg}^p_{\rm prim}$. The information sits in the total space of a pencil.

**Proposition 3.2 (where the primitive classes live).** Let $\{Y_t\}$ be a Lefschetz pencil in $|L|$ with $H^{2p-1}(Y_t)_{\rm van}\neq0$. Let $U'\subseteq U$ be nonempty Zariski open, and write $\mathcal Y_{U'}=f^{-1}(U')$. Then the map
$$P^{2p}_L(X)\longrightarrow H^{2p}(\mathcal Y_{U'}),\qquad\alpha\mapsto\sigma^*\alpha|_{\mathcal Y_{U'}},$$
is injective, and its image lies in the subspace of classes vanishing on every fibre. That subspace is $H^1(U',R^{2p-1}f_*\mathbb Q)$, the Leray piece $L^1$; here $L^2=H^2(U',R^{2p-2}f_*\mathbb Q)=0$ because $U'$ is an affine curve.

*Proof.* Fibrewise vanishing is Proposition 3.1(1). For injectivity, suppose $\sigma^*\alpha|_{\mathcal Y_{U'}}=0$. By the exact sequence of the pair $(\tilde X,\mathcal Y_{U'})$ and duality, $H^{2p}_{f^{-1}(\mathbb P^1\setminus U')}(\tilde X)\cong\bigoplus_{s\notin U'}H_{2p}(Y_s)$, so $\sigma^*\alpha$ lies in the image of $\bigoplus_{s\notin U'}H_{2p}(Y_s)\to H_{2p}(\tilde X)\cong H^{2p}(\tilde X)$.
- For smooth $Y_s$, the image is $i_{F*}H^{2p-2}(F)$ for any smooth fibre $F$, since smooth fibres are isotopic in $\tilde X$.
- For singular $Y_s$, by (T3) and (T1), $H_{2p}(Y_s)$ is the image of $H_{2p}(F_t)$ for nearby $t$, so the image is again $i_{F*}H^{2p-2}(F)$.

Hence $\sigma^*\alpha\in i_{F*}H^{2p-2}(F)$. Applying $\sigma_*$, and using $\sigma i_F=j_t$ and $H^{2p-2}(Y_t)=j_t^*H^{2p-2}(X)$:
$$\alpha=\sigma_*\sigma^*\alpha\in j_{t*}j_t^*H^{2p-2}(X)=hH^{2p-2}(X).$$
Since $hH^{2p-2}\cap P^{2p}_L=0$ (HL), $\alpha=0$.

The Leray statement holds because $E_2^{a,b}=0$ for $a\ge2$ on an affine curve, so the spectral sequence degenerates and $L^1=E_2^{1,2p-1}$. $\square$

**Proposition 3.3 (the missing step is equivalent to the conclusion).** In the setting of Proposition 3.2, consider the following condition (JI) for $\alpha\in\mathrm{Hdg}^p_{\rm prim}(X)$:

> **(JI)** There are a nonempty Zariski open $V\subseteq U$, a finite étale cover $\phi\colon V'\to V$ of degree $e$, a $\mathbb Q$-cycle $\mathcal Z$ of codimension $p$ on $\mathcal Y_{V'}=f^{-1}(V)\times_VV'$ whose class vanishes on every fibre, and $c\in\mathbb Q^\times$ with $\mathrm{cl}(\mathcal Z)=c\cdot g^*\sigma^*\alpha$ in $H^{2p}(\mathcal Y_{V'})$, where $g\colon\mathcal Y_{V'}\to f^{-1}(V)$ is the projection.

Then $\alpha\in A^p(X)\Rightarrow$(JI)$\Rightarrow\alpha\in A^p(X)+h\cdot\mathrm{Hdg}^{p-1}(X)$. So if $h\,\mathrm{Hdg}^{p-1}\subseteq A^p$ (for instance under $\mathrm{HC}(2p-1)$), (JI) is equivalent to $\alpha\in A^p(X)$.

*Proof.* If $\alpha=\mathrm{cl}(Z)$, take $V'=V=U$ and $\mathcal Z=(\sigma^*Z)|_{f^{-1}(U)}$, where $\sigma^*$ is the Gysin pull-back on Chow groups for the morphism $\sigma$ of smooth varieties. Its fibre classes are $j_t^*\alpha=0$.

Conversely, let $\tilde W$ be the closure of $g_*\mathcal Z$ in $\tilde X$. Since $g$ is finite étale of degree $e$, $\mathrm{cl}(\tilde W)|_{f^{-1}(V)}=g_*\mathrm{cl}(\mathcal Z)=c\,g_*g^*\sigma^*\alpha=ce\,\sigma^*\alpha|_{f^{-1}(V)}$. So $\xi:=\mathrm{cl}(\tilde W)-ce\,\sigma^*\alpha$ vanishes on $f^{-1}(V)$. As in the proof of Proposition 3.2, $\xi\in i_{F*}H^{2p-2}(F)$, and hence
$$\mathrm{cl}(\sigma_*\tilde W)-ce\,\alpha=\sigma_*\xi\in hH^{2p-2}(X).$$
The left side is a Hodge class, so it equals $h\gamma$ with $\gamma$ Hodge, by (HL) injectivity and (SS). $\square$

**Remark 3.3′ (what (JI) is, and why HC in lower dimension does not supply it).** By the classical theory of normal functions (Griffiths [Gr69]; Zucker [Zu76]):
- the class of a family of fibrewise homologically trivial cycles in $L^1=H^1(V',R^{2p-1})$ is the topological invariant of its Abel–Jacobi normal function $v'\mapsto AJ(\mathcal Z_{v'})$;
- the image of $\alpha$ is the topological invariant of the normal function $\nu_\alpha$.

So (JI) is implied by "Jacobi inversion": $AJ(\mathcal Z_{v'})=c\,\nu_\alpha(\phi(v'))$. This is Lefschetz's proof of the $(1,1)$ theorem for $p=1$ and Zucker's proof of HC for cubic fourfolds [Zu77], where Jacobi inversion holds because the intermediate Jacobian of a cubic threefold is generated by Abel–Jacobi images of differences of lines [CG72].

(JI) concerns cycles that are **homologically trivial on every member**. $\mathrm{HC}(Y_t)$ is a statement modulo homological equivalence and says nothing about such cycles. Nori's theorem sharpens this (cited, not proved here, statement as reported in [AC94]): for sections of sufficiently high degree, the restriction to a very general member $Y$ of a cycle representing a nonzero primitive class is **not algebraically equivalent to zero**, even rationally. The needed inductive input therefore lives in the Griffiths groups $\mathrm{Griff}^p(Y_t)_{\mathbb Q}$, which can be infinitely generated (Clemens, Voisin, Nori), and HC for $(2m+1)$-folds does not control them. This is the precise sense in which "HC$(2m+1)\Rightarrow$HC$(2m+2)$" is out of reach of the method. It is not a proof that the implication is false.

**Proposition 3.4 (a reduction to fourfolds would settle an open case by a method blind to it).** Let $A$ be a general abelian sixfold of Weil type for an imaginary quadratic field $K$ (signature $(3,3)$), for instance of non-split discriminant, and let $W_K\subseteq\mathrm{Hdg}^3(A)$ be its 2-dimensional space of Weil classes. Then:
- the images of $W_K$ in $\mathcal D^3(A):=\mathrm{Hdg}^3(A)/\mathrm{NS}_{\mathbb Q}\cdot\mathrm{Hdg}^2(A)$ span a 2-dimensional subspace;
- the Gysin images from all smooth ample divisors of $A$ meet $W_K$ only in $0$;
- every smooth member of $|L^k|$, for the polarization $L$, restricts $W_K$ to $0$.

*Proof, modulo cited facts.* We need two facts from [We77, vG94] (see also docs/02 §2.2):
- $W_K=\wedge^6_KH^1(A,\mathbb Q)$ consists of Hodge classes;
- for general $A$ of Weil type, $\mathrm{End}^0(A)=K$ with Rosati involution equal to complex conjugation, so $\rho(A)=1$, $\mathrm{NS}_{\mathbb Q}=\mathbb Q\theta$ and $\mathrm{NS}\cdot\mathrm{Hdg}^2=\theta\cdot\mathrm{Hdg}^2$.

Write $H^1(A,\mathbb C)=V_\sigma\oplus V_{\bar\sigma}$ for the eigenspaces of $K$, each of dimension 6. Then $W_K\otimes\mathbb C=\wedge^6V_\sigma\oplus\wedge^6V_{\bar\sigma}$. The polarization $\theta$ is $K$-hermitian, so $\theta\in V_\sigma\otimes V_{\bar\sigma}$, and $\theta\cdot w$ lies in $\wedge^7V_\sigma\otimes V_{\bar\sigma}\oplus V_\sigma\otimes\wedge^7V_{\bar\sigma}=0$. Hence $W_K\subseteq\ker\theta=P^6_\theta$.

By (HL), $P^6_\theta\cap\theta H^4=0$, so $W_K\cap\mathrm{NS}\cdot\mathrm{Hdg}^2=0$ and $W_K$ injects into $\mathcal D^3(A)$; this is the first item. Every ample class is a rational multiple of $\theta$, so Proposition 3.1(2) gives the second item and Proposition 3.1(1) the third. $\square$

The algebraicity of $W_K$ for non-split discriminant is open (docs/02 §2.2, docs/03 §3.5 P1). Any proof of HC$(6)$ from HC$(5)$ must prove it. Propositions 3.1 and 3.4 show that restriction to, and Gysin maps from, smooth ample divisors give no information about these classes. Markman's proof for discriminant $-1$ uses mechanism M2 of docs/03, not induction on dimension.

## 4. Target (a) in the middle degree: the Gysin condition

Let $\dim X=2p$. By §3.2, smooth divisors are useless here, so the Gysin condition has to involve singular divisors. For a reduced divisor $D\subset X$ let $\nu\colon\tilde D\to X$ be a resolution composed with the inclusion; here $\tilde D$ is the disjoint union of resolutions of the components.

**Proposition 4.1 (Gysin criterion).** Assume $\mathrm{HC}(2p-1)$; for $p=2$ this is the classical fact that HC holds for threefolds. Then $\mathrm{HC}(X,p)$ holds if and only if

> **(G)** there are finitely many reduced divisors $D_1,\dots,D_r$ with $\mathrm{Hdg}^p(X)\subseteq\sum_i\nu_{i*}H^{2p-2}(\tilde D_i)$.

*Proof.* **(G)$\Rightarrow$HC.** The map $\bigoplus_iH^{2p-2}(\tilde D_i)(-1)\to H^{2p}(X)$ is a morphism of polarizable Hodge structures. By (SS), a Hodge class $\alpha$ in its image equals $\sum\nu_{i*}\gamma_i$ with $\gamma_i\in\mathrm{Hdg}^{p-1}(\tilde D_i)$. By $\mathrm{HC}(\tilde D_i)$ the $\gamma_i$ are algebraic, and proper push-forward preserves algebraic classes.

**HC$\Rightarrow$(G).** Let $\mathrm{Hdg}^p(X)$ be spanned by classes of subvarieties $Z_1,\dots,Z_r$. Fix $i$, and for $k\gg0$ let $D_i$ be a general member of $|I_{Z_i}\otimes L^k|$. Then $D_i$ is reduced and smooth at the generic point of $Z_i$: since $\mathrm{codim}\,Z_i=p\ge1$ and $I_{Z_i}/I_{Z_i}^2\otimes L^k$ is globally generated, the general section has nonzero differential at the generic point. A resolution of $D_i$ that is an isomorphism over the smooth locus contains the strict transform $\tilde Z_i$, and $\nu_{i*}\mathrm{cl}(\tilde Z_i)=\mathrm{cl}(Z_i)$. $\square$

This is the classical statement that, given HC in lower dimension, HC in degree $2p$ is equivalent to every Hodge class having coniveau $\ge1$ [Le99], [Vo03]. It is a *tautological* closing condition: (G) carries the same content as $\mathrm{HC}(X,p)$. What can be said is how singular the $D_i$ must be.

**Proposition 4.2 (Milnor bound).** Let $\dim X=2p\ge2$, $L$ very ample, $h=c_1(L)$, and let $D\in|L|$ have only isolated singular points $x_1,\dots,x_k$, with total Milnor number $\mu(D)=\sum_i\mu(D,x_i)$. Then
$$\nu_*H^{2p-2}(\tilde D)=h\cdot H^{2p-2}(X)\ \oplus\ V_D,\qquad V_D:=\nu_*H^{2p-2}(\tilde D)\cap P^{2p}_L(X),\qquad \dim V_D\le\mu(D).$$
The same decomposition holds for Hodge classes. Consequently the image of $\nu_*\mathrm{Hdg}^{p-1}(\tilde D)$ in $\mathcal D(X)=\mathrm{Hdg}^p/\mathrm{NS}\cdot\mathrm{Hdg}^{p-1}$ has dimension at most $\mu(D)$. More precisely, $\dim V_D\le\dim\big(\mathrm{Im}(H^{2p}(X)\to H^{2p}(D))\cap\ker(sp)\big)$, where $sp\colon H^{2p}(D)\to H^{2p}(Y_t)$ is the specialization defined in the proof.

*Proof.* $D$ is reduced, because a non-reduced component would be singular everywhere. Hence $\nu_*1=[D]$, and the projection formula gives $\nu_*\nu^*\gamma=h\gamma$, so $\nu_*H^{2p-2}(\tilde D)\supseteq hH^{2p-2}(X)$. With $H^{2p}=P^{2p}_L\oplus hH^{2p-2}$ (HL) this gives the displayed decomposition. It remains to bound $\dim\nu_*H^{2p-2}(\tilde D)$.

*Poincaré duality.* $\nu_*\colon H^{2p-2}(\tilde D)\to H^{2p}(X)$ is the transpose of $\nu^*\colon H^{2p}(X)\to H^{2p}(\tilde D)$ for the Poincaré pairings on $X$ (in degrees $2p+2p=4p$) and on $\tilde D$ (in degrees $2p+(2p-2)=2\dim\tilde D$). So $\mathrm{rk}\,\nu_*=\mathrm{rk}\,\nu^*$. Moreover $\nu^*$ factors through the restriction $\rho_D\colon H^{2p}(X)\to H^{2p}(D)$, so $\mathrm{rk}\,\nu_*\le\mathrm{rk}\,\rho_D$.

*Bounding $\mathrm{rk}\,\rho_D$.* Choose $Y_\infty\in|L|$ general: smooth, missing $x_1,\dots,x_k$, and transverse to $D_{\rm reg}$. The pencil $\langle D,Y_\infty\rangle$ is then admissible: $B=D\cap Y_\infty$ is smooth by Bertini on $D_{\rm reg}$, and the general member is smooth because $Y_\infty$ is.

On $\tilde X=\mathrm{Bl}_BX$, the map $f$ is submersive along $E$ (since $f|_E=\mathrm{pr}_2$) and along $f^{-1}(0)\setminus\{x_i\}$. Near each $x_i\notin B$, $f$ is a local equation of $D$; an isolated singularity of the reduced hypersurface $f^{-1}(0)$ is an isolated critical point of $f$ with Milnor number $\mu(D,x_i)$.

Take a small disc $\Delta\ni0$ with no other critical values, and $t\in\Delta^*$. By (T1), $H^{2p}(f^{-1}(\Delta))\cong H^{2p}(D)$; let $sp\colon H^{2p}(D)\to H^{2p}(F_t)=H^{2p}(Y_t)$ be the restriction. By (T2) with $N=2p$, the exact sequence
$$H^{2p}(f^{-1}(\Delta),F_t)\to H^{2p}(f^{-1}(\Delta))\xrightarrow{sp}H^{2p}(F_t)$$
gives $\dim\ker(sp)\le\mu(D)$.

The composite $sp\circ\rho_D$ is $j_t^*$, as all maps are induced by inclusions into $\tilde X\to X$. Hence $\ker\rho_D\subseteq\ker j_t^*$ and
$$\mathrm{rk}\,\rho_D=\mathrm{rk}\,j_t^*+\dim(\mathrm{Im}\,\rho_D\cap\ker sp)\le\mathrm{rk}\,j_t^*+\mu(D).$$
Finally, $\ker j_t^*|_{H^{2p}(X)}=P^{2p}_L$ by Proposition 3.1(1), so $\mathrm{rk}\,j_t^*=b_{2p}-\dim P^{2p}_L=b_{2p-2}=\dim hH^{2p-2}(X)$ by (HL). Therefore $\dim V_D=\mathrm{rk}\,\nu_*-b_{2p-2}\le\mu(D)$.

The Hodge-class statement follows from (SS) applied to $\nu_*$ and to the decomposition $P^{2p}_L\oplus hH^{2p-2}$. $\square$

*Remarks.*
1. For a nodal $D$, $\dim\ker sp$ is the classical **defect** $\delta(D)$, the number of independent relations among the vanishing cycles of the nodes [Cl83]. A node whose vanishing cycle is nonzero and independent of the others contributes nothing. For instance, the singular members of a Lefschetz pencil with $H_{\rm van}\neq0$ have $V_D=0$, which recovers Proposition 3.2.
2. *Isolated singularities only see "rigid" vanishing relations.* To reach an $r$-dimensional space of primitive Hodge classes using members of $|L|$ with isolated singularities, the members used must have total Milnor number at least $r$. Moreover their singular points must be in special position, since only the dependent vanishing cycles count.
3. *Positive-dimensional singular loci.* For divisors with non-isolated singularities, (T2) fails and no such bound holds. Proposition 4.1 requires no restriction on singularities, and that is why it is tautological.

### 4.3 Attempt at a new class, and where it stops

The natural attempt at the top target is a two-step program for a family of $2p$-folds not covered by mechanisms M1–M6 of docs/03:
1. produce divisors $D_i\in|L^{k}|$ with isolated singularities whose defect spaces $V_{D_i}$ span $\mathrm{Hdg}^p_{\rm prim}$;
2. conclude by Propositions 4.1 and 4.2, together with $\mathrm{HC}(\tilde D_i,p-1)$, which is Lefschetz $(1,1)$ for $p=2$ and Theorem B for $p\ge3$.

Step 2 is complete. **Step 1 is the gap.** No Hodge-theoretic criterion I know produces divisors with prescribed vanishing-cycle relations. The defect of a nodal divisor is governed by the failure of its nodes to impose independent conditions on an adjoint-type linear system (Clemens' formula for threefolds in $\mathbb P^4$ [Cl83]). Constructing nodal divisors whose defect spaces contain a *given* Hodge class therefore amounts to locating the support of a cycle representing it, which is the conjecture itself.

The only families where I can verify Step 1 are those whose Hodge classes are already known to be algebraic by special geometry. The model case is Example 5.3 below: the Fermat cubic fourfold, with nodal Segre-cubic sections. So **no new class is obtained.**

## 5. Target (c): the invariant measuring the failure, Nori, and an explicit computation

**Definition.** For $X$ smooth projective of dimension $2p$, the **Lefschetz defect** of $X$ is
$$\mathcal D(X):=\mathrm{Hdg}^p(X)\Big/\sum_{Y}j_{Y*}\mathrm{Hdg}^{p-1}(Y),$$
the sum running over all smooth ample divisors $Y\subset X$. It is the cokernel on Hodge classes of all Gysin maps from smooth ample divisors.

**Proposition 5.1.** The following hold:
1. $\sum_Yj_{Y*}\mathrm{Hdg}^{p-1}(Y)=\mathrm{NS}(X)_{\mathbb Q}\cdot\mathrm{Hdg}^{p-1}(X)$, so $\mathcal D(X)=\mathrm{Hdg}^p/\mathrm{NS}_{\mathbb Q}\cdot\mathrm{Hdg}^{p-1}$;
2. if $\rho(X)=1$, then $\mathcal D(X)\cong\mathrm{Hdg}^p_{\rm prim}(X)$;
3. under $\mathrm{HC}(2p-1)$, $\mathrm{NS}\cdot\mathrm{Hdg}^{p-1}\subseteq A^p(X)$, so $\mathrm{HC}(X,p)$ holds if and only if $\mathcal D(X)$ is spanned by images of algebraic classes.

*Proof.* (1): "$\subseteq$" is Proposition 3.1(2). For "$\supseteq$": for any line bundle $M$ and very ample $A$, $M\otimes A^k$ is very ample for $k\gg0$, so very ample classes span $\mathrm{NS}_{\mathbb Q}$. Very ample systems have smooth members (Bertini), and the Gysin image of a member of class $y$ is $y\cdot\mathrm{Hdg}^{p-1}(X)$.

(2): (HL) and (SS) give $\mathrm{Hdg}^p=\mathrm{Hdg}^p_{\rm prim}\oplus h\,\mathrm{Hdg}^{p-1}$.

(3): if $Y$ is a smooth ample divisor and $\gamma\in\mathrm{Hdg}^{p-1}(X)$, then $j_Y^*\gamma$ is algebraic by $\mathrm{HC}(Y)$, so $y\gamma=j_{Y*}j_Y^*\gamma$ is algebraic. $\square$

So $\mathcal D$ is the task's "cokernel of the Gysin map on Hodge classes". For a very general hypersurface of degree $\ge3$ in $\mathbb P^{2p+1}$, $\mathrm{Hdg}^p=\mathbb Qh^p$ (docs/02 §2.1), so $\mathcal D=0$. In such families $\mathcal D$ is nonzero only on the Hodge loci (C5 in docs/03). Propositions 5.2 and 5.4 make the corresponding statement for the induction precise, using Nori's theorem.

**Proposition 5.2 (Nori: algebraic classes on very general sections come from the ambient variety).** Let $M$ be smooth projective of dimension $n+1$ and $L$ Nori-ample. Let $\mathcal Y\to B$ be the universal smooth member of $|L|$, and let $2p<2n$. There is a countable union $\Sigma$ of proper closed subvarieties of $B$ such that $A^p(Y_t)\subseteq j_t^*H^{2p}(M)$ for all $t\in B\setminus\Sigma$.

*Proof.* Apply the construction of Lemma 2.1 to $\mathcal Y\to B$, for *all* data rather than for a fixed $\lambda$. Each datum gives a proper $f\colon\tilde H\to B$ and a flat section $s(h)=\sum_ja_j\,\mathrm{cl}[\mathcal Z_{j,h}]_p$ over $\tilde H$. Let $\Sigma$ be the union of the $f(\tilde H)$ that are proper subsets of $B$.

Let $t\notin\Sigma$ and $z\in A^p(Y_t)$. As in Lemma 2.1, $z=s(h)$ for some datum and some $h\in f^{-1}(t)$, and $f(\tilde H)\ni t$ forces $f(\tilde H)=B$. By generic smoothness there is a dense open $B^0\subseteq B$ over which $f$ is smooth; put $T=f^{-1}(B^0)$, which is smooth quasi-projective and smooth over $B$. The class $\Gamma=\sum_ja_j\mathrm{ch}_p(\mathcal O_{\mathcal Z_j})|_{\mathcal Y_T}\in H^{2p}(\mathcal Y_T)$ equals $\iota^*\xi$ for some $\xi\in H^{2p}(M\times T)$ by (N), since $2p<2n$.

For $h'\in T$, the fibre inclusion $Y_{f(h')}\hookrightarrow\mathcal Y_T\xrightarrow{\iota}M\times T$ factors through $M\times\{h'\}$. So $s(h')=j_{f(h')}^*\xi_0$, where $\xi_0=\xi|_{M\times\{h'\}}$; this is independent of $h'$ because $T$ is connected. The flat sections $s$ and $h'\mapsto j^*_{f(h')}\xi_0$ therefore agree on $T$, hence on the connected $\tilde H$. In particular $z=s(h)=j_t^*\xi_0$. $\square$

By (L), the statement has content only in the middle degree $2p=n$; for $2p<n$ and $2p>n$, $j_t^*$ is respectively an isomorphism and surjective on $H^{2p}$. There it says: *algebraic classes on a very general Nori-ample section have no vanishing component.*

**Example 5.3 (Fermat cubic fourfold; computed).** Let $X=\{\sum_{i=0}^5x_i^3=0\}\subset\mathbb P^5$, $L=\mathcal O(1)$ and $\omega=e^{2\pi i/3}$.

*Part 1: the defect.* $\rho(X)=1$ and $\dim\mathrm{Hdg}^2(X)=21=h^{2,2}$ [docs/04 §4.1; recomputed with `hodge.fermat`]. So $\mathcal D(X)\cong\mathrm{Hdg}^2_{\rm prim}(X)\cong\mathbb Q^{20}$ by Proposition 5.1.

*Part 2: the planes.* For a partition $\pi=\{\{a_1,b_1\},\{a_2,b_2\},\{a_3,b_3\}\}$ of $\{0,\dots,5\}$ into pairs and $\zeta\in\mu_3^3$, let $P(\pi,\zeta)=\{x_{a_k}+\zeta_kx_{b_k}=0,\ k=1,2,3\}$. These $15\cdot27=405$ planes lie on $X$. For planes on a smooth cubic fourfold:
- $P^2=c_2(N_{P/X})=3$, from $c(N_{P/X})=(1+h)^3/(1+3h)$;
- for $P\neq P'$:
  - $P\cdot P'=-1$ if they meet in a line, by excess intersection: $3-3-3+2$;
  - $P\cdot P'=1$ if they meet in a point, where the intersection is transverse;
  - $P\cdot P'=0$ if they are disjoint.

The intersection form is positive definite on $\mathrm{Hdg}^2(X)_{\mathbb R}$ (Hodge–Riemann, $p=2$), so the rank of a Gram matrix equals the dimension of the span.

*Part 3: the Segre sections.* For $\lambda\in(\mathbb Z/3)^6/\mathbb Z/3$, the hyperplane section $D_\lambda=X\cap\{\sum_i\omega^{\lambda_i}x_i=0\}$ is the image of the Segre cubic $S_3=\{\sum x_i=\sum x_i^3=0\}$ under the automorphism $x_i\mapsto\omega^{-\lambda_i}x_i$ of $X$. There are 243 such sections. $S_3$ has exactly 10 singular points, the points $(\pm1,\dots,\pm1)$ with three plus signs, and they are nodes; so $\mu(D_\lambda)=10$. Each $D_\lambda$ contains exactly 15 of the planes, and each plane lies in 9 of the $D_\lambda$.

*Part 4: the computation.* Exact linear algebra over $\mathbb Q(\omega)$ for the pairwise intersections, then ranks of integer Gram matrices; the script is reproduced in Appendix 9.1. Results:
1. The Gram matrix of the 405 planes has rank 21, computed modulo $10^9+7$. Rank modulo a prime is a lower bound for the rational rank, and 21 is also an upper bound, so the planes span $\mathrm{Hdg}^2(X)$.
2. The Gram matrix of the 15 planes in $D_{\mathbf 0}=S_3$ has exact rational rank 6, and it stays 6 after adjoining $h^2$ (where $h^2\cdot P=1$ and $h^4=3$). So these planes span $\mathbb Qh^2\oplus V'$ with $\dim V'=5$ and $V'\subseteq V_{D_{\mathbf 0}}$.
3. For $\lambda\in\{(0,0,2,0,0,1),(0,1,1,0,0,0),(0,2,0,2,1,2),(0,0,0,0,2,1)\}$, the 60 planes in these four sections span all of $\mathrm{Hdg}^2(X)$ (rank 21 modulo the same prime).

*Conclusions.*
- $V_{D_\lambda}$ has dimension between 5 and 10, the upper bound coming from Proposition 4.2.
- It is exactly 5, using the classical fact $b_4(S_3)=6$: $S_3$ has the small resolution $\mathrm{Bl}_5\mathbb P^3$ [Hu96], so $\mathrm{rk}\,\nu^*\le b_4(D_\lambda)=6$. This equals the defect of $S_3$.
- Hence a single Segre section lowers the 20-dimensional Lefschetz defect by exactly its defect, 5. At least 4 Segre sections are needed, and 4 suffice.
- Together with Lefschetz $(1,1)$ on resolutions of the $D_\lambda$ and Proposition 4.1, this gives a proof of $\mathrm{HC}(X,2)$ by the singular-divisor induction. The result itself is classical (Zucker; Shioda; the planes); what is new is the computation of the invariant and of how the induction closes.

*Contrast.* A very general cubic fourfold has $\mathrm{Hdg}^2=\mathbb Qh^2$, so $\mathcal D=0$. For a smooth cubic fourfold containing a plane $P$, the primitive class $[P]-h^2/3$ lies in the image of $H_4(D)\to H_4(X)$ for every hyperplane section $D\supseteq P$. Every such $D$ is singular: for smooth $D$ that image would be $\mathbb Qh^2$ by Proposition 3.1(2), whereas $[P]^2=3\neq\tfrac13=(h^2/3)^2$.

**Proposition 5.4 (on very general Nori-ample sections the induction is an equivalence).** Let $M$ be smooth projective of dimension $2p+1$, $L$ Nori-ample, and assume $h\cdot\mathrm{Hdg}^{p-1}(M)\subseteq A^p(M)$ (for instance $\mathrm{HC}(M,p-1)$). The following are equivalent:
1. $\mathrm{HC}(Z,p)$ for very general $Z\in|L|$;
2. $\mathrm{HC}(M,p)$, and $\mathrm{Hdg}^p(Z)=j_Z^*\mathrm{Hdg}^p(M)$ for very general $Z$.

*Proof.* (2)$\Rightarrow$(1): $\mathrm{Hdg}^p(Z)=j^*\mathrm{Hdg}^p(M)=j^*A^p(M)\subseteq A^p(Z)$.

(1)$\Rightarrow$(2): for very general $Z$, Proposition 5.2 gives $\mathrm{Hdg}^p(Z)=A^p(Z)\subseteq j^*H^{2p}(M)$. Since $j^*$ is injective on $H^{2p}(M)$ by (L), with $2p=\dim M-1$, and is a morphism of Hodge structures, the preimage of a Hodge class is a Hodge class; so $\mathrm{Hdg}^p(Z)=j^*\mathrm{Hdg}^p(M)$.

For $\mathrm{HC}(M,p)$, let $\beta\in\mathrm{Hdg}^p(M)$. The very general locus is the complement of a countable union of proper closed subsets $S_i\subset|L|$. Choose $t_1$ outside all $S_i$ and an admissible pencil through $t_1$. Admissibility is an open condition on lines through $t_1$. Such a pencil is contained in no $S_i$, so it meets each $S_i$ in finitely many points, and $j^*\beta$ is algebraic on uncountably many of its members. Theorem A and Corollary A.1 give $\beta\in A^p(M)$. $\square$

*Reading.* On very general sections, where Nori's theorem applies, the induction step neither gains nor loses. $\mathrm{HC}(M,p)$ is equivalent to HC for the very general section plus a purely Hodge-theoretic "no new classes" statement; I expect that statement to follow from Nori's theorem combined with the algebraicity of Hodge loci [CDK95], but I have not checked this and do not use it. The classes that make a $2p$-fold hard, those in $\mathcal D$, occur only on special members (Hodge loci). There the hypothesis "very general" fails, and Proposition 3.1 shows that restriction and Gysin maps of smooth members see nothing of them. **For very general sections of a Nori-ample system this is a precise form of "the induction cannot create new cycles": there the step closes only on classes already restricted from the ambient variety, and the residue $\mathcal D$ lives on special members (where §4 shows that singular sections can still close it, as for the Fermat cubic).**

## 6. GAPS

**G1 (top target (a): no new class).** The statement I would need is:

> *For some family of $2p$-folds not covered by M1–M6 of docs/03, there are divisors $D_i$ with isolated singularities whose defect spaces $V_{D_i}$ (Proposition 4.2) span $\mathrm{Hdg}^p_{\rm prim}$.*

Given that, Propositions 4.1 and 4.2 with Lefschetz $(1,1)$ for $p=2$, or Theorem B for $p\ge3$, give HC. I cannot prove it for any new family. Producing divisors with prescribed vanishing-cycle relations is equivalent to locating the support of cycles representing the classes (§4.3). The only verified instance, Example 5.3, is a variety whose Hodge classes were already known to be algebraic.

**G2 (target (b): the odd-to-even step).** "HC$(2m+1)\Rightarrow$HC$(2m+2)$" is not proved. The exact missing statement is (JI) of Proposition 3.3 for every primitive middle-degree Hodge class on every $(2m+2)$-fold, and (JI) is *equivalent* to the algebraicity of the class. HC in dimension $2m+1$ gives no information on (JI), because (JI) concerns families of cycles that are homologically trivial on every member (Remark 3.3′). I do not claim the implication is false; I claim only that this method cannot prove it. Proposition 3.4 shows that any proof would in particular settle the open discriminant-$(+1)$ Weil sixfolds.

**G3 (Nori's theorem used as a black box).** The statement (N) was checked only against secondary sources: [Vo02N] as summarized by search, and arXiv:2209.13683. Two points should be confirmed against [No93]: the range "isomorphism for $k<2n$, injective for $k=2n$, with $n=\dim Y_b$", and the hypothesis "$T\to B$ smooth, $T$ smooth quasi-projective". Only Propositions 5.2 and 5.4 depend on (N), and only through degree $k=2p=n$ (Proposition 5.4) or $k=2p<2n$ (Proposition 5.2).

**G4 (Griffiths-group consequence of Nori).** The statement in Remark 3.3′ is taken from the summary of [AC94]: restrictions of cycles representing nonzero primitive classes are nonzero in $\mathrm{Griff}(Y)_{\mathbb Q}$ for very general high-degree $Y$. It is not proved here and not used in any labelled result.

**G5 (Example 5.3, upper bound).** "$\dim V_{D_\lambda}=5$ exactly" and "at least 4 Segre sections are needed" use the classical fact $b_4(S_3)=6$ [Hu96]. Proof (added at the referee's suggestion): $\mathrm{Bl}_5\mathbb P^3\to S_3$ is a small resolution whose exceptional set is a disjoint union of ten $\mathbb P^1$'s, so $H^4(S_3)\cong H^4(\mathrm{Bl}_5\mathbb P^3)$, which has rank $b_2(\mathrm{Bl}_5\mathbb P^3)=6$. Without it, Proposition 4.2 gives $5\le\dim V_{D_\lambda}\le10$, and hence that at least 2 sections are needed. The lower bounds and "four suffice" are rigorous computations: exact rational rank for the 15- and 16-element Gram matrices, and the rank modulo a prime against the upper bound 21 for the others.

**G6 (cited structure facts).** The following are taken from the literature and not reproved:
- Proposition 3.4 uses $\mathrm{End}^0(A)=K$ and $\rho(A)=1$ for a general Weil-type abelian variety, and that Weil classes are Hodge [We77, vG94];
- (Top) uses standard Milnor-fibration and Lefschetz-pencil topology [Mi68, La81, Di92];
- (Hilb) uses [Fu, Ex. 15.3.6].

The exact numbering of the cited results in [Vo02], [Vo03] and [Fu] should be checked by the literature referee.

**G7 (novelty).** Theorem A, Theorem B and Propositions 3.2, 3.3 and 4.1 are known in substance ([KP11], [dS21], [Zu77], [Le99]); what is mine is the exact formulation and the complete proofs. Proposition 4.2, Proposition 5.4 and the computation in Example 5.3 I believe to be new in this form, but they are elementary, and I rate my confidence in their novelty as low.

## 7. Checklist (docs/03 §3.4)

**Items 1–4 (absoluteness, Lefschetz B, VHC, open special cases).** None is delivered, as expected: nothing here proves HC. Two consistency checks:
- The induction uses hard Lefschetz only in the direction "$h^{n-2p}$ maps algebraic classes to algebraic classes". It never inverts $h$, so it does not presuppose Lefschetz B.
- Theorem A assumes algebraicity at uncountably many points, so it is not a case of the variational Hodge conjecture.

**Where rational coefficients are essential.**
1. *The multisection degree $e$ in Theorem A, and the coefficients $a_j$.* Even integral HC for all $Y_t$ yields only $e\alpha$.
2. *The hard Lefschetz step in Theorem B(1),* for degrees $2p>n$. Over $\mathbb Z$, $h^{n-2q}$ is not surjective on integral classes.
3. *(SS),* which is used to choose Hodge preimages.

**False-variant test: integral HC.** The integral analogue of Theorem B(1) is **false**. Integral HC holds for all surfaces (Lefschetz $(1,1)$ is integral), but fails for 1-cycles on Kollár's very general threefolds $X\subset\mathbb P^4$ of degree $d$ with $\ell^3\mid d$ (docs/01 §1.3). My proof breaks exactly at item 2 above. For such $X$, $H^4(X,\mathbb Z)=\mathbb Z\lambda$ with $h^2=d\lambda$, and the step $\mathrm{HC}(X,1)\Rightarrow\mathrm{HC}(X,2)$ produces only $d\lambda$.

For torsion classes (Atiyah–Hirzebruch), (L) holds integrally in degree $2p\le n-2$, so restriction is an isomorphism. Theorem A nevertheless produces only $e\alpha$, which is $0$ if $e$ kills the class. So no integral statement follows, which is consistent.

**Where projectivity is essential.** Every result starts from an ample line bundle: pencils and their blow-ups, the Lefschetz hyperplane theorem (an affine complement), relative Hilbert schemes projective over the base, Bertini, and Nori's theorem.

**False-variant test: Kähler HC.** Voisin's 4-dimensional tori (docs/01 §1.3) have no ample bundle and no hypersurfaces at all, so none of the arguments starts. Their exotic class lies in middle degree on a 4-fold, i.e. in the analogue of $\mathcal D$. On projective varieties, that is exactly the part the method provably cannot reach (Proposition 3.1), which is consistent.

The Kähler analogue of Theorem B is not even formulable. A compact Kähler manifold with a smooth ample divisor is projective (Kodaira), so the hypotheses of Theorem A force projectivity.

**Other variants.** No positivity, currents or integrality of cycle classes are used (C4 of docs/03). The method sees only the fixed part of a family's cohomology; that is consistent with C5 (the generic fibre is never where the problem is), and Proposition 5.4 makes it precise.

## 8. References

- [AC94] A. Albano, A. Collino, *On the Griffiths group of the cubic sevenfold*, arXiv:alg-geom/9308001 (Math. Ann., 1994). Cited only in Remark 3.3′, for Nori's Griffiths-group consequence.
- [CDK95] E. Cattani, P. Deligne, A. Kaplan, *On the locus of Hodge classes*, J. Amer. Math. Soc. 8 (1995) 483–506. Cited only in the reading of Proposition 5.4.
- [CG72] C. H. Clemens, P. Griffiths, *The intermediate Jacobian of the cubic threefold*, Ann. of Math. 95 (1972) 281–356.
- [Cl83] C. H. Clemens, *Double solids*, Adv. Math. 47 (1983) 107–230 (defect of nodal threefolds).
- [Di92] A. Dimca, *Singularities and Topology of Hypersurfaces*, Universitext, Springer, 1992.
- [DM22] *Nori's connectivity theorem from the perspective of D-modules*, arXiv:2209.13683 (secondary source for (N)).
- [dS21] G. da Silva Jr., *Notes on the Hodge conjecture for Fermat varieties*, Experimental Results 2 (2021) e22, arXiv:2101.04739. Its introduction states the reduction of HC to primitive middle classes on even-dimensional varieties "using hard Lefschetz, Lefschetz hyperplane theorem and some Hilbert scheme arguments".
- [FGA] A. Grothendieck, *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: les schémas de Hilbert*, Sém. Bourbaki 221 (1960/61).
- [Fu] W. Fulton, *Intersection Theory*, 2nd ed., Springer, 1998.
- [Gr69] P. Griffiths, *On the periods of certain rational integrals I, II*, Ann. of Math. 90 (1969) 460–541.
- [Hu96] B. Hunt, *The Geometry of Some Special Arithmetic Quotients*, Lecture Notes in Math. 1637, Springer, 1996 (Segre cubic).
- [KP11] M. Kerr, G. Pearlstein, *An exponential history of functions with logarithmic growth*, in: Topology of Stratified Spaces, MSRI Publ. 58 (2011), arXiv:0903.4903. States, as part of Griffiths' program, that "by induction on dimension, the Hodge conjecture can be reduced to the case of middle dimensional Hodge classes on even dimensional varieties".
- [La81] K. Lamotke, *The topology of complex projective varieties after S. Lefschetz*, Topology 20 (1981) 15–51.
- [Le99] J. D. Lewis, *A Survey of the Hodge Conjecture*, 2nd ed., CRM Monograph Ser. 10, AMS, 1999.
- [Ma25] E. Markman, arXiv:2502.03415 (Weil classes on sixfolds of discriminant $-1$; see docs/02 §2.2).
- [Mi68] J. Milnor, *Singular Points of Complex Hypersurfaces*, Ann. of Math. Stud. 61, Princeton, 1968.
- [No93] M. V. Nori, *Algebraic cycles and Hodge theoretic connectivity*, Invent. Math. 111 (1993) 349–373.
- [vG94] B. van Geemen, *An introduction to the Hodge conjecture for abelian varieties*, in: Algebraic Cycles and Hodge Theory (Torino 1993), Lecture Notes in Math. 1594, Springer, 1994.
- [Vo02] C. Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Stud. Adv. Math. 76, 2002.
- [Vo03] C. Voisin, *Hodge Theory and Complex Algebraic Geometry II*, Cambridge Stud. Adv. Math. 77, 2003.
- [Vo02N] C. Voisin, *Nori's connectivity theorem and higher Chow groups*, J. Inst. Math. Jussieu 1 (2002).
- [We77] A. Weil, *Abelian varieties and the Hodge ring* (1977), in Collected Papers III.
- [Zu76] S. Zucker, *Generalized intermediate Jacobians and the theorem on normal functions*, Invent. Math. 33 (1976) 185–222.
- [Zu77] S. Zucker, *The Hodge conjecture for cubic fourfolds*, Compositio Math. 34 (1977) 199–209.

## 9. Appendix

### 9.1 Script for Example 5.3

Pure Python with exact arithmetic; about 2 minutes. Output:
- `405 planes, rank mod p: 21`
- `Segre section: #planes 15  Q-rank 6  Q-rank with h^2 6`
- `four Segre sections: #planes 60  rank mod p 21`

```python
# Planes P(pi,z) = {x_a + w^z x_b = 0 for the 3 pairs (a,b) of pi} on X = {sum x_i^3 = 0} in P^5.
from fractions import Fraction as Fr
from itertools import product
def mul(u,v):  # elements a+b*w of Q(w), w^2 = -1-w, stored as pairs
    return (u[0]*v[0]-u[1]*v[1], u[0]*v[1]+u[1]*v[0]-u[1]*v[1])
def inv(u):
    n=u[0]*u[0]-u[0]*u[1]+u[1]*u[1]; return (Fr(u[0]-u[1])/n, Fr(-u[1])/n)
W=[(1,0),(0,1),(-1,-1)]                      # 1, w, w^2
def rank_K(M):                               # exact rank over Q(w)
    M=[r[:] for r in M]; r=0
    for c in range(6):
        i=next((i for i in range(r,len(M)) if M[i][c]!=(0,0)),None)
        if i is None: continue
        M[r],M[i]=M[i],M[r]; iv=inv(M[r][c]); M[r]=[mul(x,iv) for x in M[r]]
        for k in range(len(M)):
            if k!=r and M[k][c]!=(0,0):
                f=M[k][c]; M[k]=[(x[0]-mul(f,y)[0],x[1]-mul(f,y)[1]) for x,y in zip(M[k],M[r])]
        r+=1
    return r
def pairings(s):
    if not s: yield []; return
    for i in range(1,len(s)):
        for p in pairings(s[1:i]+s[i+1:]): yield [(s[0],s[i])]+p
planes=[(pi,z) for pi in pairings(list(range(6))) for z in product(range(3),repeat=3)]
def rows(P):
    out=[]
    for (a,b),k in zip(*P):
        r=[(0,0)]*6; r[a]=(1,0); r[b]=W[k]; out.append(r)
    return out
R=[rows(P) for P in planes]; N=len(planes)          # 405
VAL={3:3,4:-1,5:1,6:0}                               # rank of 6 forms -> P.P'
G=[[3 if i==j else VAL[rank_K(R[i]+R[j])] for j in range(N)] for i in range(N)]
def rank_p(M,p=10**9+7):
    A=[[x%p for x in r] for r in M]; r=0
    for c in range(len(A[0])):
        i=next((i for i in range(r,len(A)) if A[i][c]),None)
        if i is None: continue
        A[r],A[i]=A[i],A[r]; iv=pow(A[r][c],p-2,p); A[r]=[x*iv%p for x in A[r]]
        for k in range(len(A)):
            if k!=r and A[k][c]: f=A[k][c]; A[k]=[(x-f*y)%p for x,y in zip(A[k],A[r])]
        r+=1
    return r
def rank_Q(M):
    A=[[Fr(x) for x in r] for r in M]; r=0
    for c in range(len(A[0])):
        i=next((i for i in range(r,len(A)) if A[i][c]),None)
        if i is None: continue
        A[r],A[i]=A[i],A[r]
        for k in range(len(A)):
            if k!=r and A[k][c]: f=A[k][c]/A[r][c]; A[k]=[x-f*y for x,y in zip(A[k],A[r])]
        r+=1
    return r
def sec(lam):  # planes in D_lam = X ∩ {sum w^lam_i x_i = 0}
    return [i for i,(pi,z) in enumerate(planes) if all((lam[b]-lam[a])%3==z[k] for k,(a,b) in enumerate(pi))]
sub=lambda I:[[G[i][j] for j in I] for i in I]
print("405 planes, rank mod p:", rank_p(G))
S=sec((0,)*6); GS=sub(S)
print("Segre section: #planes", len(S), " Q-rank", rank_Q(GS),
      " Q-rank with h^2", rank_Q([r+[1] for r in GS]+[[1]*len(S)+[3]]))
four=[(0,0,2,0,0,1),(0,1,1,0,0,0),(0,2,0,2,1,2),(0,0,0,0,2,1)]
I=sorted({i for l in four for i in sec(l)})
print("four Segre sections: #planes", len(I), " rank mod p", rank_p(sub(I)))
```

## 10. Claimed results

| Label | One-line statement | Status |
|---|---|---|
| Lemma 2.1 | For a smooth projective family over a smooth base, the locus where a flat class is algebraic is a countable union of closed images $f_i(\tilde H_i)$ of proper families carrying cycles that represent the class on *every* fibre | known (standard Hilbert-scheme argument; cf. attack 01 Lemma A); proved here |
| Theorem A | $2p\le n-1$, $\alpha$ algebraic on uncountably many smooth members of one admissible pencil $\Rightarrow$ algebraic on all, and $e\alpha=\mathrm{cl}(W)+h\gamma_X$ with $\gamma_X\vert_B$ algebraic | known in substance [KP11, dS21]; proved here |
| Corollary A.1 | Under Theorem A, plus $h\,\mathrm{Hdg}^{p-1}\subseteq A^p$ (e.g. $p\le2$, or $\mathrm{HC}(X,p-1)$, or $\mathrm{HC}(Y_t,p-1)$ for one $t$): $\alpha\in A^p(X)$ | known in substance; proved here |
| Lemma 3.0 | HC for $Z\times\mathbb P^k$ implies HC for $Z$; middle-degree HC for $Z\times\mathbb P^{2r}$ implies middle-degree HC for $Z$ | elementary; proved here |
| Theorem B | $\mathrm{HC}(2m)\iff\mathrm{HC}(2m+1)$; HC in dimensions $\le2m+1$ $\iff$ middle-degree HC for $2m$-folds $\iff$ primitive middle-degree HC in even dimensions $\le2m$ | known in substance [KP11, dS21]; the dimension-by-dimension form (1) is implicit there; proved here |
| Proposition 3.1 | In middle degree, restriction to smooth members of $\lvert L^k\rvert$ kills $P^{2p}_L$; Gysin images from smooth ample divisors are $\mathrm{NS}\cdot H^{2p-2}$ (resp. $\mathrm{NS}\cdot\mathrm{Hdg}^{p-1}$); same for smooth complete intersections | elementary consequence of Lefschetz; proved here |
| Proposition 3.2 | For a Lefschetz pencil with $H_{\rm van}\ne0$, $P^{2p}_L(X)$ injects into the fibrewise-trivial classes $H^1(U',R^{2p-1})$ on the smooth part of the total space | known (Lefschetz; Zucker); proved here using (Top) |
| Proposition 3.3 | Cohomological Jacobi inversion (JI) for a primitive $\alpha$ is implied by $\alpha\in A^p$ and implies $\alpha\in A^p+h\,\mathrm{Hdg}^{p-1}$ | known in substance (Lefschetz $p=1$; Griffiths; Zucker 1977); proved here |
| Proposition 3.4 | For a general Weil-type abelian sixfold, $W_K$ is primitive and injects into $\mathcal D^3$; it is invisible to restriction to and Gysin maps from smooth ample divisors | proved here conditionally on cited facts ($\mathrm{End}^0=K$, $\rho=1$, Weil classes Hodge) [We77, vG94] |
| Proposition 4.1 | Under $\mathrm{HC}(2p-1)$: $\mathrm{HC}(X,p)\iff$ Hodge classes lie in the sum of Gysin images from finitely many resolved divisors | known (coniveau formulation; [Le99, Vo03]); proved here |
| Proposition 4.2 | A divisor $D\in\lvert L\rvert$ with isolated singularities enlarges the Gysin image beyond $h\,H^{2p-2}$ by at most $\mu(D)$ (more precisely by at most $\dim(\mathrm{Im}\,\rho_D\cap\ker sp)$, the defect for nodal $D$) | believed new in this form, elementary; proved here modulo standard Milnor-fibration topology (Top) |
| Proposition 5.1 | The Lefschetz defect $\mathcal D(X)$ (Gysin cokernel on Hodge classes) equals $\mathrm{Hdg}^p/\mathrm{NS}\cdot\mathrm{Hdg}^{p-1}$, and equals $\mathrm{Hdg}^p_{\rm prim}$ if $\rho=1$; under $\mathrm{HC}(2p-1)$, $\mathrm{HC}(X,p)\iff\mathcal D(X)$ is spanned by algebraic classes | elementary; proved here |
| Proposition 5.2 | For Nori-ample $L$ and $2p<2\dim Y$: algebraic classes on very general $Y\in\lvert L\rvert$ lie in $j^*H^{2p}(M)$ | known consequence of [No93]; proved here conditionally on Nori's theorem (N) as stated |
| Example 5.3 | Fermat cubic fourfold: $\mathcal D\cong\mathbb Q^{20}$; each Segre section (10 nodes) captures a 5-dimensional primitive subspace spanned by its 15 planes; four Segre sections suffice and at least four are needed | computed here (exact); "exactly 5" and "at least four" use the classical $b_4(S_3)=6$ [Hu96] |
| Proposition 5.4 | For Nori-ample $L$ on a $(2p+1)$-fold $M$ (with $h\,\mathrm{Hdg}^{p-1}(M)$ algebraic): HC for very general sections $\iff$ $\mathrm{HC}(M,p)$ + "no new Hodge classes on very general sections" | proved here conditionally on Nori's theorem (N); believed new formulation, low confidence in novelty |
| Top target (a) | $\mathrm{HC}(X,p)$ in the middle degree from HC of sections plus a Gysin condition verified in a new class | **not proved** (Gap G1) |
| Target (b), odd$\to$even | $\mathrm{HC}(2m+1)\Rightarrow\mathrm{HC}(2m+2)$ | **not proved**; the missing step is (JI), equivalent to the conclusion (Gap G2) |
