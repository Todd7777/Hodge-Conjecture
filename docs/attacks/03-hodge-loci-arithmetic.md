# Attack 3: Hodge loci, absolute Hodge classes and special points

**Status (read this first).** The top target of the ladder is (a): *HC for varieties over $\overline{\mathbb Q}$ implies HC for all complex varieties*. It is **not proved**. I prove that (a) is *equivalent* to a statement about how many Hodge classes conjugate varieties have, and I prove two precise negative statements about targets (b) and (c). Every labelled result below is proved from the inputs listed in §1. The one exception is Lemma 1.1, which is standard and for which I give only a sketch. The main results are:

* **Theorem A** (§2). $\mathrm{HC}^k(\overline{\mathbb Q})\wedge\mathrm{FD}^k_0\Rightarrow\mathrm{HC}^k$. Here $\mathrm{FD}^k_0$ says that every isolated point of a degree-$2k$ Hodge locus of a family defined over $\overline{\mathbb Q}$ is a $\overline{\mathbb Q}$-point. The same holds for Deligne's absolute Hodge conjecture AH, and there is a version for AH that keeps the dimension fixed. This is known in substance: Voisin 2007, together with the geometric analogue of the reduction to special points in Klingler–Otwinowska–Urbanik 2023, Cor. 1.14. KOU state that corollary for VHS whose de Rham data are defined over a number field, a class in which special points need not be algebraic (Theorem 4.2). The proofs here are self-contained. They also show that only the field-of-definition half of the special-point conjecture is used, not the half saying "Galois conjugates are special".
* **Theorem B** (§3). $\mathrm{FD}^k_0\iff\mathrm{CI}^k$, where $\mathrm{CI}^k$ says: *for every smooth projective complex $X$ and every $\sigma\in\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})$, $\dim_{\mathbb Q}\mathrm{Hdg}^k(X)=\dim_{\mathbb Q}\mathrm{Hdg}^k(X^\sigma)$.* Combined with Theorem A this gives $\mathrm{HC}^k\iff\mathrm{HC}^k(\overline{\mathbb Q})\wedge\mathrm{CI}^k$ (Cor. 3.2). So target (a) is *exactly* the implication $\mathrm{HC}^k(\overline{\mathbb Q})\Rightarrow\mathrm{CI}^k$ (Gap G1). Prop. 3.1 gives a form for a single variety: under $\mathrm{HC}^k(\overline{\mathbb Q})$, $\dim A^k(X)=\min_\sigma\dim\mathrm{Hdg}^k(X^\sigma)$, and HC holds for $X$ iff $X$ attains this minimum; every $X$ has conjugates that attain it. This is an elementary reformulation that I have not found in the literature (see G5). Voisin 2007, Lemma 1.4 (quoted in [KOU, Rem. 1.3]) proves a related equivalence for components of the locus of Hodge classes in the total space.
* **Proposition 4.1.** Zero-dimensional *atypical* special subvarieties need not be CM. The example is an explicit family over $\mathbb Q$. This corrects `docs/03` §3.2 (C3), and shows that the first half of ladder item (c) is false as stated.
* **Theorem 4.2 and Remark 4.3 (heuristic).** The field of definition of special points is not determined by the $\mathbb Z$-local system together with the algebraic de Rham data over $\overline{\mathbb Q}$. Concretely, there is a family over a transcendental field such that:
  * its de Rham realization has a $\mathbb Q$-model;
  * its local system is that of a family over $\mathbb Q$;
  * it nevertheless has an isolated Hodge point that is not algebraic.

  Heuristically, therefore, $\mathrm{FD}_0$ cannot be proved from those data plus theorems valid for all polarized $\mathbb Z$-VHS (o-minimal definability, Ax–Schanuel, the typical/atypical theory, the fixed part theorem, Principle B). Ladder item (b) needs a genuinely arithmetic input about varieties over number fields.
* Nothing is proved in the positive direction of (b) or (c) beyond what is already known (§4.4, §5).

**Referee (2026-11-13):** minor revision; corrections applied. Report summary: docs/06-attack-report.md.

*Access note.* arXiv, journal sites and the authors' home pages were blocked. I checked the statements of [KOU], [V07], [V25] and [BKU] only against abstracts and search excerpts. No proof below depends on them. Where a result is "known in substance", I say so.

## 1. Conventions, statements, inputs

**Conventions.**
* Varieties are reduced separated schemes of finite type over a subfield of $\mathbb C$, and $\overline{\mathbb Q}\subset\mathbb C$ is the algebraic closure of $\mathbb Q$.
* A **$\overline{\mathbb Q}$-family** is a smooth projective morphism $\pi\colon\mathcal X\to T$ of smooth quasi-projective $\overline{\mathbb Q}$-varieties. The same letters denote the base change to $\mathbb C$.
* $\mathbb V=R^{2k}\pi_*\mathbb Q$, and $\mathbb V_{\mathbb Z}$ is the image of $R^{2k}\pi_*\mathbb Z$.
* $\mathrm{Hdg}^k(Y)=H^{2k}(Y,\mathbb Q)\cap H^{k,k}(Y)$, and $A^k(Y)\subset\mathrm{Hdg}^k(Y)$ is the subspace of algebraic classes.
* For irreducible $T$, a point $t\in T(\mathbb C)$ is **$\overline{\mathbb Q}$-generic** if it lies on no proper closed $\overline{\mathbb Q}$-subvariety of $T$.
* The **$\overline{\mathbb Q}$-closure** of any $t$ is the smallest closed $\overline{\mathbb Q}$-subvariety containing $t$. It is irreducible, $t$ is $\overline{\mathbb Q}$-generic in it, and its dimension is $\mathrm{trdeg}_{\overline{\mathbb Q}}\overline{\mathbb Q}(t)$.

**Lemma 1.1 (standard).** Let $T$ be an irreducible $\overline{\mathbb Q}$-variety.
(i) For a closed subvariety $Z\subset T_{\mathbb C}$ the following are equivalent: $Z$ is defined over $\overline{\mathbb Q}$; $Z\cap T(\overline{\mathbb Q})$ is Zariski dense in $Z$; the orbit $\{\sigma(Z)\}_{\sigma\in\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})}$ is countable.
(ii) Any two $\overline{\mathbb Q}$-generic points of $T$ are conjugate under $\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})$.
(iii) Every non-empty Zariski open $U\subset T_{\mathbb C}$ meets $T(\overline{\mathbb Q})$. Also, $T(\mathbb C)$ is not a countable union of proper Zariski closed subsets.
(iv) (*Spreading out.*) For every smooth projective complex $X$ there are a $\overline{\mathbb Q}$-family $\mathcal X\to T$ with $T$ irreducible, and a $\overline{\mathbb Q}$-generic point $t_0$ with $X\cong X_{t_0}$. Then for every $\sigma\in\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})$ we have $X^\sigma\cong X_{\sigma(t_0)}$, and $\sigma(t_0)$ is again $\overline{\mathbb Q}$-generic. Such a pair $(\mathcal X/T,t_0)$ is called a **spread** of $X$.

*Proof.* (i) Work in an affine chart. For each $d$, the space $I(Z)_{\le d}$ of polynomials of degree $\le d$ vanishing on $Z$ is a point of a Grassmannian defined over $\mathbb Q$.
* If $Z(\overline{\mathbb Q})$ is dense, $I(Z)_{\le d}$ is cut out by $\overline{\mathbb Q}$-linear conditions on the coefficients, so it is spanned by $\overline{\mathbb Q}$-polynomials.
* If the orbit is countable, the normalized Plücker coordinates of every $I(Z)_{\le d}$ have countable orbits. They are therefore algebraic, because a transcendental number is $\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})$-conjugate to every transcendental number.
* Conversely, a $\overline{\mathbb Q}$-variety has dense $\overline{\mathbb Q}$-points (Nullstellensatz) and is $\sigma$-stable.

(ii) Every $\overline{\mathbb Q}$-generic point lies in any given affine open $\mathrm{Spec}A$, and corresponds to an injective $\overline{\mathbb Q}$-algebra map $A\to\mathbb C$. Two such maps differ by an isomorphism between countable subfields of $\mathbb C$ over $\overline{\mathbb Q}$. This isomorphism extends to an automorphism of $\mathbb C$: extend it to the algebraic closures, then match transcendence bases of $\mathbb C$ over the two fields, each of cardinality $2^{\aleph_0}$.

(iii) By (i), the Zariski closure of $T(\overline{\mathbb Q})$ is $T_{\mathbb C}$. The second claim is Baire's theorem, since proper closed subsets are nowhere dense in $T(\mathbb C)$.

(iv) The coefficients of equations of $X\subset\mathbb P^N$ generate a finitely generated $\overline{\mathbb Q}$-algebra $R\subset\mathbb C$. After inverting one element (by generic smoothness and openness of the smooth locus), $X$ is a fibre of a smooth projective $\mathcal X\to T=\mathrm{Spec}R$ with $T$ smooth. The fibre is over the point $t_0$ given by $R\subset\mathbb C$, and $t_0$ is $\overline{\mathbb Q}$-generic because $R\to\mathbb C$ is injective. Finally, $X^\sigma=\mathcal X\times_{T,\sigma\circ t_0}\mathbb C$. $\square$

**Hodge loci.** Fix a relatively ample class. Let $\tilde Q$ be the flat form on $\mathbb V$ obtained from cup product by the sign changes of the Lefschetz decomposition. By the Hodge–Riemann relations, $\tilde Q$ is positive definite on $H^{k,k}\cap H^{2k}(X_t,\mathbb R)$.

> **(I1) Cattani–Deligne–Kaplan** [CDK, Thm. 1.1]. For every $K>0$, the set $\mathcal H_K=\{(t,u):u\in\mathbb V_{\mathbb Z,t}\text{ Hodge},\ \tilde Q(u,u)\le K\}$ is a closed algebraic subvariety of the total space of the algebraic bundle $\mathbb V\otimes\mathcal O_T$, and it is finite over $T$.

**Definitions.** Let $p$ be the projection to $T$.
* An **HL-component** (of $\mathcal X/T$ in degree $2k$) is the image $p(\tilde V)\subset T_{\mathbb C}$ of an irreducible component $\tilde V$ of some $\mathcal H_K$. HL-components are closed, irreducible and algebraic, and there are countably many of them.
* An **isolated Hodge point** is a zero-dimensional HL-component $\{w\}$.
* For $u\in\mathrm{Hdg}^k(X_t)$, $\mathrm{HL}(u)_t$ denotes the germ at $t$ of the set of points where the parallel transport of $u$ is Hodge.
* $u$ is **generic** if $\mathrm{HL}(u)_t$ is the germ of $T$.

**Lemma 1.2.**
(i) Suppose $Nu\in\mathbb V_{\mathbb Z,t}$ and $\tilde Q(Nu,Nu)\le K$. Near $(t,Nu)$, $\mathcal H_K$ is the graph of the flat transport of $Nu$ over $\mathrm{HL}(u)_t$. Consequently:
  * $\mathrm{HL}(u)_t=\{t\}$ iff $(t,Nu)$ is an isolated point of $\mathcal H_K$, that is, iff $\{(t,Nu)\}$ is a component of $\mathcal H_K$. In particular, $\{w\}$ is an isolated Hodge point iff some $u\in\mathrm{Hdg}^k(X_w)$ has $\mathrm{HL}(u)_w=\{w\}$.
  * If $T$ is irreducible and $t$ lies on no proper HL-component, then every $u\in\mathrm{Hdg}^k(X_t)$ is generic.

  Note that the germ of $p(\tilde V)$ at $t$ can be larger than $\mathrm{HL}(u)_t$, because $\tilde V$ may also pass over $t$ through other classes.
(ii) The generic classes form a sub-local system $\mathbb A\subset\mathbb V$, and $\mathbb A_t\subset\mathrm{Hdg}^k(X_t)$ for all $t$.
(iii) For a smooth locally closed subvariety $W\subset T_{\mathbb C}$ (not necessarily defined over $\overline{\mathbb Q}$), the CDK locus of $\mathcal X_W/W$ is $\mathcal H_K\times_TW$, and $\mathrm{HL}(u)_t$ computed in $W$ is the intersection of the germ computed in $T$ with the germ of $W$.
(iv) If the transport of a class along every path is Hodge, the class has a finite monodromy orbit.

*Proof.* (i) $\mathbb V_{\mathbb Z}$ is discrete in the fibres. So near $(t,Nu)$, $\mathcal H_K$ is the graph of the flat transport of $Nu$ over the Hodge locus of $u$, and the first bullet follows. For the second, let $\tilde V$ be any component of $\mathcal H_K$ through $(t,Nu)$. Then $p(\tilde V)\ni t$, so $p(\tilde V)=T$ and $\dim\tilde V=\dim T$. An irreducible variety has pure-dimensional analytic germs, so every branch of $\tilde V$ at $(t,Nu)$ has dimension $\dim T$. Its image under the finite map $p$ is then a germ of dimension $\dim T$ in the smooth irreducible germ $T_t$, hence equal to $T_t$. By the graph description, $\mathrm{HL}(u)_t=T_t$.

(ii) Suppose $\mathrm{HL}(u)_t$ is the full germ, and follow a path $\gamma$. The set of points of $\gamma$ at which the transport is Hodge with full germ is open. It is also closed, because a closed analytic subset of a connected manifold with non-empty interior is everything. So genericity is preserved by transport. Sums of generic classes are generic.

(iii) Both the form and the Hodge classes restrict to $W$.

(iv) The orbit lies in $\frac1N\mathbb V_{\mathbb Z,t}\cap\{\tilde Q=\tilde Q(u,u)\}\cap H^{k,k}_{\mathbb R}$, which is a discrete subset of a compact set. $\square$

**The statements.** Fix $k$.
* $\mathrm{FD}^k$: for every $\overline{\mathbb Q}$-family, every HL-component in degree $2k$ is defined over $\overline{\mathbb Q}$.
* $\mathrm{FD}^k_0$: for every $\overline{\mathbb Q}$-family $\mathcal X\to W$, every isolated Hodge point in degree $2k$ lies in $W(\overline{\mathbb Q})$.
* $\mathrm{CI}^k$: $\dim\mathrm{Hdg}^k(X)=\dim\mathrm{Hdg}^k(X^\sigma)$ for every smooth projective complex $X$ and every $\sigma\in\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})$.
* $\mathrm{HC}^k(\overline{\mathbb Q})$ and $\mathrm{AH}^k(\overline{\mathbb Q})$: HC, resp. Deligne's absolute Hodge conjecture, for $\mathrm{Hdg}^k(Y_{\mathbb C})$ with $Y$ smooth projective over $\overline{\mathbb Q}$.
* A subscript $n$ ($\mathrm{HC}^k_n$, $\mathrm{AH}^k_n(\overline{\mathbb Q})$, …) restricts to varieties of dimension $n$.
* VHC is the variational Hodge conjecture of `docs/01`.

*Relation with special subvarieties (standard; sketch, not used in any proof below).* An HL-component is a special subvariety for $\mathbb V^\otimes$: it is the component, through a very general point, of the locus where all Hodge tensors at that point stay Hodge. Conversely, let $Z$ be a special subvariety for a VHS that is a summand of $R^m\pi_*\mathbb Q$. Then $Z$ is an HL-component, in some degree, of a fibre power $\mathcal X^r_T$. The reasons are that tensor Hodge classes are Hodge classes on fibre powers (by Künneth and Poincaré duality), and that a special subvariety is cut out by finitely many tensors. So $\bigwedge_k\mathrm{FD}^k_0$ for all $\overline{\mathbb Q}$-families is the field-of-definition part of the [KOU] conjecture for special points of VHS of geometric origin over $\overline{\mathbb Q}$. Here "special point" means zero-dimensional special subvariety [Kl, KOU].

**Further inputs.**
* (I2) Deligne's global invariant cycle theorem [D-H2, 4.1.1]. Let $\mathcal X'\to T'$ be smooth projective with $T'$ smooth and connected, and let $\bar{\mathcal X}'\supset\mathcal X'$ be a smooth compactification. Then $\mathrm{Im}(H^m(\bar{\mathcal X}',\mathbb Q)\to H^m(X'_t,\mathbb Q))=H^m(X'_t,\mathbb Q)^{\pi_1(T',t)}$, and the map is a morphism of Hodge structures. Polarizable $\mathbb Q$-Hodge structures form a semisimple category.
* (I3) Principle B [D82, Thm. 2.12]. Take a smooth projective family over a smooth connected complex base, and a global section of $R^{2k}\pi_*\mathbb Q$ that is Hodge at every point. If the section is absolute Hodge at one point, it is absolute Hodge at every point.
* (I4) Let $T$ be a $\overline{\mathbb Q}$-variety. Every finite étale cover of $T_{\mathbb C}$ is the base change of a finite étale cover of $T$. Lemma 2.3 uses this together with the Riemann existence theorem [SGA1, Exp. XII]: every finite topological cover of $T(\mathbb C)$ is a finite étale cover of $T_{\mathbb C}$. This is the invariance of the étale fundamental group under extension of algebraically closed fields of characteristic 0 [SGA1]; I did not check the exact numbering.
* (I5) For a regular embedding $i$ of smooth varieties, Gysin pull-back $CH^k\to CH^k$ is compatible with cycle classes. For $\mathcal Z$ flat over the base, the pull-back to a fibre is the fibre cycle [F, §10.1, Ch. 19].
* (I6) Let $\sigma\in\mathrm{Aut}(\mathbb C)$.
  * $Z\mapsto Z^\sigma$ gives $\dim A^k(X)=\dim A^k(X^\sigma)$, because the de Rham cycle class commutes with $\sigma$ and is injective on classes.
  * $\sigma$ induces a $\mathbb Q$-linear isomorphism between the spaces of absolute Hodge classes of $X$ and of $X^\sigma$ [D82, §2], [CS].

## 2. Target (a): the reduction, and where it stops

**2.0 The attempt.** Let $\beta\in\mathrm{Hdg}^k(X)$, and let $(\mathcal X/T,t_0)$ be a spread of $X$.
* If $\beta$ is generic, Lemma 2.3 writes it as the restriction of a Hodge class on a smooth projective $\overline{\mathbb Q}$-variety, and $\mathrm{HC}^k(\overline{\mathbb Q})$ makes it algebraic.
* If $\beta$ is not generic, then by Lemma 1.2(i) $t_0$ lies on some proper HL-component $V$. Since $t_0$ is $\overline{\mathbb Q}$-generic, $V$ is *not* defined over $\overline{\mathbb Q}$, and its $\overline{\mathbb Q}$-closure is all of $T$.

To finish, one must exclude such $V$, and $\mathrm{HC}(\overline{\mathbb Q})$ gives no handle on them. Lemma 2.4 shows why: $\mathrm{HC}(\overline{\mathbb Q})$, transported to $X$ by any correspondence that is defined over $\overline{\mathbb Q}$ or generic in the spread, only ever reaches generic classes. This is where the attempt stops (Gap G1). Theorem B identifies the missing statement as $\mathrm{CI}^k$.

**Lemma 2.1 (cutting; known in substance [KOU]).** $\mathrm{FD}^k_0\Rightarrow\mathrm{FD}^k$.

*Proof.* Set-up:
* $\mathcal X\to T$ is a $\overline{\mathbb Q}$-family with $T$ irreducible.
* $V=p(\tilde V)$ is an HL-component of dimension $d\ge1$, where $\tilde V$ is a component of $\mathcal H_K$; let $\tilde V_2,\dots,\tilde V_r$ be the other components of $\mathcal H_K$.
* $D=\bigcup_{j\ge2}p(\tilde V\cap\tilde V_j)$. Since $p$ is finite and $\tilde V\cap\tilde V_j\subsetneq\tilde V$, we have $\dim D<d$.
* Embed $T\subset\mathbb P^N$ over $\overline{\mathbb Q}$. Let $\bar V$ be the closure of $V$ and $G$ the Grassmannian of codimension-$d$ linear subspaces of $\mathbb P^N$.

*Choosing a good linear section.* There is a non-empty Zariski open $\mathcal U\subset G_{\mathbb C}$ such that every $L\in\mathcal U$ has the following properties:
* $L\cap\bar V$ is finite and non-empty (projective dimension theorem);
* $L\cap\bar V\subset V\setminus D$, because a general $L$ misses the closed set $(\bar V\setminus V)\cup\bar D$, which has dimension $<d$;
* $L\cap T$ is smooth, by generic smoothness applied to $\{(x,L):x\in L\}\subset T\times G\to G$.

By Lemma 1.1(iii) we may pick $L\in\mathcal U(\overline{\mathbb Q})$. Put $W=L\cap T$, a smooth quasi-projective $\overline{\mathbb Q}$-variety.

*Points of $V\cap L$ are algebraic.* Let $w\in L\cap V$ and $(w,u)\in\tilde V$. Since $w\notin D$, the point $(w,u)$ lies on no $\tilde V_j$ with $j\ge2$. So near $(w,u)$ the CDK locus of $\mathcal X_W/W$ (Lemma 1.2(iii)) is contained in $\tilde V\cap p^{-1}(L)$. This set is finite, because $p|_{\tilde V}$ is finite and $V\cap L$ is finite. Hence $\{(w,u)\}$ is a component of $\mathcal H_K\times_TW$, and $w$ is an isolated Hodge point of $\mathcal X_W/W$. By $\mathrm{FD}^k_0$, $w\in T(\overline{\mathbb Q})$. Thus $V\cap L\subset V(\overline{\mathbb Q})$ for all $L\in\mathcal U(\overline{\mathbb Q})$.

*Density.* Suppose the Zariski closure $Y$ of $V(\overline{\mathbb Q})$ were a proper subset of $V$. Then $\dim Y<d$, so a general $L$ misses $Y$. By Lemma 1.1(iii) some $L\in\mathcal U(\overline{\mathbb Q})$ misses $Y$, and then $\emptyset\ne L\cap V\subset Y\cap L=\emptyset$, a contradiction. So $V(\overline{\mathbb Q})$ is dense in $V$, and $V$ is defined over $\overline{\mathbb Q}$ by Lemma 1.1(i). $\square$

**Lemma 2.2.** Suppose $\mathrm{FD}^k$ holds for $\mathcal X/T$ with $T$ irreducible, and $t$ is $\overline{\mathbb Q}$-generic. Then $\mathrm{Hdg}^k(X_t)=\mathbb A_t$.

*Proof.* Every HL-component through $t$ is defined over $\overline{\mathbb Q}$ and contains a $\overline{\mathbb Q}$-generic point, so it equals $T$. Hence $t$ lies on no proper HL-component, and Lemma 1.2(i) applies. $\square$

**Lemma 2.3 (generic classes come from $\overline{\mathbb Q}$; [V07], via [D-H2]).** Let $\beta\in\mathbb A_{t_0}$. Then there are:
* a finite étale cover $T'\to T$ defined over $\overline{\mathbb Q}$;
* a smooth projective $\overline{\mathbb Q}$-variety $\bar{\mathcal X}'$ containing $\mathcal X'=\mathcal X\times_TT'$ as a dense open subset;
* a point $t_0'$ over $t_0$;
* a class $\tilde\beta\in\mathrm{Hdg}^k(\bar{\mathcal X}'_{\mathbb C})$ with $\tilde\beta|_{X_{t_0}}=\beta$.

Moreover, $\beta$ extends to a global section of $R^{2k}\pi'_*\mathbb Q$ that is Hodge at every point.

*Proof.*
1. By Lemma 1.2(iv), the stabilizer of $\beta$ in $\pi_1(T(\mathbb C),t_0)$ has finite index. The corresponding connected cover descends to some $T'$ over $\overline{\mathbb Q}$ (I4). On $T'$, $\beta$ is a global section, and it is Hodge everywhere by Lemma 1.2(ii).
2. Take the closure of $\mathcal X'$ in a projective space and resolve its singularities (Hironaka) without modifying the smooth locus. This gives $\bar{\mathcal X}'$.
3. By (I2), $\beta=\gamma|_{X_{t_0}}$ for some $\gamma\in H^{2k}(\bar{\mathcal X}',\mathbb Q)$. The restriction map onto its image is a morphism of polarizable Hodge structures, so it has a Hodge-structure splitting $s$, and $\tilde\beta=s(\beta)$ is a Hodge class. $\square$

**Lemma 2.4 (barrier).** Let $(\mathcal X/T,t_0)$ be a spread of $X$.
(i) $A^k(X)\subset\mathbb A_{t_0}$: algebraic classes are generic.
(ii) Let $Y$ be smooth projective over $\overline{\mathbb Q}$, $\eta\in\mathrm{Hdg}(Y_{\mathbb C})$, and $\Gamma\in\mathrm{Hdg}(Y_{\mathbb C}\times X)$ generic for the spread $Y\times\mathcal X\to T$. Then $\Gamma_*\eta\in\mathbb A_{t_0}$.

*Proof.* (i) Let $Z=\sum a_iZ_i$. Spreading out the coefficients of the $Z_i$ gives:
* a smooth irreducible $\overline{\mathbb Q}$-variety $T''$ with a dominant map $g\colon T''\to T$;
* a $\overline{\mathbb Q}$-generic point $t_0''$ over $t_0$;
* closed subschemes $\mathcal Z_i\subset\mathcal X''=\mathcal X\times_TT''$, flat over $T''$, with fibres $Z_i$ at $t_0''$.

By (I5), $s\mapsto\sum a_i[\mathcal Z_{i,s}]=i_s^*\sum a_i[\mathcal Z_i]$ is the restriction of a global class. So it is a flat section of $g^*\mathbb V$, Hodge everywhere. Since $t_0''$ is $\overline{\mathbb Q}$-generic, $g$ is smooth at $t_0''$ (generic smoothness). Hence $g$ maps a neighbourhood of $t_0''$ onto a neighbourhood of $t_0$, and on that neighbourhood the transport of $[Z]$ is Hodge. So $[Z]$ is generic.

(ii) $\Gamma$ and $p_1^*\eta$ extend flatly over $T$ and stay Hodge, hence so does $p_{2*}(\Gamma\cup p_1^*\eta)$. $\square$

So non-generic Hodge classes at $\overline{\mathbb Q}$-generic points are never algebraic, and correspondences over $\overline{\mathbb Q}$ only produce generic classes. Under $\mathrm{HC}(\overline{\mathbb Q})$, the possible counterexamples to HC are *exactly* the non-generic classes (Prop. 3.1).

**Theorem A (reduction).** For every $k$ and $n$:
1. $\mathrm{HC}^k(\overline{\mathbb Q})\wedge\mathrm{FD}^k_0\Rightarrow\mathrm{HC}^k$.
2. $\mathrm{AH}^k(\overline{\mathbb Q})\wedge\mathrm{FD}^k_0\Rightarrow\mathrm{AH}^k$.
3. $\mathrm{AH}^k_n(\overline{\mathbb Q})\wedge\mathrm{FD}^k_0\Rightarrow\mathrm{AH}^k_n$. In particular $\mathrm{HC}^k_n(\overline{\mathbb Q})\wedge\mathrm{FD}^k_0\Rightarrow\mathrm{AH}^k_n$; this version keeps the dimension fixed.
4. $\mathrm{HC}^k_n(\overline{\mathbb Q})\wedge\mathrm{FD}^k_0\wedge\mathrm{VHC}\Rightarrow\mathrm{HC}^k_n$.

*Proof.* Let $X$ be complex, $\beta\in\mathrm{Hdg}^k(X)$, and $(\mathcal X/T,t_0)$ a spread. By Lemmas 2.1 and 2.2, $\beta\in\mathbb A_{t_0}$. Let $T'$, $\bar{\mathcal X}'$ and $\tilde\beta$ be as in Lemma 2.3, and let $i\colon X\hookrightarrow\bar{\mathcal X}'_{\mathbb C}$ be the inclusion of the fibre. It is a regular embedding, and $X$ is closed in $\bar{\mathcal X}'_{\mathbb C}$ because it is proper.
1. By $\mathrm{HC}^k(\overline{\mathbb Q})$, $\tilde\beta=\mathrm{cl}(\tilde Z)$ for a cycle $\tilde Z$. By (I5), $\beta=i^*\tilde\beta=\mathrm{cl}(i^*\tilde Z)$.
2. $\tilde\beta$ is absolute, and pull-back by a morphism preserves absoluteness [D82, §2].
3. Pick $t_1\in T'(\overline{\mathbb Q})$. The global section $\beta$ is Hodge on the $n$-fold $X'_{t_1}$, which is defined over $\overline{\mathbb Q}$; so it is absolute there. Principle B (I3) on $T'_{\mathbb C}$ then gives absoluteness at $t_0'$.
4. As in (3), $\beta_{t_1}$ is algebraic. VHC along $T'_{\mathbb C}$ then gives algebraicity at $t_0'$. $\square$

*Remarks.*
(a) Only the field of definition of isolated Hodge points is used. The "Galois conjugates are special" half of the [KOU] conjecture is not.
(b) Part (1) needs HC on $\bar{\mathcal X}'$, whose dimension is $\dim X+\dim T$, and $\dim T$ is at least the transcendence degree of a field of definition of $X$. Codimension is preserved, dimension is not. For codimension-2 cycles on fourfolds, (1) needs $\mathrm{HC}^2$ on $\overline{\mathbb Q}$-varieties of every dimension $\ge4$.
(c) The converses also hold (Cor. 3.2).

## 3. The arithmetic obstruction as a statement about one variety

For $X$ smooth projective over $\mathbb C$, put $m^k(X)=\min\{\dim\mathrm{Hdg}^k(X^\sigma):\sigma\in\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})\}$.

**Proposition 3.1.** Let $(\mathcal X/T,t_0)$ be a spread of $X$.
1. $m^k(X)=\mathrm{rk}\,\mathbb A$, and the minimum is attained. More precisely, if $\sigma(t_0)$ lies outside the countably many proper HL-components, then $\mathrm{Hdg}^k(X^\sigma)=\mathbb A_{\sigma(t_0)}$, and such $\sigma$ exist.
2. $\dim\mathrm{Hdg}^k(X^\sigma)=m^k(X)$ iff every Hodge class of $X^\sigma$ is generic in the spread. For such $X^\sigma$: $\mathrm{HC}^k(\overline{\mathbb Q})\Rightarrow\mathrm{HC}^k(X^\sigma)$, and $\mathrm{AH}^k_{\dim X}(\overline{\mathbb Q})\Rightarrow\mathrm{AH}^k(X^\sigma)$.
3. $\dim A^k(X)\le m^k(X)$, with equality if $\mathrm{HC}^k(\overline{\mathbb Q})$ holds. Hence, under $\mathrm{HC}^k(\overline{\mathbb Q})$: $\mathrm{HC}^k(X)\iff\dim\mathrm{Hdg}^k(X)=m^k(X)\iff$ every Hodge class on $X$ is generic.

*Proof.* (1) We have $X^\sigma=X_{\sigma(t_0)}$, and $\mathrm{Hdg}^k(X_t)\supset\mathbb A_t$ for all $t$, so $\dim\mathrm{Hdg}^k(X^\sigma)\ge\mathrm{rk}\,\mathbb A$. By Lemma 1.1(iii) there is a point $t'\in T(\mathbb C)$ lying on no proper HL-component and on no proper closed $\overline{\mathbb Q}$-subvariety. By the second bullet of Lemma 1.2(i), every Hodge class at $t'$ is generic, so $\mathrm{Hdg}^k(X_{t'})=\mathbb A_{t'}$. By Lemma 1.1(ii), $t'=\sigma(t_0)$ for some $\sigma$.

(2) The first claim follows from (1) and $\mathbb A_t\subset\mathrm{Hdg}^k(X_t)$. For the second, apply the proof of Theorem A(1) and (3) to the spread $(\mathcal X/T,\sigma(t_0))$ of $X^\sigma$.

(3) $A^k(X)\subset\mathbb A_{t_0}$ by Lemma 2.4(i). Under $\mathrm{HC}^k(\overline{\mathbb Q})$, also $\mathbb A_{t_0}\subset A^k(X)$, by Lemma 2.3 and (I5). $\square$

So, granting $\mathrm{HC}(\overline{\mathbb Q})$, HC holds for a variety iff conjugation by $\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})$ cannot decrease its number of Hodge classes. Every variety has conjugates for which HC (resp. AH) reduces to $\overline{\mathbb Q}$. Note that for $\sigma\in\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})$, $X$ and $X^\sigma$ are fibres of one smooth family, hence diffeomorphic. Under $\mathrm{FD}^k$, parallel transport along any path maps $\mathrm{Hdg}^k(X)$ onto $\mathrm{Hdg}^k(X^\sigma)$, by Lemma 2.2.

**Theorem B.** $\mathrm{FD}^k_0\iff\mathrm{CI}^k$.

*Proof.* ($\Leftarrow$) Suppose $\mathcal X\to W$ is a $\overline{\mathbb Q}$-family and $\{w\}$ is an isolated Hodge point for $\beta$ with $w\notin W(\overline{\mathbb Q})$.
1. Let $W_1$ be the $\overline{\mathbb Q}$-closure of $w$; then $\dim W_1\ge1$. Let $W_2$ be its smooth locus; it contains $w$, because $w$ is $\overline{\mathbb Q}$-generic in $W_1$. So $(\mathcal X_{W_2}/W_2,w)$ is a spread of $X_w$.
2. $\beta$ is not generic in this spread. Indeed, $\mathrm{HL}(\beta)_w$ computed in $W_2$ is contained in the germ computed in $W$, which is $\{w\}$, while $\dim_wW_2\ge1$.
3. By Prop. 3.1(2) (applied with $\sigma=\mathrm{id}$), $\dim\mathrm{Hdg}^k(X_w)\ne m^k(X_w)$, hence $\dim\mathrm{Hdg}^k(X_w)>m^k(X_w)$. By Prop. 3.1(1) the minimum is attained: $m^k(X_w)=\dim\mathrm{Hdg}^k(X_w^\sigma)$ for some $\sigma\in\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})$. This contradicts $\mathrm{CI}^k$.

($\Rightarrow$) Let $(\mathcal X/T,t_0)$ be a spread of $X$ and $\sigma\in\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})$. By Lemma 2.1, $\mathrm{FD}^k$ holds. Both $t_0$ and $\sigma(t_0)$ are $\overline{\mathbb Q}$-generic, so by Lemma 2.2, $\dim\mathrm{Hdg}^k(X)=\mathrm{rk}\,\mathbb A=\dim\mathrm{Hdg}^k(X^\sigma)$. $\square$

**Corollary 3.2 (equivalences).** For every $k$:
* $\mathrm{FD}^k_0\iff\mathrm{FD}^k\iff\mathrm{CI}^k$;
* $\mathrm{HC}^k\iff\mathrm{HC}^k(\overline{\mathbb Q})\wedge\mathrm{CI}^k$;
* $\mathrm{AH}^k\iff\mathrm{AH}^k(\overline{\mathbb Q})\wedge\mathrm{CI}^k$.

In particular, target (a) in degree $2k$ is equivalent to the implication $\mathrm{HC}^k(\overline{\mathbb Q})\Rightarrow\mathrm{CI}^k$.

*Proof.*
* $\mathrm{FD}^k\Rightarrow\mathrm{FD}^k_0$ is trivial, the converse is Lemma 2.1, and $\mathrm{FD}^k_0\iff\mathrm{CI}^k$ is Theorem B.
* $\mathrm{HC}^k\Rightarrow\mathrm{CI}^k$ and $\mathrm{AH}^k\Rightarrow\mathrm{CI}^k$ follow from (I6), since all Hodge classes on $X$ and on $X^\sigma$ are then algebraic, resp. absolute.
* The reverse implications are Theorem A(1) and (2), combined with Theorem B. $\square$

**Proposition 3.3 (reduction to one parameter).** $\mathrm{FD}^k_0$ holds iff the following holds: for every algebraically closed subfield $K\subset\mathbb C$ of finite transcendence degree, and every smooth projective family over a smooth irreducible curve $C$ over $K$, all isolated Hodge points in degree $2k$ lie in $C(K)$. Here isolated Hodge points of a family over $K$ are defined exactly as in §1, using (I1) over $\mathbb C$.

*Proof.* ($\Leftarrow$) Work in the situation of the proof of Theorem B, and let $m=\dim W_2$.
1. Choose coordinates $x_1,\dots,x_m$ of an affine chart of $W_2$ such that the values $x_i(w)$ are algebraically independent over $\overline{\mathbb Q}$.
2. Let $K$ be the algebraic closure of $\overline{\mathbb Q}(x_2(w),\dots,x_m(w))$. Then $\mathrm{trdeg}_KK(w)=1$.
3. Let $C$ be the smooth locus of the $K$-Zariski closure of $w$ in $W_{2,K}$. It is a curve containing $w$.
4. The Hodge-locus germ of $\beta$ in $C$ is contained in $\{w\}$, so $w$ is an isolated Hodge point of $\mathcal X_C/C$. And $w\notin C(K)$, since $\mathrm{trdeg}_KK(w)=1$.

($\Rightarrow$) Let $c\in C$ be an isolated Hodge point for $\beta$, and suppose $c\notin C(K)$.
1. Then $c$ is $K$-generic in $C$, because the proper closed $K$-subsets of $C$ are finite sets of $K$-points.
2. Choose a finitely generated $\overline{\mathbb Q}$-algebra $R\subset K$ over which the family and $C$ are defined, and which contains a transcendence basis of $K/\overline{\mathbb Q}$. After shrinking, this gives a smooth irreducible $B=\mathrm{Spec}R$ and a $\overline{\mathbb Q}$-family $\mathcal X\to\mathcal C$, where $\mathcal C\to B$ is smooth of relative dimension 1 with irreducible total space, and $C=\mathcal C_{b_0}$ for the point $b_0$ given by $R\subset K$.
3. The point $b_0$ is $\overline{\mathbb Q}$-generic in $B$, and $K$ is algebraic over $\overline{\mathbb Q}(b_0)$. Hence $\mathrm{trdeg}_{\overline{\mathbb Q}}\overline{\mathbb Q}(c)=\dim B+\mathrm{trdeg}_KK(c)=\dim\mathcal C$, so $c$ is $\overline{\mathbb Q}$-generic in $\mathcal C$.
4. By Lemmas 2.1 and 2.2, $\beta$ is generic in $\mathcal C$. By Lemma 1.2(iii), $\mathrm{HL}(\beta)_c$ computed in $C$ is then the germ of the curve $C$, contradicting $\mathrm{HL}(\beta)_c=\{c\}$ (Lemma 1.2(i)). $\square$

**Remark 3.4.**
(a) Theorem B, Prop. 3.1 and Prop. 3.3 hold, with the same proofs, when $\overline{\mathbb Q}$ is replaced by any countable algebraically closed $K\subset\mathbb C$.
(b) *One variety suffices.* Suppose $\mathrm{HC}^k$ or $\mathrm{AH}^k$ holds for a single variety $X_w$. Then no isolated Hodge point $w$ of any $\overline{\mathbb Q}$-family with fibre $X_w$ can be transcendental. Indeed, the proof of Theorem B ($\Leftarrow$) would produce a $\sigma$ with
$$\dim\mathrm{Hdg}^k(X_w^\sigma)<\dim\mathrm{Hdg}^k(X_w)=\dim A^k(X_w)=\dim A^k(X_w^\sigma)\le\dim\mathrm{Hdg}^k(X_w^\sigma)$$
(resp. the same chain with absolute classes), which is absurd. This recovers $\mathrm{FD}_0$ for families of abelian varieties [D82], and for families whose fibres have abelian motives in André's sense [A96] (for example products of abelian varieties, K3 surfaces and Fermat hypersurfaces).

## 4. Targets (b) and (c): what special points are, and what a proof must use

**4.1 Special points need not be CM.** `docs/03` §3.2 (C3) says that at a zero-dimensional atypical component "the Hodge structure is of CM type". This is false, as the following example shows.

*Set-up.*
* $S=\mathbb P^1\setminus\{0,1,\infty\}$, and $\mathcal E\to S$ is the Legendre family $E_\lambda: y^2=x(x-1)(x-\lambda)$, with $j(\lambda)=256(\lambda^2-\lambda+1)^3/(\lambda^2(\lambda-1)^2)$.
* $C^\circ=\{\lambda: \lambda,\ 2\lambda-3,\ 3\lambda-6\in S\}=\mathbb P^1\setminus\{\infty,0,1,\tfrac32,2,\tfrac73\}$.
* $\mathcal Y\to C^\circ$ is the abelian scheme over $\mathbb Q$ with fibre $Y_\lambda=E_\lambda\times E_{2\lambda-3}\times E_{3\lambda-6}$.

**Proposition 4.1.**
(i) $\{3\}$ is an isolated Hodge point of $\mathcal Y/C^\circ$ in degree 2.
(ii) The Mumford–Tate group of $H^1(Y_3)$ is $\mathrm{GL}_{2,\mathbb Q}$, not a torus.
(iii) $\{3\}$ is atypical in the sense of [BKU]: $\mathrm{codim}_{\Phi(C^\circ)}\Phi(\{3\})=1<2=\mathrm{codim}_{D_G}D_M$. Here $\Phi$ is the period map, and $D_G$, $D_M$ are the Mumford–Tate domains of the generic and of the special Mumford–Tate group.

*Proof.* (i) At $\lambda=3$ all three factors equal $E_3$. Let $u\in\mathrm{Hdg}^1(Y_3)$ be the Künneth component, in $H^1\otimes H^1$ of the first two factors, of the class of $\Delta_{E_3}\times E_3$.
* Suppose the transport of $u$ is Hodge at $\lambda$. By Künneth and Poincaré duality, it is then a morphism of Hodge structures $H^1(E_{2\lambda-3})\to H^1(E_\lambda)$ that is an isomorphism of lattices. So $E_\lambda\cong E_{2\lambda-3}$ and $j(\lambda)=j(2\lambda-3)$.
* The orbit of $3$ under the deck group $S_3$ of $j$ is $\{3,-2,\tfrac13,-\tfrac12,\tfrac32,\tfrac23\}$, which has six elements, so $j$ is étale at $3$. Near $3$, $j(\lambda)=j(2\lambda-3)$ therefore forces $\lambda=2\lambda-3$, that is, $\lambda=3$.
* Hence $\mathrm{HL}(u)_3=\{3\}$, and $\{3\}$ is an isolated Hodge point by the first bullet of Lemma 1.2(i).

(ii) $j(3)=21952/9$ is not an algebraic integer, so $E_3$ has no CM [Si, Thm. II.6.1]. Hence $\mathrm{MT}(H^1(E_3)^{\oplus3})=\mathrm{MT}(H^1(E_3))=\mathrm{GL}_2$, embedded diagonally. In particular $D_M$ is the diagonal $\mathfrak H\subset\mathfrak H^3$.

(iii) *Very general fibres.* Consider the three pairs $(a,b)=(\lambda,2\lambda-3)$, $(\lambda,3\lambda-6)$, $(2\lambda-3,3\lambda-6)$.
* The closure in $\mathbb P^1\times\mathbb P^1$ of each curve $\{(a(\lambda),b(\lambda))\}$ passes through a point of the form (cusp, non-cusp): $(0,-3)$, $(0,-6)$ and $(0,-\tfrac32)$, at $\lambda=0$, $0$ and $\tfrac32$ respectively.
* The closures of the isogeny curves $\{\Phi_N(j(a),j(b))=0\}$ contain no such point: $\Phi_N$ is monic in each variable, so $j(a)\to\infty$ forces $j(b)\to\infty$. So none of the three curves lies in an isogeny curve, and each meets every isogeny curve in finitely many points.
* Hence, for $\lambda$ outside a countable set, the elliptic curves $E_\lambda$, $E_{2\lambda-3}$, $E_{3\lambda-6}$ are pairwise non-isogenous and have no CM (CM $j$-invariants form a countable set).

*Generic group.* Let $H\subset\mathrm{SL}_2^3$ be the Hodge group of such a fibre.
* $H$ projects onto each factor.
* By Goursat's lemma for the simple Lie algebra $\mathfrak{sl}_2$, $\mathrm{Lie}\,H$ is a product of diagonals over a partition of the three factors.
* A non-trivial block would give an $H$-equivariant, hence Hodge, isomorphism $H^1(E_a)\to H^1(E_b)$, because automorphisms of $\mathrm{SL}_2$ over $\mathbb Q$ are inner by $\mathrm{GL}_2(\mathbb Q)$. That is an isogeny, which is excluded.
* So $H=\mathrm{SL}_2^3$ and $D_G=\mathfrak H^3$.

*Conclusion.* $\mathrm{codim}_{D_G}D_M=2$, while $\Phi(C^\circ)$ is a curve, so $\mathrm{codim}_{\Phi(C^\circ)}\Phi(\{3\})=1$. $\square$

So the objects in ladder item (c) must be isolated Hodge points of arbitrary Mumford–Tate type. By Theorem B and Lemma 2.1, the field-of-definition problem concerns all of them: typical or atypical, CM or not. In Prop. 4.1 the point is rational, as it must be, since the family is of abelian type.

**4.2 De Rham data over $\overline{\mathbb Q}$ do not determine special points.** Let $E_0$ be a complex elliptic curve with $j(E_0)\notin\overline{\mathbb Q}$, and put $E_1=E_3$ (defined over $\mathbb Q$). Let $A=\mathcal E\times E_0\to S_{\mathbb C}$ and $A'=\mathcal E\times E_1\to S$; their fibres are $E_\lambda\times E_0$ and $E_\lambda\times E_1$.

**Theorem 4.2.**
(i) *Same Betti and de Rham data.* $R^1A_*\mathbb Z\cong R^1A'_*\mathbb Z$ as polarized local systems. For every $m$, $(H^m_{dR}(A/S_{\mathbb C}),\nabla,F^\bullet)\cong(H^m_{dR}(A'/S),\nabla,F^\bullet)\otimes_{\mathbb Q}\mathbb C$ as filtered algebraic flat bundles, compatibly with cup products. In particular the de Rham realization of $A$ has a model over $\mathbb Q$.
(ii) Every isolated Hodge point of $A'/S$ (in degree 2) lies in $S(\overline{\mathbb Q})$.
(iii) $A/S_{\mathbb C}$ has an isolated Hodge point $\lambda_0$ (in degree 2) with $\lambda_0\notin\overline{\mathbb Q}$.
(iv) *Positive-dimensional version.* Let $\mathcal B=\mathcal E\times\mathcal E\times E_0\to S\times S$. The curve $\{\lambda_0\}\times S$ is an HL-component in degree 2, of positive period dimension, and not defined over $\overline{\mathbb Q}$. Again the de Rham realization has a $\mathbb Q$-model, namely that of $\mathcal E\times\mathcal E\times E_1$.

*Proof.* (i) The $H^1$ of a fibre is $H^1(E_\lambda)\oplus H^1(E_0)$, resp. $H^1(E_\lambda)\oplus H^1(E_1)$, and $H^m=\Lambda^mH^1$. This holds compatibly with Gauss–Manin connections and Hodge filtrations, in both Betti and de Rham cohomology.
* *Betti side.* Both local systems are $R^1\mathcal E_*\mathbb Z\oplus\mathbb Z^2$, with the standard form on $\mathbb Z^2$.
* *De Rham side.* Choose a $\mathbb C$-linear symplectic isomorphism $\phi\colon H^1_{dR}(E_0/\mathbb C)\to H^1_{dR}(E_1/\mathbb Q)\otimes\mathbb C$ with $\phi(F^1)=F^1$; this exists because both sides are symplectic planes with a distinguished line. Then $\mathrm{id}\oplus\phi$ is an isomorphism of filtered flat bundles on $H^1$, hence on every $\Lambda^m$.

(ii) A class with isolated Hodge locus is not generic. Its components in $H^2(E_\lambda)$ and $H^2(E_1)$ are multiples of fibre classes, which are generic. So its $H^1(E_\lambda)\otimes H^1(E_1)$-component is a non-zero Hodge class, which means $\mathrm{Hom}(E_\lambda,E_1)\neq0$. Then $\Phi_N(j(\lambda),j(E_1))=0$ for some $N$, so $j(\lambda)\in\overline{\mathbb Q}$, and hence $\lambda\in\overline{\mathbb Q}$.

(iii) The map $j\colon S\to\mathbb A^1$ is surjective, so there is $\lambda_0$ with $E_{\lambda_0}\cong E_0$. Let $u$ be the $H^1\otimes H^1$-component of the class of the graph of an isomorphism $E_{\lambda_0}\to E_0$.
* As in Prop. 4.1, wherever the transport of $u$ is Hodge we have $E_\lambda\cong E_0$, i.e. $j(\lambda)=j(E_0)$. This is a finite set, so $\lambda_0$ is an isolated Hodge point.
* Since $j(\lambda_0)=j(E_0)\notin\overline{\mathbb Q}$ and $j\in\mathbb Q(\lambda)$, we get $\lambda_0\notin\overline{\mathbb Q}$.

(iv) The same class, placed on the factor $E_\lambda\times E_0$, has Hodge-locus germ $\{\lambda_0\}\times(\text{nbhd of }\mu)$ at every point $(\lambda_0,\mu)$.
* By the graph description in Lemma 1.2(i), the germ of $\mathcal H_K$ there is one-dimensional. A component $\tilde V$ through it is therefore a curve, by pure-dimensionality of germs of irreducible varieties, and $p(\tilde V)\supset\{\lambda_0\}\times S$. So $p(\tilde V)=\{\lambda_0\}\times S$ is an HL-component.
* The component $\{\lambda_0\}\times S$ maps to $\{\lambda_0\}$ under the first projection, which is a $\overline{\mathbb Q}$-morphism. So it is not defined over $\overline{\mathbb Q}$.
* The factor $E_\mu$ varies along it, so its period dimension is $1$.
* The de Rham model is obtained with the same $\phi$ as in (i). $\square$

$A$ is defined over $K=\overline{\mathbb Q(j(E_0))}$, a field of transcendence degree one. Its isolated Hodge points lie in $S(K)$: the argument of (ii), with $E_1$ replaced by $E_0$, gives $\Phi_N(j(\lambda),j(E_0))=0$. This is what $\mathrm{FD}_0$ over $K$ predicts (Remark 3.4(a)). Theorem 4.2 contradicts no conjecture about families defined over $\overline{\mathbb Q}$. It does contradict the literal statement of [KOU, Conj. 1.5(a)] (arXiv v1). KOU's Definition 1.4 calls a $\mathbb Z$-VHS *defined over a number field $L$* when $S$, $\mathcal V$, $F^\bullet$ and $\nabla$ are defined over $L$, which is exactly membership in $\mathcal C_{dR}$. $R^1A_*\mathbb Z$ is such a VHS (over $\mathbb Q$), and it has the transcendental special point $\lambda_0$. That conjecture therefore needs an extra hypothesis, for example geometric origin over $L$ or no isotrivial factor. Only arXiv v1 of [KOU] was checked. Its content is the following. What decides the field of definition of special points is the field of definition of the *family*, through the comparison between its Betti and de Rham structures. Neither structure alone decides it.

**Remark 4.3 (heuristic no-go for de Rham-intrinsic arguments; not a theorem).** Let $\mathcal C_{dR}$ be the class of smooth projective families over $S_{\mathbb C}$, with $S$ smooth quasi-projective over $\overline{\mathbb Q}$, whose algebraic de Rham realizations (with $\nabla$, $F^\bullet$ and cup products) have $\overline{\mathbb Q}$-models.
* Both $\mathrm{FD}_0$ and the statement "positive-dimensional HL-components are defined over $\overline{\mathbb Q}$" fail in $\mathcal C_{dR}$.
* Hence no proof of $\mathrm{FD}_0$, or equivalently of CI, can use only the following:
  * the isomorphism class of the $\mathbb Z$-local system;
  * the isomorphism class of the $\overline{\mathbb Q}$-model of the de Rham data;
  * theorems valid for every smooth projective family over $\mathbb C$, or for every polarized $\mathbb Z$-VHS on a quasi-projective base. Examples are [CDK], [BKT] (definability of period maps, hence Pila–Wilkie counting on the associated definable sets), Ax–Schanuel [BT], [BKU], the theorem of the fixed part and Principle B.
* Such a proof must use a structure that $A$ lacks and $A'$ has. Examples are the Betti–de Rham comparison of a variety defined over $\overline{\mathbb Q}$ (its periods), or the $\ell$-adic or $p$-adic realizations of a model over a number field, with their Galois or Frobenius structure.

*Proof.*
* $A\in\mathcal C_{dR}$ violates $\mathrm{FD}_0$ by Theorem 4.2(iii), and the positive-dimensional statement by (iv).
* $A$ and $A'$ have the same local system and the same de Rham model, by (i).
* The quoted theorems hold for $A$. $A'$ satisfies $\mathrm{FD}_0$: in degree 2 by (ii), and in all degrees by Remark 3.4(b), since its fibres are abelian varieties.
* So an argument of the excluded kind would apply verbatim to $A$, and would prove a false statement. $\square$

*Remarks.*
(a) The fixed part of the component in Theorem 4.2(iv) contains the constant summand $H^1(E_{\lambda_0})\otimes H^1(E_0)$, which is not of type $(1,1)$. Voisin's criterion [V07, Thm. 0.6] (numbering as cited in [KOU, §1.2.2]; not checked against [V07]) requires that, on the component, there is no constant sub-VHS of $R^{2k}_{\rm prim}$ other than $\mathbb Q\alpha_t$. That criterion, and the (weakly) non-factor hypothesis of [KOU], are designed to exclude exactly this. Theorem 4.2(iv) shows that such a hypothesis cannot be dropped in $\mathcal C_{dR}$. Theorem 4.2(iii) shows that at points, where the fixed part is everything, no hypothesis of this de Rham-intrinsic kind can hold. [KOU] work in $\mathcal C_{dR}$ by definition: their Def. 1.4, with Thm. 1.12(a) assuming only that $S$ is defined over $L$. I have not verified that the proof in [V07] uses only membership in $\mathcal C_{dR}$.
(b) For ladder item (b), o-minimality plus functional transcendence cannot suffice; the "transcendence input" must be arithmetic. Candidates are Grothendieck's period conjecture in André's form, or an analytic-subgroup-type theorem for non-abelian periods. No such theorem is available beyond 1-motives and abelian varieties.

**4.4 What is known for (b) and (c).**
* For (b): $\mathrm{FD}_0$ at $w$ follows from AH for $X_w$ (Remark 3.4(b)). This covers families of abelian varieties [D82] and of varieties with abelian motives [A96]. For these families, AH together with [V07] also gives the statement that Galois conjugates of special points are special.
* For (c): a CM Hodge structure is, as a Hodge structure, a summand of a tensor construction on $H^1$ of CM abelian varieties. Let $X$ be a variety with $H^{2k}(X)$ of CM type. Absoluteness of its Hodge classes would follow from an *absolute* (for example motivated) isomorphism of this kind. That isomorphism is exactly what is missing outside the abelian-motive case.

I prove nothing new in the positive direction here.

## 5. GAPS

* **G1 (target (a), not proved).**
  * *Needed:* $\mathrm{HC}^k(\overline{\mathbb Q})\Rightarrow\mathrm{CI}^k$, or equivalently $\mathrm{HC}^k(\overline{\mathbb Q})\Rightarrow\mathrm{FD}^k_0$ (Cor. 3.2).
  * *Why it is needed:* by Prop. 3.1, the only possible counterexamples left open by $\mathrm{HC}(\overline{\mathbb Q})$ are non-generic classes at $\overline{\mathbb Q}$-generic points, that is, failures of CI.
  * *Why I cannot prove it:* $\mathrm{CI}^k$ is vacuous for varieties over $\overline{\mathbb Q}$, since they are fixed by $\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})$. Every mechanism I know for transporting information from $\overline{\mathbb Q}$-varieties to $X$ only reaches generic classes (Lemma 2.4). These mechanisms are restriction from total spaces of spreads, and correspondences that are defined over $\overline{\mathbb Q}$ or generic in the spread. A non-generic class could only be reached through a non-generic class on a variety not defined over $\overline{\mathbb Q}$, which is the original problem. By Remark 4.3, the missing input is arithmetic: it concerns periods, or Galois/Frobenius realizations, of varieties over number fields.
* **G2 (target (b), not reached).**
  * No new class of variations is proved to satisfy $\mathrm{FD}_0$ or the Galois statement. Everything known follows from AH for the fibres (Remark 3.4(b)).
  * The suggested route (o-minimality plus a transcendence input) is blocked unless the transcendence input is arithmetic (Remark 4.3).
  * The candidate inputs are open: the Grothendieck–André period conjecture, and analytic subgroup theorems beyond commutative groups.
* **G3 (target (c)).** The first half is false as stated (Prop. 4.1). The second half, absoluteness of CM Hodge classes of geometric origin outside the abelian-motive case, is not reached.
* **G4 (dimension).** Theorem A(1) uses $\mathrm{HC}^k$ on $\overline{\mathbb Q}$-varieties of dimension $\dim X+\dim T$, where $T$ is the base of a spread of $X$. A dimension-preserving reduction of HC is obtained only modulo VHC (Thm. A(4)). For AH, the dimension-preserving reduction holds assuming only $\mathrm{FD}_0$ (Thm. A(3)).
* **G5 (literature and novelty).**
  * I could not read [KOU], [V07] or [V25] in full.
  * Lemma 2.1 and Theorem A(1)–(2) are, I believe, contained in substance in [V07] together with [KOU], whose abstract says that special subvarieties are defined over $\overline{\mathbb Q}$ iff special points are.
  * A search excerpt of [V25] says that the field-of-definition question for isolated points of Hodge loci is "almost equivalent" to a question that the excerpt cuts off. Theorem B may be a precise form of that remark, so its novelty is uncertain.
  * I did not check the SGA 1 reference for (I4), or the exact form of the [BKU] definition of atypicality, against the sources.

## 6. Checklist (`docs/03` §3.4)

1. **Absoluteness.** Not proved. Theorem A(2), (3) and Cor. 3.2 isolate what is missing: $\mathrm{AH}\iff\mathrm{AH}(\overline{\mathbb Q})\wedge\mathrm{CI}$. $\mathrm{FD}_0$ ($\iff$ CI) follows from the $\mathrm{Aut}(\mathbb C/\overline{\mathbb Q})$-part of checklist item 1, and it is the only part of item 1 that the reduction (a) needs. The $\mathrm{Gal}(\overline{\mathbb Q}/\mathbb Q)$-part (conjugates of special points are special) is not needed for (a).
2. **Lefschetz B, VHC and the open cases.** Not touched. VHC appears only as a hypothesis, in Thm. A(4).
3. **Rational coefficients.** These are used essentially in Lemma 2.3: the global invariant cycle theorem and the splitting of the restriction map are statements about $\mathbb Q$-Hodge structures.
   * *Integral test.* Take Kollár's very general hypersurface $X\subset\mathbb P^4$ of degree $d$ with $p^3\mid d$.
   * The locus where the generator $\ell$ of $H^4(X,\mathbb Z)$ is algebraic is a countable union of images of components of relative Hilbert schemes, all defined over $\overline{\mathbb Q}$. These images are proper subsets by [Ko], so Kollár's conclusion holds at $\overline{\mathbb Q}$-generic fibres of the universal family.
   * At such a fibre, $H^4(X,\mathbb Z)=\mathbb Z\ell$ with $h^2=d\ell$, and $\ell$ is generic, so FD is not an issue.
   * The incidence variety $I\subset\mathbb P^4\times\mathbb P^M$ is a smooth projective compactification of the total space. By the projective bundle formula ($I$ is a $\mathbb P^{M-1}$-bundle over $\mathbb P^4$), $H^4(I,\mathbb Z)$ is spanned by $h^2$, $h\zeta$ and $\zeta^2$, where $\zeta$ is the hyperplane class of the linear system. Since $\zeta|_X=0$, the image of $H^4(I,\mathbb Z)\to H^4(X,\mathbb Z)$ is $\mathbb Zh^2=d\mathbb Z\ell$.
   * So Lemma 2.3 holds with $\mathbb Q$-coefficients ($\ell=\tfrac1dh^2|_X$) but fails with $\mathbb Z$-coefficients for this compactification.
   * More generally, for no spread and no smooth projective compactification $\bar{\mathcal X}'$ is $\ell$ the restriction of an integral *algebraic* class: if $\ell=i^*\mathrm{cl}(Z)$, then $\ell=\mathrm{cl}(i^*Z)$ by (I5), contradicting [Ko]. So an integral version of Theorem A(1) must break either at Lemma 2.3 or at integral HC on the total space. Those are exactly the steps where the argument uses $\mathbb Q$.
   * Theorem B and Prop. 3.1(1), (2) are statements about Hodge structures. They are insensitive to coefficients, since integral and rational Hodge classes have the same rank, and they say nothing about integral cycles.
   * So the argument does not prove the integral HC.
4. **Projectivity.** This is used in three places:
   * in (I1), where the polarization gives algebraicity and finiteness of Hodge loci;
   * in spreading out and in $\mathrm{Aut}(\mathbb C)$-conjugation, which need algebraic varieties and algebraic de Rham cohomology;
   * in Lemma 2.3, which needs a smooth *projective* compactification over $\overline{\mathbb Q}$ to which HC applies.

   *Kähler test.* A non-algebraic compact Kähler manifold, for example one of Voisin's 4-tori, has no spread over $\overline{\mathbb Q}$ and no conjugates. So CI, $\mathrm{FD}_0$ and Theorem A do not apply to it. The analogue for families of non-polarized tori fails at (I1). So the argument does not prove the Kähler HC.
5. **Self-test against false statements.** Theorem 4.2 is itself such a test. It exhibits a class of objects ($\mathcal C_{dR}$) that has all the de Rham and Betti structure of $\overline{\mathbb Q}$-families but for which $\mathrm{FD}_0$ is false. Any purported proof of $\mathrm{FD}_0$, of CI, or of target (a) that would apply verbatim to $\mathcal C_{dR}$ is wrong. This includes the present text, which proves none of them.

## 7. References

* [A96] Y. André, *Pour une théorie inconditionnelle des motifs*, Publ. Math. IHES 83 (1996), 5–49.
* [BKT] B. Bakker, B. Klingler, J. Tsimerman, *Tame topology of arithmetic quotients and algebraicity of Hodge loci*, J. AMS 33 (2020), 917–939.
* [BT] B. Bakker, J. Tsimerman, *The Ax–Schanuel conjecture for variations of Hodge structures*, Invent. Math. 217 (2019), 77–94.
* [BKU] G. Baldi, B. Klingler, E. Ullmo, *On the distribution of the Hodge locus*, Invent. Math. 235 (2024), 441–487; arXiv:2107.08838.
* [CDK] E. Cattani, P. Deligne, A. Kaplan, *On the locus of Hodge classes*, J. AMS 8 (1995), 483–506.
* [CS] F. Charles, C. Schnell, *Notes on absolute Hodge classes*, in *Hodge Theory*, Math. Notes 49, Princeton 2014; arXiv:1101.3647.
* [D-H2] P. Deligne, *Théorie de Hodge II*, Publ. Math. IHES 40 (1971), 5–57.
* [D82] P. Deligne (notes by J. S. Milne), *Hodge cycles on abelian varieties*, LNM 900 (1982), 9–100.
* [F] W. Fulton, *Intersection Theory*, 2nd ed., Springer 1998.
* [Kl] B. Klingler, *Hodge theory, between algebraicity and transcendence*, Proc. ICM 2022; arXiv:2112.13814.
* [KOU] B. Klingler, A. Otwinowska, D. Urbanik, *On the fields of definition of Hodge loci*, Ann. Sci. ENS 56 (2023), 1299–1312; arXiv:2010.03359.
* [Ko] J. Kollár, *Trento examples*, LNM 1515 (1992), 134–135.
* [Kr] T. Kreutz, *Absolutely special subvarieties and absolute Hodge cycles*, arXiv:2111.00216 (related: special subvarieties cut out by de Rham-absolute cycles).
* [SGA1] A. Grothendieck, *Revêtements étales et groupe fondamental*, LNM 224.
* [Si] J. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, GTM 151, Thm. II.6.1 (CM $j$-invariants are algebraic integers).
* [V07] C. Voisin, *Hodge loci and absolute Hodge classes*, Compositio Math. 143 (2007), 945–958. Its Prop. 0.2 reduces HC for (weakly) absolute classes to $\overline{\mathbb Q}$; its Thm. 0.6 (numbering as cited in [KOU]) is the constant-sub-VHS criterion.
* [V25] C. Voisin, article in "Vol. 1, Issue 1 (2025)" of a journal, file `JOMP_V01N01P02Paper.pdf` on her home page. Seen only through a search excerpt; I could not retrieve the title.

## 8. Claimed results

| label | statement | status |
|---|---|---|
| Lemma 1.1 | fields of definition via $\overline{\mathbb Q}$-points or countable orbits; conjugacy of $\overline{\mathbb Q}$-generic points; spreading out | known (standard), proof sketched |
| Lemma 1.2 | local graph description of $\mathcal H_K$; characterization of isolated Hodge points; points on no proper HL-component carry only generic classes; generic classes form a local system; restriction; finite monodromy orbits | known (from [CDK]), proved here |
| Lemma 2.1 | $\mathrm{FD}^k_0\Rightarrow\mathrm{FD}^k$ (generic $\overline{\mathbb Q}$-linear sections) | proved here; known in substance [KOU] |
| Lemma 2.2 | under $\mathrm{FD}^k$, every Hodge class at a $\overline{\mathbb Q}$-generic point is generic | proved here (elementary) |
| Lemma 2.3 | a generic class is the restriction of a Hodge class on a smooth projective $\overline{\mathbb Q}$-variety, and a global flat Hodge section on a finite étale cover | known ([V07] via [D-H2]), proved here |
| Lemma 2.4 | algebraic classes, and images under generic correspondences from $\overline{\mathbb Q}$-varieties, are generic | proved here (elementary) |
| Theorem A | $\mathrm{HC}^k(\overline{\mathbb Q})\wedge\mathrm{FD}^k_0\Rightarrow\mathrm{HC}^k$; the same for AH; $\mathrm{AH}^k_n(\overline{\mathbb Q})\wedge\mathrm{FD}^k_0\Rightarrow\mathrm{AH}^k_n$; with VHC, the same for $\mathrm{HC}^k_n$ | proved here; (1)–(2) known in substance ([V07] + [KOU]) |
| Prop. 3.1 | $\min_\sigma\dim\mathrm{Hdg}^k(X^\sigma)$ equals the rank of the generic classes and is attained; under $\mathrm{HC}^k(\overline{\mathbb Q})$, $\mathrm{HC}^k(X)$ holds iff $X$ attains the minimum | proved here; elementary reformulation, novelty unverified |
| Theorem B | $\mathrm{FD}^k_0\iff\mathrm{CI}^k$ | proved here; elementary reformulation, novelty unverified (G5) |
| Cor. 3.2 | $\mathrm{HC}^k\iff\mathrm{HC}^k(\overline{\mathbb Q})\wedge\mathrm{CI}^k$; $\mathrm{AH}^k\iff\mathrm{AH}^k(\overline{\mathbb Q})\wedge\mathrm{CI}^k$; $\mathrm{FD}_0\iff\mathrm{FD}\iff\mathrm{CI}$ | proved here |
| Prop. 3.3 | $\mathrm{FD}^k_0$ is equivalent to its version for one-parameter families over algebraically closed fields of finite transcendence degree | proved here |
| Remark 3.4 | the results hold over any countable algebraically closed base field; HC or AH for one fibre $X_w$ rules out transcendental isolated Hodge points at $w$ | proved here (consequence of the proof of Thm. B) |
| Prop. 4.1 | an atypical zero-dimensional special subvariety with Mumford–Tate group $\mathrm{GL}_2$ (not CM), in a family over $\mathbb Q$ | proved here (elementary). The phenomenon is known: non-CM atypical points of curves in products of modular curves. Corrects `docs/03` C3. |
| Theorem 4.2 | same $\mathbb Z$-local system and same $\mathbb Q$-model of the de Rham data, but one family has a transcendental isolated Hodge point (and a positive-dimensional component not defined over $\overline{\mathbb Q}$) and the other does not | proved here (elementary). It contradicts the literal [KOU, Conj. 1.5(a)], whose 'defined over $L$' is de Rham-only; see the remark after Thm. 4.2. |
| Remark 4.3 | $\mathrm{FD}_0$ (equivalently CI, equivalently (a) given $\mathrm{HC}(\overline{\mathbb Q})$) cannot be proved from Betti data, de Rham data over $\overline{\mathbb Q}$, and theorems valid for all polarized $\mathbb Z$-VHS | heuristic reading of Thm. 4.2. 'A proof that uses only …' is not a formal notion. |
