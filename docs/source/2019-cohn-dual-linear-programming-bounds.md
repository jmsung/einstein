---
type: source
kind: paper
title: Dual linear programming bounds for sphere packing via modular forms
authors: Henry Cohn, Nicholas Triantafillou
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1909.04772v2
source_local: ../raw/2019-cohn-dual-linear-programming-bounds.pdf
topic: general-knowledge
cites:
---

# arXiv:1909.04772v2[math.MG]19Apr2021

## DUAL LINEAR PROGRAMMING BOUNDS FOR SPHERE PACKING VIA MODULAR FORMS

HENRY COHN AND NICHOLAS TRIANTAFILLOU

Abstract. We obtain new restrictions on the linear programming bound for sphere packing, by optimizing over spaces of modular forms to produce feasible points in the dual linear program. In contrast to the situation in dimensions 8 and 24, where the linear programming bound is sharp, we show that it comes nowhere near the best packing densities known in dimensions 12, 16, 20, 28, and 32. More generally, we provide a systematic technique for proving separations of this sort.

1. Introduction

The sphere packing problem asks for the densest packing of congruent spheres in Rd. In other words, what is the greatest proportion of Rd that can be covered by congruent balls with disjoint interiors? The case d = 1 is trivial, d = 2 was solved by Thue [32], and d = 3 was solved by Hales [19] with a computer-assisted proof that has since been formally veriﬁed [20]. These proofs make essential use of the geometry of packings in Rd in a way that seems diﬃcult to extend to higher dimensions, and so another approach is needed when d is large. Based on a long history of linear programming bounds in coding theory, Cohn and Elkies [7] developed a linear programming bound for sphere packing. It yields the best upper bounds known for the packing density in high dimensions [14], and Cohn and Elkies conjectured that the linear programming bound is sharp when d = 8 or d = 24.

In a recent breakthrough, Viazovska [34] proved this conjecture for d = 8, and thus showed that the E8 root lattice yields the densest sphere packing in R8. Shortly thereafter, Cohn, Kumar, Miller, Radchenko, and Viazovska [11] proved the conjecture for d = 24. These are the only two cases beyond d = 3 in which the sphere packing problem has been solved.

These advances raise numerous questions. Is it possible that the linear programming bound is sharp in some other dimensions? Could it even be sharp in every dimension? (Surely not, but why not?) What happens in R16, and why does that case seemingly not behave like R8 and R24? These questions remain mysterious, but in this paper we take some initial steps towards answering them.

The diﬃculty in analyzing the linear programming bound stems from the use of an auxiliary function, which must satisfy certain inequalities. The quality of the bound depends on the choice of this function, and optimizing the bound amounts to optimizing a functional over the inﬁnite-dimensional space of auxiliary functions. This optimization problem has not been solved exactly except when d ∈ {1,8,24}.

Triantaﬁllou was partially supported by an internship at Microsoft Research New England, a National Science Foundation Graduate Research Fellowship under grant #1122374, and Simons Foundation grant #550033.

1

Spherepackingdensity

100

10−1

10−2

10−3

Linear programming bound Densest known packing Dual (lower) bound

10−4

10−5

4 8 12 16 20 24 28 32

Dimension

Figure 1.1. The upper curve is the linear programming bound computed using the best auxiliary functions currently known, while the white circles are the densest sphere packings currently known (see [15, pp. xix–xx]). Our new obstructions, drawn as black circles, are lower bounds for the linear programming bound. They show that further optimizing the choice of auxiliary function cannot improve the linear programming bound by much.

In other dimensions, we can approximate the true optimum by using a computer to optimize over a ﬁnite-dimensional subspace. The resulting auxiliary function always proves some bound for the sphere packing density, and we expect it to be close to the optimal linear programming bound if the subspace is large and generic enough. However, nobody has been able to determine how close it must be. What if these numerical computations are woefully far from the true optimum? If that were the case, then they would shed very little light on the linear programming bound. It is even possible, albeit implausible, that the linear programming bound might be sharp for relatively small values of d that nobody has noticed yet.

As shown in Figure 1.1, the linear programming bound seems to vary smoothly as a function of dimension, and the sharp bounds in 8 and 24 dimensions ﬁt perfectly with the curve as a whole. These observations raise our conﬁdence that the numerical optimization is not in fact misleading. However, there remains a fundamental gap in the theory of the linear programming bound: how can one prove a corresponding lower bound, beyond which no auxiliary function can pass? In optimization terms, such a bound amounts to a dual linear programming bound, which controls how good the optimal linear programming bound could be.

In this paper, we show how to compute such a bound when the dimension is a multiple of four, by optimizing over spaces of modular forms. (We expect that other dimensions work similarly, but we have not carried out the modular form calculations in those cases.) Our results for dimensions 12, 16, 20, 28, and 32 are

shown in Figure 1.1 and Table 6.1. The most noteworthy cases are dimensions 12 and 16, where the Coxeter-Todd and Barnes-Wall lattices are widely conjectured to be optimal sphere packings:

- Theorem 1.1. The linear programming bound for the sphere packing density in R16 is greater than 1.7 times the density of the Barnes-Wall lattice, and the bound in R12 is greater than 1.686 times the density of the Coxeter-Todd lattice. In particular, the linear programming bound cannot prove that either lattice is an optimal sphere packing.


Unsurprisingly, in neither case is the linear programming bound even close to reaching the best density known. The ratios 1.7 and 1.686 are almost certainly not quite optimal, and we expect that they could be improved to 1.712 and 1.694, respectively, which would match the known upper bounds to three decimal places. See Section 7 for further discussion.

Note that even when the linear programming bound is far from sharp, determining its value is of interest in its own right. For example, it can be interpreted as describing an uncertainty principle for the signs of a function and its Fourier transform (see [8]). Thus, it has signiﬁcance beyond just the topic of sphere packing.

1.1. The linear programming bound. Before proceeding further, let us review how the linear programming bound works. Recall that a sphere packing in Rd is a disjoint union x∈C B(x,ρ) of open unit balls of some ﬁxed radius ρ and centered at the points of some subset C of Rd.

Given a sphere packing P, the upper density ∆P of P is deﬁned by

vol(B(x,r) ∩ P) vol(B(x,r))

∆P = limsup

r→∞

for any x ∈ Rd (the upper density does not depend on the choice of x). If the limit exists, and not just the limit superior, then we say that P has density ∆P. The sphere packing density in Rd is

∆d = sup

∆P,

P⊂Rd

where the supremum is over sphere packings P. We will often renormalize and work with the upper center density

#(B(x,r) ∩ C) vol(B(x,r)) ·

vol(B(0,ρ)) vol(B(0,1))

∆P vol(B(0,1))

δP =

= limsup

,

r→∞

which measures the number of center points per unit volume in space if we use spheres of radius ρ = 1. Of course the center density has no theoretical advantage over the density, but it is often convenient not have to carry around the factor of vol(B(0,1)) = πd/2/(d/2)!. For example, δ24 = 1, while ∆24 = π12/12! = 0.00192957....

We normalize the Fourier transform f of an integrable function f : Rd → R by

f(y) =

f(x)e−2πi x,y dx,

Rd

- f(x)

−2 −1 0 1 2 y

- 0
- 1


- f(y)


- 0
- 1


−2 −1 0 1 2 x

Figure 1.2. A sample auxiliary function and its Fourier transform (namely, f(x) = (1 − x2)e−x

2

on R1, with r = 1).

where  ·,·  denotes the usual inner product on Rd. Cohn and Elkies [7] showed1 how to use harmonic analysis to bound the sphere packing density as follows:

- Theorem 1.2 (Cohn and Elkies [7]). Let f : Rd → R be a continuous, integrable function, such that f is integrable as well and f is real-valued (i.e., f is even). Suppose f and f satisfy the following inequalities for some positive real number r:


- (1) f(0) > 0 and f(0) > 0,
- (2) f(x) ≤ 0 for |x| ≥ r, and
- (3) f(y) ≥ 0 for all y.


Then every sphere packing in Rd has upper center density at most

d

f(0) f(0)

r 2

·

.

The linear programming bound in Rd is the inﬁmum of the center density upper bound

d

f(0) f(0)

r 2

·

over all auxiliary functions f satisfying the hypotheses of Theorem 1.2. See Figure 1.2 for an example of an auxiliary function, which is far from optimal.

Without loss of generality, we can assume that the auxiliary function f is radial, because we can simply average its rotations about the origin. For a radial function f, we write f(t) with t ∈ [0,∞) to denote the common value f(x) with |x| = t. If f is radial, then f is radial as well, and

∞

2π |y|d/2−1

f(t)Jd/2−1(2πt|y|)td/2 dt,

f(y) =

0

where Jd/2−1 is the Bessel function of the ﬁrst kind of order d/2−1 (see, for example, Theorem 9.10.3 in [2]).

1Strictly speaking, the paper [7] imposed stronger hypotheses on f, but one can easily remove those hypotheses by mollifying f, using the approach from the ﬁrst paragraph of Section 4 in [6]. The fact that they could be removed was ﬁrst observed in [9].

The density bound

f(0) f(0)

·

r 2

d

is invariant under replacing f with x  → f(ρx) and r with r/ρ for any scaling factor ρ ∈ (0,∞). Without loss of generality we can use this invariance to ﬁx

- r = 1, and we can assume f(0) = 1 as well. Then the constraints on f from Theorem 1.2 are linear inequalities, and the density bound is also a linear functional of f. Thus, optimizing the choice of f amounts to solving an inﬁnite-dimensional linear optimization problem, which explains the name “linear programming bound.” In practice, however, ﬁxing r may not lead to the prettiest answers. For example, Cohn and Elkies found more elegant behavior if one instead ﬁxes f(0) = f(0) and lets r vary (see Section 7 of [7]).


The best choice of f is not known, except when d ∈ {1,8,24}, and little is known about how good the optimal bound might be. It is not hard to produce upper bounds by numerically optimizing over ﬁnite-dimensional spaces of functions, and in most cases these upper bounds seem to be close to the optimal linear programming bound (see [1] for the most extensive calculations so far). However, these computational methods leave open the possibility that other auxiliary functions might prove much better bounds.

What sort of obstructions prevent the linear programming bound from reaching the density of the best sphere packing? In this paper we provide a partial answer, with an algorithm to compute such obstructions via linear programming over spaces of modular forms of weight d/2. The algorithm is based on optimizing a summation formula for radial Schwartz functions, which is an analogue of Voronoi summation.

The remainder of the paper is organized as follows. In Section 2, we present a general framework for computing dual linear programming bounds. We describe our algorithm in Section 3, and we prove the summation formula underlying the algorithm in Section 4. In Section 5, we expand on the ﬁnal step of our algorithm by describing a method for checking in ﬁnite time that all of the coeﬃcients of the q-expansion of a given modular form are nonnegative. Finally, we present a table of new lower bounds in Section 6, and we conclude with open problems in Section 7.

2. Duality

Computing a bound for the objective function in a linear program is typically straightforward: it just amounts to ﬁnding a feasible point in the dual linear program. The diﬃculty in our case is that the optimization problems are inﬁnitedimensional. The primal problem is relatively tractable, because the auxiliary functions in Theorem 1.2 are well behaved in practice. We can approximate them with polynomials times Gaussians, and using high-degree polynomials yields excellent results. For example, in R16 the resulting center density bounds seem to converge to

0.10705844234092448845891681517141...

as the polynomial degree tends to inﬁnity, and we believe this number is the optimal linear programming bound for 16 dimensions, correct to 32 decimal places. Unfortunately, the dual problem is much less tractable. It amounts to optimizing over a space of measures, and we believe the optimal measures will be singular (speciﬁcally, supported on a discrete set of radii). In particular, we know of no

simple family of measures we can use to approximate them fruitfully. Instead, the dual problem appears to be quite a bit more subtle.

In Section 4 of [6], Cohn formulated the dual linear program as follows. Here, δ0 denotes a delta function at the origin, and µ is the Fourier transform of µ as a tempered distribution.

- Proposition 2.1. Let µ be a tempered distribution on Rd such that µ = δ0 +ν with ν ≥ 0, supp(ν) ⊆ {x ∈ Rd : |x| ≥ r} for some r > 0, and µ ≥ cδ0 for some c > 0. Then the linear programming bound in Rd is at least


c ·

r 2

d

.

Sketch of proof. Let f : Rd → R be an auxiliary function satisfying the hypotheses of Theorem 1.2, where we use scaling invariance to ensure that the same value of r works for both f and µ. If f and f are rapidly decreasing, then the inequalities on

- f and µ imply that


f µ ≥ c f(0), and thus

f(0) ≥

fµ =

Rd

Rd

f(0) f(0)

≥ c,

as desired. More general auxiliary functions must be molliﬁed, as described in Section 4 of [6], after which the same argument applies to them as well.

The diﬃculty in applying this proposition is how to ﬁnd a plentiful source of distributions µ that could satisfy the hypotheses. One source is Poisson summation for lattices, which says that for any lattice Λ in Rd, the Fourier transform of the distribution

δx

x∈Λ

is

1 vol(Rd/Λ) y∈Λ

δy,

∗

where Λ∗ is the dual lattice. Thus, the hypotheses of Proposition 2.1 are satisﬁed with c = 1/vol(Rd/Λ) and r = minx∈Λ\{0} |x|. The resulting lower bound amounts to proving Theorem 1.2 for lattice packings.

In principle, one could try to improve on individual lattices by using a linear combination of Poisson summation formulas for diﬀerent lattices (see, for example, the bottom of page 351 in [6]). However, that does not seem fruitful in general. Instead, we use the following analogue of Voronoi summation to produce distributions from modular forms. For deﬁnitions related to modular forms, see [18]. In particular,

a b c d ∈ GL2(R) and

recall that the slash operator is deﬁned as follows: if M =

detM > 0, then

(f|kM)(z) := (ad − bc)k/2(cz + d)−kf

az + b cz + d

.

- Proposition 2.2. Let d = 2k with k ∈ N, let g ∈ Mk(Γ1(N)) be a modular form


0 −1 N 0

of weight k for the congruence subgroup Γ1(N), let wN =

, and let

ik Nk/2zk

1 Nz

g(z) = ik(g|kwN)(z) =

g −

be ik times the image of g under the full level N Atkin-Lehner operator (so that

- g = ik g|kwN as well). Let the q-expansions of g and g be


∞

∞

anqn and g(z) =

bnqn,

g(z) =

n=0

n=0

where q = e2πiz. Then for every radial Schwartz function f : Rd → C,

2√n √

d/2 ∞

∞

anf(√n) =

2 √

bn f

.

N

N

n=0

n=0

In particular, if δr denotes a delta function supported on the sphere of radius r about the origin in Rd, then this proposition says that the tempered distributions

d/2 ∞

∞

2 √

bnδ2√

anδ√n and

n/N

N

n=0

n=0

are Fourier transforms of each other. Our algorithm will optimize over distributions of this form. The advantage of these distributions is that their supports help enforce the constraint that supp(ν) ⊆ {x ∈ Rd : |x| ≥ r} in Proposition 2.1.

For comparison, the techniques in Section 5 of [8] produce what appear to be close numerical approximations to the optimal distributions µ. They have the form

µ =

cnδr

n

n≥0

with radii given by 0 = r0 < r1 < r2 < ··· and tending to inﬁnity, coeﬃcients cn > 0, and µ = µ. For example, in R16 the ﬁrst few radii and coeﬃcients are listed in Table 2.1. The only drawback is that the results of these calculations are merely conjectural: we do not know whether such a distribution actually exists.

Our approach in this paper amounts to approximating the optimal µ with a distribution µ whose existence follows from Proposition 2.2. For comparison, Table 2.1 shows the best µ we have obtained, which we computed using the parameters N = 96 and T = 20 in the notation of the next section. This distribution is of the form µ = n≥0 c nδr

. In the table, we have rescaled the distribution µ so that c 0 = c 0 = 1. Note that

### , with Fourier transform µ = n≥0 c nδr

n

n

- r1 ≈ r 1 ≈ r 1 ≈ r 2,
- r2 ≈ r 2 ≈ r 3 ≈ r 3 ≈ r 4, and
- r3 ≈ r 4 ≈ r 5 ≈ r 5 ≈ r 6,


and the sums of the corresponding coeﬃcients are also near each other. The approximation to µ is not yet very close, but one can already see µ roughly emerging from µ .

It is natural to ask why Γ1(N) appears in Proposition 2.2, rather than the group Γ0(N) that is more often used in the theory of modular forms. This is simply a matter of generality: Γ1(N) is a subgroup of Γ0(N), and thus Mk(Γ1(N)) contains

Table 2.1. Radii and coeﬃcients for dual distributions in R16.

n rn cn

- 0 0 1

- 1 1.7393272583625204... 8431.71627140...

- 2 2.2346642069957498... 292026.09352080...

- 3 2.6462005756471079... 3111809.14450639... n r n c n


- 0 0 1

- 1 1.7385384653461733... 8360.61230142...

- 2 2.1990965401230488... 4240.44226222...
- 3 2.2331930934327142... 282582.90774253...

- 4 2.6366241274825130... 2419678.28385080...

- 5 2.6651290005171109... 584982.54962505... n r n c n


- 0 0 1

- 1 1.6604472109700065... 133.02471778...

- 2 1.7414917267847931... 8321.61159562...

- 3 2.2277237020673214... 245869.54859549...
- 4 2.2887685306282807... 50042.27252495...

- 5 2.6253975605696717... 1578408.61282183...

- 6 2.6773906784567302... 1610965.69273527...


Mk(Γ0(N)) and is generally larger. For comparison, Γ(N) is an even smaller group, but it is not closed under conjugation by wN, which means the map g  → g used in Proposition 2.2 does not preserve Mk(Γ(N)).

3. An algorithm for dual linear programming bounds

Instead of using modular forms for the congruence subgroup Γ1(N), for simplicity we will restrict our attention to those for the larger group Γ0(N) (equivalently, to modular forms for Γ1(N) that have trivial Nebentypus). This restriction entails some loss of generality: for example, Γ0(N) does not have modular forms of odd weight, while Γ1(N) often does. However, Γ0(N) serves as an attractive proving ground for the general theory, and it should suﬃce when the dimension d is a multiple of 4.

Speciﬁcally, let k = d/2 be an even integer, and let Mk(Γ0(N)) be the space of modular forms of weight k for Γ0(N). Recall that this space has a basis consisting of modular forms with rational coeﬃcients in their q-expansions (see, for example, Corollary 12.3.12 in [17]). Furthermore, the Atkin-Lehner involution on Mk(Γ0(N)) preserves the property of having rational coeﬃcients (see Lemma 3.5.3 in [27]).

In practice, to simplify Section 5 we also assume that N is not divisible by 162, 92, or p2 for any prime p > 3, but this assumption is not essential.

We would like to ﬁnd a modular form g = n≥0 anqn in Mk(Γ0(N)) with the following properties for some T, where we set g = ikg|kwN = n≥0 bnqn:

- (1) a0 = 1 and b0 > 0,
- (2) an ≥ 0 and bn ≥ 0 for all n ≥ 0, and


- (3) an = 0 for 1 ≤ n < T.


Then we use the distribution

anδ√n

µ =

n≥0

√

√

N)d/2b0 and r =

in Proposition 2.1. By Proposition 2.2, we have c = (2/

T in the notation of Proposition 2.1. Thus, we obtain a lower bound of

d/2 √

d

2 √

T 2

b0

N

for the linear programming bound in Rd, and we wish to choose g so as to maximize this bound. We will do so by linear programming, with one caveat: all our calculations will consider only the terms up to qM in the q-series for some ﬁxed M, and at the end we must check that the inequalities are not violated beyond that point.

Let g1,...,gdimM

k(Γ0(N)) be a basis of Mk(Γ0(N)) with rational q-series coeﬃ-

cients, and let gj = ikgj|kwN be ik times the image of gj under the full level N Atkin-Lehner involution. We write the q-expansions of the modular forms gj and gj as

∞

∞

gj =

ajnqn and gj =

bjnqn,

n=0

n=0

and we ﬁx integers T and M with 1 ≤ T < dimMk(Γ0(N)) < M. These bases and q-series can all be computed algorithmically (see, for example, [31]).

Now we write g = j xjgj with respect to our basis, and we optimize over the choice of coeﬃcients xj by solving the following linear program:

maximize j xjbj0 subject to 1 = j xjaj0,

0 = j xjajn for 1 ≤ n < T, 0 ≤ j xjajn for T ≤ n ≤ M, and 0 ≤ j xjbjn for 1 ≤ n ≤ M.

These inequalities encode all the desired properties of f and g, except that we examine only the terms up to qM in the q-series.

We hope that if M is large enough, then all the terms beyond qM will have nonnegative coeﬃcients automatically, and we attempt to use asymptotic bounds to conﬁrm that all of the coeﬃcients of g and g are nonnegative (see Section 5). If this veriﬁcation fails, we can increase M and attempt the optimization problem again. In practice, M = 2 · dimMk(Γ0(N)) typically seems to be suﬃcient for the algorithm to succeed, and it works for all the numerical results we report in this paper.

To ﬁnd the best possible bounds, we run the method for several values of N and T. Larger values of N typically yield better results, but not always. It seems diﬃcult to predict the best values for T in general, although they also tend to increase as N increases. See Section 6 for the results of this method applied to the spaces Mk(Γ0(N)) of modular forms of weight k ∈ {6,8,10,14,16} and level N = 24 or 96.

For a concrete illustration of the method, consider the case d = 16 and N = 4. One can show that the space M8(Γ0(4)) is ﬁve-dimensional, with the following basis.

Let

∞

σ7(n)qn

E8(z) = 1 + 480

n=1

be the Eisenstein series of weight 8 for SL2(Z) (not to be confused with the E8 root lattice), and let f be the newform of weight 8 for Γ0(2) deﬁned by

∞

(1 − qn)8(1 − q2n)8.

f(z) = q

n=1

Then Mg(Γ0(4)) has the basis g1,...,g5, where g1(z) = E8(z), g2(z) = 16E8(2z), g3(z) = 256E8(4z), g4(z) = f(z), and g5(z) = 16f(2z). The Atkin-Lehner involution acts by g1 = g3, g2 = g2, g3 = g1, g4 = g5, and g5 = g4. Using this information, we can write down the linear program explicitly and solve it. As usual, the trickiest part is identifying the right choice of T, while we can simply take M large enough (e.g., M = 10 is more than suﬃcient).

For T = 2, solving the linear program yields the modular form

1 17

1 17

480 17

xjgj =

g1 +

g2 −

g4

j

= 1 + 4320q2 + 61440q3 + 522720q4 + ··· , which is the theta series of the Barnes-Wall lattice. Similarly, for T = 4 we obtain

1 272

1 272

30 17

xjgj =

g2 +

g3 −

g5

j

= 1 + 4320q4 + 61440q6 + 522720q8 + ··· ,

which is the same modular form with q replaced by q2 and which yields the same bound. For these two values of T, the space M8(Γ0(4)) is incapable of separating the linear programming bound from the center density 0.0625 of the Barnes-Wall lattice. However, for T = 3 we obtain

1 136

121 2176

1 136

60 17

60 17

xjgj =

g1 −

g2 +

g3 −

g4 −

g5

j

= 1 + 7680q3 + 4320q4 + 276480q5 + ··· ,

which yields an improved center density lower bound of 38/216 = 0.100112..., more than 60% greater than the center density of the Barnes-Wall lattice. In fact, this modular form has been studied before: it is the extremal theta series in 16 dimensions (see equation (47) in [15, p. 190]).

It is tempting to conjecture that the extremal theta series should exactly match the optimal linear programming bound. This conjecture would be a beautiful analogue of the behavior in 8 and 24 dimensions. In those cases the optimal lattices have determinant 1 and minimal norm 2 or 4, respectively. The extremal theta series in 16 dimensions behaves like the theta series of a lattice of determinant 1 and minimal norm 3, exactly interpolating between 8 and 24 dimensions. No such lattice exists [25], but the linear programming bound could match the density of a hypothetical lattice.

That is a good approximation in this case, but the answer turns out to be more subtle: in Section 6, we obtain a better lower bound using N = 96. Instead of

minimal norm 3, the improved lower bound is 3.022. For comparison, we believe the true linear programming bound amounts to a minimal norm of

3.02525931168288206328208655790196..., but we are unable to conjecture an exact formula for this number.

4. Poisson summation analogues from modular forms

The main result of this section is Proposition 2.2, which yields a summation formula from a modular form. Summation formulas of this sort are well known to number theorists, and essentially equivalent to the functional equation for the L-function. We record the details here and sketch a proof for the convenience of the reader. (One can also prove such a formula using the density of complex Gaussians among radial Schwartz functions, along the lines of Section 6 in [28] or Section 2.3 in [12].)

Proposition 2.2 is essentially a version of Voronoi summation. Our proof will follow the approach used in standard proofs of Voronoi summation (for example, as in Section 10.2.5 of [5] or Section 2 of [24]). The key idea comes from the classical observation that the usual Poisson summation formula is a consequence of the functional equation of the Riemann zeta function. Similarly, Proposition 2.2 follows from the functional equation relating the L-functions associated to a modular form and its Atkin-Lehner dual.

In what follows, we use the notation established in Proposition 2.2. To state the functional equation, we ﬁrst deﬁne the L-function

∞

an ns

L(s,g) =

n=1

when Re(s) > k, and the completed L-function Λ(s,g) = Ns/2(2π)−sΓ(s)L(s,g).

The functional equation relating Λ(s,g) and Λ(s, g) is classical, dating back to Hecke [21]. It says that the L-functions can be analytically continued so that

a0 s

b0 k − s

Λ(s,g) +

+

is entire and bounded in every vertical strip, and we have the functional equation Λ(s,g) = Λ(k − s, g), or equivalently

Γ(s/2) Γ(k − s/2)

s 2

s 2

,g = N(s−k)/2(2π)k−s

- (4.1) L k −


L

,g˜ .

See, for example, Theorem 1 in [26, p. I-5]. Sketch of proof of Proposition 2.2. For a radial Schwartz function f on Rd, let

anf(√n).

S =

n≥1

By Mellin inversion,

anf(√n) =

- 1

- 2πi Re(s)=σ


an ns/2Mf(s)ds

for any σ > 0, where the Mellin transform Mf is deﬁned by Mf(s) =

∞

dx x

f(x)xs

. In particular, for σ = d + ε with ε > 0,

0

∞

- 1

- 2πi


an ns/2Mf(s)ds

S =

n=1 Re(s)=d+ε

- 1

- 2πi Re(s)=d+ε


s 2

,g Mf(s)ds,

=

L

where switching the sum and integral is permitted because of the uniform convergence of the sum deﬁning the L-function.

The integrand L(s/2,g)Mf(s) is negligible when s has large imaginary part. To see why, note that by a stationary phase argument the Mellin transform Mf(s) is rapidly decaying as Im(s) grows, while L(s/2,g) grows at most polynomially in Im(s) by the Phragm´en-Lindel¨of principle. Thus, we can shift the contour of integration to the left, as long as we account for poles.

It is not hard to check that Mf(s) has a possible pole at s = 0 with residue f(0), L(s/2,g) has a possible pole at s = d with residue

d/2 1 Γ(d/2)

2π √

b0, and L(0,g) = −a0, since the pole of Γ(s) at s = 0 cancels the pole of Λ(s,g) at

2

N

- s = 0. Thus,


d/2 1 Γ(d/2)Mf(d) +

- 1

- 2πi Re(s)=−ε


s 2

2π √

- S = −a0f(0) + 2b0


,g Mf(s)ds. Setting

L

N

- 1

- 2πi Re(s)=−ε


s 2

,g Mf(s)ds

T =

L

d/2

and applying the identity f(0) = 2π

Γ(d/2)Mf(d), we see that

d/2

2 √

- (4.2) a0f(0) + S =


b0 f(0) + T. Changing variables from s to d − s and applying the functional equation (4.1) yields T =

N

d − s 2

- 1

- 2πi Re(s)=d+ε


,g Mf(d − s)ds

L

- 1

- 2πi Re(s)=d+ε


Γ(s/2) Γ((d − s)/2)

s 2

Ns/2−d/4(2π)d/2−s

, g Mf(d − s)ds. Now we use the identity

=

L

πd/2−sΓ(s/2) Γ((d − s)/2) Mf(d − s)

M f(s) =

(see Theorem 5.9 in [23]). Making this substitution, we ﬁnd that

T =

2 √

N

d/2 1 2πi Re(s)=d+ε

4 N

−s/2

L

s 2

, g M f(s)ds.

Replacing the L-function with its deﬁning sum, switching the sum and integral as above, and applying Mellin inversion again (reversing the steps from the start of the proof), we see that

T =

=

=

2 √

N

2 √

N

2 √

N

∞

d/2 1 2πi Re(s)=d+ε

bn (4n/N)s/2M f(s)ds

n=1

d/2 ∞

bn (4n/N)s/2M f(s)ds

- 1

- 2πi Re(s)=d+ε


n=1

2√n √

d/2 ∞

.

bn f

N

n=1

Hence, (4.2) implies that

as desired.

∞

anf(√n) =

n=0

2 √

N

d/2 ∞

bn f

n=0

2√n √

N

,

5. Checking positivity of modular form coefficients

In this section, we explain how we check whether a modular form of weight k for Γ0(N) has nonnegative coeﬃcients in its q-series. This method uses only standard techniques from the theory of modular forms, but we describe them here for the beneﬁt of readers in discrete geometry. The key idea is that Eisenstein series typically make the dominant contribution asymptotically, which reduces the problem to a ﬁnite calculation if the Eisenstein contribution is positive.

As mentioned above, we assume for simplicity that N is not divisible by 162, 92, or p2 for any prime p > 3. This assumption guarantees that all the characters in this section are real. Furthermore, we assume that k ≥ 3, because the Eisenstein series for weight 2 must be obtained using diﬀerent formulas (the formulas that work for k ≥ 3 no longer converge when k = 2).

To verify that g = ∞n=0 anqn has an ≥ 0 for all n, we write g as ge + gc, where

ge = ∞n=0 enqn is a linear combination of Eisenstein series and gc = ∞n=0 cnqn is cuspidal, and we attempt to carry out the following steps:

- (1) Use Weil bounds to show that |cn| ≤ Cgnk/2 for some explicit constant Cg.
- (2) Use explicit formulas for Eisenstein series to show that en ≥ rgnk−1 for some explicit constant rg > 0.
- (3) Compare the Eisenstein part and the cuspidal part to produce a bound Q such that an > 0 for n > Q.
- (4) Explicitly compute the coeﬃcients an of g to check that an ≥ 0 for n ≤ Q.


The ﬁrst step is straightforward, given some powerful machinery. Deligne’s proof of the Weil conjectures [16] implies that, independent of weight, if h = ∞n=1 cnqn is a cuspidal Hecke eigenform normalized so that cn = 1 for the minimal n with cn = 0, then |cn| ≤ σ0(n)n(k−1)/2 ≤ nk/2. Let Bk(N) be the set of such eigenforms, which are a basis for the cuspidal part of Mk(Γ0(N)). (Note that the elements of Bk(N) typically do not have rational coeﬃcients. Instead, we must work over a

larger number ﬁeld.) If

∞

cnqn =

gc =

xhh

n=1

h∈Bk(N)

with coeﬃcients xh ∈ C, then

|cn| ≤ nk/2

|xh|.

h∈Bk(N)

k(N) |xh|. For the second step, we need to write down the Eisenstein series explicitly. We can describe them in terms of primitive Dirichlet characters φ of conductor u and natural numbers t such that u2t | N (where a | b means a divides b). Thanks to our divisibility hypotheses on N, it follows that u | 24, and therefore φ must be a real character; in other words, it takes on only the values ±1. Then the Eisenstein series in Mk(Γ0(N)) all have the form

Thus, step (1) holds with Cg = h∈B

Etφ =

δ(φ) 2

L(1 − k,φ) +

φ(n/t)σk−1(n/t)qn,

n≥1, t|n

where σ (m) = d|m d , L(s,φ) is the L-function of φ, and

δ(φ) =

1 if φ is the trivial character of conductor 1, and 0 otherwise.

See, for example, Theorem 4.5.2 in [18].

Since the Eisenstein series span the Eisenstein part of Mk(Γ0(N)), there exist constants ytφ such that

ytφEtφ

ge =

t,φ

ytφφ(n/t)σk−1(n/t)

### = e0 +

t,φ n≥1, t|n

 σk−1(n/t).

 

∞

ytφφ(n/t)

= e0 +

n=1 t|N, t|n

φ

It is straightforward to check that whenever t | n,

σk−1(n) tk−1 .

σk−1(n) σk−1(t) ≤ σk−1(n/t) ≤

This implies that if we set

rg(t,n) =

and

rg(n) =

if φ ytφφ(n/t) < 0, and 1

1 tk−1

σk−1(t) if φ ytφφ(n/t) ≥ 0,

 

 rg(t,n),

ytφφ(n/t)

φ

t|N, t|n

rg(n), then

rg = min n≥1

rg(n) = min

1≤n≤N

en ≥ σk−1(n)rg ≥ nk−1rg. This completes step (2), provided that rg is positive. If it is not positive, then our test will be inconclusive, since we are unable to certify that even the Eisenstein part is nonnegative.

Combining the results of the previous two steps, we ﬁnd that

an ≥ nk−1rg − nk/2Cg. Since k > 2, this inequality provides an easily computed bound Q = (Cg/rg)2/(k−2) such that an > 0 for all n > Q. Because of the large gap between nk−1 and nk/2, the bound Q is typically relatively small. Finally, to certify that the coeﬃcients of g are all nonnegative, we explicitly compute the coeﬃcients an for n ≤ Q.

This method will not always work, without more careful estimates. For example, it fails if an is not eventually positive. That can occur in practice: in the example from Section 3 with d = 16, N = 4, and T = 2, the optimal modular form is

g = 1 + 4320q2 + 61440q3 + 522720q4 + 2211840q5 + 8960640q6 + ··· , which has eventually positive coeﬃcients, but

g = 16 + 69120q4 + 983040q6 + 8363520q8 + 35389440q10 + ··· ,

which does not. Thus, proving that g has nonnegative coeﬃcients requires a little more care. However, we have not observed this phenomenon for the best choices of

- T in any of the cases we have examined. If it were to occur, it could be handled by distinguishing between the values of rg(n) for diﬀerent residue classes of n modulo N, and showing that the cuspidal contribution vanishes whenever rg(n) = 0.


6. Numerical results

Table 6.1 shows our numerical results. We used the SageMath computer algebra system [29] for our calculations, with one exception: we used Magma [3] to compute bases for modular forms and the action of the Atkin-Lehner involution. This combination works conveniently, because SageMath has an interface for calling Magma code.

To produce rigorous results, we used exact rational arithmetic, and we proved nonnegativity of coeﬃcients using the techniques of Section 5. For calculations with forms of level 24, we directly solved the linear program over Q; for level 96, we instead used ﬂoating point arithmetic to obtain an approximate solution, which we then used to obtain a rational solution and prove its correctness and optimality. All the numbers in the table are rounded correctly: lower bounds are rounded down,

Table 6.1. Center density bounds in dimensions 8 through 32. The upper bound is the linear programming bound, computed using the best auxiliary function currently known [1], while the dual bound is based on the given values of N and T, and the record packing is the densest packing currently known [15]. In dimensions 12 and 16, we include both N = 96 and N = 24 for comparison.

Dimension Record packing Dual bound Upper bound N T 8 0.0625 0.0625 0.0625 1 1 12 0.037037 0.062446 0.062742 96 9

0.059781 24 4 16 0.0625 0.106284 0.107059 96 20

0.103948 24 6 20 0.131537 0.260996 0.276169 24 9 24 1 1 1 1 2 28 1 4.591741 4.828588 24 9 32 2.565784 28.086665 29.942182 24 12

and upper bounds are rounded up. The data underlying the new bounds in Table 6.1 can be downloaded from [13]. In the notation of Section 3, this data set contains the q-expansion coeﬃcients for g(z) = n anqn and g(z) = n bnqn with 0 ≤ n < 500, which is enough information to determine these modular forms uniquely.

7. Open problems

Our new lower bounds in Table 6.1 come fairly close to the known upper bounds, but they do not agree to many decimal places. We believe that the upper bounds agree with the true linear programming bound, aside from rounding the last decimal place up, while the lower bounds could be further improved. One diﬃculty in doing so is that modular forms are inherently quantized: in the summation formula

2√n √

∞

d/2 ∞

anf(√n) =

2 √

bn f

,

N

N

n=0

n=0

there is no possibility to perturb the radii √n or 2 n/N slightly, and so one must do the best one can using only radii of these forms. In particular, closely matching the upper bound may require N to be very large, perhaps on the order of 1010 if we wish to match ten digits, and dealing with such large N is not practical. Any feasible method that could close the gap between the primal and dual bounds to within a factor of 1+10−10 would be a signiﬁcant advance, and modular forms might not be the right tool for this purpose. For comparison, [33] and [30] obtain dual linear programming bounds in high dimensions using an entirely diﬀerent approach.

Another topic we leave open is computations in dimensions that are not divisible by 4. We see no theoretical obstacle to such an extension: one must simply use modular forms of odd weight (for dimensions divisible by 2 but not 4) or half-integral weight (for odd dimensions), and replace Γ0(N) with Γ1(N) so that such forms exist. However, we have not implemented these computations. We have also not explored the uncertainty principle introduced in [4] and further studied in [8], for which one could again prove dual bounds using modular forms.

One intriguing possibility that may be nearly within reach is proving that there exists a dimension in which the linear programming bound is not sharp. All dimensions except 1, 2, 8, and 24 seem to have this property, but so far no proof is known. Three dimensions would be a natural target, because we know the optimal packing density, and thus it would suﬃce to prove any dual bound greater than this density. In higher dimensions, it would require an improvement on the linear programming bound. The only such bound currently known is Theorem 1.4 from de Laat, Oliveira, and Vallentin’s paper [22], which is a reﬁnement of the linear programming bound that seems to give a small numerical improvement in dimensions 3, 4, 5, 6, 7, and 9 (see Table 1 in [22]) and presumably higher dimensions as well, aside from 24. Any dual bound greater than this improved upper bound would suﬃce to show that the linear programming bound is not sharp. Conversely, it would be interesting to prove dual bounds for the theorem of de Laat, Oliveira, and Vallentin itself.

References

- [1] N. Afkhami-Jeddi, H. Cohn, T. Hartman, D. de Laat, and A. Tajdini, High-dimensional sphere packing and the modular bootstrap, J. High Energy Phys. 2020, no. 12, 066, 44 pp. arXiv:2006.02560 doi:10.1007/JHEP12(2020)066
- [2] G. E. Andrews, R. Askey, and R. Roy, Special Functions, Encyclopedia of Mathematics and its Applications 71, Cambridge University Press, Cambridge, 1999. doi:10.1017/CBO9781107325937 MR1688958
- [3] W. Bosma, J. Cannon, and C. Playoust, The Magma algebra system I: the user language, J. Symbolic Comput. 24 (1997), no. 3–4, 235–265. doi:10.1006/jsco.1996.0125 MR1484478
- [4] J. Bourgain, L. Clozel, and J.-P. Kahane, Principe d’Heisenberg et fonctions positives, Ann. Inst. Fourier (Grenoble) 60 (2010), no. 4, 1215–1232. arXiv:0811.4360 doi:10.5802/aif.2552 MR2722239
- [5] H. Cohen, Number Theory. Volume II: Analytic and Modern Tools, Graduate Texts in Mathematics 240, Springer, New York, 2007. doi:10.1007/978-0-387-49894-2 MR2312338
- [6] H. Cohn, New upper bounds on sphere packings II, Geom. Topol. 6 (2002), 329–353. arXiv:math/0110010 doi:10.2140/gt.2002.6.329 MR1914571
- [7] H. Cohn and N. Elkies, New upper bounds on sphere packings I, Ann. of Math. (2) 157 (2003), no. 2, 689—714. arXiv:math/0110009 doi:10.4007/annals.2003.157.689 MR1973059
- [8] H. Cohn and F. Gonc¸alves, An optimal uncertainty principle in twelve dimensions via modular forms, Invent. Math. 217 (2019), no. 3, 799–831. arXiv:1712.04438 doi:10.1007/s00222-01900875-4 MR3989254
- [9] H. Cohn and A. Kumar, Universally optimal distribution of points on spheres, J. Amer. Math. Soc. 20 (2007), no. 1, 99–148. arXiv:math/0607446 doi:10.1090/S0894-0347-06-00546-7 MR2257398
- [10] H. Cohn and A. Kumar, Optimality and uniqueness of the Leech lattice among lattices, Ann. of Math. (2) 170 (2009), no. 3, 1003–1050. arXiv:math/0403263 doi:10.4007/annals.2009.170.1003 MR2600869
- [11] H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, and M. Viazovska, The sphere packing problem in dimension 24, Ann. of Math. (2) 185 (2017), no. 3, 1017–1033. arXiv:1603.06518 doi:10.4007/annals.2017.185.3.8 MR3664817
- [12] H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, and M. Viazovska, Universal optimality of the E8 and Leech lattices and interpolation formulas, preprint, 2019. arXiv:1902.05438
- [13] H. Cohn and N. Triantaﬁllou, Data for “Dual linear programming bounds for sphere packing via modular forms”, data set, DSpace@MIT, 2021. https://hdl.handle.net/1721.1/130355
- [14] H. Cohn and Y. Zhao, Sphere packing bounds via spherical codes, Duke Math. J. 163 (2014), no. 10, 1965–2002. arXiv:1212.5966 doi:10.1215/00127094-2738857 MR3229046
- [15] J. H. Conway and N. J. A. Sloane, Sphere Packings, Lattices and Groups, third edition, Grundlehren der Mathematischen Wissenschaften 290, Springer-Verlag, New York, 1999. doi:10.1007/978-1-4757-6568-7 MR1662447


- [16] P. Deligne, La conjecture de Weil. I, Inst. Hautes Etudes´ Sci. Publ. Math. 43 (1974), 273–307. http://www.numdam.org/item?id=PMIHES_1974__43__273_0 MR0340258
- [17] F. Diamond and J. Im, Modular forms and modular curves, in V. K. Murty, ed., Seminar on Fermat’s Last Theorem (Toronto, ON, 1993–1994), pp. 39–133, CMS Conf. Proc. 17, Amer. Math. Soc., Providence, RI, 1995. MR1357209
- [18] F. Diamond and J. Shurman, A First Course in Modular Forms, Graduate Texts in Mathematics 228, Springer-Verlag, New York, 2005. doi:10.1007/978-0-387-27226-9 MR2112196
- [19] T. C. Hales, A proof of the Kepler conjecture, Ann. of Math. (2) 162 (2005), no. 3, 1065–1185. doi:10.4007/annals.2005.162.1065 MR2179728
- [20] T. Hales, M. Adams, G. Bauer, T. D. Dang, J. Harrison, L. T. Hoang, C. Kaliszyk, V. Magron, S. McLaughlin, T. T. Nguyen, Q. T. Nguyen, T. Nipkow, S. Obua, J. Pleso, J. Rute, A. Solovyev, T. H. A. Ta, N. T. Tran, T. D. Trieu, J. Urban, K. Vu, and R. Zumkeller, A formal proof of the Kepler conjecture, Forum Math. Pi 5 (2017), e2, 29 pp. arXiv:1501.02155 doi:10.1017/fmp.2017.1 MR3659768
- [21] E. Hecke, Uber¨ die Bestimmung Dirichletscher Reihen durch ihre Funktionalgleichung, Math. Ann. 112 (1936), no. 1, 664–699. doi:10.1007/BF01565437 MR1513069
- [22] D. de Laat, F. M. de Oliveira Filho, and F. Vallentin, Upper bounds for packings of spheres of several radii, Forum Math. Sigma 2 (2014), e23, 42 pp. arXiv:1206.2608 doi:10.1017/fms.2014.24 MR3264261
- [23] E. H. Lieb and M. Loss, Analysis, second edition, Graduate Studies in Mathematics 14, American Mathematical Society, Providence, RI, 2001. doi:10.1090/gsm/014 MR1817225
- [24] S. D. Miller and W. Schmid, Summation formulas, from Poisson and Voronoi to the present, in Noncommutative Harmonic Analysis, Progr. Math. 220, 419–440, Birkh¨auser Boston, Boston, MA, 2004. arXiv:math/0304187 doi:10.1007/978-0-8176-8204-0 15 MR2036579

- [25] H. D. Mittelmann and F. Vallentin, High-accuracy semideﬁnite programming bounds for kissing numbers, Experiment. Math. 19 (2010), no. 2, 175–179. arXiv:0902.1105 https://projecteuclid.org/euclid.em/1276784788 MR2676746
- [26] A. Ogg, Modular Forms and Dirichlet Series, W. A. Benjamin, Inc., New York-Amsterdam,

1969. MR0256993

- [27] M. Ohta, On the p-adic Eichler-Shimura isomorphism for Λ-adic cusp forms, J. Reine Angew. Math. 463 (1995), 49–98. doi:10.1515/crll.1995.463.49 MR1332907
- [28] D. Radchenko and M. Viazovska, Fourier interpolation on the real line, Publ. Math. Inst. Hautes Etudes´ Sci. 129 (2019), 51–81. arXiv:1701.00265 doi:10.1007/s10240-018-0101-z MR3949027
- [29] SageMath, the Sage Mathematics Software System (Version 8.8), The Sage Developers, 2019, http://www.sagemath.org.
- [30] A. Scardicchio, F. H. Stillinger, and S. Torquato, Estimates of the optimal density of sphere packings in high dimensions, J. Math. Phys. 49 (2008), no. 4, 043301, 15 pp. arXiv:0705.1482 doi:10.1063/1.2897027 MR2412293
- [31] W. Stein, Modular Forms, a Computational Approach, Graduate Studies in Mathematics 79, American Mathematical Society, Providence, RI, 2007 doi:10.1090/gsm/079 MR2289048
- [32] A. Thue, Om nogle geometrisk-taltheoretiske Theoremer, Forhandlingerne ved de Skandinaviske Naturforskeres 14 (1892), 352–353.
- [33] S. Torquato and F. H. Stillinger, New conjectural lower bounds on the optimal density of sphere packings, Experiment. Math. 15 (2006), no. 3, 307–331. arXiv:math/0508381 https://projecteuclid.org/euclid.em/1175789761 MR2264469
- [34] M. S. Viazovska, The sphere packing problem in dimension 8, Ann. of Math. (2) 185 (2017), no. 3, 991–1015. arXiv:1603.04246 doi:10.4007/annals.2017.185.3.7 MR3664816


Microsoft Research New England, One Memorial Drive, Cambridge, MA 02142 Email address: cohn@microsoft.com

Department of Mathematics, Massachusetts Institute of Technology, Cambridge,

MA 02139 Current address: Department of Mathematics, University of Georgia, Athens, GA 30602 Email address: nicholas.triantafillou@gmail.com

