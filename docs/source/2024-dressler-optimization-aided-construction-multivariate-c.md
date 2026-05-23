---
type: source
kind: paper
title: Optimization-Aided Construction of Multivariate Chebyshev Polynomials
authors: Mareike Dressler, Simon Foucart, Mioara Joldes, Etienne de Klerk, Jean Bernard Lasserre, Yuan Xu
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2405.10438v3
source_local: ../raw/2024-dressler-optimization-aided-construction-multivariate-c.pdf
topic: general-knowledge
cites:
---

arXiv:2405.10438v3[math.OC]26Oct2024

Optimization-Aided Construction of Multivariate Chebyshev Polynomials

![image 1](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile1.png>)

M. Dressler∗, S. Foucart†, M. Joldes‡, E. de Klerk§, J. B. Lasserre¶, and Y. Xu‖

![image 2](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile2.png>)

Abstract

This article is concerned with an extension of univariate Chebyshev polynomials of the ﬁrst kind to the multivariate setting, where one chases best approximants to speciﬁc monomials by polynomials of lower degree relative to the uniform norm. Exploiting the Moment-SOS hierarchy, we devise a versatile semideﬁnite-programming-based procedure to compute such best approximants, as well as associated signatures. Applying this procedure in three variables leads to the values of best approximation errors for all monomials up to degree six on the euclidean ball, the simplex, and the cross-polytope. Furthermore, inspired by numerical experiments, we obtain explicit expressions for Chebyshev polynomials in two cases unresolved before, namely for the monomial x21x22x3 on the euclidean ball and for the monomial x21x2x3 on the simplex.

Key words and phrases: best approximation, Chebyshev polynomials, sum of squares, method of moments, semideﬁnite programming.

AMS classiﬁcation: 41A10, 65D15, 90C22.

# 1 Introduction

For n ≥ 1, let Pn denote the space of univariate polynomials of degree less than or equal to n. The classical nth degree Chebyshev polynomial (of the ﬁrst kind) is the polynomial Tn often implicitly deﬁned via the relation Tn(cos θ) = cos(nθ) for all θ ∈ [−π,π]. It is characterized by a wealth of extremal properties, including:

![image 3](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile3.png>)

∗School of Mathematics and Statistics, University of New South Wales, Australia, m.dressler@unsw.edu.au †Department of Mathematics, Texas A&M University, United States, foucart@tamu.edu ‡LAAS-CNRS, France, joldes@laas.fr §Department of Econometrics and Operations Research, Tilburg University, The Netherlands,

E.deKlerk@tilburguniversity.edu ¶LAAS-CNRS and Toulouse School of Economics, France, lasserre@laas.fr ‖Department of Mathematics, University of Oregon, United States, yuan@uoregon.edu

- • 2−n+1Tn is the monic polynomial that deviates least from zero in the uniform norm on [−1,1], i.e., Tn minimizes p [−1,1] := max{|p(x)| : x ∈ [−1,1]} over all polynomials p ∈ Pn satisfying coeﬀxn(p) = 2n−1—this is how Chebyshev polynomials were ﬁrst introduced in [4];
- • 2−n+1Tn is the monic polynomial that deviates least from zero in the L2-norm on [−1,1]

with respect to the inverse semicircle weight, i.e., Tn minimizes − 11 p(x)2(1 − x2)−1/2dx over all polynomials p ∈ Pn satisfying coeﬀxn(p) = 2n−1—this relates to the orthogonality of Chebyshev polynomials for this weight;

- • Tn is the extremizer of every diﬀerentiation operator, i.e., Tn maximizes p(k) [−1,1] over all polynomials p ∈ Pn satisfying p [−1,1] ≤ 1 for every k = 1,2,... ,n—this is Markov’s inequality due to A. A. Markov for k = 1 and Markov’s inequality due to his younger brother V. A. Markov for k = 2,... ,n;
- • Tn is the polynomial with the largest growth outside [−1,1], i.e., for every t  ∈ [−1,1] and every k = 0,1,... ,n, Tn maximizes |p(k)(t)| over all polynomials p ∈ Pn satisfying p [−1,1] ≤ 1;
- • Tn is the polynomial with largest arc-length on [−1,1], i.e., Tn maximizes − 11 1 + p′(x)2dx over all polynomials p ∈ Pn satisfying p [−1,1] ≤ 1.


![image 5](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile5.png>)

Each of these ﬁve properties, which are all found in the classic book [21] by Rivlin, could serve

- as a rationale for a generalization of Chebyshev polynomials to the multivariate setting. The


generalization examined in this article is based on the ﬁrst property. Thus, denoting by Pnd the space of d-variate polynomials of degree ≤ n and considering a domain Ω ⊆ Rd, we intend to tackle the optimization program

minimize

p∈Pnd

p Ω := max x∈Ω

|p(x)| subject to p being monic.

Although this is a convex optimization program—the constraint is linear and the objective function is convex—solving it is far from trivial. By introducing a slack variable c ∈ R, it is seen to be equivalent to

(1) minimize

c subject to p being monic and to

c∈R, p∈Pnd

c + p ≥ 0 on Ω, c − p ≥ 0 on Ω.

The added constraints are polynomial nonnegativity constraints and, as such, can conceivably be dealt with using sum-of-squares (SOS) techniques. In fact, as clariﬁed later, we will advantageously use the dual facet of the Moment-SOS hierarchy [14] to address our central optimization program.

But before delving into the technicalities, let us mention that the above formulation comes with some ambiguities about

- • the notion of multivariate degree: we will concentrate exclusively on the total degree given by

deg

k=(k1,...,kd)

ck1,...,kd xk11 ··· xkdd = max

k:ck =0

|k|, where |k| = k1 + ··· + kd;

- • the choice of domain Ω: we will consider only the simplex S, the cross-polytope C (ℓ1-ball), the euclidean ball B (ℓ2-ball), and the hypercube H (ℓ∞-ball), which are given by

S = x ∈ Rd : x1,... ,xd ≥ 0 and

d

i=1

xi ≤ 1 , C = x ∈ Rd :

d

i=1

|xi| ≤ 1 ,

B = x ∈ Rd :

d

i=1

|xi|2 ≤ 1 , H = x ∈ Rd : max

i=1,...,d

|xi| ≤ 1 ;

- • the meaning of ‘monic’ in the constraint: it can be interpreted as imposing that the coeﬃcient


on a ﬁxed nth degree monomial mk equals one while the coeﬃcients on all other nth degree monomials equal zero, leading to the best approximation problem

- (2) minimize

p∈Pnd−1

mk − p Ω, where mk(x) = xk11 ··· xkdd and |k| = n,

or it could be interpreted as imposing that the coeﬃcients on all the nth degree monomials sum up to one, leading to the program

- (3) minimize p∈Pnd


p Ω subject to

coeﬀmk(p) = 1.

|k|=n

The term Chebyshev polynomial will refer to the ﬁrst interpretation. It is the subject of this article and necessitates a computational approach. The second interpretation comes, more classically, with explicit expressions for a large class of domains including S, C, B, and H. This is the subject of a companion article, see [5].

Here, our contribution includes the numerical—sometimes explicit—construction of all Chebyshev polynomials up to degree n = 6 for d = 3 variables. The whole list of errors of best approximation is assembled in Section 4, completing a partial catalog of known results recalled in Section 2. This section also provides a refresher on some important reductions and on the central concept of signature. The production of novel Chebyshev polynomials exploits a semideﬁnite programming procedure presented in Section 3. Arguably, this is the centerpiece of our work and we emphasize its versatility, which would allow one to make easy adjustments for related problems, e.g. multivariate Zolotarev’s polynomials could be constructed with only small modiﬁcations of the procedure. It is also worth noting already at this point that the workﬂow is not only numerical: the experimental Chebyshev polynomials returned by our procedure can be veriﬁed explicitly or symbolically to be genuine Chebyshev polynomials. For instance, best approximants to the monomial m(2,2,1) relative to the euclidean ball and to the monomial m(2,1,1) relative to the simplex are derived analytically in Section 4. Finally, Section 5 gives an outlook on a possible augmentation of the procedure and its deployment into further computational endeavors.

# 2 Prior Knowledge

This section is exclusively concerned with (monomial-speciﬁc) multivariate Chebyshev polynomials, i.e., with solutions to the best approximation problem (2). We start by recalling a characterization of these solutions involving the notion of signature. Then we provide a catalog of previously derived multivariate Chebyshev polynomials—more precisely, of the known results that we are aware of. We point out from the outset that multivariate Chebyshev polynomials are generically not unique, explaining our tendency to manipulate signatures preferably to polynomials themselves.

## 2.1 Characterization via signatures

To be most general, let us assume that Ω is a compact set and that we are trying to approximate a continuous function f ∈ C(Ω) by elements of a ﬁnite-dimensional vector space V ⊆ C(Ω), assuming of course that f  ∈ V. We have in mind the case where f is a nth degree monomial and where V is the space Pnd−1, but the considerations of this subsection are valid beyond this speciﬁc case. The error of best approximation and (any one of) the best approximant(s) shall be denoted by EV(f,Ω) and by v∗, respectively, so that

- (4) EV(f,Ω) = min v∈V

f − v Ω = f − v∗ Ω.

A folklore result in Approximation Theory shows that the latter can alternatively be expressed as a maximum, namely as

- (5) EV(f,Ω) = max λ∈C(Ω)∗


λ(f) subject to λ|V = 0 and λ C(Ω)∗ = 1.

In optimization custom, this is viewed as a strong duality result, whose proof is informative to sketch here. To start, the inequality that the maximum in (5) does not exceed the minimum in (4) simply follows from the fact that, for any feasible v ∈ V and λ ∈ C(Ω)∗, one has

λ(f) = λ(f − v) ≤ λ C(Ω)∗ f − v Ω = f − v Ω.

Next, for the reverse inequality, given a best approximant v∗, consider the linear functional λ deﬁned on Vf := V ⊕ Rf by

λ(v + tf) = t f − v∗ Ω, v ∈ V, t ∈ R. This linear functional has norm one: indeed, setting aside the trivial case t = 0, one has

| λ(v + tf)| = |t| f − v∗ Ω ≤ |t| f − (−v/t) Ω = v + tf Ω, with equality for t = 1 and v = −v∗. Therefore, by the Hahn–Banach extension theorem, there exists a linear functional λ deﬁned on C(Ω) such that λ C(Ω)∗ = 1 and λ|Vf = λ|Vf, implying in

particular λ|V = 0. The maximum in (5) is then larger than or equal to λ(f) = λ(f) = f −v∗ Ω, i.e., than the minimum in (4). This concludes the sketch of strong duality.

It is worth commenting on the form of the Hahn–Banch extension λ in the above argument. To do so, we notice that the linear functional λ ∈ Vf∗ is expressed as a convex combination of L extreme points of the unit ball of Vf∗, where one can take L ≤ dim(Vf) + 1 by applying Krein– Milman and Carathe´odory theorems. Since the extreme points of the unit ball of Vf∗ are restrictions to Vf of some ±δω, ω ∈ Ω, where δω represents the Dirac evaluation functional at a point ω, we can write λ = Lℓ=1 τℓεℓδωℓ|V

with ω1,... ,ωL ∈ Ω, ε1,... ,εL = ±1, and τ1,... ,τL > 0 satisfying

f

L ℓ=1 τℓ = 1. It is then clear that the Hahn–Banach extension λ can be chosen as λ = Lℓ=1 τℓεℓδωℓ. Of note, the estimation of L can be reﬁned to L ≤ dim(Vf) by calling upon Theorem 2.13 from Rivlin’s book [21], which states that a norm-one linear functional on a real ﬁnite-dimensional subspace U of C(Ω) can be expressed as a convex combination of L ≤ dim(U) extreme points of the unit ball of U∗. In the particular case U = Pkd, it equates to Tchakaloﬀ’s theorem and its generalizations (notably by Richter [20]), stating that if a measure µ on Rd has moments up to degree k, then there exists an atomic measure with at most k+dd atoms in supp(µ) and with same moments up to degree k.

Closing the digression on the value of L and keeping the above notation, we point out that

L

EV(f,Ω) = λ(f) = λ(f − v∗) =

- (6) τℓεℓ(f − v∗)(ωℓ)


ℓ=1

L

L

τℓ f − v∗ Ω = f − v∗ Ω

τℓ|(f − v∗)(ωℓ)| ≤

≤

ℓ=1

ℓ=1

= EV(f,Ω),

which implies that the equalities εℓ(f − v∗)(ωℓ) = f − v∗ Ω = EV(f,Ω) hold for all ℓ = 1,... ,L. This brings us to the notion of extremal signature associated with f − v∗, deﬁned below along the lines of [21, Section 2.2].

Deﬁnition 1. A signature with support (aka base) S ⊆ Ω is simply a function from S to {±1}. A signature σ with support S is said to be extremal for V if there exist weights τω > 0, ω ∈ S, such that ω∈S τωσ(ω)v(ω) = 0 for all v ∈ V. A signature σ with support S is said to be associated with a function g ∈ C(Ω) if S is included in the set {ω ∈ Ω : |g(ω)| = g Ω} of extremal points of g and if σ(ω) = sgn(g(ω)) for all ω ∈ S.

The argument outlined before the deﬁnition justiﬁes the following brief statement, found e.g. in [21, Theorem 2.6]. We emphasize that it does not provide a way to ﬁnd extremal signatures and best approximants, but if one comes up with a guess for these (as we will do in Section 4), then it provides a way to verify that the guess is correct.

Theorem 2. An element v∗ ∈ V is a best approximant to f ∈ C(Ω) from V if and only if there exists an extremal signature σ for V associated with f − v∗. Moreover, the support of such a signature can be chosen to have size ≤ dim(V) + 1.

An important detail not made apparent in the above statement is the existence of a signature common to all best approximants—this is revealed by (6), because the involved arguments did not depend on the best approximant v∗. This fact explains our preference for solving (5) over (4), especially since (4) typically have nonunique solutions.

## 2.2 Simple reductions

Given a ﬁxed number d of variables and a ﬁxed degree n, completely solving the problem of d-variate nth degree Chebyshev polynomials requires ﬁnding best approximants to all d-variate nth degree monomials, so we would a priori need to tackle n+d−d−11 subproblems. For d = 3 and n = 6, it amounts to 28 subproblems and for d = 3 and n = 10, it amounts to 66 subproblems. Fortunately, this number can be decreased drastically by leveraging two simple reductions. The ﬁrst reduction allows us to discard the indices ki = 0 in the multiindex k of the monomial mk, provided the full problem has been solved for all d′ < d. The second reduction allows us to consider only indices k1,... ,kd that are ordered from largest to smallest, say. These facts are precisely stated in the two propositions below. In the ﬁrst one, the domain Ω can be taken as any of our preferred choices—the simplex S, the cross-polytope C, the euclidean ball B, or the hypercube H—by selecting ϕ = 0. The argument, already found in [27, Proposition 4.1] for Ω = B, is included here to also cover the case ϕ = 0. The statement uses the notation N0 for {0,1,2,...}, ωI ∈ RI for the restriction of a vector ω ∈ Rd to a subset I of {1,2,... ,d}, and Ic for the complement of I.

- Proposition 3. Given k ∈ Nd0 with |k| = k1 + ··· + kd = n, let I := {i = 1,... ,d : ki > 0}, let d′ := |I|, and let k′ := kI ∈ Nd0′, which satisﬁes |k′| = k1′ + ··· + kd′′ = n. Let also Ω′ ⊆ RI be the d′-dimensional domain deﬁned by Ω′ = {ωI, ω ∈ Ω}. Suppose that there is a ϕ ∈ RIc such that the element ω deﬁned by ωi = ωi for i ∈ I and ωi = ϕi for i ∈ Ic belongs to Ω whenever ω ∈ Ω. Then one has


(mk′,Ω′).

(mk,Ω) = EPd′

EPd

n−1

n−1

Proof. On the one hand, with q′ ∈ Pnd′−1 such that EPd′

(mk′,Ω′) = mk′−q′ Ω′ and with q ∈ Pnd−1 deﬁned by q(x) = q′(xI), x ∈ Rd, we have

n−1

|mk′(ωI) − q′(ωI)| = max ω∈Ω

(mk′,Ω′) = mk′ − q′ Ω′ = max ω∈Ω

EPd′

|mk(ω) − q(ω)| = mk − q Ω ≥ EPd

n−1

(mk,Ω).

n−1

This inequality was obtained independently of the existence of ϕ. On the other hand, for the reverse inequality, given p ∈ Pnd−1, we have

|mk′(ωI) − p(ωI)|,

mk − p Ω = max ω∈Ω

|mk(ω) − p(ω)| ≥ max ω∈Ω

|mk( ω) − p( ω)| = max ω∈Ω

where p is implicitly deﬁned as a polynomial in Pnd′−1. Therefore, we obtain mk − p Ω ≥ mk′ − p Ω′ ≥ EPd′

(mk′,Ω′).

n−1

The inequality EPd

n−1

(mk,Ω) ≥ EPd′

n−1

(mk′,Ω′) follows by taking the inﬁmum over p.

![image 11](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile11.png>)

![image 12](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile12.png>)

![image 13](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile13.png>)

![image 14](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile14.png>)

The second fact, stated hereafter, has been previously used to derive a number of examples in [1, 2, 26]. We include a standard argument (see e.g. [27, Theorem 3.2]) for the convenience of the reader. This fact is to be used with V = Pnd−1 and G being the group of permutations of {1,2,... ,d}.

- Proposition 4. Given a ﬁnite group G acting on a domain Ω ⊆ Rd, for h ∈ C(Ω) and g ∈ G, let


hg ∈ C(Ω) be deﬁned by hg(ω) = h(gω), ω ∈ Ω. If the domain Ω and the subspace V ⊆ C(Ω) are invariant under the action of G, in the sense that

Ωg := {gω,ω ∈ Ω} coincides with Ω for all g ∈ G, Vg := {vg,v ∈ V} coincides with V for all g ∈ G,

then, for any f ∈ C(Ω) and any g ∈ G, EV(f,Ω) = EV(fg,Ω).

Furthermore, if f is invariant under the action of G, i.e., if fg coincides with f for all g ∈ G, then there is a best approximant v∗ to f from V which is invariant under the action of G, i.e., vg∗ = v∗ for all g ∈ G.

Proof. For f ∈ C(Ω), let v′ ∈ V be a best approximant to f from V. The invariance of Ω implies that, for any g ∈ G,

|fg(ω) − vg′ (ω)| ≥ EV(fg,Ω),

|f(ω) − v′(ω)| = max ω∈Ω

|f(gω) − v′(gω)| = max ω∈Ω

EV(f,Ω) = max ω∈Ω

where the last step relied on the invariance of V to ensure that vg′ ∈ V. A similar argument with fg in place of f and g−1 in place of g would yield the reverse inequality EV(fg,Ω) ≥ EV(f,Ω) and in turn the desired equality. Now, let us assume in addition that fg = f for all g ∈ G. Using the above, we have f − v′ Ω = f − vg′ Ω, so that vg′ is also a best approximant to f from V for all g ∈ G. Consequently, the element v∗ := |G|−1 g∈G vg′ ∈ V, as a convex combination of best approximants, is itself a best approximant to f from V. It is also readily seen that v∗ thus deﬁned is invariant under the action of G.

![image 15](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile15.png>)

![image 16](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile16.png>)

![image 17](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile17.png>)

![image 18](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile18.png>)

As alluded to before, Propositions 3 and 4 imply that, for the simplex, the cross-polytope, the euclidean ball, and the hypercube, it is enough to consider the monomials mk where k ∈ Nd0 satisﬁes k1 + ··· + kd = n and k1 ≥ ··· ≥ kd ≥ 1. The number of these monomials equals the number of partitions of the integer n into exactly d parts. This number pd(n) is known to obey the recurrence relation pd(n) = pd−1(n−1)+pd(n−d), which allows one to arrange them in a triangular table akin to Pascal’s triangle. For instance, for d = 3 and n = 10, one has p3(10) = 8. For d = 3 and n = 6, one has p3(6) = 3, with the three partitions being (4,1,1), (3,2,1), and (2,2,2). In case of the cross-polytope, the values of the three corresponding errors of best approximation are reported in the last column of Table 2, none of which were known before.

## 2.3 Known multivariate Chebyshev polynomials

In this section, we gather previously obtained results about multivariate Chebyshev polynomials for our domains of interest, with the exception of the cross-polytope, which seems to have been cast aside in the literature. We will use from now on the shorthand notation

E(k,Ω) := EPd

(mk,Ω),

n−1

since considering k = (k1,... ,kd) with k1 + ··· + kd = n implicitly tells us the value of d and n.

The hypercube. The case of the hypercube, i.e., Ω = H, is completely resolved. Indeed, the geometry of the domain bodes well for calculations involving the tensor products of univariate polynomials p1,... ,pd, as deﬁned by (p1⊗···⊗pd)(x1,... ,xd) = p1(x1)··· pd(xd). It is not diﬃcult to establish the following result by invoking signatures.

- Theorem 5. Given k ∈ Nd with k1 + ··· + kd = n, one has E(k,H) = 2−n+d


and a best approximant to mk from Pnd−1 is given by mk − 2−n+dTk1 ⊗ ··· ⊗ Tkd.

This result was proved by several authors, see e.g. [24, 6]. In [25], it has also been shown that mk − 2−n+dTk1 ⊗ ··· ⊗ Tkd is a unique best approximant when and only when d = 2 and k1 = k2.

The euclidean ball. The case of the euclidean ball, i.e., Ω = B, is partially resolved: it is solved for d = 2 variables but not completely in d ≥ 3 variables. With Uℓ = Tℓ′+1/(ℓ + 1) denoting the univariate ℓth degree Chebyshev polynomial of the second kind, the result for d = 2 reads as follows.

- Theorem 6. Given k ∈ N2 with k1 + k2 = n, one has E(k,B) = 2−n+1

and a best approximant to mk from Pn2−1 is given by mk − 2−n(Uk1 ⊗ Uk2 − Uk2−2 ⊗ Uk1−2), with the understanding that U−1 = 0.

This was obtained for the ﬁrst time in [10]. Other explicit best approximants can be found in [3, 19]. It is also known that the diﬀerence between two best approximants has the form (1−x21−x22)q(x1,x2) for some q ∈ Pn2−3.

For d > 2, best approximants to monomials are known only for a few low-degree instances, such as m(1,...,1)(x) = x1x2 ··· xd and m(2,1,...,1)(x) = x21x2 ··· xd, see [1, 2, 26]. Restricting our attention to the case d = 3, we now cite some articles and the result they contain:1,2

- [1] : E((1,1,1),B) = 3−3/2,
- [2] : E((2,1,1),B) = (3 −


√

![image 21](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile21.png>)

8)/2, [16] : E((3,1,1),B) = (1 − a)(a3/5)1/4/5, a = smallest root of 9t4 − 29t3 + 24t2 − 29t + 9, [26] : E((2,2,2),B) = 1/72, [26] : E((4,4,4),B) = b−1/272, b ≈ 21.8935834.

The simplex. The case of the simplex, i.e., Ω = S, is also partially resolved. Indeed, for d = 2, best approximants to monomials are presented in [17]. The result is recalled below.

- Theorem 7. Given k ∈ N2 with k1 + k2 = n, one has E(k,S) = 2−2n+1


and a best approximant to mk from Pn2−1 is given by mk − Tk1,k2, where

Tk1,k2(x,y) = Tk1−k2(2x − 1)Tk2(8xy − 1) + 8xy(2x − 1)Uk1−k2−1(2x − 1)Uk2−1(8xy − 1) for k1 ≥ k2, with the understanding that U−1 = 0.

In the case d = 3, we mention the results

- [26] : E((1,1,1),S) = 1/72,
- [26] : E((2,2,2),S) = b−1/272, b ≈ 21.8935834.


Note that there is a close connection between the best approximants on the simplex S to the monomial mk(x) = xk11 ··· xkkd and the best approximants on the euclidean ball B to the monomial m2k(x) = x21k1 ··· x2kkd, see [26] for the precise statement.

![image 22](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile22.png>)

- 1The value of E((3, 1, 1), B) is implicit in [16, Theorem 2.1.(b)]—deriving the explicit value requires some work.
- 2There was a typographical error concerning the value of E((4, 4, 4), B) in [26, Theorem 3.2].


# 3 Description of the Computational Procedure

In this section, we explain the procedure that we derived and exploited in order to produce a number of new multivariate Chebyshev polynomials (uncovered in Section 4). Our implementation is available at https://github.com/foucart/Multivariate_Chebyshev_Polynomials. Although it limits itself to the best approximation from Pnd−1 to monomials mk ∈ Pnd on the hypercube, the euclidean ball, the cross-polytope, and the simplex, the underpinning procedure is more general. Indeed, it could handle any polynomial f ∈ PNd , N ≥ n, instead of mk, while the domain Ω ∈ Rd could be any compact (with nonempty interior) basic semialgebraic set. This means that there exist polynomials g1,... ,gH such that

- (7) Ω = {x ∈ Rd : g1(x) ≥ 0,... ,gH(x) ≥ 0}.


We further assume that the polynomials describing Ω satisfy the Archimedean condition, meaning e.g. that there exist a constant C > 0 and sum-of-squares polynomials σ0,σ1,... ,σH such that

C − x 22 = σ0(x) + H

h=1

σh(x)gh(x) for all x ∈ Ω.

This occurs for all four domains considered in this article—for instance, the argument for the simplex S can be found in [23, Example 12.49] and a similar argument applies to any compact convex polytope.

Our strategy to deal with the best approximation problem is to transform it into an instance of the Generalized Moment Problem (GMP), so that we can invoke the Moment-SOS hierarchy designed to solve a GMP whose data are algebraic (polynomials and semialgebraic sets), see [14]. This process leverages a combination of: (i) semideﬁnite programming3, an eﬃcient machinery in Convex Optimization developed since the late seventies, and (ii) powerful positivity certiﬁcates and their dual analogs concerning the moment problem. These two ingredients were not available at the time of pioneering works such as the paper [22] by Rivlin and Shapiro, in which dual formulations were mostly used to prove the existence of optimal solutions and to characterize them. For the numerical computations, we will rely on GloptiPoly 3, since many of the GMP components are built in this matlab/octave program, see [12].

Let us be more speciﬁc about the computation of the error of best approximation by polynomials from Pnd−1 to a polynomial f ∈ PNd , N ≥ n, i.e., of E∗ := EPd

(f,Ω), viewed as the optimal value of (4) or of (5)—which we call primal program and dual program, respectively. Looking at (4) ﬁrst, it can be reformulated along the lines of (1) into

n−1

c + f − p ∈ P+d (Ω), c − f + p ∈ P+d (Ω),

E∗ = min

c subject to

c∈R,p∈Pnd−1

![image 24](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile24.png>)

- 3A semideﬁnite program (SDP) is a conic convex optimization problem which can be solved in time polynomial


in its input size, up to arbitrary (ﬁxed) precision (e.g. with interior point methods); for more details, see e.g. [15].

where P+d (Ω) denotes the cone of d-variate polynomials that are nonnegative on Ω. As for (5), by identifying linear functionals λ ∈ C(Ω)∗ with ﬁnite signed Borel measures µ on Ω through

λ(g) = Ω gdµ, g ∈ C(Ω), it can be rewritten as

- (8) E∗ = max µ∈M(Ω) Ω

f dµ s.to

Ω

pdµ = 0 for all p ∈ Pnd−1 and

Ω

d|µ| = 1.

With M+(Ω) denoting the cone of ﬁnite nonnegative Borel measures on Ω, the latter can further be rewritten as4

E∗ = max

µ±∈M+(Ω) Ω

f d(µ+ − µ−) s.to

Ω

- (9) pd(µ+ − µ−) = 0 for all p ∈ Pnd−1

and

Ω

d(µ+ + µ−) = 1.

This is an instance of the Generalized Moment Problem (GMP), mentioned above. Note that P+d (Ω) is the dual cone of M+(Ω) (and vice versa) with respect to the pairing p,µ := Ω pdµ. In other words, one has M+(Ω)∗ = P+d (Ω), where the dual cone is deﬁned in the usual way, i.e.,

M+(Ω)∗ := p ∈ Pd(Ω) : p,ν ≥ 0 for all ν ∈ M+(Ω) .

The quadratic module of g1,... ,gH, denoted by Q(g1,... ,gH), is an important subcone of P+d (Ω). It consists of all polynomials of the form

- (10) p = σ0 + σ1 g1 + ··· + σH gH


for some sum-of-squares polynomials σ0,σ1,... ,σH. The associated truncated quadratic module of degree 2t, denoted by Q(g1,... ,gH)t, is the subset of Q(g1,... ,gH) obtained by restricting all the terms in (10) to have degree at most 2t, i.e., deg(σ0) ≤ 2t and deg(σhgh) ≤ 2t for h = 1,... ,H.

By deﬁnition, the dual cone of Q(g1,... ,gH) consists of linear functionals λ on Pd such that λ(p) ≥ 0 for all p ∈ Q(g1,... ,gH). This dual cone can be described in terms of sequences of positive semideﬁnite matrices. To this end, we denote by Hankt(y) the Hankel matrices of size

d × t+dd built from a sequence y indexed by Nd0 as having entries yi+j for i,j ∈ {0,... ,t}d. Similarly, we construct matrices Hankt(Ghy) from sequence Ghy associated with each gh, namely (Ghy)ℓ =

t+d

coeﬀmℓ′(gh)yℓ+ℓ′ for any ℓ ∈ Nd0.

|ℓ′|≤deg(gh)

The following theorem by Putinar [18] describes the relation between P+d (Ω) and Q(g1,... ,gH), and, on the dual side, between M+(Ω) and Q(g1,... ,gH)∗.

- Theorem 8. Let Ω = {x ∈ Rd : g1(x) ≥ 0,... ,gH(x) ≥ 0} be a compact semialgebraic set such that g1,... ,gH satisfy an Archimedean condition. Then:


![image 26](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile26.png>)

4(8)≤(9) holds by considering the Jordan decomposition µ =: µ+ − µ− of a µ ∈ M(Ω) which is optimal for (8) and (9)≤(8) holds by considering µ := (µ+ − µ−)/ Ω d|µ+ − µ−| where µ+, µ− ∈ M+(Ω) are optimal for (9).

has a representing measure on Ω if and only if

(Real analysis facet): A real sequence y = (yℓ)ℓ∈Nd

0

Hankt(y) 0,Hankt(G1 y) 0,... ,Hankt(GH y) 0 for all t ∈ N.

Thus, a linear functional λ on Pd is (identiﬁed with an element) in M+(Ω) if and only if the sequence y = (λ(mℓ))ℓ∈Nd

satisﬁes the above semideﬁnite conditions.

0

(Real algebraic geometry facet): If p ∈ Pd is strictly positive on Ω, then p ∈ Q(g1,... ,gH). Conversely, any p ∈ Q(g1,... ,gH) is nonnegative on Ω.

Putinar’s Positivstellensatz may also be formulated as follows: if a polynomial p ∈ Pd is strictly positive on Ω, then there exists t ∈ N such that p ∈ Q(g1,... ,gH)t. As a result, one has

E∗ = inf

- (11) {c : c ± (f − p)(x) > 0 for all x ∈ Ω}

= inf

c∈R,p∈Pnd−1

{c : c ± (f − p) ∈ Q(g1,... ,gH)t for some t ∈ N}.

Since sums-of-squares can be modeled using semideﬁnite matrices, semideﬁnite programming can be used to compute, for any ﬁxed t ∈ N large enough5, an upper bound for E∗ as

- (12) ubt := inf c∈R,p∈Pnd−1

c subject to

c + f − p ∈ Q(g1,... ,gH)t, c − f + p ∈ Q(g1,... ,gH)t.

Notice that (ubt) forms a nonincreasing sequence and, according to (11), that limt→∞ ubt = E∗. The idea to construct such a sequence of semideﬁnite programs is originally due to Lasserre [13].

The sequence of dual semideﬁnite programs leads us to consider, for each t ∈ N,

ub′t := sup

y±∈R{0,...,2t}d |ℓ|≤N

- (13) coeﬀmℓ(f)(yℓ+ − yℓ−) s.to yℓ+ − yℓ− = 0, |ℓ| ≤ n − 1, y0+ + y0− = 1,


c∈R,p∈Pnd−1

and Hankt(y±) 0,Hankt−n′

(G1y±) 0,... ,Hankt−n′

1

H

(GHy±) 0,

where n′1 := ⌈deg(g1)/2⌉,... ,n′H := ⌈deg(gH)/2⌉. This program can be thought of as a truncation

- at level t of the program (9) in which µ± ∈ M+(Ω) would be replaced by their inﬁnite sequences of


moments yℓ± = Ω mℓ dµ±, ℓ ∈ Nd0. Here, the ﬁnite sequence y± represents pseudo-moments. Since the feasibility set of (9) is contained in the feasibility set of (13), one has E∗ ≤ ub′t, i.e., the ub′t are also upper bounds for E∗. Furthermore, by weak duality for semideﬁnite programs, one always has ub′t ≤ ubt. In view of limt→∞ ubt = E∗, it is therefore immediate that limt→∞ ub′t = E∗, too. The strong duality result ub′t = ubt is actually valid, since a constraint qualiﬁcation always holds, by a similar argument to [13, Theorem 4.2(a)]. For instance, one may construct a strictly feasible solution to the dual semideﬁnite program by setting µ+ = µ− equal to the uniform measure on Ω.

![image 28](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile28.png>)

5The semideﬁnite program of (12) may be infeasible for small t’s, in which case on has ubt = ∞, but Putinar’s Positivstellensatz guarantees that it is feasible for suﬃciently large t.

Having assumed that Ω has a nonempty interior, this implies that µ+ and µ− lie in the interior of (Q(g1,... ,gH)t)∗. The interested reader can ﬁnd more details in the proof of [13, Theorem 4.2(a)]. In particular, the dual semideﬁnite program is unbounded if the primal program (12) is infeasible.

In summary, the following result constituting the basis for our computational procedure has been established.

- Theorem 9. Let Ω = {x ∈ Rd : g1(x) ≥ 0,... ,gH(x) ≥ 0} be a compact semialgebraic set such that g1,... ,gH satisfy an Archimedean condition and let f ∈ PNd a polynomial f of degree N ≥ n. The values ubt and ub′t computed in (12) and (13) with t ≥ N + max{n′1,... ,n′H},


n′h := ⌈deg(gh)/2⌉, form nonincreasing sequences of upper bounds for the error EPd

(f,Ω) of best

n−1

approximation to f from Pnd−1 relative to Ω. Moreover, these sequences converge to the error of best approximation, i.e.,

ub′t = EPd

lim

ubt = lim

t→∞

t→∞

n−1

(f,Ω).

The above ideas have been implemented in the commands ChebPoly primal and ChebPoly dual, which require GloptiPoly 3. Although any semideﬁnite solver could have been used to solve (12) and (13), we chose GloptiPoly 3 because it oﬀers a more user-friendly way to formulate the problems. Another advantage is that, when solving (13), GloptiPoly 3 not only outputs moments but it can also extract the atomic measure generating them—the procedure used to do so is described in [11]. This corresponds to situations where the convergence of the sequence of upper bounds occurs in a ﬁnite number of steps, which is often the case in practice. While we do not know this number of steps in advance, in such cases, the precise value of EPd

![image 30](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile30.png>)

![image 31](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile31.png>)

(f,Ω) can be obtained by computing

n−1

ub′t (for t large enough) and certifying its genuine optimality “numerically” within GloptiPoly 3. Indeed, based on a deep result of Curto and Fialkow, GloptiPoly 3 veriﬁes a condition ensuring that

ub′t = EPd

(f,Ω) through a numerical estimation a rank drop in the Hankel matrices, see [11]. Such certiﬁcates substantiate the numerical values presented in the next section.

n−1

# 4 New Explicit Results

In this section, we present the discoveries that were made by exploiting the computational procedure just described. In particular, we consider the situation of d = 3 variables and give the values of the errors of best approximation from Pn3−1 to (essentially) all monomials mk of degree n up to 6. Excluding the already settled case where Ω is the hypercube, we report, from largest to smallest Ω, on the cases of the euclidean ball, the cross-polytope, and the simplex in Tables 1, 2, and 3, respectively. Their content can be reproduced by running the codes made available on https://github.com/foucart/Multivariate_Chebyshev_Polynomials. Note that an asterisk

(∗) appended to a value means that it could not be numerically certiﬁed6 by GloptiPoly 3. In a few instances, we could distill explicit expressions for previously unknown Chebyshev polynomials, see Theorems 10 and 11.

## 4.1 The euclidean ball

When Ω = B, the values of E(k,Ω) had earlier been found when |k| = 3 and |k| = 4, but not for |k| = 5 (except k = (3,1,1)) nor |k| = 6 (except k = (2,2,2)). All these values are shown in Table 1. Here and in other tables, the value of E(k,Ω) needs to be multiplied by the factor presented at the top of its column, so e.g. E((4,1,1),B) ≈ 1.923 × 10−2.

![image 33](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile33.png>)

![image 34](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile34.png>)

![image 35](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile35.png>)

![image 36](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile36.png>)

![image 37](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile37.png>)

![image 38](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile38.png>)

degree n = 3 (×10−1) degree n = 4 (×10−2) degree n = 5 (×10−2) degree n = 6 (×10−2) E((1,1,1),B) ≈ 1.924 E((2,1,1),B) ≈ 8.578 E((3,1,1),B) ≈ 4.016 E((4,1,1),B) ≈ 1.923

![image 39](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile39.png>)

![image 40](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile40.png>)

![image 41](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile41.png>)

![image 42](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile42.png>)

![image 43](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile43.png>)

![image 44](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile44.png>)

![image 45](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile45.png>)

![image 46](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile46.png>)

![image 47](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile47.png>)

![image 48](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile48.png>)

![image 49](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile49.png>)

![image 50](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile50.png>)

![image 51](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile51.png>)

E((2,2,1),B) ≈ 3.630 E((3,2,1),B) ≈ 1.652 E((2,2,2),B) ≈ 1.388

![image 52](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile52.png>)

![image 53](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile53.png>)

![image 54](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile54.png>)

![image 55](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile55.png>)

![image 56](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile56.png>)

![image 57](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile57.png>)

![image 58](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile58.png>)

Table 1: Euclidean ball in dimension d = 3: the previously unknown values are shown in boldface.

In the case k = (2,2,1), it was possible to recognize (part of) the signature points, which led us to deriving a Chebyshev polynomial explicitly. The result reads as follows.

- Theorem 10. With a := max (1 + t)2(1 − t)t/(4(1 + 4t + 4t2)),t ∈ [0,1] ≈ 3.63000825 × 10−2,


the error of best approximation on the euclidean ball to m(2,2,1)(x1,x2,x2) = x21x22x3 by trivariate polynomials of degree at most 4 is

EP3

(m(2,2,1),B) = a,

4

while a Chebyshev polynomial is given by

P(x) = m(2,2,1)(x1,x2,x3) + aT3(x3),

where T3(t) = 4t3 − 3t is the univariate Chebyshev polynomial of degree 3.

Proof. Guided by our computational procedure, we make the guess—which we are about to verify—

![image 59](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile59.png>)

6To be sure, it is the value of the error of best approximation that is certiﬁed, not the extracted atomic measure. In the case of m(2,2,1) on the simplex, for instance, even though the value E((2, 2, 1), S) ≈ 4.695 × 10−4 is certiﬁed, the extracted atomic measure suﬀers from numerical inaccuracies. This case is challenging—we have tried to derive an explicit solutions from our computations, without any success.

that a signature has support S = S+ ∪ S−, where S− = −S+ and

 

  ,

  ,

  ,

  

  

  

  ,

  

  ,

  

√3/2

√3/2 0 −1/2

![image 61](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile61.png>)

![image 62](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile62.png>)

−

0 √3/2 −1/2

0

0 −

√3/2 −1/2

S+ =

![image 63](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile63.png>)

![image 64](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile64.png>)

0 −1/2

- 0
- 1




 

  ,

  ,

  ,

  

  

  

  

  

![image 65](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile65.png>)

![image 66](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile66.png>)

![image 67](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile67.png>)

![image 68](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile68.png>)

(1 − τ2)/2 (1 − τ2)/2

(1 − τ2)/2

− (1 − τ2)/2 − (1 − τ2)/2 τ

(1 − τ2)/2

![image 69](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile69.png>)

![image 70](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile70.png>)

![image 71](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile71.png>)

![image 72](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile72.png>)

− (1 − τ2)/2 τ

− (1 − τ2)/2 τ

.



τ

For reasons soon to become apparent, the parameter τ ≈ 0.4052 is chosen as the maximizer of (1 + t)2(1 − t)t/(4(1 + 4t + 4t2)) over t ∈ [0,1], so that (1 + τ)2(1 − τ)τ/4 = a(1 + 4τ + 4τ2). Multiplying throughout by (1 − τ) yields ((1 − τ2)/2)2τ = a(1 − T3(τ)). As for best approximants to m(2,2,1) from P43, we shall show, in two steps, that p∗(x1,x2,x3) := −aT3(x3) is one of them.

The ﬁrst step consists in proving that |(m(2,2,1) − p∗)(x)| = m(2,2,1) − p∗ B for all x ∈ S. To see this, we start by noticing that (m(2,2,1) − p∗)(x) = a for all x ∈ S+—this is a simple veriﬁcation by plugging in the values x ∈ S+ into (m(2,2,1) − p∗)(x), but we emphasize that (m(2,2,1) − p∗)(±

√1 − τ2,±

√1 − τ2,τ) = ((1 − τ2)/2)2τ + aT3(τ) = a owes to our choice of τ. Then, from S− = −S+ and the oddity of m(2,2,1), it follows that (m(2,2,1) − p∗)(x) = −a for all x ∈ S−. All in all, we arrived at |(m(2,2,1) − p∗)(x)| = a for all x ∈ S. Next, we claim that |(m(2,2,1) − p∗)(x)| ≤ a for all x ∈ B. By the oddity of m(2,2,1) again, it is enough to establish, for all x ∈ B, that (m(2,2,1) −p∗)(x) ≤ a, i.e., that x21x22x3 ≤ a(1−T3(x3)). If x3 ∈ [−1,0], this is clear. If x3 ∈ [0,1], it relies on the deﬁnition of a in the last inequality of the chain

![image 73](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile73.png>)

![image 74](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile74.png>)

(1 + x3)2(1 − x3)x3 4 ≤ (1 − x3) a(1 + 4x3 + 4x23) = a(1 − T3(x3)).

(1 − x23)2 4

(x21 + x22)2 4

x21x22x3 ≤

x3 ≤

x3 = (1 − x3)

![image 75](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile75.png>)

![image 76](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile76.png>)

![image 77](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile77.png>)

Altogether, we have obtained |(m(2,2,1) −p∗)(x)| = m(2,2,1) −p∗ B = a for all x ∈ S, as announced.

The second step comprises showing that m(2,2,1) −p B ≥ a for any p ∈ P43, or in fact for some best approximant p to m(2,2,1) from P43. Let us momentarily take for granted that v = p∗ − p satisﬁes v(x) ≥ 0 for some x ∈ S+. With the help of this x ∈ S+, we derive

m(2,2,1) − p B ≥ (m(2,2,1) − p)(x) = (m(2,2,1) − p∗)(x) + (p∗ − p)(x) = a + v(x) ≥ a,

as desired. Thus, it remains to justify that existence of x ∈ S+ such that v(x) ≥ 0. According to Proposition 4, the best approximant p can be chosen to inherit properties of m(2,2,1), in particular being odd in x3, even in x1 and x2, and symmetric when swapping x1 and x2. Therefore, one can choose p to contain only the terms x3, x33, and (x21 + x22)x3, and when restricted to the boundary of B, it contains only the terms x3 and x33, just like p∗. As a consequence, we write, for some c,d ∈ R, v(x) = cx3 + dx33 for all x ∈ S+. Now assume by contradiction that v(x) < 0 for all x ∈ S+. This translates, after simpliﬁcation, into c+d < 0, −4c−d < 0, and τ−2c+d < 0. Adding

the second to the ﬁrst yields −3c < 0, while adding the second to the third yields (τ−2 − 4)c < 0, which is impossible since τ−2 ≈ 6.088 > 4. Thanks to this contradiction, the proof is complete.

![image 79](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile79.png>)

![image 80](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile80.png>)

![image 81](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile81.png>)

![image 82](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile82.png>)

We have seen that the signature in the above proof was supported on the boundary of the ball. As a matter of fact, this is a phenomenon we noticed in all cases (where we could extract signatures). We thus conjecture that, for the approximation of monomials on the euclidean ball, signatures actually live on the sphere.

## 4.2 The cross-polytope

To the best of our knowledge, Chebyshev polynomials relative to the cross-polytope have not been investigated in the literature, hence the values of E(k,C) reported in Table 2 seem to all be new. As expected, they are smaller than the values of E(k,B) presented in Table 1 and larger than the values of E(k,S) shown in Table 3.

![image 83](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile83.png>)

![image 84](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile84.png>)

![image 85](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile85.png>)

![image 86](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile86.png>)

![image 87](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile87.png>)

![image 88](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile88.png>)

degree n = 3 (×10−2) degree n = 4 (×10−2) degree n = 5 (×10−3) degree n = 6 (×10−3) E((1,1,1),C) ≈ 3.703 E((2,1,1),C) ≈ 1.273 E((3,1,1),C) ≈ 4.764 E((4,1,1),C) ≈ 1.853∗

![image 89](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile89.png>)

![image 90](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile90.png>)

![image 91](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile91.png>)

![image 92](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile92.png>)

![image 93](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile93.png>)

![image 94](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile94.png>)

![image 95](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile95.png>)

![image 96](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile96.png>)

![image 97](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile97.png>)

![image 98](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile98.png>)

![image 99](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile99.png>)

![image 100](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile100.png>)

![image 101](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile101.png>)

E((2,2,1),C) ≈ 3.398 E((3,2,1),C) ≈ 1.087 E((2,2,2),C) ≈ 0.661∗

![image 102](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile102.png>)

![image 103](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile103.png>)

![image 104](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile104.png>)

![image 105](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile105.png>)

![image 106](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile106.png>)

![image 107](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile107.png>)

![image 108](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile108.png>)

Table 2: Cross-polytope in dimension d = 3: all values were previously unknown.

## 4.3 The simplex

When Ω = S, the values of E(k,Ω) had earlier been found when |k| = 3, but not for |k| = 4, |k| = 5, and |k| = 6 (except k = (2,2,2)). All these values are shown in Table 3. It appears empirically that signatures (when they could be extracted) live on the boundary of the domain, and more precisely here on the face of equation x1 + x2 + x3 = 1. Note that this would imply, due to the close connection between the approximation of mk on S and the approximation of m2k on B, some particular cases of the conjecture relative to B.

![image 109](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile109.png>)

![image 110](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile110.png>)

![image 111](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile111.png>)

![image 112](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile112.png>)

![image 113](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile113.png>)

![image 114](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile114.png>)

degree n = 3 (×10−2) degree n = 4 (×10−3) degree n = 5 (×10−4) degree n = 6 (×10−4) E((1,1,1),S) ≈ 1.388 E((2,1,1),S) ≈ 2.688 E((3,1,1),S) ≈ 5.984∗ E((4,1,1),S) ≈ 1.405∗

![image 115](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile115.png>)

![image 116](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile116.png>)

![image 117](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile117.png>)

![image 118](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile118.png>)

![image 119](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile119.png>)

![image 120](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile120.png>)

![image 121](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile121.png>)

![image 122](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile122.png>)

![image 123](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile123.png>)

![image 124](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile124.png>)

![image 125](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile125.png>)

![image 126](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile126.png>)

![image 127](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile127.png>)

E((2,2,1),S) ≈ 4.695 E((3,2,1),S) ≈ 1.000∗ E((2,2,2),S) ≈ 0.6265

![image 128](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile128.png>)

![image 129](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile129.png>)

![image 130](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile130.png>)

![image 131](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile131.png>)

![image 132](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile132.png>)

![image 133](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile133.png>)

![image 134](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile134.png>)

Table 3: Simplex in dimension d = 3: the previously unknown values are shown in boldface.

In the case k = (2,1,1), we could use the insight brought forward by our computations to derive a Chebyshev polynomial explicitly. The result reads as follows.

- Theorem 11. With τ ∈ [0,1/4] being the solution to max y(1−2y)(y−τ)2,y ∈ [0,1/2] = τ2/18


and with c := −3/τ, the error of best approximation on the simplex to m(2,1,1)(x1,x2,x3) = x21x2x3 by trivariate polynomials of degree at most 3 is

- 1

![image 136](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile136.png>)

- 2c2


EP3

(m(2,1,1),S) =

,

3

while a Chebyshev polynomial is given by

P(x) = x21x2x3

- 1

![image 137](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile137.png>)

- 2c2 −16x21(x2 + x3) + 16x1(x2 + x3)2 − 2(64 + 12c + c2)x1x2x3 + 8x2x3 − 2(x2 + x3) + 1 .


+

Proof. Guided by our computational procedure, we make the guess—which we are about to verifythat there is a signature with support S = S+ ∪ S−, where

 

 

  

  ,

  

  ,

  

  ,

  

  ,

  

  

1/4 3/4 0

1/4 0 3/4

- 0
- 1/2
- 1/2


1 0 0

1 − 2τ τ τ

S+ =

,





 

 

  

  ,

  

  ,

  

  ,

  

  ,

  

  

3/4 1/4 0

3/4

0

- 0
- 1 0


1 − 2σ σ σ

S− =

.

- 0
- 1/4


- 0
- 1






The parameters τ,σ ∈ [0,1/2] are considered free for now—their speciﬁc choice will be revealed later.

The ﬁrst step consists in proving that |P(x)| = P S for all x ∈ S. To this end, we start by proving that P S ≤ 1/(2c2), i.e., that |P(x1,x2,x3)| ≤ 1/(2c2) whenever x1,x2,x3 ≥ 0 and x1+x2+x3 ≤ 1. This is easy to see if x1 = 0, since then 2c2 P(0,x2,x3) = 8x2x3 − 2(x2 + x3) + 1 is bounded as

≥ −2(x2 + x3) + 1 ≥ −2 + 1 = −1, ≤ 2(x2 + x3)2 − 2(x2 + x3) + 1 ≤ 1.

Using the fact that 8t(1 − 2t) ≤ 1 for all t ∈ R, it is also easy to see that |P(x1,x2,x3)| ≤ 1/(2c2) if x2 = 0 or x3 = 0, since, e.g., 2c2 P(x1,x2,0) = −16x21x2 + 16x1x22 − 2x2 + 1 is

= −2x1[8x2(x1 − x2)] − 2x2 + 1 ≥ −2x1[8x2(1 − 2x2)] − 2x2 + 1 ≥ −2x1 − 2x2 + 1 ≥ −1, 2x2[8x1(x2 − x1)] − 2x2 + 1 ≤ 2x2[8x1(1 − 2x1)] − 2x2 + 1 ≤ 2x2 − 2x2 + 1 = 1.

We therefore consider the case where x1,x2,x3 are all nonzero and we notice that we can assume x2 = x3. Indeed, if we reparametrize by setting y = (x2 + x3)/2 and z = (x2 − x3)/2, so that

x2x3 = y2 − z2, then the expression for P(x) becomes

1

P(x) = x21y2 +

- (14) 2c2 −32x21y + 64x1y2 − 2(64 + 12c + c2)x1y2 + 8y2 − 4y + 1 − x21z2 +

- 1

![image 139](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile139.png>)

- 2c2


2(64 + 12c + c2)x1z2 − 8z2

=

- 1

![image 140](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile140.png>)

- 2c2


2c2x21y2 − 32x21y − 2(32 + 12c + c2)x1y2 + 8y2 − 4y + 1 − z2q(x1)

for some univariate quadratic polynomial q. Thus, given x ∈ S such that |P(x)| = P S and t ∈ R small enough, we deﬁne x(t) ∈ S by x(1t) = x1, x(2t) = x2 + t, and x(3t) = x3 − t. In view of (x(2t) + x(3t)) = (x2 + x3)/2 =: y and of (x(2t) − x(3t)) = (x2 − x3)/2 + t =: z + t, while supposing e.g. that P(x) > 0, the inequality P(x(t)) ≤ P(x) reads P(x1,y,y)−(z+t)2q(x1) ≤ P(x1,y,y)−z2q(x1) whenever |t| is small enough. This implies that zq(x1) = 0, hence that P(x) = P(x1,y,y), meaning that the last two coordinates of an extremal point can be assumed to be equal, as claimed. Now, to determine the maximum of |P(x1,y,y)| when x1,y ≥ 0 and x1 +2y ≤ 1, we recall from (14) that

- (15) P(x1,y,y) =

- 1

![image 141](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile141.png>)

- 2c2


2c2x21y2 − 32x21y − 2(32 + 12c + c2)x1y2 + 8y2 − 4y + 1 , so that

∂P(x1,y,y) ∂y

![image 142](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile142.png>)

=

- 1

![image 143](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile143.png>)

- 2c2


4c2x21y − 32x21 − 4(32 + 12c + c2)x1y + 16y − 4 . As a consequence, at a critical point, we have (32+12c+c2)x1y = c2x21y −8x21 +4y −1 and in turn P(x1,y,y) =

- 1

![image 144](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile144.png>)

- 2c2 −16x21y − 2y + 1 .


It follows that |P(x1,y,y)| ≤ 1/(2c2) at any critical point, since [−16x21y − 2y + 1] ≤ 1 is clear, while [−16x21y − 2y + 1] ≥ −1 holds because 16x21y + 2y = 2y(8x21 + 1) ≤ (1 − x1)(8x21 + 1), the latter having maximal value (68+5√10)/54 ≈ 1.5520 ≤ 2 over x1 ∈ [0,1]. At this point, it remains to verify that |P(x1,y,y)| ≤ 1/(2c2) on the boundary of the domain {x1 ≥ 0,y ≥ 0,x1 + 2y ≤ 1}. Since the cases x1 = 0 and y = 0 have already been dealt with, we need to consider the case x1 = 1 − 2y, y ∈ [0,1/2]. After some technical calculations left to the reader, starting from (15) and recalling that τ = −3/c, we arrive at

![image 145](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile145.png>)

- (16) P(1 − 2y,y,y) =


![image 146](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile146.png>)

- 1

![image 147](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile147.png>)

- 2c2 − 2y(1 − 2y)(y − τ)2, y ∈ [0,1/2].


The inequality P(1 − 2y,y,y) ≤ 1/(2c2) is obvious from here. The parameter τ is chosen to secure the other inequality P(1 − 2y,y,y) ≥ −1/(2c2), which is equivalent to y(1 − 2y)(y − τ)2 ≤ 1/(2c2) for all y ∈ [0,1/2] and thus follows from the equation max y(1−2y)(y −τ)2,y ∈ [0,1/2] = τ2/18. Note that this equation has a (unique) solution in [0,1/4], because τ2/18 increases from 0 to 1/288 on this interval and max y(1−2y)(y−τ)2,y ∈ [0,1/2] decreases from a positive quantity to 1/512 there. In consequence, we have now established that |P(x)| ≤ 1/(2c2) for all x ∈ S, as announced. Let us turn to the justiﬁcation that |P(x)| = 1/(2c2) for all signature points x ∈ S = S+ ∪ S−. From (16), we immediately see that P(x) = 1/(2c2) for the last three points of S+. The fact that

P(x) = −1/(2c2) for the last point of S− is due to the choice of σ, as we take it to be the maximizer of y(1 − 2y)(y − τ)2 over y ∈ [0,1/2], ensuring that σ(1 − 2σ)(σ − τ)2 = 1/(2c2) and hence that P(1 − 2σ,σ,σ) = −1/(2c2). As for the other signature points, notice that they are of the form (1 − y,y,0) or (1 − y,0,y), for which technical calculations left to the reader yield

- 1

![image 149](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile149.png>)

- 2c2


P(1 − y,y,0) = P(1 − y,0,y) = −

T3(2y − 1), y ∈ [0,1],

where, as usual, T3(t) = 4t3 −3t is the univariate Chebyshev polynomial of degree 3. It then easily follows that P(x) = 1/(2c2) for the ﬁrst two points of S+ and that P(x) = −1/(2c2) for the ﬁrst four points of S−. Altogether, we have now obtained |P(x)| = P S = 1/(2c2) for all x ∈ S, as announced.

The second step consists in proving that m(2,1,1) − p S ≥ 1/(2c2) for any p ∈ P33. To this end, we notice that all signature points x ∈ S lie on the face F := {x1 ≥ 0,x2 ≥ 0,x3 ≥ 0,x1 +x2 +x3 = 1} and we remark that {(x1,x2) : x ∈ S} is the support of an extremal signature for P32 associated with P|F, in the sense that there exist cx > 0, x ∈ S, such that x∈S cx sgn(P(x))r(x1,x2) = 0 for all r ∈ P32. This can be veriﬁed (numerically) by looking at the null space of the 10 × 10 matrix with entry sgn(P(x))m(k1,k2)(x1,x2) on the row indexed by (k1,k2) with k1 + k2 ≤ 3 and on the column indexed by x ∈ S. Theorem 2 could now be invoked. Alternatively, given p ∈ P33, we can write m(2,1,1) − p = P − q for some q ∈ P33 and consider an x ∈ S such that sgn(P(x))q(x) ≤ 0, which is possible for otherwise x∈S cx sgn(P(x))q(x1,x2,1 − x2 − x3) = 0 would be violated. In this way, the desired inequality follows from

- 1

![image 150](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile150.png>)

- 2c2


.

m(2,1,1) − p S ≥ |P(x) − q(x)| ≥ |P(x)| =

The proof is now complete. Remark. The numerical values of the parameters τ and σ are τ ≈ 0.21998 and σ ≈ 0.41942, leading to the error of best approximation the numerical value EP3

![image 151](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile151.png>)

![image 152](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile152.png>)

![image 153](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile153.png>)

![image 154](<2024-dressler-optimization-aided-construction-multivariate-c_images/imageFile154.png>)

(m(2,1,1),S) ≈ 2.68850 × 10−3. In fact, it can be shown (a computer algebra system will facilitate the task) that τ is the smallest real root of the quartic polynomial 2880t4 − 5472t3 + 4880t2 − 1944t + 243.

3

# 5 Conclusion

In this article, we proposed a semideﬁnite-programming method to compute best approximants to monomials by multivariate polynomials of lower degree. More than providing numerical values, the method allows us to make guesses for the multivariate analogs of Chebyshev polynomials that cansometimes—be a posteriori certiﬁed explicitly or symbolically. Of note, the generic nonuniqueness of such analogs prompted us to preferentially solve the dual optimization program, putting the classical notion of signature at center stage. We emphasize that the underlying methodology is

quite versatile and should enable to attack other problems in multivariate Approximation Theory by relying on modern tools from Optimization Theory, so long as one is ready to give up on purely analytical solutions. This is a point of view already brought forward by a subset of the authors to determine minimal projections (exploiting moments, see [7]) and Chebyshev polynomials associated to union of intervals (exploiting sums-of-squares, see [8]). In the multivariate setting, we should also be able to deal with unions of domains, as well as tackling norms other than L∞ (notably L1 and L2m, m ∈ N), adding convex constraints (e.g. interpolatory, shape-enforcing, etc), in the spirit of the proof-of-concept software Basc, short for ‘Best Approximations by Splines under Constraints’, see [9]. We note, though, that the semideﬁnite programs encountered in Basc could only be handled thanks to the beneﬁts of representing univariate polynomials in the Chebyshev basis rather than in the monomial basis, so a similar approach should be taken in the multivariate setting. This is indeed realizable, at least in theory, and we give pointers on how to do this in some supplementary material. Still, bringing Basc to the multivariate realm will be a mighty task, but certainly one worth taking by a fresh generation of approximators/optimizers.

Acknowledgment. This work is the result of a collaboration made possible by the SQuaRE program at the American Institute of Mathematics (AIM). We are truly grateful to AIM for the supportive and mathematically rich environment they provided. In addition, we owe thanks to several funding agencies, as M. D. is supported by the Australian Research Council Discovery Early Career Award DE240100674, S. F. is partially supported by grants from the National Science Foundation (DMS-2053172) and from the Oﬃce of Naval Research (N00014-20-1-2787), E. de K. is supported by grants from the Dutch National Science Foundation (NWO) (OCENW.M.23.050 and OCENW.GROOT.2019.015), J. B. L. is supported by the AI Interdisciplinary Institute through the French program “Investing for the Future PI3A” (ANR-19-PI3A-0004) and by the National Research Foundation, Singapore, through the DesCartes and Campus for Research Excellence and Technological Enterprise (CREATE) programs, and Y. X. is partially supported by the Simons Foundation (grant #849676).

# References

- [1] N. N. Andreev and V. A. Yudin. Polynomials of least deviation from zero and Chebyshev-type cubature formulas. Proceedings of the Steklov Institute of Mathematics, 232, 39–51, 2001.
- [2] N. N. Andreev and V. A. Yudin. Best approximation of polynomials on the sphere and on the ball. In: Recent Progress in Multivariate Approximation, International Series of Numerical Mathematics 137. Birkh¨auser, 2001.
- [3] B. D. Bojanov, W. Haussmann, and G. P. Nikolov. Bivariate polynomials of least deviation from zero. Canadian Journal of Mathematics, 53, 489–505, 2001.


- [4] P. L. Chebyshev. Sur les questions de minima qui se rattachent a` la repre´sentation approximative des fonctions. Me´moires de l’Acade´mie Impe´riale des Sciences de St.-Petersbourg, 7, 199–291, 1859.
- [5] M. Dressler, S. Foucart, M. Joldes, E. de Klerk, J. B. Lasserre, and Y. Xu. Least multivariate Chebyshev polynomials on diagonally determined domains. arXiv:2405.19219v1 [math.OC].
- [6] H. Ehlich and K. Zeller. Cebyˇ ˇsev-Polynome in mehreren Ver¨nderlichen. Mathematische Zeitschrift, 93, 142–143, 1966.
- [7] S. Foucart and J. B. Lasserre. Determining projection constants of univariate polynomial spaces. Journal of Approximation Theory, 235, 74–91, 2018.
- [8] S. Foucart and J. B. Lasserre. Computation of Chebyshev polynomials for union of intervals. Computational Methods and Function Theory, 19/4, 625–641, 2019.
- [9] S. Foucart and V. Powers. Basc: constrained approximation by semideﬁnite programming. IMA Journal of Numerical Analysis, 37/2, 1066–1085, 2017.
- [10] W. B. Gearhart. Some Chebyshev approximations by polynomials in two variables. Journal of Approximation Theory, 8, 195–209, 1973.
- [11] D. Henrion and J.B. Lasserre. Detecting global optimality and extracting solutions in GloptiPoly. In: Positive Polynomials in Control, Lecture Notes in Control and Information Science

312. Springer, 2005.

- [12] D. Henrion, J. B. Lasserre, and J. Loefberg. GloptiPoly 3: moments, optimization and semideﬁnite programming. Optimization Methods and Software, 24/4-5, 761–779, 2009. https://homepages.laas.fr/henrion/software/gloptipoly3/
- [13] J.B. Lasserre. Global optimization with polynomials and the problem of moments. SIAM Journal on Optimization 11, 796–817, 2001.
- [14] J. B. Lasserre. The Moment-SOS Hierarchy. In: Proceedings of the International Congress of Mathematicians (ICM 2018). World Scientiﬁc, pp. 3773–3794, 2019.
- [15] M. Laurent and F. Rendl. Semideﬁnite Programming and Integer Programming. In: Handbooks in Operations Research and Management Science. Elsevier, pp. 393–514, 2005.
- [16] I. Moale and F. Peherstorfer. An explicit class of min–max polynomials on the ball and on the sphere. Journal of Approximation Theory 163/6, 724–737, 2011.
- [17] D. J. Newman and Y. Xu. Tchebycheﬀ polynomials on a triangular region. Constructive Approximation, 9/4, 543–546, 1993.
- [18] M. Putinar. Positive polynomials on compact semi-algebraic sets. Indiana University Mathematics Journal, 42/3, 969–984, 1993.


- [19] M. Reimer. On multivariate polynomials of least deviation from zero on the unit ball. Mathematische Zeitschrift, 153, 51–58, 1977.
- [20] H. Richter. Parameterfreie Abscha¨tzung und Realisierung von Erwartungswerten, Deutsche Gesellschaft fu¨r Versicherungsmathematik, 3, 147–162, 1957.
- [21] T. J. Rivlin. Chebyshev Polynomials. Second edition. Courier Dover Publications, 2020.
- [22] T. J. Rivlin and H. S. Shapiro. A uniﬁed approach to certain problems of approximation and optimization. SIAM Journal on Numerical Analysis, 9, 670–699, 1961.
- [23] K. Schmu¨dgen. The Moment Problem. Springer, 2017.
- [24] J. Sloss. Chebyshev approximation to zero. Paciﬁc Journal of Mathematics, 15/1, 305–313, 1965.
- [25] V. A. Yudin, Best approximation to monomials on a cube. Sbornik Mathematics, 199, 1251– 1262, 2008.
- [26] Y. Xu. On polynomials of least deviation from zero in several variables. Experimental Mathematics, 13, 103–112, 2004.
- [27] Y. Xu. Best approximation of monomials in several variables. Rendiconti del Circolo Matematico di Palermo Series 2, 76, 129–155, 2005.


