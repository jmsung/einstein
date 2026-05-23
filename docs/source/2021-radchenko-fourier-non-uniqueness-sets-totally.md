---
type: source
kind: paper
title: Fourier non-uniqueness sets from totally real number fields
authors: Danylo Radchenko, Martin Stoller
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2108.11828v3
source_local: ../raw/2021-radchenko-fourier-non-uniqueness-sets-totally.pdf
topic: general-knowledge
cites:
---

# arXiv:2108.11828v3[math.NT]8Jun2022

## FOURIER NON-UNIQUENESS SETS FROM TOTALLY REAL NUMBER FIELDS

DANYLO RADCHENKO AND MARTIN STOLLER

Abstract. Let K be a totally real number ﬁeld of degree n ≥ 2. The inverse diﬀerent of K gives rise to a lattice in Rn. We prove that the space of Schwartz Fourier eigenfunctions on Rn which vanish on the “component-wise square root” of this lattice, is inﬁnite dimensional. The Fourier non-uniqueness set thus obtained is a discrete subset of the union of all spheres √mSn−1 for integers m ≥ 0 and, as m → ∞, there are ∼ cKmn−1 many points on the m-th sphere for some explicit constant cK, proportional to the square root of the discriminant of K. This contrasts a recent Fourier uniqueness result by Stoller [17, Cor. 1.1]. Using a diﬀerent construction involving the codiﬀerent of K, we prove an analogue for discrete subsets of ellipsoids. In special cases, these sets also lie on spheres with more densely spaced radii, but with fewer points on each.

We also study a related question about existence of Fourier interpolation formulas with nodes “

√

Λ” for general lattices Λ ⊂ Rn. Using results about lattices in Lie groups of higher rank we prove that if n ≥ 2 and a certain group ΓΛ ≤ PSL2(R)n is discrete, then such interpolation formulas cannot exist. Motivated by these more general considerations, we revisit the case of one radial variable and prove, for all n ≥ 5 and all real λ > 2, Fourier interpolation results for sequences of spheres

2m/λSn−1, where m ranges over any ﬁxed coﬁnite set of non-negative integers. The proof relies on a series of Poincar´e type for Hecke groups of inﬁnite covolume and is similar to the one in [17, §4].

Contents

- 1. Introduction 1
- 2. Proof of Theorem 2 7
- 3. Proof of Theorem 1 12
- 4. Group theoretic obstructions to interpolation 15
- 5. Interpolation result via Hecke groups with inﬁnite covolume 19


- Appendix A. Proof of the upper bounds (5.4) and (5.5) in Theorem 3 24
- Appendix B. Removing ﬁnitely many interpolation nodes 25
- Appendix C. Proof of Proposition 4.1 27 References 28


1. Introduction

The subject of this paper is motivated by recent work on Fourier uniqueness and non-uniqueness pairs. Broadly speaking, we are interested in the following general question. Given a space V of continuous integrable functions on Rn and two subsets A,B ⊂ Rn, when is it possible to recover any function f ∈ V from the restrictions f|A and f|B (where f denotes the Fourier transform of f)? In other words, we are interested in conditions on A,B,V , under which the restriction map f  → (f|A, f|B) is injective. When the map is injective, we say that (A,B) is a (Fourier) uniqueness pair and if A = B,

Date: June 9, 2022.

1

we simply say that A is a (Fourier) uniqueness set. Conversely, if the map is not injective, we call (A,B) a non-uniqueness pair, and when A = B we call A a non-uniqueness set. Naturally, one would like the function space V to be as large as possible and the sets A and B to be as small as possible, or “minimal” in a certain sense.

A prototypical example of a minimal Fourier uniqueness set was found by Radchenko and Viazovska in [12], where they proved that, when V = Seven(R) is the space of even Schwartz functions on the real line, the set A = Z+ := {

√n : n ∈ Z≥0} is a uniqueness set and established an interpolation theorem in this setting. The result is sharp in the sense that no proper subset of A remains a uniqueness set for Seven(R). Their proof was based on the theory of classical modular forms, which is also well-suited to treat the case V = Srad(Rn) of radial Schwartz functions on Rn and the set A = Un := ∪m∈N0

√mSn−1. For the latter generalization, we refer to §2 in [13], which deduces the result from [4].

The second author recently proved an interpolation formula [17, Thm 1] generalizing the one by Radchenko–Viazovska also to non-radial functions, that is, to the space V = S(Rn) and the same set of concentric spheres Un. However, for n > 1, it is no longer minimal. Indeed, the (related) interpolation formula in [13, Eq. (4.1)] implies that the space of f ∈ S(Rn) satisfying f(x) = f(x) = 0 for all x ∈ ∪m≥N

√mSn−1 is ﬁnite-dimensional for all N and is in fact contained in H4N+2 ⊗ W for some ﬁnite-dimensional space W ⊂ Srad(Rn), where Hk denotes the space of harmonic polynomials on Rn of degree ≤ k. Since a generic subset of dimHk points in rSn−1 is an interpolation set for the space Hk (in the sense that any polynomial p ∈ Hk is uniquely determined by its values on dimHk generic points), this implies that there is a uniqueness set properly contained in Un that contains only ﬁnitely many points on spheres with radius ≤

√

N.

In fact, it was recently proved by the second author and Ramos in [13, Rmk 4.1, Cor 4.1] that any discrete and suﬃciently uniformly distributed subset D ⊂ Un remains a uniqueness set for S(Rn). Here, “suﬃciently” means that D ∩

√mSn−1 contains at least Cnmc

nm many points.

We contrast these Fourier uniqueness results by providing two families of discrete non-uniqueness sets in Rn, where one of them is again contained Un, while the other lies in a union of ellipsoids. Both of them are constructed from lattices corresponding to ideals in totally real number ﬁelds K/Q of degree n and their density grows with the discriminant of K (although their distribution is not uniform, in the sense that they “avoid” points near the coordinate axes; see Figure 1). We give the precise formulations in the next subsection. Thus, characterizing the discrete Fourier uniqueness sets contained in Un seems to be a subtle question.

In fact, the motivation for this work was not to ﬁnd negative results in this direction, but to try to generalize the modular form theoretic approach of Radchenko and Viazovska to treat not necessarily radial functions on Rn, in a way that is very diﬀerent from the approach taken by Stoller (who essentially reduces the problem again to the case of radial Schwartz functions). More speciﬁcally, we were interested in (possible) interpolation formulas where we replace the set of nodes A = Z+ by “square roots” of certain lattices coming from totally real number ﬁelds K, speciﬁcally, the codiﬀerent OK∨ of their ring of integers OK. In this set up, it seemed natural to ask whether one could be working with Hilbert modular forms and associated integral transforms, similarly to the proof by Radchenko–Viazovska.

As we will explain more in §4 and brieﬂy in §1.6, there is an obstruction to the existence of such interpolation formulas. From the more general point of view taken in §4, the obstruction arises because, for n ≥ 2, subgroups of PSL2(R)n that are commensurable to the Hilbert modular group PSL2(OK) are irreducible lattices and can therefore never contain subgroups of ﬁnite index with inﬁnite abelianization, by Margulis’ normal subgroup theorem. On the other hand the presence of certain unfavorable relations

in the Hilbert modular group can be exploited in an explicit manner to obtain the non-uniqueness sets indicated in the abstract.

- 1.1. Statement of non-uniqueness results. We prepare for the formulation of our main nonuniqueness results and at the same time, introduce some notation that will be used throughout the


paper. Let K be a totally real number ﬁeld of degree n ≥ 2 with ring of integers OK. Some of the objects we will introduce depend on the number ﬁeld K, but we will not always display this dependence in our notation.

We denote the n real embeddings by σj : K → R, 1 ≤ j ≤ n and assemble them into the map σ : K → Rn, σ(x) = (σ1(x),...,σn(x)). We recall that the trace of an element x ∈ K is given by Tr(x) = TrK/Q(x) = nj=1 σj(x). For any OK-submodule a ⊂ K we write

a∨ = x ∈ K : TrK/Q(ax) ∈ Z for all a ∈ a

for its dual with respect to the trace paring. As is well-known, if a is a fractional ideal in K, then σ(a) ⊂ Rn is a lattice and σ(a∨) = σ(a)∨, where on the right we mean the dual lattice in the usual sense. Moreover, the covolume of σ(a) is given by

covol(σ(a)) = N(a) |disc(K)|, (1.1)

where N(a) ∈ Q>0 is the ideal norm of a (the unique extension of the absolute norm on integral ideals to all fractional ideals of K) and |disc(K)| = covol(σ(OK))2 is the discriminant of K. For any fractional ideal a ⊂ K we deﬁne

√a := σ(a) := (x1,...,xn) ∈ Rn : (x21,...,x2n) = σ(α) for some α ∈ a ⊂ Rn (1.2) (which is not to be confused with the radical of an ideal). Recall that the codiﬀerent (or inverse diﬀerent) of K is the fractional ideal OK∨ and that the diﬀerent d = dK is deﬁned as d = (OK∨ )−1. We see that the points OK∨ lie on spheres √mSn−1 with non-negative integers m, the traces of the totally non-negative elements in OK∨ (recall that an element x ∈ K is said to be totally non-negative (resp. totally positive) if σj(x) ≥ 0 (resp. σj(x) > 0) for all j = 1,...,n). We return to these points in §1.2.

For f ∈ L1(Rn) we normalize its Fourier transform by f(ξ) = R

f(x)e−2πi x,ξ dx, ξ ∈ Rn. We

n

sometimes also use the notation F(f) = FRn(f) = f. Finally, we write H = {z ∈ C : Im(z) > 0} for the upper half plane.

- Theorem 1. Let K be a totally real number ﬁeld of degree n ≥ 2 as above. Let V ⊂ S(Rn) denote


nx2n with zj ∈ H, xj ∈ R. Then for any ∈ {±1} the subspace of all f ∈ V satisfying f(x) = 0 for all x ∈ OK∨ and f =  f is inﬁnite

1x21 ···eπiz

the subspace linearly spanned by all Gaussians eπiz

dimensional.

- Remark 1.1. Since the space of Fourier eigenfunctions vanishing on OK∨ is inﬁnite-dimensional we can obtain nontrivial functions vanishing in addition on an arbitrary ﬁnite subset of Rn, by a simple linear algebra argument. A similar remark applies to Theorem 2 below.


Besides points on spheres √mSn−1, our methods also allow us to treat other sets related to the diﬀerent, which in general lie on ellipsoids. To formulate it, we appeal to a Theorem of Hecke [7, §63, Satz 176], asserting that the diﬀerent d deﬁnes a square in the ideal class group of K. This means that we can choose a fractional ideal a and a scalar c ∈ K× such that

ca2 = d−1. (1.3)

Let us then deﬁne the set

E(c,a) := x ∈ Rn : ∃α ∈ a2 such that σ(α) = (x21/|σ1(c)|,...,x2n/|σn(c)|) . (1.4) Note that this is a discrete subset of a union of ellipsoids in Rn.

- Theorem 2. Let K, n, and V be as in Theorem 1 and let c and a be such that (1.3) holds. Then, for every ∈ {±1} the subspace of all f ∈ V satisfying f(x) = 0 for all x ∈ E(c,a) and f =  f is inﬁnite dimensional.


The functions we produce for Theorems 1 and 2 are quite explicit. The prototypical example is a linear combination of 16 Gaussians whose parameters z ∈ Hn are of the form z = γ · τ for a generic point τ ∈ Hn and some special elements γ ∈ PSL2(OK), eight of which are written down explicitly in the proof of Proposition 2.1. The entries of the matrices can be computed if one knows some non-trivial units of OK in the congruence classes 1 + 4OK and 1 + 3OK.

In the remaining parts of this introduction we give further explanations for Theorems 1 and 2 and add a few remarks. In §1.6, we describe the other two results indicated in the abstract.

√

√

√mSn−1 is 2n times the number of totally non-negative elements in d−1 of trace m ≥ 0. By choosing a Z-basis for OK containing 1 and considering the element α1 ∈ K such that the Q-linear functional y  → Tr(α1y) takes the value 1 on y = 1 and zero on all other elements of the basis, we see that Tr(α1) = 1 and α1 ∈ d−1. It follows that for all m ∈ Z, we have

√mSn−1. The cardinality of

d−1 ∩

d−1 ∩

- 1.2. On the number of points in


{α ∈ d−1 : Tr(α) = m} = mα1 + (d−1)0, (d−1)0 := {α ∈ d−1 : Tr(α) = 0}. Thus, for m ≥ 0, the subset of Rn whose cardinality we are interested in, can be written as

mσ(α1) + σ((d−1)0) ∩ [0,∞)n whose cardinality equals that of

σ((d−1)0) ∩ m([0,∞)n − σ(α1))

which is the set of lattice points of σ((d−1)0) ⊂ {x ∈ Rn : ni=1 xi = 0} in a homogeneously expanding (n − 1)-dimensional region, allowing for an application of a standard estimate of the number of such

points, as m → ∞. The necessary volume computations are done (for any fractional ideal, in fact) in the work of Ash and Friedberg, see [1, §5, Prop. 5.1 and §6]. From the cited parts of their work, we deduce that

√

√mSn−1 = 2n |disc(K)| (n − 1)!

mn−1 + O(mn−2), m → ∞, (1.5)

d−1 ∩

where the implied constant may depend on K and n. We point out the following features of this asymptotic formula:

- • The surface area of √mSn−1 grows like m

n−1

2 , so the points are more densely spaced than a constant number of points per unit surface area on Sn−1.

- • We may increase the density of points by a constant factor, by taking the discriminant of K arbitrarily large, while keeping the degree n ﬁxed.
- • For small m, there may be no points in


√

√mSn−1, but note that we can add any ﬁnite set of points on these small spheres, by Remark 1.1.

d−1 ∩

![image 1](<2021-radchenko-fourier-non-uniqueness-sets-totally_images/imageFile1.png>)

![image 2](<2021-radchenko-fourier-non-uniqueness-sets-totally_images/imageFile2.png>)

Figure 1. Non-uniqueness sets constructed from Q(√17) and Q(√257)

- 1.3. The relation between Theorem 1 and Theorem 2. If the number c in (1.3) can be taken totally positive, then E(c,a) = OK∨ and both theorems give the same result. Since we are free to

replace c by εc for any unit ε ∈ OK×, we can take c totally positive, provided K has units ε of all possible sign patterns (σj(ε)/|σj(ε)|)1≤j≤n ∈ {±1}n. In the real quadratic case, the latter is equivalent to the fundamental unit having norm −1. Such conditions are studied more generally in the literature, via the notion of signature rank.

In fact, whenever K/Q is Galois and n is odd, then c = 1 is admissible. In other words, the diﬀerent is then exactly equal to the square of another ideal. This follows from Hilbert’s formula, see [10, Ex. 5.45, p. 253].

Generally, recall that a large class of number ﬁelds which allows for an easy determination of admissible c and a in (1.3) is given by monogenic number ﬁelds. For example, for any irreducible monic polynoimal P ∈ Z[X] with square-free discriminant and no complex roots, we can take K = Q(α) ⊂ R for some root α of P. Then it is well-known that OK = Z[α] and OK∨ = P 1 (α)OK, so that (c,a) = (1/P (α),OK) is admissible in (1.3).

We note further that, if there is a constant θ > 0 so that |σj(c)| = θ for all j = 1,...,n, then the set E(c,a) is contained in the union of spheres

√

θmSn−1 (rather than in a union ellipsoids). This happens for some real-quadratic ﬁelds, see §1.4.

- 1.4. Real quadratic ﬁelds. To illustrate the theorems in the case n = 2, consider a real quadratic


√

√

ﬁeld K = Q(

D) as a subﬁeld of R of discriminant D,

D > 0 and for x ∈ K write σ1(x) = x and σ2(x) =: x so that

√

√

√

√

D. Then OK = Z + Zω

D = −

D. Deﬁne ω := (D +

D)/2 and c := 1/

and OK∨ = cOK = cOK2 (square of a fractional ideal). Thus, every element of OK∨ may be written as α = c( + mω) for  ,m ∈ Z and has Tr(α) = Tr(c) + mTr(ωc) = m. The element α is totally non-negative if and only if m ≥ 0 and −mω ≤ ≤ −mω . This shows that

√

√mS1 = 2|Z ∩ [−mω,−mω ]| ∼ 2m

OK∨ ∩

D, m → ∞,

which exempliﬁes (1.5) and Theorem 1 in the simplest case.

Let us now illustrate Theorem 2 with a = OK and the above value of c, which is not totally positive and satisﬁes |σ1(c)| = |σ2(c)| = √1D. We assume that 4|D and set d := D/4 ≡ 2,3 (mod 4), so that OK = Z + Z

√

d. Then E(c,a) is the set of x = (x1,x2) ∈ R2 such that

√

√

- 1

- 2


(x21,x22) =

√

d,a − b

a + b

d

d

√

for some a,b ∈ Z satisfying |b

d| ≤ a and x21 + x22 = √ad. In other words, E(c,a) is a discrete subset of a union of circles of radii a/

√

√

d, for all integers a ≥ 0 with about a/

d many points on each. If D ≡ 1 (mod 4), then E(c,a) is a discrete subset of the union of all circles of radii t/

√

D for all integers t ≥ 0 with about 2t/

√

D points on each.

- 1.5. A minor generalization of Theorem 1. The space of Gaussians deﬁned in Theorem 1 is a subspace of the space of Schwartz functions on Rn that are even in each variable (and it turns out to be dense in that space, see Proposition 4.1). More generally, Theorem 1 holds and will be proved in the following setting.

Let d,n ≥ 1 be integers and consider a partition d = d1 + ··· + dn of d. We view the Euclidean space Rd as the product space Rd

1

×···×Rd

n

and elements x ∈ Rd as n-tuples x = (x1,...,xn) where xj ∈ Rd

j

. The group O(d1) × ··· × O(dn) embeds block-diagonally into the orthogonal group O(d). Denote by S(Rd)O(d

1)×···×O(dn) the space of Schwartz functions on Rd that are radial in each of the n variables xj ∈ Rd

j

. Such functions can be identiﬁed with functions on [0,+∞)n and we freely use this identiﬁcation to evaluate them on n-tuples of non-negative real numbers. An O(d1) × ··· × O(dn)invariant function on Rd will be said to vanish on OK∨ , if f(x) = 0 for all x ∈ Rd such that (|x1|2,...,|xn|2) = (σ1(α),...,σn(α)) for some α ∈ OK∨ .

Besides the case where all dj are equal, our proof of Theorem 2 does not seem to easily generalize to the more general setting that we have just described, for technical reasons having to do with the existence of automorphic factors, see §2.

- 1.6. General lattices and a radial uniqueness result. As already mentioned above, in §4 we will


√

consider general lattices Λ ⊂ Rn and their square roots

Λ := {(x1,...,xn) ∈ Rn : (x21,...,x2n) ∈ Λ}. In §4.1, we will explain (mainly for motivational purposes) a natural equivalent formulation of a Fourier interpolation formula using the pair of sets (√Λ1,√Λ2) for lattices Λ1,Λ2 ⊂ Rn in terms of generating series, viewed as functions on Hn and describe their modular transformation properties in terms of a certain subgroup Γ(L1,L2) ≤ PSL2(R)n, where Li = 2Λ∨i . We will prove in Proposition 4.3 that, for n ≥ 2, there is no pair of lattices (L1,L2) such that the group Γ(L1,L2) is discrete and at the same time the free inner product of two subgroups of upper- and lower triangular elements isomorphic to L1 and L2 respectively. We prove that the latter property of Γ(L1,L2) is a necessary condition for the existence of such an interpolation formula (Proposition 4.2) and we argue why discreteness might be necessary as well.

From this more general point of view we return in §5 to the case n = 1 and prove:

Theorem (= Theorem 3 + Corollary 5.1 in §5). For all d ≥ 5 and all positive reals α,β such that αβ ≥ 1 the pair

∪m≥1 m/αSd−1,∪m≥1 m/βSd−1 (1.6)

is a Fourier uniqueness pair for S(Rd) and there exists a linear interpolation formula which proves this. Furthermore, if αβ > 1, then (1.6) remains a uniqueness pair after removing any ﬁnite number of spheres from both sides.

The radial interpolation result (Theorem 3) will be proved via a series construction generalizing the

one used in [17] from Γ(2) to the subgroup of PSL2(R) generated by 1 2α 0 1

- 1 0
- 2β 1


,

.

For αβ ≥ 1, it is conjugate in PSL2(R) to a normal subgroup of index two in a Hecke group and is isomorphic to Γ(2). For αβ > 1 these groups have inﬁnite covolume and inﬁnite dimensional spaces of modular forms. The latter fact was proved by Hecke [6, §3] and his construction of linearly independent modular forms allows us to remove ﬁnitely many spheres from (1.6).

- 1.7. Some notation. Besides the notation introduced above, we will also use the following general notation throughout the paper. For z ∈ H, the number z/i belongs to the right half plane H := {w ∈ C : Re(w) > 0} and on it, we always use the branch of the logarithm w  → log(w) that takes real values on (0,+∞). For any z ∈ H and k ∈ C, we thus deﬁne (z/i)k = exp(k log(z/i)). For x ∈ R we deﬁne sgn(x) ∈ {−1,0,1} as sgn(x) = x/|x| if x = 0 and sgn(0) := 0.


In the setting of §1.5 we will work with complex Gaussians, parameterized by points z = (z1,...,zn) ∈ Hn and deﬁned as

1|x1|2 ···eπiz

### n|xn|2, xj ∈ Rd

g(z,x) = eπiz

. (1.7) We sometimes also view g as a map g : Hn → S(Rd)O(d

j

1)×···×O(dn), so that from this point of view g(z)(x) = g(z,x). Moreover, we have, for all z ∈ Hn,

g(z) = (z1/i)−d

1/2 ···(zn/i)−d

n/2g(−1/z), −1/z := (−1/z1,...,−1/zn). (1.8) More speciﬁc notation will be introduced in the body of the paper. Acknowledgments. The second author would like to thank Maryna Viazovska for sharing ideas and techniques during his previous work [17], which were also useful in §5.

2. Proof of Theorem 2

The goal of this section is to prove Theorem 2. In §2.1 we introduce some notation and deﬁne a “theta-subgroup” Γϑ of the Hilbert modular group PSL2(OK). In §2.2 we deﬁne a slash action of the group algebra C[Γϑ] on complex-valued functions on a product of upper and lower half planes, via theta functions. The examples of non-trivial functions satisfying the vanishing conditions of Theorem 2 will be given as Gaussians slashed with suitable elements in C[Γϑ]. Lemmas 2.1 and 2.2 will show that “suitable” means to belong to the intersection of two right ideals in C[Γϑ]. In §2.3, we will show that this intersection is inﬁnite dimensional and conclude the proof of Theorem 2 in §2.4.

- 2.1. Hilbert modular groups and subgroups. As in §1, we consider a totally real number ﬁeld K of degree n = [K : Q] ≥ 2. As in (1.3), we choose and ﬁx c ∈ K× and a fractional ideal a ⊂ K so that d−1 = ca2, where d is the diﬀerent of K. Depending upon these quantities we deﬁne signs δj := sgn(σj(c)), a vector of signs δ = (δj)1≤j≤n ∈ {±1}n and


Hnδ := {z = (z1,...,zn) ∈ Cn : Im(δjzj) > 0 for all j ∈ {1,...,n}}. Instead of the ones in (1.7), we will work, for all of §2, with Gaussians

### j=1 δjzjx2j, z ∈ Hnδ , x ∈ Rn. (2.1)

n

gδ(z) ∈ S(Rn) deﬁned by gδ(z)(x) := gδ(z,x) := eπi

We consider the Hilbert modular group Γ := PSL2(OK) and denote S =

- 0 −1
- 1 0


1 β 0 1

ε 0 0 ε−1

, ε ∈ OK× ,

, Tβ =

, β ∈ OK, M(ε) =

viewing these as elements of Γ. Next, we embed Γ into PSL2(R)n via the real embeddings σj. The latter group and hence Γ itself, acts on Hnδ via fractional linear transformations. This action is faithful and we sometimes identify a group element with the associated automorphism of Hnδ , in particular when writing compositions of maps. Deﬁne

Γϑ := {S} ∪ {T2β}β∈OK ∪ {M(ε)}ε∈OK× ≤ Γ.

- Remark 2.1. Let Γ˜ϑ denote the image in Γ of the group of matrices in SL2(OK) which reduce to


∗ 0 ) in SL2(OK/2OK). By deﬁnition, Γϑ ≤ Γ˜ϑ and equality is known to hold (at least) in the case K = Q(√5) (see [8, §1]). Even though it would be convenient, we do not need to know equality in general and only mention it to provide context (but we will also refer to this group in the proof of Proposition 2.1).

(∗ 0

0 ∗) or ( 0 ∗

- 2.2. Automorphic factors and slash action. Our task here is to deﬁne a suitable automorphic


factor and a corresponding slash action of Γϑ on spaces of functions on Hnδ so that the action of S matches with the Fourier transform acting on Gaussians and so that T2β simply acts as translation by 2σ(β). We will use theta functions attached to fractional ideals in K. Essentially the same functions were already studied by Hecke [7, §56].

We deﬁne the function ϑ : Hnδ → C by the absolutely and normally convergent series ϑ(z) := ϑ(z1,...,zn) :=

n

j=1 zjσj(cα2),

eπi

α∈a

where we recall that d−1 = ca2. We next determine the transformation behavior of ϑ under the generators of Γϑ. These are certainly not new, but we include their proofs to keep the presentation self-contained. First, since a is an OK-submodule of K, we have, for every ε ∈ OK×, and every z ∈ Hnδ

ϑ(M(ε)z) = ϑ(σ1(ε)2z1,...,σn(ε)2zn) = ϑ(z). Next, ϑ(T2βz) = ϑ(z) for all z ∈ Hnδ and all β ∈ OK, since for all α ∈ a,

n

n

zjσj(cα2) + 2TrK/Q(βcα2)

(zj + 2σj(β))σj(cα2) =

j=1

j=1

and the above trace is an integer. To study the eﬀect of ϑ under S note that, by deﬁnition, ϑ(z) is the sum over the lattice σ(a) of the Schwartz function fz = gδ(|σ1(c)|z1,...,|σn(c)|zn) whose Fourier transform is

n

n

j(−1/(|σj(c)|zj))ξj2 = |NK/Q (c)|−1/2

j)(1/σj(c))ξj2.

(δj|σj(c)|zj/i)−1/2eπiδ

(δjzj/i)−1/2eπi(−1/z

fz(ξ) =

j=1

j=1

By applying Poisson summation to the function fz and the lattice σ(a) ⊂ Rn, we get ϑ(z) =

1 covol(σ(a))

fz(λ∗)

λ∗∈σ(a)∨

n

1 |NK/Q (c)|1/2 covol(σ(a))

j=1 (−1/zj)(1/σj(c))σj(β)2,

n

(δjzj/i)−1/2

eπi

=

j=1

β∈ca

where we used that a∨ = ca, which follows from multiplying the relation ca2 = d−1, by a−1 and using the general formula b∨ = d−1b−1. Writing β = cα and summing over α ∈ a, the above computation proves

ϑ(z) = (δ1z1/i)−1/2 ···(δnzn/i)−1/2ϑ(Sz)

provided that |NK/Q (c)|covol(σ(a))2 = 1 holds. This in turn follows again from the relation ca2 = d−1, the general volume formula (1.1) and properties of the ideal norm.

We now deﬁne Ωnδ := {z ∈ Hnδ : ϑ(z) = 0}, a nonempty open subset of Hnδ containing the product of the imaginary axes, which is invariant under Γϑ and the 1-cocycle jϑ : Γϑ → Hol(Ωnδ ,C×) by

ϑ(γz) ϑ(z)

jϑ(γ)(z) := jϑ(γ,z) :=

. (2.2)

Here, Hol(Ωnδ ,C×) denotes the abelian group of all nowhere vanishing, holomorphic functions on Ωnδ . Our computations from above and the deﬁnitions imply that, for all β ∈ OK, all ε ∈ OK×, all z ∈ Ωnδ and all γ1,γ2 ∈ Γϑ,

n

(δjzj/i)1/2, jϑ(γ1γ2) = (jϑ(γ1) ◦ γ2) · jϑ(γ1). (2.3)

jϑ(T2β) = 1, jϑ(M(ε)) = 1, jϑ(S,z) =

j=1

It is not strictly necessary for our purposes, but, for convenience, we will lift jϑ to a cocycle jϑ : Γϑ → Hol(Hnδ ,C×). To explain how, note that, by our deﬁnition of Γϑ via generators, and by (2.3), each function jϑ(γ) can we written as a ﬁnite product of functions jϑ(S) ◦ γ over some γ ∈ Γϑ and all of these are everywhere deﬁned, holomorphic and nowhere vanishing on Hnδ . Thus, we can (re-)deﬁne jϑ on generators by requiring that (2.3) holds. Any relation in Γϑ will be respected in Hol(Hnδ ,C×) since the functions expressing the relation must agree on the non-empty open subset Ωnδ ⊂ Hnδ .

Finally, for any function f on Hnδ with values in a complex vector space and any γ ∈ Γϑ, we deﬁne a new function f|γ on Hnδ by

f|γ := jϑ(γ)−1 · (f ◦ γ), that is (f|γ)(z) = jϑ(γ,z)−1f(γ · z). (2.4) We extend this group action to the group algebra R := C[Γϑ] in the usual way.

The next two lemmas hint at the usefulness of the action we just introduced, for the proof of Theorem 2. Indeed, these Lemmas will essentially reduce the proof of Theorem 2 to a purely algebraic statement about a right ideal in the algebra R, which will be addressed in the next section.

- Lemma 2.1. For every A ∈ R and z ∈ Hnδ we have FRn((gδ|A)(z)) = (gδ|SA)(z).

Proof. By linearity, we may assume that A ∈ Γϑ. Given that gδ(z) = jϑ(S,z)−1gδ(Sz) and the properties (2.3),

F((gδ|A)(z)) = jϑ(A,z)−1F(gδ(Az)) = jϑ(A,z)−1jϑ(S,Az)−1gδ(S(Az))

= jϑ(SA,z)−1gδ(SAz) = (gδ|SA)(z),

- as claimed.


We denote by I = β∈O

K

(1 − T2β)R the right ideal generated by all elements (1−T2β), β ∈ OK.

- Lemma 2.2. For all A ∈ I and all z ∈ Hnδ , the function (gδ|A)(z) : Rn → C vanishes at all points x = (x1,...,xn) ∈ Rn for which there is α ∈ a2 such that x2j = |σj(c)|σj(α) for all j, that is to say, at all points of the set E(c,a), deﬁned in (1.4).


Proof. By linearity, may assume that A = (T2β −1)γ for some γ ∈ Γϑ and some β ∈ OK. By deﬁnition and by (2.3), we have

(gδ|(T2β − 1)γ)(z) = (gδ|T2βγ)(z) − (gδ|γ)(z) = jϑ(γ,z)−1(gδ(γz + 2σ(β)) − gδ(γz)). Set τ := γz. Then, for all x = (x1,...,xn) ∈ Rn,

n

j=1 δjσj(β)x2j − 1 gδ(τ)(x). If there is α ∈ a2 so that x2j = |σj(c)|σj(α) for all j, then, since δj = σj(c)/|σj(c)|, we have

gδ(τ + 2σ(β))(x) − gδ(τ)(x) = e2πi

n

n

δjσj(β)x2j =

σj(c)σj(β)σj(α) = TrK/Q(cβα) ∈ Z,

j=1

j=1

because cα ∈ OK∨ and β ∈ OK. This proves what we want.

- 2.3. Ideals in the group algebra R = C[Γϑ]. Lemma 2.1 and Lemma 2.2 together show that, for any element A ∈ R which belongs to the ideal I and which can also be written as A = (1 +  S)A1 for some A1 ∈ R and ∈ {±1} is such that, for any z ∈ Hnδ , the Schwartz function f = (gδ|A)(z) vanishes


- at all points of the set E(c,a) and has Fourier transform f =  f. The next proposition will show that there are plenty of such elements A. It lies at the heart of our proof of Theorem 2 (and Theorem 1).


Proposition 2.1. We have (1 − S)R ∩ I = 0 and (1 + S)R ∩ I = 0. Moreover, these intersections are inﬁnite dimensional vector spaces over C.

Proof. We ﬁrst note that if J ⊂ R is any nonzero right ideal, then, since the group Γϑ is inﬁnite, we can produce an arbitrarily high number of right translates of a single nonzero element in J that have disjoint supports (say), showing that dimC(J ) = ∞. So we only need to show that (1 ± S)R ∩ I = 0.

To do that, we note that if two elements γ1,γ2 ∈ Γϑ have the same bottom row (possibly up to sign), then γ1 −γ2 = (1−γ2γ1−1)γ1 ∈ I. It thus suﬃces to construct A+,A− ∈ R such that (1−S)A− and (1 + S)A+ can be written as non-trivial ﬁnite sums of diﬀerences of group elements with equal bottom row. We also know that left multiplication by S interchanges the rows of a matrix and switches the sign on the top. Guided by these two observations, we make the Ansatz

cr−1 dr−1 cr dr

c r−1 d r−1 c r d r

(−1)rγ r, γ r =

A− =

γr, γr =

### , A+ =

,

r∈Z/2nZ

r∈Z/2nZ

where n ≥ 1 and cr,dr,c r,d r ∈ OK are to be found so that all elements γr,γ r belong to Γϑ and such that 0 = (1 ± S)A± because these elements always belong to I. Some experimentation shows that there are no non-trivial examples for n = 1,2,3 and further experimentation yields an example for n = 4 as follows. Choose a,b,x,y ∈ OK such that

(1 + 4a)(1 + 4x) = 1 = (1 − 3b)(1 − 3y), axby = 0. (2.5)

This is possible by Dirichlet’s unit Theorem, which implies that for all non-zero integral ideals a ⊂ OK, the kernel of the natural map OK× → (OK/a)× is inﬁnite (use this for a = 4OK or 3OK). Consider then the elements γr = γ r deﬁned by

2 −(1 + 4a) 1−4b 1+4a 2b

, γ2 = −1 2a

1 0 0 1

0 1 −1 2a

,

γ0 =

, γ1 =

, γ3 =

2 −(1 + 4a)

- 1−4b 1+4a 2b

- 2y 1+41−4xy


2y 1+41−4xy −(1 + 4x) 2

, γ6 = −(1 + 4x) 2

2x −1 1 0

γ4 =

, γ5 =

, γ7 =

.

2x −1

We claim that: (i) each γr belongs to Γϑ and (ii) that (1 ± S)A± = 0. To prove (i), we ﬁrst verify, by computing determinants and using (2.5), that each γr belongs to the congruence group Γ˜ϑ ⊃ Γϑ deﬁned in Remark 2.1. On the other hand, for r = 4, either one of the diagonal or oﬀ-diagonal entries of γr is a unit, so that, by multiplying γr from the right or the left by Sδ

T2αSδ

with suitable α ∈ OK, δ1,δ2 ∈ {0,1}, we obtain a matrix in Γ˜ϑ one of whose diagonal or oﬀ-diagonal entries is zero and hence belongs to Γϑ. For γ4, note that γ4T2(1+4a) has lower right entry equal to 1 + 4a, which is a unit.

1

2

To verify (ii) note that, since none of a,b,x,y is zero, we have {γr}r∈Z/8Z ∩ {S,1} = {1}, so that the coeﬃcient of 1 ∈ Γϑ in the ﬁnite sum (1 ± S)A± is 1 ∈ C.

Having proved Proposition 2.1 it remains to show that we can produce any number of linearly

independent functions (gδ|A)(z) by varying A ∈ I ∩ (1 ± S)R and z ∈ Hnδ suitably. This will be achieved via the next lemma and its consequences.

- Lemma 2.3. Let c1,...,cm ∈ Cn be pairwise distinct. Then the functions gµ : Rn → C, gµ(r) =


n

j=1 cµ,jrj2, µ = 1,...,m, are C-linearly independent.

e

Proof. We induct on m ≥ 1, the case m = 1 being clear. If m ≥ 2 and mµ=1 tµgµ = 0 for some tµ ∈ C, we divide by g1 and diﬀerentiate with respect to rj, giving mµ=2 2(cµ,j − c1,j)rjtµgµ(r) = 0. By continuity we may also divide by rj and apply the inductive hypothesis to deduce (cµ,j −c1,j)tµ = 0 for all j and µ. Since c1 = cµ for all µ ≥ 2, this implies tµ = 0 for all µ ≥ 2 and then also t1 = 0.

Corollary 2.1. Let z ∈ Hnδ be a point such that for all γ,ω ∈ Γϑ, we have γ = ω ⇒ γz = ωz. Then the map Φz : R → S(Rn), Φz(A) = (gδ|A)(z) is injective. Proof. Suppose that A = γ∈Γ

λγγ ∈ R is such that Φz(A) = 0. Let {γ1,...,γm} = {γ ∈ Γϑ : λγ = 0} be the support of A (with pairwise distinct γi). By assumption, we have 0 = Φz(A) =

ϑ

- m


- i
- jϑ(γi,z)−1g(γiz), so λγ


i=1 λγ

= 0 follows by applying Lemma 2.3 to cµ = πiγµz.

i

There are uncountably many points z ∈ Hnδ satisfying the assumption of Corollary 2.1; let us call such points good (for the ﬁeld K). To see this, note that the set of good points contains (since Γϑ ⊂ Γ)

{z ∈ Hnδ : γz = z} = Hnδ

{z ∈ Hnδ : γz = z} (2.6)

1 =γ∈Γ

1 =γ∈Γ

and that each ﬁx point set in the union on the right is either empty or a singleton set. Since Γ is countable and Hnδ is uncountable, the above set is indeed uncountable. (It is moreover dense in Hnδ , by Baire’s theorem, but we won’t need this fact.) We call a point belonging to the intersection (2.6) a generic point (for the ﬁeld K). Thus, all generic points are good.

- 2.4. Conclusion. We can now give the proof of Theorem 2.


Proof of Theorem 2. Fix ∈ {±1} and a good point z ∈ Hnδ for the ﬁeld K. By Corollary 2.1, the linear map Φz : R → S(Rn), Φz(A) = (gδ|A)(z) is injective. Note that it takes values in the space V ⊂ S(Rn) of all linear combinations of Gaussians. By Proposition 2.1, the space J := I ∩(1+ S)R and hence also Φz(J ) is inﬁnite dimensional. On the other hand, by Lemma 2.1 and Lemma 2.2, the space Φz(J ) is contained in the space of all f ∈ V satisfying f =  f and f(x) = 0 for all x ∈ E(c,a), proving the Theorem.

3. Proof of Theorem 1

In this section we give the proof of Theorem 1. We let, as usual, K be a totally real number ﬁeld of degree n ≥ 2 and use notation associated with it as in §1. We will also use some of the notation and results of §2, in particular, the eight elements γr, r ∈ Z/8Z given in the proof of Proposition 2.1,

- Lemma 2.3 and the notion of a generic point for K, as deﬁned near (2.6) (but with Hnδ replaced by Hn). The entries of the matrices γr depend on a non-trivial solution a,b,x,y ∈ OK to the equation (2.5). Further below, we will need to assume in addition that


all four units (1 + 4a),(1 + 4x),(1 − 3b),(1 − 3y) ∈ OK× are totally positive. (3.1)

This is possible, since the subgroup of totally positive units in OK× is inﬁnite (indeed, already the subgroup of squared units is inﬁnite, by Dirichlet’s unit Theorem).

As advertised in §1.5, we work for all of §3, on Rd = Rd

### × ··· × Rd

and with the corresponding Gaussians g(z) : Rd → C, deﬁned as in (1.7). This will prove a more general statement than Theorem 1. We also ﬁx a sign ∈ {±1} and consider a generic point z = (z1,...,zn) ∈ Hn. We use the short hand notation µ(z) := nj=1 (zj/i)d

1

n

j/2 ∈ C×. For a set of coeﬃcients {λr(z)}r∈Z/8Z ⊂ C which we will determine later, consider the linear combination of Gaussians

hz =

λr(z)g(γrz),

r∈Z/8Z

where the matrices γr ∈ Γ, r ∈ Z/8Z, are as in the proof of Proposition 2.1. We deﬁne and compute, using (1.8),

 λr(z)µ(γrz)−1g(Sγrz)

fz := hz + hz =

λr(z)g(γrz) +

r∈Z/8Z

r∈Z/8Z

λr−1(z)g(γr−1z) +  λr(z)µ(γrz)−1g(Sγrz) .

=

r∈Z/8Z

By construction, fz =  fz. We claim that the coeﬃcients λr(z) can be chosen in such a way that

λr(z) = 0 and  λr(z)µ(γrz)−1 = −λr−1(z) for all r ∈ Z/8Z. (3.2) We postpone the proof of the claim to a later stage. Assuming it, we get

λr−1(z)(g(γr−1z) − g(Sγrz)). (3.3)

fz =

r∈Z/8Z

Each diﬀerence g(γr−1z)−g(Sγrz) vanishes (in the sense deﬁned in §1.5) on OK∨ , since, by construction, Sγr = T2β

### γr−1 for some βr ∈ OK and so Sγrz = T2β

r

γr−1z = γr−1z + 2σ(βr), implying that, if there is α ∈ OK∨ so that |xj|2 = σj(α) for all j, then

r

n

j=1 σj(γr−1)zj|xj|2 1 − e2πi

n

λr−1(z)eπi

j=1 σj(βr)σj(α) = 0,

fz(x) =

r∈Z/8Z

because nj=1 σj(βr)σj(α) = Tr(αβr) ∈ Z.

So far, z was an arbitrary generic point. We now verify that fz = 0 and that we can produce an arbitrary number of linearly independent functions of this form. Since z is generic for K, we have

{r ∈ Z/8Z : γrz = z or Sγrz = z} = {r ∈ Z/8Z : γr = 1 or Sγr = 1} = {0}

### and this shows fz = 0 via Lemma 2.3 and λr(z) = 0 for all r. Assume we have constructed linearly independent fτ

of this form with generic τj ∈ Hn (here, the subscripts do not denote coordinates). Since the set of generic points for K is inﬁnte (indeed uncountable), we can choose a generic point τm+1 ∈ Hn {τ1,...,τm} and the functions fτ

### ,...,fτ

1

m

### are then linearly independent as well. Indeed, if 0 = mi=1+1 tifτ

### ,...,fτ

1

m+1

### = w∈Hn awg(w), for ti ∈ C and (unique) aw ∈ C we ﬁnd that 0 = aτ

= ti for all i, as desired.

i

i

To ﬁnish the proof of Theorem 1, it remains to prove the claim made in (3.2). A short calculation shows that this claim is equivalent to

n

((σj(γr)zj)/i)d

j/2. (3.4)

1 =

µ(γrz) =

r∈Z/8Z

r∈Z/8Z

j=1

Indeed, if (3.4) holds, we can choose an arbitrary constant λ0 = λ0(z) ∈ C× and put λk+8Z(z) = (− )kλ0

µ(γi+8Zz) for 1 ≤ k ≤ 7.

1≤i≤k

Let us denote the product on the right of (3.4) by ρ(z). From the speciﬁc shape of the γr, it is clear that ρ(z)8 = 1. Since Hn is connected, we deduce that the continuous function z  → ρ(z) is constant, with constant value given by an eighth root of unity ρ. To determine ρ, we will take the points zj to i∞. For this we need the following lemma.

- Lemma 3.1. For any g = ac db ∈ SL2(R), we have


((g · (iy))/i)1/2 |g · (iy)|1/2

= exp(−πi4 sgn(ac)) = e(−18 sgn(ac)), (3.5) where we write e(w) = exp(2πiw) and where, here and elsewhere, the conventions of §1.7 are in place.

lim

y→∞

We defer the proof of Lemma 3.1 to the end of this section. Writing ρ =

ρ |ρ|

ρ((iy,...,iy)) |ρ((iy,...,iy))|

= lim

y→∞

and applying formula (3.5) (and using the fact that the dj are integers1) , we see that ρ =

n

e −d8j sgn(σj(crcr−1)) , (3.6)

r∈Z/8Z

j=1

where we recall that cr denotes the lower left entry of γr and cr−1 the upper left entry of γr. Let us write down the eight products crcr−1 appearing in (3.6). For α1,α2 ∈ K, we write α1 ≡ α2 to express that there is a totally positive β ∈ K× so that α2 = α1β. Then, by assumption (3.1),

c0c7 = 0 c1c0 = 0 c2c1 = −2 ≡ −1 c3c2 = 2

1 − 4b 1 + 4a ≡ 1 − 4b

1 − 4b 1 + 4a

(2y) ≡ (1 − 4b)y c5c4 = −(2y)(1 + 4x) ≡ −y c6c5 = −2x(1 + 4x) ≡ −x c7c6 = 2x ≡ x.

c4c3 =

1We arrived at a minor conﬂict of notation: There are dimensions dj ∈ N, j ∈ {1, . . . , n} and elements dr ∈ OK, r ∈ Z/8Z, the entries of the right columns of the elements γr. The dr ∈ OK won’t play a role in the remaining argument.

We introduce the short hands

ηj := sgn(1 − 4σj(b)), ξj = sgn(σj(y)). Interchanging the order of multiplication in (3.6), using the above list of identities and noting that c0c7,c1c0 don’t contribute, while the contributions of c6c5 and c7c6 cancel, we arrive at the formula

n

n

ρ = e(−18Σ), where Σ =

dj(−1 + ηj + ξjηj − ξj) =

dj(ηj − 1)(ξj + 1).

j=1

j=1

We claim that for each j we have (ηj − 1)(ξj + 1) = 0, or equivalently

1 − 4σj(b) > 0 or σj(y) < 0. (3.7) By (2.5), we have (1 − 3b)(1 − 3y) = 1 and hence

(1 − 3σj(b))(1 − 3σj(y)) = 1.

By assumption (3.1), both factors in this product are positive. Assume now that σj(y) > 0. Then the factor (1 − 3σj(y)) belongs to the interval (0,1), implying that the factor (1 − 3σj(b)) belongs to the interval (1,∞) and so −σj(b) > 0. But −σj(b) > 0 implies 1 − 4σj(b) > 1 > 0. We assumed that σj(y) > 0 and deduced 1 − 4σj(b) > 0, which proves (3.7). This ﬁnishes the proof of ρ = 1, hence the proof of the claim made in (3.2) and thus the proof of Theorem 1. It only remains to prove Lemma

- 3.1.


Proof of Lemma 3.1. We need to show that for all g = ac db ∈ SL2(R), we have lim

arg(−π/4,π/4) ((g · (iy))/i)1/2 = −π4 sgn(ac). (3.8)

y→∞

Both sides of (3.8) are unchanged if we replace g by −g, so we may assume c ≥ 0 for the veriﬁcation. For y > 0, we abbreviate

aiy + b −cy + id ∈ H := {w ∈ C : Re(w) > 0}. In this proof, any asymptotic notation refers to taking y → ∞. If c = 0, then ad = 1 and we have

w(y) := (g · (iy))/i =

a2(iy) + ab i

= −b ay −→ 0,

a(iy) + b id

Im(w(y)) Re(w(y))

= a2y − iab, hence

w(y) =

=

which shows that that argument of w(y) and hence that of w(y)1/2, goes to zero, as claimed. If c > 0 and a = 0, then −bc = 1 and we have

b2 y + dbi

b2y y2 + (db)2 −

b2(db)i y2 + (db)2

= −db

b −cy + di

Im(w(y)) Re(w(y))

y −→ 0, as claimed. Assume now that c > 0 and that a = 0. Then

w(y) =

=

=

, hence

1 i

a c −

1 c(c(iy) + d)

= (−i)(a/c) + o(1). We deduce that

w(y) =

- • if a > 0, then arg(w(y)) → −π/2, hence arg(w(y)1/2) → −π/4, as claimed.
- • if a < 0, then arg(w(y)) → π/2, hence arg(w(y)1/2) → π/4, as claimed.


This ﬁnishes the proof of (3.8) and thus the proof of Lemma 3.1.

4. Group theoretic obstructions to interpolation In this section, we generalize the setting we have been studying so far in the following way. We

replace the (embedded) codiﬀerent σ(OK∨ ) ⊂ Rn of a totally real ﬁeld K and its square root σ(OK∨ ) ⊂ Rn by a general lattice Λ ⊂ Rn and its square root

√

Λ := {(x1,...,xn) ∈ Rn : (x21,...,x2n) ∈ Λ}.

To motivate looking at possible Fourier uniqueness or non-uniqueness sets of this shape, we give below in §4.1 a translation of a general Fourier interpolation problem with uniqueness pairs of the form (√Λ1,√Λ2), to the problem of ﬁnding certain holomorphic functions on Hn having modular transformation behavior with respect to a certain subgroup Γ(L1,L2) ≤ PSL2(R)n, where Li = 2Λ∨i . Ideally, we would want this group to be discrete and at the same time isomorphic to the free product L1∗L2. In Proposition 4.3 below we show that, for n ≥ 2, this can never happen. The results of §4 will not be used elsewhere in this paper, but may be of independent interest and provide further context and motivation.

## 4.1. Generating series and functional equations. Adopt the general setting of §1.5. Thus,

- n,d,d1,...,dn ≥ 1 are integers and d = d1 + ··· + dn. Fix two lattices Λ1,Λ2 ⊂ Rn and for i = 1,2, deﬁne Λi,+ := Λi ∩[0,∞)n. We want to know whether there exist functions aλ,a˜µ : Rn → C such that


for all f ∈ S(Rd)O(d

1)×···×O(dn) and all x = (x1,...,xn) ∈ Rd, f(x1,...,xn) =

√

a˜µ(|x1|,...,|xn|) f(√µ), (4.1)

aλ(|x1|,...,|xn|)f(

λ) +

µ∈Λ2,+

λ∈Λ1,+

√

λ := (√λ1,...,√λn) for λ = (λ1,...,λn).

where we used the notation

Let us ﬁrst assume that such functions aλ,a˜µ exist and that, for each ﬁxed r = (r1,...,rn) ∈ [0,+∞)n, they grow at most polynomially in their index parameters λ ∈ Λ1 and µ ∈ Λ2 respectively. We consider the generating functions

aλ(r)eπi

F(z,r) =

λ∈Λ+,1

n

i=1 ziλi, F˜(z,r) =

a˜µ(r)eπi

µ∈Λ2,+

n

i=1 ziλi, z ∈ Hn. (4.2)

By construction, each of these functions is holomorphic in z and periodic with respect to the lattices 2Λ∨1 or 2Λ∨2 respectively. Moreover, applying the formula (4.1) to the Gaussian f = g(z), as deﬁned in (1.7), shows that

n/2F˜(−1/z,r). (4.3)

g(z,r) = F(z,r) + (z1/i)−d

1/2 ···(zn/i)−d

Conversely, no longer assuming the existence of aλ,a˜µ but the existence of holomorphic 2Λ∨1 -periodic functions z  → F(z,r) and holomorphic 2Λ∨2 -periodic functions z  → F˜(z,r) satisfying suitable growth conditions, which are related via the functional equations (4.3) and with Fourier expansions indexed over Λi,+ only (instead of the whole Λi), we can deduce an interpolation formula (4.1) by making use of the following Proposition.

- Proposition 4.1. The linear span of all Gaussians g(z), z ∈ Hn is dense in S(Rd)O(d


1)×···×O(dn)

Proof. We defer this proof to the Appendix C, as we will not need it for n ≥ 2, but it seems worth recording. For n = 1, this is also contained in [5, Lemma 2.2].

- 4.2. Group theoretic and modular considerations. The modular transformation properties of the generating functions F˜ and F deﬁned above are governed by a certain subgroup of PSL2(R)n acting on Hn, depending upon the lattices Λ1,Λ2 ⊂ Rn (but not on the dimensions dj) which we deﬁne next. In the notation of §2, this subgroup can be thought of as the analogue of the subgroup of


PSL2(OK) generated by all elements T2β,ST2βS, β ∈ OK in the case where Λ1 = Λ2 = σ(OK∨ ).

Instead of working with PSL2(R)n, we ﬁnd it more convenient to work with the isomorphic group G := PSL2(Rn), where Rn = R×···×R is viewed as commutative ring with component wise addition and multiplication. For x ∈ Rn we deﬁne

1 x 0 1

1 0 x 1 ∈ G, (4.4)

Tx :=

, V x :=

where 0 = (0,...,0), 1 = (1,...,1). We also deﬁne the element S := 01 −01 ∈ G, so that STxS = V −x. For any lattice L ⊂ Rn, we deﬁne the following subgroups of G:

Γupp(L) := {Tx : x ∈ L} ∼= L, Γlow(L) := {V y : y ∈ L} ∼= L and then, for any two lattices L1,L2 ⊂ Rn, we also deﬁne the subgroup

Γ(L1,L2) := Γupp(L1) ∪ Γlow(L2) ≤ G.

The subgroup relevant to the setting described in §4.1 is then Γ(L1,L2), where Li = 2Λ∨i . To explain this, let us suppose that we are given a cocycle J : G → Hol(Hn,C×) satisfying J(Tx) = 1 for all

x ∈ Rn and J(S)(z) = nj=1 (zj/i)d

j/2. We may then deﬁne a slash action of G (and its group algebra C[G]) on functions f on Hn by f|γ := J(γ)−1 · (f ◦ γ), γ ∈ G, similarly to §2.

In practice, it suﬃces that J can be deﬁned only on the subgroup generated by Γ(L1,L2) and S, but its existence is non-trivial and may not always be guaranteed, compare with §2. On the other hand, when 8|dj for all j, such a cocycle J can be deﬁned on the full group G, namely, we deﬁne JG;d

1,...,dn(g) = nj=1(g j)−d

j/4, where g = (g1,...,gn), and g j is the derivative of the M¨bius transformation gj.

Now consider the functions F, F˜ introduced in §4.1. In what follows we will suppress the parameters r ∈ [0,∞)n and z ∈ Hn from the notation. Using the slash action just introduced, F and F˜ (as functions on Hn) must satisfy, besides certain growth conditions,

F|(Tx − 1) = 0 for all x ∈ L1, F˜|(Ty − 1) = 0 for all y ∈ L2, F + F˜|S = g, where g is the Gaussian (1.7). It suﬃces to ﬁnd only F such that

F|(Tx − 1) = 0 for all x ∈ L1, F|(V y − 1) = g|(V y − 1) for all y ∈ L2. Indeed, we can then deﬁne F˜ as F˜ = g|S − F|S and this function will be L2-periodic.

We see from the above cohomological formalism that any relation between elements in the group Γ(L1,L2) imposes a condition on the 1-cocycle Φ : γ  → F|(γ−1). There are trivial relations that come from the fee abelian subgroups Γupp(L1) and Γlow(L2) that are always respected. There is, however, no reasons why a “mixed” relation between elements of these two groups should hold, as such a relation translates to non-trivial conditions for the Gaussian g. Thus, one would like that

Γ(L1,L2) is the free inner product of Γupp(L1) and Γlow(L2). (F)

- A natural further desideratum is: Γ(L1,L2) is discrete in G ∼= PSL2(R)n. (D)


In fact, the existence of F and F˜ with the above transformation properties implies (F) by the following proposition.

- Proposition 4.2. Assume that there exist functions F and F˜ as in (4.2) satisfying (4.3). Then condition (F) holds. Proof. By way of contradiction, assume that (F) fails and consider a non-trivial relation


### Tx

### ···V y

### Tx

### V y

### Tx

V y

= 1

m

m

2

2

1

1

with m ≥ 1 minimal and with x1,...,xm ∈ L1, y1,...,ym ∈ L2, all nonzero (by conjugation with some Tx or V y if necessary, we can bring any minimal non-trivial relation into the above form). Consider the cocycle Φ(γ) = F|(γ − 1) as above and apply the cocycle property Φ(γ1γ2) = Φ(γ1)|γ2 + Φ(γ2) repeatedly, to obtain

m

m

Φ(V y

(g|V y

### Pi − g|Pi), Pi := Tx

### V y

### ···V y

### Tx

)|Pi =

0 = Φ(1) =

. (4.5)

i

i

i

i+1

m

m

i=1

i=1

Since xm = 0, all 2m group elements V y

Pi,Pi are pairwise distinct by minimality of m. Thus, we

i

have an identity 0 = 2j=1m δjJ(γj)−1g(γj) with δj ∈ {±1} and with pairwise distinct γj ∈ Γ(L1,L2). We obtain the desired contradiction by specializing this identity to some point z ∈ Hn, which is not

ﬁxed by any γiγj−1 for i = j and invoking Lemma 2.3.

- Remark 4.1. In the above proof we assumed the existence of the automorphy factor J deﬁned on the group Γ(L1,L2). When J is not well-deﬁned we can modify the argument to obtain the same conclusion in the following way. Consider the abstract free product Γ = Γ(L1,L2) = Γupp(L1) ∗ Γlow(L2) and deﬁne J : Γ → Hol(Hn,C×) by


J(Tx)(z) = 1, J(V y)(z) = µ(T−ySz)µ(z), for x ∈ L1, y ∈ L2, where, as in §3, µ(z) = nj=1 (zj/i)d

j/2. Since µ(z)µ(Sz) = 1, the cocycle J˜ is well-deﬁned on Γlow(L2), hence on all of Γ.˜ Let π denote the natural homomorphism from Γ onto Γ(L1,L2). We may then deﬁne a right action of Γ on functions f : Hn → C by f|γ := J(γ)−1(f ◦π(γ)). We deﬁne a Γ-cocycle Φ by Φ(γ) := F|(γ − 1). Since JG;8d

1,...,8dn ◦ π agrees with J8 on the generators of Γ we see that for all γ ∈ ker(π), the function J(γ) is constant and equal to some 8-th root of unity. Then, instead of (4.5), we obtain

( J(R)−1 − 1)F = Φ(R) =

m

Φ(V y

)|Pi =

i

i=1

m

(g|V y

Pi − g|Pi),

i

i=1

where R = V y

### Tx

### V y

### Tx

### ···V y

### Tx

is an element in ker(π) ⊂ Γ with m ≥ 1 minimal and Pi as in (4.5). Since F is L1-periodic, by acting on both sides of the above equation by Tx − 1 for a suitable x ∈ L1 (so that the resulting linear combination of Gaussians on the right-hand side involves 4m distinct elements) and again invoking Lemma 2.3 for suitable z ∈ Hn (not ﬁxed by any element in a ﬁnite set of non-trivial group elements) we arrive at the desired contradiction.

1

1

2

2

m

m

Thus, condition (F) is necessary for the existence of F and F˜. Regarding condition (D) we don’t have a rigorous justiﬁcation for its necessity. However, one can show that if (D) fails, then Γ(L1,L2) contains many elliptic elements of inﬁnite order (here we call γ ∈ PSL2(R)n elliptic if each component is either an elliptic element in PSL2(R) or identity), and any such element γ imposes rather strong conditions on Φ(γ) and F (e.g., if the closure of γ is a maximal compact subgroup of PSL2(R)n, F is uniquely deﬁned by the relation Φ(γ) = F|(γ − 1)). Thus it seems plausible that (D) is also necessary for the existence of F and F˜.

Before stating the next result, let us return to the examples coming from totally real number ﬁelds. As already mentioned, in the notation of §2, for a totally real number ﬁeld K/Q of degree n ≥ 2 and L1 = L2 = σ(2OK), the group Γ(L1,L2) is the subgroup of PSL2(OK) generated by all elements T2β,V 2β, β ∈ OK. As such, it is well known to be a discrete subgroup of G, so (D) holds. On the other hand, the condition (F) never holds in this case. To give a concrete example, if 0 = β ∈ OK is such that 1 + 5β ∈ OK×, then

−1

−1

V −2(1+5β) = 1. (4.6) Returning to general lattices, for n ≥ 2, there are unfortunately no examples of lattices L1,L2 ⊂ Rn

T−2β(1+5β)

V 2T2V 2βT−2(1+5β)

for which both conditions (D), (F) hold, as the following proposition shows.

- Proposition 4.3. Let n ≥ 2 and let L1,L2 ⊂ Rn be arbitrary lattices. Suppose the group Γ(L1,L2) ≤ G is discrete. Then (F) does not hold. Proof. Consider the following property (irreducibility) of a lattice L ⊂ Rn


L {0} ⊂ (R×)n. (I)

For example, if L is the image of a fractional ideal in a totally real number ﬁeld under the natural embedding then (I) holds. The proof distinguishes two cases, according to whether both L1,L2 satisfy (I) or one of them does not.

- Case 1: Both L1,L2 have property (I). In this case, by a result of A. Selberg (sketched in [16]),

generalized by Benoist-Oh [2, Cor. 1.2], there exists a totally real number ﬁeld K of degree n such that Γ(L1,L2) is commensurable to a conjugate of the group PSL2(OK) embedded in G. Since Hilbert modular groups of totally real number ﬁelds are known to be irreducible lattices2 in PSL2(R)n, it follows that Γ(L1,L2) is an irreducible lattice in G ∼= PSL2(R)n. Margulis’ normal subgroup theorem [9, Thm 4.9] then implies that the abelianization of Γ(L1,L2) must be ﬁnite, which rules out (F).

- Case 2: One of the lattices L1,L2 does not have property (I). Let us ﬁrst suppose that L1 does


not have property (I). Fix a nonzero element x0 ∈ L1 whose (say) ﬁrst coordinate is zero. We will construct a sequence of lattice vectors yk ∈ L2 {0} such that the commutators

T−x

V −y

[Tx

### ,V y

### ] = Tx

### V y

∈ Γ(L1,L2)

0

0

0

k

k

k

tend to 1 ∈ G, as k → ∞. As we are assuming that Γ(L1,L2) is discrete, the sequence must be stationary and so (F) would not hold. To produce the sequence yk, we apply Minkowski’s lattice point theorem to the convex, compact, centrally symmetric bodies

Ck := (t1,...,tn) ∈ Rn : |t1| ≤ 1 + kn−12n covol(L2), max

|tj| ≤ 1/k ,

2≤j≤n

whose volumes are > 2n covol(L2). We may thus choose 0 = yk ∈ L2 ∩ Ck and with this choice, we have [Tx

### ,V y

] → 1 as k → ∞.

0

k

Finally, if L2 does not have property (I), we can modify the argument just given in an obvious way, by taking a ﬁxed nonzero element y0 ∈ L2 with some vanishing coordinate and a sequence of nonzero lattice vectors xk ∈ L1 all of whose coordinates tend to zero, except in the coordinate where y0 is zero.

2We use the deﬁnition that a lattice Γ in a connected, real semi-simple Lie group G with ﬁnite center is irreducible if for all non-discrete closed normal subgroups N of G the subgroup ΓN is dense in G. The set of such irreducible lattices in G is closed under the equivalence relations given by conjugation and commensurability. See [11, §4.3].

To summarize the general results of this section, we have shown that for n ≥ 2 and for any two lattices Λ1,Λ2 ⊂ Rn, the following holds: If the group Γ(2Λ∨1 ,2Λ∨2 ) is discrete, then no interpolation formula as in (4.1) can exist, by Proposition 4.3 and Proposition 4.2. Combined with our previous remark on the necessity of (D), it may well be that no interpolation formula of the form (4.1) exists for n ≥ 2.

5. Interpolation result via Hecke groups with infinite covolume

By the analysis of §4, Fourier interpolation for square roots of lattices seems to be limited to the case of radial Schwartz functions and 1-dimensional lattices. Let us revisit this case in more detail and compare it to similar known results on Fourier uniqueness.

Let α,β > 0 and consider the one-dimensional lattices Λ1 = (1/α)Z ⊂ R and Λ2 = (1/β)Z ⊂ R. Thus, we consider (the possibility of existence of) interpolation formulas of the form

∞

f( n/α)an(|x|) +

f(x) =

n=0

∞

fˆ( n/β)˜an(|x|), f ∈ Srad(Rd), x ∈ Rd. (5.1)

n=0

The relevant subgroup of PSL2(R) is thus Γ(2(α1 Z)∨,2(β1Z)∨) = Γ(2αZ,2βZ) = T2α,V 2β = T2α,ST2βS .

Conjugating the group by 0 t t−01 with t = (β/α)1/4 allows us to reduce to the case α = β. Alternatively, we may reduce to that case by directly applying a scaling argument to (5.1). We then write

α = β = λ/2 for λ > 0 and consider the groups Γ(λ) := Γ(λZ,λZ) = Tλ,V λ H(λ) := S,Tλ ≤ PSL2(R). (5.2)

The latter groups H(λ) are well-studied and known to be discrete precisely when λ ≥ 2 or λ = 2cos(π/p) for some integer p ≥ 3 (we refer to [3] or [6] for background). The group Γ(λ) is known to be discrete and free precisely when λ ≥ 2. The papers [12], [4], [17] focus on the case λ = 2. Recently, Sardari [14] investigated the case 1 < λ < 2 to answer a question raised in [5]. The paper [5] itself considers the case λ = 1, but in a vector-valued setting.

Fλ

−λ2 −1 0 1 λ

2

Figure 2. A fundamental domain for H(λ) for λ > 2

### In view these results and of the conditions (D), (F), it remains to consider the case λ > 2, which is the purpose of this section. Using a series construction similar to the construction of Poincar´e series and analogous to the one used in [17], we will prove the following theorem.

Theorem 3. Let λ ≥ 2 be a real number and let d ≥ 5 be an integer. Set k = d/2. There exist sequences of entire even functions ak,λ,n,a˜k,λ,n : C → C, n = 1,2,3,..., such that for all f ∈ Srad(Rd) and all x ∈ Rd we have

∞

∞

ak,λ,n(|x|)f( 2n/λ) +

a˜k,λ,n(|x|) f( 2n/λ) (5.3)

f(x) =

n=1

n=1

and both series converge absolutely and uniformly on Rd. There are absolute constants C1,C2,C3 > 0 such that

|a˜k,λ,n(r)| ≤ C1(C2/k)k/2nk (5.4) for all n ≥ 1 and such that

|ak,λ,n(r)| + sup r∈R

sup

r∈R

|ak,λ,n(r)| + |a˜k,λ,n(r)| ≤ C3nk/2+9/8r−k+9/4 (5.5)

for all r > 0 and n ≥ 1. Corollary 5.1. For all d ≥ 5 and α,β > 0 such that αβ > 1 and all integers n0 ≥ 1, the pair

n/βSd−1 is a Fourier uniqueness pair for S(Rd). If αβ = 1, then this is true for n0 = 1.

n/αSd−1,∪n≥n0

∪n≥n0

- Remark 5.1. In the known case λ = 2, one can actually take n0 = (d + 4)/8 for all d ≥ 2 in the statement of the corollary. This follows from [4], see also [13, Thm. 1 and 2].


Proof of Corollary 5.1. As already explained, it suﬃces to consider α = β = λ/2. For radial functions and n0 = 1, this is a direct consequence of Theorem 3. For n0 > 1, we will prove in Appendix B that the radial interpolation formula (5.3) can be modiﬁed, so that both series start at n = n0. We will see that this is a consequence of the fact that, for λ > 2, the space modular forms of weight k on H(λ) is inﬁnite dimensional; see [6, §3] or also [3, Ch. 4]. Finally, the case of general Schwartz function follows from the case of radial Schwartz functions by [17, Cor 2.2].

The proof of Theorem 3 will occupy the remainder of §5. We remark that weaker and less explicit bounds than (5.4) and (5.5) suﬃce to establish (5.3) with point-wise absolute convergence. The more explicit bounds (5.4) and (5.5) can be used to upgrade the uniqueness result of Corollary 5.1 to an interpolation formula that can be written as in [17, Thm. 1] which then justiﬁes the claim made in §1.6. But even without these more explicit bounds, [17, Cor 2.1] allows to deduce some interpolation result from (5.3), but possibly suboptimal from analytic point of view. The details of this passage are almost identical to the analysis in [17, §3] so we will not give them here. However, we include a proof of (5.4) and (5.5) in Appendix A, for the sake of completeness and since it is not obvious how to generalize the corresponding proof in the case for λ = 2 from [17]. In this section §5, we will prove enough to establish (5.3) with absolute uniform convergence by proving a version of (5.4) with unspeciﬁed dependence on k and λ.

- 5.1. Preliminaries for the proof of Theorem 3. Below in §5.2, we will deﬁne the functions ak,λ,n(r), a˜k,λ,n(r) that enter (5.3) in Theorem 3 as the Fourier coeﬃcients of certain 2-periodic


holomorphic function Fk,λ(z,r), F˜k,λ(z,r) but before deﬁning those, we gather here some notation and preliminary results.

- 5.1.1. Notation for §5. For the remainder of §5, k denotes a real number and we will also assume (most of the time) that k > 2. For x ∈ R we use the elements Tx,V x ∈ PSL2(R) as deﬁned in (4.4)


as well as the element S = 01 −01 . We allow λ to be a complex number and deﬁne Γ(λ) and H(λ) as subgroups of PSL2(C) via the generators as in (5.2). The reason for this is mainly for the proof of part (vi) of Lemma 5.3 below, but otherwise, we are only interested in real λ ≥ 2. For expediency,

we will sometimes use the notation γ = acγ bγ

γ dγ for entries of a 2-by-2 matrix. If γ is an element of PSL2(R) = SL2(R)/{±I}, we will only use such notation if the expression in terms of aγ,bγ,cγ,dγ is well-deﬁned for γ ∈ PSL2(R), e.g. |aγ| ∈ R≥0 is well-deﬁned for γ ∈ PSL2(R) and so is the condition cγ = 0.

- 5.1.2. Slash action. For λ ≥ 2, it is known that the only relation in the Hecke group H(λ) is S2 = 1.

We may therefore deﬁne a 1-cocycle jk : H(λ) → Hol(H,C×) by prescribing its values on the generators S,Tλ:

jk(S)(z) := jk(S,z) = (z/i)k := exp(k log(z/i)), jk(Tλ)(z) := jk(Tλ,z) := 1 and in general by requiring the cocycle property jk(γ1γ2) = (jk(γ1) ◦ γ2) · jk(γ2) to hold. Since jk respects the relation S2 = 1, this is possible. We deﬁne a right action of H(λ) on the space of all C-valued functions F on H, by F|kγ := jk(γ)−1 · (F ◦ γ). We extend it to the group algebra C[H(λ)] in the usual way.

- Lemma 5.1. For all k ∈ R, all γ ∈ H(λ), and all z ∈ H we have |jk(γ)(z)| = |cγz + dγ|k.

Proof. Both sides of the claimed identity are 1-cocyles H(λ) → C(H,R>0), so it suﬃces to verify the identity for the generators S,Tλ of H(λ), in which case it follows from the deﬁnitions. 5.1.3. Complex λ. We will need the following lemma.

- Lemma 5.2. For λ ∈ C with |λ| ≥ 2 the group Γ(λ) = Tλ,V λ ≤ PSL2(C) is freely generated by Tλ and V λ. Proof. Consider the following subsets of P1(C):


- 5.1.4. Special subsets of Γ(λ). For λ ∈ C with |λ| ≥ 2, we deﬁne the subset Vλ ⊂ Γ(λ) to be the set of all γ ∈ Γ(λ) of the form


Xλ := {z ∈ C : |z| ≤ 1/(|λ| − 1)}, Yλ = {∞} ∪ {z ∈ C : |z| ≥ (|λ| − 1)}. Let m ∈ Z {0}. By the Ping Pong lemma, it suﬃces to show that

TmλXλ ⊂ Yλ, V mλYλ ⊂ Xλ.

Since SXλ = Yλ, S2 = 1 and STmλS = V −mλ, it suﬃces to prove the ﬁrst of these containments. And indeed, for z ∈ Xλ, we have

1

|Tmλz| = |z + mλ| ≥ |m||λ| − |z| ≥ |λ| − |z| ≥ |λ| −

|λ| − 1 ≥ |λ| − 1, since the last inequality is equivalent to |λ| ≥ 2.

γ = V e

1λTf

1λV e

2λTf

2λ ···V e

nλTf

nλ, (5.6)

where n ≥ 1 and e1,...,en,f1,...fn−1 ∈ Z {0}, fn ∈ Z. We also deﬁne two subsets Rλ,R˜λ ⊂ {1} ∪ Vλ by Rλ := {γ ∈ Vλ : γ as in (5.6) with fn = 0}, R˜λ := {1} ∪ {γ ∈ Vλ : γ as in (5.6) with fn = 0}.

The set Vλ is stable under right multiplication by powers of Tλ and Rλ is a complete set of pairwise inequivalent representatives for Vλ/ Tλ . Similarly, {1} ∪ Vλ is stable under right multiplication by powers of V λ and R˜λ is a complete set of pairwise inequivalent representatives for ({1} ∪ Vλ)/ V λ .

- Lemma 5.3. Consider an element γ ∈ Vλ as in (5.6) and write γ = ac db , so that the entries a,b,c,d depend on n,ei,fi and λ. Then the following holds:


- (i) If fn = 0, then |c| ≥ |d|.
- (ii) If fn = 0, then |d| ≥ |c|.
- (iii) c = 0 = d.
- (iv) |a| ≤ |c| and |b| ≤ |d|.
- (v) Viewing λ as a formal variable and the entries of γ as elements of Z[λ], the degrees of the polynomials c and d are at least 2n − 2.
- (vi) Viewed as functions of λ ∈ [2,∞), the entries |c| and |d| are monotonically increasing on [2,∞).


Proof. We prove parts (i), (ii), and (iii) simultaneously, using induction on n, by multiplying on the right with a non-trivial power of V λ or Tλ . The base case is n = 1, f1 = 0, so γ = V e

1λ and the inequality in (i) holds trivially and certainly cγdγ = 0. For the inductive step, assume n ≥ 2. If fn = 0, set γ = γT−f

nλ and if fn = 0, set γ = γV −e

nλ. Thus, we have either γ = γ Tf

nλ = ∗ ∗ cγ dγ + fnλcγ

nλ = ∗ ∗ cγ + enλdγ dγ

or γ = γ V e

.

If fn = 0, then |cγ | ≥ |dγ | > 0 by inductive hypothesis and hence |d| = |dγ + λfncγ | ≥ |fn||λ||cγ | − |dγ | ≥ 2|cγ | − |cγ | = |cγ | = |c| > 0,

as desired. If fn = 0, then |dγ | ≥ |cγ | > 0 by inductive hypothesis and we deduce |c| ≥ |d| > 0 in a similar way.

- Part (iv) may be proved by induction on n, in the reverse order, that is, by multiplying elements γ

from the left by elements V eλTfλ, starting with (e,f) = (en,fn) and γ = 1, then (e,f) = (en−1,fn−1) and so on. The proof can be given almost exactly as in [17, Lemma 5.2] in the case λ = 2.

- Part (v) can also be proved by induction on n, as parts (i) and (ii). In fact, one has deg(c) =

deg(d) + 1, if fn = 0 and deg(d) = deg(c) + 1 if fn = 0.

- Part (vi) is easily veriﬁed for n = 1. For n ≥ 2, note that parts (v) and (iii) together imply that the


functions c and d are non-constant polynomial functions of λ (with coeﬃcients in Z, depending upon ei,fi), all of whose complex zeros lie in the disc |λ| < 2. It follows from the Gauss–Lucas theorem that the zeros of their ﬁrst derivatives also lie in that disc. In particular, the derivatives of the polynomials c and d have no real zeros in R (−2,2) and this implies the claim in (vi).

As a ﬁnal preliminary fact, we record the following consequence of Lemma 5.3:

max(|γz|,|γSz|,|Sz|) ≤ 1 + Im(z)−1, for all γ ∈ Vλ,z ∈ H. (5.7) To see this, note that for γ ∈ Vγ, we have cγ = 0 and so

1 cγ(cγz + dγ) ≤ 1 + |cγ|−2 Im(z)−1 ≤ 1 + Im(z)−1,

aγ cγ −

|γz| =

where the ﬁrst inequality uses part (iv) and the second uses part (vi) of of Lemma 5.3 and the observation that for λ = 2 (iii) implies |cγ| ≥ 1. The upper bound for |γSz| follows in the same way, since γS = d bγ −aγ

γ −cγ .

## 5.2. Deﬁnition of ak,λ,n and a˜k,λ,n via their generating functions. For r ∈ C and z ∈ H, deﬁne

2

. Using the subsets Vλ deﬁned in §5.1.4 and the slash action deﬁned in §5.1.2, we deﬁne, for all λ ≥ 2, k ∈ R, z ∈ C, r ∈ C, the formal series

ϕr(z) = eπizr

(ϕr|kγ)(z), F˜k,λ(z,r) :=

Fk,λ(z,r) := (−1)

(ϕr|kγS)(z). (5.8)

γ∈Vλ

γ∈Vλ∪{1}

Formally, we clearly have

Fk,λ(z,r) + (z/i)−kF˜k,λ(−1/z,r) = ϕr(z). (5.9) Moreover, since VλTλ = Vλ and since

(Vλ ∪ {1})STλ = ((Vλ ∪ {1})V −λ)S = (Vλ ∪ {1})S,

both Fk,λ(z,r) and F˜k,λ(z,r) are λ-periodic in z (at least formally). The next lemma asserts that, for k > 2, the series deﬁned in (5.8) converge absolutely and uniformly on compacta and thus show that all of these formal identities hold at the level of functions.

- Lemma 5.4. Fix real k > 0, λ ≥ 2, X ≥ 1, y0 > 0 and ﬁx a compact subset Ω ⊂ C. Deﬁne

B := {z ∈ H : Im(z) ≥ y0,|Re(z)| ≤ X}. There is a constant C > 0, depending only on Ω and y0, so that

sup

(z,r)∈B×Ω

|(ϕr|kγ)(z)| ≤ C(1 + 1/y)k(X + 1)k(c2γ + d2γ)−k/2 for all γ ∈ Vλ ∪ {S} ∪ VλS. (5.10) If k > 2, the series deﬁned in (5.8) converge absolutely and uniformly on B × Ω. Proof. Let Wλ := Vλ ∪ {S} ∪ VλS. Let γ ∈ Wλ and (z,r) ∈ B × Ω. By Lemma 5.1 and the estimate (5.7), we have

|(ϕr|kγ)(z)| = |cγz + dγ|−keRe(πi(γz)r

2) ≤ |cγz + dγ|−keπ(1+y

−1

0 ) supr∈Ω |r|2. (5.11)

Let Az : C → C denote the R-linear map given by Az(ci + d) = cz + d, c,d ∈ R. Working with the operator norm of A−z 1 (and using the equivalence of norms on EndR(C)) we ﬁnd a universal constant C1 > 0 so that

(c2 + d2)1/2 = |A−z 1(cz + d)| ≤ A−z 1 |cz + d| ≤ C1(X + 1)(1 + 1/y)|cz + d| for all (c,d) ∈ R2. Raising this to the power k and then inserting into (5.11) yields (5.10). For k > 2, uniform and absolute convergence follows now from part (vi) of Lemma 5.3 and the fact that for λ = 2, the set {(cγ,dγ})γ∈W

γ

is a subset of the primitive vectors in Z2 (modulo {±1}). For each k > 2, λ ≥ 2, r ∈ C and n ∈ Z we now deﬁne

ak,λ,n(r) :=

1 λ

iy+λ/2

iy−λ/2

Fk,λ(z,r)e−2πinz/λdz, a˜k,λ,n(r) :=

1 λ

iy+λ/2

iy−λ/2

F˜k,λ(z,r)e−2πinz/λdz, (5.12)

where y > 0 can be taken arbitrarily, since F and F˜ are holomorphic and λ-periodic.

- Lemma 5.5. For n ≤ 0, we have ak,λ,n = 0 = a˜k,λ,n and, as n → ∞, we have


|a˜k,λ,n(r)| = O(nk), (5.13) where the implied constant depends only on k and λ.

|ak,λ,n(r)| + sup r∈R

sup

r∈R

Proof. We prove the assertions for ak,λ,n, the ones for a˜k,λ,n are proved in the same way. Note that, by the triangle inequality,

|ak,λ,n(r)| ≤ e2πny/λ sup

|Fk,λ(x + iy,r)| for all y > 0. (5.14)

|x|≤λ/2

If n ≤ 0, the exponential is bounded by 1, while the supremum tends to 0 as y → ∞. The latter follows from Lemma 5.4 and its proof: we can use uniform convergence to pull the limit inside the series and the fact that cγ = 0 for all γ ∈ Wλ = Vλ ∪ {S} ∪ VλS. For n ≥ 1 and r ∈ R, we again use Lemma 5.4 and its proof (modiﬁed by using the trivial bound |eπiτr

2

| ≤ 1 for τ ∈ H, r ∈ R) to deduce sup

|Fk,λ(x + iy,r)| k,λ (1 + 1/y)k. This holds for all y > 0, in particular for y = 1/n, which then yields (5.13).

|x|≤λ/2,r∈R

- 5.3. Proof of (5.3) in Theorem 3. Let d ≥ 5 be an integer, k = d/2, λ ≥ 2 real. We claim that the functions ak,λ,n, a˜k,λ,n deﬁned in (5.12) are such that (5.3) holds. By their deﬁnition, the ﬁrst assertion of Lemma 5.5, and by (5.9), the formula (5.3) holds for f(x) = ϕ|x|(z) for all z ∈ H and all x ∈ Rd. On the other hand, from the bound in Lemma 5.5, for ﬁxed x ∈ Rd, the RHS of (5.3) is


continuous in f ∈ Srad(Rd) and so the claimed formula follows in general by the density of Gaussians (Proposition 4.1, although we only need the case n = 1, for which we can also cite [5, Lemma 2.2]). We prove the more precise bounds (5.4) and(5.5) in Appendix A.

Appendix A. Proof of the upper bounds (5.4) and (5.5) in Theorem 3

We will generalize [17, Lemma 5.3] and then proceed similarly as in the rest of [17, §5]. For real κ ≥ 9/4 and λ ≥ 2, let us deﬁne V˜λ := ({1} ∪ Vλ)S and

|cγz + dγ|−κ, U˜κ,λ(z) :=

|cγ˜z + dγ˜|−κ =

|dγz − cγ|−κ.

Uκ,λ(z) :=

γ∈Vλ

γ ˜∈V˜λ

γ∈{1}∪Vλ

We note that these are both λ-periodic, continuous functions on H because of the proof of Lemma 5.4 and because both sets Vλ and V˜λ are stable under right multiplication by powers of Tλ.

Lemma A.1. There is a constant C0 > 0 so that for all z = x + iy ∈ H, all λ ≥ 2 and all κ ≥ 9/4,

max |Uκ,λ(x + iy)|,|U˜κ,λ(x + iy)| ≤ C02κ(y−κ/2 + y−κ).

Proof. By λ-periodicity, it suﬃces to consider z = x + iy ∈ H with |x| ≤ λ/2. We start with the analysis of U˜k,λ(x + iy) and explain the modiﬁcations for Uk,λ at the end. We divide the series into subseries over orbits of right multiplication by Tλ. For this, recall from §5.1.4 the deﬁnition of the set R˜λ and then note that

U˜κ,λ(z) =

|dγ|−κ

|z − (cγ/dγ + eλ)|−κ.

|dγz − (cγ + eλdγ)|−κ =

e∈Z

γ∈R˜λ e∈Z

γ∈R˜λ

For all e ∈ Z, we have

|z + (cγ/dγ + eλ)|2 = y2 + (λe + x + cγ/dγ)2 ≥ y2. By part (ii) of Lemma 5.3, we have |cγ/dγ| ≤ 1 for all γ ∈ R˜λ and therefore, for |e| ≥ 2, |z + (cγ/dγ + eλ)|2 ≥ 2y|λe + x + cγ/dγ| ≥ 2y (λ|e| − λ/2 − 1) ≥ 2yλ(|e| − (1/2 + 1/λ)) ≥ 2yλ(|e| − 1).

Using these lower bounds, we obtain

 3y−κ +

 

1 (d2γ)κ/2

1 (2yλ(|e| − 1))κ/2

U˜κ,λ(z) ≤

γ∈R˜λ

|e|≥2

1 ((c2γ + d2γ)/2)κ/2

3y−κ + (2λy)−κ/22ζ(κ/2) ,

≤

γ∈R˜λ

where we used that c2γ ≤ d2γ for γ ∈ R˜λ. Since κ ≥ 9/4 > 2 and λ ≥ 2, the claimed upper bound for U˜κ,λ follows by appealing once again to part (vi) of Lemma 5.3 and arguing as at the end of the proof of Lemma 5.4.

To treat Uκ,λ, we also split the sum over Vλ into orbits modulo Tλ and use instead the set of representatives Rλ deﬁned in §5.1.4 and correspondingly part (i) of Lemma 5.3.

2

| ≤ 1, valid for all τ ∈ H, r ∈ R, implies that for all λ ≥ 2, k ≥ 5/2, x ∈ R, y > 0, r ∈ R,

Lemma A.1 together with the trivial bound |eπiτr

|Fk,λ(x + iy,r)| ≤ Uk,λ(x + iy) ≤ C02k(y−k + y−k/2) for some absolute constant C0, not depending on k,λ,x,y or r and that the same holds with the tilde. If we insert this into the general bound (5.14) for integers n ≥ 1 and set y = πnk we obtain (after a short computation) (5.4) in Theorem 3 for the functions ak,λ,n (the analysis for a˜k,λ,n is the same).

To prove the remaining bound (5.5), we assume that r > 0. Then, for some β > 0 to be determined, we write

2

|cγz + dγ|−ke−πIm(γz)r

Im(γz)β Im(γz)−β

|Fk,λ(z,r)| ≤

γ∈Vλ

β

β

β πer2

β πer2

Im(γz)−β ≤

Im(z)−βUk−2β,λ(z).

|cγz + dγ|−k

≤

γ∈Vλ

We take β = k/2 − 9/8, so that we can apply Lemma A.1 with κ = 9/4 and so that

β

β

β πe

β πe

r−2βy−βU9/8,λ(z) ≤ C1

r−2β(y−(β+9/4) + y−(9/8+β)),

|Fk,λ(z,r)| ≤

for some absolute constant C1 > 0. We may now use this upper bound in the general estimate (5.14) for integers n ≥ 1 and set y = πnβ to obtain (5.5) in Theorem 3 (the analysis for a˜k,λ,n is the same).

Appendix B. Removing finitely many interpolation nodes

Here, we prove the modiﬁcation of Theorem 3 explained in the proof of Corollary 5.1. We assume that λ > 2 throughout this section. We ﬁrst reformulate our problem by decomposing (5.3) into Fourier eigenspaces so that we can work with modular forms on the bigger group H(λ) ⊃ Γ(λ). This is convenient since H(λ) has only one cusp, but it requires some additional notation and preliminary explanation.

For ∈ {±1}, let χ : H(λ) → {±1} denote the group homomorphisms satisfying χ (S) = and χ (Tλ) = 1. We twist the slash action deﬁned in §5.1.2 by the character χ by deﬁning f| kγ = χ (γ)jk(γ)−1 · (f ◦ γ) for γ ∈ H(λ) and functions f on H. For k ∈ R, let Mk(λ, ) denote the space of all holomorphic functions f : H → C which satisfy f| kγ = f for all γ ∈ H(λ) and which admit a

Fourier expansion of the form f(z) = ∞n=0 bneπi(2n/λ)z with polynomially growing Fourier coeﬃcients: bn = O(nc) for some c = c(f) ≥ 0.

Recall that we constructed Fk,λ(z,r),F˜k,λ(z,r) which are holomorphic and λ-periodic in z and satisfy (5.9). For ∈ {±1} we deﬁne F k,λ(z,r) by

Fk,λ+ Fk,λ−

Fk,λ+ Fk,λ−

- 1

- 2


Fk,λ F˜k,λ ⇔

Fk,λ F˜k,λ

1 −1 1 1

1 1 −1 1

### . (B.1)

=

=

Then each F k,λ(z,r) is λ-periodic in z and we have, by (5.9)

F k,λ(·,r)| k(1 − S) = ϕr| k(1 − S). (B.2) In fact, (B.2) and (5.9) are equivalent. For n ∈ Z we deﬁne (note the sign change)

iy+λ/2

1 λ

F k,λ− (z,r)e−πi(2n/λ)zdz, so that, by (B.1), we have

b k,λ,n(r) :=

iy−λ/2

b+k,λ b−k,λ

b+k,λ b−k,λ

- 1

- 2


1 1 1 −1

ak,λ a˜k,λ ⇔

1 1 1 −1

ak,λ a˜k,λ

=

### . (B.3)

=

For any φ ∈ Mk(λ, ) we can replace F k,λ(z,r) by F k,λ(z,r) − φ (z) and these functions will still be holomorphic, λ-periodic, satisfy the functional equation (B.2) and have polynomially bounded

Fourier coeﬃcients. In particular, we can take for φ any linear combination of functions b− k,n(r)φ n(z) for suitable φ n. We may then redeﬁne F,F˜ in terms of such modiﬁed F+,F− via (B.1) and the (new) Fourier coeﬃcients of F and F˜ will still satisfy the interpolation formula (5.3) with uniform convergence.

Thus, the proof of the remaining part of Corollary 5.1 is reduced to the proof of the following proposition. Indeed, given any integer N ≥ 1, we can use the functions f n, 1 ≤ n ≤ N provided by the proposition and linearly combine them to create φ n ∈ Mk(λ, ) such that φ n(0) = 0 and φ n(m) = δn,m for all n,m ∈ {1,...,N} (where the hat-notation means Fourier coeﬃcient).

Proposition B.1. Fix k > 0, λ > 2 and ∈ {±1}. Then, for every integer n ≥ 1, there exists f n ∈ Mk(λ, ) vanishing to order exactly n at inﬁnity.

Proposition B.1 is essentially due to Hecke [6, §3] who proved the existence of such f n for all integers n ≥ k/2. We will add a further observation (below near (B.5)) to his proof and show that the construction extends to all n ≥ 1. Hecke’s treatment in loc. cit. is somewhat brief and we refer to [3, Chapter 4] for more details and explanation, also for parts of the proof given below.

Proof of Proposition B.1 . Let B1 := {z ∈ C : −λ/2 < Re(z) < 0,|z| > 1}, so that B1 ∩ H is the left half of the fundamental domain Fλ drawn in Figure 2. Consider the following pieces of the boundary of B1:

L1 = −λ/2 + iR, L2 = i[1,∞), L3 = {z ∈ C : Re(z) < 0,|z| = 1}, L4 = i(−∞,−1].

By the Riemann mapping theorem, there exists a biholomorphic map h : B1 → H. It may be chosen uniquely so that it extends continuously to the boundary of B1 (minus the point −i), maps the latter to R and satisﬁes

h(i) = 0, h(−i) = −∞, h(i∞) = 1, h(−i∞) = a0, (B.4)

for some a0 > 1, where the values at ±i∞ are understood in the limit Im(τ) → ±∞. We then have h(L1) = (1,a0), h(L2) = [0,1), h(L3) = (−∞,0) and h(L4) = (a0,∞).

By the Schwarz reﬂection principle applied to L1, L2, and L3, one may extend h to an analytic function on C minus the set of points equivalent to −i under the reﬂections just mentioned. Then h|H is bounded, H(λ)-invariant and never takes the value 1.

We claim that there is δ > 0 so that for all τ ∈ B1 with |Im(τ)| ≤ 2 we have |g(τ) − 1| ≥ δ. To prove this, it suﬃces to show that for all τ ∈ B1 we have

a0 h(τ)

h(τ) =

, (B.5)

because if we specialize the above to τ ∈ R ∩ B1, we get |h(τ)|2 = a0 > 1 and can then use continuity of h to prove the claim. To prove (B.5), we note that both sides deﬁne biholomorphic mappings B1 → {z ∈ C : Im(z) < 0} and that they extend in the same way to the boundary points τ = ±i,±i∞. Now Hecke proves the existence of a holomorphic function H : H → C satisfying

h(τ + λ) = H(τ), H(−1/τ) = −H(τ), H(τ)2 = h(τ) for all τ ∈ H and then considers

h (τ) H(τ)(h(τ) − 1)

,

g(τ) :=

which is holomorphic and nowhere vanishing on H ∪ {i∞} and transforms like a modular form in M2(λ,+1) (we again refer to [3, Ch. 4] for justiﬁcation and details). Using a suitable logarithm of g, Hecke deﬁnes

1−

2 g(τ)k/2(h(τ) − 1)n

f n(τ) := H(τ)

and proves that f n ∈ Mk(λ, ) for n ≥ k/2. Note that since h(τ) − 1 vanishes to order 1 at i∞ while H and g are non-vanishing at i∞, each f n indeed vanishes to order exactly n at i∞. It remains to be shown that f n belongs to Mk(λ, ) for all n ≥ 1. For this, it suﬃces to show that the H(λ)-invariant, continuous function |f n(τ)|Im(τ)k/2 is bounded on the fundamental domain Fλ.

For τ ∈ Fλ with Im(τ) ≥ 2 we have g(τ) − 1 = O(e−(2π/λ) Im(τ)) while g(τ)k/2 and H(τ) are both O(1). For τ ∈ Fλ with Im(τ) ≤ 2, we write

1− 4

|h(τ) − 1|n−k/2|f∗(τ)|k/2, where f∗(τ) := Im(τ)|h (τ)/H(τ)|. (B.6)

|f n(τ)|Im(τ)k/2 = |h(τ)|

The function f∗ : H → R≥0 is easily seen to be bounded (see [3, Ch. 4, p. 31]) and since we showed that |h(τ) − 1| is bounded away from zero for τ ∈ Fλ with Im(τ) ≤ 2 and since we know that h is bounded on H, we are done.

Appendix C. Proof of Proposition 4.1 Recall that n ≥ 1 and dj ≥ 1 are integers such that d = d1+···+dn and that we view Rd = nj=1 Rd

.

j

Abbreviate H := O(d1) × ··· × O(dn) → O(d). We need to show that the linear span W ⊂ S(Rd)H, of all Gaussians

### j=1 zj|xj|2, z ∈ Hn,xj ∈ Rd

n

g(z)(x) = eπi

, is dense in S(Rd)H. As a matter of notation, we will write g(z)(x) = g(z,x) = gz(x) in this proof.

j

By adapting the proof of the fact that Cc∞(Rn) is dense in S(Rn), one may show that Cc∞(Rd)O(d) is dense in S(Rd)H. In particular the larger space Cc∞(Rd)H is dense in S(Rd)H.

We now ﬁx f ∈ Cc∞(Rd)H and aim to show that f ∈ W. Fix positive reals b1,...,bn > 0 and consider the function

n

### j=1 bj|xj|2, x = (x1,...,xn) ∈ Rd, xj ∈ Rd

h(x) := f(x)eπ

. Then h ∈ Cc∞(Rd)H. We claim that there exists a function η ∈ Cc∞(Rn) such that

j

h(x) = η(|x1|2,...,|xn|2) for all x ∈ Rd. (C.1) To prove this, let us ﬁx the unit vectors ej ∈ Sd

and deﬁne h0 ∈ Cc∞(Rn)O(1)×···×O(1) by h0(t1,...,tn) := h(t1e1,...,tnen). Since the algebra of real polynomials in n variables, which are even in each variable, is generated (as an algebra) by the squares of the variables, a general result of

j−1 ⊂ Rd

j

G. Schwarz [15] implies the existence of η ∈ Cc∞(Rn) such that h0(t1,...,tn) = η(t21,...,t2n) for all tj ∈ R and this function then also satisﬁes (C.1).

Now, for a function u ∈ S(Rn) such that u is compactly supported, but otherwise unspeciﬁed for the moment, we write

f(x) = h(x)g(ib

1,...,ibn)(x)

= (η − u)(|x1|2,...,|xn|2)g(ib

1,...,ibn)(x) + u(|x1|2,...,|xn|2)g(ib

1,...,ibn)(x)

= (η − u)(|x1|2,...,|xn|2)g(ib

1,...,ibn)(x) +

u(ξ)g(ib

1+2ξ1,...,ibn+2ξn)(x)dξ,

Rn

where we applied the Fourier inversion on Rn in the last step. The latter integral belongs to W, regardless of the choice of u, as long as u has compact support. This follows from integration theory in Fr´echet spaces and continuity of the map Hn → S(Rd), z  → gz (or alternatively by approximation via Riemann sums). It therefore suﬃces to show that the term involving η −u can be made arbitrarily small in the Schwartz topology. To see this, consider the linear map E : S(Rn) → S(Rd)H, deﬁned by Eϕ(x) := ϕ(|x1|2,...,|xn|2). It continuous for the Schwartz topology and multiplication by g(ib

1,...,ibn) is continuous. Since the space of u ∈ S(Rn) such that u has compact support is dense in S(Rn) and E is continuous, we can choose u in such a way that E(η−u) is in any prescribed open zero neighborhood of S(Rd). This ﬁnishes the proof of Proposition 4.1.

References

- [1] A. Ash, S. Friedberg, Hecke L-Functions and the Distribution of Totally Positive Integers, Canad. J. Math. vol. 59 (4), pp. 673–695, (2007).
- [2] O. Benoist, Y. Oh, Discreteness criterion for subgroups of products of SL(2), Transformation Groups, vol. 15, 503–515, (2010).
- [3] B. Berndt, M. Knopp, Hecke’s theory of Modular forms and Dirichlet series, World Scientiﬁc, 2008.
- [4] A. Bondarenko, D. Radchenko, K. Seip, Fourier interpolation with zeros of zeta and L-functions, arXiv e-prints, https://arxiv.org/abs/2005.02996, May 2020.
- [5] H. Cohn, A. Kumar, S. Miller, D. Radchenko, M. Viazovska, Universal optimality of the E8 and Leech lattices and interpolation formulas, Annals of Mathematics, to appear.
- [6] E. Hecke, Uber¨ die Bestimmung Dirichletscher Reihen durch ihre Funktionalgleichung, Mathematische Annalen, vol. 112, 664–699, (1936).
- [7] E. Hecke, Vorlesungen ¨uber die Theorie der algebraischen Zahlen, Leipzig: Akad. Verlag, 1923 and 1954.
- [8] H. Maass, Modulformen und quadratische Formen ¨uber dem quadratischen Zahlk¨orper R(√5), Math. Ann. vol. 118, 65–84, (1941).

- [9] G. A. Margulis, Discrete subgroups of semisimple Lie groups, Ergebnisse der Mathematik und ihrer Grenzgebiete, vol. 17, Springer, 1991.
- [10] R. A. Mollin, Algebraic Number Theory, CRC Press
- [11] D. W. Morris, Introduction to Arithmetic Groups, Deductive Press (2015). Available online at https://arxiv.org/abs/math/0106063.


- [12] D. Radchenko, M. Viazovska, Fourier interpolation on the real line, Publ. Math. Inst. Hautes Etudes´ Sci. vol. 129, 51–81, (2019).
- [13] J. Ramos, M. Stoller, Perturbed Fourier interpolation and uniqueness results in higher dimensions, Journal of Functional Analysis, vol. 282, June 2021
- [14] N. Sardari, Higher Fourier interpolation on the plane, arXiv e-prints, https://arxiv.org/abs/2102.08753, February 2021.
- [15] G. Schwarz, Smooth functions invariant under the action of a compact Lie group, Topology, vol. 14, 63–68,

(1975).

- [16] A. Selberg, Recent Developments in the Theory of Discontinuous Groups of Motions of Symmetric Spaces, Proceedings of the 15th Scandinavian Congress Oslo, 1968.
- [17] M. Stoller, Fourier interpolation from spheres, Transactions of the American Mathematical Society, vol. 374, 8045–8079, November 2021


ETH Zurich,¨ Mathematics Department, Ramistrasse¨ 101, 8092 Zurich,¨ Switzerland Email address: danradchenko@gmail.com

Batimentˆ des Mathematiques,´ EPFL, Station 8, CH-1015 Lausanne, Switzerland Email address: marstoller@gmail.com

