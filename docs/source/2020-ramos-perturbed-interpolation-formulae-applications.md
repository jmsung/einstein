---
type: source
kind: paper
title: Perturbed interpolation formulae and applications
authors: João P. G. Ramos, Mateus Sousa
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2005.10337v1
source_local: ../raw/2020-ramos-perturbed-interpolation-formulae-applications.pdf
topic: general-knowledge
cites:
---

arXiv:2005.10337v1[math.CA]20May2020

PERTURBED INTERPOLATION FORMULAE AND APPLICATIONS

JOAO˜ P. G. RAMOS AND MATEUS SOUSA

Abstract. We employ functional analysis techniques in order to deduce that some classical and recent interpolation results in Fourier analysis can be suitably perturbed. As an application of our techniques, we obtain generalizations of Kadec’s 1/4−theorem for interpolation formulae in the Paley–Wiener space both in the real and complex case, as well as a perturbation result on the recent Radchenko– Viazovska interpolation result [24] and the Cohn–Kumar–Miller–Radchenko–Viazovska [10] result for Fourier interpolation with derivatives in dimensions 8 and 24. We also provide several applications of the main results and techniques, all relating to recent contributions in interpolation formulae and uniqueness sets for the Fourier transform.

Contents

- 1. Introduction 1
- 2. Preliminaries 9
- 3. Perturbed Interpolation Formulae for Band-Limited functions 13
- 4. Perturbations of Fourier interpolation on the real line 22
- 5. Applications of the main results and techniques 37
- 6. Comments and Remarks 50 Acknowledgements 52 References 52


1. Introduction

- A fundamental question in analysis is that of how to recover a function f from


some subset {f(x)}x∈A of its values, together with some information on its Fourier transform f : R → C, which we deﬁne to be

- (1.1) f(ξ) = R

f(x)e−2πixξ dx.

The perhaps most classical result in that regard is the Shannon–Whittaker interpolation formula: if f is supported on an interval [−δ/2,δ/2], then

- (1.2) f(x) =


∞

f(k/δ)sinc(δx − k),

k=−∞

where convergence holds both in L2(R) and uniformly, where we let sinc(x) = sin(πxπx). In spite of this classical formula, a major recent breakthrough in regard to the problem

![image 1](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile1.png>)

of determining which conditions on the sets A,B ⊂ R imply that a function f ∈ S(R) is uniquely determined by its values at A and the values of its Fourier transform at B

1

was made by Radchenko and Viazovska [24], where the authors prove that, whenever f : R → R is even and Schwartz, then

- (1.3) f(x) =

∞

k=0

f(

√

![image 2](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile2.png>)

k)ak(x) +

∞

k=0

f(

√

![image 3](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile3.png>)

k) ak(x).

Radchenko and Viazovska’s result and its techniques were somewhat inspired by Viazovska’s recent solution to the sphere packing problem in dimension 8 [31], and her subsequent work with Cohn, Kumar, Miller and Radchenko to solve the same problem in dimension 24 [9], as they include the usage of modular forms in order to construct some special functions with particular properties at the desired nodes of interpolation.

Subsequently to the Radchenko–Viazovska result, other recent works have successfully used a similar approach in order to construct interpolation and uniqueness formulae. Among those, we mention the following:

(1) In [8], Cohn and Gonc¸alves use a modular form construction in order to obtain that there are cj > 0, j ∈ N, so that, for each f ∈ Srad(R12) real,

- (1.4) f(0) − j≥1


![image 4](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile4.png>)

![image 5](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile5.png>)

cjf( 2j) = − f(0) +

cj f( 2j).

j≥1

Such a formula enables the authors to prove a sharp version of a root uncertainty principle ﬁrst raised by Bourgain, Clozel and Kahane [4] in dimension 12; see, e.g., [15, 13, 14] and the references therein for more information on this topic;

- (2) On the other hand, in [10], Cohn, Kumar, Miller, Radchenko and Viazovska develop upon the basic ideas of [24] to be able to prove universal optimality

results about the E8 and Leech lattices in dimensions 8 and 24, respectively. In order to do so, they prove interpolation formulae in such dimensions that involve the values of f(√2n),f′(√2n), f(√2n), f′(√2n), where f is a radial, Schwartz function, and n ≥ n0, with n0 = 1 if d = 8, and n0 = 2 in case d = 24;

![image 6](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile6.png>)

![image 7](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile7.png>)

![image 8](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile8.png>)

![image 9](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile9.png>)

- (3) Finally, more recently, other developments in the theory of interpolation formulae given values on both Fourier and spatial side has been made by Stoller [29], who considered the problem of recovering any funtion in Rd from its restrictions and the restrictions of its Fourier transforms to spheres of radii √n, n > 0, for any d > 0. Moreover, we mention also the more recent work of Bondarendo, Radchenko and Seip [3], which generalizes Radchenko and Viazovska’s construction of the interpolating functions to prove interpolation formulae for some classes of functions f that take into account the values of f at log n/4π, and the values of f at a sequence (ρ −1/2)/i, where ρ ranges over non-trivial zeros of some L−function with positive imaginary part.


![image 10](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile10.png>)

One fundamental point to stress is that, in a suitable way, all the previously mentioned results are related to some sort of summation formula, the most basic instance

of such being the classical Poisson summation formula

f(n),

f(m) =

m∈Z

n∈Z

which is a particular case, for instance, of (1.3) in case we set x = 0. Clearly, the formula (1.4) is also a manifestation of such a principle that implies rigidity between certain values of f and other values of f.

In that regard, these topics can be inserted into the framework of crystalline measures. Indeed, if we adopt the classical deﬁnition of a crystalline measure to be a distribution with locally ﬁnite support, such that its Fourier transform possesses the same support property, we will see that the Poisson summation formula implies, for instance, that the measure δZ is not only a crystalline measure, but also self-dual, in the sense that δZ = δZ holds in S′(R).

Outside the scope of interpolation formulae per se, we mention the works [18, 19, 22], where the authors explore in a deeper lever structural questions on crystalline measures. In particular, in [22], Meyer exhibits examples of crystalline measures with selfduality properties, and uses modular forms to construct explicity examples of non-zero self-dual crystalline measures µ supported on {±

√k + a,k ∈ Z}, for a ∈ {9,24,72}. We also mention the recent work of Kurasov and Sarnak [17], where the authors, as a by-product of investigations of the additive structure of the spectrum of metric graphs, prove that there are exotic examples of positive crystalline measures other than generalized Dirac combs.

![image 11](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile11.png>)

Our investigation in this paper focuses on both classical and modern results in the theory of such interpolation formulae and crystalline measures. In generic terms, we are interested in determining when, given an interpolation formula such as (1.2) or

- (1.3), we can perturb it suitably. That is, given a sequence of real numbers {εk}k∈Z, under which conditions can we recover f from the values


- (1.5) {(f(sn + εn), f( sn + εn))}n∈Z,


given that we can recover f from {(f(sn), f( sn))}n∈Z?

In this manuscript, the main ideia is to study such perturbations of interpolation formulae for band-limited and Schwartz functions through functional analysis. Indeed, most of our considerations are based oﬀ the idea that, whenever an operator T : B →

- B, where B is a Banach space, satisﬁes that T − I B→B < 1,


then T is, in fact, a bijection with continuous inverse T−1 : B → B. In fact, in all our considerations on interpolation formulae below, some form of this principle will be employed, and even the importance of other proofs and results in the paper, such as Theorem 1.5, arise naturally when trying to employ this principle to diﬀerent contexts.

- 1.1. Perturbations and Interpolation formulae in the band-limited case. The question of when we are able to recover the values of a function such that its Fourier transform is supported in [−1/2,1/2] from its values at n + εn is well-known, having


been asked by Paley and Wiener [23], where the authors prove that recovery – and also an associated interpolation formula – is possible as long as supn |εn| < π−2. Many results relate to the original problem of Paley and Wiener, but the most celebrated of

- them all is the so-called Kadec-1/4 theorem, which states that, as long as supn |εn| < 41,

![image 12](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile12.png>)

- then one can recover any f ∈ L2(R) which has Fourier support on [−1/2,1/2] from its

values at n+εn, n ∈ Z.; see [16] for Kadec’s original proof and [1] for a generalization.

Our ﬁrst results provide one with a simpler proof of a particular range of Kadec’s result.

- Theorem 1.1. Let {εk}k∈Z be a sequence of real numbers and consider L = supk |εk|. If L < 1/2 and


1 −

sin(πL) πL

![image 13](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile13.png>)

+

π 3

![image 14](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile14.png>)

LsinπL 1 − L

![image 15](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile15.png>)

+ sin πL < 1,

then any function f ∈ PWπ is completely determined by its values {f(n+εn)}n∈Z, and there is C = C(L) > 0 such that

1 C n∈Z|f(n + εn)|2 ≤ f 22 ≤ C

![image 16](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile16.png>)

n∈Z

|f(n + εn)|2,

for all f ∈ PWπ.

Moreover, there are functions gn ∈ PWπ(R) such that for every f ∈ PWπ, the following identity holds:

f(x) =

n∈Z

f(n + εn)gn(x),

where the right-hand side converges absolutely.

The condition in Theorem 1.1 is satisﬁed for L < 0.239, which possesses only a 0.011 gap to Kadec’s result. The main diﬀerence, however, that while Kadec’s proof relies on a clever expansion of the underlying functions in a diﬀerent orthonormal basis, we have almost not used orthogonality in our considerations. We have, nonetheless, chosen not

- to pursue the path of exploring orthogonality in this question much deeper in order not to make the exposition longer.


We must also remark that, in the proof of such a result, one can use complex numbers for perturbations. The diﬀerence is that we have to take into account the sine of complex numbers, and the result would be L < 0.2125 instead of L < 0.239. This only falls very mildly short of the results in [1, Theorem 3], where L < 0.218 is achieved in the complex setting, and our methods of proof are relatively simpler in comparison to those of [1], where the authors must enter the realm of Lamb-Oseen functions and constants. Also, we do not make any use of the orthogonality, which could be exploited to improve on the current result.

As another application of the idea of inverting an operator, we mention a couple of results related to Vaaler’s interpolation formula. In [30], J. Vaaler proved, as means to study extremal problems in Fourier analysis, the following counterpart to the Shannon– Whittaker interpolation formula: let f ∈ L2(R), and suppose that f is supported on

[−1,1]. Then

sin2(πx) π2 k∈Z

f′(k) x − k

f(k) (x − k)2

+

.

- (1.6) f(x) =


![image 17](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile17.png>)

![image 18](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile18.png>)

![image 19](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile19.png>)

This can be seen as a natural tradeoﬀ: (1.2) demands that we have information at 21Z in order to recover the functions f as stated above. On the other hand, Vaaler’s result

![image 20](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile20.png>)

only demands information at Z, but one must pay the price of also providing it for the derivative.

The ﬁrst result concerning (1.6) is a direct deduction of its validity from the Shannon– Whittaker formula (1.2). We state it, for completeness, in the following form.

- Theorem 1.2. Fix a sequence {ak}k∈Z ∈ ℓ2(Z). Consider the function f ∈ PWπ given by

f(x) =

n∈Z

ansinc(x − n), for each x ∈ R. Then the interpolation formula f(x) =

4sin2(21πx) π2 j∈Z

![image 21](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile21.png>)

![image 22](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile22.png>)

a2k (x − 2k)2

![image 23](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile23.png>)

+

b2k x − 2k

![image 24](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile24.png>)

holds, where the right-hand side converges uniformly on compact sets, and we let bk =

j =k

aj k − j

![image 25](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile25.png>)

(−1)k−j.

As a main diﬀerence between our proof of Theorem 1.2 and the original proof in [30] is the absence of any signiﬁcant use of the Fourier transform. Diﬀerently, however, from the de Branges spaces approach in [11], we do not delve deeply into any theory of function spaces, but rather we make use of classical operators in ℓ2(Z) such as discrete Hilbert transforms and its properties.

Our ﬁnal contribution in the realm of interpolation formulae for band-limited function is an appropriate perturbation of Vaaler’s formula (1.6). We mention that, to the best of our knowledge, this result in its present form is new. See, for instance, the remark following Corollary 2 in [11] together with [21, 27] for related discussion on sampling sequences with derivatives for PWπ.

- Theorem 1.3. Let {εk}k∈Z be a sequence of real numbers and consider L = supk |εk|. Suppose that L < 0.111. Then any function f ∈ PW2π is completely determined by its values {f(n + εn)}n∈Z and those of its derivative {f′(n + εn)}n∈Z, and there is


- C = C(L) > 0 such that


- 1


C n∈Z |f(n + εn)|2 + |f′(n + εn)|2 ≤ f 22 ≤ C

| |f(n + εn)|2 + |f′(n + εn)|2 ,

![image 26](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile26.png>)

n∈Z

for all f ∈ PW2π. Moreover, there are functions gn,hn ∈ PW2π so that, for all f ∈ PW2π, we have

f(n + εn)gn(x) + f′(n + εn)hn(x) ,

f(x) =

n∈Z

where convergence holds absolutely.

This result and its method of proof follow, essentially, the same basic ideas from Theorem 1.1 and its proof, with only an increase in technical diﬃculties, such as considering higher order analogues of the perturbed discrete Hilbert transforms we use for the proof of 1.1. We note also that these technical changes, together with the work of Littman [20], allow one to extend the perturbation results for arbitrarily many derivatives; see Theorem 6.1 for a discussion on that. In order to avoid the not so pleasant computations needed in order to prove such a result, and due to the fact that its proof follows the main ideas of the proofs of theorems 1.3 and 1.1, we omit it.

- 1.2. Perturbations of symmetric interpolation formulae. Moving on from bandlimited functions to Schwartz functions instead, we face the fundamental question of determining whether formula (1.3) is rigid for its interpolation nodes or not. In other words, a fundamental question concerns conditions when we can replace a single


interpolation node √k by a suitable perturbation of it, say √k + εk, where εk ∈ (−1,1).

![image 27](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile27.png>)

![image 28](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile28.png>)

Perhaps surprisingly, the idea of inverting an operator T when it is reasonably close to the identity still works in this context. The next result can thus be regarded as the main new feature of this paper, establishing criteria when we are allowed, not only to perturb one node in the interpolation formula, but all of them simultaneously.

- Theorem 1.4. There is δ > 0 so that, for each sequence of real numbers {εk}k≥0 such that εk ∈ (−1/2,1/2),ε0 = 0, supk≥0 |εk|(1 + k)5/4 < δ ∀ k ≥ 0, there are sequences of functions {θj}j≥0,{ηj}j≥0 with


|θj(x)| + |ηj(x)| + | θj(x)| + | ηj(x)| (1 + j)O(1)(1 + |x|)−10 and

![image 29](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile29.png>)

![image 30](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile30.png>)

f( j + εj)θj(x) + f( j + εj)ηj(x) ,

f(x) =

j≥0

for all f ∈ Seven(R) real-valued functions. In other words, we can perturb each interpolation node from

√

![image 31](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile31.png>)

![image 32](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile32.png>)

k to ∼ k + k−5/4 and still obtain a valid interpolation formula converging for all Schwartz functions. In fact, one does not striclty need that f ∈ S(R), but only that f, f decay at least as fast as (1 + |x|)−M for some suﬃciently large M ≫ 1.

As an immediate corollary of Theorem 1.4, we obtain that the continuous family of measures

θj(x) 2

δx + δ−x 2 −

δ±√

µx =

![image 33](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile33.png>)

![image 34](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile34.png>)

![image 35](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile35.png>)

j+εj

j≥0

possesses Fourier transform given by

ηj(x) 2

δ±√

µx =

j+εj,

![image 36](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile36.png>)

![image 37](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile37.png>)

j≥0

whenever {εi}i≥0 satisﬁes the hypotheses of Theorem 1.4. This follows from the fact that µx is even and real-valued, so that its distributional Fourier transform will also be

an even and real-valued distribution. Therefore, it suﬃcies to test against even, realvalued functions f, and thus Theorem 1.4 gives us the asserted equality. This provides one with a new class of nontrivial examples of crystalline measures supported on both space and frquency on basically any set of the form ±

√k + εk, |εk| ≤ δk−5/4. This, in particular, aligns well with the recent examples from [3] and [17], which indicate that crystalline measures are, if not impossible, very hard to classify.

![image 38](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile38.png>)

In order to prove Theorem 1.4, we need to ﬁnd a suitable space to use the idea of inverting operators close to the identity. It turns out that, in analogy to Sobolev spaces, the weighted spaces ℓ2s(N) of sequences square summable against ns are natural candidates to work with, as it is well suited to accommodate the sequence

![image 39](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile39.png>)

![image 40](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile40.png>)

{(f( k + εk), f( k + εk))}k≥0 whenever f, f decay suﬃciently fast. In order to prove some perturbation result – that is, a weaker version of Theorem 1.4 –, using the spaces ℓ2s(N) together with the polynomial growth bounds on {an}n≥0 from (1.3) is already enough.

On the other hand, the fact that me may push the perturbations up until the k−5/4 threshold needs a suitable reﬁnement to the Radchenko–Viazovska [24] or even to the Bondarenko–Radchenko–Seip [3] bounds. The next result, thus, provides us with an additional exponential factor that mitigates growth of the interpolating functions.

- Theorem 1.5. Let b±n = an± an, where {an}n≥0 are the basis functions in (1.3). Then there is an absolute constant c > 0 such that


|x|

|b±n (x)| n1/4 log3/2(1 + n)e−c

√n,

![image 41](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile41.png>)

![image 42](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile42.png>)

|x|

|(b±n )′(x)| n3/4 log3/2(1 + n)e−c

√n,

![image 43](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile43.png>)

![image 44](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile44.png>)

for all positive integers n ∈ N.

The proof of such a result employs a mixture of the main ideas for the uniform bounds in [24] and [3], with the addition of an explicit computation of the best uniform constant bounding |x|k |b±n (x) + (b±n )′(x)| in terms of k and n. In order to obtain such a constant, we employ ideas from characterizations of Gelfand–Shilov spaces, as in [7]. Finally, with a modiﬁcation of the growth lemma for Fourier coeﬃcients of

- 2−periodic functions, we are able to obtain a slight improvement over the growth stated in Theorem 1.5. As, however, this modiﬁcation does not yield any improvement on the perturbation range stated in Theorem 1.4, we postpone a more detailed discussion about it to Corollary 4.7 below.


- 1.3. Applications. As a by-product of our method of proof for Theorem 1.4, we are able to deduce some interesting consequences in regard to some other interpolation formulae and uniqueness results.


Indeed, it is a not so diﬃcult task to adapt the ideas employed before to the contexts of interpolation formulae for odd functions. As remarked by Radchenko and Viazovska,

the following interpolation formula is available whenever f : R → R is odd and belongs to the Schwartz class:

f(√n) √n − cn(x)

f(√n) √n

f′(0) + i f′(0) 2

![image 45](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile45.png>)

![image 46](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile46.png>)

f(x) = d+0 (x)

,

+

cn(x)

![image 47](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile47.png>)

![image 48](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile48.png>)

![image 49](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile49.png>)

![image 50](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile50.png>)

![image 51](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile51.png>)

n≥1

where the interpolating sequence {ci}i≥0 possesses analogous properties to those of {ai}i≥0, and the function d+0 (x) = sin(πx

2)

sinh(πx) is odd, real and so that it vanishes together with its Fourier transform at ±

![image 52](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile52.png>)

√n, n ≥ 0.

![image 53](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile53.png>)

With our techniques, we are able to prove an analogous result to Theorems 1.5 and 1.4 for the odd interpolation formula. Also, with our techniques, we are able to perturb the Cohn–Kumar–Miller–Radchenko–Viazovska interpolation results with derivatives in dimensions 8 and 24 in a suitable range, as polynomial growth bounds for such interpolating functions are available in [10]; see theorems 5.10 and 5.12 for more details.

Another interesting application of our techniques delves a little deeper into functional analysis techniques. Indeed, in order to prove that the operator that takes the set of values {f(√k)}k≥0, { f(√k)}k≥0 to the sequences

![image 54](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile54.png>)

![image 55](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile55.png>)

![image 56](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile56.png>)

![image 57](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile57.png>)

{f( k + εk)}k≥0, { f( k + εk)}k≥0

is bounded and close to the identity on a suitable ℓ2s(N) × ℓ2s(N) space, we explore two main options, which are Schur’s test and the Hilbert–Schmidt test. Although there is no direct relation between them, Schur’s test seems to hold, in generic terms, for more operators than the Hilbert–Schmidt test, and for that reason we employ the former in our proof of Theorem 1.4. On the other hand, the Hilbert–Schmidt test has the advantage that, whenever an operator is bounded in the Hilbert–Schmidt norm, it is automatically a compact operator. This allows us to use many more tools derived from the theory of Fredholm operators, and, in particular, deduce a sort of interpolation/uniqueness result in case ε0 = 0, which is excluded by Theorem 1.4 above; see Theorem 5.3 below for such an application.

The perhaps most interesting and nontrivial application of Theorem 1.4 and its techniques is to the problem of Fourier uniqueness for powers of integers. In [25], we have proven a preliminary result on conditions on (α,β), 0 < α,β, α + β < 1, so that the only f ∈ S(R) such that

f(±nα) = f(±nβ) = 0 is f ≡ 0. In particular, we prove that, if α = β, then we can take α < 1 −

√2

![image 58](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile58.png>)

2 .

![image 59](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile59.png>)

By an approximation argument, a careful analysis involving Laplace transforms and the perturbation techniques and results above, we are able to reprove such a result for α = β in the α < 29 range in case f is real and even by a completely diﬀerent method than that in [25]. Although the current method does not yield any improvement over [25, Theorem 1], we believe it is a promising path towards proving that the wished uniqueness result holds in the 0 < α,β < 12 range. We refer the reader to Corollary 5.8 below and the discussion that succeeds it for more precise statements.

![image 60](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile60.png>)

![image 61](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile61.png>)

- 1.4. Organization. We comment brieﬂy on the overall display of our results throughout the text. In Section 2 below, we discuss generalities on background results needed for the proofs of the main Theorems, going over results in the theory of band-limited functions, modular forms and functional analysis. Next, in Section 3, we prove, in this order, theorems 1.1, 1.2 and 1.3 about band-limited perturbed interpolation formulae. We then prove, in Section 4, Theorem 1.4, by ﬁrst discussing the proof Theorem 1.5 in §4.1. We then discuss the applications of our main results and techniques in Section 5, and ﬁnish the manuscript with Section 6, talking about some possible reﬁnements and open problems that arise from our discussion throughout the paper.


2. Preliminaries

- 2.1. Band-limited functions. We start by recalling some basic facts about bandlimited functions. Given a function f ∈ L2(R), we say that it is band-limited if its Fourier transform satisﬁes that supp( f) ⊂ [−M,M] for some M > 0. In this case, we say that f is band-limited to [−M,M].

It is a classical result due to Paley and Wiener that a function f ∈ L2(R) is bandlimited if and only if it is the restriction of an entire function F : C → C to the real axis, and the function F is of exponential type; that is, there exists σ > 0 so that, for each ε > 0,

|F(z)| ≤ Cεe(σ+ε)|z|, for all z ∈ C. From now on we will abuse notation and let F = f whenever there is no danger of confusion, and we may also write f ∈ PWσ (Paley–Wiener space) to denote the space of functions with such properties.

Besides this fact, we will make use of some interpolation formulae for those functions. Namely,

- (1) Shannon–Whittaker interpolation formula. For each f ∈ L2(R) band-limited to [−12, 12], the following formula holds:

![image 62](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile62.png>)

![image 63](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile63.png>)

f(x) =

n∈Z

f(n)sinc(x − n),

where sinc(x) = sin(πxπx) and the sum above converges both in L2(R) and uniformly on compact sets of C.

![image 64](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile64.png>)

- (2) Vaaler interpolation formula. For each f ∈ L2(R) band-limited to [−1,1], the following formula holds:


f(x) =

sin πx π

![image 65](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile65.png>)

2

n∈Z

f(n) (x − n)2 −

![image 66](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile66.png>)

f′(n) x − n

![image 67](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile67.png>)

,

where the right-hand side converges both in L2(R) and uniformly on compact sets of C.

For more details on these classical results, see, for instance, [30], [20],[23],[28] and [32].

- 2.2. Modular forms. In order to prove the improved estimates on the interpolation basis for the Radchenko–Viazovska interpolation result, we will need to make careful


computations involving certain modular forms deﬁning the interpolating functions. For that purpose, we gather some of the facts we will need in this subsection.

We denote by H = {z ∈ C: Im(z) > 0} the upper half plane in C. The special feature of this space is that the group SL2(R) of matrices with real coeﬃcients and determinant 1 acts naturally on it through M¨obius transformations: for

γ =

a b c d ∈ SL2(R), z ∈ H ⇒ γz =

az + b cz + d ∈ H.

![image 68](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile68.png>)

For our purposes, it will suﬃce to look at the subgroup PSL2(Z) = SL2(Z)/{±I}. Some elements of this group will be of special interest to us. Namely, we let

I =

1 0 0 1

, T =

1 1 0 1

, S =

- 0 −1
- 1 0


This already allows us to deﬁne the most valuable subgroup of SL2(Z) for us: the group Γθ is deﬁned then as the subgroup of SL2(Z) generated by S and T2. This group has 1 and ∞ as cusps, and its standard fundamental domain is given by

D = {z ∈ H: |z| > 1,Re(z) ∈ (−1,1)}.

With these at hand, we deﬁne modular forms for Γθ. For that purpose, we will use the following notation for the Jacobi theta series:

exp(πin2τ + 2πinz).

ϑ(z,τ) =

n∈Z

We are interestes in some of its Nullwerte, the so-called Jacobi theta series. These are deﬁned in H by

- Θ2(τ) = exp

πiτ 4

![image 69](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile69.png>)

ϑ

- 1

![image 70](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile70.png>)

- 2


τ,τ ,

- Θ3(τ) = ϑ(0,τ)(=: θ(τ)),
- Θ4(τ) = ϑ


- 1

![image 71](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile71.png>)

- 2


,τ .

These functions satisfy the identity Θ43 = Θ42 + Θ44. Moreover, under the action of the elements S and T of SL2(Z), they transform as

- (−iz)−1/2Θ2(−1/z) = Θ4(z), Θ2(z + 1) = exp(iπ/4)Θ2(z),
- (−iz)−1/2Θ3(−1/z) = Θ3(z), Θ3(z + 1) = Θ4(z),
- (−iz)−1/2Θ4(−1/z) = Θ2(z), Θ4(z + 1) = Θ3(z).


- (2.1) These functions allow us to construct the classical lambda modular invariant given by


- Θ2(z)4

![image 72](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile72.png>)

- Θ3(z)4


.

λ(z) =

Using the nome q = q(z) = eπiz, the lambda invariant can be alternatively rewritten as

- (2.2) λ(z) = 16q ×

∞

k=1

1 + q2k 1 + q2k−1

![image 73](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile73.png>)

8

= 16q − 128q2 + 704q3 + ··· . Besides this alternative formula, this is also invariant under de action of elements of the subgroup Γ(2) ⊂ SL2(Z) of all matrices

a b c d

so that a ≡ b ≡ 1 mod 2, c ≡ d ≡ 0 mod 2. Besides this invariance, (2.1) gives us immediately that

λ(z + 1) =

λ(z) 1 − λ(z)

![image 74](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile74.png>)

, λ −

1 z

![image 75](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile75.png>)

- (2.3) = 1 − λ(z).


We then deﬁne the modular invariant function for Γθ to be J(z) =

1 16

λ(z)(1 − λ(z)).

![image 76](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile76.png>)

From (2.3), we obtain immediately that J is invariant under the action of elements of Γθ; i.e.,

1 z

J(z + 2) = J(z), J −

= J(z).

![image 77](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile77.png>)

Other properties of the functions λ and J that we may eventually need will be proved throughout the text.

Finally, we mention that, for the proof in §4, we will need to use the so-called θ−automorphy factor deﬁned, for z ∈ H and γ ∈ Γθ, as

θ(z) θ(γz)

jθ(z,γ) =

. With this in hands, we deﬁned a slash operator of weight k/2 to be (f|k/2γ)(z) = jθ(z,γ)kf

![image 78](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile78.png>)

az + b cz + d

,

![image 79](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile79.png>)

where γ =

a b c d

. These slash operators induce other sign slash operators given by

(f|εk/2γ) = χε(γ)(f|k/2γ), where we let χε be the homomorphism of Γθ so that χε(S) = ε,χε(T2) = 1.

For more information on the functions λ,J and the automorphy factors we just deﬁned, we refer the reader to [6]and [24, Section 2]; see also[2], [34].

- 2.3. Functional analysis. We also recall some classical facts in functional analysis that will be useful throughout our proof.


As our main goal and strategy throughout this manuscript is to prove that a small perturbation of the identity is invertible, we must ﬁnd ways to prove that the operators arising in our computations are bounded. To that extent, we use two major criteria to prove boundedness – and therefore to prove smallness of the bounding constant. These are:

- (1) Hilbert-Schmidt test. Let H be a Hilbert space, and let there be given a linear operator T : H → H. If T satisﬁes additionally that

i,j

| Tej,ei |2 < +∞

for some orthonormal basis {ei}i∈Z of H, then the operator T is bounded. Moreover,

T 2H→H ≤

i,j

| Tej,ei |2 =: T 2HS.

- (2) Schur test. Let (aij)i,j≥0 denote an inﬁnite matrix. Suppose that there are two sequences {pi}i≥0 and {qi}i≥0 of positive real numbers so that


- i≥0

|aij|qi ≤ λpj,

- j≥0


|aij|pj ≤ µqi,

for some positive constants µ,λ > 0. Then the operator T : ℓ2(N) → ℓ2(N) given by aij = Tei,ej (where {ei}i≥0 denotes the standard orthonormal basis of ℓ2(N)) extends to a bounded linear operator. Moreover,

![image 80](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile80.png>)

T ℓ2→ℓ2 ≤ µλ.

Both tests will play a major role in the deduction of the validity of perturbed interpolation versions of the Radchenko–Viazovska result. The main diﬀerence is that, while Schur’s test generally gives one boundedness for more operator, the HilbertSchmidt test imposes stronger conditions on the operator. In fact, let us denote by T ∈ HS(H) the fact that T HS < +∞. A classical consequence of this fact is that T ∈ K(H); that is, T is compact.

This fact will be used when proving that a suitable version of our interpolation results holds for small perturbations of the origin. See, for instance, [5, Chapter 6]

- 2.4. Notation. We will use Vinogradov’s modiﬁed notation throughout the text; that is, we write A B in case there is an absolute constant C > 0 so that A ≤ C · B. If


the constant C before depends on some set of parameters λ, we shall write A λ B.

On the other hand, we shall also use the big-O notation f = O(g) if there is an absolute constant C such that |f| ≤ C · g, although the usage of this will be restricted mostly to sequences. We may occasionally use as well the standard Vinogradov notation a ≪ b to denote that there is a (relatively) large constant C > 1 such that a ≤ C · b.

We shall also denote the spaces of sequences decaying polinomially as

ℓ2s(N) = {an}n∈N:

|an|2n2s < +∞ .

n∈N

Finally, we always normalize our Fourier transform as f(ξ) = Ff(ξ) =

f(x)e−2πix·ξ dx.

Rn

3. Perturbed Interpolation Formulae for Band-Limited functions

- 3.1. Perturbed forms of the Shannon–Whittaker formula and Kadec’s result. Fix a sequence ε = {εk}k∈Z of real numbers such that supk |εk| < 1. We wish to obtain a criterion based solely on the value of L = supn |εn| such that the sequence {n + εn}n∈Z is completely interpolating in PWπ, i.e, for every sequence a = {an} ∈ ℓ2(Z) there is a unique f ∈ L2(R) of exponential type τ(f) ≤ π that satisﬁes


f(n + εn) = an.

Our goal here is to obtain a simple proof of such a criterion going through new and simple ideas. We will fall short of the 1/4 proven by Kadec by approximately 0.11, but it illustrates the power of our perturbation scheme and does not go through the theory of exponential bases.

In this particular case, we need to invert in ℓ2(Z) the operator given by Aε(a)(n) =

aksinc(n + εn − k),

k∈Z

where

sin π(x) πx

sinc(x) =

.

![image 81](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile81.png>)

The fact Aε is invertible will follow from proving that it is a close perturbation of the identity whenever L is suﬃciently small.

- 3.1.1. Auxiliary perturbations of the Hilbert transforms. Given a sequence a = {ak}k∈Z, we deﬁne the following operators, which are kin to the discrete Hilbert transform:


Hε(a)(n) =

k =n

H0(a)(n) =

k =n

We start by comparing these two objects:

(−1)n−kak n + εn − k

,

![image 82](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile82.png>)

(−1)n−kak n − k

.

![image 83](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile83.png>)

H0(a)(n) − Hε(a)(n) =

= εn

1 n + εn − k

1 n − k −

(−1)n−kak

![image 84](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile84.png>)

![image 85](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile85.png>)

k =n

1 (n − k)(n + εn − k)

(−1)n−kak

.

![image 86](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile86.png>)

k =n

This identity then gives us

|n − k| |n + εn − k|

1 |n − k|2

|H0(a)(n) − Hε(a)(n)| ≤ |εn|

|ak|

![image 87](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile87.png>)

![image 88](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile88.png>)

k =n

1 |n − k|2

|εn| 1 − |εn| k =n

|ak|

.

≤

![image 89](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile89.png>)

![image 90](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile90.png>)

This means that, in norm, one can compare these two operators. Indeed, it is a classical result that the operator norm of H0 is π, and by Plancherel the operator norm of the transformation

1 |n − k|2 is π2/3. This in turn implies

S(a) =

ak

![image 91](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile91.png>)

k =n

π2 3

supn |εn| 1 − supn |εn|

- (3.1) .


 Hε ≤ π +

![image 92](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile92.png>)

![image 93](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile93.png>)

- 3.1.2. Norm estimates of the perturbation. It is worth noticing the the estimate (3.1)


is very crude, as it is meant to depend only on L = supn |εn|. For instance, if {εn}n∈Z is a constant sequence, then the norm  Hε is equal to π. We also note that the fact that we obtain invertibility by means of perturbations of small norm of a invertible operator does not take into account other factors, such as cancellation.

In order to apply our perturbation scheme to the operator Aε, we need to bound the following family of operators:

Pε(a)(n) =

ak(sinc(n + εn − k) − δn,k).

k∈Z

We may rewrite them as Pε(a)(n) =(sinc(εn) − 1)an +

ak(sincn(n + εn − k))

k =n

(−1)n−k sin πεn π(n + εn − k) This implies, on the other hand,

ak

=(sinc(εn) − 1)an +

![image 94](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile94.png>)

k =n

sinπεn

π Hε(a)(n), which in turn implies that

Pε(a)(n) = (sinc(εn) − 1)an +

![image 95](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile95.png>)

sin πεn

Pε ≤ sup

|sinc(εn) − 1| + sup

π  Hε ≤ sup

![image 96](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile96.png>)

n

n

supn |sin πεn|supn |εn| 1 − supn |εn|

π 3

.

|sinc(εn) − 1| + sup

|sin πεn| +

![image 97](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile97.png>)

![image 98](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile98.png>)

n

n

Since Aε = Pε + Id, whenever 1 − sinc(L) + |sin πL| +

π 3

Lsin πL 1 − L

< 1,

![image 99](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile99.png>)

![image 100](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile100.png>)

we will have that Aε is invertible. In particular, a routine numerical evaluation implies that L < 0.239 satisﬁes the inequality above. Let then A−ε 1 : ℓ2(Z) → ℓ2(Z) be the inverse of Aε, which is continuous by the considerations above. We know, by the Shannon–Whittaker interpolation formula 1.2, that Aε takes {f(k)}k∈Z, for f ∈ PWπ, to {f(k + εk)}k∈Z. This is enough to prove the assertion about recovery, and as such implies that

|f(n + εn)|2

n∈Z

is an equivalent norm to the usual L2−norm on PWπ, by [33, Theorem 1.13]. Moreover, by writing

A−ε 1(b)(k) =

bn · ρk,n, we have immediately

n∈Z

- (3.2) n∈Z


f(n + εn)ρk,n = f(k),

and supn k∈Z |ρk,n|2 1. If (A−ε 1)∗ : ℓ2(Z) → ℓ2(Z) denotes the adjoint of the inverse of Aε, then we see that

(A−ε 1)∗(sincx(k)) ℓ2(Z) A−ε 1 ℓ2→ℓ2, where the implicit constant does not depend on x, and we let sincx(k) := sinc(x − k). Therefore, by letting gn(x) = k∈Z ρk,nsinc(x − k), we have

1/2

|gn(x)|2

sup

1,

x∈R n∈Z

and thus, by the previous considerations, the sum n∈Z f(n + εn)gn(x) converges absolutely. As (A−ε 1)∗(sincx(k)),f(n + εn) = sincx(k),A−ε 1 (f(n + εn)) = f(x) by Shannon–Whittaker, this implies

f(n + εn)gn(x),

f(x) =

n∈Z

as desired. This ﬁnishes the proof of Theorem 1.1.

- 3.2. From Shannon to Vaaler: the proof of Theorem 1.2. We now concentrate in proving that the usual Shannon–Whittaker interpolation formula implies Vaaler’s celebrated interpolation result with derivatives [30].


Indeed, as proving that the interpolation formula of Theorem 1.2 converges uniformly on compact sets of C is a routine computation, given that {ak}k∈Z,{bk}k∈Z ∈ ℓ2(Z), we shall omit this part and focus on proving that the asserted equality holds.

Given a sequence a = {ak}k∈Z, we deﬁne the following operators: H(a)(k) =

ak−j j

aj k − j

1 π k =j∈Z

1 π 0 =j∈Z

=

,

![image 101](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile101.png>)

![image 102](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile102.png>)

![image 103](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile103.png>)

![image 104](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile104.png>)

ak−j j + 21

aj k − j + 12

1 π j∈Z

1 π j∈Z

=

.

H1(a)(k) =

![image 105](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile105.png>)

![image 106](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile106.png>)

![image 107](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile107.png>)

![image 108](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile108.png>)

![image 109](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile109.png>)

![image 110](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile110.png>)

It is known that both H and H1 are bounded operators in ℓ2(Z), with H1 being also unitary with H2 its inverse being given by

aj−k j − 21

aj j − k + 12

1 π j∈Z

1 π j∈Z

=

.

H2(a)(k) = −

![image 111](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile111.png>)

![image 112](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile112.png>)

![image 113](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile113.png>)

![image 114](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile114.png>)

![image 115](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile115.png>)

![image 116](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile116.png>)

Given a function f ∈ PWπ, as a consequence of the Shannon–Whittaker interpolation formula we obtain, for every k ∈ Z, that

f(j) k − j

f′(k) =

(−1)k−j.

![image 117](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile117.png>)

j =k

We consider three sequences, as follows:

a(k) = f(2k − 1), b(k) = f(2k), c(k) = f′(2k). We have, thus,

f(j) 2k − j

f(2j) k − j −

f(2j − 1) k − j + 12

- 1

![image 118](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile118.png>)

- 2 j =k


- 1

![image 119](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile119.png>)

- 2 j∈Z


c(k) = f′(2k) =

(−1)2k−j =

![image 120](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile120.png>)

![image 121](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile121.png>)

![image 122](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile122.png>)

![image 123](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile123.png>)

j =2k

π 2H(b)(k) −

- 1

![image 124](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile124.png>)

- 2 j =k


b(j) k − j −

a(j) k − j + 12

1 2 j∈Z

π 2H1(a)(k).

=

=

![image 125](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile125.png>)

![image 126](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile126.png>)

![image 127](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile127.png>)

![image 128](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile128.png>)

![image 129](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile129.png>)

![image 130](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile130.png>)

This means that, for every k ∈ Z, H1(a)(k) = H(b)(k) −

2 π

c(k). Since H2 is the inverse of H1, this can be rewritten as

![image 131](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile131.png>)

2 πH2(c)(k).

a(k) = (H2 ◦ H)(b)(k) −

![image 132](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile132.png>)

We know, by the Shannon–Whittaker interpolation formula, that f(x) =

sinπ(x − k) π(x − k)

.

f(k)

![image 133](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile133.png>)

k∈Z

This implies, on the other hand, f(x) =

sin π(x − 2k + 1) π(x − 2k + 1)

2 πH2(c)(k)]

sin π(x − 2k) π(x − 2k)

+

[(H2 ◦ H)(b)(k) −

f(2k)

![image 134](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile134.png>)

![image 135](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile135.png>)

![image 136](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile136.png>)

k∈Z

k∈Z

sin π(x − 2k + 1) π(x − 2k + 1)

sin πx π(x − 2k)

+

=

(H2 ◦ H)(b)(k)

b(k)

![image 137](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile137.png>)

![image 138](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile138.png>)

k∈Z

k∈Z

2 π k∈ZH2(c)(k)

sin π(x − 2k + 1) π(x − 2k + 1)

= A(x) + B(x) + C(x).

−

![image 139](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile139.png>)

![image 140](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile140.png>)

We shall investigate each term A,B and C thoroughly in order to obtain our ﬁnal result.

- 3.2.1. Determining C. By considering the family of functions hj ∈ PWπ – which satisfy the important property hj(k) = 0, if k ∈ 2Z – given by

hj(z) =

sin2(12πz) π2(z − 2j)

![image 141](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile141.png>)

![image 142](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile142.png>)

, we obtain

C(x) = −2

k∈Z j∈Z

f′(2j) π2(j − k + 12)

![image 143](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile143.png>)

![image 144](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile144.png>)

sin π(x − 2k + 1) π(x − 2k + 1)

![image 145](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile145.png>)

= 4

j∈Z

f′(2j)

k∈Z

1 π2((2k − 1) − 2j)

![image 146](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile146.png>)

sin π(x − (2k − 1)) π(x − (2k − 1))

![image 147](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile147.png>)

= 4

j∈Z

f′(2j)

k∈Z

hj(2k − 1)

sin π(x − (2k − 1)) π(x − (2k − 1))

![image 148](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile148.png>)

= 4

j∈Z

f′(2j)

k∈Z

hj(k)

sin π(x − k) π(x − k)

![image 149](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile149.png>)

.

Notice that one can use Fubini’s theorem to justify all the changes of order of summation, by the fact that hj ∈ PWπ. By applying the Shannon-Whittaker interpolation to hj, we have

C(x) = 4

j∈Z

f′(2j)

sin2(21πx) π2(x − 2j)

![image 150](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile150.png>)

![image 151](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile151.png>)

- 3.2.2. Determining B. For the second term, we expand


sin π(x − 2k + 1) π(x − 2k + 1)

B(x) =

H2 ◦ H(b)(k)

![image 152](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile152.png>)

k∈Z

sin π(x − 2k + 1) π(x − 2k + 1) j

H(b)(j) j − k + 12

1 π k∈Z

=

![image 153](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile153.png>)

![image 154](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile154.png>)

![image 155](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile155.png>)

![image 156](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile156.png>)

sinπ(x − 2k + 1) π(x − 2k + 1) j l =j

b(l) (j − k + 12)(j − l)

1 π2 k∈Z

.

=

![image 157](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile157.png>)

![image 158](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile158.png>)

![image 159](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile159.png>)

![image 160](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile160.png>)

By Fubini’s theorem, this implies B(x) =

1 j − k + 12

1 π2 l∈Z

1 j − l k∈Z

sin π(x − 2k + 1) π(x − 2k + 1)

b(l)

![image 161](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile161.png>)

![image 162](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile162.png>)

![image 163](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile163.png>)

![image 164](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile164.png>)

![image 165](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile165.png>)

j =l

1 π2 l∈Z

1 2j − 2k + 1

sin π(x − 2k + 1) π(x − 2k + 1)

2 j − l k∈Z

=

b(l)

![image 166](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile166.png>)

![image 167](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile167.png>)

![image 168](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile168.png>)

![image 169](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile169.png>)

j =l

sin2(21πx) 2j − x

sin2(12πx) π2 l∈Z

2 j − l

1 j(j + l − x2)

1 π2 l∈Z

![image 170](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile170.png>)

![image 171](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile171.png>)

.

=

b(l)

b(l)

=

![image 172](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile172.png>)

![image 173](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile173.png>)

![image 174](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile174.png>)

![image 175](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile175.png>)

![image 176](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile176.png>)

![image 177](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile177.png>)

j =l

j =0

But it is a well-known fact that the summation formula g(z) =

ψ(1 + z) − ψ(1 − z) z

1 j(j + z)

=

,

![image 178](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile178.png>)

![image 179](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile179.png>)

j =0

holds, where ψ(z) = dzd log Γ(z) is the digamma function. This implies, on the other hand,

![image 180](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile180.png>)

2sin2(12πx) π2 l∈Z

ψ(1 + l − x2) − ψ(1 − l + x2) 2l − x

![image 181](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile181.png>)

![image 182](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile182.png>)

![image 183](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile183.png>)

B(x) =

.

b(l)

![image 184](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile184.png>)

![image 185](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile185.png>)

- 3.2.3. Determining A + B. Using that sin(2x) = 2sin xcos x, we obtain

A(x) = −

2sin2(21πx) π2 l∈Z

![image 186](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile186.png>)

![image 187](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile187.png>)

b(l)

π cot(πx2) 2l − x

![image 188](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile188.png>)

![image 189](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile189.png>)

.

The digamma function satisﬁes the following functional equations, which we shall make use of:

ψ(1 − z) = ψ(z) + π cot πz, ψ(1 + z) = ψ(z) +

1 z

![image 190](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile190.png>)

. Using these relations with z = x2 − l in the equations above, we obtain readily A(x) + B(x) =

![image 191](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile191.png>)

4sin2(12πx) π2 l∈Z

![image 192](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile192.png>)

![image 193](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile193.png>)

b(l)

1 (x − 2l)2

![image 194](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile194.png>)

.

- 3.2.4. A+B+C. Summing the analysis undertaken for the terms above, we have


4sin2(12πx) π2 j∈Z

![image 195](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile195.png>)

f(x) = A(x) + B(x) + C(x) =

![image 196](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile196.png>)

This ﬁnishes the proof of Theorem 1.2.

f(2k) (x − 2k)2

+

![image 197](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile197.png>)

f′(2k) x − 2k

![image 198](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile198.png>)

.

- 3.3. Perturbations of Interpolation Formulae with derivatives. By the arguments in the previous section, the formula we just derived for PW2π, i.e.,


sin2(πx) π2 k∈Z

f′(k) x − k

f(k) (x − k)2

f(x) =

+

,

![image 199](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile199.png>)

![image 200](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile200.png>)

![image 201](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile201.png>)

converges in compact sets of C. We ﬁx, for shortness, the notation g(x) =

sin2(πx) π2x

sin2(πx) π2x2

, which means we can read Vaaler’s interpolation as

,h(x) =

![image 202](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile202.png>)

![image 203](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile203.png>)

f(k)g(x − k) + f′(k)h(x − k) .

f(x) =

k∈Z

Because of uniform convergence, we can diﬀerentiate term by term in the above formula. This implies, thus,

f(k)g′(x − k) + f′(k)h′(x − k) .

f′(x) =

k∈Z

We record, for completeness, the formulae for the derivatives of g′, h′ :

- g′(x) =

2sin(πx)(πxcos(πx) − sin(πx)) π2x3

![image 204](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile204.png>)

,

- h′(x) =


sin(πx)(2πxcos(πx) − sin(πx)) π2x2

,

![image 205](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile205.png>)

and for n ∈ Z,

gn = h′n = 0, gn′ = hn = δ0. Our goal now is to invert the operator A = Aε deﬁned in ℓ2(Z) × ℓ2(Z) by

- A1(a,b)n = k∈Z

ak · g(n + εn − k) +

k∈Z

bk · h(n + εn − k)

- A2(a,b)n = k∈Z


ak · g′(n + εn − k) +

- (3.3) bk · h′(n + εn − k),


k∈Z

where A(a,b) = (A1(a,b),A2(a,b)) for (a,b) ∈ ℓ2(Z) × ℓ2(Z). Furthermore, we wish to establish a criterion that depends only on L = sup|εn|. For that purpose, we estimate when the operator norm of Aε − Id from ℓ2(Z) × ℓ2(Z) to itself is small, in terms of L.

- 3.3.1. Auxiliary perturbations for the derivative case. Given a sequence a = {ak}k∈Z, we deﬁne the following operators:


ak (n + εn − k)p

Hεp(a)n =

,

![image 206](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile206.png>)

k =n

and denote by H0p the operator associated to the sequence εn = 0,∀n ∈ Z. In an analogous manner to the proof of Theore m1.1, we compare:

Therefore,

H0p(a)n − Hεp(a)n =

ak

k =n

p−1

=

j=0

p j

1 (n + εn − k)p

1 (n − k)p −

![image 207](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile207.png>)

![image 208](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile208.png>)

ak (n + εn − k)p(n − k)p−j

εpn−j

.

![image 209](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile209.png>)

k =n

p−1

|n − k|p (|n − k| − |εn|)p

p j |εn|p−j

ak |n − k|2p−j

|H0p(a)n − Hεp(a)n| ≤

.

![image 210](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile210.png>)

![image 211](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile211.png>)

j=0

k =n

p−1

p j |εn|p−jS2p−j(a∗)n,

1 (1 − |εn|)p

≤

![image 212](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile212.png>)

j=0

where

ak |n − k|q

Sεq(a)n =

,

![image 213](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile213.png>)

k =n

and a∗ = (|an|). Let us consider S(p) = max{ Sq , q = 1,... ,2p}. Since Sq+1(a∗)n ≤ Sq(a∗)n, we have

p−1

Sp+1(a∗)n (1 − |εn|)p

p j |εn|p−j

|H0p(a)n − Hεp(a)n| ≤

![image 214](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile214.png>)

j=0

(1 + |εn|)p − 1 (1 − |εn|)p Sp+1(a∗)n.

=

![image 215](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile215.png>)

This means that we have the following estimate on the norm of the perturbed operator:

- (3.4)  Hεp ≤ γp(L), where we let

γp(L) =  H0p +

(1 + L)p − 1

![image 216](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile216.png>)

(1 − L)p  Sp+1 . Now, in order to estimate the value of γp(L), we resort to [20, Corollary 2], which gives us that

 H0p =

(2π)mbm m!

![image 217](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile217.png>)

,

where bm is the maximum of |Bm(x)| when x ∈ [0,1], and Bm denotes the m-th Bernoulli polynomial. Therefore,

 H01 = π, H02 =

π2 3

![image 218](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile218.png>)

, H03 =

π3 9√3

![image 219](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile219.png>)

![image 220](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile220.png>)

. On the other hand, by Plancherel‘s theorem it is easy to see that

 Sp = 2ζ(p). Joining all these data into (3.4), we obtain

-  Hε1 ≤ π +

L 1 − L

![image 221](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile221.png>)

π2 3

![image 222](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile222.png>)

,

-  Hε2 ≤

π2 3

![image 223](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile223.png>)

+ 2

L2 + 2L (1 − L)2

![image 224](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile224.png>)

ζ(3),

-  Hε3 ≤


π3 9√3

![image 225](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile225.png>)

![image 226](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile226.png>)

+

L3 + 3L2 + 3L (1 − L)3

![image 227](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile227.png>)

π4 45

![image 228](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile228.png>)

- (3.5) .

- 3.3.2. Norm estimates of the perturbations in the derivative case. In order to invert the operator Aε, we estimate the norm of Pε = Aε − Id = (P1,P1), where


- P1(a,b)n = k∈Z

ak · (g(n + εn − k) − δn,k) +

k∈Z

bk · h(n + εn − k),

- P2(a,b)n = k∈Z


ak · g′(n + εn − k) +

k∈Z

- (3.6) bk · (h′(n + εn − k) − δn,k).

By a straightforward calculation,

- P1(a,b)n =(g(εn) − 1)an +

sin(πεn)2 π2 Hε2(a)n + h(εn)bn +

![image 229](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile229.png>)

sin(πεn)2 π2 Hε1(b)n,

![image 230](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile230.png>)

- P2(a,b)n =g′(εn)an +


2sin(πεn)(πεn cos(πεn) − sin(πεn)) π2 Hε3(a)

![image 231](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile231.png>)

+ (h′(εn) − 1)bn +

sin(πεn)(2πεn cos(πεn) − sin(πεn))

![image 232](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile232.png>)

- (3.7) π2 Hε2(b). Thus,


 Pε ≤

√

sin(πL)2 π2  Gε ,

2 max{|g(L) − 1|,|h′(L) − 1|,|g′(L)|,|h(L)|} +

![image 233](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile233.png>)

![image 234](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile234.png>)

where Gε = G = (G1,G2) and

- G1(a,b)n =Hε2(a)n + Hε1(b)n,
- G2(a,b)n =


- (3.8)


(2πεn cos(πεn) − sin(πεn))

2(πεn cos(πεn) − sin(πεn)) sin(πε) Hε3(a) +

sin(πε) Hε2(b). By taking L < 1/4 and using the Cauchy-Schwarz inequality, we have  Gε 2/2 ≤ max{ Hε1 , Hε2 }2

![image 235](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile235.png>)

![image 236](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile236.png>)

2

2

2(πLcos(πL) − sin(πL)) sin(πL)

(2πLcos(πL) − sin(πL)) sin(πL)

 Hε3

2,

 Hε2

2

+ max

![image 237](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile237.png>)

![image 238](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile238.png>)

≤ max{γ1(L)2,γ2(L)2}

2(πLcos(πL) − sin(πL)) sin(πL)

+ max

![image 239](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile239.png>)

2

γ3(L)2,

(2πLcos(πL) − sin(πL)) sin(πL)

![image 240](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile240.png>)

2

γ2(L)2 .

We note that we have abused the notation  Gε to denote the operator norm of Gε when deﬁned on ℓ2(Z) × ℓ2(Z). One can further check that, for 0 ≤ L < 1/4,

|g(L) − 1| < |h′(L) − 1|,|h(L)| < |g′(L)|,γ1(L)2 < γ2(L)2 and 2(πLcos(πL) − sin(πL)) sin(πL)

2

2

(2πLcos(πL) − sin(πL)) sin(πL)

γ2(L)2, which means, in turn,

γ3(L)2 <

![image 241](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile241.png>)

![image 242](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile242.png>)

![image 243](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile243.png>)

2

(2πLcos(πL) − sin(πL)) sin(πL)

 Gε ≤ γ2(L) 2 1 +

,

![image 244](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile244.png>)

and directly implies the estimate

2sin(πL)(sin(πL) − πLcos(πL)) π2L3

sin(πL)(2πLcos(πL) − sin(πL)) π2L2

+

 Pε ≤1 −

![image 245](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile245.png>)

![image 246](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile246.png>)

![image 247](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile247.png>)

2

sin(πL)2 π2

L2 + 2L (1 − L)2

π2 3

(2πLcos(πL) − sin(πL)) sin(πL)

+

ζ(3) 2 1 +

.

+ 2

![image 248](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile248.png>)

![image 249](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile249.png>)

![image 250](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile250.png>)

![image 251](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile251.png>)

By evaluating the last expression on the right-hand side above numerically, we obtain that we can go up to L < 0.111 and mantain  Pε < 1. By invoking again [33, Theorem 1.13], we see immediately that

|f(n + εn)|2 + |f′(n + εn)|2

n∈Z

yields an equivalent norm for PW2π, as long as supn |εn| < 0.111.

Moreover, as A−ε 1 : ℓ2(N) × ℓ2(N) → ℓ2(N) × ℓ2(N) is bounded, the same argument as in the proof of Theorem 1.1 shows that there are ̺k,n,,ϑk,n,̺′k,n,ϑ′k,n such that

f(n + εn)̺k,n + f′(n + εn)ϑk,n,

f(k) =

n∈Z

f′(k) =

- (3.9) f(n + εn)̺′k,n + f′(n + εn)ϑ′k,n,


n∈Z

and supn k∈Z{|̺k,n|2 + |ϑk,n|2 + |̺′k,n|2 + |ϑ′k,n|2} 1. By using the adjoint (A−ε 1)∗ :

ℓ2(Z)×ℓ2(Z) → ℓ2(Z)×ℓ2(Z) in an analogous manner to that of the proof of Theorem 1.1 together with (3.9) and (1.6), we obtain the asserted existence of the functions gn,hn ∈ PW2π so that

f(n + εn)gn(x) + f′(n + εn)hn(x),

f(x) =

n∈Z

where the right-hand side converges absolutely, as desired. This proves the desired perturbation of Vaaler’s interpolation formula, given in Theorem 1.3.

4. Perturbations of Fourier interpolation on the real line

- 4.1. Improved estimates on the interpolation basis. As our goal is to obtain the perturbations of the formula


[f(√n)an(x) + f(√n) an(x)]

![image 252](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile252.png>)

![image 253](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile253.png>)

f(x) =

n≥0

to as large as possible, we must improve the decay estimates for the interpolating functions an. In [24, Section 5], the authors prove that an/n2 is uniformly bounded in n ≥ 0,x ∈ R. In order to be able to make the perturbations larger, we need to improve that result substantially, as even the reﬁned bound |an| = O(n1/4 log3/2(1 + n)) from [3] does not seem to be enough for our purposes. This ﬁrst subsection is, therefore, devoted to the proof of Theorem 1.5.

In order to prove this result we will employ the moral idea behind the characterization of Gelfand-Shilov spaces. These are spaces where, in a nutshell, both function and Fourier transform decay as fast as the negative exponential of a certain monomial. The following result connects these spaces with speciﬁc decay on function and Fourier side for certain Schwartz norms. See, e.g., [7, Theorem 2.3] for a proof.

Lemma 4.1. Let A,B,r,s > 0 be positive constants. The following assertions are equivalent:

- (1) There is C > 0 such that

sup

x∈R

|xαϕ(x)| ≤ CAα(α!)r, sup ξ∈R

|ξβ ϕ(ξ)| ≤ CBβ(β!)s,

for all α,β ∈ Z;

- (2) There is C′ > 0 such that


1

1

r , | ϕ(ξ)| ≤ C′e−Ω|ξ/B|

|ϕ(x)| ≤ C′e−θ|x/A|

s ,

![image 254](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile254.png>)

![image 255](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile255.png>)

for all x,ξ ∈ R.

We will use this result together with explicit estimates on {b±n }n≥0, in the same spirit as in [24]. Indeed, let ε ∈ {±} be a sign. In [24], the authors consider the generating functions ∞

gnε(z)eiπnτ =: Kε(τ,z),

n=0

where gnε are weakly holomorphic modular forms of weight 3/2 with growth and coefﬁcient properties so that the functions

1

- 1

![image 256](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile256.png>)

- 2


gnε(z)eiπx2z dz

bεn(x) =

−1

are eigenvectors of the Fourier transform associated to the eigenvalues ε satisfying that b±n = an ± an, for {an}n≥0 deﬁned as in 1.3. We mention, for completeness, the following result:

Theorem 4.2 (Theorem 3 in [24]). The following assertions hold:

θ(τ)(1 − 2λ(τ))θ(z)3J(z) J(z) − J(θ)

,

K+(τ,z) =

![image 257](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile257.png>)

θ(τ)J(τ)θ(z)3(1 − 2λ(z)) J(z) − J(θ)

K−(τ,z) =

,

![image 258](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile258.png>)

- (4.1)

where θ,J and λ are as previously deﬁned. Moreover, Kε(τ,z) are meromorphic functions with poles at τ ∈ Γθz, and the right-hand side of (4.1) converges for all τ with large enough imaginary part.

The authors then deﬁne the natural candidate for the generating function for the {bεn}n≥0 to be

- (4.2) Fε(τ,x) =

1 2

![image 259](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile259.png>)

1

−1

Kε(τ,z)eiπx2z dz,

which is deﬁned, a priori, for each ﬁxed x ∈ R and {τ ∈ H: ∀k ∈ Z,|τ − 2k| > 1} ⊃ D + 2Z, where D is the standard fundamental domain for Γθ. By Theorem 4.2, there holds that, whenever Im(τ) > 1,

- (4.3) Fε(τ,x) =

∞

n=0

bεn(x)eiπnτ.

As Fε(τ,x) admits an analytic continuation to H (see [24, Proposition 2]), they are able to extend (4.3) to the entire upper half space H. Moreover, the following functional equations hold:

Fε(τ,x) − Fε(τ + 2,x) = 0, Fε(τ,x) + ε(−iτ)−1/2Fε −1

![image 260](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile260.png>)

τ

,x = eiπτx2 + ε(−iτ)−1/2eiπ(−1/τ)x2.

- (4.4)


The proof of Theorem 1.5 follows the same essential philosophy as the proof of [24, Theorem 4]: in order to bound each of the terms b±n , we bound, uniformly on x ∈ R, the analytic function F±(τ,x). Relating the two bounds is achieved by the following Lemma, originally attributed to Hecke (see [24, Lemma 1] and [2, Lemma 2.2(ii)]):

Lemma 4.3. Let f : H → C be a 2−periodic analytic function admitting an absolutely convergent Fourier expansion

cneiπnτ.

f(τ) =

n≥0

Suppose, additionally, that for some α > 0 it satisﬁes that |f(τ)| ≤ CIm(τ)−α, for Im(τ) < c0. Then, for all n > c1

,

![image 261](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile261.png>)

0

|cn| ≤ Cn˜ α. Moreover, if n > πcα

, the improved estimate

![image 262](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile262.png>)

0

eπ α

α

|cn| ≤ C′

nα

![image 263](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile263.png>)

holds. Proof of Lemma 4.3. As f is analytic on H and its Fourier series expansion converges absolutely, an application of Fubini’s theorem gives us that

1+i/n

f(τ)e−iπnτ dτ.

2cn =

−1+i/n

The right hand side is, nonetheless, bounded in absolute value by

1

Cnαe−π dt = 2Ce−πnα,

−1

which follows from the growth restriction on f near the boundary of H. The ﬁrst assertion follows then with C˜ = 2Ce−π. For the second one, we compute instead

1+iπnα

![image 264](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile264.png>)

f(τ)e−iπnτ dτ.

2cn =

−1+iπnα

![image 265](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile265.png>)

Estimating the absolute value of this integral with the given condition yields that |cn| ≤ C′ eπα α nα, as wished.

![image 266](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile266.png>)

We are now ready to prove Theorem 1.5:

Proof of Theorem 1.5. We consider the functions

Fεk(τ,x) := xkFε(τ,x). By Lemma 4.3, if we prove that, for some ∆ > 0,

- (4.5) |Fεk(τ,x)| ≤ Ck(k!)Im(τ)−k/2−∆, for all k ≥ 1, then we will have that


|xkbεn(x)| ≤ C˜kn∆nk/2(k!).

sup

x∈R

As bεn = ε bn, Lemma 4.1 then implies that each of the functions bεn decays like |bεn(x)| n∆e−θ|x|/

√n,

![image 267](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile267.png>)

which is the content of Theorem 1.5. Therefore, we focus on proving a suitable version of (4.5). By the functional equation for Fε, we see that Fεk is a 2−periodic function on H that satisﬁes the functional equation

- (4.6) Fεk(τ,x) + ε(−iτ)−1/2Fεk(−1/τ,x) = xk(eiπτx2 + ε(−iτ)−1/2eiπ(−1/τ)x2). The strategy, in analogy to that in [24], is of splitting in cases: if τ ∈ D, then estimates

for Fεk are available directly by analytic methods. Otherwise, we need to use (4.6) to obtain the bound (4.5) for all τ ∈ H.

More explicitly, we have the following:

Proposition 4.4. There is a positive constants C > 0 such that, for each k ≥ 0 odd, the inequality

|Fεk(τ,x)| ≤ Ck(k!)(1 + Im(τ))−k/2 holds, whenever τ ∈ D.

This Proposition can be directly compared to [24, Lemma 4]. In fact, it is nothing but a carefully quantiﬁed version of it. Proof of Proposition 4.4. As the proof follows thoroughly the main ideas in Lemma 4 in [24], we will mainly focus on the points where we have to sharpen bounds.

We see directly from the deﬁnition of Fεk that we are allowed to consider only values of τ ∈ D1 = D ∩ {τ ∈ H: Re(τ) ∈ (−1,0)}. By subsequent considerations from that reduction, we see that the bound

- (4.7) |xkFε(τ,x)| ≤ 10 ℓ

|Kε(τ,z)|xk(e−πx2Im(τ) + |z|−1/2e−πx2Im(−1/z))|dz| holds, where ℓ is the path joining i to 1 on the upper half space, deﬁned to be

- (4.8) ℓ = w ∈ D: Re(J(w)) =

1 64

![image 268](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile268.png>)

, Im(J(w)) > 0 . An explicit computation gives us that the maximal value of

xke−πx2Im(z)

is attained at at x = 2πIm( k z)

![image 269](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile269.png>)

1/2

. Therefore, as any z ∈ ℓ has norm bounded from above and below by absolute constants, we ﬁnd that there is C > 0 so that

- (4.9) |Fεk(τ,x)| ≤ Ck/2 ·


k/2

k 2πe

|Kε(τ,z)|Im(z)−k/2 |dz|. We have then three regimes to consider:

![image 270](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile270.png>)

ℓ

- Case 1: |τ −i| < 1/10. Notice that if we prove that the proposition holds for any τ ∈ H


so that |τ −i| = 101 , we can use the maximum modulus principle on Fεk on that circle to conclude that the proposition holds inside as well. Moreover, by the functional equa-

![image 271](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile271.png>)

tion (4.6), we see that the proposition holds for A = {τ ∈ H: |τ − i| = 1/10,|τ| ≤ 1}

in case it holds for the image of the circle arc A under the action of S. But a simple computation shows that SA is just another circle arc contained (up to endpoints) in {τ ∈ D1: 14 > |τ − i| > 101 }. This shows that in order to prove the proposition for this case, it suﬃces to show it for the other cases.

![image 272](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile272.png>)

![image 273](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile273.png>)

- Case 2: |τ − i| > 101 , Im(τ) > 21. For this case, we use the fact that |Kε(τ,z)| |θ(z)|3 Im(z)−2e−π/Im(z) for z ∈ ℓ, Im(τ) > 12, with constants independent of τ. Using this bound in (4.7) yields

![image 274](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile274.png>)

![image 275](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile275.png>)

![image 276](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile276.png>)

|Fεk(τ,x)| ≤ (1 + |x|k+2)e−c|x| Ck

k + 2 e

![image 277](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile277.png>)

k+2

,

for some C > 0. Applications of Stirling’s formula imply that this bound is controlled by C1k(k!), with C1 > 0 an absolute constant. This shows the result in this case.

- Case 3: |τ − i| > 101 , Im(τ) ≤ 21. Again, we resort to the estimates in the proof of Lemma 4 in [24]: there, the authors prove that


![image 278](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile278.png>)

![image 279](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile279.png>)

|K+(τ,z)| Im(τ)−1/2 |J(τ)|3/8|J(z)|5/8Im(z)−3/2 |J(z) − J(τ)|

,

![image 280](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile280.png>)

|K−(τ,z)| Im(τ)−1/2 |J(τ)|7/8|J(z)|1/8Im(z)−3/2 |J(z) − J(τ)|

.

![image 281](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile281.png>)

Due to the not-so-symmetric nature of these bounds, we focus on the one for K+, and the analysis for K−, as well as the bounds, will be almost identical for the other, and thus the details will be omitted.

Taking advantage of the explicit structure of the curve we are integrating over (4.8), and the fact that there is an absolute constant C > 0 so that Im(z)−1 ≤ C log(1+|J(z)|) plus that z ∈ ℓ ⇐⇒ J(z) = 1/64 + it, t ∈ R,

|J(τ)|3/8t−3/8 log(k−1)/2(1 + t) t2 + |J(τ)|2

∞

|K+(τ,x)|Im(z)−k/2 |dz| ≤ Ck/2Im(τ)−1/2

dt.

![image 282](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile282.png>)

![image 283](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile283.png>)

ℓ

0

- (4.10)

Now, the last integral in (4.10) can be estimated as follows: as k − 1 is even, by using that log(1 + ab) ≤ log(1 + a) + log(1 + b) whenever a,b > 0, the integral

∞

0

t−3/8 log(k−1)/2(1 + t|J(τ)|) √1 + t2

![image 284](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile284.png>)

![image 285](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile285.png>)

dt is bounded by

k−1 2

![image 286](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile286.png>)

i=0

k−1 2

![image 287](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile287.png>)

i

logi(1 + |J(τ)|)

∞

0

t−3/8 log(k−1)/2−i(1 + t) √1 + t2

![image 288](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile288.png>)

![image 289](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile289.png>)

- (4.11) dt.


t−3/8 log(k−1)/2(1 + t|J(τ)|) √1 + t2

∞

= Ck/2Im(τ)−1/2

dt.

![image 290](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile290.png>)

![image 291](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile291.png>)

0

Each summand above can be easily estimated. Indeed, (k−i1)/2 ≤ 2k/2 trivially, logi(1 + |J(τ)|) ≤ CiIm(τ)−i, and the integrals can be explicitly bounded in terms of

Gamma functions. In fact, we ﬁrst split the integrals in question as

1

+

0

∞

1

t−3/8 log(k−1)/2−i(1 + t) √1 + t2

dt.

![image 292](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile292.png>)

![image 293](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile293.png>)

For the ﬁrst part, we simply bound the integrand by t−3/8 log(2)(k−1)/2−i, and this yields us a bound uniform in k. For the second, we change variables log(1 + t)  → s in

- (4.11) above. A simple computation shows that it is bounded by

10

∞

0

e−3s/8s(k−1)/2−i ds Ck

∞

0

e−rr(k−1)/2−i dr = CkΓ

k − 1

![image 294](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile294.png>)

2 − i + 1 . Thus, (4.11) is bounded by

CkIm(τ)(1−k)/2Γ

k − 1 2

![image 295](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile295.png>)

.

Putting together the estimates in (4.10) and (4.9) and using Stirling’s formula for the approximation of Γ, we conclude that

|Fεk(τ,x)| ≤ Ck(k!)Im(τ)−k/2, which was the content of the proposition.

In order to ﬁnish the proof of Theorem 1.5, we ﬁrst notice that Fεk is 2−periodic, so we lose no generality in assuming that τ ∈ {z ∈ H: Re(z) ∈ [−1,1]} = S1. If Re(τ) ∈ [−1,1], then we have two cases:

- (1) If τ ∈ D, we can use Proposition 4.4 directly, and the decay obtained by the assertion of the Proposition remains unchanged;
- (2) If τ ∈ S1\D, the strategy is to use (4.6) to reduce it to the previous case. In fact, we deﬁne the Γθ−cocycle {φkA}A∈Γθ by


φkT2(τ,x) = 0, φkS(τ,x) = xk(eiπx2τ + ε(−iτ)−1/2eiπx2(−1/τ)),

thogether with the cocycle relation

- (4.12) φkAB = φkA + φkA|B.

For a ﬁxed τ ∈ S1 \ D, we associate τ′ ∈ D through the following process: let

 



γ0 = τ, γi = −γ 1

![image 296](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile296.png>)

i−1

− 2ni,

- (4.13)


where ni = (−1/γi−1)+1

2 . We deﬁne m = m(τ) to be the smallest positive integer so that γm ∈ D. In this case, we let γm(τ) =: τ′. In other words, we

![image 297](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile297.png>)

have that the sequence

 

τ0 = τ′, τi+1 = −τ1i + 2ni

- (4.14)

satisﬁes the hypotheses of Lemma 3 in [24]. We therefore have that |τj| > 1, Im(τj) is nonincreasing and Im(τj) ≤ 2j1−1. An inductive procedure shows us that

![image 298](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile298.png>)

γm−i = −

1 τi

![image 299](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile299.png>)

.

In particular, the sequence {τi}i≥0 is in fact ﬁnite, with at most m(τ) terms. This implies that

- (4.15) m + 1 ≤ 4m − 2 ≤ 2Im(τ)−1.

We will use (4.15) in the following computation with the cocycle condition. We write τ′ = Aτ, where A ∈ Γθ is of the form

A = ST2nmST2nm−1S ··· T2n1S.

As {φkA}A∈Γθ satisﬁes the cocycle condition (4.12), the proof of Lemma 3 in [24] gives us that

Im(τ′)1/4|φkA(τ′)| ≤

m

j=1

Im(τj)1/4|φkS(τj)|.

By the deﬁnition of φkS, we see that

- (4.16) |φkS(τj,x)| ≤ CΓ

k + 1 2

![image 300](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile300.png>)

(Im(τj)−k/2 + |τj|−1/2Im(−1/τj)−k/2).

As γm−i = −τ1i = τi+1−2ni, |τj| > 1, and the sequence Im(τj) is nonincreasing, the right-hand side of (4.16) is bounded from above by C·Γ((k+1)/2)Im(τ)−k/2.

![image 301](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile301.png>)

From (4.15), it follows that

|φkA(τ′)|Im(τ′)1/4 ≤ CΓ

k + 1 2

![image 302](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile302.png>)

Im(τ)−k/2

 

m

j=1

Im(τj)1/4

 .

If we use the aforementioned facts about Im(τj), we will see that, in fact,

- (4.17) |φkA(τ′)|Im(τ′)1/4 ≤ CΓ




![image 303](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile303.png>)

k + 1 2

Im(τ)−k/2m(τ)3/4.

![image 304](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile304.png>)

Now, using the functional equation for Fεk implies

Fεk − (Fεk)|A = φkA, which then gives us

|Fεk(τ,x)||Im(τ)|1/4 ≤ |Im(τ′)|1/4|Fεk(τ′,x)| + |φkA(τ′,x)||Im(τ′)|1/4.

Denoting Im(τ′) =: I(τ) and using Proposition 4.4 and (4.17) to estimate this expression, it follows that

- (4.18) |Fεk(τ,x)| ≤ Im(τ)−k/2−14 Ck(k!) · I(τ)1/4 + Γ((k + 1)/2)m(τ)3/4 .

![image 305](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile305.png>)

In order to estimate (4.18), we must resort not only to Lemma 4.3 and its proof, but also to the following estimate of the average values of m(τ) and I(τ), recently available by the work of Bondarenko, Radchenko and Seip. We refer the reader to Propositions 6.6 and 6.7 in [3] for a proof.

Lemma 4.5. Whenever y ∈ (0,1/2), we have

1

−1

I(x + iy)1/4 1

and 1

−1

m(x + iy)3/4 log3/2(1 + y−1).

An application of Lemma 4.5 together with the bound (4.18) to the proof of the ﬁrst bound in Lemma 4.3 implies

- (4.19) sup

x∈R

|xkb±n (x)| Ckn1/4nk/2 log3/2(1 + n)(k!)

for n > c1

![image 306](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile306.png>)

0

,k ≥ 1. Also, in case n ≥ πck0, the sharper bound

![image 307](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile307.png>)

- (4.20) sup


|xkb±n (x)| (C′)kn1/4nk/2 log3/2(1 + n)(k!)1/2

x∈R

holds instead. We now employ then the main idea of proof of Lemma 4.1: we seek to optimize in k > 0.

Indeed, let us start by optimizing (4.19). We postpone the discussion on the improved bound (4.20) to a later remark.

Notice that we may assume |x| ≥ C′√n, as for if |x| < C′√n, the bound (4.19) with k = 0 gives us already the result, as 1 c e−c|x|/

![image 308](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile308.png>)

![image 309](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile309.png>)

√n. If we then set k = C|′x√|n, where C′ > 0 will be a ﬁxed positive constant, whose exact value shall be determined later, we have that

![image 310](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile310.png>)

![image 311](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile311.png>)

![image 312](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile312.png>)

|b±n (x)| n1/4 log3/2(1 + n) · exp(k log(Cn1/2) + k log(k) − k log |x|)

The exponential term above is exp |x| C′√n

(log(|x|) − log(C′√n)) −

|x| C′√n

log(Cn1/2) + |x| C′√n

![image 313](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile313.png>)

log |x|

![image 314](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile314.png>)

![image 315](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile315.png>)

![image 316](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile316.png>)

![image 317](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile317.png>)

![image 318](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile318.png>)

![image 319](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile319.png>)

C C′ .

= exp |x| C′√n

log

![image 320](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile320.png>)

![image 321](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile321.png>)

![image 322](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile322.png>)

We only need to set C′ ≥ 2C above, and this quantity will grow like exp(−c|x|/√n). This ﬁnishes the ﬁrst assertion in Theorem 1.5.

![image 323](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile323.png>)

For the second one, we notice that the proof above adapts in many instances. Indeed,

if we shift our attentionto the function ∂xFεk(τ,x) instead, we will see that, in an almost identical fashion to that of the proof of Proposition 4.4, we are able to prove that, for

all τ ∈ D,

|∂xFεk(τ,x)| Ck(k!)Im(τ)−k+12 . On the other hand, the partial derivative ∂x of the cocycle {φkA}A∈Γθ is itself a cocycle with respect to the same slash operator. Moreover, for A = S, the following formula holds:

![image 324](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile324.png>)

∂xφkS(τ,x) = (2πi)xk+1 τeπix2τ + iε(−iτ)−3/2eπix2(−1/τ) .

In that case, using the notation from above for the elements τ′,τj ∈ H associated to τ ∈ H ∩ {|z| ≤ 1}, we see that

m

Im(τj)1/4|∂xφkA(τj)|.

Im(τ′)1/4|∂xφkA(τ′)| ≤ Im(τ′)1/4|∂xφkS(τ′)| +

j=1

- For j ∈ {0,1,2,... ,m}, the deﬁnition of our new cocycle implies


k + 3 2 |τj|Im(τj)−k+12 + |τj|−3/2Im(τj+1)−k+12 ≤ Γ

|∂xφkS(τj,x)| Γ

![image 325](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile325.png>)

![image 326](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile326.png>)

![image 327](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile327.png>)

k + 3 2

Im(τ)−k+12 .

![image 328](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile328.png>)

![image 329](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile329.png>)

This follows as before from the fact that Im(τj+1) = Im(|τ τj)

j|2 ≥ Im(τ) and that |τj| > 1. Analyzing the functional equations for ∂xFεk(τ,x) in the same way as before readily gives that

![image 330](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile330.png>)

|∂xFεk(τ,x)| ≤ CkIm(τ)−k+12 −41(k!) I(τ)1/4 + m(τ)3/4 .

![image 331](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile331.png>)

![image 332](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile332.png>)

Lemma 4.5 and the considerations employed for Fεk apply almost verbatim here, and thus we conclude that

√n, as wished.

![image 333](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile333.png>)

|(b±n )′(x)| n3/4 log3/2(1 + n)e−c|x|/

As a consequence of Theorem 1.5, we are able to establish the following bound for the interpolation basis taking account both decay and zeros.

- Corollary 4.6. Let {an} be the interpolation sequence of functions from (1.3). Then there is c > 0 so that


√N)e−c

|x|

√n, for all positive integers n ∈ N.

|an(x)| n3/4 log3/2(1 + n)dist(|x|,

![image 334](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile334.png>)

![image 335](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile335.png>)

![image 336](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile336.png>)

Proof. We simply use the fundamental theorem of calculus to the an : without loss of generality, we suppose x > 0. We then have:

x

|an(x)| = |an(x) − an(√m) + δn,m| ≤

|a′n(x)|dx + δn,m

![image 337](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile337.png>)

√m

![image 338](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile338.png>)

√N)e−c

|x|

√n + δm,n n3/4 log3/2(1 + n)dist(x,

≤ n3/4 log3/2(1 + n)dist(x,

![image 339](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile339.png>)

![image 340](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile340.png>)

![image 341](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile341.png>)

√N)e−c

|x|

√n,

![image 342](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile342.png>)

![image 343](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile343.png>)

![image 344](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile344.png>)

as the δm,n factor is only one if |x| ∈ [√n,√n + 1), where 1 e−c|x|/

√n.

![image 345](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile345.png>)

![image 346](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile346.png>)

![image 347](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile347.png>)

√n suﬃcies for our purposes, below we sketch how to deduce a slightly improved decay for the interpolation basis {an}n≥0.

Remark. Although the exponential bound n1/4 log3/2(1 +n)e−c|x|/

![image 348](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile348.png>)

2

We again wish to optimize (4.20). If we set k = |x|

C′n, where C′ > 0 will be chosen soon, we have that

![image 349](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile349.png>)

|b±n (x)| n1/4 log3/2(1 + n) · exp(k log(Cn1/2) + k log(k1/2) − k log |x|). This bound holds as long as πn k ≥ 1. If instead k < 1, that means, |x| ≤

√C′√n, we

![image 350](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile350.png>)

![image 351](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile351.png>)

use the bound in either (4.19) or (4.20) for k = 0, which yields |b±n (x)| n1/4 log3/2(1+ n) n1/4 log3/2(1 + n)e−c|x|2/n, for c > 0.

On the other hand, in case k > 1, the ﬁrst exponential term above becomes

√

exp |x|2 C′n

log(Cn1/2) + |x|2 C′n

(log(|x|) − log(

![image 352](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile352.png>)

![image 353](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile353.png>)

|x|2 C′n

![image 354](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile354.png>)

C′n)) −

log |x|

![image 355](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile355.png>)

= exp |x|2 C′n

C √C′

log

. We only need to set C′ ≥ (2C)2 above, and this quantity will grow like exp(−c|x|2/n). For the remaining |x| >

![image 356](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile356.png>)

![image 357](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile357.png>)

![image 358](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile358.png>)

√

![image 359](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile359.png>)

C′n case, we need to reﬁne the analysis of the proof of Lemma 4.3 and Theorem 1.5. Indeed, it is easy to see that if n ∈ (2−jα,21−jα), j ≥ 1, then evaluating the Fourier coeﬃcients of a 2-periodic function f : H → C such that |f(τ)| Im(τ)−α I(τ)1/4 + m(τ)3/4 for Im(τ) ≤ 1 as 2cn = 1+i

α 2jπn

![image 360](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile360.png>)

−1+i2jαπn f(τ)e−πinτ dτ implies

![image 361](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile361.png>)

α

2jπe1/2j α

nα log3/2(1 + n).

|cn|

![image 362](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile362.png>)

Using this new bound in (4.18), we obtain that, when n ∈ (2−j−1k,2−jk),

|b±n (x)| n1/4 log3/2(1 + n) · exp k j/2 + log(C√n) + log(k1/2) − log |x| . This suggests that we take k = |x|

![image 363](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile363.png>)

2

C′2jn, which is admissible to the condition n ∈ (2−j−1k,2−jk) if |x| ∼

![image 364](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile364.png>)

√

C′2jn. A similar computation to the ones above implies that

![image 365](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile365.png>)

|b±n (x)| n1/4 log3/2(1 + n)exp −c|x|2

n1/4 log3/2(1 + n)exp(−c′|x|),

![image 366](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile366.png>)

2jn

whenever C′ ≫ C. The next corollary then follows as a natural consequence.

- Corollary 4.7. Let an : R → R be the interpolating functions in the Radchenko– Viazovska interpolation formula. Then there are c,C > 0 so that


|an(x)| n1/4 log3/2(1 + n) e−c|x|2/n1|x|<Cn + e−c|x|1|x|>Cn , for each n ≥ 1.

Indeed, the application of Lemma 4.3 requires that we take n ≥ C, for some C > 0 some absolute constant. In order to prove such a result for n 1, we may simply use the deﬁnition of b±n as a Laplace transform of a the weakly holomorphic modular form gn±. Indeed, in order to extend Corollary 4.7 to n = 0, we write

1

1 4

θ(z)3 eπix2z dz.

a0(x) = a0(x) =

![image 367](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile367.png>)

−1

In order to prove that a0 decays exponentially, we employ a similar technique to that of [24, Proposition 1]. Indeed, we have

|θ(z)|3 Im(z)−2 e−π/Im(z) for z → ±1

and moreover that |θ(z)| 1 whenever z ∈ H,|z| = 1. We also suppose without loss of generality that x > 0. This implies that, for δ > 0,

δ

e−1/(2t) t2

dt + e−πx2δ e−21δ + e−πx2δ.

|a0(x)|

![image 368](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile368.png>)

![image 369](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile369.png>)

0

√π

![image 370](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile370.png>)

2x, which is the desired bound. For other bounded values of n such a proof can be easily adapted.

We then choose, for x ≫ 1, δ = √21πx. This implies that |a0(x)| e−

![image 371](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile371.png>)

![image 372](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile372.png>)

![image 373](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile373.png>)

- 4.2. Proof of the main result. Let ℓ2s(N) = {(an)n ∈ ℓ2(N) : (nsan)n ∈ ℓ2(N)}.


Let I : ℓ2s(N) × ℓ2s(N) → ℓ2s(N) × ℓ2s(N) denote the identity operator. Recall the Radchenko-Viazovska interpolation result: for f ∈ Seven(R) a real function,

- (4.21) f(x) = n≥0

(f(√n)an(x) + f(√n) an(x)),

![image 374](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile374.png>)

![image 375](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile375.png>)

where an : R → R is a sequence of interpolating functions independent of the Schwartz function f. In particular,

f(

√

![image 376](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile376.png>)

k) =

n≥0

(f(√n)an(

![image 377](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile377.png>)

√

![image 378](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile378.png>)

k) + f(√n) an(

![image 379](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile379.png>)

√

![image 380](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile380.png>)

k)).

In fact, for any pair of sequences ({xi}i,{yi}i) decaying suﬃciently fast and satisfying the Poisson summation formula

- (4.22)

n∈Z

xn2 =

n∈Z

yn2,

the function

- (4.23) G(t) = n≥0


(xnan(t) + yn an(t))

is well-deﬁned and satisﬁes that G(√k) = xk, G(√k) = yk. In fact, let ({xi}i,{yi}i) ∈ ℓ2s(N) × ℓ2s(N) for s > 0 suﬃciently large. The operator

![image 381](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile381.png>)

![image 382](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile382.png>)

T : ℓ2s(N) × ℓ2s(N) → ℓ2s(N) × ℓ2s(N) given by T = (T1,T2), where

- T1({xi},{yi})k = n≥0

(xnan(

√

![image 383](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile383.png>)

k) + yn an(

√

![image 384](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile384.png>)

k)),

- T2({xi},{yi})k = T1({yi},{xi})k,


has an explicit form: indeed, for k ≥ 1, we have T1({xi},{yi})k = xk, T2({xi},{yi}) = yk.

- For k = 0, we have


- T1({xi},{yi})0 =

x0 + y0 2 −

![image 385](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile385.png>)

n≥1

xn2 +

n≥1

yn2,

- T2({xi},{yi})0 =


x0 + y0 2 −

xn2.

yn2 +

![image 386](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile386.png>)

n≥1

n≥1

In particular, it is then easy to see that T = I whenever ({xi}i,{yi}i) satisfy the Poisson relation (4.22). Inspired by this fact, we deﬁne the perturbed operator associated to a sequence εk > 0,k ∈ N, to be

T˜ deﬁned on ℓ2s(N) × ℓ2s(N), where T˜ = (T˜1,T˜2), with

- T˜1({xi},{yi})k = n≥0

(xnan( k + εk) + yn an( k + εk)),

![image 387](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile387.png>)

![image 388](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile388.png>)

- T˜2({xi},{yi})k = T˜1({yi},{xi})k,


for k ≥ 1, and T˜1({xi},{yi})0 = x0,T˜2({xi},{yi})0 = y0. A fundamental fact we will need for our proof is that this operator is bounded from ℓ2s(N)×ℓ2s(N) → ℓ2s(N)×ℓ2s(N). One way to see this will be provided in the proof of our main theorem, by showing that the operator norm I − T˜ ℓ2

s(N)×ℓ2s(N))→ℓ2s(N)×ℓ2s(N)) < +∞. This is, incidentally, our main device to prove our result: if

I − T˜ ℓ2

s(N)×ℓ2s(N))→ℓ2s(N)×ℓ2s(N)) < 1, then T˜ is an invertible operator deﬁned on ℓ2s(N) × ℓ2s(N). Therefore, its inverse T˜−1 : ℓ2s(N) × ℓ2s(N) → ℓ2s(N) × ℓ2s(N)

is well-deﬁned and bounded. In particular, for f ∈ Seven(R) real, given the lists of values

f(0),f(√1 + ε1),f(√2 + ε2),··· ,

![image 389](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile389.png>)

![image 390](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile390.png>)

f(0), f(√1 + ε1), f(√2 + ε2),··· , there is a unique pair ({xi}i,{yi}i) ∈ ℓ2s(N) × ℓ2s(N) so that

![image 391](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile391.png>)

![image 392](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile392.png>)

T˜({xi},{yi}) = ({f( k + εk)}k,{ f( k + εk)}k). But we also know that

![image 393](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile393.png>)

![image 394](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile394.png>)

√

√

√

√

T˜({f(

![image 395](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile395.png>)

![image 396](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile396.png>)

![image 397](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile397.png>)

![image 398](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile398.png>)

![image 399](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile399.png>)

![image 400](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile400.png>)

i)}i) = {f( k + εk)}k,{ f( k + εk)}k).

i)}i,{ f(

i)}i) = T({f(

i)}i,{ f(

This implies xj = f(√j), yj = f(√j). By writing the k−th entry of the inverse of T˜ as

![image 401](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile401.png>)

![image 402](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile402.png>)

T˜−1({wi},{zi})k =

(γj,kwj + γj,kzj),

j≥0

for two sequences {γj,k}j,k≥0, { γj,k}j,k≥0 so that |γj,k| + | γj,k| (j/k)s, we must have √

![image 403](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile403.png>)

![image 404](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile404.png>)

![image 405](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile405.png>)

- (4.24) f(


(γj,kf( j + εj) + γj,k f( j + εj)).

k) =

j≥0

This implies, by (1.3), that we can recover f from its values and those of its Fourier transform at √k + εk. Moreover, as the adjoint of T˜−1 is also bounded from ℓ2s(N) × ℓ2s(N) to itself, we conclude that, for s ≫ 1 suﬃciently large and f, f both being O((1 + |x|)−10s), we can use Fubini’s theorem in (1.3) together with (4.24). This proves the existence of two sequences of functions {θj}j≥0,{ηj}j≥0 so that

![image 406](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile406.png>)

|θj(x)| + |ηj(x)| + | θj(x)| + | ηj(x)| (1 + j)s(1 + |x|)−10 and

![image 407](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile407.png>)

![image 408](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile408.png>)

f( j + εj)θj(x) + f( j + εj)ηj(x) .

f(x) =

j≥0

Thus, we focus on the proof of the invertibility of T,˜ for s > 0 suitably chosen.

Proof of invertibility of T˜. We use, for this part, the Schur test. That is, deﬁne the inﬁnite matrices A = {Aij}i,j>0 and A = { Aij}i,j>0 by

Aij = (aj(√i + εi) − δij) × (i/j)s, Aij = aj(√i + εi)(i/j)s.

![image 409](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile409.png>)

![image 410](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile410.png>)

For a given vector (x,y) ∈ ℓ2(N) × ℓ2(N), we write then

B(x,y) = (A · x + A · y,A · y + A · x), or, in matrix notation,

A A A A

B =

.

Notice that the operator norm of T˜ − I acting on ℓ2s(N) × ℓ2s(N) is, by virtue of our deﬁnitions, the same as the operator norm of B acting on ℓ2(N) × ℓ2(N). Therefore, it will suﬃce to impose bounds on this latter quantity.

By Schur’s test, it suﬃces to ﬁnd α,β > 0 and positive sequences {pi}i≥0,{qi}i≥0 so that the following inequalities hold:

(i/j)s× |aj(√i + εi) − δij|pj + | aj(√i + εi)|qj ≤ αpi,

![image 411](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile411.png>)

![image 412](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile412.png>)

j>0

(i/j)s× |aj(√i + εi) − δij|qj + | aj(√i + εi)|pj ≤ αqi,

![image 413](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile413.png>)

![image 414](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile414.png>)

j>0

(i/j)s× |aj(√i + εi) − δij|pi + | aj(√i + εi)|qi ≤ βpj,

![image 415](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile415.png>)

![image 416](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile416.png>)

i>0

(i/j)s× |aj(√i + εi) − δij|qi + | aj(√i + εi)|pi ≤ βqj.

![image 417](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile417.png>)

![image 418](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile418.png>)

i>0

- (4.25)

Now, we make the Ansatz that, for all i > 0, pi = qi = iθ, for some real number θ ∈ R. By making use of Theorem 1.5, we know that

|aj(√i + εi) − δij| + | aj(√i + εi)|

![image 419](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile419.png>)

![image 420](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile420.png>)

εi √i

![image 421](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile421.png>)

![image 422](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile422.png>)

j3/4e−c

√

![image 423](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile423.png>)

i/j. Therefore, (4.25) reduces to verifying

j>0

(i/j)s × jθ ×

εi √i

![image 424](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile424.png>)

![image 425](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile425.png>)

j3/4e−c

√

![image 426](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile426.png>)

i/j ≤ αiθ,

i>0

(i/j)s × iθ ×

εi √i

![image 427](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile427.png>)

![image 428](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile428.png>)

j3/4e−c

√

![image 429](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile429.png>)

i/j ≤ βjθ.

- (4.26) Estimate of the ﬁrst term in (4.26). For this term, we rewrite it as

is−1/2 × εi

 

j>0

j3/4−se−c

√

![image 430](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile430.png>)

i/jjθ

 .

In order to estimate this last sum, we break it into j < i1/3 and j > i1/3 contributions. Therefore,

- (4.27) j>0


√

√

![image 431](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile431.png>)

![image 432](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile432.png>)

i/jjθ i1/3imax(3/4−s+θ,0)e−ci1/3 +

j3/4−se−c

i/jjθ.

j3/4−se−c

j>i1/3

Because of the presence of the exponential, the ﬁrst term is always bounded by an absolute constant times iθ, so we treat it as negligible. For the second term, notice that the summand is bounded by a constant times j j+1 x3/4−s+θe−c

√

![image 433](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile433.png>)

i/xdx. Indeed, the ratio between both is bounded by

√

√

√√jxi (√x−

√j)

j+1

![image 434](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile434.png>)

![image 435](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile435.png>)

![image 436](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile436.png>)

![image 437](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile437.png>)

i/j−

i/x dx ≤ 23/4−s+θ sup

(x/j)3/4−s+θec

![image 438](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile438.png>)

ec

![image 439](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile439.png>)

![image 440](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile440.png>)

x∈[j,j+1)

j

√√i

![image 441](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile441.png>)

′

≤ 23/4−s+θec

![image 442](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile442.png>)

![image 443](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile443.png>)

j3 s,θ 1,

as j > i1/3. Thus, we obtain that the second term on the right-hand side of (4.27) is bounded by

s,θ

√

i−1/3

∞

√iy dy

![image 444](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile444.png>)

![image 445](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile445.png>)

(1 + 1/y)3/4−s+θy−2e−c

i/x dx =

x3/4−s+θe−c

i1/3

0

i2/3

i−1/3

√iy dy = i7/4−s+θ

√y dy

![image 446](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile446.png>)

y−11/4+s−θe−c

y−11/4+s−θe−c

![image 447](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile447.png>)

0

0

s,θ i7/4−s+θ,

as long as −11/4 + s − θ > −1, that is, θ < s − 7/4. Thus, the ﬁrst term in (4.26) is bounded under such a condition by

Cs,θεiis−12i74−s+θ = i45+θεi.

![image 448](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile448.png>)

![image 449](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile449.png>)

![image 450](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile450.png>)

In order for this last quantity to be less than αiθ, we must have εi s,θ αi−54. We will assume that we have this bound while estimating the second term.

![image 451](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile451.png>)

Estimate for the second term in (4.26). For the second term, the strategy is similar, only now the estimates become somewhat simpler by the arithmetic of the bounds given by Theorem 1.5. Indeed, the second term in (4.26) is bounded by

√

![image 452](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile452.png>)

is+θ−47e−c

cs,θj 34−s

i/j .

![image 453](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile453.png>)

![image 454](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile454.png>)

i>0

√

![image 455](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile455.png>)

Similarly as before, each summand above is bounded by i i+1 xs+θ−47e−c

x/j dx. Thus, the expression within the parenthesis above is bounded by

![image 456](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile456.png>)

√

∞

∞

√x dx.

![image 457](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile457.png>)

xs+θ−74e−c

xs+θ−47 e−c

x/j dx s,θ js+θ−43

![image 458](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile458.png>)

![image 459](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile459.png>)

![image 460](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile460.png>)

![image 461](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile461.png>)

0

1

This last integral converges given that s + θ − 74 > −1 ⇐⇒ s + θ > 43. In the end, we obtain that the second term in (4.26) is bounded by cs,θjθ if these conditions on s,θ hold.

![image 462](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile462.png>)

![image 463](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile463.png>)

Finally, we gather these two estimates to get that, if s − θ > 74,s + θ > 43 and if εi < γi−54 for γ > 0 suﬃciently small, then both terms of (4.26) are bounded by small constants times iθ and jθ. Notice that picking s = 10 and θ > 0 suﬃciently small yields that both conditions above hold true, and thus the result follows from Schur’s test, as previously indicated.

![image 464](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile464.png>)

![image 465](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile465.png>)

![image 466](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile466.png>)

As mentioned in the beginning of this manuscript, the usage of Schur’s test here was instrumental in order to expand the range of our perturbations. In fact, in §5.1, se employ the Hilbert–Schmidt test successfully to our operator T˜ and obtain that, as long as there is δ > 0 such that εi i−54−δ, then T˜ is bounded on ℓ2s(N) × ℓ2s(N), for s suﬃciently large, but we seem to be unable to include 5/4 in our considerations with the Hilbert–Schmidt method.

![image 467](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile467.png>)

On the other hand, we will see in that subsection that the Hilbert–Schmidt method provides us with a way to suitably perturb the origin, a feature we could not obtain with Schur’s test.

5. Applications of the main results and techniques

- 5.1. Interpolation formulae perturbing the origin. In the main results of this manuscript, the only interpolation node that remains unchanged in every scenario is 0. One of the reasons for that is aesthetic: we are concerned mainly with even functions here, so the origin keeps a sense of symmetry. The other main reason is technical: we recall that the operator


T : ℓ2s(N) × ℓ2s(N) → ℓ2s(N) × ℓ2s(N) given by T = (T1,T2), where

- T1({xi},{yi})k = n≥0

(xnan(

√

![image 468](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile468.png>)

k) + yn an(

√

![image 469](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile469.png>)

k)),

- T2({xi},{yi})k = T1({yi},{xi})k,


for k ≥ 0, is the identity when restricted to the set of pairs of sequences satisfying the Poisson summation formula

yn2.

xn2 =

n∈Z

n∈Z

For general sequences, the ﬁrst entries of this operators possess a correction factor due to the lack of Poisson summation. Indeed, it is not diﬃcult to verify that dim(ker(T)) = dim(coker(T)) = 1 from the explicit deﬁnitions. Therefore, we can no longer prove invertibility.

Nonetheless, we also remark that a direct computation shows that the range of T is closed. Therefore, T satisﬁes all conditions to be a Fredholm operator.

Let us then deﬁne a new perturbed operator S deﬁned on ℓ2s(N) × ℓ2s(N), such that

- S1({xi},{yi})k = n≥0

(xnan( k + εk) + yn an( k + εk)),

![image 470](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile470.png>)

![image 471](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile471.png>)

- S2({xi},{yi})k = S1({yi},{xi})k,


for all k ≥ 0, where εk > 0, ∀k ≥ 0. We denote by en ∈ ℓ2s(N) the vector consisting of n−s on the n−th entry, and zero otherwise. With this deﬁnition, the set

{(en,0): n ∈ N} ∪ {(0,en): n ∈ N} forms an orthonormal basis of ℓ2s(N) × ℓ2s(N). Thus,

A 2HS(ℓ2

( A(en,0) 2(s,s) + A(0,en) 2(s,s)),

s(N)×ℓ2s(N)) =

n∈N

where we denote by · (s,s) the norm of ℓ2s(N) × ℓ2s(N). Let then A = I − T.˜

Claim 5.1. A HS(ℓ2

s(N)×ℓ2s(N)) < +∞ holds whenever there is δ > 0 so that |εk| k−54−δ, ∀k ≥ 1.

![image 472](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile472.png>)

Proof of Claim 5.1. As mentioned before, we can write the identity on ℓ2s(N) × ℓ2s(N) as

√

√

![image 473](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile473.png>)

![image 474](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile474.png>)

2),... )), where we deﬁne the function G as in (4.23). With this notation, the operator T˜ becomes

2),... ),(y0, G(1), G(

I({xi},{yi}) = ((x0,G(1),G(

T˜({xi},{yi}) = ((x0,G(√1 + ε1),G(√2 + ε2),... ),(y0, G(√1 + ε1), G(√2 + ε2),... )). Therefore, evaluating at the basis vectors gives us

![image 475](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile475.png>)

![image 476](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile476.png>)

![image 477](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile477.png>)

![image 478](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile478.png>)

√

√

1) − an(√1 + ε1),n−s(an(

2) − an(√2 + ε2)),... ), (0,0,... )).

(I − T˜)(en,0) = ((0,n−s(an(

![image 479](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile479.png>)

![image 480](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile480.png>)

![image 481](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile481.png>)

![image 482](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile482.png>)

We readily see then that

 

I − T˜ 2HS(ℓ2

(1 + k)2s(1 + n)−2s|an(

s(N)×ℓ2s(N)) =

n>0

k≥0

- (5.1)

From Theorem 1.5, we know that

|an(

√

![image 483](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile483.png>)

k) − an( k + εk)| ≤

![image 484](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile484.png>)

√k+εk

![image 485](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile485.png>)

√k

![image 486](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile486.png>)

|a′n(t)|dt

≤

Cεk √

![image 487](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile487.png>)

![image 488](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile488.png>)

k

n3/4e−c

√

![image 489](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile489.png>)

k/n,

- (5.2) for some c > 0 and k ≥ 1. Analogously,


 

√

(1 + k)2s(1 + n)−2s| an(

+

n>0

k≥0

√

Cεk √k

![image 490](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile490.png>)

n3/4e−c

![image 491](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile491.png>)

k) − an( k + εk)| ≤

| an(

![image 492](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile492.png>)

![image 493](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile493.png>)

 

√

![image 494](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile494.png>)

k) − an( k + εk)|2

![image 495](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile495.png>)

 .

![image 496](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile496.png>)

k) − an( k + εk)|2

![image 497](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile497.png>)

√

![image 498](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile498.png>)

k/n.

These estimates plus the condition on the εk imply that (5.1) may be bounded from above by an absolute constant times

 

 n23−2s.

√

![image 499](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile499.png>)

k2sk−25−2δ · k−1e−2c

k/n

![image 500](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile500.png>)

![image 501](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile501.png>)

n≥0

k≥1

In order to prove convergence, we ﬁrst investigate the inner sum. A Riemann sum approach together with a change of variables shows that this is bounded by a constant times

∞

√t dt =: (1 + n)2s−52−2δIs,δ.

t2st−25−2δ · t−1e−c

(1 + n)2s−52−2δ

![image 502](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile502.png>)

![image 503](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile503.png>)

![image 504](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile504.png>)

![image 505](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile505.png>)

0

Clearly, the inner integral converges given that s > 54 + δ. Putting these estimates together with (5.1) and using Fubini, we obtain that

![image 506](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile506.png>)

  < +∞,

 

I − T˜ 2HS(ℓ2

(1 + n)−1−2δ

s(N)×ℓ2s(N)) ≤ Is,δ

n≥0

- as desired.


As a direct corollary, we see that, for each δ > 0, there is a > 0 so that, if |εi| ≤ ai−45−δ ∀ i > 0, then

![image 507](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile507.png>)

s(N)×ℓ2s(N)) < 1. In particular, we shall make use of the fact that T is a Fredholm operator by means of such an inequality, with aid of the following result:

A HS(ℓ2

- Theorem 5.2 (Theorems 2.8 and 2.10 in [26]). Let Φ(X,Y ) denote the set of bounded Fredholm operators between Banach spaces X and Y. If A ∈ Φ(X,Y ) and K ∈ K(X,Y ) is a compact operator, then A + K ∈ Φ(X,Y ) and i(A) = i(A + K), where we deﬁne the index i : Φ(X,Y ) → N by i(A) = dim(ker(A)) − dim(coker(A)) =: α(A) − β(A).

Furthermore, if K op is small enough, then it also holds that α(A + K) ≤ α(A).

Notice that we may write S − T = T˜ − I + K0, where K0 has ﬁnite rank and bounded, and thus also compact. Therefore, S = T + (S − T) = T + (T˜ − I) + K0 can be written as sum of a Fredholm operator T and a compact operator T˜ − I + K0. This already implies that, modulo a ﬁnite-dimensional subspace, the sequences ({f(√k + εk)},{ f(√k + εk)}) determine the sequences ({f(

![image 508](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile508.png>)

![image 509](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile509.png>)

√

![image 510](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile510.png>)

k)},{ f(

√

![image 511](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile511.png>)

k)}). That is, we can determine the function f ∈ Seven(R) from its (Fourier-)values as √k + εk, modulo subtracting functions belonging to a ﬁnite-dimensional space.

![image 512](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile512.png>)

If, however, we make |εk| < ǫk−45−δ, with ǫ small enough, and |ε0| ≪ 1, we get that the operator norms of both I − T˜ = A and K0 can be made arbitrarily small. Thus,

![image 513](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile513.png>)

i(S) = i(T + (S − T)) = i(T) = 0 ⇐⇒ α(S) = β(S), and, moreover,

α(S) ≤ α(T),

- as the Hilbert–Schmidt norm of the diﬀerence is small. Thus, either

- α(S) = β(S) = 0,

in which case we can perfectly invert the operator S, or

- α(S) = β(S) = 1,


which implies that there is essentially at most one function f0 ∈ Seven(R) that vanishes

- at √k + εk. As ({f(√k + εk)},{ f(√k + εk)}) ∈ im(S) for every real f ∈ Seven(R), we have proved the followin result.


![image 514](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile514.png>)

![image 515](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile515.png>)

![image 516](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile516.png>)

- Theorem 5.3. Let T,S,{εi}i≥0 be as above. Then one of the following holds:


- (1) Either S is an isomorphism from ℓ2s(N)×ℓ2s(N) onto itself, and thus the values ({f( j + εj)},{ f( j + εj)})


![image 517](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile517.png>)

![image 518](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile518.png>)

- determine any real function f ∈ Seven(R);
- (2) Or ker(S) has dimension one, and therefore S is an isomorphism from ker(S)⊥ onto im(S).


In particular, any real function f ∈ Seven(R) is uniquely determined by

![image 519](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile519.png>)

![image 520](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile520.png>)

({f( j + εj)},{ f( j + εj)}), together with the value of

![image 521](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile521.png>)

![image 522](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile522.png>)

({f( j + εj)},{ f( j + εj)}),({αi},{βi}) (s,s) ({αi},{βi}) 2(s,s)

,

![image 523](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile523.png>)

where ({αi},{βi}) ∈ ker(S) is a generator for the kernel of S.

Notice that the ﬁrst option in Theorem 5.3 yields immediately an interpolation formula, in the spirit of (4.24). For the second one, the operator is now only invertible if restricted to ker(S)⊥, and now the process of recovering f ∈ Seven(R : R) has to take into account the inner product with the kernel vector and the structure of the range.

- 5.2. Uniqueness for small powers of integers. Let α ∈ (0,1/2). We are interested


in determining when the only function f ∈ Seven(R) that vanishes together with its Fourier transform at ±nα is the identically zero function.

Indeed, we would like to study the natural operator that sends the sequence of values

- at the roots of integers ({f(√k)}k,{ f(√k)}k}) to the sequence ({f(nα)}n,{ f(nα)}n). Our goal is to show that this operator is injective. In order to do that, we will ﬁrst study simpler operators.


![image 524](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile524.png>)

![image 525](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile525.png>)

Indeed, let K0 ∈ N be a ﬁxed positive integer. Fix a set of 2K0 positive real numbers t1 < t2 < ··· < t2K0 such that t1 > √K0 and none of the tj can be written as a square root of a positive integer. We ﬁx s > 0 suﬃciently large and deﬁne the operator

![image 526](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile526.png>)

TK0 : ℓ2s(N) × ℓ2s(N) →ℓ2s(N) × ℓ2s(N) ({xi}i,{yi}i)  →((x0,G(t1),G(t2),... ,G(t2K0),xK0+1,xK0+2,... ), (y0, G(t1), G(t2),... , G(t2K0),yK0+1,yK0+2,... )).

Here, we denoted by G the function deﬁned as in (4.23).

- Lemma 5.4. For any K0 ≥ 1, the operator TK0 is bounded and injective.


Proof. We begin with the boundedness assertion. As TK0 diﬀers only in the ﬁrst K0 coordinates from an interation of the shift operator

s(({xi}i,{yi}i) = ((0,x0,x1,... ),(0,y0,y1,... )),

boundedness follows from boundedness of the operator that maps a pair of sequences ({xi}i,{yi}i) ∈ ℓ2s(N) × ℓ2s(N) into

((x0,G(t1),G(t2),... ,G(t2K0),0,... ), (y0, G(t1), G(t2),... , G(t2K0),0,... )).

As G, G ∈ L∞(R) for any pair of sequences {xi},{yi}, with bounds depending only on the ℓ2s(N)−norms of the sequences, it follows that this new ﬁnite-rank operator is bounded.

The injectivity part is subtler. Indeed, ﬁx a pair of sequences ({xi},{yi}) ∈ ℓ2s(N)× ℓ2s(N), and suppose that TK0({xi},{yi}) = 0. It follows that the special function G(t) is a linear combination of a1,... ,aK0, a1,... , aK0. In order to analyze such functions, we will need to investigate further the intrinsic form of the interpolating functions an, and thus those of b±n .

Indeed, it follows from the Fourier expansion of gn± near inﬁnity and the formula

1

- 1

![image 527](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile527.png>)

- 2


gn±(z)eπix2z dz that, whenever |x| > √n, it can also be represented as

b±n (x) =

−1

![image 528](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile528.png>)

∞

gn±(1 + it)e−πx2t dt.

b±n (x) = sin(πx2)

0

As an = (b+n + b−n )/2 and an = (b+n − b−n )/2, we see that the Fourier invariant part of our function g may be written as

 e−πx2t dt,

 

K0

∞

αjgj+(1 + it)

(G + G)(x) = sin(πx2)

0

j=1

for some sequence αj of real numbers, and an analogous identity holds for the −1eigenvalue part G− G, with gn− instead. We recall that the weakly holomorphic modular forms gn± satisfy that

gn+(z) = θ(z)3Pn+(1/J(z)), gn−(z) = θ(z)3(1 − 2λ(z))Pn−(1/J(z)),

where the monic polynomials Pn−,Pn+ are of degree n. Therefore, there are polynomials

- Q,R of degree ≤ K0 such that


∞

θ(1 + it)3Q(1 + it)e−πx2t dt

G + G = sin(πx2)

0

∞

θ(1 + it)3(1 − 2λ(1 + it))R(1 + it)e−πx2t dt.

G − G = sin(πx2)

0

- (5.3) Before moving forward, we need the following result:


- Lemma 5.5. The factors θ(1 + it)3 and (1 − 2λ(1 + it)) do not change sign for t ∈ (0,∞), and the function 1/J(1 + it) is real-valued and monotonic for t ∈ (0,∞). Proof. By using (2.1), we get that


(−1)ne−πn2t =

e−4πn2t −

e−π(2n+1)2t.

θ(1 + it) =

n∈Z

n∈Z

n∈Z

We now consider the function ft(x) = e−π(2x)2t. Then the sum above equals

ft(n) −

ft(n + 1/2).

n∈Z

n∈Z

By the Poisson summation formula, the diﬀerence above equals

2

2

2

1 √t n odd

- 1

![image 529](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile529.png>)

- 2√t n∈Z


n 2√t

n 2√t

n 2√t

e−π

eπine−π

e−π

![image 530](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile530.png>)

![image 531](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile531.png>)

![image 532](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile532.png>)

=

−

≥ 0.

![image 533](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile533.png>)

![image 534](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile534.png>)

![image 535](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile535.png>)

![image 536](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile536.png>)

![image 537](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile537.png>)

![image 538](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile538.png>)

n∈Z

This proves the ﬁrst assertion.

For the second, we simply see from (2.2) that λ(1+z) has only nonpositive coeﬃcients in its q−series expansion. This implies that λ(1 + it) is nonpositive por t ∈ (0,∞), which implies that 1 − 2λ(1 + it) is always nonnegative.

Finally, for the third assertion, we notice that, as J(1+z) = 161 λ(1+z)(1−λ(1+z)), and thus, from the analysis above, the q−series expansion of J(1 + z) contains only nonpositive coeﬃcients. Therefore, the function J(1+1 it) is nonpositive for t ∈ (0,∞), and it is monotonically decreasing there. This ﬁnishes the proof.

![image 539](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile539.png>)

![image 540](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile540.png>)

By Lemma 5.5, we get that the part of the integrand in the expressions above multiplying the e−πx2t factor changes sign at most K0 + 1 times. Notice that we can embed both integrals in (5.3) into the framework of Laplace transforms: denoting

Q(t) = θ(1 + it)3Q(1 + it), R(t) = θ(1 + it)3(1 − 2λ(1 + it))R(1 + it), we are interested in studying the positive zeros of L[Q](πx2),L[R](πx2), where L[φ](s) =

∞

φ(t)e−st dt

0

denotes the Laplace transform of φ evaluated at the point s. We may reduce even further our task to studying the positive zeros of L[Q],L[R]. The following result, a version of the Descartes rule for the Laplace transform, is the tool we need to bound the number of positive zeros of such expressions as a function of their number of changes of signs.

Proposition 5.6 (Descartes rule for the Laplace transform). Let φ : R → R be a smooth function such that its Laplace transform L[φ] converges on some open halfplane Re(s) > s0. Then the number of zeros of L[φ] on the interval (s0,+∞) is at most the number of sign changes of φ.

Proof. The proof follows by induction on the number of sign changes of the function φ. Indeed, if φ ≥ 0, it follows easily that the Laplace transform L[φ] ≥ 0, with equality if and only if φ ≡ 0.

Suppose now that φ changes sign n + 1 times on (0,∞). Number its zeros on the positive half-line as s0 < s1 < ··· < sn. Then L[φ] has as many zeros as es0tL[φ](t) = F(t). The derivative of F is then given by

F′(t) = −

∞

(s − s0)φ(s)e−(s−s0)t ds = es0tL[(s − s0)φ(s)](t).

0

Notice that the new smooth function (s − s0)φ(s) still satisﬁes the same properties as φ, but now has exactly n sign changes. By inductive hypothesis, F′ has at most n zeros, which, by the mean value theorem, implies that F has at most n+1 zeros. This ﬁnishes the proof.

Using this claim for Q,R, we see that their respective Laplace transform possess at most K0 zeros on the interval (√K0,+∞). With this information, we can already ﬁnish: from (5.3), the functions G ± G can only vanish at at most K0 points on the interval (√K0,∞) which are not roots of positive integers, in case G  ≡ 0. But, according to our asumption that ({xi},{yi}) ∈ ker(TK0), we have G(tj) = G(tj) = 0,j = 1,... ,2K0. By the properties we chose for the sequence tj, G ≡ 0, and thus the map TK0 is injective.

![image 541](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile541.png>)

![image 542](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile542.png>)

We need one more result in order to use our methods to infer results about uniqueness for small powers of integers. In contrast to the full perturbation case of our main theorem, we must prove that the injective operators TK0 are also somewhat stable with respect to injectivity under perturbations. In order to do this, the following result is essencial.

Lemma 5.7. The range of TK0 is closed.

Proof. Suppose the sequence in ℓ2s(N)×ℓ2s(N) given by {TK0({xji},{yij})}j≥0 is a Cauchy sequence. This implies that the sequence {{xji}i=0,K0+1,...,{yij}i=0,K0+1,...}j≥0 is a Cauchy sequence, and therefore it converges to a certain limiting sequence

{{xi}i=0,K0+1,...,{yi}i=0,K0+1,...} ∈ ℓ2s(N) × ℓ2s(N). Deﬁne, thus, the 4K0 × 2K0 matrix AK0 given by taking

(a1(tj),a2(tj),... ,aK0(tj), a1(tj), a2(tj),... , aK0(tj)) and

( a1(tj), a2(tj),... , aK0(tj),a1(tj),a2(tj),... ,aK0(tj)) to be its lines, for j = 1,... ,2K0. We ﬁrst claim that this matrix is injective. Indeed,

K0

G˜(t) =

(xiai(t) + yi ai(t))

i=1

vanishes, together with its Fourier transform, at tj,j = 1,... ,2K0, where ({xi}Ki=10 ,{yi}Ki=10 ) belongs to ker(AK0). By the proof of Lemma 5.4, this implies xi = yi = 0,i = 1,··· ,K0.

As AK0is injective, there is a constant cK0 > 0 so that

- (5.4) AK0v 4K0 ≥ cK0 v 2K0,


where we denote by   ·  d the usual euclidean norm on a d−dimensional space. Translating to our original problem, as {TK0({xji},{yij})}j≥0 is a Cauchy sequence in ℓ2s(N)× ℓ2s(N),

{{xji}i=0,K0+1,...,{yij}i=0,K0+1,...}j≥0 is a convergent sequence, and thus we get that the sequences

K0

(xki ai(tj) + yik ai(tj)), j = 1,... ,2K0

i=1

are also Cauchy in k ≥ 0. By (5.4), ({xki }Ki=10 ,{yi}Ki=10 )k≥0 is Cauchy. This implies that there is a limiting sequence ({xi},{yi}) ∈ ℓ2s(N) × ℓ2s(N) so that

TK0({xji},{yij}) → TK0({xi},{yi}), as j → ∞. This ﬁnishes the proof.

We are ﬁnally able to prove the following uniqueness result:

- Corollary 5.8. Let α ∈ (0, 29). There exists cα > 0 so that ∀c < cα, if f ∈ Seven(R) is a real function that vanishes together with its Fourier transform at ±cαnα, then f ≡ 0.


![image 543](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile543.png>)

Proof. We start by noticing that, whenever n ∈ N is suﬃciently large, then there is

√n − cmα| cα1 nα2−α1. Indeed, we simply let m = ⌊(n/c2)21α⌋. We get that

![image 544](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile544.png>)

- m ∈ N so that |


![image 545](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile545.png>)

![image 546](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile546.png>)

![image 547](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile547.png>)

(n/c2)1/(2α)

√n − cmα| = cα

tα−1 dt c1/ααnα2−α1.

![image 548](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile548.png>)

|

![image 549](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile549.png>)

⌊(n/c2)1/(2α)⌋

In particular, if α2−α1 < −45 − 21 ⇐⇒ α < 29, then for all n ≥ n0(α), there exists m ∈ N so that we can write mα = √n + εn, where εn satisﬁes the conditions of Theorem 1.4. Let us single out the sequence of numbers selected above, which we index as

![image 550](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile550.png>)

![image 551](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile551.png>)

![image 552](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile552.png>)

![image 553](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile553.png>)

![image 554](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile554.png>)

{m(n)α}n≥n0(α). We then consider the operator Tn0(α) associated to some sequence of 2n0(α) positive real numbers tj,j = 1,... ,2n0(α), satisfying the hypotheses of Lemma

- 5.4. We claim that the perturbed operator


T˜n0(α) : ℓ2s(N) × ℓ2s(N) → ℓ2s(N) × ℓ2s(N) ({xi},{yi})  → ((x0,G(t1),G(t2),... ,G(t2n0),G(m(n0 + 1)α),G(m(n0 + 2)α),... ), (y0, G(t1), G(t2),... , G(t2n0), G(m(n0 + 1)α), G(m(n0 + 2)α),... ))

- (5.5)


is injective. Indeed, from Lemma 5.7 there must exist a constant Cn0 so that Tn0v (s,s) ≥ Cn0 v (s,s)

holds for all v ∈ ℓ2s(N) × ℓ2s(N). But, by the same calculation as in the previous subsection, we have that

T ˜n0(α) − Tn0(α) HS(ℓ2

s(N)×ℓ2s(N)) < Cn0/2

holds, as long as we take α < 29 and c = c(α) suﬃciently small. This implies, in particular, that

![image 555](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile555.png>)

Cn0 2

T ˜n0v |(s,s) ≥

v (s,s), for each v ∈ ℓ2s(N) × ℓ2s(N), and thus the operator T˜n0 is, indeed, injective, as desired.

![image 556](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile556.png>)

In order to conclude, we notice that the operator Tn0(α) : ℓ2s(N) × ℓ2s(N) → ℓ2s(N) × ℓ2s(N) ({xi},{yi})  → ((x0,G(ck1α),G(ck2α),... ,G(ck2αn0),G(m(n0 + 1)α),G(m(n0 + 2)α),... ), (y0, G(ck1α), G(ck2α),... , G(ck2αn0), G(m(n0 + 1)α), G(m(n0 + 2)α),... ))

- (5.6)


for some sequence kj,j = 1,... ,2n0 of integers not belonging to the sequence m(n) we selected above, is still injective. In fact, it only diﬀers from the operator T˜n0 in at most the ﬁrst 2n0 entries. But, on the other hand, for kj = ⌊(tj/c)1/α⌋,j = 1,... ,2n0, and c > 0 suﬃciently small, we see that

∞

(xi|ai(tj) − ai(ckjα)| + yi| ai(tj) − ai(ckjα)|)

|G(ckjα) − G(tj)| ≤

i=0

∞

i5/2(|xi| + |yi|)

|tj − ckjα|

sup

j∈[0,2n0]

i=0

ǫ ({xi},{yi}) (s,s).

For ǫ > 0 suﬃciently small, we see from the previous argument that Tn0(α) still has closed range and is injective. This readily implies that the sequence ({f(±nα)},{ f(±nα)}) determines uniquely the sequence ({f(√n)},{ f(√n)}). This ﬁnishes the proof.

![image 557](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile557.png>)

![image 558](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile558.png>)

One can inquire about the importance of such a result, as in [25] we have shown that the uniqueness result stated in Corollary 5.8 hold for α ∈ (0,1 −

√2/2), which is signiﬁcantly larger than the range stated here. Nonetheless, Corollary 5.8 gives us automatic results. Indeed, if one manages to prove that for all δ > 0 there is ǫ > 0 so that, if |εk| ≤ ǫ, ∀k ∈ N, then

![image 559](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile559.png>)

I − T˜ op < δ, it implies automatically that we can extend the results in Corollary 5.8 to the full diagonal range α ∈ (0,1/2).

We also note that Corollary 5.8 is not all we can say about the problem of determining the best exponents (α,β) so that

f(±nα) = f(±nβ) = 0, f ∈ Seven(R) ⇒ f ≡ 0. Indeed, we can easily go further than the diagonal case exposed above: if α,β ∈ (0,2/9) are an arbitrary pair of exponents, we notice that we can still pick n0 ∈ N so that for each n > n0 = n0(α,β), there exists a pair (m1(n),m2(n)) ∈ N2 so that

√n| + |cm2(n)β −

√n| c1/ααnα2−α1 + c1/ββn

β−1

|cm1(n)α −

![image 560](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile560.png>)

![image 561](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile561.png>)

2β .

![image 562](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile562.png>)

![image 563](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile563.png>)

This induces us to consider the operator Tn0(α,β) : ℓ2s(N) × ℓ2s(N) → ℓ2s(N) × ℓ2s(N) ({xi},{yi})  → ((x0,G(ck1α),G(ck2α),... ,G(ck2αn0),G(m1(n0 + 1)α),G(m1(n0 + 2)α),... ), (y0, G(cl1β), G(cl2β),... , G(cl2βn

), G(m2(n0 + 1)β), G(m2(n0 + 2)β),... ))

0

- (5.7)


for two sequences of integers (kj,lj),j = 1,... ,2n0, so that |tj − ckjα| + |tj − cljβ| is suﬃciently small for all j ∈ [0,2n0], where we select tj,j = 1,... ,2n0 satisfying the hypotheses of Lemma 5.4.

By the same strategy outlined in the proof of Corollary 5.8, the Hilbert-Schmidt

norm as operators acting on ℓ2s(N) × ℓ2s(N) of the diﬀerence Tn0(α,β) − Tn0(α,β) is arbitrarily small, as long as we make the value of c = c(α,β) smaller. As a consequence,

Tn0 is also injective and its range is closed. These considerations prove, therefore, the following:

- Corollary 5.9. Let α,β ∈ (0,2/9). Then there is cα,β > 0 so that for all c < cα,β, if f ∈ Seven(R) is a real function that vanishes at ±cnα and its Fourier transform vanishes at ±cnβ, then f ≡ 0.


Remark. In the end, we do not quite attain the primary goal of this section of proving Fourier uniqueness results for the sequences ({±nα},{±nβ}), but only a slightly weaker version of it, with a small constant c(α,β) in front. The main reason for that in the proofs above is the location of the positive reals ti : although their exact values do not matter in the end, it is crucial, in order to use Proposition 5.6, that they lie after the node n0. We must therefore either force n0 not to be too large in order not to make the norm of the matrix AK0 too small, or ﬁx them from the beginning and make the perturbations of TK0 fall closer to it. In any case, this implies nontrivial use of the constant c multiplying the sequences ({±nα},{±nβ}).

We believe that further studying operators resembling TK0 above and their injectivity properties could yield better results in this regard. In order not to make this exposition even longer, we will not pursue this matter any further.

- 5.3. The Cohn-Kumar-Miller-Radchenko-Viazovska result and perturbed interpolation formulae with derivatives. As another illustration of our main technique, we prove that the interpolation formulae with derivatives in dimension 8 and 24 from [10] can be suitably perturbed.


Indeed, we ﬁrst recall one of the main results of [10]: let (d,n0) be either (8,1) or (24,2). Then every f ∈ Srad(Rd) can be uniquely recovered by the sets of values

√

√

√

√

2n),f′(

2n), f′(

![image 564](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile564.png>)

![image 565](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile565.png>)

![image 566](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile566.png>)

![image 567](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile567.png>)

{f(

2n), f(

2n)}, n ≥ n0,

through the interpolation formula f(x) =

√

√

f′(

![image 568](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile568.png>)

![image 569](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile569.png>)

2n)an(x) +

2n)bn(x)

f(

n≥n0

n≥n0

√

√

f′(

![image 570](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile570.png>)

![image 571](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile571.png>)

+

f(

2n) an(x) +

2n) bn(x).

n≥n0

n≥n0

- (5.8)

We also have uniform estimates on the functions an, an,bn, bn : indeed, there is τ > 0 so that

- (5.9) sup l∈{0,1,2}

sup

x∈Rd

(1 + |x|)100 |an(l)(x)| + | an(l)(x)| + |bn(l)(x)| + | bn(l)(x)| nτ,

for all n ∈ N. Here and throughout this section, we shall denote by g′(x) the derivative of the (radial) function g regarded as a one-dimensional function.

By [10, Theorem 1.9], we know that the matrices

- (5.10) Mn(x) =






an(x) a′n(x) an(x) an′(x) bn(x) b′n(x) bn(x) bn′(x) an(x) an′(x) an(x) a′n(x) bn(x) bn′(x) bn(x) b′n(x)

 

 

satisfy that Mn(√2m) = δmnI4×4. As we know that the map that takes a vector of suﬃciently rapidly decaying sequences

![image 572](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile572.png>)

({αn},{βn},{α˜n},{β˜n}) onto the function

αnan(x) + βnbn(x) + α˜n an(x) + β˜n bn(x)

f(x) =

n≥n0

is, in fact, injective (and moreover an isomorphism if we consider the set of all arbitrarily rapidly decaing sequences), we shall make use of this function in our estimates. Indeed, we have that the map that takes the quadruple of sequences

({αn},{βn},{α˜n},{β˜n}) onto

√

√

√

√

2n),f′(

2n), f′(

![image 573](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile573.png>)

![image 574](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile574.png>)

![image 575](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile575.png>)

![image 576](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile576.png>)

(f(

2n))n≥n0 is, in fact, the identity. Another way to represent this map is as the series

2n), f(

√

(αn,βn,α˜n,β˜n) · Mn(

![image 577](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile577.png>)

2n).

n≥n0

We deﬁne, therefore, the operator that takes the same quadruple onto (f(√2n + εn),f′(√2n + εn), f(√2n + εn), f′(√2n + εn))n≥n0. In the alternative notation, this operator, which we shall denote by T, is given by

![image 578](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile578.png>)

![image 579](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile579.png>)

![image 580](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile580.png>)

![image 581](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile581.png>)

(αn,βn,α˜n,β˜n) · Mn(√2n + εn).

![image 582](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile582.png>)

n≥n0

As before, we seek to prove that T is invertible when deﬁned over some space

ℓ2s(N) × ℓ2s(N) × ℓ2s(N) × ℓ2s(N) =: (ℓ2s(N))4, where we may take s ≫ 1 suﬃciently large. As our aim here is not to establish the sharpest possible results, but only to prove that we may perturb the aforementioned interpolation formulae, we shall make use of the Hilbert–Schmidt test, as in §5.1 above. Indeed, we wish to prove that

s(N))4) < 1. A simple computation with the Hilbert–Schmidt norm using (5.10) shows that this quantity is bounded by

I − T HS((ℓ2

√

√

2m) − an(√2m + εm)|2 + | an(

2m) − an(√2m + εm)|2+

m2sn−2s((|an(

![image 583](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile583.png>)

![image 584](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile584.png>)

![image 585](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile585.png>)

![image 586](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile586.png>)

m,n>0

- + |a′n(

√

![image 587](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile587.png>)

2m) − a′n(√2m + εm)|2 + | an′(

![image 588](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile588.png>)

√

![image 589](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile589.png>)

2m) − an′(√2m + εm)|2+ |bn(

![image 590](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile590.png>)

√

![image 591](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile591.png>)

2m) − bn(√2m + εm)|2 + | bn(

![image 592](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile592.png>)

√

![image 593](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile593.png>)

2m) − bn(√2m + εm)|2+

![image 594](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile594.png>)

- + |b′n(


√

√

2m) − b′n(√2m + εm)|2 + | bn′(

![image 595](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile595.png>)

![image 596](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile596.png>)

2m) − bn′(√2m + εm)|2).

![image 597](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile597.png>)

![image 598](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile598.png>)

By (5.9) and the mean value theorem, the sum above is bounded by (an absolute constant times)

m2sn−2s × m−100n2τε2m. The sum above is representable as a product of a sum in m and one in n. The one in

m,n>0

- n is convergent if s > τ + 1. We then ﬁx such a value of s. For such values, the second sum is


m2s−100ε2m,

m>0

which converges in case εm m49−s. For all such sequences, the diﬀerence I − T is a Hilbert–Schmidt operator. Moreover, if εm ≤ δm49−s for δ > 0 suﬃciently small, we will have I − T HS(ℓ2

s(N)4) < 1. Summarizing, we have shown the following result:

- Theorem 5.10. There is C0 > 0 so that the following holds: there is δ > 0 so that, for each sequence εk so that |εk| < δk−C0, then any function f ∈ Srad(Rd) is uniquely determined by the values


- (5.11) f(√2n + εn),f′(√2n + εn), f(√2n + εn), f′(√2n + εn) n≥n0


![image 599](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile599.png>)

![image 600](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile600.png>)

![image 601](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile601.png>)

![image 602](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile602.png>)

, where we let (d,n0) = (8,1) or (24,2).

In the same spirit of §4.2, one can obtain an interpolation formula with the values

- (5.11) from Theorem 5.10. We remark that, in the same way that we undertook our analysis for the Radchenko-


Viazovska interpolating functions, we expect the functions an,bn in [10, Theorem 1.9] should also satisfy some exponential-like decay. This fact, although possible, should be sensibly more technically involved than Theorem 1.5, due to the more complicated

nature of the construction of the interpolating functions with derivatives in dimensions 8 and 24.

- 5.4. Perturbed interpolation formulae for odd functions. Finally, in the same spirit of the results in Section 4, we brieﬂy comment on interpolation formulae for odd functions. Recall the following results from [24, Section 7]:


- Theorem 5.11 (Theorem 7 in [24]). There exist sequences of odd functions d±m : R →


- R, m ≥ 0, belonging to the Schwartz class so that d±m = (∓i)d±m, d±m(√n) = δn,m√n, n ≥ 1.


![image 603](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile603.png>)

![image 604](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile604.png>)

+ m(x)

Moreover, limx→0 d

x = δ0m. These functions satisfy the uniform bound |d±n (x)| n5/2, ∀x ∈ R,n ≥ 0, and, ﬁnally, for each odd and real Schwartz function f : R → R,

![image 605](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile605.png>)

- (5.12) f(x) = d+0 (x)

f′(0) + i f′(0) 2

![image 606](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile606.png>)

+

n≥1

cn(x)

f(√n) √n − cn(x)

![image 607](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile607.png>)

![image 608](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile608.png>)

![image 609](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile609.png>)

f(√n) √n

![image 610](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile610.png>)

![image 611](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile611.png>)

![image 612](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile612.png>)

,

where cn = (d+n +d−n)/2, and the right-hand side of the sum above converges absolutely.

As a direct consequence, we see that any real, odd, Schwartz function on the real line is determined uniquely by the union of its values at √n and the values of its Fourier transform at √n with f′(0) and f′(0). By employing the results in Section 4, we will show that we can actually recover any such function from {f(√n + εn)}n≥1 ∪ { f(√n + εn)}n≥1 ∪ {f′(0)} ∪ { f′(0)} instead.

![image 613](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile613.png>)

![image 614](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile614.png>)

![image 615](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile615.png>)

![image 616](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile616.png>)

Indeed, ﬁrst of all, we start by noticing that the same techniques employed to reﬁne the uniform estimates from Radchenko–Viazovska [24] can be applied to the functions d±m, as they are deﬁned in a completely analogous way to the b±n from Section 4. By carrying out the same kind of estimates, we are able to obtain

- (5.13) |d±n (x)| n3/4 log3/2(1 + n)e−c′|x|/


√n, ∀x ∈ R, n ≥ 1,

![image 617](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile617.png>)

for some absolute constant c′ > 0. By the same analysis of the ∂x−partial derivative of the generating function used in §4.1, this readily implies that the derivatives of the d±n satisfy morally the same decay; in fact, |(d±n )′(x)| n5/4 log3/2(1 + n)e−c′′|x|/

√n, ∀x ∈ R, n ≥ 1, with c′′ > 0 another absolute constant.

![image 618](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile618.png>)

We consider now the operator that takes a pair of sequences ({αn},{βn}) ∈ ℓ2s(N)× ℓ2s(N), s > 0 to be chosen, into

 

 

(αn,βn)Cn(√m + εm)

![image 619](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile619.png>)

,

 n≥0



m≥0

cn√(nx) − cn√(nx) cn√(nx)

cn√(nx)

![image 620](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile620.png>)

![image 621](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile621.png>)

![image 622](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile622.png>)

![image 623](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile623.png>)

. Let us denote this operator by V.

where we abbreviate Cn(x) =

![image 624](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile624.png>)

![image 625](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile625.png>)

![image 626](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile626.png>)

![image 627](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile627.png>)

2)

From (5.12) and the fact that the function d+0 (x) = sin(πx

sinh(πx) vanishes together with its Fourier transform at ±

![image 628](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile628.png>)

√n, n ∈ N, we know that the identity operator on ℓ2s(N)×ℓ2s(N)

![image 629](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile629.png>)

may be written as    n≥0

 

(αn,βn)Cn(√m)

![image 630](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile630.png>)

.



m≥0

Therefore, the techniques from §4.2, §5.3 and 5.1, together with our previous considerations in this subsection, allow us to deduce the following result:

- Theorem 5.12. There is δ > 0 so that, in case |εn| ≤ δn−47, then for each f ∈ Sodd(R) real, the values


![image 631](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile631.png>)

f(√1 + εn),f(√2 + ε2),... and

![image 632](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile632.png>)

![image 633](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile633.png>)

f(√1 + εn), f(√2 + ε2),... allow us to recover uniquely the values f(1),f(√2),f(√3),... and

![image 634](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile634.png>)

![image 635](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile635.png>)

![image 636](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile636.png>)

![image 637](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile637.png>)

f(1), f(√2), f(√3),... . In particular, given the values

![image 638](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile638.png>)

![image 639](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile639.png>)

{f(√n + εn)}n≥1 ∪ { f(√n + εn)}n≥1 ∪ {f′(0)} ∪ { f′(0)}, we can uniquely recover any real function f ∈ Sodd(R).

![image 640](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile640.png>)

![image 641](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile641.png>)

As previously mentioned, we do not carry out the details here, for their similarities with the proof of theorems 1.5 and 1.4.

6. Comments and Remarks

In this section, we gather some remarks about the problems and techniques discussed, as well as state some results we expect to be true.

- 6.1. Maximal perturbed Interpolation Formulae for Band-limited functions. In Section 3, we have seen how our basic functional analysis techniques can be employed in order to deduce new interpolation formulae for band-limited functions. Although Kadec’s proof also uses the basic fact that, whenever a perturbation of the identity is suﬃciently small, then we can basically ‘invert’ an operator, he then proceeds to ﬁnd that the set of exponentials {exp(2πi(n + εn)x)}n≥0 is a Riesz basis for L2(−1/2,1/2)


if supn |εn| < 1/4 by means of orthogonality considerations. Indeed, one key strategy in his estimates is to expand in the diﬀerent complete orthogonal system

{1,cos(2πnt),sin((2n − 1)πt)}n≥1

and use the properties of this expansion. Our results, as much as they do not come so close to Kadec’s threshold, follow a slightly diﬀerent path: instead of using the orthogonality of a diﬀerent system, we choose to work directly with discrete analogues of the Hilbert transform and estimate over those. Although we do not reach – by a 0.011 margin – the sharp 1/4−perturbation result, one advantage of our approach is that it yields bounds for perturbing any kind of interpolation formulae with derivatives. Indeed, following the line of thought of Vaaler, many authors have investigated the property of recovering the values of a function f ∈ L2(R) band-limited to [−k/2,k/2] from the values of its (k − 1)−ﬁrst derivatives (see, e.g., [20] and [12]). Our approach

in §3 in order to prove Theorem 1.3 generalizes easily to the case of several derivatives by an easy modiﬁcation. It can be summarized as follows:

Theorem 6.1. There is L(k) > 0 so that if supn∈Z |εn| < L(k), then any function f ∈ L2(R) band-limited to [−k/2,k/2] is uniquely determined by the values of

f(l)(n + εn), n ∈ Z,l = 0,1,... ,k − 1.

A natural question that connects our results to Kadec’s results is about the best value of L(k) so that Theorem 6.1 holds. We do not have evidence to back any concrete conjecture, but we ﬁnd possible that the threshold L(k) = 14 is kept for higher values of k ∈ N. We speculat that, in order to prove such a result, one would need to ﬁnd an appropriate hybrid of our techniques and Kadec’s techniques (see for instance Section

![image 642](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile642.png>)

- 10 in [33, Chapter 1]), taking into account properties of the discrete Hilbert transforms as well as orthogonality results.


- 6.2. Theorem 1.5, optimal decay rates for interpolating functions and maximal perturbations. In Theorem 1.5, we have improved the uniform bound obtained by Radchenko and Viazovska [24] and, more recently, the sharper uniform bound by


Bondarenko, Radchenko and Seip [3] on the interpolating functions an to one that decays with x; namely, we have that

|an(x)| n1/4 log3/2(1 + n) e−c|x|2/n1|x|<Cn + e−c|x|1|x|>Cn , holds for all n ∈ N, where C,c > 0 are two ﬁxed positive constants. Although this improves the decay rates from before, the power n1/4 found here and in [3] in the growth seems likely not to be optimal; to that regard, we pose the following:

Question 1. What is the best decay rate for an as in Theorem 1.5? Can one prove that supx∈R |an(x)| = O(1) in n?

This conjectured growth seems to be the best possible, due to the recent ﬁndings of Bondarenko–Radchenko–Seip [3], which show that, for each N ≫ 1, the average

1

N + 1 k≤N |ak(x)|2 grows slower than some power of log N.

![image 643](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile643.png>)

Notice that, by a simple modiﬁcation of the computations made in §4.2, an aﬃrmative answer to Question 1 yields an immediate improvement in the range of εi that we allow for the theorems in 4.2. Indeed, we get automatically that |εi| i−1 is allowed in such results. On the other hand, this seems to be the best possible result one can achieve with our current methods, as the mean value theorem implies that supx∈R |a′n(x)|

√n.

![image 644](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile644.png>)

In particular, all indicates that one needs a new idea in order to prove the following conjecture:

- Conjecture 6.2 (Maximal perturbations). Let f ∈ Seven(R) be a real function. Then there is θ > 0 so that, if |εi| < θ, ∀ i ∈ N, f can be uniquely recovered from its values

f(0),f(√1 + ε1),f(√2 + ε2),... , together with the values of its Fourier transform

![image 645](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile645.png>)

![image 646](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile646.png>)

f(0), f(√1 + ε1), f(√2 + ε2),... .

![image 647](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile647.png>)

![image 648](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile648.png>)

It might not be an easy task to prove Conjecture 6.2 even with a new idea starting from our techniques, but we believe that the following version stands a chance of being more tractable with the current methods:

- Conjecture 6.3 (Maximal perturbations, weak form). Let f ∈ Seven(R) be a real function. Then, for each a > 0, there is δ > 0 so that, if |εi| ≤ δk−a, then f can be uniquely recovered from its values


f(0),f(√1 + ε1),f(√2 + ε2),... , together with the values of its Fourier transform

![image 649](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile649.png>)

![image 650](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile650.png>)

f(0), f(√1 + ε1), f(√2 + ε2),... .

![image 651](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile651.png>)

![image 652](<2020-ramos-perturbed-interpolation-formulae-applications_images/imageFile652.png>)

In this framework, the results in §4.2 may be regarded as partial progress towards this conjecture. Notice that, by the remarks of §5.2, both versions of the conjecture imply that for each α ∈ (0,1/2), there is cα > 0 so that if an even, real Schwartz function f satisﬁes that f(c1nα) = f(c2nβ) = 0 and c1 < cα, c2 < cβ, then f ≡ 0. These results can be compared, for instance, with our previous results in [25].

Acknowledgements

We would like to thank Danylo Radchenko for several comments and suggestions in both early and later stages of development of this manuscript. We would also like to thank Felipe Gonc¸alves for helpful discussions that led to the development of §5.1. Finally, J.P.G.R. acknowledges ﬁnancial support from CNPq.

References

- [1] A Avantaggiati, P. Loretti, and P. Vellucci, Kadec-1/4 Theorem for sinc bases, preprint at arXiv:1603.08762.
- [2] B. C. Berndt and M. I. Knopp, Hecke’s Theory of Modular Forms and Dirichlet Series, World Scientiﬁc (2008).
- [3] A. Bondarenko, D. Radchenko and K. Seip, Fourier Interpolation with zeros of Zeta and L−functions, preprint at arXiv:2005.02996.
- [4] J. Bourgain, L. Clozel, and J.-P. Kahane, Principe d’Heisenberg et fonctions positives. Ann. Inst. Fourier (Grenoble) 60 (2010), no. 4, 1215–1232.
- [5] H. Brezis, Functional Analysis, Sobolev Spaces and Partial Diﬀerential Equations. Universitext, Springer–Verlag, 2011.
- [6] K. Chandrasekharan Elliptic Functions, Grundlehren der mathematischen Wissenschaften 281, Springer-Verlag, 1985.
- [7] J. Chung, S.-Y. Chung and D. Kim, Characterizations of the Gelfand-Shilov spaces via Fourier transforms, Proc. Amer. Math. Soc. 124 (1996), no. 7, 2101–2108.


- [8] H. Cohn and F. Gonc¸alves, An optimal uncertainty principle in twelve dimensions via modular forms, Invent. Math. 217 (2019), no. 3, 799–831.
- [9] H. Cohn, A. Kumar, S. Miller, D. Radchenko and M. Viazovska, The sphere packing problem in dimension 24, Ann. Math. 185 (2017), n. 3, 1017–1033.
- [10] H. Cohn, A. Kumar, S. Miller, D. Radchenko and M. Viazovska, Universal optimality of the E8 and Leech lattices and interpolation formulas, preprint at arXiv:1902.05438.
- [11] F. Gonc¸alves, Interpolation formulas with derivatives in de Branges spaces, Trans. Amer. Math. Soc. 369 (2017), 805–832.
- [12] F. Gonc¸alves and F. Littmann, Interpolation formulas with derivatives in de Branges spaces II, J. Math. Anal. Appl. 458 (2018), n. 2, 1091–1114.
- [13] F. Gonc¸alves, D. Oliveira e Silva, and J. P. G. Ramos, On regularity and mass concentration phenomena for the sign uncertainty principle, Preprint at arXiv:2003.10765.
- [14] F. Gonc¸alves, D. Oliveira e Silva, and J. P. G. Ramos, New sign uncertainty principles, Preprint at arXiv:2003.10771.
- [15] F. Gonc¸alves, D. Oliveira e Silva, and S. Steinerberger, Hermite polynomials, linear ﬂows on the torus, and an uncertainty principle for roots, J. Math. Anal. Appl. 451 (2017), n. 2, 678–711.
- [16] M.I. Kadec, The exact value of the Paley-Wiener constant, Sov. Math. Dokl. 5, 1964, 559–561.
- [17] P. Kurasov and P. Sarnak, Stable polynomials and crystalline measures, Preprint at arXiv:2004.05678
- [18] N. Lev and A. Olevskii, Measures with uniformly discrete support and spectrum, C. R. Math. Acad. Sci. Paris 351 (2013), no. 15-16, 613-617.
- [19] N. Lev and A. Olevskii, Quasicrystal and Poisson’s summation formula, Invent. Math. 200

(2015), no. 2, 585-606.

- [20] F. Littmann, Entire majorants via Euler-Maclaurin summation.
- [21] Y. Lyubarskii and K. Seip, Weighted Paley-Wiener spaces, J. Amer. Math. Soc. 15 (2002), n. 4, 979–1006.
- [22] Y. Meyer, Measures with locally ﬁnite support and spectrum, Rev. Mat. Iberoam. 33 (2017), no. 3, 1025–1036.
- [23] R. Paley and N. Wiener, Fourier transforms in the complex domain, Amer. Math. Soc. Colloquium Publications vol. 19. Amer. Math. Soc., New York, 1934
- [24] D. Radchenko and M. Viazovska, Fourier interpolation on the real line, Publ. Math. Inst. Hautes Etudes´ Sci. 129 (2019), 51–81.
- [25] J.P.G. Ramos and M. Sousa, Fourier uniqueness pairs of powers of integers, arXiv preprint at arXiv:1910.04276.
- [26] M. Schechter, Basic theory of Fredholm operators, Ann. Scuola Norm. Pisa, Classe di Scienze 3e se´rie, 21 (1967), n. 2, p. 261–280.
- [27] K. Seip and J. Ortega-Cerda`, Fourier frames, Ann. Math. 155 (2002), 789–806.
- [28] C. E. Shannon, Communications in the presence of noise, Proc. IRE 37 (1949), 10–21.
- [29] M. Stoller, Fourier interpolation from spheres, Preprint at arXiv:2002.11627.
- [30] J. D. Vaaler, Some extremal functions in Fourier analysis, Bull. Amer.Math. Soc. 12 (1985), 183–215.
- [31] M. Viazovska, The sphere packing problem in dimension 8, Ann. Math. 185 (2017), n. 3, 991– 1015.
- [32] E. T. Whittaker, On the functions which are represented by the expansions of the interpolation theory, Proc. Royal Soc. Edinburgh. 35 (1915), 181–194.
- [33] R. M. Young, An introduction to nonharmonic Fourier series, Academic Press, 1980.
- [34] D. Zagier, Elliptic modular forms and their applications, in The 1-2-3 of Modular Forms (K. Ranestad, ed.), 1–103, Universitext, Springer, Berlin (2008).


