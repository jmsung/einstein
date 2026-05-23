---
type: source
kind: paper
title: Equivariant log-concavity and equivariant Kähler packages
authors: Tao Gui, Rui Xiong
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2205.05420v3
source_local: ../raw/2022-gui-equivariant-log-concavity-equivariant-hler.pdf
topic: general-knowledge
cites:
---

arXiv:2205.05420v3[math.RT]17Oct2024

EQUIVARIANT LOG-CONCAVITY AND EQUIVARIANT KAHLER¨ PACKAGES

TAO GUI

Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Beijing, P.R. China

RUI XIONG

Department of Mathematics and Statistics, University of Ottawa, 150 Louis-Pasteur, Ottawa, ON, K1N 6N5, Canada

Abstract. We show that the exterior algebra ΛR [α1, · · · , αn], which is the cohomology of the torus T = (S1)n, and the polynomial ring R [t1, . . . , tn], which is the cohomology of the classifying space B(S1)n = (CP∞)n, are Snequivariantly log-concave. We do so by explicitly giving the Sn-representation maps on the appropriate sequences of tensor products of polynomials or exterior powers and proving that these maps satisfy the hard Lefschetz theorem. Furthermore, we prove that the whole K¨hler package, including the Poincar´e duality, the hard Lefschetz theorem, and the Hodge–Riemann bilinear relations, holds on the corresponding sequences in an equivariant setting.

Keywords. Log-concavity, Representation of symmetric group, Tensor products of representation, Equivariant log-concavity, Hard Lefschetz, K¨hler package

1. Introduction

The K¨ahler package is an algebraic structure that satisﬁes a “package” of properties tending to come bundled together: Poincar´e duality, hard Lefschetz, and Hodge–Riemann bilinear relations. They were ﬁrst discovered in the cohomology of smooth complex projective algebraic varieties, or more generally, compact K¨ahler manifolds, but have since become quite ubiquitous in a realm that goes beyond that of K¨hler geometry. For example, see [1–4,7,11,12,23,28,36]. In this paper, we discover two new K¨hler packages that are equivariant and have no geometric origin, see Theorem 1 (Theorem 7 and 12). The equivariant log-concavity hints at our discoveries for these structures.

Recall that a sequence of real numbers a0,a1,... is called log-concave if a2i ≥ ai−1ai+1 for all i ≥ 1.

![image 1](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile1.png>)

E-mail addresses: guitao18@mails.ucas.ac.cn, rxion043@uottawa.ca.

1

A ﬁnite log-concave sequence of positive numbers is always unimodal, that is, there exists an index i such that

a0 ≤ ··· ≤ ai−1 ≤ ai ≥ ai+1 ≥ ··· ≥ ad.

Log-concave and unimodal sequences turn out to be very common in algebra, geometry, and combinatorics, see [6, 34, 35]. However, proving that certain speciﬁc sequences are log-concave might be quite diﬃcult. Some recent work [1,5,20] found a deep connection between log-concavity and Hodge–Riemann bilinear relations of Hodge theory, see the ICM paper [21] for a survey.

Many log-concave phenomena appear in representation theory and algebraic topology. For example, Nakajima [29] proved that the Kirillov–Reshetikhin modules satisfy log-concave-type properties known as the T-system and Q-system for quantum loop algebras. Okounkov [31] introduced the Newton–Okounkov bodies to prove that, in the asymptotic sense, the multiplicities of the homogeneous coordinate ring of a G-stable irreducible subvariety of P(V ) are log-concave for any representation V of a reductive group G. In a sequel paper [32], based on heuristics and analogies of physical principles, Okounkov made a remarkable conjecture that the Littlewood–Richardson coeﬃcients cνλµ are log-concave in (λ,µ,ν). Although Okounkov’s conjecture is false in general [9], many consequences and interesting special cases are true, see for example [22,25,26].

Another log-concavity phenomenon comes from group actions. Following [27], see also [32], we say that a sequence of ﬁnite-dimensional representations V0,V1,..., for example, a graded representation V = ∞i=0 Vi, is equivariantly log-concave if

- (1.1) Vi−1 ⊗ Vi+1 is a subrepresentation of Vi ⊗ Vi, for all i ≥ 1,


which is a categoriﬁcation of the log-concavity of its dimension sequence. Suppose a group G acts on a topological space X, which induces a graded representation of

- G on the cohomology H∗(X). If H∗(X) is equivariantly log-concave, then the Betti numbers of X form a log-concave sequence. In [27], the authors made G-equivariant log-concavity conjectures for the cohomology of various conﬁguration spaces and exploited the theory of representation stability to give computer-assisted proofs in low degrees for G = Sn. But despite the strong experimental evidence, they did not propose any strategy that could prove Sn-equivariant log-concavity for all n in all degrees, and the full conjectures remain open.


Our results can be viewed as an attempt to attack these equivariantly log-concave conjectures. Our approach is to reduce the problem of equivariant log-concavity to the equivariant unimodality of appropriate tensor product sequences and establish the hard Lefschetz theorem to prove the unimodality. In this paper, we use this idea to establish the equivariant log-concavity for the polynomial ring and the exterior algebras by explicit construction of equivariant Lefschetz operators. Actually, more is true —the Hodge–Riemann relations also hold which forms an equivariant K¨ahler package combined with Poincar´e duality and hard Lefschetz.

Denote

Hn,m =

m

Hn,m−m+2i, with Hn,m−m+2i := Di ⊗ Rm−i,

i=0

where Di (resp., Rm−i) denotes the degree-i (resp., degree-(m − i)) piece of the polynomial ring D = R[d1,...,dn] (resp., R = R[x1,...,xn]). Let

n

∂ ∂xi

L : Hn,mi −→ Hn,mi+2, where L :=

di ⊗

.

![image 2](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile2.png>)

i=1

We deﬁne a pairing on Hn,m, see formula (4.1). Similarly, denote

Hn,m′ =

m

(Hn,m′ )−m+2i, with (Hn,m′ )−m+2i := Λi ⊗ (Λ∗)m−i,

i=0

where Λi (resp., (Λ∗)m−i) denotes the degree- i (resp., degree-(m − i)) piece of the exterior algebra Λ(V ) = ΛR [θ1,...,θn] (resp., Λ(V ∗) = ΛR [ξ1,...,ξn]), we demand that θ1,...,θn and ξ1,...,ξn form dual basis of V and V ∗. Let

n

L : (Hn,m′ )i −→ (Hn,m′ )i+2, where L :=

eθ

⊗ iθ

,

k

k

k=1

here eθ

) is the exterior (resp., interior) product with θk. We deﬁne a pairing on Hn,m′ , see formula (4.5).

(resp., iθ

k

k

Sn naturally acts on the spaces. The followings are our main results. Theorem 1 (Theorem 7 and 12). Under the notations introduced above, for H = Hn,m or Hn,m′ , we have

- (a) (Poincare´ duality) For all i ≥ 0, the bilinear pairing  −,−  : Hi × H−i −→ R

is Sn-equivariant and non-degenerate;

- (b) (Hard Lefschetz) The corresponding operator L : Hi −→ Hi+2 is Snequivariant and satisfying hard Lefschetz, i.e., for all i ≥ 0,

Li : H−i −→ Hi is an isomorphism.

- (c) (Hodge–Riemann relations) For all 0 ≤ i ≤ m/2, the Lefschetz form on H−m+2i, deﬁned by


(a,b)−Lm+2i := a,Lm−2ib , is Sn-equivariant and (−1)i-deﬁnite on PL−m+2i := ker Lm−2i+1 ∩H−m+2i.

The corresponding equivariant Lefschetz operators give the explicit maps realizing the equivariant log-concavity of the symmetric powers and the exterior powers as graded representations of Sn. And, in fact, they are equivariant for the symmetric powers and the exterior powers of any representation of any group G; see Remark 9.

Corollary 2. The symmetric powers (polynomial ring) and the exterior powers (exterior algebra) of a given representation V of any group G are equivariantly logconcave. Furthermore, the required injective maps are given by the corresponding equivariant Lefschetz operators L above.

For polynomial rings, the Lefschetz operator L is essentially the same as observed in [18, Section 3.1], but we rediscover it from a diﬀerent perspective: d1,...,dn and x1,...,xn should live in the dual vector spaces and form a dual basis. Thus, our pairing (4.1) diﬀers from the more classical apolar form in diagonal harmonic theory. Our pairing (4.1) is compatible with the Lefschetz operator L, and we discover that the resulting Lefschetz form satisﬁes Hodge–Riemann bilinear relations, which is much stronger than hard Lefschetz, forming a full K¨hler package combined with Poincar´e duality and hard Lefschetz.

For the exterior algebra, the Lefschetz operator L is new, and we establish the full K¨hler package in the equivariant setting. We also ﬁnd that the “usual” gradings on tensor products of the exterior algebra satisfy Poincar´e duality and hard Lefschetz but not Hodge–Riemann relations, see Theorem 16 and Remark 17. The hard Lefschetz theorem for this grading is essentially the same as [24, Theorem 3.2], but our proof is simpler than theirs since their proof is combinatorial and relies on the incidence matrix of the Boolean poset. They use the equivariant Lefschetz element as a key tool to study the fermionic diagonal coinvariants. We would like to see whether our constructions have other implications for the diagonal coinvariant ring and the fermionic diagonal coinvariant ring.

The detailed constructions and proofs of the aforementioned theorems will be given in Section 4. Our constructions have the following notable features:

- • The Poincar´e pairing  −,− , the Lefschetz operator L, and the Lefschetz form (a,b)−Lm+2i are all Sn-equivariant, which is rare in Lefschetz theory.
- • The adjoint operator of the Lefschetz operator L can be written explicitly.
- • The proof of hard Lefschetz and Hodge–Riemann relations is natural and it takes advantage of the geometry of the product of projective spaces.


It would be interesting to know whether our approach could shed some new light on other (equivariant) log-concavity questions and conjectures.

2. Preliminaries: Kahler¨ package and Lefschetz linear algebra

In this section, we recall properties in the K¨hler package in the linear algebra context and refer to [11, Section 2] and [10, Chapter 17] for the omitted details.

Consider a graded ﬁnite-dimensional real vector space H =

Hi.

i∈Z

We denote bi = dimHi, the i-th Betti number of H. We say H satisﬁes Poincare´ duality (PD) if there exists a non-degenerate symmetric graded bilinear form

 −,−  : H × H −→ R, where graded means that Hi,Hj = 0 if i = −j. It follows that  −,−  induces an isomorphism between H−i and Hi ∗ and bi = b−i for all i ∈ Z. That is, if

- H satisﬁes Poincar´e duality, the sequence of the Betti numbers will be symmetric, and we regard this as a numerical shadow of the duality.


If H satisﬁes Poincar´e duality, then we ﬁx a such bilinear form  −,− . In this case, we say a degree two linear map

L : Hi −→ Hi+2

is a Lefschetz operator if La,b = a,Lb for all a,b ∈ H. If L is a Lefschetz operator, then it is said to satisfy hard Lefschetz (HL) if for all i ≥ 0,

Li : H−i −→ Hi

is an isomorphism. The following lemma is standard (see for example, Theorem 4 in Section 5, Chapter IV of [33]).

Lemma 3. A degree two operator L on H satisﬁes hard Lefschetz if and only if there is an action of sl2(R) = e,f,h on H with e acting as L, and h·v = iv for all v ∈ Hi. Moreover, this sl2(R)-action is unique.

In particular, if L satisﬁes hard Lefschetz, the Betti numbers of H will satisfy

··· ≤ b−4 ≤ b−2 ≤ b0 ≥ b2 ≥ b4 ≥ ··· and

··· ≤ b−3 ≤ b−1 = b1 ≥ b3 ≥ ··· . Thus we regard the unimodality (with symmetry) as a numerical shadow of the hard Lefschetz property (assuming parity vanishing: Hodd = 0 or Heven = 0).

Let L be a Lefschetz operator. For each i ≥ 0, deﬁne the Lefschetz form on H−i with respect to L as

(a,b)−Li = a,Li b for a,b ∈ H−i, which is non-degenerate if and only if L satisﬁes hard Lefschetz because  −,−  is non-degenerate by assumption.

Suppose that L is a Lefschetz operator satisfying hard Lefschetz. For all i ≥ 0 set

PL−i = ker Li+1 ∩ H−i, elements of this subspace are called primitive vectors of degree −i, and this subspace is called a primitive subspace, which is indeed the lowest weight space in H−i (where we view H as an sl2(R)-representation via Lemma 3.)

If L is a Lefschetz operator satisfying hard Lefschetz, then we have the primitive decomposition

Lj PL−i , and for i ≥ 0,

H =

i≥0 i≥j≥0

- (2.1) H−i = PL−i ⊕ L PL−i−2 ⊕ L2 PL−i−4 ⊕ ··· . In virtue of Lemma 3, it is the isotypic decomposition of the sl2(R)-representation,


where i≥j≥0 Lj PL−i is the sum of copies of the irreducible sl2(R)-representations with highest weight i. For any Lefschetz operator L, we have

(2.2) (La,Lb)L−(i−2) = (a,b)−Li

for all i ≥ 2 and a,b ∈ H−i. It follows that if L satisﬁes hard Lefschetz, then the primitive decomposition is orthogonal with respect to the Lefschetz forms. Consequently, if L satisﬁes hard Lefschetz, then the Lefschetz form is determined by its restriction to the primitive subspaces.

Assume Hodd = 0 or Heven = 0 and that L is a Lefschetz operator satisfying hard Lefschetz. We say that (H, −,− ,L) satisﬁes Hodge–Riemann bilinear relations (HR) if the restriction of the Lefschetz form to the primitive subspace

(−,−)Lm+2i Pm+2i

L

is (−1)i-deﬁnite, where m denotes the most negative integer such that Hm = 0. If (H, −,− ,L) satisﬁes Hodge–Riemann bilinear relations, then in particular, each Lefschetz form is non-degenerate and L satisﬁes hard Lefschetz. By (2.1) and (2.2), Hodge–Riemann bilinear relations predict that the mixed signature of the Lefschetz forms is coming from some deﬁniteness on each primitive subspace and can be expressed in terms of the Betti numbers of H.

We note that in the work [1,5,20] mentioned in paragraph 2 of the introduction, the log-concave property is regarded as a numerical shadow of Hodge–Riemann bilinear relations by interpreting the “Betti numbers” in their context (for example, the Betti numbers of the Orlik-Solomon algebra) as some “intersection numbers”. But we think that “Betti numbers=intersection numbers” is a miracle, and one purpose of this paper is to provide a diﬀerent perspective on the (equivariant) log-concave property.

The main example of graded vector spaces that satisﬁes this package of properties is the cohomology ring of smooth complex projective algebraic varieties whose Hodge numbers hp,q are zero unless p = q1, with the operator L given by multiplication by an ample class. (For example, any smooth projective variety whose cohomology ring is generated by algebraic cycles will have this property.) We note that most of the K¨hler packages discovered so far have some sort of “geometric origin”. In many algebraic settings, it is often diﬃcult to ﬁnd the “lowering operator” in Lemma 3 to prove hard Lefschetz. Instead, one usually ﬁnds some notion of “positivity” or “convexity” so that the Lefschetz operator can be deformed in a family (the “Ka¨hler cone” or “ample cone”), and prove the whole package by induction.

3. Equivariant log-concavity

When considering the equivariant log-concavity of group representations, it is natural to ask for which group G and its representation V , the sequences of symmetric powers Symi(V ) and exterior powers ∧i(V ) are equivariantly log-concave? Surprisingly, the answer is for any group and any representation! Indeed, we have

Proposition 4. For any ﬁnite-dimensional complex representation V of any group G, the sequences of symmetric powers Symi(V ) and exterior powers ∧i(V ) of V are equivariantly log-concave.

Proof. Suppose dim(V ) = n, it suﬃces to show that the proposition holds for G = GLn(C) and V = Cn, the natural representation of G = GLn(C), which follows from the classical Pieri’s formula, see [13, Proposition 15.25, Exercise 15.32 and Exercise 15.33].

In fact, much more is true.

Theorem 5. Let Λ+ denote the set of the dominant weights of GLn(C), and pick any sequence {λi} in Λ+ equi-distributed on a line, then the sequence of representations {L(λi)} is equivariantly log-concave, where L(λi) is the ﬁnite-dimensional irreducible module with highest weight λi.

![image 3](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile3.png>)

1The Hodge–Riemann bilinear relations in K¨hler geometry for more general varieties without the assumption on the Hodge numbers are more complicated than the formulation which we use, see Section 7 of Chapter 0 of [15].

- Theorem 5 is a direct corollary of the following remarkable Schur log-concavity

theorem in [26], which is a special case of Okounkov’s log-concavity conjecture for the Littlewood–Richardson coeﬃcients, see [32], since the Littlewood–Richardson coeﬃcients are the structure coeﬃcients of tensor products of ﬁnite-dimensional representations of general linear groups.

- Theorem 6. [26, Theorem 12, weak version] For two partitions λ = (λ1,λ2,...,λn) and µ = (µ1,µ2,...,µn), suppose λ + µ has only even parts, and let sλ be the


corresponding Schur polynomial, then s2λ+µ

− sλsµ are Schur non-negative, which means that it is a non-negative linear combination of Schur polynomials.

![image 4](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile4.png>)

2

Theorem 5 follows from Theorem 6 since Schur polynomials are the characters of the corresponding highest weight irreducible representations of GLn(C)2. The proof of Theorem 6 relies on a deep result in [17], which in turn relies on the Kazhdan–Lusztig conjecture for the character of simple highest weight modules of sln(C). This is to our surprise since Theorem 5 concerns only ﬁnite-dimensional representations. We note that giving a representation-theoretic proof and not using tools in symmetric function theory might generalize Theorem 5 to other types.

However, giving explicit maps to realize the log-concavity in Theorem 5 might be diﬃcult. Even in the simplest example of g = sl2(C), by the classical Clebsch– Gordan formula, we have the explicit decomposition:

V (k)⊗V (l) ∼= V (k+l)⊕V (k+l−2)⊕···⊕V (k−l) ∼= (V (k+1)⊗V (l−1))⊕V (k−l) for k ≥ l, where V (k) is the irreducible (k + 1)-dimensional representation. But it would be not so easy to give the explicit injections since one has to match the highest weight vectors in the tensor products. Since the exterior powers and the symmetric powers are the two fundamental constructions of representations known as Schur functors on the category of vector spaces, a natural but basic question is: can we give explicit maps to realize the log-concavity in Proposition 4 for Sn?

4. Equivariant Kahler¨ packages

- 4.1. Polynomial rings. Consider the polynomial ring R[t1,...,tn] as a graded (we set each tj of degree 1 for convenience) representation of Sn, where Sn acts by permuting the indices. Geometrically, it is the cohomology H∗((CP∞)n ,R) of the classifying space B(S1)n = (CP∞)n (when doubling the degrees) by the K¨unneth formula and H∗ (CP∞,R) = R[t]. Sn acts on (CP∞)n by permuting the factors hence acts on the cohomology. The Betti number b2i of (CP∞)n is equal


to the binomial coeﬃcient n+ii−1 , which forms a log-concave sequence for ﬁxed n. We will construct an equivariant K¨hler package in this subsection to show that

H∗((CP∞)n ,R) is equivariantly log-concave for the Sn-action. Actually, it turns out that H∗((CP∞)n ,R) is strongly equivariantly log-concave introduced in [27].

Fix a pair of natural numbers (n,m), consider the graded R-vector space

Hn,m =

m

Hn,m−m+2i , with Hn,m−m+2i := Di ⊗ Rm−i,

i=0

![image 5](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile5.png>)

2Another log-concave property of Schur polynomials is that coeﬃcients of monomials, which are the weight multiplicities of the Schur module, are log-concave in the root directions, see [22].

where Di denotes the degree-i piece of the polynomial ring D = R[d1,...,dn], Rm−i denotes the degree-(m − i) piece of the polynomial ring R = R[x1,...,xn], Sn acts on D and R by permuting the indices hence acts on Hn,m.

We deﬁne a pairing on Hn,m by setting

- (4.1) d ⊗ f,d′ ⊗ f′ := (d,f′)(d′,f) and extending linearly, where (d,f′) = (d · f′)(0) is the number one gets by interpreting the di’s as diﬀerential operators ∂x∂

![image 6](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile6.png>)

i

acting on f′ and evaluate xi’s at 0 in the result. Intuitively, one should think that this pairs “homology” with “cohomology”.

We deﬁne

L : Hn,mi −→ Hn,mi+2 to be the linear map

L :=

n

i=1

di ⊗

∂ ∂xi

![image 7](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile7.png>)

,

where di acts by multiplication.

One of our main results is that (Hn,m, −,− ,L) satisﬁes the K¨ahler package. Theorem 7. For any pair of natural numbers (n,m), we have

- (a) (PD) The bilinear pairing  −,−  : Hn,m × Hn,m −→ R

is an Sn-equivariant symmetric graded bilinear form, which is non-degenerate;

- (b) (HL) L : Hn,mi −→ Hn,mi+2 is an Sn-equivariant Lefschetz operator satisfying the hard Lefschetz theorem, i.e., for all i ≥ 0,

Li : Hn,m−i −→ Hn,mi is an isomorphism;

- (c) (HR) For all 0 ≤ i ≤ m/2, the bilinear form (a,b)−Lm+2i = a,Lm−2ib : Hn,m−m+2i × Hn,m−m+2i −→ R


is Sn-equivariant and (−1)i-deﬁnite on the primitive subspace PL−m+2i = ker Lm−2i+1 ∩ H−m+2i.

Proof. It is clear that  −,−  is a symmetric bilinear form. It is graded (i.e.,

Hn,mi ,Hn,mj = 0 if i = −j) for degree reasons. It is Sn-equivariant since (d,f′) = (d · f′)(0) is Sn-equivariant. Finally, it is non-degenerate since

dα ⊗ x

β

![image 8](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile8.png>)

β! | |α| = i,|β| = m − i and dβ

′

⊗ x

α′

![image 9](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile9.png>)

α′! | |β′| = m − i,|α′| = i form a dual3

basis in Hn,m−m+2i and Hn,mm−2i, where dα (similarly for xβ) denotes the monomial dα

1

1 ···dα

nn for α = (α1,··· ,αn), |α| := ni=1 αi and β! := β1!···βn! for β = (β1,··· ,βn). That is,

- (4.2) dα ⊗


′

1, if α = α′, and β = β′, 0, otherwise,

xβ β!

xα

′

,dβ

⊗

=

![image 10](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile10.png>)

![image 11](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile11.png>)

α′!

which completes the proof of part (a).

![image 12](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile12.png>)

3Recall the homology H∗(CP∞, Z) of the classifying space BS1 = CP∞ is the divided polynomial algebras, see [19].

Now we turn to the proof of part (b). We have

L(d ⊗ f),d′ ⊗ f′

n

∂ ∂xi

· f,d′ ⊗ f′

did ⊗

=

![image 13](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile13.png>)

i=1

n

∂ ∂xi

(did,f′) d′,

=

· f

![image 14](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile14.png>)

i=1

n

∂ ∂xi

· f′ (did′,f)

d,

=

![image 15](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile15.png>)

i=1

n

∂ ∂xi

did′ ⊗

· f′

= d ⊗ f,

![image 16](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile16.png>)

i=1

= d ⊗ f,L (d′ ⊗ f′) ,

which shows that L is a Lefschetz operator. It is clear that L is Sn-equivariant. To show that L satisﬁes hard Lefschetz, we deﬁne the lowering operator

F : Hn,mi −→ Hn,mi−2 as

n

∂ ∂di

⊗ xi.

F :=

![image 17](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile17.png>)

i=1

By direct computation,

LF− FL

 

n

n

∂ ∂xi

∂ ∂dj

di ⊗

=

![image 18](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile18.png>)

![image 19](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile19.png>)

i=1

j=1

n

n

∂ ∂dj

∂ ∂xi

(di

⊗

xj −

=

![image 20](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile20.png>)

![image 21](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile21.png>)

i=1

j=1

n

∂ ∂xi

∂ ∂di

⊗ id− id⊗xi

(di

=

![image 22](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile22.png>)

![image 23](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile23.png>)

i=1

⊗ xj

 − 

n



j=1

∂ ∂xi

∂ ∂dj

di ⊗ xj

)

![image 24](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile24.png>)

![image 25](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile25.png>)

),

⊗ xj

∂ ∂dj

![image 26](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile26.png>)



n

∂ ∂xi

di ⊗

![image 27](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile27.png>)

i=1

the last equality follows from the Leibniz rule. We deﬁne h : Hn,mi −→ Hn,mi to be the linear map

n

h :=

i=1

∂ ∂di

∂ ∂xi

di

⊗ id− id⊗xi

![image 28](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile28.png>)

![image 29](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile29.png>)

.

Since ni=1 di∂d∂

and ni=1 xi ∂x∂

are Euler operators which act on homogeneous

![image 30](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile30.png>)

![image 31](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile31.png>)

i

i

degree-k polynomials with eigenvalue k, thus h·v = iv for all v ∈ Hn,mi as required in Lemma 3. Finally, we check the sl2-relations: by deﬁnition, LF− FL = h. We

compute hL− Lh

n

∂ ∂di

di

=

![image 32](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile32.png>)

i=1

n

n

di

=

i=1

j=1

n

∂ ∂di

(di

=

![image 33](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile33.png>)

i=1

n

2di ⊗

=

i=1

∂ ∂xi

⊗ id− id⊗xi

![image 34](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile34.png>)

n

dj ⊗

j=1

∂ ∂xi

∂ ∂xj

∂ ∂di

dj ⊗

− dj ⊗ xi

![image 35](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile35.png>)

![image 36](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile36.png>)

![image 37](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile37.png>)

∂ ∂xj

![image 38](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile38.png>)

n

∂ ∂xj

dj ⊗

−

j=1

∂ ∂di

∂ ∂xj

− djdi

⊗

![image 39](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile39.png>)

![image 40](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile40.png>)

∂ ∂di

di − didi

) ⊗

![image 41](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile41.png>)

∂ ∂xi

= 2 L,

![image 42](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile42.png>)

∂ ∂xi

∂ ∂xi

∂ ∂xi

− di ⊗ (xi

−

![image 43](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile43.png>)

![image 44](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile44.png>)

![image 45](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile45.png>)

∂ ∂xi

![image 46](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile46.png>)

n

![image 47](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile47.png>)

i=1

∂ ∂di

∂ ∂xi

di

⊗ id− id⊗xi

![image 48](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile48.png>)

![image 49](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile49.png>)

∂ ∂xj

∂ ∂xj

+ dj ⊗

xi

![image 50](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile50.png>)

![image 51](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile51.png>)

∂ ∂xi

![image 52](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile52.png>)

∂ ∂xi

xi

)

![image 53](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile53.png>)

and similar computations show that hF− Fh = −2 F. By Lemma 3, L satisﬁes hard Lefschetz, which completes the proof of part (b).

We are now turning to the proof of part (c). The Lefschetz form (a,b)−Lm+2i = a,Lm−2i b on Hn,m−m+2i is Sn-equivariant since  −,−  and L are both Sn-equivariant. It remains to prove Hodge–Riemann bilinear relations, here we use a little classical Hodge theory and we refer to Section 7 of Chapter 0 of [15] for the reader. Let V (k) be the irreducible (k+1)-dimensional representation of the Lie algebra sl2(R) with highest weight k. The direct sum n sl2(R) of n copies of sl2(R) = ei,fi,hi act on

m

m

Di ⊗ Rm−i

Hn,m−m+2i =

Hn,m =

i=0

i=0

via

∂ ∂xi

ei = di ⊗

,fi =

![image 54](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile54.png>)

∂ ∂di

∂ ∂di

⊗ xi , and hi = di

![image 55](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile55.png>)

![image 56](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile56.png>)

∂ ∂xi

⊗ id− id⊗xi

.

![image 57](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile57.png>)

Then our action of sl2(R) comes from the diagonal embedding

sl2(R) −→∆ ⊕nsl2(R), where

n

n

n

hi.

fi , and ∆(h) =

ei,∆(F) =

∆(L) =

i=1

i=1

i=1

As a representation of n sl2(R), or equivalently, as a representation of the enveloping algebra U( n sl2(R)) ∼= n U (sl2(R)), we have

Hn,m ∼=

V (α1) ⊗ ··· ⊗ V (αn),

α=(α1,··· ,αn),|α|=m

where each V (αi) is an irreducible representation of the i-th copy of sl2(R) in n sl2(R) and the other copies of sl2(R) in n sl2(R) act trivially. Therefore, as a representation of sl2(R) = L,F,h , we have the decomposition into irreducible

representations

- (4.3)

Hn,m ∼=

α=(α1,··· ,αn),|α|=m

V (α1) ⊗ ··· ⊗ V (αn)

∼=

α=(α1,··· ,αn),|α|=m

H∗ (CPα1

,R) ⊗ ··· ⊗ H∗ (CPαn

,R)

∼=

α=(α1,··· ,αn),|α|=m

H∗ (CPα1

× ··· × CPαn

,R),

where the third isomorphism is by the K¨unneth formula, the second is via the action fi tji = (αi − j + 1)tij−1,hi tji = (2j − αi)tji , and ei tji = (j + 1)tji+1 on the cohomology of projective space H∗ (CPαi

,R) = R[ti]/ tα

i+1

i . We ﬁx an isomophism such that the highest weight vector dα ⊗1 ∈ Hn,m of n sl2(R) corresponds to tα ∈ H∗ (CPα1

× ··· × CPαn

,R). By the actions of fi′ s, the lowest weight vector 1 ⊗ xα ∈ Hn,m corresponds to 1 ∈ H∗ (CPα1

× ··· × CPαn

,R). Therefore, the bilinear form  −,−  on Hn,m restricts to each H∗ (CPα1

× ··· × CPαn

,R) as the usual Poincar´e pairing up to a positive scalar by (4.2). Under this isomophism, each ei corresponds to multiplying an ample class on H∗ (CPα

i

,R). Therefore, L also corresponds to multiplying an ample class on H∗ (CPα1

× ··· × CPαn

,R). By classical Hodge theory, Hodge–Riemann bilinear relations hold for each H∗ (CPα

1

× ··· × CPα

n

,R).

This give Hodge–Riemann bilinear relations for Hn,m since it is not hard to see that the decomposition (4.3) is orthogonal with respect to the Lefschetz form in Hn,m by (4.2) again, which completes the proof of part (b). The proof is completed.

The hard Lefschetz property immediately gives the following corollary.

Corollary 8. H∗((CP∞)n ,R) = R[t1,...,tn] is strongly equivariantly log-concave for any m ≥ 0:

- (4.4)


V 0⊗V m ⊂ V 1⊗V m−1 ⊂ V 2⊗V m−2 ⊂ ··· ⊂

V m/2 ⊗ V m/2 if m is even V (m−1)/2 ⊗ V (m+1)/2 if m is odd,

where V i denotes the degree-2i piece of H∗((CP∞)n ,R) = R[t1,...,tn] (here each ti is of degree-2). Furthermore, the inclusions of Sn-representations are given by the operator

n

∂ ∂ti

ti ⊗

L =

,

![image 58](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile58.png>)

i=1

where ti acts by multiplication.

- Remark 9. Actually, the Lefschetz operator L is indeed GLn(R)-equivariant, see for example, [37]. In particular, L is equivariant for the symmetric powers of any representation of any group G. But the whole packages, in particular, the bilinear

form  −,−  and the Lefschetz form (a,b)−Lm+2i are only Sn-equivariant, or more generally, for which group G acts on R[t1,...,tn] = Symi(V ) with V ∼= V ∗. A similar remark holds for the following exterior algebra case.

- Remark 10. Each primitive subspace measures the diﬀerence of the adjacent tensor


products of representations in (4.4). The Lefschetz forms (a,b)−Lm+2i are equivariant and Hodge–Riemann bilinear relations tell us these equivariant Lefschetz

forms are positive deﬁnite or negative deﬁnite on these diﬀerences of adjacent tensor products of representations, depending only on the graded degree. A similar remark holds for the following exterior algebra case.

- 4.2. Exterior algebras. Consider the exterior algebra ΛR [α1,...,αn] as a graded (each αj is of degree 1) representation of Sn, where Sn acts by permuting the indices hence acts on exterior powers. Geometrically, it is the cohomology H∗ (S1)n,R of


the torus T = (S1)n by the K¨unneth formula and H∗ S1,R = R[α]/(α2). Sn acts on the torus T = (S1)n by permuting the factors hence acts on the cohomology. The Betti number bi of the torus T = (S1)n is equal to the binomial coeﬃcient

n i , which forms a classical log-concave sequence for ﬁxed n. This time, we will

construct an equivariant K¨hler package to show that H∗( S1 n ,R) is strongly equivariantly log-concave for the Sn action.

Fix a pair of natural numbers (n,m) with m ≤ 2n, consider the graded R-vector space

m

(Hn,m′ )−m+2i , with (Hn,m′ )−m+2i := Λi ⊗ (Λ∗)m−i,

Hn,m′ =

i=0

- where Λi denotes the degree- i piece of the exterior algebra Λ = Λ(V ) = ΛR [θ1,...,θn], (Λ∗)m−i denotes the degree- (m − i) piece of the exterior algebra Λ∗ = Λ(V ∗) = ΛR [ξ1,...,ξn], note that Λi = 0 (resp., (Λ∗)m−i = 0) except 0 ≤ i ≤ n (resp., 0 ≤ m−i ≤ n. We demand that θ1,...,θn and ξ1,...,ξn form dual basis for V and V ∗. Sn acts on Λ and Λ∗ as the exterior powers of the corresponding permutation representations hence acts on Hn,m′ .


We deﬁne a pairing 4 on Hn,m′ by setting

- (4.5) u ⊗ v∗,u′ ⊗ (v∗)′ := (−1)ε u,(v∗)′ (u′,v∗)

and extending linearly, where (−,−) is the bilinear map of Λi × (Λ∗)j → R which on indecomposable elements u = u1 ∧ ··· ∧ ui in Λi and v∗ = v1∗ ∧ ··· ∧ vj∗ in (Λ∗)j yields

- (4.6) (u,v∗) =

det(vk∗ (ul)), if i = j, 0, if i = j.

and

- (4.7) ε =


m(m − 1)/2, if 0 ≤ m ≤ n, (2n − m)(2n − m − 1)/2, if n < m ≤ 2n.

Here the global sign correction (−1)ε is to make Hodge–Riemann bilinear relations satisﬁed with the standard sign, that is, the later-deﬁned Lefschetz form is positive deﬁnite on the lowest non-zero degree of Hn,m′ (which is necessarily primitive because the later-deﬁned operator satisﬁes the hard Lefschetz theorem).

Recall that for each α ∈ V ∗ (or v ∈ V , respectively), it is possible to deﬁne an anti-derivation iα called the interior product with α on the algebra Λ(V ) (or Λ(V ∗), resp., we only consider the ﬁrst case in the remaining of this paragraph):

iα : ΛkV → Λk−1V,

![image 59](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile59.png>)

4Again, one should think intuitively that this pairs “homology” with “cohomology”!

which satisﬁes (iαw) v1∗,v2∗,...,vk∗−1 = w α,v1∗,v2∗,...,vk∗−1 for w ∈ ΛkV and v1∗,v2∗,...,vk∗−1 are k − 1 elements of V ∗. It follows that if v is an element of V = Λ1V , then iαv = α(v) is the dual pairing between elements of V and elements of V ∗. Furthermore, iα is a graded derivation of degree −1:

iα(u ∧ v) = (iαu) ∧ v + (−1)deguu ∧ (iαv). Additionally, let iαf = 0 whenever f is a pure scalar (i.e., belonging to Λ0V ).

For each v ∈ V (similarly for α ∈ V ∗), let ev denote the exterior (wedge) product with v on the left:

ev : Λk−1V → ΛkV.

The following lemma is standard and we omit the proof. Lemma 11. For any u,v ∈ V and α,β ∈ V ∗, we have

- (a) iα ◦ iβ = −iβ ◦ iα, in particular, iα ◦ iα = 0;
- (b) ev ◦ eu = −eu ◦ ev, in particular, ev ◦ ev = 0;
- (c) iα ◦ ev + ev ◦ iα = α(v) · id, iv ◦ eα + eα ◦ iv = α(v) · id;
- (d) (Adjoint) The bilinear pairing (−,−) satisﬁes (iα(u),β) = (u,eαβ) = (u,α ∧ β).


We deﬁne

L : (Hn,m′ )i −→ (Hn,m′ )i+2 to be the linear map

n

L :=

eθ

⊗ iθ

.

k

k

k=1

Our second main result is that (Hn,m′ , −,− ,L) also satisﬁes the K¨ahler package. Theorem 12. For any pair of natural numbers (n,m) with m ≤ 2n, we have

- (a) (PD) The bilinear pairing  −,−  : Hn,m′ × Hn,m′ −→ R

is an Sn-equivariant symmetric graded bilinear form, which is non-degenerate;

- (b) (HL) L : (Hn,m′ )i −→ (Hn,m′ )i+2 is an Sn-equivariant Lefschetz operator satisfying the hard Lefschetz theorem, i.e., for all i ≥ 0,

Li : (Hn,m′ )−i −→ (Hn,m′ )i is an isomorphism;

- (c) (HR) For 0 ≤ i ≤ m/2, the bilinear form (a,b)−Lm+2i = a,Lm−2ib : (Hn,m′ )−m+2i × (Hn,m′ )−m+2i −→ R


is Sn-equivariant and (−1)i-deﬁnite on the primitive subspace (PL′ )−m+2i = ker Lm−2i+1 ∩ (Hn,m′ )−m+2i.

Proof. The proof is very similar to that of Theorem 7. It is clear that  −,−  is a symmetric bilinear form. It is graded by the deﬁnition of (−,−) and it is Sn-equivariant since (−,−) is Sn-equivariant. Finally, it is non-degenerate since

′

′

| |β′| = m − i,|α′| = i form a dual basis in (Hn,m′ )−m+2i and (Hn,m′ )m−2i, where θ∧α (similarly for ξ∧β) denotes

θ∧α ⊗ ξ∧β | |α| = i,|β| = m − i and θ∧β

⊗ ξ∧α

the exterior power θα

1 ∧ ··· ∧ θα

nn for α = (α1,··· ,αn) where αj = 0 or 1, |α| :=

1

n i=1 αi. That is,

′

θ∧α ⊗ ξ∧β,θ∧β

′ 1, if α = α′, and β = β′, 0, otherwise

⊗ y∧α

,

which completes the proof of part (a).

Let us turn to the proof of part (b). The adjoint property (d) of Lemma 11 shows that L is a Lefschetz operator. It is clear that L is Sn-equivariant. To show that L satisﬁes hard Lefschetz, we deﬁne the lowering operator F : Hn,mi −→ Hn,mi−2 as

n

. A direct computation based on Lemma 11 shows that LF − FL =

F :=

iξ

⊗ eξ

k

k

k=1

n

(eθ

◦ iξ

⊗ id− id⊗eξ

◦ iθ

).

k

k

k

k

k=1

If we deﬁne h : (Hn,m′ )i −→ (Hn,m′ )i to be the linear map h :=

n

(eθ

◦ iξ

⊗ id− id⊗eξ

◦ iθ

),

k

k

k

k

k=1

then it is not hard to see that ( nk=1 eθ

)(θ∧α) = |α|θ∧α and similarly for

◦ iξ

k

k

n k=1 (eξ

), thus h · v = iv for all v ∈ (Hn,m′ )i as required.

◦ iθ

k

k

Finally, one can check the sl2-relations for L,F,h using Lemma 11. By Lemma 3, L satisﬁes hard Lefschetz.

The proof of part (c), especially the proof of Hodge–Riemann bilinear relations, is quite similar to that of part (c) in Theorem 7 given earlier except that the action of the triple sl2(R) = ek,fk,hk should be replaced with

ek = eθ

k

⊗ iθ

,fk = iξ

k

k

⊗ eξ

, and hk = eθ

k

k

◦ iξ

k

⊗ id− id⊗eξ

k

◦ iθ

,

k

and each irreducible representation V (αi) is at most 2-dimensional. It is easy to check that the global sign correction ε in (4.7) makes the bilinear form  −,−  on

Hn,m′ restricts to the usual Poincar´e pairing on each cohomology of product of projective space up to a positive scalar in a decomposition similar to (4.3), we leave the details to the reader. The proof is completed.

We have the following corollary of the hard Lefschetz theorem.

Corollary 13. H∗((S1)n,R) = ΛR [α1,...,αn] is strongly equivariantly log-concave for any 0 ≤ m ≤ 2n:

V 0⊗V m ⊂ V 1⊗V m−1 ⊂ V 2⊗V m−2 ⊂ ··· ⊂

V m/2 ⊗ V m/2 if m is even V (m−1)/2 ⊗ V (m+1)/2 if m is odd,

where V i denotes the degree-i piece of H∗((S1)n,R) = ΛR [α1,...,αn], which vanishes except 0 ≤ i ≤ n. Furthermore, the inclusions of Sn-representations are given by the operator

n

L =

eα

⊗ iα∗

.

k

k

k=1

are the exterior product and interior product, respectively, and α∗k is the linear functional on V = α1,...,αn satisfying α∗k (αl) = δkl =

where eα

and iα∗

k

k

- 0, if k = l,
- 1, if k = l.


- Remark 14. In [14, Proposition 5.7], the authors gave an alternative proof of the equivariant log-concavity for the exterior powers using formulas for the Kronecker products of Schur functions of hook shapes without giving the inclusion maps.
- Remark 15. For our application to equivariant log-concavity, it is only necessary to establish the equivariant hard Lefschetz property, here we quote the following in [4]


“The one insight that we can take away is that, while the hard Lefschetz theorem is typically the main statement needed for applications, it is always necessary to prove Poincar´e duality, the hard Lefschetz theorem, and the Hodge–Riemann relations together as a single package.”

- 4.3. An interesting example. For the exterior algebra, we now show that “usual” gradings on tensor products satisfy Poincar´e duality and hard Lefschetz but not Hodge–Riemann bilinear relations.


Fix any natural numbers n, consider the graded R-vector space

Hn =

2n

Hn−n+i , with Hn−n+i :=

Λj ⊗ (Λ∗)k,

i=0

j+k=i

- where Λj denotes the degree- j piece of the exterior algebra Λ = Λ(V ) = ΛR [θ1,...,θn], (Λ∗)k denotes the degree- k piece of the exterior algebra Λ∗ = Λ(V ∗) = ΛR [ξ1,...,ξn], i.e., we consider the “usual” gradings on the tensor product Λ ⊗ Λ∗ up to a degree shift of −n. Again, we demand that θ1,...,θn and ξ1,...,ξn form dual basis of V and V ∗. Sn acts on Λ and Λ∗ as the exterior powers of the corresponding permutation representations hence acts on Hn.


We deﬁne a graded pairing  −,−  on Hn by the multiplication map

- (4.8) Hn−n+i ⊗ Hnn−i → Hnn ∼= R,


where the linear isomorphism maps θ1∧...∧θn⊗ξ1∧...∧ξn to 1. Note the unusual grading convention here, since the identity element 1 ⊗ 1 lives in degree −n.

We deﬁne

L : Hni −→ Hni+2 to be the linear map

n

eθ

⊗ eξ

.

L :=

k

k

k=1

We have the following theorem. Theorem 16. For any natural numbers n, we have

- (a) (PD)  −,−  : Hn × Hn −→ R


is an Sn-equivariant graded bilinear form, which is non-degenerate;

- (b) (HL) L : Hni −→ Hni+2 is Sn-equivariant and satisﬁes the hard Lefschetz theorem, i.e., for all i ≥ 0,


Li : Hn−i −→ Hni is an isomorphism.

Proof. By deﬁnition,  −,−  is a graded bilinear form. It is Sn-equivariant and non-degenerate since the multiplication map

- (4.9) Λj ⊗ (Λ∗)k Λn−j ⊗ (Λ∗)n−k → Hnn ∼= R


is an Sn-equivariant perfect pairing for any 0 ≤ j,k ≤ n, which proves part (a).

Let us turn to the proof of part (b). It is clear that L is Sn-equivariant. To show that L satisﬁes hard Lefschetz, we deﬁne the lowering operator F : Hni −→ Hni−2 as

n

iξ

⊗ iθ

.

F :=

k

k

k=1

A direct computation based on Lemma 11 shows that

n

LF− FL =

(eθ

◦ iξ

⊗ id+ id⊗ eξ

◦ iθ

) − n id⊗ id.

k

k

k

k

k=1

If we deﬁne h : Hni −→ Hni to be the linear map h :=

n

(eθ

◦ iξ

⊗ id+ id⊗ eξ

◦ iθ

) − n id⊗ id,

k

k

k

k

k=1

then it is not hard to see that h·v = iv for all v ∈ Hni as required. By checking the sl2-relations for L,F,h using Lemma 11, L satisﬁes hard Lefschetz by Lemma 3. The proof is completed.

- Remark 17. The main diﬀerence between Hn and Hn,m (or Hn,m′ ) is that Hn does not satisfy the parity vanishing. Note that commuting the multiplication order of the factors in (4.9) yields a sign of (−1)j(n−j)+k(n−k), thus when n is even, the bilinear form  −,−  is skew-symmetric on the odd part. By part (b) of Lemma 11, L is a Lefschetz (i.e., self-adjoint) operator with respect to the symmetric bilinear form  −,−  except n is even and j + k = i is odd, and is skew-self-adjoint with respect to the skew-symmetric bilinear form  −,−  if it is the case. So in any case, the Lefschetz form is a symmetric bilinear form. However, the Hodge–Riemann bilinear relations are NOT satisﬁed. For example, when n = 2, it is easy to compute the signature of the Lefschetz form is (2,2) on degree −1 and is (3,3) on degree 0, neither of which matches the prediction of Hodge–Riemann bilinear relations.
- Remark 18. There is also an Sn-equivariant sl2-action on the “usual” gradings of the tensor product of the polynomial ring D = R[d1,...,dn] and R = R[x1,...,xn]:


∞

(Hn′ )i , with (Hn′ )i :=

Dj ⊗ Rk,

Hn′ =

i=0

j+k=i

via e = −

n

n

n

∂ ∂xl

∂ ∂dl

⊗

,f =

dl⊗xl , and hi = −n id⊗ id−

(dl

![image 60](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile60.png>)

![image 61](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile61.png>)

l=1

l=1

l=1

∂ ∂dl

∂ ∂xl

⊗id+ id⊗xl

).

![image 62](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile62.png>)

![image 63](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile63.png>)

But neither Poincar´e duality nor hard Lefschetz holds and the representation Hn′ is inﬁnite-dimensional.

5. Questions and Future work

We would like to ﬁnish with some questions and conjectures. Since our constructions of these K¨hler packages are purely algebraic, it is natural to ask the following question ﬁrst.

- Question 19. Are there any geometric interpretations of these constructions?

In [24], the authors use the equivariant hard Lefschetz in Theorem 16 (which is their Theorem 3.2) as a key tool to study the fermionic diagonal coinvariants. We would like to ask the following

- Question 20. Do the other two equivariant K¨ahler packages (Theorem 7 and Theorem 12), especially the Hodge–Riemann relations, have some implications for the diagonal coinvariant ring and the fermionic diagonal coinvariant ring?


In [30], the authors transformed the log-concavity conjecture of the distribution of permutations in Sn with ﬁxed length of longest increasing subsequences in [8] into the following equivariant log-concavity conjecture of Sn

- Conjecture 21. [30, Conjecture 2] Let λ be a partition of n and V λ be the irreducible representation of Sn corresponding to λ, then the graded representation Vn = nk=0 Vnk of Sn is equivariantly log-concave, where

Vnk =

λ⊢n ℓ(λ)=k

fλV λ,

here fλ is the dimension of V λ, also equal to the number of standard Young tableaux of shape λ, which is given by the hook-length formula.

Based on the representation stability theory and some numerical evidence, the ﬁrst author has the following conjecture in [16]

- Conjecture 22. For all integer n ≥ 1, the cohomology ring of the ﬂag manifold Un/T, which is also known as the coinvariant ring of Sn: H2∗(Un/T,R) ∼= R[t1,...,tn]/ (σ1,...,σn), is equivariantly log-concave as graded representation of


Sn, where each t′js is of degree 2 and σi is the i-th elementary symmetric polynomials in the variables t1,...,tn.

It is interesting to see whether similar equivariant Hodge-theoretic structures exist in the settings of the above two equivalent log-concavity conjectures and the settings of equivalent log-concavity conjectures in [27].

Acknowledgment.

The ﬁrst author would like to thank Ming Fang, Peter L. Guo, Hongsheng Hu, Ruizhi Huang, and Nanhua Xi for the useful discussions, and thank Nicholas Proudfoot and Brendon Rhoades for helpful comments, and is grateful to Neil J.Y. Fan for the help with computer calculations. This work was completed when the second author visited the AMSS, CAS. The second author would like to thank Sian Nie for the invitation. The authors would like to thank the anonymous referee for the comments and suggestions. The second author was supported in part by the National Natural Science Foundation of China (No. 11922119).

References

- [1] Karim Adiprasito, June Huh, and Eric Katz, Hodge theory for combinatorial geometries, Annals of Mathematics 188 (2018), no. 2, 381–452.
- [2] Gottfried Barthel, Jean-Paul Brasselet, Karl-Heinz Fieseler, and Ludger Kaup, Combinatorial intersection cohomology for fans, Tohoku Mathematical Journal, Second Series 54 (2002), no. 1, 1–41.
- [3] Tom Braden, Remarks on the combinatorial intersection cohomology of fans, Pure and Applied Mathematics Quarterly 2 (2006), no. 4, 1149–1186.
- [4] Tom Braden, June Huh, Jacob P Matherne, Nicholas Proudfoot, and Botong Wang, Singular Hodge theory for combinatorial geometries, arXiv preprint arXiv:2010.06088 (2020).
- [5] Petter Br¨and´en and June Huh, Lorentzian polynomials, Annals of Mathematics 192 (2020), no. 3, 821–891.
- [6] Francesco Brenti, Log-concave and unimodal sequences in algebra, combinatorics, and geometry: an update, Jerusalem combinatorics’ 93: An international conference in combinatorics, may 9-17, 1993, jerusalem, israel, 1994, pp. 71.
- [7] Paul Bressler and Valery A Lunts, Intersection cohomology on nonrational polytopes [star], Compositio Mathematica 135 (2003), no. 3, 245–278.
- [8] William YC Chen, Log-concavity and q-log-convexity conjectures on the longest increasing subsequences of permutations, arXiv preprint arXiv:0806.3392 (2008).
- [9] Calin Chindris, Harm Derksen, and Jerzy Weyman, Counterexamples to Okounkov’s logconcavity conjecture, Compositio Mathematica 143 (2007), no. 6, 1545–1557.
- [10] Ben Elias, Shotaro Makisumi, Ulrich Thiel, and Geordie Williamson, Introduction to Soergel Bimodules, Vol. 5, Springer Nature, 2020.
- [11] Ben Elias and Geordie Williamson, The Hodge theory of Soergel bimodules, Annals of Mathematics 180 (2014), no. 3, 1089–1136.
- [12] , Relative hard Lefschetz for Soergel bimodules, J. Eur. Math. Soc. (JEMS) 23 (2021), no. 8, 2549–2581 (English).

![image 64](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile64.png>)

- [13] William Fulton and Joe Harris, Representation Theory: a First Course, Vol. 129, Springer Science & Business Media, 2013.
- [14] Katie Gedeon, Nicholas Proudfoot, and Benjamin Young, The equivariant Kazhdan–Lusztig polynomial of a matroid, Journal of Combinatorial Theory, Series A 150 (2017), 267–294.
- [15] Phillip Griﬃths and Joseph Harris, Principles of Algebraic Geometry, John Wiley & Sons, 2014.
- [16] Tao Gui, On the equivariant log-concavity for the cohomology of the ﬂag varieties, arXiv preprint arXiv:2205.05408 (2022).
- [17] Mark Haiman, Hecke algebra characters and immanant conjectures, Journal of the American Mathematical Society 6 (1993), no. 3, 569–595.
- [18] , Conjectures on the quotient ring by diagonal invariants, Journal of Algebraic Combinatorics 3 (1994), no. 1, 17–76.

![image 65](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile65.png>)

- [19] Allen Hatcher, Algebraic Topology, Tsinghua University publishing house co., ltd, 2005.
- [20] June Huh, Milnor numbers of projective hypersurfaces and the chromatic polynomial of graphs, Journal of the American Mathematical Society 25 (2012), no. 3, 907–927.
- [21] , Combinatorial applications of the Hodge–Riemann relations, Proceedings of the international congress of mathematicians: Rio de janeiro 2018, 2018, pp. 3093–3111.

![image 66](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile66.png>)

- [22] June Huh, Jacob Matherne, Karola M´esz´ros, and Avery St Dizier, Logarithmic concavity of Schur and related polynomials, Transactions of the American Mathematical Society 375

(2022), no. 6, 4411–4427.

- [23] Kalle Karu, Hard Lefschetz theorem for nonrational polytopes, Inventiones mathematicae 157

(2004), no. 2, 419–447.

- [24] Jongwon Kim and Brendon Rhoades, Lefschetz theory for exterior algebras and fermionic diagonal coinvariants, International Mathematics Research Notices 2022 (2022), no. 4, 2906– 2933.
- [25] Allen Knutson and Terence Tao, The honeycomb model of GLn(C) tensor products i: Proof of the saturation conjecture, Journal of the American Mathematical Society 12 (1999), no. 4, 1055–1090.
- [26] Thomas Lam, Alexander Postnikov, and Pavlo Pylyavskyy, Schur positivity and Schur logconcavity, American journal of mathematics 129 (2007), no. 6, 1611–1622.


- [27] Jacob P Matherne, Dane Miyata, Nicholas Proudfoot, and Eric Ramos, Equivariant log concavity and representation stability, International Mathematics Research Notices 2023 (2023), no. 5, 3885–3906.
- [28] Peter McMullen, On simple polytopes, Inventiones mathematicae 113 (1993), no. 1, 419–444.
- [29] Hiraku Nakajima, t-analogs of q-characters of Kirillov–Reshetikhin modules of quantum aﬃne algebras, Represent. Theory 7 (2003), no. 2, 3.
- [30] Jonathan Novak and Brendon Rhoades, Increasing subsequences and Kronecker coeﬃcients, arXiv preprint arXiv:2006.13146 (2020).
- [31] Andrei Okounkov, Brunn–Minkowski inequality for multiplicities, Inventiones mathematicae 125 (1996), no. 3, 405–411.
- [32] , Why would multiplicities be log-concave?, The orbit method in geometry and physics, 2003, pp. 329–347.

![image 67](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile67.png>)

- [33] Jean-Pierre Serre, Complex Semisimple Lie Algebras, Springer Science & Business Media, 2000.
- [34] Richard P Stanley, Log-concave and unimodal sequences in algebra, combinatorics, and geometry, Ann. New York Acad. Sci 576 (1989), no. 1, 500–535.
- [35] , Positivity problems and conjectures in algebraic combinatorics, Mathematics: Frontiers and Perspectives: Frontiers and Perspectives (2000), 295.

![image 68](<2022-gui-equivariant-log-concavity-equivariant-hler_images/imageFile68.png>)

- [36] Geordie Williamson, Local Hodge theory of Soergel bimodules, Acta Math. 217 (2016), no. 2, 341–404 (English).
- [37] Nanhua Xi, Module structure on invariant Jacobians, Mathematical Research Letters 19


(2012), no. 3, 731–739.

