arXiv:1310.2510v3[math.CA]22Oct2014

Global Maximizers for the Sphere Adjoint Fourier Restriction Inequality

Damiano Foschi

Dipartimento di Matematica e Informatica, Universita` di Ferrara via Macchiavelli 35, 44121 Ferrara - Italy

![image 1](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile1.png>)

Abstract

We show that constant functions are global maximizers for the adjoint Fourier restriction inequality for the sphere.

Keywords: Fourier restriction, Stein Tomas inequality, maximizers, sphere

![image 2](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile2.png>)

- 1. Introduction


Recently, Christ and Shao [1, 2] have proved the existence of maximizers for the adjoint Fourier restriction inequality of Stein and Tomas [5] for the sphere:

fσ L

4(R3) f L2(S2) , (1)

where S2 = x ∈ R3: |x| = 1 is the standard unit sphere equipped with its natural surface measure σ induced by the Lebesgue measure on R3. Here the Fourier transform of a integrable function f supported on the sphere is deﬁned for any x ∈ R3 by

e−ix·ωf(ω)dσω. Let us denote by R the optimal constant in (1):

fσ(x) =

S2

fσ L

4(R3) f L2(S2)

.

R := sup

![image 3](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile3.png>)

f∈L2(S2),f =0

In [1], using concentration compactness methods, they prove that there exist sequences {fk} of nonnegative even functions in L2(S2) which converge to some maximizer of the ratio fσ L4/ f L2, but they do not compute the exact value of R. Nevertheless, they show that constant functions are local maximizers and raise the question of whether constants are actually global maximizers. The purpose of this note is to give a positive answer to that question:

![image 4](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile4.png>)

Email address: damiano.foschi@unife.it (Damiano Foschi)

Preprint submitted to Elsevier October 26, 2013

Theorem 1.1. A nonnegative function f ∈ L2(S2) is a global maximizer for (1) if and only if it is a non zero constant, and we have

1σ L

4(R3) 1 L2(S2)

R =

= 2π.

![image 5](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile5.png>)

When we combine Theorem 1.1 with the results of [2, Theorem 1.2] we obtain that all complex valued global maximizers for (1) are of the form

f(ω) = keiθeiξ·ω, for some k > 0, θ ∈ R, ξ ∈ R3.

A large part of the analysis carried out in [1] is local in nature and it is based on a comparison between the case of the sphere and that of a paraboloid which approximates the sphere at one point. Here we are able to keep everything global, thanks to an interesting geometric feature of the sphere, which is expressed in Lemma 4.2. It essentially says: when the sum ω1 +ω2+ω3 of three unit vectors is again a unit vector, then we have

|ω1 + ω2|2 + |ω1 + ω3|2 + |ω2 + ω3|2 = 4.

In order to ﬁnd maximizers for (1), we follow the spirit of the proof of analogous results obtained by the author for the paraboloid and the cone [4]. The main steps are:

- • The exponent 4 is an even integer and we can view the L4 norm as a L2 norm of a product, which becomes, through the Fourier transform, a L2 norm of a convolution. We write the L2 norm of a convolution of measures supported on the sphere as a quadrilinear integral over a submanifold of (S2)4.
- • A careful application of the Cauchy-Schwarz inequality over that submanifold allows us to control the quadrilinear integral by some bilinear integral over (S2)2.
- • Finally, by a spectral decomposition of the bilinear integral using spherical harmonics will show that the optimal bounds for the bilinear integral are obtained when we consider constant data.


We will see that every time an inequality appears, the choice of f constant will correspond to the case of equality.

- 2. Quadrilinear form associated to the estimate


- Deﬁnition 2.1. Given a complex valued function f deﬁned on S2, its antipodally conjugate f⋆ is deﬁned by f⋆(ω) := f(−ω).


![image 6](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile6.png>)

By Plancherel’s theorem we have

fσ

2 L4(R3)

![image 7](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile7.png>)

= fσ fσ

= fσ f⋆σ

L2(R3)

=

L2(R3)

= fσ ∗ f⋆σ

3

2 fσ ∗ f⋆σ L

2(R3). (2)

= (2π)

![image 8](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile8.png>)

L2(R3)

- When f is constant we can explicitely compute this convolution. Lemma 2.2. For x ∈ R3 we have


2π |x|

δ x − ω − ν dσω dσν =

σ ∗ σ(x) =

χ |x| 2 ,

![image 9](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile9.png>)

(S2)2

with norm σ ∗ σ L2(R3) = 25/2π3/2.

The notation δ · stands for the Dirac’s delta measure concentrated at the origin of Rn. Proof. The surface measure of the sphere can be written as

dσω = δ 1 − |ω| dω = 2 δ 1 − |ω|2 dω. The convolution then can be written as

δ 1 − |x − ω|2 dσω = 2

σ ∗ σ(x) = 2

S2

π

1

2π |x|

2π |x|

δ cosθ − |x2| sinθ dθ =

=

![image 10](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile10.png>)

![image 11](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile11.png>)

![image 12](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile12.png>)

0

−1

The norm can then be easily computed,

δ 2x · ω − |x|2 dσω =

S2

2π |x|

χ |x| 2

δ c − |x2| dc =

![image 13](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile13.png>)

![image 14](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile14.png>)

![image 15](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile15.png>)

σ ∗ σ 2L2(R3) = 4π2

dx |x|2

= 4π24π

![image 16](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile16.png>)

|x| 2

2

dr = 32π3.

0

For a generic data f, we can write the convolution in (2) as

1 .

![image 17](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile17.png>)

![image 18](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile18.png>)

![image 19](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile19.png>)

![image 20](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile20.png>)

fσ ∗ f⋆σ(x) =

![image 21](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile21.png>)

f(ω)f(−ν)δ x − ω − ν dσω dσν.

S2×S2

The L2 norm of the convolution can be written as a quadrilinear integral

fσ ∗ f⋆σ 2L

2(R3) =

![image 22](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile22.png>)

![image 23](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile23.png>)

f(ω1)f(−ν1)f(ω2)f(−ν2)δ ω1 + ν1 − ω2 − ν2 dσω

=

=

dσν

dσω

dσν

2

2

1

1

(S2)4

![image 24](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile24.png>)

![image 25](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile25.png>)

= f(ω1)f(−ω2)f(ω3)f(−ω4) dΣω = Q(f,f⋆,f,f⋆), (3)

where the measure Σ is given by dΣ(ω

1,ω2,ω3,ω4) := δ ω1 + ω2 + ω3 + ω4 dσω

, (4) and Q is the quadrilinear form deﬁned by

dσω

dσω

dσω

4

3

2

1

f1(ω1)f2(ω2)f3(ω3)f4(ω4)dΣω. (5) Observe that Q is fully symmetric in its arguments.

Q(f1,f2,f3,f4) :=

Γ

- Remark 2.3. The positive measure Σ deﬁned in (4) is supported on the (singular) submanifold Γ of (S2)4 of (generic) dimension 5 given by


Γ := (ω1,ω2,ω3,ω4) ∈ (S2)4: ω1 + ω2 + ω3 + ω4 = 0 .

One way to visualize and parametrize Γ is to choose freely the unit vectors ω1 and ω2, then ω3 and ω4 must be two diametrically opposite points on the circle obtained intersecting the unit sphere centered at 0 with the unit sphere centered at −ω1 − ω2 (see Figure 1).

- −ω1

- −ω2


- ω1

- ω2


ω3

−ω1 − ω2 = ω3 + ω4

ω4

Figure 1: Parametrization of the manifold Γ

- 3. Symmetrization


It is evident that Q(f1,f2,f3,f4) Q |f1|,|f2|,|f3|,|f4| , with equality when the functions fk are nonnegative. Hence, we can reduce to consider nonnegative functions only. We may say more.

- Deﬁnition 3.1. Given a complex valued function f deﬁned on S2 we deﬁne its nonnegative antipodally symmetric rearrangement f♯ by


![image 26](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile26.png>)

f♯(ω) := |f(ω)|2 + |f(−ω)|2 2

, ω ∈ S2.

![image 27](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile27.png>)

The function f♯ is also uniquely determined by the conditions f♯(ω) = f♯(−ω) 0, f♯(ω)2 + f♯(−ω)2 = |f(ω)|2 + |f(−ω)|2

Moreover, we have f♯ L2(S2) = f L2(S2). Proposition 3.2. We always have the pointwise estimate

|fσ ∗ f⋆σ(x)| f♯σ ∗ f♯σ(x), ∀x ∈ R3. (6) By (2) and (3) the proposition immediately implies:

Corollary 3.3 ([1]). We always have that

4(R3) f♯σ L

4(R3).

Q(f,f⋆,f,f⋆) Q(f♯,f♯,f♯,f♯) and fσ L

We also have equality when f is a nonnegative constant function, since in that case f = f⋆ = f♯. Corollary 3.3 was proved in [1], our proof here is much shorter and simpler.

Proof of Proposition 3.2. We may assume that f is nonnegative. By the symmetry of the convolution,

2fσ ∗ f⋆σ(x) = fσ ∗ f⋆σ(x) + f⋆σ ∗ fσ(x) =

f(ω)f(−ν) + f(−ω)f(ν) δ x − ω − ν dσω dσν. (7)

=

(S2)2

Now we use Cauchy-Schwarz inequality in its simplest form:

![image 28](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile28.png>)

![image 29](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile29.png>)

AC + BD A2 + B2 C2 + D2, (8) applied with A = f(ω), B = f(−ω), C = f(−ν), D = f(ν). We obtain

f(ω)f(−ν) + f(−ω)f(ν) 2f♯(ω)f♯(ν). We plug this into (7) and obtain (6).

![image 30](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile30.png>)

![image 31](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile31.png>)

![image 32](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile32.png>)

![image 33](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile33.png>)

- Remark 3.4. When A,B,C,D 0, we have equality in (8) if and only if AD = BC.


Suppose now that the equality Q(f,f⋆,f,f⋆) = Q(f♯,f♯,f♯,f♯) holds for some nonnegative function f. It follows from the proof of Proposition 3.2 that

f(ω)f(ν) = f(−ω)f(−ν),

for almost every (ω,ν) ∈ (S2)2. If we integrate this identity with respect to ν, we obtain that f(ω) = f(−ω) for almost every ω ∈ S2, which means that f = f⋆ is antipodally symmetric.

From now on, we may assume that f = f♯ is a nonnegative antipodally symmetric function.

- 4. Reduction to a quadratic form estimate


Our goal now is to bound Q(f,f,f,f) in terms of the L2 norm of f. We may try to use Cauchy-Schwarz inequality with respect to the measure Σ.

- Lemma 4.1. Let B(F,G) be the bilinear form given by

B(F,G) =

Γ

F(ω1,ω2)G(ω3,ω4)dΣω,

for functions F and G deﬁned on S2 × S2. Then B(F,G) 2 B |F|2 ,1 B |G|2 ,1 ,

with equality if and only if there exist two constants λ, µ and a measurable function h(x) deﬁned on |x| 2 such that

F(ω,ν) = λh(ω + ν), G(ω,ν) = µh(−ω − ν), for almost every ω,ν ∈ S2.

Proof. Apply Cauchy-Schwarz inequality to the product of F ⊗ 1 and 1 ⊗ G with respect to the measure Σ. We have equality when F ⊗ 1 and 1 ⊗ G are linearly dependent on the support of Σ. If F and G are not identically zero, that happens when there are non zero constants λ, µ such that

F(ω1,ω2) λ

![image 34](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile34.png>)

=

G(ω3,ω4) µ

![image 35](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile35.png>)

=: h(x),

for almost every ω = (ω1,ω2,ω3,ω4) ∈ Γ, with x = ω1 + ω2 = −ω3 − ω4.

![image 36](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile36.png>)

![image 37](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile37.png>)

![image 38](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile38.png>)

![image 39](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile39.png>)

In our case Q(f,f,g,g) = B(f ⊗f,g ⊗g). Lemma 4.1 and Lemma 2.2 imply that

Q(f,f,f,f) Q f2,f2,1,1 =

=

(S2)2

f(ω1)2f(ω2)2

(S2)2

δ ω1 + ω2 + ω3 + ω4 dσω

3

dσω

4

dσω

1

dσω

2

=

=

(S2)2

f(ω1)2f(ω2)2

2π |ω1 + ω2|

![image 40](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile40.png>)

dσω

1

dσω

2

,

but unfortunately the last integral is too singular for our purposes.

The next lemma contains the geometric information about the symmetries of the support of the measure Σ which allows us to neutralize the singularity of the previous integral.

- Lemma 4.2. Let ω1,ω2,ω3,ω4 ∈ S2 be such that ω1 + ω2 + ω3 + ω4 = 0. Then |ω1 + ω2||ω3 + ω4| + |ω1 + ω3||ω2 + ω4| + |ω1 + ω4||ω2 + ω3| = 4.


Proof. Let X := ω1 · ω2 + ω1 · ω3 + ω2 · ω3. We have ω1 + ω2 + ω3 = −ω4 ∈ S2. This implies that

1 = |ω4|2 = |ω1 + ω2 + ω3|2 = 3 + 2X. Hence X = −1. Then

|ω1 + ω2|2 + |ω1 + ω3|2 + |ω2 + ω3|2 = 6 + 2X = 4.

To conclude the proof it is enough to observe that |ωj + ωk| = |ωm + ωn| whenever (j,k,m,n) is any permutation of (1,2,3,4).

![image 41](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile41.png>)

![image 42](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile42.png>)

![image 43](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile43.png>)

![image 44](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile44.png>)

We combine the result of Lemma 4.2 with the symmetry properties of Q and obtain

- 3

![image 45](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile45.png>)

- 4 Γ


- 3

![image 46](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile46.png>)

- 4


B(F,F),

Q(f,f,f,f) =

f(ω1)f(ω2)|ω1 + ω2|f(ω3)f(ω4)|ω3 + ω4| dΣω =

(9) where F(ω,ν) := f(ω)f(ν)|ω + ν|. We apply the Cauchy-Schwarz inequality of

- Lemma 4.1, use again Lemma 2.2 and obtain


B(F,F) B(F2,1) = 2π

f(ω1)2f(ω2)2 |ω1 + ω2| dσω

1

(S2)2

. (10)

dσω

2

Remark 4.3. We have equality in (10) if and only if f(ω)f(ν) = h(ω + ν) for almost every (ω,ν) ∈ (S2)2 and for some measurable function h(x) deﬁned on |x| 2; this happens for example when f is a constant function.

At this point, since |ω1 + ω2| 2, we can immediately deduce the estimate B(F2,1) 4π f 4L2 , (11)

and hence prove the inequality (1), but the constant is not the optimal one and we will have strict inequality also for f constant.

- 5. Spectral decomposition of the quadratic form We consider now the quadratic functional


H(g) :=

![image 47](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile47.png>)

g(ω)g(ν)|ω − ν| dσω dσν, (12)

(S2)2

which is well deﬁned, real valued and continuous on L1(S2). It is easy to verify that

|H(g1) − H(g2)| 2 g1 L1(S2) + g2 L1(S2) g1 − g2 L1(S2) .

We want to show that the value of H(g) does not decrease when we replace g with a constant function with the same mean value.

Theorem 5.1. Let g ∈ L1(S2). Let µ = 41π S

g(ω)dσω be the mean value of g on the sphere. Then

![image 48](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile48.png>)

2

H(g) H(µ1) = |µ|2 H(1). Moreover, equality holds if and only if g is constant.

By the continuity of H on L1(S2), it is enough to prove the theorem for functions in a dense subset of L1(S2), for example in the Hilbert space L2(S2).

- When g ∈ L2(S2), we consider the decomposition of g as a sum of its spherical harmonics components. A spherical harmonic Yk of degree k is an eigenfunction of ∆S2 corresponding to the eigenvalue −k(k + 1),


∆S2Yk = −k(k + 1)Yk,

where ∆S2 stands for the Lapace-Beltrami operator on the sphere acting on scalar functions. Any function in L2(S2) can be expanded as a sum of orthogonal spherical harmonics (see for example [6, chapter IV]).

Spherical harmonics are related to Legendre polynomials. The latter can be deﬁned in terms of a generating function: when |r| < 1 and |t| 1, if we write the power series expansion

- 1

![image 49](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile49.png>)

- 2


1 − 2rt + r2 −

=

Pk(t)rk, (13)

k 0

then, for any integer k 0, the coeﬃcient Pk(t) is the Legendre polynomial of degree k. These polynomials form a complete orthogonal system in L2([−1,1]) and we have

1

2 2k + 1

Pk(t)2 dt =

.

![image 50](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile50.png>)

−1

We are going to need the following facts about spherical harmonics and Legendre polynomials.

- Lemma 5.2 (Funk-Hecke formula). Let φ be a continuous functions on [−1,1] and Yk be a spherical harmonic of degree k. Then for any ω ∈ L2(S2) we have


φ(ω · ν)Yk(ν)dσν = 2πλkYk(ω), where

S2

1

φ(t)Pk(t)dt, (14) and Pk is the Legendre polynomial of degree k.

λk =

−1

A proof of Lemma 5.2 and its generalization to higher dimensions can be found in [3, p. 247].

- Lemma 5.3. For any integer k 1 we have


d dt

(2k + 1)Pk(t) =

![image 51](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile51.png>)

Pk+1(t) − Pk−1(t) . (15)

Proof. Diﬀerentiate (13) with respect to r,

3 2

(t − r) 1 − 2rt + r2 −

![image 52](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile52.png>)

=

kPk(t)rk−1.

k 0

Multiply on both sides by 1 − 2rt + r2, (t − r)

Pk(t)rk = (1 − 2rt + r2)

k 0

k 0

kPk(t)rk−1.

From this identity, equate the coeﬃcients which multiply the same power rk, for any k 1, and obtain Bonnet’s recursion formula

(2k + 1)tPk(t) = (k + 1)Pk+1(t) + kPk−1(t). Diﬀerentiate with respect to t,

(2k + 1)Pk(t) = (k + 1)Pk′+1(t) − (2k + 1)tPk′(t) + kPk′−1(t). (16) Now, diﬀerentiate (13) with respect to t,

3 2

1 − 2rt − r2 −

![image 53](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile53.png>)

Pk′(t)rk−1.

=

k 1

Again, multiply on both sides by 1 − 2rt + r2, and obtain

Pk(t)rk = (1 − 2rt + r2)

Pk′(t)rk−1.

k 0

k 1

From this identity, equate the coeﬃcients which multiply the same power rk, for any k 1, and obtain another recurrence formula,

Pk(t) = Pk′+1(t) − 2tPk′(t) + Pk′−1(t). (17)

To end the proof, multiply (16) by 2 and subtract (17) multiplied by 2k + 1 to get (15).

![image 54](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile54.png>)

![image 55](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile55.png>)

![image 56](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile56.png>)

![image 57](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile57.png>)

We also need to know the sign of the coeﬃcients (14) when φ(t) = √2 − 2t.

![image 58](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile58.png>)

- Lemma 5.4. The integrals Λk := − 11 √2 − 2tPk(t)dt are negative numbers for all k 1. Proof. Let k 1. We use Lemma 5.3 and integration by parts,


![image 59](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile59.png>)

(2k + 1)ΛK =

where

Ak :=

1

√2 − 2t Pk′+1(t) − Pk′−1(t) dt = Ak+1 − Ak−1, (18)

![image 60](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile60.png>)

−1

1

Pk(t) √2 − 2t

dt = lim

![image 61](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile61.png>)

![image 62](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile62.png>)

r→1

−1

1

Pk(t) √1 − 2rt + r2

dt.

![image 63](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile63.png>)

![image 64](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile64.png>)

−1

The convergence of the limit follows from Lebesgue’s dominated convergence theorem, since we can use the inequality 1 − 2rt + r2 2r(1 − t) to bound the denominator. From the generating function identity (13) and the orthogonality properties of Legendre polynomials we deduce that

rk

Ak = lim r→1

1

2 2k + 1

Pk(t)2 dt =

.

![image 65](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile65.png>)

−1

This shows that the coeﬃcients Ak form a decreasing sequence, and by (18) it follows that Λk is negative for any k 1.

![image 66](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile66.png>)

![image 67](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile67.png>)

![image 68](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile68.png>)

![image 69](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile69.png>)

Proof of Theorem 5.1. When g is a function in L2(S2), we decompose it into the sum

g(ω) =

Yk(ω),

k 0

where Yk is a spherical harmonic of degree k. In particular, the spherical harmonic component of f of degree 0 is given by the constant function µ1, where µ is the mean value of f on S2. We have

![image 70](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile70.png>)

H(g) =

Yj(ω)Yk(ν)|ω − ν| dσν dσω.

j,k 0 (S2)2

By the Funk-Hecke formula of Lemma 5.2 we have that

|ω − ν|Yk(ν)dσν =

S2

S2

![image 71](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile71.png>)

2(1 − ω · ν)Yk(ν)dσν = 2πΛkYk(ω),

where Λk are the coeﬃcients computed in Lemma 5.4. By the orthogonality properties of spherical harmonics we deduce that

H(g) = 2π

Λk Yk 2L2(S2) 2πΛ0 Y0 2L2(S2) = H(µ1),

k 0

since we know by Lemma 5.4 that Λk < 0 when k 1. Here we have equality if and only if Yk ≡ 0 for all k 1, which means that f = Y0 is a constant function.

The case for a generic g ∈ L1(S2) follows by a density argument and by the continuity of H on L1(S2).

![image 72](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile72.png>)

![image 73](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile73.png>)

![image 74](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile74.png>)

![image 75](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile75.png>)

- 6. Constants are (the only real valued) maximizers


We are now ready to put together all the steps we need in order to prove estimate (1) with its best constant. From (2), (3) and Corollary 3.3 we have

fσ 4L

4(R3) = (2π)3 fσ∗fσ 2L

2(R3) = (2π)3Q(f,f⋆,f,f⋆) (2π)3Q(f♯,f♯,f♯,f♯),

where Q was deﬁned in (5). By Remark 3.4, when f is a nonnegative function we have equality here if and only if f = f♯ is antipodally symmetric.

From (9), (10) and the symmetry of f♯, we get

(2π)3Q(f♯,f♯,f♯,f♯)

- 3

![image 76](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile76.png>)

- 4


= 12π4

(2π)4

f♯(ω)2f♯(ν)2 |ω + ν| dσω dσν =

(S2)2

f♯(ω)2f♯(ν)2 |ω − ν| dσω dσν = 12π4H(f♯2),

(S2)2

where H was deﬁned in (12). As observed in Remark 4.3, we have equality here when f is constant.

The mean value of f♯2 on S2 is

1 4π S2

1 4π

f 2L2(S2) By Theorem 5.1 we have that

f♯(ω)2 dσω =

µ :=

![image 77](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile77.png>)

![image 78](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile78.png>)

12π4H(f♯2) 12π4µ2H(1) =

- 3

![image 79](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile79.png>)

- 4


π2H(1) f 4L2(S2) .

Here equality holds if and only if f♯ is constant. The value of H(1) is easily computed:

H(1) =

|ω − ν| dσν dσω =

(S2)2

![image 80](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile80.png>)

2(1 − ω · ν)dσν dσω =

(S2)2

1

√

√1 − tdt =

64 3

π2.

![image 81](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile81.png>)

![image 82](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile82.png>)

2

= 4π · 2π ·

![image 83](<2013-foschi-global-maximizers-sphere-adjoint_images/imageFile83.png>)

−1

The chain of inequalities collected in this section gives us fσ 4L

4(R3) 16π4 f 4L2(S2), with equality if and only if f = f♯ is constant. This proves Theorem 1.1.

Acknowledgments

The author is grateful to Nicola Visciglia for suggesting to look at [1] and work on this problem, and for his helpful comments on the ﬁrst draft, and to Rupert Frank for a remark which allowed to considerably simplify the proof of Theorem 5.1.

References

- [1] Michael Christ and Shuanglin Shao. Existence of extremals for a Fourier restriction inequality. Anal. PDE, 5(2):261–312, 2012.
- [2] Michael Christ and Shuanglin Shao. On the extremizers of an adjoint Fourier restriction inequality. Adv. Math., 230(3):957–977, 2012.


- [3] Arthur Erd´elyi, Wilhelm Magnus, Fritz Oberhettinger, and Francesco G. Tricomi. Higher transcendental functions. Vol. II. Robert E. Krieger Publishing Co. Inc., Melbourne, Fla., 1981. Based on notes left by Harry Bateman, Reprint of the 1953 original.
- [4] Damiano Foschi. Maximizers for the Strichartz inequality. J. Eur. Math. Soc. (JEMS), 9(4):739–774, 2007.
- [5] Elias M. Stein. Harmonic analysis: real-variable methods, orthogonality, and oscillatory integrals, volume 43 of Princeton Mathematical Series. Princeton University Press, Princeton, NJ, 1993. With the assistance of Timothy S. Murphy, Monographs in Harmonic Analysis, III.
- [6] Elias M. Stein and Guido Weiss. Introduction to Fourier analysis on Euclidean spaces. Princeton University Press, Princeton, N.J., 1971. Princeton Mathematical Series, No. 32.


