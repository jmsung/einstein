# arXiv:1902.05438v3[math.MG]10Jun2022

## Universal optimality of the E8 and Leech lattices and interpolation formulas

By Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko, and Maryna Viazovska

### Abstract

We prove that the E8 root lattice and the Leech lattice are universally optimal among point conﬁgurations in Euclidean spaces of dimensions 8 and 24, respectively. In other words, they minimize energy for every potential function that is a completely monotonic function of squared distance (for example, inverse power laws or Gaussians), which is a strong form of robustness not previously known for any conﬁguration in more than one dimension. This theorem implies their recently shown optimality as sphere packings, and broadly generalizes it to allow for long-range interactions.

The proof uses sharp linear programming bounds for energy. To construct the optimal auxiliary functions used to attain these bounds, we prove a new interpolation theorem, which is of independent interest. It reconstructs a radial Schwartz function f from the values and radial derivatives of f and its Fourier transform f at the radii √2n for integers n ≥ 1 in R8 and n ≥ 2 in R24. To prove this theorem, we construct an interpolation basis using integral transforms of quasimodular forms, generalizing Viazovska’s work on sphere packing and placing it in the context of a more conceptual theory.

### Contents

- 1. Introduction 2
- 2. Preliminaries and background on modular forms 19
- 3. Functional equations and the group algebra C[PSL2(Z)] 28
- 4. Solutions of functional equations and modular form kernels 43
- 5. Proof of the interpolation formula 63


Miller’s research was supported by National Science Foundation grants CNS-1526333 and CNS-1815562, and Viazovska’s research was supported by Swiss National Science Foundation project 184927. The authors thank the Rutgers Oﬃce of Advanced Research Computing for their computational support and resources.

© 2022 by the authors. This paper may be reproduced, in its entirely, for noncommercial purposes.

1

- 6. Positivity of kernels and universal optimality 81
- 7. Generalizations and open questions 93 Acknowledgements 96 References 97


### 1. Introduction

What is the best way to arrange a discrete set of points in Rd? Of course the answer depends on the objective: there are many diﬀerent ways to measure the quality of a conﬁguration for interpolation, quadrature, discretization, error correction, or other problems. A conﬁguration that is optimal for one purpose will often be good for others, but usually not optimal for them as well. Those that optimize many diﬀerent objectives simultaneously play a special role in mathematics. In this paper, we prove a broad optimality theorem for the E8 and Leech lattices, via a new interpolation formula for radial Schwartz functions. Our results help characterize the exceptional nature of these lattices. (See [22] and [18] for their deﬁnitions and basic properties.)

1.1. Potential energy minimization. One particularly fruitful family of objectives to optimize is energy under diﬀerent potential functions. Given a potential function p: (0,∞) → R, we deﬁne the potential energy of a ﬁnite subset C of Rd to be

p |x − y| ,

x,y∈C x =y

where | · | is the Euclidean norm (note that we include each pair of points twice, which diﬀers from the convention in physics). Our primary interest is in inﬁnite sets C, for which potential energy requires renormalization because the double sum often diverges. Deﬁne a point conﬁguration, or just conﬁguration, C to be a nonempty, discrete, closed subset of Rd (i.e., every ball in Rd contains only ﬁnitely many points of C). We say C has density ρ if

C ∩ Brd(0) vol Brd(0)

= ρ,

lim

r→∞

where Brd(0) denotes the closed ball of radius r about 0 in Rd. For such a set, we can renormalize the energy by considering the average energy per particle, as follows.

Deﬁnition 1.1. Let p: (0,∞) → R be any function. The lower p-energy of a point conﬁguration C in Rd is

1 C ∩ Brd(0)

p |x − y| .

Ep(C) := liminf

r→∞

x,y∈C∩Brd(0) x =y

If the limit of the above quantity exists, and not just its limit inferior, then we call Ep(C) the p-energy of C (and say that its p-energy exists). We allow the possibility that the energy may be ±∞.

The simplest case is when the conﬁguration is a lattice Λ, i.e., the Z-span of a basis of Rd. In that case, it has density

1

vol Rd/Λ and p-energy

p |x| ,

x∈Λ\{0}

assuming this sum is absolutely convergent. More generally, a periodic conﬁguration is the union of ﬁnitely many orbits under the translation action of some lattice, i.e., the union of pairwise disjoint translates Λ + vj of a lattice Λ, with 1 ≤ j ≤ N. Such a conﬁguration has density

N vol Rd/Λ and p-energy

- (1.1)


N

1 N

p |x + vj − vk| ,

j,k=1 x∈Λ\{vk−vj}

again assuming absolute convergence. Many important conﬁgurations are periodic, but others are not, and we do not assume periodicity in our main theorems.

Typically we take the potential function p to be decreasing, and we envision the points of C as particles subject to a repulsive force. Our framework is purely classical and does not incorporate quantum eﬀects; thus, we should not think of the particles as atoms. However, classical models have other applications [5], such as describing mesoscale materials. Our goal is then to arrange these particles so as to minimize their p-energy, subject to maintaining

a ﬁxed density.1 More precisely, we compare with the lower p-energies of other conﬁgurations:

Deﬁnition 1.2. Let C be a point conﬁguration in Rd with density ρ, where ρ > 0, and let p: (0,∞) → R be any function. We say that C minimizes energy for p if its p-energy Ep(C) exists and every conﬁguration in Rd of density ρ has lower p-energy at least Ep(C). We also call C a ground state for p.

In certain contrived cases it is easy to determine the minimal energy. For example, if p vanishes at the square roots of positive integers and is nonnegative elsewhere, then Zd clearly minimizes p-energy. However, rigorously determining ground states seems hopelessly diﬃcult in general, because of the complexity of analyzing long-range interactions. This issue arises in physics and materials science as the crystallization problem [3, 47]: how can we understand why particles so often arrange themselves periodically at low temperatures? Even the simplest mathematical models of crystallization are enormously subtle, and surprisingly little has been proved about them.

Two important classes of potential functions are inverse power laws r  → 1/rs with s > 0 and Gaussians r  → e−αr2 with α > 0. Inverse power laws are special because they are homogeneous, which implies that their ground states are scale-free: if C is a ground state in Rd with density 1, then ρ−1/dC is a ground state with density ρ. Gaussians lack this property, and the shape of their ground states may depend on density (see, for example, [16]). In applications, Gaussian potential functions are typically used to approximate eﬀective potential functions for more complex materials. For example, for a dilute solution of polymer chains in an athermal solvent, Gaussians describe the eﬀective interaction between the centers of mass of the polymers (see Sections 3.4 and 3.5 of [33]). Point particles with Gaussian interactions are known as the Gaussian core model in physics [50].

Both inverse power laws and Gaussians arise naturally in number theory (see, for example, [36] and [44]). Given a lattice Λ in Rd, its Epstein zeta

1Fixing the density prevents the particles from minimizing energy by receding to inﬁnity. If ﬁxing the density seems unphysical, we could instead impose a chemical potential that penalizes decreasing the density of the conﬁguration, to account for exchange with the external environment. That turns out to be equivalent, in the sense that one can achieve any desired density by choosing an appropriate chemical potential. Speciﬁcally, the chemical potential is a Lagrange multiplier that converts the density-constrained optimization problem to an unconstrained problem. This approach is called the grand canonical ensemble, and it is typically set up for ﬁnite systems before taking a thermodynamic limit. See, for example, Section 1.2.1(c) and Theorem 3.4.6 in [41].

function is deﬁned by

1 |x|2s

ζΛ(s) =

x∈Λ\{0}

for Re(s) > d/2 (and by analytic continuation for all s except for a pole at s = d/2), and its theta series is deﬁned by

eπiz|x|2

ΘΛ(z) =

x∈Λ

for Im(z) > 0. Then the energy of Λ under r  → 1/rs is ζΛ(s/2) when s > d, while its energy under r  → e−αr2 is ΘΛ(iα/π) − 1. In other words, minimizing energy among lattices amounts to seeking extreme values for number-theoretic special functions. The restriction to lattices makes this problem much more tractable than the crystallization problem, but it remains diﬃcult. The answer is known in certain special cases, such as suﬃciently large s when d ≤ 8 (see [42]), but the only cases in which the answer was previously known for all s and α were one or two dimensions [36].

Energy minimization also generalizes the sphere packing problem in Rd, in which we wish to maximize the minimal distance between neighboring particles while ﬁxing the particle density. (Centering non-overlapping spheres at the particles then yields a densest sphere packing.) One simple way to see why is to pick a constant r0 and use the potential function

p(r) =

- 0 if r ≥ r0, and
- 1 if 0 < r < r0.


Then the p-energy of a periodic conﬁguration vanishes if and only if the conﬁguration has minimal distance at least r0. More generally, we can use a steep potential function such as r  → 1/rs with s large (or, similarly, r  → e−αr2 with α large). As s → ∞, the contribution to energy from short distances becomes increasingly important, and in the limit minimizing energy requires maximizing the minimal distance. In many cases, the ground state will be slightly distorted at any ﬁnite s, compared with the limit as s → ∞. For example, that seems to happen in ﬁve or seven dimensions [16]. However, the E6 root lattice in R6 appears to minimize energy for all suﬃciently large s, provably among lattices [42] and perhaps among all conﬁgurations [16].

1.2. Universal optimality. In contrast to the sphere packing problem, even one-dimensional energy minimization is not easy to analyze. Ventevogel and Nijboer [52] proved that the integer lattice Z in R minimizes energy for every completely monotonic function of squared distance, i.e., every function of the form r  → g r2 with g completely monotonic. Recall that a function g: (0,∞) → R is completely monotonic if it is inﬁnitely diﬀerentiable and satisﬁes the inequalities (−1)kg(k) ≥ 0 for all k ≥ 0. In other words, g is

nonnegative, weakly decreasing, convex, and so on. For example, inverse power laws are completely monotonic, as are decreasing exponential functions. By Bernstein’s theorem [48, Theorem 9.16], every completely monotonic function g: (0,∞) → R can be written as a convergent integral

g(r) = e−αr dµ(α)

for some measure µ on [0,∞). Equivalently, the completely monotonic functions of squared distance are the cone spanned by the Gaussians and the constant function 1. For example, inverse power laws can be obtained via

1 rs

=

∞

αs/2−1 Γ(s/2)

e−αr2

dα

0

with s > 0. By contrast, Ventevogel and Nijboer showed that Z does not minimize energy for the potential function r  → 1/(16 + r4), which is not a completely monotonic function of squared distance.

It follows from Bernstein’s theorem that if a periodic conﬁguration is a ground state for every Gaussian, then the same is true for every completely monotonic function of squared distance (by monotone convergence, because the potential is an increasing limit of weighted sums of ﬁnitely many Gaussians). Following Cohn and Kumar [14], who gave a diﬀerent proof of optimality in one dimension, we call such a conﬁguration universally optimal:

Deﬁnition 1.3. Let C be a point conﬁguration in Rd with density ρ, where ρ > 0. We say C is universally optimal if it minimizes p-energy whenever p: (0,∞) → R is a completely monotonic function of squared distance.

Note that the role of density in this deﬁnition is purely bookkeeping. If C is a universal optimum in Rd with density 1, then ρ−1/dC is a universal optimum with density ρ for any ρ > 0, because the set of completely monotonic functions is invariant under rescaling the input variable. We can also reformulate universal optimality by ﬁxing a Gaussian and varying the density: a periodic conﬁguration C in Rd with density 1 is universally optimal if and only if for every ρ > 0, the conﬁguration ρ−1/dC is a ground state for r  → e−πr2. This perspective on the Gaussian core model is common in the physics literature, such as [50], because varying the density of particles governed by a ﬁxed interaction is a common occurrence in physics, while changing how they interact is more exotic.

It might seem more natural to use completely monotonic functions of distance, rather than squared distance, but squared distance turns out to be

- a better choice (for example, in allowing Gaussians). One can check that every completely monotonic function of distance is also a completely monotonic


function of squared distance; equivalently, if r  → g r2 is completely monotonic, then so is g itself.2 Thus, using squared distance strengthens the deﬁnition.

When a conﬁguration is universally optimal, it has an extraordinary degree of robustness: it remains optimal for a broad range of potential functions, rather than depending on the speciﬁc potential. Numerical studies of energy minimization indicate that universal optima are rare [16], and this special property highlights their importance across diﬀerent ﬁelds.

Before the present paper, no examples of universal optima in Rd with d > 1 had been rigorously proved. In fact, for d > 1 no proof was known of a ground state for any inverse power law or similarly natural repulsive potential function. The most noteworthy theorem we are aware of along these lines is a proof by Theil [51] of crystallization for certain Lennard-Jones-type potentials in R2. However, the potentials analyzed by Theil are attractive at long distances, and the proof makes essential use of this attraction.

Despite the lack of proof, the A2 root lattice (i.e., the hexagonal lattice) is almost certainly universally optimal in R2. It is known to be universally optimal among lattices [36], and proving its universal optimality in full generality is an important open problem.

The case of three dimensions is surprisingly tricky even to describe. For the potential function r  → e−πr2, the appropriately scaled face-centered cubic lattice is widely conjectured to be optimal among lattices of density ρ as long as ρ ≤ 1, while the body-centered cubic lattice is conjectured to be optimal when ρ ≥ 1. At density 1, they have the same energy by Poisson summation, because they are dual to each other. However, one can sometimes lower the energy by moving beyond lattices: Stillinger [50] applied Maxwell’s double tangent construction to obtain a small neighborhood around density 1, namely (0.99899854...,1.00100312...), in which phase coexistence between these lattices improves upon both of them by a small amount. Speciﬁcally, at density 1 phase coexistence lowers the energy by approximately 0.0004%, in a way that seemingly cannot be achieved exactly by any periodic conﬁguration. Thus, the behavior of the Gaussian core model in three dimensions is more complex than one might expect from the case of lattices. Even guessing the ground states on the basis of simulations is far from straightforward, and proofs seem to be well beyond present-day mathematics.

In contrast, we completely resolve the cases of eight and twenty-four dimensions, as conjectured in [14]:

2That is, if p is completely monotonic on (0, ∞), then so is r  → p r1/2 . More generally, if p and q are both completely monotonic functions, then so is the composition p ◦ q. The reason is that if one computes the k-th derivative (p ◦ q)(k), for example using Faa` di Bruno’s formula, then each term has sign (−1)k, as desired.

Theorem 1.4. The E8 root lattice and the Leech lattice are universally optimal in R8 and R24, respectively. Furthermore, they are unique among periodic conﬁgurations, in the following sense. Let C be E8 or the Leech lattice, and let C be any periodic conﬁguration in the same dimension with the same density. If there exists a completely monotonic function of squared distance p such that Ep(C ) = Ep(C) < ∞, then C is isometric to C.

Of course, the uniqueness assertion cannot hold among all conﬁgurations, because removing a single particle changes neither the density nor the energy. Uniqueness also trivially fails when p decays slowly enough that Ep(C) = ∞, because universal optimality then implies that Ep(C ) = ∞ for every C . One could attempt to renormalize a divergent potential (analogously to the analytic continuation of the Epstein zeta function), but we will not address that possibility. See [26] and [44] for more information about renormalization.

Even for lattices, Theorem 1.4 has numerous consequences, including extreme values of the theta and Epstein zeta functions. For another application, consider a ﬂat torus T = Rd/Λ, where Λ is a lattice in Rd. The height of T is a regularization of −log det∆T, where ∆T is the Laplacian on T (see [6] or [44]). If T has volume 1, then the height is a constant depending only on d plus

Å

ã

1 s − d/2

π−d/2Γ(d/2)ζΛ(s) −

lim

,

s→d/2

by Theorem 2.3 in [6]. Thus, if Λ is universally optimal, then T minimizes height among all ﬂat d-dimensional tori of ﬁxed volume. The minimal height was previously known only when d = 1 (trivial), d = 2 (due to Osgood, Phillips, and Sarnak [39]), and d = 3 (due to Sarnak and Stro¨mbergsson [44]), to which we can now add d = 8 and d = 24, as conjectured in [44]:

Corollary 1.5. Let d be 8 or 24, and let Λd be E8 or the Leech lattice, accordingly. Among all lattices Λ in Rd with determinant 1, the minimum value of ζΛ(s) for each s ∈ (0,∞)\{d/2} is achieved when Λ = Λd, as is the minimum value of ΘΛ(it) for each t > 0. Furthermore, Rd/Λd has the smallest height among all d-dimensional ﬂat tori of volume 1. For each of these optimization problems, Λd is the unique optimal lattice with determinant 1, up to isometry.

Optimality and uniqueness for ζΛ(s) with s > d/2 and for ΘΛ(it) follow from Theorem 1.4, as does optimality for the height. To deal with 0 < s < d/2 and to prove uniqueness (as well as optimality) for the height, we can use the formula

∞

1 s

π−sΓ(s)ζΛ(s) =

ΘΛ(it) − 1 ts−1 dt −

1

∞

1 s − d/2

ΘΛ∗(it) − 1 td/2−s−1 dt +

+

1

(see, for example, equation (42) in [44]) to reduce to the case of Θ(it), because Λ∗d = Λd. Note also that Corollary 1.5 and the functional equation for the Epstein zeta function imply that ζΛ(s) is minimized at Λ = Λd when s < 0 and

s is even, and maximized when s < 0 and s is odd.

Although this corollary was not previously known, it is in principle more tractable than Theorem 1.4, because the lattice hypothesis reduces these assertions to optimization problems in a ﬁxed, albeit large, number of variables.

1.3. Linear programming bounds. Our impetus for proving Theorem 1.4 was Viazovska’s solution of the sphere packing problem in eight dimensions [53], as well as our extension to twenty-four dimensions [15]. These papers proved conjectures of Cohn and Elkies [12] about the existence of certain special functions, which imply sphere packing optimality via linear programming bounds. The underlying analytic techniques are by no means limited to sphere packing, and they intrinsically take into account long-range interactions. In particular, by combining the approach of Cohn and Elkies with techniques originated by Yudin [56], Cohn and Kumar [14] extended this framework of linear programming bounds to potential energy minimization in Euclidean space. To prove Theorem 1.4, we prove Conjecture 9.4 in [14] for eight and twenty-four dimensions. (The case of two dimensions remains open.) As a corollary of our construction, we also obtain the values at the origin of the optimal auxiliary functions in these bounds, which agree with Conjecture 6.1 in [17].

Recall that linear programming bounds work as follows (see [9, 10] for further background). A Schwartz function f : Rd → C is an inﬁnitely diﬀerentiable function such that for all c > 0, the function f(x) and all its partial derivatives of all orders decay as O |x|−c as |x| → ∞. We normalize the Fourier transform by

f(y) =

f(x)e−2πi x,y dx,

Rd

where  ·,·  denotes the standard inner product on Rd. Then linear programming bounds for energy amount to the following proposition:

Proposition 1.6. Let p: (0,∞) → [0,∞) be any function, and suppose f : Rd → R is a Schwartz function. If f(x) ≤ p |x| for all x ∈ Rd \ {0} and f(y) ≥ 0 for all y ∈ Rd, then every point conﬁguration in Rd with density ρ has lower p-energy at least ρ f(0) − f(0).

In other words, we can certify a lower bound for p-energy by exhibiting an auxiliary function f satisfying speciﬁc inequalities. There is no reason to believe a sharp lower bound can necessarily be certiﬁed in this way. Indeed, in most cases the certiﬁable bounds seem to be strictly less than the true

ground state energy, and the gap between them can be large when the potential function is steep. For example, for conﬁgurations of density 1 in R3 under the Gaussian potential function r  → e−αr2, the best linear programming bound known (obtained by applying the constructions from [1] to potential energy) is roughly 3.59% less than the lowest energy known when α = π, and 15.4% less when α = 2π. Nevertheless, this technique suﬃces to prove Theorem 1.4.

Cohn and Kumar [14, Proposition 9.3] proved Proposition 1.6 for the special case of periodic conﬁgurations C. Since the proof is short and motivates much of what we do in this paper, we include it here. The proof uses the Poisson summation formula

1 vol Rd/Λ y∈Λ∗

f(y)e2πi v,y ,

f(x + v) =

x∈Λ

which holds when f : Rd → C is a Schwartz function, v ∈ Rd, Λ is a lattice in Rd, and

Λ∗ = {y ∈ Rd : x,y ∈ Z for all x ∈ Λ} is its dual lattice.

Proof of Proposition 1.6 for periodic conﬁgurations. Because C is periodic, we can write it as the disjoint union of Λ + vj for 1 ≤ j ≤ N, where Λ is a lattice and v1,...,vN ∈ Rd. Then the inequality between f and p and the formula (1.1) for energy yield the lower bound

N

1 N

Ep(C) =

p |x + vj − vk|

j,k=1 x∈Λ\{vk−vj}

N

1 N

≥

f(x + vj − vk)

j,k=1 x∈Λ\{vk−vj}

N

1 N

f(x + vj − vk) − f(0).

=

j,k=1 x∈Λ

(We can apply (1.1) because p ≥ 0: if the sum diverges, then Ep(C) = ∞ anyway.) Applying Poisson summation to this lower bound and using the nonnegativity of f and the equation N = ρvol Rd/Λ then shows that

N vol Rd/Λ y∈Λ∗

Ep(C) ≥

f(y)

≥ ρ f(0) − f(0), as desired.

N

1 N

e2πi vj,y

j=1

2

− f(0)

This proof works only for periodic conﬁgurations, but Proposition 1.6 makes no such assumption. The general case was proved by Cohn and de CourcyIreland in [11, Proposition 2.2].

Proposition 1.6 shows how to obtain a lower bound for p-energy from an auxiliary function f satisfying certain inequalities, but it says nothing about how to construct f. Optimizing the choice of f to maximize the resulting bound is an unsolved problem in general. Without loss of generality, we can assume that f is a radial function (i.e., f(x) depends only on |x|), because all the constraints are invariant under rotation and we can therefore radially symmetrize f by averaging all its rotations. We are faced with an optimization problem over functions of just one radial variable, but this problem too seems to be intractable in general.

Fortunately, one can characterize when the bound is sharp for a periodic conﬁguration. For simplicity, consider a lattice Λ. Examining the loss in the inequalities in the proof given above shows that f proves a sharp bound for Ep(Λ) if and only if both

- (1.2)

- f(x) = p(|x|) for all x ∈ Λ \ {0}, and
- f(y) = 0 for all y ∈ Λ∗ \ {0}.


Furthermore, equality must hold to second order, because f(x) ≤ p(|x|) and f(y) ≥ 0 for all x and y. Equivalently, if f is radial, then the radial derivatives of f and f satisfy

- (1.3)


- f (x) = p (|x|) for all x ∈ Λ \ {0}, and
- f (y) = 0 for all y ∈ Λ∗ \ {0}.


We will see that these conditions suﬃce to determine f in 8 or 24 dimensions.

1.4. Interpolation. For the analogous problem of energy minimization in compact spaces studied in [14], conditions (1.2) and (1.3) make it simple to construct the optimal auxiliary functions for most of the universal optima that are known. The point conﬁgurations are ﬁnite sets, and thus we have only ﬁnitely many equality constraints for f to achieve a sharp bound. To construct f, one can simply take the lowest-degree polynomial that satisﬁes these constraints. It is far from obvious that this construction works, i.e., that f satisﬁes the needed inequalities elsewhere, but at least describing this choice of f is straightforward. The description amounts to polynomial interpolation (more precisely, Hermite interpolation, since one must interpolate both values and derivatives).

In Euclidean space, describing the optimal auxiliary functions is far more subtle. It again amounts to an interpolation problem, this time for radial Schwartz functions. The interpolation points are known explicitly for R8 and

R24: the nonzero vectors in E8 have lengths √2n for integers n ≥ 1, and those in the Leech lattice have lengths √2n for n ≥ 2. What is required is to control the values and radial derivatives of f and f at these inﬁnitely many points. However, simultaneously controlling f and f is not easy, and we quickly run up against uncertainty principles [13]. The feasibility of interpolation depends on the exact points at which we are interpolating, and we do not know how to resolve these questions in general.

The fundamental mystery is how polynomial interpolation generalizes to inﬁnite-dimensional function spaces. One important case that has been thoroughly analyzed is Shannon sampling, which amounts to interpolating the values of a band-limited function (i.e., an entire function of exponential type) at linearly spaced points; see [27] for an account of this theory. Shannon sampling suﬃces to prove that Z is universally optimal [14, p. 142], but it cannot handle any higher-dimensional cases.

To construct the optimal auxiliary functions in R8 and R24, we prove a new interpolation theorem for radial Schwartz functions. Let Srad(Rd) denote the set of radial Schwartz functions from Rd to C. For f ∈ Srad(Rd), we abuse notation by applying f directly to radial distances (i.e., if r ∈ [0,∞), then f(r) denotes the common value of f(x) when |x| = r), and we let f denote the radial derivative. As above, f denotes the d-dimensional Fourier transform of f, which is again a radial function, and f denotes the radial derivative of f.

Theorem 1.7. Let (d,n0) be (8,1) or (24,2). Then every f ∈ Srad(Rd) is uniquely determined by the values f √2n , f √2n , f √2n , and f √2n for integers n ≥ n0. Speciﬁcally, there exists an interpolation basis an,bn, an, bn ∈ Srad(Rd) for n ≥ n0 such that for every f ∈ Srad(Rd) and x ∈ Rd,

- (1.4)


∞

f(x) =

n=n0

+

n=n0

∞

√

2n an(x) +

f

f

n=n0

∞

∞

√

f

2n an(x) +

f

n=n0

√

2n bn(x)

√

2n bn(x),

where these series converge absolutely.

One could likely weaken the decay and smoothness conditions on f, along the lines of Proposition 4 in [40], but determining the best possible conditions seems diﬃcult.

Theorem 1.7 tells us that in R8 or R24, the optimal auxiliary function f for a potential function p is uniquely determined by the necessary conditions

- (1.2) and (1.3), assuming it is a Schwartz function. Speciﬁcally, f satisﬁes the


conditions

√

√

√

√

2n , f

f

2n = p

2n , f

2n = p

√

√

2n = 0, f

2n = 0

for n ≥ n0, and (1.4) then gives a formula for f in terms of the interpolation basis, which we will explicitly construct as part of the proof of Theorem 1.7. The same is also true for the auxiliary functions for sphere packing constructed in [53] and [15]:

Corollary 1.8. In R8 and R24, the optimal auxiliary functions for the linear programming bounds for sphere packing or Gaussian potential energy minimization are unique among radial Schwartz functions.

Theorem 1.7 was conjectured by Viazovska as part of the strategy for her solution of the sphere packing problem in R8. Note that the interpolation formula is not at all obvious, or even particularly plausible. The lack of plausibility accounts for why it had not previously been conjectured, despite the analogy with energy minimization in compact spaces.

The proof of the interpolation formula develops the techniques introduced by Viazovska in [53] into a broader theory. Radchenko and Viazovska took a signiﬁcant step in this direction by proving an interpolation formula for single roots in one dimension [40], but extending it to double roots introduces further diﬃculties.

Theorem 1.7 extends naturally to characterize exactly which sequences can occur as f √2n , f √2n , f √2n , and f √2n for n ≥ n0, with f a radial Schwartz function. The only restriction on these sequences is on their decay rate. To state the result precisely, let S(N) be the space of rapidly decreasing sequences of complex numbers. In other words, (xn)n≥1 ∈ S(N) if and only if limn→∞ nkxn = 0 for all natural numbers k.

Theorem 1.9. Let (d,n0) be (8,1) or (24,2). Then the map sending f ∈ Srad(Rd) to

is an isomorphism from Srad(Rd) to S(N)4, whose inverse is given by (1.4).ä In other words, the inverse isomorphism maps

Ä

√

√

√

√

, f

, f

f

2n n≥n

, f

2n n≥n

2n n≥n

2n n≥n

0

0

0

0

to the function ä

Ä

αn)n≥n0, βn n≥n

, αn n≥n

, βn n≥n

0

0

0

∞

∞

∞

∞

αn an +

βn bn +

αn an +

βn bn.

n=n0

n=n0

n=n0

n=n0

One consequence of this theorem is that there are no systematic linear relations between the values f √2n , f √2n , f √2n , and f √2n for n ≥ n0 (i.e., relations that hold for all f ∈ Srad(Rd)). By contrast, Poisson summation over E8 or the Leech lattice gives such a relation between f √2n and f √2n for n ≥ 0.

Another consequence is that the values and derivatives of the interpolation basis functions and their Fourier transforms at the interpolation points are all 0 except for a single 1, which cycles through all these possibilities. It follows from the inverse isomorphism in Theorem 1.9 that in terms of the Kronecker delta,

√

√

√

√

an

2m) = 0, bn

2m) = δm,n, a n

2m) = 0, an

2m) = 0, an

√

√

√

√

2m) = 0, an

2m) = 0, b n

2m) = δm,n, bn

2m) = 0, bn

√

√

√

√

2m) = 0, bn

2m) = 0, a n

2m) = 0, an

2m) = δm,n, an

√

√

√

√

2m) = 0, b n

2m) = 0, bn

2m) = 0, bn

2m) = δm,n

for integers m,n ≥ n0. (By contrast, Theorem 1.7 allows the possibility that our interpolation basis could be redundant.) These equations uniquely

determine the functions an, bn, an, and bn, by the interpolation theorem itself. Furthermore, it follows that an = an and bn = bn.

The function b1 is characterized by b1 √2n = 0, b1 √2n = 0, and

- b1 √2n = 0 for n ≥ n0, while b1 √2n = 0 for n > n0 and b1 √2n0 = 1. Up to a constant factor, these equations are the same conditions satisﬁed by the sphere packing auxiliary functions constructed in [53] for d = 8 and [15] for d = 24. Thus the constructions in those papers are subsumed as a special case of the interpolation basis.


The interpolation theorem amounts to constructing certain radial analogues of Fourier quasicrystals. Deﬁne a radial Fourier quasicrystal to be a radial tempered distribution T on Rd such that both T and T are supported on discrete sets of radii, where T is characterized as usual by

T(x)f(x)dx =

Rd

T(x) f(x)dx

Rd

for f ∈ Srad(Rd). To reformulate the interpolation theorem in these terms, let δr denote a spherical delta function with mass 1 on the sphere of radius r about the origin, or equivalently let

f(x)δr(x)dx = f(r)

Rd

#### for f ∈ Srad(Rd), and deﬁne µr by

f(x)µr(x)dx = f (r)

Rd

for f ∈ Srad(Rd). (Note that µr is also supported on the sphere of radius r about the origin.) If we set

∞

∞

bn(x)µ√2n − δ|x|, then

an(x)δ√2n +

Tx =

n=n0

n=n0

∞

∞

an(x)δ√2n −

bn(x)µ√2n by Theorem 1.7. Thus, Tx is a radial Fourier quasicrystal.

Tx = −

n=n0

n=n0

Dyson [21] highlighted the importance of classifying Fourier quasicrystals in R1, and radial Fourier quasicrystals are a natural generalization of this problem. In the non-radial case, Fourier quasicrystals satisfying certain positivity and uniformity hypotheses can be completely described using Poisson summation [32], but even a conjectural classiﬁcation remains elusive in general.

1.5. Proof techniques. In light of Theorem 1.7 and its interpolation basis, we can write down the only possible auxiliary function f that could prove a sharp bound for E8 or the Leech lattice under a potential p (with d = 8 or 24, accordingly), at least among radial Schwartz functions:

- (1.5) f(x) =

∞

n=n0

p

√

2n an(x) +

∞

n=n0

p

√

2n bn(x).

The proof of Theorem 1.4 then amounts to checking that f(x) ≤ p |x| for all x ∈ Rd \ {0} and f(y) ≥ 0 for all y ∈ Rd. (Once we prove these inequalities, the necessary conditions for a sharp bound become suﬃcient as well.) As noted above, it suﬃces to prove the theorem when p is a Gaussian, i.e., p(r) = e−αr2 for some constant α > 0.

Thus, our primary technical contribution is to construct the interpolation basis. To do so, we analyze the generating functions

- (1.6) F(τ,x) = n≥n0

an(x)e2πinτ + 2πiτ

n≥n0

√

2nbn(x)e2πinτ

and

- (1.7) F‹(τ,x) = n≥n0


√

an(x)e2πinτ + 2πiτ

2n bn(x)e2πinτ,

n≥n0

where x ∈ Rd and τ is in the upper half-plane H = {z ∈ C : Im(z) > 0}. These generating functions determine the basis, as we show in (3.6) and (3.7), and in

Section 5.4 we prove integral formulas for the basis functions, which generalize the formulas for b1 from the sphere packing papers [53, 15].

One motivation for the seemingly extraneous factors of 2πiτ √2n in these generating functions is that they match (1.5) with τ = iα/π and p(r) = e−αr2 = eπiτr2, because

√

√

√

2n = e2πinτ and p

2ne2πinτ.

2n = 2πiτ

p

In other words, the auxiliary function f from (1.5) for this Gaussian potential function is given by f(x) = F(τ,x) = F(iα/π,x).

We can write the interpolation formula for a complex Gaussian x  → eπiτ|x|2 in terms of F and F‹. Speciﬁcally, the Fourier transform of x  → eπiτ|x|2 as a function on Rd is x  → (i/τ)d/2eπi(−1/τ)|x|2, and hence the interpolation formula

- (1.4) for x  → eπiτ|x|2 amounts to the identity


- (1.8) F(τ,x) + (i/τ)d/2F‹(−1/τ,x) = eπiτ|x|2.

In Section 3.1, we will show using a density argument in Srad(Rd) that it suﬃces to prove the interpolation theorem for complex Gaussians of the form x  → eπiτ|x|2 with τ ∈ H. Thus, constructing the interpolation basis amounts to solving the functional equation (1.8) using functions F and F‹ with expansions of the form (1.6) and (1.7).

These expansions for F and F‹ are not quite Fourier expansions in τ, because they contain terms proportional to τe2πiτn. In particular, they are not periodic in τ, but they are annihilated by the second-order diﬀerence operator. In other words,

- (1.9) F(τ + 2,x) − 2F(τ + 1,x) + F(τ,x) = 0 and
- (1.10) F‹(τ + 2,x) − 2F‹(τ + 1,x) + F‹(τ,x) = 0.


Subject to suitable smoothness and growth conditions, proving the interpolation theorem amounts to constructing functions F and F‹ satisfying the functional equations (1.8), (1.9), and (1.10), as we will show in Theorem 3.1.

To solve these functional equations, we use Laplace transforms of quasimodular forms. This approach was introduced by Viazovska in her solution of the sphere packing problem in eight dimensions [53], and we make heavy use of her techniques. In [53], only modular forms of level at most 2 and the quasimodular form E2 were needed. However, these functions turn out to be insuﬃcient to construct our interpolation basis, and we must augment them with a logarithm of the Hauptmodul λ for Γ(2). Using this enlarged set of functions, we can describe F and F‹ explicitly. The proof of the interpolation theorem then amounts to verifying analyticity, growth bounds, and functional equations for our formulas.

Once we have obtained these formulas, only one step remains in the proof of Theorem 1.4. Let p be a Gaussian potential function, and deﬁne the auxiliary function f by (1.5). To complete the proof of Theorem 1.4, we must show that f(x) ≤ p |x| for all x ∈ Rd\{0} and f(y) ≥ 0 for all y ∈ Rd. These inequalities look rather diﬀerent, but we will see that they are actually equivalent to each other, thanks to a duality transformation introduced in Section 6 of [17]. We show in Section 6.1 that the underlying inequality (Proposition 6.1) follows from the positivity of the kernel in the Laplace transform, as well as a truncated version of the kernel when d = 24. Unfortunately we have no conceptual proof of this positivity, but we are able to prove it by combining various analytic methods, including interval arithmetic computations. This inequality then completes the proof of universal optimality.

1.6. Origins of the argument. The way we present the proof in this paper diﬀers substantially from how we initially arrived at the ideas. Before we turn to the body of the paper, we will brieﬂy outline our original approach here, to show how it is rooted in the papers [53] and [15].

We began with the Ansatz that there were basis functions an, bn, an, and bn for which Theorems 1.7 and 1.9 held. We then tried to construct these functions using the techniques of [53] and [15], by splitting them into eigenfunctions for the Fourier transform and constructing each eigenfunction as an integral transform T (ϕ) of a corresponding function ϕ. Speciﬁcally,

T (ϕ)(x) = 4sin π|x|2/2 2

∞

ϕ(it)e−π|x|2t dt

0

for suﬃciently large |x|, and we extend it to small |x| by analytic continuation. To ensure that T (ϕ) is an eigenfunction of the Fourier transform, the kernel ϕ must satisfy certain quasimodularity hypotheses. Obtaining eigenfunctions with the desired behavior at the radii √2m amounts to controlling the asymptotic behavior of ϕ(it) as t → ∞ up to an additive o(1) term (i.e., specifying the non-decaying terms in its q-expansion).

In each case we examined with eigenvalue +1, we could construct a suitable kernel ϕ by using modular forms for SL2(Z) and the quasimodular form E2, just as in [53] and [15]. However, we were unable to construct the −1 eigenfunctions using only modular forms of level 2, as we had hoped based on the earlier papers. These modular forms suﬃced to solve the sphere packing problem in dimensions 8 and 24, but there were simply not enough of them to construct the putative interpolation basis. Instead, we found a natural generalization of the proof technique that would require a special function satisfying certain transformation laws, which we will state as (2.17) below. This function would play a role analogous to that of E2.

We managed to obtain such a function as an integral, after which we recognized it as a logarithm L of the Hauptmodul λ. Using this expanded set of functions, we seemed to be able to obtain any given interpolation basis function we wanted (by constructing both the +1 and the −1 eigenfunction components), but the kernel ϕ grew more complicated as the index n of the basis function increased, and the general pattern remained unclear. Ad hoc constructions of individual basis functions did not supply enough information for us to understand the basis as a whole.

To try to clarify the pattern, we sought generating functions K(τ,z) and K(τ,z) along the lines of (1.6) and (1.7) for the kernels, rather than the interpolation basis functions. For example,

√

ϕn(z)e2πinτ + 2πiτ

2nψn(z)e2πinτ,

K(τ,z) =

n≥n0

n≥n0

where the kernels ϕn and ψn satisfy T (ϕn) = an and T (ψn) = bn. Duke and Jenkins [20] had analyzed generating functions for a similar but simpler scenario, and we adapted their techniques. We guessed by analogy with their work that our generating functions would have denominator ∆(τ)∆(z)2(j(τ) − j(z)) and numerators given by linear combinations of 1, E2, and L with modular forms of certain weights in τ and z as coeﬃcients. In other words, the numerators could be parametrized by ﬁnitely many undetermined coeﬃcients. We then solved for the numerators by computing enough kernels to determine them uniquely. Once we had arrived at explicit formulas for the generating functions, we proved using techniques inspired by [20] that the formulas were correct, i.e., that the resulting interpolation basis functions had the desired values and radial derivatives at the radii √2m.

These generating functions provided a construction of the interpolation basis, but we still did not know that this basis suﬃced to reconstruct every radial Schwartz function. To analyze the basis further, we had to deal with analytic diﬃculties. For example, one might naively hope to obtain the interpolation basis generating function F(τ,x) from the kernel generating function K(τ,z) when |x| is suﬃciently large via

∞

F(τ,x) = 4sin π|x|2/2 2

K(τ,it)e−π|x|2t dt,

0

by interchanging the integral transform with the sum in the generating function. However, the integral and sum cannot be interchanged, and this formula is incorrect. Instead, the right side needs an extra eπiτ|x|2 term. These sorts of analytic issues arise frequently in the study of F and K, because z  → K(τ,z) has poles at many of the points in the SL2(Z)-orbit of τ (where the j(τ) − j(z) factor in the denominator vanishes). Understanding these poles and their residues turns out to be crucial for our proof of the interpolation theorem.

As we developed this theory further, our focus shifted to the generating functions F and F‹ and their functional equations, and our original derivation of the kernel generating functions was no longer needed. In the present paper, the kernel generating functions are analyzed diﬀerently in Section 4, and it is only after completing the proof of the interpolation theorem that we show they fulﬁll their original purpose in Section 5.4. Instead of starting with the kernel generating function, we begin instead by analyzing the functional equations for F and F‹, before relating them to kernels constructed using modular forms.

1.7. Organization of the paper. We begin by collecting background information about modular forms, elliptic integrals, and radial Schwartz functions in Section 2. Sections 3 and 4 are the heart of the paper. Section 3 shows how to reduce the interpolation theorem to the existence of generating functions with certain properties, and Section 4 describes the generating functions explicitly as integral transforms of kernels obtained by carefully analyzing an action of PSL2(Z). It is not obvious that this construction has all the necessary properties, and Section 5 completes the proof of the interpolation theorem by verifying analytic continuation and growth bounds. Proving universal optimality requires additional inequalities, which are established in Section 6. Finally, we discuss generalizations and open problems in Section 7.

### 2. Preliminaries and background on modular forms

Much of the machinery of our proof rests on properties of classical modular forms, in particular their growth rates and transformation laws. This section summarizes those features which are used later in the paper, as well as background about elliptic integrals and radial Schwartz functions. For more information about modular forms, see [8, 28, 46, 57].

2.1. Modular and quasimodular forms. Let H denote the complex upper half-plane {z ∈ C : Im(z) > 0}. The group SL2(R) acts on H by fractional linear transformations Ç

å

az + b cz + d

a b c d

· z =

.

For any integer k and γ = ac db ∈ SL2(R), deﬁne the slash operator on functions f : H → C by the rule3

ã

Å

az + b cz + d

- (2.1) (f|kγ)(z) = (cz + d)−kf


.

3When necessary, we will abuse notation by using a superscript on the slash notation to disambiguate which variable it applies to. For example, we write f(τ, z) |z2 ( 10 −01 ) or (f|z2( 01 −01 ))(τ, z) for z−2f(τ, −1/z).

We deﬁne the factor of automorphy j(γ,z) by

- (2.2) j(γ,z) = cz + d;


note that it satisﬁes the identity j(γ1γ2,z) = j(γ1,γ2z)j(γ2,z), which implies that f|k(γ1γ2) = (f|kγ1)|kγ2.

Let Γ be a discrete subgroup of SL2(R) such that the quotient Γ\H has ﬁnite volume. Recall that a holomorphic modular form of weight k for Γ is a holomorphic function f : H → C such that f|kγ = f for all γ ∈ Γ, and that furthermore satisﬁes a polynomial boundedness condition at each cusp (see [8, 28, 46] for details). The space of holomorphic modular forms of weight k for Γ will be denoted Mk(Γ). It contains the subspace Sk(Γ) of weight k cusp forms for Γ; these are the modular forms that vanish at all the cusps of Γ\H. On the other hand, we may relax the deﬁnition to allow modular functions that are holomorphic on H but merely meromorphic at the cusps (equivalently, they satisfy an exponential growth bound near the cusps). This deﬁnes the space M!k(Γ) of weakly holomorphic modular forms, which is inﬁnite-dimensional whenever Γ has a cusp.

When Γ is a congruence subgroup of SL2(Z), i.e., one that contains

®

Ç

å

´

1 0 0 1

γ ∈ SL2(Z) : γ ≡

Γ(N) =

(mod N)

for some N, the boundedness condition deﬁning Mk(Γ) is simply that |(f|kγ)(z)| is bounded as Im(z) → ∞, for every γ ∈ SL2(Z). Similarly, Sk(Γ) is deﬁned by the condition that (f|kγ)(z) → 0 as Im(z) → ∞, while M!k(Γ) is deﬁned by the condition that |(f|kγ)(z)| is bounded above by a polynomial in eIm(z). Since SL2(Z) is generated by

Ç

å

Ç

å

- 0 −1
- 1 0


1 1 0 1

- (2.3) T =


and S =

,

we will often indicate the action of SL2(Z) on a modular form for a congruence subgroup by giving the action of the slash operators corresponding to S and T.

The element −I ∈ SL2(R) acts trivially on H, and thus the action of SL2(R) descends to an action of PSL2(R) = SL2(R)/{±I}. We write Γ to denote the image of a subgroup Γ of SL2(R) in PSL2(R). The group PSL2(Z) = SL2(Z) has an elegant presentation in terms of the generators S and T, namely PSL2(Z) = S,T | S2 = (ST)3 = I , and its subgroup Γ(2) of index 6 is freely generated by T2 and ST2S (with cusps 0, 1, and ∞).

We next describe the structure of the graded rings M!(Γ) =

M!k(Γ)

k∈Z

and

M(Γ) =

Mk(Γ)

k∈Z

for the cases of interest in this paper, which are the congruence subgroups Γ = Γ(N) for N = 1,2. In these cases, the weight k of any nonzero modular form is necessarily even because −I ∈ Γ.

2.1.1. Modular forms for Γ(1) = SL2(Z). Here all modular forms can be described in terms of the Eisenstein series

- 1

- 2ζ(k) (m,n)∈Z2


(mz + n)−k

Ek(z) =

(m,n) =(0,0)

∞

2k Bk

σk−1(n)e2πinz

= 1 −

n=1

for even integers k ≥ 4, where Bk is the k-th Bernoulli number and σ (n) =

d|n d is the -th power divisor sum function. The ring M(SL2(Z)) is the free polynomial ring over C with generators

∞

σ3(n)qn and

E4(z) = 1 + 240

n=1

∞

σ5(n)qn,

E6(z) = 1 − 504

n=1

where we use the customary shorthand q = e2πiz. In particular, õ

®

û

k 12

1 for k ≡ 0,4,6,8,10 (mod 12), and 0 for k ≡ 2 (mod 12)

- (2.4) dimMk(SL2(Z)) =


+

for even integers k ≥ 0, and the identities E8 = E42, E10 = E4E6 and E14 = E42E6 hold because the modular forms of weight 8, 10, or 14 form a onedimensional space. Let

E4(z)3 − E6(z)2 1728

∆(z) =

= q

∞

(1 − qn)24

n=1

denote Ramanujan’s cusp form of weight 12. The product formula shows that ∆ does not vanish on H and satisﬁes the decay estimate

∆(x + iy) = O e−2πy

- for y ≥ 1, uniformly in x ∈ R. In particular, ∆−1 is a weakly holomorphic modular form for SL2(Z). Furthermore, since ∆ vanishes to ﬁrst order at the unique cusp of SL2(Z), we can use it to cancel the pole of any form


f ∈ M!(SL2(Z)): if f has weight k and a pole of order r at the cusp, then ∆rf ∈ Mk+12r(SL2(Z)). It follows that

M!(SL2(Z)) = C[E4,E6,∆−1]. For example, the modular j-invariant deﬁned by

- (2.5) j(z) =

E4(z)3 ∆(z)

= q−1 + 744 + 196884q + 21493760q2 + ···

is in M!0(SL2(Z)), and its derivative, which is in M!2(SL2(Z)), can be expressed as

- (2.6) j (z) = 2πiq

dj dq

= −2πi

E14(z) ∆(z)

,

since both sides share the same leading asymptotics as Im(z) → ∞ and j ∆ lies in the one-dimensional space M14(SL2(Z)).

An important role in this paper (as well as in [53, 15]) is played by the quasimodular form

- (2.7) E2(z) = 1 − 24

∞

n=1

σ1(n)qn =

- 1

- 2πi


∆ (z) ∆(z)

,

which just barely fails to be modular:

- (2.8) E2(z + 1) = E2(z) and E2


Å

ã

−1 z

6iz π

= z2E2(z) −

.

General quasimodular forms for congruence subgroups are polynomials in E2 with modular form coeﬃcients; they may also be obtained by diﬀerentiating modular forms. More precisely, a holomorphic function f : H → C is a quasimodular form for Γ(N) of weight k and depth at most p if it is an element of pj=0 E2jMk−2j(Γ(N)). In other words, depth p corresponds to a degree p polynomial in E2 or to taking the p-th derivative of a modular form (see [7], [30], and [57, Prop. 20]).4

2.1.2. Modular forms for Γ(2). Recall the Jacobi theta functions

- Θ3(z) = θ00(z) = n∈Z

eπin2z,

- Θ4(z) = θ01(z) = n∈Z


(−1)neπin2z, and

eπi(n+12)2z

Θ2(z) = θ10(z) =

n∈Z

##### 4For a more intrinsic deﬁnition of quasimodular form, which applies to non-congruence subgroups of SL2(R) as well, see [57, Section 5.3].

(with their historical numbering), which arise in the classical theory of theta functions. We deﬁne

- (2.9)

- U(z) = θ00(z)4,
- V (z) = θ10(z)4, and
- W(z) = θ01(z)4.


These functions are modular forms of weight 2 for Γ(2), they satisfy the Jacobi identity

- (2.10) U = V + W,

and M(Γ(2)) is the polynomial ring generated by V and W. As was the case for Γ = Γ(1), multiplication by powers of ∆ removes singularities at cusps while increasing the weight. Thus any element of M!(Γ(2)) is again the quotient of an element of M(Γ(2)) by some power of ∆, with the behavior at cusps determined by the numerator and the power of ∆. (In fact, M!(Γ) = M(Γ)[∆−1] for any congruence subgroup Γ, because ∆ is in M(Γ) and vanishes at all cusps.)

The modular forms U, V , and W transform under SL2(Z) as follows:

- (2.11)

U|2T = W, V |2T = −V, W|2T = U, U|2S = −U, V |2S = −W, W|2S = −V.

These formulas specify how modular forms for Γ(2) transform under the larger group SL2(Z). Conversely, every modular form for SL2(Z) is a modular form for Γ(2) and thus can be written in terms of U, V , and W. For example,

- (2.12)

E4 =

- 1

- 2


(U2 + V 2 + W2),

E6 =

- 1

- 2


(U + V )(U + W)(W − V ), and ∆ =

1 256

(UV W)2. It will also be convenient to use the holomorphic square root of ∆ deﬁned by √

∆ =

1 16

UV W, which is a modular form of weight 6 for Γ(2).

Eichler and Zagier [24, Remark after Theorem 8.4] showed as part of a general result that the algebra M(Γ(2)) is a six-dimensional free module over M1 := M(Γ(1)). Their proof shows that

- (2.13) M(Γ(2)) = M1 ⊕ UM1 ⊕ V M1 ⊕ U2M1 ⊕ V 2M1 ⊕ UV WM1,


with the only subtlety being to show that the modular form UV W of weight six does not lie in the direct sum of the ﬁrst ﬁve factors. For comparison, UV lies in M1⊕U2M1⊕V 2M1, because UV = U2+V 2−E4 by (2.10) and (2.12). As M1

is itself the free polynomial ring in U2 +V 2 +W2 and (U +V )(U +W)(W −V ), the decomposition (2.13) can also be deduced from the theory of symmetric polynomials. This decomposition will be used in Section 4.2 in the solution of some functional equations.

2.1.3. The modular function λ and its logarithm. The modular function λ = V/U mapping H to C \ {0,1} is a Hauptmodul for the modular curve X(2) = Γ(2)\(H ∪ P1(Q)) (that is, a generator of its function ﬁeld over C). For example, it is related to the Hauptmodul j for Γ(1) from (2.5) by

256(1 − λ + λ2)3 λ2(1 − λ)2

j =

.

The function λ takes the values 0, 1, and ∞ at the cusps ∞, 0, and −1, respectively, and its restriction λ(it) to the positive imaginary axis decreases from 1 to 0 as t increases from 0 to ∞. If we let

- (2.14) λS(z) := (λ|0S)(z) = λ(−z−1) = 1 − λ(z), then these functions also satisfy the properties
- (2.15) λ(z + 1) =

λ(z) λ(z) − 1

= −

λ(z) λS(z)

and λS(z + 1) =

1 λS(z)

- for z ∈ H. The nonvanishing of λ and λS on H allows us to deﬁne


L(z) =

z

0

λ (w) λ(w)

dw and LS(z) = −

∞

z

λ S(w) λS(w)

dw,

where the contours are chosen to approach the singularities 0 or ∞ on vertical lines. These functions satisfy

L(it) = log(λ(it)) and LS(it) = log(λS(it)) = log(1 − λ(it))

for t > 0, and as such are holomorphic functions for which eL = λ and eLS = λS; however, they are not in general the principal branches of the logarithms of λ or λS. We note the asymptotics

- (2.16)

L(z) = πiz + 4log(2) − 8q1/2 + O(q) and

LS(z) = −16q1/2 −

64q3/2 3

+ O

Ä

q5/2

- as q → 0, where qn/2 = e2πinz/2. ä The functions L and LS have the transformation properties


- (2.17)


L|0T = L − LS + πi, LS|0T = −LS, L|0S = LS, LS|0S = L.

Indeed, the last pair of assertions follows directly from the deﬁnitions and holomorphy. The ﬁrst two assertions, which read

L(z + 1) = L(z) − LS(z) + πi and LS(z + 1) = −LS(z),

are proved by showing that the derivatives of both sides are equal (using the derivatives of the identities in (2.15)) and by comparing the asymptotics (2.16) to determine the constant of integration.

2.2. Elliptic integrals. We normalize the complete elliptic integral of the ﬁrst kind by

π/2

dθ

K(m) =

1 − msin2 θ and of the second kind by

0

E(m) =

π/2

0

1 − msin2 θ dθ.

Note that many references, such as [38, Chapter 19], deﬁne K and E in terms of the elliptic modulus k, so that the complete elliptic integrals are what we call k  → K(k2) and k  → E(k2). Our normalization is less principled from the perspective of elliptic function theory, but it has the advantage of simplifying various expressions that occur later in our paper.

These elliptic integrals satisfy a plethora of beautiful identities, a few of which we list below. First, E and K are related by

- (2.18) K (m) =

E(m) 2m(1 − m) −

K(m) 2m

.

(Here, K denotes the derivative of K. In the elliptic function literature, K is often used instead to denote the elliptic integral with respect to the complementary modulus k =

√

1 − k2.) Legendre proved the identity K(m)E(1 − m) + E(m)K(1 − m) − K(m)K(1 − m) =

π 2

(see [35, pp. 68–69]). The two identities above can be combined to obtain

- (2.19) K(m)K (1 − m) + K (m)K(1 − m) =


π 4m(1 − m)

.

In other words, the Wronskian of K and m  → K(1 − m) has a simple form.

Elliptic integrals are also related to the modular forms of Section 2.1 via classical identities dating back to Jacobi. For z ∈ H on the imaginary axis, the key identity is the inversion formula

Θ3(z)2 = 2π−1K(λ(z))

(see [54, §21.61 and §22.301] or [45, Theorem 5.8]). It follows that for such z,

- (2.20)

- U(z) = 4π−2K(λ(z))2,
- V (z) = 4π−2λ(z)K(λ(z))2, and
- W(z) = 4π−2λS(z)K(λ(z))2,


because U = Θ43, λ = V/U, and U = V + W. Using (2.14) and Jacobi’s transformation law

Θ3(−1/z)2 = −izΘ3(z)2 (which follows immediately from Poisson summation), we obtain

- (2.21)

K(1 − λ(z)) K(λ(z))

= −iz. Diﬀerentiation combined with (2.19) yields the identity λ (z) = 4iπ−1λ(z)(1 − λ(z))K(λ(z))2. Finally, we can use (2.7), (2.12), (2.18), and (2.20) to write

- (2.22) E2(z) = 4π−2K(λ(z)) 3E(λ(z)) − (2 − λ(z))K(λ(z)) .

In Section 6 we will use equations (2.12), (2.20), (2.21), and (2.22) to write the restriction of elements of M!(Γ(2)) (and related quasimodular expressions) to the imaginary axis in terms of elliptic integrals of λ.

The elliptic integrals E and K are holomorphic in the open unit disk. Their behavior near 1 is governed by

- (2.23) E(1−z) = A1(z)+A2(z)log(z) and K(1−z) = A3(z)+A4(z)log(z),


where each Aj is a holomorphic function on the open unit disk with real Taylor coeﬃcients about the origin (see [38, Section 19.12] for explicit formulas). Furthermore, A1 and A3 have nonnegative coeﬃcients, while A2 and A4 have nonpositive coeﬃcients.

2.3. Radial Schwartz functions. For a smooth function f on Rd, deﬁne the Schwartz seminorms by

xα∂βf(x) ,

f α,β = sup x∈Rd

for α,β ∈ Zd≥0, where we use the multi-index notation

ãβ1

Å

ãβ

Å

∂ ∂xd

∂ ∂x1

d

xα = xα11 ···xαdd and ∂β =

···

.

By deﬁnition, f is a Schwartz function if and only if f α,β < ∞ for all α and β, and these seminorms deﬁne the Schwartz space topology on S(Rd). The radial Schwartz space Srad(Rd) is the subspace of radial functions in S(Rd), with the induced topology.

Lemma 2.1. A Schwartz function f on Rd is radial if and only if there exists an even Schwartz function f0 on R such that f(x) = f0 |x| for all x ∈ Rd. Furthermore, the map f0  → f is an isomorphism of topological vector spaces from Srad(R1) to Srad(Rd).

Of course Srad(R1) consists of the even functions in S(R1). For a proof of Lemma 2.1 (in fact, of a slightly stronger result), see [25, Section 3].

For our purposes, the signiﬁcance of Lemma 2.1 is that we can restrict our attention to radial derivatives when dealing with radial Schwartz functions. Let D denote the radial derivative, deﬁned by Df(x) = f 0 |x| , and deﬁne the radial seminorms by

f radk,  = sup x∈Rd

|x|k D f(x)

for k,  ∈ Z≥0. (Note that Srad(Rd) is not closed under D, because the derivative of an even function is odd, but D f(x) is nevertheless well deﬁned.) Then Lemma 2.1 tells us that a smooth, radial function f is a Schwartz function if and only if f radk,  < ∞ for all k and , and these seminorms characterize the topology of Srad(Rd).

We will also need the ﬁrst part of the following lemma, which we prove using the techniques from [40, Section 6]. See also Lemma 2 and Remark 4 in [29] for a more general density result.

Lemma 2.2. The complex Gaussians x  → eπiτ|x|2 with τ ∈ H span a dense subspace of Srad(Rd). In fact, for any y > 0, the same is true if we use only complex Gaussians with Im(τ) = y.

Proof. Compactly supported functions are dense in Srad(Rd), as is easily shown by multiplying by a suitable bump function. Thus it will suﬃce to show that compactly supported, smooth, radial functions can be approximated arbitrarily well by linear combinations of complex Gaussians with Im(τ) = y.

Removing a factor of eπy|x|2 shows that every compactly supported, smooth, radial f on Rd can be written as

f(x) = g(|x|2)e−πy|x|2,

where g is a smooth, compactly supported function on R. Let g be its onedimensional Fourier transform

Then

g(t) =

g(x)e−2πitx dx.

R

g(|x|2) =

g(t)e2πit|x|2 dt = lim

T→∞

R

T

g(t)e2πit|x|2 dt

−T

by Fourier inversion, and hence f(x) = lim

T

g(t)eπi(2t+iy)|x|2 dt. The functions

T→∞

−T

T

g(t)eπi(2t+iy)|x|2 dt

- (2.24) x  →


−T

are Schwartz functions that converge to f in Srad(Rd) as T → ∞, because g is rapidly decreasing and we can therefore control the radial Schwartz seminorms of the error term

g(t)eπi(2t+iy)|x|2 dt.

x  →

R\[−T,T]

Furthermore, for each T, equally spaced Riemann sums for (2.24) converge to this function in Srad(Rd), by the usual error estimate in terms of the derivative. These Riemann sums are linear combinations of complex Gaussians with τ = 2t + iy for diﬀerent values of t in R, as desired.

### 3. Functional equations and the group algebra C[PSL2(Z)]

3.1. From interpolation to functional equations and back. As mentioned in (1.6) and (1.7), we consider the generating functions

√

2nbn(x)e2πinτ

an(x)e2πinτ + 2πiτ

- (3.1) F(τ,x) = n≥n0


n≥n0

and

√

- (3.2) F‹(τ,x) = n≥n0


2n bn(x)e2πinτ

an(x)e2πinτ + 2πiτ

n≥n0

for the interpolation basis, where x ∈ Rd and τ is in the upper half-plane H = {z ∈ C : Im(z) > 0}. In equations (1.8)–(1.10), we derived functional equations for F and F‹from the existence of an interpolation basis. We now show that the converse holds as well: the existence of a well-behaved solution to the functional equations (1.8)–(1.10) implies an interpolation theorem, regardless of the dimension.

Theorem 3.1. Suppose there exist smooth functions F,F‹: H × Rd → C such that

- (1) F(τ,x) and F(τ,x) are holomorphic in τ,
- (2) F(τ,x) and F‹(τ,x) are radial in x,
- (3) for all nonnegative integers k and , the radial derivative Dx with respect to x satisﬁes the uniform bounds


|x|k D xF(τ,x) < αk,  Im(τ)−βk,  + γk, |τ|δk, 

and

|x|k D xF‹(τ,x) < αk,  Im(τ)−βk,  + γk, |τ|δk,  for some nonnegative constants αk, , βk, , γk, , and δk, ,

- (4) in the special case (k, ) = (0,0), max |F(τ,x)|,|F‹(τ,x)| ≤ α0,0 Im(τ)−β0,0

for −1 ≤ Re(τ) ≤ 1 and x ∈ Rd, with β0,0 > 0, and

- (5) F and F‹ satisfy the functional equations (1.8)–(1.10), i.e., F(τ + 2,x) − 2F(τ + 1,x) + F(τ,x) = 0, F‹(τ + 2,x) − 2F‹(τ + 1,x) + F‹(τ,x) = 0, and


F(τ,x) + (i/τ)d/2F‹(−1/τ,x) = eπiτ|x|2.

Then F and F‹ have expansions of the form (3.1) and (3.2) with n0 = 1, for some radial Schwartz functions an,bn, an, bn. Moreover, for every radial Schwartz function f : Rd → R, the interpolation formula

∞

∞

√

√

f(x) =

f

2n an(x) +

f

2n bn(x)

n=1

n=1

∞

∞

√

√

+

f

2n an(x) +

f

2n bn(x),

n=1

n=1

holds, and the right side converges absolutely. Finally, for ﬁxed k and , the radial seminorms

|x|k b(n )(x) , sup

|x|k a(n )(x) , sup x∈Rd

sup

x∈Rd

|x|k b(n )(x) all grow at most polynomially in n.

|x|k a(n )(x) , sup x∈Rd

x∈Rd

Furthermore, a1 = a1 = b1 = b1 = 0 if and only if F(τ,x) and F‹(τ,x) are o e−2πIm(τ) as Im(τ) → ∞ in the strip −1 ≤ Re(τ) ≤ 1 with x ﬁxed.

This last statement concerns starting the interpolation formula at n0 = 2, which Theorem 1.7 asserts is the case for d = 24. The separate condition (4) is important for ruling out a contribution from n = 0 in the interpolation formula; the restriction to the strip −1 ≤ Re(τ) ≤ 1 is because generic solutions to the recurrences in part (5) grow linearly in Re(τ) (see (3.5)).

Proof. We begin by obtaining the expansion of F. The diﬀerence F(τ + 1,x) − F(τ,x)

is holomorphic in τ and invariant under τ  → τ + 1, by the functional equation F(τ + 2,x) − 2F(τ + 1,x) + F(τ,x) = 0.

Thus, for each x there is a holomorphic function gx on the punctured disk {z ∈ C : 0 < |z| < 1} such that

F(τ + 1,x) − F(τ,x) = gx(e2πiτ),

because τ  → e2πiτ is a covering map from H to the punctured disk. Furthermore, it follows from part (4) of the hypotheses that

lim

gx(z) = 0,

z→0

and thus gx extends to a holomorphic function that vanishes at 0. By taking the Taylor series of gx about 0, we obtain coeﬃcients bn(x) for n ≥ 1 such that

- (3.3) F(τ + 1,x) − F(τ,x) = 2πi n≥1

√

2nbn(x)e2πinτ.

To obtain an(x), we remove the bn(x) terms and instead look at F(τ,x) − τ F(τ + 1,x) − F(τ,x) ,

which is again holomorphic in τ and invariant under τ  → τ+1. The parenthetical expression decays exponentially as Im(τ) → ∞ by (3.3), so the bound in part (4) again yields coeﬃcients an(x) for n ≥ 1 such that

- (3.4) F(τ,x) − τ F(τ + 1,x) − F(τ,x) = n≥1

an(x)e2πinτ.

Thus,

- (3.5) F(τ,x) = n≥1

an(x)e2πinτ + 2πiτ

n≥1

√

2nbn(x)e2πinτ.

Because of the symmetry of the hypotheses, the case of F‹ works exactly the same way, with coeﬃcients an(x) and bn(x). The assertion at the end of the theorem statement about when a1 = a1 = b1 = b1 = 0 is then an immediate consequence of formula (3.5) and its counterpart for F‹.

To check that the coeﬃcients are radial Schwartz functions, we note that for any y > 0,

- (3.6) an(x) =

iy

−1+iy

F(τ,x) − τ F(τ + 1,x) − F(τ,x) e−2πinτ dτ

and

- (3.7) bn(x) =


iy

1 2πi√2n

F(τ + 1,x) − F(τ,x) e−2πinτ dτ

−1+iy

by orthogonality using (3.4) and (3.3). We can take radial derivatives in x under the integral sign, because all the derivatives are continuous. If we do so and apply part (3) of the hypotheses, we ﬁnd that the radial seminorms

|x|k an( )(x) and sup x∈Rd

|x|k b(n )(x)

sup

x∈Rd

are all ﬁnite, for any k, , and n. Thus, an and bn are Schwartz functions (see

- Lemma 2.1). Furthermore, if we take y = 1/n and integrate over the straight


line from −1 + iy to iy, we ﬁnd that these radial seminorms of an and bn grow

- at most polynomially in n for each k and . By symmetry, the same holds for


an and bn as well. These estimates imply that the sum

∞

f

n=1

∞

+

f

n=1

∞

√

2n an(x) +

f

n=1

∞

√

2n an(x) +

n=1

√

2n bn(x)

f

√

2n bn(x),

converges absolutely whenever f is a radial Schwartz function, and that this formula deﬁnes a continuous linear functional on Srad(Rd).

All that remains is to prove the interpolation formula. Fix x0 ∈ Rd, and deﬁne the functional Λ on Srad(Rd) by

∞

∞

√

√

Λ(f) =

f

2n an(x0) +

f

2n bn(x0)

n=1

n=1

∞

∞

√

√

f

f

+

2n an(x0) +

2n bn(x0)

n=1

n=1

− f(x0),

so that the interpolation formula for x0 is equivalent to Λ = 0. Because Λ is continuous, it suﬃces to prove that Λ(f) vanishes when f is a complex Gaussian, i.e., f(x) = eπiτ|x|2 with τ ∈ H, by Lemma 2.2. This condition amounts to the function equation

F(τ,x0) + (i/τ)d/2F‹(−1/τ,x0) = eπiτ|x0|2,

because f(x) = (i/τ)d/2eπi(−1/τ)|x|2. Thus, the interpolation formula holds for all radial Schwartz functions, as desired.

Theorem 3.1 reduces Theorem 1.7 to constructing F and F‹, but the only hint it gives for how to do so is the functional equations they must satisfy. The rest of Sections 3 and 4 consists of a detailed study of these functional equations, in terms of the right action of PSL2(Z) via the slash operator |τd/2 in

the τ variable (assuming d/2 is an even integer). Using the standard generators S and T from (2.3), the equation

F(τ,x) + (i/τ)d/2F‹(−1/τ,x) = eπiτ|x|2

expresses F in terms of F‹|τd/2S and vice versa (because S2 = I). It therefore suﬃces to construct F, from which we can obtain F‹. The remaining functional equations are best stated in terms of the linear extension of the slash operator action (2.1) of PSL2(Z) to the group algebra

R = C[PSL2(Z)] of ﬁnite formal linear combinations of elements of PSL2(Z). The equation F(τ + 2,x) − 2F(τ + 1,x) + F(τ,x) = 0 says F is annihilated by the element (T − I)2 = T2 − 2T + I of R, while F‹(τ + 2,x) − 2F‹(τ + 1,x) + F‹(τ,x) = 0

speciﬁes the action of S(T − I)2 on F (see (4.5) below). Thus, the functional equations specify the action of the right ideal I = (T − I)2 · R + S(T − I)2 · R on F. This ideal does not amount to all of R, and in fact dimC(R/I) = 6, as we will see in Proposition 3.9. (For simplicity we write R/I rather than I\R, despite the fact that I is a right ideal.) To make further progress, we must understand the structure of I and the action of PSL2(Z) on the six-dimensional vector space R/I.

3.2. A six-dimensional representation of SL2(Z). Many of our arguments use facts about a particular six-dimensional representation σ of SL2(Z), which we collect here for later reference. We will see in (3.18) that this representation describes the action of PSL2(Z) on R/I.

Recall that PSL2(Z) has the subgroup Γ(2) of index 6, which is freely generated by T2 = 10 21 and ST2S = −21 −01 . The following lemma gives some standard bounds on the length of a word in these generators by the size of the matrix, in a way which will be useful for later applications such as Proposition 4.2. It follows from work of Eichler [23], but we give a direct proof. The idea of column domination that appears in part (1) dates back at least to Markov’s 1954 book on algorithms [34, Chapter VI §10 2.5].

Let γ Frob = (Tr(γγt))1/2 denote the Frobenius norm of γ ∈ SL2(R), i.e., Ç

å 2

a b c d

= a2 + b2 + c2 + d2.

Frob

We apply this norm also to elements of PSL2(R), because γ Frob =  −γ Frob. Recall that it is submultiplicative: γγ Frob ≤ γ Frob γ Frob for all γ and γ .

Lemma 3.2. Let γ1 = T2 and γ2 = ST2S, so that every element γ ∈ Γ(2) ⊆ PSL2(Z) has a unique expression as a ﬁnite reduced word γ1e1γ2f1γ1e2 ··· , with each ei,fi ∈ Z \ {0} except perhaps e1 = 0.

- (1) (Column domination property) The second column of γ has strictly greater Euclidean norm than the ﬁrst column if and only if γ’s reduced word ends in a nonzero power of γ1 = T2.
- (2) The Frobenius norm of γ satisﬁes |e1| + |f1| + |e2| + ··· ≤ γ 2Frob ≤ (2 + 4e21)(2 + 4f12)(2 + 4e22)··· .
- (3) The initial subwords


γ1sgn(e1),γ12 sgn(e1),...,γ1e1,γ1e1γ2sgn(f1),...,γ1e1γ2f1,...,γ of the reduced word of γ have strictly increasing Frobenius norms.

Of course the column vectors of an element of PSL2(Z) are deﬁned only modulo multiplication by ±1, but that suﬃces for their norms to be well deﬁned. The bounds in part (2) are not sharp, but they will suﬃce for our purposes.

Ä

ä

d −c −b a

Proof. Note that conjugating by S maps ac db to

, which interchanges the column norms as well as the generators γ1 = T2 and γ2 = ST2S. Because of this symmetry, part (1) implies that the ﬁrst column of γ has strictly greater Euclidean norm than the second column if and only if γ’s reduced word ends in a nonzero power of γ2 = ST2S, and that only the identity element of Γ(2) has columns of the same Euclidean norm. We will prove these three statements together by induction on the total number of factors γ1ei or γ2fi in γ’s reduced word. The base case of powers γ1e1 and γ2f1 is straightforward. For the inductive step, by symmetry we reduce to the case where γ has the form

Ç

åÇ

å

Ç

å

a b c d

1 2e 0 1

a b + 2ea c d + 2ec

γ =

=

,

where ac db ∈ PSL2(Z) is not the identity element, e is a nonzero integer, and a2 + c2 > b2 + d2 by the inductive assumption. The Euclidean norm squared of

γ’s second column is h(e) := b2 + d2 + 4e2(a2 + c2) + 4e(ab + cd),

and we must show that h(e) > a2 + c2 when e = 0. Because h(e) is quadratic in e and h(0) < a2 + c2, it suﬃces to show that h(±1) > a2 + c2. Indeed,

h(±1) ≥ b2 + d2 + 4(a2 + c2) − 4 a2 + c2 b2 + d2 = 2 a2 + c2 − b2 + d2 2 > a2 + c2,

- as desired, where the ﬁrst inequality follows from the Cauchy-Schwarz inequality. This proves part (1).


The upper bound in part (2) follows from the submultiplicativity of the Frobenius norm. The lower bound follows from part (3), because there are |e1| + |f1| + |e2| + ··· initial subwords. Finally, part (3) follows from part (1) and the fact that h(e) increases for e ≥ 1 and decreases for e ≤ −1 (it is a quadratic function of e whose minimum occurs between e = −1 and e = 1).

We next introduce some representations of SL2(Z). First, we deﬁne the three-dimensional representation ρ3: SL2(Z) → GL3(Z) by the formula

- (3.8) ρ3

Ç

a b c d

å

=

Ñ

a2 2ab −b2 ac ad + bc −bd −c2 −2cd d2é

;

it is the restriction of a three-dimensional representation5 of SL2(R) to SL2(Z). We deﬁne ρ2: SL2(Z) → GL2(Z) by its action on the generators,

ρ2(T) = ρ2

Ç

1 1 0 1

å

=

Ç

−1 1 0 1

å

and ρ2(S) = ρ2

Ç

- 0 −1
- 1 0


å

=

Ç

0 −1 −1 0

å

;

its image is a dihedral group of order 6 and its kernel is Γ(2), so ρ2 is just a faithful representation of the dihedral group SL2(Z)/Γ(2). Finally, deﬁne the function  v: SL2(Z) → Z2 by  v(S) = (0,0) and  v(T) = (1,−1) (thought of as row vectors), and then in general by the cocycle formula

- (3.9)  v(γγ ) =  v(γ)ρ2(γ ) +  v(γ );

to check that this cocycle is well deﬁned, we can deﬁne it via (3.9) on the free group generated by S and T, and then check that it annihilates S2 and (ST)3, so that it factors though PSL2(Z). Then

ρ(γ) =

Ñ

ρ3(γ) 0 0 0 1  v(γ) 0 0 ρ2(γ)é

deﬁnes a six-dimensional representation of SL2(Z). Many of our later calculations use a conjugate σ of ρ deﬁned by

- (3.10) σ(γ) = gρσ−1ρ(γ)gρσ, where


Ö 1 0 1 −1 0 −1 1 0 0 −1 0 0 1 −1 0 −1 1 0 3 −1 −1 3 −1 −1

è

gρσ =

,

−2 0 2 −2 0 2 2 −2 0 2 −2 0

5There is a unique irreducible, continuous representation of SL2(R) of each ﬁnite dimension, up to isomorphism.

which is characterized by its values

è

Ö 0 1 0 0 0 0

Ñ0 0 0 1 0 0

é

−1 2 0 0 0 0 2 0 0 0 0 −1 0 0 0 0 1 0 0 0 0 −1 2 0 0 0 −1 2 0 0

- 0 0 1 0 0 0
- 0 1 0 0 0 0 1 0 0 0 0 0


σ(S) =

and σ(T) =

- 0 0 0 0 0 1
- 0 0 0 0 1 0


on the generators (2.3). See the paragraph after the proof of Proposition 3.9 for more discussion of the role of σ in this paper and its relationship with ρ.

The next result shows that the (integral) matrix entries of ρ(γ) and σ(γ) do not grow quickly in terms of those of γ.

Lemma 3.3. There exist absolute constants C,N > 0 such that each matrix entry of ρ

Ç

å

Ç

å

a b c d

a b c d

is bounded by C(a2 + b2 + c2 + d2)N in absolute value.

and of σ

The boundedness assertion in this lemma depends on the realization of the abstract group SL2(Z) in integer matrices. In particular, it implies that the restrictions of ρ or σ to free subgroups of SL2(Z) satisfy the same bound, a fact that is false for general representations of these subgroups. For example, the entries of σ(T)n grow only polynomially in n, while exponential growth can occur for other representations of the subgroup T .

Proof. The assertions for these two conjugate representations are equivalent. The representation ρ3 satisﬁes this boundedness condition by virtue of its explicit algebraic formula in (3.8), while ρ2 has a ﬁnite image. Thus it suﬃces to verify that  v(γ) with γ = ac db satisﬁes the claimed bound. Furthermore, formula

- (3.9) with γ ∈ Γ(2) and γ one of the six coset representatives for Γ(2) shows that it suﬃces to prove this last bound for γ ∈ Γ(2). Because Γ(2) is the kernel of ρ2, formula (3.9) restricted to Γ(2) shows that  v is a homomorphism from


Γ(2) to Z⊕Z. Writing γ as γ1e1γ2f1γ1e2 ··· as in the statement of Lemma 3.2, we see that the entries of  v(γ) are bounded in absolute value by a constant multiple

of |e1|+|f1|+|e2|+···, and the result follows from part (2) of Lemma 3.2.

3.3. The group algebra R = C[PSL2(Z)]. In constructing a solution to the identities (1.8)–(1.10), it is convenient to use the slash operator action of

- R = C[PSL2(Z)]. Then (1.8)–(1.10) state that


- (3.11) F + id/2F‹|τd/2S = eπiτ|x|2 and F|τd/2(T − I)2 = F‹|τd/2(T − I)2 = 0,


where I denotes the identity element while S and T are deﬁned by (2.3).

This subsection is devoted to studying some properties of R that are used later in the paper, in particular quotients of the translation action of PSL2(Z) on R. Recall that PSL2(Z) is the free product of the subgroups {I,S} and

{I,ST,STST}. If we write

x = S and y = ST,

then every element γ of Γ = PSL2(Z) = x,y | x2 = y3 = 1 has a unique reduced expression as a product w1w2 ···w , where = (γ) is the length of the product, each wj is either x, y, or y2, and the only allowable consecutive pairs wj and wj+1 are

(wj,wj+1) = (x,y), (x,y2), (y,x), or (y2,x).

We extend the notion of length to R = C[Γ] by deﬁning ( γ∈Γ cγγ) to be the maximum of all (γ) for which cγ = 0 (otherwise, (0) = −∞).

The order two element x = S acts by left multiplication on R, which can be diagonalized into ±1 eigenspaces using the decomposition

- (3.12) r =

I + S 2

r +

I − S 2

r for r ∈ R. In particular,

- (3.13) {r ∈ R : (S ± I)r = 0} = (S ∓ I)R. Similarly we obtain
- (3.14) {r ∈ R : (y − 1)r = 0} = (y2 + y + 1)R from the idempotent decomposition


r =

2

1 + e2πij/3y + e4πij/3y2 3

r

j=0

into three distinct eigenspaces for left multiplication by y.

The equation (T − I)v = w is a discretization of the derivative from singlevariable calculus, and it can be solved using a discretization of the integral as follows.

Lemma 3.4. Let w = γ∈Γ cγγ with cγ ∈ C. Then there exists a solution v ∈ R to

(T − I)v = (xy − 1)v = w if and only if n∈Z c(xy)nγ = 0 for all γ, in which case the unique solution in

- R is v = γ∈Γ dγγ with dγ = n>0 c(xy)nγ.


Proof. Suppose v = γ∈Γ dγγ. Then (xy−1)v = w means cγ = d(xy)−1γ −

dγ for all γ, and hence n∈Z c(xy)nγ = 0 via telescoping. Conversely, if n∈Z c(xy)nγ = 0 for all γ, then only ﬁnitely many of the numbers dγ := n>0 c(xy)nγ are nonzero, and they satisfy d(xy)−1γ − dγ = cγ, as desired. To

see that the solution is unique, note that (xy − 1)v = 0 implies dγ = d(xy)−1γ for all γ, which can happen only when v = 0 because the coeﬃcients have ﬁnite support.

Corollary 3.5. Suppose w = γ cγγ and there exists γ ∈ Γ such that c(xy)nγ = 0 for exactly one n ∈ Z. Then w ∈/ (T − I)R.

Lemma 3.6. The set of all v ∈ R for which there exist w ∈ R satisfying (T − I)v = (S + I)w is the right ideal (y2 − y + 1)(x + 1)R. In other words, {v ∈ R : (xy − 1)v ∈ (x + 1)R} = (y2 − y + 1)(x + 1)R.

Proof. Because xy−1 = (x+1)y−(y+1), we see that (xy−1)v ∈ (x+1)R if and only if (y+1)v ∈ (x+1)R. However, y+1 is invertible in the ring R, with multiplicative inverse (y2 −y +1)/2, because y3 = 1. Thus, (y +1)v ∈ (x+1)R is equivalent to v ∈ (y2 − y + 1)(x + 1)R, as desired.

Lemma 3.7. The set of all v ∈ R for which there exist w ∈ R satisfying

(T − I)v = (S − I)w is the right ideal (y2 + y + 1)R.

Proof. The identity (xy−1)(y2+y+1) = (x−1)(y2+y+1) shows that any element of that ideal provides a solution. Conversely, if (xy − 1)v = (x − 1)w, then multiplying by x shows that

(1 − x)w = (y − x)v = (y − 1)v − (x − 1)v and hence (y − 1)v ∈ (x − 1)R. We will show that (x − 1)R ∩ (y − 1)R = {0}, from which it follows that (y −1)v = 0 and thus v ∈ (y2 +y +1)R by (3.14), as needs to be shown. If (y − 1)v ∈ (x − 1)R, we may write yv − v = xu − u, for some u = γ cγγ for which cγ = 0 if γ’s reduced word begins with x (such γ can be replaced by −xγ, which does not start with x, because (x−1)(−x) = x−1). Multiplying both sides by y2 + y + 1 on the left annihilates (y − 1)v and yields y2xu + yxu = y2u + yu − xu + u. If u is nonzero, then the right side of this equation has length at most (u) + 1, while the left side has terms having length (u) + 2 which cannot cancel each other. Thus u = 0, proving that (x − I)R ∩ (y − I)R = {0}.

3.3.1. Some ideals of R = C[PSL2(Z)]. Deﬁne the right ideals I = (T − I)2 · R + S(T − I)2 · R,

- I+ = (S + I) · R + (T − I)2 · R,

- I− = (S − I) · R + (T − I)2 · R,

I+ = (T − 2I + T−1 − 2S) · R + (I − STS) · R, and

- I− = (T − 2I + T−1 + 2S) · R + (I + STS) · R




- (3.15)


of R. (We treat ±1 and ± synonymously in subscripts.) As mentioned at the end of Section 3.1, I consists of the elements of R whose action on the generating function F is determined by the functional equations from Theorem 3.1. The ideals I± play the same role when we decompose F into eigenfunctions for

- S (see also part (3) of Proposition 3.9), while the ideals I± are characterized by Proposition 3.11 and will be used to describe the residues of the kernels constructed in Theorem 4.3. Note in particular that I ⊆ I±, because S(T − I)2 = (S ± I)(T − I)2 ∓ (T − I)2, and I+ ∩ I− = I, because Sr ≡ ±r (mod I) for r ∈ I±, so r ≡ −r (mod I) for r ∈ I+ ∩ I−.


Proposition 3.8. The sums deﬁning the ideals I, I+, and I− are all direct sums (i.e., these ideals are free modules of rank 2 over R).

Proof. To deal with I, suppose that (T − I)2r = S(T − I)2r for some r,r ∈ R. Multiply both sides by S and combine to obtain the identity (I−εS)(T −I)2(r+εr ) = 0 for ε = ±1. By (3.13), this shows (T −I)2(r+εr ) ∈

- (S + εI)R. From this we see that the assertion for I follows from those for I±. First consider I+ and u,w ∈ R for which (T − I)2u = (S + I)w. By

Lemma 3.6, (T −I)u ∈ (y2 −y +1)(x+1)R, where x = S and y = ST as above. We will prove that there is no u for which (T − I)u is a nonzero member of this ideal, using Corollary 3.5. Suppose (T − I)u = (y2 − y + 1)(x + 1)r for some r ∈ R. Without loss of generality, we may assume r = r0 + yr1 + y2r2, where r0 ∈ C and the reduced words occurring in r1 or r2 all start with x or are the identity. (The nontrivial part of this assertion is that we can take r0 ∈ C, which holds because we can use the identity (x + 1)x = x + 1 to incorporate any other terms from r0 to C, r1, or r2.) Then (y2 − y + 1)(x + 1)r equals

y2x(r0 + yr1 + y2r2) − yx(r0 + yr1 + y2r2) + x(r0 + yr1 + y2r2)

+ y2(r0 + yr1 + y2r2) − y(r0 + yr1 + y2r2) + (r0 + yr1 + y2r2). Assume now that r1 and r2 are not both zero and that (r2) ≥ (r1), so that

((T − I)u) ≤ (r2) + 3. Choose γ ∈ PSL2(Z) occurring in r2 with (γ) = (r2). The group elements (xy)nyxy2γ = (y2x)−nyxy2γ have length 2n + 2 + (r2) (if n ≥ 1) or −2n + 3 + (r2) (if n ≤ 0), and so cannot occur in (T − I)u unless n = 0, when they occur in exactly one place, namely in −yxy2r2 (they do not occur in the three terms in the second line because those have length at most

(r2) + 1). Corollary 3.5 then proves there is no solution in this case. The same argument applies if (r1) > (r2): if γ occurs in r1 with (γ) = (r1), then the group elements (xy)nyxyγ occur only in −yxyr1 and with n = 0. Thus r1 = r2 = 0, and unless r0 = 0 we may renormalize to set r0 = 1 and obtain

- (T −I)u = y2x−yx+x+y2 −y +1. Now yx is the only term in this expression of the form (xy)nyx, and we again obtain a contradiction from Corollary 3.5.


The case of I− is slightly simpler: here (T − I)2u = (S − I)w implies (T − I)u ∈ (y2 + y + 1)R by Lemma 3.7. Suppose (T − I)u = (y2 + y + 1)r with r ∈ R. This time there is no loss in generality in assuming r = r0 + xr1, where r0 ∈ C and r1 does not begin with x, because y2 + y + 1 annihilates both y − 1 and y2 − 1. Now

(y2 + y + 1)r = r0y2 + r0y + r0 + y2xr1 + yxr1 + xr1.

The terms occurring in (xy)nyxr1 occur in this expression only if n = 0, and thus Corollary 3.5 applies unless possibly r1 = 0. If r1 = 0, then the term (xy)ny occurs only for n = 0, and so we conclude that (T − I)u = 0, as desired.

Proposition 3.9. The ideals I, I+, and I− of R have the following properties:

- (1) dimC R/I = 6 and

(3.16) M1 = I, M2 = T, M3 = TS, M4 = S, M5 = ST, M6 = STS are a basis of R/I,

- (2) dimC R/I± = 3 and I,T,TS are a basis of R/I±, and
- (3) Iε = {r ∈ R : (S − εI)r ∈ I} for ε = ±1.


Proof. Consider the six-dimensional representation σ of PSL2(Z) deﬁned in (3.10). By linearity σ further extends to an algebra homomorphism from

- R = C[PSL2(Z)] to C6×6, whose ﬁrst row vanishes on I because the ﬁrst rows of both σ(S(T − I)2) and σ((T − I)2) vanish.


We begin by proving that M1,...,M6 span R/I. If M denotes the column vector (M1,...,M6) ∈ R6, then the calculations

- (3.17)

- M · S =

Ñ S

TS T I STS ST

é

= σ(S) M and

- M · T =


Ñ T

T2 TST ST ST2 STST

é

= Ü T

−I+2T+(T−I)2 2−STS+S(T−I)2T−1S ST 2ST−S+S(T−I)2 2S−TS+(T−I)2T−1S

ê

= σ(T) M + (T − I)2 ·

Ñ 0 I 0 0 0 T−1S

é

+ S(T − I)2 ·

Ñ 0

0 T−1S 0 I 0

é

show that

- (3.18) M · γ ∈ σ(γ) M + I6 for every γ ∈ PSL2(Z), because we inductively obtain


M · γγ ∈ σ(γ) M + I6 · γ ∈ σ(γ)σ(γ ) M + I6.

(In fact, (3.18) is the motivation for our deﬁnition of σ.) It follows that γ, which is the ﬁrst entry of M · γ, is a linear combination of M1,...,M6 plus an element of I.

To show that M1,...,M6 are linearly independent in R/I, we begin by checking that σ(Mi) has ﬁrst row entries that are all 0 except for a 1 in the i-th position. Because the ﬁrst row of σ(r) vanishes for all r ∈ I, no nontrivial linear combination of M1,...,M6 can lie in I, which completes the proof of part (1). (Note also that examining the ﬁrst row of σ gives a convenient algorithm for reducing elements of PSL2(Z) modulo I.)

Next we prove part (2). First, we observe that left multiplication by

- S preserves each of I and I±; for I this preservation follows immediately from the deﬁnition of I, and for I± it follows from the calculations in the paragraph containing (3.15). Because I, T, TS, S, ST, and STS span R/I, and S acts on the left by ∓1 modulo I±, we see that I, T, and TS span R/I±. Now let π: R → (R/I+) ⊕ (R/I−) be the direct sum of the projections modulo these ideals. Because I+ ∩ I− = I, the kernel of π is I, and thus


- R/I maps injectively to (R/I+) ⊕ (R/I−). We have seen that R/I± are both


- at most three-dimensional, while R/I is six-dimensional by part (1). Thus,


dimC R/I± = 3, and I, T, and TS form a basis.

All that remains is to prove part (3). Since (S − εI)(S + εI) = 0 and (S − εI)(T − I)2r = S(T − I)2r + (T − I)2(−εr) lies in I for all r ∈ R, it is clear that left multiplication by S − εI maps Iε to I. To show the reverse inclusion, suppose that

(S − εI)r = (T − I)2r1 + S(T − I)2r2 ∈ I for some r,r1,r2 ∈ R, and hence after multiplying both sides by S,

−ε(S − εI)r = (T − I)2r2 + S(T − I)2r1. Combining, we see that 2(S − εI)r = (S − εI)(T − I)2(r2 − εr1) and hence

- (S−εI) 2r−(T−I)2(r2−εr1) = 0. By (3.13), 2r−(T−I)2(r2−εr1) ∈ (S+εI)R, which implies r ∈ Iε.


Note that (3.18) gives us a natural interpretation of σ in terms of the right action of PSL2(Z) on the six-dimensional vector space R/I. From this perspective, the conjugacy between σ and ρ in Section 3.2 means R/I must decompose into the direct sum of two three-dimensional right R-modules. These submodules are the subspaces I±/I of R/I, which are spanned by I ±S, (I ± S)T, and (I ± S)TS. Here, I−/I corresponds to ρ3, while I+/I has a two-dimensional submodule corresponding to ρ2, namely (I+ ∩ Iaug)/I, where Iaug is the augmentation ideal of R. (Recall that the augmentation ideal is the two-sided ideal generated by γ − I with γ ∈ PSL2(Z). It follows immediately from the deﬁnitions of I± that I− ⊆ Iaug, while I+  ⊆ Iaug.) Choosing a basis

compatible with the above structure led us to the representation ρ and the intertwining operator gρσ introduced in Section 3.2. Note that the reason why I+/I has a two-dimensional submodule rather than a two-dimensional quotient is that σ is a left representation, while we have a right action of R on R/I. This discrepancy is unfortunate, but avoiding it would require breaking convention by either using right representations or replacing the slash operator with a left action.

Since I = (T − I)2 · R + S(T − I)2 · R is free as a right R-module, for each r ∈ R there exist unique column vectors N1(r), N2(r) ∈ R6 such that

- (3.19) M · r = σ(r) M + (T − I)2 · N1(r) + S(T − I)2 · N2(r). It follows that
- (3.20) Ni(r1r2) = σ(r1) Ni(r2) + Ni(r1) · r2


for i = 1,2 and r1,r2 ∈ R, with the cocycle relation (3.20) describing the composition law for multiple applications of (3.19). Repeated applications of

- (3.20) result in the more general formula Ni(r1r2 ···rn) = σ(r1 ···rn−1) Ni(rn)

- + σ(r1 ···rn−2) Ni(rn−1) · rn
- + σ(r1 ···rn−3) Ni(rn−2) · rn−1rn


+ ··· + Ni(r1) · r2 ···rn

- (3.21)


for more than two factors.

Lemma 3.10. There exist positive constants C and N such that for all γ ∈ PSL2(Z), the entries of Ni(γ) have the form δ∈PSL

2(Z) nδδ, with δ |nδ| ≤ C γ NFrob and δ Frob ≤ C γ Frob whenever nδ = 0.

Proof. Formula (3.20) reduces the claim to γ ∈ Γ(2), as can be seen by taking r2 ∈ Γ(2) and r1 one of the six coset representatives of Γ(2). Lemma 3.3 shows the existence of constants C0,N0 > 0 such that the matrix entries of σ(γ) are bounded by C0 γ NFrob0 in absolute value. Factor γ = γ1e1γ2f1γ1e2 ···, with γ1 = T2 and γ2 = ST2S as in Lemma 3.2, and reﬁne the factorization to γ = r1 ...rn with ri ∈ {γ1±1,γ2±1} and n = |e1| + |f1| + |e2| + ··· ≤ γ 2Frob by part (2) of Lemma 3.2. By part (3) of Lemma 3.2, r1r2 ···ri Frob is an increasing function of i, while riri+1 ···rn Frob is decreasing. Then (3.21) expresses Ni(γ) as a combination of n terms, each of which satisﬁes the asserted bounds.

Like all group rings, R is equipped with the anti-involution ι that sends γ cγγ to γ cγγ−1.

Proposition 3.11. Deﬁne linear functionals φ±: R/I± → C on the basis vectors from Proposition 3.9 by setting

- (3.22) φ±(I) = 0, φ±(T) = 1, and φ±(TS) = 0. Then


I± = {r ∈ R : φ±(r · ι(r)) = 0 for all r ∈ R}, and I,S,T are a basis of R/ I±.

The motivation for the maps φ± is that they describe the residues in part (3) of Theorem 4.3, and therefore they play a key role in the contour shifts in Section 5.

Proof. Let ε = ±1, let r1 = T − 2I + T−1 − 2εS and r2 = I − εSTS = I − εT−1ST−1 be the generators of Iε from its deﬁnition (3.15), and let

Jε = {r ∈ R : φε(r · ι(r)) = 0 for all r ∈ R}, which we will show equals Iε.

To prove that Iε ⊆ Jε, note ﬁrst that Jε is a right ideal. It will therefore suﬃce to show that φε annihilates ι(ri), Tι(ri), and TSι(ri) for i = 1,2, because I, T, and TS span R/Iε by part (2) of Proposition 3.9. We check in succession that

φε(S) = −εφε(I) = 0, φε(ST) = −εφε(T) = −ε, φε T2 = φε(2T − I) = 2φε(T) = 2,

φε T−1 = φε(2I − T) = −φε(T) = −1, φε T−1S = φε((2I − T)S) = 0,

φε(TST) = φε ST−1S = −εφε T−1S = 0, φε ST−1 = −εφε T−1 = ε,

φε T−1ST−1 = φε(STS) = −εφε(TS) = 0, φε TST−1 = φε 2I − T−1 ST−1 = 2ε, and φε T2ST = φε((2T − I)ST) = ε.

It is then straightforward to verify by direct calculation than φε evaluates to zero on ι(ri), Tι(ri), and TSι(ri), because ι(r1) = r1 and ι(r2) = I −εST−1S = I − εTST. Thus, Iε ⊆ Jε.

To complete the proof, we will show that dim(R/ Iε) ≤ dim(R/Jε). We ﬁrst note that the map ψ: R → HomC(R/Iε,C) taking r to r  → φε(r · ι(r)) has kernel Jε by deﬁnition and is surjective, because the linear functionals ψ(I),

ψ(S), and ψ(T) satisfy ψ(I)(I) = 0, ψ(I)(T) = 1, ψ(I)(TS) = 0,

- ψ(S)(I) = 0, ψ(S)(T) = 0, ψ(S)(TS) = 1,
- ψ(T)(I) = −1, ψ(T)(T) = 0, ψ(T)(TS) = 2ε


and hence span the three-dimensional space of linear functionals. Therefore

- R/Jε is a three-dimensional vector space, and it suﬃces to show that I, S, and


- T span R/ Iε. To prove that I, S, and T span R/ Iε, we begin by reducing ST, ST−1,


TS, T−1, and T2 to linear combinations of I, S, and T modulo Iε via ST = εS − εr2S

≡ εS (mod Iε), ST−1 = εS + r2ST−1

≡ εS (mod Iε), TS = 2εI + 2S − T−1S + r1S ≡ 2εI + 2S − T−1S (mod Iε)

= 2εI + 2S − εT + εr2T ≡ 2εI + 2S − εT (mod Iε),

T−1 = εTS − εr2TS ≡ εTS ≡ 2I + 2εS − T (mod Iε), and

T2 = 2T − I + 2εST + r1T ≡ 2T − I + 2εST (mod Iε) ≡ 2T − I + 2S (mod Iε).

Using these relations, we can reduce any γ ∈ Γ (and therefore any r ∈ R) to a linear combination of I, S, and T modulo Iε, by starting from the left of the reduced word representing γ.

### 4. Solutions of functional equations and modular form kernels

4.1. The action of R on holomorphic functions and integral kernels. We begin by recalling a commonly used class of functions on the upper half-plane

- H, which appears in the literature dating at least as far back as 1974 in work of Knopp [31]: those satisfying a bound of the form


- (4.1) |F(τ)| ≤ α Im(τ)−β + |τ|γ


for some α,β,γ ≥ 0. Such a bound has already appeared in part (3) of Theorem 3.1, and it is satisﬁed by any power series in eπiτ whose coeﬃcients

grow more slowly than some polynomial (e.g., the classical modular forms Ek and theta functions from Section 2.1). Conversely, the boundedness condition in the deﬁnition of modular form is automatic for functions satisfying (4.1).

Recall also that a function F has moderate growth on the symmetric space H if

- (4.2) |F(g · i)| ≤ C g N for some C,N ≥ 0, where g · i = aici++db denotes the action of g = ac db ∈ SL2(R) on i ∈ H (with i2 = −1) and  ·  is some ﬁxed matrix norm on SL2(R), such as the Frobenius norm. This notion is independent of the choice of matrix norm.

In fact, moderate growth is equivalent to (4.1). First, note that the notion of moderate growth does not depend on the choice of g: if g · i = g · i with g,g ∈ SL2(R), then g−1g ∈ SO2(R) and hence g Frob = g Frob. Now to see the equivalence between the two bounds, write τ = x + iy and let gτ = y−1/2 (y0 x1 ). Then gτ · i = τ and

gτ 2Frob = y−1 + y−1(x2 + y2) ≤ y−1 + y−2 + (x2 + y2)2 /2

= O y−2 + (x2 + y2)2 . Thus, moderate growth implies (4.1). For the other direction, we must bound y−1 and x2 + y2 by polynomials in gτ 2Frob. To do so, we note that

y−1 ≤

1 + x2 + y2 y

= gτ 2Frob and y2 ≤

Å

1 + x2 + y2 y

ã2

= gτ 4Frob, and hence

x2 + y2 = y

x2 + y2 y ≤

- 1

- 2


Å

y2 +

(x2 + y2)2 y2

ã

≤ gτ 4Frob,

- as desired. When S is a subset of H, we accordingly use the term moderate growth on


S to describe functions satisfying the bound (4.1) for τ ∈ S. Following Knopp’s notation, let

- (4.3) P = {F : H → C : F is holomorphic and satisﬁes (4.1) for all τ ∈ H}


denote the space of holomorphic functions having moderate growth on the full upper half-plane. In terms of the unit disk model of the hyperbolic plane, P corresponds to holomorphic functions on {z ∈ C : |z| < 1} that are bounded in absolute value by C(1 − |z|)−N for some constants C,N ≥ 0.

Lemma 4.1. Let F be a holomorphic function on H, and S ⊆ H. If |F(g · i)| ≤ C g NFrob

for all g ∈ SL2(R) such that g · i ∈ S, then

|(F|kγ)(g · i)| ≤ C γ NFrob+|k| g NFrob+2|k| for all γ,g ∈ SL2(R) such that g · i ∈ γ−1S.

In particular, P is preserved by the slash operation (2.1). It is consequently a representation space for SL2(Z), and for PSL2(Z) and thus R = C[PSL2(Z)] when k is even (so that ±γ act the same for γ ∈ SL2(Z); see [8, Section 1.1.6]).

Proof. The factor of automorphy j(g,z) = cz + d for a matrix g = ac db ∈ SL2(R) and point z ∈ H satisﬁes the bounds g −Frob1 ≤ |j(g,i)| ≤ g Frob. The upper bound is trivial, while the lower bound follows from g 2Frob > a2 + b2 ≥ (c2 + d2)−1, where the last inequality (a2 + b2)(c2 + d2) ≥ 1 = (ad − bc)2 is itself a consequence of the Cauchy-Schwarz inequality. Note that the same inequality also shows that g Frob ≥

√2. Let gτ be some element of SL2(R) for which gτ · i = τ. The identity j(g1g2,z) = j(g1,g2z)j(g2,z) shows that j(γ,τ) = j(γgτ,i)/j(gτ,i), and thus

- (4.4) |j(γ,τ)|,|j(γ,τ)|−1 ≤ gτ Frob γgτ Frob ≤ γ Frob gτ 2Frob for all γ ∈ SL2(R) and τ ∈ H. Now the desired bound follows from the deﬁnition

(F|kγ)(z) = j(γ,z)−kF(γ · z) of the slash operation.

We now algebraically reformulate the system (3.11) in terms of this action on P. For simplicity we assume d is a multiple of 4, so that PSL2(Z) can act with weight d/2. Then if we let F‹ = i−d/2(eπiτ|x|2 − F)|τd/2S, system (3.11) becomes

- (4.5) F|τd/2(T − I)2 = 0 and F|τd/2S(T − I)2 = eπiτ|x|2|τd/2S(T − I)2.

Since I = (T −I)2 ·R+S(T −I)2 ·R, these equations govern the slash operator action of I on F in the τ variable. After we solve for F in this section, bounds on F (e.g., to show membership in P) will be shown in Section 5. Let

- (4.6) D =

ß

z ∈ H : Re(z) ∈ (−1,1), z −

1 2

>

- 1

- 2


, z +

- 1

- 2


> and ™

- 1

- 2


- (4.7) F = {z ∈ H : Re(z) ∈ (0,1), |z| > 1, |z − 1| > 1}

be the fundamental domains for Γ(2) and SL2(Z), respectively, which are shown in Figure 4.1 and satisfy

- (4.8) D = F ∪ T−1F ∪ STSF ∪ SF ∪ ST−1F ∪ TSF.


The following proposition shows that functions with symmetry properties generalizing (4.5) are determined by their behavior on the closure D of D in H.

T−1τ = τ − 1 τ

T−2D T2D

Sτ = −τ1 TSτ = τ−τ 1 STSτ = 1−ττ ST−1τ = 1−1τ

ST2SD ST−2SD

−1 0 1

Figure 4.1. The fundamental domain D for Γ(2) deﬁned in (4.6) is shaded, with the fundamental domain F for SL2(Z) deﬁned in (4.7) shaded darker (note that F ⊆ D). The six marked points in the interior of D are the images of a point τ ∈ F.

Proposition 4.2. Let k be an even integer, and let h1,h2: H → C be continuous functions. Then the following hold:

(1) (Analytic continuation) Suppose h1 and h2 are holomorphic. Let O ⊆ H denote an open neighborhood of D, and let f : O → C be a holomorphic function satisfying the transformation laws

- (4.9) f|k(T − I)2 = h1 and f|kS(T − I)2 = h2

whenever both sides are deﬁned (that is, on O ∩ T−1O ∩ T−2O for the ﬁrst equation, and on SO ∩ T−1SO ∩ T−2SO for the second equation). Then f extends to a holomorphic function on H satisfying (4.9).

(2) (Propagation of the moderate growth bound) Suppose f : H → C is a continuous function that satisﬁes the transformation laws (4.9) on H and grows moderately on D; i.e., there exist nonnegative constants Cf and Nf such that

- (4.10) |f(g · i)| ≤ Cf g NFrobf


for g · i ∈ D (see (4.2)). Suppose also that h1 and h2 have moderate growth, and let Ch1, Ch2, Nh1, and Nh2 be nonnegative constants such

that

- (4.11) |h1(g · i)| ≤ Ch1 g NFrobh1 and |h2(g · i)| ≤ Ch2 g NFrobh2 for g ∈ SL2(R). Then f has the following moderate growth bound on all

of H: for some constants C,N ≥ 0 depending only on Nf, Nh1, Nh2, and k,

- (4.12) |f(g · i)| ≤ C(Cf + Ch1 + Ch2) g NFrob

for g ∈ SL2(R). In particular, if f, h1, and h2 are all holomorphic, then f ∈ P.

The fact that the bound (4.12) depends linearly on Cf, Ch1, and Ch2 will be used to obtain uniform moderate growth bounds in Section 5.

Proof. For expositional reasons we begin with the proof of part (2). When we refer to a “constant” in this proof, we mean that it can depend only on Nf, Nh1, Nh2, and k, and not on Cf, Ch1, or Ch2. By increasing the exponents if necessary, we may assume Nh1 = Nh2 = Nf. Since f is continuous the moderate growth bound (4.10) holds over the closure D. Recall the matrices Mi ∈ SL2(Z) from (3.16):

(M1,M2,M3,M4,M5,M6) = (I,T,TS,S,ST,STS).

It follows from the assumptions and (4.8) that (4.10) holds on M1F = F, M3F = TSF, M4F = SF, and M6F = STSF (i.e., whenever g · i is in these sets). Our ﬁrst step is to check such an inequality on M2F = TF and M5F = STF.

We can analyze the growth of f on TF as follows, using f’s moderate growth on F ∪ T−1F ⊆ D and the functional equations (4.9). By Lemma 4.1, the moderate growth of f on T−1F implies that f|kT−1 has moderate growth on F, with suitably adjusted constants as in the lemma, and the moderate growth of h1 from (4.11) implies that h1|kT−1 also has moderate growth. Now we write f|kT = f|k 2I − T−1 + h1|kT−1 by (4.9), to deduce that f|kT has moderate growth on F; hence f has moderate growth on TF by Lemma 4.1 again. Written out more explicitly, |f(g · i)| ≤ (c1Cf + c2Ch1) g NFrobf+4|k| on M2F = TF, for some constants c1,c2 > 0. Likewise, the moderate growth on SF and ST−1F implies a bound of the form |f(g·i)| ≤ (c 1Cf +c 2Ch2) g NFrobf+4|k| on M5F = (ST2)T−1F = STF, for some constants c 1,c 2 > 0. Thus, by Lemma 4.1, there exist constants C1,N1 ≥ 0 such that

- (4.13) |(f|kMj)(g · i)| ≤ C1(Cf + Ch1 + Ch2) g NFrob1 for g · i ∈ F and each j ≤ 6.


For τ ∈ H choose γ = ac db ∈ SL2(Z) such that w := γ−1·τ ∈ F. Consider

- (3.19) with r = γ, so that γ = I · γ is the ﬁrst entry of σ(γ) M + (T − I)2 ·


N1(γ)+S(T −I)2 · N2(γ). We next bound (f|kγ)(w) by expanding it according to this last decomposition. Write the matrix entries of σ(γ) as σ(γ)ij, and the ﬁrst vector entries of N1(γ) and N2(γ) as δ∈PSL

2(Z) n δδ, respectively (bounds on these quantities are given in Lemmas 3.3 and 3.10). Let gτ and gw = γ−1gτ be matrices in SL2(R) which map i to τ and w, respectively. Then

2(Z) nδδ and δ∈PSL

(cw + d)−kf(τ) = (f|kγ)(gw · i)

σ(γ)1j(f|kMj)(gw · i)

=

- (4.14)


j≤6

nδ(h1|kδ)(gw · i) + n δ(h2|kδ)(gw · i) .

+

δ∈PSL2(Z)

Invoking (4.10) and (4.11), along with Lemma 4.1 and (4.13), yields the bound

|(cw + d)−kf(τ)| ≤ C2(Cf + Ch1 + Ch2)

|σ(γ)1j| gw NFrob2

j≤6

+

δ

(|nδ| + |n δ|) δ NFrob2 gw NFrob2

for some constants C2,N2 ≥ 0. The estimates from Lemmas 3.3 and 3.10 show that the sums are at most C3 γ NFrob3 gw NFrob3 for some constants C3,N3 ≥ 0. The factor of automorphy cw + d = j(γ,w) has a bound of the same form in (4.4), and thus

|f(τ)| ≤ C4(Cf + Ch1 + Ch2) γ NFrob4 gw NFrob4 for some constants C4,N4 ≥ 0.

We now claim that for z in the standard “keyhole” fundamental domain {z ∈ H : |z| ≥ 1,−12 ≤ Re(z) ≤ 12},

- (4.15) gz Frob ≤ δgz Frob


for all δ ∈ SL2(Z), where gz is some matrix in SL2(R) with gz · i = z (this deﬁnes gz uniquely up to right multiplication by an element of SO2(R), so the quantities on both sides of inequality are independent of such a choice). Indeed, writing z = x + iy and δ = (pr qs ), we may take gz = y−1/2 (y0 x1 ), compute the norms squared, and reduce the claim to showing that

(x2 + y2 − 1)(p2 + r2 − 1) + p2 + q2 + r2 + s2 + 2x(pq + rs) − 2 ≥ 0

for all δ ∈ SL2(Z). Using the deﬁning inequalities on z, the expression on the left is at least p2 − |pq| + q2 + r2 − |rs| + s2 − 2, which is nonnegative because the rows of δ are nonzero and the integral quadratic form m2 − mn + n2 takes positive integer values on integer pairs (m,n) = (0,0).

Half of the fundamental domain F lies in the keyhole fundamental domain, while the other half lies in its translate by T. Therefore (4.15) and the submultiplicativity of the Frobenius norm imply that there exists a positive constant C such that

gw Frob ≤ C δgw Frob for all δ ∈ SL2(Z). (Speciﬁcally, if w is not in the keyhole fundamental domain, then gw = Tgz with z in it. In that case δgw Frob = δTgz Frob ≥ gz Frob ≥

T −Frob1 gw Frob, so we can take C = T Frob = √3.) Now we can use the inequality

γ Frob ≤ gτ Frob gw−1 Frob = gτ Frob gw Frob ≤ C gτ 2Frob

(the second step using the fact gw Frob = gw−1 Frob for gw ∈ SL2(R)) to deduce that

|f(τ)| ≤ C4(Cf + Ch1 + Ch2) γ NFrob4 gw NFrob4

≤ C4(Cf + Ch1 + Ch2)(C )N4 gτ 3FrobN4 , which completes the proof of part (2).

We now turn to the proof of part (1), which shares similar ingredients but instead works with a diﬀerent basis for R/I, namely the entries of the column vector

M = (M 1,M 2,M 3,M 4,M 5,M 6) = (I,T−1,STS,S,ST−1,TS) coming from (4.8) (i.e., specifying the translates of F that tile D). Checking that M consists of a basis amounts to observing that T−1 ≡ 2I − T (mod I) and ST−1 ≡ 2S − ST (mod I).

As was the case in (3.19), there exist a representation σ : PSL2(Z) → GL6(Z) and maps N i : PSL2(Z) → R6 such that

- (4.16) M · γ = σ (γ) M + (T − I)2 · N 1(γ) + S(T − I)2 · N 2(γ)


for all γ ∈ PSL2(Z), and such that these maps satisfy the analogous cocycle relation to (3.20). In particular, M is an integral change of basis from M modulo I6, and thus σ is the corresponding conjugate of σ.

By shrinking O if necessary, we assume that its only Γ(2)-translates which intersect it are T2O, T−2O, ST2SO, and ST−2SO (coming from the boundaries of D). There exists an open neighborhood OF of F such that j≤6 M jOF ⊆ O; in particular, f|kM j is deﬁned on OF for each j ≤ 6. By shrinking OF if necessary, we may assume that γOF intersects OF with γ ∈ PSL2(Z) only when γF and F share a boundary point. Accordingly, let

Ω = {ω ∈ PSL2(Z) : ωOF ∩ OF = ∅}

= {S,T,T−1,ST−1,TS,TST−1}.

Consider a pair τ,τ ∈ OF such that τ = ωτ for some ω ∈ Ω. We claim for each i ≤ 6 that

- (4.17)

(f|kM iω)(τ) =

j≤6

σ ij(ω)(f|kM j)(τ)

+ (h1|kN 1i(ω))(τ) + (h2|kN 2i(ω))(τ),

where σ ij(ω) denote the matrix entries of σ (ω), and N 1i(ω) and N 2i(ω) denote the vector entries of N 1(ω) and N 2(ω), respectively. This claim would follow immediately from (4.16) if we knew we could apply the functional equations (4.9), and so all we must do is to verify the hypotheses of (4.9), namely that γτ ∈ O ∩ T−1O ∩ T−2O for every term γ that occurs in N 1i(ω), and γτ ∈ SO ∩ T−1SO ∩ T−2SO for every term γ in N 2i(ω). To begin, we write (4.16) as

- (4.18) M iω − j≤6


σ ij(ω)M j = (T − I)2N 1i(ω) + S(T − I)2N 2i(ω).

Similarly to (3.17), it is straightforward to check for each possible choice of i and ω that either N 1i(ω) = N 2i(ω) = 0, in which case the hypotheses of (4.9) hold vacuously and (4.17) follows, or one of N 1i(ω) and N 2i(ω) is zero and the other is a group element γ ∈ PSL2(Z). In other words, the right side of

- (4.18) is of the form (T − I)2γ or S(T − I)2γ with γ ∈ PSL2(Z) whenever is it


nonzero. Since M iωτ = M iτ ∈ O and M jτ ∈ O for all i and j, all the terms on the left side of (4.18) map τ to points in O; therefore τ is mapped to O by all of T2γ,Tγ,γ or ST2γ,STγ,Sγ (depending on which form the right side has). This assertion is the hypothesis needed for (4.9) to apply at the point γτ, and (4.17) follows by applying the slash operator to f.

Having shown (4.17), we now extend f to arbitrary w ∈ H by imitating

- (4.14) (but with slightly diﬀerent notation). Namely, we write w as γτ with τ ∈ OF and γ ∈ PSL2(Z), and we deﬁne f(w) by


j(γ,τ)−kf(w) = (f|kγ)(τ)

σ 1j(γ)(f|kM j)(τ) + (h1|kN 11(γ))(τ) + (h2|kN 21(γ))(τ),

=

j≤6

where as usual j(γ,τ) is the factor of automorphy from (2.2). That f(w) is well deﬁned follows from (4.17) and the cocycle relation for σ , N 1, and N 2 analogous to (3.20). Speciﬁcally, suppose that w = γτ = γ τ , with τ,τ ∈ OF

and γ,γ ∈ PSL2(Z). Then τ = ωτ for some ω ∈ Ω, and hence γ = γ ω. Starting with the deﬁnition of j(γ,τ)−kf(w) given above, we expand the right

#### side using σ (γ) = σ (γ )σ (ω) and the cocycle relations to obtain

Ñ

é

σ ij(ω)(f|kM j)(τ) + (h1|kN 1i(ω))(τ) + (h2|kN 2i(ω))(τ)

σ 1i(γ )

j≤6

i≤6

+ (h1|kN 11(γ )ω)(τ) + (h2|kN 21(γ )ω)(τ).

Applying (4.17) to the expression in parentheses shows that j(γ,τ)−kf(w) equals

σ 1i(γ )(f|kM iω)(τ) + (h1|kN 11(γ )ω)(τ) + (h2|kN 21(γ )ω)(τ),

i≤6

or equivalently

j(ω,τ)−k

i

σ 1i(γ )(f|kM i) + (h1|kN 1i(γ )) + (h2|kN 2i(γ )) (ωτ)

by the deﬁnition of the slash operator |kω. Finally, using ωτ = τ and j(γ,τ) = j(γ ,τ )j(ω,τ) yields j(γ ,τ )−kf(w) =

σ 1i(γ )(f|kM i)(τ )+(h1|kN 1i(γ ))(τ )+(h2|kN 2i(γ ))(τ ),

i

which is the deﬁnition of f(w) as we would obtain by using τ and γ . Therefore f(w) is well deﬁned.

We have now deﬁned a holomorphic function on H agreeing with f on the

open neighborhood i≤6 M jOF of D (and thus also the original neighborhood O). Since the holomorphic identity (4.9) holds for the original function, it must

hold for the extension as well.

Equation (4.5) recasts the interpolation formula (1.4) from Theorem 1.7 in terms of properties of the function F : H × Rd → R. To construct F, we make the Ansatz that F‹|τd/2S can (essentially) be written as a Laplace transform, which is equivalent to a contour integral construction introduced by Viazovska in her work on sphere packing [53] and motivated by cycle integrals of modular forms appearing in [19]. Speciﬁcally, we will construct an integral kernel K on H × H such that

∞

- (4.19) F(τ,x) = eπiτ|x|2 + 4sin π|x|2/2 2


K(τ,it)e−π|x|2t dt,

0

- at least for |x| suﬃciently large and τ inside the fundamental domain F for


the action of SL2(Z) on H deﬁned in (4.7). Such a formula requires initially restricting τ, because the kernel K(τ,z) will have poles; see part (1) of Theorem 4.3. This is the reason we have taken the fundamental domain F to be diﬀerent from the usual keyhole fundamental domain for SL2(Z)\H, so that in particular F does not intersect the imaginary axis z = it.

It is natural here to decompose the proposed kernel into eigenfunctions of |τd/2S as K = 21(K+ + K−) using (3.12), where

- (4.20) K±(τ,z) := K(τ,z) |τd/2 (I ∓ S).


Note that K± has eigenvalue ∓1 under |τd/2S, not ±1. However, the notation is consistent with our use of signs elsewhere, such as in part (2) of the next theorem.

This labeling reﬂects the fact that K± contributes to the decomposition of F into eigenfunctions of the Fourier transform with eigenvalue ±1. In terms of

the relationship F‹ = (eπiτ|x|2 − F)|τd/2S between F‹ and F when d is a multiple of 8, the right side contains −F|τd/2S, which introduces an extra minus sign.

The next result, which is proved in Section 4.4, shows the existence of a kernel K that will be used to construct the solution F of the functional equations (4.5) via (4.19) and later extensions of this formula.

Theorem 4.3. For dimensions d = 8 and 24 there exist unique meromor-

phic functions K = K(d) and K± = K±(d) for d = 8 and 24 (related by (4.20)) on H × H satisfying the following properties.

- (1) For ﬁxed z ∈ H the poles of K(τ,z) and K±(τ,z) as functions of τ are all simple and contained in the SL2(Z)-orbit of z.
- (2) The kernel K satisﬁes the functional equations K(τ,z) |τd/2 (T − I)2 = 0 and K(τ,z) |τd/2 S(T − I)2 = 0;

that is, K|τd/2r = 0 for all r ∈ I. Also, K+ and K− satisfy the functional equations

K±(τ,z) |τd/2 (T − I)2 = 0 and K±(τ,z) |τd/2 (S ± I) = 0; that is, K±|τd/2r = 0 for all r ∈ I±.

- (3) For z ∈ H and r ∈ R, the residues of K and K± as functions of τ satisfy


- 1

- 2π


Resτ=z K|τd/2r = −

φ(r) and

- 1

- 2π


Resτ=z K±|τd/2r = −

φ±(r),

where φ: R/I → C is the linear map deﬁned by φ(I) = 0, φ(T) = 1, φ(TS) = 0, φ(S) = 0, φ(ST) = 0, φ(STS) = 0

and φ±: R/I± → C is the linear map from (3.22) deﬁned by φ±(I) = 0, φ±(T) = 1, φ±(TS) = 0.

(Note that φ and φ± are deﬁned modulo I and I± thanks to part (2) above, so it suﬃces to deﬁne them on the bases from Proposition 3.9.)

- (4) The functions


∆(τ)∆(z)(j(τ) − j(z))K±(8)(τ,z) and

∆(τ)∆(z)2(j(τ) − j(z))K±(24)(τ,z) are in the class P both as functions of τ and z. Furthermore, for z ﬁxed the kernels satisfy the bounds

- (4.21) K±(8)(τ,z) = O |τe2πiτ| and K±(24)(τ,z) = O |τe4πiτ| as Im(τ) → ∞.

It is not diﬃcult to check that the functional equations for K± in part (2) are equivalent to those for K, and the same is true for the residue calculations in part (3). We have stated both cases for completeness.

Our ﬁrst step in proving Theorem 4.3 is to solve the functional equations satisﬁed by K±. Part (2) of the theorem asserts that K±(τ,z) |τd/2 r = 0 for all r ∈ I±, and we will see in Proposition 4.10 that K±(τ,z) |z2−d/2 r = 0 for all r ∈ I±. Furthermore, part (4) reduces the problem to the case of functions in P, with the factors of ∆(τ) and ∆(z) changing the weights of the actions in τ and z.

4.2. Functions in P annihilated by I± and I±. Given a right ideal J of R = C[PSL2(Z)] and an even integer k, let

Annk(J,P) = {f ∈ P : f|kr = 0 for all r ∈ J}.

The following four propositions describe Annk(J,P) for J = I± = (S ± I) · R + (T − I)2 · R and I± = (T − 2I + T−1 ∓ 2S) · R + (I ∓ STS) · R from (3.15).

Proposition 4.4. Let k be an even integer. The space Annk(I+,P), i.e., the solutions f ∈ P to the system

- (4.22) f|k(T − I)2 = 0 and f|k(S + I) = 0, is equal to
- (4.23) ϕ2 Mk−2(SL2(Z)) + ϕ0 Mk(SL2(Z)) + ϕ−2 Mk+2(SL2(Z)), where


3i π

6i π

ϕ2(τ) = τE2(τ)2 −

E2(τ), ϕ0(τ) = τE2(τ) −

, and ϕ−2(τ) = τ. In particular, the dimension of the space of solutions equals max 0, k4 + 1 .

Proof. Suppose that f ∈ P is a solution to (4.22). The vector space spanned by f, f|kT, and f|kTS is preserved by the action of R, because

- I,T,TS are a basis of R/I+ by part (2) of Proposition 3.9, and the remainder of the proof will consist of a careful study of this action.


Set

- g0 := f|k(T − I) = f|kT − f,
- g1 := f, and
- g2 := f|k(T − I)S = f|kTS + f,


from which it follows that

- (4.24)

Ñ

- g0|kT
- g1|kT
- g2|kTé


=

Ñ

- 1 0 0
- 1 1 0
- 1 2 1éÑ


- g0
- g1
- g2é


and Ñ

- g0|kS
- g1|kS
- g2|kSé


=

Ñ

0 0 1

- 0 −1 0
- 1 0 0éÑ


- g0
- g1
- g2é


.

Deﬁne h0,h1,h2 by

- (4.25)

Ñ

- h0(τ)
- h1(τ)
- h2(τ)é


=

Ñ

1 0 0 −2τ 2 0

τ2 −2τ 1éÑ

- g0(τ)
- g1(τ)
- g2(τ)é


.

Denote the above matrix by M(τ), and the column vectors by H(τ) and G(τ), so that H(τ) = M(τ)G(τ), and denote the matrices from (4.24) for the actions of |kT and |kS on G by TG and SG, respectively. Then

(H|kT)(τ) = M(τ + 1)TGM(τ)−1H(τ) =

Ñ

1 0 0 0 1 0 0 0 1é

H(τ) = H(τ)

and

(H|kS)(τ) = M(−1/τ)SGM(τ)−1H(τ) =

Ñ

τ2 τ 1 0 1 2/τ 0 0 1/τ2é

H(τ).

In other words,

- (4.26)


h2|k−2T = h2, h2|k−2S = h2, h1|kT = h1, (h1|kS)(τ) = h1(τ) + 2τ−1h2(τ), h0|k+2T = h0, and (h0|k+2S)(τ) = h0(τ) + τ−1h1(τ) + τ−2h2(τ).

Therefore, h2 ∈ Mk−2(SL2(Z)) because of this invariance and since it has moderate growth (it is an element of P). It follows from (2.8) and the transfor-

mation properties of h1 that h1 − πi3 h2E2 ∈ Mk(SL2(Z)); in particular, h1 is a quasimodular form of weight k and depth at most 1 for SL2(Z). Similarly,

- h0 − πi6 h1E2 − π362h2E22 ∈ Mk+2(SL2(Z)), and h0 is therefore a quasimodular form of weight k + 2 and depth at most 2 for SL2(Z).


Thus we have shown the existence of modular forms f0 ∈ Mk+2(SL2(Z)), f1 ∈ Mk(SL2(Z)), and f2 ∈ Mk−2(SL2(Z)) such that h0 = f0 + f1E2 + f2E22.

Expanding and comparing with the last transformation law for h0|k+2S in (4.26), we deduce from the periodicity of h0, h1, and h2 that h1 = −6πi(f1 + 2f2E2) and h2 = −π362f2, and thus

- 1

- 2


f = g1 = τh0 +

h1 = ϕ−2f0 + ϕ0f1 + ϕ2f2. Hence f lies in (4.23), and it is straightforward to verify that all elements of

- (4.23) satisfy the conditions in (4.22). Finally, the dimension assertion follows directly from (2.4).


Proposition 4.5. Let k be an even integer. The space Annk(I−,P), i.e., the space of solutions f ∈ P to the system

- (4.27) f|k(T − I)2 = 0 and f|k(S − I) = 0, is equal to
- (4.28) ψ4 Mk−4(SL2(Z)) + ψ2 Mk−2(SL2(Z)) + ψ0 Mk(SL2(Z)), where

ψ4 = ξ4 · L + (ξ4|4S) · LS, ψ2 = ξ2 · L + (ξ2|2S) · LS, and ψ0 = 1, with

ξ4 = U2 + W2 − 2V 2 and ξ2 = U + W deﬁned in terms of the theta functions in (2.9). In particular, the dimension of the space of solutions equals max 0, k−42 + 1 .

Proof. As with the proof of Proposition 4.4, it is straightforward to use (2.11) and (2.17) to verify that all elements of (4.28) satisfy (4.27), as well as to deduce the dimension formula from (2.4). Thus we will show that any solution f ∈ P to (4.27) lies in (4.28). Set h0 := f, h1 := f|k(T − I)S, and h2 := f|k(T − I), from which it follows that

Ñ

- h0|kT
- h1|kT
- h2|kTé


=

Ñ

1 0 1 0 −1 −1 0 0 1éÑ

- h0
- h1
- h2é


and

Ñ

- h0|kS
- h1|kS
- h2|kSé


=

Ñ

1 0 0

- 0 0 1
- 0 1 0éÑ


- h0
- h1
- h2é


.

From this we see that h2|kT and h2|k(ST2S) equal h2. Since f ∈ P, h2(τ) = f(τ + 1) − f(τ) grows at most polynomially as Im(τ) → ∞, and the same is true for h2|kS = h1. Hence h2 ∈ Mk(Γ0(2)), where Γ0(2) = T,ST2S is the subgroup of matrices in SL2(Z) whose bottom-left entries are even. Furthermore, h2|k(I + S + ST) = 0 and h0 satisﬁes the system

- (4.29) h0|k(S − I) = 0 and h0|k(T − I) = h2. A solution to (4.29) is given by the function


g0 :=

1 πi

(h2 · L + h1 · LS),

as can be seen by inserting the transformation laws (2.17), and thus h0 − g0 ∈ Mk(SL2(Z)), since it satisﬁes the homogeneous version of (4.29) and inherits polynomial growth from P and (2.16).

Thus

f = h0 = h · L + (h|kS) · LS + g,

where h = πi1 h2 ∈ Mk(Γ0(2)) satisﬁes h|k(I+S+ST) = 0, and g ∈ Mk(SL2(Z)). We now invoke (2.13) and write h uniquely as

h = f1 + Uf2 + V f3 + U2f4 + V 2f5 + UV Wf6,

where f1 ∈ Mk(SL2(Z)), f2,f3 ∈ Mk−2(SL2(Z)), f4,f5 ∈ Mk−4(SL2(Z)), and f6 ∈ Mk−6(SL2(Z)). Using (2.11), we can compute the set of all solutions to the system h|k(I + S + ST) = h|k(T − I) = 0 in Mk(Γ(2)). For instance, the latter condition alone forces f6 = f4 = 0 and f2 = −2f3. We ﬁnd that the space of solutions is ξ4Mk−4(SL2(Z)) + ξ2Mk−2(SL2(Z)), which then implies

- f lies in (4.28).


For small values of k the solution spaces in Propositions 4.4 and 4.5 are small enough to rule out certain asymptotic behaviors. For example, the following lemma, which is used below to show various uniqueness statements, can be proved by direct computation of asymptotics as Im(τ) → ∞ using q-expansions (i.e., expansions in possibly fractional powers of q = e2πiz or e2πiτ, where we allow polynomials in z or τ as coeﬃcients).

Lemma 4.6. No nonzero f ∈ Ann4(I±,P) satisﬁes the bound f(τ) = o(1) as Im(τ) → ∞ with −1 ≤ Re(τ) ≤ 1. Likewise, no nonzero f ∈ Ann12(I±,P) satisﬁes the bound f(τ) = o e−2πIm(τ) as Im(τ) → ∞ with −1 ≤ Re(τ) ≤ 1.

Proposition 4.7. Let k be an even integer. The space Annk( I+,P), i.e., the solutions f ∈ P to the system

- (4.30) f|k(T − 2I + T−1 − 2S) = 0 and f|k(I − STS) = 0, is equal to
- (4.31) ϕ2 Mk−2(SL2(Z)) + ϕ0 Mk(SL2(Z)) + ϕ−2 Mk+2(SL2(Z)), where


ϕ2(z) = z2((E2|2S)(z))2, ϕ0(z) = z2(E2|2S)(z), and ϕ−2(z) = z2. In particular, the dimension of the space of solutions equals max 0, k4 + 1 . Proof. Given a solution f ∈ P to (4.30), let g0 = f|kS, g1 = −12f|k(I + S − T), and g2 = f.

Using the fact that I − STS = S(I − T)S, one veriﬁes that g0,g1,g2 satisfy the transformation law (4.24). As was shown in the proof of Proposition 4.4,

- g0 is consequently a quasimodular form of weight k + 2 and depth at most 2 for SL2(Z). Thus, g0 ∈ E22Mk−2(SL2(Z)) + E2Mk(SL2(Z)) + Mk+2(SL2(Z)). It follows that f = g0|kS lies in (4.31). The other aspects of the proof are straightforward to verify as above.


Proposition 4.8. Let k be an even integer. The space Annk( I−,P), i.e., the solutions f ∈ P to the system

- (4.32) f|k(T − 2I + T−1 + 2S) = 0 and f|k(I + STS) = 0, is equal to
- (4.33) ψ4 Mk−4(SL2(Z)) + ψ2 Mk−2(SL2(Z)) + ψ0 Mk(SL2(Z)), where


ψ4 = U2 − V 2, ψ2 = W, and ψ0 = L. In particular, the dimension of the space of solutions equals max 0, k−42 + 1 .

Proof. For the same reasons as before, we again restrict our attention to showing that solutions f ∈ P to (4.32) lie in (4.33). Let g = f|k(S + T − I). We check that g|kS = g|kT = g, and so g ∈ Mk(SL2(Z)) since it has moderate growth. Because

g · L |k(S + T − I) = πig,

the function h := f − πi1 g·L has moderate growth and satisﬁes the homogeneous equations

h|k(S + T − I) = 0 and h|kS(T + I) = 0, with the latter equation being a restatement of the second equation in (4.32) since LS|0(T + I) = 0. Then h is a modular form of weight k for Γ(2), because

T2 − I = (S + T − I)(T + I) − S(T + I) and

ST2S − I = (ST + S)(TS − S). We complete the proof by arguing, as in the proof of Proposition 4.5, and again using (2.13), that these conditions force

h ∈ ψ4Mk−4(SL2(Z)) + ψ2Mk−2(SL2(Z)).

4.3. Uniqueness of K± and their transformation properties. The characterizations of Annk(I±,P) in Section 4.2 can now be used to establish the uniqueness assertion in Theorem 4.3. Indeed, suppose K(τ,z) and K (τ,z) are two kernels satisfying conditions (1)–(4). Then for ﬁxed z ∈ H, the function τ  → K±(τ,z) − K ±(τ,z) is annihilated by |τd/2r for all r ∈ I± by part (2), and it is holomorphic at all τ ∈ H by parts (1) and (3). Furthermore, it is in P by part (4) combined with the following lemma (recall that I ⊆ I±). By

Lemma 4.6 the growth condition (4.21) forces K±(τ,z) − K ±(τ,z) to vanish identically, and hence uniqueness follows.

Lemma 4.9. Suppose f : H → C is holomorphic, k is an even integer, f|kr = 0 for all r ∈ I, and τ  → ∆(τ)(j(τ) − j(z))f(τ) is in P for some ﬁxed z ∈ H. Then f ∈ P.

Proof. The function f has moderate growth on D, because ∆(τ)(j(τ) − j(z)) −1

is bounded as τ approaches any cusp from inside D (speciﬁcally, ∆ is a cusp form and j has a pole at inﬁnity). Now Part (2) of Proposition 4.2 with

- h1 = h2 = 0 shows that f ∈ P, as desired.


Next we show that the kernels K±(τ,z) also satisfy modular functional equations in the variable z. In order to do this, ﬁrst we generalize the residue statements of part (3) of Theorem 4.3 to an action in the variable z, in addition to τ. Suppose ﬁrst that f is a meromorphic function on H, with at most simple poles. Then for any α ∈ SL2(Z) and k ∈ Z,

- (4.34) Resτ=τ0(f|kα)(τ) = j(α,τ0)2−k Resτ=ατ0 f(τ) in terms of the factor of automorphy from (2.2). Therefore

Resτ=z K|τd/2α|z2−d/2α (τ,z) = Resτ=αz K(τ,αz),

since both sides are equal to Resτ=z j(α,z)d/2−2 K|τd/2α (τ,αz). This allows us to compute

- (4.35)

Resτ=z K|τd/2α|z2−d/2β (τ,z) = Resτ=z K|τd/2αβ−1|τd/2β|z2−d/2β (τ,z)

= Resτ=βz K|τd/2αβ−1 (τ,βz)

for α,β ∈ SL2(Z). Of course these identities also hold with K replaced by K±. Combining them with (4.34), we see that part (3) of Theorem 4.3 generalizes to

- (4.36) Resτ=γz K±|τd/2α|z2−d/2β = −


j(γ,z)d/2−2 2π

φ±(αγβ−1) for α,β,γ ∈ PSL2(Z), because

Resτ=γz K±|τd/2α|z2−d/2β

j(γ,z)d/2−2 = Resτ=z K±|τd/2α|z2−d/2β|τd/2γ (by (4.34)) = Resτ=z K±|τd/2αγ|z2−d/2β

= Resτ=βz K±|τd/2αγβ−1 (τ,βz) (by (4.35))

φ±(αγβ−1) 2π

= −

.

Furthermore, for all r ∈ R = C[PSL2(Z)] and α ∈ PSL2(Z), we have the residue formula

j(α,z)d/2−2 2π

- (4.37) Resτ=αz K±|z2−d/2r (τ,z) = −


φ±(α · ι(r));

indeed, by linearity it suﬃces to verify this formula in the case that r = ι(r)−1 ∈ PSL2(Z), in which case it follows from (4.36).

Proposition 4.10. Let K± be the kernels whose existence and uniqueness are guaranteed by Theorem 4.3. Then

K±(τ,z) |z2−d/2 r = 0 for all r ∈ I±.

Proof. Let r ∈ I± and consider the function gr := K±|z2−d/2r on H × H. Part (1) of Theorem 4.3 implies that all possible poles of gr(τ,z) in τ lie at points τ = αz, where α ∈ SL2(Z). The residues at such points are computed by formula (4.37), and actually vanish since φ±(α · ι(r)) = 0 by Proposition 3.11. Thus τ  → gr(τ,z) is holomorphic, and it is in P by Lemma 4.9 and part (4) of Theorem 4.3. Thus it vanishes by Lemma 4.6 and the bounds (4.21).

4.4. Proof of Theorem 4.3 and kernel asymptotics. We can now write down the kernels in Theorem 4.3 explicitly. We claim that they are given by

ϕ−2(z) ϕ0(z) ϕ2(z) é

ϕ−2(τ) ϕ0(τ) ϕ2(τ) ét

Ñ

Ñ

· Υ(+d)(τ,z) ·

K+(d)(τ,z) =

and

· Υ(−d)(τ,z) · Ö

è

ψ0(τ) ψ2(τ) ψ4(τ)ét

Ñ

ψ0(z) ψ2(z) ψ4(z)

K−(d)(τ,z) =

in terms of the bases deﬁned in Propositions 4.4 through 4.8, for certain coeﬃcient matrices Υ(±d)(τ,z). The entries of these matrices can be written with denominators given by ∆(τ)∆(z)(j(τ)−j(z)) when d = 8 and ∆(τ)∆(z)2(j(τ)− j(z)) when d = 24, in accordance with part (4) of Theorem 4.3, and numerators that are modular forms for SL2(Z) in τ and z. Speciﬁcally, the matrix Υ(+d) will have rows of weight d/2 + 2, d/2, and d/2 − 2 in τ and columns of weight 4 − d/2, 2 − d/2, and −d/2 in z, while Υ(−d) will have rows of weight d/2, d/2 − 2, and d/2 − 4 in τ and columns of weight 2 − d/2, −d/2, and −2 − d/2 in z. (Note that although these weights can be negative, the numerator of each entry has positive weights when we use the denominator speciﬁed above.) By Propositions 4.4 through 4.8, these weights ensure that K±(d)|τd/2r = 0 for all

r ∈ I± and K±(d)|z2−d/2r = 0 for all r ∈ I±, as required by Theorem 4.3 and Proposition 4.10.

The entries of the matrices Υ(±d) are by no means obvious, but they are

uniquely determined by the list of required properties for K±(d) in Theorem 4.3. One can solve for them explicitly, with the following result. Let

(f−2,f0,f2,...,f14) = (E10/∆,1,E14/∆,E4,E6,E8,E10,∆,E14),

let Πk1,k2,k3 be the diagonal matrix diag(fk1,fk2,fk3), and let us abbreviate jτ = j(τ), jz = j(z), jτ,z = j(τ) − j(z), and N = 1728. Then we deﬁne

Ñ

1 0 0é

jτ,z 0 1 −2jτ,z −2 0

Π6,4,2(τ)

Π12,10,8(z)

Υ(8)+ (τ,z) =

,

36π−2i∆(z)(j(τ) − j(z))

Njτ,z−1 + 6 0 −6 é

Ñ

6 0 Njτ,z−1 − 6 −12jτ + 5N −2Njτ,z−1 12jτ − 7N

Π4,2,0(z)

Π14,12,10(τ)

Υ(24)+ (τ,z) =

,

36Nπ−2i∆(z)

−2N 0 0 0 1 −1 0 N − jτ jτ é

Ñ

Π10,8,6(z)

Π4,2,0(τ)

Υ(8)− (τ,z) =

, and

2Nπ∆(z)(j(τ) − j(z))

−2N −2Njτ,z 0 0 jτ + 2jτ,z −1 0 N − 2jτ,z − jτ 1 é

Ñ

Π2,0,−2(z)

Π12,10,8(τ)

Υ(24)− (τ,z) =

.

2Nπ∆(z)(j(τ) − j(z))

Note that the particular form in which we have written these matrices has no special signiﬁcance beyond being fairly compact (and it does not make the denominators readily apparent).

All that remains in the proof of Theorem 4.3 is to verify that these formulas work. Poles occur in the entries of Υ(±d)(τ,z) only from dividing by j(τ) − j(z). Thus, the poles of these matrix entries in τ are contained in the SL2(Z)-orbit of z, and they are all simple poles unless j (z) = 0. Because j = −2πiE42E6/∆ by (2.6), that can happen only if E4(z) = 0 or E6(z) = 0. The Eisenstein series E4 and E6 have single roots on the SL2(Z)-orbits of e2πi/3 and i, respectively, and no other roots by [8, Proposition 5.6.5]; the function j = 1728E43/(E43 − E62) takes the values 0 and 1728 on these orbits. Using these facts, one can check that the matrices Υ(±d)(τ,z) never have poles in τ of order greater than one.

We can calculate residues by using the identity lim

f(τ)(τ − z) j(τ) − j(z)

f(z) j (z)

if(z)∆(z) 2πE14(z)

=

=

τ→z

for a holomorphic function f on a neighborhood of z, where we interpret the right side by continuity if f(z) = j (z) = 0. We ﬁnd that for both d = 8 and 24,

π 72

0 0 1

Resτ=z Υ(+d)(τ,z) =

and

- 0 −2 0
- 1 0 0


Ç

å

−3456∆(z) 0 0 0 E4(z)2 −E6(z) 0 −E6(z) E4(z)

i 6912π2∆(z)

Resτ=z Υ(−d)(τ,z) =

.

For matrices α,β ∈ SL2(Z),

( ϕ−2|−2β)(z) (ϕ0|0β)(z) ( ϕ2|2β)(z) é

Ñ

(ϕ−2|−2α)(τ) (ϕ0|0α)(τ) (ϕ2|2α)(τ) ét

Ñ

· Υ(+d)(τ,z) ·

(K+(d)|τd/2α|z2−d/2β)(τ,z) =

and

· Υ(−d)(τ,z) · Ö

è

(ψ0|0α)(τ) (ψ2|2α)(τ) (ψ4|4α)(τ)ét

Ñ

(ψ0|0β)(z) (ψ2|2β)(z) ( ψ4|4β)(z)

(K−(d)|τd/2α|z2−d/2β)(τ,z) =

,

using the SL2(Z)-automorphy properties of the matrix entries of Υ(±d)(τ,z).

Theorem 4.3 can now be straightforwardly veriﬁed from these formulas. The uniqueness was already shown in Section 4.3, we have seen that property (1) holds, and property (2) follows from Propositions 4.4 and 4.5 and the weights of the coeﬃcients of ϕk and ψk. The residue property (3) follows from computing Resτ=z K+(d)|τd/2α as

ϕ−2(z) ϕ0(z) ϕ2(z) é

- 0 −2 0
- 1 0 0é


Ñ

Ñ

(ϕ−2|−2α)(z) (ϕ0|0α)(z) (ϕ2|2α)(z) ét

π 72 Ñ

0 0 1

·

·

and Resτ=z K−(d)|τd/2α as i 6912π2∆(z) Ñ

è

· Ö

(ψ0|0α)(z) (ψ2|2α)(z) (ψ4|4α)(z)ét

Ñ

−3456∆(z) 0 0 0 E4(z)2 −E6(z) 0 −E6(z) E4(z) é

ψ0(z) ψ2(z) ψ4(z)

·

for α ∈ {I,T,TS}. Finally, the membership in P asserted in property (4) follows from the formulas by using j∆ ∈ P, and (4.21) follows from a q-expansion calculation. This completes the proof of Theorem 4.3.

For the detailed analysis of the generating functions F and F‹ in Section 5, we will need to understand the non-decaying asymptotics of K±(d)(τ,it) as t → ∞ with t ∈ R. To do so, we expand K±(d)(τ,z) as a series in powers of eπiz,

whose coeﬃcients are functions of τ and polynomials in z of degree at most

- 2, and we deﬁne G±(d)(τ,z) to be the sum of the enπiz terms for n ≤ 0. Then


K±(d)(τ,it) = G±(d)(τ,it) + O(t2e−πt) as t → ∞. Explicit calculation shows that these functions can be expanded in z as

0

1

G±(d)(τ,z) =

zje2πikzGk,j,(d)±(τ),

j=0

k=−1

where the coeﬃcient functions Gk,j,(d)±(τ) are polynomials in τ, E2(τ), U(τ), V (τ), W(τ), L(τ), and LS(τ), and so in particular they lie in P. Note that

there are no terms with j = 2 in G±(d)(τ,z), although such terms occur elsewhere in these series expansions of K±(d)(τ,z). In addition,

G−(8)1,j,± = 0, which will be important in Sections 5 and 6. We furthermore deﬁne G(d) =

- 1

- 2 G+(d) +G−(d) to correspond with K(d), and set Gk,j(d) = 12 Gk,j,(d)+ +Gk,j,(d)− so that


0

1

zje2πikzGk,j(d)(τ). We will need the following lemma in Section 5. Lemma 4.11. Let

#### (4.38) G(d)(τ,z) =

j=0

k=−1

#### (4.39) n+,τ = 0, n−,τ = 1, n+,z = 2, n−,z = 1, n(8)τ = 2, and n(24)τ = 4.

For each δ > 0 and γ ∈ PSL2(Z), there exists a constant C = Cγ,δ > 0 such that for d ∈ {8,24},

eπi(n±,ττ+n±,zz)τ2z2 ∆(τ)∆(z)(j(τ) − j(z))

#### (4.40) K±(d)|τd/2γ|z2−d/2S (τ,z) ≤ C

,

eπin±,zzτ2z2 ∆(τ)∆(z)(j(τ) − j(z))

#### (4.41) (K±(d) − G±(d))|τd/2γ (τ,z) ≤ C

, and

(d)

τ τ+z)τ2z2 ∆(τ)∆(z)(j(τ) − j(z))

eπi( n

#### (4.42) K±(d)|z2−d/2S (τ,z) ≤ C

,

for Im(τ),Im(z) ≥ δ with j(τ) = j(z). Proof. The kernels K±(d) are annihilated by I± under |τd/2, and one can

check that the same is true for G±(d). Thus, to cover all γ ∈ PSL2(Z) it suﬃces to check the cases γ = I, T, or TS, because they form a basis of R/I± by Proposition 3.9.

For each of these three cases, the explicit formulas for the kernels show that the expressions inside the absolute values on the left sides, when multiplied by ∆(τ)∆(z)(j(τ)−j(z)), are ﬁnite sums of the form 2j=0 2k=0 φjk(τ,z)τjzk, where φjk is a holomorphic function on H × H satisfying φjk(τ + 2,z) = φjk(τ,z) = φjk(τ,z + 2). The claims then follow from the form of the double power series expansion of φjk(τ,z) in eπiτ and eπiz, which can be shown by direct calculation to vanish to the asserted order in these exponentials.

Note that the denominators of ∆(τ)∆(z)(j(τ) − j(z)) are not an obstacle to computing asymptotics. For example, if τ is ﬁxed and z = it with t ∈ (0,∞), then ∆(τ)∆(it)(j(τ)−j(it)) approaches −∆(τ) as t → ∞, and it is asymptotic to −t−12∆(τ) as t → 0 by modularity, as in the proof of Lemma 4.9.

### 5. Proof of the interpolation formula

5.1. The continuation of F from D to H. Let d be 8 or 24, and let K and K± be the kernels from Theorem 4.3 for this value of d (we also suppress superscripts (d) for G and similar terms). As before, we identify radially symmetric functions of x ∈ Rd with functions of r = |x|. Analytic continuation will be important in both τ and r, and so we view r as a complex variable.

Using the kernel K, we can now construct the generating function F we need for Theorem 3.1. We start with the formal expression (4.19), which we decompose as F(τ,r) = F1(τ,r) + F2(τ,r), where

- (5.1) F1(τ,r) = eπiτr2 and F2(τ,r) = 4sin πr2/2 2


∞

K(τ,it)e−πr2t dt.

0

We have not yet addressed when the integral is deﬁned. Part (1) of Theorem 4.3 shows that the poles of the integrand in τ are constrained to SL2(Z)-translates of the imaginary axis. None of these translates intersects D aside from the imaginary axis itself, which in fact does not contribute any poles since part (3) of Theorem 4.3 shows that K(τ,it) is holomorphic at τ = it and τ = i/t (as φ(I) = φ(S) = 0). Thus, poles are not an obstacle when τ ∈ D.

To analyze the convergence of the integral in (5.1), we must understand how K(τ,it) behaves as t → 0 or t → ∞. Inequality (4.40) (with γ = I) in Lemma 4.11 shows that it decays exponentially in 1/t as t → 0 (see also the paragraph after Lemma 4.11), while it grows at most exponentially as t → ∞ because K(τ,it) = G(τ,it) + O(t2e−πt). Therefore the integral in (5.1) is convergent for τ ∈ D and r in some open set O ⊆ C containing all suﬃciently large real numbers. More precisely, our analysis of G(τ,it) in Section 4.4 shows that it suﬃces to take |r| > 0 for d = 8 and |r| > √2 for d = 24. Furthermore,

- F2(τ,r) is holomorphic as a function of either variable on these sets. (This is a general principle about integrals of analytic functions: by Morera’s theorem, it


suﬃces to show that contour integrals vanish, and that reduces to the analyticity of the integrand by Fubini’s theorem.)

Theorem 3.1 also involves the function F‹ = (eπir2τ − F)|τd/2S = −F2|τd/2S

deﬁned just above (4.5). Since SD = D and −K|τd/2S = 12(K+ − K−) = K, we may use (5.1) to write

- (5.2) F‹(τ,r) = 4sin πr2/2 2

∞

0

K(τ,it)e−πr2t dt for τ ∈ D and r ∈ O.

We next analytically continue r  → F2(τ,r) to an open neighborhood of R in C by breaking up the integral as follows. For τ ∈ D, r ∈ O, and ﬁxed p > 0 we decompose F2(τ,r) as

- (5.3) F2(τ,r) = F2,low(τ,r) + F2,trunc(τ,r) + F2,high(τ,r), where
- (5.4)


p

F2,low(τ,r) = 4sin πr2/2 2

K(τ,it)e−πr2t dt,

0

∞

F2,trunc(τ,r) = 4sin πr2/2 2

(K(τ,it) − G(τ,it))e−πr2t dt, and

p

∞

F2,high(τ,r) = 4sin πr2/2 2

G(τ,it)e−πr2t dt

p

Å

4sin πr2/2 2 π

0

Gk,0(τ) 2k + r2

e−pπ(2k+r2)

=

k=−1

ã

i(1 + 2kpπ + pπr2)Gk,1(τ) π(2k + r2)2

+

,

where Gk,0(τ) and Gk,1(τ) are as in (4.38). As noted above, the ﬁrst two integrals are absolutely convergent because of the exponential decay in z in (4.40) and

- (4.41) with γ = I. Thus both integrals deﬁne holomorphic functions for r in a neighborhood of R in C. Furthermore, they are both averages of Gaussians, with the ﬁrst weighted by K(τ,it) (which decays exponentially in 1/t as t → 0

- by (4.40), and hence damps the contributions of e−πr2t for t small) and the second by K(τ,it)−G(τ,it) (which decays exponentially as t → ∞). To analyze the Schwartz seminorms, we can use the identity


- (5.5) max r∈R


c 2πet

c/2

rce−πr2t =

#### for c ≥ 0 and t > 0, where we interpret the right side of (5.5) as 1 when c = 0. It follows by diﬀerentiating under the integral sign and using (5.5) to bound the integrand that the ﬁrst two integrals in (5.4) deﬁne Schwartz functions, and

that for any ﬁxed k,  ≥ 0, the Schwartz seminorms

d dr

d dr

rk

rk

max

F2,low(τ,r) and max

F2,trunc(τ,r)

r∈R

r∈R

are bounded as τ ranges over any ﬁxed compact subset of D. (Recall from Lemma 2.1 that it suﬃces to use radial seminorms.) Note that the uniformity in τ makes use of (4.41) and (4.42), and not just our previous estimate K(d)(τ,it) =

- G(d)(τ,it) + O(t2e−πt) as t → ∞, although that would suﬃce to analyze the case of ﬁxed τ.


The explicit evaluation of F2,high(τ,r) shows that it is in fact entire in r, since the possible singularities at r2 = −2k are compensated for by the vanishing of sin πr2/2 2 at those points. Furthermore, for any ﬁxed k,  ≥ 0

the map τ  → maxr∈R rk drd F2,high(τ,r) is in P since each Gk,j ∈ P. Formulas

- (5.3) and (5.4) accordingly serve as our deﬁnition of F2(τ,r), and in turn F(τ,r) = eπiτr2 + F2(τ,r), for arbitrary τ ∈ D and r ∈ R. Note that although the integrals in (5.4) all depend on a parameter p, their sum is independent of p for large r by construction and hence for all r ∈ R by analytic continuation. Aside from a technical point in the proof of Proposition 5.1 that requires two diﬀerent choices of p, this parameter will be ﬁxed and hence suppressed from the notation (in Section 6 a similar construction uses the value p = 1.01).


Having deﬁned F2(τ,r) for τ ∈ D, we next turn to its analytic continuation to the full upper half-plane H. The anticipated transformation laws (4.5) for F can be restated via (5.1) as

F2(τ + 2,r) − 2F2(τ + 1,r) + F2(τ,r) = 4eπir2(τ+1) sin πr2/2 2 and (F2|τd/2S)(τ + 2,r) − 2(F2|τd/2S)(τ + 1,r) + (F2|τd/2S)(τ,r) = 0.

- (5.6)


In fact, we will use (5.6) to deﬁne the extension from D to H, via Proposition 4.2. To satisfy the hypotheses of Proposition 4.2, we will need the following extension of F2 to an open neighborhood of the closure D of D:

Proposition 5.1. There exists an open subset D+ of H containing D such that for each r, the function τ  → F2(τ,r) extends to a holomorphic function on D+, which satisﬁes the recurrences (5.6) whenever the left sides are deﬁned. Moreover, r  → F2(τ,r) is a Schwartz function for each τ, and for any ﬁxed

integers k,  ≥ 0 the Schwartz seminorm maxr∈R rk drd F2(τ,r) is bounded as τ ranges over any compact subset of D+.

Proof. We ﬁrst show the continuation to the right of Re(τ) = 1. The continuation to the left of Re(τ) = −1 is nearly identical, and those across the bottom two semicircles of the boundary of D are drastically simpler (owing to the homogeneity of the second equation in (5.6) and the absence of poles as one crosses those boundaries).

U U

T−1SU TSU

−1 0 1

Figure 5.1. The regions U, U = {τ ∈ C : −τ ∈ U}, TSU = SU , and T−1SU = SU = {τ ∈ C : −τ¯ ∈ TSU} in the proof of continuation of F2(τ,r). The shaded region is the domain D from (4.6), and D, U, U , TSU, and T−1SU together form D+.

Let U denote the interior of the closure of T

ß

™

ß

™

- 1

- 2


1 2

∪ TST−1

τ ∈ F : Re(τ) <

τ ∈ F : Re(τ) >

.

Then its closure U includes the line Re(τ) = 1 but intersects no other SL2(Z)translate of the imaginary axis (see Figure 5.1). For τ ∈ U and |r| suﬃciently large, deﬁne

F 2(τ,r) := 4sin πr2/2 2

∞

K(τ,it)e−πr2t dt,

0

i.e., by the same integral formula as in (5.1). It, too, has an analytic continuation to a neighborhood of R in C using the integral formulas in (5.4), for exactly the same reason as before.

To relate F 2 and F2, we will examine the poles of K(τ,z) using part (3) of Theorem 4.3 and equation (4.37) (with the group algebra element r in this equation given by r = 1). For τ ∈ U the only possible singularities of the integrand with z = it are at z = T−1τ or z = ST−1τ, with τ on the left boundary of U. For α ∈ PSL2(Z), there is a pole at z = ατ if and only if

i(t0 + ε)

it0 1 + it0

i(t0 − ε)

Figure 5.2. A contour achieving analytic continuation for τ near 1 + it0.

φ(α−1) = 0, because z = ατ means τ = α−1z, and by (4.37) the residue is

z − ατ τ − α−1z

Resz=ατ K(τ,z) = Resw=α−1z K(w,z) z=ατ lim

z→ατ

Å

ã

j(α−1,ατ)d/2−2 2π

1 j(α,τ)2

φ(α−1)

= −

−

φ(α−1) 2π j(α,τ)d/2

=

.

Thus, there is no pole at ST−1τ, because φ(TS) = 0. On the other hand, there is a pole with residue 1/(2π) at z = T−1τ, because φ(T) = 1. We must account for this pole if we wish to cross the line Re(τ) = 1.

To cross this line, we return to the integrals deﬁning F2(τ,r) in (5.3) and

- (5.4), which are contour integrals along pieces of the imaginary axis in the variable z = it. Consider a point it0 on one of these contours; we wish to continue τ  → F2(τ,r) from Re(τ) slightly less than 1 to a neighborhood of 1 + it0. As shown in Figure 5.2, to do so we can shift the integration in z from the segment from i(t0 − ε) to i(t0 + ε) to the semicircle z = it0 + eiθε with −π/2 ≤ θ ≤ π/2, where the radius ε = ε(t0) is taken to be small enough that this semicircle remains inside D; it is at this point that we may need two diﬀerent choices of p (e.g., p = 1 and p = 2), so that we can ensure that


|p − t0| > ε and thus ip is either above or below this semicircle. The contours having been moved out of the way of the poles of the integrand, these integrals now give an expression for F2(τ,r) that is holomorphic for T−1τ slightly to the left of the contour, in particular, for τ in a ball of radius ε/2 around 1 + it0. We now claim that F2(τ,r) is a Schwartz function of r whose Schwartz

seminorms are bounded in the region {τ ∈ C : |τ − 1 − it0| ≤ ε/2}. Indeed, the contribution of the integral from the undeformed contour along the imaginary axis retains this property, just as it did for τ ∈ D in the comments following

- (5.5). Meanwhile, K(τ,z) is continuous and hence bounded in terms of t0 for such τ and for z on the deformed semicircle, which establishes the claimed seminorm bound, just as right after (5.5).


Having shown the analytic continuation of F2(τ,r) past Re(τ) = 1 to an open subset of U, we next claim that

- (5.7) F2(τ,r) = F 2(τ,r) + 4eπir2(τ−1) sin πr2/2 2


on this common domain of deﬁnition. For suﬃciently large r, this identity follows from moving the deformed semicircles back into place and using Resz=τ−1 K(τ,z) = 1/(2π), and hence it holds for all r ∈ R by analytic continuation.

Arguing similarly, one continues τ  → F2(τ,r) across Re(τ) = −1 to the reﬂected region U = {τ ∈ C : −τ¯ ∈ U}, as well as across the bottom semicircles |τ ± 1/2| = 1/2 to TSU and T−1SU = {τ ∈ C : −τ¯ ∈ TSU}. In particular, the integral (5.1) extends holomorphically for large r to these last two domains, because part (3) of Theorem 4.3 shows there is no pole on those bottom semicircles. (Speciﬁcally, the residue of K(τ,z) at τ = γz is proportional to φ(γ), and φ(STS) = φ(ST) = φ ST−1 = φ ST−1S = 0; note also that φ(TS) = φ T−1S = 0, so there is no need to take care with inverses.)

So far, we have seen how to analytically continue τ  → F2(τ,r) to all of D+ := D ∪ U ∪ U ∪ TSU ∪ T−1SU , and the boundedness of the Schwartz seminorms holds for the same reason as above. All that remains is to prove the recurrences (5.6). We begin with the ﬁrst equation in (5.6), namely

F2(τ,r) |τd/2 (T − I)2 = 4eπir2(τ+1) sin πr2/2 2

whenever τ,τ + 1,τ + 2 ∈ D+. The set of such τ is connected (it is the interior of the closure of U ∪ T−2U), and so by analyticity it suﬃces to prove this identity when r is suﬃciently large and τ + 2 ∈ U, in which case τ,τ + 1 ∈ D. Then

F2(τ + 2,r) = F 2(τ + 2,r) + 4eπir2(τ+1) sin πr2/2 2

- by (5.7), and therefore


F2(τ,r) |τd/2 (T − I)2 = 4eπir2(τ+1) sin πr2/2 2

+ F 2(τ,r) |τd/2 T2 − 2F2(τ,r) |τd/2 T + F2(τ,r)

= 4eπir2(τ+1) sin πr2/2 2

∞

+ 4sin πr2/2 2

K(τ,it) |τd/2 (T − I)2 e−πr2t dt.

0

Because K(τ,it) |τd/2 (T − I)2 = 0, we obtain F2(τ,r) |τd/2 (T − I)2 = 4eπir2(τ+1) sin πr2/2 2, which is the ﬁrst identity in (5.6). The second identity states that

F2(τ,r) |τd/2 S(T − I)2 = 0, and it is proved almost exactly the same way. Because D+ is invariant under S, the set of τ such that Sτ,STτ,ST2τ ∈ D+ is again connected (it is the same as the set of τ such that τ,Tτ,T2τ ∈ D+). We can assume ST2τ ∈ T−1SU = SU and r is suﬃciently large. Then STτ,Sτ ∈ D, and each of the three terms in F2(τ,r) |τd/2 S(T − I)2 can be computed using the integral (5.1) when r is large enough. Thus, the second identity follows from K(τ,it) |τd/2 S(T − I)2 = 0.

We conclude this subsection with some implications of Proposition 5.1 and both parts of Proposition 4.2.

Corollary 5.2. The function τ  → F2(τ,r) extends to a holomorphic function on H satisfying the identities

- (5.8) F2|τd/2(T − I)2 = −eπir2τ|τd/2(T − I)2 and F2|τd/2S(T − I)2 = 0, and consequently F = F1+F2 extends to a holomorphic function on H satisfying


- (4.5); in particular, conditions (1) and (5) of Theorem 3.1 hold with F‹ = (eπiτ|x|2 −F)|τd/2S. Furthermore, condition (3) of Theorem 3.1 holds if and only if maxr∈R rk drd F2(τ,r) has moderate growth on D.


Of course moderate growth on D is equivalent to that on D, by continuity. Proof. The extension and the identities in (5.8) follow immediately from

part (1) of Proposition 4.2, with f(τ) = F2(τ,r), h1 = −eπir2τ|τd/2(T − I)2, and h2 = 0. Equation (4.5) is a restatement of condition (5) of Theorem 3.1, since

we have deﬁned F‹ = (eπir2τ −F)|τd/2S. As for condition (3) of Theorem 3.1, the corresponding estimate for F2, namely that maxr∈R rk drd F2(τ,r) has moderate growth on H, implies those for F(τ,r) = eπir2τ + F2(τ,r) and F‹ = −F2|τd/2S. (Here we have used that eπir2τ and all its derivatives with respect to r have moderate growth in τ, uniformly in r, which follows from (5.5).) To reduce the moderate growth to D ⊆ H, we can apply part (2) of Proposition 4.2 with

- f(τ) = rk drd F2(τ,r), h1 = −rk drd eπir2τ|τd/2(T − I)2, and h2 = 0. For ﬁxed r ∈ R the bound (4.12) then shows moderate growth in τ with constants coming


from the Schwartz seminorms of F2(τ,r) and h1, and the ﬁnal statement follows by maximizing over r ∈ R.

5.2. Proof of Theorem 1.7. The interpolation formula (1.4) will follow from Theorem 3.1 once we verify all the latter’s hypotheses. The radial hypothesis (2) holds by construction, and hypotheses (1) and (5) were just demonstrated in Corollary 5.2, which also reduced hypothesis (3) to checking the moderate

growth of maxr∈R rk drd F2(τ,r) for τ ∈ D. Since the seminorm boundedness assertion in Proposition 5.1 gives the boundedness of maxr∈R rk drd F2(τ,r) for τ in any ﬁxed compact subset of D, it further suﬃces to verify the moderate growth for τ lying in a neighborhood in D of one of its cusps. Thus to ﬁnish the proof of Theorem 1.7 we will show that

- (5.9) max r∈R


d dr

rk

F2(τ,r) has moderate growth for τ near cusps of D,

and that there is an absolute constant A > 0 such that

- (5.10) F(8)(τ,x),F‹(8)(τ,x) = O |τ|Ae−πIm(τ)

and

- (5.11) F(24)(τ,x),F‹(24)(τ,x) = O |τ|Ae−3πIm(τ)


as Im(τ) → ∞ with −1 ≤ Re(τ) ≤ 1. Indeed, (5.10) and (5.11) are stronger than hypothesis (4) and the concluding statement in Theorem 3.1, which allows us to deduce n0 = 2 in d = 24 dimensions.

The fundamental domain D has four cusps, namely −1, 0, 1, and ∞ (see

- Figure 4.1). Neighborhoods of these cusps are respectively parametrized by


the following elements of SL2(Z) acting on τ with large imaginary part in the following strips: T−1S applied to −1 ≤ Re(τ) ≤ 0; S applied to −1 ≤ Re(τ) ≤ 1; TS applied to 0 ≤ Re(τ) ≤ 1; and I applied to −1 ≤ Re(τ) ≤ 1. Since factors of automorphy do not aﬀect moderate growth by (4.4), assertion (5.9) is

equivalent to the moderate growth of maxr∈R rk drd (F2|τd/2γ)(τ,r) for each of these group elements γ and τ with large imaginary part in its corresponding strip. Alternatively, since the corresponding seminorm growth assertion holds for F1(τ,r) = eπiτr2, for each of these γ it is equivalent to replace F2 by F in this last assertion. For the rest of this subsection we thus assume

−1 ≤ Re(τ) ≤ 1 and Im(τ) is large.

Our key tool is a contour shift very similar to the proof of [53, Proposition 2]. For |r| and Im(τ) both suﬃciently large, we write the factor sin πr2/2 2 in terms of complex exponentials, incorporate them into the integrand from (5.1),

and set z = it to obtain

1+i∞

K(τ,z − 1)eπir2z dz + i

F2(τ,r) = i

1

i∞

K(τ,z)eπir2z dz,

− 2i

0

−1+i∞

K(τ,z + 1)eπir2z dz

−1

where all the contours are vertical rays. We now claim that a shift to the contours α−1, α0, α1, and α∞ shown in Figure 5.3 yields

- (5.12)


F(τ,r) = eπir2τ + F2(τ,r)

= i

K(τ,z − 1)eπir2z dz + i

α1

− 2i

K(τ,z)eπir2z dz

α0

K(τ,z + 1)eπir2z dz

α−1

+ i

α∞

K|z2−d/2(T + T−1 − 2I) (τ,z)eπir2z dz.

Speciﬁcally, we must shift the contours involving K(τ,z − 1) and K(τ,z + 1), and the only poles that can intervene in this contour shift are the poles of z  → K(τ,z ± 1) at z = τ, with residues

1 2π

Resz=τ K(τ,z ± 1) = ∓

by part (3) of Theorem 4.3. When Re(τ) > 0, we obtain a contribution from K(τ,z −1) at z = τ, while K(τ,z +1) has no pole at z = τ −1; when Re(τ) < 0,

- we obtain a contribution from K(τ,z + 1) at z = τ, while K(τ,z − 1) has no pole at z = τ +1; ﬁnally, when Re(τ) = 0 both contour shifts contribute half as much (alternatively, this case follows by continuity). In each case, the residues


cancel the eπir2τ term from F(τ,r) = eπir2τ + F2(τ,r) and we obtain (5.12). We can rewrite the last integrand in (5.12) using

- 1

- 2K+|z2−d/2(T + T−1 − 2I)


K|z2−d/2(T + T−1 − 2I) =

- 1

- 2K−|z2−d/2(T + T−1 − 2I)


+

= K+|z2−d/2S − K−|z2−d/2S

= 2 K|z2−d/2S

= −2K|τd/2S|z2−d/2S,

α∞

6i/5

α−1 α0 α1

−1 0 1

STα−1 ST−1α1

−1 1+6i/5

−1 −1+6i/5

−1 0 1

Figure 5.3. The contours α−1, α0, α1, α∞, STα−1, and ST−1α1 superimposed on the fundamental domain D shown in Figure 4.1. All four contours on the left share a common terminus at 6i/5, with α−1, α0, and α1 ending there and α∞ starting there, while those on the right go from i∞ to −1/(±1 + 6i/5).

by Proposition 4.10, the deﬁnition of I± from (3.15), and (4.20). Thus,

- (5.13)

F(τ,r) = i

α1

K(τ,z − 1)eπir2z dz + i

α−1

K(τ,z + 1)eπir2z dz

− 2i

α0

K(τ,z)eπir2z dz

− 2i

α∞

K|τd/2S|z2−d/2S (τ,z)eπir2z dz.

If we instead start with formula (5.2) for F‹ = −F2|τd/2S, or with (5.1) for

F2|τd/2TS or F2|τd/2T−1S, then no poles are encountered in these contour shifts, again because of the residue formula from part (3) of Theorem 4.3. Thus after a change of variables (5.13) generalizes to

- (5.14)


dz zd/2

K|τd/2γ|z2−d/2S (τ,z)eπir2(1−1/z)

Φ(τ,r) = i

ST−1α1

dz zd/2 − 2i

K|τd/2γ|z2−d/2S (τ,z)eπir2(−1−1/z)

+ i

STα−1

dz zd/2 − 2i

K|τd/2γ|z2−d/2S (τ,z)eπir2(−1/z)

Sα0

#### K|τd/2Sγ|z2−d/2S (τ,z)eπir2z dz,

α∞

where (Φ,γ) is one of the four pairs

- (5.15)

(F, I), (−F,‹ S), (F2|τd/2TS, TS), (F2|τd/2T−1S, T−1S),

and we assume −1 ≤ Re(τ) ≤ 1 and Im(τ) is large. Note that these pairs are exactly the cases we must analyze to treat the four cusps of D. Since

- (5.16) K =


- 1

- 2


(K+ + K−) and K = −K|τd/2S =

- 1

- 2


(K+ − K−),

estimates on the ﬁrst two kernels in (5.15) are provided in (4.42), and estimates on the last two kernels are provided in (4.40).

Though its derivation initially assumed |r| large, formula (5.14) actually gives an analytic continuation to all r ∈ R, as can be seen from (4.40) and

- (4.42), which show that each of its four integrals is absolutely convergent and can be diﬀerentiated under the integral sign. In particular, letting

ek, (z,r) = rk

d dr

eπizr2, we have

- (5.17)


dz zd/2

d dr

K|τd/2γ|z2−d/2S (τ,z)ek, (1 − 1/z,r)

rk

Φ(τ,r) = i

ST−1α1

dz zd/2 − 2i

K|τd/2γ|z2−d/2S (τ,z)ek, (−1 − 1/z,r)

+ i

STα−1

dz zd/2 − 2i

K|τd/2γ|z2−d/2S (τ,z)ek, (−1/z,r)

Sα0

K|τd/2Sγ|z2−d/2S (τ,z)ek, (z,r)dz.

α∞

Claims (5.9)–(5.11) are now reduced to bounding the four integrals in (5.17). Each of these four contours in (5.17) lies above Im(z) = 1/3, and consists of a semi-inﬁnite ray along the imaginary axis (possibly) together with a compact curve in H (see Figure 5.3). Thus for Im(τ) suﬃciently large the only SL2(Z)translates of τ near any of these contours are τ −1, τ, and τ +1, which can only possibly contribute poles for z on the imaginary axis portion of the contour.

We shift the contours (if necessary) to keep z at distance at least 1/4 from any of these potential poles, in particular by taking the integration over C1 ∪ C2 ∪ C3, where C1 runs along the compact curve and the imaginary axis between i and i(Im(τ) − 1/4), C2 is a contour between i(Im(τ) − 1/4) and i(Im(τ) + 1/4) keeping distance at least 1/4 from any SL2(Z)-translate of τ, and C3 runs along the imaginary axis between i(Im(τ) + 1/4) and ∞ (see

- Figure 5.4).


C3

- C1

- C2

- C3


C2

τ − 1 τ τ + 1

τ − 1 τ

C1

−1 0 1

−1 0 1

Figure 5.4. The contours C1, C2, and C3 (shown here for STα−1) keep distance at least 1/4 from any Z-translate of τ.

Next we use (5.16) with the estimates (4.40) and (4.42) from Lemma 4.11 to bound the kernel factors by positive linear combinations of terms of the form

eπi(Bττ+Bzz)τ2z2 ∆(τ)∆(z)(j(τ) − j(z))

,

with the integers Bτ and Bz coming from the exponents on the right sides of those bounds. We claim this last expression is itself bounded by a constant multiple of

eπi(Bττ+Bzz)τ2z2 e2πiτ − e2πiz

for Im(z) ≥ 1/3 and suﬃciently large Im(τ). Indeed, writing j’s q-expansion (2.5) as

j(w) = J(e2πiw) = e−2πiw + 744 + J(e2πinw), where J(u) = n≥1 cj(n)un, we see that J (u) = O(1) as |u| → 0 and hence j(τ) − j(z) = J(e2πiτ) − J(e2πiz) = e−2πiτ − e−2πiz +

e2πiτ

J (u)du,

e2πiz

which is (e2πiz −e2πiτ)(e−2πi(τ+z) +O(1)) for Im(τ),Im(z) ≥ 1/3. Furthermore, the product formula for ∆ implies that |∆(z)| |e2πiz| for Im(z) ≥ 1/3, where

indicates inequality up to a positive constant factor. Hence for suﬃciently large Im(τ), the O(1) term is less than half the e−2πi(τ+z) to which it is added, so |∆(τ)∆(z)(j(τ) − j(z))| |e2πiτ − e2πiz|, and the claim follows.

To deal with the functions ek,  appearing in (5.17), we note that for each k and , there exists a constant A such that

max

r∈R

d dr

eπizr2 |z|A,

rk

and the same holds if z is replaced with −1/z, 1 − 1/z, or −1 − 1/z on the left side of the inequality (this follows from (5.5) and Im(−1/z) = Im(z)/|z|2). We can assume that A ≥ 0 because Im(z) is bounded away from 0. We have thus reduced the veriﬁcation of (5.9)–(5.11) to estimates for large Im(τ) of the three integrals

eπi(Bττ+Bzz) e2πiτ − e2πiz |z|A dz

- (5.18) Ij(τ) = Cj


for j = 1,2,3, where A is a positive integer depending on k and . In all cases 1 ≤ Bz ≤ 2 and Bτ + Bz ≥ 2, by (4.39).

For z ∈ C1, the denominator |e2πiτ − e2πiz| in (5.18) is at least a constant multiple of |e2πiz|, and

Ç

å

Im(τ)−1/4

|I1(τ)| |τ|Ae−πBτ Im(τ)

e(2−Bz)πt dt

1 +

,

1

which is O e−π(Bτ+Bz−2) Im(τ)|τ|A+1 ; note that in the displayed formula above, the term 1 inside the parentheses accounts for the portion of the contour below imaginary part 1. Next, let z ∈ C2, which keeps distance at least 1/4 from all integral translates of τ, but has imaginary part within 1/4 of Im(τ); that is,

ß

™

1 4

1 4

w ∈ C : |Im(w)| ≤

for all n ∈ Z

z − τ ∈

and |w − n| ≥

.

The image of this last region under the map w  → e2πiw is compact but omits 1, and hence is bounded away from 1. It follows that the denominator |e2πiτ − e2πiz| = e−2πIm(τ)|1 − e2πi(z−τ)| is at least some constant multiple of e−2πIm(τ). Consequently,

|I2(τ)| e−π(Bτ+Bz−2) Im(τ)|τ|A.

Finally, for z ∈ C3 the denominator satisﬁes |e2πiτ − e2πiz| |e2πiτ|, and the fact that Bz ≥ 1 allows us to show

∞

|I3(τ)| ≤ e−π(Bτ−2) Im(τ)

e−πBzttA dt

Im(τ)+1/4

e−π(Bτ+Bz−2) Im(τ)|τ|A.

Combined, I1(τ) + I2(τ) + I3(τ) = O e−π(Bτ+Bz−2) Im(τ)|τ|A+1 . Thus (5.9) follows, since Bτ + Bz = 2 in all cases in (4.40) (recall (5.16)). Finally, the estimates (4.42) imply (5.10) (with Bτ +Bz = 3) and (5.11) (with Bτ +Bz = 5), which completes the proof of Theorem 1.7.

5.3. Proof of Theorem 1.9. The following lemma is a direct consequence of applying Lemma 4.6 to the eigenfunctions g ± g of |d/2S:

Lemma 5.3. Let (d,n0) be (8,1) or (24,2). If g, g ∈ P satisfy

g(τ + 2) − 2g(τ + 1) + g(τ) = 0, g(τ + 2) − 2 g(τ + 1) + g(τ) = 0,

- (5.19)


g(τ) + (i/τ)d/2 g(−1/τ) = 0,

and g(τ), g(τ) = o e−2π(n0−1) Im(τ) as Im(τ) → ∞ with −1 ≤ Re(τ) ≤ 1, then g = g = 0.

Recall that the conditions of Theorem 3.1 for F(τ,x) and F‹(τ,x) were shown to hold in the previous subsection. Therefore F(τ,x) and F‹(τ,x) have the form (3.1) and (3.2), and it follows that they and their partial derivatives of all orders in x are o e−2π(n0−1) Im(τ) as Im(τ) → ∞, for any ﬁxed x. Furthermore, for any ﬁxed x, the functions F(τ,x) and F‹(τ,x) satisfy the ﬁrst two equations in (5.19), and an inhomogeneous variant of the third, in which the right side is replaced by eπiτ|x|2. For m ≥ n0 and |x| = √2m, the pair of functions

- g(τ) = F τ,√2m −e2πimτ and g(τ) = F‹ τ,√2m satisﬁes (5.19), since e2πimτ is periodic. Thus the lemma shows g and g are identically zero, i.e.,


√

√

2m = e2πimτ and F‹ τ,

2m = 0. In terms of the coeﬃcients of the Fourier series expansion (1.6), we deduce for m,n ≥ n0 that an √2m = δn,m and bn √2m = an √2m = bn √2m = 0.

F τ,

Next consider the radial derivatives (i.e., derivatives with respect to r = |x|) of equations (1.8)–(1.10), which again have unique solutions for any ﬁxed x by the same logic as above. Suppose n,m ≥ n0. At |x| = √2m we similarly deduce that ∂F∂r τ,√2m = 2πi√2mτe2πimτ and ∂∂rF‹ τ,√2m = 0, from which

- we obtain b n √2m = δn,m and a n √2m = an √2m = bn √2m = 0. Applying the Fourier transform Fx in x and replacing τ with −1/τ in


equations (1.8)–(1.10) shows that if (F(τ,x),F‹(τ,x)) is a solution to these three equations, then so is (FxF‹(τ,x),FxF(τ,x)). Applying the lemma to the diﬀerence of these two solutions shows that F‹(τ,x) = FxF(τ,x). In terms of the Fourier series (1.6) and (1.7), an = an and bn = bn. This shows that (1.4) is in fact inverse to the map in the statement of Theorem 1.9. The image of the latter map is contained in S(N)4 because of the decay of Schwartz functions, and the image of the inverse map is a radial Schwartz function because the radial

seminorms of the interpolation basis grow at most polynomially by Theorem 3.1. This completes the proof of Theorem 1.9.

5.4. Integral formulas for the interpolation basis. We can now prove integral formulas for the interpolation basis, which generalize the formulas for the sphere packing auxiliary functions from [53, 15]. These formulas are not needed to prove the interpolation theorem or universal optimality, but they are of interest in their own right, and they help clarify the relationship with the sphere packing constructions.

We begin by noting that for z in any ﬁxed compact subset of H, whenever Im(τ) is suﬃciently large the kernels can be expanded as

- (5.20) K(τ,z) = n≥n0

αn(z)e2πinτ + 2πiτ

n≥n0

√

2nβn(z)e2πinτ

and

- (5.21) K(τ,z) = n≥n0


√

αn(z)e2πinτ + 2πiτ

2n βn(z)e2πinτ

n≥n0

for some functions αn, βn, αn, and βn that depend only on the dimension d ∈ {8,24}. The existence of expansions of these forms is ensured by parts (2) and (4) of Theorem 4.3. To obtain the explicit expansions, we use the q-series in τ for the quasimodular forms appearing in the explicit constructions of K and K, as well as the analogous expansions of L and LS, and we write

j(z)n j(τ)n+1

1 j(τ) − j(z)

=

n≥0

to deal with the factor of j(τ) − j(z) in the denominator. (Note that 1/j(τ) has an expansion in terms of positive powers of e2πiτ.)

Proposition 5.4. For d ∈ {8,24}, the interpolation basis functions from Theorem 1.7 satisfy

∞

an(r) = 4sin πr2/2 2

αn(it)e−πr2t dt and

0

∞

bn(r) = 4sin πr2/2 2

βn(it)e−πr2t dt whenever r2 > 2n, and

0

∞

an(r) = 4sin πr2/2 2

αn(it)e−πr2t dt and

0

∞

bn(r) = 4sin πr2/2 2

βn(it)e−πr2t dt whenever r2 > 0 for d = 8, and whenever r2 > 2 for d = 24.

0

In other words, the interpolation basis functions are integral transforms of the coeﬃcients in the series expansions of K and K. As usual, one can meromorphically continue the integrals in r by removing the non-decaying terms from the q-expansion of the integrand and handling them separately. Speciﬁcally, one can show (using the proof of Proposition 5.4 and the explicit formulas for the kernels K and K) that the coeﬃcients have expansions of the form

- (5.22)

αn(z) = −iz e−2πinz +

m≥m0

α0,m,n + α1,m,nz + α2,m,nz2 eπimz,

βn(z) =

e−2πinz 2π√2n

+

m≥m0

β0,m,n + β1,m,nz + β2,m,nz2 eπimz,

αn(z) =

m≥m0

α0,m,n + α1,m,nz + α2,m,nz2 eπimz, and

βn(z) =

m≥m0

β0,m,n + β1,m,nz + β2,m,nz2 eπimz

for some constants α ,m,n, β ,m,n, α ,m,n, and β ,m,n, where m0 = 0 for d = 8

- and m0 = −2 for d = 24. However, we will not need these expansions.


Proof of Proposition 5.4. As in (3.6) and (3.7), we can write the basis functions as integrals involving the generating functions F and F‹. We begin with F‹, for which the subsequent analysis is a little simpler. For any y > 0, the analogues of (3.6) and (3.7) for an and bn are

- (5.23) an(r) =

iy

−1+iy

Ä

F‹(τ,r) − τ F ‹(τ + 1,r) − F‹(τ,r)

ä

e−2πinτ dτ and

- (5.24) bn(r) =

1 2πi√2n

iy

−1+iy

F ‹(τ + 1,r) − F‹(τ,r) e−2πinτ dτ. Now we use the identity (5.2), i.e.,

- (5.25) F‹(τ,r) = 4sin πr2/2 2

∞

0

K(τ,it)e−πr2t dt,

which holds for τ ∈ D and |r| suﬃciently large (speciﬁcally, r2 > 0 when d = 8 and r2 > 2 when d = 24). We would like to use the formulas

- (5.26) αn(z) =

iy

−1+iy

Ä

K(τ,z) − τ K(τ + 1,z) − K(τ,z)

ä

e−2πinτ dτ and

- (5.27) βn(z) =


iy

1 2πi√2n

K(τ + 1,z) − K(τ,z) e−2πinτ dτ,

−1+iy

−1 + iy iy

z − 1 z

−1 + i i

Figure 5.5. Contour shift when Im(z) > 1.

which hold for suﬃciently large y (depending on z) because of the series expansions (5.20) and (5.21). Before we can use these formulas, we must check whether there is a single choice of y that works for all z on the imaginary axis. Fortunately, any y ≥ 1 will work. Speciﬁcally, it follows from the residue formulas in part (3) of Theorem 4.3 that τ  → K(τ,z) has no poles at z, −1/z, z±1, or −1/z±1. In particular, if z is on the imaginary axis, then this function is holomorphic for Im(τ) ≥ 1 and −1 ≤ Re(τ) ≤ 1. Therefore the contour integral of the integrands in (5.26) and (5.27) around the rectangle with vertex set {−1 + iy, iy, iy , −1 + iy } is zero for any y,y ≥ 1. The contributions from the vertical sides cancel since the integrand is invariant under τ  → τ + 1, which proves that the integrals in (5.26) and (5.27) are independent of y as long as y ≥ 1.

Now we substitute (5.25) into (5.23) and (5.24) for an arbitrary choice of y ≥ 1. By the Fubini-Tonelli theorem we can interchange the order of integration. (To prove absolute convergence of the iterated integral, we can use inequalities (4.40) and (4.41) from Lemma 4.11 with γ = I to obtain bounds on the integrand as t → 0 or t → ∞ that are uniform in τ. Again we need r2 > 0 when d = 8 and r2 > 2 when d = 24, because of the behavior of G±(d) in these cases.) When we do so and apply (5.26) and (5.27), we arrive at the desired formulas for an and bn in terms of αn and βn.

The case of an and bn involves two complications. The function τ  → K(τ,z) has no poles at z, −1/z, or −1/z ± 1, but it has poles at z + 1 and z − 1 with residues −1/(2π) and 1/(2π), respectively. Furthermore, we must account for the eπiτr2 term in (5.1), which says that

- (5.28) F(τ,r) = eπiτr2 + 4sin πr2/2 2


∞

K(τ,it)e−πr2t dt,

0

as long as τ ∈ D and r satisﬁes r2 > 0 when d = 8 and r2 > 2 when d = 24. The eπiτr2 term will turn out to cancel the contributions from the poles.

We begin by analyzing the eﬀects of the poles. As above,

iy

K(τ,z) − τ K(τ + 1,z) − K(τ,z) e−2πinτ dτ and

αn(z) =

−1+iy

iy

1 2πi√2n

K(τ + 1,z) − K(τ,z) e−2πinτ dτ

βn(z) =

−1+iy

when z is on the imaginary axis and y is suﬃciently large. If Im(z) < 1, then we can shift the contour in these integrals for αn and βn to y = 1, as in the case of αn and βn, because the integrand is holomorphic (since τ  → K(τ,z) has no poles at −1/z and −1/z ± 1). We may and shall ignore the case of z = i, since it has measure zero in the integrals for an and bn and the integrand is not singular there. If Im(z) > 1, then the integrand has poles at z − 1 and z. If we shift the contour to y = 1 by passing to the right of these poles, as in Figure 5.5, then this contour shift contributes a residue from integrating the terms involving K(τ + 1,z) clockwise around the pole at z. Thus, we obtain the formulas

i

K(τ,z) − τ K(τ + 1,z) − K(τ,z) e−2πinτ dτ and

αn(z) = −iz e−2πinz +

−1+i

Ç

å

i

1 2πi√2n

ie−2πinz +

K(τ + 1,z) − K(τ,z) e−2πinτ dτ

βn(z) =

−1+i

for Im(z) > 1 (note that the terms coming from the poles are the dominant terms in the ﬁrst two asymptotic expansions listed in (5.22)).

Now substituting (5.28) into (3.6) and (3.7) and interchanging the order of integration yields

Ä

Ä

ää

i

eπiτr2 − τ

eπi(τ+1)r2 − eπiτr2

e−2πinτ dτ

an(r) =

−1+i

1

+ 4sin πr2/2 2

αn(it)e−πr2t dt

0

∞

+ 4sin πr2/2 2

αn(it) − te2πnt e−πr2t dt and

1

#### Ä

ä

i

1 2πi√2n

eπi(τ+1)r2 − eπiτr2

e−2πinτ dτ

bn(r) =

−1+i

1

+ 4sin πr2/2 2

βn(it)e−πr2t dt

0

ã

Å

∞

e2πnt 2π√2n

+ 4sin πr2/2 2

e−πr2t dt.

βn(it) −

1

As above, the estimates (4.40) and (4.41) imply absolute convergence for the original integrals, and then the Fubini-Tonelli theorem shows that the interchanged integrals converge absolutely and the interchange is justiﬁed, as long as r satisﬁes r2 > 0 when d = 8 and r2 > 2 when d = 24, to justify the application of (5.28). If furthermore r2 > 2n, then t  → αn(it)e−πr2t and t  → βn(it)e−πr2t are integrable over [1,∞), because the equations

αn(it)e−πr2t = αn(it) − te2πnt e−πr2t + te−π(r2−2n)t and

Å

ã

e−π(r2−2n)t 2π√2n express them as the sum of integrable functions. Thus,

e2πnt 2π√2n

βn(it)e−πr2t =

e−πr2t +

βn(it) −

∞

∞

∞

αn(it) − te2πnt e−πr2t dt =

αn(it)e−πr2t dt −

te−π(r2−2n)t dt

1

1

1

and

Å

ã

e−π(r2−2n)t 2π√2n

∞

∞

∞

e2πnt 2π√2n

e−πr2t dt =

βn(it)e−πr2t dt −

βn(it) −

dt.

1

1

1

All the extraneous terms not involving αn or βn cancel, and we obtain the desired formulas for an and bn.

### 6. Positivity of kernels and universal optimality

6.1. Sharp bounds for energy. In this section we will prove that E8 and the Leech lattice are universally optimal (Theorem 1.4). Let d be 8 or 24, with Λd being the corresponding lattice and F the generating function from Theorem 3.1. The key inequality is the following proposition:

Proposition 6.1. Suppose Re(τ) = 0 and r > 0. Then F‹(τ,r) ≥ 0, with equality if and only if r2 is an even integer and r2 ≥ 2n0, where n0 = 1 if d = 8

- and n0 = 2 if d = 24.


The rest of this section is devoted to proving Proposition 6.1, but ﬁrst we show in this subsection that it implies universal optimality.

Lemma 6.2. For α > 0, the function f : Rd → R deﬁned by f(x) = F(iα/π,x) is a Schwartz function and satisﬁes the inequalities f(x) ≤ e−α|x|2 and f(x) ≥ 0 for all x ∈ Rd. When x = 0, equality holds if and only if |x| is the length of a nonzero vector in Λd.

In fact, equality does not hold when x = 0 either. That follows from (6.1) below, but we will not need it.

Proof. This function is a Schwartz function since F satisﬁes condition (3) from Theorem 3.1, so the substantive content of the lemma is the inequalities. The second inequality follows directly from Proposition 6.1, because f(x) = F‹(iα/π,x) (as shown at the end of Section 5.3). To prove that f(x) ≤ e−α|x|2, we use the functional equation F(τ,x) + (i/τ)d/2F‹(−1/τ,x) = eπiτ|x|2 with τ = iα/π to obtain

e−α|x|2 − f(x) = (π/α)d/2F‹(iπ/α,x).

Thus, the ﬁrst inequality amounts to Proposition 6.1 as well, as do the conditions for equality.

Although the inequalities f(x) ≤ e−α|x|2 and f(x) ≥ 0 look diﬀerent, the preceding proof derives them from the same underlying inequality. More generally, Cohn and Miller [17, Section 6] observed a duality principle when the potential function p is a Schwartz function: the auxiliary function f proves a bound for p-energy in Proposition 1.6 if and only if p − f proves a bound for penergy, and this transformation interchanges the two inequalities. Furthermore, a lattice Λ attains the p-energy bound proved by f if and only if Λ∗ attains the p-energy bound proved by p − f.

It follows immediately from Lemma 6.2 that Λd minimizes energy for all Gaussian potential functions (recall the conditions (1.2) for equality in the linear programming bounds). Furthermore, we can prove uniqueness among periodic conﬁgurations under Gaussian potential functions as follows. If C is any periodic conﬁguration in Rd of density 1 with the same energy as Λd under some Gaussian, then the distances between points in C must be a subset of those in Λd, because of the equality conditions. Without loss of generality we can assume 0 ∈ C. Then, by [12, Lemma 8.2], C is contained in an even integral lattice (namely, the subgroup of Rd generated by C), because all the distances between points in C are square roots of even integers. Because C has density 1, it must be the entire lattice. We conclude that it must be isometric to Λd, because there is only one such lattice with minimal vector length √2n0 (see [18, Chapters 16 and 18]). Thus, Theorem 1.4 holds for Gaussian potential functions.

Handling other potential functions via linear programming bounds is slightly more technical, because the potential function might decrease too slowly for any Schwartz function to interpolate its values. For example, no Schwartz function can directly prove a sharp bound for energy under an inverse power law potential in Proposition 1.6. Nevertheless, we will show that Schwartz functions come arbitrarily close to a sharp bound. Suppose we are using a completely monotonic function of squared distance p: (0,∞) → R. By Bernstein’s theorem

[48, Theorem 9.16], there is some measure µ on [0,∞) such that p(r) = e−αr2 dµ(α)

for all r ∈ (0,∞) (which implies that µ must be locally ﬁnite). Without loss of generality we can assume µ({0}) = 0, since otherwise all conﬁgurations of density 1 have inﬁnite energy. We would like to use

f(x) = F(iα/π,x)dµ(α)

as an auxiliary function for the potential function p, and it might plausibly work under the weaker hypotheses for linear programming bounds proved in [11, Proposition 2.2]. However, it will not be a Schwartz function in general, and we will not analyze the behavior of this integral. Instead, let

1/ε

F(iα/π,x)dµ(α), which deﬁnes a Schwartz function for each ε > 0 because F satisﬁes condition (3)

fε(x) =

ε

- of Theorem 3.1. Then


1/ε

f“ε(y) =

F‹(iα/π,y)dµ(α),

ε

and the inequalities fε(x) ≤ p |x| for all x ∈ Rd \ {0} and f“ε(y) ≥ 0 for all y ∈ Rd follow from Lemma 6.2. Thus, every conﬁguration in Rd of density 1 has lower p-energy at least f“ε(0) − fε(0), by Proposition 1.6. Because of the sharp bound for each α,

1/ε

f“ε(0) − fε(0) =

Er →e−αr2(Λd)dµ(α)

ε

1/ε

e−α|x|2 dµ(α)

=

ε x∈Λd\{0}

1/ε

e−α|x|2 dµ(α).

=

ε

x∈Λd\{0}

As ε → 0, this bound converges to the p-energy of Λd by monotone convergence since µ({0}) = 0, and we conclude that Λd has minimal p-energy.

Uniqueness among periodic conﬁgurations also follows from Bernstein’s theorem. Suppose C is any periodic conﬁguration of density 1 that is not isometric to Λd. We have seen that the energy of C under r  → e−αr2 is strictly greater than that of Λd for each α > 0, and these energies are continuous functions of α by (1.1). By continuity, for each compact subinterval I of (0,∞), there exists ε > 0 such that the energy gap between C and Λd is at least ε for all α ∈ I. Thus, Bernstein’s theorem and monotone convergence show

that Ep(C) ≥ Ep(Λd) + δ for some δ > 0. In particular, Ep(C) > Ep(Λd) if Ep(Λd) < ∞, as desired. This completes the proof of Theorem 1.4, except for proving Proposition 6.1.

In addition to proving universal optimality, our construction also establishes other properties of the optimal auxiliary functions. For example, the following proposition follows directly from (5.1), (5.3), and (5.4) for τ ∈ D, and for all τ ∈ H by analytic continuation:

Proposition 6.3. For all τ ∈ H and d ∈ {8,24},

F(τ,0) = 1 + iG0,1(τ), F τ,

√

2 = e2πiτ + iG−1,1(τ), ∂2

F(τ,r) = 2πiτ + 2π G0,0(τ), and ∂

∂r2 r=0

√

√

2e2πiτ + 2π

2G−1,0(τ).

F(τ,r) = 2πi

∂r r=√2

Equivalently, the proposition speciﬁes these values and derivatives of the interpolation basis functions. It gives another interpretation of the non-decaying asymptotics Gk,j of the kernel K, and it generalizes the computation of special values of the optimal sphere packing auxiliary functions in [53, Propositions 4 and 8] and [15, Sections 2 and 3].

If one computes F‹(τ,0) using Proposition 6.3 and the functional equation relating F and F‹, one obtains τ times an explicit quasimodular form. Using the theta series for Λd and Ramanujan’s derivative formulas for modular forms [57, Section 5], a straightforward calculation shows that

2πiτ d x∈Λ

- (6.1) F‹(τ,0) = −


|x|2eπi|x|2τ.

d

Equivalently, if f is the auxiliary function from Lemma 6.2 for the potential function r  → e−αr2 (corresponding to τ = iα/π in the formula above), then

2α d

Er →r2e−αr2(Λd), in agreement with the prediction in [17, Conjecture 6.1].

f(0) =

6.2. Reduction to positivity of kernels. To complete the proof of universal optimality, all that remains is to prove Proposition 6.1, i.e., the inequality F‹(τ,r) ≥ 0 and the conditions for equality. For the rest of the section we thus assume Re(τ) = 0 (in particular, τ ∈ D).

The ﬁrst obstacle to proving that F‹(τ,r) ≥ 0 is dealing with the integral transform that deﬁnes F‹ in terms of the kernel K. The kernel is written

explicitly in terms of well-known special functions, and we will deduce the positivity of the integral at the level of the kernel itself. As in the sphere packing papers [53] and [15], that will involve additional complications for d = 24 beyond those that occur in the case of d = 8.

Speciﬁcally, recall from (5.2) that

∞

- (6.2) F‹(τ,r) = 4sin πr2/2 2


K(τ,it)e−πr2t dt,

0

which is absolutely convergent for τ ∈ D and |r| suﬃciently large, and has an analytic continuation to r in some open neighborhood of R in C. We showed in Section 5.1 that this continuation of (6.2) can be achieved by subtracting pieces of the asymptotics of K(τ,it) as t → ∞, as in (5.3) and (5.4). Since Proposition 6.1 does not involve the point r = 0, here it suﬃces to perform a milder truncation by subtracting only the k = −1 terms in (4.38), and only for dimension d = 24, since for d = 8 the k = −1 terms vanish and the integral in

- (6.2) is absolutely convergent for all r > 0. When d = 8, our strategy for proving Proposition 6.1 is to show that

- K(8)(τ,it) > 0, which immediately implies both the desired inequality and the equality conditions. The analogous inequality K(24)(τ,it) > 0 for d = 24 holds


- as well, but additional work is needed to deal with small r. Speciﬁcally, we write K(24)(τ,it) = E(τ,it) + O(t) as t → ∞, where


E(τ,z) =

e−2πiz 3456π

(z E1(τ) + E0(τ)) and Ej(τ) = τ Ej,1(τ) + Ej,0(τ), with

- E0,0 = −6912log(2)∆ − 36E2E4E6 + 16E43 + 20E62 + 108E4

√

∆(V L + WLS),

- E0,1 = −πi 6E22E4E6 − 5E2E43 − 7E2E62 + 6E42E6 ,


- E1,0 = 12πi −E2E4E6 + E62 + 720∆ , and
- E1,1 = 2π2 E22E4E6 − 2E2E62 − 1728E2∆ + E42E6


expressed in terms of quasimodular forms, L, and LS.

For d = 24 the integral in (6.2) converges absolutely for |r| > √2. For the range 0 < |r| ≤

√2 we will use the truncation method from [15], by instead setting p = 1.01 and writing

∞

0

K(24)(τ,it)e−πr2t dt =

∞

0

Ktrunc(τ,it)e−πr2t dt +

∞

p

E(τ,it)e−πr2t dt,

where

- (6.3) Ktrunc(τ,it) =


®

K(24)(τ,it) for t < p, and K(24)(τ,it) − E(τ,it) for t ≥ p.

The value of p has been chosen to ensure the positivity properties below, in particular so that λ(ip) < 0.49, where λ is the modular function from Section 2.1.3 (for comparison, λ(i) = 1/2). The last integral in (6.3) can be evaluated as

∞

it E1(τ) + E0(τ) 3456π

eπ(2−r2)t dt = e−pπ(r2−2) (r2 − 2)2 ·

p

E0(τ)π(r2 − 2) + i E1(τ)(1 + pπ(r2 − 2)) 3456π3

.

The singularities from the factor of (r2−2)2 in the denominator are compensated for by the vanishing of the sin πr2/2 2 factor in (6.2). Because n0 = 2 and sin πr2/2 2 vanishes at other r2 ∈ 2Z, we deduce that Proposition 6.1 is a consequence of the following three statements for Re(τ) = 0 and t ∈ (0,∞):

- (1) K(d)(τ,it) > 0 for d ∈ {8,24},
- (2) Ktrunc(τ,it) > 0 for t ≥ p, and
- (3) E0(τ)π(r2 − 2) + i E1(τ)(1 + pπ(r2 − 2)) > 0 for r ≤


- (6.4) √


2. Statement (3) is itself a consequence of

- (3a) E0(τ) + ip E1(τ) < 0, and
- (3b) i E1(τ) > 0.


We have no simple proof of these inequalities, but we will outline below how we have proved them by mathematically rigorous computer calculations.

Proving inequalities of this sort for quasimodular forms also arose in the sphere packing papers [53] and [15], but the computations are much more challenging in our case. In the sphere packing cases, all that was needed was to prove positivity for relatively simple functions of a single variable. Asymptotic calculations reduce the proof to analyzing functions on compact intervals, and that is a straightforward and manageable computation using any of several techniques ([53] used interval arithmetic and [15] used q-expansions).

By contrast, inequalities (1) and (2) in (6.4) involve much more complicated functions of two variables. We must analyze singularities along curves, which are more subtle than the point singularities in one dimension. Furthermore, these curves intersect, and the intersection points are particularly troublesome. In the rest of this section we explain how to overcome these obstacles.

Inequalities (3a) and (3b) involve only a single variable τ, and can be veriﬁed using the methods from [15, Appendix A], or the λ function coordinates that we use below for the other inequalities. We thus focus on inequalities (1) and (2), describing the underlying mathematical ideas that were rigorously veriﬁed by a computer calculation.

6.3. Passing to the unit square. Recall from Section 2.1.3 that t  → λ(it) is a decreasing function mapping (0,∞) onto (0,1). Our ﬁrst step is to express the kernels K(d) and Ktrunc in terms of functions on the interior of the unit square by inverting the map (τ,z)  → (λ(τ),λ(z)). Rewriting the kernels in this way is not logically necessary, but it has the advantage of expressing everything in terms of a small number of functions that can be bounded systematically and eﬃciently, and we can take advantage of relationships between these functions to obtain more accurate estimates when proving bounds.

Speciﬁcally, if we use the identities (2.12), (2.20), (2.21), and (2.22) to write modular forms, z, τ, and E2 in terms of λ and write L = log(λ) and LS = log(1 − λ) on the imaginary axis, we obtain functions L(d) and Ltrunc on (0,1) × (0,1) such that

K(d)(τ,z) = L(d)(λ(τ),λ(z)) and Ktrunc(τ,z) = Ltrunc(λ(τ),λ(z))

when Re(τ) = Re(z) = 0. The resulting functions L(d)(x,y) are rational functions of x, y, and the logarithms and complete elliptic integrals of x, 1 − x, y, and 1 − y, while Ltrunc is slightly more complicated, as described below.

The inequalities (1) and (2) in (6.4) thus transform into the assertions that

L(d)(x,y) > 0 for 0 < x,y < 1 and d = 8 or 24, and that

Ltrunc(x,y) = L(24)(x,y) − ψtrunc(x,y) > 0

- for 0 < x < 1 and 0 < y < 0.49, where ψtrunc(λ(τ),λ(z)) = E(τ,z) by (6.3) and the constant 0.49 is just slightly larger than λ(ip) = λ(1.01i) = 0.4891135.... One complication with Ltrunc is that E(τ,z) involves a factor of e−2πiz, which becomes e2πK(1−y)/K(y) by (2.21) when we set y = λ(z). We write


ψtrunc(x,y) = e2πK(1−y)/K(y) ψtrunc(x,y), where ψtrunc(λ(τ),λ(z)) = (z E1(τ) + E0(τ))/(3456π). Observe that Ltrunc(x,y) ≥ L(24)(x,y) whenever ψtrunc(x,y) ≤ 0, and otherwise Ltrunc(x,y) is bounded below by Ltrunc(x,y) := L(24)(x,y) −

ã

Å

4 · 109 970299

256 y

256 y2 −

y2

ψtrunc(x,y)

+ 24 +

according to (6.5) below. In particular, inequality (1) in (6.4) and the positivity of Ltrunc(x,y) for 0 < x < 1 and 0 < y < 0.49 together imply inequality (2).

The lower bound used above can be obtained by truncating the Taylor series of e2πK(1−y)/K(y) and bounding the omitted coeﬃcients. It is most convenient to obtain such bounds via complex analysis. For example, the functions Aj(z) in (2.23), along with E(z), K(z), and log(1−z), all have modulus bounded by 5 on {z ∈ C : |z| = 0.99}, and so their Taylor series coeﬃcients of zn are bounded

above by 5 · 0.99−n. (This bound of 5, which is easily improved for some of these individual functions, comes from the constant sign of the coeﬃcients of zn for n > 1 and the value at z = 0.99.) For the bound needed above, one can check that z2e2πK(1−z)/K(z) is holomorphic on the open unit disk and

256 y2 −

- (6.5) e2πK(1−y)/K(y) ≤


4 · 109 970299

256 y

y2

+ 24 +

- for 0 < y < 1/2, where the error term comes from the bound |K(z)| ≥ 1.3 for |z| = 0.99 (which itself can be shown by evaluation at close points on the circle and derivative bounds).


The next several subsections describe the veriﬁcation of inequalities (1) and (2) in (6.4). The primary diﬃculty is dealing with singularities. Since our formulas for the kernels involve denominators of j(τ)−j(z), which vanish when τ = z or τ = −1/z, our formulas for L(d)(x,y) and Ltrunc(x,y) naively yield 0/0 when x = y or x = 1 − y. The kernels themselves are not actually singular along these lines, because φ(I) = φ(S) = 0 in the residue formulas from part (3)

- of Theorem 4.3, but in practice we must treat the diagonal lines x = y and x = 1 − y as singularities in the formulas. In addition, there are singularities


- at the edges of the unit square coming from (2.23). In this rest of this section, we describe the methods used to treat these singularities, starting away from any singularities and working our way up to the most singular points: the four corners of the unit square, at which three singularities meet.


In our numerical calculations, it is convenient to remove obviously positive factors from L(d)(x,y) and Ltrunc(x,y). To do so, we multiply each of them by

1 − xy 1 − x(1 − y) 1 − y(1 − x) 1 − (1 − x)(1 − y) , and we furthermore multiply L(8)(x,y) by

π4K(y)2K(1 − x) K(x)4

,

- L(24)(x,y) by


6π4y2(1 − y)2K(y)10K(1 − x) K(x)12

,

and Ltrunc(x,y) by

54π14y2(1 − y)2K(y)12 K(x)11

.

For simplicity of notation, in the remainder of Section 6 we use the notation L(d)(x,y) and Ltrunc(x,y) to refer to the functions after removing these factors.

6.4. Interval bounds for elliptic integrals. Away from all singularities it is possible to prove positivity via interval arithmetic estimates on L(d)(x,y) and Ltrunc(x,y). Interval arithmetic provides rigorous upper and lower bounds on the values of a function over a given interval (see, for example, [37]). It works beautifully for small intervals and well-behaved functions, but the bounds become much less tight for large intervals or near singularities. In practice, instead of simply subdividing intervals to improve the bounds, we obtained better results by using interval arithmetic to evaluate Taylor series expansions, while controlling the error terms by using crude interval arithmetic bounds on partial derivatives, because these error bounds do not need to be tight.

Interval arithmetic for polynomials and logarithms is standard and is part of many software packages. We will next describe how to obtain rigorous interval bounds for the complete elliptic integrals E and K by adapting the arithmetic-geometric mean algorithms for computing them from [4, Chapter 1]. Consider the sequences (an)n≥0 and (bn)n≥0 with a0 ≥ b0 > 0 and

an + bn 2

and bn+1 = anbn. Then bn ≤ bn+1 ≤ an+1 ≤ an and both an and bn converge to the same limit

an+1 =

- M(a0,b0) (the arithmetic-geometric mean of a0 and b0), which is related to the complete elliptic integral K by


π 2M 1,√1 − x

K(x) =

for 0 < x < 1. Since the interval [bn,an] contains M(a0,b0), these recurrences give a fast interval-arithmetic algorithm for K.

Computations of E are more subtle and use the formula

E(x) K(x)

2n−1c2n

= 1 −

- (6.6)


n≥0

from [4, Algorithm 1.2], where c0 = √x and cn+1 =

an − bn 2

with an and bn deﬁned as above, starting with (a0,b0) = 1,√1 − x ; one can show that cn+1 = c2n/(4an+1), which avoids potential precision loss from subtracting an and bn. Since

an−1 − bn−1 2 ≤

an−1

2 ≤ an ≤ 2an+1, we have

cn =

c2n 4an+1 ≤

cn 2

cn+1 =

,

#### and therefore the tail of the series is

2n−1c2n ≤

n>m

2n−1(2m+1−ncm+1)2 = 2m+1c2m+1.

n>m

From this tail bound, truncating the series in (6.6) yields interval bounds for the ratio E(x)/K(x), and hence E(x) itself in light of the algorithm for K(x) above.

6.5. Near the diagonals and their crossing. After removing factors that are obviously positive as discussed above, the kernels L(d)(x,y) and Ltrunc(x,y) have denominator (x − y)(1 − x − y), and numerators that vanish at x = y and x = 1 − y, as they must in order to be well deﬁned on the interior of the unit square. We use Taylor expansions in one of the variables (along with rigorous interval bounds on partial derivatives, which are themselves expressible in terms of polynomials, logarithms, E, and K) to prove that the kernels are positive near the diagonals. For this purpose it is convenient to work with the coordinate system (u,v) = (x − y,1 − x − y) and take partial derivatives in u and v.

The most subtle point is the diagonal crossing point (x,y) = (12, 12). There both u = x − y and v = 1 − x − y vanish, and so L(d)(x,y) and Ltrunc(x,y) can each be written in the form f(uvu,v), where f(u,0) = f(0,v) = 0 for all u and v. To analyze these functions, we obtain bounds on their Taylor series coeﬃcients by writing

1

1

f(u,v) uv

f(1,1)(us,vt)dsdt, where f(i,j)(u,v) denotes (∂i/∂ui)(∂j/∂vj)f(u,v), and hence

=

0

0

1

1

∂i ∂ui

∂j ∂vj

f(u,v) uv

sitjf(i+1,j+1)(us,vt)dsdt. It follows that

=

0

0

max0≤s,t≤1 f(i+1,j+1)(us,vt) (i + 1)(j + 1)

∂i ∂ui

∂j ∂vj

f(u,v) uv ≤

.

Interval arithmetic bounds on the derivatives then gives rigorous upper bounds on the error terms in the Taylor expansion, which can be used to show positivity close to (x,y) = (21, 12).

- 6.6. Near the edges. For the rest of this section, we reduce to the situation


of 0 < x,y ≤ 12 by changing coordinates from x to 1 − x and from y to 1 − y

- as needed. The singularities at the edges come from logarithms as well as the logarithmic behavior of the elliptic integrals E(z) and K(z) near z = 1 from (2.23). After substituting those formulas for E and K, we arrive at a sum of powers of logarithms times holomorphic functions. We compute Taylor


series for these holomorphic functions in the direction orthogonal to the edge in question, and use interval arithmetic in the tangential direction, while taking into account the Taylor coeﬃcient bounds for special functions mentioned in the paragraph containing (6.5). On narrow strips near the edges we obtain a lower bound for L(d)(x,y) and Ltrunc(x,y) as a linear or quadratic polynomial in the logarithm that is responsible for the singularity, whose positivity is straightforward to verify (e.g., using Sturm’s theorem or interval arithmetic).

- 6.7. The corners. The corners are intersections of three distinct singular


curves. As in Section 6.6, we change coordinates if necessary so that the corner is at (x,y) = (0,0). After substituting the formulas in (2.23), we obtain expressions for L(d)(x,y) and Ltrunc(x,y) of the form

- (6.7) H(x,y) =

1 x − y i,j≥0

hi,j(x,y)log(x)i log(y)j,

where the sum contains only ﬁnitely many terms and each coeﬃcient function hi,j(x,y) is holomorphic in {x ∈ C : |x| < 1} × {y ∈ C : |y| < 1}. In particular, these coeﬃcient functions can be written in terms of log(1 − u), E(u), K(u), and the functions Aj(u) from (2.23) for u = x and u = y.

Since the kernel H(x,y) is well deﬁned on the diagonal, the sum in (6.7) must vanish there, but the individual coeﬃcients hi,j(x,y) might not. To remedy this, we choose β ∈ Z and write

- (6.8)


H(x,y) =

i,j≥0

+

hi,j(x,y) x − y

log(x)i log(y)j

log(x)i log(y)j x − y

y x

β

,

hi,j(x,x)

i,j

with

hi,j(x,y) = hi,j(x,y) −

y x

β

hi,j(x,x),

so that hi,j(x,x) = 0 and therefore hi,j(x,y)/(x − y) is holomorphic at x = y. This procedure is required in only one corner for L(8)(x,y) and L(24)(x,y) (with β = 0), and one corner of Ltrunc(x,y) (with β = 2, in order to obtain better estimates).

Each function hi,j(x,y) has a Taylor series expansion n,m≥0 bn,mxnym that vanishes on the diagonal. In other words,

#### bn,mynym = 0,

n,m≥0

and therefore hi,j(x,y) x − y

xnym − ynym x − y

bn,m(xn−1+xn−2y+···+yn−1)ym

bn,m

=

=

n,m≥0

n,m≥0

gives a series expansion of this ratio. The individual coeﬃcients bn,m can be computed from the Taylor series of log(1 − z), E(z), K(z), and Aj(z), while at the same time the 5 · 0.99−n bound on the Taylor coeﬃcients of these special functions gives an upper bound on all bn,m. Computing a ﬁnite number of coeﬃcients explicitly and using this upper bound on the rest, we obtain a rigorous lower bound on the ﬁrst sum in (6.8).

When hi,j(x,x) is nonzero, direct computations show that it has a fairly simple form, from which its positivity for small values of x is manifest. For example, Ltrunc(x,y) has hi,j(x,x) nonzero only for one corner and two choices of indices (i,j), where it equals

(2 − x)(x − 1)4(x + 1)(1 − 2x)(x2 − x + 1)2K(x)2

up to a positive constant factor (as well as the obviously positive factors that were removed from L(d) and Ltrunc earlier, as mentioned above). Similar, and in fact simpler, formulas hold in all other cases, and direct computation shows that the second sum in (6.8), namely

log(x)i log(y)j x − y

hi,j(x,x)

,

i,j

can be rewritten as (log(y) − log(x))/(y − x) times an explicit, manifestly positive holomorphic function d(x,y). From this we obtain a rigorous lower bound for H(x,y) for 0 < x,y ≤ 21, of the form

log(y) − log(x) y − x

pi,j(x,y)log(x)i log(y)j + d(x,y)

- (6.9) i,j


with pi,j(x,y) ∈ R[x,y] coming from the Taylor series argument above. The coeﬃcient functions pi,j(x,y) and d(x,y) can all be approximated well on small regions using interval arithmetic, as can the quotient (log(y) − log(x))/(y − x). To obtain the positivity as both x and y approach zero, we found it eﬃcient in situations where d(x,y) vanishes identically and pi,j(0,0) = 0 to deduce lower bounds on (6.9) and similar expressions via lower bounds on gradients, for which interval arithmetic had better behavior. These arguments complete the proof of Proposition 6.1, and thus Theorem 1.4.

6.8. Computer implementation. Code to prove the inequalities needed for Proposition 6.1 is available from the MIT Libraries at https://hdl.handle. net/1721.1/141226. We provide two implementations, one via Mathematica notebooks [55] and the other via Sage code [49].

The Mathematica notebooks closely follow the techniques we have outlined in this section. They run for about a week on a 16-core server. Documentation is included in the notebooks, and we provide a README ﬁle that gives an overview of how to use the notebooks.

The Sage code is a revised and optimized version of the proof. The fundamental approach to treating the diagonals, edges, and corners remains the same, but instead of using the arithmetic-geometric mean algorithm from Section 6.4 to compute elliptic integrals, we instead expand all the functions we use as multivariate power series and derive bounds for the error introduced by truncation. These techniques and bounds are explained in the documentation provided with the code. The resulting calculations ﬁnish in less than an hour on a single core.

### 7. Generalizations and open questions

Theorem 1.7 is ideally suited to proving universal optimality for E8 and the Leech lattice, but the underlying analytic phenomena are not limited to 8 and 24 dimensions. Instead, it seems that the remarkable aspect of these dimensions is the existence of the lattices, while interpolation theorems may hold much more broadly.

Open Problem 7.1. Let d and k be positive integers. If f ∈ Srad(Rd) satisﬁes f(j)

√

√

kn = f (j)

kn = 0 for all integers n ≥ 0 and 0 ≤ j < k, then must f vanish identically?

The answer is yes when k = d = 1 by [40, Corollary 1], and it follows for k = 1 and all dimensions using the techniques of [40] without much diﬃculty. It also holds when (d,k) = (8,2) or (d,k) = (24,2) by Theorem 1.7, and likely holds more broadly for k = 2. As far as we know, interpolation theorems of this form would not lead to any optimality theorems in packing or energy minimization beyond E8 and the Leech lattice.

The special nature of the interpolation points √2n plays an essential role in our proofs. For example, the functional equations

F(τ + 2,x) − 2F(τ + 1,x) + F(τ,x) = 0 and

F‹(τ + 2,x) − 2F‹(τ + 1,x) + F‹(τ,x) = 0

encode algebraic properties of √2n, without which we would be unable to construct the interpolation basis. This framework (i.e., Theorem 3.1) generalizes naturally to the interpolation points

√

kn from Open Problem 7.1, with the corresponding functional equations using a k-th diﬀerence operator in τ. However, our methods cannot apply to k > 2 without serious modiﬁcation.

There is no reason why interpolation theorems should be restricted to radii that are square roots of integers. We expect that far more is true, at the cost of giving up the algebraic structure behind our proofs. In particular, optimizing the linear programming bound for Gaussian energy seems to lead to interpolation formulas, except in low dimensions. Recall that the optimal functions for linear programming bounds seem to work as speciﬁed by the following conjecture, which is a variant of [12, Section 7] and [14, Section 9]:

Conjecture 7.2. Fix a dimension d ≥ 3, density ρ = 1, and α > 0. Then the optimal linear programming bound f(0) − f(0) from Proposition 1.6 for the potential p(r) = e−αr2 is achieved by some radial Schwartz function f, the radii |x| for which f(x) = e−α|x|2 are the same as the radii |y| for which f(y) = 0, they form a discrete, inﬁnite set, and these radii do not depend on α.

Note that at least one implication holds among the assertions of this conjecture: the radii at which f(x) = e−α|x|2 must be the same as those for which f(y) = 0 if all these radii are independent of α, thanks to the duality symmetry from [17, Section 6].

Open Problem 7.3. Let r1,r2,... be the radii from Conjecture 7.2 for some d. For which d is every f ∈ Srad(Rd) uniquely determined by the values f(rn), f (rn), f(rn), and f (rn) for n ≥ 1 through an interpolation formula?

Numerically constructing the interpolation basis seems to work about as well for general d ≥ 3 as it does for d = 8 or d = 24, which suggests that interpolation holds for many or even all such d. In particular, simple variants of the algorithms from [12] and [13] yield interpolation formulas of this sort for all functions of the form x  → p(|x|2)e−π|x|2, where p is a polynomial of degree

- at most some bound N. As N grows, these interpolation formulas seem to converge to well-behaved limits when d ≥ 3.


From an interpolation perspective, the numerical evidence suggests that these dimensions behave much like d = 8 and d = 24. On the other hand, we know of no simple description of the interpolation points r1,r2,... when d  ∈ {8,24}, and we are not aware of any point conﬁgurations in Rd that meet the optimal linear programming bounds in these cases. In other words, d = 8 and d = 24 diﬀer both algebraically and geometrically from the other dimensions.

When d ≤ 2, universally optimal conﬁgurations exist (conjecturally for d = 2), but the radii r1,r2,... are more sparsely spaced, seemingly too much so to allow for an interpolation theorem. For d = 1, we can in fact rule out an interpolation theorem corresponding to the point conﬁguration Z:

Lemma 7.4. Radial Schwartz functions f : R → R are not uniquely determined by the values f(n), f (n), f(n), and f (n) for integers n ≥ 1.

This lemma follows immediately from [40, Theorem 2], but for completeness we will give a simpler, direct proof.

Proof. Let t be the tent function

t(x) =

1 − |x| if |x| ≤ 1, and 0 otherwise.

Then

Å

ã2

sinπy πy

t(y) =

,

which vanishes to second order at all nonzero integers. Now let b be any even, smooth, nonnegative function with support contained in [−12, 12], and consider the convolution f = b ∗ t. This function is smooth and compactly supported, and it is therefore a Schwartz function, whose Fourier transform f = b t again vanishes to second order at all nonzero integers. Furthermore, f vanishes to inﬁnite order at all nonzero integers other than ±1, because its support is contained in [−3/2,3/2]. If the interpolation property in the lemma statement held, then f would be uniquely determined by f(1) and f (1). In other words, there would be just a two-dimensional space of functions of this form. Furthermore, those two dimensions would have to correspond to the support of f and scalar multiplication. Thus, f would be completely determined by the support and total integral of b. However, that is manifestly false: the value

1

b(x)(1 − |x|)dx is not determined by the support and integral of b.

f(0) =

−1

The two-dimensional case is more diﬃcult to analyze. If we scale the hexagonal lattice so that it has density 1, then the distances between the lattice points are given by

(4/3)1/4 j2 + jk + k2, where j and k range over the integers. Bernays [2] proved that as N → ∞, the number of such distances between 0 and N (counted without multiplicity) is asymptotic to

CN2 √log N for some positive constant C. Thus, the distances in the hexagonal lattice are slightly sparser than those in E8 or the Leech lattice, for which the corresponding counts of distinct distances are N2/2 + O(1). This sparsity suggests that the

interpolation property might fail in R2, and numerical computations indicate that it does:

Conjecture 7.5. Let r1,r2,... be the positive real numbers of the form (4/3)1/4 j2 + jk + k2, where j and k are integers. Then radial Schwartz functions f : R2 → R are not uniquely determined by the values f(rn), f (rn), f(rn), and f (rn) for integers n ≥ 1.

Indeed, this conjecture has subsequently been proved by Sardari [43]. More generally, in each dimension we expect that interpolation fails whenever the sequence r1,r2,... contains only o(N2) elements between 0 and N as N → ∞, and perhaps even (c + o(1))N2 elements for some constant c < 12. However, we have not explored this possibility thoroughly. Note that the interpolation property cannot depend solely on the asymptotic growth rate of the radii, because it is sensitive to deleting a single interpolation point. We have no characterization of when the interpolation property holds, and it is unclear just how sensitive it is. For example, does moving (but not removing) ﬁnitely many interpolation points preserve the interpolation property?

Cohn and Kumar [14] conjectured that the linear programming bounds are sharp in two dimensions and prove the universal optimality of the hexagonal lattice. There is strong numerical evidence in favor of this conjecture, and in fact the numerics converge far more quickly than in eight or twenty-four dimensions. However, it seems surprisingly diﬃcult to prove that they converge to a sharp bound. Assuming Conjecture 7.5 holds, one cannot prove universal optimality in R2 via a straightforward adaptation of the interpolation strategy used in R8 and R24. Instead, a more sophisticated approach may be needed.

Despite Lemma 7.4, universal optimality in R1 can be proved using an interpolation theorem for a diﬀerent function space, namely Shannon sampling for band-limited functions (see [14, p. 142]). Is it possible that universal optimality in R2 also corresponds to an interpolation theorem for some space of radial functions? That would establish a satisfying pattern, but we are unable to propose what the relevant function space might be.

### Acknowledgements

We are grateful to Ganesh Ajjanagadde, Andriy Bondarenko, Matthew de Courcy-Ireland, Bill Duke, Noam Elkies, Yuri Gurevich, Tom Hales, Mathieu Lewin, Ed Saﬀ, Peter Sarnak, Sylvia Serfaty, Rich Schwartz, Sal Torquato, Ramarathnam Venkatesan, Akshay Venkatesh, and Don Zagier for helpful conversations. We also thank Princeton and the Institute for Advanced Study for hosting Viazovska during part of this work.

### References

- [1] N. Afkhami-Jeddi, H. Cohn, T. Hartman, D. de Laat, and A. Tajdini, Highdimensional sphere packing and the modular bootstrap, J. High Energy Phys. 2020, no. 12, Paper No. 066, 44 pp. https://doi.org/10.1007/jhep12(2020)066 arXiv:2006.02560
- [2] P. Bernays, Uber¨ die Darstellung von positiven, ganzen Zahlen durch die primitiven, bina¨ren quadratischen Formen einer nicht-quadratischen Diskriminante, dissertation, Go¨ttingen, 1912. https://resolver.sub.uni-goettingen.de/purl?PPN313341249
- [3] X. Blanc and M. Lewin, The crystallization conjecture: a review, EMS Surv. Math. Sci. 2 (2015), no. 2, 225–306. https://doi.org/10.4171/EMSS/13 arXiv:1504.01153
- [4] J. Borwein and P. Borwein, Pi and the AGM: A Study in Analytic Number Theory and Computational Complexity, Canadian Mathematical Society Series of Monographs and Advanced Texts 4, John Wiley & Sons, Inc., New York, 1998.
- [5] M. Bowick and L. Giomi, Two-dimensional matter: order, curvature and defects, Adv. in Phys. 58 (2009), no. 5, 449–563. https://doi.org/10.1080/ 00018730903043166 arXiv:0812.3064
- [6] P. Chiu, Height of ﬂat tori, Proc. Amer. Math. Soc. 125 (1997), no. 3, 723–730. https://doi.org/10.1090/S0002-9939-97-03872-0
- [7] Y. Choie and M. H. Lee, Quasimodular forms and Jacobi-like forms, Math. Z. 280 (2015), no. 3–4, 643–667. https://doi.org/10.1007/s00209-015-1441-8
- [8] H. Cohen and F. Str¨omberg, Modular Forms: A Classical Approach, Graduate Studies in Mathematics 179, American Mathematical Society, Providence, RI, 2017.
- [9] H. Cohn, Order and disorder in energy minimization, in Proceedings of the International Congress of Mathematicians (Hyderabad, August 19–27, 2010) (R. Bhatia, A. Pal, G. Rangarajan, V. Srinivas, and M. Vanninathan, eds.), Volume IV, pp. 2416–2443, Hindustan Book Agency, New Delhi, 2010. https: //doi.org/10.1142/9789814324359 0152 arXiv:1003.3053

- [10] H. Cohn, A conceptual breakthrough in sphere packing, Notices Amer. Math. Soc. 64 (2017), no. 2, 102–115. https://doi.org/10.1090/noti1474 arXiv:1611.01685
- [11] H. Cohn and M. de Courcy-Ireland, The Gaussian core model in high dimensions, Duke Math. J. 167 (2018), no. 13, 2417–2455. https://doi.org/10.1215/ 00127094-2018-0018 arXiv:1603.09684
- [12] H. Cohn and N. Elkies, New upper bounds on sphere packings I, Ann. of Math.

(2) 157 (2003), no. 2, 689–714. https://doi.org/10.4007/annals.2003.157.689 arXiv:math/0110009

- [13] H. Cohn and F. Gonc¸alves, An optimal uncertainty principle in twelve dimensions via modular forms, Invent. Math. 217 (2019), no. 3, 799–831. https://doi.org/10. 1007/s00222-019-00875-4 arXiv:1712.04438
- [14] H. Cohn and A. Kumar, Universally optimal distribution of points on spheres, J. Amer. Math. Soc. 20 (2007), no. 1, 99–148. https://doi.org/10.1090/ S0894-0347-06-00546-7 arXiv:math/0607446


- [15] H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, and M. Viazovska, The sphere packing problem in dimension 24, Ann. of Math. (2) 185 (2017), no. 3, 1017–1033. https://doi.org/10.4007/annals.2017.185.3.8 arXiv:1603.06518
- [16] H. Cohn, A. Kumar, and A. Schu¨rmann, Ground states and formal duality relations in the Gaussian core model, Phys. Rev. E (3) 80 (2009), no. 6, 061116, 7 pp. https://doi.org/10.1103/PhysRevE.80.061116 arXiv:0911.2169
- [17] H. Cohn and S. D. Miller, Some properties of optimal functions for sphere packing in dimensions 8 and 24, preprint, 2016. arXiv:1603.04759
- [18] J. H. Conway and N. J. A. Sloane, Sphere Packings, Lattices and Groups, third edition, Grundlehren der Mathematischen Wissenschaften 290, Springer, New York, 1999. https://doi.org/10.1007/978-1-4757-6568-7
- [19] W. Duke, O.¨ Imamog¯lu, and A.´ To´th, Cycle integrals of the j-function and mock modular forms, Ann. of Math. (2) 173 (2011), no. 2, 947–981. https://doi.org/10. 4007/annals.2011.173.2.8
- [20] W. Duke and P. Jenkins, On the zeros and coeﬃcients of certain weakly holomorphic modular forms, Pure Appl. Math. Q. 4 (2008), no. 4, 1327–1340. https://doi.org/10.4310/PAMQ.2008.v4.n4.a15
- [21] F. Dyson, Birds and frogs, Notices Amer. Math. Soc. 56 (2009), no. 2, 212–223.
- [22] W. Ebeling, Lattices and Codes: A Course Partially Based on Lectures by Friedrich Hirzebruch, third edition, Advanced Lectures in Mathematics, Springer Spektrum, Wiesbaden, 2013. https://doi.org/10.1007/978-3-658-00360-9
- [23] M. Eichler, Grenzkreisgruppen und kettenbruchartige Algorithmen, Acta Arith. 11

(1965), 169–180. https://doi.org/10.4064/aa-11-2-169-180

- [24] M. Eichler and D. Zagier, The Theory of Jacobi Forms, Progress in Mathematics 55, Birkh¨auser Boston, Inc., Boston, MA, 1985. https://doi.org/10.1007/ 978-1-4684-9162-3
- [25] L. Grafakos and G. Teschl, On Fourier transforms of radial functions and distributions, J. Fourier Anal. Appl. 19 (2013), no. 1, 167–179. https://doi.org/10. 1007/s00041-012-9242-5 arXiv:1112.5469
- [26] D. P. Hardin, E. B. Saﬀ, and B. Simanek, Periodic discrete energy for long-range potentials, J. Math. Phys. 55 (2014), no. 12, 123509, 27 pp. https://doi.org/10. 1063/1.4903975 arXiv:1403.7505
- [27] J. R. Higgins, Five short stories about the cardinal series, Bull. Amer. Math. Soc. (N.S.) 12 (1985), no. 1, 45–89. https://doi.org/10.1090/S0273-0979-1985-15293-0
- [28] H. Iwaniec, Topics in classical automorphic forms, Graduate Studies in Mathematics 17, American Mathematical Society, Providence, RI, 1997. https://doi. org/10.1090/gsm/017
- [29] N. K. Johnson-McDaniel, A dimensionally continued Poisson summation formula, J. Fourier Anal. Appl. 18 (2012), no. 2, 367–385. https://doi.org/10.1007/ s00041-011-9207-0 arXiv:1011.3790
- [30] M. Kaneko and D. Zagier, A generalized Jacobi theta function and quasimodular forms, in The Moduli Space of Curves (R. Dijkgraaf, C. Faber, and G. van der Geer, eds.), pp. 165–172, Progress in Mathematics 129, Birkha¨user Boston, Inc., Boston, MA, 1995. https://doi.org/10.1007/978-1-4612-4264-2 6


- [31] M. I. Knopp, Some new results on the Eichler cohomology of automorphic forms, Bull. Amer. Math. Soc. 80 (1974), no. 4, 607–632. https://doi.org/10.1090/ S0002-9904-1974-13520-2
- [32] N. Lev and A. Olevskii, Quasicrystals and Poisson’s summation formula, Invent. Math. 200 (2015), no. 2, 585–606. https://doi.org/10.1007/s00222-014-0542-z arXiv:1312.6884
- [33] C. N. Likos, Eﬀective interactions in soft condensed matter physics, Phys. Rep. 348 (2001), no. 4–5, 267–439. https://doi.org/10.1016/S0370-1573(00)00141-1
- [34] A. A. Markov, Theory of Algorithms (Russian), Trudy Mat. Inst. Steklov. 42, Acad. Sci. USSR, Moscow, 1954, http://mi.mathnet.ru/eng/tm1178; English translation in Theory of Algorithms, Israel Program for Scientiﬁc Translations, Jerusalem, 1961.
- [35] H. McKean and V. Moll, Elliptic Curves: Function Theory, Geometry, Arithmetic, Cambridge University Press, Cambridge, 1997. https://doi.org/10.1017/ CBO9781139174879
- [36] H. L. Montgomery, Minimal theta functions, Glasgow Math. J. 30 (1988), no. 1, 75–85. https://doi.org/10.1017/S0017089500007047
- [37] R. E. Moore, R. B. Kearfott, and M. J. Cloud, Introduction to Interval Analysis, Society for Industrial and Applied Mathematics, Philadelphia, PA, 2009. https: //doi.org/10.1137/1.9780898717716
- [38] F. W. J. Olver, D. W. Lozier, R. F. Boisvert, and C. W. Clark, eds., NIST Handbook of Mathematical Functions, National Institute of Standards and Technology, U.S. Department of Commerce, Washington, DC and Cambridge University Press, Cambridge, 2010. https://dlmf.nist.gov/
- [39] B. Osgood, R. Phillips, and P. Sarnak, Extremals of determinants of Laplacians, J. Funct. Anal. 80 (1988), no. 1, 148–211. https://doi.org/10.1016/0022-1236(88) 90070-5
- [40] D. Radchenko and M. Viazovska, Fourier interpolation on the real line, Publ. Math. Inst. Hautes Etudes´ Sci. 129 (2019), 51–81. https://doi.org/10.1007/ s10240-018-0101-z arXiv:1701.00265.
- [41] D. Ruelle, Statistical Mechanics: Rigorous Results, reprint of the 1989 edition, World Scientiﬁc Publishing Co., Inc., River Edge, NJ; Imperial College Press, London, 1999. https://doi.org/10.1142/4090
- [42] S. S. Ryshkov, On the question of ﬁnal ζ-optimality of lattices providing the closest lattice packing of n-dimensional spheres (Russian), Sibirsk. Mat. Z.ˇ 14 (1973), no. 5, 1065–1075; English translation in Siberian Math. J. 14 (1973), no. 5, 743–750. https://doi.org/10.1007/BF00969911
- [43] N. T. Sardari, Higher Fourier interpolation on the plane, preprint, 2021. arXiv:2102.08753
- [44] P. Sarnak and A. Str¨ombergsson, Minima of Epstein’s zeta function and heights of ﬂat tori, Invent. Math. 165 (2006), no. 1, 115–151. https://doi.org/10.1007/ s00222-005-0488-2
- [45] S. L. Segal, Nine Introductions in Complex Analysis, revised edition, North-Holland Mathematical Studies 208, Elsevier Science B.V., Amsterdam, 2008.


- [46] J.-P. Serre, A Course in Arithmetic, Graduate Texts in Mathematics 7, Springer, New York, 1973. https://doi.org/10.1007/978-1-4684-9884-4
- [47] B. Simon, Fifteen problems in mathematical physics, in Perspectives in Mathematics: Anniversary of Oberwolfach 1984 (W. Ja¨ger, J. Moser, and R. Remmert, eds.), pp. 423–454, Birkh¨user Verlag, Basel, 1984.
- [48] B. Simon, Convexity: An Analytic Viewpoint, Cambridge Tracts in Mathematics 187, Cambridge University Press, Cambridge, 2011. https://doi.org/10.1017/ CBO9780511910135
- [49] W. A. Stein et al., Sage Mathematics Software (Version 9.5), The Sage Development Team, 2022, https://www.sagemath.org.
- [50] F. H. Stillinger, Phase transitions in the Gaussian core system, J. Chem. Phys. 65 (1976), no. 10, 3968–3974. https://doi.org/10.1063/1.432891
- [51] F. Theil, A proof of crystallization in two dimensions, Comm. Math. Phys. 262

(2006), no. 1, 209–236. https://doi.org/10.1007/s00220-005-1458-7

- [52] W. J. Ventevogel and B. R. A. Nijboer, On the conﬁguration of systems of interacting particles with minimum potential energy per particle, Phys. A 98

(1979), no. 1–2, 274–288. https://doi.org/10.1016/0378-4371(79)90178-X

- [53] M. S. Viazovska, The sphere packing problem in dimension 8, Ann. of Math.

(2) 185 (2017), no. 3, 991–1015. https://doi.org/10.4007/annals.2017.185.3.7 arXiv:1603.04246

- [54] E. T. Whittaker and G. N. Watson, A Course of Modern Analysis, reprint of the fourth edition, Cambridge Mathematical Library, Cambridge University Press, Cambridge, 1996. https://doi.org/10.1017/CBO9780511608759
- [55] Wolfram Research, Inc., Mathematica (Version 11.1.1), Champaign, IL, 2017.
- [56] V. A. Yudin, The minimum of potential energy of a system of point charges (Russian), Diskret. Mat. 4 (1992), no. 2, 115–121; English translation in Discrete Math. Appl. 3 (1993), no. 1, 75–81. https://doi.org/10.1515/dma.1993.3.1.75
- [57] D. Zagier, Elliptic modular forms and their applications, in The 1-2-3 of Modular Forms (K. Ranestad, ed.), pp. 1–103, Universitext, Springer, Berlin, 2008. https: //doi.org/10.1007/978-3-540-74119-0 1


Microsoft Research New England, Cambridge, MA, USA E-mail : cohn@microsoft.com

Stony Brook University, Stony Brook, NY, USA E-mail : thenav@gmail.com

Rutgers University, Piscataway, NJ, USA E-mail : miller@math.rutgers.edu

Max Planck Institute for Mathematics, Bonn, Germany E-mail : danradchenko@gmail.com

Ecole´ Polytechnique Fed´ erale´ de Lausanne, Lausanne, Switzerland E-mail : viazovska@gmail.com

