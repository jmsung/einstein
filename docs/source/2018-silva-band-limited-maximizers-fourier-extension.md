---
type: source
kind: paper
title: Band-limited maximizers for a Fourier extension inequality on the circle
authors: Diogo Oliveira e Silva, Christoph Thiele, Pavel Zorin-Kranich
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1806.06605v2
source_local: ../raw/2018-silva-band-limited-maximizers-fourier-extension.pdf
topic: general-knowledge
cites:
---

# arXiv:1806.06605v2[math.CA]21Feb2019

## BAND-LIMITED MAXIMIZERS FOR A FOURIER EXTENSION INEQUALITY ON THE CIRCLE

DIOGO OLIVEIRA E SILVA, CHRISTOPH THIELE, AND PAVEL ZORIN-KRANICH

Abstract. Among the class of functions with Fourier modes up to degree 30, constant functions are the unique real-valued maximizers for the endpoint Tomas–Stein inequality on the circle.

1. Introduction

We are interested in the sharp constant of the endpoint Tomas–Stein adjoint restriction inequality [To] on the circle S1 = {ω ∈ R2 : |ω| = 1}. More precisely, we seek a maximizer for the functional Φ deﬁned on nonzero f ∈ L2(S1) by

Φ(f) := fσ 6L6(R2) f −L26(S1). We have written σ for the arc length measure on the circle S1, and we have used the Fourier transform

f(ω)e−ix·ω dσω, (x ∈ R2).

fσ(x) :=

S1

It is known that maximizers of Φ exist [Sh1] and are smooth [Sh2], and that the constant function 1 is a local maximizer of Φ, see [CFOT, Theorem 1.1]. Moreover, real-valued maximizers of Φ are known to be nonnegative, antipodally symmetric functions, that is

f(ω) ≥ 0, f(ω) = f(−ω),

for every ω ∈ S1. It is natural to conjecture that constant functions are global maximizers of Φ, in which case a complete characterization of complexvalued maximizers is given by [CFOT, §1, Step 6].

In this paper, we report on numerical veriﬁcation of a ﬁnite dimensional variant of this conjecture: Theorem 1. Let f ∈ L2(S1) be non-negative and antipodally symmetric. Assume that f(n) = 0 if |n| > 30. Then

Φ(f) ≤ Φ(1), with equality if and only if f is constant.

A numerical diﬃculty in this problem is that there are close competitors for maximizers, namely functions that concentrate in the vicinity of two antipodal points. Heisenberg uncertainty allows for functions with Fourier modes up to degree 30 to localize roughly in a 230π-neighborhood of these points.

This paper continues eﬀorts to implement Foschi’s program [Fo] for the 2-sphere in the case of the circle, see also [CFOT]. The approach works

1

through positive semi-deﬁniteness of a certain quadratic form on the relevant ﬁnite dimensional space. It would be nice to establish positive semideﬁniteness for the full space. For recent similar work on the paraboloid, see [Go].

2. Proof of Theorem 1 With f as in Theorem 1, we compute

fσ 6L6(R2) = (2π)2

δ 6j=1 ωj

(S1)6

3

fj(ωj)dσωj

j=1

6

fj(−ωj)dσωj

j=4

= 5π2

δ 6j=1 ωj (|ω4+ω5+ω6|2−1)

(S1)6

3

fj(ωj)dσωj

j=1

6

fj(−ωj)dσωj

j=4

6

3

δ 6j=1 ωj (|ω4 + ω5 + ω6|2 − 1)

fj(ωj)2

≤ 5π2

dσωj

(S1)6

j=1

j=1

f 6L2(S1) 1 6L2(S1) (S1)6

6

δ 6j=1 ωj (|ω4+ω5+ω6|2−1)

≤ 5π2

dσωj = Φ(1) f 6L2(S1).

j=1

Here the ﬁrst line is simply Plancherel’s identity. The second line is Foschi’s idea to improve the situation by artiﬁcially inserting a weight, which after symmetrization over the indices j reverts to a constant, see the computation following [CFOT, Lemma 1.3]. The third line is the crucial inequality. We defer its proof for the moment. The inequality in the fourth line is an application of the main result proved in [CFOT, Theorem 1.2]. Equality is attained if and only if f is constant. Identiﬁcation of the constant in the fourth line is then easy and was also observed in [CFOT].

This proves Theorem 1, safe for veriﬁcation of the crucial inequality in the third line. Note that this inequality would follow from

|ω1 + ω2 + ω3| = |ω4 + ω5 + ω6| and the inequality between the arithmetic mean and the geometric mean,

3

6

- 1

- 2


fj(−ωj) ≤

fj(ωj)

j=1

j=4

3

6

fj(ωj)2 +

fj(−ωj)2 ,

j=1

j=4

if the weight were positive. Unfortunately, the weight is not positive. One reason to believe that the inequality still holds as stated is that the negative part of the weight is small, and via antipodal symmetry the values of the function on the negative part of the weight have a strong correlation with the values on the positive part. However, the support of the measure

δ 6j=1 ωj

is not preserved under antipodal symmetry, which makes it diﬃcult to exploit this correlation. We resort to numerical veriﬁcation of the crucial inequality in the given ﬁnite dimensional space of functions.

Consider the index set

Z = {k ∈ 2Z,|k| ≤ 30},

and expand the band-limited function f into a Fourier series f(ω) =

akωk,

k∈Z

where we identify R2 with the complex plane and correspondingly deﬁne products and powers of elements in R2. Note that

- (1) a−k = ak


for every k ∈ Z. We write a constant multiple of the left-hand side of the crucial inequality as

3

6

Lk

akj

a−kj ,

k∈Z6

j=1

j=4

3

6

6

ωj−kj

ωjkj

δ 6j=1 ωj (|ω4+ω5+ω6|2−1)

Lk := (2π)−5

dσωj, and the same multiple of the right-hand side as

(S1)6

j=1

j=4

j=1

3

6

a−kj ,

Rk

akj

k∈Z6

j=1

j=4

3

6

ωjkj−kj+3

δ 6j=1 ωj (|ω4+ω5+ω6|2−1)

Rk := (2π)−5

dσωj.

(S1)6

j=1

j=1

Deﬁne for m ∈ Z3

sm := am1am2am3, and note that (sm)m∈Z3 is an element of Sym(Z3), the vector space of functions on Z3 symmetric under permutation of the three indices. At this point we do not require the symmetry (1), instead we pass to a larger space allowing for a convenient orthogonal splitting later.

The crucial inequality then follows from positive semi-deﬁniteness of the quadratic form

1 6 σ∈S

(Rm,nσ − Lm,nσ)smsn

Qm,nsmsn :=

m,n∈Z3

m,n∈Z3

3

on Sym(Z3), where we write S3 for the group of permutations of three elements and

nσ = (nσ(1),nσ(2),nσ(3)). Note that the symmetrization over S3 does not change the value of the quadratic form whenever the coeﬃcients sn are symmetric. It merely symmetrizes the coeﬃcients of the quadratic form, and allows to reduce the dimension of the matrix by identifying equivalent tuples. Letting X˜ be the space of tuples in Z3 satisfying m1 ≤ m2 ≤ m3, it therefore suﬃces to prove positive deﬁniteness of the quadratic form

Q(s,s) =

## Qm,nsmsm.

m,n∈X˜

Note that the matrix (Qm,n)m,n∈X˜ is Hermitian. Moreover, for all m ∈ Z3 we have

Rm,(0,0,0) = Lm,(0,0,0) and hence the Dirac delta vector δ(0,0,0) corresponding to constant functions on the circle is in the kernel of the matrix (Qm,n)m,n∈X˜. Therefore we replace X˜ by X = X˜ \ {(0,0,0)}.

A change of variables (ω1,ω2,ω3,ω4,ω5,ω6)  → (ω1 · ω,ω2 · ω,ω3 · ω,ω4 · ω,ω5 · ω,ω6 · ω)

for some arbitrary ω of modulus one in the expressions for Rk and Lk shows that

Qm,n = ωd(m)−d(n)Qm,n, where we have denoted

d(m) = m1 + m2 + m3. We conclude

Qm,n = 0

whenever d(m) = d(n). The matrix (Qm,n)m,n∈X therefore has the structure of a diagonal block matrix, with blocks enumerated by D := d(m).

It suﬃces to prove positive semi-deﬁniteness for each block (Qm,n)m,n∈XD separately, where XD = {m ∈ X : d(m) = D}. This will be done in the following section.

3. Numerical computations

In order to verify that the matrix (Qm,n)m,n∈XD is positive deﬁnite, we split it into a numerically computed approximation and an error term. The smallest eigenvalue of the numerical approximation will be larger than the operator norm of the error term.

|D|λmin| |D|λmin| |D|λmin| |D|λmin|
|---|---|---|---|---|---|---|---|---|---|---|
|0|0.00035| |24|0.00061| |48|0.00121| |72|0.00407|
|2|0.00037| |26|0.00064| |50|0.00133| |74|0.00501|
|4|0.00038| |28|0.00067| |52|0.00144| |76|0.00596|
|6|0.00042| |30|0.00069| |54|0.00154| |78|0.00668|
|8|0.00045| |32|0.00073| |56|0.00171| |80|0.00937|
|10|0.00049| |34|0.00077| |58|0.00188| |82|0.01258|
|12|0.00052| |36|0.00081| |60|0.00203| |84|0.01332|
|14|0.00055| |38|0.00086| |62|0.00229| |86|0.02997|
|16|0.00057| |40|0.00092| |64|0.00255| |88|0.04400|
|18|0.00057| |42|0.00097| |66|0.00278| |90|0.20081|
|20|0.00058| |44|0.00105| |68|0.00324| | | |
|22|0.00059| |46|0.00113| |70|0.00369| | | |


Table 1. Minimal eigenvalue for the approximation for the block D ∈ {0,2,4,...,90}, calculated with 5 signiﬁcant digits of precision. In the case of D = 0, the null block of the vector δ(0,0,0) has been removed.

Numerical approximation of the integrals Lk and Rk will rely on the following family of Bessel integrals for 6j=1 kj = 0:

Ik := (2π)−5

δ 6j=1 ωj

(S1)6

6

ωjkj dσωj

j=1

6

6

∞

= (2π)−1

Jkj(|x|)dx =

Jkj(r)r dr, where the Bessel function Jk is deﬁned by

R2

0

j=1

j=1

ωke−ix·ω dσω = 2π(−i)kJk(|x|)(x/|x|)k. Indeed, writing

S1

ωjωk−1,

|ω4 + ω5 + ω6|2 − 1 = 2 +

j,k∈{4,5,6},k =j

we obtain

Lm,n = 2Im,n +

Im,n+(1,−1,0)σ,

σ∈S3

Rm,n = 2Im+n,(0,0,0) +

Im+n,(1,−1,0)σ.

σ∈S3

Using the fact that J−k = (−1)kJk and the above representation we see that Qm,n = Q−m,−n, so it suﬃces to consider D ≥ 0.

To evaluate the integrals Ik, we follow the scheme in [OT]. We split the integrals into

- (2) Ik =


6

S

Jkj(r)r dr +

0

j=1

6

- R
- S


Jkj(r)r dr +

j=1

6

∞

Jkj(r)r dr,

R

j=1

with S = 3600 and R = 63000. The ﬁrst two integrals are evaluated with a Newton–Cotes quadrature rule. The step size is 0.003 for the ﬁrst integral and 0.05 for the second integral. In practice, this step involved tabulating the numerical values of 61 Bessel functions at around 3 × 106 points each, with 20 digit precision obtained via the software package Mathematica [W]. This high precision lets the rounding errors be absorbed by the error estimates below.

The approximation error for the ﬁrst integral in (2) was estimated in [OT, §8], independently of the vector k, by

Ek,1 = 1.5 × 10−9.

The approximation error for the second integral in (2) was also estimated in [OT] by

6

kj2 S

,

Ek,2 = C2

1 +

j=1

where

63 5

2 π(S − 1)

3

cosh6(1)(R + 1) with S = 3600, R = 36000 and w = 0.05.

C2 = 1.016(R − S)w8

The third integral in (2) is approximated by analytic methods. Since R = 63000 is large when compared to n2 ≤ 612, we take advantage of the following well-known asymptotic formulae which are a simpliﬁed version of [OT, Corollaries 2.6 and 2.7]. 1

Lemma 2. Let ωn := z − π4 − nπ2 and nˆ := max{1,n}. If n ≥ 0 and z > nˆ2, then

- (3) Jn±(z) −

2 πz

- 1

- 2 cos(ωn) ≤


2 π|z|

- 1

- 2 nˆ2


|z|

,

- (4) Jn±(z) −

2 πz

- 1

- 2 cos(ωn) +


4n2 − 1 8z

2 πz

- 1

- 2 sin(ωn) ≤


1 4

2 π|z|

- 1

- 2 nˆ4


|z|2

.

Here the functions Jn± are obtained by writing cos(zt) = (eizt+e−izt)/2 in the Poisson integral representation for Jn, and as such satisfy Jn = (Jn++Jn−)/2. Using (3), we may split each Bessel function into a main term plus error. Applying the distributive law yields one main integral of the form

- (5)


∞

R

2 πr

3

6

cos(ωkj) r dr,

j=1

which can be calculated exactly, plus 26 − 1 further terms involving one of the two factors

- 1

- 2


- 1

- 2


2 πr

2 πr

cos(ωkj),Jkj(r) −

cos(ωkj)

for each j. We call them cosine factor and error factor. For the main integral, observe that

cos(r − π4 − kπ2 ) = (−1) k2

·

and so (5) equals a multiple of

sin(r − π4), if k is odd, cos(r − π4), if k is even,

∞

∞

cos6(r − π4)r−2 dr, or

cos4(r − π4)sin2(r − π4)r−2 dr,

R

R

with sign determined by the parity of 3j=1( m2j + n2j ). Mathematica calculates these expressions with any prescribed accuracy. For the further

terms, consider ﬁrst those consisting of an integral of a product of ﬁve cosine factors and one error factor.

1We record a typo on the ﬁrst formula in [OT, Corollary 2.7], which should read as follows:

J0±(z) −

2 πz

- 1

- 2


1 8z

cos(ω0) −

2 πz

- 1

- 2


sin(ω0) ≤

9 128|z|2

≤

2 π|z|

- 1

- 2


cosh(| (z)|) |z| | (z)|

5 2

### .

To estimate these six terms, we use the ﬁner information given by (4). The sine term in (4) leads to integrals of the type

∞

4m21 − 1 8

2 πr

3

sin(ωm1)cos(ωm2)cos(ωm3)cos(ωn)dr

R

and similar terms with a diﬀerent cosine factor replaced by a sine factor and corresponding prefactor. The product of the six trigonometric functions is odd about the point π4. Thus the product integrates to 0 over each period. On the period [R + 2πk,R + 2π(k + 1)], we may thus replace the weight r−3 by the diﬀerence between itself and its mean over that interval, which in turn is bounded by 6πr−4. Thus the sum of terms arising from the sine term in (4) is bounded by

6

kˆj2

Ek,3 = 3π

j=1

∞

R

2 π

3

r−4 dr,

where kˆj := max{1,kj}. The sum of the six terms arising from the righthand side of (4) can be estimated by

Ek,4 =

6

1 4

kˆj4

j=0

∞

R

2 π

3

r−4 dr.

Next come ﬁfteen terms of the original 26 − 1 terms which have four cosine factors and two error factors. It suﬃces to estimate these with (3), since they beneﬁt from an extra integration of a negative power of r. Their sum can be estimated by

∞

2 π

3

kˆi2kˆj2

r−4 dr,

Ek,5 =

R

i =j

where the sum is over 62 = 15 choices of distinct indices i,j ∈ {1,2,3,4,5,6}.

The remaining 26 − 1 − 6 − 15 = 42 terms beneﬁt from an integration of at least the negative ﬁfth power of r, and are estimated even more crudely by

∞

∞

2 π

2 π

3

3

kˆi2kˆj2kˆ2

kˆi2kˆj2kˆ2k ˆm2

r−5 dr +

r−6 dr

Ek,6 =

R

R

i,j, 

i,j, ,m

∞

∞

2 π

2 π

3

3

r−7 dr + kˆ12kˆ22kˆ32kˆ42kˆ52kˆ62

kˆi2kˆj2kˆ2k ˆm2 kˆn2

r−8 dr,

+

R

R

i,j, ,m,n

where the sums are over tuples of distinct indices for a total of 63 = 20, 6 4 = 15, and 65 = 6 summands, respectively.

Addition of the error bounds Ek,1 + ··· + Ek,6 yields error bounds for Ik, which in turn give error bounds for the matrix coeﬃcients Qm,n. Applying Schur’s test to each block with a ﬁxed D individually shows that the matrix consisting of the error bounds has operator norm less than 10−5. These steps were again performed via Mathematica. Since 10−5 is smaller than the minimal eigenvalues shown in Table 1, we can conclude that the matrix (Qm,n)m,n∈X is positive deﬁnite. This completes the proof of Theorem 1.

4. Further remarks

We conclude our discussion with several observations. Table 1 reveals that the smallest eigenvalues of the block D is increasing in

the parameter D ≥ 0. It might be interesting to ﬁnd an analytic explanation of this fact.

Zooming into the main block D = 0, Figure 1 shows the non-zero eigenvalues of this block. There is a cluster of very small eigenvalues. The corresponding eigenvectors seem to suggest that many of these small eigenvalues are related to functions on the circle that are mainly supported in neighborhoods of two antipodally symmetric points. These functions are close competitors of constants for being maximizers. A line of attack on this problem, say for larger or inﬁnite bandwidth, might be to understand how to analytically separate the eﬀect of these antipodal functions. The remaining eigenvalues may be suﬃciently far from zero to allow for crude estimation.

0.08

0.06

0.04

0.02

20 40 60 80 100 120

Figure 1. Plot of the eigenvalues 0 < λ1 ≤ λ2 ≤ ... ≤ λ127 of the approximation to the block D = 0.

We calculated the entries of the quadratic form Q numerically. A look at these entries reveals some nice patterns such as circular structures, shown Figures 2 and 3 below. We do not know how to exactly describe or explain these structures independently of the numerical calculations. These structures merit further investigation. Each of the six ﬁgures below shows a row of the block D = 0. This corresponds to ﬁxing an index m0, and plotting the matrix entries corresponding to Qm0,n, where n ranges over all admissible values. Since n1 + n2 + n3 = 0, we may parametrize the entries of the row by (n1,n2), which ranges in a hexagonal region in Z2, shown in the ﬁgures as complement of the shaded region.

We close with a remark on the central Bessel integral I(0,0,0,0,0,0) =

∞

J06(r)r dr,

0

which up to a factor (2π)4 is the conjectured sharp constant Φ(1) in the Tomas–Stein adjoint restriction inequality. This integral appears in the following related context. An n-step uniform random walk is a walk in the

| |
|---|


| |
|---|


| |
|---|


- Figure 2. m0 = (−24,0,24), m0 = (−12,0,12), m0 = (−6,0,6).

| |
|---|


| |
|---|


| |
|---|


- Figure 3. m0 = (−20,8,12), m0 = (−12,6,6), m0 = (−10,2,8).


plane that starts at the origin and consists of n steps of length 1 each taken into a uniformly random direction.

If pn denotes the radial density of the distance travelled after n steps, then it is a classical result that p5(1) = I(0,0,0,0,0,0), see e.g. [BSWZ]. In the same paper, the exact value of the integral

p4(1) =

∞

- 1

- 2π2


J05(r)r dr =

0

Γ(151 )Γ(152 )Γ(154 )Γ(158 ) 5Γ(157 )Γ(1115)Γ(1315)Γ(1514)

is determined resorting to striking modularity properties of the function p4, see [BSWZ, Theorems 4.9 and 5.1]. The corresponding problem with a sixth power remains open.

Acknowledgements

We thank Emanuel Carneiro, Damiano Foschi and Felipe Gon¸calves for stimulating discussions. The software Mathematica was used to perform the numerical tasks described in §3 and §4. The authors acknowledge support by the Hausdorﬀ Center for Mathematics and the Deutsche Forschungsgemeinschaft through the Collaborative Research Center 1060.

References

[BSWZ] J. Borwein, A. Straub, J. Wan and W. Zudilin, Densities of short uniform random walks. With an appendix by Don Zagier. Canad. J. Math. 64 (2012), no. 5, 961–990.

[CFOT] E. Carneiro, D. Foschi, D. Oliveira e Silva and C. Thiele, A sharp trilinear inequality related to Fourier restriction on the circle. Rev. Mat. Iberoam. 33 (2017), no. 4, 1463–1486.

[Fo] D. Foschi, Global maximizers for the sphere adjoint Fourier restriction inequality. J. Funct. Anal. 9 (2015), no. 3, 690–702. [Go] F. Gonc¸alves, Orthogonal polynomials and sharp estimates for the Schro¨dinger equation. Preprint, 2017. arXiv:1702.08510. To appear in Int. Math. Res. Not. [OT] D. Oliveira e Silva and C. Thiele, Estimates for certain integrals of products of six Bessel functions. Rev. Mat. Iberoam. 33 (2017), no. 4, 1423–1462.

- [Sh1] S. Shao, On existence of extremizers for the Tomas–Stein inequality for S1. J. Funct. Anal. 270 (2016), 3996–4038.
- [Sh2] S. Shao, On smoothness of extremizers of the Tomas–Stein inequality for S1. Preprint, 2016. arXiv: 1601.07119.


[To] P. Tomas, A restriction theorem for the Fourier transform. Bull. Amer. Math. Soc. 81 (1975), no. 2, 477–478. [W] Wolfram Research, Inc., Mathematica. Version 11.1.1.0, Champaign, IL

(2017).

School of Mathematics, University of Birmingham, Birmingham, B15 2TT,

England E-mail address: d.oliveiraesilva@bham.ac.uk Hausdorff Center for Mathematics, 53115 Bonn, Germany

E-mail address: thiele@math.uni-bonn.de E-mail address: pzorin@math.uni-bonn.de

