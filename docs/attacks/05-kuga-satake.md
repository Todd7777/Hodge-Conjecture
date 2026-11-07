# Attack 05: Algebraicity of the Kuga–Satake correspondence

*Second run, 2026-11-07. Draft for adversarial refereeing. It does not prove the top target.*

## 0. Summary and honest status

**Top target (ladder (a)).** I want to show that for every projective K3 surface $S$ the Kuga–Satake class $\kappa_S\in H^4(S\times A\times A,\mathbb Q)$, $A=\mathrm{KS}(S)$, is algebraic. **I do not prove this.** §2 reduces it exactly to one statement, with complete proofs of the reduction (Theorem A, Corollaries A.1, A.2). The statement is the variational Hodge conjecture for the Kuga–Satake family over the moduli space $M_d$ of degree-$2d$ K3 surfaces, for each squarefree $d$. Equivalently, it is KS-HC for **one very general** K3 surface of each squarefree degree. It would follow from the Lefschetz standard conjecture $B$, or from HC for codimension-2 classes, on **one** smooth projective compactification $\bar{\mathcal X}_d$ of the total space, for each $d$. The argument stops at this algebraization step (GAPS G1–G3). Seeds of algebraicity are dense in $M_d$, but density cannot help (Remark 2.4).

**Ladder (b).** Theorem B is a complete, elementary classification of the rational transcendental lattices reachable through hyper-Kähler varieties of generalized Kummer type (Floccari's method). Every $T$ of rank $\le 5$ is reachable. A rank-6 $T$ (Picard rank $16$) is reachable iff its Witt index is $2$. That holds iff the even Clifford algebra $C^+(T)$ is split ($\cong M_4(K)$), which in turn holds iff $\mathrm{KS}(T)\sim B^4$ with $B$ an abelian fourfold. Combined with Floccari's theorem, this gives KS-HC for all $\rho\ge17$ and for $\rho=16$ in the split case (Corollary B.1). That consequence is **known in substance** (Floccari 2025); what I add is the exact boundary and its proof. The complementary class (Picard rank $16$, $C^+(T)\cong M_2(D)$ with $D$ a quaternion *division* algebra over an imaginary quadratic field) is nonempty (Example B.2). No method that transports KS-HC along Hodge similitudes can reach it from known cases (Proposition B.3). Specialization inside families with an imaginary-quadratic action on $T$ cannot reach it either (Proposition B.4). I propose it as the precise **first open case** at $\rho=16$.

**Ladder (c).** Corollary A.2 is a reduction of KS-HC for all K3 surfaces to $B$ or $\mathrm{HC}^2$ for the countably many varieties $\bar{\mathcal X}_d$. This is André's argument made explicit for a single variety. The reduction to an "explicit family of abelian or hyper-Kähler varieties" asked for in (c) is **not** achieved. Proposition B.5 and Remark 4.1 say why: any such reduction needs a variety with odd cohomology linked algebraically to $S$, and the only known hyper-Kähler examples, of Kummer type, have $b_2=7$.

`claimed_status`: **new_partial_result_only**. The new content consists of complete proofs of reductions, a classification, and obstructions. All of it is elementary given the cited theorems.

---

## 1. Set-up

Throughout, a *K3-type space* is a polarized rational Hodge structure $(V,q)$ of weight 2 with $h^{2,0}=1$ and $\dim V=n\ge3$. The form $q$ has signature $(2,n-2)$: it is positive on $(V^{2,0}\oplus V^{0,2})_{\mathbb R}$ and negative on $V^{1,1}_{\mathbb R}$. For a projective K3 surface $S$ with ample class $h$, both $h^\perp\subset H^2(S,\mathbb Q)$ and the transcendental space $T=T(S)_{\mathbb Q}:=NS(S)_{\mathbb Q}^\perp$ are K3-type spaces. Write $r=\operatorname{rk}T=22-\rho(S)$. Recall that $T(S)_{\mathbb Q}$ is the smallest rational subspace whose complexification contains $H^{2,0}(S)$.

**Kuga–Satake construction** [KS67, De72, vG00, Hu16 Ch. 4]. Let $C(V)$ be the Clifford algebra ($v^2=q(v)$) and $C^+(V)$ its even part. Choose an oriented orthonormal basis $e_1,e_2$ of the positive plane $P=(V^{2,0}\oplus V^{0,2})_{\mathbb R}$ with $e_1+ie_2\in V^{2,0}$. Put $J=e_1e_2$; it depends only on the oriented plane, and $J^2=-1$. Left multiplication by $J$ is a complex structure on $C^+(V_{\mathbb R})$, and for a lattice $\Lambda\subset C^+(V)$ the torus $\mathrm{KS}(V)=C^+(V_{\mathbb R})/\Lambda$ is an abelian variety with $H^1(\mathrm{KS}(V),\mathbb Q)=C^+(V)$. Right multiplications give $C^+(V)^{op}\subset\operatorname{End}^0(\mathrm{KS}(V))$.

Fix $v_0\in V$ with $q(v_0)\neq0$ and put $\psi_v(x)=v\,x\,v_0$ for $v\in V$, $x\in C^+(V)$.

**Lemma 1.1** (known [De72, vG00]). The map $\psi\colon V(1)\to\operatorname{End}(H^1(\mathrm{KS}(V),\mathbb Q))$ is an injective morphism of Hodge structures.

*Proof.* Injectivity: $\psi_v(1)=vv_0$, and $v_0$ is invertible. Let $H^{1,0}$ be the $i$-eigenspace of $J$.
- If $v\perp e_1,e_2$, then $v$ commutes with $e_1e_2$, so $\psi_v$ commutes with $J$ and has type $(0,0)$.
- If $v=e_1+ie_2$, then $e_1e_2v=iv$ and $ve_1e_2=-iv$. Hence $J\psi_v=i\psi_v$ and $\psi_vJ=-i\psi_v$. So $\psi_v$ kills $H^{1,0}$ and maps $H^{0,1}$ into $H^{1,0}$: it has type $(1,-1)$, which matches $V^{2,0}(1)=V(1)^{1,-1}$.
- The case $\bar v$ follows by conjugation. $\square$

Through a polarization $E$ of $A=\mathrm{KS}(V)$ we have $\operatorname{End}H^1(A)\cong H^1(A)\otimes H^1(A)(1)$. So $\psi$ becomes a morphism $V\to H^1(A)\otimes H^1(A)\subset H^2(A\times A,\mathbb Q)$. With Poincaré duality on $S$, applied to $\psi\circ\mathrm{pr}_V$ for $V\subset H^2(S,\mathbb Q)$, this gives a Hodge class
$$\kappa_S\in H^2(S,\mathbb Q)\otimes H^1(A,\mathbb Q)\otimes H^1(A,\mathbb Q)\subset H^4(S\times A\times A,\mathbb Q).$$

**Definition 1.2.** $\mathrm{KS\text{-}HC}(S)$ means that $\kappa_S$ is algebraic for $V=T(S)_{\mathbb Q}$, i.e. it is the class of a $\mathbb Q$-cycle of codimension 2. Equivalently, there is $\Gamma\in CH^2(S\times A\times A)_{\mathbb Q}$ such that $\Gamma_*|_{T}=\psi$ under the identifications above.

These are equivalent because Künneth projectors are algebraic on surfaces and on abelian varieties, and the identifications through $E$ are induced by divisor classes.

**Lemma 1.3** (independence of choices; known, cf. [vG00, Va23, Fl24]).
1. $\mathrm{KS\text{-}HC}(S)$ does not depend on $v_0$, $\Lambda$ or $E$.
2. It is equivalent to the algebraicity of the class built from $V'=H^2(S,\mathbb Q)$ with $v_0=h$, and to that built from $V=h^\perp$.
3. For any Hodge class $w$ in a K3-type space $V\subset H^2(S,\mathbb Q)$, the class $\kappa(w)\in H^2(A\times A)$ is algebraic.

*Proof.* (3) $\kappa(w)$ is a Hodge class of degree 2 on $A\times A$, so it is a divisor class by Lefschetz $(1,1)$. Also $w\in NS(S)_{\mathbb Q}$ is algebraic, so $w^\vee\otimes\kappa(w)$ is algebraic.

(1) Replacing $v_0$ by $v_0'$ composes $\psi$ with right multiplication by $c=v_0^{-1}v_0'\in C^+(V)$. This is a Hodge endomorphism of $H^1(A)$, hence an element of $\operatorname{End}(A)\otimes\mathbb Q$, induced by a $\mathbb Q$-combination of graphs. Changing $\Lambda$ is an isogeny. Changing $E$ composes with a Hodge automorphism of $H^1(A)$, again an element of $\operatorname{End}^0(A)$.

(2) Let $N=T^\perp\subset V'$, of type $(1,1)$ and dimension $m$. The graded tensor decomposition $C(V')=C(T)\hat\otimes C(N)$ gives
$$C^+(V')=C^+(T)\otimes C^+(N)\;\oplus\;C^-(T)\otimes C^-(N).$$
Fix $u\in T$ with $q(u)\ne0$. Right multiplication by $u$ is an isomorphism of left $C^+(T)$-modules $C^+(T)\to C^-(T)$ that commutes with $J$. Hence $H^1(\mathrm{KS}(V'))\cong H^1(\mathrm{KS}(T))\otimes_{\mathbb Q}C(N)$ as Hodge structures, with $C(N)$ a trivial multiplicity space, and so $\mathrm{KS}(V')\sim\mathrm{KS}(T)^{2^m}$.

For $v\in T$ and $x=a\otimes b$, we have $\psi'_v(a\otimes b)=va\otimes bh$. Under the identification just described (with $a''\in C^-(T)$ written as $a'u$), this equals $\psi^T_v\otimes R_h$ up to a nonzero scalar on each of the two summands, where $\psi^T_v(a)=vau$ and $R_h$ is right multiplication by $h$ on $C(N)$. Both the isogeny and $\mathrm{id}\otimes R_h$ (a matrix of scalars on $\mathrm{KS}(T)^{2^m}$) are algebraic. So $\kappa_{V'}|_T$ is algebraic iff $\kappa_T$ is. By (3), $\kappa_{V'}|_N$ is always algebraic. The case $V=h^\perp$ is the same argument. $\square$

**Lemma 1.4** (Buskin invariance; known in substance [Bu19], used in [Va23, Fl24]). Let $f\colon T(S)_{\mathbb Q}\to T(S')_{\mathbb Q}$ be a Hodge isometry. Then $\mathrm{KS\text{-}HC}(S)\iff\mathrm{KS\text{-}HC}(S')$.

*Proof.*
- **Extension to $H^2$.** Both $H^2(S,\mathbb Q)$ and $H^2(S',\mathbb Q)$ are isometric to $\Lambda_{K3}\otimes\mathbb Q$. By Witt cancellation $NS(S)_{\mathbb Q}\cong NS(S')_{\mathbb Q}$, so $f\oplus g$ is a Hodge isometry of $H^2$ for any isometry $g$ of the Néron–Severi spaces.
- **Algebraicity of $f$.** By Buskin's theorem [Bu19] every rational Hodge isometry $H^2(S,\mathbb Q)\to H^2(S',\mathbb Q)$ between projective K3 surfaces is algebraic. So $f$ is induced by an algebraic cycle.
- **Effect on Kuga–Satake varieties.** The algebra isomorphism $C(f)$ maps $J$ to $J'$. Indeed, $f(\sigma)=\lambda\sigma'$ with $\lambda\in\mathbb C^*$, so $f$ preserves the oriented positive planes, and $J$ depends only on that oriented plane. Hence $C^+(f)$ is an isomorphism of weight-1 Hodge structures, induced by an isogeny $\mathrm{KS}(T)\sim\mathrm{KS}(T')$.
- **Compatibility with $\psi$.** We have $C(f)(vxv_0)=f(v)\,C(f)(x)\,f(v_0)$. So $\psi'_{f(v)}\circ C^+(f)=C^+(f)\circ\psi_v$ with $v_0'=f(v_0)$.

Composing algebraic correspondences gives the claim; the converse uses $f^{-1}$. $\square$

---

## 2. The top target: deformation from special points

### 2.1 The family

**Proposition 2.1** (known [De72 §§4–6, An96b §§4–6, Ri10, MP15]). Fix $d\ge1$. There is a connected smooth quasi-projective variety $M=M_d$, finite étale over the moduli stack (hence finite and surjective onto the irreducible coarse moduli space) of primitively polarized K3 surfaces of degree $2d$, which carries the following:
- a smooth projective family $f\colon\mathcal S\to M$ with relatively ample $\mathcal H$;
- a polarized abelian scheme $g\colon\mathcal A\to M$;
- a flat global section $\kappa$ of $R^4(f\times g\times g)_*\mathbb Q$ on $\mathcal X:=\mathcal S\times_M\mathcal A\times_M\mathcal A$ whose value at every $t$ is $\kappa_{S_t}$, built with $V'=H^2(S_t,\mathbb Q)$ and $v_0=h_t$ as in Lemma 1.3(2).

*Sketch with references.*
1. Take a level structure fine enough that the monodromy $\Gamma\subset SO(H^2)$ lifts isomorphically to a subgroup $\tilde\Gamma\subset\mathrm{Spin}$ that does not contain $-1$.
2. The local system $C^+(H^2)$, with $\tilde\Gamma$ acting by left multiplication and with $J$ varying holomorphically, is a polarizable $\mathbb Z$-VHS of weight 1. By Borel's extension theorem its period map is algebraic, so it is the $H^1$ of an abelian scheme.
3. Since $\tilde\gamma$ acts by left multiplication and fixes $h$, we get $\psi_{\gamma v}(\tilde\gamma x)=\tilde\gamma\,\psi_v(x)$. So $\psi$, and hence $\kappa$, is monodromy invariant.

The flat-section form of this is in Deligne [De72] and André [An96b]. The algebraic Kuga–Satake abelian scheme over the orthogonal Shimura variety is due to Rizov [Ri10] and Madapusi Pera [MP15]. $\square$

Every projective K3 surface admits a primitive polarization of some degree $2d$, so it occurs as a fibre of some $M_d$. Let
$$\Sigma=\Sigma_d:=\{t\in M(\mathbb C):\kappa_t\ \text{is algebraic on}\ X_t\}.$$

### 2.2 Structure of the algebraicity locus

**Proposition 2.2** (standard; proof included). The set $\Sigma$ is a countable union $\bigcup_{i\in I}Z_i(\mathbb C)$ of irreducible closed algebraic subvarieties $Z_i\subset M$. On each $Z_i$, the class $\kappa$ is algebraic at *every* point.

*Proof.*
1. **Hilbert-scheme families.** Embed $\mathcal X\subset\mathbb P^N_M$. The relative Hilbert scheme $\mathrm{Hilb}(\mathcal X/M)$ is a countable disjoint union of schemes that are projective over $M$.
   - For a tuple $\tau=(H_1,\dots,H_m)$ of irreducible components whose general member is integral of codimension 2 in its fibre, let $H_\tau=H_1\times_M\cdots\times_MH_m$. It is proper over $M$. Let $H_\tau^\circ\subset H_\tau$ be the open subset over which all the universal fibres $\mathcal Z_{j,h}$ are integral of codimension 2 (openness: [EGA IV$_3$, 12.2.1, 12.2.4]).
   - The classes $[\mathcal Z_{j,h}]\in H^4(X_{\pi(h)},\mathbb Q)$ form flat sections over $H^\circ_\tau$, because fundamental classes are constant in flat families [Fu98, §10.1]. For fixed $a\in\mathbb Q^m$, the set where $\sum_ja_j[\mathcal Z_{j,h}]=\kappa_{\pi(h)}$ is therefore a union of connected components of $H^\circ_\tau$.
   - For each irreducible component $c$ of such a union, let $Z_{\tau,a,c}$ be the closure of $\pi(c)$ in $M$. It is closed and irreducible.
2. **Specialization.** Let $z\in Z_{\tau,a,c}$. Choose an irreducible curve $C\subset Z_{\tau,a,c}$ through $z$ that meets a dense open subset of $\pi(c)$. After a finite base change $C'\to C$, the cycle $\sum a_j\mathcal Z_j$ is defined over the generic point of $C'$. Fulton's specialization map over the local ring of a point of $C'$ above $z$ [Fu98, §20.3, §10.1] is compatible with cycle classes. It produces a cycle on $X_z$ with class $\kappa_z$, because $\kappa$ is flat.
3. **Union.** If $\kappa_t=\sum a_j[W_j]$ with integral $W_j$, then $t\in Z_{\tau,a,c}$ for suitable data. The data $(\tau,a,c)$ form a countable set. $\square$

**Proposition 2.3** (seeds are dense; elementary). The set of $t\in M$ with $\rho(S_t)=20$ is dense in $M(\mathbb C)$ for the analytic topology, and it is contained in $\Sigma$.

*Proof.* By global and local Torelli, the period map identifies $M$ with an open subset of $\Gamma'\backslash\mathcal D$ for a finite-index subgroup $\Gamma'$ of the orthogonal group. Here $\mathcal D$ is the space of oriented positive 2-planes $P\subset V_{\mathbb R}$, $V=h^\perp$, and the open subset is the complement of the locally finite union of $(-2)$-hyperplanes.
- **Density.** Rational planes are dense in $\mathrm{Gr}(2,V_{\mathbb R})$, and positivity is an open condition, so periods with $P$ defined over $\mathbb Q$ are dense. For such $t$, $T(S_t)_{\mathbb Q}\subset P$, so $\rho\ge20$.
- **Membership in $\Sigma$.** At these points KS-HC is known. Morrison proved it for $\rho\ge19$ via Shioda–Inose structures [Mo84, Mo85]; it also follows from Corollary B.1 below. $\square$

**Remark 2.4** (why density is useless). $\Sigma$ contains a dense set, for instance the union of the 3-dimensional loci with $\rho\ge17$. But a countable union of proper closed subvarieties can be dense, and by the Baire category theorem it is never all of $M(\mathbb C)$. So $\Sigma=M$ iff **some single** $Z_i$ equals $M$, and the seeds never produce such a $Z_i$ on their own. This is the whole difficulty, stated in Theorem A.

### 2.3 The exact reduction

Fix a countable algebraically closed field $k_0\subset\mathbb C$ over which $\mathcal X\to M$ and $\mathcal X\subset\mathbb P^N_M$ are defined. Every $Z_i$ in Proposition 2.2 is then defined over $k_0$: it is the closure of the image of an irreducible component of a $k_0$-scheme. A point $t\in M(\mathbb C)$ is **very general** if it lies in no proper closed subvariety of $M$ defined over $k_0$. Such points exist; they form the complement of a countable union of proper subvarieties. For a cycle $Z$ on $X_t$, put $\deg Z=\int_{X_t}[Z]\cdot c_1(\mathcal O(1))^{\dim Z}$.

**Theorem A** (proved here; the arguments are standard, the packaging is mine). For $M=M_d$ the following are equivalent.
1. $\Sigma=M$, i.e. KS-HC holds for every fibre $S_t$.
2. $\Sigma$ contains one very general point.
3. There are an irreducible variety $M''$, a dominant generically finite morphism $\pi\colon M''\to M$ and $\mathcal Z\in CH^2(\mathcal X\times_MM'')_{\mathbb Q}$ such that $[\mathcal Z|_{X_{\pi(s)}}]=\kappa_{\pi(s)}$ for general $s\in M''$.
4. There are integers $N,D\ge1$ and a Zariski-dense set $\Xi\subset M$ such that for every $t\in\Xi$ we have $N\kappa_t=[Z^+_t]-[Z^-_t]$ with $Z_t^\pm$ effective codimension-2 cycles on $X_t$ of degree $\le D$.
5. The variational Hodge conjecture holds for $(\mathcal X/M,\kappa)$: if $\kappa$ is algebraic at one point, it is algebraic at every point.

*Proof.*
- **(1)$\Leftrightarrow$(5).** Since $\Sigma\neq\emptyset$ (Proposition 2.3), (5) gives (1); the converse is trivial.
- **(1)$\Rightarrow$(2).** Trivial.
- **(2)$\Rightarrow$(1).** If $t\in\Sigma$ is very general, then $t\in Z_i$ for some $i$. Since $Z_i$ is defined over $k_0$ and contains $t$, it equals $M$. Proposition 2.2 then gives $\Sigma=M$.
- **(1)$\Rightarrow$(3),(4).** By Baire, some $Z_{\tau,a,c}$ (notation of the proof of 2.2) equals $M$, so $\pi(c)$ is dense.
  - For (3): cut an irreducible component of $c$ that dominates $M$ by general hyperplane sections down to dimension $\dim M$ to get $M''$, and restrict $\sum_ja_j\mathcal Z_j$ to it.
  - For (4): on $c$ the degrees of the flat families $\mathcal Z_{j,h}$ are constant, say $D_j$. Write $a=N^{-1}(n_1,\dots,n_m)$ with $n_j\in\mathbb Z$, and put $D=\sum|n_j|D_j$ and $\Xi=\pi(c)$.
- **(3)$\Rightarrow$(1).** By (3) and Chevalley, $\Sigma$ contains a dense Zariski-open subset of $M$, which is not a countable union of proper closed subvarieties (Baire). Hence (2), hence (1).
- **(4)$\Rightarrow$(1).** Integral subvarieties of $\mathbb P^N$ of fixed dimension and degree $\le D$ form a bounded family (Chow varieties are of finite type [Ko96, Ch. I.3–I.4]). So only finitely many components of $\mathrm{Hilb}(\mathcal X/M)$ contain integral codimension-2 subvarieties of fibres of degree $\le D$.
  - Write $Z^\pm=\sum n_jW_j$ with $n_j\ge1$ and $\sum n_j\deg W_j\le D$. Only finitely many data $(\tau,a)$ occur, and each $H^\circ_\tau$ has finitely many irreducible components.
  - Hence $\Xi$ is contained in a finite union of the closed sets $Z_{\tau,a,c}\subset\Sigma$. Being Zariski dense, $\Xi$ forces one of them to be $M$. $\square$

**Corollary A.1** (proved here). KS-HC holds for every projective K3 surface iff, for every squarefree $d\ge1$, it holds for one very general K3 surface of degree $2d$.

*Proof.* "Only if" is trivial. For "if", Theorem A gives $\Sigma_d=M_d$ for squarefree $d$. Let $d'=dk^2$.
1. **A degree-$2d$ partner.** Let $S'$ be any K3 surface with $NS(S')=\mathbb Zh'$, $h'^2=2d'$. Put $L_e:=\langle-2e\rangle\oplus U^2\oplus E_8(-1)^2$. This is the orthogonal complement of any primitive vector of square $2e$ in $\Lambda_{K3}$, by Eichler's criterion. We have $L_{d}\otimes\mathbb Q\cong L_{d'}\otimes\mathbb Q$ because $\langle-2d\rangle\cong_{\mathbb Q}\langle-2dk^2\rangle$.
2. **Transporting the period.** Fix an isometry $\varphi\colon L_{d,\mathbb Q}\to T(S')_{\mathbb Q}$. Realize $L_d=h^\perp\subset\Lambda_{K3}$ and put $\sigma=\varphi^{-1}(\sigma_{S'})$. Surjectivity of the period map gives a marked K3 surface $S$ with period $\sigma$.
3. **Picard group of $S$.** If $x=ah+y\in NS(S)$ with $y\in L_{d,\mathbb Q}$, then $\varphi(y)\perp\sigma_{S'}$, so $\varphi(y)$ is a rational $(1,1)$-class in $T(S')_{\mathbb Q}$, hence $0$. Therefore $NS(S)=\mathbb Zh$. After changing the sign of the marking, $h$ is ample: there are no $(-2)$-classes.
4. **Conclusion.** Thus $S\in M_d$ and $\varphi$ is a Hodge isometry $T(S)_{\mathbb Q}\cong T(S')_{\mathbb Q}$. By Lemma 1.4, KS-HC holds for every $S'\in M_{d'}$ with $\rho=1$. A very general point of $M_{d'}$ has $\rho=1$, so Theorem A gives $\Sigma_{d'}=M_{d'}$. Every projective K3 surface has a primitive ample class of some degree $2d'$. $\square$

**Corollary A.2** (reduction to one variety per squarefree degree; proved here; (b) is André's mechanism [An96a] made explicit). For squarefree $d$, let $\bar{\mathcal X}_d\supset\mathcal X_d$ be a smooth projective compactification (Hironaka); $\dim\bar{\mathcal X}_d=21+2^{21}$.
- (a) If every Hodge class in $H^4(\bar{\mathcal X}_d,\mathbb Q)$ is algebraic, then KS-HC holds for every K3 surface of degree $2dk^2$, for all $k\ge1$.
- (b) The same conclusion holds if the Lefschetz standard conjecture $B(\bar{\mathcal X}_d)$ holds.

*Proof.* (a) Fix $t\in M$.
1. **Global invariant cycles.** By Deligne's theorem [De71, 4.1.1], the image of the restriction $H^4(\bar{\mathcal X},\mathbb Q)\to H^4(X_t,\mathbb Q)$ is $H^4(X_t)^{\pi_1(M,t)}$. The restriction is a morphism of polarizable Hodge structures, so by semisimplicity the invariant Hodge class $\kappa_t$ has a Hodge preimage $\eta$.
2. **Spreading out.** If $\eta=[Z]$, then $\eta|_{X_s}=[i_s^!Z]$ is algebraic for every $s\in M$. The classes $s\mapsto\eta|_{X_s}$ form a flat global section that agrees with $\kappa$ at $t$, hence everywhere. So $\Sigma_d=M_d$.
3. **Other degrees.** The degrees $2dk^2$ follow by the argument of Corollary A.1.

(b) Let $t_0$ be a seed (Proposition 2.3), $X_0=X_{t_0}$ and $i\colon X_0\hookrightarrow\bar{\mathcal X}$.
1. **Algebraic adjoint of $i^*$.** $B(X_0)$ holds: $B$ holds for surfaces and for abelian varieties [Li68] and is stable under products [Kl68]. For $X$ satisfying $B(X)$, Kleiman's operator $*_X$ and its inverse are algebraic [Kl68, Kl94]. Here $*_X(L^j\alpha)=(-1)^{i(i+1)/2}\tfrac{j!}{(n-i-j)!}L^{n-i-j}\alpha$ for $\alpha$ primitive of degree $i$. By the Hodge–Riemann relations, $\langle x,y\rangle_X=\int_Xx\cdot{*}y$ is positive definite on rational Hodge classes. Hence $i^\dagger:=*_{\bar{\mathcal X}}^{-1}\circ i_*\circ *_{X_0}$ is algebraic, preserves Hodge classes, and satisfies $\langle i^*a,b\rangle_{X_0}=\langle a,i^\dagger b\rangle_{\bar{\mathcal X}}$ (projection formula).
2. **An invertible endomorphism.** Put $E=i^*(\mathrm{Hdg}^2(\bar{\mathcal X}))$ and $P=i^*i^\dagger$. Then $P$ maps $\mathrm{Hdg}^2(X_0)$ into $E$. It is injective on $E$: if $x=i^*y\in E$ and $Px=0$, then $\langle i^\dagger x,i^\dagger x\rangle=\langle Px,x\rangle=0$, so $i^\dagger x=0$, so $\langle x,x\rangle=\langle y,i^\dagger x\rangle=0$, so $x=0$. Thus $P|_E$ is invertible, and its inverse equals $p(P)|_E$ for a polynomial $p\in\mathbb Q[X]$ (Cayley–Hamilton).
3. **The lift.** By step 1 of (a), $\kappa_{t_0}\in E$. Put $\eta=i^\dagger p(P)\kappa_{t_0}$. It is algebraic, being an algebraic correspondence applied to an algebraic class, and $i^*\eta=\kappa_{t_0}$. Conclude as in (a). $\square$

### 2.4 Where the attempt on the top target stops

Steps 1–2 (Propositions 2.1, 2.3) are complete. Step 3, propagating algebraicity from the seeds, needs one of the statements in Theorem A. I tried three routes; each stops at a precisely identifiable point.

**(i) Semiregularity (mechanism M2 of docs/03).**
- *What it needs.* By Bloch / Buchweitz–Flenner, a semiregular $E\in D^b(X_{t_0})$ deforms along every direction in which all of $\mathrm{ch}(E)$ stays Hodge; Artin approximation would then give Theorem A(3). This needs an object at some seed whose *entire* Chern character consists of flat Hodge sections over $M$, with $\kappa$ among them, and whose semiregularity map is injective.
- *Why the known cycles fail.* The cycles known at seeds include Morrison's graphs of rational maps $A\times A\dashrightarrow\mathrm{Km}(B)$ composed with isogenies. They also include Floccari's composites of the correspondences relating $S_K$, a moduli space of sheaves on $S_K$, the crepant resolution $Y_K$ of $K/G$, and $K$, with the Kuga–Satake cycles for Kummer type [Ma23, Vo22, VV22]. As far as I can see, the individual classes of these cycles involve $NS(S_{t_0})$ and $\operatorname{End}^0(A_{t_0})$ beyond the generic ones, so they are not flat Hodge sections; only special $\mathbb Q$-combinations are. I have not checked this for every seed construction and claim nothing about it. In any case, semiregularity does not apply to $\mathbb Q$-combinations of cycles.
- *Status.* I know no admissible object $E$ (GAP G2).

**(ii) Formal lifting.**
- *What is available.* At a seed, $\xi_0=\mathrm{ch}^{-1}(z_0)\in K_0(X_{t_0})_{\mathbb Q}$ has Chern character $\kappa_{t_0}$, which stays in $F^2$ along $M$. So Bloch–Esnault–Kerz [BEK14] should give, in their setting (formal deformations in characteristic 0), a lift to the pro-system of $K$-groups of the infinitesimal thickenings. I have not checked their hypotheses for this family, and I do not use this.
- *What is missing.* Algebraizing such formal lifts is problem P5 of docs/03 and is exactly Theorem A(3) (GAP G1).

**(iii) Bounded complexity (Theorem A(4)).**
- *What it needs.* Seeds whose cycles have uniformly bounded degree and denominators.
- *What is known.* The seed cycles depend on $T(S)$, through the dimension $2n$ of the Kummer-type variety, the group $G$ and the Mukai vector. No uniform bound is known, and I can prove neither a bound nor its impossibility (GAP G3).

---

## 3. Ladder (b): the exact reach of the generalized-Kummer method, and the first open case

**Notation.**
- $H$ denotes the hyperbolic plane $U\otimes\mathbb Q$, and $i_F(V)$ the Witt index over $F$.
- For $\dim V=2m$, put $\delta(V)=(-1)^m\det V\in F^*/F^{*2}$.
- For $e\in\mathbb Q_{<0}$, put $W_e:=H^3\perp\langle e\rangle$; it has dimension 7 and signature $(3,4)$.

**Textbook facts used** [Se73 Ch. IV; La05 Ch. I, V, VI].
- (Q1) *Hasse–Minkowski.* A rational quadratic space is isotropic iff it is isotropic everywhere locally. Hence an indefinite rational space of dimension $\ge5$ is isotropic.
- (Q2) Witt cancellation holds. $V\perp(-V)\cong H^{\dim V}$. A totally isotropic subspace of dimension $k$ forces Witt index $\ge k$.
- (Q3) An anisotropic 4-dimensional space over $\mathbb Q_p$ has square determinant and is similar to $\mathrm{Nrd}_{D_p}$, the reduced norm of the quaternion division algebra $D_p$.
- (Q4) *Clifford algebras.*
  - $C(\langle a,b\rangle)\cong(a,b)$.
  - For $\dim V_1$ even, $C(V_1\perp V_2)\cong C(V_1)\otimes C(\delta(V_1)V_2)$; in particular $C(H\perp W)\cong M_2(C(W))$.
  - If $\dim V$ is even and $\delta(V)\notin F^{*2}$, then $C^+(V)$ is central simple over $K=F(\sqrt{\delta(V)})$ and $[C^+(V)]=[C(V)\otimes_FK]$ in $\mathrm{Br}(K)$ (double centralizer).
  - $C^+(V,\lambda q)\cong C^+(V,q)$ for $\lambda\in F^*$. To see this, write $V=Fv_1\perp V_1$ and use $C^+(\langle a\rangle\perp V_1)\cong C(-aV_1)$; scaling by $\lambda$ changes $-aV_1$ to $-\lambda^2aV_1\cong-aV_1$.
- (Q5) $[C(\lambda\,\mathrm{Nrd}_{(a,b)})]=[(a,b)]$. Indeed, applying (Q4) to $\langle\lambda,-\lambda a\rangle\perp\lambda\langle-b,ab\rangle$ gives $(\lambda,a)\cdot(-\lambda ab,a)=(-ab,a)=(b,a)$.
- (Q6) Over a number field, the index of a central simple algebra equals its exponent (Albert–Brauer–Hasse–Noether).

**Theorem B** (proved here; the split case's link with Weil fourfolds is due to van Geemen and Lombardo). Let $(T,q)$ be a rational quadratic space of dimension $r\ge2$ and signature $(2,r-2)$.
1. If $r\le4$, then $T$ embeds isometrically in $W_e$ for **every** $e<0$.
2. If $r=5$, then $T$ embeds in $W_e$ for some $e<0$, hence in $W_{es^2}$ for every $s\in\mathbb Q^*$.
3. If $r=6$, put $\delta=-\det T<0$ and $K=\mathbb Q(\sqrt\delta)$, an imaginary quadratic field. The following are equivalent:
   - (a) $T\hookrightarrow W_e$ for some $e<0$;
   - (b) $i_{\mathbb Q}(T)=2$;
   - (c) $T\cong H^2\perp N$ with $N$ negative definite of dimension 2;
   - (d) $C^+(T)\cong M_4(K)$.

   If they fail, then $i_{\mathbb Q}(T)=1$. There is then a prime $p$, split in $K$, with $T_{\mathbb Q_p}\cong H\perp(\text{anisotropic of dim }4)$, and $C^+(T)\cong M_2(D)$ with $D$ a quaternion **division** algebra over $K$ ramified at both primes above $p$.
4. If $r\ge7$, then $T$ embeds in no $W_e$.
5. If moreover $T$ is a K3-type space of rank 6, then $\mathrm{KS}(T)\sim B^4$ with $B$ an abelian fourfold if (a)–(d) hold, and $\mathrm{KS}(T)\sim B'^2$ with $\dim B'=8$ and $D\subset\operatorname{End}^0(B')$ otherwise. In the split case $B$ is of Weil type for $K$, and van Geemen and Lombardo [vG00, Lo01] identify these $B$ as the Weil fourfolds of discriminant 1. Neither of these two statements is used or re-checked here.

*Proof.*
- **(4).** The negative index of $T$ is $r-2\ge5>4$.
- **(1).** If $r\le3$, then $T\hookrightarrow T\perp(-T)\cong H^r\subset W_e$. If $r=4$, then $T\perp\langle-e\rangle$ has signature $(3,2)$ and is isotropic by (Q1), so $q(x)=e\lambda^2$ for some $(x,\lambda)\ne0$.
  - If $\lambda\ne0$, then $T\cong\langle e\rangle\perp T_3$ and $T\hookrightarrow\langle e\rangle\perp T_3\perp(-T_3)\cong W_e$.
  - If $\lambda=0$, then $T\cong H\perp T_2\hookrightarrow H\perp T_2\perp(-T_2)\cong H^3$.
- **(2).** By (Q1), $T\cong H\perp T_3$ with $T_3$ of signature $(1,2)$. Since $T_3\otimes\mathbb R$ is negative on a nonempty open cone, some rational $x\in T_3$ has $e:=q(x)<0$. Then $T\cong H\perp\langle e\rangle\perp T_2\hookrightarrow H\perp\langle e\rangle\perp T_2\perp(-T_2)\cong W_e$.
- **(3).** Bounds on the Witt index: $i_{\mathbb R}(T)=2$ gives $i_{\mathbb Q}(T)\le2$, and (Q1) gives $i_{\mathbb Q}(T)\ge1$. (b)$\Leftrightarrow$(c) by definition and a signature count.
  - **(c)$\Rightarrow$(a).** Write $N=\langle e,e'\rangle$ with $e,e'<0$. Then $T\hookrightarrow H^2\perp\langle e\rangle\perp\langle e',-e'\rangle\cong W_e$.
  - **(a)$\Rightarrow$(c).** $W_e\cong T\perp\langle c\rangle$ with $c>0$. Adding $\langle-c\rangle$ gives $T\perp H\cong H^3\perp\langle e,-c\rangle$, so $T\cong H^2\perp\langle e,-c\rangle$ by Witt cancellation.
  - **(c)$\Rightarrow$(d).** With $N=\langle a,b\rangle$ we have $\delta=-ab$, and by (Q4) $[C^+(T)]=[C(N)\otimes K]=[(a,b)_K]$. In $K$, $-ab$ is a square, so $b\equiv-a$ modulo $K^{*2}$ and $(a,b)_K=(a,-a)_K=0$. A split central simple algebra of degree 4 over $K$ is $M_4(K)$.
  - **$\neg$(b)$\Rightarrow\neg$(d), and the final claims.**
    1. If $i_{\mathbb Q}(T)=1$, then $T\cong H\perp Q_4$ with $Q_4$ anisotropic over $\mathbb Q$ of signature $(1,3)$. Since $Q_4$ is isotropic over $\mathbb R$, it is anisotropic over some $\mathbb Q_p$.
    2. By (Q3), $\det Q_4=\det T/\det H=-\det T=\delta$ is a square in $\mathbb Q_p$, so $p$ splits in $K$.
    3. For $\mathfrak p\mid p$ we have $K_{\mathfrak p}=\mathbb Q_p$, and by (Q3)–(Q5) $[C^+(T)]_{K_{\mathfrak p}}=[C(Q_4\otimes\mathbb Q_p)]=[D_p]\ne0$.
    4. The class $[C^+(T)]=[C(T)_K]$ has exponent dividing 2, since $C(T)$ carries an involution of the first kind; hence the exponent is exactly 2, so its index is 2 by (Q6). Therefore $C^+(T)\cong M_2(D)$ with $D$ a division algebra ramified at $\mathfrak p$.
- **(5).** The right action of $C^+(T)^{op}\cong C^+(T)$ (via the canonical involution) lies in $\operatorname{End}^0(\mathrm{KS}(T))$, and $\dim\mathrm{KS}(T)=16$. Matrix units of $M_4(K)$, respectively of $M_2(D)$, split $\mathrm{KS}(T)$ into four, respectively two, isogenous factors. $\square$

**Input (F$_n$)** (Floccari: [Fl24] for $n=3$; [Fl25] as stated for all $n\ge2$; I could not access [Fl25], so its exact scope is not re-checked). For every projective hyper-Kähler manifold $K$ of generalized Kummer type of dimension $2n$ there are:
- a projective K3 surface $S_K$ with a Hodge isometry $T(S_K)\cong T(K)(2)$, where $T(K)\subset H^2(K,\mathbb Z)$ carries the Beauville–Bogomolov form;
- the property that KS-HC$(S_K)$ holds.

**Corollary B.1** (known in substance [Fl25]; proof of the reduction to Theorem B given here). Let $\mathcal N$ be the set of $n\ge2$ for which (F$_n$) holds. If $T(S)_{\mathbb Q}\hookrightarrow W_{-(n+1)}$ for some $n\in\mathcal N$, then KS-HC$(S)$ holds. If $\mathcal N=\mathbb Z_{\ge2}$, KS-HC holds for every $S$ with $\rho(S)\ge17$, and for every $S$ with $\rho(S)=16$ and $C^+(T(S)_{\mathbb Q})$ split.

*Proof.*
1. **A lattice embedding.** By Beauville, $H^2(K,\mathbb Z)=U^3\perp\langle-2(n+1)\rangle$. With the form doubled, its rationalization is $H^3\perp\langle-4(n+1)\rangle\cong W_{-(n+1)}$. So an embedding $T(S)_{\mathbb Q}\hookrightarrow W_{-(n+1)}$ is an isometric embedding $\iota\colon T(S)_{\mathbb Q}(\tfrac12)\hookrightarrow H^2(K,\mathbb Q)$.
2. **A projective $K$.** Surjectivity of the period map [Hu99, Thm 8.1] gives a marked $K$ with period $\iota(\sigma_S)$.
   - By minimality of transcendental spaces, $T(K)_{\mathbb Q}=\iota(T(S)_{\mathbb Q}(\frac12))$.
   - The orthogonal complement of this image has signature $(1,6-r)$, so it contains a rational class of positive square, which is of type $(1,1)$. Hence $K$ is projective [Hu99, Thm 3.11].
3. **Transport.** Now (F$_n$) and $T(S_K)_{\mathbb Q}\cong T(K)_{\mathbb Q}(2)\cong T(S)_{\mathbb Q}$ give KS-HC$(S)$ by Lemma 1.4.
4. **The scope when $\mathcal N=\mathbb Z_{\ge2}$.** Every negative rational is $\equiv-(n+1)$ modulo squares for some $n\ge2$. Apply Theorem B(1)–(3). $\square$

Morrison's $\rho\ge19$ and Paranjape's six-line family ($T=U(2)^2\perp\langle-2\rangle^2$, Witt index 2) are special cases. With $\mathcal N=\{3\}$ alone one gets $e\equiv-1$. By Theorem B(1) this still covers every $S$ with $\rho\ge18$. It covers $\rho=17$ when the ternary part of $T$ represents $-1$, and $\rho=16$ when $T\cong H^2\perp\langle-1,-c\rangle$.

**Example B.2** (the complementary class is nonempty; proved here). Let $T_0=U\perp\langle10,-2,-4,-20\rangle$, an even lattice of signature $(2,4)$.
1. **Non-split Clifford algebra.** Over $\mathbb Q_5$ the quaternary summand is $\langle-2,-4\rangle\perp5\langle2,-4\rangle$. Its reductions mod 5 are $\langle3,1\rangle$ and $\langle2,1\rangle$, which are anisotropic because $2$ and $3$ are non-squares mod 5. By Springer's theorem the summand is anisotropic over $\mathbb Q_5$. Hence $i_{\mathbb Q}(T_0)=1$, $\delta\equiv-1$, $K=\mathbb Q(i)$ (in which $5$ splits), and $C^+(T_{0,\mathbb Q})\cong M_2(D)$ with $D$ division.
2. **Realization by K3 surfaces.** Since $\operatorname{rk}T_0=6\le10$, $T_0$ embeds primitively in $\Lambda_{K3}$ [Ni79, Cor. 1.12.3; Mo84, Cor. 2.10]. Take a period $\sigma\in T_0\otimes\mathbb C$ off the countably many hyperplanes $x^\perp$, $x\in T_0\setminus0$. The resulting K3 surface has $T(S)=T_0$ and $NS(S)=T_0^\perp$ of signature $(1,15)$. So $S$ is projective with $\rho=16$, and $S$ is outside Corollary B.1.

**Proposition B.3** (similitude invariance of the boundary; proved here). Let $\sim$ be the equivalence relation on projective K3 surfaces generated by "$T(S)_{\mathbb Q}$ and $T(S')_{\mathbb Q}$ are Hodge similar". Let $\mathcal K$ be the class of $S$ with $\rho=16$ and $C^+(T(S)_{\mathbb Q})$ non-split. Then $\mathcal K$ is a union of $\sim$-classes, disjoint from the classes of all surfaces covered by Corollary B.1. Consequently, no combination of the following relates a member of $\mathcal K$ to a covered surface:
- Buskin isometries;
- (twisted) derived equivalences and moduli spaces of (twisted) sheaves [Mu87, Or97, HS05];
- quotients by finite symplectic groups;
- dominant rational maps;
- Hecke correspondences.

Each of these induces a Hodge similitude of $T_{\mathbb Q}$.

*Proof.* A similitude with multiplier $\lambda$ is an isometry $(T,\lambda q)\to(T',q')$. So $C^+(T)\cong C^+(T,\lambda q)\cong C^+(T')$ by (Q4), and the rank is preserved. Covered surfaces with $\rho=16$ are split by Theorem B(3). $\square$

**Proposition B.4** (imaginary-quadratic actions force splitness; proved here). Let $\rho(S)=16$. Suppose an imaginary quadratic field $K'$ acts on $T(S)_{\mathbb Q}$ by Hodge endomorphisms with $q(ax,y)=q(x,\bar ay)$. Then $C^+(T(S)_{\mathbb Q})$ is split.

This applies in particular when $S$ has a non-symplectic automorphism $g$ of order $n\in\{3,4,6\}$. Hence $\mathcal K$ contains no member of any family of K3 surfaces with such an action, for instance the 9-dimensional families with an order-3 non-symplectic automorphism where Bolognesi–Laterveer prove KS-HC [BL24]. Specializing within such families cannot reach $\mathcal K$.

*Proof.*
1. **A Hermitian form.** Define $h(x,y)\in K'$ by $\mathrm{Tr}_{K'/\mathbb Q}(a\,h(x,y))=q(ax,y)$ for all $a\in K'$. It is Hermitian, with $h(ax,by)=a\bar b\,h(x,y)$ and $q(x,x)=2h(x,x)$.
2. **A 2-dimensional isotropic subspace.** By (Q1) there is $x\ne0$ with $q(x,x)=0$, hence $h(x,x)=0$. Then $q(ax,bx)=\mathrm{Tr}(a\bar b\,h(x,x))=0$, so $K'x$ is a totally isotropic plane. Thus $i_{\mathbb Q}=2$, and Theorem B(3) applies.
3. **The automorphism case.** $g$ preserves $T=T(S)_{\mathbb Q}$. For $k\mid n$ with $k<n$, the space $\ker(g^k-1)\cap T$ is a rational sub-Hodge structure not containing $H^{2,0}$. Its orthogonal complement in $T$ contains $H^{2,0}$, so by minimality that complement is $T$ and the kernel is $0$. Hence $\Phi_n(g)=0$ on $T$ and $\mathbb Q(\zeta_n)$ acts. Since $g$ is an isometry, $q(ax,y)=q(x,\bar ay)$. $\square$

**Proposition B.5** (weight obstruction to the "moduli of sheaves on $S$" route; trivial). Let $\mathcal C_S$ be the smallest class of rational Hodge structures containing $H^*(S,\mathbb Q)$ and $\mathbb Q(1)$ and closed under $\oplus,\otimes$, duals and subquotients. If $Y$ is smooth projective with $H^*(Y,\mathbb Q)\in\mathcal C_S$, then:
- $H^{odd}(Y,\mathbb Q)=0$;
- $\mathrm{Alb}(Y)$ and all intermediate Jacobians of $Y$ vanish;
- no nonzero abelian variety has its $H^1$ among the subquotients of $H^*(Y)$.

This applies to $S^n$, to $S^{[n]}$, and to every moduli space $M_H(v)$ whose cohomology is generated by Künneth components of a (quasi-)universal family [Ma02].

*Proof.* Every object of $\mathcal C_S$ has only even weights, while $H^k(Y)$ has weight $k$ and $H^1(B)$ has weight 1. $\square$

So ladder (a)'s suggestion to relate $\mathrm{KS}(S)$ to moduli of sheaves on $S$ cannot work through Albanese or intermediate Jacobians of such spaces. An odd-weight object must come from outside $\mathcal C_S$, as the Kummer-type $K$ does in Floccari's argument.

---

## 4. Ladder (c): what is and is not achieved

Achieved (Corollaries A.1 and A.2): KS-HC for all projective K3 surfaces is equivalent to KS-HC for one very general surface of each squarefree degree. It is implied by $\mathrm{HC}$ for $H^4$ of, or by $B$ for, the single varieties $\bar{\mathcal X}_d$, one for each squarefree $d$. These varieties are explicit only up to the choice of compactification, and they are not abelian or hyper-Kähler.

**Remark 4.1** (why I do not reach "HC for an explicit family of abelian or HK varieties"). This is not a theorem; it is about the present toolbox.
1. **Every known proof uses a linking variety.** As far as I know, every proof of KS-HC for a K3 surface runs through such a $Y$: Morrison (abelian surfaces), Paranjape (abelian varieties attached to the six-line configuration), Floccari (Kummer type), Bolognesi–Laterveer (cyclic cubic fourfolds and cubic threefolds). Each $Y$ has nonzero odd cohomology and an algebraic correspondence inducing $T(S)_{\mathbb Q}\hookrightarrow H^*(Y)$.
2. **Constraints on such $Y$.** By Proposition B.5, the cohomology of $Y$ cannot lie in $\mathcal C_S$. For a very general $S$, a link through $H^2$ needs $b_2(Y)\ge22$.
3. **Known HK types do not suffice.** The known hyper-Kähler types with odd cohomology are of Kummer type, with $b_2=7$; this gives exactly the range of Theorem B. The types $K3^{[n]}$, OG6 and OG10 have, to my knowledge, no odd cohomology.
4. **Conclusion.** A reduction of the requested kind would need a new linking variety. This is the same obstruction as GAP G4.

---

## 5. GAPS

**G1 — the top target.**
- *Needed:* for each squarefree $d$, the variational Hodge conjecture for $(\mathcal X_d/M_d,\kappa)$. By Theorem A and Corollary A.1, this is equivalent to KS-HC for one very general K3 surface of each squarefree degree.
- *Why needed:* by Theorem A this *is* the top target.
- *Why I cannot prove it:* algebraicity at the dense seeds (Proposition 2.3) cannot propagate without an algebraization mechanism, and §2.4 (i)–(iii) are all blocked.
- *A variant not claimed:* replacing "very general" by "transcendence degree 19 over $\bar{\mathbb Q}$" would need $(\mathcal A,\kappa)$ to descend to a number field compatibly with $\mathrm{Aut}(\mathbb C/\bar{\mathbb Q})$.

**G2 — semiregular seed.**
- *Needed:* a point $t_0$ and $E\in D^b(X_{t_0})$ with the following properties: every component of $\mathrm{ch}(E)$ is a flat Hodge section over $M_d$, one of them is $\kappa$ (modulo algebraic classes), and the Buchweitz–Flenner semiregularity map is injective.
- *Why needed:* it would give Theorem A(3), via deformation of $E$ and Artin approximation.
- *Why I cannot prove it:*
  - I have no candidate: as far as I can see, the known seed cycles have classes that are not flat (§2.4(i)).
  - The semiregularity map on a variety of dimension $2+2^{21}$ is far beyond direct computation.
  - I cannot prove that no such $E$ exists.

**G3 — uniform bounds.**
- *Needed:* $N,D$ and a Zariski-dense set of seeds with cycles as in Theorem A(4).
- *Why I cannot prove it:* the seed constructions vary with $T(S)$, and no bound is known in either direction.

**G4 — first open case of ladder (b).**
- *Needed:* KS-HC for the class $\mathcal K$ ($\rho=16$, $C^+(T)\cong M_2(D)$ with $D$ division; nonempty by Example B.2), and for $\rho\le15$ outside special families.
- *Why I cannot prove it:* Propositions B.3 and B.4 show that transport along similitudes and specialization inside imaginary-quadratic families cannot reach $\mathcal K$. A new seed needs a variety with odd cohomology containing $H^1(B')$, for $B'$ an abelian 8-fold with multiplication by the quaternion algebra $D$ over $K$, linked algebraically to $S$. I know none.

**G5 — scope of Floccari's input.** The full scope of Corollary B.1 ($\rho=17$ in general, and $\rho=16$ split) depends on (F$_n$) for all $n\ge2$ as stated in [Fl25], which I could not read. The network policy blocked arxiv.org, msp.org and the author's page, and my search budget ran out. With [Fl24] alone ($n=3$), the scope is as in the remark after Corollary B.1. Theorem B itself is unconditional.

**G6 — quoted statements.** Three statements are quoted, not re-proved: that $B$ is of Weil type with discriminant 1 (Theorem B(5)); the formal-lifting statement attributed to [BEK14] (§2.4(ii)); and the list of hyper-Kähler types without odd cohomology (Remark 4.1). Nothing labelled "proved here" depends on them.

---

## 6. Checklist (docs/03 §3.4)

**Rational coefficients — where they are essential.**
- Lemma 1.3(1): endomorphisms of $A$, such as right multiplication by $C^+(V)$, are algebraic only as $\mathbb Q$-combinations of graphs.
- Lemma 1.4: Buskin's cycles have $\mathbb Q$-coefficients.
- Theorem A: the coefficients $a\in\mathbb Q^m$, and the multiple $N$ in (4).
- Corollary A.2:
  - the choice of a Hodge preimage $\eta$ uses semisimplicity of polarizable $\mathbb Q$-Hodge structures;
  - the inverse $p(P)$ is a rational polynomial.

  Over $\mathbb Z$ a Hodge preimage need not exist, so the argument does not produce integral cycles.

*Integral test.* No statement here claims integral algebraicity. The formal equivalences of Theorem A also hold for $\mathbb Z$-cycles with $N=1$, but they assert nothing. Corollary A.2 fails integrally exactly at semisimplicity, as it must, given Kollár's and Engel–de Gaay Fortman–Schreieder's counterexamples.

**Projectivity — where it is essential.**
- The Kuga–Satake construction used needs signature $(2,n-2)$, i.e. a polarized K3-type space; this is the projective case.
- Proposition 2.2 and Theorem A need relative Hilbert and Chow schemes that are proper and of finite type, which requires the family $\mathcal X\to M$ to be projective.
- Proposition 2.1 uses Borel's extension theorem over the quasi-projective $M$.
- Corollary A.2 uses Deligne's invariant-cycle theorem for a smooth projective compactification.
- Corollary B.1 uses the projectivity criterion for $K$ and Buskin's theorem for projective K3 surfaces.

*Kähler test.* Every algebraicity conclusion here is transported from an *input* cycle by algebraic operations: specialization in projective families and composition of correspondences. None is produced from Hodge theory alone. So nothing here implies a Kähler analogue, for instance analyticity of $\kappa$ for a non-projective K3 surface with its Kuga–Satake torus, and Voisin's tori are not contradicted.

**Other checklist items.**
- *Absoluteness:* $\kappa$ is absolute Hodge [De72] and motivated [An96a]. It is used only through the literature and is consistent with everything here.
- *Lefschetz $B$:* Corollary A.2(b) isolates one variety per degree.
- *Variational HC:* the top target is an instance of it (Theorem A(5)).
- *Open special cases:* if achieved, the top target would give, via [Va23, Fl25], algebraicity of Hodge similitudes between K3 surfaces and the K3 cases of problem P2. That is not done here.

---

## 7. References

- [An96a] Y. André, *Pour une théorie inconditionnelle des motifs*, Publ. Math. IHÉS 83 (1996), 5–49.
- [An96b] Y. André, *On the Shafarevich and Tate conjectures for hyperkähler varieties*, Math. Ann. 305 (1996), 205–248.
- [BEK14] S. Bloch, H. Esnault, M. Kerz, *Deformation of algebraic cycle classes in characteristic zero*, Algebra & Number Theory 8 (2014), 1227–1242.
- [BL24] M. Bolognesi, R. Laterveer, *A 9-dimensional family of K3 surfaces with finite dimensional motive*, Rend. Circ. Mat. Palermo (2024); arXiv:2310.11981.
- [Bu19] N. Buskin, *Every rational Hodge isometry between two K3 surfaces is algebraic*, J. reine angew. Math. 755 (2019), 127–150.
- [De71] P. Deligne, *Théorie de Hodge II*, Publ. Math. IHÉS 40 (1971), 5–57 (Thm 4.1.1).
- [De72] P. Deligne, *La conjecture de Weil pour les surfaces K3*, Invent. Math. 15 (1972), 206–226.
- [EGA IV$_3$] A. Grothendieck, J. Dieudonné, Publ. Math. IHÉS 28 (1966).
- [Fl24] S. Floccari, *Sixfolds of generalized Kummer type and K3 surfaces*, Compositio Math. 160 (2024), 388–410; arXiv:2210.02948.
- [Fl25] S. Floccari, *K3 surfaces associated with varieties of generalized Kummer type*, arXiv:2501.02315; Geom. Topol. 30 (2026). Known to me only through search excerpts: $S_K$ exists for every $K$ of generalized Kummer type, $T(S_K)\cong T(K)(2)$, and KS-HC holds for $S_K$ and for K3 surfaces whose rational transcendental lattice admits a suitable embedding.
- [Fu98] W. Fulton, *Intersection Theory*, 2nd ed., Springer 1998.
- [HS05] D. Huybrechts, P. Stellari, *Equivalences of twisted K3 surfaces*, Math. Ann. 332 (2005), 901–936.
- [Hu99] D. Huybrechts, *Compact hyperkähler manifolds: basic results*, Invent. Math. 135 (1999), 63–113; erratum ibid. 152 (2003).
- [Hu16] D. Huybrechts, *Lectures on K3 Surfaces*, Cambridge Univ. Press 2016, Ch. 4 (Kuga–Satake), Ch. 14 (lattices).
- [Kl68] S. Kleiman, *Algebraic cycles and the Weil conjectures*, in: Dix exposés sur la cohomologie des schémas, North-Holland 1968, 359–386.
- [Kl94] S. Kleiman, *The standard conjectures*, Proc. Sympos. Pure Math. 55 (1994), Part 1, 3–20.
- [Ko96] J. Kollár, *Rational Curves on Algebraic Varieties*, Springer 1996, Ch. I.
- [KS67] M. Kuga, I. Satake, *Abelian varieties attached to polarized K3 surfaces*, Math. Ann. 169 (1967), 239–242.
- [La05] T. Y. Lam, *Introduction to Quadratic Forms over Fields*, GSM 67, AMS 2005 (Ch. V: Clifford algebras; Ch. VI: Springer's theorem, local fields).
- [Li68] D. Lieberman, *Numerical and homological equivalence of algebraic cycles on Hodge manifolds*, Amer. J. Math. 90 (1968), 366–374.
- [Lo01] G. Lombardo, *Abelian varieties of Weil type and Kuga–Satake varieties*, Tôhoku Math. J. 53 (2001), 453–466.
- [Ma02] E. Markman, *Generators of the cohomology ring of moduli spaces of sheaves on symplectic surfaces*, J. reine angew. Math. 544 (2002), 61–82.
- [Ma23] E. Markman, *The monodromy of generalized Kummer varieties and algebraic cycles on their intermediate Jacobians*, J. Eur. Math. Soc. 25 (2023), 231–321.
- [Mo84] D. Morrison, *On K3 surfaces with large Picard number*, Invent. Math. 75 (1984), 105–121.
- [Mo85] D. Morrison, *The Kuga–Satake variety of an abelian surface*, J. Algebra 92 (1985), 454–476.
- [MP15] K. Madapusi Pera, *The Tate conjecture for K3 surfaces in odd characteristic*, Invent. Math. 201 (2015), 625–668.
- [Mu87] S. Mukai, *On the moduli space of bundles on K3 surfaces I*, Tata Inst. Stud. Math. 11 (1987), 341–413.
- [Ni79] V. V. Nikulin, *Integral symmetric bilinear forms and some of their applications*, Math. USSR Izv. 14 (1980), 103–167.
- [Or97] D. Orlov, *Equivalences of derived categories and K3 surfaces*, J. Math. Sci. 84 (1997), 1361–1381.
- [Pa88] K. Paranjape, *Abelian varieties associated to certain K3 surfaces*, Compositio Math. 68 (1988), 11–22.
- [Ri10] J. Rizov, *Kuga–Satake abelian varieties of K3 surfaces in mixed characteristic*, J. reine angew. Math. 648 (2010), 13–67.
- [Se73] J.-P. Serre, *A Course in Arithmetic*, GTM 7, Springer 1973.
- [Va23] M. Varesco, *Hodge similarities, algebraic classes, and Kuga–Satake varieties*, Math. Z. (2023); arXiv:2304.02519.
- [vG00] B. van Geemen, *Kuga–Satake varieties and the Hodge conjecture*, in: The Arithmetic and Geometry of Algebraic Cycles (Banff 1998), NATO Sci. Ser. C 548, Kluwer 2000, 51–82.
- [Vo22] C. Voisin, *Footnotes to papers of O'Grady and Markman*, Math. Z. (2022); cited, as in [Fl24], for KS-HC of Kummer-type varieties.
- [VV22] M. Varesco, C. Voisin, *Hyper-Kähler manifolds of generalized Kummer type and the Kuga–Satake correspondence*, Milan J. Math. 90 (2022), 433–444.

---

## 8. Claimed results

| Label | One-line statement | Status |
|---|---|---|
| Lemma 1.1 | $\psi\colon V(1)\to\operatorname{End}H^1(\mathrm{KS}(V))$, $\psi_v(x)=vxv_0$, is an injective morphism of Hodge structures | known [De72, vG00]; proof recalled |
| Lemma 1.3 | KS-HC$(S)$ is independent of $v_0$, lattice and polarization, and is the same for $T(S)_{\mathbb Q}$, $h^\perp$ and $H^2$; the $NS$-part is always algebraic | known in substance [vG00, Fl24]; proof given |
| Lemma 1.4 | KS-HC is invariant under rational Hodge isometries of $T_{\mathbb Q}$ | known in substance (from [Bu19]); proof given |
| Proposition 2.1 | Kuga–Satake family and flat Hodge section $\kappa$ over a finite étale cover $M_d$ of the degree-$2d$ moduli space | known [De72, An96b, Ri10, MP15] |
| Proposition 2.2 | $\Sigma_d$ is a countable union of closed subvarieties, on each of which $\kappa$ is algebraic everywhere | standard; proof given here |
| Proposition 2.3 | points with $\rho=20$ are dense in $M_d$ and lie in $\Sigma_d$ | proved here (density); KS-HC there is known [Mo84, Mo85] |
| Theorem A | $\Sigma_d=M_d$ $\iff$ one very general point in $\Sigma_d$ $\iff$ relative cycle over a generically finite cover $\iff$ bounded degree on a Zariski-dense set $\iff$ VHC for $(\mathcal X_d/M_d,\kappa)$ | proved here (standard arguments) |
| Corollary A.1 | KS-HC for all projective K3 surfaces $\iff$ KS-HC for one very general K3 surface of each squarefree degree | proved here |
| Corollary A.2 | HC for $H^4(\bar{\mathcal X}_d)$, or $B(\bar{\mathcal X}_d)$, implies KS-HC in all degrees $2dk^2$ | proved here ((b) is André's mechanism made explicit) |
| Theorem B | $T$ embeds in $W_e=H^3\perp\langle e\rangle$: for every $e<0$ if $r\le4$; for some $e<0$ if $r=5$; if $r=6$ iff Witt index 2, iff $C^+(T)\cong M_4(K)$, iff $\mathrm{KS}\sim B^4$; otherwise $C^+(T)\cong M_2(D)$ with $D$ division; never if $r\ge7$ | proved here; the Weil-type, discriminant-1 identification in (5) is quoted [vG00, Lo01] |
| Corollary B.1 | KS-HC for all $\rho\ge17$ and for $\rho=16$ with $C^+(T)$ split | proved here conditionally on (F$_n$) for all $n\ge2$ (stated in [Fl25], not re-checked); known in substance [Fl25] |
| Example B.2 | K3 surfaces with $\rho=16$ and non-split $C^+(T)$ exist, e.g. $T=U\perp\langle10,-2,-4,-20\rangle$ | proved here |
| Proposition B.3 | the non-split class $\mathcal K$ is closed under Hodge similitude and disjoint from all covered cases, so no similitude-transport reaches it | proved here |
| Proposition B.4 | $\rho=16$ with an imaginary-quadratic action on $T$ (e.g. a non-symplectic automorphism of order 3, 4, 6) implies split $C^+$ | proved here |
| Proposition B.5 | $H^*(Y)\in\mathcal C_S$ implies $H^{odd}(Y)=0$: moduli of sheaves on $S$ carry no Kuga–Satake abelian variety | proved here (trivial) |
