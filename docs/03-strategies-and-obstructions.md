# 3. Strategies and obstructions: an honest analysis

**Summary.** This repository does not prove the Hodge conjecture, and the session that produced it did not find a proof or a plausible route to one. What follows is an attempt to be useful anyway: a map of the few mechanisms that have ever turned a Hodge class into an algebraic cycle, the constraints that the known counterexamples to variants impose on any proof, an assessment of each live strategy, a checklist that any claimed proof must satisfy, and a short list of concrete open problems where progress is realistic.

---

## 3.1 The mechanisms that have ever produced cycles from classes

A proof must manufacture subvarieties (or coherent sheaves) out of transcendental data: a rational class in singular cohomology whose complex-analytic representative is a $(p,p)$-form. Every known case uses one of the following.

**M1. The exponential sequence (degree 2 only).** $0\to\mathbb{Z}\to\mathcal{O}_X\xrightarrow{\exp}\mathcal{O}_X^*\to0$ identifies integral $(1,1)$-classes with first Chern classes of line bundles, and on a projective variety line bundles have meromorphic sections. This is the whole content of Lefschetz (1,1), and it is the *only* general-purpose mechanism known.
Why it does not extend: in degree $2p$ the analogous object is Deligne cohomology, $0\to J^p(X)\to H^{2p}_{\mathcal D}(X,\mathbb{Z}(p))\to \mathrm{Hdg}^p_{\mathbb{Z}}(X)\to0$, where $J^p(X)$ is Griffiths' intermediate Jacobian. There is a cycle class map $CH^p(X)\to H^{2p}_{\mathcal D}$, but (a) $J^p$ is a complex torus which is in general not an abelian variety, (b) the Abel–Jacobi map is neither surjective nor injective in general (Griffiths; Mumford), and (c) classes in $H^{2p}_{\mathcal D}$ are not "sections of anything": the would-be geometric objects (higher gerbes with connective structure) have no algebraic avatar producing subvarieties.

**M2. Chern classes of sheaves plus deformation theory.** If a Hodge class is $c_p(\mathcal F)$ for a coherent sheaf $\mathcal F$ on one fibre of a family, Bloch's semiregularity map (Bloch 1972; Buchweitz–Flenner 2003) controls whether $\mathcal F$ deforms along the locus where the class stays of type $(p,p)$: if the semiregularity map is injective, deformations of $\mathcal F$ are unobstructed exactly in the directions where the class stays Hodge. Bloch–Esnault–Kerz (2014) proved the infinitesimal statement for $K$-theory classes in general (over Artinian or formal bases a class lifts iff its Chern character stays in $F^p$). Markman's proofs for Weil classes (2023, 2025) are this mechanism carried out with extraordinary care: he builds a sheaf on a special abelian variety (e.g. from a genus-3 Jacobian) whose Chern character hits the Weil class, proves it is semiregular, and deforms it over the whole Hodge locus, then degenerates to reach other discriminants.
Limitations: one needs a *seed* (a point of the Hodge locus where an algebraic representative is already known), and semiregularity; neither is available for a general Hodge class. The step from BEK's formal lifts to actual cycles ("algebraization") is precisely the open variational Hodge conjecture. Totaro (Sept 2026) calls the obstacles to proving the variational conjecture by semiregularity "convincing".

**M3. Special geometry.** Abelian varieties (theta functions, Fourier–Mukai, moduli of sheaves, Shimura varieties), Fermat varieties (explicit linear cycles, Aoki's cycles, the Shioda–Katsura inductive structure, Jacobi sums), K3 and hyper-Kähler varieties (Mukai lattices, derived equivalences, hyperholomorphic bundles, monodromy), moduli of curves (tautological classes). Each proof uses an enormous amount of structure that a general variety does not have.

**M4. Small Chow groups.** If $CH_0(X)$ is supported on a subvariety of dimension $\le3$, the decomposition of the diagonal (Bloch–Srinivas 1983) reduces $\mathrm{HC}(X,2)$ to varieties of dimension $\le3$, where it is known. By Mumford's theorem, varieties with $h^{n,0}\neq0$ have infinite-dimensional $CH_0$, so this never touches the hard cases. It does settle, for example, codimension-2 cycles on all Fano fourfolds (rationally connected, hence $CH_0=\mathbb{Z}$): every hypersurface of degree $\le5$ in $\mathbb{P}^5$. **The first open hypersurface case is therefore the sextic (Calabi–Yau) fourfold in $\mathbb{P}^5$.**

**M5. Degeneration.** Cycles specialize, so degeneration is a tool for *obstructing* algebraicity (Kollár's integral counterexamples; Engel–de Gaay Fortman–Schreieder) and for transporting algebraicity from a family to its limits (Markman's passage from discriminant $-1$ sixfolds to fourfolds of every discriminant). It cannot create cycles on a general fibre.

**M6. Arithmetic.** HC implies that Hodge classes are absolute Hodge (stable under $\mathrm{Aut}(\mathbb{C})$). Voisin (2007) shows that for (weakly) absolute classes HC reduces to varieties over $\overline{\mathbb{Q}}$, and Klingler–Otwinowska–Urbanik (2023) prove the field-of-definition statement for special subvarieties satisfying a monodromy condition ("weakly non-factor"), which reduces the general statement to special points. Over $\overline{\mathbb{Q}}$ one could hope to bring in $\ell$-adic or $p$-adic methods (Tate conjecture, crystalline cycle classes, BEK's $p$-adic deformation theory), but the Tate conjecture is itself open, and for abelian varieties the known implications run from Hodge to Tate (through the Mumford–Tate conjecture), not the other way.

That is the complete list. Everything in `02-known-cases.md` is M1–M6 in some combination.

---

## 3.2 What the counterexamples forbid

**C1. Rational coefficients are essential.** The integral conjecture fails with unbounded denominators (Kollár: a prime $p$ with $p^3\mid d$; EdGFS: the factor 2 on abelian varieties). A proof cannot be a canonical construction "class $\mapsto$ subvariety"; it must produce cycles only up to multiples, and the multiples must be allowed to depend on the variety.

**C2. Projectivity is essential.** Voisin's tori (2002) carry Hodge classes that are not even Chern classes of coherent analytic sheaves. Hence any argument that reads as "Hodge theory plus analysis on a compact Kähler manifold" is refuted before it starts. In every known proof one can point to where projectivity enters: ample twists giving sections (Lefschetz), GAGA and moduli of sheaves on *projective* varieties (Markman), explicit equations (Fermat), the quasi-projective base of the family (Cattani–Deligne–Kaplan; the o-minimal proofs). A correct general proof must contain an identifiable step that fails for Voisin's tori.

**C3. Transcendence is unavoidable.** A Hodge class is a topological object, $\alpha\in H^{2p}(X^{\mathrm{an}},\mathbb{Q})$. For $\sigma\in\mathrm{Aut}(\mathbb{C})$ the conjugate variety $X^\sigma$ can be non-homeomorphic to $X$ (Serre 1964), and $\sigma$ acts on algebraic de Rham cohomology but not on singular cohomology. HC predicts nevertheless that $\sigma(\alpha)$ is a rational $(p,p)$-class on $X^\sigma$. Deligne proved this for abelian varieties using two ingredients: *Principle B* (absoluteness propagates along connected Hodge loci) and the structure of the Hodge loci of abelian varieties as Shimura varieties, whose zero-dimensional special subvarieties are CM points, governed by the theory of complex multiplication (Shimura–Taniyama). For a general variation of Hodge structure the period domain is not algebraic (Griffiths transversality), the Hodge loci are nevertheless algebraic (CDK), the positive-dimensional components satisfying KOU's monodromy condition behave arithmetically (KOU), and **the special points — zero-dimensional components — are the hard core**: there is no theory of complex multiplication for them. Such points need not be CM points: an isolated point of the Hodge locus of one class can have a non-torus Mumford–Tate group (`docs/attacks/03-hodge-loci-arithmetic.md`, Prop. 4.1, an example with Mumford–Tate group $\mathrm{GL}_2$ in a family over $\mathbb Q$). At a CM point (Mumford–Tate group a torus) it is known that the Hodge structure looks like a piece of the cohomology of a CM abelian variety, but only as a Hodge structure, not as a motive. Closing this gap is equivalent (by KOU) to the full field-of-definition statement, and is a necessary sub-problem of HC.

**C4. HC is not an inequality.** Demailly's positivity formulation (strongly positive $(p,p)$-currents with Hodge class are limits of effective cycles) is false (Babaee–Huh 2017). Approaches through currents, mass, or convexity cannot work as stated.

**C5. The generic fibre is never where the problem is.** By Deligne's fixed-part theorem and big-monodromy results, a very general member of a family has only the Hodge classes coming from the total space. The conjecture lives on the countable union of proper algebraic subvarieties of moduli that make up the Hodge locus. Any proof must work *at* a component of the Hodge locus; methods that only see the generic fibre (monodromy, generic Mumford–Tate groups) prove only trivial cases. Baldi–Klingler–Ullmo (2023) make the geography of these components precise (in level $\ge3$ finitely many positive-dimensional components; in level $1,2$ either none or a dense set).

---

## 3.3 Strategy-by-strategy assessment

| Strategy | What it has delivered | Where it is stuck | Assessment |
|---|---|---|---|
| **S1. Semiregularity / deformation of sheaves** (Bloch, Buchweitz–Flenner, BEK, Markman) | All abelian varieties of dimension $\le5$; $K3^{[n]}$ Hodge isometries | needs seeds and unobstructedness; the variational HC itself | The one strategy with live momentum. Next natural targets: Weil-type sixfolds of discriminant $+1$, the general $2n$-fold case of Markman's program, real multiplication on K3 surfaces. |
| **S2. Motivic formalism** (standard conjectures, André's motivated cycles, Jannsen) | a clean *reduction*: HC $\iff$ (Hodge = motivated) + Lefschetz $B$; Lefschetz $B$ for abelian, hyper-Kähler, complete intersections | "Hodge $\Rightarrow$ motivated" is as hard as HC; $B$ open in general | Indispensable language, not a proof strategy on its own. |
| **S3. Hodge loci + arithmetic + o-minimality** (CDK, Voisin, BKT, KOU, BKU) | every unconditional structural theorem since 1995 | the special points (C3) | The right framework for the "transcendental half". A proof of the Galois statement for special points of VHS of abelian or Fermat/CM type would be real progress. |
| **S4. Analytic / positivity** | nothing for the rational conjecture | C4 | Dead as a proof strategy; still useful for counterexample searches. |
| **S5. Degenerations / tropical** (Kontsevich, Zharkov, Engel et al.) | spectacular *negative* results for integral variants; a constraint on maximal degenerations of Weil-type families (arXiv:2609.14169) | the first candidate counterexamples (Weil 4-folds, discriminant $-1$ 6-folds) are now theorems | Mild evidence *for* HC in the Weil case; the "tropical Hodge conjecture" (Zharkov) would close the counterexample route entirely. |
| **S6. Explicit / computational** (Fermat, Delsarte, CM) | HC for Fermat varieties of degree $<65$ except 44, 51, 52 (all dimensions), fourfolds of odd degree $\le199$; this repository's tables | each new degree may need new cycles (Aoki's phenomenon; see `04-fermat-computations.md`) | Excellent for verification and for sharpening conjectures; cannot reach the general statement. |
| **S7. Counterexample hunting** | the historical candidates were Weil classes | Markman closed dimension $4,5$; Kontsevich's route blocked in dimension 6 for discriminant $-1$ | If a counterexample exists, Weil-type sixfolds of discriminant $+1$, non-Weil exceptional classes in dimension $\ge6$, RM classes on $K3\times K3$ and Hodge classes on sextic fourfolds are where to look. Nothing known points to one. |
| **S8. Large-scale automated search / AI** | the September–October 2026 episode produced rumours and an unverified manuscript on CM abelian varieties | no verified theorem | This session is an instance: a language model can organise, recompute and check, but has no access to a mechanism absent from M1–M6. |

---

## 3.4 Checklist: what any correct proof must deliver

A correct proof of HC establishes, as corollaries, each of the following. A manuscript that cannot say which of its steps delivers them is not a proof.

1. **Absoluteness.** All Hodge classes are absolute Hodge; in particular the Galois conjugate of a zero-dimensional component of a Hodge locus (in a family over $\overline{\mathbb{Q}}$) is again a component.
2. **Lefschetz standard conjecture $B$** for every smooth projective variety; consequently (in characteristic 0) homological and numerical equivalence agree and the Künneth projectors are algebraic.
3. **The variational Hodge conjecture.**
4. **All the special cases that are currently open**: CM abelian varieties, Weil classes in every dimension and discriminant, real-multiplication classes on $K3\times K3$, the Fermat sixfold of degree 44, codimension-2 classes on sextic fourfolds.
5. **A visible break with the false variants**: an identifiable step that uses $\mathbb{Q}$-coefficients (C1) and an identifiable step that uses projectivity (C2).

---

## 3.5 Concrete open problems where progress is realistic

* **P1. Weil classes beyond dimension 5.** Markman's ICM survey lays out a strategy for polarized abelian varieties of split Weil type in all dimensions; the sixfold case with discriminant $+1$ and the general $2n$-fold case are the stated targets.
* **P2. Real multiplication on K3 surfaces.** For $E=\mathrm{End}_{HS}(T(S))$ totally real, the classes on $S\times S$ induced by $E$. Hodge isometries are algebraic (Buskin), but RM endomorphisms are self-adjoint, not isometric. Through Kuga–Satake these classes become algebraic on $KS(S)\times KS(S)$ (Deligne); what is missing is the algebraicity of the Kuga–Satake correspondence itself, known only in special cases.
* **P3. Fermat varieties of degree 44, 51, 52.** A finite combinatorial problem plus possibly new cycle constructions; a 2026 preprint claims it. Re-verifying the published closure criteria on an independent implementation (this repository's `hodge.fermat` is a start) is a well-defined project.
* **P4. Special points.** Prove the Galois statement for zero-dimensional atypical components of variations of Hodge structure whose generic Mumford–Tate group is of abelian type, or for Fermat/CM-type families — any setting with a usable theory of complex multiplication.
* **P5. Algebraization along Hodge loci.** Given a sheaf $\mathcal F$ on $X_0$ whose Chern character is semiregular, Buchweitz–Flenner give a formal deformation of $\mathcal F$ along the Hodge locus; the question is which non-semiregular seeds can be replaced by semiregular ones (e.g. by passing to moduli spaces or to twisted sheaves), which is what Markman does by hand in each case.
* **P6. Sextic fourfolds.** The Noether–Lefschetz components of the moduli of sextic (Calabi–Yau) fourfolds through the Fermat point are computable (Movasati's program); identifying a component where no algebraic representative of the Hodge class is known would isolate a minimal open case of HC for hypersurfaces.

---

## 3.6 Assessment

The Hodge conjecture is open, with no known approach that scales beyond special geometry. The last decade's genuine progress came from two directions: Markman's deformation-theoretic constructions, which settled the classical test cases (Weil classes in dimension 4 and 5), and the o-minimal/arithmetic study of Hodge loci, which settled everything about *where* Hodge classes live except at special points. Both directions have clearly identified next steps (P1–P6) and neither has any visible route to the general statement. A proof, if one exists, must contain a theory of complex multiplication for arbitrary period domains (C3) and a cycle-producing mechanism that is not in M1–M6. Nothing in this session, and nothing in the 2026 literature I could read, supplies either.
