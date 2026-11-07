# Attack 15: intrinsic Hodge-theoretic characterizations of algebraic classes

**Status (read this first).** The top target (a), a property $P(X,\alpha)$ of the variation of Hodge structure (VHS) through $X$ that is provably *equivalent* to algebraicity, is **not** reached. For the natural candidate $P=\mathcal G$ (absoluteness together with Galois-coherence of the Hodge locus, Definition 1.1), the direction "algebraic $\Rightarrow\mathcal G$" is proved, but it is known in substance (Deligne's Principle B, Voisin 2007). I also show that the converse already contains the Hodge conjecture for all abelian varieties and that its integral version is false (Proposition 1.3), so no Hodge-theoretic argument can supply it. For target (b) I prove only the case where the Hodge locus is the whole moduli. That case gives HC for very general very ample hypersurfaces in abelian fivefolds (via Markman) and in fivefolds with small $CH_0$ (Corollary 2.2): an immediate consequence of classical Lefschetz–Deligne theory. The case of an isolated Hodge locus is exactly the special-point problem, and it is blocked (Gap G2).

The main new result is **Theorem D** (§3), a contribution to targets (c) and (d). Let $Y$ be a positive-dimensional special subvariety of a geometric VHS over a number field. Suppose $Y$ is weakly non-factor, has maximal monodromy, and has a Mumford–Tate datum of abelian type with a Hodge-type cover. Then:

* every zero-dimensional special subvariety lying on $Y$ is a $\bar{\mathbb Q}$-point;
* Galois conjugates of CM points of $Y$ are CM points of $Y$;
* their rational Hodge structures obey Shimura–Taniyama reciprocity.

None of this assumes that any Hodge class is absolute. The proof takes the graph of the period map of $Y$ into a Shimura variety $M$ of Hodge type and shows that this graph is a special, weakly non-factor subvariety of $S\times M$. Klingler–Otwinowska–Urbanik then make the graph $\bar{\mathbb Q}$-rational, and CM theory is imported from $M$. §4 states what a CM theory for a general period domain must contain, and which of its parts are proved (here or in the literature).

*Sources.* arXiv and journal sites were blocked, and the web-search budget ran out during the session. The statements of KOU, Kreutz and Saito–Schnell were checked against abstracts and search excerpts only. The André–Oort theorem of Pila–Shankar–Tsimerman and the canonical-model facts (I7) are quoted from memory. Each such input is flagged where it is used.

## 0. Conventions and inputs

Throughout, $f\colon X\to S$ is a smooth projective morphism with $S$ smooth, connected and quasi-projective, both defined over a number field $L\subset\mathbb C$, and $\mathbb V=R^kf_*\mathbb Z/\mathrm{tors}$. This is a polarizable $\mathbb Z$-VHS whose algebraic de Rham incarnation $(\mathcal V,\nabla,F^\bullet)$ is defined over $L$. For $s\in S(\mathbb C)$, $\mathrm{MT}(V_s)\subset GL(V_{s,\mathbb Q})$ is the Mumford–Tate group.

For a closed irreducible $Z\subset S$ with normalization $Z^n$:

* $G_Z$ is the *generic Mumford–Tate group*, the MT group at a Hodge-generic point of $Z^n$;
* $H_Z$ is the *algebraic monodromy group*, the identity component of the Zariski closure of the monodromy of $\mathbb V|_{Z^n}$.

Both are defined up to parallel transport. $Z$ is **special** if it is maximal among closed irreducible subvarieties $W$ with $G_W=G_Z$; equivalently, $Z$ is an irreducible component of a Hodge locus. $Z$ is **weakly non-factor** (KOU, Def. 1.10) if there is no closed irreducible $W\supset Z$ such that $H_Z$ is a strict normal subgroup of $H_W$. A **CM point** is a point $s$ with $\mathrm{MT}(V_s)$ a torus. $\{s\}$ is **special** if every closed irreducible $W\ni s$ with $\dim W>0$ has $G_W\ne\mathrm{MT}(V_s)$.

Inputs used (exact form as used):

* **(I1)** Cattani–Deligne–Kaplan; Bakker–Klingler–Tsimerman: the locus where a given multivalued flat section of $\mathbb V^{\otimes}$ is Hodge is a countable union of closed algebraic subvarieties. In particular $S$ has only countably many special subvarieties.
* **(I2)** Generic Mumford–Tate lemma (Deligne; André 1992), for a normal irreducible $T$ carrying a polarizable $\mathbb Q$-VHS:
  * off a countable union of proper closed subsets, $\mathrm{MT}(V_t)$ equals a fixed group $G_T$;
  * for every $t$ and every path in $T$, the transported $\mathrm{MT}(V_t)$ is contained in $G_T$;
  * a finite-index subgroup of $\pi_1(T)$ maps into $G_T(\mathbb Q)$;
  * $H_T$ is semisimple (Deligne, Hodge II §4.2) and normal in $G_T^{\rm der}$ (André 1992).
* **(I3)** Theorem of the fixed part (Deligne, Hodge II §4.1). Lefschetz theory (SGA 7 XVIII; Deligne, Weil II §4.4): let $\mathcal L$ be very ample on a smooth projective $Y$ of dimension $n+1$ with $n$ even, and $X\in|\mathcal L|$ smooth. Then:
  * $H^n(X,\mathbb Q)=i^*H^n(Y,\mathbb Q)\oplus H^n_{\rm van}$, an orthogonal and monodromy-stable decomposition with trivial monodromy on the first summand;
  * $H^n_{\rm van}$ is spanned by vanishing cycles;
  * the Zariski closure of the monodromy on $H^n_{\rm van}$ is either finite or the full orthogonal group;
  * $i^*$ is injective on $H^n$.
* **(I4)** Principle B (Deligne, LNM 900, Thm. 2.12). For a smooth projective family over a smooth connected base, a global flat section of $R^{2p}$ that is Hodge everywhere and absolute Hodge at one point is absolute Hodge at every point.
* **(I5)** Klingler–Otwinowska–Urbanik (Ann. ENS 56 (2023), arXiv:2010.03359). Let $\mathbb V$ be a polarizable $\mathbb Z$-VHS on a smooth quasi-projective $S$ such that $S$ and $(\mathcal V,\nabla)$ are defined over a number field $L$. Then every special, weakly non-factor subvariety is defined over $\bar{\mathbb Q}$, and its $\mathrm{Aut}(\mathbb C/L)$-conjugates are special. *(Checked against the abstract and against Kreutz's restatement in arXiv:2111.00216 only.)* I use only "defined over $\bar{\mathbb Q}$", and only for VHS of geometric origin, for which every hypothesis holds.
* **(I6)** Borel's extension theorem (J. Diff. Geom. 6 (1972)). A holomorphic map from a smooth quasi-projective variety to $\Gamma\backslash\mathcal D$, with $\mathcal D$ a bounded symmetric domain and $\Gamma$ torsion-free arithmetic, is algebraic.
* **(I7)** Canonical models (Deligne 1971, 1979; Milne 2005), quoted from memory. Let $(G',X')$ be of Hodge type and $K'$ neat. Then:
  * $\mathrm{Sh}_{K'}(G',X')$ has a model over the reflex field carrying the universal abelian scheme;
  * CM points are $\bar{\mathbb Q}$-points;
  * if $x=[h,g]$ with $h$ factoring through a torus $T$, and $\sigma\in\mathrm{Aut}(\mathbb C/E(T,h))$ restricts to $\mathrm{art}(a)$ on $E(T,h)^{\rm ab}$, then $\sigma x=[h,r(a)g]$, where $r$ is the reflex norm;
  * Galois conjugates of CM points are CM;
  * Shimura subvarieties (images of sub-data) are defined over $\bar{\mathbb Q}$.
* **(I8)** Deligne (LNM 900): Hodge classes on abelian varieties are absolute Hodge.
* **(I9)** HC for abelian varieties of dimension $\le5$ (Markman, arXiv:2509.23403, as listed in `docs/02`). Bloch–Srinivas: $\mathrm{HC}(Y,2)$ holds if $CH_0(Y)$ is supported on a subvariety of dimension $\le3$.
* **(I10)** André–Oort for Shimura varieties (Pila–Shankar–Tsimerman, arXiv:2109.08788; Tsimerman 2018 for $\mathcal A_g$). *Not re-checked in this session.*
* **(I11)** Two facts on fundamental groups (e.g. Kollár, *Shafarevich maps*, §2.10). For a normal variety, $\pi_1$ of a dense Zariski-open subset surjects onto $\pi_1$. For a dominant morphism $A\to B$ of normal irreducible varieties, the image of $\pi_1(A)$ has finite index in $\pi_1(B)$. (Proof of the second: over a dense open $B^0$ the map is a topological fibre bundle whose fibre has finitely many components, and the homotopy sequence bounds the index.)

## 1. Target (a): a Hodge-theoretic characterization, and why only one direction is provable

**Definition 1.1 (property $\mathcal G$).** Let $X$ be a smooth projective complex variety and $\alpha\in\mathrm{Hdg}^p(X)$. A *model* of $(X,\alpha)$ consists of:

* a field $k\subset\mathbb C$ finitely generated over $\mathbb Q$;
* a smooth projective $k$-morphism $\pi\colon\mathcal X\to T$ with $T$ smooth and geometrically connected;
* a point $t_0\in T(\mathbb C)$ and an isomorphism $X\cong\mathcal X_{t_0}$.

Let $Z_\alpha\subset T_{\mathbb C}$ be the union of the irreducible components through $t_0$ of the Hodge locus of $\alpha$. This is the closure of the set of points at which some parallel transport of $\alpha$ along a path from $t_0$ remains Hodge, the transport staying inside the corresponding component of the étalé space of Hodge classes. It is algebraic by (I1).

$(X,\alpha)$ has **property $\mathcal G$** if for every model and every $\sigma\in\mathrm{Aut}(\mathbb C/k)$ the following hold.

* ($\mathcal G1$) For every $t\in Z_\alpha$ and every transport $\alpha_t$ of $\alpha$ within $Z_\alpha$, the conjugate $\sigma(\alpha_{t,\rm dR})\in H^{2p}_{\rm dR}(\mathcal X_{\sigma t}/\mathbb C)$ is the de Rham class of a rational Hodge class.
* ($\mathcal G2$) $\sigma$ maps the components of $Z_\alpha$ bijectively onto the components through $\sigma(t_0)$ of the Hodge locus of the rational class $\sigma(\alpha)$.
* ($\mathcal G3$) Every component of $Z_\alpha$ is defined over $\bar k$.

$\mathcal G$ is formulated purely in terms of the VHS of models of $X$, their Hodge loci, and their algebraic de Rham incarnation over $k$. The latter is the only "field of definition" information that a VHS of geometric origin carries.

**Proposition 1.2 (algebraic $\Rightarrow$ absolute $\Rightarrow\mathcal G$).** If $\alpha$ is absolute Hodge, in particular if $\alpha$ is algebraic, then $(X,\alpha)$ has $\mathcal G$. *Known in substance: Deligne LNM 900 §2; Voisin, Compositio 143 (2007); KOU and Kreutz call the resulting loci "absolutely special".*

*Proof.*

1. *Algebraic implies absolute.* If $\alpha=\sum a_i[W_i]$ then $\sigma(\alpha_{\rm dR})=\sum a_i[\sigma W_i]_{\rm dR}$, which is rational and Hodge.

2. *Proof of $\mathcal G1$.* Let $Z$ be a component of $Z_\alpha$.
   * *Finite monodromy.* The transports of $\alpha$ within $Z$ are Hodge classes, and their monodromy orbit is finite: monodromy preserves the polarization and the Lefschetz decomposition, and on the Hodge classes of each primitive piece $\pm Q$ is definite, so an integral class has only finitely many images.
   * *An algebraic base.* So $\alpha$ becomes single-valued on a connected finite étale cover of the smooth locus of $Z$, which is algebraic by Riemann's existence theorem. Let $\tilde Z'$ be a desingularization of the normalization of $Z$ in the function field of this cover. Then $\tilde Z'\to Z$ is proper and surjective, and $\alpha$ extends to a global flat section over $\tilde Z'$ (I11).
   * *Principle B.* This section is Hodge at every point, being Hodge on a dense set and Hodge-ness being a closed condition, and it is absolute Hodge at a point over $t_0$. Principle B (I4) on the smooth connected variety $\tilde Z'$ makes it absolute Hodge everywhere.

3. *Proof of $\mathcal G2$.* The de Rham section $\alpha_{\rm dR}$ is a flat section of a regular singular algebraic connection with trivial monodromy, hence algebraic. Gauss–Manin connections and Hodge filtrations commute with conjugation, so $\sigma(\alpha_{\rm dR})$ is a flat algebraic section over $\sigma(\tilde Z')$ lying in $F^p$, and by step 2 its value at every point is rational. A flat section of $\mathbb V_{\mathbb C}$ whose values are all rational is a section of $\mathbb V_{\mathbb Q}$. Hence $\sigma(Z)$ lies in the Hodge locus of $\sigma(\alpha)$, and so in one of its components $Z'$. The class $\sigma(\alpha)$ is again absolute, so the same argument with $\sigma^{-1}$ gives $\sigma^{-1}(Z')\subset Z''$ for some component $Z''$ of $Z_\alpha$. Then $Z\subset Z''$, so $Z=Z''$ because components are maximal, and $\sigma(Z)=Z'$.

4. *Proof of $\mathcal G3$.* By step 3 and (I1), $Z$ has only countably many $\mathrm{Aut}(\mathbb C/k)$-conjugates. A subvariety with countably many conjugates is defined over $\bar k$: its field of definition is finitely generated over $k$, and a transcendental generator would have an uncountable orbit. $\square$

**Proposition 1.3 (the converse is out of reach of Hodge theory).**

* (i) Every Hodge class on an abelian variety has property $\mathcal G$.
* (ii) Consequently, a proof of "$\mathcal G\Rightarrow$ algebraic" would prove HC for all abelian varieties, including CM abelian varieties and Weil classes in dimension $\ge6$, which are open (`docs/02` §2.2).
* (iii) The integral analogue is false: there are integral classes $\alpha\in H^{2p}(X,\mathbb Z)$ that are Hodge and have $\mathcal G$, yet are not integral combinations of subvarieties.

*Proof.*

* (i) Combine (I8) with Proposition 1.2. Any model of an abelian variety is, near $t_0$, a family of abelian varieties (or of torsors under them, which have the same cohomology), so (I8) applies at every point of $Z_\alpha$.
* (ii) Immediate from (i).
* (iii) Engel–de Gaay Fortman–Schreieder: on a very general principally polarized abelian variety of dimension $g\ge4$, the minimal class $\theta^{g-1}/(g-1)!$ is an integral Hodge class that is not the class of an integral 1-cycle. It is a rational multiple of the algebraic class $\theta^{g-1}$, so it has $\mathcal G$. $\square$

**Remark 1.4 (exact statement needed for the top target).** With $P=\mathcal G$, target (a) is equivalent to the conjunction of two statements:

* $(\star)$: every absolute Hodge class is algebraic;
* Deligne's conjecture: every Hodge class is absolute.

By Voisin 2007, $(\star)$ reduces to varieties over $\bar{\mathbb Q}$. I cannot prove $(\star)$, and Proposition 1.3 shows why no refinement of $\mathcal G$ will help. Absoluteness, Galois-coherence and field of definition are already *true* for all Hodge classes on abelian varieties, where the missing ingredient is a cycle-producing mechanism (M1–M6 of `docs/03`), not information about the VHS. The same holds for the other "intrinsic" data the ladder suggests:

* the IVHS kernel $T_{t_0}Z_\alpha=\ker(\bar\nabla\alpha\colon T_{t_0}T\to H^{p-1,p+1})$;
* atypicality;
* the Mumford–Tate group at special points.

All of these are determined by the VHS germ together with its $k$-structure, and that data is identical for algebraic classes and for any hypothetical non-algebraic absolute class. This is Gap G1.

*Projectivity.* $\mathcal G$ is defined only through models over finitely generated fields, which exist only for projective (algebraic) $X$. For Voisin's non-algebraic tori, $\mathcal G$ is undefined rather than satisfied. *Coefficients.* $\mathcal G$ is invariant under $\alpha\mapsto n\alpha$, and by 1.3(iii) any proof of "$\mathcal G\Rightarrow$ algebraic" must use $\mathbb Q$-coefficients.

## 2. Target (b): transversally rigid classes

Call $\alpha\in\mathrm{Hdg}^p(X_{t})$ *rigid of the first kind* in a family if its Hodge locus is the whole base, and *rigid of the second kind* if its Hodge locus is an isolated point.

**Proposition 2.1.** Let $Y$ be smooth projective of dimension $2p+1$, let $\mathcal L$ be very ample, and let $U\subset|\mathcal L|$ be the open set of smooth members $X_t$. Assume that $H^{2p}_{\rm van}(X_t)$ is not purely of type $(p,p)$. Then for very general $t\in U$:

* (i) every $\alpha\in\mathrm{Hdg}^p(X_t)$ is rigid of the first kind;
* (ii) $\mathrm{Hdg}^p(X_t)=i_t^*\,\mathrm{Hdg}^p(Y)$.

*Proof.*

(i) For each $\alpha\in H^{2p}(X_{t_0},\mathbb Q)$ and each path class, the Hodge locus is analytic in the universal cover $\tilde U$. If it is proper, its image lies in a countable union of proper closed subsets of $U$ (I1). There are countably many such data, so a very general $t$ avoids every proper one. At such $t$, every Hodge class has all of its transports Hodge. Its $\pi_1(U)$-orbit therefore consists of integral Hodge classes of fixed norm in a definite lattice (as in the proof of 1.2), and is finite. So some finite-index $\Pi\subset\pi_1(U,t)$ fixes $\alpha$.

(ii) Write $H^{2p}(X_t,\mathbb Q)=i^*H^{2p}(Y)\oplus H_{\rm van}$ as in (I3). The monodromy of $\pi_1(U)$ equals that of a general Lefschetz pencil, by Zariski's theorem on complements of the discriminant.

*The monodromy on $H_{\rm van}$ is infinite.* Suppose it were finite. On a finite étale cover the monodromy is trivial, so by the fixed-part theorem the Hodge structure is constant, and every Picard–Lefschetz reflection $T_\delta x=x\pm(x\cdot\delta)\delta$ is an automorphism of it. If a vanishing cycle $\delta$ had a component $\delta^{a,b}\neq0$ with $a\ne b$, pick $x\in H^{b,a}$ with $x\cdot\delta\ne0$; then $T_\delta x-x\in H^{b,a}$ is a non-zero multiple of $\delta$, a contradiction. So all vanishing cycles, and hence $H_{\rm van}$, would be of type $(p,p)$, which is excluded.

*Conclusion.* By (I3) the Zariski closure of the monodromy on $H_{\rm van}$ contains $SO(H_{\rm van})$, and so does that of $\Pi$, since a finite-index subgroup has the same identity component. As $\dim H_{\rm van}\ge2$, this has no non-zero invariants. So $\alpha=i^*\beta$ with $\beta\in H^{2p}(Y,\mathbb Q)$. Since $i^*$ is an injective morphism of Hodge structures (I3), it is strict, so $\beta\in F^p$ and $\beta\in\mathrm{Hdg}^p(Y)$. $\square$

**Corollary 2.2 (HC for very general hypersurface sections).** Under the hypotheses of 2.1, if $\mathrm{HC}(Y,q)$ holds for all $q\le p$, then HC holds in every degree for $X_t$ with $t$ very general.

*Proof.*

* Degrees $2q<2p$: the Lefschetz hyperplane theorem makes $i^*$ an isomorphism of Hodge structures, and $i^*[W]=[W\cdot X_t]$.
* Degree $2p$: Proposition 2.1.
* Degrees $>2p$: hard Lefschetz on $X_t$ (`docs/01` §1.2.3). $\square$

Two instances. Both are immediate, and I have not seen either stated.

* **(a) $Y$ an abelian fivefold** (by I9). Here $K_{X_t}=\mathcal L|_{X_t}$ is ample. From $0\to\mathcal O_Y\to\mathcal L\to\mathcal L|_{X_t}\to0$, with $h^1(\mathcal O_Y)=5$ and $h^1(\mathcal L)=0$, we get $h^{4,0}(X_t)=h^0(\mathcal L)+4$. Since $i^*H^{4,0}(Y)$ has dimension 5, $\dim H^{4,0}_{\rm van}=h^0(\mathcal L)-1>0$. So: **HC holds for very general very ample hypersurfaces in abelian fivefolds.** These are fourfolds of general type.
* **(b) $CH_0(Y)$ supported on a subvariety of dimension $\le3$**, e.g. $Y$ rationally connected, such as $Y=\mathbb P^1\times(\text{cubic fourfold})$, where $h^{3,1}(Y)=1$. Then $\mathrm{HC}(Y,2)$ holds by Bloch–Srinivas and $H^{4,0}(Y)=0$. If $K_Y+\mathcal L$ is very ample, then $H^{4,0}_{\rm van}=H^{4,0}(X_t)\neq0$. Bloch–Srinivas does *not* apply to $X_t$ itself: since $h^{4,0}(X_t)\neq0$, $CH_0(X_t)$ is not supported in dimension $\le3$.

The content of (b) is the classical "very general members only carry classes from the ambient space". I record it because target (b) asks for a new class. The novelty is the class of varieties, not the method.

**Remark 2.3 (rigid of the second kind = zero-dimensional special).** Suppose $\alpha\in\mathrm{Hdg}^p(X_s)$ has isolated Hodge locus $\{s\}$. Then $\{s\}$ is special. Indeed, if $W\ni s$ is closed irreducible with $G_W=\mathrm{MT}(V_s)$, then $\alpha$ is $G_W$-invariant, hence Hodge along $W^n$ by (I2), so $W\subset\{s\}$.

So second-kind rigid classes live exactly at zero-dimensional special subvarieties: CM points, and transversal intersection points of $\Phi(S)$ with Mumford–Tate subdomains. At CM points of moduli of abelian varieties these include the open cases of HC for CM abelian varieties (`docs/02` §2.2). No step of this strategy produces cycles there. What *can* be proved about such points is their arithmetic, which is §3. This is Gap G2.

## 3. Targets (c)/(d): CM theory on special subvarieties of abelian type (Theorem D)

**3.0 Setting.** Let $f,L,\mathbb V$ be as in §0. Let $Y\subset S_{\mathbb C}$ be a special subvariety of positive dimension whose generic Mumford–Tate group $G_Y$ is not a torus. Fix a Hodge-generic point $y_0$, and write $V:=V_{y_0,\mathbb Q}$, $h_0\colon\mathbb S\to G_{Y,\mathbb R}$ for the Hodge cocharacter at $y_0$, and $D_Y^+:=G_Y(\mathbb R)^+h_0$. The hypotheses are:

* **(H1)** $Y$ is weakly non-factor.
* **(H2)** $H_Y=G_Y^{\rm der}$, i.e. the VHS on $Y$ has no constant factor.
* **(H3)** There are:
  * a Shimura datum $(G',X')$ of Hodge type, with a symplectic embedding $\rho_0\colon G'\hookrightarrow GSp(W_0)$ (weight $-1$ on $W_0$);
  * a surjection $\pi\colon G'\to G_Y$ with central kernel;
  * a point $h_0'\in X'$ with $\pi\circ h'_0=h_0$.

  Put $X'^+:=G'(\mathbb R)^+h_0'$.

Examples for (H3): $\pi=\mathrm{id}$ if $(G_Y,D_Y)$ is itself of Hodge type. If $D_Y$ is of K3 type, so $G_Y\subset SO(V)$, take $G'=\pi^{-1}(G_Y)\subset GSpin(V)$ with the spin representation (Kuga–Satake). (H3) forces $(G_Y,D_Y^+)$ to be a Shimura datum of abelian type.

**Lemma 3.1 (the period map of $Y$ lands in a Hodge-type Shimura variety).** Assume (H3).

* (a) There is a $G'$-equivariant injection $\iota\colon V\hookrightarrow T:=\bigoplus_iW_0^{\otimes a_i}\otimes W_0^{\vee\otimes b_i}$ with $b_i-a_i=k$, where $G'$ acts on $V$ through $\pi$, together with an equivariant projector onto its image. For every $h'\in X'$, $\iota$ is a morphism of Hodge structures $(V,\pi h')\to(T,T(\rho_0)h')$.
* (b) The map $h'\mapsto\pi\circ h'$ is a $G'(\mathbb R)^+$-equivariant biholomorphism $X'^+\to D_Y^+$.
* (c) There is a neat congruence subgroup $\Gamma\subset G'(\mathbb Q)$ preserving $X'^+$ and a lattice $W_{0,\mathbb Z}$, with $\pi(\Gamma)\subset GL(V_{\mathbb Z})$, such that:
  * $M:=\Gamma\backslash X'^+=\pi(\Gamma)\backslash D_Y^+$ is a connected Shimura variety;
  * $M$ and its universal abelian scheme $a\colon A\to M$ are defined over a number field (I7);
  * $\iota$ induces a flat embedding of VHS $\mathbb V_M\hookrightarrow T(\mathbb W')$ onto a flat Hodge direct summand, where $\mathbb W':=(R^1a_*\mathbb Z)^\vee$ and $\mathbb V_M:=\pi(\Gamma)\backslash(D^+_Y\times V)$.
* (d) There are a normal irreducible variety $\tilde Y$, a finite surjection $c\colon\tilde Y\to Y$, and a morphism $\Phi\colon\tilde Y\to M$ with $c^*\mathbb V_{\mathbb Q}\cong\Phi^*\mathbb V_M$ as VHS. Consequently there is a flat section $\psi$ of $\mathcal Hom(c^*\mathbb V,\Phi^*T(\mathbb W'))$ over $\tilde Y$ that is an injective morphism of Hodge structures at every point.

*Proof.*

(a) Since $\rho_0$ is faithful, every representation of $G'$ is a subquotient of a sum of the $T^{a,b}(W_0)$ (Deligne–Milne, *Tannakian categories*, Prop. 2.20). Since $G'$ is reductive, it is in fact a direct summand. The weight cocharacter is scalar on $W_0$, hence central and defined over $\mathbb Q$. $V$ is pure of weight $k$, so $\iota$ may be taken into the summands with $b-a=k$. Equivariance gives compatibility with every $h'$.

(b) Equivariance is clear, and surjectivity holds because $\pi(G'(\mathbb R)^+)=G_Y(\mathbb R)^+$. For injectivity: on a Shimura datum, $h\mapsto(\mathrm{ad}\circ h,\mathrm{ab}\circ h)$ is injective, since $G\to G^{\rm ad}\times G^{\rm ab}$ has finite kernel and $\mathbb S$ is connected. Moreover $\mathrm{ab}\circ h$ is constant on $X'^+$, and $\pi$ identifies $G'^{\rm ad}=G_Y^{\rm ad}$. So $\pi h_1'=\pi h_2'$ forces $\mathrm{ad}\,h'_1=\mathrm{ad}\,h'_2$ and hence $h'_1=h'_2$. Both complex structures are induced by the Hodge filtration on $\mathrm{Lie}\,G'^{\rm ad}=\mathrm{Lie}\,G^{\rm ad}_Y$, so the map is a biholomorphism.

(c) Take a neat compact open $K'\subset G'(\mathbb A_f)$ stabilizing $\hat W_{0,\mathbb Z}$ and contained in $\pi^{-1}(\mathrm{Stab}\,\hat V_{\mathbb Z})$, and set $\Gamma:=G'(\mathbb Q)_+\cap K'$. Central elements act trivially on $X'^+$, so $\Gamma$ acts through $\pi(\Gamma)$, which is neat (Borel), and (b) gives $\Gamma\backslash X'^+=\pi(\Gamma)\backslash D_Y^+$. For any $\Gamma$-module $(U_0,\rho)$ with a stable lattice, $\Gamma\backslash(X'^+\times U_0)$ with Hodge structure $\rho\circ h'$ is a polarizable VHS (SV1 gives transversality). For $\rho_0$ this is $\mathbb W'$ by the moduli interpretation; for $\pi$ it is $\mathbb V_M$. $\Gamma$-equivariance of $\iota$ gives the flat morphism.

(d) *Reducing the monodromy.* By (I2), a finite-index subgroup of $\pi_1$ of the smooth locus $Y^0$ of $Y^n$ maps into $G_Y(\mathbb Q)\cap GL(V_{\mathbb Z})$. This group is commensurable with the arithmetic group $\pi(\Gamma)$, so some connected finite étale $Y^1\to Y^0$ has monodromy in $\pi(\Gamma)$.

*The period points lie in $D_Y^+$.* The period points of $Y^1$ factor through $G_{Y,\mathbb R}$ (I2). The set $\{h\in D:h(\mathbb S)\subset G_{Y,\mathbb R}\}$ is a disjoint union of open-and-closed $G_Y(\mathbb R)$-orbits, by rigidity of homomorphisms out of the torus $\mathbb S$. Hence the lifted period map lands in $D_Y^+$ and descends to a holomorphic $\Phi^1\colon Y^1\to M$ with $\mathbb V|_{Y^1}\cong(\Phi^1)^*\mathbb V_M$. By (I6), $\Phi^1$ is algebraic.

*Extending over $\tilde Y$.* Let $\tilde Y$ be the normalization of $Y^n$ in the function field of $Y^1$. Since $\pi_1(Y^1)\to\pi_1(\tilde Y)$ is onto (I11), the monodromy of $c^*\mathbb V$ on $\tilde Y$ still lies in $\pi(\Gamma)$. The lifted period map is continuous with values in the closed set $D_Y^+$. So $\Phi^1$ extends continuously, hence holomorphically by normality, to $\Phi\colon\tilde Y\to M$. It is algebraic because its graph is the Zariski closure of the graph of $\Phi^1$. Finally, $\psi:=\Phi^*\iota$ is flat on $Y^1$ and extends to $\tilde Y$ (I11). It is Hodge on a dense set, hence everywhere, since being Hodge is a closed condition. $\square$

Put $\mathbb U:=\mathrm{pr}_1^*\mathbb V\oplus\mathrm{pr}_2^*\mathbb W'$ on $S\times M$, and $\bar\Gamma:=(c,\Phi)(\tilde Y)\subset S\times M$.

**Lemma 3.2.** $\bar\Gamma$ is closed and irreducible, $p_1\colon\bar\Gamma\to Y$ is finite and surjective, and $\bar\Gamma$ is a special subvariety of $S\times M$ for $\mathbb U$.

*Proof.*

*Closedness and finiteness.* The composite $p_1\circ(c,\Phi)=c$ is finite, so $(c,\Phi)$ is proper and its image $\bar\Gamma$ is closed. Also $p_1|_{\bar\Gamma}$ is proper (it is dominated by a surjection with proper composite) and quasi-finite, hence finite.

*Specialness.* Choose $b_0\in\tilde Y$ whose images in $Y$ and in $\bar\Gamma$ are Hodge-generic; this is possible because the bad sets are countable unions of proper closed subsets and $c$ is finite. Then $G_{\bar\Gamma}:=\mathrm{MT}(\mathbb U_{b_0})$ projects onto $G_Y$. Suppose some closed irreducible $Z'\supsetneq\bar\Gamma$ has $G_{Z'}=G_{\bar\Gamma}$.

1. *$p_1(Z')\subset Y$.* By (I2) on $Z'^n$, every $G_{\bar\Gamma}$-invariant tensor stays Hodge along paths in $Z'^n$. This applies in particular to the pull-backs of the $G_Y$-invariant tensors of $V$. So at a Hodge-generic point of $Y_1:=\overline{p_1(Z')}$ lying in $p_1(Z')$, the Mumford–Tate group is contained in a transport of $G_Y$. Since $G_Y\subset G_{Y_1}$ and MT groups are connected, $G_{Y_1}=G_Y$, and maximality of $Y$ gives $Y_1=Y$.

2. *The fibres of $Z'\to Y$ are finite.* Let $(y,x)\in Z'$, and let $\gamma$ be a path in $Z'^n$ from $b_0$ to a point over $(y,x)$. The tensor $\psi_{b_0}$ is Hodge, hence $G_{\bar\Gamma}$-invariant, so its transport along $\gamma$ is Hodge. In the trivialization over the universal covers, this says that $\iota$ is a morphism of Hodge structures between the endpoint lifts. By 3.1(a) and injectivity of $\iota$, $\tilde h_y=\pi\circ\tilde h'_x$, so by 3.1(b) $\tilde h'_x$ is determined by $\tilde h_y$. Thus $\{x:(y,x)\in Z'\}$ is countable, hence finite, being algebraic.

So $\dim Z'\le\dim Y=\dim\bar\Gamma$, which contradicts $Z'\supsetneq\bar\Gamma$. $\square$

**Lemma 3.3.** Assume (H1) and (H2). Then $H_{\bar\Gamma}=\{(\pi(g),\rho_0(g)):g\in G'^{\rm der}\}$, and $\bar\Gamma$ is weakly non-factor.

*Proof.*

*Computing $H_{\bar\Gamma}$.* $\tilde Y\to\bar\Gamma^n$ is finite and surjective, so by (I11) $H_{\bar\Gamma}$ can be computed on $\tilde Y$. There the monodromy of $\mathbb U$ is $\gamma\mapsto(\pi(\phi\gamma),\rho_0(\phi\gamma))$, where $\phi=\Phi_*\colon\pi_1(\tilde Y)\to\Gamma$. Let $H':=\overline{\phi(\pi_1\tilde Y)}^{\,0}$. It is semisimple (I2), so $H'\subset G'^{\rm der}$, and $\pi(H')=H_Y=G_Y^{\rm der}$ by (H2). Since $\pi\colon G'^{\rm der}\to G_Y^{\rm der}$ is an isogeny, $H'=G'^{\rm der}$.

*Weak non-factor property.* Suppose $\bar\Gamma\subset W$ with $W$ closed irreducible and $H_{\bar\Gamma}\triangleleft H_W$ strictly. Let $W_i:=\overline{p_i(W)}$. By (I11) applied to $W^n\to W_i^n$, $p_i(H_W)=H_{W_i}$. Since $H_{\bar\Gamma}$ is connected semisimple and normal in the connected group $H_W$, we have $H_W=H_{\bar\Gamma}\cdot C$ with $C:=Z_{H_W}(H_{\bar\Gamma})^0$, and $\dim C>0$ by strictness.

* *$p_2(C)$ is trivial.* It commutes with $\rho_0(G'^{\rm der})$ and lies in $H_{W_2}\subset H_M$, which is semisimple and hence contained in $\rho_0(G'^{\rm der})$. So $p_2(C)$ lies in a finite centre, and being connected it is trivial.
* *Contradiction with (H1).* Therefore $p_1(C)$ is positive-dimensional, centralizes $H_Y$, and $H_{W_1}=p_1(H_W)=H_Y\cdot p_1(C)$. So $H_Y$ is a strict normal subgroup of $H_{W_1}$ with $Y\subset W_1$, contradicting (H1). $\square$

**Theorem D (CM points on special subvarieties of abelian type).** Assume 3.0 together with (H1), (H2) and (H3).

* **(D1)** $Y$, $\bar\Gamma$ and $\tilde Y\to\bar\Gamma$ are defined over $\bar{\mathbb Q}$. Fix a number field $K\supset L$ over which these, $M$ and $A$ are defined.
* **(D2)** If $y\in Y(\mathbb C)$ and $\{y\}$ is a special subvariety of $S$, then $y\in Y(\bar{\mathbb Q})$. This covers every CM point of $Y$ at which the period map of $\mathbb V$ is quasi-finite. It also covers non-CM isolated points of Hodge loci lying on $Y$.
* **(D3)** Let $y\in Y(\mathbb C)$ be a CM point. Then $\sigma(y)$ is a CM point of $Y$ for every $\sigma\in\mathrm{Aut}(\mathbb C/K)$. Moreover, if $(y,x)\in\bar\Gamma$ and $\sigma$ also fixes the reflex field $E_x$ of the CM point $x\in M$, then $V_{\sigma(y)}\cong V_y$ as rational Hodge structures, and the integral structure of $V_{\sigma(y)}$ is obtained from that of $V_y$ through $\pi$ and the reflex norm, by the classical Shimura–Taniyama rule on $M$ (I7).

No Hodge class is assumed to be absolute Hodge.

*Proof.*

**(D1).** $\mathbb U$ is built from the Gauss–Manin systems of $X\to S$ and $A\to M$, by pull-back, duality and direct sum. So $S\times M$ and the flat bundle of $\mathbb U$ are defined over a number field, which is the hypothesis of (I5). By Lemmas 3.2 and 3.3, $\bar\Gamma$ is special and weakly non-factor, so (I5) shows that $\bar\Gamma$ is defined over $\bar{\mathbb Q}$; hence so is $Y=p_1(\bar\Gamma)$. Next, $\tilde Y\to\bar\Gamma$. Let $\bar\Gamma^0\subset\bar\Gamma$ be the complement of $p_1^{-1}(Y\smallsetminus Y^{\rm sm})$ and of the locus where $p_1$ is not étale. It is a dense open subset defined over $\bar{\mathbb Q}$: it is cut out from the $\bar{\mathbb Q}$-morphism $p_1\colon\bar\Gamma\to Y$, which is generically étale in characteristic 0. Over $Y^{\rm sm}$, $\tilde Y$ coincides with the finite étale cover $Y^1$ of 3.1(d), so $\tilde Y\to\bar\Gamma$ is finite étale over $\bar\Gamma^0$. Finite étale covers of $\bar\Gamma^0_{\mathbb C}$ descend to $\bar{\mathbb Q}$, by invariance of $\pi_1^{\rm et}$ under extension of algebraically closed fields in characteristic 0 (SGA 1, XIII 4.6). Since $\tilde Y$ is the normalization of $\bar\Gamma$ in the function field of that cover, $\tilde Y\to\bar\Gamma$ is defined over $\bar{\mathbb Q}$.

**(D2).** Pick $b\in\tilde Y$ with $c(b)=y$ and put $x=\Phi(b)$. Let $G_y=\mathrm{MT}(V_y)$ and $G^\prime_x=\mathrm{MT}(W^\prime_x)$; then $\pi(G^\prime_x)=G_y$, since the image of a Mumford–Tate group is the Mumford–Tate group of the image. Let $M_x$ be the special subvariety of $M$ through $x$ with generic Mumford–Tate group $G^\prime_x$. It is $\{x\}$ when $G^\prime_x$ is a torus and a Shimura subvariety otherwise. In both cases $M_x$ and its normalization $M_x^n\to M$ are defined over $\bar{\mathbb Q}$ (I7).

Let $B_0$ be an irreducible component, through a point $(b,\tilde x)$, of the $\bar{\mathbb Q}$-scheme $\tilde Y\times_MM_x^n$. Take a path $\beta$ in $B_0$ from $(b,\tilde x)$ and a tensor $t\in T(V_y)^{G_y}$. Then $\iota_*t$ is $G^\prime_x$-invariant, so it stays Hodge along the image path in $M_x^n$ (I2). By flatness of $\psi$, the transport of $t$ along $c(\beta)$ is also Hodge.

Hence $Y_2:=c(\mathrm{pr}_1B_0)$, which is closed because the maps involved are finite, is irreducible, contains $y$, and has $G_{Y_2}=G_y$. Since $\{y\}$ is special, $Y_2=\{y\}$. So $B_0$ is finite, i.e. $(b,\tilde x)$ is an isolated point of a $\bar{\mathbb Q}$-scheme. Therefore it is a $\bar{\mathbb Q}$-point, and $y=c(b)\in S(\bar{\mathbb Q})$.

*The quasi-finite CM case.* If $y$ is CM and the period map is quasi-finite at $y$, then $\{y\}$ is special. Indeed, any $W\ni y$ with $G_W=G_y$ has its period points in the discrete set $D^{G_y}$, so $W$ lies in a fibre of the period map and $W=\{y\}$.

**(D3).** Since $\ker\pi$ is central, $\mathrm{MT}(W^\prime_x)$ is a torus if and only if $\mathrm{MT}(V_y)$ is: their derived groups are isogenous.

*$\sigma(y)$ is CM.* Take $\sigma\in\mathrm{Aut}(\mathbb C/K)$. Then $\sigma(b)$ lies over $(\sigma y,\sigma x)\in\bar\Gamma$. The abelian variety $A_{\sigma x}=\sigma(A_x)$ is CM, since being CM is an algebraic condition, so $\sigma x$ is a CM point. The isomorphism $\psi_{\sigma(b)}$ embeds $V_{\sigma y}$ into $T(W^\prime_{\sigma x})$ as a sub-Hodge structure, so $\mathrm{MT}(V_{\sigma y})$ is a torus.

*Reciprocity.* Suppose $\sigma$ also fixes $E_x$. Write $x=[\tilde h_x,1]$. By (I7), $\sigma x=[\tilde h_x,r(a)]$, and since $\sigma M=M$ this equals $[q\tilde h_xq^{-1},1]$ for some $q\in G^\prime(\mathbb Q)$ with $q\,r(a)\in K^\prime$. Lemma 3.1(d) at $\sigma(b)$ then gives
$$V_{\sigma y}\cong(V,\pi(q)\,\pi\tilde h_x\,\pi(q)^{-1})\cong(V,\pi\tilde h_x)\cong V_y$$
via $\pi(q)\in G_Y(\mathbb Q)$, with lattice $\pi(q)^{-1}V_{\mathbb Z}$. $\square$

**Corollary 3.4 (the case $Y=S$).** Suppose (H2) and (H3) hold for $Y=S$; note that $S$ is trivially special and weakly non-factor. Then every zero-dimensional special subvariety of $S$ is a $\bar{\mathbb Q}$-point, and Galois conjugates of CM points are CM.

*Consistency check.* Take moduli of polarized K3 surfaces with level structure. Here $G_S=SO(V_{\rm prim})$ (Zarhin), the monodromy is Zariski dense in $SO$, and $G^\prime=GSpin$. The corollary recovers two known facts: CM K3 surfaces are defined over number fields, and their conjugates are CM (Pjateckii-Shapiro–Shafarevich; Rizov). The route is different: it uses (I5) where the classical proof uses Deligne's absoluteness of the Kuga–Satake correspondence.

**Corollary 3.5 (Galois orbits).** Let $y\in Y(\bar{\mathbb Q})$ be CM, and let $b\in\tilde Y$ lie over $(y,x)$. Then
$$[K(x):K]\le N\,[K(y):K],\qquad N:=\max_{z\in Y}\#c^{-1}(z)<\infty.$$
Hence any lower bound for Galois orbits of CM points of $M$ (I10) transfers to CM points of $Y$, up to the constant $N$.

*Proof.* $c$ is defined over $K$, so the $\mathrm{Gal}(\bar{\mathbb Q}/K(y))$-conjugates of $b$ lie in $c^{-1}(y)$. Hence $[K(b):K(y)]\le N$, and $K(x)\subset K(b)$. $\square$

**Corollary 3.6 (André–Oort on $Y$).** In the setting of Theorem D, the CM points of $Y$ are Zariski dense in $Y$ if and only if $\Phi\colon\tilde Y\to M$ is dominant. The direction $\Rightarrow$ assumes (I10).

*Proof.*

* $\Leftarrow$: CM points are dense in $M$. Since $\Phi$ is dominant, their preimages are dense in $\tilde Y$. By the first step of the proof of (D3) (a point $y$ is CM exactly when $x$ is), their images under $c$ are CM points, and they are dense in $Y$.
* $\Rightarrow$: Let $\Sigma\subset Y$ be a dense set of CM points. Then $c^{-1}\Sigma$ is dense in $\tilde Y$, so $\Phi(c^{-1}\Sigma)$ is a dense set of CM points in $M_Y:=\overline{\Phi(\tilde Y)}$. By (I10), $M_Y$ is special. Its generic Mumford–Tate group contains the monodromy group $G^{\prime\,\rm der}$ (Lemma 3.3 and I2). Since $G^{\prime\,\rm der}(\mathbb R)^+$ acts transitively on $X^{\prime+}$, we get $M_Y=M$. $\square$

**Remark 3.7 (where Pila–Wilkie and Ax–Schanuel enter).** A Pila–Zannier proof of André–Oort for special points of a general VHS needs five inputs:

* (PZ1) definability of the period map (Bakker–Klingler–Tsimerman);
* (PZ2) Ax–Lindemann (Bakker–Tsimerman);
* (PZ3) Galois stability of special points;
* (PZ4) Galois lower bounds;
* (PZ5) polynomial height bounds for pre-special points in Siegel sets of the Mumford–Tate domain.

Theorem D(D3) gives (PZ3) on $Y$, and Corollary 3.5 gives (PZ4) on $Y$. On such $Y$, however, André–Oort already follows from (I10) applied to $M$; that is Corollary 3.6, where the o-minimal input sits inside (I10). For VHS not of abelian type, none of (PZ3)–(PZ5) is available to me (Gap G6). So my route to target (c) goes through KOU (I5) and the Shimura variety $M$, not through a new point count.

## 4. Target (d): what a CM theory for a general period domain must contain

**Conjecture 4.0 (CM for geometric VHS).** Let $f,L,\mathbb V$ be as in §0. Let $s\in S(\mathbb C)$ be a CM point with $\{s\}$ special, $T=\mathrm{MT}(V_s)$, $\mu$ its Hodge cocharacter, and $E=E(T,\mu)$ the reflex field.

* **(CM1)** $s\in S(\bar{\mathbb Q})$.
* **(CM2)** For every $\sigma\in\mathrm{Aut}(\mathbb C/L)$, $\sigma(s)$ is a CM point, $\{\sigma(s)\}$ is special, and $\mathrm{MT}(V_{\sigma s})$ is isogenous to $T$.
* **(CM3)** There is a number field $K\supset LE$ with $s\in S(K)$ such that every $\sigma\in\mathrm{Aut}(\mathbb C/K)$ with $\sigma|_{E^{\rm ab}}=\mathrm{art}(a)$ satisfies:
  * $V_{\sigma s}\cong V_s$ as rational Hodge structures, with the lattice moved by $r_\mu(a)$;
  * $\mathrm{Gal}(\bar{\mathbb Q}/K)$ acts on $H^k_{\rm et}(X_{\bar s},\mathbb Q_\ell)$ through $T(\mathbb Q_\ell)$, by the $\ell$-adic character attached to $r_\mu$.
* **(CM4)** Converse: if $s^\prime\in S(\bar{\mathbb Q})$ and its period point in the compact dual $\check D$ (Betti $\mathbb Q$-structure) is $\bar{\mathbb Q}$-rational, then $s^\prime$ is CM.

For abelian varieties, (CM1)–(CM3) are Shimura–Taniyama theory and (CM4) is Cohen and Shiga–Wolfart (via Wüstholz).

**Lemma 4.1.** At a CM point, the Hodge filtration is defined over the splitting field of $T$, a number field. In particular the period point lies in $\check D(\bar{\mathbb Q})$.

*Proof.* $F^p=\bigoplus V_\chi$, where the sum runs over the characters $\chi$ of $T$ whose $\mu$-weight is $\ge p$, and each eigenspace $V_\chi$ is defined over the splitting field. $\square$

**Proposition 4.2 ((CM1), (CM2) from absoluteness; known, Voisin's argument).** Let $t_1,\dots,t_m$ be rational Hodge tensors at $s$ whose common stabilizer is $T$. If every $t_i$ is absolute Hodge, then (CM1) and (CM2) hold at $s$.

*Proof.*

* *The Hodge locus moves with $\sigma$.* The formal germ at $s$ of the locus where the flat continuations of the $t_{i,\rm dR}$ stay in $F^0$ is defined algebraically from $(\mathcal V,\nabla,F,t_{i,\rm dR})$. So $\sigma$ carries it to the corresponding germ at $\sigma(s)$ for the classes $\sigma(t_{i,\rm dR})$, which are rational Hodge tensors by absoluteness.
* *That germ is a point.* Its reduction at $s$ is $\{s\}$: an irreducible positive-dimensional $W\ni s$ inside it would have $G_W=T$, contradicting the specialness of $\{s\}$. Hence $\sigma(s)$ is an isolated point of the Hodge locus of $\{\sigma t_i\}$.
* *(CM1).* By (I1) there are only countably many isolated points of Hodge loci, so the $\mathrm{Aut}(\mathbb C/L)$-orbit of $s$ is countable and $s\in S(\bar{\mathbb Q})$.
* *(CM2).* $\mathrm{Stab}(\sigma t_i)$ is a $\mathbb Q$-form of $\sigma(T_{\mathbb C})$, hence a torus, so $\sigma(s)$ is CM. The point $\sigma(s)$ is isolated in the Hodge locus of $\{\sigma t_i\}$, and every $W\ni\sigma(s)$ with $G_W=\mathrm{MT}(V_{\sigma s})$ lies in that locus; hence $\{\sigma s\}$ is special. $\square$

With the theory of CM absolute-Hodge motives (Deligne, Milne in LNM 900), absoluteness also gives (CM3).

**Proposition 4.3 ((CM4) from the Grothendieck period conjecture; folklore).** Let $s\in S(\bar{\mathbb Q})$ have a $\bar{\mathbb Q}$-rational period point. Assume that the $\bar{\mathbb Q}$-Zariski closure of the period isomorphism $P\in\mathrm{Isom}(H_{\rm dR}(X_s/\bar{\mathbb Q}),H_B\otimes\bar{\mathbb Q})(\mathbb C)$ is a component of a torsor under André's motivated Galois group $G_{\rm mot}$. Then $s$ is CM.

*Proof.*

* *$G_{\rm mot}^0$ fixes the Hodge filtration.* The filtration $F_{\rm dR}$ is $\bar{\mathbb Q}$-rational, and so is $F_B=P^{-1}F_{\rm dR}$. The condition $g^{-1}F_{\rm dR}=F_B$ is $\bar{\mathbb Q}$-closed and holds at $P$, so it holds on the whole component. Hence $G_{\rm mot}^0$ stabilizes $F_B$.
* *So does $\mathrm{MT}$.* $\mathrm{MT}$ is connected and contained in $G_{\rm mot}$, so it stabilizes $F_B$.
* *$\mathrm{MT}$ is a torus.* $\mathrm{Lie}\,\mathrm{MT}$ is real, so $\mathrm{Lie}\,\mathrm{MT}\subset F^0\cap\overline{F^0}=\mathrm{End}^{0,0}$. Thus $h(\mathbb S)$ centralizes $\mathrm{MT}$, so $h(\mathbb S)$ lies in the centre of $\mathrm{MT}$, which is a $\mathbb Q$-group. By minimality $\mathrm{MT}$ equals its centre, and is therefore a torus. $\square$

**Corollary 4.4 ((CM4) on $Y$, unconditionally).** In the setting of Theorem D, if $y\in Y(\bar{\mathbb Q})$ has a $\bar{\mathbb Q}$-rational period point, then $y$ is CM.

*Proof.* By (D1), a point $b\in c^{-1}(y)$ is a $\bar{\mathbb Q}$-point, so $x=\Phi(b)\in M(\bar{\mathbb Q})$ and $A_x$ is defined over $\bar{\mathbb Q}$. The map $h^\prime\mapsto\pi h^\prime$ extends to a $\mathbb Q$-isomorphism of compact duals $\check X^\prime\cong\check D_Y$, because both are $G^{\rm ad}_{\mathbb C}/P$ and $\pi^{-1}(P_\mu)=P_{\mu^\prime}$. Composed with the $\mathbb Q$-embedding $\check X^\prime\hookrightarrow$ (Lagrangian Grassmannian of $W_0$), it shows that the period matrix of $A_x$ is algebraic. By Shiga–Wolfart and Cohen, $A_x$ is CM, and then $y$ is CM by (D3). $\square$

**4.5 Status, and the one missing statement.**

| | general geometric VHS | on $Y$ as in Theorem D | abelian varieties |
|---|---|---|---|
| (CM1) | open; follows from absoluteness (4.2) | **proved** (D2) | known |
| (CM2) | open; follows from absoluteness (4.2) | **proved** for $\sigma\in\mathrm{Aut}(\mathbb C/K)$ (D3) | known |
| (CM3), Hodge/lattice part | open | **proved** for $\sigma\in\mathrm{Aut}(\mathbb C/KE_x)$ (D3) | known |
| (CM3), $\ell$-adic part | open | open (G5) | known |
| (CM4) | follows from GPC (4.3) | **proved** (4.4) | known (Wüstholz) |

Outside such $Y$, the theory needs the following statement.

> **(MISSING)** For every CM point $s$ (with $\{s\}$ special) of a geometric VHS over $\bar{\mathbb Q}$, the Hodge-theoretic embedding $V_s\hookrightarrow T(H^1(A_s))(n)$ into a tensor construction on a CM abelian variety is weakly absolute.

Such an embedding exists as a morphism of Hodge structures, because CM Hodge structures are of abelian type. (MISSING) implies (CM1)–(CM3) by Proposition 4.2 and the theory of CM motives, and HC implies (MISSING). It is a statement about a single Hodge class on $X_s\times A_s$. When $s$ lies on no positive-dimensional special subvariety of abelian type, there is no family in which the class deforms, so Principle B and KOU, the only propagation tools available, have nothing to act on. This is Gap G3.

## 5. GAPS

* **G1 (top target (a)).** Needed: $(\star)$ every class with property $\mathcal G$ (equivalently, every absolute Hodge class) is algebraic, together with Deligne's conjecture that Hodge classes are absolute Hodge. Not proved. By Proposition 1.3, $(\star)$ contains HC for all abelian varieties, including CM abelian varieties and Weil classes in dimension $\ge6$. What is missing is a cycle-producing mechanism, not Hodge-theoretic information.
* **G2 (target (b), isolated case).** Needed: HC for Hodge classes with isolated Hodge locus. By Remark 2.3 these classes sit exactly at zero-dimensional special subvarieties, which include the open CM abelian cases. Not proved.
* **G3 ((c)/(d) at general special points).** Needed: statement (MISSING) of §4.5. Theorem D covers CM points lying on positive-dimensional special subvarieties that satisfy (H1)–(H3). It says nothing about CM points not on such subvarieties. In level $\ge3$ these are expected to be the majority (Baldi–Klingler–Ullmo).
* **G4 (the hypotheses of Theorem D).**
  * Without (H2), the graph $\bar\Gamma$ lies in the "thickening along the constant factor", where it is a factor, so (I5) no longer applies. The constant factor is a point of a smaller Mumford–Tate domain, which is G3 again.
  * Without (H1), Lemma 3.3 fails.
  * Without (H3), for instance for exceptional groups, for mixed $D^{\mathbb H}$ type, or for non-Hermitian $D_Y$, there is no Shimura variety with an algebraic family from which to import CM theory.
* **G5 ($\ell$-adic reciprocity on $Y$).** (D3) controls $V_{\sigma(y)}$ as a rational Hodge structure and its lattice, but not the Galois representation on $H^k_{\rm et}(X_{\bar y},\mathbb Q_\ell)$. That would need $\psi$ to be absolute Hodge at one point of $\tilde Y$; Principle B (I4) would then propagate it. Not available.
* **G6 (Pila–Zannier for general VHS).** Remark 3.7: (PZ3)–(PZ5) are not available outside abelian-type $Y$. In particular, polynomial height bounds for pre-special points in Siegel sets of non-Hermitian Mumford–Tate domains are not proved here.
* **G7 (verification).** The following were not checked against the primary sources in this session:
  * (I5), KOU: abstract and second-hand restatement only. Theorem D depends on its exact hypotheses.
  * (I7), canonical models, including the sign convention in the reciprocity law and the $\bar{\mathbb Q}$-definability of Shimura subvarieties: quoted from memory.
  * (I10), Pila–Shankar–Tsimerman: not re-checked; the search budget was exhausted.
  * The Shiga–Wolfart/Cohen criterion used in 4.4: from memory.
  * (I9), Markman: as listed in `docs/02`.

  The literature referee should check these first.
* **G8 (applicability).** I do not exhibit a family in which Theorem D gives an arithmetic statement not already obtainable from absoluteness. In the classical examples (K3, $H^2$ of hyper-Kähler varieties, $\mathcal A_g$, and, I believe, the known Calabi–Yau families with Shimura curves built from cyclic covers), absoluteness is available by construction. The value of Theorem D is that it needs no such construction. Whether level $\ge3$ families contain further special subvarieties satisfying (H1)–(H3) is not addressed.

## 6. Checklist (`docs/03` §3.4)

1. **Absoluteness.** Not delivered. Proposition 1.2 assumes it. Theorem D proves Galois stability of CM points on abelian-type $Y$ *without* it, but it proves no class absolute (G5).
2. **Lefschetz standard conjecture $B$.** Nothing.
3. **Variational Hodge conjecture.** Nothing.
4. **Open special cases.** None is settled. Corollary 2.2 adds instances of a classical type (very general very ample hypersurfaces in abelian fivefolds), resting on Markman's theorem.
5. **Where $\mathbb Q$-coefficients are essential.**
   * In Corollary 2.2, at the step $\alpha=i^*\beta$ with $\beta\in H^{2p}(Y,\mathbb Q)$: integrally, $i^*H^{2p}(Y,\mathbb Z)\oplus H_{{\rm van},\mathbb Z}$ has finite index in $H^{2p}(X,\mathbb Z)$, so $(i^*)^{-1}\alpha$ need not be integral. The inputs $\mathrm{HC}(Y)$ are themselves rational statements (Markman; Bloch–Srinivas, whose decomposition of the diagonal holds only up to a multiple).
   * In Theorem D, the Tannakian embedding $\iota$ exists over $\mathbb Q$; integrally, $V_{\mathbb Z}$ need not be a direct summand of $T(W_{0,\mathbb Z})$. Mumford–Tate groups and special subvarieties are defined through $\mathbb Q$-structures.
   * By Proposition 1.3(iii), the integral form of the converse in (a) is false, so any proof of G1 must use $\mathbb Q$-coefficients.
6. **Where projectivity is essential.**
   * Proposition 1.2 needs models over finitely generated fields with algebraic de Rham cohomology, and Principle B for smooth projective families.
   * Proposition 2.1 needs a very ample $\mathcal L$, Lefschetz pencils and the Lefschetz hyperplane theorem.
   * Theorem D needs a VHS of geometric origin over a number field (the hypothesis of KOU), a quasi-projective base, Borel's extension theorem, canonical models, and the projective abelian scheme over $M$.
7. **Would anything here "prove" a false variant?**
   * *Integral HC:* no. No result asserts integral algebraicity. The only cycle-producing statement (Corollary 2.2) passes through $\mathbb Q$-coefficients at the step above, and Proposition 1.3(iii) records that the natural integral analogue is false. This is consistent with Kollár and with Engel–de Gaay Fortman–Schreieder.
   * *Kähler HC:* no. A compact Kähler, non-projective manifold has no model over a finitely generated field (so $\mathcal G$ is undefined), no very ample bundle (so Proposition 2.1 does not apply), and no $\bar{\mathbb Q}$-structure (so Theorem D does not apply). Voisin's tori lie outside the scope of every statement.

## 7. References

* Y. André, *Mumford–Tate groups of mixed Hodge structures and the theorem of the fixed part*, Compositio Math. 82 (1992), 1–24.
* Y. André, *Pour une théorie inconditionnelle des motifs*, Publ. Math. IHES 83 (1996), 5–49.
* B. Bakker, B. Klingler, J. Tsimerman, *Tame topology of arithmetic quotients and algebraicity of Hodge loci*, J. AMS 33 (2020), 917–939.
* B. Bakker, J. Tsimerman, *The Ax–Schanuel conjecture for variations of Hodge structures*, Invent. Math. 217 (2019), 77–94.
* G. Baldi, B. Klingler, E. Ullmo, *On the distribution of the Hodge locus*, Invent. Math. (2024), arXiv:2107.08838.
* S. Bloch, V. Srinivas, *Remarks on correspondences and algebraic cycles*, Amer. J. Math. 105 (1983), 1235–1253.
* A. Borel, *Some metric properties of arithmetic quotients of symmetric spaces and an extension theorem*, J. Differential Geom. 6 (1972), 543–560.
* E. Cattani, P. Deligne, A. Kaplan, *On the locus of Hodge classes*, J. AMS 8 (1995), 483–506.
* P. Cohen, *Humbert surfaces and transcendence properties of automorphic functions*, Rocky Mountain J. Math. 26 (1996); H. Shiga, J. Wolfart, *Criteria for complex multiplication and transcendence properties of automorphic functions*, J. reine angew. Math. 463 (1995), 1–25.
* P. Deligne, *Théorie de Hodge II*, Publ. Math. IHES 40 (1971); *La conjecture de Weil II*, Publ. Math. IHES 52 (1980), §4.4; *Travaux de Shimura*, Sém. Bourbaki 389 (1971); *Variétés de Shimura*, Proc. Symp. Pure Math. 33 (1979), part 2, 247–290.
* P. Deligne (notes by J. Milne), *Hodge cycles on abelian varieties*; P. Deligne, J. Milne, *Tannakian categories*; both in LNM 900 (1982).
* P. Engel, O. de Gaay Fortman, S. Schreieder, *Matroids and the integral Hodge conjecture for abelian varieties*, arXiv:2507.15704.
* B. Klingler, A. Otwinowska, D. Urbanik, *On the fields of definition of Hodge loci*, Ann. Sci. ENS 56 (2023), 1299–1312, arXiv:2010.03359.
* J. Kollár, *Shafarevich maps and automorphic forms*, Princeton 1995, §2.10.
* T. Kreutz, *Absolutely special subvarieties and absolute Hodge cycles*, arXiv:2111.00216.
* E. Markman, *Secant sheaves and Weil classes on abelian varieties*, ICM 2026, arXiv:2509.23403.
* J. Milne, *Introduction to Shimura varieties*, Clay Math. Proc. 4 (2005).
* J. Pila, A. Shankar, J. Tsimerman, *Canonical heights on Shimura varieties and the André–Oort conjecture* (with an appendix by H. Esnault and M. Groechenig), arXiv:2109.08788; J. Tsimerman, *The André–Oort conjecture for $\mathcal A_g$*, Ann. of Math. 187 (2018), 379–390.
* I. Pjateckii-Shapiro, I. Shafarevich, *The arithmetic of K3 surfaces*, Trudy Mat. Inst. Steklov 132 (1973); J. Rizov, *Complex multiplication for K3 surfaces*, arXiv:math/0508018.
* M. Saito, C. Schnell, *Fields of definition of Hodge loci*, in *Recent advances in Hodge theory*, LMS Lecture Notes 427 (2016), arXiv:1408.2488.
* SGA 1 (Exp. XIII); SGA 7 II (Exp. XVIII).
* C. Voisin, *Hodge loci and absolute Hodge classes*, Compositio Math. 143 (2007), 945–958; *Hodge theory and complex algebraic geometry II*, Cambridge 2003.
* Yu. Zarhin, *Hodge groups of K3 surfaces*, J. reine angew. Math. 341 (1983), 193–220.

## 8. Claimed results

| Label | One-line statement | Status |
|---|---|---|
| Definition 1.1 | Property $\mathcal G$: absoluteness, Galois-coherence and $\bar k$-definability of the Hodge locus, in every model | definition |
| Proposition 1.2 | absolute Hodge (in particular algebraic) $\Rightarrow\mathcal G$ | known (Deligne Principle B; Voisin 2007); proof included |
| Proposition 1.3 | all Hodge classes on abelian varieties have $\mathcal G$; so "$\mathcal G\Rightarrow$ algebraic" contains HC for abelian varieties; the integral analogue is false | proved here, from Deligne (I8) and Engel–de Gaay Fortman–Schreieder |
| Proposition 2.1 | very general very ample hypersurface sections of $Y^{2p+1}$ with $H_{\rm van}$ not of pure type $(p,p)$ have $\mathrm{Hdg}^p=i^*\mathrm{Hdg}^p(Y)$ | known method (Lefschetz, Deligne); proof included |
| Corollary 2.2 | HC for very general very ample hypersurfaces in abelian fivefolds, and in fivefolds with $CH_0$ supported in dimension $\le3$ | proved here, conditional on Markman (I9) and Bloch–Srinivas; immediate, believed unrecorded |
| Remark 2.3 | an isolated Hodge locus forces $\{s\}$ to be special | proved here (elementary) |
| Lemma 3.1 | under (H3), the period map of $Y$ lifts (after a finite cover) to a Hodge-type Shimura variety $M$, with a flat Hodge embedding $\psi$ | proved here from standard inputs (Tannaka, Borel, I2, I6, I7) |
| Lemma 3.2 | the graph $\bar\Gamma\subset S\times M$ is closed, finite over $Y$, and special for $\mathbb U$ | proved here |
| Lemma 3.3 | under (H1), (H2): $H_{\bar\Gamma}$ is the graph of $G^{\prime\,\rm der}$, and $\bar\Gamma$ is weakly non-factor | proved here |
| Theorem D | under (H1)–(H3): zero-dimensional special subvarieties on $Y$ are $\bar{\mathbb Q}$-points; Galois conjugates of CM points of $Y$ are CM; Shimura–Taniyama reciprocity for the rational Hodge structures | proved here, conditional on KOU (I5) and canonical models (I7) as cited; believed new |
| Corollary 3.4 | case $Y=S$; recovers CM theory for K3 moduli (consistency check) | proved here (conditional as Theorem D); conclusion known for K3 |
| Corollary 3.5 | Galois orbits of CM points of $Y$ are at least those on $M$, divided by $N$ | proved here |
| Corollary 3.6 | CM points are dense in $Y$ iff $\Phi\colon\tilde Y\to M$ is dominant | proved here; $\Rightarrow$ conditional on André–Oort for Shimura varieties (I10) |
| Remark 3.7 | which Pila–Zannier inputs Theorem D supplies, and which are missing | discussion |
| Conjecture 4.0 | (CM1)–(CM4): what a CM theory for a general geometric VHS must contain | conjecture (formulation) |
| Lemma 4.1 | the Hodge filtration at a CM point is $\bar{\mathbb Q}$-rational | known (trivial) |
| Proposition 4.2 | absoluteness at $s$ $\Rightarrow$ (CM1), (CM2) | known (Voisin's argument); proof included |
| Proposition 4.3 | Grothendieck period conjecture $\Rightarrow$ (CM4) | folklore; proved here conditional on GPC |
| Corollary 4.4 | (CM4) holds on $Y$ as in Theorem D, unconditionally | proved here, conditional on Theorem D's inputs and on Shiga–Wolfart/Cohen |
