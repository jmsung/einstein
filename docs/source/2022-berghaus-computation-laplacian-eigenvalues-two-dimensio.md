---
type: source
kind: paper
title: Computation of Laplacian eigenvalues of two-dimensional shapes with dihedral symmetry
authors: David Berghaus, Robert Stephen Jones, Hartmut Monien, Danylo Radchenko
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2210.13229v1
source_local: ../raw/2022-berghaus-computation-laplacian-eigenvalues-two-dimensio.pdf
topic: general-knowledge
cites:
---

#### arXiv:2210.13229v1[math.NA]24Oct2022

##### COMPUTATION OF LAPLACIAN EIGENVALUES OF TWO-DIMENSIONAL SHAPES WITH DIHEDRAL SYMMETRY

DAVID BERGHAUS, ROBERT STEPHEN JONES, HARTMUT MONIEN, AND DANYLO RADCHENKO

Abstract. We numerically compute the lowest Laplacian eigenvalues of several twodimensional shapes with dihedral symmetry at arbitrary precision arithmetic. Our approach is based on the method of particular solutions with domain decomposition. We are particularly interested in asymptotic expansions of the eigenvalues λ(n) of shapes with

n edges that are of the form λ(n) ∼ x ∞k=0 C

k(x)

nk where x is the limiting eigenvalue for n → ∞. Expansions of this form have previously only been known for regular polygons with Dirichlet boundary condition and (quite surprisingly) involve Riemann zeta values and single-valued multiple zeta values, which makes them interesting to study. We provide numerical evidence for closed-form expressions of higher order Ck(x) and give more examples of shapes for which such expansions are possible (including regular polygons with Neumann boundary condition, regular star polygons and star shapes with sinusoidal boundary).

1. Introduction

Let Ψ be a function deﬁned on a domain Ω ⊂ R2 that satisﬁes the Laplace eigenvalue equation

- (1.1) − ∆Ψ(x,y) = λ · Ψ(x,y),

where ∆ = ∂x2+∂y2 denotes the Laplacian in two-dimensional Euclidean space and λ ∈ R. We consider the case when the two-dimensional shape Ω has the symmetry group of a regular n-gon, and Ψ has either Dirichlet or Neumann boundary condition on ∂Ω

Ψ|∂Ω = 0 (Dirichlet), ∂ nΨ|∂Ω = 0 (Neumann),

where ∂ n denotes the normal derivative. By combining Eq. (1.1) with the boundary condition, one obtains a discrete spectrum of eigenvalues

0 < λ1 ≤ λ2 ≤ λ3 ≤ ... ,

(in the case of Neumann boundary condition we additionally have λ0 = 0). The eigenvalues are invariant under translations and rotations but do depend on the area of the considered shape. More precisely, if Ω is obtained from Ω by a homothety, then one has

- (1.2) λi(Ω)A(Ω) = λi(Ω )A(Ω ),


where A denotes the area of the corresponding shape. Keeping the area constant is therefore crucial for investigating 1/n expansions. Throughout this paper, we will always normalize the domains to have area π, which means that the shapes will approach the unit disk in the limit as n → ∞.

We start by considering regular polygons with Dirichlet boundary condition. Additional examples will be introduced in Section 7. There are so far only two regular polygons whose eigenvalues are known explicitly. These are the regular triangle where λ1 = 4π/√3 and the square with λ1 = 2π, see, e.g., Po´lya and Szego¨ [32] (one should however mention that some eigenmodes of the regular hexagon can be obtained by piecing together eigenmodes of regular triangles). The remaining regular polygons oﬀer challenges, both analytically and numerically, due to the presence of non-analytic vertices (i.e. vertices that are not of the

1

form π/n). It has been known from works of several authors [2,7,18,25,30] that the lowest eigenvalue of a regular n-gon with Dirichlet boundary condition can be approximated by a series in 1/n

∞

Ck(x) nk

- (1.3) λ1(n) ∼ x


,

k=0

where x = j02,1 is the liming eigenvalue (i.e., the lowest eigenvalue of the unit disk, which is given by the square of the ﬁrst root of the Bessel function J0(x)). Since regular polygons are approaching the circle in the limit, it is natural that C0 = 1. Interestingly, the remaining coeﬃcients seemed to be expressible in closed-form as polynomials in x = j02,1 of degree

i−3

2 with coeﬃcients expressible in terms of Riemann zeta values C0(x) = 1, C1(x) = 0, C2(x) = 0, C3(x) = 4ζ(3), C4(x) = 0, C5(x) = ζ(5)(−2x + 12), C6(x) = ζ(3)2(4x + 8), C7(x) = ζ(7)(−12x2 − 12x + 36), C8(x) = ζ(3)ζ(5)(2x2 + 8x + 48).

The ﬁrst coeﬃcients up to third order have been discovered by Grinfeld and Strang [18] in 2012 through deforming the circle to a regular polygon and then applying a technique called calculus of moving surfaces. Three years later, Boady in his PhD thesis [7] managed to compute two more terms also using methods from the calculus of moving surfaces. The seventh and eighth coeﬃcients were recently found by the second author [25] using numerical methods similar to the ones presented in this report.

We managed to obtain eight higher order coeﬃcients in this project C9(x) = ζ(9)(94x3 + 104x2 + 438x − 1020) + ζ(3)3(240x + 96),

- C10(x) = ζ(7)ζ(3)(x3 + 39x2 − 24x + 144) + ζ(5)2(x3 − 6x2 − 12x + 72),
- C11(x) = ζ(11)(−325 x4 − 66160 x3 − 162320 x2 − 176x + 372)

+ ζ(5)ζ(3)2(80x2 + 176x + 96) + ζsv(3,5,3)(15x3 + 545 x2),

- C12(x) = ζ(9)ζ(3)(58x4 + 1073 x3 + 456x2 − 4883 x + 13603 )

+ ζ(7)ζ(5)(118 x4 + 472 x3 − 207x2 − 216x + 432) + ζ(3)4(−16x2 + 2723 x + 323 ),

- C13(x) = ζ(13)(−647 x5 − 22650116800 x4 − 12838398400 x3 − 14473931400 x2 − 618x + 1260)


+ ζ(7)ζ(3)2(x4 + 34x3 + 1236x2 + 336x + 288)

+ ζ(5)2ζ(3)(−3110x4 + 2565 x3 − 11285 x2 + 336x + 288)

+ ζsv(5,3,5)(−1400157 x4 − 350549x3 − 12339175 x2)

+ ζsv(3,7,3)(−565 x4 − 5928x3 − 74714 x2).

(The expressions of the coeﬃcients C14(x), C15(x), and C16(x) are given in the Appendix, the numerical expressions as well as the underlying eigenvalue data are provided as an attachment to this paper). In order to determine these expressions we computed the eigenvalues of 650 n-gons to at least 980 digits precision. Through this we also discovered the appearance of single-valued multiple zeta values (MZVs) in the expansion coeﬃcients,

α/2

∂Ω1

β/2

∂Ω3 ∂Ω2

∂Ω1 ∂Ω2

α/2

·

### β/2 ·

∂Ω3

Figure 1. Fundamental region of regular polygons for fully symmetric eigenfunctions

starting at eleventh order. In case of C16(x) the basis of single-valued multiple zeta values was found with help of the program HyperlogProcedures developed by Oliver Schnetz. We provide a brief introduction to MZVs and the deﬁnitions of the single-valued MZVs that appear in our expressions in the Appendix. We should note that the approach used in this paper does not produce explicitly proven results but rather gives conjectures with very high numerical evidence. We did however manage to prove some of the results for regular polygons with Dirichlet boundary condition in the companion paper [2]. Namely, we explicitly derived the results up to (and including) C14 and proved that that the expansion coeﬃcients are expressions over the space of multiple zeta values. However, the expressions for C15 and C16 can only be considered conjectural at this point.

2. The Method of Particular Solutions

Because the eigenfunctions considered in this work are dihedrally symmetric, it is suﬃcient to compute them inside a triangular subdomain (which we refer to as fundamental domain) instead of working with the full shape (see Fig. 1 for an illustration of the fundamental domain for a regular polygon). A numerical method for computing eigenvalues of triangular shapes is given by the method of particular solutions (MPS). The MPS has been introduced by Conway [10] in 1961 and established by a famous paper of Fox, Henrici and Moler [16] in 1966 on computing eigenvalues of L-shape domains.

√

The main idea of the MPS is to expand Ψ for the spectral parameter k =

λ as a Fourier-Bessel series (in polar coordinates)

- (2.1) Ψ(k,r,θ) =


cνψν(k,r,θ), where

ν=1

sin(mνθ) | Odd eigenfunctions, cos(mνθ) | Even eigenfunctions,

(k · r) ·

- (2.2) ψν(k,r,θ) = Jm


ν

and Jm denotes the Bessel function (see for example [35]). The basis functions ψν have the useful property that they can serve as eigenfunctions along an unbounded wedge by a wellmade choice of mν. Consider for example a wedge with angle α with the vertex at the origin. Dirichlet boundary conditions impose that the function has to vanish along the boundary. If

one chooses mν = νπ/α for the odd eigenfunction basis, one obtains functions that trivially fulﬁll the boundary condition along both edges of the wedge. This property (combined with the exponential decay of the basis functions) makes the MPS very useful when computing eigenvalues of triangular shapes: the boundary condition on two of the three edges can be trivially fulﬁlled by the construction of ψν. To obtain the spectral parameter k one truncates the expansion of Ψ to some ﬁnite order N and searches for the parameter k for which the expansion vanishes on a discrete set of points on the remaining edge up to the desired numerical precision (this approach is often referred to as point-matching). This results in a linear system of equations

 

  ·

 

  =

 

  ,

ψ1(k,r1,θ1) ... ψN(k,r1,θ1)

c1 . cN

0 . 0

... . ψ1(k,rN,θN) ... ψN(k,rN,θN)

.

which is square if the number of point-matching points is also chosen to be N. The parameter k now corresponds to an approximation of the true spectral parameter if the coeﬃcients are essentially invariant under the choice of matching points. In view of this, one computes the value of k for which the determinant becomes zero (i.e., when the matrix becomes singular) using root-ﬁnding algorithms (we used the secant method) [16]. By increasing N, one can obtain better approximations and hence better precision for the eigenvalue.

This approach has been applied by the second author [24, 25] who expanded from the vertex with angle β/2 (see Fig. 1) and applied point-matching to the edge ∂Ω2 to compute eigenvalues of polygons with n ≤ 150 to 50 digits of precision. We remark that the MPS has the limitation that the point-matching matrix becomes ill-conditioned for large N. This has been further analyzed by Betcke and Trefethen [4,5] in 2005 who proposed an improved approach that is referred to as modiﬁed MPS. Their main idea has been to compute an additional matrix that consists of (randomly chosen) points in the interior of the considered region. This matrix is designed to ensure that the eigenfunction is non-zero in the interior. By minimizing the lowest generalized singular value of these two matrices, one can reliably locate the eigenvalues of a given shape because spurious solutions are excluded and N can be chosen as required, without conditioning the matrix too poorly. The modiﬁed MPS might be regarded as a successor of the MPS and is superior in most applications. For the computation of eigenvalues of relatively simple shapes at arbitrary precision arithmetic, the original MPS can however still prove itself to be very competitive because the ill-conditioning can be overcome by increasing the working precision and because the generalized singular value decomposition is very computationally expensive compared to the LU-decomposition that is required for the determinant computation. Additionally, the function of the determinant w.r.t. k becomes almost linear close to the eigenvalues which makes the location of the roots very eﬃcient [24].

We further remark that recent progress has been achieved in making the results of the MPS rigorous (i.e., with certiﬁed error bounds) [11,20]. For our application, certifying the eigenvalues yields no beneﬁt because the derivation of the closed-form expressions using the LLL algorithm is non-rigorous (unless one knows a bound of the height of the coeﬃcients in advance, which we are unaware of). Additionally, speciﬁcally certifying the eigenvalues results in a loss of precision.

3. Domain Decomposition

Despite the absolute convergence of the MPS (i.e., one always gets better estimates by increasing N as long as the working precision is suﬃciently increased) the algorithm which has been applied by the second author in [24,25] has the disadvantage that the convergence rate (which is the eigenvalue precision per amount of matching points) drastically decreases for polygons with more edges (and hence “thinner” fundamental regions). To overcome

- a

- b

- c

- d


Neumann

# I

α/2

- I
- II


α/2 ·

Neumann

∂Ω1 ∂Ω2

d c b a

Neumann

- e

- f

- g


Neumann

# II

β/2 ·

β/2 ·

∂Ω3

Dirichlet

Figure 2. Domain decomposition of the fundamental region

the decrease of precision for polygons with more edges, we used the technique of domain decomposition. Domain decomposition is by no means new in the context of the MPS. The ﬁrst application was done by J. Descloux and M. Tolley [13] in 1983 who decomposed domains into several subdomains Ωk with eigenfunctions fk and minimized the quotient of the functionals

N

|fk − fl|2 + |∇fk − ∇fl|2 ds, and

- (3.1)


k<l Γkl

- (3.2)

N

k=1 Ωk

|fk|2 dxdy ,

where Γkl denote straight intersecting boundaries. This method has been further developed by Driscoll [14] in 1997 to compute eigenmodes of the famous isospectral drums of Gordon, Webb and Wolpert [17]. Betcke [3] in 2006 formulated the method of Descloux and Tolley

- as a GSVD problem which does not require the evaluation of the boundary- and domain integrals.


Our approach is based on the idea to treat the intersection of regions as an additional point-matching condition. We chose to decompose the fundamental region of regular polygons into two regions. Then, instead of minimizing Eq. (3.1), we explicitly matched the eigenfunctions of both regions and their derivatives on a discrete set of points along the intersecting line. We do not claim this approach to be new (in fact it was already mentioned in Driscoll’s paper [14]) however we are unaware of any author proving the success of this method.

4. Outline of the Algorithm

As shown in Fig. 2, the fundamental region can be decomposed into two regions I & II. For the ﬁrst region one chooses the eigenfunctions to be

- (4.1) Ψ[N


I (k,r,θ) = N

I

I]

ν=1

Jm

ν

(k · r) · cos(mνθ),

and expands of the vertex with angle α/2. To fulﬁll the Neumann boundary condition at angle θ = 0 (which is required for fully symmetric eigenmodes), the angular derivative of the wave function (which is a sine with a factor that does not matter here) has to vanish. This is always fulﬁlled since sin(mν · 0) = 0 for all mν. The second Neumann boundary condition is fulﬁlled if sin(mν α2) = 0 from which follows

- (4.2) mν =


2π α

(ν − 1).

Similarly for the second domain one expands from the β/2-vertex (and places it at the origin). We denote this coordinate system with a tilde. The space of eigenfunctions now becomes

- (4.3) Ψ[N

II]

II (k,r,˜ θ˜) = N

II

µ=1

Jm

µ

(k · r˜) · sin(mµθ˜),

with

- (4.4) mµ =


π β

(2µ − 1).

The point-matching matrix now has to treat three diﬀerent boundary conditions:

- (1) The wave functions of both regions have to match along the intersecting line

ΨI(a) =ΨII(a), . ΨI(d) =ΨII(d).

- (2) The normal derivatives of both wave functions have to match along the intersecting line

∂ ∂x

ΨI(a) = −

∂ ∂y˜

ΨII(a)

. ∂ ∂x

ΨI(d) = −

∂ ∂y˜

ΨII(d),

where the minus sign appears because the expansions have opposite orientation along the intersection line. We computed the derivatives explicitly by diﬀerentiating the Bessel and sine functions.

- (3) The outer boundary condition of the second region has to be fulﬁlled


∂ ∂x˜

ΨII(e) =0,

. ∂ ∂x˜

ΨII(g) =0.

90

80

EigenvaluePrecisioninDigits

With Domain Decomposition Without Domain Decomposition

70

60

50

40

30

20

10

0

0 100 200 300 400 500 600 700 800 900 1000

Number of Polygon Edges n

Figure 3. Comparison of the eigenvalue precision for diﬀerent polygons with 200 matching points

All these conditions can then be combined into a point-matching matrix 



−ΨII(a) . −ΨII(d)

ΨI(a) . ΨI(d)

∂

∂

∂y˜ΨII(a) .

∂xΨI(a) .

- (4.5) M =


∂

∂

∂xΨI(d)

∂y˜ΨII(d)

∂

∂x˜ΨII(e) .

 

 

0

∂

∂x˜ΨII(g)

We chose the height of the intersecting line to be equal to the length of ∂Ω3 so that region II becomes close to a square. We have also experimented with diﬀerent ways of decomposition (such as choosing the intersection line crosswise through the region, which eliminates the third point-matching condition), but none of them provided better results than the presented approach. In order to overcome the ill-conditioning of the point-matching matrix we performed the computations with about 1.2N digits working precision where N is the size of the point-matching matrix (this choice was obtained through trial and error, one could also attempt to choose N based on the asymptotic decay of the series, which does however require a growth condition for cν). The points along all boundaries (exterior and interior) were distributed using the Chebyshev distribution. By empirical testing we chose the number of matching points for all three boundary conditions equally to be N/3 each while the ﬁrst eigenfunction is expanded up to NI = N/4 and NII = 3N/4.

The advantage of this approach becomes clear in Fig. 3: the algorithm with domain decomposition is almost unaﬀected by the number of polygon edges n while the original point-matching algorithm without domain decomposition suﬀers from a heavy decrease of the convergence rate for increasing n. This allowed us to compute eigenvalues for hundreds of regular polygons to high precision.

5. Details on the numerical implementation

We implemented the algorithm in the Julia programming language [6]. We made use of Arb [21] and its Julia interface implemented in Nemo [15]. Arb is a highly optimized C library for arbitrary precision arithmetic. We used Arb to evaluate the occurring special functions. Especially the evaluation of Bessel functions is computationally demanding (in fact, most computational time was spent on computing these functions) which makes an eﬃcient implementation very important (see [22] for some benchmarks of Arb’s Bessel implementation). To compute the determinants we used a wrapper to the function arb mat approx lu of Arb which also runs considerably faster than the default Julia determinant algorithm [23]. In general, Arb is designed for interval-arithmetic (which means that every ﬂoat has an error-bound attached so that rounding errors during arithmetic operations are taken into account). However, for our implementation interval-arithmetic is counterproductive because the point-matching matrix is ill-conditioned and empirical tests have revealed that interval-arithmetic might cancel signiﬁcant digits too pessimistically during the determinant computation (as it ensures that the result is correct up to its displayed precision). It is therefore important to note that arb mat approx lu is one of the few functions of Arb where approximate (non-interval) arithmetic is used. The computing cluster

- at which the computation were performed consisted of nodes with 2x Intel Xeon E5-2680 v4 @ 2.40GHz CPUs with 14 (physical) cores each and 128GB of RAM per node. In total, 39 nodes were available. The computations were queued using HTCondor [29] which oﬀers priority-based distribution of hardware resources between multiple users. This means that the hardware was shared with other users which might have increased CPU-times. Each time the determinant of a point-matching matrix has been computed (within the secantmethod) the result (and other signiﬁcant parameters) were stored and the job re-queued. This approach allowed other users to occupy resources as well and the machines to perform required reboots. If however no other user was using the computing cluster, all resources could be used to prevent idle time. The largest computed matrices were of size 3039 × 3039 with 3647 digits precision per entry. The computation of these matrices (and their determinant) required around 45 hours of wall-clock time running on 9 threads (in our latest version we computed the point-matching matrix in parallel and then computed the determinant using Arb). To store such a matrix and compute its determinant, about 20 GB of RAM was needed. The computations took several months and required 2.7 million threadhours in total (the amount of physical core-hours without hyper-threading is impossible to determine).


6. Derivation of the coefficients

To compute the coeﬃcients of the 1/n-expansion, we used Richardson-extrapolation as it is described in [1]. The computed eigenvalues λ(n) for n-sided polygons can be expanded as a series

λ(n) = C0 + C1 · n−1 + C2 · n−2 + ··· + CN · n−N λ(n + 1) = C0 + C1 · (n + 1)−1 + C2 · (n + 1)−2 + ··· + CN · (n + 1)−N

. λ(n + N) = C0 + C1 · (n + N)−1 + C2 · (n + N)−2 + ··· + CN · (n + N)−N

were n is the lowest computed polygon and N is the total amount of computed polygons. Known coeﬃcients were subtracted to increase the precision. This creates a square system of equations which we solved with LU-decomposition to obtain numerical estimates for the coeﬃcients Ci. Using this approach gives higher precision than a standard polynomial ﬁt

- as it was applied in [25]. Still, we were unable to extract the coeﬃcients with nearly the


same precision as the computed eigenvalues. For example for the seventeenth coeﬃcient (for which we could not ﬁnd a closed-form solution) we get a precision of approximately 580 digits while the eigenvalues were computed to at least 980 digits. We tried multiple ways to extract the coeﬃcients with higher precision (for example by trying to exploit the fact that the Richardson matrix is a Vandermonde-matrix (see [12]) or by performing the computations with rational arithmetic to not implement any rounding errors) but none of them yielded in better results.

An empirical observation is that one seems to get the best results by using about 0.65D eigenvalues for the Richardson extrapolation, where D denotes the (estimated) precision of the eigenvalues in digits. This is the reason why we have computed 650 polygons to about 1000 digits precision.

After computing the numerical expressions of the coeﬃcients, we used Pari [34] to ﬁnd closed-form guesses using the LLL-algorithm [28]. For regular polygons with Dirichlet boundary condition, we have also made use of the results of [2], which give closed forms for the coeﬃcients of x0 and x1, to cut down on the search space.

7. Further Examples

- 7.1. Regular Polygons with Neumann Boundary Condition. The presented algorithm works equally well for regular polygons with Neumann boundary condition (one only has to slightly adapt the function space for the second region). We have computed the lowest Laplacian eigenvalue of 455 polygons with Neumann boundary condition to at least 700 digits precision. This computed data provides strong evidence that there is a 1/n-expansion


∞

- (7.1) λ1(n) ∼ j12,1


k=0

Ck(j12,1) nk

for the Neumann case with coeﬃcients (here x = j12,1) C0(x) = 1, C1(x) = 0, C2(x) = 0, C3(x) = 0, C4(x) = 0, C5(x) = −4ζ(5)x, C6(x) = 0, C7(x) = ζ(7)(−2x2 − 22x), C8(x) = 0, C9(x) = ζ(9)(−32x3 − 523 x2 − 2963 x),

- C10(x) = ζ(5)2(2x3 + 16x2),
- C11(x) = ζ(11)(−54x4 − 21512 x3 − 108x2 − 418x),

- C12(x) = ζ(7)ζ(5)(4x4 + 46x3 + 176x2),
- C13(x) = −ζ(13)(3532x5 + 4043150 x4 + 169912 x3 + 590x2 + 1732x) − 485 ζ(5)2ζ(3)x4 − 252 ζsv(5,3,5)x4 ,

- C14(x) = ζ(9)ζ(5)(154 x5 + 8269 x4 + 9203 x3 + 23683 x2)

+ ζ(7)2(94x5 + 18x4 + 3852 x3 + 484x2),

- C15(x) = −ζ(15)(6364x6 − 5439196720 x5 + 1665196118900 x4 + 3355736 x3 + 150145 x2 + 354945 x)


(a) {11,2} (b) {11,3} (c) {11,4} (d) {11,5} Figure 4. Regular star polygons with 11 edges and diﬀerent densities. The ﬁgure was created using a Mathematica package by Michael Schreiber [33].

| | |
|---|---|
| | |


a/4

- II
- III


a/4

α/2I

Figure 5. Domain decomposition of the fundamental region of regular star polygons.

− ζ(5)3(203 x5 + 128815 x4 + 64x3) − (ζsv(5,3,7) + 336ζ(7)ζ(5)ζ(3))(141 x5 − 1335x4), C16(x) = ζ(11)ζ(5)(27x6 + 16993120 x5 + 70885 x4 + 1714x3 + 3344x2)

+ ζ(9)ζ(7)(92x6 + 640972 x5 + 12319 x4 + 68363 x3 + 130243 x2)

+ ζ(5)2ζ(3)2(12x5 − 192x4) + ζsv(3,5,3)ζ(5)(65x5 − 965 x4).

Our results thus indicate that the appearance of single-valued MZVs is not restricted to the Dirichlet eigenvalues (although the results for Neumann boundary condition have not been formally proven yet).

- 7.2. Regular Star Polygons. In order to study whether the expandability of eigenvalues also applies for other polygonal shapes with dihedral symmetry, we have also considered regular star polygons, which are non-convex regular polygons. For convenient labeling, we make use of the Schla¨ﬂi notation: Any star polygon can be labeled as {n,q} where n corresponds to the number of vertices and q ≥ 2 is referred to as the density (see Fig. 4). The numbers q and n are also required to be relatively prime. The fundamental regions


are then given by the triangles with angles (πn, π(n2−n2q), π(n+22nq−2)). One example of a regular star polygon is the pentagram which is labeled as {5,2}. The lowest 79 eigenvalues of this

shape have been computed by the second author [24] to 20 digits of precision. Despite that, we are unaware of any eﬀorts to compute the eigenvalues of these shapes to signiﬁcantly high precision. The reason for that is probably that they are relatively diﬃcult to compute

- at high precision since they contain two non-analytic vertices. In fact, we had to compute expansions using three vertices as shown in Fig. 5. We have computed expansions of the


eigenfunctions in each region to roughly equal orders: NI ≈ NII ≈ NIII ≈ N/3 (we also chose equal numbers of points along each intersection line). The working precision for this triple-expansion approach was chosen to be 0.7N + 50.

We have computed the eigenvalues of star shapes in the case q = 2 with 12 ≤ n ≤ 263 to almost 300 digits precision and in the cases 3 ≤ q ≤ 8 to about 100 digits of precision. We ﬁnd that the expansion coeﬃcients of regular star shapes also involve zeta values and can be written as polynomials in q. For the ﬁrst nine coeﬃcients we conjecture that

C0 = 1,

C1 = 0, C2 = 0, C3 = ζ(3)(14q(q − 1) + 4), C4 = 0, C5 = ζ(5)(62q(q − 1)(q2 − q + 1) + 12 − x · 314 (q2 − q + 318 )), C6 = ζ(3)2(2(7q(q − 1) + 2)2 + x · 634 (q2 − q + 6316)), C7 = ζ(7)(254q(q − 1)(q2 − q + 1)2 + 36) − x · A7q(q − 1)(2q − 1)2

+ x · ζ(7)(80912 q(q − 1)(q2 − q + 1) − 157116 q(q − 1) − 12) − x2 · ζ(7)(12764 q(q − 1) + 12),

C8 = ζ(3)ζ(5)(28q(q − 1) + 8)(31q(q − 1)(q2 − q + 1) + 6)

+ x · ζ(3)ζ(5)(110q(q − 1)(q2 − q + 17695 ) + 8) − x · 28ζ(3)(ζ(2)ζ(3) − 2Li3,1,1(−1,1,1))q(q − 1)(2q − 1)2

+ x2 · ζ(3)ζ(5)(25532 q(q − 1) + 2). Here the number A7 is deﬁned as

A7 = 569 Li2,2,3(−1,−1,−1) + 8Li2,2,3(−1,1,−1) + 7435288 ζ(5,2) + 775144ζ(4,3). Note that these expressions also reproduce the expansion coeﬃcients of regular convex polygons which correspond to q = 1. What seems particularly interesting is that the coeﬃcients C7 and C8 involve alternating multiple zeta values which did not appear in the case of regular polygons.

- 7.3. Smooth Star Shapes. We also investigated the asymptotic expansion of the eigenvalues of shapes with curved vertices which we call smooth star shapes. Smooth star shapes are cycloids with radius


- (7.2) r(θ) = R + d · cos(n · θ)

where n corresponds to the number of arcs, d is the height of an arc and R is the radius of the underlying circle (see Fig. 6). The eigenvalues of these shapes have previously been investigated by Laura in 1964 [27] and Wagner in 1971 [36] who derived the approximate formula

- (7.3) λ(n,d) = c2 · 1 + 0.125 c · (J2(c)/J1(c) + 2(Jn−1(c) − 2Jn+1(c))/Jn(c)) · d2 ,


with c = j0,1. This formula gives an approximation of the eigenvalue at least up to the ﬁrst digit for d = 0.3. Smooth star shapes are relatively easy to construct and have been used to test numerical algorithms for the computation of Laplacian eigenvalues, see for example [9, 19]. In our case, we investigate the behavior of smooth star shape domains with d = (1/n)m where m ∈ N. This choice of radii ensures that the considered shapes have the eigenvalue of the circle as their limiting eigenvalue. To compute the eigenvalues we simply used an expansion from the interior vertex. This might not be the most eﬃcient approach (since the point-matching matrix becomes extremely ill-conditioned) however it was suﬃcient to investigate the ﬁrst terms of the asymptotic expansion. We ﬁnd that the eigenvalues of these (artiﬁcially constructed) shapes can also be written as a 1/n series where the expansion coeﬃcients are now rational polynomials of x = j02,1. For example for m = 2 one obtains the rational polynomials

C0(x) = 1, C1(x) = 0, C2(x) = 0,

R d

| | |
|---|---|
| | |


Figure 6. Smooth Star Shape with n = 5 and d = 0.3

C3(x) = 1, C4(x) = 1/2, C5(x) = −(2x + 1)/4, C6(x) = (2x + 3)/4, C7(x) = −(12x2 + 18x − 119)/96, C8(x) = (48x2 − 75x − 8)/96, C9(x) = −(144x3 + 3393x2 − 84x + 167)/2304,

- C10(x) = (384x3 + 2499x2 + 712x + 1203)/768,
- C11(x) = −(14400x4 + 926100x3 + 2283120x2 + 525440x − 390979)/368640,
- C12(x) = (46080x4 + 933075x3 + 1041030x2 − 95940x − 63551)/92160.


(The remaining coeﬃcients up to C23 as well as the coeﬃcients for m = 3 and m = 4 can be found in Appendix.) We omit the case m = 1 simply for convenience (this case is slightly more diﬃcult to compute to high precision) as we do not expect any substantially diﬀerent behavior.

- 7.4. Hypocycloids. A hypocycloid is the locus of a point on a small circle rotating along the interior of the boundary of a larger circle (see Fig. 7). In case when the ratio between the radii of the larger and smaller circles is an integer n, the resulting hypocycloid has the n-sided dihedral symmetry. Interestingly, these shapes are related to group theory: the traces of all matrices in SU(n) lie inside an n-sided hypocycloid as was shown by Kaiser [26]. Hypocycloids can be parameterized by


- x(θ) = r · (n − 1) · cos(θ) + r · cos((n − 1) · θ)
- y(θ) = r · (n − 1) · sin(θ) − r · sin((n − 1) · θ)


where r = R/n is the radius of the smaller (rotating) circle. In the limit as n → ∞ one thus obtains the parametric equations of a circle of radius R. It seems therefore natural to investigate if the eigenvalues of hypocycloids can be expressed as a 1/n-expansion, similar to what was shown in the previous sections. The vertices of hypocycloids are called cusps, i.e., the internal angle at each vertex is zero. To compute the eigenvalues of a hypocycloid one can compute the expansions from the interior angle and from the cusp and match the two eigenfunctions at the overlap (see Fig. 8). Using the Fourier-Bessel expansion ansatz it is not possible to directly fulﬁll the boundary condition along the curved arcs. The choice of the second eigenfunction (centered at the origin) is therefore the general Fourier-Bessel

2r

Figure 7. Hypocycloid with n = 10

expansion with integer coeﬃcients mν

- (7.4) Ψ[IIN](k,r,θ) = N


II mν=1

Jm

ν

(k · r) · cos(mν · θ).

The conditions are now that the two eigenfunctions (including their derivatives) have to match along the intersection line and additionally that the second function has to be zero along the arc. As far as we are aware, so far no other author has applied the method of particular solutions using expansions from a cusp vertex. The MPS (combined with domain decomposition) however works decently and achieves convergence with around 1 digit of eigenvalue precision per 25 additional matching points.

We have computed each hypocycloid eigenvalues from 5 to 100 edges for one week on a single thread, which resulted in around 65 digits precision per eigenvalue. If one ﬁts the eigenvalues on a 1/n-polynomial-expansion, the expansion coeﬃcients are converging towards constant values which are given by

C0 = 1 C1 = 0.372285278452919538950832494889900 C2 = 1.16087789045807729220949677611 C3 = 1.8723005009420124517917316

We have so far been unable to ﬁnd closed-form expressions for these numbers. Using the symmetry of the expansion formulae for higher fully symmetric eigenvalues (see for example [31]), we found indications that the expansion coeﬃcients Ci are polynomials of degree

|i−1|

2 in the limiting eigenvalue xm = j02,m. Namely, by computing the ﬁrst four fully

symmetric eigenvalues of several hypocycloids, we found evidence that C0 = 1 · (xm)0 C1 = 0.372285278452919538950832494889900 · (xm)0 C2 = 1.16087789045807729220949677611 · (xm)0 C3 = 2.4397482604 · (xm)0 − 0.0981202685 · (xm)1 C4 = 4.9228013 · (xm)0 − 0.088251328 · (xm)1

However, it remains unclear whether these numbers can be expressed in closed form.

## α/2 I II

Figure 8. Decomposition of the fundamental region of a hypocycloid 8. Conclusion

We have demonstrated how the method of particular solutions combined with domain decomposition can be eﬃciently applied to compute Laplacian eigenvalues of several twodimensional shapes with dihedral symmetry to very high precision. Using this numerical data we have computed two additional eigenvalue expansion coeﬃcients of regular polygons with Dirichlet boundary condition as well as the ﬁrst 17 coeﬃcients for regular polygons with Neumann boundary condition, and showed that single-valued multiple zeta values appear in the expansions of both of these examples. Moreover, we have also shown that Riemann zeta values and alternating MZVs appear in the eigenvalue expansion coeﬃcients of more general regular star shapes, together with a formula relating the coeﬃcients of star shapes with diﬀerent density. Additionally, we constructed examples of star shapes with sinusoidal boundary and found that the expansion coeﬃcients are deﬁned over Q[x] which indicates that the 1/n expandability of eigenvalues is not restricted to polygonal shapes only.

Acknowledgements

D.B. would like to thank Oliver Freyermuth for his help in carrying out the computations on a computing cluster, Fredrik Johansson for assistance with Arb, and Plamen Koev for discussions on possible improvements of the approach of Section 6. D.R. would like to thank Erik Panzer for help with ﬁnding a good basis for single-valued MZVs in weight 16. D.R. would also like to thank Steven Charlton for great help with calculations involving alternating MZVs. D.B. acknowledges ﬁnancial support from the Bonn-Cologne Graduate School of Physics and Astronomy honors branch.

##### 9. Appendix 9.1. Brief Introduction to Multiple Zeta Values. The Riemann zeta function

- (9.1) ζ(s) =

∞

n=1

1 ns

is known to converge for all s ∈ C that satisfy Re(s) > 1. The Riemann zeta function is arguably the most famous function in all of mathematics due to its tight connection to the distribution of prime numbers. For our treatment we restrict ourselves to the special values of ζ(s) at natural numbers s ∈ N, s > 1, which are sometimes simply called zeta values. For even zeta values, Euler has famously showed that

- (9.2) ζ(2n) =

(−1)n+1B2n(2π)2n 2(2n)!

,

where Bn are Bernoulli numbers. For odd zeta values much less is known. It has been proven by Ap´ery in 1979 that ζ(3) is irrational. His proof has not yet been extended to any other odd zeta values. It is known that at least one of ζ(5),ζ(7),ζ(9),ζ(11) has to be irrational and that there exists an inﬁnite number of irrational odd zeta values. However, it is still unknown whether all odd zeta values are irrational and whether π,ζ(3),ζ(5),...,ζ(2n + 1),... have any algebraic relations among them (altough it is widely believed that there are none). As we have seen in Section 1, the arguments of products of zeta values that appear in the expansion coeﬃcients of polygon eigenvalues add up to the index of the corresponding asymptotic coeﬃcient. For example, the tenth coeﬃcient for the Dirichlet case contains the products ζ(7)ζ(3) and ζ(5)2, and we have 7 + 3 = 2 · 5 = 10. This number is called the weight of a zeta product. Note that the product of two zeta values can be written as

- (9.3) ζ(a)ζ(b) =

∞

n=1

1 na ·

∞

m=1

1 mb

=

∞

n,m=1

1 namb

.

We can split the last sum into three terms

- (9.4)

∞

n,m=1

1 namb

=

0<n<m

+

0<n=m

+

0<m<n

1 namb

.

One of the terms is given as a zeta value

- (9.5)

∞

n=m=1

1 namb

=

∞

n=1

1 na+b

= ζ(a + b).

The remaining “crossing” terms are the so-called multiple zeta values ζ(a,b) and ζ(b,a). More generally, the multiple zeta values (MZVs) are deﬁned as

- (9.6) ζ(s1,...,sk) =

0<n1<...<nk

1 ns

1

1 ...ns

k

k

.

The decomposition

- (9.7) ζ(a)ζ(b) = ζ(a,b) + ζ(a + b) + ζ(b,a)

is sometimes called the Nielsen reﬂection formula. Multiple zeta values satisfy a wide variety of interesting relations. For instance, the Q-linear span of MZVs inside R is closed under products, i.e., forms an algebra. An important subalgebra of MZVs is given by single-valued MZVs that were deﬁned by Brown in [8]. These have been found to appear in amplitudes of Feynman diagrams of string theory. The relation between single-valued MZVs and odd zeta values is given by

- (9.8) ζsv(2n + 1) = 2ζ(2n + 1).


We will not cover the theory of single-valued MZVs in this brief introduction but instead only give an expression for the single-valued MZVs that appear in our expansion formulas

ζsv(3,5,3) = 2ζ(3,5,3) − 2ζ(3)ζ(5,3) − 10ζ(3)2ζ(5), ζsv(5,3,5) = 2ζ(5,3,5) − 22ζ(5)ζ(5,3) − 120ζ(5)2ζ(3) − 10ζ(5)ζ(8), ζsv(3,7,3) = 2ζ(3,7,3) − 2ζ(3)ζ(7,3) − 28ζ(3)2ζ(7) − 24ζ(5)ζ(5,3)

− 144ζ(5)2ζ(3) − 12ζ(5)ζ(8), ζsv(5,3,7) = 2ζ(5,3,7) − 28ζ(3,5)ζ(7) − 12ζ(3,7)ζ(5) − 336ζ(3)ζ(5)ζ(7) − 78ζ(5)3 − 6ζ(10)ζ(5) − 28ζ(8)ζ(7) − 34ζ(6)ζ(9) + 110ζ(4)ζ(11) + 1001ζ(2)ζ(13), ζsv(3,3,9) = 2ζ(3,3,9) + 12ζ(3,7)ζ(5) + 30ζ(3,5)ζ(7) + 272ζ(5)3 − 27ζ(3)2ζ(9) + 1209ζ(13)ζ(2)

+ 252ζ(11)ζ(4) + 29ζ(9)ζ(6) + 6ζ(7)ζ(8) + 318ζ(3)ζ(5)ζ(7), ζsv(1,1,3,4,6) = 2ζ(1,1,3,4,6) + 2ζ(1,1,4,6)ζ(3) − 12ζ(3)ζ(3,7)ζ(2) + 4ζ(3,3,7)ζ(2)

+ 20ζ(3,3,5)ζ(4) − 1313356 ζ(5)3 − 23ζ(3)5 − 232 ζ(3)2ζ(5)ζ(4) + 21ζ(3,5)ζ(5)ζ(2)

− 16ζ(3)ζ(5)2ζ(2) − 48110 ζ(3,5)ζ(7) + 34945 ζ(7)ζ(8) − 118175336 ζ(5)ζ(10) − 29279 ζ(3)2ζ(9) − 5671760 ζ(13)ζ(2) + 8418572 ζ(9)ζ(6) − 2719912 ζ(11)ζ(4) − 285 ζ(2)ζ(3,5,5) + 589 ζ(3)ζ(3,9) + 399292349752 ζ(3)ζ(12) + 3ζ(3)3ζ(6) − 14556 ζ(5)ζ(3,7) − 8ζ(3)ζ(3,5)ζ(4) − 1250924 ζ(3)ζ(5)ζ(7)

− 52ζ(3)2ζ(7)ζ(2).

Some of the expressions we give also involve alternating multiple zeta values which are special values of multiple polylogarithms

1 ...zn

zn

1

k

k

- (9.9) Lim


1,...,mk(z1,...,zk) =

,

1 ...nm

nm

1

k

k

0<n1<...<nk

when all zi are set to ±1.

Remaining Coeﬃcients for Regular Polygons with Dirichlet Boundary Condition.

- C14(x) = ζ(11)ζ(3)(1488 − 664x + 329025 x2 + 2038130 x3 + 10169240 x4 + 167 x5)

+ ζ(9)ζ(5)(1360 − 28243 x − 73063 x2 + 13009 x3 + 4678 x4 + x5)

+ ζ(7)2(648 − 540x − 36272 x2 + 4834 x3 + 17516 x4 + 169 x5)

+ ζ(5)ζ(3)3(128 + 27523 x + 36643 x2 + 40x3)

+ ζsv(3,5,3)ζ(3)x21296+285 x−x2 ,

- C15(x) = (−9611x3 − 86411 x2)ζsv(1,1,3,4,6) + (−727 x5 − 7136x4 − 42211 x3 − 637211 x2)ζsv(3,3,9)

+ (−16819 x5 − 21731680x4 − 13452385 x3 − 282042385 x2)ζsv(5,3,7)

+ (−25621 x6 + 20087995040 x5 + 644330219100800 x4 + 12325006817103950 x3 + 2671269085311550 x2 − 108525 x + 218445 )ζ(15)

+ (−154 x5 − 218318 x4 − 4824x3 − 1583683 x2 + 21283 x + 27203 )ζ(9)ζ(3)2

+ (−13312 x5 + 64615 x4 − 27491655 x3 − 452433655 x2 + 864x + 1728)ζ(7)ζ(5)ζ(3)

+ (−3x5 − 51110 x4 − 420268165 x3 − 207669655 x2 + 144x + 288)ζ(5)3

+ (−166455 x3 − 62528165 x2 + 313615 x + 12815 )ζ(3)5 ,

- C16(x) = (6421ζ(13)ζ(3) + 4964ζ(11)ζ(5) + 2932ζ(9)ζ(7))x6


+ (4466878400 ζ(13)ζ(3) + 42067480 ζ(11)ζ(5) + 15073288 ζ(9)ζ(7) − 2ζ(7)ζ(3)3

+ 325 ζ(5)2ζ(3)2 + (35067 ζsv(5,3,5) − 71ζsv(3,7,3))ζ(3) − 201 ζsv(3,5,3)ζ(5))x5

+ (31008572800 ζ(13)ζ(3) + 13943380 ζ(11)ζ(5) + 1118572 ζ(9)ζ(7) − 20ζ(7)ζ(3)3 − 25845 ζ(5)2ζ(3)2 − (1139350 ζsv(5,3,5) + 5128ζsv(3,7,3))ζ(3) − 1047ζsv(3,5,3)ζ(5))x4

+ (55916960 ζ(13)ζ(3) + 22245 ζ(11)ζ(5) + 37216 ζ(9)ζ(7) + 988ζ(7)ζ(3)3 − 2808ζ(5)2ζ(3)2 − (5225 ζsv(5,3,5) − 59ζsv(3,7,3))ζ(3) + 5525 ζsv(3,5,3)ζ(5))x3

+ (16964568175 ζ(3)ζ(13) − 26454ζ(5)ζ(11) − 40787ζ(9)ζ(7) + 18056ζ(7)ζ(3)3 + 1508645 ζ(5)2ζ(3)2 − (214488175 ζsv(5,3,5) − 89647 ζsv(3,7,3))ζ(3))x2

+ (−2424ζ(13)ζ(3) − 3480ζ(11)ζ(5) − 4184ζ(9)ζ(7) + 2240ζ(7)ζ(3)3 + 3360ζ(5)2ζ(3)2)x

+ (5040ζ(13)ζ(3) + 4464ζ(11)ζ(5) + 4080ζ(9)ζ(7) + 384ζ(7)ζ(3)3 + 576ζ(5)2ζ(3)2).

##### Remaining Coeﬃcients for Smooth Star Shapes with m = 2.

- C13(x) = −(1209600x5 + 169412175x4 + 1584305000x3 + 991331400x2 − 67630780x − 22055334)/44236800,
- C14(x) = (13271040x5 + 610174215x4 + 3119672640x3 + 1238016540x2

+ 7880224x + 62326230)/26542080,

- C15(x) = −(457228800x6 + 118856311875x5 + 2664517542050x4 + 8258849383400x3

+ 2125616765440x2 + 77434447468x − 10887717978)/22295347200,

- C16(x) = (33443020800x6 + 2924868777075x5 + 38003282808750x4 + 76583141218500x3

+ 12609060010540x2 + 18024777715x − 83085435396)/66886041600,

- C17(x) = −(1810626048000x7 + 785618449756875x6 + 34479052407093000x5

+ 286806810669211000x4 + 393746334459690800x3 + 41833381428570655x2 − 382662625041172x − 164371240997550)/112368549888000,

- C18(x) = (120394874880000x7 + 17871670961353125x6 + 468925800452550000x5

+ 2662356634044423750x4 + 2565871095884593000x3 + 179378699791862375x2 − 584375985329753x + 732859733409750)/240789749760000,

- C19(x) = −(21184324761600000x8 + 14232900142095075000x7 + 1079843748016254200000x6

+ 18704185436989446975000x5 + 75684321204286594467500x4

+ 52194215245123302758750x3 + 2424740991307168439892x2 + 8697289229328086768x

+ 806072685794305875)/1618107118387200000,

- C20(x) = (866843099136000000x8 + 201696166234942312500x7 + 9330236455363230750000x6

+ 113623492626641309812500x5 + 337606293009361365696875x4

+ 168745237201472986724250x3 + 5201634554633731393011x2

+ 7062388870424537486x − 2948155439034622500)/1733686198272000000,

- C21(x) = −(1779483279974400000000x9 + 1750724028590009405625000x8

+ 210914990771238755890000000x7 + 6570081043597798567754375000x6

+ 58697712321536371300988890000x5 + 130785026894321633100311176125x4

+ 47808464146250191120470311872x3 + 976817476078605785634707984x2 − 709576341339684500163424x − 466588962879561812430000)/163105197533429760000000,

- C22(x) = (2140755717626265600000000x9 + 736244702627870619077343750x8


+ 54826137837085868012812500000x7 + 1224633170486034514394552343750x6

+ 8269403144636044633016590206250x5 + 14026490060106825798594234715375x4

+ 3774510130770113767485677126049x3 + 51231956845133382896804013256x2 − 34284798535733782456620476x

+ 15568092692374386637462500)/4281511435252531200000000,

- C23(x) = −(5869945905985953792000000000x10 + 8099489427400822789150312500000x9


+ 1456333964071948513322434125000000x8 + 74056060297895723139610998046875000x7

+ 1237529454152663240037004207720702500x6 + 6452892881074851056674758533001245925x5 + 8424983842296738700856453921666897340x4 + 1676926979683976178266295659995421360x3 + 15156930607344875353880119232561056x2 + 3433373767917417187848282765632x

+ 1242040349979959360991463800000)/632978650587734212608000000000.

- Coeﬃcients for Smooth Star Shapes with m = 3. C0(x) = 1, C1(x) = 0, C2(x) = 0, C3(x) = 0, C4(x) = 0, C5(x) = 1, C6(x) = 1/2, C7(x) = −x/2, C8(x) = x/2, C9(x) = −(x2 + 4x + 2)/8,

- C10(x) = (2x2 + 2x + 3)/4,
- C11(x) = −(x + 1)(x2 + 21x − 18)/16,
- C12(x) = (16x3 + 104x2 − 25x + 10)/32,
- C13(x) = −(30x4 + 1920x3 + 5547x2 − 192x − 88)/768,
- C14(x) = (384x4 + 7776x3 + 11523x2 − 192x − 304)/768,
- C15(x) = −(168x5 + 23520x4 + 224715x3 + 184920x2 − 224x + 64)/6144,
- C16(x) = (3072x5 + 141312x4 + 758013x3 + 367512x2 + 5696x + 8192)/6144.
- C17(x) = (−12096x6 − 3144960x5 − 70977933x4 − 235020744x3 − 69971328x2 − 927744x + 602368)/589824,
- C18(x) = (98304x6 + 8601600x5 + 113600385x4 + 246217560x3 + 46297920x2 − 15360x + 88832)/196608.


- Coeﬃcients for Smooth Star Shapes with m = 4. C0(x) = 1, C1(x) = 0, C2(x) = 0, C3(x) = 0,


C4(x) = 0, C5(x) = 0, C6(x) = 0, C7(x) = 1, C8(x) = 1/2, C9(x) = −x/2,

- C10(x) = x/2,
- C11(x) = −x(x + 4)/8,
- C12(x) = x(x + 1)/2,
- C13(x) = −(x3 + 22x2 + 8x + 4)/16,
- C14(x) = (2x3 + 13x2 + 2x + 3)/4,
- C15(x) = −(5x4 + 320x3 + 912x2 + 24x − 144)/128,
- C16(x) = (16x4 + 324x3 + 480x2 − 25x + 10)/32,
- C17(x) = −x(7x4 + 980x3 + 9360x2 + 7929x − 64)/256,
- C18(x) = x(128x4 + 5888x3 + 31584x2 + 16065x − 64)/256,
- C19(x) = (−126x6 − 32760x5 − 739344x4 − 2453067x3 − 773208x2

+ 1536x + 704)/6144,

- C20(x) = (3072x6 + 268800x5 + 3550080x4 + 7730685x3 + 1545624x2 − 1536x − 2432)/6144.


References

- [1] C. M. Bender and S. A. Orszag. Advanced mathematical methods for scientists and engineers - asymptotic methods and perturbation theory. Springer-Verlag, ISBN 0-387-98931-5, 1999.
- [2] D. Berghaus, B. Georgiev, H. Monien, and D. Radchenko. On Dirichlet eigenvalues of regular polygons. arXiv:2103.01057, 2021.
- [3] T. Betcke. A GSVD formulation of a domain decomposition method forplanar eigenvalue problems. IMA Journal of Numerical Analysis, 27(3):451–478, 2006.
- [4] T. Betcke. The generalized singular value decomposition and the method of particular solutions. SIAM Journal on Scientiﬁc Computing, 30(3):1278–1295, 2008.
- [5] T. Betcke and L. N. Trefethen. Reviving the method of particular solutions. SIAM Review, 47(3):469– 491, 2005.
- [6] J. Bezanson, S. Karpinski, V. B. Shah, and A. Edelman. Julia: A fast dynamic language for technical computing. CoRR, abs/1209.5145, 2012.
- [7] M. Boady. Applications of symbolic computation to the calculus of moving surfaces. Phd thesis, Drexel University, 2016.
- [8] F. Brown. Single-valued motivic periods and multiple zeta values. Forum of Mathematics, Sigma, 2:e25,

- 2014.

[9] C. S. Chen, X. Jiang, W. Chen, and G. Yao. Fast solution for solving the modiﬁed helmholtz equation with the method of fundamental solutions. Communications in Computational Physics, 17(3):867–886,

- 2015.


- [10] H. D. Conway. The Bending, Buckling, and Flexural Vibration of Simply Supported Polygonal Plates by Point-Matching. Journal of Applied Mechanics, 28(2):288–291, 1961.
- [11] J. Dahne and B. Salvy. Computation of tight enclosures for Laplacian eigenvalues. SIAM J. Sci. Comput., 42(5):A3210–A3232, 2020.
- [12] J. Demmel and P. Koev. The accurate and eﬃcient solution of a totally positive generalized vandermonde linear system. SIAM J. Matrix Anal. Appl.,, 27(1):142–152, 2005.
- [13] J. Descloux and M. C. Tolley. An accurate algorithm for computing the eigenvalues of a polygonal membrane. Computer Methods in Applied Mechanics and Engineering, 39(1):37–53, 1983.
- [14] T. A. Driscoll. Eigenmodes of isospectral drums. SIAM Rev., 39(1), 1–17, 1997.


- [15] C. Fieker, W. Hart, T. Hofmann, and F. Johansson. Nemo/hecke. Proceedings of the 2017 ACM on International Symposium on Symbolic and Algebraic Computation - ISSAC ’17, 2017.
- [16] L. Fox, P. Henrici, and C. Moler. Approximations and bounds for eigenvalues of elliptic operators. SIAM J. Numer. Anal., 1967.
- [17] C. Gordon, D. L. Webb, and S. Wolpert. One cannot hear the shape of a drum. Bull. Amer. Math. Soc., 27:134–138, 1992.
- [18] P. Grinfeld and G. Strang. Laplace eigenvalues on regular polygons: A series in 1/n. Journal of Mathematical Analysis and Applications, 385(1):135 – 149, 2012.
- [19] P. Guidotti and J. V. Lambers. Eigenvalue characterization and computation for the laplacian on general 2-d domains. Numerical Functional Analysis and Optimization, 29(5-6):507–531, 2008.
- [20] J. G´mez-Serrano and G. Orriols. Any three eigenvalues do not determine a triangle, 2019.
- [21] F. Johansson. Arb: eﬃcient arbitrary-precision midpoint-radius interval arithmetic. IEEE Transactions on Computers, 66:1281–1292, 2017.
- [22] F. Johansson. Computing hypergeometric functions rigorously. ACM Trans. Math. Softw., 45(3), 2019.
- [23] F. Johansson. Faster arbitrary-precision dot product and matrix multiplication. In 2019 IEEE 26th Symposium on Computer Arithmetic (ARITH), pages 15–22, 2019.
- [24] R. S. Jones. Computing ultra-precise eigenvalues of the laplacian within polygons. Adv. Comput. Math., 2017.
- [25] R. S. Jones. The fundamental laplacian eigenvalue of the regular polygon with dirichlet boundary conditions. arXiv:1712.06082, 2017.
- [26] N. Kaiser. Mean eigenvalues for simple, simply connected, compact lie groups. Journal of Physics A: Mathematical and General, 39(49):15287–15298, 2006.
- [27] P. A. Laura. On the determination of the natural frequency of 8 star- shaped membrane. Journal of the Royal Aeronautical Society, Pol. 68:274–275, 1964.
- [28] A. Lenstra, H. Lenstra, and L. Lov´sz. Factoring polynomials with rational coeﬃcients. Math. Ann., 1982.
- [29] M. J. Litzkow, M. Livny, and M. W. Mutka. Condor-a hunter of idle workstations. Proceedings of the 8th International Conference of Distributed Computing Systems, pages 104–111, 1988.
- [30] L. Molinari. On the ground state of regular polygonal billiards. Journal of Physics A: Mathematical and General, 30(18):6517–6524, 1997.
- [31] V. K. Oikonomou. Casimir energy for a regular polygon with dirichlet boundaries. arXiv:1012.5376, 2010.
- [32] G. P´lya and G. Szeg¨. Isoperimetric inequalities in mathematical physics. Annals of Mathematical Studies, 1951.
- [33] M. Schreiber. Star Polygons. https://demonstrations.wolfram.com/StarPolygons/, 2011. [Online; accessed 23-September-2022].
- [34] The PARI Group, Univ. Bordeaux. PARI/GP version 2.11.2, 2019. available from http://pari. math.u-bordeaux.fr/.
- [35] I. N. Vekua. New methods for solving elliptic equations. North-Holland Series in Applied Mathematics and Mechanics, Vol. 1. North-Holland Publishing Co., Amsterdam; Interscience Publishers John Wiley & Sons, Inc., New York, 1967.
- [36] H. Wagner. Fundamental Frequency of a Star-Shaped Membrane. Zeitschrift Angewandte Mathematik und Mechanik, 51(4):325–326, 1971.


Bethe Center, University of Bonn, Nussallee 12, 53115 Bonn, Germany Email address: berghaus@th.physik.uni-bonn.de

Independent Researcher, 43074 Sunbury, Ohio, USA Email address: rsjones7@yahoo.com

Bethe Center, University of Bonn, Nussallee 12, 53115 Bonn, Germany Email address: hmonien@uni-bonn.de

Laboratoire Paul Painleve,´ University of Lille, F-59655 Villeneuve d’Ascq, France Email address: danradchenko@gmail.com

