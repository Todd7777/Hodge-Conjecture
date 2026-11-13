# Attack 9: a degree-4 analogue of the exponential sequence via $K_2$ and Deligne cohomology

**Status (2026-11-07, second run).** Draft for refereeing. The top target of the ladder (rung (a): build, for every rational Hodge class $\alpha\in\mathrm{Hdg}^2(X)$, a class in $H^2(X,\mathcal K_2)\otimes\mathbb Q$ with cycle class $\alpha$ by a "$K_2$-exponential map") is **not proved**. What is proved here:

1. the obstruction group is identified exactly: it is the space $\mathrm{Hdg}(\eta_X)$ of degree-4 Hodge classes of the **generic point** of $X$ (Theorem A), a birational invariant (Corollary A.1). It is *not* a Zariski cohomology group of $\mathcal K_2$ or $\mathcal O^*$: those groups vanish identically in the relevant degrees (Lemma 2.3);
2. the analytic degree-4 exponential sequence exists (Deligne cohomology $=$ hypercohomology of $\mathcal O^*\xrightarrow{d\log}\Omega^1$, Propositions 2.1, 2.2), but restricted to an affine open set it carries **no information beyond the Betti class** (Lemma 2.4). Hence the single missing step of the Lefschetz argument is a "degree-4 GAGA" statement, which is **equivalent** to $\mathrm{HC}(X,2)$ (Theorem B). This is a reformulation of Theorem A(i), not a reduction to something easier;
3. rung (b): a sufficient condition for $\mathrm{HC}(X,2)$ on fourfolds fibred over a curve (Theorem D, Corollary D.1), a coniveau form of the Griffiths–Zucker normal-function mechanism proved without normal functions; and a proof that the vanishing hypotheses suggested in the ladder cannot work as stated (Proposition E);
4. rung (c): precise statements locating where $\mathbb Q$-coefficients and projectivity enter (Theorem C): the analytic sequence holds on every compact Kähler manifold; the "algebraization" step holds with $\mathbb Q$-coefficients and is **false** with $\mathbb Z$-coefficients (Kollár); the "GAGA" step fails in the analytic setting (Voisin's torus); and the Zariski analogue of the sequence is identically zero.

I know of no new case of the Hodge conjecture that follows from these results (see GAPS, G4). Most statements are classical or elementary; the table at the end says which.

**Referee (2026-11-13):** minor revision; corrections applied. Report summary: docs/06-attack-report.md.

**Verification note (important for the literature referee).** This run's web-search quota was used up before I could check anything online. Every external theorem is quoted below as an input (I1)–(I14), in the weakest form I use, either from `docs/01-03` or from memory. Theorem *numbers* in Deligne's *Théorie de Hodge II* are from memory and must be checked.

## 0. The argument in one page

Lefschetz (1,1) has three steps.

* **(E1)** Exponential sequence: an integral class of type $(1,1)$ is $c_1$ of a holomorphic line bundle. True on every compact Kähler manifold.
* **(E2)** GAGA: on projective $X$ that line bundle is algebraic, hence trivial on a nonempty Zariski open set $U$; so the class vanishes on $U$.
* **(E3)** A class vanishing on a Zariski open set is a combination of classes of divisors.

In degree 4 the picture is as follows.

| step | degree 2 | degree 4 | where proved here |
|---|---|---|---|
| (E1) | $H^1(X,\mathcal O^*)\twoheadrightarrow\mathrm{Hdg}^1_{\mathbb Z}$ | $H^4_{\mathcal D}(X,\mathbb Z(2))=\mathbb H^3(X,\mathcal O^*\to\Omega^1)\twoheadrightarrow\mathrm{Hdg}^2_{\mathbb Z}$; true on compact Kähler $X$ | Prop. 2.1, 2.2 |
| (E2) | GAGA for line bundles | "$\mathrm{GAGA}_4$": every Hodge class vanishes rationally on a nonempty Zariski open set. Lemma 2.4 shows the Deligne/2-gerbe refinement is invisible on affine opens; $\mathrm{GAGA}_4\iff\mathrm{HC}(X,2)$; false in the analytic setting on Voisin's torus | Lemma 2.4, Thm A, Thm B, Thm C(ii) |
| (E3) | trivial (components of $D$) | true with $\mathbb Q$-coefficients (Lefschetz (1,1) on a resolution of $D$ + weights + semisimplicity); **false** with $\mathbb Z$-coefficients | Prop. 3.1, Thm C(iii) |

So the whole content of $\mathrm{HC}(X,2)$ sits in (E2) at the generic point. Rung (a) is therefore answered by identifying the obstruction, not by removing it.

## 1. Conventions and inputs

$X$ is a smooth projective connected complex variety, $n=\dim X$. Cohomology is singular cohomology of the analytic space. $\mathrm{Hdg}^2(X)=H^4(X,\mathbb Q)\cap H^{2,2}(X)$; $A^2(X)=\mathrm{cl}(CH^2(X)_{\mathbb Q})\subset\mathrm{Hdg}^2(X)$; $\mathbb Z(p)=(2\pi i)^p\mathbb Z\subset\mathbb C$; $\mathrm{Hdg}^2_{\mathbb Z}(X)=\{\alpha\in H^4(X,\mathbb Z(2)):\alpha_{\mathbb C}\in F^2H^4(X,\mathbb C)\}$ (torsion included). For a Zariski open $U\subset X$, $H^k(U):=H^k(U^{an},\mathbb Q)$ with Deligne's mixed Hodge structure (MHS).

**Generic point.** The nonempty Zariski open subsets of $X$ form a directed system under reverse inclusion. Put
$$H^4(\eta_X):=\varinjlim_U H^4(U),\qquad \mathrm{Hdg}(\eta_X):=\varinjlim_U \mathrm{Hom}_{MHS}\big(\mathbb Q(-2),H^4(U)\big),$$
and let $\mathrm{ob}\colon H^4(X,\mathbb Q)\to H^4(\eta_X)$ be the restriction map. Evaluation at $1$ embeds $\mathrm{Hom}_{MHS}(\mathbb Q(-2),H^4(U))$ in $H^4(U)$; a filtered colimit of injections is injective, so $\mathrm{Hdg}(\eta_X)\subset H^4(\eta_X)$. The coniveau filtration is $N^1H^4(X,\mathbb Q)=\ker(\mathrm{ob})$, the classes that vanish on some nonempty Zariski open set.

**Inputs** (all standard; quoted in the form used).

* **(I1)** The category of polarizable pure $\mathbb Q$-Hodge structures is semisimple. Hence if $\phi\colon V\to W$ is a morphism of polarizable Hodge structures of the same weight and $w\in\mathrm{Im}\,\phi$ is a Hodge class, then $w=\phi(v)$ for a Hodge class $v$. (Write $V=\ker\phi\oplus V'$ with $V'$ a sub-Hodge structure; $\phi|_{V'}\colon V'\to\mathrm{Im}\,\phi$ is an isomorphism of Hodge structures.) A quotient of a polarizable Hodge structure is polarizable. Hard Lefschetz holds for an ample class.
* **(I2)** Lefschetz (1,1): on a smooth projective variety every class in $H^2(\cdot,\mathbb Q)\cap H^{1,1}$ is the class of a $\mathbb Q$-divisor (`docs/02`, §2.1).
* **(I3)** Deligne [D2, Cor. 3.2.17]: for $U$ smooth with smooth compactification $\bar U$, $H^k(U)$ has weights $\ge k$ and $W_kH^k(U)=\mathrm{Im}(H^k(\bar U)\to H^k(U))$.
* **(I4)** Deligne [D2, §3.2]: let $X'$ be smooth projective and $D'=\bigcup_i D'_i$ a simple normal crossing (SNC) divisor with smooth components $\gamma_i\colon D'_i\hookrightarrow X'$. The weight spectral sequence $E_1^{-m,k+m}=H^{k-m}(D'^{(m)})(-m)\Rightarrow H^k(X'\setminus D')$, whose $d_1$ is the alternating sum of Gysin maps, degenerates at $E_2$. Since $E_\infty^{0,k}=W_kH^k(X'\setminus D')$ is the image of the restriction map, $\ker\big(H^k(X')\to H^k(X'\setminus D')\big)=\sum_i\gamma_{i*}H^{k-2}(D'_i)$, where $\gamma_{i*}\colon H^{k-2}(D'_i)(-1)\to H^k(X')$ are the Gysin maps (morphisms of Hodge structures).
* **(I5)** Hironaka: for a divisor $D$ in a smooth projective $X$ there is a projective birational morphism $\mu\colon X'\to X$, a composite of blow-ups along smooth centres lying over $D$ (so $\mu$ is an isomorphism over $X\setminus D$), with $X'$ smooth and $\mu^{-1}(D)_{red}$ SNC.
* **(I6)** Deligne cohomology ([EV], [V-I, §12.3]): $\mathbb Z(p)_{\mathcal D}=[\mathbb Z(p)\to\mathcal O\to\Omega^1\to\dots\to\Omega^{p-1}]$. For compact Kähler $X$ there is an exact sequence $0\to J^p(X)\to H^{2p}_{\mathcal D}(X,\mathbb Z(p))\to\mathrm{Hdg}^p_{\mathbb Z}(X)\to0$ with $J^p=H^{2p-1}(X,\mathbb C)/(F^p+H^{2p-1}(X,\mathbb Z(p)))$. For $p=1$, $\mathbb Z(1)_{\mathcal D}\simeq\mathcal O^*[-1]$. For projective $X$ there is a cycle class $CH^p(X)\to H^{2p}_{\mathcal D}(X,\mathbb Z(p))$ lifting $\mathrm{cl}$.
* **(I7)** A smooth affine variety $U$ is Stein, so $H^i(U^{an},\mathcal F)=0$ for $i>0$ and $\mathcal F$ coherent (Cartan's Theorem B). Andreotti–Frankel [AF]: $U^{an}$ has the homotopy type of a finite CW complex of dimension $\le\dim U$, so $H^k(U^{an},\mathbb Z)=0$ for $k>\dim U$, and all $H^k(U^{an},\mathbb Z)$ are finitely generated.
* **(I8)** Quillen [Q, §7]: for $X$ smooth over a field, $\mathcal K_q$ (the Zariski sheaf of $K_q$) has the flasque Gersten resolution $0\to\mathcal K_q\to i_{\eta*}K_q(\mathbb C(X))\to\bigoplus_{x\in X^{(1)}}i_{x*}K_{q-1}(\kappa(x))\to\dots\to\bigoplus_{x\in X^{(q)}}i_{x*}\mathbb Z\to0$, and $H^q(X_{Zar},\mathcal K_q)\cong CH^q(X)$ (Bloch–Quillen).
* **(I9)** Bloch–Ogus [BO]: the Zariski sheaf $\mathcal H^q_{\mathbb Q}$ associated with $U\mapsto H^q(U)$ has a Gersten resolution beginning $0\to\mathcal H^q_{\mathbb Q}\to i_{\eta*}H^q(\eta_X)\to\cdots$; in particular $H^0(X_{Zar},\mathcal H^q_{\mathbb Q})\subset H^q(\eta_X)$.
* **(I10)** Verdier [Ve]: for a morphism $f\colon X\to S$ of complex varieties and a closed subvariety $\Sigma\subset X$, there is a dense Zariski open $S_1\subset S$ over which $f$ is topologically locally trivial relative to $\Sigma$.
* **(I11)** Deligne's global invariant cycle theorem [D2, Thm. 4.1.1]: if $f\colon X\to C$ is a morphism from a smooth projective $X$ and $f$ is smooth over the Zariski open $C_1$, then $H^k(X,\mathbb Q)\to H^0(C_1,R^kf_*\mathbb Q)$ is surjective.
* **(I12)** Voisin [V02] (as stated in `docs/01`, §1.3): there is a complex torus $T$ of dimension 4 with $\mathrm{Hdg}^2(T)\neq0$ such that (V1) no nonzero class of $\mathrm{Hdg}^2(T)$ is a $\mathbb Q$-linear combination of Chern classes ($c_2$, $c_1^2$) of coherent analytic sheaves, and (V2) $T$ has no analytic subvarieties of dimension 1, 2 or 3. This follows from (V1) together with $NS(T)=0$ and simplicity of $T$ (to be confirmed in [V02]). $NS(T)=0$ excludes divisors. A curve would generate an abelian subvariety of the simple non-algebraic $T$. A surface $S$ would give $c_2(\mathcal O_S)=-[S]\ne0$ in $\mathrm{Hdg}^2(T)$, contradicting (V1).
* **(I13)** Kollár [Ko] (as stated in `docs/01`, §1.3): for a very general hypersurface $X\subset\mathbb P^4$ of degree $d$ with $p^3\mid d$ ($p$ prime), every curve on $X$ has degree divisible by $p$.
* **(I14)** Lefschetz hyperplane theorem: for a smooth hypersurface $X\subset\mathbb P^4$, $H^4(X,\mathbb Z)\cong\mathbb Z$, generated by a class $\ell$ with $\int_X\ell\cup h=1$.

## 2. The analytic degree-4 exponential sequence and its two collapses

On a complex manifold $M$ put $\Omega^{<2}:=[\mathcal O_M\xrightarrow d\Omega^1_M]$ (degrees 0, 1) and $\mathbb Z(2)_{\mathcal D}:=[\mathbb Z(2)\to\mathcal O_M\xrightarrow d\Omega^1_M]$ (degrees 0, 1, 2), and set $H^k_{\mathcal D}(M,\mathbb Z(2))=\mathbb H^k(M,\mathbb Z(2)_{\mathcal D})$. By definition $\mathbb Z(2)_{\mathcal D}=\mathrm{Cone}(\mathbb Z(2)\to\Omega^{<2})[-1]$, so there is a distinguished triangle, natural in $M$:
$$\mathbb Z(2)_{\mathcal D}\longrightarrow\mathbb Z(2)\longrightarrow\Omega^{<2}\xrightarrow{+1}.\tag{2.0}$$

**Proposition 2.1 (the degree-4 "exponential" complex).** Let $M$ be a complex manifold.

(a) $\mathbb Z(2)_{\mathcal D}$ is quasi-isomorphic to the complex $[\mathcal O_M^*\xrightarrow{d\log}\Omega^1_M]$ placed in degrees 1 and 2. Hence $H^k_{\mathcal D}(M,\mathbb Z(2))\cong\mathbb H^{k-1}(M,\mathcal O^*\xrightarrow{d\log}\Omega^1)$.

(b) The cohomology sheaves of $\mathbb Z(2)_{\mathcal D}$ are $\mathcal H^1\cong\mathbb C^*$ (locally constant), $\mathcal H^2\cong\Omega^2_{M,cl}$ (closed holomorphic 2-forms), and $\mathcal H^i=0$ otherwise. Hence there is a triangle $\mathbb C^*[-1]\to\mathbb Z(2)_{\mathcal D}\to\Omega^2_{cl}[-2]\xrightarrow{+1}$ and an exact sequence
$$H^3(M,\mathbb C^*)\to H^4_{\mathcal D}(M,\mathbb Z(2))\to H^2(M,\Omega^2_{cl})\to H^4(M,\mathbb C^*).$$
If $M$ is compact Kähler, $H^2(M,\Omega^2_{cl})\cong F^2H^4(M,\mathbb C)$.

*Proof.* (a) Define a morphism of complexes by $0$ on $\mathbb Z(2)$, by $f\mapsto\exp(f/2\pi i)$ from $\mathcal O$ to $\mathcal O^*$, and by $\omega\mapsto\omega/2\pi i$ on $\Omega^1$. It commutes with the differentials because $d\log\exp(f/2\pi i)=df/2\pi i$ and $\exp((2\pi i)^2m/2\pi i)=1$. On cohomology sheaves: in degree 0 both sides are $0$, since $\mathbb Z(2)\to\mathcal O$ is injective. In degree 1 the map is $\mathbb C/\mathbb Z(2)\to\ker(d\log)=\mathbb C^*$, $z\mapsto\exp(z/2\pi i)$, which is bijective. In degree 2 it is the map $\Omega^1/d\mathcal O\to\Omega^1/d\log\mathcal O^*$ induced by $\omega\mapsto\omega/2\pi i$. It is bijective because on a ball every unit is the exponential of a function, so $d\log\mathcal O^*=d\mathcal O$ as subsheaves of $\Omega^1$, and this subsheaf is stable under division by $2\pi i$.

(b) The computation in (a) gives $\mathcal H^1\cong\mathbb C^*$ and $\mathcal H^2=\Omega^1/d\mathcal O$. By the holomorphic Poincaré lemma, $d\colon\Omega^1/d\mathcal O\to\Omega^2_{cl}$ is an isomorphism of sheaves: it is injective by exactness of $\mathcal O\to\Omega^1\to\Omega^2$, and surjective because closed 2-forms are locally exact. The triangle is the canonical truncation $\tau_{\le1}\to\mathrm{id}\to\tau_{\ge2}$, and the sequence is its long exact sequence. In the Kähler case, $\Omega^2_{cl}\simeq\Omega^{\ge2}[2]$ by the Poincaré lemma, and $\mathbb H^4(M,\Omega^{\ge2})=F^2H^4(M,\mathbb C)$ by degeneration of the Hodge–de Rham spectral sequence. $\square$

So the degree-4 analogue of the sheaf $\mathcal O^*$ is not a sheaf. It is a two-step complex whose cohomology sheaves are the *constant* sheaf $\mathbb C^*$ and the sheaf $\Omega^2_{cl}$. (Brylinski–McLaughlin [BM] interpret classes in $\mathbb H^3(\mathcal O^*\to\Omega^1)$ as holomorphic 2-gerbes with connective structure. Nothing below uses this interpretation.)

**Proposition 2.2 (analytic degree-4 Lefschetz theorem; known).** Let $M$ be compact Kähler.

(a) [I6] Every $\alpha\in\mathrm{Hdg}^2_{\mathbb Z}(M)$ lifts to $\tilde\alpha\in H^4_{\mathcal D}(M,\mathbb Z(2))=\mathbb H^3(M,\mathcal O^*\to\Omega^1)$. The lifts form a torsor under $J^2(M)$.

(b) The exponential sequence $0\to\mathbb Z(1)\to\mathcal O\to\mathcal O^*\to0$ gives an exact sequence $H^3(M,\mathcal O^*)\to H^4(M,\mathbb Z(1))\to H^4(M,\mathcal O)$. Its last map is $\alpha\mapsto\alpha^{0,4}$, so the image of $H^3(M,\mathcal O^*)$ is $\{\alpha:\alpha^{0,4}=0\}$, which contains every integral Hodge class.

*Proof.* (a) is (I6). (b) is the exponential sequence together with the Hodge decomposition, which identifies $H^4(M,\mathbb Z)\to H^4(M,\mathcal O)\cong H^{0,4}$ with the projection. $\square$

Thus (E1) holds in degree 4 on every compact Kähler manifold, Voisin's tori included. Note that (b) alone only sees the $(0,4)$-part; the connective structure (the $\Omega^1$ term) is what cuts the image down to the $(2,2)$-classes.

**Lemma 2.3 (Zariski collapse).** Let $X$ be a smooth irreducible complex variety.

(a) $H^i(X_{Zar},A)=0$ for $i\ge1$ and every constant sheaf $A$.

(b) $H^i(X_{Zar},\mathcal O_X^*)=0$ for $i\ge2$.

(c) $H^i(X_{Zar},\mathcal K_2)=0$ for $i\ge3$, and $H^2(X_{Zar},\mathcal K_2)=CH^2(X)$.

Consequently the Zariski counterparts of the terms $H^3(\mathcal O^*)\to H^4(\mathbb Z)$ of Proposition 2.2(b), and of any degree-4 sequence built from $\mathcal O^*$ or $\mathcal K_2$ in the same pattern, are identically zero. A Zariski-sheaf description of the cycle class map to $H^4(X,\mathbb Q)$ must therefore pass through $R\varepsilon_*$, where $\varepsilon\colon X^{an}\to X_{Zar}$, that is, through the Bloch–Ogus sheaves $\mathcal H^q=R^q\varepsilon_*\mathbb Q$.

*Proof.* (a) Every nonempty open subset of the irreducible space $X$ is irreducible, hence connected, so the constant sheaf has sections $A$ on every nonempty open, with identity restriction maps. It is therefore flasque, hence acyclic. (b) $X$ is locally factorial, so $0\to\mathcal O^*\to\mathcal K_X^*\to\bigoplus_{x\in X^{(1)}}i_{x*}\mathbb Z\to0$ is exact (Cartier divisors are Weil divisors). The middle sheaf is constant, hence flasque by (a), and the right-hand sheaf is a direct sum of flasque skyscraper-type sheaves on a noetherian space, hence flasque. So $\mathcal O^*$ has a flasque resolution of length 1. (c) The Gersten resolution (I8) of $\mathcal K_2$ is a flasque resolution of length 2, and its $H^2$ is $\mathrm{coker}(\bigoplus_{X^{(1)}}\kappa(x)^*\xrightarrow{\mathrm{div}}\bigoplus_{X^{(2)}}\mathbb Z)=CH^2(X)$. $\square$

**Lemma 2.4 (Stein collapse).** Let $U$ be a smooth affine complex variety.

(a) The map $H^k_{\mathcal D}(U^{an},\mathbb Z(2))\to H^k(U^{an},\mathbb Z(2))$ from (2.0) is an isomorphism for $k\ge3$.

(b) The connecting map $H^k(U^{an},\mathcal O^*)\to H^{k+1}(U^{an},\mathbb Z(1))$ is an isomorphism for $k\ge1$.

(c) Let $X\supset U$ be smooth projective. Let $\tilde\alpha\in H^4_{\mathcal D}(X,\mathbb Z(2))$ with image $\alpha\in H^4(X,\mathbb Z(2))$, and $g\in H^3(X^{an},\mathcal O^*)$ with image $\alpha'\in H^4(X,\mathbb Z(1))$. Then $\tilde\alpha|_U=0\iff\alpha|_U=0$ and $g|_U=0\iff\alpha'|_U=0$. The same holds after multiplying by any integer $N$.

*Proof.* By (I7), $\mathcal O$ and $\Omega^1$ are acyclic on $U^{an}$. Hence $\mathbb H^k(U^{an},\Omega^{<2})$ is the cohomology of the two-term complex $\mathcal O(U^{an})\to\Omega^1(U^{an})$, which vanishes for $k\ge2$, and $H^k(U^{an},\mathcal O)=0$ for $k\ge1$. Now (a) follows from the long exact sequence of (2.0), since $\mathbb H^{k-1}(\Omega^{<2})=\mathbb H^k(\Omega^{<2})=0$ for $k\ge3$; and (b) follows from the exponential sequence. (c) The triangle (2.0) and the exponential sequence are natural for the restriction $U\hookrightarrow X$, so the restriction of $\tilde\alpha$ (resp. $g$) to $U$ maps to $\alpha|_U$ (resp. $\alpha'|_U$) under the isomorphism (a) (resp. (b)). $\square$

**Comment.** Two lifts of $\alpha$ differ by an element of $J^2(X)$, and Lemma 2.4 shows that this difference dies on every affine open set. Neither the connective structure nor the intermediate Jacobian survives Zariski-localization: the only Zariski-local information carried by a degree-4 "exponential" object is its Betti class. This is the first half of the failure of (E2) in degree 4. In degree 2 the same computation gives $H^1(U^{an},\mathcal O^*)\cong H^2(U^{an},\mathbb Z(1))$ for $U$ affine, and (E2) is rescued by GAGA, which makes the line bundle algebraic and hence Zariski-locally trivial (Proposition 3.2). For 2-gerbes or Deligne classes there is no such GAGA, because the objects are not coherent.

## 3. Rung (a): the obstruction group

**Proposition 3.1 ((E3) with rational coefficients; classical).** Let $X$ be smooth projective, $\alpha\in\mathrm{Hdg}^2(X)$, and $D\subsetneq X$ closed with $\alpha|_{X\setminus D}=0$ in $H^4(X\setminus D,\mathbb Q)$. Then $\alpha\in A^2(X)$.

*Proof.* Enlarging $D$ only shrinks $X\setminus D$, so we may assume $D$ is a divisor. Take $\mu\colon X'\to X$ as in (I5), with $D'=\mu^{-1}(D)_{red}=\bigcup_{i=1}^rD'_i$ SNC and $\mu\colon X'\setminus D'\xrightarrow\sim X\setminus D$. Then $\mu^*\alpha\in\mathrm{Hdg}^2(X')$ and $(\mu^*\alpha)|_{X'\setminus D'}=(\mu|_{X'\setminus D'})^*(\alpha|_{X\setminus D})=0$. By (I4), $\mu^*\alpha$ lies in the image of
$$\Gamma=\textstyle\sum_i\gamma_{i*}\colon V:=\bigoplus_iH^2(D'_i,\mathbb Q)(-1)\longrightarrow H^4(X',\mathbb Q),$$
a morphism of polarizable Hodge structures of weight 4. By (I1), $\mu^*\alpha=\Gamma(\beta)$ with $\beta=(\beta_i)$ a Hodge class of $V$, so each $\beta_i\in H^2(D'_i,\mathbb Q)$ has type $(1,1)$. By (I2) applied to the smooth projective $D'_i$, $\beta_i=\mathrm{cl}(B_i)$ for a $\mathbb Q$-divisor $B_i$ on $D'_i$. Since the cycle class commutes with proper push-forward, $\mu^*\alpha=\mathrm{cl}(\sum_i\gamma_{i*}B_i)\in A^2(X')$. Finally $\mu_*\mu^*\alpha=\alpha\cup\mu_*1=\alpha$, and $\mu_*$ maps algebraic classes to algebraic classes, so $\alpha\in A^2(X)$. $\square$

This is the step used in Bloch–Srinivas [BS] for the part of the diagonal supported on $D\times X$. The rational coefficients are used three times: the $E_2$-degeneration in (I4), the splitting in (I1), and the $\mathbb Q$-divisors in (I2). Theorem C(iii) shows the integral statement is false.

**Theorem A (the obstruction group).** Let $X$ be smooth projective of dimension $n\ge2$.

(i) $\mathrm{Hdg}^2(X)\cap\ker(\mathrm{ob})=A^2(X)$; that is, $\mathrm{Hdg}^2(X)\cap N^1H^4(X,\mathbb Q)=A^2(X)$.

(ii) $\mathrm{ob}(\mathrm{Hdg}^2(X))=\mathrm{Hdg}(\eta_X)$. Hence $\mathrm{ob}$ induces an isomorphism
$$\mathrm{Ob}(X):=\mathrm{Hdg}^2(X)/A^2(X)\;\xrightarrow{\ \sim\ }\;\mathrm{Hdg}(\eta_X).$$

(iii) $\mathrm{ob}(H^4(X,\mathbb Q))\subset H^0(X_{Zar},\mathcal H^4_{\mathbb Q})\subset H^4(\eta_X)$.

Consequently there is an exact sequence (the "$K_2$-exponential sequence")
$$H^2(X_{Zar},\mathcal K_2)\otimes\mathbb Q\xrightarrow{\ \mathrm{cl}\ }\mathrm{Hdg}^2(X)\xrightarrow{\ \mathrm{ob}\ }\mathrm{Hdg}(\eta_X)\to0,$$
and $\mathrm{HC}(X,2)\iff\mathrm{Hdg}(\eta_X)=0\iff$ every degree-4 Hodge class vanishes on some nonempty Zariski open set. In particular $\mathrm{HC}(X,2)$ holds if $N^1H^4(X,\mathbb Q)=H^4(X,\mathbb Q)$, for instance if $H^0(X_{Zar},\mathcal H^4_{\mathbb Q})=0$.

*Proof.* (i) If $\alpha=\mathrm{cl}(\sum_jn_jZ_j)$ with the $Z_j$ of codimension 2, then $\mathrm{cl}(Z_j)$ is the image of a class in $H^4_{Z_j}(X)$, so it restricts to $0$ on $X\setminus\bigcup_jZ_j$; hence $\mathrm{ob}(\alpha)=0$. Conversely, if $\mathrm{ob}(\alpha)=0$, then by definition of the colimit $\alpha|_U=0$ for some $U$, and Proposition 3.1 applies.

(ii) Restriction maps are morphisms of MHS, so $\mathrm{ob}(\mathrm{Hdg}^2(X))\subset\mathrm{Hdg}(\eta_X)$. Conversely let $\phi\colon\mathbb Q(-2)\to H^4(U)$ be a morphism of MHS and $x=\phi(1)$. Since $\mathbb Q(-2)$ is pure of weight 4 and morphisms are strict for $W$, $x\in W_4H^4(U)$. By (I3), applied with $\bar U=X$, $W_4H^4(U)$ is the image of the restriction $\rho\colon H^4(X,\mathbb Q)\to H^4(U)$, and it is pure of weight 4 (weights of $H^4(U)$ are $\ge4$) and polarizable as a quotient of $H^4(X)$ (I1). Since $x$ is rational and lies in $F^2$ of a pure weight-4 structure, it has type $(2,2)$. By (I1) there is $\alpha\in\mathrm{Hdg}^2(X)$ with $\rho(\alpha)=x$, so the germ of $x$ equals $\mathrm{ob}(\alpha)$. Combined with (i), this gives the isomorphism.

(iii) The compatible family $(\alpha|_U)_U$ is a global section of the presheaf $U\mapsto H^4(U)$, hence of its sheafification $\mathcal H^4_{\mathbb Q}$, and its germ at the generic point is $\mathrm{ob}(\alpha)$. By (I9) the germ map $H^0(X,\mathcal H^4_{\mathbb Q})\to H^4(\eta_X)$ is injective.

The exact sequence follows from (i), (ii) and Bloch–Quillen (I8). The remaining statements are immediate, since $N^1H^4=\ker\mathrm{ob}$. $\square$

*Status.* Known in substance; it is the classical reduction "Hodge classes of coniveau $\ge1$ are algebraic". I do not know the first reference for the generic-point form (ii); compare Bloch–Ogus [BO] and Jannsen [Ja]. The proof is included so the rest of the file is self-contained.

**Corollary A.1 (birational invariance).** If $X$ and $X'$ are birational smooth projective varieties, then $\mathrm{Hdg}^2(X)/A^2(X)\cong\mathrm{Hdg}^2(X')/A^2(X')$. In particular $\mathrm{HC}(X,2)\iff\mathrm{HC}(X',2)$.

*Proof.* Choose nonempty opens $V\subset X$, $V'\subset X'$ and an isomorphism $\psi\colon V\xrightarrow\sim V'$. Since $X$ is irreducible, the opens contained in $V$ are cofinal, and similarly for $V'$. The isomorphism $\psi$ induces MHS isomorphisms $H^4(\psi(U))\cong H^4(U)$, compatible with restrictions, so $\mathrm{Hdg}(\eta_X)\cong\mathrm{Hdg}(\eta_{X'})$. Now apply Theorem A(ii). $\square$

(Folklore; it also follows from weak factorization and the blow-up formula.)

**Corollary A.2 (why the first open case is $n=4$).** If $\dim X\le3$, then $H^4(\eta_X)=0$, and so $\mathrm{HC}(X,2)$ holds. This reproves $\mathrm{HC}$ for curves on threefolds without the hard-Lefschetz reduction to divisors. The semisimplicity (I1), whose proof uses polarizations, is still used.

*Proof.* Every nonempty open set contains a nonempty affine open $U$, and $H^4(U)=0$ by (I7), since $\dim U\le3<4$. Now apply Theorem A. $\square$

For $n=4$, an affine $U$ can have $H^4(U)\ne0$, and the obstruction group can in principle be nonzero. Theorem A thus places the first open case $(n,p)=(4,2)$ exactly where Andreotti–Frankel stops forcing $\mathrm{Hdg}(\eta_X)=0$.

**Proposition 3.2 (the same mechanism in degree 2).** Let $X$ be smooth projective and $\mathrm{Hdg}^1(\eta_X):=\varinjlim_U\mathrm{Hom}_{MHS}(\mathbb Q(-1),H^2(U))$.

(a) $\mathrm{Hdg}^1(X)/A^1(X)\cong\mathrm{Hdg}^1(\eta_X)$.

(b) The exponential sequence and GAGA give $\mathrm{Hdg}^1(\eta_X)=0$, which by (a) is Lefschetz (1,1) with $\mathbb Q$-coefficients.

*Proof.* (a) The proof of Theorem A applies verbatim, with Proposition 3.1 replaced by the following statement: on an SNC model, $\ker(H^2(X')\to H^2(X'\setminus D'))=\sum_i\gamma_{i*}H^0(D'_i)$ is spanned by the classes $[D'_i]$ (I4), hence is algebraic, and one pushes forward by $\mu_*$. No Lefschetz (1,1) is needed here. (b) Let $\alpha\in\mathrm{Hdg}^1_{\mathbb Z}(X)$. By the exponential sequence $\alpha=c_1(L)$ for a holomorphic line bundle $L$. By GAGA $L$ is algebraic, so it is trivial on some nonempty Zariski open $U$, and $\alpha|_U=c_1(L|_U)=0$. Every rational Hodge class has a multiple in $\mathrm{Hdg}^1_{\mathbb Z}$. $\square$

Proposition 3.2 shows *what* the exponential sequence contributes in Lefschetz's theorem: Zariski-local triviality at the generic point, which is (E2). The degree-4 analogue of that contribution is the next statement.

**Theorem B (degree-4 GAGA is equivalent to $\mathrm{HC}(X,2)$).** For $X$ smooth projective the following are equivalent.

(a) $\mathrm{HC}(X,2)$.

(b) ($\mathrm{GAGA}_4$ for Deligne classes) For every $\alpha\in\mathrm{Hdg}^2_{\mathbb Z}(X)$ and every lift $\tilde\alpha\in H^4_{\mathcal D}(X,\mathbb Z(2))$ there are $N\ge1$ and a nonempty Zariski open $U$ with $N\tilde\alpha|_{U^{an}}=0$.

(c) The same as (b), with "every lift" replaced by "some lift".

(d) ($\mathrm{GAGA}_4$ for 2-gerbes) For every $\alpha\in\mathrm{Hdg}^2_{\mathbb Z}(X)$ and every $g\in H^3(X^{an},\mathcal O^*)$ mapping to $\alpha$ (we identify $\mathbb Z(1)\cong\mathbb Z(2)$ by multiplication by $2\pi i$; such $g$ exist by Prop. 2.2(b)), there are $N\ge1$ and a nonempty Zariski open $U$ with $Ng|_{U^{an}}=0$.

*Proof.* Affine opens are cofinal. By Lemma 2.4(c), each of the conditions in (b), (c), (d) holds for $\alpha$ iff there are $N\ge1$ and $U$ with $N\alpha|_U=0$ in $H^4(U^{an},\mathbb Z)$. Because $H^4(U^{an},\mathbb Z)$ is finitely generated (I7), this holds iff $\alpha_{\mathbb Q}|_U=0$, that is, iff $\mathrm{ob}(\alpha_{\mathbb Q})=0$. By Theorem A(i), that is equivalent to $\alpha_{\mathbb Q}\in A^2(X)$. Every class in $\mathrm{Hdg}^2(X)$ has a nonzero integer multiple that is the image of an element of $\mathrm{Hdg}^2_{\mathbb Z}(X)$, so the conditions hold for all $\alpha$ iff $\mathrm{HC}(X,2)$ holds. $\square$

*Status.* An elementary reformulation of Theorem A(i) via Lemma 2.4. $\mathrm{GAGA}_4$ is by definition the statement that every Hodge class vanishes rationally on a nonempty Zariski open set. Its point is negative: the transcendental data used by the "$K_2$-exponential" construction (the lift $\tilde\alpha$ or $g$) can be chosen freely, but no choice helps, because whether the construction succeeds depends only on the Betti class at the generic point.

**Remark 3.3 (what the "$K_2$-torsor" is).** Under Bloch–Quillen (I8), the class produced in Proposition 3.1 is $\mu_*\sum_i\gamma_{i*}[B_i]\in H^2(X_{Zar},\mathcal K_2)_{\mathbb Q}$, where $[B_i]\in CH^1(D'_i)=H^1(D'_{i,Zar},\mathcal O^*)$ is given by the *degree-2* exponential sequence on $D'_i$ via (I2). So the "$K_2$-exponential map" exists, but only after the class has been localized on a divisor; producing the divisor is the obstruction $\mathrm{Ob}(X)$.

**Remark 3.4 (kernel-side phenomena are not the obstruction).** Griffiths (the Abel–Jacobi image is not all of $J^2$, and $J^2$ is not algebraic), Mumford (infinite-dimensionality of $CH_0$) and Nori (Griffiths groups) describe $\ker(CH^2\to\mathrm{Hdg}^2)$ and the $J^2$-part of $H^4_{\mathcal D}$. By Lemma 2.4 and Theorem A neither enters $\mathrm{Ob}(X)$. These results show that $CH^2$ has no Picard-variety-like structure, which is not what $\mathrm{HC}$ requires.

## 4. Rung (b): sufficient conditions on fourfolds

The ladder asks for $\mathrm{HC}(X,2)$ for fourfolds under a cohomological vanishing, if the obstruction analysis allows one. By Theorem A the obstruction is $\mathrm{ob}(\mathrm{Hdg}^2(X))$, so what is needed is a *coniveau* statement. The first result shows the coherent vanishing hypotheses suggested in the ladder cannot work as stated. The second gives a coniveau-type sufficient condition that can be checked fibrewise.

**Proposition E (what coherent vanishing can and cannot do).** Let $X$ be a smooth projective fourfold.

(a) $h^{2,2}(X)\ge1$, so the hypothesis "$H^2(X,\Omega^2_X)=0$" never holds.

(b) If $h^{4,0}(X)=h^{3,1}(X)=0$, then $\mathrm{Hdg}^2(X)=H^4(X,\mathbb Q)$, and $\mathrm{HC}(X,2)\iff N^1H^4(X,\mathbb Q)=H^4(X,\mathbb Q)$. This is the coniveau-1 case of Grothendieck's generalized Hodge conjecture for $H^4(X)$.

(c) $N^1H^4(X,\mathbb Q)\otimes\mathbb C\subset H^{3,1}\oplus H^{2,2}\oplus H^{1,3}$. Hence if $h^{4,0}(X)\ne0$, then $\mathrm{ob}\ne0$ on $H^4(X,\mathbb Q)$ and $H^0(X_{Zar},\mathcal H^4_{\mathbb Q})\ne0$, so the sufficient condition in Theorem A cannot be used and one must work with Hodge classes only.

*Proof.* (a) For an ample class $h$, $h^2\in H^{2,2}$ and $\int_Xh^4>0$, so $h^2\ne0$. (b) By Hodge symmetry $H^4(X,\mathbb C)=H^{2,2}$, so every rational class is a Hodge class; then apply Theorem A(i). (c) Let $x\in H^4(X,\mathbb Q)$ vanish on $X\setminus D$. By the proof of Proposition 3.1 without the last two steps, $\mu^*x=\Gamma(\beta)$ with $\beta\in\bigoplus_iH^2(D'_i)(-1)$, whose Hodge types $(p,q)$ have $p,q\ge1$, and $x=\mu_*\mu^*x$. Both $\Gamma$ and $\mu_*\colon H^4(X')\to H^4(X)$ are morphisms of Hodge structures, so $x$ has no $(4,0)$- or $(0,4)$-component. If $h^{4,0}(X)\ne0$, then $H^4(X,\mathbb C)$ has a $(4,0)$-part, so $N^1H^4\ne H^4$, i.e. $\mathrm{ob}\ne0$ on $H^4(X,\mathbb Q)$. By Theorem A(iii), $H^0(X_{Zar},\mathcal H^4_{\mathbb Q})\ne0$. $\square$

So for fourfolds the natural analogue of "$p_g=0$" (which for surfaces forces $H^2=NS_{\mathbb Q}$, by Lefschetz (1,1)) is $h^{4,0}=h^{3,1}=0$. Under it, $\mathrm{HC}(X,2)$ is *equivalent* to a coniveau statement that I cannot prove (GAPS, G2). The groups $H^3(X,\mathcal O_X)$, $H^2(X,\Omega^1_X)$, i.e. $J^2(X)$, do not enter $\mathrm{Ob}(X)$ at all (Lemma 2.4).

**Theorem D (fibration criterion).** Let $X$ be a smooth projective fourfold and $f\colon X\to C$ a surjective morphism onto a smooth projective curve. For $t\in C$ put $Y_t=f^{-1}(t)$. Assume:

> **(H)** there are a closed algebraic subset $\Sigma\subsetneq X$ and a nonempty Zariski open $C_0\subset C$ over which $f$ is smooth, such that for every $t\in C_0$ the restriction map $H^3(Y_t,\mathbb Q)\to H^3(Y_t\setminus\Sigma,\mathbb Q)$ is zero.

Then $\mathrm{HC}(X,2)$ holds.

*Proof.* Fix $\alpha\in\mathrm{Hdg}^2(X)$ and an ample divisor $H$ with class $h$.

*Step 0 (local triviality).* By (I10), choose a nonempty Zariski open $C_1\subset C_0$, $C_1\ne C$, over which $f$ is topologically locally trivial relative to $\Sigma$. Put $X_1=f^{-1}(C_1)$, $f_1=f|_{X_1}$, $U_1=X_1\setminus\Sigma$, $g=f|_{U_1}$. $U_1$ is a nonempty Zariski open subset of $X$: otherwise $\Sigma\supset X_1$, which is dense, so $\Sigma=X$. Over a small disc $V\ni t$ the pair $(f^{-1}V,\Sigma\cap f^{-1}V)$ is homeomorphic over $V$ to $V\times(Y_t,\Sigma\cap Y_t)$. Hence $R^qf_{1*}\mathbb Q$ and $R^qg_*\mathbb Q$ are local systems with stalks $H^q(Y_t)$ and $H^q(Y_t\setminus\Sigma)$, and the map $\rho^q\colon R^qf_{1*}\mathbb Q\to R^qg_*\mathbb Q$ induced by restriction is, on stalks, the restriction map. By (H), $\rho^3=0$. Since $C_1$ is a compact Riemann surface minus a nonempty finite set, it is homotopy equivalent to a finite graph, so $H^p(C_1,\mathbb L)=0$ for $p\ge2$ and every local system $\mathbb L$.

*Step 1 (removing the fibrewise part).* By hard Lefschetz on the smooth projective threefolds $Y_t$, cup product with $h_t=h|_{Y_t}$ is an isomorphism of local systems $L\colon R^2f_{1*}\mathbb Q\to R^4f_{1*}\mathbb Q$, and an isomorphism of Hodge structures $H^2(Y_t)(-1)\to H^4(Y_t)$ on each fibre. The section $s(t)=\alpha|_{Y_t}$ of $R^4f_{1*}\mathbb Q$ is flat, being the image of $\alpha$, so $\delta:=L^{-1}(s)\in H^0(C_1,R^2f_{1*}\mathbb Q)$, and $\delta_t\in H^2(Y_t,\mathbb Q)$ has type $(1,1)$. Fix $t_0\in C_1$. By (I11), $H^2(X,\mathbb Q)\to H^2(Y_{t_0},\mathbb Q)$ is a morphism of Hodge structures whose image contains $\delta_{t_0}$. By (I1) there is $\beta\in\mathrm{Hdg}^1(X)$ with $\beta|_{Y_{t_0}}=\delta_{t_0}$. Both $t\mapsto\beta|_{Y_t}$ and $\delta$ are flat sections, they agree at $t_0$, and $C_1$ is connected; so $\beta|_{Y_t}=\delta_t$ for all $t\in C_1$. By (I2), $\beta=\mathrm{cl}(B)$ for a $\mathbb Q$-divisor $B$. Put $Z_0=B\cdot H\in CH^2(X)_{\mathbb Q}$, so $\mathrm{cl}(Z_0)=\beta\cup h$ and $\mathrm{cl}(Z_0)|_{Y_t}=L_t(\delta_t)=\alpha|_{Y_t}$. Hence $\alpha':=\alpha-\mathrm{cl}(Z_0)\in\mathrm{Hdg}^2(X)$ satisfies $\alpha'|_{Y_t}=0$ for all $t\in C_1$.

*Step 2 (Leray).* The Leray spectral sequences $E_2^{p,q}=H^p(C_1,R^qf_{1*}\mathbb Q)\Rightarrow H^{p+q}(X_1)$ and $E_2^{p,q}=H^p(C_1,R^qg_*\mathbb Q)\Rightarrow H^{p+q}(U_1)$ have only the columns $p=0,1$ (Step 0). They therefore degenerate at $E_2$ and give natural exact sequences
$$0\to H^1(C_1,R^3f_{1*}\mathbb Q)\to H^4(X_1)\to H^0(C_1,R^4f_{1*}\mathbb Q)\to0,$$
and similarly for $g$. The restriction $H^4(X_1)\to H^4(U_1)$ is induced by the morphism $Rf_{1*}\mathbb Q\to Rf_{1*}Rj_*\mathbb Q=Rg_*\mathbb Q$ in $D^b(C_1)$, with $j\colon U_1\hookrightarrow X_1$. A morphism in the derived category induces a morphism of the Leray (canonical-filtration) spectral sequences. So the restriction maps the left-hand term $H^1(C_1,R^3f_{1*}\mathbb Q)$ to $H^1(C_1,R^3g_*\mathbb Q)$ by $H^1(\rho^3)=0$. By Step 1, the image of $\alpha'|_{X_1}$ in $H^0(C_1,R^4f_{1*}\mathbb Q)$ is $t\mapsto\alpha'|_{Y_t}=0$, so $\alpha'|_{X_1}$ lies in the left-hand term. Hence $\alpha'|_{U_1}=0$.

*Step 3.* $\alpha'$ is a Hodge class vanishing on the nonempty Zariski open set $U_1$. By Proposition 3.1, $\alpha'\in A^2(X)$, so $\alpha=\alpha'+\mathrm{cl}(Z_0)\in A^2(X)$. $\square$

**Corollary D.1 (after base change).** Let $X$ be a smooth projective fourfold with a surjective morphism $f\colon X\to C$ onto a smooth projective curve. Suppose there are a finite surjective morphism $C'\to C$ from a smooth projective curve and a resolution $X'$ of an irreducible component of $X\times_CC'$ dominating $X$ such that $X'\to C'$ satisfies (H). Then $\mathrm{HC}(X,2)$ holds.

*Proof.* $\pi\colon X'\to X$ is generically finite and surjective, of some degree $d\ge1$. For $\alpha\in\mathrm{Hdg}^2(X)$, $\pi^*\alpha\in\mathrm{Hdg}^2(X')$ is algebraic by Theorem D ($X'\to C'$ is surjective and generically smooth). Then $\alpha=d^{-1}\pi_*\pi^*\alpha$ by the projection formula, and this is algebraic. $\square$

**Remarks on Theorem D.**

1. If $H^3(Y_t,\mathbb Q)=0$ for general $t$, then (H) holds with $\Sigma=\emptyset$. Example: fibrations whose fibres are $S_t\times\mathbb P^1$ with $S_t$ K3 surfaces. Such $X$ can have infinite-dimensional $CH_0$, so [BS] does not apply directly; but in the examples I know, product or projective-bundle arguments also give $\mathrm{HC}(X,2)$ (G4).
2. (H) forces $h^{3,0}(Y_t)=0$, and hence $h^{4,0}(X)=0$: because $f_*\omega_{X/C}=0$, $H^0(K_X)=H^0(C,f_*\omega_{X/C}\otimes\omega_C)=0$. Theorem D does not reach fourfolds with $p_g>0$.
3. Theorem D is a coniveau version of the Griffiths–Zucker mechanism. The normal function of $\alpha'$ lives in the $H^1(C_1,R^3f_*)$-term, and (H) says the fibre intermediate Jacobians are "uniformly of coniveau 1". In Zucker's proof for cubic fourfolds [Z], the fibres of a Lefschetz pencil are cubic threefolds, whose $H^3$ is supported on the surface swept out by the lines meeting a fixed line (Clemens–Griffiths [CG]). With Corollary D.1, to choose that line in families, and with the blow-up of the base locus, this should recover Zucker's theorem. I have not written out the verification of (H) in that case, and I do not claim it.
4. The hypothesis is uniform in $t$. Deducing it from the pointwise statement "$H^3(Y_t,\mathbb Q)=N^1H^3(Y_t,\mathbb Q)$ for very general $t$" requires a countability-of-Hilbert-schemes and constructibility argument, plus a finite base change. I expect this to be routine but have not written it, so it is listed as G3.

## 5. Rung (c): why no Lefschetz-type sheaf sequence proves $\mathrm{HC}$ in degree 4

The literal claim "no exact sequence of Lefschetz type exists in degree 4" is not a well-posed statement. A cokernel sequence $CH^2_{\mathbb Q}\to\mathrm{Hdg}^2\to\mathrm{Hdg}^2/A^2\to0$ exists for every $X$, and Theorem A identifies its third term with $\mathrm{Hdg}(\eta_X)$; only in that weak sense is Theorem A such a sequence, $CH^2_{\mathbb Q}\to\mathrm{Hdg}^2\to\mathrm{Hdg}(\eta_X)\to0$, and Proposition 2.2 is an exact analytic sequence of sheaf cohomology groups. Nor can one prove that the third term is nonzero for some $X$, unless $\mathrm{HC}(\cdot,2)$ is false: by Theorems A and B, its vanishing for all $X$ *is* $\mathrm{HC}(\cdot,2)$. What can be proved is the following list. It says which steps of the Lefschetz argument survive in degree 4, and which fail, and where.

**Theorem C.**

(i) *(E1) holds on all compact Kähler manifolds.* For every compact Kähler $M$, every $\alpha\in\mathrm{Hdg}^2_{\mathbb Z}(M)$ lifts to $H^4_{\mathcal D}(M,\mathbb Z(2))=\mathbb H^3(M,\mathcal O^*\to\Omega^1)$ and to $H^3(M,\mathcal O^*)$.

(ii) *(E2) fails in the analytic setting.* Let $T$ be the torus of (I12). For every closed analytic subset $A\subsetneq T$, the map $H^4(T,\mathbb Q)\to H^4(T\setminus A,\mathbb Q)$ is injective. Hence, for every nonzero $\alpha\in\mathrm{Hdg}^2(T)$, every $\alpha_{\mathbb Z}\in\mathrm{Hdg}^2_{\mathbb Z}(T)$ with $\alpha_{\mathbb Z}\otimes\mathbb Q=M\alpha$ ($M\ge1$), and every lift $\tilde\alpha$ (or $g$) of $\alpha_{\mathbb Z}$ as in (i), no nonzero multiple of $\tilde\alpha$ (or $g$) vanishes on the complement of a proper analytic subset. The "analytic coniveau" $N^1_{an}H^4(T,\mathbb Q)$ is zero, so the whole of $\mathrm{Hdg}^2(T)\ne0$ is obstruction; by (V1), none of it consists of Chern classes of coherent sheaves.

(iii) *(E3) fails integrally, already for fourfolds.* Let $X\subset\mathbb P^4$ be as in (I13), $\ell$ as in (I14), $U=X\setminus(X\cap\text{hyperplane})$, and $X_4=X\times\mathbb P^1$. Then $\ell\in\mathrm{Hdg}^2_{\mathbb Z}(X)$ and $\mathrm{pr}_1^*\ell\in\mathrm{Hdg}^2_{\mathbb Z}(X_4)$ are integral Hodge classes that vanish on the nonempty Zariski open sets $U$, resp. $U\times\mathbb P^1$, and that are not classes of integral algebraic cycles. Thus the integral versions of Proposition 3.1 and Theorem A(i) are false, and rational coefficients are used essentially exactly there.

(iv) *There is no Zariski-sheaf version.* For smooth irreducible $X$, the Zariski groups $H^{\ge1}(X_{Zar},\mathbb Z)$, $H^{\ge2}(X_{Zar},\mathcal O^*)$ and $H^{\ge3}(X_{Zar},\mathcal K_2)$ vanish (Lemma 2.3). The analytic sequence of Proposition 2.2 therefore has no Zariski counterpart, and comparing the Zariski site with Betti cohomology forces the obstruction into the generic-point group $\mathrm{Hdg}(\eta_X)\subset H^0(X_{Zar},\mathcal H^4_{\mathbb Q})$ (Theorem A).

*Proof.* (i) Proposition 2.2.

(ii) Let $A\subsetneq T$ be closed analytic. Each irreducible component of $A$ has dimension $\le3$: a 4-dimensional component of a closed analytic subset of the connected 4-dimensional manifold $T$ would be all of $T$. By (V2) the components are points, and there are finitely many by compactness. By excision, $H^4_A(T,\mathbb Q)=\bigoplus_{a\in A}H^4(B_a,B_a\setminus a;\mathbb Q)\cong\bigoplus_a\tilde H^3(S^7;\mathbb Q)=0$, where $B_a$ is a coordinate ball. The exact sequence $H^4_A(T)\to H^4(T)\to H^4(T\setminus A)$ gives injectivity. If $N\tilde\alpha|_{T\setminus A}=0$ (or $Ng|_{T\setminus A}=0$), then applying the natural map to $H^4(T\setminus A,\mathbb Z)$ gives $NM\alpha|_{T\setminus A}=0$ in $H^4(T\setminus A,\mathbb Q)$, so $\alpha=0$, a contradiction. $N^1_{an}H^4(T,\mathbb Q):=\bigcup_A\ker(H^4(T)\to H^4(T\setminus A))=0$ by the same computation.

(iii) $H^4(X,\mathbb Q)=\mathbb Q h^2$ by (I14), so $H^4(X,\mathbb C)=H^{2,2}$ and $\ell$ is an integral Hodge class; hence so is $\mathrm{pr}_1^*\ell$. $U$ is a smooth affine threefold, so $H^4(U,\mathbb Z)=0$ by (I7), and so $\ell|_U=0$ and $(\mathrm{pr}_1^*\ell)|_{U\times\mathbb P^1}=\mathrm{pr}_1^*(\ell|_U)=0$. If $\ell=\mathrm{cl}(\sum n_jC_j)$ with integral $n_j$, then $1=\int\ell\cup h=\sum n_j\deg C_j\equiv0\pmod p$ by (I13), which is absurd. Suppose $\mathrm{pr}_1^*\ell=\mathrm{cl}(Z)$ for an integral codimension-2 cycle $Z$ on $X_4$. For a general point $s\in\mathbb P^1$, $Z$ meets $X\times\{s\}$ properly: the components of $Z$ not dominating $\mathbb P^1$ lie over finitely many points. Since the cycle class is compatible with proper intersection, $\ell=i_s^*\mathrm{pr}_1^*\ell=\mathrm{cl}(Z\cdot(X\times\{s\}))$, an integral algebraic class, contradicting the previous sentence.

(iv) Lemma 2.3 and Theorem A(iii). $\square$

*Status.* (i), (iv): known or elementary. (ii), (iii): short deductions, proved here, from Voisin's and Kollár's theorems as quoted in (I12), (I13). The fact that Kollár's classes vanish on an affine open set is implicit in the unramified-cohomology analysis of Colliot-Thélène–Voisin [CTV]; I do not claim it as new.

**Where projectivity must enter.** (E1) holds for compact Kähler manifolds (C(i)). The algebraization step (E3) is pure Hodge theory plus Lefschetz (1,1) on a resolution of a hypersurface. Its Kähler analogue would at best produce Chern classes of coherent sheaves, and on $T$ it is vacuous, because $T$ has no hypersurfaces. What fails on $T$ is (E2), for every nonzero Hodge class (C(ii)). Therefore any proof of $\mathrm{HC}(X,2)$ along this route must contain a proof of $\mathrm{GAGA}_4$ that uses a property of projective varieties failing on $T$. Concretely, it must produce from $\alpha$ a hypersurface $D$ with $\alpha|_{X\setminus D}=0$. The known ways of doing this use projectivity explicitly: [BS], through algebraic families of points and the decomposition of the diagonal; Theorem D, through a morphism to a curve, a rational ample class and Deligne's invariant cycle theorem; Zucker, through Lefschetz pencils.

**Where $\mathbb Q$ must enter.** In Proposition 3.1, as shown by C(iii); also in Theorem D, Step 1, through $L^{-1}$ and (I1). Theorems A, B and D are statements with $\mathbb Q$-coefficients only. The integral version of $\mathrm{GAGA}_4$ is *not* refuted by C(iii): Kollár's classes do vanish on a Zariski open set. Kollár's counterexamples live in (E3), that is, in $N^1H^4(X,\mathbb Z)/N^2H^4(X,\mathbb Z)$, where $N^2H^4(X,\mathbb Z)$ is exactly the image of $CH^2(X)$ by purity. More generally, [CTV] deduce from the Bloch–Kato conjecture that the Zariski sheaf $\mathcal H^4(\mathbb Z)$ is torsion-free. This would put every integral Hodge class that is rationally algebraic into $N^1H^4(X,\mathbb Z)$. Since the Bloch–Kato conjecture is a theorem (Rost–Voevodsky), this is unconditional [CTV, Thm. 3.1]. I do not use it.

## 6. GAPS

**G1 (the top target; rung (a)). Not proved.** The statement needed is
> $\mathrm{GAGA}_4$: for every smooth projective $X$ and every $\alpha\in\mathrm{Hdg}^2(X)$ there is a nonempty Zariski open $U\subset X$ with $\alpha|_U=0$ in $H^4(U,\mathbb Q)$.

*Why it is needed.* By Theorems A and B it is equivalent to $\mathrm{HC}(X,2)$. It is also exactly what the "$K_2$-exponential map" needs before it can start (Remark 3.3).

*Why I cannot prove it.* I know of no mechanism that produces the divisor $D$ from $\alpha$. The analytic objects the strategy offers are the Deligne class, the holomorphic 2-gerbe, and (through $d\log$) analytic $K_2$-symbols landing in $\mathcal H^2(\mathbb Z(2)_{\mathcal D})=\Omega^2_{cl}$. Each of them reduces, on an affine open set, to the Betti class (Lemma 2.4), so none supplies $D$. The analytic analogue of $\mathrm{GAGA}_4$ is false on Voisin's torus (Theorem C(ii)), so a proof must use projectivity in a new essential way. Known partial mechanisms: the decomposition of the diagonal [BS] ($CH_0$ supported in dimension $\le3$), Theorem D and Zucker (fibrations whose fibres have $H^3$ uniformly of coniveau 1), and special geometry (`docs/03`, M3).

**G2 (rung (b) as posed). Not achievable as stated.** "$H^2(X,\Omega^2)=0$" never holds (Prop. E(a)). The vanishing of $H^3(X,\mathcal O_X)$, or of all of $J^2(X)$, does not interact with $\mathrm{Ob}(X)$ (Lemma 2.4, Theorem B). The natural vanishing $h^{4,0}=h^{3,1}=0$ makes $\mathrm{HC}(X,2)$ *equivalent* to the following statement (Prop. E(b)), which I would need and cannot prove:
> if $h^{4,0}(X)=h^{3,1}(X)=0$, then every class of $H^4(X,\mathbb Q)$ vanishes on some nonempty Zariski open set.

**G3 (uniformity in Theorem D).** Hypothesis (H) is uniform in $t$. The pointwise version (coniveau 1 for $H^3(Y_t)$ at very general $t$) should imply (H) after a finite base change (Corollary D.1), by countability of relative Hilbert schemes and constructibility of the rank of $H^3(Y_t)\to H^3(Y_t\setminus\Sigma_t)$ over a parameter space. I have not written this argument, so the pointwise version is **not** claimed.

**G4 (no new cases).** I do not know a fourfold to which Theorem D or Corollary D.1 applies and for which $\mathrm{HC}(X,2)$ was not already known, by [BS], by product or projective-bundle formulas, or by Zucker [Z]. The recovery of Zucker's theorem sketched after Theorem D (Remark 3) is not verified in detail.

**G5 (inputs not re-checked online).** The search quota was exhausted. Theorem C(ii) depends on (I12)(V2) exactly in the form "every proper closed analytic subset of $T$ is finite". If Voisin's torus is only known to lack some of these subvarieties, C(ii) must be weakened accordingly. Theorem numbers for (I3), (I4), (I11) are from memory.

**G6 (not treated).** The torsion and integral refinements (unramified $H^3$, [CTV]), étale and $\ell$-adic analogues, Brauer-type groups, and the infinitesimal theory (Bloch's tangent space to $K_2$, Bloch–Esnault–Kerz) are not treated here. None of them bears on the rational obstruction $\mathrm{Ob}(X)$: they concern torsion or deformations, which is strategy S1, attack 01.

## 7. Checklist (`docs/03`, §3.4)

1. **Absoluteness.** Not delivered. $\mathrm{Ob}(X)\cong\mathrm{Hdg}(\eta_X)$ is defined through Betti cohomology of the generic point, on which $\mathrm{Aut}(\mathbb C)$ does not act. A proof of $\mathrm{GAGA}_4$ would imply absoluteness of degree-4 Hodge classes, through $\mathrm{HC}$. It must therefore contain an arithmetic ingredient (`docs/03`, C3), and nothing here supplies one.
2. **Lefschetz standard conjecture B.** Not delivered.
3. **Variational Hodge conjecture.** Not delivered. Theorem D concerns families, but it builds cycles on the total space from coniveau of fibres. It does not propagate cycles along a Hodge locus.
4. **Open special cases.** None settled. Of the open cases in `docs/03`, §3.4, item 4, the CM abelian varieties, the Weil classes and the Fermat sixfold have dimension $>4$, where Theorem D says nothing. Sextic fourfolds and $K3\times K3$ are fourfolds with $h^{4,0}=1$. For them, by Prop. E(c) the obstruction map is nonzero on $H^4$, and by Remark 2 after Theorem D, hypothesis (H) cannot hold for any fibration over a curve. The route says nothing new there.
5. **Break with the false variants.**
   * *Rational coefficients* are used in Proposition 3.1 (the $E_2$-degeneration (I4), the splitting (I1), $\mathbb Q$-divisors (I2)), in Theorem A through 3.1, in Theorem B (the multiples $N$), and in Theorem D, Step 1 (the inverse $L^{-1}$ of hard Lefschetz is only rational, plus (I1)). Theorem C(iii) shows that the use in Proposition 3.1 is unavoidable: integrally the statement is false, already on the fourfold $X\times\mathbb P^1$. No result here is stated integrally, so none of them implies the false integral Hodge conjecture.
   * *Projectivity* is used in Theorems A and B through the Zariski topology and algebraic mixed Hodge theory ((I3)–(I5) are applied to algebraic varieties), and through Lefschetz (1,1) in divisor form. In Theorem D it enters through the rational ample class, Verdier's theorem and the invariant cycle theorem. The essential use is the one the route cannot supply, $\mathrm{GAGA}_4$; Theorem C(ii) shows it fails on Voisin's torus.
   * *Kähler test.* Propositions 2.1, 2.2 and Lemma 2.4 hold on compact Kähler manifolds, but they produce no cycles. A Kähler analogue of Theorem A(i), which I do not prove, could at most say that Hodge classes vanishing off an analytic hypersurface are Chern-class combinations. On $T$ that would be vacuous ($N^1_{an}=0$, Theorem C(ii)), so it is consistent with (V1). Nothing here "proves" the Kähler Hodge conjecture.

## 8. References

(Quoted from memory or from `docs/05-references.md`; not re-checked online in this run.)

* [AF] A. Andreotti, T. Frankel, *The Lefschetz theorem on hyperplane sections*, Ann. of Math. 69 (1959), 713–717.
* [BM] J.-L. Brylinski, D. A. McLaughlin, *The geometry of degree-four characteristic classes and of line bundles on loop spaces I*, Duke Math. J. 75 (1994), 603–638.
* [BO] S. Bloch, A. Ogus, *Gersten's conjecture and the homology of schemes*, Ann. Sci. ÉNS (4) 7 (1974), 181–201.
* [BS] S. Bloch, V. Srinivas, *Remarks on correspondences and algebraic cycles*, Amer. J. Math. 105 (1983), 1235–1253.
* [CG] C. H. Clemens, P. A. Griffiths, *The intermediate Jacobian of the cubic threefold*, Ann. of Math. 95 (1972), 281–356.
* [CTV] J.-L. Colliot-Thélène, C. Voisin, *Cohomologie non ramifiée et conjecture de Hodge entière*, Duke Math. J. 161 (2012), 735–801.
* [D2] P. Deligne, *Théorie de Hodge II*, Publ. Math. IHÉS 40 (1971), 5–57.
* [EV] H. Esnault, E. Viehweg, *Deligne–Beilinson cohomology*, in: Beilinson's Conjectures on Special Values of L-functions, Perspect. Math. 4, Academic Press 1988, 43–91.
* [H] H. Hironaka, *Resolution of singularities of an algebraic variety over a field of characteristic zero I, II*, Ann. of Math. 79 (1964), 109–326.
* [Ja] U. Jannsen, *Mixed motives and algebraic K-theory*, LNM 1400, Springer 1990.
* [Ko] J. Kollár, *Trento examples*, in: Classification of irregular varieties, LNM 1515, Springer 1992, 134–135.
* [Q] D. Quillen, *Higher algebraic K-theory I*, in: Algebraic K-theory I, LNM 341, Springer 1973, 85–147.
* [V-I] C. Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge 2002 (Deligne cohomology, §12.3).
* [V02] C. Voisin, *A counterexample to the Hodge conjecture extended to Kähler varieties*, IMRN 2002, no. 20, 1057–1075.
* [Ve] J.-L. Verdier, *Stratifications de Whitney et théorème de Bertini–Sard*, Invent. Math. 36 (1976), 295–312.
* [Z] S. Zucker, *The Hodge conjecture for cubic fourfolds*, Compositio Math. 34 (1977), 199–209.
* Background, not used in proofs: D. Mumford, *Rational equivalence of 0-cycles on surfaces*, J. Math. Kyoto Univ. 9 (1969); M. Nori, *Algebraic cycles and Hodge theoretic connectivity*, Invent. Math. 111 (1993); P. Griffiths, *On the periods of certain rational integrals I, II*, Ann. of Math. 90 (1969); S. Bloch, H. Esnault, M. Kerz (2014), see `docs/05`.

## 9. Claimed results

| Label | Statement (one line) | Status |
|---|---|---|
| Prop. 2.1 | $\mathbb Z(2)_{\mathcal D}\simeq[\mathcal O^*\xrightarrow{d\log}\Omega^1][-1]$, with cohomology sheaves $\mathbb C^*$ (degree 1) and $\Omega^2_{cl}$ (degree 2) | proved here (standard) |
| Prop. 2.2 | On compact Kähler $M$, $H^4_{\mathcal D}(M,\mathbb Z(2))\twoheadrightarrow\mathrm{Hdg}^2_{\mathbb Z}(M)$, and $\mathrm{Im}(H^3(\mathcal O^*)\to H^4(\mathbb Z))=\{\alpha^{0,4}=0\}$ | known (Deligne; [EV], [V-I]) |
| Lemma 2.3 | $H^{\ge1}_{Zar}(\text{constant})=H^{\ge2}_{Zar}(\mathcal O^*)=H^{\ge3}_{Zar}(\mathcal K_2)=0$ on smooth $X$ | proved here (standard) |
| Lemma 2.4 | On affine $U$, $H^k_{\mathcal D}(U,\mathbb Z(2))\cong H^k(U,\mathbb Z(2))$ ($k\ge3$) and $H^k(U,\mathcal O^*)\cong H^{k+1}(U,\mathbb Z(1))$ ($k\ge1$), naturally | proved here (elementary; likely folklore) |
| Prop. 3.1 | A rational Hodge class of degree 4 vanishing on a nonempty Zariski open set is algebraic | known (classical, cf. [BS]); proof included |
| Theorem A | $\mathrm{Hdg}^2(X)\cap N^1=A^2(X)$ and $\mathrm{Hdg}^2/A^2\cong\mathrm{Hdg}(\eta_X)\subset H^0(X,\mathcal H^4_{\mathbb Q})$ | known in substance; proved here |
| Cor. A.1 | $\mathrm{Hdg}^2/A^2$ is a birational invariant; $\mathrm{HC}(X,2)$ is a birational property | proved here (folklore) |
| Cor. A.2 | $\dim X\le3\Rightarrow\mathrm{Hdg}(\eta_X)=0$, giving $\mathrm{HC}(X,2)$ without the hard-Lefschetz reduction to divisors | proved here (conclusion known) |
| Prop. 3.2 | In degree 2, $\mathrm{Hdg}^1/A^1\cong\mathrm{Hdg}^1(\eta_X)$, and exp + GAGA kill $\mathrm{Hdg}^1(\eta_X)$ | proved here (reformulation of Lefschetz (1,1)) |
| Theorem B | $\mathrm{HC}(X,2)\iff$ $\mathrm{GAGA}_4$ (Deligne classes, equivalently 2-gerbes, of Hodge classes are rationally Zariski-locally trivial) | tautological reformulation of Theorem A(i) via Lemma 2.4 |
| Theorem C | (E1) holds on Kähler manifolds; (E2) fails on Voisin's torus; integral (E3) fails (Kollár, also on $X\times\mathbb P^1$); no Zariski version | (i), (iv) known or elementary. (ii), (iii) short deductions from (I12), (I13). (iii) is known [CTV]. (ii) uses (I12)(V2) in its strong form. |
| Prop. E | $h^{2,2}\ge1$; if $h^{4,0}=h^{3,1}=0$ then $\mathrm{HC}(X,2)\iff H^4=N^1H^4$; $h^{4,0}\ne0\Rightarrow\mathrm{ob}\ne0$ on $H^4$ | proved here (elementary) |
| Theorem D | Fourfold $X\to C$ with $H^3(Y_t)\to H^3(Y_t\setminus\Sigma)$ zero for $t$ in a nonempty open (H) $\Rightarrow\mathrm{HC}(X,2)$ | proved here (coniveau form of the Griffiths–Zucker mechanism; essentially known, cf. Zucker 1977, Conte–Murre 1978, Bloch–Srinivas 1983). It gives no new case (G4). |
| Cor. D.1 | The same after a finite base change $C'\to C$ | proved here |
