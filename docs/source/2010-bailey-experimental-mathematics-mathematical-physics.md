---
type: source
kind: paper
title: Experimental Mathematics and Mathematical Physics
authors: David H. Bailey, Jonathan M. Borwein, David Broadhurst, Wadim Zudilin
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1005.0414v1
source_local: ../raw/2010-bailey-experimental-mathematics-mathematical-physics.pdf
topic: general-knowledge
cites:
---

Contemporary Mathematics

# arXiv:1005.0414v1[math-ph]3May2010

## Experimental Mathematics and Mathematical Physics

David H. Bailey, Jonathan M. Borwein, David Broadhurst, and Wadim Zudilin

Abstract. One of the most eﬀective techniques of experimental mathematics is to compute mathematical entities such as integrals, series or limits to high precision, then attempt to recognize the resulting numerical values. Recently these techniques have been applied with great success to problems in mathematical physics. Notable among these applications are the identiﬁcation of some key multi-dimensional integrals that arise in Ising theory, quantum ﬁeld theory and in magnetic spin theory.

### 1. Introduction

One of the most eﬀective techniques of experimental mathematics is to compute mathematical entities to high precision, then attempt to recognize the resulting numerical values. Techniques for eﬃciently performing basic arithmetic operations and transcendental functions to high precision have been known for several decades, and within the past few years these have been extended to deﬁnite integrals, sums of inﬁnite series and limits of sequences. Recognition of the resulting numerical values is typically done by calculating a list of n possible terms on the right-hand side of an identity, also to high precision, then applying the pslq algorithm [21, 11] to see if there is a linear relation in this set of n + 1 values. If pslq does ﬁnd a credible relation, then by solving this relation for the value in question, one obtains a formula. These techniques have been described in detail in [14], [15], and [9].

In almost applications of this methodology, both in sophistication and in computation time, the most demanding step is the computation of the key value to suﬃcient precision to permit pslq detection. As we will show below, computation of some high-dimensional integrals, for instance, often requires several hours on a highly parallel computer system. In contrast, applying pslq to ﬁnd a relation among, say, 20 candidate terms, each computed to 500-digit precision, usually can be done on a single-CPU system in less than a minute.

In our studies of deﬁnite integrals, we have used either Gaussian quadrature (in cases where the function is well behaved on a closed interval) or the “tanh-sinh”

D. H. Bailey supported in part by the Director, Oﬃce of Computational and Technology Research, Division of Mathematical, Information, and Computational Sciences of the U.S. Department of Energy, under contract no. DE-AC02-05CH11231. J. M. Borwein supported in part by ARC.

1

c 0000 (copyright holder)

quadrature scheme due to Takahasi and Mori [29] (in cases where the function has an inﬁnite derivative or blow-up singularity at one or both endpoints). For many integrand functions, these schemes exhibit “quadratic” or “exponential” convergence – dividing the integration interval in half (or, equivalently, doubling the number of evaluation points) approximately doubles the number of correct digits in the result.

The tanh-sinh scheme is based on the observation, rooted in the Euler-Maclaurin

summation formula, that for certain bell-shaped integrands (namely those where the function and all higher derivatives rapidly approach zero at the endpoints of the interval), a simple block-function or trapezoidal approximation to the integral is remarkably accurate [3, pg. 180]. This principle is exploited in the tanh-sinh scheme by transforming the integral of a given function f(x) on a ﬁnite interval such as [−1,1] to an integral on (−∞,∞), by using the change of variable x = g(t), where g(t) = tanh(π/2·sinht). The function g(t) has the property that g(x) → 1 as x → ∞ and g(x) → −1 as x → −∞, and also that g (x) and all higher derivatives rapidly approach zero for large positive and negative arguments. Thus one can write, for h > 0,

N

∞

1

f(g(t))g (t)dt ≈ h

f(x)dx =

- (1) wjf(xj),


−1

−∞

j=−N

where the abscissas xj = g(hj), the weights wj = g (hj), and N is chosen large enough that terms beyond N (positive or negative) are smaller than the “epsilon” of the numeric precision being used. In many cases, even where f(x) has an inﬁnite derivative or an integrable singularity at one or both endpoints, the transformed integrand f(g(t))g (t) is a smooth bell-shaped function for which the Euler-Maclaurin argument applies. In these cases, the error in this approximation (1) decreases more rapidly than any ﬁxed power of h. Full details are given in [12].

Both Gaussian quadrature and the tanh-sinh scheme are appropriate for analytic functions on a ﬁnite interval. Functions on a semi-inﬁnite intervals can be handled by a simple transformation such as:

∞

f(t)dt =

0

1

f(t)dt +

0

1

f(1/t)dt t2

0

Oscillatory integrands such as 0 ∞(1/xsinx)p dx can be eﬃciently computed by applying a clever technique recently introduced by Ooura and Mori [26]. Let x =

g(t) = Mt/(1 − exp(−2π sinht)). Then in the case of p = 2, for instance,

2

2

∞

∞

sing(t) g(t)

sinx x

· g (t)dt

dx =

−∞

0

N

2

sing(hk) g(hk)

≈ h

· g (hk)

k=−N

Now note that if one chooses M = π/h, then for large k, the g(hk) values are all very close to kπ, so the sin(g(hk)) values are all very close to zero. Thus the sum can be truncated after a modest number of terms, as in tanh-sinh quadrature. In practice, this scheme is very eﬀective for oscillatory integrands such as this.

In the next four sections we consider Ising integrals, Bessel moment integrals, ‘box’ integrals, and hyperbolic volumes arising from quantum ﬁeld theory respectively. We then conclude with a description of very recent work on multidimensional sums: Euler sums and MZVs.

### 2. Ising integrals

In a recent study, Bailey, Borwein and Richard Crandall applied tanh-sinh quadrature, implemented using the ARPREC package, to study the following classes of integrals [8]. The Dn integrals arise in the Ising theory of mathematical physics, and the Cn have tight connections to quantum ﬁeld theory.

∞

∞

1

du1 u1 ···

dun un

4 n!

···

Cn =

2

n j=1(uj + 1/uj)

0

0

2

ui−uj ui+uj

∞

∞

4 n!

du1 u1 ···

dun un

i<j

···

Dn =

2

n j=1(uj + 1/uj)

0

0

 

 

2

1

1

uk − uj uk + uj

dt2 dt3 ···dtn,

···

En = 2

0

0

1≤j<k≤n

where (in the last line) uk = ki=1 ti.

Needless to say, evaluating these n-dimensional integrals to high precision presents a daunting computational challenge. Fortunately, in the ﬁrst case, we were able to show that the Cn integrals can be written as one-dimensional integrals:

∞

2n n!

pK0n(p)dp,

Cn =

0

where K0 is the modiﬁed Bessel function [1]. After computing Cn to 1000-digit accuracy for various n, we were able to identify the ﬁrst few instances of Cn in terms of well-known constants, e.g.,

1 (3n + 2)2

1 (3n + 1)2 −

C3 = L−3(2) =

n≥0

7 12

C4 =

ζ(3),

where ζ denotes the Riemann zeta function. When we computed Cn for fairly large n, for instance

C1024 = 0.63047350337438679612204019271087890435458707871273234...,

we found that these values rather quickly approached a limit. By using the new edition of the Inverse Symbolic Calculator, available at http://ddrive.cs.dal.ca/~isc, this numerical value can be identiﬁed as

Cn = 2e−2γ,

lim

n→∞

where γ is Euler’s constant. We later were able to prove this fact—this is merely the ﬁrst term of an asymptotic expansion—and thus showed that the Cn integrals are fundamental in this context [8].

The integrals Dn and En are much more diﬃcult to evaluate, since they are not reducible to one-dimensional integrals (as far as we can tell), but with certain symmetry transformations and symbolic integration we were able to reduce the dimension in each case by one or two. In the case of D5 and E5, the resulting 3-D integrals are extremely complicated, but we were nonetheless able to numerically evaluate these to at least 240-digit precision on a highly parallel computer system. In this way, we produced the following evaluations, all of which except the last we subsequently were able to prove:

- D2 = 1/3

- D3 = 8 + 4π2/3 − 27L−3(2)

- D4 = 4π2/9 − 1/6 − 7ζ(3)/2

E2 = 6 − 8log 2 E3 = 10 − 2π2 − 8log 2 + 32log2 2

- E4 = 22 − 82ζ(3) − 24log 2 + 176log2 2 − 256(log3 2)/3 + 16π2 log 2 − 22π2/3






E5 =? 42 − 1984Li4(1/2) + 189π4/10 − 74ζ(3) − 1272ζ(3)log 2 + 40π2 log2 2 −62π2/3 + 40(π2 log 2)/3 + 88log4 2 + 464log2 2 − 40log 2,

where Li denotes the polylogarithm function. In the case of D2, D3 and D4, these are conﬁrmations of known results. We tried but failed to recognize D5 in terms of similar constants (the 500-digit numerical value is available if anyone wishes to try). The conjectured identity shown here for E5 was conﬁrmed to 240-digit accuracy, which is 180 digits beyond the level that could reasonably be ascribed to numerical round-oﬀ error; thus we are quite conﬁdent in this result even though we do not have a formal proof.

In a follow-on study [6], we examined the following generalization of the Cn integrals:

Cn,k =

4 n!

∞

···

0

∞

1

du1 u1 ···

dun un

.

k+1

n j=1(uj + 1/uj)

0

Here we made the initially surprising discovery—now proven in [17] and in outline much earlier [13]—that there are linear relations in each of the rows of this array (considered as a doubly-inﬁnite rectangular matrix), e.g.,

0 = C3,0 − 84C3,2 + 216C3,4 0 = 2C3,1 − 69C3,3 + 135C3,5 0 = C3,2 − 24C3,4 + 40C3,6 0 = 32C3,3 − 630C3,5 + 945C3,7 0 = 125C3,4 − 2172C3,6 + 3024C3,8.

### 3. Bessel moment integrals

In a more recent study of Bessel moment integrals, co-authored with Larry Glasser [7], the ﬁrst three authors were able to analytically recognize many of the Cn,k constants in the earlier study—because, remarkably, these same integrals appear naturally in quantum ﬁeld theory (for odd k). We also discovered, and then

proved with considerable eﬀort, that with cn,k normalized by Cn,k = 2n cn,k/(n!k!), we have

√3π3 8 3

3Γ6(1/3) 32π22/3

1 4

1/2,1/2,1/2 1,1

c3,0 =

=

F2

√3π3 288 3

1 4

1/2,1/2,1/2 2,2

F2

c3,2 =

c4,0 =

c4,2 =

4 44n

∞

2n n

π4 4

n=0

=

π4 4 4

F3

1/2,1/2,1/2,1/2 1,1,1

π4 64

44F3

1/2,1/2,1/2,1/2 1,1,1

1

1

−34F3

1/2,1/2,1/2,1/2 2,1,1

3π2 16

1 −

,

where pFq denotes the generalized hypergeometric function [1]. The corresponding values for small odd second indices are c3,1 = 3L−3(2)/4, c3,3 = L−3(2)−2/3, c4,1 = 7ζ(3)/8 and c4,3 = 7ζ(3)/32 − 3/16.

Integrals in the Bessel moment study were quite challenging to evaluate numerically. As one example, we sought to numerically verify the following identity that we had derived analytically:

c5,0 =

π 2

π/2

−π/2

π/2

K(sinθ)K(sinφ)

dθ dφ,

cos2 θ cos2 φ + 4sin2(θ + φ)

−π/2

where K denotes the elliptic integral of the ﬁrst kind [1]. Note that this function has blow-up singularities on all four sides of the region of integration, with particularly troublesome singularities at (π/2,−π/2) and (−π/2,π/2) (see Figure 1). Nonetheless, after making some minor substitutions, we were able to evaluate (and conﬁrm) this integral to 120-digit accuracy (using 240-digit working precision) in a run of 43 minutes on 1024 cores of the “Franklin” system at LBNL.

In a separate study, the ﬁrst two authors studied correlation integrals for the Heisenberg spin-1/2 antiferromagnet, as given by Boos and Korepin, for a length-n spin chain [24, eqn. 2.2]:

∞

∞

∞

πn(n+1)/2 (2πi)n ·

U(x1 − i/2,x2 − i/2,··· ,xn − i/2) × T(x1 − i/2,x2 − i/2,··· ,xn − i/2)dx1 dx2 ···dxn

···

P(n) :=

−∞

−∞

−∞

where U(x1 − i/2,x2 − i/2,··· ,xn − i/2) = 1≤k<j≤n

sinh[π(xj − xk)] 1≤j≤n in coshn(πxj)

(xj − i/2)j−1(xj + i/2)n−j 1≤k<j≤n(xj − xk − i)

T(x1 − i/2,x2 − i/2,··· ,xn − i/2) = 1≤j≤n

.

They computed numerical values for these n-fold integrals to as great a precision as we could, then attempted to recognize them using pslq. They found

![image 1](<2010-bailey-experimental-mathematics-mathematical-physics_images/imageFile1.png>)

Figure 1. Plot of c5,0 integrand function

the following, which conﬁrm some earlier results obtained by others using physical symmetry methods:

- P(1) =

- 1

- 2

P(2) =

1

- 3 −


- P(3) =

1 4 − log 2 +

3 8

ζ(3)

- P(4) =

1 5 − 2log 2 +

173 60

ζ(3) −

11 6

ζ(3)log 2 −

51 80

ζ2(3) −

55 24

ζ(5) +

85 24

ζ(5)log 2

- P(5) =


1 3

log 2

1 6 −

10 3

281 24

45 2

489 16

6775 192

ζ2(3) −

ζ(3) −

ζ(3)log 2 −

log 2 +

ζ(5)

425 64

12125 256

6223 256

1225 6

ζ2(5) +

ζ(5)log 2 −

ζ(3)ζ(5) −

ζ(7) −

+

11515 64

42777 512

ζ(7)log 2 +

ζ(3)ζ(7)

These computations underscore the rapidly increasing cost of computing integrals in higher dimensions. Precision levels, processor counts and run times are shown in Table 1.

|n<br><br>|Digits|Processors|Run Time|
|---|---|---|---|
|2<br><br>3<br><br>4<br><br>5<br><br>6<br><br><br>|120 120<br><br>60 30<br><br>6|1 8<br><br>64 256 256<br><br>|10 sec. 55 min. 27 min. 39 min.<br><br>59 hrs.|


Table 1. Run times and precision levels for spin integral calculations

4. Box integrals Let us deﬁne box integrals for dimension n as

Bn(s) :=

∆n(s) :=

1

···

0

1

···

0

1

0

1

0

r12 + ··· + rn2 s/2 dr1 ···drn

(r1 − q1)2 + ··· + (rn − qn)2 s/2 dr1 ···drn dq1 ···dqn.

As explained in previous treatments [4, 5], these integrals have several physical interpretations:

- (1) Bn(1) is the expected distance of a random point from the origin (or from any ﬁxed vertex) of the n-cube.
- (2) ∆n(1) is the expected distance between two random points of the n-cube.
- (3) Bn(−n + 2) is the expected electrostatic potential in an n-cube whose origin has a unit charge. Such statements presume that electrostatic potential in n dimensions is V (r) = 1/rn−2, and say log r for n = 2; in other words, the negative powers of r can also have physical meaning.
- (4) ∆n(−n + 2) is the expected electrostatic energy between two points in a uniform cube of charged “jellium.”
- (5) Recently integrals of this type have arisen in neuroscience e.g., the average distance between synapses in a mouse brain.


Note that the deﬁnitions show immediately that both ∆n(2m) and Bn(2m) are rational when m,n are natural numbers. A pivotal, original treatment on box integrals is the 1976 work of Anderssen et al [2]. There have been interesting modern treatments of the Bn and related integrals, as in [10], [14, pg. 208], [32], and [30]. Related material may also be found in [23, 31].

Like the Ising integrals, some of these n-dimensional integrals are reducible to 1-dimension integrals. For instance, we found that

+ √π uerf(u))3 u6

2

∞

(−1 + e−u

2 √π

∆3(−1) =

du.

0

After calculating a 400-digit numerical value for this constant, we were able to recognize it as

√

√

√

√

1 15

2 − 12

3 − 10π + 30log(1 +

∆3(−1) =

6 + 6

2) + 30log(2 +

3) .

A selection of results that we have found are shown in Tables 2, 3, 4 and 5. Here G denotes Catalan’s constant, namely, G := n≥0(−1)n/(2n + 1)2, θ =

|n|s|Bn(s)|
|---|---|---|
|any 1|even s ≥ 0 s = −1<br><br>|rational, e.g.: B2(2) = 2/3 1 s+1<br><br>|
|2 2 2 2 2 2<br><br>|−4 −3 −1 1 3 s = −2|−14 − π8<br><br>−<br><br>√2<br><br>2log(1 + √2)<br><br>1<br><br>3<br><br>√2 + 13 log(1 + √2)<br><br>7 20<br><br>√2 + 203 log(1 + √2)<br><br>2<br><br>2+s 2F1 12,−2s; 32;−1<br><br><br>|
|3 3 3 3 3 3|−5 −4 −2 −1 1 3<br><br>|−16<br><br>√3 − 121 π<br><br>−32<br><br>√2arctan √12<br><br>−3G + 23π log(1 + √2) + 3Ti2(3 − 2√2)<br><br>−14π + 32 log 2 + √3<br><br>1<br><br>4<br><br>√3 − 241 π + 12 log 2 + √3<br><br>2<br><br>5<br><br><br><br><br>√3 − 601 π + 207 log 2 + √3<br><br>|


Table 2. Recent evaluations of Box integrals

|n|s<br><br>|Bn(s)|
|---|---|---|
|4 4 4 4 4<br><br>|−5 −3 −2 −1 1|−<br><br>√8 arctan √ 18 4 G − 12Ti2(3 − 2√2)<br><br>π log 2 + √3 − 2G − π<br><br>2<br><br>8<br><br>2log 3 − 23 G + 2Ti2 3 − 2√2 −<br><br>√8 arctan √ 18<br><br>2 5 − 10G + 103 Ti2 3 − 2√2 + log 3 − 7<br><br>√2 10 arctan √ 18<br><br>|
|5<br><br>5 5<br><br>5|−3<br><br>−2 −1<br><br>1<br><br>|110<br><br>9 G − 10 log 2 −<br><br>√3 θ − 81 π2 −10Cl2 13 θ + 13 π + 10Cl2 13 θ − 16 π + 103 Cl2 θ + 16 π<br><br>+203 Cl2 θ + 43 π − 103 Cl2 θ + 35 π − 203 Cl2 θ + 116 π 8 3 B5(−6) − 13 B5(−4) + 25 π log 3 + 10Ti2 13 − 10G<br><br>−11027 G + 103 θ log 2 −<br><br>√3 + 481 π2<br><br>+5 log 1+<br><br>√5 2 − 52<br><br>√3arctan √ 115<br><br>+103 Cl2 13 θ + 13 π − 103 Cl2 13 θ − 61 π − 109 Cl2 θ + 61 π −209 Cl2 θ + 43 π + 109 Cl2 θ + 35 π + 209 Cl2 θ + 116 π<br><br>−7781 G + 79 θ log 2 −<br><br>√3 + 3601 π2 + 61 √5<br><br>+103 log 1+<br><br>√5 2 − 43<br><br>√3arctan √ 115<br><br>+79 Cl2 13 θ + 13 π − 79 Cl2 13 θ − 61 π − 277 Cl2 θ + 16 π −1427 Cl2 θ + 43 π + 277 Cl2 θ + 53 π + 1427 Cl2 θ + 116 π<br><br>|


Table 3. Recent evaluations of Box integrals, continued; here θ := arctan 16−3

√15 11

|n<br><br>|s<br><br>|∆n(s)|
|---|---|---|
|2 2 2|−5 −1 1<br><br>|4 3 + 89√2<br><br>4 3 − 34<br><br>√2 + 4log(1 + √2)<br><br>2 15 + 151 √2 + 13 log(1 + √2)<br><br>|
|3 3<br><br>3 3 3|−7 −2<br><br>−1 1 3<br><br>|4<br><br>5 − 16<br><br><br>√2<br><br>15 + 2<br><br>√3 5 + 15π<br><br>2π − 12 G + 12Ti2 3 − 2√2 + 6π log 1 + √2 +2log 2 − 52 log 3 − 8√2arctan √ 12<br><br>2 5 − 23π + 25√2 − 45<br><br>√3 + 2log 1 + √2 + 12log 1+<br><br>√√23 − 4log 2 + √3 −11821 − 23 π + 3421 √2 − 47<br><br>√3 + 2 log 1 + √2 + 8 log 1+<br><br>√√23<br><br>−1051 − 1052 π + 84073 √2 + 351 √3 + 563 log 1 + √2 + 1335 log 1+<br><br>√√23<br><br>|


- Table 4. Recent evaluations of Box integrals, continued

|n<br><br>|s|∆n(s)|
|---|---|---|
|4<br><br>4<br><br>4<br><br>4<br><br>|−3<br><br>−2<br><br>−1<br><br>1|−12815 + 163 π − 8 log 1 + √2 − 32 log 1 + √3 + 16 log 2 + 20 log 3 −85<br><br>√2 + 325 √3 − 32√2arctan √ 18 − 96Ti2 3 − 2√2 + 32G<br><br>−1615 π √3 − 83 π log 2 + 163 π log 1 + √3 − 23 π2 + 45 π<br><br>+85 √2arctan 2√2 + 25 log 3 − 4π log √2 − 1<br><br>+8Ti2 3 − 2√2 − 403 G − 38 log 2<br><br>−152315 − 158 π − 165 log 2 + 25 log 3 + 10568 √2 − 1635<br><br>√3 + 45 log 1 + √2<br><br>+325 log 1 + √3 − 83 G + 8Ti2 3 − 2√2 − 85<br><br>√2arctan √2/4<br><br>−13523 − 31516 π − 10552 log 2 + 197420 log 3 + 63073 √2 + 1058 √3<br><br>+141 log 1 + √2 + 104105 log 1 + √3 −10568<br><br>√2arctan √ 18 − 154 G + 54 Ti2 3 − 2√2<br><br>|
|5<br><br>|1|−1279567 G − 1894 π + 3154 π2 − 3465449 + 623703239 √2 + 3465568 √3 − 6237380<br><br>√5<br><br>+295252 log 3 + 541 log 1 + √2 + 2063 log 2 + √3 + 18964 log 1+<br><br>√5 2<br><br>−7363<br><br>√2arctan √ 18 − 218<br><br>√3arctan √ 115 + 10463 log 2 −<br><br>√3 θ<br><br>+57 Ti2 3 − 2√2 + 10463 Cl2 13 θ + 13 π − 10463 Cl2 13 θ − 61 π −104189 Cl2 θ + 16 π − 208189 Cl2 θ + 43 π +104189 Cl2 θ + 35 π + 208189 Cl2 θ + 116 π<br><br>|


- Table 5. Recent evaluations of Box integrals, continued


arctan (16 − 3√15)/11 , Cl denotes Clausen’s function,

Cl2(θ) =

sin(nθ) n2

,

n≥1

and Ti denotes Lewin’s inverse-tan function,

Ti2(x) =

x2n+1 (2n + 1)2

(−1)n

.

n≥0

### 5. Clausen functions and hyperbolic volumes

In an unpublished 1998 study [16] two of the present authors (Borwein and Broadhurst) identiﬁed 998 closed hyperbolic 3-manifolds whose volumes are rationally related to Dedekind zeta values, with coprime integers a and b giving

(−D)3/2 (2π)2n−4

ζK(2) 2ζ(2)

- a

- b


vol(M) =

- (2)

for a manifold M whose invariant trace ﬁeld K has a single complex place, discriminant D, degree n, and Dedekind zeta value ζK(2). While the existence of integers a,b can be established, via algebraic K-theory as in [35], for the most part it was and is not possible to specify the rational a/b other than empirically [35].

The simplest identity implicit in (2) devolves to

3Cl2(α) − 3Cl2(2α) + Cl2(3α) =

7√7 4

- (3) L−7(2),

with α = 2arctan(√7), as is recorded in [14, p. 91]. Here L−7(2) := n>0 n7 /n2 is the primitive Dirichlet L-series modulo 7 evaluated at 2 where n7 is the Legendre symbol. This was rewritten in equivalent and more self-contained form as

24 7√7

- π/2
- π/3


log

tant + √7 tant −

√7

- (4) dt = L−7(2)

in [9, p. 61]—and elsewhere.

Note that the integrand function of (4) has a nasty singularity at arctan(√7) (see Figure 2). However, we were able to numerically evaluate this integral to 20,000-digit accuracy, by splitting the integral into two parts, namely on the intervals [π/3,arctan(√7)] and [arctan(√7),π/2]. Note that tanh-sinh quadrature can be used on each part, since it can readily handle blow-up singularities at one or both endpoints of the interval of integration. This run required 46 minutes on 1024 CPUs of the Virginia Tech Apple cluster. The right-hand side was also evaluated, using Mathematica, to 20,000-digit precision. The two values agreed to 19,995 digits [9, pg. 61]. Alternative representations of the integral in (4) are given in [20].

We shall now provide a proof of Eqn. (3) and hence of Eqn. (4). Actually, an equivalent (if not obviously so) form of identity (3), namely

ζQ(√

−7)(2) =

π2 3√7

A cot

π 7

+ A cot

2π 7

+ A cot

4π 7

- (5)


√

√

√

√

√

2π2 7√7

7 − 2

=

2A(

3) with the notation

7) + A(

7 + 2

3) + A(

x

4 1 + t2

1 1 + t2

log

dt = Cl2(2arccotx),

A(x) :=

0

![image 2](<2010-bailey-experimental-mathematics-mathematical-physics_images/imageFile2.png>)

Figure 2. Plot of integrand function in (4)

is already established in [33]. The ﬁrst equality in (5) can be written as

π2 6

ζQ(√

−7)(2) =

- (6) L−7(2) = ζ(2)L−7(2).


On noting that

√7 + i 2√2

√

cotarg

=

7

(1 + i√7)(1 ∓ i√3) 4√2

√

√

7 ± 2

cotarg

=

3

einθ n2

Cl2(θ) = Im

,

n≥1

we can translate the remaining, highly non-trivial, part of (5) to

√

2A(

√

7) + A(

7 + 2

= 2Im

n≥1

#### +Im

n≥1

√

√

√

7 − 2

3) + A(

3)

√7 + i 2√2

2n

1 n2

1 n2

#### + Im

n≥1

(1 + i√7)(1 + i√3) 4√2

2n

1 n2

#### .

(1 + i√7)(1 − i√3) 4√2

2n

Now we use

(1 + i√7)(1 + i√3) 4√2

2

#### = µe2πi/3 (1 + i√7)(1 − i√3) 4√2

2

= µe−2πi/3

√7 + i 2√2

3 + i√7 4

2n

n

= −Im(−µ)n for n = 0,1,2,...,

Im

= Im

where µ := (−3 + i√7)/4 has absolute value 1 and arg µ = α = 2arctan(√7), to write the latter equality as

√

√

√

√

√

7 − 2

- (7) 3)

= Im

n≥1

µn(e2πin/3 + e−2πin/3 − 2(−1)n) n2

= Im

n≥1

µn n2 −

n≥1

µ2n n2

+

1 3 n≥1

µ3n n2

= Cl2(α) − Cl2(2α) +

1 3

Cl2(3α), where we have applied the following two standard identities

- 1

- 2 n≥1

x2n n2

=

n≥1

xn n2

+

n≥1

(−1)nxn n2 1

- 3 n≥1


x3n n2

=

n≥1

xn n2

+

n≥1

e2πin/3xn n2

+

n≥1

e−2πin/3xn n2

for the dilogarithm function. It remains to substitute our ﬁnding (7) into (5) and

(6) to ﬁnish a proof of identity (3).

The equivalent identity (4) can be obtained by some reasonably straightforward but tedious manipulation of the Clausen integral representation

Cl2(θ) = −

θ

0

- (8) log |2sinσ|dσ

for 0 ≤ θ < 2π, and an appropriate change of variables. As Don Zagier points out in [33]

“we observe that the values of A(x) at algebraic arguments satisfy many non-trivial linear relations over the rational numbers; I know of no direct proof, for instance, of the equality of the righthand sides of Eqns. (5) and (6).”

Zagier’s Eqns. (5) and (6) are our identity (5). Another result in [33], Theorem 3, implies the identity

ζQ(√

−7)(2) =

2π2 21√7

3A

1 √7

+ 3A

3 √7

+ A

5 √7

- (9) ,


2A(

7) + A(

7 + 2

3) + A(

which may be thought of as complimentary to Eqn. (5) (see pg. 300 in [33] for details). Since

√

1 √7

A

= Cl2 2arctan

7

√7 3 A

3 √7

A

= Cl2 2arctan

√7 5

5 √7

, and

= Cl2 2arctan

√7 3

√7 5

√

= −2α + 2π, 2arctan

2arctan

7 = α, 2arctan

= 3α − 2π,

identity (3) follows from (9) immediately. Thus paper [33] contains two diﬀerent proofs of (3)!

Let us clarify the current status and somewhat-complicated history of various of the discoveries in [16]. Until recently the authors of [16] after discussion with Zagier believed (5) to be unproven. It was only when Zudilin spent time with Don Zagier in 2008 that he remembered his equivalent pre-dilogarithm (see [34, 35]) result in [33]. Two of the present authors (Borwein and Broadhurst) [16] wrote

“While the existence of such relations is understood [33, 34, 35], their precise forms appear to be unpredictable, thus far, by deductive mathematics. They are therefore ripe for the application of experimental mathematics.”

The great bulk of the results recorded in [16] remain unproven. They were discovered by intensive physically and mathematically motivated computation, using SnapPea, Pari-GP, Maple, and other tools.

Indeed, the cases

D = −8,−11,−15,−20,−24

are challenging enough! These ﬁve respectively yield the following conjectured identities—each of which is open. First

6π 8

2π 8

27Cl2(θ2) − 9Cl2(2θ2) + Cl2(3θ2) =? 8Cl2

- (10) ,

with θ2 := 2arctan√2. Secondly,

15Cl2(θ11) − 10Cl2(2θ11) + Cl2(5θ11) =? 11

5

k=1

k 11

Cl2

2πk 11

- (11) ,

where θ11 := 2arctan√11 and 11 k is the Jacobi (or Legendre) symbol for the Dirichlet character. Thirdly,

- (12) 24Cl2(θ5,3) − 12Cl2(2θ5,3) − 8Cl2(3θ5,3) + 6Cl2(4θ5,3)


+ 8Cl2

7

k 15

2πk 15

=? 15

Cl2

k=1

,

with θ5,3 := 2arctan 5/3. Fourthly

- (13) 36Cl2(θ5) − 30Cl2(2θ5) + 4Cl2(3θ5) + 3Cl2(4θ5)

=? 20

k∈{1,3,7,9}

Cl2

2πk 20

,

with θ5 := 2arctan√5. Finally,

- (14) 60Cl2(θ3,2) − 18Cl2(2θ3,2) − 4Cl2(3θ3,2) + 3Cl2(4θ3,2)

=? 24

k∈{1,5,7,11}

Cl2

2πk 24

,

with θ3,2 := 2arctan 3/2. So, for the ﬁfth time, we have a relation that is as easy to check numerically as it appears hard to derive. Needless to say, it would be interesting to check whether Zagier’s 1986 theorems in [33] work for all such small values of D; Theorem 2 in [33] looks suﬃciently powerful for this task, while Theorem 3 therein depends critically on a delicate geometric construction and might be of use for D = −11,−15,−20. Moreover, is there a more transparent method to deduce identity (3) as well as (10)–(14)?

As another example of the ubiquity of Clausen values, we complete this section with the most diﬃcult integral evaluation required in [5]:

K1 :=

4

3

arcsec(x) √x2 − 4x + 3

- (15) dx


θ 3 −

θ 3 −

π 6 −

3 11

3 11

= 3Cl2

Cl2

Cl2

15 11

3 11

2π 3 −

π 6 −

−

Cl2 θ −

Cl2 θ +

√

π 2

log 2 −

+ 2θ −

3 . Here

16 − 3√15 11

θ := arctan

θ 3

π 6

+

+

3 11

π 6

Cl2 θ −

π 3

18 11

Cl2 θ −

.

It may well be that this closed form (15) for K1 can be further simpliﬁed.

### 6. Relations between MZVs and Euler sums

We conclude with an application of experimental mathematics to discover relations between multiple zeta values (MZVs) of the form

1 ns

ζ(s1,s2,...,sk) =

1 ...ns

k

1

k

n1>n2>...>nk>0

#### with weight w = ki=1 si and depth k and Euler sums of the more general form

n1 1 ... n

k

k ns

1 ...ns

1

k

k

n1>n2>...>nk>0

with signs i = ±1. Both types of sum occur in evaluations of Feynman diagrams in quantum ﬁeld theory [18, 19] as mentioned in [14]. These sums are described in some mathematical detail in [15, Chapter 3].

First we recall the ﬁrst Broadhurst–Kreimer conjectures (see [18] and also [15]) for the enumeration of primitive MZVs and Euler sums of a given weight and depth. Let En,k be the number of independent Euler sums at weight n > 2 and depth k that cannot be reduced to primitive Euler sums of lesser depth and their products. It is conjectured that [18]

x3y (1 − xy)(1 − x2)

n,k =? 1 −

(1 − xnyk)E

.

n>2 k>0

We emphasise that, since the irrationality of odd values of depth-one MZVs (i.e., Riemann’s ζ) is not settled, such dimensionality conjectures are necessarily experimental. Now let Dn,k be the number of independent MZVs at weight n > 2 and depth k that cannot be reduced to primitive MZVs of lesser depth and their products. Thus we believe that D12,4 = 1, since there is no known relationship between the depth-4 sum ζ(6,4,1,1) = j>k>l>m 1/(j6k4lm) and MZVs of lesser depth or their products. It is conjectured that [18]

x12y2(1 − y2) (1 − x4)(1 − x6)

x3y 1 − x2

n,k =? 1 −

(1 − xnyk)D

+

.

n>2 k>0

The ﬁnal Broadhurst–Kreimer conjecture concerns the existence of relations between MZVs and Euler sums of lesser depth. The now proven relation [19]

ζ(6,4,1,1) =

64 9

371 144

107 24

ζ(9,3) +

ζ(9,3) + 3ζ(2)ζ(7,3) +

ζ(5)ζ(7)

1 12

3131 144

7 2

ζ4(3) −

ζ(2)ζ2(5) + 10ζ(2)ζ(3)ζ(7)

+

ζ(3)ζ(9) +

3 5

1 5

18 35

117713 2627625

+ζ2(2)

ζ(2)ζ2(3) −

ζ4(2)

ζ(5,3) −

ζ(3)ζ(5) −

shows that the depth-4 MZV on the left can be expressed in terms of Euler sums of lesser depth and their products. In fact, it suﬃces to include the alternating double sum ζ(9,3) = j>k>0(−1)j+k/(j9k3), where a bar above an argument of ζ serves to indicate an alternating sign. In the language of [18, 19] this is a “pushdown”, at weight 12, of an MZV of depth 4 to an Euler sum of depth 2. Let Mn,k be the number of primitive Euler sums of weight n > 2 and depth k whose products furnish a basis for all MZVs. It is conjectured that [18]

x3y 1 − x2

n,k =? 1 −

(1 − xnyk)M

.

n>2 k>0

Then by comparison of the output D21,3 = 6, D21,5 = 9, D21,7 = 1 of (16) with the output M21,3 = 9, M21,5 = 7 of (16) we conclude that at weight 21, for example, three pushdowns are expected from depth 5 to depth 3 and one from depth 7 to depth 5.

By massive use of the computer algebra language form, to implement the shuﬄe algebras of MZVs and Euler sums, the authors of [19] were recently able to reduce all Euler sums with weight w ≤ 12 and all MZVs with w ≤ 22 to concrete bases whose sizes are in precise agreement with conjectures (16,16). Moreover,

further support to these conjectures came by studying even greater weights, w ≤ 30, using modular arithmetic. However, such algebraic methods were insuﬃcient to investigate pushdown at weight 21. Instead the authors resorted to a combination of the pslq methods reported in [11] with the lll algorithm [25] of Pari-GP [27], ﬁnding empirical forms for precisely the expected numbers of pushdowns at all weights w ≤ 21. Most notable of these is the pushdown from depth 7 to depth 5, at weight 21, in the empirical form

326 81

ζ(6,2,3,3,5,1,1) =? −

ζ(3,6,3,6,3) + {depth − 5 MZV products}

where the remaining 150 terms are formed by MZVs with depth no greater than 5, and their products.

It is proven, by exhaustion, in [19] that the shuﬄe algebras do not allow the sum ζ(6,2,3,3,5,1,1) in equation (16) to be reduced to MZVs of depth less than 7. It is also proven that all other MZVs of weight 21 and depth 7 are reducible to ζ(6,2,3,3,5,1,1) and MZVs of depth less than 7. Yet it appears to be far beyond the limits of current algebraic methods to prove that inclusion of the rather striking depth-5 alternating sum

ζ(3,6,3,6,3) =

(−1)k+m (jk2lm2n)3

,

j>k>l>m>n>0

with the rather simple coeﬃcient −326/81, leaves the remainder reducible to MZVs of depth no greater than ﬁve.

Thus we are left with a notable empirical validation of a pushdown conjecture relevant to quantum ﬁeld theory, crying out for elucidation.

### 7. Conclusion

We have presented here a brief survey of the rapidly expanding applications of experimental mathematics (in particular, the application of high-precision arithmetic) in mathematical physics. It is worth noting that all but the penultimate of these examples have arisen in the past ﬁve to ten years. Eﬀorts to analyze integrals that arise in mathematical physics have underscored the need for signiﬁcantly faster schemes to produce high-precision values of 2-D, 3-D and higher-dimensional integrals. Along this line, the “sparse grid” methodology has some promise [28, 36].

Current research is aimed at evaluating such techniques for high-precision applications. To illustrate the diﬃculty, we leave as a challenge to the reader the computation of the triple integral

C

f(u,v,w) − 2dudv dw = 1.1871875...,

where C := [0,1/2]3 and

f(u,v,w) := cos2 ((v + w)π) + cos2 ((u − v)π) + cos2 ((u + w)π) +cos2 (vπ) + cos2 (uπ) + cos2 (wπ) to, say, 32 decimal digit accuracy.

### References

- [1] Milton Abramowitz and Irene A. Stegun, ed., Handbook of Mathematical Functions, Dover, New York, 1972.
- [2] R. Anderssen, R. Brent, D. Daley, and P. Moran, “Concerning 1

0 · · · 0 1(x21 + · · · x2n)12 dx1 · · · dxn and a Taylor series method,” SIAM Journal of Applied Mathematics, vol. 30 (1976), 22–30.

- [3] Kendall E. Atkinson, Elementary Numerical Analysis, John Wiley, 1993.
- [4] David H. Bailey, Jonathan M. Borwein and Richard E. Crandall, “Box integrals,” Journal of Computational and Applied Mathematics, vol. 206 (2007), 196–208.
- [5] David H. Bailey, Jonathan M. Borwein and Richard E. Crandall, “Advances in the Theory of Box Integrals,” to appear in Mathematics of Computation; available at http://crd.lbl.gov/~dhbailey/dhbpapers/BoxII.pdf.
- [6] David H. Bailey, David Borwein, Jonathan M. Borwein and Richard Crandall, “Hypergeometric forms for Ising-class integrals,” Experimental Mathematics, vol. 16 (2007), no. 3, 257–276.
- [7] David H. Bailey, Jonathan M. Borwein, David Broadhurst and M. L. Glasser, “Elliptic integral evaluations of Bessel moments,” Journal of Physics A: Mathematics and General, vol. 41 (2008), 205203.
- [8] David H. Bailey, Jonathan M. Borwein and Richard E. Crandall, “Integrals of the Ising class,” Journal of Physics A: Mathematics and General, vol. 39 (2006), 12271–12302.
- [9] David H. Bailey, Jonathan M. Borwein, Neil Calkin, Roland Girgensohn, Russell Luke and Victor Moll, Experimental Mathematics in Action, A. K. Peters, Wellesley, MA, 2007.
- [10] David H. Bailey, Jonathan M. Borwein, Vishaal Kapoor, and Eric W. Weisstein, “Ten problems in experimental mathematics,” American Mathematical Monthly, vol. 113 (2006), 481–509.
- [11] D. H. Bailey and D. Broadhurst, “Parallel integer relation detection: Techniques and applications,” Mathematics of Computation, vol. 70, no. 236 (2000), 1719–1736.
- [12] D. H. Bailey, X. S. Li and K. Jeyabalan, “A comparison of three high-precision quadrature schemes,” Experimental Mathematics, vol. 14 (2005), 317–329.
- [13] P. Barrucand, “Sur la somme des puissances des coeﬃcients multinomiaux et les puissances successives d’une fonction de Bessel,” Comptes rendus hebdomadaires des s´eances de l’Acad´emie des sciences, vol. 258 (1964), 5318–5320.
- [14] Jonathan M. Borwein and David H. Bailey, Mathematics by Experiment: Plausible Reasoning in the 21st Century, A. K. Peters, Natick, MA, second edition, 2008.
- [15] Jonathan M. Borwein, David H. Bailey and Roland Girgensohn, Experimentation in Mathematics: Computational Routes to Discovery, A. K. Peters, Natick, MA, 2004.
- [16] J. M. Borwein and D. J. Broadhurst, “Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links,” [arXiv:hep-th/9811173], 19 November 1998.
- [17] Jonathan M. Borwein and Bruno Salvy, “A proof of a recursion for Bessel moments,” Experimental Mathematics, vol. 17 (2008), 223–230.
- [18] D. J. Broadhurst and D. Kreimer, Association of multiple zeta values with positive knots via Feynman diagrams up to 9 loops, Phys. Lett. B 393 (1997) 403–412, [arXiv:hep-th/9609128].
- [19] J. Blu¨mlein, D. J. Broadhurst and J. A. M. Vermaseren, The Multiple Zeta Value Data Mine, [arXiv:math-ph/09072557].
- [20] Mark W. Coﬀey, “Alternative evaluation of a ln tan integral arising in quantum ﬁeld theory,” [arXiv:0810.5077], November 2008.
- [21] Helaman R. P. Ferguson, David H. Bailey and Stephen Arno, “Analysis of PSLQ, an integer relation ﬁnding algorithm,” Mathematics of Computation, vol. 68, no. 225 (Jan 1999), 351–369.
- [22] J. A. M. Vermaseren, New features of FORM, [arXiv:math-ph/0010025].
- [23] Wolfram Koepf, Hypergeometric Summation: An Algorithmic Approach to Summation and Special Function Identities, American Mathematical Society, Providence, RI, 1998.
- [24] H. Boos and V. Korepin, “Evaluation of integrals representing correlations in the XXX Heisenberg spin chain,” in: MathPhys Odyssey, 2001, Prog. Math. Phys., vol. 23, Birkh¨auser, Boston, 2002, 65–108.


- [25] A. K. Lenstra, H. W. Lenstra and L. Lov´asz, Factoring Polynomials with Rational Coeﬃcients, Math. Ann. 261 (1982) 515-534.
- [26] T. Ooura and M. Mori, “Double exponential formulas for oscillatory functions over the half inﬁnite interval,” Journal of Computational and Applied Mathematics, vol. 38 (1991), 353–360.
- [27] The PARI/GP page: http://pari.math.u-bordeaux.fr/
- [28] S. Smolyak, “Quadrature and interpolation formulas for tensor products of certain classes of functions,” Soviet Math. Dokl., vol. 4 (1963), 240243.
- [29] H. Takahasi and M. Mori, “Double exponential formulas for numerical integration,” Publications of RIMS, Kyoto University, vol. 9 (1974), pg. 721–741.
- [30] Michael Trott, Private communication, 2005.
- [31] Michael Trott, “The area of a random triangle,” Mathematica Journal, vol. 7 (1998), 189–198.
- [32] Eric Weisstein, “Hypercube line picking,” available at http://mathworld.wolfram.com/HypercubeLinePicking.html.
- [33] D. Zagier, “Hyperbolic manifolds and special values of Dedekind zeta-functions,” Invent. Math., vol. 83 (1986), 285–301.
- [34] D. Zagier,“The remarkable dilogarithm,” J. Math. Phys. Sci., vol. 22 (1988), 131–145.
- [35] D. Zagier, “Polylogarithms, Dedekind zeta functions and the algebraic K-theory of ﬁelds,” in: Arithmetic algebraic geometry (Texel, 1989), Progr. Math., vol. 89, Birkh¨auser, Boston, 1991, 391–430.
- [36] C. Zenger, “Sparse grids,” in W. Hackbusch, ed., Parallel Algorithms for Partial Diﬀerential Equations, vol. 31 of Notes on Numerical Fluid Mechanics, Vieweg, 1991.


D. H. Bailey: Lawrence Berkeley National Laboratory, Berkeley, CA 94720 E-mail address: dhbailey@lbl.gov

J. M. Borwein: School of Mathematical and Physical Sciences, University of Newcastle, Callaghan, NSW 2308, Australia E-mail address: jonathan.borwein@newcastle.edu.au

D. Broadhurst: Physics and Astronomy Department, Open University, Milton Keynes MK7 6AA, UK E-mail address: D.Broadhurst@open.ac.uk

W. Zudilin: School of Mathematical and Physical Sciences, University of Newcastle, Callaghan, NSW 2308, Australia E-mail address: wadim.zudilin@newcastle.edu.au

