# Attack 12: trying to disprove the Hodge conjecture — which obstruction mechanisms survive with $\mathbb{Q}$-coefficients

*Strategy S7 (counterexample hunting), second run, 2026-11-07. Draft for refereeing. Every result labelled "proved here" has a complete proof in this file; everything else is quoted with a reference and listed in §9.*

**Referee (2026-11-13):** major revision; corrections applied. Report summary: docs/06-attack-report.md.

## 0. Outcome

**Top target: not reached.** I found no rational Hodge class that is provably non-algebraic, and I have no candidate with a proof of non-algebraicity.

**What is proved instead.** For each obstruction mechanism on the list (specialization/degeneration, tropical/maximal degeneration, Galois/absoluteness, reduction modulo $p$, positivity, coniveau) I either prove that it is *void with $\mathbb{Q}$-coefficients* on the candidate families, or reduce it to a precisely stated open problem.

* **Theorem A (rational specialization obstructions reduce to HC on the components).** In any projective degeneration, the specialization of a flat family of Hodge classes is a sum of push-forwards of *Hodge classes on the components of a resolved special fibre*. So a rational specialization obstruction can only *transport* a counterexample that already lives on a component; it can never create one. Corollaries A.2–A.4 make this independent of the model and remove every rational version of the Kollár and Engel–de Gaay Fortman–Schreieder (EdGFS) arguments for abelian varieties, provided the abelian part of the degeneration satisfies HC (conditional on the existence of toric-bundle models, gap G3).
* **Theorem B (Weil type).** For abelian $2n$-folds of Weil type, the Witt index of the Hermitian form is $n$ when $\operatorname{disc}=(-1)^n$ and $n-1$ otherwise. Every local monodromy satisfies $\operatorname{rk}N\le 2\cdot(\text{Witt index})$. The "maximal degeneration only if $\operatorname{disc}=(-1)^n$" part is the content of arXiv:2609.14169; the exact Witt index is also in arXiv:2609.14169 (Lemma 9); the proof here is an alternative via Meyer's theorem. **Corollary B.2:** for non-split sixfolds ($\operatorname{disc}\ne-1$), every degeneration with non-trivial monodromy has abelian part a non-split Weil fourfold or surface. Combined with Theorem A, this leaves no rational specialization obstruction (conditional on G3).
* **Theorem C (real multiplication).** Families of projective K3 surfaces with real multiplication by a totally real field $E\neq\mathbb{Q}$ have *finite* local monodromy on $H^2$. They have no type II or III degenerations, so the degeneration and tropical mechanisms have nothing to work with on $S\times S$.
* **Proposition D (Galois).** Known results show this mechanism is void on abelian varieties, products of K3 surfaces and Fermat varieties. Immediate corollary of Principle B (D4): it is also void along every component of the Hodge locus of sextic fourfolds that passes through the Fermat point.
* **Proposition E, Theorem E4 (characteristic $p$).** The Tate-class test is passed automatically. What survives is a **rationality test at supersingular primes** (Milne's rationality conjecture). For Weil classes I make it explicit: there is an invariant $[\lambda_v]\in(K\otimes\mathbb{Q}_\ell)^\times/K^\times$ with rational norm, and HC implies $[\lambda_v]=1$. The accompanying sign condition holds unconditionally (Milne, Ann. Math. 155 (2002), Remark 3.7), so only the class of $\lambda_v$ in $T^1(\mathbb{Q}_\ell)/T^1(\mathbb{Q})$ can carry an obstruction; this is a case of Milne's rationality conjecture. **This is the only mechanism on the list that I cannot show to be void. If a counterexample exists among the candidates, this is the mechanism I would use to look for it** (Statement S, gap G1).
* **Proposition F (reductions; known in substance).** A counterexample on an abelian variety yields either a counterexample on a CM abelian variety (and then a non-algebraic *split* Weil class), or a counterexample to the variational Hodge conjecture over a Shimura variety. It also yields a failure of the Lefschetz standard conjecture $B$ on some variety.

## 1. Conventions; what an "obstruction mechanism" is

$X$ is smooth projective over $\mathbb{C}$ with $\dim X=n$, and $\mathrm{Hdg}^p(X)=H^{2p}(X,\mathbb{Q})\cap H^{p,p}$. A class is *algebraic* if it lies in the $\mathbb{Q}$-span $A^p(X)$ of classes of subvarieties. For a complex variety $Y$, $H_*(Y)$ is singular homology with $\mathbb{Q}$-coefficients, which equals Borel–Moore homology when $Y$ is compact. The cycle class map $\mathrm{cl}\colon CH_k(Y)_\mathbb{Q}\to H_{2k}(Y)$ commutes with proper push-forward [Fu, 19.1]. "HS" means a polarizable rational Hodge structure.

An *obstruction mechanism* attaches to each pair $(X,\alpha)$, $\alpha\in\mathrm{Hdg}^p(X)$, a condition $\mathsf N(X,\alpha)$ that holds whenever $\alpha\in A^p(X)$. It *disproves HC* if some Hodge class violates $\mathsf N$. It is *void on a family of pairs* if $\mathsf N$ provably holds for every Hodge class in that family.

The candidate families (from the task) are:

* (K1) abelian $2n$-folds of Weil type with $\operatorname{disc}\ne(-1)^n$ ("non-split"), in particular sixfolds with $\operatorname{disc}\in\mathbb{Q}_{<0}/N(K^\times)$, $\operatorname{disc}\ne-1$ (with $\operatorname{disc}=\det H$ no Weil sixfold has discriminant $+1$, since $\det H$ has sign $(-1)^n$);
* (K2) simple abelian varieties of dimension $\ge6$ with exceptional non-Weil classes;
* (K3) $S\times S$ for a projective K3 surface $S$ with real multiplication (RM) by a totally real field $E\ne\mathbb{Q}$;
* (K4) sextic fourfolds on Noether–Lefschetz components;
* (K5) Fermat varieties and their products, at indecomposable Hodge characters.

## 2. Specialization and degeneration (Kollár, EdGFS): Theorem A

**Setting 2.1.** $C$ is a smooth connected curve, $0\in C$ and $C^\circ=C\smallsetminus\{0\}$. $f\colon\mathcal{X}\to C$ is a projective morphism from an integral variety, smooth of relative dimension $n$ over $C^\circ$, with fibres $X_t=f^{-1}(t)$. For a small disc $\Delta\ni 0$ the inclusion $j\colon X_0\hookrightarrow\mathcal X_\Delta:=f^{-1}(\Delta)$ is a homotopy equivalence (triangulate the pair; Łojasiewicz, see [Cl, §1]). For $t\in\Delta^*$ define $\mathrm{sp}:=(j_*)^{-1}\circ i_{t*}\colon H_*(X_t)\to H_*(X_0)$.

*Background (standard; quoted, not used in any proof).* Suppose $\alpha_t$ is algebraic for $t$ outside a countable subset of $C^\circ$. Then, by countability of the components of relative Hilbert schemes and Fulton's specialization of cycles [Fu, §10.1, §19.2], after a finite base change $\mathrm{sp}(\alpha_t\cap[X_t])$ is the class of a $\mathbb{Q}$-cycle on $X_0$. Kollár's and EdGFS's arguments exhibit a homomorphism $\lambda$ on $H_{2n-2p}(X_0,\mathbb{Z})$, with values in a torsion group, that kills algebraic classes but not $\mathrm{sp}(\alpha)$. The rational analogue would be a $\mathbb{Q}$-linear $\lambda$ with the same property. Theorem A shows that such a $\lambda$ can exist only if HC fails on a component.

**Theorem A (proved here).** In Setting 2.1, let $\alpha\in H^0(C^\circ,R^{2p}f_*\mathbb{Q})$ be a flat section with $\alpha_t\in\mathrm{Hdg}^p(X_t)$ for one $t$; then the same holds for every $t$, by the theorem of the fixed part [De2, 4.1.2]. Let $\bar f\colon\bar{\mathcal X}\to\bar C$ be a morphism from a smooth projective variety to the smooth completion of $C$, together with a proper birational $\rho\colon\bar f^{-1}(C)\to\mathcal X$ over $C$ that is an isomorphism over $C^\circ$. Such data exist by Hironaka: compactify, then resolve without touching the smooth locus. Let $E_1,\dots,E_r$ be the irreducible components of $\tilde X_0:=\bar f^{-1}(0)$, let $\epsilon_l\colon\tilde E_l\to E_l$ be resolutions, and let $\phi_l\colon\tilde E_l\to\bar{\mathcal X}$ and $\psi_l:=\rho\circ\phi_l\colon\tilde E_l\to X_0$ be the induced morphisms. Then:

1. there is $\tilde\alpha\in\mathrm{Hdg}^p(\bar{\mathcal X})$ with $\tilde\alpha|_{X_t}=\alpha_t$ for all $t\in C^\circ$;
2. for every such $\tilde\alpha$ there are $c_l\in\mathbb{Q}$ such that, with $\gamma_l:=\phi_l^*\tilde\alpha\in\mathrm{Hdg}^p(\tilde E_l)$,
$$\mathrm{sp}\big(\alpha_t\cap[X_t]\big)=\sum_{l}c_l\,\psi_{l*}\big(\gamma_l\cap[\tilde E_l]\big)\quad\text{in } H_{2n-2p}(X_0);$$
3. hence, if every $\gamma_l$ is algebraic on $\tilde E_l$ (for instance if $\mathrm{HC}(\tilde E_l,p)$ holds for all $l$), then $\mathrm{sp}(\alpha_t\cap[X_t])=\mathrm{cl}(z)$ for a $\mathbb{Q}$-cycle $z$ on $X_0$. In that case no $\mathbb{Q}$-linear functional on $H_{2n-2p}(X_0)$ that kills algebraic classes can detect $\alpha$.

*Proof.* (1) $U:=\bar f^{-1}(C^\circ)$ is Zariski open in the smooth projective $\bar{\mathcal X}$, and $U\to C^\circ$ is smooth and projective. By Deligne's global invariant cycle theorem [De2, 4.1.1], the restriction $r\colon H^{2p}(\bar{\mathcal X},\mathbb{Q})\to H^{2p}(X_t,\mathbb{Q})$ has image $H^{2p}(X_t)^{\pi_1(C^\circ,t)}$, which contains $\alpha_t$. The map $r$ is a morphism of pure HS of weight $2p$, and $H^{2p}(\bar{\mathcal X})$ is polarizable. So $\ker r$ has a complement $M$ that is a sub-HS (its orthogonal complement for a polarization), and $r|_M\colon M\to\operatorname{Im}r$ is an isomorphism of HS. Put $\tilde\alpha:=(r|_M)^{-1}(\alpha_t)$. It is a Hodge class, because an isomorphism of HS identifies Hodge classes. The sections $s\mapsto\tilde\alpha|_{X_s}$ and $\alpha$ are flat over the connected $C^\circ$ and agree at $t$, so they agree everywhere.

(2) Put $\tilde{\mathcal X}_\Delta:=\bar f^{-1}(\Delta)$. For small $\Delta$, the inclusion $\tilde j\colon\tilde X_0\hookrightarrow\tilde{\mathcal X}_\Delta$ is a homotopy equivalence. Let $\tilde i_t\colon X_t\hookrightarrow\tilde{\mathcal X}_\Delta$. Then $i_t=\rho\circ\tilde i_t$ and $\rho\circ\tilde j=j\circ\rho_0$, where $\rho_0:=\rho|_{\tilde X_0}$. Let $a:=\tilde\alpha|_{\tilde{\mathcal X}_\Delta}$, so that $\tilde i_t^*a=\alpha_t$.

Since $\tilde X_0$ is a Cartier divisor in the irreducible $(n+1)$-fold $\bar{\mathcal X}$, it has pure dimension $n$. So $H_{2n}(\tilde X_0)$ has basis the classes $(\iota_l\epsilon_l)_*[\tilde E_l]$, where $\iota_l\colon E_l\hookrightarrow\tilde X_0$ [Fu, Lemma 19.1.1]. Hence $\tilde i_{t*}[X_t]=\tilde j_*\sum_l c_l(\iota_l\epsilon_l)_*[\tilde E_l]$ for some $c_l\in\mathbb{Q}$. (They are the multiplicities of $E_l$ in $\bar f^*(0)$, but this is not needed.) Applying the projection formula $g_*(g^*x\cap y)=x\cap g_*y$ three times:
$$i_{t*}(\alpha_t\cap[X_t])=\rho_*\big(a\cap\tilde i_{t*}[X_t]\big)=\rho_*\tilde j_*\sum_l c_l(\iota_l\epsilon_l)_*\big(\phi_l^*\tilde\alpha\cap[\tilde E_l]\big)=j_*\sum_l c_l\,\psi_{l*}\big(\gamma_l\cap[\tilde E_l]\big).$$
Now apply $(j_*)^{-1}$. Each $\gamma_l$ is a Hodge class because $\phi_l$ is a morphism of smooth projective varieties.

(3) If $\gamma_l=\mathrm{cl}(z_l)$, then $\gamma_l\cap[\tilde E_l]$ is the class of $z_l$ in $H_{2n-2p}(\tilde E_l)$, and $\psi_{l*}\mathrm{cl}(z_l)=\mathrm{cl}(\psi_{l*}z_l)$ [Fu, 19.1]. $\square$

**Remark 2.2 (where $\mathbb{Q}$ is used; why Kollár and EdGFS survive integrally).** Coefficients enter only in step (1): the global invariant cycle theorem and the semisimplicity splitting are statements over $\mathbb{Q}$. Integrally, the computation in (2) holds verbatim for any *integral* Hodge lift. What can fail is twofold. First, an integral Hodge lift may not exist: in general only $N\alpha_t$ lifts, for some $N\ge1$ depending on the family. Second, integral HC may fail on the components. In a maximal degeneration with toric components, integral HC holds on the components [Fl, §5.2]. So any integral obstruction detected there through the condition "$\mathrm{sp}(\alpha)$ is algebraic on $X_0$" must come from the lifting step. (The actual EdGFS argument uses finer monodromy and matroid information, which I do not analyse.)

**Remark 2.3 (any class on a Hodge locus fits Setting 2.1).** Let $\alpha$ be a Hodge class on a fibre of a smooth projective family over a smooth connected curve $C^\circ$ that lies in the Hodge locus of $\alpha$, in the sense that parallel transport of $\alpha$ along every path in $C^\circ$ stays Hodge. Then the monodromy orbit of $\alpha$ consists of Hodge classes in a lattice $\frac1m H^{2p}(X_t,\mathbb{Z})$, all of the same norm for a monodromy-invariant polarization, which is definite on real $(p,p)$-classes by the Hodge–Riemann relations. So the orbit is finite. After a finite base change, $\alpha$ is therefore a global flat section.

**Corollary A.2 (independence of the model; proved here).** Suppose that for one projective model $\mathcal P\to C$ with smooth total space and for one Hodge lift $\tilde\alpha$ as in A(1), every component $Y$ of $P_0$ is smooth and every restriction $\tilde\alpha|_{Y}$ is algebraic. Then $\mathrm{sp}'(\alpha)$ is algebraic for *every* projective model $\mathcal X'\to C'$ of the family after any finite base change $C'\to C$.

*Proof.* Here a model over $C'$ means a projective $\mathcal X'\to C'$ that is isomorphic over $C'^\circ$ to the pull-back of the family. The rational map $\bar{\mathcal X}'\dashrightarrow\bar{\mathcal P}$ over $\bar C$ is a morphism over $C'^\circ$. Resolve the closure of its graph. This gives a smooth projective $\bar{\mathcal X}''$, a birational morphism $\pi\colon\bar{\mathcal X}''\to\bar{\mathcal X}'$ that is an isomorphism over $C'^\circ$, and a morphism $\mu\colon\bar{\mathcal X}''\to\bar{\mathcal P}$ over $\bar C$, which maps the fibre over $0'$ into $P_0$. Apply Theorem A to $\mathcal X''\to C'$ with the lift $\mu^*\tilde\alpha$, which restricts to $\alpha$ on the general fibre. Each component $\tilde E$ of the resolved special fibre is irreducible and reduced and maps into some component $Y$ of $P_0$. Since $Y$ is smooth, $\gamma_{\tilde E}=(\mu|_{\tilde E})^*(\tilde\alpha|_Y)$ is the pull-back of an algebraic class along a morphism of smooth projective varieties, hence algebraic. Thus $\mathrm{sp}''(\alpha)$ is algebraic. Finally, $\mathrm{sp}'=\pi_*\circ\mathrm{sp}''$ by naturality of the retractions, and $\pi_*$ preserves algebraic classes. $\square$

**Lemma A.3 (toric bundles; proved here).** Let $B$ be smooth projective, $T=\mathbb{G}_m^r$, $P\to B$ a $T$-torsor (Zariski locally trivial by Hilbert 90), and $Z$ a smooth projective toric variety with torus $T$. Assume $Y=P\times^T Z$ is projective. If $\mathrm{HC}(B,q)$ holds for all $q\le p$, then $\mathrm{HC}(Y,p)$ holds.

*Proof.* The divisor classes $\xi_\rho=[P\times^T D_\rho]$, for the $T$-invariant prime divisors $D_\rho\subset Z$, restrict on each fibre to $[D_\rho]$, and these generate $H^*(Z,\mathbb{Q})$ [Fl, §5.2]. Choose monomials $m_1,\dots,m_s$ in the $\xi_\rho$ restricting to a basis of $H^*(Z)$. By Leray–Hirsch, $\Phi\colon\bigoplus_i H^{*-2d_i}(B)(-d_i)\to H^*(Y)$, $(b_i)\mapsto\sum_i\pi^*b_i\cdot m_i$ with $d_i=\deg m_i$, is bijective. It is a morphism of HS, since the $m_i$ are algebraic of type $(d_i,d_i)$, so it is an isomorphism of HS. Hence $\mathrm{Hdg}^p(Y)=\sum_i\pi^*\mathrm{Hdg}^{p-d_i}(B)\cdot m_i$, and every class on the right is algebraic. $\square$

**Corollary A.4 (rational EdGFS-type obstructions; proved here, conditional on G3).** Let $\mathcal A\to C^\circ$ be a polarized family of abelian $g$-folds whose local monodromy at $0$ has $\operatorname{rk}N=t$, and let $B$ be the abelian part of the limit (of dimension $g-t$). Assume, as provided by Mumford's construction and the toroidal compactifications of Faltings–Chai [FC, III, VI] together with toroidal resolution, that after a finite base change there is a projective model with smooth total space whose special-fibre components are toric-variety bundles, as in Lemma A.3, over abelian varieties isogenous to $B$. If $\mathrm{HC}$ holds for $B$ in all degrees, then for every flat family $\alpha$ of Hodge classes and every projective model, $\mathrm{sp}(\alpha)$ is algebraic. This applies when $t=g$ (maximal degeneration, $B=0$: the EdGFS setting) and whenever $\dim B\le5$, where HC is known [Ma2, Ma3].

*Proof.* Combine Lemma A.3, Corollary A.2 and HC for abelian varieties isogenous to $B$; HC is invariant under isogeny, since isogenies are finite surjective morphisms. $\square$

## 3. Weil type: Witt index and degenerations (Theorem B)

**Setting 3.1.** $K\subset\mathbb{C}$ is imaginary quadratic, $a\mapsto\bar a$ is conjugation, and $N=N_{K/\mathbb{Q}}$. An abelian $2n$-fold of Weil type is a triple $(A,\iota,E)$: here $\iota\colon K\to\mathrm{End}^0(A)$, $E$ is a Riemann form on $V=H_1(A,\mathbb{Q})$ with $E(\iota(a)x,y)=E(x,\iota(\bar a)y)$, and $\iota(a)$ acts on $T_0A$ with eigenvalues $a$ and $\bar a$, each with multiplicity $n$. Fix $\eta\in K$ with $\bar\eta=-\eta$ and put $H(x,y)=E(x,\iota(\eta)y)+\eta E(x,y)$.

A direct check shows that $H$ is $K$-linear in $y$ and satisfies $\overline{H(y,x)}=H(x,y)$. It has signature $(n,n)$. To see this, let $J$ be the complex structure, $g=E(\cdot,J\cdot)$ and $\theta=J^{-1}\iota(\eta)/|\eta|$. Then $\theta$ is a $g$-self-adjoint involution commuting with $J$ and $\iota(K)$, and its eigenspaces have complex dimensions given by the eigenvalue multiplicities. Moreover $H(x,x)=E(x,\iota(\eta)x)=|\eta|\,g(x,\theta x)$. In the same way, multiplicities $(a,b)$ give signature $(a,b)$. Set $\operatorname{disc}(A):=\det H\in\mathbb{Q}^\times/N(K^\times)$; it does not depend on $\eta$ or on scaling $E$.

The hyperbolic plane $\mathbb H$ (Gram matrix $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$) has determinant $-1$, so $\operatorname{disc}(\mathbb H^n)=(-1)^n$; *split* means $H\cong\mathbb H^n$. With this convention Markman's theorem for sixfolds [Ma2] is the case $\operatorname{disc}=-1$, i.e. the split case (called "split Weil type" in [Ma3]), and K1 for $n=3$ is $\operatorname{disc}\in\mathbb{Q}_{<0}/N(K^\times)\smallsetminus\{-1\}$. The Witt index $\operatorname{ind}(H)$ is the maximal dimension of a totally isotropic $K$-subspace.

**Theorem B (proved here; the consequence "no maximal degeneration unless split" is the content of arXiv:2609.14169).**

1. $\operatorname{ind}(H)\in\{n-1,n\}$, and $\operatorname{ind}(H)=n$ if and only if $\operatorname{disc}(A)=(-1)^n$.
2. Let $(\mathcal A,\iota,E)\to\Delta^*$ be a family of abelian $2n$-folds of Weil type with $\iota$ and $E$ flat, and let $\gamma$ be the local monodromy on $V=H_1(A_t,\mathbb{Q})$. For some $m\ge1$, $u=\gamma^m$ satisfies $(u-1)^2=0$. The operator $N:=u-1$ is $K$-linear, $\operatorname{Im}N$ is totally isotropic for $H$, and $\ker N=(\operatorname{Im}N)^\perp$. Hence $\operatorname{rk}_\mathbb{Q}N=2\dim_K\operatorname{Im}N\le 2\operatorname{ind}(H)$. In particular, maximal unipotent monodromy ($\operatorname{rk}N=\dim A=2n$) forces $\operatorname{disc}(A)=(-1)^n$.

*Proof.* (1) Let $W$ be a maximal totally isotropic subspace, of dimension $r$.

*An isotropic partner.* Choose a complement $U$ of $W^\perp$. Then $H\colon W\times U\to K$ is perfect, so $U$ has a basis $u_j$ dual to a basis $w_i$ of $W$. Put $u'_j=u_j-\tfrac12\sum_i H(u_i,u_j)w_i$. Then $H(u'_j,u'_k)=H(u_j,u_k)-\tfrac12\overline{H(u_k,u_j)}-\tfrac12H(u_j,u_k)=0$, and $H(w_i,u'_j)=\delta_{ij}$. So $P=W\oplus\langle u'_j\rangle\cong\mathbb H^r$ and $V=P\perp V_0$.

*$V_0$ is anisotropic.* An isotropic $v\in V_0\smallsetminus0$ would make $W+Kv$ totally isotropic of dimension $r+1$. By Sylvester, $V_0$ has signature $(n-r,n-r)$. If $n-r\ge1$, the trace form $q(x)=H(x,x)$ on the $\mathbb{Q}$-space $V_0$ (of dimension $4(n-r)$) is anisotropic and indefinite. By Meyer's theorem [Se, IV.3.2, Cor. 2] this forces $4(n-r)\le4$. So $r\ge n-1$.

*The two cases.* If $r=n$, then $H\cong\mathbb H^n$ and $\det H=(-1)^n$. If $r=n-1$, diagonalize $V_0\cong\langle a\rangle\perp\langle b\rangle$ with $a,b\in\mathbb{Q}^\times$. It is isotropic iff $aN(x)+bN(y)=0$ has a solution $(x,y)\ne0$, i.e. iff $-ab=-b/a\cdot a^2\in N(K^\times)$. Anisotropy therefore gives $\det V_0=ab\notin -N(K^\times)$, hence $\det H=(-1)^{n-1}ab\notin(-1)^nN(K^\times)$.

(2) The monodromy theorem [La] gives $(\gamma^m-1)^{2}=0$ on $H_1$, since the weight is $1$. The operator $u$ commutes with $\iota(K)$ and preserves $E$, hence preserves $H$, so $N$ is $K$-linear. From $H(ux,uy)=H(x,y)$ we get $H(Nx,y)+H(x,Ny)+H(Nx,Ny)=0$. Replacing $y$ by $Ny$ and using $N^2=0$ gives $H(Nx,Ny)=0$. Then $H(Nx,y)=-H(x,Ny)$, so $\ker N=(\operatorname{Im}N)^\perp$. $\square$

**Corollary B.1 (abelian parts; proved here).** In (2), the central graded piece $\ker N/\operatorname{Im}N$ of the limit mixed Hodge structure is $H_1(B)$ for an abelian variety $B$ of dimension $2n-\operatorname{rk}N$. This $B$ is of Weil type for $K$ with $\operatorname{disc}(B)=(-1)^{\operatorname{rk}N/2}\operatorname{disc}(A)$. If $A$ is non-split, so is $B$. For $n=3$ and $A$ non-split ($\operatorname{disc}(A)\ne-1$): $\operatorname{rk}N\in\{0,2,4\}$, and $B$ is a non-split Weil sixfold, fourfold or surface.

*Proof.* For $N^2=0$ the weight filtration on homology is $\operatorname{Im}N\subseteq\ker N\subseteq V$. The central piece is a pure HS polarized by $E$ [Sc, 6.16], and $K$ acts on it by functoriality of the limit. $H$ induces a non-degenerate $H_B$ on $\ker N/\operatorname{Im}N=W^\perp/W$, where $W=\operatorname{Im}N$. With an isotropic partner of $W$ as in (1), $H\cong\mathbb H^{m}\perp H_B$ with $m=\dim_KW$. So $\det H_B=(-1)^m\det H$ and $H_B$ has signature $(n-m,n-m)$. By 3.1, $K$ then acts on $\mathrm{Lie}\,B$ with multiplicities $(n-m,n-m)$. Non-splitness follows from (1). $\square$

**Corollary B.2 (degenerations cannot disprove HC on K1 for $n=3$; proved here, conditional on G3).** Let a family of non-split Weil sixfolds over $C^\circ$ degenerate at $0$.

* If $\operatorname{rk}N\in\{2,4\}$, the abelian part is an abelian fourfold or surface, for which HC is known [Ma2; Lefschetz]. By Corollary A.4, every rational specialization obstruction vanishes, for every model.
* If $\operatorname{rk}N=0$, then after base change the period map extends over $\Delta$ and the family extends to an abelian scheme. Specialization then carries the Weil classes to Weil classes of another non-split Weil sixfold (same Hermitian form), which is the same open problem.

For general $n$, by Lemma A.3, a rational specialization obstruction on a non-split Weil $2n$-fold must be witnessed by a counterexample to HC on the abelian part $B$: a non-split Weil variety of smaller dimension $2n-\operatorname{rk}N\ge2$.

## 4. Real multiplication on K3 surfaces: Theorem C

**Theorem C (proved here; equivalent to the compactness of the RM Shimura variety ($\mathrm{Res}_{E/\mathbb{Q}}SO(\phi)$ is $\mathbb{Q}$-anisotropic because $\phi$ is definite at the real places $\sigma\ne\sigma_1$; Godement's criterion)).** Let $\pi\colon\mathcal S\to\Delta^*$ be a smooth projective family of K3 surfaces with a flat class $h$ of a relatively ample line bundle. Let $\mathbb T\subseteq R^2\pi_*\mathbb{Q}$ be a sub-VHS with $\mathbb T\perp h$ and $H^{2,0}(S_t)\subset\mathbb T_t\otimes\mathbb{C}$. Let a totally real field $E$ with $[E:\mathbb{Q}]=d\ge2$ act on $\mathbb T$ by flat endomorphisms of HS that are self-adjoint for the intersection form $\psi$. Then the local monodromy $\gamma$ has finite order on $\mathbb T_t$. If $\mathbb T^\perp$ consists of Hodge classes (e.g. $\mathbb T_t=T(S_t)$ for very general $t$), then $\gamma$ has finite order on $H^2(S_t,\mathbb{Q})$.

(For RM, self-adjointness is automatic: by Zarhin [Za], the adjoint involution on the field $\mathrm{End}_{Hdg}(T(S))$ is complex conjugation, hence the identity when this field is totally real. It is a closed condition, so it propagates from a very general fibre.)

*Proof.* *Step 1.* For $x,y\in\mathbb T_t$ the map $e\mapsto\psi(ex,y)$ is $\mathbb{Q}$-linear, so it equals $e\mapsto\operatorname{tr}_{E/\mathbb{Q}}(e\,\phi(x,y))$ for a unique $\phi(x,y)\in E$. The form $\phi$ is $E$-bilinear, and symmetric by self-adjointness. Flat endomorphisms commute with monodromy, so $\gamma$ is $E$-linear and preserves $\psi$; since the trace form is non-degenerate, $\gamma$ preserves $\phi$.

*Step 2.* Write $\mathbb T_t\otimes\mathbb{R}=\bigoplus_\sigma T_\sigma$ with $T_\sigma=\mathbb T_t\otimes_{E,\sigma}\mathbb{R}$. This decomposition is $\psi$-orthogonal, and $\psi|_{T_\sigma}=\sigma\circ\phi$. $E$ preserves the line $H^{2,0}$ and acts on it through one (real) embedding $\sigma_1$, so $H^{2,0}\oplus H^{0,2}\subseteq T_{\sigma_1}\otimes\mathbb{C}$. For $\sigma\neq\sigma_1$ we get $T_\sigma\otimes\mathbb{C}\subseteq H^{1,1}$, so $T_\sigma\subseteq H^{1,1}_\mathbb{R}\cap h^\perp$, on which $\psi$ is negative definite (Hodge index theorem, $h^2>0$). Since $d\ge2$, such a $\sigma$ exists.

*Step 3.* By [La], $u=\gamma^m|_{\mathbb T_t}$ is unipotent for some $m$. Let $N=\log u$, a polynomial in $u-1$ with rational coefficients; it is $E$-linear. It is $\phi$-skew: $s\mapsto\phi(e^{sN}x,e^{sN}y)$ is a polynomial in $s$ that is constant on $\mathbb Z$, hence constant, and differentiating at $s=0$ gives skewness. Suppose $N\ne0$. Let $k\ge1$ be maximal with $N^k\ne0$, and $w=N^kx\ne0$. Then $\phi(w,w)=(-1)^k\phi(x,N^{2k}x)=0$. Take $\sigma\neq\sigma_1$ from Step 2: $\psi(w\otimes1,w\otimes1)=\sigma(\phi(w,w))=0$ forces $w\otimes1=0$ in $T_\sigma$. But $\mathbb T_t\to T_\sigma$ is injective, because $\mathbb T_t$ is a free $E$-module. This is a contradiction, so $u=1$.

*Step 4.* On $\mathbb T^\perp$, $\gamma$ preserves the lattice $\mathbb T^\perp\cap H^2(S_t,\mathbb{Z})$, fixes $h$, and preserves the negative definite form on $h^\perp\cap\mathbb T^\perp$. So it has finite order there too. $\square$

**Corollary C.1.** In every one-parameter degeneration of K3 surfaces with RM by $E\neq\mathbb{Q}$, the monodromy on $H^2(S_t)$ and on $H^*(S_t\times S_t)$ has finite order. After base change $N=0$, so the limit mixed Hodge structure is pure, and a Kulikov model is of type I [Ku, PP]: there are no type II or III degenerations. Every mechanism that reads an obstruction off the non-trivial weight-graded or combinatorial part of a limit (tropical limits, matroidal EdGFS-type arguments, Kontsevich's program) therefore has no input on K3. Theorem A still applies; when a smooth projective K3 model exists, it only moves the RM class to the square of another RM K3 surface.

**Remark C.2 (projectivity is used).** Step 2 needs a class $h$ of type $(1,1)$ with $h^2>0$ that is orthogonal to $\mathbb T$. For non-projective K3 surfaces, $\mathbb T$ can contain a positive $(1,1)$-direction, and for $d=2$ the argument breaks down.

## 5. Galois conjugation and absoluteness (Proposition D)

A Hodge class $\alpha$ is *absolute Hodge* if, for every $\sigma\in\mathrm{Aut}(\mathbb{C})$, the conjugate of its de Rham and adelic components is again a rational Hodge class on $X^\sigma$ [De1, §2]. Algebraic classes are absolute Hodge. So a Hodge class with a non-Hodge conjugate would be a counterexample.

**Proposition D.** In each of the following cases every Hodge class is absolute Hodge, so the Galois mechanism is void:

* (D1) abelian varieties [De1, Thm 2.11];
* (D2) products of K3 surfaces and abelian varieties, in particular all RM classes on $S\times S$: K3 motives lie in the category generated by abelian varieties [An2], via Kuga–Satake [De0];
* (D3) Fermat hypersurfaces and their products (Deligne [De1]; see also [An3]; via Shioda–Katsura). The underlying argument: the Shioda–Katsura morphism $\tilde\varphi$ from a blow-up of $X^r_m\times X^s_m$ to $X^{r+s}_m$ is generically finite and surjective, so $\alpha=\frac1{\deg\tilde\varphi}\tilde\varphi_*\tilde\varphi^*\alpha$. The blow-up formula is given by algebraic correspondences. By induction, every Hodge class is the image under an algebraic correspondence of a Hodge class on a product of Fermat curves;
* (D4) (*proved here*) sextic fourfolds. Let $S$ be a smooth connected variety, $\mathcal X\to S$ a family of smooth sextic fourfolds, and $\alpha\in H^0(S,R^4\pi_*\mathbb{Q})$ a section that is Hodge at every point. Suppose $\alpha_{s_0}$ is algebraic for one $s_0$; this holds, for example, if $s_0$ maps to the Fermat sextic, where HC is known (Shioda 1979, $m=6\le20$; reconfirmed in `results/README.md`). Then every $\alpha_s$ is absolute Hodge.

*Proof of (D4).* $\alpha_{s_0}$ is algebraic, hence absolute Hodge. By Deligne's Principle B [De1, Thm 2.12], a global flat section that is Hodge everywhere and absolute at one point is absolute everywhere. $\square$

By Remark 2.3, every irreducible component of the Hodge locus through the Fermat point, with any branch of the class, gives such an $S$: resolve the component and pass to a finite étale cover. Since the universal family of sextics is defined over $\mathbb{Q}$, such components are then defined over $\overline{\mathbb Q}$ [Vo2]. For K4 the mechanism could therefore only act at (i) zero-dimensional components (special points, the hard core C3 of docs/03), or (ii) positive-dimensional components through no point where HC is known. By [BKU] the positive-period-dimension Hodge locus of sextic fourfolds is a *finite* union of special subvarieties ($n=4$, $d=6$ is in their range). By [KOU], components satisfying a monodromy condition are defined over $\overline{\mathbb Q}$.

## 6. Reduction modulo $p$ (Proposition E, Theorem E4)

**Setting 6.1.** $X$ is smooth projective over a number field $F\subset\mathbb{C}$, and $v$ is a finite place of good reduction with residue characteristic $p$. $X_0$ is the reduction over $\overline{\mathbb F}_v$, and $\ell\ne p$. Comparison followed by smooth proper base change gives
$$\mathrm{sp}\colon H^k(X(\mathbb{C}),\mathbb{Q})\otimes\mathbb{Q}_\ell\xrightarrow{\ \sim\ }H^k_{et}(X_0,\mathbb{Q}_\ell),$$
compatible with cup products, trace maps and Tate twists. $\mathcal Z^k(X_0)\subseteq H^{2k}_{et}(X_0,\mathbb{Q}_\ell(k))$ denotes the $\mathbb{Q}$-span of cycle classes.

**Proposition E.**

* (E1) [De1, 2.9] If $\alpha$ is absolute Hodge, then $\mathrm{sp}(\alpha)$ is a Tate class. Indeed, the absolute Hodge classes form a finite-dimensional $\mathbb{Q}$-space on which $\mathrm{Gal}(\overline{\mathbb Q}/F)$ acts through a finite quotient. Inertia at $v$ acts trivially on $H_{et}$, the decomposition group surjects onto $\mathrm{Gal}(\overline{\mathbb F}_v/\mathbb F_v)$, and $\mathrm{sp}$ is equivariant. So, wherever Proposition D applies, the "Tate-class" test is void.
* (E2) (*standard; proved here*) If $\alpha$ is algebraic, then $\mathrm{sp}(\alpha)\in\mathcal Z^p(X_0)$. In particular $\int_{X_0}\mathrm{sp}(\alpha)\cup z\in\mathbb{Q}$ for all $z\in\mathcal Z^{n-p}(X_0)$, and this number does not depend on $\ell$.
* (E3) Let $X=S\times S$ with $S$ a K3 surface, and $p\ge5$. The Tate conjecture holds for $S_0\times S_0$ [IIK; Ya]. Together with (E1) and (D2), this gives $\mathrm{sp}(\alpha)\in\mathcal Z^2(S_0\times S_0)\otimes\mathbb{Q}_\ell$ for every RM class $\alpha$. Only the *rationality* part of (E2) is left as a possible obstruction.

*Proof of (E2).* Write $\alpha=\mathrm{cl}(z)$. The components of the Chow varieties of $X$ are defined over $\overline{\mathbb Q}$, and cycle classes are locally constant in connected families, so $z$ can be chosen defined over a finite extension $F'$. Then $\alpha\otimes1=\mathrm{cl}_\ell(z)$ [SGA4½, Cycle], and $\mathrm{sp}\,\mathrm{cl}_\ell(z)=\mathrm{cl}_\ell(\bar z)$ for Fulton's specialization $\bar z$ over $\mathcal O_{F',w}$ [Fu, §20.3]. Intersection numbers of cycles on $X_0$ are degrees of $0$-cycles: rational and independent of $\ell$. $\square$

**Setting 6.2 (Weil classes).** Let $(A,\iota,E)$ be as in 3.1, all defined over $F$, and write $V^\vee=H^1(A,\mathbb{Q})$. Over $\mathbb{C}$, $V^\vee_\mathbb{C}=V^\vee_\sigma\oplus V^\vee_{\bar\sigma}$ is the eigenspace decomposition for $\iota(a)^*$, with eigenvalues $\sigma(a)$ and $\bar\sigma(a)$, each of dimension $2n$. The space $W_\mathbb{C}=\bigwedge^{2n}V^\vee_\sigma\oplus\bigwedge^{2n}V^\vee_{\bar\sigma}$ is defined over $\mathbb{Q}$, and $W:=W_\mathbb{C}\cap H^{2n}(A,\mathbb{Q})$ is Weil's 2-dimensional space of Hodge classes [We]. Define $\kappa(a)$ to act on $W$ by $\sigma(a)$ on the first summand and by $\bar\sigma(a)$ on the second. It is defined over $\mathbb{Q}$ and makes $W$ a $K$-line, and $\iota(a)^*|_W=\kappa(a^{2n})$. Let $\mathcal D^k(A_0)\subseteq H^{2k}_{et}(A_0,\mathbb{Q}_\ell(k))$ be the $\mathbb{Q}$-span of products of $k$ divisor classes. Write $W_\ell=\mathrm{sp}(W)\otimes\mathbb{Q}_\ell$ and $K_\ell=K\otimes\mathbb{Q}_\ell$. Twists are suppressed.

**Theorem E4 (proved here).** In Setting 6.2, suppose $A_0$ is supersingular, i.e. the Frobenius eigenvalues are $\sqrt q$ times roots of unity.

* (a) For all $k$, $\mathcal D^k(A_0)\otimes\mathbb{Q}_\ell\to H^{2k}_{et}(A_0,\mathbb{Q}_\ell(k))$ is an isomorphism, the intersection pairing $\mathcal D^k\times\mathcal D^{2n-k}\to\mathbb{Q}$ is perfect, and $\mathcal Z^k(A_0)=\mathcal D^k(A_0)$.
* (b) $W_0:=W_\ell\cap\mathcal D^n(A_0)$ is a $K$-line (via $\kappa$) that spans $W_\ell$ over $K_\ell$. Hence $W_0=\kappa(\lambda_v)\,\mathrm{sp}(W)$ for some $\lambda_v\in K_\ell^\times$, well defined modulo $K^\times$, and $\nu:=N_{K_\ell/\mathbb{Q}_\ell}(\lambda_v)\in\mathbb{Q}^\times$.
* (c) If the Weil classes of $A$ are algebraic, then $\lambda_v\in K^\times$. Consequently $(-1)^n\int_{A_0}w_0\cup w_0>0$ for every $0\ne w_0\in W_0$ (this inequality is in fact unconditional: $W_0$ consists of primitive Lefschetz classes [Mi3, Rem. 3.7]).

So exhibiting $(A,v)$ with $\lambda_v\notin K^\times$ would disprove HC. (The inequality $(-1)^n\int w_0^2>0$ always holds [Mi3, Rem. 3.7].)

*Proof.* (a) *Surjectivity.* Pass to a finite field of definition $\mathbb F_q$ and enlarge $q$. Frobenius $\pi$ is semisimple [Ta], with eigenvalues $\sqrt q\,\zeta$, so after replacing $q$ by a power, $\pi=\sqrt q\cdot\mathrm{id}$ on $H^1$. Hence $\pi$ acts trivially on $H^2(A_0,\mathbb{Q}_\ell(1))$, and Tate's theorem [Ta] gives $NS(A_0)\otimes\mathbb{Q}_\ell=H^2(A_0,\mathbb{Q}_\ell(1))$. Since $\bigwedge^{2k}H^1$ is spanned by products of elements of $\bigwedge^2H^1$, the map is onto.

*Perfectness and injectivity.* $\mathcal D^k$ is finite-dimensional. Take $\mathbb{Q}$-bases $(d_i)$ of $\mathcal D^k$ and $(e_j)$ of $\mathcal D^{2n-k}$, and let $M=(\langle d_i,e_j\rangle)$, a matrix of intersection numbers, so $M$ is rational. If $c\in\mathbb{Q}^{\#i}$ satisfies $cM=0$, then $\sum c_id_i$ pairs to zero with all $e_j$, hence with all of $H^{4n-2k}$ by surjectivity. So $\sum c_id_i=0$ by Poincaré duality, and $c=0$. The symmetric argument shows $M$ is square and invertible over $\mathbb{Q}$. A $\mathbb{Q}_\ell$-relation $\sum c_id_i=0$ gives $cM=0$, hence $c=0$: injectivity.

*$\mathcal Z^k=\mathcal D^k$.* Any $z\in H^{2k}$ can be written $z=\sum c_id_i$ with $c\,M=(\langle z,e_j\rangle)_j$. If $z$ is a cycle class, the right-hand side consists of intersection numbers of cycles, so it is rational, and then $c=(\langle z,e_j\rangle)_jM^{-1}\in\mathbb{Q}^{\#i}$.

(b) *The kernel description.* Choose $a\in K$ with $\bar a/a$ not a root of unity, for instance a generator of $\mathfrak p^h$ for a prime $\mathfrak p$ above a rational prime that splits in $K$, where $h$ is the class number. Then $a^{2n}\notin\mathbb{Q}$, so $\mathbb{Q}[a^{2n}]=K$. The semisimple operator $\iota(a)^*$ has eigenvalue $\sigma(a)^i\bar\sigma(a)^{2n-i}$ on $\bigwedge^iV^\vee_\sigma\otimes\bigwedge^{2n-i}V^\vee_{\bar\sigma}$, and the eigenvalues with $0<i<2n$ differ from $\sigma(a)^{2n}$ and $\bar\sigma(a)^{2n}$. So $W=\ker P(\iota(a)^*)$, where $P\in\mathbb{Q}[x]$ is the minimal polynomial of $a^{2n}$.

*$W_0$ is a $K$-line.* $\iota$ reduces to endomorphisms of $A_0$, and $\iota(a)^*$ preserves $\mathcal D^\bullet(A_0)$, being a ring map that sends divisors to divisors. By (a), $W_0=\ker\big(P(\iota(a)^*)|_{\mathcal D^n}\big)$ is therefore a $\mathbb{Q}$-form of $\ker P(\iota(a)^*)|_{H^{2n}_\ell}=W_\ell$. It is stable under $\kappa(a^{2n})$, hence under $\kappa(K)$, so it is a $K$-line; so is $\mathrm{sp}(W)$. Since $W_\ell$ is free of rank one over $K_\ell$, $W_0=\kappa(\lambda_v)\mathrm{sp}(W)$ with $\lambda_v$ unique up to $K^\times$.

*The norm.* Let $b(x,y)=\int x\cup y$. Since $\bigwedge^{2n}V^\vee_\sigma\cup\bigwedge^{2n}V^\vee_\sigma\subseteq\bigwedge^{4n}V^\vee_\sigma=0$, $b$ pairs the $\sigma$-part with the $\bar\sigma$-part. Hence $b(\kappa(c)x,y)=b(x,\kappa(\bar c)y)$, and $b(\kappa(c)x,\kappa(c)x)=N(c)\,b(x,x)$ for $c\in K_\ell$. Weil classes are primitive: $\iota(a)^*\theta=N(a)\theta$ forces $\theta\in V^\vee_\sigma\otimes V^\vee_{\bar\sigma}$, and $\theta\cup\bigwedge^{2n}V^\vee_\sigma=0$. They have type $(n,n)$, so the Hodge–Riemann relations give $(-1)^nb(w,w)>0$ for $0\ne w\in W$. With $w_1\in\mathrm{sp}(W)\smallsetminus0$ and $w_0=\kappa(\lambda_v)w_1$ we get $N(\lambda_v)\,b(w_1,w_1)=b(w_0,w_0)$. Here $b(w_1,w_1)\in\mathbb{Q}^\times$ is a Betti intersection number and $b(w_0,w_0)\in\mathbb{Q}$ is an intersection number of Lefschetz classes, so $\nu\in\mathbb{Q}^\times$.

(c) If $W$ is algebraic, then by (E2) and (a), $\mathrm{sp}(W)\subseteq\mathcal Z^n=\mathcal D^n$. So $\mathrm{sp}(W)=W_0$ (both are 2-dimensional), i.e. $\lambda_v\in K^\times$, and the sign follows from Hodge–Riemann on $A$. $\square$

**Remarks E5.**

1. *The norm is controlled by the sign.* $W_0$ is the kernel of $P(\iota(a)^*)$ on products of divisors modulo numerical equivalence, which by (a) agrees with $\ell$-adic homological equivalence. So $W_0$, and the rational number $\nu$, do not depend on $\ell$. Hence $\nu$ is a norm from $K_\ell$ for every $\ell\ne p$. By Hilbert reciprocity and the Hasse norm theorem, $\nu\in N(K^\times)$ if and only if $\nu>0$, i.e. if and only if the sign condition of (c) holds. Since the sign condition holds unconditionally [Mi3, Rem. 3.7], $[\lambda_v]$ can be normalized into $T^1(\mathbb{Q}_\ell)/T^1(\mathbb{Q})$ with $T^1=\ker N$. This group is infinite, so nothing forces $[\lambda_v]=1$ a priori.
2. *Relation to known conjectures.* The sign condition is the instance, for $W_0$, of Grothendieck's Hodge standard conjecture on $A_0$; since $W_0$ consists of Lefschetz classes it is a theorem [Mi3, Remark 3.7]. The statement "$[\lambda_v]=1$ for all CM $(A,v)$" is equivalent, by (a), to the Weil-class, supersingular case of Milne's rationality conjecture [Mi2] ("the specialization of a Hodge class has rational intersection numbers with Lefschetz classes"). That conjecture is open [Mi2, Mi4]. It holds whenever HC is known for $A$: all abelian fourfolds, and split sixfolds [Ma2].
3. *Hypotheses.* E4 needs a supersingular place but not CM. For CM abelian varieties, supersingular places are expected to be plentiful (Shimura–Taniyama), but I have not checked their existence for a specific non-split CM sixfold.

## 7. Structural reductions (Propositions F, G, H)

**Proposition F (where an abelian counterexample would have to come from).**

* (F1) (*known in substance; proof here*) Let $A$ be a complex abelian variety with a non-algebraic $\alpha\in\mathrm{Hdg}^p(A)$. Then either some CM abelian variety carries a non-algebraic Hodge class, or the variational Hodge conjecture fails for a polarized abelian scheme over a connected Shimura variety.
* (F2) [An1; Mi1] Hodge classes on CM abelian varieties are generated by divisor classes and *split* Weil classes: the groups fixing the two sets of classes coincide [Mi1, Thm 2]. So a CM counterexample yields a non-algebraic split Weil class on some CM abelian variety of split Weil type, possibly of large dimension.
* (F3) [An3; Mi1] The Lefschetz standard conjecture $B$ for all smooth projective varieties implies HC for abelian varieties. Hence a counterexample in K1 or K2 forces $B$ to fail on some smooth projective variety, which cannot be an abelian variety (Lieberman [Li]).

*Proof of (F1).* Let $G=MT(A)$, and let $X_G$ be the $G(\mathbb{R})$-orbit of the Hodge cocharacter of $A$. Then $(G,X_G)$ is a Shimura datum of Hodge type. For a neat arithmetic $\Gamma\subset G(\mathbb{Q})$ preserving a lattice and the polarization, $S=\Gamma\backslash X_G^+$ is a smooth connected quasi-projective variety carrying a polarized abelian scheme $\mathcal A\to S$ with $A$ as a fibre (Baily–Borel; Borel's extension theorem). The class $\alpha$ is $G$-invariant, hence $\Gamma$-invariant, so it is a global flat section. It is Hodge at every point, because every $h\in X_G$ factors through $G_\mathbb{R}$. Special points are dense in $S$ [Mi5], and at a special point $s$ the group $MT(A_s)$ is a torus, i.e. $A_s$ is CM. If $\alpha_s$ is not algebraic, we are in the first alternative. If it is, the family $(\mathcal A\to S,\alpha)$ violates the variational Hodge conjecture. $\square$

**Proposition G (Voisin's positivity mechanism has no projective analogue; proved here).** Voisin's tori [Vo1] carry Weil classes that are not Chern classes of any coherent analytic sheaf. The reason is that, in the absence of $(1,1)$-classes, the Chern classes of all sheaves satisfy a Bogomolov–Lübke-type positivity that Weil classes violate. On a projective $X$ with ample $H$ and any Kähler class $\omega$, take $E=\bigoplus_{i=1}^p\mathcal O(a_iH)$ with $a_i\in\mathbb{Z}$. Then $c_p(E)=(\prod_i a_i)H^p$, so $\int c_p(E)\,\omega^{n-p}$ takes all integer multiples of $\int H^p\omega^{n-p}>0$, of both signs. Hence no constraint of the form "$c_p$ of every sheaf lies in a closed salient cone" can hold on a projective variety. This is precisely where projectivity (C2 of docs/03) removes the mechanism.

**Proposition H (coniveau; classical).**

* (H1) For a Hodge class $\alpha$, $\mathbb{Q}\alpha$ is a sub-HS of level $0$. Grothendieck's mechanism (a rational subspace of $F^c$ that is not a sub-HS) therefore never applies to it.
* (H2) $\alpha\in\mathrm{Hdg}^p(X)$ is algebraic if and only if $\alpha|_{X\smallsetminus Z}=0$ for some closed $Z$ of codimension $\ge p-1$.

*Proof of (H2), "if".* By Deligne's weights [De2, §8], $\ker\big(H^{2p}(X)\to H^{2p}(X\smallsetminus Z)\big)$ is spanned by Gysin images from resolutions $\tilde Z_i$ of the components of $Z$. Components of codimension $\ge p$ contribute fundamental classes. For codimension $p-1$ the contribution is the image of a morphism of HS $H^2(\tilde Z_i)(1-p)\to H^{2p}(X)$. By semisimplicity, $\alpha$ minus its algebraic part lifts to Hodge classes in $H^2(\tilde Z_i)$, which are algebraic by Lefschetz $(1,1)$. $\square$

So any coniveau obstruction is HC itself; there is no Hodge-theoretic intermediate step.

*Bloch–Beilinson.* The conjectural Bloch–Beilinson filtration constrains $\ker(\mathrm{cl})$, not its image. Its one unconditional consequence for HC, Bloch–Srinivas, is a *sufficient* condition for HC (small $CH_0$). All candidates K1–K5 have $h^{n,0}\neq0$ or a large $CH_0$, so it neither proves nor obstructs anything here.

## 8. Verdict, candidate by candidate

"Void" means proved void in this file or by the cited theorem; "open" means not shown void.

| mechanism | K1 non-split Weil (dim 6) | K2 exceptional non-Weil | K3 RM on $S\times S$ | K4 sextic NL | K5 Fermat |
|---|---|---|---|---|---|
| Galois / absoluteness | void (D1) | void (D1) | void (D2) | void on components through a point with known HC, e.g. the Fermat point (D4); open at special points | void (D3) |
| specialization (Kollár type), rational | void for degenerations with $\operatorname{rk}N\in\{2,4\}$ (B.2, A.4, cond. G3); $\operatorname{rk}N=0$ uninformative | void when the abelian part has $\dim\le5$ (A.4); otherwise reduces to a smaller abelian variety | uninformative: finite monodromy (C, C.1) | reduces to HC on components (A, A.2) | reduces to HC on components (A) |
| tropical / maximal degeneration | no MUM degeneration exists (B) | rationally void when MUM exists (A.4) | no type II/III (C.1) | reduces to (A) | reduces to (A) |
| char $p$: Tate-class test | void (E1) | void (E1) | void (E1, E3) | void where (D4) applies | void (E1) |
| char $p$: **rationality test** | **open**: $[\lambda_v]$ of E4 | **open** (Milne) | **open** (E3) | open | **open** |
| positivity (Voisin type) | void (G) | void (G) | void (G) | void (G) | void (G) |
| coniveau / GHC | equivalent to HC (H) | equivalent to HC | equivalent to HC | equivalent to HC | equivalent to HC |
| Lefschetz $B$ on $X$ | holds [Li]; a counterexample forces $B$ to fail elsewhere (F3) | same | holds (products of surfaces) | holds (hypersurfaces) | holds |

**Conclusion of the attack.** On the five candidate families every mechanism on the list is void with $\mathbb{Q}$-coefficients, reduces to HC on a smaller or simpler variety, or is equivalent to HC itself. The one exception is the **rationality test in characteristic $p$**. For Weil classes it is the class $[\lambda_v]$ of Theorem E4: a rational, computable-in-principle invariant that HC forces to be trivial, and for which I know no a priori reason to be trivial (Remark E5.1).

## 9. GAPS

**G1 (the missing step for a counterexample). Statement S.** *There exist a non-split abelian sixfold of Weil type $(A,\iota,E)$ ($\operatorname{disc}\ne-1$) over a number field, a place $v$ of supersingular good reduction, and $\ell\ne p$, such that $\lambda_v\notin K^\times$ (Theorem E4).*

S would disprove HC, by E4(c). It is needed because the rationality test is the only mechanism on the list that I could not show to be void (§8).

I can prove neither S nor its negation. Computing $\lambda_v$ requires comparing two $\mathbb{Q}$-structures on the $K_\ell$-line $W_\ell$: the Betti one, and the one cut out by $\mathrm{End}^0(A_0)\cong M_6(D_{p,\infty})$ through divisor classes. For CM $A$, the theory of complex multiplication (Shimura–Taniyama) controls the comparison of the $\ell$-adic and adelic structures, but I have no formula for the relative position of these two *rational* structures. Their compatibility is exactly Milne's weak rationality conjecture [Mi2, Conj. 4.4, Remarks 4.6–4.7]. The negation of S for CM $A$ is a case of Milne's rationality conjecture [Mi2].

What is known about $\lambda_v$:

* $N(\lambda_v)\in N(K^\times)$ always (Remark E5.1 together with [Mi3, Rem. 3.7]);
* $[\lambda_v]=1$ whenever HC is known for $A$, in particular for split sixfolds [Ma2];
* by (F2), for CM $A$ the Weil classes are generated by split Weil classes on other CM abelian varieties. Their reductions face the same rationality question, so nothing known excludes S.

**G2 (Theorem A is a reduction, not a vanishing theorem).** For a general degeneration I do not know HC on the components $\tilde E_l$. Theorem A only shows that a rational obstruction must come from a counterexample there: a Hodge class restricted from the total space.

**G3 (models).** Corollaries A.4 and B.2 assume that, after a finite base change, there is a projective model over a curve with smooth total space whose special-fibre components are toric-variety bundles, as in Lemma A.3, over abelian varieties isogenous to the abelian part. Over complete DVRs this is Mumford's construction with Künnemann's projective regular models [Kü]. Algebraic families over curves in toroidal compactifications come from [FC, VI]. I have not checked that these satisfy *exactly* the hypotheses of Lemma A.3 (Zariski-local triviality of the torsor, smooth projective toric fibres) in every case.

**G4 (K2).** I have no classification of exceptional non-Weil classes in dimension $\ge6$. The analogue of Theorem B for K2 (bounding $\operatorname{rk}N$ by the $\mathbb{Q}$-rank of the generic Mumford–Tate group) is not worked out. Only the general statements D1, A.4, E1, E2 and F apply.

**G5 (K4).** Absoluteness on components of the sextic Hodge locus that pass through no point with known HC, and in particular at zero-dimensional components, is open (docs/03, C3). I did not identify an explicit component of either kind.

**G6 (K5).** I did not evaluate the rationality test for the indecomposable Fermat characters of `results/README.md`. By (D3) and (F2), a counterexample there would produce one on a product of Fermat Jacobians, which are CM.

**G7 (quoted, not re-proved).** The global invariant cycle theorem and the theorem of the fixed part [De2]; the monodromy theorem [La]; limit mixed Hodge structures [Sc]; absoluteness and Principle B [De1]; [An1–An3]; [Mi1–Mi5]; [Ta]; [IIK, Ya]; [Ma1–Ma3]; [Ku, PP]; Meyer's theorem [Se]; [Za]; [BKU, KOU, Vo2]; [Kü, FC]; the cycle-theoretic compatibilities in [Fu] and [SGA4½].

**G8 (literature checking).** The session's web-search budget ran out part way through. I read the abstracts of arXiv:2609.14169, 2502.03415, 2509.23403, 2507.15704, 2107.08838 and 2010.03359 directly on arxiv.org. Ito–Ito–Koshikawa, Milne's rationality conjecture and its open status [Mi2, Mi4], and Milne's account of André's results [Mi1] were checked only through search-engine summaries. Theorem numbers in [De1] (2.9, 2.11, 2.12), [De2] (4.1.1, 4.1.2, §8) and [Sc] (6.16) are quoted from memory.

## 10. Checklist (docs/03, §3.4)

**Where rational coefficients are essential.**

* *Theorem A.* Step (1) uses the global invariant cycle theorem and semisimplicity, both over $\mathbb{Q}$. Integrally only some multiple $N\alpha$ lifts (Remark 2.2), and this is exactly the room in which the Kollár and EdGFS counterexamples live. Would the argument prove the integral HC? No. An integral version of Corollary A.4 would assert that the minimal curve class of a very general principally polarized abelian variety specializes to an *integral* algebraic class on a maximal degeneration. That is not claimed: the proof needs $\mathbb{Q}$ in step (1). So there is no conflict with EdGFS.
* *Theorems B and C* are about forms over $\mathbb{Q}$ and over $E$: Meyer's theorem, and anisotropy at a real place.
* *E2 and E4* are by design a $\mathbb{Q}$-versus-$\mathbb{Q}_\ell$ rationality statement. No integral refinement is used.

**Where projectivity is essential.**

* *Theorem A* needs a smooth projective total space, for the invariant cycle theorem and for polarizability. Its conclusion is conditional on HC for the components. For Kähler families the same proof would only reduce to the Kähler HC on the components, which is false, so it yields no false statement.
* *Theorem B* needs the polarization to define $H$; non-polarizable tori of Weil type, such as Voisin's, are outside its scope.
* *Theorem C* uses an ample class in Step 2 (Remark C.2).
* *Proposition E* concerns reductions of projective varieties over number fields, and uses Tate's theorems.
* *(F1)* uses the algebraicity of Shimura varieties and of their universal families.
* *Proposition G* uses ample line bundles, which is exactly what Voisin's tori lack.

**Does anything prove too much?** No result here asserts the algebraicity of a class that was not already known to be algebraic.

* A, A.2, A.4 and B.2 are conditional reductions.
* B, C and E4(a,b) are structural statements.
* D and E1 are known absoluteness results.
* E2, E4(c), F and H are necessary conditions or reductions.
* G shows that a certain kind of constraint cannot exist.

So nothing here implies the integral HC or the Kähler HC.

**The other items of §3.4.**

* Absoluteness: used, not proved (D).
* Lefschetz $B$: (F3).
* Variational HC: (F1) shows that abelian counterexamples come from CM counterexamples or from failures of VHC.
* Open special cases: none of them is settled here.

## 11. References

* [An1] Y. André, *Une remarque à propos des cycles de Hodge de type CM*, Sém. Théorie des Nombres Paris 1989–90, Progr. Math. 102 (1992), 1–7.
* [An2] Y. André, *On the Shafarevich and Tate conjectures for hyperkähler varieties*, Math. Ann. 305 (1996), 205–248.
* [An3] Y. André, *Pour une théorie inconditionnelle des motifs*, Publ. Math. IHÉS 83 (1996), 5–49.
* [BKU] G. Baldi, B. Klingler, E. Ullmo, *On the distribution of the Hodge locus*, arXiv:2107.08838.
* [Cl] C. H. Clemens, *Degeneration of Kähler manifolds*, Duke Math. J. 44 (1977), 215–290.
* [De0] P. Deligne, *La conjecture de Weil pour les surfaces K3*, Invent. Math. 15 (1972), 206–226.
* [De1] P. Deligne (notes by J. S. Milne), *Hodge cycles on abelian varieties*, LNM 900 (1982), 9–100.
* [De2] P. Deligne, *Théorie de Hodge II*, Publ. Math. IHÉS 40 (1971), 5–57.
* [EdGFS] P. Engel, O. de Gaay Fortman, S. Schreieder, *Matroids and the integral Hodge conjecture for abelian varieties*, arXiv:2507.15704.
* [FC] G. Faltings, C.-L. Chai, *Degeneration of abelian varieties*, Springer 1990.
* [Fl] W. Fulton, *Introduction to toric varieties*, Princeton 1993.
* [Fu] W. Fulton, *Intersection theory*, 2nd ed., Springer 1998.
* [IIK] K. Ito, T. Ito, T. Koshikawa, *CM liftings of K3 surfaces over finite fields and their applications to the Tate conjecture*, Forum Math. Sigma 9 (2021), e29; arXiv:1809.09604.
* [KOU] B. Klingler, A. Otwinowska, D. Urbanik, *On the fields of definition of Hodge loci*, Ann. Sci. ENS 56 (2023); arXiv:2010.03359.
* [Ko] J. Kollár, *Trento examples*, LNM 1515 (1992), 134–135.
* [Ku] V. Kulikov, *Degenerations of K3 surfaces and Enriques surfaces*, Math. USSR Izv. 11 (1977), 957–989.
* [Kü] K. Künnemann, *Projective regular models for abelian varieties, semistable reduction, and the height pairing*, Duke Math. J. 95 (1998), 161–212.
* [La] A. Landman, *On the Picard–Lefschetz transformation for algebraic manifolds acquiring general singularities*, Trans. AMS 181 (1973), 89–126.
* [Li] D. Lieberman, *Numerical and homological equivalence of algebraic cycles on Hodge manifolds*, Amer. J. Math. 90 (1968), 366–374.
* [Ma1] E. Markman, JEMS 25 (2023), 231–321. [Ma2] E. Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*, arXiv:2502.03415. [Ma3] E. Markman, *Secant sheaves and Weil classes on abelian varieties*, arXiv:2509.23403.
* [Mi1] J. S. Milne, *Hodge classes on abelian varieties*, arXiv:2010.08857. [Mi2] J. S. Milne, *Rational Tate classes*, Moscow Math. J. 9 (2009); arXiv:0707.3167. [Mi3] J. S. Milne, *Polarizations and Grothendieck's standard conjectures*, Ann. of Math. 155 (2002), 599–610. [Mi4] J. S. Milne, *The Tate conjecture over finite fields (AIM talk)*, arXiv:0709.3040. [Mi5] J. S. Milne, *Introduction to Shimura varieties* (density of special points).
* [PP] U. Persson, H. Pinkham, *Degeneration of surfaces with trivial canonical bundle*, Ann. of Math. 113 (1981), 45–66.
* [Sc] W. Schmid, *Variation of Hodge structure: the singularities of the period mapping*, Invent. Math. 22 (1973), 211–319.
* [Se] J.-P. Serre, *A course in arithmetic*, Springer 1973 (Ch. IV: Hasse–Minkowski, Meyer).
* [SGA4½] P. Deligne et al., *Cohomologie étale*, LNM 569 (1977), exposé "Cycle".
* [Ta] J. Tate, *Endomorphisms of abelian varieties over finite fields*, Invent. Math. 2 (1966), 134–144.
* [Vo1] C. Voisin, *A counterexample to the Hodge conjecture extended to Kähler varieties*, IMRN 2002. [Vo2] C. Voisin, *Hodge loci and absolute Hodge classes*, Compositio Math. 143 (2007), 945–958.
* [We] A. Weil, *Abelian varieties and the Hodge ring*, Collected Papers III (1977), 421–429.
* [Ya] Z. Yang, *The Tate conjecture for motivic endomorphisms of K3 surfaces over finite fields*, arXiv:2110.01350 ($p\ge5$).
* [Za] Yu. G. Zarhin, *Hodge groups of K3 surfaces*, J. reine angew. Math. 341 (1983), 193–220.
* arXiv:2609.14169, *Discriminants of Hermitian forms, maximal degenerations and Kontsevich's tropical approach to the Hodge conjecture* (2026).

## 12. Claimed results

| label | one-line statement | status |
|---|---|---|
| Theorem A | The specialization of a flat family of Hodge classes is $\sum_l c_l\psi_{l*}PD(\gamma_l)$ with $\gamma_l$ Hodge on the components of a resolved special fibre, so a rational specialization obstruction requires a counterexample on a component | proved here (folklore-type statement, complete proof) |
| Remark 2.2 | $\mathbb{Q}$ enters only through the lifting step; integrally only $N\alpha$ lifts | proved here |
| Remark 2.3 | A class on a Hodge-locus curve becomes a global flat section after a finite base change | proved here |
| Corollary A.2 | If one smooth model has algebraic restrictions on all components, then $\mathrm{sp}(\alpha)$ is algebraic for every model | proved here |
| Lemma A.3 | For a toric-variety bundle $Y\to B$, $\mathrm{HC}(B)$ in degrees $\le p$ implies $\mathrm{HC}(Y,p)$ | proved here (standard) |
| Corollary A.4 | Rational EdGFS/Kollár-type obstructions vanish for abelian degenerations whose abelian part satisfies HC (maximal degenerations, or $\dim B\le5$) | proved here conditionally on G3 (existence of toric-bundle models) and on [Ma2] |
| Theorem B(1) | The Witt index of a Weil-type Hermitian form is $n$ iff $\operatorname{disc}=(-1)^n$, and $n-1$ otherwise | proved here |
| Theorem B(2) | $\operatorname{rk}N\le2\operatorname{ind}(H)$; maximal unipotent monodromy forces $\operatorname{disc}=(-1)^n$ | known (arXiv:2609.14169, Lemma 9 and Prop. 4); alternative proof here |
| Corollary B.1 | The abelian part of a degeneration is of Weil type with $\operatorname{disc}(B)=(-1)^{\operatorname{rk}N/2}\operatorname{disc}(A)$; non-split stays non-split | proved here |
| Corollary B.2 | Degenerations give no rational obstruction for non-split Weil sixfolds | proved here conditionally on G3 and [Ma2] |
| Theorem C | Families of projective K3 surfaces with RM by $E\ne\mathbb{Q}$ have finite local monodromy on $H^2$ | proved here (folklore in substance) |
| Corollary C.1 | RM K3 degenerations are of type I with pure limits; tropical mechanisms have no input | proved here, quoting [Ku, PP] for Kulikov models |
| Proposition D (D1–D3) | Hodge classes on abelian varieties, K3 products and Fermat varieties are absolute | known [De1, An2] |
| Proposition D (D4) | Sextic-fourfold Hodge classes in a family through a point with known HC (e.g. Fermat) are absolute | immediate from Principle B [De1, 2.12] and the known HC for the Fermat sextic fourfold |
| Proposition E (E1) | Absolute Hodge implies Tate after reduction | known [De1] |
| Proposition E (E2) | Algebraic implies that the reduction is in $\mathcal Z(X_0)_\mathbb{Q}$, with rational intersection numbers | proved here (standard ingredients) |
| Proposition E (E3) | Tate conjecture for $S_0\times S_0$ | known [IIK, Ya] |
| Theorem E4 | For Weil type with supersingular reduction there is an invariant $[\lambda_v]\in K_\ell^\times/K^\times$ with rational norm; HC implies $[\lambda_v]=1$ and a sign condition | proved here; the Weil-class, supersingular case of Milne's (weak) rationality conjecture [Mi2, §4], where the two $\mathbb{Q}$-structures are already described; the sign part is unconditional [Mi3, Rem. 3.7] |
| Remark E5.1 | $N(\lambda_v)$ is a global norm iff the sign condition holds | proved here |
| Proposition F (F1) | An abelian counterexample yields a CM counterexample or a failure of VHC over a Shimura variety | proved here (known in substance) |
| Proposition F (F2, F3) | Split Weil classes generate CM Hodge classes; Lefschetz $B$ implies HC for abelian varieties | known [An1, An3, Mi1] |
| Proposition G | No closed salient cone contains $c_p$ of all bundles on a projective variety | proved here (elementary) |
| Proposition H | Grothendieck's mechanism never applies to a Hodge class; HC is equivalent to coniveau $\ge p-1$ | known (classical; proof sketched) |
| Statement S | A non-split Weil sixfold and a supersingular place with $\lambda_v\notin K^\times$ (would be a counterexample) | **open** (G1) |
