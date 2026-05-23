# arXiv:1509.06309v2[math.CA]30Sep2015

## ESTIMATES FOR CERTAIN INTEGRALS OF PRODUCTS OF SIX BESSEL FUNCTIONS.

DIOGO OLIVEIRA E SILVA AND CHRISTOPH THIELE

Abstract. We establish good numerical estimates for a certain class of integrals involving sixfold products of Bessel functions. We use relatively elementary methods. The estimates will be used in the study of a sharp Fourier restriction inequality on the circle in [1].

1. Introduction

Let (S1,σ) denote the unit circle in the plane equipped with its arc length measure. The companion paper [1] discusses partial progress towards understanding the optimal constant Copt in the endpoint Tomas-Stein adjoint restriction inequality [6] on the circle:

- (1) fσ L6(R2) ≤ Copt f L2(S1), where the Fourier transform of the measure fσ is given by
- (2) fσ(x) = S1

f(ω)e−ix·ωdσω, (x ∈ R2).

It is conjectured that equality is attained in (1) when f is a constant function. For the constant function f = 1, the sixth power of the left-hand side of inequality (1) turns into the integral

- (3) (2π)7

∞

0

J06(r)rdr, where the Bessel function of order n, denoted Jn, is deﬁned via the identity

- (4) ein·σ(x) = 2π(−i)nJn(|x|)einarg(x).


Part of the analysis in [1] consists of a Fourier expansion of f on the circle, and one needs estimates with rather precise numerical error bounds for integrals of the following two types:

Date: July 12, 2018. 2010 Mathematics Subject Classiﬁcation. 33C10, 42B10, 65D30. Key words and phrases. Bessel functions, Fourier restriction, asymptotic analysis, Newton-Coates quad-

rature.

1

∞

Jn+m(r)Jn(r)Jm(r)J03(r)rdr and

### (5) I0 = I0,m,n :=

0

∞

Jn+m(r)Jn(r)Jm(r)J12(r)J0(r)rdr.

### (6) I1 = I1,m,n :=

0

The purpose of the present paper is to establish these estimates, summarized in the following theorem:

Theorem 1. Let n ≥ 2 be some integer. Then each of the following quantities is less than 0.002n−4:

- (i) For n ≥ 7: I0,0,n −

- 3

- 4π2


1 n

+

3 32π2

1 (n − 1)n(n + 1)

, and for n ≥ 3:

I1,0,n −

1 4π2

1 n −

3 32π2

1 (n − 1)n(n + 1)

.

- (ii) For any n ≥ 2 :


1 n(n + 1)(n + 2)

15 64π2

I0,2,n −

,

9 64π2

1 n(n + 1)(n + 2)

I1,2,n −

. Moreover, each of the following quantities is less than 0.0015n−4:

- (iii) For n ≥ 4:

I0,4,n −

1557 1024π2

1 n(n + 1)(n + 2)(n + 3)(n + 4)

,

I1,4,n −

855 1024π2

1 n(n + 1)(n + 2)(n + 3)(n + 4)

.

- (iv) For even m ≥ 6 and n ≥ m: |I0,m,n| and |I1,m,n|.


Thus Theorem 1 controls integrals of the two types I0 and I1 for n ≥ 2 and even 0 ≤ m ≤ n, with the exception of the ﬁve cases m = 0 and n = 2,3,4,5,6 for I0, and the two cases m = 0 and n = 2,3 for I1. It follows from Table 1 below that, in these exceptional cases, the quantities are still less than 0.01n−4, which provides information about I0 and I1 with at least two percent relative accuracy.

It follows from the methods of this paper, or alternatively from general principles, that such a result holds with bounds cn−4 for any positive number c in place of 0.002 or 0.0015, and with some ﬁnite set of exceptions. The point of Theorem 1 is to narrow down these exceptions precisely for the speciﬁc numbers c = 0.002 (for m = 0,2) and c = 0.0015 (for

m ≥ 4). Slightly better numerical estimates are listed in Sections 7 and 8 for the various cases, but for simplicity we do not reproduce all of them here.

Our methods apply to obtain a more general set of estimates than the ones listed in Theorem 1, but we focus on the stated estimates which are needed in [1]. There exists a very satisfactory theory of similar integrals of products of two Bessel functions, see for example Lemmata 3 and 4 below, and a still explicit but substantially more complicated theory for integrals of products of four Bessel functions. While integrals of sixfold products of Bessel functions still fall into the class of functions for which explicit symbols have been introduced in the theory of hypergeometric functions and their generalizations, we do not know how to obtain our rather accurate numerical bounds in a much easier way than by the elementary but somewhat laborious approach presented in this paper.

Our approach is to expand four of the six Bessel function factors, namely those four with the lowest orders, into their asymptotic expansions. This will reduce the integrals in question to core integrals of the type

(7)

∞

Jn(r)Jn+m(r)sin( r)r−kdr,

0

∞

Jn(r)Jn+m(r)cos( r)r−kdr

0

for = 0,±2,±4. For these integrals, one has good information as in Lemmata 2, 4, 5. In more detail, the paper is organized as follows. In Section 2, we review the theory of Bessel functions inasmuch as it is useful for our purposes. In particular, we establish the aforementioned lemmata, together with asymptotic expansions with precise control on the error terms. In Section 3, we prove some useful estimates for binomial coeﬃcients, the Gamma function, and the coeﬃcients that arise in the various asymptotic expansions. The analytic part of the proof of Theorem 1 begins in Section 4, where we asymptotically expand the functions J0 and J1. Section 5 accomplishes the same for the function of next lowest order, namely Jm. Finally, Section 6 is devoted to the analysis of the core integrals. The estimates from Sections 4−6 are then assembled together in Section 7. The approach works for n ≥ 20, and so for n < 20 we numerically estimate the integrals; this is the content of the ﬁnal Section 8.

We close this discussion with a brief illustration of the diﬃculty involved. Figure 1 depicts the plot of the integrand of I1,6,9 between r = 0 and r = 100. One observes an initial region until about r = n = 9 where the function is very small. Then one sees a region with fairly erratic behaviour until about r = n2 = 81. Past r = 81, one sees a more repetitive behaviour where one has good asymptotic control. The asymptotic region yields a positive contribution to the desired integral, which is in general of the order n−2. The erratic region yields a negative contribution which nearly cancels the positive part from the asymptotic region. In question is a very good numerical control of the order n−4 of the small diﬀerence. The main tools to capture this cancellation are the algebraic identities from Lemma 2 and an exact orthogonality formula due to Kapteyn [2] which can be found in Lemma 3.

0.0004

0.0002

20 40 60 80 100

- -0.0004

- -0.0002


Figure 1. Plot of the function J15(r)J9(r)J6(r)J12(r)J0(r)r for 0 ≤ r ≤ 100.

Acknowledgements. The software Mathematica was heavily used in the brainstorming phase of the research project, as well as in the numerical part of the paper. We are thankful to Emanuel Carneiro for helpful discussions during the preparation of this work, and to Pavel Zorin-Kranich for pointing out an improvement to the ﬁrst version of our Mathematica code. Finally, we would like to thank both the Hausdorﬀ Center for Mathematics and the Hausdorﬀ Institute for Mathematics for support.

2. Background on Bessel functions

We rewrite the deﬁnition (4) of the Bessel function in the form of a Bessel integral which is the starting point in [5, p. 338]. For n ∈ Z and z ≥ 0, we claim that

- (8) Jn(z) =

- 1

- 2π


π

−π

eizsinθe−inθdθ.

More precisely, replacing θ = ω + π/2 in (8) and using even symmetry of the cosine we obtain for the right-hand side of (8):

- (9)


π

π

(−i)n 2π

(−i)n π

eizcosωe−inωdω =

eizcosω cos(nω)dω, from which the equivalence of (8) and (4) is evident.

−π

0

The Bessel function, deﬁned via (8) for general z ∈ C, is an entire function. From (8) we obtain the estimate

- (10) |Jn(z)| ≤ e| (z)|.

Diﬀerentiation under the integral sign in (8) and integration by parts yield the following recurrence relations in the sense of meromorphic functions:

- (11) Jn−1(z) − Jn+1(z) = 2J n(z),

Jn−1(z) + Jn+1(z) =

2n z

- (12) Jn(z).

A diﬀerent representation of the Bessel function is the Poisson integral, which contains a power of a trigonometric function rather than a power of an exponential function:

- (13) Jn(z) =

(z/2)n Γ(n + 1/2)Γ(1/2)

π

0

cos(z cos(θ))sin2n(θ)dθ . Here we use the Gamma function

Γ(s) :=

∞

0

e−tts−1dt ,

which satisﬁes the functional equation sΓ(s) = Γ(s+1) and thus meromorphically extends the factorial, that is Γ(n + 1) = n! for natural numbers n. We mainly need the Gamma function for half-integer values, which can be expressed as

- (14) Γ

- 1

- 2


+ n =

(2n)! 4nn!

√π and Γ

- 1

- 2 − n =


(−4)nn! (2n)!

√π.

This can be recursively veriﬁed from Γ(21) = √π, which in turn can be read from the well-known property

- (15) sin(πx)Γ(x)Γ(1 − x) = π.

The latter can be seen by verifying periodicity of the left-hand side together with growth estimates which force the left-hand side to be constant.

To see equivalence of the Poisson integral representation (13) with (8), one veriﬁes the case n = 0 by substitution and then veriﬁes by partial integration that the Poisson integral also satisﬁes the recursion relations (11) and (12). Combining these two second order recurrence relations into a ﬁrst order relation between Jn and Jn+1, equivalence of the two integral representations follows recursively by a uniqueness result for ordinary diﬀerential equations, where we use that both integral representations vanish for z = 0 and n > 0.

From the Poisson integral representation one sees the following estimate from [7, §3.31(1), p. 49], useful for small z:

- (16) |Jn(z)| ≤


|z|ne| z| 2nn!

,

where we have used

π

1 n!

1 Γ(n + 1/2)Γ(1/2)

sin2n(θ)dθ , which one proves by induction on n using integration by parts.

=

0

We turn to the core integrals (7). The case = ±2 will be the most pleasant to deal with via the following lemma:

- Lemma 2. Let 0 ≤ n,m have the same parity, and 1 ≤ k ≤ n + m. Then if k is even ∞

0

Jn(r)Jm(r)r−k cos(2r)dr = 0 , and if k is odd

∞

0

Jn(r)Jm(r)r−k sin(2r)dr = 0 .

Proof. By the parity assumption, we may extend the integrals to the full real line. It then suﬃces to show that the Fourier transform

∞

−∞

Jn(r)Jm(r)r−ke−iξr dr vanishes at ξ = 2. Substituting ξ = cosω on the right-hand side of (9) yields Jn(z) =

(−i)n π

1

−1

eizξ

cos(narccosξ) 1 − ξ2

dξ .

Hence we see that Jn is the Fourier transform of the function Bn(ξ) =

(−i)n π

Tn(ξ)(1 − ξ2)−1/21[−1,1](ξ) , where Tn denotes the Chebysheﬀ polynomial Tn(ξ) := cos(narccosξ).

We ﬁrst consider the case k ≤ n in the lemma. Then the Fourier transform Bn(−k) of Jn(r)r−k is still supported on [−1,1] since Bn has vanishing moments of orders 0,1,...,k− 1. This can be deduced from (13). Seen as the convolution of an Lp function with an Lp

function for p = 2−, the function Bn(−k) ∗ Bm is continuous. Since it is also supported on the interval [−2,2], it must vanish at ξ = 2. This proves the lemma in case k ≤ n. If n < k ≤ n + m, we distribute some powers of r over Jm and argue similarly.

The understanding of the dominant case = 0 of the core integrals (7) begins with Kapteyn’s identity, proved in a delightful two page paper [2].

- Lemma 3 ([2]). If n,m ≥ 0 and n + m = 0, then


sin m−2 nπ m2 − n2 with the following natural interpretation in case n = m:

∞

2 π

Jn(r)Jm(r)r−1dr =

(17)

0

∞

- 1

- 2n


Jn(r)2r−1dr =

.

0

Note in particular that (17) vanishes if m − n is a nonzero even integer. Moreover, identities (14), (15), and some algebra yield

sin m2−nπ m2 − n2

2−1Γ(m2+n) Γ(m+2n+2)Γ(n−m2 +2)Γ(m−2n+2)

2 π

=

. From Kapteyn’s identity, one obtains the following more general result.

- Lemma 4. If 0 ≤ n,m and 1 ≤ k ≤ n + m, then

(18)

∞

0

Jn(r)Jm(r)r−kdr =

2−kΓ(k)Γ(m+n2+1−k) Γ(m+n2+1+k)Γ(n−m2+k+1)Γ(m−n2+k+1)

.

Proof. The identity is true for k = 1 by Lemma 3. Let k ≥ 1 be given and assume that identity (18) is true for this particular k. To prove the identity for k + 1 we denote the integral in (18) by In,m,k. Then, by the second recursion in (12) and using the induction hypothesis, we have that

In,m,k+1 =

- 1

- 2n


(In−1,m,k + In+1,m,k)

=

2−(k+1)n−1Γ(k)Γ(m+2n−k) Γ(m+2n+k)Γ(n−m2 +k)Γ(m−n2+k+2)

+

2−(k+1)n−1Γ(k)Γ(m+n2+2−k) Γ(m+n2+2+k)Γ(n−m2+k+2)Γ(m−2n+k)

=

2−(k+1)Γ(k + 1)Γ(m+2n−k) Γ(m+n2+2+k)Γ(n−m2+k+2)Γ(m−n2+k+2)

(m + n + k)(n − m + k) + (m + n − k)(m − n + k) 4nk

The second fraction in the last line is equal to 1, and this proves the inductive step.

Note in particular that if k is odd and satisﬁes k < |n−m|, then (18) vanishes since the function 1/Γ has zeros at s = 0,−1,−2,... Note also that three of the Gamma factors, the one with argument k in the numerator and the two involving the diﬀerence m − n in the denominator, typically form a binomial coeﬃcient, which can be roughly estimated by 2k. An alternative approach to Lemma 4 is the integration theory of Weber and Schafheitlin as outlined in [7, §13.24, p. 398].

The case = ±4 of the core integrals (7) gives small error terms which we estimate with the following lemma.

- Lemma 5. Let 0 ≤ n,m and 1 ≤ k < n + m. Then: ∞


2k−1 4n+m

Jn(r)Jm(r)r−ke4irdr ≤

0

(n + m − k)! n!m!

.

Proof. We estimate this integral by the descent method, changing the contour of integration to the contour consisting of a line segment from 0 to iN for some large N, then a line segment from iN to N, and then a ray from N to ∞ along the real axis. Only the ﬁrst integral provides a substantial contribution, since the next two segments give contributions that tend to 0 as N tends to inﬁnity.

Along the ﬁrst segment of the contour the integral can be estimated using (16) by

∞

∞

1 n!m!

- 1

- 2n+m


|Jn(ix)||Jm(ix)|x−ke−4xdx ≤

xn+m−ke−2xdx

0

0

2k−1 4n+m

(n + m − k)! n!m!

=

. The integral over the second part of the contour is estimated using (10) by √

N

|Jn(x + i(N − x))||Jm(x + i(N − x))||x + i(N − x)|−ke−4(N−x)dx

2

0

√

√

N

2)−ke−2(N−x)dx ≤ 2k+1N−k ,

≤

(N/

2

0

which tends to 0 as N → ∞. The integral over the third piece of the contour is estimated using the fact that the functions Jn and Jm are in L4 as Fourier transforms of L4/3 functions and thus the continuous function Jn(r)Jm(r)r−1 is in L1. It then follows from the dominated convergence theorem that

∞

|Jn(r)Jn+m(r)|r−1dr = 0 . Adding the contour integrals and letting N → ∞ yields the desired bound.

lim

N→∞

N

To arrive at the core integrals, we need asymptotic expansions of the Bessel functions near inﬁnity as in the following lemma. Lemma 6. Let n ∈ N and (z) > 0. Let ωn = z − nπ/2 − π/4. Let ∈ N be such that

≥ max{n − 1/2,1}. If is even, then

- (19)

Jn(z) =

2 πz

- 1

- 2 (cosωn)


 

2−1

k=0

(−1)k

a2k(n) z2k

  − (sinωn)

 

2−1

k=0

(−1)k

a2k+1(n) z2k+1

  + Rn, (z).

If is odd, then

- (20)

Jn(z) =

2 πz

- 1

- 2 (cosωn)


 

−1 2

k=0

(−1)k

a2k(n) z2k

  − (sinωn)

 

−3 2

k=0

(−1)k

a2k+1(n) z2k+1

  + Rn, (z).

Here the coeﬃcients aj(n) are deﬁned by

- (21) aj(n) =


Γ(n + j + 12) Γ(n − j + 12)j!2j

,

and the remainder function Rn,  satisﬁes the bounds

−n+12

- 1

- 2 Γ(n + + 21) |Γ(n − + 12)| !


|z| (z)

2 π|z|

- 1

- 2|z|


|Rn, (z)| ≤

cosh( (z))

.

Proof. We expand on the proof outlined in Watson [7, §7.3, p. 205]. The change of variables t = cosθ turns the Poisson integral (13) into

1

(z/2)n Γ(n + 1/2)Γ(1/2)

cos(zt)(1 − t2)n−1/2 dt .

Jn(z) =

−1

We split

- 1

- 2


(Jn+(z) + Jn−(z)), with

Jn(z) =

1

(z/2)n Γ(n + 1/2)Γ(1/2)

eizt(1 − t2)n−1/2 dt

Jn+(z) =

−1

and Jn−(z) = Jn+(z). Now we change the contour in the integral for Jn+ towards a Π-shaped contour consisting of the line segment from −1 to −1 + iN, followed by the line segment from −1 + iN to 1 + iN, and then the line segment from 1 + iN to 1. On that contour as well as on its convex hull, we have (1−t2) ≥ 0 with equality only at the end points of the contour. Hence we may choose the continuous branch of the square root function on the slit plane C\(−∞,0) which takes positive values on the positive real axis. For simplicity of notation, let us introduce the half-integer ν := n−1/2. The integral over the ﬁrst segment of the contour becomes

(z/2)ν+1/2 Γ(ν + 1)Γ(1/2)

N

e−iz (2πz)1/2Γ(ν + 1)

e−ize−zs(2is + s2)νids =

0

ei(−z+(ν+1)π/2) (2πz)1/2Γ(ν + 1)

=

zN

e−uuν(i +

0

zN

e−uuν(1 −

0

u 2z

)νidu

iu 2z

)ν du ,

where in the ﬁrst identity we replaced zs by u and rotated the contour towards the line segments from 0 to zN, and used Γ(1/2) = π1/2. In the second identity, we ﬁrst pulled an integer power of i out of the integral and and then pulled half a power of i out of the integral without leaving the domain of deﬁnition of the chosen branch of the square root function. If (z) > 0, then this last integral has a limit as N → ∞. Similarly, the integral over the third line segment becomes

(z/2)ν+1/2 Γ(ν + 1)Γ(1/2)

−

N

ei(z−(ν+1)π/2 (2πz)1/2Γ(ν + 1)

eize−zs(−2is+s2)νids =

0

zN

e−uuν(1+

0

iu 2z

)ν du .

If (z) > 0, then the limit again exists. Moreover, the integral over the second line segment tends to 0 as N → ∞. We therefore obtain

∞

(2πz)−1/2 Γ(ν + 1)

iu 2z

iu 2z

e−uuν e−iωn(1 −

Jn+(z) =

)ν + eiωn(1 +

)ν du ,

0

where ωn = z − nπ/2 − π/4 = z − (ν + 1)π/2, and the contour has been changed to one along the real axis.

The function (1 + αu)ν is inﬁnitely diﬀerentiable in u ∈ [0,∞) for any α ∈ C \ (−∞,0]. Taylor’s expansion gives, for any ≥ 1,

−1

(αu)k k!

Γ(ν + 1) Γ(ν + 1 − k)

u

(1 + αu)ν =

+ r

,

!

k=0

where r is the -th derivative of the function u  → (1 + αu)ν at some point u0 ∈ [0,u]. If

> ν, then this derivative is proportional to a negative power of the function and thus attains its maximum at the point where the value of the function comes closest to the origin. This point equals u = − (α)/|α|2 and the value of the -th derivative there equals

ν−

(α) α

Γ(ν + 1) Γ(ν + 1 − )

α 1 −

. Hence we can write for the remainder term

ν− (αu)

Γ(ν + 1) Γ(ν + 1 − )

(α) α

u

1 −

= θ(u)

r

! for some |θ(u)| ≤ 1 that also depends on α. Note that

!

(α) α | = |α − (α)|

= | (α)| |α|

|1 −

,

|α|

and the latter equals (z)/|z| if α = ±i/(2z) = ±iz/(2|z|2). For (z) > 0, we have that 1 ± 2iuz is not real, hence we may insert the Taylor expansion into the integral for Jn+, and obtain for Jn+(z) the expression

−1

∞

e−uuν+k e−iωn −i 2z

1 Γ(ν + 1 − k)k!

(2πz)−1/2

0

k=0

−1

k

e−iωn −i 2z

Γ(ν + k + 1) Γ(ν + 1 − k)k!

= (2πz)−1/2

+ eiωn

k=0

where the remainder term R = Rn,  satisﬁes

k

+ eiωn

i 2z

k

i 2z

k

+ R(z) ,

du + R(z)

−ν

|z| (z)

1/2 Γ(ν + + 1) |Γ(ν + 1 − )| !

- 1

- 2|z|


2 π|z|

|Rn, (z)| ≤

. We split the summation into even integers and odd integers to obtain

cosh( (z))

Jn+(z) =

−

2 πz

2 πz

Γ(ν + k + 1) Γ(ν + 1 − k)k!2k

1/2

(−1)k/2

cos(ωn)

0≤k< : k even

1 z

Γ(ν + k + 1) Γ(ν + 1 − k)k!2k

1/2

(−1)(k−1)/2

sin(ωn)

0≤k< : k odd

This completes the proof of the lemma.

k

1 z

k

+ Rn, (z).

We specify our ﬁndings into explicit ﬁrst order asymptotics valid for suﬃciently large z near the positive real axis. We have with the notation from the above proof: Corollary 7. Let z ∈ C be such that (z) < (z). Then

- J0±(z) −

2 πz

1/2

cos(ω0) ≤

1 8|z|

2 π|z|

1/2

cosh( (z)) |z| | (z)|

3/2

,

- J1±(z) −


1/2

2 πz

3 8|z|

cos(ω1) ≤

and if n > 1 and (z) > n2, then

2 π|z|

1/2

cosh( (z)) |z| | (z)|

1/2

,

1/2

1/2 n2 |z|

1/2

cosh( (z)) |z| | (z)|

2 πz

2 π|z|

Jn±(z) −

cos(ωn) ≤

.

Proof. Following the previous argument, only the last inequality requires explanation. We choose = n = ν + 1/2, and apply the above expansion with the observation that

for k ≤ ν. It follows that

1/2

2 πz

Jn±(z) −

- 1

- 2


Γ(ν + 1 + k) Γ(ν + 1 − k) ≤ ν +

2k

cos(ωn) ≤

2 π|z|

1/2 −1

n2k cosh( (z))(2|z|)−k + R

k=1

1/2

1/2

1/2

n2 |z|

n2 |z|

|z| | (z)|

2 π|z|

2 π|z|

(1 − 21− ) + R ≤

≤

, where in the last line we estimated the remainder similarly to the terms in the expansion.

cosh( (z))

cosh( (z))

One proves explicit asymptotics with one extra term in a similar way:

- Corollary 8. Let z ∈ C be such that (z) > 1/4 and (z) < (z). Then

- J0±(z) −

2 πz

1/2

cos(ω0) +

1 8z

2 πz

1/2

sin(ω0) ≤

≤

9 128|z|2

2 π|z|

1/2

cosh(| (z)|) |z| | (z)|

5/2

,

- J1±(z) −


2 πz

1/2

cos(ω1) +

3 8z

2 πz

1/2

sin(ω1) ≤

≤

15 128|z|2

2 π|z|

1/2

cosh( (z)) |z| | (z)|

3/2

,

and if n > 1 and (z) > n2, then

Jn±(z) −

2 πz

1/2

cos(ωn) +

4n2 − 1 8z

2 πz

1/2

sin(ωn) ≤

≤

1 4

2 π|z|

1/2

cosh( (z))

n4 |z|2

|z| | (z)|

1/2

.

Finally, we need zero order upper bounds for the asymptotic expansion:

- Corollary 9. For r > 0, we have that


- (a)

|J0(r)| ≤

9 8

2 πr

1/2

,

- (b)


11 8

|J1(r)| ≤

2 πr

1/2

.

Proof. This follows for r > 1 from Corollary 7, while for r ≤ 1 it follows from the trivial bound |Jn| ≤ 1.

Remark. Using more reﬁned oscillatory techniques related to Sturm’s comparision principle, the sharper bound r1/2|J0(r)| ≤ (2/π)1/2 is established in [3]. However, the bounds given by Corollary 9 suﬃce for our purpose, and its proof is more in light with the elementary nature of the present paper.

3. Useful estimates involving the Gamma function A version [4] of Stirling’s formula for the Gamma function states that, for x ≥ 0,

- (22) Γ(x) =

√

2πxx−1/2e−xeµ(x), where the function µ satisﬁes the double inequality

- (23)

1 12x + 1

< µ(x) <

1 12x

. The starting point for all the convex estimates we need is the following well-known result: Lemma 10. For x > 0, the function x  → log(Γ(x)) is convex. Proof. Let x,y > 0 and 0 < λ < 1. Set p = λ1 and q = 1−1λ. It suﬃces to show that

- (24) Γ


x p

+

y q ≤ Γ(x)

1

1

pΓ(y)

q ,

for then the result follows by taking logarithms on both sides. To verify (24), consider the auxiliary functions

y−1

x−1

t

t

p e−

q e−

q , which satisfy

f(t) := t

p and g(t) := t

p+yq−1e−t, f(t)p = tx−1e−t, and g(t)q = ty−1e−t. The result is thus a consequence of H¨lder’s inequality.

x

f(t)g(t) = t

- Corollary 11. Let x ≥ 21. Then:

x − 1/2 ≤

Γ x + 12 Γ(x) ≤

√x. Proof. Use the identity x = Γ(x + 1)/Γ(x) together with log convexity of Γ.

- Corollary 12. Let x ≥ y > 0 and w ≥ 0. Then:


- Γ(x)

- Γ(y) ≤


- Γ(x + w)

- Γ(y + w)


. Proof. For ﬁxed w ≥ 0, we claim that the function

Γ(x) Γ(x + w)

x  →

is decreasing in x. This happens if the inequality Γ (x) Γ(x) ≤

Γ (x + w) Γ(x + w)

holds for every x > 0, which in turn is a consequence of the log convexity of Γ proved in Lemma 10.

The following lemma estimates binomial coeﬃcients.

Lemma 13. Let x ≥ 1 and let 0 ≤ d < x be an integer. Then:

e1/24 2√π

Γ(2x) Γ(x − d)Γ(x + d) ≤

x1/222xe−d2/x. Proof. By Stirling’s formula (22), we have that

(25)

(2x)2x−1/2 √2πx2x−1 eµ(2x)−2µ(x) =

### x1/222x 2√π

Γ(2x) Γ(x)2

eµ(2x)−2µ(x).

=

Also, since x ≥ 1, we have that µ(2x) ≤ 241 , and therefore

eµ(2x)−2µ(x) ≤ eµ(2x) ≤ e1/24. It follows that

e1/24 2√π

Γ(2x) Γ(x)2 ≤

x1/222x. By induction, observe that

d

- d

j=1

- e−2j/x = e−(d2+d)/x,


x − j x + j ≤

Γ(x)Γ(x + 1) Γ(x − d)Γ(x + d + 1)

=

j=1

whenever d is an integer satisfying 0 ≤ d < x. This is a consequence of the elementary inequality

1 − y 1 + y ≤ e−2y,

which is valid in particular for y ∈ [0,1]. Using (x + d)/d ≤ ed/x we obtain that

d

- d

j=1

- e−2j/x = e−d2/x,


x − j x + j ≤ ed/x

Γ(x)Γ(x) Γ(x − d)Γ(x + d) ≤ ed/x

j=1

again for integers d ∈ [0,x). Finally,

Γ(2x) Γ(x − d)Γ(x + d)

=

as desired. Remark. The inequality

e1/24 2√π

Γ(2x) Γ(x)2

Γ(x)Γ(x) Γ(x − d)Γ(x + d) ≤

x1/222xe−d2/x,

Γ(x)Γ(x)

Γ(x − d)Γ(x + d) ≤ e−d2/x, is still valid for non-integer values of d ∈ [0,x), and therefore Lemma 13 holds in this case as well.

We will also need estimates for the magnitude of the coeﬃcients aj(m) deﬁned in (21) when j is close to m. More precisely, in Section 5 we will need good upper bounds for the quantities |am+4(m)|. For small values of m, we compute them explicitly. For large values of m, we estimate these quantities via the following lemma.

Lemma 14. For any natural number m ≥ 1, we have that

105 16

2 π

(2m − 1)−1/22mmme−m. Proof. The goal is to bound the absolute value of

|am+4(m)| ≤

Γ(2m + 9/2) Γ(−7/2)Γ(m + 5)2m+4

am+4(m) =

.

Making repeated use of the identity Γ(x+1) = xΓ(x), together with the convexity estimate from Corollary 11 and Stirling’s formula (22), we have that

Γ(2m − 1/2) Γ(−7/2)Γ(m)2m+4 ≤ 2(2m − 1)−1/2

|am+4(m)| ≤ 25

Γ(2m) Γ(−7/2)Γ(m)2m

2(2m − 1)−1/2 Γ(−7/2)2m

(2m)2m−1/2 mm−1/2 e−meµ(2m)−µ(m).

=

The bounds (23) for the function µ imply that µ(2m) ≤ µ(m), and so eµ(2m)−µ(m) ≤ 1. It follows that

2(2m − 1)−1/2 Γ(−7/2)2m

22m−1/2mme−m.

- (26) |am+4(m)| ≤


√π

The value Γ(−7/2) = 16

105 can be computed via the second formula in (14), and this completes the proof.

4. Part I. Expanding J0 and J1

In the next four sections, we will be working under the standing assumption that n ≥ n0 := 20. We start by asymptotically expanding the Bessel functions of order 0 and 1 and their relevant products. Due to need of accuracy, we must consider asymptotic expansions of length six and keep track of all the terms. The following notation will be convenient. Let us say that

a ∼ (a0) + (a1) + (a2) + (a3) + (a4) + (a5) with remainders r0,r1,r2,r3,r4,r5,r6 if

k

ai−1 ≤ rk, for every 0 ≤ k ≤ 6. We also call r6 the last remainder. Suppose additionally that

a −

i=1

b ∼ (b0) + (b1) + (b2) + (b3) + (b4) + (b5) with remainders s0,s1,s2,s3,s4,s5,s6. Then we have the following product formula:

5

k

ab ∼

(

aibk−i) with remainders

i=0

k=0

k

ri|bk−i|, for every 0 ≤ k ≤ 6. Recall the coeﬃcients a0(n) through a5(n) for n = 0,

r0sk +

i=1

9 128

75 1024

3675 32768

59535 262144

2401245 4194304

57972915 33554432

1 8

, −

, −

, −

1, −

, and for n = 1,

,

,

,

15 128

105 1024

4725 32768

72765 262144

2837835 4194304

66891825 33554432

3 8

, −

, −

, −

. To make the forthcoming notation less cumbersome, let us deﬁne, in view of Lemma 6,

1,

,

,

,

πr 2

1/2

Jn(r). To avoid writing many fractions, we further deﬁne t := (16r)−1. We also set

Jn(r) :=

c := cos(r − π/4) and s := sin(r − π/4). From Lemma 6 and Corollary 9, we have that

J0(r) ∼ (c) + (2ts) + (−18t2c) + (−300t3s) + (7350t4c) + (238140t5s) with remainders discussed there as

9 8

, 2t, 18t2, 300t3, 7350t4, 238140t5, 9604980t6. In a similar way,

J1(r) ∼ (s) + (6tc) + (30t2s) + (−420t3c) + (−9450t4s) + (291060t5c) with remainders

11 8

, 6t, 30t2, 420t3, 9450t4, 291060t5, 11351340t6.

Applying the product formula, we obtain successively J20(r) ∼ (c2) + (4tcs) + (−36t2c2 + 4t2s2) + (−672t3cs)+

+ (15024t4c2 − 1200t4s2) + (516480t5cs) with remainders

81 64

17 4

169 4

1419 2

68571 4

1092495 2

43435485 2

t6, and

t2,

t3,

t4,

t5,

,

t,

- (27) J30(r) ∼ J000(r) :=(c3) + (6tc2s) + (−54t2c3 + 12t2cs2) + (−1116t3c2s + 8t3s3)

+ (23022t4c3 − 3816t4cs2) + (836964t5c2s − 3600t5s3) with remainders

729 512

,

217 32

t,

2353 32

t2,

20003 16

t3,

956787 32

t4,

15017799 16

t5,

588969477 16

t6. In particular,

- (28) |J30(r) − J000(r)| ≤

588969477 16

(16r)−6. On the other hand, we have

J21(r) ∼ (s2) + (12tcs) + (36t2c2 + 60t2s2) + (−480t3cs)+

+ (−5040t4c2 − 18000t4s2) + (443520t5cs) with remainders

121 64

,

57 4

t,

429 4

t2,

2715 2

t3,

113535 4

t4,

1659735 2

t5,

62391105 2

t6, and

(J21J0)(r) ∼ J110(r) :=(cs2) + (12tc2s + 2ts3) + (36t2c3 + 66t2cs2) + (−624t3c2s − 180t3s3)

- (29)

+ (−5688t4c3 − 16290t4cs2) + (519480t5c2s + 184140t5s3) with remainders

1089 512

,

577 32

t,

5433 32

t2,

38331 16

t3,

1638411 32

t4,

23971455 16

t5,

897834285 16

t6. In particular,

- (30) |(J21J0)(r) − J110(r)| ≤


897834285 16

(16r)−6.

Inequalities (28) and (30) are at the core of the following result, the proof of which does not require m to be even, nor m ≤ n.

Estimate A. For n ≥ n0 = 20 and m ≥ 0, we have

- (31)

∞

0

Jn+mJnJm(J30 − J000)r−1dr ≤ 0.74n−0 1/2(n + m)−6,

- (32)


∞

Jn+mJnJm(J21J0 − J110)r−1dr ≤ 1.12n−0 1/2(n + m)−6.

0

Proof of Estimate A. Using the Cauchy-Schwarz inequality and Lemmata 3 and 4 to compute the integrals, we have that

∞

1/2 ∞ 0

1/2 ∞ 0

π 2

dr r

dr r12

|JnJn+mJm|r−7dr ≤

Jn2

Jn2+m

0

Γ(n + m − 112 ) Γ(n + m + 132 )

1 2n

1/2 128 693

1/2

=

64 693n

1/2

≤ a10/2

(n + m)−6, where

1/2

Γ(292 ) Γ(532 )

Γ( − 112 ) Γ( + 132 )

12 =

2012 ≤ 1.21.

a0 := sup ≥n0

Thus, for n ≥ n0, the left-hand side of inequality (31) is bounded by

588969477/16 166

64 693n

1/2

(n + m)−6 ≤ αn0−1/2(n + m)−6, where

a10/2

≤

64 693

588969477/16 166

1/2

a10/2

≤ 0.74. In a similar way, for n ≥ n0, the left-hand side of inequality (32) is bounded by

α =

897834285/16 166

64 693n

1/2

(n + m)−6 ≤ βn0−1/2(n + m)−6, where

a01/2

≤

897834285/16 166

64 693

1/2

a01/2

≤ 1.12.

β =

5. Part II. Expanding Jm

Start by noting that cosωm = (−1)m/2c and sinωm = (−1)m/2s since m is an even integer. We have that

- (33)

where the error term ρm is implicitly deﬁned by this identity. From Lemma 6 we know that

- (34) |ρm(r)| ≤

|am+4(m)| rm+4 for every r ≥ 0. The main integrals, which are the subject of the next section, arise from replacing JmJ000 by

- (35) Jm000 := (Jm − ρm)J000, and JmJ110 by
- (36) Jm110 := (Jm − ρm)J110.

Estimating the error term in this replacement is the main goal of the present section. We formulate it as

Estimate B. Let n ≥ n0 = 20 and m be even.

If m = 0, then

- (37)

∞

0

Jn2(J0J000 − J0000)r−1dr ≤ 0.022n−0 1n−4,

- (38)

∞

0

Jn2(J0J110 − J0110)r−1dr ≤ 0.023n−0 1n−4, If m = 2, then

- (39)

∞

0

Jn+2Jn(J2J000 − J2000)r−1dr ≤ 0.162n−0 1n−6,

- (40)


m 2 +1

m 2 +1

Jm(r) − ρm(r) = (−1)m/2 c

(−1)k(16t)2ka2k(m) − s

(−1)k(16t)2k+1a2k+1(m) ,

k=0

k=0

∞

Jn+2Jn(J2J110 − J2110)r−1dr ≤ 0.166n−0 1n−6, If m = 4, then

0

∞

### Jn+4Jn(J4J000 − J4000)r−1dr ≤ 2.823n−0 1n−8,

0

∞

Jn+4Jn(J4J110 − J4110)r−1dr ≤ 2.885n−0 1n−8, If 6 ≤ m ≤ n, then

0

- (41)

∞

0

Jn+mJn(JmJ000 − Jm000)r−1dr ≤ 0.015n−0 1n−4,

- (42)

∞

0

Jn+mJn(JmJ110 − Jm110)r−1dr ≤ 0.015n−0 1n−4.

Proof of Estimate B. We consider the case m = 0 ﬁrst. The left-hand side of (37) is bounded by

- (43) |a4(0)|

∞

0

Jn2(r)(1 + 6t + 66t2 + 1124t3 + 26838t4 + 840564t5)r−5dr, whereas the left-hand side of (38) is bounded by

- (44) |a4(0)|


∞

Jn2(r)(1 + 14t + 102t2 + 804t3 + 21978t4 + 703620t5)r−5dr. For ∈ {5,6,...,10}, Lemma 4 implies that

0

Γ(n − −21) Γ(n + +12 )

∞

2− Γ( ) Γ( +12 )2

Jn2(r)r− dr =

. This can be estimated as follows:

0

∞

Jn2(r)r− dr ≤ c(0) n− , where

0

Γ(20 − −21) Γ(20 + +12 )

2− Γ( ) Γ( +12 )2

c(0) :=

20 . In particular, for ∈ {5,6,...,10}, one can easily check that

0.14 ≤ c(0) ≤ 0.19.

It follows that the upper bounds for each of the last ﬁve summands on the right-hand side of inequalities (43) and (44) can be estimated by a small fraction of the upper bound for the ﬁrst summand. Quantifying this, one obtains (37) and (38), respectively.

We consider the case m = 2 next. Again for ∈ {5,6,...,10}, the integral to consider is the following:

∞

|Jn(r)Jn+2(r)|r−2− dr.

0

In view of the absolute value in the integrand, this cannot be computed directly with Lemma 4. Instead, we use the Cauchy-Schwarz inequality to estimate

∞

|JnJn+2|r−2− dr ≤

0

=

∞

1/2 ∞ 0

dr r

dr r2 +3

1/2

Jn2

Jn2+2

0

1/2 2−(2 +3)Γ(2 + 3) Γ( + 2)2

Γ(n − + 1) Γ(n + + 4)

- 1

- 2n


1/2

,

where the last identity is a consequence of Lemmata 3 and 4. Reasoning as before, we derive the estimate

∞

|JnJn+2|r−2− dr ≤ c(2) n−2− , where

0

2−(2 +3)Γ(2 + 3) 2Γ( + 2)2

Γ(20 − + 1) Γ(20 + + 4)

1/2

c(2) :=

202 +3

. In particular, for every ∈ {5,6,...,10}, one checks that

0.11 ≤ c(2) ≤ 0.15. As before, it follows that the last ﬁve summands on the right-hand sides of estimates

∞

Jn+2Jn(J2J000 − J2000)r−1dr ≤

0

6 16

66 162

1124 163

26838 164

840564 165

|a6(2)| c(2)5 n−7+

c(2)10 n−12 and

c(2)6 n−8+

c(2)7 n−9+

c(2)8 n−10+

c(2)9 n−11+

∞

Jn+2Jn(J2J110 − J2110)r−1dr ≤

0

14 16

102 162

804 163

21978 164

703620 165

|a6(2)| c(2)5 n−7+

c(2)10 n−12 can be bounded by a small fraction of the ﬁrst summand. Quantifying this yields (39) and

c(2)6 n−8+

c(2)7 n−9+

c(2)8 n−10+

c(2)9 n−11+

(40).

The cases m = 4,6,8,10 can be treated in a completely analogous way to what was done for m = 2. We omit the details, but remark that for m = 6,8,10 this method produces estimates which are stronger than (41) and (42). However, the latter will be enough for our purposes.

Finally, we deal with the case of even m ≥ 12. Again for ∈ {5,6,...,10}, the integral to consider is bounded by

∞

1/2 2−(2m+2 −1)Γ(2m + 2 − 1) Γ(m + )2

Γ(n − + 1) Γ(n + 2m + )

1 2n

1/2

|JnJn+m|r−m− dr ≤

. Identifying a binomial coeﬃcient, we notice the trivial bound

0

2−(2m+2 −1)Γ(2m + 2 − 1) Γ(m + )2 ≤

- 1

- 2


. It follows that

∞

Γ(n − + 1) Γ(n + 2m + )

- 1

- 2


1/2

|JnJn+m|r−m− dr ≤

n−1/2

. To handle the coeﬃcients |am+4(m)|, we recall Lemma 14. For even m ≥ 12, deﬁne c(m) :=

0

202 −1

2 π

- 1

- 2


1/2

(2m − 1)−1/22me−m

, a decreasing function of m for ﬁxed . We ﬁnally arrive at

2 −2 k=0 (20 − + 1 + k)

∞

Jn+mJn(JmJ000 − Jm000)r−1dr ≤ 105 16

0

6 16

66 162

1124 163

26828 164

840564 165

c(10m)n−10 and

c(5m)n−5+

c(6m)n−6+

c(7m)n−7+

c(8m)n−8+

c(9m)n−9+

∞

Jn+mJn(JmJ110 − Jm110)r−1dr ≤ 105 16

0

14 16

102 162

804 163

21978 164

703620 165

c(10m)n−10 . If m ≥ 12, then both of these expressions are bounded by 0.015n−0 1n−4, as claimed.

c(5m)n−5+

c(6m)n−6+

c(7m)n−7+

c(8m)n−8+

c(9m)n−9+

6. Part III. The core integrals The main integrals that are left to analyze,

- µ0 = µ0(m,n) :=

∞

0

Jn(r)Jn+m(r)Jm000(r)r−1dr;

- µ1 = µ1(m,n) :=


∞

Jn(r)Jn+m(r)Jm110(r)r−1dr,

0

decompose into the core integrals (7) by means of expanding Jm000 and Jm110 using the following elementary trigonometric facts:

8c4 = −cos(4r) + 4sin(2r) + 3, 8c3s = −sin(4r) − 2cos(2r), 8c2s2 = cos(4r) + 1, 8cs3 = sin(4r) − 2cos(2r), 8s4 = −cos(4r) − 4sin(2r) + 3.

These identities can be readily checked recalling the deﬁnitions c = cos(r − π/4) and s = sin(r − π/4), and noting again that cosωm = (−1)m/2c and sinωm = (−1)m/2s.

A simple parity check veriﬁes that the resulting core integrals with cos(2r) and sin(2r) satisfy the parity assumption of Lemma 2 relative to the powers of r, and so these terms yield zero contribution. It therefore suﬃces to consider the constant terms and the terms involving cos(4r) and sin(4r). The strategy will be to split the main integrals

- µ0 = µ(cos)0 + µ(sin)0 ;
- µ1 = µ(cos)1 + µ(sin)1 ,


according to cosine and sine contributions. More precisely, recall deﬁnitions (35) and (36) for Jm000 and Jm110, respectively. The ﬁrst factor in each of them, namely Jm − ρm, is given by identity (33). The right-hand side of this identity consists of two sums which come aﬀected by a coeﬃcient of c and s. These are at the source of what we denote by cosine and sine contributions, respectively. Working out the algebra, one is led to deﬁne

- (45) µ(cos)∗ :=

(−1)m/2 8

m 2 +1

k=0

(−1)ka2k(m)

∞

0

Jn(r)Jn+m(r) · (α0 + α2t2 + α4t4)+

+ (β0 + β2t2 + β4t4)cos(4r) + (γ1t + γ3t3 + γ5t5)sin(4r) r−2k−1dr for the sequence of coeﬃcients given by

- (46) (α0,α2,α4) =

(3,−150,65250), if ∗ = 0, (1,174,−33354), if ∗ = 1;

- (47) (β0,γ1,β2,γ3,β4,γ5) =


(−1,−6,66,1124,−26838,−840564), if ∗ = 0, (1,−10,30,444,−10602,−335340), if ∗ = 1,

and

- (48) µ(sin)∗ := −

(−1)m/2 8

m 2 +1

k=0

(−1)ka2k+1(m)

∞

0

Jn(r)Jn+m(r) · (α1t + α3t3 + α5t5)+

+ (β1t + β3t3 + β5t5)cos(4r) + (γ0 + γ2t2 + γ4t4)sin(4r) r−2k−2dr for the sequence of coeﬃcients given by

- (49) (α1,α3,α5) =

(6,−1092,826164), if ∗ = 0, (18,−1164,1071900), if ∗ = 1;

- (50) (γ0,β1,γ2,β3,γ4,β5) =

(−1,6,66,−1124,−26838,840564), if ∗ = 0, (1,10,30,−444,−10602,335340), if ∗ = 1.

For ∗ ∈ {0,1}, the goal is to obtain a set of estimates of the form

- (51) |µ(cos)∗ (m,n) − M∗(cos)(m,n)| ≤ E1(cos),∗ (m,n) + E2(cos),∗ (m,n);
- (52) |µ(sin)∗ (m,n) − M∗(sin)(m,n)| ≤ E1(sin),∗ (m,n) + E2(sin),∗ (m,n),


where M and E1 denote the main and error terms coming from the analysis of the constant terms, and E2 denotes the error term coming from the analysis of the terms of frequency 4r. We shall denote E1 and E2 by error terms of the ﬁrst and second kind, respectively.

6.1. Constant terms. Everything originating from the constant terms can be explicitly computed, one just needs to be careful about bookkeeping. As indicated before, we organize the terms into cosine and sine contributions.

6.1.1. Cosine contributions. We split the analysis in four cases: m = 0, m = 2, m = 4 and m ≥ 6. In each of these four cases we will identify, as announced, a main term M and an error term E1.

Let us start by handling the case m = 0. In this case, the contribution coming from the non-oscillatory term α0 + α2t2 + α4t4 in (45) can by computed exactly with the help of Lemmata 3 and 4, the result being a main term

- 1

- 2n


1 8

α2 162 − a2(0)α0

1 4(n − 1)n(n + 1)

1 8

M∗(cos)(0,n) :=

, and an error term of the ﬁrst kind

α0

+

a0(0)

1 8

E1(cos),∗ (0,n) :=

α4 164 − a2(0)

α2 162

a0(0)

3Γ(n − 2) 16Γ(n + 3)

1 8 − a2(0)

α4 164

+

5Γ(n − 3) 32Γ(n + 4)

.

Recalling (46), the main term can be computed as follows:

- (53) M∗(cos)(0,n) =

3

16n − 2048(n−511)n(n+1), if ∗ = 0,

1

16n + 2048(n−391)n(n+1), if ∗ = 1. To estimate the error term, we ﬁrst compute it as

E1(cos),∗ (0,n) =

101925Γ(n−2) 4194304Γ(n+3) − 1073741824Γ(1468125Γ(n−n+4)3) , if ∗ = 0, −4194304Γ(54729Γ(nn−+3)2) + 1073741824Γ(750465Γ(n−n3)+4), if ∗ = 1.

Using the triangle inequality together with the easily veriﬁed bounds 1 n5 ≤

Γ(n − 2) Γ(n + 3) ≤

1.02 n5

and

1 n7 ≤

Γ(n − 3) Γ(n + 4) ≤

1.04 n7

, valid for n ≥ 20, one arrives at

- (54) |E1(cos),∗ (0,n)| ≤

0.026n−0 1n−4, if ∗ = 0, 0.015n−0 1n−4, if ∗ = 1.

We move on to the case m = 2. Orthogonality kicks in the form of Lemma 4 to ensure that we only have one main term, which the same lemma computes as

M∗(cos)(2,n) :=

1 8 − a0(2)

α2 162

+ a2(2)α0

1 8n(n + 1)(n + 2)

. In other words,

- (55) M∗(cos)(2,n) =

195

4096n(n+1)(n+2), if ∗ = 0,

9

4096n(n+1)(n+2), if ∗ = 1. The error term of the ﬁrst kind is now given by

E1(cos),∗ (2,n) :=

1 8 − a0(2)

α4 164

+ a2(2)

α2 162 − a4(2)α0

Γ(n − 1) 8Γ(n + 4)

+

1 8

a2(2)

α4 164 − a4(2)

α2 162

15Γ(n − 2) 128Γ(n + 5)

+

1 8 − a4(2)

α4 164

7Γ(n − 3) 64Γ(n + 6)

. Proceeding as in the case m = 0, we see that this term obeys the following estimate:

- (56) |E1(cos),∗ (2,n)| ≤


0.039n−0 1n−4, if ∗ = 0, 0.012n−0 1n−4, if ∗ = 1.

In the case m = 4, we expand to one higher order. The reason for this will become apparent at the end of Section 8. We thus have exactly one main term

1 8

M∗(cos)(4,n) :=

α4 164 − a2(4)

α2 162

a0(4)

+ a4(4)α0

1 32n(n + 1)(n + 2)(n + 3)(n + 4)

,

and an error term of the ﬁrst kind

3Γ(n − 1) 64Γ(n + 6)

1 8 − a2(4)

α4 164

α2 162 − a6(4)α0

E1(cos),∗ (4,n) :=

+ a4(4)

7Γ(n − 2) 128Γ(n + 7)

α2 162

1 8

α4 164 − a6(4)

1 8 − a6(4)

α4 164

+

a4(4)

+

As before, we compute the main term

15Γ(n − 3) 256Γ(n + 8)

.

- (57) M∗(cos)(4,n) =

322425

- 1048576n(n+1)(n+2)(n+3)(n+4), if ∗ = 0, 7011

- 1048576n(n+1)(n+2)(n+3)(n+4), if ∗ = 1,


and verify the following bounds for the error term:

- (58) |E1(cos),∗ (4,n)| ≤

0.42n−0 1n−6, if ∗ = 0, 0.11n−0 1n−6, if ∗ = 1.

If m ≥ 6, orthogonality ensures that there is no main term. The error term of the ﬁrst kind is given by

E1(cos),∗ (m,n) :=

1 8

am−4(m)

α4 164 − am−2(m)

α2 162

+ am(m)α0

Γ(n) 2m+1Γ(n + m + 1)

+

1 8 − am−2(m)

α4 164

+ am(m)

α2 162 − am+2(m)α0

(m + 2)Γ(n − 1) 2m+3Γ(n + m + 2)

+

1 8

am(m)

α4 164 − am+2(m)

α2 162

(m + 3)(m + 4)Γ(n − 2) 2m+6Γ(n + m + 3)

+

1 8 − am+2(m)

α4 164

(m + 4)(m + 5)(m + 6)Γ(n − 3) 3 · 2m+8Γ(n + m + 4)

,

and this can be crudely bounded in the following way. If m ≥ 6, then

- (59) |E1(cos),∗ (m,n)| ≤ |E1(cos),∗ (6,n)|


for the given range of admissible m and n. It is easy to see that inequality (59) holds if m is large enough, essentially because each of the summands that constitute the left-hand side of that inequality is of order at most n−(m+1). For the remaining cases, one checks it directly. The upshot is a bound of the form

- (60) |E1(cos),∗ (m,n)| ≤

6.34n−0 3n−4, if ∗ = 0, 0.09n−0 3n−4, if ∗ = 1,

valid for every even m ≥ 6.

- 6.1.2. Sine contributions. We proceed similarly, again splitting the analysis into four cases. If m = 0, then the contribution coming from α1t + α3t3 + α5t5 amounts to a main term


M∗(sin)(0,n) := −

1 8

a1(0)

α1 16

1 4(n − 1)n(n + 1)

, and an error term of the ﬁrst kind

−E1(sin),∗ (0,n) :=

1 8

a1(0)

α3 163 − a3(0)

α1 16

3Γ(n − 2) 16Γ(n + 3)

+

1 8

a1(0)

α5 165 − a3(0)

α3 163

5Γ(n − 3) 32Γ(n + 4)

+

1 8

a3(0)

α5 165

35Γ(n − 4) 256Γ(n + 5)

. Recalling (49), we compute the main term as

- (61) M∗(sin)(0,n) =

3

2048(n−1)n(n+1), if ∗ = 0,

9

2048(n−1)n(n+1), if ∗ = 1. Arguing as in the last subsection, the error term can be seen to obey the following bounds:

- (62) |E1(sin),∗ (0,n)| ≤

0.0016n−0 1n−4, if ∗ = 0, 0.0030n−0 1n−4, if ∗ = 1.

If m = 2, there is a main term

- (63) M∗(sin)(2,n) :=


1 8

α1 16

1 8n(n + 1)(n + 2)

a1(2)

=

and an error term of the ﬁrst kind

45

- 4096n(n+1)(n+2), if ∗ = 0, 135

- 4096n(n+1)(n+2), if ∗ = 1,


Γ(n − 1) 8Γ(n + 4)

1 8 − a1(2)

α3 163

α1 16

−E1(sin),∗ (2,n) :=

+ a3(2)

1 8 − a1(2)

α5 165 − a3(2)

α3 163 − a5(2)

α1 16

+

7Γ(n − 3) 64Γ(n + 6)

1 8

α3 163

α5 165 − a5(2)

+

a3(2)

15Γ(n − 2) 128Γ(n + 5)

1 8 − a5(2)

α5 165

+

105Γ(n − 4) 1024Γ(n + 7)

which satisﬁes

- (64) |E1(sin),∗ (2,n)| ≤

0.0062n−0 1n−4, if ∗ = 0, 0.0031n−0 1n−4, if ∗ = 1.

If m = 4, we again expand to one higher order. There is a main term

M∗(sin)(4,n) := −

1 8

a1(4)

α3 163 − a3(4)

α1 16

1 32n(n + 1)(n + 2)(n + 3)(n + 4) and an error term of the ﬁrst kind

−E1(sin),∗ (4,n) :=

1 8

a1(4)

α5 165 − a3(4)

α3 163

+ a5(4)

α1 16

3Γ(n − 1) 64Γ(n + 6)

+

1 8 − a3(4)

α5 165

+ a5(4)

α3 163 − a7(4)

α1 16

7Γ(n − 2) 128Γ(n + 7)

+

1 8

a5(4)

α5 165 − a7(4)

α3 163

15Γ(n − 3) 256Γ(n + 8)

+

1 8 − a7(4)

α5 165

495Γ(n − 4) 8192Γ(n + 9)

. The main term satisﬁes

- (65) M∗(sin)(4,n) :=

76167

- 1048576n(n+1)(n+2)(n+3)(n+4), if ∗ = 0, 211869

- 1048576n(n+1)(n+2)(n+3)(n+4), if ∗ = 1,


and the error term can be bounded as follows:

- (66) |E1(sin),∗ (4,n)| ≤


0.086n−0 1n−6, if ∗ = 0, 0.063n−0 1n−6, if ∗ = 1.

Finally, if m ≥ 6, there is no main term, and the error term of the ﬁrst kind is given by

1 8 − am−5(m)

α5 165

α3 163 − am−1(m)

α1 16

Γ(n) 2m+1Γ(n + m + 1)

−E1(sin),∗ (m,n) :=

+ am−3(m)

(m + 2)Γ(n − 1) 2m+3Γ(n + m + 2)

α5 165 − am−1(m)

1 8

α3 163

α1 16

am−3(m)

+

+ am+1(m)

(m + 3)(m + 4)Γ(n − 2) 2m+6Γ(n + m + 3)

1 8 − am−1(m)

α5 165

α3 163 − am+3(m)

α1 16

+

+ am+1(m)

(m + 4)(m + 5)(m + 6)Γ(n − 3) 3 · 2m+8Γ(n + m + 4)

1 8

α3 163

α5 165 − am+3(m)

+

am+1(m)

(m + 5)(m + 6)(m + 7)(m + 8)Γ(n − 4) 3 · 2m+12Γ(n + m + 5)

1 8 − am+3(m)

α5 165

. Again the monotonicity formula

+

|E1(sin),∗ (m,n)| ≤ |E1(sin),∗ (6,n)| holds for every even m ≥ 6, and this implies a bound of the form

- (67) |E1(sin),∗ (m,n)| ≤

1.49n−0 3n−4, if ∗ = 0, 4.08n−0 3n−4, if ∗ = 1,

which is valid in that range of m. 6.2. Frequency 4r terms. To handle the terms of frequency 4r, we make repeated use of the following result:

Proposition 15. Let n,m ∈ N be such that n ≥ n0 = 20 and m even with 0 ≤ m ≤ n. Let α ∈ {1,3,5} and β ∈ {2,4,6}. Then each of the following quantities is less than n−10.35n:

- (i)

m 2 +1

k=0

∞

0

Jn(r)Jn+m(r)r−2ka2k(m)cos(4r)r−α dr ,

- (ii)

m 2 +1

k=0

∞

0

Jn(r)Jn+m(r)r−2ka2k(m)sin(4r)r−β dr ,

- (iii)

m 2 +1

k=0

∞

0

Jn(r)Jn+m(r)r−2k−1a2k+1(m)cos(4r)r−β dr ,

- (iv)


m 2 +1

k=0

∞

0

Jn(r)Jn+m(r)r−2k−1a2k+1(m)sin(4r)r−α dr .

Proof. All estimates can be proved in a very similar way. We focus on the tightest case, that of (i) with α = 1, and brieﬂy comment on the other cases at the end of the proof. Using the deﬁnition of the coeﬃcients aj(n) and Lemma 5, together with the convexity estimate from Corollary 12, we obtain

m 2 +1

k=0

|a2k(m)|

∞

0

Jn(r)Jn+m(r)r−2k cos(4r)r−1 dr ≤

≤

m 2 +1

k=0

Γ(m + 2k + 1/2) Γ(m − 2k + 1/2)22kΓ(2k + 1)

22k 42n+m

Γ(2n + m − 2k) Γ(n + 1)Γ(n + m + 1)

≤

m 2 +1

k=0

Γ(m + 2k + 1/2) Γ(m − 2k + 1/2)Γ(4k + 1)

Γ(2n + m) Γ(n + 1)Γ(n + m + 1)

- (68) 4−2n−m.


The second fraction in this expression resembles a binomial coeﬃcient and does not depend on k. It can be estimated in the following way: using Lemma 13 with x = n + m/2 and d = m/2, we see that

Γ(2n + m) Γ(n + 1)Γ(n + m + 1)

Γ(2n + m) Γ(n)Γ(n + m) ≤

1 n(n + m)

=

e1/24 2√π

(m/2)2 n+m/2

1 n(n + m)

(n + m/2)1/222n+me−

e1/24 2√π

1 n(n + m)1/2

(69) 22n+m.

≤

To estimate the sum of the ﬁrst fractions in (68), we proceed as follows. For k = m/2 + 1, we simply have that

Γ(m + 2k + 1/2) Γ(m − 2k + 1/2)Γ(4k + 1)

Γ(2m + 5/2) Γ(−3/2)Γ(2m + 5) ≤

=

1 (2m + 4)(2m + 3)

1 Γ(−3/2)

Γ(2m + 3) Γ(2m + 5)

- 3

- 4√π


≤

=

.

On the other hand, as long as1 0 ≤ k ≤ m/2, we can use Corollary 12 followed by Lemma 13 with x = m/2 + k + 1 and d = |3k − m/2| to conclude that:

m 2

Γ(m + 2k + 1/2) Γ(m − 2k + 1/2)Γ(4k + 1) ≤

k=0

=

≤

m 2

Γ(m + 2k + 1) Γ(m − 2k + 1)Γ(4k + 1)

k=0

m 2

Γ(m + 2k + 2) Γ(m − 2k + 1)Γ(4k + 1)

1 m + 2k + 1

k=0

m 2

2e1/24 √π

(m/2 + k + 1)1/2 m + 2k + 1

(3k−m/2)2

4ke−

2m

m/2+k+1 .

k=0

1/2

For 0 ≤ k ≤ m/2, it is easy to check that the quantity (m/2+k+1)

m+2k+1 is decreasing in k. Moreover, for k = 0, we have that

(m/2 + 1)1/2

m + 1 ≤ (m + 1)−1/2. Using this, we are left to estimate the Gaussian sum

1This does not work for k = m/2 + 1 because the assumptions of Corollary 12 are not met and the conclusion fails.

m 2

(3k−m/2)2

4ke−

m/2+k+1 . We start with the trivial estimate

Υm :=

k=0

m 2

(3k−m/2)2

4ke−

Υm ≤

m+1 .

k=0

Changing variables of summation 3 = 3k − m/2, we see that

(3 )2

4 e−

Υm ≤ 2m/3

m+1 ,

∈L

where L is the new summation set, given by L := −

m 6

m 6

m 3 ⊂

1 3

Z.

,−

+ 1,...,

We estimate this sum by the product of the largest term and the number of terms #L = m/2 + 1. To detect the largest term, deﬁne the function

(3x)2

ϕm(x) := 4xe−

m+1 . The unique solution x0 ∈ [−m6 , m3 ] to the stationary condition ϕ m(x0) = 0 is given by

log 2 9

x0 =

(m + 1), for which we have

ϕm(x0) = Am+1, where

log 2

log 2

3 )2 ≤ 1.06. Since ϕm( ) ≤ ϕm(x0) for every ∈ L, we thus have that

9 e−(

A := 4

m 2

+ 1 2m/3Am+1. It follows that

Υm ≤

m 2 +1

Γ(m + 2k + 1/2)

- (70) Γ(m − 2k + 1/2)Γ(4k + 1) ≤


k=0

2e1/24 √π

- 3

- 4√π


1 (2m + 4)(2m + 3) ≤

m 2

(m + 1)−1/22m

+ 1 2m/3Am+1 +

≤

2e1/24 √π

103 100

m 2

(m + 1)−1/22m

+ 1 2m/3Am+1,

where the last inequality holds since the second summand on the second line amounts to at most 1003 of the ﬁrst summand. Finally, estimates (69) and (70) together imply that

- m 2 +1

k=0

|a2k(m)|

∞

0

Jn(r)Jn+m(r)r−2k cos(4r)r−1 dr

≤

m 2 +1

k=0

Γ(m + 2k + 1/2) Γ(m − 2k + 1/2)Γ(4k + 1)

Γ(2n + m) Γ(n + 1)Γ(n + m + 1)

4−2n−m

≤

103 100

2e1/24 √π

(m + 1)−1/22m

m 2

+ 1 2m/3Am+1

e1/24 2√π

1 n(n + m)1/2

22n+m 4−2n−m ≤ n−12m/3Am2−2n.

Since m ≤ n, we ﬁnally get the desired estimate:

≤ n−12n/3An2−2n = n−1

21/3A 4

n

≤ n−10.35n.

This completes the estimate of sum (i) with α = 1. For the other cases, letting k ∈ {0,1,...,m/2 + 1} and 1 ≤ j ≤ 7, one just checks that the bounds given by Lemma 5, namely

∞

0

Jn(r)Jn+m(r)r−2k−je4ir dr ≤

22k+j−1 42n+m

(2n + m − 2k − j)! n!(n + m)!

,

are decreasing in j as long as the conditions of the statement are met. Remark. We will need the following observation for the purpose of our applications. For

- n ≥ 20, we have that 0.35n/2 ≤ n−3, and so the bound given by Proposition 15 can be further estimated as follows:


n−10.35n = n−10.35n/20.35n/2 ≤ 0.35n0/2n−4 ≤ 0.6n0n−4,

provided n ≥ n0 = 20. Alternatively, still for n ≥ 20, we have that 0.35τn ≤ n−5 if τ > 0.72. Using this bound instead, we see that

n−10.35n = n−10.35τn0.35(1−τ)n ≤ 0.35(1−τ)n0n−6 ≤ 0.75n0n−6. All in all, we have the following upper bound for the quantities considered in Proposition 15:

min{0.6n0,0.75n0n−2} n−4.

This distinction will play a role to ensure good bounds for the m = 4 terms which were expanded to one higher order in the last subsection.

We are ﬁnally ready to estimate the contribution coming from the oscillatory terms (β0 + β2t2 + β4t4)cos(4r) and (γ1t + γ3t3 + γ5t5)sin(4r) in expression (45), and similarly

in (48). Appealing to Proposition 15 and the remark following it, we see that we can take the following for errors of the second kind:

1 8 |β0| + |γ1|

+ |β2| 162

+ |γ3| 163

+ |β4| 164

+ |γ5| 165

E2(cos),∗ (m,n) :=

16

θn0n−t;

+ |γ2| 162

+ |β3| 163

+ |γ4| 164

+ |β5| 165

1 8 |γ0| + |β1|

E2(sin),∗ (m,n) :=

θn0n−t,

16

where (θ,t) = (0.75,6) if m = 4 and (θ,t) = (0.6,4) if m = 4. Plugging the values of β,γ from (47) and (50), we obtain the estimates

- (71) |E2(cos),∗ (4,n)|,|E2(sin),∗ (4,n)| ≤

0.39 · 0.75n0n−6, if ∗ = 0, 0.30 · 0.75n0n−6, if ∗ = 1,

- and, if m = 4,


- (72) |E2(cos),∗ (m,n)|,|E2(sin),∗ (m,n)| ≤


0.39 · 0.6n0n−4, if ∗ = 0, 0.30 · 0.6n0n−4, if ∗ = 1.

7. Putting it all together

In the last section we analyzed the core integrals, which were decomposed into main terms and error terms. We derived several estimates which are recalled below in each case. These are used together with Estimates A and B to yield appropriate bounds, which are then evaluated at n0 = 20:

- (i) If m = 0, then we use the knowledge about the main terms coming from (53) and

(61), the estimates for the error terms of the ﬁrst kind contained in (54) and (62), and the bounds for the error terms of the second kind from (72), to conclude that

∞

0

Jn2(r)J40(r)r−1dr −

3 16

1 n

+

3 128

1 (n − 1)n(n + 1)

≤ (0.022 + 0.026 + 0.0016)n−0 1 + 0.74n−0 5/2 + 0.78 · 0.6n0 n−4 ≤ 0.0030n−4, and that

∞

0

Jn2(r)J21(r)J20(r)r−1dr −

1 16

1 n −

3 128

1 (n − 1)n(n + 1)

≤ (0.023 + 0.015 + 0.0030)n−0 1 + 1.12n−0 5/2 + 0.60 · 0.6n0 n−4 ≤ 0.0028n−4.

- (ii) If m = 2, then we use the knowledge about the main terms coming from (55) and


(63), the estimates for the error terms of the ﬁrst kind contained in (56) and (64),

### and the bounds for the error terms of the second kind from (72), to conclude that

∞

15 256

1 n(n + 1)(n + 2) ≤ (0.039 + 0.0062)n−0 1 + 0.74n−0 5/2 + 0.162n−0 3 + 0.78 · 0.6n0 n−4 ≤ 0.0028n−4, and that

Jn+2(r)Jn(r)J2(r)J30(r)r−1dr −

0

∞

9 256

1 n(n + 1)(n + 2)

Jn+2(r)Jn(r)J2(r)J21(r)J0(r)r−1dr −

0

≤ (0.012 + 0.0031)n−0 1 + 1.12n−0 5/2 + 0.166n−0 3 + 0.60 · 0.6n0 n−4 ≤ 0.0015n−4.

- (iii) If m = 4, then we use the knowledge about the main terms coming from (57) and

(65), the estimates for the error terms of the ﬁrst kind contained in (58) and (66), and the bounds for the error terms of the second kind from (71), to conclude that

∞

0

Jn+4(r)Jn(r)J4(r)J30(r)r−1dr −

1557 4096

1 n(n + 1)(n + 2)(n + 3)(n + 4)

≤ 0.74n−0 1/2 + (0.42 + 0.086)n−0 1 + 2.823n−0 3 + 0.78 · 0.75n0 n−6 ≤ 0.197n−6, and that

∞

0

Jn+4(r)Jn(r)J4(r)J21(r)J0(r)r−1dr −

855 4096

1 n(n + 1)(n + 2)(n + 3)(n + 4)

≤ 1.12n−0 1/2 + (0.11 + 0.063)n−0 1 + 2.885n−0 3 + 0.60 · 0.75n0 n−4 ≤ 0.264n−6.

- (iv) If m ≥ 6 is even, then there are no main terms, and we use the estimates for the error terms of the ﬁrst kind contained in (60) and (67), and the bounds for the error terms of the second kind from (72), to conclude that


∞

Jn+m(r)Jn(r)Jm(r)J30(r)r−1dr

0

≤ 0.015n−0 1 + 0.74n0−5/2 + (6.34 + 1.49)n−0 3 + 0.78 · 0.6n0 n−4 ≤ 0.0022n−4, and that

∞

Jn+m(r)Jn(r)Jm(r)J21(r)J0(r)r−1dr

0

≤ 0.015n−0 1 + 1.12n0−5/2 + (0.09 + 4.08)n−0 3 + 0.60 · 0.6n0 n−4 ≤ 0.0020n−4.

To get the constants promised by Theorem 1, one just multiplies the far right-hand sides of each inequality by the normalizing factor π42 < 21. This concludes the proof of Theorem 1 for n ≥ 20.

8. Numerical estimates for n < 20

In this section, we numerically evaluate the integrals I0 and I1 deﬁned in (5) and (6), respectively, for 2 ≤ n ≤ 19 and even 0 ≤ m ≤ n. We split the integrals into

∞

R

Ij = Ij,low + Ij,high =

...dr +

...dr .

0

R

We use a quadrature rule for the ﬁrst integral and estimate the second integral by analytic methods. We aim at an absolute error of at most 0.9 × 10−8 for I0 and I1.

The high integral would be entirely negligible at our desired accuracy for the threshold (say) R = 1010, but this would put unnecessarily much computing time on the low integrals. We choose R = 63000 and estimate the high integrals by a more careful analysis of the asymptotic expansion. To bring down the computing time for the low integrals, we use a high degree Newton-Coates quadrature rule.

We ﬁrst discuss the high integrals and begin with I0,high. Since R is large compared to (n + m)2, we take advantage of the asymptotic information in Corollary 7. Splitting each Bessel function into main term plus error, and applying the distributive law, yields one main integral of the form

3

∞

2 πr

cos(ωn+m)cos(ωn)cos(ωm)cos3(ω0)rdr plus 26 − 1 error terms.

I0,main,high =

R

If n is even, since m is even as well, an even number of the integers n,m,n + m is congruent two modulo four, and we obtain, with the periodicity cos(ωn) = −cos(ωn+2),

3

∞

2 πr

cos6(ω0)rdr ,

I0,main,high = I0,main,high,even :=

R

a term which is in fact independent of the particular even n and m. If n is odd, then we obtain similarly

3

∞

2 πr

cos2(ω1)cos4(ω0)rdr . Likewise, if n is even, we have

I0,main,high = I0,main,high,odd :=

R

3

∞

2 πr

cos2(ω1)cos4(ω0)rdr ,

I1,main,high = I1,main,high,even :=

R

- and, if n is odd,


3

∞

2 πr

cos4(ω1)cos2(ω0)rdr .

I1,main,high = I1,main,high,odd :=

R

These integrals have closed-form expressions in terms of trigonometric and trigonometric integral functions. Mathematica calculates these expression and evaluates them with prescribed accuracy, resulting in

|I0,main,high,even − 1.2798 × 10−6| < 10−10,

|I0,main,high,odd − 0.2560 × 10−6| < 10−10, |I1,main,high − 0.2560 × 10−6| < 10−10, where the distinction between even and odd n is not visible at the prescribed accuracy in the case of I1,main,high. A sample Mathematica code used to evaluate I0,main,high,even is the following:

N[Integrate[(2/Pi)3 ∗ Cos[r − Pi/4]6 ∗ r(−2),{r,63000,Inﬁnity}],20] .

We now estimate the 26 − 1 error terms of Ii,high − Ii,main,high. Of these error terms, six of them consist of an integral of a product of ﬁve main terms of Corollary 7 and one error term of Corollary 7. To estimate these six terms, we use the ﬁner information from Corollary 8 for the error term of Corollary 7.

The second main term of Corollary 8 leads to integrals of the type −

3

∞

4((n + m)2 − 1) 8

2 πr

sin(ωn+m)cos(ωn)cos(ωm)cos3(ω0)dr

R

and similar terms with a diﬀerent cosine factor replaced by a sine factor and corresponding prefactor. The product of the six trigonometric functions is odd about the point π/4. Thus this product integrates to 0 over each period. On the period [R +2πk,R +2π(k +1)) with any nonnegative integer k, we may thus replace the weight r−3 by the diﬀerence between r−3 and its mean over that interval. This diﬀerence is bounded by 6r−4π on that interval, hence we may estimate the sum of terms arising from the second main term of Corollary 8 by

3

∞

2 π

r−4dr ≤ 2.1 × 10−11 .

3π((37)2 + (19)2 + (18)2 + 3)

R

The sum of the six terms arising from the error terms of Corollary 8 can be further estimated by

3

∞

2 π

1 4

r−4dr ≤ 1.64 × 10−9 .

((37)4 + (19)4 + (18)4 + 3)

R

Next come ﬁfteen terms of the original 26 − 1 error terms which have four main terms and two error terms of Corollary 7. These beneﬁt from an integration of the negative fourth power of r, and can be estimated by

3

∞

2 π

r−4dr ≤ 3.32 × 10−9 .

[372 × 192 + 372 × 182 + 192 × 184 + 12 × 362]

R

The remaining 26−1−6−15 = 42 terms beneﬁt from an integration of at least the negative ﬁfth power of r, and are estimated even more crudely as

3

∞

2 π

r−5dr ≤ 4.5 × 10−10 . Adding all these error contributions yields

42 × [372 × 192 × 182]

R

|Ii,high − Ii,main,high| ≤ 5.5 × 10−9 .

### We next turn to the low integrals. We recall the Newton-Coates rule

6

f(x)dx = F(f) with

0

F(f) = 140−1(41f(0) + 216f(1) + 27f(2) + 272f(3) + 27f(4) + 216f(5) + 41f(6)),

which is valid for all real polynomials f up to degree 7. For any eight times continuously diﬀerentiable function f on [0,6], we have that

6

64 5

|f(8)(ξ)| 8!

f(x)dx − F(f) ≤

- (73)


sup

.

ξ∈[0,1]

0

A well-known argument shows that polynomials of degree eight extremize this inequality. It is then a straightforward matter of checking that polynomials of degree eight, whose

eighth derivative is constant, realize the optimal constant 654 promised by (73).

Now let Fa,w be the suitably scaled and translated Newton-Coates formula which integrates polynomials of degree 7 on the interval [a,a + 6w] exactly. Then, by rescaling,

a+6w

|f(8)(ξ)| 8!

64 5

f(x)dx − Fa,w(f) ≤ w9

sup

.

ξ∈[a,a+6w]

a

Now assume that the length of the interval [a,b] is an integer multiple of 6w, say 6wN. Then partitioning this interval into N intervals of length 6w and applying the NewtonCoates formula on each interval yields

N−1

b

|f(8)(ξ)| 8!

63 5

Fa+kw,w(f) ≤ (b − a)w8

f(x)dx −

sup

.

ξ∈[a,b]

a

k=0

We cut the interval [0,R] into [0,S] ∪ [S,R] with S = 3600. On the interval [0,S], we estimate the eighth derivative of the functions

f(r) = Jn+m(r)Jn(r)Jm(r)J03(r)r and

f(r) = Jn+m(r)Jn(r)Jm(r)J12(r)J0(r)r using the Cauchy integral formula for the circle of radius 1 about r together with the trivial bound (10) to obtain the estimate

|f(8)(r)| ≤ 8!e6(S + 1) .

Approximating the integral over [0,S] by the above summation rule with width w = 0.003 gives the error bound

63 5

e6(S + 1) ≤ 1.49 × 10−9 .

S(.003)8

On the interval [S,R], we estimate the eighth derivative of f again by the Cauchy integral

formula with circles of radius one. We use the estimate from Corollary 7 for Jn+ to obtain, for (z) > S − 1 and (z) ≤ 1,

2 π|z|

1/2

|Jn+(z)| ≤

(1 + n2/S)cosh( (z)) × 1.01 ,

and similarly for Jn−. Estimating the product of the various terms analogous to (1+n2/S)× 1.01 by 3, we then obtain

2 π(S − 1)

3

|f(8)(r)| ≤ 3 × 8! ×

(cosh(1))6(R + 1) .

Approximating the integral over [S,R] by the above summation rule with width w = 0.05 gives the error bound

63 5

2 π(S − 1)

3

(cosh(1))6(R + 1) ≤ 1.42 × 10−9 . Collecting error terms, we obtain

3 × (R − S)w8

|I0 − 1.2798 × 10−6 − F[0,S] − F[S,R]| ≤ 0.85 × 10−8 if n is even, and

- |I0 − 0.256 × 10−6 − F[0,S] − F[S,R]| ≤ 0.85 × 10−8 if n is odd, and
- |I1 − 0.256 × 10−6 − F[0,S] − F[S,R]| ≤ 0.85 × 10−8


for any n, where F[0,S] and F[S,R] are the quadrature formulae described above for the corresponding integrals.

We evaluate F[0,S] and F[S,R] using Mathematica. Products of Bessel functions at the grid points are computed with 20-digit precision, and the corresponding rounding errors for F[0,S]+F[S,R] can be safely estimated by 0.05×10−8. As an example, in the case n = 14 and m = 4 for I0, we use the following code to compute F[0,S]:

BJ[x ] := N[BesselJ[18,x] ∗ BesselJ[14,x] ∗ BesselJ[4,x] ∗ BesselJ[0,x]3 ∗ x,20] BJSA := 41 ∗ BJ[0] + 82 ∗ Sum[BJ[x],{x,18/1000,3599982/1000,18/1000}] + 216 ∗ Sum[BJ[x],{x,3/1000,3599985/1000,18/1000}] + 27 ∗ Sum[BJ[x],{x,6/1000,3599988/1000,18/1000}] + 272 ∗ Sum[BJ[x],{x,9/1000,3599991/1000,18/1000}] + 27 ∗ Sum[BJ[x],{x,12/1000,3599994/1000,18/1000}] + 216 ∗ Sum[BJ[x],{x,15/1000,3599997/1000,18/1000}] + 41 ∗ BJ[3600] (BJSA ∗ .018)/840

For m = 0 and even n, Table 1 lists upper bounds for the quantities 1 n −

- 3

- 4π2


3 32π2

1

(n − 1)n(n + 1) − 1.2798 × 10−6 − F[0,S] − F[S,R] + 0.9 × 10−8 100n4 on top of each entry, and for

1 4π2

1 n

3 32π2

1 (n − 1)n(n + 1) − 0.256 × 10−6 − F[0,S] − F[S,R] + 0.9 × 10−8 100n4

+

at the bottom of each entry, with the appropriate quadrature formulae F[0,S] and F[S,R] described above. For m = 0 and odd n, it similarly lists upper bounds for

1 n −

1

3 4π2

3 32π2

(n − 1)n(n + 1) − 0.256 × 10−6 − F[0,S] − F[S,R] + 0.9 × 10−8 100n4 on top, and for

1 n

3 32π2

1 (n − 1)n(n + 1) − 0.256 × 10−6 − F[0,S] − F[S,R] + 0.9 × 10−8 100n4

1 4π2

+

at the bottom. Thus each entry on the ﬁrst column (m = 0) of Table 1, divided by 100, provides a constant c for which the estimate of Theorem 1 holds for the corresponding n with c in place of 0.002 or 0.0015. The entries of Table 1 for m > 0 are analogous.

The poorer constants near n = 19 are artiﬁcial and due to the chosen numerical accuracy 0.9×10−8; note that, for this value of n, the quantity 0.9×10−8n4 is already close to 0.0014. The very good constants at m = 4 are due to the extra term in the expansion that has been elaborated in that case.

|n \ m| |0<br><br>|2<br><br>|4|6<br><br>|8<br><br>|10<br><br>|12|14<br><br>|16|18|
|---|---|---|---|---|---|---|---|---|---|---|---|
|2| |.85 .64|.14 .03<br><br>| | | | | | | | |
|3<br><br>| |.44 .21<br><br>|.16 .05| | | | | | | | |
|4| |.33 .16<br><br>|.16 .04<br><br>|.03 .01| | | | | | | |
|5| |.26 .12<br><br>|.15 .04|.02 .01<br><br>| | | | | | | |
|6| |.22 .10|.15 .04<br><br>|.02 .01|.11 .06<br><br>| | | | | | |
|7| |.19 .09|.14 .04<br><br>|.02 .01|.09 .05<br><br>| | | | | | |
|8| |.17 .08<br><br>|.13 .04<br><br>|.02 .01|.08 .05<br><br>|.02 .02| | | | | |
|9| |.15 .07|.13 .04<br><br>|.02 .01<br><br>|.07 .05|.02 .02<br><br>| | | | | |
|10| |.14 .07<br><br>|.13 .04|.02 .02<br><br>|.07 .04<br><br>|.02 .02|.02 .02<br><br>| | | | |
|11| |.13 .07<br><br>|.13 .04|.02 .02<br><br>|.07 .04|.03 .02<br><br>|.02 .02| | | | |
|12| |.13 .07|.13 .05<br><br>|.03 .03<br><br>|.07 .05|.03 .03<br><br>|.03 .03<br><br>|.03 .03| | | |
|13| |.13 .08<br><br>|.13 .05<br><br>|.04 .03|.07 .05<br><br>|.04 .04<br><br>|.03 .03<br><br>|.03 .03| | | |
|14| |.13 .08<br><br>|.13 .06|.05 .04<br><br>|.07 .06|.05 .05<br><br>|.04 .04|.04 .04<br><br>|.04 .04<br><br>| | |
|15| |.14 .09<br><br>|.14 .07|.06 .06<br><br>|.08 .07|.06 .06<br><br>|.06 .06<br><br>|.06 .06<br><br>|.06 .06<br><br>| | |
|16<br><br>| |.15 .10|.15 .09<br><br>|.07 .07<br><br>|.09 .08|.07 .07<br><br>|.07 .07<br><br>|.07 .07|.07 .07<br><br>|.07 .07| |
|17| |.16 .12<br><br>|.17 .10<br><br>|.09 .09<br><br>|.11 .10|.09 .09<br><br>|.09 .09<br><br>|.09 .09|.09 .09<br><br>|.09 .09<br><br>| |
|18| |.18 .14<br><br>|.19 .13|.11 .11<br><br>|.13 .12<br><br>|.11 .11|.11 .11<br><br>|.11 .11<br><br>|.11 .11|.11 .11<br><br>|.11 .11|
|19| |.20 .16|.20 .15<br><br>|.14 .14<br><br>|.15 .14|.14 .14<br><br>|.14 .14<br><br>|.14 .14|.14 .14<br><br>|.14 .14<br><br>|.14 .14|


### Table 1

### References

- [1] E. Carneiro, D. Foschi, D. Oliveira e Silva and C. Thiele, A sharp trilinear inequality related to Fourier restriction on the circle. Preprint, arXiv:1509.06674.
- [2] W. Kapteyn, A deﬁnite integral containing Bessel’s functions. Proc. Section of Sci., K. Akad. van Wet. te Amsterdam 4 (1902), 102–103.
- [3] L. J. Landau, Bessel functions: monotonicity and bounds. J. London Math. Soc. (2) 61 (2000), no. 1, 197–215.
- [4] H. Robbins, A remark on Stirling’s formula. Amer. Math. Monthly 62, (1955), 26–29.
- [5] E. M. Stein, Harmonic Analysis: Real-Variable Methods, Orthogonality, and Oscillatory Integrals. Princeton Univ. Press, Princeton, NJ, 1993.
- [6] P. Tomas, A restriction theorem for the Fourier transform. Bull. Amer. Math. Soc. 81 (1975), no. 2, 477–478.
- [7] G. N. Watson, A Treatise on the Theory of Bessel Functions. Second Edition. Cambridge University Press, Cambridge, 1966.


Hausdorff Center for Mathematics, Universitat¨ Bonn, 53115 Bonn, Germany. E-mail address: dosilva@math.uni-bonn.de E-mail address: thiele@math.uni-bonn.de

