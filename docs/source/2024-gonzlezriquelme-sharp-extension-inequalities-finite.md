---
type: source
kind: paper
title: Sharp extension inequalities on finite fields
authors: Cristian González-Riquelme, Diogo Oliveira e Silva
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2405.16647v2
source_local: ../raw/2024-gonzlezriquelme-sharp-extension-inequalities-finite.pdf
topic: general-knowledge
cites:
---

arXiv:2405.16647v2[math.CA]11Jul2024

SHARP EXTENSION INEQUALITIES ON FINITE FIELDS

CRISTIAN GONZALEZ-RIQUELME´ AND DIOGO OLIVEIRA E SILVA

Abstract. Sharp restriction theory and the ﬁnite ﬁeld extension problem have both received a great deal of attention in the last two decades, but so far they have not intersected. In this paper, we initiate the study of sharp restriction theory on ﬁnite ﬁelds. We prove that constant functions maximize the Fourier extension inequality from the parabola P1 ⊂ F2q∗ and the paraboloid P2 ⊂ F3q∗ at the euclidean Stein–Tomas endpoint; here, Fdq∗ denotes the (dual) d-dimensional vector space over the ﬁnite ﬁeld Fq with q = pn elements, where p is a prime number greater than 3 or 2, respectively. We fully characterize the maximizers for the L2 → L4 extension inequality from P2 whenever q ≡ 1(mod 4). Our methods lead to analogous results on the hyperbolic paraboloid, whose corresponding euclidean problem remains open. We further establish that constants maximize the L2 → L4 extension inequality from the cone Γ3 := {(ξ, τ, σ) ∈ F4q∗ : τσ = ξ2} \ {0} whenever q ≡ 3(mod 4). By contrast, we prove that constant functions fail to be critical points for the corresponding inequality on Γ3 ∪ {0} over F4p. While some inspiration is drawn from the euclidean setting, entirely new phenomena emerge which are related to the underlying arithmetic and discrete structures.

1. Introduction

Stein’s restriction problem in euclidean space [29] concerns the possibility of restricting the Fourier transform of certain suﬃciently nice functions to curved null subsets of Rd+1 like the paraboloid {(ξ,τ) ∈ Rd × R : τ = |ξ|2} and the cone {(ξ,τ) ∈ Rd × R : τ2 = |ξ|2}. The dual problem is formulated in terms of the adjoint restriction, or extension, operator. In turn, extension estimates from the paraboloid and the cone are equivalent to the well-known Strichartz inequalities [30] for the Schro¨dinger equation iut = ∆u with initial datum u(0,·) = f,

- (1.1) u L2+4/d(Rd+1) ≤ Sd f L2(Rd), and for the wave equation utt = ∆u with initial data (u(0,·),ut(0,·)) = (f,g),
- (1.2) u L2+4/(d−1)(Rd+1) ≤ Wd (f,g) H ˙ 1/2(Rd)×H˙ −1/2(Rd).

The restriction/extension problem has attracted widespread attention due to its deep links to problems in harmonic analysis (Bochner–Riesz), partial diﬀerential equations (local smoothing), geometric measure theory (Kakeya) and number theory (decoupling). Conversely, progress in restriction theory has emerged via powerful tools from diﬀerent ﬁelds, e.g., the multilinear approach which pivots on higher notions of curvature and transversality [3, 4] and the algebro-geometric approach known as the polynomial method [16, 17].

In 2002, Mockenhaupt–Tao [25] inaugurated the study of the extension1 phenomenon for ﬁnite

ﬁelds. Given exponents 1 ≤ p,q ≤ ∞, let R∗S(p → q) denote the best constant for which the extension inequality

- (1.3) (fσ)∨ Lq(Fd,dx) ≤ R∗S(p → q) f Lp(S,dσ)


holds for all functions f : S → C on a given nonempty set of frequencies S ⊂ Fd∗; here, Fd∗ is dual to the d-dimensional vector space Fd over the ﬁnite ﬁeld F, and S is then called a “surface”. In (1.3), (fσ)∨ denotes the extension operator acting on f, dx is the usual counting measure on Fd and dσ is the normalized surface measure on S; these concepts are deﬁned in §2.2 below. The restriction problem for S asks for the set of exponents p,q such that R∗S(p → q) ≤ Cp,q, where Cp,q does not

![image 1](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile1.png>)

2020 Mathematics Subject Classiﬁcation. 05B25, 11T24, 12E20, 42B05, 58E15. Key words and phrases. Finite ﬁelds, Fourier extension problem, sharp restriction theory. 1The Kakeya problem over ﬁnite ﬁelds had been previously introduced by Wolﬀ [31] in 1999, and was famously solved

by Dvir [11] in 2008 using the polynomial method; see also [12].

1

depend on the underlying ﬁeld F. In this case, we say that the restriction property R∗S(p → q) holds. The authors of [25] considered two particular surfaces: the paraboloid (we abbreviate ξ2 := ξ · ξ)

- (1.4) Pd := {(ξ,τ) ∈ Fd∗ × F∗ : τ = ξ2} when d ∈ {1,2}, and the cone
- (1.5) Γd := {(ξ,τ,σ) ∈ F(d−1)∗ × F∗ × F∗ : τσ = ξ2} \ {0}, when d = 2, both equipped with their normalized surface measures. They showed that the restriction

property R∗S(2 → 4) holds when S ∈ {P1,P2,Γ2}. Many authors followed, exploiting methods from additive combinatorics and incidence geometry, among others. We remark that there is no particularly

natural notion of curvature in ﬁnite ﬁelds; to some extent, it may be replaced by the maximal size of aﬃne subspaces, or the Witt index for a quadratic surface; see [23] for details and a careful account of the state of the art concerning the ﬁnite ﬁeld extension problem. Other discrete models for the extension and the Kakeya phenomena have been proposed in [18]; very recently, the Kakeya conjecture has been established over rings of integers modulo N [8, 9], the p-adics [1] and local ﬁelds of positive characteristic [28].

Sharp restriction theory aims at discovering the best constants and maximizers for extension-type inequalities like (1.1) and (1.2). In 2006, Foschi [13] proved that gaussians maximize the cases d ∈ {1,2} of (1.1), which respectively correspond to L2 → L6 and L2 → L4 extension inequalities. In fact, all maximizers are given by initial data corresponding to the orbit of the Schro¨dinger propagator of the standard gaussian exp(−| · |2) under the galilean group of symmetries. In the same paper, Foschi proved that (1.2) is saturated by the pair ((1 + | · |2)−1,0) if d = 3, which corresponds to an L2 → L4 extension inequality. All maximizers are then obtained by letting the Poincare´ group act on the wave propagator of ((1 + | · |2)−1,0). In particular, the best constants S1,S2,W3 are known. Alternative proofs of some of these facts rely on representation formulae [6, 22], heat ﬂow monotonicity [2] and orthogonal polynomials [14], but they all ultimately hinge on the Lebesgue exponents in question being even integers. In this case, one can invoke Plancherel’s identity in order to reduce the problem to a (simpler) multilinear convolution estimate. Sharp restriction theory ﬂourished, with many interesting works on submanifolds of codimension 1 or d−1; see the recent survey [27] for the state of the art.

In the ﬁnite setting of Mockenhaupt–Tao [25], no extension inequality is yet known in sharp form.2 In the present paper, we inaugurate the study of sharp restriction theory on ﬁnite ﬁelds, and proceed to describe our main results on the paraboloids P1,P2 and the cone Γ3. We are also able to handle the hyperbolic paraboloid H2 deﬁned on (1.11) below, and present some further results on the cone Υ3 deﬁned on (1.15) below.

Let p be an odd prime number and q = pn for some n ∈ N. Let Fq denote the ﬁnite ﬁeld with q elements.

- 1.1. Sharp parabolic extension. Our ﬁrst result establishes the sharp L2 → L4 extension inequality from the paraboloid P2 ⊂ F3q∗ equipped with the normalized surface measure σ = σP2.


- Theorem 1.1. It holds that R∗P2(2 → 4) = (1 + q−1 − q−2)41. In other words, the inequality


![image 2](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile2.png>)

- (1.6) (fσ)∨ 4L4(F3


1 q2

1 q −

f 4L2(P2,dσ)

q,dx) ≤ 1 +

![image 3](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile3.png>)

![image 4](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile4.png>)

is sharp, and equality holds if f : P2 → C is a constant function. Moreover, any maximizer of (1.6) has constant modulus.

Our second result fully characterizes the maximizers of inequality (1.6) whenever q ≡ 1(mod 4). The latter condition ensures that −1 is a square in Fq. Given ξ ∈ F2q∗, we then write ξ = η(1,w)+ζ(1,−w), where w2 = −1. We could use the canonical basis {(1,0),(0,1)} of F2q∗ instead, but the lines spanned by (1,±w) turn out to capture the geometry of the parabolic extension problem in a more transparent

![image 5](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile5.png>)

2Interestingly, the proof of [23, Theorem 3] is based on a careful analysis of the near-maximizers for the Stein–Tomas inequality, but the goal there is to analyze concentration eﬀects; see also [23, §17.5–6].

way. We slightly abuse notation and identify a function f : P2 → C with its projection f : F2q∗ → C, f(ξ) = f(ξ,ξ2). Finally, the trace map, Trn : Fq → Fp, is deﬁned in (2.1) below.

- Theorem 1.2. Let q = pn and w ∈ Fq be such that q ≡ 1(mod 4) and w2 = −1. Then f : P2 → C is a maximizer of (1.6) if and only if

(1.7) f(η(1,w) + ζ(1,−w)) = λexp

2πiTrn(aη + bζ + cηζ) p

![image 6](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile6.png>)

,

for some λ ∈ C \ {0} and a,b,c ∈ Fq.

Our third result establishes the sharp L2 → L6 extension inequality from the parabola P1 ⊂ F2q∗ equipped with normalized surface measure σ = σP1. This requires char(Fq) = p > 3.

- Theorem 1.3. Let p > 3. It holds that R∗P1(2 → 6) = (1+q−1−q−2)16. In other words, the inequality

![image 7](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile7.png>)

(1.8) (fσ)∨ 6L6(F2

q,dx) ≤ 1 +

1 q −

![image 8](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile8.png>)

1 q2

![image 9](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile9.png>)

f 6L2(P1,dσ)

is sharp, and equality holds if f : P1 → C is a constant function. Moreover, any maximizer of (1.8) has constant modulus.

Theorems 1.1, 1.2 and 1.3 are ﬁnite ﬁeld analogues of Foschi’s results [13, Theorems 1.1 and 1.4] for the euclidean paraboloid. The crucial observation there was that the relevant convolutions of the projection measure on the paraboloid are constant in the interior of their support, whereas the boundary values can be safely disregarded since they are attained in a null set. In the case of ﬁnite ﬁelds, substantial complications arise which are entirely new. These are due to the ﬁnite nature of Fq, which makes boundary terms non-negligible, and to various arithmetic matters which we proceed to describe.

The proofs of Theorems 1.1 and 1.3 share a common high-level structure which can be summarized as follows. After rewriting the problem in convolution form, we compute the relevant k-fold convolution measures, k ∈ {2,3}. In both cases, the convolution attains two distinct values, one along the socalled critical set, denoted C, and another one on the remaining generic set. A direct application of the Cauchy–Schwarz inequality suﬃces to handle the generic set. Our main eﬀort is geared towards a careful estimate of the terms associated to the critical set. The need arises for a distinction between the cases q ≡ 1 or 3(mod 4) on P2 and q ≡ 1 or 2(mod 3) on P1. In fact, the set of k-tuples of points on the paraboloid which sum to a given (ξ,τ),

(1.9) ΣkPd(ξ,τ) := (ξi)ki=1 ∈ (Fdq∗)k :

k

i=1

(ξi,ξ2i ) = (ξ,τ) ,

is a singleton whenever (ξ,τ) ∈ C, provided q ≡ 3(mod 4) and (d,k) = (2,2), or q ≡ 2(mod 3) and (d,k) = (1,3). This simpliﬁes the analysis considerably. Estimating the terms associated to C in the remaining cases is much more delicate, since adequate bounds for the relevant quantity,

(ξ,τ)∈C

 

 (ξi)ki=1∈ΣkPd(ξ,τ)

k

i=1

f(ξi,ξ2i)

2

− (q − 1)

(ξi)ki=1∈ΣkPd(ξ,τ)

k

i=1

f(ξi,ξ2i )

2

 

(1.10) ,

do not follow from any straightforward application of the Cauchy–Schwarz inequality; see Remarks

- 4.1 and 6.1 below. At this point, the analysis for P2 and P1 splits, as a detailed understanding of the


geometry of the sets ΣkPd(ξ,τ) for (ξ,τ) ∈ C is required.

As far as the proof of Theorem 1.2 is concerned, we note that the euclidean methods from [13, §7] do not seem adequate to handle ﬁnite ﬁelds. Instead, we study the cases of equality for all intermediate inequalities required to estimate (1.10), and then bring in the constraint coming from the initial

Cauchy–Schwarz step for the generic set. The structure of the sets ΣkPd(ξ,τ) for (ξ,τ) ∈ C again plays a key role.

Our methods are quite robust. Surprisingly, the proof of Theorem 1.1 when q ≡ 1(mod 4) can be modiﬁed to yield the sharp L2 → L4 extension inequality from the hyperbolic paraboloid,

- (1.11) H2 := {(ξ1,ξ2,τ) ∈ F3q∗ : τ = ξ12 − ξ22},


equipped with the normalized surface measure σ = σH2, together with the complete characterization of maximizers. This is the content of our fourth result. We highlight that the corresponding euclidean problem remains open [7, 10].

- Theorem 1.4. It holds that R∗H2(2 → 4) = (1 + q−1 − q−2)41. In other words, the inequality

![image 10](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile10.png>)

(1.12) (fσ)∨ 4L4(F3

q,dx) ≤ 1 +

1 q −

![image 11](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile11.png>)

1 q2

![image 12](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile12.png>)

f 4L2(H2,dσ)

is sharp, and equality holds if f : H2 → C is a constant function. Moreover, letting q = pn, then f : H2 → C is a maximizer of (1.12) if and only if

(1.13) f(η(1,1) + ζ(1,−1)) = λexp

2πiTrn(aη + bζ + cηζ) p

![image 13](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile13.png>)

,

for some λ ∈ C \ {0} and a,b,c ∈ Fq.

1.2. Sharp conic extension. The restriction property R∗Γ3(2 → 4) is known to hold [20]. Our ﬁfth result establishes the sharp L2 → L4 extension inequality from the cone Γ3 ⊂ F4q∗ equipped with the normalized surface measure ν = νΓ whenever q ≡ 3(mod 4).

- Theorem 1.5. Let q ≡ 3(mod 4). It holds that


R∗Γ3(2 → 4) = (1 − 2q−1 + 2q−2 − 3q−4 + 3q−5)41(1 − q−1)−34(1 + q−2)−34. In other words, the inequality

![image 14](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile14.png>)

![image 15](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile15.png>)

![image 16](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile16.png>)

- (1.14) (fν)∨ 4L4(F4

q,dx) ≤

q4(q5 − 2q4 + 2q3 − 3q + 3) (q − 1)3(q2 + 1)3

![image 17](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile17.png>)

f 4L2(Γ3,dν)

is sharp, and equality holds if f : Γ3 → C is a constant function. Moreover, any maximizer of (1.14) has constant modulus.

- Theorem 1.5 is the ﬁnite ﬁeld analogue of Foschi’s result [13, Theorem 1.5] for the euclidean cone.

The two-fold convolution of the Lorentz invariant measure on the euclidean cone is constant in the interior of its support, but again this does not suﬃce to handle the case of ﬁnite ﬁelds. In fact, the convolution of the surface measure on the cone Γ3 attains three diﬀerent values: one at the origin 0, a diﬀerent value on Γ3, and yet a diﬀerent one on the remaining generic set. It turns out that Γ3 can be decomposed as a union of disjoint lines, {Ls : s ∈ S}, and that these lines satisfy {η1 ∈ Γ3 : η − η1 ∈ Γ3} ⊂ Ls, for each η ∈ Ls. This structural property plays a key role in the analysis.

Mockenhaupt–Tao remark on [25, p. 53] that the origin has been removed in (1.5) for technical convenience, but that it can be restored with no signiﬁcant change to the results. Surprisingly, this is not the case for the sharp results which we seek to prove. Indeed, if we deﬁne the cone

(1.15) Υ3 := {(ξ,τ,σ) ∈ F2q∗ × F∗q × F∗q : τ2 + σ2 = ξ2} \ {0},

we are able to show that constant functions fail to be critical points on the full cones Γ30 := Γ3 ∪ {0} and Υ30 := Υ3 ∪ {0}. This is the content of our sixth and ﬁnal result, which is valid on ﬁelds of prime cardinality, and stands in sharp contrast with the euclidean case [26].

- Theorem 1.6. Constants are not critical points for the L2(S,dν) → L4(F4p,dx) extension inequality from S ∈ {Γ30,Υ30}.




In particular, constant functions are not local maximizers, and therefore not global maximizers, for R∗Γ3

(2 → 4) or R∗Υ3

(2 → 4). We refer the reader to [26, 27] for the state of the art on sharp conic restriction in the euclidean setting.

0

0

Overview. The paper is organized as follows: In §2, we discuss the relevant ﬁnite ﬁeld preliminaries from Fourier analysis and number theory. In §3, we compute the relevant convolution measures exactly, both via Fourier inversion and counting methods. In the remaining six sections, §4–§9, we prove Theorems 1.1–1.6, respectively.

2. Notation and preliminaries

- 2.1. Notation. Given a set A, we denote its indicator function by 1A. We occasionally extend this notation to statements S, deﬁning 1(S) = 1 if S is true and 1(S) = 0 if S is false. If A is a ﬁnite set, then |A| denotes its cardinality. Real and imaginary parts of a given complex number z ∈ C are denoted by ℜ(z) and ℑ(z), and the principal value of the argument is Arg(z) ∈ (−π,π]. If F is a ﬁnite set of variables, then C(F) denotes a quantity which only depends on elements of F.

We reserve the letter p to denote an odd prime number, and let q = pn for some n ∈ N := {1,2,...}. As in the introduction, Fq denotes the ﬁnite ﬁeld with q elements.

- 2.2. Fourier analysis on ﬁnite ﬁelds. A useful reference for this section is [5]. We are interested in the additive characters of Fq. These can be listed via the trace map, Trn : Fq → Fp, given by


- (2.1) Trn(x) := x + xp + ... + xpn−1.

If n = 1, then Tr1 is just the identity. For each a ∈ Fq, the map ea : Fq → S1,e(x) := exp(2πiTrn(ax)/p), is a character of Fq; if a = 0, then we say that ea is a nonprincipal character, in which case {ea(b·) : b ∈ Fq} is a listing of all the characters of Fq. If e is a nonprincipal character of Fq, which we ﬁx from now onwards, then

- (2.2) x∈Fq

e(x) = 0.

Let Fdq denote the vector ﬁeld over Fq of dimension d < ∞. Then Fdq is a ﬁnite abelian group, and we can describe its Fourier analysis in terms of the nonprincipal character e, since the characters of Fdq are indexed by elements ξ ∈ Fdq∗ of the dual group, via

eξ(x) := e(x · ξ) = e

n

i=1

xiξi =

n

i=1

eξi(xi). From this and (2.2), it follows that

- (2.3) x∈Fdq

e(x · ξ) :=

qd, if ξ = 0, 0, if ξ = 0.

Choosing a speciﬁc nonprincipal character e : Fq → S1 amounts to ﬁxing a group isomorphism between Fdq and Fdq∗, but the corresponding natural measures are diﬀerent. We endow Fdq with the counting measure dx, and Fdq∗ with the normalized counting measure dξ so that Fdq∗ has total mass 1:

Fdq

f(x)dx :=

x∈Fdq

f(x), and

Fdq∗

g(ξ)dξ :=

1 qd

![image 18](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile18.png>)

ξ∈Fdq∗

g(ξ).

Given a function f : Fdq → C, its Fourier transform f : Fdq∗ → C is deﬁned via f(ξ) :=

Fdq

f(x)e(−x · ξ)dx =

x∈Fdq

f(x)e(−x · ξ).

Fourier inversion states that

- (2.4) f(x) =

1 qd

![image 19](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile19.png>)

ξ∈Fdq∗

f(ξ)e(x · ξ) =

Fdq∗

f(ξ)e(x · ξ)dξ =: ( f)∨(x).

Convolution on Fdq is deﬁned in the usual way with respect to counting measure dx, whereas on Fdq∗ convolution is deﬁned with respect to normalized counting measure dξ. The Fourier transform intertwines convolution and multiplication:

- (2.5) f g = f ∗ g, and fg = f ∗ g. If σ is a measure on Fdq∗ deﬁned via its action on a function f : Fdq∗ → C by


1 qd

f(ξ)dσ(ξ) =

f,σ =

f(ξ)w(ξ),

![image 20](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile20.png>)

Fdq∗

ξ∈Fdq∗

then we identify σ with the function w. If 1 ≤ s < d and π : Fsq → Fdq∗ parametrizes an s-dimensional surface S ⊂ Fdq∗, then the normalized surface measure σS (with total mass 1) is given by

- (2.6) f,σS =

1 qs y∈Fs

![image 21](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile21.png>)

q

f(π(y)) =

1 qd

![image 22](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile22.png>)

ξ∈Fdq∗

f(ξ)qd−s|π−1(ξ)|.

In particular, the measure σS is associated with the function w(ξ) = qd−s|π−1(ξ)|. The inverse Fourier transform of σS is given by

σS∨(x) = e(·x),σS =

1 qs y∈Fs

![image 23](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile23.png>)

q

e(x · π(y)),

and, more generally, if f is a complex-valued function deﬁned on the image of π, then

- (2.7) (fσS)∨(x) =

1 qs y∈Fs

![image 24](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile24.png>)

q

f(π(y))e(x · π(y)).

In this paper, the surface S will be either a paraboloid Pd, cone Γd, hyperbolic paraboloid H2, or cone Υ3, respectively deﬁned in (1.4), (1.5), (1.11), (1.15). In this case, we abbreviate σ = σS, and note that (2.6) specializes to

- (2.8) f,σ =

1 |S| ξ∈S

![image 25](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile25.png>)

f(ξ),

and that the extension operator (2.7) acting on a function f : S → C is given by

- (2.9) (fσ)∨(x) =

1 |S| ξ∈S

![image 26](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile26.png>)

f(ξ)e(x · ξ).

For the sake of notation, we will henceforth drop the star from Fd⋆q altogether.

Recall the deﬁnition of the best constant R∗S given in (1.3). It turns out that extension inequalities with even exponents admit combinatorial reformulations which are better suited towards sharp reﬁnements. The next result makes this eﬀective. Further connections between extension inequalities and counting problems are discussed in [15, p. 49] and [25, p. 43].

- Proposition 2.1. The extension inequality


- (2.10) (fσ)∨ L2k(Fdq,dx) ≤ R∗S(2 → 2k) f L2(S,dσ) is equivalent to the combinatorial inequality
- (2.11)


2

 

 

k

k

≤ C∗S(2 → 2k)

|f(ξ)|2

f(ξi)

,

i=1

ξ∈Fdq ξ1+...+ξk=ξ ξi∈S

ξ∈S

in the sense that the set of maximizers of (2.10) coincides with that of (2.11), and the corresponding best constants are related via

C∗S(2 → 2k) = q−d|S|kR∗S(2 → 2k)2k. Proof. Start by noting that

 

 

k

f 2Lk2(S,dσ) = |S|−k

|f(ξ)|2

.

ξ∈S

Raising the left-hand side of (2.10) to the power 2k, using (2.9), and reversing the order of summation,

|(fσ)∨(x)|2k =

x∈Fdq

2k

1 |S|2k

f(ξ)e(x · ξ)

![image 27](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile27.png>)

x∈Fdq ξ∈S

qd |S|2k

=

![image 28](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile28.png>)

∗ k

![image 29](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile29.png>)

f(ξi)f(ηi),

i=1

∗

runs over k-tuples (ξi)ki=1,(ηi)ki=1 ∈ Sk such that ki=1 ξi = ki=1 ηi. In fact, the orthogonality relation (2.3) implies that

where the sum

- (2.12) x∈Fdq

e x ·

k

i=1

ξi −

k

i=1

ηi = 0

unless ki=1 ξi = ki=1 ηi, in which case the left-hand side of (2.12) equals qd. The ﬁnal observation is that

∗ k

i=1

f(ξi)f(ηi) =

![image 30](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile30.png>)

ξ∈Fdq ξ1+...+ξk=ξ ξi∈S

k

i=1

f(ξi)

2

.

2.3. Number theory on ﬁnite ﬁelds. A useful reference for this section is [24, Chapters 5 and 6]. Recall that p denotes an odd prime number, and q = pn for some n ∈ N. Let F×q := Fq \ {0}. For the reader’s convenience, we include elementary proofs of some well-known results, including the size of certain hyperbolas and ellipses in F2q via the following lemma; see also [24, Lemma 6.24].

Lemma 2.2. Let r ∈ F×q . If c = 0 is a square in Fq, then

- (2.13) {(x,y) ∈ F2q : x2 − cy2 = r} = q − 1. If c is not a square in Fq, then
- (2.14) {(x,y) ∈ F2q : x2 − cy2 = r} = q + 1.

- Remark 2.3. In the degenerate case r = 0, one easily checks that


- (2.15) |{(x,y) ∈ F2q : x2 = cy2}| :=

 



2q − 1, if c = 0 is a square in Fq, 1, if c = 0 is not a square in Fq, q, if c = 0.

Proof of Lemma 2.2. If c = 0 is a square in Fq, then let w ∈ F×q be such that w2 = c. The change of variables (x,y)  → (u,v) := (x − wy,x + wy) then yields

{(x,y) ∈ F2q : x2 − cy2 = r} = {(u,v) ∈ F2q : uv = r} = {(u,ru−1) : u ∈ F×q } = q − 1, since r = 0. Now suppose that c is not a square in Fq. Consider the quadratic ﬁeld extension Fq(w)/Fq, where w is an element of the algebraic closure of Fq such that w2 = c. Since Fq(w)/Fq is a Galois extension of degree two, it has just one non-trivial automorphism. Therefore the automorphism (x + wy)  → (x + wy)q coincides with the map x + wy  → x − wy. Hence

{(x,y) ∈ F2q : x2 − cy2 = r} = {(x,y) ∈ F2q : (x + wy)(x − wy) = r}

= {(x,y) ∈ F2q : (x + wy)q+1 = r}

= {a ∈ Fq(w) : aq+1 = r} .

Since the ﬁelds Fq(w) and Fq2 are isomorphic, the group Fq(w)× is cyclic; let g be a generator, and write gα = r = 0. Since rq = r, it follows that gα(q−1) = 1 and therefore q2 − 1 divides α(q − 1). This implies α = α0(q + 1), for some α0 ∈ Zq2−1, and so

{a ∈ Fq(w) : aq+1 = r} = {β ∈ Zq2−1 : β(q + 1) ≡ α(mod(q2 − 1))}

= {β ∈ Zq2−1 : β ≡ α0(mod(q − 1))} = q + 1. This concludes the proof of the lemma.

The Legendre symbol,

a p

![image 31](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile31.png>)

:=

 



1, if a = 0 is a square in Fp, −1, if a is not a square in Fp, 0, if a = 0,

is a completely multiplicative function of its top argument, i.e., for every a,b ∈ Fp,

- (2.16)


a p

b p

ab p

=

.

![image 32](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile32.png>)

![image 33](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile33.png>)

![image 34](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile34.png>)

The Jacobi symbol, m a , is a generalization of the Legendre symbol that allows for a composite bottom argument m, which is assumed to be odd and positive.

![image 35](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile35.png>)

Legendre symbols can be used to evaluate quadratic Gauss sums. If a = 0, then

- (2.17) S(a) := x∈Fp

e(ax2) =

a p

![image 36](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile36.png>)

S(1),

where

- (2.18) S(1) = εp√p, and εp :=

![image 37](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile37.png>)

1, if p ≡ 1(mod 4), i, if p ≡ 3(mod 4);

see [24, Theorems 5.12(i) and 5.15].

- Lemma 2.4. Let εp be as in (2.18). If a ∈ Fp, then

(2.19)

x∈F×p

x p

![image 38](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile38.png>)

e(ax) =

a p

![image 39](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile39.png>)

εp√p.

![image 40](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile40.png>)

Proof. No generality is lost in assuming a = 0. Since (p0) = 0, the sum on the left-hand side of (2.19) can run over the whole Fp instead of F×p . Since (ap)2 = 1, identity (2.16) and the change of variables ax = y together yield

![image 41](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile41.png>)

![image 42](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile42.png>)

(2.20)

x∈Fp

x p

![image 43](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile43.png>)

e(ax) =

a p x∈F

![image 44](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile44.png>)

p

ax p

![image 45](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile45.png>)

e(ax) =

a p y∈F

![image 46](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile46.png>)

p

y p

![image 47](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile47.png>)

e(y).

By (2.2), y∈F

p

e(y) = 0. On the other hand, 1 + (yp) equals the number of solutions to the equation

![image 48](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile48.png>)

z2 = y in Fp. It follows that the right-hand side of (2.20) equals a p z∈F

![image 49](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile49.png>)

p

e(z2) =

a p

![image 50](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile50.png>)

S(1),

which via (2.18) leads to the desired result.

- Lemma 2.5. Let εp be as in (2.18). If a ∈ F×p and b ∈ Fp, then

x∈Fp

e(ax2 + bx) = e(−4b2a)

![image 51](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile51.png>)

a p

![image 52](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile52.png>)

εp√p.

![image 53](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile53.png>)

Proof. Complete the square and change variables. In more detail:

x∈Fp

e(ax2 + bx) = e(−4b2a)

![image 54](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile54.png>)

x∈Fp

e(a(x + 2ba)2) = e(−4b2a)

![image 55](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile55.png>)

![image 56](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile56.png>)

y∈Fp

e(ay2) = e(−4b2a)S(a).

![image 57](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile57.png>)

The desired result follows from (2.17) and (2.18).

We recall the law of quadratic reciprocity, (2.21)

p r

![image 58](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile58.png>)

r p

![image 59](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile59.png>)

= (−1)

(p−1)(r−1)

![image 60](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile60.png>)

4 ,

which holds for Jacobi symbols of arbitrary odd positive coprime integers p,r. This follows from the usual version (e.g., [24, Theorem 5.17]) by induction. We will need (2.21) only for odd primes p. The ﬁrst supplement then reads

(2.22) −1 p

![image 61](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile61.png>)

= (−1)

p−1

![image 62](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile62.png>)

2 ,

and the second supplement then reads (2.23)

2 p

![image 63](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile63.png>)

= (−1)

p2−1

![image 64](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile64.png>)

8 .

We conclude this section by presenting the following well-known characterization of when −1 and −3 are squares over Fq, with q = pn and p an odd prime.

- Lemma 2.6. −1 is a square in Fq if and only if q ≡ 1(mod 4). If p > 3, then −3 is a square in Fq if and only if q ≡ 1(mod 3).




Proof. The ﬁrst statement follows from two elementary observations: the group F×q is cyclic of order q−1 =: m, and −1 is the unique element of order 2 in F×q (this uses p > 2). It follows that there exists x ∈ F×q for which x2 = −1 if and only if 4|m, or equivalently q ≡ 1(mod 4). The second statement is also straightforward to verify. The case n = 1 follows from complete multiplicativity (2.16) of the Legendre symbol, the ﬁrst supplement (2.22) and quadratic reciprocity (2.21):

p 3

= −1 p

3 p

p 3

−3 p

(p−1)(3−1) 4

p−1

, which equals 1 if and only if p ≡ 1(mod 3). If q = pn for some n > 1, we consider two cases: if

=

= (−1)

2 (−1)

![image 65](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile65.png>)

![image 66](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile66.png>)

![image 67](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile67.png>)

![image 68](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile68.png>)

![image 69](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile69.png>)

![image 70](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile70.png>)

![image 71](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile71.png>)

- p ≡ 1(mod 3), then −3 is a square already in Fp. If p ≡ 2(mod 3), then the polynomial x2 + 3 is irreducible over Fp, and so K := Fp[x]/ x2 + 3 is a ﬁeld which contains both zeros of x2 + 3. Since

[K : Fp] = 2, we have that −3 is a square in Fp2. But Fp2 ⊂ Fpn if and only if 2|n. To conclude, we observe that p ≡ 1(mod 3) or 2|n is equivalent to q ≡ 1(mod 3).

3. Convolutions The paraboloid Pd and the cone Γd were deﬁned in (1.4) and (1.5), respectively. In this section, we

compute the k-fold convolution of normalized surface measure σ = σS on S ∈ {Pd,Γd} for diﬀerent values of (d,k,n), where n is such that q = pn. We take two complementary approaches.

- In §3.1, we use Fourier analysis to handle the case of Pd for general d,k ≥ 2, but only when n = 1.
- In §3.2, we use elementary counting methods to handle the case of Pd for general n ≥ 1, but only when directly relevant to Theorems 1.1–1.3, i.e., when (d,k) ∈ {(2,2),(1,3)}. In §3.3, we use Fourier


analysis to compute the two-fold convolution on the full cone Γ30 := Γ3 ∪ {0}, but only when n = 1, and note that this is related to the case of the full cone Υ30 := Υ3 ∪ {0} deﬁned in (1.15) when

- p ≡ 1(mod 4). The case of Γ30 when q ≡ 3(mod 4) and n ≥ 1 is arbitrary, which is directly relevant to Theorem 1.5, is then handled using counting methods in §3.4.


- 3.1. Paraboloids in vector spaces over Fp via Fourier analysis. If k is even, then we write k = 2ν2(k)ℓ, with ν2(k) = max{ℓ ∈ N : 2ℓ|k} and ℓ ≥ 1 odd. Let (1p) := 1.


![image 72](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile72.png>)

- Proposition 3.1. Given d,k ≥ 2 and an odd prime p > k, let σ = σPd denote the normalized surface measure on the paraboloid Pd ⊂ Fdp+1. Then the k-fold convolution measure of σ is given by


- (3.1) σ∗k(ξ,τ) = 1 + εdp(k+1)p

d(1−k)

![image 73](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile73.png>)

2 ϕ(ξ,τ), (ξ,τ) ∈ Fdp+1, where εp was deﬁned in (2.18) and the function ϕ = ϕd,k,p is given by

- (3.2) ϕ(ξ,τ) :=


 

p1{τ=ξ2/k} − 1, if d is even, (−1)

(p−1)(k+1)

4 p

k (p1{τ=ξ2/k} − 1), if d,k are odd, εp√p(−1)

![image 74](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile74.png>)

![image 75](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile75.png>)



2−1

ξ2/k−τ

(p−1)(ℓ+1)

4 +p

8 ν2(k) p ℓ

p , if d is odd and k is even.

![image 76](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile76.png>)

![image 77](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile77.png>)

![image 78](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile78.png>)

![image 79](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile79.png>)

![image 80](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile80.png>)

Proof. It was veriﬁed in [25, Eq. (17)] that σ∨ = δ0 + K, where the Dirac delta δ0 is deﬁned as usual via δ0(0,0) = 1 and δ0(x,t) = 0 if (x,t) = (0,0), and K is the Bochner–Riesz kernel (see [15, p. 52]), deﬁned as K(x,0) = 0 for all x ∈ Fdp, and

1 |Pd|

e(x · ξ + tξ2) = p−dS(t)de −x4t2 , if t = 0.

K(x,t) =

![image 81](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile81.png>)

![image 82](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile82.png>)

(ξ,ξ2)∈Pd

Here, S(t) denotes the quadratic Gauss sum as in (2.17). Using Fourier inversion (2.4) and the intertwining property (2.5), we have for k ≥ 2:

σ∗k(ξ,τ) = [(σ∨)k]∧(ξ,τ) = 1 +

(σ∨)k(x,t)e(−x · ξ − tτ)

(x,t)∈Fdp×F×p

S(t)dke −k4xt2 e(−x · ξ)e(−tτ).

= 1 + p−dk

![image 83](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile83.png>)

(x,t)∈Fdp×F×p

Completing the square,

e −k4xt2 e(−x · ξ) = e −4kt(x + 2ktξ)2 e tξk2 ,

![image 84](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile84.png>)

![image 85](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile85.png>)

![image 86](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile86.png>)

![image 87](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile87.png>)

we obtain via a shift in the x-variable:

 

 

S(t)dke(t(ξk2 − τ))

e(−k4xt2)

σ∗k(ξ,τ) = 1 + p−dk

![image 88](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile88.png>)

![image 89](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile89.png>)

t∈F×p

x∈Fdp

S(t)dke(t(ξk2 − τ))S(−4kt)d

= 1 + p−dk

![image 90](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile90.png>)

![image 91](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile91.png>)

t∈F×p

dk −k/(4t) p

d

t p

- (3.3) e(t(ξk2 − τ)),

![image 92](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile92.png>)

where the passage to the last line uses (2.17). We split the analysis into two cases, depending on the parity of d. If d is odd, then we will further split into two subcases, depending on the parity of k.

- Case 1. If d is even, then all the powers of Legendre symbols appearing in (3.3) are equal to 1. Appealing to (2.18), we then have that

σ∗k(ξ,τ) = 1 + εdp(k+1)p

d(1−k) 2

![image 93](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile93.png>)

t∈F×p

e(t(ξk2 − τ)).

![image 94](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile94.png>)

By (2.2), the latter sum evaluates to

t∈F×p

e(t(ξk2 − τ)) = p − 1, if τ = ξk2,

![image 95](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile95.png>)

![image 96](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile96.png>)

−1, otherwise. For even d, it then holds that

σ∗k(ξ,τ) = 1 + εdp(k+1)p

d(1−k)

![image 97](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile97.png>)

2 (p1{τ=ξ2/k} − 1).

- Case 2. If d is odd, then matters are simpler if k is odd. In this case, k is coprime to p since k < p. Complete multiplicativity (2.16) of the Legendre symbol, the ﬁrst supplement (2.22), and quadratic reciprocity (2.21) together yield


t p

![image 98](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile98.png>)

−k/(4t) p

![image 99](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile99.png>)

= −k/4 p

![image 100](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile100.png>)

= −k p

![image 101](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile101.png>)

= −1 p

![image 102](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile102.png>)

k p

![image 103](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile103.png>)

= (−1)

p−1

![image 104](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile104.png>)

2 (−1)

(p−1)(k−1) 4

![image 105](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile105.png>)

p k

![image 106](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile106.png>)

= (−1)

(p−1)(k+1) 4

![image 107](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile107.png>)

p k

![image 108](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile108.png>)

. From (3.3) we then have, for odd d and k,

σ∗k(ξ,τ) = 1 + εdp(k+1)p

d(1−k)

![image 109](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile109.png>)

2 (−1)

(p−1)(k+1) 4

![image 110](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile110.png>)

p k

![image 111](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile111.png>)

(p1{τ=ξ2/k} − 1).

We ﬁnally come to the case when d is odd and k is even. If k is not a power of 2, then k = 2ν2(k)ℓ, for some odd integer ℓ > 1. We compute:

t p

![image 112](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile112.png>)

−k/(4t) p

![image 113](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile113.png>)

= −k p

![image 114](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile114.png>)

= (−1)

p−1 2

![image 115](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile115.png>)

k p

![image 116](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile116.png>)

= (−1)

p−1 2

![image 117](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile117.png>)

2 p

![image 118](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile118.png>)

ν2(k) ℓ p

![image 119](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile119.png>)

= (−1)

(p−1)(ℓ+1)

![image 120](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile120.png>)

4 +p

2−1

![image 121](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile121.png>)

8 ν2(k) p ℓ

![image 122](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile122.png>)

.

- (3.4)


= 1 + p−dkS(1)d(k+1)

![image 123](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile123.png>)

![image 124](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile124.png>)

t∈F×p

The last identity uses quadratic reciprocity (2.21) (ℓ is odd and coprime to p since k < p) and the second supplement (2.23). From (3.3), we then have, for odd d and even k,

d(1−k)

(p−1)(ℓ+1)

4 +p

σ∗k(ξ,τ) = 1 + εdp(k+1)p

2 (−1)

![image 125](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile125.png>)

![image 126](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile126.png>)

The latter sum can be evaluated with Lemma 2.4,

t∈F×p

t p

![image 127](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile127.png>)

e(t(ξk2 − τ)) =

![image 128](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile128.png>)

8 ν2(k) p ℓ

2−1

![image 129](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile129.png>)

![image 130](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile130.png>)

t∈F×p

ξ2/k − τ p

![image 131](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile131.png>)

εp√p,

![image 132](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile132.png>)

t p

![image 133](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile133.png>)

e(t(ξk2 − τ)).

![image 134](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile134.png>)

which ﬁnally yields

- (3.5) σ∗k(ξ,τ) = 1 + εdp(k+1)+1p

d(1−k)+1

![image 135](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile135.png>)

2 (−1)

(p−1)(ℓ+1)

![image 136](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile136.png>)

4 +p

2−1

![image 137](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile137.png>)

8 ν2(k) p ℓ

![image 138](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile138.png>)

ξ2/k − τ p

![image 139](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile139.png>)

. If k = 2ν2(k) is a power of 2, then matters are simpler. In this case, (3.4) simpliﬁes to

t p

![image 140](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile140.png>)

−k/(4t) p

![image 141](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile141.png>)

= (−1)

p−1 2

![image 142](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile142.png>)

2 p

![image 143](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile143.png>)

ν2(k)

, and (3.3) then boils down to

- (3.6) σ∗k(ξ,τ) = 1 + εdp(k+1)+1p

d(1−k)+1

![image 144](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile144.png>)

2 (−1)

p−1

![image 145](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile145.png>)

2 +p

2−1

![image 146](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile146.png>)

8 ν2(k) ξ2/k − τ p

![image 147](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile147.png>)

.

In other words, formula (3.5) is still valid for ℓ = 1 with the convention that (1p) = 1. This completes the proof of Proposition 3.1.

![image 148](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile148.png>)

Remark 3.2. From (3.6), it follows that the two-fold convolution of normalized surface measure on P1 ⊂ F2p, corresponding to (d,k) = (1,2), is given by

- (3.7) (σ ∗ σ)(ξ,τ) = 1 + (−1)

p−1

![image 149](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile149.png>)

2 +p

2−1 8

![image 150](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile150.png>)

ξ2/2 − τ p

![image 151](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile151.png>)

, (ξ,τ) ∈ F2p.

This expression takes on three distinct values, depending on whether ξ2/2 − τ is or is not a square in Fp, or whether ξ2/2 − τ is divisible by p, and each of these values occurs multiple times.

- 3.2. Low dimensional paraboloids in vector spaces over Fq via counting. Letting σ = σPd denote the normalized surface measure on the paraboloid Pd ⊂ Fdq+1, from Proposition 2.1 we have


- (3.8) σ∗k(ξ,τ) =

qd+1 |Pd|k

![image 152](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile152.png>)

|ΣkPd(ξ,τ)|,

where the set ΣkPd(ξ,τ) was deﬁned in (1.9). Since Pd is the graph of the function ϕ : Fdq → Fq, ϕ(ξ) = ξ2, we have that |Pd| = qd. In the proof of the following result, we compute the cardinality

of ΣkPd(ξ,τ), thereby generalizing to vector spaces over Fq (and not just over Fp) the cases (d,k) ∈ {(1,3),(2,2)} of Proposition 3.1.

- Proposition 3.3. The two-fold convolution on P2 ⊂ F3q is given by


- (3.9) (σ ∗ σ)(ξ,τ) =

1 q × q ± q ∓ 1, if τ = ξ22,

![image 153](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile153.png>)

![image 154](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile154.png>)

q ∓ 1, otherwise, where the ﬁrst choice of signs corresponds to q ≡ 1(mod 4) and the second one to q ≡ 3(mod 4). If p > 3, then the three-fold convolution on P1 ⊂ F2q is given by

- (3.10) (σ ∗ σ ∗ σ)(ξ,τ) =

1 q × q ± q ∓ 1, if τ = ξ32,

![image 155](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile155.png>)

![image 156](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile156.png>)

q ∓ 1, otherwise, where the ﬁrst choice of signs corresponds to q ≡ 1(mod 3) and the second one to q ≡ 2(mod 3). Given (γ,s) ∈ Fdq × Fq, we deﬁne the sphere of center γ and squared radius s as in [19]:

- (3.11) S(γ,s) := {η ∈ Fdq : (γ − η)2 = s}.


- Proof of Proposition 3.3. Let us start with the two-fold convolution. From ξ = ξ1+ξ2 and τ = ξ21+ξ22 it follows that ξ21 + (ξ − ξ1)2 = τ, or equivalently ξ1 ∈ S(ξ2, 2τ−4ξ2). In particular,


![image 157](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile157.png>)

![image 158](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile158.png>)

|Σ2P2(ξ,τ)| = S(ξ2, 2τ−4ξ2) .

![image 159](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile159.png>)

![image 160](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile160.png>)

- If τ = ξ2/2, then a translation, the ﬁrst statement in Lemma 2.6 and Remark 2.3 imply


|Σ2P2(ξ,τ)| = |S(ξ2,0)| =

![image 161](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile161.png>)

- If τ = ξ2/2, then Lemma 2.2 implies


2q − 1, if q ≡ 1(mod 4), 1, if q ≡ 3(mod 4).

|Σ2P2(ξ,τ)| =

q − 1, if q ≡ 1(mod 4), q + 1, if q ≡ 3(mod 4).

- Identity (3.9) follows from this via (3.8). To handle the three-fold convolution, observe that ξ = ξ1 + ξ2 + ξ3 and τ = ξ12 + ξ22 + ξ32 together imply

(3.12) 3τ − ξ2 = (ξ1 − ξ2)2 + (ξ2 − ξ3)2 + (ξ3 − ξ1)2. We thus need to count the number of solutions to (3.12). Changing variables (ξ1,ξ2,ξ3)  → (ξ1,α1,α2) :=

(ξ1,ξ2 − ξ1,ξ3 − ξ2), the latter equals the number of solutions to α21 + α22 + (α1 + α2)2 = 3τ − ξ2 or, by further renaming (β,γ) =: (α1 + α2/2,α2/2), the number of solutions to β2 + 3γ2 = (3τ − ξ2)/2. If τ = ξ2/3, then the second statement in Lemma 2.6 and Remark 2.3 together imply

(3.13) |Σ3P1(ξ,τ)| = (β,γ) ∈ F2q : β2 + 3γ2 = 0 =

2q − 1, if q ≡ 1(mod 3), 1, if q ≡ 2(mod 3).

If τ = ξ2/3, then r := (3τ − ξ2)/2 is nonzero, and Lemma 2.2 implies

(3.14) |Σ3P1(ξ,τ)| = (β,γ) ∈ F2q : β2 + 3γ2 = r =

q − 1, if q ≡ 1(mod 3), q + 1, if q ≡ 2(mod 3).

- Identity (3.10) follows from this via (3.8). This concludes the proof of the proposition.


- 3.3. Cones in vector spaces over Fp via Fourier analysis. Recall the deﬁnition of the cones Γ3 and Υ3 given in (1.5) and (1.15), respectively, and that Γ30 := Γ3 ∪ {0} and Υ30 := Υ3 ∪ {0}.


- Proposition 3.4. The two-fold convolution of normalized surface measure on Υ30 ⊂ F4p, denoted νΥ, is given by


- (3.15) (νΥ ∗ νΥ)(ξ,τ,σ) =

p3 (p2 + p − 1)2 ×

![image 162](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile162.png>)

 



p2 + p − 1, if (ξ,τ,σ) = 0,

2p − 1, if (ξ,τ,σ) ∈ Υ3, p + 1, if (ξ,τ,σ) ∈/ Υ30.

The two-fold convolution of normalized surface measure on Γ30 ⊂ F4p, denoted νΓ, is given by

- (3.16) (νΓ ∗ νΓ)(ξ,τ,σ) =

p3 (p2 ± p ∓ 1)2 ×

![image 163](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile163.png>)

 



p2 ± p ∓ 1, if (ξ,τ,σ) = 0, p ± p ∓ 1, if (ξ,τ,σ) ∈ Γ3, p ± 1, if (ξ,τ,σ) ∈/ Γ30,

where the ﬁrst choice of signs corresponds to p ≡ 1(mod 4) and the second one to p ≡ 3(mod 4).

- Proof of Proposition 3.4. We start with the proof of (3.15), which is similar to that of (3.16) when


- p ≡ 1(mod 4). The case p ≡ 3(mod 4) of (3.16) is simpler and will be presented afterwards.


The case of Υ30. Write (x,t,s) ∈ F4p, where x = (x1,x2) ∈ F2p, for the variables dual to (ξ,τ,σ) ∈ F4p. Let ζ(x,t,s) := x2 − t2 − s2. Start by noting that

- (3.17) νΥ∨(x,t,s) =


 

1, if (x,t,s) = 0,

p−1

p2+p−1, if ζ(x,t,s) = 0 but (x,t,s) = 0,

![image 164](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile164.png>)



−1

p2+p−1, if ζ(x,t,s) = 0; Indeed, since (ξ,τ,σ) ∈ Υ30 if and only if ζ(ξ,τ,σ) = 0, it follows that

![image 165](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile165.png>)

|Υ30| p4

1 p4

νΥ∨(x,t,s) =

e((x,t,s) · (ξ,τ,σ))

![image 166](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile166.png>)

![image 167](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile167.png>)

(ξ,τ,σ)∈Υ30

  e((x,t,s) · (ξ,τ,σ))

 1

1 p4

e(λζ(ξ,τ,σ))

=

![image 168](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile168.png>)

![image 169](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile169.png>)

p λ∈F

(ξ,τ,σ)∈F4p

p

δ0(x,t,s) p

1 p5 λ =0

=

+

e(λζ(ξ,τ,σ) + (x,t,s) · (ξ,τ,σ))

![image 170](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile170.png>)

![image 171](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile171.png>)

(ξ,τ,σ)∈F4p

δ0(x,t,s) p

+

=

![image 172](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile172.png>)

1 p3 λ =0

e ζ(−x4,t,sλ ) ,

![image 173](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile173.png>)

![image 174](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile174.png>)

where the last identity follows from four consecutive applications of Lemma 2.5. Therefore

|Υ30| p4

1 p3 ×

δ0(x,t,s) p

p − 1, if ζ(x,t,s) = 0, −1, if ζ(x,t,s) = 0.

νΥ∨(x,t,s) =

+

![image 175](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile175.png>)

![image 176](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile176.png>)

![image 177](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile177.png>)

From νΥ∨(0) = 1, it then follows that |Υ30| = p(p2+p−1), which implies (3.17). We use this to compute the convolution measure νΥ ∗ νΥ via Fourier inversion (2.4) and the intertwining property (2.5):

(νΥ ∗ νΥ)(ξ,τ,σ) = [(νΥ∨)2]∧(ξ,τ,σ)

2

2

e(−(x,t,s) · (ξ,τ,σ)) + p2 p+−p1−1

= 1 + p2+ −p1−1

e(−(x,t,s) · (ξ,τ,σ))

![image 178](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile178.png>)

![image 179](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile179.png>)

- (3.18)

Since the ﬁrst sum on the previous line equals p4δ0(ξ,τ,σ) − 1, our main task will be to compute S(ξ,τ,σ) :=

ζ(x,t,s)=0

e(−(x,t,s) · (ξ,τ,σ)).

Note that S(0) = |Υ30| and that S(±ξ1,±ξ2,±τ,±σ) is independent of the choice of signs. Changing variables (a,b) := (s − x2,s + x2), which implies (x2,s) = 12(b − a,a + b), yields

![image 180](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile180.png>)

(x,t,s) · (ξ,τ,σ) = (x1, b−2a,t, a+2b) · (ξ,τ,σ) = x1ξ1 + aσ−2ξ2 + tτ + bξ22+σ. After this change of variables, ζ(x,t,s) = 0 if and only x21 − t2 = ab, and so

![image 181](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile181.png>)

![image 182](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile182.png>)

![image 183](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile183.png>)

![image 184](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile184.png>)

- (3.19) S(ξ,τ,σ) =

  

x2 1

−t2=ab b=0

+

x2 1

−t2=ab b =0

  e(−(x,t,s) · (ξ,τ,σ)) =: S1(ξ,τ,σ) + S2(ξ,τ,σ).

The ﬁrst sum in (3.19), corresponding to b = 0, evaluates to

S1(ξ,τ,σ) =

t=±x1 a∈Fp

e(−x1ξ1 − tτ)e a

ξ2 − σ 2

![image 185](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile185.png>)

=

 

x1∈Fp

e(−x1(ξ1 + τ)) +

x1∈Fp

e(−x1(ξ1 − τ)) − 1

 

a∈Fp

e a

ξ2 − σ 2

![image 186](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile186.png>)

- (3.20) ,

which is nonzero only if ξ2 = σ. More precisely, we have that

- (3.21) S1(ξ,τ,σ) =

 



(2p − 1)p, if ξ1 = τ = 0 and ξ2 = σ, (p − 1)p, if ξ1 = ±τ = 0 and ξ2 = σ, −p, if ξ1 = ±τ and ξ2 = σ, 0, otherwise.

We proceed to compute the second sum in (3.19), corresponding to b = 0. Changing variables (A,B) := (σ − ξ2,σ + ξ2), we have that

S2(ξ,τ,σ) =

x1,t∈Fp b =0

e −x1ξ1 −

x21 − t2 b

![image 187](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile187.png>)

σ − ξ2 2 − tτ − b

![image 188](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile188.png>)

ξ2 + σ 2

![image 189](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile189.png>)

=

b =0

 

x1∈Fp

e(−x1ξ1 − 2Abx21)

![image 190](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile190.png>)

 

 

t∈Fp

e(−tτ + 2Abt2)

![image 191](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile191.png>)



- (3.22) e(−bB2 ).


ζ(x,t,s)=0 (x,t,s) =0

ζ(x,t,s) =0

2

e(−(x,t,s) · (ξ,τ,σ)) + (p2p+2−p−2p1)2 (−1 + S(ξ,τ,σ)) .

=: 1 + p2+ −p1−1

![image 192](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile192.png>)

![image 193](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile193.png>)

(x,t,s) =0

![image 194](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile194.png>)

If A = 0, i.e., ξ2 = σ, then Lemma 2.5 implies S2(ξ,τ,σ) = ε2pp

−A/2b p

![image 195](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile195.png>)

b =0

= pε2p −1 p b =0

e (ξ

![image 196](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile196.png>)

A/2b p

![image 197](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile197.png>)

2 1b

e ξ

2A e − τ22Ab e −bB2

![image 198](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile198.png>)

![image 199](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile199.png>)

![image 200](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile200.png>)

2 1−τ2)b

2A e −bB2

![image 201](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile201.png>)

![image 202](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile202.png>)

p − 1, if ζ(ξ,τ,σ) = 0, −1, if ζ(ξ,τ,σ) = 0.

e ζ(ξ2,τ,σA )b = p ×

= p

- (3.23)

Here, we used the facts that ε2p −1

![image 203](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile203.png>)

p

= 1, for every p, and AB = σ2 −ξ22. If A = 0, i.e., ξ2 = σ, then from (3.22) we have that

S2(ξ,τ,σ) =

b =0

 

x1∈Fp

e(−x1ξ1)

 

 

t∈Fp

e(−tτ)

  e(−bB2 )

![image 204](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile204.png>)

=

 

x1∈Fp

e(−x1ξ1)

 

 

t∈Fp

e(−tτ)

 

 

b =0

e(−bB2 )

![image 205](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile205.png>)

 

= pδ0(ξ1) × pδ0(τ) × (pδ0(B) − 1), or equivalently

- (3.24) S2(ξ,τ,σ) = p2 ×

 



p − 1, if ξ1 = τ = 0 and ξ2 = −σ, −1, if ξ1 = τ = 0 and ξ2 = −σ, 0, otherwise .

Identities (3.21) and (3.23)–(3.24) together imply that

S(ξ,τ,σ) = S1(ξ,τ,σ) + S2(ξ,τ,σ) =

 



p3 + p2 − p, if (ξ,τ,σ) = 0, p2 − p, if (ξ,τ,σ) ∈ Υ3, −p, if (ξ,τ,σ) ∈/ Υ30,

from where (3.15) follows. This concludes the analysis of the two-fold convolution on Υ30. The case of Γ30. If p ≡ 1(mod 4), then −1 is a square in Fp. In this case, let w2 = −1. Then the change of variables (τ,σ) = (u + wv,u − wv) bijectively maps Γ30 into Υ30, and this implies (3.16).

If p ≡ 3(mod 4), then matters are diﬀerent for Γ30 but simpler than what we already did for Υ30, so we shall be brief. Continue to write (x,t,s) ∈ F4p, where x = (x1,x2) ∈ F2p, for the variables dual to (ξ,τ,σ) ∈ F4p. Let η(x,t,s) := x2 − 4ts. The ﬁrst observation is that

- (3.25) νΓ∨(x,t,s) =

 



1, if (x,t,s) = 0,

1−p

![image 206](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile206.png>)

p2−p+1, if η(x,t,s) = 0 but (x,t,s) = 0,

1

![image 207](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile207.png>)

p2−p+1, if η(x,t,s) = 0;

recall (3.17) and see [21, Lemma 4.1]. We then compute the convolution measure νΓ ∗ νΓ via Fourier inversion as in (3.18):

- (3.26) (νΓ ∗ νΓ)(ξ,τ,σ)

= 1 + p2− 1p+1

![image 208](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile208.png>)

2

(x,t,s) =0

e(−(x,t,s) · (ξ,τ,σ)) + (p2p−2−p+1)2p 2

![image 209](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile209.png>)

 −1 +

η(x,t,s)=0

e(−(x,t,s) · (ξ,τ,σ))

  .

The ﬁrst sum equals p4δ0(ξ,τ,σ) − 1. We decompose the second sum in two pieces, depending on whether t is zero or not:

- (3.27)


![image 210](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile210.png>)

b =0

  e(−x · ξ) +

 

e(−x · ξ − tτ)e −x4t2σ .

e(−sσ)

e(−(x,t,s) · (ξ,τ,σ)) =

![image 211](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile211.png>)

s∈Fp

x∈F2p t =0

x2=0

η(x,t,s)=0

The inner sum of the ﬁrst summand on the right-hand side of (3.27) is zero unless σ = 0:

e(−sσ) =

s∈Fp

p, if σ = 0, 0, if σ = 0,

and the condition on the outer sum, x2 = 0, implies x = 0 since −1 is not a square in Fp. As for the second summand on the right-hand side of (3.27), if σ = 0, then we have

 

p2(p − 1), if (ξ,τ,σ) = 0, −p2, if ξ = 0 and τ = 0, 0, if ξ = 0.

e(−x · ξ − tτ) =



x∈F2p t =0

If σ = 0, then things are a bit more delicate. Completing squares,

x2 4t

σ

e(−x · ξ − tτ)e −

![image 212](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile212.png>)

x∈F2p t =0

 

2   

2   

 

- (3.28)

By translation symmetry, the inner Gauss sums are identical, giving rise to a contribution which equals S −4σt 2 = S(1)2 = −p,

![image 213](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile213.png>)

- and so (3.28) boils down to

−p

t =0

e t ξσ2 − τ =

![image 214](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile214.png>)

p − p2, if (ξ,τ,σ) ∈ Γ30 and σ = 0, p, if (ξ,τ,σ) ∈/ Γ30 and σ = 0.

Putting everything together, we have that

(3.29) (νΓ ∗ νΓ)(ξ,τ,σ) = 1 + −1 + p41(ξ,τ,σ)=0 + (p2 − 2p)Ap(ξ,τ,σ) (p2 − p + 1)2

![image 215](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile215.png>)

, where the function Ap is given by

Ap(ξ,τ,σ) := −1 + p1(σ = 0) + p2(p − 1)1((ξ,τ,σ) = 0)

− p21(ξ = 0,τ = 0 = σ) + p1(σ = 0) − p21((ξ,τ,σ) ∈ Γ30, σ = 0). The ﬁnal observation is that

{(ξ,τ,σ) ∈ F4p : ξ = 0,τ = 0 = σ} ∪ {(ξ,τ,σ) ∈ F4p : (ξ,τ,σ) ∈ Γ30 and σ = 0} = Γ3,

- and so (3.29) simpliﬁes to


- (3.30) (νΓ ∗ νΓ)(ξ,τ,σ) =


e t ξσ2 − τ .

e −4σt x1 + 2ξσ1t

e −4σt x2 + 2ξσ2t

=

![image 216](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile216.png>)

![image 217](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile217.png>)

![image 218](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile218.png>)

![image 219](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile219.png>)

![image 220](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile220.png>)

 x

 x

1∈Fp

2∈Fp

t =0

p(p − 1)(p − 2) − 1 + p4(p − 1)1(ξ,τ,σ)=0 − p3(p − 2)1(ξ,τ,σ)∈Γ3

0

(νΓ ∗ νΓ)(ξ,τ,σ) = 1 +

, from where the case p ≡ 3(mod 4) of (3.16) follows at once.

![image 221](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile221.png>)

(p2 − p + 1)2

- 3.4. Cones in vector spaces over Fq via counting. Letting ν = νΓ denote the normalized surface measure on the cone Γ30 ⊂ F4q, from Proposition 2.1 it follows that


q4 |Γ30|2

|Σ2Γ3

(ξ,τ,σ)|, where, similarly to (1.9), we deﬁne the set

![image 222](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile222.png>)

0

(ξ,τ,σ) := ((ξi,τi,σi))2i=1 ∈ (Γ30)2 :

Σ2Γ3

0

2

(ξi,τi,σi) = (ξ,τ,σ) .

i=1

In this section, we compute the convolution measure (3.30) whenever q ≡ 3(mod 4), thereby generalizing this instance of (3.16) to vector spaces over Fq (and not just over Fp). We start by computing the size of the cone Γ30 ⊂ F4q.

- Lemma 3.5. Let q ≡ 3(mod 4). Then Γ30 = q(q2 − q + 1).


Proof. We count the number of solutions (ξ,τ,σ) ∈ F4q to the equation ξ2 = τσ =: ρ. If ρ = 0, then Remark 2.3 leads to 2q − 1 solutions. If ρ = 0, then identity (2.14) leads to (q − 1)2(q + 1) solutions; this uses the fact that −1 is not a square in Fq. To conclude, note that (2q − 1) + (q − 1)2(q + 1) = q(q2 − q + 1).

Proposition 3.6. Let q ≡ 3(mod 4). Then the two-fold convolution on Γ30 ⊂ F4q is given by

- (3.31) (νΓ ∗ νΓ)(ξ,τ,σ) =

q3 (q2 − q + 1)2 ×

![image 223](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile223.png>)

 



q2 − q + 1, if (ξ,τ,σ) = 0,

1, if (ξ,τ,σ) ∈ Γ3, q − 1, if (ξ,τ,σ) ∈/ Γ30.

Proof. From (3.30) and Lemma 3.5, it suﬃces to verify that

- (3.32) |Σ2Γ3

0

(ξ,τ,σ)| =

 



q(q2 − q + 1), if (ξ,τ,σ) = 0, q, if (ξ,τ,σ) ∈ Γ3, q(q − 1), if (ξ,τ,σ) ∈/ Γ30.

Start by noting that Σ2Γ3

0

(ξ,τ,σ) has the same number of elements as the set

S(ξ,τ,σ) := {(ξ1,τ1,σ1) ∈ Γ30 : (ξ − ξ1,τ − τ1,σ − σ1) ∈ Γ30}.

Given (ξ1,τ1,σ1) ∈ S(ξ,τ,σ), we have (ξ − ξ1)2 = (τ − τ1)(σ − σ1). Since ξ21 = τ1σ1, this can be rewritten as

- (3.33) τσ − ξ2 − τ1σ = τσ1 − 2ξ · ξ1. We split the analysis of (3.33) into two cases, depending on whether or not τ is nonzero.

Case 1: τ = 0. In this case, the number of solutions (ξ1,τ1,σ1) ∈ S(ξ,τ,σ) with τ1 = 0 of

ξ21 = τ1σ1 τσ − ξ2 − τ1σ = τσ1 − 2ξ · ξ1

equals the number of solutions with τ1 = 0 of the equation τσ − ξ2 − τ1σ =

τ τ1

![image 224](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile224.png>)

ξ1 −

τ1 τ

![image 225](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile225.png>)

ξ

2

−

τ1 τ

![image 226](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile226.png>)

ξ2, or equivalently of

(ξ2 − τσ)

τ1 − τ τ

![image 227](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile227.png>)

=

τ τ1

![image 228](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile228.png>)

ξ1 −

τ1 τ

![image 229](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile229.png>)

ξ

2

- (3.34) . We split the analysis into two further subcases.

- Case 1.1. ξ2 = τσ. By Lemma 2.2, any nonzero τ1 = τ deﬁnes q + 1 points ξ1 that solve (3.34). If τ1 = τ, then necessarily ξ1 = ξ. In this case, we then have |S(ξ,τ,σ)∩{τ1 = 0}| = (q −2)(q +1)+1 =

- q2 −q−1. On the other hand, if τ1 = 0, then ξ21 = 0 and therefore ξ1 = 0; in particular, σ1 = σ−ξ2/τ yields the unique solution. All in all, we have |S(ξ,τ,σ)| = q(q − 1).


- Case 1.2. ξ2 = τσ. For each τ1 = 0, (3.34) has a unique solution, whence |S(ξ,τ,σ) ∩ {τ1 =


0}| = q − 1. On the other hand, if τ1 = 0, then ξ1 = 0, which by (3.33) forces σ1 = 0. Therefore |S(ξ,τ,σ)| = q.

Case 2: τ = 0. In this case, equation (3.33) boils down to

- (3.35) ξ2 + τ1σ = 2ξ · ξ1, which can be analyzed by splitting into three further subcases.


Case 2.1. ξ = 0. In this case, τ1σ = 0. If σ = 0, then Lemma 3.5 implies |S(0,0,0)| = Γ30 = q(q2 − q + 1). If σ = 0, then (ξ1,τ1) = (0,0) while σ1 is free, and so |S(0,0,σ)| = q.

In order to handle the two remaining subcases, we observe that the number of solutions of (3.35) (alongside with ξ21 = τ1σ1) when σ1 = 0 equals the number of solutions of

σ σ1

ξ2 + ξ21

- (3.36) = 2ξ · ξ1.

Case 2.2. ξ2 = 0 and σ = 0. In this case, (3.36) can be rewritten as

- (3.37) ξ1 −

σ1 σ

![image 230](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile230.png>)

ξ

2 σ σ1

![image 231](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile231.png>)

=

σ1 − σ σ

![image 232](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile232.png>)

ξ2.

For each nonzero σ1 = σ, Lemma 2.2 implies the existence of q +1 distinct points ξ1 that solve (3.37). If σ1 = σ, then ξ1 = ξ is the unique solution. Therefore |S(ξ,τ,σ) ∩ {σ1 = 0}| = (q − 2)(q + 1) + 1 = q2 − q − 1. On the other hand, if σ1 = 0, then ξ1 = 0 and (3.35) becomes ξ2 + τ1σ = 0, and therefore (0,0,−ξ2/σ,0) is the unique solution. Thus |S(ξ,τ,σ)| = q(q − 1).

Case 2.3. ξ2 = 0 = σ. In this case, (3.36) boils down to

- (3.38) ξ2 = 2ξ · ξ1,


![image 233](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile233.png>)

which has exactly q solutions. From (3.38) it follows that ξ21 = 0, and for each nonzero ξ1 there exist q − 1 pairs (τ1,σ1), such that ξ21 = τ1σ1. Thus |S(ξ,τ,σ)| = q(q − 1).

To conclude the proof of (3.32), note that (ξ,τ,σ) ∈/ Γ30 in Cases 1.1, 2.2 and 2.3, that (ξ,τ,σ) ∈ Γ3 in Case 1.2, and that (ξ,τ,σ) ∈ Γ30 in Case 2.1.

4. Proof of Theorem 1.1

In this section, we prove Theorem 1.1. In view of Proposition 2.1 and the beginning of the proof of Proposition 3.3, we aim to verify the sharp inequality

- (4.1)

(ξ,τ)∈F3q ξ1∈S ξ2,2τ−4ξ2

![image 234](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile234.png>)

![image 235](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile235.png>)

f(ξ1)f(ξ − ξ1)

2

≤ q + 1 −

1 q

![image 236](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile236.png>)

P2

|f|2

2

,

for every function f : P2 → C, with equality if f is constant. Here, P2 |f|2 := ξ∈F2

q

|f(ξ,ξ2)|2.

- Remark 4.1. In the spirit of Foschi [13, Eq.(13)] and Mockenhaupt–Tao [25, Lemma 5.1], it may seem natural to use the inequality


S(ξ2, 2τ−4ξ2) ≤ sup|S|, where the supremum is taken over all spheres S ⊂ F2q. By Cauchy–Schwarz, this would lead to

![image 237](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile237.png>)

![image 238](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile238.png>)

(ξ,τ)∈F3q ξ1∈S ξ2,2τ−4ξ2

![image 239](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile239.png>)

![image 240](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile240.png>)

f(ξ1)f(ξ − ξ1)

2

≤ sup|S|

(ξ,τ)∈F3q ξ1∈S ξ2,2τ−4ξ2

![image 241](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile241.png>)

![image 242](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile242.png>)

|f(ξ1)f(ξ − ξ1)|2

= sup|S|

P2

|f|2

2

,

- (4.2)


which is never sharp. Indeed, from Lemma 2.2 and Remark 2.3, it follows that sup|S| equals 2q − 1 if q ≡ 1(mod 4) and q + 1 if q ≡ 3(mod 4). This implies inequality (4.1) with constants 2q − 1 and q + 1, respectively, instead of the optimal q + 1 − 1/q. Thus a more reﬁned analysis is needed.

The analysis splits into two cases, depending on the congruence class of q modulo 4.

- 4.1. The case q ≡ 3(mod 4). In this case, −1 is not a square in Fq (Lemma 2.6) and spheres of radius zero in F2q are singletons (Remark 2.3). This simpliﬁes the analysis considerably. Decompose the ambient space F3q into the critical surface C2 := {(ξ,τ) ∈ F3q : 2τ = ξ2} and its complement, F3q \ C2. On the latter, an application of Cauchy–Schwarz similar to (4.2) yields

(ξ,τ)∈F3q\C2 ξ1∈S ξ2 ,2τ−4ξ2

![image 243](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile243.png>)

![image 244](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile244.png>)

f(ξ1)f(ξ − ξ1)

2

≤ (q + 1)

(ξ,τ)∈F3q\C2 ξ1∈S ξ2,2τ−4ξ2

![image 245](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile245.png>)

![image 246](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile246.png>)

|f(ξ1)f(ξ − ξ1)|2,

with equality if f is a constant function. We now add and subtract the contribution of the critical surface – a key step of mass transport ﬂavor which has already appeared in (3.18) and (3.26) – yielding

(ξ,τ)∈F3q ξ1∈S ξ2 ,2τ−4ξ2

![image 247](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile247.png>)

![image 248](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile248.png>)

f(ξ1)f(ξ − ξ1)

2

≤ (q + 1)

(ξ,τ)∈F3q ξ1∈S ξ2,2τ−4ξ2

![image 249](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile249.png>)

![image 250](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile250.png>)

|f(ξ1)f(ξ − ξ1)|2

+

(ξ,τ)∈C2

   ξ1∈S(ξ2,0)

![image 251](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile251.png>)

f(ξ1)f(ξ − ξ1)

2

− (q + 1)

ξ1∈S(ξ2,0)

![image 252](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile252.png>)

|f(ξ1)f(ξ − ξ1)|2

  .

(4.3)

The ﬁrst sum on the right-hand side of (4.3) can be computed as follows:

(ξ,τ)∈F3q ξ1∈S ξ2,2τ−4ξ2

![image 253](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile253.png>)

![image 254](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile254.png>)

|f(ξ1)f(ξ − ξ1)|2

=

ξ1,ξ2∈F2q

|f(ξ1)f(ξ2)|2

τ∈Fq

1 ξ1,ξ2 ∈ S ξ1+2ξ2, 2τ−(ξ1+ξ2)

![image 255](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile255.png>)

2

![image 256](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile256.png>)

(4.4) 4

=

ξ1,ξ2∈F2q

|f(ξ1)f(ξ2)|2 =

P2

|f|2

2

.

Indeed, for each given pair (ξ1,ξ2) ∈ (F2q)2, there exists a unique τ ∈ Fq such that (ξ1 − ξ2)2 = 2τ − (ξ1 + ξ2)2, and so the inner sum in (4.4) is equal to 1. On the other hand, since S(ξ2,0) = {ξ2}, the second sum on the right-hand side of (4.3) boils down to

![image 257](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile257.png>)

![image 258](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile258.png>)

(4.5)

(ξ,τ)∈C2

   ξ1∈S(ξ2,0)

![image 259](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile259.png>)

f(ξ1)f(ξ − ξ1)

2

− (q + 1)

ξ1∈S(ξ2,0)

![image 260](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile260.png>)

|f(ξ1)f(ξ − ξ1)|2

   = −q

P2

|f|4.

A second application of the Cauchy–Schwarz inequality yields

(4.6) q

P2

|f|4 ≥

1 q

![image 261](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile261.png>)

P2

|f|2

2

,

with equality if and only if |f| is constant. The desired inequality (4.1) follows from (4.3)–(4.6), and is sharp since constant functions turn each step of the proof into an equality. Finally, the cases of equality in (4.6) imply that any maximizer must necessarily have constant modulus. This concludes the proof of Theorem 1.1 when q ≡ 3(mod 4).

- 4.2. The case q ≡ 1(mod 4). In this case, −1 is a square in Fq (Lemma 2.6) and spheres of radius zero in F2q have 2q −1 elements (Remark 2.3). This complicates the analysis, which nonetheless starts


in a similar way to that of §4.1. Via Cauchy–Schwarz and mass transport, we have

2

2

|f|2

f(ξ1)f(ξ − ξ1)

≤ (q − 1)

(ξ,τ)∈F3q ξ1∈S ξ2,2τ−4ξ2

P2

![image 262](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile262.png>)

![image 263](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile263.png>)

- (4.7)

Equality in (4.7) is achieved if and only if

- (4.8) f(ξ1)f(ξ − ξ1) = C(ξ,τ), for every ξ1 ∈ S

ξ 2

![image 264](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile264.png>)

,

2τ − ξ2 4

![image 265](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile265.png>)

such that 2τ = ξ2.

- Remark 4.2. In the spirit of §4.1, one may try to estimate the left-hand side of (4.7) by Cauchy– Schwarz only, via the upper bound


(ξ,τ)∈F3q

S

ξ 2

![image 266](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile266.png>)

,

2τ − ξ2 4

![image 267](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile267.png>)

ξ1∈S ξ2,2τ−4ξ2

![image 268](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile268.png>)

![image 269](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile269.png>)

- (4.9) |f(ξ1)f(ξ − ξ1)|2.


   ξ1∈S(ξ2,0)

  .

2

|f(ξ1)f(ξ − ξ1)|2

− (q − 1)

+

f(ξ1)f(ξ − ξ1)

ξ1∈S(ξ2,0)

(ξ,τ)∈C2

![image 270](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile270.png>)

![image 271](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile271.png>)

However, for ﬁxed P2 |f|2, this expression is not maximized by constants. Indeed, consider the indicator function of the line (contained in P2) spanned by the vector (1,w,0) ∈ F3q, where w2 = −1, i.e., let f0 := 1(t(1,w,0) : t ∈ Fq). If (ξ,τ) = (t(1,w),0), then Remark 2.3 yields

S

ξ 2

,

![image 272](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile272.png>)

2τ − ξ2 4

![image 273](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile273.png>)

= S

t 2

(1,w),0 = 2q − 1.

![image 274](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile274.png>)

For any t ∈ Fq, we further have that

|f0(t1(1,w))|2|f0((t − t1)(1,w))|2 = q,

t1(1,w)∈S(2t(1,w),0)

![image 275](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile275.png>)

and so (4.9) equals q2(2q − 1) when f = f0. Since P2 |f0|2 = q, it then follows that

P2

|f0|2

−2

(ξ,τ)∈F3q

S

ξ 2

,

![image 276](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile276.png>)

2τ − ξ2 4

![image 277](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile277.png>)

ξ1∈S ξ2,2τ−4ξ2

![image 278](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile278.png>)

![image 279](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile279.png>)

|f0(ξ1)f0(ξ − ξ1)|2 = 2q − 1.

This implies inequality (4.1) with constant 2q − 1 instead of the optimal q + 1 − 1/q. Thus a more reﬁned analysis is needed.

We proceed to analyze the second summand on the right-hand side of (4.7), which is nothing but

(1.10) when d = k = 2. We will prove that it is maximized by constants for ﬁxed P2 |f|2, via the following four steps.

Step 1: Line decomposition. Let w ∈ Fq be such that w2 = −1 in Fq. Given (ξ,τ) ∈ C2, the sphere S(ξ2,0) is the union of the two lines

![image 280](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile280.png>)

L±(ξ) := ξ1 ∈ F2q : ξ1 =

ξ 2

+ t(1,±w), t ∈ Fq ,

![image 281](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile281.png>)

which intersect exactly at ξ2. Deﬁning the punctured lines L◦±(ξ) := L±(ξ) \ {ξ2}, we then have L◦−(ξ) ∪ L◦+(ξ) = S(ξ2,0) \ {ξ2}. Going back to (4.7), it follows that

![image 282](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile282.png>)

![image 283](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile283.png>)

![image 284](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile284.png>)

![image 285](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile285.png>)

2

2

f(ξ1)f(ξ − ξ1)

(ξ,τ)∈C2 ξ1∈S(ξ2,0)

![image 286](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile286.png>)

- (4.10)

We proceed to estimate the two summands on the right-hand side of (4.10). Step 2: Estimating the ﬁrst summand. Let us start with

ξ1∈L◦−(ξ)∪L◦+(ξ)

f(ξ1)f(ξ − ξ1)

2

=

ξ1∈L◦−(ξ)

f(ξ1)f(ξ − ξ1)

2

+

ξ1∈L◦+(ξ)

f(ξ1)f(ξ − ξ1)

2

+ 2ℜ

 

ξ1∈L◦−(ξ)

f(ξ1)f(ξ − ξ1)

ξ1∈L◦+(ξ)

![image 287](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile287.png>)

f(ξ1)f(ξ − ξ1)

 .

By Cauchy–Schwarz, it follows that

- (4.11) ξ1∈L◦±(ξ)

f(ξ1)f(ξ − ξ1)

2

≤ (q − 1)

ξ1∈L◦±(ξ)

|f(ξ1)f(ξ − ξ1)|2,

where equality holds if and only if f(ξ1)f(ξ−ξ1) = C±(ξ), for every ξ1 ∈ L◦±(ξ). Moreover, a repeated application of the elementary inequality 2xy ≤ x2 + y2 yields

- (4.12) ℜ

 

ξ1∈L◦−(ξ)

f(ξ1)f(ξ − ξ1)

ξ1∈L◦+(ξ)

![image 288](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile288.png>)

f(ξ1)f(ξ − ξ1)

  ≤

ξ1∈L◦−(ξ)

|f(ξ1)|2

ξ2∈L◦+(ξ)

|f(ξ2)|2.

Inequalities (4.11) and (4.12) together imply

ξ1∈L◦−(ξ)∪L◦+(ξ)

f(ξ1)f(ξ − ξ1)

2

≤ (q − 1)

ξ1∈L◦−(ξ)∪L◦+(ξ)

|f(ξ1)f(ξ − ξ1)|2 + 2

ξ1∈L◦−(ξ)

|f(ξ1)|2

ξ2∈L◦+(ξ)

|f(ξ2)|2,

and therefore

ξ1∈L◦−(ξ)∪L◦+(ξ)

f(ξ1)f(ξ − ξ1)

2

− (q − 1)

ξ1∈S(ξ2,0)

![image 289](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile289.png>)

|f(ξ1)f(ξ − ξ1)|2

≤ 2

ξ1∈L◦−(ξ)

|f(ξ1)|2

ξ2∈L◦+(ξ)

|f(ξ2)|2 − (q − 1) f ξ2

![image 290](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile290.png>)

4

.

- (4.13)


  f ξ2

4

+ 2ℜ

+

![image 291](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile291.png>)

(ξ,τ)∈C2

f(ξ1)f(ξ − ξ1)

=

(ξ,τ)∈C2 ξ1∈L◦−(ξ)∪L◦+(ξ)

 f ξ2

2

![image 292](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile292.png>)

![image 293](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile293.png>)

 

 .

f(ξ1)f(ξ − ξ1)

ξ1∈L◦−(ξ)∪L◦+(ξ)

Step 3: Estimating the second summand. We need the following estimate whose proof is omitted.

- Lemma 4.3. Let a,b,c ∈ C \ {0}. The following inequality holds


|a|2 2

(|b|2 + |c|2),

ℜ(a2bc) ≤

![image 294](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile294.png>)

![image 295](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile295.png>)

and equality holds if and only if Arg(a) = 21(Arg(b) + Arg(c)) and |b| = |c|.

![image 296](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile296.png>)

- Lemma 4.3 and symmetry considerations together yield


  ≤

 f ξ2

2

- 1

![image 297](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile297.png>)

- 2


2

![image 298](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile298.png>)

|f(ξ1)|2 + |f(ξ − ξ1)|2

f ξ2

f(ξ1)f(ξ − ξ1)

ℜ

![image 299](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile299.png>)

![image 300](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile300.png>)

ξ1∈L◦−(ξ)∪L◦+(ξ)

ξ1∈L◦−(ξ)∪L◦+(ξ)

2

- (4.14) |f(ξ1)|2.

Assuming that f never vanishes, equality holds in (4.14) if and only if

- (4.15) |f(ξ1)| = |f(ξ − ξ1)| and 2Arg f ξ2 = Arg(f(ξ1)) + Arg(f(ξ − ξ1)), for every ξ ∈ F2q and ξ1 ∈ L◦−(ξ) ∪ L◦+(ξ).

![image 301](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile301.png>)

Step 4: End of proof. From (4.13) and (4.14), we see that the second summand on the right-hand side of (4.7) is bounded by

(ξ,τ)∈C2

 2

ξ1∈L◦−(ξ)

|f(ξ1)|2

ξ2∈L◦+(ξ)

|f(ξ2)|2 + (2 − q) f ξ2

![image 302](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile302.png>)

4

+ 2 f ξ2

![image 303](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile303.png>)

2

ξ1∈L◦−(ξ)∪L◦+(ξ)

|f(ξ1)|2

 .

- (4.16)

This is equal to

2

ξ1,ξ2∈F2q

|f(ξ1)|2|f(ξ2)|2 − q

(ξ,τ)∈C2

f ξ2

![image 304](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile304.png>)

4

= 2

P2

|f|2

2

− q

P2

- (4.17) |f|4,

from where the desired sharp inequality (4.1) follows via (4.6). To verify that (4.16) and (4.17) indeed coincide, note that

ξ1∈L◦−(ξ)

|f(ξ1)|2

ξ2∈L◦+(ξ)

|f(ξ2)|2 + f ξ2

![image 305](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile305.png>)

4

+ f ξ2

![image 306](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile306.png>)

2

ξ1∈L◦−(ξ)∪L◦+(ξ)

|f(ξ1)|2

=

ξ1∈L−(ξ)

|f(ξ1)|2

ξ2∈L+(ξ)

|f(ξ2)|2.

Interchanging the order of summation, we further have that

(ξ,τ)∈C2 ξ1∈L−(ξ)

|f(ξ1)|2

ξ2∈L+(ξ)

|f(ξ2)|2 =

ξ1,ξ2∈F2q

|f(ξ1)|2|f(ξ2)|2

since

- (4.18)


= f ξ2

![image 307](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile307.png>)

ξ1∈L◦−(ξ)∪L◦+(ξ)

1(ξ1 ∈ L−(ξ),ξ2 ∈ L+(ξ)) = 1.

(ξ,τ)∈C2

To verify (4.18), note that the 4 × 4 matrix associated to the system of equations

- ξ1 = ξ2 + t1(1,w)

![image 308](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile308.png>)

- ξ2 = ξ2 + t2(1,−w)


![image 309](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile309.png>)

has nonzero determinant (equal to ±w/2) and therefore, given any pair (ξ1,ξ2) ∈ (F2q)2, there exists a unique ξ ∈ F2q, such that ξ1 ∈ L−(ξ) and ξ2 ∈ L+(ξ).

Constant functions turn every single step of the preceding proof into an equality and, as in §4.1, the cases of equality in (4.6) imply that any maximizer must necessarily have constant modulus. This concludes the proof of Theorem 1.1.

5. Proof of Theorem 1.2

In this section, we prove Theorem 1.2. It suﬃces to show that all maximizers of inequality (4.1) are of the form (1.7) when q ≡ 1(mod 4). This will follow from studying the functional equations satisﬁed by functions which saturate the intermediate inequalities from §4.2.

Let f⋆ : P2 → C be a maximizer of (4.1), which as usual is identiﬁed with its projection f⋆ : F2q → C. We have already observed that |f⋆| is constant (for otherwise (4.6) would be strict). Hence f⋆ = λρ⋆, where λ ∈ C \ {0} and ρ⋆ : F2q → S1 satisﬁes ρ⋆(0) = 1. From the second condition in (4.15), we have

- (5.1) ρ2⋆ ξ2 = ρ⋆(ξ1)ρ⋆(ξ − ξ1), for every ξ1 ∈ L+(ξ) ∪ L−(ξ). The next result is key towards the solution of the functional equation (5.1).

![image 310](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile310.png>)

Lemma 5.1. Let q = pn be the power of an odd prime. Let ρ : Fq → S1 be such that ρ(0) = 1 and

- (5.2) ρ(x)ρ(y) = ρ x+2y 2 , for every x,y ∈ Fq. Then there exists a unique a ∈ Fq, such that

![image 311](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile311.png>)

ρ(x) = exp

2πiTrn(ax) p

![image 312](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile312.png>)

, for every x ∈ Fq. Proof. In light of our discussion at the beginning of §2.2, it suﬃces to verify that

- (5.3) ρ(x + y) = ρ(x)ρ(y), for every x,y ∈ Fq. From (5.2), it follows that
- (5.4) ρ(tx) = ρ(x)t, for any (t,x) ∈ Fp × Fq. This is a direct consequence of the following chain of identities:

ρ((t + 1)x) = ρ((t + 1)x)ρ(0) = ρ t+12 x 2 = ρ(x)ρ(tx). Since px = 0 for every x ∈ Fq, from (5.4) it then follows that

![image 313](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile313.png>)

- (5.5) 1 = ρ(0) = ρ(px) = ρ(x)p.

On the other hand, (5.4) implies ρ(2x) = ρ(x)2 and so ρ(x)2ρ(y)2 = ρ(2x)ρ(2y) = ρ(x+y)2. Therefore ρ(x)ρ(y) = ±ρ(x + y). But if ρ(x)ρ(y) = −ρ(x + y), then (ρ(x)ρ(y))p+1 = ρ(x + y)p+1, which by (5.5) would imply ρ(x)ρ(y) = ρ(x + y). This leads to a contradiction since p > 2 and ρ is nonzero. Thus

- (5.3) holds, as desired. By (5.1) and Lemma 5.1, there exist unique a,b ∈ Fq such that, for every η,ζ ∈ Fq,


ρ⋆|L+(0)(η(1,w)) = exp

2πiTrn(aη) p

![image 314](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile314.png>)

- (5.6) ,

ρ⋆|L−(0)(ζ(1,−w)) = exp

2πiTrn(bζ) p

![image 315](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile315.png>)

- (5.7) .

More generally, let {e1,... ,en} be a basis of the vector space Fq over Fp. By Lemma 5.1, there exists a unique n-tuple (v1,... ,vn) ∈ Fnq such that, for every i ∈ {1,... ,n} and η ∈ Fq,

ρ⋆ ρ⋆(ei(1,−w)) L+(2ei(1,−w))

![image 316](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile316.png>)

(η(1,w) + ei(1,−w)) = exp

2πiTrn(viη) p

![image 317](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile317.png>)

- (5.8) .

Similarly, given any η(1,w) ∈ L+(0), there exist a unique vη ∈ Fq such that ρ⋆ ρ⋆(η(1,w)) L−(2η(1,w))

![image 318](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile318.png>)

(η(1,w) + ζ(1,−w)) = exp

2πiTrn(vηζ) p

![image 319](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile319.png>)

- (5.9) , for every ζ ∈ Fq. Identities (5.6)–(5.9) together imply


2πiTrn(vηei) p

2πiTrn(vηei) p

2πiTrn(aη) p

exp

= ρ⋆(η(1,w))exp

= ρ⋆(η(1,w) + ei(1,−w))

exp

![image 320](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile320.png>)

![image 321](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile321.png>)

![image 322](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile322.png>)

2πiTrn(viη) p

2πiTrn(viη) p

2πiTrn(bei) p

= exp

. It follows that

ρ⋆(ei(1,−w)) = exp

exp

![image 323](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile323.png>)

![image 324](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile324.png>)

![image 325](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile325.png>)

Trn(aη) + Trn(vηei) = Trn(viη) + Trn(bei),

for every i ∈ {1,... ,n}. The next result allows us to gain further control over the element vη.

- Lemma 5.2. Let {e1,... ,en} be a basis of the vector space Fq over Fp. Let t1,... tn ∈ Fp. Then there exists a unique a ∈ Fq such that Trn(aei) = ti, for every i ∈ {1,... ,n}.


Proof. Each a ∈ Fq gives rise to a unique n-tuple (Trn(aei))ni=1. Indeed, Trn(aei) = Trn(bei) for all i ∈ {1,... ,n} implies Trn(a·) = Trn(b·), and therefore a = b; see [24, Theorem 2.24]. The map a  → (Trn(aei))ni=1 is thus injective from Fq to Fnp. To conclude, note that |Fq| = |Fnp|.

By Lemma 5.2, vη is the unique element in Fq such that Trn(vηei) = Trn((vi − a)η + bei), for every i ∈ {1,... ,n}. Consequently, if ζ = ni=1 λiei, for some λi ∈ Fp, then

- (5.10) Trn(vηζ) = Trn

n

i=1

λi(vi − a)η + bζ .

From (5.6) and (5.9)–(5.10), it follows that ρ⋆(η(1,w) + ζ(1,−w)) = ρ⋆(η(1,w))

ρ⋆(η(1,w) + ζ(1,−w)) ρ⋆(η(1,w))

![image 326](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile326.png>)

= ρ⋆(η(1,w))exp

2πiTrn(vηζ) p

![image 327](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile327.png>)

= exp

2πiTrn(aη) p

![image 328](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile328.png>)

exp

2πiTrn( ni=1 λi(vi − a)η + bζ) p

![image 329](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile329.png>)

= exp

2πiTrn(aη + bζ + L(ζ)η) p

![image 330](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile330.png>)

,

- (5.11)

where L : Fq → Fq is the Fp-linear map whose matrix representation with respect to the basis {e1,... ,en} has columns (vi − a)ni=1. We proceed to investigate the map L, with the goal of showing that L(ζ) = L(1)ζ, for every ζ ∈ Fq.

From (4.8), given (ξ,s) ∈ F2q × F×q , we know that

- (5.12) f⋆(ξ1)f⋆(ξ − ξ1) = C(ξ,s), for every ξ1 ∈ S ξ2,s .

![image 331](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile331.png>)

Writing ξ = η(1,w) + ζ(1,−w) and ξ1 = η1(1,w) + ζ1(1,−w), condition (5.12) can be rewritten in terms of the function ρ⋆ as follows:

ρ⋆((η − η1)(1,w) + (ζ − ζ1)(1,−w))ρ⋆(η1(1,w) + ζ1(1,−w)) = exp

2πiC(η,ζ,s) p

![image 332](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile332.png>)

- (5.13) ,


whenever s = ((η1 − η2)(1,w) + (ζ1 − ζ2)(1,−w))2 = (2η1 − η)(2ζ1 − ζ) is nonzero. From (5.11) and

![image 333](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile333.png>)

![image 334](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile334.png>)

- (5.13), we then have

C(η,ζ,s) =Trn(aη1 + bζ1 + L(ζ1)η1) + Trn(a(η − η1) + b(ζ − ζ1) + L(ζ − ζ1)(η − η1))

=Trn(aη + bζ + L(ζ1)η1 + L(ζ − ζ1)(η − η1)), whenever (2η1 − η)(2ζ1 − ζ) = s is nonzero. Noting that

L(ζ1)η1 + L(ζ − ζ1)(η − η1) −

- 1

![image 335](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile335.png>)

- 2


L(ζ)η =

- 1

![image 336](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile336.png>)

- 2


L(ζ − 2ζ1)(η − 2η1), we then have

- (5.14) Trn(L(ζ − 2ζ1)(η − 2η1)) = C(η,ζ,s),

whenever (2η1 − η)(2ζ1 − ζ) = s is nonzero. Writing u = ζ − 2ζ1, the latter constraint becomes η − 2η1 = s/u, and so (5.14) boils down to

- (5.15) Trn (sL(u)/u) = C(η,ζ,s),

where u = 0 is now a free variable. In particular, the left-hand side of (5.15) and therefore its right-hand side are actually independent of η,ζ. Therefore the choice u = 1 leads to

- (5.16) Trn (s (L(u)/u − L(1))) = 0, for every s,u ∈ F×q .


From Lemma 5.2, it then follows that L(u) = L(1)u, for every u ∈ Fq. This concludes the proof of Theorem 1.2.

6. Proof of Theorem 1.3 In this section, we prove Theorem 1.3. In view of Proposition 2.1, we aim to verify that

2

3

1 q

|f|2

,

≤ q + 1 −

f(ξ1)f(ξ2)f(ξ3)

- (6.1) (ξ,τ)∈F2q (ξ1,ξ2,ξ3)∈Σ3P1(ξ,τ)


![image 337](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile337.png>)

P1

|f(ξ,ξ2)|2. As in §4, we split the sum on the left-hand side of (6.1) into the contribution from the critical curve,

for every function f : P1 → C. Here, P1 |f|2 := ξ∈F

q

C1 := ξ, ξ32 : ξ ∈ Fq ,

![image 338](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile338.png>)

and from its complement, F2q \ C1. By Proposition 3.3, the cardinality of Σ3P1(ξ,τ) is constant in each of these sets. The sum over F2q \ C1 can be controlled by a direct application of Cauchy–Schwarz:

2

2

≤

f(ξ1)f(ξ2)f(ξ3)

f(ξ1)f(ξ2)f(ξ3)

(ξ,τ)∈F2q (ξ1,ξ2,ξ3)∈Σ3P1(ξ,τ)

(ξ,τ)∈C1 (ξ1,ξ2,ξ3)∈Σ3P1(ξ,τ)

- (6.2)

The critical curve C1 requires a more delicate analysis depending on the geometry of the sets Σ3P1(ξ,τ), which we proceed to explore.

Let (ξ,τ) ∈ C1 and (ξ1,ξ2,ξ3) ∈ Σ3P1(ξ,τ). From the proof of Proposition 3.3, we can write (ξ1,ξ2,ξ3) =

1 3

![image 339](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile339.png>)

(ξ,ξ,ξ) + (η1,η2,−η1 − η2), for some η1,η2 ∈ Fq, in which case identity (3.12) boils down to

- (6.3) η12 + η1η2 + η22 = 0.

If q ≡ 2(mod 3), then −3 is not a square in Fq (recall Lemma 2.6) and equation (6.3) has no nonzero solutions. If q ≡ 1(mod 3), then −3 is a square in Fq, and the solutions of (6.3) can be parametrized by

(η1,η2) = ℓ(j,1), where ℓ ∈ F×q and j2 + j + 1 = 0. The analysis thus splits into two cases, depending on the congruence class of q modulo 3.

6.1. The case q ≡ 2(mod 3). In this case, Σ3P1(ξ,τ) = 13 (ξ,ξ,ξ) whenever (ξ,τ) ∈ C1. This simple structure simpliﬁes the analysis signiﬁcantly. Invoking (3.14), the right-hand side of(6.2) can then be

![image 340](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile340.png>)

bounded by

(ξ,τ)∈C1

f 3 ξ

![image 341](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile341.png>)

6

+ (q + 1)

(ξ,τ)∈F2q\C1 (ξ1,ξ2,ξ3)∈Σ3P1(ξ,τ)

|f(ξ1)f(ξ2)f(ξ3)|2

= (q + 1)

(ξ,τ)∈F2q (ξ1,ξ2,ξ3)∈Σ3P1(ξ,τ)

|f(ξ1)f(ξ2)f(ξ3)|2 − q

(ξ,τ)∈C1

f 3 ξ

![image 342](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile342.png>)

6

.

- (6.4)

Interchanging the order of summation as in (4.4), we have that

- (6.5) (ξ,τ)∈F2q (ξ1,ξ2,ξ3)∈Σ3P1(ξ,τ)

|f(ξ1)f(ξ2)f(ξ3)|2 =

P1

|f|2

3

,

On the other hand, H¨older’s inequality yields

- (6.6)


|f(ξ1)f(ξ2)f(ξ3)|2.

Σ3P1(ξ,τ)

+

(ξ,τ)∈F2q\C1

(ξ1,ξ2,ξ3)∈Σ3P1(ξ,τ)

3

1 q2

6

f 3 ξ

|f|2

|f|6 ≥

.

=

![image 343](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile343.png>)

![image 344](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile344.png>)

P1

P1

(ξ,τ)∈C1

Combining (6.5)–(6.6) with (6.2) and 6.4, we obtain the sharp inequality (6.1). As before, maximizers necessarily have constant modulus. This concludes the proof of Theorem 1.3 when q ≡ 2(mod 3).

- 6.2. The case q ≡ 1(mod 3). In this case, the right-hand side of(6.2) can be bounded by


2

|f(ξ1)f(ξ2)f(ξ3)|2

f(ξ1)f(ξ2)f(ξ3)

+ (q − 1)

(ξ,τ)∈C1 (ξ1,ξ2,ξ3)∈Σ3P1(ξ,τ)

(ξ,τ)∈F2q\C1 (ξ1,ξ2,ξ3)∈Σ3P1(ξ,τ)

 

   (ξ1,ξ2,ξ3)∈Σ3P1(ξ,τ)

2

|f(ξ1)f(ξ2)f(ξ3)|2

- (6.7) 

+ (q − 1)

P1

|f|2

3

.

Remark 6.1. In order to handle (6.7), it is not enough to use Cauchy–Schwarz directly. In light of (3.13), |Σ3P1(ξ,τ)| = 2q − 1 for all (ξ,τ) ∈ C1, and so the resulting upper bound would be

q

(ξ,τ)∈C1 (ξ1,ξ2,ξ3)∈Σ3P1(ξ,τ)

|f(ξ1)f(ξ2)f(ξ3)|2,

which is not bounded by the value attained by constant functions, (2 − 1/q) P1 |f|2 3. To see this, it suﬃces to consider the case when f = δ0 is a Dirac delta at the origin.

We proceed to analyze (6.7), which coincides with (1.10) when (d,k) = (1,3). We will prove that it is maximized by constants for ﬁxed P1 |f|2, via the following six steps.

- Step 1: Line decomposition. Let j± denote the two distinct roots of the polynomial j2 + j + 1 in

Fq. If (ξ,τ) ∈ C1, then Σ3P1(ξ,τ) is the union of the two lines L±(ξ) := {13(ξ,ξ,ξ) + ℓ(j±,1,−1 − j±) : ℓ ∈ Fq},

![image 345](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile345.png>)

which intersect exactly at 31(ξ,ξ,ξ). Given g : Fq → C, a key observation which is particular to this L2 → L6 setting is that

![image 346](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile346.png>)

(ξ1,ξ2,ξ3)∈L+(ξ)

g(ξ1)g(ξ2)g(ξ3) =

(ξ1,ξ2,ξ3)∈L−(ξ)

(6.8) g(ξ1)g(ξ2)g(ξ3).

Indeed, every element of L−(ξ) is a permutation of an element of L+(ξ) since j−j+ = 1 implies j−(j+,1,−1 − j+) = (1,j−,−1 − j−). Writing L◦±(ξ) := L±(ξ) \ {13(ξ,ξ,ξ)}, the term inside the outer sum in (6.7) then equals (6.9)

![image 347](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile347.png>)

2

(ξ1,ξ2,ξ3)∈L◦+(ξ)

f(ξ1)f(ξ2)f(ξ3) + f 3 ξ

![image 348](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile348.png>)

3

2

−(q −1)

 2

(ξ1,ξ2,ξ3)∈L◦+(ξ)

|f(ξ1)f(ξ2)f(ξ3)|2 + f 3 ξ

![image 349](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile349.png>)

6

 ,

which is the same as

4

(ξ1,ξ2,ξ3)∈L◦+(ξ)

f(ξ1)f(ξ2)f(ξ3)

2

− (q − 2) f 3 ξ

![image 350](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile350.png>)

6

+ 4ℜ

 f 3 ξ

![image 351](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile351.png>)

![image 352](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile352.png>)

3

(ξ1,ξ2,ξ3)∈L◦+(ξ)

f(ξ1)f(ξ2)f(ξ3)

  − 2(q − 1)

(ξ1,ξ2,ξ3)∈L◦+(ξ)

|f(ξ1)f(ξ2)f(ξ3)|2 .

(6.10)

- Step 2: Intermediate inequalities. The ﬁrst summand in (6.10) can be estimated by Cauchy–Schwarz:




− (q − 1)

=

f(ξ1)f(ξ2)f(ξ3)

(ξ1,ξ2,ξ3)∈Σ3P1(ξ,τ)

(ξ,τ)∈C1

f(ξ1)f(ξ2)f(ξ3)

(ξ1,ξ2,ξ3)∈L◦+(ξ)

2

|f(ξ1)f(ξ2)f(ξ3)|2 .

≤ (q − 1)

(ξ1,ξ2,ξ3)∈L◦+(ξ)

The third summand in (6.10) can be estimated via the triangle inequality:

  ≤ f 3 ξ

 f 3 ξ

3

3

![image 353](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile353.png>)

f(ξ1)f(ξ2)f(ξ3)

|f(ξ1)f(ξ2)f(ξ3)| .

ℜ

![image 354](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile354.png>)

![image 355](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile355.png>)

(ξ1,ξ2,ξ3)∈L◦+(ξ)

(ξ1,ξ2,ξ3)∈L◦+(ξ)

It follows that (6.7) is bounded by

2

6

− (q − 2) f 3 ξ

2

f(ξ1)f(ξ2)f(ξ3)

![image 356](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile356.png>)

(ξ1,ξ2,ξ3)∈L◦+(ξ)

(ξ,τ)∈C1

- (6.11)

with equality if f is constant. Step 3: Analyzing the ﬁrst term in (6.11). Interchanging the order of summation,

(ξ,τ)∈C1 (ξ1,ξ2,ξ3)∈L◦+(ξ)

f(ξ1)f(ξ2)f(ξ3)

2

=

(ξ1,ξ2,ξ3)∈F3q (η1,η2,η3)∈F3q

f(ξ1)f(ξ2)f(ξ3)f(η1)f(η2)f(η3)m(ξ1,ξ2,ξ3,η1,η2,η3),

![image 357](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile357.png>)

- (6.12)

where

m(ξ1,ξ2,ξ3,η1,η2,η3) :=

(ξ,τ)∈C1

1((ξ1,ξ2,ξ3),(η1,η2,η3) ∈ L◦+(ξ)).

The function m takes values in {0,1}, and it equals 1 if and only if there exist u,v ∈ F×q , such that

 



ξ1 + ξ2 + ξ3 = η1 + η2 + η3 =: 3ζ

(ξ1,ξ2,ξ3) = (ζ + uj+,ζ + u,ζ − u − uj+) (η1,η2,η3) = (ζ + vj+,ζ + v,ζ − v − vj+)

- (6.13)

We proceed to analyze the set A := m−1(1), and claim the existence of (explicit) functions ω1 : F2q \ {(ℓ,ℓ) : ℓ ∈ Fq} → Fq and ω2,ω3 : B → Fq, where B ⊂ F3q is deﬁned as

- (6.14) B := (ℓ1,ℓ2,ℓ3) ∈ F3q : ℓ1 = ℓ2 and ℓ3 =

ℓ2j+ − ℓ1 j+ − 1

![image 358](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile358.png>)

, such that

- (6.15) A = {(ξ1,ξ2,ω1(ξ1,ξ2),η1,ω2(ξ1,ξ2,η1),ω3(ξ1,ξ2,η1)) : (ξ1,ξ2,η1) ∈ B}. Indeed, any non-diagonal pair (ξ1,ξ2) ∈ F2q deﬁnes a unique center ζ = ζ(ξ1,ξ2) ∈ Fq and a unique

- nonzero height u = u(ξ1,ξ2) ∈ F×q such that (ξ1,ξ2) = (ζ + uj+,ζ + u). If (ξ1,ξ2,ξ3,η1,η2,η3) ∈ A, then ξ3 = ζ − u − uj+ =: ω1(ξ1,ξ2). In particular, ζ = ξ2jj+−ξ1

![image 359](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile359.png>)

+−1 . Moreover, any η1 = ζ deﬁnes a unique

- nonzero height v = v(ξ1,ξ2,η1) ∈ F×q , such that η1 = ζ + vj+ and η2 = ζ + v =: ω2(ξ1,ξ2,η1) and η3 = ζ −v −vj+ =: ω3(ξ1,ξ2,η1). The claim follows, as does the fact that (ω1,ω2,ω3) : B → B′ deﬁnes a bijection between the set B from (6.14) and


B′ := (ℓ1,ℓ2,ℓ3) ∈ F3q : ℓ2 = ℓ3 andℓ1 =

ℓ3 + ℓ2 + ℓ2j+ 2 + j+

![image 360](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile360.png>)

.

Write (ω4,ω5,ω6) = (ω1,ω2,ω3)−1 : B′ → B, and observe that the function ω6 depends only on the last two coordinates of B′. In fact, given η2 = η3, if (ξ1,ξ2,η1) is such that ω2(ξ1,ξ2,η1) = η2 and ω3(ξ1,ξ2,η1) = η3, then (η1,η2,η3) = (ζ + vj+,ζ + v,ζ − v − vj+), and consequently

ω6(ξ3,η2,η3) = η1 = ζ − (1 + j+) −vj+ 1 + j+

![image 361](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile361.png>)

= ω1 ζ + j+ −vj+ 1 + j+

![image 362](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile362.png>)

,ζ + −vj+ 1 + j+

![image 363](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile363.png>)

= ω1(ζ + v,ζ − j+ − vj+) = ω1(η2,η3).

- (6.16)


3

+4 f ξ3

|f(ξ1)f(ξ2)f(ξ3)| ,

![image 364](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile364.png>)

(ξ1,ξ2,ξ3)∈L◦+(ξ)

Step 4: Bounding (6.12). Let ω1 = ω1(ξ1,ξ2), ω2 = ω2(ξ1,ξ2,η1), ω3 = ω3(ξ1,ξ2,η1) be as in the previous step. By (6.15), the right-hand side of (6.12) equals

![image 365](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile365.png>)

f(ξ1)f(ξ2)f(ω1)f(η1)f(ω2)f(ω3)

(ξ1,ξ2,η1)∈B

 

 

- 1

![image 366](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile366.png>)

- 2


|f(ξ1)f(ξ2)f(η1)|2 + |f(ω1)f(ω2)f(ω3)|2

≤

- (6.17)

Since ζ(ξ1,ξ2) = 13(ξ1 + ξ2 + ω1(ξ1,ξ2)), we have that

![image 367](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile367.png>)

(ξ1,ξ2,η1)∈B

|f(ξ1)f(ξ2)f(η1)|2 =

(ξ1,ξ2,η1)∈F3q

|f(ξ1)f(ξ2)f(η1)|2

−

(ξ1,η1)∈F2q

|f(ξ1)|4|f(η1)|2 −

ξ1 =ξ2

f(ξ1)f(ξ2)f ξ1+ξ2+ω31(ξ1,ξ2)

![image 368](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile368.png>)

2

.

- (6.18)

Invoking the fact that ω6 = ω1, recall (6.16), we further have that

(ξ3,η2,η3)∈B′

|f(ξ3)f(η2)f(η3)|2 =

(ξ3,η2,η3)∈F3q

|f(ξ3)f(η2)f(η3)|2

−

(ξ3,η2)∈F2q

|f(η2)|4|f(ξ3)|2 −

η2 =η3

f(η2)f(η3)f η2+η3+ω31(η2,η3)

![image 369](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile369.png>)

2

.

- (6.19)

Estimates (6.17)–(6.19) together imply that (6.12) is bounded by

P1

|f|2

3

−

P1

|f|2

P1

|f|4 −

ξ1 =ξ2

f(ξ1)f(ξ2)f ξ1+ξ2+ω31(ξ1,ξ2)

![image 370](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile370.png>)

2

- (6.20) ,

with equality if f is constant. Step 5: Bounding the last term in (6.11). Interchanging the order of summation,

(ξ,τ)∈C1

f 3 ξ

![image 371](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile371.png>)

3

(ξ1,ξ2,ξ3)∈L◦+(ξ)

|f(ξ1)f(ξ2)f(ξ3)|

=

(ξ1,ξ2,ξ3)∈F3q

|f(ξ1)f(ξ2)f(ξ3)|

(ξ,τ)∈C1

f 3 ξ

![image 372](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile372.png>)

3

1((ξ1,ξ2,ξ3) ∈ L◦+(ξ)).

- (6.21)

By the previous steps, (ξ1,ξ2,ξ3) ∈ L◦+(ξ) if and only if ξ = ξ1 + ξ2 + ω1(ξ1,ξ2) and ξ1 = ξ2 and ξ3 = ω1(ξ1,ξ2). Therefore, (6.21) equals

ξ1 =ξ2

|f(ξ1)f(ξ2)f(ω1(ξ1,ξ2))| f ξ1+ξ2+ω31(ξ1,ξ2)

![image 373](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile373.png>)

3

- (6.22) .

Step 6: End of proof. The bounds (6.20) and (6.22) combine in (6.11) to yield the following upper bound for (6.7):

2

P1

|f|2

3

− 2

P1

|f|2

P1

|f|4 − 2

ξ1 =ξ2

f(ξ1)f(ξ2)f ξ1+ξ2+ω31(ξ1,ξ2)

![image 374](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile374.png>)

2

− (q − 2)

P1

|f|6 + 4

ξ1 =ξ2

|f(ξ1)f(ξ2)f(ω1(ξ1,ξ2))| f ξ1+ξ2+ω31(ξ1,ξ2)

![image 375](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile375.png>)

3

,

- (6.23)


(ξ1,ξ2,η1)∈B

 

 .

- 1

![image 376](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile376.png>)

- 2


|f(ξ1)f(ξ2)f(η1)|2 +

|f(ξ3)f(η2)f(η3)|2

=

(ξ3,η2,η3)∈B′

(ξ1,ξ2,η1)∈B

with equality when f is constant. We further have that 2

3

|f(ξ1)f(ξ2)f(ω1(ξ1,ξ2))| f ξ1+ξ2+ω31(ξ1,ξ2)

![image 377](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile377.png>)

ξ1 =ξ2

- (6.24)


2

f(ξ1)f(ξ2)f ξ1+ξ2+ω31(ξ1,ξ2)

|f(ω1(ξ1,ξ2))|2 f ξ1+ξ2+ω31(ξ1,ξ2)

≤

+

![image 378](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile378.png>)

![image 379](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile379.png>)

ξ1 =ξ2

ξ1 =ξ2

4

.

The map (ξ1,ξ2)  → ω1(ξ1,ξ2), 13(ξ1 + ξ2 + ω1(ξ1,ξ2)) is a bijection from the set F2q \ {(ℓ,ℓ) : ℓ ∈ Fq} onto itself. Indeed, ζ = 31(ξ1 + ξ2 + ω1(ξ1,ξ2)) and (ξ1,ξ2,ω1(ξ1,ξ2)) = (ζ + uj+,ζ + u,ζ − (1 + j+)u). Knowing ω1(ξ1,ξ2) and 13(ξ1 + ξ2 + ω1(ξ1,ξ2)), we thus recover u,ζ and ξ1,ξ2. It follows that the map in question is injective, and therefore a bijection. Hence

![image 380](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile380.png>)

![image 381](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile381.png>)

![image 382](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile382.png>)

|f(ω1(ξ1,ξ2))|2 f ξ1+ξ2+ω31(ξ1,ξ2)

![image 383](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile383.png>)

ξ1 =ξ2

4

|f(ξ1)|2|f(ξ2)|4.

=

ξ1 =ξ2

This identity together with (6.24) implies that (6.23) is bounded by

2

P1

|f|2

3

− 2

P1

|f|2

P1

|f|4 − (q − 2)

P1

|f|6 + 2

= 2

P1

|f|2

3

− q

P1

|f(ξ1)|2|f(ξ2)|4

ξ1 =ξ2

|f|6.

A ﬁnal application of H¨older’s inequality as in (6.6) yields the sharp inequality (6.1), and maximizers again have constant modulus. This concludes the proof of Theorem 1.3 when q ≡ 1(mod 3).

7. Proof of Theorem 1.4

The proof of Theorem 1.4 parallels that of Theorem 1.1 when q ≡ 1(mod 4) and that of Theorem 1.2, and so we only highlight the necessary changes.

Let q = pn be an arbitrary power of an odd prime. Firstly, the two-fold convolution of normalized counting measure σ = σH2 is given by

2q − 1, if τ = ξ⊙2ξ, q − 1, otherwise,

1 q ×

![image 384](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile384.png>)

- (7.1) (σ ∗ σ)(ξ,τ) =


![image 385](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile385.png>)

where ξ ⊙ ξ := ξ12 − ξ22 if ξ = (ξ1,ξ2) ∈ F2q. Secondly, inequality (1.12) is equivalent to

- (7.2) (ξ,τ)∈F3q ξ1∈H(ξ2,2τ−4ξ⊙ξ)

![image 386](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile386.png>)

![image 387](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile387.png>)

f(ξ1)f(ξ − ξ1)

2

≤ q + 1 −

1 q

![image 388](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile388.png>)

H2

|f|2

2

,

where H2 |f|2 := ξ∈F2

q

|f(ξ,ξ ⊙ ξ)|2 and, given (γ,s) ∈ Fdq × Fq, we deﬁne the saddle

- (7.3) H(γ,s) := {η ∈ Fdq : (γ − η) ⊙ (γ − η) = s}.

Thirdly, the critical surface is now C2 := {(ξ,τ) ∈ F3q : 2τ = ξ ⊙ ξ} and, given (ξ,τ) ∈ C2, the saddle H(ξ2,0) is the union of the two lines

![image 389](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile389.png>)

- (7.4) L±(ξ) := ξ1 ∈ F2q : ξ1 =


ξ 2

+ t(1,±1), t ∈ Fq ,

![image 390](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile390.png>)

which intersect exactly at ξ/2. The rest of the argument goes through as in §4.1 without further changes, leading to the sharp inequality (1.12).

The characterization of maximizers follows the same steps as the ones in §5. From the proof outlined in the previous paragraph, any maximizer f⋆ of (7.2) has constant modulus, whence f⋆ = λρ⋆ with ρ⋆ : F2q → S1 and λ ∈ C \ 0. From Lemma 5.1 and the functional equation derived from the cases of

equality in (7.2), it follows that ρ⋆ is a character over any line L±(ξ). We are then able to conclude that there exist unique a,b ∈ Fq, such that

2πiTrn(aη + bζ + L(ζ)η) p

- (7.5) , for every η,ζ ∈ Fq,

for a certain Fp-linear map L : Fq → Fq. We want to verify that L(ζ) = L(1)ζ, for all ζ ∈ Fq. From the equality cases of the intermediate inequalities required for (7.2), we obtain

ρ⋆((η − η1)(1,1) + (ζ − ζ1)(1,−1))ρ⋆(η1(1,1) + ζ1(1,−1)) = exp

2πiC(η,ζ,s) p

![image 391](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile391.png>)

- (7.6)


ρ⋆(η(1,1) + ζ(1,−1)) = exp

![image 392](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile392.png>)

whenever s = ξ ⊙ ξ = (2η1 − η)(2ζ1 − ζ) is nonzero, where ξ = (η1 − η2)(1,1) + (ζ1 − 2ζ)(1,−1). From

![image 393](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile393.png>)

![image 394](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile394.png>)

- (7.5) and (7.6), it follows that C(η,ζ,s) =Trn(aη1 + bζ1 + L(ζ1)η1) + Trn(a(η − η1) + b(ζ − ζ1) + L(ζ − ζ1)(η − η1))

=Trn(aη + bζ + L(ζ1)η1 + L(ζ − ζ1)(η − η1))

whenever s = (2η1−η)(2ζ1−ζ) is nonzero. From this point onwards, the proof follows that of Theorem 1.2 line by line. This concludes the proof of Theorem 1.4.

8. Proof of Theorem 1.5

In this section, we prove Theorem 1.5. Let q ≡ 3(mod 4). From Lemma 3.5, it follows that |Γ3| = (q − 1)(q2 + 1). In view of Proposition 2.1, we aim to establish the sharp inequality

η∈F4q η1,η2∈Γ3 η1+η2=η

f(η1)f(η2)

2

≤

q5 − 2q4 + 2q3 − 3q + 3 (q − 1)(q2 + 1)

![image 395](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile395.png>)

Γ3

|f|2

2

- (8.1) ,


for every function f : Γ3 → C. Here, Γ3 |f|2 := τσ=ξ2 |f(ξ,τ,σ)|2.

Our approach can be summarized as follows. We decompose F4q into the three disjoint subsets where the two-fold convolution is constant: Γ3, {0}, and F4q \ Γ30; recall Proposition 3.6. A direct application of the Cauchy–Schwarz inequality suﬃces to handle the complement of Γ30. Points in the cone Γ3 require knowledge of the preimages of the corresponding two-fold convolution, combined with Cauchy–Schwarz. Crucially, these preimages correspond to disjoint punctured lines that folliate the cone. The contribution from the origin is dealt with in a similar way, taking into account the higher number of antipodal pairs. We proceed to establish (8.1) in the course of the following four steps.

Step 1: Slicing the cone. Deﬁne the sets

- S1 := {(ξ,τ,σ) ∈ F4q : ξ2 = τσ = 1},
- S2 := {(ξ,τ,σ) ∈ F4q : ξ2 = τσ = −1}.


Given i ∈ {1,2}, let Si∗ ⊂ Si be such that, for each pair {η,−η} ⊂ Si, one and only one element of {η,−η} belongs to Si∗. Further deﬁne S3∗ := {(0,1,0),(0,0,1)}. Each point η ∈ Si∗, i ∈ {1,2,3}, deﬁnes a punctured line Lη := {αη : α ∈ F×q }, and lines corresponding to distinct points do not intersect. Indeed, if (ξ1,τ1,σ1) = η1 ∈ S1∗ and (ξ2,τ2,σ2) = η2 ∈ S2∗, then (αξ1)2 is a square in Fq, whereas ξ22 is not. Moreover, if η1 = η2 are such that η1,η2 ∈ S1 and αξ1 = ξ2, then α2 = α2ξ21 = ξ22 = 1. Thus α = −1 and {η1,−η1} ⊂ S1∗, which is absurd. The case of η1,η2 ∈ S2 is analogous. The disjointness of the lines generated by the elements of S3∗ is immediate. Letting S∗ = S1∗ ∪ S2∗ ∪ S3∗, we then have that Γ3 equals the disjoint union of all punctured lines indexed by elements of S∗,

Γ3 =

- (8.2) Lη.


η∈S∗

Indeed, given (ξ,τ,σ) ∈ Γ3 such that ξ2 = t2 for some t ∈ F×q , then t−1 (ξ,τ,σ) ∈ S1, and thus t−1 (ξ,τ,σ) ∈ S1∗ or −t−1 (ξ,τ,σ) ∈ S1∗. On the other hand, if 0 = ξ2 = t2 for all t ∈ F×q , then there exists t0 ∈ F×q such that −t20 = ξ2, since {t2 : t ∈ F×q } and {−t2 : t ∈ F×q } are disjoint subsets of F×q

with (q −1)/2 elements each; in particular, t−0 1 (ξ,τ,σ) ∈ S2. Finally, if ξ2 = 0, then τ−1(ξ,τ,σ) ∈ S3∗ or σ−1(ξ,τ,σ) ∈ S3∗, and (8.2) follows. As a consequence, given η ∈ Γ3 and s ∈ S∗ such that η = αs for some α = 0, we have that

- (8.3) {(η1,η2) ∈ (Γ3)2 : η1 + η2 = η} = {(βs,(α − β)s) : β ∈ F×q \ {α}}.

Indeed, the right-hand side of (8.3) contains q − 2 elements of the left-hand side. That these are all follows from (3.32).

Step 2: Mass transport. The decomposition F4q = (F4q \ Γ30) ∪ Γ3 ∪ {0} and two applications of Cauchy–Schwarz together with Proposition 3.6 lead to

η∈F4q η1,η2∈Γ3 η1+η2=η

f(η1)f(η2)

2

≤ q(q − 1)

η∈F4q\Γ30 η1,η2∈Γ3 η1+η2=η

|f(η1)f(η2)|2

+(q − 2)

η∈Γ3 η1,η2∈Γ3 η1+η2=η

|f(η1)f(η2)|2 +

η∈Γ3

f(η)f(−η)

2

,

- (8.4)

with equality if f is constant. Interchanging the order of summation as in (4.4), we have

η∈F4q η1,η2∈Γ3 η1+η2=η

|f(η1)f(η2)|2 =

Γ3

|f|2

2

,

and therefore the right-hand side of (8.4) equals

q(q − 1)

Γ3

|f|2

2

− ((q − 1)q − (q − 2))

η∈Γ3 η1,η2∈Γ3 η1+η2=η

|f(η1)f(η2)|2

+

η∈Γ3

f(η)f(−η)

2

− q(q − 1)

η∈Γ3

|f(η)f(−η)|2.

- (8.5)

We proceed to analyze the cone slices coming from the second summand in (8.5), and the antipodal pairs from the third and fourth summands in (8.5).

Step 3: Cone slices. Interchanging the order of summation, we have

- (8.6)

η∈Γ3 η1,η2∈Γ3 η1+η2=η

|f(η1)f(η2)|2 =

η1,η2∈Γ3

|f(η1)f(η2)|21(η1 + η2 ∈ Γ3).

In light of (8.3), it holds that η1 +η2 ∈ Γ3 if and only if there exist s ∈ S∗ and β1,β2 ∈ F×q , such that β1s = η1 and β2s = η2 and β1 = −β2. Therefore (8.6) boils down to

s∈S∗ β1,β2∈F×q β1 =−β2

|f(β1s)f(β2s)|2 =

s∈S∗ β1,β2∈F×q

|f(β1s)f(β2s)|2 −

η∈Γ3

|f(η)f(−η)|2

=

s∈S∗

 

β∈F×q

|f(βs)|2

 

2

−

η∈Γ3

|f(η)f(−η)|2.

- (8.7)

Since |S∗| = (q − 1)−1|Γ3| = q2 + 1, a further application of Cauchy–Schwarz yields

- (8.8) s∈S∗


 

 

 

 

2

2

1 q2 + 1

1 q2 + 1

|f(βs)|2

|f|2

|f(βs)|2

=

≥

![image 396](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile396.png>)

![image 397](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile397.png>)

s∈S∗ β∈F×q

β∈F×q

Γ3

2

,

where we used (8.2) in the last identity. Equality holds in (8.8) if f is constant.

Step 4: Antipodal pairs. It remains to analyze the last two summands in (8.5) along with the additional term coming from the antipodal pairs in (8.7). In light of Lemma 3.5, these can be bounded by Cauchy–Schwarz as follows:

2

2

2

q3 − q2 + 1 q(q2 − q + 1) − 1

(q − 2) q(q2 − q + 1) − 1

|f|2

- (8.9) .

Combining (8.4)–(8.9), we obtain the desired (8.1), with equality if f is constant. We proceed to prove that all maximizers of (8.1) have constant modulus.

8.1. Maximizers of (8.1) have constant modulus. Let f⋆ : Γ3 → C be a maximizer of (8.1). We note that g := |f⋆| is also a maximizer of (8.1), and aim to show that g is constant. In order for equality to hold in (8.9), the value of g(η)g(−η) must not depend on η ∈ Γ3. Moreover, in order for equality to hold in the second application of Cauchy–Schwarz in (8.4), we must have

- (8.10) g(η1)g(η2) = C(η1 + η2), for every η1,η2 ∈ Ls with η1 = η2, and, in light of (8.3), that g(αs)g(βs) = g(α+2βs)2 whenever α = −β. Interestingly, the analysis splits into two cases, depending on whether q equals 3 or not.

![image 398](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile398.png>)

Case 1: q > 3. Given s ∈ S∗, assume that the function α  → g(αs) is maximized for α = α0 = 0. Given any nonzero β = 2α0, we then have

g(βs)g(α0s) ≥ g(βs)g((2α0 − β)s) = g(α0s)2,

and therefore g(βs) = g(α0s). Similarly, we conclude that g(2α0s) = g(α0s). Indeed, let β ∈ F×q be such that β = α0 and β = 2α0 (this requires q > 3). We have already seen that g(βs) = g(α0s) is maximal, and so

g(2α0s)g(βs) ≥ g(2α0s)g((2β − 2α0)s) = g(βs)2. It follows that g(αs) = C(s), for every α ∈ F×q . This implies that g is constant, since equality in (8.8) forces α∈F×

q

g(αs)2 to be constant. The case q = 3 is more involved, and combinatorially more interesting.

Case 2: q = 3. By Lemma 3.5 and (8.2), the cone Γ3 ⊂ F43 has twenty points and equals the disjoint union of ten lines, each with two antipodal points. As before, there exists c ≥ 0 such that

- (8.11) g(η)g(−η) = c, for every η ∈ Γ3.


f(η)f(−η)

≤

f(η)f(−η)

−

![image 399](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile399.png>)

![image 400](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile400.png>)

η∈Γ3

Γ3

η∈Γ3

√c, and denote the set of such s′ by S′. In order for equality to hold in (8.8), we need g(s′)2 + g(−s′)2 = C to be constant; since g is nonzero, it follows that g(s′) > 0, for all s′ ∈ S′. Identity (8.11) then implies

On each of the ten lines {Ls : s ∈ S∗} that make up Γ3, take s′ ∈ Ls such that g(s′) ≥

![image 401](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile401.png>)

c2 g(s′)2

= C, for all s′ ∈ S′.

g(s′)2 +

![image 402](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile402.png>)

√c, and so g is constant on S′. Writing g |S′=: ρ ≥

The function x  → x2 + c2/x2 is strictly increasing if x ≥

![image 403](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile403.png>)

√c, it suﬃces to show that ρ = √c. We will suppose ρ > √c, and establish suﬃciently many structural constraints on the set S′ to reach a contradiction.

![image 404](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile404.png>)

![image 405](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile405.png>)

![image 406](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile406.png>)

To implement this strategy, let s′0 := (0,a,0) ∈ S′, where a ∈ {1,2}, and π : Γ3 → F3 denote the projection onto the last coordinate, (ξ,τ,σ)  → σ. Given i ∈ {1,2}, write Si′ := {s′ ∈ S′ : π(s′) = i}. In order to get equality in (8.4), we need that g(s′1)g(s′2) = C(s′1 + s′2) for all s′1,s′2 ∈ S′. Moreover, given η ∈ F43 \ Γ30, the set of unordered pairs A(η) := {{s1,s2} : s1,s2 ∈ Γ3, s1 + s2 = η} has exactly three elements by (3.32). Assume that S1′ is nonempty (the case of nonempty S2′ is dealt with in a similar way). Given s′1 ∈ S1′ , we thus have |A(s′0 + s′1)| = 3. Consider the other two pairs {s′2,s′3},{s′4,s′5} ∈ A(s′0 + s′1). Since

ρ2 = g(s′0)g(s′1) = g(s′2)g(s′3) = g(s′4)g(s′5),

it follows from ρ > √c that ρ = g(s′2) = g(s′3) = g(s′4) = g(s′5), and thus s′2,s′3,s′4,s′5 ∈ S′. Crucially, we observe that s′2,s′3,s′4,s′5 ∈ S2′ since π(s′2 + s′3) = π(s′4 + s′5) = 1. On the other hand, if A(s′0 + s′2) = {{s′0,s′2},{s′6,s′7},{s′8,s′9}}, then π(s′0 + s′2) = 2, and so we conclude in a similar way that s′6,s′7,s′8,s′9 ∈ S1′. Further note that s′1 ∈/ {s′6,s′7,s′8,s′9}, for otherwise s′1 +s′i = s′0 +s′2 for some i ∈ {6,7,8,9}; from s′0 + s′1 = s′2 + s′3, we would then obtain 2s′0 = s′i + s′3, which is absurd since 2s′0,s′i,s′3 belong to distinct lines (recall (8.3)). Thus S′ = {s′0}∪S1′ ∪S2′, where S1′ = {s′1,s′6,s′7,s′8,s′9} and S2′ := {s′2,s′3,s′4,s′5} are disjoint, and disjoint from {s′0}. It follows that the set

![image 407](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile407.png>)

(A(s′0 + s′i) \ {s′0 + s′i})

s′i∈S1′

contains ten distinct pairs, and thus cannot be a subset of the six-element set {{u,v} : u,v ∈ S2′,u = v}. This contradiction results from assuming ρ > √c; thus ρ = √c, and g = |f⋆| is constant. This concludes the proof of Theorem 1.5.

![image 408](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile408.png>)

![image 409](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile409.png>)

9. Proof of Theorem 1.6

In this section, we prove Theorem 1.6. Starting with the case of the cone Υ30 equipped with normalized counting measure ν = νΥ, we test the functional

|(fεν)∨(x)|4 1

4 p

- (9.1) Φp(ε) := x∈F


![image 410](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile410.png>)

2

|Υ30| ξ∈Υ30 |fε(ξ)|2

![image 411](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile411.png>)

against the function fε := 1Υ3

+ εδ0, for small values of ε > 0. The denominator in (9.1) is straightforward to compute:

0

(|Υ30| − 1) × 12 + 1 × (1 + ε)2 |Υ30|

1 |Υ30|

|fε(ξ)|2 =

= 1 −

![image 412](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile412.png>)

![image 413](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile413.png>)

ξ∈Υ30

(1 + ε)2 |Υ30|

1 |Υ30|

+

.

![image 414](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile414.png>)

![image 415](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile415.png>)

As for the numerator in (9.1), note that (2.9) implies

1 |Υ30| ξ=0

(δ0ν)∨(x) =

e(x · ξ) =

![image 416](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile416.png>)

1 |Υ30|

, for every x ∈ F4p,

![image 417](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile417.png>)

ν)∨ = νΥ∨ has been computed in (3.17). Together with |Υ30| = p3 + p2 − p (Proposition 3.4), this leads to

whereas (1Υ3

0

4

4

4

3+p(p−1) |Υ30|

1 × ε+p

+ (|Υ30| − 1) × ε+|pΥ(p3−1)

+ (p4 − |Υ30|) × | εΥ−3p

![image 418](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile418.png>)

![image 419](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile419.png>)

![image 420](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile420.png>)

0|

0|

Φp(ε) =

2 ,

![image 421](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile421.png>)

0| + (1+|Υε3)2

1 − |Υ13

![image 422](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile422.png>)

![image 423](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile423.png>)

0|

which can be simpliﬁed to Φp(ε) = Ap(ε)/Bp(ε), where Ap(ε) := 2p5 + p6 − 7p7 − p8 + 5p9 + p10 + (−8p5 + 4p6 + 8p7)ε + (−6p3 + 6p4 + 6p5)ε2 + 4p2ε3 + p2ε4;

Bp(ε) := (p2 + p − 1)2(p3 + p2 − p + ε(2 + ε))2. Consequently,

4p2(p − 2)(p2 − 1)2 (p2 + p − 1)5

Φ′p(0) =

, which is a strictly positive quantity for every prime p > 2.

![image 424](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile424.png>)

To handle the cone Γ30 equipped with normalized counting measure ν = νΓ, consider the functional

|(fεν)∨(x)|4 1

4 p

- (9.2) Ψp(ε) := x∈F


2.

![image 425](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile425.png>)

|Γ30| ξ∈Γ30 |fε(ξ)|2

![image 426](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile426.png>)

If p ≡ 1(mod 4), then the proof is the same as the one for Υ30 above; recall our discussion in the course of the proof of Proposition 3.4. If p ≡ 3(mod 4), then (1Γ3

ν)∨ = νΓ∨ is given by (3.25), which together

0

with |Γ30| = p3 − p2 + p (Lemma 3.5) leads to

4

4

4

3−p(p−1) |Γ30|

+ (|Γ30| − 1) × ε−p|Γ(p3−1)

1 × ε+p

+ (p4 − |Γ30|) × ε|Γ+3p

![image 427](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile427.png>)

![image 428](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile428.png>)

![image 429](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile429.png>)

0|

0|

2 .

Ψp(ε) =

![image 430](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile430.png>)

0| + (1+|Γ3ε)2

1 − |Γ13

![image 431](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile431.png>)

![image 432](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile432.png>)

0|

This can be simpliﬁed to Ψp(ε) = Cp(ε)/Dp(ε), where Cp(ε) := −2p5 + 5p6 − 5p7 + 5p8 − 3p9 + p10 + 4p6ε + (6p3 − 6p4 + 6p5)ε2 + 4p2ε3 + p2ε4;

Dp(ε) := (p2 − p + 1)2(p3 − p2 + p + ε(2 + ε))2. It follows that

4p2(p − 2)(p − 1)2(p2 + 1) (p2 − p + 1)5

Ψ′p(0) = −

, which is a strictly negative quantity for every prime p ≡ 3(mod 4).

![image 433](<2024-gonzlezriquelme-sharp-extension-inequalities-finite_images/imageFile433.png>)

As a consequence, for S ∈ {Γ30,Υ30} and any prime p, the function 1S is not a critical point of the functionals Ψp,Φp, respectively, and therefore not a local or global maximizer for the L2(S,dν) → L4(F4p,dx) extension inequality from S ⊂ F4p. This concludes the proof of Theorem 1.6.

Acknowledgments

The authors are partially supported by FCT/Portugal through CAMGSD, IST-ID, projects UIDB/ 04459/2020 and UIDP/04459/2020 and 3 by IST Santander Start Up Funds. They are grateful to Asem Abdelraouf and Emanuel Carneiro for inspiring discussions regarding the present work.

References

- [1] B. Arsovski, The p-adic Kakeya conjecture. J. Amer. Math. Soc. 37 (2024), no. 1, 69–80.
- [2] J. Bennett, N. Bez, A. Carbery, D. Hundertmark, Heat-ﬂow monotonicity of Strichartz norms. Anal. PDE 2 (2009), no. 2, 147–158.
- [3] J. Bennett, A. Carbery, T. Tao, On the multilinear restriction and Kakeya conjectures. Acta Math. 196 (2006), no. 2, 261–302.
- [4] J. Bourgain, L. Guth, Bounds on oscillatory integral operators based on multilinear estimates. Geom. Funct. Anal. 21 (2011), no. 6, 1239–1295.
- [5] A. Carbery, Harmonic analysis on vector spaces over ﬁnite ﬁelds. Lecture notes. https://www.maths.ed.ac.uk/~carbery/analysis/notes/fflpublic.pdf, 2006.
- [6] E. Carneiro, A sharp inequality for the Strichartz norm. Int. Math. Res. Not. IMRN 2009, no. 16, 3127–3145.
- [7] E. Carneiro, L. Oliveira, M. Sousa, Gaussians never extremize Strichartz inequalities for hyperbolic paraboloids. Proc. Amer. Math. Soc. 150 (2022), no. 8, 3395–3403.
- [8] M. Dhar, The Kakeya set conjecture over Z/NZ for general N. Adv. Comb. (2024), Paper No. 2, 26 pp.
- [9] M. Dhar, Z. Dvir, Proof of the Kakeya set conjecture over rings of integers modulo square-free N. Comb. Theory 1

(2021), Paper No. 4, 21 pp.

- [10] B. Dodson, J. Marzuola, B. Pausader, D. Spirn, The proﬁle decomposition for the hyperbolic Schr¨odinger equation. Illinois J. Math. 62 (2018), no. 1–4, 293–320. Erratum: Illinois J. Math. 65 (2021), no. 1, 259–260.
- [11] Z. Dvir, On the size of Kakeya sets in ﬁnite ﬁelds. J. Amer. Math. Soc. 22 (2009), no. 4, 1093–1097.
- [12] J. Ellenberg, R. Oberlin, T. Tao, The Kakeya set and maximal conjectures for algebraic varieties over ﬁnite ﬁelds. Mathematika 56 (2010), no. 1, 1–25.
- [13] D. Foschi, Maximizers for the Strichartz inequality. J. Eur. Math. Soc. (JEMS) 9 (2007), no. 4, 739– 774.
- [14] F. Gonc¸alves, Orthogonal polynomials and sharp estimates for the Schr¨odinger equation. Int. Math. Res. Not. IMRN 2019, no. 8, 2356–2383.
- [15] B. Green, Restriction and Kakeya phenomena. Cambridge Part III course notes. http://people.maths.ox.ac.uk/greenbj/papers/rkp.pdf, 2013
- [16] L. Guth, A restriction estimate using polynomial partitioning. J. Amer. Math. Soc. 29 (2016), no. 2, 371–413.
- [17] L. Guth, Restriction estimates using polynomial partitioning II. Acta Math. 221 (2018), no. 1, 81–142.
- [18] J. Hickman, J. Wright, The Fourier restriction and Kakeya problems over rings of integers modulo N. Discrete Anal.

(2018), Paper No. 11, 54 pp.

- [19] A. Iosevich, D. Koh, Extension theorems for spheres in the ﬁnite ﬁeld setting. Forum Math. 22 (2010), no. 3, 457–483.
- [20] D. Koh, S. Lee, T. Pham, On the ﬁnite ﬁeld cone restriction conjecture in four dimensions and applications in incidence geometry. Int. Math. Res. Not. IMRN (2022), no. 21, 17079–17111.
- [21] D. Koh, S. Yeom, Restriction of averaging operators to algebraic varieties over ﬁnite ﬁelds. Taiwanese J. Math. 21

(2017), no. 1, 211–229.

- [22] D. Hundertmark, V. Zharnitsky, On sharp Strichartz inequalities in low dimensions. Int. Math. Res. Not. IMRN

(2006), Art. ID 34080, 1–18.

- [23] M. Lewko, Finite ﬁeld restriction estimates based on Kakeya maximal operator estimates. J. Eur. Math. Soc. (JEMS) 21 (2019), no. 12, 3649–3707.


- [24] R. Lidl, H. Niederreiter, Finite ﬁelds. With a foreword by P. M. Cohn. Second edition. Encyclopedia Math. Appl.,

20. Cambridge University Press, Cambridge, 1997.

- [25] G. Mockenhaupt, T. Tao, Restriction and Kakeya phenomena for ﬁnite ﬁelds. Duke Math. J. 121 (2004), no. 1, 35–74.
- [26] G. Negro, D. Oliveira e Silva, B. Stovall, J. Tautges, Exponentials rarely maximize Fourier extension inequalities for cones. arXiv:2302.00356.
- [27] G. Negro, D. Oliveira e Silva, C. Thiele, When does e−|τ| maximize Fourier extension for a conic section? Harmonic analysis and convexity, 391–426. Adv. Anal. Geom., 9, De Gruyter, Berlin, 2023.
- [28] A. Salvatore, The Kakeya conjecture on local ﬁelds of positive characteristic. Mathematika 69 (2023), no. 1, 1–16.
- [29] E. M. Stein, Harmonic Analysis: Real-Variable Methods, Orthogonality, and Oscillatory Integrals. Princeton Univ. Press, Princeton, NJ, 1993.
- [30] R. Strichartz, Restrictions of Fourier transforms to quadratic surfaces and decay of solutions of wave equations. Duke Math. J. 44 (1977), no. 3, 705–714.
- [31] T. Wolﬀ, Recent work connected with the Kakeya problem. Prospects in mathematics (Princeton, NJ, 1996), 129–162. American Mathematical Society, Providence, RI, 1999


Email address: cristian.g.riquelme@tecnico.ulisboa.pt Email address: diogo.oliveira.e.silva@tecnico.ulisboa.pt Center for Mathematical Analysis, Geometry and Dynamical Systems & Departamento de Matematica,´

Instituto Superior T´ecnico, Av. Rovisco Pais, 1049-001 Lisboa, Portugal

