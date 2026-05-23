arXiv:2002.11627v2[math.NT]22Mar2021

FOURIER INTERPOLATION FROM SPHERES

MARTIN STOLLER

Abstract. In every dimension d ≥ 2, we give an explicit formula that expresses the values of any Schwartz function on Rd only in terms of its restrictions, and the restrictions of its Fourier transform, to all origin-centered spheres whose radius is the square root of an integer. We thus generalize an interpolation theorem by Radchenko and Viazovska [15] to higher dimensions. We develop a general tool to translate Fourier uniqueness- and interpolation results for radial functions in higher dimensions, to corresponding results for non-radial functions in a ﬁxed dimension. In dimensions greater or equal to 5, we solve the radial problem using a construction closely related to classical Poincar´e series. In the remaining small dimensions, we combine this technique with a direct generalization of the Radchenko–Viazovska formula to higher-dimensional radial functions, which we deduce from general results by Bondarenko, Radchenko and Seip [3].

1. Introduction

- 1.1. Main result. The purpose of this paper is to prove the following interpolation formula, which generalizes to higher dimensions the ones obtained by Radchenko and Viazovska [15]. Our main result is easiest to formulate in dimensions at least 5. The theorem covering dimensions 2,3 and 4 will be stated and proved in §4.

Throughout the paper, we write fˆ for the Fourier transform of an integrable function f on Rd (see §1.4.2 for the normalization). We often abbreviate by S = Sd−1 the unit sphere in Rd and always integrate with respect to probability surface measure over it.

Theorem 1. Let d ≥ 5 and let the smooth functions An,A˜n : Rd × Sd−1 → C be deﬁned as in §3. Then, for every Schwartz function f : Rd → C and every point x ∈ Rd, we have

f(x) =

∞

n=1 S

An(x,ζ)f(√nζ)dζ +

![image 1](<2020-stoller-fourier-interpolation-spheres_images/imageFile1.png>)

∞

n=1 S

A˜n(x,ζ)fˆ(√nζ)dζ (1.1)

![image 2](<2020-stoller-fourier-interpolation-spheres_images/imageFile2.png>)

and both series converge absolutely.

Formula (1.1) holds more generally for functions f on Rd, such that f and fˆ decay sufﬁciently fast at inﬁnity, see Corollary 6.1. In §3, we will show that the partial sums on the right hand side of (1.1) converge uniformly, together with all partial derivatives, on compact subsets of Rd \ {0}.

- 1.2. Context. Radchenko and Viazovska [15] constructed a sequence of even Schwartz func-


tions an : R → R such that, for all even Schwartz functions f : R → C and all points x ∈ R, one has

∞

∞

fˆ(√n) an(x), (1.2)

f(√n)an(x) +

![image 3](<2020-stoller-fourier-interpolation-spheres_images/imageFile3.png>)

![image 4](<2020-stoller-fourier-interpolation-spheres_images/imageFile4.png>)

f(x) =

n=0

n=0

1

where both series converge absolutely. They obtained a similar result for odd Schwartz functions, to which we will return shortly. Their result is one out of a growing number of constructive existence theorems in Euclidean harmonic analysis [22, 4, 15, 5, 6], related to sphere packing, energy minimization, sign uncertainty principles and interpolation, in which the constructed object comes from a modular form or some generalization thereof. The employed method often involves a certain integral transform, which has ﬁrst appeaerd in Viazovska’s work on sphere packing [22].

The cited works are primarily concerned with radial Schwartz functions and focus on a particular dimension. The restriction to radial functions is natural given the type of questions that these works adress. In the context of the interpolation theorems [15, 6], one can still ask if the formulas generalize to other dimensions, or to functions that are not necessarily radial. Theorem 1 provides such a generalization.

We remark that, in contrast to the cited works on interpolation, we do not prove a free interpolation theorem in our non-radial setting, so (1.1) is merely a “sampling formula”. More precisely, we do not give suﬃcient conditions for when a pair of sequences of functions on the unit sphere comes from a Schwartz function, by restricting it and its Fourier transform to the spheres √nSd−1. We will provide some necessary conditions in §7, which indicate that the problem is more diﬃcult than in the radial setting.

![image 5](<2020-stoller-fourier-interpolation-spheres_images/imageFile5.png>)

We still have the following immediate corollary of Theorem 1, which may be interesting in its own right. Theorem 3 below gives an analogous corollary for dimensions 2,3,4, taking into account information near the origin.

- Corollary 1.1. For d ≥ 5, the only Schwartz function f on Rd satisfying f(√nS) = fˆ(√nS) = {0} for all n ≥ 1 is f = 0.


![image 6](<2020-stoller-fourier-interpolation-spheres_images/imageFile6.png>)

![image 7](<2020-stoller-fourier-interpolation-spheres_images/imageFile7.png>)

The corollary naturally extends to ellipsoids, by composing f with an invertible linear transformation and correspondingly fˆwith the adjoint of the inverse. One could ask whether a purely analytic proof of Corollary 1.1 can be given, one that does not go through Theorem

- 1 or modular forms. Recently, J. Ramos and M. Sousa obtained Fourier uniqueness results in this direction, namely for radial Schwartz functions and sequences of interpolation nodes that concentrate “more densely near inﬁnity than √n”, see [16, Thm. 1 and §5] for precise statements. Our analysis in §2 shows how one can deduce from such results corresponding uniqueness results for non-radial Schwartz functions, see Corollary 2.2.


![image 8](<2020-stoller-fourier-interpolation-spheres_images/imageFile8.png>)

- 1.3. Ideas. We proceed by further outlining the contents of the paper and sketching some of the main ideas.


- 1.3.1. Relationship to the radial problem. In §2, we show how to deduce a non-radial interpolation formula in dimension d, from radial ones in a sequence of higher dimensions. More speciﬁcally, we deduce such a formula from the existence of radial functions ap,n,a˜p,n on Rp, with p ≡ d (mod 2), having the property that for all f ∈ Srad(Rp) and all x ∈ Rp,


∞

∞

fˆ(√n)˜ap,n(x). (1.3)

f(√n)ap,n(x) +

![image 9](<2020-stoller-fourier-interpolation-spheres_images/imageFile9.png>)

![image 10](<2020-stoller-fourier-interpolation-spheres_images/imageFile10.png>)

f(x) =

n=0

n=0

This step towards Theorem 1 is quite general and actually works for arbitrary sequences of interpolation nodes. It relies only on harmonic analysis on the sphere and Euclidean space with no reference to the particular nodes √n. We state the result as Corollary 2.1, which gives a formula that expresses any value f(x) for f ∈ S(Rd), as a sum of two double series of

![image 11](<2020-stoller-fourier-interpolation-spheres_images/imageFile11.png>)

integrals over the sphere and may be badly behaved from the point of view of convergence. Interchanging sums and integrals formally, we ﬁnd candidates for the kernels An,A˜n in

- Theorem 1. To justify these rearrangments, we need absolute convergence of the double

series and hence some speciﬁc bounds on the functions ap,n(x),a˜p,n(x), that are explicit in all parameters, including the “auxiliary” dimension p. We do not know, whether one can produce radial Schwartz functions obeying suﬃcient bounds, via contour integral methods similar to those in [15, 6]. We circumvent the use of such contour integrals by solving the radial interpolation problem in a diﬀerent way, based on a method which is closely related to the construction of Poincar´e series, described in a bit more detail below in §1.3.2.

A special case of using radial functions in higher dimensions, as mentioned above, is already implicit in Radchenko’s and Viazovska’s work, as we now brieﬂy explain. Besides

- (1.2), valid for even (i.e. radial) Schwartz functions on R, Radchenko and Viazovska also ﬁnd a formula for odd Schwartz functions. Since


S(R) = Seven(R) ⊕ Sodd(R) = Srad(R) ⊕ xSrad(R), (1.4) one can combine the two and write down a formula that reconstructs any f ∈ S(R) from the values f(√n), fˆ(√n), together with the values f′(0), fˆ′(0). The underlying mechanism here is that the topological vector space Sodd(R) is isomorphic to Srad(R3), in a way that is compatible with Fourier transforms. To describe the isomorphism explicitly, let us deﬁne, for any f ∈ S(R), the radial function Lf : R3 → C, by

![image 12](<2020-stoller-fourier-interpolation-spheres_images/imageFile12.png>)

![image 13](<2020-stoller-fourier-interpolation-spheres_images/imageFile13.png>)

Lf(x) =

f(|x|) − f(−|x|) 2|x|

![image 14](<2020-stoller-fourier-interpolation-spheres_images/imageFile14.png>)

for x ∈ R3 \ {0} and Lf(0) = f′(0). (1.5)

Using Taylor’s Theorem one can show that Lf ∈ Srad(R3). In the other direction, we can deﬁne, for each f ∈ Srad(R3), the Schwartz function Rf ∈ Sodd(R) by Rf(t) = tf(t,0,0). The (continuous) linear maps R and L are then mutually inverse and intertwined with the Fourier transforms on R and R3 by Lf = iLfˆ, see [9, §2.1 in ch.4]. Thus, we can use use the map R to “transport” interpolation formulas as in (1.3) from Srad(R3) to Sodd(R).

For dimensions d ≥ 2 we will deﬁne in §2 a generalization of the map L in (1.5), by replacing the ﬁnite average of over the zero-dimensional sphere S0 = {−1,1} by a continuous average over Sd−1, one for each harmonic polynomial. In fact, the deﬁnitions can be written in the same way, by working with the probability measure on S0, assigning mass 1/2 to both of its endpoints. The ﬁnite direct sum (1.4) will be replaced by an inﬁnite direct (topological) sum, described by spaces of harmonic polynomials.

1.3.2. Solving the radial problem by Poincare´-type series. To have a supply of radial functions satisfying (1.3), we will prove in §5 the following Theorem. It pertains to dimensions at least 5. For dimensions 2,3,4, we will need an additional result, that we deduce from more general results by Bondarenko, Radchenko and Seip [3], see §4.

- Theorem 2. Let p ≥ 5. There exist sequences of even entire functions bp,n,˜bp,n : C → C such that, for every f ∈ Srad(Rp) and every x ∈ Rp, we have


∞

∞

fˆ(√n)˜bp,n(|x|) (1.6)

f(√n)bp,n(|x|) +

![image 15](<2020-stoller-fourier-interpolation-spheres_images/imageFile15.png>)

![image 16](<2020-stoller-fourier-interpolation-spheres_images/imageFile16.png>)

f(x) =

n=1

n=1

with absolute convergence. They obey the following bounds.

- (i) There exist two constants C1,C2 > 0, independent of p, such that, for all n ≥ 1, all r ∈ R and all ε ∈ (0,1/8], we have

max (|bp,n(r)|,|˜bp,n(r)|) ≤ C1(47/p)p/4 np/2, (1.7) r = 0 ⇒ max (|bp,n(r)|,|˜bp,n(r)|) ≤ C2ε−2np/4+1+ε|r|−p/2+2(1+ε). (1.8)

- (ii) For every multi-index α ∈ Nd0 and every R > 0, there exist constants C3,C4 > 0, depending on d, α and R, but not on p, such that for all n ≥ 1, all x ∈ Rd, with |x| ≤ R and all ε ∈ (0,1/8], we have


max |∂αbp,n(|x|)|,|∂α˜bp,n(|x|)| ≤ C3(47/p)p/4np/2+|α|, (1.9) x = 0 ⇒ max |∂αbp,n(|x|)|,|∂α˜bp,n(|x|)| ≤ C4ε−2np/4+1+ε+|α||x|−p/2+2(1+ε). (1.10)

Remark. The assertion in part (ii) includes implicitly that for each d ∈ N, the functions x  → bp,n(|x|),˜bp,n(|x|) are smooth on Rd, in particular in a neighborhood of the origin. The number 47 comes from 47 ≥ 2πe2 ≈ 46.4.

We now brieﬂy explain what goes into the proof of Theorem 2. Let H = {τ ∈ C : Im(τ) > 0} denote the upper half plane. The strategy is to ﬁnd the generating functions

∞

∞

˜bp,n(r)eπinτ,

bp,n(r)eπinτ, F˜p(τ,r) =

Fp(τ,r) =

n=1

n=1

knowing only that they need to satisfy a certain functional equation, which comes from applying the desired interpolation formula (1.6) to Gaussians eπiτr

2

. This strategy has already appeared in [15, 6] and we explain the version we need in §5.2. The cited works succeed in ﬁnding the generating functions by integrating a suitable meromorphic and separately modular kernel function on H × H against the Gaussian eπizr

2

over a suitable path. Here we use a diﬀerent method, which is closely related to the construction of Poincar´e series and partly inspired by the works of Knopp on Eichler cohomology [11].

In the context of classical modular forms, a Poincar´e series Pm has an integral parameter m ≥ 1, which indicates that the mth Fourier coeﬃcient of a cusp form is returned when we pair it against Pm with respect to the Petersson inner product. It is constructed by averaging the function eπimτ, with respect to the so-called slash-action, over cosets of the subgroup of translations, of the congruence subgroup involved. In our case, the relevant congruence subgroup is Γ(2). Roughly speaking, we will modify this construction by summing over a speciﬁc subset of Γ(2), which represents the above coset space, up to the identity coset and, instead of averaging the function eπimτ = eπi

√m2τ, we will average the Gaussian eπir

2τ over

![image 17](<2020-stoller-fourier-interpolation-spheres_images/imageFile17.png>)

that subset (for any r ∈ C), so that, when r2 ∈ Z, we almost have Fp(τ,r) = Pr2(τ), up to the constant term in the Fourier expansion and up to constant multiples.

By imitating the classical computation for the Fourier coeﬃcients of Poincar´e series, we can write bp,n(r) as an inﬁnite series involving Bessel functions and ﬁnite exponential sums sums that look very much like classical Kloosterman sums, see (8.5), (8.6). By specializing these formulas to r = √m and even dimensions p ≥ 6, we will see that, if n = m, the value bp,n(√m) equals (up to constant factors) the nth Fourier coeﬃcient of the mth Poincar´eseries in weight p/2 with respect to Γ0(4) (which is conjugate to Γ(2)) and character χk, where χ is the non-trivial Dirichlet character modulo 4. These observations allow us to deduce that, for inﬁnitely many indices n, the function r  → |r|p/2−1+ε|bp,n(r)| is unbounded

![image 18](<2020-stoller-fourier-interpolation-spheres_images/imageFile18.png>)

![image 19](<2020-stoller-fourier-interpolation-spheres_images/imageFile19.png>)

on R, for every ε > 0, see Proposition 8.1. In particular, inﬁnitely of the functions bp,n(r) are not of rapid decay on R.

- 1.4. General notation and a few preliminary facts.


- 1.4.1. Radial functions. A function f on Rd is radial, if f(x) = f(y) for all vectors x,y ∈ Rd with the same Euclidean norm |x| = |y|. If f is radial and r ≥ 0 is a real number, we will sometimes abuse notation and denote also by f(r) the common value of f on the set rSd−1 = {x ∈ Rd : |x| = r}.

We denote by S(Rd) the Schwartz space and by Srad(Rd) the subspace of radial Schwartz functions. We use the standard topology on these spaces. For later reference, we record the following convenient lemma, which follows from Proposition 3.3 in [8].

- Lemma 1.1. For every p ≥ 1, the assignment f  → (x  → f(|x|)) deﬁnes a continuous linear map Srad(R) → Srad(Rp).

The proof of Proposition 3.3 in [8] uses an old result of Hassler Whitney [23], asserting that for every smooth even function φ : R → C there exists a smooth function w : R → C such that φ(r) = w(r2) for all r ∈ R. As a consequence, we see that for every p ≥ 1, the assignment φ  → (x  → φ(|x|)) gives a well-deﬁned linear map Crad∞ (R) → Crad∞ (Rp).

1.4.2. Fourier transforms. Given an integrable function f : Rd → C we denote by F(f) = fˆ its Fourier transform, which we normalize by fˆ(ξ) = R

d

f(x)e−2πix·ξdx, where x · ξ denotes the Euclidean inner product of x,ξ ∈ Rd. We will sometimes compare the Fourier transform of functions on Rd and radial functions on Rd+2m, but context and notation should make it clear in which dimension the Fourier transform is computed.

- 1.4.3. Square roots. We denote by H = {z ∈ C : Im(z) > 0} the complex upper half plane. Given k ∈ C, we deﬁne (−iτ)k = (τ/i)k = exp(k log (τ/i)), where we choose the holomorphic function τ  → log(τ/i) in such a way that it is value at τ = i is 0.
- 1.4.4. Two-periodic holomorphic functions. We denote the open unit disc by D = {w ∈ C : |w| < 1} and by D× = D \ {0} the punctured open unit disc. Given a two-periodic holomorphic function F : H → C, write Fdisc : D× → C for the unique holomorphic function satisfying Fdisc(eπiz) = F(z) for all z ∈ H. Then F admits a Fourier–Laurent expansion F(z) = n∈Z F(n)eπinz with Fourier–Laurent coeﬃcients given by


F(n) =

- 1

![image 20](<2020-stoller-fourier-interpolation-spheres_images/imageFile20.png>)

- 2 iy


0+[−1,1]

F(x + iy0)e−πinxdx =

- 1

![image 21](<2020-stoller-fourier-interpolation-spheres_images/imageFile21.png>)

- 2πi |w|=δ


Fdisc(w)

dw wn+1

![image 22](<2020-stoller-fourier-interpolation-spheres_images/imageFile22.png>)

,

for any y0 > 0 and any δ ∈ (0,1). We say that F is meromorphic (holomorphic, vanishes) at inﬁnity if Fdisc is meromorphic (holomorphic, vanishes) at zero.

1.4.5. Gaussians. For p ≥ 1 and z ∈ H we denote by Gp(z) ∈ Srad(Rp) the function deﬁned by Gp(z)(x) = Gp(z,x) = eπiz|x|

2

for x ∈ Rp and we refer to it as the Gaussian (with parameter z). A proof of the following important Lemma can be found in [6, Lemma 2.2] and will be used in the proof of Proposition 2.1 and in §5.2.

- Lemma 1.2. The set {Gp(z) : z ∈ H} spans a dense subspace of Srad(Rp).




2. Harmonic analysis part

The goal of this section to write down an interpolation formula for Schwartz functions on Rd, assuming that one has interpolation formulas for radial Schwartz functions in every dimension p ∈ {d + 2m : m ∈ N0}.

To ﬁx notation, we ﬁrst recall some basic deﬁnitions and facts about harmonic polynomials and spherical harmonics. All of these facts can be found [21, ch. 3] and [1, ch. 5]. Let d ≥ 2. For each m ∈ N0, let Hm(Rd) denote the space of all complex-valued harmonic polynomial functions on Rd, which are homogeneous of degree m. We call these harmonic polynomials (of degree m) for short. Let Hm(Sd−1) denote the space of all restrictions u|Sd−1 of u ∈ Hm(Rd). It is the space of spherical harmonics of eigenvalue −m(d−2+m) for the spherical Laplacian and carries an L2-inner product structure, coming from the probability surface measure on Sd−1. Via restriction, the spaces Hm(Rd) and Hm(Sd−1) are by deﬁnition isomorphic and we will freely use this isomorphism to give meaning to “orthonormal basis” Bm ⊂ Hm(Rd) or to make sense of values u(x) for x ∈ Rd, even when u was initially declared to belong to Hm(Sd−1). We have

d + m − 1 d − 1 −

d + m − 3 d − 1 ∼

2 (d − 2)!

dimC (Hm(Rd)) =

md−2, (2.1)

![image 23](<2020-stoller-fourier-interpolation-spheres_images/imageFile23.png>)

as m → ∞. For each point ω ∈ Sd−1 and each m ∈ N0, let ζ  → Zmd (ζ,ω) denote the zonal spherical harmonic of degree m with pole ω, characterized by the property

![image 24](<2020-stoller-fourier-interpolation-spheres_images/imageFile24.png>)

u(ζ)Zmd (ζ,ω)dζ = u(ω) for all u ∈ Hm(Sd−1). (2.2) For any orthonormal basis Bm ⊂ Hm(Sd−1), we have

Sd−1

Zmd (ζ,ω) =

![image 25](<2020-stoller-fourier-interpolation-spheres_images/imageFile25.png>)

u(ζ)u(ω) (2.3)

u∈Bm

and for each ω ∈ Sd−1, one has

Zmd (ω,ω) = Zmd (·,ω) 2L2(Sd−1) = dimHm(Rd). (2.4) It follows from (2.2), (2.4) and the Cauchy–Schwarz inequality that

|u(ζ)| ≤ u L2(Sd−1) dimHm(Rd) 1/2 , (2.5)

sup

ζ∈Sd−1

for every u ∈ Hm(Sd−1). We will also use the fact that every homogeneous polynomial P : Rd → C of degree m can be (uniquely) written as

|x|2juj(x), for some uj ∈ Hm−2j(Rd). (2.6)

P(x) =

0≤j≤m/2

The next deﬁnition and proposition will generalize the discussion surrounding (1.5) in the introduction. For any ﬁxed u ∈ Hm(Rd), we give here an explicit inverse of the natural map Srad(Rd+2m) → uSrad(Rd) (up to constant multiples), which intertwines the Weil representations of a two-fold covering group of SL2(R) acting on the respective Schwartz spaces (see [9, Ch. 3]). This is closely related to Bochner’s periodicity relations and the transformation laws for harmonic theta series, see [9, Ch. 3, Ch. 4] and [2]. The result may be known in some equivalent form, but we include our proof to keep the presentation self-contained.

Deﬁnition 2.1. Let d ≥ 2, m ∈ N0 and u ∈ Hm(Rd). For each f ∈ C∞(Rd) and each p ∈ N we deﬁne the radial function Lpuf : Rp → C by

f(|x|ζ)u(ζ/|x|)dζ for x ∈ Rp \ {0},

Lpuf(x) =

![image 26](<2020-stoller-fourier-interpolation-spheres_images/imageFile26.png>)

Sd−1

(∂αf)(0) α! Sd−1

Lpuf(0) =

ζαu(ζ)dζ.

![image 27](<2020-stoller-fourier-interpolation-spheres_images/imageFile27.png>)

![image 28](<2020-stoller-fourier-interpolation-spheres_images/imageFile28.png>)

|α|=m

Proposition 2.1. With notations as in Deﬁnition 2.1, the following holds.

- (i) Each Lpuf is a smooth radial function on Rp.
- (ii) The assignment f  → Lpuf deﬁnes a continuous linear map S(Rd) → Srad(Rp).
- (iii) For all f ∈ S(Rd) we have F(Ldu+2mf) = imLdu+2mF(f).


Proof. Fix d ≥ 2, m ≥ 0, f ∈ C∞(Rd) and u ∈ Hm(Rd). We prove parts (i) and (ii) in the case p = 1, which will imply the general case by the discussion in §1.4.1. We therefore

temporarily write Lf(y) = L1uf(y) for y ∈ R. To start, recall that by Taylor’s theorem we have, for every x ∈ Rd and every K ∈ N0,

K

1

(∂αf)(0) α!

K + 1 α!

xα +

(1 − t)K(∂αf)(tx)dtxα.

f(x) =

![image 29](<2020-stoller-fourier-interpolation-spheres_images/imageFile29.png>)

![image 30](<2020-stoller-fourier-interpolation-spheres_images/imageFile30.png>)

0

k=0 |α|=k

|α|=K+1

We specialize this to x = |y|ζ, where (y,ζ) ∈ R× × S and take K ≥ m + 1. Then we integrate over ζ ∈ S against u(ζ/|y|) and use the decomposition (2.6), applied to monomials P(x) = xα, combined with orthogonality relations for spherical harmonics, to obtain

![image 31](<2020-stoller-fourier-interpolation-spheres_images/imageFile31.png>)

K

Lf(y) =

k=m k≡m(2)

with remainder term

|y|k−m

|α|=k

(∂αf)(0) α! S

ζαu(ζ)dζ + |y|K+1−mRK(y), (2.7)

![image 32](<2020-stoller-fourier-interpolation-spheres_images/imageFile32.png>)

![image 33](<2020-stoller-fourier-interpolation-spheres_images/imageFile33.png>)

K + 1 α! S

RK(y) =

![image 34](<2020-stoller-fourier-interpolation-spheres_images/imageFile34.png>)

|α|=K+1

1

(1 − t)K(∂αf)(|y|ζt)dtu(ζ)ζαdζ.

![image 35](<2020-stoller-fourier-interpolation-spheres_images/imageFile35.png>)

0

The ﬁrst sum in (2.7) is a polynomial in y2, hence in Crad∞ (R). It therefore suﬃces to show that y  → |y|K+1−mRK(y) belongs to Cℓ(K)(R) in such a way that ℓ(K) → ∞ as K → ∞. To that end, we ﬁrst check that on R×, we have

dj dyj |y|c = (y/|y|)j

c!

(c − j)!|y|c−j (0 ≤ j ≤ c), (2.8) dj dyj

![image 36](<2020-stoller-fourier-interpolation-spheres_images/imageFile36.png>)

![image 37](<2020-stoller-fourier-interpolation-spheres_images/imageFile37.png>)

(∂α+βf)(|y|tζ)ζβ. (2.9)

(∂αf)(tζ|y|) = tj(y/|y|)j

![image 38](<2020-stoller-fourier-interpolation-spheres_images/imageFile38.png>)

|β|=j

We now take K of the form K = m + 2N for N ∈ N. Then we deduce from the Leibniz rule and the above formulas (2.8), (2.9) that, for 0 ≤ j ≤ N, the derivative d

j

dyj |y|K−m+1RK(y)

![image 39](<2020-stoller-fourier-interpolation-spheres_images/imageFile39.png>)

(y/|y|)j

is equal to (y/|y|)j = (y/|y|)j

, times

2

1

1

K + 1 α! S

1,j2|y|2N+1−j

(1 − t)K(∂α+βf)(t|y|ζ)dtζα+βu(ζ)dζ,

tj

![image 40](<2020-stoller-fourier-interpolation-spheres_images/imageFile40.png>)

aj

1

2

![image 41](<2020-stoller-fourier-interpolation-spheres_images/imageFile41.png>)

0

j1+j2=j

|α|=K+1 |β|=j2

(2.10) where aj

(2N+1)!

1,j2 = j j!

(2N+1−j1)!. All of these computations hold for y ∈ R×. We deduce that

![image 42](<2020-stoller-fourier-interpolation-spheres_images/imageFile42.png>)

![image 43](<2020-stoller-fourier-interpolation-spheres_images/imageFile43.png>)

1!j2!

dj dyj |y|K−m+1RK(y) → 0, as y → 0 on R× and that the relevant diﬀerence quotients at y = 0 also tend to zero.

![image 44](<2020-stoller-fourier-interpolation-spheres_images/imageFile44.png>)

We now turn to part (ii), so assume that f ∈ S(Rd) and still that p = 1. Fix integers j,n ≥ 0 such that n is even. Deﬁne

|(1 + yn)(Lf)(j)(y)|, B = sup

|(1 + yn)(Lf)(j)(y)|.

A = sup

y∈[0,1]

y∈[1,∞)

It suﬃces to show that A and B can be bounded in terms of ﬁnitely many continuous seminorms of f. Here, we also used that (Lf)(j) is either even or odd, to be able to restrict to non-negative arguments y, for convenience.

- To estimate the term A, we again take K = 2N + m with j ≤ N. We then read oﬀ from

- (2.7) that the jth derivative of the polynomial Lf(y) − |y|2N+1RK(y) has degree at most


- 2N −j, and that its coeﬃcients are multiples of ∂αf(0), with |α| ≤ K, so that the supremum over y ∈ [0,1] of that derivative may be bounded in terms of ﬁnitely many continuous seminorms of f. For the remainder term we note that inside the integrals appearing in (2.10), the vectors t|y|ζ ∈ Rd have Euclidean norm at most 1 for all triples (t,y,ζ) ∈ [0,1]2 × S under consideration, so that we can bound these integrals in terms of suprema of partial derivatives of f, over the closed unit ball in Rd.


- To estimate the term B, we compute directly from the deﬁnition, using the Leibniz rule as well as (2.9) (with α = 0,t = 1), that, for m ≥ 1, y ≥ 1,


(∂βf)(yζ)ζβu(ζ)dζ, (2.11)

1,j2y−m−j

(Lf)(j)(y) =

![image 45](<2020-stoller-fourier-interpolation-spheres_images/imageFile45.png>)

bj,j

1

|β|=j2 S

j1+j2=j

(−1)j1(m+j1−1)!

1,j2 = j j!

(m−1)! . If m = 0, the formula for (Lf)(j) is simpler (namely only the inner sum in (2.11) with j2 replaced by j and u(ζ) replaced by 1). We may now multiply (2.11) with 1 + yn, and use that

where bj,j

![image 46](<2020-stoller-fourier-interpolation-spheres_images/imageFile46.png>)

![image 47](<2020-stoller-fourier-interpolation-spheres_images/imageFile47.png>)

1!j2!

![image 48](<2020-stoller-fourier-interpolation-spheres_images/imageFile48.png>)

|(1 + yn)(∂βf)(yζ)| ≤ sup

(1 + |x|n)|∂βf(x)|,

|x|≥1

using yn = |yζ|n for ζ ∈ S = Sd−1 for the inequality here. Thus, B can be bounded in terms of f as required.

We turn to part (iii) in which we assume that p = d + 2m and that f ∈ S(Rd). By part (ii) and continuity of the Fourier transform, we may assume that f belongs to a (generating set of a) dense subspace of S(Rd). It thus suﬃces to consider Schwartz functions f of the form f(x) = u0(x)eπiz|x|

2

(Rd), m0 ∈ N0 and z ∈ H, because:

, for some u0 ∈ Hm0

- • the linear span of all Schwartz functions of the form x  → P(x)e−π|x|

2

, where P : Rd → C is a polynomial function, is dense in S(Rd), see [9, Ch.3, Ex. 6],

- • by (2.6), every polynomial P on Rd, is a sum of products of a harmonic polynomial with an even power of the Euclidean norm,


2

- • as the parameter z traverses the upper half plane H, the Gaussians eπiz|x|


span a dense subspace of Srad(Rd), see Lemma 1.2.

Under this assumption on f, we have, by deﬁnition, Lud+2mf(y) =

2

2

0−m u0,u L2(S), for all y ∈ Rd+2m \{0}. If m0 = m, then u0,u L2(S) = 0, by orthogonality. If m0 = m, then F(Lud+2mf)(η) = (−iz)−

u0(|y|ζ)u(ζ/|y|)dζ = eπiz|y|

|y|m

eπiz y|ζ|

![image 49](<2020-stoller-fourier-interpolation-spheres_images/imageFile49.png>)

S

d+2m

2

2 eπi(−1/z)|η|

u0,u L2(S), (2.12)

![image 50](<2020-stoller-fourier-interpolation-spheres_images/imageFile50.png>)

for every η ∈ Rd+2m. On the other hand, the Hecke-Funk identity, which follows from [21, Thm 3.4] by homogeneity and analyticity, says that for all ξ ∈ Rd, one has

d+2m0

2

fˆ(ξ) = (−i)m

(−iz)−

2 u0(ξ)eπi(−1/z)|ξ|

. From Deﬁnition 2.1 we see

0

![image 51](<2020-stoller-fourier-interpolation-spheres_images/imageFile51.png>)

d+2m0 2

2

(Lud+2mfˆ)(η) = (−i)m

eπi(−1/z)||η|ζ|

(−iz)−

![image 52](<2020-stoller-fourier-interpolation-spheres_images/imageFile52.png>)

u0(|η|ζ)u(ζ/|η|)dζ

0

![image 53](<2020-stoller-fourier-interpolation-spheres_images/imageFile53.png>)

S

d+2m0

2

(−iz)−

= (−i)m

0−m u0,u L2(S), (2.13) for every η ∈ Rd+2m \ {0}. If m0 = m, then this again is zero. Otherwise, by comparing

2 eπiz|η|

|η|m

0

![image 54](<2020-stoller-fourier-interpolation-spheres_images/imageFile54.png>)

- (2.12) with (2.13) we obtain the formula claimed in (iii).


- Corollary 2.1. Let d ≥ 2. Let (rn)n∈N


be two sequences of non-negative real numbers. Suppose we are given, for each integer p ∈ {d + 2m : m ∈ N0}, each real number r ≥ 0 and each n ∈ N0, two complex numbers cp,n(r),c˜p,n(r) such that: for all g ∈ Srad(Rp) and all y ∈ Rp,

, (ρn)n∈N

0

0

∞

∞

cp,n(|y|)g(rn) +

c˜p,n(|y|)ˆg(ρn),

g(y) =

n=0

n=0

and both of these series converge (not necessarily absolutely). Then, for every x ∈ Rd and every f ∈ S(Rd),

∞

∞

f(rnζ)Zmd (x,ζ/rn)dζ

cd+2m,n(|x|)

f(x) =

S

m=0

n=0

fˆ(ρnζ)Zmd (x,ζ/ρn)dζ , (2.14)

+ imc˜d+2m,n(|x|)

S

where, if ρn = 0 or rn = 0, the integrals are deﬁned through Deﬁnition 2.1. The double series converges in the indicated order of summation and is such that ∞m=0 |(...)| < ∞.

Proof. For every m ≥ 0 we choose an orthonormal basis Bm ⊂ Hm(Sd−1) and we let f ∈ S(Rd). Then for every r ≥ 0, the function ω  → f(rω) is smooth on Sd−1, so that its L2-expansion into spherical harmonics

∞

![image 55](<2020-stoller-fourier-interpolation-spheres_images/imageFile55.png>)

f(rω) =

f(rζ)u(ζ)dζ (2.15)

u(ω)

S

m=0 u∈Bm

converges pointwise absolutely and uniformly with respect to the sup-norm. Now let x ∈ Rd \ {0}. In this proof, we write ιm(x) = (x,0) ∈ Rd+2m for the vector whose ﬁrst d coordinates are given by those of x and whose last 2m coordinates are all zero. Since (2.15)

holds for r = |x| and ω = x/|x| and since each u ∈ Bm is homogeneous of degree m, we obtain

∞

∞

u(x)Ldu+2mf(ιm(x)), (2.16)

![image 56](<2020-stoller-fourier-interpolation-spheres_images/imageFile56.png>)

f(|x|ζ)u(ζ/|x|)dζ =

f(x) =

u(x)

S

m=0 u∈Bm

m=0 u∈Bm

using Deﬁnition 2.1. Here, we could have embedded the vector x also in any other space Rp(m) and (2.16) would be true with Lud+2mf replaced by Lup(m)f. The point is that p(m) = d+2m allows us to use part (iii) of Proposition 2.1 and the assumption, giving

∞

Lud+2mf(ιm(x)) =

n=0

cd+2m,n(|x|)Ldu+2mf(rn) + c˜d+2m,n(|x|)imLdu+2mfˆ(ρn) . (2.17)

Inserting (2.17) back into (2.16) gives (2.14) (by recalling (2.3)). As we assumed that x = 0, we still need to show that

∞

fˆ(ρnζ)dζ

f(rnζ)dζ + c˜d,n(0)

cd,n(0)

f(0) =

S

S

n=0

∞

cd,n(0)Ld1f(rn) + c˜d,n(0)F(Ld1f)(ρn) ,

=

n=0

where 1 stands for the constant polynomial 1. But this identity holds by the assumed radial interpolation formula, applied to Ld1(f) ∈ Srad(Rd) at the point zero.

We record a further corollary of the general expansion in (2.16) and part (iii) of Proposition

- 2.1. It allows one to translate Fourier uniqueness results for radial functions in all dimensions, to corresponding uniqueness results for non-radial functions in a ﬁxed dimension. It may be applicable to the generalization of the uniqueness results by J. Ramos and M. Sousa [16] to radial functions in higher dimensions, as sketched in §5 of their paper. The statement of the corollary itself will not be used elsewhere in the paper, but might be relevant for future work.


Corollary 2.2. Fix a dimension d ≥ 2 and ﬁx two subsets R,Rˆ ⊂ (0,∞). Suppose that for all p ∈ {d + 2m : m ∈ N0} an all f ∈ Srad(Rp), the following implication holds

r∈R rSp−1 = 0 and fˆ|

f|

ρ∈Rˆ ρSp−1 = 0 =⇒ f = 0. (2.18) Then the same implication holds for arbitrary f ∈ S(Rp).

Proof. Suppose that f ∈ S(Rd) vanishes on all spheres rSd−1, r ∈ R and that fˆ vanishes on all spheres ρSd−1, ρ ∈ Rˆ. Fix a nonzero point x ∈ Rd and aim to show that f(x) = 0 (which suﬃces by continuity). By (2.16), it suﬃces to show that for all m ≥ 0 and u ∈ Hm(Rd), the function Lud+2mf ∈ Srad(Rd+2m) and its Fourier transform imLdu+2mfˆ (using part (iii) of Proposition 2.1 here), vanish identically. By the assumption (2.18), this is implied by the vanishing of these radial functions at all radii r ∈ R and ρ ∈ Rˆ respectively. That in turn, follows directly from the deﬁnition of Lpu and our assumption on f.

We conclude section 2 with the following lemma giving bounds for the L2-norm of derivatives of harmonic polynomials. It will be used in in the proof of Lemma 3.1 below.

- Lemma 2.1. Let d ≥ 2, m ≥ 0 and γ ∈ Nd0 and assume (m,γ) = (0,0). Set c = |γ|. Then, for all u ∈ Hm(Rd), we have


√

![image 57](<2020-stoller-fourier-interpolation-spheres_images/imageFile57.png>)

∂γu L2(S) ≤

dc mc u L2(S).

Proof. We may assume that m ≥ 1 and that c ≤ m, as otherwise ∂γu = 0. By [1, Thm 5.14] there exists a constant νd > 0 so that for all u,v ∈ Hm(Rd) of the form u(x) = |α|=m bαxα, v(x) = |α|=m cαxα, we have

m−1

(d + 2i)−1

![image 58](<2020-stoller-fourier-interpolation-spheres_images/imageFile58.png>)

α!bαcα.

u(ζ)v(ζ)dζ = νd

u,v L2(S) =

![image 59](<2020-stoller-fourier-interpolation-spheres_images/imageFile59.png>)

S

i=0

|α|=m

Applying this with u = v and computing ∂γu(x) = |α|=m,α≥γ cα (α−α!γ)!xα−γ, we obtain

![image 60](<2020-stoller-fourier-interpolation-spheres_images/imageFile60.png>)

  max

  u 2L2(S) ≤ (md)cmc u 2L2(S).

m−1

α! (α − γ)!

∂γu 2L2(S) ≤

(d + 2i)

![image 61](<2020-stoller-fourier-interpolation-spheres_images/imageFile61.png>)

|α|=m γ≤α

i=m−c

3. Proof of the main theorem

The aim of this section is to give the proof of Theorem 1 assuming the conclusion of Theorem 2. Throughout §3, we assume that d ≥ 5; the generalization to dimensions d = 2,3,4 will be given in §4 and requires an additional input.

At some points of the proof, it will be convenient to work with an orthonormal basis Bm ⊂ Hm(Rd), so let us choose one such basis for each m ≥ 0. Recall that Zmd (x,y) =

![image 62](<2020-stoller-fourier-interpolation-spheres_images/imageFile62.png>)

u∈Bm u(x)u(y) for all (x,y) ∈ Rd × Rd and all m ∈ N0 and note that Z0d(x,y) = 1.

Let us start by applying Corollary 2.1 with rn = ρn = √n and cp,n(r) = bp,n(r) and c˜p,n(r) = ˜bp,n(r), the numbers provided by Theorem 2. In formula (2.14) we formally interchange the n-sum with the m-sum and then the m-sum with the integral and are thus motivated to deﬁne, for each (x,ζ) ∈ Rd × S and every n ≥ 1, the (formal) series

![image 63](<2020-stoller-fourier-interpolation-spheres_images/imageFile63.png>)

∞

bd+2m,n(|x|)Zmd (x,ζ/√n), (3.1)

![image 64](<2020-stoller-fourier-interpolation-spheres_images/imageFile64.png>)

An(x,ζ) =

m=0

∞

im˜bd+2m,n(|x|)Zmd (x,ζ/√n). (3.2)

A˜n(x,ζ) =

![image 65](<2020-stoller-fourier-interpolation-spheres_images/imageFile65.png>)

m=0

We will address convergence of these series in a moment, but let us observe right away that they trivially converge when x = 0, with values An(0,ζ) = bd,n(0) and A˜n(0,ζ) = ˜bd,n(0). It follows from Corollary 2.1 that the formula (1.1) in Theorem 1 holds at x = 0, because in (2.14), the outer m-sum then reduces to the term with m = 0. The convergence is also absolute in this case, by Theorem 2.

To quantify convergence more generally and more precisely we introduce the following notations. For each tuple of parameters

T = (n,α,β,δ,R,s) ∈ N × Nd0 × Nd0 × [0,∞) × [0,∞) × (0,1], (3.3) satisfying δ ≤ R and for each m ∈ N0, we deﬁne

∂xα∂yβbd+2m,n(|x|)Zmd (x,y)n−m/2

Sm(T) = sup

δ≤|x|≤R s≤|y|≤s−1

and S˜m(T) analogously by replacing bd+2m,n by ˜bd+2m,n. We moreover deﬁne A(T) =

∞

∞

S˜m(T). The main technical estimates we require are contained in the following lemma.

Sm(T), A˜(T) =

m=0

m=0

- Lemma 3.1. Fix multi-indices α,β ∈ Nd0.


- (i) For every s ∈ (0,1], R > 0 and n ∈ N, the tuple T = (n,α,β,0,R,s) satisﬁes A(T) < ∞ and A˜(T) < ∞. Note here that δ = 0.
- (ii) For all 0 < δ < R < ∞, there exists a constant C > 0, depending on δ,α,R and d, such that for every n ∈ N, the tuple T = (n,α,0,δ,R,1) satisﬁes


5d

4 +81+|α|.

max((A(T),A˜(T)) ≤ Cn

![image 66](<2020-stoller-fourier-interpolation-spheres_images/imageFile66.png>)

![image 67](<2020-stoller-fourier-interpolation-spheres_images/imageFile67.png>)

In the arguments below, we will only use Lemma 3.1 in the case α = β = 0. It may be helpful to focus on this special case in a ﬁrst reading, to avoid distracting details that come from partial derivatives. The statements for general α,β imply that the partial sums on the right hand side of formula (1.1) converge uniformly, together with all partial derivatives, on compact subsets of Rd \ {0}.

Proof of Lemma 3.1. To be able to refer to them later, let us ﬁrst record the following computations, which follow directly from the generalized Leibniz rule and the formula (2.3):

α! γ1!γ2!

∂xα∂yβbd+2m,n(|x|)Zmd (x,y) =

x ∂yβZmd (x,y) (3.4)

x bd+2m,n(|x|)∂γ

∂γ

2

1

![image 68](<2020-stoller-fourier-interpolation-spheres_images/imageFile68.png>)

γ1+γ2=α

α! γ1!γ2!

x bd+2m,n(|x|)∂γ

∂γ

∂yβu(y)

![image 69](<2020-stoller-fourier-interpolation-spheres_images/imageFile69.png>)

x u(x). (3.5)

=

2

1

![image 70](<2020-stoller-fourier-interpolation-spheres_images/imageFile70.png>)

γ1+γ2=α

u∈Bm

Whenever an estimate below involves the γ2th or βth derivative of a harmonic polynomial of degree m, we may assume that |γ2| ≤ m or |β| ≤ m, as otherwise the derivative vanishes. Moreover, we focus on the estimates for A(T), which will equally hold for A˜(T), because

- Theorem 2 gives the same upper bounds for bp,n and ˜bp,n. Part (i) follows basically from the presence of the term (47/p)p/4 in the bounds of Theorem


2 and from Lemma 2.1. Turning to details, let s ∈ (0,1], R > 0 and n ∈ N be given. We bound the absolute value of the sum (3.5), for |x| ≤ R and s ≤ |y| ≤ s−1, by combining the following estimates:

- • From (2.5), u L2(S) = 1 and Lemma 2.1 we obtain |∂βu(y)| ≤ |y|m−|β| sup

![image 71](<2020-stoller-fourier-interpolation-spheres_images/imageFile71.png>)

Sd−1

|∂βu| ≤ |y|m−|β|(dimHm−|β|(Rd))1/2 ∂βu L2(S)

≪d,|β| s|β|−m(m − |β|)

d−2

![image 72](<2020-stoller-fourier-interpolation-spheres_images/imageFile72.png>)

2 m|β|.

- • Similarly, we ﬁnd sup|x|≤R |∂γ

x2u(x)| ≪d,γ2

Rm(m − |γ2|)

d−2

![image 73](<2020-stoller-fourier-interpolation-spheres_images/imageFile73.png>)

2 m|γ

2|, for each γ2 ≤ α.

- • The bound (1.9) in Theorem 2 implies

sup

|x|≤R

|∂γ

1

x bd+2m,n(|x|)| ≪d,γ1,R n

d+2m

![image 74](<2020-stoller-fourier-interpolation-spheres_images/imageFile74.png>)

2 +|γ1| 47 d + 2m

![image 75](<2020-stoller-fourier-interpolation-spheres_images/imageFile75.png>)

d/4+m/2

. (3.6)

- • The number of terms is |Bm| = dim Hm(Rd) ≪d md−2, which follows from (2.1).


We deduce that there are U,X,Y > 0, all depending at most on d,α,β,R,s and n, so that Sm(T) ≤ UmXY m(2m+d)−m/2 for all m ∈ N0. By the root-test or the ratio-test, the series in part (i) therefore converge, as claimed.

In the remaining part (ii), we will track the dependence on n more precisely. Let 0 < δ < R < ∞ and set T = (n,α,0,δ,R,1). We may and will assume that δ < 1 ≤ R. Let M ≥ 1 be an integral parameter, to be chosen later. We deﬁne start and tail sums

Astart(T) =

M

∞

Sm(T), Atail(T) =

Sm(T).

m=0

m=M+1

We start with the analysis of the tail, which is similar to part (i) and we will not yet use that |x| ≥ δ. As in the proof of part (i), we use Lemma 2.1 to bound the derivatives with respect to x of Zmd (x,y) appearing in (3.4) by

d−2

2| Zmd (·,ζ) L2(S) ≪d,|γ2| |x|m−|γ

2 m|γ

x Zmd (x,ζ)| ≪d,|γ2| |x|m−|γ

2|(m − |γ2|)

|∂γ

2

![image 76](<2020-stoller-fourier-interpolation-spheres_images/imageFile76.png>)

2|md−2+|γ

2|, (3.7)

where we used that Zmd (·,ζ) 2L2(S) = dimHm(Rd) and where the implied constants depend neither on x, nor on ζ. We have |x|m−|γ

2| ≤ Rm in (3.7) and combined with (3.6) we see that

∞

d/4+m/2

α! γ1!γ2!

47 d + 2m

d+2m

2 Rmmd−2

n|γ

1|m|γ

2|

n−m/2

Atail(T) ≪d,R,α

n

![image 77](<2020-stoller-fourier-interpolation-spheres_images/imageFile77.png>)

![image 78](<2020-stoller-fourier-interpolation-spheres_images/imageFile78.png>)

![image 79](<2020-stoller-fourier-interpolation-spheres_images/imageFile79.png>)

γ1+γ2=α

m=M+1

m/2

∞

47R2n d + 2m

≪d,R,α nd/2+|α|

md−2(1 + m)|α|,

![image 80](<2020-stoller-fourier-interpolation-spheres_images/imageFile80.png>)

m=M+1

where we absorbed the term (47/(d + 2m))d/4 ≪ 1 into the implied constant and used that the inner sum over γ1,γ2 is equal to

(n + m)|α| = (n(1 + m/n))|α| ≤ n|α|(1 + m)|α|. We now take M = ⌊47R2n⌋ + 2. Then 47R

2n

d+2m ≤ 21 for all m ≥ M + 1 and hence Atail(T) ≪d,R,α nd/2+|α|

![image 81](<2020-stoller-fourier-interpolation-spheres_images/imageFile81.png>)

![image 82](<2020-stoller-fourier-interpolation-spheres_images/imageFile82.png>)

∞

2−m/2md−2(1 + m)|α| ≪d,α,R nd/2+|α|.

m=1

It remains to bound the ﬁnite sum Astart(T). At this point, the restriction |x| ≥ δ > 0 becomes important. By (1.10) in Theorem 2 (applied by setting ε = 1/8 in its statement) we have, for δ ≤ |x| ≤ R,

bd+2m,n(|x|)| ≪γ1,R n9/8+d/4+m/2+|γ

1||x|−d/2−m+9/4. (3.8)

|∂γ

1

Crucially, the term nm/2 in (3.8) cancels with the term n−m/2 in the deﬁnition of Sm(T) and the term |x|−m in (3.8) cancels with |x|m in (3.7). This implies

M

α! γ1!γ2!

n9/8+d/4+|γ

1||x|−d/2+9/4|x|−|γ

2|md−2+|γ

2|

Astart(T) ≪d,R,α

sup

![image 83](<2020-stoller-fourier-interpolation-spheres_images/imageFile83.png>)

δ≤|x|≤R γ1+γ2=α

m=0

M

|x|−d/2+9/4 nd/4+9/8

(n + m/δ)|α|md−2. (3.9)

≤ sup

δ≤|x|≤R

m=0

For m ≤ M we can bound (n + m/δ)|α| = n|α|δ−|α|(δ + mn )|α| ≤ n|α|δ−|α|(1 + 47R

2n+2 n )|α| ≪R,α n|α|.

![image 84](<2020-stoller-fourier-interpolation-spheres_images/imageFile84.png>)

![image 85](<2020-stoller-fourier-interpolation-spheres_images/imageFile85.png>)

Inserting this into (3.9), we get

Astart(T) ≪d,R,δ,α nd/4+9/8+|α|(M + 1)Md−2 ≪R,d nd/4+9/8+|α|+(d−1) = n5d/4+1/8+|α|. Thus Astart(T) dominates Atail(T) and this proves part (ii).

As already mentioned, part (i) of Lemma 3.1 implies that for every n ∈ N, the series

An(x,ζ) and A˜n(x,ζ) deﬁne smooth functions of (x,ζ) ∈ Rd ×(Rd \{0}), so they are smooth on Rd × Sd−1. Moreover, it shows that for every continuous function g : Rd → C, the

integral S An(x,ζ)g(√nζ)dζ deﬁnes a smooth function of x ∈ Rd such that, for all α ∈ Nd0 and 0 < δ ≤ 1 ≤ R,

![image 86](<2020-stoller-fourier-interpolation-spheres_images/imageFile86.png>)

An(x,ζ)g(√nζ)dζ ≪d,δ,R,α n

|g(√nζ)| (3.10) and such that

5d

4 +81+|α| sup ζ∈S

∂xα

![image 87](<2020-stoller-fourier-interpolation-spheres_images/imageFile87.png>)

![image 88](<2020-stoller-fourier-interpolation-spheres_images/imageFile88.png>)

sup

![image 89](<2020-stoller-fourier-interpolation-spheres_images/imageFile89.png>)

![image 90](<2020-stoller-fourier-interpolation-spheres_images/imageFile90.png>)

δ≤|x|≤R

S

∞

bd+2m,n(|x|)Zmd (x,ζ/√n)g(√nζ)dζ. (3.11)

An(x,ζ)g(√nζ)dζ =

![image 91](<2020-stoller-fourier-interpolation-spheres_images/imageFile91.png>)

![image 92](<2020-stoller-fourier-interpolation-spheres_images/imageFile92.png>)

![image 93](<2020-stoller-fourier-interpolation-spheres_images/imageFile93.png>)

m=0 S

S

The upper bound (3.10) and the identity (3.11) also hold for An replaced by A˜n and bd+2m,n replaced by im˜bd+2m,n.

With these preliminaries in place, we are now ready to prove Theorem 1. Consider any Schwartz function f : Rd → C and ﬁx a point x ∈ Rd \{0}. The sequences of the suprema of f and fˆ over the spheres of radius √n then decay rapidly. Together with part (ii) of Lemma

![image 94](<2020-stoller-fourier-interpolation-spheres_images/imageFile94.png>)

- 3.1, applied with T = (n,0,0,|x|,|x|,1), it follows that the double series ∞


∞

∞

An(x,ζ)f(√nζ)dζ =

Zmd (x,ζ/√n)f(√nζ)dζ, (3.12)

![image 95](<2020-stoller-fourier-interpolation-spheres_images/imageFile95.png>)

![image 96](<2020-stoller-fourier-interpolation-spheres_images/imageFile96.png>)

![image 97](<2020-stoller-fourier-interpolation-spheres_images/imageFile97.png>)

bd+2m,n(|x|)

n=1 S

S

n=1

m=0

converges absolutely, as does the one involving fˆ, A˜n and ˜bd+2m,n. By Fubini–Tonelli on N × N0, we can therefore interchange the sum over n with that over m. Then, combining

- (3.12) with (3.11) and Corollary 2.1, we deduce that the left hand side of (3.12), plus the


corresponding series involving A˜n and fˆ, equals f(x). This proves our interpolation formula (1.1) in Theorem 1 for the point x = 0. Finally, recall that we already proved it for x = 0,

right after the deﬁnition of An(x,ζ), A˜n(x,ζ). This completes the proof of Theorem 1, up to the proof of Theorem 2, which will be given in §5.

- 3.1. Remarks on (uniform) convergence. If we keep track of the implied constants in the proof of part (ii) in Lemma 3.1 in the case |α| = |β| = 0, we obtain the following explicit


bound. For any 0 < δ ≤ 1 ≤ R and every n ∈ N, the supremum supδ≤|x|≤R,|ζ|=1 |An(x,ζ)| is less than or equal to

∞

C2Hd(1/δ)d/2−9/4nd/4+9/8(47nR2 + 3)d−1 + C1Hd(47/d)d/4

2−m/2md−2, (3.13)

m=1

dim Hm(Rd) md−2

where Hd = (d−22)! supm∈N

, compare with (2.1) and where C1,C2 > 0 are constants as in part (i) of Theorem 2. We deduce that the interpolation formula (1.1) converges

![image 98](<2020-stoller-fourier-interpolation-spheres_images/imageFile98.png>)

![image 99](<2020-stoller-fourier-interpolation-spheres_images/imageFile99.png>)

0

uniformly and rapidly on every d-dimensional annulus, equivalently on any compact subset avoiding the origin. Note moreover that, if 2 ≤ d ≤ 4, then (1/δ)d/2−9/4 ≤ 1 and the proof shows that we have uniform convergence on any compact subset of Rd.

- 3.2. Reformulation of the proof. We can formulate the above proof of Theorem 1 in a way that is more reminiscent of [15] (or [6]). Namely, we can ﬁx a vector x ∈ Rd and interpret the


right hand side of the interpolation formula (1.1) as a linear functional ℓx : S(Rd) → C. Note that it is indeed deﬁned on all of S(Rd) by Lemma 3.1 and moreover continuous. It therefore suﬃces to show that ℓx(f) = f(x), for f in a generating set of a dense subspace of S(Rd). Arguing as in the proof of Proposition 2.1, we can therefore reduce to f(x) = u0(x)eπiz

0|x|2, where u0 ∈ Bm0

and z0 ∈ H are ﬁxed. In this case, the desired identity ℓ(x) = f(x) reduces to the formula (1.6) in Theorem 2, in dimension p = d + 2m0, applied to the Gaussian.

4. Dimensions 2, 3 and 4

To extend Theorem 1 to dimensions 2,3 and 4, we need the following input. Proposition 4.1. For every p ∈ {2,3,4}, there exist sequences (ap,n)n∈N

of radial Schwartz functions on Rp such that, for every f ∈ S(Rp) and every x ∈ Rp,

, (˜ap,n)n∈N

0

0

∞

∞

ap,n(x)f(√n) +

a˜p,n(x)fˆ(√n), (4.1)

![image 100](<2020-stoller-fourier-interpolation-spheres_images/imageFile100.png>)

![image 101](<2020-stoller-fourier-interpolation-spheres_images/imageFile101.png>)

f(x) =

n=0

n=0

where the series converge absolutely and such that, for every continuous semi-norm · on S(Rp), the sequences ( ap,n )n∈N

are of polynomial growth.

, ( a ˜p,n )n∈N

0

0

Proof. This follows from more general results by Bondarenko, Radchenko and Seip [3]. In the notation of their paper, we specialize the discussions in section 3 of [3] to the function ϕ(z) = eπizr

2

, where r = |x| ∈ R≥0 and to the parameter k = p/2 (their results would in fact

cover all real k ≥ 0). The Fourier coeﬃcients of the series denoted Fk±(τ,ϕ) give the Fouriereven and -odd parts of the radial functions ap,n and a˜p,n is the Fourier transform of ap,n on Rp. The interpolation formula (4.1) follows from the density of complex Gaussians (Lemma

1.2) together with the functional equations satisﬁed by the generating series Fk±(τ,ϕ), as in [15] (see also §5.2 for a related discussion). The same technique as in [15] can be used to

prove that the functions ap,n,a˜p,n belong to the Schwartz space and that all their Schwartz semi-norms grow polynomially with n (see also Proposition 6.1 in [3]).

- Theorem 3. Let d ∈ {2,3,4}. For every n ≥ 1, there are two smooth functions An,A˜n : Rd × Sd−1 → C and for every multi-index α ∈ Nd0 of size |α| ≤ 1, two Schwartz functions hα,h˜α ∈ S(Rd) such that, deﬁning


h˜α(x)(∂αg)(0),

hα(x)(∂αf)(0), T˜x(g) =

Tx(f) =

|α|≤1

|α|≤1

for f,g ∈ S(Rd) and x ∈ Rd, the following holds. For all f ∈ S(Rd) and all x ∈ Rd,

∞

∞

An(x,ζ)f(√nζ)dζ + T˜x(fˆ) +

A˜n(x,ζ)fˆ(√nζ)dζ (4.2)

![image 102](<2020-stoller-fourier-interpolation-spheres_images/imageFile102.png>)

![image 103](<2020-stoller-fourier-interpolation-spheres_images/imageFile103.png>)

f(x) = Tx(f) +

n=1 S

n=1 S

and both series converge absolutely.

Proof. We modify the arguments in §3 as follows. First, we deﬁne the integers M2 = 2, M3 = 1, M4 = 1. We start with Corollary 2.1 and apply it with inputs rn = ρn = √n and cp,n(r) and c˜p,n(r) taken as follows, depending on the dimension d of interest:

![image 104](<2020-stoller-fourier-interpolation-spheres_images/imageFile104.png>)

(cd+2m,n(r),c˜d+2m,n(r)) = (ad+2m,n(r),a˜d+2m,n(r)) if m < Md, (cd+2m,n(r),c˜d+2m,n(r)) = (bd+2m,n(r),˜bd+2m,n(r)) if m ≥ Md, where bd+2m,n and ˜bd+2m,n are as in Theorem 2 and ad+2m,n,a˜d+2m,n are as in Proposition

- 4.1 (and we abuse notation as in §1.4.1). We then redeﬁne the series An in (3.1) to

An(x,ζ) =

∞

m=0

cd+2m,n(|x|)Zmd (x,ζ/√n)

![image 105](<2020-stoller-fourier-interpolation-spheres_images/imageFile105.png>)

and redeﬁne A˜n in (3.2) in the same way, replacing ˜bd+2m by c˜d+2m. Again, these series trivially converge at x = 0 and the formula (4.2) holds in this case by Corollary 2.1. Notice

that they diﬀer by at most two terms from the ones that involved only bd+2m,n, ˜bd+2m,n. By the assumption on the semi-norms of ap,n,a˜p,n, we can control the “exceptional” terms by

|ad+2m,n(|x|)Zmd (x,ζ)| ≪d sup ξ∈Rd

ad+2m,n(|ξ|)|ξ|m md−2 ≪ nBmd−2,

where B > 0 depends only on d (because at most two values of m need to be considered here). It follows that the new functions An, A˜n obey bounds similar to those stated in Lemma 3.1. The functions hα, h˜α arise from Corollary 2.1 as follows. In the double sum (2.14), we split the inner n-sum into the sub-sums over n ∈ {0} and n ∈ N and then interchange (as we may) the outer sum with these inner sums individually. Doing so, we see that

hα(x) =

1 α! S

![image 106](<2020-stoller-fourier-interpolation-spheres_images/imageFile106.png>)

ζαZmd (x,ζ)dζ ad+2m,0(|x|) =

1 α! u∈B

![image 107](<2020-stoller-fourier-interpolation-spheres_images/imageFile107.png>)

m S

ζαu(ζ)dζ ad+2m,0(|x|)u(x),

![image 108](<2020-stoller-fourier-interpolation-spheres_images/imageFile108.png>)

where S = Sd−1 and Bm ⊂ Hm(Rd) is an orthonormal basis. In this way we can prove (4.2), with point-wise absolute convergence (but recall also the remarks regarding uniform convergence made at the end of §3.1).

5. Poincar´e series-type construction

The goal of §5 is to prove Theorem 2. Basic preliminaries on modular forms follow in §5.1 and the general proof strategy via generating series and functional equations, following [15, 6], is explained in §5.2. After some group theoretic preliminaries in §5.3, the deﬁnition of the solutions to the above mentioned functional equations, as well as the deﬁnition of the functions bp,n,˜bp,n in Theorem 2, is given in §5.4. The required growth estimates are then proved in §5.5.

5.1. Modular preliminaries. We assemble some basic facts related to modular forms that are relevant for our purposes. As general references, we mention [10, 20, 14, 19].

- 5.1.1. Fractional linear transformations. We let SL2(R) and its subgroups act on the upper


half plane H by fractional linear transformations. For M = ac db ∈ SL2(R) and τ ∈ H we deﬁne j(M,τ) = cτ +d and we recall that Im(Mτ) = Im(τ)|j(M,τ)|−2. For M ∈ SL2(R) we use [M] to denote its image in PSL2(R) and similarly for elements of subgroups Γ ≤ SL2(R) containing −I. We write Γ for the image of such a subgroup in PSL2(R).

![image 109](<2020-stoller-fourier-interpolation-spheres_images/imageFile109.png>)

- 5.1.2. Congruence subgroups of level 2. We use S = 1 0 −01 and T = (10 11) ∈ SL2(Z), which together generate the group SL2(Z). Let pr2 : SL2(Z) → SL2(Z/2Z) denote the natural morphism. The principal congruence subgroup of level 2 is the normal subgroup Γ(2) = ker(pr2) ⊳ SL2(Z). It is generated by −I,T2,ST2S. The group Γ(2) is freely generated by

![image 110](<2020-stoller-fourier-interpolation-spheres_images/imageFile110.png>)

[T2] and [ST2S]. The theta subgroup is Γθ = pr−2 1({1,pr2(S)}) and equal to Γ(2) ⊔ SΓ(2) and moreover generated by S and T2.

- 5.1.3. Jacobi’s theta function. For (z,τ) ∈ C × H, let ϑ(z,τ) = n∈Z eπin

2τ+2πinz denote Jacobi’s theta function and let Θ3(τ) = θ00(τ) = ϑ(0,τ) denote one of its Nullwerte, following historical notations. This series converges normally on H and it is well-known that Θ3 never vanishes on H, by Jacobi’s celebrated triple product formula (for example). We may therefore deﬁne, for all (M,τ) ∈ PSL2(R) × H, the number jΘ(M,τ) = Θ3(Mτ)/Θ3(τ) ∈ C×. The Poisson summation formula for even Schwartz functions on R is equivalent to jΘ(S,τ) = (−iτ)1/2 (Lemma 1.2 and §1.4.3) and the identity jΘ(T2,τ) = 1 is trivial. Since Γθ is generated by S and T2, it follows that Θ83 transforms like a modular form of weight 4 on Γθ and that

|j(M,τ)| = |jΘ(M,τ)|2 for all (M,τ) ∈ Γθ × H. (5.1) We give more information on the transformation laws of Θ3 in §8 and introduce its accompanying theta constants Θ2,Θ4 in §7, but these things will not be needed in the remainder of §5.

![image 111](<2020-stoller-fourier-interpolation-spheres_images/imageFile111.png>)

- 5.1.4. Slash action. For any half-integer k ∈ 12Z and any complex vector space S (e.g. S = Srad(Rp) or C), we deﬁne the slash-action in weight k on the space of all functions f : H → S, by (f|kM)(z) = jΘ(M,z)−2kf(Mz). We extend it linearly to the group ring C[PSL2(R)].


![image 112](<2020-stoller-fourier-interpolation-spheres_images/imageFile112.png>)

- 5.2. Generating series and functional equations. As part of the proof Theorem 2, we explain here the general strategy to prove an interpolation formula for radial Schwartz functions on Rd, by rephrasing the problem in terms of certain holomorphic functions on the complex upper half plane. This strategy is very similar to the one used in [15] and also similar to the more complicated one used in [6]. We shall implement it in §5.4 and §5.5.


Suppose we want to ﬁnd radial functions an,a˜n on Rp such that for all f ∈ Srad(Rp) and all x ∈ Rp,

∞

∞

fˆ(√n)˜an(x) (5.2)

f(√n)an(x) +

![image 113](<2020-stoller-fourier-interpolation-spheres_images/imageFile113.png>)

![image 114](<2020-stoller-fourier-interpolation-spheres_images/imageFile114.png>)

f(x) =

n=0

n=0

with absolute convergence. Fixing a point x ∈ Rp we may think of (5.2) as an identity of linear functionals on Srad(Rp). From this point of view, it is reasonable to search among sequences (an(x))n∈N

that grow at most polynomially in n, because in this case, the right hand side of (5.2) also deﬁnes a continuous linear functional and the validity of (5.2) becomes equivalent to the validity of the same equation for f belonging to a (generating set of a) dense subspace of Srad(Rp). Such a set is given by {Gp(τ) : τ ∈ H}, by Lemma 1.2. Requiring polynomial growth on the coeﬃcients also implies that the generating series

, (˜an(x))n∈N

0

0

∞

∞

an(x)eπinτ, F˜(τ,x) =

a˜n(x)eπinτ

F(τ,x) =

n=0

n=0

converge absolutely for all τ ∈ H and x ∈ Rp. If (5.2) holds for all f, then in particular for f = Gp(τ), and hence the following set of functional equations must be satisﬁed by F,

F˜. We write these without the variables x,τ and we use the slash action of C[PSL2(Z)] in weight k = p/2, as deﬁned in §5.1.4.

- (i) F + F˜|kS = Gp.
- (ii) F|k(T2 − 1) = 0.
- (iii) F˜|k(T2 − 1) = 0.
- (iv) F|k(ST2S − 1) = Gp|k(ST2S − 1). Here, equation (iv) is implied by all the others and equation (iii) is implied by all the others. The formal veriﬁcation is left to the reader. Conversely, if we can ﬁnd, in the ﬁrst place, two functions F,F˜ : H × Rp → C that are holomorphic and 2-periodic in the ﬁrst variable, radial in the second and moreover related by (i), then we can deﬁne an(x) as the nth Fourier coeﬃcient of τ  → F(τ,x) and a˜n as the nth Fourier coeﬃcient of τ  → F˜(τ,x). To prove


- (5.2), it then only remains to be shown that an = 0 = a˜n for n < 0 and that the polynomial growth requirement holds.


- 5.3. A particular set of words. We continue with our preparations for the proof of Theorem 2, outlined at the beginning of §5, by introducing and studying a certain subset of Γ(2), that will enter the deﬁnition of the generating series in the next subsection.


![image 115](<2020-stoller-fourier-interpolation-spheres_images/imageFile115.png>)

As for notation, for an element M ∈ SL2(Z), we denote by [M] its class modulo {±I}, but we also use S¯ = [S] in this section. Note that S¯2 = 1 ∈ PSL2(Z). If M = ac db , then we will often write a = aM, b = bM, c = cM and d = dM. When it is unambiguous, we use the same notation for M ∈ PSL2(Z), for example, writing |cM| ≥ 1 or a ratio of matrix entries. We recall that the group Γ(2) is freely generated by the elements A = [T2] and B = [ST2S]. We also use the representatives A0 = T2, B0 = ST2S−1 in this section.

![image 116](<2020-stoller-fourier-interpolation-spheres_images/imageFile116.png>)

![image 117](<2020-stoller-fourier-interpolation-spheres_images/imageFile117.png>)

Deﬁnition 5.1. The subset B ⊂ Γ(2) is deﬁned as the set of all nonempty ﬁnite reduced words in A and B that start with a nonzero power of B. More formally, an element M ∈ Γ(2) belongs to B, if and only if there are integers m ≥ 1 and e1,...,em,f1,...,fm, all nonzero, except possibly em, such that M = Bf

![image 118](<2020-stoller-fourier-interpolation-spheres_images/imageFile118.png>)

. We deﬁne the set B˜ = BS ⊔ {S} = {MS : M ∈ B} ⊔ {S} ⊂ Γθ.

Ae

···Bf

Ae

![image 119](<2020-stoller-fourier-interpolation-spheres_images/imageFile119.png>)

![image 120](<2020-stoller-fourier-interpolation-spheres_images/imageFile120.png>)

m

m

1

1

![image 121](<2020-stoller-fourier-interpolation-spheres_images/imageFile121.png>)

![image 122](<2020-stoller-fourier-interpolation-spheres_images/imageFile122.png>)

![image 123](<2020-stoller-fourier-interpolation-spheres_images/imageFile123.png>)

We shall prove that the elements B and those of B˜ are uniquely determined by their

bottom rows (up to sign). To formulate this precisely, we deﬁne P = {(c,d) ∈ Z2 : gcd(c,d) = 1, c ≡ 0,d ≡ 1 (mod 2), c = 0}, P˜ = {(c,d) ∈ Z2 : gcd(c,d) = 1, c ≡ 1,d ≡ 0 (mod 2)}.

The unit group Z× = {−1,1} acts on these sets in the obvious way, via ε · (c,d) = (εc,εd), for ε ∈ Z×. We further equip them with an action of Z, deﬁned as (c,d)|ℓ = (c,d + 2ℓc). These actions commute, so that Z acts on the quotients P/Z×, P˜/Z×. We write the class of (c,d) in these quotients as [(c,d)] = {(c,d),(−c,−d)}.

- Lemma 5.1. With notations as above, the following holds.


- (i) For each M ∈ B, M˜ ∈ B˜ and each ℓ ∈ Z one has MAℓ ∈ B and MA˜ ℓ ∈ B˜. In other words, the group Z ∼= A acts on either set B, B˜ by right multiplication.
- (ii) The assignment a b c d  → [(c,d)] (5.3)


deﬁnes Z-equivariant bijections B ∼= P/Z×, B˜ ∼= P˜/Z×.

Proof. We prove part (i). Let M ∈ B, M˜ ∈ B˜, ℓ ∈ Z. It follows directly from the deﬁnition that MAℓ ∈ B. As for M˜ , write M˜ = HS¯ for some H ∈ B ⊔ {1}. Then

MA˜ ℓ = HSA¯ ℓ = HSA¯ ℓS¯S¯ = HBℓS.¯ and we deduce MA˜ ℓ ∈ B˜ in all cases; it equals S¯ if H = B−ℓ and HBℓ belongs to B otherwise.

We prove part (ii). In general, the assignment (5.3) deﬁnes a mapping PSL2(Z) → Z2prim/Z×, where Z2prim denotes the set of all primitive row vectors in Z2 (nonzero vectors with coprime entries). Also in general, two elements X1,X2 ∈ Γθ have the same image under

![image 124](<2020-stoller-fourier-interpolation-spheres_images/imageFile124.png>)

- (5.3), if and only if there is ℓ ∈ Z so that X2 = AℓX1, as a short calculation shows. We now prove the assertion about B, proving that the map is well-deﬁned, injective and


surjective one after the other.

First, it maps indeed to P, because no element of B can have lower left entry zero. Indeed, elements of Γ(2) have lower left-entry equal to zero, if and only if they belong to A and

![image 125](<2020-stoller-fourier-interpolation-spheres_images/imageFile125.png>)

A ∩ B = ∅ holds by deﬁnition.

Let M1,M2 ∈ B and suppose they have the same image under (5.3). This implies that M2 = AℓM1 for some ℓ ∈ Z. By deﬁnition of B and and the fact that A and B freely generate Γ(2), this implies that ℓ = 0, so our map is injective.

![image 126](<2020-stoller-fourier-interpolation-spheres_images/imageFile126.png>)

It remains to establish surjectivity. Let (c0,d0) ∈ P such that c0 > 0. Recall that c0 is even and d0 is odd by deﬁnition. Since gcd(2c0,d0) = 1 we may choose a0,b0 ∈ Z such that M0 = a

0 b0

c0 d0 ∈ Γ(2). It then suﬃces to ﬁnd h ∈ Z so that Ah[M0] ∈ B, because this element will still map to [(c0,d0)]. One may ﬁnd such an h, via repeated reduction of the bottom entries mod 2d0 and 2c0, implemented via the formulas1

a b c d

Am0 =

a b c d

1 2m 0 1

=

a b + 2am c d + 2cm

,

a − 2bℓ b c − 2dℓ d

a b c d

a b c d

1 0 −2ℓ 1

B0ℓ =

=

.

We will now deduce that the map (5.3) also induces a bijection B˜ ∼= P˜/Z×. It is well-deﬁned because

- 0 −1
- 1 0


b −a d −c

a b c d

=

. (5.4)

It is injective, because if M˜1 = M1S¯, M˜2 = M2S¯, Mi ∈ B ⊔ {1} map to the same element of P˜, then, by the above general remark on the assignment (5.3), we have M˜2 = AℓM˜2, for some ℓ ∈ Z, equivalently M2 = AℓM1, hence ℓ = 0. Finally, to show surjectivity, let (c,d) ∈ P˜. By deﬁnition, c,d are coprime integers, c is odd and d is even. There are two cases:

- • d = 0. Then c ∈ {−1,1} and [S] maps to [(c,d)] under (5.3).
- • d = 0. Then [(d,−c)] ∈ P and by what we have shown above, there is M ∈ B mapping to [(d,−c)]. By (5.4), the element MS¯ ∈ B˜ then maps to [(−c,−d)] = [(c,d)], as required.


![image 127](<2020-stoller-fourier-interpolation-spheres_images/imageFile127.png>)

1Since the bottom row entries of matrices in Γ(2) are of opposite parities, at least one of them reduces by at least 1 in absolute value, in each step in the successive reductions described above. If, say M0Bℓ1Am1Bℓ2 has lower left entry zero, this product equals A−h, for some h ∈ Z and hence AhM0 = B−ℓ2A−m1B−ℓ1. Now ℓ2 = 0, as otherwise the process would have ended earlier, namely when MBℓ1 had lower left entry zero. In fact, we will not need surjectivity in the proof of Theorem 2. It will only be used in the supplementary section 8.

This concludes the proof of Lemma 5.1.

The next lemma and its corollary will be used for certain estimates in §5.5 in combination with the useful identity

a c −

1 c(cτ + d)

aτ + b cτ + d

, (5.5) which holds for all τ ∈ H and all a,b,c,d ∈ R, satisfying with c = 0 and ad − bc = 1.

=

![image 128](<2020-stoller-fourier-interpolation-spheres_images/imageFile128.png>)

![image 129](<2020-stoller-fourier-interpolation-spheres_images/imageFile129.png>)

![image 130](<2020-stoller-fourier-interpolation-spheres_images/imageFile130.png>)

- Lemma 5.2. For every M ∈ B we have |aM| ≤ |cM| and |bM| ≤ |dM| and for every M˜ ∈ B˜ we have |aM˜ | ≤ |cM˜ |.


Proof. Since right-multiplication by S¯ interchanges columns (5.4) and since the upper left entry of S¯ is zero, it suﬃces to prove the assertion about elements of B. We do this via induction on the word length of M ∈ B, but we will add letters on the left in the inductive step. We ﬁrst compute generally, for any a,b,c,d,m,ℓ ∈ Z, that

a b c d

a + 2ℓc b + 2ℓd 2am + c(1 + 4mℓ) 2mb + d(4mℓ + 1)

B0−mAℓ0

=

.

Base case: In the above, take a = d = 1, c = b = 0 and assume that m = 0. We need to show that |1| ≤ |2m| and |2ℓ| ≤ |4mℓ + 1|. This is immediate.

Inductive step: We assume that |a| ≤ |c|, |b| ≤ |d| and that mℓ = 0. We need to show:

- (1) |a + 2ℓc| ≤ |2am + c(1 + 4mℓ)|,
- (2) |b + 2ℓd| ≤ |2mb + d(1 + 4mℓ)|.


If c = 0, then (1) holds trivially and if d = 0, then (2) holds trivially (since m = 0). We therefore assume that cd = 0. Dividing then (1) by |c| and (2) by |d|, the inductive hypothesis reduces our task to showing that for all q ∈ [−1,1] ∩ Q,

|q + 2ℓ| ≤ |2mq + (1 + 4mℓ)| = |2m(q + 2ℓ) + 1|. Introduce y = q + 2ℓ, so that what we want to show is |y| ≤ |2my + 1|. But indeed,

|2my + 1| ≥ 2|m||y| − 1 ≥ 2|y| − 1 ≥ |y|, since |m| ≥ 1 and |y| = |2ℓ + q| ≥ 2 − |q| ≥ 1 since |q| ≤ 1.

- Corollary 5.1. Let Ω ⊂ H be a compact set. Then sup(τ,M)∈Ω×(B∪B˜) |Mτ| < ∞.


Proof. For z ∈ H write Λz = Zz + Z ⊂ C for the lattice generated by z and 1 and, for any lattice Λ ⊂ C, write s(Λ) = inf0 =λ∈Λ |λ| for the length of its shortest vectors. The assignment z  → s(Λz) deﬁnes a continuous function H → (0,+∞), as is well-known. Now let M ∈ B ∪B˜ be represented by ac db and let τ ∈ Ω. We have |c| ≥ 1 and by Lemma 5.2 and (5.5),

1 c(cτ + d) ≤ 1 +

1 infz∈Ω s(Λz)

1 |cτ + d|

a c −

≤ 1 +

|Mτ| =

, which is ﬁnite and depends only on Ω.

![image 131](<2020-stoller-fourier-interpolation-spheres_images/imageFile131.png>)

![image 132](<2020-stoller-fourier-interpolation-spheres_images/imageFile132.png>)

![image 133](<2020-stoller-fourier-interpolation-spheres_images/imageFile133.png>)

![image 134](<2020-stoller-fourier-interpolation-spheres_images/imageFile134.png>)

Remark. In the above proof, instead of using continuity of the shortest vector function, one can simply use that |cτ + d| ≥ Im(τ), for c = 0 and thus generalize the corollary to subsets Ω satisfying infτ∈Ω (Im(τ)) > 0.

- 5.4. Deﬁnition of the generating series and the basis functions. With the preparations from the previous subsections, we are now ready to give solutions to the functional


equations in §5.2 and give the deﬁnition of the functions bp,n,˜bp,n entering Theorem 2. Let p ≥ 5 be an integer. For τ ∈ H and r ∈ C deﬁne the series

2

2Mτ, (5.6)

eπiτr

(Θ3(Mτ)/Θ3(τ))−peπir

Fp(τ,r) = −

|p/2M = −

M∈B

M∈B

2Mτ. (5.7)

2

F˜p(τ,r) =

(Θ3(Mτ)/Θ3(τ))−peπir

eπiτr

|p/2M =

M∈B˜

M∈B˜

We now show they converge absolutely and uniformly on compact sets. So let Ω1 ⊂ H and Ω2 ⊂ C be compact subsets. Then by (5.1) and by Corollary 5.1, we have, for all M ∈ B∪B˜, (τ,r) ∈ Ω1 × Ω2,

exp(π|r|2|Mτ|) |cMτ + dM|p/2

1 |cMτ + dM|p/2

2Mτ ≤

(Θ3(Mτ)/Θ3(τ))−peπir

≪Ω1,Ω2

,

![image 135](<2020-stoller-fourier-interpolation-spheres_images/imageFile135.png>)

![image 136](<2020-stoller-fourier-interpolation-spheres_images/imageFile136.png>)

> 0 with the property that |cMi+dM| ≤ C|cMτ +dM| for all M ∈ B ∪ B˜ and all τ ∈ Ω1. We deduce

By compactness, there exists C = CΩ

1

1 |cMi + dM|p/2

2Mτ ≪Ω1,Ω2

(Θ3(Mτ)/Θ3(τ))−peπir

, (5.8)

sup

![image 137](<2020-stoller-fourier-interpolation-spheres_images/imageFile137.png>)

(τ,r)∈Ω1×Ω2

where the implied constant does not depend upon M ∈ B ∪ B˜. Since p ≥ 5, the sequence ( 0<c2+d2≤N |ci + d|−p/2)N∈N is bounded and increasing in [0,∞), which, combined with (5.8) and the injectivity of the mappings in Lemma 5.1, implies that the series deﬁning Fp,F˜p converge pointwise absolutely and uniformly on Ω1×Ω2 and thus deﬁne continuous functions on H × C that are holomorphic in each variable separately.

Part (ii) of Lemma 5.1 asserted that B and B˜ are stable under right multiplication by powers of A. By absolute convergence, we deduce that the functions Fp, F˜p are both 2periodic in the ﬁrst argument. By deﬁnition of the set B˜ and because of the minus sign in the deﬁnition of Fp(τ,r), they are moreover related by the functional equation

2τ. (5.9)

Fp(τ,r) + (−iτ)−p/2F˜p(−1/τ) = eπir

Replacing r by the Euclidean norm of x ∈ Rp, gives the desired solutions to the system of functional equations in §5.2. For n ∈ Z, we deﬁne

- 1

![image 138](<2020-stoller-fourier-interpolation-spheres_images/imageFile138.png>)

- 2 iy


Fp(τ,r)e−πinτdτ, (5.10)

bp,n(r) =

0+[−1,1]

- 1

![image 139](<2020-stoller-fourier-interpolation-spheres_images/imageFile139.png>)

- 2 iy


F˜p(τ,r)e−πinτdτ, (5.11)

˜bp,n(r) =

0+[−1,1]

for any y0 > 0, as the integrals are independent of y0 (§1.4.4). By continuity of Fp and F˜p and holomorphy in the second argument, the functions r  → bp,n(r) and r  → ˜bp,n(r) are entire and they are clearly even. By the general remarks of §1.4.1, the functions x  → bp,n(|x|),

- x  → ˜bp,n(|x|) are smooth on Rd, but we will also prove this directly in the next section.


- 5.5. Upper bounds for Fourier coeﬃcients. To complete our implementation of the general strategy explained in §5.2 and thus prove Theorem 2, we must give upper bounds for the Fourier coeﬃcients bp,n(r) and ˜bp,n(r) deﬁned in (5.10), (5.11) in terms of n and r. We will do so by ﬁrst bounding the generating functions Fp(τ,r), F˜p(τ,r) themselves and then applying the triangle inequality to the integrals for a suitable height y0 > 0. In the end, we will take y0 ≍ p/n, but also want the upper bound to hold for all pairs (n,p) ∈ N×Z≥5, since we implicitly sum over them in our main interpolation formula. We therefore seek bounds for Fp(τ,r) and F˜p(τ,r) that are equally uniform in y0 = Im(τ). To this end, we deﬁne, for any real k > 2, the auxiliary functions Uk,U˜k : H → (0,+∞) by


|cMτ + dM|−k, U˜k(τ) =

|cMτ + dM|−k. (5.12)

Uk(τ) =

M∈B˜

M∈B

Note that |Fp(τ,r)| ≤ Up/2(τ) and |F˜p(τ,r)| ≤ U˜p/2(τ) for all (τ,r) ∈ H × R.

- Lemma 5.3. There exists a constant C0 > 0 with the following property. For all ε ∈ (0,1/8], all k ≥ 2 + 2ε, all x ∈ [−1,1] and all y0 > 0, we have


max (Uk(x + iy0),U˜k(x + iy0)) ≤ C0ε−2(y0−k + y0−k/2).

Proof. By absolute convergence and the injectivity assertions from Lemma 5.1 and by simply enlarging the sets P, P˜, we have

∞

c

1 (cx + d + ℓc)2 + (cy0)2 k/2

max (Uk(x + iy0),U˜k(x + iy0)) ≤

.

![image 140](<2020-stoller-fourier-interpolation-spheres_images/imageFile140.png>)

c=1

d=1 ℓ∈Z

To bound the denominators from below, we ﬁrst write

(cx + d + ℓc)2 + (cy0)2 = c2 (x + d/c + ℓ)2 + y02 and then use, in the range |ℓ| ≤ 2, the trivial estimate

(x + d/c + ℓ)2 + y02 ≥ y02, while in the range |ℓ| ≥ 3, we use

(x + d/c + ℓ)2 + y02 ≥ 2|x + d/c + ℓ|y0 ≥ 2(|ℓ| − 2)y0, which holds since |x| ≤ 1 and |d/c| ≤ 1 for all terms in the series. We deduce that

∞

max(Uk(x + iy0),U˜k(x + iy0)) ≤

c1−k 5y0−k + (2y0)−k/2

(|ℓ| − 2)−k/2 ,

c=1

|ℓ|≥3

which is now a product. For s > 1, let ζ(s) = ∞n=1 n−s. The sum over |ℓ| ≥ 3 is at most 2ζ(1 + ε), while the sum over c is at most ζ(1 + 2ε). We conclude the analysis by recalling

that lims→1 (s − 1)ζ(s) = 1.

- Corollary 5.2. If n ≤ 0 then bp,n = 0 = ˜bp,n. Proof. By analyticity, it suﬃces to show that bp,n(r) = 0 = ˜bp,n(r) for all r ∈ R. By Lemma


- 5.3 and (5.10) we have, for all y0 > 0 and r ∈ R,


y0−p/2 + y0−p/4 ,

Up/2(τ) ≪ eπny

|bp,n(r)| ≤ eπny

sup

0

0

τ∈iy0+[−1,1]

where the implied constant is independent of p,n,r and y0. Since eπny

≤ 1 we can let

0

- y0 → ∞ to deduce bp,n(r) = 0. The argument for ˜bp,n is very similar.


In the remainder of §5.5, we prove assertions (i) and (ii) of Theorem 2, that is, we prove the claimed upper bounds for ∂αbp,n(|x|), ∂α˜bp,n(|x|) for x ∈ Rd and α ∈ Nd0. In view of

- Corollary 5.2 and the general remarks of §5.2, this will then also prove the radial interpolation formula (1.6) and complete the proof of Theorem 2. We focus on the analysis of Fp and bp,n;


the one for F˜p and ˜bp,n is the same, because of the maximum in Lemma 5.3. We work with the following parameters and notations.

- • A real number ε ∈ (0,1/8].
- • A constant C0 > 0 having the property stated in Lemma 5.3. Until the end of §5.5, a constant will be called absolute, if it depends at most C0.
- • For each 0 ≤ j ≤ |α|, the polynomial Pj = Pα,d,j ∈ Z[2πi][x1,...,xd] of degree at most |α| with the property that for all z ∈ C and x ∈ Rd,

∂xαeπiz|x|

2

= eπiz|x|

2

|α|

j=0

Pj(x)zj. (5.13)

These will play no role if α = 0, a case worth focusing on in a ﬁrst reading.

- • The parameter σ = σp,ε = p/4 − (1 + ε) ≥ 1/8.
- • For |x| > 0, the shorthand Bσ(|x|) = πe σ|x|2


σ

2

= supy∈(0,+∞) yσe−πy|x|

. To start, we diﬀerentiate (5.10), giving

![image 141](<2020-stoller-fourier-interpolation-spheres_images/imageFile141.png>)

1 2 iy

∂xαFp(τ,|x|)e−πinτdτ. (5.14)

∂xαbp,n(|x|) =

![image 142](<2020-stoller-fourier-interpolation-spheres_images/imageFile142.png>)

0+[−1,1]

To bound ∂xαFp(τ,|x|), we apply (5.13) with z = Mτ = a

cM − c 1

M(cMτ+dM) and obtain

M

![image 143](<2020-stoller-fourier-interpolation-spheres_images/imageFile143.png>)

![image 144](<2020-stoller-fourier-interpolation-spheres_images/imageFile144.png>)

|α|

j

j t

2

2

(aM/cM)j−t(−cM(cMτ + dM))−t.

∂xαeπi(Mτ)|x|

= eπi(Mτ)|x|

Pj(x)

t=0

j=0

We have |cM| ≥ 1 by Lemma 5.1 and |aM/cM| ≤ 1 by Lemma 5.2, hence

|α|

j

j t |cMτ + dM|−t.

2

2

|∂xαeπi(Mτ)|x|

| ≤ e−πIm(Mτ)|x|

|Pj(x)|

t=0

j=0

2

We may now either use the trivial bound e−πIm(Mτ)|x|

≤ 1, or, if |x| > 0, e−πIm(Mτ)|x|

2

2

Im(Mτ)−σ ≤ Bσ(|x|)|cMτ + dM|2σ Im(τ)−σ. Using the auxiliary function Uk, deﬁned in (5.12), we deduce

= Im(Mτ)σe−πIm(Mτ)|x|

|α|

j

|∂xαFp(τ,|x|)| ≤

|Pj(x)|

t=0

j=0

j t

|∂xαFp(τ,|x|)| ≤ Bσ(|x|)Im(τ)−σ

Up/2+t(τ), (from the trival bound) (5.15)

|α|

j

|Pj(x)|

t=0

j=0

j t

Up/2−2σ+t(τ), if |x| > 0. (5.16)

We now apply the triangle inequality to (5.14) and use Lemma 5.3, applied with k = p/2+t and the binomial theorem (read “backwards”), to deduce from (5.15) that

|∂xαbp,n(|x|)| ≤ 64C0eπny

0

|α|

|Pj(x)| y0−p/2(1 + y0−1)j + y0−p/4(1 + y0−1/2)j . (5.17)

j=0

If y0 = 2πnp (so that 1/y0 ≤ 2n), then (5.17) implies (after some calculations)

![image 145](<2020-stoller-fourier-interpolation-spheres_images/imageFile145.png>)

|α|

|Pj(x)|(1 + 2n)j, (5.18)

|∂xαbp,n(|x|)| ≤ H1np/2(2πe2/p)p/4

j=0

- for some absolute constant H1 > 0. We deduce similarly from (5.16) and Lemma 5.3, applied with k = p/2 − 2σ + t = 2 + 2ε + t ≥ 2 + 2ε, that |∂xαbp,n(|x|)| is less than or equal to

ε−2C0Bσ(|x|)y0−σeπny

0

|α|

j=0

|Pj(x)| y0−2(1+ε)(1 + y0−1)j + y0−(1+ε)(1 + y0−1/2)j , (5.19)

if |x| > 0. If y0 = πnσ (so that 1/y0 ≤ 30n) then (5.19) implies (after some calculations)

![image 146](<2020-stoller-fourier-interpolation-spheres_images/imageFile146.png>)

|∂xαbp,n(|x|)| ≤ H2ε−2np/4+1+ε|x|−p/2+2(1+ε)

|α|

j=0

|Pj(x)|(1 + 30n)j, (5.20)

- for some absolute constant H2. Here, the choice of y0 also ensured that the term (σ/(πe))σ coming from Bσ(|x|) disappeared. To obtain the ﬁnal bounds in Theorem 2, it only remains to bound the polynomials |Pj(x)| for |x| ≤ R by compactness and continuity (which we do only when α = 0) and to use |jα=0| (1 + κn)j ≪κ,|α| n|α|, for κ ∈ {2,30}.


6. Other function spaces

Here we extend Theorem 1 from S(Rd) to a larger function space. We closely follow the approach of [15, Prop. 4], which generalizes to higher dimensions without much diﬃculty.

- 6.1. Preliminaries. For any k ∈ N0, we denote by Ck(Rd) the space of k-times continuously diﬀerentiable functions f : Rd → C whose partial derivatives are all bounded on Rd. For


f ∈ Ck(Rd) we denote its Ck-norm by f Ck(Rd) = |α|≤k supx∈Rd |∂αf(x)|. For every function f : Rd → C and every B > 0, we deﬁne the extended real number

(1 + |x|B)|f(x)| ∈ [0,+∞]

QB(f) = sup x∈Rd

and then, for every B > d, the space WB(Rd) = {f ∈ C0(Rd) : QB(f) < ∞, QB(fˆ) < ∞}. (6.1)

Note that if B > d + 2 and f ∈ WB(Rd), then f ∈ C2(Rd). The next Lemma shows that we can then also control the decay of the ﬁrst-order partial derivatives of f.

- Lemma 6.1. Let B > 0 and f ∈ C2(Rd). Then QB(f) < ∞ implies QB/2(|∇f|) < ∞.


Proof sketch. Suppose that QB(f) < ∞. For y ∈ Rd, denote by Hf(y) the Hessian of f at y. Then by Taylor’s theorem we have, for any x,ξ ∈ Rd,

1

(1 − t)(ξ · Hf(x + tξ)ξ)dt. By assumption, y  → Hf(y) is a continuous bounded function on Rd. Hence from the above,

f(x + ξ) = f(x) + ξ · ∇f(x) +

0

ξ · ∇f(x) = f(x) − f(x + ξ) + O(|ξ|2). (6.2) Fixing x ∈ Rd with |x| ≥ 1 and taking ξ = ε∇f(x) with ε > 0 chosen small enough in terms of the implied constant in (6.2) and supRd |∇f| , we conclude.

- 6.2. Convolutions. We ﬁx a dimension d ≥ 1 and write


2

φ(x) = e−π|x|

, φε(x) = φ(x/ε)ε−d, ψε(x) = φ(εx) for the Gaussian, the Gaussian approximate identity and the “ﬂat” Gaussian respectively, where ε > 0 and x ∈ Rd. We have φε = ψε and ψε = φε. For any f,g ∈ C0(Rd), we deﬁne

Jεf = ψε · (f ∗ φε), J˜εg = φε ∗ (g · ψε). (6.3)

For every subset Ω ⊂ Rd and every r ≥ 0, we write Br(Ω) to denote the set of all x ∈ Rd, for which there exists ω ∈ Ω such that |x − ω| ≤ r. We write Br(x) = Br({x}) for x ∈ Rd.

- Lemma 6.2. The operators Jε,J˜ε have the following properties.


- (i) For every f ∈ C0(Rd) and all ε > 0, we have Jεf ∈ S(Rd)
- (ii) For all B > d, all f ∈ WB(Rd) and all ε > 0, we have Jεf = J˜εfˆ.
- (iii) There exists a constant C1 > 0, depending only on d, such that for all f ∈ C1(Rd), all x ∈ Rd, and all ε > 0, we have

|Jεf(x) − f(x)| ≤ C1e−π|εx|

2

ε sup

B1(x)

|∇f| + e−

π 2ε2

![image 147](<2020-stoller-fourier-interpolation-spheres_images/imageFile147.png>)

f C0(Rd) + C1ε2|x|2|f(x)|.

- (iv) There exists a constant C2 > 0, depending only on d, such that for all g ∈ C1(Rd), all ξ ∈ Rd satisfying |ξ| ≥ 1 and all ε ∈ (0,1], we have


2

|J˜εg(ξ) − g(ξ)| ≤ C2 ε sup

|∇g| + e−(π/8)|ξ/ε|

g C0(Rd) + ε2|ξ|2|g(ξ)| .

B|ξ|/2(ξ)

Proof. We believe this to be standard, but we sketch the proof for completeness. For (i), we readily check that φε ∗ f is smooth with bounded derivatives. For (ii), we recall that for B > d we have WB(Rd) ֒→ L1(Rd), so that the claim follows from φε = ψε and the convolution theorem. To prove (iii), we write Jεf(x) − f(x) = X + Y + Z, where:

- X = ψε(x) |y|≤1

φε(y)

1

0

(∇f(x + ty) · y)dtdy,

- Y = ψε(x) |y|≥1

φε(y)(f(x + y) − f(x)) dy,

- Z = (ψε(x) − 1)f(x).


The integral X gives the ﬁrst term in the inequality claimed in (iii), where the factor ε comes from a change of variables y ↔ y/ε. The integral Y gives the second, using |y|≥1 φε(y) ≪d

π

e−

2ε2 . The integral Z gives the third, using |ψε(x) − 1| ≤ πε2|x|2. To prove (iv), suppose that |ξ| ≥ 1 and write J˜εg(ξ) − g(ξ) = U + V + W, where

![image 148](<2020-stoller-fourier-interpolation-spheres_images/imageFile148.png>)

- U = |y|≤|ξ|/2

φε(y)ψε(ξ + y)

1

0

(∇g(ξ + ty) · y)dtdy,

- V = |y|≥|ξ|/2

φε(y)ψε(ξ + y)(g(y + ξ) − g(ξ)) dy,

- W = g(ξ) Rd


φε(y)(ψε(y + ξ) − 1)dy.

To bound U, we use the gradient bound as for X. For V , we ﬁrst apply the triangle inequality and then change to the variable u = y/ε, to obtain

φ(y/ε)ψε(y + ξ)ε−ddy = 2 g C0(Rd)

|V | ≤ 2 g C0(Rd)

φ(u)ψε(εu + ξ)du.

|ξ| 2

|ξ| 2ε

|y|≥

|u|≥

![image 149](<2020-stoller-fourier-interpolation-spheres_images/imageFile149.png>)

![image 150](<2020-stoller-fourier-interpolation-spheres_images/imageFile150.png>)

2/2 and bounding ψε(εu+ξ) ≤ 1 here, we get the second term claimed in (iv). For W, we apply the triangle inequality and use the estimate

2/2e−π|u|

Writing φ(u) = e−π|u|

|ψε(y + ξ) − 1| ≤ πε2|y + ξ|2 ≤ πε2|ξ|2(|y| + 1)2,

where the last inequality uses the assumption |ξ| ≥ 1. We bound bound the remaining integral independently of ε, by changing to the variable u = y/ε, noting that (|εu| + 1)2 ≤ (|u| + 1)2, since ε ≤ 1.

6.3. Limiting argument. Suppose that d ≥ 5 and An,A˜n ∈ C∞(Rd × S) be such that they satisfy the conclusion of Theorem 1. In principle, a similar discussion applies to lower dimensions, using Theorem 3, but we stick to d ≥ 5 for simplicity.

We consider henceforth a ﬁxed compact subset Ω ⊂ Rd and we suppose given constants K,a,c > 0 so that for all n ∈ N,

|An(x,ζ)| + |A˜n(x,ζ)| ≤ Knad+c. (6.4)

sup

(x,ζ)∈Ω×S

If An, A˜n are as deﬁned in §3, then Theorem 2 and Lemma 3.1 provide admissible values of a,c. Namely, one can take (a,c) = (1/2,0) if Ω = {0}, or (a,c) = (5/4,1/8) if 0 ∈/ Ω. We proceed generally and specialize to these values later. Consider a decay rate B satisfying

B > max(d + 2,4(1 + ad + c)). (6.5) For all f,g ∈ C0(Rd), satisfying QB(f) < ∞ and QB(g) < ∞ and all x ∈ Ω, we may deﬁne

∞

∞

A˜n(x,ζ)g(√nζ)dζ,

An(x,ζ)f(√nζ)dζ, Rg˜ (x) =

![image 151](<2020-stoller-fourier-interpolation-spheres_images/imageFile151.png>)

![image 152](<2020-stoller-fourier-interpolation-spheres_images/imageFile152.png>)

Rf(x) =

n=1 S

n=1 S

which converge absolutely and vary continuously with x ∈ Ω, since B > 2(1 + ad + c). Let f ∈ WB(Rd). It follows from parts (i) and (ii) of Lemma 6.2 and from Theorem 1 that for all ε > 0,

f = (f − Jεf) + Jεf = (f − Jεf) + R(Jεf) + R˜( Jεf)

= (f − Jεf) + (Rf + R˜fˆ) + R(Jεf − f) + R˜(J˜εfˆ− fˆ),

as functions on Ω. We want to show that f = Rf + R˜fˆ, so it suﬃces to show that the terms depending upon ε tend to zero as ε tends to zero. By part (iii) of Lemma 6.2, we have supΩ |f − Jεf| → 0, as ε → 0 and our assumption (6.4) implies

∞

nad+c √sup nS

|R(Jεf − f)| ≤ K

|Jεf − f|, (6.6)

sup

Ω

![image 153](<2020-stoller-fourier-interpolation-spheres_images/imageFile153.png>)

n=1

∞

|R˜(J˜εfˆ− fˆ)| ≤ K

|J˜εfˆ− fˆ|. (6.7)

nad+c √sup nS

sup

Ω

![image 154](<2020-stoller-fourier-interpolation-spheres_images/imageFile154.png>)

n=1

It follows from part (iii) of Lemma 6.2, applied with x = ζ√n and part (iv) with ξ = ζ√n, for (ζ,n) ∈ S × N and the assumption on the decay rate B, that (6.6), (6.7) are both O(ε). Here, the more subtle terms come from the gradients of f and fˆ, which may be controlled by Lemma 6.1, implying the estimates

![image 155](<2020-stoller-fourier-interpolation-spheres_images/imageFile155.png>)

![image 156](<2020-stoller-fourier-interpolation-spheres_images/imageFile156.png>)

|∇fˆ| ≪ n−B/4.

|∇f| ≪ n−B/4, sup

sup

B√n/2(√nS)

B1(√nS)

![image 157](<2020-stoller-fourier-interpolation-spheres_images/imageFile157.png>)

![image 158](<2020-stoller-fourier-interpolation-spheres_images/imageFile158.png>)

![image 159](<2020-stoller-fourier-interpolation-spheres_images/imageFile159.png>)

To summarize, assuming the bound (6.4) on An, A˜n and assuming B satisﬁes (6.5), the interpolation formula (1.1) holds for all f ∈ WB(Rd) and all x ∈ Ω with uniform convergence. Specializing the discussion to the concrete values (a,c) = (5/4,1/8) and noting that 5/4 > 1/2 and 4(1 + 5d/4 + 1/8) = 5d + 9/2, we obtain the following corollary.

- Corollary 6.1. Suppose that B > 5d+9/2. Then the interpolation formula (1.1) in Theorem


1 holds for all f ∈ WB(Rd) with absolute convergence at every point and uniform convergence on compact subsets avoiding the origin.

7. Relations between restrictions of Schwartz functions to spheres

Here we elaborate on the remarks on free interpolation made in §1.2. The main result of this section, Proposition 7.1 below, won’t be used elsewhere in the paper, but may give an interesting comparison to other work. We again restrict to dimensions d ≥ 5 for simplicity.

Recall that Radchenko and Viazovska prove in [15, Thm2], that the linear map sending f ∈ Srad(R1) to the pair of sequences (f(√n))n∈N

, (fˆ(√n))n∈N

![image 160](<2020-stoller-fourier-interpolation-spheres_images/imageFile160.png>)

![image 161](<2020-stoller-fourier-interpolation-spheres_images/imageFile161.png>)

deﬁnes an isomorphism of Fr´echet spaces with a subspace of co-dimension one, in the space of all pairs of rapidly decreasing sequences of complex numbers. This subspace is cut out by a single linear functional coming from Poisson summation.

0

0

In our setting of not necessarily radial functions, we consider the linear map Φd : S(Rd) −→ Vd, f  → (f(√n ·))n∈N,(fˆ(√n·))n∈N , (7.1)

![image 162](<2020-stoller-fourier-interpolation-spheres_images/imageFile162.png>)

![image 163](<2020-stoller-fourier-interpolation-spheres_images/imageFile163.png>)

where Vd denotes the the space all pairs of sequences of functions fn,gn ∈ C∞(Sd−1), whose sup-norms decay rapidly with n.

- Proposition 7.1. For d ≥ 5, the map Φd has inﬁnite dimensional cokernel. In fact, the annihilator of the image of Φd is an inﬁnite dimensional subspace of the dual space Vd∗.


To prepare the proof of this proposition, let us introduce the theta functions Θ2(τ) = θ10(τ) =

2τ, Θ4(τ) = θ01(τ) =

2τ.

eπi(n+1/2)

(−1)neπin

n∈Z

n∈Z

For any half-integer k ≥ 0, let Mk(Γ(2)) denote the space of modular forms of weight k for Γ(2), where modularity refers to the slash action introduced in §5.1.4. By [19, Thm 7.1.7],

this space has dimension 1 + ⌊k/2⌋ and {Θ42jΘ32k−4j}0≤j≤⌊k/2⌋ is a basis. For ϕ ∈ Mk(Γ(2)) we deﬁne ϕ0 ∈ Mk(Γ(2)) by ϕ0(τ) = (−iτ)−kϕ(−1/τ).

We moreover ﬁx, for each m ≥ 0, an orthonormal basis Bm ⊂ Hm(Sd−1) and deﬁne the auxiliary function Pm(ζ) = u∈B

![image 164](<2020-stoller-fourier-interpolation-spheres_images/imageFile164.png>)

u(ζ), Note that Pm,Pµ L2(S) = δm,µ|Bm|.

m

Proof of Proposition 7.1. Recall ﬁrst that the spaces Mk(Γ(2)) are linearly independent as k varies. We will deﬁne a linear map ϕ  → ϕ∗ from the space Md = ⊕m≥0Md+m/2(Γ(2)) to the annihilator of the image of Φd and show that this map restricts to an injection on the inﬁnite dimensional subspace Jd, consisting of all ﬁnite sums of forms ϕ ∈ Md/2+m(Γ(2)), such that ϕ and ϕ0 vanish at inﬁnity (the ϕ that vanish at the cusps 0 and ∞ of Γ(2)).

By linear independence of the spaces Mk(Γ(2)), it suﬃces to deﬁne ϕ∗ : Vd → C for ϕ ∈ Md/2+m(Γ(2)), in which case the deﬁnition is

∞

∞

fn(ζ)Pm(ζ/√n)dζ − im

gn(ζ)Pm(ζ/√n)dζ,

ϕ∗((fn),(gn)) =

![image 165](<2020-stoller-fourier-interpolation-spheres_images/imageFile165.png>)

![image 166](<2020-stoller-fourier-interpolation-spheres_images/imageFile166.png>)

ϕ(n)

ϕ0(n)

Sd−1

Sd−1

n=1

n=1

where the series converge absolutely since the Fourier coeﬃcients ϕ(n) of ϕ and ϕ0(n) of ϕ0 are polynomially bounded. It now suﬃces to prove the following statements for all ϕ ∈ Id.

(i) ϕ∗(Φd(f)) = 0 for all f ∈ S(Rd). (ii) ϕ∗ = 0, if and only if ϕ = 0.

2

By continuity, it suﬃces to verify (i) for all Schwartz functions of the form f(x) = w(x)eπiτ|x|

, with w ∈ ∪m≥0Bm and τ ∈ H, since those functions generate a dense subspace of S(Rd) (compare with the proof of part (iii) of Proposition 2.1). In this case, the desired identity reduces

to the trivial identity ϕ(τ)−(−iτ)−d/2−mϕ0(τ) = 0, by orthogonality of spherical harmonics. To prove assertion (ii), suppose that ϕ∗ = 0, where ϕ = Nj=1 ϕj ∈ Jd, ϕj ∈ Md/2+m

(Γ(2)) and m1 < m2 < ··· < mN. Fix n0 ∈ N and deﬁne fn,gn ∈ C∞(Sd−1) by

j

N

(√nζ), gn(ζ) = 0.

1 |Bmj|

![image 167](<2020-stoller-fourier-interpolation-spheres_images/imageFile167.png>)

![image 168](<2020-stoller-fourier-interpolation-spheres_images/imageFile168.png>)

Pm

fn(ζ) = δn,n

![image 169](<2020-stoller-fourier-interpolation-spheres_images/imageFile169.png>)

j

0

j=1

A short computation then shows that ϕ∗((fn),(gn)) = Nj=1 ϕj(n0) = 0 and hence ϕ = 0, since n0 was arbitrary.

8. More on the functions bp,n(r)

Here we present further connections of the series Fp(τ,r) deﬁned in (5.6), to classical Poincar´e series by expressing the coeﬃcients bp,n(r) deﬁned in (5.10) as a sum of Bessel functions times Kloosterman-type sums. By combining the formulas thus obtained with known estimates for Fourier coeﬃcients of cusp forms, we will prove in Proposition 8.1 below that inﬁnitely many of the functions bp,n(r) are not of rapid decay. This points out two diﬀerences between the interpolation formula in Theorem 2 and the interpolation theorems in [15, 6]. The basis functions in those theorems are Schwartz functions, whose values at the interpolation nodes give, together with the values of their Fourier transforms, the “natural” basis in a suitable space of pairs (or quadruples) of sequences of complex numbers. By contrast, we will prove that, whenever the nth Poincar´e series of weight p/2 on Γ0(4) does

not vanish identically, the function bp,n(r) does not have either of these properties. For simplicity, we focus on even integers p here and the functions bp,n(r). Similar results should hold for odd p and the functions ˜bp,n(r).

![image 170](<2020-stoller-fourier-interpolation-spheres_images/imageFile170.png>)

To start, we recall from §5.3 the deﬁnition of the set B ⊂ Γ(2) and its basic properties. We choose a complete set of representatives R(B) ⊂ B for the quotient B/ A . By absolute and uniform convergence of the generating series Fp(τ,r), deﬁned in (5.6) and by (5.10), we have

- 1

![image 171](<2020-stoller-fourier-interpolation-spheres_images/imageFile171.png>)

- 2 M∈R(B) ℓ∈Z iy0+[−1,1]


2

(eπiτr

|p/2(MAℓ))e−πinτdτ

bp,n(r) = −

- 1

![image 172](<2020-stoller-fourier-interpolation-spheres_images/imageFile172.png>)

- 2 M∈R(B) iy0+R


2

(eπiτr

|p/2M)e−πinτdτ. (8.1)

= −

The justiﬁcation of the second equal sign is implied by assertion (i) of the Lemma 8.1 below, which will be used to evaluate the above integrals. Before we give its statement, let us recall that the Bessel function Jα is given by

α ∞

(−1)j Γ(α + 1 + j)j!

2j

x 2

x 2

, x,α > 0.

Jα(x) =

![image 173](<2020-stoller-fourier-interpolation-spheres_images/imageFile173.png>)

![image 174](<2020-stoller-fourier-interpolation-spheres_images/imageFile174.png>)

![image 175](<2020-stoller-fourier-interpolation-spheres_images/imageFile175.png>)

j=0

2/q and for any coprime integers c,d with c > 0, we deﬁne

For integers a,q with q ≥ 1, we deﬁne the Gauss sum Gq(a) = qm=1 e2πiam

- 1

![image 176](<2020-stoller-fourier-interpolation-spheres_images/imageFile176.png>)

- 2G2c(d) if c ≡ 0 (mod 2), Gc(2d) if c ≡ 1 (mod 2).


gc(d) =

Using Poisson summation one can verify that for any M = (∗c ∗d) ∈ Γθ with c > 0, one has

Θ3(Mz) = gc(d)(−i(z + d/c))1/2Θ3(z), (8.2) for all z ∈ H (note that z + d/c ∈ H, so §1.4.3 applies); see also [14, pp. 28-33] for a detailed treatment on the transformation laws of Θ3(τ) and ϑ(z,τ), or [10, Thm 10.10] for the closely related function θ(z) = Θ3(2z). Raising (8.2) to the eighth power, we deduce from (5.1) that gc(d)8 = c4 and in particular, |gc(d)| = √c.

![image 177](<2020-stoller-fourier-interpolation-spheres_images/imageFile177.png>)

Lemma 8.1. For matrices M = ac db ∈ Γθ with c > 0, real numbers y0 > 0, r ≥ 0 and integers n, p such that p ≥ 5, deﬁne the integral

2

(eπiτr

|p/2M)e−πinτdτ.

Ip(M,r,n,y0) =

iy0+R

- (i) The integral Ip(M,r,n,y0) converges absolutely and is independent of y0.
- (ii) For all n ≤ 0, we have Ip(M,r,n,y0) = 0.
- (iii) For all n ≥ 1, we have Ip(M,0,n,y0) = 2π(πn)

p/2−1

![image 178](<2020-stoller-fourier-interpolation-spheres_images/imageFile178.png>)

Γ(p/2) gc(d)−peπi

d

![image 179](<2020-stoller-fourier-interpolation-spheres_images/imageFile179.png>)

cn.

- (iv) For all n ≥ 1 and r > 0, we have


cnJp/2−1(2πr√n/c).

cr2eπi

a

d

Ip(M,r,n,y0) = (2π)(n/r2)p/4−1/2cp/2−1gc(d)−peπi

![image 180](<2020-stoller-fourier-interpolation-spheres_images/imageFile180.png>)

![image 181](<2020-stoller-fourier-interpolation-spheres_images/imageFile181.png>)

![image 182](<2020-stoller-fourier-interpolation-spheres_images/imageFile182.png>)

The proof of Lemma 8.1 closely follows standard computations in text books, for example [10, Ch. 3.2]. We include them for completeness, convenience of the reader and because of the minor issue that the parameter r2 is not an integer in our setting.

2

Proof of Lemma 8.1. We abbreviate by g the function g(τ) = (eπiτr

|p/2M)e−πinτ. For part (i), note that for τ = t + iy0,

eπny

eπny

0

0

|g(τ)| = |g(t + iy0)| ≤

, (8.3)

=

![image 183](<2020-stoller-fourier-interpolation-spheres_images/imageFile183.png>)

![image 184](<2020-stoller-fourier-interpolation-spheres_images/imageFile184.png>)

((ct + d)2 + c2y02)p/4

|cτ + d|p/2

which is an integrable function of t. Independence y0 follows by applying Cauchy’s Theorem to the function g(τ) and rectangles y0 ≤ Im(τ) ≤ y1, |Re(τ)| ≤ R, where R → ∞. Alternatively, it follows from the formulas (iii) and (iv), to be proven below.

Since we do not need part (ii) further below, we omit the simple proof, but we note that the statement of part (ii) would reprove Corollary 5.2.

To prepare for parts (iii) and (iv), we write Mτ = ac − c2(τ+1d/c) and use (8.2) to write

![image 185](<2020-stoller-fourier-interpolation-spheres_images/imageFile185.png>)

![image 186](<2020-stoller-fourier-interpolation-spheres_images/imageFile186.png>)

r2

cr2e−πi

a

eπi

c2(τ+d/c)e−πin(τ+d/c−d/c) gc(d)p(−i(τ + d/c))p/2

![image 187](<2020-stoller-fourier-interpolation-spheres_images/imageFile187.png>)

![image 188](<2020-stoller-fourier-interpolation-spheres_images/imageFile188.png>)

2

g(τ) = (eπiτr

|p/2M)e−πinτ =

.

![image 189](<2020-stoller-fourier-interpolation-spheres_images/imageFile189.png>)

By changing variables τ ↔ τ + d/c, we obtain

r2

e−πi

c2τ e−πinτ (−iτ)p/2

![image 190](<2020-stoller-fourier-interpolation-spheres_images/imageFile190.png>)

cr2eπi

a

d

Ip(M,r,n,y0) = gc(d)−peπi

cnJp(r,c), where Jp(r,c) =

dτ.

![image 191](<2020-stoller-fourier-interpolation-spheres_images/imageFile191.png>)

![image 192](<2020-stoller-fourier-interpolation-spheres_images/imageFile192.png>)

![image 193](<2020-stoller-fourier-interpolation-spheres_images/imageFile193.png>)

iy0+R

- For the proof of part (iii), we need the formula R e

iνt

![image 194](<2020-stoller-fourier-interpolation-spheres_images/imageFile194.png>)

(η+it)z dt = (2π)e

−νηνz−1

![image 195](<2020-stoller-fourier-interpolation-spheres_images/imageFile195.png>)

Γ(z) , taken from [7, 8.315] and valid for Re(z) > 1, η,ν > 0, where the argument of η + it taken in (−π/2,π/2), consistent with our convention form §1.4.3. By writing τ = iy + t, changing t to −t in the integral and applying the previous formula with η = y0, ν = πn, z = p/2, we obtain

Jp(0,c) = eπny

0

R

eπint (y0 + it)p/2

![image 196](<2020-stoller-fourier-interpolation-spheres_images/imageFile196.png>)

= eπny

0

(2π)e−πny

0

(πn)p/2−1 Γ(p/2)

![image 197](<2020-stoller-fourier-interpolation-spheres_images/imageFile197.png>)

=

(2π)(πn)p/2−1 Γ(p/2)

![image 198](<2020-stoller-fourier-interpolation-spheres_images/imageFile198.png>)

.

- For the proof of part (iv), we introduce the variable β = r2/c2 > 0. We write e−πi(β/τ) = ∞ j=0


1 j!(−πiβ/τ)j and reduce to the case r = 0 considered (iii) in the following way:

![image 199](<2020-stoller-fourier-interpolation-spheres_images/imageFile199.png>)

∞

∞

e−πinτ τj(−iτ)p/2

1 j!

1 j!

(−πiβ)j

(−πβ)j Jp+2j(0,c)

Jp(r,c) =

dτ =

![image 200](<2020-stoller-fourier-interpolation-spheres_images/imageFile200.png>)

![image 201](<2020-stoller-fourier-interpolation-spheres_images/imageFile201.png>)

![image 202](<2020-stoller-fourier-interpolation-spheres_images/imageFile202.png>)

iy0+R

j=0

j=0

∞

(2π)(πn)p/2+j−1 Γ(p/2 + j)

(−1)j j!

(πβ)j

![image 203](<2020-stoller-fourier-interpolation-spheres_images/imageFile203.png>)

= (2π)(n/β)p/4−1/2Jp/2−1(2π βn)

=

![image 204](<2020-stoller-fourier-interpolation-spheres_images/imageFile204.png>)

![image 205](<2020-stoller-fourier-interpolation-spheres_images/imageFile205.png>)

j=0

To proceed with the computation (8.1), let us deﬁne, for all n,c ∈ N such that c is even and all r ∈ C, the sum

2c

(√c/gc(d))peπi(

α(c,d)

c r2+dnc ), (8.4)

![image 206](<2020-stoller-fourier-interpolation-spheres_images/imageFile206.png>)

Sp(r,n,c) =

![image 207](<2020-stoller-fourier-interpolation-spheres_images/imageFile207.png>)

![image 208](<2020-stoller-fourier-interpolation-spheres_images/imageFile208.png>)

d=1,gcd(c,d)=1

where α(c,d) ∈ Z is deﬁned by requiring that α(c,dc ) d∗ ∈ B, which is possible by Lemma 5.1. We can deﬁne an analogous sum S˜p(r,n,c) for all odd positive integers c. Inserting the

formulas from Lemma 8.1 into (8.1), we obtain

∞

Sp(r,n,c)Jp/2−1(2πr√n/c), r > 0, (8.5)

1 c

bp,n(r) = −π(n/r2)p/4−1/2

![image 209](<2020-stoller-fourier-interpolation-spheres_images/imageFile209.png>)

![image 210](<2020-stoller-fourier-interpolation-spheres_images/imageFile210.png>)

c=1 c≡0(2)

∞

π(πn)p/2−1 Γ(p/2)

1 cp/2

bp,n(0) = −

Sp(0,n,c). (8.6)

![image 211](<2020-stoller-fourier-interpolation-spheres_images/imageFile211.png>)

![image 212](<2020-stoller-fourier-interpolation-spheres_images/imageFile212.png>)

c=1 c≡0(2)

A similar formula holds for ˜bp,n(r) involving S˜p(r,n,c), where we sum over odd positive integers.

Let us now specialize (8.5) to radii r = √m with m ∈ N and to even dimensions p ≥ 6 and moreover introduce the notation k = p/2 ∈ Z≥3. We shall relate the values b2k,n(√m) to Fourier coeﬃcients of (actual) Poincar´e series of weight k on Γ0(4). To that end, we start by replacing c by c/2 in (8.5) and correspondingly sum over c ∈ 4N, giving

![image 213](<2020-stoller-fourier-interpolation-spheres_images/imageFile213.png>)

![image 214](<2020-stoller-fourier-interpolation-spheres_images/imageFile214.png>)

∞

k−1 2

b2k,n(√m) = −π

Sp(√m,n,c/2)Jk−1(4π√nm/c). (8.7)

2 c

n m

![image 215](<2020-stoller-fourier-interpolation-spheres_images/imageFile215.png>)

![image 216](<2020-stoller-fourier-interpolation-spheres_images/imageFile216.png>)

![image 217](<2020-stoller-fourier-interpolation-spheres_images/imageFile217.png>)

![image 218](<2020-stoller-fourier-interpolation-spheres_images/imageFile218.png>)

![image 219](<2020-stoller-fourier-interpolation-spheres_images/imageFile219.png>)

![image 220](<2020-stoller-fourier-interpolation-spheres_images/imageFile220.png>)

c=1 c≡0(4)

Next, we rewrite the factor c/2/gc/2(d) appearing in Sp(√m,n,c/2). For this, we use that for 4|c and d coprime to c, we have Gc(d)2 = i(2c)χ(d) , where χ : (Z/4Z)× → {−1,1} denotes the non-trivial character. (This can be deduced from (8.2) and [10, eq. 2.73, p. 46], for example.) Hence ( c/2/gc/2(d))2k = i−kχ(d)k. Moreover, we have α(c/2,d)d ≡ 1 (mod c) and thus we can rewrite (8.7) as

![image 221](<2020-stoller-fourier-interpolation-spheres_images/imageFile221.png>)

![image 222](<2020-stoller-fourier-interpolation-spheres_images/imageFile222.png>)

![image 223](<2020-stoller-fourier-interpolation-spheres_images/imageFile223.png>)

k−1 2

b2k,n(√m) = −2πi−k

n m

![image 224](<2020-stoller-fourier-interpolation-spheres_images/imageFile224.png>)

![image 225](<2020-stoller-fourier-interpolation-spheres_images/imageFile225.png>)

σk(m,n), (8.8) where, abbreviating e(w) = e2πiw and writing d¯ for the inverse of d mod c,

![image 226](<2020-stoller-fourier-interpolation-spheres_images/imageFile226.png>)

∞

Sχk(m,n,c)Jk−1(4π√nm/c),

1 c

![image 227](<2020-stoller-fourier-interpolation-spheres_images/imageFile227.png>)

σk(m,n) =

![image 228](<2020-stoller-fourier-interpolation-spheres_images/imageFile228.png>)

c=1 c≡0(4)

dm ¯ + nd c

χ(d)ke

Sχk(m,n,c) =

.

![image 229](<2020-stoller-fourier-interpolation-spheres_images/imageFile229.png>)

d∈(Z/cZ)×

Consider the mth Poincar´e series for Γ0(4) of weight k and character χk ∈ {χ,1}: Pm(z) =

χ(γ)k(cγz + dγ)−ke(m(γz)), (8.9)

γ∈Γ∞\Γ0(4)

where Γ∞ ⊂ Γ0(4) denotes the subgroup of upper triangular matrices, where cγ,dγ denote the bottom row entries of γ and where we suppress the dependence on k and hence χ from the notation. It is well-known [12, Lemma 14.2] that its nth Fourier coeﬃcient is given by

k−1 2

n m

![image 230](<2020-stoller-fourier-interpolation-spheres_images/imageFile230.png>)

Pm(n) = 2πi−k

(δ(m,n) + σk(m,n)) . (8.10)

![image 231](<2020-stoller-fourier-interpolation-spheres_images/imageFile231.png>)

Comparing (8.10) with (8.8) we deduce that b2k,n(√m) = − Pm(n), for all m,n ∈ N such that n = m. The following proposition shows that, for inﬁnitely many n, the upper bounds

![image 232](<2020-stoller-fourier-interpolation-spheres_images/imageFile232.png>)

for bp,n(r) given in (1.8) in Theorem 2, can’t be signiﬁcantly improved: the term r−(p/2)+2+ε cannot be replaced by r−(p/2)+1−ε.

- Proposition 8.1. Fix an even integer p ≥ 6 and let k = p/2. There exist inﬁnitely many


integers n ≥ 1 with the following property. For each ε > 0, the function r  → rk−1+εb2k,n(r) is unbounded on (0,+∞), in fact, unbounded on the subset of r = √m, m ∈ N.

![image 233](<2020-stoller-fourier-interpolation-spheres_images/imageFile233.png>)

Proof. We ﬁrst recall that, for any n ≥ 1, taking the Petersson inner product of the nth Poincar´e series Pn (as deﬁned in (8.9)) with any f ∈ Mk(Γ0(4),χk) returns the nth Fourier coeﬃcient f(n) of f, up to nonzero scalars (see [12, Lemma 14.3]). Since the space Mk(Γ0(4),χk) is nonzero and a nonzero modular form has inﬁnitely many nonzero Fourier coeﬃcients, there are inﬁnitely many indices n, for which Pn does not vanish identically.

Fix an index n ∈ N such that Pn = 0 and assume that for some A > 0, we have b2k,n(r) =

O(r−A), as r → ∞. We will show that A ≤ k−1. Our main calculation b2k,n(√m) = − Pm(n) and (8.8), (8.10) imply that, for all m ∈ N \ {n},

![image 234](<2020-stoller-fourier-interpolation-spheres_images/imageFile234.png>)

|b2k,n(√m)| = | Pm(n)| =

k−1

n m

![image 235](<2020-stoller-fourier-interpolation-spheres_images/imageFile235.png>)

| Pn(m)|.

![image 236](<2020-stoller-fourier-interpolation-spheres_images/imageFile236.png>)

Our assumption then gives | Pn(m)| = O(m−A/2+k−1), as m → ∞. In particular, we have M−k Mm=1 | f(m)|2 = O(M−A+k−1), as M → ∞. On the other hand, the Rankin– Selberg method (see [17, Theorem 1 and Remark B on page 364]) implies that for every f ∈ Sk(Γ0(4),χk), the Fourier coeﬃcients f(m) satisfy

M

| f(m)|2 = ck(f)Mk + O(Mk−2/5), M → ∞,

m=1

where ck(f) is proportional to the Peterson norm of f (which is > 0, if and only f = 0). Taking f = Pn here and comparing the two asymptotic relations, we deduce A ≤ k − 1.

Remark. Little is known about the (non-)vanishing of individual Poincar´e seires, even in level 1. A result of Mozzochi [13][Thm 2], that builds up on the work of Rankin [18] in level 1, implies that, for all suﬃciently large even integral weights k, the ﬁrst O(k1.99) Poincar´e series of weight k on Γ0(N), do not vanish identically.

Acknowledgments. I would like to thank Maryna Viazovska, my doctoral advisor, for her valuable ideas, her support and guidance over the course of this work. That a formula like the one in Theorem 1 could exist, was conjectured by Danylo Radchenko, whom I thank for several enlightening discussions and suggestions. I also thank Matthew de Courcy-Ireland for giving me detailed feedback on earlier drafts of this paper and helpful discussions.

References

- [1] Sheldon Axler, Paul Bourdon, and Wade Ramey. Harmonic Function Theory. Springer, 2001.
- [2] S. Bochner. Theta relations with spherical harmonics. Proceedings of the National Academy of Sciences of the United States of America, 37(12):804–808, 1951.
- [3] Andiry Bondarenko, Danylo Radchenko, Kristian Seip. Fourier interpolation with zeros of zeta and L-functions. arXiv e-prints, 2005.02996, 2020.
- [4] Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko, and Maryna Viazovska. The sphere packing problem in dimension 24. Annals of Mathematics, 185(3):1017–1033, 2017.
- [5] Henry Cohn and Felipe Gon¸calves. An optimal uncertainty principle in twelve dimensions via modular forms. Inventiones mathematicae, 217(3):799–831, 2019.


- [6] Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko, and Maryna Viazovska. Universal optimality of the E8 and Leech lattices and interpolation formulas. Annals of Mathematics, to appear.
- [7] Gradshteyn, I. S. and Ryzhik, I. M. Table of integrals, series, and products. Elsevier/Academic Press, Amsterdam, 2007.
- [8] Loukas Grafakos and Gerald Teschl. On fourier transforms of radial functions and distributions. Journal of Fourier Analysis and Applications, 19(1):167–179, 2013.
- [9] Roger E. Howe and Eng C. Tan. Non-Abelian Harmonic Analysis: Applications of SL(2, R). Universitext. Springer New York, 2012.
- [10] Henryk Iwaniec. Topics in Classical Automorphic Forms. American Mathematical Society, 1997.
- [11] Marvin I. Knopp. Some new results on the Eichler cohomology of automorphic forms. Bulletin of the American Mathematical Society, 80(4):607–632, 07, 1974.
- [12] Emmanuel Kowalski, Henryk Iwaniec. Analytic Number Theory, American Mathematical Society, 2004.
- [13] C Mozzochi. On the non-vanishing of Poincar´e series. Proceedings of the Edinburgh Mathematical Society, 32(1), 131-137, 1989.
- [14] David Mumford. Tata lectures on Theta, I. Birkh¨auser, 1994.
- [15] Danylo Radchenko and Maryna Viazovska. Fourier interpolation on the real line. Publications math´ematiques de l’IHES,´ 129(1):51–81, 2019.
- [16] Joa˜o P. G. Ramos and Mateus Sousa. Fourier uniqueness pairs of powers of integers. Journal of the European Mathematical Society, to appear.
- [17] Robert Rankin. Contributions to the theory of Ramanujan’s function τ(n) and similar arithmetical functions: II. The order of the Fourier coeﬃcients of integral modular forms. Mathematical Proceedings of the Cambridge Philosophical Society, 35(3), 357-372, 1939.
- [18] Robert Rankin. The vanishing of Poincar´e series. Proceedings of the Edinburgh Mathematical Society. 23(2), 151-161. 1980.
- [19] Robert Rankin. Modular Forms and Functions. Cambridge University Press, 1977.
- [20] Jean-Pierre Serre. A Course in Arithmetic. Springer, 1973.
- [21] Elias M. Stein and Guido Weiss. Introduction to Fourier Analysis on Euclidean Spaces. Princeton University Press, 1971.
- [22] Maryna S. Viazovska. The sphere packing problem in dimension 8. Annals of Mathematics, 185(3):991– 1015, 2017.
- [23] Hassler Whitney. Diﬀerentiable even functions. Duke Mathematical Journal, 10(1):159–160, 03, 1943.


Ecole Polytechnique F´ed´erale de Lausanne, Lausanne, Switzerland Email address: martin.stoller@epfl.ch

