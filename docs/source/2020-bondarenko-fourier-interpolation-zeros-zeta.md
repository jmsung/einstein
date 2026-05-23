---
type: source
kind: paper
title: Fourier interpolation with zeros of zeta and $L$-functions
authors: Andriy Bondarenko, Danylo Radchenko, Kristian Seip
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2005.02996v3
source_local: ../raw/2020-bondarenko-fourier-interpolation-zeros-zeta.pdf
topic: general-knowledge
cites:
---

arXiv:2005.02996v3[math.NT]3Nov2022

FOURIER INTERPOLATION WITH ZEROS OF ZETA AND L-FUNCTIONS

ANDRIY BONDARENKO, DANYLO RADCHENKO, AND KRISTIAN SEIP

Abstract. We construct a large family of Fourier interpolation bases for functions analytic in a strip symmetric about the real line. Interesting examples involve the nontrivial zeros of the Riemann zeta function and other L-functions. We establish a duality principle for Fourier interpolation bases in terms of certain kernels of general Dirichlet series with variable coeﬃcients. Such kernels admit meromorphic continuation, with poles at a sequence dual to the sequence of frequencies of the Dirichlet series, and they satisfy a functional equation. Our construction of concrete bases relies on a strengthening of Knopp’s abundance principle for Dirichlet series with functional equations and a careful analysis of the associated Dirichlet series kernel, with coeﬃcients arising from certain modular integrals for the theta group.

Contents

- 1. Introduction 2 Outline of the paper 6
- 2. Generalities on Fourier interpolation 6

- 2.1. The Dirichlet series kernel associated with Λ 7
- 2.2. The Dirichlet series kernel associated with Λ∗ 9
- 2.3. Examples 11
- 2.4. The joint density of Λ and Λ∗ 12
- 2.5. Fourier interpolation and crystalline measures 13


- 3. Modular integrals for the theta group 14

- 3.1. Preliminaries on the theta group 15
- 3.2. Modular forms for the theta group 16
- 3.3. Modular kernels 18
- 3.4. Deﬁnition and basic properties of Fk±(τ, s) 20


- 4. The Dirichlet series kernel associated with zeros of ζ(s) 23


- 4.1. The Mellin transform of Fk±(τ, s) 23
- 4.2. Construction of the Dirichlet series kernels 26
- 4.3. Proof of Theorem 1.1 27
- 4.4. Relation with the Riemann–Weil formula 30
- 5. Fourier interpolation with zeros of Dirichlet L-functions and other Dirichlet series 30


![image 1](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile1.png>)

2010 Mathematics Subject Classiﬁcation. 11M06, 11F37, 42A38. Bondarenko and Seip were supported in part by Grant 275113 of the Research Council of Norway.

1

- 5.1. Fourier interpolation bases associated with even primitive characters 31

- 5.2. Fourier interpolation bases associated with odd characters 33

- 5.3. Fourier interpolation with zeros of other Dirichlet series 34
- 6. Estimates for the Fourier coeﬃcients of Fk±(τ, s) 37


- 6.1. Estimates for the contour integral 37


- 6.2. Estimates for Fk±(τ, ϕ) near the real line 40


- 6.3. Estimates for the Fourier coeﬃcients 41


- 6.4. Estimate for I(τ) 44


- 6.5. Estimate for N(τ) 45
- 7. The Fourier interpolation basis of Theorem A revisited 46 References 49


1. Introduction

The Riemann–Weil explicit formula (sometimes also called the Guinand–Weil explicit formula) expresses the familiar duality between the prime numbers and the nontrivial zeros of the Riemann zeta function ζ(s) in the following compelling way:

∞

Γ′(1/4 + it/2) Γ(1/4 + it/2) − log π dt + f

+ f −i 2

i 2

- 1

![image 2](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile2.png>)

- 2π


f(t)

![image 3](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile3.png>)

![image 4](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile4.png>)

![image 5](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile5.png>)

−∞

∞

ρ − 1/2 i

log n 2π

log n 2π

Λ(n) √n

- 1

![image 6](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile6.png>)

- 2π


+ f −

- (1.1) .


+

f

f

=

![image 7](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile7.png>)

![image 8](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile8.png>)

![image 9](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile9.png>)

![image 10](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile10.png>)

![image 11](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile11.png>)

ρ

n=1

Here f(z) is a function analytic in the strip | Im z| < 1/2 + ε for some ε > 0, |f(z)| ≪ (1 + |z|)−1−δ for some δ > 0 when | Re z| → ∞, and

∞

f(x)e−2πixξdx;

f(ξ) :=

−∞

Λ(n) is the von Mangoldt function deﬁned to be log p if n = pk, p a prime and k ≥ 1, and zero otherwise, while the second sum in (1.1) runs over the nontrivial zeros ρ of ζ(s) (counting multiplicities in the usual way). The Riemann–Weil formula generalizes the classical Riemann–von Mangoldt explicit formula [4, Ch. 17] and arose to prominence from Weil’s work [30], in which it appeared in a considerably more general form.

Our nontraditional emplacement of the two series in (1.1) on one side of the equation is made to connect the Riemann–Weil formula to the object of study of this paper, the prototype of which is another Fourier duality relation involving the nontrivial zeros of ζ(s). We follow the convention of denoting these zeros by ρ = β + iγ, but instead of accounting for multiple zeros (if any) in the usual way, we associate with each ρ the multiplicity m(ρ) of the zero of ζ(s) at ρ. We let H1 denote the space of functions f(z) that are analytic in the strip | Im z| < 1/2 + ε and satisfy the integrability condition

∞

|f(x + iy)|(1 + |x|)dx < ∞

sup

|y|<1/2+ε

−∞

for some ε > 0. Functions h(z) on C with the property that

h(x + iy) ≪y,l (1 + |x|)−l for every real y and positive l will be said to be rapidly decaying. To simplify matters, we state our result only for even functions.

- Theorem 1.1. There exist two sequences of rapidly decaying and even entire functions Un(z), n = 1, 2, ..., and Vρ,j(z), 0 ≤ j < m(ρ), with ρ ranging over the nontrivial zeros of ζ(s) with positive imaginary part, such that for every even function f in H1 and every z = x + iy in the strip |y| < 1/2 we have


- (1.2) f(z) =

∞

n=1

f

log n 4π

![image 12](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile12.png>)

Un(z) + lim

k→∞ 0<γ≤Tk

m(ρ)−1

j=0

f(j)

ρ − 1/2 i

![image 13](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile13.png>)

Vρ,j(z)

for some increasing sequence of positive numbers T1, T2, . . . tending to ∞ that does not depend on neither f nor on z. Moreover, the functions Un(z) and Vρ,j(z) enjoy the following interpolatory properties:

- (1.3)


′

Un(j) ρ−i1/2 = 0, Un logn

4π = δn,n′, V (j

![image 14](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile14.png>)

![image 15](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile15.png>)

′) ρ,j

ρ′−1/2

i = δ(ρ,j),(ρ′,j′), Vρ,j log4πn = 0,

![image 16](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile16.png>)

![image 17](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile17.png>)

with ρ, ρ′ ranging over the nontrivial zeros of ζ(s) with positive imaginary part, j, j′ over all nonnegative integers less than or equal to respectively m(ρ)−1, m(ρ′)−1, and n, n′ over all positive integers.

As an immediate corollary we get the following result that appears to be diﬃcult to obtain without relying on the interpolation formula from Theorem 1.1.

Corollary 1.1. (i) If an even function f in H1 satisﬁes f(log4πn) = f(j)(ρ−i1/2) = 0 for all n ≥ 1 and 0 ≤ j < m(ρ), where ρ ranges over the nontrivial zeros of ζ(s), then f vanishes

![image 18](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile18.png>)

![image 19](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile19.png>)

identically.

(ii) An even function f in H1 that is divisible by ζ(21+is) (in the sense that f(s)/ζ(21+is) is holomorphic for | Im z| < 1/2 + ε) is uniquely determined by the values f(log4πn), n ≥ 1.

![image 20](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile20.png>)

![image 21](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile21.png>)

![image 22](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile22.png>)

It is worth emphasizing that both Theorem 1.1 and the above corollary are rather sensitive to the choice of interpolation points and break down if one removes any single point from the set {log4πn}n≥1 or from the (multi)set of nontrivial zeros of ζ(s).

![image 23](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile23.png>)

Both (1.1) and (1.2) rely crucially on the functional equation π−s/2Γ(s/2)ζ(s) = π−(1−s)/2Γ((1 − s)/2)ζ(1 − s),

but a principal distinction between them is that the deduction of the Riemann-Weil formula starts from the Euler product representation of ζ(s), while formula (1.2) is tied to the Dirichlet series representation of ζ(s). Hence we may think of the two formulas as expressing respectively a multiplicative and an additive duality relation between the zeta zeros and a distinguished sequence of integers. We observe that the sequence of integers in-

volved in (1.1) (the prime powers n = pk, corresponding to the nontrivial terms Λ(n) f(log2πn)

![image 24](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile24.png>)

in (1.1)) is a rather sparse subsequence of the corresponding sequence appearing in (1.2) (the square-roots of the positive integers, corresponding to f(log

√n

![image 25](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile25.png>)

2π ) in (1.2)).

![image 26](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile26.png>)

In view of this inclusion, we may think of (1.1) as arising from (1.2) in the following way: The left-hand side of (1.1) deﬁnes a linear functional on H1, while the right-hand side gives the representation of this functional with respect to the basis functions of Theorem 1.1. This is the rationale for our way of writing the Riemann–Weil formula.

Assuming for a moment the truth of the Riemann hypothesis and that all the zeta zeros are simple, we may think of a formula like (1.2) as a conﬁrmative answer to the following Fourier analytic question: Is it possible to recover, in a non-redundant way, any suﬃciently nice function f on the real line from samples of f and its Fourier transform f along two suitably chosen sequences in respectively the time and frequency domain? Here the recovery being non-redundant means that it fails as soon as any point is removed from either of the two sequences. Clearly, such a favorable situation requires a delicate interplay between the two sequences.

Radchenko and Viazovska [25] have shown that one obtains a Fourier interpolation formula of desired type by choosing both sequences to be ±

√n with n ranging over the nonnegative integers. For simplicity, we restrict again to the case of even functions. Theorem A ([25]). There exists a sequence of even Schwartz functions an: R → R with the property that for every even Schwartz function f : R → R we have

![image 27](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile27.png>)

- (1.4) f(x) =

∞

n=0

f(√n)an(x) +

![image 28](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile28.png>)

∞

n=0

f(√n) an(x),

![image 29](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile29.png>)

where each of the two series on the right-hand side converges absolutely for every real x. The functions an satisfy the following interpolatory properties: an(√m) = δn,m and an(√m) = 0 when m ≥ 1, and in addition

![image 30](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile30.png>)

![image 31](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile31.png>)

- (1.5) a0(0) = a0(0) =


- 1

![image 32](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile32.png>)

- 2


, an2(0) = − an2(0) = −1, an(0) = − an(0) = 0 otherwise.

The non-redundancy of the representation (1.4) follows from the speciﬁc properties of the functions an as shown in [25]. We note in passing that the methods developed in the present paper allow us to sharpen this result considerably (see Section 7 below).

Returning to the general discussion, we note that the properties (1.5) show that (1.4) becomes the Poisson summation formula when evaluated at x = 0. We have therefore a curious analogy between the Poisson summation and Riemann–Weil formulas: They can both be viewed as representing distinguished linear functionals in terms of a Fourier interpolation basis. Both formulas owe their existence and importance to an inherent algebraic structure, which in the ﬁrst case is additive (periodicity) and in the latter multiplicative.

To construct our interpolation formulas, we will use weakly holomorphic modular forms for the theta group. The core ingredient in our construction is a function of two complex variables w and s, which in the case of even functions takes the form

∞

βn(s)n−w/2,

D(w, s) :=

n=1

with βn(s) being the Fourier coeﬃcients of a certain 2-periodic analytic function on the upper half-plane that is related through a Mellin transform to the functions F+(x, τ) considered in [25]. The Dirichlet series w  → D(w, s) converges absolutely in a half-plane depending on s and has a meromorphic extension to C with simple poles at the three points 1, s, 1 − s. A crucial point is that D(w, s) is related to the Riemann zeta function in the following precise way:

- (1.6) H(w, s) :=

ζ(s) ζ(w)

![image 33](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile33.png>)

D(w, s)

satisﬁes the functional equations H(1−w, s) = −H(w, s) and H(w, 1−s) = H(w, s). These properties of H(w, s), along with suitable estimates for D(w, s) and a familiar contour integration argument applied to

- (1.7)


1/2+ε+i∞

w − 1/2 i

1 2πi

H(w, iz + 1/2)dw,

f

![image 34](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile34.png>)

![image 35](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile35.png>)

1/2+ε−i∞

are what we will use to establish Theorem 1.1. It is essential that H(w, s) is a Dirichlet series in w so that (1.7) produces a weighted sum of Fourier transforms of f.

We may now observe that if we replace ζ(s)/ζ(w) by F(s)/F(w) in (1.6), with F(s) an L-function satisfying a functional equation of the form

Q−sΓ(s/2)F(s) = Q−(1−s)Γ((1 − s)/2)F(1 − s)

![image 36](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile36.png>)

![image 37](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile37.png>)

for some positive Q, then we still have a Dirichlet series in the variable w that is amenable to our method of proof. This observation allows us to associate Fourier interpolation bases with the nontrivial zeros of all such L-functions. Hence the single function D(w, s) generates an abundance of Fourier interpolation bases. We stress that this situation relies on a special multiplicative structure inherent in the present setting, namely that the class of Dirichlet series over exponentials of the form n−w/2 is closed under multiplication.

The general phenomenon of Fourier interpolation bases may be thought of as ranging from Theorem A via our Theorem 1.1 to the “degenerate” situation related to the cardinal series

∞

sinπ(z − n) π(z − n)

f(n)

.

![image 38](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile38.png>)

n=−∞

We ﬁnd it enlightening to place our results in this more general context by considering two necessary conditions for a pair of sequences to generate Fourier interpolation bases. First, we show that the existence of a kernel function with properties similar to those of the function H(w, s) is a prerequisite for Fourier interpolation. This observation yields a precise notion of duality between the two sequences involved in a Fourier interpolation basis, closely aligned with modular relations as for example studied in some generality by Bochner [3]. Second, we discuss a recent density theorem of Kulikov [20], which is a version of the uncertainty principle valid for Fourier interpolation bases. We observe that there is a precise correspondence between Kulikov’s density condition and the Riemann–von Mangoldt formula for the density of the nontrivial zeros of zeta and L-functions.

Outline of the paper. We will begin our discussion in Section 2 with some general considerations as outlined in the preceding paragraph. We have included in this section also a brief subsection pointing out that Fourier interpolation bases generate families of “crystalline” measures, a topic that in our context goes back to Guinand [9] and that recently has received notable attention. See for example the recent papers of Kurasov and Sarnak [21], Lev and Olevskii [22], and Meyer [23].

We then proceed in Section 3 to construct the modular integrals that are used to build the Dirichlet series D(w, s) referred to above. This requires a fairly comprehensive discussion of modular forms for the theta group. This section builds largely on ideas that go back to Knopp [15], with an important additional ingredient from [25], namely, the construction of modular integrals using contour integrals with modular kernels.

Based on the groundwork laid in Section 3, we may proceed to prove a weak version of

- Theorem 1.1. By this we mean the following: We may prove that (1.2) holds for functions f that are analytic in a suﬃciently wide strip and that has suﬃcient decay at ±∞. This is our rationale for proceeding to the proof of Theorem 1.1 in Section 4.2 and the corresponding results for other L-functions and Dirichlet series in Section 5, postponing the most technical part of the proof to the later Section 6. We hope this choice of exposition will give the reader easier access to the main ideas underlying formula (1.2).


Section 6 contains precise estimates for the coeﬃcients of D(w, s), including bounds for associated partial sums. The estimates obtained in this section appear to be close to optimal. Indeed, in certain ranges of the parameters that are involved, this may be concluded up to a logarithmic factor. By the results of this section, we obtain the precise quantitative restrictions on the function f in Theorem 1.1. We also obtain, as will be shown in the ﬁnal Section 7, a new version of Theorem A with rather mild constraints on the function f being represented by the Fourier interpolation formula (1.4).

2. Generalities on Fourier interpolation

The main purpose of this section is to show that Fourier interpolation bases generically arise from certain kernels that we will refer to as Dirichlet series kernels for suggestive reasons. We do not explicitly use the results of this section anywhere else in the paper, but it does provide motivation for some of our constructions.

We start from the assumption that any “reasonable” function f can be represented as

f(λ∗)hλ∗(x),

- (2.1) f(x) =


f(λ)gλ(x) +

λ∗∈Λ∗

λ∈Λ

where Λ and Λ∗ are two sequences of real numbers with no ﬁnite accumulation point and the associated functions gλ(x) and hλ∗(x) also are “reasonable”, so that convergence of the two series is ensured. We also require that this representation behaves in the expected way under Fourier transformation, so that

f(x) =

f(λ∗) hλ∗(x).

f(λ) gλ(x) +

λ∗∈Λ∗

λ∈Λ

The basic phenomenon that we observe is that the two (general) Dirichlet series

∗z

∗z and

hλ∗(x)e−2πiλ

hλ∗(x)e−2πiλ

λ∗≤0

λ∗≥0

admit meromorphic extension to C for every x, with simple poles at x and at the points of the dual sequence Λ. Moreover, the two Dirichlet series are intertwined by a functional equation. By duality, an analogous result holds if we reverse the roles of the two sequences and replace hλ∗(x) by gλ(ξ). Conversely, as will be demonstrated in concrete terms in later sections of this paper, Dirichlet series kernels with such properties generate, by contour integration, Fourier interpolation formulas, with the range of validity depending on speciﬁc quantitative properties of these kernels.

Guided by the canonical case when the two sequences Λ and Λ∗ consist of the same points ±

√n, n = 0, 1, 2, ..., we will assume that one of the sequences satisﬁes a sparseness condition asserting that there is an entire function vanishing on Λ whose growth is at most of order 2 and ﬁnite type in any horizontal strip. In what follows, we will let Λ be the sequence enjoying this property.

![image 39](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile39.png>)

Before turning to precise results about general Dirichlet series kernels, we would like to point out that more liberal assumptions could certainly be made, such as Λ and Λ∗ be multisets (so that derivatives appear in (2.1)) or the sequence Λ be located in a strip. The assumptions of Theorem 2.1 below represent a trade-oﬀ between describing a general phenomenon and avoiding excessive technicalities and inessential diﬃculties.

- 2.1. The Dirichlet series kernel associated with Λ. In what follows, we use the


convention that a prime on a summation sign, like in ′λ∗, means that a possible term corresponding to λ∗ = 0 should be divided by 2, while all other terms are summed in the

usual way.

- Theorem 2.1. Let Λ be a sequence of distinct real numbers such that there exists an entire


function GΛ vanishing on Λ and satisfying the growth estimate GΛ(x+iy) ≪η ecx2 for some positive c in every strip |y| ≤ η. Let Λ∗ be another locally ﬁnite subset of the real line, and suppose there exist associated sequences of functions gλ : R → C, λ ∈ Λ and hλ∗ : R → C, λ∗ ∈ Λ∗ with the following properties:

- (a) There exists a positive number η0 such that for every real x, the two Dirichlet series E±(x, z) := 2πi ′∓λ∗≥0 hλ∗(x)e−2πiλ∗z converge absolutely for ±Imz ≥ η0.
- (b) For every ε > 0 and x in R, gλ(x)e−ελ2 → 0 when |λ| → ∞.
- (c) For every ε > 0 and z satisfying | Imz| ≥ η0, the function fε,z(x) := e−εx2/(z − x) can be represented as


fε,z(λ∗)hλ∗(x).

fε,z(λ)gλ(x) +

- (2.2) fε,z(x) =


λ∗∈Λ∗

λ∈Λ

Then for every x, the functions z  → E±(x, z) extend to meromorphic functions with simple poles at x and every point λ in Λ with respective residues ±1 and ±gλ(x), and the functional equation

E+(x, z) = −E−(x, z)

holds.

Note that the two assumptions (a) and (b) guarantee that the two series in (2.2) converge absolutely.

- Proof of Theorem 2.1. We ﬁx x and consider the function


Fε(z) :=

fε,z(λ)gλ(x),

λ∈Λ

which by (b) represents a meromorphic function in C. By (2.2), we may write

- (2.3) Fε(z) = fε,z(x) −

λ∗∈Λ∗

fε,z(λ∗)hλ∗(x)

when | Imz| ≥ η0. We may use assumption (a) to control the sum on the right-hand side of (2.3) on the two lines Imz = ±η0. To this end, assume ﬁrst that Imz = η0. Then since

- (2.4) fε,z(ξ) = −2π3/2i √ε

![image 40](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile40.png>)

![image 41](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile41.png>)

0

−∞

e−2πiwze−π

2ε−1(ξ−w)2dw, we have

- (2.5) fε,z(ξ) ≪

e2πη

0ξ, ξ ≤ 0, e−π2ε−1ξ2, ξ > 0,

uniformly when Imz = η0 and 0 < ε ≤ 1, say. The same argument applies to

- (2.6) fε,z(ξ) =


∞

2π3/2i √ε

2ε−1(ξ−w)2dw

e−2πiwze−π

![image 42](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile42.png>)

![image 43](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile43.png>)

0

when Imz = −η0, and hence, by (2.3) and (a), Fε(z) is uniformly bounded on | Imz| = η0 for 0 < ε ≤ 1. This along with our assumption on the sequence Λ implies that the function

2

Fε(z)GΛ(z)e−cz

is bounded on | Imz| = η0, uniformly for 0 < ε ≤ 1. It is also clear by assumption (b) and the sparseness of Λ that there exist tn → ∞ such that Fε(tn + iy) → 0 for any ﬁxed ε, uniformly when |y| ≤ η0. Similarly, there exist τn → −∞ such that Fε(τn + iy) → 0 for any ﬁxed ε, uniformly when |y| ≤ η0. Hence, by the maximum modulus principle, Fε(z)GΛ(z)e−cz2 is bounded in the strip | Imz| ≤ η0. Now a normal family argument shows that when ε → 0, Fε(z) tends locally uniformly to a meromorphic function F(z) with simple poles at the sequence Λ. On the other hand, it follows from (2.4) and (2.6) along with the uniform bound (2.5) that

1

z−x + E+(x, z), Imz = η0

![image 44](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile44.png>)

F(z) =

1

z−x − E−(x, z), Imz = −η0.

![image 45](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile45.png>)

This relation yields the asserted meromorphic continuation of the two functions E±(x, z) as well as the functional equation E+(x, z) = −E−(x, z).

- 2.2. The Dirichlet series kernel associated with Λ∗. In the preceding section, we put


a sparseness condition on Λ to control the growth of the entire function GΛ. In contrast, the dual sequence Λ∗ could be arbitrarily dense, and this means that the Phragm´en–Lindelo¨ftype argument used above would not work to establish an analogue of Theorem 2.1. This obstacle may be circumvented by relying instead on Theorem 2.1. To avoid unnecessary technicalities, we begin by stating a result that follows quite easily from Theorem 2.1 without giving the exact analogue that we are aiming for.

In what follows, we will use the function

iη0

e2πizwE−(x, z)dz

Φ(x, w) :=

−iη0

several times. Here the integral is to be interpreted in the principal value sense, should z  → E−(x, z) have a simple pole at 0. We observe that w  → Φ(x, w) is an entire function for every real x. It will also be convenient to employ the usual notation H(x) for the Heaviside step function.

- Theorem 2.2. Let the assumptions be as in Theorem 2.1 and assume in addition the following:


- (d) There exists a positive number ν0 such that the two Dirichlet series E±∗ (x, w) := 2πi ′±λ≥0 gλ(x)e2πiλw converge absolutely for ±Imw ≥ ν0.
- (e) We have E±(x, tn + iη) ≪ ec|t


n| for some c > 0, uniformly for |η| ≤ η0 and for suitable sequences {tn}n≥1 tending to ±∞.

Then

0(w−λ∗)

0(w−λ∗)

e−2πη

e2πη

′

′

E+∗ (x, w) = −2πie2πixwH(x) +

hλ∗(x)

hλ∗(x)

+

+ Φ(x, w)

![image 46](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile46.png>)

![image 47](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile47.png>)

(w − λ∗)

(w − λ∗)

λ∗≥0

λ∗≤0

E−∗ (x, w) = −2πie2πixw − E+∗ (x, w).

We see from the latter two expressions that the two functions E±∗ (x, w) have meromorphic extensions to C. We also observe that in order to obtain the desired counterpart to the functional equation E+(x, z) = −E−(x, z), we should apply Fourier transformation in the variable x. Such a step would require some additional mild assumptions that we prefer not to specify. If we take this step for granted and denote the Fourier transforms of x  → E±∗ (x, w) by E∗

±(ξ, w), then we get the desired equation E∗

+(ξ, w) = − E∗

−(ξ, w) and also that E∗

±(ξ, w) has simple poles at ξ and each point −λ∗ of −Λ∗ with respective residues ±1 and ± hλ∗(ξ).

One could imagine situations in which assumption (d) fails, for instance because the nodes λ come arbitrarily close to each other. This could be remedied by using only assumption (e) to deﬁne E±∗ (x, w) in a slightly more involved way in terms of convergence of sequences of partial sums. We ﬁnd that nothing essential is lost by refraining from entering such technicalities.

- Proof of Theorem 2.2. We set


- 1

![image 48](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile48.png>)

- 2πi


F+(w) :=

∞−iη0

e2πiwzE−(x, z)dz

−iη0

when Imw > 0. This function is well-deﬁned since E−(x, z) is uniformly bounded on the line of integration by assumption (a) of Theorem 2.1. By absolute convergence of the Dirichlet series representation of E−(x, z), we may integrate termwise and obtain that

- (2.7) F+(w) = −

- 1

![image 49](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile49.png>)

- 2πi λ


∗≥0

′

hλ∗(x)

e2πη

0(w−λ∗)

![image 50](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile50.png>)

(w − λ∗)

.

Here the series on the right-hand side converges absolutely when w is not one of the points λ∗, and hence F(w) extends to a meromorphic function in C with poles at λ∗ with λ∗ ≥ 0. Adding the constraint that Imw ≥ max(c, ν0), we now move the line of integration to z = ξ +iη0, ξ > 0. Using the functional equation E+(x, z) = −E−(x, z) and assumption (e), we then ﬁnd by the residue theorem that

- (2.8) F+(w) = −e2πixwH(x) −

λ≥0

′

gλ(x)e2πiλw −

- 1

![image 51](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile51.png>)

- 2πi


∞+iη0

iη0

e2πiwzE+(x, z)dz +

Φ(x, w) 2πi

![image 52](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile52.png>)

.

Hence using the Dirichlet series representation of E+(x, z) and integrating termwise in the ﬁrst integral on the right-hand side of (2.8), we obtain the alternate representation

F+(w) = − e2πixwH(x) −

λ≥0

′

gλ(x)e2πiλw

+

- 1

![image 53](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile53.png>)

- 2πi λ


∗≥0

′

hλ∗(x)

e−2πη

0(w−λ∗)

![image 54](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile54.png>)

(w − λ∗)

+

Φ(x, w) 2πi

![image 55](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile55.png>)

.

Combining this with (2.7), we ﬁnd that

E+∗ (x, w) := 2πi

λ≥0

′

gλ(x)e2πiλw = − 2πie2πixwH(x) +

λ∗≥0

′

hλ∗(x)

e−2πη

0(w−λ∗)

![image 56](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile56.png>)

(w − λ∗)

- (2.9)


0(w−λ∗)

e2πη

′

hλ∗(x)

+

+ Φ(x, w),

![image 57](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile57.png>)

(w − λ∗)

λ∗≤0

which yields the required expression for E+∗ (x, w). By similar calculations applied to the function

−iη0

- 1

![image 58](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile58.png>)

- 2πi


e2πiwzE−(x, z)dz

F−(w) :=

−∞−iη0

for Imw ≤ max(c, ν0), we arrive at the representation

0(w−λ∗)

e−2πη

′

E−∗ (x, w) = − 2πie2πixwH(−x) −

hλ∗(x)

![image 59](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile59.png>)

(w − λ∗)

λ∗≥0

0(w−λ∗)

e2πη

′

−

(w − λ∗) − Φ(x, w).

hλ∗(x)

![image 60](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile60.png>)

λ∗≤0

Combining this formula with (2.9), we obtain the required relation between E+∗ (x, w) and E−∗ (x, w).

- 2.3. Examples. We illustrate the above discussion with two examples where the corresponding Fourier interpolation identity is known: the Whittaker–Shannon interpolation formula and the Fourier interpolation formula from [25]. Theorem 1.1, one of the main results of this paper, yields a third example that will be treated in Section 4; a large family of related formulas will then be presented in the subsequent Section 5.3.


- 2.3.1. The Paley–Wiener case. Suppose that f is such that the periodized function


F(y) :=

f(y + n)

n∈Z

is well-deﬁned and in L2(−1/2, 1/2). Then we may express f as f(x) =

∞

f(y) − F(y)1[−1/2,1/2](y) e2πixydy

f(n) sinc(π(x − n)) +

−∞

n∈Z

1[n−1/2,n+1/2](y)e−2πixn dy.

f(y)e2πixy 1 −

f(n) sinc(π(x − n)) +

=

|y|≥1/2

n∈Z

n =0

We may think of this formula as representing the degenerate case when Λ = Z and Λ∗ = (−∞, −1/2] ∪ [1/2, ∞). The associated kernels are

1[n−1/2,n+1/2](y)e−2πixn dy,

e−2πiy(z−x) 1 −

E±(x, z) := 2πi

∓y≥1/2

n =0

∞

e±2πin(w−ξ) .

E∗

±(ξ, w) := 1[−1/2,1/2](ξ) πi + 2πi

n=1

We may in this case compute their meromorphic continuations explictly:

eπi(z−x) z − x −

πe−πiz sin πz

E±(x, z) = ∓

sincπ(z − x) , E∗

![image 61](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile61.png>)

![image 62](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile62.png>)

±(ξ, w) = ±π1[−1/2,1/2](ξ) cotπ(w − ξ).

The latter kernel has a pole of residue ±1 at ξ; all other poles are located in Λ∗, and the collection of all such poles when ξ varies in [−1/2, 1/2] is indeed the entire set Λ∗.

- 2.3.2. The √n case. We can reinterpret the results of [25] in terms of Dirichlet series


![image 63](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile63.png>)

√n}n∈Z, all of the identities can be symmetrized over x  → −x. In particular, this implies that we may assume E−(x, z) = E+(−x, −z). It is convenient to split the kernels into even and odd parts. First, we look at the even kernels

kernels as follows. As Λ = Λ∗ = {±

![image 64](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile64.png>)

- 1

![image 65](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile65.png>)

- 2(E+(x, z) + E+(−x, z)). Since for all even Schwartz functions f we have


an(x)f(√n) +

an(x) f(√n), we get

![image 66](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile66.png>)

![image 67](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile67.png>)

f(x) =

n≥0

n≥0

1 2

√nz,

![image 68](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile68.png>)

an(x)e2πi

(E+(x, z) + E+(−x, z)) = 2πi

![image 69](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile69.png>)

n≥0

- 1

![image 70](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile70.png>)

- 2


√nz.

(E+∗ (x, z) + E+∗ (−x, z)) = 2πi

![image 71](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile71.png>)

an(x)e2πi

n≥0

- Theorem 2.1 and Theorem 2.2 in this case tell us that the functions z  → E+(x, z) and


√nz, n ≥ 0 in the upper halfplane extend to meromorphic functions in C with simple poles at ±

z  → E+∗ (x, z), given by a general Dirichlet series over e2πi

![image 72](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile72.png>)

√n, as well as a simple pole at ±x. Moreover, the analytic extension to the lower half-plane in each case is given by a general Dirichlet series over e−2πi

![image 73](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile73.png>)

√nz, n ≥ 0.

![image 74](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile74.png>)

One can treat the odd kernels 21(E+(x, z)−E+(−x, z)) similarly. In this case we use the interpolation formula for odd functions [25, Thm. 7]

![image 75](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile75.png>)

f(√n) √n −

f(√n) √n

f′(0) + ifˆ′(0) 2

![image 76](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile76.png>)

![image 77](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile77.png>)

+

cn(x)

f(x) = c0(x)

.

cn(x)

![image 78](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile78.png>)

![image 79](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile79.png>)

![image 80](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile80.png>)

![image 81](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile81.png>)

![image 82](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile82.png>)

n≥1

n≥1

From this we obtain (E+(x, z) − E+(−x, z)) = (2πi) − c0(x)(πiz) −

cn(x) √n

- 1

![image 83](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile83.png>)

- 2


√nz

![image 84](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile84.png>)

e2πi

![image 85](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile85.png>)

![image 86](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile86.png>)

n≥1

and an analogous expression for the dual odd kernel 12(E+∗ (x, z) − E+∗ (−x, z)). A new feature in the odd case is a pole of order two at z = 0, which corresponds to the fact that

![image 87](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile87.png>)

the interpolation formula involves f′(0) and fˆ′(0).

- 2.4. The joint density of Λ and Λ∗. We now come to a basic necessary condition for existence of formulas like (2.1), that was recently established by Kulikov [20]. This


condition yields a joint bound for the two counting functions NΛ(T) and NΛ∗(W), which we deﬁne as the number of points from the respective sequences to be found in the two intervals [−T, T] and [−W, W]. Kulikov made the assumptions that NΛ(T) ≪ TL for some positive integer L and that the functions gλ(x) be polynomially bounded in the two variables λ and x. Assuming also the validity of (2.1) for all functions f with C∞-smooth and compactly supported Fourier transform, he showed that for every η > 0, there exists a positive constant C such that

- (2.10) NΛ(T) + NΛ∗(W) ≥ 4WT − C log2+η(4WT)


holds whenever W, T ≥ 1. This result relies on sharp estimates of Karnik, Romberg, and Davenport [13] for the eigenvalue distribution of time-frequency localization operators. We may view (2.10) as a manifestation of the uncertainty principle as discussed for instance in the work of Slepian [27]. To simplify matters, we have again suppressed the possibility that Λ and Λ∗ be multi-sets which however is accounted for in [18].

We observe that in the √n case, NΛ(T) = 2T2 + O(1) and NΛ∗(W) = 2W2 + O(1), so that (2.10) holds since T2 + W2 ≥ 2WT. To relate Kulikov’s bound to Theorem 1.1, we let Λ consist of the points (ρ − 1/2)/i and Λ∗ be the sequence of points ±(log n)/(4π) for n ≥ 1. Then NΛ(T) = 2N(T) and NΛ∗(W) = e4πW + O(1), where we in the ﬁrst relation use the standard notation N(T) for the usual counting function for the nontrivial zeros of ζ(s). Then (2.10) yields

![image 88](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile88.png>)

2N(T) + e4πW ≥ 4WT − C log2+η(4WT). If we now set W = (log T − log(2π))/(4π), then we get

T 2π

T 2πe − C log2+η T,

N(T) ≥

log

![image 89](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile89.png>)

![image 90](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile90.png>)

which clearly holds in view of the Riemann-von Mangoldt formula T 2π

T 2πe

- (2.11) N(T) =


log

+ O(log T).

![image 91](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile91.png>)

![image 92](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile92.png>)

There is a similar precise relation between Kulikov’s bound (2.10) and the Riemann-von Mangoldt formula for any L-function to which the methods developed in this paper apply. We will return to this point in Subsection 5.3.

We should like to emphasize that Kulikov does not assume minimality of the system of functions gλ(x) and hλ∗(x). It seems reasonable to expect that an assumption about minimality should imply a sparseness condition that would complement (2.10). It would be interesting to see if a general version of the Riemann–von Mangoldt formula (2.11) (though with a less precise remainder term) could be obtained as a consequence of (2.10) along with such a sparsity condition.

- 2.5. Fourier interpolation and crystalline measures. It is immediate that a formula like (2.1) should imply that the distributional Fourier transform of


µx := δx −

gλ(x)δλ

λ∈Λ

will be

hλ∗(x)δλ∗,

µx =

λ∗∈Λ∗

where as usual δξ is the unit mass at the point ξ. This means that any Fourier interpolation formula as a byproduct generates a whole family of measures that are crystalline in an appropriate sense. We refer to [21, 22, 23] for some interesting recent results on crystalline measures and Fourier quasicrystals. It is our impression that the results of the present paper, while perhaps shedding some light on Dyson’s thoughts on the Riemann hypothesis

in his acclaimed lecture [6], adds further evidence to the common belief (see [21]) that a classiﬁcation of such measures would probably be very diﬃcult to obtain.

3. Modular integrals for the theta group

In this section we construct a family of special functions (modular integrals) on the complex upper half-plane H := {τ ∈ C: Imτ > 0} whose Mellin transforms form the building blocks for our Dirichlet series kernels.

The deﬁnition of these functions is most naturally viewed in terms of Eichler cohomology for the theta group. Nevertheless, they have a simple elementary description: we are interested in 2-periodic analytic functions F : H → C that are of moderate growth (see below) and satisfy

- (3.1) F(τ) − ε(τ/i)−kF(−1/τ) = (τ/i)−s − ε(τ/i)s−k.

Here ε ∈ {±1}, k ≥ 0, and s ∈ C. In what follows, we will always interpret the expression (z/i)α for z ∈ H as the principal branch, i.e., (z/i)α takes the value xα for z = ix, x > 0 (equivalently, (z/i)α = eαLog(z/i)).

The condition (3.1) is not suﬃcient to uniquely pinpoint the function F. Nevertheless, it determines F uniquely modulo a ﬁnite-dimensional space of modular forms if we additionally require F to be of moderate growth. Following Knopp [15], we say that a function ϕ: H → C is of moderate growth if

ϕ(τ) ≪ Im(τ)−α + |τ|β, τ ∈ H, where α and β are some positive constants. Equivalently, ϕ is of moderate growth if and only if for some r > 0 we have |ϕ(i1+1−zz)| ≪ (1 − |z|)−r for all z in the unit disk |z| < 1.

![image 93](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile93.png>)

For a 2-periodic function F moderate growth is tantamount to having a Fourier expansion F(τ) =

n≥0

aneπinτ, τ ∈ H,

where the sequence {an}n≥0 has polynomial growth. To make the solution unique, we require in addition that the ﬁrst few coeﬃcients an vanish. More precisely, we require an = 0 for n < νε, where we set

- (3.2) ν− = ν−(k) :=

k + 2 4

![image 94](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile94.png>)

, ν+ = ν+(k) :=

k + 4 4

![image 95](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile95.png>)

.

Theorem 3.1. If ϕ: H → C is an analytic function of moderate growth, then for any k ≥ 0 and ε ∈ {±1} there exists a unique 2-periodic analytic function F : H → C of moderate growth with a Fourier expansion of the form

F(τ) =

n≥νε

aneπinτ, τ ∈ H

such that

- (3.3) F(τ) − ε(τ/i)−kF(−1/τ) = ϕ(τ) − ε(τ/i)−kϕ(−1/τ).


The proof of uniqueness will come as a simple corollary of some basic properties of modular forms for the theta group (see Proposition 3.1), while the proof of existence follows from Proposition 3.3.

Let us denote the function F from Theorem 3.1 by Fkε(τ, ϕ). Since ϕs(τ) = (τ/i)−s is

of moderate growth in H for any s ∈ C, there is a unique function Fk±(τ, s) := Fk±(τ, ϕs) with a Fourier expansion

αn,k± (s)eπinτ such that

Fk±(τ, s) =

n≥ν±

Fkε(τ, s) − ε(τ/i)−kFkε(−1/τ, s) = (τ/i)−s − ε(τ/i)s−k. This is exactly the function that we are interested in.

Remark. For k > 2 the existence part of Theorem 3.1 follows from the results of Knopp on Eichler cohomology [15]. Instead of this we use a construction with contour integrals as in [25] (in Section 3.3 below we will sketchily explain the motivation behind this construction). The main reason for doing this is, ﬁrst, because the construction works for all k ≥ 0, and second, since it can be used to give relatively good estimates for the size of the coeﬃcients αn,k± (s) as n → ∞, at least in the range 0 ≤ k ≤ 2.

Let us also note that for k = 0 the existence of the decomposition (3.3) is related to the result of Hedenmalm and Montes-Rodriguez [11] that the system of functions eiπnx, eiπn/x, n ∈ Z is weak-star complete in L∞(R).

- 3.1. Preliminaries on the theta group. The group SL2(R) of 2 × 2 real matrices with determinant 1 acts in the usual way on the upper half-plane H by


aτ + b cτ + d

a b c d ∈ SL2(R).

γτ =

, γ =

![image 96](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile96.png>)

Since the matrix −I = ( −01 −01) acts trivially, we will work with the group PSL2(R) := SL2(R)/{±I} instead, but we still prefer to write the elements of PSL2(R) as matrices. Let us denote

- 0 −1
- 1 0


1 1 0 1

S :=

, T :=

.

The theta group Γθ ⊂ PSL2(Z) is the subgroup generated by S and T2. The group Γθ consists of all the elements of PSL2(Z) congruent to (01 01) or (10 10) modulo 2 (see [17, p.7 Cor. 4]). The only relation between the generators of Γθ is S2 = 1. This implies that any element γ ∈ Γθ can be written in a unique way as γ = Sε

T2m

ST2m

. . .ST2m

Sε

, where εj ∈ {0, 1}, which we call the canonical word or the canonical representation for γ.

k

0

1

2

1

A fundamental domain for Γθ is given by (see Figure 3.1) F := {z ∈ H: − 1 < Rez < 1, |z| > 1}.

Since F is a fundamental domain for the group Γθ, for any τ ∈ H there exists an element γ = γτ ∈ Γθ such that γτ is in F. Moreover, if τ does not belong to the set γ∈Γ

![image 97](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile97.png>)

∂F (which is nowhere dense and of measure 0), then the element γ is unique, and otherwise there are at most two such elements: {γ, Sγ} or {γ, T2γ}. The element γτ can be found

θ

T−2F F

T2F

T−2SF

T2SF

SF

−3 −2 −1 0 1 2 3

Figure 3.1. Fundamental domain for Γθ and some of its translates

by repeatedly performing the following operation: ﬁrst apply some power of T2 to get τ into the strip {| Reτ| ≤ 1}, and then, if the resulting point is not yet in the fundamental domain, apply the inversion S.

- 3.2. Modular forms for the theta group. In this subsection we will collect the necessary basic facts about modular forms for the theta group. A more detailed exposition can be found in [2, Ch. 6].


Let θ(τ) be the Jacobi theta function θ(τ) :=

2τ.

eπin

n∈Z

The function θ: H → C is holomorphic, and it satisﬁes the transformations (τ/i)−1/2θ(−1/τ) = θ(τ), θ(τ + 2) = θ(τ),

which correspond to the two generators of the theta group Γθ. More generally, for any γ = ( ac db ) ∈ Γθ with c > 0 or c = 0, d > 0, we have

aτ + b cτ + d

θ(τ) = ζγ(cτ + d)−1/2θ

,

![image 98](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile98.png>)

where (cτ + d)−1/2 is the principal branch and ζγ is a certain 8th root of unity that can be written explicitly in terms of Jacobi symbols (see [24, Th. 7.1]). Finally, as a corollary of the

5(τ)

Jacobi triple product identity, one has θ(τ) = η

η2(2τ)η2(τ/2), where η(τ) := q1/24 n≥1(1−qn) is the Dedekind eta function, and thus we see that θ(τ) does not vanish anywhere in H. Here and in what follows we deﬁne the nome q by q := e2πiτ and for arbitrary rational number r we will interpret qr as e2πirτ.

![image 99](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile99.png>)

- 3.2.1. The theta automorphy factor. We deﬁne the theta automorphy factor jθ(τ, γ) by


θ(τ) θ(γτ)

jθ(τ, γ) :=

, γ ∈ Γθ.

![image 100](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile100.png>)

It satisﬁes jθ(τ, γ1γ2) = jθ(τ, γ2)jθ(γ2τ, γ1) and jθ(τ, γ)8 = (cτ + d)−4. We deﬁne the slash operator in weight k with theta automorphy factor by

(f|kγ)(τ) = jθ2k(τ, γ)f(γτ).

It is easy to see that this formula deﬁnes a right action of Γθ on the space of functions f : H → C. More generally, let χε: Γθ → {±1}, where ε = ±1 be the homomorphism deﬁned by χε(T2) = 1 and χε(S) = ε. We then deﬁne

(f|εkγ)(τ) := χε(γ)jθ2k(τ, γ)f(γτ). Note that all of the above deﬁnitions remain valid for real k ≥ 0 (and in fact for all complex k), if we interpret jθ2k(τ, γ) as θ

2k(τ)

θ2k(γτ) and θ2k(τ) using the principal branch, i.e., θa(τ) := exp a

![image 101](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile101.png>)

τ

θ′(z) θ(z)

dz , a ∈ C.

![image 102](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile102.png>)

i∞

- 3.2.2. Modular forms for Γθ. We deﬁne Mk(Γθ, ε) to be the space of holomorphic modular forms of weight k with respect to the above slash action, i.e., f : H → C is in Mk(Γθ, ε) if and only if f is a holomorphic function of moderate growth and f|εkγ = f for all γ ∈ Γθ. We also denote by Mk!(Γθ, ε) the space of weakly holomorphic modular forms of weight k:


a holomorphic function f : H → C belongs to Mk!(Γθ, ε) if f|εkγ = f for all γ ∈ Γθ and its Fourier expansion at each of the cusps has at most ﬁnitely many negative powers of q (i.e., f has at worst poles at the cusps).

If we let J(τ) = J+(τ) := λ(τ)(116−λ(τ)) = (ηθ((ττ)))12 and J−(τ) := 1 − 2λ(τ), where λ(τ) is the modular lambda invariant, then J± is in M0!(Γθ, ±). Moreover, J+(τ) is a Hauptmodul for the group Γθ and it maps the fundamental domain F conformally onto the cut plane C (−∞, 64], as shown in Figure 3.2. In particular, since J(τ) is a Hauptmodul, any

![image 103](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile103.png>)

![image 104](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile104.png>)

f ∈ Mk!(Γθ, ±) can be written as f(τ) = θ2k(τ)J±(τ)P(J(τ)), where P is some Laurent polynomial. (A priori P can be a rational function, but since f has poles only at the cusps and J(τ) takes values 0 and ∞ at the two cusps, the poles of P must be contained in {0, ∞}.) Note that the identity

Mk!(Γθ, ±) = θ2kJ±C[J, J−1] makes sense for all complex values of k if we interpret θ2k(τ) as the principal branch.

H

C

F

0 64

J

i

ℓ

−1 1

Figure 3.2. J(z) as a conformal map.

Since J(τ) has a pole at the cusp at ∞, if f ∈ Mk(Γθ, ε), then f(τ) = θ2k(τ)Jε(τ)p(1/J(τ)), where p(x) ∈ C[x] is now a polynomial (without constant term

if ε = +). From

- 1

![image 105](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile105.png>)

- 2(τi )−1/2θ(1 − τ1) = q1/8 + q9/8 + q25/8 + . . ., −2−12J(1 − τ1) = q + 24q2 + 300q3 + . . . ,


![image 106](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile106.png>)

![image 107](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile107.png>)

- (3.4)

we see that f is in Mk(Γθ, +) if and only if deg(p) ≤ ν+(k) and f is in Mk(Γθ, −) if and only if deg(p) ≤ ν−(k) − 1. Thus we get the following (see [2, Thm. 6.3]).

- Proposition 3.1. We have dim Mk(Γθ, ε) = νε(k), where ν± are deﬁned in (3.2). More-


over, any f ∈ Mk(Γθ, ε) with a Fourier expansion of the form f(τ) = n≥ν

±

cneπinτ must vanish identically.

Note that this immediately implies uniqueness in Theorem 3.1, since any two 2-periodic solutions of the functional equation (3.3) diﬀer by an element of Mk(Γθ, ε), which must vanish by Proposition 3.1.

Finally, let us record some simple asymptotic relations between various functions in the fundamental domain F. For z → i∞, we have Im(1 − 1/z) = Im(z)|z|−2 ≍ Im(z)−1 and J(1 − 1/z) ∼ −4096e2πiz, so that log |J(z)| ≍ −Im(z)−1, as z tends to ±1 in the fundamental domain. From this we deduce that, when expressed in terms of w = J(z), as w → 0 (which again corresponds to z → ±1 inside the fundamental domain), we have Im(z) ≍ log|1w−1|, and therefore

![image 108](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile108.png>)

|θ(z)|2 ≍ |w|1/4 log |w−1|. Moreover, since J−(z)2 = 1 − 64/J(z), we get that J−(z) = ± 1 − 64/w. We also record here the following identity

![image 109](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile109.png>)

- (3.5) J′(z) = −πiθ4(z)J(z)J−(z). In particular, this implies that if we set w = J(z), then
- (3.6) θ4(z)dz = π−1w−1/2(64 − w)−1/2dw.

- 3.3. Modular kernels. We deﬁne the following two-variable meromorphic functions on the upper half-plane:


Kk+(τ, z) := θ2k(τ)θ4−2k(z)

Jν

+

(z) Jν+(τ)

![image 110](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile110.png>)

J(τ)J−(z) J(τ) − J(z)

![image 111](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile111.png>)

=

∞

n=ν+

gn,k+ (z)qn/2,

Kk−(τ, z) := θ2k(τ)θ4−2k(z)

Jν−(z) Jν−(τ)

![image 112](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile112.png>)

J(τ)J−(τ) J(τ) − J(z)

![image 113](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile113.png>)

=

∞

n=ν−

gn,k− (z)qn/2.

- (3.7)


![image 114](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile114.png>)

8 J−(1 − τ1) = q−1/2 + 20q1/2 − 62q3/2 + . . .

![image 115](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile115.png>)

Here we view the series on the right as formal power series in the variable q1/2. Note that by construction Kk±(τ, z) is a meromorphic modular form of weight k in τ (respectively of weight 2 − k in z) for each ﬁxed z (respectively τ). For ﬁxed τ it has simple poles for z ∈ Γθτ and no other singularities in H. Moreover, (3.5) implies that the residue of Kk±(τ, z) at z = τ is (πi)−1. From the above estimates for θ(z) and J(z) near the cusp at

z = ±1, we get that for any ﬁxed τ the function Kk±(τ, z) is rapidly decreasing as z → ±1 non-tangentially.

Let us also record some important properties of the coeﬃcients gn,k± (z).

- Proposition 3.2. The functions gn,k± : H → C, n ≥ ν± belong to M2!−k(Γθ, ∓), vanish at the cusp at ±1, and satisfy

(3.8) gn,k± (τ) = q−n/2 + O(q−(ν±−1)/2), τ → i∞.

Proof. The ﬁrst two claims follow trivially from the deﬁnition, while the last statement is proved in exactly the same way as Theorem 3 in [25] (see also earlier papers by Asai, Kaneko, and Ninomiya [1, Sec. 3] and by Zagier [31] where analogues of gn,k± for the full modular group appear).

- ℓ1 ℓ0
- ℓ2


τ −1/τ

−1 1 Figure 3.3. Deforming the contour of integration

- Proposition 3.3. If ϕ: H → C is a holomorphic function of moderate growth, then


1

- 1

![image 116](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile116.png>)

- 2


- (3.9) Fk±(τ, ϕ) :=


Kk±(τ, z)ϕ(z)dz, τ ∈ F,

−1

where the integral is taken over a semicircle in the upper half-plane, admits an analytic continuation to H that satisﬁes the conditions of Theorem 3.1.

Proof. We only sketch the proof, since it essentially repeats the proof of Proposition 2 in [25]. The main idea is to show that the contour integral in (3.9) extends analytically from F to the neighboring fundamental domain SF, that the extension satisﬁes (3.3) in F ∪ SF, and from there to extend it iteratively to all of H using the functional equation.

Note that the integral is well-deﬁned since Kk±(τ, z) has exponential decay in Im(z)−1 as z → ±1 non-tangentially and ϕ is bounded there by some power of Im(z)−1. Let us denote the right-hand side of (3.9) by G0(τ), τ ∈ F. Since the only singularities of the kernel z  → Kk±(τ, z) are at z ∈ Γθτ, G0(τ) extends analytically across the vertical lines τ ∈ H, Reτ = ±1 and the resulting analytic extension is 2-periodic. Let us show that it also extends across the semicircle and the extension satisﬁes the functional equation (3.3).

Let ℓ0 denote the semicircle, and consider two other paths ℓ1 and ℓ2 as in Figure 3.3 such that ℓ2 is the image of ℓ1 under the inversion z  → −1/z, with all three paths oriented

Kk±(τ, z)ϕ(z)dz. Note that G1 deﬁnes an analytic function in the region U (the shaded region in Figure 3.3) between ℓ1 and ℓ2. Let τ be a point in the region between ℓ0 and ℓ1. Then the residue theorem tells us that

from −1 to 1. Let us deﬁne G1(τ) := 21 ℓ

![image 117](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile117.png>)

1

G0(τ) − G1(τ) = ϕ(τ),

so that G1(τ)+ϕ(τ) provides an analytic extension of G0 to U. Moreover, we automatically get (3.3) since G1(τ) = ±(τ/i)−kG1(−1/τ) for τ ∈ U because of the corresponding property of Kk±(τ, z).

To obtain an analytic extension to all of H we simply deﬁne F(τ) for τ ∈ γ−1F as G0|±k γ + ϕγ, where {ϕγ}γ∈Γθ

![image 118](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile118.png>)

is the Γθ-cocycle generated by ϕT2 = 0 and ϕS = ϕ − ϕ|±k S (see Section 6.2). Since the neighboring regions of γ−1F are γ−1SF and γ−1T±2F, the above continuation properties of F0 imply that F is well-deﬁned and analytic on H.

![image 119](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile119.png>)

![image 120](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile120.png>)

![image 121](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile121.png>)

Finally, since ϕ is of moderate growth and F(τ) is an automorphic integral for the cocycle

generated by ϕ, by the main result of [16] we get that Fk±(τ, ϕ) := F(τ) is also of moderate growth.

We will prove more precise statements about the growth of Fk±(τ, ϕ) in Section 6.

Remark. Let us give a brief explanation of why one would expect a formula like (3.9). Assume that k = 0 and the sign is “+”. Then the function that we are looking for, when written in terms of w = J(τ), is a holomorphic function on C [0, 64] with prescribed jumps along the segment [0, 64]. By the classical Sokhotski-Plemelj formula, such a function is

![image 122](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile122.png>)

given by an integral 0 64 wA−(ss)ds, where A(s) is the jump at the point s. When expressed in terms of the upper half-plane variables τ and z, the Cauchy kernel simply becomes K0+(τ, z) and we obtain (3.9). To get the formula in the general case we simply divide both sides of the functional equation (3.3) by θ2k(τ)Jε(τ)Jn(τ) for an appropriate value n ∈ Z to reduce to the case k = 0, ε = +. Let us also mention that, in the case of PSL2(Z), such integrals have previously appeared in a work of Duke, Imamo¯lu, and T´th [5].

![image 123](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile123.png>)

Remark. The functions Kk±(τ, z) are sometimes called Green’s functions, see, e.g., Eichler’s paper [7, p. 121]. For k > 2 one can instead use the Poincar´e series

eπiγτ + eπiz eπiγτ − eπiz

- 1

![image 124](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile124.png>)

- 2


Pk±(τ, z) :=

χ±(γ)jθ−2k(γ, τ)

,

![image 125](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile125.png>)

γ∈Γθ,∞\Γθ

(where Γθ,∞ denotes the subgroup of Γθ generated by T2) which diﬀers from Kk±(τ, z) by an element of Mk!(Γθ, ±) ⊗ M2!−k(Γθ, ∓).

- 3.4. Deﬁnition and basic properties of Fk±(τ, s). Using the result of Proposition 3.3 we can now precisely deﬁne the special functions Fk±.


For k ≥ 0 we deﬁne Fk±: H × C → C by

1

- 1

![image 126](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile126.png>)

- 2


Kk±(τ, z)(z/i)−sdz, τ ∈ F

- (3.10) Fk±(τ, s) :=


−1

and by analytic continuation in τ if τ is in H   F. The function Fk±(·, s) is 2-periodic and has a Fourier expansion

- (3.11) Fk±(τ, s) =

∞

n=ν±

αn,k± (s)eπinτ,

where αn,k± (s) are given by

- (3.12) αn,k± (s) :=

- 1

![image 127](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile127.png>)

- 2


1

−1

gn,k± (z)(z/i)−sdz,

and gn,k± are weakly holomorphic modular forms of weight 2 − k deﬁned by (3.7). The coeﬃcients αn,k± (s) are of polynomial growth in n for any ﬁxed s ∈ C and

- (3.13) Fk±(τ, s) ∓ (τ/i)−kFk±(−1/τ, s) = (τ/i)−s ∓ (τ/i)s−k, τ ∈ H. Finally, for any ﬁxed τ ∈ H the function Fk±(τ, s) is an entire function of s and it satisﬁes
- (3.14) Fk±(τ, k − s) = ∓Fk±(τ, s).

The last claim follows from the uniqueness part of Theorem 3.1 since Fk±(τ, k − s) is 2-periodic in τ and satisﬁes the same functional equation as Fk±(τ, s), up to sign.

Finally, we remark that αn,k± (s) is an entire function of exponential type. More precisely, by making a change of variable z = ie2πit in (3.12) we obtain

- (3.15) αn,k± (s) = −π


1/4

gn,k± (ie2πit)e−2πit(s−1)dt,

−1/4

so that αn,k± (s) is the Fourier transform of a C∞-smooth function with support in [−1/4, 1/4]. An analogous calculation also shows that for τ ∈ F the function s  → Fk±(τ, s) is also the Fourier transform of a smooth function with support in [−1/4, 1/4]. Similarly, we get the following result.

- Proposition 3.4. Let k ≥ 0. Then there exists c > 0 such that for all x > 1 we have


√

![image 128](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile128.png>)

π

|Ims|. Proof. Making the change of variable z = eit in the deﬁnition we get

2|Ims|e−πx−c

|Fk±(ix, s) − α0±,k(s)| ≪k e

![image 129](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile129.png>)

0

- 1

![image 130](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile130.png>)

- 2


Fk±(ix, s) − α0±,k(s) =

(Kk±(ix, ieit) − g0±,k(ieit))(e−ist ∓ ei(s−k)t)dt.

−π/2

If x ≥ 2, then using the leading terms of the asymptotic expansions (3.4) and the fact that J(ix) > 100 for x ≥ 2, we get

|Kk±(ix, ieit) − g0±,k(ieit)| ≪k exp(−πx − κ

cost), t ∈ (−π/2, π/2),

±

![image 131](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile131.png>)

where κ+ := 2π(1 − {k/4}) and κ− := 2π(1 − {(k − 2)/4}). Thus we have

π/2

κ±

|Fk±(ix, s) − α0±,k(s)| ≪k e−πx

e|Ims|t−

costdt

![image 132](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile132.png>)

0

√

π/2

κ±

![image 133](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile133.png>)

π

π

κ±|Ims|,

2|Ims|e−πx

e−|Ims|t−

2|Ims|e−πxe−2

sintdt ≤ π2e

= e

![image 134](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile134.png>)

![image 135](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile135.png>)

![image 136](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile136.png>)

![image 137](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile137.png>)

0

√

![image 138](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile138.png>)

where we have used the inequalities sin1 t ≥ 1t and at + bt−1 ≥ 2

ab. Since κ± > 0, this proves the claim.

![image 139](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile139.png>)

![image 140](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile140.png>)

If 1 < x < 2, then we split the integral as − −π/π/24 + − 0π/4. Then we use the same estimate for the ﬁrst integral, while the second integral is of size ≪k e

π

4|Ims|, which can be seen by deforming the contour of integration (similarly to what was done in the proof of

![image 141](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile141.png>)

- Proposition 3.3) so as to avoid large values of the denominator J(τ)−J(z) in Kk±(τ, z).


- 3.4.1. Relation to the interpolation bases for the √n case. Next, let us relate αn,k± (s) to the functions b±n and d±n constructed in [25]. If we deﬁne


![image 142](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile142.png>)

1

- 1

![image 143](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile143.png>)

- 2


2

gn,±1/2(z)eπizx

b±n (x) :=

dz,

−1

- (3.16)

(the sign notation diﬀers from that of [25] so that b±n and d±n in our context coincide with respectively b∓n and d∓n from [25]) then a routine calculation shows that

ΓR(s)αn,±1/2(s/2) = 2

∞

0

b±n(x)xs−1dx,

ΓR(s)αn,±3/2(s/2) = 2

∞

0

d±n(x)xs−2dx,

- (3.17)

where we again use the notation ΓR(s) := π−s/2Γ(s/2). We remark here that in [25, Prop. 1, Prop. 3] it is proved that b±n(x) is an even Fourier eigenfunction with eigenvalue ∓1, d±n(x) is an odd Fourier eigenfunction with eigenvalue ±i, and moreover that

- (3.18) b±n (√m) = d±n(√m) = δn,m, m ≥ 1. All these properties can be easily checked directly from the deﬁnition, using (3.8).

![image 144](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile144.png>)

![image 145](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile145.png>)

3.4.2. Special values. We conclude this section by giving explicit evaluations of Fk±(τ, s) for some special values of s. We do this using the fact that (3.11) and (3.13) uniquely

determine Fk±(τ, s) as a function of τ, so that if we can ﬁnd a 2-periodic function f(τ) that satisﬁes (3.13), then necessarily Fk±(τ, s) − f(τ) belongs to Mk(Γθ, ±).

A trivial example is s = 0, where we can take f(τ) = 1. Thus Fk±(τ, 0) = 1−g(τ), where g(τ) = 0 if ν± = 0 and otherwise g(τ) is the unique modular form in Mk(Γθ, ±) with the q-expansion g(τ) = 1 + O(qν±/2). In particular,

- (3.19) Fk−(τ, 0) = 1, Fk+(τ, 0) = 1 − θ2k(τ), 0 ≤ k < 2.


1

- 1

![image 146](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile146.png>)

- 2


2

d±n(x) :=

gn,±3/2(z)xeπizx

dz,

−1

Similarly, from (3.13) we see that Fk+(τ, k/2) is in Mk(Γθ, +) and looking at the qexpansion, we see that in fact

Fk+(τ, k/2) = 0, 0 ≤ k < 2. A more interesting example is the identity

π 3

F2−(τ, 1) =

(−E2(τ/2) + 5E2(τ) − 4E2(2τ)),

![image 147](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile147.png>)

where E2 is the weight 2 Eisenstein series, E2(τ) = 1−24 n≥1 σ(n)qn (here σ(n) = d|n d is the divisor sum function). To see this we use that by the well-known functional equation

6 π

E2(τ) − τ−2E2(−1/τ) =

(τ/i)−1

![image 148](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile148.png>)

we have F2−(τ, 1) − π3E2(τ) ∈ M2(Γθ, −) and note that the space M2(Γθ, −) is onedimensional, spanned by E2(τ/2) − 4E2(τ) + 4E2(2τ). As a corollary, we have

![image 149](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile149.png>)

αn,−2(1) = 8π(σ(n) − 5σ(n/2) + 4σ(n/4)), n ≥ 1, where we deﬁne σ(x) = 0 if x  ∈ N.

4. The Dirichlet series kernel associated with zeros of ζ(s)

In this section we assume that the weight k is a positive real number and consider the function Fk±(τ, s) given by the Fourier expansion

αn,k± (s)eπinτ,

Fk±(τ, s) :=

n≥ν±

where, as before, ν− = ⌊(k + 2)/4⌋ and ν+ = ⌊(k + 4)/4⌋. For convenience we extend the deﬁnition of αn,k± (s) to all n ≥ 0 by setting αn,k± (s) :=0, 0 ≤ n < ν±.

- 4.1. The Mellin transform of Fk±(τ, s). Let us deﬁne A±k (w, s) by


αn,k± (s) nw

∞

- (4.1) A±k (w, s) :=


(Fk±(it, s) − α0±,k(s))tw−1dt = π−wΓ(w)

.

![image 150](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile150.png>)

0

n≥1

Since for ﬁxed s the sequence {αn,k± (s)} grows polynomially, the above Dirichlet series converges absolutely for suﬃciently large Rew. Similarly, for ﬁxed s we have (by (3.13))

Fk±(it, s) = α0±,k(s) + O(e−πt), t → ∞, Fk±(it, s) = ±α0±,k(s)t−k + t−s ∓ ts−k + O(t−ke−π/t), t → 0+,

and hence the integral in (4.1) converges absolutely for Rew > max(k, Res, Re(k − s)).

- Proposition 4.1. The function w  → A±k (w, s) extends to a meromorphic function in C with simple poles at w = s, k−s with respective residues 1, ∓1, and at most simple poles at


w = 0, k with respective residues −α0±,k(s), ±α0±,k(s). Moreover, the function A±k satisﬁes the two functional equations

A±k (k − w, s) = ±A±k (w, s), A±k (w, k − s) = ∓A±k (w, s).

- (4.2)

Finally, the function w  → A±k (w, s) is bounded in lacunary vertical strips {u + iv | a ≤ u ≤ b, |v| ≥ T} for suﬃciently large T > 0.

Proof. The claims follow from the general result of Bochner [3, Th. 4] combined with (3.13).

More speciﬁcally, using the standard trick (see, e.g., [32]) by splitting the integral deﬁning A±k (w, s) as 0 1 + 1 ∞ and applying (3.14) to the part 0 1 we obtain

A±k (w, s) = −α0±,k(s)(w−1 ± (k − w)−1) + (w − s)−1 ± (k − w − s)−1

+

∞

1

(Fk±(it, s) − α0±,k(s))(tw−1 ± tk−w−1)dt.

- (4.3)


Since the integral deﬁnes an analytic function of (w, s), this immediately implies meromorphic continuation with given simple poles, and since the integral is clearly bounded in vertical strips, we also obtain boundedness in lacunary strips for w  → A±k (w, s). Finally, the functional equations (4.2) follow trivially from (4.3) and (3.14).

Note that α0+,k(s) = 0 for k ≥ 0 and α0−,k(s) = 0 for k ≥ 2 hence in these cases (which

correspond to ν± > 0) the only singularities of w  → A±k (w, s) are the simple poles at s and k − s.

Remark. Bochner’s Converse Theorem [2, Th. 7.1], [3, Th. 4] implies that the function w  → A±k (w, s) is essentially uniquely deﬁned by the ﬁrst equation in (4.2) and its poles. Let us make this precise in the case when ν± > 0: assume that ψ(w) = n≥ν

ann−w is convergent in some right half-plane and extends to a meromorphic function in C such that (w − s)(w − k + s)ψ(w) is entire of ﬁnite order and Ψ(w) = π−wΓ(w)ψ(w) satisﬁes Ψ(k−w) = ±Ψ(w). Then Ψ(w) is a multiple of A±k (w, s). Thus we see that these functions are in some sense universal: if ψ(w) is any Dirichlet series such that ψ(w)P(w) is entire of ﬁnite order for some polynomial P and such that Ψ(k − w) = ±Ψ(w), then

±

∂m

j

A±k (w, sj)

cj

Ψ(w) = Lf(w) +

![image 151](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile151.png>)

∂smj

j

for some cj, sj ∈ C, where f ∈ Mk(Γθ, ±) and Lf(w) = 0 ∞(f(it) − a0(f))tw−1dt. This gives a considerable strengthening of the abundance principle of Knopp [19].

Using the estimates from Section 6 we get quite precise information about the behavior of w  → A±k (w, s) in vertical strips.

- Lemma 4.1. Suppose that k/2 ≤ Res < k < 2 and let κ = max(k, 1) . Then


|A±k (u + iv, s)| ≤ C(s)π−u|Γ(u + iv)|(1 + |v|)κ+ε−u, k − κ − ε ≤ u ≤ κ + ε, for every ε > 0 and all suﬃciently big |v|, where C(s) > 0 depends only on s.

A weaker version of Lemma 4.1, with a cruder bound on the growth in the vertical direction, may be obtained directly from Proposition 3.3. This would in turn suﬃce to establish a weaker version of Theorem 1.1, as alluded to in the introduction.

Proof of Lemma 4.1. By the Cauchy–Schwarz inequality, we have

 

 

2

|αn,k± (s)|n−u

≤ 2l(1−2u)

|αn,k± (s)|2.

2l≤n<2l+1

2l≤n<2l+1

Therefore, by applying Proposition 6.4 from Section 6 we get

|αn,k± (s)|2 ≪s xk+|k−1| log2x,

n≤x

and thus the Dirichlet series representing w  → A±k (w, s) converges absolutely for Rew > κ. Let us set

πw Γ(w)A±k (w, s).

D(w) :=

![image 152](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile152.png>)

Note that D(w) can have poles only at w = k, s, k − s, since the potential pole at w = 0 is canceled by the pole at w = 0 of Γ(w). Since the Dirichlet series converges absolutely for Rew > κ, for arbitrary ﬁxed ε > 0 we have

D(κ + ε + iv) ≪ 1 and D(k − κ − ε + iv) ≪ (1 + |v|)2κ−k+2ε. Here the second inequality follows because of the absolute convergence of the Dirichlet series, and the second follows by the functional equation for A±k (k − w, s). Now

F(w) := D(w)(w − 1)(w − s)(w − (k − s)) is an entire function satisfying

F(κ + ε + iv) ≪ (1 + |v|)3 and F(k − κ − ε + iv) ≪ (1 + |v|)2κ−k+3+2ε. The deduction of the functional equation for D(w, s) implies the crude bound

|F(u + iv)| ≪ |v|3|Γ(u + iv)|−1

in the strip k−κ−ε ≤ u ≤ κ+ε. We may therefore use the Phragm´en–Lindelo¨f principle in a familiar way (see for example [28, Sect. 5.65]) to conclude that F(w)((κ+2ε−w)i)(w−κ−ε)−3 is a bounded analytic function in that strip.

To conclude the discussion of A±k (w, s), note that, as a corollary of (3.19), we obtain

- (4.4) A+l/2(w, 0) = −π−wΓ(w)

n≥1

rl(n) nw

![image 153](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile153.png>)

, l = 1, 2, 3,

where rl(n) is the number of representations of n as a sum of squares of l integers. In particular, A+1/2(w, 0) = −2π−wΓ(w)ζ(2w). Similarly, (3.19) implies

- (4.5) A−l/2(w, 0) = A−l/2(w, l/2) = 0, l = 1, 2, 3.


Using the results from Section 3.4.2 one can also easily obtain explicit expressions for A±l/2(w, 0) for other values of l.

- 4.2. Construction of the Dirichlet series kernels. We will now construct, in accordance with the general setup of Section 2, the Dirichlet series kernels corresponding to the interpolation formula of Theorem 1.1. This will provide us with an explicit construction of the functions Un(z) and Vρ,j(z) and will be used to prove our main result.


We deﬁne the Dirichlet series kernels H±(w, s) by

A−1/2(w/2, s/2) ζ∗(w)

h−n(s) nw/2

ζ∗(s) 2

H−(w, s) :=

=

, s = 0, 1,

![image 154](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile154.png>)

![image 155](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile155.png>)

![image 156](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile156.png>)

n≥1

- (4.6)

where ζ∗(s) = ΓR(s)ζ(s) is the completed zeta function. Formulas (4.4) and (4.5) show that both functions extend analytically also to s = 0, 1. Note that the coeﬃcients h±n(s) can be computed using M¨obius inversion as

- (4.7) h±n(s) =

ζ∗(s) 2

![image 157](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile157.png>)

d2|n

µ(d)αn/d± 2,1/2(s/2).

From this and (4.4), (4.5) we see that h±n(s), n ≥ 1 are entire (we also set h+1 (s) := 0). Since ζ∗(1 − s) = ζ∗(s), the functional equations (4.2) imply

H±(1 − w, s) = ±H±(w, s), H±(w, 1 − s) = ∓H±(w, s).

- (4.8)

Moreover, from (4.3) and the fact that ζ∗(w) has simple poles at w = 0, 1, we see that for a ﬁxed s the function w  → H±(w, s) has simple poles at w = s and w = 1−s with residues 1 and ∓1, and a pole at w = ρ of order at most m(ρ) for each nontrivial zero ρ of ζ(s).

From the above discussion we see that, if we deﬁne E±(w, s) = H+(w, s) ± H−(w, s), then w  → E+(w, s) (respectively w  → E−(w, s)) is a Dirichlet series with poles at w = ρ for nontrivial zeros of ζ and at w = s (respectively w = 1 − s). According to the setup of

Section 2, this suggests that E±(w, s) (up to an appropriate linear change of variables that maps the critical line to R) are Dirichlet series kernels associated to a Fourier interpolation formula with Λ = {(ρ − 1/2)/i: ζ∗(ρ) = 0} and Λ∗ = {±log n/(4π)}n≥1. Motivated by this we deﬁne Un±(z) as

- (4.9) Un±(z) := h∓n(1/2 + iz). Similarly, we deﬁne Vρ,j±(z) by


A+1/2(w/2, s/2) ζ∗(w) − α1+,1/2(s/2) =

ζ∗(s) 2

h+n(s) nw/2

H+(w, s) :=

, s = 0, 1,

![image 158](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile158.png>)

![image 159](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile159.png>)

![image 160](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile160.png>)

n≥2

m(ρ)−1

ij

H∓(w, 1/2 + iz) =

j=0

j! Vρ,j±(z) (w − ρ)j+1

+ O(1), w → ρ,

![image 161](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile161.png>)

or, equivalently,

- (4.10) Vρ,j±(z) :=

1 2πi |w−ρ|=ε

![image 162](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile162.png>)

i−j(w − ρ)j j!

![image 163](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile163.png>)

H∓(w, 1/2 + iz)dw, where ε is chosen so that ε < |ρ−1/2±z| and ε < |ρ−ρ′| for all ρ′ = ρ such that ζ∗(ρ′) = 0. We now turn to rigorously proving Theorem 1.1.

- 4.3. Proof of Theorem 1.1. As in the proof of Lemma 4.1 we will use certain estimates


for the coeﬃcients αn,k± (s) that are somewhat technical and are proved in Section 6. We deﬁne the auxiliary functions

D−(w, s) :=

ΓR(s) 2 n≥1

![image 164](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile164.png>)

αn,−1/2(s/2) nw/2

![image 165](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile165.png>)

, D+(w, s) :=

ΓR(s) 2 n≥1

![image 166](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile166.png>)

αn,+1/2(s/2) − α1+,1/2(s/2) nw/2

![image 167](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile167.png>)

,

and note that

H±(w, s) :=

ζ(s) ζ(w)

![image 168](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile168.png>)

D±(w, s).

- Lemma 4.2. Suppose that 1/2 ≤ Res < 1. Then

(4.11) |D±(u + iv, s)| ≤ C(s)(1 + |v|)(2+ε−u)/2, u ≤ 2 + ε, H±(1 + ε + iv, s) =

n≤x

(4.12) h±n(s)n−(1+ε+iv)/2 + O (1 + |v|)x−ε/3

for every ε > 0, where C(s) is a positive constant that depends only on s. Proof. The ﬁrst claim follows from Lemma 4.1. We next prove (4.12). Set A(x) :=

n≤x h±n (s). Using summation by parts, we get H±(w, s) =

n≤x

h±n(s)n−w/2 +

w 2

![image 169](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile169.png>)

∞

x

(A(y) − A(x))y−w/2−1dy

when Rew > 1, so it suﬃces to show that

A(x) ≪ε x1/2+ε/6 for every ε > 0. But this holds because

A(x) =

ζ∗(s) 2

![image 170](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile170.png>)

d≤

√x

![image 171](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile171.png>)

µ(d)

n≤x/d2

αn,±1/2(s/2) ≪

√x

![image 172](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile172.png>)

d≤

√x

![image 173](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile173.png>)

1 d ≤

![image 174](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile174.png>)

√xlog x

![image 175](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile175.png>)

when 1/2 ≤ Res < 1 by Proposition 6.5.

We also require an additional lemma which is a result from a paper by Ramachandra and Sankaranarayanan [26, Thm. 2].

- Lemma 4.3. There exists a positive constant c such that




|ζ(σ + it)|−1 ≤ exp c(log log T)2 holds for all suﬃciently large T.

min

max

1/2≤σ≤2

T≤t≤T+T1/3

We now consider a general function f in H1 and prove a representation that splits naturally into an even and an odd part, so that the even part yields Theorem 1.1. We set

s − 1/2 i let

F(s) := f

![image 176](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile176.png>)

F(s) − F(1 − s) 2 be respectively the even and odd part of F(s). The proof naturally splits into three parts. Proof of (1.2). Consider the operator

F(s) + F(1 − s) 2

and F−(s) :=

F+(s) :=

![image 177](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile177.png>)

![image 178](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile178.png>)

- (4.13) (RδFδ)(s) :=

1 4πi

![image 179](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile179.png>)

c+i∞

c−i∞

[H−δ(w, s) − H−δ(1 − w, s)]Fδ(w)dw,

where δ = ± and both 1 − c < Res < c and c > 1. The proof follows the usual scheme of computing these integrals in two diﬀerent ways. First, using the functional equation for H±(1−w, s), we express the integrand in (4.13) as Fδ(w) times a Dirichlet series in w. We then apply (4.12) and the assumption that f is in H1 to infer that

(RδFδ)(s) =

- 1

![image 180](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile180.png>)

- 2πi


c+i∞

c−i∞

H−δ(w, s)Fδ(w)dw

=

- 1

![image 181](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile181.png>)

- 2πi n≤x


h−nδ(s)

c+i∞

c−i∞

n−w/2Fδ(w)dw + O(x−ε/3)

=

n≤x

(M−1Fδ)(√n)h−nδ(s) + O(x−ε/3),

![image 182](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile182.png>)

- (4.14)

where M−1Fδ is the inverse Mellin transform of Fδ. Since Un(z) = Un+(z) are deﬁned by (4.9), this gives the ﬁrst sum on the right-hand side of (1.2) .

On the other hand, by viewing the integral in (4.13) as two contour integrals and using the residue theorem, we ﬁnd that

- (4.15) (RδFδ)(s) = Fδ(s) +


ρ:0<γ≤T

where

Resw=ρ H−δ(w, s)Fδ(w) + E(s, T),

|ζ(u + iT)|−1T−1/4+ε +

|f(c + it)|(1 + |v|)(2−c+ε)/2dv

E(s, T) ≪ max

1/2≤u≤2

|v|>T

for ε small enough. Indeed, D−δ(u+iv, s) ≪ (1+|v|)3/4+ε by Lemma 4.2 and Fδ(u+iv) ≪ (1+|v|)−1 for suﬃciently small ε by the assumption that f is in H1. Given a large positive integer k, we choose Tk in [2k, 2k+1] such that

|ζ(u + iTk)|−1 ≤ exp c(log log Tk)2 ,

max

1/2≤u≤2

which is feasible in view of Lemma 4.3. Let us deﬁne Un = n−2π1/4Un+ and Vρ,j = Vρ,j+ as in (4.9) and (4.10). Then we obtain (1.2) by comparing the right-hand sides of (4.14)

![image 183](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile183.png>)

and (4.15) and letting k → ∞. Rapid decay of the basis functions Un(z) and Vρ,j(z). By (4.7), the functions h±n(s) have rapid decay in vertical strips since |ζ∗(σ + it)| = O(ta

e−πt/4) and by (3.15) we have that |αm,± 1/2((σ + it)/2)| = O(eπt/4(1 + |t|)−k) for all k > 0. Thus Un(z) is rapidly decaying.

σ

To get the corresponding property of Vρ,j(z), we use (4.10) to infer that it is suﬃcient

to show that s  → ζ∗(s)A±1/2(w, s) is rapidly decaying in vertical strips (uniformly for w in compact sets). In view of (4.3), it is enough to check that

∞

s  → ζ∗(s)

(Fk±(it, s) − α0±,k(s))(tw−1 ± tk−w−1)dt is rapidly decaying in vertical strips. This is clear from Proposition 3.4. The interpolatory properties (1.3). From (3.17) and (4.7) we see that h±n(s) is the Mellin transform of

1

∞

u±n(x) :=

µ(d)b±n/d2(kx).

k=1 d2|n

Therefore, for m, n ≥ 1, from the interpolatory properties of bεm(x) (3.18) we conclude that

∞

µ(d)bεn/d2(k√m) =

uεn(√m) =

1, m = n, 0, m = n.

![image 184](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile184.png>)

![image 185](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile185.png>)

µ(d) =

√

k=1 d2|n

![image 186](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile186.png>)

d|

n/m

Since Un is an even function and Un(ξ) = n−1/4eπξu−n(e2πξ), this implies the interpolatory properties of Un at log4πm. By deﬁnition h±n(s) vanishes at s = ρ to the same order as ζ∗(s), and we therefore also get that Un(j)(ρ−i1/2) = 0 for 0 ≤ j < m(ρ).

![image 187](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile187.png>)

![image 188](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile188.png>)

Next, let us check the interpolatory properties of Vρ,j(z). From (4.10) we immediately see that V (j

′)

′−1/2

ρ,j (ρ

i ) = 0 for 0 ≤ j′ < m(ρ′), where ρ′ = ρ is a diﬀerent nontrivial zero of ζ with Imρ′ > 0. The property V (j

![image 189](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile189.png>)

′)

ρ,j (ρ−i1/2) = δj,j′ for 0 ≤ j′ < m(ρ) again follows from (4.10), since for any ε > 0 such that ε < |ρ − ρ′| for all ρ′ = ρ, the diﬀerence

![image 190](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile190.png>)

ij′−j(w − ρ)j j!

∂j′H− ∂sj′

- 1

![image 191](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile191.png>)

- 2πi |w−ρ|=ε


′)

V (j

ρ,j (z) −

(w, 1/2 + iz)dw

![image 192](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile192.png>)

![image 193](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile193.png>)

is equal to 0 for ε < |ρ − 1/2 ± z| and to δj,j′ for ε > |ρ − 1/2 ± z|. Finally, we need to verify that Vρ,j(±log4πn) = 0. To this end, we consider

![image 194](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile194.png>)

k≥1 b±n (kx) nw/2

U±(w, x) := ΓR(w)

![image 195](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile195.png>)

n≥1

and note that H±(w, s) is the Mellin transform in x of U±(w, x)/ζ∗(w). The function U±(w, x) continues analytically to a meromorphic function of w in C since it is the Mellin

transform of F1±/2(it, ϕx), where ϕx(z) = 12(θ(zx) − 1). Setting x = √m and using (3.18), we obtain

![image 196](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile196.png>)

![image 197](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile197.png>)

U±(w, √m) = ΓR(w)

1 nw/2

= ζ∗(w)m−w/2

![image 198](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile198.png>)

![image 199](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile199.png>)

n≥1 n=k2m

ﬁrst for Rew suﬃciently large, and then, by analytic continuation, for all w = 0, 1. The numbers Vρ,j(ξ), j ≥ 0 are simply the coeﬃcients of the principal part of the Laurent series of w  → U±(w, e2πξ)/ζ∗(w) at w = ρ. Since for ξ = log4πm the latter function specializes to an entire function w  → m−w/2, we get that Vρ,j(±log4πm) = 0.

![image 200](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile200.png>)

![image 201](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile201.png>)

This concludes the proof of Theorem 1.1.

- 4.4. Relation with the Riemann–Weil formula. We return brieﬂy to the viewpoint mentioned in the introduction, namely that we may think of the Riemann–Weil explicit formula as expressing a linear functional W in terms of our interpolation basis. This functional W acts on functions f in H1 and is deﬁned by the left-hand side of (1.1):


∞

Γ′(1/4 + it/2) Γ(1/4 + it/2) − log π dt + f

+ f −i 2

1 2π

i 2

- (4.16) Wf :=


.

f(t)

![image 202](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile202.png>)

![image 203](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile203.png>)

![image 204](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile204.png>)

![image 205](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile205.png>)

−∞

By the equality in (1.1) and the interpolatory properties of the basis functions, we then ﬁnd that

π−1Λ(n)/√n, n a square 0, otherwise,

![image 206](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile206.png>)

WUn =

while

WVρ,j =

2, j = 0 0, j > 0.

It would be interesting to know whether these curious properties of the basis functions could be obtained without resorting to the Riemann–Weil formula. In the same vein, it may be worthwhile searching for further relations between our Fourier interpolation formula and the Riemann–Weil explicit formula.

5. Fourier interpolation with zeros of Dirichlet L-functions and other Dirichlet series

The methods developed above give without much additional eﬀort Fourier interpolation formulas associated with the nontrivial zeros of Dirichlet L-functions and, more generally, of functions that are representable by Dirichlet series and satisfy a functional equation of the form L∗(k − s) = ±L∗(s), for

L∗(s) = rs/2ΓR(s)L(s) or L∗(s) = rs/2ΓC(s)L(s)

- where r is some positive number. Here we use the common notation ΓR(s) := π−s/2Γ(s/2), ΓC(s) := 2(2π)−sΓ(s). We will now present some key results of this kind, with emphasis on features that have not appeared earlier in our treatise.


We begin with the case of Dirichlet characters χ. We recall that the gamma factor appearing in the functional equation for L(s, χ) diﬀers depending on whether χ is even or odd, i.e., on whether χ(−n) = χ(n) or χ(−n) = −χ(n). This leads to a principal diﬀerence between the respective Fourier interpolation bases, and it is natural to treat the two cases separately. In either case, however, we will need the following analogue of Lemma 4.3.

Lemma 5.1. Let χ be a primitive Dirichlet character. There exists a positive constant c = cχ such that

- (5.1) min

T≤t≤2T

max

1/2≤σ≤2

|L(σ + it, χ)L(σ + it, χ)|−1 ≤ exp c(log log T)2 holds for all suﬃciently large T.

![image 207](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile207.png>)

The proof is word for word the same as that in [26], with ζ(s) replaced by L(s, χ)L(s, χ). We could prove the same bound for minT≤t≤2T max1/2≤σ≤2 |L(σ + it, χ)|−1, which would suﬃce when χ is real. In the complex case, however, (5.1) is useful because we integrate along segments that cross the critical strip. Invoking the functional equation for L(s, χ), we then need lower bounds for both |L(s, χ)| and |L(s, χ)| along such segments.

![image 208](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile208.png>)

![image 209](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile209.png>)

5.1. Fourier interpolation bases associated with even primitive characters. Theorem 1.1 only deals with even functions, but the result extends painlessly to arbitrary functions in H1, as there is a similar interpolation formula for odd functions. In the case of complex characters, it is less natural to decompose the interpolation formula into even and odd parts. We therefore take the opportunity to state and prove in one stroke an interpolation formula for arbitrary functions.

- Theorem 5.1. Let χ be a primitive even Dirichlet character to the modulus q for some


- q ≥ 2. There exist two sequences of rapidly decaying entire functions Un(z), n ∈ Z, and Vρ,j(z), 0 ≤ j < m(ρ), with ρ ranging over the nontrivial zeros of L(χ, s), such that for


- every function f in H1 and every z = x + iy in the strip |y| < 1/2 we have


f(z)= lim

N→∞

0<|n|≤N

f

sgn(n)(log |n| + log q) 4π

![image 210](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile210.png>)

Un(z)+

f(−i/2) L∗(0, χ)

![image 211](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile211.png>)

+

f(i/2) L∗(1, χ)

![image 212](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile212.png>)

U0(z)

+ lim

k→∞

|γ|≤Tk

m(ρ)−1

j=0

f(j)

ρ − 1/2 i

![image 213](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile213.png>)

- (5.2) Vρ,j(z)

for some increasing sequence of positive numbers T1, T2, ... tending to ∞ that is independent of f and z. Moreover, the functions Un(z) and Vρ,j(z) enjoy the following interpolatory properties:

- (5.3)


′)(log |n′|+log q)

Un(j) ρ−i1/2 = 0, Un sgn(n

4π = δn,n′, V (j

![image 214](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile214.png>)

![image 215](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile215.png>)

′) ρ,j

ρ′−1/2

i = δ(ρ,j),(ρ′,j′), Vρ,j sgn(n)(log4π|n|+logq) = 0,

![image 216](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile216.png>)

![image 217](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile217.png>)

with ρ, ρ′ ranging over the nontrivial zeros of L(s, χ), j, j′ over all nonnegative integers less than or equal to respectively m(ρ) − 1, m(ρ′) − 1, and n, n′ are in Z {0}.

The distinguished function U0(z) satisﬁes U0(0) = U0(1) = 1/2 as well as

- (5.4) U0(j)

ρ − 1/2 i

![image 218](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile218.png>)

= 0 and U0

sgn(n)(log |n| + log q) 4π

![image 219](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile219.png>)

= 0

when, as above, ρ ranges over the nontrivial zeros of L(s, χ), j over all nonnegative integers less than or equal to m(ρ) − 1, and n over all integers diﬀerent from 0. The formula takes however a more involved and interesting form at the special points 0 and 1 as will be exhibited after we have established the theorem. As in the proof of Theorem 1.1, we will resort to the change of variable z = (s−1/2)/i and use Mellin instead of Fourier transform. Most of the proof follows the same lines as that of Theorem 1.1, and we therefore omit some of the computations.

Proof sketch of Theorem 5.1. We set

Hδ(w, s; χ) :=

L∗(s, χ) 2L∗(w, χ)Aδ1/2(w/2, s/2),

![image 220](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile220.png>)

where L∗(s, χ) = qs/2ΓR(s)L(s, χ). These kernels satisfy the functional equations

- (5.5) Hδ(w, s; χ) = δw(χ)Hδ(1 − w, s; χ), where w(χ) is the root number of L(s, χ). We now consider the operator

![image 221](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile221.png>)

(TχF)(s) :=

1 4πi

![image 222](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile222.png>)

c+i∞

c−i∞

- (5.6) [H+(w, s; χ)F(w) + w(χ)H+(1 − w, s; χ)F(1 − w)]dw


![image 223](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile223.png>)

c+i∞

1 4πi

[H−(w, s; χ)F(w) − w(χ)H−(1 − w, s; χ)F(1 − w)]dw,

+

![image 224](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile224.png>)

![image 225](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile225.png>)

c−i∞

where both 1 − c < Res < c and c > 1, with the additional assumption that F(s) is analytic in 1 − c ≤ Res ≤ c and

∞

|F(σ + it)|(1 + |t|)dt < ∞.

sup

1−c≤σ≤c

∞

Following the corresponding computation in Section 4.3, we may compute the integrals on the right-hand side of (5.6) and get

∞

1 4

µ(d)χ(d)(αn/d+ 2(s) + αn/d− 2(s))

(M−1F)((qn)1/2)

L∗(s, χ)

(TχF)(s) =

![image 226](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile226.png>)

n=1

d2|n

∞

1 4

µ(d)χ(d)(αn/d− 2(s) − αn/d+ 2(s)),

L∗(s, χ)w(χ)

(M−1F)((qn)−1/2)(qn)−1/2

+

![image 227](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile227.png>)

![image 228](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile228.png>)

n=1

d2|n

where we have set αn±(s) := αn,±1/2(s/2). On the other hand, viewing the two integrals on the right-hand side of (5.6) as contour integrals, we may use the functional equations (5.5)

and the residue theorem to deduce that (TχF)(s) = f(s) − α0−(s)qs/2L(s, χ)

F(1) L∗(1, χ)

F(0) L∗(0, χ)

+

![image 229](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile229.png>)

![image 230](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile230.png>)

- 1

![image 231](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile231.png>)

- 2


Resw=ρ H+(w, s; χ)F(w) + Resw=ρ H−(w, s; χ)F(w)

lim

+

k→∞

|γ|≤Tk

for some sequence Tk → ∞. To achieve this, we use the sub-convexity bound L(1/2+it) ≪ q1/2|t|1/6 log(q|t|) (see [10, p. 149]), along with Lemma 4.2 and Lemma 5.1. We arrive at

- (5.2) by equating our two expressions for (TχF)(s) and changing back to Fourier transforms and the variable z = (s − 1/2)/i.


To evaluate (5.2) at s = 1, we recall from (4.4) that

A+1/2(w/2, 1/2) = −2ζ∗(w). Plugging this into (5.2), we arrive at

∞

log n + 21 log q 2π

L∗(1, χ) L∗(0, χ)

![image 232](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile232.png>)

(qn)−1/2 f

f(i/2) = q1/2L(1, χ)

f(−i/2) +

(1 − χ(p))

![image 233](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile233.png>)

![image 234](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile234.png>)

n=1

p|n

∞

(qn)−1/2 f −log n − 12 log q 2π

![image 235](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile235.png>)

− q1/2L(1, χ)w(χ)

- (5.7) (1 − χ(p))


![image 236](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile236.png>)

![image 237](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile237.png>)

n=1

p|n

ζ(w) qw/2L(w, χ)

+ q1/2L(1, χ) lim

Resw=ρ

f(w),

![image 238](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile238.png>)

k→∞

|γ|≤Tk

which has a curious resemblance with the Riemann–Weil Formula.

- 5.2. Fourier interpolation bases associated with odd characters. In this case of odd characters, the gamma factor for L(s, χ) is π−(s+1)/2Γ((s + 1)/2), and thus we will use the function A±3/2(w2+1, s+12 ) which involves the same gamma factor. Note that the


![image 239](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile239.png>)

![image 240](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile240.png>)

abscissa of convergence and the abscissa of absolute convergence of w  → A±3/2(w+12 , s+12 ) are both equal to 2, and we therefore need to require that functions be analytic in a strip of width 3 + ε. As in the preceding cases, we need a growth condition in the strip, but we may require less at the boundary of the strip because the Dirichlet series kernel converges absolutely there. We ﬁnd it convenient to restrict to functions f that are analytic in the strip | Im z| < 3/2 + ε and satisfy

![image 241](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile241.png>)

![image 242](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile242.png>)

|f(x + iy)| ≪ (1 + |x|)−1−ε

for some ε > 0, where we in the latter inequality assume that |y| ≤ (3 + ε)/2. We let H2 denote the space of all such functions.

- Theorem 5.2. Let χ be a primitive odd Dirichlet character to the modulus q for some


- q ≥ 3. There exist two sequences of rapidly decaying entire functions Un(z), n ∈ Z, and


Vρ,j(z), 0 ≤ j < m(ρ), with ρ ranging over the nontrivial zeros of L(χ, s), such that for

- every function f in H2 and every z = x + iy in the strip |y| < 1/2 we have


f(−3i/2) L∗(0, χ)

sgn(n)(log |n| + log q) 4π

f(3i/2) L∗(1, χ)

Un(z) +

U0(z)

+

f

f(z)= lim

![image 243](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile243.png>)

![image 244](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile244.png>)

![image 245](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile245.png>)

N→∞

0<|n|≤N

m(ρ)−1

ρ − 1/2 i

f(j)

+ lim

- (5.8) Vρ,j(z)

for some increasing sequence of positive numbers T1, T2, ... tending to ∞ that does not depend on neither f nor on z. Moreover, the functions Un(z) and Vρ,j(z) enjoy the following interpolatory properties:

- (5.9)


![image 246](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile246.png>)

k→∞

j=0

0<|γ|≤Tk

′)(log |n′|+log q)

Un(j) ρ−i1/2 = 0, Un sgn(n

4π = δn,n′, V (j

![image 247](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile247.png>)

![image 248](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile248.png>)

′) ρ,j

ρ′−1/2

i = δ(ρ,j),(ρ′,j′), Vρ,j sgn(n)(log4π|n|+logq) = 0,

![image 249](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile249.png>)

![image 250](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile250.png>)

with ρ, ρ′ ranging over the nontrivial zeros of ζ(s), j, j′ over all nonnegative integers less than or equal to respectively m(ρ) − 1, m(ρ′) − 1, and n, n′ are in Z {0}.

As in the case of even characters, the distinguished function U0(z) satisﬁes (5.4), and we also have U0(±3i/2) = 1/2. The formula at the special points ±3i/2 will be somewhat more complicated than (5.7) and will instead of ζ(w) involve the Dirichlet series

∞

r3(n)n−(w+1)/2,

−

n=1

where r3(n) is the number of representations of n as the sum of squares of 3 integers. Proof. We deﬁne the Dirichlet series kernel

L∗(s, χ) 2L∗(w, χ)Aδ3/2

s + 1 2 and follow the same argument as in Theorem 5.1.

w + 1 2

Hδ(w, s; χ) :=

,

![image 251](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile251.png>)

![image 252](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile252.png>)

![image 253](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile253.png>)

- 5.3. Fourier interpolation with zeros of other Dirichlet series. We may deduce an abundance of further Fourier interpolation formulas based on the techniques developed in Section 4, as will now be brieﬂy explained. Detailed analysis of these generalizations falls outside the scope of this paper, so we only sketchily outline the details, and in each case, we will only indicate the construction of the corresponding Dirichlet series kernels


H±(w, s) that lead to the interpolation formula with Λ being the (multi-)set given by a suitable rotation of the nontrivial zeros of L(s).

- 5.3.1. Dedekind zeta functions of imaginary quadratic ﬁelds and Hecke L-functions of modular forms. First, we obtain Fourier interpolation formulas associated with zeros of Dedekind zeta functions ζK(s) for imaginary quadratic ﬁelds K. In this case we deﬁne

H±(w, s) :=

ζK∗ (s) ζ∗

![image 254](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile254.png>)

K(w)A±1 (w, s),

where ζK∗ (s) = |∆K|s/2ΓC(s)ζK(s) is the completed zeta function and ΓC(s) = 2(2π)−sΓ(s). More generally, this construction applies to products of two Dirichlet L-functions whose

(primitive) characters have diﬀerent parity, i.e., L(s) = L(s, χ1)L(s, χ2) where χ1 is an even character and χ2 is an odd character. In this case the corresponding sequence of points on the Fourier side is Λ∗ = {±log(2n

√

![image 255](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile255.png>)

N)/(2π)}, where N is the conductor, i.e., N = |∆K| for L(s) = ζK(s) and N = q1q2 for L(s) = L(s, χ1)L(s, χ2).

Next, using A±k (w, s) for an even integer k ≥ 2 we can construct Fourier interpolation formulas associated to zeros of Hecke L-functions of modular forms. More precisely, let f in Sk(Γ0(N)) be a normalized Hecke newform. Then L(s, f) = n≥1 ann−s admits an analytic continuation to C and satisﬁes L∗(k − s, f) = L∗(s, f), where L∗(s, f) = Ns/2ΓC(s)L(f, s) is the completed L-function. In this case, we deﬁne H±(w, s) as

H±(w, s) :=

L∗(s, f) L∗(w, f)A±k (w, s).

![image 256](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile256.png>)

The formula again involves the sequence Λ∗ = {±log(2n

√

![image 257](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile257.png>)

N)/(2π)}.

- 5.3.2. Dirichlet series without Euler products. Furthermore, we may obtain a continuous family of Fourier interpolation formulas associated with the sequence of points Λ∗ = {0, ±(log n)/(4π), n ≥ 1} by starting from kernels of the form


(w, s) := Aεk(s/2, s0) Aεk(w/2, s0)A±k ε(w/2, s),

- (5.10) Hk,ε,s±


![image 258](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile258.png>)

0

- where s0 is some ﬁxed point satisfying 0 ≤ Res0 ≤ k. The (multi-)set Λ dual to Λ∗ will


now be a suitable rotation and translation of the zero set of Aεk(w/2, s0).

We may however need to put more severe restrictions on the functions represented by Fourier interpolation formulas associated with kernels such as those deﬁned by (5.10). Indeed, since the denominator of (5.10) in general can not be represented as an Euler product, the techniques from [26] must be abandoned. In the absence of a multiplicative structure, we may resort to the following classical argument, yielding a much cruder bound than that of Lemma 4.3. We use then that the function A(w) := Aεk(w/2, s0) grows polynomially in the vertical direction, and hence, by Jensen’s formula, the number of zeros in a strip of width 1 at height T is O(log T). An application of the Borel–Carath´eodory theorem shows that

|A(w)| |γ−T|≤1 |s − ρ|

≥ T−C

![image 259](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile259.png>)

for some constant C when | Imw −T| ≤ 1/2. Hence we can ﬁnd an η, |η| ≤ 1/2, such that

σ0

σ0

|σ + i(T + η) − ρ)|−1dσ ≪ Tclog logT

|F(σ + i(T + η)|−1dσ ≤ TC

- (5.11)


1−σ0 |γ−T|≤1

1−σ0

for some constant c. The bound in (5.11) is our replacement for Lemma 4.3, and, consequently, we need to require that functions decay accordingly.

The individual basis functions arising from kernels of the form (5.10) will have additional poles at s = 2s0 and s = 2(k − s0), and hence they do not belong to any nice function space. The situation is particularly bad in the most natural case when s0 is on the line of symmetry Res = k/2. Then the inverse Fourier transform of any basis function is neither integrable nor in any Lp space for p < ∞. This is a less attractive feature of “basis decompositions” stemming from (5.10).

- 5.3.3. Further extensions and more complicated gamma factors. Further extensions are obtained if we apply algebraic operations that preserve functional equations in a suitable way. We may for instance take linear combinations of L-functions that satisfy the same functional equation. Moreover, we may, for an arbitrary polynomial P of degree n, multiply for example a Dirichlet L-function by rns/2P(r−(s−1/2)) with r > 1 an integer and P(0) = 0. Then the polynomial


Q(z) = znP(1/z)

will appear in the functional equation, where n is the degree of P. In other words, any complex arithmetic progression with common diﬀerence 2π/ log r may be adjoined to a given multi-set Λ stemming from the nontrivial zeros of an L-function to which our methods apply. This allows us, in particular, to establish a Fourier interpolation formula associated with every Dirichlet L-function L(s, χ), irrespective of whether χ is primitive or not. As should be clear from the preceding two subsections, by adjoining such an arithmetic progression, we will ﬁnd that both the negative and positive part of the sequence Λ∗ are “pushed away” by log r/(4π) from the origin.

We can also treat Dirichlet series with more complicated gamma factors, although in this case the results are less satisfactory in the sense that while we get a Fourier interpolation formula, in general the resulting functions Un and Vρ,j will no longer form a basis, and we will not get the interpolatory properties like in (1.3). For example, let L(s) satisfy L∗(1 − s) = L∗(s) where L∗(s) = Ns/2Γr

R (s)Γr

C (s)L(s), and let L0 be another Dirichlet series such that L∗0(s) = N0s/2Γr

2

1

1−1

R (s)Γr

C (s)L0(s). Then we can form a Dirichlet series kernel

2

L∗(s) L∗(w)

L∗0(w)A±1/2(w/2, s/2),

H±(w, s) :=

![image 260](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile260.png>)

which has the expected poles and leads to a Fourier interpolation formula with zeros of L(s) and Λ∗ = {0, ±log(nN/N

0)

4π , n ≥ 1}.

![image 261](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile261.png>)

- 5.3.4. Density of interpolation nodes. Let us ﬁnally note that Kulikov’s inequality for Λ and Λ∗ (see (2.10)) will hold in the same marginal way as when Λ consists of the zeros of ζ(s), whenever these sequences (or multisets) are constructed as indicated above. Indeed, we may in all the above cases establish a Riemann–von Mangoldt formula. We may for instance observe that the number of nontrivial zeros ρ = β + iγ of A(w) satisfying |γ| ≤ T will be


T π

T 2πe

log

+ O(log T).

![image 262](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile262.png>)

![image 263](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile263.png>)

We follow the standard approach to prove this, i.e., we apply the argument principle along with the functional equation, and we use the Hadamard product of A(w) to control its logarithmic derivative. If we adjoin arithmetic progressions to Λ by multiplying, say, a Dirichlet L-function by rns/2P(r−(s−1/2)), then there will be an additional term

nT π

log r

![image 264](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile264.png>)

in the Riemann–von Mangoldt formula, balancing the “repulsion” by nlog r/(4π) of the sequence Λ∗ from the origin.

6. Estimates for the Fourier coefficients of Fk±(τ, s)

In this section we will derive estimates for the growth of αn,k± (s) and certain related quantities as a function of n. As before, we assume that k ≥ 0.

First, it will be convenient to deﬁne two quantities related to γτ, which we recall is the (generically unique) element of Γθ that maps τ ∈ H to the fundamental domain F. The ﬁrst quantity is I(τ), the imaginary part of γττ, i.e.,

I(τ) := Im γττ.

It is easy to see that the function I: H → R is continuous and Γθ-invariant. The second quantity is N: H → Z≥0, which we deﬁne as one plus the number of inversions S that appear in the canonical representation of γτ, i.e.,

N(τ) :=j + ε0 + ε1, γτ = Sε

T2m

0

1

ST2m

2

. . .ST2m

Sε

.

j

1

In cases when γτ is not uniquely deﬁned, i.e., for τ ∈ Γθ∂F, we set N(τ) to be the larger of the two possible values.

- 6.1. Estimates for the contour integral. Our ﬁrst step is to show that Fk±(τ, s) is bounded for τ ∈ F. We prove this for the slightly more general functions Fk±(τ, ϕ) from


- Theorem 3.1, as long as ϕ is bounded on the domain D illustrated in Figure 6.1. Explicitly we set


![image 265](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile265.png>)

![image 266](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile266.png>)

D := {τ ∈ H: | Reτ| < 1, 3/4 < |τ| < 4/3, |τ ± 1/2| > 1/2};

the particular shape of D is not important as long as it contains the geodesic from −1 to 1 and lies in F ∪ SF.

![image 267](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile267.png>)

D

−1 1 Figure 6.1. The domain D.

- Proposition 6.1. Let k ≥ 0 and ϕ: H → C be analytic such that |ϕ(τ)| ≤ Cϕ for τ in D, where D is deﬁned as above. Then for τ ∈ F we have


|Fk±(τ, ϕ)| ≪k

Cϕ, k ± 1  ∈ 1 + 4Z, Cϕ Im(τ)−1, otherwise.

Proof. Without loss of generality we may assume that Reτ is in (−1, 0), |τ| > 1, and that |τ − i| > 1/10 (for τ close to i we get the claimed bound using the contour deformation from Figure 3.3). We will also assume that Imτ ≤ 1/2 (for Imτ > 1/2 the claim follows from the same argument, but with simpler estimates). By deﬁnition of Fk±(τ, ϕ) we have

- 1

![image 268](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile268.png>)

- 2


Fk±(τ, ϕ) =

i

Kk±(τ, z)(ϕ(z) ∓ (z/i)−kϕ(−1/z))dz.

−1

Set ϕ±(z) := 21(ϕ(z) ∓ (z/i)−kϕ(−1/z)). Note that ϕ+(i) = 0. Since D is invariant under z  → −1/z, by assumption we have

![image 269](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile269.png>)

|ϕ±(z)| ≪k Cϕ, z ∈ D.

To estimate the integral, we change the variable of integration to w = J(z) and deform the contour of integration in w from the segment [0, 64] to a curve ℓ in the lower half-plane (see Figure 3.2) in such a way that its preimage under J in F ∪ SF lies in D. Using (3.6) to make the change of variables, we obtain

![image 270](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile270.png>)

i

J−(τ)θ2k(τ) Jν−−1(τ)

Fk−(τ, ϕ) =

![image 271](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile271.png>)

−1

J−(τ)θ2k(τ) Jν−−1(τ)

1 π

=

![image 272](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile272.png>)

![image 273](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile273.png>)

0

Jν−(z) θ2k(z)

1 J(τ) − J(z)

ϕ−(z)θ4(z)dz

![image 274](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile274.png>)

![image 275](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile275.png>)

64

ϕ−(t(w)) J(τ) − w

1 θ2k(t(w))

wν−−1/2(64 − w)−1/2dw,

![image 276](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile276.png>)

![image 277](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile277.png>)

where t(w) is the inverse function to z  → J(z). Since J(τ) belongs to the upper half-plane and w belongs to the lower, we have |J(τ) − w| ≫ |J(τ)|2 + |w|2. From this we get

![image 278](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile278.png>)

−−1/2|64 − w|−1/2 |θ2k(t(w))| |J(τ)|2 + |w|2

|w|ν

|Fk−(τ, ϕ)| ≪ Cϕ|J−(τ)θ2k(τ)| |Jν−−1(τ)| ℓ

|dw|

![image 279](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile279.png>)

![image 280](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile280.png>)

![image 281](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile281.png>)

−ie−1

−−(k+2)/4|64 − w|−1/2 logk |w−1| |J(τ)|2 + |w|2

≪k Cϕ|J−(τ)θ2k(τ)| |Jν−−1(τ)|

|w|ν

|dw|

1 +

![image 282](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile282.png>)

![image 283](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile283.png>)

![image 284](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile284.png>)

0

e−1

t−{(k+2)/4} |J(τ)|2 + t2

≪ Cϕ|J−(τ)θ2k(τ)| |Jν−−1(τ)|

log−k(t−1)

1 +

dt .

![image 285](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile285.png>)

![image 286](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile286.png>)

![image 287](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile287.png>)

0

From this we obtain (using Lemma 6.1 below), for k  ∈ 2 + 4Z,

|Fk−(τ, ϕ)| ≪k Cϕ|J−(τ)θ2k(τ)|

Im(τ)k ≪k Cϕ

![image 288](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile288.png>)

|J(k−2)/4(τ)|

when τ approaches the real line inside the fundamental domain. For k ∈ 2 + 4Z using the same argument we obtain

|Fk−(τ, ϕ)| ≪k Cϕ Im(τ)−1 . For Fk+ we calculate

i

θ2k(τ) Jν+−1(τ)

Jν

(z) θ2k(z)

J−(z) J(τ) − J(z)

+

Fk+(τ, ϕ) =

ϕ+(z)θ4(z)dz

![image 289](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile289.png>)

![image 290](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile290.png>)

![image 291](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile291.png>)

−1

64

θ2k(τ) Jν+−1(τ)

ϕ+(t(w)) J(τ) − w

1 θ2k(t(w))

1 π

+−1dw and again using Lemma 6.1 we get |Fk+(τ, ϕ)| ≪

wν

=

![image 292](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile292.png>)

![image 293](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile293.png>)

![image 294](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile294.png>)

![image 295](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile295.png>)

0

+−1

|θ2k(τ)| |Jν+−1(τ)| ℓ

|w|ν

|ϕ+(t(w))| |θ2k(t(w))|

|dw|

![image 296](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile296.png>)

![image 297](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile297.png>)

![image 298](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile298.png>)

![image 299](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile299.png>)

|J(τ)|2 + |w|2

e−1

t−{(k+4)/4} |J(τ)|2 + t2

≪k Cϕ |θ2k(τ)| |Jν+−1(τ)|

log−k(t−1)

dt .

1 +

![image 300](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile300.png>)

![image 301](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile301.png>)

![image 302](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile302.png>)

0

Thus for k  ∈ 4Z we have

|Fk+(τ, ϕ)| ≪k Cϕ |θ2k(τ)|

Im(τ)k ≪k Cϕ,

![image 303](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile303.png>)

|Jk/4(τ)|

and for k ∈ 4Z we get |Fk+(τ, ϕ)| ≪k Cϕ Im(τ)−1. In the proof above we have used the following simple lemma. Lemma 6.1. Let α be a real number and β be a number in (−1, 0]. Then as T → ∞

e−1

tβ logα(t−1) √T−2 + t2

T−β logα T , β < 0 , logα+1 T , β = 0, α = −1 .

dt ≍

![image 304](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile304.png>)

![image 305](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile305.png>)

0

Proof. For β < 0 we have

e−1

T−1

e−1

tβ logα(t−1) √T−2 + t2

tβ logα(t−1)dt +

tβ−1 logα(t−1)dt

dt ≍ T

![image 306](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile306.png>)

![image 307](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile307.png>)

T−1

0

0

log T

= TE−α((1 + β) log T) log1+α T +

e−βxxαdx ≍ T−β logα T,

1

where Ea(x) := 1 ∞ e−txt

dt ∼ e−xx, x → +∞, and the implied constants only depend on α and β. Similarly, for β = 0 we have

![image 308](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile308.png>)

![image 309](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile309.png>)

a

e−1

logα(t−1) √T−2 + t2

logα+1(T) α + 1 ≍ logα+1 T .

dt ≍ TE−α(log T) log1+α T +

![image 310](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile310.png>)

![image 311](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile311.png>)

![image 312](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile312.png>)

0

In particular, since ϕ(τ) = (τ/i)−s is obviously bounded in D, the above proposition applies to Fk±(τ, s) and shows that it is bounded in F.

- 6.2. Estimates for Fk±(τ, ϕ) near the real line. To estimate Fk±(τ, ϕ) away from the fundamental domain we repeatedly apply periodicity and the functional equation (3.3).


Let us denote by | the slash operator |±k in weight k twisted by the character of Γθ that sends S to ±1. To further simplify the notation we will write F(τ) instead of Fk±(τ, ϕ).

Let us denote ψ = 2ϕ±. We deﬁne a 1-cocycle {ψγ}γ∈Γθ

in such a way that ψS = ψ and ψT2 = 0. In other words, the functions ψγ satisfy

1|γ2, γ1, γ2 ∈ Γθ.

ψγ

1γ2 = ψγ

+ ψγ

2

Any such 1-cocycle is uniquely determined by ψS and ψT2 since Γθ is generated by S and T2, and since the only relation between the generators is S2 = 1 and by deﬁnition ψ

satisﬁes ψ+ψ|S = 0, the family of functions {ψγ}γ is indeed well-deﬁned. Note that, more generally, for γ1, . . ., γn ∈ Γθ we have

n−1|γn + · · · + ψγ

1|γ2 . . .γn.

+ ψγ

1γ2...γn = ψγ

- (6.1) ψγ


n

Since γ  → F − F|γ and γ  → ψγ are 1-cocycles that take equal values on the group generators, we have F − F|γ = ψγ for all γ ∈ Γθ.

Let τ ∈ H be such that Reτ ∈ (−1, 1) and |τ| < 1, and consider the element γ ∈ Γθ that sends τ0 ∈ j∈Z(2j + F) to τ. Let us write γ as ST2m

S . . .T2m

S, mi ∈ Z {0}, which we can assure by changing τ0 by a translation, if necessary. Then, using (6.1) and the fact that ψT2 = 0 we get

n

1

- (6.2) ψγ = ψ + ψ|T2m


S + · · · + ψ|T2m

S . . .T2m

S. Note that the slash action has the property

n

1

1

Im(γτ)k/2 Im(τ)k/2

|(f|kγ)(τ)| = |f(γτ)|

. In particular, (6.2) implies

![image 313](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile313.png>)

|ψγ(τ0)| Im(τ0)k/2 ≤ |ψ(τ0)| Im(τ0)k/2 + |ψ(τ1)| Im(τ1)k/2 + · · · + |ψ(τn)| Im(τn)k/2,

where τj = T2m

S . . . T2m

Sτ0, and τ = Sτn. Therefore,

j

1

- (6.3) |F(τ)| Im(τ)k/2 ≤ |F(τ0)| Im(τ0)k/2 + |ψ(τ0)| Im(τ0)k/2 +

n

i=1

|ψ(τi)| Im(τi)k/2. Proposition 6.2. With the above notation assume that |ψ(z)| ≤ C for |z| ≥ 1/2. Then

- (6.4) |F(τ)| Im(τ)k/2 ≪k

 



C(I(τ)k/2 + N(τ)1−k/2) k ∈ (0, 2), C(I(τ) + log(1 + Im(τ)−1)) k = 2, C(I(τ)k/2 + 1) k > 2.

Proof. Since |τ0| ≥ 1 by induction we see that for j ≥ 1 we have Imτj ≤ 1 and |τj| ≥ 1. By Proposition 6.1 the ﬁrst two terms on the right of (6.3) are ≪k C(1 + I(τ)k/2) and the remaining sum is trivially bounded by C j N=1(τ) Im(τj)k/2. Note that Imτj ≤ 2/(2j − 1) (see Lemma 2 in [25]), so that n ≪ Im(τ)−1. Thus

n

j=1

Im(τj)k/2 ≪k

 



(n + 1)(2−k)/2 k ∈ (0, 2), log(n + 1) k = 2, 1 k > 2.

Since n + 1 = N(τ) and n ≪ Im(τ)−1 this implies the claim.

6.3. Estimates for the Fourier coeﬃcients. From now on we concentrate on the case ϕ(τ) = (τ/i)−s. Using the estimates for I(τ) and N(τ) from Section 6.4 and Section 6.5 below, we will now obtain various estimates for αn,k± (s). For 0 ≤ Res ≤ k deﬁne

- (6.5) c(s) := max


|(z/i)−s ± (z/i)s−k| ≤ 2k+1eπ|Ims|/2.

|z|≥1/2

- Proposition 6.3. Let k > 0 and 0 ≤ Res ≤ k. Then


 

c(s)nk/2(1 + log2−k n), k ∈ (0, 2), c(s)n(1 + log n), k = 2, c(s)nk−1, k > 2,

αn,k± (s) ≪k



where c(s) is deﬁned in (6.5). Proof. We have αn,k± (s) = 21 i/n i/n−+11 Fk±(τ, s)e−πinτdτ. Therefore, for 0 < k < 2 we have

![image 314](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile314.png>)

1

c(s) 2

(I(x + i/n)k/2 + N(x + i/n)1−k/2)dx ≪k c(s)nk/2(1 + log2−k n), where we have used Proposition 6.6 and Corollary 6.1. Similarly, for k = 2 we have

|αn,k± (s)| ≪k nk/2

![image 315](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile315.png>)

−1

1

c(s) 2

|αn,±2(s)| ≪k n

(I(x + i/n) + log n)dx ≪ c(s)n(1 + log n), and for k > 2 we have

![image 316](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile316.png>)

−1

1

c(s) 2

|αn,k± (s)| ≪k nk/2

(I(x + i/n)k/2 + 1)dx ≪ c(s)nk−1,

![image 317](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile317.png>)

−1

as claimed. Similarly, we get an estimate for sums of squares of the coeﬃcients.

- Proposition 6.4. Let k ∈ (0, 2) and 0 ≤ Res ≤ k. Then for x ≥ 2 we have

n≤x

|αn,k± (s)|2 ≪k c(s)2xk+|k−1| log2 x.

Proof. Using Proposition 6.2 we get

n≥0

|αn,k± (s)|2tke−2πnt =

1 2

![image 318](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile318.png>)

1+it

−1+it

|F(τ)|2 Im(τ)kdτ ≪k c(s)2

1

−1

(I(x+it)k+N(x+it)2−k)dx.

By Proposition 6.6 and Corollary 6.1 the integral on the right is bounded by t−|k−1| log2(1/t). Setting t = 1/x gives the claim.

Note that from the proof of Lemma 4.1 it follows that for k ≥ 1 and 0 < Res < k the Dirichlet series deﬁning A±k (w, s) converges absolutely for Rew > k. Since for 1 ≤ k < 2 the function w  → A−k (w, s) has a pole at w = k, we see that the above bound is optimal up to powers of log x in this range.

Finally, we give an approximation to the partial sums n≤x αn,k± (s).

- Proposition 6.5. Let 0 < k < 2 and k/2 ≤ Res ≤ k. Then


(πx)k Γ(k + 1)

(πx)s Γ(s + 1)

αn,k± (s) = ±α0±,k(s)

+ O(c(s)xk/2 log3x).

+

![image 319](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile319.png>)

![image 320](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile320.png>)

n≤x

Proof. Let x = N + 1/2, where N ∈ Z and deﬁne S(x) = n≤x αn,k± (s). To simplify the notation we will write F(τ) = Fk±(τ, s). Since Nn=0 e−πinτ = eπiτe−e−Nπiτ

πiτ−1 we have S(x) =

![image 321](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile321.png>)

1+i/x

1+i/x

eπiτ − e−Nπiτ eπiτ − 1

e−xπiτ sin πτ2

1 2

i 4

dτ.

F(τ)

F(τ)

dτ =

![image 322](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile322.png>)

![image 323](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile323.png>)

![image 324](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile324.png>)

![image 325](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile325.png>)

−1+i/x

−1+i/x

![image 326](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile326.png>)

πiτ

(The integral − 1+1+i/xi/x F(τ)e

1+i/x

−1+i/x F(τ)eπimτdτ clearly vanishes.) Note that

eπiτ−1 dτ = − m≥1

![image 327](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile327.png>)

1 sin πτ2 = πτ2 + O(τ) for τ ∈ [−1 + i/x, 1 + i/x], and integrating the O(τ) term gives an error of the order at most O(xk/2 log2x) as in the proof of Proposition 6.3.

![image 328](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile328.png>)

![image 329](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile329.png>)

![image 330](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile330.png>)

After applying the identity (3.13) to the part of the integral with πτ2 we are left with

![image 331](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile331.png>)

i+1/x

eπxr r

- 1

![image 332](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile332.png>)

- 2πi


(±F(i/r)r−k + r−s ∓ rs−k)

dr.

![image 333](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile333.png>)

−i+1/x

By inverse Laplace transform we have

- (6.6)


- 1

![image 334](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile334.png>)

- 2πi


i∞+1/x

(πx)α Γ(α + 1)

eπxr rα+1

dr =

,

![image 335](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile335.png>)

![image 336](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile336.png>)

−i∞+1/x

and thus

i+1/x

(πx)k−s Γ(k − s + 1)

(πx)s Γ(s + 1) ∓

1 2πi

(r−s ∓ rs−k)eπxrr−1dr =

+ O(1). Thus it remains to estimate

![image 337](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile337.png>)

![image 338](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile338.png>)

![image 339](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile339.png>)

−i+1/x

1

tx2 + ix 1 + t2x2

eπ 2π

(it + 1/x)−k−1eπxitdt.

±

F

![image 340](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile340.png>)

![image 341](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile341.png>)

−1

We split this integral into two parts: |t| ≤ 2√1x and 1 ≥ |t| ≥ 2√1x. To estimate the integral for |t| ≤ 2√1x we plug in the Fourier expansion of F. By (6.6) the constant term gives a contribution of

![image 342](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile342.png>)

![image 343](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile343.png>)

![image 344](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile344.png>)

![image 345](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile345.png>)

![image 346](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile346.png>)

![image 347](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile347.png>)

(πx)k Γ(k + 1)

±α0±,k(s)

+ O(xk/2). The rest of the terms are αn,k± (s)In, where

![image 348](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile348.png>)

- 1

![image 349](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile349.png>)

- 2√x


exp −πnx + πintx2 1 + t2x2

eπ 2π

![image 350](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile350.png>)

(it + 1/x)−k−1eπxitdt.

In := ±

![image 351](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile351.png>)

![image 352](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile352.png>)

−2√1x

![image 353](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile353.png>)

![image 354](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile354.png>)

We claim that In ≪ e−πnx(k−1)/2 when x ≥ 16, say. To see this, we begin by observing that, by symmetry and a trivial estimate, it suﬃces to consider

- (6.7) Jn :=


- 1

![image 355](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile355.png>)

- 2√x


exp −πnx + πintx2 1 + t2x2

![image 356](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile356.png>)

![image 357](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile357.png>)

2 x

![image 358](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile358.png>)

(it + 1/x)−k−1eπxitdt

and show that Jn ≪ e−πnx(k−1)/2. To this end, we set B(t) := exp −πnx

1 + t2x2 |it + 1/x|−k−1, A(t) :=

![image 359](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile359.png>)

πntx2 1 + t2x2

+ πxt − (k + 1) Imlog(it + 1/x), so that the integrand in (6.7) can be written as B(t) exp(iA(t)). We observe that

![image 360](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile360.png>)

B(t) ≪ e−πnx−(k+1)/2 uniformly for |t| ≤ 1/(2√x). Moreover,

![image 361](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile361.png>)

πn(1/x2 − t2) (1/x2 + t2)2

i(k + 1) it + 1/x ≪ nx

A′(t) =

+ πx − Im

![image 362](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile362.png>)

![image 363](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile363.png>)

uniformly for 2/x ≤ t ≤ 1/(2√x). A calculus argument shows that B(t)/A′(t) is a decreasing function on that interval, whence a classical bound for oscillatory integrals [29, Lem. 4.3] yields the asserted bound

![image 364](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile364.png>)

B(t) |A′(t)|

≪ e−πnx(k−1)/2. Summing this over all n ≥ 1, we obtain the asserted contribution O(x(k−1)/2).

Jn ≪ max

2/x≤t≤1/(2√x)

![image 365](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile365.png>)

![image 366](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile366.png>)

√x + 1/2. Using the change of variables t  → 2n1+t which sends [−1, 1] to [2n1+1, 2n1−1], and noting that

Finally, we split the integral over |t| ≥ 2√1x into intervals [2n1+1, 2n1−1], n ≤

![image 367](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile367.png>)

![image 368](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile368.png>)

![image 369](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile369.png>)

![image 370](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile370.png>)

![image 371](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile371.png>)

![image 372](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile372.png>)

![image 373](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile373.png>)

![image 374](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile374.png>)

(2n+t)−1x2+ix

1+(2n+t)−2x2 is very close to 2n + t + 4nx2i, we get

![image 375](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile375.png>)

![image 376](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile376.png>)

1

n−1 ≪ xk/2 log3x.

|F(t + 4n2i/x)|dt ≪k xk/2 log2x

nk−1

≪

√x+1

√x+1

|t|≥2√1x

−1

![image 377](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile377.png>)

n≤

n≤

![image 378](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile378.png>)

![image 379](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile379.png>)

![image 380](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile380.png>)

This concludes the proof.

- 6.4. Estimate for I(τ).


- Proposition 6.6. For 0 < y < 1/2 we have


 

1 α ∈ (0, 1), log(y−1) α = 1, y1−α α > 1.

1

I(x + iy)αdx ≪α

- (6.8)




−1

Proof. Fix y = N−1. Since Im aτcτ++db = |cτIm+τd|

and γ(τ) ∈ F if and only if Imγ(τ) is maximal among all γ ∈ Γθ, we see that

![image 381](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile381.png>)

![image 382](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile382.png>)

2

y (cx − d)2 + c2y2

I(x) := I(x + iy) = max

(c, d) = 1, 2|cd .

![image 383](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile383.png>)

Without loss of generality we only consider (c, d) with c > 0. Note that N−1 ≤ I(x) ≤ N for all x ∈ [−1, 1]. Let I(x) ≥ T > 2. Therefore (cx − d)2 + c2N−2 ≤ N−1T−1 for some c, d

![image 384](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile384.png>)

with c > 0, which implies c ≤ N/T and |x − d/c| ≤ c√1NT . If (c′, d′) is a diﬀerent pair with c′ ≤ N/T such that |x − d′/c′| ≤ c 1

![image 385](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile385.png>)

![image 386](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile386.png>)

![image 387](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile387.png>)

NT , then 1

′√

![image 388](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile388.png>)

![image 389](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile389.png>)

1 c

1 c′

2 cc′T

cc′ ≤ |d/c − d′/c′| ≤

√

√

NT ≤

,

+

![image 390](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile390.png>)

![image 391](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile391.png>)

![image 392](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile392.png>)

![image 393](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile393.png>)

![image 394](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile394.png>)

![image 395](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile395.png>)

NT

which is impossible. Hence the above inequality can hold only for one pair (c, d) with c ≤ N/T. Conversely, if |x − d/c| ≤ c√1NT and c ≤ N/T, then I(x) ≥ T/2. Let us denote

![image 396](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile396.png>)

![image 397](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile397.png>)

![image 398](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile398.png>)

![image 399](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile399.png>)

2ϕ(c) c

2 √

,

u(T) :=

![image 400](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile400.png>)

![image 401](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile401.png>)

![image 402](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile402.png>)

√

NT

![image 403](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile403.png>)

c≤

N/T

where ϕ is Euler’s totient function. Then a simple estimate shows that u(T) ≤ 4/T for T < N. Moreover, for T > 2 the measure of the set I−1([T, N]) belongs to the interval [u(2T), u(T)]. From this we see that for k ≥ 1

µ(I−1([2k, 2k+1])) ≤ u(2k) ≤ 22−k, so that 1

2(α−1)k + 21+α,

Iα(x)dx ≤ 22+α

−1

k≤log2(N)

which immediately implies (6.8).

6.5. Estimate for N(τ).

- Proposition 6.7. We have


1

2 π2

log2 y + O(log y), y → 0.

N(x + iy)dx =

![image 404](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile404.png>)

−1

Corollary 6.1. For y ∈ (0, 1) we have

1

N(x + iy)αdx ≪ log2α(1 + y−1), 0 < α ≤ 1,

−1

1

N(x + iy)αdx ≪α y1−α log2(1 + y−1), α > 1.

−1

Proof. For 0 < α ≤ 1 the claim follows from Proposition 6.7 by H¨older’s inequality. Since N(x + iy) ≪ 1 + y−1, for α > 1 we have

1

1

N(x + iy)dx ≪ (y/2)1−α log2(1 + y−1),

Nα(x + iy)dx ≪ (1 + y−1)α−1

−1

−1

from which we obtain the second claim.

- Proof of Proposition 6.7. We set Uj := {τ : |τ| < 1, N(τ) ≥ j + 1}. From the deﬁnition of N(τ) it follows that U1 = D = {τ ∈ H: |τ| < 1}. Moreover, from the description of the greedy algorithm for computing γτ, we have N(τ) = N(−1/τ) + 1 for |τ| < 1, which leads to the recursion Uj+1 = n =0 ST2nUj. This implies that


ST2n

. . .ST2n

Uj+1 =

D, j ≥ 0.

j

1

n1,...,nj =0

By the deﬁnition of Uj, we have

1γ(D)(τ), |τ| < 1,

- (6.9) N(τ) = 1 +


(τ) = 1 +

1U

j

j≥1

γ∈C

where C denotes the set of all elements of the form γ = ST2n

. . .ST2n

for j ≥ 0 with n1, . . ., nj = 0.

j

1

Note that the preimage (in Γθ) of (c, d) under the map ( ac db )  −→r (c, d) is the coset T2Z( ac db ). Any such coset contains exactly one element of the form ST2n

. . .ST2n

Sδ. A simple

j

1

inductive argument shows that if ( ac db ) ∈ C, then |c| < |d|, and if ( ac db ) ∈ CS, then |c| > |d|. Thus r provides a bijection between C and the set N of all pairs (c, d) with |c| < |d|,

gcd(c, d) = 1, and c  ≡ d (mod 2), modulo the equivalence relation (c, d) ∼ (−c, −d). Deﬁne Φ(y) := − 11 N(x + iy)dx and for Res > 1 consider

∞

(Φ(y) − 2)ys−1dy.

Ψ(s) :=

0

For γ = ( ac db ) ∈ Γθ, γ(D) is a half-disk with endpoints γ(±1) and radius 21|γ(1)−γ(−1)| = |c2 − d2|−1. An elementary calculation then shows that for γ = ( ac db ) we have

![image 405](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile405.png>)

∞

1

Γ(s/2)Γ(3/2) Γ((s + 3)/2)

1γ(D)(x + iy)ys−1dydx = |c2 − d2|−s−1

.

![image 406](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile406.png>)

−1

0

Combined with (6.9) and the above description of C we get

ζodd2 (s + 1) ζodd(2s + 2)

Γ(s/2)Γ(3/2) Γ((s + 3)/2)

Γ(s/2)Γ(3/2) Γ((s + 3)/2)

|c2 − d2|−s−1 =

Ψ(s) =

,

![image 407](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile407.png>)

![image 408](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile408.png>)

![image 409](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile409.png>)

(c,d)∈N

where ζodd(s) = n≥1(2n − 1)−s. To obtain this identity we have used the bijection (c, d)  → (c − d, c + d) between N and the set of all pairs of coprime odd integers (m, n) with opposite signs, again modulo (m, n) ∼ (−m, −n). The function Ψ(s) is meromorphic in the half-plane Res > −1/2 with the only singularity at s = 0 with principal part

c2 s2

c1 s

4 π2s3

+ O(1), s → 0

+

+

Ψ(s) =

![image 410](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile410.png>)

![image 411](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile411.png>)

![image 412](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile412.png>)

for some c1, c2 ∈ R. Since |Ψ(u + iv)| ≪u |v|−5/4 for u > −1/2, by a standard application of the inverse Mellin transform we obtain

Φ(y) = 2π−2 log2 y − c2 log y + c1 + 2 + Oε(y1/2−ε), y → 0. The constants c1, c2 are explicit, albeit complicated, for instance,

12 + 4 log 2 − 24 log π − 288ζ′(−1) 3π2

c2 =

= 1.180066... .

![image 413](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile413.png>)

7. The Fourier interpolation basis of Theorem A revisited

It was shown in [25, Prop. 4] that (1.4) holds if one assumes f(x), f(x) ≪ (1 + |x|)−13. Using the estimates from Section 6.2 we may now weaken these constraints.

Theorem 7.1. Suppose f is an even integrable function on R such that also f is integrable. Suppose also that both f and f are absolutely continuous and that the two integrability conditions

∞

- (7.1) |f′(x)|(1 + |x|)1/2 log3(e + |x|)dx < ∞,


−∞ ∞

|( f)′(ξ)|(1 + |ξ|)1/2 log3(e + |ξ|)dξ < ∞

−∞

hold. Then we may represent f as in (1.4) for every real x, with the two series in (1.4) being in general only conditionally convergent.

The proof of this theorem relies on the following proposition.

Proposition 7.1. For x > 0 and N ≥ 1 we have

- (7.2)

n≤N

b±n(x) = ±2b±0 (x)N1/2 + O(N1/4 log3N) + O(min(x−1/2N1/4, N1/2)),

where b±n are deﬁned by (3.16) and the implied constants in the O terms are absolute.

The proposition remains true when x = 0, but in that case it is better to use the two expressions

- (7.3)

N

n=1

b−n(0) = 0 and

N

n=1

b+n (0) = −2N1/2 + O(1),

which are obvious consequences of the facts that b−n (0) = 0 for all n ≥ 1 and b+n(0) = −2 if n is a square and otherwise b+n (0) = 0.

Proof of Proposition 7.1. From [25, Prop. 2] it follows that that F(τ) = n≥0 b±n (x)eπinτ is of moderate growth and

- (7.4) F(τ) ∓ (τ/i)−1/2F(−1/τ) = eπix

2τ ∓ (τ/i)−1/2eπix

2(−1/τ).

Therefore, we have F(τ) = F1±/2(τ, ϕ), where ϕ(τ) = eπix2τ. Since ϕ(τ) is bounded for |τ| ≥ 1/2, Proposition 6.2 implies that (6.4) holds for k = 1/2 and hence

|b±n(x)| ≪ n1/4(1 + log2 n).

Then we repeat the argument from the proof of Proposition 6.5, the only diﬀerence being that after applying (7.4) we get, along with the two ﬁrst terms on the right-hand side of (7.2), the term

- (7.5)

- 1

![image 414](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile414.png>)

- 2πi


i+1/N

−i+1/N

(e−πx

2r ± r−1/2e−πx

2/r)

eπNr r

![image 415](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile415.png>)

dr .

The ﬁrst term in the integrand in (7.5) yields trivially a contribution that is O(log N), and this can be absorbed in the ﬁrst O term in (7.2). We estimate the contribution from the second term in the integrand of (7.5) trivially if x ≤ N−1/2 and see that we then get a term that is O(N1/2). When x ≥ N−1/2, we estimate the contribution to the integral from the interval | Imr| ≤ max(1, 2xN−1/2) trivially and use again the bound for oscillatory integrals from [29, Lem. 4.3] to deal with the remaining part. We obtain then a term that is O(x−1/2N1/4) which yields the latter O term in (7.2).

Proof of Theorem 7.1. We begin by showing that the two series in (1.4) converge. By symmetry, it suﬃces to consider the ﬁrst of them. By partial summation, we ﬁnd that

- (7.6)

N

n=K+1

f(√n)an(x) = f(

![image 416](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile416.png>)

√

![image 417](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile417.png>)

N)A(N) − f(

√

![image 418](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile418.png>)

K)A(K) −

N

K

f′(√y)

![image 419](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile419.png>)

- 1

![image 420](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile420.png>)

- 2√y


![image 421](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile421.png>)

A(y)dy,

where A(N) := n≤N an(x). By Proposition 7.1 and the relation an(x) = (b+n(x)+b−n (x))/2, we have

- (7.7) A(y) = −b−0 (0)y1/2 + O(y1/4 log3y)


when y = 0, but in view of (7.3), this is also true for y = 0. Since the ﬁrst term on the right-hand side of (7.7) is smooth, we may now use integration by parts in (7.6) along with a change of variables to deduce that

N

√

√

f(√n) an(x) ≪ |f(

![image 422](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile422.png>)

![image 423](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile423.png>)

- (7.8) K)|K1/4 log3K

+

√

![image 424](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile424.png>)

N √

![image 425](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile425.png>)

K

|f(y)|dy +

√

![image 426](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile426.png>)

N √

![image 427](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile427.png>)

K

|f′(y)| y1/2 log3y dy.

The ﬁrst two terms on the right-hand side of (7.8) tend to 0 when K, N → ∞ because

f(y) = −

∞

y

D f(ξ)dξ ≪ y−1/2 log−3y

∞

y

|D f(ξ)|(1 + |ξ|)1/2 log3(e + |ξ|)dξ.

Here the integral to the right tends to 0 when y → ∞ in view of (7.1). The two integrals on the right-hand side of (7.8) also tend to 0 when K, N → ∞ by the respective integrability conditions on f and f′.

We now turn to the proof that equality holds in (1.4). To this end, we follow the proof of [25, Prop. 4]. We write

RMf(x) := M1/2e−πx

2/M

∞

−∞

f(x − y)e−πMy

2

dy

and

RMf(x) := M1/2

∞

−∞

f(x − y)e−π(x−y)

2/M−πMy2dy.

It is plain that RMf(x) → f(x) when M → ∞, and hence it suﬃces to prove that

∞

n=0

RMf(√n) − f(√n) an(x) → 0 and

![image 428](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile428.png>)

![image 429](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile429.png>)

∞

n=0

RMf(√n) − f(√n) an(x) → 0

![image 430](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile430.png>)

![image 431](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile431.png>)

when M → ∞. We consider only the latter convergence, as the two cases are almost identical. For convenience, we write

∆Mf(y) := RMf(y) − f(y) and Dg := g′.

By the same argument of partial summation and integration as used in the ﬁrst part of the proof, we ﬁnd that

- (7.9)


N)|N1/4 log3N + |f(

![image 432](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile432.png>)

n=K+1

∞

∞

∞

∆Mf(√n) an(x) ≪

|D ∆Mf(y)| (1 + y)1/2 log3(e + y)dy.

![image 433](<2020-bondarenko-fourier-interpolation-zeros-zeta_images/imageFile433.png>)

| ∆Mf(y)|dy +

1

1

n=1

A routine argument, using that f is integrable, shows that the ﬁrst integral on the righthand side of (7.9) tends to 0 when M → ∞. To deal with the second integral, we write

∞

2

D f(y − v) − D f(y) e−πMv

D ∆Mf(y) = M1/2

dv

−∞

∞

2/M − 1 e−πMv

2

D f(y − v) e−π(y−v)

+ M1/2

dv

−∞

∞

2/Me−πMv

2

f(y − v)2π(y − v)M−1e−π(y−v)

+ M1/2

- (7.10) dv


−∞

and apply again routine arguments, along with our integrability assumptions on f and D f, to show that each of the corresponding three terms tends to 0 when M → ∞. We give the details only for the last term in (7.10). To this end, it suﬃces to observe that

(1 + y)1/2 log3(e + y) ≪ |y − v|δ + |v|δ for some δ, 1/2 < δ < 1, so that

∞

∞

2/Me−πMv

2

dv (1 + y)1/2 log3(e + y)dy

f(y − v)2π(y − v)M−1e−π(y−v)

M1/2

−∞

1

∞

∞

2

2

e−πMv

|v|δe−πMv

≪ Mδ/2

dv +

dv f 1, and the latter term tends to 0 when M → ∞ since δ < 1.

−∞

−∞

As was observed in the introduction, formula (1.4) reduces to the Poisson summation formula when x = 0 in view of (1.5). Since we have the more precise formula (7.3) (instead of (7.7)) in that case, the above proof therefore shows that the Poisson summation formula is valid when f, f′, f, ( f)′ are all integrable. Somewhat related and reﬁned conditions can be found in the work of Kahane and Lemari´e-Rieusset [12]. See also Gro¨chenig’s paper [8], where it is shown that the Poisson summation formula holds for functions in the Feichtinger algebra.

On the other hand, by a classical example of Katznelson [14], there exist functions f with both f and f in L1 for which the Poisson summation formula fails. This shows that we need indeed an additional assumption, beyond integrability of f and f, for the Fourier interpolation formula (1.4) to hold for every real x.

References

- [1] T. Asai, M. Kaneko, and H. Ninomiya, Zeros of certain modular functions and an application, Comment. Math. Univ. St. Paul. 46 (1) (1997), 93–101.
- [2] B.C. Berndt and M.I. Knopp, Hecke’s theory of modular forms and Dirichlet series, World Scientiﬁc, Singapore, 2008.
- [3] S. Bochner, Some properties of modular relations, Ann. of Math. 53 (2) (1951), 332–363.
- [4] H. Davenport, Multiplicative Number Theory, Third edition, Revised and with a preface by Hugh L. Montgomery, Graduate Texts in Mathematics 74, Springer-Verlag, New York, 2000.


- [5] W. Duke, O.¨ Imamog¯lu, and A.´ T´th, Cycle integrals of the j-function and mock modular forms, Ann. of Math. 173 (2) (2011), 947–981.
- [6] F. Dyson, Birds and frogs, Notices Amer. Math. Soc. 56 (2009), 212–223.
- [7] M. Eichler, The basis problem for modular forms and the traces of the Hecke operators, in Modular Functions of One Variable I. LNM 320, 75–152, Berlin-Heidelberg-New York: Springer, 1973.
- [8] K. Gr¨ochenig, An uncertainty principle related to the Poisson summation formula, Studia Math. 121 (1996), 87–104.
- [9] A. Guinand, Concordance and the harmonic analysis of sequences, Acta Math. 101 (1959), 235– 271.
- [10] D. R. Heath-Brown, Hybrid bounds for Dirichlet L-functions, Invent. Math. 47 (1978), 149–170.
- [11] H. Hedenmalm, A. Montes-Rodriguez, Heisenberg uniqueness pairs and the Klein-Gordon equation, Ann. of Math. 173 (2) (2011), 1507–1527.
- [12] J.-P. Kahane and P.-G. Lemari´e-Rieusset, Remarques sur la formule sommatoire de Poisson, Studia Math. 109 (1994), 303–316.
- [13] S. Karnik, J. Romberg, and M. A. Davenport, Improved bounds for the eigenvalues of prolate spheroidal wave functions and discrete prolate spheroidal sequences, Appl. Comp. Harm. Anal. 55

(2021), 97–128.

- [14] Y. Katznelson, Une remarque concernant la formule de Poisson, Studia Math. 29 (1967), 107–108.
- [15] M. Knopp, Some new results on the Eichler cohomology of automorphic forms. Bull. Amer. Math. Soc. 80 (1974), 607–632.
- [16] M. Knopp, On the growth of entire automorphic integrals, Result. Math. 8 (1985), 146–152.
- [17] M. Knopp, Modular Functions in Analytic Number Theory, Second edition, AMS Chelsea Publishing, 1993.
- [18] M. Knopp, On Dirichlet series satisfying Riemann’s functional equation, Invent. Math. 117 (1994), 361–372.
- [19] M. Knopp, Hamburger’s theorem on ζ(s) and the abundance principle for Dirichlet series with functional equations, Number theory, Trends Math., Birkh¨user, Basel, 2000, 201–216.
- [20] A. Kulikov, Fourier interpolation and time-frequency localization, J. Fourier Anal. Appl. 27 (2021), Article No. 58.
- [21] P. Kurasov and P. Sarnak, Stable polynomials and crystalline measures, J. Math. Phys. 61 (2020), no. 8, 083501, 13 pp.
- [22] N. Lev and A. Olevskii, Quasicrystals and Poisson’s summation formula, Invent. Math. 200

(2015), 585–606.

- [23] Y. Meyer, Measures with locally ﬁnite support and spectrum, Proc. Natl. Acad. Sci. USA 113

(2016), 3152–3158.

- [24] D. Mumford, Tata Lectures on Theta: Jacobian theta functions and diﬀerential equations, Progress in mathematics, Birkh¨user, 1983.
- [25] D. Radchenko and M. Viazovska, Fourier interpolation on the real line, Publ. Math. Inst. Hautes Etudes´ Sci. 129 (2019), 51–81.
- [26] K. Ramachandra and A. Sankaranarayanan, Notes on the Riemann zeta-function, J. Indian Math. Soc.(N.S.) 57 (1991), 67–77.
- [27] D. Slepian, Some comments on Fourier analysis, uncertainty and modeling, SIAM Rev. 25 (1983), 379–393.
- [28] E. C. Titchmarsh, The Theory of Functions, Second edition, Oxford University Press, Oxford, 1939.
- [29] E. C. Titchmarsh, The Theory of the Riemann Zeta-Function, Second edition, Edited and with a preface by D. R. Heath-Brown, Oxford University Press, New York, 1986.
- [30] A. Weil, Sur les “formules explicites” de la the´orie des nombres premiers, Comm. S´em. Math. Univ. Lund [Medd. Lunds Univ. Mat. Sem.] 1952, Tome Suppl´ementaire, pp. 252–265.


- [31] D. Zagier, Traces of singular moduli, in Motives, Polylogarithms and Hodge Theory, Part I, International Press Lecture Series, 2002, 211–244.
- [32] D. Zagier, The Mellin transform and other useful analytic techniques, Appendix to E. Zeidler, Quantum Field Theory I: Basics in Mathematics and Physics. A Bridge Between Mathematicians and Physicists, Springer-Verlag, Berlin-Heidelberg-New York (2006), 305–323.


Department of Mathematical Sciences, Norwegian University of Science and Technol-

ogy, NO-7491 Trondheim, Norway Email address: andriybond@gmail.com ETH Zurich, Mathematics Department, Zurich¨ 8092, Switzerland Email address: danradchenko@gmail.com Department of Mathematical Sciences, Norwegian University of Science and Technol-

ogy, NO-7491 Trondheim, Norway Email address: kristian.seip@ntnu.no

