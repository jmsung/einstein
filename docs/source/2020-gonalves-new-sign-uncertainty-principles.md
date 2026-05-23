---
type: source
kind: paper
title: New Sign Uncertainty Principles
authors: Felipe Gonçalves, Diogo Oliveira e Silva, João P. G. Ramos
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2003.10771v4
source_local: ../raw/2020-gonalves-new-sign-uncertainty-principles.pdf
topic: author-sweep
cites:
---

DISCRETE ANALYSIS, 2023:9, 46 pp. www.discreteanalysisjournal.com

## arXiv:2003.10771v4[math.CA]20Jul2023

# New Sign Uncertainty Principles

##### Felipe Gonçalves* Diogo Oliveira e Silva† João P. G. Ramos‡

Received 7 September 2021; Published 21 July 2023

Abstract: We prove new sign uncertainty principles which vastly generalize the recent developments of Bourgain, Clozel & Kahane and Cohn & Gonçalves, and apply our results to a variety of spaces and operators. In particular, we establish new sign uncertainty principles for Fourier and Dini series, the Hilbert transform, the discrete Fourier and Hankel transforms, spherical harmonics, and Jacobi polynomials, among others. We present numerical evidence highlighting the relationship between the discrete and continuous sign uncertainty principles for the Fourier and Hankel transforms, which in turn are connected with the sphere packing problem via linear programming. Finally, we explore some connections between the sign uncertainty principle on the sphere and spherical designs.

Key words and phrases: Dini series, Fourier series, Fourier transform, Gegenbauer polynomials, Hamming cube, Hankel transform, Hilbert transform, Jacobi polynomials, linear programming, sphere packing, spherical design, spherical harmonics, uncertainty principle.

#### 1 Introduction

The uncertainty principle, discovered by W. Heisenberg in 1927, is one of the cornerstones of quantum mechanics. It can be expressed via Heisenberg’s inequality:

∥f∥4L2(R) 16π2

(x−a)2|f(x)|2dxˆ ∞ −∞

ˆ ∞

(ξ −b)2| f(ξ)|2dξ ⩾

inf

,

a,b∈R

−∞

*Supported by the Deutsche Forschungsgemeinschaft through the Collaborative Research Center 1060. †Supported by the EPSRC New Investigator Award “Sharp Fourier Restriction Theory”, grant no. EP/T001364/1. ‡Supported by the Deutscher Akademischer Austauschdienst.

© 2023 Felipe Gon¸calves, Diogo Oliveira e Silva, and Jo˜ao P. G. Ramos cb Licensed under a Creative Commons Attribution License (CC-BY) DOI: 10.19086/da.84266

where f denotes the Fourier transform of f. This estimate reflects the fact that the Fourier transform of a highly localized function must necessarily be widely dispersed in frequency space. Six years later, G. H. Hardy developed a more refined theory in this respect, and in particular established the following result: If there exist a,b > 0, such that the estimates f(x) = O(e−aπx2), f(ξ) = O(e−bπξ2) hold, then f ≡ 0 whenever ab > 1, and f must coincide with a polynomial multiple of the Gaussian function e−aπx2 if ab = 1. Thus the uncertainty inequalities of Heisenberg and Hardy respectively explore, in a quantitative way, the notions of concentration around the origin and decay at infinity; see [16] for further details.

In 2010, motivated by applications to number theory, Bourgain, Clozel & Kahane [5] investigated an analogue of the uncertainty principle, where the notions of concentration and decay are replaced by that of nonnegativity. To describe it precisely, consider the following setting. Given d ⩾ 1, a function f : Rd → R is said to be eventually nonnegative if f(x) ⩾ 0 for all sufficiently large |x|. In this case, consider the quantity

###### r(f) := inf{r > 0 : f(x) ⩾ 0 if |x| ⩾ r},

which corresponds to the radius of the last sign change of f. Normalize the Fourier transform,

f(ξ) = ˆ

Rd

f(x)e−2πi⟨x,ξ⟩dx, (1.1)

where ⟨·,·⟩ represents the usual inner product in Rd. Let A+(d) denote the set of functions f : Rd → R which are not identically zero and satisfy the following conditions:

- • f ∈ L1(Rd), f ∈ L1(Rd), and f is real-valued (i.e. f is even);
- • f is eventually nonnegative while f(0) ⩽ 0;
- • f is eventually nonnegative while f(0) ⩽ 0.


The product r(f)r( f) is invariant under rescaling, and becomes a natural quantity to consider. In this setting, the authors of [5] estimated the quantity

A+(d) := inf

f∈A+(d)\{0}

r(f)r( f). (1.2)

In particular, it is shown in [5, Théorème 3.1] that A+(d) is bounded from below, and that in fact it grows linearly with the square root of the dimension.

Very recently, Cohn & Gonçalves [9] discovered a complementary uncertainty principle which is connected with the linear programming bounds of Cohn & Elkies [8] for the sphere packing problem. To describe it precisely, let A−(d) denote the set of functions f : Rd → R which satisfy the following conditions:

- • f ∈ L1(Rd), f ∈ L1(Rd), and f is real-valued (i.e. f is even);
- • f is eventually nonnegative while f(0) ⩽ 0;


- • − f is eventually nonnegative while f(0) ⩾ 0.


In a similar spirit to [5], the authors of [9] showed that the quantity

A−(d) := inf

r(f)r(− f) (1.3)

f∈A−(d)\{0}

is bounded from below, and that in fact it grows linearly with √d. We shall refer to the boundedness of the quantities defined in (1.2), (1.3) as the ±1 uncertainty principles; see §1.1 below (in particular, the statement of Theorem 1.8) for further information. Our first main result consists in the following generalization of the ±1 uncertainty principles.

- Theorem 1.1 (Operator Sign Uncertainty Principle). Let X,Y be two arbitrary measure spaces, equipped with positive measures µ,ν, respectively. Let F ⊆ L1(X,µ)×L1(Y,ν) be a given family of pairs of functions. Assume that there exist real numbers p,q > 1 and a,b,c > 0, such that, for every (f,g) ∈ F,


- • ∥g∥L∞(Y,ν) ⩽ a∥f∥L1(X,µ);
- • ∥g∥Lq(Y,ν) ⩽ b∥f∥Lp(X,µ);
- • ∥f∥Lp(X,µ) ⩽ c∥g∥Lq(Y,ν);


Y gdν ⩽ 0. Then, for every nonzero (f,g) ∈ F, the following inequality holds: µ({x ∈ X : f(x) < 0})

X f dµ ⩽ 0,

•

´

´

1

1

q ⩾ a−1b−

p′ ν({y ∈ Y : g(y) < 0})

q′

q (2c)−q′, (1.4)

where p′ = p/(p−1) denotes the exponent conjugate to p, and similarly for q′.

The designation Operator Sign Uncertainty Principle derives from the fact that the family F is usually defined in terms of a given invertible operator T : Lp(X,µ) → Lq(Y,ν), i.e., it is often the case that F = {(f,T(f)) : f ∈ S}, for some S ⊆ Lp(X,µ). For instance, if for1 s ∈ {+,−} we let

Fs = {(f,s f) : f,s f ∈ L1(Rd) and both eventually nonnegative},

then the hypotheses of Theorem 1.1 are satisfied with p = q = 2 and a = b = c = 1. Since f(x),s f(ξ) ⩾ 0 for |x| ⩾ r(f),|ξ| ⩾ r(s f), respectively, it follows that

1 16

###### ⩽ |{x ∈ Rd : f(x) < 0}||{ξ ∈ Rd : s f(ξ) < 0}| ⩽ |Bd1|2r(f)dr(s f)d. (1.5)

1Henceforth we shall use the letter s to denote a sign from {+,−} and, by a slight but convenient abuse of notation, we will sometimes identify the signs {+,−} with the integers {+1,−1}.

Here, |E| represents the Lebesgue measure of a given set E ⊆ Rd, and Bd1 ⊆ Rd denotes the unit ball centered at the origin. In turn, estimate (1.5) immediately implies the aforementioned ±1 uncertainty principles of Bourgain, Clozel & Kahane and Cohn & Gonçalves.

Theorem 1.1 opens the door to a variety of novel sign uncertainty principles of interest, as evidenced by the many examples explored in §2, §3, §4 below, which we shall introduce as further main results of the present article. For instance, in §2 we establish a sign uncertainty principle for Fourier series. In §3, we describe some discrete sign uncertainty principles, which in the limit seem to converge back to the continuous ±1 uncertainty principles. In §4, we discuss sign uncertainty principles for certain convolution operators on spaces of bandlimited functions, including the Hilbert transform. These connections are entirely new, and can potentially find many applications in several different branches of mathematics.

Motivation for our second main result comes from letting Y = := {0,1,2,3,...} in Theorem 1.1, and taking F to be the family of pairs (f,s f), for some chosen sign s ∈ {+,−}, where f : → R is the coefficient sequence obtained by expanding f in some orthonormal basis. We shall derive a result that applies to a wide class of metric measure spaces, which we proceed to describe. Let X = (X,d,λ) be a metric measure space, with a distance function d : X ×X → [0,∞), and a probability measure λ. Further consider the space L2(X,λ) of square-integrable, real-valued functions f : X → R, which we will simply denote by L2(X) if no confusion arises. Given x ∈ X and r > 0, let B(x,r) := {y ∈ X : d(x,y) ⩽ r}.

- Definition 1.2 (Admissible space). The space (X,d,λ) is admissible if there exists an orthonormal basis {ϕn : X → R}n∈ of L2(X) and a fixed point2 0 ∈ X, such that ϕ0 ≡ 1, and, for every n ∈ ,

ϕn(0) := lim

r→0+

1 λ(B(0,r))

ˆ

B(0,r)

ϕn dλ = ∥ϕn∥L∞(X) < ∞. (1.6)

- Definition 1.3 (The As(X)-cone). Let s ∈ {+,−}. Let (X,d,λ) be an admissible space, for which {ϕn}n∈ is an orthonormal basis of L2(X) satisfying (1.6) for some 0 ∈ X. Then As(X) consists of all square-integrable functions f : X → R, such that:


- • If f = ∑∞n=0 f(n)ϕn then ∞

∑

n=0

| f(n)|∥ϕn∥L∞(X) < ∞; (1.7)

- • f(0) ⩽ 0;
- • {s f(n)}n∈ is eventually nonnegative while sf(0) ⩽ 0.


X fϕndλ. Note that As(X) ⊆ L1(X) since L2(X) ⊆ L1(X). From (1.7), it also follows that f ∈ ℓ1( ) if f ∈ As(X), simply because ∥ϕn∥L∞(X) ⩾ ∥ϕn∥L2(X) = 1. Since the series ∑∞n=0 f(n)ϕn converges absolutely and uniformly, the function f would coincide λ-almost everywhere with a continuous function if each ϕn were continuous. While this is the case for most of our applications, the latter

Here f(n) = ⟨f,ϕn⟩L2(X) =

´

2It may be useful to think of 0 as the origin of X with respect to the basis {ϕn}n∈ .

continuity property is not strictly necessary to make sense of the value of a given f ∈ As(X) at 0. Indeed, in the current setting, one can easily show that 0 is a Lebesgue point of f, and invoke (1.7) to define f(0) as follows:

∞

1 λ(B(0,r))

ˆ

### ∑

f dλ =

###### f(n)ϕn(o)

f(0) := lim

r→0+

B(0,r)

n=0

Given r1,r2 ∈ [0,∞), we write r1 ∼ r2 if λ(B(o,r1)) = λ(B(o,r2)), or equivalently if B(o,r1) = B(o,r2) up to λ-null sets. One easily checks that ∼ defines an equivalence relation on [0,∞), and that each equivalence class is an interval which contains its infimum. Let R := {infI : I ∈ [0,∞)/ ∼}. Given f ∈ As(X), we define3 the following quantities:

r(f;X) := inf{r ∈ R : f(x) ⩾ 0 for λ-a.e. x ∈ X such that d(x,o) ⩾ r}; (1.8) k(s f) := min{k ⩾ 1 : s f(n) ⩾ 0 if n ⩾ k}. (1.9)

In fact, throughout the paper, given a sequence {an}Nn=0 ⊂ R with N < ∞ or N = ∞, we will more generally write

ka = k(a) = min{k ⩾ 0 : an ⩾ 0 if n ⩾ k}.

Note that r(f;X) can be +∞, or equal to the smallest r0 > 0 for which X ⊆ B(o,r0). On the other hand, if f is nonzero, then r(f;X) > 0 as long as λ({o}) = 0, for otherwise f ⩾ 0 (λ-a.e.), which contradicts f(0) ⩽ 0. Moreover, s f(n) cannot be nonnegative for all n ⩾ 0, for otherwise

0 ⩽

∞

### ∑

###### s f(n)ϕn(o) = sf(o) ⩽ 0,

n=0

and therefore f(n) = 0, for all n ⩾ 0, which is absurd because f is nonzero. We also have that k(− f) ⩾ 2, for otherwise

∞

### ∑

f(x)− f(0) =

n=1

∞

### ∑

f(n)ϕn(x) ⩾

n=1

###### f(n)ϕn(o) = f(o)− f(0),

whence f(x) ⩾ f(o) ⩾ 0 for all x ∈ X, which is absurd because f(0) ⩽ 0 and f is nonzero. On the other hand, it might be the case that k( f) = 1 (e.g. take f ≡ −1); but if f(0) = 0, then it is easy to see that k( f) ⩾ 2 as well.

We are now ready to state our second main result.

- Theorem 1.4 (Orthonormal Sign Uncertainty Principle). Let s ∈ {+,−}. Let (X,d,λ) be an admissible space, for which {ϕn}n∈ is an orthonormal basis of L2(X) satisfying (1.6) for some 0 ∈ X. Then, for every


3Definition (1.8) turns out to be more adequate than merely taking the infimum over all r ⩾ 0. Indeed, let X = , with d(n,m) := |n − m| and counting measure λ. Then R = , and r(f;X) coincides with the unique integer m ⩾ 1, for which f(m−1) < 0 but f(n) ⩾ 0 for all n ⩾ m.

nonzero f ∈ As(X), the following inequality holds:

λ({x∈X : f(x)<0}) ∑

n⩾0: s f(n)<0

∥ϕn∥2L∞(X) ⩾

1 16

. (1.10)

In particular, it holds that

k(s f)−1

λ(B(o,r(f;X)))

n=0

### ∑

∥ϕn∥2L∞(X) ⩾

1 16

. (1.11)

Theorems 1.1 and 1.4 are not entirely unrelated: for instance, the latter easily follows from the former

(with a lower bound which possibly differs from 161 ) in the special case when the orthonormal basis satisfies supn∈ ∥ϕn∥L∞(X) < ∞. If the space L2(X) is finite dimensional, then a corresponding version of Theorem 1.4 holds; we omit the obvious statement, but note that the proof is exactly the same. Consequences of Theorem

- 1.4 to a variety of settings will be explored in §2.4 In particular, we establish a sign uncertainty principle for spherical harmonics in §2.1. It turns out that, in the case of the unit sphere Sd−1 ⊆ Rd, the zero set of


a minimizer to the restricted problem on a finite dimensional subspace V = span{ϕn}Nn=0 exhibits natural geometric structure. In particular, we shall see how to relate this zero set to the set of cosine distances of certain spherical designs.

###### 1.1 Further Background

We briefly expand on the history of previous work which inspired the present paper, and its connections to our main results. The initial lower and upper bounds for A+(d) of Bourgain, Clozel & Kahane [5] were subsequently sharpened by Gonçalves, Oliveira e Silva & Steinerberger [19]. Cohn & Gonçalves [9] then discovered that the sign uncertainty principle is connected with the linear programming bounds for the sphere packing problem, and exploited this connection to prove that A+(12) = √2. Crucially, they realized the applicability of the powerful machinery devised by Viazovska [33] in her solution to the eight-dimensional sphere packing problem to construct eigenfunctions of the Fourier transform via certain Laplace transforms of modular forms. To understand this connection in greater depth, we shall briefly discuss the upper bounds on sphere packings via linear programming from the groundbreaking work of Cohn & Elkies [8]. Let ALP(d) denote the set of functions f : Rd → R, which satisfy the following conditions:

- • f ∈ L1(Rd), f ∈ L1(Rd), and f is real-valued (i.e. f is even);
- • −f is eventually nonnegative while f(0) = 1;
- • f is nonnegative and f(0) = 1.


4For most applications, we will limit ourselves to the formulation given by (1.11), see Theorems 2.3, 2.13, 2.21, 4.2, 4.3 below, but the reader should bear in mind that the more general formulation given by (1.10) likewise holds in all of these results.

In [8, Theorem 3.2] it is shown that, given any sphere packing P ⊆ Rd of congruent balls, its upper density δ¯(P) satifies

###### δ¯(P) ⩽ r(−f)d|Bd1

|, (1.12) for any f ∈ ALP(d). Therefore the quantity

2

ALP(d) := inf

r(−f)

f∈ALP(d)

becomes of interest. High precision numerical data indicated that the upper bound (1.12) agrees with the packing density of the hexagonal, E8, and Leech lattices in dimensions 2,8, and 24, respectively. In a celebrated breakthrough, Viazovska [33] found the magical function f realizing equality in (1.12) when d = 8, thereby proving optimality of the E8-lattice packing and showing that ALP(8) = √2. Shortly thereafter, Cohn, Kumar, Miller, Radchenko & Viazovska [11] used similar methods to prove the optimality of the Leech lattice when d = 24, thereby showing that ALP(24) = 2. An elementary geometric argument reveals that the hexagonal packing is optimal if d = 2 (see e.g. [23]), but the corresponding magical function is yet to be discovered. Cohn & Gonçalves [9] later noticed that the −1 uncertainty principle described in the previous section underpins the construction in dimensions d ∈ {8,24}. The connection is simple to describe: If f ∈ ALP(d), then f − f ∈ A−(d) and r( f − f) ⩽ r(−f), and therefore A−(d) ⩽ ALP(d). In [9], the authors performed extensive numerical calculations, producing compelling evidence towards the following conjecture,5 which if proved would establish a precise mathematical link between the sign uncertainty principle and the sphere packing problem, and clarify the constructions in [11, 33].

- Conjecture 1.5. ALP(d) = A−(d), for every d ⩾ 1. Indeed, one can extract the −1 eigenfunctions from [11, 33], and then use Poisson-type summation

formulae for the E8 and Leech lattices (in the same way as the Eisenstein series E6 was used to prove optimality in [9]) in order to conclude that ALP(8) = A−(8) = √2 and ALP(24) = A−(24) = 2. Cohn & Elkies [8] further showed that ALP(1) = 1, and that the function f(x) = (1−|x|)+ is optimal; from their proof, one can easily derive that A−(1) = 1, and that a corresponding minimizer is given by the function x  → ( f − f)(x) = sin

2(πx)

(πx)2 −(1−|x|)+. Together with A+(12) = √2 (recall [9]), these constitute a complete list of dimensions d for which A±(d),ALP(d) are known. From the possible equality in (1.12) for the hexagonal packing when d = 2, Cohn & Elkies [8] further conjectured that ALP(2) = (43)14. Therefore one should also expect that A−(2) = (43)14.

- Conjecture 1.6. ALP(2) = A−(2) = (34)14. As a consequence of our new sign uncertainty principle for the discrete Fourier transform (see §3.1, §6.1

below), we now have numerical evidence pointing towards following conjecture.

- Conjecture 1.7. A+(1) < 0.555. Moreover, any minimizer for A+(1) vanishes identically in a sequence of nonempty intervals after the last sign change (see Figure 2).


5Conjecture 1.5 is equivalent to [8, Conjecture 7.2]; the equivalence was proven in [9].

To the best of our knowledge, these are the only dimensions for which even a guess of the actual solution exists, all other dimensions remaining for the most part entirely mysterious. We believe that solving Conjectures 1.6 or 1.7 would require brand new techniques, which could potentially be applied to other dimensions, and open windows of possibilities. Even though the exact answer is not known, or even conjectured, in any other dimension d ∈/ {1,2,8,12,24}, it has been established that radial minimizers exist in all dimensions, and that such minimizers must necessarily vanish at infinitely many radii greater than A+(d). This was shown in [19, Theorem 4] for the +1 uncertainty principle, and the technique was later [9] adapted to handle the −1 uncertainty principle. The following result summarizes the state-of-the-art knowledge of minimizers for the ±1 uncertainty principles.

- Theorem 1.8 ([5, 9, 19]). Let d ⩾ 1. Then the following two-sided inequalities hold:


1 √2πe

A+(d) √d

1 √2π

⩽

⩽

+od(1); (1.13) 1 √2πe

A−(d) √d

⩽

⩽ 0.3194...+od(1). (1.14)

Moreover, for each s ∈ {+,−} and d ⩾ 1, there exists a radial function f ∈ As(d)\{0}, such that f = sf, f(0) = 0, r(f) = As(d). Any such function must vanish at infinitely many radii greater than As(d).

The number 0.3194... in (1.14) is derived from the classical upper bounds of Kabatiansky & Levenshtein [25] for the sphere packing problem. Indeed, the construction in [12] reveals how the same bound can be obtained via linear programming, whence ALP(d) ⩽ (0.3194...+od(1))

√d. The upper bound in (1.14) then follows from the aforementioned estimate A−(d) ⩽ ALP(d). In spite of the distinct upper bounds in

- (1.13), (1.14), it is conjectured in [9] (with strong numerical evidence) that there exists a constant c > 0,


for which A+(d) ∼ A−(d) ∼ c√d, as d → ∞. Moreover, there are reasons to believe that c might not be too far from 0.3194; indeed, recent numerical results in the framework of the modular bootstrap in

conformal field theory [7] suggest that c = π1. The structural statement in Theorem 1.8 (concerning the double roots of the minimizers) stem from a seemingly new observation concerning Hermite polynomials, which relates their pointwise values to linear flows on the torus Td, and extends to other families of orthogonal polynomials; see [20] for further applications of this idea. The proof of [19, Theorem 4] can easily be adapted to show that minimizers for ALP(d) exist, and must also have infinitely many double roots. Finally, some equivalent formulations of the ±1 uncertainty principles, and mass concentration phenomena exhibited by the corresponding minimizing sequences, were the subject of very recent explorations in [18]. Further related recent results can be found in [6, 21].

###### 1.2 Outline

In §2, we establish sign uncertainty principles for spherical harmonics (§2.1), Jacobi polynomials (§2.2), Fourier series (§2.3), and Dini series (§2.4). In §3, we establish sign uncertainty principles for the discrete

Fourier transform (§3.1), the discrete Hankel transform (§3.2), and the Hamming cube (§3.3). In §4, we establish sign uncertainty principles for convolution kernels in bandlimited function spaces (§4.1), the Hilbert transform of bandlimited functions (§4.2), and the Hankel transform (§4.3). The main results are proved in §5. Finally, in §6, we present our numerical findings related to the discrete Fourier transform (§6.1), and the discrete Hankel transform (§6.2).

#### 2 Sign Uncertainty for Classical Orthogonal Systems

###### 2.1 Spherical Harmonics

Let Sd−1 = {ω ∈ Rd : |ω| = 1} denote the unit sphere, equipped with the geodesic distance dg : Sd−1×Sd−1 → [0,π], dg(ω,ν) := arccos(⟨ω,ν⟩), and normalized surface measure σ¯, induced from the ambient space Rd in the natural way and satisfying σ¯(Sd−1) = 1. The special orthogonal group SO(d) consists of all d ×d orthogonal matrices of unit determinant, and acts transitively on the unit sphere Sd−1. The vector space of spherical harmonics on Sd−1 of degree n, denoted Hnd, consists of restrictions to Sd−1 of real-valued harmonic polynomials on Rd which are homogeneous of degree n. The spaces Hnd are mutually orthogonal and span L2(Sd−1) = L2(Sd−1,σ¯),

∞

###### Hnd.

L2(Sd−1) =

n=0

Let hn := dim Hnd, and denote the north pole by η = (0,...,0,1) ∈ Sd−1.

- Definition 2.1 (Signed basis). An orthonormal basis {Yn,j ∈ Hnd : n ∈ , j = 1,...,hn} of L2(Sd−1) is signed if:


- • Yn,j(η) ⩾ 0, for every n ∈ , j = 1,2,...,hn;
- • Yn,j(η) > 0, for every j = 1,2,...,hn, provided n is sufficiently large.


A signed basis for L2(Sd−1) can be constructed as follows. Given a continuous function f : Sd−1 → R, let Z(f) := {ω ∈ Sd−1 : f(ω) = 0} denote its zero set. Start with an arbitrary basis Y = {Yn,j ∈ Hnd : n ∈ , j = 1,2,...,hn} of L2(Sd−1), and consider the corresponding zero set,

∞

hn

Z(Yn,j).

Z(Y) :=

j=1

n=0

Since σ¯(Z(Y)) = 0, we can find a rotation ρ ∈ SO(d) such that ρ(η) ∈/ Z(Y). Therefore there exists a sequence of signs {sn,j} ⊆ {+,−} , for which {sn,jYn,j ◦ρ : n ∈ , j = 1,2,...,hn} is a signed basis for L2(Sd−1).

Henceforth, we fix a signed orthonormal basis {Yn,j : n ∈ , j = 1,2,...,hn} of L2(Sd−1). Any real-

valued, square-integrable function f : Sd−1 → R can be expanded as follows:

∞

hn

### ∑

### ∑

f =

f(n, j)Yn,j, (2.1)

n=0

j=1

Sd−1 f(ω)Yn,j(ω)dσ¯(ω).

where f(n, j) =

´

- Definition 2.2 (The Bs(Sd−1)-cone). Let s ∈ {+,−}. Then Bs(Sd−1) consists of all continuous functions f : Sd−1 → R, such that:


- • f(0,1) ⩽ 0;
- • {s f(n, j) : n ∈ , j = 1,2,...,hn} is eventually nonnegative while sf(η) ⩽ 0. Given f ∈ Bs(Sd−1), set


θ(f) := inf{θ ∈ (0,π] : f(ω) ⩾ 0 if dg(ω,η) ⩾ θ}; k(s f) := min{k ⩾ 1 : s f(n, j) ⩾ 0 if n ⩾ k},

and define the quantity

(1−cos(θ(f)))21k(s f), (2.2)

Bs(Sd−1) := inf

f∈Bs(Sd−1)\{0}

which is estimated by our next result.

- Theorem 2.3. Let s ∈ {+,−} and d ⩾ 2. Then the following estimates hold:


2Γ(d+21)d−21 (4e121 )d−21(d2 −1)12

Bs(Sd−1) ⩾

, (2.3)

√2, and B−(Sd−1) ⩽ 2√2. (2.4)

B+(Sd−1) ⩽

Remark. Since (1−cosθ)12 = √2sin θ2 ≈ θ if 0 ⩽ θ ⩽ π, a similar uncertainty principle would be obtained if (1−cos(θ(f)))21 were replaced by θ(f) in (2.2). We made this choice with a view towards identity (2.5) below, which would otherwise be merely a two-sided inequality instead of an equality. Further note that by Stirling’s formula we have

2Γ(d+21)d−21 (4e121 )d−21(d2 −1)21

= e−1 +O(d−1logd),

###### √d.

which is in sharp contrast with the Euclidean (noncompact) case where As(d) ≈

The proof of Theorem 2.3 involves Gegenbauer polynomials, which are particular instances of Jacobi polynomials, discussed in §2.2 below. As with most results in this section, Theorem 2.3 ultimately boils down to a special case of a more general result from §2.2. More precisely, the proof of the lower bound (2.3)

proceeds in two steps. Firstly, via a zonal symmetrization procedure, we may assume the existence of an eventually nonnegative sequence of coefficients {an}n∈ , for which

∞

### ∑

anCnd/2−1(⟨ω,η⟩).

f(ω) =

n=0

Here, Cnd/2−1 denotes the Gegenbauer polynomial of degree n and order d2 −1; see (2.10) below. Secondly, the map g(x)  → g(⟨ω,η⟩) defines a bijection between the set Bs(I; d−3

2 , d−23) from Definition 2.12 below and the set of functions in Bs(Sd−1) which are invariant under rotations that fix the north pole. Consequently, the following identity holds:

Bs(Sd−1)2 = Bs [−1,1]; d−3

2 , d−23 , (2.5) where the right-hand side is defined in (2.13) below. Therefore Theorem 2.3 will ultimately follow from

- Theorem 2.13; see §5.3 for details.


Definition 2.4 (The class B0s(Sd−1)). Let s ∈ {+,−} and d ⩾ 2. Then B0s(Sd−1) consists of all functions f ∈ Bs(Sd−1) which are invariant under rotations that fix the north pole η, and satisfy f(η) = 0.

Further define the quantity

(1−cos(θ(f)))21k(s f). The following result is a direct consequence of (2.5) and Proposition 2.14 below. Proposition 2.5. Let s ∈ {+,−} and d ⩾ 2. Then B0s(Sd−1) = Bs(Sd−1).

B0s(Sd−1) := inf

f∈B0s(Sd−1)\{0}

For the remainder of this section, we investigate polynomials in B0s(Sd−1) which are optimal in the following sense.

- Definition 2.6 (s-optimal polynomial in B0s(Sd−1)). Let s ∈ {+,−} and d ⩾ 2. A polynomial f ∈ B0s(Sd−1) is locally s-optimal if there exists δ > 0, such that


(1−cos(θ(f)))12k(s f) < (1−cos(θ(h)))21k(s h),

for any polynomial h ∈ B0s(Sd−1) satisfying deg(h) ⩽ deg(f) and 0 < infc>0∥f − ch∥L∞(Sd−1) < δ. The polynomial f is said to be globally s-optimal if one can take δ = +∞.

###### 2.1.1 Connections with Spherical Designs

A fundamental tool employed in the solutions of the sphere packing problem in 8 and 24 dimensions [33, 11] and of the +1-uncertainty principle in 12 dimensions [9] is the Poisson summation formula associated with certain modular forms; recall the discussion in §1.1. Poisson summation is often used to extract sharp lower bounds, and to access information about the root location of the conjectural minimizer. On the sphere Sd−1,

the role of Poisson summation seems to be played by spherical designs; see [1] for an excellent introduction to this topic.

Let us introduce some terminology. A finite subset Ω ⊆ Sd−1 is called a spherical t-design if, for every polynomial f : Sd−1 → R of degree at most t,

1

ˆ

#Ω ∑

f(ω)dσ¯(ω) =

###### f(ω).

Sd−1

ω∈Ω

We say that Ω has m distances if the set of cosine distances,

α(Ω) := {⟨ω,ω′⟩ : ω,ω′ ∈ Ω, ω ̸= ω′},

is such that #α(Ω) = m; in this case, we write α(Ω) = {αm < αm−1 < ... < α1}. Note that necessarily t ⩽ 2m, for otherwise the nonnegative, nonzero function

f(ω) = (1−⟨ω,ω1⟩)

m

### ∏

(⟨ω,ω1⟩−αj)2, (ω1 ∈ Ω)

j=1

would have zero average on Sd−1. Moreover, if t = 2m, then Ω cannot contain a pair of antipodal points, for otherwise αm = −1, and the function

m−1

### ∏

g(ω) = (1−⟨ω,ω1⟩2)

(⟨ω,ω1⟩−αj)2

j=1

would have zero average on Sd−1, which is again impossible. Delsarte, Goethals & Seidel [14] showed that, if Ω ⊆ Sd−1 is a spherical t-design, then

d +⌊t/2⌋−1 ⌊t/2⌋

d +⌈t/2⌉−2 ⌈t/2⌉−1

#Ω ⩾

. (2.6)

+

A spherical t-design Ω ⊆ Sd−1 is said to be tight if equality holds in (2.6). It is also shown in [14] that, if Ω is a spherical t-design, then Ω is tight if and only if #α(Ω) = ⌈t/2⌉ and Ω is antipodal if t is odd.

The regular (t +1)-gon is a tight t-design on S1 ⊆ R2, for any t ⩾ 1. By contrast, tight t-designs on Sd−1 with d ⩾ 3 are rare. In particular, Bannai & Damerell [2, 3] established the following: if d ⩾ 3, then tight t-spherical designs can only exist when t ∈ {1,2,3,4,5,7,11}. Moreover, modulo isometries: if t = 1, then Ω consists of a pair of antipodal points; if t = 2, then Ω is the regular simplex with d +1 vertices; if t = 3, then Ω = {±ej}dj=1 is the cross-polytope with 2d vertices; and if t = 11, then d = 24 and Ω is the set of 196560 minimal vectors of the Leech Lattice. The complete classification of spherical t-designs is open for t ∈ {4,5,7}, although several examples are known; see [1, p. 1401] and [10, Table 1].

- Definition 2.7 (s-optimal spherical design). Let s ∈ {+,−} and d ⩾ 2. Let Ω ⊆ Sd−1 be a tight spherical t-design with α(Ω) = {αm < αm−1 < ... < α1}, where m = ⌈t/2⌉. For m ⩾ 2, let a = 1 if αm = −1, a = 2 if


αm > −1, and define the polynomial

P(ω) := (x−1)(x−αm)a(x−α1)

m−1

### ∏

(x−αj)2, where x = ⟨ω,η⟩. (2.7)

j=2

If m = 1, set P(ω) := (x−1)(x−α1). We say that Ω is locally (resp. globally) s-optimal if the polynomial P is locally (resp. globally) s-optimal in B0s(Sd−1).

Since every tight spherical design generates a quadrature rule for the measure associated to Gegenbauer polynomials (see §2.2.2), the zonal symmetrization argument from the proof of Theorem 2.3 leads to the following result.

Proposition 2.8. Let s ∈ {+,−} and d ⩾ 2. Let Ω ⊆ Sd−1 be a spherical t-design with α(Ω) = {αm < αm−1 < ... < α1}. Let f ∈ Bs(Sd−1) \ {0} be a polynomial satisfying deg(f) ⩽ t, and further assume f(η) = 0 if s = +1. Then θ(f) ⩾ arccos(α1). Moreover, if θ(f) = arccos(α1) and f is invariant under rotations that fix the north pole η, then f coincides with a positive multiple of the polynomial P defined in

- (2.7).


The discussion preceding Corollary 2.17 below implies that every tight spherical t-design is in fact locally s-optimal. Moreover, in light of Proposition 2.8, a tight spherical t-design is globally s-optimal if the corresponding polynomial P defined via (2.7) satisfies6 k(s P) = 2. In the following examples, given a certain set of nodes X = (xm,xm−1,...,x0), W = (wm,wm−1,...,w0) will be such that ∑m wj

m j=0

is the set of weights of the quadrature rule associated with the nodes in X.

i=0 wi

- Example 2.9 (Simplex). The regular simplex on Sd−1 is a tight spherical 2-design with d +1 vertices and one cosine distance, −d1. It induces a quadrature rule of degree t = 2 for the Gegenbauer measure wν−1

2,ν−12 (see (2.8) below), ν = d2 −1, with X = 2ν −+12,1 and W = (2ν +2,1). One easily checks that this quadrature rule integrates all polynomials of degree at most 2 exactly, for all ν ⩾ 0. Moreover, letting7

P(x) = (x−1) x+

- 1

- 2ν +2


= −(2ν +1)

4ν +4

Gν1(x)+

- 1

- 2ν +2


Gν2(x),

we have that k( P) = 2. Hence P is a globally +1-optimal polynomial in B0+(I;ν − 21,ν − 12), and the regular simplex is a globally +1-optimal tight 2-design on Sd−1.

- Example 2.10 (Cross-polytope). The cross-polytope {±ej}dj=1 on Sd−1 is a tight spherical 3-design with


- 2d vertices and two cosine distances, {−1,0}. It induces a quadrature rule of degree t = 3 for wν−1


, ν = d2 −1, with X = (−1,0,1) and W = (1,4ν +2,1). One easily checks that this quadrature rule integrates

2,ν−12

6Recall that k(s P) ⩾ 2 since P ∈ B0s(Sd−1). 7The modified Gegenbauer polynomials are defined as Gνn(x) := ν−1Cnν(x) for ν ⩾ 0, with the understanding that G0n(x) =

limν→0+ ν−1Cnν(x).

all polynomials of degree at most 3 exactly, for all ν ⩾ 0. Moreover, letting

P(x) = (x2 −1)x = −(2ν +1) 4(ν +2)

3 4(ν +1)(ν +2)

Gν1(x)+

Gν3(x),

we have that k( P) = 2. Hence P is a globally +1-optimal polynomial in B0+(I;ν − 21,ν − 12), and the cross-polytope is a globally +1-optimal tight 3-design on Sd−1.

We summarize the preceding discussion in the following result.

- Theorem 2.11. Let d ⩾ 2. Every tight spherical t-design is locally s-optimal, for any s ∈ {+,−}. Furthermore:


- • The regular simplex on Sd−1 with d +1 vertices is a globally +1-optimal tight 2-design;
- • The cross-polytope on Sd−1 with 2d vertices is a globally +1-optimal tight 3-design.


We have not been able to find any globally −1-optimal design, nor any further globally +1-optimal designs.

###### 2.2 Jacobi Polynomials

Let {Pn(α,β)}n∈ denote the Jacobi polynomials with parameters α,β > −1. These are defined in [31, Ch. IV] as the orthogonal polynomials on the interval I := [−1,1], associated with the measure

wα,β(x)dx = cα,β(1−x)α(1+x)β I(x)dx, (2.8)

and normalized in such a way that

If α = β = ν − 21, then

Pn(α,β)(1) =

n+α n

. (2.9)

n+ν n n+2ν−1 n

- 1

- 2,ν−


- 1

- 2)


P(ν−

Cnν(x), (2.10)

n (x) =

where Cnν is the Gegenbauer polynomial of degree n and order ν. The constant cα,β in (2.8) is chosen in such a way that wα,β(x)dx defines a probability measure,

α,β = ˆ 1 −1

Γ(α +1)Γ(β +1) Γ(α +β +2)

(1−x)α(1+x)β dx = 2α+β+1

c−1

. (2.11)

Rodrigues’ formula [31, (4.3.1)] states that

(−1)n 2nn!

(1−x)α(1+x)βPn(α,β)(x) =

d dx

n

###### [(1−x)n+α(1+x)n+β],

from which it can be deduced that

h(nα,β) := ˆ 1 −1

Pn(α,β)(x)2wα,β(x)dx

Γ(α +β +2)Γ(n+α +1)Γ(n+β +1) Γ(α +1)Γ(β +1)Γ(n+1)Γ(n+α +β +1)

1 2n+α +β +1

=

.

Here, (2n+α +β +1)Γ(n+α +β +1) has to be replaced by Γ(n+α +β +2) if n = 0; see [31, (4.3.3)]. Setting

pn(α,β) := (hn(α,β))−12Pn(α,β),

we then have that {p(nα,β)}n∈ constitutes an orthonormal basis of L2(I) = L2(I,wα,β). Any real-valued function f : [−1,1] → R in L2(I) can be decomposed as

∞

f(n)p(nα,β)(x), (2.12)

### ∑

f(x) =

n=0

where f(n) denotes the n-th coefficient of f with respect to the orthonormal basis {pn(α,β)}n∈ .

- Definition 2.12 (The Bs(I;α,β)-cone). Let s ∈ {+,−}, and let α ⩾ β ⩾ −12. Then Bs(I;α,β) consists of all continuous functions f : [−1,1] → R, such that:


- • f(0) ⩽ 0;
- • {s f(n)}n∈ is eventually nonnegative while sf(1) ⩽ 0.


The proof of Theorem 2.13 below will reveal that the space8 (I,d,wα,β(x)dx) is admissible in the sense of Definition 1.2, with respect to the basis {pn(α,β)}n∈ and 0 = 1. Moreover, Bs(I;α,β) = As(I) (recall

- Definition 1.3). Specializing (1.8), (1.9) to the present case, we are led to consider


###### r(f;I) = inf{r ∈ (0,2] : f(x) ⩾ 0 if x ∈ [−1,1−r)};

k(s f) = min{k ⩾ 1 : s f(n) ⩾ 0 if n ⩾ k}, together with the quantity

r(f;I)k(s f)2, (2.13)

Bs(I;α,β) := inf

f∈Bs(I;α,β)\{0}

which is estimated by our next result.

Theorem 2.13. Let s ∈ {+,−} and α ⩾ β ⩾ −21. Then the following estimate holds:

2Γ(α +2)α+21 (4e121 )α+21(α +β +2)(α +2)

Bs(I;α,β) ⩾

. (2.14)

8Here, d : I ×I → [0,2] denotes the restriction of the usual Euclidean distance.

Moreover, B+(I;α,β) ⩽ 2 and B−(I;α,β) ⩽ 8. Remark. By Stirling’s formula, the right-hand side of (2.14) satisfies

2Γ(α +2)α+21 (4e121 )α+21(α +β +2)(α +2)

=

2e−2 1+ αβ

1+O

log(α +2) α +1

.

The upper bounds B+(I;α,β) ⩽ 2 and B−(I;α,β) ⩽ 8 are produced by the polynomials

P1(α,β)(x) P1(α,β)(1)

f+(x) = −1+

P1(α,β)(x) P1(α,β)(1)

and f−(x) = −

P2(α,β)(x) P2(α,β)(1)

, (2.15)

+

respectively. We have performed extensive numerical searches in order to find polynomials up to degree 30 which lead to better upper bounds, but were unable to find any. Nevertheless, we would be extremely surprised if the polynomials f± from (2.15) turned out to be extremal.

We are interested in the following restricted optimum:

B0s (I;α,β) := inf r(f;I)k(s f)2 : f ∈ Bs(I;α,β)\{0}, f(1) = 0 ,

which according to the next result coincides with (2.13).

Proposition 2.14. Let s ∈ {+,−}, α ⩾ β ⩾ −12, and f ∈ Bs(I;α,β)\{0}. Then there exists a polynomial g such that f +g ∈ Bs(I;α,β)\{0}, (f +g)(1) = 0, k(s f +s g) = k(s f), and r(f +g;I) < r(f;I). In particular, B0s (I;α,β) = Bs(I;α,β).

###### 2.2.1 Connections with Quadrature

A finite set {(xj,λj)}mj=0 with −1 ⩽ xm < xm−1 < ... < x0 ⩽ 1 and λj > 0 for j = 0,...,m is said to generate a quadrature rule of degree t for the measure wα,β if, for every polynomial f of degree at most t,

ˆ 1

f(x)wα,β(x)dx =

−1

m

### ∑

λj f(xj).

j=0

X := {xj}mj=0 is the set of nodes and Λ := {λj}mj=0 is the set of weights. Note that necessarily t ⩽ 2m+1, for otherwise the integral of the polynomial ∏mj=0(x−xj)2 against the measure wα,β would be zero, which is absurd. Similarly, if xm = −1 < −x0 or xm > −1 = −x0, then t ⩽ 2m, and if x0 = −xm = 1, then t ⩽ 2m−1.

Quadrature rules where t is as large as possible can be completely classified via the Gauss–Jacobi quadrature [31, Theorem 3.4.1], with nodes given by the zeros of Jacobi polynomials, and weights given by the Christoffel numbers; see [14]. A quick review follows.

- • Assume that −1 < xm < x0 < 1 and t = 2m + 1. Then q(x) = ∏mj=0(x − xj) is orthogonal to all


- polynomials of degree ⩽ m with respect to the measure wα,β, and therefore q = c p(mα+,β1), for some c > 0.
- • Assume that −1 = xm < x0 < 1 (resp. −1 < xm < x0 = 1) and t = 2m. Then q(x) = ∏mj=−01(x−xj) (resp. q(x) = ∏mj=1(x−xj)) is orthogonal to all polynomials of degree ⩽ m−1 with respect to wα,β+1 (resp. wα+1,β), and therefore q = c pm(α,β+1) (resp. q = c p(mα+1,β)), for some c > 0.
- • Assume that −1 = xm < x0 = 1 and t = 2m − 1. Then q(x) = ∏mj=−11(x − xj) is orthogonal to all


polynomials of degree ⩽ m−2 with respect to wα+1,β+1, and therefore q = c p(mα−+11,β+1), for some c > 0.

- Definition 2.15 (s-optimal polynomial in B0s(I;α,β)). Let s ∈ {+,−} and α ⩾ β ⩾ −21. A polynomial f ∈ B0s(I;α,β) is locally s-optimal if there exists δ > 0, such that


r(f;I)k(s f)2 < r(h;I)k(s h)2,

for any polynomial h ∈ B0s(I;α,β) satisfying deg(h) ⩽ deg(f) and 0 < infc>0∥f − ch∥L∞(I) < δ. The polynomial f is said to be globally s-optimal if one can take δ = +∞.

In what follows, we let x1(α,m,β) denote the largest zero of the polynomial p(mα,β).

- Theorem 2.16. Let α ⩾ β ⩾ −21. Define the polynomials


p(mα+1,β)(x)2 x1(α,m+1,β) −x

, (m ⩾ 1);

###### P(x) := (1−x)

p(mα−+11,β+1)(x)2 x1(α,m+−11,β+1) −x

###### Q(x) := (1−x2)

, (m ⩾ 2).

Then P and Q are locally s-optimal in B0s(I;α,β), for any s ∈ {+,−}.

(2.16)

###### 2.2.2 Quadrature and Spherical Designs

Aiming to establish a connection between spherical designs and the sign uncertainty principle for spherical harmonics, we now restrict attention to Gegenbauer polynomials. For notational simplicity, set µν := wν−1

. Let Ω ⊆ Sd−1 be a tight spherical t-design with set of cosine distances {αm < αm−1 < ... < α1} ⊆ [−1,1), where t = 2m if αm > −1, and t = 2m−1 if αm = −1. Define

2,ν−21

ℓj := #{(ω,ω′) ∈ Ω2 : ⟨ω,ω′⟩ = αj},

and further set ℓ0 = 1, x0 = 1, and {xj = αj}mj=1. We note that {(xj, #ℓΩj2)}mj=0 generates a quadrature rule of degree t for µν. Indeed, if f is a polynomial of degree at most t, and σ¯ denotes the normalized surface

measure on Sd−1, then ˆ

(Sd−1)2

1

#Ω2 ∑

f(⟨ζ,ν⟩)dσ¯(ζ)dσ¯(ν) =

ω,ω′∈Ω

m

ℓj #Ω2

### ∑

f(⟨ω,ω′⟩) =

f(xj).

j=0

In particular, the sequence {αj}mj=1 \ {−1} coincide with the zeros of the polynomial p(mν+1/2,ν−1/2) or p(mν−+11/2,ν+1/2), depending on whether αm > −1 or αm = −1, respectively. On the other hand, if η ∈ Sd−1 denotes the north pole as usual, then

ˆ

f(⟨ζ,ν⟩)dσ¯(ζ)dσ¯(ν) = ˆ

(Sd−1)2

Sd−1

f(⟨ζ,η⟩)dσ¯(ζ) = ˆ 1 −1

f(x)µν(x)dx.

Moreover, it is straightforward to verify that the map f(x)  → F(ω) := f(⟨ω,η⟩) defines a bijection between the sets B0s(I;ν − 12,ν − 12) and B0s(Sd−1), and that k(s f) = k(s F) and r(f;I) = 1−cos(θ(F)). With these considerations in place, one easily checks that Theorem 2.16 specializes to the following result.

- Corollary 2.17. Let d ⩾ 2, and set α = β = d−23 in Theorem 2.16. Then, for any s ∈ {+,−}, the polynomials f := P(⟨·,η⟩) and g := Q(⟨·,η⟩) (where P,Q were defined in (2.16)) are locally s-optimal in B0s(Sd−1) .


###### 2.3 Fourier Series

Given d ⩾ 1, the d-torus Td = Rd/Zd can be defined as the set of equivalence classes under the equivalence relation x ∼ y if x−y ∈ Zd. Equivalently, we will think of Td as the following subset of Cd:

Td = {(e2πix1,...,e2πixd) ∈ Cd : (x1,...,xd) ∈ [−12, 12]d} Functions on Td are in one-to-one correspondence with functions on Rd which are 1-periodic in each coordinate. The Haar probability measure on Td, denoted λ, is simply the restriction of d-dimensional Lebesgue measure to the unit cube [−12, 12]d. Translation invariance of the Lebesgue measure, and periodicity of functions on Td, imply that ˆ

f dλ = ˆ

f(x)dx.

[−12,12]d

Td

Given a real-valued function f ∈ L1(Td) = L1(Td,λ), and m ∈ Zd, define the corresponding Fourier coefficient

f(m) = ˆ

f(x)e−2πi⟨x,m⟩dλ(x).

Td

An immediate consequence is the estimate ∥ f∥ℓ∞(Zd) ⩽ ∥f∥L1(Td). If f ∈ L1(Td) and f ∈ ℓ1(Zd), then Fourier inversion applies, and implies that, for λ-almost every x ∈ Td,

f(x)= ∑

f(m)e2πi⟨x,m⟩.

m∈Zd

In particular, f is almost everywhere equal to a continuous function on Td; see [22, Prop. 3.1.14]. If moreover f ∈ L2(Td), then Plancherel’s identity states that

∥f∥2L2(Td) = ∑

###### | f(m)|2.

m∈Zd

As an immediate consequence of Theorem 1.1, we obtain the following result.

- Theorem 2.18. Let s ∈ {+,−}, d ⩾ 1. Let f ∈ L1(Td) be nonzero and such that f ∈ ℓ1(Zd), ˆ

Td

f dλ ⩽0, and ∑

m∈Zd

s f(m) ⩽ 0.

Then the following inequality holds:

λ({x ∈ Td : f(x) < 0})·#{m ∈ Zd : s f(m) < 0} ⩾

1 16

.

The space (Td,d∞,λ) is admissible for 0 = (0,...,0) ∈ Td in the sense of Definition 1.2. Here, d∞ : Td ×Td → [0,1] is defined via

d∞(x,y) := max

1⩽j⩽d

|xj −yj|,

where |x| denotes the distance from x to 0 in T1. The following result then follows from Theorem 1.4, or more directly from Theorem 2.18.

- Theorem 2.19. Let s ∈ {+,−}, d ⩾ 1. Let f ∈ As(Td) be a nonzero, even function, for which there exist rf ∈ (0,1],ks f ⩾ 1 with the following properties: f(x) ⩾ 0 if d∞(x,0) ⩾ rf while f(0) ⩽ 0, and s f(m) ⩾ 0 if |m| ⩾ ks f while sf(0) ⩽ 0. Then the following inequality holds:


###### rf(2ks f −1) ⩾ 2−(1+d4).

In the companion paper [18], we established the following estimate:

inf

f∈A+(T1)\{0}

rfk f ⩽ A+(1); (2.17)

see [18, Prop. 4]. We do not know whether an analogous result holds for s = −1. Another open problem is to determine whether equality holds in (2.17), in which case the statement could be regarded as a transference principle between the continuous and discrete settings. It would also be interesting to prove a similar result for Dini series, which should relate to the higher dimensional ±1 uncertainty principles As(d), d ⩾ 2, and are the subject of the next section.

- 2.4 Dini Series The Dini series of a function f : [0,1] → R is given by


f(x) = B0(x)+

∞

### ∑

cnJν(λnx), (2.18)

n=1

where 0 < λ1 < λ2 < ... denote the positive zeros of the function

zJν′ (z)+HJν(z) = (H +ν)Jν(z)−zJν+1(z). (2.19)

Here, Jν is the Bessel function of the first kind of order ν ⩾ −21, and H ∈ R. The initial term in (2.18), B0(x), depends on the sign of H +ν. If H +ν > 0, then B0 ≡ 0; if H +ν < 0, then the function (2.19) has two purely imaginary zeros ±iλ0, whose contributions are manifested by taking B0(x) to be an appropriate multiple of Jν(iλ0x); if H +ν = 0, then the imaginary zeros coalesce at the origin, and B0(x) = 2(ν +1)xν

´ 1

0 tν+1 f(t)dt. Note that the functions x  → Jν(λnx),n ∈ , are orthogonal in [0,1] with respect to the measure xdx. Indeed, [34, §5.11-(8)] implies that, for all real numbers k ̸= ℓ,

ˆ 1

kJν+1(k)Jν(ℓ)−ℓJν(k)Jν+1(ℓ) k2 −ℓ2

. (2.20)

Jν(kx)Jν(ℓx)xdx =

0

If k,ℓ are distinct zeros of (2.19), then one can invoke the usual recurrence relations for Bessel functions in order to deduce that the integral in (2.20) vanishes.

If H +ν = 0, then the elements of the sequence {λn}n⩾1 coincide with the positive zeros of the function

Jν+1. In this case, if ν = −12, then Jν+1(x) = (π2x)12 sin(x) and λn = πn; hence the Dini series (2.18) specializes to the Fourier series from §2.3. In this way, Dini series for H +ν = 0 are seen to generalize one-dimensional Fourier series to the higher dimensional radial case.

In order to properly place Dini series within the scope of Theorem 1.4, we need to normalize the functions Jν(λnx), in such a way as to ensure that their maximum is attained at the origin. This is most easily done by introducing the even, entire function Aν(z) := Γ(ν +1)(12z)−νJν(z), since |Aν(z)| ⩽ Aν(0) = 1. One can then rescale the results from [34, §18.33], and invoke the identity [34, §5.11-(11)],

2 ν(λn)

´ 1 0 A2ν(λnx)x2ν+1dx = A

2 , in order to derive the following proposition.

- Proposition 2.20. Let ν ⩾ −12. For every f ∈ L2 [0,1], 2x(2νν++11) dx , we have that


∞

f(x) = f(0)+2√ν +1

### ∑

n=1

Aν(λnx) Aν(λn)

f(n)

(2.21)

in the L2-sense, where {λn}n⩾1 denote the positive zeros of the Bessel function Jν+1,

2√ν +1 Aν(λn)

x2ν+1dx 2(ν +1)

ˆ 1

f(x)Aν(λnx)

f(n) =

, (2.22)

0

0 f(x)x22(νν++11d)x. Moreover, if f is continuous and of bounded variation in [0,1], then the Dini series (2.21) of f converges absolutely and uniformly in [0,1].

´ 1

for all n ⩾ 1, and f(0) =

´ 1

0 Aν(kx)x2ν+1dx = A2ν(k++1(1k)), and reveals that the functions {Aν(λnx)}n⩾1 are orthogonal to the constant function 1. Consequently, the orthonormal basis

Identity [34, §12.11-(1)] translates into

2√ν +1 Aν(λn)

Aν(λnx)

{1}∪

n⩾1 satisfies all the hypotheses of Theorem 1.4 with 0 = 0. We can then use the well-known asymptotic formulae λn ∼ πn and

2 πz

###### cos(z−νπ/2−π/4)+O(|z|−3/2),

Jν(z) =

see [34, §7.1], in order to deduce that Aν(λn)−2 ∼ λn2ν+1, where the implied constant depends only on ν. The following result can then be derived from Theorem 1.4 at once.

- Theorem 2.21. Let s ∈ {+,−}, ν ⩾ −12. Let f : [0,1] → R be a nonzero continuous function of bounded variation, whose coefficients { f(n)}n⩾1 defined in (2.22) satisfy


∞

- 1

- 2| f(n)| < ∞.


### ∑

nν+

n=1

Suppose that there exist rf ∈ (0,1], ksf ⩾ 1, such that f(x) ⩾ 0 if x ∈ [rf,1] while f(0) ⩽ 0, and s f(n) ⩾ 0 if n ⩾ ksf while sf(0) ⩽ 0. Then there exists cν > 0, such that

rf ksf2ν+2 ⩾ cν. (2.23)

The constant cν in (2.23) depends only on ν and can be made explicit, e.g. by appealing to [26, Lemma

- 2.5]. However, the number of terms in the required asymptotic expansion grows linearly with the parameter ν, and as such we have omitted the precise formulation of the corresponding (somewhat cumbersome) statement.

3 Sign Uncertainty in Discrete Spaces

- 3.1 Discrete Fourier Transform


Let q ⩾ 1 be an integer, and let Z2q+1 denote the set of equivalence classes of integers modulo 2q+1. The choice of a residue class of odd size is convenient9 for numerical purposes, since we can then place the origin (in the sense of Definition 1.2) at n = 0.

9On the other hand, everything that follows can be easily adapted to residue classes of arbitrary size.

If f : Z2q+1 → R is real-valued and even, then its discrete Fourier transform f, defined via

q

1 √2q+1

### ∑

f(k) =

n=−q

1 √2q+1

kn

f(n)e−2πi

2q+1 =

q

kn 2q+1

### ∑

f(n)cos 2π

f(0)+2

n=1

is likewise real-valued and even. Since the discrete Fourier transform defines an isometry from L2(Z2q+1) ≃ R2q+1 onto itself, and max−q⩽k⩽q| f(k)| ⩽ (2q+1)−21 ∑qn=−q|f(n)|, the following result is a direct consequence of Theorem 1.1.

- Theorem 3.1. Let s ∈ {+,−} and q ⩾ 1 be an integer. Let f : Z2q+1 → R be nonzero and even. Assume that sf(0) ⩽ 0 and f(0) ⩽ 0. Then the following inequality holds:


2q+1 16

#{n ∈ Z2q+1 : f(n) < 0}·#{k ∈ Z2q+1 : s f(k) < 0} ⩾

###### .

The following problem will be of interest.

- Problem 3.1 (Feasibility Linear Programming Problem for the discrete Fourier transform). Given s ∈ {+,−}, let


Adiscs (q) := min{ksf ⩾ 0 : f ∈ Adiscs (q)},

where Adiscs (q) denotes the set of even functions f :Z2q+1 →R, such that sf(0), f(0)⩽0 and f(±q),s f(±q)⩾ 1, and ksf is the smallest nonnegative integer, for which f(n),s f(n) ⩾ 0 if ksf ⩽ |n| ⩽ q. Here, |n| denotes the absolute value of the representation of n in the interval {−q,...,0,...,q}.

- Definition 3.2 (s-Feasibility). Let s ∈ {+,−}. A pair (k,q) is s-feasible if there exists f ∈ Adiscs (q), such that ksf ⩽ k.


The following result is an immediate consequence of Theorem 3.1 and Definition 3.1.

- Corollary 3.3. Let s ∈ {+,−} and q ⩾ 1 be an integer. Then


Adiscs (q) √2q+1

1 8

⩾

###### .

Problem 3.1 can be solved numerically with a linear programming solver, and we have done so. Numerical evidence presented in §6.1 strongly supports the following conjecture.

- Conjecture 3.4. Let s ∈ {+,−}. If (k,q) is s-feasible, then (k+1,q),(k,q−1) are s-feasible. The function


q  → Adiscs (q) is non-decreasing, and its range contains all integers k ⩾ 2 if s = +1, and all integers k ⩾ 3 if s = −1. Moreover,

Adiscs (q) √2q+1

###### = As(1).

lim

q→∞

where As(1) denotes the optimal constant for the one-dimensional continuous sign uncertainty principles defined in (1.2), (1.3).

Since the discrete Fourier transform is a proper discretization of the Fourier transform (1.1), it is natural to expect that the discrete uncertainty principles converge to their continuous counterparts, in the limit when q → ∞. Indeed, this is what seems to happen numerically. Moreover, the patterns in §6.1 (see Table 1) are relatively straightforward to identify, and they provide evidence towards the following conjecture.

2

2

2 ) is −1-feasible, for every integer k ⩾ 4. Moreover, if q−(k) = (k−1)

- Conjecture 3.5. The pair (k, (k−1)


2 , then k = Adiscs ( qs(k))+o(k).

In this way, Conjectures 3.4 and 3.5 together imply A−(1) = 1, which is known to hold; recall the discussion in §1.1, and see §6.1 below for further details.

We have performed extensive numerical computations for Problem 3.1 using the Gurobi linear programming solver [24] implemented via PARI/GP [4], which we discuss in §6. Numerically we observed the dimension of the cone of optimal vectors f ∈ Adiscs (q) for Problem 3.1 which satisfy ksf = Adiscs (q) to be large. Further numerical experiments revealed that a good selection method consists in finding an optimal vector f ∈ Adiscs (q) for which the corresponding energy, ∑|n|⩾ksf f(n)2, is minimized. In particular, the plot of such a vector appears to be quite smooth.10 In the −1 case, we were able to exactly identify the vector f⋆ ∈ Adisc− (q) delivered by the the solver after energy was minimized. We observed that

2sin2(πx) π(1−x2)

f⋆(n) ≈ sin(2π|x|)1[−1,1](x)−

(3.1)

for x = n/√2q+1 and |n| ⩽ q. Indeed, the function on the right-hand side of (3.1) is admissible and optimal for the continuous −1 uncertainty principle, revealing once again that A−(1) = 1. Our next results makes these numerical observations precise, and adds weight to the validity of Conjecture 3.4.

- Proposition 3.6. Assume 2q+1 = ℓ2, for some integer ℓ ⩾ 3, and set


g(n) = sin(2π|n|/ℓ)1[−ℓ,ℓ](n),

so that, for |n| ⩽ q,

2sin2(πn/ℓ)sin(2π/ℓ) ℓ(cos(2πn/ℓ2)−cos(2π/ℓ))

g(n) =

.

Let f⋆ = g− g. Then f⋆ ∈ Adisc− (1), f⋆ = −f⋆, f⋆(0) = 0, and k−f⋆ = ℓ. Hence

Adisc− (q) √2q+1

⩽ 1.

In general, if 2q+1 is not a perfect square, then

- 1+√2q

- 2q+1


Adisc− (q) √2q+1

⩽ 1+

,

10Recall that the Gibbs phenomenon permeates throughout such numerical computations, and one should find ways to reduce it.

disc − (q)

for all q ⩾ 5. In particular, limsupq→∞ A

###### √2q+1 ⩽ 1.

Proof. Setting x = n/ℓ, a straightforward computation shows that11

2sin2(πx)sin(2π/ℓ) ℓ(cos(2πx/ℓ)−cos(2π/ℓ))

ℓ

2 ℓ

### ∑

sin(2π j/ℓ)cos(2π jx/ℓ) =

g(n) =

. (3.2)

j=1

To verify (3.2), replace sine and cosine by the corresponding exponential representations, note that the resulting sums are geometric and thus can be calculated explicitly, and rearrange terms. The claimed properties of the function f⋆ = g− g are easy to deduce, and we leave the details to the reader. For any given q ⩾ 5 for which 2q+1 is not a perfect square, we can simply take ℓ ⩾ 4 such that (ℓ−1)2 < 2q+1 ⩽ ℓ2; in particular, q ⩾ ℓ. Then g can be seen as a vector in Adisc− (q) and, by the same computations as above, g(n) ⩽ 0 if |n| ⩾ ⌈(2q+1)/ℓ⌉. We obtain

- 1+√2q

- 2q+1


Adisc− (q) √2q+1

⩽ ⌈(2q+1)/ℓ⌉ℓ

ℓ 2q+1

⩽ 1+

⩽ 1+

,

2q+1

as desired. This concludes the proof of the proposition.

| |
|---|


For every fixed x ∈ R, we have that

2sin2(πx) π(1−x2)

f⋆(⌊ℓx⌋) → sin(2π|x|)1[−1,1](x)−

, as ℓ → ∞.

Numerically we have confirmed that Adisc− ((ℓ2−1)/2) = ℓ, for every ℓ ⩽ 100. It would be nice to find a proof along the lines of the reasoning above, showing that Adisc− ((ℓ2 −1)/2) ⩾ ℓ.

Conjecture 3.7. Adisc− ((ℓ2 −1)/2) = ℓ, for every integer ℓ ⩾ 3.

###### 3.2 Discrete Hankel Transform

The discrete Hankel transform was proposed by Siegman in 1977, and later on several other versions were put forward; see [15]. To the best of our knowledge, none of the proposed explicit forms defines a unitary operator; rather, they are only asymptotically unitary. In one way or another, they all properly discretize a given compactly supported function f, and then appeal to Bessel–Fourier series in order to further discretize the Hankel transform of f. Fisk Johnson [15] proposes several approaches, which turn out to work well in practice since they are already very close to being unitary when applied to “short” vectors. Since Theorem 1.1 only requires approximate inversion, it seems reasonable to expect that a sign uncertainty principle holds for each of the kernels defined in [15, (13) & (16)–(19)]; for the sake of brevity, we chose not to fully pursue this line of investigation.

11Note that if n = ℓ, then the numerator vanishes with the same order as the denominator.

The main purpose of this section is to formulate a sign uncertainty principle for the discrete Hankel transform of Fisk Johnson, and to start discussing the numerical experiments which we conducted. Since (after normalization) the Hankel transform of order ν = d2 −1 coincides with the Fourier transform of a radial function in Rd, one may expect that, in the limit, the corresponding discrete sign uncertainty principle converges to the continuous sign uncertainty principle in all dimensions. We proceed to describe the evidence we obtained in support of this possibility.

Given ν ⩾ −21, let {jn}n⩾1 denote the positive zeros of the Bessel function Jν. Our starting point is formula [15, (13)], for N = q+1 and T = jq+1. Fisk Johnson proposes a discretization of the following version of the Hankel transform of parameter ν ⩾ −21,

Hν(f)(x) = ˆ ∞

f(y)Jν(xy)ydy, (3.3)

0

which we proceed to describe. Define the discrete Hankel transform with parameter ν ⩾ −12 of a given12 f : [q] → R, as follows:

q

Jν(jm jn/jq+1) Jν+1(jn)2

2 jq+1

### ∑

Hνdisc(f)(m) =

f(n)

###### .

n=1

Each of the values f(n) is to be interpreted as the evaluation of some continuous function at the node jn(jq+1)−

- 1

- 2. By showing that the kernel of the composition HνdiscHνdisc satisfies13


q

4 Jν+1(jℓ)jq2+1

n=1

Jν(jm jn/jq+1)Jν(jn jℓ/jq+1) Jν+1(jn)2

### ∑

###### = δm,ℓ +o(1), as q → ∞,

where the term o(1) is already small for small values of q, the author argues that HνdiscHνdisc ≈ Id; see [15,

(11)]. We turn to the following feasibility problem.

- Problem 3.2 (Feasibility Linear Programming Problem for the discrete Hankel transform). Given s ∈ {+,−}, let


Adiscs (q,ν) := min{ksf : f ∈ Adiscs (q,ν)},

where Adiscs (q,ν) denotes the set of functions f : [q] → R, such that sf(1),Hνdisc(f)(1) ⩽ 0 and f(q),s f(q) ⩾ 1, and ksf is the smallest nonnegative integer for which f(n), sHνdisc(f)(n) ⩾ 0 if ksf ⩽ n ⩽ q.

- Definition 3.8 ((s,ν)-Feasibility). Let s ∈ {+,−},ν ⩾ −12. A pair (k,q) is (s,ν)-feasible it there exists f ∈ Adiscs (q,ν), such that ksf ⩽ k.


In §6.2 below, we present compelling numerical evidence towards the following conjecture.

- Conjecture 3.9. Let s ∈ {+,−},ν ⩾ −21. If (k,q) is (s,ν)-feasible, then (k +1,q),(k,q −1) are (s,ν)feasible. The function q  → Adiscs (q,ν) is non-decreasing, and its range contains \[k0], for some k0 ⩾ 1.


- 12Here, [q] := {1,2,...,q}.
- 13Here, δm,ℓ denotes the usual Kronecker delta: δm,ℓ = 1 if m = ℓ, and δm,ℓ = 0 otherwise.


Moreover, if ν = d2 −1 and nq = Adiscs (q,ν), then

jnq 2π jq+1

lim

q→∞

= As(d), (3.4)

where As(d) denotes the optimal constant for the continuous sign uncertainty principles defined in (1.2), (1.3), and {jn}n⩾1 are the positive zeros of the Bessel function Jν.

If f : Rd → R is radial and ν = d2 −1, then identity (4.3) below can be rephrased as

d 2−1 f(ξ) = cν Hν[yν f(y)](2π|ξ|),

|ξ|

for some cν > 0, and therefore the factor √2π in (3.4) is to be expected. The particular cases d ∈ {8,12,24} are especially interesting since it is known that A−(8) = A+(12) = √2 and A−(24) = 2. In these cases, the numerical data presented in §6.2 corroborate Conjecture 3.9. Moreover, if d ∈ {2,8,12,24}, then our numerics point to the following more structured version of Conjecture 3.9.

- Conjecture 3.10. The following statements hold:


- • k,⌊

√3(k2−2k+2)

4 ⌋ is (−1, 22 −1)-feasible, for every integer k ⩾ 4;

- • k,⌊k42⌋ is (−1, 82 −1)-feasible, for every integer k ⩾ 4;

- • k,⌊k2+68k−8⌋ is (−1, 242 −1)-feasible, for every integer k ⩾ 4;

- • k,⌊k24−2⌋ is (+1, 122 −1)-feasible, for every integer k ⩾ 3.


Moreover, if we write the pairs above as (k, qs(k,ν)) for (s,ν) = (−,0),(−,3),(−,11),(+,5), respectively, then

k = Adiscs ( qs(k,ν),ν)+o(k), as k → ∞.

Noting that jn ∼ πn, as n → ∞, Conjectures 3.9 and 3.10 would imply that A−(8) = A+(12) = √2 and A−(24) = 2, which are known to be true, but also that A−(2) = (43)14, which is the content of Conjecture 1.6.

###### 3.3 Hamming Cube

The Hamming cube HN := {−1,1}N can be equipped with normalized counting measure, λH := 2−N#, and the Hamming distance dH : HN ×HN → [N],

dH(x,y) := #{n ∈ [N] : xn ̸= yn}.

We write x = (x1,...,xN) ∈ HN with xj = ±1, for each j, and let 1 = (1,...,1) ∈ HN. An orthonormal basis of L2(HN) = L2(HN,λH) is given by {ϕS : S ⊆ [N]}, where ϕS : HN → {−1,1} are the monomials defined

via ϕS(x) := ∏i∈Sxi, with the understanding that ϕ0/ ≡ 1. Every function f : HN → R admits an expansion of the form

f = ∑

f(S)ϕS,

S⊆[N]

with (real-valued) coefficients given by

- 1

- 2N ∑


f(x)ϕS(x).

f(S) :=

x∈HN

Let HN = {c : 2[N] → R} denote the finite dimensional vector space of sequences of real numbers indexed by subsets of [N], and define

- 1

- 2N ∑


∥c∥2L2( HN) :=

|c(S)|2.

S⊆[N]

The operator T : HN → HN, f  → 2N2 f, defines an isometric isomorphism, in the sense that

∥T(f)∥2L2( HN) = ∑

| f(S)|2 = ∥f∥2L2(HN).

S⊆[N]

Moreover, supS⊆[N]|T(f)(S)| ⩽ 2N2 ∥f∥L1(HN). We can then apply Theorem 1.1 to the operator T, with p = q = 2, a = 2N2 , and b = c = 1, and obtain the following result.

- Theorem 3.11. Let s ∈ {+,−}. Let f : HN → R be nonzero, and such that

∑

x∈HN

f(x) ⩽ 0, sf(1) ⩽ 0.

Then the following estimate holds:

#{x ∈ HN : f(x) < 0}·#{S ⊆ [N] : s f(S) < 0} ⩾ 2N−4.

In particular, if f(x) ⩾ 0 when dH(x,1) ⩾ r and s f(S) ⩾ 0 when #S ⩾ k, then

r

∑

n=1

N n−1

k

∑

n=1

N n−1

⩾ 2N−4.

4 Sign Uncertainty for Convolution Operators

- 4.1 Convolution Kernels in Bandlimited Function Spaces


Let PWd denote the L1-Paley–Wiener space of bandlimited functions in Rd, i.e. the set of all real-valued, continuous functions f ∈ L1(Rd), whose Fourier support is contained on the unit ball, supp( f) ⊆ Bd1. Given

- a function ψ : Rd → R for which ψ(0) ⩾ 0 and there exist a,b,c ∈ (0,∞), such that ∥ψ∥L∞ = a, ∥ψ∥L1 =


- b, and c| ψ(ξ)| ⩾ 1 if ξ ∈ Bd1, consider the associated convolution operator, Tψ(f) := f ∗ ψ. Young’s convolution inequality and Plancherel’s Theorem together imply that ∥Tψ(f)∥L∞ ⩽ a∥f∥L1, ∥Tψ(f)∥L1 ⩽ b∥f∥L1, ∥Tψ(f)∥L2 ⩽ b∥f∥L2, and ∥f∥L2 ⩽ c∥Tψ(f)∥L2, for every f ∈ PWd. Therefore the family F = {(f,Tψ(f)) : f ∈ PWd} satisfies the hypotheses of Theorem 1.1 with p = q = 2, and we obtain the following result.


- Theorem 4.1. Let d ⩾ 1. Let ψ : Rd → R be as above. Let f ∈ PWd \{0} be such that


Rd f ⩽ 0. Then the following inequality holds:

´

|{x ∈ Rd : f(x) < 0}||{ξ ∈ Rd : Tψ(f)(ξ) < 0}| ⩾ (16a2b2c4)−1.

In particular, if there exist r1,r2 > 0 such that f(x) ⩾ 0 if |x| ⩾ r1, and Tψ(f)(ξ) ⩾ 0 if |ξ| ⩾ r2, then

r1r2 ⩾ 16a2b2c4|Bd1|2

−d1 .

Theorem 4.1 can be extended to the more general setting of locally compact abelian groups; the reader is referred to [30] for the relevant background.

###### 4.2 Hilbert Transform of Bandlimited Functions

It is of interest to consider the situation in which the kernel ψ from §4.1 above fails to be integrable. For instance, if d = 1, then the choice ψ(x) = π1x leads to the Hilbert transform H, as long as the convolution is taken in the principal value sense. It is well-known that H defines a bounded operator in Lp(R), for all

- p ∈ (1,∞), and that the optimal constant in ∥H(f)∥Lp ⩽ Cp∥f∥Lp is given by


Cp :=

tan(2πp), if 1 < p ⩽ 2, cot(2πp), if 2 < p < ∞;

(4.1)

see [28]. Moreover, since H(f)(ξ) = −isign(ξ) f(ξ), we have that H(H(f)) = −f, hence the reverse inequality, ∥f∥Lp ⩽ Cp∥H(f)∥Lp, holds with the same optimal constant. Now, if f ∈ PW1 (recall the definition in §4.1), then f is supported in [−1,1], and consequently

∥H(f)∥L∞ ⩽ ∥ H(f)∥L1 = ∥ f∥L1 ⩽ 2∥ f∥L∞ ⩽ 2∥f∥L1.

Note that f is continuous since f ∈ L1. A necessary condition for H(f) to be integrable if f ∈ L1 is that

- f(0) = 0, in which case H(f)(0) = 0 as well. We then conclude that


###### Fs = {(f,sH(f)) : f ∈ PW1; f(0) = 0}

satisfies all the hypotheses of Theorem 1.1, with p = q ∈ (1,∞), a = 2, and b = c = Cp. As a consequence, we obtain the following result.

- Theorem 4.2. Let s ∈ {+,−} and p ∈ (1,∞). Let f ∈ PW1 satisfy f(0) = 0. Suppose that there exist r1,r2,s > 0, such that f(y) ⩾ 0 if |y| ⩾ r1, and sH(f)(x) ⩾ 0 if |x| ⩾ r2,s. Then the following estimate holds:


p+1 p−1

1 r21,/sp ⩾ 2−(p′+2)C−

′

r1/p

p ,

where Cp is given by (4.1) above.

Theorem 4.2 can probably be extended to a certain class of singular integral operators given by Calderón– Zygmund kernels of convolution type (see [22, Ch. 5]) which includes the higher dimensional Riesz transforms.

###### 4.3 Hankel Transform

The Hankel transform with parameter ν > −1 of a function f : R+ → R is given by

Hν(f)(x) = ˆ ∞

f(y)Aν(xy)y2ν+1dy, (4.2)

0

where Aν(z) = Γ(ν +1)(12z)−νJν(z), and Jν is the Bessel function of the first kind. Alternative ways to define the Hankel Transform exist, the most common one having Aν replaced by Jν, and y2ν+1dy replaced by ydy; recall (3.3), and see e.g. [32]. However, the choice of kernel in (4.2) suits us better since the function Aν(z) is entire, Aν(0) = 1, and routine computations show that, if f : Rd → R is radial, then its Fourier transform f, as defined in (1.1), is also radial, and satisfies

2−1(f)(2π|ξ|), (4.3)

f(ξ) = cdHd

for some cd > 0. The analogue of (2.20) over the unbounded region of integration (0,∞) reveals the following Plancherel-type identity:

ˆ ∞

|Hν(f)(x)|2x2ν+1dx = 4νΓ2(ν +1)ˆ ∞

|f(y)|2y2ν+1dy.

0

0

Moreover, since |Aν(x)| ⩽ Aν(0) = 1, we easily obtain that

|Hν(f)(x)| ⩽ ˆ ∞

|f(y)|y2ν+1dy.

sup

x>0

0

Therefore, for a given s ∈ {+,−}, the family

Fs = (f,Hν(f)) : f,Hν(f) ∈ L1(R+,y2ν+1dy),

ˆ ∞

f(y)y2ν+1dy,sˆ ∞

Hν(f)(x)x2ν+1dx ⩽ 0

0

0

satisfies the hypotheses of Theorem 1.1 when p = q = 2, a = 1, and b = 1/c = 2νΓ(ν + 1). It is then straightforward to derive the following result.

- Theorem 4.3. Let s ∈ {+,−} and ν > −1. Let f : R+ → R be a continuous nonzero function, such that f,Hν(f) ∈ L1(R+,y2ν+1dy). Assume that there exist r1,r2,s > 0, such that f(y) ⩾ 0 if y ⩾ r1 while Hν(f)(0) ⩽ 0, and sHν(f)(x) ⩾ 0 if x ⩾ r2,s while sf(0) ⩽ 0. Then the following estimate holds:


r1r2,s ⩾ 4ν−2Γ2(ν +1).

#### 5 Proofs of Main Results

###### 5.1 Proof of Theorem 1.1

Proof. Since

X f dµ ⩽ 0, we have that

´

∥f∥L1(X,µ) ⩽ 2ˆ

{f<0}

1

|f|dµ ⩽ 2µ({f < 0})

p′ ∥f∥Lp(X,µ), (5.1)

where the last estimate follows from Hölder’s inequality. On the other hand, the hypotheses, convexity of Lp-norms, the fact that s

Y gdν ⩽ 0, and a second application of Hölder’s inequality, together yield

´

∥f∥qLp(X,µ) ⩽ cq∥g∥qLq(Y,ν) ⩽ cq∥g∥qL−∞(1Y,ν)∥g∥L1(Y,ν) ⩽ 2cqaq−1∥f∥qL−1(1X,µ)

ˆ

|g|dν

{sg<0}

1

⩽ 2cqaq−1∥f∥qL−1(1X,µ)ν({sg < 0})

q′ ∥g∥Lq(Y,ν) ⩽ 2cqaq−1b∥f∥qL−1(1X,µ)ν({sg < 0})

1

q′ ∥f∥Lp(X,µ).

Cancelling one power of ∥f∥Lp(X,µ) (which is allowed since f is nonzero), taking the (q−1)-th root on both sides, and plugging the resulting estimate into (5.1), we finally obtain:

q′

1

1

q (2c)q′µ({f < 0})

p′ ν({sg < 0})

∥f∥L1(X,µ) ⩽ ab

q∥f∥L1(X,µ),

from where (1.4) follows at once.

| |
|---|


###### 5.2 Proof of Theorem 1.4

Proof. Let f ∈ As(X)\{0} and S := {x ∈ X : f(x) < 0}. On the one hand,

and therefore

0 ⩾ f(0) = ˆ

X

f dλ = ˆ

X\S

|f|dλ −ˆ

S

|f|dλ,

∥f∥L1(X) ⩽ 2ˆ

S

- 1

- 2∥f∥L2(X). (5.2)


|f|dλ ⩽ 2λ(S)

On the other hand, setting R := {n ⩾ 0 : s f(n) < 0}, we have

∞

### ∑

s f(n)ϕn(0)= ∑

| f(n)|∥ϕn∥L∞(X)− ∑

| f(n)|∥ϕn∥L∞(X), (5.3)

0 ⩾ sf(0) =

n∈R

n=0

n∈/R

where in the latter identity we used that ϕn(0) = ∥ϕn∥L∞(X). We also have that

| f(n)| = ˆ

X

fϕndλ ⩽ ∥f∥L1(X)∥ϕn∥L∞(X),

and therefore

∞

### ∑

∥f∥2L2(X) =

| f(n)|2

n=0

∞

### ∑

| f(n)|∥ϕn∥L∞(X)

⩽ ∥f∥L1(X)

n=0

⩽2∥f∥L1(X) ∑

| f(n)|∥ϕn∥L∞(X)

n∈R

⩽2∥f∥L1(X)∥f∥L2(X) ∑

∥ϕn∥2L∞(X)

n∈R

- 1

- 2


###### .

From the second to the third lines, we appealed to (5.3). Cancelling one power of ∥f∥L2(X) from both sides, and plugging the resulting estimate into (5.2), yields (1.10).

| |
|---|


###### 5.3 Proof of Theorem 2.3

Proof. The strategy is to establish identity (2.5), and then invoke Theorem 2.13. With this purpose in mind, let f ∈ Bs(Sd−1)\{0}, and let SOη(d) ⊆ SO(d) denote the subgroup of rotations which fix the north pole η ∈ Sd−1, equipped with Haar probability measure γ. Consider the partially radialized function g : Sd−1 → R, defined by

g(ω) = ˆ

f(ρ ω)dγ(ρ). (5.4)

SOη(d)

One easily checks that g is continuous, sg(η) = sf(η) ⩽ 0, and that θ(g) ⩽ θ(f). Note that the possibility that g ≡ 0 cannot be excluded, so we split the analysis into two cases.

First we consider the case when g is nonzero. Set ν = d2 −1, and let Zn(ω) := Cnν(⟨ω,η⟩) denote the

zonal harmonic of degree n. Here, Cnν is the Gegenbauer polynomial of degree n; see (2.10). If d ⩾ 3, then n+ν

ν Cnν(⟨·,·⟩) is the reproducing kernel of Hnd with respect to the normalized surface measure on Sd−1; see [13, Def. 1.2.2 and Theorem 1.2.6]. Consequently,

ˆ

P(ρ ω)dγ(ρ) = P(η)

SOη(d)

Zn(ω) Zn(η)

, for every P ∈ Hnd. (5.5)

To verify identity (5.5), one checks that the left-hand side depends on ω only through its inner product with the north pole, invokes [13, Lemma 1.7.1], and sets ω = η to compute the leading constant on the right-hand side. It follows from (2.1), (5.4), (5.5) that

g(ω) =

∞

hn

### ∑

### ∑

anZn(ω), where an :=

n=0

Yn,j(η) Zn(η)

f(n, j)

###### .

j=1

From (2.9) and (2.10), we have that Zn(η) = Cnν(1) = n+2nν−1 > 0, and since the basis {Yn,j} is signed, it follows that san ⩾ 0, for every n ⩾ k(s f). Set G(x) := g(ω), where x = ⟨ω,η⟩. The function G : [−1,1] → R is continuous, and satisfies sG(1) = sg(η) ⩽ 0. Moreover, for every x ∈ [−1,cos(θ(f))], we have that G(x) = ∑∞n=0anCnν(x) ⩾ 0, where san ⩾ 0, for every n ⩾ k(s f). As a consequence, we obtain the following lower bound:

(1−cos(θ(f)))k(s f)2 ⩾ Bs(I;ν − 21,ν − 12). (5.6)

If g ≡ 0, then an = 0 for all n ⩾ 0, and since Yn,j(η) > 0 for all sufficiently large n, we also have that f(n, j) = 0 for all sufficiently large n. Hence f is a polynomial. In turn, this implies θ(f) = π, for otherwise f would have to vanish identically on the spherical cap {ω ∈ Sd−1 : θ(f) < dg(ω,η) ⩽ π}, which cannot happen unless f were the zero polynomial. This shows that (1−cos(θ(f)))k( f)2 ⩾ 2 and14 (1−cos(θ(f)))k(− f)2 ⩾ 8. On the other hand, the functions

C1ν(x) C1ν(1)

C1ν(x) C1ν(1)

C2ν(x) C2ν(1)

f+(ω) = −1+

, f−(ω) = −

+

###### ,

respectively belong to B+(Sd−1), B−(Sd−1) as functions of ω, and respectively belong to B+(I;ν − 12,ν −

- 1

- 2), B−(I;ν − 12,ν − 21) as functions of x = ⟨ω,η⟩. They also satisfy (1 − cos(θ(f+)))k( f+)2 = 2 and (1−cos(θ(f−)))k(− f−)2 = 8, hence (5.6) still holds. This also establishes the upper bounds in (2.4). We conclude that Bs(Sd−1)2 ⩾ Bs(I;ν − 12,ν − 12). Conversely, given a function F in Bs(I;ν − 12,ν − 12), then


14Recall that, by the discussion preceding the statement of Theorem 1.4, we must have k(− f) ⩾ 2.

f := F(⟨·,η⟩) belongs to Bs(Sd−1), and satisfies

(1−cos(θ(f)))12k(s f) = r(F;I)12k(s F).

This shows that Bs(Sd−1)2 ⩽ Bs(I;ν − 21,ν − 12), and therefore (2.5) holds. Theorem 2.13 then implies the following lower bound:

Bs(Sd−1) = Bs(I;ν − 12,ν − 12)12

2 ν+1/2

Γ(ν + 23)

⩾

2

(4e121 )

ν+1/2(ν + 12)(ν + 32)

This concludes the proof of the theorem.

- 1

- 2


2Γ(d+21)d−21 (4e121 )d−21(d2 −1)12

=

.

| |
|---|


###### 5.4 Proof of Theorem 2.13

Proof. Let α ⩾ β ⩾ −12. Consider the interval I = [−1,1], equipped with the restricted Euclidean metric d and the probability measure wα,β. Then (I,d,wα,β) is an admissible space in the sense of Definition 1.2, with 0 = 1. Indeed, if α = max{α,β} ⩾ −12, then from [31, Theorem 7.32.1] and (2.9) it follows that

|Pn(α,β)(x)| = Pn(α,β)(1), (5.7)

max

−1⩽x⩽1

and therefore the orthogonal basis {p(nα,β)}n∈ of L2(I) satisfies (1.6) with 0 = 1.

Moreover, the class As(I) from Definition 1.3 coincides with the class Bs(I;α,β) from Definition 2.12. To see why this is the case, note that (5.7) and the second condition required by Definition 1.3 together imply that ∞

| f(n)|pn(α,β)(1) < ∞. (5.8)

### ∑

n=0

Therefore the series (2.12) converges absolutely and uniformly, and the function f is continuous. This shows that As(I) ⊆ Bs(I;α,β). Conversely, the sequence {s f(n)}n∈ being eventually nonnegative implies that (5.8) holds if and only if ∑∞n=0 f(n)p(nα,β)(1) < ∞, which in turn is equivalent to the limit limr→1− ∑∞n=0 f(n)p(nα,β)(1)rn existing and being finite. The latter limit exists and equals f(1) since the power series of any real-valued, continuous function on I is Abel summable. It follows that As(I) = Bs(I;α,β), as claimed.

From Theorem 1.4, it then follows directly that ˆ 1

Pn(−α,1β)(1)2 h(nα−,1β)

k(s f)

1 16

### ∑

⩾

wα,β(x)dx

. (5.9)

1−r(f;I)

n=1

To estimate the left-hand side of (5.9), start by noting that the confluent form of the Christoffel–Darboux

formula for Jacobi polynomials (see [31, (4.5.8)]) implies that

Pn(−α,1β)(1)2 h(nα−,1β)

k(s f)

Γ(α +k(s f)+1)Γ(α +β +k(s f)+1)Γ(β +1) Γ(α +2)Γ(k(s f))Γ(β +k(s f))Γ(α +β +2)

### ∑

. (5.10)

=

n=1

A version of Stirling’s formula for the Gamma function [29] states that

√2πxx−

- 1

- 2e−xeµ(x), for every x > 0,


Γ(x) =

where the function µ satisfies the two-sided inequality 12x1+1 < µ(x) < 121x. Moreover, it is elementary to check that

a x

x

⩽ exp(a), for every a,x ⩾ 0. In particular, if x ⩾ y ⩾ −1,k ⩾ 1, then we may estimate:

1+

- (k+x+1)k+x+

- 1

- 2e−k−x−1


- (k+y+1)k+y+


- Γ(k+x+1)

- Γ(k+y+1)


⩽ e121

- 1

- 2e−k−y−1


- 1

- 2


k+y+

x−y k+y+1

= e121 ey−x(k+x+1)x−y 1+

###### ⩽ e121 (k+x+1)x−y ⩽ e121 kx−y(x+2)x−y.

Applying the latter estimate (twice) to (5.10), with k = k(s f), yields

Γ(α +k(s f)+1)Γ(α +β +k(s f)+1)Γ(β +1) Γ(α +2)Γ(k(s f))Γ(β +k(s f))Γ(α +β +2)

e16(α +2)α+1(α +β +2)α+1Γ(β +1) Γ(α +2)Γ(α +β +2)

k(s f)2α+2. (5.11)

⩽

On the other hand, a crude estimate together with identity (2.11) yield ˆ 1

wα,β(x)dx ⩽ cα,β2β ˆ 1

Γ(α +β +2) Γ(α +2)Γ(β +1)

- 1

- 2α+1


(1−x)α dx =

r(f;I)α+1. (5.12)

1−r(f;I)

1−r(f;I)

The lower bound in (2.14) now follows from (5.9), (5.10), (5.11), (5.12). Since the upper bounds were already established via (2.15), this concludes the proof of the theorem.

| |
|---|


###### 5.5 Proof of Proposition 2.14

Proof. We split the proof into the cases s ∈ {+,−}.

Case s = −1. Let f ∈ B−(I;α,β)\{0}, and consider the auxiliary polynomial g−,

p(nα,β)(x)2 (x−x1,n)

(1−x1,n) pn(α,β)(1)2

g−(x) =

,

where x1,n denotes the largest zero15 of p(nα,β). Clearly, g−(1) = 1, g−(x) ⩽ 0 if −1 ⩽ x ⩽ x1,n, and g−(0) = 0 (since p(nα,β) is orthogonal to all polynomials of degree less than n). We claim that g−(n) ⩾ 0, for all n ⩾ 1. Indeed, [17, Theorem] states that, for all m,n ⩾ 0,

pn(α,β)(x)pm(α,β)(x) =

m+n

R(α,β, j)p(jα,β)(x),

### ∑

j=0

where R(α,β, j) ⩾ 0, for j = 0,...,m+n. Moreover, [10, Theorem 3.1] implies that the Jacobi expansion of the polynomial

pn(α,β)(x) ∏ℓj=1(x−xj,n)

, (1 ⩽ ℓ ⩽ n)

x  →

has nonnegative coefficients. Together these results directly imply the claim. Since, for any fixed ℓ, xℓ,n → 1 as n → ∞, one can set F− := f − f(1)g−, and check that F− ∈ B0−(I;α,β)\{0}, k(− F−) = k(− f), r(F−;I) < r(f;I), provided n is chosen sufficiently large.

Case s = +1. Let f ∈ B+(I;α,β)\{0}, and consider the auxiliary polynomial g+,

p(nα,β)(x)2 (x−x1,n)(x−x2,n)

(1−x1,n)(1−x2,n) p(nα,β)(1)2

g+(x) =

.

Similarly to the case s = −1, we have that g+(1) = 1, g+(x) ⩾ 0 if −1 ⩽ x ⩽ x2,n, g+(0) = 0, and g+(n) ⩾ 0 for all n ⩾ 1. Letting F+ := f − f(1)g+, we check that F+ ∈ B0+(I;α,β) \ {0}, satisfies k( F+) = k( f), r(F+;I) < r(f;I), provided n is chosen sufficiently large.

| |
|---|


###### 5.6 Proof of Theorem 2.16

We present the proof for the polynomial P only, since it proceeds analogously for Q. For simplicity, we write x0 = 1 and {xm < ... < x1} ⊂ (−1,1) for the zeros of the polynomial p(mα+1,β). The crux of the matter boils down to the following simple result.

Lemma 5.1. Let f ∈ Bs(I;α,β) \ {0} be a polynomial of degree at most 2m, and further assume that

- f(1) = 0 if s = +1. Then r(f;I) ⩾ 1−x1, where equality is attained if and only if f is a positive multiple of the polynomial P in (2.16).


Proof of Lemma 5.1. Aiming at a contradiction, assume that r(f;I) < 1−x1. Then f(x) ⩾ 0 if −1 ⩽ x ⩽ x1,

15More generally, we let −1 < xn,n < xn−1,n < ... < x1,n < 1 denote the zeros of the polynomial p(nα,β).

whence

λj f(xj) = ˆ 1 −1

m

### ∑

0 ⩽ λ0 f(1)+

f(x)wα,β(x)dx = f(0) ⩽ 0.

j=1

Thus f(xj) = 0 for j = 0,...,m, and f′(xj) = 0 for j = 1,...,m. Moreover, f necessarily vanishes at x = 1−r(f;I). We conclude that deg(f) ⩾ 2m+2, which is absurd. The preceding argument further shows that if r(f;I) = 1−x1, then f must coincide with a positive multiple of the polynomial (2.16).

| |
|---|


Proof of Theorem 2.16. Set k := k(s P). Note that k ⩾ 2, and that s P(k−1) < 0. Moreover, since P is monic of degree 2m, then k = 2m+1 if s = −1. Set δ := −21s P(k−1), and let h ∈ B0s(I;α,β)\{0} be such that ∥ch−P∥L∞(I) < δ, for some c > 0. Estimate:

- 1

- 2


|c h(k−1)− P(k−1)| ⩽ ∥ch−P∥L2(I) ⩽ ∥ch−P∥L∞(I) < δ = −

s P(k−1).

Thus sc h(k−1) < 21s P(k−1) < 0, and k(s h) ⩾ k. Lemma 5.1 implies that if h is not a multiple of P (i.e. infc>0∥ch−P∥L∞(I) > 0), then r(P;I) < r(h;I). Therefore r(P;I)k(s P)2 < r(h;I)k(s h)2, as desired.

| |
|---|


#### 6 Numerical Evidence

###### 6.1 Discrete Fourier Transform

Conjecture 3.4 implies the existence of a well-defined jump function k  → qs(k), which records the smallest value of q for which (k,q) is s-feasible but (k−1,q) is not; in other words, k = Adiscs (qs(k)), and no other

- q < qs(k) has this property. We strongly believe that the first few values of qs(k) coincide with the ones displayed in Table 1, although we cannot claim its correctness in any rigorous way since all the computations


were performed using floating-point arithmetic. In the case s = −1, the pattern of qs(k) in Table 1 is easy to guess, since for k > 3 it is in perfect accordance with the sequence

###### (k−1)2

= 5,8,13,18,25,32,41,50,61,72,....

2 k⩾4

From Proposition 3.6 we know that Adisc− (q) ⩽ ℓ if q = (ℓ2 −1)/2. However, (ℓ2 −1)/2 is never equal to

(k−1)2

2 , and this is why we see no entry equal to 1 in the column of Table 1 corresponding to √2qk

−+1.

In the case s = +1, the pattern is not so easy to guess, although it seems to grow quadratically with k. Surprisingly, typing the numbers 6,14,25,40,58 into the On-Line Encyclopedia of Integer Sequences [27] returns precisely one hit, which reveals that our numerical approximation of q+(k) agrees for k ∈ {3,4,5,6,7} with

(k−1)2ϕ k⩾3 = 6,14,25,40,58,79,103,131,161,195,..., (6.1) where ϕ = 1+

√5 2 denotes the golden ratio. Unfortunately, this coincidence stops at k = 7, and from then

onwards our numerical value of q+(k) seems to be slightly larger than that of (6.1). One might still conjecture

that q+(k) = ⌊(k−1)2ϕ⌋+o(k) which would show, under Conjecture 3.4, that A+(1) = (2ϕ)−12 = 0.5558... A least squares fit for the data shows that actually q+(k) ≈ 0.882−3.348k+1.65k2, which under Conjecture 3.4 suggests that

###### A+(1) ≈ 0.550.

However we can derive a more reliable upper bound for A+(1) by exploiting monotonicity. Noting that (k,q) is +-feasible for any q in the interval q+(k) ⩽ q < q+(k+1), we can look at the function v(k) = √ k

2q∗+(k)+1,

where q∗+(k) = ⌊q+(k)+q+2(k+1)−1⌋. This function is decreasing for 3 ⩽ k ⩽ 67; see Figure 1. If v(k) is decreasing for all k ⩾ 3, then from this and Conjecture 3.4 it would follow that

###### A+(1) < v(68) = 0.5548... < 0.555,

###### as predicted by Conjecture 1.7. In particular, this rules out the aforementioned relation between A+(1) and the golden ratio.

0.58

0.55

35 67

Figure 1: This is a plot of the function v(k) = √ k

.

2q+(k+1)−1

The most outstanding feature of our numerics is the possibility that a minimizer for A+(1) vanishes identically in certain intervals; see Figure 2. The first author together with Henry Cohn and David de Laat have unpublished numerical data in strong support of an upper bound for A+(1) which starts with 0.558... The function attaining the latter bound is a polynomial multiple of a Gaussian, and exhibits a shape which is

remarkably akin to the plot in Figure 2; in particular, it appears to vanish identically in similar intervals. It is worth pointing out that, since qs(k) seems to grow quadratically with k, the error of k(2qs(k)+1)− of the order O(k−1). Therefore, in order to obtain a 3-digit approximation of the limit of k(2qs(k)+1)− as k → ∞, one would have to set k ≈ 103 and run several linear programs with q ≈ 106, which lies at the computational limit of what the current best linear programming solvers can accomplish in a reasonable time frame. For some reason which is unclear to us, the +1 uncertainty principle consistently seems to be computationally harder than the −1 uncertainty principle.

- 1

- 2 is


- 1

- 2,


1 2 3 4 5 6 7 8 9 10 11 12

q n=0

Figure 2: This is a plot of the sequence √2 nq+1, f(n)

, where f is an optimal answer to Problem 3.1 in

the case s = +1 with kf = 68 and q = 7401. Moreover, this vector satisfies f = f, f(0) = 0, and has minimal energy ∑7401n=68 f(n)2. One can only wonder whether the flatter areas in the plot indicate that minimizers for A+(1) may vanish identically in certain intervals.

|k 3|q− √2qk +1<br><br>−<br><br>3 1.3339|q+ √2qk +1<br><br>+<br><br>6 0.8321| |k 25|q− √2qk +1<br><br>−<br><br>288 1.0408|q+ √2qk +1<br><br>+<br><br>948 0.5740| |k 47|q− √2qk +1<br><br>−<br><br>1058 1.0215|q+ √2qk +1<br><br>+<br><br>3488 0.5627|
|---|---|---|---|---|---|---|---|---|---|---|
|4|5 1.2060|14 0.7428| |26|313 1.0383|1029 0.5730| |48|1105 1.0208|3641 0.5625|
|5|8 1.2127|25 0.7001| |27|338 1.0377|1113 0.5721| |49|1152 1.0206|3798 0.5622|
|6|13 1.1547|40 0.6667| |28|365 1.0356|1200 0.5714| |50|1201 1.0200|3958 0.5619|
|7|18 1.1508|58 0.6472| |29|392 1.0351|1291 0.5706| |51|1250 1.0198|4121 0.5617|
|8|25 1.1202|80 0.6305| |30|421 1.0333|1385 0.5699| |52|1301 1.0192|4287 0.5615|
|9|32 1.1163|104 0.6225| |31|450 1.0328|1482 0.5693| |53|1352 1.0190|4457 0.5613|
|10|41 1.0976|133 0.6120| |32|481 1.0312|1583 0.5686| |54|1405 1.0185|4630 0.5611|
|11|50 1.0945|164 0.6064| |33|512 1.0307|1687 0.5680| |55|1458 1.0183|4807 0.5609|
|12|61 1.0820|198 0.6023| |34|545 1.0294|1794 0.5675| |56|1513 1.0178|4987 0.5607|
|13|72 1.0796|236 0.5977| |35|578 1.0290|1904 0.5671| |57|1568 1.0177|5170 0.5605|
|14|85 1.0706|277 0.5943| |36|613 1.0277|2018 0.5666| |58|1625 1.0172|5356 0.5604|
|15|98 1.0687|322 0.5906| |37|648 1.0274|2135 0.5662| |59|1682 1.0171|5546 0.5602|
|16|113 1.0620|370 0.5878| |38|685 1.0263|2256 0.5657| |60|1741 1.0167|5738 0.5601|
|17|128 1.0604|420 0.5862| |39|722 1.0260|2379 0.5653| |61|1800 1.0165|5935 0.5599|
|18|145 1.0552|475 0.5837| |40|761 1.0250|2506 0.5650| |62|1861 1.0161|6134 0.5597|
|19|162 1.0539|533 0.5817| |41|800 1.0247|2637 0.5645| |63|1922 1.0160|6337 0.5596|
|20|181 1.0497|594 0.5800| |42|841 1.0238|2770 0.5642| |64|1985 1.0156|6543 0.5594|
|21|200 1.0487|658 0.5787| |43|882 1.0235|2907 0.5639| |65|2048 1.0155|6753 0.5593|
|22|221 1.0453|726 0.5772| |44|925 1.0227|3047 0.5636| |66|2113 1.0151|6965 0.5592|
|23|242 1.0444|797 0.5759| |45|968 1.0225|3191 0.5632| |67|2178 1.0150|7182 0.5590|
|24|265 1.0415|871 0.5749| |46|1013 1.0217|3337 0.5630| |68|2245 1.0147|7401 0.5589|


Table 1: The table displays pairs (k,q−),(k,q+) which are numerically −1- and +1-feasible, respectively. Recall that, according to Definition 3.2, a pair (k,q) is s-feasible if there exists f ∈ Adiscs (q), such that ksf ⩽ k. We produced this table using Gurobi [24] and PARI/GP [4]. We have checked numerically that, for any given pair (k,q±) from the table, the pairs (k′,qs),(k,q′s) are always s-feasible, for any k′ ⩾ k and q′s ⩽ qs. We also verified numerically that the set of integers q, for which (k,q) is s-feasible but (k−1,q) is not, coincides with the interval [qs(k),qs(k+1)−1], where k  → qs(k) is the function given by the table. Thus the table seems to indeed record the jumps of the function q  → Adiscs (q).

1 2 3 4 5 6 7 8

q n=0

Figure 3: There are two plots. The one in blue corresponds to a plot of the sequence √2 nq+1, f(n)

, where f is an optimal answer to Problem 3.1 in the case s = −1 with k−f = 120 and q = (k−f −1)2/2 = 7081. Moreover, this vector satisfies f = −f, f(0) = 0, and has minimal energy ∑7081n=120 f(n)2. This plot almost matches the plot of the function f⋆(x) = sin(2π|x|)1[−1,1](x)− 2sin

2(πx)

π(1−x2) (in black) which was included for comparison.

###### 6.2 Discrete Hankel Transform

Tables 2 and 3 display numerical data16 relative to the sign uncertainty principles for the discrete Hankel transform. For each sign s ∈ {+,−}, dimension d, and parameter k, the pair (k,qs) is numerically (s, d2 −1)feasible, in the sense of Definition 3.8. We used floating-point arithmetic, and therefore we cannot claim these numbers to be correct in the theoretical sense, but we believe they are. We have checked numerically that, for any given pair (k,qs) in these tables, the pairs (k′,qs),(k,q′s) are always s-feasible, for any k′ ⩾ k and q′s ⩽ qs. We have also numerically verified that the set of integers q, for which (k,q) is (s, d2 −1)-feasible but (k−1,q) is not, coincides with the interval [qs(k;d),qs(k+1;d)−1], where k  → qs(k;d) denotes the function given by Tables 2 and 3. Hence these tables seem to record the jumps of the function q  → Adiscs (q, d2 −1).

It does not seem easy to detect any distinguishable patterns in the entries of Tables 2 and 3, except for the special cases d ∈ {2,8,24} when s = −1, and d = 12 when s = +1. In these cases, one can indeed spot a pattern in the first few entries of the corresponding columns, which in turn motivated Conjecture 3.10. If

16The main reason to display Tables 2, 3 in full is that it might be possible to spot certain numerical patterns and thus produce conjectures towards the continuous sign uncertainty constants As(d) for dimensions other than d ∈ {1,2,8,12,24}.

(s,d) = (−,2), then the sequence

√3(k2 −2k+2) 4

= 4,7,11,16,21,28,35,43,52,62,... (6.2)

k⩾4

matches the data from Table 2 for k ∈ {4,5,6,7,8}, and seems to be slightly below the values from that table if k > 8. In particular, this means that k,⌊

√3(k2−2k+2)

4 ⌋ should be (s,2/1−1)-feasible, for all k ⩾ 4. Similarly, if (s,d) = (−,8),(−,24),(+,12) respectively, then the data match the sequences17

k2 4 k⩾4

= 4,6,9,12,16,20,25,30,36,42,..., k2 +6k−8

= 4,5,8,10,13,15,19,22,26,29,..., k2 +2k−1

(6.3)

8 k⩾4

= 3,5,8,11,15,19,24,29,35,41,...,

4 k⩾3

for k ∈ {4,5,6,7,8,9,10,11,12}, k ∈ {4,5,6,7,8}, and k ∈ {3,4,5,6,7,8,9,10,11}.

Similarly to what was already observed in §6.1, the +1 problem seems to be computationally harder than the −1 problem. Nevertheless, one can check that the sequences in (6.2) and (6.3) always belong to the interval (qs(k−1;d),qs(k;d)] for k ⩽ 30 and (s,d) ∈ {(−,2),(−,8),(−,24),(+,12)}, respectively. This means that k−1 coincides with the quantities

√3(k2 −2k+2) 4

k2 4

2 2 −1 , Adisc−

8 2 −1 ,

Adisc−

,

,

k2 +6k−8 8

k2 +2k−1 4

24 2 −1 , Adisc+

12

Adisc−

2 −1 , and provides further evidence towards Conjecture 3.10.

,

,

17From the available data, one could try to look for a best-fitting quadratic polynomial whose floor function agrees with the data for many more values of k. Our choice was the simplest one among those with rational coefficients and small denominators.

|23456789101112131415161718192021222324|44444444444444444444444<br><br>77776666666666555555555<br><br>119999998888888888888888<br><br>1615151413131212111111111111111111111111111110<br><br>2119181717161615151515141414141414141414141313<br><br>2927252322212020191919181818181717171717171716<br><br>3531292827262524242323232222222121212120202020<br><br>4541383533313030292827272626262525252524242424<br><br>5347434139383635343333323131303029292928282828<br><br>6458534946444341403938373636353534333333323232<br><br>7465605754524948464544434241404039383837373636<br><br>8779726662595755535250494847464544444342424141<br><br>9887807571686562605857555453525150494848474646<br><br>114102938580767370686664626159585756555453525251<br><br>1261111029690868279767371696766646362616059585756<br><br>143129117107101969188848179777573717068676665646362<br><br>15713912811911210610197939087858280787775747271706968<br><br>1771581431321241171121071039996939088868482817978767574<br><br>1921691551451361291231171131081051029996949290888685838280<br><br>2131911731591491411341281231181141111081051029997959492908987<br><br>23120318617316215314613913412912412011711311110810510310199979694<br><br>254227205188176166158151145139134130126122119116114111109107105103101<br><br>272240220204191180171163156150145140136132128125122120117115112111109<br><br>297266239220206194184176168162156151146142138134131128126123121118116<br><br>318280256237222209198189181174167162157152148144140137134132129127124<br><br>344308277255238224213203194186179173168163158154150147143140138135133<br><br>367323295273255240228217207199191185179173168164160156153149146144141<br><br>|
|---|---|
|k d|4<br><br>5<br><br>6<br><br>7<br><br>8<br><br>9<br><br>10<br><br>11<br><br>12<br><br>13<br><br>14<br><br>15<br><br>16<br><br>17<br><br>18<br><br>19<br><br>20<br><br>21<br><br>22<br><br>23<br><br>24<br><br>25<br><br>26<br><br>27<br><br>28<br><br>29<br><br>30|


26122119116114111109107105103101

36132128125122120117115112111109

46142138134131128126123121118116

57152148144140137134132129127124

68163158154150147143140138135133

79173168164160156153149146144141

111111111111111111110

414141414141414141313

818181717171717171716

222222121212120202020

626262525252524242424

131303029292928282828

636353534333333323232

241404039383837373636

847464544444342424141

453525150494848474646

415161718192021222324

088868482817978767574

996949290888685838280

573717068676665646362

280787775747271706968

081051029997959492908987

1711311110810510310199979694

159585756555453525251

766646362616059585756

88888888888

44444444444

66555555555

dTable2:NumericaldataforthediscreteHankeltransform1uncertaintyprinciple.Ifqisanentryinthetable,thenkqisnumerically11-feasible.−−−(,)(,)−−2

TheGurobisolver[24]wasusedwithPARI/GP[4]asinterface.

|23456789101112131415161718192021222324|33333333333333333333333<br><br>97766665555555555555554<br><br>14121099888888877777777777<br><br>2418161514131212121111111110101010101010101010<br><br>3324211918171716161515151414141413131313131313<br><br>4635302724232221202019191818181817171717161616<br><br>5842363331292827262524232322222221212121202020<br><br>7556484239363433313029292827272626252525242424<br><br>9066565147444240383735343333323131303029292828<br><br>11182706156525047454342403938373736353534333332<br><br>12994807266625855535049474644434241404039393837<br><br>153114978577726764615856545251504847464544444343<br><br>1751271099789837773706664626058565554525150494848<br><br>203150128111102948883797572696765636260595856555454<br><br>2291661411261151069993898581787573716967656463626160<br><br>260192163142129119111105999590878481797775737169686766<br><br>289209178159144133124116110105100969390878482807877757472<br><br>32423820217716014713712912211611110610299969390888684828179<br><br>35525822019517716315114213412712211711210810510299969492908886<br><br>395290245215194179166155147139133127122118114111108105102100979694<br><br>430311265235213195181170160152145139133128124120117114111108106103101<br><br>472347293257232213197185174165157150145139134130126123120117114112109<br><br>511370315279252231214200188179170163156150145140136133129126123120118<br><br>558409345302273250231216204193183175168162156151147142139135132129126<br><br>600434369326294269249233219207197188181174168162157153149145141138135<br><br>649476401352317290268250235223212202194186180174168163159155151148144<br><br>695503427378340311288268252238227216207199192186179174170165161157154<br><br>748548462405364333308287270255242231221212205198191186181176171167163<br><br>|
|---|---|
|k d|3<br><br>4<br><br>5<br><br>6<br><br>7<br><br>8<br><br>9<br><br>10<br><br>11<br><br>12<br><br>13<br><br>14<br><br>15<br><br>16<br><br>17<br><br>18<br><br>19<br><br>20<br><br>21<br><br>22<br><br>23<br><br>24<br><br>25<br><br>26<br><br>27<br><br>28<br><br>29<br><br>30|


128124120117114111108106103101

139134130126123120117114112109

150145140136133129126123120118

162156151147142139135132129126

174168162157153149145141138135

186180174168163159155151148144

199192186179174170165161157154

212205198191186181176171167163

10101010101010101010

14141413131313131313

18181817171717161616

22222221212121202020

27272626252525242424

33323131303029292828

15161718192021222324

90878482807877757472

99969390888684828179

10810510299969492908886

38373736353534333332

44434241404039393837

65636260595856555454

73716967656463626160

81797775737169686766

118114111108105102100979694

51504847464544444343

58565554525150494848

7777777777

3333333333

5555555554

dTable3:Ifqisanentryinthetable,thenkqisnumerically11-feasible.−(,)(+,)++2

#### Acknowledgments

The authors are grateful to Henry Cohn, David de Laat, and Danylo Radchenko for helpful discussions, and to the anonymous referee for a careful reading and valuable suggestions.

#### References

- [1] E. BANNAI AND E. BANNAI, A survey on spherical designs and algebraic combinatorics on spheres. European J. Combin. 30 (2009), no. 6, 1392–1425. 12
- [2] E. BANNAI AND R. M. DAMERELL, Tight spherical designs. I. J. Math. Soc. Japan 31 (1979), 199–207. 12
- [3] E. BANNAI AND R. M. DAMERELL, Tight spherical designs. II. J. London Math. Soc. 21 (1980), 13–30. 12
- [4] C. BATUT, K. BELABAS, D. BENARDI, H. COHEN, AND M. OLIVIER, User’s Guide to PARI-GP, version 2.11.1 (2018). 23, 39, 42
- [5] J. BOURGAIN, L. CLOZEL, AND J.-P. KAHANE, Principe d’Heisenberg et fonctions positives. Ann. Inst. Fourier (Grenoble) 60 (2010), no. 4, 1215–1232. 2, 3, 6, 8
- [6] E. CARNEIRO, M. B. MILINOVICH, AND K. SOUNDARARAJAN, Fourier optimization and prime gaps. Comment. Math. Helv. 94 (2019), no. 3, 533–568. 8
- [7] N. AFKHAMI-JEDDI, H. COHN, T. HARTMAN, D. DE LAAT, AND A. TAJDINI, High-dimensional sphere packing and the modular bootstrap, J. High Energ. Phys. 2020, 66 (2020). 8
- [8] H. COHN AND N. ELKIES, New upper bounds on sphere packings I. Ann. of Math. (2) 157 (2003), no. 2, 689–714. 2, 6, 7
- [9] H. COHN AND F. GONÇALVES, An optimal uncertainty principle in twelve dimensions via modular forms. Invent. Math. 217 (2019), no. 3, 799–831. 2, 3, 6, 7, 8, 11
- [10] H. COHN AND A. KUMAR, Universally optimal distribution of points on spheres. J. Amer. Math. Soc. 20 (2007), no. 1, 99–148. 12, 35
- [11] H. COHN, A. KUMAR, S. MILLER, D. RADCHENKO, AND M. VIAZOVSKA, The sphere packing problem in dimension 24. Ann. of Math. (2) 185 (2017), no. 3, 1017–1033. 7, 11
- [12] H. COHN AND Y. ZHAO, Sphere packing bounds via spherical codes. Duke Math. J. 163 (2014), no. 10, 1965–2002. 8


- [13] F. DAI AND Y. XU, Approximation theory and harmonic analysis on spheres and balls. Springer Monographs in Mathematics. Springer, New York, 2013. 32
- [14] P. DELSARTE, J. M. GOETHALS, AND J. J. SEIDEL, Spherical codes and designs. Geom. Dedicata 6

(1977), 363–388. 12, 16

- [15] H. FISK JOHNSON, An improved method for computing a discrete Hankel transform. Comput. Phys. Comm. 43 (1987), no. 2, 181–202. 24, 25
- [16] G. B. FOLLAND AND A. SITARAM, The uncertainty principle: a mathematical survey. J. Fourier Anal. Appl. 3 (1997), no. 3, 207–238. 2
- [17] G. GASPER, Linearization of the product of Jacobi polynomials. I. Canadian J. Math. 22 (1970), no. 1, 171–175. 35
- [18] F. GONÇALVES, D. OLIVEIRA E SILVA, AND J. P. G. RAMOS, On regularity and mass concentration phenomena for the sign uncertainty principle. J. Geom. Anal. 31 (2021), no. 6, 6080–6101. 8, 19
- [19] F. GONÇALVES, D. OLIVEIRA E SILVA, AND S. STEINERBERGER, Hermite polynomials, linear flows on the torus, and an uncertainty principle for roots. J. Math. Anal. Appl. 451 (2017), no. 2, 678–711. 6, 8
- [20] F. GONÇALVES, D. OLIVEIRA E SILVA, AND S. STEINERBERGER, A universality law for sign correlations of eigenfunctions of differential operators. J. Spectr. Theory (2021), 1–16, DOI 10.4171/JST/351. 8
- [21] D. V. GORBACHEV, V. I. IVANOV, AND S. YU. TIKHONOV, Uncertainty principles for eventually constant sign bandlimited functions. SIAM J. Math. Anal. 52 (2020), no. 5, 4751–4782. 8
- [22] L. GRAFAKOS, Classical Fourier analysis. Second edition. Graduate Texts in Mathematics, 249. Springer, New York, 2008. 19, 29
- [23] T. C. HALES, Cannonballs and honeycombs. Notices Amer. Math. Soc. 47 (2000), no. 4, 440–449. 7
- [24] GUROBI OPTIMIZATION, LLC, Gurobi Optimizer Reference Manual (2020). 23, 39, 42
- [25] G. A. KABATIANSKY AND V. I. LEVENSHTEIN, Bounds for packings on a sphere and in space (in Russian). Problemy Peredachi Informacii 14 (1978), 3–25; English translation in Probl. Inf. Transm. 14

(1978), 1–17. 8

- [26] D. OLIVEIRA E SILVA AND C. THIELE, Estimates for certain integrals of products of six Bessel functions. Rev. Mat. Iberoam. 33 (2017), no. 4, 1423–1462. 21
- [27] On-Line Encyclopedia of Integer Sequences. https://oeis.org. 36


- [28] S. K. PICHORIDES, On the best values of the constants in the theorems of M. Riesz, Zygmund and Kolmogorov. Studia Math. 44 (1972), 165–179. 28
- [29] H. ROBBINS, A remark on Stirling’s formula. Amer. Math. Monthly 62 (1955), 26–29. 34
- [30] W. RUDIN, Fourier analysis on groups. Interscience Tracts in Pure and Applied Math., no. 12. Wiley, New York, 1962. 28
- [31] G. SZEGÖ, Orthogonal polynomials. Fourth edition. American Mathematical Society, Colloquium Publications, Vol. XXIII. American Mathematical Society, Providence, R.I., 1975. 14, 15, 16, 33, 34
- [32] E. C. TITCHMARSH, Introduction to the Theory of Fourier Integrals. Chelsea Publishing Co., New York, 1986. 29
- [33] M. VIAZOVSKA, The sphere packing problem in dimension 8. Ann. of Math. (2) 185 (2017), no. 3, 991–1015. 6, 7, 11
- [34] G. N. WATSON, A Treatise on the Theory of Bessel Functions. Cambridge University Press, Cambridge,


1966. 20, 21

###### AUTHORS

Felipe Gonçalves Instituto Nacional de Matemática Pura e Aplicada Rio de Janeiro, Brazil goncalves impa br https://w3.impa.br/%7Egoncalves/index.html

![image 1](<2020-gonalves-new-sign-uncertainty-principles_images/imageFile1.png>)

![image 2](<2020-gonalves-new-sign-uncertainty-principles_images/imageFile2.png>)

Diogo Oliveira e Silva Instituto Superior Técnico Lisboa, Portugal diogo.oliveira.e.silva tecnico ulisboa pt https://www.math.tecnico.ulisboa.pt/~oliveiraesilva/

![image 3](<2020-gonalves-new-sign-uncertainty-principles_images/imageFile3.png>)

![image 4](<2020-gonalves-new-sign-uncertainty-principles_images/imageFile4.png>)

![image 5](<2020-gonalves-new-sign-uncertainty-principles_images/imageFile5.png>)

João P. G. Ramos Eidgenössische Technische Hochschule Zürich, Switzerland joao.ramos math ethz ch https://sites.google.com/view/gionnoramos/

![image 6](<2020-gonalves-new-sign-uncertainty-principles_images/imageFile6.png>)

![image 7](<2020-gonalves-new-sign-uncertainty-principles_images/imageFile7.png>)

![image 8](<2020-gonalves-new-sign-uncertainty-principles_images/imageFile8.png>)

