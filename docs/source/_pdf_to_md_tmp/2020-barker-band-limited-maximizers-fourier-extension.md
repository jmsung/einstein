# arXiv:2002.05118v5[math.CA]4Mar2022

## BAND-LIMITED MAXIMIZERS FOR A FOURIER EXTENSION INEQUALITY ON THE CIRCLE, II

JAMES BARKER, CHRISTOPH THIELE, AND PAVEL ZORIN-KRANICH

Abstract. Among the class of functions on the circle with Fourier modes up to degree 120, constant functions are the unique real-valued maximizers for the endpoint Tomas-Stein inequality.

1. Introduction

This article continues the investigation in [OTZ19] of extremizers of the classical Tomas-Stein [Tom75] Fourier extension inequality on the circle in classes of band limited functions. We improve the main theorem in [OTZ19], which concerns functions with Fourier modes up to degree 30, towards degree N = 120.

Theorem 1. Let f ∈ L2 S1 be real-valued. Assume that fn = 0 for all n > 120. Then

Φ(f) ≤ Φ(1), with equality if and only if f is constant.

Here, S1 is the unit circle in the complex plane, and fn are the coeﬃcients in the Fourier series

fnωn. The Tomas-Stein functional

f(ω) =

n∈Z

6 L6(R2)

f −L26(S1) is the sixth power of the norm quotient for the Fourier extension map fσ(x) :=

Φ(f) := fσ

f(ω)e−ix·ω dσω, x ∈ R2 ,

S1

where we identify the complex plane with the Euclidean plane R2 when we take the dot product x · ω, and σ is the arclength measure on the circle. The constant function 1 is conjectured to extremize the functional Φ among all functions in L2 S1 .

We refer to [Car+17], [OTZ19], and [FO17] for further background on the sharp Fourier restriction and extension problems. In particular, it is known that real-valued maximizers of the functional Φ do not change sign and are antipodally symmetric. Hence, it suﬃces to show the variant of Theorem 1 for non-negative and antipodally symmetric functions as in [OTZ19].

Since f in Theorem 1 is assumed to be real-valued, we have fˆn = fˆ−n, so that the Fourier modes vanish for |n| > 120. Theorem 1 thus concerns ﬁnite set of Fourier modes and turns the extremizing problem into a ﬁnite 1

Minimaleigenvalue

10−1

10−2

10−3

10−4

0 100 200 300

Block D

Figure 1. Minimal eigenvalue for each block 0 ≤ D ≤ 360, N = 120.

dimensional problem. This makes it accessible to numerical computation. As in [OTZ19], the theorem is reduced to demonstrating positive semideﬁniteness of each of the 3N/2 + 1 matrices

- (1) (Qm,n)m,n∈X


D

with 0 ≤ D ≤ 3N an even number, XD = (m1,m2,m3) ∈ (2Z)3 \ {(0,0,0)}

m1+m2+m3=D, |m1|,|m2|,|m3|≤N, m1≤m2≤m3

, and, writing S3 for the group of permutations of three elements and

nσ = nσ(1),nσ(2),nσ(3) , σ ∈ S3, we set

1 6 σ∈S

Qm,n :=

### (Rm,nσ − Lm,nσ),

3

Lm,n := 2Im,−n +

Im,−n+(1,−1,0)

### ,

σ

σ∈S3

Rm,n := 2Im−n,(0,0,0) +

Im−n,(1,−1,0)

,

σ

σ∈S3

6

∞

Im,n := Ik :=

Jkj(r)r dr,

0

j=1

where k ∈ Z6 in the ﬁnal deﬁnition is the concatenation of m and n, and the Bessel function Jk is deﬁned by

ωke−ix·ω dσω = 2π(−i)kJk(|x|)(x/|x|)k.

S1

Note that in the formulas for Lm,n and Rm,n given in [OTZ19], n should be replaced by −n on the right-hand side. This error is corrected here.

Minimaleigenvalue

10−3

Eigenvalues

#### 0.15N−1.74

10−4

20 40 60 80 100120

N

### Figure 2. Minimal eigenvalues for the D = 0 matrix in (1) with 20 ≤ N ≤ 120.

### The main computational task in the proof of the theorem is the numerical approximation of the various integrals Ik. The number of such integrals increases as the ﬁfth power of N; approximately 2.1 × 105 distinct integrals (up to sign and permutation of k) must be calculated for the N = 30 case, increasing to approximately 1.6 × 108 for the N = 120 case. In Section 2, we describe carefully the numerical scheme used to approximate each Ik and estimate the associated error. This scheme is an improved version of the scheme given in [OTZ19], requiring fewer arithmetic operations per integral. We also discuss the adjustment of the parameters in the scheme for arbitrary N.

### Due to the high level of precision required, the various calculations used in the proof were performed using arbitrary-precision arithmetic as implemented in the Arb numerical library [Joh17]; when used carefully, such arithmetic provides rigorous error bounds for the output of calculations. The calculation code was written in C++, employing hybrid parallelization through the use of both OpenMP and MPI. Computations were performed in parallel using 94 nodes of a modern compute cluster, requiring approximately 16 hours of wall time. Weights and points used for Gauss-Legendre quadrature were calculated using Mathematica [W19] to high precision and imported into the main calculation code by hand. The calculations can be reproduced using the code given in the supporting information; a copy of the output of this code, showing the approximated eigenvalues of the matrices (1), is also given. Some results (plots, etc.) outside the scope of the main proof were calculated by post-processing the calculated integrals I˜k using standard numerical software, as the precision requirements are in context less stringent.

### In Section 3, we describe the results of these computations, give an assessment of the eigenvalues, and discuss various plots of matrix entries and eigenfunctions. The quality of the experimentally-obtained information about the matrices in (1) and their eigenvalues and eigenfunctions has substantially

improved compared to the computations in [OTZ19]. Phenomena are seen with much better resolution and allow further investigation. In particular, we obtain positivity of all eigenvalues in question, as shown to suﬃcient accuracy in Figure 1, which implies Theorem 1 by the reductions described in [OTZ19].1

Figure 1 shows that D = 0 has the smallest eigenvalue among the matrices in (1) for N = 120. It is cheap to conjecture that the analogous statement holds for arbitrarily large N. In addition, Figure 2 suggests the conjecture that the smallest eigenvalue of the matrix D = 0 has a power decay, possibly of the order N−7/4, and is in particular positive. These conjectures would imply the analogue to Theorem 1 for arbitrarily large N, and with it the general conjecture about constant functions maximizing the Tomas-Stein functional in L2 S1 .

2. Numerical estimation of Ik and error bounds

As in [OTZ19], we approximate integrals Ik by quantities I˜k deﬁned by approximating schemes. We split

Ik = Ik0,S + IkS,T + IkT,∞

6

6

S

T

- (2)

and correspondingly combine

- (3) I˜k = I˜k0,S + I˜kS,T + I˜kT,∞,


=

Jkj(r)r dr +

Jkj(r)r dr +

0

S

j=1

j=1

6

∞

Jkj(r)r dr,

T

j=1

where the ﬁrst two terms are quadrature rules with diﬀerent parameters approximating the corresponding compact integrals in (2), and the third term is an exact integral over an approximation to the integrand using asymptotic expansion. As opposed to [OTZ19], we use Gauss-Legendre quadrature instead of Newton-Cotes quadrature on the ﬁrst two pieces, and we use more terms of the asymptotic expansion on the third integral. The cutoﬀs S and T should be chosen well for numerical speed and accuracy. Our discussion of the error bounds requires S ≥ 0.95N3/2 ln(N) + 1 and T > 10N2. For N = 120, in accordance with these conditions, we choose S = 6,000 and T = 150,000.

- 2.1. Gauss-Legendre quadrature on the intervals [0,S] and [S,T]. We cut each of the intervals [0,S] and [S,T] into small intervals of constant length and use Gauss-Legendre quadrature with n = 12 points on each of these small intervals. We will estimate the error of the quadrature using Lemma 3 below. We ﬁrst quickly review the theory behind this lemma.


1During the preparation of the ﬁnal version of this paper, the authors became aware of a minor but non-negligible error in previous preprint versions, namely that an incorrect value of T was used in the numerical calculation of the tail approximation I˜kT,∞ in (3). The error has been corrected, and all values, plots, etc. have been recalculated and updated accordingly.

In L2([−1,1]), the even or odd real monic polynomial

- (4)

n! (2n)!

∂xn x2 − 1 n =:

n

i=1

(x − xi) =: pn(x)

is orthogonal to all polynomials of lower degree (this is the Rodrigues formula for the Legendre polynomials with a diﬀerent constant factor). This is seen by n-fold partial integration, with boundary terms vanishing due to the structure of pn. The zeroes x1,...,xn are distinct and contained in (−1,1), or else there was a lower degree polynomial with the same sign as pn on [−1,1], contradicting orthogonality. The linear combination xpn − pn+1 has degree at most n and is orthogonal to all polynomials pk with k < n − 1. By parity consideration, it is a multiple of pn−1 with factor determined by examination of the highest order coeﬃcient:

xpn − pn+1 = −n2(n − 1) (2n)(2n − 1) −

−(n + 1)2n (2n + 2)(2n + 1)

pn−1

=

n2 (2n + 1)(2n − 1)

pn−1.

Pairing with pn−1, using orthogonality relations, identifying the n-th factor of the Wallis product, and solving the recursion yields

1

−1

p2n(x)dx =

1 4

(2n)2 (2n − 1)(2n + 1)

1

−1

p2n−1(x)dx ≤ 2−2nπ.

- Lemma 2 (Gauss-Legendre quadrature). There are weights wi such that, for every function f that is 2n times continuously diﬀerentiable on [−1,1], we have


- (5)


n

f(2n)(ξ) (2n)!

1

wif(xi) ≤ π2−2n sup

f(y)dy −

−1

ξ∈[−1,1]

i=1

Proof. By regularity of the Vandermonde determinant, there are weights wi such that the left-hand-side of (5) vanishes if f is a polynomial of degree at most n − 1. The left-hand-side also vanishes evidently for all polynomials of the form xkpn with k ≤ n − 1, and thus for all polynomials of degree at most 2n − 1. For arbitrary f as in the lemma, let h be the polynomial of degree < 2n such that f − h vanishes of second order at all points xi. Then the function k = (f − h)p−n2 is continuous. We estimate the left-hand-side of (5) as:

1

1

k(y)pn(y)2 dy

(f − h)(y)dy =

−1

−1

1

pn(y)2 dy ≤ π2−2n|k(x)|

≤ |k(x)|

−1

for some x ∈ [−1,1]. By Rolle’s theorem, there is a ξ ∈ [−1,1] with 0 = ∂ξ2n(f − h − k(x)p2n)(ξ) = f(2n)(ξ) − k(x)(2n)!

- Lemma 3. Assume f is analytic on the union of balls of radius 1 about each of the points of the interval [a,b] and bounded by F on this union. Then


n

b

f(x)dx −

a

i=1

b − a 2

wi

f

a + b 2

+

xi ≤ π2−2n |b − a| 2

b − a 2

2n+1

F.

Proof. This follows by translation and dilation of f from the case [a,b] = [−1,1] with balls of radius 1 replaced by balls of radius 2/|b − a|. The estimate in case [−1,1] follows from Lemma 2 when estimating f

(2n)(ξ)

2n! with Cauchy’s integral formula as an average of the analytic function f over the circle of radius 2/|b − a| about the point ξ.

On the interval [0,S], we use the bound

|Jn(z)| ≤ e| (z)| on the strip (z) ≤ 1, obtained as reviewed in Section 2 of [OT17] from the integral representation

2π

- 1

- 2π


eizsin(θ)einθ dθ. Hence, the function

Jn(z) =

0

- (6) f(z) = z

6

i=1

Jni(z)

is bounded in absolute value by |z|e6 on this strip. Cutting the interval [0,S] into K intervals of length 2d = S/K and using Gauss-Legendre quadrature as in Lemma 3 on each interval gives

Ik0,S − I˜k0,S =

S

0

f(z)dz −

K−1

j=0

d

n

i=1

wif(d(2j + 1) + dxi)

≤ π2−2nd2n+1e6

K−1

j=0

(2d(j + 1) + 1)

≤ π2−2n−1d2ne6

S

0

(x + 2d + 1)dx ≤ π2−2n−1d2ne6(S + 2d + 1)2 ≤ 0.000038 × (S + 2d + 1)2d24 ≤ 0.1 × 10−10.

- (7)


Here we have used n = 12 in the penultimate and S = 6,000 and d = 0.25 in the ultimate inequality. Note that this estimate does not depend on particular assumptions on S, and our parameters lead to an algorithm with 144,000 evaluations of the integrand.

On the interval [S,T], we recall from [OT17, Section 2] the following representation for Jn, which arises through the change of variables t = cos(θ) from the Poisson integral:

(z/2)n Γ(n + 1/2)Γ(1/2)

1

cos(zt) 1 − t2 n−1/2 dt.

Jn(z) =

−1

We split Jn = 21(Jn+ + Jn−), where Jn+(z) = Jn−(z) and Jn+(z) =

(z/2)n Γ(n + 1/2)Γ(1/2)

1

eizt 1 − t2 n−1/2 dt.

−1

Indeed, Jn = Jn+ due to symmetry of the weight. A change of the contour integral leads to

- (8) Jn+(z) =

(2πz)−1/2 Γ(ν + 1)

∞

0

e−uuν e−iω 1 −

iu 2z

ν

+ eiω 1 +

iu 2z

ν

du with the abbreviations

ν := n −

- 1

- 2


, ω := z −

π 4 −

nπ 2

.

We split further Jn+ = 12(Jn++ + Jn+−) with Jn+−(z) = Jn++(z) and

- (9) Jn++(z) =


2 πz

1/2 eiω Γ(ν + 1)

∞

iu 2z

e−uuν 1 +

0

ν

du.

- Lemma 4. Assume N ≥ 20 and 0 ≤ n ≤ N. Assume | (z)| > 0.95N 32 ln(N) and | (z)| ≤ 1. Then


Jn++(z) ≤ 3.36|z|−1/2. The analogous estimate holds for Jn+−, Jn+, Jn−, and Jn. Proof. We ﬁrst estimate the part of the integral in (9) from 0 to 2N ln(N). We estimate in this range

- 1

- 2 ≤ 1 +


iu 2z

u (z) 2|z|2

u (z) 2|z|2

= 1 +

+ i

2

1 0.9N ≤ 1 +

1 0.9N2 ln(N)

≤ 1 +

+

1 N

,

where the lower bound by 12 will only be used if ν is negative, that is ν = −1/2. We obtain

ν

∞

2N ln(N)

iu 2z

e−uuν 1 +

e−uuν du

du ≤ e

0

0

= eΓ(ν + 1). Turning to the part of the integral in (9) from 2N ln(N) to ∞, we estimate

ν

iu 2z

u N

ν+2

1 ±

≤

### . Hence we have

ν

∞

∞

iu 2z

u N

ν+2

e−uuν 1 +

du ≤ e−N ln(N)

e−u/2uν

du

2N ln(N)

0

1 100

= N−N−ν−222ν+3Γ(2ν + 3) ≤

Γ(ν + 1). With eiω ≤ cosh(| z|) ≤ cosh(1) it follows that

1/2

2 π|z|

1 100

+ e ≤ 3.36|z|−1/2.

Jn+(z) ≤

cosh(1)

The analogous estimates for the other variants of Bessel’s function are clear.

With Lemma 4, we estimate the function (6) on the strip (z) ≤ 1 and

(z) ≥ 0.95N 32 ln(N) in absolute value by (3.36)6|z|−2. Cutting the interval [S,T] into K intervals of length 2d = (T − S)/K and using Gauss-Legendre quadrature as in Lemma 3 on each interval, we obtain

- (10)

Here we used n = 12 in the penultimate and S = 6,000 and d = 0.8 in the ultimate inequality. The use of Lemma 4 here requires S ≥ 0.95N3/2 ln(N)+1, which is satisﬁed with N = 120 and S = 6,000. Assuming T = 150,000, this amounts to 1,080,000 evaluations of the integrand.

- 2.2. Asymptotic approximation on the interval [T,∞). We present a precise error bound for the classical asymptotic expansion of order four of Bessel functions, a slight reﬁnement of the corresponding discussion in Section 2 of [OT17].


- Lemma 5. Assume N ≥ 20 and n ≤ N. Assume z is real and z > 2N 32 ln(N). Then


πz 2

- 1

- 2Jn++(z)e−iω = 1 + i


Γ(ν + 2) 2Γ(ν)z −

Γ(ν + 3) 8Γ(ν − 1)z2 − i

Γ(ν + 4) 48Γ(ν − 2)z3

+ R

- (11)

with

|R| ≤ 0.0043

N8 z4

. Proof. Recalling (9), we see

- (12)


IkS,T − I˜kS,T =

K−1

T

f(z)dz −

S

j=0

n

d

wif(S + d(2j + 1) + dxi)

i=1

K−1

π 22n

(S + 2dj − 1)−2

d2n+1(3.36)6

≤

j=0

T

π 22n+1

(x − 1 − 2d)−2 dx ≤ π2−2n−1d2n(3.36)6(S − 1 − 2d)−1

d2n(3.36)6

≤

S

- ≤ 0.000135 × (S − 1 − 2d)−1d24
- ≤ 1.1 × 10−10.


πz 2

- 1

- 2Jn++(z)e−iω =


1 Γ(ν + 1)

∞

iu 2z

e−uuν 1 +

0

ν

du.

We expand (1 + ix)ν for real 0 ≤ x with Taylor’s theorem into (1 + ix)ν = 1 + iνx −

- 1

- 2


1 6

iν(ν − 1)(ν − 2)x3 + r where

ν(ν − 1)x2 −

x

1 6

ν(ν − 1)(ν − 2)(ν − 3)(x − t)3(1 + it)ν−4 dt

|r| =

0

1 24|ν(ν − 1)(ν − 2)(ν − 3)|x4 1 + x2 Thus the right hand side of (12) becomes (11) with

- 1

- 2 max{ν−4,0}.


≤

∞

e−uuν|r(u)|du

|R| ≤

0

and r(u) similar to above with x replaced by u/2z. We cut the integral at u = 4N ln(N). For u ≤ 4N ln(N) we have

N 2

|ν(ν − 1)(ν − 2)(ν − 3)|u4 384z4

1 N

|r(u)| ≤

1 +

and thus

4N ln(N)

e1/2N8 384z4

1 Γ(ν + 1)

Γ(ν + 5) 384|Γ(ν − 3)|z4 ≤

euuνr(u)du ≤ e1/2

. For u ≥ 4N ln(N) we have

0

|ν(ν − 1)(ν − 2)(ν − 3)|u4 6(2z)4

u N

N/2

|r(u)| ≤

, and therefore

∞

1 Γ(ν + 1)

e−uuνr(u)du

4N ln(N)

∞

u N

1 384z4|Γ(ν − 3)|

N/2

e−u/2e−2N ln(N)uν+4

≤

du

0

2ν+5+N/2 N2N+N/2

1 96z4|Γ(ν − 3)|

Γ(ν + 5 + N/2) ≤ z−4.

≤

Adding the estimates for the two pieces of the integral gives the bound claimed in the lemma.

With the above lemma, we obtain for Jn+ in the range of n and z discussed in the lemma:

- 1

- 2Jn+(z) = a + bz−1 + cz−2 + dz−3 + R


πz 2 with

- (13)


- a = cos(ω),
- b = −sin(ω)

- 1

- 2


n2 −

1 4

,

- c = −cos(ω)


1 8

1 4

n2 −

9 4

n2 −

,

1 48

- d = sin(ω)


1 4

n2 −

9 4

n2 −

25 4

n2 −

,

and R satisﬁes the same bounds as in the lemma. The analogous identity holds for Jn since it coincides with Jn+ on the real line. Now we consider six indices nj and corresponding ωj := z − π/4 − njπ/2 and obtain for real z

6

π 2

3

Jnj(z)z = Az−2 + Bz−3 + Cz−4 + Q

j=1

with

- A = cos(ω1)cos(ω2)cos(ω3)cos(ω4)cos(ω5)cos(ω6),
- B = −

6

j =1

n2j − 1/4 2

sin ωj

1≤j≤6,j =j

cos(ωj),

- C =


n2j − 1/4 n2j − 1/4 4

6

6

sin ωj sin ωj

j =1

j =j +1

6 j=1 n2j − 1/4 n2j − 9/4

−

8

6

cos(ωj).

j=1

1≤j≤6,j =j ,j =j

cos(ωj)

The remainder term Q we estimate from above. For this we collect terms of order z−5, z−6, z−7, z−8 and higher order separately. We begin with a remark on integrals of type

6

∞

φj(ωj)z−5

T

j=1

where an odd number of functions φj are the cosine function and an odd number of φj are the sine function. If a function is odd in the variable z about the point π4 then we call it of parity −1, and if it is even we call it of parity 1. The function

π 4 −

nπ 2

sin(ωj) = sin z −

has parity −(−1)n about the point π4, while the function cos(ωj) = cos z −

π 4 −

nπ 2

has parity (−1)n. A product of six such functions with 6j=1 nj even and an involving an odd number of sine function is therefore odd about the point π/4. This means it integrates to zero about each period of the periodic function. Hence by partial integration

 

 5z−6 dz + T−5

6

6

∞

∞

∂z−1

φj(ωj)z−5 dz ≤

φj(ωj)

T

T

j=1

j=1

≤ (π + 1)T−5

where we used that the function 6j=1 φj(ωj) is bounded by 1 and since it integrates to 0 of periods of length 2π its primitive ∂z−1 6j=1 φj(ωj) is bounded by π.

We use this estimate in each of the terms of the ﬁfth order, all of which

have an odd number of sine functions. We estimate all factors n2j − x by N2. Counting the terms and referring to the abbreviations in (13), we obtain

- 6 terms with a factor d, 30 factors with a product bc and 20 terms with a factor b3. Thus this term is estimated by


- (14)

6 48

+

30 16

+

20 8

(1 + π)

N6 T5 ≤ 19

N6 T5

.

To estimate sixth order terms we estimate all sine and cosine functions by 1. Integrating z−6 then simply gives T−5/5. We obtain 6 terms with a factor R, 30 terms with a factor bd, 15 terms with a factor c2, 60 terms with a factor cb2, 15 terms with a factor b4. This gives the estimate

- (15) 6 × 0.0043 +

30 96

+

15 64

+

60 32

+

- 15

- 16


N8 5T5 ≤ 0.68

N8 T5

.

The seventh order terms we estimate similarly. We obtain 30 terms with a factor Rb, 30 terms with a factor dc, 60 terms with a factor db2, 60 terms with a factor c2b, 60 terms with a factor cb3 and 6 terms with a factor b5. This gives the estimate

- (16)

30 2 × 0.0043 +

30 384

+

60 192

+

60 128

+

60 64

+

6 32

N10 6T6 ≤ 0.35

N10 T6

.

Counting the eighth order terms we ﬁnd 30 terms with a factor Rc, 60 terms with a factor Rb2, 15 terms with a factor d2, 120 terms with a factor dcb, 60 terms with a factor db3, 15 terms with a factor c3, 45 terms with a factor c2b2, 30 terms with a factor cb4, and one term with a factor b6. This gives the estimate

0.0043

30 8

+

60 4

+

15 2304

+

120 768

+

60 384

+

15 512

+

45 256

+

30 128

+

1 32

N12 7T7 ≤ 0.13

N12 T7

.

- (17)

The terms of order 9 or higher we estimate more crudely. There are at most 56 terms, the product of pre factors being at most 0.0043 if a factor R is involved and being at most 1281 if no such factor is involved. Thus we get, assuming N2 ≤ T, the upper bound

- (18) ≤


56 128

N14 8T8 ≤ 16

N14 T8

.

D λmin

0 0.0000369980 2 0.0000371564 4 0.0000374854 6 0.0000379002 8 0.0000384081

10 0.0000389622 Table 1. Smallest eigenvalues for matrices (Qm,n)m,n∈X

, for D = 0,2,...,10, rounded to 11 signiﬁcant ﬁgures.

D

Assuming N = 120 ≥ 20 and T ≥ 10N2 we may add (14), (15), (16), (17),

- and (18) to

IkT,∞ − I˜kT,∞ ≤ 19 × 10−420−2 + 0.68 × 10−4 + 0.35 × 10−5

+ 0.13 × 10−6 + 16 × 10−7 T−1 ≤ 0.75 × 10−4T−1 ≤ 0.5 × 10−9.

(19)

Here we used T = 150,000 > 10N2 in the last inequality. Summing (7), (10),

- and (19), we ﬁnally obtain


- (20) Ik − I˜k ≤ 0.73 × 10−9.


3. Numerical Results Using the approximations I˜k, one computes approximations (Q˜m,n)m,n∈X

D

to the matrices (Qm,n)m,n∈X

analogously to the formulae in the introduction. Using evaluations of Bessel functions of suﬃcient accuracy and arbitraryprecision arithmetic, the I˜k and Q˜m,n as well as the eigenvalues of the matrices (Q˜m,n)m,n∈X

D

were computed up to an error of at most 10−20. The computed smallest eigenvalue for each D is plotted in Figure 1 and shown in Table 1 for small D. In particular, the matrix (Q˜m,n)m,n∈X

D

is positive deﬁnite with smallest eigenvalue at least 0.000036.

D

We have for each m,n in question from (20) Qm,n − Q˜m,n ≤ 16 × 0.73 × 10−9 ≤ 1.2 × 10−8.

This entry-wise bound is multiplied by the size 1860 of the set XD for N = 120 to obtain a bound for the operator norm

− Q ˜m,n

≤ 1860 × 1.2 × 10−8 ≤ 0.000023.

(Qm,n)m,n∈X

D

m,n∈XD op

As this is less than the smallest eigenvalue of the matrix Q ˜m,n

,

m,n∈XD

we may deduce that the matrix (Qm,n)m,n∈X

is positive deﬁnite as well. Following the reductions of [OTZ19], this proves Theorem 1.

D

While the error bounds (20) are good enough to prove the main theorem, they are not good enough to guarantee that our plots and tables of eigenvalues of (Q˜m,n)m,n∈X

within the margins suggested by the visible information. However, the arguments obtaining (20) as well as the use of the operator norm above are very crude estimates. With very high likelihood, the true diﬀerences between the corresponding eigenvalues of the two matrices are much smaller than the operator norm above. In this sense, we consider our plots and tables of eigenvalues of (Q˜m,n)m,n∈X

are representative for those of (Qm,n)m,n∈X

D

D

as very much representative of those of (Qm,n)m,n∈X

D

. This is in accordance with the rather regular behaviour of the plots and of Table 1, a level of regularity that one might expect from the eigenvalues of (Qm,n)m,n∈X

D

.

D

A number of numerical ﬁndings would be interesting to understand analytically and maybe prove for large N asymptotically. Any progress in this understanding would presumably require an asymptotic understanding of the entries of the matrices in (1). Figure 3 shows sample columns of these matrices. For nicer visualization, we have undone the dimension reduction by symmetry in [OTZ19] and shown the related matrices

- (21) Q˜(D) := (Qm,n)m,n∈Z

D

, in the space

ZD := (m1,m2,m3) ∈ (2Z)3 \ {(0,0,0)} | mm11+|,|mm22+|,|mm33=|≤D,N . The space ZD is naturally depicted as a hexagon. It has a sixfold symmetry under permutations of the three elements, which is the symmetry group of a regular hexagon. This symmetry extends to symmetries of the columns shown and is visible in the plots of Figure 3. The space XD in our previous calculations is only one fundamental domain under this symmetry.

The largest entry in each column of the matrices in (1) is the diagonal element. The diagonal elements appear as brights dots on the ellipses in Figure 3. Due to the sixfold symmetry of the visualization, they appear three or six times in each image depending on their orbit under the symmetry group, namely the points where m is a permutation of n. While it may be tempting to try to prove positive deﬁniteness of the matrices in (1) by diagonal dominance, for N = 120 and D = 0, the ratios

- (22) rm := |Qm,m|−1 n∈X0\{m}


|Qm,n|,

can be large as well as small, e.g.

r(−2,0,2) ≈ 3.1, r(−90,40,50) ≈ 1.9, r(−4,2,2) ≈ 0.7. Indeed, this failure of this attempt is natural due to the existence of some very small eigenvalues.

A secondary collection of large entries in each column shown in Figure 3 can be seen as yellow ellipses in the diagrams. These visual ellipses correspond to circles in a visualization of the domain as regular hexagon. The circles

#### m = (10,10,−20)

120

n2

0

−120

−120 0 120

m = (10,50,−60)

120

0

−120

−120 0 120

#### m = (40,50,−90)

120

n2

0

−120

−120 0 120

n1

m = (10,100,−110)

120

0

−120

−120 0 120

n1

−16 −14 −12 −10 −8 −6 −4 ln of abs. val. of entry

Figure 3. Columns of (21) with D = 0 and N = 120 for sample ﬁxed values of m, in coordinates n1,n2. Coloring is logarithmic in the absolute values of entries; logarithmic values below −16 are clipped.

were already observed in [OTZ19]. The current data even more strongly suggests that these secondary peaks are located on the surface

- (23) n21 + n22 + n23 = m21 + m22 + m23.


Indeed, in Figure 4, the ellipse/circle given by (23), plotted as a white line, is overlayed onto one of the plots, showing that it matches the yellow peaks very well. The size of the sum of oﬀ-diagonal elements in (22) is essentially entirely due to the elements near the circle.

At the moment, we do not even have a qualititive understanding of the occurrence of these circles, let alone a quantitative one, which would

n2

120

0

−120−120 0 120

n1

−4

−6

ofabs.val.ofentryln

−8

−10

−12

−14

−16

### Figure 4. Column m = (20,70,−90) of (21) with D = 0 and N = 120, in coordinates n1,n2. Coloring is logarithmic in the absolute values of entries; logarithmic values below −16 are clipped. The white line indicates the ellipse given by (23).

### probably be required if one wanted to extract positive deﬁniteness from the structure of these matrices. Figure 5 plots the values of the entries of the column (40,60,−100) as a function of the radial variable n21 + n22 + n23 in the vicinity of the radius of the yellow circle, which is about 123.3. The plot strongly suggests that the pattern of the circle is asymptotically well approximated by a smooth radial function of low complexity. The value at the diagonal element, which is at radius about 123.3, is not plotted in Figure 5, because it is too large at about 0.044. Likewise, two further entries near the diagonal elements are not shown, they have value −0.0024. They are part of the small ring of six large elements around the diagonal elements, which also include the four entries with values near −0.0015 shown in Figure 5. Also, small matrix entries are cut oﬀ in the plot 5.

### Due to the monotonicity shown in Figure 1, it is of particular interest to study the matrix in (1) for D = 0. Figure 6 shows all eigenvalues of the matrix D = 0 for N = 120 sorted and enumerated by size. For comparison, we also show the analogous plot for the matrix D = 200, a diagram that is somewhat similar. Note the two jumps of the diagram for D = 0 at about the 60-th smallest and 60-th largest eigenvalues. An analytical proof of positivity for all N in the asymptotic regime would require a better understanding of the ensemble of small eigenvalues below the ﬁrst jump.

Columnentry

·10−3

0.5

0

−0.5

−1

−1.5

120 122 124 126 128

Radial variable

### Figure 5. Partial plot of the values of the entries of column m = (40,60,−100) of (21) with D = 0 and N = 120 in dependence of the radial variable.

Eigenvalue

0.10

0.05

0.00

0 500 1,000 1,500 2,000

Eigenvalue

0.05

0.00

0 100 200 300 400 500 600

Sorted index

### Figure 6. Sorted eigenvalues of 1 with D = 0 (top, 1860 eigenvalues) and D = 200 (bottom, 574 eigenvalues), both with N = 120.

n2

120

0

−120−120 0 120

n1

- 0.8
- 1


entryvalue

0.6

0.4

0.2

0

Figure 7. Eigenvector of (1) with D = 0 and N = 120 corresponding to the smallest eigenvalue in coordinates n1,n2. The dotted lines are points where the orbit of the symmetry group has only three elements. They are an artifact of dimension reduction: the values of the eigenvector at these points are half as large as those of the corresponding eigenvector of (1).

The eigenfunctions corresponding to the smallest eigenvalues experimentally appear to be essentially radial functions in the visualization corresponding to Figure 3, cf. Figure 7. There are three notable observations to be made here:

- (1) The bulk of the eigenvector depends essentially only on n21 + n22 + n23.

- (2) The value at the points where two of the nis coincide is smaller than suggested by this radial dependence by a factor of two (although this is not evident from this particular visualization).
- (3) Outside of the largest circle that ﬁts into the region Z0, the eigenvector is small.


The second point above is related to the fact that in the matrices (21), the rows and the columns of (21) appear as many times as there are distinct permutations of m and n respectively, i.e. 3 and 6 times. It therefore appears more natural to analyze the eigenvalues of (21), or, equivalently, the matrices given by (pmQm,npn)m,n∈X

, where pm is the number of distinct permutations of m.

0

In view of the third point above, it also appears natural to truncate the ma-

trices not according to max(|n1|,|n2|,|n3|), but according to n21 + n22 + n23. In what follows, let us therefore consider the matrices

- (24) Q◦ := (pmQm,npn)m,n∈X◦,


sn

- λ1

- λ2

- λ3

- λ4

- λ5


- 0.5
- 1


0

0 20 40 60 80 100 120 140 160

n 2

Figure 8. Eigenfunctions associated to ﬁve smallest eigenvalues λi,1 ≤ i ≤ 5 of (24) with D = 0 and N = 120.

where

√ m1+m2+m3=0,

√

X◦ = (m1,m2,m3) ∈ (2Z)3 \ {(0,0,0)}

.

m21+m22+m23≤

3/2N, m1≤m2≤m3

is the largest disc contained in X0. The eigenvectors of the matrices (24) corresponding to small eigenvalues seem to be smooth functions of the

radial variable n21 + n22 + n23, see Figure 8. In that ﬁgure, the ﬁve smallest eigenvalues are represented by diﬀerent colors. For each eigenvalue, there

is a point for every n ∈ X◦. Surprisingly, the corresponding eigenvector entries sn fall on a one-dimensional curve, although X◦ is taken from a twodimensional lattice. After a suitable rescaling, the proﬁle of the curve seems to be independent of N, as shown in Figure 9 for the smallest eigenvalue.

It is natural to link the behaviour of the eigenfunctions to the smallest eigenvectors to a natural enemy of the sharp Fourier extension conjecture. Namely, functions on the circle which approximate two Dirac deltas at antipodally symmetric points are close competitors to extremize the TomasStein functional; they “lose” to the constant function by only a small amount. Such Dirac deltas, on the Fourier transform side depicted in the above hexagons, correspond to wide bumps such as the lowest eigenfunction. One can well imagine that all the radial eigenfunctions to small eigenvalues aspire to resolve structure near the Dirac deltas.

Acknowledgements

The main calculations described in this paper were performed using the supercomputing facilities of Fraunhofer SCAI. The authors acknowledge support by the Deutsche Forschungsgemeinschaft through the Hausdorﬀ Center for Mathematics (DFG Projektnummer 390685813) and the Collaborative Research Center 1060 (DFG Projektnummer 211504053). The authors also

REFERENCES 19

sn

N = 40 N = 60 N = 80

- 0.8
- 1


N = 100 N = 120

0.6

0.4

0.2

0

0 0.2 0.4 0.6 0.8 1

n21+n22+n23

3 2N

Figure 9. Eigenfunctions associated to the smallest eigenvalues of (24) with D = 0 and N ∈ {40,60,80,100,120}.

gratefully acknowledge the comments and suggestions of the anonymous reviewers, and in particular their detection of several small errors.

References

[Car+17] Emanuel Carneiro et al. A sharp trilinear inequality related to Fourier restriction on the circle. In: Rev. Mat. Iberoam. 33.4 (2017), pp. 1463–1486. issn: 0213-2230. doi: 10.4171/RMI/978. arXiv: 1509.06674.

[FO17] Damiano Foschi and Diogo Oliveira e Silva. Some recent progress on sharp Fourier restriction theory. In: Anal. Math. 43.2 (2017), pp. 241–265. issn: 0133-3852. doi: 10.1007/s10476-017-0306-2. arXiv: 1701.06895.

[Joh17] Fredrik Johansson. Arb: eﬃcient arbitrary-precision midpointradius interval arithmetic. In: IEEE Transactions on Computers 66.8 (2017), pp. 1281–1292.

[OT17] Diogo Oliveira e Silva and Christoph Thiele. Estimates for certain integrals of products of six Bessel functions. In: Rev. Mat. Iberoam. 33.4 (2017), pp. 1423–1462. issn: 0213-2230. doi: 10.4171/RMI/ 977. arXiv: 1509.06309.

[OTZ19] Diogo Oliveira e Silva, Christoph Thiele, and Pavel Zorin-Kranich. Band-limited maximizers for a Fourier extension inequality on the circle. In: Experimental Mathematics (2019), pp. 1–7. arXiv: 1806.06605.

[Tom75] Peter A. Tomas. A restriction theorem for the Fourier transform. In: Bull. Amer. Math. Soc 81.2 (1975), pp. 477–478. [W19] Wolfram Research Inc. Mathematica, Version 12.0. Champaign, IL, 2019. url: https://www.wolfram.com/mathematica.

20 REFERENCES

(Barker) Fraunhofer SCAI, Schloss Birlinghoven, 53754 Sankt Augustin,

Germany Email address: james.barker@scai.fraunhofer.de (Barker) Institute for Numerical Simulation, Endenicher Allee 19B, 53115

Bonn, Germany

(Thiele, Zorin-Kranich) Hausdorff Center for Mathematics, 53115 Bonn, Germany

Email address: thiele@math.uni-bonn.de Email address: pzorin@math.uni-bonn.de

