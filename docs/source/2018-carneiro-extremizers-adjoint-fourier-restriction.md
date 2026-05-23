---
type: source
kind: paper
title: "Extremizers for adjoint Fourier restriction on hyperboloids: the higher dimensional case"
authors: Emanuel Carneiro, Diogo Oliveira e Silva, Mateus Sousa, Betsy Stovall
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1809.05698v1
source_local: ../raw/2018-carneiro-extremizers-adjoint-fourier-restriction.pdf
topic: general-knowledge
cites:
---

arXiv:1809.05698v1[math.CA]15Sep2018

EXTREMIZERS FOR ADJOINT FOURIER RESTRICTION ON HYPERBOLOIDS: THE HIGHER DIMENSIONAL CASE

EMANUEL CARNEIRO, DIOGO OLIVEIRA E SILVA, MATEUS SOUSA, AND BETSY STOVALL

Abstract. We prove that in dimensions d ≥ 3, the non-endpoint, Lorentz-invariant L2 → Lp adjoint Fourier restriction inequality on the d-dimensional hyperboloid Hd ⊆ Rd+1 possesses maximizers. The analogous result had been previously established in dimensions d = 1, 2 using the convolution structure of the inequality at the lower endpoint (an even integer); we obtain the generalization by using tools from bilinear restriction theory.

1. Introduction

- 1.1. Setup. In this note we continue the study initiated in [3, 12] on sharp Fourier restriction theory on hyperboloids. Let us start by recalling the basic terminology and the main deﬁnitions.


Throughout this work we adopt the following normalization for the Fourier transform in Rd+1: g(ζ) =

e−iz·ζ g(z)dz. (1.1)

Rd+1

If ξ ∈ Rd, we deﬁne ξ := (1 + |ξ|2)12. The hyperboloid Hd ⊂ Rd+1 is the surface deﬁned by1

![image 1](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile1.png>)

Hd = (ξ,τ) ∈ Rd × R : τ = ξ , and comes equipped with the Lorentz-invariant measure

dξ dτ ξ

dσ(ξ,τ) = δ τ − ξ

, (1.2) which is deﬁned by duality on an appropriate dense class of functions via the identity

![image 2](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile2.png>)

ϕ(ξ,τ)dσ(ξ,τ) =

Hd

dξ ξ

.

ϕ(ξ, ξ )

![image 3](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile3.png>)

Rd

The Fourier extension operator on Hd (or adjoint Fourier restriction operator) is given by T(f)(x,t) :=

dξ ξ

eix·ξeit ξ f(ξ)

, (1.3)

![image 4](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile4.png>)

Rd

where (x,t) ∈ Rd × R and f belongs to the Schwartz class in Rd. Throughout this note we identify a function f : Hd → C with a complex-valued function deﬁned on Rd. The norm in Lp(Hd) =

![image 5](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile5.png>)

2010 Mathematics Subject Classiﬁcation. 42B10. Key words and phrases. Sharp Fourier restriction theory, extremizers, Klein–Gordon equation, hyperboloid. 1A simple rescaling argument transfers all the results of this paper to the hyperboloids Hds = (ξ, τ) ∈ Rd × R : τ = (s2 + |ξ|2)12 , s > 0.

![image 6](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile6.png>)

1

Lp(Hd,σ) is then given by

1 p

dξ ξ

![image 7](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile7.png>)

|f(ξ)|p

. With the Fourier transform normalized as in (1.1), note that

f Lp(Hd) =

![image 8](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile8.png>)

Rd

T(f)(x,t) = fσ(−x,−t). (1.4) The seminal work of Strichartz [16, Theorem 1, Cases III (b)(c)] establishes the estimate

T(f) Lp(Rd+1) ≤ Hd,p f L2(Hd) , (1.5) with a ﬁnite constant Hd,p (independent of f), provided that

 

6 ≤ p < ∞, if d = 1;

(1.6)



2(d+2)

d ≤ p ≤ 2(dd−+1)1 , if d ≥ 2.

![image 9](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile9.png>)

![image 10](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile10.png>)

We reserve the symbol Hd,p for the optimal constant

T(f) Lp(Rd+1) f L2(Hd)

Hd,p := sup

, (1.7)

![image 11](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile11.png>)

0 =f∈L2(Hd)

and say that a nonzero function f ∈ L2(Hd) is an extremizer of (1.5) if it realizes the supremum in (1.7), and we call a nonzero sequence {fn} ⊂ L2(Hd) an extremizing sequence of (1.5) if the ratio

T(fn) Lp(Rd+1)/ fn L2(Hd) converges to Hd,p as n → ∞.

- 1.2. Main theorem. The ﬁrst result to address the sharp form of (1.5) is due to Quilodr´an [12],


in which he computes the exact values of Hd,p in the endpoint cases (d,p) = (2,4),(2,6) and (3,4), and establishes the non-existence of extremizers in these cases.2 A crucial element of his proof is the fact that the Lebesgue exponents p under consideration are even integers, a fact that allows one to use the convolution structure of the problem via an application of Plancherel’s theorem. In [12], Quilodr´an also raises two interesting questions: What is the value of the sharp constant at the endpoint (d,p) = (1,6) (the remaining case with p even); and do extremizers exist in the non-endpoint cases.

The precursor [3] of the present work contains two main results. The ﬁrst result [3, Theorem 1] is the explicit computation of the optimal constant Hd,p in the case (d,p) = (1,6) and the proof that extremizers do not exist in this case. The second result [3, Theorem 2] establishes the existence of extremizers in all non-endpoint cases of (1.5) in dimensions d ∈ {1,2}. The proof of the latter result is obtained by establishing that extremizing sequences converge modulo certain symmetries of the problem. In the present case, by a symmetry we mean an operator S : L2(Hd) → L2(Hd) such that

Sf L2(Hd) = f L2(Hd) and T(Sf) Lp(Rd+1) = T(f) Lp(Rd+1).

![image 12](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile12.png>)

2By contrast, the recent work [13] establishes existence of extremizers for the endpoint L2 to L4 adjoint Fourier restriction inequality on the one-sheeted hyperboloid in dimension 4.

Such an operator can shift the mass of sequences and destroy strong convergence while still mantaining its extremizing properties, hence the study of these symmetries is fundamental. In the case of the hyperboloid, one has to account for the action of the Lorentz group and space-time modulations (and their compositions), which we introduce in more detail in the next section. In [3], the convergence is obtained via a direct and self-contained approach that explores the convolution structure of the problem at the lower endpoint (which is an even integer in these low dimensions). The drawback of this particularly simple proof is that it does not work in the higher dimensional cases d ≥ 3.

In this note we return to this problem and extend the result of [3, Theorem 2] to dimensions d ≥ 3. Our main result is the following.

Theorem 1. Let d ≥ 3. Extremizers for inequality (1.5) exist if 2(dd+2) < p < 2(dd−+1)1 . In fact, given any extremizing sequence {fn}, there exist symmetries Sn such that {Snfn} converges in L2(Hd) to an extremizer f, after passing to a subsequence.

![image 13](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile13.png>)

![image 14](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile14.png>)

The main new ingredient of the proof, when compared to that of [3, Theorem 2], is the use of machinery from bilinear restriction theory to obtain a reﬁned version of inequality (1.5). As in [2, 3], we exploit the fact that the hyperboloid is well approximated by the paraboloid and the cone. The geometric construction underlying the bilinear restriction machinery accounts for this fact: in some sense, it interpolates between the two endpoint cases, which we will refer to as the elliptic and the conic regimes, respectively.

Estimates for Fourier extension operators are related to estimates for dispersive partial diﬀerential equations. In our case, the extension operator T deﬁned in (1.3) is related to the Klein–Gordon equation ∂t2u = ∆xu − u for (x,t) ∈ Rd × R. Deﬁning the (half) Klein–Gordon propagator as

√1−∆g(x) :=

1 (2π)d Rd

![image 15](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile15.png>)

eit

eix·ξ eit ξ g(ξ)dξ, one readily sees that

![image 16](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile16.png>)

√1−∆ g(x), (1.8) with g(ξ) = ξ −1f(ξ). Therefore, inequality (1.5) can be restated as

![image 17](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile17.png>)

T(f)(x,t) = (2π)d eit

√1−∆g Lp

![image 18](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile18.png>)

x,t(Rd×R) ≤ (2π)−d Hd,p g H1

eit

2(Rd), where for s ≥ 0 we denote by Hs(Rd) the nonhomogeneous Sobolev space, deﬁned as

![image 19](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile19.png>)

Hs(Rd) = g ∈ L2(Rd) : g 2Hs(Rd) :=

| g(ξ)|2 ξ 2sdξ < ∞ .

Rd

The reader should keep in mind this equivalent formulation, since some of the results we quote from [3, Section 6] are stated in terms of the Klein–Gordon propagator.

Extremal problems related to Fourier restriction theory have garnished a lot of attention in recent years, and a large body of work has emerged. Several authors have investigated the interface between bilinear restriction theory and these extremal questions, both from the restriction side and

the partial diﬀerential equations point of view. Here we mention the works [1, 2, 5, 6, 7, 10, 14], all of which deal with these connections. Many other authors have contributed to the development of the area, and we refer the reader to [3] for an exposition of related literature on sharp Fourier restriction theory.

- 1.3. Outline. We discuss the Lorentz symmetry of the problem in Section 2, where we also establish an annular decoupling inequality which implies a modest gain of control over extremizing sequences. The actual proof starts in Section 3, with a simple but useful argument that allows us to restrict the angular support of the functions under consideration. In Section 4, we describe a geometric decomposition of space into caps and sectors, and the corresponding bilinear restriction estimates that will play a key role in the analysis. As in [3], the crux of the matter is the construction of a distinguished region, i.e. the lift of a cap or a sector to the hyperboloid that contains a positive universal proportion of the total mass in an extremizing sequence. We establish this fact via a reﬁned Strichartz inequality, formulated as Theorem 4 and proved in Section 5. Once the existence of a special region has been established in dimensions d ≥ 3, the proof of Theorem 1 is ﬁnished by invoking the concentration-compactness material of [3, Section 6], which was already tailor-made to receive the input in any dimension. The details are outlined in Section 6.
- 1.4. Notation. Universal quantities will be allowed to depend only on the dimension d and the Lebesgue exponent p. In a similar spirit, given A,B ≥ 0, we write A ≃ B (resp. A B) and say


that A,B are comparable if there exists a ﬁnite constant C = C(d,p) > 0, such that C1 B ≤ A ≤ CB (resp. A ≤ CB). A number N is said to be dyadic if it is an integral power of 2, i.e. N ∈ 2Z.

![image 20](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile20.png>)

2. Preliminaries

- 2.1. Lorentz boosts. The Lorentz group, denoted L, is deﬁned as the group of invertible linear transformations in Rd+1 that preserve the bilinear form (x,y) ∈ Rd+1 × Rd+1  → x · Jy, where J = diag(−1,...,−1,1). In particular, if L ∈ L, then |detL| = 1. Denote the subgroup of L


that preserves Hd by L+. A one-parameter subgroup of L+ is {Lt}t∈(−1,1), where the linear map Lt : Rd+1 → Rd+1 is deﬁned via

τ + tξ1 √1 − t2

ξ1 + tτ √1 − t2

Lt(ξ1,...,ξd,τ) =

.

,ξ2,...,ξd,

![image 21](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile21.png>)

![image 22](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile22.png>)

![image 23](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile23.png>)

![image 24](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile24.png>)

Given an orthogonal matrix A ∈ O(d), the map (ξ,τ)  → (Aξ,τ) belongs to L+. A way to parametrize more general Lorentz boosts is as follows. Given a frequency parameter ν ∈ Rd, we deﬁne the Lorentz boost in the direction ν as

Lν(ξ,τ) := (ξ⊥ + ν ξ − ντ, ν τ − ν · ξ). (2.1) Here ξ⊥ and ξ denote the components of ξ which are orthogonal and parallel to ν, respectively. The boost Lν preserves space-time volume since its determinant is one, and acts on Rd via

L♭ν(ξ) := ξ⊥ + ν ξ − ν ξ . (2.2)

Note that L−ν 1 = L−ν, and likewise (L♭ν)−1 = L♭−ν. We also have that Lν(ν, ν ) = (0,1), and correspondingly L♭ν(ν) = 0. For p ∈ [1,∞], L ∈ L+, and f ∈ Lp(Hd), deﬁne the composition L∗f = f ◦ L. Then one easily checks that

L∗f Lp(Hd) = f Lp(Hd) and T(L∗f) Lp(Rd+1) = T(f) Lp(Rd+1).

- 2.2. Annular decoupling. The extension operator T deﬁned in (1.3) satisﬁes more general mixednorm estimates of which (1.5) is a particular case. As pointed out in [8] and the references therein, the inequality


q−r1 f L2

1

ξ(Hd) (2.3) holds, provided q ∈ [2,∞], r ∈ [2,2d/(d − 2)] (r ∈ [2,∞] if d ∈ {1,2}), and

T(f) Lq

tLrx(Rd+1) ξ

![image 25](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile25.png>)

![image 26](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile26.png>)

d − 1 + θ r

d − 1 + θ 2

2 q

, (q,r) = (2,∞),

+

=

![image 27](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile27.png>)

![image 28](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile28.png>)

![image 29](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile29.png>)

for some θ ∈ [0,1]. A pair (q,r) of Lebesgue exponents satisfying these conditions will be referred to as an admissible pair. Certain instances of inequality (2.3) together with a variant of the Littlewood– Paley decomposition yield an annular decoupling inequality which we now prove.

We will use a dyadic frequency decomposition. To implement it, let N ≥ 1 be a dyadic number. Given f ∈ L2(Hd), we denote by fN the smoothed out restriction of f to frequencies |ξ| ≃ N. More precisely, ﬁx a smooth radial bump function ψ : Rd → [0,1] supported in the ball {ξ ∈ Rd : |ξ| ≤ 1110} and equal to 1 on the unit ball {ξ ∈ Rd : |ξ| ≤ 1}, and deﬁne

![image 30](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile30.png>)

ψ(ξ)f(ξ), if N = 1, ψ(Nξ ) − ψ(2Nξ) f(ξ), if N > 1.

fN(ξ) :=

![image 31](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile31.png>)

![image 32](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile32.png>)

Note that supp(f1) ⊆ {ξ ∈ Rd : |ξ| ≤ 2} and supp(fN) ⊆ {ξ ∈ Rd : N2 ≤ |ξ| ≤ 2N}, for N > 1. The following annular decoupling is in the spirit of [7, 10].

![image 33](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile33.png>)

- Proposition 2. Let d ≥ 3 and 2(dd+2) ≤ p ≤ 2(dd−+1)1 . Then


![image 34](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile34.png>)

![image 35](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile35.png>)

T(f) pL

T(fN) pL−2

p(Rd+1) f 2L2(Hd), (2.4)

p(Rd+1) sup

N∈2Z≥0

for every f ∈ L2(Hd).

Proof. By the Littlewood–Paley square function estimate, we have that

T(f) pLp

≃

x,t

N

|T(fN)|2

- 1

![image 36](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile36.png>)

- 2 p


. (2.5)

Lpx,t

Indeed, Fx[T(f)](ξ,t) = eit ξ ξ −1f(ξ), where Fx denotes the Fourier transform in the variable x ∈ Rd. Standard Littlewood–Paley theory yields

- 1

![image 37](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile37.png>)

- 2 p


T(f)(·,t) pLp

|T(fN)(·,t)|2

≃

,

Lpx

x

N

for each ﬁxed t ∈ R. Estimate (2.5) then follows from integration in the time variable t.

p

Since d ≥ 3, we have that p2 ≤ 2, and thus the sequence space embedding ℓ

2 ֒→ ℓ2 implies

![image 38](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile38.png>)

![image 39](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile39.png>)

2 p

- 1

![image 40](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile40.png>)

- 2


![image 41](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile41.png>)

p 2

|T(fN)|2

≤

|T(fN)|

.

![image 42](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile42.png>)

N

N

We can estimate

2

p 2

p 2

p 2

T(f) pLp

![image 43](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile43.png>)

|T(fN)|

|T(fM)T(fN)|

,

=

T(fM)T(fN)

![image 44](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile44.png>)

![image 45](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile45.png>)

p 2

![image 46](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile46.png>)

x,t Rd+1 N

L

Rd+1 N,M

x,t

M N≤M

(2.6) where the last inequality follows from Fubini’s theorem and symmetry. We control each of the summands of the right-hand side of (2.6) using the mixed-norm estimates (2.3). With this purpose in mind, ﬁx admissible pairs (q0,r0) and (q1,r1) with q1 < p < q0 and r0 < p < r1, which additionally satisfy

2 p

1 q1

1 r0

1 r1

1 q0

. (2.7) Then, invoking Ho¨lder’s inequality twice, we have that

+

=

+

=

![image 47](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile47.png>)

![image 48](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile48.png>)

![image 49](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile49.png>)

![image 50](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile50.png>)

![image 51](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile51.png>)

T(fM)T(fN)

p 2

p 2 −1 Lp T(fN)

p 2 −1

≤ T(fM)

![image 52](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile52.png>)

![image 53](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile53.png>)

![image 54](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile54.png>)

Lp T(fM)T(fN) Lp

p 2

![image 55](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile55.png>)

2

L

![image 56](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile56.png>)

p 2 −1 Lp T(fM) Lq0

p 2 −1 Lp T(fN)

![image 57](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile57.png>)

![image 58](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile58.png>)

≤ T(fM)

t Lrx0 T(fN) Lq1

t Lrx1 T(fM)

p 2 −1 Lp ξ

p 2 −1 Lp T(fN)

1

1

q0 −r10 fM L2(Hd) ξ

q1 −r11 fN L2(Hd).

![image 59](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile59.png>)

![image 60](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile60.png>)

![image 61](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile61.png>)

![image 62](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile62.png>)

![image 63](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile63.png>)

![image 64](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile64.png>)

where the last line is a consequence of (2.3). Since ξ ≃ M inside the support of fM, and similarly for fN, from this and (2.7) it follows that

q1 − r11

1

N M

p 2 −1 Lp T(fN)

p 2 −1 Lp fM L2(Hd) fN L2(Hd).

p 2

![image 65](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile65.png>)

![image 66](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile66.png>)

![image 67](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile67.png>)

![image 68](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile68.png>)

![image 69](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile69.png>)

T(fM)

T(fM)T(fN)

p 2

![image 70](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile70.png>)

L

![image 71](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile71.png>)

Going back to (2.6) and noting that q1

− r11 > 0, we use Ho¨lder’s inequality and the elementary estimate 2ab ≤ a2 + b2 with a = fN L2(Hd) and b = fM L2(Hd), and sum a geometric series to ﬁnally conclude that

![image 72](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile72.png>)

![image 73](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile73.png>)

1

N M

p 2

T(fN) pL−p2

![image 74](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile74.png>)

≤ sup

T(fM)T(fN)

p 2

![image 75](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile75.png>)

L

![image 76](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile76.png>)

N

M N≤M

M N≤M

T(fN) pL−p2 f 2L2(Hd). This ﬁnishes the proof of the proposition.

sup

N

q1 − r11

1

![image 77](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile77.png>)

![image 78](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile78.png>)

fM L2(Hd) fN L2(Hd)

3. Beginning of the proof: angular restriction

Let {fn}n∈N ⊂ L2(Hd) be an extremizing sequence for (1.5). We may assume that fn L2(Hd) = 1 and that T(fn) Lp(Rd+1) → Hd,p as n → ∞. Recall from the Introduction that each fn is regarded as a function on Rd. Given K ∈ N, consider a ﬁnite partition of the unit sphere Sd−1 = {ξ ∈ Rd : |ξ| = 1} into K disjoint regions,

K

Sd−1 =

Ck∗.

k=1

Given a function f : Rd → C, let f(k) := f R

, where Rk = {ξ ∈ Rd : ξ/|ξ| ∈ Ck∗}. In this way we split Rd into K angular sectors. The triangle inequality implies

k

K

T(fn) Lp(Rd+1) ≤

k=1

T(fn(k)) Lp(Rd+1).

Observe that, possibly after extraction of a subsequence, there exists k0 ∈ {1,2,...,K} such that {fn(k0)}n∈N is a quasi-extremizing sequence for (1.5). By this we mean that fn(k0) L2(Hd) ≤ 1, and

T(f(k

0)

n ) Lp(Rd+1) ≥ δ1, (3.1) for every n ∈ N and some universal δ1 > 0 (we may take for instance δ1 = H2d,pK ).

![image 79](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile79.png>)

Under these circumstances, we will establish the existence of a universal ball B ⊂ Rd centered at the origin, a universal δ2 > 0, and a sequence of Lorentz transformations {Ln}n∈N such that

L∗nf(k

0)

n L2(B) ≥ δ2, for every n ∈ N. This naturally implies

L∗nfn L2(B) ≥ δ2, for every n ∈ N. The latter inequality is of the sort which is required in order to invoke the machinery from [3, Section 6] and conclude the proof of Theorem 1.

Throughout the upcoming Sections 4 and 5 we will thus assume that our functions are supported

in a small angular region R1 (the corresponding C1∗ ⊂ Sd−1 is described at the beginning of Section 4). Henceforth, such functions will be referred to as admissible.

4. Caps, sectors and bilinear estimates

As mentioned in the Introduction, one of the key ingredients in the proof of Theorem 1 is the use of tools from bilinear restriction theory. Classical works on the topic include [17, 18, 20].

In this section, we deﬁne the appropriate geometric regions and the notion of separation between them, and establish the bilinear restriction estimates that will be of relevance in the sequel.

- 4.1. Deﬁnition of dyadic regions. Let d ≥ 3 be a ﬁxed dimension. Consider the (d − 1)dimensional cube


C1 = {η = (η1,η2,...,ηd−1) ∈ Rd−1 : |ηi| ≤ ℓ, i = 1,2,...,d − 1}

of sidelength 2ℓ centered at the origin. The quantity ℓ < 41 is a small ﬁxed number which depends only on the dimension d, and shall be appropriately chosen in due course. Given a dyadic number

![image 80](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile80.png>)

M ∈ 2Z≤0, let ΓM denote the usual dyadic decomposition of the cube C1 into cubes of sidelength 2ℓM on Rd−1. In particular, Γ1 = {C1}, and ΓM consists of M−(d−1) essentially disjoint cubes (i.e. the intersection of any two distinct cubes is a Lebesgue null-set). Let ∗ : C1 → Sd−1 be the lift of

a point in C1 to a point in the unit sphere Sd−1 ⊂ Rd, deﬁned via

- 1

![image 81](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile81.png>)

- 2).


η∗ = (η,(1 − |η|2) For each cube Q ∈ ΓM, let

Q∗ = {η∗ : η ∈ Q} denote the lift of the cube Q, and let Γ∗M denote the collection of the lifted cubes of ΓM.

For the purposes of the present construction, we may think of distances in C1∗ ⊂ Sd−1 ⊂ Rd as being almost the same as Euclidean distances in C1 ⊂ Rd−1. More precisely, given any constant ε1 > 0, we may choose ℓ = ℓ(d,ε1) > 0 suﬃciently small, such that

|η − ζ| ≤ dist(η∗,ζ∗) ≤ (1 + ε1)|η − ζ| (4.1) for all η,ζ ∈ C1 ⊂ Rd−1. Here | · | denotes Euclidean distance in Rd−1, and dist(·,·) denotes the geodesic distance on Sd−1 ⊂ Rd. We may take for instance ε1 = 1001 .

![image 82](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile82.png>)

Given N ∈ 2Z

, deﬁne the restricted dyadic annulus

>0

AN := ξ ∈ Rd : 12N ≤ |ξ| ≤ 2N and ξ/|ξ| ∈ C1∗ , (4.2) and set A1 := {ξ ∈ Rd : |ξ| ≤ 2 and ξ/|ξ| ∈ C1∗}.

![image 83](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile83.png>)

, let r ∈ 2Z be such that 0 < r ≤ N. If 0 < r ≤ 1, then we further decompose the restricted annulus AN into an essentially disjoint union of regions

Given N ∈ 2Z

≥0

A(Nj) := ξ ∈ AN : 21N(1 + 3jr) ≤ |ξ| ≤ 12N(1 + 3(j + 1)r) , (4.3) for j ∈ J := {0,1,...,r−1 − 1}. If 1 < r ≤ N, then we unify the notation below by letting J = {0} and A(0)N := AN. In both cases we then have that #J = max{1,r−1}.

![image 84](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile84.png>)

![image 85](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile85.png>)

, and r ∈ 2Z such that 0 < r ≤ N, let M = r/N and consider DN,r := κj,kN,r : (j,k) ∈ J × {1,2,...,M−(d−1)} , where the regions κ = κj,kN,r are deﬁned as

Given N ∈ 2Z

≥0

κj,kN,r := ξ ∈ A(Nj) : ξ/|ξ| ∈ Q∗k , (4.4) and Q∗k is a cube in the collection Γ∗M. The center of a region κ = κj,kN,r as in (4.4) is deﬁned to be

c(κ) := 21N 1 + 3 min{1,r}(j + 21) ωk∗, (4.5) where ωk∗ ∈ Sd−1 is the lift of the center ωk of the cube Qk ∈ ΓM.

![image 86](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile86.png>)

![image 87](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile87.png>)

If 0 < r ≤ 1, then an element of DN,r is called an r-cap at scale N. If 1 < r ≤ N, then an element of DN,r is called an r-sector at scale N. The Lebesgue measure of an r-cap at scale N is comparable to Nrd, and the Lebesgue measure of an r-sector at scale N is comparable to Nrd−1.

By a region we will continue to mean a set which is either a cap or a sector. For ﬁxed N,r, the regions in DN,r are essentially disjoint. If r < N, then each κ ∈ DN,r is contained in a unique

κ◦ ∈ DN,2r, and we refer to κ◦ as the parent of κ. In a similar spirit, each κ ∈ DN,r has either 2d−1 or 2d children, according to the change of regime when r = 1.

The construction outlined above can be regarded as a hybrid between a dyadic decomposition on Rd (caps) and on Rd−1 (sectors), and is convenient to treat the elliptic and conic regimes in a uniﬁed way.

- 4.2. Separated regions. We call two regions adjacent if their closures intersect, possibly at bound-

ary points. We say that two regions κ,κ′ ∈ DN,r are separated, and write κ ∼ κ′ ∈ DN,r, if κ,κ′ are not adjacent, their parents are not adjacent, their 2-parents (i.e. grandparents) are not adjacent, ..., their (d−1)-parents are not adjacent, and their d-parents are adjacent. Naturally, this assumes that r ≤ N/2d, so that κ,κ′ indeed have ancestors up to the d-th generation. The main reason why we climb up d degrees in the genealogical tree when deﬁning separation is to ensure that certain naturally arising geometric regions which contain κ,κ′ are also “separated”. In fact, as will become clear from the proof below, around k generations up in the tree with k ≃ log2 d would morally suﬃce.

If κ,κ′ ∈ DN,r are separated regions, then either: (i) the angular distance between c(κ) and c(κ′)

(which is ≃ N|ωk∗ − ωk∗′|) is comparable to r; or (ii) the radial distance between c(κ) and c(κ′) is comparable to Nr. Note that option (ii) is only available if 0 < r < 2−d.

Deﬁning the regions and the separation between them in this way, we ensure that the union in the forthcoming expression (5.25) is essentially disjoint, an important step in the proof of the reﬁned Strichartz estimate.

- 4.3. Bilinear estimates. If κ ∈ DN,r is a dyadic region as deﬁned in the previous subsection, then we set fκ := f κ. The main result of this section is the following.


- Proposition 3. Let d ≥ 3 and 2(dd+2) ≤ p ≤ 2(dd−+1)1 . Then there exists an exponent 1 ≤ s < 2, which can be taken arbitrarily close to 2, for which the following bilinear extension estimates hold, uniformly in N,r,f,g. Let f,g ∈ L2(Rd) be admissible functions, and let N ≥ 1 be a dyadic number.


![image 88](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile88.png>)

![image 89](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile89.png>)

- (i) If 0 < r ≤ 1 is a dyadic number, and κ ∼ κ′ ∈ DN,r, then

T(fκ)T(gκ′) Lp

![image 90](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile90.png>)

2 (Rd+1) s N−

2

![image 91](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile91.png>)

s r

2d

![image 92](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile92.png>)

s′ −2(dp+2) fκ Ls(Rd) gκ′ Ls(Rd). (4.6)

![image 93](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile93.png>)

- (ii) If 1 < r ≤ N is a dyadic number, and κ ∼ κ′ ∈ DN,r, then


s′ −2(dp+1) fκ Ls(Rd) gκ′ Ls(Rd). (4.7)

2(d−1)

2

2 (Rd+1) s N−

s r

T(fκ)T(gκ′) Lp

![image 94](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile94.png>)

![image 95](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile95.png>)

![image 96](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile96.png>)

![image 97](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile97.png>)

Proof. We ﬁrst establish the estimate in the elliptic regime 0 < r ≤ 1. The proof consists of a rescaling of the bilinear extension result of Tao [17]. We start by constructing aﬃne transformations that map separated caps κ ∼ κ′ ∈ DN,r into unit separated regions.

Boosted caps. Let N ≥ 1 and 0 < r ≤ 1 be dyadic numbers, and let κ ∼ κ′ ∈ DN,r. Let κ, κ′ denote the lifts of the caps κ,κ′ into the hyperboloid Hd, deﬁned as

κ = {(ξ, ξ ) : ξ ∈ κ}, κ′ = {(ξ, ξ ) : ξ ∈ κ′}. (4.8)

be the Lorentz transformation deﬁned in (2.1) with ν = ξ0. Then Lξ

Let ξ0 = c(κ) denote the center of the cap κ as in (4.5), and let Lξ

0

maps κ, κ′ into the lifts λ, λ′ of sets λ := L♭ξ

(κ) and λ′ := L♭ξ

0

0

(κ′) which are contained in r-separated cubes of sidelength comparable to r. Moreover, we can take the center of the cube containing λ to be L♭ξ

0

(ξ0) = 0. Recall that the Lorentz boost Lξ

0

) = 1. Moreover, on κ∪κ′, the map L♭ξ

is volume preserving, det(Lξ

has Jacobian determinant det(DL♭ξ

0

0

0

) ≃ N−1.

0

Parabolic rescaling. The region {(ξ, ξ ) ∈ Rd × R : |ξ| 1} is of elliptic type, in the terminology of [17, Section 9]. The parabolic rescaling

Pr(ξ,τ) := ξr, τr−21 , maps the lifts λ, λ′ deﬁned above to the lifts ρ, ρ′ into the compact hypersurface

![image 98](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile98.png>)

![image 99](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile99.png>)

Σr := ξ, rξr −2 1 : |ξ| 1 (4.9) of O(1)-separated sets ρ,ρ′ of diameter comparable to 1. Let Pr♭ : Rd → Rd denote the map ξ  → r−1ξ, whose Jacobian determinant satisﬁes det(DPr♭) = r−d. Note that Pr♭−1 ◦ Pr♭ = Id, and that Pr is an aﬃne map whose linear part has determinant equal to r−(d+2).

![image 100](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile100.png>)

Bilinear extension of caps. With ρ,ρ′ as deﬁned above, set fρ := f ρ and gρ′ := g ρ′. Let Er denote the Fourier extension operator associated to the hypersurface Σr deﬁned in (4.9),

Er(f)(x,t) :=

eix·ξeitΦ

r(ξ)f(ξ)dξ,

Rd

with phase function given by Φr(ξ) := rξr −2 1. The hypersurfaces {Σr}0<r≤1 are uniformly elliptic in the sense of [18]. As a consequence of Tao’s bilinear extension theorem for general elliptic

![image 101](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile101.png>)

hypersurfaces [17, Section 9], the estimate

 Er(fρ)Er(gρ′) Lq fρ L2 gρ′ L2, q > dd+1+3, (4.10) holds, uniformly in 0 < r ≤ 1. Using the Riesz–Th¨orin convexity theorem to interpolate the latter inequality with the trivial estimate

![image 102](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile102.png>)

 Er(fρ)Er(gρ′) L∞ ≤ fρ L1 gρ′ L1, (4.11) we conclude the existence of s0 < 2, such that

 Er(fρ)Er(gρ′) Lp

fρ Ls gρ′ Ls, (4.12)

![image 103](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile103.png>)

2

for every s ∈ (s0,2). We claim that (4.6) follows from (4.12) by a standard change of variables, which we now present in detail. Start by noting that fρ = fκ ◦ L♭−ξ

◦ Pr♭−1. It follows that

0

fρ sLs =

|fκ(L♭−ξ

0

ρ

◦ Pr♭−1(ξ))|sdξ ≃ (Nrd)−1 fκ sLs, (4.13)

since on κ the change of variables ξ = (Pr♭ ◦ L♭ξ

)(ζ) has Jacobian determinant comparable to det(DPr♭)det(DL♭ξ

0

) ≃ r−dN−1.

0

On the other hand, a straightforward computation shows that

t r2

Er(fρ)(x,t) = r−de−i

![image 104](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile104.png>)

x

r,rt2 )·(ξ,τ)fκ(L−ξ

ei(

(ξ,τ))δ τ2 − ξ 2 ξ dξ dτ,

![image 105](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile105.png>)

![image 106](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile106.png>)

0

Rd+1

(ξ,τ) = (ξ′,τ′) yields

and so another change of variables L−ξ

0

dξ ξ

T

t r2

ξ0(xr,rt2)·(ξ, ξ )fκ(ξ) L♭ξ

eiL

Er(fρ)(x,t) = r−de−i

(ξ)

. This in turn can be rewritten as

![image 107](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile107.png>)

![image 108](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile108.png>)

![image 109](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile109.png>)

![image 110](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile110.png>)

0

Rd

t r2

Er(fρ)(x,t) = r−de−i

(·) )(LTξ

T(fκ L♭ξ

(xr , rt2)), and so, in particular,

![image 111](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile111.png>)

![image 112](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile112.png>)

![image 113](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile113.png>)

0

0

(·) )((LTξ

|Er(fρ)(x,t)| = r−d|T(fκ L♭ξ

◦ Dr)(x,t))|, where Dr denotes the parabolic dilation Dr(x,t) := (xr, rt2). It follows that

0

0

![image 114](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile114.png>)

![image 115](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile115.png>)

p 2

p 2

(·) )T(gκ′ L♭ξ

= r−dprd+2 T(fκ L♭ξ

![image 116](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile116.png>)

![image 117](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile117.png>)

(·) )

Er(fρ)Er(gρ′)

. (4.14)

p 2

p 2

0

0

L

L

![image 118](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile118.png>)

![image 119](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile119.png>)

Since L♭ξ

(ξ) ≃ 1 if ξ ∈ κ ∪ κ′, inequality (4.6) is now easily seen to follow from (4.12), (4.13) and

0

- (4.14). This concludes the veriﬁcation of the elliptic case.


For the conic case 1 < r ≤ N, we can follow a similar path, invoking either Wolﬀ’s bilinear estimates for the cone [20] or a variant on Tao’s estimates for the paraboloid noted in [11]. We choose to take a shortcut, noting that Candy’s recent work [2] on bilinear restriction estimates for general phases already implies the adequate rescaled substitute of (4.10) in the conic regime. More precisely, [2, Theorem 1.10] specializes to the inequality

d+1

T(fκ)T(gκ′) Lq N−1rd−1−

q fκ L2 gκ′ L2, q > dd+3+1. (4.15) As before, this can be interpolated with the trivial

![image 120](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile120.png>)

![image 121](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile121.png>)

T(fκ)T(gκ′) L∞ N−2 fκ L1 gκ′ L1 to yield (4.7). The proof is now complete.

5. A refined Strichartz estimate

There exists a well-established program, using tools from Littlewood–Paley theory, Whitneytype decompositions and quasi-orthogonality, to derive reﬁned inequalities of Strichartz type from bilinear restriction estimates, see for instance the works [1, 9, 10, 14].

The goal of this section is to establish the following reﬁnement of inequality (1.5) which holds for admissible functions in each dyadic annulus.

Theorem 4. Let d ≥ 3 and 2(dd+2) ≤ p ≤ 2(dd−+1)1 . Then there exists γ ∈ (0,1 − p2) such that the following inequality holds

![image 122](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile122.png>)

![image 123](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile123.png>)

![image 124](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile124.png>)

T(fN) pL

(rd)(

p(Rd+1) sup

0<r≤1

p

2−d+2d )(1−γ) sup

![image 125](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile125.png>)

![image 126](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile126.png>)

κ∈DN,r

T(fκ) pγL

p(Rd+1)

p

2−dd−+11)(1−γ) sup

p(Rd+1) fN L p(1−γ)

T(fκ) pγL

(rd−1)(

+ sup

2(Hd), (5.1)

![image 127](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile127.png>)

![image 128](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile128.png>)

1<r≤N

κ∈DN,r

for every dyadic number N ≥ 1 and admissible function f ∈ L2(Hd).

Remark. Both exponents in r appearing on the right-hand side of inequality (5.1) are favorable:

p 2 − d+2d ≥ 0 (in case r ≤ 1) and p2 − dd+1−1 ≤ 0 (in case r > 1), with strict inequality except for the

![image 129](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile129.png>)

![image 130](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile130.png>)

![image 131](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile131.png>)

![image 132](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile132.png>)

case of endpoint exponents.

We start with two technical lemmata which bound certain quantities that will naturally appear in the course of the proof of Theorem 4.

- Lemma 5. Let d ≥ 3 and 2(dd+2) ≤ p ≤ 2(dd−+1)1 . Then the following inequality holds


![image 133](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile133.png>)

![image 134](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile134.png>)

p 2

p 2

![image 135](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile135.png>)

![image 136](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile136.png>)

T(fκ)T(fκ′)

T(fκ)T(fκ′)

p 2 (Rd+1)

p 2 (Rd+1)

L

![image 137](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile137.png>)

L

![image 138](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile138.png>)

0<r≤N κ∼κ′∈DN,r

0<r≤N κ∼κ′∈DN,r

for every dyadic number N ≥ 1 and admissible function f ∈ L2(Hd).

, (5.2)

Proof. Let κ ∈ DN,r be given, and let ξ0 = c(κ) denote its center as in (4.5). For every ξ ∈ κ, one easily checks that

|ξ| − |ξ0| min{1,r}N, (5.3) |ξ||ξ0| − ξ · ξ0

- 1

![image 139](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile139.png>)

- 2


r. (5.4) Indeed, inequality (5.3) follows from the fact that the length along the radial direction of r-caps and r-sectors at scale N is comparable to rN and to N, respectively, and inequality (5.4) amounts to the fact that the angle between the vectors ξ and ξ0 is O(Nr ). Now, given κ ∼ κ′ ∈ DN,r, with corresponding centers ξ0 = c(κ) and ξ0′ = c(κ′), the following estimate follows from the deﬁnition of the separation relation ∼:

![image 140](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile140.png>)

- 1

![image 141](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile141.png>)

- 2


+ |ξ0||ξ0′| − ξ0 · ξ0′ N ≃

|ξ0| − |ξ0′ | N2

r N

. (5.5) Let κ and κ′ be the lifts of the regions κ and κ′ into the hyperboloid Hd as deﬁned in (4.8).

![image 142](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile142.png>)

![image 143](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile143.png>)

![image 144](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile144.png>)

We aim to use [14, Lemma 2.2] (which is a slightly more general version of [9, Lemma A.9] and [18, Lemma 6.1]) to obtain the quasi-orthogonality proposed in (5.2). Our ﬁrst task is to understand the geometry of the sumset

κ + κ′ = (ξ + ξ′, ξ + ξ′ ) : (ξ,ξ′) ∈ κ × κ′ ⊂ Rd+1.

Using (5.3), (5.4) and (5.5), one may reason as in [3, Proof of Prop. 15] to further check that3 ξ + ξ′ − ξ + ξ′ 2 ≃ r

2

N , (5.6)

![image 145](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile145.png>)

|ξ + ξ′| − |ξ0 + ξ0′| min{1,r}N, (5.7) |ξ + ξ′||ξ0 + ξ0′| − (ξ + ξ′) · (ξ0 + ξ0′)

1 2

![image 146](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile146.png>)

r. (5.8)

- Step 1. Observe that (5.6), (5.7) and (5.8) imply that the sumsets κ + κ′ are almost disjoint, in the following sense: There exists a universal constant such that, for any pair (κ,κ′) with κ ∼ κ′ ∈ DN,r, the number of pairs (ρ,ρ′) with ρ ∼ ρ′ ∈ DN,s and

κ + κ′) ∩ ρ + ρ′) = ∅ (5.9)

is bounded by this constant. In fact, if (5.9) occurs, then estimate (5.6) implies the existence of universal constants a,b ∈ Z such that 2ar ≤ s ≤ 2br. Let η0 = c(ρ) denote the center of ρ. Once s is trapped, then (5.3), (5.5) and (5.7) imply that the lengths of |η0| and |ξ0| are not far from each other, in the sense that

|η0| − |ξ0| min{1,r}N. (5.10)

In a similar way, (5.4), (5.5) and (5.8) together imply that the angle between η0 and ξ0 is controlled, that is

|η0||ξ0| − η0 · ξ0

- 1

![image 147](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile147.png>)

- 2


r. (5.11)

Expressions (5.10) and (5.11) imply that, given ξ0, the number of possible choices for η0 in the dyadic decomposition is ﬁnite and universally bounded. For each possible η0 = c(ρ), the number of regions ρ′ separated from ρ is also ﬁnite and universally bounded.

- Step 2. Observe that supp Ft,x[T(fκ)T(fκ′)] ⊂ κ + κ′, (5.12)


where Ft,x denotes the space-time Fourier transform. In order to use [14, Lemma 2.2], it is convenient to place the sumsets κ + κ′ inside regions which are geometrically simpler but still almost disjoint. Expression (5.6) already implies that

2

2

κ + κ′ ⊂ (ξ,τ) ∈ Rd × R : ξ 2 + c1r

N and ξ ∈ κ + κ′ =: Γκ,κ′, (5.13) for some universal constants c1,c2. Note that equations (5.7) and (5.8) imply that the set κ + κ′ lies inside a rectangle centered at γ0 := ξ0 + ξ0′ , of height comparable to min{1,r}N (the major axis being aligned with the vector γ0) and of sidelength comparable to r. Denote this rectangle by Rκ,κ′. Consider a centered dilation4 Rκ,κ∗ ′ := (1 + α) · Rκ,κ′ of Rκ,κ′, with α > 0 suﬃciently small and independent of (κ,κ′), such that the sets

N ≤ τ ≤ ξ 2 + c2r

![image 148](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile148.png>)

![image 149](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile149.png>)

Σκ,κ′ := (ξ,τ) ∈ Rd × R : ξ 2 + c

- 1

![image 150](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile150.png>)

- 2


2

r2 N ≤ τ ≤ ξ 2 + 2c2r

N and ξ ∈ Rκ,κ∗ ′

![image 151](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile151.png>)

![image 152](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile152.png>)

![image 153](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile153.png>)

3Here we use the notation x s := (s2 + |x|2)12 . Estimates (5.6)–(5.8) also appear in [2, Proof of Theorem 2.6]. 4More generally, given a parallelepiped P and λ > 0, we denote by λ · P the centered dilate of P. In other words, if cP denotes the center of P, then λ · P := λ(P − cP ) + cP.

![image 154](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile154.png>)

still have bounded overlap. We may now decompose the collection {(κ,κ′) : κ ∼ κ′} as a union of a ﬁnite (universal) number of subsets whose corresponding {Σκ,κ′} are pairwise disjoint. By the triangle inequality, it suﬃces to bound the sum over just one of these subsets, which we henceforth denote by T .

- Step 3. We claim the existence of a universal number K with the following property: For every (κ,κ′) ∈ T , there exist parallelepipeds {Pℓ = Pℓ(κ,κ′)}Kℓ=1 with disjoint interiors, satisfying


K

Γκ,κ′ ⊂

Pℓ,

ℓ=1

and such that (1 + β) · Pℓ ⊂ Σκ,κ′, for some universal β > 0.

Indeed, given a point γ ∈ Rd, deﬁne T(γ) to be the tangent plane to the hyperboloid Hd2 at the point (γ, γ 2), i.e.

T(γ) := {(γ, γ 2) + v : v ∈ Rd+1, v⊥(γ/ γ 2,−1)}. Let e1,e2,...,ed+1 denote the canonical basis vectors in Rd+1. Without loss of generality, assume γ0 to be parallel to ed. At a vector ted, the slope of the tangent to the hyperbola {(ted, t 2) : t ∈ R} equals t/ t 2. We may then consider a point γ = ted suﬃciently close to γ0, and the corresponding hyperplane

T(γ) = {(γ, γ 2) + (x1,x2,...,xd−1,xd,xd t/ t 2) with each xi ∈ R}.

Lifting the rectangle Rκ,κ′ to the hyperplane T(γ) amounts to choosing |(x1,x2,...,xd−1)| r and xd ≃ min{1,r}N. Set y = (x1,x2,...,xd−1), and assume

|y| ≤ c3r and |xd| ≤ c4 min{1,r}N, (5.14)

for some constants c3,c4 which are yet to be chosen. Under these assumptions, we may estimate the largest displacement in the vertical direction ed+1 between the hyperplane T(γ) and the hyperboloid Hd2 as follows. Recalling that t ≃ N, this displacement is given by

4x2d + |y|2(4 + t2) N3

txd √4 + t2 ≃

![image 155](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile155.png>)

![image 156](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile156.png>)

4 + (t + xd)2 + |y|2 − 4 + t2 +

.

![image 157](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile157.png>)

![image 158](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile158.png>)

![image 159](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile159.png>)

By choosing the constants c3,c4 suﬃciently small (but universal), we can bound this displacement from above by δ c

r2 N , where δ < 1 is chosen so c2 + δc

10 < 3c

2 , i.e. δ < 5c

c1 , where c1,c2 are the universal constants appearing in the deﬁnition (5.13) of Γκ,κ′. This implies the existence of a constant K, such that the original rectangle Rκ,κ′ can be decomposed into a union of K smaller rectangles {Rℓ = Rℓ(κ,κ′)}Kℓ=1 of the same size having disjoint interiors and verifying conditions

1

2

2

1

![image 160](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile160.png>)

![image 161](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile161.png>)

![image 162](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile162.png>)

![image 163](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile163.png>)

![image 164](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile164.png>)

10

- (5.14). We again emphasize that, once c3 and c4 are chosen, the number K is universal.


For each ℓ, let αℓ be the center of the rectangle Rℓ, and let T(Rℓ) denote the lift of Rℓ into the hyperplane T(αℓ). Deﬁne the region Pℓ = Pℓ(κ,κ′) ⊂ Rd+1 as the sumset

2

2

N ≤ s ≤ (c2 + δc

10 )r

Pℓ := T(Rℓ) + {sed+1 : c1r

N }.

1

![image 165](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile165.png>)

![image 166](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile166.png>)

![image 167](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile167.png>)

Note that each Pℓ is a parallelepiped lying above the hyperboloid Hd2 of height comparable to r2/N. Moreover, distinct elements of the family {Pℓ}Kℓ=1 have disjoint interiors. Further observe that

K

κ + κ′ ⊂ Γκ,κ′ ⊂

Pℓ. (5.15)

ℓ=1

It follows from the construction of Rκ,κ∗ ′ and {Rℓ} that there exists β > 0, such that (1 + β) · Rℓ ⊂ Rκ,κ∗ ′, for every ℓ ∈ {1,2,...,K}. From the aforementioned displacement considerations and the choice of δ (by possibly choosing a smaller β, depending only on c1,c2), we may guarantee that the parallelepipeds {Pℓ} further satisfy

(1 + β) · Pℓ ⊂ Σκ,κ′. (5.16) This concludes the the veriﬁcation of claim.

. The estimate

- Step 4. Deﬁne ψℓ := P


ℓ

f ∗ ψℓ Lq(Rd+1) ≤ C f Lq(Rd+1), (5.17) which holds for any exponent q > 1, follows from a simple application of the boundedness of the Hilbert transform, yielding a constant C = Cq,d < ∞ that does not depend on ℓ nor on (κ,κ′). By the support considerations from (5.12) and (5.15), we have that

T(fκ)T(fκ′) =

K

(T(fκ)T(fκ′)) ∗ ψℓ.

ℓ=1

By the triangle inequality, it suﬃces to establish the estimate

p 2

![image 168](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile168.png>)

(T(fκ)T(fκ′)) ∗ ψℓ

T(fκ)T(fκ′)

p 2 (Rd+1)

L

![image 169](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile169.png>)

(κ,κ′)∈T

(κ,κ′)∈T

for each ℓ ∈ {1,2,...,K}. From [14, Lemma 2.2], we have that

p 2

![image 170](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile170.png>)

(T(fκ)T(fκ′)) ∗ ψℓ

(T(fκ)T(fκ′)) ∗ ψℓ

p 2 (Rd+1)

L

![image 171](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile171.png>)

(κ,κ′)∈T

(κ,κ′)∈T

p 2

![image 172](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile172.png>)

, (5.18)

p 2 (Rd+1)

L

![image 173](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile173.png>)

p 2

![image 174](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile174.png>)

. (5.19)

p 2 (Rd+1)

L

![image 175](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile175.png>)

In fact, the Fourier transform of each function (T(fκ)T(fκ′)) ∗ ψℓ is supported in Pℓ, and as we have seen there exists β > 0 such that the elements in the family {(1 + β) · Pℓ}(κ,κ′)∈T are pairwise disjoint. Moreover, for each (κ,κ′) ∈ T , one easily constructs a function ϕ = ϕ(κ,κ′) satisfying

supp(ϕ) ⊂ (1 + β) · Pℓ,

ϕ(x) ≡ 1, if x ∈ Pℓ, ϕ L1(Rd+1) ≤ C,

where the constant C is uniform in (κ,κ′). One just has to observe that each parallelepiped Pℓ is an aﬃne image of the unit cube. Therefore (5.19) follows from a direct application of [14, Lemma 2.2]. To ﬁnish, invoke (5.17) with q = p/2 > 1 in order to obtain (5.18) from (5.19). The proof is now complete.

- Lemma 6. Let d ≥ 3 and 2(dd+2) ≤ p ≤ 2(dd−+1)1 . Let 1 ≤ s < 2 and 0 < γ < 1 − p2. Then the following inequality holds


![image 176](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile176.png>)

![image 177](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile177.png>)

![image 178](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile178.png>)

p

2(1−γ) fN L p(1−γ)

2

|κ|1−

s fκ 2Ls(Rd)

![image 179](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile179.png>)

2(Rd), (5.20)

![image 180](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile180.png>)

0<r≤N κ∈DN,r

for every dyadic number N ≥ 1 and admissible function f ∈ L2(Hd).

Proof. We may assume that fN L2 = 1. The strategy, suggested by the proof of [1, Theorem 1.3], amounts to decomposing the function fN into low and high frequencies, depending on the size of the region κ. More precisely, write

2}fN =: fN≤ + fN>. Set α := p2(1 − γ). To estimate the low frequencies, use Ho¨lder’s inequality to bound fN≤ Ls(κ) ≤ |κ|

fN = {|f|≤|κ|

2}fN + {|f|>|κ|

− 1

− 1

![image 181](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile181.png>)

![image 182](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile182.png>)

![image 183](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile183.png>)

1

s−21α fN≤ L2α(κ), which holds provided 2α ≥ s, or equivalently γ ≤ 1 − ps. In this case,

![image 184](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile184.png>)

![image 185](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile185.png>)

![image 186](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile186.png>)

α

2

s fN≤ 2Ls(κ)

|κ|α−1 fN≤ 2Lα2α(κ). (5.21)

|κ|1−

![image 187](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile187.png>)

0<r≤N κ∈DN,r

0<r≤N κ∈DN,r

Let VN,r denote the volume of a region κ ∈ DN,r. Recall that VN,r ≃ Nrd when 0 < r ≤ 1, and that VN,r ≃ Nrd−1 when 1 < r < N. The right-hand side of (5.21) can be estimated as follows:

|κ|α−1 fN≤ 2Lα2α(κ)

(VN,r)α−1 |f(ξ)|2αdξ. (5.22)

|ξ|≃N 0<r≤N: |f(ξ)|≤(VN,r)− 12

0<r≤N κ∈DN,r

![image 188](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile188.png>)

Thus the sum on the right-hand side of (5.22) amounts to two geometric series, both of which can be estimated by their largest terms:

|f(ξ)|−2(α−1)|f(ξ)|2αdξ = fN 2L2 = 1.

(VN,r)α−1 |f(ξ)|2αdξ

|ξ|≃N 0<r≤N: |f(ξ)|≤(VN,r)− 12

|ξ|≃N

![image 189](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile189.png>)

Note that the latter inequality only holds provided α − 1 > 0, or equivalently γ < 1 − p2, which is a valid constraint since p > 2.

![image 190](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile190.png>)

To estimate the high frequencies, use Minkowski’s inequality to bound

 

 

2α s

![image 191](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile191.png>)

α

2

s

|κ|1−

s fN> 2Ls(κ)

2−1 fN> sLs(κ)

≤

|κ|

,

![image 192](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile192.png>)

![image 193](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile193.png>)

0<r≤N κ∈DN,r

0<r≤N κ∈DN,r

which as before holds provided 2α ≥ s. The right-hand side of this expression can be estimated as before:

s

s

2−1 fN> sLs(κ)

2−1 |f(ξ)|sdξ

|κ|

(VN,r)

![image 194](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile194.png>)

![image 195](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile195.png>)

|ξ|≃N 0<r≤N: |f(ξ)|>(VN,r)− 12

0<r≤N κ∈DN,r

![image 196](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile196.png>)

s

|f(ξ)|−2(

2−1)|f(ξ)|sdξ = fN 2L2 = 1. This concludes the veriﬁcation of (5.20).

![image 197](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile197.png>)

|ξ|≃N

We are now ready for the proof of the reﬁned Strichartz inequality.

Proof of Theorem 4. We recall the following simple geometric observation: Given dyadic numbers N ≥ 1 and 0 < r ≤ N, and a region κ ∈ DN,r, the number of regions κ′ ∈ DN,r which are separated from κ is universally bounded. In other words,

#{κ′ : κ ∼ κ′ ∈ DN,r} d 1. (5.23) Via a standard decomposition argument, see [1, 18], we have that

p 2

![image 198](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile198.png>)

T(fN) pLp =

. (5.24)

T(fκ)T(fκ′)

p 2

0<r≤N κ∼κ′∈DN,r

L

![image 199](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile199.png>)

To verify this, recall the deﬁnition (4.2) of the restricted annulus AN, and consider the diagonal Γ := {(ξ,η) ∈ AN × AN : ξ = η}.

Then the following Whitney-type decomposition is a consequence of the construction performed in Section 4:

κ × κ′. (5.25)

(AN × AN) \ Γ =

0<r≤N κ∼κ′∈DN,r

p 2

Identity (5.24) follows from this by writing T(fN) pLp = T(fN)2

![image 200](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile200.png>)

. By Lemma 5, we then have

p 2

L

![image 201](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile201.png>)

p 2

T(fN) pLp

![image 202](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile202.png>)

T(fκ)T(fκ′)

. (5.26)

p 2

L

![image 203](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile203.png>)

0<r≤N κ∼κ′∈DN,r

On the one hand, each of these summands can be bounded by Ho¨lder’s inequality as follows:

≤ T(fκ) γLp T(fκ′) γLp T(fκ)T(fκ′) 1−γ

, (5.27)

T(fκ)T(fκ′) Lp

p 2

![image 204](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile204.png>)

2

L

![image 205](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile205.png>)

where γ ∈ (0,1) is a parameter to be chosen below. On the other hand, we can split the sum on the right-hand side of (5.26) into two pieces, depending on whether 0 < r ≤ 1 or 1 < r ≤ N. Let us

focus on the ﬁrst sum, that over caps. We claim that

p 2

2−d+2d )(1−γ) T(fκ) pγLp

p

p

(rd)(

N−

2(1−γ) sup

![image 206](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile206.png>)

sup

T(fκ)T(fκ′)

![image 207](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile207.png>)

![image 208](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile208.png>)

![image 209](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile209.png>)

p 2

L

![image 210](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile210.png>)

0<r≤1

κ∈DN,r

0<r≤1 κ∼κ′∈DN,r

p

2(1−γ). (5.28)

2

s fκ 2Ls

|κ|1−

![image 211](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile211.png>)

×

![image 212](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile212.png>)

0<r≤1 κ∈DN,r

This follows from inequality (5.27), the case f = g of the bilinear extension estimate (4.6), and the observation (5.23) that allows to bound the double sum κ∼κ′ by a single sum κ. One just has to recall that the Lebesgue measure of an r-cap at scale N is comparable to Nrd.

Lemma 6 then implies that the last factor on the right-hand side of inequality (5.28) is O( fN L p(12 −γ)), provided γ < 1 − 2p. As a consequence, the following inequality for r-caps at scale N holds:

![image 213](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile213.png>)

0<r≤1 κ∼κ′∈DN,r

T(fκ)T(fκ′)

p 2

![image 214](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile214.png>)

p 2

L

![image 215](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile215.png>)

(rd)(

sup

sup

κ∈DN,r

0<r≤1

2−d+2d )(1−γ) T(fκ) pγLp fN L p(1−γ)

p

2(Hd). (5.29)

![image 216](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile216.png>)

![image 217](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile217.png>)

In a similar way, recalling that the Lebesgue measure of an r-sector at scale N is comparable to Nrd−1, and using (4.7) instead of (4.6), one can show the corresponding inequality for r-sectors at scale N,

1<r≤N κ∼κ′∈DN,r

T(fκ)T(fκ′)

p 2

![image 218](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile218.png>)

p 2

L

![image 219](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile219.png>)

p

2−dd−+11)(1−γ) T(fκ) pγLp fN L p(1−γ)

(rd−1)(

sup

sup

2(Hd), (5.30)

![image 220](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile220.png>)

![image 221](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile221.png>)

1<r≤N

κ∈DN,r

under the same assumption γ < 1 − 2p. Inequality (5.1) follows from (5.26), (5.29) and (5.30). The proof is now complete.

![image 222](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile222.png>)

6. End of the proof: concentration-compactness As we left oﬀ in Section 3, let {fn}n∈N ⊂ L2(Hd) be an extremizing sequence for (1.5), with

fn L2(Hd) = 1 for all n ∈ N, and let {fn(k0)}n∈N be a quasi-extremizing sequence in the sense of (3.1). Assuming without loss of generality that k0 = 1, the sequence {fn(1)}n∈N belongs to our class of admissible functions considered in Sections 4 and 5.

From Proposition 2, for each n ∈ N, there exists N = Nn ∈ 2Z≥0 such that T (fn(1))N) L

p(Rd+1) ≥ δ3,

- where δ3 > 0 is a universal constant.


If 2(dd+2) ≤ p < 2(dd−+1)1 , then Theorem 4 ensures for each n ∈ N the existence of a dyadic number r = rn satisfying r ≤ 2α for a universal constant α, and of a region κ = κn ∈ DN,r, such that

![image 223](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile223.png>)

![image 224](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile224.png>)

T (fn(1))κ L

p(Rd+1) ≥ δ4,

- where δ4 > 0 is a universal constant. This implies at once that (fn(1))κ L2(Hd) ≥ δ5,
- where δ5 > 0 is a universal constant. Set Ln := Lc(κ), where c(κ) denotes as usual the center of

the region κ. Since r ≤ 2α, a standard computation shows that the image L♭n(κ) is contained in a universal ball B ⊂ Rd centered at the origin. Therefore

L∗nfn(1) L2(B) ≥ δ6,

- where δ6 > 0 is a universal constant. As already observed in Section 3, this plainly implies that L∗nfn L2(B) ≥ δ6.


This establishes the existence of distinguished region when 2(dd+2) ≤ p < 2(dd−+1)1 .

![image 225](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile225.png>)

![image 226](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile226.png>)

We can now invoke the machinery of [3, Section 6], which only works when 2(dd+2) < p ≤ 2(dd−+1)1 , to arrive at the existence of extremizers stated in Theorem 1 in the non-endpoint range 2(dd+2) < p < 2(dd−+1)1 . We provide the details below.

![image 227](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile227.png>)

![image 228](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile228.png>)

![image 229](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile229.png>)

![image 230](<2018-carneiro-extremizers-adjoint-fourier-restriction_images/imageFile230.png>)

By [3, Proposition 18], there exists (xn,tn) ∈ Rd × R such that the sequence {hn}n∈N deﬁned by hn(ξ) := eix

n·ξeit

n ξ fn(ξ)

admits a subsequence that converges weakly to a nonzero limit, say h = 0, in L2(Hd). For this subsequence, possibly after extracting a further subsequence, [3, Proposition 19] implies

T(hn)(x,t) → T(h)(x,t), as n → ∞,

for almost every (x,t) ∈ Rd × R. The existence of extremizers then follows from a straightforward application of [4, Proposition 1.1]. This completes the proof of Theorem 1.

Acknowledgements

The authors are thankful to Rupert Frank and Ren´e Quilodr´an for helpful comments and suggestions. E.C. acknowledges support from CNPq - Brazil, FAPERJ - Brazil and the Simons Associate Scheme from the International Centre for Theoretical Physics (ICTP) - Italy. D.O.S. was partially supported by the Hausdorﬀ Center for Mathematics, the Deutsche Forschungsgemeinschaft through the Collaborative Research Center 1060, and the College Early Career Travel Fund of the University of Birmingham. M.S. acknowledges support from the grant PICT 2014-1480 (ANPCyT). B.S. was supported by a National Science Foundation grant (DMS-1600458).

References

- [1] P. B´egout and A. Vargas, Mass concentration phenomena for the L2-critical nonlinear Schr¨odinger equation, Trans. Amer. Math. Soc. 359 (2007), no. 11, 5257–5282.
- [2] T. Candy, Multi-scale bilinear restriction estimates for general phases, Preprint, 2017, arXiv:1707.08944.
- [3] E. Carneiro, D. Oliveira e Silva and M. Sousa, Extremizers for Fourier restriction on hyperboloids, Preprint, 2017, arXiv:1708.03826. To appear in Ann. Inst. H. Poincar´e Anal. Non Lin´eaire.


- [4] L. Fanelli, L. Vega and N. Visciglia, On the existence of maximizers for a family of restriction theorems, Bull. Lond. Math. Soc. 43 (2011), no. 4, 811–817.
- [5] R. Frank, E. H. Lieb and J. Sabin, Maximizers for the Stein–Tomas inequality, Geom. Funct. Anal. 26 (2016), no. 4, 1095–1134.
- [6] R. Frank and J. Sabin, Extremizers for the Airy–Strichartz inequality, Preprint, 2017, arXiv:1712.04156. To appear in Math. Ann.
- [7] J. Jiang, S. Shao and B. Stovall, Linear proﬁle decompositions for a family of fourth order Schr¨odinger equations, Preprint, 2014. arXiv:1410.7520.
- [8] J. Kato and T. Ozawa, Endpoint Strichartz estimates for the Klein–Gordon equation in two space dimensions and some applications, J. Math. Pures Appl. (9) 95 (2011), no. 1, 48–71.
- [9] R. Killip and M. Visan, Nonlinear Schr¨odinger equations at critical regularity, Evolution equations, 325–437, Clay Math. Proc. 17, Amer. Math. Soc., Providence, RI, 2013.
- [10] R. Killip, B. Stovall and M. Visan, Scattering for the cubic Klein–Gordon equation in two space dimensions, Trans. Amer. Math. Soc. 364 (2012), no. 3, 1571–1631.
- [11] S. Lee and A. Vargas, Restriction estimates for some surfaces with vanishing curvatures, J. Funct. Anal. 258

(2010), no. 9, 2884–2909.

- [12] R. Quilodran´ , Nonexistence of extremals for the adjoint restriction inequality on the hyperboloid, J. Anal. Math. 125 (2015), 37–70.
- [13] R. Quilodran´ , Existence of extremals for a Fourier restriction inequality on the one sheeted hyperboloid, Preprint, 2018.
- [14] J. Ramos, A reﬁnement of the Strichartz inequality for the wave equation with applications, Adv. Math. 230

(2012), no. 2, 649–698.

- [15] E. M. Stein, Harmonic Analysis: Real-Variable Methods, Orthogonality, and Oscillatory Integrals, Princeton University Press, Princeton, NJ, 1993.
- [16] R. S. Strichartz, Restrictions of Fourier transforms to quadratic surfaces and decay of solutions of wave equations, Duke Math. J. 44 (1977), no. 3, 705–714.
- [17] T. Tao, A sharp bilinear restriction estimate for paraboloids, Geom. Funct. Anal. 13 (2003), no. 6, 1359–1384.
- [18] T. Tao, A. Vargas and L. Vega, A bilinear approach to the restriction and Kakeya conjectures, J. Amer. Math. Soc. 11 (1998), no. 4, 967–1000.
- [19] P. Tomas, A restriction theorem for the Fourier transform, Bull. Amer. Math. Soc. 81 (1975), no. 2, 477–478.
- [20] T. Wolff, A sharp bilinear cone restriction estimate, Ann. of Math. (2) 153 (2001), no. 3, 661–698.


IMPA - Instituto de Matematica´ Pura e Aplicada, Rio de Janeiro - RJ, Brazil, 22460-320. E-mail address: carneiro@impa.br

University of Birmingham, Edgbaston, Birmingham, B15 2TT, England. E-mail address: d.oliveiraesilva@bham.ac.uk

Ludwig-Maximilans Universitat¨ Munchen,¨ Theresienstr. 39, 80333 Munchen,¨ Germany. E-mail address: sousa@math.lmu.de

University of Wisconsin–Madison, 480 Lincoln Drive, Madison, Wisconsin, USA, 53706. E-mail address: stovall@math.wisc.edu

