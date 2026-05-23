---
type: source
kind: paper
title: High-dimensional sphere packing and the modular bootstrap
authors: Nima Afkhami-Jeddi, Henry Cohn, Thomas Hartman, David de Laat, Amirhossein Tajdini
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2006.02560v2
source_local: ../raw/2020-afkhamijeddi-high-dimensional-sphere-packing-modular.pdf
topic: general-knowledge
cites:
---

# arXiv:2006.02560v2[hep-th]14Dec2020

## High-dimensional sphere packing and the modular bootstrap

Nima Afkhami-Jeddi,1 Henry Cohn,2 Thomas Hartman,3 David de Laat,4 and Amirhossein Tajdini3

1Enrico Fermi Institute & Kadanoﬀ Center for Theoretical Physics, University of Chicago, Chicago, Illinois, USA 2Microsoft Research New England, Cambridge, Massachusetts, USA

- 3Department of Physics, Cornell University, Ithaca, New York, USA
- 4Delft Institute of Applied Mathematics, Delft University of Technology, Delft, The Netherlands


nimaaj@uchicago.edu, cohn@microsoft.com, hartman@cornell.edu, d.delaat@tudelft.nl, at734@cornell.edu

Abstract

We carry out a numerical study of the spinless modular bootstrap for conformal ﬁeld theories with current algebra U(1)c × U(1)c, or equivalently the linear programming bound for sphere packing in 2c dimensions. We give a more detailed picture of the behavior for ﬁnite c than was previously available, and we extrapolate as c → ∞. Our extrapolation indicates an exponential improvement for sphere packing density bounds in high dimensions. Furthermore, we study when these bounds can be tight. Besides the known cases c = 1/2, 4, and 12 and the conjectured case c = 1, our calculations numerically rule out sharp bounds for all other c < 90, by combining the modular bootstrap with linear programming bounds for spherical codes.

## Contents

- 1 Introduction 2
- 2 The spinless modular bootstrap 6
- 3 Numerical results 12
- 4 Properties of the spectrum and degeneracies 17
- 5 Spherical codes and implied kissing numbers 28


- A The limiting case of the spinless modular bootstrap 39
- B Convergence of the spinless bootstrap 40


## 1 Introduction

To what extent do self-consistency principles constrain, or even determine, the behavior of a system? This question underlies many topics in mathematics and physics. One notable example is the conformal bootstrap program [1, 2, 3, 4] (see [5, 6, 7] for reviews), which seeks to map the space of possible conformal ﬁeld theories (CFTs) and to identify those on the boundary of theory space (i.e., those with extremal properties, almost but not quite inconsistent). A more down to earth example is the sphere packing problem, in which the goal is to maximize the fraction of Rd covered by congruent spheres whose interiors are not allowed to overlap. In low dimensions it is not hard to guess the optimal packings, but even that remains mysterious in high dimensions. Proving upper bounds for the packing density is particularly diﬃcult, and in most cases the best bounds currently known are obtained via the linear programming bound of Cohn and Elkies [8], which relies on harmonic analysis.

While these problems sound completely unrelated, Hartman, Maz´aˇc, and Rastelli [9] discovered a surprising connection between them: the spinless modular bootstrap for twodimensional CFTs is very nearly the same as the linear programming bound for sphere packing. The underlying optimization problems are exactly equivalent when the current algebra U(1)cleft × U(1)cright¯ with total central charge ctotal = c + c¯ acts on the CFT and the sphere packing dimension is given by d = ctotal, and they are closely related (but not equivalent) under the Virasoro algebra. The relationship between the modular bootstrap and linear programming bounds seems to be speciﬁc to these particular techniques, rather than being based on a direct connection between CFTs and sphere packings.

In this paper we will focus on the spinless modular bootstrap for U(1)cleft × U(1)cright¯ with ctotal large. The analysis depends only on ctotal, not on the left and right central charges individually. To simplify the notation we set c¯ = c and refer simply to the U(1)c modular bootstrap, parameterizing our results by c = ctotal/2.

Neither the modular bootstrap nor the linear programming bound has been completely analyzed, either theoretically or numerically. Each depends on producing some additional information (namely, an auxiliary function or linear functional satisfying certain inequalities), which must be chosen carefully to optimize the resulting bound, and this optimization has proved diﬃcult. The equivalence between these problems adds to the motivation for studying

- them, because any consequences will shed light on two seemingly disparate topics. A third application is to generalizations of the Bourgain-Clozel-Kahane uncertainty principle for signs of functions [10, 11]. Thus, these problems live at a particularly fruitful intersection of several ﬁelds.


In this paper, we carry out the ﬁrst large-scale numerical study of the U(1)c spinless modular bootstrap with c large, or equivalently the linear programming bound on sphere packing in high dimensions, by adapting the numerical techniques introduced by AfkhamiJeddi, Hartman, and Tajdini for the Virasoro case [12]. These techniques closely parallel the approach independently taken by Cohn, Elkies, Kumar, and Gon¸calves [8, 13, 11, 14] in the sphere packing literature, but the paper [12] introduced better extrapolation techniques and

achieved superior performance.

In CFT terms, the spinless modular bootstrap corresponds to constraints on the partition function at zero angular potential. A natural question is whether the spinning modular bootstrap, i.e., including an angular potential, also bounds the density of general sphere packings. The answer is that it does not, as this would contradict known packings. The spinning bootstrap analysis for CFTs with U(1)cleft × U(1)cright symmetry has interesting implications for holographic duality and will appear in a separate paper [15].

### 1.1 Results from the spinless modular bootstrap for large c

For sphere packing in high dimensions, the central question is the asymptotic behavior of the packing density. It is at least 2−d in Rd, with only much lower-order improvements known [16, 17, 18], and it is at most 2−(κ+o(1))d with κ = 0.59905576.... The latter bound was found by Kabatyanskii and Levenshtein [19] in 1978, and the exponential decay rate has not been improved since then. Cohn and Zhao [20] showed how to obtain it via the linear programming bound, and a fundamental open question is whether the linear programming bound is capable of improving on this decay rate.

In terms of the U(1)c spinless modular bootstrap, bounding the packing density amounts to bounding the spectral gap of the CFT. Speciﬁcally, the Kabatyanskii-Levenshtein bound says that the scaling dimension of the lowest non-vacuum primary is at most c/(K + o(1)) as c → ∞, where K = eπ22κ−1 = 9.79674646.... No better bound is known for the spectral gap.

One of our primary results in this paper is a numerical estimate of the fully optimized U(1)c spinless modular bootstrap bound for the spectral gap (Conjecture 3.1). In sphere packing terms, it amounts to an upper bound of 2−(λ+o(1))d for the sphere packing density in Rd as d → ∞ with λ ≈ 0.6044; in modular bootstrap terms, it amounts to an upper bound of c/(Λ + o(1)) for the spectral gap as c → ∞ with Λ ≈ 9.869. This bound is based on numerical extrapolation, with no proof or even heuristic derivation, but we give a careful accounting of the potential error from the extrapolation. We furthermore guess that the exact value of Λ is π2 (Conjecture 3.2), although that conjecture is much more speculative.

Conceptually, what our computations indicate is that the Kabatyanskii-Levenshtein upper bound can be decreased by an exponential factor through optimizing the linear programming bound. If proved, this bound would settle a longstanding open problem in discrete geometry. However, the improvement in the decay rate will be small.

The analytical [9] and numerical [12] results for Virasoro symmetry are quite a bit further away from each other (the analytical bound for the spectral gap is c/8.503, while the numerical bound is c/9.08). We have no conceptual explanation for why the Kabatyanskii-Levenshtein bound should come rather close to optimizing the U(1)c case, yet fall slightly short. Perhaps generalizing this bound will oﬀer new techniques for optimizing the modular bootstrap more broadly, but we do not expect that it will lead to an exact solution without some new idea.

Sphere packings are error-correcting codes for a continuous communication channel, and they therefore play an important role in information theory. Their discrete counterpart is

error-correcting codes for a binary channel, and these two theories are in many ways closely analogous [21], with substantial interplay between them, both in results and in techniques. The linear program bound originated in the discrete setting, in a fundamental paper by Delsarte [22], before being generalized to sphere packing by Cohn and Elkies [8], and the KabatyanskiiLevenshtein bound was inspired by the MRRW bound, due to McEliece, Rodemich, Rumsey, and Welch [23].

Much like the case of sphere packing, the asymptotic rate in the MRRW bound has not been beaten by any method, and it is an open problem whether it optimizes the linear programming bound. Barg and Jaﬀe [24] examined this issue numerically, and they conjectured that it is the optimal rate in the linear programming bound. Their conjecture is widely believed, but the evidence is not conclusive. While our results have no direct implications for binary error-correcting codes, they suggest that the MRRW bound may not be optimal, because it is the discrete analogue of the Kabatyanskii-Levenshtein bound. It would be valuable to perform a more extensive study than Barg and Jaﬀe were able to do in 2001, as well as to compare the data with Section 3.2 of [25].

At the optimum, the linear programming approach provides not just a bound on the spectral gap, but a candidate spectrum for a CFT that saturates it. In sphere packing terms, this spectrum amounts to the pair correlation function of the packing. We study the spectrum numerically in Section 4 and ﬁnd some intriguing structure. For computational purposes, the inﬁnite set of bootstrap constraints is truncated to a ﬁnite system of 2N equations, with N taken as large as possible. The corresponding spectrum has N states other than the vacuum,

with scaling dimensions ∆1 < ∆2 < ··· < ∆N. We conjecture a formula for the ratio ∆n/N in the limit N → ∞ with n/N held ﬁxed. The formula is piecewise smooth, with an abrupt transition from linear to nonlinear behavior at n ∼ (2/π)N. We have no analytic explanation for this transition. The linear portion of the spectrum matches the spectrum of the generalized free fermion in one dimension, which was used to construct analytic functionals for CFT in [26] and adapted to sphere packing in [9].

### 1.2 New constraints on tight sphere packing bounds

In addition to studying the asymptotic behavior of the modular bootstrap, we also search for exceptional behavior at ﬁnite central charge. Four particular values are known to play a special role, namely c = 1/2, 1, 4, and 12. In sphere packing terms, these cases correspond to exact solutions of the sphere packing problem in dimensions 1, 2, 8, and 24. While d = 1 is trivial, d = 8 and d = 24 are far deeper, and they are the only cases in which the sphere packing problem has been solved above d = 3 (which was solved by Hales [27, 28], with no connection to the modular bootstrap). Dimension 8 was a breakthrough due to Viazovska [29], and dimension 24 built on her techniques [30]. The linear programming bound seems to be exact when d = 2 as well, but no proof is known, although the two-dimensional sphere packing problem can be solved directly [31, 32].

These cases are more subtle for CFTs than they are for sphere packings. For (c,c¯) = (4,4),

there is indeed a CFT invariant under U(1)cleft × U(1)cright¯ that achieves the spinless modular bootstrap bound, namely eight free fermions [33]. No such CFT exists for (c,c¯) = (12,12) (see [15]), but there is a chiral CFT with (c,c¯) = (24,0), namely the 24 chiral bosons compactiﬁed using the quotient of R24 by the Leech lattice.1 The case c = 1/2 is not an integer, so U(1)cleft × U(1)cright symmetry does not even make sense, but again we can use a chiral boson with (c,c¯) = (1,0). This time, however, it is not fully conformally invariant. Instead, it has a nontrivial phase under the action of the generator T of SL2(Z), but the spinless modular bootstrap nevertheless applies. Finally, in the case c = 1 no CFT invariant under U(1)cleft × U(1)cright achieves the spinless bound (see [15]), but it is achieved by two chiral bosons with (c,c¯) = (2,0) and a nontrivial phase under the T transformation. Thus, the CFT picture encompasses all four exceptional cases, provided we allow chiral CFTs and are willing to relax conformal invariance.

Why should the exceptional solutions of the sphere packing problem be limited to these speciﬁc dimensions? It comes as no surprise to see sporadic behavior tied to E8 and the Leech lattice (for c = 4 and 12, respectively), but it is diﬃcult to explain why this behavior is not more widespread. For a provocative example, why shouldn’t the linear programming bound solve the sphere packing problem in all suﬃciently large dimensions? We do not know how to rule out this possibility, although it is utterly implausible.

To shed light on this problem, we examine the conditions that would have to hold to obtain a sphere packing meeting the linear programming bound. To do so, we incorporate additional constraints beyond the modular invariance of the partition function. Speciﬁcally, we study the implied kissing number, the average number of tangencies between spheres in a hypothetical packing with this property. In all dimensions up through d = 250 other than 1,

- 2, 8, 24, 180, 181, and 192, we show that the implied kissing number from our numerically optimized bound is impossibly large. Thus, no sphere packing can attain the exact linear programming bound in these dimensions.2 We do not expect optimal solutions in dimensions 180, 181, or 192, and we see no sign of them, but our bounds do not rule them out.


As the unexpected occurrence of dimensions such as 181 indicates, this problem has a surprisingly intricate structure. While certain aspects behave in straightforward ways that are not hard to extrapolate, other aspects are far more subtle. One feature of our numerical solutions for which we have no conceptual explanation is a kind of periodicity: the degeneracies are especially well described by a Cardy-like entropy formula when c is a multiple of 8, and the scaling dimensions are especially close to those for generalized one-dimensional free fermions when c is 4 more than a multiple of 8. In other words, multiples of 4 behave particularly well, but no value of c looks equally simple from all perspectives. The reason for this behavior remains mysterious.

- 1Note that we do not take an orbifold quotient, as in the Monster CFT of Frenkel, Lepowsky, and Meurman [34], because we want current algebra U(1)24. Similarly, 8 chiral bosons compactiﬁed using E8 meet the bound with (c, c¯) = (8, 0), but the (c, c¯) = (4, 4) case is more noteworthy.
- 2Strictly speaking, our work does not amount to a proof, because it leaves open the possibility that we have not fully optimized the linear programming bound. However, we present strong numerical evidence that we have optimized it.


## 2 The spinless modular bootstrap

### 2.1 Setting up the bootstrap

In this section, we will brieﬂy review the spinless modular bootstrap, which is a technique for proving bounds on the possible scaling dimensions of primary ﬁelds in a compact, unitary

- 2d CFT [35, 36, 33]. Given such a CFT, let Z(τ,τ¯) be its partition function, i.e., the sum over all states of qh−c/24q¯h¯−c/¯ 24, where h and h¯ are the conformal weights of the state, c and c¯ are the left and right central charges, and q = e2πiτ and q¯ = e−2πiτ¯ (with τ and −τ¯ in the upper half-plane).3 Because of conformal invariance, the partition function satisﬁes modular invariance:


aτ + b cτ + d

aτ¯ + b cτ¯ + d

= Z(τ,τ¯) (2.1) whenever

Z

,

a b c d ∈ SL2(Z) (2.2)

(where in these formulas c is of course not necessarily the left central charge). In terms of the usual generators

- 0 −1
- 1 0


1 1 0 1

and T =

(2.3)

S =

of SL2(Z), modular invariance amounts to Z(−1/τ,−1/τ¯) = Z(τ + 1,τ¯ + 1) = Z(τ,τ¯). (2.4)

For the spinless modular bootstrap, we specialize the partition function to have zero angular potential. In other words, we set τ¯ = −τ (i.e., q¯ = q) and use the restricted partition function

Z(τ) = Z(τ,−τ). (2.5) The action of S on τ and τ¯ preserves the condition τ¯ = −τ, and thus

Z(−1/τ) = Z(τ), (2.6)

but the action of T does not. Thus, we expect that usually Z(τ + 1) = Z(τ).

The spinless modular bootstrap is based on the identity Z(−1/τ) = Z(τ). Because we make no use of the action of T, the bound applies even to theories that are invariant only under S. A simple example is a single chiral boson at the self-dual radius, for which Z(τ,τ¯) = θ3(τ)/η(τ) in terms of the Jacobi theta function and Dedekind eta function. Such theories are not fully conformally invariant, but the spinless modular bootstrap still applies.

The combined contribution of the descendants of a primary ﬁeld of scaling dimension ∆ = h + h¯ to the partition function Z(τ) is a character χ∆(τ) of a Verma module of the

3Mathematicians should note that the bars do not denote complex conjugates.

current algebra, and thus the partition function is given by a sum

Z(τ) =

∆

d∆χ∆(τ) (2.7)

over the scaling dimensions of the primary ﬁelds, each with multiplicity given by the degeneracy d∆. The vacuum corresponds to ∆ = 0, with degeneracy d0 = 1, and the other scaling dimensions are positive numbers ∆1 < ∆2 < ··· that tend to inﬁnity.

The precise form of the characters depends on the current algebra. Our main interest in

this paper will be the algebra U(1)cleft × U(1)cright¯ (more precisely, the corresponding aﬃne Lie algebra), in which case

e2πiτ∆ η(τ)c+¯c

χ∆(τ) =

, (2.8)

where η is again the Dedekind eta function. In particular, the only dependence on the central charges is through their sum c + c¯.

The spectral gap of the CFT is the lowest scaling dimension ∆1 of a primary other than the vacuum. We can obtain an upper bound for the spectral gap by producing a linear functional that acts in a certain way on functions of τ. The key observation is that if we set

Φ∆(τ) = χ∆(τ) − χ∆(−1/τ), (2.9)

- then we obtain the crossing equation


∆

d∆Φ∆(τ) = 0 (2.10)

by modular invariance. Now suppose ω is a linear functional such that

ω(Φ0) > 0 (2.11) and

ω(Φ∆) ≥ 0 (2.12)

whenever ∆ ≥ ∆gap for some constant ∆gap. If we apply ω to the crossing equation, we ﬁnd that

ω(Φ0) +

d∆ω(Φ∆) = 0, (2.13)

∆>0

which would be impossible if all the non-zero scaling dimensions were at least ∆gap, because the total would be positive. Thus, we conclude that some primary must have a scaling dimension strictly between 0 and ∆gap. In other words, ∆gap is a strict upper bound for the spectral gap. One can show that it is a weak upper bound even if ω(Φ0) = 0, as long as ω(Φ∆) is not identically zero (see Appendix A), and that ω(Φ0) = 0 must hold for the optimal choice of ω.

The optimal functional ω is not known, except in a handful of special cases discussed

below. In Sections 3 and 4, we will give the most detailed numerical study so far of how ω and ∆gap behave.

As noted earlier, because the spinless modular bootstrap for U(1)cleft × U(1)cright¯ depends only on c+c¯, we will set c¯ = c and refer just to c. Strictly speaking this notation is misleading when c + c¯ is odd, because the current algebra U(1)cleft × U(1)cright¯ makes sense only when c and c¯ are nonnegative integers. For example, the only physically meaningful cases with c + c¯ = 1 are (c,c¯) = (1,0) or (0,1), and they are therefore what we mean when we refer to the c = 1/2 case. More generally, the abstract problem of optimizing the bound makes sense for any c > 0, but there are consequences for CFTs only when c is an integer or half-integer.

### 2.2 Uncertainty principle

Hartman, Maza´cˇ, and Rastelli [9] reformulated the U(1)c spinless modular bootstrap in terms of an uncertainty principle for eigenfunctions of the Fourier transform as follows. Suppose d = 2c is an integer, which is the meaningful case for CFTs. Given a functional ω as above, we deﬁne a radial function fω : Rd → R by fω(x) = ω(Φ|x|2/2). If we normalize the Fourier transform in Rd by

dxf(x)e−2πi x,y , (2.14)

f(y) =

Rd

then fω is an eigenfunction of the Fourier transform with eigenvalue −1; in other words, fω = −fω. To see why, we start with

Φ|x|2/2(τ) = χ|x|2/2(τ) − χ|x|2/2(−1/τ)

eπiτ|x|2 η(τ)d −

eπi(−1/τ)|x|2 η(−1/τ)d

=

.

eπiτ|x|2 − (i/τ)d/2eπi(−1/τ)|x|2 η(τ)d

=

,

(2.15)

because the Dedekind eta function satisﬁes the identity η(−1/τ) = (τ/i)1/2η(τ). The complex Gaussian x  → eπiτ|x|2 on Rd has Fourier transform y  → (i/τ)d/2eπi(−1/τ)|y|2. Thus, the function x  → eπiτ|x|2 −(i/τ)d/2eπi(−1/τ)|x|2 in the numerator of Φ|x|2/2(τ) is a −1 eigenfunction of the Fourier transform for each τ, because it is the diﬀerence of a Gaussian and its Fourier transform. We conclude that fω also satisﬁes fω = −fω, by the linearity of ω. The same holds even when 2c is not an integer, if we interpret the radial Fourier transform in non-integral dimension as a Hankel transform.

Conversely, every radial −1 eigenfunction of the Fourier transform in Rd arises as fω for some ω, which we can obtain as follows by constructing a basis. If we let

ωk =

∂k ∂τk τ=i

, (2.16)

then ωk(Φ∆) is the product of e−2π∆ with a polynomial in ∆ of degree at most k, in which

the coeﬃcient of ∆k is

 

(2πi)k − (i/τ)d/2(2πi)k(1/τ2)k η(τ)d

0 if k is even, and 2(2πi)k/η(i)d if k is odd.

=

(2.17)



τ=i

For comparison, the Laguerre polynomials Lk(d/2−1) give a basis for radial functions on Rd

- as x  → L(kd/2−1)(2π|x|2)e−π|x|2, with eigenvalues (−1)k under the Fourier transform. We conclude that the functions x  → ωk(Φ|x|2/2) with k = 1,3,5,...,2m − 1 must span the same space as the Laguerre eigenfunctions with these values of k, and thus they span the entire −1 eigenspace as m → ∞.


We have seen that choosing the linear functional ω in the U(1)c spinless modular bootstrap amounts to choosing an integrable, radial function f : Rd → R with f = −f such that f is not identically zero. The constraints on ω say that f(0) ≥ 0 and f(x) ≥ 0 whenever |x| ≥ r for some radius r. Then ∆gap = r2/2, and optimizing the bound means minimizing r. This optimization problem for signs of eigenfunctions was ﬁrst studied by Cohn and Elkies [8], and it was placed in the context of more general uncertainty principles for signs of functions by Cohn and Gon¸calves [11].

The corresponding problem for +1 eigenfunctions asks for an integrable, radial function g: Rd → R with g = g such that g(0) ≤ 0 and g(x) ≥ 0 for |x| ≥ r. Again the goal is to minimize r, without letting g vanish identically. This problem does not arise in the spinless modular bootstrap as set up above, but it would apply if the partition function satisﬁed Z(−1/τ) = −Z(τ) and d∆ < 0 for ∆ > 0 (see Section 2.1 of [11]). It behaves much like the −1 case. For example, Cohn and Gonc¸alves [11] obtained an exact solution of the +1 problem for c = 6, which is analogous to the solutions of the −1 problem with c = 4 or 12. The partition function in this case is given by Z(τ) = j(τ) − 1728, which also arises as the Norton series for a certain pair of elements in the Monster group (see equation (7.3.4c) in [37, p. 425]). Although we do not have a direct physical interpretation for this problem, generalized modular transformations do arise in theories with discrete anomalies [38] or fermions [39, 40], including sectors that obey Z(−1/τ) = −Z(τ).

### 2.3 Sphere packing

The −1 eigenfunction uncertainty principle plays a fundamental role in discrete geometry, where it underlies the linear programming bound for the sphere packing density. Linear programming bounds are a powerful technique for proving upper bounds for packing density or error-correcting code rates. They were introduced for discrete error-correcting codes by Delsarte [22] in 1972, and extended to sphere packing in Euclidean space by Cohn and Elkies [8] in 2003. The connection with the spinless modular bootstrap for U(1)c was derived by Hartman, Maz´ˇc, and Rastelli [9] in 2019.

The linear programming bound for sphere packing in Rd converts an auxiliary function

satisfying certain inequalities into a sphere packing density bound, as follows.4

Theorem 2.1 (Cohn and Elkies [8]). Let h: Rd → R be an integrable, continuous, radial function such that h is integrable, and let r be a positive real number. If h(0) = h(0) = 1, h(x) ≤ 0 whenever |x| ≥ r, and h(y) ≥ 0 for all y, then every sphere packing in Rd has density

- at most the volume of a sphere of radius r/2 in Rd, i.e.,


πd/2 (d/2)!

r 2

d

. (2.18)

The problem of choosing h so as to minimize r is clearly reminiscent of the −1 eigenfunction uncertainty principle, but not obviously equivalent to it. One direction is simple: if h satisﬁes the hypotheses of Theorem 2.1, then the function f = h − h satisﬁes f(0) = 0, f = −f, and f(x) ≥ 0 for |x| ≥ r. Conversely, Cohn and Elkies conjectured that an optimal solution f of the −1 eigenfunction problem can always be lifted to a function h for use in Theorem 2.1 with the same value of r, such that h − h = f. In other words, the linear programming bound for sphere packing should be identical to the spinless modular bootstrap. No proof is known, but no counterexample has been found, either numerically or analytically.

At ﬁrst glance, it is not obvious that any auxiliary function satisﬁes the hypotheses of the linear programming bound. For a ﬁrst example, let χ: Rd → R be the characteristic function of a ball Br/2 centered at the origin, with its radius r/2 chosen so that vol(Br/2) = 1. Then the convolution h := χ ∗ χ has Fourier transform h = χ2. By construction, h(x) = 0 for |x| ≥ r and h(y) ≥ 0 for all y; furthermore, h(0) = vol(Br/2) = 1 and h(0) = vol(Br/2)2 = 1. Thus, the sphere packing density in Rd is at most vol(Br/2) = 1. This bound is sharp when d = 1, but it is of course not an exciting packing bound. For d > 1 the linear programming bound is much better than this ﬁrst attempt.

In fact, it is the best upper bound known for the sphere packing density in high dimensions [20], but it is generally far from a tight bound [41]. Only four cases seem to be sharp: d = 1 (as shown above), 2, 8, and 24. The case d = 8 was a breakthrough due to Viazovska [29], and the case d = 24 extended her techniques [30]. These are the only cases in which the sphere packing problem has been solved above three dimensions. The optimal auxiliary functions for d = 8 and 24 can also be derived from analytic functionals constructed that same year by Maz´aˇc [26] in the four-point function bootstrap for 1d CFTs, as shown by Hartman, Maz´ˇc, and Rastelli [9]. Remarkably, the case d = 2 remains unsolved analytically. There is no doubt that it matches the two-dimensional packing density,5 but no proof is known.

Linear programming bounds can be applied not just to sphere packing, but to understand ground states under pair potential functions more broadly [42, 43, 44]. We will not address that topic in this paper, except to note that our numerical results seem consistent with Conjecture 7.2 in [44], which says that the linear programming bound for sphere packing

4The original technical hypotheses in [8] were slightly stronger; see [20] and [41]. 5With the techniques from Appendix A of [13], we can prove rigorously that they agree to more than a

thousand decimal places, by using 300 forced double roots at the vector lengths from the hexagonal lattice.

extends to the Gaussian core model and thereby proves a form of universal optimality, despite the failure of the analogous statement for binary error-correcting codes [45].

### 2.4 Numerics

To obtain numerical bounds for the U(1)c spinless modular bootstrap, we must choose a ﬁnite-dimensional space of functionals ω. We truncate at derivative order 4N − 1; in other words, ω will be a linear combination of ω1,ω3,...,ω4N−1, where as above ωk = ∂k/∂τk τ=i.

For convenience let f(∆) = ω(Φ∆), which diﬀers from the −1 Fourier eigenfunction in being a function of ∆ rather than x with ∆ = |x|2/2. Then f(∆) can be written in terms of the Laguerre eigenfunctions as

2N

f(∆) =

αjfj(∆), (2.19)

j=1

where

fj(∆) = L2(cj−−1)1 (4π∆)e−2π∆. (2.20)

For ﬁxed ∆gap and N, the question is whether f can be chosen to satisfy the positivity conditions f(0) ≥ 0 and f(∆) ≥ 0 for ∆ ≥ ∆gap without vanishing identically. This problem can be solved using semideﬁnite programming, or approximated using linear programming.

Let ∆LP1 ,N(c) be the best bound that can be obtained for a ﬁxed truncation order N, and let ∆LP1 (c) be the best bound without restriction on ω. Increasing N improves the bound, and we expect that

∆LP1 ,N(c). (2.21) Numerical linear or semideﬁnite programming succeeds at small N, but has been limited

∆LP1 (c) = lim

N→∞

- to N 100 by the computational cost. It is much faster to trade the linear program for a nonlinear optimization over the roots of f(∆).


At the optimum, f(∆) is found empirically to have single roots at ∆0 = 0 and ∆1 = ∆gap, and N − 1 double roots ∆2,∆3,...,∆N. Assuming this to hold in general, we can restate the optimization problem as follows: ﬁx ∆1, and maximize f(0) over the parameters αj for 1 ≤ j ≤ 2N and ∆n for 2 ≤ n ≤ N, subject to the pattern of roots

f(∆1) = 0 and f(∆n) = f (∆n) = 0 for 2 ≤ n ≤ N.

(2.22)

If the optimized function has f(0) > 0, then this value of ∆1 is excluded. The marginal bound has f(0) = 0, and the corresponding ∆1 gives ∆LP1 ,N(c).

If this problem can be solved with some mild non-degeneracy conditions, then it provably gives ∆LP1 ,N(c) (see Section 5 of [11]). However, there is no guarantee that the optimum must be of this form, and it fails for c = 3/2. Speciﬁcally, when c = 3/2 it works for 1 ≤ N ≤ 21 and 27 ≤ N ≤ 32, but for 22 ≤ N ≤ 26 and N = 33 there is a diﬀerent pattern of roots. We do not know what happens as N → ∞.

Aside from c = 3/2, this method has always worked in practice.6 The resulting bound can be made rigorous simply by proving that the optimal functional satisﬁes the positivity conditions.

This is essentially the method used by Cohn and Elkies [8]. In the conformal bootstrap, a similar approach was ﬁrst discussed by El-Showk and Paulos in the context of 1d correlation functions [46]. Recently, their methods were improved by Afkhami-Jeddi, Hartman, and Tajdini and applied to the modular bootstrap [12]. The ﬁrst step is to dualize the optimization problem. The dual problem, together with the equation f(0) = 0, leads to the equations

fk(0) +

N

dnfk(∆n) = 0 for 1 ≤ k ≤ 2N. (2.23)

n=1

Here the unknowns are d1,...,dN and ∆1,...,∆N. These equations are nothing but the original crossing equation (2.10) truncated to N states. If we absorb the factors of e−2π∆n from fk(∆n) into the coeﬃcients dn, we are left with 2N polynomial equations in 2N unknowns.

Solutions to (2.23) with dn > 0 place a lower bound ∆LP1 ,N(c) ≥ ∆1, almost by deﬁnition. What is more surprising is that the solution saturating ∆1 = ∆LP1 ,N(c) has exactly N states and can be found eﬃciently by Newton’s method. The last ingredient we need in the algorithm is a procedure to generate the initial guess for Newton’s method. We start at small N, where it is easy to ﬁnd a guess by hand, and then gradually increase N, using the results from lower N to generate the next guess as in Appendix B of [12]. This method allows for large jumps in N, while still converging to the bound within a few Newton steps.

## 3 Numerical results

### 3.1 Data and plots

The linear programming bound for the sphere packing density in Rd is shown in Figure 1 for d ≤ 48, along with the record packing densities from [21, Table I.1, pp. xix–xx], and Table 1, while Figure 2 shows ∆LP1 (c)/c. We believe that the truncation order in our calculations is high enough that these plots and table are indistinguishable from the fully optimized bounds; see Appendix B for how we calibrated the convergence rate. All of our data is available from https://hdl.handle.net/1721.1/125646, including truncation orders, scaling dimensions, and degeneracies.

The linear programming bound is sharp when d = 1, 2 (conjecturally), 8, or 24, and seemingly nowhere else. From the perspective of discrete geometry, one of the most mysterious aspects is the role of these special dimensions. Unlike some other cases of the conformal bootstrap (see, for example, [47, Section V.B.4]), the bound itself shows no sign of kinks or other non-analytic behavior at these points in Figure 1. Instead, the upper bound looks much the same there as elsewhere, and it is the packing densities that show anomalous behavior.

6Our primary interest is in large c, and the main role of c = 3/2 is to dash any hope of proving that the

dimension

0 4 8 12 16 20 24 28 32 36 40 44 48

0

| | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |Linear programming bound Record sphere packing Record lattice packing<br><br>| | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |


- −1
- −2
- −3
- −4
- −5
- −6
- −7
- −8


log(density)10

##### Figure 1: The linear programming bound for the sphere packing density.

- 0
- 1


| |∆LP1 (c)/c Lower bound<br><br>| | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |


∆(c)/c1

- 0 2 4 6 8 10 12 14 16 18 20 22 24


central charge c

##### Figure 2: The ratio ∆LP1 (c)/c, together with lower bounds from sphere packings.

dimension

- 1 2 4 8 16 32 64 128 256 512 1024 2048


0

| | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |Levenshtein Kabatyanskii-Levenshtein Linear programming bound Record sphere packing Scardicchio-StillingerTorquato<br><br>LP| | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |


- −0.1
- −0.2
- −0.3
- −0.4
- −0.5
- −0.6
- −0.7
- −0.8
- −0.9 −1


log(density)/dimension2

1

log2 − 2

KL

log4 − 32

1

Figure 3: A comparison of the linear programming bound with other bounds. The annotations on the right show the limits of the colored curves in high dimensions, including our conjectured limit for the linear programming bound from Conjecture 3.1.

Figures 1 and 2 faithfully reﬂect the qualitative properties of these bounds, but they are of limited use in extrapolating to high dimensions. For that purpose, a log-log plot is more eﬀective, as in Figure 3. This ﬁgure shows the linear programming bound and the record sphere packing densities from [21] in black. The green and red curves show the best bounds that have been analytically derived: the green curve is Levenshtein’s bound [48], and the red curve is the Kabatyanskii-Levenshtein bound [19], computed using Levenshtein’s universal bound for spherical codes [49, 50] and the approach of Cohn and Zhao [20] (we review these bounds in Sections 5.2 and 5.3). It is known that the linear programming bound is at least as strong as these bounds [8, 20], but no further analytic results are known. As shown in Figure 3, our numerical calculations indicate that the linear programming bound is not much stronger than the better of these two bounds.

The blue curve in Figure 3 is a lower bound for the linear programming bound due to Scardicchio, Stillinger, and Torquato [51], which is a variant of a bound obtained by Torquato and Stillinger [52]. No better lower bound is known for the linear programming bound in the limit as d → ∞, and the known lower bounds for the sphere packing density are much worse.

method works for all c. We have no conceptual explanation for why this case seems to diﬀer from all the others.

Table 1: Numerical comparison of the linear programming bound in Rd (denoted LP) with the Kabatyanskii-Levenshtein bound (denoted KL). The bounds are in the form (log2 density)/d, and are rounded rather than truncated.

d LP KL KL − LP Diﬀerence Ratio

1 0.00000 0.00000 0.00000 2 −0.07049 0.29248 0.36297 4 −0.15665 0.17511 0.33176

0.03122 8 −0.24737 −0.04879 0.19858

0.23 16 −0.33192 −0.21692 0.11501

0.13318

1.59 32 −0.40382 −0.33342 0.07040

0.08357

1.87 64 −0.46101 −0.41947 0.04154

0.04461

1.55 128 −0.50432 −0.47947 0.02485

0.02885

1.73 256 −0.53589 −0.52023 0.01566

0.01669

1.82 512 −0.55824 −0.54749 0.01075

0.00919

1.87 1024 −0.57370 −0.56553 0.00816

0.00491

1.90 2048 −0.58418 −0.57737 0.00682

0.00259

1.92 4096 −0.59120 −0.58508 0.00611

0.00135

1.92

0.00070

∞ ? −0.59906 ?

For example, the Minkowski-Hlawka bound says that there exist sphere packings of density at least 2−d in Rd, which amounts to the bottom edge of Figure 3; this exponential decay rate is the same as in the ideal glass phase of the hard sphere model (see [53, p. 247]), and no known lower bound improves on this rate. These lower bounds are obtained from probabilistic or averaging arguments, and as far as we are aware, no explicit construction in dimension 2048 or greater has been shown to achieve the Minkowski-Hlawka bound.

### 3.2 Extrapolation

The annotations on the right side of Figure 3 show the limits of the various curves as d → ∞. The limits of the green, red, and blue curves are known explicitly, and one can see that even d = 2048 is not especially close to the asymptotic limit as d → ∞. We know that the black curve always lies below the red curve, and it appears to be getting steadily closer. Thus, we expect the linear programming bound to be at most slightly better than the KabatyanskiiLevenshtein bound in the limit as d → ∞. What Figure 3 does not reveal is whether the gap in fact tends to zero.

To estimate the asymptotic gap between the red and black curves, it is helpful to examine numerical data. Table 1 shows the diﬀerence KL − LP between these two bounds, as well as the diﬀerences between consecutive values of KL − LP and their ratios. The KL − LP column does indeed seem to decrease for d ≥ 2, and we expect that it is converging towards

its limit at a rate proportional to 1/d. In that case, the diﬀerence column to its right should be decreasing towards zero at the same rate 1/d, and so the ratios in the last column should tend to 2. The behavior of the ratio column is not absolutely clear, but it does look like it may be increasing towards 2 beyond d = 32.

We therefore hypothesize that the diﬀerence column will continue to decrease by a factor between 1.92 and 2 in each additional row. In that case, the sum of all the entries below 0.00070 in the diﬀerence column must lie between

∞

0.00070 2n

= 0.00070 and

n=1

∞

- 0.00070

- 1.92n


< 0.00077. (3.1)

n=1

In other words, the KL − LP column will fall below 0.00611 by an amount between 0.00070 and 0.00077, and so its limiting value will be between 0.00534 and 0.00541. We conclude that the limit of the LP column must be −0.6044±0.0001 (i.e., between −0.6045 and −0.6043). In other words, the linear programming bound will be approximately 2−0.6044d when d is large.

- Conjecture 3.1. There exists a constant λ with 0.604 < λ < 0.605 such that the linear programming bound for the sphere packing density in Rd is 2−(λ+o(1))d as d → ∞ when the auxiliary function is fully optimized.

Of course we have no proof of this conjecture, or even a heuristic derivation. It is possible that the numbers could behave entirely diﬀerently when d is much larger, but that does not seem plausible. We are very conﬁdent in the ﬁrst three decimal places of the estimate 0.6044 for λ, and fairly conﬁdent in the fourth. In fact, we have a proposal for the exact constant:

- Conjecture 3.2. The constant λ in Conjecture 3.1 is given by 2−λ = e/(2π). Equivalently,


∆LP1 (c) c

lim

=

c→∞

1 π2

(3.2)

and

1 π

A−(d) √

=

, (3.3)

lim

d

d→∞

where A−(d) denotes the optimal radius for the −1 eigenfunction uncertainty principle in Rd.

Of course Conjecture 3.2 is speculative, and four digits of accuracy is far from enough to make a deﬁnitive argument for this value. The equivalent limits are much more appealing than the formula for λ, and their simplicity justiﬁes going out on a limb. We have no great faith in this conjecture, but it is worth noting that a simple formula ﬁts the data beautifully. For comparison, λ = 0.6044 ± 0.0001 would amount to

0.318287 < lim

d→∞

A−(d) √

< 0.318333, (3.4)

d

and 1/π = 0.318309....

Table 2: The ratio of the −1 eigenfunction uncertainty principle radius to the +1 radius.

d −1 radius +1 radius Ratio 4 1.2038 0.9660 1.2462 8 1.4142 1.2173 1.1618

16 1.7393 1.5812 1.1000 32 2.2241 2.1000 1.0591 64 2.9317 2.8359 1.0338

128 3.9515 3.8787 1.0188 256 5.4109 5.3565 1.0102 512 7.4905 7.4504 1.0054

1024 10.446 10.417 1.0028 2048 14.640 14.619 1.0014

Our calculations also support Conjecture 1.5 from [11], which says that the sign change radii for the +1 and −1 eigenfunction uncertainty principles in Rd are the same asymptotically as d → ∞. See Table 2 and https://hdl.handle.net/1721.1/125646 for the numerical data.7 In the notation of [11],

A+(d) √

lim

= lim

d

d→∞

d→∞

A−(d) √

. (3.5)

d

Speciﬁcally, the ratio A+(d)/A−(d) seems to be 1 + O(1/d).

## 4 Properties of the spectrum and degeneracies

The spectra of our numerically optimized solutions of the spinless modular bootstrap behave remarkably regularly when the central charge c is large. Figure 4 shows the scaling dimensions for c ≤ 64, with the sharp cases c = 1/2, 1, 4, and 12 highlighted. When c = 4 or 12, the scaling dimensions are positive integers, excluding 1 when c = 12. The green lines in the ﬁgure extrapolate these arithmetic progressions to other values of c. In other words, the n-th green line from the bottom amounts to ∆n = n + (c − 4)/8. While this equation never holds exactly except when c = 4 or 12, it is an excellent approximation when n is large and c ≥ 4. Later in this section we will examine how close this approximation is.

The equation ∆n = n + (c − 4)/8 amounts to the 1d generalized free fermion spectrum. This spectrum arose in analytic functionals for the 1d conformal bootstrap constructed by Maza´cˇ [26], which were generalized to a basis by Maza´cˇ and Paulos [54]. Hartman, Maza´cˇ, and Rastelli [9] discovered that these functionals could be adapted to the 2d modular bootstrap

7The reason why this table omits d = 1 and 2 is that we do not have good numerical data in these dimensions. See the end of Section 4 in [11].

scalingdimensions

35

| | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |


30

25

20

15

.

∆LP5 (c)

10

.

∆LP1 (c)

5

0

0 4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64 central charge c

Figure 4: The spectra ∆LPn (c) for 2 ≤ c ≤ 64 and c ∈ {1/2,1}, drawn in black. The dots highlight the spectra for c ∈ {1/2,1,4,12}, and the green lines show the 1d generalized free fermion spectra.

with U(1)c or Virasoro symmetry, and special cases were independently constructed by Rolen and Wagner [55] and by Feigenbaum, Grabner, and Hardin [56].

Figure 5 shows the sphere packing bounds obtained from these functionals. No proof is known that the functionals satisfy the required inequalities, and indeed they do not for 8 < d < 24; in particular, they would prove an impossibly good linear programming bound for d = 16 (see the dual bounds in [41]). However, the inequalities seem to hold for other values of d. Unfortunately, the resulting bounds are disappointing. The fact that the ∆LP1 (c) curve in Figure 4 bends below the free fermion line ∆1 = 1 + (c − 4)/8 is crucial for obtaining a strong bound, and the quality of the bound depends on the degree of deﬂection.

In contrast to the behavior for large c, the spectra for small c are much less regularly spaced. As we decrease c below 4, the scaling dimensions in Figure 4 start to diverge unpredictably from the green lines, and the behavior for c ∈ {1/2,1} is entirely diﬀerent. Our numerical techniques break down at c = 3/2, and it is presumably not a coincidence that this failure occurs at the transition between diﬀerent regimes. It would be interesting to explore this transition for 1 < c < 2.

dimension

1 2 4 8 16 32 64 128 256 512 1024 2048

0

Linear programming bound Hypothetical bound Record sphere packing

- −0.1
- −0.2
- −0.3
- −0.4
- −0.5
- −0.6


log(density)/dimension2

1+log π

log4 − 2

−0.7

##### Figure 5: The linear programming bound and the hypothetical bound

based on the 1d generalized free fermion spectrum ∆n(c) = n + (c − 4)/8.

200

| |∆LPn ,1(128)<br><br>.<br><br>∆LPn ,128(128) 1d generalized free fermions| | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


175

150

125

100

75

50

25

0

0 16 32 48 64 80 96 112 128 n

##### Figure 6: The spectrum for c = 128 computed using truncation order N = 1, 2, 4, ..., 128 (red through black) and the free fermion spectrum ∆n(c) = n + (c − 4)/8 (green).

1

0

0 2/π 4/π

- Figure 7: The probability density function for the normalized spectrum is 1 on [0,2/π] and x  → x−1/2(4/π − x)1/2 on [2/π,4/π].


### 4.1 Convergence to the free fermion spectrum

Figure 6 shows how the spectrum converges as we increase the truncation order N. The limiting values for ∆LPn ,N(c) as N → ∞ are quite close to the 1d generalized free fermion values, but there is a substantial divergence when n is large enough relative to N, as noted in [57, Section 3] and [12, Figure 2]. Although we have no proof, we can predict the form of this divergence. It occurs starting at n ∼ (2/π)N, with shape determined by the following conjecture:

- Conjecture 4.1. For each c ≥ 2, the distribution of the normalized spectrum ∆LPn ,N(c)/N with 1 ≤ n ≤ N converges as N → ∞ to the probability distribution on the interval [0,4/π] with density function 1 on [0,2/π] and x  → x−1/2(4/π−x)1/2 on [2/π,4/π], shown in Figure 7.


See Figure 8 for a comparison with numerical data for c = 4 and N = 128. The behavior is similar for all c ≥ 2, with slower convergence as c grows.

Conjecture 4.1 says that the distribution shifts from uniform to a beta distribution around n ∼ (2/π)N. The uniform distribution corresponds to the 1d generalized free fermion spectrum, and the beta distribution describes the root distribution of high-degree Laguerre polynomials (see [58, Theorem 1]). Speciﬁcally, if we normalize the roots of the highest-degree polynomial L(4cN−−1)1(4π∆) from the truncated crossing equation (2.23) by dividing by a factor of N, then their distribution converges as N → ∞ to the beta function on [0,4/π] with density x  → x−1/2(4/π − x)1/2/2. From this perspective, the transition in Conjecture 4.1 is between the uniform limiting behavior as N → ∞ and a generic root distribution corresponding to high-degree Fourier eigenfunctions.

Conjecture 4.1 gives the following description of the curves in Figure 6 via Theorem 4 in [59]. We wish to approximate ∆LPn ,N(c)/N as N → ∞ with n/N → α for some constant

- 0

- 1

- 2/π


0 2/π 4/π

Figure 8: The cumulative distribution functions for the normalized spectrum ∆LPn ,N(4)/N with 1 ≤ n ≤ N when N = 128 (red) and in the limit as N → ∞ (black).

α ∈ [0,1]. The conjecture says that

 

∆LPn ,N(c) N →

α if α ≤ 2/π, and (2/π)(1 + cosβ) if α ≥ 2/π,

(4.1)



where β is the solution of β−sinβ = (1−α)π/2 with 0 ≤ β ≤ π/2. We will give some motivation for the high-energy portion of this formula in Section 4.6, after discussing degeneracies.

### 4.2 Deviations from the free fermion spectrum

Aside from c = 4 or 12, the spectrum ∆LPn (c) is not exactly equal to the 1d generalized free fermion spectrum ∆n(c) = n + (c − 4)/8. Instead, we always ﬁnd some error in this approximation, and one natural question is whether the error tends to 0 as n → ∞. Figure 9 shows four test cases, namely c ∈ {16,20,24,28}. In each of these cases, the error |∆LPn (c) − (n+(c−4)/8)| becomes small, no more than 10−5 when n is large. However, there is a striking diﬀerence between two diﬀerent scenarios: when c = 16 or 24, the error stabilizes above zero, while it seems to converge to 0 when c = 20 or 28. We have no conceptual explanation of this behavior, which seems to be periodic modulo 8 as c varies, with multiples of 8 being the worst case and 4 modulo 8 being the best case (and the only case with convergence to zero). Note that c = 4 and 12 fall into the latter category.

Figure 10 shows another aspect of this periodicity. In this ﬁgure, we plot

|∆LPn (c) − (n + (c − 4)/8)|. (4.2)

ε(c) = max

2c≤n≤128

Here the upper bound of 128 for n should be viewed as a stand-in for inﬁnity, and the lower

22

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


20

18

16

14

12

10

8

6

4

2

0

0 16 32 48 64 80 96 112 128

n

##### Figure 9: The gaps log10(1/|∆n(c) − (n + (c − 4)/8)|) for c = 16 (black), c = 20 (red), c = 24 (green), and c = 28 (blue).

55

log2(1/ε(c)) c + log2(π)

50

45

40

35

30

25

20

15

10

- 4 8 12 16 20 24 28 32 36 central charge c

0

- 5


##### Figure 10: The maximum ε(c) of |∆LPn (c) − (n + (c − 4)/8)| over 2c ≤ n ≤ 128.

bound 2c is intended to exclude sporadic behavior for small n before convergence; in other words, we view ε(c) as an approximation to

|∆LPn (c) − (n + (c − 4)/8)|. (4.3)

limsup

n→∞

In the plot, there are singularities at c = 4 and 12 that correspond to ε(c) = 0, with similar cusps at c = 20, 28, and 36, and again we see the largest error terms when c is a multiple of 8. This unexpected periodicity shows that the spinless modular bootstrap has a much richer number-theoretic structure than is apparent from the smooth plot of ∆LP1 (c) in Figure 2.

We can summarize Figures 9 and 10 with the following conjecture:

- Conjecture 4.2. For c ≥ 4, the quantity


|∆LPn (c) − (n + (c − 4)/8)| (4.4)

limsup

n→∞

vanishes if and only if c is an integer congruent to 4 modulo 8, and there is a constant α such that

|∆LPn (c) − (n + (c − 4)/8)| ≤ α2−c (4.5) for all c ≥ 4. Furthermore, we can take α = 1/π + o(1) as c → ∞.

limsup

n→∞

### 4.3 Growth rate of the degeneracies

Solving the truncated crossing equation (2.23) yields not just scaling dimensions ∆LP1 ,N(c) but also corresponding degeneracies dLPn ,N(c), which converge as N → ∞ to the degeneracies dLPn (c) of a hypothetical CFT that attains the spinless modular bootstrap bound. For c ≤ 50 and c  ∈ {1/2,1,4,12}, numerical calculations show that these degeneracies are not integers, and thus they cannot come from an actual CFT.8 For larger c, it is diﬃcult to assess integrality, because the degeneracies grow exponentially as c → ∞ and must therefore be computed to high precision.

The cumulative growth rate of the degeneracies is determined by modularity as follows. Because η(−1/τ) = (τ/i)1/2η(τ), the modular invariance of the partition function Z(τ) = η(τ)−2c ∆ d∆e2πiτ∆ implies the identity

∆

d∆e2πiτ∆ = (i/τ)c

∆

e−2πi∆/τ. (4.6)

##### If we set τ = iβ/(2π) and let β → 0, we ﬁnd that

∆

d∆e−β∆ ∼ (2π/β)c. (4.7)

8They could still come from a sphere packing. In that case dn would be the average number of sphere centers at distance √2∆n from a given sphere center, which need not be an integer.

Now the Karamata Tauberian theorem [60, Theorem 4.3 of Chapter V] implies that

(2πA)c Γ(c + 1)

d∆ ∼

∆≤A

as A → ∞. In other words, the function

(2π)c∆c−1 Γ(c)

ρc(∆) =

is the U(1)c analogue of the Cardy formula [61] for degeneracies, because

(4.8)

(4.9)

A

(2πA)c Γ(c + 1)

d∆ρc(∆) =

. (4.10)

0

A similar formula applies to operator-product coeﬃcients that appear in the bootstrap equations for conformal correlators [62].

Because the scaling dimensions ∆LPn (c) are uniformly spaced with distance 1 asymptotically, we expect that dLPn (c) will be roughly ρc(∆LPn (c)) as n → ∞. The asymptotic formula (4.8) gives a sense in which this approximation is true on average, but we will see that the precise behavior is far more delicate. In the Virasoro case, a more ﬁne-grained understanding of the asymptotic spectrum has been obtained recently using complex Tauberian theorems [63, 64, 65, 66, 67]. It would be interesting to do the same for sphere packing. This could perhaps explain the linear portion of the large-c spectrum, where the level spacing is very close to 1.

### 4.4 Degeneracies for c = 4 and 12

The degeneracies dLPn (4) and dLPn (12) are the coeﬃcients of the theta series of the E8 and Leech lattices, respectively. Much is known about these modular forms, including precise descriptions of their coeﬃcients (see, for example, [21, p. 122 and p. 134]). The degeneracies are well understood, but far more subtle than the scaling dimensions ∆LPn (4) = n and ∆LPn (12) = n+1.

Figure 11 shows the normalized degeneracies dLPn (4)/ρ4(∆LPn (4)) for c = 4. They are bounded above and below, but do not converge to 1; instead, they are strictly bounded away from 1. The most noteworthy aspect of Figure 11 is that the normalized degeneracies are almost, but not quite, periodic.9 This near periodicity is explained by a classical formula for coeﬃcients of Eisenstein series: dLPn (4)/ρ4(∆LPn (4)) = σ3(n)/(ζ(4)n3), where σk(n) denotes the sum of the k-th powers of the divisors of n, and ζ is the Riemann zeta function. This function is not periodic, but for each ε > 0, there exists a natural number m such that if n1 ≡ n2 (mod m), then |σ3(n1)/n31 −σ3(n2)/n32| < ε. In other words, for each ε > 0 it is approximately periodic to within ε, with the period length growing as ε → 0. Similarly, the function n  → dLPn (12)/ρ12(∆LPn (12)) is the sum of the almost periodic function n  → σ11(n)/(ζ(12)n3)

9See [68, Theorem 5.13A.1] for the theory of almost periodic functions.

1.2

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


normalizeddegeneracy

- 0.8
- 1


0 32 64 96 128 160 192 224 256

n

Figure 11: The normalized degeneracies dLPn (4)/ρ4(∆LPn (4)) for 1 ≤ n ≤ 256. As n → ∞, they ﬂuctuate between 1/ζ(4) = 0.9239... and ζ(3)/ζ(4) = 1.1106..., shown with gray lines, and they are bounded away from 1.

and a term converging to zero as n → ∞.

### 4.5 Degeneracies for arbitrary c

The unexpected periodicity modulo 8 for scaling dimensions has a counterpart for degeneracies, as shown in Figure 12. Here the multiples of 8 are the best case for the accuracy of the U(1)c Cardy formula, while integers that are 4 modulo 8 are the worst case. Unlike the case of scaling dimensions, the cusps in Figure 12 do not seem to correspond to zero error in the limit

- as n → ∞. Instead, see Figure 13. Perhaps this discrepancy indicates that ρc(∆) should be replaced with some better approximation.


Based on this data and the cases c = 4 and 12, we make the following conjecture, which is a more precise analogue of Conjecture 4.2:

#### Conjecture 4.3. For c > 2,

dLPn (c) ρc(∆LPn (c)) ≤

ζ(c − 1) ζ(c)

= 1 + 2−c + O(3−c) (4.11)

limsup

n→∞

and

dLPn (c) ρc(∆LPn (c)) ≥

1 ζ(c)

= 1 − 2−c + O(3−c), (4.12) with equality whenever c is an integer that is congruent to 4 modulo 8.

liminf

n→∞

Equality provably holds for c = 4 or 12.

50

| |log2(1/δ(c)) c| | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


45

40

35

30

25

20

15

10

- 4 8 12 16 20 24 28 32 36 central charge c

0

- 5


##### Figure 12: The maximum δ(c) of |dLPn (c)/ρc(∆LPn (c)) − 1| over 2c ≤ n ≤ 128.

- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10


| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


0 16 32 48 64 80 96 112 128 n

##### Figure 13: The gaps log10(1/|dLPn (c)/ρc(∆LPn (c))−1|) for c = 8 (black), c = 12 (red), c = 16 (green), and c = 20 (blue).

### 4.6 Possible explanation of the high-energy spectrum

The formula for the upper portion of the high-energy spectrum, given by the second line in (4.1), was motivated by the following calculation. It does not fully explain the formula, but it indicates why it is a reasonable guess.

The counterpart of the Cardy formula in terms of functionals acting on the crossing equation is the integral identity

∞

(2π)c∆(c−1) Γ(c)

e−2π∆L(kc−1)(4π∆) = (−1)kL(kc−1)(0), (4.13)

d∆

0

which is the evaluation at 0 of the condition of being a radial Fourier eigenfunction. We will use this identity to generate an exact solution of the truncated crossing equations, which has too many states but is otherwise suggestive of the optimal solution.

For small enough k, we can evaluate the integral exactly using the Gauss-Laguerre quadrature formula

n

∞

dxxc−1e−xp(x) =

wmp(xm), (4.14)

0

m=1

which holds for all polynomials p of degree at most 2n − 1 if we use the roots of L(nc−1)(x) as the quadrature nodes xm with weights

Γ(n + c)xm n!(n + 1)2(L(nc+1−1)(xm))2

wm =

. (4.15)

If we take n = 2N and p(x) = L(kc−1)(2x), we ﬁnd that for k ≤ 4N − 1,

∞

(2π)c∆(c−1) Γ(c)

e−2π∆L(kc−1)(4π∆) =

d∆

0

2N

dmL(kc−1)(4π∆m), (4.16)

m=1

where dm = wm/Γ(c) and the dimensions ∆m satisfy L(2cN−1)(2π∆m) = 0. In other words, we have generated a solution to the equations

L(kc−1)(0) +

2N

dmL(kc−1)(4π∆m) = 0 (4.17)

m=1

for odd k ≤ 4N − 1. This solution has 2N + 1 states, while our numerical method involves ﬁnding a solution to these truncated crossing equations with only N +1 states, so this solution has no direct bearing on the bound. However we observe numerically that the high energy spectrum approximately agrees. The roots of the Laguerre polynomial L(2cN−1)(2π∆) for large N and ∆ are given by the beta distribution described in Section 4.1, which motivates its appearance.

## 5 Spherical codes and implied kissing numbers

In sphere packing terms, the scaling dimensions ∆n measure the distances √2∆n between distinct sphere centers in the packing, and the corresponding degeneracy is the average number of centers at that distance from a given center. In particular, the ﬁrst degeneracy d1 is the average number of tangencies for spheres in the packing, i.e., the average kissing number of the packing. De Laat, Oliveira, and Vallentin [69] showed how to strengthen the linear programming bound for sphere packing by incorporating geometric bounds for the degeneracies, which go beyond the modular invariance of the partition function. In this section, we will use this idea systematically to explore when the linear programming bound can be sharp and how to improve on it. Along the way, we will review the Kabatyanskii-Levenshtein bound.

As motivation for this line of work, consider the implied kissing number dLP1 (d/2), which is the average kissing number in a hypothetical d-dimensional packing achieving the linear programming bound. When d = 1, 2, 8, or 24, we of course obtain the kissing number of the optimal packing, but in general we obtain unrealistic numbers. For example, when d = 4 the implied kissing number is 26.43..., which exceeds Musin’s optimal bound of 24 for the four-dimensional kissing number [70]; it is therefore impossible for any packing to achieve the exact linear programming bound in R4. As Figure 14 shows, the implied kissing number is impossibly high for every d ≤ 24 except the known sharp cases. Within this range of dimensions, it perfectly delineates which cases are sharp.

Figure 15 shows how the implied kissing number grows in high dimensions. Comparing it with upper bounds turns out to be surprisingly subtle, and we will do so in Figure 16 once we have explained more about the needed bounds. Aside from low dimensions, Figure 15 looks similar to Figure 3, and that is not a coincidence: Table 3 indicates that the implied kissing number is 2d+o(d) times the linear programming bound as d → ∞. This relationship is easily explained using the U(1)c Cardy formula, because the sphere packing density is ρc(∆1)∆1/(c4c) in terms of the spectral gap ∆1 and c = d/2. We can approximate the implied kissing number dLP1 (c) by ρc(∆LP1 (c)) using the Cardy formula; because of the size of ∆LP1 (c) we expect some error, but the error factor should be subexponential in c, in fact roughly ∆LP2 (c) − ∆LP1 (c). We conclude that the linear programming bound for the packing density is dLP1 (c)/(4 + o(1))c as c → ∞, which is the desired relationship.

To prove bounds for kissing numbers, the relevant optimization problem is the spherical code problem, which is a compact analogue of the sphere packing problem. In dimension d and with minimal angle θ this problem asks how large a subset C of the unit sphere in Rd can be if x,y ≥ s for all distinct x,y ∈ C, where s = cosθ. In other words, all points in C must be separated by at least a distance of θ along the surface of the sphere, and so C yields a packing with spherical caps of radius θ/2. Such a set is called a spherical code with minimal angle θ. The kissing problem amounts to the case θ = π/3; note that here we are considering the kissing problem for a single sphere, rather than averaged over a packing in Euclidean space.

log(kissingnumber)10

- 0
- 1
- 2
- 3
- 4
- 5
- 6


| |Implied kissing number Upper bound Record kissing number| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


0 4 8 12 16 20 24 dimension

Figure 14: The implied kissing number from the linear programming bound, compared with the best upper bound known for the actual kissing number [71] and the current record [21].

Let A(d,s) be the largest possible size of such a code. Delsarte, Goethals, and Seidel [74] introduced a linear programming bound for A(d,s), which Kabatyanskii and Levenshtein [19] used to obtain the best sphere packing density bounds known in Euclidean space.

After brieﬂy reviewing this linear programming bound, we will discuss two applications of spherical codes to the sphere packing problem, followed by a new average kissing bound. First we discuss the Kabatyanskii-Levenshtein bound, using the approach from [50]. Then we discuss a strengthening of the linear programming bound for the sphere packing problem through bounds for spherical codes, and its implications for when the bound can be tight. We conclude with a linear programming bound for the average kissing number.

The results of this section rely on the geometry of the sphere packing problem and do not appear to have any direct application to CFTs. On the other hand, conceptually, upper bounds on the average kissing number are similar to upper bounds on operator-product coeﬃcients often considered in the bootstrap literature (e.g., [75, 76]). It is also our hope that the methods in this section (in particular, the application of the Christoﬀel-Darboux formula to produce positive auxiliary functions) will inspire new analytic approaches to the conformal bootstrap.

log(kissingnumber)/dimension2

- 0

- 0.5
- 1


- 1.5


| |Implied kissing number Record kissing number Volume lower bound| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |


1 2 4 8 16 32 64 128 256 512 1024 2048 dimension

Figure 15: The implied kissing number in high dimensions, compared with the record kissing number [21, 72] and the excluded volume lower bound for the kissing number from [73].

### 5.1 The linear programming bound

The analogue of the radial Fourier transform on the surface of a sphere is the expansion in terms of zonal spherical harmonics, which uses the following orthogonal polynomials.10 Let d be the dimension of the spherical code, and let a and b be nonnegative integers. (We can take a = b = 0 for now, but we will make use of a and b in the Kabatyanskii-Levenshtein bound.)

Let

Γ(a + b + d − 1) 2a+b+d−2Γ(a + d−21)Γ(b + d−21)

(1 − t)a(1 + t)b(1 − t2)(d−3)/2, (5.1)

wa,b(t) =

where the normalization is chosen so that − 11 dtwa,b(t) = 1. Deﬁne the orthogonal polynomials Qa,bi (t) with deg(Qa,bi ) = i and positive leading coeﬃcients by

1

dtQa,bi (t)Qa,bj (t)wa,b(t) = δi,j (5.2)

−1

for i,j ≥ 0. Up to normalization, these polynomials are the Jacobi polynomials with parameters

10One key conceptual diﬀerence between spheres and Euclidean space is that Rd is its own Pontryagin dual, which means Fourier eigenfunctions make sense, while that concept does not apply to spheres.

Table 3: Numerical comparison of the linear programming bound for the sphere packing density in Rd (denoted LP) with the implied kissing number (denoted IK), both in the form log2(·)/d.

d LP IK 1 + LP − IK

- 1 0.00000 1.00000 0.00000
- 2 −0.07049 1.29248 −0.36297 4 −0.15665 1.18103 −0.33768 8 −0.24737 0.98836 −0.23573


16 −0.33192 0.81510 −0.14702 32 −0.40382 0.68279 −0.08661 64 −0.46101 0.58837 −0.04937

128 −0.50432 0.52325 −0.02757 256 −0.53589 0.47929 −0.01518 512 −0.55824 0.45003 −0.00827

1024 −0.57370 0.43077 −0.00447 2048 −0.58418 0.41822 −0.00240 4096 −0.59120 0.41009 −0.00128

∞ −0.6044 0.3956 0.00000

(d − 3)/2 + a and (d − 3)/2 + b.

The parameters a = b = 0 are particularly important, and the polynomials Qi := Q0i,0 are known as the ultraspherical polynomials in dimension d. For a continuous function f : [−1,1] → R,

1

dtf(t)w0,0(t) =

f0 :=

dµ(x)f( x,e ), (5.3)

Sd−1

−1

where e ∈ Sd−1 is an arbitrary point and µ is the surface measure on the sphere Sd−1, normalized so that µ(Sd−1) = 1. Therefore the polynomials Qi are orthogonal if we think of

- them as zonal functions on Sd−1, i.e., functions x  → Qi( x,e ) invariant under the stabilizer subgroup of O(d) with respect to e. Moreover, these polynomials are of positive type: for all ﬁnite C ⊆ Sd−1 and all coeﬃcients cx ∈ R for x ∈ C,


cxcyQi( x,y ) ≥ 0. (5.4)

x,y∈C

This inequality follows from the addition formula

Qi( x,y ) Qi(1)

1 ri

=

ri

vi,j(x)vi,j(y), (5.5)

j=1

where the functions vi,j : Rd → R for j = 1,...,ri are an orthonormal basis of the spherical

harmonics of degree i (see [77, Theorem 9.6.3]); speciﬁcally, the addition formula shows that the left side of (5.4) is a square and therefore nonnegative.

The linear programming bound for spherical codes converts an auxiliary function into an upper bound on the greatest size of a spherical code:

Theorem 5.1 ([74]). Let f : [−1,1] → R be a continuous function and s ∈ [−1,1]. If f is of positive type as a zonal function on Sd−1, f(t) ≤ 0 for t ∈ [−1,s], and f0 = 0, then A(d,s) is

- at most f(1)/f0. By Schoenberg’s theorem [78], every continuous function f : [−1,1] → R of positive type


is of the form f(x) = ∞n=0 fnQn(x) with fn ≥ 0, where convergence is uniform and absolute. Therefore the linear programming bound can be approximated arbitrarily well by the minimum

of f(1)/f0 over functions f of the form

f(t) =

N

fnQn(t) (5.6)

n=0

with f0 > 0, f1,...,fN ≥ 0, and f(t) ≤ 0 for t ∈ [−1,s].

One can optimize this bound numerically for given d and N using semideﬁnite programming. Speciﬁcally, we can create a semideﬁnite program where f0,...,fN are one-by-one positive semideﬁnite matrices, and the inequality constraint is modeled as

 

−v0(t)TXv0(t) − (t + 1)(s − t)v1(t)TY v1(t) if N is even, and −(t + 1)v0(t)TXv0(t) − (s − t)v0(t)TY v0(t) if N is odd,

f(t) =

(5.7)



where X and Y are positive semideﬁnite matrices and

vk(t) = (Q0(t),...,Q N/2 −k(t)). (5.8)

If we additionally require f0 = 1, then the objective is f(1), which means we are minimizing a linear functional over positive semideﬁnite matrices with linear constraints. This semideﬁnite program can be solved numerically on a computer.

Shtrom [79] computed the exact linear programming bound for the kissing number A(d,1/2) when d ≤ 146, by determining the optimal value of N, beyond which there is no improvement. We have extended these computations to d ≤ 424 using N = 95, which appears to be high enough in this range of dimensions and in any case should closely approximate the optimum. Figure 16 shows the ratio of the implied kissing number to this upper bound. They are very close to each other in size, but their precise ratio seems diﬃcult to predict, and we do not know what happens as d → ∞. No sphere packing can match the linear programming bound for density when this ratio is strictly greater than 1. Our initial hope was that this condition would rule out every dimension d > 24, but it does not. Instead, further progress may depend on more powerful bounds for the kissing number, such as semideﬁnite programming bounds [80, 71].

1.25

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |


ratio

1

0.9

0

8

180

424

24

192

282

294

dimension

Figure 16: The ratio of the implied kissing number to the linear programming bound for the kissing number. It dips below 1 at dimensions 180–181, 192, 282–283, 294–296, and many beyond that.

This approach can rule out exact equality in the linear programming bound for packing density, but it does not give a quantitative improvement. We will return to the problem of improving the density bound, once we explain Levenshtein’s universal bound and the Kabatyanskii-Levenshtein bound.

- 5.2 Levenshtein’s universal bound Levenshtein’s universal bound is the best bound that has been analytically derived from


Theorem 5.1; our explanation follows Section 5.4 in [50]. Let ta,bk ∈ [−1,1) be the largest root of Qa,bk (t), where we set t10,1 = −1. One can show that

tk1,−11 < t1k,0 < tk1,1 (5.9) for all k ≥ 1 (see (5.89) in [50]). For s ∈ [−1,1), deﬁne the function

 

(t − s) Kk1−,01(t,s) 2 if tk1,−11 ≤ s < tk1,0, and (t + 1)(t − s) Kk1−,11(t,s) 2 if tk1,0 ≤ s < t1k,1,

f(s)(t) =

(5.10)



where

k−1

Kka,b−1(t,s) =

Qa,bi (t)Qa,bi (s). (5.11)

i=0

This function f(s) will prove a bound in Theorem 5.1, once we verify the hypotheses of the theorem (see Theorem 5.42 in [50] for more details than we give here). By construction,

- f(s)(t) ≤ 0 for −1 ≤ t ≤ s. To show f(s)(t) is of positive type for tk1,−11 ≤ s < tk1,0, one can


check that for such s,

Q10,0(s) > 0, ..., Qk1,−01(s) > 0, and Q1k,0(s) < 0. (5.12)

Since Q1k,0(t) is of positive type, these inequalities show Kk1−,01(t,s) is of positive type as a function of t. Moreover, they also show (t − s)Kk1−,01(t,s) is of positive type as a function of t by using the Christoﬀel-Darboux formula, which says

(t − s)Kk1−,01(t,s) = (ck−1/ck) Qk1,0(t)Q1k,−01(s) − Qk1,0(s)Q1k,−01(t) , (5.13)

where ck > 0 is the leading coeﬃcient of Q1k,0. Since the product of functions of positive type is also of positive type, it follows that f(s)(t) is of positive type for tk1,−11 ≤ s < tk1,0. By using the property that

(t + 1)Qi1,1(t)Q1j,1(t) (5.14) is of positive type, this argument can be extended to show f(s)(t) is of positive type for all s ∈ [−1,1].

Thus, these function can be used as auxiliary functions for Theorem 5.1, which gives Levenshtein’s universal bound for the sphere. In terms of the normalized polynomials Qi(s) = Qi(s)/Qi(1), we arrive at the bound

 

d−1 − Qk(1−−1(ss))Q−Qk(s)

k(s) if t1k,−11 ≤ s < t1k,0, and

k+d−3 k−1

2k+d−3

A(d,s) ≤

(5.15)



d−1 − (1+(1−ss)()(QQk(s)−Qk+1(s))

k(s)+Qk+1(s)) if tk1,0 ≤ s < tk1,1.

k+d−2 k

2k+d−1

In certain cases this bound is the best that can be obtained from Theorem 5.1, but in general it does not fully optimize the choice of auxiliary function.

### 5.3 The Kabatyanskii-Levenshtein bound

The following geometric inequality shows how the sphere packing density ∆Rd in Rd can be bounded using A(d,s):

sind(θ/2)A(d,cosθ) = min

∆Rd ≤ min

π/3≤θ≤π

−1≤s≤1/2

- 1 − s

- 2


d/2

A(d,s) (5.16)

(see (6.9) in [50] or Proposition 2.1 in [20]).

To obtain a good bound for ﬁxed d, this inequality can be combined with Levenshtein’s universal bound for A(d,s), where the best value of s can be found by optimizing a piecewise diﬀerentiable function. The resulting bound is the one shown as the Kabatyanskii-Levenshtein bound in Figure 3, although Kabatyanskii and Levenshtein [19] used a slightly worse bound for A(d,s) as well as for ∆Rd in terms of A(d,s).

To obtain an asymptotic bound as d → ∞, we can use the inequality

f(tk1,1)(1) f(t

d + k − 1 k

A(d,s) ≤ A(d,tk1,1) ≤

= 2

1,1 k )

0

when s ≤ t1k,1 (see (6.13) in [50]). If k,d → ∞ with k/d → α, then

2 α(1 + α) 2α + 1

tk1,1 →

by Corollary 5.17 in [50]. For θ < π/2, taking

(5.17)

(5.18)

1 − sinθ 2sinθ

α =

ensures that t1k,1 → cosθ, and applying Stirling’s formula shows that

1 + sinθ 2sinθ

1 d

log2 A(d,cosθ) ≤

log2

1 − sinθ 2sinθ

1 + sinθ 2sinθ −

log2

1 − sinθ 2sinθ

(5.19)

+ o(1) (5.20)

- as d → ∞. It now follows from (5.16) that the sphere packing density is at most 2−(κ+o(1))d, where

κ = −log2 sin

θ 2 −

1 + sinθ 2sinθ

log2

1 + sinθ 2sinθ

+

1 − sinθ 2sinθ

log2

1 − sinθ 2sinθ

. (5.21) Optimizing for the best choice of θ between π/3 and π/2 yields the root θ = 1.09951240... of secθ + tanθ = e(tanθ+sinθ)/2, (5.22)

- at which point we obtain the Kabatyanskii-Levenshtein bound κ = 0.59905576.... Cohn and Zhao [20] gave a general transformation showing that any bound obtained from


- Theorem 5.1 and (5.16) can also be obtained directly from the Euclidean linear programming bound. Thus, there is no need to use spherical codes to obtain the Kabatyanskii-Levenshtein bound. However, the transformation sheds little additional light on this bound, and it is diﬃcult to see how someone might think of it without using spherical codes.


### 5.4 Implied kissing numbers

One can strengthen the linear programming bound by taking into account constraints on spherical codes. The following relaxation of the kissing number will prove useful in doing so. Let C be the set of sphere centers in a packing. For x ∈ C and r ≥ 0, let

Nx(r) = #{y ∈ C : 0 < |x − y| ≤ r}, (5.23)

and let N(r) be the average of Nx(r) over x ∈ C (we can restrict our attention to periodic packings, so that this average is well deﬁned). If r0 is the minimal distance in C, then N(r0)

is the average kissing number of C, and for t > 0 we deﬁne the average t-neighbor number to be N(tr0). In other words, the average kissing number is the average 1-neighbor number.

The following strengthening of the linear programming bound is a special case of Theorem 1.4 in [69], where it was used to give improved bounds in dimensions 4 through 7 and 9. The proof in [69] amounts to retaining more terms in the Poisson summation argument from [8].

- Theorem 5.2 ([69]). Let g: Rd → R be a radial Schwartz function, and suppose that g satisﬁes the following inequalities for some η ≥ 0 and s > r > 0:


- (1) g(0) > 0 and g(0) > 0,
- (2) g(x) ≤ ηg(0) for r ≤ |x| ≤ s,
- (3) g(x) ≤ 0 for |x| ≥ s, and
- (4) g(y) ≥ 0 for all y.


Suppose furthermore that every sphere packing in Rd has average s/r-neighbor number at most

- M. Then the sphere packing density in Rd is at most


πd/2 (d/2)!

r 2

d g(0) g(0)

(1 + ηM). (5.24)

The linear programming bound is equivalent to taking η = 0. The extra ﬂexibility of being able to choose g(0) and g(0) is irrelevant, because we can rescale g and its input variable, but it will be convenient below.

When the implied kissing number is impossibly large, we can apply Theorem 5.2 to improve on the linear programming bound from Theorem 2.1 as follows. Suppose h is a Schwartz function satisfying the hypotheses of the linear programming bound with radius r. One can check by a rescaling argument that the average kissing number of any sphere packing that achieves this bound must be

d rh (r)

K = −

, (5.25)

where h (r) denotes the radial derivative at radius r (see Lemma 5.1 in [57]). Thus, if h is the optimal auxiliary function in the bound, then K must be the implied kissing number.

Suppose furthermore that for some t > 1 we can prove an upper bound B for the average t-neighbor number in every packing in Rd with B < K. For example, B could be an upper bound for A(d,cosθ) for some θ > π/3, which can be arbitrarily close to π/3.

Given such a bound B < K, Theorem 5.2 proves a strictly stronger density bound than Theorem 2.1 using h, as follows. Let s = (1 + ε)r for some small ε > 0, and deﬁne g by

- g(x) = h(x/(1+ε)). Then g satisﬁes the hypotheses of Theorem 5.2 with η = −rh (r)ε+O(ε2),


- g(0) = 1, and g(0) = (1 + ε)d = 1 + dε + O(ε2). (5.26)


If ε is small enough, then we can take M = B in Theorem 5.2, and

1 − rh (r)Bε + O(ε2) 1 + dε + O(ε2)

g(0) g(0)

= 1 + d(B/K − 1)ε + O(ε2), (5.27)

(1 + ηM) =

which is less than 1 when ε is suﬃciently small, because B < K. The improvement here is not large, but the resulting density bound is strictly better than that from Theorem 2.1. Thus, Figure 16 shows that we can extend the improved density bound from [69] to 10 ≤ d ≤ 23, 25 ≤ d ≤ 179, and a number of larger values of d. However, we do not know what happens as d → ∞.

### 5.5 Bounds for the average kissing number

The implied kissing number has a concrete geometric meaning, beyond being the average kissing number of a hypothetical packing. It turns out to be an upper bound for the average kissing number of any sphere packing, subject to some conjectures about interpolation. The key tool is the following theorem, which is the Euclidean analogue of Proposition 4.1 in [81] by Bourque and Petri.

- Theorem 5.3. Let f : Rd → R be a radial Schwartz function and r > 0, and suppose that f satisﬁes the following inequalities:


- (1) f(r) < 0,
- (2) f(x) ≤ 0 for |x| ≥ r, and
- (3) f(y) ≥ 0 for all y.


Then the average kissing number of any d-dimensional sphere packing is at most

f(0) f(r)

−

. (5.28)

Here f(r) denotes the value of f(x) when |x| = r.

Proof. It suﬃces to prove the inequality for ﬁnite packings and take a limit. Let C be any ﬁnite subset of Rd with minimal distance r, and let

N = #{(x,y) ∈ C2 : |x − y| = r}/|C| (5.29)

be its average kissing number. Then Fourier inversion implies that

while

f(|x1 − x2|) =

x1,x2∈C

dy f(y)

Rd

e2πi x,y

x∈C

2

≥ 0, (5.30)

f(|x1 − x2|) ≤ |C|f(0) + N|C|f(r) (5.31)

x1,x2∈C

thanks to the inequalities for f. By combining these two bounds, we conclude that N ≤ −f(0)/f(r).

| |
|---|


One can also prove this theorem using Poisson summation, along the lines of [8] or [81]. The conditions for equality are similar to those for the linear programming bound for packing density, if we assume self-duality.11 Speciﬁcally, equality holds iﬀ f vanishes at radius rn := √2∆n for n ≥ 2, f vanishes at rn for n ≥ 0 (with r0 = 0), r = r1, and

- f (r1) = 0 (because otherwise shifting r would improve the bound). For comparison, the equality conditions for h in Theorem 2.1 are identical, except that the conditions f (r1) = 0 and f(0) = 0 are replaced with h(r1) = 0.

Suppose rn = 2∆LPn (d/2) and dn = dLPn (d/2) come from the optimal solution to the linear programming bound in Rd. The crossing equation says that

n≥0

dnf(rn) =

n≥0

dn f(rn) (5.32)

for every radial Schwartz function f : Rd → R. If f satisﬁes the equality conditions for Theorem 5.3, then this equation reduces to

f(0) + d1f(r1) = 0. (5.33)

In other words, the bound −f(0)/f(r1) for the average kissing number is d1, as desired.

When should such a function f exist and satisfy the hypotheses of Theorem 5.3? First, note that the condition f(0) = 0 is redundant, for the following reason. If we let F(x) = |x|f (x), then F(y) = −d f(y) − |y| f (y). The other conditions on f guarantee that F(0) = F(rn) = F(rn) = 0 for n ≥ 1, and then the crossing equation implies that F(0) = 0 and hence f(0) = 0. What we need is for f to satisfy the same equality conditions as h, except for changing h(r1) = 0 to f (r1) = 0.

These conditions arise naturally in interpolation problems [82, 44]. Speciﬁcally, Open Problem 7.3 from [44] raised the question of whether radial Schwartz functions g: Rd → R are uniquely determined by the values and radial derivatives of g and g at the radii rn for n ≥ 1. While this assertion fails for d ≤ 2 and is diﬃcult to test for d = 3, it seems to hold numerically for d ≥ 4. Proving or disproving it would be an important step forward in our understanding of the modular bootstrap.

The conditions on f and h mean they are part of an interpolation basis for reconstructing

- g from these values, since all but one of the values must vanish for f and h. Thus, Theorem 5.3 gives a natural geometric interpretation for one of the basis functions, just as Theorem 2.1 does.


Aside from d = 8 or 24 (in which case [44] proves an interpolation theorem), we do not know how to prove that an interpolation basis exists, or that the basis functions satisfy the

11This is the same issue as the conjectured agreement between the linear programming bound and the −1 eigenfunction uncertainty principle.

right sign conditions for these theorems. However, the numerical evidence indicates that both are true. If so, the implied kissing number is an upper bound for the average kissing number of every sphere packing.

This relationship has a pleasing consequence: in each dimension, either the implied kissing number is the best bound known for the average kissing number, or we can use a better bound in Theorem 5.2 to improve on the packing density bound.12 In other words, if we fail

- to improve on the linear programming bound for density, it can only be because we have obtained an excellent bound for the average kissing number.


## A The limiting case of the spinless modular bootstrap

In this appendix, we explain why ∆gap is an upper bound for the spectral gap in the spinless modular bootstrap even if ω(Φ0) = 0 (in the notation of Section 2.1). We expect that any such functional ω is the limit of functionals with ω(Φ0) > 0, but it is not clear how to justify that expectation. Instead, we can use essentially the same argument as the proof of Proposition 2.4 in [11]. We will translate it into modular bootstrap terms for the convenience of the reader.

First, we note that the spectrum 0 = ∆0 < ∆1 < ∆2 < ··· must satisfy

∆j+1 ∆j

lim

= 1, (A.1)

j→∞

since otherwise (4.8) could not hold for ∆j < A < ∆j+1 with j large.

Now suppose ω is a linear functional such that ω(Φ0) ≥ 0, ω(Φ∆) ≥ 0 whenever ∆ ≥ ∆gap, and ω(Φ∆) is not identically zero. We wish to obtain a contradiction if ∆1 > ∆gap. The crossing equation

ω(Φ0) +

d∆ω(Φ∆) = 0 (A.2)

∆>0

shows that ω(Φ∆j) must vanish for each j, but that does not directly yield a contradiction.

Instead, for each constant λ ≥ 1 we will replace ω with a modiﬁed functional ωλ such that ωλ(Φ∆) = ω(Φλ∆) + λ−cω(Φ∆/λ). To see why this is possible, let f(r) = ω(Φr2/2). As explained in Section 2, f is a −1 eigenfunction for the radial Fourier transform in 2c dimensions,

and conversely any such function arises for a suitable choice of ω. Let fλ(r) = f(λ1/2r), so that fλ(r) = λ−c f(r/λ1/2) = −λ−cf(r/λ1/2), and deﬁne ωλ by ωλ(Φr2/2) = fλ(r) − fλ(r) = f(λ1/2r) + λ−cf(r/λ1/2), which works because fλ − fλ is again a −1 eigenfunction.

This new functional satisﬁes ωλ(Φ0) ≥ 0 and ωλ(Φ∆) ≥ 0 whenever ∆ ≥ λ∆gap. Furthermore, the only way ωλ(Φ∆) can vanish at a point ∆ ≥ λ∆gap is if ω(Φλ∆) = ω(Φ∆/λ) = 0.

Now suppose ∆1 > ∆gap, and let λgap = ∆1/∆gap. Then we conclude that ω(Φ∆) = 0 whenever ∆ is in one of the intervals (λ−gap1 ∆j,λgap∆j). Because limj→∞ ∆j+1/∆j = 1, these intervals cover an entire half-line [R,∞) for some R > 0. However, an eigenfunction of the Fourier transform cannot have compact support unless it vanishes identically, because it must

12Technically we need a bound for the average t-neighbor number for some t > 1, but that is practically the same as a bound for t = 1.

dimension

1 2 4 8 16 32 64 128 256 512 1024 2048

0

| | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |


- −0.1
- −0.2
- −0.3
- −0.4
- −0.5
- −0.6


log(density)/dimension2

1

log4 − 1

KL

−0.7

Figure 17: Density bounds based on N = 1, 2, 4, 8, ..., 512 (colored red through black).

be an entire function if it (equivalently, its Fourier transform) has compact support. Thus, because ω(Φ∆) does not vanish identically, we conclude that ∆1 ≤ ∆gap, as desired.

## B Convergence of the spinless bootstrap

In this appendix, we examine the convergence rate of the spinless modular bootstrap as a function of the truncation order, and in particular explain why we are conﬁdent that the numerical calculations in Sections 3 and 4 have been fully optimized.

Figure 17 shows the density bounds obtained using truncation orders N = 1, 2, 4, .. . , 512 for dimensions d ≤ 2048, in the same format as Figure 3.13 Each ﬁxed N seems to lead to the same limit as d → ∞, analogously to [36, Section 3.2], but they closely approximate the optimal linear programming bound over increasingly large ranges of d. In particular, doubling

- N more or less doubles the range of dimensions over which we obtain a close approximation. What Figure 17 indicates is that N should be chosen proportionally to d if we wish to


obtain comparably accurate results. Figure 18 makes this assertion more precise, and shows that the required truncation order is remarkably close to linear in d. We obtained the limiting values ∆LP1 (c) in Figure 18 by taking N quite large, in particular more than twice as large as needed to make the plotted values stop changing.

We do not know a formula for the slopes in Figure 18. When we need to estimate the convergence rate in high dimensions, we extrapolate from lower dimensions and then make a conservative underestimate. What makes this procedure reliable is how close to linear

13Technically, when d is small we plot only the smaller values of N, to avoid the failure of our numerical method for d = 3 and N > 32, which we noted in Section 2.4.

120

|ε = 0.001 ε = 0.01 ε = 0.1| |
|---|---|
| | |


111

100

80

63

60

N

40

20

20

0

0 32 64 96 128 160 192 224 256 central charge c

Figure 18: Minimal N such that ∆LP1 ,N(c) ≤ (1+ε)∆LP1 (c) for ε = 0.1, 0.01, and 0.001, together with the least squares regression lines.

Figure 18 is. By contrast, Figure 19 ﬁxes c and examines how many digits of ∆LP1 ,N(c) have converged as a function of N. Here, the behavior is not nearly as linear, and it is more diﬃcult to extrapolate.

The most delicate numerical estimation in this paper occurs in obtaining the number −0.6044 as the inﬁnite-dimensional limit of the LP column in Table 1. Table 4 gives evidence that the values in Table 1 are correctly extrapolated to inﬁnite truncation order. Speciﬁcally, for each dimension Table 4 lists the largest truncation order N we have computed, together with the smallest order Nk that agrees with order N to k decimal places. The numbers in black are exact, meaning that truncation order Nk − 1 is not enough. In each such case N is at least 2Nk, and often much larger than that; this margin of safety gives us conﬁdence that these values do reﬂect the limit as N → ∞. The red numbers are obtained by doubling the numbers above them, which seems to produce an overestimate and would work in every other case with d > 2. Even for the red numbers, N5 < N, and therefore we believe that our truncation orders are high enough for all the numbers in Table 1 to have stabilized.

## Acknowledgements

We are grateful to Ganesh Ajjanagadde, Matthew de Courcy-Ireland, Abhinav Kumar, Dalimil Maza´cˇ, Stephen D. Miller, Danylo Radchenko, Leonardo Rastelli, Peter Sarnak, and Maryna Viazovska for helpful conversations. The work of TH and AT is supported by the Simons Foundation (Simons Collaboration on the Nonperturbative Bootstrap). NA is supported by the Leo Kadanoﬀ Fellowship.

45

45

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |


40

40

35

35

LP,NLP−−(c)/∆(c)1)log(∆1011

30

30

25

25

20

20

15

15

10

10

5

5

0

0

0 32 64 96 128 160 192 224 256 N

Figure 19: Convergence of ∆LP1 ,N(c) as a function of N for c = 1/2, 1, 2, 4, ..., 256 (colored red through black).

Table 4: The truncation order Nk required to approximate (log2 density)/d to within 0.5 · 10−k, so that rounding to k decimal places leads to error at most 10−k.

d N N1 N2 N3 N4 N5

- 1 ∞ 1 1 2 2 2
- 2 33 1 2 3 4 5 4 308 1 2 4 5 7 8 ∞ 2 3 5 7 9


16 933 2 4 7 10 13 32 997 3 7 11 15 19 64 1025 5 11 18 25 33

128 780 8 20 33 46 59 256 844 14 37 61 86 111 512 972 25 71 118 167 215

1024 852 48 138 232 327 422 2048 1700 93 271 458 647 836 4096 1750 183 536 916 1294 1672

## References

- [1] S. Ferrara, A. Grillo and R. Gatto, Tensor representations of conformal algebra and conformally covariant operator product expansion, Annals Phys. 76, 161–188, 1973.
- [2] A. Polyakov, Non-Hamiltonian approach to conformal quantum ﬁeld theory, Zh. Eksp. Teor. Fiz. 66, 23–42, 1974. English translation in Soviet Physics JETP 39, 10–18, 1974.
- [3] G. Mack, Duality in quantum ﬁeld theory, Nucl. Phys. B 118, 445–457, 1977.
- [4] R. Rattazzi, V. S. Rychkov, E. Tonni and A. Vichi, Bounding scalar operator dimensions in 4D CFT, JHEP 12, 031, 2008, [arXiv:0807.0004 [hep-th]].
- [5] S. Rychkov, EPFL lectures on conformal ﬁeld theory in D ≥ 3 dimensions. SpringerBriefs in Physics. Springer Nature, 2017, 10.1007/978-3-319-43626-5. [arXiv:1601.05000 [hep-th]].
- [6] D. Simmons-Duﬃn, The conformal bootstrap, in New frontiers in ﬁelds and strings: proceedings of the 2015 Theoretical Advanced Study Institute in elementary particle physics, pp. 1–74. World Scientiﬁc Publishing Company, 2017. 10.1142/9789813149441 0001. arXiv:1602.07982 [hep-th].

- [7] D. Poland and D. Simmons-Duﬃn, The conformal bootstrap, Nature Phys. 12, 535–539, 2016.
- [8] H. Cohn and N. Elkies, New upper bounds on sphere packings I, Ann. of Math. (2) 157, 689–714, 2003, [arXiv:math/0110009 [math.MG]].
- [9] T. Hartman, D. Maza´cˇ and L. Rastelli, Sphere packing and quantum gravity, JHEP 12, 048, 2019, [arXiv:1905.01319 [hep-th]].
- [10] J. Bourgain, L. Clozel and J.-P. Kahane, Principe d’Heisenberg et fonctions positives, Ann. Inst. Fourier (Grenoble) 60, 1215–1232, 2010.
- [11] H. Cohn and F. Gon¸calves, An optimal uncertainty principle in twelve dimensions via modular forms, Invent. Math. 217, 799–831, 2019, [arXiv:1712.04438 [math.CA]].
- [12] N. Afkhami-Jeddi, T. Hartman and A. Tajdini, Fast conformal bootstrap and constraints on 3d gravity, JHEP 05, 087, 2019, [arXiv:1903.06272 [hep-th]].
- [13] H. Cohn and A. Kumar, Optimality and uniqueness of the Leech lattice among lattices, Ann. of Math. (2) 170, 1003–1050, 2009, [arXiv:math/0403263 [math.MG]].
- [14] H. Cohn and F. Gon¸calves, Data for “An optimal uncertainty principle in twelve dimensions via modular forms”, data set, DSpace@MIT, 2018. https://hdl.handle.net/1721.1/118165.
- [15] N. Afkhami-Jeddi, H. Cohn, T. Hartman and A. Tajdini, Free partition functions and an averaged holographic duality, 2020, [arXiv:2006.04839 [hep-th]].
- [16] K. Ball, A lower bound for the optimal density of lattice packings, Internat. Math. Res. Notices 1992, 217–221, 1992.


- [17] S. Vance, Improved sphere packing lower bounds from Hurwitz lattices, Adv. Math. 227, 2144–2156, 2011, [arXiv:1105.3779 [math.MG]].
- [18] A. Venkatesh, A note on sphere packings in high dimension, Int. Math. Res. Not. IMRN 1628–1642, 2013.
- [19] G. A. Kabatyanskii and V. I. Levenshtein, Bounds for packings on a sphere and in space, Problemy Peredachi Informatsii 14, 3–25, 1978. English translation in Problems of Information Transmission 14, 1–17, 1978.
- [20] H. Cohn and Y. Zhao, Sphere packing bounds via spherical codes, Duke Math. J. 163, 1965–2002, 2014, [arXiv:1212.5966 [math.MG]].
- [21] J. H. Conway and N. J. A. Sloane, Sphere packings, lattices and groups, vol. 290 of Grundlehren der Mathematischen Wissenschaften. Springer-Verlag, New York, third ed., 1999, 10.1007/978-1-4757-6568-7.
- [22] P. Delsarte, Bounds for unrestricted codes, by linear programming, Philips Res. Rep. 27, 272–289, 1972.
- [23] R. J. McEliece, E. R. Rodemich, H. Rumsey, Jr. and L. R. Welch, New upper bounds on the rate of a code via the Delsarte-MacWilliams inequalities, IEEE Trans. Inform. Theory IT-23, 157–166, 1977.
- [24] A. Barg and D. B. Jaﬀe, Numerical results on the asymptotic rate of binary codes, in Codes and association schemes (Piscataway, NJ, 1999), vol. 56 of DIMACS Ser. Discrete Math. Theoret. Comput. Sci., pp. 25–32. Amer. Math. Soc., Providence, RI, 2001. 10.1090/dimacs/056/02.
- [25] P. Boyvalenkov, D. Danev and M. Stoyanova, Reﬁnements of the Levenshtein bounds in q-ary Hamming spaces, Problemy Peredachi Informatsii 54, 35–50, 2018. English translation in Problems of Information Transmission 54, 329–342, 2018.
- [26] D. Maz´ˇc, Analytic bounds and emergence of AdS2 physics from the conformal bootstrap, JHEP 04, 146, 2017, [arXiv:1611.10060 [hep-th]].
- [27] T. C. Hales, A proof of the Kepler conjecture, Ann. of Math. (2) 162, 1065–1185, 2005.
- [28] T. Hales, M. Adams, G. Bauer, T. D. Dang, J. Harrison, L. T. Hoang, C. Kaliszyk, V. Magron, S. McLaughlin, T. T. Nguyen, Q. T. Nguyen, T. Nipkow, S. Obua, J. Pleso, J. Rute, A. Solovyev, T. H. A. Ta, N. T. Tran, T. D. Trieu, J. Urban, K. Vu and R. Zumkeller, A formal proof of the Kepler conjecture, Forum Math. Pi 5, e2, 1–29, 2017, [arXiv:1501.02155 [math.MG]].
- [29] M. S. Viazovska, The sphere packing problem in dimension 8, Ann. of Math. (2) 185, 991–1015, 2017, [arXiv:1603.04246 [math.NT]].
- [30] H. Cohn, A. Kumar, S. D. Miller, D. Radchenko and M. Viazovska, The sphere packing problem in dimension 24, Ann. of Math. (2) 185, 1017–1033, 2017, [arXiv:1603.06518 [math.NT]].


- [31] A. Thue, Om nogle geometrisk-taltheoretiske Theoremer, Forhandlingerne ved de Skandinaviske Naturforskeres 14, 352–353, 1892.
- [32] T. C. Hales, Cannonballs and honeycombs, Notices Amer. Math. Soc. 47, 440–449, 2000.
- [33] S. Collier, Y.-H. Lin and X. Yin, Modular bootstrap revisited, JHEP 09, 061, 2018, [arXiv:1608.06241 [hep-th]].
- [34] I. Frenkel, J. Lepowsky and A. Meurman, Vertex operator algebras and the Monster, vol. 134 of Pure and Applied Mathematics. Academic Press, Inc., Boston, MA, 1988.
- [35] S. Hellerman, A universal inequality for CFT and quantum gravity, JHEP 08, 130, 2011, [arXiv:0902.2790 [hep-th]].
- [36] D. Friedan and C. A. Keller, Constraints on 2d CFT partition functions, JHEP 10, 180, 2013, [arXiv:1307.6562 [hep-th]].
- [37] T. Gannon, Moonshine beyond the Monster: the bridge connecting algebra, modular forms and physics. Cambridge Monographs on Mathematical Physics. Cambridge University Press, Cambridge, 2006, 10.1017/CBO9780511535116.
- [38] Y.-H. Lin and S.-H. Shao, Anomalies and bounds on charged operators, Phys. Rev. D 100, 025013, 2019, [arXiv:1904.04833 [hep-th]].
- [39] C. A. Keller and H. Ooguri, Modular constraints on Calabi-Yau compactiﬁcations, Commun. Math. Phys. 324, 107–127, 2013, [arXiv:1209.4649 [hep-th]].
- [40] N. Benjamin and Y.-H. Lin, Lessons from the Ramond sector, 2020, [arXiv:2005.02394 [hep-th]].
- [41] H. Cohn and N. Triantaﬁllou, Dual linear programming bounds for sphere packing via modular forms, 2019, [arXiv:1909.04772 [math.MG]].
- [42] H. Cohn and A. Kumar, Universally optimal distribution of points on spheres, J. Amer. Math. Soc. 20, 99–148, 2007, [arXiv:math/0607446 [math.MG]].
- [43] H. Cohn and M. de Courcy-Ireland, The Gaussian core model in high dimensions, Duke Math. J. 167, 2417–2455, 2018, [arXiv:1603.09684 [math.MG]].
- [44] H. Cohn, A. Kumar, S. D. Miller, D. Radchenko and M. Viazovska, Universal optimality

of the E8 and Leech lattices and interpolation formulas, 2019, [arXiv:1902.05438 [math.MG]].

- [45] H. Cohn and Y. Zhao, Energy-minimizing error-correcting codes, IEEE Trans. Inform. Theory 60, 7442–7450, 2014, [arXiv:1212.1913 [math.CO]].
- [46] S. El-Showk and M. F. Paulos, Extremal bootstrapping: go with the ﬂow, JHEP 03, 148, 2018, [arXiv:1605.08087 [hep-th]].
- [47] D. Poland, S. Rychkov and A. Vichi, The conformal bootstrap: theory, numerical techniques, and applications, Rev. Mod. Phys. 91, 015002, 2019, [arXiv:1805.04405 [hep-th]].


- [48] V. I. Levensˇteı˘n, On bounds for packings in n-dimensional Euclidean space, Dokl. Akad. Nauk SSSR 245, 1299–1303, 1979. English translation in Soviet Math. Dokl. 20, 417–421, 1979.
- [49] V. I. Levenshtein, Designs as maximum codes in polynomial metric spaces, Acta Appl. Math. 29, 1–82, 1992.
- [50] V. I. Levenshtein, Universal bounds for codes and designs, in Handbook of coding theory, Vol. I, pp. 499–648. North-Holland, Amsterdam, 1998.
- [51] A. Scardicchio, F. H. Stillinger and S. Torquato, Estimates of the optimal density of sphere packings in high dimensions, J. Math. Phys. 49, 043301, 2008, [arXiv:0705.1482 [cond-mat.stat-mech]].
- [52] S. Torquato and F. H. Stillinger, New conjectural lower bounds on the optimal density of sphere packings, Experiment. Math. 15, 307–331, 2006, [arXiv:math/0508381 [math.MG]]. http://projecteuclid.org/euclid.em/1175789761.
- [53] G. Parisi, P. Urbani and F. Zamponi, Theory of simple glasses: exact solutions in inﬁnite dimensions. Cambridge University Press, Cambridge, 2020, 10.1017/9781108120494.
- [54] D. Maz´ˇc and M. F. Paulos, The analytic functional bootstrap. Part II. Natural bases for the crossing equation, JHEP 02, 163, 2019, [arXiv:1811.10646 [hep-th]].
- [55] L. Rolen and I. Wagner, A note on Schwartz functions and modular forms, Arch. Math. (Basel) 115, 35–51, 2020, [arXiv:1903.05737 [math.NT]].
- [56] A. S. Feigenbaum, P. J. Grabner and D. P. Hardin, Eigenfunctions of the Fourier Transform with speciﬁed zeros, 2019, [arXiv:1907.08558 [math.MG]].
- [57] H. Cohn and S. D. Miller, Some properties of optimal functions for sphere packing in dimensions 8 and 24, 2016, [arXiv:1603.04759 [math.MG]].
- [58] W. Gawronski, On the asymptotic distribution of the zeros of Hermite, Laguerre, and Jonqui`ere polynomials, J. Approx. Theory 50, 214–231, 1987.
- [59] L. Gatteschi, Asymptotics and bounds for the zeros of Laguerre polynomials: a survey, J. Comput. Appl. Math. 144, 7–27, 2002.
- [60] D. V. Widder, The Laplace transform, vol. 6 of Princeton Mathematical Series. Princeton University Press, Princeton, NJ, 1941.
- [61] J. L. Cardy, Operator content of two-dimensional conformally invariant theories, Nucl. Phys. B 270, 186–204, 1986.
- [62] J. Qiao and S. Rychkov, A tauberian theorem for the conformal bootstrap, JHEP 12, 119, 2017, [arXiv:1709.00008 [hep-th]].
- [63] B. Mukhametzhanov and A. Zhiboedov, Modular invariance, tauberian theorems and microcanonical entropy, JHEP 10, 261, 2019, [arXiv:1904.06359 [hep-th]].
- [64] S. Ganguly and S. Pal, Bounds on the density of states and the spectral gap in CFT2, Phys. Rev. D 101, 106022, 2020, [arXiv:1905.12636 [hep-th]].


- [65] S. Pal and Z. Sun, Tauberian-Cardy formula with spin, JHEP 01, 135, 2020, [arXiv:1910.07727 [hep-th]].
- [66] B. Mukhametzhanov and S. Pal, Beurling-Selberg extremization and modular bootstrap at high energies, SciPost Phys. 8, 088, 2020, [arXiv:2003.14316 [hep-th]].
- [67] S. Pal and Z. Sun, High energy modular bootstrap, global symmetries and defects, JHEP 08, 064, 2020, [arXiv:2004.12557 [hep-th]].
- [68] B. Simon, Szeg˝o’s theorem and its descendants: spectral theory for L2 perturbations of orthogonal polynomials. M. B. Porter Lectures. Princeton University Press, Princeton, NJ, 2011.
- [69] D. de Laat, F. M. de Oliveira Filho and F. Vallentin, Upper bounds for packings of spheres of several radii, Forum Math. Sigma 2, e23, 1–42, 2014, [arXiv:1206.2608 [math.MG]].
- [70] O. R. Musin, The kissing number in four dimensions, Ann. of Math. (2) 168, 1–32, 2008, [arXiv:math/0309430 [math.MG]].
- [71] F. C. Machado and F. M. de Oliveira Filho, Improving the semideﬁnite programming bound for the kissing number by exploiting polynomial symmetry, Exp. Math. 27, 362–369, 2018, [arXiv:1609.05167 [math.OC]].
- [72] K. Kallal, T. Kan and E. Wang, Improved lower bounds for kissing numbers in dimensions 25 through 31, SIAM J. Discrete Math. 31, 1895–1908, 2017, [arXiv:1608.07270 [math.MG]].
- [73] A. D. Wyner, Capabilities of bounded discrepancy decoding, Bell System Tech. J. 44, 1061–1122, 1965.
- [74] P. Delsarte, J. M. Goethals and J. J. Seidel, Spherical codes and designs, Geometriae Dedicata 6, 363–388, 1977.
- [75] S. Hellerman and C. Schmidt-Colinet, Bounds for state degeneracies in 2D conformal ﬁeld theory, JHEP 08, 127, 2011, [arXiv:1007.0756 [hep-th]].
- [76] S. El-Showk, M. F. Paulos, D. Poland, S. Rychkov, D. Simmons-Duﬃn and A. Vichi, Solving the 3d Ising model with the conformal bootstrap II. c-minimization and precise critical exponents, J. Stat. Phys. 157, 869, 2014, [arXiv:1403.4545 [hep-th]].
- [77] G. E. Andrews, R. Askey and R. Roy, Special functions, vol. 71 of Encyclopedia of Mathematics and its Applications. Cambridge University Press, Cambridge, 1999, 10.1017/CBO9781107325937.
- [78] I. J. Schoenberg, Positive deﬁnite functions on spheres, Duke Math. J. 9, 96–108, 1942.
- [79] D. V. Shtrom, The Delsarte method in the problem of the contact numbers of Euclidean spaces of high dimensions, Proc. Steklov Inst. Math. Suppl. 2, S162–S189, 2002.
- [80] C. Bachoc and F. Vallentin, New upper bounds for kissing numbers from semideﬁnite programming, J. Amer. Math. Soc. 21, 909–924, 2008, [arXiv:math/0608426 [math.MG]].


- [81] M. F. Bourque and B. Petri, Kissing numbers of closed hyperbolic manifolds, 2019, [arXiv:1905.11083 [math.GT]].
- [82] D. Radchenko and M. Viazovska, Fourier interpolation on the real line, Publ. Math. Inst. Hautes Etudes´ Sci. 129, 51–81, 2019, [arXiv:1701.00265 [math.NT]].


