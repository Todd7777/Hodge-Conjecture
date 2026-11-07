# Attack 10: Hypersurfaces — Jacobian rings, Noether–Lefschetz loci, sextic fourfolds

**Status (read this first).** The top target (a), $\mathrm{HC}(X,2)$ for every smooth sextic fourfold $X\subset\mathbb P^5$, is **not** proved. Nothing here touches the zero-dimensional components of the Hodge locus. At the Fermat point these are the generic case: a general rational class there has an isolated Hodge locus (Prop. 7.5). What is proved, with complete proofs:

1. **Theorem A.** If the Jacobian-ring element $P_\lambda$ of a Hodge class $\lambda$ is annihilated by three independent linear forms, then either $\lambda\in\mathbb Q[\Pi]\oplus\mathbb Q h^2$ for a plane $\Pi\subset X$, or $X$ lies in an explicit locus $\mathcal W$ of codimension $\ge 34$.
2. **Rung (b) with $c=19$.** Theorem C, unconditional: there is a proper Zariski-closed subset $E$ of the parameter space, not containing the Fermat point, such that every component of a Hodge locus of codimension $\le 19$ that is not contained in $E$ is a component of the locus of sextics containing a plane, and HC holds along it. Theorem B: if a precise statement (G1) about Artinian Gorenstein algebras holds, the same is true with $E=\emptyset$. The inequality "codimension $\ge 19$ near the Fermat point" is Movasati's. The uniqueness statement off $E$, and its proof by torus degeneration of Gorenstein annihilators (Lemma 5.1, Theorem 5.3), are new as far as I know.
3. **Corollary 5.4.** At a *fake plane* (a Jacobian plane not contained in $X$), the germ of the Hodge locus is never smooth when the point lies off $E$, for example at the Fermat point.
4. **Proposition 6.2.** An unconditional bound at every point: every component has codimension $\ge 8$. The Macaulay–Gotzmann method provably cannot give more.
5. **Rungs (c) and (d).** Prop. 7.1 is a Hessian-rank criterion for the variational Hodge conjecture (VHC). Cor. 7.2 applies it to complete-intersection surfaces, recovering Dan and Kloosterman. Prop. 7.4 and Table 2 compute exactly, for every Hodge character of the Fermat sextic fourfold, the codimension of the Zariski tangent space of the Hodge locus. They also give explicit one-parameter families that carry non-linear Hodge classes, along which no algebraic cycle is constructed here.

*Literature caveat.* arXiv and journal sites were blocked, and the web-search budget ran out during the session. Statements taken from the literature are given as found in abstracts or as I recall them, and are marked **[lit]**.

## 0. Notation and conventions

Let $S=\mathbb C[x_0,\dots,x_5]$, let $F\in S_6$ with $X=X_F=V(F)\subset\mathbb P^5$ smooth, let $J=J_F=(\partial_0F,\dots,\partial_5F)$, and let $R=R^F=S/J$.

* The $\partial_iF$ have no common zero, so they form a regular sequence. Hence $R$ is Artinian Gorenstein of socle degree $24$, with $\dim R_k=[t^k](1+t+\dots+t^4)^6$. In particular $\dim R_6=\dim R_{18}=426$ and $\dim R_{12}=1751$.
* $R_k\times R_{24-k}\to R_{24}\cong\mathbb C$ is perfect (Macaulay). Fix an isomorphism $\mathrm{Res}:R_{24}\to\mathbb C$.

For $P\in R_{12}$ define:

* $\mathrm{Ann}(P)=\{Q\in S:QP=0 \text{ in } R\}\supseteq J$;
* $A_P=S/\mathrm{Ann}(P)$ and $h_P(k)=\dim(A_P)_k$;
* $\mathrm{rk}(P)=\mathrm{rank}(R_6\xrightarrow{\cdot P}R_{18})=h_P(6)$.

Since $A_P\cong R\cdot P$ up to a shift by $12$, for $P\ne0$ the ring $A_P$ is Artinian Gorenstein of socle degree $12$. Consequently:

* $h_P(k)=h_P(12-k)$;
* $Q\in\mathrm{Ann}(P)_k$ if and only if $QS_{12-k}\subseteq\mathrm{Ann}(P)_{12}$;
* $\mathrm{Ann}(P)$ determines $P$ up to a scalar.

We write $[a]_t=1+t+\dots+t^{a-1}$.

Let $U\subset\mathbb P(S_6)=\mathbb P^{461}$ be the open set of smooth sextics and $\tilde U\subset S_6$ its cone. Let $h$ be the hyperplane class, so $h^4=6$, and put $\lambda_{prim}=\lambda-\frac{\lambda\cdot h^2}{6}h^2$. Let $\mathcal P\subset U$ be the closed set of sextics containing a plane.

**Hodge loci.** For $t_0\in U$ and $\lambda\in\mathrm{Hdg}^2(X_{t_0})$ with $\lambda_{prim}\neq0$, transport $\lambda$ flatly over a small ball $B\ni t_0$.

* $NL_\lambda\subset B$ is the complex subspace defined by $\langle\lambda_t,\omega\rangle=0$ for $\omega$ in a holomorphic frame of $\mathcal F^3$. Since $(F^3)^\perp=F^2$, this is the locus where $\lambda_t\in F^2$.
* A *component of $NL_\lambda$ through $t_0$* is an irreducible component of the reduced germ $(NL_\lambda,t_0)$.
* *General points* of a component are those outside a proper closed analytic subset.
* Codimensions are taken in $U$. They equal codimensions in moduli, because everything is $PGL_6$-invariant.
* All statements below are local. Cattani–Deligne–Kaplan [CDK] is needed only to read them globally.

## 1. The Hodge locus as a critical locus

**Facts 1.1 [known].**
(i) (Griffiths [Gr]) Let $\Omega=\sum_i(-1)^ix_i\,dx_0\wedge\cdots\widehat{dx_i}\cdots\wedge dx_5$. For $0\le q\le 4$:
* the classes $\mathrm{res}(Q\Omega/F^{q+1})$, $Q\in S_{6q}$, span $F^{4-q}H^4_{prim}$;
* $Q\mapsto \mathrm{res}(Q\Omega/F^{q+1})$ induces an isomorphism $R_{6q}\xrightarrow{\sim}F^{4-q}H^4_{prim}/F^{5-q}$.

(ii) Residues are integrals over tubes, and the tubes move locally constantly with $F$. Hence the Gauss–Manin derivative along $F+\epsilon A$ is $\partial_A\,\mathrm{res}(Q\Omega/F^{q+1})=-(q+1)\,\mathrm{res}(AQ\Omega/F^{q+2})$. This is the Carlson–Griffiths description of the infinitesimal variation of Hodge structure as multiplication in $R$ [CG].

For $\lambda$ as in §0, define on a conic neighbourhood of $F_0$ in $\tilde U$:
* the **superpotential** $\Phi_\lambda(F)=\langle\lambda_F,\mathrm{res}(\Omega/F)\rangle$, which is homogeneous of degree $-1$;
* the functional $\ell_\lambda(Q)=\langle\lambda,\mathrm{res}(Q\Omega/F_0^3)\rangle$;
* the element $P_\lambda\in R_{12}$ with $\ell_\lambda(Q)=\mathrm{Res}(QP_\lambda)$.

**Proposition 1.2 (the Hodge locus is a critical locus; known in substance [GVW, BV]).** On the cone, $\widetilde{NL}_\lambda=\mathrm{Crit}(\Phi_\lambda)$ as complex spaces: its ideal is generated by the $\partial_A\Phi_\lambda$, $A\in S_6$. Moreover $\mathrm{Hess}_{F_0}\Phi_\lambda(A,B)=2\,\mathrm{Res}(ABP_\lambda)$, and $P_\lambda\neq0$ if and only if $\lambda_{prim}\neq0$.

*Proof.*
1. By 1.1(ii), $\partial_A\Phi_\lambda=-\langle\lambda,\mathrm{res}(A\Omega/F^2)\rangle$.
2. By 1.1(i), these classes span $F^3H^4=F^3H^4_{prim}$ as $A$ runs over $S_6$; note that $\mathrm{res}(\Omega/F)=\mathrm{res}(F\Omega/F^2)$.
3. So the $\partial_A\Phi_\lambda$ are the pairings of $\lambda$ with a spanning family of holomorphic sections of $\mathcal F^3$. They therefore generate the ideal of $NL_\lambda$.
4. Differentiating once more, $\partial_B\partial_A\Phi_\lambda=2\langle\lambda,\mathrm{res}(AB\Omega/F^3)\rangle=2\ell_\lambda(AB)$.
5. $\ell_\lambda$ factors through $R_{12}$: for $Q\in J$ we have $\mathrm{res}(Q\Omega/F^3)\in F^3$, and $\lambda\in H^{2,2}\perp F^3$.
6. $\ell_\lambda$ pairs $F^2_{prim}/F^3\cong R_{12}$ with $\lambda_{prim}\in H^{2,2}_{prim}$. This pairing is perfect by Hodge–Riemann, so $\ell_\lambda\neq0$ if and only if $\lambda_{prim}\ne0$. $\square$

**Corollary 1.3.**
* $T_{F_0}\widetilde{NL}_\lambda=\mathrm{Ann}(P_\lambda)_6$, so the Zariski tangent space of $NL_\lambda$ at $t_0$ has codimension $\mathrm{rk}(P_\lambda)$.
* Every component $Z$ of $NL_\lambda$ through any point $t$ satisfies $\operatorname{codim}Z\ge\mathrm{rk}(P_{\lambda_t})$.
* At smooth points $t$ of $Z$, $\mathrm{rk}(P_{\lambda_t})\le\operatorname{codim}Z$.

*Proof.*
1. $\Phi_\lambda$ and $d\Phi_\lambda$ vanish at $F_0$. So the tangent space is the kernel of the Hessian.
2. By duality, $\mathrm{Res}(ABP)=0$ for all $B\in R_6$ if and only if $AP=0$ in $R_{18}$.
3. A smooth germ contained in $NL_\lambda$ has its tangent space inside the Zariski tangent space. $\square$

*Remark (residual potential).* Work on a slice transverse to the $PGL_6$-orbits. By the holomorphic splitting lemma [AGV, §11],
$$\Phi_\lambda\simeq y_1^2+\dots+y_r^2+g(z),\qquad r=\mathrm{rk}(P_\lambda),\quad g\in\mathfrak m_z^3,$$
with $z$ running over $426-r$ variables. Hence $(NL_\lambda,t_0)\cong(\mathrm{Crit}(g),0)$. Jacobian-ring data at a single point see only $r$; the germ is smooth if and only if $g\equiv0$, and Cor. 5.4 is about this.

## 2. The class of a plane

**Lemma 2.1.** Let $\Pi=V(x_0,x_1,x_2)\subset X$ and write $F=x_0G_0+x_1G_1+x_2G_2$. Put $\mathcal I_\Pi=(x_0,x_1,x_2,G_0,G_1,G_2)$. Then:
* $\mathcal I_\Pi$ is a complete intersection;
* $[\Pi]_{prim}\neq0$;
* $\mathrm{Ann}(P_{[\Pi]})=\mathcal I_\Pi$, so $\mathrm{rk}(P_{[\Pi]})=[t^6][5]_t^3=19$.

Moreover $\mathcal P$ has codimension $19$. This agrees with Villaflor's determinantal formula for complete-intersection cycles [Vi2] **[lit]**; the proof below is self-contained.

*Proof.*
1. *Complete intersection.* A common zero $p$ of $\mathcal I_\Pi$ lies on $\Pi$. There $\partial_jF(p)=G_j(p)+\sum_{i\le2}x_i(p)\partial_jG_i(p)=0$ for every $j$, where $G_j:=0$ for $j\ge3$. This contradicts smoothness. So the six generators form a regular sequence, and $S/\mathcal I_\Pi$ is Gorenstein of socle degree $12$.
2. *$[\Pi]_{prim}\ne0$.* We have $[\Pi]^2=c_2(N_{\Pi/X})=[h^2]\big((1+h)^3(1+6h)^{-1}\big)=21$ and $[\Pi]\cdot h^2=1$. If $[\Pi]_{prim}=0$, then $[\Pi]=h^2/6$ and $[\Pi]^2=1/6$, which is absurd.
3. *The incidence variety.* $\{(F',\Pi'):F'|_{\Pi'}=0\}\subset\tilde U\times G(3,6)$ is a vector bundle over the Grassmannian, hence smooth of dimension $9+434=443$. Along it, $[\Pi']$ is the flat transport of $[\Pi]$. So its image lies in $\widetilde{NL}_{[\Pi]}$, and by Cor. 1.3 the image of its tangent space lies in $\mathrm{Ann}(P_{[\Pi]})_6$.
4. *Tangent vectors.* A tangent vector is a pair $(\dot F,\phi)$, where $\phi_0,\phi_1,\phi_2$ are linear forms in $x_3,x_4,x_5$ describing the moving plane $x_i=\epsilon\phi_i$. The constraint is $\dot F|_\Pi+\sum_i\phi_iG_i|_\Pi=0$. The set of such $\dot F$ is exactly $(\mathcal I_\Pi)_6$, which has dimension $462-19=443$. So the differential is injective, and $\mathcal P$ has codimension $19$.
5. *The two ideals agree in degree 12.* $\mathcal I_\Pi$ is generated in degrees $\le5$, so $(\mathcal I_\Pi)_{12}=(\mathcal I_\Pi)_6S_6\subseteq\mathrm{Ann}(P_{[\Pi]})_{12}$. Both are hyperplanes of $S_{12}$ (socle degree $12$, and $P_{[\Pi]}\neq0$), hence they are equal.
6. *Conclusion.* For both Gorenstein ideals, $Q\in I_k$ if and only if $QS_{12-k}\subseteq I_{12}$. So the two ideals coincide. $\square$

## 3. Jacobian planes

**Definition.** A plane $\Pi\subset\mathbb P^5$ is a *Jacobian plane* of $F$ if the restrictions $\partial_0F|_\Pi,\dots,\partial_5F|_\Pi\in H^0(\mathcal O_\Pi(5))$ span a space of dimension $\le3$. Write $V_\Pi$ for this span.

**Proposition 3.1.** Let $0\ne P\in R_{12}$. Then $h_P(1)\ge3$. Suppose $h_P(1)=3$, and put $\Pi=V(\mathrm{Ann}(P)_1)$. Then:
* $\Pi$ is a Jacobian plane, and $V_\Pi$ is $3$-dimensional and base-point free;
* $\mathrm{Ann}(P)=I_\Pi+(\tilde V_\Pi)$ for any lift $\tilde V_\Pi\subset S_5$ of $V_\Pi$; this is a complete intersection of type $(1,1,1,5,5,5)$;
* $h_P$ is the coefficient sequence of $[5]_t^3$, namely $(1,3,6,10,15,18,19,18,15,10,6,3,1)$, so $\mathrm{rk}(P)=19$.

Conversely, every Jacobian plane $\Pi$ arises in this way from exactly one line $\mathbb CP_\Pi\subset R_{12}$.

*Proof.*
1. *Setup.* Let $r=h_P(1)$ and choose coordinates with $\mathrm{Ann}(P)_1=\langle x_r,\dots,x_5\rangle$. Put $T=\mathbb C[x_0,\dots,x_{r-1}]$. Then $A_P\cong T/\bar I$, where $\bar I$ is Gorenstein of socle degree $12$ and contains the restrictions $\partial_iF|_L$ to $L=V(x_r,\dots,x_5)\cong\mathbb P^{r-1}$.
2. *Regular sequence.* The restrictions $\partial_iF|_L$ have no common zero on $L$, since such a zero would be a singular point of $X$. So $r$ general linear combinations $q_1,\dots,q_r$ of them form a regular sequence in $T$.
3. *$r\ge3$.* $A_P$ is a quotient of $B=T/(q_1,\dots,q_r)$, which has socle degree $4r$. Hence $12\le4r$, i.e. $r\ge3$.
4. *The case $r=3$.* Here $B$ is Gorenstein with the same socle degree as its quotient $A_P$. A nonzero ideal of $B$ contains the socle $B_{12}$, so $\bar I=(q_1,q_2,q_3)$.
5. *Consequences.* Then $\bar I_5=\langle q_1,q_2,q_3\rangle\supseteq V_\Pi\supseteq\langle q_1,q_2,q_3\rangle$, so $V_\Pi=\bar I_5$. This gives all the listed claims.
6. *Converse.* If $\Pi$ is a Jacobian plane, then $V_\Pi$ is base-point free; hence it is $3$-dimensional and spanned by a regular sequence. So $\mathcal I=I_\Pi+(\tilde V_\Pi)\supseteq J$ is a complete intersection of socle degree $12$. The space $(\mathcal I/J)_{12}$ is a hyperplane of $R_{12}$, and its $\mathrm{Res}$-orthogonal is a line $\mathbb CP_\Pi$. Step 6 of the proof of Lemma 2.1 then shows $\mathrm{Ann}(P_\Pi)=\mathcal I$. $\square$

*Numerical check.* At the Fermat point, for Jacobian planes of the two shapes $\{x_0=t_1x_1,\,x_2=t_2x_3,\,x_4=t_3x_5\}$ and $\{x_3=ax_2,\,x_4=bx_2,\,x_5=cx_2\}$ with random parameters, I solved $\ell\cdot P=0$ in $R_{13}$ for the three linear forms $\ell$ over $\mathbb F_{1000003}$. The solution space was $1$-dimensional and its rank was $19$. For a random plane the solution space was $0$.

So the following are equivalent: $P_\lambda$ is annihilated by three independent linear forms; $\mathrm{Ann}(P_\lambda)$ is the ideal of a Jacobian plane; $h_{P_\lambda}=[5]_t^3$. Each of them forces $\mathrm{rk}=19$. Every plane $\Pi\subset X$ is a Jacobian plane, with $P_\Pi\propto P_{[\Pi]}$ (Lemma 2.1). Jacobian planes not contained in $X$ are rare:

**Proposition 3.2.** Let $\mathcal W\subset U$ be the set of $[F]$ that have a Jacobian plane $\Pi\not\subset X_F$. Then:
* $\mathcal W$ is constructible and $PGL_6$-invariant, and $\dim\overline{\mathcal W}\le\dim U-34$;
* if $\Pi=V(x_0,x_1,x_2)$ is such a plane, $f=F|_\Pi$, and $\dim\langle\partial f\rangle=3$, then in suitable linear coordinates $y'$ on a complementary plane, $F\equiv f(y')\bmod (x_0,x_1,x_2)^2$.

*Proof.*
1. *Decomposition.* Fix $\Pi=V(x_0,x_1,x_2)$ and put $T=\mathbb C[x_3,x_4,x_5]$. Write uniquely $F=f+\sum_{i\le 2}x_iG_i+H$ with $f\in T_6$, $G_i\in T_5$ and $H\in(x_0,x_1,x_2)^2$. Then $\partial_iF|_\Pi=G_i$ for $i\le2$ and $\partial_jF|_\Pi=\partial_jf$ for $j\ge3$.
2. *The number $s$.* Let $s=\dim\langle\partial_3f,\partial_4f,\partial_5f\rangle$. Since $f\neq0$, Euler's formula gives $s\in\{1,2,3\}$. A ternary form whose first partials span an $s$-dimensional space is, after a linear change, a form in $s$ variables: each relation $\sum_jc_j\partial_jf=0$ is a translation invariance.
3. *Counting.* The condition is that $\langle\partial f\rangle+\langle G_0,G_1,G_2\rangle\subseteq V$ for some $V\in G(3,T_5)$. The admissible pairs $(f,G)$ form a set of dimension at most $\dim\{f\}+(3-s)\cdot18+9$. This equals $28+0+9=37$ for $s=3$, $9+18+9=36$ for $s=2$, and $3+36+9=48$ for $s=1$. The space of all $(f,G)$ has dimension $91$, and $H$ is free.
4. *Codimension.* So for fixed $\Pi$ the condition has codimension $\ge43$ in $S_6$. Letting $\Pi$ vary in the $9$-dimensional Grassmannian gives codimension $\ge34$ for $\mathcal W$. Constructibility holds because $\mathcal W$ is the image of a locally closed incidence variety.
5. *Normal form.* If $s=3$, write $G_i=\sum_ja_{ij}\partial_jf$ and set $y'=y+A^{\mathsf T}x$. Then $f(y')\equiv f+\sum_ix_iG_i \bmod (x)^2$. $\square$

**Theorem A.** Let $X$ be a smooth sextic fourfold and $\lambda\in\mathrm{Hdg}^2(X)$ with $\lambda_{prim}\ne0$. Suppose $P_\lambda$ is annihilated by three independent linear forms, and let $\Pi$ be their common zero set. Then the Zariski tangent space of $NL_\lambda$ has codimension $19$, and:
* if $\Pi\subset X$, then $\lambda\in\mathbb Q[\Pi]\oplus\mathbb Qh^2$, so $\lambda$ is algebraic;
* if $\Pi\not\subset X$, then $[X]\in\mathcal W$.

In particular, HC holds for all such classes on every $X\notin\mathcal W$.

*Proof.*
1. By Prop. 3.1, $\mathrm{Ann}(P_\lambda)=I_\Pi+(\tilde V_\Pi)$ and $\mathrm{rk}=19$.
2. Suppose $\Pi\subset X$. Then $\partial_jF|_\Pi=0$ for $j\ge3$, so $V_\Pi=\langle G_0,G_1,G_2\rangle|_\Pi$ and the ideal above is $\mathcal I_\Pi$. By Lemma 2.1, $\mathcal I_\Pi=\mathrm{Ann}(P_{[\Pi]})$. Hence $P_\lambda=cP_{[\Pi]}$ for some $c\in\mathbb C^*$.
3. The map $\lambda\mapsto P_\lambda$ is linear and injective on primitive classes (Prop. 1.2). So $\lambda_{prim}=c[\Pi]_{prim}$.
4. Both classes are rational and nonzero, so $c\in\mathbb Q$, and $\lambda=c[\Pi]+\frac{\lambda\cdot h^2-c}{6}h^2$.
5. If $\Pi\not\subset X$, then $[X]\in\mathcal W$ by definition. $\square$

## 4. Components of codimension at most 19

**Lemma 4.1 (plane classes specialize).** Let $Z$ be a component of $NL_\lambda$ through $t_0$. Suppose that for a dense set of $t\in Z$ there are a plane $\Pi_t\subset X_t$ and $a_t,b_t\in\mathbb Q$ with $\lambda_t=a_t[\Pi_t]+b_th^2$. Then the same holds at every point of $Z$.

*Proof.*
1. We have $\lambda_{prim}^2=a_t^2[\Pi_t]_{prim}^2=\tfrac{125}{6}a_t^2$, and the left side is constant. So $a_t=\pm a$ for a fixed $a$, and $b_t=(\lambda\cdot h^2-a_t)/6$.
2. Choose $t_n\to t_0$ with $(a_{t_n},b_{t_n})$ constant and, by compactness of the Grassmannian, $\Pi_{t_n}\to\Pi_\infty$. Then $\Pi_\infty\subset X_{t_0}$.
3. The relative Fano scheme of planes over $B$ is a closed analytic subset of $B\times G(3,6)$. It is locally path connected, and the cycle class is locally constant on it. Hence the flat transport of $[\Pi_{t_n}]$ is $[\Pi_\infty]$ for $n\gg0$.
4. So $\lambda_{t_0}=a[\Pi_\infty]+bh^2$. $\square$

**Corollary 4.2.** Let $Z$ be a component of $NL_\lambda$ through $t_0$ with $\operatorname{codim}Z\le33$. Suppose $P_{\lambda_t}$ is annihilated by three linear forms for $t$ in a dense subset of $Z$. Then:
* $Z$ is a component of the germ $(\mathcal P,t_0)$, and $\operatorname{codim}Z=19$;
* for every $t\in Z$ there is a plane $\Pi_t\subset X_t$ with $\lambda_t\in\mathbb Q[\Pi_t]\oplus\mathbb Qh^2$.

*Proof.*
1. The condition $\dim\mathrm{Ann}(P_{\lambda_t})_1\ge3$ is closed: it is a rank condition on $S_1\to S_{11}^\vee$, $L\mapsto\ell_{\lambda_t}(L\,\cdot\,)$, which depends holomorphically on $t$. So it holds on all of $Z$.
2. Since $\dim Z>\dim\overline{\mathcal W}$, a general $t\in Z$ is not in $\overline{\mathcal W}$, and Theorem A applies there.
3. Lemma 4.1 extends the conclusion to all of $Z$. In particular $Z\subseteq\mathcal P$. By Prop. 3.1, $\dim\mathrm{Ann}(P_{\lambda_t})_1\le3$, so it equals $3$ on $Z$. Hence the planes $\Pi_t=V(\mathrm{Ann}(P_{\lambda_t})_1)\subset X_t$ vary continuously with $t\in Z$.
4. Fix a general $t\in Z$. Let $\mathcal P_t$ be the germ at $t$ of the image of the incidence variety near $(t,\Pi_t)$. By step 4 of the proof of Lemma 2.1 it is smooth of codimension $19$.
5. $\mathcal P_t\subseteq NL_\lambda$: along $\mathcal P_t$ the plane $\Pi_t$ deforms with flat class, so $\lambda=a[\Pi_t]+bh^2$ stays Hodge.
6. $Z\subseteq\mathcal P_t$ near $t$, by the continuity in step 3.
7. At a general point, $(Z,t)$ is an irreducible component of $(NL_\lambda,t)$, so $(Z,t)=\mathcal P_t$. Hence $\operatorname{codim}Z=19$, and since $Z\subseteq\mathcal P$, $Z$ is a component of $(\mathcal P,t_0)$. $\square$

To pass from "codimension $\le19$" to the hypothesis of Cor. 4.2, one needs the following statement.

> **(G1) Infinitesimal plane bound.** For every smooth sextic $F$ and every $0\ne P\in R^F_{12}$: if $\mathrm{rk}(P)\le19$, then $\dim\mathrm{Ann}(P)_1\ge3$.

By Prop. 3.1, (G1) is equivalent to: $\mathrm{rk}(P)\ge19$ for all $P\neq0$, with equality only for $h_P=[5]_t^3$. Its equality case cannot be strengthened to "$\Pi\subset X$", because of fake planes (§5).

**Theorem B (conditional on (G1)).** Assume (G1). Let $Z$ be any component of any $NL_\lambda$ with $\lambda_{prim}\ne0$. Then:
* $\operatorname{codim}Z\ge19$;
* if $\operatorname{codim}Z\le19$, then $Z$ is a component of $(\mathcal P,t_0)$ and $\lambda_t\in\mathbb Q[\Pi_t]\oplus\mathbb Qh^2$ for all $t\in Z$.

In particular, HC holds for every Hodge class whose Hodge locus has a component of codimension $\le19$.

*Proof.*
1. If $\mathrm{rk}(P_{\lambda_t})\le18$ at some point, then (G1) and Prop. 3.1 give $\mathrm{rk}=19$, a contradiction. So $\operatorname{codim}Z\ge19$ by Cor. 1.3.
2. If $\operatorname{codim}Z\le19$, then $\mathrm{rk}\le19$ at the smooth points of $Z$ by Cor. 1.3. By (G1), $P_{\lambda_t}$ is annihilated by three linear forms on this dense set. Now apply Cor. 4.2. $\square$

## 5. The Fermat point, and a Zariski-open set where (G1) holds

Let $F_0=\sum x_i^6$. Then $J_{F_0}=(x_i^5)$, and $R$ has the monomial basis $x^\beta$ with $0\le\beta_i\le4$. One has $\mathrm{Ann}(x^\beta)=(x_0^{5-\beta_0},\dots,x_5^{5-\beta_5})$, so the Hilbert series of $A_{x^\beta}$ is $\prod_i[5-\beta_i]_t$. Let $\mathcal R_k\to U$ be the vector bundle with fibres $R^F_k$; it has constant rank because $J_F$ is a complete intersection.

**Lemma 5.1 (limits of Gorenstein annihilators).** Let $(F_n,[P_n])\to(F_\infty,[P_\infty])$ in $\mathbb P(\mathcal R_{12})$, with $h_{P_n}=h$ for all $n$. Suppose $\mathrm{Ann}(P_\infty)$ is generated in degrees $\le6$ and $h_{P_\infty}(6)=h(6)$. Then $h=h_{P_\infty}$.

*Proof.*
1. Pass to a subsequence along which $\mathrm{Ann}(P_n)_k$ converges to a point $I_k$ of the Grassmannian, for each $k\le12$.
2. $I=\bigoplus_k I_k$ is an ideal, because this is a closed condition.
3. $I_k\subseteq\mathrm{Ann}(P_\infty)_k$: if $Q_nP_n\in J_{F_n}$ and $Q_n\to Q$, then $QP_\infty\in J_{F_\infty}$, since $(J_{F_n})_m\to(J_{F_\infty})_m$.
4. At $k=6$ the dimensions agree, so $I_6=\mathrm{Ann}(P_\infty)_6$.
5. For $k\ge6$, $\mathrm{Ann}(P_\infty)_k=S_{k-6}I_6\subseteq I_k$, so equality holds. Hence $h(k)=h_{P_\infty}(k)$ for $k\ge6$.
6. For $k\le6$, use the Gorenstein symmetry of both functions. $\square$

**Proposition 5.2 (the Fermat point).** For every $0\ne P\in R^{F_0}_{12}$ we have $\mathrm{rk}(P)\ge19$. If $\mathrm{rk}(P)=19$, then $h_P=[5]_t^3$, so $P$ is annihilated by three linear forms; that is, (G1) holds at $F_0$. The inequality is Movasati's [Mo] **[lit]**.

*Proof.*
1. *Torus action.* The torus $(\mathbb C^*)^6$ preserves $J_{F_0}$, so it acts on $R$ by graded automorphisms, preserving $\mathrm{rk}$ and $h_P$.
2. *Degeneration to a vertex.* Let $\beta^*$ be a vertex of the Newton polytope of $P$, and let $\rho$ be a one-parameter subgroup for which $\beta^*$ is the unique weight-minimizer. Then $s^{-c}\rho(s)P\to c_{\beta^*}x^{\beta^*}$ as $s\to0$.
3. *Inequality.* Rank is lower semicontinuous, so $\mathrm{rk}(P)\ge\mathrm{rk}(x^{\beta^*})=[t^6]\prod_i[5-\beta^*_i]_t$. Enumerating all $\beta$ with $|\beta|=12$ and $\beta_i\le4$ shows this is $\ge19$. Equality holds only when $\{4-\beta_i\}=\{4,4,4,0,0,0\}$; the next value is $32$.
4. *Equality case.* If $\mathrm{rk}(P)=19$, then $x^{\beta^*}$ is of that type, and $\mathrm{Ann}(x^{\beta^*})=(x_i,x_j,x_k,x_a^5,x_b^5,x_c^5)$ is generated in degrees $\le5$. Apply Lemma 5.1 with $F_n=F_0$ and $P_n=s_n^{-c}\rho(s_n)P$; it gives $h_P=h_{x^{\beta^*}}$. $\square$

**Theorem 5.3.** There is a dense Zariski-open, $PGL_6$-invariant set $V\subset U$ containing $[F_0]$ such that, for every $F\in V$, (G1) holds and $\mathrm{rk}(P)\ge19$ for all $0\ne P\in R^F_{12}$.

*Proof.*
1. *Definition of $V$.* In $\mathbb P(\mathcal R_{12})$, let $\mathcal B_0=\{\mathrm{rk}\le18\}$, which is closed, and $\mathcal B_1=\{\mathrm{rk}\le19,\ h_P(1)\ge4\}$, which is locally closed; both are rank conditions on bundle maps. Put $E=\mathrm{pr}(\mathcal B_0)\cup\overline{\mathrm{pr}(\mathcal B_1)}$ and $V=U\setminus E$. The set $E$ is closed because $\mathrm{pr}$ is proper.
2. *$F_0\notin\mathrm{pr}(\mathcal B_0)$:* this is Prop. 5.2.
3. *$F_0\notin\overline{\mathrm{pr}(\mathcal B_1)}$.* Suppose otherwise. For constructible sets, the Zariski closure equals the classical closure. So there are $(F_n,[P_n])\in\mathcal B_1$ with $F_n\to F_0$, and by properness $[P_n]\to[P_\infty]$; we may assume $h_{P_n}=h$ is constant.
4. Then $\mathrm{rk}(P_\infty)\le19$, so by Prop. 5.2 $\mathrm{rk}(P_\infty)=19$ and $\mathrm{Ann}(P_\infty)$ is a complete intersection of type $(1,1,1,5,5,5)$. By semicontinuity $\mathrm{rk}(P_n)=19$, so $h(6)=19=h_{P_\infty}(6)$.
5. Lemma 5.1 gives $h(1)=h_{P_\infty}(1)=3$, contradicting $h(1)\ge4$. $\square$

**Theorem C (rungs (b) and (c), unconditional).** Let $E=U\setminus V$ be as in Theorem 5.3. Let $t_0\in U$, let $\lambda\in\mathrm{Hdg}^2(X_{t_0})$ with $\lambda_{prim}\ne0$, and let $Z$ be a component of $NL_\lambda$ through $t_0$ with $Z\not\subseteq E$. Then:
* $\operatorname{codim}Z\ge19$;
* if $\operatorname{codim}Z\le19$, then $Z$ is a component of $(\mathcal P,t_0)$, and for every $t\in Z$ there is a plane $\Pi_t\subset X_t$ with $\lambda_t\in\mathbb Q[\Pi_t]\oplus\mathbb Qh^2$.

In particular this applies to every component through the Fermat point. For $(n,d)=(4,6)$ it recovers the uniqueness of the minimal-codimension component through the Fermat point due to Duque Franco–Villaflor Loyola [DV] **[lit]**, and extends it to all components not contained in $E$.

*Proof.* The general points of $Z$ lie in $V$ and are smooth points of $Z$. Run the proof of Theorem B at these points, using Theorem 5.3 in place of (G1). $\square$

**Corollary 5.4 (fake planes).** Let $t_0\in V$ and $\lambda\in\mathrm{Hdg}^2(X_{t_0})$ with $\mathrm{rk}(P_\lambda)=19$, and suppose $\lambda\notin\mathbb Q[\Pi]\oplus\mathbb Qh^2$ for every plane $\Pi\subset X_{t_0}$. Then:
* $P_\lambda\propto P_\Pi$ for a Jacobian plane $\Pi\not\subset X_{t_0}$;
* every component of $NL_\lambda$ through $t_0$ has codimension $\ge20$, while the Zariski tangent space has codimension $19$; so the germ $(NL_\lambda,t_0)$ is not smooth.

Such classes exist at $t_0=[F_0]$: they are the "fake linear cycles" for $d=6$ of [DV] **[lit]**, who prove the stronger statement that the Hodge locus is non-reduced there.

*Proof.*
1. Theorem 5.3 and Prop. 3.1 give the Jacobian plane $\Pi$, and Theorem A shows $\Pi\not\subset X_{t_0}$.
2. Every component through $t_0$ has codimension $\ge19$ by Cor. 1.3.
3. If some component through $t_0$ had codimension $19$, Theorem C would put $\lambda_{t_0}$ in $\mathbb Q[\Pi']\oplus\mathbb Qh^2$ for a plane $\Pi'\subset X_{t_0}$, contrary to the hypothesis.
4. A germ whose Zariski tangent space is larger than all of its components is not smooth. $\square$

## 6. What elementary Hilbert-function arguments give at every point

Write $a^{\langle k\rangle}$ for Macaulay's bound on the growth of a Hilbert function from degree $k$ to degree $k+1$.

**Lemma 6.1.** Let $F$ be any smooth sextic, $0\ne P\in R^F_{12}$, and $5\le k\le 11$. Then $h_P(k+1)<h_P(k)^{\langle k\rangle}$.

*Proof.*
1. Put $I=\mathrm{Ann}(P)$ and $I'=(I_{\le k})$. Since $k\ge5$, $I'\supseteq J$.
2. Suppose $h_P(k+1)\ge h_P(k)^{\langle k\rangle}$. Then $h_{S/I'}(k+1)\ge h_P(k+1)\ge h_{S/I'}(k)^{\langle k\rangle}$, so equality holds by Macaulay's theorem.
3. Gotzmann's persistence theorem [Go; BH 4.3.3] then gives $h_{S/I'}(m)\ge1$ for all $m\ge k$. Hence $V(I')\ne\emptyset$.
4. But $V(I')\subseteq V(J)=\emptyset$, a contradiction. $\square$

**Proposition 6.2.** For every smooth sextic $F$ and every $0\ne P\in R_{12}$, $\mathrm{rk}(P)\ge8$. Hence every component of every Hodge locus (of a class with nonzero primitive part) has codimension $\ge8$.

*Proof.*
1. Write $h=h_P$. By Gorenstein symmetry $h(k+1)=h(11-k)$, so Lemma 6.1 for $k=6,\dots,10$ gives
$$h(5)<h(6)^{\langle6\rangle},\quad h(4)<h(5)^{\langle7\rangle},\quad h(3)<h(4)^{\langle8\rangle},\quad h(2)<h(3)^{\langle9\rangle},\quad h(1)<h(2)^{\langle10\rangle}.$$
2. Recall that $a^{\langle k\rangle}=a$ for $a\le k$, and $(k+1)^{\langle k\rangle}=k+2$.
3. Suppose $h(6)\le7$. Then the inequalities give successively $h(5)\le7$, $h(4)\le6$, $h(3)\le5$, $h(2)\le4$ and $h(1)\le3$.
4. Prop. 3.1 then forces $h(6)=19$, a contradiction. $\square$

*The method cannot do better.* I searched exhaustively over symmetric sequences that satisfy Macaulay's bounds and Lemma 6.1. Sequences such as $(1,4,5,6,7,8,8,8,7,6,5,4,1)$ and $(1,6,7,8,9,9,9,9,9,8,7,6,1)$ survive. So these tools cannot prove more than $8$. Closing the gap from $8$ to $19$ needs information about Artinian Gorenstein algebras of codimension $4$–$6$ that I do not have; see (G1) in §8.

## 7. A criterion for VHC, and an honest list (rungs (c), (d))

**Proposition 7.1 (Hessian-rank criterion; folklore, cf. [Mo, Da, Kl]).** Let $t_0\in U$ and $\lambda=\sum_in_i[W_i]$ with $W_i\subset X_{t_0}$ surfaces. Let $\psi:(M,m_0)\to(\tilde U,F_0)$ be a holomorphic map from a smooth germ, such that each $W_i$ deforms to $W_i(m)\subset X_{\psi(m)}$ with flat class. If $\mathrm{rank}\,d\psi_{m_0}=\dim S_6-\mathrm{rk}(P_\lambda)$, then:
* $\widetilde{NL}_\lambda$ is smooth at $F_0$, of codimension $\mathrm{rk}(P_\lambda)$, and coincides near $F_0$ with $\psi(M)$;
* hence $\lambda_t=\sum n_i[W_i(m)]$ is algebraic on a neighbourhood of $t_0$ in $NL_\lambda$.

By the standard countability argument (the algebraic locus of a flat class is a countable union of closed algebraic subsets, images of relative Hilbert schemes), $\lambda$ is then algebraic on the whole algebraic component through $t_0$, i.e. VHC holds along it.

*Proof.*
1. Since $\psi(M)\subseteq\widetilde{NL}_\lambda$, for $m$ near $m_0$:
$$\mathrm{rank}\,d\psi_m\le\dim T_{\psi(m)}\widetilde{NL}_\lambda\le\dim T_{F_0}\widetilde{NL}_\lambda=\mathrm{rank}\,d\psi_{m_0}\le\mathrm{rank}\,d\psi_m .$$
The second inequality is upper semicontinuity of the Zariski tangent dimension; the last is lower semicontinuity of rank.
2. So $d\psi$ has constant rank near $m_0$. By the constant rank theorem, $\psi(M)$ is a submanifold of dimension $\dim T_{F_0}\widetilde{NL}_\lambda$.
3. A germ containing a smooth germ of its own embedding dimension is smooth and equal to it. $\square$

**Corollary 7.2 (complete-intersection surfaces; recovers Dan [Da] and Kloosterman [Kl] for sextic fourfolds).** Let $X=V(\sum_{i=1}^3f_ig_i)$ with $\deg f_i=d_i\in\{1,2,3\}$ and $\deg g_i=6-d_i$, and suppose $W=V(f_1,f_2,f_3)$ is a surface. Then:
* $\mathrm{Ann}(P_{[W]})=(f_1,f_2,f_3,g_1,g_2,g_3)$;
* near $X$, $NL_{[W]}$ is smooth and equal to the locus of sextics containing a complete intersection of type $(d_i)$, of codimension $\mathrm{rk}=[t^6]\prod_i[d_i]_t[6-d_i]_t$.

For the ten types $(1,1,1)$, $(1,1,2)$, $(1,1,3)$, $(1,2,2)$, $(1,2,3)$, $(1,3,3)$, $(2,2,2)$, $(2,2,3)$, $(2,3,3)$, $(3,3,3)$ this codimension is $19, 32, 37, 54, 62, 71, 92, 106, 122, 141$.

*Proof.*
1. As in Lemma 2.1, the ideal is a complete intersection, since a common zero would be singular on $X$. Its socle degree is $\sum(d_i-1)+\sum(5-d_i)=12$, and it is generated in degrees $\le5$.
2. The map $\psi:(f',g')\mapsto\sum_i f'_ig'_i$ has differential with image $(f,g)_6$.
3. $[W]_{prim}\neq0$. For general $f$ the surface $W$ is smooth, and $[W]^2=\deg W\cdot(e_2-6e_1+36)$, where $e_k$ are the elementary symmetric functions of the $d_i$. In all ten cases this differs from $(\deg W)^2/6$; for example $66\ne6$ for type $(1,2,3)$. The classes are locally constant on the connected parameter space, so the conclusion holds for every $W$.
4. The argument of Lemma 2.1 then identifies the ideal, and Prop. 7.1 applies.
5. The codimensions agree with naive parameter counts: $28-9=19$ for planes, $49-17=32$ for quadric surfaces, $64-27=37$ for cubic surfaces, $85-31=54$ for type $(1,2,2)$, $146-54=92$ for type $(2,2,2)$. $\square$

**Lemma 7.3 (symmetric deformations).** Let $H$ be a group of diagonal automorphisms of $\mathbb P^5$ fixing $F_0$, and let $S_6^H$ be the span of the $H$-invariant monomials. Suppose $H^4(X_{F_0},\mathbb Q)^H$ is of type $(2,2)$. Then for every smooth $F\in S_6^H$, the flat continuation of $H^4(X_{F_0},\mathbb Q)^H$ consists of Hodge classes.

*Proof.*
1. $H$ acts fibrewise on the family over $\mathbb P(S_6^H)\cap U$, which is connected, and the action commutes with the Gauss–Manin connection.
2. The projector $e=|H|^{-1}\sum_{g\in H}g^*$ is flat, self-adjoint for the cup product, and preserves $\mathcal F^p$. So $\mathrm{rank}\,e(\mathcal F^3)$ is constant; it is zero at $F_0$, hence zero everywhere.
3. For invariant $\lambda$, $\langle\lambda,\mathcal F^3\rangle=\langle\lambda,e\mathcal F^3\rangle=0$. $\square$

**Proposition 7.4 (Fermat character classes).** Let $\alpha$ be a Hodge character of $X^4_6$, in the notation of `docs/04`, and let $\lambda\in W_\alpha$ be rational and nonzero. Put $\beta=\alpha-\mathbf 1$ and $\bar\beta=\mathbf 4-\beta$. Then:
* $P_\lambda=c\,x^\beta+c'x^{\bar\beta}$ with $cc'\neq0$, and $\mathrm{rk}(P_\lambda)$ does not depend on $(c,c')$; the values are in Table 2;
* if $H_\alpha=\ker\chi_\alpha$ satisfies the hypothesis of Lemma 7.3, then $\dim_{F_0}NL_\lambda\ge|M_\alpha|-6$ in moduli, where $M_\alpha$ is the set of degree-$6$ monomials $x^\gamma$ with $\gamma\bmod 6\in\mathbb Z\alpha$.

*Proof.*
1. *Form of $P_\lambda$.* $V(\pm\alpha)$ is spanned by $\mathrm{res}(x^{\pm\alpha-\mathbf1}\Omega/F_0^3)$, and complex conjugation exchanges them. So both components of a real $\lambda\ne0$ are nonzero. The pairing is $G$-invariant, and $\mathrm{Res}(x^\gamma x^\delta)\neq0$ if and only if $\gamma+\delta=\mathbf 4$; this gives the shape of $P_\lambda$.
2. *Rank.* In monomial bases, $x^\gamma\mapsto c\,x^{\gamma+\beta}+c'x^{\gamma+\bar\beta}$ is a bipartite graph of maximal degree $2$. A cycle would force $k(\beta-\bar\beta)=0$. So for $\beta\neq\bar\beta$ the components are paths, and a weighted path has full rank whenever all weights are nonzero. For $\beta=\bar\beta$ there is only one term.
3. *Symmetric family.* The tangent space of $\mathbb P(S_6^{H_\alpha})$ maps onto the span in $R_6$ of $M_\alpha\setminus\{x_i^6\}$. No $x_ix_j^5$ with $i\neq j$ is $H_\alpha$-invariant, because $k\alpha=e_i-e_j$ is impossible when every entry of $\alpha$ is nonzero mod $6$. Lower semicontinuity of rank then bounds the dimension of the image in moduli from below. $\square$

**Table 2.** The 1751 primitive Hodge characters of $X^4_6$ fall into 14 types up to permutation and $\alpha\mapsto-\alpha$. In the table, "#" is the number of characters of the type, "std" says whether $W_\alpha$ lies in the span of linear cycles (the standard types account for $1001$ characters, as in [BFLV] **[lit]**), "$\dim T$" is the dimension of the Zariski tangent space in moduli ($426-\mathrm{rk}$), and "sym" is the lower bound $|M_\alpha|-6$ for $\dim NL_\lambda$. A dash means the hypothesis of Lemma 7.3 fails, because $2\alpha$ has weight $2$.

| type | # | std | $\mathrm{rk}$ | $\dim T$ | sym |
|---|---|---|---|---|---|
| $(1,1,1,5,5,5)$ | 20 | yes | 38 | 388 | 0 |
| $(1,1,2,4,5,5)$ | 180 | yes | 64 | 362 | 0 |
| $(1,1,3,3,5,5)$ | 90 | yes | 74 | 352 | 0 |
| $(1,1,3,4,4,5)$ | 360 | **no** | 90 | 336 | 0 |
| $(1,2,2,4,4,5)$ | 180 | yes | 108 | 318 | 1 |
| $(1,1,4,4,4,4)$ | 30 | **no** | 112 | 314 | — |
| $(1,2,3,3,4,5)$ | 360 | yes | 122 | 304 | 0 |
| $(1,3,3,3,3,5)$ | 30 | yes | 122 | 304 | 2 |
| $(2,3,3,3,3,4)$ | 30 | yes | 122 | 304 | 2 |
| $(3,3,3,3,3,3)$ | 1 | yes | 141 | 285 | 0 |
| $(1,3,3,3,4,4)$ | 120 | **no** | 148 | 278 | 1 |
| $(1,2,3,4,4,4)$ | 240 | **no** | 150 | 276 | 1 |
| $(2,2,3,3,4,4)$ | 90 | yes | 178 | 248 | 1 |
| $(2,2,2,4,4,4)$ | 20 | yes | 182 | 244 | 0 |

The ranks were computed over $\mathbb F_{1000003}$. By step 2 of the proof of Prop. 7.4 the rank equals the combinatorial path rank, so the field and the coefficients do not matter. The minimum over monomials used in Prop. 5.2 was found by exhaustive enumeration.

**Proposition 7.5 (isolated components are generic).** There is a proper algebraic hypersurface $D\subset H^{2,2}_{prim}(X_{F_0})$ such that, for every rational $\lambda$ with $\lambda_{prim}\notin D$, $NL_\lambda$ is a reduced isolated point in moduli.

*Proof.*
1. The condition $\mathrm{rk}(P)=426$ is Zariski open in $P$.
2. It is nonempty: for general linear $\ell$, multiplication by $\ell^{12}$ is bijective $R_6\to R_{18}$, by the strong Lefschetz property of $\mathbb C[x]/(x_i^5)$ (Stanley, Watanabe).
3. Rational classes are Zariski dense in $H^{2,2}_{prim}$, because $\mathrm{Hdg}^2(X_{F_0})\otimes\mathbb C=H^{2,2}$. $\square$

**The honest list (rung (d)).** For Hodge classes on sextic fourfolds, the components of the Hodge locus fall into three groups.

*(i) HC holds along the whole component.*
* Components of codimension $\le19$ not contained in $E$; these are plane loci (Theorem C).
* Complete-intersection components (Cor. 7.2).
* Isolated components at Fermat-type points (Prop. 7.5). There HC is HC at a single point, known for the Fermat sextic (`docs/02`).

*(ii) The tangent-space method fails.*
* Fake planes (Cor. 5.4). The class is algebraic at $F_0$, but I do not know the true codimension of the components through $F_0$, nor a cycle at their general points.

*(iii) No cycle is known to me at the general point.* Take the non-standard types of Table 2 with $\mathrm{sym}=1$.
* For $\alpha=(1,2,3,4,4,4)$, $W_\alpha$ stays Hodge along $\mathcal F_1=\{\sum_ix_i^6+b\,x_0^3x_2^3=0\}$.
* For $\alpha=(1,3,3,3,4,4)$, $W_\alpha$ stays Hodge along $\mathcal F_2=\{\sum_ix_i^6+b\,x_0^2x_4^2x_5^2=0\}$.
* These classes are algebraic at $b=0$, but no algebraic representative for general $b$ is constructed here. More generally, for every non-standard type, VHC along the component through $F_0$ is open to me, whatever its dimension (between the "sym" and "$\dim T$" columns).

## 8. GAPS

* **(G0) Top target (a): no argument.** At the Fermat point, a general rational class has an isolated Hodge locus (Prop. 7.5). At an isolated component there is nothing to propagate. A cycle has to be produced at the point itself, and the Jacobian-ring data there (a single nondegenerate quadratic form) say nothing about which cycle. So $\mathrm{HC}$ for all sextic fourfolds contains the special-point problem of `docs/03` (C3) in full, and none of the methods here touches it.

* **(G1) Infinitesimal plane bound (§4).** *Statement:* for every smooth sextic $F$ and every $0\ne P\in R^F_{12}$, $\mathrm{rk}(P)\le19$ implies $\dim\mathrm{Ann}(P)_1\ge3$.
  * *Why it is needed:* it is the only missing step in Theorem B, i.e. in rung (b) with $c=19$ for all components.
  * *What is proved:* (G1) holds on the dense open set $V$ (Theorem 5.3). The bound $\mathrm{rk}\ge8$ holds everywhere (Prop. 6.2).
  * *Why I cannot prove it:* Macaulay–Gotzmann bounds combined with smoothness provably stop at $8$ (§6). The Fermat degeneration works only near $F_0$, and $E=U\setminus V$ is not explicit. What is missing is a classification of the Artinian Gorenstein quotients $S/I$ of socle degree $12$ with $I\supseteq J_F$ and $h(6)\le19$. Equivalently, one needs to classify the degree-$12$ forms in six variables that are apolar to $J_F$ and have middle catalecticant rank $\le19$. There is no structure theorem for Gorenstein algebras in codimension $4$–$6$.
  * *Weakenings that would suffice:* $\operatorname{codim}E\ge20$ would already make Theorem B unconditional. (G1) itself cannot be strengthened to "$\Pi\subset X$", by Cor. 5.4.

* **(G2) No components of codimension $20$–$31$.** Expected: the next locus after planes is that of quadric surfaces, of codimension $32$. Not proved. At $F_0$, the vertex argument shows that $\mathrm{rk}(P)\le31$ forces every vertex of the Newton polytope to be of plane type. I could not complete the analysis of edges and higher faces.

* **(G3) VHC along non-linear components through the Fermat point.** This covers the non-standard rows of Table 2, and in particular the explicit families $\mathcal F_1$ and $\mathcal F_2$ of §7. An expected but unchecked reduction: $\mathcal F_1$ is a Thom–Sebastiani sum of a binary sextic and the Fermat quaternary, so the Shioda–Katsura construction dominates it by (a blow-up of) $C_b\times X^3_6$, where $C_b=\{x_0^6+bx_0^3x_2^3+x_2^6+u^6=0\}$. This would reduce HC for $X_b$ to the algebraicity of Hodge classes in $H^1(C_b)\otimes H^3(X^3_6)$. I have not verified the details or the literature.

* **(G4) Fake planes.** I do not know the true codimension of the components through $F_0$ of fake linear cycles, nor whether these classes stay algebraic along them (Cor. 5.4 only shows the germs are singular).

* **(G5) Literature.** I could not read [Mo], [Vi1], [Vi2], [DV], [Ot1], [Ot2], [Da], [Kl] or [BFLV]. Every **[lit]** statement should be checked, in particular:
  * whether [Mo] already contains the uniqueness part of Theorem C;
  * the exact range of degrees in [DV];
  * whether [Ot1] covers $d=6$ (I believe it requires $d\gg0$).

## 9. Checklist (`docs/03` §3.4)

* **Where rational coefficients are essential.** Theorems A, B and C conclude $\lambda\in\mathbb Q[\Pi]\oplus\mathbb Qh^2$. The coefficients come from proportionality, $\lambda_{prim}=c[\Pi]_{prim}$, and from the primitive projection, which divides by $h^4=6$. For integral $\lambda$ they need not be integers. The lattice $\langle[\Pi],h^2\rangle$ has Gram matrix $\begin{pmatrix}21&1\\1&6\end{pmatrix}$ and discriminant $125$, and $([\Pi]+4h^2)/5$ pairs integrally with both $[\Pi]$ and $h^2$. Whether this class lies in $H^4(X,\mathbb Z)$, and if so whether it is the class of an integral cycle, is not addressed. So nothing here yields an integral statement. The integral HC is open even for the Fermat sextic [BFLV] **[lit]**, and is not claimed.
* **Where projectivity is essential.** The cycle-producing step is Theorem A. Three linear forms of the homogeneous coordinate ring annihilating $P_\lambda$ cut out a linear subspace $\Pi\subset\mathbb P^5$, and the class is identified with $[\Pi]$. Both Griffiths' residues and the graded ring $S$ require the embedding $X\subset\mathbb P^5$. The argument has no analogue on a compact Kähler manifold, so it cannot "prove" the Kähler HC, which is false. [CDK] is used only to read the local statements globally.
* **False-variant test.**
  * Integral HC: not implied, as above.
  * Kähler HC: not applicable.
  * Hodge's original generalized conjecture: not used.
  * Demailly-type positivity: not used.
* **Consistency checks.**
  * Theorem C recovers the uniqueness through the Fermat point of [DV] for $(4,6)$.
  * Cor. 5.4 is consistent with their non-reducedness result.
  * Cor. 7.2 matches parameter counts.
  * Prop. 3.1 was checked numerically at $F_0$ (§3).
  * The standard characters give $1001$, matching [BFLV].
* **Checklist items 1–4.** The classes of Theorems A–C are algebraic, hence absolute. VHC is proved only along the components of Theorem C and Cor. 7.2. Special points are untouched.

## 10. References

* [AGV] V. Arnold, S. Gusein-Zade, A. Varchenko, *Singularities of Differentiable Maps I*, §11 (splitting lemma).
* [BH] W. Bruns, J. Herzog, *Cohen–Macaulay Rings*, §4.2–4.3 (Macaulay, Gotzmann).
* [BV] A. Braun, R. Valandro, $G_4$ flux, algebraic cycles and complex structure moduli stabilization, JHEP 01 (2021) 207.
* [BFLV] A. Braun, H. Fortin, D. Lopez Garcia, R. Villaflor Loyola, More on $G$-flux and general Hodge cycles on the Fermat sextic, JHEP (2024), arXiv:2401.00470 **[lit]**.
* [CDK] E. Cattani, P. Deligne, A. Kaplan, On the locus of Hodge classes, JAMS 8 (1995).
* [CG] J. Carlson, P. Griffiths, Infinitesimal variations of Hodge structure and the global Torelli problem, in *Géométrie algébrique Angers 1979* (1980). [CGGH] Carlson–Green–Griffiths–Harris, Compositio Math. 50 (1983).
* [Da] A. Dan, Noether–Lefschetz locus and a special case of the variational Hodge conjecture: using elementary techniques, arXiv:1404.7519 **[lit]**.
* [DV] J. Duque Franco, R. Villaflor Loyola, On fake linear cycles inside Fermat varieties, Algebra Number Theory 17 (2023), arXiv:2112.14818 **[lit]**.
* [Go] G. Gotzmann, Math. Z. 158 (1978).
* [Gr] P. Griffiths, On the periods of certain rational integrals I, II, Ann. of Math. 90 (1969).
* [GVW] S. Gukov, C. Vafa, E. Witten, CFT's from Calabi–Yau four-folds, Nucl. Phys. B 584 (2000).
* [Kl] R. Kloosterman, Variational Hodge conjecture for complete intersections on hypersurfaces in projective space, Rend. Sem. Mat. Univ. Padova 148 (2022); Hodge loci associated with linear subspaces intersecting in codimension one, Math. Nachr. 298 (2025) **[lit]**.
* [Mo] H. Movasati, Gauss–Manin connection in disguise: Noether–Lefschetz and Hodge loci, Asian J. Math. 21 (2017), arXiv:1411.1766 **[lit]**.
* [Ot1] A. Otwinowska, Composantes de petite codimension du lieu de Noether–Lefschetz, J. Algebraic Geom. 12 (2003) **[lit]**. [Ot2] Sur la fonction de Hilbert des algèbres graduées de dimension 0, J. reine angew. Math. 545 (2002) **[lit]**.
* [Vi1] R. Villaflor Loyola, Small codimension components of the Hodge locus containing the Fermat variety, Commun. Contemp. Math. (2022), arXiv:2001.01019 **[lit]**. [Vi2] Periods of complete intersection algebraic cycles, manuscripta math. (2022) **[lit]**.
* Green (J. Diff. Geom. 27, 29), Voisin (Math. Ann. 280; Comment. Math. Helv. 64): the surface case, for comparison only.

## 11. Claimed results

| label | one-line statement | status |
|---|---|---|
| Facts 1.1 | Griffiths residues; IVHS = multiplication in $R$ | known [Gr, CG] |
| Prop. 1.2 | $NL_\lambda=\mathrm{Crit}(\Phi_\lambda)$; Hessian $=2\,\mathrm{Res}(ABP_\lambda)$ | known in substance [GVW, BV]; proof here |
| Cor. 1.3 | $T\,NL_\lambda=\mathrm{Ann}(P_\lambda)_6$; $\operatorname{codim}Z\ge\mathrm{rk}$ | known [CGGH]; proof here |
| Lemma 2.1 | $\mathrm{Ann}(P_{[\Pi]})=(x_0,x_1,x_2,G_0,G_1,G_2)$; $\mathrm{rk}=19$; $\operatorname{codim}\mathcal P=19$ | known in substance [Vi2, Mo]; self-contained proof here |
| Prop. 3.1 | $h_P(1)\ge3$; equality iff Jacobian plane, then $h_P=[5]_t^3$ | proved here (form believed new) |
| Prop. 3.2 | Jacobian planes not in $X$: locus $\mathcal W$ of codim $\ge34$; normal form | proved here (believed new) |
| Theorem A | plane-like Hodge classes lie in $\mathbb Q[\Pi]\oplus\mathbb Qh^2$, or $X\in\mathcal W$ | proved here (believed new) |
| Lemma 4.1 | plane-type classes specialize along a component | proved here (standard) |
| Cor. 4.2 | plane-like components of codim $\le33$ are plane loci; HC along them | proved here |
| Theorem B | every component has codim $\ge19$; codim $\le19$ means plane locus; HC | proved here conditionally on (G1) |
| Lemma 5.1 | limits of Gorenstein annihilators preserve Hilbert functions | proved here |
| Prop. 5.2 | Fermat point: $\mathrm{rk}\ge19$, and $\mathrm{rk}=19\Rightarrow h_P=[5]_t^3$ | inequality known [Mo]; equality case proved here |
| Theorem 5.3 | (G1) holds on a dense Zariski-open $V\ni F_0$ | proved here (believed new) |
| Theorem C | components $\not\subseteq E$ of codim $\le19$ are plane loci; HC along them | proved here (through $F_0$: cf. [DV]) |
| Cor. 5.4 | fake planes in $V$: the Hodge-locus germ is not smooth | proved here (weaker than [DV] at $F_0$) |
| Lemma 6.1 | no maximal Macaulay growth in degrees $5$–$11$ | proved here (Green-type, elementary) |
| Prop. 6.2 | every component has codim $\ge8$; the method cannot give more | proved here |
| Prop. 7.1 | Hessian-rank criterion for VHC | folklore; proof here |
| Cor. 7.2 | CI surface classes: $NL$ = CI locus; codims $19,\dots,141$ | known [Da, Kl]; proof here |
| Lemma 7.3 | symmetric deformations keep invariant $(2,2)$-classes Hodge | standard; proof here |
| Prop. 7.4 | exact tangent codims for Fermat character classes (Table 2) | proved here (computation; believed new) |
| Prop. 7.5 | at $F_0$, generic rational classes have isolated reduced $NL_\lambda$ | proved here (elementary) |
