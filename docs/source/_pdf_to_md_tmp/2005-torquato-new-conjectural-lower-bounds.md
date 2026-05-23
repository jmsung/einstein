New Conjectural Lower Bounds on the Optimal Density of Sphere Packings

arXiv:math/0508381v2[math.MG]5Mar2006

S. Torquato1,2,3,4 and F. H. Stillinger1 1Department of Chemistry, 2Program in Applied and Computational Mathematics, 3Princeton Institute for the Science and Technology of Materials, and 4 Princeton Center for Theoretical Physics Princeton University, Princeton, NJ 08544 ABSTRACT

Sphere packings in high dimensions interest mathematicians and physicists and have direct applications in communications theory. Remarkably, no one has been able to provide exponential improvement on a 100-year-old lower bound on the maximal packing density due to Minkowski in d-dimensional Euclidean space Rd. The asymptotic behavior of this bound is controlled by 2−d in high dimensions. Using an optimization procedure that we introduced earlier [TS02] and a conjecture concerning the existence of disordered sphere packings in Rd, we obtain a conjectural lower bound on the density whose asymptotic behavior is controlled by 2−0.77865...d, thus providing the putative exponential improvement of Minkowski’s bound. The conjecture states that a hard-core nonnegative tempered distribution is a pair correlation function of a translationally invariant disordered sphere packing in Rd for asymptotically large d if and only if the Fourier transform of the autocovariance function is nonnegative. The conjecture is supported by two explicit analytically characterized disordered packings, numerical packing constructions in low dimensions, known necessary conditions that only have relevance in very low dimensions, and the fact that we can recover the forms of known rigorous lower bounds. A byproduct of our approach is an asymptotic conjectural lower bound on the average kissing number whose behavior is controlled by 20.22134...d, which is to be compared to the best known asymptotic lower bound on the individual kissing number of 20.2075...d. Interestingly, our optimization procedure is precisely the dual of a primal linear program devised by Cohn and Elkies [CE03] to obtain upper bounds on the density, and hence has implications for linear programming bounds. This connection proves that our density estimate can never exceed the Cohn-Elkies upper bound, regardless of the validity of our conjecture.

# 1 Introduction

A collection of congruent spheres in d-dimensional Euclidean space Rd is called a sphere packing P if no two of the spheres have an interior point in common. The packing density or simply density φ(P) of a sphere packing is the fraction of space Rd covered by the spheres. We will call

φmax = sup

φ(P) (1)

P⊂Rd

the maximal density, where the supremum is taken over all packings in Rd. The sphere packing problem seeks to answer the following question: Among all packings of congruent spheres, what is the maximal packing density φmax, i.e., largest fraction of Rd covered by the spheres, and what are the corresponding arrangements of the spheres [Rog64, CS98]? The sphere packing problem is of great fundamental and practical interest, and arises in a variety of contexts, including classical ground states of matter in low dimensions [CL95], the famous Kepler conjecture for d = 3 [Hal98], error-correcting codes [CS98] and spherical codes [CS98].

For arbitrary d, the sphere packing problem is notoriously diﬃcult to solve. In the case of packings of congruent d-dimensional spheres, the exact solution is known for the ﬁrst three space dimensions. For d = 1, the answer is trivial because the spheres tile the space so that φmax = 1. In two dimensions, the optimal solution is the triangular lattice arrangement (also called the hexagonal packing) with φmax = π/√12. In three dimensions, the Kepler conjecture that the face-centered cubic lattice arrangement provides the densest packing with φmax = π/√18 was only recently proved by Hales [Hal98]. For 3 < d < 10, the densest known packings of congruent spheres are lattice packings (deﬁned below). However, for suﬃciently large d, lattice packings are likely not to be the densest. Indeed, this paper suggests that disordered sphere arrangements may be the densest packings as d → ∞.

![image 1](<2005-torquato-new-conjectural-lower-bounds_images/imageFile1.png>)

![image 2](<2005-torquato-new-conjectural-lower-bounds_images/imageFile2.png>)

We review some basic deﬁnitions that we will subsequently employ. A packing is saturated if there is no space available to add another sphere without overlapping the existing particles. The set of lattice packings is a subset of the set of sphere packings in Rd. A lattice Λ in Rd is a subgroup consisting of the integer linear combinations of vectors that constitute a basis for Rd. A lattice packing PL is one in which the centers of nonoverlapping spheres are located at the points of Λ. In a lattice packing, the space Rd can be geometrically divided into identical regions F called fundamental cells, each of which contains the center of just one sphere. Thus, the density of a lattice packing φL consisting of spheres of unit diameter is given by

v1(1/2) Vol(F)

φL =

, (2)

![image 3](<2005-torquato-new-conjectural-lower-bounds_images/imageFile3.png>)

where

πd/2 Γ(1 + d/2)

Rd (3)

v1(R) =

![image 4](<2005-torquato-new-conjectural-lower-bounds_images/imageFile4.png>)

is the volume of a d-dimensional sphere of radius R and Vol(F) is the volume of a fundamental cell. We will call

φLmax = sup

φ(PL) (4)

PL⊂Rd

the maximal density among all lattice packings in Rd. For a general packing of spheres of unit diameter for which a density φ(P) exists, it is useful to introduce the number (or center) density ρ deﬁned by

φ(P) v1(1/2)

, (5) which therefore can be interpreted as the average number of sphere centers per unit volume.

ρ =

![image 5](<2005-torquato-new-conjectural-lower-bounds_images/imageFile5.png>)

Three distinct categories of packings have been distinguished, depending on their behavior with respect to nonoverlapping geometric constraints and/or externally imposed virtual displacements: locally jammed, collectively jammed, and strictly jammed [TS01, TDS03, DTSC04]. Loosely speaking, these jamming categories, listed in order of increasing stringency, reﬂect the degree of mechanical stability of the packing. A packing is locally jammed if each particle in the system is locally trapped by its neighbors; i.e., it cannot be translated while ﬁxing the positions of all other particles. Each sphere simply has to have at least d + 1 contacts with neighboring spheres, not all in the same d-dimensional hemisphere. A collectively jammed packing is any locally jammed conﬁguration in which no ﬁnite subset of particles can simultaneously be continuously displaced so that its members move out of contact with one another and with the remainder set. A strictly jammed packing is any collectively jammed conﬁguration that disallows all globally uniform volume-nonincreasing deformations of the system boundary. Importantly, the jamming category is generally dependent on the type of boundary conditions imposed (e.g., hard wall or periodic boundary conditions) as well as the shape of the boundary. The range of possible densities for a given jamming category decreases with increasing stringency of the category. Whereas the lowest-density states of collectively and strictly jammed packings in two or three dimensions are currently unknown, one can achieve locally jammed packings with vanishing density [B¨or64]. This classiﬁcation of packings according to jamming criteria is closely related to the concepts of “rigid” and “stable” packings found in the mathematics literature [CBB98].

In the next section, we summarize some previous upper and lower bounds on the maximal density. For large d, the asymptotic behavior of the well-known Minkowski lower bound [Min05] on the maximal density is controlled by 2−d. Thus far, no one has been able to provide

exponential improvement on this lower bound. Using an optimization procedure and a conjecture concerning the existence of disordered sphere packings in high dimensions, we obtain conjectural lower bounds that yield the long-sought asymptotic exponential improvement on Minkowski’s bound. We believe that consideration of truly disordered packings is the key notion that will yield exponential improvement on Minkowski’s lower bound. A byproduct of our approach is an asymptotic conjectural lower bound on the average kissing number that is superior to the best known asymptotic lower bound on the individual kissing number.

# 2 Some Previous Upper and Lower Bounds

The nonconstructive lower bounds of Minkowski [Min05] established the existence of reasonably dense lattice packings. He found that the maximal density φLmax among all lattice packings for d ≥ 2 satisﬁes

ζ(d) 2d−1

φLmax ≥

, (6)

![image 6](<2005-torquato-new-conjectural-lower-bounds_images/imageFile6.png>)

where ζ(d) = ∞k=1 k−d is the Riemann zeta function. Note that for large values of d, the asymptotic behavior of the Minkowski lower bound is controlled by 2−d. Since 1905, many extensions and generalizations of (6) have been obtained [DR47, Bal92, CS98], but none of these investigations have been able to improve upon the dominant exponential term 2−d. It is useful to note that the density of a saturated packing of congruent spheres in Rd for all d satisﬁes

- 1

![image 7](<2005-torquato-new-conjectural-lower-bounds_images/imageFile7.png>)

- 2d


φ ≥

. (7)

The proof is trivial. A saturated packing of congruent spheres of unit diameter and density φ in Rd has the property that each point in space lies within a unit distance from the center of some sphere. Thus, a covering of the space is achieved if each sphere center is encompassed by a sphere of unit radius and the density of this covering is 2dφ ≥ 1. Thus, the bound (7), which is sometimes called the “greedy” lower bound, has same the dominant exponential term

- as (6). In Section 4.1, we show that there exists a construction of a disordered packing of congruent spheres that realizes the weaker lower bound of (7), i.e., φ = 2−d.


The best currently known lower bound on φLmax was obtained by Ball [Bal92]. He found that

2(d − 1)ζ(d) 2d

φLmax ≥

. (8)

![image 8](<2005-torquato-new-conjectural-lower-bounds_images/imageFile8.png>)

As d → ∞, Table 1 gives the dominant asymptotic behavior of several lower bounds on φLmax for large d.

Table 1: Dominant asymptotic behavior of lower bounds on φLmax for large d.

![image 9](<2005-torquato-new-conjectural-lower-bounds_images/imageFile9.png>)

![image 10](<2005-torquato-new-conjectural-lower-bounds_images/imageFile10.png>)

![image 11](<2005-torquato-new-conjectural-lower-bounds_images/imageFile11.png>)

(2)2−d Minkowski (1905) [ln(√2)d]2−d Davenport and Rogers (1947) (2d)2−d Ball (1992)

![image 12](<2005-torquato-new-conjectural-lower-bounds_images/imageFile12.png>)

![image 13](<2005-torquato-new-conjectural-lower-bounds_images/imageFile13.png>)

![image 14](<2005-torquato-new-conjectural-lower-bounds_images/imageFile14.png>)

![image 15](<2005-torquato-new-conjectural-lower-bounds_images/imageFile15.png>)

![image 16](<2005-torquato-new-conjectural-lower-bounds_images/imageFile16.png>)

![image 17](<2005-torquato-new-conjectural-lower-bounds_images/imageFile17.png>)

![image 18](<2005-torquato-new-conjectural-lower-bounds_images/imageFile18.png>)

Nontrivial upper bounds on the maximal density φmax for any sphere packing in Rd have been derived. Blichfeldt [Bli29] showed that the maximal packing density for all d satisﬁes φmax ≤ (d/2 + 1)2−d/2. This upper bound was improved by Rogers [Rog58, Rog64] by an analysis of the Voronoi cells. For large d, Rogers’ upper bound asymptotically becomes d2−d/2/e. Kabatiansky and Levenshtein [KL78] found an even stronger bound, which in the limit d → ∞ yields φmax ≤ 2−0.5990d(1+o(1)). Cohn and Elkies [CE03] obtained and computed linear programming upper bounds, which provided improvement over Rogers’ upper bound for dimensions 4 through 36. They also conjectured that their approach could be used to prove sharp bounds in 8 and 24 dimensions. Indeed, Cohn and Kumar [CK04] used these techniques to prove that the Leech lattice is the unique densest lattice in ℜ24. They also proved that no sphere packing in ℜ24 can exceed the density of the Leech lattice by a factor of more than 1 + 1.65 × 10−30, and gave a new proof that E8 is the unique densest lattice in ℜ8. Table 2 provides the dominant asymptotic behavior of several upper bounds on φmax for large d.

Table 2: Dominant asymptotic behavior of upper bounds on φmax for large d.

![image 19](<2005-torquato-new-conjectural-lower-bounds_images/imageFile19.png>)

![image 20](<2005-torquato-new-conjectural-lower-bounds_images/imageFile20.png>)

![image 21](<2005-torquato-new-conjectural-lower-bounds_images/imageFile21.png>)

(d/2)2−0.5d Blichfeldt (1929) (d/e)2−0.5d Rogers (1958)

![image 22](<2005-torquato-new-conjectural-lower-bounds_images/imageFile22.png>)

![image 23](<2005-torquato-new-conjectural-lower-bounds_images/imageFile23.png>)

![image 24](<2005-torquato-new-conjectural-lower-bounds_images/imageFile24.png>)

![image 25](<2005-torquato-new-conjectural-lower-bounds_images/imageFile25.png>)

2−0.5990d Kabatiansky and Levenshtein (1979)

![image 26](<2005-torquato-new-conjectural-lower-bounds_images/imageFile26.png>)

![image 27](<2005-torquato-new-conjectural-lower-bounds_images/imageFile27.png>)

# 3 Realizability of Point Processes

As will be described in Section 5, our new approach to lower bounds on the density of sphere packings in Rd rests on whether certain one- and two-point correlation functions are realizable by sphere packings. As we will discuss, a sphere packing can be regarded to be a special case of a point process and so a more general question concerns the necessary and suﬃcient conditions for the realizability of point processes in Rd. Before discussing the realizability of

point processes, it is useful to recall some basic results from the theory of spatial stochastic (or random) processes. Let x ≡ (x1, x2, . . .xd) denote a vector position in Rd. Consider a stochastic process {Y (x; ω) : x ∈ Rd; ω ∈ Ω}, where Y (x; ω) is a real-valued random variable, ω is a realization generated by the stochastic process and (Ω, F, P) is a probability space (i.e., Ω is a sample space, F is a σ-algebra of measurable subsets of Ω, and P is a probability measure). For simplicity, we will often suppress the variable ω.

## 3.1 Ordinary Stochastic Processes

We will assume that the stochastic process is translationally invariant (i.e., statistically homogeneous in space). Let us further assume that the mean µ = Y (x) and autocovariance function

χ(r) = [Y (x) − µ][Y (x + r) − µ] (9)

exist, where angular brackets denote an expectation, i.e., an average over all realizations. The fact that the mean µ and autocovariance function χ(r) are independent of the variable x is a consequence of the translational invariance of the measure. Clearly,

χ(0) = Y 2 − µ2 (10)

and it follows from Schwarz’s inequality that

|χ(r)| ≤ Y 2 − µ2. (11)

It immediately follows [Lo`e63] that the autocovariance function χ(r) must be positive semidefinite (nonnegative) in the sense that for any ﬁnite number of spatial locations r1, r2, . . ., rm in Rd and arbitrary real numbers a1, a2, . . ., am,

m

i=1

m

aiajχ( bfri − rj) ≥ 0. (12)

j=1

It is clear that [Y (x + r) − Y (x)]2 = 2[χ(0) − χ(r)]. Thus, if the autocovariance function χ(r) is continuous at the point r = 0, the process Y (x) on Rd will be mean square continuous, i.e., limr→0 [Y (x + r) − Y (x)]2 = 0 for all x. Stochastic processes that are continuous in the mean square sense will be called ordinary. It is simple to show that if χ(r) is continuous at r = 0, it is continuous for all r.

Does every continuous positive semideﬁnite function f(r) correspond to a translationally invariant ordinary stochastic process with a continuous autocovariance χ(r)? The answer is

yes, and a proof is given in the book by Lo`eve [Lo`e63] for stochastic processes in time. Here we state without proof the generalization to stochastic processes in space.

- Theorem 3.1 A continuous function f(r) on Rd is an autocovariance function of a translationally invariant ordinary stochastic process if and only if it is positive semideﬁnite.


Remark:

Assuming that f(r) is positive semideﬁnite, one needs to show that there exists a random variable Y (x) on Rd such that [Y (x)−µ][Y (x+r)−µ] = f(r). This is done by demonstrating that there exists a Gaussian (normal) process for every autocovariance function [Lo`e63]. A crucial property of a Gaussian process is that its full probability distribution is completely determined by its mean and autocovariance.

The nonnegativity condition (12) is diﬃcult to check. It turns out that it is easier to establish the existence of an autocovariance function by appealing to its spectral representation. We denote the space of absolutely integrable functions on Rd by L1. The Fourier transform of an L1 function f : Rd → ℜ is deﬁned by

f˜(k) =

f(r)e−ik · r dr. (13)

Rd

If f : Rd → R is a radial function, i.e., f depends only on the modulus r = |r| of the vector r, then its Fourier transform given by

d 2

f˜(k) = (2π)

![image 28](<2005-torquato-new-conjectural-lower-bounds_images/imageFile28.png>)

∞

J(d/2)−1(kr) (kr)(d/2)−1

rd−1f(r)

dr, (14)

![image 29](<2005-torquato-new-conjectural-lower-bounds_images/imageFile29.png>)

0

where k is the modulus of the wave vector k and Jν(x) is the Bessel function of order ν. The Wiener–Khintchine theorem states that a necessary and suﬃcient condition for the existence of a continuous autocovariance function χ(r) of a translationally invariant stochastic process {Y (x) : x ∈ Rd} is that its Fourier transform is nonnegative everywhere, i.e., χ˜(k) ≥ 0 for all k [Yag87, Tor02]. The key “necessary” part of the proof of this theorem rests on a well-known theorem due to Bochner [Boc36], which states that any continuous function f(r) is positive semideﬁnite in the sense of (12) if and only if it has a Fourier–Stieltjes representation with a nonnegative bounded measure.

## 3.2 Generalized Stochastic Processes

The types of autocovariance functions that we are interested in must allow for generalized functions, such as Dirac delta functions. The Weiner-Khintchine theorem has been extended to autocovariances in the class of generalized functions called tempered distributions, i.e., continuous linear functionals on the space S of inﬁnitely diﬀerentiable functions Φ(x) such that Φ(x) as well as all of its derivatives decay faster than polynomially. Nonnegative tempered distributions are nonnegative unbounded measures ν on Rd such that

dν(r) (1 + |r|)n

< ∞ (15)

![image 30](<2005-torquato-new-conjectural-lower-bounds_images/imageFile30.png>)

Rd

for some n. The interested reader is referred to the books by Gel’fand [GV64] and Yaglom [Yag87] for details about generalized stochastic processes. It suﬃces to say here that {Y (Φ(x)) : x ∈ Rd} is a generalized stochastic process if for each Φ(x) ∈ S we have a random variable Y (Φ(x)) that is linear and mean square continuous in Φ. Then the mean is the linear functional µ(Φ(x)) = Y (Φ1(x)) and the autocovariance function is the bilinear functional

[Y (Φ1(x))−µ(Φ(x1))][Y (Φ2(x+r))−µ(Φ(x2))] , which we still denote by χ(r) for simplicity.

- Theorem 3.2 A necessary and suﬃcient condition for an autocovariance function χ(r) to come from a translationally invariant generalized stochastic process {Y (Φ(x)) : x ∈ Rd} is that that its Fourier transform χ˜(k) is a nonnegative tempered distribution.


Remark: We will call Theorem 3.2 the generalized Wiener-Khintchine theorem.

## 3.3 Stochastic Point Processes

Loosely speaking, a stochastic point process in Rd is deﬁned as a mapping from a probability space to conﬁgurations of points x1, x2, x3 . . . in Rd. More precisely, let X denote the set of conﬁgurations such that each conﬁguration x ∈ X is a subset of Rd that satisﬁes two regularity conditions: (i) there are no multiple points (xi = xj if i = j) and (ii) each bounded subset of Rd must contain only a ﬁnite number of points of x. We denote by N(B) the number of points within x∩B, B ∈ B, where B is the ring of bounded Borel sets in Rd. Thus, we always have N(B) < ∞ for B ∈ B but the possibility N(Rd) = ∞ is not excluded. We denote by

- U the minimal σ-algebra of subsets of X that renders all of the functions N(B) measurable.


Let (Ω, F, P) be a probability space. Any measurable map x(ω) : Ω → X, ω ∈ Ω, is called a stochastic point process [SKM95]. Point processes belong to the class of generalized stochastic processes.

A particular realization of a point process in Rd can formally be characterized by the random variable

∞

n(r) =

δ(r − xi) (16)

i=1

called the “local” density at position r, where δ(r) is a d-dimensional Dirac delta function. The “randomness” of the point process enters through the positions x1, x2, . . .. Let us call

1, r ∈ A, 0, r ∈/ A,

(17)

IA(r) =

the indicator function of a measurable set A ⊂ Rd, which we also call a “window.” For a particular realization, the number of points N(A) within such a window is given by

N(A) =

=

=

n(r)IA(r) dr

Rd

∞

δ(r − xi)IA(r) dr

i=1 Rd

IA(xi). (18)

i≥1

Note that this random setting is quite general. It incorporates cases in which the location of the points are deterministically known, such as a lattice. A packing of congruent spheres of unit diameter is simply a point process in which any pair of points cannot be closer than a unit distance from one another.

It is known that the probability measure on (X, U) exists provided that the inﬁnite set of n-point correlation functions ρn, n = 1, 2, 3 . . . meet certain conditions [Len73, Len75a, Len75b]. The n-point correlation function ρn(r1, r2, . . ., rn) is the contribution to the expectation n(r1)n(r2) · · ·n(rn) when the indices on the sums are not equal to one another, i.e.,

∞

ρn(r1, r2, . . ., rn) =

) . (19)

δ(r1 − xi

)δ(r2 − xi

) · · ·δ(rn − xi

n

1

2

i1 =i2 =··· =in

Note that the distribution-valued function ρn(r1, r2, . . ., rn) also has a probabilistic interpretation: apart from trivial constants, it is the probability density function associated with ﬁnding n diﬀerent points at positions r1, r2, . . ., rn. For this reason, ρn is also called the n-particle density and, for any n, has the nonnegativity property

ρn(r1, r2, . . ., rn) ≥ 0 ∀ri ∈ Rd (i = 1, 2, . . .n). (20)

Translational invariance means that for every constant vector y in Rd, ρn(r1, r2, . . ., rn) = ρn(r1 + y, . . ., rn + y), which implies that

ρn(r1, r2, . . ., rn) = ρngn(r12, . . ., r1n), (21)

where ρ is the number (or center) density and gn(r12, . . ., r1n) is the n-particle correlation function, which depends on the relative positions r12, r13, . . ., where rij ≡ rj − ri and we have chosen the origin to be at r1.

For such point processes without long-range order, gn(r12, . . ., r1n) → 1 when the points (or “particles”) are mutually far from one another, i.e., as |rij| → ∞ (1 ≤ i < j < ∞), ρn(r1, r2, . . ., rn) → ρn. Thus, the deviation of gn from unity provides a measure of the degree of spatial correlation between the particles, with unity corresponding to no spatial correlation. Note that for a translationally invariant Poisson point process, gn is unity for all values of its argument.

As we indicated in the beginning of this section, the ﬁrst two correlation functions, ρ1(r1) = ρ and ρ2(r1, r2) = ρ2g2(r), for translationally invariant point processes are of central concern in this paper. If the point process is also rotationally invariant (statistically isotropic), then g2 depends on the radial distance r = |r| only, i.e.,

g2(r) = g2(r), (22) and is referred to as the radial distribution function. Strictly speaking, one should use diﬀerent notation for the left and right members of Eq. (22), but to conform to conventional statisticalmechanical usage, we invoke the common notation for both. Because ρ2(r1, r2)/ρ = ρg2(r) is a conditional joint probability density, then

Z(r1, r2) =

r2

ρs1(r)g2(r) dr (23)

r1

is the expected number of points at radial distances between r1 and r2 from a randomly chosen point. Here s1(r) is the surface area of a d-dimensional sphere of radius r given by

2πd/2rd−1 Γ(d/2)

s1(r) =

. (24)

![image 31](<2005-torquato-new-conjectural-lower-bounds_images/imageFile31.png>)

For a packing of congruent spheres of unit diameter, g(r) = 0 for 0 ≤ r < 1, i.e.,

supp(g2) ⊆ {r : r ≥ 1}. (25)

Note that the radial distribution function g2(r) (or any of the ρn) for a point process must be able to incorporate Dirac delta functions. We will speciﬁcally consider those radial distribution

functions that are nonnegative distributions. For example, g2(r) for a lattice packing is the rotational symmetrization of the sum of delta functions at lattice points at a radial distance r from any lattice point [TS03].

For a translationally invariant point process, the autocovariance function χ(r) is related to the pair correlation function via

χ(r) = ρδ(r) + ρ2h(r), (26)

where

h(r) ≡ g2(r) − 1, (27) is the total correlation function. This relation is obtained using deﬁnitions (9) and (16) with Y (x) = n(x). Note that χ(r) = ρδ(r) (i.e., h = 0) for a translationally invariant Poisson point process. Positive and negative pair correlations are deﬁned as those instances in which h is positive (i.e., g2 > 1) and h is negative (i.e., g2 < 1), respectively. The Fourier transform of the distribution-valued function χ(r) is given by

χ˜(k) = ρ + ρ2h˜(k), (28)

where h˜(k) is the Fourier transform of h(r). It is common practice in statistical physics to deal with a function trivially related to the spectral function χ˜(k) called the structure factor S(k), i.e.,

χ˜(k) ρ

= 1 + ρh˜(k). (29)

S(k) ≡

![image 32](<2005-torquato-new-conjectural-lower-bounds_images/imageFile32.png>)

A natural question to ask at this point is the following: Given a positive number density ρ and a pair correlation function g2(r), does there exist a translationally invariant point process in Rd with measure P for which ρ and g2 are one-point and two-point correlation functions, respectively. Two obvious nonnegativity conditions [TS02] that must be satisﬁed are the following:

g2(r) ≥ 0 for all r (30) and

S(k) = 1 + ρh˜(k) ≥ 0 for all k. (31)

The ﬁrst condition is trivial and comes from (20) with n = 2. The second condition is nontrivial and derives from the generalized Wiener-Khintchine theorem (3.2) using relations (28) and (29). However, for realizability of point processes in arbitrary dimension d, the two standard conditions (30) and (31) are only necessary, not necessary and suﬃcient. The

same state of aﬀairs applies to the theory of random sets [Tor02], where it is known that the Wiener-Khintchine theorem only provides a necessary condition on realizable autocovariance functions. The simplest example of a random set is one in which Rd is partitioned into two disjoint regions (phases) but with an interface that is only known in a probabilistic sense. (A packing can therefore be viewed as a special random set). Thus, a random set is described by a random variable that is the indicator function for a particular phase, i.e., it is a binary stochastic process. The class of autocovariances that comes from a binary stochastic process is a subclass of the total class that comes from an ordinary process {Y (x) : x ∈ Rd} and meets the existence condition of Theorem 3.2. Similarly, the class of autocovariances that comes from a point process is a subset of of a generalized process {Y (Φ(x)) : x ∈ Rd} and therefore the existence condition of Theorem 3.2 is only necessary.

It has recently come to light that a positive g2 for a positive ρ must satisfy an uncountable number of necessary and suﬃcient conditions for it to correspond to a realizable point process [CL04]. However, these conditions are very diﬃcult (or, more likely, impossible) to check for arbitrary dimension. In other words, given ρ1 = ρ and ρ2 = ρ2g2, it is diﬃcult to ascertain if there are some higher-order functions ρ3, ρ4, . . . for which these one- and two-point correlation functions hold. Thus, an important practical problem becomes the determination of a manageable number of necessary conditions that can be readily checked.

One such additional necessary condition, obtained by Yamada [Yam61], is concerned with σ2(A) ≡ (N(A) − N(A) )2 , the variance in the number of points N(A) contained within a window A ⊂ Rd. Speciﬁcally, he showed that

σ2(A) ≥ θ(1 − θ), (32)

where θ is the fractional part of the expected number of points ρ|A| contained in the window. This inequality is a consequence of the fact that the number of points N(A) within a window

- at some ﬁxed position is an integer, not a continuous variable, and sets a lower limit on the number variance. We note in passing that the determination of the number variance for lattice point patterns is an outstanding problem in number theory [Ken48, KR53, SS05]. The number variance for a speciﬁc choice of A is necessarily a positive number and generally related to the total pair correlation function h(r) for a translationally invariant point process [TS03]. In the special case of a spherical window of radius R in Rd, it is explicitly given by


σ2(R) = ρv1(R) 1 + ρ

h(r)α2(r; R) dr ≥ θ(1 − θ), (33)

Rd

where σ2(R) is the number variance for a spherical window of radius R in Rd, v1(R) is the volume of the window, and α2(r; R) is the volume common to two spherical windows of radius

R whose centers are separated by a distance r divided by v1(R). We will call α2(r; R) the scaled intersection volume. The lower bound (33) provides another integral condition on the pair correlation function.

For large R, it has been proved that σ2(R) cannot grow more slowly than γRd−1, where γ is a positive constant [Bec87]. This implies that the Yamada lower bound in (33) is always satisﬁed for for suﬃciently large R for any d ≥ 2. In fact, we have not been able to construct any examples of a pair correlation function g2(r) at some number density ρ that satisfy the two nonnegativity conditions (30) and (31) and simultaneously violate the Yamada condition for any R and any d ≥ 2. Thus, it appears that the Yamada condition is most relevant in one dimension, especially in those cases when σ2(R) is bounded. We note that point processes (translationally invariant or not) for which σ2(R) ∼ Rd−1 for large R are examples of hyperuniform point patterns [TS03]. This classiﬁcation includes all lattices as well as aperiodic point patterns. Hyperuniformity implies that the structure factor S(k) has the following small k behavior:

lim

S(k) = 0. (34)

k→0

The scaled intersection volume α2(r; R) appearing in (33) will play a prominent role in this paper. It has support in the interval [0, 2R), the range [0, 1] and the following integral representation:

cos−1(r/(2R))

sind(θ) dθ, (35) where c(d) is the d-dimensional constant given by

α2(r; R) = c(d)

0

2Γ(1 + d/2) π1/2Γ((d + 1)/2)

c(d) =

. (36)

![image 33](<2005-torquato-new-conjectural-lower-bounds_images/imageFile33.png>)

Following the analysis given by Torquato and Stillinger [TS03] for low dimensions, we obtain the following new series representation of the scaled intersection volume α2(r; R) for r ≤ 2R and for any d:

∞

α(r; R) = 1 − c(d)x + c(d)

n=2

(d − 1)(d − 3) · · ·(d − 2n + 5)(d − 2n + 3) (2n − 1)2 · 4 · 6 · (2n − 4)(2n − 2)

(−1)n

x2n−1, (37)

![image 34](<2005-torquato-new-conjectural-lower-bounds_images/imageFile34.png>)

where x = r/(2R). This is easily proved with the help of Maple. For even dimensions, relation (37) is an inﬁnite series, but for odd dimensions, the series truncates such that α2(r; R) is a univariate polynomial of degree d. Except for the ﬁrst term of unity, all of the terms in (37) involve only odd powers of x. Figure 1 shows graphs of the scaled intersection volume α2(r; R) as a function of r for the ﬁrst ﬁve space dimensions. For any dimension, α(r; R) is a

monotonically decreasing function of r. At a ﬁxed value of r in the interval (0, 2R), α2(r; R) is a monotonically decreasing function of the dimension d. For large d, we will subsequently make use of the asymptotic result

α2(R; R) ∼

6 π

![image 35](<2005-torquato-new-conjectural-lower-bounds_images/imageFile35.png>)

1/2 3 4

![image 36](<2005-torquato-new-conjectural-lower-bounds_images/imageFile36.png>)

d/2 1 d1/2

. (38)

![image 37](<2005-torquato-new-conjectural-lower-bounds_images/imageFile37.png>)

- 0.8
- 1


Spherical window of radius R

0.6

d=1

α(r;R)

0.4

d=5

0.2

0

0 0.4 0.8 1.2 1.6 2

r/(2R)

- Figure 1: The scaled intersection volume α2(r; R) for spherical windows of radius R as a function of r for the ﬁrst ﬁve space dimensions. The uppermost curve is for d = 1 and lowermost curve is for d = 5.


Before closing this section, it is useful to note that there has been some recent work that demonstrates the existence of point processes for a speciﬁc ρ and g2 provided that ρ and g2 meet certain restrictions. For example, Ambartzumian and Sukiasian proved the existence of point processes that come from Gibbs measures for a special g2 for suﬃciently small ρ [AS91]. Determinantal point processes have been considered by Soshnikov [Sos00] and Costin and Lebowitz [CL04]. Costin and Lebowitz have also studied certain one-dimensional renewal point processes [CL04]. Stillinger and Torquato [ST04] discussed the possible existence of a general interparticle pair potential (associated with a Gibbs measure) for a given ρ and

- g2 using a cluster expansion procedure but did not address the issue of convergence of this expansion. Koralov [Kor05] indeed proves the existence of a pair potential on a lattice (with the restriction of single occupancy per lattice site) for which ρ is the density and g2 is the pair correlation function for suﬃciently small ρ and g2. There is no reason to believe that Koralov’s proof is not directly extendable to the case of a point process corresponding to a sphere packing in Rd, where the nonoverlap condition is the analog of single occupancy on the lattice. Thus, we expect that one can prove the existence of a pair potential in Rd


corresponding to a sphere packing for a given ρ and g2 provided that ρ and g2 suﬃciently small.

# 4 Disordered Packings in High Dimensions and the Decorrelation Principle

In this section, we examine the asymptotic behavior of certain disordered packings in high dimensions and show that unconstrained spatial correlations vanish asymptotically, yielding a decorrelation principle. We deﬁne a disordered packing in Rd to be one in which the pair correlation function g2(r) decays to its long-range value of unity faster than |r|−d−ε for some ε > 0. The decorrelation principle as well as a number of other results (that will be discussed in Section 5) motivate us to propose a conjecture in Section 5 that describes the circumstances in which the two standard nonnegativity conditions (30) and (31) are necessary and suﬃcient to ensure the existence of a disordered sphere packing.

## 4.1 Example 1: Disordered Sequential Packings

First we show that there exists a disordered sphere packing that realizes the greedy lower bound (7) (φ = 1/2d) for all d. Then we study the asymptotic properties of the n-particle correlation functions in the large dimension limit.

The disordered packing that achieves the greedy lower bound is a special case of a generalization of the so-called random sequential addition (RSA) process [Tor02]. This generalization, which we introduce here, is a subset of the Poisson point process. Speciﬁcally, the centers of “test” spheres of unit diameter arrive continually throughout Rd during time t ≥ 0 according to a translationally invariant Poisson process of density per unit time η, i.e., η is the number of points per unit volume and time. Therefore, the expected number of centers in a region of volume Ω during time t is ηΩt and the probability that this region is empty of centers is exp(−ηΩt). However, this Poisson distribution of test spheres is not a packing because the spheres can overlap. To create a packing from this point process, one must remove test spheres such that no sphere center can lie within a spherical region of unit radius from any sphere center. Without loss of generality, we will set η = 1.

There is a variety of ways of achieving this “thinning” process such that the subset of points correspond to a sphere packing. One obvious rule is to retain a test sphere at time t only

if it does not overlap a sphere that was successfully added to the packing at an earlier time. This criterion deﬁnes the well-known RSA process in Rd [Tor02], and is clearly a statistically homogeneous and isotropic sphere packing in Rd with a time-dependent density φ(t). In the limit t → ∞, the RSA process corresponds to a saturated packing with a maximal or saturation density φs(∞) ≡ limt→∞ φ(t). In one dimension, the RSA process is commonly known as the “car parking problem”, which Re´nyi showed has a saturation density φs(∞) = 0.7476 . . . [Re´n63]. For 2 ≤ d < ∞, an exact determination of φs(∞) is not possible, but estimates for it have been obtained via computer experiments for low dimensions [Tor02]. However, as we will discuss below, the standard RSA process at small times (or, equivalently, small densities) can be analyzed exactly.

Another thinning criterion retains a test sphere centered at position r at time t if no other test sphere is within a unit radial distance from r for the time interval κt prior to t, where κ is a positive constant in the interval [0, 1]. This packing is a subset of the RSA packing, and therefore we refer to it as the generalized RSA process. Note that when κ = 0, the standard RSA process is recovered, and when κ = 1, a relatively unknown model due to Mat´ern [Mat86] is recovered. The latter is amenable to exact analysis.

The time-dependent density φ(t) in the case of the generalized RSA process with κ = 1 is easily obtained. (Note that for any 0 < κ ≤ 1, the generalized RSA process is always an unsaturated packing.) In this packing, a test sphere at time t is accepted only if does not overlap an existing sphere in the packing as well as any previously rejected test sphere (which we will call “ghost” spheres.) An overlap cannot occur if a test sphere is outside a unit radius of any successfully added sphere or ghost sphere. Because of the underlying Poisson process, the probability that a trial sphere is retained at time t is given by exp(−v1(1)t), where v1(1) is the volume of a sphere of unit radius having the same center as the retained sphere of radius 1/2. Therefore, the expected number density ρ(t) and packing density φ(t) at any time t are respectively given by

ρ(t) =

t

exp(−v1(1)t′) dt′ =

0

1 v1(1)

[1 − exp(−v1(1)t)] (39)

![image 38](<2005-torquato-new-conjectural-lower-bounds_images/imageFile38.png>)

and

- 1

![image 39](<2005-torquato-new-conjectural-lower-bounds_images/imageFile39.png>)

- 2d


φ(t) = ρ(t)v1(1/2) =

[1 − exp(−v1(1)t)]. (40) We see that φ(t) is a monotonically increasing function of t. This result was ﬁrst given by Mat´ern using a diﬀerent approach and he also gave a formal expression for the time-dependent radial distribution function g2(r; t) (see Section 3). Here we present an explicit expression for

g2(r; t) at time t for any dimension d:

1 − exp[−2dβ2(r; 1)t] β2(r; 1)

Θ(r − 1) 22d−1[β2(r; 1) − 1]φ2(t)

2dφ(t) −

. (41)

g2(r; t) =

![image 40](<2005-torquato-new-conjectural-lower-bounds_images/imageFile40.png>)

![image 41](<2005-torquato-new-conjectural-lower-bounds_images/imageFile41.png>)

Here

- 0, x < 0,
- 1, x ≥ 0,


(42) is the unit step function and

Θ(x) =

β2(r; R) = 2 − α2(r; R) (43) is the union volume of two spheres of radius R (whose centers are separated by a distance r) divided by the volume of a sphere of radius R and α2(r; R) is the scaled intersection volume of two such spheres given by (35). Our approach for obtaining (41) is diﬀerent than Mat´ern’s and details are given elsewhere [TS06].

It is useful to note that at small times or, equivalently, low densities, formula (40) yields the asymptotic expansion φ(t) = v1(1)t/2d −v12(1)t2/2d+1 +O(t3), which when inverted yields t = 2dφ/v1(1) + 2d−1φ2 + O(φ3). Substitution of this last result into (41) gives

g2(r; φ) = Θ(r − 1) + O(φ3), (44)

which implies that g2(r; φ) tends to the unit step function Θ(r −1) as φ → 0 for any ﬁnite d.

1.6

1.4

d=1

1.2

- 0.8
- 1


d=5

∞g(r;)2

0.6

0.4

0.2

0

0 0.5 1 1.5 2 2.5

r

- Figure 2: Radial distribution function for the ﬁrst ﬁve space dimensions at the maximum density φ = 1/2d for the generalized RSA model with κ = 1.


In the limit t → ∞, the maximum density is given by

- 1

![image 42](<2005-torquato-new-conjectural-lower-bounds_images/imageFile42.png>)

- 2d


φ(∞) ≡ lim

φ(t) =

t→∞

(45)

and

Θ(r − 1) 1 − α2(r; 1)/2

2Θ(r − 1) β2(r; 1)

. (46) We see that the greedy lower-bound limit on the density is achieved in the inﬁnite-time limit for this sequential but unsaturated packing. This is the ﬁrst time that such an observation has been made. Obviously, for any 0 ≤ κ < 1, the maximum (inﬁnite-time) density of the generalized RSA packing is bounded from below by 1/2d (the maximum density for κ = 1). Note also that because β2(r; 1) is equal to 2 for r ≥ 2, g2(r; ∞) = 1 for r ≥ 2, i.e., spatial correlations vanish identically for all pair distances except those in the small interval [0, 2). Even the positive correlations exhibited for 1 < r < 2 are rather weak and decrease with increasing dimension. The function g2(r; ∞) achieves its largest value at r = 1+ in any dimension and for d = 1, g2(1+; ∞) = 4/3. The radial distribution function g2(r; ∞) is plotted in Fig. 2 for the ﬁrst ﬁve space dimensions. Using the asymptotic result (38) and relation (46), it is seen that for large d,

=

g2(r; ∞) ≡ lim

g2(r; t) =

![image 43](<2005-torquato-new-conjectural-lower-bounds_images/imageFile43.png>)

![image 44](<2005-torquato-new-conjectural-lower-bounds_images/imageFile44.png>)

t→∞

Θ(r − 1) 1 −

g2(1+; ∞) ∼

, (47)

![image 45](<2005-torquato-new-conjectural-lower-bounds_images/imageFile45.png>)

1/2 3 4

d/2 1 d1/2

3 2π

![image 46](<2005-torquato-new-conjectural-lower-bounds_images/imageFile46.png>)

![image 47](<2005-torquato-new-conjectural-lower-bounds_images/imageFile47.png>)

![image 48](<2005-torquato-new-conjectural-lower-bounds_images/imageFile48.png>)

and thus g2(r; ∞) tends to the unit step function Θ(r − 1) exponentially fast as d → ∞ because the scaled intersection volume α2(1; 1) vanishes exponentially fast.

The higher-order correlation functions for this model have not been given previously. In another work [TS06], we use an approach diﬀerent from the one used by Mat´ern to obtain not only g2 but an explicit formula for the general n-particle correlation function gn, deﬁned by (21), for any time t and n and for arbitrary dimension d. To our knowledge, this represents the ﬁrst exactly solvable disordered sphere packing model for any d. These details are somewhat tangential to the present work and for our purposes it suﬃces to state the ﬁnal result in the limit t → ∞ for n ≥ 2:

n

Θ(rij − 1)

n

i<j

gn−1(Qi; ∞) (48)

gn(r1, . . ., rn; ∞) =

![image 49](<2005-torquato-new-conjectural-lower-bounds_images/imageFile49.png>)

βn(r1, . . ., rn; 1)

i=1

where the sum is over all the n distinguishable ways of choosing n−1 positions from n positions r1, . . .rn and the arguments of gn−1 are the associated n−1 positions, which we denote by Qi,

and g1 ≡ 1. Moreover, βn(r1, . . ., rn; R) is the union volume of n congruent spheres of radius R, whose centers are located at r1, . . ., rn, where rij = |rj − ri| for all 1 ≤ i < j ≤ n, divided by the volume of a sphere of radius R.

Lemma 4.1 In the limit d → ∞, the n-particle correlation function gn(r1, . . ., rn; ∞) ∼ 1 uniformly in (r1, . . ., rn) ∈ Rd such that rij ≥ 1 for all 1 ≤ i < j ≤ n. If rij < 1 for any pair of points ri and rj, then gn(r1, . . ., rn; ∞) = 0.

Proof: The second part of the Lemma is the trivial requirement for a packing. Whenever rij ≥ 1 for all 1 ≤ i < j ≤ n, it is clear from (48) that we have the following upper and lower bounds on the n-particle correlation function:

ngn∗−1 βn

n βn ≤ gn ≤

, (49)

![image 50](<2005-torquato-new-conjectural-lower-bounds_images/imageFile50.png>)

![image 51](<2005-torquato-new-conjectural-lower-bounds_images/imageFile51.png>)

where gn∗−1 denotes the largest possible value of gn−1. The scaled union volume βn of n spheres obeys the bounds

n −

α2(rij; 1) ≤ βn ≤ n, (50)

i<j

but since the scaled intersection volume of two spheres α2(r; 1) attains its maximum value for r ≥ 1 when r = 1, we also have

n(n − 1) 2

α2(1; 1) ≤ βn ≤ n. (51) Use of this inequality and the recursive relation (48) yields the bounds

n −

![image 52](<2005-torquato-new-conjectural-lower-bounds_images/imageFile52.png>)

1 1 −

1 ≤ gn ≤

. (52)

![image 53](<2005-torquato-new-conjectural-lower-bounds_images/imageFile53.png>)

n(n − 1)α2(1; 1) 4

+ O(α2(1; 1)2)

![image 54](<2005-torquato-new-conjectural-lower-bounds_images/imageFile54.png>)

Using the asymptotic result (38), we see that the upper bound tends to the lower bound for any given n as d → ∞, which proves the Lemma.

In summary, the Lemma enables us to conclude that in the limit d → ∞ and for φ = 1/2d

n

g2(rij; ∞), (53)

gn(r12, . . ., r1n; ∞) ∼

i<j

where

g2(r; ∞) ∼ Θ(r − 1). (54)

Importantly, we see that the asymptotic behavior of g2 in the low-density limit φ → 0 for any d [cf. (44)] is the same as the high-dimensional limit d → ∞ [cf. (54)], i.e., spatial

correlations, which exist for positive densities at ﬁxed d, vanish for pair distances beyond the hard-core diameter. Note also that gn for n ≥ 3 asymptotically factorizes into products involving only the pair correlation function g2. Is the similarity between the low-density and high-dimensional limits for this model of a disordered packing a general characteristic of disordered packings? In what follows, we discuss another disordered packing that has this attribute and subsequently formulate what we refer to as a “decorrelation principle.”

## 4.2 Example 2: The Classic Gibbsian Hard-Sphere Packing

The statistical mechanics of the classic Gibbsian hard-sphere packing is well established (see [Tor02] and references therein). The purpose of this subsection is simply to collect some results that motivate the decorrelation principle. Let ΦN(rN) be the N-body interaction potential for a ﬁnite but large number of particles with conﬁguration rN ≡ {r1, r2, . . ., rN} in a volume

- V in Rd at absolute temperature T. A large collection of such systems in which N, V and T are ﬁxed but in which the particle conﬁgurations are otherwise free to vary is called the Gibbs canonical ensemble. Our interest is in the thermodynamic limit, i.e., the distinguished limit in which N → ∞ and V → ∞ such that the number density ρ = N/V exists. For a Gibbs canonical ensemble, when the n-particle densities ρn (deﬁned in Section 3) exist, they are entirely determined by the interaction potential ΦN(rN). For a hard-sphere packing, the interaction potential is given by a sum of pairwise terms such that


ΦN(rN) =

N

u2(|rj − ri|). (55)

i<j

where u2(r) is the pair potential deﬁned by

+ ∞, r < 1, 0, r ≥ 1,

u2(r) =

(56)

Thus, the particles do not interact for interparticle separation distances greater than or equal to unity but experience an inﬁnite repulsive force for distances less than unity. The hard spheres have kinetic energy, and therefore a temperature, but the temperature enters in a trivial way because the conﬁgurational correlations between the spheres are independent of the temperature. We call this the classic equilibrium sphere packing, which is both translationally and rotationally invariant.

In one dimension, the n-particle densities ρn for such packings are known exactly in the thermodynamic limit. The density φ lies in the interval [0, 1] but this one-dimensional

6.0

d=3

φ=0.49

5.0

4.0

()gr2

3.0

2.0

1.0

0.0

0.0 1.0 2.0 3.0 4.0 5.0 r

- Figure 3: The radial distribution function for the classic three-dimensional equilibrium packing at φ = 0.49 as obtained from molecular dynamics computer simulations. The graph is adapted from Figure 3.15 of Torquato [Tor02].


packing is devoid of a discontinuous (ﬁrst-order) transition from a disordered (liquid) phase to an ordered (solid) phase. Although a rigorous proof for the existence of a liquid-to-solid phase transition in two or three dimensions is not yet available, there is overwhelming numerical evidence (as obtained from computer simulations) that such a transformation takes place at suﬃciently high densities. The maximal densities for equilibrium sphere packings in two and three dimensions are φmax = π/√12 and φmax = π/√18, respectively, i.e., they correspond to the density of the densest sphere packing in the respective dimension.

![image 55](<2005-torquato-new-conjectural-lower-bounds_images/imageFile55.png>)

![image 56](<2005-torquato-new-conjectural-lower-bounds_images/imageFile56.png>)

Figure 3 shows the three-dimensional radial distribution function as obtained from computer simulations for a density φ = 0.49, which is near the maximum value for the stable disordered branch. It is seen that the packing exhibits short-range order [i.e., g2(r) has both positive and negative correlations for small r], but g2(r) decays to its long-range value exponentially fast after several diameters. By contrast, in the limit d → ∞, it has been shown that the “pressure” [Rue99] of an equilibrium packing is exactly given by the ﬁrst two terms of its asymptotic low-density expansion for some positive density interval [0, φ0] [WRF87, FP99]. (Roughly speaking, the pressure is the average force per unit area acting on an “imaginary planar wall” in the packing due collisions between the spheres and the wall.) Frisch and Percus [FP99] have established, albeit not rigorously, that φ0 = 1/2d. This result for the pressure implies that the leading-order term of the low-density expansion of the radial distribution

function in arbitrary dimension [Tor02]

g2(r) = Θ(r − 1) 1 + 2dα2(r; 1)φ + O(φ2) (57)

becomes asymptotically exact in the limit d → ∞ in the same density interval. The presence of the unit step function Θ(r − 1) in relation (57) means that the scaled intersection volume α2(r; 1) need only be considered for values of r in the interval [1, 2]. Since α2(r; 1) is largest when r = 1 for 1 ≤ r ≤ 2 and α2(1; 1) has the asymptotic behavior (38), the product 2dα2(1; 1)φ vanishes no more slowly than (6/π)1/2/[(4/3)d/2d1/2] in the limit d → ∞ for 0 ≤ φ ≤ 1/2d, and therefore g2(r) tends to Θ(r − 1) exponentially fast. In summary, we see again that spatial correlations that exist in low dimensions for r > 1 completely vanish in the limit d → ∞. Moreover, this is yet another disordered packing model in which the high-dimensional asymptotic behavior corresponds to the low-density asymptotic behavior.

The corresponding n-particle correlation function gn, deﬁned by (21), in the low-density limit [Sal58] is given by

gn(r12, . . ., r1n) =

n

g2(rij) 1 + 2dαn(r12, . . ., r1n; 1)φ + O(φ2) (58)

i<j

where αn(r12, . . ., r1n; R) is the intersection volume of n congruent spheres of radius R (whose centers are located at r1, . . ., rn, where rij = rj − ri for all 1 ≤ i < j ≤ n) divided by the volume of a sphere of radius R. The scaled intersection volume αn(r12, . . ., r1n; R)/n has the range [0, 1]. Now since α2(rij, 1) ≥ αn(r12, . . ., r1n; 1) for any pair distance rij = |rij| such that 1 ≤ i < j ≤ n, then it follows from the analysis above that in the limit d → ∞ for

- 0 ≤ φ ≤ 1/2d g2(r) ∼ Θ(r − 1) (59)


and

n

g2(rij). (60)

gn(r12, . . ., r1n) ∼

i<j

Again, as in the generalized RSA example with κ = 1, gn factorizes into products involving only g2’s in the limit d → ∞. Moreover, we should also note that the standard RSA process (generalized RSA process with κ = 0) has precisely the same asymptotic low-density behavior

- as the standard Gibbs hard-sphere model [Tor02]. More precisely, these two models share


the same low-density expansions of the gn through terms of order φ and therefore the same asymptotic expressions (59) and (60).

## 4.3 Decorrelation Principle

The previous two examples illustrate two important and related asymptotic properties that are expected to apply to all disordered packings:

- 1. the high-dimensional asymptotic behavior of g2 is the same as the asymptotic behavior in the low-density limit for any ﬁnite d, i.e., unconstrained spatial correlations, which exist for positive densities at ﬁxed d, vanish asymptotically for pair distances beyond the hard-core diameter in the high-dimensional limit;
- 2. and gn for n ≥ 3 asymptotically can be inferred from a knowledge of only the pair correlation function g2 and number density ρ.


What is the explanation for these two related asymptotic properties? Because we know from the Kabatiansky and Levenshtein (1979) asymptotic upper bound on the maximal density that φ must go to zero at least as fast as 2−0.5990d for large d, unconstrained spatial correlations between spheres must vanish, i.e., statistical independence is established. (An example of constrained spatial correlations is described below.) Such a decorrelation means that the gn for n ≥ 3 are determined entirely from a knowledge of the decorrelated pair correlation function g2. In the speciﬁc examples that we considered, the gn factorize into products involving only g2’s, but there may be other decompositions. For example, the gn for n ≥ 3 can be functionals that only involve ρ and g2. We will call the two asymptotic properties the decorrelation principle for disordered packings. This principle as well as other results described in Section

- 5 leads us to a conjecture concerning the existence of disordered sphere packings in high dimensions, which we state in Section 5.1.


An example of constrained spatial correlations that would not vanish asymptotically is illustrated in Fig. 4, where we show the pair correlation function g2(r) for a three-dimensional sphere packing near the so-called maximally random jammed state [TTD00, Tor02]. A special feature of g2(r) for a maximally random jammed packing is a delta-function contribution

- at r = 1, which reﬂects the fact that the average kissing number (i.e., average number of contacting particles per particle) is eﬀectively six for this collectively jammed packing, meaning that the packing is isostatic [DST05]. A positive average kissing number is required if the packing is constrained to be jammed and in Rd this means that the average kissing number is 2d for either collective or strict jamming [DST05]. Isostatic packings are jammed packings with the minimum number of contacts for a particular jamming category. According to the Decorrelation Principle, as d tends to inﬁnity, g2 for a maximally random jammed packing


- 0
- 1
- 2
- 3
- 4
- 5


| | |
|---|---|


g(r)2

0 1 2 3

r

- Figure 4: The radial distribution function of a three-dimensional packing of spheres near the maximally random jammed state [TTD00, Tor02] at a density φ = 0.64 as obtained from computer simulations [TS02]. The delta function contribution at r = 1 (of course, not explicitly shown) corresponds to an average kissing number of about six.

would retain this delta-function contribution but the unconstrained spatial correlations beyond r = 1 would vanish. Of course, the manner in which the g2 shown in Fig. 4 approaches the asymptotic limit of a step function Θ(r − 1) plus a delta-function contribution at r = 1 is crucial. We note that maximally random jammed packings contain about 2–3% rattler spheres, i.e., spheres trapped in a cage of jammed neighbors but free to move within the cage.

- 5 New Approach to Lower Bounds


The salient ideas behind our new approach to the derivation of lower bounds on φmax were actually laid out in our earlier work [TS02]. The main objective of that work was to study sphere packings in three dimensions in which long-range order was suppressed and shortrange order was controlled (i.e., disordered sphere packings in ℜ3) using so-called g2-invariant processes. A g2-invariant process is one in which a given nonnegative pair correlation g2(r) function remains invariant for all r over the range of densities

0 ≤ φ ≤ φ∗. (61)

The terminal density φ∗ is the maximum achievable density for the g2-invariant process subject to satisfaction of the structure factor S(k) inequality (31). A ﬁve-parameter test family of

g2’s had been considered, which incorporated the known features of core exclusion, contact pairs, and damped oscillatory short-range order beyond contact. The problem of ﬁnding the maximal packing fraction φ∗ was posed as an optimization problem: maximize φ over the set of parameters subject to the constraints (30) and (31). We noted in passing that when the damped-oscillatory contribution to g2 was set equal to zero, the optimization problem could be solved analytically for all space dimensions, leading to a terminal density φ∗ = (d+2)/2d+1. Under the assumption that such a g2 was a realizable packing, we also observed that this φ∗ was a lower bound on the maximal density for any sphere packing [i.e., φmax ≥ (d + 2)/2d+1] because the terminal density would have been higher by including the damped-oscillatory contribution to g2. This conjectural lower bound was noted to provide linear improvement over Minkowski’s lower bound, but we were not aware of Ball’s similar lower bound [Bal92] at the time. Since our original 2002 paper, we also learned about other necessary conditions for the realizability of a point process for a given number density ρ and g2, such as Yamada’s condition (32). In any event, our brief remarks about lower bounds on sphere packings were not intended to be mathematically rigorous.

It is our intent here to make our optimization methodology to obtain lower bounds on φmax more mathematically precise, especially in light of recent developments and the considerations of the previous two sections. We then apply the optimization procedure to provide alternative derivations of previous lower bounds as well as a new bound.

We will consider those “test” g2(r)’s that are distributions on Rd depending only on the radial distance r such that h(r) = g2(r) − 1. For any test g2(r), we want to maximize the corresponding density φ satisfying the following three conditions:

- (i) g2(r) ≥ 0 for all r,
- (ii) supp(g2) ⊆ {r : r ≥ 1},
- (iii)


∞

d 2

S(k) = 1 + ρ(2π)

![image 57](<2005-torquato-new-conjectural-lower-bounds_images/imageFile57.png>)

0

J(d/2)−1(kr) (kr)(d/2)−1

rd−1[g2(r) − 1]

dr ≥ 0 for all k.

![image 58](<2005-torquato-new-conjectural-lower-bounds_images/imageFile58.png>)

We will call the maximum density the terminal density and denote it by φ∗. Remarks:

- 1. The conditions (i)–(iii) are just recapitulations of (25), (30), and (31) for this class of test functions. We will call condition (ii) the hard-core constraint.
- 2. When there exist sphere packings with g2 satisfying conditions (i)–(iii) for φ in the interval


[0, φ∗], then we have the lower bound on the maximal density given by

φmax ≥ φ∗. (62) The best lower bound would be obtained if one could probe the entire class of test functions. In practice, we will consider here only a small subset of test functions and in particular those that are amenable to exact asymptotic analysis. In some instances, we will associate with the terminal density φ∗ an optimized average kissing number Z∗. Thus, whenever inequality (62) applies, the maximal kissing number Zmax is bounded from below by Z∗, i.e.,

Zmax ≥ Z∗. (63)

In the next subsection, we put forth a conjecture that states when the conditions (i)–(iii) are necessary and suﬃcient for the existence of disordered sphere packings.

- 3. Remarkably, the optimization problem deﬁned above is identical to one formulated by Cohn [Coh02]. In particular, it is the dual of the primal inﬁnite-dimensional linear program that Cohn employed with Elkies [CE03] to obtain upper bounds on the maximal packing density. One need only replace S(k) with gˆ − cδ(k), where c plays the role of number density, g is a tempered distribution and gˆ is its Fourier transform in Cohn’s notation. Thus, even if there does not exist a sphere packing with g2 satisfying conditions (i)–(iii), our formulation has implications for upper bounds on φmax, which we discuss in Section 6. For ﬁnite-dimensional linear programs (and many inﬁnite-dimensional ones) there is no “duality gap,” i.e., the optima of the primal and dual programs are equal. However, in this inﬁnite-dimensional setting, it is not clear how to prove that there is no duality gap [Coh02]. Therefore, it is rigorously


true that the terminal density φ∗ can never exceed the Cohn-Elkies upper bound, which is a desirable feature of our formulation, otherwise the terminal density could never correspond to a rigorous lower bound.

We will show that for the test radial distribution functions considered in this paper, the Yamada condition (32) is only relevant in one dimension, and even then in just some cases. A remark about the Yamada condition for sphere packings is in order here. In earlier work [TS03], we observed that for any sphere packing of congruent spheres, the number variance for a spherical window of radius R deﬁned by (33) obeys the lower bound

σ2(R) ≥ 2dφRd 1 − 2dφRd (64)

for any R. This is a tight bound for suﬃciently small R and is exact for R ≤ 1/2. However, we note here that provided that 2dφRd ≤ 1, the Yamada lower bound (32) and lower bound

(64) are identical. Thus, the Yamada lower bound for any sphere packing only needs to be checked for R > R0, where

- 1

![image 59](<2005-torquato-new-conjectural-lower-bounds_images/imageFile59.png>)

- 2φ1/d


. (65)

R0 =

## 5.1 Existence of Disordered Packings in High Dimensions

We have seen that a necessary condition for the existence of a translationally invariant point process with a speciﬁed positive ρ and nonnegative g2 is that S(k) is nonnegative [cf. (31)]. In other words, given ρ and g2, it does not mean that there are some higher-order functions

- g3, g4, . . . for which these one- and two-point correlation functions hold. The function g2 speciﬁes how frequently pair distances of a given length occur statistically in Rd. The thirdorder function g3 reveals how these pair separations are linked into triangles. This additional information generally cannot be inferred from the knowledge of ρ and g2 alone, however. The fourth-order function g4 controls the assembly of triangles into tetrahedra (and is the lowest-order correlation function that is sensitive to chirality) but g4 cannot be determined by only knowing ρ, g2 and g3. In general, gn for any n ≥ 3 is not completely determined from a knowledge of the lower-order correlations functions alone. This is to be contrasted with general stochastic processes in which nonnegativity of ﬁrst- and second-order statistics (mean and autocovariance) are necessary and suﬃcient to establish existence because one can always ﬁnd a Gaussian process with such given ﬁrst- and second-order statistics. For a Gaussian process, ﬁrst- and second-order statistics determine all of the high-order statistics.


There are a number of results that suggest it is reasonable to conclude that the generally necessary nonnegativity conditions for the existence of a disordered sphere packing become necessary and suﬃcient for suﬃciently large d. First, the decorrelation principle of the previous section states that unconstrained correlations in disordered sphere packings vanish asymptotically in high dimensions and that the gn for any n ≥ 3 can be inferred entirely from a knowledge of ρ and g2. Second, as we noted in Section 4, the necessary Yamada condition appears to only have relevance in very low dimensions. Third, we will demonstrate below that other new necessary conditions also seem to be germane only in very low dimensions. Fourth, we will describe numerical constructions of conﬁgurations of disordered sphere packings on the torus corresponding to certain test radial distributions functions in low dimensions for densities up to the terminal density. Finally, we will show that certain test radial distributions functions recover the asymptotic forms of known rigorous bounds. In light of these results, we propose the following conjecture:

Conjecture 5.1 For suﬃciently large d, a hard-core nonnegative tempered distribution g2(r) that satisﬁes g2(r) = 1 + O(|r|−d−ε) for some ε > 0 is a pair correlation function of a translationally invariant disordered sphere packing in Rd at number density ρ if and only if S(k) ≡ 1 + ρh˜(k) ≥ 0. The maximum achievable density is the terminal density φ∗.

Remarks:

- 1. A weaker form of this conjecture would replace the phrase “for suﬃciently large d” with “in the limit d → ∞.”
- 2. Employing the aforementioned optimization procedure with a certain test function g2 and this conjecture, we obtain in what follows conjectural lower bounds that yield the long-sought asymptotic exponential improvement on Minkowski’s bound. Before obtaining this result, we ﬁrst apply the procedure to two simpler test functions that we examined in the past.


## 5.2 Step Function

The simplest possible choice for a radial distribution function corresponding to a disordered packing is the following unit step function:

g2(r) = Θ(r − 1). (66)

This states that all pair distances beyond the hard-core diameter are equally probable, i.e., spatial correlations vanish identically. The corresponding structure factor [cf. condition (iii)] for this test function in any dimension d is given by [TS02]

φ23νΓ(1 + ν) kν

S(k) = 1 −

Jν(k), (67)

![image 60](<2005-torquato-new-conjectural-lower-bounds_images/imageFile60.png>)

where ν = d/2. Since there are no parameters to be optimized here, the terminal density φ∗ is readily obtained by determining the highest density for which the condition (31) is satisﬁed, yielding

- 1

![image 61](<2005-torquato-new-conjectural-lower-bounds_images/imageFile61.png>)

- 2d


φ∗ =

. (68)

Now we show that the Yamada condition (32) is satisﬁed in any dimension for 0 ≤ φ ≤ 2−d. Consider the more general class of radial distribution functions:

0 ≤ g2(r) ≤ 1 for r > 1. (69)

The test function (66) belongs to this class. Note that for any dimension, the scaled intersection volume given by (37) obeys the inequality

r 2R

α2(r; R) ≤ 1 −

![image 62](<2005-torquato-new-conjectural-lower-bounds_images/imageFile62.png>)

for 0 ≤ r ≤ 2R, (70)

where the equality applies when d = 1. For g2(r) satisfying (69), relation (33) and inequality

(70) yield the following lower bound for any d:

σ2(R) ≥ 2dφRd 1 + d2dφ

2R

r 2R

rd−1h(r) 1 −

![image 63](<2005-torquato-new-conjectural-lower-bounds_images/imageFile63.png>)

0

dr . (71)

At φ = 1/2d, the lower bound (71) for the test function (66) is given by

d 2(d + 1)

σ2(R) ≥

Rd−1 (72)

![image 64](<2005-torquato-new-conjectural-lower-bounds_images/imageFile64.png>)

and because R0 = 1 [cf. (65)], we only need to consider R > 1. In particular, the right side of this inequality is smallest at R = 1 so that

d 2(d + 1)

σ2(R) ≥

. (73)

![image 65](<2005-torquato-new-conjectural-lower-bounds_images/imageFile65.png>)

Since σ2(R) ≥ 1/4 for d ≥ 1, Yamada’s condition is satisﬁed for all R for the step function

(66) at φ = 1/2d as well as all φ < 1/2d.

We already established in Section 4 that there exist sphere packings that asymptotically have radial distribution functions given by the simple unit step function (66) for φ ≤ 2−d. Nonetheless, invoking Conjecture 5.1 and terminal density speciﬁed by (68) implies the asymptotic lower bound on the maximal density is given by

φmax ≥

- 1

![image 66](<2005-torquato-new-conjectural-lower-bounds_images/imageFile66.png>)

- 2d


, (74)

which provides an alternate derivation of the elementary bound (7).

Using numerical simulations with a ﬁnite but large number of spheres on the torus, we have been able to construct particle conﬁgurations in which the radial distribution function (sampled at discretized pair distances) is given by the test function (66) in one, two and three dimensions for densities up to the terminal density [CTS03, OST06]. The existence of such a discrete approximation to (66) of course is not conclusive proof of the existence of such packings in low dimensions, but they are suggestive that the standard nonnegativity conditions may be suﬃcient to establish existence in this case for densities up to φ∗.

## 5.3 Step Plus Delta Function

An important feature of any dense packing is that the particles form contacts with one another. Ideally, one would like to enforce strict jamming (see Introduction). The probability that a pair of particles form such contacts at the pair distance r = 1 for the test function (66) is strictly zero. Accordingly, let us now consider the test radial distribution function given by the previous test function plus a delta-function contribution as follows:

g2(r) = Θ(r − 1) +

Z s1(1)ρ

δ(r − 1). (75)

![image 67](<2005-torquato-new-conjectural-lower-bounds_images/imageFile67.png>)

Here s1(r) is the surface area of a d-dimensional sphere of radius r given by (24) and Z is a parameter, which is the average kissing number. Because we allow for interparticle contacts via the second term in (75), the terminal density is expected to be greater than 2−d, which will indeed be the case. The corresponding structure factor [cf. (iii)] for this test function in any dimension d is given by [TS02]

φ23νΓ(1 + ν) kν

Z2νΓ(1 + ν) dkν−1

Jν(k) +

Jν−1(k), (76)

S(k) = 1 −

![image 68](<2005-torquato-new-conjectural-lower-bounds_images/imageFile68.png>)

![image 69](<2005-torquato-new-conjectural-lower-bounds_images/imageFile69.png>)

where ν = d/2. The structure factor for small k can be expanded in a MacLaurin series as follows:

2d−2φ 1 + d/2 −

Z 2d

S(k) = 1 + (Z − 2dφ) +

k2 + O(k4). (77) The last term changes sign if Z increases past 2dφd/(d + 2). At this crossover point,

![image 70](<2005-torquato-new-conjectural-lower-bounds_images/imageFile70.png>)

![image 71](<2005-torquato-new-conjectural-lower-bounds_images/imageFile71.png>)

S(k) = 1 −

2d+1 d + 2

φ + O(k4) (78)

![image 72](<2005-torquato-new-conjectural-lower-bounds_images/imageFile72.png>)

Under the constraint that the minimum of S(k) occurs at k = 0, then we have the exact results

d + 2 2d+1

d 2

φ∗ =

. (79)

, Z∗ =

![image 73](<2005-torquato-new-conjectural-lower-bounds_images/imageFile73.png>)

![image 74](<2005-torquato-new-conjectural-lower-bounds_images/imageFile74.png>)

We see that at the terminal density, the average kissing number Z∗ = d/2, which does not even meet the local jamming criterion described in the Introduction.

The Yamada condition (32) is violated only for d = 1 for the test function (75) at the terminal density speciﬁed by (79). It is easy to verify directly that the Yamada condition becomes less restrictive as the dimension increases from d = 2. Interestingly, we have also shown via numerical simulations that there exist sphere packings possessing radial distribution functions given by the test function (75) (in the discrete approximation) in two and three dimensions for densities up to the terminal density [OST06]. This is suggestive that Conjecture 5.1 for this test function may in fact be stronger than is required.

In the high-dimensional limit, we invoke Conjecture 5.1 and the terminal density given by (79), yielding the conjectural lower bound

φmax ≥

d + 2 2d+1

. (80)

![image 75](<2005-torquato-new-conjectural-lower-bounds_images/imageFile75.png>)

This lower bound provides the same type of linear improvement over Minkowski’s lower bound as does Ball’s lower bound [Bal92].

## 5.4 Step Plus Delta Function with a Gap

The previous test function (75) provided an optimal average kissing number Z∗ = d/2 that did not even meet the local jamming criterion. Experience with disordered jammed packings in low dimensions reveals that the kissing number as well as the density can be substantially increased if there is there is a low probability of ﬁnding noncontacting particles from a typical particle at radial distances just larger than the nearest-neighbor distance. This small-distance negative correlation is clearly manifested in the graph of g2(r) for the three-dimensional maximally random jammed packing (Figure 4) for values of r approximately between 1.1 and 1.5. We would like to idealize this small-distance negative correlation in such a way that it is amenable to exact asymptotic analysis. Accordingly, we consider a test radial distribution function that is similar to the previous one [cf. (75)] but one in which there is a gap between the location of the unit step function and the delta function at ﬁnite d, i.e.,

g2(r) = Θ(r − σ) +

Z s1(1)ρ

δ(r − 1). (81)

![image 76](<2005-torquato-new-conjectural-lower-bounds_images/imageFile76.png>)

The expression contains two adjustable parameters, σ ≥ 1 and Z, which must obviously be constrained to be nonnegative. According to the decorrelation principle of Section 4, the location of the step function r = σ must approach unity asymptotically, i.e., it must approach the previous test function (75). However, as we have emphasized, the manner in which the test function (81) approaches (75) is crucial. Indeed, we will see that the presence of a gap between the unit step function and delta function will indeed lead asymptotically to substantially higher terminal densities.

The structure factor is given by

23νφσdΓ(1 + ν) (kσ)ν

2νZΓ(1 + ν) dkν−1

S(k) = 1 −

Jν(kσ) +

Jν−1(k). (82)

![image 77](<2005-torquato-new-conjectural-lower-bounds_images/imageFile77.png>)

![image 78](<2005-torquato-new-conjectural-lower-bounds_images/imageFile78.png>)

The goal now is to ﬁnd the optimal values of the the adjustable nonnegative parameters Z and σ that maximize the density φ subject to the constraint (iii). This search in two-dimensional

parameter space can be reduced by imposing the further condition that a minimum of the structure factor occurs at k = 0. The MacLaurin expansion of expression (82) gives

S = 1 + [Z − (2σ)dφ] +

2d−1σd+2φ d + 2 −

Z 2d

![image 79](<2005-torquato-new-conjectural-lower-bounds_images/imageFile79.png>)

![image 80](<2005-torquato-new-conjectural-lower-bounds_images/imageFile80.png>)

k2 + O(k4). (83)

Requiring that a zero of S(k) occurs at the origin (hyperuniformity) such that the quadratic coeﬃcient is nonnegative implies the restrictions

Z = (2σ)dφ − 1 (84)

and

(2σ)dφ[dσ2 − (d + 2)] + d + 2 ≥ 0. (85) Combination of (82) and (84) yields the structure factor as

Jν(kσ) (kσ)ν

Jν−1(k) (kσ)ν−1

S(k) = 1 − c1(d)

+ c2(d)

![image 81](<2005-torquato-new-conjectural-lower-bounds_images/imageFile81.png>)

![image 82](<2005-torquato-new-conjectural-lower-bounds_images/imageFile82.png>)

where the d-dependent coeﬃcients c1(d) and c2(d) are given by

, (86)

c1(d) = φσd23νΓ(1 + ν) (87)

Γ(1 + ν) d

c2(d) = [(2σ)dφ − 1]2ν

. (88)

![image 83](<2005-torquato-new-conjectural-lower-bounds_images/imageFile83.png>)

Now the problem reduces to ﬁnding the optimal value of the parameter σ(d) as a function of the space dimension d that maximizes the density φ subject to the constraint (iii). It will be shown below that the optimal σ is of order unity and approaches unity in the limit d → ∞. It immediately follows from (86) and the asymptotic properties of the Bessel functions of ﬁxed order that S(k) → 1 for k → ∞.

In general, S(k) will possess multiple minima and thus we want to ensure that the values of S(k) at each of these minima are all nonnegative. To ﬁnd the minima of S(k), we set its ﬁrst derivative to zero, yielding the relation

c1(d) σν−1

Jν+1(kσ) = c2(d)kJν(k), (89) where we have used the identity

![image 84](<2005-torquato-new-conjectural-lower-bounds_images/imageFile84.png>)

d dx

![image 85](<2005-torquato-new-conjectural-lower-bounds_images/imageFile85.png>)

Jν(x) xν

![image 86](<2005-torquato-new-conjectural-lower-bounds_images/imageFile86.png>)

Jν+1(x) xν

= −

. (90)

![image 87](<2005-torquato-new-conjectural-lower-bounds_images/imageFile87.png>)

For suﬃciently small d (d ≤ 200), the search procedure is carried out numerically using Maple, and is made more eﬃcient by exploiting the fact that the minima of S(k) occur at

70

60

|d=24 d=12<br><br>|
|---|


50

40

S

30

20

10

0

0 10 k 20 30

Figure 5: The optimized structure factor for d = 12 and d = 24.

the real solutions of (89). Figure 5 shows the optimized structure factor for d = 12 and d = 24. Our numerical examination of S(k) for a wide range of d values has consistently shown that the ﬁrst minimum for positive k is the deepest one. Although we have not proven this rigorously, we assume that this is a general result.

We should note that the Yamada condition (32) is violated only for d = 1 for the test function (81) for the terminal density φ∗ and associated optimized parameters σ∗ and Z∗ [calculated via (84)]. One can again verify directly that the Yamada condition becomes less restrictive as the dimension increases from d = 2. However, although the test function (81) for d = 2 with optimized parameters φ∗ = 0.74803, σ∗ = 1.2946 and Z∗ = 4.0148 satisﬁes the Yamada condition, it cannot correspond to a sphere packing because it violates local geometric constraints speciﬁed by σ∗ and Z∗. Speciﬁcally, for an average kissing number of 4.0148, there must be particles that are in contact with at least ﬁve others. But no arrangement of the ﬁve exists which is consistent with the assumed pair correlation function (step plus delta function with a gap from 1 to 1.2946). Simple geometric considerations show that either some pairs of the ﬁve would be forced into the gap, or they would be restricted to ﬁxed separations that would correspond to undesired delta functions beyond the gap. To our knowledge, this is the ﬁrst example of a test radial distribution function that satisﬁes the two standard nonnegativity conditions (30) and (31) and the Yamada condition (32), but cannot correspond to a point process. Thus, there is at least one previously unarticulated necessary condition that has been violated in the low dimension d = 2.

In three dimensions one obtains φ∗ = 0.5758254, σ∗ = 1.246997, and Z∗ = 7.932582. The last of these requires that some nonzero fraction of the spheres must have at least 8 contacting neighbors. We have veriﬁed that valid arrangements of both 8 and 9 contacts are possible, thereby avoiding the analog of the violation encountered in d = 2. As is the case

- d+1φ∗

![image 88](<2005-torquato-new-conjectural-lower-bounds_images/imageFile88.png>)

- d+2 , which is the relative improvement of the terminal density over the gapless-test-function terminal density [cf. (79)].


Table 3: Optimized parameters σ∗, Z∗ and φ∗, and the ratio 2

![image 89](<2005-torquato-new-conjectural-lower-bounds_images/imageFile89.png>)

![image 90](<2005-torquato-new-conjectural-lower-bounds_images/imageFile90.png>)

![image 91](<2005-torquato-new-conjectural-lower-bounds_images/imageFile91.png>)

![image 92](<2005-torquato-new-conjectural-lower-bounds_images/imageFile92.png>)

![image 93](<2005-torquato-new-conjectural-lower-bounds_images/imageFile93.png>)

![image 94](<2005-torquato-new-conjectural-lower-bounds_images/imageFile94.png>)

- d+1φ∗

![image 95](<2005-torquato-new-conjectural-lower-bounds_images/imageFile95.png>)

- d+2


d σ∗ Z∗ φ∗ 2

![image 96](<2005-torquato-new-conjectural-lower-bounds_images/imageFile96.png>)

- 3 1.246997 7.932582 0.5758254 1.842641

![image 97](<2005-torquato-new-conjectural-lower-bounds_images/imageFile97.png>)

![image 98](<2005-torquato-new-conjectural-lower-bounds_images/imageFile98.png>)

![image 99](<2005-torquato-new-conjectural-lower-bounds_images/imageFile99.png>)

![image 100](<2005-torquato-new-conjectural-lower-bounds_images/imageFile100.png>)

- 4 1.212589 13.71016 0.4252472 2.267985

![image 101](<2005-torquato-new-conjectural-lower-bounds_images/imageFile101.png>)

![image 102](<2005-torquato-new-conjectural-lower-bounds_images/imageFile102.png>)

![image 103](<2005-torquato-new-conjectural-lower-bounds_images/imageFile103.png>)

![image 104](<2005-torquato-new-conjectural-lower-bounds_images/imageFile104.png>)

- 5 1.186929 21.97918 0.3048322 2.787037

![image 105](<2005-torquato-new-conjectural-lower-bounds_images/imageFile105.png>)

![image 106](<2005-torquato-new-conjectural-lower-bounds_images/imageFile106.png>)

![image 107](<2005-torquato-new-conjectural-lower-bounds_images/imageFile107.png>)

![image 108](<2005-torquato-new-conjectural-lower-bounds_images/imageFile108.png>)

- 6 1.167000 33.53884 0.2136444 3.418310

![image 109](<2005-torquato-new-conjectural-lower-bounds_images/imageFile109.png>)

![image 110](<2005-torquato-new-conjectural-lower-bounds_images/imageFile110.png>)

![image 111](<2005-torquato-new-conjectural-lower-bounds_images/imageFile111.png>)

![image 112](<2005-torquato-new-conjectural-lower-bounds_images/imageFile112.png>)

- 7 1.151106 49.42513 0.1471058 4.184343

![image 113](<2005-torquato-new-conjectural-lower-bounds_images/imageFile113.png>)

![image 114](<2005-torquato-new-conjectural-lower-bounds_images/imageFile114.png>)

![image 115](<2005-torquato-new-conjectural-lower-bounds_images/imageFile115.png>)

![image 116](<2005-torquato-new-conjectural-lower-bounds_images/imageFile116.png>)

- 8 1.137967 70.88348 0.09985085 5.112364 24 1.058992 5473.546 8.245251e-05 106.4095 36 1.041611 76521.15 2.566299e-07 928.1828 56 1.028036 4.248007e06 1.253255e-11 31140.19 60 1.026330 9.179315e06 1.674130e-12 62262.60 64 1.024823 1.968233e07 2.221414e-13 124175.32 80 1.020211 3.908042e08 6.521679e-17 1.922982e06


![image 117](<2005-torquato-new-conjectural-lower-bounds_images/imageFile117.png>)

![image 118](<2005-torquato-new-conjectural-lower-bounds_images/imageFile118.png>)

![image 119](<2005-torquato-new-conjectural-lower-bounds_images/imageFile119.png>)

![image 120](<2005-torquato-new-conjectural-lower-bounds_images/imageFile120.png>)

![image 121](<2005-torquato-new-conjectural-lower-bounds_images/imageFile121.png>)

![image 122](<2005-torquato-new-conjectural-lower-bounds_images/imageFile122.png>)

![image 123](<2005-torquato-new-conjectural-lower-bounds_images/imageFile123.png>)

![image 124](<2005-torquato-new-conjectural-lower-bounds_images/imageFile124.png>)

![image 125](<2005-torquato-new-conjectural-lower-bounds_images/imageFile125.png>)

![image 126](<2005-torquato-new-conjectural-lower-bounds_images/imageFile126.png>)

![image 127](<2005-torquato-new-conjectural-lower-bounds_images/imageFile127.png>)

![image 128](<2005-torquato-new-conjectural-lower-bounds_images/imageFile128.png>)

![image 129](<2005-torquato-new-conjectural-lower-bounds_images/imageFile129.png>)

![image 130](<2005-torquato-new-conjectural-lower-bounds_images/imageFile130.png>)

![image 131](<2005-torquato-new-conjectural-lower-bounds_images/imageFile131.png>)

![image 132](<2005-torquato-new-conjectural-lower-bounds_images/imageFile132.png>)

![image 133](<2005-torquato-new-conjectural-lower-bounds_images/imageFile133.png>)

![image 134](<2005-torquato-new-conjectural-lower-bounds_images/imageFile134.png>)

![image 135](<2005-torquato-new-conjectural-lower-bounds_images/imageFile135.png>)

![image 136](<2005-torquato-new-conjectural-lower-bounds_images/imageFile136.png>)

![image 137](<2005-torquato-new-conjectural-lower-bounds_images/imageFile137.png>)

![image 138](<2005-torquato-new-conjectural-lower-bounds_images/imageFile138.png>)

![image 139](<2005-torquato-new-conjectural-lower-bounds_images/imageFile139.png>)

![image 140](<2005-torquato-new-conjectural-lower-bounds_images/imageFile140.png>)

![image 141](<2005-torquato-new-conjectural-lower-bounds_images/imageFile141.png>)

![image 142](<2005-torquato-new-conjectural-lower-bounds_images/imageFile142.png>)

![image 143](<2005-torquato-new-conjectural-lower-bounds_images/imageFile143.png>)

![image 144](<2005-torquato-new-conjectural-lower-bounds_images/imageFile144.png>)

![image 145](<2005-torquato-new-conjectural-lower-bounds_images/imageFile145.png>)

![image 146](<2005-torquato-new-conjectural-lower-bounds_images/imageFile146.png>)

![image 147](<2005-torquato-new-conjectural-lower-bounds_images/imageFile147.png>)

![image 148](<2005-torquato-new-conjectural-lower-bounds_images/imageFile148.png>)

100 1.016421 1.478804e10 2.288485e-21 5.688234e08 125 1.013311 1.246172e12 5.610270e-27 3.758024e09 150 1.011214 9.698081e13 1.275632e-32 2.319290e11 175 1.009671 7.086019e15 2.745830e-38 1.485866e13 200 1.008510 4.959086e17 5.667098e-44 9.016510e14

![image 149](<2005-torquato-new-conjectural-lower-bounds_images/imageFile149.png>)

![image 150](<2005-torquato-new-conjectural-lower-bounds_images/imageFile150.png>)

![image 151](<2005-torquato-new-conjectural-lower-bounds_images/imageFile151.png>)

![image 152](<2005-torquato-new-conjectural-lower-bounds_images/imageFile152.png>)

![image 153](<2005-torquato-new-conjectural-lower-bounds_images/imageFile153.png>)

![image 154](<2005-torquato-new-conjectural-lower-bounds_images/imageFile154.png>)

![image 155](<2005-torquato-new-conjectural-lower-bounds_images/imageFile155.png>)

![image 156](<2005-torquato-new-conjectural-lower-bounds_images/imageFile156.png>)

![image 157](<2005-torquato-new-conjectural-lower-bounds_images/imageFile157.png>)

![image 158](<2005-torquato-new-conjectural-lower-bounds_images/imageFile158.png>)

![image 159](<2005-torquato-new-conjectural-lower-bounds_images/imageFile159.png>)

![image 160](<2005-torquato-new-conjectural-lower-bounds_images/imageFile160.png>)

![image 161](<2005-torquato-new-conjectural-lower-bounds_images/imageFile161.png>)

![image 162](<2005-torquato-new-conjectural-lower-bounds_images/imageFile162.png>)

![image 163](<2005-torquato-new-conjectural-lower-bounds_images/imageFile163.png>)

![image 164](<2005-torquato-new-conjectural-lower-bounds_images/imageFile164.png>)

![image 165](<2005-torquato-new-conjectural-lower-bounds_images/imageFile165.png>)

![image 166](<2005-torquato-new-conjectural-lower-bounds_images/imageFile166.png>)

with the Yamada condition (32), this additional necessary condition appears to lose relevance as d increases.

The terminal density φ∗ and the associated optimized parameters σ∗ and Z∗ are listed in Table 3 for selected values of the space dimension between d = 3 and d = 200. Note that for d ≤ 56, the terminal density lies below the density of the densest known packing. For d = 56, the densest arrangement is a lattice (designated by L56,2(M) [Neb98]) with density φ = 2.327670 × 10−11, which is about twice as large as φ∗, as shown in the table. However, for d > 56, φ∗ can be larger than the density of the densest known arrangement. For d = 60, the densest known packing is again a lattice (designated by L56,2(M) [CS98]) with density φ = 2.966747 × 10−13, which is about ﬁve times smaller than φ∗, as shown in the table. The next dimension for which data is available is d = 64, where the densest known packing is the Ne64 lattice [Neb98] with density φ = 1.326615 × 10−12, which is about six times larger than φ∗. The table also reveals exponential improvement of the terminal density φ∗ over the one for the gapless case, i.e., φ∗ = (d + 2)/2d+1. The crucial question is whether such exponential improvement persists in the high-dimensional limit.

To obtain an asymptotic expression for φ∗ for large d, we use the fact that (2σ)dφ ≫ 1, implying that c1(d)/c2(d) → d [cf. (87) and (88)]. Therefore, the minima of S(k) for large d are the solutions of

k d

Jν+1(kσ) σν−1

Jν(k). (91) We see that the locations of the minima depend only on σ (not on φ). The deepest minimum of S(k), after the one at k = 0, is a zero and occurs at the wavenumber k = kmin. [This characteristic is true in any dimension (see Figure 5).] Therefore, S(k = kmin) = 0, c2(d) = c1(d)/d, and relation (82) gives the condition

=

![image 167](<2005-torquato-new-conjectural-lower-bounds_images/imageFile167.png>)

![image 168](<2005-torquato-new-conjectural-lower-bounds_images/imageFile168.png>)

c1(d) kminν

∆ν(kmin) = 1, (92)

![image 169](<2005-torquato-new-conjectural-lower-bounds_images/imageFile169.png>)

where

Jν(kminσ) σν − kmin

Jν−1(kmin) d

∆ν(kmin) =

. (93) The solution of equation (92) produces the desired optimal values of σ∗ and φ∗, where

![image 170](<2005-torquato-new-conjectural-lower-bounds_images/imageFile170.png>)

![image 171](<2005-torquato-new-conjectural-lower-bounds_images/imageFile171.png>)

kminν 23νΓ(1 + ν)σ∗2ν∆ν(kmin)

φ∗ =

. (94)

![image 172](<2005-torquato-new-conjectural-lower-bounds_images/imageFile172.png>)

We ﬁnd the solutions of (91) by linearizing each Bessel function in (91) around its respective ﬁrst positive zero, i.e.,

Jν(x) = β1(x0)(x − x0) + O (x − x0)2 , (95)

Jν+1(x) = β2(y0)(x − y0) + O (x − y0)2 , (96) where

- β1(x0) =

- 1

![image 173](<2005-torquato-new-conjectural-lower-bounds_images/imageFile173.png>)

- 2


[Jν−1(x0) − Jν+1(x0)], (97)

- β2(y0) =


- 1

![image 174](<2005-torquato-new-conjectural-lower-bounds_images/imageFile174.png>)

- 2


[Jν(y0) − Jν+2(y0)], (98)

and x0 and y0 denote the locations of the ﬁrst positive zeros of Jν(z) and Jν+1(z), respectively. Similarly, we employ the linearized form

xJν(x) = x0β1(x0)(x − x0) + O (x − x0)2 . (99)

Use of these relations in (91) yields the following equation for kmin:

d(y0 − σx0)

. (100)

kmin ≃ x0 −

![image 175](<2005-torquato-new-conjectural-lower-bounds_images/imageFile175.png>)

- β1

![image 176](<2005-torquato-new-conjectural-lower-bounds_images/imageFile176.png>)

- β2σν−1x0 − dσ


This formula provides an excellent approximation for kmin. For example, for d = 200 (or ν = 100), substitution of the exact values x0 = 108.8361659, y0 = 109.8640469 and β1/β2 = 1.003189733 as well as the numerical search solution σ∗ = 1.008510 into this formula predicts kmin = 108.4368917. This value is to be compared to the numerical search solution of kmin = 108.4395. This supports the fact that the higher-order terms in the aforementioned linearized forms of the Bessel functions are negligibly small. Indeed, we expect that this can be rigorously proved, but we shall not do so here. We will assume the validity of the linearized forms in the asymptotics displayed below.

For large d = 2ν, we make use of the asymptotic formulas

- x0 = ν + a1ν1/3 +

a2 ν1/3

![image 177](<2005-torquato-new-conjectural-lower-bounds_images/imageFile177.png>)

+

a3 ν

![image 178](<2005-torquato-new-conjectural-lower-bounds_images/imageFile178.png>)

+ O(

1 ν5/3

![image 179](<2005-torquato-new-conjectural-lower-bounds_images/imageFile179.png>)

), (101)

- y0 = ν + a1ν1/3 + 1 +


a2 ν1/3

+

![image 180](<2005-torquato-new-conjectural-lower-bounds_images/imageFile180.png>)

a2 3ν2/3

![image 181](<2005-torquato-new-conjectural-lower-bounds_images/imageFile181.png>)

1 ν4/3

a3 ν

+ O(

+

), (102)

![image 182](<2005-torquato-new-conjectural-lower-bounds_images/imageFile182.png>)

![image 183](<2005-torquato-new-conjectural-lower-bounds_images/imageFile183.png>)

where the constants a1, a2 and a3 are explicitly given in the Appendix. For d = 200, these formulas predict x0 = 108.8362067 and y0 = 109.8640871, which are in excellent agreement with the exact values reported in the preceding paragraph. Using the asymptotic results given in the Appendix, we obtain that

- β1

![image 184](<2005-torquato-new-conjectural-lower-bounds_images/imageFile184.png>)

- β2


- 2

![image 185](<2005-torquato-new-conjectural-lower-bounds_images/imageFile185.png>)

- 3ν −


- 2C2

![image 186](<2005-torquato-new-conjectural-lower-bounds_images/imageFile186.png>)

- 3C1ν5/3


+ O

= 1 +

1 ν2

![image 187](<2005-torquato-new-conjectural-lower-bounds_images/imageFile187.png>)

, (103)

where the constants C1 and C2 are given explicitly in terms of the constants a1 and a2 in the Appendix. For d = 200, for example, this formula together with (A-19) provide the estimate β1/β2 = 1.007122331, which is to be compared to the exact result β1/β2 = 1.006215695.

The optimized asymptotic form for σ∗ is obtained by taking the derivative of both sides of the zero-condition (92) with respect to σ and solving for σ using relation (100) for kmin. We obtain that

q1 ν

q2 ν5/3

1 ν2

σ∗ = 1 +

, (104) where

+

+ O

![image 188](<2005-torquato-new-conjectural-lower-bounds_images/imageFile188.png>)

![image 189](<2005-torquato-new-conjectural-lower-bounds_images/imageFile189.png>)

![image 190](<2005-torquato-new-conjectural-lower-bounds_images/imageFile190.png>)

q1 = 0.90763589355 . . . (105) is the unique positive root of xex + e2x − 5ex + 4 = 0 and

a1(8eq

− 2q1eq

− 10e2q

+ 4 + e3q

+ 4q1e2q

) 3eq1(2q1eq1

1

1

1

1

1

= −1.279349474. (106)

q2 =

![image 191](<2005-torquato-new-conjectural-lower-bounds_images/imageFile191.png>)

− 2q1 + 12 + 3e2q1

− 13eq1)

Therefore, expression (100) for kmin has the asymptotic form

a2 ν1/3

kmin = ν + a1ν1/3 + Q1 +

+ O

![image 192](<2005-torquato-new-conjectural-lower-bounds_images/imageFile192.png>)

1 ν2/3

![image 193](<2005-torquato-new-conjectural-lower-bounds_images/imageFile193.png>)

, (107)

where

2(q1 − 1) eq1

Q1 =

= −0.3860921576. (108)

![image 194](<2005-torquato-new-conjectural-lower-bounds_images/imageFile194.png>)

− 2

These formulas predict σ∗ = 1.008482538 and kmin = 108.4501542, which again are in excellent agreement with values reported above.

Linearizing each Bessel function appearing in (93) about its ﬁrst positive zero and using the results of the Appendix yields

β3(z0)kmin(kmin − z0) 2ν

β1(x0)(kminσ∗ − x0) σ∗ν −

, (109)

∆ν(kmin) ≃

![image 195](<2005-torquato-new-conjectural-lower-bounds_images/imageFile195.png>)

![image 196](<2005-torquato-new-conjectural-lower-bounds_images/imageFile196.png>)

where β1(x0) is given by (97), β3(z0) = [Jν−2(z0)−Jν(z0)]/2, and z0 is the ﬁrst positive zero of Jnu−1. Using relations (104) and (107), and the results of the Appendix yields the asymptotic expansion of ∆ν(kmin):

D1 ν2/3

D2 ν4/3

1 ν5/3

∆ν(kmin) =

(110) where

+

+ O

![image 197](<2005-torquato-new-conjectural-lower-bounds_images/imageFile197.png>)

![image 198](<2005-torquato-new-conjectural-lower-bounds_images/imageFile198.png>)

![image 199](<2005-torquato-new-conjectural-lower-bounds_images/imageFile199.png>)

C1 [a1(2eq

+ 6q1e−q

C1(2 − eq

C2D1 C1

− 7) + 3q2(q1 − 1)] 3(2 − eq1)

) 2eq1

1

1

1

+

. (111) Note also that

, D2 =

D1 =

![image 200](<2005-torquato-new-conjectural-lower-bounds_images/imageFile200.png>)

![image 201](<2005-torquato-new-conjectural-lower-bounds_images/imageFile201.png>)

![image 202](<2005-torquato-new-conjectural-lower-bounds_images/imageFile202.png>)

ν

E1 ν1/3

E2 ν2/3

1 ν

kmin ν

1ν1/3+Q1 1 +

= ea

+

+ O

![image 203](<2005-torquato-new-conjectural-lower-bounds_images/imageFile203.png>)

![image 204](<2005-torquato-new-conjectural-lower-bounds_images/imageFile204.png>)

![image 205](<2005-torquato-new-conjectural-lower-bounds_images/imageFile205.png>)

![image 206](<2005-torquato-new-conjectural-lower-bounds_images/imageFile206.png>)

(112) and

2q22 ν4/3

q12 ν

2q2 ν2/3 −

1 ν5/3

σ∗2ν = e2q

1 +

, (113) where

+

+ O

1

![image 207](<2005-torquato-new-conjectural-lower-bounds_images/imageFile207.png>)

![image 208](<2005-torquato-new-conjectural-lower-bounds_images/imageFile208.png>)

![image 209](<2005-torquato-new-conjectural-lower-bounds_images/imageFile209.png>)

![image 210](<2005-torquato-new-conjectural-lower-bounds_images/imageFile210.png>)

a21 2

a41 − 4a21a2 + 4a22 8

E1 = a2 −

, (114) and Q1 is given by (108). For d = 200, these formulas [together with the constants speciﬁed by (105), (106), (111), 114), (A-5) and (A-19)] predict ∆ν(kmin) = 0.00567441932, (kmin/ν)ν = 3353.018128 and σ∗2ν = 5.405924156. These values should be compared to the exact value of ∆ν(kmin) = 0.00559813885, (kmin/ν)ν = 3301.799093 and σ∗2ν = 5.445550297.

, E2 = −Q1a1 +

![image 211](<2005-torquato-new-conjectural-lower-bounds_images/imageFile211.png>)

![image 212](<2005-torquato-new-conjectural-lower-bounds_images/imageFile212.png>)

Thus, substituting the asymptotic relations above into the optimal expression (94) for the density and invoking Conjecture 5.1 yields the conjectural lower bound

φmax ≥ φ∗ =

+

![image 213](<2005-torquato-new-conjectural-lower-bounds_images/imageFile213.png>)

1 2[3−log2(e)]ν−log2(e)a1ν1/3+(2q1−Q1) log2(e)

2 π

E1 ν1/6

- 1

![image 214](<2005-torquato-new-conjectural-lower-bounds_images/imageFile214.png>)

- 2D1


ν1/6 +

![image 215](<2005-torquato-new-conjectural-lower-bounds_images/imageFile215.png>)

![image 216](<2005-torquato-new-conjectural-lower-bounds_images/imageFile216.png>)

![image 217](<2005-torquato-new-conjectural-lower-bounds_images/imageFile217.png>)

1 ν5/6

E2 − 2q2 − D2/D1 ν1/2

+ O

, (115)

![image 218](<2005-torquato-new-conjectural-lower-bounds_images/imageFile218.png>)

![image 219](<2005-torquato-new-conjectural-lower-bounds_images/imageFile219.png>)

where we have used the asymptotic relation Γ(1 + ν) ∼ νν√2πνe−ν. For d = 200, this asymptotic formula [together with the constants speciﬁed by (105), (106), (111), 114), (A-5) and (A-19)] predicts φ∗ = 5.626727001×10−44, which is in good agreement with the numerical search solution of φ∗ = 5.667098×10−44. Note also that the formula (94) with kmin estimated from (100) yields φ∗ = 5.666392126 × 10−44, which is remarkably close to the numerical solution. For large d, result (115) yields the following dominant asymptotic formula for the conjectural lower bound on φmax:

![image 220](<2005-torquato-new-conjectural-lower-bounds_images/imageFile220.png>)

d1/6 22/3D1√π 2[3−log2(e)]d/2 =

3.276100896 d1/6 20.7786524795...d

φmax ≥ φ∗ ∼

. (116)

![image 221](<2005-torquato-new-conjectural-lower-bounds_images/imageFile221.png>)

![image 222](<2005-torquato-new-conjectural-lower-bounds_images/imageFile222.png>)

![image 223](<2005-torquato-new-conjectural-lower-bounds_images/imageFile223.png>)

This putatively provides the long-sought exponential improvement on Minkowski’s lower bound. Note that the constant D1 = 0.1084878572 appearing in (116) is determined from the appropriate relation in (111) using the value for q1 given by (105) and the more reﬁned estimate of C1 given by (A-21).

Substitution of the asymptotic expression (116) into (84) and use of (63) yields a conjectural lower bound on the maximal kissing number

21/3e2q

d1/6 D1√π

1

Zmax ≥ Z∗ ∼

![image 224](<2005-torquato-new-conjectural-lower-bounds_images/imageFile224.png>)

![image 225](<2005-torquato-new-conjectural-lower-bounds_images/imageFile225.png>)

2[log

2(e)−1]d/2 = 40.24850787 d1/6 20.2213475205... d, (117)

which applies for large d. This result is superior to the best known asymptotic lower bound on the maximal kissing number of 20.2075...d [Wyn65]. Note that such a disordered packing would be substantially hyperstatic (the average kissing number is greater than 2d [DST05]) and therefore would be appreciably diﬀerent from a maximally random jammed packing [TTD00, Tor02], which is isostatic (see Section 4.3) and hence signﬁcantly smaller in density.

# 6 Discussion

Our results have immediate implications for the linear programming bounds of Cohn and Elkies [CE03], regardless of the validity of Conjecture 5.1. As we noted earlier, our optimization procedure is precisely the dual of the their primal linear programming upper bound. The existence of our test functions (75) and (81) that satisfy the conditions (i), (ii) and (iii) of Section 5 for densities up to the terminal density φ∗ narrows the duality gap [cf. (79) and (115)]. In particular, inequality (115) provides the greatest lower bound known for the dual linear program. Moreover, the existence of the inequalities (80) and (115) proves that linear programming bounds cannot possibly match the Minkowski lower bound for any dimension d.

Finally, this link to the Cohn-Elkies formulation proves that the terminal density φ∗ can never exceed the Cohn-Elkies upper bound, which obviously must be true if the terminal density corresponds to a rigorous lower bound.

Conjecture 5.1 concerning the existence of disordered sphere packings is plausible for a number of reasons: (i) the decorrelation principle of Section 4.3; (ii) the necessary Yamada condition appears to only have relevance in very low dimensions; (iii) other new necessary conditions described in Section 5.4 also seem to be germane only in very low dimensions; (iv) there are numerical constructions of conﬁgurations of disordered sphere packings on the torus corresponding to these test radial distributions functions in low dimensions for densities up to the terminal density [CTS03, OST06]; and (v) the test radial distributions functions (66) and (75) recover the asymptotic forms of known rigorous bounds. Concerning the latter point, if Conjecture 5.1 is false, it is certainly not revealed by the results produced by the test functions (66) and (75) because the forms of known rigorous results, obtained using completely diﬀerent techniques, are recovered. If Conjecture 5.1 is false, why would it suddenly be revealed by the introduction of a gap in the test radial distribution function [cf. (81)] relative to (75)? This would seem to be unlikely and lends credibility to the conjecture in our view.

Conjecture 5.1, the particular choice (81) and our optimization procedure leads to a lower bound on the maximal density that improves on the Minkowski bound by an exponential factor. Our results suggest that the densest packings in suﬃciently high dimensions may be disordered rather than periodic, implying the existence of disordered classical ground states for some continuous potentials. A byproduct of our procedure is an associated lower bound on the maximal kissing number, which is superior to the currently best known result. By no means is the choice (81) optimal. For example, one may be able to improve our putative lower bound by allowing the test function to be some positive function smaller than unity for 1 ≤ r ≤ σ. Of course, it would be desirable to choose test functions that make asymptotic analysis exactly rather than numerically tractable.

Our putative exponential improvement over Minkowksi’s bound is striking and should provide some impetus to determine the validity of Conjecture 5.1. As a ﬁrst step in this direction, it would be fruitful if one could show that for suﬃciently small densities, the two standard nonnegativity conditions on the pair correlation function g2 are suﬃcient to assure the existence of a point process, whether it is a sphere packing or not. Another problem worth pursuing is the demonstration of the existence of a pair interaction potential in Rd corresponding to a sphere packing for a given ρ and g2 provided that ρ and g2 are suﬃciently small. Such a proof may be possible following the methods that Koralov [Kor05] used for the

lattice setting. It would also be proﬁtable to pursue the construction of disordered sphere packings with densities that exceed 1/2d for suﬃciently large d.

Acknowledgments

This work supported in part by the National Science Foundation under Grant No. DMS0312067. We thank Peter Sarnak and Enrico Bombieri for encouraging us to apply our methods to try to obtain exponential improvement on Minkowski’s lower bound. We beneﬁted greatly from discussions with Henry Cohn, John Conway, Leonid Koralov and Thomas Spencer.

# APPENDIX

An asymptotic expression for Jν(x) when ν is large and x > ν is given by [Wat58]

3x2 + 2ν2 12(x2 − ν2)

, (A-1)

Jν(x) = Aν(x) cos[ων(x) − π/4] + O

![image 226](<2005-torquato-new-conjectural-lower-bounds_images/imageFile226.png>)

where

1/2

2 π√x2 − ν2

Aν(x) =

(A-2) and

![image 227](<2005-torquato-new-conjectural-lower-bounds_images/imageFile227.png>)

![image 228](<2005-torquato-new-conjectural-lower-bounds_images/imageFile228.png>)

√

![image 229](<2005-torquato-new-conjectural-lower-bounds_images/imageFile229.png>)

x2 − ν2 − ν cos−1(ν/x). (A-3)

ων(x) =

The function Aν(x) cos[ων(x) − π/4] in (A-1) actually represents the dominant term in the asymptotic expansion (4) on page 244 of Watson [Wat58] for Jν(x) when ν is large and x > ν and Aν(x) multiplied by the big-O term represents the largest absolute error when this dominant term is used to estimate Jν(x). A problem of central concern is an estimate of Jν(x) in the vicinity of its ﬁrst positive zero x0 when ν is large. The ﬁrst positive zero has the asymptotic expansion [Olv60]

a2 ν1/3

a3 ν

x0 = ν + a1ν1/3 +

+

![image 230](<2005-torquato-new-conjectural-lower-bounds_images/imageFile230.png>)

![image 231](<2005-torquato-new-conjectural-lower-bounds_images/imageFile231.png>)

1 ν5/3

+ O(

), (A-4)

![image 232](<2005-torquato-new-conjectural-lower-bounds_images/imageFile232.png>)

where

a1 = 1.8557571 . . ., a2 = 1.033150 . . ., a3 = −0.003971 . . .. (A-5)

Expanding Jν(x) in a Taylor series about x = x0 and neglecting quadratic and higher-order terms gives the linear estimate

Jν(x) ≃

- 1

![image 233](<2005-torquato-new-conjectural-lower-bounds_images/imageFile233.png>)

- 2


[Jν−1(x0) − Jν+1(x0)](x − x0), (A-6)

where we take the Bessel functions on the right side to be given by the asymptotic forms

3x2 + 2ν2 12(x2 − ν2)

(A-7)

Jν+1(x0) = Aν+1(x0) cos[ων+1(x0) − π/4] + O

![image 234](<2005-torquato-new-conjectural-lower-bounds_images/imageFile234.png>)

and

3x2 + 2ν2 12(x2 − ν2)

. (A-8) We will also need to consider the related functions

Jν−1(x0) = Aν−1(x0) cos[ων−1(x0) − π/4] + O

![image 235](<2005-torquato-new-conjectural-lower-bounds_images/imageFile235.png>)

Jν+1(x) ≃

- 1

![image 236](<2005-torquato-new-conjectural-lower-bounds_images/imageFile236.png>)

- 2


[Jν(y0) − Jν+2(y0)](x − y0), (A-9)

- 1

![image 237](<2005-torquato-new-conjectural-lower-bounds_images/imageFile237.png>)

- 2


[Jν−2(z0) − Jν(z0)](x − z0), (A-10)

Jν−1(x) ≃

where y0 and z0 are the ﬁrst positive zeros of Jν+1(x) and Jν−1(x), respectively, which are asymptotically given by

- y0 = ν + a1ν1/3 + 1 +

a2 ν1/3

![image 238](<2005-torquato-new-conjectural-lower-bounds_images/imageFile238.png>)

+

a2 3ν2/3

![image 239](<2005-torquato-new-conjectural-lower-bounds_images/imageFile239.png>)

+

a3 ν

![image 240](<2005-torquato-new-conjectural-lower-bounds_images/imageFile240.png>)

+ O(

1 ν4/3

![image 241](<2005-torquato-new-conjectural-lower-bounds_images/imageFile241.png>)

), (A-11)

- z0 = ν + a1ν1/3 − 1 +


a2 3ν2/3

a2 ν1/3 −

![image 242](<2005-torquato-new-conjectural-lower-bounds_images/imageFile242.png>)

![image 243](<2005-torquato-new-conjectural-lower-bounds_images/imageFile243.png>)

1 ν4/3

a3 ν

+ O(

+

). (A-12)

![image 244](<2005-torquato-new-conjectural-lower-bounds_images/imageFile244.png>)

![image 245](<2005-torquato-new-conjectural-lower-bounds_images/imageFile245.png>)

Note that the asymptotic expressions for the zeros given here for ν = 100 (d = 200) predict x0 = 108.8362071, y0 = 109.8641774 and z0 = 107.8082369, which are in excellent agreement with exact results x0 = 108.8361659, y0 = 109.8640469 and z0 = 107.8081033 as obtained from Maple.

Using Maple and the results above, we obtain the following asymptotic expansions:

- 1

![image 246](<2005-torquato-new-conjectural-lower-bounds_images/imageFile246.png>)

- 2


[Jν−1(x0) − Jν+1(x0)] =

- 1

![image 247](<2005-torquato-new-conjectural-lower-bounds_images/imageFile247.png>)

- 2


[Jν(y0) − Jν+2(y0)] =

- 1

![image 248](<2005-torquato-new-conjectural-lower-bounds_images/imageFile248.png>)

- 2


[Jν−2(z0) − Jν(z0)] =

C1 ν2/3

![image 249](<2005-torquato-new-conjectural-lower-bounds_images/imageFile249.png>)

C1 ν2/3

![image 250](<2005-torquato-new-conjectural-lower-bounds_images/imageFile250.png>)

C1 ν2/3

![image 251](<2005-torquato-new-conjectural-lower-bounds_images/imageFile251.png>)

C2 ν4/3

1 ν2

+

+ O

![image 252](<2005-torquato-new-conjectural-lower-bounds_images/imageFile252.png>)

![image 253](<2005-torquato-new-conjectural-lower-bounds_images/imageFile253.png>)

C2 ν4/3 −

2C1 3ν5/3

+

![image 254](<2005-torquato-new-conjectural-lower-bounds_images/imageFile254.png>)

![image 255](<2005-torquato-new-conjectural-lower-bounds_images/imageFile255.png>)

C2 ν4/3

2C1 3ν5/3

+

+

![image 256](<2005-torquato-new-conjectural-lower-bounds_images/imageFile256.png>)

![image 257](<2005-torquato-new-conjectural-lower-bounds_images/imageFile257.png>)

, (A-13)

+ O

+ O

1 ν2

![image 258](<2005-torquato-new-conjectural-lower-bounds_images/imageFile258.png>)

1 ν2

![image 259](<2005-torquato-new-conjectural-lower-bounds_images/imageFile259.png>)

, (A-14)

. (A-15)

where

21/4 √2f1(a1) + 8a13/2f2(a1) 8√πa15/4

![image 260](<2005-torquato-new-conjectural-lower-bounds_images/imageFile260.png>)

C1 = −

, (A-16)

![image 261](<2005-torquato-new-conjectural-lower-bounds_images/imageFile261.png>)

![image 262](<2005-torquato-new-conjectural-lower-bounds_images/imageFile262.png>)

23/4 [1152a61 − 3840a41a2 − 180a31 + 600a1a2 − 225]f1(a1) + 21/4 3072a91/2 − 200a31/2 f2(a1) 3840√πa113/4

,

C2 =

![image 263](<2005-torquato-new-conjectural-lower-bounds_images/imageFile263.png>)

![image 264](<2005-torquato-new-conjectural-lower-bounds_images/imageFile264.png>)

(A-17) f1(a1) = sin

(2a1)3/2 3

(2a1)3/2 3

(2a1)3/2 3 − cos

(2a1)3/2 3

+ cos

, f2(a1) = sin

. (A-18)

![image 265](<2005-torquato-new-conjectural-lower-bounds_images/imageFile265.png>)

![image 266](<2005-torquato-new-conjectural-lower-bounds_images/imageFile266.png>)

![image 267](<2005-torquato-new-conjectural-lower-bounds_images/imageFile267.png>)

![image 268](<2005-torquato-new-conjectural-lower-bounds_images/imageFile268.png>)

Thus, substitution of the values for the constants a1 and a2 into the expressions above yields the estimates

C1 = −1.104938082, C2 = 1.627074727. (A-19) For d = 200 (ν = 100), for example, the asymptotic expansions (A-13) - (A-15) predict −0.04778125640, −0.04743934518 and −0.04812316762, respectively. This is to compared to the corresponding exact results: −0.04829366129, −0.04799533693 and −0.04859672879. Note that although the estimates of the constants C1 and C2 given by (A-19) involve a small error due to our use of only the dominant asymptotic term (A-1), the functional forms of the asymptotic expansions (A-13) - (A-15) are exact.

We can show that the exact expressions for the constants C1 and C2 appearing in (A-13) - (A-15) are rapidly converging asymptotic expansions in inverse powers of the constant a1 appearing in (A-4). For example, using expansion (4) on page 244 of Watson, we ﬁnd that the ﬁrst three terms of the expansion of C1 is given by

C11 a15/4

C1 =

![image 269](<2005-torquato-new-conjectural-lower-bounds_images/imageFile269.png>)

C12 a111/4

+

+

![image 270](<2005-torquato-new-conjectural-lower-bounds_images/imageFile270.png>)

C13 a117/4

+ O

![image 271](<2005-torquato-new-conjectural-lower-bounds_images/imageFile271.png>)

1 a123/4

![image 272](<2005-torquato-new-conjectural-lower-bounds_images/imageFile272.png>)

, (A-20)

where

21/4 √2f1(a1) + 8a13/2f2(a1) 8√π

5 · 21/4 4√2f1(a1) − 7a31/2f2(a1) 384√π

![image 273](<2005-torquato-new-conjectural-lower-bounds_images/imageFile273.png>)

![image 274](<2005-torquato-new-conjectural-lower-bounds_images/imageFile274.png>)

,

C11 = −

, C12 =

![image 275](<2005-torquato-new-conjectural-lower-bounds_images/imageFile275.png>)

![image 276](<2005-torquato-new-conjectural-lower-bounds_images/imageFile276.png>)

![image 277](<2005-torquato-new-conjectural-lower-bounds_images/imageFile277.png>)

![image 278](<2005-torquato-new-conjectural-lower-bounds_images/imageFile278.png>)

385 · 21/4 13√2f1(a1) + 8a31/2f2(a1) 221184√π

![image 279](<2005-torquato-new-conjectural-lower-bounds_images/imageFile279.png>)

C13 = −

.

![image 280](<2005-torquato-new-conjectural-lower-bounds_images/imageFile280.png>)

![image 281](<2005-torquato-new-conjectural-lower-bounds_images/imageFile281.png>)

The ﬁrst term of the expansion (A-20) is the dominant one and is identical to the estimate given in (A-16). The ﬁrst term of (A-20) is about 66 times larger than the second term in absolute value and the second term is about 7 times larger than the third term in absolute value. Substitution of the constant a1 into (A-20) yields the more reﬁned estimate

C1 = −1.123958144. (A-21)

This reﬁned estimate diﬀers from the dominant ﬁrst-term estimate given in (A-19) in the third signiﬁcant ﬁgure. One could continue correcting this estimate by including additional terms in the asymptotic expansion but this quickly becomes tedious and is not necessary because, as we show at the end of Section 5, the precise value of C1 is not relevant for the putative exponential improvement of Minkowski’s lower bound on the density, as speciﬁed by (116).

# References

[AS91] R. Ambartzumian and H. Sukiasian. Inclusion-exclusion and point processes. Acta Applicandae Mathematicae, 22:15–31, 1991.

[Bal92] K. Ball. A lower bound for the optimal density of lattice packings. Duke J. Math.,

68:217–221, 1992. [Bec87] J. Beck. Irregularties of distribution I. Acta Mathemtica, 159:1–49, 1987. [Bli29] H. Blichfeldt. The minimum value of quadratic forms and the closest packing of

spheres. Math. Ann., 101:605–608, 1929. [Boc36] S. Bochner. Lectures on Fourier Analysis. Edwards, Ann Arbor, Michigan, 1936. [Bo¨r64] K. B¨oro¨czky. Uber stabile Kreis- und Kugelsysteme. Ann. Univ. Sci. Budapest

Estvss. Sect. Math., 7(79), 1964. [CBB98] R. Connelly, K. Bezdek, and A. Bezdek. Finite and uniform stability of sphere packings. Discrete and Computational Geometry, 20:111–130, 1998. [CE03] H. Cohn and N. Elkies. New upper bounds on sphere packings I. Annals of Mathematics, 157:689–714, 2003. [CK04] H. Cohn and A. Kumar. Optimality and uniqueness of the Leech lattice among lattices. 2004. arXiv:math.MG/0403263. [CL95] P. M. Chaikin and T. C. Lubensky. Principles of Condensed Matter Physics. Cambridge University Press, New York, 1995. [CL04] O. Costin and J. Lebowitz. On the construction of particle distributions with speciﬁed single and pair densities. J. Phys. Chem. B., 108:19614–19618, 2004.

[Coh02] H. Cohn. New upper bounds on sphere packings II. Geom. Topol., 6:329–353, 2002. [CS98] J. H. Conway and N. J. A. Sloane. Sphere Packings, Lattices and Groups. Springer-

Verlag, New York, 1998. [CTS03] J. R. Crawford, S. Torquato, and F. H. Stillinger. Aspects of correlation function realizability. J. Chem. Phys., 119, 2003.

[DR47] H. Davenport and C. Rogers. Hlawka’s theorem in the geometry of numbers. Duke J. math., 14:367–375, 1947.

[DST05] A. Donev, , F. H. Stillinger, and S. Torquato. Pair correlation function characteristics of nearly jammed disordered and ordered hard-sphere packings. Phys. Rev. E, 71:011105: 1–14, 2005.

[DTSC04] A. Donev, S. Torquato, F. H. Stillinger, and R. Connelly. Jamming in hard sphere and disk packings. J. Appl. Phys., 95:989–999, 2004.

[FP99] H. L. Frisch and J. K. Percus. High dimensionality as an organizing device for classical ﬂuids. Phys. Rev. E, 60:2942–2948, 1999.

[GV64] I. M. Gel’fand and N. Ya. Vilenkin. Generalized Functions. Academic Press, New

York, 1964. [Hal98] T. C. Hales. The Kepler conjecture. arXiv:math.MG/9811078, 1998. [Ken48] D. G. Kendall. On the number of lattice points inside a random oval. Quart. J.

Math. (Oxford), 19:1–24, 1948. [KL78] G. A. Kabatiansky and V. I. Levenshtein. Bounds for packings on a sphere and in space. Problems of Information Transmission, 14:1–17, 1978. [Kor05] L. Koralov. The existence of pair potential corresponding to speciﬁed density and pair correlation. Lett. Math. Phys., 71:135–148, 2005. [KR53] D. G. Kendall and R. A. Rankin. On the number of points of a given lattice in a random hypersphere. Quart. J. Math. Oxford, 4:178–189, 1953. [Len73] A. Lennard. Correlation functions and the uniqueness of the state in classical statistical mechanics. Commun. Math. Phys., 30:35–44, 1973.

- [Len75a] A. Lennard. States of classical statistical mechanical systems of inﬁnitely many particles I. Arch. Rational Mech. Anal., 59:219–239, 1975.
- [Len75b] A. Lennard. States of classical statistical mechanical systems of inﬁnitely many particles II. Arch. Rational Mech. Anal., 59:241–256, 1975.


[Lo`e63] M. Lo`eve. Probability Theory. Van Nostrand, Princeton, New Jersey, 3rd edition, 1963.

[Mat86] B. Mat´ern. Spatial variation. In Lecture Notes in Statistics, volume 36. SpringerVerlag, New York, second edition, 1986.

[Min05] H. Minkowski. Diskontinuit¨atsbereich f¨ur arithmetische Aquivalenz.¨ J. reine

angew. Math., 129:220–274, 1905. [Neb98] G. Nebe. Some cyclo-quaternionic lattices. J. Algebra, 199:472–498, 1998. [Olv60] F. W. Olver. Bessel Functions III: Zeros and Associated Values, Royal Soc. Math.

Tables, volume 7. Cambridge University Press, Cambridge, 1960. [OST06] O. U. Ouche, F. H. Stillinger, and S. Torquato. On the realizability of pair correlation functions. Physica A, 360:21–36, 2006. [Re´n63] A. Re´nyi. On a one-dimensional problem concerning random space ﬁlling. Sel. Trans. Math. Stat. Prob., 4:203–218, 1963. [Rog58] C. A. Rogers. The packing of equal spheres. Proc. Lond. Math. Soc., 8:609–620, 1958. [Rog64] C. A. Rogers. Packing and Covering. Cambridge University Press, Cambridge, 1964. [Rue99] D. Ruelle. Statistical Mechanics: Rigorous Results. World Scientiﬁc, Riveredge, New Jersey, 1999. [Sal58] E. E. Salpeter. On Mayer’s theory of cluster expansions. Ann. Physics, 5:183–223, 1958. [SKM95] D. Stoyan, W. S. Kendall, and J. Mecke. Stochastic Geometry and Its Applications. Wiley, New York, second edition, 1995. [Sos00] A. Soshnikov. Determinantal random point ﬁelds. Russian Mathematical Surveys, 55:923–975, 2000. [SS05] P. Sarnak and A. Strombergsson. Minima of Epstein’s zeta function and heights of ﬂat tori. 2005. preprint. [ST04] F. H. Stillinger and S. Torquato. Pair correlation function realizability: Lattice model implications. J. Phys. Chem. B, 108:19589–19594, 2004.

[TDS03] S. Torquato, A. Donev, and F. H. Stillinger. Breakdown of elasticity theory for jammed hard-particle packings: Conical nonlinear constitutive theory. Int. J. Solids Structures, 40:7143–7153, 2003.

[Tor02] S. Torquato. Random Heterogeneous Materials: Microstructure and Macroscopic Properties. Springer-Verlag, New York, 2002.

- [TS01] S. Torquato and F. H. Stillinger. Multiplicity of generation, selection, and classiﬁcation procedures for jammed hard-particle packings. J. Phys. Chem. B, 105:11849– 11853, 2001.
- [TS02] S. Torquato and F. H. Stillinger. Controlling the short-range order and packing densities of many-particle systems. J. Phys. Chem. B, 106:8354–8359, 2002. Erratum 106, 11406 (2002).
- [TS03] S. Torquato and F. H. Stillinger. Local density ﬂuctuations, hyperuniform systems, and order metrics. Phys. Rev. E, 68:041113: 1–25, 2003.


[TS06] S. Torquato and F. H. Stillinger. Exactly solvable disordered sphere-packing model in arbitrary-dimensional Euclidean spaces. Phys. Rev. E, 2006. in press.

[TTD00] S. Torquato, T. M. Truskett, and P. G. Debenedetti. Is random close packing of spheres well deﬁned? Phys. Rev. Lett., 84:2064–2067, 2000.

[Wat58] G. N. Watson. Theory of Bessel Functions. Cambridge University Press, Cambridge, England, second edition, 1958.

[WRF87] D. Wyler, N. Rivier, and H. L. Frisch. Hard-sphere ﬂuid in inﬁnite dimensions. Phys. Rev. A, 36:2422–2431, 1987.

[Wyn65] A. D. Wyner. Capabilities of bounded discrepancy decoding. Bell System Tech. J., 44:1061–1122, 1965.

[Yag87] A. M. Yaglom. Correlation Theory of Stationary and Related Functions I Basic Results. Springer-Verlag, New York, 1987.

[Yam61] M. Yamada. Geometrical study of the pair distribution function in the many-body problem. Prog. Theor. Phys., 25:579–594, 1961.

