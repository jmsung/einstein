# arXiv:1505.05116v3[math.OC]13Jun2017

## Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations

PEYMAN MOHAJERIN ESFAHANI AND DANIEL KUHN

Abstract. We consider stochastic programs where the distribution of the uncertain parameters is only observable through a ﬁnite training dataset. Using the Wasserstein metric, we construct a ball in the space of (multivariate and non-discrete) probability distributions centered at the uniform distribution on the training samples, and we seek decisions that perform best in view of the worst-case distribution within this Wasserstein ball. The state-of-the-art methods for solving the resulting distributionally robust optimization problems rely on global optimization techniques, which quickly become computationally excruciating. In this paper we demonstrate that, under mild assumptions, the distributionally robust optimization problems over Wasserstein balls can in fact be reformulated as ﬁnite convex programs—in many interesting cases even as tractable linear programs. Leveraging recent measure concentration results, we also show that their solutions enjoy powerful ﬁnite-sample performance guarantees. Our theoretical results are exempliﬁed in mean-risk portfolio optimization as well as uncertainty quantiﬁcation.

1. Introduction

Stochastic programming is a powerful modeling paradigm for optimization under uncertainty. The goal of a generic single-stage stochastic program is to ﬁnd a decision x ∈ Rn that minimizes an expected cost EP[h(x,ξ)], where the expectation is taken with respect to the distribution P of the continuous random vector ξ ∈ Rm. However, classical stochastic programming is challenged by the large-scale decision problems encountered in today’s increasingly interconnected world. First, the distribution P is never observable but must be inferred from data. However, if we calibrate a stochastic program to a given dataset and evaluate its optimal decision on a diﬀerent dataset, then the resulting out-of-sample performance is often disappointing—even if the two datasets are generated from the same distribution. This phenomenon is termed the optimizer’s curse and is reminiscent of overﬁtting eﬀects in statistics [48]. Second, in order to evaluate the objective function of a stochastic program for a ﬁxed decision x, we need to compute a multivariate integral, which is #P-hard even if h(x,ξ) constitutes the positive part of an aﬃne function, while ξ is uniformly distributed on the unit hypercube [24, Corollary 1].

Distributionally robust optimization is an alternative modeling paradigm, where the objective is to ﬁnd a decision x that minimizes the worst-case expected cost supQ∈P EQ[h(x,ξ)]. Here, the worst-case is taken over an ambiguity set P, that is, a family of distributions characterized through certain known properties of the unknown data-generating distribution P. Distributionally robust optimization problems have been studied since Scarf’s seminal treatise on the ambiguity-averse newsvendor problem in 1958 [43], but the ﬁeld has gained thrust only with the advent of modern robust optimization techniques in the last decade [3, 9].

Date: June 14, 2017. The authors are with the Delft Center for Systems and Control, TU Delft, The Netherlands

(P.MohajerinEsfahani@tudelft.nl), and the Risk Analytics and Optimization Chair, EPFL, Switzerland (daniel.kuhn@epfl.ch).

1

Distributionally robust optimization has the following striking beneﬁts. First, adopting a worst-case approach regularizes the optimization problem and thereby mitigates the optimizer’s curse characteristic for stochastic programming. Second, distributionally robust models are often tractable even though the corresponding stochastic model with the true data-generating distribution (which is generically continuous) are #P-hard. So even if the data-generating distribution was known, the corresponding stochastic program could not be solved eﬃciently.

The ambiguity set P is a key ingredient of any distributionally robust optimization model. A good ambiguity set should be rich enough to contain the true data-generating distribution with high conﬁdence. On the other hand, the ambiguity set should be small enough to exclude pathological distributions, which would incentivize overly conservative decisions. The ambiguity set should also be easy to parameterize from data, and—ideally—it should facilitate a tractable reformulation of the distributionally robust optimization problem as a structured mathematical program that can be solved with oﬀ-the-shelf optimization software.

Distributionally robust optimization models where ξ has ﬁnitely many realizations are reviewed in [2, 7, 39]. This paper focuses on situations where ξ can have a continuum of realizations. In this setting, the existing literature has studied three types of ambiguity sets. Moment ambiguity sets contain all distributions that satisfy certain moment constraints, see for example [18, 22, 51] or the references therein. An attractive alternative is to deﬁne the ambiguity set as a ball in the space of probability distributions by using a probability distance function such as the Prohorov metric [20], the Kullback-Leibler divergence [27, 25], or the Wasserstein metric [38, 52] etc. Such metric-based ambiguity sets contain all distributions that are close to a nominal or most likely distribution with respect to the prescribed probability metric. By adjusting the radius of the ambiguity set, the modeler can thus control the degree of conservatism of the underlying optimization problem. If the radius drops to zero, then the ambiguity set shrinks to a singleton that contains only the nominal distribution, in which case the distributionally robust problem reduces to an ambiguity-free stochastic program. In addition, ambiguity sets can also be deﬁned as conﬁdence regions of goodness-of-ﬁt tests [7].

In this paper we study distributionally robust optimization problems with a Wasserstein ambiguity set centered at the uniform distribution PN on N independent and identically distributed training samples. The Wasserstein distance of two distributions Q1 and Q2 can be viewed as the minimum transportation cost for moving the probability mass from Q1 to Q2, and the Wasserstein ambiguity set contains all (continuous or discrete) distributions that are suﬃciently close to the (discrete) empirical distribution PN with respect to the Wasserstein metric. Modern measure concentration results from statistics guarantee that the unknown data-generating distribution P belongs to the Wasserstein ambiguity set around PN with conﬁdence 1 − β if its radius is a sublinearly growing function of log(1/β)/N [11, 21]. The optimal value of the distributionally robust problem thus provides an upper conﬁdence bound on the achievable out-of-sample cost.

While Wasserstein ambiguity sets oﬀer powerful out-of-sample performance guarantees and enable the decision maker to control the model’s conservativeness, moment-based ambiguity sets appear to display better tractability properties. Speciﬁcally, there is growing evidence that distributionally robust models with moment ambiguity sets are more tractable than the corresponding stochastic models because the intractable high-dimensional integrals in the objective function are replaced with tractable (generalized) moment problems [18, 22, 51]. In contrast, distributionally robust models with Wasserstein ambiguity sets are believed to be harder than their stochastic counterparts [36]. Indeed, the state-of-the-art method for computing the worstcase expectation over a Wasserstein ambiguity set P relies on global optimization techniques. Exploiting the fact that the extreme points of P are discrete distributions with a ﬁxed number of atoms [52], one may reformulate the original worst-case expectation problem as a ﬁnite-dimensional non-convex program, which can be solved via “diﬀerence of convex programming” methods, see [52] or [36, Section 7.1]. However, the

computational eﬀort is reported to be considerable, and there is no guarantee to ﬁnd the global optimum. Nevertheless, tractability results are available for special cases. Speciﬁcally, the worst case of a convex lawinvariant risk measure with respect to a Wasserstein ambiguity set P reduces to the sum of the nominal risk and a regularization term whenever h(x,ξ) is aﬃne in ξ and P does not include any support constraints [53]. Moreover, while this paper was under review we became aware of the PhD thesis [54], which reformulates a distributionally robust two-stage unit commitment problem over a Wasserstein ambiguity set as a semi-inﬁnite linear program, which is subsequently solved using a Benders decomposition algorithm.

The main contribution of this paper is to demonstrate that the worst-case expectation over a Wasserstein ambiguity set can in fact be computed eﬃciently via convex optimization techniques for numerous loss functions of practical interest. Furthermore, we propose an eﬃcient procedure for constructing an extremal distribution that attains the worst-case expectation—provided that such a distribution exists. Otherwise, we construct a sequence of distributions that attain the worst-case expectation asymptotically. As a by-product, our analysis shows that many interesting distributionally robust optimization problems with Wasserstein ambiguity sets can be solved in polynomial time. We also investigate the out-of-sample performance of the resulting optimal decisions—both theoretically and experimentally—and analyze its dependence on the number of training samples. We highlight the following main contributions of this paper.

- • We prove that the worst-case expectation of an uncertain loss (ξ) over a Wasserstein ambiguity set coincides with the optimal value of a ﬁnite-dimensional convex program if (ξ) constitutes a pointwise maximum of ﬁnitely many concave functions. Generalizations to convex functions or to sums of maxima of concave functions are also discussed. We conclude that worst-case expectations can be computed eﬃciently to high precision via modern convex optimization algorithms.
- • We describe a supplementary ﬁnite-dimensional convex program whose optimal (near-optimal) solutions can be used to construct exact (approximate) extremal distributions for the inﬁnite-dimensional worst-case expectation problem.
- • We show that the worst-case expectation reduces to the optimal value of an explicit linear program if the 1-norm or the ∞-norm is used in the deﬁnition of the Wasserstein metric and if (ξ) belongs to any of the following function classes: (1) a pointwise maximum or minimum of aﬃne functions;

(2) the indicator function of a closed polytope or the indicator function of the complement of an open polytope; (3) the optimal value of a parametric linear program whose cost or right-hand side coeﬃcients depend linearly on ξ.

- • Using recent measure concentration results from statistics, we demonstrate that the optimal value of a distributionally robust optimization problem over a Wasserstein ambiguity set provides an upper conﬁdence bound on the out-of-sample cost of the worst-case optimal decision. We validate this theoretical performance guarantee in numerical tests.


If the uncertain parameter vector ξ is conﬁned to a ﬁxed ﬁnite subset of Rm, then the worst-case expectation problems over Wasserstein ambiguity sets simplify substantially and can often be reformulated as tractable conic programs by leveraging ideas from robust optimization. An elegant second-order conic reformulation has been discovered, for instance, in the context of distributionally robust regression analysis [32], and a comprehensive list of tractable reformulations of distributionally robust risk constraints for various risk measures is provided in [39]. Our paper extends these tractability results to the practically relevant case where ξ has uncountably many possible realizations—without resorting to space tessellation or discretization techniques that are prone to the curse of dimensionality.

When (ξ) is linear and the distribution of ξ ranges over a Wasserstein ambiguity set without support constraints, one can derive a concise closed-form expression for the worst-case risk of (ξ) for various convex

risk measures [53]. However, these analytical solutions come at the expense of a loss of generality. We believe that the results of this paper may pave the way towards an eﬃcient computational procedure for evaluating the worst-case risk of (ξ) in more general settings where the loss function may be non-linear and ξ may be subject to support constraints.

Among all metric-based ambiguity sets studied to date, the Kullback-Leibler ambiguity set has attracted most attention from the robust optimization community. It has ﬁrst been used in ﬁnancial portfolio optimization to capture the distributional uncertainty of asset returns with a Gaussian nominal distribution [19]. Subsequent work has focused on Kullback-Leibler ambiguity sets for discrete distributions with a ﬁxed support, which oﬀer additional modeling ﬂexibility without sacriﬁcing computational tractability [14, 2]. It is also known that distributionally robust chance constraints involving a generic Kullback-Leibler ambiguity set are equivalent to the respective classical chance constraints under the nominal distribution but with a rescaled violation probability [27, 26]. Moreover, closed-form counterparts of distributionally robust expectation constraints with Kullback-Leibler ambiguity sets have been derived in [25].

However, Kullback-Leibler ambiguity sets typically fail to represent conﬁdence sets for the unknown distribution P. To see this, assume that P is absolutely continuous with respect to the Lebesgue measure and that the ambiguity set is centered at the discrete empirical distribution PN. Then, any distribution in a Kullback-Leibler ambiguity set around PN must assign positive probability mass to each training sample. As P has a density function, it must therefore reside outside of the Kullback-Leibler ambiguity set irrespective of the training samples. Thus, Kullback-Leibler ambiguity sets around PN contain P with probability 0. In contrast, Wasserstein ambiguity sets centered at PN contain discrete as well as continuous distributions and, if properly calibrated, represent meaningful conﬁdence sets for P. We will exploit this property in Section 3 to derive ﬁnite-sample guarantees. A comparison and critical assessment of various metric-based ambiguity sets is provided in [45]. Speciﬁcally, it is shown that worst-case expectations over Kullback-Leibler and other divergence-based ambiguity sets are law invariant. In contrast, worst-case expectations over Wasserstein ambiguity sets are not. The law invariance can be exploited to evaluate worst-case expectations via the sample average approximation.

The models proposed in this paper fall within the scope of data-driven distributionally robust optimization [20, 16, 7, 23]. Closest in spirit to our work is the robust sample average approximation [7], which seeks decisions that are robust with respect to the ambiguity set of all distributions that pass a prescribed statistical hypothesis test. Indeed, the distributions within the Wasserstein ambiguity set could be viewed as those that pass a multivariate goodness-of-ﬁt test in light of the available training samples. This amounts to interpreting the Wasserstein distance between the empirical distribution PN and a given hypothesis Q as a test statistic and the radius of the Wasserstein ambiguity set as a threshold that needs to be chosen in view of the test’s desired signiﬁcance level β. The Wasserstein distance has already been used in tests for normality [17] and to devise nonparametric homogeneity tests [40].

The rest of the paper proceeds as follows. Section 2 sketches a generic framework for data-driven distributionally robust optimization, while Section 3 introduces our speciﬁc approach based on Wasserstein ambiguity sets and establishes its out-of-sample performance guarantees. In Section 4 we demonstrate that many worst-case expectation problems over Wasserstein ambiguity sets can be reduced to ﬁnite-dimensional convex programs, and we develop a systematic procedure for constructing worst-case distributions. Explicit linear programming reformulations of distributionally robust single and two-stage stochastic programs as well as uncertainty quantiﬁcation problems are derived in Section 5. Section 6 extends the scope of the basic approach to broader classes of objective functions, and Section 7 reports on numerical results.

Notation. We denote by R+ the non-negative and by R := R ∪ {−∞,∞} the extended reals. Throughout this paper, we adopt the conventions of extended arithmetics, whereby ∞·0 = 0·∞ = 0/0 = 0 and ∞−∞ = −∞ + ∞ = 1/0 = ∞. The inner product of two vectors a,b ∈ Rm is denoted by a,b := a b. Given a norm  ·  on Rm, the dual norm is deﬁned through z ∗ := sup ξ ≤1 z,ξ . A function f : Rm → R is proper if f(ξ) < +∞ for at least one ξ and f(ξ) > −∞ for every ξ in Rm. The conjugate of f is deﬁned as f∗(z) := supξ∈Rm z,ξ − f(ξ). Note that conjugacy preserves properness. For a set Ξ ⊆ Rm, the indicator function 1Ξ is deﬁned through 1Ξ(ξ) = 1 if ξ ∈ Ξ; = 0 otherwise. Similarly, the characteristic function χΞ is deﬁned via χΞ(ξ) = 0 if ξ ∈ Ξ; = ∞ otherwise. The support function of Ξ is deﬁned as σΞ(z) := supξ∈Ξ z,ξ . It coincides with the conjugate of χΞ. We denote by δξ the Dirac distribution concentrating unit mass at ξ ∈ Rm. The product of two probability distributions P1 and P2 on Ξ1 and Ξ2, respectively, is the distribution

- P1 ⊗ P2 on Ξ1 × Ξ2. The N-fold product of a distribution P on Ξ is denoted by PN, which represents a distribution on the Cartesian product space ΞN. Finally, we set the expectation of : Ξ → R under P to EP[ (ξ)] = EP max{ (ξ),0} + EP min{ (ξ),0} , which is well-deﬁned by the conventions of extended arithmetics.


2. Data-Driven Stochastic Programming

Consider the stochastic program J := inf

EP h(x,ξ) =

h(x,ξ)P(dξ) (1)

x∈X

Ξ

with feasible set X ⊆ Rn, uncertainty set Ξ ⊆ Rm and loss function h : Rn × Rm → R. The loss function depends both on the decision vector x ∈ Rn and the random vector ξ ∈ Rm, whose distribution P is supported on Ξ. Problem (1) can be viewed as the ﬁrst-stage problem of a two-stage stochastic program, where h(x,ξ) represents the optimal value of a subordinate second-stage problem [46]. Alternatively, problem (1) may also be interpreted as a generic learning problem in the spirit of [49].

Unfortunately, in most situations of practical interest, the distribution P is not precisely known, and therefore we miss essential information to solve problem (1) exactly. However, P is often partially observable through a ﬁnite set of N independent samples, e.g., past realizations of the random vector ξ. We denote the training dataset comprising these samples by ΞN := { ξi}i≤N ⊆ Ξ. We emphasize that—before its revelationthe dataset ΞN can be viewed as a random object governed by the distribution PN supported on ΞN.

A data-driven solution for problem (1) is a feasible decision xN ∈ X that is constructed from the training dataset ΞN. Throughout this paper, we notationally suppress the dependence of xN on the training samples in order to avoid clutter. Instead, we reserve the superscript ‘ ’ for objects that depend on the training data and thus constitute random objects governed by the product distribution PN. The out-of-sample performance of xN is deﬁned as EP h( xN,ξ) and can thus be viewed as the expected cost of xN under a new sample ξ that is independent of the training dataset. As P is unknown, however, the exact out-of-sample performance cannot be evaluated in practice, and the best we can hope for is to establish performance guarantees in the form of tight bounds. The feasibility of xN in (1) implies J ≤ EP h( xN,ξ) , but this lower bound is again of limited use as J is unknown and as our primary concern is to bound the costs from above. Thus, we seek data-driven solutions xN with performance guarantees of the type

PN ΞN : EP h( xN,ξ) ≤ JN ≥ 1 − β, (2)

where JN constitutes an upper bound that may depend on the training dataset, and β ∈ (0,1) is a signiﬁcance parameter with respect to the distribution PN, which governs both xN and JN. Hereafter we refer to JN as a certiﬁcate for the out-of-sample performance of xN and to the probability on the left-hand side of (2) as its

reliability. Our ideal goal is to ﬁnd a data-driven solution with the lowest possible out-of-sample performance. This is impossible, however, as P is unknown, and the out-of-sample performance cannot be computed. We thus pursue the more modest but achievable goal to ﬁnd a data-driven solution with a low certiﬁcate and a high reliability.

A natural approach to generate data-driven solutions xN is to approximate P with the discrete empirical probability distribution

1 N

PN :=

N

δ ξ

, (3)

i

i=1

that is, the uniform distribution on ΞN. This amounts to approximating the original stochastic program (1) with the sample-average approximation (SAA) problem

JSAA := inf

x∈X

E PN

1 N

h(x,ξ) =

N

h(x, ξi) . (4)

i=1

If the feasible set X is compact and the loss function is uniformly continuous in x across all ξ ∈ Ξ, then the optimal value and optimal solutions of the SAA problem (4) converge almost surely to their counterparts of the true problem (1) as N tends to inﬁnity [46, Theorem 5.3]. Even though ﬁnite sample performance guarantees of the type (2) can be obtained under additional assumptions such as Lipschitz continuity of the loss function (see e.g., [47, Theorem 1]), the SAA problem has been conceived primarily for situations where the distribution P is known and additional samples can be acquired cheaply via random number generation. However, the optimal solutions of the SAA problem tend to display a poor out-of-sample performance in situations where N is small and where the acquisition of additional samples would be costly.

In this paper we address problem (1) with an alternative approach that explicitly accounts for our ignorance of the true data-generating distribution P, and that oﬀers attractive performance guarantees even when the acquisition of additional samples from P is impossible or expensive. Speciﬁcally, we use ΞN to design an ambiguity set PN containing all distributions that could have generated the training samples with high conﬁdence. This ambiguity set enables us to deﬁne the certiﬁcate JN as the optimal value of a distributionally robust optimization problem that minimize the worst-case expected cost.

JN := inf

x∈X

EQ h(x,ξ) (5)

sup

Q∈ PN

Following [38], we construct PN as a ball around the empirical distribution (3) with respect to the Wasserstein metric. In the remainder of the paper we will demonstrate that the optimal value JN as well as any optimal solution xN (if it exists) of the distributionally robust problem (5) satisfy the following conditions.

- (i) Finite sample guarantee: For a carefully chosen size of the ambiguity set, the certiﬁcate JN provides a 1 − β conﬁdence bound of the type (2) on the out-of-sample performance of xN.
- (ii) Asymptotic consistency: As N tends to inﬁnity, the certiﬁcate JN and the data-driven solution xN converge—in a sense to be made precise below—to the optimal value J and an optimizer x of the stochastic program (1), respectively.
- (iii) Tractability: For many loss functions h(x,ξ) and sets X, the distributionally robust problem (5) is computationally tractable and admits a reformulation reminiscent of the SAA problem (4).


Conditions (i)–(iii) have been identiﬁed in [7] as desirable properties of data-driven solutions for stochastic programs. Precise statements of these conditions will be provided in the remainder. In Section 3 we will use the Wasserstein metric to construct ambiguity sets of the type PN satisfying the conditions (i) and

(ii). In Section 4, we will demonstrate that these ambiguity sets also fulﬁll the tractability condition (iii). We see this last result as the main contribution of this paper because the state-of-the-art method for solving distributionally robust problems over Wasserstein ambiguity sets relies on global optimization algorithms [36].

3. Wasserstein Metric and Measure Concentration

Probability metrics represent distance functions on the space of probability distributions. One of the most widely used examples is the Wasserstein metric, which is deﬁned on the space M(Ξ) of all probability distributions Q supported on Ξ with EQ ξ = Ξ ξ Q(dξ) < ∞. Deﬁnition 3.1 (Wasserstein metric [29]). The Wasserstein metric dW : M(Ξ) × M(Ξ) → R is deﬁned via

Π is a joint distribution of ξ1 and ξ2 with marginals Q1 and Q2, respectively

dW Q1,Q2 := inf

ξ1 − ξ2 Π(dξ1,dξ2) :

Ξ2

for all distributions Q1,Q2 ∈ M(Ξ), where  ·  represents an arbitrary norm on Rm.

The decision variable Π can be viewed as a transportation plan for moving a mass distribution described by

- Q1 to another one described by Q2. Thus, the Wasserstein distance between Q1 and Q2 represents the cost of an optimal mass transportation plan, where the norm  ·  encodes the transportation costs. We remark that a generalized p-Wasserstein metric for p ≥ 1 is obtained by setting the transportation cost between ξ1 and ξ2 to ξ1 − ξ2 p. In this paper, however, we focus exclusively on the 1-Wasserstein metric of Deﬁnition 3.1, which is sometimes also referred to as the Kantorovich metric.


We will sometimes also need the following dual representation of the Wasserstein metric.

- Theorem 3.2 (Kantorovich-Rubinstein [29]). For any distributions Q1,Q2 ∈ M(Ξ) we have


f(ξ)Q2(dξ) , where L denotes the space of all Lipschitz functions with |f(ξ) − f(ξ )| ≤ ξ − ξ for all ξ,ξ ∈ Ξ.

f(ξ)Q1(dξ) −

dW Q1,Q2 = sup

f∈L Ξ

Ξ

Kantorovich and Rubinstein [29] originally established this result for distributions with bounded support. A modern proof for unbounded distributions is due to Villani [50, Remark 6.5, p. 107]. The optimization problems in Deﬁnition 3.1 and Theorem 3.2, which provide two equivalent characterizations of the Wasserstein metric, constitute a primal-dual pair of inﬁnite-dimensional linear programs. The dual representation implies that two distributions Q1 and Q2 are close to each other with respect to the Wasserstein metric if and only if all functions with uniformly bounded slopes have similar integrals under Q1 and Q2. Theorem 3.2 also demonstrates that the Wasserstein metric is a special instance of an integral probability metric (see e.g. [33]) and that its generating function class coincides with a family of Lipschitz continuous functions.

In the remainder we will examine the ambiguity set Bε( PN) := Q ∈ M(Ξ) : dW PN,Q ≤ ε , (6)

which can be viewed as the Wasserstein ball of radius ε centered at the empirical distribution PN. Under a common light tail assumption on the unknown data-generating distribution P, this ambiguity set oﬀers attractive performance guarantees in the spirit of Section 2.

- Assumption 3.3 (Light-tailed distribution). There exists an exponent a > 1 such that


A := EP exp( ξ a) =

exp( ξ a)P(dξ) < ∞.

Ξ

Assumption 3.3 essentially requires the tail of the distribution P to decay at an exponential rate. Note that this assumption trivially holds if Ξ is compact. Heavy-tailed distributions that fail to meet Assumption 3.3 are diﬃcult to handle even in the context of the classical sample average approximation. Indeed, under a heavy-tailed distribution the sample average of the loss corresponding to any ﬁxed decision x ∈ X may not even converge to the expected loss; see e.g. [13, 15]. The following modern measure concentration result provides the basis for establishing powerful ﬁnite sample guarantees.

- Theorem 3.4 (Measure concentration [21, Theorem 2]). If Assumption 3.3 holds, we have

PN dW P, PN ≥ ε ≤

c1 exp −c2Nεmax{m,2} if ε ≤ 1, c1 exp −c2Nεa if ε > 1,

(7)

for all N ≥ 1, m = 2, and ε > 0, where c1,c2 are positive constants that only depend on a, A, and m.1

Theorem 3.4 provides an a priori estimate of the probability that the unknown data-generating distribution P resides outside of the Wasserstein ball Bε( PN). Thus, we can use Theorem 3.4 to estimate the radius of the smallest Wasserstein ball that contains P with conﬁdence 1−β for some prescribed β ∈ (0,1). Indeed, equating the right-hand side of (7) to β and solving for ε yields

εN(β) :=

 



log(c1β−1) c2N

1/max{m,2}

if N ≥ log(c

1β−1) c2 ,

log(c1β−1) c2N

1/a

if N < log(c

1β−1) c2 .

(8)

Note that the Wasserstein ball with radius εN(β) can thus be viewed as a conﬁdence set for the unknown true distribution as in statistical testing; see also [7].

- Theorem 3.5 (Finite sample guarantee). Suppose that Assumption 3.3 holds and that β ∈ (0,1). Assume also that JN and xN represent the optimal value and an optimizer of the distributionally robust program (5)

with ambiguity set PN = Bε

N(β)( PN). Then, the ﬁnite sample guarantee (2) holds.

Proof. The claim follows immediately from Theorem 3.4, which ensures via the deﬁnition of εN(β) in (8) that PN{P ∈ Bε

N(β)( PN)} ≥ 1−β. Thus, EP[h( xN,ξ)] ≤ supQ∈ P

N

EQ[h( xN,ξ)] = JN with probability 1−β.

It is clear from (8) that for any ﬁxed β > 0, the radius εN(β) tends to 0 as N increases. Moreover, one can show that if βN converges to zero at a carefully chosen rate, then the solution of the distributionally robust optimization problem (5) with ambiguity set PN = Bε

N(βN)( PN) converges to the solution of the original stochastic program (1) as N tends to inﬁnity. The following theorem formalizes this statement.

- Theorem 3.6 (Asymptotic consistency). Suppose that Assumption 3.3 holds and that βN ∈ (0,1), N ∈ N,


satisﬁes ∞N=1 βN < ∞ and limN→∞ εN(βN) = 0.2 Assume also that JN and xN represent the optimal value and an optimizer of the distributionally robust program (5) with ambiguity set PN = Bε

N(βN)( PN), N ∈ N.

- (i) If h(x,ξ) is upper semicontinuous in ξ and there exists L ≥ 0 with |h(x,ξ)| ≤ L(1+ ξ ) for all x ∈ X and ξ ∈ Ξ, then P∞-almost surely we have JN ↓ J as N → ∞ where J is the optimal value of (1).
- (ii) If the assumptions of assertion (i) hold, X is closed, and h(x,ξ) is lower semicontinuous in x for every ξ ∈ Ξ, then any accumulation point of { xN}N∈N is P∞-almost surely an optimal solution for (1).


The proof of Theorem 3.6 will rely on the following technical lemma.

- 1A similar but slightly more complicated inequality also holds for the special case m = 2; see [21, Theorem 2] for details.
- 2A possible choice is βN = exp(−


√

N).

- Lemma 3.7 (Convergence of distributions). If Assumption 3.3 holds and βN ∈ (0,1), N ∈ N, satisﬁes ∞


N(βN)( PN), N ∈ N, where QN may depend on the training data, converges under the Wasserstein metric (and thus weakly) to P almost surely with respect to P∞, that is,

N=1 βN < ∞ and limN→∞ εN(βN) = 0, then, any sequence QN ∈ Bε

P∞ lim

dW P, QN = 0 = 1.

N→∞

Proof. As QN ∈ Bδ

( PN), the triangle inequality for the Wasserstein metric ensures that dW P, QN ≤ dW P, PN + dW PN, QN ≤ dW P, PN + εN(βN).

N

Moreover, Theorem 3.4 implies that PN{dW P, PN ≤ εN(βN)} ≥ 1−βN, and thus we have PN{dW P, QN ≤ 2εN(βN)} ≥ 1 − βN. As ∞N=1 βN < ∞, the Borel-Cantelli Lemma [28, Theorem 2.18] further implies that

P∞ dW P, QN ≤ εN(βN) for all suﬃciently large N = 1.

Finally, as limN↑∞ εN(βN) = 0, we conclude that limN↑∞ dW P, QN = 0 almost surely. Note that convergence with respect to the Wasserstein metric implies weak convergence [10].

- Proof of Theorem 3.6. As xN ∈ X, we have J ≤ EP[h( xN,ξ)]. Moreover, Theorem 3.5 implies that


PN J ≤ EP[h( xN,ξ)] ≤ JN ≥ PN P ∈ Bε

N(βN)( PN) ≥ 1 − βN, for all N ∈ N. As ∞N=1 βN < ∞, the Borel-Cantelli Lemma further implies that

P∞ J ≤ EP[h( xN,ξ)] ≤ JN for all suﬃciently large N = 1.

To prove assertion (i), it thus remains to be shown that limsupN→∞ JN ≤ J with probability 1. As h(x,ξ) is upper semicontinuous and grows at most linearly in ξ, there exists a non-increasing sequence of functions

hk(x,ξ), k ∈ N, such that h(x,ξ) = limk→∞ hk(x,ξ), and hk(x,ξ) is Lipschitz continuous in ξ for any ﬁxed x ∈ X and k ∈ N with Lipschitz constant Lk ≥ 0; see Lemma A.1 in the appendix. Next, choose any δ > 0, ﬁx a δ-optimal decision xδ ∈ X for (1) with EP[h(xδ,ξ)] ≤ J + δ, and for every N ∈ N let QN ∈ PN be a δ-optimal distribution corresponding to xδ with

EQ[h(xδ,ξ)] ≤ EQN

sup

[h(xδ,ξ)] + δ.

Q∈ PN

Then, we have limsup

EQ[h(xδ,ξ)] ≤ limsup

E QN

JN ≤ limsup

sup

[h(xδ,ξ)] + δ

N→∞

N→∞

N→∞

Q∈ PN

E QN

≤ lim

[hk(xδ,ξ)] + δ ≤ lim

limsup

k→∞

N→∞

EP[hk(xδ,ξ)] + Lk dW P, QN + δ

limsup

k→∞

N→∞

EP[hk(xδ,ξ)] + δ, P∞-almost surely

= lim

k→∞

= EP[h(xδ,ξ)] + δ ≤ J + 2δ,

where the second inequality holds because hk(x,ξ) converges from above to h(x,ξ), and the third inequality follows from Theorem 3.2. Moreover, the almost sure equality holds due to Lemma 3.7, and the last equality follows from the Monotone Convergence Theorem [30, Theorem 5.5], which applies because |EP[hk(xδ,ξ)]| < ∞. Indeed, recall that P has an exponentially decaying tail due to Assumption 3.3 and that hk(xδ,ξ) is Lipschitz continuous in ξ. As δ > 0 was chosen arbitrarily, we thus conclude that limsupN→∞ JN ≤ J .

To prove assertion (ii), ﬁx an arbitrary realization of the stochastic process { ξN}N∈N such that J = limN→∞ JN and J ≤ EP[h( xN,ξ)] ≤ JN for all suﬃciently large N. From the proof of assertion (i) we know that these two conditions are satisﬁed P∞-almost surely. Using these assumptions, one easily veriﬁes that

EP[h( xN,ξ)] ≤ lim

liminf

JN = J . (9)

N→∞

N→∞

Next, let x be an accumulation point of the sequence { xN}N∈N, and note that x ∈ X as X is closed. By passing to a subsequence, if necessary, we may assume without loss of generality that x = limN→∞ xN. Thus,

J ≤ EP[h(x ,ξ)] ≤ EP[liminf N→∞

EP[h( xN,ξ)] ≤ J ,

h( xN,ξ)] ≤ liminf N→∞

where the ﬁrst inequality exploits that x ∈ X, the second inequality follows from the lower semicontinuity of h(x,ξ) in x, the third inequality holds due to Fatou’s lemma (which applies because h(x,ξ) grows at most linearly in ξ), and the last inequality follows from (9). Therefore, we have EP[h(x ,ξ)] = J .

In the following we show that all assumptions of Theorem 3.6 are necessary for asymptotic convergence, that is, relaxing any of these conditions can invalidate the convergence result. Example 1 (Necessity of regularity conditions).

- (1) Upper semicontinuity of ξ  → h(x,ξ) in Theorem 3.6 (i): Set Ξ = [0,1], P = δ0 and h(x,ξ) = 1(0,1](ξ), whereby J = 0. As P concentrates unit mass at 0, we have PN = δ0 = P irrespective of N ∈ N. For any ε > 0, the Dirac distribution δε thus resides within the Wasserstein ball Bε( PN). Hence, JN fails to converge to J for ε → 0 because

JN ≥ Eδε

[h(x,ξ)] = h(x,ε) = 1, ∀ε > 0.

- (2) Linear growth of ξ  → h(x,ξ) in Theorem 3.6 (i): Set Ξ = R, P = δ0 and h(x,ξ) = ξ2, which implies that J = 0. Note that for any ρ > ε, the two-point distribution Qρ = (1 − ρε)δ0 + ρεδρ is contained in the Wasserstein ball Bε( PN) of radius ε > 0. Hence, JN fails to converge to J for ε → 0 because

JN ≥ sup ρ>ε

EQρ

[h(x,ξ)] = sup

ρ>ε

ερ = ∞, ∀ε > 0.

- (3) Lower semicontinuity of x  → h(x,ξ) in Theorem 3.6 (ii):


Set X = [0,1] and h(x,ξ) = 1[0.5,1](x), whereby J = 0 irrespective of P. As the objective is independent of ξ, the distributionally robust optimization problem (5) is equivalent to (1). Then,

xN = N2−N1 is a sequence of minimizers for (5) whose accumulation point x = 12 fails to be optimal in (1).

A convergence result akin to Theorem 3.6 for goodness-of-ﬁt-based ambiguity sets is discussed in [7, Section 4]. This result is complementary to Theorem 3.6. Indeed, Theorem 3.6(i) requires h(x,ξ) to be upper semicontinuous in ξ, which is a necessary condition in our setting (see Example 1) that is absent in [7]. Moreover, Theorem 3.6(ii) only requires h(x,ξ) to be lower semicontinuous in x, while [7] asks for equicontinuity of this mapping. This stronger requirement provides a stronger result, that is, the almost sure convergence of supQ∈ P

EQ[h(x,ξ)] to EP[h(x,ξ)] uniformly in x on any compact subset of X.

N

Theorems 3.5 and 3.6 indicate that a careful a priori design of the Wasserstein ball results in attractive ﬁnite sample and asymptotic guarantees for the distributionally robust solutions. In practice, however, setting the Wasserstein radius to εN(β) yields over-conservative solutions for the following reasons:

- • Even though the constants c1 and c2 in (8) can be computed based on the proof of [21, Theorem 2],

the resulting Wasserstein ball is larger than necessary, i.e., P ∈/ Bε

N(β)( PN) with probability β.

- • Even if P ∈/ Bε

N(β)( PN), the optimal value JN of (5) may still provide an upper bound on J .

- • The formula for εN(β) in (8) is independent of the training data. Allowing for random Wasserstein radii, however, results in a more eﬃcient use of the available training data.


While Theorems 3.5 and 3.6 provide strong theoretical justiﬁcation for using Wasserstein ambiguity sets, in practice, it is prudent to calibrate the Wasserstein radius via bootstrapping or cross-validation instead of using the conservative a priori bound εN(β); see Section 7.2 for further details. A similar approach has been advocated in [7] to determine the sizes of ambiguity sets that are constructed via goodness-of-ﬁt tests.

So far we have seen that the Wasserstein metric allows us to construct ambiguity sets with favorable asymptotic and ﬁnite sample guarantees. In the remainder of the paper we will further demonstrate that the distributionally robust optimization problem (5) with a Wasserstein ambiguity set (6) is not signiﬁcantly harder to solve than the corresponding SAA problem (4).

4. Solving Worst-Case Expectation Problems

We now demonstrate that the inner worst-case expectation problem in (5) over the Wasserstein ambiguity set (6) can be reformulated as a ﬁnite convex program for many loss functions h(x,ξ) of practical interest. For ease of notation, throughout this section we suppress the dependence on the decision variable x. Thus, we examine a generic worst-case expectation problem

EQ (ξ) (10)

sup

Q∈Bε( PN)

involving a decision-independent loss function (ξ) := maxk≤K k(ξ), which is deﬁned as the pointwise maximum of more elementary measurable functions k : Rm → R, k ≤ K. The focus on loss functions representable as pointwise maxima is non-restrictive unless we impose some structure on the functions k. Many tractability results in the remainder of this paper are predicated on the following convexity assumption.

- Assumption 4.1 (Convexity). The uncertainty set Ξ ⊆ Rm is convex and closed, and the negative constituent


functions − k are proper, convex, and lower semicontinuous for all k ≤ K. Moreover, we assume that k is not identically −∞ on Ξ for all ≤ K.

Assumption 4.1 essentially stipulates that (ξ) can be written as a maximum of concave functions. As we will showcase in Section 5, this mild restriction does not sacriﬁce much modeling power. Moreover, generalizations of this setting will be discussed in Section 6. We proceed as follows. Subsection 4.1 addresses the reduction of (10) to a ﬁnite convex program, while Subsection 4.2 describes a technique for constructing worst-case distributions.

### 4.1. Reduction to a Finite Convex Program

The worst-case expectation problem (10) constitutes an inﬁnite-dimensional optimization problem over probability distributions and thus appears to be intractable. However, we will now demonstrate that (10) can be re-expressed as a ﬁnite-dimensional convex program by leveraging tools from robust optimization.

- Theorem 4.2 (Convex reduction). If the convexity Assumption 4.1 holds, then for any ε ≥ 0 the worst-case


expectation (10) equals the optimal value of the ﬁnite convex program

 

N

λε + N1

si s.t. [− k]∗(zik − νik) + σΞ(νik) − zik, ξi ≤ si ∀i ≤ N, ∀k ≤ K zik ∗ ≤ λ ∀i ≤ N, ∀k ≤ K.

inf

λ,si,zik,νik

i=1

(11)



Recall that [− k]∗(zik − νik) denotes the conjugate of − k evaluated at zik − νik and zik ∗ the dual norm of zik. Moreover, χΞ represents the characteristic function of Ξ and σΞ its conjugate, that is, the support function of Ξ.

- Proof of Theorem 4.2. By using Deﬁnition 3.1 we can re-express the worst-case expectation (10) as


 

sup Π,Q Ξ (ξ)Q(dξ)

ξ − ξ Π(dξ,dξ ) ≤ ε Π is a joint distribution of ξ and ξ with marginals Q and PN, respectively

s.t. Ξ

EQ (ξ) =

2

sup

Q∈Bε( PN)



 

N

1 N

Ξ (ξ)Qi(dξ)

sup

Qi∈M(Ξ)

i=1

=

N



s.t. N1

Ξ ξ − ξi Qi(dξ) ≤ ε.

i=1

The second equality follows from the law of total probability, which asserts that any joint probability distribution Π of ξ and ξ can be constructed from the marginal distribution PN of ξ and the conditional distributions Qi of ξ given ξ = ξi, i ≤ N, that is, we may write Π = N1 Ni=1 δ ξ

⊗Qi. The resulting optimization problem represents a generalized moment problem in the distributions Qi, i ≤ N. Using a standard duality argument, we obtain

i

N

N

1 N

1 N

EQ (ξ) = sup

(ξ)Qi(dξ) + λ ε −

ξ − ξi Qi(dξ)

sup

inf

λ≥0

Qi∈M(Ξ)

Q∈Bε( PN)

i=1 Ξ

i=1 Ξ

N

1 N

(ξ) − λ ξ − ξi Qi(dξ) (12a)

≤ inf

sup

λε +

λ≥0

Qi∈M(Ξ)

i=1 Ξ

N

1 N

(ξ) − λ ξ − ξi , (12b)

sup

= inf

λε +

λ≥0

ξ∈Ξ

i=1

where (12a) follows from the max-min inequality, and (12b) follows from the fact that M(Ξ) contains all the Dirac distributions supported on Ξ. Introducing epigraphical auxiliary variables si, i ≤ N, allows us to reformulate (12b) as

 

N

λε + N1

si s.t. sup

inf

λ,si

i=1

(12c)

(ξ) − λ ξ − ξi ≤ si ∀i ≤ N λ ≥ 0

ξ∈Ξ



 

N

λε + N1

si s.t. sup

inf

λ,si

i=1

(12d)

=

zik,ξ − ξi ≤ si ∀i ≤ N, ∀k ≤ K λ ≥ 0

k(ξ) − max

zik ∗≤λ

ξ∈Ξ



 

N

λε + N1

si s.t. min

inf

λ,si

i=1

≤

(12e)

k(ξ) − zik,ξ − ξi ≤ si ∀i ≤ N, ∀k ≤ K λ ≥ 0.

sup

zik ∗≤λ

ξ∈Ξ



Equality (12d) exploits the deﬁnition of the dual norm and the decomposability of (ξ) into its constituents

k(ξ), k ≤ K. Interchanging the maximization over zik with the minus sign (thereby converting the maximization to a minimization) and then with the maximization over ξ leads to a restriction of the feasible set of (12d). The resulting upper bound (12e) can be re-expressed as

 

N

λε + N1

si s.t. sup

inf

λ,si,zik

i=1

k(ξ) − zik,ξ + zik, ξi ≤ si ∀i ≤ N, ∀k ≤ K zik ∗ ≤ λ ∀i ≤ N, ∀k ≤ K

ξ∈Ξ



 

N

λε + N1

si s.t. [− k + χΞ]∗(zik) − zik, ξi ≤ si ∀i ≤ N, ∀k ≤ K zik ∗ ≤ λ ∀i ≤ N, ∀k ≤ K,

inf

λ,si,zik

i=1

(12f)

=



where (12f) follows from the deﬁnition of conjugacy, our conventions of extended arithmetic, and the substitution of zik with −zik. Note that (12f) is already a ﬁnite convex program.

Next, we show that Assumption 4.1 reduces the inequalities (12a) and (12e) to equalities. Under Assumption 4.1, the inequality (12a) is in fact an equality for any ε > 0 by virtue of an extended version of a well-known strong duality result for moment problems [44, Proposition 3.4]. One can show that (12a) continues to hold as an equality even for ε = 0, in which case the Wasserstein ambiguity set (6) reduces to the singleton { PN}, while (10) reduces to the sample average N1 Ni=1 ( ξi). Indeed, for ε = 0 the variable λ in (12b) can be increased indeﬁnitely at no penalty. As (ξ) constitutes a pointwise maximum of upper semicontinuous concave functions, an elementary but tedious argument shows that (12b) converges to the sample average N1 Ni=1 ( ξi) as λ tends to inﬁnity.

The inequality (12e) also reduces to an equality under Assumption 4.1 thanks to the classical minimax theorem [4, Proposition 5.5.4], which applies because the set {zik ∈ Rm : zik ∗ ≤ λ} is compact for any ﬁnite λ ≥ 0. Thus, the optimal values of (10) and (12f) coincide.

Assumption 4.1 further implies that the function − k + χΞ is proper, convex and lower semicontinuous. Properness holds because k is not identically −∞ on Ξ. By [42, Theorem 11.23(a), p. 493], its conjugate essentially coincides with the epi-addition (also known as inf-convolution) of the conjugates of the functions − k and σΞ. Thus,

[− k + χΞ]∗(zik) = inf νik

[− k]∗(zik − νik) + [χΞ]∗(νik)

[− k]∗(zik − νik) + σΞ(νik) ,

= cl inf

νik

where cl[·] denotes the closure operator that maps any function to its largest lower semicontinuous minorant. As cl[f(ξ)] ≤ 0 if and only if f(ξ) ≤ 0 for any function f, we may conclude that (12f) is indeed equivalent to (11) under Assumption 4.1.

Note that the semi-inﬁnite inequality in (12c) generalizes the nonlinear uncertain constraints studied in [1] because it involves an additional norm term and as the loss function (ξ) is not necessarily concave under

Assumption 4.1. As in [1], however, the semi-inﬁnite constraint admits a robust counterpart that involves the conjugate of the loss function and the support function of the uncertainty set.

From the proof of Theorem 4.2 it is immediately clear that the worst-case expectation (10) is conservatively approximated by the optimal value of the ﬁnite convex program (12f) even if Assumption 4.1 fails to hold. In this case the sum − k + χΞ in (12f) must be evaluated under our conventions of extended arithmetics, whereby ∞ − ∞ = ∞. These observations are formalized in the following corollary.

Corollary 4.3 (Approximate convex reduction). For any ε ≥ 0, the worst-case expectation (10) is smaller or equal to the optimal value of the ﬁnite convex program (12f).

### 4.2. Extremal Distributions

Stress test experiments are instrumental to assess the quality of candidate decisions in stochastic optimization. Meaningful stress tests require a good understanding of the extremal distributions from within the Wasserstein ball that achieve the worst-case expectation (10) for various loss functions. We now show that such extremal distributions can be constructed systematically from the solution of a convex program akin to (11).

Theorem 4.4 (Worst-case distributions). If Assumption 4.1 holds, then the worst-case expectation (10) coincides with the optimal value of the ﬁnite convex program



N

K

αik k ξi − q

1 N

sup

ik αik

αik,qik

i=1

k=1

N

K

s.t. N1



qik ≤ ε K k=1

i=1

k=1

(13)

αik = 1 ∀i ≤ N

αik ≥ 0 ∀i ≤ N, ∀k ≤ K ξi − q



αik ∈ Ξ ∀i ≤ N, ∀k ≤ K

ik

irrespective of ε ≥ 0. Let αik(r),qik(r) r∈N be a sequence of feasible decisions whose objective values converge to the supremum of (13). Then, the discrete probability distributions

K

N

qik(r) αik(r)

1 N

Qr :=

ik(r) with ξik(r) := ξi −

αik(r)δξ

i=1

k=1

belong to the Wasserstein ball Bε( PN) and attain the supremum of (10) asymptotically, i.e.,

EQ (ξ) = lim

EQr

sup

r→∞

Q∈Bε( PN)

N

1 N

(ξ) = lim

k→∞

i=1

K

αik(r) ξik(r) .

k=1

We highlight that all fractions in (13) must again be evaluated under our conventions of extended arithmetics. Speciﬁcally, if αik = 0 and qik = 0, then qik/αik has at least one component equal to +∞ or −∞, which implies that ξi −qik/αik ∈/ Ξ. In contrast, if αik = 0 and qik = 0, then ξi −qik/αik = ξi ∈ Ξ. Moreover, the ik-th component in the objective function of (13) evaluates to 0 whenever αik = 0 regardless of qik.

The proof of Theorem 4.4 is based on the following technical lemma.

- Lemma 4.5. Deﬁne F : Rm × R+ → R through F(q,α) = infz∈Rm z,q − α ξ + αf∗(z) for some proper, convex, and lower semicontinuous function f : Rm → R and reference point ξ ∈ Rm. Then, F coincides with


the (extended) perspective function of the mapping q  → −f( ξ − q), that is,

F(q,α) = −αf ξ − q/α if α > 0, −χ{0}(q) if α = 0.

Proof. By construction, we have F(q,0) = infz∈Rm z,q = −χ{0}(q). For α > 0, on the other hand, the deﬁnition of conjugacy implies that

F(q,α) = −[αf∗]∗(α ξ − q) = −α[f∗]∗ ξ − q/α .

The claim then follows because [f∗]∗ = f for any proper, convex, and lower semicontinuous function f [4, Proposition 1.6.1(c)]. Additional information on perspective functions can be found in [12, Section 2.2.3, p. 39].

Proof of Theorem 4.4. By Theorem 4.2, which applies under Assumption 4.1, the worst-case expectation (10) coincides with the optimal value of the convex program (11). From the proof of Theorem 4.2 we know that (11) is equivalent to (12f). The Lagrangian dual of (12f) is given by

 

N

K

si N +

βik zik ∗ − λ + αik [− k + χΞ]∗(zik) − zik, ξi − si s.t. αik ≥ 0 ∀i ≤ N, ∀k ≤ K

sup

inf

λε +

λ,si,zik

βik,αik

i=1

k=1



βik ≥ 0 ∀i ≤ N, ∀k ≤ K,

where the products of dual variables and constraint functions in the objective are evaluated under the standard convention 0·∞ = 0. Strong duality holds since the function [− k + χΞ]∗ is proper, convex, and lower semicontinuous under Assumption 4.1 and because this function appears in a constraint of (12f) whose righthand side is a free decision variable. By explicitly carrying out the minimization over λ and si, one can show that the above dual problem is equivalent to



N

K

βik zik ∗+αik[− k + χΞ]∗(zik) − αik zik, ξi

sup

##### inf

zik

βik,αik

i=1

k=1

N

K



s.t.

βik = ε K k=1

i=1

k=1

αik = N1 ∀i ≤ N αik ≥ 0 ∀i ≤ N, ∀k ≤ K βik ≥ 0 ∀i ≤ N, ∀k ≤ K.



By using the deﬁnition of the dual norm, (14a) can be re-expressed as 

N

K

zik,qik +αik[− k + χΞ]∗(zik) − αik zik, ξi

sup

##### inf

max

zik

qik ≤βik

βik,αik

i=1

k=1

N

K



s.t.

βik = ε K k=1

i=1

k=1

αik = N1 ∀i ≤ N

αik ≥ 0 ∀i ≤ N, ∀k ≤ K βik ≥ 0 ∀i ≤ N, ∀k ≤ K



(14a)

(14b)



N

K

zik,qik +αik[− k + χΞ]∗(zik) − αik zik, ξi

sup

max

inf

zik

qik ≤βik

βik,αik

i=1

k=1

K

N



βik = ε K k=1

s.t.

i=1

k=1

=

(14c)

αik = N1 ∀i ≤ N αik ≥ 0 ∀i ≤ N, ∀k ≤ K βik ≥ 0 ∀i ≤ N, ∀k ≤ K,



where (14c) follows from the classical minimax theorem and the fact that the qik variables range over a non-empty and compact feasible set for any ﬁnite ε; see [4, Proposition 5.5.4]. Eliminating the βik variables and using Lemma 4.5 allows us to reformulate (14c) as



N

K

zik,qik − αik ξi +αik[− k + χΞ]∗(zik) s.t.

sup

##### inf

zik

αik,qik

i=1

k=1



N

K

qik ≤ ε K k=1

(14d)

i=1

k=1

αik = N1 ∀i ≤ N αik ≥ 0 ∀i ≤ N, ∀k ≤ K





N

K

##### αik +χΞ ξi − q

−αik − k ξi − q

αik 1{α

ik>0} − χ{0}(qik)1{α

sup

ik

ik

ik=0}

αik,qik

i=1

k=1



N

K

qik ≤ ε K k=1

s.t.

(14e)

=

i=1

k=1

αik = N1 ∀i ≤ N αik ≥ 0 ∀i ≤ N, ∀k ≤ K.



Our conventions of extended arithmetics imply that the ik-th term in the objective function of problem (14e) simpliﬁes to

qik αik − χΞ ξi −

qik αik

αik k ξi −

. (14f)

Indeed, for αik > 0, this identity trivially holds. For αik = 0, on the other hand, the ik-th objective term in (14e) reduces to −χ{0}(qik). Moreover, the ﬁrst term in (14f) vanishes whenever αik = 0 regardless of qik, and the second term in (14f) evaluates to 0 if qik = 0 (as 0/0 = 0 and ξi ∈ Ξ) and to −∞ if qik = 0 (as qik/0 has at least one inﬁnite component, implying that ξi +qik/0 ∈/ Ξ). Therefore, (14f) also reduces to −χ{0}(qik) when αik = 0. This proves that the ik-th objective term in (14e) coincides with (14f). Substituting (14f) into (14e) and re-expressing −χΞ ξi − q

αik in terms of an explicit hard constraint yields 

ik

N

K

αik k ξi − q

sup

ik αik

αik,qik

i=1

k=1

N

K



qik ≤ ε K k=1

s.t.

i=1

k=1

(14g)

αik = N1 ∀i ≤ N αik ≥ 0 ∀i ≤ N, ∀k ≤ K ξi − q



αik ∈ Ξ ∀i ≤ N, ∀k ≤ K.

ik

Finally, replacing αik,qik with N1 αik,qik shows that (14g) is equivalent to (13). This completes the ﬁrst part of the proof.

![image 1](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile1.png>)

|![image 2](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile2.png>)|![image 3](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile3.png>)<br><br>![image 4](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile4.png>)|
|---|---|
|![image 5](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile5.png>)|![image 6](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile6.png>)<br><br>![image 7](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile7.png>)|


Figure 1. Example of a worst-case expectation problem without a worst-case distribution

As for the second claim, let {αik(r),qik(r)}r∈N be a sequence of feasible solutions that attains the supremum in (13), and set ξik(r) := ξi − q

ik(r)

αik(r) ∈ Ξ. Then, the discrete distribution

K

N

1 N

Πr :=

αik(r)δ ξ

ik(r), ξi

i=1

k=1

has the distribution Qr deﬁned in the theorem statement and the empirical distribution PN as marginals. By the deﬁnition of the Wasserstein metric, Πr represents a feasible mass transportation plan that provides an upper bound on the distance between PN and Qr; see Deﬁnition 3.1. Thus, we have

dW Qr, PN ≤

Ξ2

1 N

ξ − ξ Πr(dξ,dξ ) =

N

i=1

K

N

K

1 N

αik(r) ξik(r) − ξi =

i=1

k=1

k=1

qik(r) ≤ ε,

where the last inequality follows readily from the feasibility of qik(r) in (13). We conclude that

EQ (ξ) ≥ limsup

EQr

sup

k→∞

Q∈Bε( PN)

1 N

≥ limsup

k→∞

K

N

1 N

(ξ) = limsup

αik(r) ξik(r)

k→∞

i=1

k=1

K

N

EQ (ξ) ,

αik(r) k ξik(r) = sup

Q∈Bε( PN)

i=1

k=1

where the ﬁrst inequality holds as Qr ∈ Bε( PN) for all k ∈ N, and the second inequality uses the trivial estimate ≥ k for all k ≤ K. The last equality follows from the construction of αik(r) and ξik(r) and the fact that (13) coincides with the worst-case expectation (10).

In the rest of this section we discuss some notable properties of the convex program (13).

In the ambiguity-free limit, that is, when the radius of the Wasserstein ball is set to zero, then the optimal value of the convex program (13) reduces to the expected loss under the empirical distribution. Indeed, for ε = 0 all qik variables are forced to zero, and αik enters the objective only through Kk=1 αik = N1 . Thus, the objective function of (13) simpliﬁes to E PN

[ (ξ)].

We further emphasize that it is not possible to guarantee the existence of a worst-case distribution that attains the supremum in (10). In general, as shown in Theorem 4.4, we can only construct a sequence of distributions that attains the supremum asymptotically. The following example discusses an instance of (10) that admits no worst-case distribution.

Example 2 (Non-existence of a worst-case distribution). Assume that Ξ = R, N = 1, ξ1 = 0, K = 2, 1(ξ) = 0 and 2(ξ) = ξ − 1. In this case we have PN = δ{0}, and problem (13) reduces to

 

−q12 − α12

sup

α1j,q1j

s.t. |q11| + |q12| ≤ ε α11 + α12 = 1 α11 ≥ 0, α12 ≥ 0.

EQ (ξ) =

sup

Q∈Bε(δ0)



The supremum on the right-hand side amounts to ε and is attained, for instance, by the sequence α11(r) = 1 − k1, α12(r) = k1, q11(r) = 0, q12(r) = −ε for k ∈ N. Deﬁne

Qr = α11(r)δξ

12(r), with ξ11(r) = ξ1 − q

11(r) + α12(r)δξ

11(r)

α11(r) = 0, and ξ12(r) = ξ1 − q

12(r)

α12(r) = εk. By Theorem 4.4, the two-point distributions Qr reside within the Wasserstein ball of radius ε around δ0 and asymptotically attain the supremum in the worst-case expectation problem. However, this sequence has no weak limit as ξ12(r) = εk tends to inﬁnity,

- see Figure 1. In fact, no single distribution can attain the worst-case expectation. Assume for the sake of contradiction that there exists Q ∈ Bε(δ0) with EQ [ (ξ)] = ε. Then, we ﬁnd ε = EQ [ (ξ)] < EQ [|ξ|] ≤ ε, where the strict inequality follows from the relation (ξ) < |ξ| for all ξ = 0 and the observation that Q = δ0, while the second inequality follows from Theorem 3.2. Thus, Q does not exist.

The existence of a worst-case distribution can, however, be guaranteed in some special cases.

- Corollary 4.6 (Existence of a worst-case distribution). Suppose that Assumption 4.1 holds. If the uncertainty set Ξ is compact or the loss function is concave (i.e., K = 1), then the sequence {αik(r),ξik(r)}r∈N constructed in Theorem 4.4 has an accumulation point {α ik,ξ ik}, and


Q :=

1 N

N

i=1

K

k=1

α ikδξ

ik

is a worst-case distribution achieving the supremum in (10).

Proof. If Ξ is compact, then the sequence {αik(r),ξik(r)}r∈N has a converging subsequence with limit {α ik,ξ ik}.

Similarly, if K = 1, then αi1 = 1 for all i ≤ N, in which case (13) reduces to a convex optimization problem with an upper semicontinuous objective function over a compact feasible set. Hence, its supremum is attained

at a point {α ik,ξ ik}. In both cases, Theorem 4.4 guarantees that the distribution Q implied by {α ik,ξ ik} achieves the supremum in (10).

The worst-case distribution of Corollary 4.6 is discrete, and its atoms ξ ik reside in the neighborhood of the given data points ξi. By the constraints of problem (13), the probability-weighted cumulative distance between the atoms and the respective data points amounts to

N

i=1

K

k=1

αik ξ ik − ξi =

N

i=1

K

k=1

qik ≤ ε,

which is bounded above by the radius of the Wasserstein ball. The fact that the worst-case distribution Q (if it exists) is supported outside of ΞN is a key feature distinguishing the Wasserstein ball from the ambiguity sets induced by other probability metrics such as the total variation distance or the Kullback-Leibler divergence;

- see Figure 2. Thus, the worst-case expectation criterion based on Wasserstein balls advocated in this paper should appeal to decision makers who wish to immunize their optimization problems against perturbations of the data points.


| | |
|---|---|
| |![image 8](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile8.png>)<br><br>|


|![image 9](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile9.png>)<br><br>| |
|---|---|
| |![image 10](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile10.png>)<br><br>|


![image 11](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile11.png>)

![image 12](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile12.png>)

![image 13](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile13.png>)

![image 14](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile14.png>)

![image 15](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile15.png>)

![image 16](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile16.png>)

![image 17](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile17.png>)

![image 18](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile18.png>)

![image 19](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile19.png>)

![image 20](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile20.png>)

![image 21](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile21.png>)

![image 22](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile22.png>)

![image 23](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile23.png>)

![image 24](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile24.png>)

![image 25](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile25.png>)

(a) Empirical distribution on a training dataset with N = 2 samples

(b) A representative discrete distribution in the total variation or the KullbackLeiber ball

(c) A representative discrete distribution in the Wasserstein ball

Figure 2. Representative distributions in balls centered at PN induced by diﬀerent metrics

- Remark 4.7 (Weak coupling). We highlight that the convex program (13) is amenable to decomposition and parallelization techniques as the decision variables associated with diﬀerent sample points are only coupled through the norm constraint. We expect the resulting scenario decomposition to oﬀer a substantial speedup of the solution times for problems involving large datasets. Eﬃcient decomposition algorithms that could be used for solving the convex program (13) are described, for example, in [35] and [5, Chapter 4].


5. Special Loss Functions

We now demonstrate that the convex optimization problems (11) and (13) reduce to computationally tractable conic programs for several loss functions of practical interest.

### 5.1. Piecewise Aﬃne Loss Functions

We ﬁrst investigate the worst-case expectations of convex and concave piecewise aﬃne loss functions, which arise, for example, in option pricing [8], risk management [34] and in generic two-stage stochastic programming [6]. Moreover, piecewise aﬃne functions frequently serve as approximations of smooth convex or concave loss functions.

- Corollary 5.1 (Piecewise aﬃne loss functions). Suppose that the uncertainty set is a polytope, that is, Ξ = {ξ ∈ Rm : Cξ ≤ d} where C is a matrix and d a vector of appropriate dimensions. Moreover, consider the aﬃne functions ak(ξ) := ak,ξ + bk for all k ≤ K.


- (i) If (ξ) = maxk≤K ak(ξ), then the worst-case expectation (10) evaluates to  


N

λε + N1

si s.t. bk + ak, ξi + γik,d − C ξi ≤ si ∀i ≤ N, ∀k ≤ K

inf

λ,si,γik

i=1

C γik − ak ∗ ≤ λ ∀i ≤ N, ∀k ≤ K γik ≥ 0 ∀i ≤ N, ∀k ≤ K.



(15a)

- (ii) If (ξ) = mink≤K ak(ξ), then the worst-case expectation (10) evaluates to 


N

λε + N1

si

inf

λ,si,γi,θi

i=1

s.t. θi,b + A ξi + γi,d − C ξi ≤ si ∀i ≤ N C γi − A θi ∗ ≤ λ ∀i ≤ N θi,e = 1 ∀i ≤ N



(15b)

γi ≥ 0 ∀i ≤ N θi ≥ 0 ∀i ≤ N,



where A is the matrix with rows a k, k ≤ K, b is the column vector with entries bk, k ≤ K, and e is the vector of all ones.

Proof. Assertion (i) is an immediate consequence of Theorem 4.2, which applies because (x) is the pointwise maximum of the aﬃne functions k(ξ) = ak(ξ), k ≤ K, and thus Assumption 4.1 holds for J = K. By deﬁnition of the conjugacy operator, we have

bk if z = −ak, ∞ else,

[− k]∗(z) = [−ak]∗(z) = sup

z,ξ + ak,ξ + bk =

ξ

and

 

ν,ξ s.t. Cξ ≤ d

sup

γ,d s.t. C γ = ν,

inf

γ≥0

=

σΞ(ν) =

ξ



where the last equality follows from strong duality, which holds as the uncertainty set is non-empty. Assertion (i) then follows by substituting the above expressions into (11).

Assertion (ii) also follows directly from Theorem 4.2 because (ξ) = 1(ξ) = mink≤K aj(ξ) is concave and thus satisﬁes Assumption 4.1 for J = 1. In this setting, we ﬁnd

 

 

θ,b s.t. A θ = −z

inf

z,ξ + τ s.t. Aξ + b ≥ τe

sup

θ≥0

[− ]∗(z) = sup

ak,ξ + bk =

=

z,ξ + min

ξ,τ



k≤K



ξ

θ,e = 1

where the last equality follows again from strong linear programming duality, which holds since the primal maximization problem is feasible. Assertion (ii) then follows by substituting [− ]∗ as well as the formula for σΞ from the proof of assertion (i) into (11).

As a consistency check, we ascertain that in the ambiguity-free limit, the optimal value of (15a) reduces to the expectation of maxk≤K ak(ξ) under the empirical distribution. Indeed, for ε = 0, the variable λ can be set to any positive value at no penalty. For this reason and because all training samples must belong to the uncertainty set (i.e., d − C ξi ≥ 0 for all i ≤ N), it is optimal to set γik = 0. This in turn implies that si = maxk≤K ak( ξi) at optimality, in which case N1 Ni=1 si represents the sample average of the convex loss function at hand.

An analogous argument shows that, for ε = 0, the optimal value of (15b) reduces to the expectation of mink≤K ak(ξ) under the empirical distribution. As before, λ can be increased at no penalty. Thus, we conclude that γi = 0 and

si = min θi≥0

θi,b + A ξi : θi,e = 1 = min k≤K

ak( ξi)

at optimality, in which case N1 Ni=1 si is the sample average of the given concave loss function.

### 5.2. Uncertainty Quantiﬁcation

A problem of great practical interest is to ascertain whether a physical, economic or engineering system with an uncertain state ξ satisﬁes a number of safety constraints with high probability. In the following we denote by A the set of states in which the system is safe. Our goal is to quantify the probability of the event ξ ∈ A (ξ ∈/ A) under an ambiguous state distribution that is only indirectly observable through a ﬁnite training dataset. More precisely, we aim to calculate the worst-case probability of the system being unsafe, i.e.,

Q[ξ ∈/ A], (16a)

sup

Q∈Bε( PN)

as well as the best-case probability of the system being safe, that is,

Q[ξ ∈ A]. (16b)

sup

Q∈Bε( PN)

- Remark 5.2 (Data-dependent sets). The set A may even depend on the samples ξ1,..., ξN, in which case A is renamed as A. If the Wasserstein radius ε is set to εN(β), then we have P ∈ Bε( PN) with probability 1−β, implying that (16a) and (16b) still provide 1 − β conﬁdence bounds on P[ξ ∈/ A] and P[ξ ∈ A], respectively.


- Corollary 5.3 (Uncertainty quantiﬁcation). Suppose that the uncertainty set is a polytope of the form Ξ = {ξ ∈ Rm : Cξ ≤ d} as in Corollary 5.1.


- (i) If A = {ξ ∈ Rm : Aξ < b} is an open polytope and the halfspace ξ : ak,ξ ≥ bk has a nonempty intersection with Ξ for any k ≤ K, where ak is the k-th row of the matrix A and bk is the k-th entry of the vector b, then the worst-case probability (16a) is given by







inf

λ,si,γik,θik

λε + N1

N

i=1

si s.t. 1 − θik bk − ak, ξi + γik,d − C ξi ≤ si ∀i ≤ N, ∀k ≤ K

akθik − C γik ∗ ≤ λ ∀i ≤ N, ∀k ≤ K γik ≥ 0 ∀i ≤ N, ∀k ≤ K θik ≥ 0 ∀i ≤ N, ∀k ≤ K si ≥ 0 ∀i ≤ N.

(17a)

- (ii) If A = {ξ ∈ Rm : Aξ ≤ b} is a closed polytope that has a nonempty intersection with Ξ, then the best-case probability (16b) is given by




N

λε + N1

si s.t. 1 + θi,b − A ξi + γi,d − C ξi ≤ si ∀i ≤ N

inf

λ,si,γi,θi

i=1



A θi + C γi ∗ ≤ λ ∀i ≤ N γi ≥ 0 ∀i ≤ N θi ≥ 0 ∀i ≤ N si ≥ 0 ∀i ≤ N.

(17b)



Proof. The uncertainty quantiﬁcation problems (16a) and (16b) can be interpreted as instances of (10) with loss functions = 1 − 1A and = 1A, respectively. In order to be able to apply Theorem 4.2, we should represent these loss functions as ﬁnite maxima of concave functions as shown in Figure 3.

![image 26](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile26.png>)

![image 27](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile27.png>)

![image 28](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile28.png>)

![image 29](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile29.png>)

![image 30](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile30.png>)

![image 31](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile31.png>)

![image 32](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile32.png>)

![image 33](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile33.png>)

![image 34](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile34.png>)

![image 35](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile35.png>)

![image 36](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile36.png>)

![image 37](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile37.png>)

![image 38](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile38.png>)

![image 39](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile39.png>)

![image 40](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile40.png>)

![image 41](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile41.png>)

![image 42](<2015-esfahani-data-driven-distributionally-robust-optimizati_images/imageFile42.png>)

(a) Indicator function of the unsafe set (b) Indicator function of the safe set

Figure 3. Representing the indicator function of a convex set and its complement as a pointwise maximum of concave functions

Formally, assertion (i) follows from Theorem 4.2 for a loss function with K +1 pieces if we use the following deﬁnitions. For every k ≤ K we deﬁne

1 if ak,ξ ≥ bk, −∞ otherwise.

k(ξ) =

Moreover, we deﬁne K+1(ξ) = 0. As illustrated in Figure 3(a), we thus have (ξ) = maxk≤K+1 k(ξ) = 1 − 1A(ξ) and

EQ [ (ξ)].

Q[ξ ∈/ A] = sup

sup

Q∈Bε( PN)

Q∈Bε( PN)

Assumption 4.1 holds due to the postulated properties of A and Ξ. In order to apply Theorem 4.2, we must determine the support function σΞ, which is already known from Corollary 5.1, as well as the conjugate functions of − k, k ≤ K + 1. A standard duality argument yields

 

sup

z,ξ + 1 s.t. ak,ξ ≥ bk

1 − bkθ s.t. akθ = −z,

inf

[− k]∗(z) =

θ≥0

=

ξ



for all k ≤ K. Moreover, we have [− K+1]∗ = 0 if ξ = 0; = ∞ otherwise. Assertion (ii) then follows by substituting the formulas for [− k]∗, k ≤ K + 1, and σΞ into (11).

Assertion (ii) follows from Theorem 4.2 by setting K = 2, 1(ξ) = 1 − χA(ξ) and 2(ξ) = 0. As illustrated in Figure 3(b), this implies that (ξ) = max{ 1(ξ), 2(ξ)} = 1A(ξ) and

EQ [ (ξ)].

Q[ξ ∈ A] = sup

sup

Q∈Bε( PN)

Q∈Bε( PN)

Assumption 4.1 holds by our assumptions on A and Ξ. In order to apply Theorem 4.2, we thus have to determine the support function σΞ, which was already calculated in Corollary 5.1, and the conjugate functions of − 1 and − 2. By the deﬁnition of the conjugacy operator, we ﬁnd

 

sup

z,ξ + 1 s.t. Aξ ≤ b

θ,b + 1 s.t. A θ = z

inf

[− 1]∗(z) = sup ξ∈A

θk≥0

z,ξ + 1 =

=

ξ



where the last equality follows from strong linear programming duality, which holds as the safe set is nonempty. Similarly, we ﬁnd [− 2]∗ = 0 if ξ = 0; = ∞ otherwise. Assertion (ii) then follows by substituting the above expressions into (11).

In the ambiguity-free limit (i.e., for ε = 0) the optimal value of (17a) reduces to the fraction of training samples residing outside of the open polytope A = {ξ : Aξ < b}. Indeed, in this case the variable λ can be set to any positive value at no penalty. For this reason and because all training samples belong to the

uncertainty set (i.e., d − C ξi ≥ 0 for all i ≤ N), it is optimal to set γik = 0. If the i-th training sample belongs to A (i.e., bk − ak, ξi > 0 for all k ≤ K), then θik ≥ 1/(bk − ak, ξi ) for all k ≤ K and si = 0 at optimality. Conversely, if the i-th training sample belongs to the complement of A, (i.e., bk − ak, ξi ≤ 0 for some k ≤ K), then θik = 0 for some k ≤ K and si = 1 at optimality. Thus, Ni=1 si coincides with the number of training samples outside of A at optimality. An analogous argument shows that, for ε = 0, the optimal value of (17b) reduces to the fraction of training samples residing inside of the closed polytope A = {ξ : Aξ ≤ b}.

### 5.3. Two-Stage Stochastic Programming

A major challenge in linear two-stage stochastic programming is to evaluate the expected recourse costs, which are only implicitly deﬁned as the optimal value of a linear program whose coeﬃcients depend linearly on the uncertain problem parameters [46, Section 2.1]. The following corollary shows how we can evaluate the worst-case expectation of the recourse costs with respect to an ambiguous parameter distribution that is only observable through a ﬁnite training dataset. For ease of notation and without loss of generality, we suppress here any dependence on the ﬁrst-stage decisions.

- Corollary 5.4 (Two-stage stochastic programming). Suppose that the uncertainty set is a polytope of the form Ξ = {ξ ∈ Rm : Cξ ≤ d} as in Corollaries 5.1 and 5.3.


- (i) If (ξ) = infy y,Qξ : Wy ≥ h is the optimal value of a parametric linear program with objective uncertainty, and if the feasible set {y : Wy ≥ h} is non-empty and compact, then the worst-case expectation (10) is given by







inf

λ,si,γi,yi

λε + N1

N

i=1

si

s.t. yi,Q ξi + γi,d − C ξi ≤ si ∀i ≤ N Wyi ≥ h ∀i ≤ N

Q yi − C γi ∗ ≤ λ ∀i ≤ N γi ≥ 0 ∀i ≤ N.

(18a)

- (ii) If (ξ) = infy q,y : Wy ≥ Hξ + h is the optimal value of a parametric linear program with righthand side uncertainty, and if the dual feasible set {θ ≥ 0 : W θ = q} is non-empty and compact with


vertices vk, k ≤ K, then the worst-case expectation (10) is given by

 

N

λε + N1

si s.t. vk,h + H vk, ξi + γik,d − C ξi ≤ si ∀i ≤ N, ∀k ≤ K

inf

λ,si,γik

i=1

(18b)

C γik − H vk ∗ ≤ λ ∀i ≤ N, ∀k ≤ K γik ≥ 0 ∀i ≤ N, ∀k ≤ K.



Proof. Assertion (i) follows directly from Theorem 4.2 because (ξ) is concave as an inﬁmum of linear functions in ξ. Indeed, the compactness of the feasible set {y : Wy ≥ h} ensures that Assumption 4.1 holds for K = 1. In this setting, we ﬁnd

[− ]∗(z) = sup

ξ

z,ξ + inf

y

y,Qξ : Wy ≥ h

= inf

y

sup

ξ

z + Q y,ξ : Wy ≥ h

0 if there exists y with Q y = −z and Wy ≥ h, ∞ otherwise,

=

where the second equality follows from the classical minimax theorem [4, Proposition 5.5.4], which applies because {y : Wy ≥ h} is compact. Assertion (i) then follows by substituting [− ]∗ as well as the formula for σΞ from Corollary 5.1 into (11).

Assertion (ii) relies on the following reformulation of the loss function,

 

sup

θ,Hξ + h s.t. W θ = q

q,y s.t. Wy ≥ Hξ + h

inf

y

(ξ) =

=

= max

vk,Hξ + h

θ≥0



k≤K

= max

H vk,ξ + vk,h ,

k≤K

where the ﬁrst equality holds due to strong linear programming duality, which applies as the dual feasible set is non-empty. The second equality exploits the elementary observation that the optimal value of a linear program with non-empty, compact feasible set is always adopted at a vertex. As we managed to express (ξ) as a pointwise maximum of linear functions, assertion (ii) follows immediately from Corllary 5.1 (i).

As expected, in the ambiguity-free limit, problem (18a) reduces to a standard SAA problem. Indeed, for ε = 0, the variable λ can be made large at no penalty, and thus γi = 0 and si = yi,Q ξi at optimality. In this case, problem (18a) is equivalent to

inf

yi

N

1 N

i=1

yi,Q ξi : Wyi ≥ h ∀i ≤ N .

Similarly, one can verify that for ε = 0, (18b) reduces to the SAA problem

inf

yi

N

1 N

i=1

yi,q : Wyi ≥ H ξi ∀i ≤ N .

We close this section with a remark on the computational complexity of all the convex optimization problems derived in this section.

- Remark 5.5 (Computational tractability).


- • If the Wasserstein metric is deﬁned in terms of the 1-norm (i.e., ξ = mk=1 |ξk|) or the ∞-norm (i.e., ξ = maxk≤m |ξk|), then the optimization problems (15a), (15b), (17a), (17b), (18a) and (18b) all reduce to linear programs whose sizes scale with the number N of data points and the number J of aﬃne pieces of the underlying loss functions.
- • Except for the two-stage stochastic program with right-hand side uncertainty in (18b), the resulting linear programs scale polynomially in the problem description and are therefore computationally

tractable. As the number of vertices vk, k ≤ K, of the polytope {θ ≥ 0 : W θ = q} may be exponential in the number of its facets, however, the linear program (18b) has generically exponential size.

- • Inspecting (15a), one easily veriﬁes that the distributionally robust optimization problem (5) reduces to a ﬁnite convex program if X is convex and h(x,ξ) = maxk≤K ak(x),ξ + bk(x), while the gradients ak(x) and the intercepts bk(x) depend linearly on x. Similarly, (5) can be reformulated as a ﬁnite convex program if X is convex and h(x,ξ) = infy y,Qξ : Wy ≥ h(x) or h(x,ξ) = infy q,y : Wy ≥ H(x)ξ + h(x) , while the right hand side coeﬃcients h(x) and H(x) depend linearly on x; see (18a) and (18b), respectively. In contrast, problems (15b), (17a) and (17b) result in non-convex optimization problems when their data depends on x.


- • We emphasize that the computational complexity of all convex programs examined in this section is independent of the radius ε of the Wasserstein ball.


6. Tractable Extensions

We now demonstrate that through minor modiﬁcations of the proofs, Theorems 4.2 and 4.4 extend to worst-case expectation problems involving even richer classes of loss functions. First, we investigate problems where the uncertainty can be viewed as a stochastic process and where the loss function is additively separable. Next, we study problems whose loss functions are convex in the uncertain variables and are therefore not necessarily representable as ﬁnite maxima of concave functions as postulated by Assumption 4.1.

### 6.1. Stochastic Processes with a Separable Cost

Consider a variant of the worst-case expectation problem (10), where the uncertain parameters can be interpreted as a stochastic process ξ = ξ1,...,ξT , and assume that ξt ∈ Ξt, where Ξt ⊆ Rm is non-empty and closed for any t ≤ T. Moreover, assume that the loss function is additively separable with respect to the temporal structure of ξ, that is,

T

(ξ) :=

max

k≤K

t=1

tk ξt , (19)

where tk : Rm → R is a measurable function for any k ≤ K and t ≤ T. Such loss functions appear, for instance, in open-loop stochastic optimal control or in multi-item newsvendor problems. Consider a process

norm ξ T = Tt=1 ξt associated with the base norm  ·  on Rm, and assume that its induced metric is the one used in the deﬁnition of the Wasserstein distance. Note that if  ·  is the 1-norm on Rm, then  · T reduces to the 1-norm on RmT.

By interchanging summation and maximization, the loss function (19) can be re-expressed as

T

(ξ) = max

kt≤K

t=1

tkt ξt ,

where the maximum runs over all KT combinations of k1,...,kT ≤ K. Under this representation, Theorem 4.2 remains applicable. However, the resulting convex optimization problem would involve O(KT) decision variables and constraints, indicating that an eﬃcient solution may not be available. Fortunately, this deﬁciency can be overcome by modifying Theorem 4.2.

- Theorem 6.1 (Convex reduction for separable loss functions). Assume that the loss function is of the form


- (19), and the Wasserstein ball is deﬁned through the process norm  · T. Then, for any ε ≥ 0, the worst-case expectation (10) is smaller or equal to the optimal value of the ﬁnite convex program


 

N

T

λε + N1

sti s.t. [− tk]∗ ztik − νtik + σΞ

inf

λ,sti,ztik,νtik

t=1

i=1

(20)

(νtik) − ztik, ξti ≤ sti ∀i ≤ N, ∀k ≤ K, ∀t ≤ T, ztik ∗ ≤ λ ∀i ≤ N, ∀k ≤ K, ∀t ≤ T.

t



If Ξt and { tk}k≤K satisfy the convexity Assumption 4.1 for every t ≤ T, then the worst-case expectation (10) coincides exactly with the optimal value of problem (20).

Proof. Up until equation (12d), the proof of Theorem 6.1 parallels that of Theorem 4.2. Starting from (12d), we then have

1 N

EQ (ξ) = inf

sup

λε +

λ≥0

Q∈Bε( PN)

N

T

1 N

##### = inf

λε +

λ≥0

t=1

i=1

N

sup

ξ

i=1

(ξ) − λ ξ − ξi

T

sup

ξt∈Ξt

max

k≤K

tk ξt − λ ξt − ξti ,

where the interchange of the summation and the maximization is facilitated by the separability of the overall loss function. Introducing epigraphical auxiliary variables yields

 

T

N

λε + N1

sti s.t. sup

inf

λ,sti

t=1

i=1

tk ξt − λ ξt − ξti ≤ sti ∀i ≤ N, ∀k ≤ K, ∀t ≤ T λ ≥ 0

ξt∈Ξt



 

N

T

λε + N1

inf

sti s.t. sup

λ,sti,ztik

t=1

i=1

≤

tk ξt − ztik,ξt + ztik, ξti ≤ sti ∀i ≤ N, ∀k ≤ K, ∀t ≤ T ztik ∗ ≤ λ ∀i ≤ N, ∀k ≤ K, ∀t ≤ T

ξt∈Ξt



 

N

T

λε + N1

inf

sti s.t. [− tk + χΞ

λ,sti,ztik

t=1

i=1

=

]∗ − ztik + ztik, ξti ≤ sti ∀i ≤ N, ∀k ≤ K, ∀t ≤ T ztik ∗ ≤ λ ∀i ≤ N, ∀k ≤ K, ∀t ≤ T,

t



where the inequality is justiﬁed in a similar manner as the one in (12e), and it holds as an equality provided that Ξt and { tk}k≤K satisfy Assumption 4.1 for all t ≤ T. Finally, by [42, Theorem 11.23(a), p. 493], the conjugate of − tk + χΞ

##### can be replaced by the inf-convolution of the conjugates of − tk and χΞ

. This completes the proof.

t

t

Note that the convex program (20) involves only O(NKT) decision variables and constraints. Moreover, if tk is aﬃne for every t ≤ T and k ≤ K, while  ·  represents the 1-norm or the ∞-norm on Rm, then

- (20) reduces to a tractable linear program (see also Remark 5.5). A natural generalization of Theorem 4.4 further allows us to characterize the extremal distributions of the worst-case expectation problem (10) with a separable loss function of the form (19).


- Theorem 6.2 (Worst-case distributions for separable loss functions). Assume that the loss function is of


the form (19), and the Wasserstein ball is deﬁned through the process norm  · T. If Ξt and { tk}k≤K satisfy Assumption 4.1 for all t ≤ T, then the worst-case expectation (10) coincides with the optimal value of the ﬁnite convex program



T

N

K

αtik tk ξti − q

1 N

sup

tik αtik

αtik,qtik

t=1

i=1

k=1

N

K

T

s.t. N1



qtik ≤ ε K k=1

t=1

i=1

k=1

(21)

αtik = 1 ∀i ≤ N, ∀t ≤ T

αtik ≥ 0 ∀i ≤ N, ∀t ≤ T, ∀k ≤ K ξti − q



αtik ∈ Ξt ∀i ≤ N, ∀t ≤ T, ∀k ≤ K

tik

irrespective of ε ≥ 0. Let αtik(r),qtik(r) r∈N be a sequence of feasible decisions whose objective values converge to the supremum of (21). Then, the discrete (product) probability distributions

N

T

1 N

Qr :=

t=1

i=1

K

qtik(r) αtik(r)

tik(r) with ξtik(r) := ξti −

αtik(r)δξ

k=1

belong to the Wasserstein ball Bε( PN) and attain the supremum of (10) asymptotically, i.e.,

EQr

EQ (ξ) = lim

sup

r→∞

Q∈Bε( PN)

N

1 N

(ξ) = lim

r→∞

i=1

K

T

αtik(r) tk ξtik(r) .

t=1

k=1

Proof. As in the proof of Theorem 4.4, the claim follows by dualizing the convex program (20). Details are omitted for brevity of exposition.

We emphasize that the distributions Qr from Theorem 6.2 can be constructed eﬃciently by solving a convex program of polynomial size even though they have NKT discretization points.

### 6.2. Convex Loss Functions

Consider now another variant of the worst-case expectation problem (10), where the loss function is proper, convex and lower semicontinuous. Unless is piecewise aﬃne, we cannot represent such a loss function as a pointwise maximum of ﬁnitely many concave functions, and thus Theorem 4.2 may only provide a loose upper bound on the worst-case expectation (10). The following theorem provides an alternative upper bound that admits new insights into distributionally robust optimization with Wasserstein balls and becomes exact for Ξ = Rm.

- Theorem 6.3 (Convex reduction for convex loss functions). Assume that the loss function is proper, convex,


and lower semicontinuous, and deﬁne κ := sup θ ∗ : ∗(θ) < ∞ . Then, for any ε ≥ 0, the worst-case expectation (10) is smaller or equal to

N

1 N

( ξi). (22)

κε +

i=1

If Ξ = Rm, then the worst-case expectation (10) coincides exactly with (22).

- Remark 6.4 (Radius of eﬀective domain). The parameter κ can be viewed as the radius of the smallest ball containing the eﬀective domain of the conjugate function ∗ in terms of the dual norm. By the standard conventions of extended arithmetic, the term κε in (22) is interpreted as 0 if κ = ∞ and ε = 0.


Proof. Equation (12b) in the proof of Theorem 4.2 implies that

N

1 N

EQ (ξ) = inf

(ξ) − λ ξ − ξi (23)

sup

λε +

sup

λ≥0

ξ∈Ξ

Q∈Bε( PN)

i=1

for every ε > 0. As is proper, convex, and lower semicontinuous, it coincides with its bi-conjugate function ∗∗, see e.g. [4, Proposition 1.6.1(c)]. Thus, we may write

θ,ξ − ∗(θ),

(ξ) = sup

θ∈Θ

where Θ := {θ ∈ Rm : ∗(θ) < ∞} denotes the eﬀective domain of the conjugate function ∗. Using this dual representation of in conjunction with the deﬁnition of the dual norm, we ﬁnd

sup

ξ∈Ξ

(ξ) − λ ξ − ξi = sup ξ∈Ξ

sup

θ∈Θ

θ,ξ − ∗(θ) − λ ξ − ξi

θ,ξ − ∗(θ) + z,ξ − z, ξi .

##### = sup

sup

inf

z ∗≤λ

ξ∈Ξ

θ∈Θ

The classical minimax theorem [4, Proposition 5.5.4] then allows us to interchange the maximization over ξ with the maximization over θ and the minimization over z to obtain

θ + z,ξ − ∗(θ) − z, ξi

(ξ) − λ ξ − ξi = sup θ∈Θ

sup

inf

sup

z ∗≤λ

ξ∈Ξ

ξ∈Ξ

σΞ(θ + z) − ∗(θ) − z, ξi . (24)

= sup

inf

z ∗≤λ

θ∈Θ

Recall that σΞ denotes the support function of Ξ. It seems that there is no simple exact reformulation of (24) for arbitrary convex uncertainty sets Ξ. Interchanging the maximization over θ with the minimization over z in (24) would lead to the conservative upper bound of Corollary 4.3. Here, however, we employ an alternative approximation. By deﬁnition of the support function, we have σΞ ≤ σRm = χ{0}. Replacing σΞ with χ{0} in (24) thus results in the conservative approximation

( ξi) if sup θ ∗ : θ ∈ Θ ≤ λ, ∞ otherwise.

(ξ) − λ ξ − ξi ≤

(25)

sup

ξ∈Rm

The inequality (22) then follows readily by substituting (25) into (23) and using the deﬁnition of κ in the theorem statement. For Ξ = Rm we have σΞ = χ{0}, and thus the upper bound (22) becomes exact. Finally, if ε = 0, then (10) trivially coincides with (22) under our conventions of extended arithmetic. Thus, the claim follows.

Theorem 6.3 asserts that for Ξ = Rm, the worst-case expectation (10) of a convex loss function reduces the sample average of the loss adjusted by the simple correction term κε. The following proposition highlights that κ can be interpreted as a measure of maximum steepness of the loss function. This interpretation has intuitive appeal in view of Deﬁnition 3.1.

- Proposition 6.5 (Steepness of the loss function). Let κ be deﬁned as in Theorem 6.3.


- (i) If is L-Lipschitz continuous, i.e., if there exists ξ ∈ Rm such that (ξ) − (ξ ) ≤ L ξ − ξ for all ξ ∈ Rm, then κ ≤ L.

- (ii) If majorizes an aﬃne function, i.e., if there exists θ ∈ Rm with θ ∗ =: L and ξ ∈ Rm such that (ξ) − (ξ ) ≥ θ,ξ − ξ for all ξ ∈ Rm, then κ ≥ L.


Proof. The proof follows directly from the deﬁnition of conjugacy. As for (i), we have ∗(θ) = sup

θ,ξ − (ξ) ≥ sup

θ,ξ − L ξ − ξ − (ξ )

ξ∈Rm

ξ∈Rm

θ,ξ − z,ξ − ξ − (ξ ),

= sup

inf

ξ∈Rm

z ∗≤L

where the last equality follows from the deﬁnition of the dual norm. Applying the minimax theorem [4, Proposition 5.5.4] and explicitly carrying out the maximization over ξ yields

θ,ξ − (ξ ) if θ ∗ ≤ L, ∞ otherwise.

∗(θ) ≥

Consequently, ∗(θ) is inﬁnite for all θ with θ ∗ > L, which readily implies that the  · ∗-ball of radius L contains the eﬀective domain of ∗. Thus, κ ≤ L.

As for (ii), we have

∗(θ) = sup

ξ∈Rm

θ,ξ − (ξ) ≤ sup

ξ∈Rm

θ,ξ − z,ξ − ξ − (ξ )

= σRm(θ − z) + z,ξ − (ξ ), which implies that ∗(θ) ≤ θ,ξ − (ξ ) < ∞. Thus, θ belongs to the eﬀective domain of ∗. We then conclude that κ ≥ θ ∗ = L.

- Remark 6.6 (Consistent formulations). If Ξ = Rm and the loss function is given by (ξ) = maxk≤K{ ak,ξ + bk}, then both Corollary 5.1 and Theorem 6.3 oﬀer an exact reformulation of the worst-case expectation (10) in

terms of a ﬁnite-dimensional convex program. On the one hand, Corollary 5.1 implies that (10) is equivalent to

 



min

λ

λε + N1

N

i=1

( ξi) s.t. ak ∗ ≤ λ ∀k ≤ K,

which is obtained by setting C = 0 and d = 0 in (15a). At optimality we have λ = maxk≤K ak ∗, which corresponds to the (best) Lipschitz constant of (ξ) with respect to the norm  · . On the other hand, Theorem 6.3 implies that (10) is equivalent to (22) with κ = λ . Thus, Corollary 5.1 and Theorem 6.3 are consistent.

- Remark 6.7 (ε-insensitive optimizers3). Consider a loss function h(x,ξ) that is convex in ξ, and assume that Ξ = Rm. In this case Theorem 6.3 remains valid, but the steepness parameter κ(x) may depend on x. For loss functions whose Lipschitz modulus with respect to ξ is independent of x (e.g., the newsvendor loss), however, κ(x) is constant. In this case the distributionally robust optimization problem (5) and the SAA problem (4) share the same minimizers irrespective of the Wasserstein radius ε. This phenomenon could explain why the SAA solutions tend to display a surprisingly strong out-of-sample performance in these problems.


7. Numerical Results

We validate the theoretical results of this paper in the context of a stylized portfolio selection problem. The subsequent simulation experiments are designed to provide additional insights into the performance guarantees of the proposed distributionally robust optimization scheme.

### 7.1. Mean-Risk Portfolio Optimization

Consider a capital market consisting of m assets whose yearly returns are captured by the random vector ξ = [ξ1,...,ξm] . If short-selling is forbidden, a portfolio is encoded by a vector of percentage weights x = [x1,...,xm] ranging over the probability simplex X = {x ∈ Rm+ : mi=1 xi = 1}. As portfolio x invests a percentage xi of the available capital in asset i for each i = 1,...,m, its return amounts to x,ξ . In the remainder we aim to solve the single-stage stochastic program

EP − x,ξ + ρP-CVaRα − x,ξ , (26)

J = inf

x∈X

which minimizes a weighted sum of the mean and the conditional value-at-risk (CVaR) of the portfolio loss − x,ξ , where α ∈ (0,1] is referred to as the conﬁdence level of the CVaR, and ρ ∈ R+ quantiﬁes the investor’s risk-aversion. Intuitively, the CVaR at level α represents the average of the α×100% worst (highest) portfolio losses under the distribution P. Replacing the CVaR in the above expression with its formal deﬁnition [41], we obtain

1 α

EP − x,ξ + ρ inf

EP τ +

max − x,ξ − τ,0

J = inf

x∈X

τ∈R

EP max k≤K

= inf

ak x,ξ + bkτ ,

x∈X,τ∈R

3We are indepted to Vishal Gupta who has brought this interesting observation to our attention.

where K = 2, a1 = −1, a2 = −1 − αρ , b1 = ρ and b2 = ρ(1 − α1 ). An investor who is unaware of the distribution P but has observed a dataset ΞN of N historical samples from P and knows that the support of P is contained in Ξ = {ξ ∈ Rm : Cξ ≤ d} might solve the distributionally robust counterpart of (26) with respect to the Wasserstein ambiguity set Bε( PN), that is,

EQ max k≤K

JN(ε) := inf

ak x,ξ + bkτ ,

sup

x∈X,τ∈R

Q∈Bε( PN)

where we make the dependence on the Wasserstein radius ε explicit. By Corollary 5.1 we know that



N

λε + N1

si s.t. x ∈ X

inf

x,τ,λ,si,γik

i=1



JN(ε) =

(27)

bkτ + ak x, ξi + γik,d − C ξi ≤ si ∀i ≤ N, ∀k ≤ K

C γik − akx ∗ ≤ λ ∀i ≤ N, ∀k ≤ K γik ≥ 0 ∀i ≤ N, ∀k ≤ K.



Before proceeding with the numerical analysis of this problem, we provide some analytical insights into its optimal solutions when there is signiﬁcant ambiguity. In what follows we keep the training data set ﬁxed and let xN(ε) be an optimal distributionally robust portfolio corresponding to the Wasserstein ambiguity set of radius ε. We will now show that, for natural choices of the ambiguity set, xN(ε) converges to the equally weighted portfolio m1 e as ε tends to inﬁnity, where e := (1,...,1) . The optimality of the equally weighted portfolio under high ambiguity has ﬁrst been demonstrated in [37] using analytical methods. We identify this result here as an immediate consequence of Theorem 4.2, which is primarily a computational result.

For any non-empty set S ⊆ Rm we denote by recc(S) := {y ∈ Rm : x + λy ∈ S ∀x ∈ S, ∀λ ≥ 0} the recession cone and by S◦ := {y ∈ Rm : y,x ≤ 0 ∀x ∈ S} the polar cone of S.

Lemma 7.1. If {εk}k∈N ⊂ R+ tends to inﬁnity, then any accumulation point x of xN(εk) k∈N is a portfolio that has minimum distance to (recc(Ξ))◦ with respect to  · ∗.

Proof. Note ﬁrst that xN(εk), k ∈ N, and x exist because X is compact. For large Wasserstein radii ε, the term λε dominates the objective function of problem (27). Using standard epi-convergence results [42, Section 7.E], one can thus show that

x ∈ arg min

C γik − akx ∗

min

max

x∈X

γik≥0

i≤N, k≤K

C γ + |ak|x ∗

= arg min

max

min

x∈X

γ≥0

i≤N, k≤K

|ak|

= arg min

min

C γ + x ∗ max k≤K

x∈X

γ≥0

= arg min

min

C γ + x ∗,

x∈X

γ≥0

where the ﬁrst equality follows from the fact that ak < 0 for all k ≤ K, the second equality uses the substitution γ → γ|ak|, and the last equality holds because the set of minimizers of an optimization problem is not aﬀected by a positive scaling of the objective function. Thus, x is the portfolio nearest to the cone C = {C γ : γ ≥ 0}. The claim now follows as the polar cone

C◦ := {y ∈ Rm : y x ≤ 0 ∀x ∈ C} = {y ∈ Rm : y C γ ≤ 0 ∀γ ≥ 0} = {y ∈ Rm : Cy ≥ 0} is readily recognized as the recession cone of Ξ and as C = (C◦)◦.

- Proposition 7.2 (Equally weighted portfolio). Assume that the Wasserstein metric is deﬁned in terms of the


p-norm in the uncertainty space for some p ∈ [1,∞). If {εk}k∈N ⊂ R+ tends to inﬁnity, then xN(εk) k∈N converges to the equally weighted portfolio x = m1 e provided that the uncertainty set is given by

- 0.8
- 1


Averageportfolioweights

0.6

0.4

0.2

0

10-3 10-2 10-1 100

ε

(a) N = 30 training samples

- 0.8
- 1


Averageportfolioweights

0.6

0.4

0.2

0

10-3 10-2 10-1 100

ε

(b) N = 300 training samples

- 0.8
- 1


Averageportfolioweights

0.6

0.4

0.2

0

10-3 10-2 10-1 100

ε

(c) N = 3000 training samples

Figure 4. Optimal portfolio composition as a function of the Wasserstein radius ε averaged over 200 simulations; the portfolio weights are depicted in ascending order, i.e., the weight of asset 1 at the bottom (dark blue area) and that of asset 10 at the top (dark red area)

- (i) the entire space, i.e., Ξ = Rm, or
- (ii) the nonnegative orthant shifted by −e, i.e., Ξ = {ξ ∈ Rm : ξ ≥ −e}, which captures the idea that no asset can lose more than 100% of its value.


Proof. (i) One easily veriﬁes from the deﬁnitions that (recc(Ξ))◦ = {0}. Moreover, we have  · ∗ =  · q where p1 + 1q = 1. As p ∈ [1,∞), we conclude that q ∈ (1,∞], and thus the unique nearest portfolio to (recc(Ξ))◦ with respect to  · ∗ is x = m1 e. The claim then follows from Lemma 7.1. Assertion (ii) follows in a similar manner from the observation that (recc(Ξ))◦ is now the non-positive orthant.

With some extra eﬀort one can show that for every p ∈ [1,∞) there is a threshold ε¯ > 0 with xN(ε) = x for all ε ≥ ε¯, see [37, Proposition 3]. Moreover, for p ∈ {1,2} the threshold ε¯ is known analytically.

### 7.2. Simulation Results: Portfolio Optimization

Our experiments are based on a market with m = 10 assets considered in [7, Section 7.5]. In view of the capital asset pricing model we may assume that the return ξi is decomposable into a systematic risk factor ψ ∼ N(0,2%) common to all assets and an unsystematic or idiosyncratic risk factor ζi ∼ N(i×3%,i×2.5%) speciﬁc to asset i. Thus, we set ξi = ψ + ζi, where ψ and the idiosyncratic risk factors ζi, i = 1,...,m, constitute independent normal random variables. By construction, assets with higher indices promise higher mean returns at a higher risk. Note that the given moments of the risk factors completely determine the distribution P of ξ. This distribution has support Ξ = Rm and satisﬁes Assumption 3.3 for the tail exponent a = 1, say. We also set α = 20% and ρ = 10 in all numerical experiments, and we use the 1-norm to measure distances in the uncertainty space. Thus,  · ∗ is the ∞-norm, whereby (27) reduces to a linear program.

#### 7.2.A. Impact of the Wasserstein Radius

In the ﬁrst experiment we investigate the impact of the Wasserstein radius ε on the optimal distributionally robust portfolios and their out-of-sample performance. We solve problem (27) using training datasets of cardinality N ∈ {30,300,3000}. Figure 4 visualizes the corresponding optimal portfolio weights xN(ε) as a function of ε, averaged over 200 independent simulation runs. Our numerical results conﬁrm the theoretical insight of Proposition 7.2 that the optimal distributionally robust portfolios converge to the equally weighted portfolio as the Wasserstein radius ε increases; see also [37].

- 0

.2

.4

.6

.8

- 1


- -1.4
- -1.3
- -1.2
- -1.1
- -1
- -0.9


Out-of-sampleperformance

Reliability

10-4 10-3 10-2 10-1

"

- 0

.2

.4

.6

.8

- 1


- -1.4
- -1.3
- -1.2
- -1.1
- -1
- -0.9


| | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |


Out-of-sampleperformance

Reliability

10-4 10-3 10-2 10-1

"

- 0

.2

.4

.6

.8

- 1


- -1.4
- -1.3
- -1.2
- -1.1
- -1
- -0.9


| | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |


Out-of-sampleperformance

Reliability

10-4 10-3 10-2 10-1

"

(a) N = 30 training samples

(b) N = 300 training samples

(c) N = 3000 training samples

Figure 5. Out-of-sample performance J( xN(ε)) (left axis, solid line and shaded area) and reliability PN[J( xN(ε)) ≤ JN(ε)] (right axis, dashed line) as a function of the Wasserstein radius ε and estimated on the basis of 200 simulations

The out-of-sample performance J xN(ε) := EP − xN(ε),ξ + ρP-CVaRα − xN(ε),ξ

of any ﬁxed distributionally robust portfolio xN(ε) can be computed analytically as P constitutes a normal distribution by design, see, e.g., [41, p. 29]. Figure 5 shows the tubes between the 20% and 80% quantiles (shaded areas) and the means (solid lines) of the out-of-sample performance J xN(ε) as a function of εestimated using 200 independent simulation runs. We observe that the out-of-sample performance improves (decreases) up to a critical Wasserstein radius εcrit and then deteriorates (increases). This stylized fact was observed consistently across all of simulations and provides an empirical justiﬁcation for adopting a distributionally robust approach.

Figure 5 also visualizes the reliability of the performance guarantees oﬀered by our distributionally robust portfolio model. Speciﬁcally, the dashed lines represent the empirical probability of the event J xN(ε) ≤ JN(ε) with respect to 200 independent training datasets. We ﬁnd that the reliability is nondecreasing in ε. This observation has intuitive appeal because JN(ε) ≥ J( xN(ε)) whenever P ∈ Bε( PN), and the latter event becomes increasingly likely as ε grows. Figure 5 also indicates that the certiﬁcate guarantee sharply rises towards 1 near the critical Wasserstein radius εcrit. Hence, the out-of-sample performance of the distributionally robust portfolios improves as long as the reliability of the performance guarantee is noticeably smaller than 1 and deteriorates when it saturates at 1. Even though this observation was made consistently across all simulations, we were unable to validate it theoretically.

#### 7.2.B. Portfolios Driven by Out-of-Sample Performance

Diﬀerent Wasserstein radii ε may result in robust portfolios xN(ε) with vastly diﬀerent out-of-sample performance J( xN(ε)). Ideally, one should select the radius εNopt that minimizes J( xN(ε)) over all ε ≥ 0; note that εNopt inherits the dependence on the training data from J( xN(ε)). As the true distribution P is unknown, however, it is impossible to evaluate and minimize J( xN(ε)). In practice, the best we can hope for is to approximate εNopt using the training data. Statistics oﬀers several methods to accomplish this goal:

- • Holdout method: Partition ξ1,..., ξN into a training dataset of size NT and a validation dataset of size NV = N − NT. Using only the training dataset, solve (27) for a large but ﬁnite number of candidate


(ε). Use the validation dataset to estimate the out-of-sample performance of xN

radii ε to obtain xN

T

(ε) via the sample average approximation. Set εNhm to any ε that minimizes this quantity. Report xNhm = xN

T

( εNhm) as the data-driven solution and JNhm = JN

( εNhm) as the corresponding certiﬁcate.

T

T

- • k-fold cross validation: Partition ξ1,..., ξN into k subsets, and run the holdout method k times. In each run, use exactly one subset as the validation dataset and merge the remaining k − 1 subsets to a training dataset. Set εNcv to the average of the Wasserstein radii obtained from the k holdout runs. Resolve (27) with ε = εNcv using all N samples, and report xNcv = xN( εNcv) as the data-driven solution and JNcv = JN( εNcv) as the corresponding certiﬁcate.


The holdout method is computationally cheaper, but cross validation has superior statistical properties. There are several other methods to estimate the best Wassertein radius εNopt. By construction, however, no method can provide a radius εN such that xN( εN) has a better out-of-sample performance than xN( εNopt).

In all experiments we compare the distributionally robust approach based on the Wasserstein ambiguity set with the classical sample average approximation (SAA) and with a state-of-the-art data-driven distributionally robust approach, where the ambiguity set is deﬁned via a linear-convex ordering (LCX)-based goodness-of-ﬁt test [7, Section 3.3.2]. The size of the LCX ambiguity set is determined by a single parameter, which should be tuned to optimize the out-of-sample performance. While the best parameter value is unavailable, it can again be estimated using the holdout method or via cross validation. To our best knowledge, the LCX approach represents the only existing data-driven distributionally robust approach for continuous uncertainty spaces that enjoys strong ﬁnite-sample guarantees, asymptotic consistency as well as computational tractability.4

To keep the computational burden manageable, in all experiments we select the Wasserstein radius as well

- as the LCX size parameter from within the discrete set E = {ε = b·10c : b ∈ {0,...,9}, c ∈ {−3,−2,−1}} instead of R+. We have veriﬁed that reﬁning or extending E has only a marginal impact on our results, which indicates that E provides a suﬃciently rich approximation of R+.


In Figures 6(a)–6(c) the sizes of the (LCX and Wasserstein) ambiguity sets are determined via the holdout method, where 80% of the data are used for training and 20% for validation. Figure 6(a) visualizes the tube between the 20% and 80% quantiles (shaded areas) as well as the mean value (solid lines) of the out-of-sample performance J( xN) as a function of the sample size N and based on 200 independent simulation runs, where xN is set to the minimizer of the SAA (blue), LCX (purple) and Wasserstein (green) problems, respectively. The constant dashed line represents the optimal value J of the original stochastic program (1), which is computed through an SAA problem with N = 106 samples. We observe that the Wasserstein solutions tend to be superior to the SAA and LCX solutions in terms of out-of-sample performance.

- Figure 6(b) shows the optimal values JN of the SAA, LCX and Wasserstein problems, where the sizes of

the ambiguity sets are chosen via the holdout method. Unlike Figure 6(a), Figure 6(b) thus reports in-sample estimates of the achievable portfolio performance. As expected, the SAA approach is over-optimistic due to the optimizer’s curse, while the LCX and Wasserstein approaches err on the side of caution. All three methods are known to enjoy asymptotic consistency, which is in agreement with all in-sample and out-of-sample results.

- Figure 6(c) visualizes the reliability of the diﬀerent performance certiﬁcates, that is, the empirical proba-


bility of the event J( xN) ≤ JN evaluated over 200 independent simulation runs. Here, xN represents either an optimal portfolio of the SAA, LCX or Wasserstein problems, while JN denotes the corresponding optimal value. The optimal SAA portfolios display a disappointing out-of-sample performance relative to the optimistically biased mimimum of the SAA problem—particularly when the training data is scarce. In contrast, the out-of-sample performance of the optimal LCX and Wasserstein portfolios often undershoots JN.

4Much like worst-case expectations over Wasserstein balls, worst-case expectations over LCX ambiguity sets can be reformulated as ﬁnite convex programs whenever the underlying loss function represents a pointwise maximum of K concave component functions. Unlike problem (11) in Theorem 4.2, however, the resulting convex program scales exponentially with K.

10

0.5

- 0.8
- 1


Out-of-sampleperformance

SAA LCX Wass

SAA LCX Wass

8

0

J?

6

J?

cateCerti-

Reliability

0.6

SAA LCX Wass

4

- -1.5
- -1
- -0.5


2

0.4

0

0.2

-2

0

101 102 103

101 102 103

101 102 103

N

N

N

(a) Holdout method

(b) Holdout method

###### (c) Holdout method

10

0.5

Out-of-sampleperformance

- 0.8
- 1


SAA LCX Wass

SAA LCX Wass

8

0

J?

6

J?

cateCerti-

Reliability

0.6

4

SAA LCX Wass

- -1.5
- -1
- -0.5


2

0.4

0

0.2

-2

0

101 102 103

101 102 103

101 102 103

N

N

N

(d) k-fold cross validation

(e) k-fold cross validation

###### (f) k-fold cross validation

10

0.5

- 0.8
- 1


Out-of-sampleperformance

SAA LCX Wass

SAA LCX Wass

8

0

J?

6

J?

cateCerti-

Reliability

0.6

SAA LCX Wass

4

- -1.5
- -1
- -0.5


2

0.4

0

0.2

-2

0

101 102 103

101 102 103

101 102 103

N

N

N

(g) Optimal size

(h) Optimal size

(i) Optimal size

Figure 6. Out-of-sample performance J( xN), certiﬁcate JN, and certiﬁcate reliability PN J( xN) ≤ JN for the performance-driven SAA, LCX and Wasserstein solutions as a function of N

Figures 6(d)–6(f) show the same graphs as Figures 6(a)–6(c), but now the sizes of the ambiguity sets are determined via k-fold cross validation with k = 5. In this case, the out-of-sample performance of both distributionally robust methods improves slightly, while the corresponding certiﬁcates and their reliabilities increase signiﬁcantly with respect to the naı¨ve holdout method. However, these improvements come at the expense of a k-fold increase in the computational cost.

One could think of numerous other statistical methods to select the size of the Wasserstein ambiguity set. As discussed above, however, if the ultimate goal is to minimize the out-of-sample performance of xN(ε), then the best possible choice is ε = εNopt. Similarly, one can construct a size parameter for the LCX ambiguity set that leads to the best possible out-of-sample performance of any LCX solution. We emphasize that these optimal Wasserstein radii and LCX size parameters are not available in practice because computing J( xN(ε)) requires knowledge of the data-generating distribution. In our experiments we evaluate J( xN(ε)) to high

accuracy for every ﬁxed ε ∈ E using 2·105 validation samples, which are independent from the (much fewer) training samples used to compute xN(ε). Figures 6(g)–6(i) show the same graphs as Figures 6(a)–6(c) for optimally sized ambiguity sets. By construction, no method for sizing the Wasserstein or LCX ambiguity sets can result in a better out-of-sample performance, respectively. In this sense, the graphs in Figure 6(g) capture the fundamental limitations of the diﬀerent distributionally robust schemes.

#### 7.2.C. Portfolios Driven by Reliability

In Section 7.2.B the Wasserstein radii and LCX size parameters were calibrated with the goal to achieve the best out-of-sample performance. Figures 6(c), 6(f) and 6(i) reveal, however, that by optimizing the outof-sample performance one may sacriﬁce reliability. An alternative objective more in line with the general philosophy of Section 2 would be to choose Wasserstein radii that guarantee a prescribed reliability level. Thus, for a given β ∈ [0,1] we should ﬁnd the smallest Wasserstein radius ε ≥ 0 for which the optimal value JN(ε) of (27) provides an upper 1 − β conﬁdence bound on the out-of-sample performance J( xN(ε)) of its optimal solution. As the true distribution P is unknown, however, the optimal Wasserstein radius corresponding to a given β cannot be computed exactly. Instead, we must derive an estimator εNβ that depends on the training data. We construct εNβ and the corresponding reliability-driven portfolio via bootstrapping as follows:

- (1) Construct k resamples of size N (with replacement) from the original training dataset. It is well known that, as N grows, the probability that any ﬁxed training data point appears in a particular resample converges to e−e1 ≈ 32. Thus, about N3 training samples are absent from any resample. We collect all unused samples in a validation dataset.

- (2) For each resample κ = 1,...,k and ε ≥ 0, solve problem (27) using the Wasserstein ball of radius ε around the empirical distribution PκN on the κ-th resample. The resulting optimal decision and optimal value are denoted as xκN(ε) and JNκ (ε), respectively. Next, estimate the out-of-sample performance J( xκN(ε)) of xκN(ε) using the sample average over the κ-th validation dataset.
- (3) Set εNβ to the smallest ε ≥ 0 so that the certiﬁcate JNκ (ε) exceeds the estimate of J( xκN(ε)) in at least (1 − β) × k diﬀerent resamples.
- (4) Compute the data-driven portfolio xN = xN( εNβ) and the corresponding certiﬁcate JN = JN( εNβ) using the original training dataset.


As in Section 7.2.B, we compare the Wasserstein approach with the LCX and SAA approaches. Speciﬁcally, by using bootstrapping, we calibrate the size of the LCX ambiguity set so as to guarantee a desired reliability level 1−β. The SAA problem, on the other hand, has no free parameter that can be tuned to meet a prescribed reliability target. Nevertheless, we can construct a meaningful certiﬁcate of the form JN(∆) := JSAA + ∆ for the SAA portfolio by adding a non-negative constant to the optimal value of the SAA problem. Our aim is to ﬁnd the smallest oﬀset ∆ ≥ 0 with the property that JN(∆) provides an upper 1−β conﬁdence bound on the out-of-sample performance J( xSAA) of the optimal SAA portfolio xSAA. The optimal oﬀset corresponding to a given β cannot be computed exactly. Instead, we must derive an estimator ∆Nβ that depends on the training data. Such an estimator can be found through a simple variant of the above bootstrapping procedure.

In all experiments we set the number of resamples to k = 50. Figures 7(a)–7(c) visualize the out-ofsample performance, the certiﬁcate and the empirical reliability of the reliability-driven portfolios obtained with the SAA, LCX and Wasserstein approaches, respectively, for the reliability target 1 − β = 90% and based on 200 independent simulation runs. Figures 7(d)–7(f) show the same graphs as Figures 7(a)–7(c) but for the reliability target 1 − β = 75%. We observe that the new SAA certiﬁcate now overestimates the true optimal value of the portfolio problem. Moreover, while the empirical reliability of the SAA solution now closely matches the desired reliability target, the empirical reliabilities of the LCX and Wasserstein

10

- 0.8
- 1


- 0

0.5

1

- 1.5 SAA


SAA LCX Wass

Out-of-sampleperformance

LCX Wass

8

J?

J?

6

cateCerti-

Reliability

0.6

4

0.4

2

-0.5

0.2

SAA LCX Wass

0

-1

-2

0

-1.5

101 102 103

101 102 103

101 102 103

N

N

N

(a) β = 10%

- 0

- 0.5
- 1


- 1.5 SAA


Out-of-sampleperformance

LCX Wass

J?

cateCerti-

- -1.5
- -1
- -0.5


101 102 103

N

(b) β = 10%

- 0
- 1
- 2
- 3
- 4


| | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |SA LC|A X| | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | |W J|as<br><br>?|s| |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |


- -2
- -1


101 102 103

N

###### (c) β = 10%

- 0.8
- 1


Reliability

0.6

SAA LCX Wass

0.4

0.2

0

101 102 103

N

(d) β = 25%

(e) β = 25%

(f) β = 25%

Figure 7. Out-of-sample performance J( xN), certiﬁcate JN, and certiﬁcate reliability PN J( xN) ≤ JN for the reliability-driven SAA, LCX and Wasserstein portfolios as a function of N

solutions are similar but noticeably exceed the prescribed reliability threshold. A possible explanation for this phenomenon is that the k resamples generated by the bootstrapping algorithm are not independent, which may give rise to a systematic bias in estimating the Wasserstein radii required for the desired reliability levels.

#### 7.2.D. Impact of the Sample Size on the Wasserstein Radius

It is instructive to analyze the dependence of the Wasserstein radii on the sample size N for diﬀerent datadriven schemes. As for the performance-driven portfolios from Section 7.2.B, Figure 8 depicts the best possible Wasserstein radius εNopt as well as the Wasserstein radii εNhm and εNcv obtained by the holdout method and via k-fold cross validation, respectively. As for the reliability-driven portfolios from Section 7.2.C, Figure 8 further depicts the Wasserstein radii εβN, for β ∈ {10%,25%}, obtained by bootstrapping. All results are averaged across 200 independent simulation runs. As expected from Theorem 3.6, all Wasserstein radii tend to zero as N increases. Moreover, the convergence rate is approximately equal to N−21 . This rate is likely to be optimal. Indeed, if X is a singleton, then every quantile of the sample average estimator JSAA converges to J at rate N−12 due to the central limit theorem. Thus, if εN = o(N−21 ), then JN also converges to J

- at leading order N−12 by Theorem 6.3, which applies as the loss function is convex. This indicates that the a priori rate N−m1 suggested by Theorem 3.4 is too pessimistic in practice.


εNhm Holdout

εNcv k-fold

εNopt Optimal

AverageWassersteinradii

εNβ Bootstrap β = 25% εNβ Bootstrap β = 10%

10-1

10-2

101 102 103

N

Figure 8. Optimal performance-driven Wasserstein radius εNopt and its estimates εNhm and εNcv obtained via the holdout method and k-fold cross validation, respectively, as well as the reliability-driven Wasserstein radius εβN for β ∈ {10%,25%} obtained via bootstrapping

### 7.3. Simulation Results: Uncertainty Quantiﬁcation

Investors often wish to determine the probability that a given portfolio will outperform various benchmark indices or assets. Our results on uncertainty quantiﬁcation developed in Section 5.2 enable us to compute this probability in a meaningful way—solely on the basis of the training dataset.

Assume for example that we wish to quantify the probability that any data-driven portfolio xN outperforms the three most risky assets in the market jointly. Thus, we should compute the probability of the closed polytope

A = ξ ∈ Rm : xN,ξ ≥ ξi ∀i = 8,9,10 .

As the true distribution P is unknown, the probability P[ξ ∈ A] cannot be evaluated exactly. Note that A as well as P[ξ ∈ A] constitute random objects that depend on xN and thus on the training data. Using the same training dataset that was used to compute xN, however, we may estimate P[ξ ∈ A] from above and below by

Q ξ ∈ A and inf

Q ξ ∈ A = 1 − sup

Q ξ ∈/ A ,

sup

Q∈Bε( PN)

Q∈Bε( PN)

Q∈Bε( PN)

respectively. Indeed, recall that the true data-generating probability distribution resides in the Wasserstein ball of radius εN(β) deﬁned in (8) with probability 1 − β. Therefore, we have

1 − β ≤ PN ΞN : P ∈ Bε

N(β)( PN) ≤ PN ΞN : sup

Q A ≥ P A ∀A ∈ B(Ξ)

Q∈BεN(β)( PN)

= PN ΞN : inf

Q A − P A ≥ 0 ,

sup

A∈B(Ξ)

Q∈BεN(β)( PN)

where B(Ξ) denotes the set of all Borel subsets of Ξ. The data-dependent set AN can now be viewed as a (measurable) mapping from ΞN to the subsets in B(Ξ). The above inequality then implies

PN ΞN : sup

Q AN − P AN ≥ 0 ≥ 1 − β.

Q∈BεN(β)( PN)

Thus, sup{Q[ AN] : Q ∈ Bε

N(β)( PN)} provides indeed an upper bound on P[ AN] with conﬁdence 1 − β. Similarly, one can show that inf{Q[ AN] : Q ∈ Bε

N(β)( PN)} provides a lower conﬁdence bound on P[ AN].

- 0.8
- 1


Excess

0.2

Shortfall

Reliability

0.1

Excess/Shortfall

Reliability

0.6

0

0.4

- -0.2
- -0.1


0.2

0

10-6 10-5 10-4 10-3 10-2

"

(a) N = 30

- 0.8
- 1


Excess

0.2

Shortfall

Reliability

0.1

Excess/Shortfall

Reliability

0.6

0

0.4

- -0.2
- -0.1


0.2

0

10-6 10-5 10-4 10-3 10-2

"

(b) N = 300

Figure 9. Excess JN+(ε) − P[ A] and shortfall JN−(ε) − P[ A] (solid lines, left axis) as well as reliability PN[ JN−(ε) ≤ P[ A] ≤ JN+(ε)] (dashed lines, right axis) as a function of ε

The upper conﬁdence bound can be computed by solving the linear program (17a). Replacing A with its interior in the lower conﬁdence bound leads to another (potentially weaker) lower bound that can be computed by solving the linear program (17b). We denote these computable bounds by JN+(ε) and JN−(ε), respectively. In all subsequent experiments xN is set to a solution of the distributionally robust program (27) calibrated via k-fold cross validation as described in Section 7.2.B.

#### 7.3.A. Impact of the Wasserstein Radius

As JN+(ε) and JN−(ε) estimate a random target P[ A], it makes sense to ﬁlter out the randomness of the target and to study only the diﬀerences JN+(ε) − P[ A] and JN−(ε) − P[ A]. Figures 9(a) and 9(b) visualize the empirical mean (solid lines) as well as the tube between the empirical 20% and 80% quantiles (shaded areas) of these diﬀerences as a function of the Wasserstein radius ε, based on 200 training datasets of cardinality N = 30 and N = 300, respectively. Figure 9 also shows the empirical reliability of the bounds (dashed lines), that is, the empirical probability of the event JN−(ε) ≤ P[ A] ≤ JN+(ε). Note that the reliability drops to 0 for ε = 0, in which case both JN+(0) and JN−(0) coincide with the SAA estimator for P[ A]. Moreover, at ε = 0 the set A is constructed from the SAA portfolio xN, whose performance is overestimated on the training dataset. Thus, the SAA estimator for P[ A], which is evaluated using the same training dataset, is positively biased. For ε > 0, ﬁnally, the reliability increases as the shaded conﬁdence intervals move away from 0.

#### 7.3.B. Impact of the Sample Size

We propose a variant of the k-fold cross validation procedure for selecting ε in uncertainty quantiﬁcation. Partition ξ1,..., ξN into k subsets and repeat the following holdout method k times. Select one of the subsets as the validation set of size NV and merge the remaining k − 1 subsets to a training dataset of size NT = N −NV . Use the validation set to compute the SAA estimator of P[ A], and use the training dataset to compute JN+

(ε) for a large but ﬁnite number of candidate radii ε. Set εNhm to the smallest candidate radius for which the SAA estimator of P[ A] is not larger than JN+

T

(ε). Next, set εNcv to the average of the Wasserstein radii obtained from the k holdout runs, and report JN+ = JN+( εNcv) as the data-driven upper bound on P[ A]. The data-driven lower bound JN− is constructed analogously in the obvious way.

T

| | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |
| | | | | | | | |Ex Sh|cess ortfa| |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |


0.2

0.1

Excess/Shortfall

0

- -0.2
- -0.1


101 102 103

N

(a) Excess JN+ − P[ A] and shortfall JN− − P[ A] of the datadriven conﬁdence bounds for P[ A]

10-1

| | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | |Ex|c|ess| | | |
| | | | | | | | | | | | |Sh|or|tf|a|ll| |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |


AverageWassersteinradii

10-2

10-3

10-4

101 102 103

N

(b) Data-driven Wasserstein radius εNcv obtained via k-fold cross validation

Figure 10. Dependence of the conﬁdence bounds and the Wasserstein radius on N

- Figure 10(a) visualizes the empirical means (solid lines) as well as the tubes between the empirical 20%

and 80% quantiles (shaded areas) of JN+ − P[ A] and JN− − P[ A] as a function of the sample size N, based on 300 independent training datasets. As expected, the conﬁdence intervals shrink and converge to 0 as N

increases. We emphasize that JN+ and JN− are computed solely on the basis of N training samples, whereas the computation of P[ A] necessitates a much larger dataset, particularly if A constitutes a rare event.

- Figure 10(b) shows the Wasserstein radius εNcv obtained via k-fold cross validation (both for JN+ and JN−).


As usual, all results are averaged across 300 independent simulation runs. A comparison with Figure 8 reveals that the data-driven Wasserstein radii in uncertainty quantiﬁcation display a similar but faster polynomial decay than in portfolio optimization. We conjecture that this is due to the absence of decisions, which implies that uncertainty quantiﬁcation is less susceptible to the optimizer’s curse. Thus, nature (i.e., the ﬁctitious adversary choosing the distribution in the ambiguity set) only has to compensate for noise but not for bias. A smaller Wasserstein radius seems to be suﬃcient for this purpose.

Acknowledgments. We thank Soroosh Shaﬁeezadeh Abadeh for helping us with the numerical experiments. The authors are grateful to Vishal Gupta, Ruiwei Jiang and Nathan Kallus for their valuable comments. This research was supported by the Swiss National Science Foundation under Grant BSCGI0 157733.

Appendix A.

The following technical lemma on the pointwise approximation of an upper semicontinuous function by a non-increasing sequence of Lipschitz continuous majorants strengthens [31, Theorem 4.2], which focuses on bounded domains and continuous (but not necessarily Lipschitz continuous) majorants.

Lemma A.1. If h : Ξ → R is upper semicontinuous and satisﬁes h(ξ) ≤ L(1 + ξ ) for some L ≥ 0, then there exists a non-increasing sequence of Lipschitz continuous functions that converge pointwise to h on Ξ.

Proof. The proof is constructive. Deﬁne the functions

h(ξ ) − kL ξ − ξ , k ∈ N,

hk(ξ) = sup ξ ∈Ξ

where L is the linear growth rate of h. Note that by construction hk(ξ) ≤ L(1 + ξ ). As ξ = ξ is feasible in the maximization problem deﬁning hk(ξ), we have hk(ξ) ≥ h(ξ) for all ξ ∈ Ξ and k ∈ N. Moreover, hk(ξ) is Lipschitz continuous with Lipschitz constant kL (as hk(ξ) constitutes a supremum of norm functions with this property). Given any ξ ∈ Ξ, it remains to be shown that limk→∞ hk(ξ) = h(ξ). Thus, choose ξ k ∈ Ξ with

1 k

h(ξ ) − kL ξ − ξ ≤ h(ξ k) − kL ξ − ξ k +

hk(ξ) = sup ξ ∈Ξ

.

We ﬁrst show that ξk converges to ξ as k tends to ∞. Indeed, we have h(ξ) ≤ hk(ξ) ≤ h(ξ k) − kL ξ − ξ k +

1 k ≤ L(1 + ξ k ) − kL ξ − ξ k +

1 k

1 k

1 k − (k − 1)L ξ − ξ k ,

≤ L(1 + ξ − ξ k + ξ ) − kL ξ − ξ k +

= L(1 + ξ ) +

which implies

1 L(k − 1)

1 k

ξ − ξ k ≤

h(ξ) − L(1 + ξ ) −

, that is, ξ − ξ k → 0 as k → ∞. Therefore, we ﬁnd

1 k ≤ limsup

h(ξ k) ≤ h(ξ), where the last inequality is due to the upper semicontinuity of h. This concludes the proof.

h(ξ) ≤ lim

hk(ξ) ≤ limsup

h(ξ k) − kL ξ − ξ k +

k→∞

k→∞

k→∞

References

- [1] A. Ben-Tal, D. den Hertog, and J.-P. Vial, Deriving robust counterparts of nonlinear uncertain inequalities, Mathematical Programming, 149 (2015), pp. 265–299.
- [2] A. Ben-Tal, D. den Hertog, A. D. Waegenaere, B. Melenberg, and G. Rennen, Robust solutions of optimization problems aﬀected by uncertain probabilities, Management Science, 59 (2013), pp. 341–357.
- [3] A. Ben-Tal, L. El Ghaoui, and A. Nemirovski, Robust Optimization, Princeton University Press, 2009.
- [4] D. P. Bertsekas, Convex Optimization Theory, Athena Scientiﬁc, 2009.
- [5] , Convex Optimization Algorithms, Athena Scientiﬁc, 2015.

- [6] D. Bertsimas, X. V. Doan, K. Natarajan, and C.-P. Teo, Models for minimax stochastic linear optimization problems with risk aversion, Mathematics of Operations Research, 35 (2010), pp. 580–602.
- [7] D. Bertsimas, V. Gupta, and N. Kallus, Robust SAA. Available at arXiv:1408.4445, 2014.
- [8] D. Bertsimas and I. Popescu, On the relation between option and stock prices: A convex optimization approach, Operations Research, 50 (2002), pp. 358–374.
- [9] D. Bertsimas and M. Sim, The price of robustness, Operations Research, 52 (2004), pp. 35–53.
- [10] E. Boissard, Simple bounds for convergence of empirical and occupation measures in 1-Wasserstein distance, Electronic Journal of Probability, 16 (2011), pp. 2296–2333.
- [11] F. Bolley, A. Guillin, and C. Villani, Quantitative concentration inequalities for empirical measures on non-compact spaces, Probability Theory and Related Fields, 137 (2007), pp. 541–593.
- [12] S. Boyd and L. Vandenberghe, Convex Optimization, Cambridge University Press, 2009.
- [13] C. Brownlees, E. Joly, and G. Lugosi, Empirical risk minimization for heavy-tailed losses, The Annals of Statistics, 43

(2015), pp. 2507–2536.

- [14] G. C. Calafiore, Ambiguous risk measures and optimal robust portfolios, SIAM Journal on Optimization, 18 (2007), pp. 853–877.
- [15] O. Catoni, Challenging the empirical mean and empirical variance: A deviation study, Annales de l’Institut Henri Poincare´, Probabilit´es et Statistiques, 48 (2012), pp. 1148–1185.
- [16] N. Chehrazi and T. A. Weber, Monotone approximation of decision problems, Operations Research, 58 (2010), pp. 1158– 1177.
- [17] E. del Barrio, J. A. Cuesta-Albertos, C. Matran,´ et al., Tests of goodness of ﬁt based on the l2-Wasserstein distance, The Annals of Statistics, 27 (1999), pp. 1230–1239.
- [18] E. Delage and Y. Ye, Distributionally robust optimization under moment uncertainty with application to data-driven problems, Operations Research, 58 (2010), pp. 595–612.


- [19] L. El Ghaoui, M. Oks, and F. Oustry, Worst-case Value-at-Risk and robust portfolio optimization: A conic programming approach, Operations Research, 51 (2003), pp. 543–556.
- [20] E. Erdogan˘ and G. Iyengar, Ambiguous chance constrained problems and robust optimization, Mathematical Programming, 107 (2006), pp. 37–61.
- [21] N. Fournier and A. Guillin, On the rate of convergence in Wasserstein distance of the empirical measure, Probability Theory and Related Fields, (2014), pp. 1–32.
- [22] J. Goh and M. Sim, Distributionally robust optimization and its tractable approximations, Operations Research, 58 (2010), pp. 902–917.
- [23] G. A. Hanasusanto and D. Kuhn, Robust data-driven dynamic programming, in Advances in Neural Information Processing Systems, 2013, pp. 827–835.
- [24] G. A. Hanasusanto, D. Kuhn, and W. Wiesemann, A comment on “Computational complexity of stochastic programming problems”, Mathematical Programming, (2016), pp. 557–569.
- [25] Z. Hu and L. J. Hong, Kullback-Leibler divergence constrained distributionally robust optimization. Available at Optimization Online, 2013.
- [26] Z. Hu, L. J. Hong, and A. M.-C. So, Ambiguous probabilistic programs. Available at Optimization Online, 2013.
- [27] R. Jiang and Y. Guan, Data-driven chance constrained stochastic program, Mathematical Programming, 158 (2016), pp. 291–327.
- [28] O. Kallenberg, Foundations of Modern Probability, Probability and its Applications (New York), Springer-Verlag, New York, 1997.
- [29] L. V. Kantorovich and G. S. Rubinshtein, On a space of totally additive functions, Vestnik Leningradskogo Universiteta, 13 (1958), pp. 52–59.
- [30] S. Lang, Real and Functional Analysis, Springer-Verlag, third ed., 1993.
- [31] J. Mashreghi, Representation Theorems in Hardy Spaces, Cambridge University Press, 2009.
- [32] S. Mehrotra and H. Zhang, Models and algorithms for distributionally robust least squares problems, Mathematical Programming, 146 (2014), pp. 123–141.
- [33] A. Muller¨ , Integral probability metrics and their generating classes of functions, Advances in Applied Probability, (1997), pp. 429–443.
- [34] K. Natarajan, M. Sim, and J. Uichanco, Tractable robust expected utility and risk models for portfolio optimization, Mathematical Finance, 20 (2010), pp. 695–731.
- [35] N. Parikh and S. Boyd, Block splitting for distributed optimization, Mathematical Programming Computation, 6 (2014), pp. 77–102.
- [36] G. C. Pflug and A. Pichler, Multistage Sochastic Optimization, Springer, 2014.
- [37] G. C. Pflug, A. Pichler, and D. Wozabal, The 1/N investment strategy is optimal under high model ambiguity, Journal of Banking & Finance, 36 (2012), pp. 410 – 417.
- [38] G. C. Pflug and D. Wozabal, Ambiguity in portfolio selection, Quantitative Finance, 7 (2007), pp. 435–442.
- [39] K. Postek, D. den Hertog, and B. Melenberg, Tractable counterparts of distributionally robust constraints on risk measures, forthcoming in SIAM Review, (2016).
- [40] A. Ramdas, N. Garcia, and M. Cuturi, On Wasserstein two sample testing and related families of nonparametric tests. Available at arXiv:1509.02237, 2015.
- [41] R. T. Rockafellar and S. Uryasev, Optimization of conditional Value-at-Risk, Journal of Risk, 2 (2000), pp. 21–42.
- [42] R. T. Rockafellar and R. J.-B. Wets, Variational Analysis, Springer, 2010.
- [43] H. E. Scarf, A min-max solution of an inventory problem, in Studies in the Mathematical Theory of Inventory and Production, K. J. Arrow, S. Karlin, and H. E. Scarf, eds., Stanford University Press, 1958, pp. 201–209.
- [44] A. Shapiro, On duality theory of conic linear problems, in Semi-Inﬁnite Programming, M. A. Goberna and M. A. L´opez, eds., Kluwer Academic Publishers, 2001, pp. 135–165.
- [45] , Distributionally robust stochastic programming. Available at Optimization Online, 2015.

- [46] A. Shapiro, D. Dentcheva, and A. Ruszczynski´ , Lectures on Stochastic Programming, SIAM, second ed., 2014.
- [47] A. Shapiro and A. Nemirovski, On complexity of stochastic programming problems, in Continuous Optimization, Springer, New York, 2005, pp. 111–146.
- [48] J. E. Smith and R. L. Winkler, The optimizers curse: Skepticism and postdecision surprise in decision analysis, Management Science, 52 (2006), pp. 311–322.
- [49] V. N. Vapnik, Statistical Learning Theory, Wiley, 1998.
- [50] C. Villani, Topics in Optimal Transportation, American Mathematical Society, 2003.
- [51] W. Wiesemann, D. Kuhn, and M. Sim, Distributionally robust convex optimization, Operations Research, 62 (2014), pp. 1358–1376.


- [52] D. Wozabal, A framework for optimization under ambiguity, Annals of Operations Research, 193 (2012), pp. 21–47.
- [53] , Robustifying convex risk measures for linear portfolios: A nonparametric approach, Operations Research, 62 (2014), pp. 1302–1315.

- [54] C. Zhao, Data-Driven Risk-Averse Stochastic Program and Renewable Energy Integration, PhD thesis, University of Florida, 2014.


