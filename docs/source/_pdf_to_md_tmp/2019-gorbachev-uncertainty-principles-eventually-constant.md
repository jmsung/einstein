arXiv:1904.11328v1[math.CA]25Apr2019

UNCERTAINTY PRINCIPLES FOR EVENTUALLY CONSTANT SIGN BANDLIMITED FUNCTIONS

D. V. GORBACHEV, V. I. IVANOV, AND S. YU. TIKHONOV

Abstract. We study the uncertainty principles related to the generalized Logan problem in Rd. Our main result provides the complete solution of the following problem: for a ﬁxed m ∈ Z+, ﬁnd

sup{|x|: (−1)mf(x) > 0} · sup{|x|: x ∈ supp f } → inf, where the inﬁmum is taken over all nontrivial positive deﬁnite bandlimited functions such that Rd |x|2kf(x)dx = 0 for k = 0,...,m − 1 if m ≥ 1.

We also obtain the uncertainty principle for bandlimited functions related to the recent result by Bourgain, Clozel, and Kahane.

1. Introduction

- 1.1. Logan’s problems. Logan stated and proved [31, 32] the following two extremal problems for real-valued positive deﬁnite bandlimited functions on R. Since such functions are even, we state these problems for functions on R+ = [0, ∞).


- Problem A. Find the smallest λ0 > 0 such that f(x) ≤ 0, x > λ0,

where f is a positive deﬁnite function of exponential type at most 1 satisfying

- (1.1) f(x) =


1

0

cosxtdµ(t), dµ ≥ 0, f(0) = 1.

Logan showed that admissible functions are integrable (even if the measure dµ is nonnegative in a neighborhood of the origin), λ0 = π, and the unique extremizer is

f0(x) =

cos2(x/2) 1 − x2/π2

![image 1](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile1.png>)

=

π 2

![image 2](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile2.png>)

1

0

sinπtcosxtdt,

Note that f0 satisﬁes R

+

f0(x) dx = 0.

- Problem B. Find the smallest λ1 > 0 such that f(x) ≥ 0, x > λ1,


where f is a positive deﬁnite integrable function satisfying (1.1) and having mean value zero.

![image 3](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile3.png>)

Date: April 26, 2019. 1991 Mathematics Subject Classiﬁcation. 42A82, 42A38. Key words and phrases. Logan’s problem, positive deﬁnite functions, bandlimited functions, the

uncertainty principle, Hankel transform.

The work of D.V. Gorbachev and V.I. Ivanov is supported by the Russian Science Foundation under grant 18-11-00199 and performed in Tula State University. S.Yu. Tikhonov was partially supported by MTM 2017-87409-P, 2017 SGR 358, and the CERCA Programme of the Generalitat de Catalunya.

1

It turns out that admissible functions are integrable with respect to the weight x2, and λ1 = 3π. Moreover, the unique extremizer is

1

cos2(x/2) (1 − x2/π2)(1 − x2/(3π)2)

- 3π

![image 4](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile4.png>)

- 4


(sinπt)3 cos xtdt,

f1(x) =

=

![image 5](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile5.png>)

0

x2f1(x) dx = 0.

This function satisﬁes R

+

We will study the multivariate generalization of Logan’s problems for the Fourier transforms. In more detail, we consider the m-parameter problem, m ∈ Z+ = {0, 1, . . .}, so that, for d = 1, if m = 0, 1 we recover Problems A and B respectively.

Let d ∈ N and Rd is d-dimensional Euclidean space with the scalar product x, y = x1y1 + · · · + xdyd and the norm |x| = x, x 1/2. Let Bτd = {x ∈ Rd: |x| ≤ τ} be the ball of radius τ > 0. Let Q = Rd or Q = R+. As usual, for a positive measure space (Q, dρ), let Lp(Q, dρ) denote the space of measurable functions such that f p,dρ =

Q |f(x)|p dρ(x) 1/p < ∞, L∞(Q) be the space of the essentially bounded measurable functions, and C(Q) consists of continuous functions on Q. The Fourier transform of f is given by

f(x)e−i x,y dx, y ∈ Rd. A function f deﬁned on Rd is positive-deﬁnite if for each N

f (y) = (2π)−d/2

Rd

N

cicj f(xi − xj) ≥ 0, ∀c1, . . ., cN ∈ C, ∀x1, . . ., xN ∈ Rd.

![image 6](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile6.png>)

i,j=1

Recall that for a continuous function f, by Bochner’s theorem, f is positive deﬁnite if and only if

- (1.2) f(x) =


ei x,y dµ(x),

Rd

where µ is a ﬁnite positive Borel measure (see, e.g., [15, 9.2.8]). In particular, if f ∈ L1(Rd), then dµ(x) = (2π)−d/2 f (x) dx and f ≥ 0.

In this paper we deal with continuous even functions f : Rd → R, which are constant

sign outside of a ball Bλd. Denote by λ(f) the smallest radius of a ball such that f is non-positive outside of this ball, that is,

λ(f) = sup{|x|: f(x) > 0}. Thus, functions with λ(−f) < ∞ are eventually nonnegative.

A function f is bandlimited if the distributional Fourier transform f (or the measure µ in (1.2)) has a compact support. Let

τ(f) = sup{|x|: x ∈ supp f }.

By the Paley–Wiener–Schwarz theorem, bandlimited functions f are restrictions of complex-valued entire functions of spherical exponential type τ(f) to Rd (see, e.g., [34]).

As in the original Logan’s problems we are interested in the smallest value of λ(±f) for continuous positive deﬁnite functions f with ﬁnite type τ(f). We also assume that the following orthogonality condition holds:

|x|2kf(x) dx = 0, k = 0, . . ., km, f ∈ L1(Rd, |x|2k

dx), for some integer km, cf. the condition in Problem B. This condition is equivalent to ∆k f (0) = 0, k = 0, . . ., km,

m

Rd

where ∆ is the Laplace operator, ∆0 = Id. One of the main goals of this paper is to solve the following

- Problem C. For d ∈ N and m ∈ Z+, ﬁnd inf λ((−1)mf)τ(f),


where the inﬁmum is taken over all nontrivial continuous positive deﬁnite bandlimited functions on Rd such that additionally if m ≥ 1, f ∈ L1(Rd, |x|2m−2 dx) and ∆k f (0) = 0, k = 0, . . ., m − 1.

It is worth mentioning that admissible functions in problem C as well as the expression λ(±f)τ(f) are invariant with respect to the dilation fa(x) = f(ax), a > 0, since λ(±fa) = a−1λ(±f) and τ(fa) = aτ(f). Note that in Problems A and B we have τ(f) = 1.

Problem C has various applications, in particular, to investigate Odlyzko’s question on zeros of the Dedekind zeta function (see [32] and [8, Sec. 4]). For m = 0 it plays an important role in several extremal problems in approximation theory (see, e.g., [7, 20]).

To formulate our main result, for α ≥ −1/2 we introduce the even entire function of exponential type 2

- (1.3) fα,m(t) =

jα2(t) (1 − t2/qα,2 1) · · ·(1 − t2/qα,m2 +1)

![image 7](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile7.png>)

, t ∈ R+,

where jα(t) = Γ(α+1)(2/t)αJα(t) is the normalized Bessel function and qα,1 < qα,2 < · · · are positive zeros of Jα.

- Theorem 1.1. For d ∈ N and m ∈ Z+, we have inf λ((−1)mf)τ(f) = 2qd/2−1,m+1,


where the inﬁmum is taken over all admissible functions in Problem C. The function fd/2−1,m(|x|) is the unique extremizer up to a positive constant. Moreover, this function satisﬁes ∆m f(0) = 0.

We note that the same statement is valid not only for positive deﬁnite functions but also for even functions with nonnegative Fourier transforms in a neighborhood of the origin. The positive deﬁniteness of fd/2−1,m for m = 0, 1 was established by Yudin [39, 41]. In the case m = 0, 1 Theorem 1.1 was proved in [20]. We prove Theorem 1.1 by solving a more general problem for the Dunkl transform Fk (see Section 6). In its turn, the corresponding problem for the Dunkl transform can be reduced to the one-dimensional problem for the Hankel transform Hα, α ≥ −1/2, in (R+, λ2α+1 dλ).

The key step in the proof of Theorem 1.1 is to show the positive deﬁniteness of fd/2−1,m for m ≥ 2. Note that since the normalized Bessel function jd/2−1(|x|) is positive deﬁnite it is enough to verify that gd/2−1,m(|x|) is positive deﬁnite, where

- (1.4) gα,m(t) =


jα(t) (1 − t2/qα,2 1) · · ·(1 − t2/qα,m2 +1)

.

![image 8](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile8.png>)

This remarkable fact has been recently established by Cohn and de Courcy-Ireland [12, Proposition 3.1]. The method of the proof is based on the Mehler–Heine formula on interrelation between the Bessel functions and Gegenbauer polynomials as well as the important result from the paper [10] stating that the polynomial

Pn(α,α)(z) (z − r1,n) · · ·(z − rk,n)

![image 9](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile9.png>)

is a linear combination of P0(α,α)(z), . . . , Pn(α,α−k)(z) with nonnegative coeﬃcients for each k ≤ n, where r1,n > r2,n > · · · > rn,n are zeros of the Jacobi polynomial Pn(α,α)(z) (in the case k = 1, 2, this was proved in [19]). Cohn and de Courcy-Ireland used the function fd/2−1,m to obtain lower bounds for energy in the Gaussian core model (see [12, Sect. 6]).

To solve Logan’s problem for the Hankel transform Hα, one should show that gα,m is positive deﬁnite with respect to Hα for any α ≥ −1/2 and m ≥ 0. For α = −1/2, m = 0, 1, we arrive at the cosine Fourier transform considered by Logan. We will give two proofs of positive deﬁniteness of the function gα,m. The ﬁrst one is the direct proof using the Sturm theorem on number on zeros of linear combinations of eigenfunctions (see Section 7). In particular, following this approach, one can obtain the monotonicity of the Hankel transform of the function gα,m on [0, 1]. The second proof extends the one by Cohn and de Courcy-Ireland for the case of any α (not necessarily half-integer) and is given in Section 8.

- Remark 1.1. Note that the functions gd/2−1+θ,m(|x|) and fd/2−1+θ,m(|x|) are positive deﬁnite on Rd for any θ ≥ 0 and m ∈ Z+. This follows from (2.16) below and the fact that for any α ≥ −1/2 and m ∈ Z+, gα,m and fα,m are positive deﬁnite with respect to Hankel transform. This result answers the question by M. Buhmann and is related to the theory of radial basis functions (see, e.g., [9]).


- 1.2. Uncertainty principle relations. Recently, Bourgain, Clozel, and Kahane [8] have studied the following uncertainty principle problem: ﬁnd


- 1

![image 10](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile10.png>)

- 2π


A+d =

inf λ(−f)λ(− f ),

where inﬁmum is taken over all even real-valued (nontrivial) functions f such that f, f ∈ C(Rd) ∩ L1(Rd) and f(0) ≤ 0, f (0) ≤ 0. They established

d 2πe

d + 2 2π

< A+d <

- (1.5)


, d ∈ N. For further results, see [13, 18]. Cohn and Gonc¸alves [13] proved that A+12 = 2.

![image 11](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile11.png>)

![image 12](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile12.png>)

Moreover, the authors considered the following problem: A−d = (2π)−1 inf λ(−f)λ( f ) for f(0) ≥ 0, f (0) ≤ 0 and found

A−1 = 1, A−8 = 2, A−24 = 4. This question is closely related to the linear programming bound for the sphere packing problem, which has been recently solved in dimensions 8 and 24 [11, 38].

In [18, Theorem 1.4], it was shown that an extremizer in the problem A±d exists and it is a radial function such that (2π)d/2 f(2πx) = ±f(x) and f(0) = 0. In particular, this implies that the support of f is not compact.

We study problems similar to that of ﬁnding A±d for bandlimited functions and obtain the following uncertainty principle.

- Theorem 1.2. Let d ∈ N, m, s ∈ Z+. We have inf λ((−1)mf)τ(f) = 2qd/2+s,m+1,


where the inﬁmum is taken over all nontrivial even continuous bandlimited functions f ∈ L1(Rd, |x|2m dx) such that

∆k f (0) = 0, k = 0, . . ., m − 1, ∆lf(0) = 0, l = 0, . . ., s − 1,

(for m = 0 or s = 0 the corresponding conditions are not assumed) and ∆m f (0) ≥ 0, ∆sf(0) ≤ 0. Each extremizer f(x) has the form r(x)fd/2+s,m(|x|), where

- (1.6) r(x) =

s+1

j=0

|x|2s+2−2jh2j(x) ≥ 0, |x| ≥ qd/2+s,m+1,

and h2j(x) are even harmonic polynomials of order at most 2j such that h0 > 0, h2j(0) = 0, j = 1, . . ., s + 1. Moreover, ∆m f (0) = ∆sf(0) = 0.

- Remark 1.2. (1) We also obtain the following result (see Theorem 6.1 (iii)):

- (1.7) inf λ((−1)mf)τ(f) = 2qd/2+s−1,m+1, where the inﬁmum is taken over all nontrivial even continuous bandlimited functions f ∈ L1(Rd, |x|2m+2s dx) such that
- (1.8) ∆k f (0) = 0, k = s, . . ., m + s − 1, ∆m+s f (0) ≥ 0. The function fd/2+s−1,m+1(|x|) is the unique (up to a positive constant) extremizer. Moreover, this function satisﬁes ∆m+s f(0) = 0.


- (2) For s = 0 all admissible functions in problem C satisfy condition (1.8). Moreover,

the positive deﬁnite function fd/2−1,m+1(|x|) is the unique extremizer in both problems C

- and (1.7).


- (3) If the polynomial r(x) given by (1.6) is nonnegative on Rd, then it is an even


homogeneous polynomial of order 2s + 2.

- Remark 1.3. Let us compare problems A±d and Theorem 1.2 with m = s = 0. From the observations above we note that A±d = (2π)−1 inf λ(f)λ(± f ) with f(0) = f(0) = 0. For bandlimited f, we have λ(± f ) ≤ τ(f) and therefore, A±d ≤ (2π)−1 inf λ(f)τ(f). In particular, we get A±d ≤ π−1qd/2,1 for any d ∈ N. If d = 1 we arrive at the sharp bound A±d ≤ 1. If d → ∞, we derive

A±d ≤

d 2π

![image 13](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile13.png>)

(1 + o(1)).

The latter corresponds to (1.5) but it is less interesting since qα,1 = α+cα1/3+O(α−1/3), where c = 1.855 · · · [6, Sec. 7.9].

- Remark 1.4. It is also worth mentioning the related results in metric geometry. Let




L ⊂ Rd be a lattice of rank d, λ1(L) be the ﬁrst successive minimum of L, µ(L) be the covering radius of L, and L∗ be a dual lattice. One of the important problems is to ﬁnd the inﬁmum of µ(L)λ1(L∗). There exists a self-dual lattice Ld such that [4]

d 2πe

(1 + o(1)) ≤ µ(Ld)λ1(L∗d) as d → ∞.

![image 14](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile14.png>)

Yudin showed [40] that µ(L)λ1(L∗) ≤ (2π)−1λ(f)τ(f) for any admissible function in Problem C with m = 0. This and Theorem 1.1 imply

d 2π

d 2πe

(1 + o(1)) ≤ µ(L)λ1(L∗) ≤

(1 + o(1)), cf. (1.5) (see also [4]).

![image 15](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile15.png>)

![image 16](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile16.png>)

- 1.3. Structure of the paper. Section 2 contains some auxiliary results on the Hankel


transform Hα as well as the Gauss- and Radau-type quadrature formulas with zeros of Bessel functions as nodes.

In Section 3, we give the solution of the generalized Logan problem for Hankel transform (see Theorem 3.1). Section 4 provides the uncertainty principle relations for bandlimited functions in (R+, t2α+1 dt) (see Theorem 4.1).

In Section 5, we study the problem of ﬁnding the smallest interval containing at least n

zeros of functions represented by f(λ) = 0 1 jα(λt) dσ(t) with a nonnegative bounded Stieltjes measure dσ. We will see that extremizers in this problem and Problem C are

closely related (Remark 5.1).

- In Section 6, we solve the multidimensional Logan problem for the Dunkl transform

(see Theorem 6.1) reducing this problem to the corresponding problems for the Hankel transforms (Theorems 3.1 and 4.1). Theorems 1.1 and 1.2 dealing with for the Fourier transform are partial cases of Theorem 6.1.

- In Section 7, we prove that the normalized Bessel functions form the Chebyshev


system. Section 8 contains the proof of positive deﬁniteness of the function gα,m based on the Mehler–Heine formula for Jacobi polynomials.

2. Notation and auxiliary results

Useful facts on harmonic analysis involving Hankel transform Hα in (R+, t2α+1 dt), α ≥ −1/2, can be founded in [6, 22, 30]. For the reader’s convenience we recall some of them. Let

- (2.1) Bα =

1 t2α+1

![image 17](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile17.png>)

d dt

![image 18](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile18.png>)

t2α+1

d dt

![image 19](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile19.png>)

=

d2 dt2

![image 20](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile20.png>)

+

2α + 1 t

![image 21](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile21.png>)

d dt

![image 22](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile22.png>)

,

be the Bessel diﬀerential operator. The normalized Bessel function jα(z) satisﬁes Bαjα(λt) = −λ2jα(λt) and is given by

- (2.2) jα(z) = 2αΓ(α + 1)

Jα(z) zα

![image 23](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile23.png>)

=

∞

k=0

(−1)kΓ(α + 1)(z/2)2k k! Γ(k + α + 1)

![image 24](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile24.png>)

,

where Jα(z) is the Bessel function of order α. In particular, j−1/2(z) = cosz and j1/2(z) = z−1 sin z. Moreover, the normalized Bessel function is the even entire function of exponential type 1, satisfying jα(z) = ∞k=1 1 − qz22

![image 25](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile25.png>)

α,k

, where qα,1 < qα,2 < . . . are positive zeros of Jα.

The known formulas for Bessel functions imply

- (2.3)

d dz

![image 26](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile26.png>)

jα(z) = −

z 2(α + 1)

![image 27](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile27.png>)

jα+1(z) =

2α z

![image 28](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile28.png>)

(jα−1(z) − jα(z)),

- (2.4)

d dz

![image 29](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile29.png>)

(z2α+2jα+1(λz)) = 2(α + 1)z2α+1jα(λz), and

- (2.5)

z

0

jα(at)jα(bt)t2α+1 dt =

z2α+2{a2jα+1(az)jα(bz) − b2jα(az)jα+1(bz)} 2(α + 1)(a2 − b2)

![image 30](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile30.png>)

. For λ ∈ R, we have

- (2.6) |jα(λ)| ≤ jα(0) = 1,


- and for |z| → ∞, Rez ≥ 0,
- (2.7) zα+1/2jα(z) =

2α+1/2Γ(α + 1) Γ(1/2)

![image 31](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile31.png>)

cos z −

π(2α + 1) 4

![image 32](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile32.png>)

+ O(|z|−1e|Imz|) . For α > −1/2, we also have Poisson’s integral representation

- (2.8) jα(λ) = cα

1

0

1 − t2 α−1/2 cos(λt) dt, cα =

Γ(α + 1) Γ(1/2)Γ(α + 1/2)

![image 33](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile33.png>)

. Then using

(−1)m cosλ −

m−1

k=0

(−1)kλ2k

![image 34](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile34.png>)

(2k)! ≥ 0, m ∈ N, λ ≥ 0, Poisson’s representation gives

- (2.9) ψm(λ) = (−1)m jα(λ) −

m−1

k=0

(−1)kΓ(α + 1)(λ/2)2k

![image 35](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile35.png>)

k! Γ(k + α + 1) ≥ 0. Deﬁne

- (2.10) dνα(t) = bαt2α+1 dt, t ∈ R+, b−α1 = 2αΓ(α + 1). The Hankel transform is given by

Hα(f)(λ) =

∞

0

f(t)jα(λt) dνα(t), λ ∈ R+.

It is an unitary operator in L2(R+, dνα) and Hα−1 = Hα.

If f ∈ L1(R+, dνα) ∩ C(R+) and Hα(f) ∈ L1(R+, dνα), then, for any t ∈ R+, one has the inversion formula

- (2.11) f(t) =

∞

0

Hα(f)(λ)jα(λt) dνα(λ).

We also recall the homogeneity property Hα(fa)(λ) = a−2α−2Hα(f)(λ/a), where fa(t) = f(at), a > 0. Note that the Hankel transform is a particular case of the one-dimensional Dunkl transform associated with the reﬂection group Z2 [35], see Section 6.

Let Bατ(R+) be the class of even entire functions f of exponential type at most τ > 0 such that the restriction of f to R+ belongs to L1(R+, dνα). For such functions one has |f(z)| ≤ f C(R

+)eτ|Imz|, ∀z ∈ C. Furthermore, the Paley–Wiener theorem states that f ∈ Bατ(R+) if and only if f ∈ L1(R+, dνα) ∩ C(R+) and supp Hα(f) ⊂ [0, τ] (see [27, Sect. 5], [2, Sect. 5], and [23]).

The following result ([25, 16], see also [22]) provides the Gauss and Radau (with multiple nodes) quadrature formulas for Bατ(R+) functions.

- Lemma 2.1. For any function f ∈ Bατ(R+) one has


τ 2

![image 36](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile36.png>)

2α+2 ∞

0

f(λ) dνα(λ) =

∞

k=1

γkf

2qα,k τ

![image 37](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile37.png>)

- (2.12)

=

r−1

l=0

αl,rf(2l)(0) +

∞

k=1

γk,rf

2qα+r,k τ

![image 38](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile38.png>)

- (2.13) , r ∈ N.


The series in (2.12) and (2.13) converge absolutely and the weights γk, γk,r, αr−1,r are positive.

Remark 2.1. (1) Formula (2.13) was formulated in [16] under the more restrictive condition f(λ) = O(λ−δ), λ → +∞, δ > 2α + 2. However, (2.12) was obtained for any f ∈ L1(R+, dνα) [25, 22]. It is easy to see that (2.13) follows from (2.12). Indeed, assuming τ = 2, one applies (2.12) with dνα+r, r ≥ 1 to the function

r−1

λ2j

g(λ) = λ−2r f(λ) − jα2+r(λ)

(fjα−+2r)(2j)(0)

(2j)! ∈ Bα2+r(R+). Straightforward calculations give (2.13).

![image 39](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile39.png>)

j=0

(2) One has αr−1,r = cα,r 0 ∞ jα2+r(λ) dνα+r−1(λ) > 0 with some cα,r > 0, see [16]. To construct extremizers for Problem C, we will use the generalized translation ope-

rator Tαt given by, for x, t ∈ R+,

- (2.14) Tαtf(x) =

- 1

![image 40](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile40.png>)

- 2 (f(x + t) + f(|x − t|), α = −1/2, cα 0 π f(√x2 + t2 − 2xtcos θ) sin2α θ dθ, α > −1/2,


![image 41](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile41.png>)

where cα is from (2.8) (see, e.g., [29, 24]). The translation operator is positive selfadjoint operator, Tαtf(x) ∈ C(R+ × R+) whenever f ∈ C(R+), and Tαt extends to the space Lp(R+, dνα), 1 ≤ p ≤ ∞. It is known that Tαtjα(λx) = jα(λt)jα(λx), which implies

- (2.15) Hα(Tαtf)(λ) = jα(tλ)Hα(f)(λ).

Moreover, supp Tαtf(x) ⊂ [0, a + t] if suppf ⊂ [0, a]. By means of the operator Tαt we deﬁne the positive convolution operator

(f1 ∗α f2)(x) =

∞

0

Tαtf1(x)f2(t) dνα(t),

which satisﬁes Hα(f1∗αf2) = Hα(f1)Hα(f2) and supp (f1∗αf2) ⊂ [0, a1+a2] if suppfi ⊂ [0, ai].

Following Levitan [29, § 11], an even function is called positive deﬁnite with respect to the Hankel transform Hα if for each N

N

i,j=1

cicj Tx

![image 42](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile42.png>)

i

α f(xj) ≥ 0, ∀c1, . . ., cN ∈ C, ∀x1, . . ., xN ∈ R+,

or, equivalently, the matrix (Tx

αif(xj))Ni,j=1 is positive semideﬁnite. By Bochner-type theorem [29, Theorem 12.1], the condition that a continuous function f is positive deﬁnite is equivalent to the fact that f is the Hankel transform of a measure σ,

f(λ) =

∞

0

jα(λt) dσ(t),

where σ is a non-decreasing function of bounded variation. In particular, if f ∈ L1(R+, dνα), then dσ = Hα(f) dνα and Hα(f) ≥ 0.

Moreover, it is easy to see that if f is positive deﬁnite with respect to Hβ, then it is the same with respect to Hα for α < β, since

- (2.16) Hα(f)(t) =

1 2β−α−1Γ(β − α)

![image 43](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile43.png>)

∞

t

s(s2 − t2)β−α−1Hβ(f)(s) ds, t ∈ R+. The latter follows from Sonine’s ﬁrst integral for the Bessel functions:

- (2.17) jβ(λ) =


b−β1 2β−α−1Γ(β − α)

1

(1 − t2)β−α−1jα(λt) dνα(t), where bβ is deﬁned in (2.10).

![image 44](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile44.png>)

0

Special attention will be paid below to the positive deﬁnite functions jα+1(λ) and jα2+1(λ). By (2.17), we have

1

jα+1(λ) = b−α+11

jα(λt) dνα(t) = b−α+11 Hα(χ[0,1])(λ), where χI(t) is the characteristic function of an interval I. Thus,

0

- (2.18) jα2+1(λ) = b−α+12 Hα(χ[0,1] ∗α χ[0,1])(λ)


and supp Hα(jα2+1) ⊂ [0, 2]. We will also use the following two lemmas.

- Lemma 2.2 ([21]). Let α ≥ −1/2. There exists an even entire function ωα(z), z = x + iy, of exponential type 2, positive for x > 0, and such that

ωα(x) ≍ x2α+1, x → +∞, |ωα(iy)| ≍ y2α+1e2y, y → +∞,

where F1 ≍ F2 means that C−1F1 ≤ F2 ≤ CF1, C > 0. One can take ωα(z) = z2m+2jν(z + i)jν(z − i), where α = m − ν, m ∈ Z+, and ν ∈ [−1/2, 1/2].

- Lemma 2.3. Let F be an even entire function of exponential type τ > 0 bounded on R. Let Ω be an even entire function of ﬁnite exponential type, all the zeroes of Ω be zeros of F, and, for some m ∈ Z+,


e−τyy2m|Ω(iy)| > 0. Then the function F(z)/Ω(z) is an even polynomial of degree at most 2m. Lemma 2.3 is an easy consequence of Akhiezer’s result [28, Appendix VII.10].

liminf

y→+∞

3. Logan problem for the Hankel transform

Let α ≥ −1/2 and m ∈ Z+. In this section we solve the generalized Logan problem (with parameter m) for the Hankel transform Hα in (R+, dνα(λ)). This is the crucial step to prove Theorems 1.1 and 1.2.

Consider the class Eα(R+) of real-valued even entire functions f of ﬁnite exponential type such that

- (3.1) f(λ) =

τ(f)

0

jα(λt) dσ(t), where σ is a function of bounded variation.

Let λ(f) = sup{λ > 0: f(λ) > 0}. For m ∈ Z+, denote by Eα,m(R+) the subclass of functions f ∈ Eα(R+) such that λ((−1)mf) < ∞ and, if m ≥ 1, f ∈ L1(R+, λ2m−2 dνα) and for k = 0, . . ., m − 1

- (3.2) BαkHα(f)(0) = (−1)k

∞

0

λ2kf(λ) dνα(λ) = 0.

We will see that this class is not empty, in particular, fα,m(λ) = jα(λ)gα,m(λ) ∈ Eα,m(R+), see (1.3) and (1.4). Due to (2.15), for the Hankel transforms of functions fα,m and gα,m one has

Hα(fα,m) = Tα1Hα(gα,m).

Theorem 3.1. (i) Let f ∈ Eα,m(R+)\{0} be given by (3.1) such that σ is non-decreasing in some neighborhood of the origin. Then

- (3.3) f ∈ L1(R+, λ2m dνα), (−1)m


∞

λ2mf(λ) dνα(λ) ≥ 0,

0

and

- (3.4) 2qα,m+1 ≤ λ((−1)mf)τ(f).

Moreover, inequality (3.4) is sharp and the function fα,m is the unique extremizer up to a positive constant.

- (ii) The functions gα,m and fα,m are positive deﬁnitive and

(3.5)

∞

0

λ2mfα,m(λ) dνα(λ) = 0.

- (iii) There holds gα,m = Hα(pα,mχ[0,1]), where pα,m(t) is decreasing on [0, 1] and has


- (3.6) ψm(2m)(0) > 0, ρε(λ) ≥ 0, lim


a zero of multiplicity 2m + 1 at t = 1.

Proof. The proof is divided into several steps. Since the class Eα,m(R+) and the quantity λ((−1)mf)τ(f) are invariant under dilations, we let for convenience τ(f) = 2. We also denote qk = qα,k for k ≥ 1.

- Proof of (3.3). Let m = 0. The embedding Eα,0(R+) ⊂ L1(R+, dνα) can be shown using the method of Logan, see [32, Lemma].


We consider the positive deﬁnite kernel ϕε(x) = jα2+1(ε|x|/2), ε > 0. By (2.7), (2.6),

- and (2.18), ϕε ∈ C(R+)∩L1(R+, dνα), ϕε C(R


+) = ϕε(0) = 1, and suppHα(ϕε) ⊂ [0, ε]. Since dσ ≥ 0 in some neighborhood of the origin, then for suﬃciently small ε we have

ε

∞

∞

0 ≤

Hα(ϕε)(t) dσ(t) =

Hα(ϕε)(t) dσ(t) =

f(λ)ϕε(λ) dνα(λ)

0

0

0

λ(f)

∞

=

f(λ)ϕε(λ) dνα(λ) −

|f(λ)|ϕε(λ) dνα(λ), which implies

0

λ(f)

∞

λ(f)

λ(f)

|f(λ)|ϕε(λ) dνα(λ) ≤

f(λ)ϕε(λ) dνα(λ) ≤

|f(λ)| dνα. Letting ε → 0, Fatou’s lemma yields

λ(f)

0

0

∞

λ(f)

|f(λ)| dνα(λ) ≤

|f(λ)| dνα(λ) < ∞,

λ(f)

0

which implies f ∈ L1(R+, dνα).

Let m ≥ 1. We have f ∈ L1(R+, dνα) and dσ(t) = Hα(f)(t) dt, where Hα(f)(t) is continuous and nonnegative in some neighborhood of the origin. Moreover, (−1)m+1f(λ) = |f(λ)| for λ ≥ λ((−1)mf).

Consider

(2m)! ψm(ελ) ε2mψm(2m)(0)

ρε(λ) =

,

![image 45](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile45.png>)

where ψm(λ) is given in (2.9). We have

ρε(λ) = λ2m, λ ∈ R+. In light of

ε→0

(2m)! ψm(2m)(0)

2/4

ε2eλ

|ρε(λ) − λ2m| ≤

![image 46](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile46.png>)

we derive that ρε(λ) converges uniformly to λ2m on any ﬁnite interval [0, b] as ε → 0.

Taking into account (2.9), (3.6), the orthogonality condition (3.2), and nonnegativity of Hα(f) near the origin, we obtain

∞

∞

(2m)! ε2mψm(2m)(0)

(−1)m

ρε(λ)f(λ) dνα(λ) =

f(λ)jα(ελ) dνα(λ)

![image 47](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile47.png>)

0

0

(2m)! ε2mψm(2m)(0)

- (3.7) Hα(f)(ε) ≥ 0. Thus,
- (3.8) (−1)m+1

∞

λ((−1)mf)

ρε(λ)f(λ) dνα(λ) ≤ (−1)m

λ((−1)mf)

0

ρε(λ)f(λ) dνα(λ). Using (3.7), (3.6), and Fatou’s lemma we arrive at

(−1)m+1

∞

λ((−1)mf)

λ2mf(λ) dνα(λ) = (−1)m+1

∞

λ((−1)mf)

lim

ε→0

ρε(λ)f(λ) dνα(λ)

≤ liminf

ε→0

(−1)m+1

∞

λ((−1)mf)

ρε(λ)f(λ) dνα(λ).

In light of (3.8), we continue as follows

≤ liminf

ε→0

(−1)m

λ((−1)mf)

0

ρε(λ)f(λ) dνα(λ)

= (−1)m

λ((−1)mf)

0

lim

ε→0

ρε(λ)f(λ) dνα(λ) = (−1)m

λ((−1)mf)

0

λ2mf(λ) dνα(λ) < ∞, which gives (3.3).

- Proof of (3.4). Let f ∈ Eα,m(R+). We will prove that qm+1 ≤ λ((−1)mf). Assume the converse, i.e., λ((−1)mf) < qm+1. We have (−1)mf(λ) ≤ 0 for λ ≥ qm+1. By (3.3) we have λ2mf ∈ Bα2(R+). Then using Gauss’ quadrature formula (2.12) and (3.2), we get


0 ≤ (−1)m

∞

0

λ2mf(λ) dνα(λ) = (−1)m

∞

0

m

k=1

(λ2 − qk2)f(λ) dνα(λ)

= (−1)m

∞

s=m+1

γsf(qs)

m

k=1

- (3.9) (qs2 − qk2) ≤ 0.

Therefore, qs, s ≥ m + 1, are zeros of multiplicity 2 for f. Similarly, applying Gauss’ quadrature formula for f, we obtain

- (3.10) 0 =


=

![image 48](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile48.png>)

m

m

∞

(qs2 − qk2)f(qs), s = 1, . . ., m.

(λ2 − qk2)f(λ) dνα(λ) = γs

0

k=1 k =s

k=1 k =s

Therefore, qs, s = 1, . . ., m, are zeros of f.

Take the function ωα(λ) from Lemma 2.2 and consider the following even functions of exponential type 4:

ωα(λ)jα2(λ)

F(λ) = ωα(λ)f(λ), Ω(λ) =

.

m

![image 49](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile49.png>)

k=1(1 − λ2/qk2)

Note that F ∈ L1(R) since f ∈ L1(R+, λ2α+1 dλ) and ωα(λ) ≍ λ2α+1, λ → +∞. Then F is bounded on R.

From (2.7) and Lemma 2.2 we have |Ω(iy)| ≍ y−2me4y as y → +∞. Since all zeros of Ω(λ) are also zeros of F(λ), taking into account Lemma 2.3, we obtain

jα2(λ) mk=0 ckλ2k

f(λ) =

,

m

![image 50](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile50.png>)

k=1(1 − λ2/qk2)

where ck = 0 for some k. Note that jα(λ) ∈/ L2(R+, dνα), see (2.7). This contradicts f ∈ L1(R+, λ2m dνα). Hence, λ((−1)mf) ≥ qm+1 and λ((−1)mf)τ(f) ≥ 2qm+1.

Now we consider the function fα,m given by (1.3). Note that in virtue of the estimate fα,m(λ) = O(λ−2α−2m−3) as λ → ∞ we have fα,m ∈ L1(R+, λ2m dνα). Moreover, τ(fα,m) = 2 and λ((−1)mfα,m) = qα,m+1. Part (i) is proved.

To verify part (ii), we ﬁrst note that Gauss’ quadrature formula implies (3.5). To show the positive deﬁniteness of fα,m, it is enough to prove that gα,m is positive deﬁnite. Positive deﬁniteness of the function gα,m. This result has been recently obtained by Cohn and de Courcy-Ireland [12] for α = d/2 − 1, d ∈ N. We prove the same statement for any α. For this, we calculate the Hankel transform of gα,m and show that it is nonnegative.

For ﬁxed λ1, . . ., λk ∈ R, consider the polynomial

k

(λi − λ), λ ∈ R. Then

ωk(λ) = ω(λ, λ1, . . ., λk) =

i=1

k

1 ωk(λ)

1 ωk′ (λi)(λi − λ)

.

=

![image 51](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile51.png>)

![image 52](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile52.png>)

i=1

Setting λi = qi2, we have

- (3.11)

1

![image 53](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile53.png>)

k

i=1(1 − λ2/qi2)

=

k

i=1

qi2

1 ωk(λ2)

![image 54](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile54.png>)

=

k

i=1

qi2

k

i=1

1 ωk′ (qi2)(qi2 − λ2)

![image 55](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile55.png>)

=

k

i=1

Ai qi2 − λ2

![image 56](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile56.png>)

,

where

- (3.12) ωk′ (qi2) =

k

j=1 j =i

(qj2 − qi2), Ai =

k

j=1 qj2 ωk′ (qi2)

![image 57](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile57.png>)

.

Note that

- (3.13) sign Ai = (−1)i−1. Setting

ϕi(t) = jα(qit), i = 1, . . ., m + 1,

we remark that ϕi(t) are eigenfunctions and qi2 are eigenvalues of the following Sturm– Liouville problem on [0, 1]:

- (3.14) (t2α+1u′)′ + λ2t2α+1u = 0, u′(0) = 0, u(1) = 0.

It follows from (2.5), (2.3), and jα(qi) = 0 that

∞

0

ϕi(t)χ[0,1](t)jα(λt)t2α+1 dt =

1

0

jα(qit)jα(λt)t2α+1 dt = −

ϕ′i(1)jα(λ) qi2 − λ2

![image 58](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile58.png>)

, or, equivalently,

- (3.15) Hα −b−α1


ϕiχ[0,1] ϕ′i(1)

jα(λ) qi2 − λ2

(λ) =

.

![image 59](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile59.png>)

![image 60](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile60.png>)

Note that

- (3.16) signϕ′i(1) = (−1)i. Consider the following polynomial in eigenfunctions ϕi(t):
- (3.17) pα,m(t) = −b−α1

m+1

i=1

Ai ϕ′i(1)

![image 61](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile61.png>)

ϕi(t) =

m+1

i=1

Biϕi(t).

Due to (3.13), (3.14), and (3.16), we have that Bi > 0, pα,m(0) > 0, and pα,m(1) = 0. Moreover, in virtue of (3.11) and (3.15),

- (3.18) gα,m(λ) =

jα(λ)

![image 62](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile62.png>)

m+1

i=1 (1 − λ2/qi2)

= Hα(pα,mχ[0,1])(λ).

From this, it is enough to show that pα,m(t) ≥ 0 on [0, 1]. Deﬁne the Vandermonde determinant ∆(λ1, . . ., λk) = k1≤j<i≤k(λi − λj), then

∆(λ1, . . ., λk) ωk′ (λi)

![image 63](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile63.png>)

= (−1)i−1∆(λ1, . . ., λi−1, λi+1, . . ., λk). In virtue of (3.11) and (3.12), we have

pα,m(t) = −c

m+1

i=1

(−1)i−1∆(q12, . . ., qi2−1, qi2+1, . . ., qm2 +1)

ϕi(t) ϕ′i(1)

![image 64](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile64.png>)

= −c

ϕ1(t)

![image 65](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile65.png>)

ϕ′1(1) . . . ϕ

m+1(t)

![image 66](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile66.png>)

ϕ′m+1(1) 1 . . . 1 q12 . . . qm2 +1 . . . . . . . . . . . . . . q12m−2 . . . qm2m+1−2

, c =

b−α1 mj=1+1 qj2 ∆(q12, . . ., qm2 +1)

![image 67](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile67.png>)

- (3.19) > 0.

Here and in what follows if m = 0 we deal with only the (1, 1) entries of the matrices. Let us show that

- (3.20)


ϕ′1(1) . . . ϕ

m+1(t) ϕ′m+1(1)

ϕ1(t)

![image 68](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile68.png>)

![image 69](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile69.png>)

ϕ1(t)

ϕ′1(1) . . . ϕ

m+1(t)

![image 70](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile70.png>)

![image 71](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile71.png>)

ϕ′m+1(1) 1 . . . 1 q12 . . . qm2 +1 . . . . . . . . . . . . . . q12m−2 . . . qm2m+1−2

1 . . . 1

(3) m+1(1)

ϕ(3)1 (1)

ϕ′1(1) . . . ϕ

m(m−1) 2

.

= (−1)

![image 72](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile72.png>)

![image 73](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile73.png>)

![image 74](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile74.png>)

ϕ′m+1(1)

. . . . . . . . . . . . . . . . .

(2m−1) m+1 (1)

ϕ(21 m−1)(1)

ϕ′1(1) . . . ϕ

![image 75](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile75.png>)

![image 76](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile76.png>)

ϕ′m+1(1)

By (3.14), we derive

tϕ′′i (t) + (2α + 1)ϕ′i(t) + qi2tϕi(t) = 0. Therefore,

tϕ(is+2)(t) + sϕ(is+1)(t) + (2α + 1)ϕ(is+1)(t) + qi2tϕ(is)(t) + sqi2ϕ(is−1)(t) = 0, which implies for t = 1

ϕ(is+2)(1) = −(s + 2α + 1)ϕ(is+1)(1) − qi2ϕ(is)(1) − sqi2ϕ(is−1)(1), ϕ(0)i (1) = 0. By induction we then obtain for k = 0, 1, . . .

k

ϕ(2i k+1)(1) = ϕ′i(1)

j=0

akj(α)qi2j, ϕ(2i k+2)(1) = ϕ′i(1)

k

bkj(α)qi2j,

j=0

where akj(α), bkj(α) are polynomials in α with coeﬃcients not depending on qi and moreover akk(α) = (−1)k. This implies for k = 1, 2, . . .

k

ϕ(2i k)(1) ϕ′i(1)

ϕ(2i s−1)(1) ϕ′i(1)

- (3.21) ,

ϕ(2i k+1)(1) ϕ′i(1)

![image 77](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile77.png>)

=

k

s=1

c1s(α)

ϕ(2i s−1)(1) ϕ′i(1)

![image 78](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile78.png>)

- (3.22) + (−1)kqi2k,

where c0s(α) and c1s(α) do not depend on qi. Then (3.22) implies (3.20) since

ϕ1(t)

![image 79](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile79.png>)

ϕ′1(1) . . . ϕ

m+1(t) ϕ′m+1(1)

![image 80](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile80.png>)

1 . . . 1

ϕ(3)1 (1)

![image 81](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile81.png>)

ϕ′1(1) . . . ϕ

(3) m+1(1)

![image 82](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile82.png>)

ϕ′m+1(1)

. . . . . . . . . . . . . . . . .

ϕ(21 m−1)(1)

![image 83](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile83.png>)

ϕ′1(1) . . . ϕ

(2m−1) m+1 (1)

![image 84](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile84.png>)

ϕ′m+1(1)

=

ϕ1(t)

![image 85](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile85.png>)

ϕ′1(1) . . . ϕ

m+1(t) ϕ′m+1(1)

![image 86](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile86.png>)

1 . . . 1 −q12 . . . −qm2 +1

. . . . . . . . . . . . . . . . . . . . . . . . (−1)m−1q12m−2 . . . (−)m−1qm2m+1−2

.

Further, taking into account (3.19) and (3.20), we derive

- (3.23) p(1)α,m(1) = p(3)α,m(1) = · · · = pα,m(2m−1)(1) = 0. Therefore, by (3.17) and (3.21), we obtain for k = 0, . . ., m that

p(2α,mk)(1) = −b−α1

m+1

i=1

Ai

ϕ(2i k)(1) ϕ′i(1)

![image 87](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile87.png>)

= −b−α1

m+1

i=1

Ai

k

s=1

c0s(α)

ϕ(2i s−1)(1) ϕ′i(1)

![image 88](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile88.png>)

= −b−α1

k

s=1

c0s(α)

m+1

i=1

Ai

ϕ(2i s−1)(1) ϕ′i(1)

![image 89](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile89.png>)

=

k

s=1

c0s(α)p(2α,ms−1)(1) = 0.

Together with (3.23), this implies that the zero t = 1 of the polynomial pα,m(t) has multiplicity 2m+1. Then taking into account (3.18), the same also holds for Hα(gα,m)(t).

Let us show that pα,m(t) does not have zeros on [0, 1) and hence pα,m(t) > 0 on [0, 1). This yields that gα,m is the positive deﬁnite function.

We use the facts that {ϕi(t)}im=1+1 for any m ∈ Z+ is the Chebyshev system on the

interval (0, 1) (see Theorem 7.1 below) and any polynomial mi=1+1 ciϕi(t) on (0, 1) has at most m zeros, counting multiplicity.

We now consider the polynomial

- (3.24) p(t, ε) =

ϕ1(t)

![image 90](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile90.png>)

ϕ′1(1) . . . ϕ

m+1(t)

![image 91](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile91.png>)

ϕ′m+1(1) ϕ1(1−ε)

![image 92](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile92.png>)

(−ε)ϕ′1(1) . . . ϕ

m+1(1−ε)

![image 93](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile93.png>)

(−ε)ϕ′m+1(1) ϕ1(1−2ε)

![image 94](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile94.png>)

(−2ε)3ϕ′1(1) . . . ϕ

m+1(1−2ε) (−2ε)3ϕ′m+1(1)

![image 95](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile95.png>)

. . . . . . . . . . . . . . . . . . . . . . . . .

ϕ1(1−mε)

![image 96](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile96.png>)

(−mε)2m−1ϕ′1(1) . . . ϕ

m+1(1−mε) (−mε)2m−1ϕ′m+1(1)

![image 97](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile97.png>)

.

If m = 0, it is positive on (0, 1) and, if m ≥ 1, for any 0 < ε < 1/m, it has m zeros at the points tj = 1 − jε, j = 1, . . ., m. Letting ε → 0+, we note that the polynomial

lim

ε→0+

p(t, ε) does not have zeros on (0, 1). Let us show that

- (3.25) lim


=

c0s(α)

![image 98](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile98.png>)

![image 99](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile99.png>)

s=1

p(t, ε) = cpα,m(t) with some c = 0. This implies that the polynomial pα,m(t) is positive on [0, 1).

ε→0+

To show (3.25), by Taylor’s theorem, we have

ϕi(1 − jε) (−jε)2j−1ϕ′i(1)

=

![image 100](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile100.png>)

2j−2

ϕ(is)(1) s! (−jε)2j−1−sϕ′i(1)

![image 101](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile101.png>)

s=1

ϕ(2i j−1)(1) + o(1) (2j − 1)! ϕ′i(1)

+

, ε → 0,

![image 102](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile102.png>)

for j = 1, . . ., m − 1. Using formulas (3.21) and (3.22) and progressively subtracting the row j from the row j − 1 in the determinant (3.24), we arrive at

ϕ1(t)

ϕ′1(1) . . . ϕ

m+1(t) ϕ′m+1(1)

![image 103](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile103.png>)

![image 104](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile104.png>)

1 + o(1) . . . 1 + o(1)

1

(3) m+1(1)+o(1)

ϕ(3)1 (1)+o(1)

ϕ′1(1) . . . ϕ

.

p(t, ε) =

![image 105](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile105.png>)

![image 106](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile106.png>)

![image 107](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile107.png>)

ϕ′m+1(1)

m−1

j=1 (2j − 1)!

. . . . . . . . . . . . . . . . . . . . . . .

(2m−1) m+1 (1)+o(1)

ϕ(21 m−1)(1)+o(1)

ϕ′1(1) . . . ϕ

![image 108](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile108.png>)

![image 109](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile109.png>)

ϕ′m+1(1)

Then, taking into account (3.19) and (3.20), we have (3.25).

Monotonicity of pα,m. The polynomial p(t, ε) vanishes at m + 1 points: tj = 1 − jε, j = 1, . . ., m, and tm = 1, thus its derivative p′(t, ε) has m zeros on the interval (1−ε, 1).

In virtue of (2.3),

qi2t 2(α + 1)

ϕ′i(t) = −

jα+1(qit), t ∈ [0, 1].

![image 110](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile110.png>)

This and Theorem 7.1 imply that {ϕ′i(t)}mi=1+1 is the Chebyshev system on (0, 1). Therefore, p′(t, ε) does not have zeros on (0, 1 − ε]. Then for ε → 0+ we derive that p′α,m(t) does not have zeros on (0, 1). Since pα,m(0) > 0 and pα,m(1) = 0, then p′α,m(t) < 0 on (0, 1). Thus, pα,m(t) is decreasing on the interval [0, 1]. This completes the proof of part (iii).

Uniqueness of the extremizer fα,m. As above, we will use Lemmas 2.2 and 2.3. Let f(λ) be an extremizer and λ((−1)mf) = qm+1. Consider the functions

F(λ) = ωα(λ)f(λ), Ω(λ) = ωα(λ)fα,m(λ), where fα,m is deﬁned in (1.3) and ωα is from Lemma 2.2.

Note that all zeros of Ω(λ) are also zeros of F(λ). Indeed, we have (−1)mf(λ) ≤ 0 for λ ≥ qm+1 and f(qm+1) = 0 (otherwise λ((−1)mf) < qm+1, which is a contradiction). This and (3.9) imply that the points qs, s ≥ m + 2, are double zeros of f. By (3.10), we also have that f(qs) = 0 for s = 1, . . ., m and therefore the function f has zeros (at least, of order one) at the points qs, s = 1, . . ., m + 1.

Using asymptotic relations given in Lemma 2.2, we derive that F(λ) is the entire function of exponential type, integrable on real line and therefore bounded. Taking into account (2.7) and Lemma 2.2, we get

|Ω(iy)| ≍ y−2m−2e4y, y → +∞.

Now using Lemma 2.3, we arrive at f(λ) = ψ(λ)fα,m(λ), where ψ(λ) is an even polynomial of degree at most 2m+2. Note that the degree cannot be 2s, s = 1, . . ., m+1, since in this case (2.7) implies that f ∈/ L1(R+, λ2m dνα). Thus, f(λ) = cfα,m(λ), c > 0.

4. Uncertainty principle for bandlimited functions on R+

Let as above λ(f) = sup{λ > 0: f(λ) > 0}, Eα(R+) be the class of real-valued even bandlimited functions f ∈ C(R+), τ(f) be the type of a bandlimited function f, and Bα denote the operator (2.1).

Following the proof of Theorem 3.1, we obtain the following uncertainty principle for bandlimited functions on R+.

- Theorem 4.1. Let α ≥ −1/2 and m, s ∈ Z+. (i) One has


inf λ((−1)mf)τ(f) = 2qα+s+1,m+1,

where the inﬁmum is taken over all nontrivial functions f ∈ Eα(R+) ∩ L1(R+, λ2m dνα) such that

- (4.1)

BαkHα(f)(0) = 0, k = 0, . . ., m − 1, Bαl f(0) = 0, l = 0, . . ., s − 1,

and

- (4.2) BαmHα(f)(0) ≥ 0, Bαsf(0) ≤ 0.

Moreover, the function λ2s+2fα+s+1,m(λ) is the unique extremizer up to a positive constant, which additionally satisﬁes BαmHα(f)(0) = Bαsf(0) = 0.

(ii) One has

inf λ((−1)mf)τ(f) = 2qα+s,m+1,

where the inﬁmum is taken over all nontrivial functions f ∈ Eα(R+)∩L1(R+, λ2m+2s dνα) such that

- (4.3) BαkHα(f)(0) = 0, k = s, . . ., m + s − 1, Bαm+sHα(f)(0) ≥ 0.


Moreover, the function fα+s,m(λ) is the unique extremizer up to a positive constant, which additionally satisﬁes Bαm+sHα(f)(0) = 0.

Proof. Part (i). Let f be an admissible function. Without loss of generality we can assume that τ(f) = 2. Unlike the proof of Theorem 3.1 we will use the Radau quadrature formula (2.13) with r = s + 1.

First, we show that f(2l)(0) = 0 for 0 ≤ l ≤ s − 1 and f(2s)(0) ≤ 0. Indeed, we have Bαλ2j = 2j(2α + 2j)λ2j−2, and therefore for j, l ∈ Z+, by induction, we obtain for the l-th power of Bα that Bαl λ2j = cα,j,lλ2j−2l, where cα,j,l > 0 for j ≥ l and cα,j,l = 0 otherwise. This and Taylor’s expansion of f imply

cα,l,l (2l)!

Bαl f(0) =

f(2l)(0).

![image 111](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile111.png>)

Second, let λ((−1)mf) < qm′ +1, where for simplicity we put qk′ = qα+s+1,k, k ≥ 1. Recall that qα,k are zeros of the Bessel function jα(λ). Applying (2.13) to g(λ) = (−1)m mk=1(λ2 − qk′ 2)f(λ) (note that g ∈ Bα2(R+)), we derive

s

∞

∞

γk,s+1g(qk′ ). On the other hand, we have ∞

αl,s+1g(2l)(0) +

g(λ) dνα(λ) =

0

l=0

k=1

∞

g(λ) dνα(λ) = (−1)m

λ2mf(λ) dνα(λ) = BαmHα(f)(0) ≥ 0

0

0

and

m

qk′2 ≤ 0. Therefore,

g(2j)(0) = 0, j = 0, . . ., s − 1, g(2s)(0) = f(2s)(0)

k=1

∞

0 ≤ αs,s+1g(2s)(0) +

γk,s+1g(qk′ ) ≤ 0,

k=m+1

where we have used that γk,s+1 > 0 and the fact that g(λ) ≤ 0 for λ ≥ λ((−1)mf). Thus, f has double zeros at the points qk′ , k ≥ m + 1, and the zero of order 2s + 2 at the origin.

Further, applying formula (2.13) for j = 1, . . ., m to the functions mk=1

(λ2 − qk′2)f(λ),

k =j

we conclude that the function f has at least simple zeros at the points qj, 1 ≤ j ≤ m. Then as in the proof of Theorem 3.1, using Lemmas 2.2, 2.3 and the fact that

λ2s+2jα2+s+1(λ) ∈/ L1(R+, dνα), we derive that f(λ) =

λ2s+2jα2+s+1(λ) mk=0 ckλ2k

∈/ L1(R+, λ2m dνα).

m

![image 112](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile112.png>)

k=1(1 − λ2/qk′2)

Hence, following arguments similar to those used to show (3.4), we obtain that λ((−1)mf) ≥ qm′ +1. In fact, we have that λ((−1)mf) = qm′ +1 for

λ2s+2jα2+s+1(λ)

k=1 (1 − λ2/qk′2) ∈ L1(R+, λ2m dνα). Moreover, f is a unique extremizer up to a positive constant (similarly to the proof of the uniqueness of fα,m in Theorem 3.1).

- (4.4) f(λ) =


![image 113](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile113.png>)

m+1

Using (2.13) and f(2s)(0) = 0, we also have BαmHα(f)(0) = Bαsf(0) = 0. Part (ii). The case s = 0 follows from Theorem 3.1 since to prove estimate (3.4), we

only used condition (3.3). Let s ≥ 1. We observe that for any admissible function f, that is, satisfying condition

- (4.3), the function g(λ) = λ2sf(λ) satisﬁes conditions (4.1) and (4.2) with the parameter s−1 in place of s. At the same time, we have λ((−1)mf)τ(f) = λ((−1)mg)τ(g). Hence, using the fact that cλ2sfα+s,m(λ) is the unique extremizer in part (i), we conclude that cfα+s,m(λ) is the unique extremizer in problem (ii).


5. Number of zeros of positive definite function on R+

It was proved in [33] that if a function from the class (1.1) has n zeros on the interval [0, L], then L ≥ π2 n. Moreover,

![image 114](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile114.png>)

x n

n

Fn(x) = cos

![image 115](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile115.png>)

is the unique extremal function. Note that the functions Fn(πn(x − 12)) for n = 1 and 3 coincide, up to constants, with the cosine Fourier transform of f0 and f1 (see Introduction) on [0, 1].

![image 116](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile116.png>)

In this section we study a similar problem for the Hankel transform Hα with α ≥ −1/2. We will use the approach which was developed in Section 3. The key argument in the proof is based on the properties of the polynomial pα,m(t) deﬁned in (3.17).

Let NI(f) be the number of zeros of f on I, counting multiplicity. We will say that

f ∈ Eα+(R+) if f(λ) = 0 1 jα(λt) dσ(t) with a nonnegative bounded Stieltjes measure dσ = 0.

- Theorem 5.1. Let α ≥ −1/2, n ∈ N, and


L(f, n) = inf {L > 0: N[0,L](f) ≥ n}. Then

qα,m+1, n = 2m + 1, qα+1,m+1, n = 2m + 2.

inf

L(f, n) ≤ θα,n =

f∈Eα+(R+)

Moreover, there exists a function Fα,n ∈ Eα+(R+) such that L(Fα,n, n) = θα,n.

- Remark 5.1. (1) For α = −1/2, we have q−1/2,m+1 = π2 (2m + 1), q1/2,m+1 = π(m + 1), and, therefore, θ−1/2,n = π2 n. Hence, we arrive at the mentioned above result [33]


![image 117](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile117.png>)

![image 118](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile118.png>)

π 2

inf

L(f, n) =

n,

![image 119](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile119.png>)

f∈E−+1/2(R+)

where the extremal function F−1/2,n(λ) = (cos λn)n has on [0, π2 n] the unique zero λ = π2 n of multiplicity n.

![image 120](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile120.png>)

![image 121](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile121.png>)

![image 122](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile122.png>)

(2) We will show that the function Fα,n(λ) has on [0, θα,n] the unique zero λ = θα,n of multiplicity n. Moreover, one has for λ ∈ [0, θα,n]

pα,m(λ/qα,m+1), n = 2m + 1,

Fα,n(λ) =

1

λ/qα+1,m+1 spα+1,m(s) ds, n = 2m + 2. Proof. Let n = 2m + 1. Consider the polynomial (see (3.17))

m+1

pα,m(t) =

Bijα(qit), t ∈ R+,

i=1

where qi = qα,i. It has positive coeﬃcients Bi and the unique zero t = 1 of multiplicity 2m + 1 on the interval [0, 1] (see Theorem 3.1 (iii)). This and (3.18) imply that the function

m+1

qi qm+1

λ , λ ∈ R+,

Fα,n(λ) =

Bijα

![image 123](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile123.png>)

i=1

is the positive deﬁnite entire function of exponential type 1 such that λ = qm+1 is a unique zero of multiplicity 2m+1 on the interval [0, qm+1]. Therefore, L(Fα,n, 2m+1) ≤ qm+1.

Assume that n = 2m + 2. Consider the polynomial of type (3.17), with respect to the parameter α + 1:

m+1

Bi′jα+1(qi′t), t ∈ R+,

pα+1,m(t) =

i=1

where qi′ = qα+1,i. As above, Bi′ > 0 and A′i

m+1

A′i qi′2 − λ2

1

- (5.1) Bi′ = −b−α+11


.

,

=

![image 124](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile124.png>)

![image 125](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile125.png>)

![image 126](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile126.png>)

m+1

d

dt jα+1(qi′t)|t=1

i=1 (1 − λ2/qi′2)

![image 127](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile127.png>)

i=1

Set

m+1

1

Bi′ qi′2

(jα(qi′t) − jα(qi′)), where we have used (2.3).

P(t) =

spα+1,m(s) ds = 2(α + 1)

![image 128](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile128.png>)

t

i=1

In virtue of (2.4), dtd jα+1(qi′t)

= 2(α+1)jα(qi′) and therefore the polynomial pα+1,m is positive and decreasing on [0, 1) and it has zero of multiplicity 2m+1 at t = 1. Then

![image 129](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile129.png>)

t=1

it is clear that the polynomial P(t) is positive and decreasing on [0, 1) and it has zero of multiplicity 2m + 2 at t = 1.

Moreover, P(t) can be represented as follows

m+1

P(t) = B0′′ +

Bi′′jα(qi′t),

i=1

where Bi′′ > 0 for i ≥ 1 and, by (5.1),

m+1

m+1

Bi′ qi′2

A′i qi′2

B0′′ = −2(α + 1)

= b−α+11 > 0. We ﬁnish the proof deﬁning

jα(qi′) = b−α+11

![image 130](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile130.png>)

![image 131](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile131.png>)

i=1

i=1

m+1

Fα,n(λ) = B0′′ +

Bi′′jα

i=1

qi′ qm′ +1

λ , λ ∈ R+,

![image 132](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile132.png>)

which is a positive deﬁnite entire function of exponential type 1, having the unique zero λ = qm′ +1 of multiplicity 2m + 2 on [0, qm′ +1]. Therefore, L(Fα,n, 2m + 2) ≤ qm′ +1.

6. Generalized Logan problem for Dunkl and Fourier transforms

In this section we solve the Logan problem for the Dunkl transform. We remark that in this case we will use the function fα,m deﬁned by (1.3) for any α ≥ −1/2 unlike the case of Fourier transform where we deal with only α = d/2 − 1.

Basic facts on Dunkl harmonic analysis can be found in, e.g., [35]. Let a ﬁnite subset R ⊂ Rd \ {0} be a root system, G(R) ⊂ O(d) be a ﬁnite reﬂection group, generated by reﬂections {σa: a ∈ R}, where σa is a reﬂection with respect to hyperplane a, x = 0, and κ: R → R+ be a G-invariant multiplicity function. The Dunkl weight is given by

| a, x |2κ(a),

vκ(x) =

a∈R+

where R+ positive subsystem of R.

Let Eκ(x, y) be the symmetric Dunkl kernel associated with G and κ and eκ(x, y) = Eκ(x, iy) be the generalized exponential function. It is known that

ei ξ,y dµκx(ξ),

eκ(x, y) =

Rd

where µκx is a probability Borel measure supported on the convex hull of the G-orbit of x ∈ Rd. Moreover, one has (−∆κ)reκ( ·, y) = |y|2reκ( ·, y), r ∈ Z+, where ∆κ is the Dunkl Laplacian.

Denote

d 2 − 1 +

ακ =

κ(a).

![image 133](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile133.png>)

a∈R+

We will need the following Fischer-type decomposition for the Dunkl Laplacian: any even polynomial P(x), x ∈ Rd, of degree at most 2r can be represented by

m

r

|x|2m−2jHm,2j(x),

P(x) =

j=0

m=0

where Hm,2j are even κ-harmonic homogeneous polynomials of degree 2j, i.e., ∆κHm,2j = 0 (see [14, Sec. 5.1]). Such polynomials satisfy

∆κ|x|2iHm,2j(x) = 2i(2i + 4j + 2ακ)|x|2i−2Hm,2j(x)

(see [14, Lemma 5.1.9]), which implies

- (6.1) ∆lκ|x|2iHm,2j(x) = cijl|x|2i−2lHm,2j(x), cijl = 0 for i < l. The Dunkl transform is deﬁned as follows


Fκ(f)(y) = cκ

f(x)eκ(x, y)vκ(x) dx, y ∈ Rd,

![image 134](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile134.png>)

Rd

- d
- e−|x|2/2vκ(x) dx is the Macdonald–Mehta–Selberg integral. It is a uni-


where c−κ1 = R tary operator in L2(Rd, dµκ) such that Fκ−1(f)(x) = Fκ(f)(−x).

In the non-weighted case (κ = 0) we have dµ0(x) = (2π)−d/2 dx, e0(x, y) = ei x,y , ∆0 = ∆, and F0 is the Fourier transform.

Let f ∈ C(Rd) be such that

- (6.2) f(x) =

Rd

eκ(x, y) dµ(y)

with a ﬁnite nonnegative Borel measure µ. We call such functions positive deﬁnite with respect to the Dunkl transform, if µ is nonnegative. For κ = 0, by Bochner’s theorem, we arrive at the usual concept of positive deﬁniteness.

Denote by Eκ(Rd) the class of all even real-valued continuous bandlimited functions f of form (6.2) with the compactly supported measure µ. As usual, τ(f) is the exponential (spherical) type of f if suppµ ⊂ Bτd(f) (cf. [26]). Recall that λ(f) = sup{|x| > 0: f(x) > 0}.

We are now in a position to formulate the complete solution of the generalized Logan problem as well as the uncertainty principle relations for the Dunkl transform. Theorem 6.1. Let d ≥ N and m, s ∈ Z+.

(i) One has

inf λ((−1)mf)τ(f) = 2qα

κ,m+1,

where the inﬁmum is taken over all nontrivial functions f ∈ Eκ(Rd) such that the measure µ in (6.2) is nonnegative in some neighborhood of the origin and, if m ≥ 1, f ∈ L1(Rd, |x|2m−2vκ(x) dx) and the condition

∆jκFκ(f)(0) = 0, j = 0, . . ., m − 1, is fulﬁlled. Moreover, the positive deﬁnite radial function fα

κ,m(|x|) is the unique extremizer up to a positive constant. This function satisﬁes f ∈ L1(Rd, |x|2mvκ(x) dx) and ∆mκ Fκ(f)(0) = 0. (ii) One has

inf λ((−1)mf)τ(f) = 2qα

κ+s+1,m+1, where the inﬁmum is taken over all nontrivial functions f ∈ Eκ(Rd) ∩ L1(Rd, |x|2mvκ(x) dx) such that

- (6.3)


∆jκFκ(f)(0) = 0, j = 0, . . ., m − 1, ∆lκf(0) = 0, l = 0, . . ., s − 1,

and

∆mκ Fκ(f)(0) ≥ 0, ∆sκf(0) ≤ 0. Moreover, each extremizer has the form r(x)fα

κ+s+1,m(|x|) and satisﬁes the condition ∆mκ Fκ(f) = ∆sκf(0) = 0. Here

s+1

|x|2s+2−2jh2j(x) ≥ 0, |x| ≥ qα

κ+s,m+1,

r(x) =

j=0

where h2j(x) are even κ-harmonic polynomials of order at most 2j such that h0 > 0, h2j(0) = 0, j = 1, . . ., s + 1.

(iii) One has

inf λ((−1)mf)τ(f) = 2qα

κ+s,m+1, where the inﬁmum is taken over all nontrivial functions f ∈ Eκ(Rd) ∩ L1(Rd, |x|2m+2svκ(x) dx) such that

∆jκFκ(f)(0) = 0, j = s, . . ., m + s − 1, ∆mκ +sFκ(f)(0) ≥ 0. The function fα

κ+s,m(|x|) is the unique extremizer up to a positive constant. Moreover, this function satisﬁes ∆mκ +sFκ(f)(0) = 0.

- Remark 6.1. (1) For s = 0, the class of admissible functions in part (iii) of Theorem 6.1 contains admissible functions from part (i).


- (2) For κ = 0, part (i) implies Theorem 1.1, part (ii) implies Theorem 1.2, and

part (iii) implies Remark 1.2.

- (3) In part (ii), if a polynomial r(x) is nonnegative on Rd, then it is an even homo-


geneous polynomial of order 2s + 2. Proof. Our main idea is to reduce the proof of Theorem 6.1 to the case of Hankel transform of radial functions. Using polar coordinates, we have

∞

f(λx′) cκvκ(x′) dωκ(x′) λ2α

κ+1 dλ

cκ

f(x)vκ(x) dx =

Rd

0 Sd−1

∞

f(λx′) dωκ(x′) dνα

=

(λ), where dνα

κ

0 Sd−1

is given by (2.10), Sd−1 = {x′ ∈ Rd: |x′| = 1} is the Euclidean sphere, and dωκ(x′) = b−α1

κ

cκvκ(x′) dx′ is a probability measure on Sd−1 [36, Sec. 2.2]. In particular, for a radial function f(x) = f0(|x|) one has

κ

- (6.4) Fκ(f)(0) = cκ

Rd

f(x)vκ(x) dx =

∞

0

f0(λ) dνα

κ

(λ).

Let now f ∈ Eκ(Rd) be a function of type τ, written f(x) = B consider its radial part f0(λ) = S

- d τ
- eκ(x, y) dµ(y). We


d−1

f(λx′) dωκ(x′). Due to the well-known formula [36, Corollary 2.5]

Sd−1

eκ(λx′, y) dωκ(x′) = jα

κ

(λ|y|), y ∈ Rd, we conclude that f0 can be represented by

- (6.5) f0(λ) =

Bτd

jα

κ

(λ|y|) dµ(y) =

τ

0

jα

κ

(λt) dσ(t),

where σ is a function of bounded variation. It is also clear that if dµ in (6.5) is nonnegative in some neighborhood of the origin (or everywhere), then dσ satisﬁes the same property.

In light of (6.4) and (6.5), we derive that

- (6.6)


(f0)(0) = ∆rκFκ(f)(0) = (−1)rcκ

|x|2rf(x)vκ(x) dx,

Bαr

κHακ

Rd

|y|2r dµ(y).

f0(0) = ∆rκf(0) = (−1)r

Bαr

κ

Rd

In virtue of these relationships we note that if a function f is admissible in any of problems (i)–(iii) in Theorem 6.1, then its radial part f0(|x|) is also admissible in

the same problem and λ((−1)mf0)τ(f0) ≤ λ((−1)mf)τ(f). Hence, the corresponding inﬁmums are attained on radial functions.

Formulas (6.5) and (6.6) also imply that radial extremizers in problems (i)–(iii) coincide with extremizers in Theorems 3.1 and 4.1 for Hankel transforms. Thus, the functions fα

κ,m(|x|), |x|2s+2fα

κ+s,m(|x|) are extremizers for problems (i), (ii), and (iii), respectively.

κ+s+1,m(|x|), and fα

Note that for any admissible function f from part (i), taking into account Theorem 3.1, we have that ∆mκ Fκ(f)(0) = Bαm

(f0)(0) ≥ 0. This implies part (1) of

κHακ

Remark 6.1. It is left to prove the uniqueness of extremizers in problems (i)–(iii). Part (ii). Let τ = 2, qj′ = qα

κ+s+1,j, and f be an extremizer. Then (−1)m+1f(x) ≥ 0 for |x| ≥ qm′ +1 and its radial part is

- (6.7) f0(λ) = cλ2s+2fα

κ+s+1,m(λ), c > 0. Therefore, S

d−1

f(qj′x′) dωκ(x′) = 0 for j ≥ m + 1, which gives f(x) = 0 if |x| = qj′,

- j ≥ m + 1. Moreover, f ∈ L1(Rd, |x|2mvκ(x) dx), since, in light of (4.4),


cκ

|x|≥qm′ +1

|x|2m|f(x)|vκ(x) dx = (−1)m+1c

∞

qm′ +1

λ2m+2s+2fα

κ+s+1,m(λ) dνα

κ

(λ) < ∞.

Denote f(x) = f(λx′) = fx′(λ), where λ = |x|, x′ = x/|x|. Since f is even and fx′(λ) = B bounded on R. By Fubini’s theorem, fx′ ∈ L1(R+, λ2m dνα

- d τ
- eκ(λx′, y) dµ(y), then fx′ is the even entire function of exponential type τ


κ

).

The function fx′(λ) keeps its sign for λ ≥ qm′ +1 and fx′(qj′) = 0 for j ≥ m+ 1. Hence, qj′ are double zeros for j ≥ m + 2. Therefore, we have

- (6.8) fx′(λ) = rx′(λ)fα

κ+s+1,m(λ)

with some even entire function rx′(λ) of exponential type. Similar to the proof of uniqueness of extremizer fα,m in Theorem 3.1, using Lemmas 2.2 and 2.3, we obtain that rx′(λ) is an even polynomial of degree at most 2s+2 (otherwise fx′ ∈/ L1(R+, λ2m dνα

κ

)). Thus, by (6.8), we have

- (6.9) f(x) = r(x)fα


κ+s+1,m(|x|), where r(x) = sk+1=0 ck(x′)|x|2k. Taylor’s expansions are given by f(x) =

∞

∞

aj|x|2j,

Al(x′)|x|2l, fα

κ+s+1,m(|x|) =

j=0

l=0

where Al(x′) are homogeneous polynomials of degree 2l, A0(x′) = A0, and a0 = 1. Therefore, we arrive at the linear system

l

cj(x′)al−j = Al(x′), l = 0, 1, . . ., s + 1,

j=0

in variables cj(x′). We derive that

c0 = A0, cj(x′) = Aj(x′) +

j−1

bijAi(x′), j = 1, . . ., l.

i=0

Thus, cj(x′) = Aj(x′) + i j=0−1 bijAi(x′)|x|2j−2i are homogeneous polynomials of degree 2j, j = 1, . . ., l, and then r(x) is an even polynomial of degree 2s + 2.

Now we ﬁnd under which conditions on r the function f is an extremizer. Since λ((−1)mf) = qm′ +1, we necessarily have

r(x) ≥ 0, |x| ≥ qm′ +1.

We write r(x) = sk+1=0 r2k(x), where r2k(x) are homogeneous polynomials of degree 2k. By (6.9) and (6.7),

s+1

λ2kr2k(x′) dωκ(x′) = cλ2s+2fα

κ+s+1,m(λ). This implies

f0(λ) = fα

κ+s+1,m(λ)

k=0 Sd−1

- (6.10)

Sd−1

r2k(x′) dωκ(x′) = 0, k = 0, 1, . . ., s,

Sd−1

r2s+2(x′) dωκ(x′) > 0. In particular, r0 = 0. Furthermore, (6.10), the Fisher-type decomposition

r(x) =

s+1

j=0

|x|2s+2−2jh2j(x)

with h2j(x) being even κ-harmonic polynomials of order at most 2j, and the fact that h2j(0) = S

d−1

h2j(x) dωκ(x′) imply that

- (6.11) h0 > 0, h2j(0) = 0, j = 1, . . ., s + 1.


It is enough to verify that the function f(x) = r(x)fα

κ+s+1,m(|x|) is an extremizer. Let us show (6.3). By Theorem 4.1, for k = 0, 1, . . ., m we have

cκ

|x|2kf(x)vκ(x) dx

Rd

s+1

∞

λ2k+2s+2−2jfα

=

(λ)

κ+s+1,m(λ) dνα

κ

0

j=0

Sd−1

s+1

∞

λ2k+2s+2−2jfα

=

h2j(0)

(λ)

κ+s+1,m(λ) dνα

κ

0

j=0

∞

λ2k+2s+2fα

= h0(0)

(λ) = 0. Since

κ+s+1,m(λ) dνα

κ

0

f(x) =

s+1

|x|2s+2−2jh2j(x)

j=0

∞

∞

ck|x|2k =

ck

k=0

k=0

s+1

j=0

h2j(x)vκ(x′) dωκ(x′)

|x|2s+2−2j+2kh2j(x),

both (6.1) and (6.11) imply that ∆lκf(0) = 0 for l = 0, 1, . . ., s. Thus, condition (6.3) holds and moreover, ∆mκ Fκ(f) = ∆sκf(0) = 0 is valid.

Finally, let us show that if r(x) ≥ 0 on Rd, then r(x) is homogeneous polynomials of degree 2s + 2. Assume that r(x) = λk

0 s+1

k=k0 λk−k

r2k(x′), x = λx′, where 1 ≤

0

(x′) dωκ(x′) = 0, we derive r(λx′0) < 0 for some x′0 ∈ Sd−1 and suﬃciently small λ > 0. This contradiction implies that r(x) = r2s+2(x).

- k0 ≤ s and r2k


(x) = 0 (recall that r0 = 0). Using S

r2k

d−1

0

0

Parts (i) and (iii) with s = 0. Similar reasonings as above imply that any extremizer has the form cfα

κ,m(|x|) with c > 0.

Part (iii) with s ≥ 1. As in the proof of Theorem 4.1, we reduce the question about uniqueness of an extremizer f in part (iii) to similar problem in part (ii) with s − 1 in place of s. Thus, we arrive at the function cfα

κ+s,m(|x|), c > 0.

7. Chebyshev systems of normalized Bessel functions

Recall that NI(f) stands for the number of zeros of f on I, counting multiplicity. A family of real-valued functions {ϕk(t)} deﬁned on an interval I ⊂ R is a Chebyshev system (T-system) if for any n ∈ N and any nontrivial linear combination

n

Akϕk(t),

P(t) =

k=1

there holds NI(P) ≤ n − 1, see, e.g., [1, Chap. II].

As above we assume that α ≥ −1/2, qk = qα,k, and qk′ = qα+1,k for k ∈ N. The main result of this section is the following theorem.

- Theorem 7.1. (i) The families of the Bessel functions


- (7.1) {jα(qkt)}∞k=1, {1, jα(qk′ t)}∞k=1


form Chebyshev systems on [0, 1) and [0, 1], respectively. (ii) The families of the Bessel functions

{jα+1(qkt)}∞k=1, {jα(qk′ t) − jα(qk′ )}∞k=1 form Chebyshev systems on (0, 1).

For α = −1/2 this theorem becomes the well-known result for trigonometric systems, which has many applications in approximation theory (see [1, Chap. II]). For α > −1/2 this result seems to be new.

We will use the following Sturm’s theorem on zeros of linear combinations of eigenfunctions of Sturm–Liouville problem. This result is not widely known in the literature, see the discussion in [5].

Theorem 7.2 (Sturm, 1836; Liouville, 1836). Let {Vk}∞k=1 be the system of eigenfunctions associated to eigenvalues ρ1 < ρ2 < . . . of the following Sturm–Liouville problem on the interval [a, b]:

- (7.2) (KV ′)′ + (ρG − L)V = 0, (KV ′ − hV )(a) = 0, (KV ′ + HV )(b) = 0,


where G, K, L ∈ C[a, b], K ∈ C1(a, b), K, G > 0 on (a, b), h, H ∈ [0, ∞] and ρ denotes the spectral parameter.

Then for any nontrivial real polynomial of the form P =

n

AkVk, m, n ∈ N, m ≤ n, we have

k=m

m − 1 ≤ N(a,b)(P) ≤ n − 1. In particular, every k-th eigenfunction Vk has exactly k − 1 simple zeros in (a, b).

For trigonometric system this result is known as the Sturm–Hurwitz theorem (see, e.g., [3]).

Note that in the proof given by Liouville (see [5]) it is enough to assume that K, G > 0 only on the interval (a, b). This allows us to include the singular case, that is, when K

and G may have zeros at the endpoints of [a, b]. In particular, we may deal with the Sturm–Liouville problem for Bessel functions.

Proof of Theorem 7.1. We will use the fact that, by Theorem 7.2, the system of eigenfunctions {Vk}∞k=1 is the Chebyshev system. We note that (7.1) are the families of eigenfunctions for the (singular for α > −1/2) Sturm–Liouville problem (see [29])

- (7.3)

(t2α+1u′(t))′ + λ2t2α+1u(t) = 0, t ∈ [0, 1], u′(0) = 0, cosθ u(1) + sinθ u′(1) = 0,

where θ ∈ [0, π/2] and λ2 is the spectral parameter. Here for the family {jα(qkt)}∞k=1, we assume the Dirichlet conditions θ = 0 and u(1) = 0 and, for {1, jα(qk′ t)}∞k=1, the Neumann conditionds θ = π/2 and u′(1) = 0.

In virtue of (2.3), we have

cosθ jα(λ) − sin θ

λ2 2(α + 1)

![image 135](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile135.png>)

jα+1(λ) = 0, or, equivalently,

- (7.4) cosθ Jα(λ) − sinθ λJα+1(λ) = AJα(λ) + BλJα′ (λ) = 0,


where A = cosθ − α sinθ, B = sin θ. Since A/B + α = tanθ ≥ 0, α > −1, we have that equation (7.4) has only real roots (see [6, Sec. 7.9]). Due to evenness, it is enough to consider only nonnegative zeros, which we denote by 0 ≤ r1 < r2 < . . .. Then the eigenvalues and the eigenfunctions of the Sturm–Liouville problem (7.3) are rk2 and jα(rkt), k ∈ N, respectively. In particular, we have rk = qk for θ = 0 and rk = qk′−1 for θ = π/2, where we put q0′ = 0.

The Sturm–Liouville problem (7.3) is a particular case of the problem (7.2); take K = G = w, L = 0, r = λ2, h = 0, and H = cot θ. Then the statement of part (i) is valid for the interval (0, 1). In order to include the endpoints, we ﬁrst prove part (ii).

Let us show that the family {jα+1(qkt)}∞k=1 is the Chebyshev system on (0, 1). Assume

that the polynomial P(t) = nk=1 Akjα+1(qkt) has n zeros on (0, 1). We consider F(t) = t2α+2P(t). It has at least n + 1 zeros including t = 0. By Rolle’s theorem, for a smooth

real function f one has N(a,b)(f′) ≥ N(a,b)(f) − 1 (see [5]). Thus, P′ has at least n zeros on (0, 1). In light of (2.4), we obtain

F′(t) = 2(α + 1)t2α+1

n

Akjα(qkt).

k=1

This contradicts the fact that {jα(qkt)}∞k=1 is the Chebyshev system on (0, 1). To prove that {jα(qk′ t) − jα(qk′ )}∞k=1 is the Chebyshev system on (0, 1), assume that

P(t) = nk=1 Ak(jα(qk′ t) − jα(qk′ )) has n zeros on (0, 1). Taking into account the zero t = 1, its derivative (see (2.3))

t 2α + 2

P′(t) = −

![image 136](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile136.png>)

n

Akqk′2jα+1(qk′ t)

k=1

has at least n zeros on (0, 1). This contradicts the fact that {jα+1(qα+1,kt)}∞k=1 is the Chebyshev system on (0, 1).

Now we are in a position to show that the ﬁrst system in (7.1) is Chebyshev on

[0, 1). Note that if P(t) = nk=1 Akjα(qkt) has n zeros on [0, 1), then always P(0) = 0. Moreover, P(1) = 0. Therefore, P′ has at least n zeros on (0, 1), which is impossible

n

since P′(t) = −2αt+2

k=1 Akqk2jα+1(qkt) and jα+1(qkt) is the Chebyshev system on (0, 1).

![image 137](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile137.png>)

Similarly, if P(t) = k n=0−1 Akjα(qk′ t) (we assume q0′ = 0) has n zeros on [0, 1], then one of the endpoints is a zero. Then P′(t) = −2αt+2 k n=1−1 Akqk′2jα+1(qk′ t) has at least n − 1 zeros in (0, 1), which is impossible for Chebyshev system {jα+1(qα+1,kt)}∞k=1.

![image 138](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile138.png>)

8. An alternative proof of positive definiteness of the function gα,m

In [12], the positive deﬁniteness of the function gd/2−1,m given by (1.4) was proved based on the use of classical translation operator in Rd. This causes the restriction α = d/2 − 1. Another approach to see that gα,m is positive deﬁnite, is to employ Bochner’s theorem and show that the Hankel transform of gα,m is nonnegative, which is equivalent to fact that the matrix of the generalized translations (Tx

αif(xj))Ni,j=1 is positive deﬁnite, see Section 2. Here we follow this approach and ideas from [12].

(α,α) n (θ)

Let Rn(α)(θ) = P

be the normalized Jacobi polynomial and −1 < rn < · · · <

![image 139](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile139.png>)

Pn(α,α)(1)

r1 < 1 be its zeros, see, e.g., [37]. Deﬁne the generalized translation operator on [−1, 1] as follows

√

π

![image 140](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile140.png>)

![image 141](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile141.png>)

- (8.1) τθf(ρ) = cα


1 − θ2 1 − ρ2 + 2θρcosϕ) sin2α ϕ dϕ,

f(

0

where cα is deﬁned in (2.8). We remark that τθRn(α)(ρ) = Rn(α)(θ)Rn(α)(ρ). Consider the polynomial pn−k(θ) = R

(α) n (θ)

(θ−r1)···(θ−rk). It was shown in [10] that

![image 142](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile142.png>)

n−k

asRs(α)(θ), as ≥ 0, i = 0, . . ., n − k.

pn−k(θ) =

s=0

pn−k(θj))ni,j=1 is positive semideﬁnite, i.e.,

This implies that for any choice of θ1, . . ., θN ⊂ [−1, 1] the matrix (τθ

i

n−k

N

cicj τθ

pn−k(θj) =

i

![image 143](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile143.png>)

s=0

i,j=1

N

cicj τθ

as

![image 144](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile144.png>)

i,j=1

n−k

N

cicj Rs(α)(θi)Rs(α)(θj) =

=

as

![image 145](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile145.png>)

s=0

i,j=1

Rs(α)(θj)

i

n−k

as

s=0

N

ciRs(α)(θi)

i=1

2

≥ 0.

Recall again that qi = qα,i are zeros of jα(y) and gk(y) = j

α(y)

(q12−y2)···(qk2−y2). We note (see [37, Sec. 8.1]) that

![image 146](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile146.png>)

y2 2n2

1 n2

Rn(α) 1 −

= jα(y) uniformly in y ∈ [0, L] for any positive L. Since ([37, Sec. 8.1])

+ o

lim

![image 147](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile147.png>)

![image 148](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile148.png>)

n→∞

qi2 2n2

1 n2

, then setting θ = 1 − y2/(2n2) + o(1/n2), we obtain

+ o

ri = 1 −

![image 149](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile149.png>)

![image 150](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile150.png>)

(2n2)k(θ − r1) · · ·(θ − rk) = (q12 − y2) · · ·(qk2 − y2) uniformly in y ∈ [0, L].

lim

n→∞

Let us show that there holds

y2 2n2

1 n2

(2n2)−kpn−k 1 −

- (8.2) lim


+ o

= gk(y)

![image 151](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile151.png>)

![image 152](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile152.png>)

n→∞

uniformly in y ∈ [0, L]. This is true on any interval without arbitrarily small neighborhoods of points qi, i = 1, . . ., k. Without loss of generality, it is enough to consider a

small neighborhood of q1, since (q22 − y2) · · ·(qk2 − y2) is bounded away from zero in this neighborhood.

Using (2.2) implies

jα(y) q12 − y2

![image 153](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile153.png>)

∞

y2ν − q12ν q12 − y2

(−1)νΓ(α + 1) 4νν! Γ(ν + α + 1)

jα(y) − jα(q1) q12 − y2

=

=

![image 154](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile154.png>)

![image 155](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile155.png>)

![image 156](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile156.png>)

ν=1

∞

ν−1

(−1)ν−1Γ(α + 1) 4νν! Γ(ν + α + 1)

y2sq12(ν−1−s)

=

![image 157](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile157.png>)

ν=1

s=0

∞

∞

y2 q12

(−1)kΓ(α + 1)q12k 4k+1(k + 1)! Γ(k + α + 2)

s

=

![image 158](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile158.png>)

![image 159](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile159.png>)

s=0

k=s

∞

∞

y2 4

q12 4

Γ(α + 1) Γ(s + l + 2)Γ(s + l + α + 2) −

1 4

s

−

=

![image 160](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile160.png>)

![image 161](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile161.png>)

![image 162](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile162.png>)

![image 163](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile163.png>)

s=0

l=0

l

.

Similarly, if θ = 1 − y2/(2n2) + o(1/n2), then [37, Sec. 4.21]

n

Rn(α)(θ) θ − r1

Γ(n + ν + 2α + 1)Γ(n + α + 1)((θ − 1)ν − (r1 − 1)ν) 2νν! Γ(n − ν + 1)Γ(n + 2α + 1)Γ(ν + α + 1)(θ − r1)

n + α n

=

![image 164](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile164.png>)

![image 165](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile165.png>)

ν=1

n

ν−1

Γ(n + ν + 2α + 1)Γ(n + α + 1) 2νν! Γ(n − ν + 1)Γ(n + 2α + 1)Γ(ν + α + 1)

(θ − 1)s(r1 − 1)ν−s−1

=

![image 166](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile166.png>)

ν=1

s=0

n−1

n−1

Γ(n + ν + 2α + 2)Γ(n + α + 1)(θ − 1)s(r1 − 1)ν−s 2ν+1(ν + 1)! Γ(n − ν)Γ(n + 2α + 1)Γ(ν + α + 2)

=

![image 167](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile167.png>)

s=0

ν=s

n−1

n−1−s

Γ(n + s + l + 2α + 2)Γ(n + α + 1)(θ − 1)s(r1 − 1)l 2s+lΓ(s + l + 2)Γ(n − s − l)Γ(n + 2α + 1)Γ(s + l + α + 2)

- 1

![image 168](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile168.png>)

- 2


=

![image 169](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile169.png>)

s=0

l=0

n−1

n−1−s

Γ(n + s + l + 2α + 2)Γ(n + α + 1)(−y2/4)s(−q12/4)l(1 + o(1/n2)) n2(s+l)Γ(s + l + 2)Γ(n − s − l)Γ(n + 2α + 1)Γ(s + l + α + 2)

- 1

![image 170](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile170.png>)

- 2


=

.

![image 171](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile171.png>)

s=0

l=0

Since

nα Γ(α + 1)

- Γ(n + a)

![image 172](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile172.png>)

- Γ(n + b) ∼ na−b,


n + α n ∼

, n → ∞, then, for ﬁxed s and l,

![image 173](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile173.png>)

Γ(α + 1)Γ(n + s + l + 2α + 2)Γ(n + α + 1)(1 + o(1/n2))(−y2/4)s(−q12/4)l 4n2(s+l+1)+αΓ(n − s − l)Γ(n + 2α + 1)Γ(s + l + 2)Γ(s + l + α + 2) ∼

![image 174](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile174.png>)

Γ(α + 1)(−y2/4)s(−q12/4)l 4Γ(s + l + 2)Γ(s + l + α + 2)

- (8.3) , n → ∞, and, for θ = 1 − y2/(2n2) + o(1/n2), we have, uniformly on y ∈ [0, L],


![image 175](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile175.png>)

Rn(α)(θ) θ − r1

jα(y) q12 − y2

2−1nα−2

=

.

lim

![image 176](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile176.png>)

![image 177](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile177.png>)

n→∞

We should explain how we take the limit under the sum. Since for any n ≥ 1, 0 ≤ s ≤ n − 1, 0 ≤ l ≤ n − 1 − s,

Γ(n + s + l + 2α + 2) Γ(n + 2α + 1) ≤ (2n + 2α)s+l+1,

![image 178](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile178.png>)

Γ(n) Γ(n − s − l) ≤ ns+l,

Γ(n + α + 1)

Γ(n) ≤ C(α)nα+1, then (8.3) can be bounded from above by

![image 179](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile179.png>)

![image 180](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile180.png>)

Γ(α + 1)Γ(n + s + l + 2α + 2)Γ(n + α + 1)|1 + o(1/n2)|(y2/4)s(q12/4)l 4n2(s+l+1)+αΓ(n − s − l)Γ(n + 2α + 1)Γ(s + l + 2)Γ(s + l + α + 2)

![image 181](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile181.png>)

(y2/4)s(q12/4)l Γ(s + l + 2)Γ(s + l + α + 2)

≤ C1(α)

. Moreover, the following series converges uniformly on any interval [0, L], q1 ≤ L,

![image 182](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile182.png>)

∞

∞

(y2/4)s(q12/4)l Γ(s + l + 2)Γ(s + l + α + 2)

![image 183](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile183.png>)

s=0

l=0

∞

∞

∞

∞

(L2/4)s+l Γ(s + l + 2)Γ(s + l + α + 2) ≤

(L2/4)s+l (s + l + 1)!

≤

![image 184](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile184.png>)

![image 185](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile185.png>)

s=0

s=0

l=0

l=0

∞

∞

(L2/4)m m!

(L2/4)m (m + 1)!

2/4.

= eL

=

=

(m + 1)

![image 186](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile186.png>)

![image 187](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile187.png>)

m=0

m=0

Thus, (8.2) is proved. Let

![image 188](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile188.png>)

xi n ≤ 1, θi = 1 −

xi n

2

xi ∈ [0, ∞),

, i = 1, . . ., N. For i, j = 1, . . ., N, there holds, uniformly on ϕ ∈ [0, π] and for suﬃciently large n,

![image 189](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile189.png>)

![image 190](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile190.png>)

yij2 2n2

![image 191](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile191.png>)

![image 192](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile192.png>)

xixj n2

1 n2

xi n

xj n

2

2

, where

+ 2

cosϕ = 1 −

+ o

1 −

1 −

![image 193](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile193.png>)

![image 194](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile194.png>)

![image 195](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile195.png>)

![image 196](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile196.png>)

![image 197](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile197.png>)

![image 198](<2019-gorbachev-uncertainty-principles-eventually-constant_images/imageFile198.png>)

yij = x2i + x2j − 2xixj cosϕ. Therefore, by (8.2) and the deﬁnitions of the generalized translation operator (2.14) and (8.1), for any i, j,

(2n2)−kτθ

pn−k(θj) = Tx

α gk(xj). Since the matrix (τθ

lim

i

i

n→∞

pn−k(θj)) is positive semideﬁnite, then the matrix (Tx

αigk(xj)) is also positive semideﬁnite. Then, by Levitan’s theorem, Hα(gk)(t) ≥ 0 and the functions gk and (1.4) are positive deﬁnite.

i

Acknowledgements. We would like to thank P. B´erard who pointed out the possibility to apply Liouville’s method to show Theorem 7.1 and E. Berdysheva for helpful comments.

References

- [1] N.N Achieser, Theory of Approximation, New York, Dover, 2004.
- [2] N.B. Andersen and M. de Jeu, Elementary proofs of Paley–Wiener theorems for the Dunkl transform on the real line, Int. Math. Res. Notices 2005 (2005), no. 30, 1817–1831.
- [3] W.O. Amrein, A.M. Hinz, and D.B. Pearson, eds., Sturm–Liouville Theory: Past and Present, Basel, Birkh¨auser, 2005.
- [4] W. Banaszczyk, New bounds in some transference theorems in the geometry of numbers, Math. Ann. 296 (1993), no. 4, 625–635.
- [5] P. B´erard and B. Helﬀer, Sturm’s theorem on zeros of linear combinations of eigenfunctions, arXiv:1706.08247.


- [6] G. Bateman, A. Erd´elyi, et al., Higher Transcendental Functions, Vol. II, McGraw Hill Book Company, New York, 1953.
- [7] E.E. Berdysheva, Two related extremal problems for entire functions of several variables, Math. Notes 66 (1999), no. 3, 271–282.
- [8] J. Bourgain, L. Clozel, and J.-P. Kahane, Principe d’Heisenberg et fonctions positives, Ann. Inst. Fourier (Grenoble) 60 (2010), no. 4, 1215–1232.
- [9] M. D. Buhmann, Radial basis functions: Theory and implementations, Cambridge University Press, 2003.
- [10] H. Cohn and A. Kumar, Universally optimal distribution of points on spheres, J. Amer. Math. Soc. 20 (2007), no. 1, 99–148.
- [11] H. Cohn, A. Kumar, S.D. Miller, D. Radchenko, and M. Viazovska, The sphere packing problem in dimension 24, Ann. of Math. 185 (2017), no. 3, 1017–1033.
- [12] H. Cohn and M. de Courcy-Ireland, The Gaussian core model in high dimensions, Duke Math. J. 167 (2018), no. 13, 2417–2455.
- [13] H. Cohn and F. Gonc¸alves, An optimal uncertainty principle in twelve dimensions via modular forms, to appear in Invent. Math., arXiv:1712.04438.
- [14] C. F. Dunkl and Y. Xu, Orthogonal polynomials of several variables, Encyclopedia of Mathematics and Its Applications, Vol. 81, Cambridge University Press, Cambridge, 2001.
- [15] R.E. Edwards, Fourier Series: A Modern Introduction, Vol. 1, New York, Springer, 1979.
- [16] R. B. Ghanem, C. Frappier, Explicit quadrature formulae for entire functions of exponential type, J. Approx. Theory 92 (1998), no. 2, 267–279.
- [17] S. Ghobber and P. Jaming, The Logvinenko–Sereda theorem for the Fourier–Bessel transform, Integr. Transf. Spec. F. 24 (2013), no. 6, 470–484.
- [18] F. Gonc¸alves, D. Oliveira e Silva, and S. Steinerberger, Hermite polynomials, linear ﬂows on the torus, and an uncertainty principle for roots, J. Math. Anal. Appl. 451 (2017), no. 2, 678–711.
- [19] D.V. Gorbachev and V.I. Ivanov, An extremum problem for polynomials related to codes and designs, Math. Notes 67 (2000), no. 4, 433–438.
- [20] D.V. Gorbachev, Extremum problems for entire functions of exponential spherical type, Math. Notes 68 (2000), no. 2, 159–166.
- [21] D.V. Gorbachev, V.I. Ivanov, and R.A. Veprintsev, Optimal argument in sharp Jackson’s inequality in the space L2 with the hyperbolic weight, Math. Notes 96 (2014), no. 6, 338–348.
- [22] D.V. Gorbachev and V.I. Ivanov, Gauss and Markov quadrature formulae with nodes at zeros of eigenfunctions of a Sturm–Liouville problem, which are exact for entire functions of exponential type, Sbornik: Math. 206 (2015), no. 8, 1087–1122.
- [23] D.V. Gorbachev and V.I. Ivanov, Turan, Fejer, and Boman extremal problems for the multidimensional Fourier transform in the eigenfunctions of a Sturm–Liouville problem, to appear in Sbornik: Math. (2019).
- [24] D.V. Gorbachev, V.I. Ivanov, and S.Yu. Tikhonov, Positive Lp-bounded Dunkl-type generalized translation operator and its applications, Constr. Approx. (2019), https://doi.org/10.1007/s00365018-9435-5.
- [25] G.R. Grozev and Q.I. Rahman, A quadrature formula with zeros of Bessel functions as nodes, Math. Comp. 64 (1995), 715–725.
- [26] M. de Jeu, Paley–Wiener theorems for the Dunkl transform, Trans. Amer. Math. Soc. 358 (2006), no. 10, 4225–4250.
- [27] T. Koornwinder, A new proof of a Paley–Wiener type theorem for the Jacobi transform, Ark. Mat. 13 (1975), 145–159.
- [28] B.Ya. Levin, Distribution of Zeros of Entire Functions, Providence, RI, Amer. Math. Soc., 1980.
- [29] B.M. Levitan, Expansion in Fourier series and integrals with Bessel functions, Uspekhi Mat. Nauk 6 (1951), no. 2, 102–143. [in Russian]
- [30] B.M. Levitan and I.S. Sargsjan, Introduction to spectral theory: Selfadjoint ordinary diﬀerential operators, Transl. Math. Monogr., Vol. 39, Amer. Math. Soc., Providence, Rhode Island, 1975.
- [31] B.F. Logan, Extremal problems for positive-deﬁnite bandlimited functions. I. Eventually positive functions with zero integral, SIAM J. Math. Anal. 14 (1983), no. 2, 249–252.
- [32] B.F. Logan, Extremal problems for positive-deﬁnite bandlimited functions. II. Eventually negative functions, SIAM J. Math. Anal. 14 (1983), no. 2, 253–257.
- [33] B.F. Logan, Extremal problems for positive-deﬁnite bandlimited functions. III. The maximum number of zeros in an interval [0,T], SIAM J. Math. Anal. 14 (1983), no. 2, 258–268.


- [34] R. Nessel and G. Wilmes, Nikolskii-type inequalities for trigonometric polynomials and entire functions of exponential type, J. Austral. Math. Soc., 25 (1978), no. 1, 7–18.
- [35] M. R¨osler, Dunkl Operators: Theory and applications, Lecture Notes in Math., Berlin, Springer 1817 (2003), 93–135.
- [36] M. R¨osler, A positive radial product formula for the Dunkl kernel, Trans. Amer. Math. Soc. 355

(2003), 2413–2438.

- [37] G. Szeg¨o, Orthogonal Polynomials, AMS Colloquium Publications 23, Providence, Amer. Math. Soc., 1975.
- [38] M.S. Viazovska, The sphere packing problem in dimension 8, Ann. of Math. 185 (2017), no. 3, 991–1015.
- [39] V.A. Yudin, Multidimensional Jackson theorem in L2, Math. Notes 29 (1981), no. 2, 158–162.
- [40] V.A. Yudin, Two external problems for trigonometric polynomials, Sbornik: Math. 187 (1996), no. 11, 1721–1136.
- [41] V.A. Yudin, Disposition of points on a torus and extremal properties of polynomials, Proc. Steklov Inst. Math. 219 (1997), 447–457.


D. Gorbachev, Tula State University, Department of Applied Mathematics and Com-

puter Science, 300012 Tula, Russia E-mail address: dvgmail@mail.ru V. Ivanov, Tula State University, Department of Applied Mathematics and Computer

Science, 300012 Tula, Russia E-mail address: ivaleryi@mail.ru S. Tikhonov, Centre de Recerca Matematica,` Campus de Bellaterra, Edifici C 08193

Bellaterra, Barcelona, Spain; ICREA, Pg. Llu´is Companys 23, 08010 Barcelona, Spain, and Universitat Autonoma´ de Barcelona

E-mail address: stikhonov@crm.cat

