---
type: source
kind: paper
title: Asymptotic Log-concavity of Dominant Lower Bruhat Intervals via Brunn--Minkowski Inequality
authors: Gaston Burrull, Tao Gui, Hongsheng Hu
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2311.17980v3
source_local: ../raw/2023-burrull-asymptotic-log-concavity-dominant-lower.pdf
topic: general-knowledge
cites:
---

# arXiv:2311.17980v3[math.CO]2Aug2025

Asymptotic log-concavity of dominant lower Bruhat intervals via Brunn–Minkowski inequality

Gaston Burrull, Tao Gui, and Hongsheng Hu

Abstract. Bjo¨rner and Ekedahl [Ann. of Math. (2), 170.2(2009), pp. 799–817] pioneered the study of length-counting sequences associated with (parabolic) lower Bruhat intervals in crystallographic Coxeter groups. In this paper, we study the asymptotic behavior of these sequences in aﬃne Weyl groups. Let W be an aﬃne Weyl group with corresponding Weyl group Wf and fW be the set of minimal representatives for the right cosets Wf\W. Let tλ be the translation by a dominant coroot lattice element λ and fbtiλ be the number of elements of length i below tλ in the Bruhat order on fW, which is the 2i-dimensional Betti number of a Schubert variety in a certain aﬃne Grassmannian. We show that the sequence (fbtiλ)i is “asymptotically log-concave” in the following sense: The sequence of discrete measures (mk)k constructed from the k-fold dilated sequence (fbtikλ)i, as k tends to inﬁnity, converges weakly to a continuous measure obtained from a polytope Pλ. Moreover, the sequence of step functions (Sk)k of (fbtikλ)i converges uniformly to the density function of this continuous measure. By Brunn–Minkowski inequality, this density is log-concave.

Contents

- 1. Introduction 2

- 1.1. Background 2
- 1.2. Our setting 4
- 1.3. Main results 6
- 1.4. An example 9
- 1.5. Connections with other works 10
- 1.6. Structure of the paper 14 Acknowledgments 14


- 2. Preliminaries 14

- 2.1. The aﬃne Weyl group and alcoves 14
- 2.2. Dominant alcoves and fW 16
- 2.3. Measures on R and E 18
- 2.4. Polytopes 19


- 3. The partial order and the Bruhat–Chevalley order 20
- 4. Dominant elements 22


![image 1](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile1.png>)

2020 Mathematics Subject Classiﬁcation. 05E16 (Primary), 05E14, 52A27, 52A38, 51F15 (Secondary).

1

- 4.1. The polytope Pλ and the dominant lower interval f[e,tλ] 22
- 4.2. The dominant lattice formula 25
- 4.3. Truncations 27


- 5. The weak convergence of (m1,m2,...) 30

- 5.1. Weak convergence of “companion” measures 30
- 5.2. Proof of Theorem 1.3(1) 32


- 6. The uniform convergence of (S1,S2,...) 34

- 6.1. Outline of the proof of Theorem 1.3(2) 34
- 6.2. Volume estimations 35
- 6.3. Proof of Theorem 1.3(2) 39
- 6.4. Proof of Equation (6.12) 43


- 7. General dominant elements 45 References 46


1. Introduction

- 1.1. Background


Schubert varieties are certain subvarieties of ﬂag varieties. They are projective algebraic varieties that are usually singular. Studying classes of Schubert varieties in the cohomology ring of the ﬂag variety leads to important results in enumerative geometry (the classical “Schubert calculus”), while the study of their intersection cohomology plays a fundamental role in the representation theory of Lie-theoretic objects (the “Kazhdan–Lusztig theory”). Following Bjo¨rner and Ekedahl [5], we are interested in the behavior of the Betti numbers of Schubert varieties.

More precisely, consider a complex Kac–Moody group G (a gentle introduction of Kac–Moody groups and their ﬂag varieties can be found in [23]) with Borel subgroup B and maximal torus T. The corresponding Weyl group W has the structure of a crystallographic Coxeter system (W,S), where S is the generating set of simple reﬂections and we denote by ℓ: W → N the length function. For any J ⊂ S, there is a parabolic subgroup WJ := s ∈ J of W with corresponding subgroup PJ := BWJB of G.

The quotient PJ\G is a projective (ind-)variety called the generalized (partial) ﬂag variety. We have Bruhat decomposition

PJ\G =

PJ\PJwB,

w∈JW

where JW is the set of minimal representatives for the right cosets WJ\W. The component Cw := PJ\PJwB is called the Schubert cell associated with w ∈ JW. Topologically, Cw is an ℓ(w)-dimensional aﬃne space Aℓ(w). Its closure Xw := Cw, called the Schubert variety associated with w, is a ﬁnitedimensional projective irreducible subvariety of PJ\G. There is a partial order ≤ on JW called the Bruhat–Chevalley order, deﬁned by v ≤ w if

![image 2](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile2.png>)

Cv ⊆ Xw. Furthermore, we have the decomposition

- (1.1) Xw = v∈JW,v≤w

PJ\PJvB.

An interesting question is:

Question 1.1. How many complex i-dimensional cells occur in the decomposition (1.1) of Xw?

Let us denote this number by Jbwi . Equation (1.1) gives the equality

- (1.2) Jbwi = Card v ∈ JW v ≤ w and ℓ(v) = i ,

which also equals the 2i-dimensional Betti number of Xw (the odd dimensional Betti numbers of Xw are 0).

Question 1.1 is diﬃcult to answer in general. If Xw is smooth, the

Poincare´ duality for ordinary cohomology implies that Jbwi = Jbwℓ(w)−i. While the hard Lefschetz theorem for ordinary cohomology of smooth projective

varieties implies that the sequence (Jbwi )i is unimodal. This means that for some 0 ≤ k ≤ ℓ(w) (here k = ⌈ℓ(w)/2⌉), we have

Jbw0 ≤ Jbw1 ≤ ··· ≤ Jbwk−1 ≤ Jbwk ≥ Jbwk+1 ≥ ··· ≥ Jbwℓ(w). But Xw is singular in general, hence Poincare´ duality and hard Lefschetz theorem for ordinary cohomology usually fail. By means of deep results in Hodge theory such as the purity theorem and hard Lefschetz theorem for the intersection cohomology [2], Bjo¨rner and Ekedahl [5] showed that, for every w ∈ JW, the sequence (Jbwi )i satisﬁes the following two sets of inequalities:

Jbwi ≤ Jbwℓ(w)−i for i ≤

ℓ(w) 2

![image 3](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile3.png>)

- (1.3) , and Jbw0 ≤ Jbw1 ≤ ··· ≤ Jbw⌈ℓ(w)/2⌉.


The ﬁrst set of inequalities is rephrased as the sequence being top-heavy, while the second is the fact that the sequence is weakly increasing in the “lower half part”.

Some variants of Question 1.1 have been studied. By Equation (1.2), one can formulate an analog of Question 1.1 for general Coxeter groups. Using Soergel bimodules and their Hodge theory established by Elias and Williamson in their foundational paper [15], it is proven that the analog of the inequalities (1.3) holds for general Coxeter groups in the non-parabolic case (that is, J = ∅, see [32]). For the parabolic case, we believe that a proof of these inequalities should follow from the Hodge theory of singular Soergel bimodules, see [31] and [32, Remark 3.18]. On the other hand, in the context of Schubert varieties of hyperplane arrangements, Huh and Wang [21] proved Dowling and Wilson’s “Top-Heavy conjecture” for matroids realizable over some ﬁeld using Hodge-theoretic ideas analogous to the ones in Bjo¨rner and Ekedahl [5]. Later, Braden, Huh, Matherne, Proudfoot, and Wang [7] achieved the remarkable task of generalizing this result to every matroid by establishing Hodge theory for the intersection cohomology of matroids.

Despite these great achievements, the unimodality of (Jbwi )i for the “upper half part” remains an interesting open problem. To the best of our knowledge, there is no partial result yet. However, conjectures related to this problem have been made. Before we get into these, let us recall that a sequence (a0,a1,... ,an) of positive real numbers is said to be log-concave if

ai−1ai+1 ≤ a2i for all 0 < i < n.

This notion is stronger: log-concave sequences are always unimodal. Regarding log-concavity of Bruhat intervals, Brenti conjectured the following:

Conjecture 1.2 ([9, Conjecture 2.11]). Let W be a Weyl group, and u,v ∈ W. The sequence (b[iu,v])i is log-concave, where

b[iu,v] = Card{w ∈ W |u ≤ w ≤ v,ℓ(w) = i} .

The parallel conjecture in the setting of matroids and Schubert varieties of hyperplane arrangements is known as “Rota’s unimodality conjecture” [34]. Its simplest non-trivial case for rank-3 realizable matroids is referred to as the “points-lines-planes conjecture” and it remains open.

The parabolic analog of Conjecture 1.2 does not hold. For example, consider the symmetric group W = S12 with generating set S = {s1,... ,s11} where si = (i,i+1) is the corresponding adjacent transposition and J := S\ {s4}. According to Stanton [36], Young’s lattice for the partition (8,8,4,4) deﬁnes a non-unimodal sequence

(1,1,2,3,5,6,9, 11,15,17, 21,23,27, 28,31, 30, 31,27,24,18,14,8, 5, 2, 1).

This is the sequence (Jbwi )i corresponding to a parabolic lower Bruhat interval of JW, which gives the Betti numbers of the Schubert variety X(8,8,4,4) inside the Grassmannian Gr(4,12).

- 1.2. Our setting


Let W = ZΦ∨⋊Wf be the aﬃne Weyl group with Weyl group Wf and root system Φ of rank r. Let (E,(−|−)) be the r-dimensional Euclidean space where Φ lives. Let fW (resp. Wf) be the set of minimal representatives for the right cosets Wf\W (resp. left cosets W/Wf). We denote by C+ the dominant Weyl chamber. Let λ ∈ ZΦ∨ ∩ C+ be a dominant coroot lattice element, and tλ ∈ W be the translation by λ. Let

![image 4](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile4.png>)

f[e,tλ] := {w ∈ fW | w ≤ tλ} be the dominant lower Bruhat interval (see Section 2 for details.) The inverse map w  → w−1 preserves the length and the Bruhat–Chevalley order. It restricts to a bijection from f[e,tλ] to [e,t−λ]f := {w ∈ Wf | w ≤ t−λ}, where the second Bruhat interval corresponds to a (spherical) Schubert variety in the corresponding aﬃne Grassmannian as we will explain below.

- 1.2.1. Spherical Schubert varieties in the aﬃne Grassmannian. We recommend [1, Chapter 9], [23], and [41] for a more in-depth introduction to the aﬃne Grassmannians.


Let G be the semisimple and simply connected complex algebraic group with coroot lattice ZΦ∨. Let B be a Borel subgroup of G and T ⊂ B be a maximal torus. Let F = C((t)) with ring of integers O = C[[t]]. The algebraic loop group G(F) has a maximal compact group K = G(O). Consider the evaluation at t = 0 map

ev: K = G(O) −−→t=0 G(C) = G, and consider the Iwahori subgroup

I := ev−1 (B). The aﬃne Grassmannian associated to G is

Gr := G(F)/K, which is an ind-projective variety.

The aﬃne Grassmannian Gr has the following decomposition into Korbits:

Grλ where Grλ := KtλK/K.

Gr =

![image 5](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile5.png>)

λ∈ZΦ∨∩C+

We regard tλ as a point in G(C t±1 ) ⊂ G(F). Let NG(F)(T) be the normalizer of T in G(F). The isomorphism NG(F)(T)/T → W sends tλ to the anti-dominant translation t−λ ∈ Wf [24, Section 4.1]. The corresponding spherical Schubert variety is

![image 6](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile6.png>)

Grλ =

Grµ,

![image 7](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile7.png>)

µ∈ZΦ∨∩C+, µ λ

where µ λ if and only if λ − µ is a sum of positive coroots. It plays an important role in geometric representation theory since its intersection cohomology carries the structure of the simple G∨-module of the Langlands dual group G∨ with highest weight λ [26] via the celebrated geometric Satake equivalence [27], a cornerstone of the geometric Langlands program.

On the other hand, the I-orbits on Gr give the Bruhat decomposition Gr =

IxK/K.

x∈Wf

We have the Schubert variety Xy := IyK/K =

![image 8](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile8.png>)

IxK/K.

x∈Wf, x≤y

Each I-orbit IxK/K is a Schubert cell which is isomorphic to the aﬃne space of dimension ℓ(x).

By considering the I-orbits, we have [24, Section 4.3] Grλ = Xt−λ,

![image 9](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile9.png>)

![image 10](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile10.png>)

that is, the spherical Schubert variety Grλ is a special Schubert variety Xt−λ indexed by the translation t−λ ∈ Wf, where −λ is anti-dominant. After taking inverses, we can see that the topological information of Grλ is encoded in the dominant lower Bruhat interval f[e,tλ].

![image 11](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile11.png>)

- 1.3. Main results In this paper, we prove that the length-counting sequence


fbtiλ := Card w ∈ f[e,tλ] ℓ(w) = i , i = 0,1,... ,ℓ(tλ),

of f[e,tλ], which is the sequence of Betti numbers of the spherical Schubert variety Gr−w0λ = Xt−λ is asymptotically log-concave. This statement consists of two parts:

![image 12](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile12.png>)

- • Theorem 1.3, which informally speaking, tells us that the “shape” of

the length-counting sequences of the k-fold dilated intervals f[e,tkλ] converges to a continuous function as k tends to inﬁnity (see Figure 1 for an illustration).

- • Corollary 1.6, which states that this continuous function is logconcave.


- 1.3.1. Asymptotic convergence. Let λ ∈ ZΦ∨ ∩ C+. We deﬁne the convex polytope


![image 13](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile13.png>)

Pλ := Conv{wλ | w ∈ Wf} ∩ C+ ⊂ E, where Conv denotes the convex hull of a set (see Section 4.1 for details.)

![image 14](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile14.png>)

Let ht: Pλ → R be the height function ht(x) := (2ρ|x), where ρ is the half-sum of positive roots. In particular, ht(λ) = ℓ(tλ). We denote by Volr the Lebesgue measure on E and by ht∗Volr the corresponding push-forward measure on R. We also denote by Volr−1 the Lebesgue measure on aﬃne hyperplanes of E. Then, the density function of ht∗Volr, which is

- 1

![image 15](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile15.png>)

- 2ρ


Volr−1(ht−1(z)), z ∈ R,

g(z) =

evaluates volumes of hyperplane sections of the polytope Pλ up to a scalar (see Section 5 for details.)

Let δz denote the Dirac measure (that is, point mass) at the point z ∈ R. For any positive integer k, we deﬁne the discrete measure mk supported on [0,ℓ(tλ)] by

- (1.4) mk :=


1 kr

fbtikλδ i

.

![image 16](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile16.png>)

![image 17](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile17.png>)

k

0≤i≤kℓ(tλ)

Intuitively, mk distributes the sequence (fbtikλ)i evenly on the interval [0,ℓ(tλ)]. We also deﬁne the step function Sk: [0,ℓ(tλ)] → R by

i k

i + 1 k

1 kr−1

fbtikλ, whenever z ∈

,

.

Sk(z) :=

![image 18](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile18.png>)

![image 19](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile19.png>)

![image 20](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile20.png>)

The function Sk records the numbers (fbtikλ)i and behaves like the “density function” of mk (see Section 6 for details.) The following is our main theorem.

- Theorem 1.3. Let Volr(A+) be the volume of the fundamental alcove A+.

- (1) (The weak convergence of (mk)k). The sequence of measures (mk)k, as k tends to inﬁnity, converges weakly to the measure

1 Volr(A+)

![image 21](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile21.png>)

ht∗Volr.

- (2) (The uniform convergence of (Sk)k). The sequence of functions


(Sk)k, as k tends to inﬁnity, converges uniformly to the function

1

![image 22](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile22.png>)

Volr(A+)g.

This convergence result also holds for general “dominant” elements, that is, elements in fW. See Section 7.

- 1.3.2. The dominant lattice formula. We deﬁne the Poincare´ polynomial πtλ(q) of the sequence (fbtiλ)i by

πtλ(q) :=

0≤i≤ℓ(tλ)

fbtiλqi,

which is the Poincare´ polynomial of the singular cohomology of the spherical Schubert variety Grλ = Xt−λ as we explained in the previous section. Moreover, for µ ∈ ZΦ∨, we write

![image 23](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile23.png>)

µπf(q) :=

w∈µWf

qℓ(w),

where µWf is the set of minimal representatives for the right cosets Wf,µ\Wf, and Wf,µ is the stabilizer of µ in Wf.

One of the key ingredients to prove Theorem 1.3 is the following formula, which is one of our most important results (see Figure 3 for an illustration). Theorem 1.4 (Dominant lattice formula). Let λ ∈ ZΦ∨ ∩ C+. We have

![image 24](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile24.png>)

πtλ(q) =

µ∈Pλ∩ZΦ∨

q(2ρ|µ) · µπf(q−1).

This formula is a powerful way—in terms of computer eﬃciency—to obtain the generating function of the sequence (fbtiλ)i from the set of lattice points in Pλ. The evaluation at q = 1 gives a formula for Card(f[e,tλ]), while the coeﬃcient of qi gives a formula for fbtiλ.

- 1.3.3. Log-concavity and a conjecture on unimodality. Recall that a real function f deﬁned on a convex subset U of a vector space V is called concave




if f a+2b ≥ f(a)+2f(b) for any a,b ∈ U. The following result follows from the classical Brunn–Minkowski inequality.

![image 25](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile25.png>)

![image 26](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile26.png>)

- Theorem 1.5 (Brunn–Minkowski, see [29, p. 270]). Let L1 be a real vector space and let M ⊂ L1 be a convex body. Let p: L1 → L2 be a linear transformation. Then


z  → Vol p−1(z) ∩ M

is a concave function on p(M).

1/(dim M−dimp(M))

Applying the above theorem to the map ht: Pλ → R and composing with the logarithm function (which is concave), we immediately have the following corollary.

- Corollary 1.6. The density function g of the measure ht∗Volr is log-concave. That is, log g is a concave function.


Note that even though log g(z) = −∞ if z ∈/ [0,ℓ(tλ)], the notion of concavity still makes sense.

- Remark 1.7. Asymptotic log-concavity turns out to be an interesting fact


since the sequence (fbtiλ)i can fail to be log-concave itself. For example, from the step function in Figure 1(a), we observe that the sequence contains the

consecutive terms (4,4,5).

In spite of Remark 1.7, the unimodality of the sequence (fbtiλ)i might hold without the need to take limits, and it has been tested in many small rank cases (see below). We state it as a conjecture.

Conjecture 1.8. The sequence (fbtiλ)i is unimodal.

Before listing the computational evidence of the conjecture above, let us deﬁne λ to be below a vector v if, under the basis of fundamental coweights, each coeﬃcient of λ is less than or equal to the corresponding coeﬃcient of v.

We veriﬁed Conjecture 1.8 with the software SageMath and the help of our dominant lattice formula (which considerably reduced the time of computations) for several λ ∈ ZΦ∨ in cases where the rank of Φ is not too big:

- • rank(Φ) ≤ 3: for Φ of each type, we tested hundreds of λ, and we omit the details.
- • rank(Φ) = 4:

- ◦ Φ of type A. Tested for the 30 intervals with λ below [2,3,3,2].
- ◦ Φ of type B. Tested for the 54 intervals with λ below [2,2,3,2].
- ◦ Φ of type C. Tested for the 48 intervals with λ below [2,2,3,2].
- ◦ Φ of type D. Tested for the 30 intervals with λ below [2,2,3,2].
- ◦ Φ of type F. Tested for the 36 intervals with λ below [1,2,2,1].


- • rank(Φ) = 5: Φ of type A. Tested for the 24 intervals with λ below [1,2,3,2,1].


We did not test other Φ’s due to the limitation of our computer resources.

- 1.4. An example


Example 1.9 (Type C3). Let W be the aﬃne Weyl group associated with the root system Φ of type C3 and simple roots ∆ = {α1,α2,α3}. Then, r = 3. Following [6, Plate III], we write α1 = ǫ1 − ǫ2, α2 = ǫ2 − ǫ3, and α3 = 2ǫ3. Let

λ = 3α∨1 + 6α∨2 + 7α∨3 .

We have that ht(λ) = 32. For convenience, let (a,b,c)Φ := aα∨1 +bα∨2 +cα∨3 . The polytope Pλ is the convex polyhedron with six vertices given by

{(0,0,0)Φ,(3,3,3)Φ,(3,5,7)Φ,(3,6,6)Φ,(7/3,14/3,7)Φ,(3,6,7)Φ}, which is an example of a non-lattice polytope. Since ρ = (3,5,3)Φ, we get

ρ = √14. By direct computations, we have Vol3(A+) = 1/48. In view of Theorem 1.3(2), the only missing ingredient to compute the limit function is to determine Vol2(ht−1(z)). By the theory of convex polytopes, this function is a piecewise quadratic polynomial, and its exact form can be obtained by Lagrange interpolation. We omit details and give a graph of the function g/Vol3(A+) in Figure 1(d).

![image 27](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile27.png>)

(a) Graph of S1. (b) Graph of S2.

(c) Graph of S8. (d) Graph of g/ Volr(A+).

Figure 1. In the aﬃne Weyl group W of aﬃne type C3, we consider λ = 3α∨1 +6α∨2 +7α∨3 . These pictures illustrate how the sequence of step functions Sk : [0,ℓ(tλ)] → R converges uniformly to a continuous function.

We can use Theorem 1.3(2) to give quick estimates of the terms in the sequence (fbtikλ)i when k is big. For instance, when k = 8, the value of fbt1968λ

is virtually impossible to obtain in a computer directly from deﬁnitions. Let us take z = 24.5(= 196/8). By our theorem, we have

389 30

1 82

fbt1968λ ∼ 48g(24.5) =

,

S8(24.5) =

![image 28](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile28.png>)

![image 29](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile29.png>)

which gives fbt1968λ ∼ 829.87.

On the other hand, our dominant lattice formula gives the exact values of the terms in the sequence (fbtikλ)i (which takes a considerable time to get in a computer.) In particular, we have fbt1968λ = 863. Our quick estimate of 829.87 was oﬀ by 3.84%. See Figure 1 for the graphs of the step functions S1, S2, and S8.

- 1.5. Connections with other works


- 1.5.1. Asymptotic behavior of weight multiplicities. Let K be a compact


connected Lie group with a maximal torus T, let Wf be the corresponding Weyl group, and let λ be a dominant weight of T. In [20], Heckman used

the weight multiplicities dimV (kλ)µ of the irreducible representation of K with highest weight kλ to construct a discrete measure

µ dimV (kλ)µδµ

![image 30](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile30.png>)

k

,

![image 31](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile31.png>)

µ dimV (kλ)µ

supported on the weight polytope Conv{wλ | w ∈ Wf}. He proved that this sequence of discrete measures, as k tends to inﬁnity, converges weakly to the push-forward of the Liouville measure of the coadjoint orbit of λ under the moment map. The limit measure is the Duistermaat–Heckman measure associated with λ. Its density function—the Duistermaat–Heckman function—is a piecewise polynomial [13], and Graham proved that it is logconcave via Hodge–Riemann inequalities [17].

Later, Okounkov [28] introduced the Newton–Okounkov bodies to prove that, in a similar weak limit sense, for any representation V of a reductive group G, the multiplicities of irreducible G-modules in the homogeneous coordinate ring of a G-stable irreducible subvariety of P(V ) are log-concave. In a sequel paper [30], Okounkov pointed out the importance of log-concavity and related it to the properties of entropy in statistical physics.

Our construction in Equation (1.4) and the formulation of Theorem 1.3(1) draw inspiration from the works of Heckman [20] and Okounkov [28]. Actually, Theorem 1.3(1) has the following representation-theoretic interpretation: Let G be the semisimple and simply connected complex algebraic group and B be a Borel subgroup of G as in Section 1.2.1. Let ˇg be the complex semisimple Lie algebra of the Langlands dual group G∨. Consider a standard principal nilpotent element e ∈ ˇg, and let X = (G∨)e denote the stabilizer of e in G∨ under the adjoint action. The subgroup X is abelian and has dimension equal to the rank of G. For instance, in type A, X is the group of upper-triangular unipotent Toeplitz matrices [33]. Let ˇge be the abelian Lie algebra of X. By Ginzburg’s theorem [16, Theorem 1.5], the

canonical map

H•(Grλ,C) → IH •(Grλ,C) is injective and corresponds, under the geometric Satake equivalence, to the inclusion

![image 32](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile32.png>)

![image 33](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile33.png>)

U → Vλ,

where Vλ is the simple G∨-module with highest weight λ and U is the cyclic submodule of the enveloping algebra U(ˇge) generated by a lowest weight

vector vλ of Vλ. Note that gˇe is stable under the adjoint action of a regular semisimple element and the weight decomposition gives a grading on U(ˇge)

and hence on U = U(ˇge)/AnnU(ˇge)vλ, which corresponds to the cohomological grading on H•(Grλ,C). Therefore, Theorem 1.3(1) explicitly computes the Duistermaat–Heckman measure of the one-dimensional torus C× generated by the regular semisimple element acting on U. The corresponding Duistermaat–Heckman function is then given by the density function g of ht∗Volr up to a constant.

![image 34](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile34.png>)

Nevertheless, our framework and proof techniques diﬀer signiﬁcantly from Heckman’s work since there is no symplectic manifold related to the module U. Hence, it is not immediately clear that our original cell-counting problem has such a fundamental connection to the geometry of a convex polytope. Furthermore, Theorem 1.3(2) is novel compared to the results of Heckman and Okounkov, and it is stronger than Theorem 1.3(1) (see Remark 6.13).

- 1.5.2. Ehrhart’s theory. For an r-dimensional lattice polytope P (that is, all vertices of P are points of a given lattice L), the Ehrhart polynomial [14] E(P,k) is a rational polynomial in k that counts the number of lattice points in the k-fold dilation kP. That is, there exist rational numbers E0(P),... ,Er(P), such that


E(P,k) := |L ∩ kP| = Er(P)kr + Er−1(P)kr−1 + ··· + E0(P)

for all positive integers k. The leading coeﬃcient, Er(P), is equal to the r-dimensional volume Volr(P) of P, divided by the volume d(L) of the fundamental region of the lattice L. This implies that

d(L) · |L ∩ kP| kr

.

- (1.5) Volr(P) = lim k→∞


![image 35](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile35.png>)

If X is the toric variety associated with P, then P deﬁnes an ample line bundle on X. The Ehrhart polynomial of P coincides with the Hilbert polynomial of this line bundle, and the above asymptotic result (1.5) is a consequence of the asymptotic Riemann–Roch theorem [35, Tag 0BJ8].

The problem in our work is analogous to the one in Ehrhart’s theory. However, we count alcoves in each length rather than all lattice points in the polytope Pλ. When Pλ is not a lattice polytope, it has no Ehrhart polynomial, and the proof of Theorem 1.3(2) is technical (see Section 6.1 for an outline). We hope the proof techniques will be helpful in future works concerning general convex polytopes.

Let r = rank(Φ). We want to raise the following question:

- Question 1.10. For k suﬃciently large, is the total Betti number

Card f[e,tkλ] =

i

fbtikλ

a quasi-polynomial1 in k of degree r, with Volr(P

λ)

![image 36](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile36.png>)

Volr(A+) as the leading coeﬃcient?

Our main object of study, the sequence (fbtiλ)i, is related to a reﬁnement of this question, which deals with some slices of Pλ instead of Pλ as a whole. These slices are hyperplane sections ht−1(i) of Pλ, for diﬀerent values of

i. Theorem 1.4 relates (fbtiλ)i with the numbers of lattice points in these diﬀerent slices. The reﬁnement of Question 1.10 is the following:

- Question 1.11. For k suﬃciently large, is fbtkikλ a quasi-polynomial in k of degree (r − 1) with


Volr−1(ht−1(i)) Volr(A+) · 2ρ

![image 37](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile37.png>)

as the leading coeﬃcient?

If the answer to Question 1.11 is yes, this immediately implies Corollary 6.2.

- 1.5.3. Euclidean geometry of alcoves. In his expository paper [25], Libedinsky conjectured an intrinsic connection between Bruhat intervals for aﬃne Weyl groups and Euclidean geometry. The results in the present paper give some evidence in this regard: From the perspective of Euclidean geometry, a Bruhat interval can be realized as a region—a union of ﬁnitely


many alcoves—inside E. As the lattice element λ in the interval f[e,tλ] is dilated and the region is rescaled accordingly, the alcoves within it become progressively smaller. In the limit, the region converges to the polytope Pλ (Figure 2). This observation is the main geometric intuition behind Theorem 1.3.

Although connections between convex polytopes and the aﬃne Bruhat order are well known, their precise formulations can be unexpectedly subtle. For example, even in the simplest nontrivial case of type A2, making the connection between an aﬃne Bruhat interval and a convex polygon explicit proved highly nontrivial, as shown in [11, Theorem C].

For elements associated with dominant coweights µ, Castillo, de la Fuente, Libedinsky, and Plaza proved a “Geometric Formula” [12, Theorem B] relating the cardinality of the corresponding lower Bruhat interval and volumes of faces of the weight polytope Conv{wµ | w ∈ Wf} using their “Lattice formula” [12, Theorem A]. Our dominant lattice formula is similar to theirs but with some diﬀerences: their lattice formula considers the presence of

![image 38](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile38.png>)

1A function f : N → N is a quasi-polynomial if there exist polynomials p0, . . . , ps−1 such that f(n) = pi(n) when i ≡ n mod s.

![image 39](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile39.png>)

![image 40](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile40.png>)

![image 41](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile41.png>)

ASYMPTOTIC LOG-CONCAVITY OF DOMINANT LOWER BRUHAT INTERVALS 13

(a) The Bruhat interval f[e,t2λ]. (b) The Bruhat interval f[e,t6λ].

(c) Polytope Pλ.

Figure 2. Behavior of the intervals f[e,tkλ] when W is of aﬃne type A2 and λ = 3α+4β, where α := α∨1 and β := α∨2 . In each picture, the set of small triangles corresponds to the set of alcoves. The coroot lattice is indicated by black bullets, and the dominant Weyl chamber is colored blue. In the ﬁrst two pictures, the alcoves corresponding to the elements in the intervals are ﬁlled with darker blue. So is the polytope Pλ in the third picture.

dominant and non-dominant weights, while our formula takes into account the length of each lattice point together with the singular phenomena when lattice points belong to walls of the dominant Weyl chamber. In view of their work, we would like to ask the following:

- Question 1.12. For λ ∈ ZΦ∨ ∩ C+, is there a convex geometry formula giving the cardinality of f[e,tλ] (that is, the total Betti number i fbtiλ of


![image 42](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile42.png>)

![image 43](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile43.png>)

the spherical Schubert variety Gr−w0λ = Xt−λ) in terms of volumes of faces of the polytope Pλ?

- 1.5.4. Measuring top-heaviness. Recall that Bjo¨rner and Ekedahl [5] showed


that the sequence (Jbwi )i is top-heavy, that is, Jbwi ≤ Jbwℓ(w)−i, for i ≤ ℓ(2w). It is natural to ask “how top-heavy” these sequences are. In this directionand inspired by the question at the end of [5]—we ask the following:

![image 44](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile44.png>)

- Question 1.13. For each Φ and λ ∈ ZΦ∨∩C+, let z0(λ) be the point where the density function of ht∗Volr(Pλ) reaches its maximum. Is it true that


![image 45](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile45.png>)

sup zℓ0(t(λ)

λ) = 1? Here, the supremum is taken over all root systems and all λ ∈ ZΦ∨ ∩ C+.

![image 46](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile46.png>)

![image 47](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile47.png>)

If the answer to the above question is yes, Theorem 1.3 would reveal the existence of an interesting family of non-trivial parabolic Kazhdan–Lusztig polynomials or, in other words, non-rationally-smooth aﬃne parabolic Schubert varieties.

- 1.6. Structure of the paper


The remainder of the paper is organized as follows. In Section 2, we introduce our notations and some preliminary results. In Section 3, we compare two partial orders related to our study: the partial order on ZΦ∨ and the Bruhat–Chevalley order ≤ on fW. In Section 4, we introduce our relevant sequences of study and the polytope Pλ, and prove the dominant lattice formula. In Section 5, we prove the weak convergence of the discrete measure sequence (mk)k. In Section 6, we prove the uniform convergence of the step function sequence (Sk)k. As a byproduct, we obtain a combinatorial identity (Equation (6.12)) related to the root system.

Acknowledgments

The ﬁrst author would like to express his gratitude to Anthony Henderson and Geordie Williamson for great discussions regarding the aﬃne Weyl group during his Ph.D. program. The authors would like to thank Allen Knutson, David Plaza, Alex Weekes, Ge Xiong, and Xinwen Zhu for their valuable communications. The third author is supported by the Fundamental Research Funds for the Central Universities (No. 531118010972).

2. Preliminaries

In this section, we recollect our notations and some preliminary results for later use. Throughout the paper, we use either Card(A) or |A| to denote the cardinality of a set A.

- 2.1. The aﬃne Weyl group and alcoves


Standard references for Sections 2.1 and 2.2 are [22, 6]. Let Φ be the (irreducible, reduced, and crystallographic) root system of a ﬁnite-dimensional

simple Lie algebra over C, and E be the Euclidean space where Φ lives. We denote by (−|−): E×E → R the inner product on E. For any root α ∈ Φ, we

denote by α∨ the corresponding coroot (α2|αα). Then Φ∨ := {α∨ ∈ E | α ∈ Φ} is the dual root system. We ﬁx a set ∆ = {αi | i = 1,... ,r} of simple roots of Φ, where r = dimE is the rank of Φ. Let

![image 48](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile48.png>)

si: E → E, x  → x − (x|αi)α∨i , i = 1,... ,r,

be the simple reﬂections. Let Wf := s1,... ,sr be the (ﬁnite) Weyl group associated with Φ.

For a nonzero vector β ∈ E and a real number z ∈ R, we have the hyperplane

Hβ,z := {x ∈ E | (x|β) = z} . The aﬃne Weyl group W associated with Φ is deﬁned to be the group of aﬃne transformations generated by aﬃne reﬂections {sα,k | α ∈ Φ+,k ∈ Z}, where Φ+ denotes the set of positive roots and sα,k is the aﬃne reﬂection along the aﬃne hyperplane Hα,k. Explicitly, the aﬃne reﬂection sα,k (α ∈ Φ+, k ∈ Z) is given by

- (2.1) sα,k(v) = v + k − (v|α) α∨ = sα,0(v) + kα∨, for all v ∈ E.

In particular, si = sαi,0 ∈ W for all i = 1,... ,r. Let α0 be the highest root in Φ, and s0 := sα0,1. Then, (W,S) is a Coxeter system with the set S := {s0,s1,... ,sr} of simple reﬂections. We denote by ℓ the length function on W and by ≤ the Bruhat–Chevalley order on W. For x,y ∈ W, we write x < y if x ≤ y and x = y. The restriction of ℓ to the ﬁnite Coxeter system (Wf,Sf) is also denoted by ℓ, where Sf = S \ {s0}.

The aﬃne Weyl group W is isomorphic to the semidirect product

ZΦ∨ ⋊ Wf, where ZΦ∨ is the coroot lattice. For any element λ ∈ ZΦ∨, we denote by tλ ∈ W the translation x  → x + λ on E. In the semidirect product decomposition, the element tλ corresponds to the pair (λ,idWf).

A connected component of E \{Hα,k | α ∈ Φ+,k ∈ Z} is called an alcove. The closure A of any alcove A is a fundamental domain for the action of W on E. Let

![image 49](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile49.png>)

A+ := {x ∈ E | 0 < (x|α) < 1 for all α ∈ Φ+} be the fundamental alcove. The group W acts on E and preserves the set of hyperplanes

{Hα,k | α ∈ Φ+,k ∈ Z}. Therefore, W acts on the set of alcoves. This action is simply transitive, hence induces a natural bijection between W and the set of alcoves

- (2.2) w  → Aw := wA+, for any w ∈ W. The following lemma is classical.


Lemma 2.1. Suppose w ∈ W, and s is a reﬂection along some hyperplane Hα,k for α ∈ Φ+ and k ∈ Z. Then:

- (1) sw > w if and only if the two alcoves A+ and Aw are in the same side of Hα,k, that is,

(u|α) − k (v|α) − k > 0 for some (and hence for all) u ∈ A+ and v ∈ Aw.

- (2) The length ℓ(w) of w equals the number of hyperplanes separating A+ and Aw, that is,

ℓ(w) = Card Hα,k

α ∈ Φ+, k ∈ Z, such that A+ and Aw lie in opposite sides of Hα,k

.

- (3) If s ∈ Sf, that is, α ∈ ∆ and k = 0, then ws > w if and only if A+ and Aw are in the same side of wHα,0.


- Remark 2.2. The statement “A+ and Aw are in the same side of wHα,0” in


Lemma 2.1(3) is equivalent to “Aw−1 and A+ are in the same side of Hα,0”, that is,

(u|α)(v|α) > 0 for some (and hence for all) u ∈ Aw−1 and v ∈ A+. Since taking inverse preserves the Bruhat–Chevalley order, Lemma 2.1(3) follows from Lemma 2.1(1).

By the orbit-stabilizer theorem, we have the following lemma.

Lemma 2.3. We have a natural bijection ZΦ∨ → W/Wf given by λ  → tλWf.

Proof. The action of W on E induces a transitive action of W on the lattice ZΦ∨, and the stabilizer of the origin 0 ∈ E is exactly Wf.

Remark 2.4. The lattice point λ ∈ ZΦ∨ belongs to the closure of Aw (w ∈ W) if and only if w ∈ tλWf. Geometrically, the alcoves {Aw | w ∈ tλWf} are the translation by λ of the alcoves corresponding to Wf, and they are “arranged” around λ.

- 2.2. Dominant alcoves and fW The dominant Weyl chamber C+ is deﬁned by


C+ := {x ∈ E | (x|αi) > 0, for all i = 1,... ,r},

which is an open simplicial cone in E. The hyperplanes {Hα,0 | α ∈ ∆} are called the walls of C+. A point x ∈ E is called strongly dominant if

![image 50](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile50.png>)

![image 51](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile51.png>)

- x ∈ C+, and dominant if x ∈ C+, the closure of C+. The closed cone C+ is a fundamental domain for the action of Wf on E. Each alcove A is contained in C+ or has an empty intersection with C+; in the ﬁrst case, we say that A is dominant.


The Weyl group (Wf,Sf) is a standard parabolic subgroup of the aﬃne Weyl group (W,S). As mentioned in the introduction, fW ⊂ W is deﬁned to be the set of minimal representatives for the right cosets Wf\W. By Lemma 2.1(1), we immediately have the following proposition. It states

that under the bijection (2.2) the set fW corresponds to the set of dominant alcoves.

- Proposition 2.5. An element w ∈ W is the minimal length representative in its right coset Wfw (that is, w ∈ fW) if and only if Aw is dominant, that is, Aw ⊂ C+. In particular, for any λ ∈ ZΦ∨ ∩ C+, we have tλ ∈ fW.


![image 52](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile52.png>)

Therefore, we call the set f[e,w] := {v ∈ fW | v ≤ w} a dominant lower Bruhat interval.

Let ρ := 21 α∈Φ+ α be the half-sum of all positive roots2. Moreover, let ρ∨ := 21 α∈Φ+ α∨ be the half-sum of all positive coroots (in general, ρ∨ and (ρ2|ρρ) are not the same). The next lemma and its following corollary are standard.

![image 53](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile53.png>)

![image 54](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile54.png>)

![image 55](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile55.png>)

- Lemma 2.6 ([6, Ch. VI, Sect. 1, No. 10]). We have (ρ|α∨i ) = 1 and (ρ∨|αi) = 1 for all i = 1,... ,r.


- Corollary 2.7. There is δ ∈ R>0 such that ερ∨ ∈ A+ for any 0 < ε < δ.


The following lemma computes the length of tλ for λ ∈ ZΦ∨ ∩ C+. This is a particular case of [22, Proposition 1.23].

![image 56](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile56.png>)

- Lemma 2.8. For any λ ∈ ZΦ∨ ∩ C+, we have ℓ(tλ) = (2ρ|λ). Corollary 2.9. For any λ ∈ ZΦ∨ ∩C+ and k ∈ N, we have ℓ(tkλ) = kℓ(tλ).


![image 57](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile57.png>)

![image 58](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile58.png>)

The following lemma is useful when dealing with λ ∈ ZΦ∨ on some walls of the dominant Weyl chamber C+.

- Lemma 2.10. Suppose λ ∈ ZΦ∨ ∩ C+. Let I := {i | 1 ≤ i ≤ r,(λ|αi) = 0},


![image 59](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile59.png>)

that is, λ belongs to the wall Hαi,0 if i ∈ I. Then, we have: tλsi > tλ if i ∈ I; tλsi < tλ if i ∈ {1,... ,r} \ I.

Proof. By Lemma 2.1(3), it suﬃces to show that A+ and Atλ lie in the same side of tλHαi,0 if and only if i ∈ I. This statement is equivalent to the following:

- (2.3) At−λ and A+ lie in the same side of Hαi,0 if and only if i ∈ I.


Let ε ∈ R>0 be small enough such that ερ∨ ∈ A+ (see Corollary 2.7). For all i = 1,... ,r, we have (ρ∨|αi) = 1. Moreover, (λ|αi) ≥ 1 if i ∈/ I. Thus, (ερ∨|αi) = ε > 0, and

> 0, if i ∈ I, < 0, if i ∈/ I.

(ερ∨ − λ|αi) = ε − (λ|αi)

Since ερ∨ ∈ A+ and ερ∨ − λ ∈ At−λ, this veriﬁes the statement (2.3).

![image 60](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile60.png>)

2The vector ρ is often called the Weyl vector in the literature.

- Corollary 2.11. If a coroot lattice point λ is strongly dominant, that is, λ ∈ ZΦ∨ ∩ C+, then tλ is the maximal element in the left coset tλWf. Proof. If λ is strongly dominant, then the set I in Lemma 2.10 is empty. Thus tλsi < tλ for all i = 1,... ,r.


- Remark 2.12. Let λ ∈ ZΦ∨ ∩ C+, then tλ is the minimal representative for the right coset Wftλ by Proposition 2.5 and the maximal representative for the left cost tλWf by Corollary 2.11.


- 2.3. Measures on R and E


In this subsection, we recollect some terminology and basic results about weak convergence of measures. For a more complete exposition, we refer to [3, 4].

Let B be the Borel σ-ﬁeld in R generated by the set of open subsets, that is, the smallest collection of subsets of R containing all open subsets, which is closed under taking complements, countable unions, and countable intersections. A set in B is called a Borel set. In particular, any countable set is a Borel set. A measure m on (R,B) (or simply, on R) is a set function m: B → R≥0 ∪ {∞} such that m(∅) = 0 and m( ∞i=1 Ui) = ∞i=1 m(Ui) for any sequence of disjoint sets (Ui)i.

A measure m on R is said to be bounded if m(R) < ∞. If a closed set F ⊂ R is such that m(R \ F) = 0, we say that m is supported on F.

- Deﬁnition 2.13. A sequence of bounded measures (mk)k is said to converge weakly to a measure m if


lim

f dmk = f dm for any bounded continuous real function f.

k→∞

- Lemma 2.14 ([3, Sect. 25], [4, Example 2.3]). A sequence of bounded measures (mk)k on R converges weakly to a measure m if and only if


mk (−∞,z] = m (−∞,z] for any z ∈ R such that m({z}) = 0.

lim

k→∞

- Remark 2.15. There is another notion of convergence of measures. A sequence of measures (mk)k is said to converge strongly (or setwise) to a measure m if limk→∞ mk(U) = m(U) for any Borel set U.


On the r-dimensional Euclidean space E where the root system Φ lives, we have the Lebesgue measure induced by the inner product (−|−). This measure is denoted by Volr. Moreover, for an i-dimensional aﬃne subspace M in E (i = 0,1,... ,r − 1), we can talk about the i-dimensional Lebesgue measure Voli on M which is also induced by (−|−). For example, Vol1(v) =

![image 61](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile61.png>)

(v|v) is the length of a vector v, also denoted by v . Let D be the open parallelotope spanned by the simple coroots, that is,

r

aiα∨i ∈ E 0 < ai < 1 for all i .

D :=

i=1

The following lemma relates the volumes of D and A+.

- Lemma 2.16. Volr(D) = |Wf| · Volr(A+). Proof. We have the following facts:

- (1) W acts continuously and properly on E, and Volr is a W-invariant measure;
- (2) ZΦ∨ is a subgroup of W;
- (3) A+ and D are both open subsets of E with ﬁnite non-zero measure;
- (4) the unions E′ := w∈W wA+ and E′′ := λ∈ZΦ∨ tλD are both disjoint;
- (5) Volr(E \ E′) = Volr(E \ E′′) = 0.


Applying [6, Ch. VI, Sect. 2, No. 4, Lemma 1] to the above facts, we obtain

|Wf| = (W : ZΦ∨) =

Volr(D) Volr(A+)

![image 62](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile62.png>)

as desired. 2.4. Polytopes

For references on polytopes, one may refer to [18, 42]. A (convex) polytope P in the Euclidean space E is the convex hull of a ﬁnite set of points in E. Note that a polytope is a bounded closed set. Equivalently, a polytope in E is a bounded subset of E, which can be written in the form

P =

i=1,...,k

{x ∈ E | fi(x) ≥ ai},

where each fi is a linear function on E and ai ∈ R. We deﬁne an open face of P to be an equivalence class of the equivalence relation ∼ on P deﬁned by x ∼ y if for each i = 1,... ,k, we have fi(x) = ai if and only if fi(y) = ai. The closure of an open face is called a face. Clearly, P is a disjoint union of ﬁnitely many open faces.

For a subset M of E, we denote by M aﬀ the aﬃne subspace of E spanned by M, that is, the smallest aﬃne subspace containing M. For an open face F◦ of P and the corresponding face F = F◦, F◦ is the relative interior of F and it is an open subset of F◦ aﬀ (hence we call it an “open face”). The dimension of F◦ and F is deﬁned to be the dimension of F◦ aﬀ. In particular, the 0-dimensional open faces of P are the same as the 0-dimensional faces of P, that is, the vertices of P. The dimension of P is the maximal dimension among its faces. We list some elementary facts without proof.

![image 63](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile63.png>)

- Lemma 2.17. Let P be a polytope in E, and H ⊆ E be an aﬃne hyperplane.


- (1) If P ∩ H is not empty, then it is a polytope.
- (2) If F◦ is an open face of P and F◦ ∩ H = ∅, then F◦ ∩ H is an open face of P ∩ H.
- (3) Any open face of P ∩ H is of the form F◦ ∩ H for some open face F◦ of P.


3. The partial order and the Bruhat–Chevalley order

Besides the Bruhat–Chevalley order ≤ on W, there are two other related partial orders. One is deﬁned on ZΦ∨ and the other on W.

- Deﬁnition 3.1.


- (1) For λ,µ ∈ E, we write µ λ if λ − µ is a non-negative linear

combination of simple coroots {α∨1 ,... ,α∨r } (as well as simple roots). This gives a partial order on E. For simplicity, we write µ ≺ λ if

µ λ and µ = λ. (Note that if λ,µ ∈ ZΦ∨ and µ λ, then λ − µ is a non-negative integral linear combination of simple coroots.)

- (2) For x,y ∈ W, we write y ≤a x if there exists a sequence of elements (y = y0,y1,... ,yn−1,yn = x) in W and a sequence of aﬃne reﬂections


{sβi,ki | βi ∈ Φ+,ki ∈ Z,i = 1,... ,n},

such that for each i = 1,... ,n, we have sβi,kiyi = yi−1 and (ui|βi) > ki for some (and hence for all) ui ∈ Ayi. Following Verma [39] and Wang [40], we call the partial order ≤a on W the aﬃne order.

In Deﬁnition 3.1(2), we have ui ∈ Ayi, sβi,ki(ui) ∈ Ayi−1, and

ui − sβi,ki(ui) = ui − ui + ki − (ui|βi) βi∨ = (ui|βi) − ki βi∨ which is a positive multiple of βi∨. Inductively, we have:

- Corollary 3.2. If x,y ∈ W and y ≤a x, then u − yx−1(u) is an R≥0-linear combination of simple coroots for any u ∈ Ax (and hence yx−1(u) ∈ Ay).


We have the following relation between the aﬃne order ≤a on W and the partial order on ZΦ∨, which says that ≤a is an extension of .

- Lemma 3.3. For two lattice points µ,λ ∈ ZΦ∨, tµ ≤a tλ if and only if µ λ.


Proof. Suppose tµ ≤a tλ. For u ∈ Atλ, we have tµt−λ1(u) = u − λ + µ ∈ Atµ. By Corollary 3.2, u − tµt−λ1(u) = λ − µ is an R≥0-linear combination of simple coroots. Therefore, we have µ λ.

Conversely, suppose µ λ. By induction, we may assume λ = µ + α∨ for some simple coroot α∨. Let k = (λ|α) ∈ Z. From the formula of aﬃne reﬂections in Equation (2.1), one may easily verify that sα,k−1sα,k = t−α∨. Therefore,

sα,k−1sα,ktλ = tµ. We choose ε ∈ R>0 small enough so that ερ∨ ∈ A+ as in Corollary 2.7. Then λ + ερ∨ ∈ Atλ. Moreover,

(λ + ερ∨|α) = k + ε > k.

This implies sα,ktλ ≤a tλ by Deﬁnition 3.1(2). Similarly, sα,k(λ + ερ∨) ∈ Asα,ktλ, and

sα,k(λ + ερ∨) α = λ + ερ∨ + k − (λ + ερ∨|α) α∨ α

= (λ + ερ∨|α) + 2(k − (λ + ερ∨|α))

= k − ε > k − 1.

This gives tµ = sα,k−1sα,ktλ ≤a sα,ktλ ≤a tλ.

The following lemma states that the Bruhat–Chevalley order and the aﬃne order coincide for elements in fW.

- Lemma 3.4 ([39, Sect. 1.6]). For x,y ∈ fW, y ≤ x if and only if y ≤a x.


- Remark 3.5. The assertion in Lemma 3.4 was ﬁrstly stated and partially proved by Verma [39, Sect. 1.6]. However, Verma skipped the key point (whose proof is somewhat involved) in his incomplete proof and referred it to his unpublished preprint [38]. A complete proof can be found in Wang’s paper [40], whose Chinese original appeared 12 years later than Verma’s paper. According to Wang (see the introductory section and the “Notes by the author” in [40]), and to the best of the authors’ knowledge, there was no complete proof of Lemma 3.4 available in the literature before his paper.


We need the following lemma.

![image 64](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile64.png>)

- Lemma 3.6 ([19, Proposition 8.44]). Suppose λ,µ ∈ C+. Then the following are equivalent:


- (1) µ λ.
- (2) µ ∈ Conv{wλ | w ∈ Wf}, the convex hull of the ﬁnite set Wfλ in E.


By combining the lemmas above, we have the following important result comparing the partial orders ≤ on fW and on ZΦ∨. This will allow us to translate questions involving the Bruhat–Chevalley order on fW into questions involving convex geometry.

Theorem 3.7. Suppose λ,µ ∈ ZΦ∨ ∩ C+. The following are equivalent:

![image 65](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile65.png>)

- (1) tµ ≤ tλ in the Bruhat–Chevalley order.
- (2) tµ ≤a tλ in the aﬃne order.
- (3) µ λ.
- (4) µ ∈ Conv{wλ | w ∈ Wf}.


Proof. (1) ⇔ (2): Since λ,µ are dominant, we have tλ,tµ ∈ fW by Proposition 2.5. Then the equivalence between (1) and (2) follows from Lemma 3.4.

- (2) ⇔ (3): This is a particular case of Lemma 3.3.
- (3) ⇔ (4): This is a particular case of Lemma 3.6.


- Remark 3.8. The equivalences in Theorem 3.7 are not new. Similar statements appear in [26, Sect. 2] and [37, Sect. 0 and Theorem 4.10].


The implication “(1) ⇒ (3)” in Theorem 3.7 is also a particular case of the following proposition, whose proof also uses Lemma 3.4.

- Proposition 3.9. Suppose x ∈ fW ∩ (tλWf) and y ∈ fW ∩ (tµWf). If

y ≤ x, then µ λ.

Proof. Suppose x = tλw and y = tµv where w,v ∈ Wf. If y ≤ x, then by Lemma 3.4, we have y ≤a x. By Corollary 3.2, for any u ∈ Ax, the vector u − yx−1(u) is an R≥0-linear combination of simple coroots. Note that λ ∈ Ax = tλwA+ and µ ∈ Ay = tµvA+. We have

![image 66](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile66.png>)

![image 67](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile67.png>)

![image 68](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile68.png>)

![image 69](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile69.png>)

lim

u∈Ax,u→λ

u − yx−1(u) = λ − yx−1(λ) = λ − tµvw−1t−λ(λ) = λ − µ, and it is an R≥0-linear combination of simple coroots. Therefore, µ λ. See Remark 2.4 for the geometric interpretation of the coset tλWf.

4. Dominant elements

For the rest of the paper, λ ∈ ZΦ∨∩C+ is a ﬁxed dominant coroot lattice point.

![image 70](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile70.png>)

- 4.1. The polytope Pλ and the dominant lower interval f[e,tλ]


As stated in the introduction, we are interested in the sequence (fbtiλ)i. Recall that

fbtiλ = Card x ∈ fW x ≤ tλ,ℓ(x) = i

= Card {x ∈ W | x ≤ tλ,ℓ(x) = i,Ax ⊂ C+} ,

where i ∈ {0,... ,ℓ(tλ)}. The second equality is due to Proposition 2.5. Instead of studying these numbers directly, we ﬁrst study the partner sequence

(bλi )i, given by

bλi :=Card µ ∈ ZΦ∨ ∩ C+ µ λ,(2ρ|µ) = i

![image 71](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile71.png>)

=Card µ ∈ ZΦ∨ ∩ C+ tµ ≤ tλ,ℓ(tµ) = i . The second equality is due to Lemma 2.8 and Theorem 3.7. For later use,

![image 72](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile72.png>)

- we introduce (bλi,+)i, the “strongly dominant” version of (bλi )i, given by


bλi,+ := Card µ ∈ ZΦ∨ ∩ C+ µ λ,(2ρ|µ) = i .

We deﬁne the convex polytope Pλ and its “strongly dominant” counterpart P+λ:

Pλ := Conv{wλ | w ∈ Wf} ∩ C+ ⊂ E, P+λ := Conv{wλ | w ∈ Wf} ∩ C+ ⊂ E, where Conv{wλ | w ∈ Wf} is the convex hull of the ﬁnite set {wλ | w ∈ Wf} in E. Note that Pλ is a bounded closed subset of E, and P+λ = Pλ.

![image 73](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile73.png>)

![image 74](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile74.png>)

We obtain the following proposition from Lemma 3.6 and Theorem 3.7, which motivates the deﬁnition of the polytope Pλ.

- Proposition 4.1. We have the following four equalities:


r

ciα∨i ci ∈ R≥0 ,

Pλ = C+ ∩ λ −

![image 75](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile75.png>)

i=1

r

ciα∨i ci ∈ R≥0 ,

P+λ = C+ ∩ λ −

i=1

Pλ ∩ ZΦ∨ = µ ∈ ZΦ∨ ∩ C+ µ λ , P+λ ∩ ZΦ∨ = µ ∈ ZΦ∨ ∩ C+ µ λ . Proof. If µ ∈ C+, then µ λ if and only if µ ∈ Conv{wλ | w ∈ Wf} by

![image 76](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile76.png>)

![image 77](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile77.png>)

- Lemma 3.6. Therefore, Pλ = Conv{wλ | w ∈ Wf} ∩ C+ = C+ ∩ {µ ∈ E | µ λ}.


![image 78](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile78.png>)

![image 79](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile79.png>)

This proves the ﬁrst equality. The other equalities hold by similar reasons.

- Remark 4.2. By deﬁnition, the number bλi is the cardinality of Pλ ∩ ZΦ∨ ∩ H2ρ,i. In other words, bλi counts the number of lattice points in the slice of Pλ cut by the hyperplane H2ρ,i. On the other hand, since (2ρ|µ) is an even integer for any µ ∈ ZΦ∨, each element in Pλ ∩ ZΦ∨ is counted by bλi for a unique i, and also bλi = 0 whenever i is odd. A similar observation also applies to bλi,+ which counts the points in P+λ ∩ZΦ∨∩H2ρ,i (that is, omitting those points on the walls of C+). Obviously, bλi,+ ≤ bλi .


![image 80](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile80.png>)

- Remark 4.3. For ν ∈ C+ (not necessarily a coroot lattice element), we can also deﬁne the polytope Pν. If ν is strongly dominant, then the face structure of the polytope Pν has a simple description [10]: Pν is combinatorially equivalent to an r-dimensional cube with 2r vertices


ν −

cjα∨j J ⊆ [r] ,

j∈J

where (cj)j∈J = MJ−1 · (αj|λ) j∈J and MJ is the square submatrix of the Cartan matrix M corresponding to the index set J. Thus, the combinatorial type of Pν depends only on the rank r of Φ, and its vertices can be computed explicitly from the Cartan matrix. On the other hand, if ν lies on some of the walls, the structure of the polytope Pν is more complicated and not well explored. However, for the present paper, the fact that Pλ is bounded and convex is suﬃcient.

By deﬁnition of Pλ or by Proposition 4.1, Pkλ is the k-fold dilation of Pλ:

- Corollary 4.4. Pkλ = kPλ := {kx | x ∈ Pλ}, for k ∈ N.


For µ ∈ ZΦ∨, we denote by Wf,µ the parabolic subgroup of Wf generated by {si | 1 ≤ i ≤ r,(µ|αi) = 0}, and by µWf the set of minimal representatives for the right cosets Wf,µ\Wf. Then, Wf,µ is the stabilizer of µ in Wf. In particular, if µ ∈ C+, then Wf,µ is trivial and µWf = Wf.

The following lemma is needed to prove the dominant lattice formula (Theorem 1.4).

- Lemma 4.5. Suppose µ ∈ Pλ ∩ ZΦ∨. Let w = tµwf ∈ tµWf be arbitrary, where wf ∈ Wf. Then, w ∈ fW if and only if wf ∈ µWf. In this case, we have w ≤ tµ ≤ tλ and ℓ(w) = ℓ(tµ) − ℓ(wf).


In particular, if µ ∈ P+λ ∩ ZΦ∨, then we always have w ≤ tµ, w ∈ fW, and ℓ(w) = ℓ(tµ) − ℓ(wf). Proof. We choose ε small enough so that ερ∨ ∈ A+ (see Corollary 2.7). Then

w(ερ∨) = εwf(ρ∨) + µ ∈ Aw. For any i = 1,... ,r, we have

w(ερ∨) αi = ε wf(ρ∨) αi + (µ|αi) = ε ρ∨ wf−1(αi) + (µ|αi).

Let Iµ := {i | 1 ≤ i ≤ r,(µ|αi) = 0}. If i ∈/ Iµ, then (µ|αi) ≥ 1 and (w(ερ∨)|αi) > 0. If otherwise i ∈ Iµ, then (µ|αi) = 0. In this case, (w(ερ∨)|αi) > 0 if and only if wf−1(αi) ∈ Φ+. Therefore, we have the following equivalences:

w ∈ fW ⇐⇒ Aw ⊂ C+ (by Proposition 2.5), ⇐⇒ w(ερ∨) αi > 0, for all i = 1,... ,r, ⇐⇒ w(ερ∨) αi > 0, for all i ∈ Iµ, ⇐⇒ wf−1(αi) ∈ Φ+ for all i ∈ Iµ, ⇐⇒ siwf > wf for all i ∈ Iµ, ⇐⇒ wf ∈ µWf.

This proves the ﬁrst assertion. Next, we show that for any wf ∈ µWf we always have tµwf ≤ tµ. Let wf = si1 ··· sil be a reduced expression for wf, where 1 ≤ i1,... ,il ≤

r. For any k = 1,... ,l, we have

- (4.1) sik−1 ··· si1t−µ1(ερ∨) = sik−1 ··· si1(ερ∨ − µ) ∈ sik−1 ··· si1t−µ1A+, and
- (4.2) sik−1 ··· si1(ερ∨ − µ) αik = ε ρ∨ si1 ··· sik−1(αik) − µ si1 ··· sik−1(αik) .


Note that si1 ··· sik−1(αik) ∈ Φ+ since si1 ··· sik−1sik > si1 ··· sik−1. We write

r

ck,iαi, (ck,i ∈ N).

γk := si1 ··· sik−1(αik) =

i=1

We claim that for any k, there exists j ∈/ Iµ such that ck,j = 0. Otherwise, say, γk = i∈I

ck,iαi. For all i ∈ Iµ we have wf−1αi ∈ Φ+ since wf−1si > wf−1. Thus wf−1(γk) ∈ Φ+. However,

µ

wf−1(γk) = sil ··· si1 · si1 ··· sik−1(αik) = sil ··· sik(αik) ∈ Φ−, which is a contradiction. Therefore, ck,j > 0 for some j ∈/ Iµ.

![image 81](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile81.png>)

Let j be as above (may depend on k). Note that µ ∈ C+. Thus, (µ|γk) ≥ (µ|ck,jαj) ≥ (µ|αj) ≥ 1. By Equation (4.2), we have

sik−1 ··· si1(ερ∨ − µ) αik = ε ρ∨ si1 ··· sik−1(αik) − (µ|γk) < 0.

- By (4.1), this implies that the alcoves sik−1 ··· si1t−µ1A+ and A+ lie in dif-


k,0. Equivalently, A+ and tµsi1 ··· sik−1A+ lie in diﬀerent sides of the aﬃne hyperplane tµsi1 ··· sik−1Hαi

ferent sides of Hαi

k,0. By Lemma 2.1(3), we have

- (4.3) tµsi1 ··· sik−1sik < tµsi1 ··· sik−1 (for all k = 1,... ,l).


Consequently, we have tµwf ≤ tµ as we wanted. Moreover, (4.3) also yields the equation ℓ(tµwf) = ℓ(tµ) − l where l = ℓ(wf). At last, tµ ≤ tλ by Theorem 3.7 and Proposition 4.1. This completes the proof.

We end this subsection with a corollary of the above lemma, which describes the interval f[e,tλ] in terms of the lattice points in Pλ. Corollary 4.6. Let λ ∈ ZΦ∨ ∩ C+. We have

![image 82](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile82.png>)

f[e,tλ] = {tµwf ∈ W | µ ∈ Pλ ∩ ZΦ∨,wf ∈ µWf}.

Proof. Any element w ∈ f[e,tλ] can be uniquely written in the form w = tµwf where µ ∈ ZΦ∨ and wf ∈ Wf. By Proposition 3.9, we have µ

![image 83](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile83.png>)

![image 84](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile84.png>)

λ. Moreover, µ ∈ C+ since Aw ⊂ C+ (by Proposition 2.5) and µ ∈ Aw. Therefore, µ ∈ Pλ ∩ ZΦ∨ by Proposition 4.1. By Lemma 4.5, we have

- wf ∈ µWf. This proves “⊆”. On the other hand, for any µ ∈ Pλ ∩ ZΦ∨ and any wf ∈ µWf, we have


tµwf ≤ tλ and tµwf ∈ fW by Lemma 4.5 again. That is, tµwf ∈ f[e,tλ]. This proves “⊇”.

- 4.2. The dominant lattice formula


We deﬁne the Poincare´ polynomials πtλ(q), πλ(q) and π+λ(q) of the sequences (fbtiλ)i, (bλi )i and (bλi,+)i, respectively, by

fbtiλqi =

πtλ(q) :=

qℓ(w),

w∈f[e,tλ]

0≤i≤ℓ(tλ)

πλ(q) :=

bλi qi =

q(2ρ|µ),

µ∈Pλ∩ZΦ∨

0≤i≤ℓ(tλ)

π+λ(q) :=

bλi,+qi =

q(2ρ|µ).

µ∈P+λ∩ZΦ∨

0≤i≤ℓ(tλ)

The Poincare´ polynomial πf(q) of the ﬁnite Weyl group Wf is deﬁned to be πf(q) :=

qℓ(w) =

bi,fqi,

i

w∈Wf

where

bi,f := Card{w ∈ Wf | ℓ(w) = i}. For µ ∈ ZΦ∨, we also deﬁne the Poincare´ polynomial µπf of the set µWf by

qℓ(w).

µπf(q) :=

w∈µWf

In particular, if µ ∈ ZΦ∨ ∩ C+, then µπf = πf. Obviously πtλ(q), πλ(q), π+λ(q) and µπf(q) belong to N[q].

- Remark 4.7. The polynomials πtλ(q), πf(q), and µπf(q) are indeed the Poincare´ polynomials for the ordinary cohomology of the corresponding spherical Schubert variety, ﬁnite ﬂag variety, and ﬁnite partial ﬂag variety, respectively. However, we are not aware of any topological interpretation of

the polynomials πλ(q) and π+λ(q), and they are not palindromic or unimodal in general.

We are ready to prove the dominant lattice formula (Theorem 1.4): πtλ(q) =

µ∈Pλ∩ZΦ∨

q(2ρ|µ) · µπf(q−1).

Proof of Theorem 1.4. We have πtλ(q) =

w∈f[e,tλ]

qℓ(w) =

µ∈Pλ∩ZΦ∨,wf∈µWf

qℓ(tµwf)

=

µ∈Pλ∩ZΦ∨,wf∈µWf

qℓ(tµ) · q−ℓ(wf)

=

µ∈Pλ∩ZΦ∨

qℓ(tµ) ·

wf∈µWf

q−ℓ(wf)

=

µ∈Pλ∩ZΦ∨

q(2ρ|µ) · µπf(q−1).

The second equality is due to Corollary 4.6, and the third one is due to Lemma 4.5.

For an illustration of the formula in the case Φ of type A2, see Figure 3.

- Remark 4.8. The dominant lattice formula can be proved and understood geometrically. Recall from Sections 1.2.1 and 1.3.2 that the polynomial


πtλ(q) is equal to the Poincare´ polynomial of the singular cohomology of the spherical Schubert variety Grλ. We recall the K-orbit decomposition,

![image 85](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile85.png>)

![image 86](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile86.png>)

Grλ =

Grµ.

![image 87](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile87.png>)

µ∈ZΨ∨∩C+, µ λ

Let Pµ ⊂ G be the parabolic subgroup generated by the root subgroups for simple roots α satisfying (µ|α) = 0. Note that each Grµ has dimension (2ρ|µ) and is an aﬃne space bundle over the ﬁnite partial ﬂag variety G/Pµ [41, Section 2]. In particular, the Poincare´ polynomial of Grµ is the same as the Poincare´ polynomial of G/Pµ, which is given by µπf (q). By Poincare´ duality, µπf (q) is palindromic, so it diﬀers from q(2ρ|µ) · µπf(q−1) only by a power of q. Since the odd cohomology of each Grµ is zero, the long exact sequence of cohomology splits, and this gives the dominance lattice formula. A similar argument can be found in [8, Section 2(iii)].

- 4.3. Truncations


In this subsection, we introduce truncations of Laurent polynomials, which will be used in the proof of Theorem 1.3(1). At the end of this subsection, we prove a useful consequence (Corollary 4.11) of the dominant lattice formula.

For two Laurent polynomials g(q),h(q) ∈ N[q±1], we write g(q) ≤ h(q) if gi ≤ hi for any degree i where gi,hi ∈ N are coeﬃcients of qi in g(q) and h(q), respectively. Moreover, for any integer n ∈ Z, we deﬁne the truncation T≤ng(q) of g(q) to be the Laurent polynomial given by

T≤ng(q) :=

giqi.

i≤n

For a real number z, we write T≤zg(q) to indicate the truncation T≤⌊z⌋g(q), where ⌊z⌋ is the largest integer less than or equal to z. By abuse of notation, we write T≤zg(1) to denote the evaluation of the Laurent polynomial T≤zg(q) at q = 1. We need the following two lemmas.

- Lemma 4.9. Let f(q),g(q),h(q) ∈ N[q±1], we have:

- (1) If g(q) ≤ h(q), then T≤zg(q) ≤ T≤zh(q) for any z ∈ R. Moreover, we have g(1) ≤ h(1) and T≤zg(1) ≤ T≤zh(1).
- (2) If g(q) ≤ h(q), then we have f(q)·g(q) ≤ f(q)·h(q) and f(q)+g(q) ≤ f(q) + h(q).


Proof. Obvious.

- Lemma 4.10. Suppose h(q) = −l≤i≤0 hiqi ∈ N[q−1], where l ≥ 1 is an integer. Then, for any g(q) ∈ N[q±1] and z ∈ R we have


T≤zg(q) · h(q) ≤ T≤z g(q) · h(q) ≤ T≤z+lg(q) · h(q).

![image 88](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile88.png>)

28 GASTON BURRULL, TAO GUI, AND HONGSHENG HU

Figure 3. Description of two of the summands of the dominant lattice formula when W is of aﬃne type A2 and λ = 2α + 3β, where α := α∨1 and β := α∨2 . The yellow points are the lattice points inside Pλ. The dominant Weyl chamber is blue-colored. The alcoves of the interval f[e,tλ] are colored with a darker blue. There are 6 dominant alcoves arranged around the strongly dominant lattice point µ := 2α + 2β, and 3 around the lattice point ν := α + 2β which is on the wall. The summand corresponding to µ in the formula is given by q8 · µπf(q−1) = q5 + 2q6 + 2q7 + q8. The terms of this polynomial are colored orange and placed in the corresponding alcoves in the picture. The summand corresponding to ν is given by q6 · νπf(q−1) = q4 + q5 + q6, whose terms are colored brown.

Proof. We write g(q) = i giqi where each gi ∈ N. Then

g(q) · h(q) =

gihj qk.

k i+j=k

We denote by (gh)k := i+j=k gihj the coeﬃcient of qk in g(q) · h(q). It is clear that the exponents of the q-powers of T≤zg(q) · h(q) concentrate on the interval (−∞,z]. For any integer k ∈ (−∞,z], the coeﬃcient of qk in T≤zg(q) · h(q), say, ak, satisﬁes

gihj ≤

ak =

gihj = (gh)k.

i≤z,i+j=k

i+j=k

This proves the ﬁrst inequality T≤zg(q) · h(q) ≤ T≤z g(q) · h(q) .

On the other hand, for any integer k ∈ (−∞,z], the restrictions i +j = k and −l ≤ j ≤ 0 force i ≤ z + l. Therefore, we have

(gh)k =

gihj =

gihj

i+j=k

i≤z+l,i+j=k

which equals the coeﬃcient of qk (k ≤ z) in T≤z+lg(q) · h(q). While for k > z, the coeﬃcient of qk in T≤z g(q) · h(q) is zero. Thus,

T≤z g(q) · h(q) ≤ T≤z+lg(q) · h(q) which is the second inequality.

Recall that πtλ(q),πλ(q),π+λ (q),µπf(q) are polynomials in N[q]. We regard them as Laurent polynomials in N[q±1]. The following corollary of the dominant lattice formula is crucial in the proof of Theorem 1.3.

Corollary 4.11. π+λ(q) · πf(q−1) ≤ πtλ(q) ≤ πλ(q) · πf(q−1). Proof. By deﬁnition, whatever µ is, we always have µπf(q−1) ≤ πf(q−1). Therefore,

πtλ(q) =

q(2ρ|µ) · µπf(q−1)

µ∈Pλ∩ZΦ∨

q(2ρ|µ) · πf(q−1) = πλ(q) · πf(q−1),

≤

µ∈Pλ∩ZΦ∨

where the ﬁrst equality is the dominant lattice formula, and the inequality follows from Lemma 4.9(2).

On the other hand, µπf(q−1) = πf(q−1) if µ ∈ ZΦ∨ ∩ C+. Thus, π+λ(q) · πf(q−1) =

q(2ρ|µ) · πf(q−1)

µ∈P+λ∩ZΦ∨

q(2ρ|µ) · µπf(q−1)

=

µ∈P+λ∩ZΦ∨

q(2ρ|µ) · µπf(q−1)

≤

µ∈Pλ∩ZΦ∨

= πtλ(q). This completes the proof.

5. The weak convergence of (m1,m2,...)

Let λ ∈ ZΦ∨ ∩ C+ be a ﬁxed dominant coroot lattice point as before. Recall that Volr denotes the Lebesgue measure on E induced by the inner product (−,−). Let ht: Pλ → R (“ht” for “height”) be the linear map ht(x) := (2ρ|x). The push-forward measure ht∗Volr is deﬁned as follows, for any Borel set U ⊆ R,

![image 89](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile89.png>)

(ht∗Volr)(U) := Volr(ht−1 U) = Volr x ∈ Pλ (2ρ|x) ∈ U . Note that by Proposition 4.1 we have 0 ≤ ht(x) ≤ (2ρ|λ) = ℓ(tλ) for any

- x ∈ Pλ. Therefore, ht∗Volr is supported on [0,ℓ(tλ)]. Moreover, for any


- z ∈ R we have ht−1(z) = Pλ ∩ H2ρ,z. Therefore, we also have


- 1

![image 90](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile90.png>)

- 2ρ


Volr−1(ht−1(z))dz.

(ht∗Volr)(U) =

U

Here the integral is the Lebesgue integral, 2ρ denotes the length of 2ρ, and Volr−1 is the Lebesgue measure on the hyperplanes H2ρ,z induced by the inner product (−|−). The coeﬃcient 1/ 2ρ appears in the integral because, any line segment L perpendicular to H2ρ,z is mapped by ht to an interval of length 2ρ ·  L . In other words, the density function of the measure ht∗Volr is

- 1

![image 91](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile91.png>)

- 2ρ


Volr−1(ht−1(z)).

g(z) =

For any real number z ∈ R, let δz be the Dirac measure at z, that is, for any Borel set U ⊂ R, δz(U) = 1 if z ∈ U, and δz(U) = 0 if z ∈/ U. For each positive integer k, we deﬁne a measure mk on R as follows,

ℓ(tkλ)

1 kr

fbtikλδ i

.

mk :=

![image 92](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile92.png>)

![image 93](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile93.png>)

k

i=0

Note that ℓ(tkλ) = kℓ(tλ) by Corollary 2.9.

- 5.1. Weak convergence of “companion” measures


We deﬁne two “companions” of mk, denoted by mlatk and mlatk,+ (“lat” for “lattice”), respectively, by

ℓ(tkλ)

ℓ(tkλ)

mlatk := |Wf|

, mlatk,+ := |Wf|

bkλi δ i

bkλi,+δ i

.

![image 94](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile94.png>)

![image 95](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile95.png>)

kr

kr

![image 96](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile96.png>)

![image 97](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile97.png>)

k

k

i=0

i=0

Recall Lemma 2.16 that |Wf| = Volr(D)/Volr(A+) where D is the open parallelotope spanned by the simple coroots.

- Remark 5.1. In the deﬁnition of mlatk , intuitively, we consider the k-fold dilation of the polytope Pλ, and count the ZΦ∨-lattice points3 in Pkλ∩H2ρ,i.


![image 98](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile98.png>)

3This procedure is in a similar ﬂavor as the theory of Ehrhart polynomial for lattice polytope [14], although Pλ is not a lattice polytope in general.

Then we scale back and put the number bkλi obtained as the mass at the point ki ∈ R. This is equivalent to count the k1ZΦ∨-lattice points in the slice Pλ ∩ H2ρ,i

![image 99](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile99.png>)

![image 100](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile100.png>)

, that is,

![image 101](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile101.png>)

k

- (5.1) bkλi = Card Pλ ∩ (

1 k

![image 102](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile102.png>)

ZΦ∨) ∩ H2ρ,i

![image 103](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile103.png>)

k

.

In addition, as mentioned in Remark 4.2, each element in Pλ ∩ k 1ZΦ∨ contributes to the measure mlatk once and only once. Similar observations also apply to mlatk,+.

![image 104](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile104.png>)

The scalar |Wf|/kr in the deﬁnition is for normalization, since there are |Wf| many alcoves “around” a lattice point (see Remark 2.4).

Clearly, all the measures ht∗Volr, mk, mlatk and mlatk,+ are non-negative, bounded, and supported on [0,ℓ(tλ)]. We have the following: Proposition 5.2.

- (1) The sequence of measures (mlatk )k converges weakly to Vol 1

![image 105](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile105.png>)

r(A+)ht∗Volr.

- (2) The sequence of measures (mlatk,+)k converges weakly to Vol 1


![image 106](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile106.png>)

r(A+)ht∗Volr. Proof. To prove the ﬁrst statement, by Lemma 2.14, it suﬃces to show that for any z ∈ [0,ℓ(tλ)], we have

- (5.2) lim

k→∞

mlatk ([0,z]) =

1 Volr(A+)

![image 107](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile107.png>)

ht∗Volr([0,z]).

We denote by P[0λ,z] := x ∈ Pλ 0 ≤ (2ρ|x) ≤ z the truncation of Pλ. Then

- (5.3) (ht∗Volr) ([0,z]) = Volr P[0λ,z] . On the other hand, we have (see Remark 5.1)


kℓ(tλ)

bkλi = Card P[0λ,z] ∩

bkλi δ i

([0,z]) =

![image 108](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile108.png>)

k

i=0

i∈N,0≤i≤kz

1 k

ZΦ∨ ,

![image 109](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile109.png>)

namely, the number of lattice points of k1ZΦ∨ in the truncation P[0λ,z]. Therefore,

![image 110](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile110.png>)

mlatk ([0,z]) = |Wf|

Card P[0λ,z] ∩

![image 111](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile111.png>)

kr

D k

1 Volr(A+)

Volr

=

![image 112](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile112.png>)

![image 113](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile113.png>)

1 k

ZΦ∨

![image 114](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile114.png>)

Card P[0λ,z] ∩

1 k

ZΦ∨

![image 115](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile115.png>)

is a Riemann sum, and the limit limk mlatk ([0,z]) is the Riemann integral

1 Volr(A+)

1 Volr(A+)

Volr P[0λ,z] . By Equation (5.3), we see that Equation (5.2) is valid.

=

![image 116](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile116.png>)

![image 117](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile117.png>)

P[0λ,z]

The proof of the second statement is similar. We have the Riemann sum

mlatk,+([0,z]) = |Wf|

1 k

ZΦ∨ , where

Card P+λ,[0,z] ∩

![image 118](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile118.png>)

![image 119](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile119.png>)

kr

P+λ,[0,z] := x ∈ P+λ 0 ≤ (2ρ|x) ≤ z .

But Volr(P[0λ,z]) = Volr(P+λ,[0,z]). So the analog of Equation (5.2) also holds for mlatk,+.

- Remark 5.3. The sequences (mlatk )k and (mlatk,+)k do not converge strongly (see Remark 2.15) to the limit measure. For example, Q = Q ∩ [0,ℓ(tλ)] is a Borel set and its inverse image ht−1(Q) consists of a countable union of (r − 1)-dimensional slices, so (ht∗Volr)(Q) = 0. However, limk mlatk (Q) =


Volr(Pλ)/Volr(A+) > 0, this is because any point mass of any mlatk is supported on Q.

- 5.2. Proof of Theorem 1.3(1)


Recall the theorem states that the sequence of measures (mk)k converges weakly to the measure Vol 1

r(A+)ht∗Volr. Proof. As in the proof of Proposition 5.2, it suﬃces to show that

![image 120](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile120.png>)

- (5.4)

for any z ∈ [0,ℓ(tλ)], we have lim

k→∞

mk([0,z]) =

1 Volr(A+)

![image 121](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile121.png>)

ht∗Volr([0,z]). For any k = 1,2,... , we have

- (5.5)

mk([0,z]) =

1 kr

![image 122](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile122.png>)

ℓ(tkλ)

i=0

fbtikλδ i

![image 123](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile123.png>)

k

([0,z])

=

1 kr i∈N,0≤i≤kz

![image 124](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile124.png>)

fbtikλ

=

1 kr

![image 125](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile125.png>)

T≤kzπtkλ(1),

where T≤kz is the truncation and πtkλ is the Poincare´ polynomial from Section 4.

By Corollary 4.11 and Lemma 4.9(1), we have

- (5.6) T≤kz π+kλ(q) · πf(q−1) ≤ T≤kzπtkλ(q) ≤ T≤kz πkλ(q) · πf(q−1) .

Let l := |Φ+| be the length of the longest element in Wf. Then the exponents of q-powers in the Laurent polynomial πf(q−1) concentrate on the interval [−l,0]. Therefore, Lemma 4.10 applies to the ﬁrst and third terms of (5.6). We have

- (5.7) T≤kzπ+kλ(q) · πf(q−1) ≤ T≤kz π+kλ(q) · πf(q−1) ≤ T≤kzπtkλ(q),


- where the ﬁrst inequality is obtained by applying Lemma 4.10 to the ﬁrst term of (5.6), and the second one is exactly the ﬁrst inequality of (5.6). Evaluating the ﬁrst and the third term of (5.7) at q = 1, we obtain
- (5.8) |Wf| · T≤kzπ+kλ(1) ≤ T≤kzπtkλ(1). By Equation (5.5), the right hand side of (5.8) equals krmk([0,z]). Therefore, by the deﬁnitions of mlatk,+ and π+kλ(q), we have
- (5.9) mlatk,+([0,z]) = |Wf| kr i∈N,0≤i≤kz

![image 126](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile126.png>)

bkλi,+ = |Wf|

![image 127](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile127.png>)

kr · T≤kzπ+kλ(1) ≤ mk([0,z]).

On the other hand, applying Lemma 4.10 to the third term of (5.6), we also have

- (5.10) T≤kzπtkλ(q) ≤ T≤kz πkλ(q) · πf(q−1) ≤ T≤kz+lπkλ(q) ·πf(q−1),

where the ﬁrst inequality comes from (5.6). Evaluating the ﬁrst and the third term of (5.10) at q = 1 yields

T≤kzπtkλ(1) ≤ |Wf| · T≤kz+lπkλ(1). Therefore, by Equation (5.5) and the deﬁnitions of πkλ(q) and mlatk , we have

- (5.11)

mk([0,z]) ≤

|Wf| kr · T≤kz+lπkλ(1)

![image 128](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile128.png>)

= |Wf| kr 0≤i≤kz+l

![image 129](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile129.png>)

bkλi

= mlatk [0,z +

l k

![image 130](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile130.png>)

]

= mlatk ([0,z]) + mlatk (z,z +

l k

![image 131](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile131.png>)

] . The inequalities (5.9) and (5.11) tell us

- (5.12) mlatk,+([0,z]) ≤ mk([0,z]) ≤ mlatk ([0,z]) + mlatk (z,z +

l k

![image 132](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile132.png>)

] . By the proof of Proposition 5.2, we have

- (5.13) lim

k→∞

mlatk,+([0,z]) = lim

k→∞

mlatk ([0,z]) =

1 Volr(A+)

![image 133](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile133.png>)

ht∗Volr([0,z]).

So it remains to show that the “error term” mlatk (z,z + kl ] tends to zero. For any δ ∈ R>0, we have kl < δ for k large enough. Thus,

![image 134](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile134.png>)

![image 135](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile135.png>)

lim

k→∞

mlatk (z,z +

l k

![image 136](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile136.png>)

] ≤ lim

k→∞

mlatk (z,z + δ] =

1 Volr(A+)

![image 137](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile137.png>)

Volr(P[λz,z+δ]).

But δ ∈ R>0 can be taken to be arbitrarily small, and Pλ is a bounded polytope. Therefore Volr(P[λz,z+δ]) can be arbitrarily small. This proves

- (5.14) lim


l k

mlatk (z,z +

] = 0.

![image 138](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile138.png>)

k→∞

- By (5.12), (5.13), and (5.14), we obtain (5.4), as desired.

6. The uniform convergence of (S1,S2,...)

Let λ ∈ ZΦ∨ ∩ C+ be a ﬁxed dominant coroot lattice point as before. For any positive integer k, we deﬁne the step function Sk : [0,ℓ(tλ)] → R

![image 139](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile139.png>)

as follows. For any z ∈ [0,ℓ(tλ)], there exists a unique i ∈ {0,1,... ,kℓ(tλ)} such that z ∈ [ki , i+1k ). We deﬁne

![image 140](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile140.png>)

![image 141](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile141.png>)

Sk(z) :=

1 kr−1

![image 142](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile142.png>)

fbtikλ.

Remark 6.1. The function Sk(z) can be interpreted as an approximation of the density function (which in this case does not exist) of the discrete

measure mk in the following sense: for any z ∈ [0,ℓ(tλ)], there exists a unique i ∈ {0,1,... ,kℓ(tλ)} such that z ∈ [ki , i+1k ), and we have

![image 143](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile143.png>)

![image 144](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile144.png>)

- (6.1) mk([0,z]) =

1 kr 0≤j≤i

![image 145](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile145.png>)

fbtjkλ =

i+1 k

![image 146](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile146.png>)

0

Sk(x)dx.

Let us recall the statement of Theorem 1.3(2): The sequence of step functions (Sk(z))k converges uniformly to the function

z  →

1 Volr(A+) · 2ρ

![image 147](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile147.png>)

Volr−1(ht−1(z)). Theorem 1.3(2) has the following corollary:

Corollary 6.2. For every 0 ≤ i ≤ ℓ(tλ), we have lim

k→∞

1 kr−1

![image 148](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile148.png>)

fbtkikλ =

1 Volr(A+) · 2ρ

![image 149](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile149.png>)

Volr−1(ht−1(i)).

Proof. This is because limk Sk(i) = g(i)/Volr(A+) by Theorem 1.3(2).

The proof of Theorem 1.3(2), which occupies Sections 6.2 to 6.4, is more technical than that of Theorem 1.3(1). Therefore, before the full proof, we outline the main ideas.

6.1. Outline of the proof of Theorem 1.3(2) To prove the uniform convergence, we need to estimate the value fbtikλ/kr−1

of the step function Sk at z ∈ [ki , i+1k ). Using Corollary 4.11, we switch this estimation to the estimation of the numbers

![image 150](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile150.png>)

![image 151](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile151.png>)

- (6.2) bkλi+j = Card Pλ ∩




1 k

ZΦ∨ ∩ H2ρ,i+j

![image 152](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile152.png>)

![image 153](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile153.png>)

k

and their companions bkλi+j,+, where 0 ≤ j ≤ |Φ+| (see Inequality (6.11)). Note that bkλi+j = 0 only if i + j is even, and in this case (k1ZΦ∨) ∩ H2ρ,i+j

is a lattice of rank (r − 1) in the aﬃne hyperplane H2ρ,i+j

![image 154](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile154.png>)

![image 155](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile155.png>)

k

.

![image 156](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile156.png>)

k

We choose a fundamental domain Bk of the lattice (k1ZΦ∨) ∩ H2ρ,0 containing the origin. If we join all the translations of Bk by points in Pλ ∩ (k1ZΦ∨) ∩ H2ρ,i+j

![image 157](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile157.png>)

, we obtain the region

![image 158](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile158.png>)

![image 159](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile159.png>)

k

1 k

ZΦ∨ ∩ H2ρ,i+j

R = Rk,i,j := p + Bk p ∈ Pλ ∩

⊂ H2ρ,i+j

.

![image 160](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile160.png>)

![image 161](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile161.png>)

![image 162](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile162.png>)

k

k

Since we can compute the volume of Bk directly from Φ, estimating the value of (6.2) is equivalent to estimating Volr−1(R). The proof of the convergence is then achieved by comparing Volr−1(R) with Volr−1(Pλ ∩ H2ρ,z). This, as well as the uniformity, requires carefully estimating the volume of some open neighborhood of the boundary of Pλ ∩ H2ρ,z (see Figures 4 and 6 for an example of such a neighborhood). When k is large enough, for any z, the boundary of R is “contained” in such a neighborhood. Because the volume of such a neighborhood can be suﬃciently small, Volr−1(R) can be suﬃciently close to Volr−1(Pλ∩H2ρ,z). This leads to the proof of the uniform convergence.

- 6.2. Volume estimations


Only in this subsection, let E = Rn be an arbitrary Euclidean space of dimension n with inner product (−|−): E × E → R. In the proof of Theorem 1.3(2), we will use the results in this subsection mainly in the case n = r − 1.

For two points x,y ∈ E, we denote by d(x,y) the distance between x and

![image 163](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile163.png>)

- y, that is, d(x,y) = (x − y|x − y). For a nonempty subset Y ⊂ E the distance between x and Y is deﬁned by


d(x,y) and the diameter of Y is deﬁned by

d(x,Y ) := inf

y∈Y

d(y,y′).

diam(Y ) := sup

y,y′∈Y

For an n-dimensional polytope P with n > 0, its boundary ∂P is the union of all its faces of dimension strictly less than n. Both P and ∂P are bounded closed sets. For any real number δ > 0, we deﬁne

P+δ := {x ∈ E | d(x,P) < δ}, P−δ := {x ∈ P | d(x,∂P) > δ}.

For example, in Figure 4, P is the solid triangle in a Euclidean plane, P+δ is the interior of the dotted area, and P−δ is the interior of the dashed triangle.

![image 164](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile164.png>)

![image 165](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile165.png>)

A moment’s thought shows that the diﬀerence set P+δ \ P−δ, where P−δ is the closure of P−δ, is the open neighbourhood

N(∂P,δ) := {x ∈ E | d(x,∂P) < δ}

of ∂P. We want to estimate its volume, Voln(N(∂P,δ)). Before this, we need to introduce some notations.

|δ| |
|---|---|
|δ| |


Figure 4. A triangle P and the P+δ, P−δ.

Suppose F◦ is an open face of P and dimF◦ ≤ n−1. Then F◦ ⊆ ∂P. Let x ∈ F◦ be an arbitrary point, and Hx⊥ be the aﬃne subspace transversal to

F◦ aﬀ at x, that is, the (n − dimF◦)-dimensional aﬃne subspace passing through x and perpendicular to F◦ aﬀ. We denote by

Bx,δ⊥ := {y ∈ Hx⊥ | d(x,y) < δ} the open ball in Hx⊥ with center x and radius δ, and by CF◦,δ :=

Bx,δ⊥

x∈F◦

the disjoint union of the balls. Geometrically, CF◦,δ is isometric to the product of F◦ and an (n−dimF◦)-ball of radius δ, which looks like a “cylinder”.

For instance, in the case n = 3, Figure 5 illustrates examples of CF◦,δ, where F◦ is an open triangle, an open segment, and a point, respectively.

δ δ

δ

δ

Figure 5. Examples of CF◦,δ in a 3-dimensional Euclidean space.

We can compute the volume of CF◦,δ.

- Lemma 6.3. Let Bδk be a k-dimensional ball of radius δ. Then for an i-dimensional open face F◦ of an n-dimensional polytope P, we have


Voln(CF◦,δ) = Voli(F◦) × Voln−i(Bδn−i) = Voli(F◦) × cn−iδn−i, where cn−i = πn−2 i/Γ(n−2 i + 1) and Γ is the Euler’s Gamma function. Proof. Clear since Volk(Bδk) = ckδk.

![image 166](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile166.png>)

![image 167](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile167.png>)

Note that cn−i is a constant that only depends on dimF◦ = i, not on the shape or the volume of F◦.

- Lemma 6.4. Let Fi be the set of i-dimensional open faces of an n-dimensional polytope P with n > 0. Then, for any δ > 0,


N(∂P,δ) =

CF◦,δ.

0≤i≤n−1 F◦∈Fi

Proof. Suppose y ∈ CF◦,δ for some open face F◦ of dimension strictly less than n. Then y ∈ Bx,δ⊥ for some x ∈ F◦. Thus d(y,∂P) < δ and y ∈ N(∂P,δ). This proves “⊇”.

Conversely, suppose y ∈ E satisﬁes d(y,∂P) < δ. We can assume y ∈/ ∂P. Since ∂P is a bounded closed subset and hence a compact subset in E, there exists x ∈ ∂P (hence x = y) such that d(y,x) = d(y,∂P). Suppose F◦ is the open face containing x. We claim that the aﬃne line  {x,y} aﬀ is perpendicular to the aﬃne subspace F◦ aﬀ. Otherwise, since F◦ is open in F◦ aﬀ, we can ﬁnd some x′ ∈ F◦ such that d(y,x′) < d(y,x), which contradicts d(y,x) = d(y,∂P). In particular, our claim implies y ∈ Bx,δ⊥ ⊆ CF◦,δ. This proves “⊆”.

For the example in Figure 4, the set N(∂P,δ) for a small δ is a union of three disks and three rectangles, see the gray area in Figure 6.

| |
|---|
| |


Figure 6. The set N(∂P,δ) equals the union of the dotted areas.

As a consequence, we have the following estimate of Voln(N(∂P,δ)).

- Proposition 6.5. Let ck and Fi be as in Lemmas 6.3 and 6.4. Then


Voli(F◦) cn−iδn−i.

Voln(N(∂P,δ)) ≤

0≤i≤n−1 F◦∈Fi

Proof. Follows immediately from Lemmas 6.3 and 6.4. Now, suppose {e1,... ,en} is a basis of E. Then, for any k ∈ Z>0, Lk :=

mn k

m1 k

en m1,... ,mn ∈ Z

e1 + ··· +

![image 168](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile168.png>)

![image 169](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile169.png>)

is a lattice in E. Only in this subsection, we deﬁne

B := {c1e1 + ··· + cnen ∈ E | c1,... ,cn ∈ [0,1)} and

cn k

c1 k

1 k

en c1,... ,cn ∈ [0,1)

e1 + ··· +

B =

Bk :=

![image 170](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile170.png>)

![image 171](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile171.png>)

![image 172](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile172.png>)

for any k ∈ Z>0. In subsequent subsections, we will use the notations B and Bk for the case n = r − 1 and ei = α∨i+1 − α∨1 . Note that for any k, Bk is a fundamental domain of the translation action of Lk on E, and we have

1 k

diam(Bk) =

diam(B). We have the following lemma.

![image 173](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile173.png>)

- Lemma 6.6. Let {e1,... ,en} be a basis of E, and notations Lk and Bk be as above. Then, for any positive δ > 0, any integer k > diam(B)/δ, any n-dimensional polytope P in E, and any set of lattice points Z satisfying (P \ ∂P) ∩ Lk ⊆ Z ⊆ P ∩ Lk, we have


P−δ ⊆

(x + Bk) ⊆ P+δ.

x∈Z

Proof. Let integer k > diam(B)/δ be arbitrary. Then diam(Bk) < δ. Suppose x ∈ P ∩ Lk. Then for any y ∈ x + Bk, we have

d(y,P) ≤ d(y,x) ≤ diam(Bk) < δ. Therefore, y ∈ P+δ. Since x ∈ P ∩Lk and y ∈ x+Bk are arbitrary, we have

(x + Bk) ⊆ P+δ.

x∈P∩Lk

On the other hand, suppose y ∈ P−δ (if P−δ = ∅). Then there exists

a unique x ∈ Lk such that y ∈ x + Bk, since {x + Bk | x ∈ Lk} forms a partition of the ambient space E. Then

- (6.3) d(y,x) ≤ diam(Bk) < δ. Next, we prove x ∈ P \ ∂P by contradiction. Suppose x ∈/ P. Then


d(y,x) > d(y,∂P) > δ, since y ∈ P−δ ⊆ P \∂P (the interior of P). But this contradicts (6.3). Thus,

- x ∈ P. If x ∈ ∂P, then we have d(y,x) ≥ d(y,∂P) > δ,


which is also a contradiction. Therefore, x ∈ P \∂P. Since y ∈ P−δ is taken arbitrarily, we have

P−δ ⊆

(x + Bk).

x∈(P\∂P)∩Lk

At last, we have the chain of containment relations P−δ ⊆

(x + Bk) ⊆

(x + Bk) ⊆

x∈Z

x∈P∩Lk

x∈(P\∂P)∩Lk

(x + Bk) ⊆ P+δ,

because (P \ ∂P) ∩ Lk ⊆ Z ⊆ P ∩ Lk. The proof is complete.

- 6.3. Proof of Theorem 1.3(2)


Return to the setting of Theorem 1.3(2). Note that in the case r = 1, that

is, W is of aﬃne type A1, Theorem 1.3(2) holds trivially since Sk(z) ≡ 1. Therefore, we assume r ≥ 2.

For z ∈ [0,ℓ(tλ)], we deﬁne Pzλ := ht−1(z) = Pλ ∩ H2ρ,z.

Then Pzλ is a polytope in the (r − 1)-dimensional Euclidean space H2ρ,z (see Lemma 2.17(1)). Moreover, since Pλ is convex of dimension r, we have

dimPzλ = r−1 except for the two extremal cases z = 0 and z = ℓ(tλ), where P0λ and Pℓλ(t

λ) are both single points. As in Section 6.2, we deﬁne

Pzλ,+δ := {x ∈ H2ρ,z | d(x,Pzλ) < δ}, Pzλ,−δ := {x ∈ Pzλ | d(x,∂Pzλ) > δ}. Then the set Pzλ,+δ \ Pzλ,−δ is the open neighbourhood

![image 174](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile174.png>)

N(∂Pzλ,δ) := {x ∈ H2ρ,z | d(x,∂Pzλ) < δ}

of ∂Pzλ in H2ρ,z. Remember that N(∂Pzλ,δ) is an open subset in the (r−1)dimensional space H2ρ,z.

- Lemma 6.7. For any real number ε > 0, there exists δ > 0 small enough such that for any z ∈ [0,ℓ(tλ)], we have


Volr−1(N(∂Pzλ,δ)) < ε. In particular, since Pzλ,−δ ⊆ Pzλ ⊆ Pzλ,+δ, we have

Volr−1(Pzλ,+δ) − Volr−1(Pzλ) < ε, Volr−1(Pzλ) − Volr−1(Pzλ,−δ) < ε.

Proof. For each i = 0,1,... ,r − 2, let Fz,i be the set of i-dimensional open faces of Pzλ, and Fλ be the set of all open faces of Pλ. By Lemma 2.17, each open face of Pzλ is an intersection of some open face in Fλ with H2ρ,z. Therefore, it holds that

|Fz,i| ≤ |Fλ|, for any z ∈ [0,ℓ(tλ)].

0≤i≤r−2

Moreover, since Pλ is a bounded area, there exists a uniform bound M ∈ R+ (independent of z) such that

Voli(F◦) ≤ M for any z and any F◦ ∈ Fz,i.

Then by Proposition 6.5, for any z ∈ [0,ℓ(tλ)], Volr−1(N(∂Pzλ,δ)) ≤

Voli(F◦) cr−1−iδr−1−i

0≤i≤r−2 F◦∈Fz,i

≤ M|Fλ|

cr−1−iδr−1−i

0≤i≤r−2

= M|Fλ|(c1δ + c2δ2 + ··· + cr−1δr−1),

where c1,... ,cr−1 are constants independent of z (see Lemma 6.3). The existence of the desired δ is now clear.

- Lemma 6.8. For any real number ε > 0, there exists δ > 0 small enough such that for any z,z′ ∈ [0,ℓ(tλ)] with |z − z′| < δ, we have


|Volr−1(Pzλ) − Volr−1(Pzλ′)| < ε.

Proof. This is because the function z  → Volr−1(Pzλ) is a continuous function on [0,ℓ(tλ)], and hence uniformly continuous.

Recall that {α∨1 ,... ,α∨r } is a basis of E, and

- (6.4) {α∨i − α∨1 | i = 2,... ,r}

is a basis of H2ρ,0, as well as a basis for the lattice ZΦ∨∩H2ρ,0. For arbitrary z ∈ R, if we choose and ﬁx an origin o ∈ H2ρ,z for the Euclidean space H2ρ,z, then the set of vectors in (6.4) is also a basis for H2ρ,z. If moreover z ∈ 2Z and o is taken from ZΦ∨ ∩ H2ρ,z, then (6.4) is also a basis for the lattice

ZΦ∨ ∩ H2ρ,z =

 



o +

1≤i≤r

niα∨i

1≤i≤r

ni = 0

 



.

We deﬁne

- (6.5) B :=


 

 

ci(α∨i − α∨1 ) c2,... ,cr ∈ [0,1)

 2≤i≤r

 to be the parallelotope in H2ρ,0, and

 

 

ci k

1 k

(α∨i − α∨1 ) c2,... ,cr ∈ [0,1)

B =

Bk :=

![image 175](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile175.png>)

![image 176](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile176.png>)

 2≤i≤r

 for any k ∈ N>0. Then

1 kr−1

Volr−1(B).

Volr−1(Bk) =

![image 177](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile177.png>)

Remark 6.9. There are many possible choices of basis for the lattice ZΦ∨ ∩ H2ρ,0. For example, {α∨i − α∨i+1 | i = 1,... ,r − 1} is another choice. Although the shape and the diameter of the corresponding parallelotope B both depend on the chosen basis, the volume Volr−1(B) is independent of this choice.

- As observed in Remark 4.2, the numbers bkλi and bkλi,+ are zero if i is odd.


On the other hand, for i even, we have the following estimation:

- Lemma 6.10. For any δ > 0, any integer k > diam(B)/δ, and any i ∈ 2Z, we have


Volr−1(Pλ,i −δ

) ≤ bkλi,+ · Volr−1(Bk) ≤ bkλi · Volr−1(Bk) ≤ Volr−1(Pλ,i +δ

). Proof. Let i ∈ 2Z be arbitrary. Recall that

![image 178](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile178.png>)

![image 179](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile179.png>)

k

k

bkλi = Card(Pkλ ∩ ZΦ∨ ∩ H2ρ,i)

1 k

ZΦ∨ ∩ H2ρ, i

= Card(Pλ ∩

)

![image 180](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile180.png>)

![image 181](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile181.png>)

k

= Card(Pλi

∩ Li,k), where Li,k := (k1ZΦ∨) ∩ H2ρ,i

![image 182](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile182.png>)

k

. Let o ∈ Li,k be arbitrary. Then

![image 183](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile183.png>)

![image 184](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile184.png>)

k

 

 

nj k

(α∨j − α∨1 ) n2,... ,nr ∈ Z

Li,k =

o +

![image 185](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile185.png>)





2≤j≤r

. Moreover, o + Bk is a fundamental domain for the translation action of Li,k on H2ρ,i

is a lattice in the hyperplane H2ρ,i

![image 186](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile186.png>)

k

. Let integer k > diam(B)/δ be arbitrary. Then, by Lemma 6.6, we have

![image 187](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile187.png>)

k

(x + Bk) ⊆ Pλ,i +δ

.

![image 188](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile188.png>)

k

x∈Pλi k

∩Li,k

![image 189](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile189.png>)

Therefore,

bkλi · Volr−1(Bk) ≤ Volr−1(Pλ,i +δ

). Similarly,

![image 190](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile190.png>)

k

1 k

bkλi,+ = Card(P+λ ∩

) = Card(P+λ ∩ Li,k). Notice that

ZΦ∨ ∩ H2ρ,i

![image 191](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile191.png>)

![image 192](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile192.png>)

k

Pλi

\ ∂Pλi

⊆ P+λ ∩ H2ρ,i

⊆ Pλi

. By Lemma 6.6 again,

![image 193](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile193.png>)

![image 194](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile194.png>)

![image 195](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile195.png>)

![image 196](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile196.png>)

k

k

k

k

Pλ,i −δ

![image 197](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile197.png>)

k

⊆

(x + Bk),

x∈P+λ∩Li,k

and hence

Volr−1(Pλ,i −δ

) ≤ bkλi,+ · Volr−1(Bk). This completes the proof.

![image 198](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile198.png>)

k

Recall that

bj,f = Card{w ∈ Wf | ℓ(w) = j} is the coeﬃcient of qj in πf(q). The following lemma is classical:

- Lemma 6.11.


bj,f = |Wf| 2

.

bj,f =

![image 199](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile199.png>)

0≤j≤|Φ+| j∈2Z

0≤j≤|Φ+| j∈2Z+1

The following proposition states that the sequence of step functions (Sk(z))k converges uniformly to the continuous function

|Wf| 2Volr−1(B)

Volr−1(Pzλ),

z  →

![image 200](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile200.png>)

where B is as in Equation (6.5). Proposition 6.12. For any ε > 0, there exists a positive integer K, such that for any integer k > K and any z ∈ [0,ℓ(tλ)], we have

|Sk(z) − cVolr−1(Pzλ)| < ε, where

c = |Wf| 2Volr−1(B)

![image 201](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile201.png>)

is a constant. Proof. Let ε > 0 be arbitrary, and ε′ := Vol|rW−1(B)

f| ε. By Lemma 6.7, there exists δ > 0 small enough such that

![image 202](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile202.png>)

- (6.6) Volr−1(Pzλ,+δ) < Volr−1(Pzλ) + ε′ for any z ∈ [0,ℓ(tλ)], and
- (6.7) Volr−1(Pzλ,−δ) > Volr−1(Pzλ) − ε′ for any z ∈ [0,ℓ(tλ)]. For such δ, by Lemma 6.10, there exists a positive integer K such that
- (6.8) bkλi Volr−1(Bk) ≤ Volr−1(Pλ,i +δ

![image 203](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile203.png>)

k

) for any k > K and any i ∈ 2Z, and

- (6.9) bkλi,+ Volr−1(Bk) ≥ Volr−1(Pλ,i −δ

![image 204](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile204.png>)

k

) for any k > K and any i ∈ 2Z.

Moreover, by Lemma 6.8, there exists δ′ > 0 such that for any z,z′ ∈ [0,ℓ(tλ)] with |z −z′| < δ′, we have |Volr−1(Pzλ)−Volr−1(Pzλ′)| < ε′. We can choose the integer K large enough such that |Φ

+|

![image 205](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile205.png>)

K < δ′. Then we have

- (6.10)

|Volr−1(Pzλ) − Volr−1(Piλ+j

![image 206](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile206.png>)

k

)| < ε′ for any k > K, i,j ∈ Z with z ∈ [ki , i+1k ) and 0 ≤ j ≤ |Φ+|. Now, let δ, K be as above, and k > K, z ∈ [0,ℓ(tλ)] be arbitrary. There

![image 207](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile207.png>)

![image 208](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile208.png>)

exists a unique i ∈ {0,1,... ,kℓ(tλ)} such that z ∈ [ki , i+1k ). Consider the coeﬃcient of qi in Corollary 4.11, we have the inequalities

![image 209](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile209.png>)

![image 210](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile210.png>)

- (6.11)


bj,fbkλi+j,+ ≤ fbtikλ ≤

bj,fbkλi+j.

0≤j≤|Φ+|

0≤j≤|Φ+|

Here the numbers bkλi+j,+ and bkλi+j are regarded as zero if i+j > ℓ(tkλ). Notice that bkλi+j = 0 whenever i + j is odd. We have the following inequalities:

fbtikλ Volr−1(Bk) (by Inequality (6.11)) ≤

bj,fbkλi+j Volr−1(Bk)

0≤j≤|Φ+|

bj,fbkλi+j Volr−1(Bk)

=

0≤j≤|Φ+| i+j∈2Z

bj,f Volr−1(Piλ,++j δ

(by Inequality (6.8)) ≤

)

![image 211](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile211.png>)

k

0≤j≤|Φ+| i+j∈2Z

) + ε′

bj,f Volr−1(Piλ+j

(by Inequality (6.6)) <

![image 212](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile212.png>)

k

0≤j≤|Φ+| i+j∈2Z

bj,f Volr−1(Pzλ) + 2ε′

(by Inequality (6.10)) <

0≤j≤|Φ+| i+j∈2Z

(by Lemma 6.11) =|Wf| 2

Volr−1(Pzλ) + 2ε′ .

![image 213](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile213.png>)

- At last, since Volr−1(Bk) = kr1−1 Volr−1(B), we obtain


![image 214](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile214.png>)

fbtikλ < |Wf| 2Volr−1(B)

1 kr−1

Sk(z) =

![image 215](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile215.png>)

![image 216](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile216.png>)

Volr−1(Pzλ) + 2ε′ = cVolr−1(Pzλ) + ε.

Similarly, by Inequalities (6.11), (6.9), (6.7), (6.10) and Lemma 6.11, we have

Sk(z) > cVolr−1(Pzλ) − ε, and we are done.

Proposition 6.12 proves Theorem 1.3(2) up to the following equality: 1 Volr(A+) · ρ

= |Wf| Volr−1(B)

,

- (6.12)


![image 217](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile217.png>)

![image 218](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile218.png>)

where B is as in Equation (6.5). We prove this equality in the next subsection.

6.4. Proof of Equation (6.12)

In this subsection, we provide two independent proofs of Equation (6.12). The ﬁrst proof uses the convergence results (Theorem 1.3(1) and Proposition 6.12), while the second only uses Lie-theoretical information.

First proof. By our deﬁnitions of the discrete measure mk and the step function Sk(z), we have

- (6.13)

mk([0,ℓ(tλ)]) =

1 kr

![image 219](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile219.png>)

0≤i≤ℓ(tkλ)

fbtikλ

=

ℓ(tλ)

0

Sk(z)dz +

fbtℓkλ(t

kλ) kr

![image 220](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile220.png>)

=

ℓ(tλ)

0

Sk(z)dz +

1 kr

![image 221](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile221.png>)

. By the weak convergence result (Theorem 1.3(1)), we have

- (6.14) lim

k→∞

mk([0,ℓ(tλ)]) =

Volr(Pλ) Volr(A+)

![image 222](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile222.png>)

. While by the uniform convergence (Proposition 6.12), we have

- (6.15)

lim

k→∞

ℓ(tλ)

0

Sk(z)dx =

ℓ(tλ)

0

|Wf| · 2ρ 2Volr−1(B)

![image 223](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile223.png>)

g(z)dz

= |Wf| · ρ · Volr(Pλ) Volr−1(B)

![image 224](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile224.png>)

.

Because of Equation (6.13), the two limits in (6.14) and (6.15) must coincide. This gives Equation (6.12).

Second proof. Retain the notation D from Section 2.3. Then

![image 225](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile225.png>)

D =

 

 1≤i≤r

aiα∨i ∈ E 0 ≤ ai ≤ 1 for all i

 

 is the closed parallelotope spanned by simple coroots. Let

∆ := Conv{0,α∨1 ,... ,α∨r } be the simplex with vertices {0,α∨1 ,... ,α∨r }. It is well known that

- (6.16) Volr(D) = r! · Volr(∆). Let Z := Hρ,1 ∩ D. Then, Z is the face of ∆ containing α∨1 ,... ,α∨r since

![image 226](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile226.png>)

![image 227](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile227.png>)

(ρ|α∨i ) = 1. The distance from 0 to Hρ,1 equals ρ1 , and we have

![image 228](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile228.png>)

- (6.17) Volr(∆) =


1 ρ · Volr−1(Z).

1 r ·

![image 229](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile229.png>)

![image 230](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile230.png>)

Notice that

 

aiα∨i 0 ≤ ai ≤ 1 for all i, and

Z =

 1≤i≤r

i

 

ai = 1



 

 

α∨1 +

ai(α∨i − α∨1 ) 0 ≤ ai ≤ 1 for all i, and

ai ≤ 1

=

.





2≤i≤r

2≤i≤r

Therefore, Z is a translation of the (r−1)-dimensional simplex with vertices 0,α∨2 − α∨1 ,... ,α∨r − α∨1 .

Note also that B is the parallelotope spanned by α∨2 − α∨1 ,... ,α∨r − α∨1 . Therefore

- (6.18) (r − 1)! · Volr−1(Z) = Volr−1(B). Combining Equations (6.16), (6.17), (6.18), and Lemma 2.16, we have


Volr−1(B) ρ

![image 231](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile231.png>)

= Volr(D) = Volr(D) = |Wf| · Volr(A+) which gives Equation (6.12).

![image 232](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile232.png>)

Remark 6.13. The weak convergence result (Theorem 1.3(1)) can also be deduced from the uniform convergence (Proposition 6.12) and Equations (6.1) and (6.12).

7. General dominant elements Theorem 1.3(2) can be extended to general dominant lower intervals. For

- y ∈ fW, we deﬁne fbyi := Card x ∈ fW x ≤ y,ℓ(x) = i .


Theorem 7.1. Let λ ∈ ZΦ∨ ∩C+. Suppose (wk)k is a sequence of elements in fW such that wk ∈ tkλWf for each k. We deﬁne the step functions Sk by

![image 233](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile233.png>)

Sk(z) := k−(r−1) fbwi k, whenever z ∈ k i , i+1k . Then (Sk)k converges uniformly to g/Volr(A+).

![image 234](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile234.png>)

![image 235](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile235.png>)

Proof. Let λ ∈ ZΦ∨ ∩ C+ and J := {i | 1 ≤ i ≤ r,(λ|αi) = 0}. Then, λ = i∈J ai̟i∨ where each ai ∈ R>0 and the ̟i∨’s are the fundamental coweights, that is, (̟i∨|αj) = δij. Note that each ̟i∨ is a rational combination of simple coroots. Therefore, there is a positive integer n such that λ0 := n i∈J ̟i∨ ∈ ZΦ∨. For this n, there is k0 ∈ N such that for any k ≥ k0 we have

![image 236](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile236.png>)

R>0̟i∨.

kλ − λ0 ∈

i∈J

In particular, λ0,kλ − λ0 ∈ C+ and λWf = kλWf = λ0Wf.

![image 237](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile237.png>)

For any k ≥ k0, we write wk = tkλuk where uk ∈ Wf. By Lemma 4.5, the assumption wk ∈ fW forces that uk ∈ λWf. Moreover, we have wk ≤ tkλ. On the other hand, by Lemmas 4.5 and 2.8, we have

ℓ(wk) = ℓ(tkλ) − ℓ(uk) = ℓ(tkλ−λ0) + ℓ(tλ0) − ℓ(uk) = ℓ(tkλ−λ0) + ℓ(tλ0uk).

Note that wk = tkλ−λ0tλ0uk. Therefore, tkλ−λ0 ≤ wk ≤ tkλ. Hence, for all i we have

fbtikλ−λ0 ≤ fbwi k ≤ fbtikλ.

Let Sk′ and Sk′′ be the corresponding sequences of step functions associated with the sequences (fbtikλ−λ0)i and (fbtikλ)i, respectively. By Theorem 1.3(2), (Sk′′)k converges uniformly to g/Volr(A+). While for (Sk′ )k, using the same arguments as in Section 6, it can be proved that (Sk′ )k converges uniformly to g/Volr(A+) as well. We omit the details.

References

- [1] Pramod N. Achar, Perverse Sheaves and Applications to Representation Theory, Mathematical Surveys and Monographs, vol. 258, American Mathematical Society, Providence, RI, 2021. ↑5
- [2] Aleksandr A. Beı˘linson, Joseph Bernstein, and Pierre Deligne, Faisceaux pervers, Analysis and topology on singular spaces, I (Luminy, 1981), Aste´risque, vol. 100, Soc. Math. France, Paris, 1982, pp. 5–171. ↑3
- [3] Patrick Billingsley, Probability and Measure, third ed., Wiley Series in Probability and Mathematical Statistics, John Wiley & Sons, Inc., New York, 1995, A WileyInterscience Publication. ↑18
- [4] , Convergence of Probability Measures, second ed., Wiley Series in Probability and Statistics: Probability and Statistics, John Wiley & Sons, Inc., New York, 1999, A Wiley-Interscience Publication. ↑18

![image 238](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile238.png>)

- [5] Anders Bjo¨rner and Torsten Ekedahl, On the shape of Bruhat intervals, Ann. of Math.

(2) 170 (2009), no. 2, 799–817. ↑2, 3, and 14

- [6] Nicolas Bourbaki, Lie Groups and Lie Algebras. Chapters 4–6, Elements of Mathematics (Berlin), Springer-Verlag, Berlin, 2002, Translated from the 1968 French original by Andrew Pressley. ↑9, 14, 17, and 19
- [7] Tom Braden, June Huh, Jacob P. Matherne, Nicholas Proudfoot, and Botong Wang, Singular Hodge theory for combinatorial geometries, Preprint, arXiv:2010.06088,

2020. ↑3

- [8] Alexander Braverman, Michael Finkelberg, and Hiraku Nakajima, Towards a mathematical deﬁnition of Coulomb branches of 3-dimensional N = 4 gauge theories, II, Adv. Theor. Math. Phys. 22 (2018), no. 5, 1071–1147. ↑27
- [9] Francesco Brenti, Some open problems on Coxeter groups and unimodality, Available at https://www.samuelfhopkins.com/OPAC/files/proceedings/brenti.pdf, 2022. ↑4
- [10] Gaston Burrull, Tao Gui, and Hongsheng Hu, Strongly dominant weight polytopes are cubes, Preprint, arXiv:2311.16022, 2024. ↑23
- [11] Gaston Burrull, Nicolas Libedinsky, and Rodrigo Villegas, Shape and Class of Bruhat intervals, Preprint, arXiv:2507.14033, 2025. ↑12
- [12] Federico Castillo, Damian de la Fuente, Nicolas Libedinsky, and David Plaza, On the size of Bruhat intervals, Preprint, arXiv:2309.08539, 2023. ↑12
- [13] Johannes J. Duistermaat and Gerrit J. Heckman, On the variation in the cohomology of the symplectic form of the reduced phase space, Invent. Math. 69 (1982), no. 2, 259–268. ↑10
- [14] Euge`ne Ehrhart, Sur les poly`edres rationnels homoth´etiques ` n dimensions, C. R. Acad. Sci. Paris 254 (1962), 616–618. ↑11 and 30
- [15] Ben Elias and Geordie Williamson, The Hodge theory of Soergel bimodules, Ann. of Math. (2) 180 (2014), no. 3, 1089–1136. ↑3
- [16] Victor Ginzburg, Loop Grassmannian cohomology, the principal nilpotent and Kostant theorem, arXiv preprint: math/9803141, 1998. ↑10
- [17] William Graham, Logarithmic convexity of push-forward measures, Invent. Math. 123


(1996), no. 2, 315–322. ↑10

- [18] Branko Gru¨nbaum, Convex Polytopes, second ed., Graduate Texts in Mathematics, vol. 221, Springer-Verlag, New York, 2003, Prepared and with a preface by Volker Kaibel, Victor Klee and Gu¨nter M. Ziegler. ↑19
- [19] Brian Hall, Lie Groups, Lie Algebras, and Representations—An Elementary Introduction, second ed., Graduate Texts in Mathematics, vol. 222, Springer, Cham, 2015. ↑21
- [20] Gerrit J. Heckman, Projections of orbits and asymptotic behavior of multiplicities for compact connected Lie groups, Invent. Math. 67 (1982), no. 2, 333–356. ↑10
- [21] June Huh and Botong Wang, Enumeration of points, lines, planes, etc., Acta Math. 218 (2017), no. 2, 297–317. ↑3
- [22] Nagayoshi Iwahori and Hideya Matsumoto, On some Bruhat decomposition and the structure of the Hecke rings of p-adic Chevalley groups, Inst. Hautes Etudes´ Sci. Publ. Math. 25 (1965), 5–48. ↑14 and 17
- [23] Shrawan Kumar, Kac-Moody Groups, their Flag Varieties and Representation Theory, Progress in Mathematics, vol. 204, Birkh¨auser Boston, Inc., Boston, MA, 2002. ↑2 and 5
- [24] Thomas Lam and Konstanze Rietsch, Total positivity, Schubert positivity, and geometric Satake, J. Algebra 460 (2016), 284–319. ↑5
- [25] Nicolas Libedinsky, IntroSurvey of representation theory, J. Indian Inst. Sci. 102

(2022), no. 3, 907–946. ↑12

- [26] George Lusztig, Singularities, character formulas, and a q-analog of weight multiplicities, Analysis and topology on singular spaces, II, III (Luminy, 1981), Aste´risque, vol. 101-102, Soc. Math., France, Paris, 1983, pp. 208–229. ↑5 and 21
- [27] Ivan Mirkovic´ and Kari Vilonen, Geometric Langlands duality and representations of algebraic groups over commutative rings, Ann. of Math. (2) (2007), 95–143. ↑5
- [28] Andrei Okounkov, Brunn-Minkowski inequality for multiplicities, Invent. Math. 125

(1996), no. 3, 405–411. ↑10

- [29] , Log-concavity of multiplicities with application to characters of U(∞), Adv. Math. 127 (1997), no. 2, 258–282. ↑8

![image 239](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile239.png>)

- [30] , Why would multiplicities be log-concave?, The orbit method in geometry and physics (Marseille, 2000), Progr. Math., vol. 213, Birkh¨auser Boston, Boston, MA, 2003, pp. 329–347. ↑10

![image 240](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile240.png>)

- [31] Leonardo Patimo, Singular Rouquier complexes, Proc. Lond. Math. Soc. 125 (2022), no. 6, 1332–1352. ↑3
- [32] , A Hom formula for Soergel Modules, Preprint, arXiv:2504.06161, 2025. ↑3

![image 241](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile241.png>)

- [33] Konstanze Rietsch, Totally positive Toeplitz matrices and quantum cohomology of partial ﬂag varieties, J. Amer. Math. Soc. 16 (2003), no. 2, 363–392. ↑10
- [34] Gian-Carlo Rota, Combinatorial theory, old and new, Actes du Congre`s International des Mathe´maticiens (Nice, 1970), Tome 3, Gauthier-Villars Editeur,´ Paris, 1971, pp. 229–233. ↑4
- [35] The Stacks Project Authors, The Stacks Project, https://stacks.math.columbia.edu/tag/0BJ8. ↑11
- [36] Dennis Stanton, Unimodality and Young’s lattice, J. Combin. Theory Ser. A 54

(1990), no. 1, 41–53. ↑4

- [37] John R. Stembridge, Tight quotients and double quotients in the Bruhat order, Electron. J. Combin. 11 (2004/06), no. 2, Research Paper 14, 41. ↑21
- [38] Daya-Nand Verma, A strengthening of the exahcange property of Coxeter groups, preprint, 1972. ↑21
- [39] , The roˆle of aﬃne Weyl groups in the representation theory of algebraic Chevalley groups and their Lie algebras, Lie groups and their representations (Proc. Summer School, Bolyai J´anos Math. Soc., Budapest, 1971), Halsted Press, New YorkToronto, Ont., 1975, pp. 653–705. ↑20 and 21


![image 242](<2023-burrull-asymptotic-log-concavity-dominant-lower_images/imageFile242.png>)

- [40] Jianpan Wang, Partial orderings on aﬃne Weyl groups, Forty years of algebraic groups, algebraic geometry, and representation theory in China—in memory of the centenary year of Xihua Cao’s birth, East China Norm. Univ. Sci. Rep., vol. 16, World Sci. Publ., Singapore, 2023, Translated from the Chinese original [J. Wang, Partial orderings on aﬃne Weyl groups, J. East China Norm. Univ., Nat. Sci. Ed. 1987, No. 4, 15–25] by Wang and his daughter Xin Wang, pp. 109–126. ↑20 and 21
- [41] Xinwen Zhu, An introduction to aﬃne Grassmannians and the geometric Satake equivalence, Geometry of moduli spaces and representation theory, IAS/Park City Math. Ser., vol. 24, Amer. Math. Soc., Providence, RI, 2017, pp. 59–154. ↑5 and 27
- [42] Gu¨nter M. Ziegler, Lectures on Polytopes, Graduate Texts in Mathematics, vol. 152, Springer-Verlag, New York, 1995. ↑19


(Gaston Burrull) Beijing International Center for Mathematical Research, Peking Univer-

sity, No. 5 Yiheyuan Road, Haidian District, Beijing 100871, China Email address: gaston(at)bicmr(dot)pku(dot)edu(dot)cn

(Tao Gui) Beijing International Center for Mathematical Research, Peking Univer-

sity, No. 5 Yiheyuan Road, Haidian District, Beijing 100871, China Email address: guitao18(at)mails(dot)ucas(dot)ac(dot)cn

(Hongsheng Hu) School of Mathematics, Hunan University, Changsha 410082, China Email address: huhongsheng(at)hnu(dot)edu(dot)cn

