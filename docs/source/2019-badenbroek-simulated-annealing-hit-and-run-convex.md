---
type: source
kind: paper
title: "Simulated annealing with hit-and-run for convex optimization: rigorous complexity analysis and practical perspectives for copositive programming"
authors: Riley Badenbroek, Etienne de Klerk
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1907.02368v1
source_local: ../raw/2019-badenbroek-simulated-annealing-hit-and-run-convex.pdf
topic: general-knowledge
cites:
---

arXiv:1907.02368v1[math.OC]4Jul2019

Simulated annealing with hit-and-run for convex optimization: rigorous complexity analysis and practical perspectives for copositive programming

Riley Badenbroek Etienne de Klerk July 5, 2019

Abstract

We give a rigorous complexity analysis of the simulated annealing algorithm by Kalai and Vempala [Math of OR 31.2 (2006): 253-266] using the type of temperature update suggested by Abernethy and Hazan [arXiv 1507.02528v2, 2015]. The algorithm only assumes a membership oracle of the feasible set, and we prove that it returns a solution in polynomial time which is near-optimal with high probability. Moreover, we propose a number of modiﬁcations to improve the practical performance of this method, and present some numerical results for test problems from copositive programming.

Keywords: Simulated annealing, convex optimization, hit-and-run sampling, semideﬁnite and copositive programming

# 1 Introduction

Let K ⊆ Rn be a convex body, and suppose that only a membership oracle of K is available. Fix a vector c ∈ Rn, and let  ·,·  be an inner product on Rn. We are interested in the problem

min

c,x . (1)

x∈K

One approach to solve problems of this type is using simulated annealing, a paradigm of randomized algorithms for general optimization introduced by Kirkpatrick et al. [13]. It features a so-called temperature parameter that decreases during the run of the simulated annealing algorithm. At high temperatures, the method explores the feasible set relatively freely, also moving to solutions that have worse objective values than the current point. As the temperature decreases, so does the probability that a solution with a worse objective value is accepted. Kalai and Vempala [10] showed that, for convex optimization, a polynomialtime simulated annealing algorithm exists. Speciﬁcally, their algorithm returns a feasible solution that is near-optimal with high probability in polynomial time.

Abernethy and Hazan [1] recently clariﬁed that Kalai and Vempala’s algorithm is in some sense equivalent to an interior point method. In general, interior point methods for convex bodies require a so-called selfconcordant barrier of the feasible set. It was shown by Nesterov and Nemirovskii [18] that every open convex set that does not contain an aﬃne subspace is the domain of a self-concordant barrier, known as the universal barrier. However, it is not known how to compute the gradients and Hessians of this barrier in general.

The interior point method to which Kalai and Vempala’s algorithm corresponds uses the so-called entropic barrier over K, to be deﬁned later. This barrier was introduced by Bubeck and Eldan [6], who also established the self-concordance of the barrier and analyzed its complexity parameter ϑ.

Drawing on the connection to interior point methods, Abernethy and Hazan [1] proposed a new temperature schedule for Kalai and Vempala’s algorithm. This schedule does not depend on the dimension n of the problem, but on the complexity parameter ϑ of the entropic barrier. Our goal is to prove in detail

that simulated annealing with this new temperature schedule returns a solution in polynomial time which is near-optimal with high probability. Moreover, we aim to investigate the practical applicability of this method.

- 1.1 Algorithm Statement


Central to Kalai and Vempala’s algorithm is a family of exponential-type probability distributions known as Boltzmann distributions.

- Deﬁnition 1. Let K ⊆ Rn be a convex body, and let θ ∈ Rn. Let  ·,·  be the Euclidean inner product. Then, the Boltzmann distribution with parameter θ is the probability distribution supported on K having density with respect to the Lebesgue measure proportional to x  → e θ,x .

Throughout this work, we will use Σ(θ) to refer to the covariance matrix of the Boltzmann distribution with parameter θ ∈ Rn. If  ·,·  is some reference inner product, then x,y θ := x,Σ(θ)y for any θ ∈ Rn. Moreover, let · θ denote the norm induced by the inner product  ·,· θ.

As mentioned above, Abernethy and Hazan’s temperature schedule depends on the complexity parameter of the entropic barrier. This function is deﬁned as follows.

- Deﬁnition 2. Let K ⊆ Rn be a convex body. Deﬁne the function f : Rn → R as f(θ) = ln K e θ,x dx. Then, the convex conjugate f∗ of f,


is called the entropic barrier for K.

f∗(x) = sup θ∈Rn

{ θ,x − f(θ)} ,

Bubeck and Eldan [6] showed that f∗ is a self-concordant barrier for K with complexity parameter ϑ ≤ n + o(n). The complexity parameter of f∗ is

Df∗(x),[D2f∗(x)]−1Df∗(x) = sup θ∈Rn

θ 2θ, (2)

ϑ := sup

θ,Σ(θ)θ = sup

θ∈Rn

x∈K

where we refer the reader to [2, inequality (13)] for details.

The procedure Kalai and Vempala [10] use to generate samples on K is called hit-and-run sampling. This Markov Chain Monte Carlo method was introduced by Smith [20] to sample from the uniform distribution over a bounded convex set. Later, it was generalized to absolutely continuous distributions (see for example B´elisle et al. [3]). The details of hit-and-run sampling are given in Algorithm 1.

![image 1](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile1.png>)

- Algorithm 1 The hit-and-run sampling procedure Input: Oracle for a convex body K ⊆ Rn; probability distribution µ to sample from (i.e. the target


![image 2](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile2.png>)

distribution); covariance matrix Σ ∈ Rn×n; starting point x ∈ K; number of hit-and-run steps ℓ ∈ N.

- 1: X0 ← x
- 2: for i ∈ {1,...,ℓ} do
- 3: Sample direction Di from a N(0,Σ)-distribution
- 4: Sample Xi from the univariate distribution µ restricted to K ∩ {Xi−1 + tDi : t ∈ R}
- 5: end for
- 6: return Xℓ


![image 3](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile3.png>)

The algorithm by Kalai and Vempala [10] that uses a temperature schedule of the type introduced by Abernethy and Hazan [1] is now given in Algorithm 2. Note in particular that the temperature parameter in iteration k of Algorithm 2 is given by Tk.

![image 4](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile4.png>)

- Algorithm 2 Algorithm by Kalai and Vempala [10] using temperature schedule of type introduced by Abernethy and Hazan [1]


![image 5](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile5.png>)

Input: unit vector c ∈ Rn; membership oracle OK : Rn → {0,1} of a convex body K; radius R of Euclidean ball containing K; complexity parameter ϑ ≤ n + o(n) of the entropic barrier over K; x0 ∈ K drawn randomly from the uniform distribution over K; update parameter α > 1 + 1/

√

![image 6](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile6.png>)

ϑ; number of phases m ∈ N; number of hit-and-run steps ℓ ∈ N; number of covariance update samples N ∈ N; approximation Σ(0) of Σ(0) satisfying 12v⊤ Σ(0)v ≤ v⊤Σ(0)v ≤ 2v⊤ Σ(0)v for all v ∈ Rn; starting temperature T0 = R.

![image 7](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile7.png>)

Output: xm such that c,xm − minx∈K c,x ≤ ǫ¯ at terminal iteration m.

- 1: X0 ← x0
- 2: θ0 = 0
- 3: for k ∈ {1,...,m} do
- 4: Tk ← 1 − α√1ϑ Tk−1

![image 8](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile8.png>)

![image 9](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile9.png>)

- 5: θk ← −c/Tk
- 6: Generate Xk by applying hit-and-run sampling to the Boltzmann distribution with parameter θk, starting the walk from Xk−1, taking ℓ steps, drawing directions from a N(0, Σ(θk−1))-distribution
- 7: for j ∈ {1,...,N} do
- 8: Generate Yjk by applying hit-and-run sampling to the Boltzmann distribution with parameter θk, starting the walk from Xk−1, taking ℓ steps, drawing directions from a N(0, Σ(θk−1))-distribution
- 9: end for
- 10: Σ(θk) ← N1 Nj=1 YjkYjk⊤ − N 1 Nj=1 Yjk N 1 Nj=1 Yjk

![image 10](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile10.png>)

![image 11](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile11.png>)

![image 12](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile12.png>)

⊤

- 11: end for
- 12: return Xm


![image 13](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile13.png>)

In their original paper, Kalai and Vempala [10] show that the algorithm returns a near-optimal solution with high probability, for the temperature update (cf. line 4 in Algorithm 2)

1 √n

Tk = 1 −

Tk−1, (3)

![image 14](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile14.png>)

![image 15](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile15.png>)

in m = O∗(√n) iterations, where O∗ suppresses polylogarithmic terms in the problem parameters. Abernethy and Hazan [1] propose the alternative temperature update

![image 16](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile16.png>)

1 4

√

Tk = 1 −

Tk−1, (4)

![image 17](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile17.png>)

![image 18](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile18.png>)

ϑ

√

![image 19](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile19.png>)

which will lead to m = O∗(

ϑ) iterations. As noted above, we have ϑ ≤ n + o(n) in general, but it is not currently known if ϑ < n for any convex bodies. In particular, the temperature update (4) only improves on (3) if ϑ < n/16, which is not known to hold for any convex body. We show in Appendix A to this paper that, for the Euclidean unit ball in Rn, numerical evidence suggests that ϑ = (n + 1)/2. We therefore consider a variation on the temperature schedule (4) suggested by Abernethy and Hazan, namely

1 α

√

Tk = 1 −

![image 20](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile20.png>)

![image 21](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile21.png>)

ϑ

Tk−1 for some α > 1 + 1/

√

![image 22](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile22.png>)

ϑ, (5)

which corresponds to (4) when α = 4, but gives larger temperature reductions when α < 4. We will refer to (5) as Abernethy-Hazan-type temperature updates. If ϑ < n, this results in a larger temperature decrease than the Kalai and Vempala [10] scheme (3), for a suitable choice of the parameter α.

- 1.2 Outline of this paper


Abernethy and Hazan [1] do not give a rigorous analysis of the temperature schedule (4) in their paper, only a sketch of the proof. In this paper we provide the full details for the more general schedule (5). We start with a review of useful facts on probability distributions in Section 2, followed by a section on mixing conditions for hit-and-run sampling in Section 3. In Section 4 we give the main analysis on the rate of convergence of Algorithm 2. In doing so, we also provide some details that were omitted in the original work by Kalai and Vempala [10], that concerns the application of a theorem by Rudelson [19]. In the remainder of the paper, we discuss the perspectives for practical computation with Algorithm 2. In Section 5, we look at the behavior of hit-and-run sampling for optimization over the doubly nonnegative cone, and suggest some heuristic improvements to obtain speed-up. We then evaluate the resulting algorithm on problems from copositive programming (due to Berman et al. [4]) in Section 6.

# 2 Preliminaries on probability distributions

Below, we will deﬁne some tools necessary for the analysis of Kalai and Vempala’s algorithm with the type of temperature schedule by Abernethy and Hazan. We start with the notion of isotropy.

- Deﬁnition 3. Let (K,E) be a measurable space with K ⊆ Rn, and ǫ ≥ 0. Let  ·,·  be the Euclidean inner product. A probability distribution µ over (K,E) is (1 + ǫ)-isotropic if for every v ∈ Rn,

1 1 + ǫ

![image 23](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile23.png>)

v 2 ≤

K

v,x − Eµ[X] 2 dµ(x) ≤ (1 + ǫ) v 2.

Moreover, we will need two measures of divergence between probability distributions. Before we can deﬁne them, we recall the deﬁnition of absolute continuity.

- Deﬁnition 4. Let (K,E) be a measurable space, and let ν and µ be measures on this space. Then, ν is absolutely continuous with respect to µ if µ(A) = 0 implies ν(A) = 0 for all A ∈ E. We write this property as ν ≪ µ.

The ﬁrst measure of divergence between probability distributions is the L2-norm.

- Deﬁnition 5. Let (K,E) be a measurable space. Let ν and µ be two probability distributions over this space, such that ν ≪ µ. Then, the L2-norm of ν with respect to µ is


2

dν dµ

dν dµ

ν/µ :=

dµ,

dν =

![image 24](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile24.png>)

![image 25](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile25.png>)

K

K

where ddµν is the Radon-Nikodym derivative of µ with respect to ν. It is easily shown that the L2-norm is invariant under invertible aﬃne transformations.

![image 26](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile26.png>)

Lemma 6. Let (K,E) be a measurable space, and suppose K ⊆ Rn. Let ν and µ be two probability measures over this space having densities hν and hµ with respect to the Lebesgue measure, respectively. Let A : Rn → Rn be an invertible linear operator and write K := {Ax : x ∈ K}. Deﬁne the transformed probability density hν : K → R+ by hν(y) = det(A−1)hν(A−1y), and similarly for hµ. Denote their induced distributions over K by ν and µ. Then,

![image 27](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile27.png>)

![image 28](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile28.png>)

![image 29](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile29.png>)

![image 30](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile30.png>)

![image 31](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile31.png>)

![image 32](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile32.png>)

![image 33](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile33.png>)

![image 34](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile34.png>)

ν/µ = ν/µ . The second measure of divergence between probability distributions is the total variation distance.

![image 35](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile35.png>)

![image 36](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile36.png>)

Deﬁnition 7. Let (K,E) be a measurable space. For two probability distributions µ and ν over this space, their total variation distance is

µ − ν := sup

|µ(A) − ν(A)|.

A∈E

A useful property of the total variation distance is that it allows coupling of random variables, in the sense of the following lemma.

Lemma 8 (e.g. Proposition 4.7 in [14]). Let X be a random variable on K ⊆ Rn with distribution µ, and let ν be a diﬀerent probability distribution on K. If µ − ν = α, there exists a random variable Y on K distributed according to ν such that the joint distribution of X and Y satisﬁes P{X = Y } = 1 − α.

# 3 Mixing Conditions

The main purpose of this section is to study how we can use hit-and-run sampling to approximate covariance matrices of Boltzmann distributions as in Line 10 of Algorithm 2. Our ﬁrst step is showing that hit-andrun indeed mixes in our setting. While Theorem 4.7 in [2] gives conditions under which it can be done, it depends on an approximation of an inverse covariance matrix. In Kalai and Vempala’s algorithm, it is more convenient to maintain that we have an approximation of a covariance matrix, not necessarily its inverse. We therefore state the following mixing theorem.

Theorem 9. Let K ⊆ Rn be a convex body, and let  ·,·  be the Euclidean inner product. Let q > 0, and θ0,θ1 ∈ Rn such that ∆θ := max{ θ1 − θ0 θ

. Pick ǫ ≥ 0, and suppose we have an invertible matrix Σ(θ0) such that 1 1 + ǫ

1} < 1. Deﬁne ∆θ0 := θ1 − θ0 θ

, θ1 − θ0 θ

0

0

v⊤ Σ(θ0)v ≤ v⊤Σ(θ0)v ≤ (1 + ǫ)v⊤ Σ(θ0)v ∀v ∈ Rn. (6)

![image 37](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile37.png>)

Consider a hit-and-run random walk applied to the Boltzmann distribution µ with parameter θ1 from a random starting point drawn from a Boltzmann distribution with parameter θ0. Let ν(ℓ) be the distribution of the hit-and-run point after ℓ steps of hit-and-run sampling applied to µ, where the directions are drawn from a N(0, Σ(θ0))-distribution. Then, after

256 exp(−2∆θ0)n√n(1 + ǫ) (1 − ∆θ0)2(1 − ∆θ)2 exp(2∆θ)q2

16384e21030n3(1 + ǫ)2 (1 − ∆θ)4 exp(4∆θ)

2 exp(−2∆θ0) (1 − ∆θ0)2q2

![image 38](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile38.png>)

ln3

ln2

ℓ =

, (7)

![image 39](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile39.png>)

![image 40](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile40.png>)

![image 41](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile41.png>)

hit-and-run steps, we have ν(ℓ) − µ ≤ q.

Proof. To show the claim, we will prove that conditions (i)-(iii) from Corollary 4.2 in [2] are satisﬁed. As in Kalai and Vempala [10], the three conditions will follow if the distribution to sample from, i.e. µ, is near-isotropic after K is transformed by Σ(θ0)−1/2.

Denote the Boltzmann distributions over K with parameter θ0 by ν. With v = Σ(θ0)−1/2u, (6) is equivalent to 1+1ǫ u 2 ≤ u⊤ Σ(θ0)−1/2Σ(θ0) Σ(θ0)−1/2u ≤ (1 + ǫ) u 2. In other words,

![image 42](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile42.png>)

2

e θ

0,x dx

u⊤ Σ(θ0)−1/2(x − Eθ

[X])

1 1 + ǫ

u 2 ≤ K

0

K e θ0,x dx ≤ (1 + ǫ) u 2. With a change of variables y = Σ(θ0)−1/2x, this result is equivalent to

![image 43](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile43.png>)

![image 44](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile44.png>)

1 1 + ǫ

![image 45](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile45.png>)

2

0)1/2θ0,y dy Σ(θ0)−1/2K e Σ(θ0)1/2θ0,y dy

e Σ(θ

−1/2K u⊤(y − Σ(θ0)1/2Eθ

[X])

u 2 ≤ Σ(θ0)

0

≤ (1 + ǫ) u 2,

![image 46](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile46.png>)

where Σ(θ0)1/2Eθ

[X] equals

0

Σ(θ0)−1/2xe θ

0,x dx K e θ0,x dx

Σ(θ0)−1/2Eθ

[X] = K

![image 47](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile47.png>)

0

0)1/2θ0,y dy Σ(θ0)−1/2K e Σ(θ0)1/2θ0,y dy

−1/2K ye Σ(θ

= Σ(θ0)

.

![image 48](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile48.png>)

Hence, (6) is equivalent to the statement that the Boltzmann distribution with parameter Σ(θ0)1/2θ0 over

- Σ(θ0)−1/2K is in (1 + ǫ)-isotropic position. Let us refer to this distribution as ν, and to the Boltzmann


![image 49](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile49.png>)

distribution over the same body with parameter Σ(θ0)1/2θ1 as µ. By Lemma 4.3 from Kalai and Vempala [10], µ is t-isotropic with

![image 50](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile50.png>)

![image 51](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile51.png>)

t = 16(1 + ǫ)max{ ν/µ , µ/ν } = 16(1 + ǫ)max{ ν/µ , µ/ν },

![image 52](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile52.png>)

![image 53](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile53.png>)

![image 54](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile54.png>)

![image 55](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile55.png>)

where the ﬁnal equality is due to Lemma 6. To upper bound the L2-norms between µ and ν, we use the fact that they are Boltzmann distributions. By Lemma 4.5 in [2], the value of t can therefore be bounded by

1}) (1 − max{ θ1 − θ0 θ

, θ1 − θ0 θ

exp(−2 max{ θ1 − θ0 θ

exp(−2∆θ) (1 − ∆θ)2

0

t ≤ 16(1 + ǫ)

= 16(1 + ǫ)

.

![image 56](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile56.png>)

![image 57](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile57.png>)

1})2

, θ1 − θ0 θ

0

Kalai and Vempala [10, Lemma 4.2] show that the level set of µ with probability 18 contains a Euclidean ball of radius 8e1√t and Eµ[ Y −Eµ[Y ] 2] ≤ tn. Transforming back to K, we have that the level set of µ with probability 18 contains a · Σ(θ

![image 58](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile58.png>)

![image 59](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile59.png>)

![image 60](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile60.png>)

![image 61](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile61.png>)

![image 62](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile62.png>)

![image 63](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile63.png>)

0)−1-ball with radius 8e1√t and Eµ[ X − Eµ[X] 2 Σ(θ

0)−1] ≤ tn. Since Lemma

![image 64](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile64.png>)

![image 65](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile65.png>)

![image 66](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile66.png>)

- 4.5 in [2] can be used to upper bound ν/µ , all conditions for Corollary 4.2 in [2] are satisﬁed, which proves the statement.


![image 67](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile67.png>)

![image 68](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile68.png>)

![image 69](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile69.png>)

![image 70](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile70.png>)

In iteration k of Algorithm 2, one uses the temperature update (5), as well as sampling from the Boltzmann distribution with parameter θk := −c/Tk. For these parameters, we can derive the following corollary to Theorem 9.

Corollary 10. Let K ⊆ Rn be a convex body, and let  ·,·  be the Euclidean inner product. Let q > 0, and θ0,θ1 ∈ Rn such that θ1 = θ0/(1 − α√1ϑ), where ϑ is the complexity parameter of the entropic barrier over K, and α > 1 + 1/

![image 71](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile71.png>)

![image 72](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile72.png>)

√

![image 73](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile73.png>)

ϑ. Pick ǫ ≥ 0, and suppose we have an invertible matrix Σ(θ0) such that

1 1 + ǫ

v⊤ Σ(θ0)v ≤ v⊤Σ(θ0)v ≤ (1 + ǫ)v⊤ Σ(θ0)v ∀v ∈ Rn. (8)

![image 74](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile74.png>)

Consider a hit-and-run random walk applied to the Boltzmann distribution µ with parameter θ1 from a random starting point drawn from a Boltzmann distribution with parameter θ0. Let ν(ℓ) be the distribution of the hit-and-run point after ℓ steps of hit-and-run sampling applied to µ, where the directions are drawn from a N(0, Σ(θ0))-distribution. Then, after

√

√

√

√

ϑ − 1))n√n(1 + ǫ)(α

![image 75](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile75.png>)

![image 76](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile76.png>)

![image 77](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile77.png>)

![image 78](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile78.png>)

ϑ − 1)4 ((α − 1)

ϑ − 1)4 ((α − 1)

16384e21030n3(1 + ǫ)2(α

256 exp(−2

![image 79](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile79.png>)

ϑ/(α

ln2

√

√

√

√

√

√

ℓ =

![image 80](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile80.png>)

![image 81](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile81.png>)

![image 82](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile82.png>)

![image 83](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile83.png>)

![image 84](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile84.png>)

![image 85](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile85.png>)

![image 86](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile86.png>)

![image 87](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile87.png>)

ϑ − 1)4 exp(4

ϑ − 1)4 exp(2

ϑ − 1))q2

ϑ − 1))

ϑ/(α

ϑ/(α

√

√

√

![image 88](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile88.png>)

![image 89](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile89.png>)

![image 90](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile90.png>)

ϑ − 1)2 ((α − 1)

2 exp(−2

ϑ − 1))(α

ϑ/(α

× ln3

√

,

![image 91](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile91.png>)

![image 92](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile92.png>)

ϑ − 1)2q2

(9)

hit-and-run steps, we have ν(ℓ) − µ ≤ q. Proof. Note that by (2),

√

√

√

√

![image 93](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile93.png>)

![image 94](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile94.png>)

![image 95](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile95.png>)

α

ϑ α

ϑ α

ϑ α

α

![image 96](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile96.png>)

√

√

√

0 ≤

ϑ − 1 − 1 θ0 θ

ϑ − 1 − 1

θ1 − θ0 θ

< 1,

=

ϑ =

![image 97](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile97.png>)

![image 98](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile98.png>)

![image 99](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile99.png>)

0

![image 100](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile100.png>)

![image 101](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile101.png>)

![image 102](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile102.png>)

ϑ − 1

and similarly,

√

√

![image 103](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile103.png>)

1 α

1 α

ϑ α

1 α ≤

![image 104](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile104.png>)

√

√

√

1 ≤

θ1 − θ0 θ

=

< 1. For these upper bounds, Theorem 9 shows the result.

θ1 θ

ϑ =

![image 105](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile105.png>)

![image 106](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile106.png>)

![image 107](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile107.png>)

![image 108](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile108.png>)

1

![image 109](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile109.png>)

![image 110](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile110.png>)

![image 111](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile111.png>)

ϑ − 1

ϑ

ϑ

![image 112](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile112.png>)

![image 113](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile113.png>)

![image 114](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile114.png>)

![image 115](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile115.png>)

In other words, the temperature scheme by Abernethy and Hazan allows mixing with a path length that has the same asymptotic complexity as the path length by Kalai and Vempala. This result shows that the Xk and Yjk samples in Algorithm 2 approximately follow the correct distribution, if the path length ℓ is chosen as in (9).

The main condition that needs to be satisﬁed before Corollary 10 guarantees mixing is (8). As one would expect, approximating the covariance matrix of some distribution is possible if one can sample from this distribution. However, with hit-and-run, we cannot sample exactly from the correct distribution, and the samples we do generate are not independent. Theorem 5.3 in [2] covers these pitfalls, but it requires a guarantee that the random walks have mixed well enough with the target distribution. Corollary 10 provides such a guarantee. Letting λmin(A) denote the smallest eigenvalue (with respect to the Euclidean inner product) of the matrix A, the following can thus be proven in the same manner as Theorem 5.3 in [2].

- Theorem 11. Let K ⊆ Rn be a convex body, and let  ·,·  be the Euclidean inner product. Suppose K is contained in a Euclidean ball with radius R > 0. Let p ∈ (0,1), ε ∈ (0,1], and ǫ ≥ 0. Let θ0,θ1 ∈ Rn such that θ1 = θ0/(1 − α√1ϑ), where ϑ is the complexity parameter of the entropic barrier over K, and α > 1 + 1/

![image 116](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile116.png>)

![image 117](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile117.png>)

√

![image 118](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile118.png>)

ϑ. Suppose we have an invertible matrix Σ(θ0) such that 1 1 + ǫ

![image 119](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile119.png>)

v⊤ Σ(θ0)v ≤ v⊤Σ(θ0)v ≤ (1 + ǫ)v⊤ Σ(θ0)v ∀v ∈ Rn. Pick

N ≥

490n2 pε2

![image 120](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile120.png>)

, q ≤

pε2 49980n2R4

![image 121](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile121.png>)

λmin(Σ(θ1))2.

Let X0 be a random starting point drawn from a Boltzmann distribution with parameter θ0. Let Y (1),...,Y (N) be the end points of N hit-and-run random walks applied to the Boltzmann distribution with parameter θ1 having starting point X0, where the directions are drawn from a N(0, Σ(θ0))-distribution, and each walk has length ℓ given by (9). (Note that ℓ depends on ǫ, n, and q.) Then, the empirical covariance matrix Σ(θ1) ≈ Σ(θ1) as deﬁned in line 10 of Algorithm 2 satisﬁes

P

1 1 + ε

![image 122](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile122.png>)

v⊤ Σ(θ1)v ≤ v⊤Σ(θ1)v ≤ (1 + ε)v⊤ Σ(θ1)v ∀v ∈ Rn ≥ 1 − p.

Note that a non-trivial lower bound on λmin(Σ(θ1)) was given in Theorem 3.3 in [2]. We see that a good approximation of Σ(θ0) can be used to create a good approximation of Σ(θ1). In other words, throughout the run of Algorithm 2, the Xk and Yjk samples are always from the desired distribution with high probability.

4 Rate of convergence proof for Algorithm 2

We continue by proving that Algorithm 2 converges to the optimum in polynomial time. The following result was established by Kalai and Vempala [10] for linear functions, and extended from linear to convex functions h : Rn → R by De Klerk and Laurent [9].

- Theorem 12 (Corollary 1 in [9]). Let K ⊆ Rn be a convex body. For any convex function h : Rn → R, temperature T > 0, and X ∈ K chosen according to a probability distribution on K with density proportional to x  → e−h(x)/T, we have


E[h(X)] ≤ nT + min

h(x), where

x∈K

h(x)e−h(x)/T dx K e−h(x)/T dx

E[h(X)] := K

.

![image 123](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile123.png>)

We are ready to prove that Algorithm 2 converges in polynomial time.

- Theorem 13. Let K ⊆ Rn be a convex body, and let  ·,·  be the Euclidean inner product. Suppose K is contained in a Euclidean ball with radius R > 0 and contains a Euclidean ball with radius r > 0. Denote


√

![image 124](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile124.png>)

ϑ. Let ǫ¯ ∈ (0,2R], p ∈ (0,1), and ǫ = 1. Assume X0 is uniform on K and we have an approximation Σ(0) of Σ(0) satisfying

the complexity parameter of the entropic barrier over K by ϑ, and ﬁx some α > 1 + 1/

- 1

![image 125](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile125.png>)

- 2v⊤ Σ(0)v ≤ v⊤Σ(0)v ≤ 2v⊤ Σ(0)v for all v ∈ Rn. Consider Algorithm 2 with input


√

2nR pǫ¯

![image 126](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile126.png>)

ϑ − 21)ln

+ 1 ,

m = (α

![image 127](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile127.png>)

![image 128](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile128.png>)

1000n2m p

,

N =

![image 129](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile129.png>)

8√ϑ+4

4 pǫ¯ 8Rn

![image 130](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile130.png>)

p 102000mn2R4

r n + 1

1 4096

q =

,

![image 131](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile131.png>)

![image 132](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile132.png>)

![image 133](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile133.png>)

![image 134](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile134.png>)

and let ℓ be as in (9). Then, with probability at least 1−p, we have c,Xm −minx∈K c,x ≤ ǫ¯. The number of membership oracle calls is O∗(ϑ3.5n5/p) = O∗(n8.5/p).

Proof. Throughout all iterations k of Algorithm 2, we want to maintain the conditions that Xk is a sample from the Boltzmann distribution with parameter θk, and

- 1

![image 135](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile135.png>)

- 2v⊤ Σ(θk)v ≤ v⊤Σ(θk)v ≤ 2v⊤ Σ(θk)v ∀v ∈ Rn, (10)


with high probability. We assume that these conditions hold in iteration k − 1, and we will show that they then also hold for iteration k with high probability. First, Corollary 10 and Lemma 8 guarantee that Xk is sampled from the Boltzmann distribution with parameter θk with probability at least 1 − q. Moreover, noting that

ln 2pnRǫ¯ ln α

ln 2 pnRǫ¯ ln 1 − α√1ϑ

√

2nR pǫ¯

![image 136](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile136.png>)

![image 137](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile137.png>)

![image 138](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile138.png>)

ϑ − 21)ln

+ 1 ≥

m ≥ (α

+ 1 =

+ 1, (11)

√

![image 139](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile139.png>)

![image 140](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile140.png>)

![image 141](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile141.png>)

![image 142](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile142.png>)

![image 143](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile143.png>)

ϑ α

√

![image 144](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile144.png>)

![image 145](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile145.png>)

![image 146](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile146.png>)

![image 147](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile147.png>)

ϑ−1

we have

1−m

2n pǫ¯

1 α

1 Tk ≤

1 Tm

1 R

√

≤

1 −

θk =

=

, and therefore Theorem 3.3 in [2] gives

![image 148](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile148.png>)

![image 149](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile149.png>)

![image 150](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile150.png>)

![image 151](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile151.png>)

![image 152](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile152.png>)

![image 153](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile153.png>)

ϑ

1 64

λmin(Σ(θk)) ≥

![image 154](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile154.png>)

1 4R θk

![image 155](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile155.png>)

√

![image 156](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile156.png>)

4

ϑ+2 r n + 1

![image 157](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile157.png>)

2

1 64

≥

![image 158](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile158.png>)

pǫ¯ 8Rn

![image 159](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile159.png>)

4√ϑ+2 r n + 1

![image 160](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile160.png>)

![image 161](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile161.png>)

2

.

It then follows that

p10049m 49980nR4

490n2 p10049m

![image 162](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile162.png>)

λmin(Σ(θk))2 and N ≥

q ≤

,

![image 163](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile163.png>)

![image 164](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile164.png>)

![image 165](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile165.png>)

such that the conditions of Theorem 11 are satisﬁed. Hence, with probability p10049m, (10) also holds for iteration k.

![image 166](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile166.png>)

By induction, Xm is sampled from a Boltzmann distribution with parameter θm and (9) is satisﬁed for k = m, with probability at least

49 100m ≥ 1 − m

1 − m q + p

![image 167](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile167.png>)

p 100m

49p 100m

+

![image 168](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile168.png>)

![image 169](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile169.png>)

= 1 − p/2,

by the union bound. It then follows from the Markov inequality, Theorem 12, and (11), that

E[ c,Xm − minx∈K c,x ] ǫ¯ ≤

nTm ¯ǫ ≤

P c,Xm − min x∈K

c,x > ¯ǫ ≤

![image 170](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile170.png>)

![image 171](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile171.png>)

p 2

. (12)

![image 172](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile172.png>)

In conclusion, the total success probability of the algorithm is at least 1 − p. The number of oracle calls is

√

√

![image 173](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile173.png>)

n2

ϑ p

![image 174](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile174.png>)

n3ϑ2.5 = O∗(ϑ3.5n5/p) = O∗(n8.5/p),

O∗(mNℓ) = O∗

ϑ

![image 175](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile175.png>)

where the ﬁnal equality uses ϑ = n + o(n).

![image 176](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile176.png>)

![image 177](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile177.png>)

![image 178](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile178.png>)

![image 179](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile179.png>)

We note that if a lower bound on λmin(Σ(θ)) were found that was not exponential in ϑ, then the algorithm complexity would improve by a factor ϑ2.5. Even then, we would still be a factor of n1.5 away from the complexity O∗(n4.5) by Kalai and Vempala. The reason for this gap is that they use the following corollary to a theorem by Rudelson [19].

- Theorem 14 ([10, Theorem A.1]). Let µ be an isotropic logconcave probability distribution over Rn with mean 0, and let ǫ > 0,p > 1. Then, there exists a number N with

N = O

np2 ǫ2

![image 180](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile180.png>)

log2(n/ǫ2)max{p,log n} , (13)

such that for N independent samples X1,...,XN from µ we have

E

1 N

![image 181](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile181.png>)

N

i=1

XiXi⊤ − I

p

≤ ǫp.

However, the samples that are generated by hit-and-run sampling do not follow the target distribution µ, and are not independent. As we have seen in e.g. Theorem 9, they are drawn from a distribution that has total variation distance q > 0 to µ. Moreover, the samples were shown to be 6q-independent by [2, Lemma

- 4.3], i.e. for any two hit-and-run samples X and Y and measurable A,B ⊆ K, |P{X ∈ A ∧ Y ∈ B} − P{X ∈ A}P{Y ∈ B}| ≤ 6q.


While Kalai and Vempala claim that Theorem 14 can be extended to this setting without signiﬁcantly changing (13), a formal proof is not given. In particular, it is not shown how the relaxation of the independence assumption can be aligned with Rudelson’s proof.

There is another reason (13) could change in the hit-and-run setting. Theorem 14 holds for isotropic probability distributions, so to apply it to a Boltzmann distribution with parameter θ ∈ Rn over a convex body K ⊆ Rn, we should ﬁrst transform the K by Σ(θ)−1/2. Consequently, the transformed body is not necessarily contained in a Euclidean ball with radius R anymore; in the worst case, the radius of the new enclosing ball depends on the smallest eigenvalue of Σ(θ). Since we do not have a better bound on this eigenvalue than Theorem 3.3 in [2], the diameter of Σ(θ)−1/2K may be exponential in n. The suggestions by Kalai and Vempala to prove a statement similar to Theorem 14 in the hit-and-run setting require a bound on this diameter. If this bound grows exponentially in n, then q should decrease exponentially in n to compensate (see e.g. Lemma 2.7 and the proof of Theorem 5.9 from Kannan, Lo´vasz and Simonovits [12]). Such a small q would contribute a polynomial factor of n to the ﬁnal algorithm complexity.

Assuming these issues can be overcome, Kalai and Vempala show the following.

- Theorem 15 ([10, Theorem 4.2]). Let t ≥ 0. With N = O∗(t3n) samples per phase in each of m phases, every distribution encountered by the sampling algorithm is 160-isotropic with probability at least 1 − m/2t.


Kalai and Vempala are then able to pick t = O(log(m/p)), and can therefore claim N = O∗(n). We ﬁnd in Theorem 11 that N = O(n2/(p/m)) samples are required, which is O∗(n

√

![image 182](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile182.png>)

ϑ) = O∗(n1.5) worse than Kalai and Vempala’s result.

One might still wonder how to generate a good estimate Σ(0) of the uniform covariance matrix Σ(0) to start Algorithm 2. For this purpose, the rounding the body procedure from Lov´asz and Vempala [15] is

suitable. It is shown by Theorem 5.3 in [15] that, with probability at least 1 − 1/n, the uniform distribution over Σ(0)−1/2K is 2-isotropic. As shown in the proof of Theorem 9, this is equivalent to

- 1

![image 183](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile183.png>)

- 2v⊤ Σ(0)v ≤ v⊤Σ(0)v ≤ 2v⊤ Σ(0)v ∀v ∈ Rn,


which satisﬁes the starting condition for Algorithm 2. The number of calls to the membership oracle for this procedure is O∗(n4).

# 5 Numerical Examples on the Doubly Nonnegative Cone

Let Sm×m denote the space of real symmetric m × m matrices. We will test the method described above on the problem of determining whether some matrix C ∈ Sm×m is copositive, i.e. x⊤Cx ≥ 0 for all x ∈ Rm+ (see Bomze [5] for a survey on copositive programming and its applications). The standard SDP relaxation of this problem is the following:

 

 

m

m

Xij ≤ 1,X ≥ 0,X 0

, (14)

inf

C,X :





j=1

i=1

where  ·,·  is the trace inner product. If the value of (14) is nonnegative, the matrix C is copositive. However, since we place a nonnegativity constraint on every element of the matrix X, the Newton system in every interior point iteration is of size O(m2 ×m2), which quickly leads to impractical computation times (see e.g. Burer [7]).

Before we can apply Algorithm 2, we need to translate (14) to a problem over Rm(m+1)/2. The approach is standard: for any A = [Aij]ij ∈ Sm×m, deﬁne

√

√

√

√

2A2m,...,Amm)⊤,

![image 184](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile184.png>)

![image 185](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile185.png>)

![image 186](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile186.png>)

![image 187](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile187.png>)

svec(A) := (A11,

2A12,...,

2A1m,A22,

2A23,...,

such that svec(A) ∈ Rm(m+1)/2. If Rm(m+1)/2 is endowed with the Euclidean inner product, the adjoint of svec is deﬁned for every a ∈ Rm(m+1)/2 as

a1 a2/√2 ... am/√2 a2/√2 am+1 ... a2m−1/√2





![image 188](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile188.png>)

![image 189](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile189.png>)

![image 190](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile190.png>)

![image 191](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile191.png>)

smat(a) =

,

 

 

... . am/√2 a2m−1/√2 ... am(m+1)/2

. .

![image 192](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile192.png>)

![image 193](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile193.png>)

such that smat(a) ∈ Sm×m. Moreover, smat(svec(A)) = A and svec(smat(a)) = a for all A and a. Now let c = svec(C). Problem (14) is equivalent to the following problem over Rm(m+1)/2:

 

 

m

m

(smat(x))ij ≤ 1,x ≥ 0,smat(x) 0

. (15)

inf

c,x :





j=1

i=1

Note that membership of the feasible set of (15) can be determined in O(m3) operations. Let n = 12m(m+1) be the number of variables in problem (15).

![image 194](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile194.png>)

- 5.1 Covariance Approximation


First, we investigate how the quality of the covariance approximation depends on the walk length for problem (15). We take 20,000 hit-and-run samples from the uniform distribution over the feasible set of (15) with walk length 50,000 (directions are drawn from N(0,I) and the starting point is svec(mI +J)/(2e⊤ svec(mI +J)), where J is the all-ones matrix). These samples are used to create the estimate Σ0. Then, the experiment is

repeated for walk lengths ℓ ≤ 50,000 and sample sizes N ≤ 20,000. We refer to these new estimates as Σℓ,N. We would like

−ǫy⊤ Σℓ,Ny ≤ y⊤( Σ0 − Σℓ,N)y ≤ ǫy⊤ Σℓ,Ny ∀y ∈ Rn, for some small ǫ > 0. This is equivalent to

−ǫx⊤x ≤ x⊤( Σℓ,N−1/2 Σ0 Σℓ,N−1/2 − I)x ≤ ǫx⊤x ∀x ∈ Rn,

i.e. we would like the spectral radius of Σℓ,N−1/2 Σ0 Σℓ,N−1/2 − I to be at most ǫ. Because the spectra of Σℓ,N−1/2 Σ0 Σℓ,N−1/2 − I and Σ−ℓ,N1 Σ0 − I are the same, we focus on the spectral radius ρ( Σ−ℓ,N1 Σ0 − I).

The result is shown in Figure 1, where m refers to the size of the matrices in (14). Hence, the covariance matrices in question are of size 21m(m + 1) × 21m(m + 1).

![image 195](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile195.png>)

![image 196](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile196.png>)

1−( Σ Σ−)ρI0ℓ,N

1−( Σ Σ−)ρI0ℓ,N

m = 5

100

10−1

102 103 104

Sample size N

m = 15

- 100
- 101
- 102


103 104

Sample size N

1−( Σ Σ−)ρI0ℓ,N

1( Σ Σ−)−ρI0ℓ,N

m = 10

|ℓ = 100 ℓ = 200 ℓ = 500 ℓ = 1000 ℓ = 2000 ℓ = 5000 ℓ = 10,000 ℓ = 20,000 ℓ = 50,000<br><br>|
|---|


- 100
- 101
- 102


10−1

102 103 104

Sample size N

m = 20

|ℓ = 100 ℓ = 200 ℓ = 500 ℓ = 1000 ℓ = 2000 ℓ = 5000 ℓ = 10,000 ℓ = 20,000 ℓ = 50,000<br><br>|
|---|


- 100
- 101
- 102


103 104

Sample size N

Figure 1: Eﬀect of sample size N and walk length ℓ on quality of uniform covariance approximation

One major conclusion from Figure 1 is that the trajectory towards zero is relatively slow. To show that simply adding more samples with higher walk lengths will in practice not be feasible, we present the running times required to estimate a covariance matrix at the desired accuracy in Figure 2. Speciﬁcally, this ﬁgure shows the running times of the “eﬃcient” combinations of N and ℓ: these are the combinations of N and ℓ plotted in Figure 1 for which there are no N′ and ℓ′ such that N′ℓ′ ≤ Nℓ and ρ( Σ−ℓ′,N1 ′ Σ0−I) < ρ( Σ−ℓ,N1 Σ0−I). (The computer used has an Intel i7-6700 CPU with 16 GB RAM, and the code used six threads.) Figure

- 2 shows that, even at low dimensions, approximating the covariance matrix to high accuracy will take an unpractical amount of time.


Runningtime(s)

- 100
- 101
- 102
- 103
- 104


10−1

10−1 100 101 102

ρ( Σ−ℓ,N1 Σ0 − I)

|m = 5 m = 10 m = 15 m = 20<br><br>|
|---|


Figure 2: Running times required to ﬁnd an approximation Σℓ,N of the desired quality

To show that the slow trajectory towards zero in Figure 1 is a result of convariance estimation’s fundamental diﬃculty, we consider a simpler problem. We want to approximate the covariance matrix of the uniform distribution over the hypercube [0,1]n in Rn. Note that the true covariance matrix of this distribution is known to be Σ := 121 I.

![image 197](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile197.png>)

Again, we will use hit-and-run with varying walk lengths and sample sizes to generate samples from

the uniform distribution over [0,1]n, and compare the resulting covariance matrices Σℓ,N with Σ = 121 I (comparing against a covariance estimate based on hit-and-run samples as in Figure 1 yields roughly the

![image 198](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile198.png>)

same image). The result is shown in Figure 3.

Figure 3 shows a pattern similar to that of Figure 1: as the problem size increases, the walk length should increase with the sample size to ensure the estimate is as good as the sample size can guarantee. While this progression towards zero may appear as slow, we do not have to know every entry of the covariance with high accuracy. Recall that we only use this covariance estimate in Algorithm 2 to generate hit-and-run directions. As such, it may suﬃce to have an estimate that roughly shows which directions are “long”, and which ones are “short”.

- 5.2 Mean Approximation


Next, we consider the problem of approximating the mean. Although it is not required for Algorithm 2 to approximate the mean of a Boltzmann distribution, such a mean does lie on the central path of the interior point method proposed by Abernethy and Hazan [1].

We again take 20,000 hit-and-run samples from the uniform distribution over the feasible set of (15) with walk length 50,000 (directions are drawn from N(0,I) and the starting point is svec(mI +J)/(2e⊤ svec(mI + J)), where J is the all-ones matrix). These samples are used to create the mean estimate x0. Then, the experiment is repeated for walk lengths ℓ ≤ 50,000 and sample sizes N ≤ 20,000. We refer to these new estimates as xℓ,N. Using the approximation Σ0 of the uniform covariance matrix from the previous section, we compute x0 − xℓ,N Σ−1

and plot the results in Figure 4.

0

The results are comparable to those in Figures 1 and 2. It will take an impractical amount of time before the mean estimate approximates the true mean well enough for practical purposes.

n = 15

1−Σ−)( ΣIρℓ,N

100

10−1

102 103 104

Sample size N

n = 120

1−( ΣΣ−)ρIℓ,N

- 100
- 101


103 104

Sample size N

1−( ΣΣ−)ρIℓ,N

1−( ΣΣ−)ρIℓ,N

n = 55

|Truly uniform ℓ = 100 ℓ = 200 ℓ = 500 ℓ = 1000<br><br>|
|---|


- 100
- 101


10−1

102 103 104

Sample size N

n = 210

|Truly uniform ℓ = 100 ℓ = 200 ℓ = 500 ℓ = 1000<br><br>|
|---|


- 100
- 101


103 104

Sample size N

Figure 3: Eﬀect of sample size N and walk length ℓ on quality of uniform covariance matrix approximation over the hypercube in Rn

- 5.3 Kalai-Vempala Algorithm

The results from the previous two sections show that we should not hope to approximate the covariance matrix and sample mean with high accuracy in high dimensions. However, it is still insightful to verify if this is really required for Algorithm 2 to work in practice.

We therefore generated a random vector c ∈ Rm(m+1)/2 as follows: if C ∈ Rm×m is a matrix with all elements belonging to a standard normal distribution, then C+C⊤+(√2−2)Diag(C) is a symmetric matrix whose elements all have variance 2. We then let

![image 199](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile199.png>)

c =

svec(C + C⊤ + (√2 − 2)Diag(C)) svec(C + C⊤ + (√2 − 2)Diag(C))

![image 200](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile200.png>)

![image 201](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile201.png>)

![image 202](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile202.png>)

,

serve as the objective of our optimization problem (15). We can ﬁnd the optimal solution x∗ with MOSEK 8.0 [16], and then run Algorithm 2 with ǫ¯ = 10−3 and p = 10−1. The ﬁnal gap c,xﬁnal − x∗ is shown in

- Figure 5. One can see that for practical sample sizes and walk lengths, the method does not converge to the optimal solution.


- 5.4 Kalai-Vempala Algorithm with Acceleration Heuristic


Keeping our ﬁndings above in mind, we propose the heuristic adaption of of Algorithm 2 presented in Algorithm 3. The main modiﬁcations to Algorithm 2 are:

m = 5

100

− x x0ℓ,N1− Σ

0

10−1

102 103 104

Sample size N

m = 10

|ℓ = 100 ℓ = 200 ℓ = 500 ℓ = 1000 ℓ = 2000 ℓ = 5000 ℓ = 10,000 ℓ = 20,000 ℓ = 50,000<br><br>|
|---|


- 100
- 101


− x x0ℓ,N1− Σ

0

10−1

102 103 104

Sample size N

− x x0ℓ,N1− Σ

- 0

m = 15

102 103 104

10−1

- 100
- 101
- 102


Sample size N

− x x0ℓ,N1− Σ

0

m = 20

|ℓ = 100 ℓ = 200 ℓ = 500 ℓ = 1000 ℓ = 2000 ℓ = 5000 ℓ = 10,000 ℓ = 20,000 ℓ = 50,000<br><br>|
|---|


Figure 4: Eﬀect of sample size N and walk length ℓ on quality of uniform mean approximation

- 1. Use the (centered) samples generated in the previous iteration as directions for hit-and-run in the current iteration. This would eliminate the need to estimate the covariance matrix of a distribution, only to then draw samples from that same distribution. Instead, we can also draw directions directly from the centered samples (cf. line 10 in Algorithm 3). Thus each sample is used to generate a hitand-run direction with uniform probability.
- 2. Start a random walk from the end point of the previous random walk, rather than from a common starting point. The idea here is that the random sample as a whole will exhibit less dependence, thus improving the approximation quality of the empirical distribution.
- 3. As a starting point for the walk in some iteration k, use the sample mean from iteration k − 1. While this does signiﬁcantly change the distribution of the starting point, it concentrates more probability


- 100
- 101


10−1

102 103 104

Sample size N

mass around the mean of the Boltzmann distribution with parameter θk−1, such that the starting point of the random walk is likely already close to the mean of the Boltzmann distribution with parameter θk. In a similar vein, we return the mean of the samples in the ﬁnal iteration, not just one sample. This will not change the expected objective value of the ﬁnal result, and will therefore also not aﬀect the probabilistic guarantee that we derived in (12) by Markov’s inequality. However, using the mean does reduce the variance in the ﬁnal solution.

The modiﬁed algorithm is given in full in Algorithm 3.

With these modiﬁcations implemented, we can no longer study the quality of the covariance matrix. Therefore, we will simply consider if the resulting optimization algorithm leads to a small error in the

n = 5

− c, xxﬁnal∗

10−1

10−2

102 103

− c, xxﬁnal∗

Sample size N

n = 15

10−0.9

10−1

10−1.1

10−1.2

10−1.3

102.5 103 103.5

Sample size N

− c, xxﬁnal∗

10−1

10−2

n = 10

|ℓ = 5 ℓ = 10 ℓ = 20 ℓ = 40 ℓ = 80 ℓ = 160 ℓ = 320 ℓ = 640 ℓ = 1280<br><br>|
|---|


102 103

Sample size N

n = 20

− c, xxﬁnal∗

|ℓ = 5 ℓ = 10 ℓ = 20 ℓ = 40 ℓ = 80 ℓ = 160 ℓ = 320 ℓ = 640 ℓ = 1280<br><br>|
|---|


10−1.1

10−1.2

10−1.3

102.6 102.8 103 103.2 103.4

Sample size N

Figure 5: Eﬀect of sample size N and walk length ℓ on the ﬁnal gap of Algorithm 2

objective value. We solve the problem from Section 5.3 with Algorithm 3. The results are given in Figure 6. For low dimensions in particular, the proposed changes seem to have a positive eﬀect. It can be seen from

- Figure 6 that – roughly speaking – the ﬁnal gap c,xﬁnal − x∗ takes values between two extremes. At one end, the method does not converge and the ﬁnal gap is still of the order 10−1. At the other end, the method does converge to the optimum, such that the gap is of the order 10−4 = ǫp¯ . Note that ǫp¯ is exactly the size we would like the expected gap to have to guarantee that the gap is smaller than ¯ǫ with probability 1 − p by Markov’s inequality. Whether we are at one end or the other depends on N and ℓ being large enough compared to m. As a heuristic, we propose that


N = n√n , ℓ = n√n , (16)

![image 203](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile203.png>)

![image 204](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile204.png>)

where n = m(m + 1)/2 is the number of variables, are generally suﬃcient to ensure that the ﬁnal gap is of the order ǫp¯ .

# 6 Numerical Examples on the Copositive Cone

We now turn our attention away from the doubly nonnegative cone, and towards the copositive cone. Although deciding if a matrix is copositive is a co-NP-complete problem [17], there are a number of procedures to test for copositivity. Clearly, A = [Aij]ij ∈ Sm×m is copositive if and only if

min a⊤Aa : e⊤a = 1,a ≥ 0 , (17)

![image 205](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile205.png>)

Algorithm 3 Heuristic adaptation of Algorithm 2 Input: unit vector c ∈ Rn; membership oracle OK : Rn → {0,1} of a convex body K; radius R of Euclidean

![image 206](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile206.png>)

ball containing K; complexity parameter ϑ ≤ n + o(n) of the entropic barrier over K; update parameter α > 1 + 1/

√

![image 207](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile207.png>)

ϑ; error tolerance ¯ǫ > 0; failure probability p ∈ (0,1); number of hit-and-run steps ℓ ∈ N; number of samples N ∈ N; y1,...,yN ∈ K drawn randomly from the uniform distribution over K.

- 1: Yj0 ← yj for all j ∈ {1,...,N}
- 2: X0 ← N1 Nj=1 Yj0

![image 208](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile208.png>)

- 3: θ0 ← 0
- 4: T0 ← ∞,T1 ← R
- 5: k ← 1
- 6: while nTk−1 > ǫp¯ do
- 7: θk ← −c/Tk
- 8: Y0k ← Xk−1
- 9: for j ∈ {1,...,N} do
- 10: Generate Yjk by applying hit-and-run sampling to the Boltzmann distribution with parameter θk, starting the walk from Yj−1,k, taking ℓ steps, drawing directions uniformly from {Y1,k−1 − Xk−1,...,YN,k−1 − Xk−1}
- 11: end for
- 12: Xk ← N1 Nj=1 Yjk

![image 209](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile209.png>)

- 13: Tk+1 ← min{R(1 − α√1ϑ)k,R(1 − √1n)k}

![image 210](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile210.png>)

![image 211](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile211.png>)

![image 212](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile212.png>)

![image 213](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile213.png>)

- 14: k ← k + 1
- 15: end while
- 16: return Xk−1


![image 214](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile214.png>)

is nonnegative, where e is the all-ones vector. Xia et al. [22] show that solving (17) is equivalent to solving min − ν

s.t.Aa + νe − η = 0 e⊤a = 1 0 ≤ a ≤ b 0 ≤ η ≤ M(e − b) b ∈ {0,1}n,

(18)

where M = 2mmaxi,j∈{1,...,m} |Aij|. (To be precise, every optimal solution (a,ν,η) to (18) gives an optimal solution a to (17), and these two problems have the same optimal values.) Note that we are generally not interested in solving (18) to optimality: it suﬃces to ﬁnd a feasible solution of (18) with a negative objective value, or conﬁrm that no such solution exists. For the majority of the matrices encountered by Algorithm 3 applied to our test sets described below, this could be checked quickly.

- 6.1 Separating from the Completely Positive Cone


Recall that a matrix A ∈ Sm×m is completely positive if A = BB⊤ for some B ≥ 0. It is easily seen that optimization problems over the completely positive cone can be relaxed as optimization problems over the doubly nonnegative cone. To strengthen this relaxation, one could add a cutting plane separating the

− c, xxﬁnal∗

m = 5

10−1

10−2

10−3

10−4

101 102 103

Sample size N

m = 15

− c, xxﬁnal∗

10−1

10−2

10−3

10−4

101 102 103

Sample size N

m = 10

− c, xxﬁnal∗

|ℓ = 5 ℓ = 10 ℓ = 20 ℓ = 40 ℓ = 80 ℓ = 160 ℓ = 320 ℓ = 640 ℓ = 1280<br><br>|
|---|


10−1

10−2

10−3

10−4

101 102 103

Sample size N

m = 20

− c, xxﬁnal∗

|ℓ = 5 ℓ = 10 ℓ = 20 ℓ = 40 ℓ = 80 ℓ = 160 ℓ = 320 ℓ = 640 ℓ = 1280<br><br>|
|---|


10−1

10−2

10−3

10−4

101 102 103

Sample size N

Figure 6: Eﬀect of sample size N and walk length ℓ on the ﬁnal gap of Algorithm 3

optimal solution Y of the doubly nonnegative relaxation from the completely positive cone. This is listed as an open (computational) problem by Berman et al. [4, Section 5], who note that the problem of generating such a cut has only been answered for speciﬁc structures of Y , including 5 × 5 matrices [8]. In general, such a cut could be generated for a doubly nonnegative matrix Y by the copositive program

inf { Y,X : X,X ≤ 1,X copositive}. (19) Below, we solve this problem for 6 × 6 matrices, by way of example.

To generate test instances, we are interested in matrices on the boundary of the 6×6 doubly nonnegative cone. The extreme rays of this cone are described by Ycart [23, Proposition 6.1]. We generate random instances from the class of matrices described under case 3, graph 4 in Proposition 6.1 in [23]. These matrices are (up to permutation of the indices) doubly nonnegative matrices Y = [Yij]ij with rank 3 satisfying Yi,i+1 = 0 for i = 1,...,5. To generate such a matrix, we draw the elements of two vectors v1,v2 ∈ R6 and the ﬁrst element (v3)1 ∈ R of a vector v3 ∈ R6 from a Poisson distribution with rate 1, and multiply each of these elements with −1 with probability 21. The remaining elements of v3 are then chosen such that Y = 3k=1 vkvk⊤ satisﬁes Yi,i+1 = 0 for i = 1,...,5. This procedure is repeated if the matrix Y is not doubly nonnegative, or if BARON 15 [21] could ﬁnd a nonnegative matrix B ∈ R6×9 such that Y = BB⊤ in less than 30 seconds (for the cases where such a decomposition could be found, BARON terminated in less than a second). Thus, we are left with doubly nonnegative matrices for which it cannot quickly be shown that they are completely positive.

![image 215](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile215.png>)

For ten of such randomly generated matrices (see Appendix B), the optimal value of Algorithm 3 applied to (19) is given in Table 1. This table shows the normalized objective value Y/ Y ,X∗ , where Y is a

![image 216](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile216.png>)

Final objective value (normalized) Oracle calls Name Algorithm 3 Ellipsoid method Algorithm 3 Ellipsoid method

![image 217](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile217.png>)

![image 218](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile218.png>)

![image 219](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile219.png>)

- extremal rand 1 -7.626893e-03 -7.667645e-03 8.766473e+06 3.152000e+03

![image 220](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile220.png>)

![image 221](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile221.png>)

- extremal rand 2 -1.983630e-02 -1.987634e-02 9.073317e+06 3.412000e+03

![image 222](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile222.png>)

![image 223](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile223.png>)

- extremal rand 3 -3.591875e-02 -3.596345e-02 9.334264e+06 3.835000e+03

![image 224](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile224.png>)

![image 225](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile225.png>)

- extremal rand 4 -9.937402e-03 -9.980087e-03 8.830209e+06 3.147000e+03

![image 226](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile226.png>)

![image 227](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile227.png>)

- extremal rand 5 -5.897273e-03 -5.940056e-03 8.628287e+06 2.957000e+03

![image 228](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile228.png>)

![image 229](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile229.png>)

- extremal rand 6 -4.303956e-02 -4.307761e-02 9.438518e+06 4.024000e+03

![image 230](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile230.png>)

![image 231](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile231.png>)

- extremal rand 7 -2.411010e-02 -2.415651e-02 9.179767e+06 3.708000e+03

![image 232](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile232.png>)

![image 233](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile233.png>)

- extremal rand 8 -6.822593e-02 -6.826558e-02 9.641288e+06 4.277000e+03

![image 234](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile234.png>)

![image 235](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile235.png>)

- extremal rand 9 -4.232229e-02 -4.236829e-02 9.416909e+06 3.981000e+03

![image 236](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile236.png>)

![image 237](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile237.png>)

- extremal rand 10 -2.962993e-02 -2.967333e-02 9.236507e+06 3.743000e+03


![image 238](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile238.png>)

![image 239](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile239.png>)

![image 240](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile240.png>)

Table 1: Objective values returned by Algorithm 3 and by the Ellipsoid method, applied to (19). Algorithm

- 3 was run with ǫ¯ = 10−3 and p = 0.1, and N and ℓ as in (16). The Ellipsoid method was run with error tolerance 10−4.


doubly nonnegative matrix as described above, and X∗ is the ﬁnal solution returned by Algorithm 3. Note that in all cases, Algorithm 3 succeeded in ﬁnding a copositive matrix X∗ such that Y,X∗ < 0, which means a cut separating Y from the completely positive matrices was found.

Note that solving the MILP (18) for a matrix A that is not copositive yields a hyperplane separating A from the copositive cone. Thus, we can also solve problem (19) with the ellipsoid method of Yudin and Nemirovski [24], for example. For the sake of comparison, the results of the Ellipsoid method are also included in Table 1. Note, in particular, that the number of oracle calls in Table 1 is several orders of magnitude smaller for the Ellipsoid method.

# 7 Conclusion

We have shown that Kalai and Vempala’s algorithm [10] returns a solution which is near-optimal for (1) with high probability in polynomial time, when the temperature update (5) is used. The main drawback to using the algorithm in practice, is the large number of samples (i.e. membership oracle calls) required. As a result, in our tests the Ellipsoid method outperformed Algorithm 3 by a large margin. Thus, based on our experiments, one would favor polynomial-time cutting plane methods like the Ellipsoid method, or more sophisticated alternatives as described e.g. in [11]. In order to obtain a practically viable variant of the Kalai-Vempala algorithm, one would have to improve the sampling process greatly, or utilize massive parallelism to speed up the hit-and-run sampling.

Acknowledgements

The authors would like to thank S´ebastien Bubeck, Osman G¨uler, and Levent Tunc¸el for valuable discussions about the complexity parameter of the entropic barrier.

# A The complexity parameter of the entropic barrier for the Euclidean ball

Let Bn := {x ∈ Rn : x 2 ≤ 1} be the unit ball in Rn with respect to the inner product  ·,· . We are interested in the complexity parameter ϑ of the entropic barrier on Bn. We will follow the notation from [2].

Approximation θ,H(θ)θ

- 0
- 1
- 2
- 3
- 4
- 5
- 6


0 200 400 600 θ

|n = 1<br><br>n = 2<br><br>n = 3<br><br>n = 4<br><br>n = 5<br><br>n = 6<br><br>n = 7<br><br>n = 8<br><br>n = 9<br><br>n = 10<br>|
|---|


Figure 7: Numerical approximation of θ,H(θ)θ

Bubeck and Eldan [6, Lemma 1(iii)] show that the gradient g∗ of the entropic barrier is a bijection of Bn to Rn. Therefore,

( gx∗(x) ∗x)2 = sup

ϑ = sup

x∈Bn

x∈Bn

g∗(x),H∗(x)−1g∗(x) = sup θ∈Rn

θ,H(θ)θ ,

where the ﬁnal equality uses H∗(x)−1 = H(θ(x)) (see [6, Lemma 1(iv)]). Recall that H(θ) is the covariance operator of the Boltzmann distribution with parameter θ. Then,

θ,H(θ)θ = Eθ[ X − Eθ[X],θ 2] = Eθ[ θ,X 2] − θ,Eθ[X] 2.

From now on, we will let  ·,·  be the Euclidean inner product. For every θ ∈ Rn, there exists a rotation matrix Q with |detQ| = 1 such that θ,Qy = θ y1 for all y ∈ Rn. Using the fact that the volume of an (n − 1)-dimensional ball with radius r is rn−1 times some factor depending only on n, we see that

1 −1 θ y1( 1 − y12)n−1e θ y

![image 241](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile241.png>)

θ y1e θ y

θ,x e θ,x dx Bn e θ,x dx

dy Bn e θ y1 dy

dy1

1

1

= B

θ,Eθ[X] = B

n

n

=

.

![image 242](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile242.png>)

![image 243](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile243.png>)

![image 244](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile244.png>)

1 −1( 1 − y12)n−1e θ y1 dy1

![image 245](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile245.png>)

The ﬁnal expression cannot be computed in closed form, but it can be approximated numerically for ﬁxed θ . Similarly,

1 −1 θ 2y12( 1 − y12)n−1e θ y

![image 246](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile246.png>)

θ 2y12e θ y

θ,x 2e θ,x dx Bn e θ,x dx

dy Bn e θ y1 dy

dy1

1

1

= B

Eθ[ θ,X 2] = B

n

n

=

.

![image 247](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile247.png>)

![image 248](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile248.png>)

![image 249](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile249.png>)

1 −1( 1 − y12)n−1e θ y1 dy1

![image 250](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile250.png>)

Numerical approximation of Eθ[ θ,X 2] − θ,Eθ[X] 2 for diﬀerent values of n and θ yields Figure 7. This ﬁgure suggests that ϑ = 21(n + 1).

![image 251](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile251.png>)

# B Extremal Doubly Nonnegative Matrix Examples

Below are the ten randomly generated extreme points of the 6 × 6 doubly nonnegative cone that are used in Section 6.1. These matrices can be strictly separated from the completely positive cone.

extremal rand 1 =

![image 252](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile252.png>)

![image 253](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile253.png>)

extremal rand 3 =

![image 254](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile254.png>)

![image 255](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile255.png>)

extremal rand 5 =

![image 256](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile256.png>)

![image 257](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile257.png>)

extremal rand 7 =

![image 258](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile258.png>)

![image 259](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile259.png>)

extremal rand 9 =

![image 260](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile260.png>)

![image 261](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile261.png>)





2 0 6 0 1 2 0 6 0 8 1 2 6 0 18 0 3 6

- 0 8 0 11 0 3
- 1 1 3 0 6 0
- 2 2 6 3 0 3


 

 





12 0 4 2 0 2 0 2 0 2 1 2 4 0 2 0 1 0 2 2 0 3 0 3 0 1 1 0 2 0 2 2 0 3 0 3

 

 





5 0 5 0 5 3 0 6 0 10 1 18

- 5 0 5 0 5 3 0 10 0 20 0 42
- 5 1 5 0 6 0 3 18 3 42 0 99


 

 





14 0 4 8 2 16 0 6 0 4 2 8 4 0 8 0 8 0 8 4 0 8 0 16 2 2 8 0 9 0 16 8 0 16 0 32

 

 





2 0 2 0 4 2

- 0 2 0 2 2 0 2 0 2 0 4 2
- 0 2 0 3 0 2
- 4 2 4 0 14 0 2 0 2 2 0 6


 

 

extremal rand 2 =

![image 262](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile262.png>)

![image 263](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile263.png>)

extremal rand 4 =

![image 264](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile264.png>)

![image 265](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile265.png>)

extremal rand 6 =

![image 266](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile266.png>)

![image 267](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile267.png>)

extremal rand 8 =

![image 268](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile268.png>)

![image 269](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile269.png>)

extremal rand 10 =

![image 270](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile270.png>)

![image 271](<2019-badenbroek-simulated-annealing-hit-and-run-convex_images/imageFile271.png>)





- 2 0 2 3 1 3

- 0 2 0 3 1 1

2 0 3 0 2 1 3 3 0 18 0 12

- 1 1 2 0 2 0 3 1 1 12 0 9




 

 





- 2 0 2 2 2 4 0 8 0 4 4 8
- 2 0 3 0 4 0
- 2 4 0 8 0 16 2 4 4 0 8 0 4 8 0 16 0 32


 

 





- 3 0 3 4 0 4 0 6 0 2 6 2

- 3 0 11 0 4 0
- 4 2 0 8 0 8 0 6 4 0 8 0


- 4 2 0 8 0 8


 

 





6 0 4 2 0 2 0 5 0 2 2 2 4 0 6 0 2 0 2 2 0 2 0 2 0 2 2 0 2 0 2 2 0 2 0 2

 

 





- 2 0 2 2 0 2

- 0 2 0 2 2 2

2 0 3 0 1 0 2 2 0 8 0 8

- 0 2 1 0 3 0
- 2 2 0 8 0 8




 

 

# References

- [1] J. Abernethy and E. Hazan. Faster convex optimization: Simulated annealing with an eﬃcient universal barrier. arXiv preprint arXiv:1507.02528, 2015.
- [2] R. Badenbroek and E. de Klerk. Complexity analysis of a sampling-based interior point method for convex optimization. arXiv preprint arXiv:1811.07677, 2018.
- [3] C. J. B´elisle, H. E. Romeijn, and R. L. Smith. Hit-and-run algorithms for generating multivariate distributions. Mathematics of Operations Research, 18(2):255–266, 1993.
- [4] A. Berman, M. Dur, and N. Shaked-Monderer. Open problems in the theory of completely positive and copositive matrices. Electronic Journal of Linear Algebra, 29(1):46–58, 2015.
- [5] I. M. Bomze. Copositive optimization–recent developments and applications. European Journal of Operational Research, 216(3):509–520, 2012.


- [6] S. Bubeck and R. Eldan. The entropic barrier: Exponential families, log-concave geometry, and selfconcordance. Mathematics of Operations Research, 44(1):264–276, 2018.
- [7] S. Burer. Optimizing a polyhedral-semideﬁnite relaxation of completely positive programs. Mathematical Programming Computation, 2(1):1–19, 2010.
- [8] S. Burer and H. Dong. Separation and relaxation for cones of quadratic forms. Mathematical Programming, 137(1-2):343–370, 2013.
- [9] E. de Klerk and M. Laurent. Comparison of Laserre’s measure-based bounds for polynomial optimization to the bounds obtained by simulated annealing. Mathematics of Operations Research, 43(4):1051–1404, 2018.
- [10] A. T. Kalai and S. Vempala. Simulated annealing for convex optimization. Mathematics of Operations Research, 31(2):253–266, 2006.
- [11] Y.T. Lee, A. Sidford, and S.C. Wong. A Faster Cutting Plane Method and its Implications for Combinatorial and Convex Optimization. In 56th Annual Symposium on Foundations of Computer Science (FOCS 2015).
- [12] R. Kannan, L. Lov´asz, and M. Simonovits. Random walks and an O∗(n5) volume algorithm for convex bodies. Random Structures and Algorithms, 11(1):1–50, 1997.
- [13] S. Kirkpatrick, C. D. Gelatt, M. P. Vecchi, et al. Optimization by simulated annealing. Science, 220(4598):671–680, 1983.
- [14] D. A. Levin, Y. Peres, and E. L. Wilmer. Markov Chains and Mixing Times, volume 107. American Mathematical Society, 2017.
- [15] L. Lov´asz and S. Vempala. Simulated annealing in convex bodies and an O∗(n4) volume algorithm. Journal of Computer and System Sciences, 72(2):392–417, 2006.
- [16] MOSEK ApS. The MOSEK optimization toolbox for MATLAB manual. Version 8.1., 2017.
- [17] K. G. Murty and S. N. Kabadi. Some NP-complete problems in quadratic and nonlinear programming. Mathematical programming, 39(2):117–129, 1987.
- [18] Y. Nesterov and A. Nemirovskii. Interior-Point Polynomial Algorithms in Convex Programming. SIAM, 1994.
- [19] M. Rudelson. Random vectors in the isotropic position. Journal of Functional Analysis, 164(1):60–72, 1999.
- [20] R. L. Smith. Eﬃcient Monte Carlo procedures for generating points uniformly distributed over bounded regions. Operations Research, 32(6):1296–1308, 1984.
- [21] M. Tawarmalani and N. V. Sahinidis. A polyhedral branch-and-cut approach to global optimization. Mathematical Programming, 103(2):225–249, 2005.
- [22] W. Xia, J. Vera, and L. F. Zuluaga. Globally solving non-convex quadratic programs via linear integer programming techniques. arXiv preprint arXiv:1511.02423, 2015.
- [23] B. Ycart. Extr´emales du coˆne des matrices de type non n´egatif, ` coeﬃcients positifs ou nuls. Linear Algebra and its Applications, 48:317–330, 1982.
- [24] D. Yudin and A.S. Nemirovski, Informational complexity and eﬀective methods of solution of convex extremal problems. Economics and Mathematical Methods, 12:357–369, 1976.


