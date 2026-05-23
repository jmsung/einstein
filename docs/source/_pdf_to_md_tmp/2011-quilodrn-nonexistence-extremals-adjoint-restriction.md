arXiv:1108.6324v4[math.CA]28Dec2017

NONEXISTENCE OF EXTREMALS FOR THE ADJOINT RESTRICTION INEQUALITY ON THE HYPERBOLOID

RENE´ QUILODRAN´

Abstract. We study the problem of existence of extremizers for the L2 to Lp adjoint Fourier restriction inequalities for the hyperboloid in dimensions 3 and 4 in the case p is an even integer. We use the method developed by Foschi in [5] to show that extremizers do not exist.

1. Introduction

![image 1](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile1.png>)

For d ≥ 1, let d denote the hyperboloid in d+1, d = {(y, 1 + |y|2) : y ∈ d}, equipped with the measure

deﬁned by duality as

![image 2](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile2.png>)

σ(y, y′) = δ y′ − 1 + |y|2

dydy′ 1 + |y|2

![image 3](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile3.png>)

![image 4](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile4.png>)

dy 1 + |y|2

![image 5](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile5.png>)

g(y, y′)dσ(y, y′) =

g y, 1 + |y|2

,

![image 6](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile6.png>)

![image 7](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile7.png>)

d

d

for all g ∈ C0( d+1).

A function f : d → can be identiﬁed with a function from d to , and in what follows, we do so. We denote the Lp( d, σ)-norm of a function f by

f Lp( d), f Lp(σ) or f p. The extension or adjoint Fourier restriction operator for d is given by

√

![image 8](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile8.png>)

1+|y|2f(y)(1 + |y|2)−1/2dy, (1.1)

eix·yeit

Tf(x, t) =

d

where (x, t) ∈ d × and f ∈ S( d). With the Fourier transform in d+1 deﬁned to be gˆ(ξ) =

e−ix·ξg(x)dx, we see that Tf(x, t) = fσ(−x, −t).

d+1

It is known [13] that there exists Cd,p < ∞ such that for all f ∈ L2( d), the estimate for Tf

Tf Lp( d+1) ≤ Cd,p f L2( d) (1.2) holds provided that

2(d + 2) d ≤p ≤

2(d + 1) d − 1

if d > 1, 6 ≤p < ∞, if d = 1.

![image 9](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile9.png>)

![image 10](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile10.png>)

(1.3)

![image 11](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile11.png>)

Research supported in part by NSF grant DMS-0901569.

1

For p satisfying (1.3), we denote by Hd,p the best constant in (1.2), Hd,p = sup

Tf Lp( d+1) f L2( d)

. We also consider the two-sheeted hyperboloid

![image 12](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile12.png>)

0 =f∈L2( d)

¯ d = {(y, y′) ∈ d × : y′2 = 1 + |y|2}. and endow it with the measure σ¯ = σ+ + σ−, where

dydy′ 1 + |y|2

![image 13](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile13.png>)

σ+(y, y′) = σ(y, y′) = δ y′ − 1 + |y|2

,

![image 14](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile14.png>)

![image 15](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile15.png>)

dydy′ 1 + |y|2

![image 16](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile16.png>)

σ−(y, y′) = δ y′ + 1 + |y|2

.

![image 17](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile17.png>)

![image 18](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile18.png>)

The corresponding adjoint Fourier restriction operator is Tf¯ = fσ+ + fσ−. If (d, p) satisﬁes (1.3), then

Tf ¯ Lp( d+1) ≤ H¯ d,p f L2(¯d), (1.4) where

Tf ¯ Lp( d+1) f L2(¯d)

H¯ d,p = sup

(1.5)

![image 19](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile19.png>)

0 =f∈L2( ¯ d)

is ﬁnite. Deﬁnition 1.1. An extremizing sequence for inequality (1.2) is a sequence {fn}n∈ of functions in L2( d) satisfying fn L2( d) ≤ 1 such that

Tfn Lp( d+1) → Hd,p as n → ∞.

An extremizer for inequality (1.2) is a function f = 0 which satisﬁes Tf Lp( d+1) = Hd,p f L2( d). These terms are deﬁned analogously for inequality (1.4).

We are interested in the following pairs (2, 4), (2, 6) and (3, 4) of (d, p), which are the only cases for d > 1 where p is an even integer. The main result of this paper is the following theorem.

Theorem 1.2. The values of the best constants are H2,4 = 23/4π, H2,6 = (2π)5/6 and H3,4 = (2π)5/4. Moreover, extremizers for inequality (1.2) do not exist in each of the three cases of (d, p).

The best constants for the two-sheeted hyperboloid are H¯ 2,4 = (3/2)1/4H2,4, and H¯ 3,4 = (3/2)1/4H3,4, and extremizers for inequality (1.4) do not exist.

When (d, p) = (2, 6) we only prove an inequality for H¯ 2,6 as recorded in the next remark. Remark 1.3. In Proposition 7.5 we show that for each f ∈ L2(¯ 2), f = 0

25 4

Tf ¯ 6L6( 3) f −L6

H62,6,

2(¯2) <

![image 20](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile20.png>)

and therefore H¯ 2,6 ≤ (5/2)1/3H2,6. Moreover, a reﬁnement of the argument shows that there is a strict inequality H¯ 2,6 < (5/2)1/3H2,6.

We normalize the Fourier transform in d as gˆ(ξ) = normalization, the convolution and L2( d) norm satisfy

- d
- e−ix·ξg(x)dx. With this


f ∗ g = fˆgˆ and f ˆ L2( d) = (2π)d/2 f L2( d), respectively. If p = 2k is an even integer, we can write (1.2) in “convolution form”

Tf kL2k( d+1) = (Tf)k L2( d+1) = ( fσ)k L2( d+1) = (fσ ∗ · · · ∗ fσ)ˆ L2( d+1)

= (2π)(d+1)/2 fσ ∗ · · · ∗ fσ L2( d+1),

(1.6) where fσ ∗ · · · ∗ fσ denotes the k-fold convolution of fσ with itself. Therefore, for p an even integer, (1.2) is equivalent to

fσ ∗ · · · ∗ fσ 1L/k

2( d+1) ≤ (2π)−(d+1)/2kCd,2k f L2( d) for all f ∈ S( d+1). For reference, we write here the best constants in convolution form:

fσ ∗ fσ 1L/22( 3) f −L21( 2) = π1/4, (1.7) sup 0 =f∈L2( 2)

sup

0 =f∈L2( 2)

fσ ∗ fσ ∗ fσ 1L/23( 3) f −L21( 2) = (2π)1/3, (1.8) sup 0 =f∈L2( 3)

fσ ∗ fσ 1L/22( 4) f −L21( 3) = (2π)1/4. (1.9)

It would be interesting to analyze the case d = 1 for even integers greater than or equal to 6. Our argument relies on the explicit computation of the n-fold convolution of the measure σ with itself, and this seems to be computationally complicated if n ≥ 3.

Interpolation shows that H2,p ≤ Hθ2,4H12−,6θ for d = 2 and p ∈ [4, 6], where p1 =

![image 21](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile21.png>)

θ 4 + 1−6θ. We do not know whether extremizers exist for p ∈ (4, 6), as our method only applies when p is an even integer.

![image 22](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile22.png>)

![image 23](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile23.png>)

![image 24](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile24.png>)

We consider, for s > 0, the hyperboloid ds = {(y, s2 + |y|2) : y ∈ d}, equipped with the measure

dydy′ s2 + |y|2

![image 25](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile25.png>)

σs(y, y′) = δ y′ − s2 + |y|2

. (1.10)

![image 26](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile26.png>)

![image 27](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile27.png>)

As we mention in Section 3, this measure is natural, since up to multiplication by scalar, it is the only Lorentz invariant measure on ds. Let Tsf(x, t) = fσs(x, t). For (d, p) satisfying (1.3),

Tsf Lp( d+1) ≤ Hd,p,s f L2( ds), (1.11) where

Tsf Lp( d+1) f L2( ds)

Hd,p,s = sup

(1.12) is a ﬁnite constant.

![image 28](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile28.png>)

0 =f∈L2( ds)

As shown in Appendix 1, simple scaling relates Hd,p,s and Hd,p by Hd,p,s = s(d−1)/2−(d+1)/pHd,p. (1.13)

Moreover, {fn}n∈ is a extremizing sequence for inequality (1.2) if and only if the sequence {s−1/2fn(s−1·)}n∈ is extremizing for inequality (1.11). Thus, for the problem of extremizers and properties of extremizing sequences, it is enough to study the case s = 1.

For each ρ ∈ (0, ∞), we consider the truncated hyperboloid

![image 29](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile29.png>)

d

s,ρ = y, s2 + |y|2 : y ∈ d, |y| ≤ ρ ,

endowed with the measure which is the restriction of σs to ds,ρ. For f ∈ L2( ds,ρ), let Ts,ρf = Tsf denote the corresponding adjoint Fourier restriction operator. Since

Ts,ρf L∞( d) ≤ C f L2( ds,ρ), it follows that for d ≥ 1,

Ts,ρf Lp( d+1) ≤ C f L2( ds,ρ) (1.14) for p ≥ 2(d + 2)/d and some constant C = C(d, p, s, ρ) < ∞.

The main theorem of Fanelli, Vega and Visciglia in [3, Theorem 1.1] implies that if d ≥ 1 and p > 2(d + 2)/d, complex-valued extremizers for (1.14) exist. There exist nonnegative extremizers if p is an even integer, as can be seen from the equivalent “convolution form” of (1.14). This shows that for (d, p) = (2, 6) and (d, p) = (3, 4), there exist extremizers for (1.14). The case (d, p) = (2, 4) does not follow from the result in [3], since it is the endpoint. In Proposition 5.6, we prove that in this case, extremizers do not exist and that the best constant in (1.14) is independent of ρ and equals the best constant for the full hyperboloid 2s.

2. Some related results

In this section, we discuss the results in [4] and their connection to the case of the adjoint Fourier restriction inequalities for the hyperboloid analyzed in this paper.

For r ∈ , the (nonhomogeneous) Sobolev space Hr( d) consists of tempered distributions g over d such that gˆ ∈ L2loc( d) and the norm

g 2Hr( d) :=

|gˆ(y)|2(1 + |y|2)rdy

d

is ﬁnite. The homogeneous Sobolev space H˙ r( d) is the space of tempered distributions g over d such that gˆ ∈ L1loc( d) and the norm

g 2H˙

|gˆ(y)|2|y|2rdy

r( d) :=

d

is ﬁnite. Note that the H˙ r( d)-norm satisﬁes the scaling property g(λ·) H ˙ r( d) = λr−d/2 g H ˙ r( d).

Let us introduce the notation used in [4]. For a function h : d → , the operator eith(D) is deﬁned by

1 (2π)d d

eix·yeith(y)gˆ(y)dy for g ∈ S( d), (2.1)

eith(D)g(x) =

![image 30](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile30.png>)

√

![image 31](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile31.png>)

and for a function η : → we deﬁne eitη(

−∆) = eitη(|D|). Note that eit

√

![image 32](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile32.png>)

−∆+s2g(x) = (2π)−dTf(x, t), where gˆ(y) = f(y)(s2 + |y|2)−1/2; therefore, (1.2) is equivalent to the estimate

√

![image 33](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile33.png>)

−∆+s2g Lp

eit

t,x( d+1) ≤ Cd,p,s g H1

2( d) (2.2) for a constant Cd,p,s < ∞ and p as in (1.3). For s > 0, the operator eit

![image 34](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile34.png>)

√

![image 35](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile35.png>)

−∆+s2 satisﬁes more general mixed-norm Strichartz estimates, namely,

√

![image 36](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile36.png>)

−∆+s2g Lp

eit

tLqx( d+1) ≤ C g

, (2.3) where p ∈ [2, ∞], q ∈ [2, 2d/(d − 2)] (q ∈ [2, ∞] if d = 1, 2), and

1 p − 1

q + 1

2 ( d)

![image 37](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile37.png>)

![image 38](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile38.png>)

![image 39](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile39.png>)

H

2 p

d − 1 + θ q

d − 1 + θ 2

+

=

, (p, q) = (2, ∞)

![image 40](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile40.png>)

![image 41](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile41.png>)

![image 42](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile42.png>)

Here, θ ∈ [0, 1]. We refer the reader to [6] and the references therein for these estimates.

Using (2.3), the Sobolev Embedding Theorem, and interpolation, we obtain that for d ≥ 2,

√

![image 43](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile43.png>)

−∆+s2g Lp

eit

t,x( d+1) ≤ C g Hr( d) (2.4) for all p and r satisfying

d 2

2(d + 2)(d − 1) d(d − 2r) ≤ p ≤

2(d + 1) d − 2r

- 1

![image 44](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile44.png>)

- 2 ≤ r <


,

. (2.5)

![image 45](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile45.png>)

![image 46](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile46.png>)

![image 47](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile47.png>)

An equivalent way to look at the adjoint Fourier restriction inequalities for the hyperboloid ds is through Strichartz estimates for the Klein-Gordon equation

∂t2u = ∆u − s2u in d+1 u(0, x) = u0(x), ∂tu(x, x) = u1(x).

(2.6) Writing the solution of (2.6) as

sin(t√

√

![image 48](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile48.png>)

−∆ + s2) √

![image 49](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile49.png>)

−∆ + s2)u0(·) +

u(t, ·) = cos(t

u1(·), or equivalently as

![image 50](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile50.png>)

![image 51](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile51.png>)

−∆ + s2

√

![image 52](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile52.png>)

−∆+s2

eit

√

- 1

![image 53](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile53.png>)

- 2


1 i

![image 54](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile54.png>)

−∆+s2u0(·) +

eit

√

u(t, ·) =

u1(·)

![image 55](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile55.png>)

![image 56](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile56.png>)

![image 57](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile57.png>)

−∆ + s2

e−it√

![image 58](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile58.png>)

−∆+s2

√

1 i

- 1

![image 59](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile59.png>)

- 2


![image 60](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile60.png>)

−∆+s2u0(·) −

e−it

√

u1(·) , we see that (2.4) is equivalent to the Strichartz estimate for u

+

![image 61](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile61.png>)

![image 62](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile62.png>)

![image 63](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile63.png>)

−∆ + s2

t,x( d+1) ≤ C (u0, u1) Hr( d)×Hr−1( d), (2.7) where (u0, u1) 2H

u Lp

r( d)×Hr−1( d) := u0 2H

r( d) + u1 2H

r−1( d), p and r are as in (2.5), and C < ∞ is a constant depending only on d, p, r and s.

In the context of this paper, it is natural to ask whether inequalities (2.4) and (2.7) admit extremizers g ∈ Hr( d) and (u0, u1) ∈ Hr( d)×Hr−1( d), respectively,

and whether extremizing sequences are precompact, after the possible application of symmetries. Here, extremizers and extremizing sequences are deﬁned similarly as for

- inequality (1.2) in Deﬁnition 1.1. In [4], the existence of extremals and precompactness of extremizing sequences is

studied for an inequality of the form eith(D)g Lp

t,x( d+1) ≤ C g H ˙ r( d), (2.8) for operators eith(D) that satisfy mixed-norm estimates

eith(D)g Lp

tLqx( d+1) ≤ C g H ˙ r( d)

for some 0 < r < d/2 and p and q satisfying 2 ≤ p < q ≤ ∞ where the function h(ξ) is homogenous of some degree k > 0, meaning that h(λξ) = λkh(ξ) for all λ > 0 and ξ ∈ d.

The argument in [4] uses the homogeneous Sobolev spaces H˙ r( d) and that the function h(ξ) is homogenous. Indeed, it is the scaling property of the H˙ r( d)-norm and the homogeneity of the function h that imply that (2.8) is invariant under scaling, and therefore the sequence deﬁned in [4, Equation 2.15] is still an extremizing sequence for the same inequality.

For the hyperboloid, the function h(ξ) = s2 + |ξ|2 is not homogeneous if s = 0. Therefore, in this case, the question of existence of extremizers in Hr( d), 1/2 < r < d/2, for inequality (2.4) is not answered in [4], although information can be obtained from arguments therein, which we record in Proposition 2.1. We can contrast this situation with the case of the cone Γd = {(y, |y|) : y ∈ d} with its dilation invariant measure σ0 = δ(y′ − |y|)|y|−1dydy′. This cone can be seen as the limiting case of the hyperboloid ( ds, σs) as s → 0.

![image 64](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile64.png>)

Let Tc denote the adjoint Fourier restriction operator on the cone (Γd, σ0):

Tcf(x, t) :=

d

eix·yeit|y|f(y)|y|−1dy, for f ∈ S( d). (2.9)

The operator eit

√

![image 65](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile65.png>)

−∆ is related to Tc by eit

√

![image 66](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile66.png>)

−∆g(x) = (2π)−dTcf(x, t), where gˆ(y) = f(y)|y|−1. For d ≥ 2, the operator eit

√

![image 67](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile67.png>)

−∆ satisﬁes

eit

√

![image 68](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile68.png>)

−∆g

L

2(d+1) d−2r

![image 69](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile69.png>)

t,x ( d+1)

≤ C g H ˙ r( d),

- 1

![image 70](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile70.png>)

- 2 ≤ r <


d 2

![image 71](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile71.png>)

. (2.10)

The main result of [4], Theorem 1.1, implies that for d ≥ 2, extremizers exist for

- inequality (2.10) for every 1/2 < r < d/2 and, moreover, extremizing sequences are precompact after the application of symmetries.


For the case r = 1/2, the existence of extremizers was proved by Carneiro [1] in the cases d = 2 and d = 3; he also found the exact form of the extremizers. The precompactness of extremizing sequences after the application of symmetries, and thus the existence of extremizers, was proved in [10] for d = 2 and by Ramos [11] for d ≥ 2.

The limiting case of the Klein-Gordon equation (2.6) as s → 0 is the wave equation ∂t2u = ∆u in d+1, u(0, x) = u0(x), ∂tu(x, x) = u1(x).

(2.11)

Its solution can be written as

√

e−it√

![image 72](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile72.png>)

![image 73](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile73.png>)

eit

−∆

−∆

√

√

- 1

![image 74](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile74.png>)

- 2


1 i

1 i

- 1

![image 75](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile75.png>)

- 2


![image 76](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile76.png>)

![image 77](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile77.png>)

eit

e−it

−∆u0(·) +

−∆u0(·) −

√

√

u(t, ·) =

u1(·) and satisﬁes, for d ≥ 2 and 1/2 ≤ r < d/2, u

u1(·) +

![image 78](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile78.png>)

![image 79](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile79.png>)

![image 80](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile80.png>)

![image 81](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile81.png>)

![image 82](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile82.png>)

![image 83](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile83.png>)

−∆

−∆

≤ C (u0, u1) H ˙ r( d)×H˙ r−1( d). (2.12)

2(d+1) d−2r

![image 84](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile84.png>)

t,x ( d+1)

L

Just as for the case of the adjoint Fourier restriction inequality for the cone, there are results concerning the existence of extremizers for inequality (2.12), (u0, u1) ∈ H˙ r( d) × H˙ r−1( d). Foschi [5] studied the case r = 1/2 for d = 2 and d = 3, proved the existence of extremizers, and found their exact form. The existence of extremizers for (2.12) when d ≥ 2 and 1/2 < r < d/2 was proved in [4], while the case d ≥ 2 and r = 1/2 was proved by Ramos [11]. See also the discussion at the end of [4, Example 1.4] for complementary results.

We note that the argument in [4] does not apply to inequality (2.7) for the same reasons stated before for inequality (2.4).

Let us return to inequality (2.4), where we consider the nonendpoint case, that is, the case p and r satisfy

d 2

2(d + 2)(d − 1) d(d − 2r)

2(d + 1) d − 2r

- 1

![image 85](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile85.png>)

- 2 ≤ r <


,

< p ≤

, (2.13)

![image 86](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile86.png>)

![image 87](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile87.png>)

![image 88](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile88.png>)

that is, (2.5) with the endpoint p = 2(d + 2)(d − 1)/d(d − 2r) removed.

In the next proposition, we show that the only obstruction to the convergence of extremizing sequences for inequality (2.4), after the applications of symmetries, is “concentration at inﬁnity” of the Fourier transform.

Proposition 2.1. Suppose that p and r satisfy (2.13). Let {gn}n∈ be an extremizing sequence for inequality (2.4). Then one of the following two possibilities holds.

- (i) For all R ∈ (0, ∞), limn→∞ |y|≤R |gˆn(y)|2(1 + |y|2)rdy = 0.
- (ii) There exist a subsequence {gn


k}k∈ and a sequence {(yk, tk)}k∈ ⊂ d × such that {eitk

√

![image 89](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile89.png>)

−∆+s2gn

(y − yk)}k∈ converges in Hr( d). Moreover, if (i) holds, then there exist a subsequence {gn

k

k}k∈ , a sequence of positive real numbers {λk}k∈ , λk → 0 as k → ∞, a sequence {(yk, tk)}k∈ ⊂ d × , and 0 = v ∈ H˙ r( d) such that

√

λd/k 2−reit

![image 90](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile90.png>)

−∆+s2gn

(λk(y − yk)) ⇀ v as k → ∞ (2.14) weakly in the homogeneous Sobolev space H˙ r( d).

k

k

In the dual formulation, in “physical space” instead of “frequency space”, that is, via the equality gˆ(y) = f(y)(s2 + |y|2)−1/2, inequality (2.4) becomes the weighted estimate

Tsf Lp( d) ≤ C f L2(µs), (2.15) where the measure µs(y, y′) = (1 + |y|2)r(s2 + |y|2)−1/2σs(y, y′) is supported on ds.

The two possibilities in the previous proposition, when written for (2.15), are as follows.

- (i’) The sequence {fn}n∈ concentrates at spatial inﬁnity, that is, for all R ∈ (0, ∞),

lim

n→∞ |y|≤R

|fn(y)|2(s2 + |y|2)r−1dy = 0.

- (ii’) There exist a subsequence {fn


k}k∈ and a sequence {(yk, tk)}k∈ ⊂ d × such that {eiy·ykeit

√

![image 91](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile91.png>)

s2+|y|2fn

(y)}k∈ converges in L2(µs). For a set A ⊆ d we denote χA the characteristic function of the set A. Sketch of the proof of Proposition 2.1. If condition (i) is not satisﬁed, then there exist R ∈ (0, ∞) and a subsequence of {gn}n∈ , which we also call {gn}n∈ , satisfying

k

k

|gˆn(y)|2(1 + |y|2)rdy =: ε2 > 0. (2.16)

inf

n∈ |y|≤R

We deﬁne gn,1 and gn,2 by their Fourier transforms, gˆn,1(y) = gˆn(y)χ{|y|≤R}, gˆn,2(y) = gˆn(y)χ{|y|>R}. Then gn = gn,1+gn,2; and for all large enough n, we have gn,1 Hr( d) ≥ ε/2 and eit

√

![image 92](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile92.png>)

−∆+s2gn,1 Lp( d+1) ≥ c > 0 for a certain constant c independent of n.

Under the assumptions on p and r, we can apply the “ﬁrst step“ in the proof of [3, Theorem 1.1] to the sequence {gn,1}n∈ to show that there exist a subsequence, which we also call {gn,1}n∈ , and a sequence {(yn, tn)}n∈ ⊂ d × such that the functions y  → (eit

√

![image 93](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile93.png>)

−∆+s2gn,1)(y − yn) have a nonzero uniform limit in {y ∈ d : |y| ≤ R}. This implies that weak limits of the sequence {eit

n

√

![image 94](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile94.png>)

−∆+s2gn(· − yn)}n∈ in Hr( d) are nonzero. Using the argument given in the proof of [4, Theorem 1.1] or an argument similar to that in [10, Proposition 8.3], we see that all the hypotheses of [3, Proposition 1.1] are satisﬁed by the sequence {eit

n

√

![image 95](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile95.png>)

−∆+s2gn(· −yn)}n∈ , which is extremizing. Therefore the latter sequence is precompact in Hr( d), and (ii) is satisﬁed.

n

k}k∈ , the sequences {λk}k∈ , and {(yk, tk)}k∈ ⊂ d × , and the function v ∈ H˙ r( d), v = 0, satisfying (2.14) follows as in [4, Proof of Theorem 1.1]. That λk → 0 as k → ∞ follows from (i). Indeed, if there exists a subsequence {λk

Let us now suppose that (i) is satisﬁed. The existence of the subsequence {gn

l}l∈ with infl∈ λk

> 0, then the functions hk(y) := λd/k 2−reitk

l

√

![image 96](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile96.png>)

−∆+s2gn

(λk(y − yk)) satisfy

k

|hˆk

(y)|2(1/λ2k

(y)|2(1 + |y|2)rdy =

|gˆn

l

kl

l

|y|≤R

|y|≤R/λkl

for every R < ∞, which is impossible since v = 0.

+ |y|2)rdy → 0 as l → ∞,

3. The Lorentz invariance

The Lorentz group is deﬁned as the group of invertible linear transformations in d+1 preserving the bilinear form (x, y) ∈ d+1 × d+1  → x · Jy, where J = diag(−1, . . ., −1, 1).

Let us denote by L+ the subgroup of Lorentz transformations in d+1 that preserve

- s. It is known that σs is invariant under the action of L+ and moreover is, up to

multiplication by scalar, the unique measure on ds invariant under such Lorentz transformations; see [12] where the case d = 3 is considered. The same argument can be adapted to d ≥ 2.

For t ∈ (−1, 1), we deﬁne the linear map Lt : d+1 → d+1 by Lt(ξ1, . . ., ξd, τ) =

ξ1 + tτ √1 − t2

![image 97](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile97.png>)

![image 98](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile98.png>)

, ξ2 . . ., ξd,

τ + tξ1 √1 − t2

![image 99](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile99.png>)

![image 100](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile100.png>)

.

Then {Lt}t∈(−1,1) is a one parameter subgroup of Lorentz transformations contained in L+.

For i, j ∈ {1, . . ., d}, let Pi,j be the linear transformation that swaps the ith and jth components of every vector in d+1. More precisely, for (ξ1, . . ., ξd, τ) ∈ d+1, Pi,j(ξ1, . . ., ξd, τ) = (ξω

i,j(1), . . ., ξω

i,j(d), τ), where ωi,j is the permutation of {1, . . ., d} deﬁned by

ωi,j(k) =

 



- j if k = i, i if k = j,
- k otherwise.


For every orthogonal matrix A ∈ O(d, ), the transformation (ξ, τ)  → RA(ξ, τ) = (Aξ, τ) belongs to L+.

Composing the transformations Pi,j and Lt for suitable i, j’s and t’s, we easily see that if (ξ, τ) ∈ d+1 satisﬁes τ > |ξ|, then there exists L ∈ L+ such that L(ξ, τ) = (0, τ2 − ξ2). Alternatively, this can be seen using the transformations RA and Lt. We ﬁrst ﬁnd A ∈ O(d, ) such that Aξ = (|ξ|, 0, . . ., 0). We take

![image 101](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile101.png>)

- t = −|ξ|τ−1 and note that Lt(RA(ξ, τ)) = Lt(|ξ|, 0, . . ., 0, τ) = (0, τ2 − |ξ|2).


d

![image 102](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile102.png>)

For p ∈ [1, ∞], L ∈ L+, and f ∈ Lp( ds) we deﬁne L∗f = f ◦ L; here “◦” denotes composition. The invariance of the measure σs under the action of L+ implies that f Lp( ds) = L∗f Lp( ds) for all p ∈ [1, ∞], equality holding for p = ∞ since Lorentz transformations are invertible. It is also straightforward to check that

Ts(L∗f) Lp( d+1) = Tsf Lp( d+1) for p ∈ [1, ∞]. Therefore, if {fn}n∈ is an extremizing sequence for (1.11) and {Ln}n∈ ⊂ L+, then {L∗

nfn}n∈ is also an extremizing sequence for (1.11).

We use the Lorentz transformations Pi,j, RA and Lt. The invariance of σs with respect to these transformations can be seen directly from an examination of the Jacobians in the change of variables formula.

4. On Foschi’s argument

For ease of notation, let ψs(x) = √s2 + x2 for s, x ∈ and set ψ := ψ1. We also write ψs(y) to mean ψs(|y|) for y ∈ d. We deﬁne the convolution of measures µ, ν

![image 103](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile103.png>)

on d by duality as

gd(µ ∗ ν) =

d

g(x + y)dµ(x)dν(y),

( d)2

for all g ∈ C0( d). For a measure µ on d and n ≥ 1, µ(∗n) = µ ∗ · · · ∗ µ denotes the n-fold convolution of µ with itself.

The measure σs on ds has the property that σs(∗n) is supported in the closure of the region Pd,n = {(ξ, τ) : τ > (ns)2 + |ξ|2}. For each ﬁxed (ξ, τ) ∈ Pd,n, we deﬁne the measure on ( d)n

![image 104](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile104.png>)

µ(ξ,τ) = δ τ − ψs(x1) − · · · − ψs(xn) ξ − x1 − · · · − xn

dx1 · · ·dxn.

Recall that the Dirac delta measure δ0 on d × , is deﬁned by δ0, f = f(0), for all f ∈ S( d × ).

The measure µ(ξ,τ) is the pullback of δ0 on d × by Φ(ξ,τ) : ( d)n → d × given by

Φ(ξ,τ)(x1, . . ., xn) = (ξ − x1 − · · · − xn, τ − ψs(x1) − · · · − ψs(xn)).

As discussed in [5], the pullback is well-deﬁned as long as the diﬀerential of Φ(ξ,τ) is surjective at the points where Φ(ξ,τ) vanishes. The diﬀerential of Φ(ξ,τ) is surjective at a point (x1, . . ., xn) if and only if x1, . . ., xn are not all equal. Now Φ(ξ,τ)(x, . . ., x) = 0 if and only if τ2 = (ns)2 + |ξ|2, that is, at the boundary of Pd,n. Thus, the pullback is well-deﬁned on Pd,n.

For each (ξ, τ) ∈ Pd,n, we deﬁne the inner product  ·, · (ξ,τ) and norm  · (ξ,τ) associated to µ(ξ,τ) as

F, G (ξ,τ) =

![image 105](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile105.png>)

F(x1, . . ., xn)G(x1, . . ., xn)dµ(ξ,τ)(x1, . . ., xn),

( d)n

F 2(ξ,τ) =

|F(x1, . . ., xn)|2 dµ(ξ,τ)(x1, . . ., xn).

( d)n

What connects this inner product with inequality (1.2) is the following identity. For f1, . . ., fn ∈ L2( ds),

f1(x1) · · ·fn(xn) ψs(x1) · · ·ψs(xn)

f1σs ∗ · · · ∗ fnσs =

δ(ξ − x1 − · · · − xn) · δ(τ − ψs(x1) − · · · − ψs(xn)) dx1 · · ·dxn

![image 106](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile106.png>)

( d)n

f1(x1) · · ·fn(xn) ψs(x1) · · ·ψs(xn)

=

dµ(ξ,τ)(x1, . . ., xn)

![image 107](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile107.png>)

( d)n

= F, G (ξ,τ), where

f1(x1) · · ·fn(xn) ψs(x1)1/2 · · ·ψs(xn)1/2

F(x1, . . ., xn) =

![image 108](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile108.png>)

and

1 ψs(x1)1/2 · · ·ψs(xn)1/2

.

G(x1, . . ., xn) =

![image 109](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile109.png>)

- Lemma 4.1. If f ∈ S( d), then


(fσs)(∗n) L2( d) ≤ σs(∗n) 1L/2

∞( d) f nL2( ds). (4.1) Moreover, for f = 0, equality holds in (4.1) only if σs(∗n)(ξ, τ) = σs(∗n) L∞( d) for a.e. (ξ, τ) in the support of (fσs)(∗n). Proof. Let g ∈ S( d+1). By deﬁnition of the convolution,

g, (fσs)(∗n) =

g(x1 + · · · + xn, ψs(x1) + · · · + ψs(xn))

( d)n

f(x1) · · ·f(xn) ψs(x1) · · ·ψs(xn)

dx1 . . .dxn

·

![image 110](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile110.png>)

g(x1 + · · · + xn, ψs(x1) + · · · + ψs(xn)) ψs(x1)1/2 · · ·ψs(xn)1/2 ·

=

![image 111](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile111.png>)

( d)n

f(x1) · · ·f(xn) ψs(x1)1/2 · · ·ψs(xn)1/2

dx1 · · ·dxn

![image 112](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile112.png>)

1/2

g2(x1 + · · · + xn, ψs(x1) + · · · + ψs(xn)) ψs(x1) · · ·ψs(xn)

dx1 · · ·dxn

≤

![image 113](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile113.png>)

( d)n

(4.2) ·

1/2

f(x1)2 · · ·f(xn)2 ψs(x1) · · ·ψs(xn)

dx1 · · ·dxn

![image 114](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile114.png>)

( d)n

= g2, σs(∗n) 1/2 f nL2( ds) ≤ g L2( d) σs(∗n) 1L/2

∞( d) f nL2( ds). (4.3) Taking the supremum over g ∈ L2( d+1) proves (4.1).

L2( d) = σs(∗n) 1L/2

∞( d) f nL2( d

s), then, taking g = (fσs)(∗n), we must have equality in (4.3), i.e.,

Now if (fσs)(∗n)

((fσs)(∗n))2, σs(∗n) = (fσs)(∗n) 2L2( ds) σs(∗n) L∞( d),

which occurs if and only if σs(∗n)(ξ, τ) = σs(∗n) L∞( d) for a.e. (ξ, τ) in the support of (fσs)(∗n).

From Lemma 4.1 and (1.6), we obtain the following result.

- Corollary 4.2. Let (d, p) satisfy (1.3) and suppose p = 2k is an even integer. Then


Tsf Lp( d+1) ≤ (2π)(d+1)/p σs(∗k) 1L/p

∞( d+1) f L2( ds), (4.4) and thus

Hd,p,s ≤ (2π)(d+1)/p σs(∗k) 1L/p

∞( d+1). (4.5)

In the three cases of pairs (d, p) that interest us in this paper, (4.5) gives

H2,4,s ≤ (2π)3/4 σs ∗ σs 1L/∞4( 3),

- H2,6,s ≤ (2π)1/2 σs ∗ σs ∗ σs 1L/∞6( 3), and
- H3,4,s ≤ 2π σs ∗ σs 1L/∞4( 4).


To prove the nonexistence of extremizers, we use the following result.

- Corollary 4.3. Let (d, p) satisfy (1.3) and suppose p = 2k is an even integer. Sup-


pose that Hd,p = (2π)(d+1)/p σ(∗k) 1/p

L∞( d+1) and that σ(∗k)(τ, ξ) < σ(∗k)

L∞( d+1) for a.e. (ξ, τ) in the support of σ(∗k). Then extremizers for inequality (1.2) do not exist for the pair (d, p).

Proof. This is direct consequence of the last assertion in Lemma 4.1.

- Lemma 4.4. If f ∈ S( d), then


fσs(∗n) 2L2( d) ≤

f2(x1) · · ·f2(xn) ψs(x1) · · ·ψs(xn)

![image 115](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile115.png>)

( d)n

· σs(∗n)(x1 + · · · + xn, ψs(x1) + · · · + ψs(xn)) dx1 · · ·dxn. (4.6)

Proof. We prove the Lemma only for the case n = 2; the proof for the general case is similar and only requires more notation. Following Foschi’s argument, we write

fσs ∗ fσs(ξ, τ) =

=

f(x)f(y) ψs(x)ψs(y)

δ(ξ − x − y)δ(τ − ψs(x) − ψs(y)) dxdy

![image 116](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile116.png>)

( d)2

f(x)f(y) ψs(x)ψs(y)

dµ(τ,ξ)(x, y). (4.7)

![image 117](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile117.png>)

( d)2

From the Cauchy-Schwarz inequality, for (ξ, τ) ∈ Pd,2,

|fσs ∗ fσs(τ, ξ)| ≤

f(x)f(y) ψs(x)1/2ψs(y)1/2 (τ,ξ)

![image 118](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile118.png>)

1 ψs(x)1/2ψs(y)1/2 (τ,ξ)

. (4.8)

![image 119](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile119.png>)

Now

1 ψs(x)1/2ψs(y)1/2

![image 120](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile120.png>)

2

= σs ∗ σs(ξ, τ) (4.9)

(τ,ξ)

- as can be seen from (4.7) by taking f ≡ 1. Then


2

f(x)f(y) ψs(x)1/2ψs(y)1/2

fσs ∗ fσs 22 ≤

σs ∗ σs(ξ, τ)dτ dξ

![image 121](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile121.png>)

Pd,2

(τ,ξ)

f2(x)f2(y) ψs(x)ψs(y)

δ τ − ψs(x) − ψs(y) ξ − x − y

=

σs ∗ σs(ξ, τ) dxdy dτ dξ

![image 122](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile122.png>)

Pd,2 ( d)2

f2(x)f2(y) ψs(x)ψs(y) P

δ τ − ψs(x) − ψs(y) ξ − x − y

=

σs ∗ σs(ξ, τ) dτ dξ dxdy

![image 123](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile123.png>)

( d)2

d,2

f2(x)f2(y) ψs(x)ψs(y)

σs ∗ σs(x + y, ψs(x) + ψs(y)) dxdy.

=

![image 124](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile124.png>)

( d)2

5. Nonexistence of extremizers

In this section, we prove the ﬁrst part of Theorem 1.2 related to the best constants and nonexistence of extremizers for the adjoint Fourier restriction inequality for d. We start with the computation of the double and triple convolution of σs with itself.

- Lemma 5.1. Let d = 2, s > 0, and let σs be the measure on 2s given in (1.10). Then for (ξ, τ) ∈ 2 × ,


2π τ2 − |ξ|2

χ{τ≥√

σs ∗ σs(ξ, τ) =

(2s)2+|ξ|2}, (5.1)

![image 125](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile125.png>)

![image 126](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile126.png>)

![image 127](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile127.png>)

3s τ2 − |ξ|2

χ{τ≥√

σs ∗ σs ∗ σs(ξ, τ) = (2π)2 1 −

(3s)2+|ξ|2}. (5.2)

![image 128](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile128.png>)

![image 129](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile129.png>)

![image 130](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile130.png>)

- In particular, σs ∗ σs L∞( 3) = π/s, and σs ∗ σs(ξ, τ) < σs ∗ σs L∞( 3) for all (ξ, τ) in the interior of the support of σs ∗ σs. Also, σs ∗ σs ∗ σs L∞( 3) = (2π)2, and for all (ξ, τ) ∈ d+1, σs ∗ σs ∗ σs(ξ, τ) < σs ∗ σs ∗ σs L∞( 3). Proof. It is easy to compute the convolution


![image 131](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile131.png>)

δ(τ − 2 s2 + |y|2)

σs ∗ σs(0, τ) =

2

Let u = 2√s2 + r2. Then

![image 132](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile132.png>)

σs ∗ σs(0, τ) = 2π

∞

2s

dy s2 + |y|2

= 2π

![image 133](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile133.png>)

∞

δ(τ − 2

0

√

rdr s2 + r2

![image 134](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile134.png>)

s2 + r2)

.

![image 135](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile135.png>)

du u

=

δ(τ − u)

![image 136](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile136.png>)

2π τ

χ{τ≥2s}.

![image 137](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile137.png>)

By Lorentz invariance, we obtain

2π τ2 − |ξ|2

χ{τ≥√

(2s)2+|ξ|2}.

σs ∗ σs(ξ, τ) =

![image 138](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile138.png>)

![image 139](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile139.png>)

![image 140](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile140.png>)

To compute the triple convolution, we use the expression we just obtained for the double convolution, which yields

dy s2 + |y|2

![image 141](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile141.png>)

σ ∗ σ(−y, τ − s2 + |y|2)

σs ∗ σs ∗ σs(0, τ) =

![image 142](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile142.png>)

![image 143](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile143.png>)

2

√

χ{τ−√s

∞

rdr √s2 + r2

![image 144](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile144.png>)

![image 145](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile145.png>)

2+r2≥

(2s)2+r2}

= (2π)2

.

√s2 + r2)2 − r2

![image 146](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile146.png>)

![image 147](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile147.png>)

![image 148](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile148.png>)

![image 149](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile149.png>)

![image 150](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile150.png>)

0

(τ −

Let u = √s2 + r2. Then

![image 151](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile151.png>)

τ2−3s2 2τ

du (τ − u)2 − (u2 − s2)

![image 152](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile152.png>)

σs ∗ σs ∗ σs(0, τ) = (2π)2χ{τ≥3s}

![image 153](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile153.png>)

![image 154](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile154.png>)

s

τ2−3s2 2τ

du √τ2 − 2τu + s2

![image 155](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile155.png>)

= (2π)2χ{τ≥3s}

![image 156](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile156.png>)

![image 157](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile157.png>)

s

3s τ

= (2π)2 1 −

χ{τ≥3s}. By Lorentz invariance,

![image 158](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile158.png>)

3s τ2 − |ξ|2

χ{τ≥√

σs ∗ σs ∗ σs(ξ, τ) = (2π)2 1 −

(3s)2+|ξ|2}.

![image 159](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile159.png>)

![image 160](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile160.png>)

![image 161](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile161.png>)

- Lemma 5.2. Let d = 3 and s > 0. Then for (ξ, τ) ∈ 3 × ,


1/2

4s2 τ2 − |ξ|2

χ{τ≥√

(2s)2+|ξ|2}. (5.3)

σs ∗ σs(ξ, τ) = 2π 1 −

![image 162](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile162.png>)

![image 163](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile163.png>)

- In particular, σs ∗ σs L∞( 4) = 2π, and for all (ξ, τ) ∈ 4, σs ∗ σs(ξ, τ) < σs ∗ σs L∞( 4).


Proof. σs ∗ σs(0, τ) =

√

∞

- r2dr

![image 164](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile164.png>)

- s2 + r2


dy s2 + |y|2

![image 165](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile165.png>)

![image 166](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile166.png>)

δ(τ − 2 s2 + |y|2)

s2 + r2)

. Let u = 2√s2 + r2. Then

= 4π

δ(τ − 2

![image 167](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile167.png>)

3

0

![image 168](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile168.png>)

√u2 − 4s2 u

√τ2 − 4s2 τ

∞

![image 169](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile169.png>)

![image 170](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile170.png>)

σs ∗ σs(0, τ) = 2π

δ(τ − u)

du = 2π

χ{τ≥2s}

![image 171](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile171.png>)

![image 172](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile172.png>)

2s

1/2

4s2 τ2

= 2π 1 −

χ{τ≥2s}. Therefore, by the Lorentz invariance,

![image 173](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile173.png>)

1/2

4s2 τ2 − |ξ|2

χ{τ≥√

(2s)2+|ξ|2}. From Corollary 4.2 and Lemmas 5.1 and 5.2, we obtain the following result.

σs ∗ σs(ξ, τ) = 2π 1 −

![image 174](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile174.png>)

![image 175](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile175.png>)

Corollary 5.3. H2,4 ≤ 23/4π, H2,6 ≤ (2π)5/6, and H3,4 ≤ (2π)5/4.

To obtain the lower bound for the best constants, we exhibit explicit extremizing sequences.

- Lemma 5.4. Let d = 2 and s > 0. For a > 0, let fa(y) = e−a

√

![image 176](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile176.png>)

s2+|y|2, y ∈ 2. Then

lim

a→∞

Tsfa L4( 3) fa −L21( 2

s) =

23/4π s1/4

![image 177](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile177.png>)

, (5.4) lim

a→0+

Tsfa L6( 3) fa −L21( 2

s) = (2π)5/6. (5.5)

The proof of this is given in Appendix 2. For the case d = 3, we have an analogous result.

- Lemma 5.5. Let d = 3 and s > 0. For a > 0, let fa(y) = e−a


√

![image 178](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile178.png>)

s2+|y|2, y ∈ 3. Then lim a→0+

Tsfa L4( 4) fa −L21( 3

s) = (2π)5/4.

The proof of Lemma 5.5 is in Appendix 3. Note that Corollary 5.3 and Lemmas 5.4 and 5.5 imply that for (d, p) = (2, 4), the family {fa/ fa L2(σs)}a>0 is an extremizing family as a → ∞, while for (d, p) = {fa/ fa L2(σs)}a>0 is an extremizing family as a → 0+. An extremizing family {fa}a>0 is deﬁned as in Deﬁnition 1.1, where we replace the limit in n by a limit in a.

- (2, 3), {fa/ fa L2(σs)}a>0 is an extremizing family as a → 0+, and for (d, p) = (3, 6),


We now give the proof of the part of Theorem 1.2 related to the best constants

and extremizers for the adjoint Fourier restriction inequality on ds; the proof of the second part, related to the two-sheeted hyperboloid ¯ d

s, is deferred to Section 7.

Proof of the ﬁrst part of Theorem 1.2. Combining Corollary 5.3 and Lemmas 5.4 and 5.5, we obtain the ﬁrst part of Theorem 1.2, namely

H2,4 = 23/4π, H2,6 = (2π)5/6, and H3,6 = (2π)5/4.

That extremizers do not exist is a consequence of Corollary 4.3 and the last assertions about the inﬁnity norm of the double and triple convolutions of σ with itself, contained in Lemmas 5.1 and 5.2.

We now prove the assertion given in the Introduction about extremizers for the truncated operator Tρ for d = 2 and p = 4.

- Proposition 5.6. Let (d, p) = (2, 4) and s > 0. For any ρ > 0, the best constant in inequality (1.14) equals 23/4π/s1/4, and there are no extremizers for inequality (1.14).


Proof. The nonexistence of extremizers for inequality (1.14) follows from the nonexistence of extremizers for inequality for (1.2) once we prove that the best constant for the truncated hyperboloid equals the best constant for the entire hyperboloid, H2,4,s. For this, we need a lower bound.

Since the extremizing family {fa/ fa L2(σs)}a>0 given in Lemma 5.4 concentrates

- at y = 0 as a → ∞, one easily sees that Tρ(faχ{|y|≤ρ}/ faχ{|y|≤ρ} L2(σs)) → 23/4π/s1/4 , as a → ∞


for the family {faχ{|y|≤ρ}/ faχ{|y|≤ρ} L2(σs)}a>0. This gives the desired lower bound.

6. On extremizing sequences

In this section, we obtain some general properties concerning concentration of extremizing sequences for inequality (1.2) for the cases (d, p) = (2, 4), (2, 6) and

- (3, 4). The Lorentz invariance of σs implies that given an extremizing sequence {fn}n∈


for inequality (1.11) and a sequence of Lorentz transformations {Ln}n∈ preserving

d

s, {fn ◦ Ln}n∈ is also an extremizing sequence. In this section, it is only in the case (d, p) = (2, 4) that the Lorentz group is used explicitly, but an equivalent result can be written without it, as discussed before the statement of Proposition 6.3.

Consider ﬁrst the case d = 2 and p = 6. From Lemma 5.4, it follows that the family of functions {fa/ fa 2}a>0 is an extremizing family as a → 0+. This particular extremizing family concentrates at spatial inﬁnity, that is, for every ε, R > 0, there

exists a0 > 0 such that for all 0 < a < a0, fa/ fa 2 L2(B(0,R)) < ε, where B(0, R) = {y ∈ 2 : |y| < R}. Next we show that this is the case for every extremizing sequence.

- Proposition 6.1. Let {fn}n∈ be an extremizing sequence for inequality (1.11) in


- the case (d, p) = (2, 6). Then for any ε, R > 0, there exists N ∈ such that for n ≥ N,


fn L2(B(0,R)) < ε, that is, the sequence concentrates at spatial inﬁnity. Proof. Let ε, R > 0 be given. From the proof of Lemma 4.4 and from Lemma 5.1, we have for the inequality in convolution form

fnσs∗fnσs ∗ fnσs 2L2( 3) ≤

2

fn(x)fn(y)fn(z) ψs(x)1/2ψs(y)1/2ψs(z)1/2

σs ∗ σs ∗ σs(τ, ξ)dτdξ

![image 179](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile179.png>)

P2,3

(τ,ξ)

2

3s τ2 − |ξ|2

fn(x)fn(y)fn(z) ψs(x)1/2ψs(y)1/2ψs(z)1/2

= (2π)2

1 −

dτdξ

![image 180](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile180.png>)

![image 181](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile181.png>)

![image 182](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile182.png>)

P2,3

(τ,ξ)

2

3s dτdξ τ2 − |ξ|2

fn(x)fn(y)fn(z) ψs(x)1/2ψs(y)1/2ψs(z)1/2

= (2π)2 fn 6L2(σs) − (2π)2

.

![image 183](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile183.png>)

![image 184](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile184.png>)

![image 185](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile185.png>)

P2,3

(τ,ξ)

Since fnσs ∗ fnσs ∗ fnσs 2L2( 3) → (2π)2 as n → ∞, we obtain

2

dτdξ τ2 − |ξ|2

fn(x)fn(y)fn(z) ψs(x)1/2ψs(y)1/2ψs(z)1/2

→ 0 as n → ∞; (6.1)

![image 186](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile186.png>)

![image 187](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile187.png>)

![image 188](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile188.png>)

P2,3

(τ,ξ)

and thus there exists N ∈ such that for all n ≥ N,

2

dτdξ τ2 − |ξ|2

fn(x)fn(y)fn(z) ψs(x)1/2ψs(y)1/2ψs(z)1/2

ε 3√s2 + R2

<

.

![image 189](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile189.png>)

![image 190](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile190.png>)

![image 191](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile191.png>)

![image 192](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile192.png>)

![image 193](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile193.png>)

P2,3

(τ,ξ)

By Lemma 4.4, the expression in the left hand side can be written as

2

dτdξ τ2 − |ξ|2

fn(x)fn(y)fn(z) ψs(x)1/2ψs(y)1/2ψs(z)1/2

![image 194](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile194.png>)

![image 195](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile195.png>)

![image 196](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile196.png>)

P2,3

(τ,ξ)

fn2(x)fn2(y)fn2(z) ψs(x)ψs(y)ψs(z) P

dτdξ τ2 − |ξ|2

δ τ − ψs(x) − ψs(y) − ψs(z) ξ − x − y − z

=

dxdydz

![image 197](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile197.png>)

![image 198](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile198.png>)

![image 199](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile199.png>)

( 2)3

2,3

fn2(x)fn2(y)fn2(z) ψs(x)ψs(y)ψs(z) P

1 τ

δ τ − ψs(x) − ψs(y) − ψs(z) ξ − x − y − z

dτdξ dxdy dz

≥

![image 200](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile200.png>)

![image 201](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile201.png>)

( 2)3

2,3

fn2(x)fn2(y)fn2(z) ψs(x)ψs(y)ψs(z)

dxdy dz ψs(x) + ψs(y) + ψs(z)

≥

.

![image 202](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile202.png>)

![image 203](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile203.png>)

(B(0,R))3

If x, y, z ∈ B(0, R), then 3s < ψs(x) + ψs(y) + ψs(z) ≤ 3ψs(R) = 3√s2 + R2. Therefore, for all n ≥ N,

![image 204](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile204.png>)

2

dτdξ

ε 3√s2 + R2

fn(x)fn(y)fn(z) ψs(x)1/2ψs(y)1/2ψs(z)1/2

>

![image 205](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile205.png>)

![image 206](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile206.png>)

![image 207](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile207.png>)

![image 208](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile208.png>)

![image 209](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile209.png>)

τ2 − |ξ|2 ≥

P2,3

(τ,ξ)

1 3√s2 + R2

fn 6L2(B(0,R)); and so, supn≥N fn L2(B(0,R)) < ε as desired.

![image 210](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile210.png>)

![image 211](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile211.png>)

We now turn to the case d = 3 and p = 4. Here we can also prove the analog of Proposition 6.1, namely, that extremizing sequences must concentrate at spatial inﬁnity.

- Proposition 6.2. Let {fn}n∈ be an extremizing sequence for inequality (1.11) in


- the case (d, p) = (3, 4). Then for any ε, R > 0, there exists N ∈ such that for all n ≥ N,


fn L2(B(0,R)) < ε, that is, the sequence concentrates at spatial inﬁnity. Proof. The proof follows the same lines as that of Proposition 6.1. Using the convolution form of the inequality, we obtain the analog of equation (6.1),

2

4s2 τ2 − |ξ|2

fn(x)fn(y)fn(z) ψs(x)1/2ψs(y)1/2ψs(z)1/2

1/2

1 − 1 −

![image 212](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile212.png>)

![image 213](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile213.png>)

P3,2

(τ,ξ)

If we use the bound 1 − 1 −

1/2

4s2 τ2 − |ξ|2

4s2 τ2

≥ 1 − 1 −

![image 214](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile214.png>)

![image 215](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile215.png>)

dτdξ → 0 as n → ∞.

1/2

and the fact that 0 < ψs(x) + ψs(y) ≤ 2ψs(R) whenever |x|, |y| ≤ R, we obtain

2

4s2 τ2 − |ξ|2

fn(x)fn(y)fn(z) ψs(x)1/2ψs(y)1/2ψs(z)1/2

1/2

1 − 1 −

dτdξ

![image 216](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile216.png>)

![image 217](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile217.png>)

P3,2

(τ,ξ)

R2 R2 + s2

1/2

fn 2L2(B(0,R)). The conclusion follows as in the proof of Proposition 6.1.

≥ 1 −

![image 218](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile218.png>)

We now analyze the last case (d, p) = (2, 4). Since σs ∗ σs(ξ, τ) = σs ∗ σs L∞( 3)

![image 219](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile219.png>)

whenever τ = (2s)2 + |ξ|2, that is, at the boundary of the support of σs ∗ σs, it is not hard to see that there are extremizing sequences that concentrate at any given

point in 2s. For the example of an extremizing sequence given in Lemma 5.4, the concentration occurs at the vertex of the hyperboloid (ξ, τ) = (0, s) =: P. We want to show that all extremizing sequences concentrate.

Since every point in 2s has an extremizing sequence concentrating at it, we can construct an extremizing sequence that concentrates along any given sequence in

s in the sense that given a sequence {yn}n∈ ⊂ 2s, there exists an extremizing sequence {fn}n∈ ⊂ L2( 2s) with the property that for every ε > 0 and r > 0, there exists N ∈ such that

2

|fn(y)|2 dσs(y) ≤ ε (6.2) for all n ≥ N. Equivalently, taking a Lorentz transformation Ln ∈ L+ with L−1

|y−yn|>r

n (yn) = (0, s) = P and using the Lorentz invariance of the measure σs, we can write (6.2) as

|L∗nfn(y)|2 dσs(y) ≤ ε, where L∗

L−n1({y:|y|>r})+P

nfn(y) = fn(Lny). We show next that this is the case for every extremizing sequence.

- Proposition 6.3. Let {fn}n∈ be an extremizing sequence for inequality (1.11) in the case (d, p) = (2, 4). There exists a sequence {Ln}n∈ ⊂ L+ with the property that for all ε, r > 0, there exists N ∈ such that


|L∗nfn(y)|2 dσs(y) ≤ ε, (6.3) for all n ≥ N, where P = (0, s) is the vertex of the hyperboloid 2s.

|y−P|>r

To prove this proposition, we introduce the function ds : 2 × 2 → given by the formula

- 1

![image 220](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile220.png>)

- 2s


((ψs(x) + ψs(y))2 − |x + y|2)1/2 − 1.

ds(x, y) =

Elementary properties of ds are described in the next lemma, whose proof is left to the reader.

- Lemma 6.4. (i) For all x, y ∈ 2, ds(x, y) = ds(y, x) ≥ 0, and ds(x, y) = 0 if and only if x = y.


(ii) For all x ∈ 2, lim|y|→∞ ds(x, y) = ∞. (iii) For every R > 0, there exist 0 < C1(R), C2(R) < ∞ such that

C1(R)|x − y|2 ≤ ds(x, y) ≤ C2(R)|x − y|, for all x, y with |x|, |y| ≤ R.

- Property (ii) implies that for given y ∈ 2, the ds-ball of radius R > 0 and center


(y, R) := {x ∈ 2 : ds(x, y) ≤ R}, is a bounded set. Property (iii) relates the ds-ball to the euclidean ball; namely, it implies that for y with |y| ≤ R and r > 0

y, Bd

s

(y, r) ⊂ B(y, c′√r), (6.4) for some constants c, c′ depending only on R and r.

![image 221](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile221.png>)

B(y, cr) ⊂ Bd

s

Proof of Proposition 6.3. The ﬁrst task is to ﬁnd a sequence {yn}n∈ ⊂ 2s such that an analog of (6.2) is satisﬁed. It is convenient, for notational purposes only, to

identify functions from 2s to with functions from 2 to , and points in 2s with points in 2. This is done via the projection of 2s onto 2 × {0}.

From Lemmas 4.4 and 5.1, for the inequality in convolution form, we have

2

fn(x)fn(y) ψs(x)1/2ψs(y)1/2

fnσs ∗ fnσs 2L2( 3) ≤

σs ∗ σs(τ, ξ)dτdξ

![image 222](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile222.png>)

P2,2

(τ,ξ)

2

2s τ2 − |ξ|2

fn(x)fn(y) ψs(x)1/2ψs(y)1/2

π s P

=

dτdξ

![image 223](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile223.png>)

![image 224](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile224.png>)

![image 225](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile225.png>)

![image 226](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile226.png>)

(τ,ξ)

2,2

π s

fn 4L2. Since fnσs ∗ fnσs 2L2( 3) → π/s as n → ∞, we obtain

≤

![image 227](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile227.png>)

2

fn(x)fn(y) ψs(x)1/2ψs(y)1/2

2s τ2 − |ξ|2

dτdξ → 1 as n → ∞. (6.5)

![image 228](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile228.png>)

![image 229](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile229.png>)

![image 230](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile230.png>)

P2,2

(τ,ξ)

As in the proof of Lemma 4.4, the expression on the left hand side can be written as

2

2s τ2 − |ξ|2

fn(x)fn(y) ψs(x)1/2ψs(y)1/2

dτdξ

![image 231](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile231.png>)

![image 232](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile232.png>)

![image 233](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile233.png>)

P2,2

(τ,ξ)

fn2(x)fn2(y) ψs(x)ψs(y) P

2s τ2 − |ξ|2

δ τ − ψs(x) − ψs(y) ξ − x − y

dτdξ dxdy

=

![image 234](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile234.png>)

![image 235](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile235.png>)

![image 236](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile236.png>)

( 2)2

2,2

fn2(x)fn2(y) ψs(x)ψs(y)

2s ((ψs(x) + ψs(y))2 − |x + y|2)1/2

dxdy

=

![image 237](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile237.png>)

![image 238](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile238.png>)

( 2)2

fn2(x)fn2(y) ψs(x)ψs(y)

=

Ks(x, y)dxdy. Observe that

![image 239](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile239.png>)

( 2)2

fn2(x)fn2(y) ψs(x)ψs(y)

dxdy = fn 2L2( 2s) → 1 as n → ∞

![image 240](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile240.png>)

( 2)2

and

2s ((ψs(x) + ψs(y))2 − |x + y|2)1/2

1

Ks(x, y) :=

ds(x, y) + 1 ≤ 1 for all x, y ∈ 2. Equation (6.5) implies that

=

![image 241](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile241.png>)

![image 242](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile242.png>)

fn2(x)fn2(y) ψs(x)ψs(y)

Ks(x, y)dxdy → 1 as n → ∞.

![image 243](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile243.png>)

( 2)2

Let hn(y) = fn(y)2/ψs(y), so that limn→∞

hn(y)dy = 1. For ε > 0,

2

hn(x)hn(y)Ks(x, y)dxdy =

( 2)2

hn(x)hn(y)Ks(x, y)dxdy

ds(x,y)≤ε

+

hn(x)hn(y)Ks(x, y)dxdy

ds(x,y)>ε

1 ε + 1 d

≤ hn 2L1( 2) − 1 −

hn(x)hn(y)dxdy. Since the left hand side tends to 1 as n → ∞, we conclude that

![image 244](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile244.png>)

s(x,y)>ε

hn(x)hn(y)dxdy = 1. Using Fubini’s Theorem, we can write

lim

n→∞ ds(x,y)≤ε

hn(x)hn(y)dxdy =

ds(x,y)≤ε

hn(y)

2

hn(x)dxdy

ds(x,y)≤ε

≤ h L1( 2) sup

hn(x)dx. Then

y∈ 2 ds(x,y)≤ε

hn(x)dx = 1. (6.6) Equation (6.6) implies that there exists N(ε) ∈ such that for all n ≥ N(ε),

lim

sup

n→∞

y∈ 2 Bds(y,ε)

ε 2

hn(y)dy ≥ 1 −

sup

,

![image 245](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile245.png>)

y∈ 2 Bds(y,ε)

and hence there exists {ynε}n≥N(ε) ⊂ 2 such that

hn(y)dy ≥ 1 − ε.

Bds(ynε ,ε)

Applying (6.6) in this way, we obtain, for each ε > 0, a number N(ε) and a sequence {ynε}n≥N(ε).

The construction of the sequence {yn}n∈ is obtained by a diagonal process. We take a strictly decreasing sequence {εk}k∈ such that εk → 0 as k → ∞. This gives sequences {N(k)}k∈ and {ynk}n≥N(k),k≥0. We can take the sequence {N(k)}k∈

strictly increasing. For each n ≥ N(1), we let l(n) = sup{k ∈ : N(k) ≤ n}. Next, deﬁne {yn}n∈ by

ynl(n) if n ≥ N(1), y0 if n < N(1),

yn =

where y0 ∈ 2 is arbitrary, but ﬁxed.

Now let ε, r > 0 be given. Take k such that εk < min{ε, r}. For n ≥ N(k), l(n) ≥ k, so εl(n) ≤ εk < min{ε, r} and B

ds(ynl(n),εl(n)) hn(y)dy ≥ 1 − εl(n); hence

hn(y)dy ≥ 1 − εl(n) ≥ 1 − ε. Therefore, for every ε, r > 0, there exists N ∈ such that

hn(y)dy ≥

Bds(ynl(n),εl(n))

Bds(yn,r)

dy s2 + |y|2

|fn(y)|2

≥ 1 − ε. (6.7) for all n ≥ N.

![image 246](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile246.png>)

![image 247](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile247.png>)

Bds(yn,r)

To ﬁnish the proof we use the Lorentz invariance. This is better done without

identifying 2s with 2. So now we lift everything to 2s. Let Ds : {(ξ, τ) ∈ 2 × : τ > |ξ|}2 → be deﬁned by

- 1

![image 248](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile248.png>)

- 2s


((τ1 + τ2)2 − |ξ1 + ξ2|2)1/2 − 1. Observe that for every L ∈ L+, Ds(L(ξ1, τ1), L(ξ2, τ2)) = Ds((ξ1, τ1), (ξ2, τ2)). Let zn = (yn, ψs(yn)) ∈ 2s. We can write (6.7) as

Ds((ξ1, τ1), (ξ2, τ2)) =

|fn(z)|2dσs(z) ≥ 1 − ε. By the Lorentz invariance of Ds and σs, we have that for Ln ∈ L+ for which L−1

Ds(z,zn)≤r

n (zn) = (0, s) = P and for every ε, r > 0, there exists N ∈ such that

|L∗nfn(z)|2dσs(z) ≥ 1 − ε for all n ≥ N. (6.8)

Ds(z,P)≤r

- Property (iii) in Lemma 6.4 and (6.8) imply that for every ε, r > 0, there exists N ∈ such that


|L∗nf(z)|2dσs(z) ≥ 1 − ε for all n ≥ N.

|z−P|≤r

7. The two-sheeted hyperboloid In this section, we consider the two-sheeted hyperboloid

¯ ds = {(y, y′) ∈ d × : y′2 = s2 + |y|2} with measure

dydy′ s2 + |y|2

dydy′ s2 + |y|2

![image 249](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile249.png>)

![image 250](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile250.png>)

+ δ(y′ + s2 + |y|2)

σ¯s(y, y′) = δ(y′ − s2 + |y|2)

![image 251](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile251.png>)

![image 252](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile252.png>)

![image 253](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile253.png>)

![image 254](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile254.png>)

and the adjoint Fourier restriction operator deﬁned by T¯sf = fσ¯s, for f ∈ S( d+1). ¯ d s is the union of the two sheets

![image 255](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile255.png>)

d,±

s = {(y, y′) ∈ d × : y′ = ± s2 + |y|2}.

What in this section we are calling d,s + is what before we denoted by ds. In the previous section, we proved that for d,s + (and thus also for d,−

s ), extremizers do not exist for the cases (d, p) = (2, 4), (2, 6) and (3, 4). Here, we show that extremizers for ¯ d

s do not exist either and compute the best constants.

The adjoint Fourier restriction operator on d,s + is denoted by Ts, and the adjoint Fourier restriction operator on d,−

s by T−

s . For s = 1, we drop the subscript s. For A, B ⊆ d, we set A + B = {a + b : a ∈ A, b ∈ B} and −A = {−a : a ∈ A}.

- Lemma 7.1. For d ≥ 1,


![image 256](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile256.png>)

d,+

s + d,s + ⊆ {(ξ, τ) ∈ d × : τ ≥ (2s)2 + |ξ|2}, (7.1)

d,+

s + d,s − ⊆ {(ξ, τ) ∈ d × : |τ| ≤ |ξ|}, (7.2)

![image 257](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile257.png>)

s + d,s − ⊆ {(ξ, τ) ∈ d × : τ ≤ − (2s)2 + |ξ|2}. (7.3) Proof. To establish (7.1), let ξ = x + y and τ = ψs(x) + ψs(y). Thus

d,−

τ2 = (ψs(x) + ψs(y))2 = 2s2 + |x|2 + |y|2 + 2(s2 + |x|2)1/2(s2 + |y|2)1/2, while |ξ|2 = |x + y|2 = |x|2 + |y|2 + 2x · y. Then (7.1) is equivalent to the inequality

(s2 + |x|2)1/2(s2 + |y|2)1/2 ≥ s2 + x · y for all x, y ∈ d. (7.4)

Using x · y = |x||y| cosθ, where θ is the angle between x and y, we see that (7.4) is equivalent to

(s2 + a2)1/2(s2 + b2)1/2 ≥ s2 + ab for all a, b, s ≥ 0, which is easily shown to hold by squaring both sides.

We proceed in a similar way for (7.2). Let ξ = x + y and τ = ψs(x) − ψs(y). Then τ2 = 2s2 + |x|2 + |y|2 − 2(s2 + |x|2)1/2(s2 + |y|2)1/2. As before, (7.2) is equivalent to the inequality

−(s2 + |x|2)1/2(s2 + |y|2)1/2 ≤ −s2 + x · y for all x, y ∈ d, which in turn is equivalent to

(s2 + a2)1/2(s2 + b2)1/2 ≥ s2 + ab, which holds for all real numbers a, b, s ≥ 0.

s = − d,s +. Lemma 7.2. Let d ≥ 1,

As for (7.3), it follows from (7.1) observing that d,−

![image 258](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile258.png>)

d,+

s + d,s + + d,s + ⊆ {(ξ, τ) ∈ d × : τ ≥ (3s)2 + |ξ|2}, (7.5)

![image 259](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile259.png>)

d,−

s + d,s − + d,s − ⊆ {(ξ, τ) ∈ d × : τ ≤ − (3s)2 + |ξ|2}, (7.6)

![image 260](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile260.png>)

d,+

s + d,s + + d,s − ⊆ {(ξ, τ) ∈ d × : τ ≥ − s2 + |ξ|2}, (7.7)

![image 261](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile261.png>)

d,+

s + d,s − + d,s − ⊆ {(ξ, τ) ∈ d × : τ ≤ s2 + |ξ|2}. (7.8)

Proof. We know from Lemma 7.1 that

![image 262](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile262.png>)

d,+

s + d,s + ⊆ {(ξ, τ) : τ ≥ (2s)2 + |ξ|2}.

We start with (7.5). Setting ξ = x + y and τ ≥ ψ2s(x) + ψs(y) > 0 and squaring the latter inequality for τ gives

τ2 ≥ 5s2 + |x|2 + |y|2 + 2(4s2 + |x|2)1/2(s2 + |y|2)1/2. Then (7.5) follows from the inequality

(4s2 + |x|2)1/2(s2 + |y|2)1/2 ≥ 2s2 + x · y for all x, y ∈ d, which is equivalent to

(4s2 + a2)1/2(s2 + b2)1/2 ≥ 2s2 + ab, which is easy to verify for all a, b, s ≥ 0.

We now establish (7.7). Let ξ = x + y and τ ≥ ψ2s(x) − ψs(y). If τ ≥ 0, we are done. So, we suppose that 0 ≥ τ ≥ ψ2s(x) − ψs(y). Then

τ2 ≤ 5s2 + |x|2 + |y|2 − 2(4s2 + |x|2)1/2(s2 + |y|2)1/2, and (7.7) follows from the inequality

−(4s2 + |x|2)1/2(s2 + |y|2)1/2 ≤ −2s2 + x · y for all x, y ∈ d which is equivalent to

(4s2 + a2)1/2(s2 + b2)1/2 ≥ 2s2 + ab, which holds for all a, b, s ≥ 0.

Both (7.6) and (7.8) can be proved similarly or obtained from (7.5) and (7.7) using that d,−

s = − d,s +. For a function f ∈ L2( ¯ d

s), we write f = f+ + f−, where f+ is supported on d,s + and f− is supported on d,−

s . Then f 2L2(¯d

2( d,s +) + f− 2L

s) = f+ 2L

2( d,s −). s), f = 0. Then

- Proposition 7.3. Let d ∈ {2, 3} and f ∈ L2( ¯ d


3 2

T ¯sf 4L4( d+1) f −L4

H4d,4,s. (7.9) If equality holds in (7.9),

s) ≤

2( ¯ d

![image 263](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile263.png>)

s ) and Ts−f− L4( d+1) = Hd,4,s f− L2( d,−

Tsf+ L4( d+1) = Hd,4,s f+ L2( d,+

s ).

Moreover, if {fn}n∈ is an extremizing sequence for T¯s, then {fn,+/ fn,+ 2}n∈ and {fn,−/ fn,− 2}n∈ are extremizing sequences for Ts in d,s + and T−

s in d,−

s , respectively.

Proof. The proof of (7.9) is analogous to the argument in [5, pp. 754-755]. We restrict attention to the case s = 1, but the other cases follow in the same way or by the use of scaling. Observe that

Tf ¯ 4L4 = Tf+ + T−f− 4L4 = (Tf+ + T−f−)2 2L2

= (Tf+)2 + (T−f−)2 + 2(Tf+)(T−f−) 2L2.

Using the fact that product transforms into convolution under the Fourier transform, we see that the Fourier transforms of (Tf+)2, (T−f−)2 and (Tf+)(T−f−) are supported on d,+ + d,+, d,− + d,−, and d,+ + d,−, respectively. By Lemma 7.1, the pairwise intersections of these three sets have measure zero. Therefore,

Tf ¯ 4L4 = Tf+ 4L4 + T−f− 4L4 + 4 (Tf+)(T−f−) 2L2 (7.10) ≤ H4d,4( f+ 4L2 + f− 4L2 + 4 f+ 2L2 f− 2L2) (7.11) ≤

3 2

H4d,4( f+ 2L2 + f− 2L2)2 (7.12)

![image 264](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile264.png>)

3 2

H4d,4 f 4L2, (7.13) where we have used the sharp inequality (as in [5])

=

![image 265](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile265.png>)

3 2

(X + Y )2, X, Y ≥ 0, (7.14) where equality holds if and only if X = Y . Thus,

X2 + Y 2 + 4XY ≤

![image 266](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile266.png>)

Tf ¯ 4L4( d+1) f −L4

2(¯d) ≤

3 2

H4d,4. (7.15)

![image 267](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile267.png>)

For f = 0, equality holds in (7.15) if and only if it holds in (7.11) and (7.12). Equality holds in (7.11) if and only if Tf+ L4 = Hd,4 f+ L2( d,+), T−f− L4 = Hd,4 f− L2( d,−) and |Tf+| = λ|T−f−| a.e. in d+1 for some λ ≥ 0, and in (7.12) if and only if f+ 2 = f− 2. Note that equality in (7.12) implies that λ = 1.

Let {fn}n∈ be an extremizing sequence for T¯, so that limn→∞ Tf ¯ n L4( d) = H¯ d,4 and fn 2 ≤ 1. For the decomposition fn = fn,+ + fn,−, we see that

3 2

( fn,+ 4L2 + fn,− 4L2 + 4 fn,+ 2L2 fn,− 2L2) =

.

lim

![image 268](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile268.png>)

n→∞

This implies that if limn→∞ fn,+ L2 and limn→∞ fn,− L2 exist, then they must be equal, and thus equal to 1/√2. Therefore, any subsequence has a convergent subsequence with limit 1/√2. This implies the existence of both limits and

![image 269](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile269.png>)

![image 270](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile270.png>)

1 √2

. If we write

fn,− L2 =

fn,+ L2 = lim

lim

![image 271](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile271.png>)

![image 272](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile272.png>)

n→∞

n→∞

Tfn,+ L4 = anHd,4 fn,+ L2( d,+) and T−fn,− L4 = bnHd,4 fn,− L2( d,−),

then, as before, limn→∞ an fn,+ 2 = 1/√2, and so limn→∞ an = 1; similarly, limn→∞ bn = 1. Hence, {fn,+/ fn,+ 2}n∈ and {fn,−/ fn,− 2}n∈ are extremizing sequences for T and T− in d,+ and d,−, respectively.

![image 273](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile273.png>)

Corollary 7.4. For d ∈ {2, 3}, p = 4 and s > 0, H¯ d,4,s = (3/2)1/4Hd,4,s. Moreover, extremizers for the adjoint Fourier restriction inequality for ¯ d

s do not exist.

Proof. The only part missing is the lower bound for the value of the best constant. For this, take {fn,+}n∈ to be an extremizing sequence for Ts, then, identifying a function on d,±

s with a function from d to , set fn,−(y) = fn,+(−y), (the complex conjugate of fn,+ evaluated at −y), y ∈ d. Then {fn}n∈ = {(fn,+ + fn,−)/√2}n∈ is an extremizing sequence for T¯s in ¯ d

![image 274](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile274.png>)

![image 275](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile275.png>)

s, since inequalities (7.11) and (7.12) become

equalities in the limit n → ∞. Proposition 7.5. Let d ∈ {1, 2}, s > 0 and f ∈ L2(¯ d

s), f = 0. Then T ¯sf 6L6( d+1) f −L6

25 4

H6d,6,s. (7.16) In particular,

s) <

2( ¯ d

![image 276](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile276.png>)

1/3

5 2

H¯ d,6,s ≤

Hd,6,s. When d = 2 we have the reﬁnement

![image 277](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile277.png>)

H¯ 2,6,s ≤

√

5 8

![image 278](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile278.png>)

(4 + 3

2)

![image 279](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile279.png>)

1/6

H2,6,s.

Proof. The proof follows the same lines as [5, pp. 758-760], and Proposition 7.3 using Lemma 7.2. Since we want to highlight that (7.16) is a strict inequality and that a reﬁnement is possible we provide the details. Let us take s = 1 as other values of s follow by scaling. We start by writing Tf¯ = Tf+ + T−f−, so that

Tf ¯ 6L6 = Tf+ + T−f− 6L6 = (Tf+ + T−f−)3 2L2

= (Tf+)3 + 3(Tf+)2(T−f−) + 3(Tf+)(T−f−)2 + (T−f−)3 2L2.

The Fourier transform of the functions (Tf+)3, (Tf+)2(T−f−), (Tf+)(T−f−)2 and (T−f−)3 are supported on d,++ d,++ d,+, d,++ d,++ d,−, d,++ d,−+ d,− and d,− + d,− + d,−, respectively. Therefore, using Lemma 7.2 we obtain

Tf ¯ 6L6 = Tf+ 6L6 + T−f− 6L6 + 9 (Tf+)2(T−f−) 2L2 + 9 (Tf+)(T−f−)2 2L2

+ 6 (Tf+)3 , (Tf+)2(T−f−) + 6 (Tf+)(T−f−)2 , (T−f−)3

+ 18 (Tf+)2(T−f−) , (Tf+)(T−f−)2 .

(7.17)

Using the Cauchy-Schwarz and H¨older’s inequalities together with the sharp inequality for T and T− we obtain

Tf ¯ 6L6 ≤ H6d,6( f+ 6L2 + f− 6L2 + 9 f+ 4L2 f− 2L2 + 9 f+ 2L2 f− 4L2

(7.18)

+ 6 f+ 5L2 f− L2 + 6 f+ L2 f− 5L2 + 18 f+ 3L2 f− 3L2).

We now use the numerical inequality from [5, Lemma 6.6], namely, for X, Y ≥ 0 X6 + Y 6 + 9X4Y 2 + 9X2Y 4 + 6X5Y + 6XY 5 + 18X3Y 3 ≤

25 4

(X2 + Y 2)3, with equality if and only if X = Y . In this way we obtain

![image 280](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile280.png>)

25 4

25 4

Tf ¯ 6L6 ≤

H6d,6( f+ 2L2 + f− 2L2)3 =

H6d,6 f 6L2. (7.19)

![image 281](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile281.png>)

![image 282](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile282.png>)

From the ﬁrst part of Theorem 1.2 we have the inequalities Tf+ 6L6 ≤ H6d,6 f+ 6L2 and T−f− 6L6 ≤ H6d,6 f− 6L2, which are strict whenever f+ = 0 and f− = 0, so that if f = 0 then (7.19) is a strict inequality. More importantly, the inequalities

(Tf+)3 , (Tf+)2(T−f−) ≤ (Tf+)3 L2 (Tf+)2(T−f−) L2 (7.20) (Tf+)(T−f−)2 , (T−f−)3 ≤ (Tf+)(T−f−)2 L2 (T−f−)3 L2 (7.21)

(Tf+)2(T−f−) , (Tf+)(T−f−)2 ≤ (Tf+)(T−f−)2 L2 (T−f−)3 L2 (7.22)

are strict, whenever f+, f− = 0. Indeed, equality in the Cauchy-Schwarz inequality (7.20) forces (Tf+)3 = λ(Tf+)2(T−f−) for some λ ∈ C, λ = 0, which by the use of the Fourier transform implies that f+σ+ ∗ f+σ+ ∗ f+σ+ = λf+σ+ ∗ f+σ+ ∗ f−σ−, so that the support of f+σ+ ∗ f+σ+ ∗ f−σ− is contained in d,+ + d,+ + d,+, which is impossible if f+, f− = 0. A similar argument shows that (7.21) and (7.22) are strict inequalities when f+, f− = 0.

It was observed by D. Foschi in a related argument that it is possible to sharpen an inequality such as (7.20), (7.21) and (7.22) which then can be used to obtain a better bound for the best constant H¯ d,6. In what follows we adapt the argument to the hyperboloid in the case d = 2.

![image 283](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile283.png>)

Let us write f−(y) = f−(−y), where the overline denotes complex conjugation. Then

(Tf+)3 , (Tf+)2(T−f−) = (Tf+)3(T−f−), (Tf+)2 = (Tf+)3(T f−) , (Tf+)2

![image 284](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile284.png>)

= (2π)3 f+σ ∗ f+σ ∗ f+σ ∗ f−σ , f+σ ∗ f+σ ≤ (2π)3 σ(∗4) · σ(∗2) 1L/∞2 f+ 5L2 f− L2,

where in the last line we used an argument as in Lemma 4.1. From Lemma 5.1 we know

2π τ2 − |ξ|2

χ{τ≥√

σ ∗ σ(ξ, τ) =

22+|ξ|2}, while the fourth convolution can be calculated in a similar way

![image 285](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile285.png>)

![image 286](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile286.png>)

![image 287](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile287.png>)

![image 288](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile288.png>)

( τ2 − |ξ|2 − 4)2 τ2 − |ξ|2

χ{τ≥√

σ(∗4)(ξ, τ) = 4π3

42+|ξ|2}. Then

![image 289](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile289.png>)

![image 290](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile290.png>)

![image 291](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile291.png>)

![image 292](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile292.png>)

( τ2 − |ξ|2 − 4)2 τ2 − |ξ|2

σ(∗4) · σ(∗2) L∞( 3) = 8π4

![image 293](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile293.png>)

χ{√

![image 294](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile294.png>)

τ2−|ξ|2≥4}

= 8π4.

L∞( 3)

We obtain the inequality (Tf+)3, (Tf+)2(T−f−) ≤ 16

√

![image 295](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile295.png>)

2π5 f+ 5L2 f− L2, (7.23) and a similar method gives improved inequalities for (7.21) and (7.22) with the same constant on the right hand side. Note that 16√2π5 < H62,6 = (2π)5, so there is an improvement over using the Cauchy-Schwarz and H¨older’s inequality together with the sharp bound for T and T−. Using (7.17) and (7.23) we can obtain the analog of (7.18),

![image 296](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile296.png>)

Tf ¯ 6L6 ≤ H6d,6( f+ 6L2 + f− 6L2 + 9 f+ 4L2 f− 2L2 + 9 f+ 2L2 f− 4L2

√

√

√

![image 297](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile297.png>)

![image 298](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile298.png>)

![image 299](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile299.png>)

2 f+ L2 f− 5L2 + 9

2 f+ 3L2 f− 3L2). (7.24)

2 f+ 5L2 f− L2 + 3

+ 3

There is the sharp numerical bound X6+Y 6+9X4Y 2+9X2Y 4+3

√

√

√

√

5 8

![image 300](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile300.png>)

![image 301](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile301.png>)

![image 302](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile302.png>)

![image 303](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile303.png>)

2)(X2+Y 2)3, for all X, Y ≥ 0, with equality if and only if X = Y . It implies Tf ¯ 6L6 ≤

2X5Y +3

2XY 5+9

2X3Y 3 ≤

(4+3

![image 304](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile304.png>)

√

5 8

![image 305](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile305.png>)

2)H6d,6 f 6L2, which is the desired improvement over (7.19).

(4 + 3

![image 306](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile306.png>)

Proposition 7.3 gives the proof of the second part of Theorem 1.2 while Proposition 7.5 explains the comment in Remark 1.3.

8. Scaling

Here, we record the scaling for the family of operators {Ts}s>0. Recall from the Introduction that for s > 0, ds := {(y, s2 + |y|2) : y ∈ d} is equipped with the measure σs(y, y′) = δ(y′ − s2 + |y|2)dydy′/ s2 + |y|2. The operator Ts is deﬁned on S( d) by

![image 307](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile307.png>)

![image 308](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile308.png>)

![image 309](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile309.png>)

√

dy s2 + |y|2

![image 310](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile310.png>)

s2+|y|2f(y)

eix·yeit

Tsf(x, t) = fσs(−x, −t) =

.

![image 311](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile311.png>)

![image 312](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile312.png>)

d

We want to show that Hd,p,s deﬁned in (1.12) satisﬁes (1.13). With the change of variables v = sy in (1.1), we have

√

dy 1 + |y|2

![image 313](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile313.png>)

1+|y|2f(y)

eix·yeit

Tf(x, t) =

![image 314](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile314.png>)

![image 315](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile315.png>)

d

√

s−ddy 1 + s−2|y|2

![image 316](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile316.png>)

−1x·yeit

1+s−2|y|2f(s−1y)

eis

=

![image 317](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile317.png>)

![image 318](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile318.png>)

d

√

dy

![image 319](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile319.png>)

−1x·yeis

−1t

s2+|y|2s−1/2f(s−1y)

eis

= s−d+3/2

![image 320](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile320.png>)

![image 321](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile321.png>)

s2 + |y|2 from which it follows that sd−3/2Tf(sx, st) = Ts(s−1/2f(s−1·))(x, t) and

d

sd−3/2−(d+1)/p Tf Lp( d+1) = Tss−1/2f(s−1·) Lp( d+1).

On the other hand,

s−ddy 1 + s−2|y|2

dy 1 + |y|2

|f(y)|2

|f(s−1y)|2

=

![image 322](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile322.png>)

![image 323](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile323.png>)

![image 324](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile324.png>)

![image 325](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile325.png>)

d

d

dy s2 + |y|2

|s−1/2f(s−1y)|2

= s−d+2

,

![image 326](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile326.png>)

![image 327](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile327.png>)

d

that is, f L2(σ) = s−(d−2)/2 s−1/2f(s−1·) L2(σs). Thus

s(d−1)/2−(d+1)/p Tf Lp( d+1) f −L21(σ) = Tss−1/2f(s−1·) Lp( d+1) s−1/2f(s−1·) −L21(σ

s), and it follows that for all s > 0,

Hd,p,s = s(d−1)/2−(d+1)/pHd,p. (8.1)

9. Some explicit calculations for the case d = 2 The exponential integral function Ei(x), x = 0, is deﬁned by

Ei(x) = −

∞

e−t t

dt =

![image 328](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile328.png>)

−x

x

et t

dt (9.1)

![image 329](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile329.png>)

−∞

where the principal value is taken for x > 0.

√

Lemma 9.1. Let a > 0 and fa(y) = e−a

![image 330](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile330.png>)

s2+|y|2, y ∈ 2. Then

Tsfa 6L6( 3) fa −L26(σ

s) = (2π)5(1 − 6as − 36a2s2e6as Ei(−6as)), and (9.2) Tsfa 4L4( 3) fa −L24(σ

23π4 s

(−4ase4as Ei(−4as)). (9.3)

s) =

![image 331](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile331.png>)

Proof. We ﬁrst compute the L2(σs)-norm of fa,

fa 2L2(σs) =

2

= 2π

s

√

s2+|y|2 dy s2 + |y|2

![image 332](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile332.png>)

e−2a

= 2π

![image 333](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile333.png>)

![image 334](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile334.png>)

∞

π a

e−2ardr =

e−2as.

![image 335](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile335.png>)

∞

√s2+r2 r √s2 + r2

![image 336](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile336.png>)

e−2a

dr

![image 337](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile337.png>)

![image 338](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile338.png>)

0

The formulas in (9.2) and (9.3) are easier to compute in their equivalent convolution form. Let ga(ξ, τ) = e−aτ and observe that faσs ∗faσs = gaσs ∗ gaσs and faσs ∗ faσs ∗ faσs = gaσs ∗ gaσs ∗ gaσs. Then, because ga is the exponential of a linear function, gaσs ∗ gaσs(ξ, τ) = ga(ξ, τ) σs ∗ σs(ξ, τ) and gaσs ∗ gaσs ∗ gaσs(ξ, τ) = ga(ξ, τ) σs ∗ σs ∗

σs(ξ, τ). Therefore, faσs ∗ faσs ∗ faσs 2L2( 3)

2

3s τ2 − |ξ|2

χ{τ≥√

e−2aτ(2π)4 1 −

=

(3s)2+|ξ|2}dτdξ

![image 339](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile339.png>)

![image 340](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile340.png>)

![image 341](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile341.png>)

× 2

√

![image 342](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile342.png>)

2

τ2−(3s)2

∞

3s √τ2 − r2

e−2aτ 1 −

= (2π)5

rdrdτ

![image 343](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile343.png>)

![image 344](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile344.png>)

0

3s

√

![image 345](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile345.png>)

τ2−(3s)2

∞

r √t2 − r2

r τ2 − r2 − 6s

= (2π)5

e−2aτ r + (3s)2

drdτ

![image 346](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile346.png>)

![image 347](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile347.png>)

![image 348](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile348.png>)

3s

0

∞

= (2π)5

e−2aτ(12(τ2 − (3s)2) + (3s)2(log τ − log(3s)) − 6s(τ − 3s))dτ

![image 349](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile349.png>)

3s

∞

∞

- 1

![image 350](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile350.png>)

- 2


= (2π)5

e−2aττ2dτ + (3s)2

e−2aτ log τdτ

3s

3s

∞

∞

e−2aττdτ − (92s2 + (3s)2 log(3s))

e−2aτdτ

− 6se−6as

![image 351](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile351.png>)

3s

0

e−6as(1 + 6as(1 + 3as)) 8a3

6se−6as 4a2 −

e−6as log(3s) − Ei(−6as) 2a −

= (2π)5

+ (3s)2

![image 352](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile352.png>)

![image 353](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile353.png>)

![image 354](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile354.png>)

e−6as 2a

9 2

s2 + (3s)2 log(3s)

.

![image 355](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile355.png>)

![image 356](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile356.png>)

Rearranging terms, we have

faσs ∗ faσs ∗ faσs 2L2( 3) = (2π)5e−6as

Ei(−6as)e6as 2a −

1 8a3 − (3s)2

6s 8a2

![image 357](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile357.png>)

![image 358](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile358.png>)

![image 359](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile359.png>)

.

Thus

Ei(−6as)e6as 2a −

1 8a3 − (3s)2

6s 8a2

faσs ∗ faσs ∗ faσs 2L2( 3) fa −L26(σ

s) = (2π)5π−3a3

![image 360](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile360.png>)

![image 361](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile361.png>)

![image 362](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile362.png>)

= (2π)2(1 − 6as − 36a2s2e6as Ei(−6as)). For the case of L4( 3),

(2π)2 τ2 − |ξ|2

χ{τ≥√

faσs ∗ faσs 2L2( 3) =

e−2aτ

(2s)2+|ξ|2}dτdξ

![image 363](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile363.png>)

![image 364](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile364.png>)

× 2

√

![image 365](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile365.png>)

τ2−(2s)2

∞

r τ2 − r2

e−2aτ

= (2π)3

drdτ

![image 366](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile366.png>)

0

2s

e−4as 2a

e−4as log(2s) − Ei(−4as) 2a − log(2s)

= (2π)3

![image 367](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile367.png>)

![image 368](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile368.png>)

Ei(−4as) 2a

= −(2π)3

.

![image 369](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile369.png>)

Thus

Ei(−4as) 2π2

faσs ∗ faσs 2L2( 3) fa −L24(σ

s) = −(2π)3a

e4as

![image 370](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile370.png>)

π s

(−4ase4as Ei(−4as)).

=

![image 371](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile371.png>)

- Proof of Lemma 5.4. Using the expressions in Lemma 9.1, we obtain

lim

a→0+

Tsfa 6L6( 3) fa −L26(σ

s) = lim

a→0+

(2π)5(1 − 6as − 36a2s2e6as Ei(−6as)) = (2π)5

and

lim

a→∞

Tsfa 4L4( 3) fa −L24(σ

s) = lim

a→∞

23π4 s

![image 372](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile372.png>)

(−4ase4as Ei(−4as)) =

23π4 s

![image 373](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile373.png>)

.

Remark 9.2.

- 1. It is not hard to see that the function a  → 1 − a + a2ea Ei(−a) is strictly decreasing for a ∈ [0, ∞) and tends to 0 as a → ∞ and to 1 as a → 0+. Thus

Tsfa 6L6( 3) fa −L26(σ

s) is a strictly decreasing function of a, for each ﬁxed s.

- 2. The function a  → −aea Ei(−a) is strictly increasing for a ∈ [0, ∞) and tends


to 0 as a → 0+ and to 1 as a → ∞. Thus Tsfa 4L4( 3) fa −L24(σ

s) is a strictly increasing function of a, for each ﬁxed s.

10. Some explicit calculations for the case d = 3

- Proof of Lemma 5.5. For the L2(σs)-norm of fa, we have


fa 2L2(σs) =

3

= 4π

s

√

s2+|y|2 dy s2 + |y|2

![image 374](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile374.png>)

e−2a

= 4π

![image 375](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile375.png>)

![image 376](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile376.png>)

√

∞

4π a2

![image 377](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile377.png>)

e−2au

u2 − s2du =

![image 378](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile378.png>)

∞

√s2+r2 r2 dr √s2 + r2

![image 379](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile379.png>)

e−2a

![image 380](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile380.png>)

![image 381](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile381.png>)

0

∞

![image 382](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile382.png>)

e−2x x2 − (as)2dx.

as

Then

a2 π

fa 2L2(σs) = 1. Using the convolution form of the inequality, our goal is to show lim

lim

![image 383](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile383.png>)

a→0+

a4 faσs ∗ faσs 2L2( 4) = 2π3.

a→0+

As in the proof of Lemma 9.1,

4s2 τ2 − |ξ|2

χ{τ≥√

e−2aτ(2π)2 1 −

faσs ∗ faσs 2L2( 4) =

(2s)2+|ξ|2}dτdξ

![image 384](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile384.png>)

![image 385](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile385.png>)

× 3

√

![image 386](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile386.png>)

τ2−(2s)2

∞

4s2 τ2 − r2

= (2π)24π

r2drdτ

e−2aτ 1 −

![image 387](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile387.png>)

2s

0

∞

1 3

3

(τ2 − (2s)2)

2 + 4s2((τ2 − (2s)2)1/2

= 16π3

e−2aτ

![image 388](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile388.png>)

![image 389](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile389.png>)

2s

![image 390](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile390.png>)

τ + τ2 − (2s)2 2s

− τ log

dτ

![image 391](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile391.png>)

∞

4s2 a

16π3 a

1 3a3

3

e−2τ

(τ2 − (2as)2)

((τ2 − (2as)2)1/2

2 +

=

![image 392](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile392.png>)

![image 393](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile393.png>)

![image 394](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile394.png>)

![image 395](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile395.png>)

2as

![image 396](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile396.png>)

τ + τ2 − (2as)2 2as

τ a

dτ. Multiplying by a4 and taking the limit as a → 0+ gives

log

−

![image 397](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile397.png>)

![image 398](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile398.png>)

∞

16π3 3

a4 faσs ∗ faσs 2L2( 4) =

e−2ττ3dτ = 2π3.

lim

![image 399](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile399.png>)

a→0+

0

Acknowledgments. The author thanks his dissertation advisor, Michael Christ, for many helpful comments and suggestions.

References

- [1] E. Carneiro, A sharp inequality for the Strichartz norm, Int. Math. Res. Not. 16 (2009), 3127– 3145.
- [2] M. Christ and S. Shao, Existence of extremals for a Fourier restriction inequality, Anal. PDE 5 (2012), no. 2, 261-312.
- [3] L. Fanelli, L. Vega, and N. Visciglia, On the existence of maximizers for a family of restriction theorems, Bull. London Math. Soc. 43 (2011), no. 4, 811-817.
- [4] , Existence of maximizers for Sobolev-Strichartz inequalities, Adv. Math. 229 (2012), no. 3, 1912-1923.

![image 400](<2011-quilodrn-nonexistence-extremals-adjoint-restriction_images/imageFile400.png>)

- [5] D. Foschi, Maximizers for the Strichartz inequality, J. Eur. Math. Soc. 9 (2007), no. 4, 739–774.
- [6] J. Kato and T. Ozawa, Endpoint Strichartz estimates for the Klein-Gordon equation in two space dimensions and some applications, J. Math. Pures Appl. (9) 95 (2011), no. 1, 48–71.
- [7] W. Magnus and F. Oberhettinger, Formulas and Theorems for the Special Functions of Mathematical Physics, Chelsea Publishing Company, New York, N.Y., 1949. Translated by John Wermer.
- [8] A. Moyua, A. Vargas, and L. Vega, Restriction theorems and maximal operators related to oscillatory integrals in 3, Duke Math. J. 96 (1999), no. 3, 547–574.
- [9] F. Oberhettinger and L. Badii, Tables of Laplace transforms, Springer-Verlag, New York, 1973.
- [10] R. Quilodr´an, On extremizing sequences for the adjoint restriction inequality on the cone, J. London Math. Soc. 87 (2013), no. 1, 223-246.
- [11] J. Ramos, A reﬁnement of the Strichartz inequality for the wave equation with applications, Adv. Math. 230 (2012), no. 2, 649–698.
- [12] M. Reed and B. Simon, Methods of modern mathematical physics. II. Fourier analysis, selfadjointness, Academic Press, New York, 1975.


- [13] R. S. Strichartz, Restrictions of Fourier transforms to quadratic surfaces and decay of solutions of wave equations, Duke Math. J. 44 (1977), no. 3, 705–714.
- [14] G. N. Watson, A Treatise on the Theory of Bessel Functions, Cambridge University Press, Cambridge, England, 1944.


Department of Mathematics, University of California, Berkeley, CA 94720-3840, USA

E-mail address: rquilodr@math.berkeley.edu

