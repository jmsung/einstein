---
type: source
kind: paper
title: Concentration inequalities for Paley-Wiener spaces
authors: Syed Husain, Friedrich Littmann
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2210.10029v2
source_local: ../raw/2022-husain-concentration-inequalities-paley-wiener-spaces.pdf
topic: general-knowledge
cites:
---

# arXiv:2210.10029v2[math.CA]25Oct2022

## CONCENTRATION INEQUALITIES FOR PALEY-WIENER SPACES

SYED HUSAIN, FRIEDRICH LITTMANN

Abstract. This article considers the question of how much of the mass of an element in a Paley-Wiener space can be concentracted on a given set. We seek bounds in terms of relative densities of the given set. We extend a result of Donoho and Logan from 1992 in one dimension and consider similar results in higher dimensions.

1. Introduction

Let M be a convex body in Rd, and let Bp(M), 1 ≤ p ≤ ∞, be the Paley-Wiener space of elements from Lp(Rd) with distributional Fourier transform supported in M. The Fourier transform Ff is given by

Ff(ϕ) =

ϕ(t)f(t)dt

R

for a Schwarz function ϕ. (We use ϕ(t) = ϕ(x)e−2πixtdx.) We write Bp(τ) if M is the ball with center at the origin and radius τ.

Let N and Wδ ⊆ Rd be measurable and set Wδ(x) = x + Wδ. (In this article, Wδ is either a ball or a cube.) We consider the problem of ﬁnding a constant C(M,δ) > 0 such that

- (1) |N ∩ Wδ(x)| G 1 for all G ∈ B1(M).

Here |.| denotes Lebesgue measure and χN is the characteristic function of N. We emphasize that the constant is not allowed to depend on N.

This question was studied by Donoho and Logan [5] in dimension d = 1 in connection with recovery of a bandlimited signal that is corrupted by noise. In their setting, an unknown noise n ∈ L1(R) is added to a known signal F ∈ B1([−τ,τ]), and they investigate suﬃcient conditions under which the best approximation F ∈ B1([−τ,τ]) to F +n satisﬁes F = F, i.e., when F can be perfectly recovered from knowledge of F + n through best L1-approximation.

Denoting now by N the support of n, it is a remarkable fact that the concentration condition

GχN 1 G 1

<

- 1

- 2


- (2) for all G ∈ B1(M)

is suﬃcient to conclude that F = F. The argument can be found in several places, e.g., Donoho and Stark [6, Section 6.2], who refer to it as Logan’s phenomenon. (Logan’s thesis [9] appears to contain the earliest record of this argument.) It was shown in [5, Theorem 7]

that (1) holds for Wδ(x) = [x − 2δ,x + 2δ] with C([−τ,τ],δ) =

πτ sin(πτδ)

- (3) ,


GχN 1 ≤ C(M,δ) sup x∈Rd

1

### and combining this with (2), it is evident that this gives F = F provided the relative density (or Nyquist density) of the support of the noise satisﬁes

sin(πτδ) 2πτδ

δ−1 sup x∈R

|N ∩ [x,x + δ]| <

.

We mention that conditions to recover an element of a closed subspace of an L1 space that has been corrupted by a sparse L1-noise have been investigated in many diﬀerent settings, and concentration inequalities lead frequently to suﬃcient conditions. (This relies on the fact that if a set N satisﬁes an analogue of (2) for all G in a given closed subspace of an L1-space, then the zero function is the closest element from the subspace to every L1 function with support contained in N.) For interested readers we refer to Cand`es, Romberg, and Tao [3], Benyamini, Kro´, and Pinkus [2], Abreu and Speckbacher [1], and the references therein.

2. Results

There are two questions that this article seeks to address. First, it is clear that the shape of the bound in (3) requires δτ < 1. In contrast, it was shown for p = 2 in [5, Theorem 4] that for any positive τ and δ

GχN 22 ≤ τ + δ−1 sup x∈R

|N ∩ [x,x + δ]| G 22

for all G ∈ B2(τ) (with constants adjusted due to the diﬀerent normalization of the Fourier transform) which suggests that an inequality with constant c(τ +δ−1) should also be true for p = 1. Our ﬁrst result conﬁrms that this is the case.

- Theorem 1. Let N be the support of n ∈ L1(R). Then for all G ∈ B1(τ)

GχN 1 ≤ Cτ,δ sup x∈R

|N ∩ [x,x + δ]| G 1.

where Cτ,δ ≤ 1380(τ + δ−1) for all positive τ and δ. The bound may be improved to Cτ,δ ≤

- 5 2(τ + δ−1) for τδ ≥ 2. Moreover, limτδ→∞ Cτ,δ = 2.


As is usual with this method, the bounds only become eﬀective when the density is a fraction of the reciprocal of the type τ. If one is interested in bounds for GχN 1/ G 1 at larger densities, a version of the Logvinenko-Sereda theorem from O. Kovrijkine [8] gives non-trivial bounds whenever the density is smaller than 11. The constants are not eﬀective and don’t yield concrete bounds to decide when the quotient is < 1/2.

Our second result deals with reconstruction in higher dimensions. We investigate the

case when M is a cube and Wδ(0) is a ball with center at the origin, and we indicate the obstructions that we encountered when taking M to be a ball with center at the origin. We

denote by Jν the Bessel function of the ﬁrst kind and by jν(k) its kth positive zero.

- Theorem 2. Let d ∈ N and let N ⊆ Rd). If αλ < jd/2(1)d−21, then for all G ∈ B1([λ,λ]d)


√

dλ)d/2 αd/2Jd/2(2π

(

√

GχN 1 ≤

|N ∩ B(x,α)| G 1.

sup

dαλ)

x∈Rd

1The authors are grateful to Walton Green to draw their attention to [8].

Analogously to dimension one, for a convex body K we deﬁne the maximum Nyquist density of N (relatively to K) by

1 |K|

|N ∩ (u + K)|.

ρ(N,K) =

sup

u∈Rd

We compare the result of Theorem 2 to the case where the window K is a hypercube of side length δ, which is an extension of the L1 reconstruction result by [5]. The zero jp(1) has an asymptotic expansion given in [4] by

jp(1)

p 2

1 4

+

π.

Denote the ball of radius r centered at origin by B(0,r), and the volume of a ball with radius α in d-dimensions by Vd(α). It is given by Vd(α) = Γ(d/πd/2+1)2 αd. When the window is a ball of radius α, perfect reconstruction is possible if the maximum Nyquist density satisﬁes

√

dαλ) 2(πα

Γ(d/2 + 1)Jd/2(2π

√

,

ρ(N,B(0,α)) <

dλ)d/2

where α < j2d/π√2(1)dλ. For λδ < 2π, the corresponding density bound is

d

- 1

- 2


sin(λδ/2) λδ/2

ρ(N,[−δ/2,δ/2]d) <

.

The support of the Fourier transform for both the problems is same, that is, [−λ,λ]d. In the second case, we consider the ball just outside the cube such that the radius satisﬁes α = δ

√

d 2 . Let δ = 2π12. For large d, the bound is asymptotically

Γ(d/2 + 1)Jd/2(d/2) 2(d/4)d/2

ρ(T,B(0,α),F) <

√

πd 2 de d/2 2 d4 d/2

Γ(1/3) 21/3 · 31/6 · π.d1/3

∼

d/2

2 e

∼ d1/6

The Nyquist density for the cube window satisﬁes ρ(T,[−δ/2,δ/2]d,F) <

- 1

- 2


4π2 sin(1/4π2) d .

The bound for the Nyquist density of the cube window remains larger than the bound for the Nyquist density of ball window for any d in this case.

Third, we set the volume of the cube is equal to the volume of the ball. Then the radius α of the ball satisﬁes

Γ(d/2 + 1) πd/2

α = δ d

. Using Sterling’s approximation, we get

d/2

d 2πe

α δ d

(πd)1/2.

√2πe

Let δ =

4π2 . For large d, the Bessel function in the Nyquist density of the ball window satisﬁes

Jd/2(2π2√α) = Jd/2(d · π1/2d · d1/2d/2) → Jd/2(d/2), since π1/2d · d1/2d → 1 for large d. The bound for the Nyquist density of the ball window is then

Γ(d/2 + 1)Jd/2(d/2) 2 π2

ρ(T,B(0,α),F) <

√

√2πe 4π2√π

d Γ(d/2 + 1)

d

d/2 1

Γ(1/3).π1/4 2 · 21/3 · 31/6 · π

4 2e

∼

d1/12 Tor the cube window, the suﬃcient bound for reconstruction is

sin(√2πe/8π) √2πe/8π

d

- 1

- 2


ρ(T,[−δ/2,δ/2]d,F) <

.

In this case also, the Nyquist density for the cube window remains larger than the Nyquist density of ball window for any dimension d.

3. Proof of Theorem 1

We brieﬂy review a general approach to prove inequalities of the above form introduced by Donoho and Logan in [5]. Construct a kernel K(x,y) so that f  → Tf given by

Tf(y) = K(x,y)f(x)dx

deﬁnes a bounded invertible transformation when restricted to B1(τ). Then a change of integration order gives

|G(x)|dx ≤

N

N

|K(x,y)|T−1G(x)|dxdy

K(x,y)dy T−1 G 1.

≤ sup

x N

If K(x,y) = g(x − y) for some g ∈ L∞ with supp(g) ⊆ Wδ(0), then the supremum may be further estimated by g ∞ supx |N ∩ Wδ(x)|, where T = Tg is now the convolution operator Tgf = f ∗ g restricted to B1(τ). For given g the size of the constant depends then only on

g ∞ Tg−1 , and (2) shows that we need sup

1 2 g ∞ Tg−1

|N ∩ Wδ(x)| <

.

x

Thus, it is the task to construct g as above where g ∞ Tg−1 is as small as possible. The choice in [5] was g = χ[−δ

2,2δ], which is optimal for δτ ≤ 21, gives a non-optimal bound for

- 1

- 2 < δτ < 1, and fails to give a bound for δτ ≥ 1. This can be traced back to the fact that g(δ) = 0.


To create an auxiliary function g with computable product g ∞ Tg−1 , Logan and Donoho observed that if 1/ g is positive and convex up on an interval I = [−a,a] with center at the origin, then the periodic extension of 1/ g restricted to I is the Fourier transform of a measure ν that acts as the inverse operator of convolution with g on B1(a) and has total variation

1.0

6

0.8

0.6

4

0.4

2

0.2

-1.0 -0.5 0.5 1.0

-6 -4 -2 2 4 6

Figure 1. The transform pair g4(x) and g4(t)

|ν| = 1/ g(a). (In fact, ν is the minimal extrapolation of 1/ g restricted to I in the sense of Beurling.) Our choice of g is based on this idea. We deﬁne for τ > 0 and real x a function gτ, supported on [−1,1], by

cos2π(τ + 1)x − cos2πτx 4π2x2

gτ(x) = −2(1 − |x|)

χ[−1,1](x).

The Fourier transform of gτ has the useful property that the sum of its partials with respect to t and τ has a simple integral representation. Proposition 1. For any t and τ

∂ ∂t

∂ ∂τ

( gτ(t)) +

( gτ(t)) =

2π(t+τ+1)

sin2 u u2

du.

2π(t+τ)

Proof. For ease of notation we set G(t,τ) = gτ(t), and we denote ﬁrst partials by Gt and Gτ. Writing

cos2π(τ + 1)x − cos2πτx (−2πix)2

gτ(x) = 2(1 − |x|)

χ[−1,1](x) and using that gτ(x) is even, we have Gt(t,τ) =

1

(−2πix)gτ(x)e−2πixtdx

−1

1

(−2πix)gτ(x)(−isin(2πxt))dx

=

−1

- 1

−1

- 2(1 − |x|)


cos(2π(τ + 1)x) − cos(2πτx) 2πx

=

sin(2πxt)dx

1

cos(2π(τ + 1)x) − cos(2πτx) 2πx

(1 − x)

sin(2πxt)dx. Similarly,

= 4

0

Gτ(t,τ) =

= 4

1

∂ ∂τ

(gτ(x))e−2πixtdx

−1

1

sin(2π(τ + 1)x) − sin(2πτx) 2πx

(1 − x)

cos(2πxt)dx.

0

The integrals have representations in terms of the sine-integral Si(u) = 0 u sin(w)/wdw. A direct calcuation gives

1

sin(2πbx) x

dx = Si(2π(a + b)) − Si(2π(a − b))

cos(2πax)

2

0

1

cos(2π(a − b)) 2π(a − b) −

b π(a − b)(a + b)

cos(2π(a + b)) 2π(a + b)

cos(2πax)sin(2πbx)dx = −

. We obtain

2

+

0

sin2(π(t + τ)) (t + τ)(t + τ + 1)

2 π2

+ π Si(2π(t + τ + 1)) − π Si(2π(t + τ)

Gt(t,τ) + Gτ(t,τ) =

π(t+τ+1)

2π(t+τ+1)

sin2 u u

∂ ∂u

2 π

sinw w

2 π

−

du +

=

dw

π(t+τ)

2π(t+τ)

π(t+τ+1)

sin2 u u2

2 π

du after substituting w = 2u and combining the integrands. Corollary 1. (1) gτ ∞ = gτ(0) = 2τ + 1.

=

π(t+τ)

- (2) The function τ  → gτ(0) is positive, monotonically increasing, and has limit 1 as τ → ∞. Moreover,

g0(0) > 0.65, g1(1) > 0.8.

- (3) t  → gτ(t) −1 is positive and convex (up) on [−τ,τ].


Proof. Property (1) is obtained by direct calculation. For the proof of (2) it follows from symmetry of t  → gτ(t) that g τ(0) = 0, and hence Proposition 1 gives ∂/∂τ gτ(0) > 0. Direct calculations give the claimed bounds.

Regarding (3), we require an explicit representation of g τ(t). It follows from gτ(x) = 2(1 − |x|)

cos2π(τ + 1)x − cos2πτx (−2πix)2

χ[−1,1](x) that

1

(−2πix)2gτ(x)e−2πixtdx

g τ(t) =

−1

2

2

sinπ(t − τ) π(t − τ)

sinπ(t + τ) π(t + τ)

= −

−

(4)

2

2

sinπ(t − τ − 1) π(t − τ − 1)

sinπ(t + τ + 1) π(t + τ + 1)

+

+

sin2(π(t − τ))(2(t − τ) − 1) (t − τ)2(t − τ − 1)2 −

sin2(π(t + τ))(2(t + τ) + 1) (t + τ)2(t + τ + 1)2

=

.

Since the ﬁrst term is negative for t − τ < 1/2 and the second term is positive for t + τ > −1/2, it follows that

- 1

- 2


g τ(t) < 0 for − τ − 21 < t < τ +

.

Multivariate chain rule and Proposition 1 show that

∂ ∂τ

( gτ(τ)) > 0,

and since g0(0) > 0, it follows that gτ(τ) > 0 for all τ. Since gτ is concave down on [−τ,τ], it follows that gτ(t) > 0 for t ∈ [−τ,τ]. It follows that the second derivative of t  → ( gτ(t))−1 is positive for |t| ≤ τ.

Proof of Theorem 1. Setting gτ,δ(x) = gτδ/2(2x/δ), we observe that gτ,δ is supported on [−δ/2,δ/2], and

δ 2

gτ,δ(t) =

gτδ/2(δt/2).

It follows that t  → ( gτ,δ(t))−1 is positive and convex up for |t| ≤ τ. Let an = an(τ,δ) be the Fourier coeﬃcients satisfying

1 gτ,δ(t)

aneπiτt n

=

n∈Z

for |t| ≤ τ. Positivity and convexity imply that |an| = (−1)nan. Deﬁne a measure ν = ντ,δ on R for any Borel set A by

ν(A) =

anδn/(2τ)(A)

n∈Z

where δb is the Dirac measure at b ∈ R. We observe that ν(t) = 1/ gτ,δ(t) for |t| ≤ τ, and the total variation satisﬁes

1 gτδ/2(τδ/2)

an(−1)n =

|ν|(R) =

|an| =

.

n∈Z

n∈Z

It follows that convolution with ν is the inverse operator of convolution with gτ,δ when

restricted to PWτ1. Moreover, for gτ,δ the choice of ν is optimal, since the value of the Fourier transform of ν is always a lower bound for the total variation.

It follows that

1 gτδ/2(τδ/2)

Tg−1

. We observe the identities

=

τ,δ

2τ + 2δ−1 gτδ/2(τδ/2)

gτδ/2 ∞ gτδ/2(τδ/2)

gτ,δ ∞ gτ,δ(τ)

2 δ

=

=

.

For τ > 0 and δ > 0 we use the inequality gτδ/2(τδ/2) ≥ g0(0) > 0.65. For τδ ≥ 2, we may use the lower bound g1(1) > 0.8 instead.

4. Proof of Theorem 2

As in the ﬁrst section, the main task lies in computing a minimal extrapolation of 1/ g restricted support of the Fourier transform for a suitably chosen function g. For x ∈ Rd we consider

gα(x) = χB(0,α)(x) whose Fourier transform for t ∈ Rd is

αd/2Jd/2(2πα|t|) |t|d/2

.

gα(t) =

To construct a minimal extrapolation of 1/ gα restricted to [−τ,τ]d, we need facts from the theory of Laguerre-P´lya entire functions. We follow [7]. An entire function E belongs to the Laguerre-P´lya class E if and only if it has the form

∞

s ak

s

E(s) = ecs2+bs

1 −

e

ak ,

k=1

where c ≥ 0, b, ak(k = 1,2,···) are real, and

∞

1 a2k

k=1

< ∞.

- Lemma 1. There exists a non-negative, integrable function G such that for x ∈ (−jp(1),jp(1))


0

xp Jp(x)

e−x2tG(t)dt.

=

−∞

Proof. The Bessel function Jp(x) has an inﬁnite product representation [4, Section 10.21(iii)]. Dividing each side by xp gives us

∞

x2 jp,k2

Jp(x) xp

1 2pΓ(p + 1)

1 −

=

k=1

∞

∞

1 2pΓ(p + 1)

x jp,k

x jp,k

e−x/jp,k

ex/jp,k

1 −

=

1 +

k=1

k=1

- Substituting x = √y in the inﬁnite product representation of Jpx(px) gives us


Jp(√y) yp/2

∞

y jp,k2

1 2pΓ(p + 1)

1 −

=

k=1

which is an entire function and belongs to class E. Let E(x) = Jpx(px). Then by [7, Theorem

- 6.1] the function 1/E(√y) has a Laplace transform representation given by


1 E(√y)

e−ytG(t)dt,

=

R

where G(t) ∈ C∞ is a nonnegative, integrable function and the integral converges in the largest vertical strip which contains the origin and is free of zeroes of E(√y), which is −∞ < y < jp,21. Next, we want to determine the values of t for which G(t) > 0. This result is obtained using Corollary 3.1 (Chapter 5 in [7]). Note that E(√y) can be expressed as

∞

E(√y) =

y jp,k2

1 2pΓ(p + 1)

1 −

k=1

∞

1 2pΓ(p + 1)

1

=

∞

−

(y/jp,k)

k=1

e

k=1

y jp,k2

1 −

e(y/jp,k)

The function E(√y) has no negative zeroes. Therefore, in the setting of Corollary 3.1, α1 = −∞ and b = −

∞

1

jp,k. Therefore G(t) > 0 if t ∈ (−∞,0)) and G(t) = 0 otherwise, giving us for y ∈ (0,jp,21),

k=1

0

1 E(√y)

e−ytG(t)dt.

=

−∞

- Substituting y = x2 gives the claim.


√

dαλ < jd/2(1). We construct a (signed) measure ν that is an inverse transform on B1([−λ,λ]d) of convolution with gα satisfying

Let λ > 0 and α > 0 with 2π

√

dλ)d/2 αd/2Jd/2(2π

(

√

f ∗ ν 1 ≤

f 1,

dλα)

and we show that the constant is best possible among all inverse transformations of convolution with gα on B1([−λ,λ]d). We expand 1/ gα restricted to [−λ,λ]d into its Fourier series

1 gα(t)

Hα(n)e2πint

=

n∈Zd

where

d

|x|d/2 αd/2Jd/2(2πα|x|)

- 1

- 2λ


e−iπλnxdx.

Hα(n) =

[−λ,λ]d

- Lemma 2. The coeﬃcients satisfy H(n1,...,nd) = (−1)n1+...+nd|H(n1,...,nd)|


Proof. The restrictions on αλ imply that the following integrals converge absolutely. Inserting the Schoenberg representation (??) gives with n = (n1,...,nd)

 

 dt

d

d 0

1 2√2παλ

e−x2jte−iπλnjxjdxj

Hα(n) =

G(t)

−∞

j=1 [−λ,λ]

Since t < 0, the function xj  → e−tx2j is positive, symmetric, and convex up. Hence e−iπλnjxj

may be replaced by cos(πλnjxj). A short argument involving two integration by parts may be used to show that

e−x2jt cos(πλnjxj)dxj ≥ 0, which implies the claim of the lemma. We deﬁne a measure να on Rd by

(−1)nj

[−λ,λ]

να =

Hα(n)δ n

2λ

n∈Zd

### where δx is the point measure at x with δx(Rd) = 1.

√

- Lemma 3. Let λ and α be positive with 2π


dλα < jd/2(1). Convolution with να is the inverse operator of convolution with gα on B1([−λ,λ]d with

√

dλ)d/2 αd/2Jd/2(2π

(

√

f ∗ να 1 ≤

f 1

dαλ)

for all f ∈ B1([−λ,λ]d). Proof. By construction of να we have

gα(t) να(t) = 1 for all t ∈ [−λ,λ]d, and we observe that the total variation measure |να| satisﬁes |να|(Rd) =

1 gα(λ,...,λ)

Hα(n)(−1)n1+...+nd =

|Hα(n)| =

,

n∈Zd

n∈Zd

and Minkowski’s inequality f ∗ να 1 ≤ |να| f 1 shows that convolution with να deﬁnes a bounded operator on B1([−λ,λ]d) that inverts convolution with gα.

Lemma 3 gives a bound for the operator norm of the inverse of convolution with gα, and the calculation at the beginning of the proof of Theorem 1 may be used to complete the proof of Theorem 2.

References

- 1. L. D. Abreu and M. Speckbacher, Donoho-Logan large sieve principles for modulation and polyanalytic Fock spaces, Bull. Sci. Math. 171 (2021), Paper No. 103032, 25. MR 4295117
- 2. Y. Benyamini, A. Kroo´, and A. Pinkus, L1-approximation and ﬁnding solutions with small support, Constr. Approx. 36 (2012), no. 3, 399–431. MR 2996438
- 3. E. J. Cande`s, J. Romberg, and T. Tao, Robust uncertainty principles: exact signal reconstruction from highly incomplete frequency information, IEEE Trans. Inform. Theory 52 (2006), no. 2, 489–509. MR 2236170
- 4. NIST Digital Library of Mathematical Functions, http://dlmf.nist.gov/, Release 1.1.6 of 2022-06-30, F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier, B. I. Schneider, R. F. Boisvert, C. W. Clark, B. R. Miller, B. V. Saunders, H. S. Cohl, and M. A. McClain, eds.
- 5. D. L. Donoho and B. F. Logan, Signal recovery and the large sieve, SIAM J. Appl. Math. 52 (1992), no. 2, 577–591. MR 1154788
- 6. D. L. Donoho and P. B. Stark, Uncertainty principles and signal recovery, SIAM J. Appl. Math. 49 (1989), no. 3, 906–931. MR 997928
- 7. I. I. Hirschman and D. V. Widder, The convolution transform, Princeton University Press, Princeton, N. J., 1955. MR 0073746
- 8. Oleg Kovrijkine, Some results related to the Logvinenko-Sereda theorem, Proc. Amer. Math. Soc. 129 (2001), no. 10, 3037–3047. MR 1840110
- 9. B. F. Logan, Properties of high-pass signals, Ph.D. thesis, Columbia University, 1965.


