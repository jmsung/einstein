# arXiv:1507.02528v2[math.OC]5Nov2015

## Faster Convex Optimization: Simulated Annealing with an Eﬃcient Universal Barrier

Jacob Abernethy Department of Computer Science University of Michigan jabernet@umich.edu

Elad Hazan Department of Computer Science Princeton University ehazan@princeton.edu November 6, 2015

Abstract

This paper explores a surprising equivalence between two seemingly-distinct convex optimization methods. We show that simulated annealing, a well-studied random walk algorithms, is directly equivalent, in a certain sense, to the central path interior point algorithm for the the entropic universal barrier function. This connection exhibits several beneﬁts. First, we are able improve the state of the art time complexity for convex optimization under the membership oracle model. We improve the analysis of the randomized algorithm of Kalai and Vempala [7] by utilizing tools developed by Nesterov and Nemirovskii [16] that underly the central path following interior point algorithm. We are able to tighten the temperature schedule for simulated annealing which gives an improved running time, reducing by square root of the dimension in certain instances. Second, we get an eﬃcient randomized interior point method with an eﬃciently computable universal barrier for any convex set described by a membership oracle. Previously, eﬃciently computable barriers were known only for particular convex sets.

### 1 Introduction

Convex optimization is by now a well established ﬁeld and a cornerstone of the ﬁelds of algorithms and machine learning. Polynomial time methods for convex optimization belong to relatively few classes: the oldest and perhaps most general is the ellipsoid method with roots back to Kachiyan in the 50s [4]. Despite its generality and simplicity, the ellipsoid method is known to perform poorly in practice.

A more recent family of algorithms are the celebrated interior point methods, initially developed by Karmarkar in the context of linear programming, and generalized in the seminal work of Nesterov and Nemirovskii [16]. These methods are known to perform well in practice and come with rigorous theoretical guarantees of polynomial running time, but with a signiﬁcant catch: the underlying constraints must admit an eﬃciently-computable self-concordant barrier function. Barrier functions are deﬁned as satisfying certain diﬀerential inequality conditions that facilitate the path-following scheme developed by Nesterov and Nemirovskii [16], in particular it guarantees that the Newton step procedure maintains feasibility of the iterates. Indeed the iterative path following scheme essentially reduces the optimization problem to the construction of a barrier function, and in many nice scenarios a self-concordant barrier is easy to obtain; e.g., for polytopes the simple logarithmic barrier suﬃces. Yet up to the present there is no known universal eﬃcient construction of a barrier that applies to any convex set. The problem is seemingly even more diﬃcult in the membership oracle model where our access to K is given only via queries of the form “is x ∈ K?”.

The most recent polynomial time algorithms are random-walk based methods, originally pioneered in the work of Dyer et al. [3] and greatly advanced by Lov´sz and Vempala [13]. These algorithms apply in full generality of convex optimization and require only a membership oracle. The state of the art in polynomial time convex optimization is the random-walk based algorithm of simulated annealing and the speciﬁc temperature schedule analyzed in the breakthrough of Kalai and Vempala [7]. Improvements have been given in certain cases, most notably in the work of Narayanan and Rakhlin [14] where barrier functions were utilized.

In this paper we tie together two of the three known methodologies for convex optimization, give an eﬃciently computable universal barrier for interior point methods, and derive a faster algorithm for convex optimization in the membership oracle model. Speciﬁcally,

- 1. We deﬁne the heat path of a simulated annealing method as the (determinisitc) curve formed by the mean of the annealing distribution as the temperature parameter is continuously decreased. We show that the heat path coincides with the central path of an interior point algorithm with the entropic universal barrier function. This intimately ties the two major convex optimization methods together and shows they are approximately equivalent over any convex set.

We further enhance this connection by showing that the central path following interior point method applied with the universal entropic barrier is a ﬁrst-order approximation of simulated annealing.

- 2. Using the connection above, we give an eﬃcient randomized interior point method with an eﬃciently computable universal barrier for any convex set described by a membership oracle. Previously, eﬃciently computable barriers were known only for particular convex sets.
- 3. We give a new temperature schedule for simulated annealing inspired by interior point methods. This gives rise to an algorithm for general convex optimization with running time of O˜(√νn4), where ν is the self-concordance parameter of the entropic barrier. The previous state of the


art is O˜(n4.5) by [7]. We note that our algorithm does not need explicit access to the entropic barrier, it only appears in the analysis of the temperature schedule.

It was recently shown by Bubeck and Eldan [2] that the entropic barrier satisﬁes all require self-concordance properties and that the associated barrier parameter satisﬁes ν ≤ n(1 + o(1)), although this is generally not tight. Our algorithm improves the previous annealing run time by a factor of O˜( nν ) which in many cases is o(1). For example, in the case of semi-deﬁnite programming over matrices in Rn×n, the entropic barrier is identically the standard log-determinant barrier [5], exhibiting a parameter ν = n, rather than n2, which an improvement of n compared to the state-of-the-art. More details are given in section 4.4.

The Problem of Convex Optimization For the remainder of the paper, we will be considering the following algorithmic optimization problem. Assume we are given access to an arbitrary bounded convex set K ⊂ Rn, and we shall assume without loss of generality that K lies in a 2-norm ball of radius 1. Assume we are also given as input a vector θˆ ∈ Rn. Our goal is to solve the following:

θˆ x. (1)

min

x∈K

We emphasize that this is, in a certain sense, the most general convex optimization problem one can pose. While the objective is linear in x, we can always reduce non-linear convex objectives to the problem (1). If we want to solve minx∈K f(x) for some convex f : K → R, we can instead deﬁne a new problem as follows. Letting K := {(x,c) ∈ K × R : f(x) − c ≤ 0}, this non-linear problem is equivalent to solving the linear problem min{(x,c)∈K } c. This equivalence is true in in the membership oracle model, since a membership oracle for K immediately implies an eﬃcient membership oracle for K .

#### 1.1 Preliminaries

This paper ties together notions from probability theory and convex analysis, most deﬁnitions are deferred to where they are ﬁrst used. We try to follow the conventions of interior point literature as in the excellent text of Nemirovski [15], and the simulated annealing and random-walk notation of [7].

For some constant C, we say a distribution P is C-isotropic if for any vector v ∈ Rd we have

1 C

v 2 ≤ E

[(v X)2] ≤ C v 2.

X∼P

Let P,P be two distributions on Rn with means µ,µ , respectively. We say P is C-isotropic with respect to P if

1 C

[(v X)2].

[(v X)2] ≤ E

[(v X)2] ≤ C E

E

X∼P

X∼P

X∼P

One measure of the distance between two distributions, often referred to as the 2 norm, is given by

µ π ≡ E

µ(x) π(x)

µ(x) π(x)

dµ(x). We note that this distance is not symmetric in general.

=

x∼µ

x∼µ

For a diﬀerentiable convex function f : Rn → R, the Bregman divergence Df(x,y) between points x,y ∈ dom(f) is the quantity

Df(x,y) ≡ f(x) − f(y) − ∇f(y) (x − y).

Further, we can always deﬁne the Fenchel conjugate (or Fenchel dual) [17] which is the function f∗ deﬁned as

f∗(θ) := supx∈dom(f) θ x − f(x). (2) It is easy to see that f∗(·) is also convex, and under weak conditions one has f∗∗ = f. A classic duality result (see e.g. [17]) states that when f∗ is smooth and strictly convex on its domain and tends to inﬁnity at the boundary, we have a characterization of the gradients of f and f∗ in terms of maximizers:

∇f∗(θ) = arg max x∈dom(f)

θ x − f∗(θ). (3)

θ x − f(x) and ∇f(x) = arg max

θ∈dom(f∗)

#### 1.2 Structure of this paper

We start by an overview of random-walk methods for optimization in the next section, and introduce the notion of the heat path for simulated annealing. The following section surveys the important notions from interior point methods for optimization and the entropic barrier function. In section

- 4 we tie the two approaches together formally by proving that the heat path and central path are the same for the entropic barrier. We proceed to give a new temperature schedule for simulated annealing as well as prove its convergence properties. In the appendix we describe the KalaiVempala methodology for analyzing simulated annealing and its main components for completeness.


- 2 An Overview of Simulated Annealing Consider the following distribution over the set K for an arbitrary input vector θ ∈ Rn.


Pθ(x) := exp(−θ x)

K exp(−θ x )dx . (4) This is often referred to as the Boltzmann distribution and is a natural exponential family parameterized by θ. It was observed by [7] that the optimization objective (1) can be reduced to sampling from these distributions. That is, if we choose some scaling quantity t > 0, usually referred to as the temperature, then any sample X from the distribution Pθ/tˆ must be nt-optimal in expectation. More precisely, [7] show that

θˆ x ≤ nt. (5)

[θˆ X] − min

E

x∈K

X∼Pθ/tˆ

As we show later, our connection implies an even stronger statement, replacing n above by the self-concordant parameter of the entropic barrier, as we will deﬁne in the next section equation

(10). It is quite natural that for small temperature parameter t ∈ R, samples from the Pθ

are essentially optimal – the exponential nature of the distribution will eventually concentrate all probability mass on a small neightborhood around the maximizing point x∗ ∈ K. The problem, of course, is that sampling from a point mass around x∗ is precisely as hard as ﬁnding x∗.

t

This brings us to the technique of so-called simulated annealing, originally introduced by Kirkpatrick et al. [9] for solving generic problems of the form minx∈K f(x), for arbitrary (potentially non-convex) functions f. At a very high level, simulated annealing would begin by sampling from a “high-entropy” distribution (t very close to 0), and then continue by slowly “turning down the temperature” on the distribution, i.e. decreasing t, which involves sampling according to the pdf Qf,t(x) ∝ exp(−1tf(x)). The intuition behind annealing is that, as long as t /t is a small constant, then the distributions Qf,t and Qf,t will be “close” in the sense that a random walk starting from the initial distribution Qf,t will mix quickly towards its stationary distribution Qf,t.

Since its inception, simulated annealing is generally referred to as a heuristic for optimization, as polynomial-time guarantees have been diﬃcult to establish. However, the seminal work of Kalai and Vempala [7] exhibited a poly-time annealing method with formal guarantees for solving linear optimization problems in the form of (1). Their technique possessed a particularly nice feature: the sampling algorithm utilizes a well-studied random walk (Markov chain) known as HitAndRun [18, 10, 13], and the execution of this Markov chain requires only access to a membership oracle on the set K. That is, HitAndRun does not rely on a formal description of K but only the ability to (quickly) answer queries “x ∈ K?” for arbitrary x ∈ Rd.

Let us now describe the HitAndRun algorithm in detail. We note that this Markov chain was ﬁrst introduced by Smith [18], a poly-time guarantee was given by Lov´sz [10] for uniform sampling, and this was generalized to arbitrary log-concave distributions by Lov´sz and Vempala [11]. HitAndRun requires several inputs, including: (a) the distribution parameter θ, (b) an estimate of the covariance matrix Σ of Pθ, (c) the membership oracle OK, for K, (d) a starting point X0, and (e) the number of iterations N of the random walk.

- Algorithm 1: HitAndRun(θ,OK,N,Σ,X0) for approximately sampling Pθ


- 1 Inputs: parameter vector θ, oracle OK for K, covariance matrix Σ, #iterations N, initial X0 ∈ K.
- 2 for i = 1,2,...,N do

- 3 Sample a random direction u ∼ N(0,Σ)
- 4 Querying OK, determine the line segment R = {Xi−1 + ρu : ρ ∈ R} ∩ K
- 5 Sample a point Xi from R according to the distribution Pθ restricted to R

- 6 Return XN


The ﬁrst key fact of HitAndRun(θ) is that the stationary distribution of this Markov chain is indeed the desired Pθ; a proof can be found in [19]. The diﬃculty for this and many other random walk techniques is to show that the Markov chain “mixes quickly”, in that the number of steps N needn’t be too large as a function of n. This issue has been the subject of much research will be discussed below. Before proceeding, we note that a single step of HitAndRun can be executed quite eﬃciently. Sampling a random gaussian vector with covariance Σ (line 3) can be achieved by simply sampling a standard gaussian vector z and returning Σ1/2z. Computing the line segment R (line 4) requires simply ﬁnding the two locations where the line {Xi−1+ρu : ρ ∈ R} intersects with the boundary of K, but an -approximation of these points can be found via binary search using O log 1 queries to OK. Sampling from Pθ restricted to the line segment R can also be achieved eﬃciently, and we refer the reader to Vempala [19].

The analysis for simulated annealing in [7] proceeds by imagining a sequence of distributions

![image 1](<2015-abernethy-faster-convex-optimization-simulated_images/imageFile1.png>)

- Figure 1: The progression of two Hit-and-Run random walks for a high temperature (red squares) and a low temperature (black circles). Notice that at low temperature the walk coverges very quickly to a corner of K.


. Let k = O(√nlog n ),

k

where t1 = R is the diameter of the set K and tk := 1 − √1n

Pθk = Pθ/tˆ

k

then sampling from Pθk is enough to achieve the desired optimization guarantee. That is, via Equation 5, we see a sample from Pθk is -optimal in expectation.

To sample from Pθk, [7] construct a recursive sampling oracle using HitAndRun. The idea is

that samples from Pθk+1 can be obtained from a warm start by sampling from Pθk according to a carefully chosen temperature schedule. The details are given in Algorithm 2.

Algorithm 2: SimulatedAnnealing with HitAndRun – Kalai and Vempala [7]

- 1 Input: temperature schedule {tk,k ∈ [T]}, objective θˆ.
- 2 Set X0 = 0, Σ1 = I, t1 = R
- 3 for k = 1,...,T do

- 4 θk ← tθˆ

k

- 5 Xk ← HitAndRun(θk,OK,N,Σk,Xk−1)
- 6 for j = 1,..,n do

- 7 Ykj = HitAndRun(θk,OK,N,Σk,Ykj−1)

- 8 Estimate covariance: Σk+1 := CovMtx(Y1k,...,Ynk)

- 9 Return XT


The Kalai and Vempala [7] analysis leans on a number of technical but crucial facts which they

prove. The temperature update schedule that they devise, namely tk = (1 − √1n)tk−1, is shown to satisfy these iterative rules and thus return an approximate solution.

- Theorem 1 (Key result of Kalai and Vempala [7] and Lov´sz and Vempala [11]). Fix k and


consider the HitAndRun walk used in Algorithm 2 to compute Xk and Ykj for each j. Assume we choose the temperature schedule in order that successive distributions Pθk,Pθk−1 are close in 2:

, Pθk−1

max P Pθk

Pθk

θk−1 2

2

≤ 10. (6)

Then, as long as the warm start samples Xk−1 and Ykj−1 are (approximately) distributed according to Pθk−1, the random walk HitAndRun mixes to Pθk with N = O˜(n3) steps. That is, the output samples Xk and Ykj are distributed according to Pθk up to error ≤ .

In the appendix we sketch the proof of this theorem for completeness.

- Corollary 1. The temperature schedule tk := (1 − 1/√n)k t1 satisﬁes condition (6), and thus


- Algorithm 2 with this schedule returns an -approximate solution in time O˜(n4.5). Proof. By equation (5), to achieve error it suﬃce that 1t ≥ n , or in other words k needs to be large enough such that (1−√1n)k ≤ n for which k = 8√nlog n suﬃces: (1−√1n)k ≤ e−

k

2√n = e−4 log n ≤ n. Hence the temperature schedule need be applied with T = O˜(√n) iterations. Each iteration requires O(n) applications of HitAndRun that cost O(n3), for the total running time of O˜(n4.5).

| |
|---|


In later sections we proceed to give a more reﬁned temperature schedule that satisﬁes the KalaiVempala conditions, and thus results in a faster algorithm. Our temperature schedule is based on new observations in interior point methods, which we describe next.

- 2.1 The heat path for simulated annealing


Our main result follow from the observation that the path-following interior point method has an analogue in the random walk world. Simulated annealing incorporates a carefully chosen temperature schedule to reach its objective from a near-uniform distribution. We can think of all temperature schedules as performing a random process whose changing mean is a single well-deﬁned curve. For a given convex set K ⊆ Rd and objective θˆ, deﬁne the heat path as the following set of points, parametrized by the temperature t ∈ [0,∞] as follows:

HeatPath(t) = E

x∼Pθ/tˆ

[x]

We can now deﬁne the heat path as HeatPath = ∪t≥0{HeatPath(t)}. At this point it is not yet clear why this set of points is even a continuous curve in space, let alone equivalent to an analogous notion in the interior point world. We will return to this equivalence in section 4.

- 3 An Overview of Interior Point Methods for Optimization


Let us now review the vast literature on Interior Point Methods (IPMs) for optimization, and in particular the use of the Iterative Newton Step technique. The ﬁrst instance of polynomial time algorithms for convex optimization using interior point machinery was the linear programming algorithm of Karmarkar [8]. The pioneering book of Nesterov and Nemirovskii [16] brought up

techniques in convex analysis that allowed for polynomial time algorithms for much more general convex optimization, ideas that are reviewed in great detail and clarity in [15] .

The goal remains the same, to solve the linear optimization problem posed in Equation (1). The intuition behind IPMs is that iterative update schemes such as gradient descent for solving (1) can fail because the boundary of K can be diﬃcult to manage, and “moving in the direction of descent” will fail to achieve a fast rate of convergence. Thus one needs to “smooth out” the objective with the help of an additional function. In order to produce an eﬃcient algorithm, a well-suited type of function is known as a self-concordant barrier which have received a great deal of attention in the optimization literature.

A self-concordant barrier function ϕ : int(K) → R, with barrier parameter, ν is a convex function satisfying two diﬀerential conditions: for any h ∈ Rn and any x ∈ K,

∇3ϕ[h,h,h] ≤ 2(∇2ϕ[h,h])3/2, and ∇ϕ[h] ≤ ν∇2ϕ[h,h], (7)

in addition to the property that the barrier should approach inﬁnity when approaching the boundary of K. Such function possess very desirable properties from the perspective of optimization, several of which we discuss in the present section. We note an important fact: while the existence of such a function ϕ for general sets K has been given by Nesterov and Nemirovskii [16]—the universal barrier with parameter parameter ν = O(n), to be discussed further in Section 4.4—an eﬃcient construction of such a function has remained elusive and was considered an important question in convex optimization. This indeed suggests that the annealing results we previously outlined are highly desirable, as HitAndRun requires only a membership oracle on K. However, one of the central results of the present work is the equivalence between annealing and IPMs, where we show that sampling gives one implicit access to a particular barrier function. This will be discussed at length in Section 4.

Let us now assume we are given such a function ϕ with barrier parameter ν. A standard approach to solving (1) is to add the function ϕ(x) to the primary objective, scaling the linear term by a “temperature” parameter t > 0:

{tθˆ x + ϕ(x)}. (8) As the the temperature t tends to ∞ the solution of (8) will tend towards the optimal solution to

min

x∈K

1. This result is proved for completeness in Theorem 2.

Towards developing in detail the iterative Newton algorithm, let us deﬁne the following for every positive integer k:

k

tk := 1 + √cν

for some c > 0, (9) Φk(x) := tkθˆ x + ϕ(x)

Φk(x) As ϕ is a barrier function, it is clear that x¯k is in the interior of K and, in particular, ∇Φk(¯xk) =

x¯k := arg min

x

- 0 =⇒ ∇ϕ(¯xk) = tkθˆ. It is shown in [15] (Equation 3.6) that any ν-SCB (Self-Concordant Barrier) ϕ satisﬁes ∇ϕ(x) (y − x) ≤ ν, whence we can bound the diﬀerence in objective value between x¯k and the optimal point x∗:


θˆ (x∗ − x¯k) = ∇ϕ(¯xk) (x∗ − x¯k) tk ≤

ν tk

. (10)

We see that the approximation point x¯k becomes exponentially better as k increases. Indeed, setting k =

√ν

c log(ν/ ) guarantees that the error is bounded by .

The iterative Newton’s method technique actually involves approximating x¯k with xˆk, a nearoptimal maximizer of Φk, at each iteration k. For an arbitrary v ∈ Rn, x ∈ int(K), and any k ≥ 1, following [15] we deﬁne:

v x := v ∇2ϕ(x)v, the “local norm” of v w.r.t x; (11) v ∗x := v ∇−2ϕ(x)v, the corresponding dual norm of v, (12)

λ(x,tk) :=  ∇Φk(x) ∗x, the Newton decrement of x for temperature tk. (13)

Note that, for a ﬁxed point x ∈ K, the norms · x and · ∗x are dual to each other1. It will turn out that λ(x,tk) will be used both as a quantity in the algorithm, and as a kind of potential that we need to keep small.

In Algorithm 3 we describe the damped newton update algorithm, henceforth called IterativeNewtonStep. We note that the

Algorithm 3: IterativeNewtonStep

- 1 Input: θˆ ∈ Rd, K and barrier function ϕ
- 2 Solve: xˆ0 = arg maxx∈K θˆ x + ϕ(x)
- 3 for k = 1,2,... do

- 4 xˆk ← xˆk−1 − 1+λ(ˆx1


k−1,tk)∇−2ϕ(ˆxk−1)∇Φk(ˆxk−1)

The most diﬃcult part of the analysis is in the following two lemmas, which are crucial elements of the IterativeNewtonStep analysis. A full exposition of these results is found in the excellent survey [15]. The ﬁrst lemma tells us that when we update the temperature, we don’t perturb the Newton decrement too much. The second lemma establishes the quadratic convergence of the Newton Update for a ﬁxed temperature.

- Lemma 1. Let c be the constant chosen in the deﬁnition (9). Let t > 0 be arbitrary and let t = t 1 + √cν . Then for any x ∈ int(K), we have λ(x,t ) ≤ (1 + c)λ(x,t) + c.

- Lemma 2. Let k be arbitrary and assume we have some xˆk−1 such that λ(ˆxk−1,tk) is ﬁnite. The Newton update xˆk satisﬁes λ(ˆxk,tk) ≤ 2λ2(ˆxk−1,tk).

The previous two lemmas can be combined to show that the following invariant is maintained. Neither the constant bound of 1/3 on the Newton decrement nor the choice of c = 1/20 are particularly fundamental; they are convenient for the analysis but alternative choices are possible.

- Lemma 3. Assume we choose c = 1/20 for the parameter in (9). Then for all k we have λ(ˆxk,tk) <


- 1


- 3.


1Technically, for   ·  x and its dual to be a norm, we need ∇2ϕ to be positive deﬁnite and ϕ to be strictly convex. One can verify this is the case for bounded sets, which is the focus of this paper.

Proof. We give a simple proof by induction. The base case is satisﬁed since we assume that λ(ˆx0,t0) = 0, as t0 = 1.2 For the inductive step, assume λ(ˆxk−1,tk−1) < 1/3. Then

λ(ˆxk,tk) ≤ 2λ2(ˆxk−1,tk) ≤ 2((1 + c)λ(ˆxk−1,tk−1) + c)2 < 2(0.4)2 < 1/3.

The ﬁrst inequality follows by Lemma 2 and the second by Lemma 1, hence we are done.

| |
|---|


- Theorem 2. Let x∗ be a solution to the objective (1). For every k, xˆk is an k-approximate solution


√ν/4 tk . In particular, for any > 0, as long as k >

√ν

to (1), where k = ν+

c log(2ν/ ) then xˆk is an

-approximation solution. Proof. Let k be arbitrary. Then,

θˆ (ˆxk − x∗) = θˆ (¯xk − x∗) + θˆ (ˆxk − x¯k) (By (10)) ≤ tν

+ θˆ (ˆxk − x¯k) (H¨older’s Inequality) ≤ tν

k

+ θ ˆ ∗x¯

x ¯k − xˆk x ¯k ([15] Eqn. 2.20) ≤ tν

k

k

λ(ˆxk,tk) 1−λ(ˆxk,tk) (Applying Lemma 3 and (14)) ≤ tν

+ θ ˆ ∗x¯

k

k

√ν/4 tk

∗ x¯k

+ ∇ϕt(¯xk)

1 4 ≤ ν+

k

k

The last equation utilizes a fact that derives immediately from the deﬁnition (7), namely

√ν (14) holds for any SCBF ϕ with parameter ν, and for any x ∈ K.

 ∇ϕ∗(x) ∗x =  ∇ϕ∗(x) θ(x) ≤

| |
|---|


We proceed to give a speciﬁc barrier function that applies to any convex set and gives rise to an eﬃcient algorithm.

### 4 The Equivalence of IterativeNewton and SimulatedAnnealing

We now show that the previous two techniques, Iterative Newton’s Method and Simulated Annealing, are in a certain sense two sides of the same coin. In particular, with the appropriate choice of barrier function ϕ the task of computing the sequence of Newton iterates xˆ1,xˆ2,... may be viewed precisely as estimating the means for each of the distributions Pθ1,Pθ2,.... This correspondence helps to unify two very popular optimization methods, but also provides three additional novel results:

- 1. We show that the heat path for simulated annealing is equivalent to the central path with the entropic barrier.


2As stated, Algorithm 3 requires ﬁnding the minimizer of ϕ(·) on K, but this is not strictly necessary. The convergence rate can be established as long as a “reasonable” initial point xˆ0 can be computed—e.g. it suﬃces that λ(ˆx0, 1) < 1/2.

- 2. We show that the running time of Simulated Annealing can be improved to O(n4√ν) from the previous best of O(n4.5). In the most general case we know that ν = O(n), but there are many convex sets in which the parameter ν is signiﬁcantly smaller. Notably such is the case for the positive-semi-deﬁnite cone, which is the basis of semi-deﬁnite programming and a cornerstone of many approximation algorithms. Further examples are surveyed in section 4.4.

- 3. We show that Iterative Newton’s Method, which previously required a provided barrier function on the set K, can now be executed eﬃciently where the only access to K is through a membership oracle. This method relies heavily on previously-developed sampling techniques [7]. Discussion is deferred to Appendix C.
- 4.1 The Duality of Optimization and Sampling We begin by rewriting our Boltzmann distribution for θ in exponential family form,


Pθ(x) := exp(−θ x − A(θ)) where A(θ) := log K exp(−θ x )dx . (15)

The function A(·) is known as the log partition function of the exponential family, and it has several very natural properties in terms of the mean and variance of Pθ:

∇A(θ) = − E

[X] (16) ∇2A(θ) = E

X∼Pθ

[(X − EX)(X − EX) ]. (17)

X∼Pθ

We can also appeal to Convex (Fenchel) Duality [17] to obtain the conjugate

A∗(x) := supθ θ x − A(θ). (18)

It is easy to establish that A∗ is smooth and strictly convex. The domain of A∗(·) is precisely the space of gradients of A(·), and it is straightforward to show that this is the set int(−K), the interior of the reﬂection of K about the origin. However we want a function deﬁned on (the interior of) K, not its reﬂection, so let us deﬁne a new function A∗−(x) := A∗(−x) whose domain is int(K). We now present a recent result of Bubeck and Eldan [2].

- Theorem 3 ([2]). The function A∗− is a ν-self-concordant barrier function on K with ν ≤ n(1 + o(1)).


One of the signiﬁcant drawbacks of barrier/Newton techniques is the need for a readily-available self-concordant barrier function. In their early work on interior point methods, Nesterov and Nemirovskii [16] provided such a function, often referred to as the “universal barrier”, yet the actual construction was given implicitly without oracle access to function values or derivatives. Bubeck and Eldan [2] refer to function A∗−(·) as the entropic barrier, a term we will also use, as it relates to a notion of diﬀerential entropy of the exponential family of distributions.

It is important to note that, when our set of interest is a cone K, the entropic barrier on K corresponds exactly to the Fenchel dual of the universal barrier on the dual cone K∗ [6], which immediately establishes the self-concordance. Indeed, many beautiful properties of the entropic barrier on cones have been developed, and for a number of special cases A∗−(·) corresponds exactly

to the canonical barrier used in practice; e.g. A∗−(·) on the PSD cone corresponds to the logdeterminant barrier. In many such cases one obtains a much smaller barrier parameter ν than the n(1 + o(1)) bound. We defer a complete discussion to Section 4.4.

In order to utilize A∗−(·) as a barrier function as in (8) we must be able to approximately solve objectives of the form minx∈K{θ x + A∗−(x)}. One of the key observations of the paper, given in the following Proposition, is that solving this objective correponds to computing the mean of the distribution Pθ.

Proposition 1. Let θ ∈ Rn be arbitrary, and let Pθ be deﬁned as in (15). Then we have

θ x + A∗−(x) . (19)

E

[X] = arg min

X∼Pθ

x∈int(K)

Proof. Let θ be an arbitrary input vector. As we mentioned in (3), standard Fechel duality theory gives us

θ x − A∗(x) = arg min

−θ x + A∗(x) .

∇A(θ) = arg max

x∈dom(A∗)

x∈dom(A∗)

It can be veriﬁed that the domain of A∗ is precisely the interior of −K, the reﬂection of K. Thus we have

θ x + A∗−(x) .

−θ x + A∗(x) = − arg min x∈int(K)

∇A(θ) = arg min

x∈int(−K)

In addition, we noted in (15) that ∇A(θ) = −EX∼Pθ[X]. Combining the latter two facts gives the result.

| |
|---|


We now have a direct connection between sampling methods and barrier optimization. For the remainder of this section, we shall assume that our chosen ϕ(·) is the entropic barrier A∗(·), and the quantities Φk(·), · x,λ(·,·) are deﬁned accordingly. We shall also use the notation x(θ) := EX∼Pθ[X] = −∇A(θ).

- Lemma 4. Let θ,θ be such that x(θ ) − x(θ) x(θ) ≤ 12. Then we have


(x(θ ),x(θ)) = KL(P θ,Pθ) = DA(θ,θ ) ≤ 2 x(θ ) − x(θ) 2x(θ) (20) Proof. The duality relationship of the Bregman divergence, and its equivalence to Kullback-Leibler divergence, is classical and can be found in, e.g., [20] equation (5.10) The ﬁnal inequality follow as a direct consequence of [15], Equation 2.4.

DA∗

−

| |
|---|


#### 4.2 Equivalence of the heat path and central path

The most appealing observation on the equivalence between random walk optimization and interior point methods is the following geometric equivalence of curves. For a given convex set K ⊆ Rd and objective θˆ, deﬁne the heat path as the following set of points:

##### { E

[x]}

HeatPath = ∪

{HeatPath(t)} = ∪

t≥0

t≥0

x∼Pθˆ t

To see that this set of points is a continuous curve in space, consider the central path w.r.t. barrier function ϕ(x):

{tθˆ x + ϕ(x)}

CentralPath(ϕ) = ∪

{CentralPath(t,ϕ)} = ∪

{arg min

t≥0

t≥0

x∈K

![image 2](<2015-abernethy-faster-convex-optimization-simulated_images/imageFile2.png>)

- Figure 2: For a set of seven diﬀerent temperatures t, we used Hit-and-Run to generate and scatter


plot several samples from Pθ/t using colored circles. We also computed the true means for each distribution, plotted with squares, giving a curve representing the HeatPath across the seven temperatures. Of course via Corollary 2 this corresponds exactly to the CentralPath for the entropic barrier.

It is well known that the central path is a continuous curve in space for any self-concordant barrier function φ. We now have the following immediate corollary of Proposition 1:

- Corollary 2. The central path corresponding to the self-concordant barrier A∗ over any set K is equivalent to the heat path over the same set, i.e.


HeatPath ≡ CentralPath(A∗)

This mathematical equivalence is demonstrated in ﬁgure 2 generated by simulation over a polytope.

#### 4.3 IPM techniques for sampling and the new schedule We now prove our main theorem, formally stated as:

- Theorem 4. The temperature schedule of θ1 = R where R = diam(K) and θk := 1 − 4√1ν θk−1, for ν being the self-concordance parameter of the entropic barrier for the set K, satisﬁes condition


(6) of theorem 1. Therefore algorithm 2 with this schedule returns an -approximate solution in time O˜(√νn4).

Condition (6) is formally proved in the following lemma, which crucially uses the interior point methodology, namely Lemma 3.

- Lemma 5. Consider distributions Pθ and Pθ where θ = (1 + γ)θ for γ < 6√1ν. Then we have the following bound on the 2 distance between distributions:


P(1+γ)θ

Pθ P(1+γ)θ 2

Pθ 2 ≤ 10 Proof. We ﬁrst show by elementary linear algebra that

max

,

Pθ/P(1−γ)θ = Pθ/P(1+γ)θ = exp(DA((1 + γ)θ,θ) + DA((1 − γ)θ,θ)). Let us consider the log of the 2-norm:

exp(−θ x − A(θ)) exp(−(1 + γ)θ x − A((1 + γ)θ))

dPθ

log Pθ/P(1+γ)θ = log

K

exp(γθ x − A(θ) + A((1 + γ)θ))dPθ

= log

K

exp(γθ x − A(θ) + A((1 + γ)θ))exp(−θ x − A(θ))dx

= log

K

= A((1 + γ)θ) − 2A(θ) + log

exp(−(1 − γ)θ x)dx

K

= A((1 + γ)θ) − 2A(θ) + A((1 − γ)θ) = DA((1 + γ)θ,θ) + DA((1 − γ)θ,θ).

Replacing γ by −γ, we get a completely symmetrical expression. Next, we observe that

Pθ(1+γ)/Pθ = Pθ˜/Pθ˜(1−γ˜)

where θ˜ = θ(1 + γ) and 1 − γ˜ = 1+1γ = 1 − 1+γγ, thus γ˜ ∈ γ × [1,2]. By this observation, both sides of the lemma follow if we prove an upper bound

Pθ P(1+γ)θ 2 ≤ 10 for γ <

1 6√ν × 2 =

1 3√ν

Lemma 1 implies λ(x(θ),1 + γ) ≤ (1 + c)λ(x(θ),1) + c = c ≤ 14. Applying Lemma 4, DA((1 + γ)θ,θ) ≤ 2 x(θ) − x((1 + γ)θ) 2x((1+γ)θ) Lemma 4 ≤ 2 1− λ(λx((xθ()θ,)1+,1+γ)γ)

2

(2.28) in [15]

2

2

< 2(1/3)

≤ 2 1− cc

(2/3)2 = 12 Lemma 1

Notice that to apply Lemma 4, we need the point x((1 + γ)θ) to lie in the Dikin ellipsoid of x(θ), which is exactly whats proved in the last two lines of the above proof.

The bound on DA((1−γ)θ,θ) follows in precisely the same fashion, by similar change of variables as before (again, the condition for applying Lemma 4 is proven in the last few lines of the equations

below):

DA((1 − γ)θ,θ) = DA(θ,˜ θ˜(1 + γ˜)) ≤ 2 x(θ˜) − x((1 + γ˜)θ˜) 2x(θ˜) Lemma 4

2

≤ 2 1− λ(λx((xθ˜()θ˜,)1+˜,1+ˆγ)γ)

(2.27) in [15]

2

2

< 2(1/3)

≤ 2 1− cc

(2/3)2 = 12 Lemma 1

It follows that Pθ/P(1+γ)θ ≤ eDA((1+γ)θ,θ)+DA((1−γ)θ,θ) ≤ e12+12 ≤ 10.

| |
|---|


#### 4.4 Some history on the entropic barrier and the universal barrier for cones

Let K be a cone in Rn and let K∗ = {θ : θ x ≥ 0 ∀x ∈ K} be its dual cone. We note that a cone K is homogeneous if its automorphism group is transitive; that is, for every x,y ∈ K there is an automorphism B : K → K such that Bx = y. Homogeneous cones are very rare, but one notable example is the PD cone (matrices with all positive eigenvalues). Given any point x ∈ K, we can deﬁne a truncated region of K∗ as the set K∗(x) := {y ∈ K∗ : x y ≤ 1}. Nesterov and Nemirovskii [16] deﬁned the ﬁrst generic self-concordant barrier function, known as the universal barrier in terms of these regions. Namely, they show that the function

uK(x) := log(vol(K∗(x))) is a self concordant barrier function with an O(n) parameter.

There is an alternative characterization of the universal barrier in terms of the larg partition

function. Let FK(x) := log K∗ exp(θ x)dθ and equivalently let FK∗(θ) := log K exp(θ x)dx. It was shown by G¨uler [5] that

FK(x) = uK(x) + n!, that is, the universal barrier corresponds exactly to a log-partition function but deﬁned on the dual cone K∗, modulo a simple additive constant. We note that this is not the entropic barrier construction we have here, as our function of interest is A∗−(·) ≡ FK∗ ∗(·) (the Fenchel conjugate of FK∗(x)), and not FK(x). However, it was also shown by G¨uler [5] that, when K is a homogeneous cone, we have the identity FK(·) ≡ FK∗ ∗(·); in other words, the universal barrier and the entropic barrier are equivalent for homogeneous cones.

It is worth noting that, following the connection of Gu¨ler [5], A∗−(·) is (up to additive constant) the Fenchel conjugate of the universal barrier uK∗ for K∗. It was shown by Nesterov and Nemirovskii [16] (Theorem 2.4.1) that Fenchel conjugation preserves all required self concordance properties and in particular if g is a ν-self-concordant barrier for a cone K, then g∗ will be a self-concordant barrier for K∗ with the same parameter ν. With this observation it follows immediately that the entropic barrier FK∗ ∗(·) on K is an O(n)-self-concordant barrier. Bubeck and Eldan [2] took this statement further, proving that FK∗ ∗(·) enjoys an essentially optimal self-concordance parameter ν = n(1 + o(1)).

It is important to note that the assumption that the set of interest is a cone is, roughly speaking, without loss of generality. Given any convex set U ⊂ Rn we have the ﬁtted cone K(U) := {α(x,1) : x ∈ U,α ≥ 0} ⊆ Rn+1. Hence once can always work with the barrier function FK∗ (U)∗(·) on K(U),

and take its restriction to the set U × {1} ⊂ K(U) to obtain a barrier on U (aﬃne restriction preserves the barrier properties).

We conclude by summarizing several results in Gu¨ler [5] regarding the entropic barrier for various cones, as well as the associated barrier parameter of each. In these canonical cases the entropic barrier corresponds exactly to the “typical” barrier, up to additive and multiplicative constants. We use the notation f(·) ∼= g(·) to denote that f and g are identical up to additive constants.

- 1. Assume K := Rn+ the nonnegative orthant. This is a homogeneous cone and we have FK(x) ∼= FK∗ ∗(x) ∼= − ni=1 log xi. This is the optimal barrier for K and the barrier parameter is ν = n.
- 2. Assume K := {x ∈ Rn : x21+...+x2n−1 ≤ x2n} be the Lorentz cone. K is a homogeneous self-dual cone. K can also be described by the ﬁtted cone of the radius-1 L2 ball, so we may parameterize elements of K as α(x,1) where α ≥ 0 and x is vector in Rn−1 with L2 norm bounded by 1. Then FK(α(x,1)) ∼= FK∗ ∗(α(x,1)) ∼= −n+12 log(α2 − x2). This barrier has parameter ν = n + 1 which is indeed not optimal, one has the optimal barrer −log(α2 − x2) which has parameter ν = 2, but this is simply a scaled version of the entropic barrier.

- 3. The PSD cone K of positive semi-deﬁnite matrices, i.e. symmetric matrices with non-negative eigenvalues, is a homogeneous self-dual cone. The entropic barrier is FK(x) ∼= FK∗ ∗(x) ∼=


−n+12 log det(x) and exhibits a parameter of ν = n(n2+1) which is multiplicatively n+12 worse than the optimal barrier, the log-determined −log det(x). However, as can be seen this barrier

is quite simply a scaled version of the entropic barrier.

### Bibliography

- [1] R. Adamczak, A. E. Litvak, A. Pajor, and N. Tomczak-Jaegermann. Quantitative estimates of the convergence of the empirical covariance matrix in log-concave ensembles. Journal of the American Mathematical Society, 23:535–561, apr 2010. doi: 10.1090/S0894-0347-09-00650-X.
- [2] S. Bubeck and R. Eldan. The entropic barrier: a simple and optimal universal self-concordant barrier. arXiv preprint arXiv:1412.1587, 2014.
- [3] M. Dyer, A. Frieze, and R. Kannan. A random polynomial-time algorithm for approximating the volume of convex bodies. J. ACM, 38(1):1–17, Jan. 1991. ISSN 0004-5411.
- [4] M. Gr¨tschel, L. Lov´sz, and A. Schrijver. Geometric algorithms and combinatorial optimization. Algorithms and combinatorics. Springer-Verlag, 1993. ISBN 9780387136240. URL https://books.google.com/books?id=agLvAAAAMAAJ.
- [5] O. Gu¨ler. Barrier functions in interior point methods. Mathematics of Operations Research, 21(4):860–885, 1996.
- [6] O. Gu¨ler. On the self-concordance of the universal barrier function. SIAM Journal on Optimization, 7(2):295–303, 1997.
- [7] A. T. Kalai and S. Vempala. Simulated annealing for convex optimization. Mathematics of Operations Research, 31(2):253–266, 2006.


- [8] N. Karmarkar. A new polynomial-time algorithm for linear programming. In Proceedings of the Sixteenth Annual ACM Symposium on Theory of Computing, STOC ’84, pages 302–311, 1984.
- [9] S. Kirkpatrick, M. Vecchi, et al. Optimization by simmulated annealing. science, 220(4598): 671–680, 1983.
- [10] L. Lov´sz. Hit-and-run mixes fast. Mathematical Programming, 86(3):443–461, 1999.
- [11] L. Lov´sz and S. Vempala. The geometry of logconcave functions and an o(n3) sampling algorithm. Technical report, Technical Report MSR-TR-2003-04, Microsoft Research, 2003.
- [12] L. Lov´sz and S. Vempala. Hit-and-run from a corner. SIAM J. Comput., 35(4):985–1005, Apr. 2006. ISSN 0097-5397.
- [13] L. Lov´sz and S. Vempala. Fast algorithms for logconcave functions: Sampling, rounding, integration and optimization. In Foundations of Computer Science, 2006. FOCS’06. 47th Annual IEEE Symposium on, pages 57–68. IEEE, 2006.
- [14] H. Narayanan and A. Rakhlin. Random walk approach to regret minimization. In Advances in Neural Information Processing Systems, pages 1777–1785, 2010.
- [15] A. Nemirovski. Interior point polynomial time methods in convex programming. Lecture Notes– Faculty of Industrial Engineering and Management, Technion–Israel Institute of Technology, Technion City, Haifa, 32000, 1996.
- [16] Y. Nesterov and A. Nemirovskii. Interior-point Polynomial Algorithms in Convex Programming, volume 13. SIAM, 1994.
- [17] R. T. Rockafellar. Convex analysis. Princeton university press, 1970.
- [18] R. L. Smith. Eﬃcient monte carlo procedures for generating points uniformly distributed over bounded regions. Operations Research, 32(6):1296–1308, 1984.
- [19] S. Vempala. Geometric random walks: a survey. MSRI volume on Combinatorial and Computational Geometry, 2005.
- [20] M. J. Wainwright and M. I. Jordan. Graphical models, exponential families, and variational inference. Foundations and Trends R in Machine Learning, 1(1-2):1–305, 2008.


### A An Explanation of Newton’s Method via Reweighting

Proposition 1 brings out a strong connection between interior point techniques and the ability to sample from Boltzmann distributions. But with this stochastic viewpoint, it is not immediately clear why Newton’s method is an appropriate iterative update scheme for optimization. We now provide some evidence along these lines.

Assuming we have already computed (an approximation of) x(θ), and our distribution parameter is updated to a “nearby” θ , our goal is now to compute the new mean x(θ ).

−x(θ ) =

xdPθ =

K

dPθ (x) dPθ(x)

dPθ = E

x

X∼Pθ

K

X exp(X (θ − θ ) + A(θ ) − A(θ))

Think of the last term as the reweighting factor. Now we are going to rewrite A(θ) − A(θ ) = −∇A(θ)(θ −θ)−DA(θ ,θ) = x(θ) (θ −θ)−KL(Pθ,Pθ ). We shall use the following approximation of the exponential: exp(z) ≈ 1 + z for small values of z. Proceeding,

−x(θ ) = E

X exp(X (θ − θ ) − x(θ) (θ − θ) + KL(Pθ,Pθ ))

X∼Pθ

= eKL(Pθ,Pθ ) E

X exp((X − x(θ)) (θ − θ))

X∼Pθ

≈ eKL(Pθ,Pθ ) E

X(1 + (X − x(θ)) (θ − θ))

X∼Pθ

= eKL(Pθ,Pθ )(−x(θ) + Σθ(θ − θ)).

Duality theory tells us that Σθ = ∇2A(θ) = ∇−2A∗(x(θ)) and θ −θ is precisely the gradient of the objective θ x − A∗(x) at the point x(θ). The eKL(Pθ,Pθ ) term is somewhat mysterious, but it can be interpreted as something of a “damping” factor akin to the Newton decrement damping of the the Newton update.

### B Proof structure of the Kalai-Vempala theorem

We hereby sketch the structure of the proof of theorem 1 for completeness. Recall the statement of the theorem:

Algorithm 2 with a temperature schedule that satisﬁes the following condition:

The successive distributions are not “too far” in total variational distance. That is, for every j,

Pθj Pθj−1 2

Pθj−1 Pθj 2 ≤ 10

max

,

Guarantees that HitAndRun requires N = O˜(n3) steps in order to ensure mixing to the stationary distribution Pθj. Proof sketch. The proof is based on iteratively applying the following Theorem from [12]:

- Theorem 5. Let f be a density proportional to e−aTx over a convex set K such that


- [a]. the level set of probability 1/64 contains a ball of radius s
- [b]. Ef( x − µf 2) ≤ S, where µf = Ef[x] is the mean of f
- [c]. the 2 norm of the starting distribution σ w.r.t. the stationary distribution of HitAndRun denoted πf, is at most M.


Let σm be the distribution of the current point after m steps of HitAndRun applied to f. Then, for any τ > 0, after m = O(n2sS22 log5 nMτ ) steps, the total variation distance of σm and πf is less than τ.

The proof proceeds to show that conditions [a]-[c] of the theorem above are all satisﬁed if indeed condition (6) is satisﬁed, along the steps below. Once it is established that the conditions of the theorem hold, then the next HitAndRun walk mixes and computes warm start and variance estimates for the next epoch. Then again, the conditions of the theorem hold, and this whole process is repeated for the entire temperature schedule.

To show conditions [a]-[c], ﬁrst notice that condition (6) is essentially equivalent to condition [c] above. Thus we only need to worry about conditions [a],[b].

- [I]. For simplicity, we assumed that at the current iteration, Σj = I is the identity. This can be assumed by a transformation of the space, and allows for simpler discussion of isotropy of densities (otherwise, the isotropy condition would be replaced by relative-isotropy w.r.t the current variance).
- [II]. A density f is C-isotropic if for any unit vector v = 1, 1

C ≤

Rn

(v (x − µf))2f(x)dx ≤ C

It is shown (Lemma 4.2) that if the density given by f is O(1)-isotropic, then conditions [a],[b] are satisﬁed with Ss = O˜(√n).

- [III]. It is shown (Lemma 4.3) that if f is C-isotropic, and max fg

2

, f g

2

≤ D, then g is CD-isotropic.

- [IV]. Since condition (6) holds, together with the previous points [II,III] this implies that fθj+1 is isotropic for some constant. Thus, conditions [a]-[c] of Theorem 5 hold. Therefore we can


sample suﬃciently many samples to estimate the covariance matrix Σj+1 and proceed to the next epoch.

Throughout the proof special care needs to be taken to ensure that repeated samples are nearlyindependent for various concentration lemmas to apply, we omit discussion of these and the reader is referred to the original paper of [7].

| |
|---|


### C Interior point methods with a membership oracle

Below we sketch a universal IPM algorithm - one that applies to any convex set described by a membership oracle - that can be implemented to run in polynomial time. This algorithm is an instantiation of Algorithm 3 with the particular barrier function A∗(x) as deﬁned in section 4.1.

Without loss of generality, we can assume our goal is to (approximately) compute the update direction

∇−2A∗(x)(θ − ∇A∗(x))

for some x which is already within the Dikin ellipsoid of radius 1/2 around x(θ). First, we note that the IPM analysis of [15] allows one to replace the inverse hessian ∇−2A∗(x) with the nearby ∇−2A∗(x(θ)) = CovMtx(Pθ). Of course the latter can be estimated via sampling, in the sense that the estimate Σˆ will be “ -isotropically close”:

(1 − )v ∇2Ψ(θ )v ≤ v Σ ˆv ≤ (1 + )v ∇2Ψ(θ )v for any unit vector v. See, for example, [1] on the concentration of empirical covariance matrices.

It remains to compute ∇A∗(x). Deﬁne θ(x) to be

θ · x − log

θ(x) = arg max

θ

exp(−θ · y)dy = ∇A∗(x) (21)

K

Then θ(x) can be computed in polynomial time by another interior point algorithm – this problem, however, is much simpler to work with. Deﬁne Ψ(θ ) := θ·x−log K exp(−θ·y)dy to be the objective we want to optimize. Notice that ∇Ψ(θ ) = x − EX ∼Pθ [X ] and the latter can be estimated to within via SimulatedAnnealing with O˜(n/ 2) samples. The hessian ∇2Ψ(θ ) = −CovMtx(Pθ ) can similarly be estimated with an -isotropically close empirical covariance. Because the error gap is multiplicatively close to 1, the inverse operation on ∇2Ψ(θ ) maintains the approximation.

