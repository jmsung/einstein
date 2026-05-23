---
type: source
kind: paper
title: "Distributionally robust optimization with polynomial densities: theory, models and algorithms"
authors: Etienne de Klerk, Daniel Kuhn, Krzysztof Postek
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1805.03588v1
source_local: ../raw/2018-klerk-distributionally-robust-optimization-polynomial.pdf
topic: general-knowledge
cites:
---

arXiv:1805.03588v1[math.OC]9May2018

Distributionally robust optimization with polynomial densities: theory, models and algorithms

Etienne de Klerk∗ Daniel Kuhn† Krzysztof Postek‡ May 10, 2018

Abstract

In distributionally robust optimization the probability distribution of the uncertain problem parameters is itself uncertain, and a ﬁctitious adversary, e.g., nature, chooses the worst distribution from within a known ambiguity set. A common shortcoming of most existing distributionally robust optimization models is that their ambiguity sets contain pathological discrete distribution that give nature too much freedom to inﬂict damage. We thus introduce a new class of ambiguity sets that contain only distributions with sum-of-squares polynomial density functions of known degrees. We show that these ambiguity sets are highly expressive as they conveniently accommodate distributional information about higher-order moments, conditional probabilities, conditional moments or marginal distributions. Exploiting the theoretical properties of a measure-based hierarchy for polynomial optimization due to Lasserre [SIAM J. Optim. 21(3) (2011), pp. 864–885], we prove that certain worst-case expectation constraints are computationally tractable under these new ambiguity sets. We showcase the practical applicability of the proposed approach in the context of a stylized portfolio optimization problem and a risk aggregation problem of an insurance company.

Keywords: distributionally robust optimization semideﬁnite programming sum-of-squares polynomials generalized eigenvalue problem AMS classiﬁcation: 90C22, 90C26, 90C15

# 1 Introduction

Since George Dantzig’s 1955 paper on linear programming under uncertainty [10], the ﬁeld of stochastic programming has developed numerous methods for solving optimization problems that depend on uncertain parameters governed by a known probability distribution, see, e.g., [5, 36, 42]. Stochastic programming usually aims to minimize a probability functional such as the expected value, a percentile or the conditional value-at-risk of a given cost function. In practice, however, the distribution that is needed to evaluate this probability functional is at best indirectly observable through independent training samples. Thus, the stochastic programming approach is primarily useful when there is abundant training data. If data is scarce or absent, on the other hand,

![image 1](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile1.png>)

∗Tilburg University & TU Delft, The Netherlands; E.deKlerk@uvt.nl †EPFL, Lausanne, Switzerland; daniel.kuhn@epﬂ.ch ‡Erasmus University Rotterdam, The Netherlands; postek@ese.eur.nl

it may be more adequate to use a robust optimization approach, which models the uncertainty through the set of all possible (or suﬃciently likely) uncertainty realizations and minimizes the worst-case costs. Robust optimization is the appropriate modeling paradigm for safety-critical applications with little tolerance for failure and has been popularized in the late 1990’s, when it was discovered that robust optimization models often display better tractability properties than stochastic programming models [1]. Distributionally robust optimization is a hybrid approach that attempts to salvage the tractability of robust optimization while maintaining the beneﬁts of (limited) distributional information. In this context, uncertainty is modeled through an ambiguity set, that is, a family of typically inﬁnitely many diﬀerent distributions that are consistent with the available training data or any prior distributional information, and the objective is to minimize the worst-case expected costs across all distributions in the ambiguity set. A distributionally robust newsvendor model that admits an analytical solution has been investigated as early as in 1958 [39], and the theoretical properties of distributionally robust linear programs were ﬁrst studied in 1966 [46]. Interest in distributionally robust optimization has also been fuelled by important applications in ﬁnance [34, 33]. However, only recently it was recognized that many distributionally robust optimization problems of practical relevance can actually be solved in polynomial time. Tractability results are available both for moment ambiguity sets, which contain all distributions that satisfy a ﬁnite number of moment conditions [11, 15, 45], as well as for metric-based ambiguity sets, which contain all distributions within a prescribed distance from a nominal distribution with respect to some probability metric [2, 31]. In all these cases, the extremal distributions that determine the worst-case expectation are discrete, and the number of their discretization points is often surprisingly small, e.g., proportional to the number of moment constraints. As these unnatural discrete distributions are almost always inconsistent with the available training samples, distributionally robust optimization models with moment and metric-based ambiguity sets are often perceived as overly pessimistic.

In an attempt to mitigate the over-conservatism of traditional distributionally robust optimization, several authors have studied moment ambiguity sets that require their member distributions to satisfy additional structural properties such as symmetry, unimodality, monotonicity or smoothness etc. By leveraging ideas from Choquet theory and polynomial optimization, it has been shown that the resulting distributionally robust optimization problems admit hierarchies of increasingly accurate semideﬁnite programming (SDP) bounds [35]. An exact SDP reformulation for the worst-case probability of a polytope with respect to all unimodal distributions with known ﬁrst and second moments is derived in [44], while second-order conic reformulations of distributionally robust individual chance constraints with moment and unimodality information are reported in [27]. For a survey of recent results on distributionally robust uncertainty quantiﬁcation and chance constrained programming problems with moment and structural information we refer to [18]. Even though unimodality or monotonicity conditions eliminate all discrete distributions from a moment ambiguity set, the extremal distributions that critically determine all worst-case expectations remain pathological. For example, all extremal unimodal distributions are supported on line segments emanating from a single point in space (the mode) and thus fail to be absolutely continuous with respect to the Lebesgue measure. Thus, the existing distributionally robust optimization models with structural information remain overly conservative. This observation motivates us to investigate a new class of ambiguity sets that contain only distributions with non-degenerate polynomial density functions.

This paper aims to study worst-case expectation constraints of the form sup

EPf(x,z) ≤ 0, (1)

P∈P

where x ∈ Rn is a decision vector, z ∈ Rm is an uncertain parameter governed by an ambiguous probability distribution P ∈ P, and f(x,z) is an uncertainty-aﬀected constraint function that can be interpreted as a cost. In words, the constraint (1) requires that the expected cost of the decision x be non-positive for every distribution in the ambiguity set P. Throughout the paper we will assume that f(x,z) depends polynomially on z and that each distribution P ∈ P admits a sum-of-squares (hence non-negative) polynomial density function h(z) with respect to some prescribed reference measure µ on Rm (e.g., the Lebesgue measure). Imposing an upper bound on the polynomial degree of h(z) thus yields a ﬁnite-dimensional parameterization of the ambiguity set P. Moreover, many popular distributional properties can be expressed through linear constraints on the coeﬃcients of h(z) and are thus conveniently accounted for in the deﬁnition of P. Examples include moment bounds, probability bounds for certain subsets of Rm, bounds on conditional tail probabilities and marginal distribution conditions. Note that by ﬁxing the marginal distributions of all components of z, the worst-case expectation problem on the left-hand side of (1) reduces to a Fr´echet problem that seeks the worst-case copula of the uncertain parameters.

By leveraging a measure-based hierarchy for polynomial optimization due to Lasserre [24], we will demonstrate that the subordinate worst-case probability problem in (1) admits an exact SDP reformulation. Under mild additional conditions on f(x,z), we will further prove that the feasible set of the constraint (1) admits a polynomial-time separation oracle. Moreover, we will analyze the convergence of the worst-case expectation in (1) as the polynomial degree of h(z) tends to inﬁnity, and we will illustrate the practical use of the proposed approach through numerical examples.

More succinctly, the main contributions of this paper can be summarized as follows:

- (i) Modeling power: We introduce a new class of ambiguity sets containing distributions that admit sum-of-squares polynomial density functions of degree at most 2r, r ∈ N, with respect to a given reference measure. Ambiguity sets of this type are highly expressive as they conveniently accommodate distributional information about higher-order moments, conditional probabilities or conditional moments. They also allow the modeler to prescribe (not necessarily discrete) marginal distributions that must be matched exactly by all distributions in the ambiguity set.
- (ii) Computational tractability: We identify general conditions under which the worst-case expectations over the new ambiguity sets can be reformulated exactly as tractable SDPs with

O n+r r variables. We also propose an eﬃcient heuristic for computing the worst-case expectations approximately by solving a sequence of signiﬁcantly smaller SDPs. Finally, we delineate

conditions under which the feasible sets of the worst-case expectation constraints admit a polynomial-time separation oracle and thus lend themselves to eﬃcient optimization via the ellipsoid method.

- (iii) Convergence analysis: We demonstrate that, as r tends to inﬁnity, the worst-case expectations over the new ambiguity sets converge monotonically to classical worst-case expectations over larger ambiguity sets that relax the polynomial density requirement. At the same time, the extremal density functions converge to pathological discrete worst-case distributions characteristic for classical moment ambiguity sets without restrictions on the density functions.
- (iv) Numerical results: We showcase the practical applicability of the proposed approach in the context of a stylyzed portfolio optimization problem and a simple Fr´echet problem inspired by [43] that models the risk aggregation problem of an insurance company.


The intimate relation between polynomial optimization and the problem of moments has already been exploited in several papers on distributionally robust optimization. For example, ideas from polynomial optimization give rise to SDP bounds on the probability of a semi-algebraic set [4] or the expected value of a piecewise polynomial [47] across all probability distributions satisfying a given set of moment constraints. These SDP bounds are tight in the univariate case or if only marginal moments are speciﬁed. Otherwise, one may obtain hierarchies of asymptotically tight SDP bounds. As an application, these techniques can be used to derive bounds on the prices of options with piecewise polynomial payoﬀ functions, based solely on the knowledge of a few moments of the underlying asset prices [3]. Moreover, asymptotically tight SDP bounds that account for both moment and structural information are proposed in [35]. However, all these approaches diﬀer from our work in that the ambiguity sets have discrete or otherwise degenerate extremal distributions.

Distributionally robust polynomial optimization problems over non-degenerate polynomial density functions that are close to a nominal density estimate (obtained, e.g., via a Legendre series density estimator) in terms of the L2-distance are considered in [30]. In this work the non-negativity of the candidate density functions is not enforced explicitly, which considerably simpliﬁes the problem and may be justiﬁed if the distance to the nominal density is suﬃciently small. It is shown that the emerging distributionally robust optimization problems are equivalent to deterministic polynomial optimization problems that are not signiﬁcantly harder than the underlying nominal problem and can be addressed by solving a sequence of tractable SDP relaxations.

Distributionally robust chance constraints with ambiguity sets containing all possible mixtures of a given parametric distribution family are studied in [24]. The mixtures are encoded through a probability density function on a compact parameter space. The authors propose an asymptotically tight SDP hierarchy of inner approximations for the feasible set of the distributionally robust chance constraint. In contrast, we explicitly represent all probability distributions in the ambiguity set through polynomial density functions that can capture a wide range of distributional features.

The remainder of this paper develops as follows. Section 2 reviews Lasserre’s measure-based approach to polynomial optimization, which is central to this paper. A major drawback of the resulting SDP hierarchies is their limited scalability. This prompts us to devise an eﬃcient heuristic solution algorithm in Section 3. Sections 4 and 5 develop SDP hierarchies for worst-case expectation constraints of the form (1) with and without moment information, respectively, and investigate the convergence of the underlying worst-case expectations as the degree of the polynomial density functions tends to inﬁnity. Section 6 highlights the modeling power of the proposed approach, while Section 7 reports on numerical results for a portfolio design problem as well as a risk aggregation problem of an insurance company. Conclusions are drawn in Section 8.

# 2 Lasserre’s measure-based hierarchy for polynomial optimization

In what follows, we denote by xα := ni=1 xα

i the monomial of the variables x = (x1,...,xn) with

i

respective exponents α = (α1,...,αn) ∈ Nn0, and we deﬁne N(n,r) := {α ∈ Nn0 : ni=1 αi ≤ r} as the set of all exponents that give rise to monomials with degree at most r. We let Σ[x] denote the

set of all sum-of-squares (SOS) polynomials in the variables x, and we deﬁne Σ[x]r as the subset of all SOS polynomials with degree at most 2r.

Now consider the polynomial global optimization problem

pαxα, (2)

pmin,K := min x∈K

p(x) = min

x∈K

α∈N(n,d)

where p(x) = α∈N(n,d) pαxα is an n-variate polynomial of degree d, and K ⊂ Rn a closed set with nonempty interior. (We assume existence of a global minimizer.)

We also assume that the moments of a ﬁnite Borel measure µ supported on K are known in the sense that they are either available in closed-form or eﬃciently computable. To be clear, we view a ﬁnite Borel measure µ on Rn as a nonnegative set function deﬁned on the Borel σ-algebra of Rn. (Recall that the Borel σ-algebra is generated by all open sets in Rn.) By deﬁnition, µ must satisfy µ(∅) = 0 and µ(∪∞i=1Si) = ∞i=1 µ(Si) for any collection of disjoint, measurable sets Si ⊂ Rn, i ∈ N, and µ(Rn) < ∞. The support of µ, denoted by supp(µ), is deﬁned as the smallest closed set K so that µ(Rn \ K) = 0.

We denote the (known) moments of µ by

xαdµ(x) for α ∈ Nn0. (3) Lasserre [24] introduced the following upper bound on pmin,K,

mα(K) :=

K

p(Kr) := min

p(x)h(x)dµ(x) :

h(x)dµ(x) = 1 (4)

h∈Σr K

![image 2](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile2.png>)

K

= min

Ex∼(K,h)[p(x)],

h∈Σ[x]r

where r is a ﬁxed integer, and x ∼ (K,h) indicates that x is a random vector supported on K that is governed by the probability measure h · dµ. It is known that if µ is the Lebesgue measure, then

p(Kr) is equal to the the smallest generalized eigenvalue of the system Av = λBv, (5)

![image 3](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile3.png>)

with v = 0, where the symmetric matrices A and B are of size n+r r with rows and columns indexed by N(n,r), and

pδmα+β+δ(K), Bα,β = mα+β(K) for α,β ∈ N(n,r). (6)

Aα,β =

δ∈N(n,d)

Lasserre [24] establishes conditions on µ and K so that limr→∞ p(Kr) = pmin,K, and the rate of convergence was subsequently studied in [9, 7, 8] for special choices of µ and K. The most general

![image 4](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile4.png>)

condition under which convergence holds, as shown in [25, Theorem 2.2], is when K is closed with nonempty interior, and the moments of µ on K satisfy the following conditions:

x2ikdµ(x) ≤ (2k)!M ∀i ∈ {1,...,n},k ∈ N, (7)

K

for some M > 0. For example, if one deﬁnes µ in terms of a ﬁnite Borel measure ϕ with supp(ϕ) = K via

dµ(x) = exp(−|x1| − ... − |xn|)dϕ(x), (8) then this choice satisﬁes the conditions (7); see [24, §3.2].

We summarize the known convergence results in Table 1.

Table 1: Known rates of convergence for the Lasserre hierarchy

![image 5](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile5.png>)

![image 6](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile6.png>)

![image 7](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile7.png>)

![image 8](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile8.png>)

![image 9](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile9.png>)

![image 10](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile10.png>)

K ⊂ Rn p(Kr) − pmin,K measure µ, supp(µ) = K reference closed, nonempty interior o(1) satisﬁes (7) [24]

![image 11](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile11.png>)

![image 12](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile12.png>)

![image 13](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile13.png>)

![image 14](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile14.png>)

![image 15](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile15.png>)

![image 16](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile16.png>)

![image 17](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile17.png>)

![image 18](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile18.png>)

![image 19](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile19.png>)

![image 20](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile20.png>)

![image 21](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile21.png>)

![image 22](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile22.png>)

compact, nonempty interior o(1) ﬁnite Borel measure [24] compact, satisﬁes interior cone condition O √ 1r Lebesgue measure [9]

![image 23](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile23.png>)

![image 24](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile24.png>)

![image 25](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile25.png>)

![image 26](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile26.png>)

![image 27](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile27.png>)

![image 28](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile28.png>)

![image 29](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile29.png>)

convex body O 1r Lebesgue measure [7] [−1,1]n Θ r 12 dµ(x) = ni=1(1 − x2i )−1/2dx [8]

![image 30](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile30.png>)

![image 31](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile31.png>)

![image 32](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile32.png>)

![image 33](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile33.png>)

![image 34](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile34.png>)

![image 35](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile35.png>)

![image 36](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile36.png>)

![image 37](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile37.png>)

![image 38](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile38.png>)

![image 39](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile39.png>)

![image 40](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile40.png>)

![image 41](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile41.png>)

![image 42](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile42.png>)

2.1 Examples of known moments

The moments (3) are available in closed-form, for example, if µ is the Lebesgue measure and K is an ellipsoid or triangulated polytope; see, e.g., [24] and [9]. For the canonical simplex, ∆n = {x ∈ Rn+ : ni=1 xi ≤ 1}, we have

n i=1 αi!

, (9)

mα(∆n) =

( ni=1 αi + n)!

![image 43](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile43.png>)

see, e.g., [22, Equation (2.4)] or [17, Equation (2.2)]. One may trivially verify that the moments for the hypercube Qn = [0,1]n are given by

mα(Qn) =

n

xαdx =

Qn

i=1

n

1

1 αi + 1

xα

.

i dxi =

i

![image 44](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile44.png>)

0

i=1

The moments for the unit Euclidean ball are given by

mα(B1(0)) =

π(n−1)/22(n+1)/2 ni=1(αi−1)!!

(n+ ni=1 αi)!! if αi is even for all i, 0 otherwise,

![image 45](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile45.png>)

(10)

where the double factorial of any integer k is deﬁned through

k!! =   

- k · (k − 2)···3 · 1 if k > 0 is odd,
- k · (k − 2)···4 · 2 if k > 0 is even, 1 if k = 0 or k = −1.


When K is an ellipsoid, one may obtain the moments from (10) by applying an aﬃne transformation of variables. Another tractable support set that will become relevant in Section 7.1 of this paper is the knapsack polytope, that is, the intersection of a hypercube and a half-space; the moments for this and related polytopes are derived in [29]. Finally, in Section 7.2 we will work with the nonnegative orthant K = Rn+. Since K is unbounded in this case, we need to introduce a measure of the form (8). A suitable choice that corresponds to dϕ(x) = 2n exp(− ni=1 xi) dx in (8), is

n

dµ(x) = exp −

xi dx.

i=1

This is the exponential measure associated with the orthogonal Laguerre polynomials. For more information, the reader is referred to [24, §3.2]. We will also use another choice of measure for

K = Rn+ in Section 7.2, namely the lognormal measure,

n

dµ(x) =

i=1

(ln(xi) − z¯i)2 2vi2

1 xivi√2π

exp −

![image 46](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile46.png>)

![image 47](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile47.png>)

![image 48](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile48.png>)

dxi, (11)

where z¯i and vi represent prescribed location and scale parameters, i = 1,...,n. The moments of µ are given by

n

exp(αiz¯i + (αivi)2/2). (12)

mα(K) =

i=1

One may readily verify that these moments do not satisfy the bounds on the moments in (7). When using this measure we are therefore not guaranteed convergence of the Lasserre hierarchy.

We stress that, even though these examples of known moments are limited, they include typical sets that are routinely used in (distributionally) robust optimization to represent uncertainty sets or supports, most notably budget uncertainty sets and ellipsoids.

# 3 An eﬃcient, heuristic implementation of a Lasserre-type hierarchy

The drawback of solving problem (4) is that it involves operations with matrices of order n+r r for increasing values of r. Thus one is limited to relatively small values of n and r.

In this section we describe a weaker hierarchy of bounds that is similar in spirit to the hierarchy in (4), but where the sizes of the corresponding generalized eigenvalue problems remain the same at each level of the hierarchy. Conceptually, the idea is to use the optimal density function, say

- h ∈ Σr at level r, to approximate the optimal density function at a higher level in the hierarchy. To explain the idea, consider again the global optimization problem (2), which minimizes an n-


variate polynomial p over a convex body K. We assume that the moments of a prescribed reference measure µ supported on K are known, and we denote these moments by

mµα(K) :=

xαdµ(x) for α ∈ Nn0,

K

where we add the superscript µ to make the dependence on the reference measure explicit. Next we compute the upper bound p(Kr) as in (4), where r is a ﬁxed (small) integer. Denoting the resulting optimal density by h(x) = β∈N(n,2r) hβxβ ∈ Σ[x]r, we can then deﬁne a new probability measure µ′ on K through

![image 49](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile49.png>)

dµ′(x) = h(x) · dµ(x). (13)

Note that we may obtain the moments of µ′ from the moments of µ via

′

mµ

α (K) =

=

=

=

xαdµ′(x)

K

xαh(x)dµ(x)

K

xα+βdµ(x)

hβ

K

β∈N(n,2r)

hβmµα+β(K) for α ∈ Nn0.

β∈N(n,2r)

Finally, one may now replace µ by µ′ and repeat the same process R times for some ﬁxed R ∈ N. The complete procedure is summarized in Algorithm 1.

Data: Polynomial p of degree d, allowed degree r ≥ d, integer order R; moments of some

measure µ up to order 2r + d + 2(R − 1)r = 2rR + d, i.e., the values mµα(K) for all α ∈ N(n,2rR + d)

Result: Upper bound of order R on pmin,K for k ← 1 to R do

![image 50](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile50.png>)

Form the matrices A and B deﬁned in (6) ; Solve the generalized eigenvalue problem for A and B in (5) to obtain the optimal

density h ∈ Σr ; Deﬁne the measure µ′ via (13) ; Obtain the moments of µ′ via mµ

′

α (K) = β∈N(n,2r) hβmµα+β(K) for all α ∈ N(n,2r(R − k) + d) ;

′

Replace µ ← µ′ and mµα(K) ← mµ

α (K) for all α ∈ N(n,2r(R − k) + d) ; end

Algorithm 1: Algorithm to compute the upper bound p(Kr,R) of order R on p(Kr).

![image 51](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile51.png>)

![image 52](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile52.png>)

The following remarks on this heuristic procedure are in order:

- 1. The bound computed by the algorithm is no better than the bound pK(r·R), but is much cheaper

![image 53](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile53.png>)

to compute because, in each iteration, it only involves generalized eigenvalue problems of order

n+r

r for a small ﬁxed integer r, e.g., r = 4.

- 2. The bounds generated by the algorithm, as indexed by R, are not guaranteed to converge to

pmin,K as R → ∞. However, one may easily obtain a convergent variant (at a computational cost) by increasing the value r inside a given iteration, if no improvement in the upper bound is obtained in that iteration.

- 3. One has to store and update a moment table indexed by α ∈ N(n,2r(R−k)+d) in iteration k, and the updating process involves simple linear algebra.


Table 2: Test functions, all with n = 2, domain K = [−1, 1]2, and minimum pmin,K = 0.

![image 54](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile54.png>)

![image 55](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile55.png>)

![image 56](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile56.png>)

![image 57](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile57.png>)

Name p(x) Matyas function 26(x21 + x22) − 48x1x2 Motzkin polynomial 64(x41x22 + x21x42) − 48x21x22 + 1

![image 58](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile58.png>)

![image 59](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile59.png>)

![image 60](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile60.png>)

![image 61](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile61.png>)

![image 62](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile62.png>)

![image 63](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile63.png>)

![image 64](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile64.png>)

![image 65](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile65.png>)

![image 66](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile66.png>)

We now give some numerical examples to indicate how this algorithm performs. We will consider the test functions in Table 2.

For ease of reference, we will denote the bound generated by Algorithm 1 by p(Kr,R). As this bound corresponds to a density function of degree rR with respect to the initial reference measure, it is natural to compare it to the stronger, but more expensive, bound pK(r·R). The following table lists diﬀerent bounds for the case r · R = 20, each corresponding to a density function of degree 40.

![image 67](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile67.png>)

![image 68](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile68.png>)

![image 69](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile69.png>)

![image 70](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile70.png>)

![image 71](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile71.png>)

![image 72](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile72.png>)

![image 73](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile73.png>)

![image 74](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile74.png>)

![image 75](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile75.png>)

![image 76](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile76.png>)

Function p(20)K p(10K ,2) p(5K,4) p(4K,5) p(2K,10)

![image 77](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile77.png>)

![image 78](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile78.png>)

![image 79](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile79.png>)

![image 80](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile80.png>)

![image 81](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile81.png>)

![image 82](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile82.png>)

![image 83](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile83.png>)

![image 84](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile84.png>)

![image 85](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile85.png>)

![image 86](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile86.png>)

![image 87](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile87.png>)

![image 88](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile88.png>)

![image 89](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile89.png>)

Matyas 0.4811 0.4989 0.7285 0.9604 1.1070 Motzkin 0.1817 0.1969 0.2907 0.3603 0.4588

![image 90](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile90.png>)

![image 91](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile91.png>)

![image 92](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile92.png>)

![image 93](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile93.png>)

![image 94](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile94.png>)

![image 95](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile95.png>)

![image 96](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile96.png>)

![image 97](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile97.png>)

Note that the p(Kr,R) bounds with largest r are the strongest in the examples, as one may expect.

![image 98](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile98.png>)

# 4 Distributionally robust constraints involving polynomial uncertainty

We now consider a worst-case feasibility constraint of the form (1), where z ∈ Rm represents a random vector with a support K ⊂ Rm, assumed to be closed and with nonempty interior. Assume that the constraint function f(x,z) displays a polynomial dependence on z. In particular, assume that f(x,z) = β∈N(m,d) fβ(x)zβ has degree d in z, where the fβ : Rn → R are functions of x only.

If the ambiguity set P contains all distributions that have an SOS polynomial density of degree at most 2r, r > 1, with respect to a a ﬁxed, ﬁnite Borel measure µ supported on K, then the worst-case expected feasibility constraint (1) reduces to

fK(r)(x) := sup

f(x,z)h(z)dµ(z) :

h∈Σ[z]r K

h(z)dµ(z) = 1 ≤ 0. (14)

K

Formally speaking, we consider an ambiguity set of the form

P = h · dµ : h ∈ Σ[z]r,

h(z)dµ(z) = 1 . (15)

K

We assume that the moments of the measure µ on K are available, and we again use the notation

mα(K) :=

zαdµ(z) for α ∈ Nm0 .

K

Expressing h ∈ Σ[z]r as h(z) = α∈N(m,2r) hαzα, the left-hand-side of (14) may be re-written as sup

hαmα+β(K) s.t.

fβ(x)

hα:α∈N(m,2r) β∈N(m,d)

α∈N(m,2r)

hαmα(K) = 1,

(16)

α∈N(m,2r)

hαzα ∈ Σ[z]r.

α∈N(m,2r)

Since the sum-of-squares condition on h is equivalent to a linear matrix inequality in its coeﬃcients hα, problem (16) constitutes a tractable semideﬁnite program (SDP) in hα, α ∈ N(m,2r), if x is ﬁxed. The next theorem establishes that we can also eﬃciently optimize over the feasible set of the constraint (14) whenever the coeﬃcient functions fβ are convex and K ⊂ Rm+.

- Theorem 1. Consider the constraint (14) and assume that all fβ are convex functions of x whose


subgradients are eﬃciently computable. Moreover, assume that K ⊂ Rm+. Then, the set of x ∈ Rn that satisfy (14) is convex and admits a polynomial-time separating hyperplane oracle.

Proof. We have to show that the function fK(r)(x) from (14) is convex in x. We may rewrite the function as

fK(r)(x) = sup

Ez∼(K,h) zβ fβ(x)

h∈Σ[z]r

β∈N(m,d)

For each h ∈ Σ[z]r, the function Ez∼(K,h) zβ fβ(x) is convex in x, since K ⊂ Rm+ implies Ez∼(K,h) zβ ≥ 0. Thus fK(r)(x) is the point-wise supremum of an inﬁnite collection of convex functions, and therefore convex itself (see, e.g., [37, Theorem 5.5]). Thus the set C := {x ∈ Rn | fK(r)(x) ≤ 0} is convex.

If x¯ ∈/ C, i.e., fK(r)(¯x) > 0, then we may construct a hyperplane that separates x¯ from C as follows. Let ¯h ∈ Σ[z]r be such that

Ez∼(K,h¯) zβ fβ(¯x) > 0.

fh¯(¯x) :=

β∈N(m,d)

One may obtain such an h¯ in polynomial time by solving the SDP (16) with ﬁxed x = x¯. Now let ∂fh¯(¯x) denote a subgradient of fh¯ at x¯. (By assumption such a subgradient is available in polynomial time.) By the deﬁnition of a subgradient, we now have

∂fh¯(¯x)T(x − x¯) ≤ fh¯(x) − fh¯(¯x) ≤ −fh¯(¯x) ∀x ∈ C. The outer linear inequality now separates x¯ from C.

![image 99](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile99.png>)

![image 100](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile100.png>)

![image 101](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile101.png>)

![image 102](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile102.png>)

Theorem 1 implies that if all coeﬃcient functions fβ are convex, one may optimize a convex function of x over a set given by constraints of the type (14) in polynomial time, e.g., by using the ellipsoid method, provided that an initial ellipsoid is known that contains an optimal solution [16].

Finally, we point out that, due to the convergence properties of the Lasserre hierarchy, one recovers the usual robust counterpart (robust against the single worst-case realization of z as in [1]) in the limit as r tends to inﬁnity.

- Theorem 2. Assume that K ⊂ Rn is closed with nonempty interior. Then, in the limit as r → ∞, the constraint (14) reduces to the usual robust counterpart constraint

max

z∈K

f(x,z) ≤ 0.

More precisely, if x ∈ K is ﬁxed, and (K,µ) satisﬁes one of the assumptions in Table 1, one has lim

r→∞

fK(r)(x) = max z∈K

f(x,z).

Moreover the rate of convergence is as given in Table 1, depending on the choice of (K,µ).

Proof. For ﬁxed x, the computation of fK(r)(x) is an SDP problem of the form (4), and the required convergence result therefore follows from the convergence of the Lasserre hierarchy (4), as

summarized in Table 1.

![image 103](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile103.png>)

![image 104](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile104.png>)

![image 105](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile105.png>)

![image 106](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile106.png>)

5 Approximate solution of the general problem of moments

In applications it is often possible to inject moment information into the ambiguity set P. For example, if there is prior information about the location or the dispersion of the random vector z, one can include constraints on its mean vector or its covariance matrix into the deﬁnition of the ambiguity set. Speciﬁcally, if it is known that Ez∼(K,h)[zβ

i

] = γi for some βi ∈ Nn0 and γi ∈ R for i = 1,...,p, one can restrict the ambiguity set (15) by including the moment constraints

K

zβ

i

h(z)dµ(z) =

α∈N(m,2r)

hαmα+β

i

(K) = γi ∀i = 1,...,p,

which reduce to simple linear equations for the coeﬃcients hα, α ∈ N(m,2r), of the density function h. In this setup, the maximization over the ambiguity set corresponds to a general problem of moments, see, e.g., [41]. We show how our approach may be used to solve this problem, and we will illustrate this through concrete examples in Section 7.

Throughout this section we assume that K ⊂ Rk is a nonempty closed set, while f0,f1,...,fp are real-valued Borel-measurable functions on K. Moreover, we assume that µ is a ﬁnite Borel measure on K such that f0,...,fp are µ-integrable.

- Theorem 3. Let Ki, i = 0,...,p, be Borel-measureable subsets of K. Then there exists an atomic Borel measure µ′ on K with a ﬁnite support of at most p + 2 points so that


fi(z)dµ(z) =

Ki

fi(z)dµ′(z) ∀i = 0,...,p.

Ki

Proof. This result is due to Rogosinsky [38], but an elementary proof is given by Shapiro [41, Lemma 3.1]; see also Lasserre [23].

![image 107](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile107.png>)

![image 108](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile108.png>)

![image 109](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile109.png>)

![image 110](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile110.png>)

As a consequence one has the following result for the problem of moments. Corollary 1. Consider the problem of moments

val := inf

f0(z)dµ(z) :

µ∈P K0

fi(z)dµ(z) = bi ∀i = 1,...,p , (17)

Ki

where P is the set of all Borel probability measures supported on K, and Ki is a Borel-measurable subset of K for each i = 0,...,p. If the problem has a solution, it has a solution that is an atomic measure supported on at most p + 2 points in K, i.e., a convex combination of at most p + 2 Dirac delta measures supported in K.

In what follows we show how the atomic measure solution, whose existence is guaranteed by Corollary 1, may be approximated arbitrarily well by SOS polynomial density functions.

- Theorem 4. Consider problem (17) with the additional assumptions that K ⊂ Rn has nonempty


interior and that the functions f0, f1, ..., fp are polynomials. Also assume that K and µ satisfy one of the assumptions in Table 1. Then, for any ǫ > 0 there exists a d ∈ N and a probability density h ∈ Σd[z] such that one has

f0(z)h(z)dµ(z) ∈ (val − ǫ,val + ǫ)

K0

fi(z)h(z)dµ(z) = (bi − ǫ,bi + ǫ) ∀i = 1,...,p.

Ki

Moreover, for the choices of K and µ in Table 1 where a rate of convergence is known, one may bound d in terms of ǫ. For example, if K is a convex body and µ the Lebesgue measure, then one may assume that d = O(1/ǫ2).

Proof. Fix a ∈ K, and consider the polynomials z  → (fi(z) − fi(a))2, i = 0,...,p. Moreover, let p be a polynomial with global minimizer a such that p(a) = 0 and p upper bounds all these polynomials on K, i.e.,

p(z) ≥ (fi(z) − fi(a))2 for all z ∈ K and all i ∈ {0,...,p}. (18) For a given probability density h ∈ Σ[z]r with K h(z)dµ(z) = 1, we denote as before

Ez∼(K,h)[p(z)] =

p(z)h(z)dµ(z).

K

Note that by (18) we have Ez∼(K,h)[p(z)] ≥ Ez∼(K,h)[(fi(z) − fi(a))2]. Combining with Jensen’s inequality, we therefore conclude

Ez∼(K,h)[(fi(z) − fi(a))] 2 ≤ Ez∼(K,h)[(fi(z) − fi(a))2] ≤ Ez∼(K,h)[p(z)].

Recalling the notation of the Lasserre hierarchy from (4), we denote pK(r) = minh∈Σ[z]

Ez∼(K,h)[p(z)].

r

![image 111](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile111.png>)

If µ and K satisfy one of the conditions from Table 1, one has limr→∞ pK(r) = 0, with the rate of convergence as indicated in the table. Thus, for any ǫ > 0 there is a suﬃciently large d ∈ N such

![image 112](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile112.png>)

that

Ez∼(K,h)[(fi(z) − fi(a))] 2 ≤ ǫ ∀r ≥ d, i ∈ {0,...,p}. Letting h∗ denote the minimizer, one has

min

h∈Σ[z]r

√ǫ ∀r ≥ d, i ∈ {0,...,p}.

![image 113](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile113.png>)

Ez∼(K,h∗)[(fi(z)] − fi(a) ≤

To complete the proof, we simply have to associate a with an atom of the optimal atomic distribution from Corollary 1.

![image 114](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile114.png>)

![image 115](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile115.png>)

![image 116](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile116.png>)

![image 117](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile117.png>)

As a consequence of Theorem 4, we may obtain approximate solutions to the generalized problem of moments (17) by solving SDPs of the form:

fi(z)h(z)dµ(z) = [bi − ǫ,bi + ǫ] ∀i = 1,...,p ,

min

f0(z)h(z)dµ(z) :

h∈Σ[z]r K0

Ki

for given r ∈ N and ǫ ≥ 0, and we will do precisely that in the example of Section 7.1. We remark that these SDPs are diﬀerent from the ones studied by Lasserre [23], where an outer approximation of the cone of ﬁnite Borel measures supported on K is used, whereas we use an inner approximation.

# 6 Modeling power

The ambiguity set P deﬁned in (15) contains all distributions supported on a convex body K that have an SOS polynomial density h ∈ Σ[z]r with respect to a prescribed reference measure µ. For any ﬁxed x, the worst-case expectation fK(r)(x) on the left-hand-side of the worst-case feasibility constraint (14) can be computed eﬃciently by solving the SDP (16). The ambiguity set P admits several generalizations that preserve the SDP-representability of the worst-case expectation.

Moment information As already discussed in Section 5, conditions on (mixed) moment values of diﬀerent random variables give rise to simple linear conditions on the polynomial coeﬃcients of h.

Conﬁdence information If the random vector z is known to materialize inside a given Borel set C ⊂ Rm with probability γ ∈ [0,1], we can add the condition Pz∼(K,h)[z ∈ C] = γ to the deﬁnition of the ambiguity set P. Moreover, if the moments mα(K∩C) of the reference measure µ over K∩C are either available analytically or eﬃciently computable for all α ∈ N(m,2r), then this condition can be re-expressed as the following simple linear equation in the polynomial coeﬃcients of h.

hαmα(K ∩ C) = γ

1z∈C h(z)dµ(z) =

K

α∈N(m,2r)

Upper and lower bounds on Pz∼(K,h)[z ∈ C] can be handled similarly in the obvious manner. In the context of purely moment-based ambiguity sets, such probability bounds have been studied in [45].

Conditional probabilities Given any two Borel sets C1,C2 ⊂ Rm and a probability γ ∈ [0,1], we can also enforce the condition Pz∼(K,h)[z ∈ C2|z ∈ C1] = γ in the deﬁnition of P. If the moments mα(K ∩ C1) and mα(K ∩ C1 ∩ C2) of the reference measure µ are either available analytically or eﬃciently computable for all α ∈ N(m,2r), then this condition can be re-expressed as

h(z)dµ(z) ⇐⇒

12∩C2 h(z)dµ(z) = γ

1z∈C

1z∈C

1

K

K

hα (mα(K ∩ C1 ∩ C2) − γ mα(K ∩ C1)) = 0,

α∈N(m,2r)

which is again linear in the coeﬃcients of h. Upper and lower bounds on conditional probabilities can be handled similarly.

Conditional moment information If it is known that Ez∼(K,h)[zβ|C] = γ for some β ∈ Nn0, Borel set C ⊂ Rm and γ ∈ R, while the moments mα+β(K ∩ C) of the reference measure µ over set K ∩ C are either available analytically or eﬃciently computable for all α ∈ N(m,2r), then one can add the following condition to the ambiguity set P, which is linear in the coeﬃcients of h.

zβ1z∈C h(z)dµ(z) = γ

1z∈C h(z)dµ(z) ⇐⇒

K

K

hα (mα+β(K ∩ C) − γ mα(K ∩ C)) = 0,

α∈N(m,2r)

Multiple reference measures The distributions in the ambiguity set P deﬁned in (15) depend both on the reference measure µ as well as the density function h. A richer ambiguity set can be constructed by specifying multiple reference measures µi with corresponding density functions hi ∈ Σ[z]r, i = 1,...,p. The distributions in the resulting ambiguity set are of the form pi=1 hi·dµi. If the moments miα(K) of the reference measure µi over K are either available analytically or eﬃciently computable for all α ∈ N(m,2r) and i = 1,...,p, then the normalization constraint can be recast as

p

hiαmiα(K) = γi ∀i = 1,...,p and

γi = 1,

i=1

α∈N(m,2r)

where γ = (γ1,...,γp) ≥ 0 constitutes an auxiliary decision vector. The resulting ambiguity set can be interpreted as a convex combination of p ambiguity sets of the form (15) and thus lends itself for modeling multimodality information; see, e.g., [20]. In this case, γi captures the probability of the i-th mode, which may itself be uncertain. Thus, γ should range over a subset of the probability simplex, e.g., a φ-divergence uncertainty set of the type studied in [2].

Marginal distributions It is often easier to estimate the marginal distributions of all m components of a random vector z instead of the full joint distribution. Marginal distribution information can also be conveniently encoded in ambiguity sets of the type (15). To see this, assume that the marginal distribution of zi is given by µi and is supported on a compact interval Ki ⊂ R, i = 1,...,m. In this case it makes sense to set K =×

m i=1 Ki and to deﬁne the reference mea-

sure µ through dµ = mi=1 dµi. Thus, µ coincides with the product of the known marginals. The requirement

dµj(zj) = 1 ∀zi ∈ Ki, ∀i = 1,...,m

h(z)

×j =i Kj

j =i

then ensures that the marginal distribution of zi under h · dµ exactly matches µi. If the moments mα

(Ki) of the marginal distribution µi over Ki are either available analytically or eﬃciently computable for all αi = 1,...,2r, then the above condition simpliﬁes to the linear equations

i

(Kj) = 0 ∀ℓ = 1,...,2r, ∀i = 1,...,m.

hα

(Kj) = 1 and

mα

mα

hα

j

j

j =i

j =i

α∈N(m,2r) αi=ℓ

α∈N(m,2r) αi=0

(19) Situations where the marginals of groups of random variables are known can be handled analogously. Note that when all marginals are known, there is only ambiguity about the dependence structure or copula of the components of z [40]. Quantifying the worst-case copula amounts to

solving a so-called Fr´echet problem. In distributionally robust optimization, Fr´echet problems with discrete marginals or approximate marginal matching conditions have been studied in [13, 12, 43].

Besides the ambiguity set P, the constraint function f also admits some generalizations that preserve the SDP-representability of the worst-case expectation in (14).

Uncertainty quantiﬁcation problems If the constraint function f in (14) is given by f(x,z) = 1z∈C for some Borel set C ⊂ Rm, then the worst-case expectation reduces to the worst-case probability of the set C. Moreover, if the moments mα(K ∩ C) of the reference measure µ over K ∩ C are either available analytically or eﬃciently computable for all α ∈ N(m,2r), then the worst-case probability can be computed by solving a variant of the SDP (16) with the alternative objective function

hαmα(K ∩ C).

α∈N(m,2r)

# 7 Numerical experiments

In the following we will exemplify the proposed approach to distributionally robust optimization in the context of ﬁnancial portfolio analysis (Section 7.1) and risk aggregation (Section 7.2).

- 7.1 Portfolio analysis


Consider a portfolio optimization problem, where the decision vector x ∈ Rn captures the percentage weights of the initial capital allocated to n diﬀerent assets. By deﬁnition, one thus has xi ∈ [0,1] for all i = 1,...,n and i xi = 1. We assume that the asset returns ri = (ui + li)/2 + zi(ui − li)/2 depend linearly on some uncertain risk factors zi ∈ [−1,1] for all i = 1,...,n, where li and ui represent known upper and lower bounds on the i-th return, respectively. In this framework, we denote by z ∈ Rn the vector of all risk factors and by K = [−1,1]n its support. Moreover, the portfolio return can be expressed as

f(x,z) =

n

xi · ((ui + li)/2 + zi(ui − li)/2).

i=1

Unless otherwise stated, we set µ to the Lebesgue measure on Rn. Modeling the probability density functions as SOS polynomials allows to account for various statistical properties and stylized facts of real asset returns as described in [6]. For example, the proposed approach can conveniently capture gain loss asymmetry, i.e., the observation that large drawdowns in stock prices and stock index values are more common than equally large upward movements. This feature can be modeled by assigning a higher probability to an individual asset’s large upward returns than to its low downward returns. Speciﬁcally, the ambiguity set may include the conditions Pz∼(K,h)(zi ≤ ai) = γ1 and Pz∼(K,h)(zi ≥ bi) = γ2 for some thresholds ai < bi and conﬁdence levels γ1 > γ2.

Similarly, our approach can handle correlations of extreme returns. As pointed in [6], in spite of the widespread use of the covariance matrix, ‘in circumstances when stock prices undergo large ﬂuctuations [...], a more relevant quantity is the conditional probability of a large (negative) return in one stock given a large negative movement in another stock.’ An example constraint on the

conditional probability of one asset’s low performance given another assets’ lower performance is Pz∼(K,h)(zi ≤ ri|zj ≤ rj) ≤ γ, where ri and rj are given thresholds, while γ is a conﬁdence level.

![image 118](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile118.png>)

![image 119](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile119.png>)

![image 120](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile120.png>)

![image 121](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile121.png>)

In this numerical experiment we evaluate the probability that the return of a ﬁxed portfolio x materializes below a prescribed threshold r, that is, we evaluate the worst case of the probability

![image 122](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile122.png>)

Pz∼(K,h) (r(x,z) ≤ r) over an ambiguity set P of the form (15) with the additional moment constraints Ez∼(K,h)[zβ

![image 123](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile123.png>)

] = γi

i

for some given exponents βi ∈ Nn0 and targets γi ∈ R for i = 1,...,p. This corresponds to computing the integral of the density function over the knapsack polytope K ∩ A(x,u,l,r), where

![image 124](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile124.png>)

n

n

A(x,u,l,r) = z ∈ Rn :

xi(ui − li)zi/2 ≤ r −

xi(ui + li)/2

![image 125](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile125.png>)

![image 126](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile126.png>)

i=1

i=1

represents a halfspace in Rn that depends on the ﬁxed portfolio x, the return bounds l = (l1,...ln) and u = (u1,...,un), and the threshold r. To formulate this problem as an SDP, we ﬁrst need to compute the moments of the monomials with respect to the Lebesgue measure over the given knapsack polytope by using the results of [29]. The worst-case probability problem can then be reformulated as the SDP

![image 127](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile127.png>)

hαmα(K ∩ A(x,u,l,r)) s.t.

sup

![image 128](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile128.png>)

h(z)

α∈N(n,2r)

hαmα(K) = 1,

α∈N(n,2r)

(K) = γi ∀i = 1,...,p,

hαmα+β

i

α∈N(n,2r)

hαzα ∈ Σ[z]r.

α∈N(n,2r)

(20)

In the numerical experiment we assume that there are n = 2 assets with lower and upper return bounds l = (0.8,0.7)⊤ and u = (1.2,1.3)⊤, respectively. We evaluate the probability that the return of the ﬁxed portfolio x = (0.75,0.25)⊤ falls below the threshold r = 0.9 (the minimum possible return of the portfolio is 0.775). We assume that the only known moment information about the asset returns is that their means both vanish, that is, we set p = 2, β1 = (1,0), β2 = (0.1) and γ1 = γ2 = 0. Table 3 reports the exact optimal values of the SDP (20) for r = 1,...,12 (R = 1). The value in the last row of the table (labeled r = ∞) provides the worst-case probability across all distributions satisfying the prescribed moment conditions (not only those with a polynomial density) and was computed using the methods described in [19]. In this case, one can also show that there exists a worst-case distribution with only two atoms. It assigns probability 0.31 to the scenario z = (1,1)⊤ and probability 0.69 to the scenario z = (0.28,0.28)⊤. We further computed the worst-case probabilities approximately by using Algorithm 1 from Section 3 for SOS parameters r = 1,...,6 and for up to R = 14 iterations. The results are given in Table 3 (R > 1).

![image 129](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile129.png>)

- 7.2 Risk aggregation


In the second experiment we study the risk aggregation problem of an insurer holding a portfolio of diﬀerent random losses zi, i = 1,...,n, corresponding to diﬀerent types of insurance claims, e.g.,

Table 3: Worst-case probabilities for the portfolio return falling below r computed by directly solving the SDP (20) (R = 1) and by using Algorithm 1 (R > 1). Missing values indicate the occurrence of numerical instability.

![image 130](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile130.png>)

![image 131](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile131.png>)

![image 132](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile132.png>)

![image 133](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile133.png>)

![image 134](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile134.png>)

R r 1 2 3 4 5 6 7 8 9 10 11 12 13 14

![image 135](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile135.png>)

![image 136](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile136.png>)

![image 137](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile137.png>)

![image 138](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile138.png>)

![image 139](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile139.png>)

- 0 0.17

![image 140](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile140.png>)

![image 141](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile141.png>)

![image 142](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile142.png>)

- 1 0.39 0.47 0.49 0.50 0.50 0.50 0.50 0.50 0.50 0.50 0.50 0.50 0.50 0.57

![image 143](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile143.png>)

![image 144](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile144.png>)

![image 145](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile145.png>)

- 2 0.48 0.52 0.54 0.55 0.56 0.57 0.60 - - - - - - -

![image 146](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile146.png>)

![image 147](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile147.png>)

![image 148](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile148.png>)

- 3 0.50 0.56 0.59 0.62 - - - - - - - - - -

![image 149](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile149.png>)

![image 150](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile150.png>)

![image 151](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile151.png>)

- 4 0.53 0.58 0.61 - - - - - - - - - - -

![image 152](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile152.png>)

![image 153](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile153.png>)

![image 154](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile154.png>)

- 5 0.55 0.59 - - - - - - - - - - - -

![image 155](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile155.png>)

![image 156](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile156.png>)

![image 157](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile157.png>)

- 6 0.56 0.60 - - - - - - - - - - - -

![image 158](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile158.png>)

![image 159](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile159.png>)

![image 160](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile160.png>)

- 7 0.58 - - - - - - - - - - - - -

![image 161](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile161.png>)

![image 162](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile162.png>)

![image 163](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile163.png>)

- 8 0.59 - - - - - - - - - - - - -

![image 164](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile164.png>)

![image 165](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile165.png>)

![image 166](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile166.png>)

- 9 0.59 - - - - - - - - - - - - -

![image 167](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile167.png>)

![image 168](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile168.png>)

![image 169](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile169.png>)

- 10 0.60 - - - - - - - - - - - - -

![image 170](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile170.png>)

![image 171](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile171.png>)

![image 172](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile172.png>)

- 11 0.61 - - - - - - - - - - - - -

![image 173](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile173.png>)

![image 174](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile174.png>)

![image 175](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile175.png>)

- 12 0.61 - - - - - - - - - - - - ∞ 0.69 - - - - - - - - - - - - -


![image 176](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile176.png>)

![image 177](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile177.png>)

![image 178](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile178.png>)

![image 179](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile179.png>)

![image 180](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile180.png>)

![image 181](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile181.png>)

![image 182](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile182.png>)

life, vehicle, health or home insurance policies, etc. Inspired by [43, § 6], we aim to estimate the worst-case probability that the sum of the n losses exceeds a critical threshold b = 10 beyond which the insurance company would be driven into illiquidity. Formally, we aim to maximize

Pz∼(K,h) (z1 + ... + zn ≥ b) (21)

across all distributions in an ambiguity set P, which reﬂects the prior distributional information available to the insurer. We will consider diﬀerent models for the domain K of z = (z1,...,zn), the reference measure µ on K and the ambiguity set P. Throughout the experiments we will always assume that the reference measure is separable with respect to the losses, that is, we assume that

dµ(z) = ̺1(z1)···̺n(zn)dz,

where ̺i denotes a given density function (with respect to the Lebesgue measure) of the random variables zi for each i = 1,...,n. We will consider the following complementary settings:

- 1. Lognormal densities: We set K = Rn+ and let ̺i be a lognormal density function deﬁned earlier in (11), but repeated here for convenience:

̺i(zi) =

1 zivi√2π

![image 183](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile183.png>)

![image 184](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile184.png>)

exp −

(log(zi) − z¯i)2 2vi2

![image 185](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile185.png>)

, (22)

where z¯i and vi represent prescribed location and scale parameters, i = 1,...,n.

- 2. Exponential densities: We set K = Rn+ and let ̺i be the exponential density function with unit rate parameter deﬁned through ̺i(zi) = exp(−zi), i = 1,...,n. The resulting reference measure is intimately related to the orthogonal Laguerre polynomials.


- 3. Uniform densities: We set K = [0,M]n for some constant M > 0 and let ̺i be the uniform density function deﬁned through ̺i(zi) = 1/M, i = 1,...,n. Note that under this choice the reference measure is proportional to the Lebesgue measure.


In order to reformulate the risk aggregation problem as a tractable SDP, we need the moments of the reference measure µ over the hypercube K and over the knapsack polytope K ∩ C, where

C = {z ∈ Rn : z1 + ... + zn ≥ b}.

For all classes of density functions described above, the moments of µ are indeed accessible. Specifically, under the lognormal densities, the moments of µ over K are given by (12), and repeated here for convenience:

mα(K) =

K

n

zα

i

i

i=1

n

(log(zi) − z¯i)2 2vi2

1 zivi√2π

exp −

![image 186](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile186.png>)

![image 187](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile187.png>)

![image 188](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile188.png>)

i=1

dz =

n

exp(αiz¯i + (αivi)2/2).

i=1

Moreover, the moments of µ over K ∩ C can be expressed as mα(K ∩ C) = mα(K) − mα(K\C)

n

n

1 zivi√2π

zα

= mα(K) −

i

![image 189](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile189.png>)

i

![image 190](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile190.png>)

K\C

i=1

i=1

(log(zi) − z¯i)2 2vi2

exp −

![image 191](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile191.png>)

dz.

To evaluate the integral in the last expression, we use the MATLAB routine adsimp(·) from [14]. Furthermore, under the exponential and the uniform densities, the moments of the reference measure µ over K and K ∩ C are all available in closed form.

We assume that the insurance company is able to estimate the marginal distributions of the individual losses either exactly or approximately by using a combination of statistical analysis and probabilistic modeling. However, the insurer has no information about the underlying copula. This type of distributional information is often justiﬁed in practice because obtaining reliable marginal information requires signiﬁcantly less data than obtaining exact dependence structures; see, e.g., [28]. Throughout the experiment we assume that there are n = 2 random losses governed by lognormal probability density functions of the form (22) with parameters z¯1 = −0.3, z¯2 = 0.4, v1 = 0.8 and v2 = 0.5. The ambiguity set P then contains all distributions of the form h · dµ, h ∈ Σ[z]r, under which the marginals of the losses follow the prescribed lognormal distributions either exactly or approximately. More precisely, we model the marginal distributional information as follows:

- 1. Marginal distribution matching: The lognormal distributions of the individual losses are matched exactly by any distribution h · dµ in the ambiguity set. This can be achieved by deﬁning the reference measure µ as the product of the marginal lognormal distributions and by requiring that h satisﬁes (19). Note that under the alternative reference measures corresponding to the exponential or uniform density functions, lognormal marginals cannot be matched exactly with polynomial densities of any degrees. Note also that an exact matching of (non-discrete) marginal distributions cannot be enforced with the existing numerical techniques for solving Fr´echet problems proposed in [13, 12, 43].
- 2. Marginal moment matching: The marginals of the individual losses have the same moments of order 0, 1 or 2 as the prescribed lognormal distributions. Note that this kind of moment


- matching can be enforced under any of the reference measures corresponding to lognormal, exponential or uniform density functions. Moreover, moment matching is also catered for in [43] bar the extra requirement that the joint distribution of the losses must have an SOS polynomial density.
- 3. Marginal histogram matching: We may associate a histogram with each marginal lognormal distribution as illustrated in Figure 1 and require that the marginals of the losses under the joint distribution h·dµ have the same histograms. This condition can be enforced under any of the reference measures corresponding to lognormal, exponential or uniform density functions. In the numerical experiments, we use histograms with 20 bins of width 0.25 starting at the origin. Histogram matching is also envisaged in [43].


- 0.8
- 1


0.6

0.6

0.4

0.4

0.2

0.2

0

0

0 1 2 3 4 5

0 1 2 3 4 5

Figure 1: Histograms of the lognormal marginal distributions of z1 (left) and z2 (right).

For K = Rn+ and the reference measure corresponding to the lognormal density functions, the worst-case values of the probability (21) are reported in Table 4. Results are shown for r ≤ 5, which corresponds to polynomial densities of degrees at most 10. The last row of the table (r = ∞) provides the worst-case probabilities across all distributions satisfying the prescribed moment or histogram conditions (not only those with a polynomial density) and was computed using the methods described in [43]. Note that under moment matching up to order 2, the worstcase probability for r = 5 amounts to 0.0021, as opposed to the much higher probability of 0.0615 obtained with the approach from [43]. A similar observation holds for histogram matching. The requirement that the distributions in the ambiguity set be suﬃciently regular in the sense that they admit a polynomial density function with respect to the reference measure is therefore restrictive and eﬀectively rules out pathological discrete worst-case distributions. Moreover, the worst-case probabilities under exact distribution matching and under histogram matching are of the same order of magnitude for all r ≤ 5 but signiﬁcantly smaller than the worst-case pobability under histogram matching for r = ∞. A key question to be asked in practice is thus whether one deems the class of distributions h · dµ with h ∈ Σ[z]r to be rich enough to contain all ‘reasonable’ distributions.

Table 5 reports the worst-case probabilities corresponding to the reference measure on K = Rn+ induced by the exponential density functions. For low values of r, the polynomial densities lack the necessary degrees of freedom to match all imposed moment constraints. In these situations, the worst-case probability problem becomes infeasible (indicated by ‘-’). When feasible, however, we managed to solve the problem for r up to 12. The density functions corresponding to large values of r are highly ﬂexible and thus result in worst-case probabilities that are closer to those obtained by the benchmark method from [43], which relaxes the restriction to a subspace of polynomial

- Table 4: Worst-case probabilities for the lognormal reference measure. Moment matching up to order Histogram Distribution

![image 192](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile192.png>)

![image 193](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile193.png>)

![image 194](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile194.png>)

![image 195](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile195.png>)

![image 196](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile196.png>)

![image 197](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile197.png>)

![image 198](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile198.png>)

r 0 1 2 matching matching

![image 199](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile199.png>)

![image 200](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile200.png>)

![image 201](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile201.png>)

![image 202](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile202.png>)

![image 203](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile203.png>)

![image 204](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile204.png>)

- 0 0.0017 0.0017 0.0017 0.0017 0.0017

![image 205](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile205.png>)

![image 206](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile206.png>)

![image 207](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile207.png>)

![image 208](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile208.png>)

![image 209](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile209.png>)

- 1 0.1432 0.0042 0.0017 0.0017 0.0017

![image 210](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile210.png>)

![image 211](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile211.png>)

![image 212](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile212.png>)

![image 213](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile213.png>)

![image 214](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile214.png>)

- 2 0.8255 0.0106 0.0020 0.0019 0.0018

![image 215](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile215.png>)

![image 216](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile216.png>)

![image 217](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile217.png>)

![image 218](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile218.png>)

![image 219](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile219.png>)

- 3 0.9982 0.0114 0.0021 0.0022 0.0019

![image 220](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile220.png>)

![image 221](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile221.png>)

![image 222](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile222.png>)

![image 223](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile223.png>)

![image 224](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile224.png>)

- 4 1.0000 0.0117 0.0021 0.0026 0.0023

![image 225](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile225.png>)

![image 226](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile226.png>)

![image 227](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile227.png>)

![image 228](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile228.png>)

![image 229](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile229.png>)

- 5 1.0000 0.0118 0.0021 0.0026 0.0023 ∞ 1.0000 1.0000 0.0615 0.0198 n/a


![image 230](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile230.png>)

![image 231](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile231.png>)

![image 232](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile232.png>)

![image 233](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile233.png>)

![image 234](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile234.png>)

![image 235](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile235.png>)

![image 236](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile236.png>)

![image 237](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile237.png>)

![image 238](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile238.png>)

![image 239](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile239.png>)

![image 240](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile240.png>)

- Table 5: Worst-case probabilities for the exponential reference measure.


![image 241](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile241.png>)

![image 242](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile242.png>)

![image 243](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile243.png>)

![image 244](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile244.png>)

![image 245](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile245.png>)

Moment matching up to order Histogram matching r 0 1 2 ℓ1-dist. ≤ 0.1 ℓ1-dist. ≤ 0.05 ℓ1-dist. ≤ 0.02

![image 246](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile246.png>)

![image 247](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile247.png>)

![image 248](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile248.png>)

![image 249](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile249.png>)

![image 250](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile250.png>)

![image 251](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile251.png>)

- 0 0.0005 - - - - -

![image 252](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile252.png>)

![image 253](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile253.png>)

![image 254](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile254.png>)

![image 255](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile255.png>)

- 1 0.0214 0.0147 - - - -

![image 256](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile256.png>)

![image 257](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile257.png>)

![image 258](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile258.png>)

![image 259](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile259.png>)

- 2 0.2058 0.0823 - - - -

![image 260](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile260.png>)

![image 261](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile261.png>)

![image 262](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile262.png>)

![image 263](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile263.png>)

- 3 0.6481 0.1484 - - - -

![image 264](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile264.png>)

![image 265](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile265.png>)

![image 266](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile266.png>)

![image 267](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile267.png>)

- 4 0.9393 0.1497 0.0086 - - -

![image 268](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile268.png>)

![image 269](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile269.png>)

![image 270](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile270.png>)

![image 271](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile271.png>)

- 5 0.9953 0.1699 0.0104 - - -

![image 272](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile272.png>)

![image 273](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile273.png>)

![image 274](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile274.png>)

![image 275](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile275.png>)

- 6 0.9998 0.1709 0.0139 - - -

![image 276](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile276.png>)

![image 277](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile277.png>)

![image 278](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile278.png>)

![image 279](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile279.png>)

- 7 1.0000 0.1800 0.0158 - - -

![image 280](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile280.png>)

![image 281](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile281.png>)

![image 282](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile282.png>)

![image 283](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile283.png>)

- 8 1.0000 0.1860 0.0182 0.0802 - -

![image 284](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile284.png>)

![image 285](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile285.png>)

![image 286](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile286.png>)

![image 287](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile287.png>)

- 9 1.0000 0.1862 0.0207 0.1076 - -

![image 288](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile288.png>)

![image 289](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile289.png>)

![image 290](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile290.png>)

![image 291](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile291.png>)

- 10 1.0000 0.1928 0.0224 0.1144 0.0515 -

![image 292](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile292.png>)

![image 293](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile293.png>)

![image 294](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile294.png>)

![image 295](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile295.png>)

- 11 1.0000 0.1968 0.0244 0.1156 0.0633 0.0204

![image 296](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile296.png>)

![image 297](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile297.png>)

![image 298](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile298.png>)

![image 299](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile299.png>)

- 12 1.0000 0.1971 0.0262 0.1160 0.0652 0.0320 ∞ 1.0000 1.0000 0.0615 n/a n/a n/a


![image 300](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile300.png>)

![image 301](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile301.png>)

![image 302](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile302.png>)

![image 303](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile303.png>)

![image 304](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile304.png>)

![image 305](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile305.png>)

![image 306](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile306.png>)

![image 307](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile307.png>)

![image 308](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile308.png>)

densities. Similar phenomena are also observed in the context of histogram matching. It was impossible to match the prescribed histogram probabilities exactly for all r ≤ 12. We thus relaxed the histogram matching conditions in the deﬁnition of the ambiguity set to allow for densities whose implied marginal histograms are within a prescribed ℓ1-distance from the target histograms. This approximate histogram matching condition is easily captured in our framework and gives rise to a few extra linear constraints on the coeﬃcients of the polynomial density function. Table 5 reports the worst-case probabilities for three diﬀerent tolerances on the histogram mismatch in terms of the ℓ1-distance. We observe that the resulting worst-case probabilities are signiﬁcantly larger than those obtained under the lognormal reference measure and increase with the ℓ1-tolerance.

Finally, Table 6 reports the worst-case probabilities corresponding to the uniform reference measure on K = [0,10]2. The results are qualitatively similar to those of Table 5, but they also show that the choice of the reference measure plays an important role when r is small.

Table 6: Worst-case probabilities for the uniform reference measure.

![image 309](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile309.png>)

![image 310](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile310.png>)

![image 311](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile311.png>)

![image 312](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile312.png>)

![image 313](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile313.png>)

Moment matching up to order Histogram matching r 0 1 2 ℓ1-dist. ≤ 0.1 ℓ1-dist. ≤ 0.05 ℓ1-dist. ≤ 0.02

![image 314](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile314.png>)

![image 315](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile315.png>)

![image 316](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile316.png>)

![image 317](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile317.png>)

![image 318](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile318.png>)

![image 319](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile319.png>)

- 0 0.5000 - - - - -

![image 320](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile320.png>)

![image 321](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile321.png>)

![image 322](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile322.png>)

![image 323](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile323.png>)

- 1 0.9082 - - - - -

![image 324](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile324.png>)

![image 325](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile325.png>)

![image 326](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile326.png>)

![image 327](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile327.png>)

- 2 0.9933 - - - - -

![image 328](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile328.png>)

![image 329](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile329.png>)

![image 330](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile330.png>)

![image 331](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile331.png>)

- 3 0.9997 0.0304 - - - -

![image 332](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile332.png>)

![image 333](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile333.png>)

![image 334](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile334.png>)

![image 335](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile335.png>)

- 4 1.0000 0.1035 - - - -

![image 336](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile336.png>)

![image 337](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile337.png>)

![image 338](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile338.png>)

![image 339](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile339.png>)

- 5 1.0000 0.1340 - - - -

![image 340](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile340.png>)

![image 341](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile341.png>)

![image 342](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile342.png>)

![image 343](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile343.png>)

- 6 1.0000 0.1612 0.0089 - - -

![image 344](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile344.png>)

![image 345](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile345.png>)

![image 346](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile346.png>)

![image 347](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile347.png>)

- 7 1.0000 0.1783 0.0166 - - -

![image 348](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile348.png>)

![image 349](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile349.png>)

![image 350](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile350.png>)

![image 351](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile351.png>)

- 8 1.0000 0.1935 0.0192 - - -

![image 352](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile352.png>)

![image 353](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile353.png>)

![image 354](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile354.png>)

![image 355](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile355.png>)

- 9 1.0000 0.2042 0.0216 0.0738 - -

![image 356](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile356.png>)

![image 357](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile357.png>)

![image 358](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile358.png>)

![image 359](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile359.png>)

- 10 1.0000 0.2133 0.0274 0.1066 0.0407 -

![image 360](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile360.png>)

![image 361](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile361.png>)

![image 362](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile362.png>)

![image 363](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile363.png>)

- 11 1.0000 0.2202 0.0292 0.1142 0.0609 -

![image 364](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile364.png>)

![image 365](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile365.png>)

![image 366](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile366.png>)

![image 367](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile367.png>)

- 12 1.0000 0.2274 0.0311 0.1163 0.0653 0.0178 ∞ 1.0000 1.0000 0.0615 n/a n/a n/a


![image 368](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile368.png>)

![image 369](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile369.png>)

![image 370](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile370.png>)

![image 371](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile371.png>)

![image 372](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile372.png>)

![image 373](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile373.png>)

![image 374](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile374.png>)

![image 375](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile375.png>)

![image 376](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile376.png>)

# 8 Conclusions

In this paper, we present ﬁrst steps towards using SOS polynomial densities in distributionally robust optimization for problems that display a polynomial dependence on the uncertain parameters. The main advantages of this approach may be summarized as follows:

- 1. The proposed framework is tractable (in the sense of polynomial-time solvability) for SOS density functions of any ﬁxed degree.
- 2. The approach oﬀers considerable modeling ﬂexibility. Speciﬁcally, one may conveniently encode various salient features of the unknown distribution of the uncertain parameters trough linear constraints and/or linear matrix inequalities.
- 3. In the limit as the degree of the SOS density functions tends to inﬁnity, one recovers the usual robust counterpart or generalized moment problem. One may therefore view the degree of the density as a tuning parameter that captures the model’s ‘level of conservativeness.’


The approach also suﬀers from shortcomings that necessitate further work and insights:

- 1. The approach is not applicable to objective or constraint functions that display a general (decision-dependent) piecewise polynomial dependence on the uncertain parameters as is the case for the recourse functions of linear two-stage stochastic programs.
- 2. The proposed distributionally robust optimization problems can be reduced to generalized eigenvalue problems or even semideﬁnite programs of large sizes that are often poorly conditioned. We have introduced a heuristic solution procedure in Section 3 as a practical remedy, but additional work is required to make the approach more scalable.


Acknowledgements Etienne de Klerk would like to thank Dorota Kurowicka and Jean Bernard Lasserre for valuable discussions and references. Daniel Kuhn gratefully acknowledges ﬁnancial support from the Swiss National Science Foundation under grant BSCGI0 157733.

![image 377](<2018-klerk-distributionally-robust-optimization-polynomial_images/imageFile377.png>)

# References

- [1] Ben-Tal, A., El Ghaoui, L., Nemirovski, A., Robust Optimization, Princeton University Press

(2009).

- [2] Ben-Tal, A. den Hertog, D., de Waegenaere, A., Melenberg, B., Rennen, G. Robust solutions of optimization problems aﬀected by uncertain probabilities. Management Science 59(2), 341–357

(2013).

- [3] Bertsimas, D., Popescu, I. On the relation between option and stock prices: a convex optimization approach, Operations Research 50(2), 358–374 (2002).
- [4] Bertsimas, D., Popescu, I. Optimal inequalities in probability theory: a convex optimization approach, SIAM Journal on Optimization 15(3), 780–804 (2005).
- [5] Birge, J.R., Louveaux, F. Introduction to Stochastic Programming, Springer (1997).
- [6] Cont, R. Empirical properties of asset returns: stylized facts and statistical issues. Quantitative Finance 1, 223–236 (2001).
- [7] de Klerk, E., Laurent, M. Comparison of Lasserre’s measure-based bounds for polynomial optimization to bounds obtained by simulated annealing. Mathematics of Operations Research, to appear. Preprint available at http://arxiv.org/abs/1703.00744
- [8] de Klerk, E., Laurent, M. Worst-case examples for Lasserre’s measure–based hierarchy for polynomial optimization on the hypercube (2018). Preprint available at http://arxiv.org/abs/1804.05524
- [9] de Klerk, E., Laurent, M., Sun, Z. Convergence analysis for Lasserre’s measure-based hierarchy of upper bounds for polynomial optimization. Mathematical Programming Series A 162(1), 363–392 (2017).
- [10] Dantzig, G.B. Linear programming under uncertainty. Management Science 1(3-4), 197–206

(1955).

- [11] Delage, E., Ye, Y. Distributionally robust optimization under moment uncertainty with application to data-driven problems. Operations Research 58(3), 595–612 (2010).
- [12] Doan, X.V., Li, X., Natarajan, K. Robustness to dependency in portfolio optimization using overlapping marginals. Operations Research 63(6), 1468–1488 (2015).
- [13] Doan X.V., Natarajan K. On the complexity of nonoverlapping multivariate marginal bounds for probabilistic combinatorial optimization problems. Operations Research 60(1),138–49

(2012).

- [14] Genz, A., Cools, R. An adaptive numerical cubature algorithm for simplices. ACM Transactions on Mathematical Software 29(3), 297–308 (2003).


- [15] Goh, J., Sim, M. Distributionally robust optimization and its tractable approximations, Operationis Research 58(4), 902–917 (2010).
- [16] Gr¨otschel, M., Lov´asz, L., Schrijver, A. Geometric Algorithms and Combinatorial Optimization. Springer (1988).
- [17] Grundmann, A., Moeller, H.M. Invariant integration formulas for the n-simplex by combinatorial methods. SIAM Journal on Numerical Analysis 15, 282–290 (1978).
- [18] Hanasusanto, G.A., Roitch, V., Kuhn, D., Wiesemann, W. A distributionally robust perspective on uncertainty quantiﬁcation and chance constrained programming. Mathematical Programming Series B 151(1), 35–62 (2015).
- [19] Hanasusanto, G.A., Roitch, V., Kuhn, D., Wiesemann, W. Ambiguous joint chance constraints under mean and dispersion information. Operations Research 65(3), 751–767 (2017).
- [20] Hanasusanto, G.A., Kuhn, D., Wallace, S.W., Zymler, S. Distributionally robust multi-item newsvendor problems with multimodal demand distributions. Mathematical Programming Series A 152(1), 1–32 (2015).
- [21] Kroo, A., Szil´ard, R. On Bernstein and Markov-type inequalities for multivariate polynomials on convex bodies. Journal of Approximation Theory 99(1), 134–152 (1999).
- [22] Lasserre, J.B., Zeron, E.S. Solving a class of multivariate integration problems via Laplace techniques. Applicationes Mathematicae 28(4), 391–405 (2001).
- [23] Lasserre, J.B. A semideﬁnite programming approach to the generalized problem of moments. Mathematical Programming Series B 112, 65–92 (2008).
- [24] Lasserre, J.B. A new look at nonnegativity on closed sets and polynomial optimization. SIAM Journal on Optimization 21(3), 864–885 (2011).
- [25] Lasserre, J.B. The K-moment problem for continuous linear functionals. Transactions of the American Mathematical Society 365(5), 2489–2504 (2012).
- [26] Lasserre, J.B., Weisser, T. Representation of distributionally robust chance-constraints (2018). Preprint available at http://arxiv.org/abs/1803.11500
- [27] Li, B., Jiang, R., Mathieu, J.L. Ambiguous risk constraints with moment and unimodality information, Mathematical Programming Series A, to appear (2017). Preprint available at http://www.optimization-online.org/DB_FILE/2016/09/5635.pdf
- [28] McNeil, A., Frey, R., Embrechts, P. Quantitative Risk Management: Concepts, Techniques and Tools, Princeton University Press (2015).
- [29] Marichal, J.-L., Mossinghof, M.J. Slices, slabs, and sections of the unit hypercube. Online Journal of Analytic Combinatorics 3, 1–11 (2008).
- [30] Mevissen, M., Ragnoli, E., Yu, J.Y. Data-driven distributionally robust polynomial optimization, Advances in Neural Information Processing Systems (NIPS) 26 (2013).


- [31] Mohajerin Esfahani, P., Kuhn, D. Data-driven distributionally robust optimization using the Wasserstein metric: performance guarantees and tractable reformulations, Mathematical Programming Series A, to appear (2017). Preprint available at https://arxiv.org/abs/1505.05116
- [32] Natarajan, K., Pachamanova, D., Sim, M. Constructing risk measures from uncertainty sets, Operations Research 57(5), 1129–1141 (2009).
- [33] Pﬂug, G.C., Pichler, A., Wozabal, D. The 1/N investment strategy is optimal under high model ambiguity, Journal of Banking & Finance 36(2), 410–417 (2012).
- [34] Pﬂug, G.C., Wozabal, D. Ambiguity in portfolio selection, Quantitative Finance 7, 435–442

(2007).

- [35] Popescu, I. A semideﬁnite programming approach to optimal-moment bounds for convex classes of distributions, Mathematics of Operations Research 30(3), 632–657 (2005).
- [36] Pr´ekopa, A. Stochastic Programming, Kluwer Academic Publishers (1995).
- [37] Rockafellar, R.T. Convex Analysis, Princeton University Press (1970).
- [38] Rogosinski, W.W. Moments of non-negative mass, Proceedings of the Royal Society A 245, 1–27 (1958).
- [39] Scarf, H. A min-max solution of an inventory problem, in H. Scarf, K. Arrow, and S. Karlin (Eds.), Studies in the Mathematical Theory of Inventory and Production, Volume 10, pp. 201–

209. Stanford University Press (1958).

- [40] Sklar, A. Fonctions de r´epartition ` n dimensions et leurs marges, Publications de l’Institut de Statistique de L’Universite´ de Paris 8, 229–231 (1959).
- [41] Shapiro, A. On duality theory of conic linear problems, Semi-Inﬁnite Programming: Recent Advances (M,A.´ Goberna and M.A. Lo´pez, eds.), Springer, 135–165 (2001).
- [42] Shapiro, A., Dentcheva, D., Ruszczy´nski, A. Lectures on Stochastic Programming: Modeling and Theory, SIAM (2009).
- [43] Van Parys, B.P.G., Goulart, P.J., Embrechts, P. Fr´echet inequalities via convex optimization (2016). Preprint available at http://www.optimization-online.org/DB_FILE/2016/07/5536.pdf
- [44] Van Parys, B.P.G., Goulart, P.J., Kuhn, D. Generalized Gauss inequalities via semideﬁnite programming. Mathematical Programming Series A 156(1-2), 271–302 (2016).
- [45] Wiesemann, W., Kuhn, D., Sim, M. Distributionally robust convex optimization. Operations Research 62(6), 1358–1376 (2014).
- [46] Za´ˇckov´a,ˇ J. On minimax solutions of stochastic linear programming problems, Casopisˇ pro peˇstov´nı´ matematiky 91, 423–430 (1966).
- [47] Zuluaga, L., Pe˜na J.F. A conic programming approach to generalized Tchebycheﬀ inequalities, Mathematics of Operations Research 30(2), 369–388 (2005).


