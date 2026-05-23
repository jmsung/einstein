arXiv:1903.06826v1[math.CA]15Mar2019

A UNIVERSALITY LAW FOR SIGN CORRELATIONS OF EIGENFUNCTIONS OF DIFFERENTIAL OPERATORS

FELIPE GONC¸ALVES, DIOGO OLIVEIRA E SILVA, AND STEFAN STEINERBERGER

Abstract. We establish a universality law for sequences of functions {wn}n∈N satisfying a form of WKB approximation on compact intervals. This includes eigenfunctions of generic Schr¨odinger operators, as well as Laguerre and Chebyshev polynomials. Given two distinct points x, y ∈ R, we ask how often do wn(x) and wn(y) have the same sign. Asymptotically, one would expect this to be true half the time, but this turns out to not always be the case. Under certain natural assumptions, we prove that, for all x = y,

1 3

1 N

- 2

![image 1](<2019-gonccalves-universality-law-sign-correlations_images/imageFile1.png>)

- 3


≤ lim

# {0 ≤ n < N : sgn(wn(x)) = sgn(wn(y))} ≤

,

![image 2](<2019-gonccalves-universality-law-sign-correlations_images/imageFile2.png>)

![image 3](<2019-gonccalves-universality-law-sign-correlations_images/imageFile3.png>)

N→∞

and that these bounds are optimal, and can be attained. Our methods extend to other questions of similar ﬂavor and we also discuss a number of open problems.

1. Introduction

- 1.1. Setup. This paper is concerned with a simple and surprising property exhibited by the sequence of eigenfunctions for the eigenvalue problem of certain diﬀerential operators. Consider, on the real line, the Schro¨dinger operator associated to the potential V ,


d2 dx2

+ V (x). Here, V : R → R is some increasing function satisfying V (x) → ∞, as |x| → ∞.

- (1) H = −


![image 4](<2019-gonccalves-universality-law-sign-correlations_images/imageFile4.png>)

y

x

Figure 1. The potential V (x) = x2 (dashed) and the ﬁrst three eigenfunctions of the quantum harmonic oscillator.

![image 5](<2019-gonccalves-universality-law-sign-correlations_images/imageFile5.png>)

2010 Mathematics Subject Classiﬁcation. 34C10, 34L20.

Key words and phrases. Schr¨odinger operator, sign correlation limit, universality law, Hermite polynomials. D. O. S. acknowledges partial support by the College Early Career Travel Fund of the University of Birm-

ingham. S.S. is supported by the NSF (DMS-1763179) and the Alfred P. Sloan Foundation.

1

The eigenvalue problem

- (2) H(wn) = λnwn

has been studied extensively, the simpler case V (x) = x2 corresponding to the quantum harmonic oscillator whose eigenfunctions are given by the Hermite functions (see Figure 1). It is well understood that, as the eigenvalues become large, the second derivative dominates, and the eigenfunctions start to look locally like trigonometric functions. This phenomenon is known as WKB approximation, named after Wentzel, Kramers, and Brillouin. The purpose of our paper is to establish a rather surprising universality statement for sign correlations of sequences of functions for which a kind of WKB approximation holds. Our starting point is very simple to state: given two distinct points x,y ∈ R, how often do wn(x) and wn(y) have the same sign? More precisely, we are interested in the sign correlation limit, deﬁned as

- (3) ℓ{wn}(x,y) := lim N→∞

1 N

![image 6](<2019-gonccalves-universality-law-sign-correlations_images/imageFile6.png>)

#{0 ≤ n < N : sgn(wn(x)) = sgn(wn(y))}.

One could be tempted to conjecture that, in the high frequency limit, the two points x,y decouple and the corresponding signs behave essentially like independent Bernoulli random variables, thus exhibiting the same sign in roughly half of the cases. This seemingly natural conjecture turns out to be a good guess for the generic behavior of the system. However, earlier work of the authors [8] hinted at the possible existence of an exceptional set exhibiting a diﬀerent kind of behavior, and motivated the present paper.

1.2. Main Result. A sequence {an} ⊆ [0,1] is said to be equidistributed in [0,1] if, for any subinterval [c,d] ⊆ [0,1],

lim

N→∞

1 N

![image 7](<2019-gonccalves-universality-law-sign-correlations_images/imageFile7.png>)

#{0 ≤ n < N : an ∈ [c,d]} = d − c.

A sequence {an} ⊆ R is said to be equidistributed modulo 1 if the sequence of the fractional parts {an − ⌊an⌋} is equidistributed in [0,1]. Our ﬁrst main result applies to a sequence of functions obeying a certain asymptotic behavior which is inspired by the WKB approximation, and is satisﬁed by several classical objects (see the examples in §4). Regarding notation, on(1) will denote a quantity that tends to 0, as n → ∞. We will also write an = O(bn), or |an| |bn|, if there exists a constant C < ∞ (independent of n) such that |an| ≤ C|bn|, for every n.

- Theorem 1 (Main Result). Given D ⊆ R, let wn : D → R be a sequence of functions satisfying


- (4) wn(x) = (1 + on(1)) φ(x,n)cos (2π(µnϕ(x) − θ)),

for every x ∈ D and some {µn} ⊂ R, θ ∈ R, and function φ : D × N → R. Consider distinct points x,y ∈ D such that ϕ(x) = ±ϕ(y) and φ(x,n)φ(y,n) > 0 for all n. If the sequences {p−1µnϕ(x)} and {q−1µnϕ(y)} are equidistributed modulo 1 for any p,q ∈ Z \ {0}, then the sign correlation limit (3) exists, and satisﬁes

- (5)


- 2

![image 8](<2019-gonccalves-universality-law-sign-correlations_images/imageFile8.png>)

- 3


1 3 ≤ ℓ{wn}(x,y) ≤

. Moreover, these constants are optimal.

![image 9](<2019-gonccalves-universality-law-sign-correlations_images/imageFile9.png>)

We believe this result to be rather surprising. In particular, it establishes the existence of correlations diﬀerent from 12. These correlations are, however, universally bounded away from both 0 and 1. Theorem 1 motivates a number of natural questions, see §1.4 below.

![image 10](<2019-gonccalves-universality-law-sign-correlations_images/imageFile10.png>)

- 1.3. Sharper asymptotics. The sign correlation limit can be computed exactly in a number


of situations of interest. We proceed to describe one such situation. Let V ∈ L1loc(R) be a locally integrable potential such that V (x) → ∞, as |x| → ∞, and assume V to be bounded

from below,

- (6) ess infx∈RV (x) > −∞. We renormalize the Hamiltonian by setting HV = −4π12

![image 11](<2019-gonccalves-universality-law-sign-correlations_images/imageFile11.png>)

d2

![image 12](<2019-gonccalves-universality-law-sign-correlations_images/imageFile12.png>)

dx2 + V (x) (this is adapted to our choice of normalization for the Fourier transform, see (12) below). Under these conditions, the operator HV given by (1) is known to have compact resolvent. In particular, HV has purely discrete spectrum and a complete set of eigenfunctions, see [13, Theorem XIII.67]. This means that there exists an orthogonal basis {wn} of L2(R) such that HV (wn) = λnwn, where the eigenvalues {λn} form a non-decreasing sequence satisfying λn → ∞, as n → ∞. In addition, we require V to be an even function. This implies that the basis {wn} naturally splits into even and odd functions, since these subspaces are HV -invariant. In particular, we can reorder the basis elements in such a way that wn is an even function if n is even, and an odd function if n is odd. After doing so, the sequence {λn} may no longer be non-decreasing, however we still have that λn → ∞, as n → ∞. By uniqueness of solutions to the eigenvalue problem (2), we may further impose sgn(w2n(0)) = sgn(w2′n+1(0)) = (−1)n. Here and in the rest of the paper a prime denotes diﬀerentiation with respect to the variable x. We will also require both subsequences {

√λ2nx} and { λ2n+1x} to be equidistributed modulo 1, for every x = 0. Whether this should generically be the case is discussed in Problem (3) from §1.4 below. We are now ready to state our second main result.

![image 13](<2019-gonccalves-universality-law-sign-correlations_images/imageFile13.png>)

![image 14](<2019-gonccalves-universality-law-sign-correlations_images/imageFile14.png>)

- Theorem 2 (Sharper asymptotics). Let V ∈ L1loc(R) be an even potential, bounded from below in the sense of (6), and such that V (x) → ∞, as |x| → ∞. For each n ∈ N, assume that for the associated eigenvalue problem HV (wn) = λnwn, the following assertions hold:


- (H1) the function wn is even if n is even, and odd if n is odd,
- (H2) the sequences {

√λ2nx} and { λ2n+1x} are equidistributed modulo 1, for any x ∈ R \ {0},

![image 15](<2019-gonccalves-universality-law-sign-correlations_images/imageFile15.png>)

![image 16](<2019-gonccalves-universality-law-sign-correlations_images/imageFile16.png>)

- (H3) and we have sgn(w2n(0)) = sgn(w2′n+1(0)) = (−1)n.


Then the asymptotic

- (7) wn(x) = (1 + on(1)) wn(0)2 + w

′ n(0)2

![image 17](<2019-gonccalves-universality-law-sign-correlations_images/imageFile17.png>)

4π2λn

1/2

cos 2π λnx − n4 holds uniformly on compact subsets of the real line. If x,y are distinct real numbers such that

![image 18](<2019-gonccalves-universality-law-sign-correlations_images/imageFile18.png>)

![image 19](<2019-gonccalves-universality-law-sign-correlations_images/imageFile19.png>)

- x

![image 20](<2019-gonccalves-universality-law-sign-correlations_images/imageFile20.png>)

- y = pq for some nonzero coprime integers p,q, then the sign correlation limit (3) is given by


![image 21](<2019-gonccalves-universality-law-sign-correlations_images/imageFile21.png>)

- (8) ℓ{wn}(x,y) =


- 1

![image 22](<2019-gonccalves-universality-law-sign-correlations_images/imageFile22.png>)

- 2 + 21pq if p ≡ q ≡ 1 mod 4, or p ≡ q ≡ 3 mod 4,


![image 23](<2019-gonccalves-universality-law-sign-correlations_images/imageFile23.png>)

- 1

![image 24](<2019-gonccalves-universality-law-sign-correlations_images/imageFile24.png>)

- 2 otherwise.


If xy is irrational, then ℓ{wn}(x,y) = 12.

![image 25](<2019-gonccalves-universality-law-sign-correlations_images/imageFile25.png>)

![image 26](<2019-gonccalves-universality-law-sign-correlations_images/imageFile26.png>)

The asymptotic (7) is exactly the one given via WKB approximation. The quadratic case V (x) = x2, where the WKB approximation coincides with the classical asymptotic for Hermite polynomials, falls under the scope of Theorem 2 and is described in more detail in §4 (together with higher dimensional extensions, provided by the Laguerre polynomials).

- 1.4. Further remarks and open problems.


- (1) Can Theorems 1 and 2 be extended to sign correlations of three or more points? What can be said about the density with which a speciﬁc sign conﬁguration, say (+,−,+,−,−), can occur? Some of these may be universally bounded away from 0 and 1, while others may not be. In principle, our approach provides a framework for obtaining such bounds since each such question is reduced to a ﬁnite computation. However, the increase in complexity is substantial, which is why we have not been able to further explore this question. We believe it to be a promising avenue for future research.
- (2) Is it possible to characterize the class of potentials V such that our result applies to

eigenfunctions of the Schro¨dinger operator HV ? The WKB approximation seems to be a valuable tool; however, it is not clear to us whether a suitable theory on the equidistribution of the eigenvalues of diﬀerential operators exists. On the other hand, the asymptotic growth of {λn}, as n → ∞, has been studied extensively, see e.g. [7], but this question seems more subtle.

- (3) As we shall see, these questions are connected to classical problems on the asymptotic behavior of geodesics on the d-dimensional torus Td. It is natural to expect that several of the new developments regarding strong forms of linear ﬂow rigidity [1, 2, 3, 4, 9, 15] can be used to make more precise statements in some special cases. We also note that at least for some classical families of orthogonal polynomials it should be possible to obtain more precise quantitative information – see §4 below for further details.


2. Useful Lemmata

We start with a general result that will serve as a ﬁrst step towards computing the sign correlation limit of a sequence of functions over a ﬁxed ﬁnite set of points a = (a1,...,ad) ∈ Rd.

- Lemma 1. Given a ∈ Rd, assume that λa ∈ Zd, for some λ > 0. Let f : R → R be a


continuous 1-periodic function. Let {µn} ⊂ R be a sequence such that {µλn} is equidistributed modulo 1. Let s ∈ {−1,1}d. Then

![image 27](<2019-gonccalves-universality-law-sign-correlations_images/imageFile27.png>)

1

1 N

Ψ(λta)dt,

#{0 ≤ n < N : (sgn[f(µna1)],...,sgn[f(µnad)]) = ±s} =

lim

![image 28](<2019-gonccalves-universality-law-sign-correlations_images/imageFile28.png>)

N→∞

0

where the function Ψ : Rd → {0,1} is deﬁned as follows: given u ∈ Rd, then Ψ(u) = 1 if (sgn[f(u1)],...,sgn[f(ud)]) = ±s, and Ψ(u) = 0 otherwise. Proof. Consider the function g(t) := Ψ(λta), which satisﬁes g(t + 1) = g(t), for every t ∈ R. By construction, we have that

{0 ≤ n < N : (sgn[f(µna1)],...,sgn[f(µnad)]) = ±s} = {0 ≤ n < N : g(µλn ) = 1}.

![image 29](<2019-gonccalves-universality-law-sign-correlations_images/imageFile29.png>)

Since the function g is 1-periodic and the sequence {µλn } is equidistributed modulo 1, we have that, as N → ∞,

![image 30](<2019-gonccalves-universality-law-sign-correlations_images/imageFile30.png>)

1 N

g.

#{0 ≤ n < N : (sgn[f(µna1)],...,sgn[f(µnad)]) = ±s} → |{t ∈ [0,1] : g(t) = 1}| =

![image 31](<2019-gonccalves-universality-law-sign-correlations_images/imageFile31.png>)

[0,1]

The last identity follows from the fact that the function g takes values in {0,1}. This concludes the proof of the lemma.

Only the case d = 2 of Lemma 1 will be relevant to our applications. For the remainder of the section, we will discuss integrals of the function

- (9) Φ(x,y) := sgn(cos(2πx)cos(2πy))

over rays of the two-dimensional torus T2 = R2/Z2, which will play a key role in the proof of our main theorems. We remark that the Haar measure on T2 coincides with the Lebesgue measure on the fundamental domain [0,1]2. We further note that, given a ray γ : R → T2 deﬁned by γ(t) = (At − α,Bt − β) for some A,B = 0, then

- (10) lim T→∞

1 T

![image 32](<2019-gonccalves-universality-law-sign-correlations_images/imageFile32.png>)

T

0

Φ(γ(t))dt = lim

T→∞

1 T

![image 33](<2019-gonccalves-universality-law-sign-correlations_images/imageFile33.png>)

T

0

Φ( γ(t))dt,

where γ : R → T2 is in turn given by γ(t) = (t,at+b), with a = B/A and b = (B/A)α−β. The following lemma is well-known, with suitable modiﬁcations and vast generalizations appearing in [5, 6, 12]. For the sake of completeness, we provide a short proof.

- Lemma 2. Given a,b ∈ R, let γ(t) = (t,at + b) be the corresponding line in R2. Then the limit

(11) lim

T→∞

1 T

![image 34](<2019-gonccalves-universality-law-sign-correlations_images/imageFile34.png>)

T

0

Φ(γ(t))dt exists. Moreover, if the limit is nonzero, then the coeﬃcient a is a rational number.

Proof. Since the function Φ is 1-periodic in the variables x and y, the problem reduces to a standard question in equidistribution theory on the 2-dimensional torus T2. If a is irrational, then the line t  → (t,at + b) is densely wound and equidistributes over T2, and the averaged integral in (11) converges to the average value of Φ,

lim

T→∞

1 T

![image 35](<2019-gonccalves-universality-law-sign-correlations_images/imageFile35.png>)

T

0

Φ(γ(t))dt =

T2

Φ = 0,

see [6, §2.3]. If a is rational, then the line t  → (t,at + b) gives rise to a closed geodesic on T2, and the existence of the limit (11) follows from periodicity.

The next lemma further analyzes the case of rational slope a = p/q ∈ Q. It is of quantitative ﬂavor, and relies on the explicit form of the function Φ. We achieve this by resorting to Fourier series, and will normalize the Fourier coeﬃcients of an integrable function f : [0,1] → C in the following way:

(12) f(n) =

1

0

f(x)e−2πinx dx.

- Lemma 3. Let A,B ∈ R be nonzero real numbers, such that A/B = p/q for some coprime p,q ∈ Z. Let α,β ∈ R and let γ(t) = (At − α,Bt − β) be the corresponding ray on T2. If either p or q are even, then




T

1 T

lim

Φ(γ(t))dt = 0. If both p and q are odd, then

![image 36](<2019-gonccalves-universality-law-sign-correlations_images/imageFile36.png>)

T→∞

0

1 T

lim

![image 37](<2019-gonccalves-universality-law-sign-correlations_images/imageFile37.png>)

T→∞

T

Φ(γ(t))dt = (−1)

0

2 +1 8 π2pq

p+q

![image 38](<2019-gonccalves-universality-law-sign-correlations_images/imageFile38.png>)

![image 39](<2019-gonccalves-universality-law-sign-correlations_images/imageFile39.png>)

∞

cos (2π(2ℓ + 1)(pβ − qα)) (2ℓ + 1)2

.

![image 40](<2019-gonccalves-universality-law-sign-correlations_images/imageFile40.png>)

ℓ=0

In particular, in this case, we have that lim

T

1 |pq|

1 T

, (p,q odd) where equality is attained if and only if pβ − qα is an integer. Proof. By periodicity, recall (10), we have that

Φ(γ(t))dt ≤

![image 41](<2019-gonccalves-universality-law-sign-correlations_images/imageFile41.png>)

![image 42](<2019-gonccalves-universality-law-sign-correlations_images/imageFile42.png>)

T→∞

0

1

T

1 T

Φ(pt − α,qt − β)dt. Expanding the function Φ in Fourier series,

Φ(γ(t))dt =

lim

![image 43](<2019-gonccalves-universality-law-sign-correlations_images/imageFile43.png>)

T→∞

0

0

sin(πn2 )sin(πm2 ) mn

4

![image 44](<2019-gonccalves-universality-law-sign-correlations_images/imageFile44.png>)

![image 45](<2019-gonccalves-universality-law-sign-correlations_images/imageFile45.png>)

e2πi(mx+ny),

Φ(x,y) =

![image 46](<2019-gonccalves-universality-law-sign-correlations_images/imageFile46.png>)

![image 47](<2019-gonccalves-universality-law-sign-correlations_images/imageFile47.png>)

π2 n,m∈Z m,n =0

we obtain that

sin(πn2 )sin(πm2 ) mn

1

1

4

![image 48](<2019-gonccalves-universality-law-sign-correlations_images/imageFile48.png>)

![image 49](<2019-gonccalves-universality-law-sign-correlations_images/imageFile49.png>)

e2πi(mp+nq)te−2πi(mα+nβ) dt

Φ(pt − α,qt − β)dt =

![image 50](<2019-gonccalves-universality-law-sign-correlations_images/imageFile50.png>)

![image 51](<2019-gonccalves-universality-law-sign-correlations_images/imageFile51.png>)

π2 n,m∈Z m,n =0

0

0

∞

sin(πkp2 )sin(πkq2 ) k2

8 π2pq

![image 52](<2019-gonccalves-universality-law-sign-correlations_images/imageFile52.png>)

![image 53](<2019-gonccalves-universality-law-sign-correlations_images/imageFile53.png>)

=

cos(2πk(pβ − qα)).

![image 54](<2019-gonccalves-universality-law-sign-correlations_images/imageFile54.png>)

![image 55](<2019-gonccalves-universality-law-sign-correlations_images/imageFile55.png>)

k=1

This quantity vanishes if either p or q are even. On the other hand, if both p and q are odd, then

∞

1

cos(2π(2ℓ + 1)(pβ − qα)) (2ℓ + 1)2

2 +1 8 π2pq

p+q

.

Φ(pt − α,qt − β)dt = (−1)

![image 56](<2019-gonccalves-universality-law-sign-correlations_images/imageFile56.png>)

![image 57](<2019-gonccalves-universality-law-sign-correlations_images/imageFile57.png>)

![image 58](<2019-gonccalves-universality-law-sign-correlations_images/imageFile58.png>)

0

ℓ=0

Since ∞ℓ=0 (2ℓ+1)1 2 = π82, the triangle inequality implies

![image 59](<2019-gonccalves-universality-law-sign-correlations_images/imageFile59.png>)

![image 60](<2019-gonccalves-universality-law-sign-correlations_images/imageFile60.png>)

1

1 |pq|

Φ(pt − α,qt − β)dt ≤

, where equality is attained if and only if (pβ − qα) ∈ Z.

![image 61](<2019-gonccalves-universality-law-sign-correlations_images/imageFile61.png>)

0

3. Proofs of Theorems 1 and 2

- Proof of Theorem 1. Let x = y ∈ D be given, satisfying ϕ(x) = ±ϕ(y) and φ(x,n)φ(y,n) > 0, for all n. No generality is lost in assuming that ϕ(x)/ϕ(y) = p/q for some coprime p,q ∈ Z,


and that p/ϕ(x) = q/ϕ(y) > 0, for otherwise Lemma 2 would imply that ℓ{wn}(x,y) = 12, and there is nothing to prove. Now, since φ(x,n)φ(y,n) > 0 for all n, the asymptotic (4) implies

![image 62](<2019-gonccalves-universality-law-sign-correlations_images/imageFile62.png>)

- (13) ℓ{wn}(x,y) = ℓ{un}(x,y),

where un(x) := cos(2π(µnϕ(x)−θ)). We focus on the latter limit, and prepare to apply Lemma 1 with a = (ϕ(x),ϕ(y)), s = (1,1), λ = p/ϕ(x) = q/ϕ(y), and f(z) = cos(2π(z − θ)). Note

that the our equidistribution assumption implies that the sequence {µλn } = {p−1µnϕ(x)} is equidistributed modulo 1, and so all the hypotheses of Lemma 1 are satisﬁed. The conclusion

![image 63](<2019-gonccalves-universality-law-sign-correlations_images/imageFile63.png>)

is that

- (14) ℓ{un}(x,y) =


1

Ψ(pt − θ,qt − θ)dt,

0

where the function Ψ is related to Φ from (9) via Φ = 2Ψ − 1. It then follows from (13) and

- (14) that
- (15) ℓ{wn}(x,y) =

- 1

![image 64](<2019-gonccalves-universality-law-sign-correlations_images/imageFile64.png>)

- 2


+

- 1

![image 65](<2019-gonccalves-universality-law-sign-correlations_images/imageFile65.png>)

- 2


1

0

Φ(pt − θ,qt − θ)dt.

The latter integral was computed in the course of the proof of Lemma 3, and is non-zero only if both p,q are odd. In that case, applying Lemma 3 with A = ϕ(x), B = ϕ(y), and α = β = θ, yields

- (16)

1

0

Φ(pt − θ,qt − θ)dt ≤

1 |pq|

![image 66](<2019-gonccalves-universality-law-sign-correlations_images/imageFile66.png>)

.

To ﬁnish the argument, note that p,q both being odd, and ϕ(x) = ±ϕ(y), jointly force the inequality |pq1 | ≤ 31. Estimates (15) and (16) then imply (5), which is the ﬁrst desired conclusion. To verify the claimed optimality, recall the cases of equality in Lemma 3 and consider the particular case when ϕ(x) = 3ϕ(y) and θ(ϕ(x) − ϕ(y)) ∈ Z.

![image 67](<2019-gonccalves-universality-law-sign-correlations_images/imageFile67.png>)

![image 68](<2019-gonccalves-universality-law-sign-correlations_images/imageFile68.png>)

Proof of Theorem 2. Let us brieﬂy recall the proof of the asymptotic (7). Start by noting that two linearly independent solutions of the associated homogeneous equation wn′′+4π2λnwn = 0 are given by

wn,1(x) := cos(2π λnx), and wn,2(x) := sin(2π λnx), and have constant Wronskian

![image 69](<2019-gonccalves-universality-law-sign-correlations_images/imageFile69.png>)

![image 70](<2019-gonccalves-universality-law-sign-correlations_images/imageFile70.png>)

W(wn(1),wn(2)) := det

wn,1 wn,2 wn,′ 1 wn,′ 2

= 2π λn. The general solution to the eigenvalue problem (2) is then given by

![image 71](<2019-gonccalves-universality-law-sign-correlations_images/imageFile71.png>)

- (17) acos(2π λnx) + bsin(2π λnx) +

![image 72](<2019-gonccalves-universality-law-sign-correlations_images/imageFile72.png>)

![image 73](<2019-gonccalves-universality-law-sign-correlations_images/imageFile73.png>)

2π √λn

![image 74](<2019-gonccalves-universality-law-sign-correlations_images/imageFile74.png>)

![image 75](<2019-gonccalves-universality-law-sign-correlations_images/imageFile75.png>)

x

0

sin(2π λn(x − t))V (t)wn(t)dt,

![image 76](<2019-gonccalves-universality-law-sign-correlations_images/imageFile76.png>)

for some a,b ∈ R, as can be easily checked by direct diﬀerentiation. Evaluating (17) and its derivative at zero while appealing to hypotheses (H1) and (H3), we then have that

- (18)


x

2π √λn

![image 77](<2019-gonccalves-universality-law-sign-correlations_images/imageFile77.png>)

′ n(0)2

wn(x) = wn(0)2 + w

![image 78](<2019-gonccalves-universality-law-sign-correlations_images/imageFile78.png>)

![image 79](<2019-gonccalves-universality-law-sign-correlations_images/imageFile79.png>)

4π2λn cos 2π λnx − n4 +

sin(2π λn(x−t))V (t)wn(t)dt.

![image 80](<2019-gonccalves-universality-law-sign-correlations_images/imageFile80.png>)

![image 81](<2019-gonccalves-universality-law-sign-correlations_images/imageFile81.png>)

![image 82](<2019-gonccalves-universality-law-sign-correlations_images/imageFile82.png>)

![image 83](<2019-gonccalves-universality-law-sign-correlations_images/imageFile83.png>)

0

Deﬁne Mn(x) := max{|wn(y)| : y ∈ [0,x]}. Applying the integral form of Gro¨nwall’s inequality [17, Theorem 1.10] to (18), we deduce

1/2

′ n(0)2

Mn(x) ≤ wn(0)2 + w

+ on(1)Mn(x), and therefore

![image 84](<2019-gonccalves-universality-law-sign-correlations_images/imageFile84.png>)

4π2λn

1/2

′ n(0)2

Mn(x) wn(0)2 + w

,

![image 85](<2019-gonccalves-universality-law-sign-correlations_images/imageFile85.png>)

4π2λn

from where asymptotic (7) follows at once. The rest of the proof follows similar steps to those of Theorem 1. Firstly, we can restrict attention to the case of rational x/y. Secondly,

ℓ{wn}(x,y) = ℓ{vn}(x,y),

where vn(x) := cos(2π(√λnx − n4)). Thirdly, given the equidistribution assumption (H2), Lemma 1 again applies and reduces the computation to

![image 86](<2019-gonccalves-universality-law-sign-correlations_images/imageFile86.png>)

![image 87](<2019-gonccalves-universality-law-sign-correlations_images/imageFile87.png>)

1

Ψ0 + Ψ1 2

(pt,qt)dt.

ℓ{vn}(x,y) =

![image 88](<2019-gonccalves-universality-law-sign-correlations_images/imageFile88.png>)

0

Here, the functions Ψ0,Ψ1 are given by Φ0 =: 2Ψ0 −1 and Φ1 =: 2Ψ0 −1, where Φ0 := Φ was given in (9), and Φ1(x,y) := Φ(x − 14,y − 41). Consequently,

![image 89](<2019-gonccalves-universality-law-sign-correlations_images/imageFile89.png>)

![image 90](<2019-gonccalves-universality-law-sign-correlations_images/imageFile90.png>)

1

1

1 4

- 1

![image 91](<2019-gonccalves-universality-law-sign-correlations_images/imageFile91.png>)

- 2


1 4

Φ(pt − 41,qt − 14)dt. These integrals can be calculated with Lemma 3. Invoking it with α = β = 0, and then with α = β = 14, yields

+

ℓ{wn}(x,y) =

Φ(pt,qt)dt +

![image 92](<2019-gonccalves-universality-law-sign-correlations_images/imageFile92.png>)

![image 93](<2019-gonccalves-universality-law-sign-correlations_images/imageFile93.png>)

![image 94](<2019-gonccalves-universality-law-sign-correlations_images/imageFile94.png>)

![image 95](<2019-gonccalves-universality-law-sign-correlations_images/imageFile95.png>)

0

0

![image 96](<2019-gonccalves-universality-law-sign-correlations_images/imageFile96.png>)

- 1

![image 97](<2019-gonccalves-universality-law-sign-correlations_images/imageFile97.png>)

- 2


1 4pq

p+q

2 +1 + (−1)p+1 This is readily seen to be equivalent to the result as stated in (8).

ℓ{wn}(x,y) =

(−1)

+

![image 98](<2019-gonccalves-universality-law-sign-correlations_images/imageFile98.png>)

![image 99](<2019-gonccalves-universality-law-sign-correlations_images/imageFile99.png>)

4. Further examples: Hermite functions, Laguerre polynomials and sets of bounded remainder

- 4.1. Hermite functions. One could think of replacing hypothesis (4) from Theorem 1 by a less restrictive assumption of the form


wn(x) = (1 + on(1)) φ(x,n)cos (2π(µnϕ(x) − θn)), where {θn} is now a sequence. Without any further assumption, several steps of the preceding proofs break down completely. However, if some quantitative control on the speed with which the sequences {µnϕ(x)} and {µnϕ(y)} equidistribute modulo 1 is known, then we can allow for a certain degree of variability in the sequence {θn}. It is not clear to us what the sharp version of such a statement would be, and we leave it for future research.

Cases in which the sequence {θn} changes rapidly with n, but does so in a structured manner, are also of interest. Such cases may be dealt with by partitioning {wn} into an appropriate number of subsequences, as we now illustrate. A particularly nice example which ﬁts into this framework (and served as original inspiration for Theorem 2) is that of the Schro¨dinger operator on the real line,

d2 dx2

1 4π2

+ x2. The operator H is diagonalized by the Hermite functions, ϕn(x) := Hn(

H := −

![image 100](<2019-gonccalves-universality-law-sign-correlations_images/imageFile100.png>)

![image 101](<2019-gonccalves-universality-law-sign-correlations_images/imageFile101.png>)

√

2πx)e−πx2.

![image 102](<2019-gonccalves-universality-law-sign-correlations_images/imageFile102.png>)

Here, {Hn(x)} denote the classical Hermite polynomials, which are orthogonal with respect to the standard Gaussian measure e−πx2 dx. As is well-known,

2n + 1 2π

- (19) H(ϕn) =


ϕn. Moreover, the asymptotic from [16, Theorem 8.22.6 and Formula (8.22.8)], Hn(

![image 103](<2019-gonccalves-universality-law-sign-correlations_images/imageFile103.png>)

√

n 4

Γ(n + 1) Γ(n2 + 1)

![image 104](<2019-gonccalves-universality-law-sign-correlations_images/imageFile104.png>)

2πx)e−πx2 = (1 + on(1))

cos 2π 2n2+1π x −

![image 105](<2019-gonccalves-universality-law-sign-correlations_images/imageFile105.png>)

![image 106](<2019-gonccalves-universality-law-sign-correlations_images/imageFile106.png>)

![image 107](<2019-gonccalves-universality-law-sign-correlations_images/imageFile107.png>)

![image 108](<2019-gonccalves-universality-law-sign-correlations_images/imageFile108.png>)

![image 109](<2019-gonccalves-universality-law-sign-correlations_images/imageFile109.png>)

shows that the eigenfunctions {ϕn} in (19) do not satisfy the assumptions of Theorem 1, but that the subsequences {ϕ2n} and {ϕ2n+1} do. We further note that the basis {ϕn} diagonalizes the Fourier transform in the following sense: the elements of {ϕn} are pairwise orthogonal, dense in L2(R), and

ϕn(ξ) =

∞

ϕn(x)e−2πiξx dx = (−i)nϕn(ξ).

−∞

A simple consequence of Theorem 2 (plus a short computation) is the following.

- Proposition 3 (Sign Correlations for Hermite functions). Let x,y = 0 and y/x ∈ Z. Then

ℓ{ϕn}(x,y) =

- 1

![image 110](<2019-gonccalves-universality-law-sign-correlations_images/imageFile110.png>)

- 2 + 2xy if xy ≡ 1 mod 4, 1 2 otherwise.


![image 111](<2019-gonccalves-universality-law-sign-correlations_images/imageFile111.png>)

![image 112](<2019-gonccalves-universality-law-sign-correlations_images/imageFile112.png>)

![image 113](<2019-gonccalves-universality-law-sign-correlations_images/imageFile113.png>)

- 4.2. Laguerre polynomials. An extension of the previous example to higher dimensions


involves the so-called Laguerre polynomials. Let {Lνn(x)} be the (generalized) Laguerre polynomials with parameter ν > −1, deﬁned via

(20)

∞

0

Lνn(x)Lνm(x)xνe−x dx =

Γ(n + ν + 1) n!

![image 114](<2019-gonccalves-universality-law-sign-correlations_images/imageFile114.png>)

δ(n − m).

It is well-known, see [16, Formula (8.22.2)], that

Lνn(2πx2)e−πx2 = (1 + on(1))

nν/2−1/4 √π(2π)ν/2+1/4xν+1/2

![image 115](<2019-gonccalves-universality-law-sign-correlations_images/imageFile115.png>)

![image 116](<2019-gonccalves-universality-law-sign-correlations_images/imageFile116.png>)

cos 2π 4n+22πν+2x −

![image 117](<2019-gonccalves-universality-law-sign-correlations_images/imageFile117.png>)

![image 118](<2019-gonccalves-universality-law-sign-correlations_images/imageFile118.png>)

2ν + 1 8

![image 119](<2019-gonccalves-universality-law-sign-correlations_images/imageFile119.png>)

.

It is also known that the set of Laguerre functions

x ∈ Rd  → Φn(x) := Lνn(2π|x|2)e−π|x|2,

with ν = d/2 − 1, diagonalizes the operator H = −4π12∆ + |x|2 over the space of radial functions in Rd, and that

![image 120](<2019-gonccalves-universality-law-sign-correlations_images/imageFile120.png>)

H(Φn) =

(4n + 2ν + 2) 2π

![image 121](<2019-gonccalves-universality-law-sign-correlations_images/imageFile121.png>)

Φn.

We also note that {Φn} diagonalizes the Fourier transform over the space of square integrable radial functions in Rd. Indeed,

Φn(ξ) =

Rd

Φn(x)e−2πiξ·x dx = (−1)nΦn(ξ).

The following result is a direct application of Lemma 3 with α = β = 2ν8+1 = d−81.

![image 122](<2019-gonccalves-universality-law-sign-correlations_images/imageFile122.png>)

![image 123](<2019-gonccalves-universality-law-sign-correlations_images/imageFile123.png>)

- Proposition 4 (Sign Correlations for Laguerre functions). Let r1,r2 > 0 be radii such that r1 r2 = pq for some coprime integers p and q. Then


![image 124](<2019-gonccalves-universality-law-sign-correlations_images/imageFile124.png>)

![image 125](<2019-gonccalves-universality-law-sign-correlations_images/imageFile125.png>)

 

- 1

![image 126](<2019-gonccalves-universality-law-sign-correlations_images/imageFile126.png>)

- 2, if p or q is even, or if p,q and (p−q)(2d−1) are odd,


![image 127](<2019-gonccalves-universality-law-sign-correlations_images/imageFile127.png>)

ℓ{Φn}(r1,r2) =

- 1

![image 128](<2019-gonccalves-universality-law-sign-correlations_images/imageFile128.png>)

- 2 − 21pq(−1)p+2q+(p−q)(4d−1), otherwise.




![image 129](<2019-gonccalves-universality-law-sign-correlations_images/imageFile129.png>)

![image 130](<2019-gonccalves-universality-law-sign-correlations_images/imageFile130.png>)

![image 131](<2019-gonccalves-universality-law-sign-correlations_images/imageFile131.png>)

- 4.3. Sets of bounded remainder. In this ﬁnal section, we describe a curious phenomenon which was discovered by accident. Consider the family of Chebyshev polynomials of the ﬁrst


kind on the interval [−1,1], denoted {Tn}n≥0 and deﬁned via Tn(x) := cos(narccos x). This turns out to be one of the extremal examples for Theorem 1 since

# 0 ≤ n < N : sgn Tn(cos (210π)) = sgn Tn(cos (3210π)) = (1 + oN(1))N3 . Indeed, the arising quantities simplify to

![image 132](<2019-gonccalves-universality-law-sign-correlations_images/imageFile132.png>)

![image 133](<2019-gonccalves-universality-law-sign-correlations_images/imageFile133.png>)

![image 134](<2019-gonccalves-universality-law-sign-correlations_images/imageFile134.png>)

Tn(cos (210π)) = cos (210πn) and Tn(cos (3210π)) = cos(3210πn),

![image 135](<2019-gonccalves-universality-law-sign-correlations_images/imageFile135.png>)

![image 136](<2019-gonccalves-universality-law-sign-correlations_images/imageFile136.png>)

![image 137](<2019-gonccalves-universality-law-sign-correlations_images/imageFile137.png>)

![image 138](<2019-gonccalves-universality-law-sign-correlations_images/imageFile138.png>)

and both sequences {210πn} and {3210πn} are equidistributed modulo 1. If we go one step further and try to understand the error term, we encounter the following surprising phenomenon. At

![image 139](<2019-gonccalves-universality-law-sign-correlations_images/imageFile139.png>)

![image 140](<2019-gonccalves-universality-law-sign-correlations_images/imageFile140.png>)

least for N ≤ 104, we used Mathematica to verify that

# 0 ≤ n < N : sgn Tn(cos (210π)) = sgn Tn(cos (3210π)) − N3 ≤ 10. This is probably related to the ﬁne structure of Kronecker sequences [10, 11, 14], and one cannot hope for such strong results in general. This is reminiscent of exciting new developments in the theory of continuous ﬂows on the torus, Jozse´f Beck’s superuniformity theory [1, 2, 3, 4], that may have nontrivial implications to the present context. We also refer to a related paper by Grepstad & Larcher on sets of bounded remainder [9], which seems to provide further interesting directions of research.

![image 141](<2019-gonccalves-universality-law-sign-correlations_images/imageFile141.png>)

![image 142](<2019-gonccalves-universality-law-sign-correlations_images/imageFile142.png>)

![image 143](<2019-gonccalves-universality-law-sign-correlations_images/imageFile143.png>)

References

- [1] J. Beck, Strong uniformity. Uniform distribution and quasi-Monte Carlo methods, 17–44, Radon Ser. Comput. Appl. Math. 15, De Gruyter, Berlin, 2014.
- [2] J. Beck, Super-uniformity of the typical billiard path. An irregular mind, 39–129, Bolyai Soc. Math. Stud. 21, J´anos Bolyai Math. Soc., Budapest, 2010.
- [3] J. Beck, From Khinchin’s conjecture on strong uniformity to superuniform motions. Mathematika 61

(2015), no. 3, 591–707.

- [4] J. Beck, Dimension-free uniformity with applications, I. Mathematika 63 (2017), no. 3, 734–761.
- [5] J. Dick and F. Pillichshammer, Digital nets and sequences. Discrepancy theory and quasi-Monte Carlo integration. Cambridge University Press, Cambridge, 2010.
- [6] M. Drmota and R. Tichy, Sequences, discrepancies and applications. Lecture Notes in Mathematics,

1651. Springer-Verlag, Berlin, 1997.

- [7] C. Fefferman, The uncertainty principle. Bull. Amer. Math. Soc. 9 (1983), no. 2, 129–206.
- [8] F. Gonc¸alves, D. Oliveira e Silva and S. Steinerberger, Hermite polynomials, linear ﬂows on the torus, and an uncertainty principle for roots. J. Math. Anal. Appl. 451 (2017), no. 2, 678–711.
- [9] S. Grepstad and G. Larcher, Sets of bounded remainder for a continuous irrational rotation on [0, 1]2. Acta Arith. 176 (2016), no. 4, 365–395.
- [10] E. Hecke, Uber¨ analytische Funktionen und die Verteilung von Zahlen mod. eins. Abh. Math. Sem. Univ. Hamburg 1 (1922), no. 1, 54–76.
- [11] H. Kesten, On a conjecture of Erd¨s and Szu¨sz related to uniform distribution mod 1. Acta Arith. 12 1966/1967 193–212.
- [12] L. Kuipers and H. Niederreiter, Uniform distribution of sequences. Pure and Applied Mathematics. Wiley-Interscience, New York-London-Sydney, 1974.
- [13] M. Reed and B. Simon, Methods of modern mathematical physics. I. Functional analysis. Academic Press, New York-London, 1972.
- [14] V. T. Sos´ , On the distribution mod 1 of the sequence nα, Ann. Univ. Sci. Budapest, Eo¨tv¨os Sect. Math. 1 (1958), 127–134.
- [15] S. Steinerberger, Maximizing smooth functions over toroidal geodesics. arXiv:1805.02601. To appear in Bull. Aust. Math. Soc.
- [16] G. Szego¨, Orthogonal polynomials. Fourth edition. American Mathematical Society, Colloquium Publications, Vol. XXIII. American Mathematical Society, Providence, R.I., 1975.


- [17] T. Tao, Nonlinear dispersive equations. Local and global analysis. CBMS Regional Conference Series in Mathematics, 106. Published for the Conference Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society, Providence, RI, 2006.


Hausdorff Center for Mathematics, 53115 Bonn, Germany E-mail address: goncalve@math.uni-bonn.de

School of Mathematics, University of Birmingham, Edgbaston, Birmingham, B15 2TT, England E-mail address: d.oliveiraesilva@bham.ac.uk

Department of Mathematics, Yale University, New Haven, CT 06511, USA E-mail address: stefan.steinerberger@yale.edu

