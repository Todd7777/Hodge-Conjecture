# Attack 8: p-adic methods over number fields

**Status (read this first).** The top target of the ladder is **not proved**. That target says: an absolute Hodge class on a variety over a number field, with Galois-invariant $p$-adic realization, is algebraic. It contains HC for all abelian varieties, because by Deligne their Hodge classes are absolute. What this file proves:

1. **Theorem A** (§2, a conditional reduction with complete proof). It isolates exactly what the chain "reduce mod $p$ → Tate conjecture → lift with BEK" needs. Besides the Tate conjecture (T) and algebraization, it needs two further inputs:
   - a rationality statement (Rat$_v$), which is the crystalline form of Milne's rationality conjecture;
   - homological = numerical equivalence (D) on the special fibre.

   Proposition 3.1 (known) shows that (Rat$_v$) cannot be extracted from $p$-adic data: the $\mathbb Q_p$-coefficient analogue is false.
2. **Theorem B** (§4, conditional, believed new in this form). Assume hypothesis (Cont): algebraic $K$-theory of a smooth projective $W(k)$-scheme is continuous with finite coefficients. This is the proper-scheme analogue of a theorem of Clausen–Mathew–Morrow for complete noetherian rings. Then every class that Bloch–Esnault–Kerz lift to the formal scheme is, up to a nonzero integer multiple, *numerically* equivalent on the special fibre to the specialization of a class from the generic fibre. So BEK + (Cont) yields the algebraization half of the $p$-adic variational Hodge conjecture modulo numerical equivalence.
3. **Theorem C** (§5, conditional, believed new in this form; the positivity trick is standard). Assume (Cont), and a Lefschetz-type condition (Pos$_v$) on the special fibre. Let $\alpha$ be a Hodge class on a variety over a number field whose crystalline specialization at one good unramified prime $p>d+6$ is algebraic. Then $\alpha$ is algebraic. Hodge–Riemann positivity in characteristic $0$ replaces standard conjecture D.
4. **Corollaries C.1–C.2.** For abelian varieties with supersingular good reduction, (T), (D) and (Pos$_v$) hold unconditionally (Proposition 5.2). So modulo (Cont), a Hodge class satisfying (Rat$_v$) at one such prime is algebraic, and conversely an algebraic class satisfies (Rat$_v$) at all but finitely many such primes. CM abelian varieties have infinitely many such primes. Consequently, modulo (Cont), **Milne's rationality conjecture (its crystalline part at one supersingular prime) implies HC for CM abelian varieties.** The converse implication is Milne's.
5. **§6** records the reduction asked for in ladder item (c) (Voisin 2007, known). It adds a proved necessary condition: every $p$-adic method is confined to Hodge classes whose de Rham component is $\bar{\mathbb Q}$-rational.

No unconditional new case of HC, or of the $p$-adic variational Hodge conjecture, is proved. The ladder item "codimension-2 classes when $H^2(X,\mathcal O)=0$" is not achieved. §4.4 explains that this hypothesis controls the wrong obstruction group and gives the correct analogue.

**Access caveat.** arXiv, journal sites and author home pages were unreachable (DNS-blocked), and the shared web-search budget ran out partway through. Every external input is stated below in the form I use it, with a flag recording how far that form could be checked (search-engine excerpts only).

## 1. Notation and inputs

**Notation.**
- $F$ is a number field and $X/F$ is smooth projective of dimension $d$. The codimension $r$ satisfies $2r\le d$. This suffices for HC by hard Lefschetz, docs/01 §1.2.3.
- Fix embeddings $\sigma:\bar F\hookrightarrow\mathbb C$ and, for each finite place $v\mid p$, $\iota_v:\bar F\hookrightarrow\bar F_v$.
- A place $v$ is a **good unramified place** if $F_v/\mathbb Q_p$ is unramified, so that $\mathcal O_v=W(k)$ with $k=k(v)$ finite, and $X_{F_v}$ extends to a smooth projective $\mathcal X/W(k)$.
- Put $X_n=\mathcal X\otimes W_n(k)$, so $X_1$ is the special fibre. Put $K_0=W(k)[1/p]$, and $K_0'=W(k')[1/p]$ for finite $k'/k$.
- $H^i_{\rm crys}(X_1\otimes k')_{\mathbb Q}:=H^i_{\rm crys}(X_1\otimes k'/W(k'))\otimes\mathbb Q$, with its $\sigma$-semilinear Frobenius $\varphi$.
- $T^r(X_1\otimes k'):=\{x\in H^{2r}_{\rm crys}(X_1\otimes k')_{\mathbb Q}:\varphi x=p^rx\}$, a $\mathbb Q_p$-vector space.

For $\alpha\in\mathrm{Hdg}^r(X_{\sigma,\mathbb C})$, write $\alpha_B\in H^{2r}(X_\sigma(\mathbb C),\mathbb Q(r))$, $\alpha_{dR}\in H^{2r}_{dR}(X_{\sigma,\mathbb C})$ and $\alpha_\ell$ for its realizations, the last when $\alpha$ is absolute Hodge.
- $\alpha$ is **de Rham-rational over $F$** if $\alpha_{dR}\in H^{2r}_{dR}(X/F)$.
- If so, its **crystalline specialization** at $v$ is $\alpha_{\rm crys}:=\mathrm{BO}(\iota_v\alpha_{dR})\in H^{2r}_{\rm crys}(X_1)_{\mathbb Q}$. Here $\mathrm{BO}$ is the isomorphism (I1).
- $\alpha_{\rm crys}\in F^r$, because the Hodge filtration is defined over $F$.

**Inputs.** Flags: **[v]** the statement was confirmed from search excerpts of the source; **[s]** standard textbook fact; **[u]** the exact form was not verified against the source.

- **(I1) [s]** Berthelot–Ogus [BO]. There is an isomorphism $H^*_{\rm crys}(X_1/W)\otimes\mathbb Q\cong H^*_{dR}(X_{F_v}/F_v)$ compatible with:
  - cup product and trace;
  - Chern classes of vector bundles on $\mathcal X$. For $c_1$ this is [BO, Prop. 3.4] **[v]**; in general it follows by the splitting principle.

  Also, for a cycle $z$ on $X_1\otimes k'$ one has $\varphi(c_{\rm crys}(z))=p^rc_{\rm crys}(z)$, and crystalline cohomology $\otimes K_0'$ is a Weil cohomology [GM]. For a line bundle this is elementary: $F^*M\cong M^{\otimes p}$.
- **(I2) [v; bound u]** BEK [BEK]. Let $\mathcal X/W(k)$ be smooth projective, $k$ perfect, $p>d+6$, and $\xi_1\in K_0(X_1)_{\mathbb Q}$. Then $ch_{\rm crys}(\xi_1)\in\bigoplus_iF^iH^{2i}_{dR}(X_{F_v})$ iff, "rationally, $\xi_1$ lifts to a formal pro-class in $K$-theory". By Lemma 4.1 the only non-vacuous reading is the following:
  - some $N\xi_1$, with $N\ge1$, is the image of an element of $\pi_0K^{\rm cont}(\mathcal X)$, where $K^{\rm cont}(\mathcal X):=\mathrm{holim}_nK(X_n)$;
  - equivalently, $N\xi_1$ is the image of an element of $\varprojlim_nK_0(X_n)$, by the Milnor sequence.

  The bound $p>d+6$ appears in Thm. 11.1 of the authors' final preprint; I could not check the published numbering. Antieau–Mathew–Morrow–Nikolaus [AMMN] generalize the result, and I could not check whether they relax the bound.
- **(I3) [v]** Clausen–Mathew–Morrow [CMM, Thm. 5.5 / Thm. F]. If $R$ is noetherian and $I$-adically complete, and $R/p$ is $F$-finite, then $K(R)\to\lim_nK(R/I^n)$ is a $p$-adic equivalence. The authors remark that, for a smooth proper scheme over a complete local ring, their methods do not let them compare its $K$-theory with that of its truncations; they are "essentially limited to the affine case".
- **(I4) [s]** Crystalline comparison (Fontaine–Messing, Faltings, Tsuji; compatibility with cycle classes by Nizioł [Ni] **[u]**). For $V=H^{2r}_{et}(X_{\bar F_v},\mathbb Q_p(r))$, Fontaine's formula $V^{G}=(\mathrm{Fil}^0D_{\rm crys}V)^{\varphi=1}$ gives a canonical isomorphism
  $$V^{G_{F_v}}\xrightarrow{\ \sim\ }T^r(X_1)\cap F^rH^{2r}_{dR}(X_{F_v}),$$
  which sends étale cycle classes to crystalline ones.
- **(I5) [v]** Blasius [Bl]: Hodge classes on abelian varieties over number fields are *de Rham*. That is, the isomorphism of (I4) sends $\alpha_p$ to $\alpha_{\rm crys}$.
- **(I6) [s]** Deligne [De]: Hodge classes on abelian varieties are absolute Hodge. If $\alpha$ is absolute Hodge on $X/F$, there is a finite $F'/F$ such that $\alpha_{dR}\in H_{dR}(X/F')$ and every $\alpha_\ell$ is $G_{F'}$-invariant.
- **(I7) [s]** Standard tools:
  - the Hodge–Riemann bilinear relations;
  - Hilbert schemes;
  - Riemann–Roch: $ch:K_0\otimes\mathbb Q\xrightarrow{\sim}CH^*_{\mathbb Q}$, and HRR, $\chi(Y,E)=\int_Ych(E)\,td(Y)$, for $Y$ smooth projective over a field [Fu, Ch. 15];
  - specialization of cycles and its compatibility with Chern classes [Fu, Ch. 20];
  - $K_{-1}(Y)=0$ for $Y$ regular, and Zariski descent for $K$ [TT];
  - Goodwillie's theorem [Go].
- **(I8) [v]** Lazda–Pál [LP]: the crystalline variational Tate conjecture fails for line bundles with $\mathbb Q_p$-coefficients, with examples from elliptic curves.
- **(I9) [v]** Milne's **rationality conjecture** [Mi1]. Let $A/\mathbb Q^{al}$ have CM, or more generally good reduction $A_0$ over $\mathbb F=\bar{\mathbb F}_p$. Then the product of the specialization to $A_0$ of any Hodge class on $A$ with any Lefschetz class on $A_0$ of complementary dimension lies in $\mathbb Q$.
  - HC for CM abelian varieties implies it [Mi1].
  - It is listed as open in [Mi3] (2025).
  - Milne's specialization uses $\mathbb A_f^p\times\mathbb Q_p$-coefficients, with the $p$-part crystalline; I assume that its $p$-part is $\alpha_{\rm crys}$ as defined here **[u]**. This is consistent with (I5).
- **(I10) [v]** Voisin [Vo, Prop. 0.2]: if HC holds for (weakly) absolute Hodge classes on varieties defined over $\bar{\mathbb Q}$, then it holds for (weakly) absolute Hodge classes on all smooth projective complex varieties.
- **(I11) [v; numbering u]** Berthelot–Ogus: a line bundle $L_1$ on $X_1$ lifts to $\mathrm{Pic}(\mathcal X)[1/p]$ iff $c_1^{\rm crys}(L_1)\in F^1$. Morrow [Mo1] proves the characteristic-$p$ variational Tate conjecture for divisors, and an infinitesimal version in higher codimension.

The task text also mentions work of Emerton–Kisin on $p$-adic variational Hodge. I could not locate it before the search budget ran out, and nothing below uses it.

## 2. Reduction modulo $p$ (ladder item (a))

**Definition 2.0.** Let $\alpha$ be de Rham-rational over $F$ and $v$ a good unramified place. We consider the following hypotheses, where "all $k'$" means all finite extensions $k'/k$.

- **(dR$_v$)** The isomorphism of (I4) sends $\alpha_p$ to $\alpha_{\rm crys}$.
- **(T$_v$)** For all $k'$, $T^r(X_1\otimes k')$ is spanned over $\mathbb Q_p$ by crystalline classes of cycles on $X_1\otimes k'$ (the crystalline Tate conjecture in codimension $r$).
- **(D$_v$)** For all $k'$, every numerically trivial $u\in CH^r(X_1\otimes k')_{\mathbb Q}$ has $c_{\rm crys}(u)=0$.
- **(Rat$_v$)** For all $k'$ and all $w\in CH^{d-r}(X_1\otimes k')_{\mathbb Q}$, $\int\alpha_{\rm crys}\cdot c_{\rm crys}(w)\in\mathbb Q$.
- **(pVHC$_v$)** For all $k'$: if $z_1\in CH^r(X_1\otimes k')_{\mathbb Q}$ has $c_{\rm crys}(z_1)\in F^r$, then there is $Z\in CH^r(X_{K_0'})_{\mathbb Q}$ with $\mathrm{BO}(c_{dR}(Z))=c_{\rm crys}(z_1)$.

**Remark 2.0.1 (numerical triviality is geometric).** Let $u\in CH^r(X_1\otimes k')_{\mathbb Q}$ be numerically trivial (against cycles over $k'$), and let $w$ be a cycle on $X_1\otimes k''$, where $k''/k'$ is finite of degree $m$ with Galois group $\Gamma$. Put $\pi:X_1\otimes k''\to X_1\otimes k'$. Then $c(\pi_*w)=\sum_{\gamma\in\Gamma}\gamma\,c(w)$. The class $c(u)$ is $\Gamma$-invariant and $\int c(u)c(w)\in\mathbb Q$. Hence
$$0=\int c(u)\,c(\pi_*w)=\sum_{\gamma\in\Gamma}\gamma\Big(\int c(u)c(w)\Big)=m\int c(u)c(w),$$
so $u$ is numerically trivial against all cycles over $\bar k$.

**Lemma 2.1 (Frobenius invariance).** Let $\alpha$ be de Rham-rational over $F$, and suppose (dR$_v$) holds and $\alpha_p$ is $G_{F_v}$-invariant. Then $\alpha_{\rm crys}\in T^r(X_1)\cap F^r$.

*Proof.* $\alpha_p\in V^{G_{F_v}}$. By (I4) and (dR$_v$), its image under the isomorphism of (I4) is $\alpha_{\rm crys}$, and that image lies in $T^r(X_1)\cap F^r$. $\square$

**Lemma 2.2 (rigidity of cycle classes).** Let $\Omega\supseteq\bar F$ be algebraically closed, and $Z\in Z^r(X_\Omega)_{\mathbb Q}$. Then there is $Z'\in Z^r(X_{\bar F})_{\mathbb Q}$ with $c_{dR}(Z'_\Omega)=c_{dR}(Z)$ in $H^{2r}_{dR}(X/\bar F)\otimes_{\bar F}\Omega$.

*Proof.* By linearity we may take $Z$ integral, with Hilbert polynomial $P$ for a fixed embedding $X\subset\mathbb P^N_F$. Then $Z$ is a point $h\in\mathrm{Hilb}^P_{X_{\bar F}}(\Omega)$.

- Let $H$ be an irreducible component of $(\mathrm{Hilb}^P_{X_{\bar F}})_{\rm red}$ through $h$. Since $\bar F$ is algebraically closed, $H$ is geometrically irreducible.
- Let $\nu:\tilde H\to H$ be a resolution of singularities. Choose $\tilde h\in\tilde H(\Omega)$ over $h$, which exists because $\nu$ is proper surjective and $\Omega$ is algebraically closed. Choose $\tilde h'\in\tilde H(\bar F)$.
- Let $\mathcal Z\subset X\times\tilde H$ be the pulled-back universal family; it is flat over $\tilde H$.

For any point $t$ of $\tilde H$ with values in an algebraically closed field, flatness gives $Li_t^*\mathcal O_{\mathcal Z}=\mathcal O_{\mathcal Z_t}$. Hence $i_t^*ch_r(\mathcal O_{\mathcal Z})=ch_r(\mathcal O_{\mathcal Z_t})=[\mathcal Z_t]_r$, the codimension-$r$ part of the fundamental cycle [Fu, Ex. 15.3.6]. Thus $[\mathcal Z_{\tilde h}]_r=Z$, and $Z':=[\mathcal Z_{\tilde h'}]_r$ is a cycle on $X_{\bar F}$.

To compare the two classes:
- Choose a countable algebraically closed subfield $\Omega_1\subseteq\Omega$ containing $\bar F$ and a field of definition of $\tilde h$, and an embedding $j:\Omega_1\hookrightarrow\mathbb C$.
- Both classes lie in $H_{dR}(X/\bar F)\otimes\Omega_1$, and $\otimes_{\Omega_1,j}\mathbb C$ is injective. After base change along $j$, they are the comparison images of the Betti classes $c_B([\mathcal Z_{j\tilde h}]_r)$ and $c_B([\mathcal Z_{j\tilde h'}]_r)$ on $X^j(\mathbb C)$.
- These Betti classes are $i_t^*c_B(ch_r\mathcal O_{\mathcal Z})$ for two points $t$ of the connected space $\tilde H^j(\mathbb C)$. Inclusions of fibres of a product over a path-connected base are homotopic, so the two classes agree. $\square$

**Corollary 2.3 (a necessary condition).** If $X$ is defined over $\bar{\mathbb Q}$ and $\alpha\in\mathrm{Hdg}^r(X_{\mathbb C})$ is algebraic, then $\alpha_{dR}\in H^{2r}_{dR}(X/\bar{\mathbb Q})$.

*Proof.* Apply Lemma 2.2 with $\Omega=\mathbb C$, and use that the Betti–de Rham comparison is injective and compatible with cycle classes. $\square$

**Lemma 2.4 (rationality).** Let $V$ be a finite-dimensional $\mathbb Q$-vector space, $V'$ a $\mathbb Q$-vector space, and $\langle\,,\rangle:V\times V'\to\mathbb Q$ a pairing with $V\hookrightarrow\mathrm{Hom}(V',\mathbb Q)$. Let $E\supseteq\mathbb Q$ be a field. Then:
- (a) $V\otimes E\to\mathrm{Hom}(V',E)$ is injective;
- (b) if $x\in V\otimes E$ satisfies $\langle x,v'\rangle\in\mathbb Q$ for all $v'\in V'$, then $x\in V$.

*Proof.* Let $v_1,\dots,v_m$ be a basis of $V$. By injectivity there are $v'_1,\dots,v'_m\in V'$ with $M=(\langle v_i,v'_j\rangle)\in GL_m(\mathbb Q)$. Write $x=\sum c_iv_i$ with $c_i\in E$. Then $(\langle x,v'_j\rangle)_j=cM$. If $x$ pairs to $0$, then $c=0$, which is (a). If all $\langle x,v'_j\rangle$ are rational, then $c=(\langle x,v'_j\rangle)_jM^{-1}\in\mathbb Q^m$, which is (b). $\square$

**Theorem A (what the reduction argument needs).** Let $\alpha\in\mathrm{Hdg}^r(X_{\sigma,\mathbb C})$, with $2r\le d$, be de Rham-rational over $F$. Let $v$ be a good unramified place with $p>d+6$.

- **(i) Lifting.** Suppose $\alpha_{\rm crys}=c_{\rm crys}(z_1)$ for some $z_1\in CH^r(X_1\otimes k')_{\mathbb Q}$, and (pVHC$_v$) holds for $z_1$. Then $\alpha$ is algebraic.
- **(ii) Specialization is algebraic.** Suppose $\alpha_p$ is $G_{F_v}$-invariant and (dR$_v$), (T$_v$), (D$_v$), (Rat$_v$) hold. Then $\alpha_{\rm crys}=c_{\rm crys}(z_1)$ for some $z_1\in CH^r(X_1)_{\mathbb Q}$.
- **(iii) Necessity.** Suppose $\alpha=c(Z)$ with $Z\in CH^r(X)_{\mathbb Q}$ defined over $F$. Then:
  - $\alpha_p$ is $G_F$-invariant, and (dR$_v$), (Rat$_v$) hold;
  - $\alpha_{\rm crys}=c_{\rm crys}(\sigma_vZ)$, where $\sigma_v$ is specialization [Fu, Ch. 20];
  - (pVHC$_v$) holds for $z_1=\sigma_vZ$.

Consequently, for an absolute Hodge class (made $G_F$-invariant and de Rham-rational over $F$ by enlarging $F$, (I6)), algebraicity follows from:
- (dR$_v$) — known for abelian varieties (I5);
- the two conjectures (T$_v$) and (D$_v$) on $X_1$ alone;
- (Rat$_v$);
- (pVHC$_v$).

Of these, (dR$_v$), (Rat$_v$) and the instance of (pVHC$_v$) used are necessary.

*Proof.* (i) (pVHC$_v$) gives $Z$ on $X_{K_0'}$ with $\mathrm{BO}(c_{dR}(Z))=\alpha_{\rm crys}$. Lemma 2.2, with $\Omega=\bar K_0'\supseteq\bar F$ via $\iota_v$, gives $Z'$ on $X_{\bar F}$ with $\iota_v(c_{dR}(Z'))=\iota_v(\alpha_{dR})$. Since $\iota_v$ is injective on $H_{dR}(X/\bar F)$, $c_{dR}(Z')=\alpha_{dR}$. Under the $\sigma$-comparison, $c_B(Z'_\sigma)$ and $\alpha_B$ become the same element of $H^{2r}_{dR}(X_{\sigma,\mathbb C})$, so they are equal.

(ii) By Lemma 2.1, $\alpha_{\rm crys}\in T^r(X_1)$. By (T$_v$) with $k'=k$, $\alpha_{\rm crys}$ lies in the $\mathbb Q_p$-span of the $\mathbb Q$-space $A\subset H^{2r}_{\rm crys}(X_1)_{\mathbb Q}$ of classes of cycles over $k$. Pair $A$ with $A'$, the analogous space in degree $2d-2r$:
- by (D$_v$) and Remark 2.0.1, $A\hookrightarrow\mathrm{Hom}(A',\mathbb Q)$;
- $A$ is finite-dimensional, since it embeds in the numerical group, which is finitely generated;
- by Lemma 2.4(a), the span is $A\otimes\mathbb Q_p$.

By (Rat$_v$) and Lemma 2.4(b), $\alpha_{\rm crys}\in A$.

(iii) Compatibility of the comparison isomorphisms with cycle classes and specialization (I1), (I4). Intersection numbers on $X_1$ are rational. $Z_{F_v}$ itself is the lift required by (pVHC$_v$). $\square$

**What Theorem A says about the top target.**
- An absolute Hodge class on a variety over a number field is automatically Galois-invariant for **every** $\ell$, after a finite extension (I6). So the hypothesis "Galois-invariant for one prime $p$" adds nothing, and the top target is equivalent to "absolute Hodge $\Rightarrow$ algebraic over number fields".
- Theorem A reduces this to (T$_v$), (D$_v$), (Rat$_v$) and (pVHC$_v$) at a single good unramified place, together with (dR$_v$).
- Using a density-one set of places does not help with (Rat$_v$). That condition concerns intersection numbers with cycles that exist only on the special fibre, and these cycles differ from place to place.
- (Rat$_v$) is the input easiest to overlook. The Tate conjecture only gives $\alpha_{\rm crys}\in A\otimes\mathbb Q_p$, and Proposition 3.1 shows that $p$-adic data cannot close the gap between $A\otimes\mathbb Q_p$ and $A$.
- §4 attacks (pVHC$_v$).

## 3. Rational coefficients are essential: the $\mathbb Q_p$-version fails

**Proposition 3.1 (known; cf. (I8), Serre–Tate).** Let $p>2$ and let $E_0/\mathbb F_p$ be an ordinary elliptic curve. There exist:
- elliptic curves $E,E'$ over $\mathbb Z_p$ lifting $E_0$, with $\mathrm{Hom}_{\bar{\mathbb Q}_p}(E,E')=0$;
- a class $x\in NS(E_0\times E_0)\otimes\mathbb Q_p$, for the special fibre of $X:=E\times E'$,

such that:
- $\varphi x=px$ and $x\in F^1H^2_{dR}(X_{\mathbb Q_p})$;
- $x\notin NS(X_1)_{\mathbb Q}$;
- $x\notin\mathbb Q_p\cdot c(NS(X_{\bar{\mathbb Q}_p}))$.

Hence "Frobenius-invariant, in $F^r$, and in the $\mathbb Q_p$-span of algebraic classes of $X_1$" does not imply that a class is a $\mathbb Q$-combination of cycle classes. In other words, via (I4), the Tate conjecture fails over $\mathbb Q_p$. In Theorem A, therefore, (Rat$_v$) cannot be deduced from these local properties alone. Any proof of it must use more, for instance the global Betti $\mathbb Q$-structure.

*Proof.* **The Dieudonné module.**
- $D:=H^1_{\rm crys}(E_0/\mathbb Z_p)$ is free of rank 2. Its Frobenius is $\mathbb Z_p$-linear (here $\sigma=\mathrm{id}$) and equals the action of the Frobenius endomorphism $\pi$, with characteristic polynomial $T^2-aT+p$, $p\nmid a$.
- The roots $\alpha_0\in\mathbb Z_p^\times$ and $\beta_0=p/\alpha_0$ are distinct mod $p$, so $D=\mathbb Z_pe_0\oplus\mathbb Z_pe_1$ with $\varphi e_0=\alpha_0e_0$ and $\varphi e_1=\beta_0e_1$.
- $\mathcal E:=\mathrm{End}(E_0)\otimes\mathbb Q=\mathbb Q(\pi)$ is imaginary quadratic and commutes with $\varphi$. So it acts diagonally, $f\mapsto(\iota f,\iota\bar f)$, for an embedding $\iota:\mathcal E\hookrightarrow\mathbb Q_p$. Then $\mathcal E\otimes\mathbb Q_p=\mathbb Q_p\times\mathbb Q_p$, acting by $(u_0,u_1)$ on $(e_0,e_1)$.

**The Hodge lines of lifts.**
- The canonical lift carries a lift $\tilde\pi$ of $\pi$. Then $\tilde\pi^*$ preserves the Hodge line and acts on it by a non-unit, because Frobenius kills differentials. So its Hodge line is $\mathbb Z_pe_1$, and the Hodge line of $E_0$ is $\bar e_1$.
- By Serre–Tate and Grothendieck–Messing ($p>2$), plus Grothendieck existence for the algebraization, the lifts of $E_0$ to $\mathbb Z_p$ correspond to the lines $\ell_y=\mathbb Z_p(ye_0+e_1)$ with $y\in p\mathbb Z_p$. Here $\ell_y=F^1H^1_{dR}(E_y/\mathbb Z_p)$ under BO.
- Choose $y=p$ and $y'=p\lambda$, where $\lambda\in\mathbb Z_p^\times$ is not of the form $\iota(\bar f)/\iota(f)$ with $f\in\mathcal E^\times$; such $\lambda$ exist because that set is countable. Put $E=E_y$ and $E'=E_{y'}$.

**The class $x$ is in $F^1$.**
- Under Künneth and Poincaré duality, $F^1\cap\big(H^1(E)\otimes H^1(E')\big)$ corresponds to the maps $H^1(E')\to H^1(E)$ that send $F^1$ into $F^1$. Indeed, $(H^1\otimes H^1)/F^1=(H^1/F^1)\otimes(H^1/F^1)$, and in a 2-dimensional symplectic space the Hodge line is its own orthogonal.
- Divisor classes in $\mathrm{End}(E_0)\subset NS(E_0\times E_0)$ map to $f^*$, up to sign.
- $u=(u_0,u_1)$ sends $\ell_{y'}$ into $\ell_y\otimes\mathbb Q_p$ iff $u_0y'=u_1y$. So $u=(y,y')$ works, and the corresponding $x$ lies in $F^1$.
- $\varphi x=px$, because $x\in NS\otimes\mathbb Q_p$.

**The class $x$ is not rational.**
- $u\in\mathcal E$ would force $\iota(\bar f)/\iota(f)=y'/y=\lambda$, which is excluded; and for $f\neq0$ the same equation is the condition for $f$ to preserve the filtrations. So no nonzero $f\in\mathcal E$ preserves the Hodge filtrations.
- Homomorphisms of abelian schemes preserve Hodge filtrations, and reduction $\mathrm{Hom}(E,E')\hookrightarrow\mathrm{End}(E_0)$ is injective (rigidity). So $\mathrm{Hom}(E,E')=0$. The same holds over the integers of every finite extension of $\mathbb Q_p$, since by Néron extension homomorphisms over $\bar{\mathbb Q}_p$ come from such integers.
- Hence $NS(X_{\bar{\mathbb Q}_p})_{\mathbb Q}=\mathbb Qh_1+\mathbb Qh_2$. These classes lie in $H^2\otimes H^0+H^0\otimes H^2$, while $x\neq0$ lies in $H^1\otimes H^1$.
- Finally $x\notin NS(X_1)_{\mathbb Q}$, because $u\notin\mathcal E$ and $NS(X_1)_{\mathbb Q}\otimes\mathbb Q_p\hookrightarrow H^2_{\rm crys}$. This injectivity is (D) for divisors plus Lemma 2.4(a). $\square$

## 4. Algebraization (ladder item (b)): Theorem B

**Lemma 4.1 (the meaning of the BEK lift).** $K_0(X_n)_{\mathbb Q}\to K_0(X_1)_{\mathbb Q}$ is an isomorphism for every $n$. Hence $\varprojlim_n\big(K_0(X_n)\otimes\mathbb Q\big)=K_0(X_1)_{\mathbb Q}$. So the statement in (I2) is non-vacuous only for lifts in $\big(\varprojlim_nK_0(X_n)\big)\otimes\mathbb Q$, equivalently in $\pi_0K^{\rm cont}(\mathcal X)\otimes\mathbb Q$.

*Proof.*
- On an affine open $\mathrm{Spec}A$, the relative term $K(A,pA)$ is rationally $HC(A_{\mathbb Q},pA_{\mathbb Q})[1]=0$, by Goodwillie [Go] ($pA$ is nilpotent and $A_{\mathbb Q}=0$).
- $\mathrm{fib}(K(X_n)\to K(X_1))$ is a Zariski sheaf of spectra on $|X_1|$ [TT] whose sections on affines are rationally trivial.
- $|X_1|$ has finite Krull dimension, so by the descent spectral sequence the fibre is rationally trivial. $\square$

**Hypothesis (Cont$_0$) for $\mathcal X$.** For every $m\ge1$, the map $\pi_0\big(K(\mathcal X)/p^m\big)\to\pi_0\big(K^{\rm cont}(\mathcal X)/p^m\big)$ is surjective.
- It follows from the full continuity statement $K(\mathcal X)/p\simeq\mathrm{holim}_nK(X_n)/p$.
- That statement is the projective-scheme analogue of (I3). (I3) proves it for $p$-adically complete noetherian rings with $F$-finite reduction. For proper schemes it is not covered by (I3), and I know no proof.
- Note that $\mathrm{Perf}(\mathcal X)\simeq\lim_n\mathrm{Perf}(X_n)$ holds by Grothendieck existence for perfect complexes (Lurie, *SAG*, §8.5 **[u]**). (Cont) is therefore the assertion that $K$-theory commutes, $p$-adically, with this particular limit.
- Only the consequence (App) below, for the given class, is used.

**Lemma 4.2.** Let $Y$ be smooth projective over a field, and let $\mathcal N(Y):=K_0(Y)/\mathrm{rad}(\chi)$, where $\chi(\xi,\zeta)=\chi(Y,\xi\otimes^L\zeta)$. Then $\mathcal N(Y)$ is a finitely generated free abelian group. Moreover, $\xi\in\mathrm{rad}(\chi)\otimes\mathbb Q$ iff every graded piece of $ch(\xi)$ is numerically trivial.

*Proof.* By HRR (I7), $\chi(\xi,\zeta)=\int ch(\xi)ch(\zeta)td(Y)$, computed in $\ell$-adic cohomology.
- The $\mathbb Q_\ell$-span of $\{ch_\ell(\zeta)\,td_\ell(Y)\}$ is finite-dimensional; pick $\zeta_1,\dots,\zeta_m$ whose classes span it.
- Then $\xi\mapsto(\chi(\xi,\zeta_j))_j\in\mathbb Z^m$ has kernel exactly $\mathrm{rad}(\chi)$. Indeed, every $ch(\zeta)td$ is a $\mathbb Q_\ell$-combination of the $ch(\zeta_j)td$.
- So $\mathcal N(Y)\hookrightarrow\mathbb Z^m$.
- For the second claim: $td$ is a unit of $CH^*_{\mathbb Q}$ and $ch$ is bijective, so $\int ch(\xi)\,c=0$ for all $c\in CH^*_{\mathbb Q}$ iff $\chi(\xi,\cdot)=0$ rationally. $\square$

**Theorem B (formal lifts are algebraic up to numerical equivalence, given (Cont)).** Let $k$ be perfect and $\mathcal X/W(k)$ smooth projective. Let $\xi_1\in K_0(X_1)$, and suppose $N\xi_1$ is the image of some $\hat\xi\in\pi_0K^{\rm cont}(\mathcal X)$ for some $N\ge1$. This holds, by (I2) and Lemma 4.1, whenever $p>d+6$ and $ch_{\rm crys}(\xi_1)\in\bigoplus_iF^i$. Assume (Cont$_0$) for $\mathcal X$. Then:
- **(App)** for every $m$, $N\xi_1\in\mathrm{res}(K_0(\mathcal X))+p^mK_0(X_1)$;
- there are an integer $N'\ge1$ prime to $p$ and $\eta\in K_0(\mathcal X)$ such that $N'N\xi_1-\eta|_{X_1}\in\mathrm{rad}(\chi)$.

Equivalently, every graded piece of $N'N\,ch(\xi_1)-ch(\eta|_{X_1})$ is numerically trivial on $X_1$. Here $ch(\eta|_{X_1})$ is the specialization of $ch(\eta_{K_0})\in CH^*(X_{K_0})_{\mathbb Q}$ [Fu, Ch. 20].

*Proof.* **(App).**
- Since $K_{-1}=0$ for regular schemes (I7), $\pi_0(K(\mathcal X)/p^m)=K_0(\mathcal X)/p^m$ and $\pi_0(K(X_1)/p^m)=K_0(X_1)/p^m$.
- Let $\kappa:K(\mathcal X)\to K^{\rm cont}(\mathcal X)$ be the canonical map and $\mathrm{pr}_1:K^{\rm cont}(\mathcal X)\to K(X_1)$ the projection. Then $\mathrm{pr}_1\circ\kappa=\mathrm{res}$.
- By (Cont$_0$), $\hat\xi\bmod p^m=\kappa_*(e\bmod p^m)$ for some $e\in K_0(\mathcal X)$.
- Applying $\mathrm{pr}_1$ and naturality of $(-)/p^m$ gives $N\xi_1\equiv\mathrm{res}(e)\pmod{p^mK_0(X_1)}$.

**The numerical statement.**
- Let $\theta:K_0(X_1)\to Q:=\mathcal N(X_1)$ be the quotient map, with $Q$ finitely generated (Lemma 4.2), and put $M=\theta(\mathrm{res}\,K_0(\mathcal X))$.
- By (App), the class of $\theta(N\xi_1)$ in $Q/M$ lies in $\bigcap_mp^m(Q/M)$.
- For a finitely generated abelian group, this intersection is the prime-to-$p$ torsion subgroup.
- Hence $N'\theta(N\xi_1)\in M$ for some $N'$ prime to $p$. Choose $\eta$ with $\theta(\mathrm{res}\,\eta)=N'\theta(N\xi_1)$.
- The reformulation is Lemma 4.2 together with compatibility of $ch$ with specialization. $\square$

**Corollary B.1.** Assume $p>d+6$, (Cont$_0$) for $\mathcal X\otimes W(k')$ for all finite $k'$, and (D$_v$). Then (pVHC$_v$) holds.

*Proof.* Let $c_{\rm crys}(z_1)\in F^r$, and take $\xi_1$ with $ch(\xi_1)=z_1$; this is possible since $ch$ is bijective rationally. By Theorem B, $u=N'Nz_1-\sigma(Z)$ is numerically trivial, where $Z:=ch_r(\eta_{K_0'})$. By (D$_v$), $c_{\rm crys}(u)=0$, so $c_{\rm crys}(z_1)=(N'N)^{-1}\mathrm{BO}(c_{dR}(Z))$ by (I1). $\square$

**Proposition B.2 (divisors; known).** For $r=1$, (pVHC$_v$) holds unconditionally. This follows from (I11): a $p$-power of $L_1$ lifts to $\mathcal X$. In the language of Theorem B, (Cont) is replaced by Grothendieck existence $\mathrm{Pic}(\mathcal X)=\varprojlim_n\mathrm{Pic}(X_n)$, and numerical equivalence is not needed. This is the sanity check of ladder item (b): the mechanism reproduces the known divisor case. It does **not** recover Lefschetz (1,1) for absolute classes from $p$-adic data. Theorem A for $r=1$ still needs (T$_v$) and (Rat$_v$) for divisors on $X_1$, and the only proof I know of (Rat$_v$) for $r=1$ goes through Lefschetz (1,1) itself (as Milne notes for his conjecture).

**4.4. On "codimension 2 when $H^2(X,\mathcal O)=0$".**
- For $r=1$, the hypothesis $h^{0,2}=0$ is exactly $F^1H^2=H^2$, which makes the BEK condition vacuous.
- The codimension-$r$ analogue is $h^{i,2r-i}=0$ for all $i<r$, which says $F^rH^{2r}=H^{2r}$. For $r=2$ this means $h^{0,4}=h^{1,3}=0$.
- $H^2(\mathcal O)$ only governs the obstruction for line bundles. The obstruction to deforming codimension-2 classes lives in $H^3(\Omega^1)$ and $H^4(\mathcal O)$, the graded pieces of $H^4/F^2$.

**Corollary B.3 (Hodge-vacuous case).** Suppose $h^{i,2r-i}(X_{F_v})=0$ for all $i<r$, $p>d+6$, and (Cont$_0$) holds. Then every $z_1\in CH^r(X_1\otimes k')_{\mathbb Q}$ is numerically equivalent to a rational multiple of a specialization of a cycle from $X_{K_0'}$. If in addition (D$_v$) holds, then the $\mathbb Q$-span of the crystalline cycle classes of codimension $r$ on $X_1\otimes k'$ equals $\mathrm{BO}$ of the de Rham cycle classes of codimension $r$ on $X_{K'_0}$.

*Proof.* Here $F^rH^{2r}=H^{2r}$, so (I2) applies to every class. Then use Theorem B and Corollary B.1. $\square$

## 5. Hodge classes with algebraic crystalline specialization: Theorem C

**The Lefschetz–Hodge operator.** Let $H^*$ be a graded-commutative algebra over a field $E$ with Poincaré duality in degree $2d$, and $L\in H^2$ satisfying hard Lefschetz. For $x\in H^{2r}$ with $2r\le d$, write the Lefschetz decomposition $x=\sum_{j\ge0}L^jx_j$, where $x_j\in P^{2r-2j}:=H^{2r-2j}\cap\ker L^{d-2r+2j+1}$. Define
$$*_Lx:=\sum_j(-1)^{r-j}L^{d-2r+j}x_j\in H^{2d-2r}.$$

**Lemma 5.0 (Hodge–Riemann).** Let $Y$ be a complex projective manifold of dimension $d$, $L$ an ample class, and $0\neq x\in H^{2r}(Y,\mathbb Q)\cap H^{r,r}$ with $2r\le d$. Then $\int_Yx\cup*_Lx>0$.

*Proof.*
- **Cross terms vanish.** For $j<j'$, $\int L^jx_j\cdot L^{d-2r+j'}x_{j'}$ contains the factor $L^{d-2r+j+j'}x_j$. Its exponent is at least $d-2r+2j+1$, so the factor is $0$ by primitivity of $x_j$. The case $j>j'$ is symmetric.
- **Diagonal terms are positive.** The decomposition is defined over $\mathbb Q$ and respects Hodge types, so each $x_j$ is a rational primitive class of type $(r-j,r-j)$. Its term is $(-1)^{r-j}\int L^{d-2(r-j)}x_j^2$, which is $>0$ if $x_j\ne0$ by the Hodge–Riemann relations $i^{p-q}(-1)^{k(k-1)/2}\int L^{d-k}y\bar y>0$. $\square$

**Hypothesis (Pos$_v$).** Let $\mathcal L$ be relatively ample on $\mathcal X$, and put $L_1=c_1^{\rm crys}(\mathcal L|_{X_1})$. Hard Lefschetz holds for $L_1$ because it holds for $\mathcal L_{F_v}$, via (I1). The hypothesis is: for every finite $k'$ and every numerically trivial $u\in CH^r(X_1\otimes k')_{\mathbb Q}$, the class $*_{L_1}c_{\rm crys}(u)$ lies in the $K_0''$-span of crystalline classes of cycles on $X_1\otimes k''$, for some finite $k''\supseteq k'$.

**Lemma 5.1 (when (Pos$_v$) holds).** (Pos$_v$) follows from either of the following:
- (a) the crystalline Tate conjecture for $X_1$ in codimension $d-r$, over all finite extensions;
- (b) Lefschetz standard conjecture B for $X_1$ in the form "$*_{L_1}$ is induced by an algebraic correspondence".

It also follows from (D$_v$), which gives $c(u)=0$. Neither (a) nor (b) is known to imply (D$_v$). For instance, in characteristic $p$, B is only known to give D together with the Hodge standard conjecture.

*Proof of (a).* $\varphi L_1=pL_1$ by (I1), so the Lefschetz decomposition is $\varphi$-stable. If $\varphi x=p^rx$, uniqueness of the decomposition gives $\varphi x_j=p^{r-j}x_j$, and hence $\varphi(*x)=p^{d-r}*x$. Since $c(u)\in T^r$, it follows that $*c(u)\in T^{d-r}$, which lies in the span of cycle classes by (T). (b) is immediate. $\square$

**Theorem C.** Let $\alpha\in\mathrm{Hdg}^r(X_{\sigma,\mathbb C})$, with $2r\le d$, be de Rham-rational over $F$. Let $v$ be a good unramified place with $p>d+6$. Assume:
- (a) $\alpha_{\rm crys}=c_{\rm crys}(z_1)$ for some $z_1\in CH^r(X_1\otimes k')_{\mathbb Q}$;
- (b) (Cont$_0$) holds for $\mathcal X\otimes W(k')$;
- (c) (Pos$_v$) holds.

Then $\alpha$ is algebraic. Hypothesis (a) is necessary, by Theorem A(iii).

*Proof.* **Step 1 (Theorem B).** Pick $\xi_1$ with $ch(\xi_1)=z_1$. Its Chern character lies in $F^r$, so (I2) and Theorem B give $M\ge1$ and $\eta\in K_0(\mathcal X\otimes W(k'))$ such that $u:=Mz_1-ch_r(\eta|_{X_1})$ is numerically trivial.

**Step 2 (the difference class).**
- Put $Z:=ch_r(\eta_{K_0'})$. By (I1), $c_{\rm crys}(ch_r(\eta|_{X_1}))=\mathrm{BO}(c_{dR}(Z))$.
- Lemma 2.2 gives $Z'$ on $X_{\bar F}$ with $\iota_v c_{dR}(Z')=c_{dR}(Z)$.
- Let $\beta:=M\alpha-c(Z')$. It is a rational Hodge class (via $\sigma$), with $\beta_{dR}\in H^{2r}_{dR}(X/\bar F)$ and $\mathrm{BO}(\iota_v\beta_{dR})=c_{\rm crys}(u)$.

**Step 3 (an ample class over $\bar F$).**
- By Lemma 2.2 with $r=1$, there is a divisor $D'$ on $X_{\bar F}$ with $\iota_vc_{dR}(D')=c_1(\mathcal L_{\bar F_v})$.
- $D'$ is ample by Nakai–Moishezon. For a subvariety $V$ of dimension $e$, $D'^e\cdot V=\mathcal L^e\cdot V_{\bar F_v}>0$, because intersection numbers depend only on cohomology classes.
- Let $*$ be the operator of $L:=c(D')$ on $H_{dR}(X/\bar F)$. It is compatible with the $\sigma$-comparison and, through $\iota_v$ and BO, with $*_{L_1}$, since all of these are isomorphisms of graded rings carrying $L$ to $L$.

**Step 4 (two evaluations of one algebraic number).** Put $q:=\int\beta_{dR}\cup*\beta_{dR}\in\bar F$.
- Over $\mathbb C$: Betti and de Rham traces match with the twist $\mathbb Q(d)$. Writing $\beta_B=(2\pi i)^rb$ with $b\in H^{2r}(X_\sigma(\mathbb C),\mathbb Q)$, we get $\sigma(q)=\int b\cup*_{\ell}b$, where $\ell:=(2\pi i)^{-1}c_B(D')\in H^2(X_\sigma(\mathbb C),\mathbb Q)$ is ample. The operators for $c_B(D')$ and for $\ell$ differ by the factor $(2\pi i)^{d-2r}$, which the twists absorb. This is $>0$ unless $\beta=0$, by Lemma 5.0.
- Over $\bar F_v$: $\iota_v(q)=\int c(u)\cup*_{L_1}c(u)$. By (Pos$_v$) this equals $\sum_ic_i\deg(u\cdot w_i)=0$, using Remark 2.0.1.
- Both $\sigma$ and $\iota_v$ are injective on $\bar F$, so $q=0$, hence $\beta=0$, i.e. $\alpha=M^{-1}c(Z')$. $\square$

**Proposition 5.2 (supersingular abelian varieties).** Let $A_1$ be a supersingular abelian variety of dimension $g$ over a finite field $k$. There is a finite $k'/k$ with the following properties for every finite $k''\supseteq k'$. Let $\Lambda^r\subset H^{2r}_{\rm crys}(A_1\otimes k'')_{\mathbb Q}$ be the $\mathbb Q$-span of crystalline classes of Lefschetz cycles (polynomials in divisors) of codimension $r$. Then:
- (a) $T^r(A_1\otimes k'')=\Lambda^r\otimes\mathbb Q_p$, and $T^r\otimes K_0''\cong H^{2r}$, for all $r$. In particular (T$_v$) holds in every codimension.
- (b) The pairing $\Lambda^r\times\Lambda^{g-r}\to\mathbb Q$ is nondegenerate, and every numerically trivial $u\in CH^r(A_1\otimes k'')_{\mathbb Q}$ has $c_{\rm crys}(u)=0$. In particular (D$_v$), and hence (Pos$_v$), hold.

*Proof.* **Divisors.**
- Since $A_1$ is supersingular, its Frobenius eigenvalues are $\sqrt q$ times roots of unity. Pass to $k'$ of square order $q$ where the $q$-Frobenius $\pi$ has all eigenvalues $\sqrt q$. Since $\pi$ is semisimple (Tate), $\pi=\sqrt q$ on $H^1_\ell$. Hence $\pi=q$ on $H^2_\ell$, and Tate's theorem for divisors on abelian varieties over finite fields gives $\rho(A_1\otimes k')=b_2=\binom{2g}2$.
- By (I1), $NS_{\mathbb Q}$ maps into $T^1$.
- A numerically trivial line bundle has a power in $\mathrm{Pic}^0$ (Matsusaka), and $\mathrm{Pic}^0(k'')$ is finite. So its crystalline class is $0$. Lemma 2.4(a), pairing with curve classes, then gives $NS_{\mathbb Q}\otimes\mathbb Q_p\hookrightarrow T^1$.
- $\dim_{\mathbb Q_p}T^r\le\dim_{K_0''}H^{2r}$ for all $r$. Indeed, a shortest $K_0''$-relation $\sum c_ix_i=0$ among $\varphi$-eigenvectors, normalized with $c_1=1$, can be compared with its image under $p^{-r}\varphi$, giving $\sum(\sigma(c_i)-c_i)x_i=0$. Minimality forces $c_i\in\mathbb Q_p$, so $\mathbb Q_p$-independent elements of $T^r$ are $K_0''$-independent.
- Hence $T^1=NS_{\mathbb Q}\otimes\mathbb Q_p$ and $T^1\otimes K_0''=H^2$.

**Higher codimension.**
- $H^*_{\rm crys}(A_1)_{\mathbb Q}=\bigwedge^*H^1$ [Il]. $\bigwedge^{2r}H^1$ is spanned by $r$-fold products from $\bigwedge^2H^1=H^2$.
- So the $\mathbb Q_p$-span $P^r$ of $r$-fold products from $T^1$, which equals $\mathbb Q_p\Lambda^r$, satisfies $P^r\subseteq T^r$ and $K_0''P^r=H^{2r}$.
- Comparing dimensions, $P^r=T^r$ and $T^r\otimes K_0''\cong H^{2r}$. This is (a).

**The pairing.**
- $\varphi$ acts on $H^{2g}$ as $p^g\sigma$, so Poincaré duality restricts to a $\mathbb Q_p$-valued pairing $T^r\times T^{g-r}\to\mathbb Q_p$. Its $K_0''$-extension is Poincaré duality, so it is perfect.
- If $\lambda\in\Lambda^r$ or $\lambda=c(u)$, with $u$ numerically trivial, pairs to $0$ with $\Lambda^{g-r}$, then it pairs to $0$ with $T^{g-r}=\mathbb Q_p\Lambda^{g-r}$. Hence $\lambda=0$, which is (b). $\square$

**Corollary C.1 (supersingular reduction).** Let $A/F$ be an abelian variety, and $\alpha\in\mathrm{Hdg}^r(A_{\mathbb C})$ with $2r\le g$. Enlarge $F$ by (I6) so that $\alpha$ is $G_F$-invariant and de Rham-rational over $F$. Let $v$ be a good unramified place with $p>g+6$ and supersingular reduction $A_1$. Assume (Cont$_0$) for $\mathcal A\otimes W(k')$ for all finite $k'$. Then:
- **(Rat$_v$) $\Rightarrow$ algebraic.** If (Rat$_v$) holds, already for $w$ ranging over Lefschetz cycles, then $\alpha$ is algebraic.
- **Converse.** If $\alpha$ is algebraic, (Rat$_v$) holds at every such $v$ that is unramified in the field of definition of some cycle representing $\alpha$, i.e. at all but finitely many such $v$.

*Proof of the first statement.*
- (I5) gives (dR$_v$), and Lemma 2.1 gives $\alpha_{\rm crys}\in T^r$.
- Proposition 5.2 and Lemma 2.4(b), with $V=\Lambda^r$ and $V'=\Lambda^{g-r}$, together with (Rat$_v$), give $\alpha_{\rm crys}\in\Lambda^r$. That is, $\alpha_{\rm crys}=c(z_1)$ for a Lefschetz cycle $z_1$.
- Proposition 5.2(b) gives (D$_v$), so Corollary B.1 gives (pVHC$_v$) for $z_1$, and Theorem A(i) concludes. (Theorem C gives the same conclusion.)

*Proof of the converse.* This is Theorem A(iii) over the field of definition. $\square$

**Corollary C.2 (CM abelian varieties).** Let $A/F$ have CM, and let $\tilde{\mathcal E}$ be the compositum of the Galois closures of the CM fields of its simple factors. $\tilde{\mathcal E}$ is a CM field, Galois over $\mathbb Q$, and its complex conjugation $c$ is central in $\mathrm{Gal}(\tilde{\mathcal E}/\mathbb Q)$.
- By Chebotarev, a set of primes $p$ of positive density is unramified in $\tilde{\mathcal E}$ with $\mathrm{Frob}_p=c$.
- For such $p$, every prime $\mathfrak P\mid p$ of each CM field $\mathcal E_i$ satisfies $\bar{\mathfrak P}=\mathfrak P$. So the set $H_{\mathfrak P}$ of embeddings inducing $\mathfrak P$ is stable under $c$, and $|\Phi_i\cap H_{\mathfrak P}|=|H_{\mathfrak P}|/2$.
- By the Shimura–Taniyama formula [CCO, §2.1] **[u]**, every good reduction of $A$ above $p$ is supersingular.
- After enlarging $F$ as in C.1, and also so that the endomorphisms are defined over $F$, all but finitely many of these $p$ are unramified in $F$, of good reduction, and $>g+6$.

So C.1 applies at infinitely many places. Choose $F$ so large that all of the finite-dimensional space $\mathrm{Hdg}^*(A)$ is $G_F$-invariant and de Rham-rational. Then one place serves for all classes. In particular, **if (Cont$_0$) holds for abelian schemes over $W(\mathbb F_q)$, then the crystalline component of Milne's rationality conjecture (I9), at a single such place, implies HC for every Hodge class on $A$.** The converse (HC $\Rightarrow$ (Rat$_v$)) is elementary (Corollary C.1) and is Milne's observation [Mi1]. So, modulo (Cont), HC for a CM abelian variety is equivalent to (Rat$_v$) for its Hodge classes at a supersingular unramified place outside a finite set. HC is known for $g\le5$ (Markman, docs/02), so the content is for $g\ge6$.

## 6. Ladder item (c): from number fields to $\mathbb C$, and what $p$-adic methods cannot see

**Proposition 6.1 (known: Voisin [Vo, Prop. 0.2] and Deligne [De]).** HC holds if and only if both of the following hold:
- (i) HC for absolute Hodge classes on smooth projective varieties over $\bar{\mathbb Q}$;
- (ii) every Hodge class on every smooth projective complex variety is absolute Hodge.

*Proof.* "$\Rightarrow$": cycle classes are absolute Hodge [De, §2]. "$\Leftarrow$": by (ii), every Hodge class is absolute, and (I10) then gives HC.

*Sketch of Voisin's argument, for orientation; not claimed as proved here.* Spread $X$ out to a smooth projective $\mathcal X\to S$ over $\bar{\mathbb Q}$, with $X=\mathcal X_s$ for a point $s$ that is generic over $\bar{\mathbb Q}$.
1. Absoluteness, together with Cattani–Deligne–Kaplan and a countability argument, shows that the component of the Hodge locus of $\alpha$ through $s$ has only countably many $\mathrm{Aut}(\mathbb C/\bar{\mathbb Q})$-conjugates. So it is defined over $\bar{\mathbb Q}$, and it equals $S$ because $s$ is generic.
2. Deligne's global invariant cycle theorem and semisimplicity give an absolute Hodge class $\tilde\alpha$ on a smooth compactification of $\mathcal X$, defined over $\bar{\mathbb Q}$, restricting to $\alpha$.
3. Apply (i) to $\tilde\alpha$. $\square$

**Proposition 6.2 (proved here; elementary).** Let $X$ be defined over $\bar{\mathbb Q}$ and $\alpha\in\mathrm{Hdg}^r(X_{\mathbb C})$. The following are equivalent:
- (a) $\alpha_{dR}\in H^{2r}_{dR}(X/\bar{\mathbb Q})$;
- (b) for every $\tau\in\mathrm{Aut}(\mathbb C/\bar{\mathbb Q})$, the vector $\tau(\alpha_{dR})$ is the de Rham component of a rational Hodge class on $X$. Here $\tau$ acts on $H_{dR}(X/\bar{\mathbb Q})\otimes\mathbb C$ through the second factor.

Condition (a) is necessary for algebraicity (Corollary 2.3). It is also a prerequisite for every construction in §§2–5, which all start from $\alpha_{\rm crys}=\mathrm{BO}(\iota_v\alpha_{dR})$.

*Proof.* (a)$\Rightarrow$(b): then $\tau(\alpha_{dR})=\alpha_{dR}$.

(b)$\Rightarrow$(a): write $\alpha_{dR}=\sum c_ie_i$ in a $\bar{\mathbb Q}$-basis. If some $c_i$ were transcendental, its $\mathrm{Aut}(\mathbb C/\bar{\mathbb Q})$-orbit would be the uncountable set of all transcendental numbers. But by (b) the orbit of $\alpha_{dR}$ lies in the countable set of de Rham components of rational classes. $\square$

**Consequence.** The $p$-adic strategy can address only part (i) of Proposition 6.1, and only for classes satisfying (a). Property (a), for all Hodge classes on varieties over $\bar{\mathbb Q}$, is part of the "transcendental" content C3 of docs/03 (special points of Hodge loci). None of the $p$-adic inputs used here bears on it. The precise obstruction of this route is therefore the conjunction of:
- (ii), the absoluteness conjecture, untouched;
- within (i), the hypotheses of Theorem A: (T$_v$), (D$_v$), (Rat$_v$), and (Cont) [or (pVHC$_v$)].

For CM abelian varieties only (Rat$_v$) and (Cont) remain (Corollary C.2).

## 7. GAPS

- **G1 — continuity of $K$-theory (Cont$_0$).**
  - *Statement:* for $\mathcal X$ smooth projective over $W(k)$ and all $m$, $\pi_0(K(\mathcal X)/p^m)\to\pi_0(\mathrm{holim}_nK(X_n)/p^m)$ is surjective.
  - *Where needed:* Theorem B rests on it, and hence so do B.1, B.3, Theorem C, C.1 and C.2, each also needing the other hypotheses it names.
  - *Why I cannot prove it.* Grothendieck existence identifies $\mathrm{Perf}(\mathcal X)$ with $\lim_n\mathrm{Perf}(X_n)$, but $K$-theory does not commute with limits of categories in general.
  - CMM prove the affine case (I3) and say their methods do not reach proper schemes.
  - The natural route would be Zariski descent on $|X_1|$ for $U\mapsto K(\lim_n\mathrm{Perf}(U_n))$. Thomason–Trobaugh descent does not apply, because a limit of Verdier localizations $\mathrm{Perf}(X_n)\to\mathrm{Perf}(U_n)$ need not be a Verdier localization. I do not know how to fix this.
  - Only the consequence (App) is used, for the single class at hand.
- **G2 — rationality (Rat$_v$).** This is the crystalline part of Milne's rationality conjecture (I9).
  - It is open, and implied by HC for CM abelian varieties.
  - Proposition 3.1 shows that it is not a consequence of Frobenius invariance, the Hodge filtration, and the $\mathbb Q_p$-span of algebraic classes.
  - Using many primes does not help: the test cycles $w$ exist only on the special fibre at one prime.
- **G3 — the standard conjectures on the special fibre.** (T$_v$) and (D$_v$) are open for general $X_1$. They are used in Theorem A(ii) and Corollary B.1. They hold unconditionally for supersingular abelian varieties (Proposition 5.2), with Lefschetz cycles.
- **G4 — the de Rham property (dR$_v$).** It is known for abelian varieties (I5) and open for general absolute Hodge classes. (I expect it for André-motivated classes, because the $p$-adic comparison respects the operations that generate them; this is not checked.)
- **G5 — absoluteness.** This is Proposition 6.1(ii), outside the reach of the method (Proposition 6.2).
- **G6 — inputs whose exact form was not verified against sources** (network block).
  - BEK: the bound $p>d+6$ and the form of the lift. Lemma 4.1 shows that the form used is the only non-vacuous reading.
  - The numbering of (I11); Nizioł's compatibility (I4).
  - The Shimura–Taniyama formula used in Corollary C.2.
  - The normalization of the $p$-part in Milne's conjecture (I9).
  - [Il] for $H^*_{\rm crys}$ of abelian varieties.
  - Lurie's Grothendieck existence for perfect complexes. This is used only in a remark and not in any proof.
- **G7 — ladder item (b) for codimension 2.** No new unconditional case of the $p$-adic VHC was obtained. In particular, nothing is proved for codimension-2 classes when $H^2(X,\mathcal O)=0$. §4.4 explains why that hypothesis is the wrong one, and Corollary B.3 gives the correct analogue (still conditional on G1).
- **G8 — top target (a).** It is not proved. Theorem A is a reduction to G1–G4, and the passage to $\mathbb C$ needs G5.

## 8. Checklist (docs/03 §3.4)

**Where rational coefficients are essential.**
1. **BEK lifts only rationally.** By Lemma 4.1, each $K_0(X_n)_{\mathbb Q}$ equals $K_0(X_1)_{\mathbb Q}$. The content of (I2) is that some multiple $N\xi_1$ lifts compatibly.
2. **Theorem B produces only multiples.** It gives $N'N\xi_1$, where $N'$ is an uncontrolled integer prime to $p$ coming from torsion in $\mathcal N(X_1)/M$. Its proof uses the finite generation of the numerical group, which is $\mathbb Z$-structure, to pass from "$p$-adically approximable" to "rational multiple".
3. **The $\mathbb Q_p\to\mathbb Q$ step is where $\mathbb Q$-coefficients bite.** Lemma 2.4 makes this step using the $\mathbb Q$-valued intersection pairing. With $\mathbb Q_p$-coefficients the corresponding statements are **false** (Proposition 3.1, (I8)). If $\xi_1\in K_0(X_1)\otimes\mathbb Z_p$ is not rational, the proof of Theorem B breaks exactly at the Krull-intersection step, because $\theta(\xi_1)\notin Q$.
4. **The final cycle has denominators.** It is $M^{-1}Z'$, with $\mathbb Q$-coefficients, and $ch$ itself has denominators up to $d!$.

**Integral Hodge conjecture test.** Nothing here yields integral classes. The multiples $N$ (BEK), $N'$ (Theorem B), $M$ (Theorem C) and the denominators of $ch$ are uncontrolled. Varying $p$ does not remove them, because $N'$ is an arbitrary integer prime to $p$. So there is no conflict with Atiyah–Hirzebruch, Kollár, or Engel–de Gaay Fortman–Schreieder.

**Where projectivity is essential.**
- A smooth **projective** model over $W(k)$. This is required by BEK and by Grothendieck existence (Proposition B.2), and makes the comparison isomorphisms (I1), (I4) available.
- Hilbert schemes, in Lemma 2.2.
- An **ample** class in Theorem C. It is produced over $\bar F$ by Nakai–Moishezon (Step 3) and feeds the Hodge–Riemann inequality of Lemma 5.0. This is the step that fails for non-projective Kähler manifolds.
- HRR and intersection theory on the projective special fibre, in Lemma 4.2.

**Kähler Hodge conjecture test.** A non-algebraic complex torus, such as Voisin's, has no model over a number field or over $W(k)$. It has no algebraic de Rham, crystalline or $p$-adic étale cohomology to compare, and no ample class. So no step applies, and the argument cannot "prove" the false Kähler statement.

**Other false variants.**
- **Tate over $p$-adic fields and the $\mathbb Q_p$-coefficient $p$-adic VHC.** Both are false (Proposition 3.1). All our results need a *global* class: a Hodge class with $\alpha_{dR}$ over $F$, or a class in $K_0(X_1)$ rather than $K_0(X_1)\otimes\mathbb Z_p$.
- **Hodge classes not known to be absolute.** Excluded by Proposition 6.2.

**What a full proof must deliver (docs/03 §3.4), versus this file.**
- Absoluteness: not delivered; it is assumed (G5).
- Lefschetz B: not delivered. It is only used, as one sufficient condition for (Pos$_v$), and is known for abelian varieties.
- VHC: only its $p$-adic form is addressed, and only modulo (Cont) and numerical equivalence (Theorem B).
- The CM abelian case: conditional on (Cont) and (Rat$_v$) (Corollary C.2).
- A visible use of $\mathbb Q$-coefficients and of projectivity: yes, both, as listed above.

## 9. References

- [AMMN] B. Antieau, A. Mathew, M. Morrow, T. Nikolaus, *On the Beilinson fiber square*, Duke Math. J. 171 (2022), 3707–3806; arXiv:2003.12541.
- [BEK] S. Bloch, H. Esnault, M. Kerz, *p-adic deformation of algebraic cycle classes*, Invent. Math. 195 (2014), 673–722; arXiv:1203.2776. Characteristic-0 companion: *Deformation of algebraic cycle classes in characteristic zero*, Algebra & Number Theory 8 (2014).
- [Bl] D. Blasius, *A p-adic property of Hodge classes on abelian varieties*, in Motives, Proc. Symp. Pure Math. 55, Part 2 (1994); MPIM preprint 1992-59.
- [BO] P. Berthelot, A. Ogus, *F-isocrystals and de Rham cohomology I*, Invent. Math. 72 (1983), 159–199.
- [CCO] C.-L. Chai, B. Conrad, F. Oort, *Complex multiplication and lifting problems*, AMS Math. Surveys and Monographs 195 (2014).
- [CMM] D. Clausen, A. Mathew, M. Morrow, *K-theory and topological cyclic homology of henselian pairs*, J. Amer. Math. Soc. 34 (2021); arXiv:1803.10897.
- [De] P. Deligne (notes by J. Milne), *Hodge cycles on abelian varieties*, LNM 900 (1982).
- [Fu] W. Fulton, *Intersection theory*, 2nd ed., Springer 1998.
- [GM] H. Gillet, W. Messing, *Cycle classes and Riemann–Roch for crystalline cohomology*, Duke Math. J. 55 (1987).
- [Go] T. Goodwillie, *Relative algebraic K-theory and cyclic homology*, Ann. of Math. 124 (1986), 347–402.
- [Il] L. Illusie, *Complexe de de Rham–Witt et cohomologie cristalline*, Ann. Sci. ENS 12 (1979). See also Berthelot–Breen–Messing, LNM 930.
- [LP] C. Lazda, A. Pál, *Cycle classes in overconvergent rigid cohomology and a semistable Lefschetz (1,1) theorem*, Compositio Math. 155 (2019); arXiv:1701.05017.
- [Mi1] J. S. Milne, *Rational Tate classes*, Moscow Math. J. 9 (2009); arXiv:0707.3167.
- [Mi2] J. S. Milne, *Polarizations and Grothendieck's standard conjectures*, Ann. of Math. 155 (2002).
- [Mi3] J. S. Milne, *Abelian motives and Shimura varieties in nonzero characteristic*, arXiv:2508.09972 (2025).
- [Mo1] M. Morrow, *A variational Tate conjecture in crystalline cohomology*, J. Eur. Math. Soc. 21 (2019), 3467–3511; arXiv:1408.6783.
- [Mo2] M. Morrow, *A case of the deformational Hodge conjecture via a pro Hochschild–Kostant–Rosenberg theorem*, C. R. Math. 352 (2014), 173–177.
- [Ni] W. Nizioł, *Crystalline conjecture via K-theory*, Ann. Sci. ENS 31 (1998).
- [TT] R. Thomason, T. Trobaugh, *Higher algebraic K-theory of schemes and of derived categories*, Grothendieck Festschrift III (1990).
- [Vo] C. Voisin, *Hodge loci and absolute Hodge classes*, Compositio Math. 143 (2007), 945–958.
- Also used as standard background: Fontaine–Messing (1987), Faltings (1989) and Tsuji (1999) for the crystalline comparison; Tate (1966) for endomorphisms and divisors of abelian varieties over finite fields; Grothendieck–Messing and Katz, *Serre–Tate local moduli* (LNM 868), for lifting ordinary elliptic curves.

## 10. Claimed results

| Label | One-line statement | Status |
|---|---|---|
| Remark 2.0.1 | Numerical triviality over $k'$ implies numerical triviality over $\bar k$ | proved here (elementary) |
| Lemma 2.1 | (dR$_v$) and $G_{F_v}$-invariance imply $\alpha_{\rm crys}\in T^r\cap F^r$ | proved here, from (I4) (standard) |
| Lemma 2.2 | A cycle class over any algebraically closed $\Omega\supseteq\bar F$ is the class of a cycle over $\bar F$ | proved here (standard rigidity) |
| Corollary 2.3 | Algebraic Hodge classes on varieties over $\bar{\mathbb Q}$ have $\bar{\mathbb Q}$-rational de Rham component | proved here (known) |
| Lemma 2.4 | Rational pairings plus nondegeneracy force $E$-combinations to be rational | proved here (elementary) |
| Theorem A | Absolute class + (dR$_v$) + (T$_v$) + (D$_v$) + (Rat$_v$) + (pVHC$_v$) $\Rightarrow$ algebraic; (dR$_v$), (Rat$_v$) and the instance of (pVHC$_v$) used are necessary | proved here, conditional on the named hypotheses |
| Proposition 3.1 | The $\mathbb Q_p$-coefficient version fails: there is a Frobenius-invariant $F^1$-class in $NS(X_1)\otimes\mathbb Q_p$ that is neither rational nor liftable | known (Serre–Tate; cf. Lazda–Pál), proof included |
| Lemma 4.1 | $K_0(X_n)_{\mathbb Q}=K_0(X_1)_{\mathbb Q}$, which pins down the meaning of the BEK lift | proved here, from Goodwillie (known in substance) |
| Lemma 4.2 | The numerical $K$-group $\mathcal N(Y)$ is finitely generated free | proved here (standard) |
| Theorem B | (Cont$_0$) + a BEK formal lift $\Rightarrow$ $N'N\xi_1$ is numerically a specialization | proved here, conditional on (Cont$_0$) (and BEK for the corollaries); believed new in this form |
| Corollary B.1 | (Cont$_0$) + (D$_v$) + $p>d+6$ $\Rightarrow$ (pVHC$_v$) | proved here, conditional on (Cont$_0$), (D$_v$), BEK |
| Proposition B.2 | $p$-adic VHC for divisors (some $p$-power lifts) | known (Berthelot–Ogus + Grothendieck existence) |
| Corollary B.3 | If $h^{i,2r-i}=0$ for $i<r$, every codim-$r$ cycle on $X_1$ is numerically a specialization | proved here, conditional on (Cont$_0$) (and (D$_v$) for the cohomological form) |
| Lemma 5.0 | $\int x*_Lx>0$ for nonzero rational $(r,r)$-classes, $2r\le d$ | known (Hodge–Riemann), proof included |
| Lemma 5.1 | (Pos$_v$) follows from (T) in codimension $d-r$, from B, or from (D) | proved here (elementary) |
| Theorem C | Algebraic crystalline specialization + (Cont$_0$) + (Pos$_v$) $\Rightarrow$ algebraic | proved here, conditional on (Cont$_0$), (Pos$_v$), BEK; believed new in this form (positivity trick standard) |
| Proposition 5.2 | Supersingular abelian $A_1$: Tate classes are $\mathbb Q_p$-spans of Lefschetz classes, and (D) holds | proved here (known in substance) |
| Corollary C.1 | Supersingular good reduction, given (Cont$_0$): Hodge class algebraic $\Leftarrow$ (Rat$_v$); converse at almost all such $v$ | proved here, conditional on (Cont$_0$) and the inputs (I2), (I5), (I6) |
| Corollary C.2 | CM: infinitely many supersingular places. Hence (Cont$_0$) + Milne's rationality conjecture (crystalline part) $\Rightarrow$ HC for CM abelian varieties | proved here, conditional on (Cont$_0$), (Rat$_v$), BEK and Shimura–Taniyama (cited) |
| Proposition 6.1 | HC $\Leftrightarrow$ HC for absolute classes over $\bar{\mathbb Q}$ $\wedge$ (Hodge $\Rightarrow$ absolute) | known (Voisin 2007, Deligne) |
| Proposition 6.2 | For $X/\bar{\mathbb Q}$: $\alpha_{dR}$ is $\bar{\mathbb Q}$-rational iff all $\mathrm{Aut}(\mathbb C/\bar{\mathbb Q})$-conjugates of $\alpha_{dR}$ are Hodge | proved here (elementary) |
