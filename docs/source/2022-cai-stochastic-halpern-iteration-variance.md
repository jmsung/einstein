---
type: source
kind: paper
title: Stochastic Halpern Iteration with Variance Reduction for Stochastic Monotone Inclusions
authors: Xufeng Cai, Chaobing Song, Cristóbal Guzmán, Jelena Diakonikolas
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2203.09436v4
source_local: ../raw/2022-cai-stochastic-halpern-iteration-variance.pdf
topic: general-knowledge
cites:
---

# arXiv:2203.09436v4[math.OC]8Jan2023

## Stochastic Halpern Iteration with Variance Reduction for Stochastic Monotone Inclusions

Xufeng Cai* Chaobing Song* Crist´obal Guzm´an† Jelena Diakonikolas*

Abstract

We study stochastic monotone inclusion problems, which widely appear in machine learning applications, including robust regression and adversarial learning. We propose novel variants of stochastic Halpern iteration with recursive variance reduction. In the cocoercive—and more generally Lipschitz-monotone—setup, our algorithm attains norm of the operator with O( 1 3 ) stochastic operator evaluations, which signiﬁcantly improves over state of the art O( 1 4 ) stochastic operator evaluations required for existing monotone inclusion solvers applied to the same problem classes. We further show how to couple one of the proposed variants of stochastic Halpern iteration with a scheduled restart scheme to solve stochastic monotone inclusion problems with O(log(1 2/ )) stochastic operator evaluations under additional sharpness or strong monotonicity assumptions.

### 1 Introduction

Recent trends in machine learning (ML) involve the study of models whose solutions do not reduce to optimization but rather to equilibrium conditions. Standard examples include generative adversarial networks, adversarially robust training of ML models, and training of ML models under notions of fairness. It turns out that several of these equilibrium conditions (including, but not limited to, ﬁrst-order stationary points, saddle-points, and Nash equilibria of minimax games) can be cast as solutions to a monotone inclusion problem, which is deﬁned as the problem of computing a zero of a (maximal) monotone operator F : Rd → Rd (see (MI) for a formal deﬁnition). In the context of min-max optimization problems, monotone inclusion reduces to a stationarity condition, which for unconstrained problems boils down to ﬁnding a point with small gradient norm.

Of particular interest to machine learning are stochastic versions of these problems, in which the operator F is not readily available, but can only be accessed through a stochastic oracle F. Such are the settings mentioned above, where the deﬁnitions of equilibria involve expectations over continuous high-dimensional spaces. The corresponding problem, known as the stochastic monotone inclusion, has not been thoroughly studied, particularly in the context of its stochastic oracle complexity. Understanding stochastic oracle complexity of monotone inclusion in all standard settings with Lipschitz operators, from the algorithmic aspect, is the main motivation of this work.

#### 1.1 Contributions

We study three main classes of stochastic monotone inclusion problems with Lipschitz operators, deﬁned by the assumptions made about the operator itself: (i) cocoercive class, which is the most restricted class, but nevertheless fundamental for understanding monotone inclusion, as it relates to the problem of ﬁnding a ﬁxed point of a nonexpansive (1-Lipschitz) operator; (ii) Lipschitz monotone class, which is perhaps the most basic class arising in the study of smooth convex-concave min-max optimization problems; and (iii) Lipschitz monotone class with an additional sharpness property of the operator. Sharpness is a widely studied property of optimization problems, often referred to as the “local error bound” condition, which is weaker than strong convexity and roughly corresponds to the problem landscape being curved outside of the solution set (see Pang (1997) for a survey of classical results).

From an algorithmic standpoint, we consider variants of classical Halpern iteration (Halpern, 1967), which was originally introduced for solving ﬁxed point equations with nonexpansive operators. Variants of this iteration have

*Department of Computer Sciences, University of Wisconsin-Madison. XC (xcai74@wisc.edu), CS (chaobing.song@wisc.edu), JD (jelena@cs.wisc.edu).

†Institute for Mathematical and Computational Eng., Facultad de Matem´aticas and Escuela de Ingenier´ıa, Pontiﬁcia Universidad Cat´olica de Chile. crguzmanp@mat.uc.cl.

recently been shown to lead to (near-)optimal ﬁrst-order oracle complexity for all aforementioned standard problem classes in deterministic settings (Diakonikolas, 2020; Diakonikolas and Wang, 2022; Yoon and Ryu, 2021). However, to the best of our knowledge, stochastic variants of these methods have received very limited attention prior to our work. The only results we are aware of are for a two-step extragradient-like variant of Halpern iteration in negative comonotone Lipschitz settings (Lee and Kim, 2021) and which show that when variance of operator estimates is bounded by order-

2

k

in iteration k, the method attains operator norm after O(1 ) iterations. However, Lee and Kim (2021) does not discuss how such variance control would be obtained. Simple mini-batching, as we show, only leads to O( 1 4 ) stochastic oracle complexity.

We show that existing variants of the Halpern iteration (Diakonikolas, 2020; Tran-Dinh and Luo, 2021) can be effectively combined with recursive variance reduction (Li et al., 2021) to obtain O( 1 3 ) stochastic oracle complexity in the cocoercive and Lipschitz monotone setups. We then show that the complexity can be further reduced to O 1 2 log(1 ) under an additional sharpness assumption about the operator. The last bound is unimprovable in terms of the dependence on  , due to existing lower bounds, as we argue for completeness in Section 7.

To the best of our knowledge, our work is the ﬁrst to use variance reduction to reduce stochastic oracle complexity of monotone inclusion (small gradient norm in min-max optimization settings), and the attained bounds are the best achieved to date for direct methods.

#### 1.2 Techniques

Inspired by the potential function originally used by Diakonikolas (2020) and later used either in the same or slightly modiﬁed form by Diakonikolas and Wang (2022); Yoon and Ryu (2021); Tran-Dinh and Luo (2021); Lee and Kim (2021), we adapt this potential function-based argument to account for stochastic error terms arising due to the stochastic oracle access to the operator. We ﬁrst show that in the cocoercive minibatch setting, this argument only leads to O( 1 4 ) stochastic oracle complexity, and it is unclear how to improve it directly, as the analysis appears tight. We then combine the cocoercive variant of Halpern iteration (Diakonikolas, 2020) with the PAGE estimator (Li et al., 2021) to reduce the stochastic oracle complexity to O( 1 3 ). The same variance reduced estimator is also used in conjunction with the two-step extrapolated variant of Halpern iteration introduced by Tran-Dinh and Luo (2021), as a direct application of Halpern iteration is not known to converge on the class of Lipschitz monotone operators.

While the basic ideas in our arguments are simple, their realization requires addressing major technical obstacles. First, the variance reduced estimator that we use (Li et al., 2021) was originally devised for smooth nonconvex optimization problems, where it was coupled with a stochastic variant of gradient descent. This is signiﬁcant, because the proof relies on a descent lemma, which allows cancelling the error arising from the variance of the estimator by the “descent” part. Such an argument is not possible in our setting, as there is no objective function to descend on. Instead, our analysis relies on an intricate inductive argument that ensures that the expected norm of the operator is bounded in each iteration, assuming a suitable bound on the variance of the estimator. To obtain our desired result for the variance, we propose a data-dependent batch allocation in PAGE estimator (Li et al., 2021) (see Corollary 2.2), which scales proportionally to the squared distance between successive iterates, similar to Arjevani et al. (2020). We inductively argue that the squared distance between successive iterates arising in the batch size of the estimator reduces at rate k12 in expectation. This allows us to further certify that the estimators do not only remain accurate, but their variance decreases as O( 2/k), where k is the iteration count.

In the context of the potential function argument, unlike in the deterministic settings, we do not establish that the potential function is non-increasing, even in expectation. The stochastic error terms that arise due to the stochastic nature of the operator evaluations are controlled by taking slightly smaller step sizes than in the vanilla methods from Diakonikolas (2020); Tran-Dinh and Luo (2021), which allows us to “leak” negative quadratic terms that are further used in controlling the stochastic error. The argument for controlling the value of the potential function is itself coupled with the inductive argument for ensuring that the expected operator norm remains bounded.

Finally, while applying a restarting strategy is standard under sharpness conditions (Roulet and d’Aspremont, 2020), obtaining the claimed stochastic oracle complexity result of O 1 2 log(1 ) requires a rather technical argument to bound the total number of stochastic queries to the operator.

#### 1.3 Related work

Monotone inclusion and variational inequalities. Variational inequality problems were originally devised to deal with approximating equilibria. Their systematic study was initiated by Stampacchia (1964). The relationship between

variational inequalities and min-max optimization was observed soon after Rockafellar (1970), while one of the earliest papers to study solving monotone inclusion as a generalization of variational inequalities, convex and min-max optimization, and complementarity problems is Rockafellar (1976). For a historical overview of this area and an extensive review of classical results, see Facchinei and Pang (2003).

In the case of monotone operators, standard variants of variational inequality problems (see Section 2) and monotone inclusion are equivalent—their solution sets coincide. This is a consequence of the celebrated Minty Theorem (Minty, 1962). However, there is a major difference between these problems when it comes to solving them to a ﬁnite accuracy. In particular, on unbounded domains, approximating variational inequalities is meaningless, whereas monotone inclusion remains well-deﬁned. This is most readily seen from the observation that mapping from min-max optimization, variational inequalities correspond to primal-dual gap guarantees, while monotone inclusion corresponds to a guarantee in gradient norm. For a simple bilinear function f(x,y) = xy which has the unique min-max solution at (x,y) = (0,0), the primal-dual gap is inﬁnite for any point other than (0,0), while the gradient remains ﬁnite and is a good proxy for measuring quality of a solution. Further, even on bounded domains or using restricted gap functions on unbounded domains as in e.g., Nesterov (2007), optimal oracle complexity guarantees for approximate monotone inclusion imply optimal complexity guarantees for approximately satisﬁed variational inequalities (see, e.g., Diakonikolas (2020)). The opposite does not hold in general. In particular, in deterministic settings, standard algorithms such as the celebrated extragradient (Korpelevich, 1977; Nemirovski, 2004), dual extrapolation (Nesterov, 2007), or Popov’s method (Popov, 1980) that have the optimal oracle complexity O(1 ) for approximating variational inequalities are suboptimal for monotone inclusion and attain oracle complexity of the order O( 1 2 ) (Golowich et al., 2020; Diakonikolas and Wang, 2022).

Halpern iteration. Halpern iteration is a classical ﬁxed point iteration originally introduced by Halpern (1967), and studied extensively in terms of both its asymptotic and non-asymptotic convergence guarantees (Wittmann, 1992; Leustean, 2007; Lieder, 2021; Kohlenbach, 2011; Kohlenbach and Leu¸stean, 2012; Cheval et al., 2022).. The ﬁrst tight nonasymptotic convergence rate guarantee of 1/t was obtained in Lieder (2021); Sabach and Shtern (2017). This rate was also matched by an alternative method proposed by Kim (2019).

The usefulness of Halpern iteration for solving monotone inclusion problems was ﬁrst observed by Diakonikolas (2020),1 who showed that its variants can be used to obtain near-optimal oracle complexity results for all standard classes of monotone inclusion problems with Lipschitz operators also studied in this work. The near-tightness (up to poly-logarithmic factors) of the results from Diakonikolas (2020) was certiﬁed using lower bound reductions from minmax optimization lower bounds introduced by Ouyang and Xu (2019). These lower bounds were made tight for the cocoercive setup in Diakonikolas and Wang (2022).

The generalization of Halpern iteration from the cocoercive to Lipschitz monotone setup in Diakonikolas (2020) utilized approximating what is known as the resolvent operator, which led to a double-loop algorithm and an additional log(1/ ) in the resulting complexity. This log factor was shaved off in Yoon and Ryu (2021), who introduced a two-step variant of Halpern iteration, inspired by the extragradient method of Korpelevich (1977). The results of Diakonikolas

- (2020); Yoon and Ryu (2021) were further extended to other classes of Lipschitz operators by Tran-Dinh and Luo
- (2021); Lee and Kim (2021). Except for Lee and Kim (2021) which considered controlled variance as discussed above, all of the existing results only targeted deterministic settings.


Stochastic settings and variance reduction. Vanilla stochastic gradient methods have constant variance of stochastic gradients, which creates a bottleneck in the convergence rate. To improve the convergence rate, in the past decade, powerful variance reduction techniques have been proposed.

For strongly convex ﬁnite-sum problems, SAG (Schmidt et al., 2017), which used a biased stochastic estimator of the full gradient, was the ﬁrst stochastic gradient method with a linear convergence rate. Johnson and Zhang (2013) and Defazio et al. (2014) improved Schmidt et al. (2017) by proposing unbiased estimators of SVRG-type and SAGA-type, respectively. Such unbiased estimators were further combined with Nesterov acceleration (Allen-Zhu, 2017; Song et al., 2020), or applied to nonconvex ﬁnite-sum/inﬁnite-sum problems (Reddi et al., 2016; Lei et al., 2017). For nonconvex stochastic (inﬁnite-sum) problems, SARAH (Nguyen et al., 2017) and SPIDER (Fang et al., 2018; Zhou et al., 2018a,b) estimators were proposed to attain the optimal oracle complexity of O(1/ 3) for ﬁnding an -approximate stationary point. Both estimators are referred to as “recursive” variance reduction estimators, as they are biased when taking expectation w.r.t. current randomness but unbiased w.r.t. all the randomness in history. PAGE (Li et al., 2021) and

1Interestingly, the algorithm proposed by Kim (2019) for cocoercive inclusion coincides with the Halpern iteration for a related nonexpansive operator (see Contreras and Cominetti (2021, Proposition 4.3)).

STORM (Cutkosky and Orabona, 2019) signiﬁcantly simpliﬁed SARAH and SPIDER in terms of reducing the number of loops and avoiding large minibatches, respectively. Arjevani et al. (2020) further extended this line of work by incorporating second-order information and dynamic batch sizes.

In the setting of min-max optimization and variational inequalities/monotone inclusion, variance reduction has primarily been used for approximating variational inequalities, corresponding to the primal-dual gap in min-max optimization; see, for example Palaniappan and Bach (2016); Alacaoglu and Malitsky (2022); Iusem et al. (2017); Chavdarova et al. (2019); Carmon et al. (2019); Loizou et al. (2021). Under strong monotonicity (or sharpness in the case of Loizou et al. (2021)), such results generalize to monotone inclusion; however, to the best of our knowledge, there have been no results that address monotone inclusion under the weaker assumptions considered in this work. In the context of monotone inclusion with Lipschitz operators, the tightest complexity result that we are aware of is O( 1 4 ), due to Diakonikolas et al. (2021), and it applies to a more general class of structured non-monotone Lipschitz operators, for the best iterate. The same oracle complexity can be deduced for the last iterate of a two-step variant of Halpern from Lee and Kim (2021, Theorem 6.1), using mini-batching. All the results in our work are also for the last iterate.

### 2 Preliminaries

We consider a real d-dimensional normed space (Rd, · ), where  ·  is induced by an inner product associated with the space, i.e.,  ·  =  ·,· . Let U ⊆ Rd be closed and convex; in the unconstrained case, U ≡ Rd. When U is bounded,

- D = maxu,v∈U u − v denotes its diameter.


##### Classes of monotone operators. We say that an operator F : Rd → Rd is

- 1. monotone, if ∀u,v ∈ Rd, F(u) − F(v),u − v ≥ 0.
- 2. L-Lipschitz continuous for some L > 0, if ∀u,v ∈ Rd, F(u) − F(v) ≤ L u − v .
- 3. γ-cocoercive for some γ > 0, if ∀u,v ∈ Rd, F(u) − F(v),u − v ≥ γ F(u) − F(v) 2 .
- 4. µ-strongly monotone for some µ > 0, if ∀u,v ∈ Rd, F(u) − F(v),u − v ≥ µ u − v 2 .


Note that we can easily specialize these deﬁnitions to the set U by restricting u,v to be from U. Throughout the paper, the minimum assumption that we make about an operator F is that it is monotone and

Lipschitz. Observe that any γ-cocoercive operator is monotone and γ1-Lipschitz. The converse to this statement does not hold in general.

##### Monotone inclusion and variational inequalities. Monotone inclusion asks for u∗ such that

0 ∈ F(u∗) + ∂IU(u∗), (MI) where IU is the indicator function of the set U and ∂IU(·) denotes the subdifferential of IU.

If F is continuous and monotone, the solution set to (MI) is the same as the solution set of the Stampacchia Variational Inequality (SVI) problem, which asks for u∗ ∈ U such that

(∀u ∈ U) : F (u∗),u − u∗ ≥ 0. (SVI)

Further, when F is monotone, the solution set of (SVI) is equivalent to the solution set of the Minty Variational Inequality (MVI) problem consisting in ﬁnding u∗ such that

(∀u ∈ U) : F(u),u∗ − u ≤ 0. (MVI)

We assume throughout the paper that a solution to monotone inclusion (MI) exists, which implies that solutions to both (SVI) and (MVI) exist as well. Existence of solutions follows from standard results and is guaranteed whenever e.g., U is compact, or, if there exists a compact set U such that Id − L1 F maps U to itself, where Id is the identity map (Facchinei and Pang, 2003). As remarked in the introduction, in unbounded setups it is generally not possible to approximate (MVI) and (SVI), whereas approximating (MI) is quite natural: we only need to ﬁnd u such that 0 ∈ F(u) + ∂IU(u) + B( ), where 0 denotes the zero vector and B( ) denotes the centered ball of radius .

Stochastic access to the operator. We consider the stochastic setting for monotone inclusion problems. More speciﬁcally, we make the following assumptions for stochastic queries to F. These assumptions are made throughout the paper, without being explicitly invoked.

- Assumption 1 (Unbiased samples with bounded variance). For each query point x ∈ U, we observe F(x,z) where z ∼ Pz is a random variable that satisﬁes the following assumptions:

Ez F(x,z) = F(x) and Ez F(x,z) − F(x) 2 ≤ σ2.

- Assumption 2 (Multi-point oracle). We can query a set of points (x1,...,xn) and receive F(x1,z),..., F(xn,z) where z ∼ Pz.
- Assumption 3 (Lipschitz in expectation). Ez F(u,z) − F(v,z) 2 ≤ L2 u − v 2, ∀u,v ∈ U.


We note that complexity results of the paper will bound the total number of queries made to this oracle. In particular, if multiple query points and/or multiple samples z are used in a single iteration, our complexity is given by the sum of all those queries throughout all iterations of the method. Also, Assumption 3 is primary with parameter L, by which F is also L-Lipschitz using Jensen’s inequality.

PAGE variance-reduced estimator. We now summarize a variant of the PAGE estimator, originally developed for smooth nonconvex optimization by Li et al. (2021), adapted to our setting. In particular, given queries to F, we deﬁne the variance reduced estimator F(uk) for k ≥ 1 by

 

S1(k) i=1 F(uk,zi(k)) w. p. pk,

1 S1(k)

(2.1)

F(uk) =

S2(k) i=1 F(uk,zi(k)) − F(uk−1,zi(k)) w. p. 1 − pk,



F(uk−1) + 1

S2(k)

where p0 = 1, zi(k) i.i.d.∼ Pz, and S1(k) and S2(k) are the sample sizes at iteration k. Observe that Assumption 2 guarantees that we can query F at uk and uk−1 using the same random seed. Our analysis will make use of conditional expectations, and to that end, we deﬁne natural ﬁltration Fk by Fk := σ({ F(uj)}j≤k); namely Fk contains all the randomness that arises in the deﬁnitions of F(uj) for j ≤ k. Following a similar argument as in Li et al. (2021), we recursively bound the variance of the estimator F, as summarized in the following lemma. The proof is provided in Appendix A.

Lemma 2.1. Let F be a monotone operator accessed via stochastic queries F, under Assumptions 1–3. Then, the variance of F deﬁned by Eq. (2.1) satisﬁes the following recursive bound: for all k ≥ 1,

L2 uk − uk−1 2 S2(k)

pkσ2 S1(k)

E[ F(uk) − F(uk) 2] ≤

+ (1 − pk) E[ F(uk−1) − F(uk−1) 2] + E

.

With the choices of pk,S1(k),S2(k) speciﬁed in the following corollary and using induction with the inequality from

- Lemma 2.1, we obtain the following bound on the variance.


2 uk−uk−1 2

2

- Corollary 2.2. Given a target error > 0, if for all k ≥ 1, pk = k+12 ,S1(k) ≥ 8σ


pk 2 ,S2(k) ≥ 8L

p2k 2 , then

- E F(uk) − F(uk) 2 ≤


2

k .

### 3 Stochastic Halpern Iteration for Cocoercive Operators

In this section, we consider the setting of L1 -cocoercive operators F. While cocoercivity is a strong assumption that implies that an operator is both Lipschitz and monotone (as discussed in Section 2), it is nevertheless the most basic

setup for studying the Halpern iteration. In particular, while Halpern iteration can be applied directly to the nonexpansive counterpart of a cocoercive operator F (i.e., to the linear transformation Id − L2 F, where L1 is an upper bound on the cocoercivity parameter of F), convergence does not seem possible to establish for the more general class of Lipschitz monotone operators. We begin this section by providing a generic proof of stochastic oracle complexity, which we then

use to brieﬂy illustrate how to obtain O( 1 4 ) oracle complexity with a simple minibatch stochastic estimator of F. We then show how to improve this bound to O( 1 3 ) by applying the proposed variant of the PAGE estimator from Eq. (2.1) to Halpern iteration.

The stochastic variant of Halpern iteration that we consider is deﬁned by

uk+1 = λk+1u0 + (1 − λk+1) uk −

2 Lk+1

F(uk) , (3.1)

where F is a stochastic (possibly biased) estimator of F, λk+1 = Θ(k1) is the step size, and Lk+1 ≥ L is a parameter of the algorithm. Compared to the classical iteration uk+1 = λk+1u0 + (1 − λk+1)T(uk), where T : Rd → Rd

is a nonexpansive (1-Lipschitz) map (Halpern, 1967), T is replaced by the mapping Id − L 2

F, which is stochastic

k+1

and may not be nonexpansive (as the stochastic estimate F of F is not guaranteed to be cocoercive even when F is). Compared to the iteration variant considered by Diakonikolas (2020), the access to the monotone operator is stochastic and we also take slightly larger (by a factor of 2) values of Lk+1 to bound the stochastic error terms.

Our argument for bounding the total number of stochastic queries to F is based on the use of the following potential function Ck = A

Lk F(uk) 2 + Bk F(uk),uk − u0 , where {Ak}k≥1 and {Bk}k≥1 are positive and non-decreasing sequences of real numbers, while the step size λk is deﬁned by λk := B

k

Ak+Bk . Such potential function was previously used for the deterministic case of Halpern iteration in Diakonikolas (2020); Diakonikolas and Wang (2022). Observe that even though we make oracle queries to F, the potential function Ck and the ﬁnal bound we obtain are in terms of the true operator value F.

k

Compared to the analysis of Halpern iteration in the deterministic case (Diakonikolas, 2020; Diakonikolas and Wang,

- 2022), our analysis for the stochastic case needs to account for the error terms caused by accessing F via stochastic queries and is based on an intricate inductive argument. A generic bound on iteration complexity, under mild assumptions about the estimator F, is summarized in Theorem 3.1. The proof is in Appendix B.


Theorem 3.1. Given an arbitrary u0 ∈ Rd, suppose that iterates uk evolve according to Halpern iteration from Eq. (3.1) for k ≥ 1, where Lk = 2L and λk = k+11 . Assume further that the stochastic estimate F(u) is unbiased for u = u0 and E[ F(u0) − F(u0) 2] ≤

8 . Given > 0, if for all k ≥ 1, we have that E F(uk) − F(uk) 2 ≤

2

2

k , then for all k ≥ 1,

Λ0 k

+ Λ1 , (3.2)

E[ F(uk)) ] ≤

where Λ0 = 76L u0 − u∗ and Λ1 = 4 23. As a result, stochastic Halpern iteration from Eq. (3.1) returns a point uk such that E[ F(uk) ] ≤ 4 after at most N = 2Λ

0−u∗ iterations.

= O L u

0

We remark that the previous result states an iteration complexity bound under a rather high accuracy assumption for the operator estimators at each iteration. In order to attain these accuracy requirements, we could either use a minibatch at every iteration, or use variance reduction. In what follows we explore both approaches. We further remark that we made no effort to optimize the constants in the bound above, and thus the constants are likely improvable.

2

k , we can certify by Chebyshev bound that P[ F(uk) − F(uk) ≥ ] ≤ k1. In particular, after O(1 ) iterations, if we have F ˜(uk) ≤ (which holds in expectation), then F(uk) is also O( ) with probability at least 1− . This is particularly important for practical implementations, where a stopping criterion can be based on the value of F(uk) , which, unlike F(uk) , can be efﬁciently evaluated.

Finally, observe that due to the required low error for the estimates E[ F(uk) − F(uk) 2] ≤

#### 3.1 Stochastic Oracle Complexity With a Simple Mini-batch Estimate

Sk i=1 F(uk,zi(k)) leads to the overall

A direct consequence of Theorem 3.1 is that a simple estimator F(uk) = S1

k

O( 1 4) oracle complexity, as stated in the following corollary of Theorem 3.1.

Sk i=1 F(uk,zi(k)), where F(uk,zi(k)) satisﬁes

- Corollary 3.2. Under the assumptions of Theorem 3.1, if F(uk) = S1


k

Assumption 1 and zi(k) i.i.d.∼ Pz, then setting Sk = σ

2(k+1)

2 for all k ≥ 0 guarantees that E[ F(uk) ] ≤ 4 after at most O σ

2L2 u0−u∗ 2

4 queries to F.

Proof. The averaged operator from the theorem statement is unbiased, by Assumption 1. Further, as by Assumption 1,

2

2

F(uk) − F(uk,zi(k)) 2 ≤ σ2, it immediately follows that F(uk) − F(uk) 2 ≤ σ

k+1. Applying Theorem 3.1, the total number of iterations N of Halpern iteration until E[ F(uN) ] ≤ 4 is N = O(L u

Sk =

0−u∗ ). To complete the proof, it remains to bound the total number of oracle queries F to F, which is simply Nk=0 Sk = O N

2σ2

2 = O σ

2L2 u0−u∗ 2

4 .

| |
|---|


- 3.2 Improved Oracle Complexity via Variance Reduction We now consider using the recursive variance reduction method from Eq. (2.1) to obtain the variance bound required in


- Theorem 3.1. The algorithm with all its corresponding parameter settings is summarized in Algorithm 1. Of course, in practice, u0 − u∗ is not known, and instead of running the algorithm for a ﬁxed number of iterations N, one could


run it, for example, until reaching a point with F(uk) ≤  . Notice that convergence is guaranteed by Theorem 3.1; however it does not directly address the problem of the oracle complexity (as batch sizes depend on successive iterate distances). To resolve this issue, we ﬁrst provide a bound on uk − uk−1 .

Algorithm 1: Stochastic Halpern-Cocoercive Input u0 ∈ Rd, u0 − u∗ , L, > 0, σ; Initialization: Λ0 = 76L u

0−u∗ , N = 2Λ

2

, S1(0) = 8σ

2 ; F(u0) = 1

0

S1(0) i=1 F(u0,zi(0));

S1(0)

for k = 1 : N do

uk = k+11 u0 + k+1k uk−1 − L1 F(uk−1) ; pk = k+12 , S1(k) = 8σ

2 uk−uk−1 2

2

pk 2 , S2(k) = 8L

pk2 2 ; Compute F(uk) based on Eq. (2.1)

end Return: uN

- Lemma 3.3. Given an arbitrary initial point u0 ∈ Rd, let {uk}k≥1 be the sequence of points produced by Algorithm 1. Assume further that λk = k+11 , Lk = 2L for all k ≥ 0. Then,


- 1

4L2 F(u0) 2 if k = 1,

- 2k2


uk − uk−1 2 ≤

(3.3)

2

L2(k+1)2 F(uk−1) 2 + ki=0−2 2(i+1)

k(k+1)2L2 F(ui) 2 if k ≥ 2.

Moreover, if for 1 ≤ i ≤ k − 1, all of the following conditions hold (same as in Theorem 3.1): (i) E[ F(ui) ] ≤ Λ0

i + Λ1 , where Λ0 = 76L u0 − u∗ and Λ1 = 4 23, (ii) E F(ui) − F(ui) 2 ≤

2

i , and (iii) ≤ Λ

k , then E[ uk − uk−1 2] = O u

0

0−u∗ 2

k2 .

Proof. For k = 1, u1 = 12u0 + 12 u0 − L1 F(u0) , which leads to u1 − u0 2 = −21L F(u0) 2 = 4L12 F(u0) 2. For k ≥ 2, recursively applying Eq. (3.1), we have uk − uk−1 = λk(u0 − uk−1) − 1−λ

L F(uk−1) = λk(1 − λk−1)(u0 − uk−2) + λ

k

k(1−λk−1)

L F(uk−2) − 1−λ

L F(uk−1), leading to

k

k−2

k−1

1 − λk L

λk L

(1 − λj) F(ui).

uk − uk−1 = −

F(uk−1) +

i=0

j=i+1

2

Recalling that λk = k+11 , we have uk − uk−1 2 = −L(kk+1) F(uk−1) + ki=0−2 k(ki+1+1)L F(ui)

, which gives us Inequality (3.3) by applying a generalized variant of Young’s inequality Ki=1 Xi

2

≤ Ki=1 K Xi 2 twice (ﬁrst to the sum of −L(kk+1) F(uk−1) and the summation term, then to the summation term, while noticing that k−1

k ≤ 1).

For the second claim, by the lemma assumptions and the analysis in the proof for Theorem 3.1, we have E[ F(ui) 2] = O(L

2 u0−u∗ 2

2 u0−u∗ 2

i2 ) for i ≤ k−1 ≤ O 1 , thus E[ F(ui) 2] ≤ 2E[ F(ui) ]2+2E[ F(ui) − F(ui) 2] = O(L

i2 ). Plugging this bound into Inequality (3.3), we get E[ uk − uk−1 2] = O( u

0−u∗ 2

k2 ).

| |
|---|


Using Lemma 3.3 and making the appropriate parameter settings for the estimator from Eq. (2.1), it is now possible to apply Theorem 3.1 to obtain the improved O( 1 3 ) stochastic oracle complexity bound, as stated in the following corollary of Theorem 3.1.

- Corollary 3.4. Given arbitrary u0 ∈ Rd and > 0, consider uN returned by Algorithm 1. Then, E[ F(uN) ] ≤ 4


2L u0−u∗ +L3 u0−u∗ 3

with expected O(σ

3 ) oracle queries to F.

Proof. Let mk be the number of stochastic queries made by the estimator from Eq. (2.1) in iteration k. Using Corollary 2.2, we have

2 uk−uk−1 2

2

E mk+1|Fk−1 = pkS1(k) + 2(1 − pk)S2(k) = pk 8σ

pk 2 + 2(1 − pk) 8L

p2k 2 ,

where the ﬁrst equality holds because S2(k) is measurable w.r.t. Fk−1 and the only random choice that remains is the selection of the estimator in Eq. (2.1) determined by probabilities pk and 1 − pk.

Taking expectation with respect to all randomness on both sides, rearranging the terms, and using the fact that x ≤

k)L2E[ uk−uk−1 2]

2

2 + 16(1−p

- x + 1 for any x ∈ R, we obtain E[mk+1] ≤ 8σ


p2k 2 + 2. Recalling that pk = k+12 = O(k1) and E[ uk − uk−1 2] = O u

0−u∗ 2

2+L2 u0−u∗ 2

k2 by Lemma 3.3, it follows that E[mk+1] = O σ

2 . As, by Theorem 3.1, the total number of iterations to attain 4 norm of the operator in expectation is N = 2Λ

0−u∗ and m0 = S1(0) = O σ

= O L u

0

2L u0−u∗ +L3 u0−u∗ 3

2

2 , the total number of queries to F is E[M] = E[ Nk=1 mk] = O σ

3 .

| |
|---|


We note in passing that the running time guarantee of this algorithm is of Las Vegas-type: despite its iteration number being surely bounded by 2Λ0

0−u∗ , the batch sizes (in particular S2(k)) are random, and are not universally bounded.

= O L u

We further argue that Algorithm 1 can be extended to constrained settings by deﬁning the operator mapping as in Diakonikolas (2020) and modifying the variance-reduced stochastic estimator accordingly based on the projection of

- F. We show that the newly deﬁned operator mapping is also cocoercive while the variance of the modiﬁed estimator is bounded by the variance of F, so arguments from Theorem 3.1 and Corollary 3.4 extend to this case. This modiﬁed estimator need not be unbiased (as neither is F); however, this is irrelevant to our analysis as it does not require unbiasedness. For completeness, a detailed extension to the constrained case is provided in Appendix B.2.


### 4 Monotone and Lipschitz Setup

Throughout this section, we assume that F is monotone and L-Lipschitz. While the previous section addresses the cocoercive setup using the classical version of Halpern iteration adapted to cocoercive operators, it is unclear how to directly generalize this result to the setting with monotone Lipschitz operators. In the deterministic setting, generalization to monotone Lipschitz operators can be achieved through the use of a resolvent operator (see Diakonikolas (2020)). However, such an approach incurs an additional log(1/ ) factor in the iteration complexity coming from approximating the resolvent and it is further unclear how to generalize it to stochastic settings, as the properties of the stochastic estimate F of F do not readily translate into the same or similar properties for the resolvent of F. Instead of taking the approach based on the resolvent, we consider a recently proposed two-step variant of Halpern iteration (Tran-Dinh and Luo, 2021), adapted here to the stochastic setting. The variant uses extrapolation and is deﬁned by

vk := λku0 + (1 − λk)uk − ηkF(vk−1), uk+1 := λku0 + (1 − λk)uk − ηk F(vk),

(4.1)

where λk ∈ [0,1), ηk > 0, and F is deﬁned by (2.1). The resulting algorithm with a complete parameter setting is provided in Algorithm 2.

To analyze the convergence of the extrapolated Halpern variant from Eq. (4.1), we use the potential function Vk = Ak F(uk) 2 +Bk F(uk),uk − u0 +ckL2 uk −vk−1 2, previously used by Tran-Dinh and Luo (2021), where Ak,

Algorithm 2: Extrapolated Stochastic Halpern-Monotone (E-Halpern) Input: u0 ∈ Rd, u0 − u∗ , 0 < η0 ≤ 3√13L, L, > 0, σ; Initialize: v−1 = u0, S1(−1) = S1(0) = 8σ

2 0)

2

2 , M = 9L2, η = η0(1−2Mη

1−Mη02 ; Set Λ0 = 4(L

√ √ΛΛ10 ; F(v−1) = 1

2η0η+1) u0−u∗ 2

(1+Mηη0) Mη2 , N =

η2 , Λ1 = 5

S1(−1) i=1 F(v−1,zi(−1)), where zi(−1) i.i.d.∼ Pz;

S1(−1)

for k = 1 : N do vk−1 = k+11 u0 + k+1k uk−1 − ηk−1 F(vk−2); pk−1 = min(k2,1), S1(k−1) = 8σ

2 vk−1−vk−2 2

2

pk−1 2 , S2(k−1) = 8L

pk−12 2 ;

Compute F(vk−1) based on Eq. (2.1); uk = k+11 u0 + k+1k uk−1 − ηk−1 F(vk−1); ηk = (1−

1 (k+1)2 −Mηk−12)(k+1)2 (1−Mηk−12)k(k+2) ηk−1

##### end Return: uN

Bk and ck are positive parameters to be determined later. Observe that this is essentially the same potential function as Ck, corrected by the quadratic term ckL2 uk − vk−1 2 to account for error terms appearing in the analysis of the two-step variant from Eq. (4.1). Similarly as in the cocoercive setup, the potential function is not monotonically nonincreasing, due to the error terms that arise due to the stochastic access to F. Bounding these error terms requires a careful technical argument, and is the main technical contribution of this section. Due to space constraints, the complete technical argument is deferred to Appendix C, while the main results are stated below.

- Theorem 4.1. Given an arbitrary initial point u0 ∈ Rd and target error > 0, assume that the iterates uk evolve according to Algorithm 2 for k ≥ 1. Then, for all k ≥ 2,

E F(uk) 2 + 2L2 uk − vk−1 2 ≤

Λ0 (k + 1)(k + 2)

+ Λ1 2, (4.2)

where Λ0 = 4(L

2η0η+1) u0−u∗ 2

η2 and Λ1 = 5

(1+Mηη0)

Mη2 . In particular, E F(uN) 2 + 2L2 uN − vN−1 2 ≤ 2Λ1 2 = O( 2) after at most N =

√ √ΛΛ10 = O L u

0−u∗ iterations. The total number of oracle queries to F is O σ

2L u0−u∗ +L3 u0−u∗ 3

3 in expectation.

5 Faster Convergence Under a Sharpness Condition

We now show that by restarting Algorithm 2, we can achieve the O 1 2 log 1 oracle complexity under a milder than strong monotonicity µ-sharpness condition: for all u ∈ U, F(u) − F(u∗),u − u∗ ≥ µ u − u∗ 2. The scheme is summarized in Algorithm 3, and the proof is deferred to Appendix D.

- Theorem 5.1. Given F that is L-Lipschitz and µ-sharp and the precision parameter , Algorithm 3 outputs uN with


0−u∗ iterations with at most O σ

E[ uN − u∗ 2] ≤ 2 as well as E F(uN) 2 ≤ L2 2 after N = O Lµ log u

2(µ+L) log( u0−u∗ / )+L3 u0−u∗ 2

µ3 2 queries to F in expectation.

### 6 Numerical experiments and discussion

We now illustrate the empirical performance of stochastic Halpern iteration on robust least square problems. Speciﬁcally, given data matrix A ∈ Rn×d and noisy observation vector b ∈ Rn subject to bounded deterministic perturbation δ with δ ≤ ρ, robust least square (RLS) minimizes the worst-case residue as minx∈Rd maxδ: δ ≤ρ Ax − y 22 with

Algorithm 3: Restarted Extrapolated Stochastic Halpern-Sharp (Restarted E-Halpern)

Input: v−1 = u0 ∈ Rd, u0 − u∗ , 0 < η0 ≤ 3√13L, L, µ, > 0, σ; Initialize: M = 9L2, η = η0

√6 u0−u∗

(1−2Mη02) 1−Mη02 , N = log

2 ; for k = 1 : N do

√

Mη2

Call Algorithm 2 with initialization v−(k1) = u(0k) = uk−1, k = µ 

2

, and S1(−1) = S1(0) = 8σ

,

2 k

2 5(1+Mηη0)

√

L2η0η+1

for K = 4

µη iterations, and return uk;

end Return: uN

- y = b + δ (El Ghaoui and Lebret, 1997). We consider solving MI induced from RLS with Lagrangian relaxation


where u = (x,y)T and F(u) = ∇xLλ(x,y),−∇yLλ(x,y) T for Lλ(x,y) = 21n Ax − y 22 − 2λn y − b 22. We use a real-world superconductivity dataset (Hamidieh, 2018) from UCI Machine Learning Repository (Dua and Graff,

2017) for our experiment, which is of size 21263 × 81. To ensure the problem is concave in y, we need that λ > 1; in the experiments, we set λ = 1.5. For the experiment, we compare Halpern, E-Halpern, and Restarted E-Halpern

![image 1](<2022-cai-stochastic-halpern-iteration-variance_images/imageFile1.png>)

![image 2](<2022-cai-stochastic-halpern-iteration-variance_images/imageFile2.png>)

(a) Comparison on superconductivity dataset. (b) E-Halpern with different stochastic estimators.

Figure 1: Empirical comparison of min-max algorithms on the robust least squares problem.

algorithms with gradient descent-ascent (GDA), extragradient (EG) (Korpelevich, 1977), and Popov’s method (Popov, 1980) in stochastic settings. Even though our theoretical results for Restarted E-Halpern require scheduled restarts based on known problem parameters, in the implementation, to avoid complicated parameter tuning and illustrate empirical performance, we restart E-Halpern whenever the norm of stochastic estimator F used in E-Halpern halves. All Halpern variants are implemented with PAGE estimator considered in our paper; all other algorithms are implemented using minibatches. Additionally, we compare E-Halpern with the PAGE estimator against E-Halpern with single-sample and mini-batch estimators.

We report and plot the (empirical) operator norm F(u) against the number of stochastic operator evaluations. Note that evaluations of F(u) are only used for plotting but not for running any of the algorithms. We use the same random initialization and tune the batch sizes and step sizes (to the values achieving fastest convergence under noise) for each method by grid search. We use constant batch sizes and constant step sizes for GDA, EG, and Popov. We also choose the batch sizes of PAGE estimator to ensure E[ F(uk) − F(uk) 2] ≤ O(k1), which handles error accumulation (Lee and Kim, 2021) and early stagnation of stochastic Halpern iteration. We implement all the algorithms in Python and run each algorithm using one CPU core on a macOS machine with Intel 2.3GHz Dual Core i5 Processor and 8GB RAM.2

We observe that (i) in Figure 1(a) both Halpern and E-Halpern exhibit faster convergence to approximate stationary

2Code is available at https://github.com/zephyr-cai/Halpern.

points (with much smaller gradient norm after same number of gradient evaluations) than other algorithms, and restarting E-Halpern provides additional speedup, validating our theoretical insights; (ii) in Figure 1(b), E-Halpern with PAGE estimator displays faster convergence compared to other two estimators, in agreement with our theoretical analysis.

### 7 (Near) Tightness of Stochastic Oracle Complexity Bounds

In this section, we brieﬂy discuss lower bound reductions which imply that our results for Lipschitz sharp setups are unimprovable in terms of the dependence on  . To keep the discussion simple, we only focus on the dependence here and unconstrained settings. The near-optimality of our bounds is implied by the known lower bound for the optimality gap in L-smooth µ-strongly convex stochastic optimization, which is of the order Ω(σ

2

µ ) in the high noise σ2 or low error regimes; see, for example, the discussion in Ghadimi and Lan (2016) (the omitted part of the lower bound comes from the deterministic complexity of smooth strongly convex optimization and is less interesting in our context). The same lower bound implies a lower bound of Ω(σ

2

2 ) for minimizing the gradient of a smooth strongly convex function f. Suppose not (for the purpose of contradiction); i.e., suppose that there were an algorithm that constructs a point x with E[ ∇f(x) 2] ≤ ¯ 2 in o(σ

2

¯ 2 ) oracle queries to the stochastic gradient. By µ-strong convexity of f, this would imply that we get E[f(x) − minu f(u)] ≤ 21µE[ ∇f(x) 2] ≤ ¯

2

2

¯ 2 ) oracle queries to the stochastic gradient. Setting ¯ = √ µ, we get that this would imply oracle complexity o(σ

2µ with o(σ

2

µ ), and we reach a contradiction on the lower bound for the optimality gap.

2 2 ) lower bound applies to the minimization of the gradient of smooth strongly convex functions in stochastic regimes. Observe that the gradients of smooth strongly convex functions are Lipschitz and strongly monotone (thus also sharp), so a lower bound for this problem class implies a lower bound for the class of sharp Lipschitz monotone inclusion problems. Thus, we can conclude that our result from Section 5 for sharp Lipschitz monotone inclusion problems that gives O σ

Hence, Ω(σ

2(µ+L) log( u0−u∗ / )+L3 u0−u∗ 2

µ3 2 stochastic oracle complexity is near-optimal in terms of the dependence on σ and (but likely not near-optimal in terms of the dependence on the remaining problem parameters).

### 8 Conclusion

We introduced stochastic variance reduced variants of Halpern iteration for addressing monotone inclusion problems. Our work addresses all standard classes of Lipschitz monotone problems and achieves improved stochastic oracle complexity guarantees, all for the last iterate. Subsequent to this work, Chen and Luo (2022) obtained near-optimal bounds for the cases considered in this work, by reducing the Lipschitz monotone case to the Lipschitz strongly monotone case, using regularization. It is an open question to obtain such near-optimal bounds with a direct method, without the use of regularization.

### Acknowledgements

XC and CS were supported in part by the NSF grant 2023239. CG’s research was partially supported by INRIA Associate Teams project, FONDECYT 1210362 grant, ANID Anillo ACT210005 grant, and National Center for Artiﬁcial Intelligence CENIA FB210017, Basal ANID. Part of this work was done while CG was at the University of Twente. JD was supported by the NSF grant 2007757, by the Ofﬁce of Naval Research under contract number N00014-22-1-2348, and by the Wisconsin Alumni Research Foundation. Part of this work was done while JD and CS were visiting Simons Institute for the Theory of Computing.

### References

Ahmet Alacaoglu and Yura Malitsky. Stochastic variance reduction for variational inequality methods. In Proc. COLT’22, 2022.

Zeyuan Allen-Zhu. Katyusha: The ﬁrst direct acceleration of stochastic gradient methods. The Journal of Machine Learning Research, 18(1):8194–8244, 2017.

Yossi Arjevani, Yair Carmon, John C Duchi, Dylan J Foster, Ayush Sekhari, and Karthik Sridharan. Second-order

information in non-convex stochastic optimization: Power and limitations. In Proc. COLT’20, 2020. Amir Beck. First-order methods in optimization, volume 25. SIAM, 2017. Yair Carmon, Yujia Jin, Aaron Sidford, and Kevin Tian. Variance reduction for matrix games. In Proc. NeurIPS’19,

2019. Tatjana Chavdarova, Gauthier Gidel, Franc¸ois Fleuret, and Simon Lacoste-Julien. Reducing noise in GAN training with variance reduced extragradient. In Proc. NeurIPS’19, 2019. Lesi Chen and Luo Luo. Near-optimal algorithms for making the gradient small in stochastic minimax optimization. arXiv preprint arXiv:2208.05925, 2022. Horatiu Cheval, Ulrich Kohlenbach, and Laurentiu Leustean. On modiﬁed Halpern and Tikhonov-Mann iterations. arXiv preprint arXiv:2203.11003, 2022. Juan Pablo Contreras and Roberto Cominetti. Optimal error bounds for nonexpansive ﬁxed-point iterations in normed spaces. arXiv preprint, arXiv:2108.10969, 2021. Ashok Cutkosky and Francesco Orabona. Momentum-based variance reduction in non-convex SGD. In Proc. NeurIPS’19, 2019. Aaron Defazio, Francis Bach, and Simon Lacoste-Julien. SAGA: A fast incremental gradient method with support for non-strongly convex composite objectives. In Proc. NeurIPS’14, 2014. Jelena Diakonikolas. Halpern iteration for near-optimal and parameter-free monotone inclusion and strong solutions to variational inequalities. In Proc. COLT’20, 2020. Jelena Diakonikolas and Puqian Wang. Potential function-based framework for minimizing gradients in convex and min-max optimization. SIAM Journal on Optimization, 32(3):1668–1697, 2022. Jelena Diakonikolas, Constantinos Daskalakis, and Michael Jordan. Efﬁcient methods for structured nonconvexnonconcave min-max optimization. In Proc. AISTATS’21, 2021. Dheeru Dua and Casey Graff. UCI Machine Learning Repository, 2017. URL http://archive.ics.uci.edu/ ml. Laurent El Ghaoui and Herv´e Lebret. Robust solutions to least-squares problems with uncertain data. SIAM Journal on Matrix Analysis and Applications, 18(4):1035–1064, 1997. Francisco Facchinei and Jong-Shi Pang. Finite-dimensional variational inequalities and complementarity problems. Springer Science & Business Media, 2003. Cong Fang, Chris Junchi Li, Zhouchen Lin, and Tong Zhang. Spider: Near-optimal non-convex optimization via stochastic path-integrated differential estimator. In Proc. NeurIPS’18, 2018. Saeed Ghadimi and Guanghui Lan. Accelerated gradient methods for nonconvex nonlinear and stochastic programming. Mathematical Programming, 156(1-2):59–99, 2016. Noah Golowich, Sarath Pattathil, Constantinos Daskalakis, and Asuman Ozdaglar. Last iterate is slower than averaged iterate in smooth convex-concave saddle point problems. In Proc. COLT’20, 2020. Benjamin Halpern. Fixed points of nonexpanding maps. Bulletin of the American Mathematical Society, 73(6):957–961, 1967. Kam Hamidieh. A data-driven statistical model for predicting the critical temperature of a superconductor. Computational Materials Science, 154:346–354, 2018. Alfredo N Iusem, Alejandro Jofr´e, Roberto Imbuzeiro Oliveira, and Philip Thompson. Extragradient method with variance reduction for stochastic variational inequalities. SIAM Journal on Optimization, 27(2):686–724, 2017.

Rie Johnson and Tong Zhang. Accelerating stochastic gradient descent using predictive variance reduction. In Proc. NeurIPS’13, 2013.

Donghwan Kim. Accelerated proximal point method and forward method for monotone inclusions. arXiv preprint arXiv:1905.05149, 2019.

Ulrich Kohlenbach. On quantitative versions of theorems due to F.E. Browder and R. Wittmann. Advances in Mathematics, 226(3):2764–2795, 2011.

Ulrich Kohlenbach and Lauren¸tiu Leu¸stean. Effective metastability of Halpern iterates in CAT(0) spaces. Advances in

Mathematics, 231(5):2526–2556, 2012. GM Korpelevich. Extragradient method for ﬁnding saddle points and other problems. Matekon, 13(4):35–49, 1977. Sucheol Lee and Donghwan Kim. Fast extra gradient methods for smooth structured nonconvex-nonconcave minimax

problems. In Proc. NeurIPS’21, 2021. Lihua Lei, Cheng Ju, Jianbo Chen, and Michael I Jordan. Non-convex ﬁnite-sum optimization via SCSG methods. In Proc. NeurIPS’17, 2017. Laurentiu Leustean. Rates of asymptotic regularity for Halpern iterations of nonexpansive mappings. Journal of Universal Computer Science, 13(11):1680–1691, 2007. Zhize Li, Hongyan Bao, Xiangliang Zhang, and Peter Richt´arik. PAGE: A simple and optimal probabilistic gradient

estimator for nonconvex optimization. In Proc. ICML’21, 2021. Felix Lieder. On the convergence rate of the Halpern-iteration. Optimization Letters, 15(2):405–418, 2021. Nicolas Loizou, Hugo Berard, Gauthier Gidel, Ioannis Mitliagkas, and Simon Lacoste-Julien. Stochastic gradient

descent-ascent and consensus optimization for smooth games: Convergence analysis under expected co-coercivity. In Proc. NeurIPS’21, 2021.

George J Minty. Monotone (nonlinear) operators in Hilbert space. Duke Mathematical Journal, 29(3):341–346, 1962. Arkadi Nemirovski. Prox-method with rate of convergence O(1/t) for variational inequalities with Lipschitz continuous

monotone operators and smooth convex-concave saddle point problems. SIAM Journal on Optimization, 15(1):229– 251, 2004.

Yurii Nesterov. Dual extrapolation and its applications to solving variational inequalities and related problems. Mathematical Programming, 109(2-3):319–344, 2007.

Lam M Nguyen, Jie Liu, Katya Scheinberg, and Martin Tak´aˇc. SARAH: A novel method for machine learning problems using stochastic recursive gradient. In Proc. ICML’17, 2017.

Yuyuan Ouyang and Yangyang Xu. Lower complexity bounds of ﬁrst-order methods for convex-concave bilinear saddlepoint problems. Mathematical Programming, Aug 2019.

Balamurugan Palaniappan and Francis Bach. Stochastic variance reduction methods for saddle-point problems. In

Proc. NeurIPS’16, 2016. Jong-Shi Pang. Error bounds in mathematical programming. Mathematical Programming, 79(1):299–332, 1997. L. D. Popov. A modiﬁcation of the Arrow-Hurwicz method for search of saddle points. Mathematical notes of the

Academy of Sciences of the USSR, 28(5):845–848, Nov 1980. Sashank J Reddi, Ahmed Hefny, Suvrit Sra, Barnabas Poczos, and Alex Smola. Stochastic variance reduction for nonconvex optimization. In Proc. ICML’16, 2016. R Tyrrell Rockafellar. Monotone operators associated with saddle-functions and minimax problems. Nonlinear Functional Analysis, 18(part 1):397–407, 1970.

R Tyrrell Rockafellar. Monotone operators and the proximal point algorithm. SIAM Journal on Control and Optimization, 14(5):877–898, 1976.

Vincent Roulet and Alexandre d’Aspremont. Sharpness, restart, and acceleration. SIAM Journal on Optimization, 30

(1):262–289, 2020. Shoham Sabach and Shimrit Shtern. A ﬁrst order method for solving convex bilevel optimization problems. SIAM Journal on Optimization, 27(2):640–660, 2017. Mark Schmidt, Nicolas Le Roux, and Francis Bach. Minimizing ﬁnite sums with the stochastic average gradient. Mathematical Programming, 162(1):83–112, 2017. Chaobing Song, Yong Jiang, and Yi Ma. Variance reduction via accelerated dual averaging for ﬁnite-sum optimization. In Proc. NeurIPS’20, 2020. Guido Stampacchia. Formes bilineaires coercitives sur les ensembles convexes. Acad´emie des Sciences de Paris, 258: 4413–4416, 1964. Quoc Tran-Dinh and Yang Luo. Halpern-type accelerated and splitting algorithms for monotone inclusions. arXiv preprint arXiv:2110.08150, 2021. Rainer Wittmann. Approximation of ﬁxed points of nonexpansive mappings. Archiv der Mathematik, 58(5):486–491, 1992. Taeho Yoon and Ernest K Ryu. Accelerated algorithms for smooth convex-concave minimax problems with O(1/k2) rate on squared gradient norm. In Proc. ICML’21, 2021. Dongruo Zhou, Pan Xu, and Quanquan Gu. Finding local minima via stochastic nested variance reduction. arXiv preprint arXiv:1806.08782, 2018a. Dongruo Zhou, Pan Xu, and Quanquan Gu. Stochastic nested variance reduction for nonconvex optimization. In Proc. NeurIPS’18, 2018b.

### A Omitted proofs from Section 2

Lemma 2.1. Let F be a monotone operator accessed via stochastic queries F, under Assumptions 1–3. Then, the variance of F deﬁned by Eq. (2.1) satisﬁes the following recursive bound: for all k ≥ 1,

pkσ2 S1(k)

L2 uk − uk−1 2 S2(k)

E[ F(uk) − F(uk) 2] ≤

+ (1 − pk) E[ F(uk−1) − F(uk−1) 2] + E

.

Proof. Using the deﬁnition of F, conditional on Fk−1, we have for all k ≥ 1

2

E F(uk) − F(uk)

Fk−1

S1(k)

2

1 S1(k)

F(uk,zi(k)) − F(uk)

= pkE

Fk−1

i=1

S2(k)

1 S2(k)

F(uk,zi(k)) − F(uk−1,zi(k)) − F(uk)

+ (1 − pk)E F(uk−1) +

i=1

2

Fk−1 ,

where Fk−1 = σ({ F(uj)}j≤k−1) is the natural ﬁltration, as deﬁned in Section 2. Note that both uk−1 ∈ Fk−1 and uk ∈ Fk−1 by the updating scheme considered in this paper, so we have

2

E F(uk) − F(uk)

Fk−1

S1(k)

2

1 S1(k)

F(uk,zi(k)) − F(uk)

= pk Ez(k)

i=1

(A.1)

T1

S2(k)

2

1 S2(k)

F(uk,zi(k)) − F(uk−1,zi(k)) − F(uk)

+ (1 − pk)Ez(k) F(uk−1) +

.

i=1

T2

Here we use Ez(k) to denote taking expectation with respect to the randomness of random seeds zi(k) i.i.d.∼ Pz sampled at iteration k.

For the term T1, we have

S1(k)

2

1 S1(k)

F(uk,zi(k)) − F(uk)

Ez(k)

i=1

(A.2)

S1(k)

σ2 S1(k)

2

1 S1(k) 2

(=i) Ez(k)

F(uk,zi(k)) − F(uk)

≤

,

i=1

where (i) is due to zi(k) i.i.d.∼ Pz and E F(uk,zi(k)) = F(uk).

For the term T2, we have

S2(k)

2

1 S2(k)

F(uk,zi(k)) − F(uk−1,zi(k)) − F(uk)

Ez(k) F(uk−1) +

i=1

S2(k)

1 S2(k) 2

###### (=i) Ez(k)

F(uk,zi(k)) − F(uk−1,zi(k)) − (F(uk) − F(uk−1))

i=1

2

+ Ez(k) F(uk−1) − F(uk−1)

S2(k)

2

1 S2(k) 2

###### (=ii) Ez(k)

F(uk,zi(k)) − F(uk−1,zi(k)) − (F(uk) − F(uk−1))

i=1

2

+ Ez(k) F(uk−1) − F(uk−1)

,

2

where (i) and (ii) can be veriﬁed by expanding the square norm and using the assumption that all zi(k) are i.i.d. and F(x,zi(k)) is unbiased. Since E[ X − EX 2] ≤ E[ X 2] for any random variable X, and using Assumption 3 for the stochastic queries, we have

S2(k)

1 S2(k) 2

Ez(k)

i=1

S2(k)

1 S2(k) 2

Ez(k)

≤

i

i=1

F(uk,zi(k)) − F(uk−1,zi(k)) − (F(uk) − F(uk−1))

2

F(uk,zi(k)) − F(uk−1,zi(k))

2

L2 uk − uk−1 2 S2(k)

≤

.

So we obtain

S2(k)

1 S2(k)

F(uk,zi(k)) − F(uk−1,zi(k)) − F(uk)

Ez(k) F(uk−1) +

i=1

L2 uk − uk−1 2 S2(k)

2

≤ F(uk−1) − F(uk−1)

+

.

Plugging Inequalities (A.2) and (A.3) into Eq. (A.1), we have

2

(A.3)

2

E F(uk) − F(uk)

Fk−1

pkσ2 S1(k)

+ (1 − pk) F(uk−1) − F(uk−1)

≤

(1 − pk)L2 uk − uk−1 2 S2(k)

2

+

.

Taking expectation with respect to all the randomness on both sides, and by the tower property of conditional expectations, we now obtain

E F(uk) − F(uk)

2

1 S1(k)

≤ pkσ2E

+ (1 − pk)E F(uk−1) − F(uk−1)

uk − uk−1 2

+ (1 − pk)L2E

,

S2(k)

2

which leads to the inequality in the lemma when S1(k) are deterministic, thus completing the proof. Corollary 2.2. Given a target error > 0, if for all k ≥ 1, pk = k+12 ,S1(k) ≥ 8σ

| |
|---|


2 uk−uk−1 2

2

pk 2 ,S2(k) ≥ 8L

###### p2k 2 , then E F(uk) − F(uk) 2 ≤

2

k .

Proof. We prove it by induction whose base step is

p1σ2 S1(1)

2

2

8 ≤ 2, where we use that p1 = 1.

E F(u1) − F(u1)

≤

≤

Assume that the result holds for all j < k; then by Lemma 2.1, we have that at iteration k

2

E F(uk) − F(uk)

pkσ2 S1(k)

+ (1 − pk)E F(uk−1) − F(uk−1)

≤

2

+ (1 − pk)L2E

uk − uk−1 2

S2(k)

.

Plugging in our choice of pk, S1(k) and S2(k), we have

p2k 2 8

(1 − pk) 2 k − 1

p2k(1 − pk) 2 8

2

E F(uk) − F(uk)

≤

+

+

p2k 2 4

(1 − pk) 2 k − 1

2

(i)

(ii)

1 (k + 1)2

1 k + 1

2

≤

≤

+

=

+

,

k

2 k(1−pk) 2

2 k

2

where (i) is due to p

8 ≤ p

8 , and (ii) is because k(k + 2) ≤ (k + 1)2. Hence, by induction, we can conclude that the result holds for all k ≥ 1.

| |
|---|


### B Omitted proofs from Section 3

#### B.1 Unconstrained settings

Our argument for bounding the total number of stochastic queries to F is based on the use of the following potential function, which was previously used for the deterministic case of Halpern iteration in (Diakonikolas, 2020; Diakonikolas and Wang, 2022),

Ak Lk

F(uk) 2 + Bk F(uk),uk − u0 , (B.1)

Ck =

where {Ak}k≥1 and {Bk}k≥1 are positive and non-decreasing sequences of real numbers, while the step size λk is deﬁned by λk := B

Ak+Bk . We start the proof by ﬁrst justifying that a bound on the chosen potential function Ck leads to a bound on F(uk) in expectation. The proof is a simple extension of (Diakonikolas, 2020, Lemma 4) and is provided for completeness.

k

- Lemma B.1. Given k ≥ 1, let Ck be deﬁned as in Eq. (B.1) and let u∗ be a solution to the monotone inclusion problem corresponding to F. If E[Ck] ≤ E[Ek] for some error term Ek, then


BkLk Ak

Lk Ak

E F(uk) 2 ≤

u0 − u∗ E[ F(uk) ] +

E[Ek], (B.2)

where the expectation is taken with respect to all random queries to F. Proof. By the deﬁnition of Ck, we have

BkLk Ak

Lk Ak

E F(uk) 2 ≤

E[ F(uk),u0 − uk ] +

E[Ek]

BkLk Ak

Lk Ak

E[ F(uk),u0 − u∗ + u∗ − uk ] +

E[Ek]

=

BkLk Ak

BkLk Ak

Lk Ak

E[ F(uk),u0 − u∗ ] +

E[ F(uk),u∗ − uk ] +

E[Ek].

=

Since u∗ is a solution to the monotone inclusion problem, as discussed in Section 2, it is also a weak VI (or MVI) solution, and thus

(∀k ≥ 0) F(uk),u∗ − uk ≤ 0.

As a result,

BkLk Ak

Lk Ak

E F(uk) 2 ≤

E[ F(uk),u0 − u∗ ] +

E[Ek] (i)

BkLk Ak

Lk Ak

E[ F(uk) u0 − u∗ ] +

E[Ek] (=ii)

≤

BkLk Ak

Lk Ak

u0 − u∗ E[ F(uk) ] +

E[Ek],

where we use Cauchy-Schwarz inequality for (i), while (ii) holds because u0 − u∗ involves no randomness.

| |
|---|


Using Lemma B.1, our goal now is to show that we can provide a bound on E[Ck] by appropriately choosing the algorithm parameters. In the deterministic setup, it is sufﬁcient to choose Lk = O(L) and λk = O(k1) to ensure that {AkCk}k≥1 is monotonically non-increasing, which immediately leads to Ck ≤ A

Ak C1. In the stochastic setup considered here, we follow the same motivation, but need to deal with additional error terms caused by the stochastic access to F.

1

We assume throughout that L is known, and make the following assumption on the choice of {Ak}k≥1, {Bk}k≥1, and {Lk}k≥1, and provide a corresponding bound on the change of Ck in Lemma B.2. Assumption 4. {Lk}k≥1 is a sequence of positive reals such that Lk ≥ L for all k ∈ N. Sequences {Ak}k≥1 and {Bk}k≥1 are positive and non-decreasing, satisfying the following for all k ≥ 2:

Bk Ak + Bk

1 Lk

Bk−1 Ak

2Bk Ak + Bk

Ak−1 AkLk−1

1 −

=

,

###### .

=

- Lemma B.2. Let Ck be deﬁned as in Eq. (B.1), where {Ak}k≥1 and {Bk}k≥1 satisfy Assumption 4. Let Lk = 2L for all k ≥ 1. Then, for any k ≥ 2, we have


Ak − Ak−1 2L

2

Ak 2L

Ck − Ck−1 ≤

F(uk−1) − F(uk−1)

F(uk−1),F(uk−1) − F(uk−1) .

+

Proof. By the deﬁnition of Ck, we have

Ak Lk

F(uk) 2 + Bk F(uk),uk − u0 −

Ck − Ck−1 =

Ak−1 Lk−1

###### F(uk−1) 2 − Bk−1 F(uk−1),uk−1 − u0 .

Since the operator F is cocoercive with parameter L1 , we have

F(uk) − F(uk−1),uk − uk−1 ≥

1 L

F(uk) − F(uk−1) 2

1 Lk

1 Lk

1 L −

F(uk) − F(uk−1) 2 +

F(uk) − F(uk−1) 2

=

1 Lk

1 Lk

2 Lk

F(uk) 2 −

F(uk−1) 2

=

F(uk),F(uk−1) +

1 Lk

1 L −

F(uk) − F(uk−1) 2 .

+

By rearranging, we obtain

1 Lk

F(uk) 2 ≤ F(uk),uk − uk−1 +

1 Lk

F(uk−1) 2 −

−

2 Lk

F(uk−1) − F(uk−1),uk − uk−1

1 Lk

1 L −

F(uk) − F(uk−1) 2 .

Multiplying Ak on both sides and plugging into Ck − Ck−1, we have

2Ak Lk

Ck − Ck−1 ≤ F(uk),Ak(uk − uk−1) +

F(uk−1) + Bk(uk − u0) − F(uk−1),Ak(uk − uk−1) + Bk−1(uk−1 − u0) −

Ak Lk

Ak−1 Lk−1

1 L −

1 Lk

F(uk−1) 2 − Ak

F(uk) − F(uk−1) 2 .

+

Since λk = B

Ak+Bk , we have

k

Bk Ak + Bk

Ak Ak + Bk

uk =

u0 +

2 Lk

uk−1 −

F(uk−1) ,

###### Lk F(uk−1)− F(uk−1) . Further, as B

which leads to Ak(uk−uk−1)+2A

###### Lk F(uk−1)+Bk(uk−u0) = 2A

Ak = B

k−1

k

k

k

Ak+Bk

by Assumption 4, we have

F(uk−1),Ak(uk − uk−1) + Bk−1(uk−1 − u0)

Ak − Bk−1 Ak

Bk−1 Ak

u0 −

= Ak F(uk−1),uk −

uk−1

Bk Ak + Bk

Ak Ak + Bk

= Ak F(uk−1),uk −

u0 −

uk−1

2Ak Lk(Ak + Bk)

= − Ak F(uk−1),

F(uk−1) .

Ak+Bk = A

###### 1 − 2B

Moreover, by Assumption 4, we have L1

AkLk−1 , so we obtain F(uk−1),Ak(uk − uk−1) + Bk−1(uk−1 − u0)

k−1

k

k

2Ak Lk(Ak + Bk)

= − Ak F(uk−1),

F(uk−1)

Ak Lk

Ak−1 Lk−1

= − F(uk−1),

+

###### F(uk−1) .

Since by hypothesis Lk = 2L for all k ≥ 1, we have

Ak + Ak−1 2L

Ak L

(F(uk−1) − F(uk−1)) + F(uk−1),

Ck − Ck−1 ≤ F(uk),

F(uk−1)

Ak 2L

Ak + Ak−1 2L

F(uk) − F(uk−1) 2 (=i)

F(uk−1) 2 −

−

Ak L

Ak 2L

F(uk) − F(uk−1) 2

F(uk) − F(uk−1),F(uk−1) − F(uk−1) −

Ak − Ak−1 2L

F(uk−1) − F(uk−1) ,

+ F(uk−1),

where (i) is derived by rearranging and grouping terms. Using that 2 p,q − p 2 ≤ q 2 holds for any p,q ∈ Rd, we ﬁnally obtain

Ak − Ak−1 2L

2

Ak 2L

F(uk−1),F(uk−1) − F(uk−1) , thus completing the proof.

F(uk−1) − F(uk−1)

Ck − Ck−1 ≤

+

| |
|---|


By Lemma B.2, if we choose Ak = O(k2) and Bk = O(k) satisfying Assumption 4, and take sufﬁciently large size of samples queried to ensure that E F(uk) − F(uk) 2 ≤

2

k for k ≥ 0, then we can obtain O(1/k) expected convergence rate in the norm of the operator by induction. Observe that we do not need an assumption that F is an unbiased estimator of F for any point except for the initial one; all that is needed is that the second moment of the estimation error, F(uk) − F(uk) 22, is bounded.

Theorem 3.1. Given an arbitrary u0 ∈ Rd, suppose that iterates uk evolve according to Halpern iteration from Eq. (3.1) for k ≥ 1, where Lk = 2L and λk = k+11 . Assume further that the stochastic estimate F(u) is unbiased for u = u0 and E[ F(u0) − F(u0) 2] ≤

###### 8 . Given > 0, if for all k ≥ 1, we have that E F(uk) − F(uk) 2 ≤

2

2

k , then for all k ≥ 1,

Λ0 k

+ Λ1 , (3.2)

E[ F(uk)) ] ≤

where Λ0 = 76L u0 − u∗ and Λ1 = 4 23. As a result, stochastic Halpern iteration from Eq. (3.1) returns a point uk such that E[ F(uk) ] ≤ 4 after at most N = 2Λ

0−u∗ iterations.

= O L u

0

Proof. Observe ﬁrst that the chosen sequence of numbers Ak,Bk satisﬁes Assumption 4, and thus Lemma B.2 applies. Observe further that, by Jensen’s Inequality,

E[ F(uk)) ] ≤ E[ F(uk) 2]

- 1

- 2


###### .

and, thus, to prove the theorem, it sufﬁces to show that there exists Λ0 and Λ1 such that for all k ≥ 1

- 1

- 2


Λ0 k

E[ F(uk) 2]

≤

+ Λ1 .

We prove this claim by induction on k. For the base case k = 1, in which u1 = u0 − 21L F(u0), we have

1 L

1 L

F(u1) 2 + 2 F(u1),u1 − u0 =

F(u1) 2 − F(u1), F(u0) . (B.3)

C1 =

Further, since the operator F is cocoercive with parameter L1 , it is also cocoercive with parameter 21L, and thus we have

F(u1) − F(u0) 2 ≤ 2L F(u1) − F(u0),u1 − u0 = F(u1) − F(u0),− F(u0) . Expanding and rearranging the terms, we have

F(u1) 2 ≤ F(u0), F(u0) − F(u0) + 2 F(u1),F(u0) − F(u1), F(u0) .

Recall that, by assumption, E[ F(u0)] = F(u0). Subtracting F(u1), F(u0) from both sides in the last inequality and taking expectation with respect to all the randomness on both sides, we have

E F(u1) 2 − F(u1), F(u0) ≤ E F(u0), F(u0) − F(u0) + 2 F(u1),F(u0) − 2 F(u1), F(u0)

= 2E F(u1),F(u0) − F(u0) (i) ≤ E

- 1

- 2


F(u1) 2 + 2 F(u0) − F(u0) 2 ,

where for (i) we use Young’s inequality. Plugging into Eq. (B.3), we obtain that

1 L

E

E[C1] ≤

- 1

- 2


F(u1) 2 + 2 F(u0) − F(u0) 2 .

Note that A1 = B1 = 2 and L1 = 2L, by Lemma B.1 we have

B1L1 A1

E[ F(u1) 2] ≤

u0 − u∗ E[ F(u1) ] +

- 1

- 2


= 2L u0 − u∗ E[ F(u1) ] + E

L1 A1

1 L

- 1

- 2


F(u1) 2 + 2 F(u0) − F(u0) 2

E

F(u1) 2 + 2 F(u0) − F(u0) 2 .

Subtracting E[12 F(u1) 2] on both sides and using that (by Jensen’s inequality) E[ F(u1) ] ≤ E[ F(u1) 2] and (by assumption) E[ F(u0) − F(u0) 2] ≤

2

8 , we have

2

- 1

- 2


E[[ F(u1) 2] ≤ 4L u0 − u∗ E[ F(u1) 2]

+

,

2

- 1

- 2


which is a quadratic inequality in (E[ F(u1) 2])12 . Bounding the solution to this quadratic inequality by its larger root, we have

- 1

- 2


- 1

- 2


(E[ F(u1) 2])

16L2 u0 − u∗ 2 + 2 2 ≤ 2L u0 − u∗ +

≤ 2L u0 − u∗ +

√

- 1

- 2


(4L u0 − u∗ +

2 )

≤ 4L u0 − u∗ + ≤ Λ0 + Λ1 .

This completes the proof for the base case. Moreover, we can get a bound for E[C1] as follows

2

1 L

- 1

- 2


F(u1) 2 + 2 F(u0) − F(u0)

E[C1] ≤

E

2

(i)

- 1

- 2L


3 2

2 L

24L2 u0 − u∗ 2 +

2 +

≤

8

2

= 12L u0 − u∗ 2 +

,

L

where (i) can be veriﬁed by the bound we get above for E[ F(u1) 2] and by applying Young’s inequality and that, by assumption, E[ F(u0) − F(u0) 2] ≤

2

8 .

For the inductive hypothesis, assume that the result holds for all 1 ≤ i ≤ k − 1, and consider iteration k. By Lemma B.2, we have for ∀i ≥ 2

Ai − Ai−1 2L

2

Ai 2L

Ci − Ci−1 ≤

F(ui−1),F(ui−1) − F(ui−1) (i)

F(ui−1) − F(ui−1)

+

2

5i(i + 1) 2L

i 8L(i + 1)

F(ui−1) 2 ,

≤

F(ui−1) − F(ui−1)

+

where we use Young’s inequality and Ai = i(i + 1) for (i). Taking expectation with respect to all randomness on both sides and telescoping from i = 2 to k, we obtain

k

5i(i + 1) 2L

i 8L(i + 1)

F(ui−1) − F(ui−1) 2 +

F(ui−1) 2

E[Ck] ≤ E C1 +

i=2

k

2

5i(i + 1) 2L

i 8L(i + 1)

F(ui−1) 2

≤ E

F(ui−1) − F(ui−1)

+

i=2

2

+ 12L u0 − u∗ 2 +

.

L

Using that, by assumption, for k ≥ 1, E[ F(uk) − F(uk) 2] ≤

2

k , we further have

E

k

5i(i + 1) 2L

i=2

k

2

5i(i + 1) 2L

F(ui−1) − F(ui−1) 2 ≤

i − 1

i=2

k

5(i + 1) 2 L

(i)

≤

i=2

5(k + 4)(k − 1) 2 2L

=

,

(B.4)

(B.5)

where (i) is because i−i1 ≤ 2 for all i ≥ 2. By induction, we have

k

- (i) ≤

k

i=2

1 8L

2Λ20 (i − 1)2

+ 2Λ21 2

- (ii)


i 8L(i + 1)

F(ui−1) 2

E

i=2

1 4L

Λ20

≤

Λ20π2 24

1 L

=

π2 6

+ (k − 1)Λ21 2

(k − 1)Λ21 2 4

,

+

(B.6)

2

where (i) follows from induction and i+1i ≤ 1, and (ii) is due to ki=2 (i−11)2 ≤ ∞i=1

6 . Combining Eqs. (B.4)– (B.6), we get

1 i2 = π

2

Λ20π2 24

5(k + 4)(k − 1) 2 2L

(k − 1)Λ21 2 4

1 L

E[Ck] ≤ 12L u0 − u∗ 2 +

. Applying Lemma B.1 to the bound on Ck from the last inequality, we have

+

+

+

L

E F(uk) 2 ≤

BkLk Ak

u0 − u∗ E[ F(uk) ]

2

5(k + 4)(k − 1) 2 2L

Λ20π2 24L

(k − 1)Λ21 2 4L

Lk Ak

12L u0 − u∗ 2 +

+

+

+

+

L

2L k

u0 − u∗ E[ F(uk) ]

=

Λ20π2 12

(k − 1)Λ21 2 2

1 k(k + 1)

24L2 u0 − u∗ 2 + 2 2 + 5(k + 4)(k − 1) 2 +

+

+

24L2 u0 − u∗ 2 k2

Λ21 2(k + 1)

Λ20π2 12k2

(i)

2L k

u0 − u∗ E[ F(uk) ] +

2 +

≤

+ 8 +

,

where (i) is due to k(k1+1) ≤ k12 , 5(kk+1)((k+1)k−1) ≤ 6 and k−1

k(k+1) ≤ k+11 . Since E[ F(uk) ] ≤ (E[ F(uk) 2])21 by Jensen’s inequality, we have

E F(uk) 2 ≤

2L k

u0 − u∗ E F(uk) 2

- 1

- 2


+

24L2 u0 − u∗ 2 k2

Λ21 2(k + 1)

+ 8 +

Λ20π2 12k2

2 +

,

which is a quadratic inequality with respect to (E[ F(uk) 2])12 . Similarly as for k = 1, bounding its solution by its larger root, we obtain

E F(uk) 2

- 1

- 2


L k

≤

- 1

- 2


u0 − u∗ +

24L2 u0 − u∗ 2 k2

Λ20π2 12k2

Λ21 2(k + 1)

4L2 k2

u0 − u∗ 2 + 4

2 +

+ 8 +

- (i)

≤

2L k

u0 − u∗ +

5L u0 − u∗ k

+ 8 +

Λ21 2(k + 1)

+

Λ0π 2√3k

=

7L u0 − u∗ + Λ

0π 2√3

k

+ 8 +

Λ21 2(k + 1)

- (ii)


Λ0 k

≤

+ Λ1 ,

where (i) is due to the fact that ni=1 Xi2 ≤ ni=1 |Xi|, and (ii) is because of our choice of Λ0,Λ1. Hence, the result also holds for the case k. Then by induction we know that the result holds for all k ≥ 1.

Finally, when k ≥ 2Λ

0 , we have Λ0

k ≤  /2. Also, since we have Λ1 = 4 23 < 3.5, we obtain

E[ F(uk) ] ≤

- 1

- 2


+ 4

- 2

- 3 ≤ 4 .


Hence, the total number of iterations needed to attain 4 norm of the operator is

L u − u∗

2Λ0

= O

, thus completing the proof.

N =

| |
|---|


#### B.2 Constrained setting with a cocoercive operator

To extend the results to possibly constrained settings, similar to Diakonikolas (2020), we make use of the operator mapping deﬁned by

Gη(u) = η u − ΠU u −

1 η

F(u) , (B.7)

where U ⊆ Rd is the closed convex constraint set and ΠU(u) is the projection operator. Operator Gη is a valid proxy for approximating (MI); see (Diakonikolas, 2020) for further details.

The extension of our results to constrained stochastic settings is not immediate; the reason is that the stochastic query assumptions (Assumptions 1 and 2) are made for the operator F, not Gη. Nevertheless, as we show in this subsection, it is not hard to match the stochastic oracle complexity of the unconstrained setups by proving an additional auxiliary result that bounds the variance of an operator mapping corresponding to F (Lemma B.4).

We begin by recalling that whenever F is L1 -cocoercive and η ≥ L, the operator mapping Gη is 43η-cocoercive (see, e.g., (Diakonikolas, 2020, Proposition 7) and (Beck, 2017, Lemma 10.11)). Proposition B.3. Let F be L1 -cocoercive and let Gη be deﬁned as in Eq. (B.7), where η ≥ L. Then Gη is 43η-cocoercive.

To state the variant of stochastic Halpern iteration for constrained settings, we also deﬁne the operator mapping corresponding to the stochastic estimate F by

Gη(u) = η u − ΠU u −

1 η

F(u) . (B.8)

In the following lemma, we bound the error between the stochastic operator mapping and true operator mapping by the variance of stochastic queries.

- Lemma B.4. Let Gη(·) and Gη(·) be deﬁned as in Eq. (B.7) and Eq. (B.8), respectively. Then, for any u ∈ U and any η > 0, we have


Gη(u) − Gη(u) 2 ≤ F(u) − F(u) 2. (B.9) Proof. By the deﬁnition of gradient mapping, we have

Gη(u) − Gη(u)

2

= η2 ΠU u −

Since the projection operator is non-expansive, we obtain

1 η

F(u) − ΠU u −

1 η

F(u)

2

.

Gη(u) − Gη(u)

2

≤ η2 u −

1 η

F(u) − u −

1 η

F(u)

2

= F(u) − F(u)

2

,

thus completing the proof. Similar to the unconstrained setup, we deﬁne the following stochastic Halpern iteration for the constrained setup:

| |
|---|


(uk)/Lk+1 , (B.10)

uk+1 = λk+1u0 + (1 − λk+1) uk − GL

k

where Lk ≥ L, ∀k ≥ 0. By the cocoercivity of the operator mapping and the error bound in Lemma B.4, we can immediately obtain the results for the iteration complexity and stochastic oracle complexity as in the unconstrained case, by applying Theorem 3.1 and Corollary 3.4 to GL and GL. This is summarized in the following Theorem B.6 and Corollary B.7. To prove these, we make use of the potential function as in the unconstrained settings

Ak 2Lk

Ck =

###### (uk) 2 + Bk GL

###### (uk),uk − u0 , (B.11)

GL

k

k

and ﬁrst bound the change of Ck in the following Lemma B.5. For short, we denote GL as G below.

- Lemma B.5. Let Ck be deﬁned as in Eq. (B.11), where Ak and Bk satisfy Assumption 4. Assume that L is already known and we set Lk = L for any k ≥ 1. Then for any k ≥ 2, we have


Ak − Ak−1 2L

2

Ak L

G(uk−1) − G(uk−1)

G(uk−1),G(uk−1) − G(uk−1) .

Ck − Ck−1 ≤

+

Proof. By the deﬁnition of Ck, we have

Ak 2Lk

###### (uk) 2 + Bk GL

Ck − Ck−1 =

(uk),uk − u0 −

GL

k

k

Ak−1 2Lk−1

(uk−1) 2 − Bk−1 GL

###### (uk−1),uk−1 − u0 .

###### GL

k−1

k−1

Since GL

is cocoercive with parameter 4L3

when Lk ≥ L, we have GL

k

k

(uk−1),uk − uk−1 ≥

###### (uk) − GL

k

k

- 3

- 4Lk


(uk−1) 2

###### (uk) − GL

GL

k

k

- 1

- 2Lk


###### (uk) 2 − 2 GL

(uk−1) 2

=

GL

###### (uk),GL

###### (uk−1) + GL

k

k

k

k

1 4Lk

(uk−1) 2 .

###### (uk) − GL

GL

+

k

k

Multiplying Ak on both sides and rearranging the terms, we obtain

Ak 2Lk

Ak Lk

###### (uk) 2 ≤ GL

(uk),Ak(uk − uk−1) +

GL

GL

###### (uk−1) − GL

k

k

k

(uk−1),Ak(uk − uk−1) −

k

Ak 4Lk

Ak 2Lk

(uk−1) 2 −

(uk−1) 2 .

###### (uk) − GL

GL

GL

k

k

k

Plugging this into Ck − Ck−1, we have

Ak Lk

###### (uk−1) + Bk(uk − u0) − GL

###### Ck − Ck−1 ≤ GL

(uk),Ak(uk − uk−1) +

GL

k

k

(uk−1),Bk−1(uk−1 − u0) −

###### (uk−1),Ak(uk − uk−1) + GL

k−1

k

Ak 2Lk

Ak−1 2Lk−1

(uk−1) 2

(uk−1) 2 +

GL

###### GL

k−1

k

Ak 4Lk

(uk−1) 2 .

###### (uk) − GL

−

GL

k

k

###### Since λk = B

Ak+Bk , we have

k

Bk Ak + Bk

Ak Ak + Bk

uk =

u0 +

uk−1 − GL

###### (uk−1)/Lk ,

k−1

which leads to Ak(uk − uk−1) + A

(uk−1) + Bk(uk − u0) = A

(uk−1) . Further, as B

(uk−1) − GL

Lk GL

Lk GL

k

k

k−1

k−1

k

Ak = B

Ak+Bk by https://www.overleaf.com/project/5fe36b9ad2991b26777b720dAssumption 4, we have

k−1

k

(uk−1),Ak(uk − uk−1) + Bk−1(uk−1 − u0)

###### GL

k

Bk−1 Ak

(uk−1),uk − uk−1 +

(uk−1 − u0)

= Ak GL

k

Ak Ak + Bk

Bk Ak + Bk

(uk−1),uk −

uk−1 −

= Ak GL

##### u0

k

Ak Ak + Bk

(uk−1),−

= Ak GL

GL

(uk−1)/Lk .

k−1

k

Ak+Bk ) = A

###### (1 − 2B

AkLk−1 , so we obtain GL

Moreover, by Assumption 4, we have L1

k−1

k

k

(uk−1),Ak(uk − uk−1) + Bk−1(uk−1 − u0)

k

Ak Ak + Bk

(uk−1),−

= Ak GL

GL

(uk−1)/Lk

k−1

k

- 1

- 2


Ak Lk

Ak−1 Lk−1

= −

GL

(uk−1),

+

###### GL

(uk−1) .

k−1

k

Having Lk = L and denoting GL = G for short, we have

Ak + Ak−1 2L

Ak L

G(uk−1) − G(uk−1) + G(uk−1),

Ck − Ck−1 ≤ G(uk),

G(uk−1)

Ak 4L

Ak + Ak−1 2L

G(uk−1) 2 −

G(uk) − G(uk−1) 2

−

Ak L

Ak 4L

G(uk) − G(uk−1) 2 −

G(uk),G(uk−1) − G(uk−1) −

=

Ak + Ak−1 2L

G(uk−1),G(uk−1) − G(uk−1)

Ak L

Ak 4L

G(uk) − G(uk−1) 2

G(uk) − G(uk−1),G(uk−1) − G(uk−1) −

=

Ak − Ak−1 2L

G(uk−1),G(uk−1) − G(uk−1) .

+

Since 2 p,q + p 2 ≤ q 2 for any p,q ∈ Rd, we have

Ak − Ak−1 2L

2

Ak L

G(uk−1),G(uk−1) − G(uk−1) , thus completing the proof.

G(uk−1) − G(uk−1)

Ck − Ck−1 ≤

+

| |
|---|


Theorem B.6. Given an arbitrary u0 ∈ Rd, suppose that iterates uk evolve according to Halpern iteration for the constrained setup from Eq. (B.10) for k ≥ 1, where Lk = L and λk = k+11 . Given > 0, if we have that E[ F(u0) − F(u0) 2] ≤

8 and E F(uk) − F(uk) 2 ≤

2

2

k for all k ≥ 1, then for all k ≥ 1,

Λ0 k

+ Λ1 , (B.12)

E[ G(uk)) ] ≤

where Λ0 = 20L u0 − u∗ and Λ1 = √13. As a result, stochastic Halpern iteration from Eq. (3.1) returns a point uk such that E[ G(uk) ] ≤ 5 after at most N = 2Λ

0−u∗ iterations.

= O L u

0

Proof. First note that since U is convex and closed, and uk − G(uk)/L = ΠU uk − L1 F(uk) , then we have for ∀k > 0.

uk+1 = λk+1u0 + (1 − λk+1) uk − G(uk)/L = λk+1u0 + (1 − λk+1)ΠU uk −

1 L

F(uk) ∈ U. Then we come to prove the convergence. By Jensen’s Inequality, we have for k ≥ 1

- 1

- 2


E[ G(uk)) ] ≤ E[ G(uk) 2]

###### .

So it sufﬁces to show that there exists Λ0 and Λ1 such that for all k ≥ 1

- 1

- 2


Λ0 k

E[ G(uk) 2]

≤

+ Λ1 .

We prove it by induction. First, we consider the basis case k = 1 in which u1 = u0 − 21L G(u0), so we have C1 = 1 L G(u1) 2 + 2 G(u1),u1 − u0 = L1 G(u1) 2 − G(u1), G(u0) . Also, since the operator G is cocoercive

with parameter 43L, thus cocoercive with 21L, we have

G(u1) − G(u0) 2 ≤ 2L G(u1) − G(u0),u1 − u0 = G(u1) − G(u0),− G(u0) . Expanding and rearranging the terms, we have

G(u1) 2 ≤ G(u0), G(u0) − G(u0) + 2 G(u1),G(u0) − G(u1), G(u0) .

Subtracting G(u1), G(u0) and taking expectation with respect to all randomness on both sides, we have

E G(u1) 2 − G(u1), G(u0)

≤ E G(u0), G(u0) − G(u0) + 2 G(u1),G(u0) − 2 G(u1), G(u0) (i) ≤ E

2

- 1

- 2


- 1

- 2


5 2

G(u0) 2 +

G(u1) 2 +

G(u0) − G(u0)

,

where for (i) we use Young’s Inequality. Since u∗ is the solution of monotone inclusion, then we have G(u∗) = 0. So we have

(i) ≤ 10L2 u0 − u∗ 2 ,

G(u0) 2 = G(u0) − G(u∗) 2

where (i) can be veriﬁed by Young’s Inequality and using the fact that the projection operator is non-expansive. Also using the results in Lemma B.4, we obtain that

2

1 L

- 1

- 2


5 2

E 5L2 u0 − u∗ 2 +

G(u1) 2 +

E[C1] ≤

F(u0) − F(u0)

. Proceeding similar to Lemma B.1, we have

2B1L1 A1

E[ G(u1) 2] ≤

u0 − u∗ E[ G(u1) ]

- 1

- 2


2L1 A1L

5 2

E 5L2 u0 − u∗ 2 +

G(u1) 2 +

F(u0) − F(u0)

+

= 2L u0 − u∗ E[ G(u1) ]

2

- 1

- 2


5 2

+ E 5L2 u0 − u∗ 2 +

G(u1) 2 +

F(u0) − F(u0)

###### .

2

Subtracting E[12 G(u1) 2] on both sides and using the fact that E[ G(u1) ] ≤ E[ G(u1) 2]

2

8 , we have

1 2

and E[ F(u0) − F(u0)

2

] ≤

E[[ G(u1) 2] ≤ 4L u0 − u∗ E[ G(u1) 2]

5 2 8

- 1

- 2


+ 10L2 u0 − u∗ 2 +

,

which is a quadratic function with respect to (E[ G(u1) 2])21. So by its larger root we have

- 1

- 2


5 2

- 1

- 2


56L2 u0 − u∗ 2 +

(E[ G(u1) 2])

≤ 2L u0 − u∗ +

2

√10 2

√

- 1

- 2


14L u0 − u∗ +

≤ 2L u0 − u∗ +

) ≤ 6L u0 − u∗ + ≤ Λ0 + Λ1 .

(2

So the result holds for the basis case. Moreover, we can get a bound for E[C1] as follows

2

1 L

- 1

- 2


5 2

E 5L2 u0 − u∗ 2 +

G(u1) 2 +

E[C1] ≤

F(u0) − F(u0)

2

(i) ≤ 5L u0 − u∗ 2 +

1 2L

5 4

5 2L

50L2 u0 − u∗ 2 +

2 +

8 ≤ 30L u0 − u∗ 2 +

2

,

L

where (i) can be veriﬁed by using the bound we get above for E[ G(u1) 2] and applying Young’s Inequaltiy, and the fact that E[ F(u0) − F(u0)

2

2

8 .

] ≤

Assume that the result holds for all 1 ≤ i ≤ k − 1, then we come to prove the case k. By Lemma B.5 we have for ∀i ≥ 2

Ai − Ai−1 2L

2

Ai L

Ci − Ci−1 ≤

G(ui−1) − G(ui−1)

G(ui−1),G(ui−1) − G(ui−1)

+

- (i)

≤

3i(i + 1) L

G(ui−1) − G(ui−1)

2

+

i 8L(i + 1)

G(ui−1) 2

- (ii)


2

i 8L(i + 1)

3i(i + 1) L

G(ui−1) 2 ,

≤

F(ui−1) − F(ui−1)

+

where we use Young’s Inequality and Ai = i(i + 1) for (i), and (ii) is due to Lemma B.4. Taking expectation with respect to all randomness on both sides and telescoping from i = 2 to k, we obtain

k

E[Ck] ≤ E C1 +

i=2

3i(i + 1) L

≤ 30L u0 − u∗ 2 +

+ E

By Corollary 2.2, we have

k

3i(i + 1) L

i=2

k

3i(i + 1) L

E

i=2

k

3i(i + 1) L

≤

i=2

F(ui−1) − F(ui−1)

2

i 8L(i + 1)

+

2

+ E

L

k

i 8L(i + 1)

i=2

F(ui−1) − F(ui−1)

G(ui−1) 2

2

###### .

G(ui−1) 2

F(ui−1) − F(ui−1)

2

i − 1

k

6(i + 1) 2 L

(i)

≤

=

i=2

2

3(k + 4)(k − 1) 2 L

,

where (i) is because i−i1 ≤ 2 for all i ≥ 2. By induction, we have

E

k

i 8L(i + 1)

i=2

G(ui−1) 2

- (i) ≤

k

i=2

1 8L

2

Λ20 (i − 1)2

+ 2Λ21 2

- (ii)


1 4L

≤

π2 6

1 L

Λ20

+ (k − 1)Λ21 2 =

Λ20π2 24

(k − 1)Λ21 2 4

+

,

where (i) follows from induction and i+1i ≤ 1, and (ii) is due to ki=2 (i−11)2 ≤ ∞i=1

2

6 . We now obtain

1 i2 = π

2

E[Ck] ≤ 30L u0 − u∗ 2 +

L

3(k + 4)(k − 1) 2 L

1 L

+

+

Λ20π2 24

+

(k − 1)Λ21 2 4

.

By the same derivation of Lemma B.1, we have

E G(uk) 2 ≤

+

L k

=

+

(i)

L k

≤

BkLk Ak

u0 − u∗ E[ G(uk) ]

3(k + 4)(k − 1) 2 L

Λ20π2 24L

2

Lk Ak

30L u0 − u∗ 2 +

+

+

+

L

30L2 u0 − u∗ 2 k(k + 1)

u0 − u∗ E[ G(uk) ] +

Λ20π2 24

(k − 1)Λ21 2 4

1 k(k + 1)

2 + 3(k + 4)(k − 1) 2 +

+

30L2 u0 − u∗ 2 k2

Λ21 4k

u0 − u∗ E[ G(uk) ] +

+ (11 +

(k − 1)Λ21 2 4L

Λ20π2 24k2

) 2 +

,

where (i) is due to k(k1+1) ≤ k12 , 3(kk+1)((k+1)k−1) ≤ 10 and k−1

k(k+1) ≤ k1. Since E[ G(uk) ] ≤ (E[ G(uk) 2])21 by Jensen’s Inequality, we have

L k

E G(uk) 2 ≤

+

- 1

- 2


u0 − u∗ E G(uk) 2

30L2 u0 − u∗ 2 k2

+ (11 +

Λ21 4k

Λ20π2 24k2

) 2 +

,

which is a quadratic function with respect to (E[ G(uk) 2])21 . So by its larger root we obtain

E G(uk) 2

- 1

- 2


L 2k

≤

- 1

- 2


u0 − u∗ +

- (i)

≤

L k

u0 − u∗ +

√30L u0 − u∗ k

+ 11 +

Λ21 4k

+

Λ0π 2√6k

=

(1 + √30)L u0 − u∗ + Λ

0π 2√6

k

+ 11 +

Λ21 4k

- (ii)


Λ0 k

≤

+ Λ1 ,

30L2 u0 − u∗ 2 k2

Λ20π2 24k2

Λ21 4k

L2 k2

u0 − u∗ 2 + 4

) 2 +

+ (11 +

where (i) is due to the fact that ni=1 Xi2 ≤ ni=1 |Xi|, and (ii) is because of our choice of Λ0,Λ1. Hence, the result also holds for the case k. Then by induction we know that the result holds for all k ≥ 1.

k ≤  /2. Also, since we have Λ1 = √13, we obtain

Finally, when k ≥ 2Λ

0 , we have Λ0

√

- 1

- 2


E[ G(uk) ] ≤

13 ≤ 5 .

+

Hence, the total number of iterations needed to attain 5 norm of the operator is

2Λ0

2Λ0

∆

≤

, thus completing the proof.

N =

+ 1 =

| |
|---|


Corollary B.7. Given an arbitrary u0 ∈ Rd, suppose that iterates uk evolve according to Halpern iteration from Eq. (B.10) for k ≥ 1, where Lk = L, and λk = k+11 . Assume further that the stochastic estimate F(u) is deﬁned according to Eq. (2.1), with its parameters set according to Corollary 2.2. Then, given any > 0, stochastic Halpern iteration from Eq. (B.10) returns a point uk such that E[ G(uk) ] ≤ 5 with at most O(σ

2L u0−u∗ +L3 u0−u∗ 3

3 ) oracle queries to F in expectation.

Proof. Let mk be the number of stochastic queries made by the estimator from Eq. (2.1) at iteration k. Conditional on Fk and using Corollary 2.2, since each stochastic gradient mapping G(uk) only involves one PAGE invariant stochastic estimate F(uk), we have

E mk+1|Fk−1 = pk

(i) ≤ pk

8L2 uk − uk−1 2 p2k 2

8σ2 pk 2

+ 2(1 − pk)

8L2 uk − uk−1 2 p2k 2

8σ2 pk 2

+ 1 + 2(1 − pk)

+ 1 ,

where (i) is due to the fact that x ≤ x + 1 for any x ∈ R. Taking expectation with respect to all randomness on both sides, and rearranging the terms, we obtain

16(1 − pk)L2E uk − uk−1 2 p2k 2

8σ2 2 +

E[mk+1] ≤

+ 2.

By the same derivation as Lemma 3.3, we have

 

- 1

4L2 G(u0)

2

if k = 1,

- 2k2


uk − uk−1 2 ≤

(B.13)



2

2

2

+ ki=0−2 2(i+1)

if k ≥ 2.

L2(k+1)2 G(uk−1)

k(k+1)2L2 G(ui)

2 u0−u∗ 2

By the corollary assumptions, we have E[ G(ui) 2] ≤ O(L

i2 ) for i ≤ k − 1 by Theorem B.6. Then we obtain

2

2

≤ 2E G(ui) 2 + 2E G(ui) − G(ui)

E G(ui)

(i) ≤ 2E G(ui) 2 + 2E F(ui) − F(ui)

2

L2 u0 − u∗ 2 i2

≤ O

,

where (i) is due to Lemma B.4. Plugging it into Inequality (B.13), we have E[ uk − uk−1 2] = O( u

0−u∗ 2

k2 ), which leads to

σ2 + L2 u0 − u∗ 2

E[mk+1] = O

2

###### using pk = k+12 = O(1/k).

Further, by Theorem B.6, the total number of iterations to attain 5 norm of the operator in expectation is N = O(L u

0−u∗ ) and m1 = S1(0) = O(σ

2

2 ), we conclude that the total number of stochastic queries to F is

N

σ2L u0 − u∗ + L3 u0 − u∗ 3 3 ,

E[M] = E

mk = O

k=1

thus completing the proof.

| |
|---|


### C Omitted proofs from Section 4

We use the potential function, previously used by (Tran-Dinh and Luo, 2021),

Vk := Ak F(uk) 2 + Bk F(uk),uk − u0 + ckL2 uk − vk−1 2, (C.1)

prove Theorem 4.1. Here Ak, Bk and ck are positive parameters to be determined later. We start by bounding the change of Vk under the following assumption on the parameters.

1−λk , Ak = B

kηk 2λk ,

Assumption 5. λk ∈ [0,1), ηk > 0, and Ak, Bk and ck are positive parameters satisfying Bk+1 = B

k

1 − λ2k − Mηk2 λk+1ηk 1 − Mηk2 1 − λk λk

λk+1 1 − λk Mλkηk

, Mηk2 + λ2k < 1, and ηk+1 ≤

, (C.2)

0 < ηk+1 =

where M = 3L2(2 + θ) and θ > 0 is some parameter that can be determined later.

The following lemma gives a bound on the difference between the potential function values at two consecutive iterations with the control of the parameters above.

- Lemma C.1. Let Vk be deﬁned as in Eq. (C.1), where the parameters satisfy Assumption 5. Then the difference of potential function between two consecutive iterations can be bounded by


Vk+1 − Vk ≤ − L2

2Ak Mηk2

+

θAk Mηk2 − ck+1 uk+1 − vk 2 − L2(ck − Ak) uk − vk−1 2

2

2

+ Ak F(vk−1) − F(vk−1)

F(vk) − F(vk)

.

Proof. By the iteration scheme in Eq. (4.1), we can deduce the following identities:

 

uk+1 − uk = λk(u0 − uk) − ηk F(vk) uk+1 − uk =

λk 1 − λk

ηk 1 − λk

(u0 − uk+1) −

F(vk) uk+1 − vk = −ηk F (vk) − F (vk−1)



Further, by the deﬁnition of the potential function Vk, we can write

Vk − Vk+1 = Ak F (uk) 2 − Ak+1 F (uk+1) 2

T[1]

+ Bk F (uk),uk − u0 − Bk+1 F (uk+1),uk+1 − u0

T[2]

+ ckL2 uk − vk−1 2 − ck+1L2 uk+1 − vk 2 .

To obtain the claimed bound, in the rest of the proof we focus on bounding T[1] and T[2]. To bound T[1], by the Lipschitz continuity of F, we have

F (uk+1) − F (vk) 2 ≤ L2 uk+1 − vk 2 = L2ηk2 F (vk) − F (vk−1)

2

,

(C.3)

(C.4)

(C.5)

where in the last step we used the third identity from Eq. (C.4). Further, for any θ > 0

2

###### + θL2 uk+1 − vk 2 ≤ 2 F (uk+1) − F (vk) 2 + 2 F (vk) − F (vk)

F (uk+1) − F (vk)

2

+ θL2 uk+1 − vk 2

2

2

≤ηk2L2(2 + θ) F (vk) − F (vk−1)

+ 2 F (vk) − F (vk)

,

where again in the last step we used the third identity from Eq. (C.4). Notice that

(C.6)

2

F (vk) − F (vk−1)

2

= F (vk) − F (uk) + F (uk) − F (vk−1) + F (vk−1) − F (vk−1)

2

+ 3 F (uk) − F (vk−1) 2 + 3 F (vk−1) − F (vk−1)

≤ 3 F (vk) − F (uk)

2

≤ 3 F (uk) 2 − 2 F (uk), F (vk) + F (vk)

+ 3L2 uk − vk−1 2

2

+ 3 F (vk−1) − F (vk−1)

###### .

2

Let M := 3L2(2 + θ). Expanding the term F(uk+1) − F(vk) 2 on the LHS in Inequality (C.6) and combining with the inequality above, we have

2

− 2 F (uk+1), F (vk) + θL2 uk+1 − vk 2

F (uk+1) 2 + F (vk)

2

+ ML2ηk2 uk − vk−1 2

≤ Mηk2 F (uk) 2 − 2 F (uk), F (vk) + F (vk)

2

2

+ Mηk2 F (vk−1) − F (vk−1)

+ 2 F (vk) − F (vk)

###### .

Mηk2 , rearranging this inequality and subtracting Ak+1 F(uk+1) 2 on both sides, we obtain T[1] = Ak F (uk) 2 − Ak+1 F(uk+1) 2

Multiplying both sides by Ak

Ak 1 − Mηk2 Mηk2

2

Ak Mηk2 − Ak+1 F (uk+1) 2 +

≥

F (vk)

2Ak 1 − Mηk2 Mηk2

−

F (uk+1), F (vk) − 2Ak F (uk+1) − F (uk), F (vk)

(C.7)

AkθL2 Mηk2

uk+1 − vk 2 − AkL2 uk − vk−1 2

+

2

2

2Ak Mηk2

−

F(vk) − F(vk)

− Ak F(vk−1) − F(vk−1)

.

To bound T[2], notice that F is monotone, so we have

###### F (uk+1),uk+1 − uk ≥ F (uk),uk+1 − uk .

Using the ﬁrst line in Eq. (C.4) for the RHS and the second line for the LHS, we can obtain

λk 1 − λk

F (uk+1),u0 − uk+1 ≥ λk F (uk),u0 − uk − ηk F (uk), F (vk)

ηk 1 − λk

+

F (uk+1), F (vk) .

Multiplying both sides by Bk

λk and using that Bk+1 = B

1−λk by Assumption 5, we have

k

Bkηk λk

Bkηk λk (1 − λk)

F (uk+1), F (vk) −

T[2] ≥

F (uk), F (vk)

Bkηk λk

F (uk+1) − F (uk), F (vk) .

= Bk+1ηk F (uk+1), F (vk) +

Combining Inequalities (C.7) and (C.8) and plugging the bounds into Eq. (C.5), we obtain

Vk − Vk+1 ≥

Ak 1 − Mηk2 Mηk2

Ak Mηk2 − Ak+1 F (uk+1) 2 +

F (vk)

Ak 1 − Mηk2 Mηk2 −

Bk+1ηk 2

− 2

F (uk+1), F (vk)

2

Bkηk λk − 2Ak F (uk+1) − F (uk), F (vk)

+

Akθ Mηk2 − ck+1 uk+1 − vk 2 + L2 (ck − Ak) uk − vk−1 2

+ L2

2

2

2Ak Mηk2

− Ak F(vk−1) − F(vk−1)

F(vk) − F(vk)

−

###### .

By Assumption 5, we choose Ak = B

kηk

2λk . Deﬁne: 

- Sk11 :=

Ak Mηk2 − Ak+1 =

Bk 2Mλkηk −

Bkηk+1 2(1 − λk)λk+1 Sk22 :=

Ak 1 − Mηk2 Mηk2

=

Bk 1 − Mηk2 2Mηkλk

- Sk12 :=




Ak 1 − Mηk2 Mηk2 −

Bk+1ηk 2



Then, we obtain

1 − λk − Mηk2 Bk 2M (1 − λk)λkηk

=

.

2

Vk − Vk+1 ≥ Sk11 F (uk+1) 2 + Sk22 F (vk)

− 2Sk12 F (uk+1), F (vk)

Akθ Mηk2 − ck+1 uk+1 − vk 2 + L2 (ck − Ak) uk − vk−1 2

+ L2

2

2

2Ak Mηk2

F(vk) − F(vk)

− Ak F(vk−1) − F(vk−1)

−

###### .

Suppose that Sk11 ≥ 0, Sk22 ≥ 0 and Sk11Sk22 = Sk12. Then, we can conclude

2

Vk − Vk+1 = Sk11F (uk+1) − Sk22 F (vk)

Akθ Mηk2 − ck+1 uk+1 − vk 2 + L2 (ck − Ak) uk − vk−1 2

+ L2

2

2

2Ak Mηk2

−

F(vk) − F(vk)

− Ak F(vk−1) − F(vk−1)

Akθ Mηk2 − ck+1 uk+1 − vk 2 + L2 (ck − Ak) uk − vk−1 2

≥ L2

2

2

2Ak Mηk2

−

F(vk) − F(vk)

− Ak F(vk−1) − F(vk−1)

###### .

(C.8)

To complete the proof, let us argue that the assumptions that Sk11 ≥ 0, Sk22 ≥ 0 and Sk11Sk22 = Sk12 we made above are valid. First, notice that Sk11 ≥ 0 is equivalent to ηk+1 ≤ λ

k+1(1−λk)

Mλkηk , and Sk22 ≥ 0 is equivalent to Mηk2 ≤ 1, which are both included in Assumption 5. Moreover, since Bk > 0, Sk11Sk22 = Sk12 is equivalent to

2

1 − Mηk2 Mηk ·

1 − λk − Mηk2 M (1 − λk)ηk

1 Mηk −

λkηk+1 (1 − λk)λk+1

,

=

(1−Mηk2−λ2k)

which is further equivalent to ηk+1 = λk+1

λk(1−λk)(1−Mηk2) ·ηk, provided that Mηk2 +λ2k ≤ 1. Both these inequalities hold by Assumption 5, thus completing the proof.

| |
|---|


Motivated by Assumption 5 and Lemma C.1, we make the choice of λk and ηk as

1 − λ2k − Mηk2 λk+1ηk (1 − Mηk2)(1 − λk)λk

1 k + 2

and ηk+1 :=

, (C.9)

λk :=

where M = 3L2 (2 + θ) and 0 < η0 < √21M . The sequence {ηk}k≥1 given by Eq. (C.9) is actually non-increasing and has a positive limit. We summarize this result in the following lemma for completeness, and the proof can be found in

(Tran-Dinh and Luo, 2021).

√3 2

- Lemma C.2. Given M > 0, the sequence {ηk} generated by Eq. (C.9) is non-increasing, i.e. ηk+1 ≤ ηk ≤ η0 <


M . Moreover, if 0 < η0 < √21M , we have that η∗ := limk→∞ ηk exists and

√

η0 1 − 2Mη02 1 − Mη02

> 0. (C.10)

η∗ ≥ η :=

We now prove the results for the iteration complexity and the corresponding oracle complexity for Algorithm 2.

Theorem 4.1. Given an arbitrary initial point u0 ∈ Rd and target error > 0, assume that the iterates uk evolve according to Algorithm 2 for k ≥ 1. Then, for all k ≥ 2,

Λ0 (k + 1)(k + 2)

E F(uk) 2 + 2L2 uk − vk−1 2 ≤

+ Λ1 2, (4.2)

2η0η+1) u0−u∗ 2

(1+Mηη0)

η2 and Λ1 = 5

where Λ0 = 4(L

Mη2 . In particular, E F(uN) 2 + 2L2 uN − vN−1 2 ≤ 2Λ1 2 = O( 2) after at most N =

√ √ΛΛ10 = O L u

0−u∗ iterations. The total number of oracle queries to F is O σ

2L u0−u∗ +L3 u0−u∗ 3

3 in expectation.

Proof. We start with verifying that the conditions in Eq. (C.2) of Lemma C.1 are all satisﬁed. By Eq. (C.9) and Lemma C.2, we know that {ηk} is non-increasing and η∗ = limk→∞ ηk > 0, so the ﬁrst condition in Eq. (C.2) is satisﬁed. Also, as 0 < ηk ≤ η0 ≤ √21M , we have Mηk2 ≤ Mη02 ≤ 12 < 1 − (k+2)1 2 . So the second condition in Eq. (C.2) holds. Moreover, since ηk+1 ≤ ηk, the third condition holds if ηk2 ≤ λ

k+1(1−λk)

Mλk = Mk(k+1+3). Due to the fact that

k+1 M(k+3) ≥ 3M1 and ηk ≤ η0 for all k ≥ 1, we can have this condition hold if η0 ≤ √31M . Hence all the conditions hold with our parameter update and letting η0 ≤ √31M .

Let ck = Ak, then we obtain

Akθ Mηk2 − ck+1 uk+1 − vk 2 + L2 (ck − Ak) uk − vk−1 2

L2

Akθ Mηk2 − Ak+1 uk+1 − vk 2

= L2

L2Bk 2

θ Mλkηk −

ηk+1 λk+1 (1 − λk)

uk+1 − vk 2 .

=

k+1(1−λk)

Here we choose the parameters such that ηkηk+1 ≤ θλ

kηk − η

Mλk = Mθ((kk+1)+3) to ensure Mλ θ

λk+1(1−λk) ≥ 0.

k+1

Since ηk+1 ≤ ηk, the required inequality holds if ηk ≤ Mθ((kk+1)+3), which is satisﬁed if we let η0 ≤ 3Mθ as ηk ≤ η0 for all k ≥ 1.

Combining the two conditions on η0, and choosing θ = 1, we have

1 √

η0 ≤

=

3M

1 3L√2 + θ

1 3L√3

=

,

which is required by Algorithm 2 and thus satisﬁed. Hence, with 0 < η0 ≤ 3L1√3, we have

Vk − Vk+1 ≥ L2

−

≥ −

Akθ Mηk2 − ck+1 uk+1 − vk 2 + L2 (ck − Ak) uk − vk−1 2

2

2

2Ak Mηk2

− Ak F(vk−1) − F(vk−1)

F(vk) − F(vk)

2

2

2Ak Mηk2

F(vk) − F(vk)

− Ak F(vk−1) − F(vk−1)

.

(C.11)

Consider Ck = Ak F(uk) 2 + Bk F(uk),uk − u0 . Then:

- (i) ≥ Ak F(uk) 2 + Bk F(uk) − F(u∗),uk − u∗ + Bk F(uk),u∗ − u0
- (ii)


Ck

Bk2 2Ak

Ak 2

F(uk) 2 −

u0 − u∗ 2

≥ Ak F(uk) 2 −

Bk2 2Ak

Ak 2

F(uk) 2 −

u0 − u∗ 2 ,

=

where (i) is due to u∗ being the solution to the monotone inclusion problem so an (SVI) solution as well, and we use monotonicity and Young’s Inequality for (ii). So we obtain

Ak 2

Bk2 2Ak

F(uk) 2 + AkL2 uk − vk−1 2 ≤ Ck + AkL2 uk − vk−1 2 +

Bk2 2Ak

u0 − u∗ 2 .

= Vk +

u0 − u∗ 2

Since Bk+1 = B

1−λk and λk = k+21 , we have Bk = (k + 1)B0 for any B0 > 0. Then we obtain Ak = ck = Bkηk

k

2 . By Lemma C.2, we know that 0 < η ≤ η∗ ≤ ηk ≤ η0, so B0(k+1)(2 k+2)η ≤ Ak = ck ≤ B0(k+1)(k+2)η0

2λk = B

0(k+1)(k+2)ηk

2 . By Inequality (C.11) and noticing v−1 = u0, we have

B0ηL2(k + 1)(k + 2) 2

B0η(k + 1)(k + 2) 4

uk − vk−1 2 ≤

F(uk) 2 +

Ak 2

F(uk) 2 + AkL2 uk − vk−1 2

Bk2 2Ak

u0 − u∗ 2

≤ Vk +

Bk2 2Ak

2

2Ak−1 Mηk2−1

u0 − u∗ 2 +

≤ Vk−1 +

F(vk−1) − F(vk−1)

+ Ak−1 F(vk−2) − F(vk−2)

2

###### .

Unrolling this recursive bound down to V0, we obtain

B0ηL2(k + 1)(k + 2) 2

B0η(k + 1)(k + 2) 4

F(uk) 2 +

uk − vk−1 2

k−1

k−1

Bk2 2Ak

2

2

2Ai Mηi2

u0 − u∗ 2 +

Ai F(vi−1) − F(vi−1)

F(vi) − F(vi)

≤ V0 +

+

i=0

i=0

B0(k + 1)2 η(k + 1)(k + 2)

(i) ≤ B0η0 F(u0) 2 +

u0 − u∗ 2

k−1

2

B0(i + 1)(i + 2) Mη

F(vi) − F(vi)

+

i=0

k−1

2

B0(i + 1)(i + 2)η0 2

F(vi−1) − F(vi−1)

+

,

i=0

where we plug in the bound for Ai and ηi in (i). Taking expectation with respect to all randomness on both sides and using the variance bound from Corollary 2.2, we obtain that

E F(uk) 2 + 2L2 uk − vk−1 2 ≤

B0(k + 1)2 η(k + 1)(k + 2)

4 B0η(k + 1)(k + 2)

B0η0 F(u0) 2 +

u0 − u∗ 2

k−1

2

B0(i + 1)(i + 2) Mη

E F(vi) − F(vi)

+

i=0

k−1

2

B0(i + 1)(i + 2)η0 2

E F(vi−1) − F(vi−1)

+

i=0

- (i)

≤

4 η(k + 1)(k + 2)

L2η0 +

1 η

u0 − u∗ 2 +

2 Mη

+ η0 + 3η0

2

8

+

k−1

i=1

(i + 1)(i + 2) Mη

2

i

+

k−1

i=2

(i + 1)(i + 2)η0 2

2

i − 1

- (ii)

≤

4 L2η0η + 1 u0 − u∗ 2 η2(k + 1)(k + 2)

+

1 + 2Mηη0 Mη(k + 1)(k + 2)

2

+

4(k − 1)(k + 4) Mη2(k + 1)(k + 2)

2 +

4η0(k − 2)(k + 3) η(k + 1)(k + 2)

2

- (iii)


4 L2η0η + 1 u0 − u∗ 2 η2(k + 1)(k + 2)

1 + 2Mηη0 Mη2(k + 1)(k + 2)

4 1 + Mη0η Mη2

2 +

≤

+

2,

where we use Lipschitz property and variance bounds by variance reduction for (i). For (ii), we use the fact that i+1i ≤ 2 and ii−+21 ≤ 4 and sum over 2(i + 1), respectively. Moreover, (iii) is due to ((kk−+1)(1)(kk+3)+4) ≤ 1 and ((kk−+1)(2)(kk+2)+3) ≤ 1 and by combining the last two terms.

√√ΛΛ10 = O L u

(L2η0η+1) u0−u∗ 2 η2 and Λ1 = 5

(1+Mηη0) Mη2 , we have

0−u∗ , where Λ0 = 4

When k ≥

Λ0 (k + 1)(k + 2)

E F(uk) 2 + 2L2 uk − vk−1 2 ≤

+ Λ1 2 ≤ 2Λ1 2. Claimed stochastic oracle complexity follows from Lemma C.3 below.

| |
|---|


- Lemma C.3. Let u0 ∈ Rd be an arbitrary initial point and assume that iterates uk evolve according to Algorithm 2.


2L u0−u∗ +L3 u0−u∗ 3 3

Then, Algorithm 2 returns a point uN such that E F(uN) 2 ≤ 2Λ1 2 after at most O σ

stochastic queries to F.

Proof. Let mk be the number of stochastic queries made by the variance reduction method at iteration k for k ≥ 1. Conditional on Fk−1, we have

E mk+1|Fk−1 = E pkS1(k) + 2(1 − pk)S2(k) Fk−1

8L2 vk − vk−1 2 p2k 2

8σ2 pk 2

+ 2(1 − pk)

= pk

8L2 vk − vk−1 2 p2k 2

8σ2 pk 2

(i) ≤ pk

+ 1 + 2(1 − pk)

+ 1 ,

where (i) is due to the fact that x ≤ x + 1 for any x ∈ R. Taking expectation with respect to all randomness on both sides, and rearranging the terms, we obtain

16(1 − pk)L2E vk − vk−1 2 p2k 2

8σ2 2 +

E[mk+1] ≤

+ 2.

2

With m0 = m1 = S1(0) = 8σ

2 , let M be the total number of stochastic queries up to iteration N such that E[ F(uk) ] ≤ 2Λ1 for all k ≥ N, we have

N

N

8σ2 2 + E

E[M] = E

mk = 2

mk

k=0

k=2

N

16(1 − pk)L2E vk − vk−1 2 p2k 2

16σ2 2 + 2 +

8σ2 2 +

≤

+ 2

k=1

N

(1 − pk)E vk − vk−1 2 p2k

8σ2∆ 3 +

16σ2 2 +

16L2

(i)

2∆

, (C.12)

≤

+

2

k=1

where (i) follows from N ≤ ∆ with ∆ = Λ

###### Λ1 + , and 1 − pk ≤ 1.

0

Then we come to bound E vk − vk−1 2 . Notice that for k ≥ 1

vk − vk−1 = vk − uk+1 + uk+1 − uk + uk − vk−1

(=i) ηk F(vk) − F(vk−1) − ηk−1 F(vk−1) − F(vk−2) + uk+1 − uk

= ηk F(vk) − ηk + ηk−1 F(vk−1) + ηk−1 F(vk−2) + uk+1 − uk,

where (i) is based on the third line in Eq. (C.4). To estimate uk+1 − uk, we recursively use the ﬁrst line in Eq. (C.4), and obtain for k ≥ 2,

uk+1 − uk = λk (u0 − uk) − ηk F (vk)

= λk (1 − λk−1)(u0 − uk−1) + λkηk−1 F (vk−1) − ηk F (vk)

k−2

k−1

(1 − λj) ηi F(vi) + λkηk−1 F (vk−1) − ηk F (vk)

= λk

i=0

j=i+1

k−2

ηk−1 k + 2

i + 2 (k + 2)(k + 1)

F(vk−1) − ηk F(vk).

ηi F(vi) +

=

i=0

So we have

uk+1 − uk =



−η0 F(v0) if k = 0,



λ1η0 F(v0) − η1 F(v1) if k = 1,



k−2 i=0

(k+2)(k+1)ηi F(vi) + η

k+2 F(vk−1) − ηk F(vk) if k ≥ 2.

i+2

k−1

(C.13)

Then we obtain for k ≥ 3

vk − vk−1 2

2

k−2

ηk−1 k + 2 − ηk − ηk−1 F(vk−1) + ηk−1 F(vk−2) +

i + 2 (k + 2)(k + 1)

=

ηi F(vi)

i=0

2

2

2

2

ηk−1 k + 2 − ηk − ηk−1

kηk−2 (k + 1)(k + 2)

≤ 3

F(vk−2)

F(vk−1)

+ 3 ηk−1 +

k−3

3(i + 2)2(k − 2) k2(k + 1)2

2

ηi2 F(vi)

+

i=0

k−3

3(i + 2)2 k(k + 1)2

2

2

2

≤ η02 12 F(vk−1)

η02 F(vi)

+

+ 5 F(vk−2)

###### .

i=0

Taking expectation with respect to all randomness on both sides, we have

E vk − vk−1 2 ≤ η02 12E F(vk−1)

2

+ 5E F(vk−2)

2

k−3

3(i + 2)2 k(k + 1)2

η02E F(vi)

+

i=0

2

###### .

Note that for k ≥ 1, we have

2

≤ 2E F(uk+1) 2 + 4E F(uk+1) − F(vk) 2 + 4E F(vk) − F(vk)

E F(vk)

- (i) ≤ 2E F(uk+1) 2 + 2L2 uk+1 − vk 2 + 4

2

k

- (ii)


2

Λ0 (k + 1)2

+ Λ1 2 + 4

≤ 2

,

k

2

where (i) is due to the Lipschitz property and the variance bound, and we use the result of Theorem 4.1 for (ii). Proceeding similarly, we have E F(v0)

2

2

2 , so we obtain for k ≥ 4,

≤ 2 Λ0 + Λ1 2 +

E vk − vk−1 2

k−3

3(i + 2)2 k(k + 1)2

2

2

≤ η02 12 F(vk−1)

η02 F(vi)

+

+ 5 F(vk−2)

i=0

2

2

Λ0 k2

Λ0 (k − 1)2

≤ η02 24

+ Λ1 2 + 2

+ Λ1 2 + 2

+ 10

k − 1

k − 2

k−3

12η02 k(k + 1)2

2

6(i + 2)2 k(k + 1)2

Λ0 (i + 1)2

2 Λ0 + Λ1 2 +

η02

+

+

2

i=1

k−3

Λ1 2 k

Λ0 (k − 1)2

4Λ0 k(k + 1)2

≤ 40η02

+ 35η02 (Λ1 + 1) 2 + 6η02

+

+

i=1

Λ0 (k − 1)2

4Λ0 (k + 1)2

≤ 40η02

+ 35η02 (Λ1 + 1) 2 + 6η02

+ (Λ1 + 2) 2

40 (k − 1)2

24 (k + 1)2

= η02Λ0

+ 41η02 (Λ1 + 2) 2.

+

2

2

+ Λ1 2 + 2

i

2 2 k

Since pk = k+12 , we have for k ≥ 4

E vk − vk−1 2 p2k ≤

(k + 1)2 4

24 (k + 1)2

40 (k − 1)2

+ 41η02 (Λ1 + 2) 2

η02Λ0

+

≤ 30η02Λ0 + 11η02 (Λ1 + 2) 2(k + 1)2 (i) ≤ 30η02Λ0 + 11η02 (Λ1 + 2) 2

∆2

2

= 30η02Λ0 + 11η02 (Λ1 + 2)∆2, where (i) is due to k ≤ N < ∆ . So we obtain

N

N

(1 − pk)E vk − vk−1 2 p2k ≤

E vk − vk−1 2 p2k

k=4

k=1

N

30η02Λ0 + 11η02 (Λ1 + 2)∆2

≤

k=1

∆ 30η02Λ0 + 11η02 (Λ1 + 2)∆2

≤

. For k = 3, we have

(1 − p3)E v3 − v2 2 p23

= 2E v3 − v2 2 ≤ 2 10η02Λ0 + 35η02 (Λ1 + 2) 2 . Moreover, we have

(1 − p2)E v2 − v1 2 p22

3 4

E v2 − v1 2

=

2

2

2

2

3 2

η0 6

- 3η1

- 4


E

≤

+ η1

+ η2

F(u0)

+

F(u1)

49 16

Λ0 2

3 2

49 36

+ 2Λ1 2 + 4 2 ≤ 7η02Λ0 + 14(Λ1 + 2) 2.

η02

2Λ0 + 2Λ1 2 + 2/2 +

≤

Note that p1 = 1, so we have

N

(1 − pk)E vk − vk−1 2

16σ2 2 +

16L2

8σ2∆ 3 +

2∆

E[M] ≤

+

p2k ≤

2

k=1

16L2∆ 24η02Λ0 + 5η02 (Λ1 + 2)∆2

8σ2∆ 3 +

16σ2 2 +

2∆

+

3

32L2 10η02Λ0 + 35η02 (Λ1 + 2) 2 2 +

16L2 7η02Λ0 + 14(Λ1 + 2) 2

+

2

σ2L u0 − u∗ + L3 u0 − u∗ 3 3 ,

= O

where we assume without loss of generality that L u0 − u∗ ≥ 1, thus completing the proof.

| |
|---|


### D Omitted proofs from Section 5

Theorem 5.1. Given F that is L-Lipschitz and µ-sharp and the precision parameter , Algorithm 3 outputs uN with

0−u∗ iterations with at most O σ

###### E[ uN − u∗ 2] ≤ 2 as well as E F(uN) 2 ≤ L2 2 after N = O Lµ log u

2(µ+L) log( u0−u∗ / )+L3 u0−u∗ 2

µ3 2 queries to F in expectation.

Proof. Let Gk−1 be the natural ﬁltration of all the random variables used up to (and including) the (k − 1)th outer loop. By Theorem 4.1, we have

Λ(0k) (K + 1)(K + 2)

+ Λ(1k) 2k, (D.1)

E F(uk) 2 |Gk−1 ≤

2η0η+1) uk−1−u∗ 2

(1+Mηη0)

η2 and Λ(1k) = 5

where Λ(0k) = 4(L

Mη2 . By the sharpness condition, we have

1 µ

uk − u∗ 2 ≤

- (i)

≤

1 µ

F(uk),uk − u∗

- (ii)


1 µ

≤

F(uk) − F(u∗),uk − u∗

F(uk) uk − u∗ ,

where (i) is because u∗ is a solution to (SVI), and we use Cauchy-Schwarz inequality for (ii). Taking expectation conditional on Gk−1 on both sides, we have

E F(uk) 2 |Gk−1 ≥ E µ2 uk − u∗ 2 |Gk−1 , which leads to

Λ(0k) (K + 1)(K + 2)

1 µ2

+ Λ(1k) 2k .

E uk − u∗ 2 |Gk−1 ≤

√

(k) 0

L2η0η+1

2 uk−1−u∗ 2

If we choose K ≥ 4

µη , we have Λ

(K+1)(K+2) ≤ µ

4 . On the other hand, by our choice of k in Algorithm 3, we obtain

µ2 2Mη2 20 1 + Mηη0 ≤

µ2 2 4

5 1 + Mηη0 Mη2

Λ(1k) 2k ≤

.

So we have

uk−1 − u∗ 2

2

E uk − u∗ 2 |Gk−1 ≤

. Taking expectation with respect to all the randomness on both sides, we obtain

+

4

4

E uk−1 − u∗ 2 4

E uk − u∗ 2 ≤

+

Recursively using Inequality (D.2) till k = 0, we have

2

. (D.2)

4

1 4k

E uk − u∗ 2 ≤

k

2

1 4k

u0 − u∗ 2 +

4i ≤

i=1

∞

2

1 4k

u0 − u∗ 2 +

4i ≤

i=1

u0 − u∗ 2 +

- 2

- 3


###### .

√6 u0−u∗

2 outer loops, the Algorithm 3 can output a point uk such that E uk − u∗ 2 ≤

Hence, after log

2, as well as E F(uk) 2 ≤ L2 2. More speciﬁcally, the total number of iterations such that the algorithm can return a point uk such that E uk − u∗ 2 ≤ 2 will be

√6 u0 − u∗ 2

4 L2η0η + 1 µη

u0 − u∗

L µ

= O

log

log

.

Next we come to bound the expected number of the stochastic oracle queries for each call to Algorithm A. Denote i-th iterate in k-th call as u(ik) and vi(k), and let K = 4

√

L2η0η+1

µη , then proceeding as in the proof of Corollary C.3,

we obtain

K

m(ik) Gk−1

E Mk|Gk−1 = E

i=0

2

16(1 − pi)L2E vi(k) − vi(−k)1

Gk−1 p2i 2k

K

16σ2

8σ2

(D.3)

≤

+ 2

+ 2 +

+

2 k

2 k

i=1

2

16(1 − pi)L2E vi(k) − vi(−k)1

Gk−1 p2i 2k

K

16σ2

8σ2K

,

=

+ 2(K + 1) +

+

2 k

2 k

i=1

√

L2η0η+1

where Mk is the total number of queries at the kth call. Notice that K = 4

###### µη = O Lµ and 2k =

2

E vi(k)−vi(−k)1

µ2 2Mη2 20(1+Mηη0)

p2i for 1 ≤ i ≤ K. The proof of Lemma C.3 shows that for i ≥ 4

= O µ2 2 , then it remains to bound

2

E vi(k) − vi(−k)1

Gk−1 p2i ≤ 30η02Λ(0k) + 11η02 Λ(1k) + 2 2k(i + 1)2.

2

(k) i −vi(−k)1

On the other hand, for 1 ≤ i ≤ 3, we have 3i=1 E v

2 uk−1−u∗ 2 ), we obtain

p2i = o(L

2

16(1 − pi)L2E vi(k) − vi(−k)1

Gk−1 p2i 2k

K

= O

i=1

L3 uk−1 − u∗ 2 µ3 2

.

Combining last inequality with Inequality (D.3) and taking expectations on both sides, we obtain

E[Mk] = O

σ2(µ + L) + L3E uk−1 − u∗ 2 µ3 2

Telescoping from k = 1 to N = log

√6 u0−u∗

2 and noticing that

.

E uk − u∗ 2 ≤

1 4

E uk−1 − u∗ 2 +

2

4 ≤

we have

∞

N

1 4k

E uk−1 − u∗ 2 ≤ u0 − u∗ 2

+

k=1

k=1

Hence, we ﬁnally arrive at

1 4k

u0 − u∗ 2 +

- 2

- 3


,

u0 − u∗ 2

N 2 3 ≤

+

3

N 2 3

.

E

N

Mk = O

k=1

σ2(µ + L)log( u0 − u∗ / ) + L3 u0 − u∗ 2 µ3 2

,

which completes the proof.

| |
|---|


