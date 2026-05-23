---
type: source
kind: paper
title: "Proximal basin hopping: global optimization with guarantees"
authors: Guillaume Lauga, Cesare Molinari, Samuel Vaiter
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2605.18364v1
source_local: ../raw/2026-lauga-proximal-basin-hopping-global.pdf
ingested_for_concept: basin-hopping-multistart.md
cites:
  - ../wiki/concepts/basin-hopping-multistart.md
  - ../wiki/problems/1-*.md
  - ../wiki/problems/10-*.md
  - ../wiki/problems/12-*.md
  - ../wiki/problems/13-*.md
  - ../wiki/problems/15-*.md
  - ../wiki/problems/16-*.md
  - ../wiki/problems/17-*.md
---

# arXiv:2605.18364v1[cs.LG]18May2026

## Proximal basin hopping: global optimization with guarantees

Cesare Molinari MALGA Università di Genova Italy cecio.molinari@gmail.com

Guillaume Lauga LJAD Université Côte d’Azur France guillaume.lauga@univ-cotedazur.fr

Samuel Vaiter CNRS, LJAD Université Côte d’Azur France samuel.vaiter@univ-cotedazur.fr

May 19, 2026

Abstract

Global optimization is a challenging problem, with plenty of algorithms displaying empirical success, but scarce theoretical backing. In this work, we propose a new theoretical framework called Proximal Basin Hopping (PBH), carefully tailored to combine proximal optimization and local minimization. We use it to construct a practical algorithm that converges to the global minimizer with high probability, when using a finite amount of samples. Proximal Basin Hopping outperforms well known algorithms with theoretical backing on standard synthetic hard functions, and real problems such as fitting scaling laws for deep learning. Furthermore, the higher the dimension, the better the performance gap.

### 1 Introduction

Finding global minimizers of highly non-convex functions is a challenging but crucial task in various fields such as computational chemistry and biology [Prentiss et al., 2008, Alvarez and Calaminici, 2025], engineering design [Arora et al., 1995, Englander et al., 2020] and of course machine learning [Goodfellow et al., 2016]. We are interested in solving the following optimization problem

f(x). (1)

Find x ∈ arg min

x∈Rd

where f is a non-convex, continuous function. We will assume that f possesses one global minimizer and some regularity that can be exploited to compute some descent steps (or find local minimizers directly). To tackle this problem, we propose a hybrid approach that sits at the intersection between proximal algorithms [Parikh and Boyd, 2014] and basin hopping algorithms [Wales and Doye, 1997].

Standard first-order algorithms can only hope to obtain local solutions to Problem (1), which has prompted many to propose global optimization techniques, most of which are heuristic and do not possess strong convergence guarantees. Global optimization algorithms perform by combining exploration (through random perturbation of the current guesses) and exploitation steps (through function evaluation and/or local minimization) to reach a solution. The exploration requires a number of samples going to infinity to fit an underlying algorithm with increasing precision [Fornasier et al., 2024, Zhang et al., 2024], or a number of samples growing exponentially fast with the dimension to cover the space sufficiently enough [Hansen et al., 1992, Bouttier et al., 2020] to reach acceptable accuracy. This becomes rapidly cumbersome, even for problems of (nowadays) relatively small dimension (in the few hundreds) [Papenmeier et al., 2025]. On the other hand, the inexactness of the exploitation

0Acknowledgements. This work has been supported by the French government, through the 3IA Cote d’Azur Investments in the project managed by the National Research Agency (ANR) with the reference number ANR-23-IACL-0001, the ANR project PRC MAD ANR-24-CE23-1529 and the support of the “France 2030” funding ANR-23-PEIA-0004 (PDE-AI).

![image 1](<2026-lauga-proximal-basin-hopping-global_images/imageFile1.png>)

![image 2](<2026-lauga-proximal-basin-hopping-global_images/imageFile2.png>)

- Figure 1: Proximal Basin Hopping on the 2D-Rastrigin function at iteration 3 (left) and iteration 5 (right), where


convergence to the global minimizer, x∗ = (0,0), has occurred. From the current iterate, we draw several samples, that are then sent to their nearest achievable local minimizer, then weighted with respect to the achieved function value giving a new guess that is again sent to its nearest achievable local minimizer (if it is not there already).

steps through local minimization is difficult to account for in the theoretical analysis [György and Kocsis, 2011]. Hence, we propose a new framework opening the path to quantify the effect of sample size and inexactness on the convergence to the global minimizer.

Contributions. The method we propose, which we call Proximal Basin Hopping (PBH) is derived from an ideal operator proxγT

###### f(x), where Tf is a deterministic local solver, yielding for (almost) any starting point its achievable local minimizer, and prox denotes a proximal operation. This operator mimics Tf(proxf◦T

f

(x)) from which we gradually relax the required computations, in order to construct an algorithm using a finite amount of samples and possibly inexact local minimization (see Figure 1 for an illustration). We obtain thus four operators, from most ideal to most practical:

f

- 1. Ideal PBH: we make sense of the ≈ in Lemma 1,

Sfγ(x) := proxγT

f

f(x) ≈ Tf proxγ(f◦T

f)(x) .

- 2. Exact expectation PBH: the proximal operator is replaced by its zeroth-order approximation

Sfγ(x) ≈δ Tf

Ey∼N(x,δγId)[Tf(y)exp(−f (Tf(y))/δ)] Ey∼N(x,δγId)[exp(−f (Tf(y))/δ)]

.

- 3. Approximated expectation PBH: the zeroth-order approximation of the prox is estimated using N samples. For i = 1,...,N, yi ∼ N(x,δγId)

Sfγ(x) ≈Nδ Tf

N i=1 Tf(yi)exp(−f (Tf(yi))/δ)

N i=1 exp(−f (Tf(yi))/δ)

.

- 4. Approximated expectation & inexact local solving PBH:


 

 ,

N i=1 Tfε(yi)exp(−f Tfε(yi) /δ)

Sfγ(x) ≈Nδ,ε Tfε

N i=1 exp(−f Tfε(yi) /δ)

By allowing inexact computations of the proximal operator and of the local solver, we obtain a practical algorithm, that can recover the global minimizer. This relies on a structural assumption on f: the global minimizer is sufficiently different in function value from local minimizers.

We present extensive experiments on hard-to-optimize functions in moderate dimension (2 to 200), and apply our algorithm to the problem of fitting scaling laws on real data from [Shukor et al., 2025]. When the dimension is low (between 1 and 10) our algorithm is competitive with basin hopping, with respect to CPU time. It becomes conclusively better from moderate to high dimension.

Summary of theoretical results. Our goal is to show the convergence of our most practical algorithm. Such a result is obtained building up on the proofs of convergence of more ideal algorithms, by trying to emulate the same behavior: the second operator induces convergence because it approximates the first operator. The third operator induces convergence by emulating the second, and so on.

- 1. Ideal PBH: convergence holds through the properties of the potential Vx(M) := 1/(2γ)dist(x,Att(M))2+f(M)

and of its minimizers which are the elements of Sfγ(x): it is sufficiently well-behaved for finite time convergence to occur.

- 2. Exact expectation PBH: by proving convergence of the expectation onto the minimizers of Vx(·) when δ goes to 0, we can reuse the convergence arguments of the first algorithm to guarantee convergence to the global minimizer (but not in finite time).
- 3. Approximated expectation PBH: first by standard arguments, bringing N to infinity allows us to recover the setting of the second algorithm. In a following analysis, we show that with high probability, we only need a finite N to converge.
- 4. Approximated expectation & inexact local solving PBH: we highlight simple conditions on the inexactness that should hold to obtain convergence.


### 2 Structural assumptions on f and the local solver

In this section, we present in detail the structural assumptions we make on f and on the local solver Tf in order to guarantee convergence of our algorithms. We make assumptions on f that are either standard in optimization, or reasonable given our goal of reaching the global minimizer.

- Assumption 1. The function f : Rd → R ∪ {+∞} is proper, continuous, and coercive. We define the family of sets of local minimizers of f as

M := M connected :∃ V (open) ⊂ Rd, M ⊊ V, M = arg min

x∈V

f(x),∀x ∈ V \ M, f(x) > f(M) . (2)

We assume that every M ∈ M is Borel, bounded, and only finitely many elements of M intersect each compact subset of Rd.

This definition of M prevents redundancy, and ensures that the M are pairwise disjoints. Thus, M consists of possibly infinitely many disjoint, connected components of local minimizers M ∈ Rd, but finitely many on any compact set. In other words, f is "tame" (see App. C.1 for some examples). In the basin hopping literature, the standard hypothesis is for f to have finitely many of these components1. This case is easily covered by our framework. We take the liberty of writing f(M) < f(Q) for any component Q and M in M as f is constant on each connected component. We will denote the union of all elements of M as M∗ = M∈M M. We also need separation between the global minimizer and other local minima:

- Assumption 2. The function f has a unique global minimizer {x∗}. ∃ µ > 0 such that for all M ∈ M \ {x∗}, fmin + µ < f(M).


This assumption is relatively strong by preventing arbitrary accumulation of almost global local minimizers, but also in line with previous assumptions of the literature such as [Zhang et al., 2024, Assumption 3] which requires that no critical point x ̸= x∗ such that f(x) < fmin + µ exists.

1Finite does not mean small, the number of minimizers grows exponentially with the dimension for the Lennard-Jones cluster problem, introduced in the seminal paper of basin hopping [Wales and Doye, 1997].

- Assumption 3. The local solver Tf : Rd → Rd is measurable, single-valued, and outputs almost everywhere a local minimizer, i.e., Tf(x) ∈ M∗ a.e..

Tf maps any point to its unique achievable local minimizer. We define this achievability with the attractors of the local minimizers, which we denote by Att

(∀M ∈ M), Att(M) := y ∈ Rd, Tf(y) ∈ M . (3)

Obviously the geometry of Att depends a lot on the solver [Asenjo et al., 2013, Levy, 2018, 2026], we can operate under the assumption that these sets are open or closed but well-behaved2. Furthermore, under standard assumptions the attraction sets of critical points which are not local minimizers are of measure 0 [Lee et al., 2016]. As a consequence, the sets Att(M) form a measurable partition of Rd up to a null set (Lemma 6).

- Assumption 4. For every M ∈ M, the restriction of Tf to int(Att(M)) is continuous.

This assumption is verified for a gradient flow, or a finitely many gradient steps, if the gradient is continuous. See App. C.1 for a detailed discussion when Tf is built with gradient descent.

We make one last structural assumption on the behavior of M  → dist(x,Att(M)) for x ∈ Rd.

- Assumption 5. For every x ∈ Rd and γ > 0, the function


- 1

- 2γ


dist(x,Att(M))2 (4)

Vx : M ∈ M  → f(M) +

has a nonempty bounded set of minimizers on M. Furthermore,

dist(x,Att(M)◦) = dist(x,Att(M)) = dist(x,Att(M)). (5) We define:

Sfγ(x) := proxγT

Vx(M). (6)

f(x) := arg min

f

M∈M

This assumption is relatively strong (it implies well-posedness of Sfγ) but also reasonable: it holds for gradient flow. The coercivity of f yields the coercivity of Vx, and the assumption that f has finitely many components of local minimizers on any bounded set imply the boundedness of the arg min. The non-emptiness is always true if f is C1 and Tf consists of finitely many gradient steps as it is continuous, yielding closedness of Att(M). For a general gradient flow, Att(M) is open: take for instance f := ∥ · ∥2/2. Hence, this assumption. Finally, we define for x ∈ Rd,

M. (7)

αx := inf

Vx(M), M =

M∈M

M∈Sfγ(x)

### 3 Proposed method

We first consider our ideal operator. Its study is of great interest as it will provide the optimization problem which we hope our relaxed algorithm will emulate with the proper parameter δ. For any entry x ∈ Rd, the operator Sfγ identifies nearby local minimizers. All the proofs of this section are deferred to App. D.1. Under the assumption that x does not see Att(M) only through its boundary, we can prove that Sfγ(x) = Tf(proxf◦T

(x)), which is a helpful characterization in order to approximate Sfγ later.

f

- Lemma 1. Suppose that Assumptions 1, 3, and 5 hold. Set γ > 0. We have for all x ∈ Rd such that for every

- M ∈ Sfγ(x), projAtt(M)(x) ∩ Att(M) ̸= ∅, that Sfγ(x) = Tf(proxf◦T


f

(x)).

This operator Sfγ identifies the achievable minimizers to which x can be sent. The selection of the minimizer depends on the value of γ. Provided that γ is large enough, Sfγ recovers the global minimizer in one iteration.

- Lemma 2. Suppose that Assumptions 1, 2, and 5 hold. For all x ∈ Rd, there exists γx > 0 such that {x∗} ∈ Sfγ(x) for every γ ≥ γx.


2See [Levy, 2018, 2026] for a more exhaustive discussion on basins of attraction.

As we will see, this relationship between γ and the elements of Sfγ is predictive of the convergence of our more practical algorithms.

- Theorem 1. Convergence of ideal proximal basin hopping. Suppose that Assumptions 1, 2, and 5 hold. Let x0 ∈ Rd, γ0 > 0, η > 1, iterate for k = 0,1,...


f(z) (8)

xk+1 ∈ arg min

z∈Mxk

k+1)<f(xk)} (9) Then, {xk}k∈N converges to x∗ in finitely many iterations.

γk+1 = ηγk1{f(x

k+1)=f(xk)} + γk1{f(x

#### 3.1 Proximal basin hopping with exact expectation.

Equipped with the proximal interpretation of Sfγ, we introduce a relaxation by replacing the proximal operator by its zeroth-order approximation of parameter δ > 0 [Osher et al., 2023, Lauga and Vaiter, 2026], playing the role of

the temperature, for all x ∈ Rd

Ey∼N(x,δγId)[Tf(y)exp(−f (Tf(y))/δ)] Ey∼N(x,δγId)[exp(−f (Tf(y))/δ)]

Sfγ(x) ≈δ Tf

. (10)

With respect to the ideal operator, we want to understand how the approximated proximal operator actually converges to a solution of arg minVx when δ goes to 0. In the small δ regime, this approximation behaves closely to the ideal Sfγ, with the only caveat that if Sfγ is set-valued, the approximation sits near the convex hull of this set. As before, proofs are deferred to App. D.2.

We have this first result, derived from large deviation theory [den Hollander, 2000] and the properties of the Gaussian distribution. It is the foundation of our analysis. Lemma 3. Suppose that Assumptions 1, 5 hold. Let x ∈ Rd, γ > 0, δ > 0, and let Yδ ∼ N(x,δγId). Let M ∈ M. Then the family (Yδ)δ>0 satisfies, for each M,

- 1

- 2γ


δ log P(Yδ ∈ Att(M)) = −

lim

δ↓0

dist(x,Att(M))2.

One can see that weighting this probability by e−f(M)/δ will make the potential Vx appear on the right-hand side. Hence, we can show that the ratio of expectations in Eq. (10) converges to the set of minimizers of Vx when δ goes to 0. This is easy to obtain if the number of minimizing components is finite (App. D.2, Proposition 5). As we have infinite number of local-minimizer components, the crucial part is to make sure that almost all the mass is in a bounded set where the finite-number-of-components argument will help us complete the proof3. One can see that f cannot be too flat in all directions for this property to hold, otherwise it would allow some of the mass to escape to infinity. Coercivity is not enough to contain the mass, hence we make an additional growth assumption on f.

- Assumption 6. There exist C1,C2,C3 > 0 and 0 < α < β such that (∀z ∈ Rd), C1∥z∥α − C2 ≤ f(z) ≤ C3(1 + ∥z∥)β. (11)


First, we show that a measure induced by the exponential weights goes to 1 when δ ↓ 0 on bounded sets of M∗.

- Proposition 1. Suppose that Assumptions 1, 2, 3, 5, and 6 hold. Let x ∈ Rd, γ,δ > 0, and Yδ ∼ N(x,δγId). For any Borel B ∈ M∗, we define


νx,δ(B) νx,δ(M∗)

νx,δ(B) := E e−f(T

f(Yδ))/δ1{T

, (12)

f(Yδ)∈B} , µx,δ(B) :=

For any bounded set K ⊂ M∗, µx,δ(K) −−→

1.

δ↓0

3An easy way to make sure that all the mass is in a compact set is to truncate the attained minimizers if they have a norm above a threshold R, thus falling back on the finite minimizers case.

In addition, we can also ensure that the mass outside bounded sets does not escape too far (App. D.2, Proposition 6). Finally, we obtain our convergence result.

- Proposition 2. Suppose that Assumptions 1, 2, 3, 5, and 6 hold. Let x ∈ Rd, δ,γ > 0 and Yδ ∼ N(x,δγId). Denote by conv(Mx) the convex hull of Mx, the set of minimizers of Vx (Eq. 7). We have


E[Tf(Yδ)e−f(T

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ]

0 (13)

,conv(Mx) −−→

dist

δ↓0

In particular, if Mx = {mx,∗}, i.e., an isolated local minimizer, then, E[Tf(Yδ)e−f(T

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ] −−→

mx,∗. (14)

δ↓0

This result is almost equivalent to that of the finite case: the weighted barycenter onto which mδ converges is inside the convex hull (App. D.2, Proposition 5). In general, mδ does not need to lie inside the convex hull as some of the mass still lies outside the set of interest as long as δ > 0.

The convergence now relies on playing with the γ parameter to identify competing minimizers (Remark 1) and enable concentration on one element. If, in some iterations, several components are tied, it is not really a problem as long as it does not happen indefinitely. And we can guarantee that it does not by imposing a simple rule: if the new guess is of higher function value than the current one, we increase γ. However, with respect to the first ideal algorithm, we need γ to grow comparatively slower than δ, in order to avoid breaking our concentration result, hence we decrease δ at each iteration (while γ does not change if progress is made). Note that we do not reject equivalent samples in terms of function values for the sake of exploration.

- Algorithm 1 Exact expectation proximal basin hopping Require: x0 ∈ Rd, 1 < η1 < η2, γ0 > 0, δ0 > 0 (small)


- 1: for k = 0,1..., do
- 2: mδ

k,γk ← E[Tf(Y )e

−f(Tf(Y ))/δk]

E[e−f(Tf(Y))/δk] , Y ∼ N(xk,δkγk)

- 3: x+ ← Tf (mδ

k,γk)

- 4: if f(x+) > f(xk) then
- 5: xk+1 ← xk,γk+1 ← η1γk
- 6: else if f(x+) = f(xk) then
- 7: xk+1 ← x+, γk+1 ← η1γk
- 8: else
- 9: xk+1 ← x+,γk+1 ← γk
- 10: δk+1 ← δ

k η2

- 11: return xend


- Theorem 2. Convergence of exact expectation PBH. Suppose that Assumptions 1, 2, 3, 5, and 6 hold. Then, the iterates {xk}k∈N of Algorithm 1 converge to x∗ when k → +∞.
- 3.2 Proximal basin hopping with approximated expectation.


In practice, we estimate our operator Sfγ with a certain number of samples. It immediately begs the question, can this be sufficient to obtain convergence with reasonably high probability? The answer is yes, and we will show it

by studying the case where N actually goes to infinity to understand it. Again, we defer the proofs to App. D.3.

Sfγ(x) ≈Nδ Tf

N i=1 Tf(yi)exp(−f (Tf(yi))/δ)

N i=1 exp(−f (Tf(yi))/δ)

where yi ∼ N(x,δγId). (15)

Convergence when N → +∞. As for the exact case, we are first concerned with the well-posedness of the operator mN,δ,γ for all x ∈ Rd (line 2 Alg. 2). With standard arguments, we recover that mN,δ,γ → mδ,γ when

- N → +∞ (App. D.3, Lemma 12). The convergence of Tf(mN,δ,γ) to Tf(mδ,γ) is however not directly guaranteed as mδ,γ may lie on the boundary of some Att(M) (where we would lose local continuity of Tf), or may lie in the


null set, which consists of points from which Tf will not converge to a local minimizer. The first situation is covered by Lemma 13 and 14 (App. D.3). The null set is handled directly by our algorithm. With our built-in increase of γ, mδ,γ will fall under the conditions of Lemma 13. Indeed, for sufficiently large γ, and sufficiently small δ, mδ,γ is close to x∗ (Proposition 2). Hence increasing N sufficiently does the job.

- Algorithm 2 Approximated expectation proximal basin hopping Require: x0 ∈ Rd, 1 < η1 < η2, γ0 > 0, δ0 > 0 (small), C ≥ 1, N0 ∈ N \ {0},

- 1: for k = 0,1..., do
- 2: mN

k,δk,γk ←

Nk i=1 Tf(yi) exp(−f(Tf(yi))/δ)

Nk i=1 exp(−f(Tf(yi))/δ)

, y1,y2,...,yN

k ∼ N(xk,δkγkId)

- 3: x+ ← Tf (mN

k,δk,γk)

- 4: if f(x+) > f(xk) then
- 5: xk+1 ← xk, γk+1 ← η1γk
- 6: else if f(x+) = f(xk) then
- 7: xk+1 ← x+, γk+1 ← η1γk
- 8: else
- 9: xk+1 ← x+, γk+1 ← γk
- 10: δk+1 ← δ

k

η2, Nk+1 ← C × Nk

- 11: return xend


- Theorem 3. Convergence of approximate expectation PBH (N → +∞). Suppose that Assumptions 1, 2,

3, 4, 5, and 6 hold. The iterates {xk}k∈N of Algorithm 2 (i.e., C > 1) converge to x∗ when k → +∞.

Convergence when N < +∞. We now address the convergence of our algorithm when the number of samples remains finite. By quantifying that for N large enough ∥mN,δ,γ − mδ,γ∥ is small with high probability, we can use the arguments of the proof of Theorem 3 to recover the convergence.

Proposition 3. Suppose that Assumptions 1, 2, 3, 4, 5, and 6 hold. Let x ∈ Rd, γ,δ > 0. For any ε > 0, if N ∈ N \ {0} is large enough there exist α(ε) > 0, such that for N i.i.d. samples yi drawn from Yδ ∼ N(x,δγId),

P(∥mN,δ,γ − mδ,γ∥ ≤ ε) ≥ 1 −

α(ε) N

. (16) In fact, the previous result holds for all N, but is vacuous for N too small. It also holds for fixed δ and γ so we

need to be careful in bringing δ to 0 too fast for theoretical and practical reasons.

- Theorem 4. Convergence of approximate expectation PBH (N < +∞). Suppose that Assumptions 1, 2,




- 3, 4, 5, and 6 hold. Then, the iterates {xk}k∈N of Algorithm 2 with finite N (i.e., C = 1) converge to x∗ when k → +∞ with high probability if N is sufficiently large.


The required N is path-dependent, but does not need to hold for all the iterates, only for those that have an underlying mδ,γ able to send them to x∗. Practical considerations are discussed in App. B, notably the interplay between Proposition 3 and the values of δ and γ. Remark that the local minimizations of the yi’s can be parallelized.

#### 3.3 Proximal basin hopping with approximated expectation and local minimization.

Now, if we also assume that we cannot do complete local minimization but only obtain approximate local solutions, then we have a third level of approximations in our algorithm.

 , where yi ∼ N(x,δγId) (17)

 

N i=1 Tfε(yi)exp −f Tfε(yi) /δ

Sfγ(x) ≈Nδ,ε Tfε

N i=1 exp −f Tfε(yi) /δ

where for all x ∈ Rd, f(Tfε(x)) ≤ f(Tf(x)) + ε, and ∥Tfε(x) − Tf(x)∥ ≤ r(ε) for some ε ≥ 0 and function r : R+ → R+, such that r(0) := 0. If Tf := Id we recover the zeroth-order proximal algorithm, which converges

provided that N → +∞. A first observation is that to obtain convergence we will need δε → 0 with the iterations

as: exp(−f(Tfε(x))/δ) ≥ exp(−f(Tf(x))/δ)exp −δε . The right-hand side exponential is approximately the size of the perturbation on the weights. A second observation is that we also need ∥Tfε(x)−Tf(x)∥ to go to 0 uniformly for all x w.r.t. ε; otherwise the weighted average would not behave as mN,δ,γ, let alone for the refined guess.

### 4 Numerical experiments

In this section, we benchmark our algorithm against the zeroth-order proximal (ZOP) algorithm presented in [Zhang et al., 2024], and basin hopping (BH) algorithm [Wales and Doye, 1997]. We argue that these two algorithms are sufficient as benchmarks as other global optimization algorithms lack convergence guarantees, and because ZOP was shown to often be better than them in [Zhang et al., 2024] as was also shown for BH [Baioletti et al., 2024].

Comparison setup. Basin hopping is our Algorithm 2 with sample size of 1. The new guess, however, is accepted with probability proportional to exp(f(x)−fδ(Tf(yi))). Zeroth-order Prox is our Algorithm App. Exp. PBH with Tf = Id. As the three algorithms are not comparable w.r.t. to iteration count, we choose to report CPU time instead. We set parameters of all algorithms to the same value at initialization, and update with the rules of our algorithm, keeping the number of samples constant for PBH and ZOP. We did not investigate multisearch, and instead focused on convergence from one initialization. After the CPU-time budget has been spent, algorithms are stopped.

Set of problems. We propose to test our algorithm on various problems, with different complexities.

Hard synthetic functions. We test our algorithm against the d-dimensional Rastrigin, and d-dimensional Griewank functions, both satisfying our growth assumption. The global minimizer is at 0 for all d, with f(0) = 0. Rastrigin displays a much higher number of local minimizers than the Griewank function. We optimized these two functions with dimensions ranging from 2 to 200. The local solver uses gradient descent.

Lennard–Jones cluster. Let x1,...,xD ∈ R3 denote the positions of D ≥ 2 atoms. The Lennard–Jones energy is defined by

2 ∥xi − xj∥6

1 ∥xi − xj∥12

−

LJ(x1,...,xD) :=

.

1≤i<j≤D

The associated global optimization problem is of dimension d := 3D. The energy depends only on pairwise distances, and is therefore invariant under translations, rotations, and permutations. We optimized this function for 3 to 50 atoms. The local solver uses LBFGS steps.

Fitting scaling laws. Fitting scaling laws is an important problem in deep learning to predict model performance as a function of model size K and the number of tokens D. In particular, the choice of dataset mixtures is of crucial importance. To derive a good scaling law, the authors of [Shukor et al., 2025] collected training runs with different domain weights h (datasets), model sizes K, and token budgets D, and recorded the resulting loss on the target domain. Three scaling law models were tested in [Shukor et al., 2025] to understand optimal data mixtures [Shukor et al., 2025, Section 2.2]. The optimal parameters are estimated by minimizing a Huber objective over p observations. Finally, evaluation is performed on held-out runs with unseen triples (K,D,h) by comparing predicted and observed losses. The local solver uses LBFGS steps. The code for computing, fitting, and evaluating the scaling laws is reused from https://github.com/apple/ml-scalefit.

Numerical results. All the results displayed in this section are computed using 8 CPUs. We report final values, and not best achieved values, to highlight convergence capabilities and robustness. For the synthetic functions, we can see that the performance gap increases between PBH and BH when the dimension increases on the Rastrigin function, and stays consistent on the simpler Griewank function. ZOP did not converge on either functions: our hypothesis is that the number of samples needs to increase as δ decreases [Zhang et al., 2024, Section 5.2] in a much more constrained way than PBH. In our experiments, we saw that what matters at initialization is the scaling δγ: reducing δ at initialization would target smaller function values, but at the cost of exploration, thus γ should be increased accordingly. In this constrained budget setting, it appears that allocating more time to the exploration is not always useful: it is better to do more iterations with fewer samples. We display the results for the additive scaling law, for the three large deep learning models tested in [Shukor et al., 2025]: large language model (LLM), native multi-modal model (NMM), and large vision model (LVM). We report the results for the additive scaling law, that yielded the best test error. For almost all problems PBH with N = 5 is better than

![image 3](<2026-lauga-proximal-basin-hopping-global_images/imageFile3.png>)

![image 4](<2026-lauga-proximal-basin-hopping-global_images/imageFile4.png>)

![image 5](<2026-lauga-proximal-basin-hopping-global_images/imageFile5.png>)

- Figure 2: Comparison of BH (orange), PBH (blue), and ZOP (green) on (left) Rastrigin, (middle) Griewank, and (right) Lennard–Jones: the ranking between algorithms is plotted (1 is best). N = 10 × d, 10 local steps, CPU time = 2 × d. When it does not appear, ZOP diverged. We set γ = 5 and δ = 0.5 at initialization. Rastrigin experiment ran in 18h, with 8 CPUs and 2GB of memory.


ZOP or BH (Table 1). Increasing the number of LBFGS steps did not yield better results (for PBH and BH), as increasing the number of samples (keeping CPU number fixed).

|Family Domain<br><br>|PBH (N=5) PBH (N=10) PBH (N=15)<br><br>|ZOP (N=5) BH|
|---|---|---|
|LLM (d = 19)<br><br>arxiv book c4 commoncrawl github stackexchange wikipedia|7.244 ± 4.369 6.848 ± 4.795 7.336 ± 5.859<br><br>3.671 ± 2.804 4.136 ± 2.778 3.752 ± 3.382<br><br>4.105 ± 3.225 4.528 ± 3.622 4.168 ± 3.460<br><br><br>3.964 ± 2.848 5.172 ± 3.235 4.009 ± 3.615<br><br>8.597 ± 7.418 9.899 ± 7.707 8.961 ± 8.241<br><br><br>6.109 ± 3.795 7.024 ± 4.270 6.374 ± 5.469 8.540 ± 5.088 9.484 ± 5.011 8.554 ± 5.340<br><br>|7.431 ± 7.533 10.037 ± 5.472<br><br>6.158 ± 6.523 4.915 ± 3.298<br>7.061 ± 6.521 6.977 ± 4.146 5.638 ± 6.520 6.843 ± 3.820<br><br><br>11.131 ± 9.351 13.191 ± 8.458 7.651 ± 6.644 8.640 ± 6.598 10.416 ± 6.524 13.898 ± 5.064|
|LVM (d = 13)<br><br>alttext<br><br>highquality1<br><br>highquality2 synthetic<br><br><br>|3.083 ± 3.745 6.037 ± 3.585 4.896 ± 3.674 5.753 ± 3.368 7.636 ± 3.903 6.474 ± 3.091 3.978 ± 2.948 8.189 ± 7.543 4.681 ± 7.894 11.384 ± 12.289 16.939 ± 13.689 11.302 ± 11.621<br><br>|6.354 ± 4.648 6.452 ± 4.459<br><br>14.093 ± 6.332 5.494 ± 3.799 14.201 ± 12.136 5.446 ± 4.691 24.611 ± 15.638 14.320 ± 7.138|
|NMM (d = 11)<br><br>captions interleaved text|3.725 ± 3.209 4.526 ± 3.400 4.074 ± 3.891 2.854 ± 1.329 3.299 ± 1.318 2.693 ± 1.470 2.387 ± 1.185 3.169 ± 1.320 2.341 ± 1.313<br><br>|8.698 ± 7.172 5.741 ± 4.222 6.176 ± 2.263 5.618 ± 2.622 4.500 ± 1.894 7.332 ± 3.689|


Table 1: Test MRE = |predictionobservation−observation| (%) for fitting additive scaling law. (lbfgs steps=5, CPU time=300s). We set γ = 10 and δ = 10−3 at initialization. Results averaged over three seeds, we report the standard deviation.

On average, PBH yields better test error than other algorithms. The standard deviation is also indicative of the best possible value reachable.

### 5 Conclusion, limitations and broader impact

Conclusion. In this paper, we present a new theoretical framework, Proximal Basin Hopping, from which we construct a practical algorithm outperforming state-of-the-art methods on various problems.

Limitations. With respect to the present convergence analysis, and the subsequent algorithm, a question can be raised about the fact that we aggregate points, instead of simply taking the best point every time. In this setting, we would lose the proximal interpretation which is vital for convergence to the global minimizer through the parameter γ, but the practical results may be better. It has been shown for the basin hopping algorithm that in some cases, better-tailored perturbation could improve optimization [Englander and Englander, 2014]. Here, if we steer away from a Gaussian distribution for the stochastic exploration, we also steer away from the proximal interpretation and the convergence analysis of our algorithm. However, a variable metric [Chouzenoux et al., 2014] is possible by using y ∼ N(xk,δγΣ) instead of y ∼ N(xk,δγId). It remains to choose Σ properly. Also, the impact of the inexactness of the local minimization should be investigated on a per-solver basis. A first step should be to investigate it for gradient flow. Significant work is required as the geometry of attraction basins should be described in far more detail than what we used here. Finally, if letting the number of samples be fixed

simplifies greatly the computations, it could be interesting to adapt the number of samples on the fly (notably with Proposition 3), to temporarily escape some traps, or reduce the computational load if progress continues.

Broader impact. The proposed method may help reduce the number of searches required to obtain global minimizer, and reduce the overall computational load.

### References

J. A. S. Alvarez and P. Calaminici. A review of global optimization methods for molecular structures: Algorithms, applications and perspectives. Journal of Computational Chemistry, 46(28):e70243, 2025.

J. S. Arora, O. A. Elwakeil, A. I. Chahande, and C. C. Hsieh. Global optimization methods for engineering applications: a review. Structural optimization, 9(3):137–159, 1995.

- D. Asenjo, J. D. Stevenson, D. J. Wales, and D. Frenkel. Visualizing basins of attraction for different minimization algorithms. The Journal of Physical Chemistry B, 117(42):12717–12723, 2013.

M. Audin, M. Damian, and E. Erné. Morse theory and Floer homology, volume 2. Springer, 2014. W. Azizian, F. Iutzeler, J. Malick, and P. Mertikopoulos. What is the long-run distribution of stochastic gradient

descent? a large deviations analysis. In ICML 2024-41st International Conference on Machine Learning, pages 1–70, 2024.

W. Azizian, F. Iutzeler, J. Malick, and P. Mertikopoulos. The global convergence time of stochastic gradient descent in non-convex landscapes: Sharp estimates via large deviations. In International Conference on Machine Learning, pages 1982–2044. PMLR, 2025.

M. Baioletti, V. Santucci, and M. Tomassini. A performance analysis of basin hopping compared to established metaheuristics for global optimization. Journal of Global Optimization, 89(3):803–832, 2024.

C. Bouttier, T. Cesari, M. Ducoffe, and S. Gerchinovitz. Regret analysis of the Piyavskii-Shubert algorithm for global Lipschitz optimization. arXiv preprint arXiv:2002.02390, 2020.

- E. Chouzenoux, J.-C. Pesquet, and A. Repetti. Variable metric forward–backward algorithm for minimizing the sum of a differentiable function and a convex function. Journal of Optimization Theory and Applications, 162

(1):107–132, 2014. P. L. Combettes and V. R. Wajs. Signal recovery by proximal forward-backward splitting. Multiscale modeling & simulation, 4(4):1168–1200, 2005.

- M. Coste. An introduction to o-minimal geometry. 1999.

- B. de Souza. Goat: A global optimization algorithm for molecules and atomic clusters. Angewandte Chemie International Edition, 64(18):e202500393, 2025.


F. den Hollander. Large Deviations. American Mathematical Society, 2000.

- N. Di, E. C. Chi, and S. W. Fung. A monte carlo approach for nonsmooth convex optimization via proximal splitting algorithms. arXiv preprint arXiv:2509.07914, 2025.




A. C. Englander, J. A. Englander, and M. J. Carter. Hopping with an adaptive hop probability distribution. In Astrodynamics Specialist Meeting, 2020.

J. A. Englander and A. C. Englander. Tuning monotonic basin hopping: improving the efficiency of stochastic search as applied to low-thrust trajectory optimization. In International Symposium on Space Flight Dynamics 2014, number GSFC-E-DAA-TN14154, 2014.

J. F. Fernando. On the set of local extrema of a subanalytic function. Collectanea mathematica, 71(1):1–24, 2020. M. Fornasier, T. Klock, and K. Riedl. Consensus-based optimization methods converge globally. SIAM Journal on

Optimization, 34(3):2973–3004, 2024.

###### I. Goodfellow, Y. Bengio, A. Courville, and Y. Bengio. Deep learning, volume 1. MIT press Cambridge, 2016.

M. Goodridge, J. Moriarty, J. Vogrinc, and A. Zocca. Hopping between distant basins. Journal of Global Optimization, 84(2):465–489, 2022.

A. Grosso, M. Locatelli, and F. Schoen. A population-based approach for hard global optimization problems based on dissimilarity measures. Mathematical Programming, 110(2):373–404, 2007.

- A. György and L. Kocsis. Efficient multi-start strategies for local search algorithms. Journal of Artificial Intelligence Research, 41:407–444, 2011.
- B. Hajek. Cooling schedules for optimal annealing. Mathematics of operations research, 13(2):311–329, 1988.

- P. Hansen, B. Jaumard, and S.-H. Lu. Global optimization of univariate Lipschitz functions: I. Survey and properties. Mathematical programming, 55(1):251–272, 1992.

C. M. Kellett. A compendium of comparison function results. Mathematics of Control, Signals, and Systems, 26

(3):339–374, 2014. J. Kennedy and R. Eberhart. Particle swarm optimization. In Proceedings of ICNN’95-international conference on

neural networks, volume 4, pages 1942–1948. ieee, 1995. E. Kosygina and T. Mountford. Introductory examples and definitions. Cramér’s theorem, 2018. Lecture notes. A. Lambora, K. Gupta, and K. Chopra. Genetic algorithm-a literature review. In 2019 international conference

on machine learning, big data, cloud and parallel computing (COMITCon), pages 380–384. IEEE, 2019. G. Lauga and S. Vaiter. Characterizations of inexact proximal operators. working paper or preprint, January

2026. URL https://hal.science/hal-05449026. J. D. Lee, M. Simchowitz, M. I. Jordan, and B. Recht. Gradient descent only converges to minimizers. In Conference on learning theory, pages 1246–1257. PMLR, 2016. A. B. Levy. Attraction in numerical minimization: iteration mappings, attractors, and basins of attraction. Springer, 2018. A. B. Levy. Analyzing basins of attraction in numerical minimization. Set-Valued and Variational Analysis, 34(1): 6, 2026.

- M. Locatelli and F. Schoen. (global) optimization: historical notes and recent developments. EURO Journal on Computational Optimization, 9:100012, 2021.

D. Morales, P. Pérez-Aros, and E. Vilches. Convergence rates for stochastic proximal and projection estimators. arXiv preprint arXiv:2602.06750, 2026.

G. Ochoa, S. Verel, F. Daolio, and M. Tomassini. Local optima networks: A new model of combinatorial fitness landscapes. In Recent advances in the theory and application of fitness landscapes, pages 233–262. Springer, 2014.

S. Osher, H. Heaton, and S. W. Fung. A hamilton–jacobi-based proximal operator. Proceedings of the National Academy of Sciences, 120(14), 2023.

L. Papenmeier, M. Poloczek, and L. Nardi. Understanding high-dimensional bayesian optimization. In Forty-Second International Conference on Machine Learning, 2025.

- N. Parikh and S. Boyd. Proximal algorithms. Foundations and Trends in optimization, 1(3):127–239, 2014.


M. C. Prentiss, D. J. Wales, and P. G. Wolynes. Protein structure prediction using basin-hopping. The Journal of chemical physics, 128(22), 2008.

- Q. Rebjock and N. Boumal. Fast convergence to non-isolated minima: four equivalent conditions for c2 functions. Mathematical Programming, 213(1):151–199, 2025.
- R. T. Rockafellar and R. J.-B. Wets. Variational analysis, volume 317. Springer Science & Business Media, 2009.




- C. Rohilla Shalizi. General theory of large deviations. Lecture notes, 36-754 Statistical Machine Learning, Carnegie Mellon University, 2006. URL https://www.stat.cmu.edu/~cshalizi/754/2006/notes/lecture-30.pdf. Chapter 30.

M. Shukor, L. Béthune, D. Busbridge, D. Grangier, E. Fini, A. El-Nouby, and P. Ablin. Scaling laws for optimal data mixtures. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025.

- Y. Sun, Á. Baricz, and S. Zhou. On the monotonicity, log-concavity, and tight bounds of the generalized marcum and nuttall q-functions. IEEE Transactions on Information Theory, 56(3):1166–1186, 2010.

M. Tomassini. A local optima network view of real function fitness landscapes. Entropy, 24(5):703, 2022. D. J. Wales. Energy landscapes: some new horizons. Current Opinion in Structural Biology, 20(1):3–10, 2010. D. J. Wales and J. P. K. Doye. Global optimization by basin-hopping and the lowest energy structures of

lennard-jones clusters containing up to 110 atoms. The Journal of Physical Chemistry A, 101(28):5111–5116, 1997.

- Z. B. Zabinsky. Random search algorithms. Department of Industrial and Systems Engineering, University of Washington, USA, 34, 2009.




M. Zhang, F. Han, Y. T. Chow, S. Osher, and H. Schaeffer. Inexact proximal point algorithms for zeroth-order global optimization. arXiv preprint arXiv:2412.11485, 2024.

### A Related works

Global optimization and zeroth-order methods. Global optimization has a long history, with most used methods being derived from some metaheuristics [Locatelli and Schoen, 2021]. A large part of this literature can be viewed as zeroth-order optimization, as the algorithms only query function values. The simplest one being pure random search, which samples candidate points and keeps the best value found [Zabinsky, 2009]. More structured deterministic zeroth-order methods include Lipschitz global optimization, but are typically limited by dimension [Hansen et al., 1992, Bouttier et al., 2020]. Multi-start local search is another way to combine global exploration and local descent, and its efficiency depends obviously on how starting points are allocated [György and Kocsis, 2011].

Genetic and evolutionary algorithms maintain and transform a population of candidate solutions through selection and variation mechanisms [Lambora et al., 2019]. Simulated annealing instead constructs a stochastic process whose ability to escape local minima is controlled by a temperature parameter; classical convergence guarantees require sufficiently slow cooling schedules [Hajek, 1988] if the number of states to investigate is finite. Particle swarm optimization updates a population of particles using both individual and collective best positions [Kennedy and Eberhart, 1995]. Consensus-based optimization is another population-based approach in which particles concentrate around weighted averages favoring low objective values; it is a more theoretically principled way of doing particles optimization, as global convergence under suitable assumptions was derived [Fornasier et al., 2024]. Bayesian optimization and related surrogate-based methods are highly effective in low to moderate dimension, but their behavior in high dimension remains delicate [Papenmeier et al., 2025].

Energy landscapes, basins, and local optima networks. A complementary line of work, that has attracted most of its attention from chemistry fields, studies the organization of nonconvex landscapes through their local minima and basins of attraction. Local optima networks encode local minimizers as nodes and transitions between them as edges, giving a graph representation of the landscape [Ochoa et al., 2014, Tomassini, 2022]. Such tools have been used to visualize and quantify funneling landscapes, in which local descent tends to guide configurations toward increasingly low-energy regions [Wales, 2010]. The structure of attraction basins evidently depends on the local solver: different minimization algorithms may induce different basins on the same objective [Asenjo et al.,

- 2013]. This viewpoint is closely related to the study of iteration maps, attractors, and basins of attraction in numerical minimization [Levy, 2018, 2026].


Basin-hopping algorithms. Basin hopping was introduced for the global optimization of atomic cluster energies, in particular Lennard–Jones clusters [Wales and Doye, 1997]. The central idea is to compose random perturbations with local minimization, thereby transforming the original objective into an energy landscape over local minima. This transformation has proved especially effective in molecular and cluster optimization [Prentiss et al., 2008, Alvarez and Calaminici, 2025, de Souza, 2025]. Despite its practical success, this scheme has limited general convergence theory and is typically analyzed or tuned empirically.

Several variants of basin hopping have since been created, due to its success. Monotonic basin hopping accepts only moves that improve the objective and has been tuned for trajectory optimization problems [Englander and Englander, 2014]. Adaptive hopping strategies modify the perturbation distribution to improve transitions between promising regions [Englander et al., 2020]. Population-based basin hopping maintains several candidate solutions and uses dissimilarity or diversity mechanisms to explore multiple regions of the landscape [Grosso et al., 2007]. Recent comparisons show that basin hopping is competitive with established metaheuristics on global optimization benchmarks, but its performance remains problem dependent [Baioletti et al., 2024]. There is also theoretical work studying the difficulty of moving between distant basins [Goodridge et al., 2022].

Proximal algorithms and stochastic proximal approximations. Proximal algorithms are a central tool in convex and variational optimization [Combettes and Wajs, 2005, Parikh and Boyd, 2014, Rockafellar and Wets, 2009]. In convex settings, inexact proximal splitting methods remain convergent when the errors in the proximal evaluations are controlled, for instance by summability assumptions [Combettes and Wajs, 2005]. Recent work also studies Monte Carlo approximations of proximal steps for nonsmooth convex optimization [Di et al., 2025].

- A Hamilton–Jacobi-based zeroth-order approximation of the proximal operator was proposed in [Osher et al.,


2023]:

Ey∼N(x,δλI) [y exp(−f(y)/δ)] Ey∼N(x,δλI) [exp(−f(y)/δ)]

proxδλf(x) =

proxδλf(x). (18)

, proxλf(x) = lim δ↓0

Rates for such stochastic proximal and projection estimators have been investigated in [Lauga and Vaiter, 2026, Morales et al., 2026]. This approximation has also been used for zeroth-order global optimization in [Zhang et al., 2024], where an adaptive proximal-point scheme encourages exploration near non-global critical points. Their implementation estimates the expectation either by tensor-train methods or by Monte Carlo integration. The convergence argument relies on decreasing the smoothing parameter and increasing the number of samples sufficiently fast so that the accumulated proximal error remains controlled, for example through summability conditions [Zhang et al., 2024, Corollary 4].

### B Details about our algorithm

In practice. Instead of decreasing δ at each iteration, we adjust it on the fly: if the minimum value of f identified by the sampling mechanism has not lead to concentration on this minimum value, we decrease δ accordingly. This small tweak is a practical tradeoff given that we are using small sample sizes.

Furthermore, for numerical stability, the weighted mean is computed by substracting the maximum weight value, before computing the ratio. It is also done for the ZOP algorithm (for the same reasons).

- Proposition 4. Suppose that Assumptions 1, 2, and 3 hold. Let N ∈ N \ {0}, let {mi}1≤i≤N ∈ M∗, and assume


that there exists 1 ≤ ix ≤ N such that f(mi

)◦. If δ is small enough, i.e., such that

) < f(mi) for all i ̸= ix, with mi

x ∈ B(mi,x,ri,x) ⊆ Att(mi

x

x

ri

e−∆/δ ≤

, (19)

x

(N − 1)max1≤i≤N ∥mi − mi

x∥

where ∆ = min1≤i≤N,i̸=i

), then

f(mi) − f(mi

x

x

N i=1 mi exp(−f (mi)/δ)

. (20)

= mi

Tf

N i=1 exp(−f (mi)/δ)

x

Proof. We note

N i=1 mi exp(−f (mi)/δ)

exp(−f (mi)/δ) N i=1 exp(−f (mi)/δ)

and λi =

mδ :=

N i=1 exp(−f (mi)/δ)

We need to show that mδ ∈ Att(mi

> 0 such that B(mi

) to conclude. mi

being in the interior of Att(mi

) there exist ri

x

x

x

x

). By taking this radius as large as possible, we upper bound the value of δ required. We want:

) ⊂ Att(mi

,ri

x

x

x

N

x ≤ ri

x ⇔

λimi − mi

i=1

N

λi(mi − mi

) ≤ ri

x

x

i=1,i̸=ix

Now,

N

N

λi(mi − mi

) ≤

λi∥mi − mi

x∥ ≤ (1 − λi

∥mi − mi

x∥.

) max

x

x

1≤i≤N

i=1,i̸=ix

i=1,i̸=ix

∆ is stricly greater than 0 by assumption. We have

1 1 + i̸=i

λi

=

,

x

exp(−(f (mi) − f(mi

))/δ)

x

x

hence,

1 − λi

x ≤

exp(−(f (mi) − f(mi

))/δ) ≤ (N − 1)exp(−∆/δ).

x

i̸=ix

Thus for concentration to occur, we need δ small enough so that e−∆/δ ≤

ri

x

.

(N − 1)max1≤i≤N ∥mi − mi

x∥

| |
|---|


reduces the mass on "bad" local minimizers while increasing the mass on the correct local minimizer. An other aspect that is not directly covered by Proposition

###### This threshold on δ is a worst case, a multiplicity of mi

x

- 3 is the dependence on the dimension for α(ε). We can at least quantify the probability of eating the basin of attraction for one sample. It is reasonable to assume that we can fit a ball of non zero radius in each basin of attraction and we can estimate the probability of one sample being in this ball explicitly, and subsequently of at least one among N. We plot in Figure 3 an estimation of these probabilities with respect to the dimension and the number of samples.


- Lemma 4. Let x ∈ Rd, σ > 0 and Yσ ∼ N(x,σ2Id). Let r > 0. We have

P(Yσ ∈ B(0,r)) = CDFX′

d(∥x∥2/σ2)(

r2 σ2

). (21) Moreover to have a probability 0 < α < 1 of one sample hitting this ball, we need

N ≥

log(1 − α) log(1 − P(Yσ ∈ B(0,r)))

. (22)

Proof. We have

P(Yσ ∈ B(0,r)) = P(∥Yσ∥ ≤ r) = P(∥Yσ∥2 ≤ r2) = P(∥Yσ∥2/σ2 ≤ r2/σ2)

Now, ∥Yσ∥2/σ2 is the sum of d independent standard normal distributions, with non zero means. Hence, it is a non central chi-square distribution:

∥Yσ∥2 σ2 ∼ Xd′(λ), where λ =

d

i=1

µ2i σ2

. (23)

Therefore,

P(Yσ ∈ B(0,r)) = CDFX′

d(λ)(

r2 σ2

).

Setting α as the probability of one sample to be in this ball when drawing (yi)1≤i≤N samples of Yσ, it is defined as: P(∃ 1 ≤ i ≤ N,yi ∈ B(0,r)) = 1 − (1 − P(Yσ ∈ B(0,r)))N = α, which yields after a few rewriting:

N ≥

log(1 − α) log(1 − P(Yσ ∈ B(0,r)))

. (24)

| |
|---|


For instance, if P(Yσ ∈ B(0,r)) is small and α = 0.95 we obtain that N needs to be of the order N ≳

3 P(Yσ ∈ B(0,r))

. (25)

Therefore we can guarantee with high probability that we can identify basin of attractions of better local minimizers (from a local minimizer), provided that the number of samples is high enough. One should also be wary of the value of σ not to spread our samples to much. In order to quantify that more precisely we can use the fact that the cumulative distribution function of the non-central chi-squared distribution can be expressed with the generalized Marcum Q-function [Sun et al., 2010].

- Lemma 5. Let x ∈ Rd \ {0}, σ > 0 and Yσ ∼ N(x,σ2Id). Let r > 0. The probability P(Yσ ∈ B(0,r)) is, with the other parameters fixed, strictly decreasing in the dimension d and the norm ∥x∥, and stricly increasing in the ratio r/σ. On the other hand, with other parameters fixed and ∥x∥ > r,


P(Yσ ∈ B(0,r)) = 0, (26) implying that there exists σ∗ such that

P(Yσ ∈ B(0,r)) = 0 and lim

lim

σ→+∞

σ→0

###### ∈ B(0,r)) ≥ P(Yσ ∈ B(0,r)) (27)

(∀σ > 0), P(Yσ

∗

![image 6](<2026-lauga-proximal-basin-hopping-global_images/imageFile6.png>)

![image 7](<2026-lauga-proximal-basin-hopping-global_images/imageFile7.png>)

Figure 3: Probability of being in a ball in the basin of x∗ and r2/σ2 = 1.

Proof. We have

r2 σ2

d(∥x∥2/σ2)(

CDFX′

) = 1 − Qd

2

∥x∥ σ

,

r σ

.

The first result follows from [Sun et al., 2010, Theorem 1(a)] as all parameters are strictly positive. The second one is immediate from the fact that ∥x∥ > r.

| |
|---|


### C Preliminary results and discussion of the assumptions

- C.1 Assumptions on f


Finitely many minimizing components in any compact set. As stated, f is tame, meaning for any compact set K

- 1. K is definable in some o-minimal structure over R, and f|K : K → R is definable: the set of local minima is a definable subset of Rd [Fernando, 2020, Lemma 1.7] and definable subset have finitely many connected components [Coste, 1999, Section 3.2].
- 2. K is semi-algebraic, and f|K is semi-algebraic: semi-algebraic function are definable [Fernando, 2020].
- 3. K is globally subanalytic, and f|K is globally subanalytic: same as above [Fernando, 2020]
- 4. f|K is a Morse function, i.e., it is C2 with only isolated nondegenerate critical points [Audin et al., 2014].
- 5. f|K is a Morse-Bott function, i.e., it is C2, and each connected component of minima is a critical submanifold [Rebjock and Boumal, 2025]. This is the case of the Rastrigin function.


Graph of local minimizers. Following the basin hopping literature [Hajek, 1988, Wales, 2010, Tomassini, 2022], and some other recent works [Azizian et al., 2025], in practice we somehow assume that local minimizers of f can be represented with a graph. This assumption is however not required to prove convergence. Here, the edges depend on the local solver Tf in the following sense: for any local minimizer P ∈ M, the distance from p to the attractor of a better local minimizer Q (in the sense that f(P) > f(Q)) is uniformly bounded for all P.

Assumption 7. For all P ∈ M \ {x∗}, there exists Q ∈ M such that

dist(x,Att(Q)) ≤ df < +∞ and f(P) > f(Q) (28)

sup

x∈P

Hence, we construct our graph with vertices as local minimizers (or connected components of local minimizers) and a directed edge between two vertices P and Q if dist(P,Att(Q)) ≤ df. The edge is undirected if also dist(Q,Att(P)) ≤ df. From this assumption, the global minimizer x∗ is reachable by "simply" jumping from one local minimizer to a better local minimizer. This assumption is implicitly made in basin hopping optimization so that random perturbations can reach the basin of a better local minimizer [Goodridge et al., 2022].

We can numerically compute an upper bound of df (Assumption 7) for the 1 − D Rastrigin function only has isolated local minimizers, and isolated local maximizers:

Ras(x) = x2 + 10(1 − cos(2πx)), (29) which are solutions of

x 10π

= −sin(2πx).

These solutions can be computed numerically and are approximately away from each other by a little less than 0.5, hence df = 12 is a valid upper bound in this case.

#### C.2 Properties of the solver

The definition of the solver in the main body of the paper contains only the relevant assumption to derive our analysis, we lay here a more detailed presentation of what these assumptions entail. Assume that f is C2-smooth (with Lipschitz continuous gradient). Let us define φ : [0,+∞),Rd  → Rd the gradient flow mapping any x ∈ Rd to a local minimizer of f:

φ(0,x) = x φ(t,x) = −∇f(φ(t,x))

(30) Define the critical components of f as:

critf := x ∈ Rd,0 = ∇f(x) (31)

and we assume it is composed of infinitely many connected components. Following this definition, we have for any component C ∈ critf that

Att(C) := x ∈ Rd, lim

dist(φ(t,x),C) = 0 . (32)

t→+∞

[Azizian et al., 2024, Lemma D.28] holds in our context and thus for any x ∈ Rd, there exists C ∈ critf such that lim

d(φ(t,x),C) = 0. (33)

t→+∞

The proof is immediate from [Azizian et al., 2024, Lemma D.28], as f is coercive and the components C are connected. The finiteness of the number of components is not important, their connectedness is. M is the set of asymptotically stable critical components [Azizian et al., 2024, Lemma D.29] (again the proof does not rely on finiteness of critical components), implying that for all M ∈ M, Att(M) is open. Under standard assumptions [Lee et al., 2016] any C ∈ critf \ M, Att(C) is of measure 0.

##### C.3 Some preliminary results related to the local minimizers We start this presentation by listing some important properties of the local minimizers and their attractor sets.

- Lemma 6. Suppose that Assumptions 1, 3, and 5 hold. The sets {Att(M)}M∈M form a measurable partition of Rd up to a null set.

Proof. First, the sets of attractors of critical points who are non local minimizers is of measure 0. Let us denote by N this set of points which are not attracted by a local minimizer through Tf. We have for all y ∈ Rd \ N, Tf(y) ∈ M∗ and more precisely, there exists a unique M ∈ M such that Tf(y) ∈ M as the M are pairwise disjoints. Hence, for any P,Q ∈ M, Att(P) ∩ Att(Q) = ∅, and

j

Att(Mj) = Tf−1(M∗) = Rd \ N. (34)

As Tf is measurable and every M is Borel by assumption, we get the desired result.

| |
|---|


- Lemma 7. Let x ∈ Rd. For every η > 0, there exists a finite subset Kη ⊂ M such that


Vx( M) + η. (35)

Vx(M) ≥ inf

inf

M∈M\Kη

M∈M

Proof. Since dist(x,Att(M))2 ≥ 0, one has

Vx(M) ≥ f(M), M ∈ M. Set

Vx(M). By coercivity of f, there exists Rη > 0 such that

αx := inf

M∈M

∥y∥ ≥ Rη =⇒ f(y) ≥ αx + η. Let

Kη := {M ∈ M : M ∩ B(0,Rη) ̸= ∅}.

Since B(0,Rη) is compact and only finitely many elements of M intersect a compact set, Kη is finite. Let M ∈ M \ Kη. Then M ∩ B(0,Rη) = ∅, so for every m ∈ M one has ∥m∥ > Rη. Hence f(M) = f(m) ≥ αx + η. Therefore Vx(M) ≥ f(M) ≥ αx + η. Taking the infimum over M ∈ M \ Kη gives

Vx(M) ≥ αx + η = inf

Vx( M) + η.

inf

M∈M\Kη

M∈M

| |
|---|


Any finite subset of M is automatically bounded by boundedness of every elements of M and they have a positive value gap with inf Vx. Fact 1. Let x ∈ Rd, αx := infM∈M Vx(M), ε > 0, and

M, and (Mx)ε = z ∈ Rd, dist(z,Mx) < ϵ .

Mx =

M∈Sfγ(x)

Let R > 0. On B(0,R) there exists a positive gap of Vx between M ∈ Sfγ(x) and every other M that intersects B(0,R), i.e., there exists cR,ε > 0 such that for every M in

Mx,R,ε := M ∈ M, M ∩ B(0,R) ̸= ∅, M ∩ ((Mx)ε)∁ ̸= ∅ , Vx(M) ≥ αx + cR,ϵ.

- Lemma 8. Suppose that Assumptions 1, 2, 3, and 5 hold. Let x ∈ Rd and δ,γ > 0. If one of the conditions below hold


- • There exist C1,C2,C3 > 0 and 0 < α < β such that (∀z ∈ Rd), C1∥z∥α − C2 ≤ f(z) ≤ C3(1 + ∥z∥)β. (36)
- • M has finitely many components.


Then, Tf : Rd → M∗ is integrable and square integrable against the Gaussian distribution, i.e.,

−1

2γδ∥y−x∥2dy < +∞, and

∥Tf(y)∥e

Rd

−1

2γδ∥y−x∥2dy < +∞ (37)

∥Tf(y)∥2e

Rd

Proof. Let us consider the second case first. Denote by J the number of components of M. Then M∗ = Jj=1 Mj. By assumption any M ∈ M is bounded. Thus there exists some R > 0 such that M∗ ⊂ B(0,R). Hence,

∥y−x∥2

∥y−x∥2

∥Tf(y)∥e−

e−

2δγ dy ≤ R

2δγ dy < +∞.

Rd

Rd

Now to the first case. We have for all z ∈ Rd, f(z) ≥ f(Tf(z)), therefore C1∥Tf(z)∥α − C2 ≤ f(Tf(z)) ≤ f(z) ≤ C3(1 + ∥z∥)β

and,

∥Tf(z)∥ ≤ C1−1/α C2 + C3(1 + ∥z∥β) 1/α . Hence,

∥y−x∥2

∥y−x∥2

C1−1/α C2 + C3(1 + ∥y∥β) 1/α e−

∥Tf(y)∥e−

2δγ dy < +∞. The square case follows immediately from the same arguments.

2δγ dy ≤

Rd

Rd

| |
|---|


Assumption 6 and the first condition in Lemma 8 imply that f has polynomially bounded growth. This is slightly stronger than coercivity and is akin to the notion of radially unbounded function in control theory4 [Kellett,

- 2014].


- Lemma 9. Suppose that Assumptions 1, 3, 5, and 6 hold. Let x ∈ Rd, Yδ ∼ N(x,γδId), q > 0 and r > 0. We have:


(r − ∥x∥2)+ 2γ

δ log E (1 + ∥Yδ∥q)1{∥Y

. (38)

δ∥>r} ≤ −

limsup

δ↓0

Proof. We have

∥y − x∥2 2γδ

1 (2πδγ)d/2 {∥y∥>r}

E (1 + ∥Yδ∥q)1{∥Y

(1 + ∥y∥q)exp −

δ∥>r} =

dy.

Fix R > r. Splitting the domain gives {∥y∥ > r} = {r < ∥y∥ ≤ R}∪{∥y∥ > R}, hence we can split the expectation in

Iδ(r) := E (1 + ∥Yδ∥q)1{∥Y

δ∥>r} = Iδ,1(r,R) + Iδ,2(R), where

1 (2πδγ)d/2 {r<∥y∥≤R}

∥y−x∥2

(1 + ∥y∥q)e−

Iδ,1(r,R) :=

2γδ dy

and

1 (2πδγ)d/2 {∥y∥>R}

∥y−x∥2

(1 + ∥y∥q)e−

2γδ dy.

Iδ,2(R) :=

On the bounded region {r < ∥y∥ ≤ R}, we have 1 + ∥y∥q ≤ 1 + Rq. Moreover, if ∥y∥ > r, then ∥y − x∥ ≥ ∥y∥ − ∥x∥ ≥ (r − ∥x∥)+. Therefore

(r − ∥x∥)2+ 2γδ

(1 + Rq)λd(B(0,R)) (2πδγ)d/2

Iδ,1(r,R) ≤

exp −

.

Since δ log(δ−d/2) → 0, it follows that

limsup

δ↓0

(r − ∥x∥)2+ 2γ

δ log Iδ,1(r,R) ≤ −

.

∥y−x∥2 2γδ

(R−∥x∥)2

∥y−x∥2

Now onto Iδ,2(R). Assume R > ∥x∥. For ∥y∥ > R, ∥y − x∥ ≥ R − ∥x∥, hence e−

≤ e−

4γδ e−

4γδ . Thus

1 (2πδγ)d/2 Rd

(R−∥x∥)2 4γδ

∥y−x∥2

Iδ,2(R) ≤ e−

(1 + ∥y∥q)e−

4γδ dy.

Using ∥y∥q ≤ max{1,2q−1}(1 + ∥y − x∥q + ∥x∥q), we obtain 1 + ∥y∥q ≤ C(1 + ∥y − x∥q) for some constant C > 0. Hence

1 (2πδγ)d/2 Rd

(R−∥x∥)2 4γδ

∥y−x∥2

Iδ,2(R) ≤ Ce−

(1 + ∥y − x∥q)e−

4γδ dy.

√

Making the change of variables z = (y−x)/

δ, we obtain that the righthandside integral is in O(δd/2)+O(δ(d+q)/2) hence bounded uniformly for δ ∈ (0,1]. Therefore there exists CR > 0 such that

(R−∥x∥)2

Iδ,2(R) ≤ CRe−

4γδ ,

###### 4In this setting, ψ is also required to be positive [Kellett, 2014, Section 2].

and thus

(R − ∥x∥)2 4γ

δ log Iδ,2(R) ≤ −

. Finally,

limsup

δ↓0

δ log Iδ(r) ≤ max limsup

limsup

δ log Iδ,2(R) . Hence

δ log Iδ,1(r,R), limsup

δ↓0

δ↓0

δ↓0

(r − ∥x∥)2+ 2γ

(R − ∥x∥)2 4γ

, −

δ log Iδ(r) ≤ max −

. Choosing R > r large enough so that

limsup

δ↓0

(r − ∥x∥)2+ 2γ

(R − ∥x∥)2 4γ

, we conclude that

>

(r − ∥x∥)2+ 2γ

δ log E (1 + ∥Yδ∥q)1{∥Y

δ∥>r} ≤ −

limsup

.

| |
|---|


δ↓0

Remark 1. Evolution of the set Mx with respect to γ. There exists approximately three regimes. When γ is small, Vx heavily penalizes distant local minimizers hence its arg min is more likely to contain one unique solution. Slowly increasing γ makes it more likely that several competitors M can arise. Then as γ increases more, Vx is more likely to select a unique better local minimizer.

The first regime is characterized in the next Lemma.

- Lemma 10. Suppose that Assumptions 1, 2, 3, 7, and 5 hold. Let x ∈ Rd, γ > 0, and P ∈ M the closest (w.r.t. to Att(P)) minimizing component. Denote by Q the closest (w.r.t. Att(Q)) better local minimizing component of P in the sense of Assumption 7. If:


dist(x,Att(Q))2 − dist(x,Att(P))2 2(f(P) − f(Q))

(39)

γ <

then,

Vx(M). (40)

P = arg min

M∈M

Proof. We have that for all M ∈ M \ {Q} such that dist(x,Att(M)) ≤ df then f(M) > f(Q). Furthermore, by Assumption 7, any better local minimizer in the vicinity of P has function value equal to that of Q in a radius df, hence we just need to make sure that Q does not belong in the arg min, giving immediately the positive upper bound on γ.

| |
|---|


These scenarios where we have a series of equally distant and of equal function values are not possible indefinitely, first because there is a unique global minimizer, and second because the function f is coercive so it needs to grow to infinity, thus contradicting the existence of these increasingly distant local minimizers of decreasing function values.

### D Proofs of Section 3: Proposed method

#### D.1 Proofs for ideal basin hopping

- Proof of Lemma 1 Proof. We have for all x ∈ Rd


and

- 1

- 2γ ∥y − x∥2 + f(T(y)),


proxγf◦T

(x) = arg min

f

y∈Rd

Sfγ(x) := arg min

M∈M

- 1

- 2γ


dist(x,Att(M))2 + f(M).

Looking more closely at the first optimization problem, we have min

- 1

- 2γ ∥y − x∥2 + f(T(y)) = min


- 1

- 2γ


dist(x,Att(M))2 + f(M).

y∈Rd

M∈M

Hence, if for every M ∈ Sfγ(x), projAtt(M)(x) ∩ Att(M) ̸= ∅, proxγf◦T

projAtt(M)(x),

(x) =

f

M∈arg minM∈M 21γ dist(x,Att(M))2+f(M)

where proj denotes the orthogonal projection. Thus, as Tf maps to M, we recover

- 1

- 2γ


dist(x,Att(M))2 + f(M).

Tf(proxγf◦T

(x)) = arg min

f

M∈M

| |
|---|


- Proof of Lemma 2 Proof. Let x ∈ Rd. We have that for all γ > 0.


Sfγ(x) = arg min

M∈M

Hence,

- 1

- 2γ


dist(x,Att(M))2 + f(M).

x∗ ∈ Sfγ(x) ⇔ ∀M ∈ M,

⇔ ∀M ∈ M,

- 1

- 2γ


- 1

- 2γ


dist(x,Att(x∗))2 + f(x∗) ≤

dist(x,Att(M))2 + f(M)

- 1

- 2µ


dist(x,Att(x∗))2 − dist(x,Att(M))2 ≤ γ,

where the last inequality was obtained using Assumption 2. The minimal required value of γ depends on the close and achievable minimizers. Indeed, all minimizing components such that dist(x,Att(x∗))2 − dist(x,Att(M))2 ≤ 0 yields no constraint on γ.

| |
|---|


###### Proof of Theorem 1.

Proof. First iterations are well defined as Sfγ is non-empty and bounded (Assumption 5, Lemma 1). Second, if for any K ∈ N, xK = x∗ then xk = x∗ for all k > K. Finally, by construction f(xk+1) ≤ f(xk), hence by coercivity of f (Assumption 1), the iterates are bounded. Denote by B0 this bounded set. We can guarantee that there exists only finitely many failed iterations (where f(x+) = f(xk)).

Indeed, by boundedness of the iterates, there exists df ≥ 0 such that for all k ∈ N, dist(xk,Att(x∗)) ≤ df. Let P ∈ M, such that P ∩ B0 ̸= ∅ and P ̸= {x∗}. We have for any x ∈ P, Vx(x∗) < Vx(P) if

dist(x,Att(x∗))2 2γ

+ fmin < f(P)

2 f

2 f

which happens if γ > d

2(f(P)−fmin). Thus, taking the infimum over all P not equal to {x∗}, we have γs ≥ d

2µ implies that for all x ∈ B0, x∗ ∈ Sγ

f (x). Let K ∈ N. For any γ > 0, γηK ≤ γs ⇔K log(η) ≤ log

s

γs γ

log (γs/γ) log(η) Therefore, after at most log(γ

⇔K ≤

s/γ) log(η)

failed iterations, x∗ belongs to Sfγ.

+

Now, by boundedness of the iterates, only finitely many M ∈ M can be visited. Hence, we conclude that convergence occurs in a finite number of iterations.

| |
|---|


- D.2 Proofs for exact expectation basin hopping


- Proof of Lemma 3.


Proof. By the small-noise Gaussian large deviation principle with speed δ−1, and rate function Ix(y) = 21γ∥y −x∥2, for every Borel set A ⊂ Rd [den Hollander, 2000], 5

δ log P(Yδ ∈ A) ≤ limsup

δ log P(Yδ ∈ A) ≤ − inf

− inf

Ix(y) ≤ liminf

Ix(y).

y∈A◦

δ↓0

y∈A

δ↓0

Applying this with A = Att(M) yields

− inf

y∈Att(M)◦

Which is equivalent to

- 1

- 2γ ∥y − x∥2 ≤ liminf


δ log P(Yδ ∈ Att(M))

δ↓0

- 1

- 2γ ∥y − x∥2.


δ log P(Yδ ∈ Att(M)) ≤ − inf

≤ limsup

δ↓0

y∈Att(M)

- 1

- 2γ


dist(x,Att(M)◦)2 ≤ liminf

δ log P(Yδ ∈ Att(M))

−

δ↓0

- 1

- 2γ


dist(x,Att(M))2.

δ log P(Yδ ∈ Att(M)) ≤ −

≤ limsup

δ↓0

By the regularity assumption the lower and upper bounds coincide, and hence

- 1

- 2γ


dist(x,Att(M))2.

δ log P(Yδ ∈ Att(M)) = −

lim

δ↓0

This proves the first claim. The equivalent exponential form follows immediately: if a scalar quantity aδ satisfies δ log aδ → −c, then aδ = exp −1δ[c + o(1)] (see [Shalizi, 2006, Definition 401]).

| |
|---|


First case: finite number of minimizers. If there are finitely many sets of local minimizers, then we can obtain an explicit concentration result inside the convex hull defined by the solutions in Mx (Fact 1), when δ goes to 06.

- Proposition 5. Let x ∈ Rd, γ > 0, δ > 0, and let Yδ ∼ N(x,δγId). Suppose that M has finitely many components, i.e.,


Mj (41)

M∗ =

1≤j≤J

for some J ∈ N. Denote by Ix the set of indices of the minimizers of fj + 21γdist(x,Att(Mj))2

, i.e., Ix ⊆ {1,...,J}. Then,

1≤j≤J

i/δP(Yδ ∈ Att(Mi))E[Tf(Yδ)|Yδ ∈ Att(Mi)] i∈Ix e−fi/δP(Yδ ∈ Att(Mi))

i∈Ix e−f

E[Tf(Yδ)e−f(T

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ] −−→

.

δ↓0

If Ix is a singleton {ix}, and Mi

x} contains an isolated local minimizer then, E[Tf(Yδ)e−f(T

= {mi

x

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ] −−→

mi

.

x

δ↓0

Proof. Since the local minimizers reached by Tf decompose into the finite disjoint union M, the sets (Attj)1≤j≤J form a measurable partition of the subset of Rd on which Tf will land in M. Denoting fj the value of f attained

- 5The small-noise Gaussian rate function can be identified directly from the explicit normal example in [Kosygina and Mountford,

2018, pp.4–5] with Xn ∼ N(0, 1/n) , which yields the rate function I(x) = x2/2, and cf. [den Hollander, 2000, Exercise III.9, p.30].

- 6This result is similar in spirit to [Zhang et al., 2024, Corollary 1] even though proofs are completely different


on Mj, we have

E[Tf(Yδ)e−f(T

f(Yδ))/δ] =

=

=

J

E[Tf(Yδ)e−f(T

f(Yδ))/δ1{Y

δ∈Att(Mj)}]

j=1

J

e−f

j/δE[Tf(Yδ)1{Y

δ∈Att(Mj)}]

j=1

J

e−f

j/δP(Yδ ∈ Att(Mj))E[Tf(Yδ)|Yδ ∈ Att(Mj)].

j=1

Moreover, using Lemma 3, we obtain that

δ log e−f

j/δP(Yδ ∈ Att(Mj)) =δ→0 −fj −

- 1

- 2γ


dist(x,Att(Mj))2,

implying

1 2γ

1 δ

e−f

dist(x,Att(Mj))2 + o(1) . Now, take the set Ix. For all i ∈ Ix, and j ∈ J \ Ix, we have

j/δP(Yδ ∈ Att(Mj)) =δ→0 exp −

fj +

i/δP(Yδ ∈ Att(Mi)) e−fj/δP(Yδ ∈ Att(Mj)) −−→

e−f

1 2γ

- 1

- 2γ


dist(x,Att(Mj))2 − fi −

dist(x,Att(Mi))2 > 0

δ log

fj +

δ↓0

implying that

i/δP(Yδ ∈ Att(Mi)) e−fj/δP(Yδ ∈ Att(Mj))

e−f

= +∞. Hence, we obtain that

lim

δ→0

j/δP(Yδ ∈ Att(Mj)) j∈J e−fj/δP(Yδ ∈ Att(Mj))

j∈J\Ix e−f

lim

= 0.

δ→0

The rest follows from the fact that no connected components of M is unbounded, guaranteeing that E[Tf(Yδ)|Yδ ∈ Att(Mj)] is bounded for all j.

| |
|---|


This result highlights the need for the uniqueness of the global minimizer: the barycenter of several global minimizers does not make any sense unless these global minimizers belong to the same connected and convex set.

- Proof of Proposition 1. Proof. Fix η > 0, and let Kη ⊂ M∗ be a bounded set such that (Lemma 7)


Vx(m) ≥ αx + η.

inf

m/∈Kη

Set

Aη := {y ∈ Rd : Tf(y) ∈ Kη∁}. We look at our measure outside this bounded set

νx,δ(Kη∁) = E e−f(T

f(Yδ))/δ1{T

f(Yδ)∈Kη∁}

f(Tf(y)) + ∥y − x∥2 2γ

1 (2πδγ)d/2 A

1 δ

exp −

=

η

dy.

2

2γ . If y ∈ Aη, then Tf(y) ∈ M ∈ Kη∁, and since y ∈ Att(M),

We first study the term in the exponential. Set g(y) = f(Tf(y)) + ∥y−x∥

dist(x,Att(M))2 2γ

∥y − x∥2 2γ ≥

.

Hence,

g(y) = f(M) + ∥y − x∥2 2γ ≥ f(M) +

dist(x,Att(M))2 2γ

= Vx(M) ≥ αx + η. Therefore, infy∈A

g(y) ≥ αx + η. Now, to estimate the measure, we split our set with a ball of radius R > 0 in the following way:

η

Aη = (Aη ∩ B(0,R)) ∪ Aη ∩ B(0,R)∁ . The measure on the lefthandside of the union is easily bounded by the previous inequality as we have, 1 (2πδγ)d/2 A

λd(B(0,R)) (2πδγ)d/2

e−g(y)/δ dy ≤

e−(α

x+η)/δ.

η∩B(0,R)

Since

δ log δ−d/2 −−→

0, it follows that

δ↓0

1 (2πδγ)d/2 A

e−g(y)/δ dy ≤ −(αx + η).

limsup

δ log

η∩B(0,R)

δ↓0

f is bounded from below on Rd, hence all y,

g(y) ≥ fmin + ∥y − x∥2 2γ

.

Thus

∥y − x∥2 2γδ

1 (2πδγ)d/2 A

min/δ 1 (2πδγ)d/2 B(0,R)∁

e−g(y)/δ dy ≤ e−f

exp −

η∩B(0,R)∁

The last term is exactly

e−f

min/δ P(∥Yδ∥ > R). We can take R > ∥x∥, large enough so that

(R − ∥x∥)2 2γ

fmin +

> αx + η.

dy.

Since ∥y − x∥ ≥ R − ∥x∥ whenever ∥y∥ > R, the Gaussian tail satisfies [den Hollander, 2000]

(R − ∥x∥)2 2γ

δ log P(∥Yδ∥ > R) ≤ −

limsup

,

δ↓0

and therefore

(R − ∥x∥)2 2γ

δ log e−f

min/δP(∥Yδ∥ > R) ≤ −fmin −

< −(αx + η).

limsup

δ↓0

Combining the estimates on Aη ∩ B(0,R) and Aη ∩ B(0,R)∁, we obtain limsupδ↓0 δ log νx,δ(Kη∁) ≤ −(αx + η). We now lower bound the denominator. Let ε > 0. By definition of αx, there exists Mε ∈ M such that

Vx(Mε) ≤ αx + ε. Then

νx,δ(M) = E e−f(T

f(Yδ))/δ ≥ e−f(m

ε)/δP(Yδ ∈ Att(Mε)). By Lemma 3,

- 1

- 2γ


dist(x,Att(Mε))2, hence

δ log P(Yδ ∈ Att(Mε)) = −

lim

δ↓0

- 1

- 2γ


dist(x,Att(Mε))2 = −Vx(Mε) ≥ −(αx + ε).

δ log νx,δ(M) ≥ −f(Mε) −

liminf

δ↓0

Letting ε ↓ 0 gives

δ log νx,δ(M) ≥ −αx. Finally,

liminf

δ↓0

νx,δ(Kη∁) νx,δ(M)

µx,δ(Kη∁) =

, so

δ log µx,δ(Kη∁) ≤ −(αx + η) − (−αx) = −η. In particular, µx,δ(Kη∁) → 0, that is, µx,δ(Kη) → 1. Proof of Proposition 6.

limsup

δ↓0

- Proposition 6. Let x ∈ Rd, γ > 0, q ≥ 0, and let Yδ ∼ N(x,δγId). Let R > 0. We have


1/β

C1Rα−C2−C3 C3

− ∥x∥2

+

+

δ log E[∥Tf(Yδ)∥e−f(T

f(Yδ))/δ1{∥T

f(Yδ)∥>R}] ≤ −fmin −

limsup

,

2γ

δ↓0

and that

δ log E[e−f(T

f(Yδ))/δ] ≥ −αx. Then,

liminf

δ↓0

| |
|---|


limsup

δ log

δ↓0

1/β

C1Rα−C2−C3 C3

− ∥x∥2

E[∥Tf(Yδ)∥e−f(T

f(Yδ))/δ1{∥T

f(Yδ)∥>R}] E[e−f(Tf(Yδ))/δ] ≤ αx − fmin −

+

+

.

2γ

Proof. We have that

E[Tf(Yδ)e−f(T

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ]

is well defined. Indeed, 0 ≤ E[e−f(T

min/δ < +∞ and E[∥Tf(Yδ)∥e−f(T

min/δE[∥Tf(Yδ)∥] <

f(Yδ))/δ] ≤ e−f

f(Yδ))/δ] ≤ e−f

+∞ by Lemma 8. Using our measure introduced in Proposition 1 we have E[Tf(Yδ)e−f(T

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ]

=

mdµx,δ(m)

m∈M∗

Using similar arguments than in the proof of Lemma 8 we can have that m  → ∥m∥ is integrable against µx,δ. We have

E[∥Tf(Yδ)∥e−f(T

f(Yδ))/δ1{∥T

f(Yδ)∥>R}] E[e−f(Tf(Yδ))/δ]

∥m∥dµx,δ(m) =

m∈M∗,∥m∥>R

As

min/δE[C1−1/α C2 + C3(1 + ∥Yδ∥β) 1/α 1∥T

E[∥Tf(Yδ)∥e−f(T

f(Yδ)∥>R] ≤ e−f

f(Yδ))/δ1∥T

f(Yδ)∥>R], and,

implying that

R < C1−1/α C2 + C3(1 + ∥Yδ∥β) 1/α ⇔

1/β

C1Rα − C2 − C3 C3

< ∥Yδ∥,

{∥Tf(Yδ)∥ > R} ⊂ ∥Yδ∥ >

(C1Rα − C2 − C3)+ C3

1/β

###### .

Therefore,

E[∥Tf(Yδ)∥e−f(T

f(Yδ))/δ1∥T

f(Yδ)∥>R] ≤ e−f

###### min/δE C1−1/α C2 + C3(1 + ∥Yδ∥β) 1/α 1

∥Yδ∥> Rα−CC2−C3

3

1/β

We can show that there exists C2,α,C3,α > 0 such that

C1−1/α C2 + C3(1 + ∥Yδ∥β) 1/α ≤ C2,α + C3,α(1 + ∥Yδ∥β/α).

1/β

1Rα−C2−C3 C3

Now, using Lemma 9 with q = β/α and r = C

we have

(r − ∥x∥2)+ 2γ

δ log E C1−1/α C2 + C3(1 + ∥Yδ∥β) 1/α 1{∥Y

δ∥>r} ≤ −

limsup

.

δ↓0

The lower bound was already shown in Proposition 1. Hence the result.

| |
|---|


- Lemma 11. Let x ∈ Rd, γ,δ > 0, ε > 0 and Yδ ∼ N(x,δγId). Let R > 0. We have


δ log µx,δ ((Mx)ε)∁ ∩ B(0,R) ≤ −cR,ε. (42)

limsup

δ↓0

Therefore for sufficiently large R

δ log µx,δ ((Mx)ε)∁ < 0. (43) hence,

limsup

δ↓0

µx,δ ((Mx)ε)∁ −−→

1 (44)

0, and µx,δ (((Mx)ε)) −−→

δ↓0

δ↓0

Proof. We have

E e−f(T

f(Yδ))/δ1{Tf(Yδ)∈((Mx)ε)∁∩B(0,R)}

µx,δ ((Mx)ε)∁ ∩ B(0,R) =

E e−f(Tf(Yδ))/δ and, there exists some set Mx,R,ε (Fact 1) such that

Tf(Yδ) ∈ ((Mx)ε)∁ ∩ B(0,R) ⊂ Mx,R,ε. Hence,

E e−f(T

e−f(M)/δP(Yδ ∈ Att(M)),

f(Yδ))/δ1{Tf(Yδ)∈((Mx)ε)∁∩B(0,R)} ≤

M∈Mx,R,ε

which is sufficient to conclude for the first inequality by applying Lemma 3. The second inequality comes from the fact that

µx,δ ((Mx)ε)∁ ≤ µx,δ ((Mx)ε)∁ ∩ B(0,R) + µx,δ(B(0,R)∁), where the second complement is taken in M∗. We apply Proposition 1 to obtain the desired result. If R is large enough then it means that the mass outside the ball B(0,R) goes to 0 when δ ↓ 0.

| |
|---|


- Proof of Proposition 2. Proof. Fix ε > 0 and R > 0. For convenience, we write


E[Tf(Yδ)e−f(T

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ]

mδ :=

Since the distance to a closed convex set is a convex function, Jensen’s inequality gives

dist(mδ,conv(Mx)) = dist

z µδ,x(dz),conv(Mx)

M∗

≤

dist(z,conv(Mx)) µδ,x(dz).

M∗

We split the integral over the three regions (Mx)ε ∩ B(0,R), B(0,R) \ (Mx)ε, and B(0,R)∁. If z ∈ (Mx)ε, then since Mx ⊂ conv(Mx), dist(z,conv(Mx)) ≤ dist(z,Mx) < ε. If z ∈ B(0,R) \ (Mx)ε, then dist(z,conv(Mx)) ≤ ∥z∥ ≤ R. If ∥z∥ > R, then dist(z,conv(Mx)) ≤ ∥z∥. Therefore,

dist(mδ,conv(Mx)) ≤ ε + R µδ,x ((Mx)ε)∁ +

∥z∥1{∥z∥>R} µδ,x(dz).

M∗

Now let δ ↓ 0. By Lemma 11 ,

µδ ((Mx)ε)∁ → 0, hence

∥z∥1{∥z∥>R} µδ,x(dz). Next let R → ∞ and use Lemma 6 on the righthandside integral to obtain

dist(mδ,conv(Mx)) ≤ ε + limsup

limsup

δ↓0

δ↓0 M∗

dist(mδ,conv(Mx)) ≤ ε.

limsup

δ↓0

Since ε > 0 is arbitrary, this proves

dist(mδ,conv(Mx)) −−→

0. The limit in the isolated local minimizer case follows immediately.

δ↓0

| |
|---|


###### Proof of Theorem 2.

Proof. First, by rejecting worse update and coercivity of f (Assumption 1), iterates are bounded and stay in some bounded set B ⊂ Rd. Thus

dist(x,Att(x∗)) < +∞. Set γ > 0. For every x ∈ B,

df := sup x∈B

- 1

- 2γ


d2f + fmin

Vx(x∗) ≤

2 f

If γ > d

2µ then, for all M ̸= x∗,

Vx(x∗) < fmin + µ ≤ Vx(M). Meaning that for γ sufficiently large, by Proposition 2 there exists δ > 0 and r > 0 such that for all δ ≤ δ

∥mδ,γ − x∗∥ ≤ r.

Therefore, if there exists r > 0, such that B(x∗,r) ⊂ Att(x∗), then x+ = x∗. Such statement holds in our context as x∗ is an isolated local minimizer, reached by Tf. We thus obtain immediate convergence if γ is large enough and δ small enough.

Now there are several scenarios:

- • if progress (i.e., strict decrease) is made at every iteration, as iterates are bounded, we visit finitely many M ∈ M until convergence (see proof of Theorem 1).
- • As derived just before, we can only "not improve" the next iterate finitely many times before reaching γk large enough, hence we obtain convergence as soon as δ is small enough which happens eventually.


Hence, we obtain convergence of the iterates to the global minimizer.

| |
|---|


- D.3 Proofs for approximate expectation PBH


- Proof of Lemma 12.

Lemma 12. Let x ∈ Rd, δ,γ > 0 and i.i.d. samples {yi} ∼ Yδ ∼ N(x,δγId). Then, almost surely,

mN,δ,γ :=

N i=1 Tf(yi)exp(−f (Tf(yi))/δ)

N i=1 exp(−f (Tf(yi))/δ)

−−−−−→

N→+∞

mδ,γ. (45)

Proof. We have first that for all N ∈ N, Ni=1 exp(−f (Tf(yi))/δ) > 0, each term is integrable against the Gaussian measure, and thus by the strong law of large numbers N1 Ni=1 exp(−f (Tf(yi))/δ) −−−−−→

N→+∞

E e−f(T

f(Yδ))/δ

a.s.. On the other end, by Lemma 8, each term in Ni=1 Tf(yi)exp(−f (Tf(yi))/δ) is integrable against the Gaussian measure, and thus by the strong law of large numbers N1 Ni=1 Tf(yi)exp(−f (Tf(yi))/δ) −−−−−→

N→+∞ E Tf(Yδ)e−f(T

f(Yδ))/δ a.s.. Hence, mN,δ,γ −−−−−→

N→+∞

mδ,γ a.s..

| |
|---|


- Proof of Lemma 13.

Lemma 13. Let x ∈ Rd, δ,γ > 0 and i.i.d. samples {yi} ∼ Yδ ∼ N(x,δγId). Suppose that there exists M ∈ M such that dist(mδ,γ,∂Att(M)) > 0. Then, almost surely,

Tf(mN,δ,γ) −−−−−→

N→+∞

Tf(mδ,γ). (46)

Proof. We have by Assumption 4 that Tf is continuous on any interior of Att(M), hence the result follows from Lemma 12.

| |
|---|


- Proof of Lemma 14.


- Lemma 14. Let (mN)N≥1 be a sequence in Rd such that mN → m, N → +∞. Assume that for sufficiently large


N, mN does not belong to Ns the measurable null set not included in the partition of Rd defined by M∈M Att(M) (Lemma 6). Then every accumulation point of the sequence (Tf(mN))N≥1 belongs to

Q, Adj(m) := {Q ∈ M : m ∈ Att(Q)}. (47)

Q∈Adj(m)

Proof. Let m be a cluster point of (Tf(mN))N≥1. Then there exists a subsequence (mN

)k≥1 such that Tf(mN

k

) → m. Since (Tf(mN

k

))k≥1 converges, it is bounded. Hence there exists a compact set K ⊂ Rd such that Tf(mN

) ∈ K for all k. By assumption, only finitely many components of M intersect K. Therefore, after extracting a further subsequence, there exists a component Q ∈ M such that

k

k

) ∈ Q for all ℓ ≥ 1. On the other hand, for k large enough one has mN

Tf(mN

kℓ

k ∈ Att(Mk) for a unique component Mk ∈ M. Because Tf(mN

∈/ N, and therefore mN

k

) ∈ Q and Tf(y) ∈ M whenever y ∈ Att(M), we must have Mk = Q. Hence for all sufficiently large k, mN

k

k → m, we obtain m ∈ Att(Q). Thus Q ∈ Adj(m).

k ∈ Att(Q). Passing to the limit and using mN

| |
|---|


###### Proof of Theorem 3.

Proof. First, as the number of samples grows to infinity, by Lemma 12, all mN,δ,γ are close to mδ,γ, hence we the behavior of the algorithm is governed asymptotically by the behavior of Algorithm 1.

By rejecting worse update and coercivity of f (Assumption 1), iterates are bounded and stay in some bounded set B ⊂ Rd. Thus

dist(x,Att(x∗)) < +∞.

df := sup x∈B

Set γ > 0. For every x ∈ B,

- 1

- 2γ


d2f + fmin

Vx(x∗) ≤

2 f

If γ > d

2µ then, for all M ̸= x∗,

Vx(x∗) < fmin + µ ≤ Vx(M). Meaning that for γ sufficiently large, by Proposition 2 there exists δ > 0 and r1 > 0 such that for all δ ≤ δ

∥mδ,γ − x∗∥ ≤ r1. Moreover, for N sufficiently large, there exists r2 > 0 such that

∥mN,δ,γ − mδ,γ∥ ≤ r2.

Therefore, as there exists r > 0, such that B(x∗,r) ⊂ Att(x∗), and r1 + r2 ≤ r, then x+ = x∗. We thus obtain immediate convergence if γ is large enough, N is large enough and δ small enough.

Now as in Theorem 2, there are several scenarios:

- • if progress (i.e., strict decrease) is made at every iteration, as iterates are bounded, we visit finitely many

M ∈ M until convergence (see proof of Theorem 1). We can however visit non minimizing point as mN,δ,γ may sit with non zero probability in the null set of the partition defined by Att(M) for all M ∈ M, hence finite convergence cannot be guaranteed to happen.

- • As derived just before, we can only "not improve" the next iterate finitely many times before reaching γk large enough, hence we obtain convergence as soon as δ is small enough, and N is big enough which happens eventually.


Hence, we obtain convergence of the iterates to the global minimizer.

| |
|---|


###### Proof of Proposition 3.

Proof. Denote mN,δ,γ = A

BN , mδ,γ = BA, where

N

N

1 N

Tf(yi)exp(−f(Tf(yi))/δ), and A = E[Tf(Yδ)exp(−f(Tf(Yδ))/δ)],

AN =

i=1

while

N

1 N

exp(−f(Tf(yi))/δ), and B = E[exp(−f(Tf(Yδ))/δ)]. We want to control

BN =

i=1

B(AN − A) − A(BN − B) BBN

AN BN −

A B

=

,

w.r.t. quantities that we control, i.e., ∥AN − A∥ and |BN − B|. We first look at the denominator. Set 0 < η < B and the event {|BN −B| ≤ η}. On this event, we have BN ≥ B −η > 0, implying by the triangular inequality that

+ ∥A∥|BN − B| B(B − η)

∥AN − A∥ B − η

B(AN − A) − A(BN − B) BBN ≤

∥mN,δ,γ − mδ,γ∥ =

.

Now, to obtain ∥mN,δ,γ − mδ,γ∥ ≤ ε, we bound the two terms on the righthandside of this inequality w.r.t. B − η. If ∥AN − A∥ ≤ 2ε(B − η), and |BN − B| ≤ min η, εB2(∥BA−∥η) , then we obtain the desired bound. It remains to quantify the probability of these two bounds holding together. Indeed, we have

εB(B − η) 2∥A∥

ε 2

(B − η) |BN − B| ≤ min η,

{∥mN,δ,γ − mδ,γ∥ ≤ ε} ⊂ ∥AN − A∥ ≤

The union bound on the complements then tells us that

.

P(∥mN,δ,γ − mδ,γ∥ ≤ ε) ≥ 1 − P ∥AN − A∥ >

εB(B − η) 2∥A∥

ε 2

(B − η) − P |BN − B| > min η,

.

The two righthandside probabilities can be controlled through Markov’s and Chebyshev’s inequality. We can apply it through the growth control on f and Lemma 8 as ∥AN − A∥ and |BN − B| are both square integrable against the Gaussian measure. We have

As

E[∥AN − A∥2] t2

Var(BN) s2

, and P(|BN − B| > s) ≤

P(∥AN − A∥ > t) ≤

.

1 N2

E[∥AN − A∥2] = E

  1

= E

1 N2

=

N

N

AiN − A,

AiN − A

i=1

i=1

 

N

AiN − A,AjN − A

N2

i,j=1

N

E AiN − A,AjN − A

i,j=1

For i ̸= j by independence, we have E AiN − A,AjN − A = 0. Remain the N, i = j terms, giving

1 N

E∥Tf(y1)exp(−f(Tf(y1))/δ) − A∥2, while

E ∥AN − A∥2 =

Var(exp(−f(Tf(y1))/δ)) N

, Therefore, we obtain

Var(BN) =

4E∥Tf(y1)exp(−f(Tf(y1))/δ) − A∥2 Nε2(B − η)2 −

Var(exp(−f(Tf(y1))/δ)) N min η, εB2(∥BA−∥η)

P(∥mN,δ,γ − mδ,γ∥ ≤ ε) ≥ 1 −

2 .

We deduce then the existence of α by setting N large enough.

| |
|---|


The dependence on δ may appear highly problematic, but also note that in practice f(Tf(y1)) should be of the order of δ for our best samples.

###### Proof of Theorem 4.

Proof. The number of samples is finite, by Lemma 12, all mN,δ,γ are close to mδ,γ, hence we the behavior of the algorithm is governed asymptotically by the behavior of Algorithm 1.

By rejecting worse update and coercivity of f (Assumption 1), iterates are bounded and stay in some bounded set B ⊂ Rd. Thus

dist(x,Att(x∗)) < +∞. Set γ > 0. For every x ∈ B,

df := sup x∈B

- 1

- 2γ


d2f + fmin

Vx(x∗) ≤

2 f

If γ > d

2µ then, for all M ̸= x∗,

Vx(x∗) < fmin + µ ≤ Vx(M). Meaning that for γ sufficiently large, by Proposition 2 there exists δ > 0 and r1 > 0 such that for all δ ≤ δ ∥mδ,γ − x∗∥ ≤ r1. For N sufficiently large (Proposition 3), there exists ε > 0 and 0 < α < 1 such that P(∥mN,δ,γ − mδ,γ∥ ≤ ε) ≥ α.

Therefore, as there exists r > 0, such that B(x∗,r) ⊂ Att(x∗), we need ε small enough so that and r1 + ε ≤ r, then with probability superior or equal to α, x+ = x∗. Thus, if N is large enough so this ε is small enough, then the high probability follows.

The rest of the proof is the same as in Theorem 3. Hence, we obtain convergence of the iterates to the global minimizer with high probability.

| |
|---|


The trick here is that we do not need an uniform control on the probability on all the iterates. We simply need to wait for γ to be sufficiently large so that one of the iterates theoretically has x∗ as one of its minimizers of the potential Vx, then if we have enough samples we reach the correct solution with high probability.

### E Additional results

We display additional results for the full scaling law (all parameters available to be fitted Shukor et al. [2025]). The results are worse (in terms of prediction) than those of the additive law, in average. It was expected given the results of Shukor et al. [2025]. Our algorithm stil outperforms the others.

|Family Domain<br><br>|N = 5 N = 10 N = 15 N = 20 N = 30 N = 40 N = 50|ZOP BH|
|---|---|---|
|LLM (d = 47)<br><br>arxiv book c4 commoncrawl github stackexchange wikipedia<br><br>|12.085 12.303 11.681 12.358 11.861 12.177 12.694 10.046 10.949 10.173 10.722 10.718 10.264 10.265<br><br>10.937 10.949 10.874 10.936 11.115 11.472 10.716 10.445 11.038 11.834 11.710 11.450 11.516 11.256<br><br>17.323 17.385 18.258 17.305 18.434 17.899 18.470 12.488 12.891 12.943 13.162 13.110 13.024 13.073 19.658 19.859 20.044 19.664 19.915 19.739 19.749<br><br>|12.646 12.379<br><br>10.800 10.649<br>11.309 11.314 11.677 11.464<br><br><br>19.882 18.847<br><br>13.620 13.374<br><br>20.529 19.827<br><br><br>|
|LVM (d = 29)<br><br>alttext<br><br>highquality1<br><br>highquality2 synthetic<br><br><br>|4.117 6.703 11.270 10.317 12.237 14.245 14.062 7.634 7.758 9.393 12.712 18.447 16.315 19.492 7.536 10.969 9.483 11.711 15.700 18.769 19.177 11.435 14.736 11.070 13.664 14.441 16.844 21.105<br><br>|13.176 10.130 21.979 11.756 21.367 12.207 29.138 15.884|
|NMM (d = 23)<br><br>captions interleaved text|10.944 12.190 11.921 12.111 12.098 12.596 12.347 10.839 8.768 10.925 11.097 10.969 10.586 10.706<br><br>6.565 9.392 8.811 9.057 9.313 9.174 9.131<br><br>|11.351 11.317 10.178 10.907 8.774 8.120|


- Table 2: Test MRE = |predictionobservation−observation| (%) for fitting full scaling law. (lbfgs steps=10, CPU time=300s). We set γ = 10 and δ = 10−3 at initialization. Results averaged over three seeds.

|Family Domain<br><br>|N = 5 N = 10 N = 15 N = 20 N = 30 N = 40 N = 50|ZOP BH|
|---|---|---|
|LLM (d = 47)<br><br>arxiv book c4 commoncrawl github stackexchange wikipedia<br><br>|12.373 12.445 11.820 12.478 12.318 12.561 12.387<br><br>9.910 10.947 10.529 10.590 10.451 10.295 10.256 11.226 11.266 11.571 11.161 11.201 11.203 10.992<br>10.650 11.254 11.733 11.249 11.321 11.679 11.331 16.579 18.328 18.947 16.835 18.686 18.750 18.329<br>11.735 12.606 13.342 12.858 13.802 13.620 13.517 19.285 19.407 19.909 19.398 19.976 20.077 19.930<br>|12.646 12.269<br><br>10.800 10.629<br><br>11.309 11.060<br><br><br>11.677 11.474<br><br>19.882 18.243<br><br>13.620 13.339<br><br>20.529 19.744<br><br><br><br><br>|
|LVM (d = 29)<br><br>alttext<br><br>highquality1<br>highquality2 synthetic<br>|4.438 6.761 13.017 10.932 13.403 14.336 14.217 7.228 7.850 10.172 12.248 18.583 17.110 19.230 7.305 10.519 9.581 12.259 17.326 18.470 19.405 9.318 11.464 10.898 15.507 18.410 17.687 20.299<br><br>|13.176 10.094 21.979 11.735 21.367 12.217 29.138 18.764|
|NMM (d = 23)<br><br>captions interleaved text<br><br>|10.727 11.847 11.867 12.172 12.224 12.383 12.094 10.561 8.522 10.151 11.040 10.564 10.552 10.649 7.202 8.772 8.902 9.023 9.787 9.147 9.147|11.351 11.308 10.178 10.906 8.774 8.120<br><br>|


- Table 3: Test MRE = |predictionobservation−observation| (%) for fitting full scaling law. (lbfgs steps=5, CPU time=300s). We set γ = 10 and δ = 10−3 at initialization. Results averaged over three seeds.


# arXiv:2605.18364v1[cs.LG]18May2026

## Proximal basin hopping: global optimization with guarantees

Cesare Molinari MALGA Università di Genova Italy cecio.molinari@gmail.com

Guillaume Lauga LJAD Université Côte d’Azur France guillaume.lauga@univ-cotedazur.fr

Samuel Vaiter CNRS, LJAD Université Côte d’Azur France samuel.vaiter@univ-cotedazur.fr

May 19, 2026

Abstract

Global optimization is a challenging problem, with plenty of algorithms displaying empirical success, but scarce theoretical backing. In this work, we propose a new theoretical framework called Proximal Basin Hopping (PBH), carefully tailored to combine proximal optimization and local minimization. We use it to construct a practical algorithm that converges to the global minimizer with high probability, when using a finite amount of samples. Proximal Basin Hopping outperforms well known algorithms with theoretical backing on standard synthetic hard functions, and real problems such as fitting scaling laws for deep learning. Furthermore, the higher the dimension, the better the performance gap.

### 1 Introduction

Finding global minimizers of highly non-convex functions is a challenging but crucial task in various fields such as computational chemistry and biology [Prentiss et al., 2008, Alvarez and Calaminici, 2025], engineering design [Arora et al., 1995, Englander et al., 2020] and of course machine learning [Goodfellow et al., 2016]. We are interested in solving the following optimization problem

f(x). (1)

Find x ∈ arg min

x∈Rd

where f is a non-convex, continuous function. We will assume that f possesses one global minimizer and some regularity that can be exploited to compute some descent steps (or find local minimizers directly). To tackle this problem, we propose a hybrid approach that sits at the intersection between proximal algorithms [Parikh and Boyd, 2014] and basin hopping algorithms [Wales and Doye, 1997].

Standard first-order algorithms can only hope to obtain local solutions to Problem (1), which has prompted many to propose global optimization techniques, most of which are heuristic and do not possess strong convergence guarantees. Global optimization algorithms perform by combining exploration (through random perturbation of the current guesses) and exploitation steps (through function evaluation and/or local minimization) to reach a solution. The exploration requires a number of samples going to infinity to fit an underlying algorithm with increasing precision [Fornasier et al., 2024, Zhang et al., 2024], or a number of samples growing exponentially fast with the dimension to cover the space sufficiently enough [Hansen et al., 1992, Bouttier et al., 2020] to reach acceptable accuracy. This becomes rapidly cumbersome, even for problems of (nowadays) relatively small dimension (in the few hundreds) [Papenmeier et al., 2025]. On the other hand, the inexactness of the exploitation

0Acknowledgements. This work has been supported by the French government, through the 3IA Cote d’Azur Investments in the project managed by the National Research Agency (ANR) with the reference number ANR-23-IACL-0001, the ANR project PRC MAD ANR-24-CE23-1529 and the support of the “France 2030” funding ANR-23-PEIA-0004 (PDE-AI).

![image 8](<2026-lauga-proximal-basin-hopping-global_images/imageFile8.png>)

![image 9](<2026-lauga-proximal-basin-hopping-global_images/imageFile9.png>)

Figure 1: Proximal Basin Hopping on the 2D-Rastrigin function at iteration 3 (left) and iteration 5 (right), where convergence to the global minimizer, x∗ = (0,0), has occurred. From the current iterate, we draw several samples, that are then sent to their nearest achievable local minimizer, then weighted with respect to the achieved function value giving a new guess that is again sent to its nearest achievable local minimizer (if it is not there already).

steps through local minimization is difficult to account for in the theoretical analysis [György and Kocsis, 2011]. Hence, we propose a new framework opening the path to quantify the effect of sample size and inexactness on the convergence to the global minimizer.

Contributions. The method we propose, which we call Proximal Basin Hopping (PBH) is derived from an ideal operator proxγT

###### f(x), where Tf is a deterministic local solver, yielding for (almost) any starting point its achievable local minimizer, and prox denotes a proximal operation. This operator mimics Tf(proxf◦T

f

(x)) from which we gradually relax the required computations, in order to construct an algorithm using a finite amount of samples and possibly inexact local minimization (see Figure 1 for an illustration). We obtain thus four operators, from most ideal to most practical:

f

1. Ideal PBH: we make sense of the ≈ in Lemma 1,

Sfγ(x) := proxγT

f(x) ≈ Tf proxγ(f◦T

f)(x) .

f

2. Exact expectation PBH: the proximal operator is replaced by its zeroth-order approximation

Sfγ(x) ≈δ Tf

Ey∼N(x,δγId)[Tf(y)exp(−f (Tf(y))/δ)] Ey∼N(x,δγId)[exp(−f (Tf(y))/δ)]

.

3. Approximated expectation PBH: the zeroth-order approximation of the prox is estimated using N samples. For i = 1,...,N, yi ∼ N(x,δγId)

N i=1 Tf(yi)exp(−f (Tf(yi))/δ)

Sfγ(x) ≈Nδ Tf

.

N i=1 exp(−f (Tf(yi))/δ)

4. Approximated expectation & inexact local solving PBH:

 

 ,

N i=1 Tfε(yi)exp(−f Tfε(yi) /δ)

Sfγ(x) ≈Nδ,ε Tfε

N i=1 exp(−f Tfε(yi) /δ)

By allowing inexact computations of the proximal operator and of the local solver, we obtain a practical algorithm, that can recover the global minimizer. This relies on a structural assumption on f: the global minimizer is sufficiently different in function value from local minimizers.

We present extensive experiments on hard-to-optimize functions in moderate dimension (2 to 200), and apply our algorithm to the problem of fitting scaling laws on real data from [Shukor et al., 2025]. When the dimension is low (between 1 and 10) our algorithm is competitive with basin hopping, with respect to CPU time. It becomes conclusively better from moderate to high dimension.

Summary of theoretical results. Our goal is to show the convergence of our most practical algorithm. Such a result is obtained building up on the proofs of convergence of more ideal algorithms, by trying to emulate the same behavior: the second operator induces convergence because it approximates the first operator. The third operator induces convergence by emulating the second, and so on.

1. Ideal PBH: convergence holds through the properties of the potential Vx(M) := 1/(2γ)dist(x,Att(M))2+f(M)

and of its minimizers which are the elements of Sfγ(x): it is sufficiently well-behaved for finite time convergence to occur.

- 2. Exact expectation PBH: by proving convergence of the expectation onto the minimizers of Vx(·) when δ goes to 0, we can reuse the convergence arguments of the first algorithm to guarantee convergence to the global minimizer (but not in finite time).
- 3. Approximated expectation PBH: first by standard arguments, bringing N to infinity allows us to recover the setting of the second algorithm. In a following analysis, we show that with high probability, we only need a finite N to converge.
- 4. Approximated expectation & inexact local solving PBH: we highlight simple conditions on the inexactness that should hold to obtain convergence.


### 2 Structural assumptions on f and the local solver

In this section, we present in detail the structural assumptions we make on f and on the local solver Tf in order to guarantee convergence of our algorithms. We make assumptions on f that are either standard in optimization, or reasonable given our goal of reaching the global minimizer.

Assumption 1. The function f : Rd → R ∪ {+∞} is proper, continuous, and coercive. We define the family of sets of local minimizers of f as

M := M connected :∃ V (open) ⊂ Rd, M ⊊ V, M = arg min

f(x),∀x ∈ V \ M, f(x) > f(M) . (2)

x∈V

We assume that every M ∈ M is Borel, bounded, and only finitely many elements of M intersect each compact subset of Rd.

This definition of M prevents redundancy, and ensures that the M are pairwise disjoints. Thus, M consists of possibly infinitely many disjoint, connected components of local minimizers M ∈ Rd, but finitely many on any compact set. In other words, f is "tame" (see App. C.1 for some examples). In the basin hopping literature, the standard hypothesis is for f to have finitely many of these components1. This case is easily covered by our framework. We take the liberty of writing f(M) < f(Q) for any component Q and M in M as f is constant on each connected component. We will denote the union of all elements of M as M∗ = M∈M M. We also need separation between the global minimizer and other local minima:

Assumption 2. The function f has a unique global minimizer {x∗}. ∃ µ > 0 such that for all M ∈ M \ {x∗}, fmin + µ < f(M).

This assumption is relatively strong by preventing arbitrary accumulation of almost global local minimizers, but also in line with previous assumptions of the literature such as [Zhang et al., 2024, Assumption 3] which requires that no critical point x ̸= x∗ such that f(x) < fmin + µ exists.

1Finite does not mean small, the number of minimizers grows exponentially with the dimension for the Lennard-Jones cluster problem, introduced in the seminal paper of basin hopping [Wales and Doye, 1997].

Assumption 3. The local solver Tf : Rd → Rd is measurable, single-valued, and outputs almost everywhere a local minimizer, i.e., Tf(x) ∈ M∗ a.e..

Tf maps any point to its unique achievable local minimizer. We define this achievability with the attractors of the local minimizers, which we denote by Att

(∀M ∈ M), Att(M) := y ∈ Rd, Tf(y) ∈ M . (3)

Obviously the geometry of Att depends a lot on the solver [Asenjo et al., 2013, Levy, 2018, 2026], we can operate under the assumption that these sets are open or closed but well-behaved2. Furthermore, under standard assumptions the attraction sets of critical points which are not local minimizers are of measure 0 [Lee et al., 2016]. As a consequence, the sets Att(M) form a measurable partition of Rd up to a null set (Lemma 6).

Assumption 4. For every M ∈ M, the restriction of Tf to int(Att(M)) is continuous.

This assumption is verified for a gradient flow, or a finitely many gradient steps, if the gradient is continuous. See App. C.1 for a detailed discussion when Tf is built with gradient descent.

We make one last structural assumption on the behavior of M  → dist(x,Att(M)) for x ∈ Rd. Assumption 5. For every x ∈ Rd and γ > 0, the function

1 2γ

dist(x,Att(M))2 (4)

Vx : M ∈ M  → f(M) +

has a nonempty bounded set of minimizers on M. Furthermore,

dist(x,Att(M)◦) = dist(x,Att(M)) = dist(x,Att(M)). (5) We define:

Sfγ(x) := proxγT

Vx(M). (6)

f(x) := arg min

f

M∈M

This assumption is relatively strong (it implies well-posedness of Sfγ) but also reasonable: it holds for gradient flow. The coercivity of f yields the coercivity of Vx, and the assumption that f has finitely many components of local minimizers on any bounded set imply the boundedness of the arg min. The non-emptiness is always true if f is C1 and Tf consists of finitely many gradient steps as it is continuous, yielding closedness of Att(M). For a general gradient flow, Att(M) is open: take for instance f := ∥ · ∥2/2. Hence, this assumption. Finally, we define for x ∈ Rd,

M. (7)

αx := inf

Vx(M), M =

M∈M

M∈Sfγ(x)

### 3 Proposed method

We first consider our ideal operator. Its study is of great interest as it will provide the optimization problem which we hope our relaxed algorithm will emulate with the proper parameter δ. For any entry x ∈ Rd, the operator Sfγ identifies nearby local minimizers. All the proofs of this section are deferred to App. D.1. Under the assumption that x does not see Att(M) only through its boundary, we can prove that Sfγ(x) = Tf(proxf◦T

(x)), which is a

f

helpful characterization in order to approximate Sfγ later. Lemma 1. Suppose that Assumptions 1, 3, and 5 hold. Set γ > 0. We have for all x ∈ Rd such that for every M ∈ Sfγ(x), projAtt(M)(x) ∩ Att(M) ̸= ∅, that Sfγ(x) = Tf(proxf◦T

(x)).

f

This operator Sfγ identifies the achievable minimizers to which x can be sent. The selection of the minimizer depends on the value of γ. Provided that γ is large enough, Sfγ recovers the global minimizer in one iteration. Lemma 2. Suppose that Assumptions 1, 2, and 5 hold. For all x ∈ Rd, there exists γx > 0 such that {x∗} ∈ Sfγ(x) for every γ ≥ γx.

2See [Levy, 2018, 2026] for a more exhaustive discussion on basins of attraction.

As we will see, this relationship between γ and the elements of Sfγ is predictive of the convergence of our more practical algorithms. Theorem 1. Convergence of ideal proximal basin hopping. Suppose that Assumptions 1, 2, and 5 hold. Let x0 ∈ Rd, γ0 > 0, η > 1, iterate for k = 0,1,...

f(z) (8)

xk+1 ∈ arg min

z∈Mxk

k+1)<f(xk)} (9) Then, {xk}k∈N converges to x∗ in finitely many iterations.

γk+1 = ηγk1{f(x

k+1)=f(xk)} + γk1{f(x

#### 3.1 Proximal basin hopping with exact expectation.

Equipped with the proximal interpretation of Sfγ, we introduce a relaxation by replacing the proximal operator by its zeroth-order approximation of parameter δ > 0 [Osher et al., 2023, Lauga and Vaiter, 2026], playing the role of

the temperature, for all x ∈ Rd

Ey∼N(x,δγId)[Tf(y)exp(−f (Tf(y))/δ)] Ey∼N(x,δγId)[exp(−f (Tf(y))/δ)]

Sfγ(x) ≈δ Tf

. (10)

With respect to the ideal operator, we want to understand how the approximated proximal operator actually converges to a solution of arg minVx when δ goes to 0. In the small δ regime, this approximation behaves closely to the ideal Sfγ, with the only caveat that if Sfγ is set-valued, the approximation sits near the convex hull of this set. As before, proofs are deferred to App. D.2.

We have this first result, derived from large deviation theory [den Hollander, 2000] and the properties of the Gaussian distribution. It is the foundation of our analysis. Lemma 3. Suppose that Assumptions 1, 5 hold. Let x ∈ Rd, γ > 0, δ > 0, and let Yδ ∼ N(x,δγId). Let M ∈ M. Then the family (Yδ)δ>0 satisfies, for each M,

1 2γ

δ log P(Yδ ∈ Att(M)) = −

lim

δ↓0

dist(x,Att(M))2.

One can see that weighting this probability by e−f(M)/δ will make the potential Vx appear on the right-hand side. Hence, we can show that the ratio of expectations in Eq. (10) converges to the set of minimizers of Vx when δ goes to 0. This is easy to obtain if the number of minimizing components is finite (App. D.2, Proposition 5). As we have infinite number of local-minimizer components, the crucial part is to make sure that almost all the mass is in a bounded set where the finite-number-of-components argument will help us complete the proof3. One can see that f cannot be too flat in all directions for this property to hold, otherwise it would allow some of the mass to escape to infinity. Coercivity is not enough to contain the mass, hence we make an additional growth assumption on f.

Assumption 6. There exist C1,C2,C3 > 0 and 0 < α < β such that

(∀z ∈ Rd), C1∥z∥α − C2 ≤ f(z) ≤ C3(1 + ∥z∥)β. (11) First, we show that a measure induced by the exponential weights goes to 1 when δ ↓ 0 on bounded sets of M∗.

Proposition 1. Suppose that Assumptions 1, 2, 3, 5, and 6 hold. Let x ∈ Rd, γ,δ > 0, and Yδ ∼ N(x,δγId). For any Borel B ∈ M∗, we define

νx,δ(B) νx,δ(M∗)

νx,δ(B) := E e−f(T

f(Yδ))/δ1{T

, (12)

f(Yδ)∈B} , µx,δ(B) :=

For any bounded set K ⊂ M∗, µx,δ(K) −−→

1.

δ↓0

3An easy way to make sure that all the mass is in a compact set is to truncate the attained minimizers if they have a norm above a threshold R, thus falling back on the finite minimizers case.

In addition, we can also ensure that the mass outside bounded sets does not escape too far (App. D.2, Proposition 6). Finally, we obtain our convergence result. Proposition 2. Suppose that Assumptions 1, 2, 3, 5, and 6 hold. Let x ∈ Rd, δ,γ > 0 and Yδ ∼ N(x,δγId). Denote by conv(Mx) the convex hull of Mx, the set of minimizers of Vx (Eq. 7). We have

E[Tf(Yδ)e−f(T

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ]

0 (13)

,conv(Mx) −−→

dist

δ↓0

In particular, if Mx = {mx,∗}, i.e., an isolated local minimizer, then, E[Tf(Yδ)e−f(T

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ] −−→

mx,∗. (14)

δ↓0

This result is almost equivalent to that of the finite case: the weighted barycenter onto which mδ converges is inside the convex hull (App. D.2, Proposition 5). In general, mδ does not need to lie inside the convex hull as some of the mass still lies outside the set of interest as long as δ > 0.

The convergence now relies on playing with the γ parameter to identify competing minimizers (Remark 1) and enable concentration on one element. If, in some iterations, several components are tied, it is not really a problem as long as it does not happen indefinitely. And we can guarantee that it does not by imposing a simple rule: if the new guess is of higher function value than the current one, we increase γ. However, with respect to the first ideal algorithm, we need γ to grow comparatively slower than δ, in order to avoid breaking our concentration result, hence we decrease δ at each iteration (while γ does not change if progress is made). Note that we do not reject equivalent samples in terms of function values for the sake of exploration.

Algorithm 1 Exact expectation proximal basin hopping Require: x0 ∈ Rd, 1 < η1 < η2, γ0 > 0, δ0 > 0 (small)

1: for k = 0,1..., do 2: mδ

−f(Tf(Y ))/δk]

k,γk ← E[Tf(Y )e

E[e−f(Tf(Y))/δk] , Y ∼ N(xk,δkγk) 3: x+ ← Tf (mδ

k,γk) 4: if f(x+) > f(xk) then 5: xk+1 ← xk,γk+1 ← η1γk 6: else if f(x+) = f(xk) then 7: xk+1 ← x+, γk+1 ← η1γk 8: else 9: xk+1 ← x+,γk+1 ← γk

10: δk+1 ← δ

k

η2 11: return xend

Theorem 2. Convergence of exact expectation PBH. Suppose that Assumptions 1, 2, 3, 5, and 6 hold. Then, the iterates {xk}k∈N of Algorithm 1 converge to x∗ when k → +∞.

#### 3.2 Proximal basin hopping with approximated expectation.

In practice, we estimate our operator Sfγ with a certain number of samples. It immediately begs the question, can this be sufficient to obtain convergence with reasonably high probability? The answer is yes, and we will show it

by studying the case where N actually goes to infinity to understand it. Again, we defer the proofs to App. D.3.

Sfγ(x) ≈Nδ Tf

N i=1 Tf(yi)exp(−f (Tf(yi))/δ)

N i=1 exp(−f (Tf(yi))/δ)

where yi ∼ N(x,δγId). (15)

Convergence when N → +∞. As for the exact case, we are first concerned with the well-posedness of the operator mN,δ,γ for all x ∈ Rd (line 2 Alg. 2). With standard arguments, we recover that mN,δ,γ → mδ,γ when N → +∞ (App. D.3, Lemma 12). The convergence of Tf(mN,δ,γ) to Tf(mδ,γ) is however not directly guaranteed as mδ,γ may lie on the boundary of some Att(M) (where we would lose local continuity of Tf), or may lie in the

null set, which consists of points from which Tf will not converge to a local minimizer. The first situation is covered by Lemma 13 and 14 (App. D.3). The null set is handled directly by our algorithm. With our built-in increase of γ, mδ,γ will fall under the conditions of Lemma 13. Indeed, for sufficiently large γ, and sufficiently small δ, mδ,γ is close to x∗ (Proposition 2). Hence increasing N sufficiently does the job.

Algorithm 2 Approximated expectation proximal basin hopping Require: x0 ∈ Rd, 1 < η1 < η2, γ0 > 0, δ0 > 0 (small), C ≥ 1, N0 ∈ N \ {0},

1: for k = 0,1..., do 2: mN

Nk i=1 Tf(yi) exp(−f(Tf(yi))/δ)

, y1,y2,...,yN

k ∼ N(xk,δkγkId) 3: x+ ← Tf (mN

k,δk,γk ←

Nk i=1 exp(−f(Tf(yi))/δ)

k,δk,γk) 4: if f(x+) > f(xk) then 5: xk+1 ← xk, γk+1 ← η1γk 6: else if f(x+) = f(xk) then 7: xk+1 ← x+, γk+1 ← η1γk 8: else 9: xk+1 ← x+, γk+1 ← γk

10: δk+1 ← δ

η2, Nk+1 ← C × Nk 11: return xend

k

Theorem 3. Convergence of approximate expectation PBH (N → +∞). Suppose that Assumptions 1, 2, 3, 4, 5, and 6 hold. The iterates {xk}k∈N of Algorithm 2 (i.e., C > 1) converge to x∗ when k → +∞.

Convergence when N < +∞. We now address the convergence of our algorithm when the number of samples remains finite. By quantifying that for N large enough ∥mN,δ,γ − mδ,γ∥ is small with high probability, we can use the arguments of the proof of Theorem 3 to recover the convergence.

Proposition 3. Suppose that Assumptions 1, 2, 3, 4, 5, and 6 hold. Let x ∈ Rd, γ,δ > 0. For any ε > 0, if N ∈ N \ {0} is large enough there exist α(ε) > 0, such that for N i.i.d. samples yi drawn from Yδ ∼ N(x,δγId),

α(ε) N

. (16) In fact, the previous result holds for all N, but is vacuous for N too small. It also holds for fixed δ and γ so we

P(∥mN,δ,γ − mδ,γ∥ ≤ ε) ≥ 1 −

need to be careful in bringing δ to 0 too fast for theoretical and practical reasons.

Theorem 4. Convergence of approximate expectation PBH (N < +∞). Suppose that Assumptions 1, 2, 3, 4, 5, and 6 hold. Then, the iterates {xk}k∈N of Algorithm 2 with finite N (i.e., C = 1) converge to x∗ when k → +∞ with high probability if N is sufficiently large.

The required N is path-dependent, but does not need to hold for all the iterates, only for those that have an underlying mδ,γ able to send them to x∗. Practical considerations are discussed in App. B, notably the interplay between Proposition 3 and the values of δ and γ. Remark that the local minimizations of the yi’s can be parallelized.

#### 3.3 Proximal basin hopping with approximated expectation and local minimization.

Now, if we also assume that we cannot do complete local minimization but only obtain approximate local solutions, then we have a third level of approximations in our algorithm.

 , where yi ∼ N(x,δγId) (17)

 

N i=1 Tfε(yi)exp −f Tfε(yi) /δ

Sfγ(x) ≈Nδ,ε Tfε

N i=1 exp −f Tfε(yi) /δ

where for all x ∈ Rd, f(Tfε(x)) ≤ f(Tf(x)) + ε, and ∥Tfε(x) − Tf(x)∥ ≤ r(ε) for some ε ≥ 0 and function r : R+ → R+, such that r(0) := 0. If Tf := Id we recover the zeroth-order proximal algorithm, which converges

provided that N → +∞. A first observation is that to obtain convergence we will need δε → 0 with the iterations

as: exp(−f(Tfε(x))/δ) ≥ exp(−f(Tf(x))/δ)exp −δε . The right-hand side exponential is approximately the size of the perturbation on the weights. A second observation is that we also need ∥Tfε(x)−Tf(x)∥ to go to 0 uniformly for all x w.r.t. ε; otherwise the weighted average would not behave as mN,δ,γ, let alone for the refined guess.

### 4 Numerical experiments

In this section, we benchmark our algorithm against the zeroth-order proximal (ZOP) algorithm presented in [Zhang et al., 2024], and basin hopping (BH) algorithm [Wales and Doye, 1997]. We argue that these two algorithms are sufficient as benchmarks as other global optimization algorithms lack convergence guarantees, and because ZOP was shown to often be better than them in [Zhang et al., 2024] as was also shown for BH [Baioletti et al., 2024].

Comparison setup. Basin hopping is our Algorithm 2 with sample size of 1. The new guess, however, is accepted with probability proportional to exp(f(x)−fδ(Tf(yi))). Zeroth-order Prox is our Algorithm App. Exp. PBH with Tf = Id. As the three algorithms are not comparable w.r.t. to iteration count, we choose to report CPU time instead. We set parameters of all algorithms to the same value at initialization, and update with the rules of our algorithm, keeping the number of samples constant for PBH and ZOP. We did not investigate multisearch, and instead focused on convergence from one initialization. After the CPU-time budget has been spent, algorithms are stopped.

Set of problems. We propose to test our algorithm on various problems, with different complexities.

Hard synthetic functions. We test our algorithm against the d-dimensional Rastrigin, and d-dimensional Griewank functions, both satisfying our growth assumption. The global minimizer is at 0 for all d, with f(0) = 0. Rastrigin displays a much higher number of local minimizers than the Griewank function. We optimized these two functions with dimensions ranging from 2 to 200. The local solver uses gradient descent.

Lennard–Jones cluster. Let x1,...,xD ∈ R3 denote the positions of D ≥ 2 atoms. The Lennard–Jones energy is defined by

2 ∥xi − xj∥6

1 ∥xi − xj∥12

−

LJ(x1,...,xD) :=

.

1≤i<j≤D

The associated global optimization problem is of dimension d := 3D. The energy depends only on pairwise distances, and is therefore invariant under translations, rotations, and permutations. We optimized this function for 3 to 50 atoms. The local solver uses LBFGS steps.

Fitting scaling laws. Fitting scaling laws is an important problem in deep learning to predict model performance as a function of model size K and the number of tokens D. In particular, the choice of dataset mixtures is of crucial importance. To derive a good scaling law, the authors of [Shukor et al., 2025] collected training runs with different domain weights h (datasets), model sizes K, and token budgets D, and recorded the resulting loss on the target domain. Three scaling law models were tested in [Shukor et al., 2025] to understand optimal data mixtures [Shukor et al., 2025, Section 2.2]. The optimal parameters are estimated by minimizing a Huber objective over p observations. Finally, evaluation is performed on held-out runs with unseen triples (K,D,h) by comparing predicted and observed losses. The local solver uses LBFGS steps. The code for computing, fitting, and evaluating the scaling laws is reused from https://github.com/apple/ml-scalefit.

Numerical results. All the results displayed in this section are computed using 8 CPUs. We report final values, and not best achieved values, to highlight convergence capabilities and robustness. For the synthetic functions, we can see that the performance gap increases between PBH and BH when the dimension increases on the Rastrigin function, and stays consistent on the simpler Griewank function. ZOP did not converge on either functions: our hypothesis is that the number of samples needs to increase as δ decreases [Zhang et al., 2024, Section 5.2] in a much more constrained way than PBH. In our experiments, we saw that what matters at initialization is the scaling δγ: reducing δ at initialization would target smaller function values, but at the cost of exploration, thus γ should be increased accordingly. In this constrained budget setting, it appears that allocating more time to the exploration is not always useful: it is better to do more iterations with fewer samples. We display the results for the additive scaling law, for the three large deep learning models tested in [Shukor et al., 2025]: large language model (LLM), native multi-modal model (NMM), and large vision model (LVM). We report the results for the additive scaling law, that yielded the best test error. For almost all problems PBH with N = 5 is better than

![image 10](<2026-lauga-proximal-basin-hopping-global_images/imageFile10.png>)

![image 11](<2026-lauga-proximal-basin-hopping-global_images/imageFile11.png>)

![image 12](<2026-lauga-proximal-basin-hopping-global_images/imageFile12.png>)

Figure 2: Comparison of BH (orange), PBH (blue), and ZOP (green) on (left) Rastrigin, (middle) Griewank, and (right) Lennard–Jones: the ranking between algorithms is plotted (1 is best). N = 10 × d, 10 local steps, CPU time = 2 × d. When it does not appear, ZOP diverged. We set γ = 5 and δ = 0.5 at initialization. Rastrigin experiment ran in 18h, with 8 CPUs and 2GB of memory.

ZOP or BH (Table 1). Increasing the number of LBFGS steps did not yield better results (for PBH and BH), as increasing the number of samples (keeping CPU number fixed).

|Family Domain<br><br>|PBH (N=5) PBH (N=10) PBH (N=15)<br><br>|ZOP (N=5) BH|
|---|---|---|
|LLM (d = 19)<br><br>arxiv book c4 commoncrawl github stackexchange wikipedia|7.244 ± 4.369 6.848 ± 4.795 7.336 ± 5.859<br><br>3.671 ± 2.804 4.136 ± 2.778 3.752 ± 3.382<br><br>4.105 ± 3.225 4.528 ± 3.622 4.168 ± 3.460<br><br><br>3.964 ± 2.848 5.172 ± 3.235 4.009 ± 3.615<br><br>8.597 ± 7.418 9.899 ± 7.707 8.961 ± 8.241<br><br><br>6.109 ± 3.795 7.024 ± 4.270 6.374 ± 5.469 8.540 ± 5.088 9.484 ± 5.011 8.554 ± 5.340<br><br>|7.431 ± 7.533 10.037 ± 5.472<br><br>6.158 ± 6.523 4.915 ± 3.298<br>7.061 ± 6.521 6.977 ± 4.146 5.638 ± 6.520 6.843 ± 3.820<br><br><br>11.131 ± 9.351 13.191 ± 8.458 7.651 ± 6.644 8.640 ± 6.598 10.416 ± 6.524 13.898 ± 5.064|
|LVM (d = 13)<br><br>alttext<br><br>highquality1<br><br>highquality2 synthetic<br><br><br>|3.083 ± 3.745 6.037 ± 3.585 4.896 ± 3.674 5.753 ± 3.368 7.636 ± 3.903 6.474 ± 3.091 3.978 ± 2.948 8.189 ± 7.543 4.681 ± 7.894 11.384 ± 12.289 16.939 ± 13.689 11.302 ± 11.621<br><br>|6.354 ± 4.648 6.452 ± 4.459<br><br>14.093 ± 6.332 5.494 ± 3.799 14.201 ± 12.136 5.446 ± 4.691 24.611 ± 15.638 14.320 ± 7.138|
|NMM (d = 11)<br><br>captions interleaved text|3.725 ± 3.209 4.526 ± 3.400 4.074 ± 3.891 2.854 ± 1.329 3.299 ± 1.318 2.693 ± 1.470 2.387 ± 1.185 3.169 ± 1.320 2.341 ± 1.313<br><br>|8.698 ± 7.172 5.741 ± 4.222 6.176 ± 2.263 5.618 ± 2.622 4.500 ± 1.894 7.332 ± 3.689|


Table 1: Test MRE = |predictionobservation−observation| (%) for fitting additive scaling law. (lbfgs steps=5, CPU time=300s). We set γ = 10 and δ = 10−3 at initialization. Results averaged over three seeds, we report the standard deviation.

On average, PBH yields better test error than other algorithms. The standard deviation is also indicative of the best possible value reachable.

### 5 Conclusion, limitations and broader impact

Conclusion. In this paper, we present a new theoretical framework, Proximal Basin Hopping, from which we construct a practical algorithm outperforming state-of-the-art methods on various problems.

Limitations. With respect to the present convergence analysis, and the subsequent algorithm, a question can be raised about the fact that we aggregate points, instead of simply taking the best point every time. In this setting, we would lose the proximal interpretation which is vital for convergence to the global minimizer through the parameter γ, but the practical results may be better. It has been shown for the basin hopping algorithm that in some cases, better-tailored perturbation could improve optimization [Englander and Englander, 2014]. Here, if we steer away from a Gaussian distribution for the stochastic exploration, we also steer away from the proximal interpretation and the convergence analysis of our algorithm. However, a variable metric [Chouzenoux et al., 2014] is possible by using y ∼ N(xk,δγΣ) instead of y ∼ N(xk,δγId). It remains to choose Σ properly. Also, the impact of the inexactness of the local minimization should be investigated on a per-solver basis. A first step should be to investigate it for gradient flow. Significant work is required as the geometry of attraction basins should be described in far more detail than what we used here. Finally, if letting the number of samples be fixed

simplifies greatly the computations, it could be interesting to adapt the number of samples on the fly (notably with Proposition 3), to temporarily escape some traps, or reduce the computational load if progress continues.

Broader impact. The proposed method may help reduce the number of searches required to obtain global minimizer, and reduce the overall computational load.

### References

J. A. S. Alvarez and P. Calaminici. A review of global optimization methods for molecular structures: Algorithms, applications and perspectives. Journal of Computational Chemistry, 46(28):e70243, 2025.

J. S. Arora, O. A. Elwakeil, A. I. Chahande, and C. C. Hsieh. Global optimization methods for engineering applications: a review. Structural optimization, 9(3):137–159, 1995.

D. Asenjo, J. D. Stevenson, D. J. Wales, and D. Frenkel. Visualizing basins of attraction for different minimization

algorithms. The Journal of Physical Chemistry B, 117(42):12717–12723, 2013. M. Audin, M. Damian, and E. Erné. Morse theory and Floer homology, volume 2. Springer, 2014. W. Azizian, F. Iutzeler, J. Malick, and P. Mertikopoulos. What is the long-run distribution of stochastic gradient

descent? a large deviations analysis. In ICML 2024-41st International Conference on Machine Learning, pages 1–70, 2024.

W. Azizian, F. Iutzeler, J. Malick, and P. Mertikopoulos. The global convergence time of stochastic gradient descent in non-convex landscapes: Sharp estimates via large deviations. In International Conference on Machine Learning, pages 1982–2044. PMLR, 2025.

M. Baioletti, V. Santucci, and M. Tomassini. A performance analysis of basin hopping compared to established metaheuristics for global optimization. Journal of Global Optimization, 89(3):803–832, 2024.

C. Bouttier, T. Cesari, M. Ducoffe, and S. Gerchinovitz. Regret analysis of the Piyavskii-Shubert algorithm for global Lipschitz optimization. arXiv preprint arXiv:2002.02390, 2020.

E. Chouzenoux, J.-C. Pesquet, and A. Repetti. Variable metric forward–backward algorithm for minimizing the sum of a differentiable function and a convex function. Journal of Optimization Theory and Applications, 162

(1):107–132, 2014. P. L. Combettes and V. R. Wajs. Signal recovery by proximal forward-backward splitting. Multiscale modeling &

simulation, 4(4):1168–1200, 2005. M. Coste. An introduction to o-minimal geometry. 1999. B. de Souza. Goat: A global optimization algorithm for molecules and atomic clusters. Angewandte Chemie

International Edition, 64(18):e202500393, 2025. F. den Hollander. Large Deviations. American Mathematical Society, 2000. N. Di, E. C. Chi, and S. W. Fung. A monte carlo approach for nonsmooth convex optimization via proximal

splitting algorithms. arXiv preprint arXiv:2509.07914, 2025. A. C. Englander, J. A. Englander, and M. J. Carter. Hopping with an adaptive hop probability distribution. In Astrodynamics Specialist Meeting, 2020.

J. A. Englander and A. C. Englander. Tuning monotonic basin hopping: improving the efficiency of stochastic search as applied to low-thrust trajectory optimization. In International Symposium on Space Flight Dynamics 2014, number GSFC-E-DAA-TN14154, 2014.

J. F. Fernando. On the set of local extrema of a subanalytic function. Collectanea mathematica, 71(1):1–24, 2020. M. Fornasier, T. Klock, and K. Riedl. Consensus-based optimization methods converge globally. SIAM Journal on

Optimization, 34(3):2973–3004, 2024.

I. Goodfellow, Y. Bengio, A. Courville, and Y. Bengio. Deep learning, volume 1. MIT press Cambridge, 2016. M. Goodridge, J. Moriarty, J. Vogrinc, and A. Zocca. Hopping between distant basins. Journal of Global

Optimization, 84(2):465–489, 2022. A. Grosso, M. Locatelli, and F. Schoen. A population-based approach for hard global optimization problems based on dissimilarity measures. Mathematical Programming, 110(2):373–404, 2007. A. György and L. Kocsis. Efficient multi-start strategies for local search algorithms. Journal of Artificial Intelligence

Research, 41:407–444, 2011. B. Hajek. Cooling schedules for optimal annealing. Mathematics of operations research, 13(2):311–329, 1988. P. Hansen, B. Jaumard, and S.-H. Lu. Global optimization of univariate Lipschitz functions: I. Survey and

properties. Mathematical programming, 55(1):251–272, 1992. C. M. Kellett. A compendium of comparison function results. Mathematics of Control, Signals, and Systems, 26

(3):339–374, 2014. J. Kennedy and R. Eberhart. Particle swarm optimization. In Proceedings of ICNN’95-international conference on

neural networks, volume 4, pages 1942–1948. ieee, 1995. E. Kosygina and T. Mountford. Introductory examples and definitions. Cramér’s theorem, 2018. Lecture notes. A. Lambora, K. Gupta, and K. Chopra. Genetic algorithm-a literature review. In 2019 international conference

on machine learning, big data, cloud and parallel computing (COMITCon), pages 380–384. IEEE, 2019. G. Lauga and S. Vaiter. Characterizations of inexact proximal operators. working paper or preprint, January

2026. URL https://hal.science/hal-05449026. J. D. Lee, M. Simchowitz, M. I. Jordan, and B. Recht. Gradient descent only converges to minimizers. In Conference on learning theory, pages 1246–1257. PMLR, 2016. A. B. Levy. Attraction in numerical minimization: iteration mappings, attractors, and basins of attraction. Springer, 2018. A. B. Levy. Analyzing basins of attraction in numerical minimization. Set-Valued and Variational Analysis, 34(1): 6, 2026. M. Locatelli and F. Schoen. (global) optimization: historical notes and recent developments. EURO Journal on Computational Optimization, 9:100012, 2021. D. Morales, P. Pérez-Aros, and E. Vilches. Convergence rates for stochastic proximal and projection estimators. arXiv preprint arXiv:2602.06750, 2026.

G. Ochoa, S. Verel, F. Daolio, and M. Tomassini. Local optima networks: A new model of combinatorial fitness landscapes. In Recent advances in the theory and application of fitness landscapes, pages 233–262. Springer, 2014.

S. Osher, H. Heaton, and S. W. Fung. A hamilton–jacobi-based proximal operator. Proceedings of the National Academy of Sciences, 120(14), 2023.

L. Papenmeier, M. Poloczek, and L. Nardi. Understanding high-dimensional bayesian optimization. In Forty-Second

International Conference on Machine Learning, 2025. N. Parikh and S. Boyd. Proximal algorithms. Foundations and Trends in optimization, 1(3):127–239, 2014. M. C. Prentiss, D. J. Wales, and P. G. Wolynes. Protein structure prediction using basin-hopping. The Journal of

chemical physics, 128(22), 2008. Q. Rebjock and N. Boumal. Fast convergence to non-isolated minima: four equivalent conditions for c2 functions. Mathematical Programming, 213(1):151–199, 2025. R. T. Rockafellar and R. J.-B. Wets. Variational analysis, volume 317. Springer Science & Business Media, 2009.

C. Rohilla Shalizi. General theory of large deviations. Lecture notes, 36-754 Statistical Machine Learning, Carnegie Mellon University, 2006. URL https://www.stat.cmu.edu/~cshalizi/754/2006/notes/lecture-30.pdf. Chapter 30.

M. Shukor, L. Béthune, D. Busbridge, D. Grangier, E. Fini, A. El-Nouby, and P. Ablin. Scaling laws for optimal data mixtures. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025.

Y. Sun, Á. Baricz, and S. Zhou. On the monotonicity, log-concavity, and tight bounds of the generalized marcum

and nuttall q-functions. IEEE Transactions on Information Theory, 56(3):1166–1186, 2010. M. Tomassini. A local optima network view of real function fitness landscapes. Entropy, 24(5):703, 2022. D. J. Wales. Energy landscapes: some new horizons. Current Opinion in Structural Biology, 20(1):3–10, 2010. D. J. Wales and J. P. K. Doye. Global optimization by basin-hopping and the lowest energy structures of

lennard-jones clusters containing up to 110 atoms. The Journal of Physical Chemistry A, 101(28):5111–5116, 1997.

Z. B. Zabinsky. Random search algorithms. Department of Industrial and Systems Engineering, University of Washington, USA, 34, 2009.

M. Zhang, F. Han, Y. T. Chow, S. Osher, and H. Schaeffer. Inexact proximal point algorithms for zeroth-order global optimization. arXiv preprint arXiv:2412.11485, 2024.

### A Related works

Global optimization and zeroth-order methods. Global optimization has a long history, with most used methods being derived from some metaheuristics [Locatelli and Schoen, 2021]. A large part of this literature can be viewed as zeroth-order optimization, as the algorithms only query function values. The simplest one being pure random search, which samples candidate points and keeps the best value found [Zabinsky, 2009]. More structured deterministic zeroth-order methods include Lipschitz global optimization, but are typically limited by dimension [Hansen et al., 1992, Bouttier et al., 2020]. Multi-start local search is another way to combine global exploration and local descent, and its efficiency depends obviously on how starting points are allocated [György and Kocsis, 2011].

Genetic and evolutionary algorithms maintain and transform a population of candidate solutions through selection and variation mechanisms [Lambora et al., 2019]. Simulated annealing instead constructs a stochastic process whose ability to escape local minima is controlled by a temperature parameter; classical convergence guarantees require sufficiently slow cooling schedules [Hajek, 1988] if the number of states to investigate is finite. Particle swarm optimization updates a population of particles using both individual and collective best positions [Kennedy and Eberhart, 1995]. Consensus-based optimization is another population-based approach in which particles concentrate around weighted averages favoring low objective values; it is a more theoretically principled way of doing particles optimization, as global convergence under suitable assumptions was derived [Fornasier et al., 2024]. Bayesian optimization and related surrogate-based methods are highly effective in low to moderate dimension, but their behavior in high dimension remains delicate [Papenmeier et al., 2025].

Energy landscapes, basins, and local optima networks. A complementary line of work, that has attracted most of its attention from chemistry fields, studies the organization of nonconvex landscapes through their local minima and basins of attraction. Local optima networks encode local minimizers as nodes and transitions between them as edges, giving a graph representation of the landscape [Ochoa et al., 2014, Tomassini, 2022]. Such tools have been used to visualize and quantify funneling landscapes, in which local descent tends to guide configurations toward increasingly low-energy regions [Wales, 2010]. The structure of attraction basins evidently depends on the local solver: different minimization algorithms may induce different basins on the same objective [Asenjo et al., 2013]. This viewpoint is closely related to the study of iteration maps, attractors, and basins of attraction in numerical minimization [Levy, 2018, 2026].

Basin-hopping algorithms. Basin hopping was introduced for the global optimization of atomic cluster energies, in particular Lennard–Jones clusters [Wales and Doye, 1997]. The central idea is to compose random perturbations with local minimization, thereby transforming the original objective into an energy landscape over local minima. This transformation has proved especially effective in molecular and cluster optimization [Prentiss et al., 2008, Alvarez and Calaminici, 2025, de Souza, 2025]. Despite its practical success, this scheme has limited general convergence theory and is typically analyzed or tuned empirically.

Several variants of basin hopping have since been created, due to its success. Monotonic basin hopping accepts only moves that improve the objective and has been tuned for trajectory optimization problems [Englander and Englander, 2014]. Adaptive hopping strategies modify the perturbation distribution to improve transitions between promising regions [Englander et al., 2020]. Population-based basin hopping maintains several candidate solutions and uses dissimilarity or diversity mechanisms to explore multiple regions of the landscape [Grosso et al., 2007]. Recent comparisons show that basin hopping is competitive with established metaheuristics on global optimization benchmarks, but its performance remains problem dependent [Baioletti et al., 2024]. There is also theoretical work studying the difficulty of moving between distant basins [Goodridge et al., 2022].

Proximal algorithms and stochastic proximal approximations. Proximal algorithms are a central tool in convex and variational optimization [Combettes and Wajs, 2005, Parikh and Boyd, 2014, Rockafellar and Wets, 2009]. In convex settings, inexact proximal splitting methods remain convergent when the errors in the proximal evaluations are controlled, for instance by summability assumptions [Combettes and Wajs, 2005]. Recent work also studies Monte Carlo approximations of proximal steps for nonsmooth convex optimization [Di et al., 2025].

A Hamilton–Jacobi-based zeroth-order approximation of the proximal operator was proposed in [Osher et al., 2023]:

Ey∼N(x,δλI) [y exp(−f(y)/δ)] Ey∼N(x,δλI) [exp(−f(y)/δ)]

proxδλf(x) =

proxδλf(x). (18)

, proxλf(x) = lim δ↓0

Rates for such stochastic proximal and projection estimators have been investigated in [Lauga and Vaiter, 2026, Morales et al., 2026]. This approximation has also been used for zeroth-order global optimization in [Zhang et al., 2024], where an adaptive proximal-point scheme encourages exploration near non-global critical points. Their implementation estimates the expectation either by tensor-train methods or by Monte Carlo integration. The convergence argument relies on decreasing the smoothing parameter and increasing the number of samples sufficiently fast so that the accumulated proximal error remains controlled, for example through summability conditions [Zhang et al., 2024, Corollary 4].

### B Details about our algorithm

In practice. Instead of decreasing δ at each iteration, we adjust it on the fly: if the minimum value of f identified by the sampling mechanism has not lead to concentration on this minimum value, we decrease δ accordingly. This small tweak is a practical tradeoff given that we are using small sample sizes.

Furthermore, for numerical stability, the weighted mean is computed by substracting the maximum weight value, before computing the ratio. It is also done for the ZOP algorithm (for the same reasons). Proposition 4. Suppose that Assumptions 1, 2, and 3 hold. Let N ∈ N \ {0}, let {mi}1≤i≤N ∈ M∗, and assume that there exists 1 ≤ ix ≤ N such that f(mi

)◦. If δ is small enough, i.e., such that

) < f(mi) for all i ̸= ix, with mi

x ∈ B(mi,x,ri,x) ⊆ Att(mi

x

x

ri

e−∆/δ ≤

, (19)

x

(N − 1)max1≤i≤N ∥mi − mi

x∥

where ∆ = min1≤i≤N,i̸=i

), then

f(mi) − f(mi

x

x

N i=1 mi exp(−f (mi)/δ)

. (20)

= mi

Tf

N i=1 exp(−f (mi)/δ)

x

Proof. We note

N i=1 mi exp(−f (mi)/δ)

exp(−f (mi)/δ) N i=1 exp(−f (mi)/δ)

and λi =

mδ :=

N i=1 exp(−f (mi)/δ)

We need to show that mδ ∈ Att(mi

> 0 such that B(mi

) to conclude. mi

being in the interior of Att(mi

) there exist ri

x

x

x

x

). By taking this radius as large as possible, we upper bound the value of δ required. We want:

) ⊂ Att(mi

,ri

x

x

x

N

x ≤ ri

x ⇔

λimi − mi

i=1

N

λi(mi − mi

) ≤ ri

x

x

i=1,i̸=ix

Now,

N

N

λi(mi − mi

) ≤

λi∥mi − mi

x∥ ≤ (1 − λi

∥mi − mi

x∥.

) max

x

x

1≤i≤N

i=1,i̸=ix

i=1,i̸=ix

∆ is stricly greater than 0 by assumption. We have

1 1 + i̸=i

λi

=

,

x

exp(−(f (mi) − f(mi

))/δ)

x

x

hence,

1 − λi

x ≤

exp(−(f (mi) − f(mi

))/δ) ≤ (N − 1)exp(−∆/δ).

x

i̸=ix

Thus for concentration to occur, we need δ small enough so that e−∆/δ ≤

ri

x

.

(N − 1)max1≤i≤N ∥mi − mi

x∥

| |
|---|


reduces the mass on "bad" local minimizers while increasing the mass on the correct local minimizer. An other aspect that is not directly covered by Proposition 3 is the dependence on the dimension for α(ε). We can at least quantify the probability of eating the basin of attraction for one sample. It is reasonable to assume that we can fit a ball of non zero radius in each basin of attraction and we can estimate the probability of one sample being in this ball explicitly, and subsequently of at least one among N. We plot in Figure 3 an estimation of these probabilities with respect to the dimension and the number of samples.

###### This threshold on δ is a worst case, a multiplicity of mi

x

Lemma 4. Let x ∈ Rd, σ > 0 and Yσ ∼ N(x,σ2Id). Let r > 0. We have

r2 σ2

). (21) Moreover to have a probability 0 < α < 1 of one sample hitting this ball, we need

P(Yσ ∈ B(0,r)) = CDFX′

d(∥x∥2/σ2)(

Proof. We have

log(1 − α) log(1 − P(Yσ ∈ B(0,r)))

. (22)

N ≥

P(Yσ ∈ B(0,r)) = P(∥Yσ∥ ≤ r) = P(∥Yσ∥2 ≤ r2) = P(∥Yσ∥2/σ2 ≤ r2/σ2)

Now, ∥Yσ∥2/σ2 is the sum of d independent standard normal distributions, with non zero means. Hence, it is a non central chi-square distribution:

Therefore,

d

∥Yσ∥2 σ2 ∼ Xd′(λ), where λ =

i=1

µ2i σ2

. (23)

r2 σ2

P(Yσ ∈ B(0,r)) = CDFX′

).

d(λ)(

Setting α as the probability of one sample to be in this ball when drawing (yi)1≤i≤N samples of Yσ, it is defined as: P(∃ 1 ≤ i ≤ N,yi ∈ B(0,r)) = 1 − (1 − P(Yσ ∈ B(0,r)))N = α, which yields after a few rewriting:

log(1 − α) log(1 − P(Yσ ∈ B(0,r)))

. (24)

N ≥

| |
|---|


For instance, if P(Yσ ∈ B(0,r)) is small and α = 0.95 we obtain that N needs to be of the order N ≳

3 P(Yσ ∈ B(0,r))

. (25)

Therefore we can guarantee with high probability that we can identify basin of attractions of better local minimizers (from a local minimizer), provided that the number of samples is high enough. One should also be wary of the value of σ not to spread our samples to much. In order to quantify that more precisely we can use the fact that the cumulative distribution function of the non-central chi-squared distribution can be expressed with the generalized Marcum Q-function [Sun et al., 2010].

Lemma 5. Let x ∈ Rd \ {0}, σ > 0 and Yσ ∼ N(x,σ2Id). Let r > 0. The probability P(Yσ ∈ B(0,r)) is, with the other parameters fixed, strictly decreasing in the dimension d and the norm ∥x∥, and stricly increasing in the ratio r/σ. On the other hand, with other parameters fixed and ∥x∥ > r,

P(Yσ ∈ B(0,r)) = 0, (26) implying that there exists σ∗ such that

P(Yσ ∈ B(0,r)) = 0 and lim

lim

σ→+∞

σ→0

###### ∈ B(0,r)) ≥ P(Yσ ∈ B(0,r)) (27)

(∀σ > 0), P(Yσ

∗

![image 13](<2026-lauga-proximal-basin-hopping-global_images/imageFile13.png>)

![image 14](<2026-lauga-proximal-basin-hopping-global_images/imageFile14.png>)

Figure 3: Probability of being in a ball in the basin of x∗ and r2/σ2 = 1.

Proof. We have

r2 σ2

d(∥x∥2/σ2)(

CDFX′

) = 1 − Qd

2

∥x∥ σ

,

r σ

.

The first result follows from [Sun et al., 2010, Theorem 1(a)] as all parameters are strictly positive. The second one is immediate from the fact that ∥x∥ > r.

| |
|---|


### C Preliminary results and discussion of the assumptions

C.1 Assumptions on f

Finitely many minimizing components in any compact set. As stated, f is tame, meaning for any compact set K

- 1. K is definable in some o-minimal structure over R, and f|K : K → R is definable: the set of local minima is a definable subset of Rd [Fernando, 2020, Lemma 1.7] and definable subset have finitely many connected components [Coste, 1999, Section 3.2].
- 2. K is semi-algebraic, and f|K is semi-algebraic: semi-algebraic function are definable [Fernando, 2020].
- 3. K is globally subanalytic, and f|K is globally subanalytic: same as above [Fernando, 2020]
- 4. f|K is a Morse function, i.e., it is C2 with only isolated nondegenerate critical points [Audin et al., 2014].
- 5. f|K is a Morse-Bott function, i.e., it is C2, and each connected component of minima is a critical submanifold [Rebjock and Boumal, 2025]. This is the case of the Rastrigin function.


Graph of local minimizers. Following the basin hopping literature [Hajek, 1988, Wales, 2010, Tomassini, 2022], and some other recent works [Azizian et al., 2025], in practice we somehow assume that local minimizers of f can be represented with a graph. This assumption is however not required to prove convergence. Here, the edges depend on the local solver Tf in the following sense: for any local minimizer P ∈ M, the distance from p to the attractor of a better local minimizer Q (in the sense that f(P) > f(Q)) is uniformly bounded for all P.

Assumption 7. For all P ∈ M \ {x∗}, there exists Q ∈ M such that

dist(x,Att(Q)) ≤ df < +∞ and f(P) > f(Q) (28)

sup

x∈P

Hence, we construct our graph with vertices as local minimizers (or connected components of local minimizers) and a directed edge between two vertices P and Q if dist(P,Att(Q)) ≤ df. The edge is undirected if also dist(Q,Att(P)) ≤ df. From this assumption, the global minimizer x∗ is reachable by "simply" jumping from one local minimizer to a better local minimizer. This assumption is implicitly made in basin hopping optimization so that random perturbations can reach the basin of a better local minimizer [Goodridge et al., 2022].

We can numerically compute an upper bound of df (Assumption 7) for the 1 − D Rastrigin function only has isolated local minimizers, and isolated local maximizers:

Ras(x) = x2 + 10(1 − cos(2πx)), (29) which are solutions of

x 10π

= −sin(2πx).

These solutions can be computed numerically and are approximately away from each other by a little less than 0.5, hence df = 12 is a valid upper bound in this case.

#### C.2 Properties of the solver

The definition of the solver in the main body of the paper contains only the relevant assumption to derive our analysis, we lay here a more detailed presentation of what these assumptions entail. Assume that f is C2-smooth (with Lipschitz continuous gradient). Let us define φ : [0,+∞),Rd  → Rd the gradient flow mapping any x ∈ Rd to a local minimizer of f:

φ(0,x) = x φ(t,x) = −∇f(φ(t,x))

(30) Define the critical components of f as:

critf := x ∈ Rd,0 = ∇f(x) (31)

and we assume it is composed of infinitely many connected components. Following this definition, we have for any component C ∈ critf that

Att(C) := x ∈ Rd, lim

dist(φ(t,x),C) = 0 . (32)

t→+∞

[Azizian et al., 2024, Lemma D.28] holds in our context and thus for any x ∈ Rd, there exists C ∈ critf such that lim

d(φ(t,x),C) = 0. (33)

t→+∞

The proof is immediate from [Azizian et al., 2024, Lemma D.28], as f is coercive and the components C are connected. The finiteness of the number of components is not important, their connectedness is. M is the set of asymptotically stable critical components [Azizian et al., 2024, Lemma D.29] (again the proof does not rely on finiteness of critical components), implying that for all M ∈ M, Att(M) is open. Under standard assumptions [Lee et al., 2016] any C ∈ critf \ M, Att(C) is of measure 0.

#### C.3 Some preliminary results related to the local minimizers

We start this presentation by listing some important properties of the local minimizers and their attractor sets. Lemma 6. Suppose that Assumptions 1, 3, and 5 hold. The sets {Att(M)}M∈M form a measurable partition of Rd up to a null set.

Proof. First, the sets of attractors of critical points who are non local minimizers is of measure 0. Let us denote by N this set of points which are not attracted by a local minimizer through Tf. We have for all y ∈ Rd \ N, Tf(y) ∈ M∗ and more precisely, there exists a unique M ∈ M such that Tf(y) ∈ M as the M are pairwise disjoints. Hence, for any P,Q ∈ M, Att(P) ∩ Att(Q) = ∅, and

Att(Mj) = Tf−1(M∗) = Rd \ N. (34)

j

As Tf is measurable and every M is Borel by assumption, we get the desired result. Lemma 7. Let x ∈ Rd. For every η > 0, there exists a finite subset Kη ⊂ M such that

| |
|---|


Vx( M) + η. (35)

Vx(M) ≥ inf

inf

M∈M\Kη

M∈M

Proof. Since dist(x,Att(M))2 ≥ 0, one has

Vx(M) ≥ f(M), M ∈ M. Set

Vx(M). By coercivity of f, there exists Rη > 0 such that

αx := inf

M∈M

∥y∥ ≥ Rη =⇒ f(y) ≥ αx + η. Let

Kη := {M ∈ M : M ∩ B(0,Rη) ̸= ∅}.

Since B(0,Rη) is compact and only finitely many elements of M intersect a compact set, Kη is finite. Let M ∈ M \ Kη. Then M ∩ B(0,Rη) = ∅, so for every m ∈ M one has ∥m∥ > Rη. Hence f(M) = f(m) ≥ αx + η. Therefore Vx(M) ≥ f(M) ≥ αx + η. Taking the infimum over M ∈ M \ Kη gives

Vx(M) ≥ αx + η = inf

Vx( M) + η.

inf

M∈M\Kη

M∈M

| |
|---|


Any finite subset of M is automatically bounded by boundedness of every elements of M and they have a positive value gap with inf Vx. Fact 1. Let x ∈ Rd, αx := infM∈M Vx(M), ε > 0, and

M, and (Mx)ε = z ∈ Rd, dist(z,Mx) < ϵ .

Mx =

M∈Sfγ(x)

Let R > 0. On B(0,R) there exists a positive gap of Vx between M ∈ Sfγ(x) and every other M that intersects B(0,R), i.e., there exists cR,ε > 0 such that for every M in

Mx,R,ε := M ∈ M, M ∩ B(0,R) ̸= ∅, M ∩ ((Mx)ε)∁ ̸= ∅ , Vx(M) ≥ αx + cR,ϵ.

Lemma 8. Suppose that Assumptions 1, 2, 3, and 5 hold. Let x ∈ Rd and δ,γ > 0. If one of the conditions below hold

- • There exist C1,C2,C3 > 0 and 0 < α < β such that (∀z ∈ Rd), C1∥z∥α − C2 ≤ f(z) ≤ C3(1 + ∥z∥)β. (36)
- • M has finitely many components. Then, Tf : Rd → M∗ is integrable and square integrable against the Gaussian distribution, i.e.,


−1

2γδ∥y−x∥2dy < +∞, and

∥Tf(y)∥e

Rd

−1

2γδ∥y−x∥2dy < +∞ (37)

∥Tf(y)∥2e

Rd

Proof. Let us consider the second case first. Denote by J the number of components of M. Then M∗ = Jj=1 Mj. By assumption any M ∈ M is bounded. Thus there exists some R > 0 such that M∗ ⊂ B(0,R). Hence,

∥y−x∥2

∥y−x∥2

∥Tf(y)∥e−

e−

2δγ dy ≤ R

2δγ dy < +∞.

Rd

Rd

Now to the first case. We have for all z ∈ Rd, f(z) ≥ f(Tf(z)), therefore C1∥Tf(z)∥α − C2 ≤ f(Tf(z)) ≤ f(z) ≤ C3(1 + ∥z∥)β

and,

∥Tf(z)∥ ≤ C1−1/α C2 + C3(1 + ∥z∥β) 1/α . Hence,

∥y−x∥2

∥y−x∥2

C1−1/α C2 + C3(1 + ∥y∥β) 1/α e−

∥Tf(y)∥e−

2δγ dy < +∞. The square case follows immediately from the same arguments.

2δγ dy ≤

Rd

Rd

| |
|---|


Assumption 6 and the first condition in Lemma 8 imply that f has polynomially bounded growth. This is slightly stronger than coercivity and is akin to the notion of radially unbounded function in control theory4 [Kellett, 2014].

Lemma 9. Suppose that Assumptions 1, 3, 5, and 6 hold. Let x ∈ Rd, Yδ ∼ N(x,γδId), q > 0 and r > 0. We have:

(r − ∥x∥2)+ 2γ

δ log E (1 + ∥Yδ∥q)1{∥Y

. (38)

δ∥>r} ≤ −

limsup

δ↓0

Proof. We have

∥y − x∥2 2γδ

1 (2πδγ)d/2 {∥y∥>r}

E (1 + ∥Yδ∥q)1{∥Y

(1 + ∥y∥q)exp −

δ∥>r} =

dy.

Fix R > r. Splitting the domain gives {∥y∥ > r} = {r < ∥y∥ ≤ R}∪{∥y∥ > R}, hence we can split the expectation in

Iδ(r) := E (1 + ∥Yδ∥q)1{∥Y

δ∥>r} = Iδ,1(r,R) + Iδ,2(R), where

1 (2πδγ)d/2 {r<∥y∥≤R}

∥y−x∥2

(1 + ∥y∥q)e−

Iδ,1(r,R) :=

2γδ dy

and

1 (2πδγ)d/2 {∥y∥>R}

∥y−x∥2

(1 + ∥y∥q)e−

2γδ dy.

Iδ,2(R) :=

On the bounded region {r < ∥y∥ ≤ R}, we have 1 + ∥y∥q ≤ 1 + Rq. Moreover, if ∥y∥ > r, then ∥y − x∥ ≥ ∥y∥ − ∥x∥ ≥ (r − ∥x∥)+. Therefore

(r − ∥x∥)2+ 2γδ

(1 + Rq)λd(B(0,R)) (2πδγ)d/2

Iδ,1(r,R) ≤

exp −

.

Since δ log(δ−d/2) → 0, it follows that

limsup

δ↓0

(r − ∥x∥)2+ 2γ

δ log Iδ,1(r,R) ≤ −

.

∥y−x∥2 2γδ

(R−∥x∥)2

∥y−x∥2

Now onto Iδ,2(R). Assume R > ∥x∥. For ∥y∥ > R, ∥y − x∥ ≥ R − ∥x∥, hence e−

≤ e−

4γδ e−

4γδ . Thus

1 (2πδγ)d/2 Rd

(R−∥x∥)2 4γδ

∥y−x∥2

Iδ,2(R) ≤ e−

(1 + ∥y∥q)e−

4γδ dy.

Using ∥y∥q ≤ max{1,2q−1}(1 + ∥y − x∥q + ∥x∥q), we obtain 1 + ∥y∥q ≤ C(1 + ∥y − x∥q) for some constant C > 0. Hence

1 (2πδγ)d/2 Rd

(R−∥x∥)2 4γδ

∥y−x∥2

Iδ,2(R) ≤ Ce−

(1 + ∥y − x∥q)e−

4γδ dy.

√

Making the change of variables z = (y−x)/

δ, we obtain that the righthandside integral is in O(δd/2)+O(δ(d+q)/2) hence bounded uniformly for δ ∈ (0,1]. Therefore there exists CR > 0 such that

(R−∥x∥)2

Iδ,2(R) ≤ CRe−

4γδ ,

###### 4In this setting, ψ is also required to be positive [Kellett, 2014, Section 2].

and thus

(R − ∥x∥)2 4γ

δ log Iδ,2(R) ≤ −

. Finally,

limsup

δ↓0

δ log Iδ(r) ≤ max limsup

limsup

δ log Iδ,2(R) . Hence

δ log Iδ,1(r,R), limsup

δ↓0

δ↓0

δ↓0

(r − ∥x∥)2+ 2γ

(R − ∥x∥)2 4γ

, −

δ log Iδ(r) ≤ max −

. Choosing R > r large enough so that

limsup

δ↓0

(r − ∥x∥)2+ 2γ

(R − ∥x∥)2 4γ

, we conclude that

>

(r − ∥x∥)2+ 2γ

δ log E (1 + ∥Yδ∥q)1{∥Y

δ∥>r} ≤ −

limsup

.

| |
|---|


δ↓0

Remark 1. Evolution of the set Mx with respect to γ. There exists approximately three regimes. When γ is small, Vx heavily penalizes distant local minimizers hence its arg min is more likely to contain one unique solution. Slowly increasing γ makes it more likely that several competitors M can arise. Then as γ increases more, Vx is more likely to select a unique better local minimizer.

The first regime is characterized in the next Lemma.

Lemma 10. Suppose that Assumptions 1, 2, 3, 7, and 5 hold. Let x ∈ Rd, γ > 0, and P ∈ M the closest (w.r.t. to Att(P)) minimizing component. Denote by Q the closest (w.r.t. Att(Q)) better local minimizing component of P in the sense of Assumption 7. If:

dist(x,Att(Q))2 − dist(x,Att(P))2 2(f(P) − f(Q))

(39)

γ <

then,

Vx(M). (40)

P = arg min

M∈M

Proof. We have that for all M ∈ M \ {Q} such that dist(x,Att(M)) ≤ df then f(M) > f(Q). Furthermore, by Assumption 7, any better local minimizer in the vicinity of P has function value equal to that of Q in a radius df, hence we just need to make sure that Q does not belong in the arg min, giving immediately the positive upper bound on γ.

| |
|---|


These scenarios where we have a series of equally distant and of equal function values are not possible indefinitely, first because there is a unique global minimizer, and second because the function f is coercive so it needs to grow to infinity, thus contradicting the existence of these increasingly distant local minimizers of decreasing function values.

### D Proofs of Section 3: Proposed method

#### D.1 Proofs for ideal basin hopping

Proof of Lemma 1 Proof. We have for all x ∈ Rd

- 1

- 2γ ∥y − x∥2 + f(T(y)), and


proxγf◦T

(x) = arg min

f

y∈Rd

1 2γ

Sfγ(x) := arg min

dist(x,Att(M))2 + f(M).

M∈M

Looking more closely at the first optimization problem, we have min

1 2γ ∥y − x∥2 + f(T(y)) = min

1 2γ

dist(x,Att(M))2 + f(M).

y∈Rd

M∈M

Hence, if for every M ∈ Sfγ(x), projAtt(M)(x) ∩ Att(M) ̸= ∅, proxγf◦T

projAtt(M)(x),

(x) =

f

M∈arg minM∈M 21γ dist(x,Att(M))2+f(M)

where proj denotes the orthogonal projection. Thus, as Tf maps to M, we recover

1 2γ

dist(x,Att(M))2 + f(M).

Tf(proxγf◦T

(x)) = arg min

f

M∈M

| |
|---|


Proof of Lemma 2 Proof. Let x ∈ Rd. We have that for all γ > 0.

Sfγ(x) = arg min

M∈M

Hence,

1 2γ

dist(x,Att(M))2 + f(M).

x∗ ∈ Sfγ(x) ⇔ ∀M ∈ M,

⇔ ∀M ∈ M,

1 2γ

1 2γ

dist(x,Att(x∗))2 + f(x∗) ≤

dist(x,Att(M))2 + f(M)

1 2µ

dist(x,Att(x∗))2 − dist(x,Att(M))2 ≤ γ,

where the last inequality was obtained using Assumption 2. The minimal required value of γ depends on the close and achievable minimizers. Indeed, all minimizing components such that dist(x,Att(x∗))2 − dist(x,Att(M))2 ≤ 0 yields no constraint on γ.

| |
|---|


###### Proof of Theorem 1.

Proof. First iterations are well defined as Sfγ is non-empty and bounded (Assumption 5, Lemma 1). Second, if for any K ∈ N, xK = x∗ then xk = x∗ for all k > K. Finally, by construction f(xk+1) ≤ f(xk), hence by coercivity of f (Assumption 1), the iterates are bounded. Denote by B0 this bounded set. We can guarantee that there exists only finitely many failed iterations (where f(x+) = f(xk)).

Indeed, by boundedness of the iterates, there exists df ≥ 0 such that for all k ∈ N, dist(xk,Att(x∗)) ≤ df. Let P ∈ M, such that P ∩ B0 ̸= ∅ and P ̸= {x∗}. We have for any x ∈ P, Vx(x∗) < Vx(P) if

dist(x,Att(x∗))2 2γ

+ fmin < f(P)

2 f

2 f

which happens if γ > d

2(f(P)−fmin). Thus, taking the infimum over all P not equal to {x∗}, we have γs ≥ d

2µ implies that for all x ∈ B0, x∗ ∈ Sγ

f (x). Let K ∈ N. For any γ > 0, γηK ≤ γs ⇔K log(η) ≤ log

s

γs γ

log (γs/γ) log(η) Therefore, after at most log(γ

⇔K ≤

s/γ) log(η)

failed iterations, x∗ belongs to Sfγ.

+

Now, by boundedness of the iterates, only finitely many M ∈ M can be visited. Hence, we conclude that convergence occurs in a finite number of iterations.

| |
|---|


#### D.2 Proofs for exact expectation basin hopping

Proof of Lemma 3. Proof. By the small-noise Gaussian large deviation principle with speed δ−1, and rate function Ix(y) = 21γ∥y −x∥2, for every Borel set A ⊂ Rd [den Hollander, 2000], 5

δ log P(Yδ ∈ A) ≤ limsup

δ log P(Yδ ∈ A) ≤ − inf

− inf

Ix(y) ≤ liminf

Ix(y).

y∈A◦

δ↓0

y∈A

δ↓0

Applying this with A = Att(M) yields

1 2γ ∥y − x∥2 ≤ liminf

δ log P(Yδ ∈ Att(M))

− inf

y∈Att(M)◦

δ↓0

- 1

- 2γ ∥y − x∥2. Which is equivalent to


δ log P(Yδ ∈ Att(M)) ≤ − inf

≤ limsup

δ↓0

y∈Att(M)

1 2γ

dist(x,Att(M)◦)2 ≤ liminf

δ log P(Yδ ∈ Att(M))

−

δ↓0

1 2γ

dist(x,Att(M))2.

δ log P(Yδ ∈ Att(M)) ≤ −

≤ limsup

δ↓0

By the regularity assumption the lower and upper bounds coincide, and hence

1 2γ

dist(x,Att(M))2.

δ log P(Yδ ∈ Att(M)) = −

lim

δ↓0

This proves the first claim. The equivalent exponential form follows immediately: if a scalar quantity aδ satisfies δ log aδ → −c, then aδ = exp −1δ[c + o(1)] (see [Shalizi, 2006, Definition 401]).

| |
|---|


First case: finite number of minimizers. If there are finitely many sets of local minimizers, then we can obtain an explicit concentration result inside the convex hull defined by the solutions in Mx (Fact 1), when δ goes to 06.

Proposition 5. Let x ∈ Rd, γ > 0, δ > 0, and let Yδ ∼ N(x,δγId). Suppose that M has finitely many components, i.e.,

Mj (41)

M∗ =

1≤j≤J

for some J ∈ N. Denote by Ix the set of indices of the minimizers of fj + 21γdist(x,Att(Mj))2

, i.e., Ix ⊆ {1,...,J}. Then,

1≤j≤J

i/δP(Yδ ∈ Att(Mi))E[Tf(Yδ)|Yδ ∈ Att(Mi)] i∈Ix e−fi/δP(Yδ ∈ Att(Mi))

i∈Ix e−f

E[Tf(Yδ)e−f(T

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ] −−→

.

δ↓0

If Ix is a singleton {ix}, and Mi

x} contains an isolated local minimizer then, E[Tf(Yδ)e−f(T

= {mi

x

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ] −−→

mi

.

x

δ↓0

Proof. Since the local minimizers reached by Tf decompose into the finite disjoint union M, the sets (Attj)1≤j≤J form a measurable partition of the subset of Rd on which Tf will land in M. Denoting fj the value of f attained

- 5The small-noise Gaussian rate function can be identified directly from the explicit normal example in [Kosygina and Mountford, 2018, pp.4–5] with Xn ∼ N(0, 1/n) , which yields the rate function I(x) = x2/2, and cf. [den Hollander, 2000, Exercise III.9, p.30].
- 6This result is similar in spirit to [Zhang et al., 2024, Corollary 1] even though proofs are completely different


on Mj, we have

E[Tf(Yδ)e−f(T

f(Yδ))/δ] =

=

=

J

E[Tf(Yδ)e−f(T

f(Yδ))/δ1{Y

δ∈Att(Mj)}]

j=1

J

e−f

j/δE[Tf(Yδ)1{Y

δ∈Att(Mj)}]

j=1

J

e−f

j/δP(Yδ ∈ Att(Mj))E[Tf(Yδ)|Yδ ∈ Att(Mj)].

j=1

Moreover, using Lemma 3, we obtain that

δ log e−f

j/δP(Yδ ∈ Att(Mj)) =δ→0 −fj −

1 2γ

dist(x,Att(Mj))2,

implying

1 2γ

1 δ

e−f

dist(x,Att(Mj))2 + o(1) . Now, take the set Ix. For all i ∈ Ix, and j ∈ J \ Ix, we have

j/δP(Yδ ∈ Att(Mj)) =δ→0 exp −

fj +

i/δP(Yδ ∈ Att(Mi)) e−fj/δP(Yδ ∈ Att(Mj)) −−→

e−f

1 2γ

1 2γ

dist(x,Att(Mj))2 − fi −

dist(x,Att(Mi))2 > 0

δ log

fj +

δ↓0

implying that

i/δP(Yδ ∈ Att(Mi)) e−fj/δP(Yδ ∈ Att(Mj))

e−f

= +∞. Hence, we obtain that

lim

δ→0

j/δP(Yδ ∈ Att(Mj)) j∈J e−fj/δP(Yδ ∈ Att(Mj))

j∈J\Ix e−f

lim

= 0.

δ→0

The rest follows from the fact that no connected components of M is unbounded, guaranteeing that E[Tf(Yδ)|Yδ ∈ Att(Mj)] is bounded for all j.

| |
|---|


This result highlights the need for the uniqueness of the global minimizer: the barycenter of several global minimizers does not make any sense unless these global minimizers belong to the same connected and convex set.

Proof of Proposition 1. Proof. Fix η > 0, and let Kη ⊂ M∗ be a bounded set such that (Lemma 7)

Vx(m) ≥ αx + η.

inf

m/∈Kη

Set

Aη := {y ∈ Rd : Tf(y) ∈ Kη∁}. We look at our measure outside this bounded set

νx,δ(Kη∁) = E e−f(T

f(Yδ))/δ1{T

f(Yδ)∈Kη∁}

f(Tf(y)) + ∥y − x∥2 2γ

1 (2πδγ)d/2 A

1 δ

exp −

=

η

dy.

2

2γ . If y ∈ Aη, then Tf(y) ∈ M ∈ Kη∁, and since y ∈ Att(M),

We first study the term in the exponential. Set g(y) = f(Tf(y)) + ∥y−x∥

dist(x,Att(M))2 2γ

∥y − x∥2 2γ ≥

.

Hence,

g(y) = f(M) + ∥y − x∥2 2γ ≥ f(M) +

dist(x,Att(M))2 2γ

= Vx(M) ≥ αx + η. Therefore, infy∈A

g(y) ≥ αx + η. Now, to estimate the measure, we split our set with a ball of radius R > 0 in the following way:

η

Aη = (Aη ∩ B(0,R)) ∪ Aη ∩ B(0,R)∁ . The measure on the lefthandside of the union is easily bounded by the previous inequality as we have, 1 (2πδγ)d/2 A

λd(B(0,R)) (2πδγ)d/2

e−g(y)/δ dy ≤

e−(α

x+η)/δ.

η∩B(0,R)

Since

δ log δ−d/2 −−→

0, it follows that

δ↓0

1 (2πδγ)d/2 A

e−g(y)/δ dy ≤ −(αx + η).

limsup

δ log

η∩B(0,R)

δ↓0

f is bounded from below on Rd, hence all y,

g(y) ≥ fmin + ∥y − x∥2 2γ

.

Thus

∥y − x∥2 2γδ

1 (2πδγ)d/2 A

min/δ 1 (2πδγ)d/2 B(0,R)∁

e−g(y)/δ dy ≤ e−f

exp −

η∩B(0,R)∁

The last term is exactly

e−f

min/δ P(∥Yδ∥ > R). We can take R > ∥x∥, large enough so that

(R − ∥x∥)2 2γ

fmin +

> αx + η.

dy.

Since ∥y − x∥ ≥ R − ∥x∥ whenever ∥y∥ > R, the Gaussian tail satisfies [den Hollander, 2000]

(R − ∥x∥)2 2γ

δ log P(∥Yδ∥ > R) ≤ −

limsup

,

δ↓0

and therefore

(R − ∥x∥)2 2γ

δ log e−f

min/δP(∥Yδ∥ > R) ≤ −fmin −

< −(αx + η).

limsup

δ↓0

Combining the estimates on Aη ∩ B(0,R) and Aη ∩ B(0,R)∁, we obtain limsupδ↓0 δ log νx,δ(Kη∁) ≤ −(αx + η). We now lower bound the denominator. Let ε > 0. By definition of αx, there exists Mε ∈ M such that

Vx(Mε) ≤ αx + ε. Then

νx,δ(M) = E e−f(T

f(Yδ))/δ ≥ e−f(m

ε)/δP(Yδ ∈ Att(Mε)). By Lemma 3,

1 2γ

dist(x,Att(Mε))2, hence

δ log P(Yδ ∈ Att(Mε)) = −

lim

δ↓0

1 2γ

dist(x,Att(Mε))2 = −Vx(Mε) ≥ −(αx + ε).

δ log νx,δ(M) ≥ −f(Mε) −

liminf

δ↓0

Letting ε ↓ 0 gives

δ log νx,δ(M) ≥ −αx. Finally,

liminf

δ↓0

νx,δ(Kη∁) νx,δ(M)

µx,δ(Kη∁) =

, so

δ log µx,δ(Kη∁) ≤ −(αx + η) − (−αx) = −η. In particular, µx,δ(Kη∁) → 0, that is, µx,δ(Kη) → 1. Proof of Proposition 6. Proposition 6. Let x ∈ Rd, γ > 0, q ≥ 0, and let Yδ ∼ N(x,δγId). Let R > 0. We have

limsup

δ↓0

1/β

C1Rα−C2−C3 C3

− ∥x∥2

+

+

δ log E[∥Tf(Yδ)∥e−f(T

f(Yδ))/δ1{∥T

f(Yδ)∥>R}] ≤ −fmin −

limsup

,

2γ

δ↓0

and that

δ log E[e−f(T

f(Yδ))/δ] ≥ −αx. Then,

liminf

δ↓0

| |
|---|


limsup

δ log

δ↓0

1/β

C1Rα−C2−C3 C3

− ∥x∥2

E[∥Tf(Yδ)∥e−f(T

f(Yδ))/δ1{∥T

f(Yδ)∥>R}] E[e−f(Tf(Yδ))/δ] ≤ αx − fmin −

+

+

.

2γ

Proof. We have that

E[Tf(Yδ)e−f(T

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ]

is well defined. Indeed, 0 ≤ E[e−f(T

min/δ < +∞ and E[∥Tf(Yδ)∥e−f(T

min/δE[∥Tf(Yδ)∥] <

f(Yδ))/δ] ≤ e−f

f(Yδ))/δ] ≤ e−f

+∞ by Lemma 8. Using our measure introduced in Proposition 1 we have E[Tf(Yδ)e−f(T

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ]

=

mdµx,δ(m)

m∈M∗

Using similar arguments than in the proof of Lemma 8 we can have that m  → ∥m∥ is integrable against µx,δ. We have

E[∥Tf(Yδ)∥e−f(T

f(Yδ))/δ1{∥T

f(Yδ)∥>R}] E[e−f(Tf(Yδ))/δ]

∥m∥dµx,δ(m) =

m∈M∗,∥m∥>R

As

min/δE[C1−1/α C2 + C3(1 + ∥Yδ∥β) 1/α 1∥T

E[∥Tf(Yδ)∥e−f(T

f(Yδ)∥>R] ≤ e−f

f(Yδ))/δ1∥T

f(Yδ)∥>R], and,

implying that

R < C1−1/α C2 + C3(1 + ∥Yδ∥β) 1/α ⇔

1/β

C1Rα − C2 − C3 C3

< ∥Yδ∥,

{∥Tf(Yδ)∥ > R} ⊂ ∥Yδ∥ >

(C1Rα − C2 − C3)+ C3

1/β

###### .

Therefore,

E[∥Tf(Yδ)∥e−f(T

f(Yδ))/δ1∥T

f(Yδ)∥>R] ≤ e−f

###### min/δE C1−1/α C2 + C3(1 + ∥Yδ∥β) 1/α 1

∥Yδ∥> Rα−CC2−C3

3

1/β

We can show that there exists C2,α,C3,α > 0 such that

C1−1/α C2 + C3(1 + ∥Yδ∥β) 1/α ≤ C2,α + C3,α(1 + ∥Yδ∥β/α).

1/β

1Rα−C2−C3 C3

Now, using Lemma 9 with q = β/α and r = C

we have

(r − ∥x∥2)+ 2γ

δ log E C1−1/α C2 + C3(1 + ∥Yδ∥β) 1/α 1{∥Y

δ∥>r} ≤ −

limsup

.

δ↓0

The lower bound was already shown in Proposition 1. Hence the result. Lemma 11. Let x ∈ Rd, γ,δ > 0, ε > 0 and Yδ ∼ N(x,δγId). Let R > 0. We have

| |
|---|


δ log µx,δ ((Mx)ε)∁ ∩ B(0,R) ≤ −cR,ε. (42)

limsup

δ↓0

Therefore for sufficiently large R

δ log µx,δ ((Mx)ε)∁ < 0. (43) hence,

limsup

δ↓0

µx,δ ((Mx)ε)∁ −−→

1 (44)

0, and µx,δ (((Mx)ε)) −−→

δ↓0

δ↓0

Proof. We have

E e−f(T

f(Yδ))/δ1{Tf(Yδ)∈((Mx)ε)∁∩B(0,R)}

µx,δ ((Mx)ε)∁ ∩ B(0,R) =

E e−f(Tf(Yδ))/δ and, there exists some set Mx,R,ε (Fact 1) such that

Tf(Yδ) ∈ ((Mx)ε)∁ ∩ B(0,R) ⊂ Mx,R,ε. Hence,

E e−f(T

e−f(M)/δP(Yδ ∈ Att(M)),

f(Yδ))/δ1{Tf(Yδ)∈((Mx)ε)∁∩B(0,R)} ≤

M∈Mx,R,ε

which is sufficient to conclude for the first inequality by applying Lemma 3. The second inequality comes from the fact that

µx,δ ((Mx)ε)∁ ≤ µx,δ ((Mx)ε)∁ ∩ B(0,R) + µx,δ(B(0,R)∁), where the second complement is taken in M∗. We apply Proposition 1 to obtain the desired result. If R is large enough then it means that the mass outside the ball B(0,R) goes to 0 when δ ↓ 0.

| |
|---|


Proof of Proposition 2. Proof. Fix ε > 0 and R > 0. For convenience, we write

E[Tf(Yδ)e−f(T

f(Yδ))/δ] E[e−f(Tf(Yδ))/δ]

mδ :=

Since the distance to a closed convex set is a convex function, Jensen’s inequality gives

dist(mδ,conv(Mx)) = dist

z µδ,x(dz),conv(Mx)

M∗

≤

dist(z,conv(Mx)) µδ,x(dz).

M∗

We split the integral over the three regions (Mx)ε ∩ B(0,R), B(0,R) \ (Mx)ε, and B(0,R)∁. If z ∈ (Mx)ε, then since Mx ⊂ conv(Mx), dist(z,conv(Mx)) ≤ dist(z,Mx) < ε. If z ∈ B(0,R) \ (Mx)ε, then dist(z,conv(Mx)) ≤ ∥z∥ ≤ R. If ∥z∥ > R, then dist(z,conv(Mx)) ≤ ∥z∥. Therefore,

dist(mδ,conv(Mx)) ≤ ε + R µδ,x ((Mx)ε)∁ +

∥z∥1{∥z∥>R} µδ,x(dz).

M∗

Now let δ ↓ 0. By Lemma 11 ,

µδ ((Mx)ε)∁ → 0, hence

∥z∥1{∥z∥>R} µδ,x(dz). Next let R → ∞ and use Lemma 6 on the righthandside integral to obtain

dist(mδ,conv(Mx)) ≤ ε + limsup

limsup

δ↓0

δ↓0 M∗

dist(mδ,conv(Mx)) ≤ ε.

limsup

δ↓0

Since ε > 0 is arbitrary, this proves

dist(mδ,conv(Mx)) −−→

0. The limit in the isolated local minimizer case follows immediately.

δ↓0

| |
|---|


Proof of Theorem 2. Proof. First, by rejecting worse update and coercivity of f (Assumption 1), iterates are bounded and stay in some bounded set B ⊂ Rd. Thus

dist(x,Att(x∗)) < +∞. Set γ > 0. For every x ∈ B,

df := sup x∈B

1 2γ

d2f + fmin

Vx(x∗) ≤

2 f

If γ > d

2µ then, for all M ̸= x∗,

Vx(x∗) < fmin + µ ≤ Vx(M). Meaning that for γ sufficiently large, by Proposition 2 there exists δ > 0 and r > 0 such that for all δ ≤ δ

∥mδ,γ − x∗∥ ≤ r.

Therefore, if there exists r > 0, such that B(x∗,r) ⊂ Att(x∗), then x+ = x∗. Such statement holds in our context as x∗ is an isolated local minimizer, reached by Tf. We thus obtain immediate convergence if γ is large enough and δ small enough.

Now there are several scenarios:

- • if progress (i.e., strict decrease) is made at every iteration, as iterates are bounded, we visit finitely many M ∈ M until convergence (see proof of Theorem 1).
- • As derived just before, we can only "not improve" the next iterate finitely many times before reaching γk


large enough, hence we obtain convergence as soon as δ is small enough which happens eventually. Hence, we obtain convergence of the iterates to the global minimizer.

| |
|---|


#### D.3 Proofs for approximate expectation PBH

Proof of Lemma 12. Lemma 12. Let x ∈ Rd, δ,γ > 0 and i.i.d. samples {yi} ∼ Yδ ∼ N(x,δγId). Then, almost surely,

N i=1 Tf(yi)exp(−f (Tf(yi))/δ)

mδ,γ. (45)

−−−−−→

mN,δ,γ :=

N i=1 exp(−f (Tf(yi))/δ)

N→+∞

Proof. We have first that for all N ∈ N, Ni=1 exp(−f (Tf(yi))/δ) > 0, each term is integrable against the Gaussian measure, and thus by the strong law of large numbers N1 Ni=1 exp(−f (Tf(yi))/δ) −−−−−→

E e−f(T

f(Yδ))/δ

N→+∞

a.s.. On the other end, by Lemma 8, each term in Ni=1 Tf(yi)exp(−f (Tf(yi))/δ) is integrable against the Gaussian measure, and thus by the strong law of large numbers N1 Ni=1 Tf(yi)exp(−f (Tf(yi))/δ) −−−−−→

N→+∞ E Tf(Yδ)e−f(T

f(Yδ))/δ a.s.. Hence, mN,δ,γ −−−−−→

mδ,γ a.s..

| |
|---|


N→+∞

Proof of Lemma 13. Lemma 13. Let x ∈ Rd, δ,γ > 0 and i.i.d. samples {yi} ∼ Yδ ∼ N(x,δγId). Suppose that there exists M ∈ M such that dist(mδ,γ,∂Att(M)) > 0. Then, almost surely,

Tf(mδ,γ). (46)

Tf(mN,δ,γ) −−−−−→

N→+∞

Proof. We have by Assumption 4 that Tf is continuous on any interior of Att(M), hence the result follows from Lemma 12.

| |
|---|


###### Proof of Lemma 14.

Lemma 14. Let (mN)N≥1 be a sequence in Rd such that mN → m, N → +∞. Assume that for sufficiently large N, mN does not belong to Ns the measurable null set not included in the partition of Rd defined by M∈M Att(M) (Lemma 6). Then every accumulation point of the sequence (Tf(mN))N≥1 belongs to

Q, Adj(m) := {Q ∈ M : m ∈ Att(Q)}. (47)

Q∈Adj(m)

Proof. Let m be a cluster point of (Tf(mN))N≥1. Then there exists a subsequence (mN

)k≥1 such that Tf(mN

k

) → m. Since (Tf(mN

k

))k≥1 converges, it is bounded. Hence there exists a compact set K ⊂ Rd such that Tf(mN

) ∈ K for all k. By assumption, only finitely many components of M intersect K. Therefore, after extracting a further subsequence, there exists a component Q ∈ M such that

k

k

) ∈ Q for all ℓ ≥ 1. On the other hand, for k large enough one has mN

Tf(mN

kℓ

k ∈ Att(Mk) for a unique component Mk ∈ M. Because Tf(mN

∈/ N, and therefore mN

k

) ∈ Q and Tf(y) ∈ M whenever y ∈ Att(M), we must have Mk = Q. Hence for all sufficiently large k, mN

k

k → m, we obtain m ∈ Att(Q). Thus Q ∈ Adj(m).

k ∈ Att(Q). Passing to the limit and using mN

| |
|---|


Proof of Theorem 3. Proof. First, as the number of samples grows to infinity, by Lemma 12, all mN,δ,γ are close to mδ,γ, hence we the behavior of the algorithm is governed asymptotically by the behavior of Algorithm 1.

By rejecting worse update and coercivity of f (Assumption 1), iterates are bounded and stay in some bounded set B ⊂ Rd. Thus

dist(x,Att(x∗)) < +∞.

df := sup x∈B

Set γ > 0. For every x ∈ B,

1 2γ

d2f + fmin

Vx(x∗) ≤

2 f

If γ > d

2µ then, for all M ̸= x∗,

Vx(x∗) < fmin + µ ≤ Vx(M). Meaning that for γ sufficiently large, by Proposition 2 there exists δ > 0 and r1 > 0 such that for all δ ≤ δ

∥mδ,γ − x∗∥ ≤ r1. Moreover, for N sufficiently large, there exists r2 > 0 such that

∥mN,δ,γ − mδ,γ∥ ≤ r2.

Therefore, as there exists r > 0, such that B(x∗,r) ⊂ Att(x∗), and r1 + r2 ≤ r, then x+ = x∗. We thus obtain immediate convergence if γ is large enough, N is large enough and δ small enough.

Now as in Theorem 2, there are several scenarios:

- • if progress (i.e., strict decrease) is made at every iteration, as iterates are bounded, we visit finitely many M ∈ M until convergence (see proof of Theorem 1). We can however visit non minimizing point as mN,δ,γ may sit with non zero probability in the null set of the partition defined by Att(M) for all M ∈ M, hence finite convergence cannot be guaranteed to happen.
- • As derived just before, we can only "not improve" the next iterate finitely many times before reaching γk large enough, hence we obtain convergence as soon as δ is small enough, and N is big enough which happens eventually.


Hence, we obtain convergence of the iterates to the global minimizer.

| |
|---|


Proof of Proposition 3. Proof. Denote mN,δ,γ = A

BN , mδ,γ = BA, where

N

N

1 N

Tf(yi)exp(−f(Tf(yi))/δ), and A = E[Tf(Yδ)exp(−f(Tf(Yδ))/δ)],

AN =

i=1

while

N

1 N

exp(−f(Tf(yi))/δ), and B = E[exp(−f(Tf(Yδ))/δ)]. We want to control

BN =

i=1

B(AN − A) − A(BN − B) BBN

AN BN −

A B

=

,

w.r.t. quantities that we control, i.e., ∥AN − A∥ and |BN − B|. We first look at the denominator. Set 0 < η < B and the event {|BN −B| ≤ η}. On this event, we have BN ≥ B −η > 0, implying by the triangular inequality that

+ ∥A∥|BN − B| B(B − η)

∥AN − A∥ B − η

B(AN − A) − A(BN − B) BBN ≤

∥mN,δ,γ − mδ,γ∥ =

.

Now, to obtain ∥mN,δ,γ − mδ,γ∥ ≤ ε, we bound the two terms on the righthandside of this inequality w.r.t. B − η. If ∥AN − A∥ ≤ 2ε(B − η), and |BN − B| ≤ min η, εB2(∥BA−∥η) , then we obtain the desired bound. It remains to quantify the probability of these two bounds holding together. Indeed, we have

εB(B − η) 2∥A∥

ε 2

(B − η) |BN − B| ≤ min η,

{∥mN,δ,γ − mδ,γ∥ ≤ ε} ⊂ ∥AN − A∥ ≤

The union bound on the complements then tells us that

.

P(∥mN,δ,γ − mδ,γ∥ ≤ ε) ≥ 1 − P ∥AN − A∥ >

εB(B − η) 2∥A∥

ε 2

(B − η) − P |BN − B| > min η,

.

The two righthandside probabilities can be controlled through Markov’s and Chebyshev’s inequality. We can apply it through the growth control on f and Lemma 8 as ∥AN − A∥ and |BN − B| are both square integrable against the Gaussian measure. We have

As

E[∥AN − A∥2] t2

Var(BN) s2

, and P(|BN − B| > s) ≤

P(∥AN − A∥ > t) ≤

.

1 N2

E[∥AN − A∥2] = E

  1

= E

1 N2

=

N

N

AiN − A,

AiN − A

i=1

i=1

 

N

AiN − A,AjN − A

N2

i,j=1

N

E AiN − A,AjN − A

i,j=1

For i ̸= j by independence, we have E AiN − A,AjN − A = 0. Remain the N, i = j terms, giving

1 N

E∥Tf(y1)exp(−f(Tf(y1))/δ) − A∥2, while

E ∥AN − A∥2 =

Var(exp(−f(Tf(y1))/δ)) N

, Therefore, we obtain

Var(BN) =

4E∥Tf(y1)exp(−f(Tf(y1))/δ) − A∥2 Nε2(B − η)2 −

Var(exp(−f(Tf(y1))/δ)) N min η, εB2(∥BA−∥η)

P(∥mN,δ,γ − mδ,γ∥ ≤ ε) ≥ 1 −

2 .

We deduce then the existence of α by setting N large enough.

| |
|---|


The dependence on δ may appear highly problematic, but also note that in practice f(Tf(y1)) should be of the order of δ for our best samples.

Proof of Theorem 4. Proof. The number of samples is finite, by Lemma 12, all mN,δ,γ are close to mδ,γ, hence we the behavior of the algorithm is governed asymptotically by the behavior of Algorithm 1.

By rejecting worse update and coercivity of f (Assumption 1), iterates are bounded and stay in some bounded set B ⊂ Rd. Thus

dist(x,Att(x∗)) < +∞. Set γ > 0. For every x ∈ B,

df := sup x∈B

1 2γ

d2f + fmin

Vx(x∗) ≤

2 f

If γ > d

2µ then, for all M ̸= x∗,

Vx(x∗) < fmin + µ ≤ Vx(M). Meaning that for γ sufficiently large, by Proposition 2 there exists δ > 0 and r1 > 0 such that for all δ ≤ δ ∥mδ,γ − x∗∥ ≤ r1. For N sufficiently large (Proposition 3), there exists ε > 0 and 0 < α < 1 such that P(∥mN,δ,γ − mδ,γ∥ ≤ ε) ≥ α.

Therefore, as there exists r > 0, such that B(x∗,r) ⊂ Att(x∗), we need ε small enough so that and r1 + ε ≤ r, then with probability superior or equal to α, x+ = x∗. Thus, if N is large enough so this ε is small enough, then the high probability follows.

The rest of the proof is the same as in Theorem 3. Hence, we obtain convergence of the iterates to the global minimizer with high probability.

| |
|---|


The trick here is that we do not need an uniform control on the probability on all the iterates. We simply need to wait for γ to be sufficiently large so that one of the iterates theoretically has x∗ as one of its minimizers of the potential Vx, then if we have enough samples we reach the correct solution with high probability.

### E Additional results

We display additional results for the full scaling law (all parameters available to be fitted Shukor et al. [2025]). The results are worse (in terms of prediction) than those of the additive law, in average. It was expected given the results of Shukor et al. [2025]. Our algorithm stil outperforms the others.

|Family Domain<br><br>|N = 5 N = 10 N = 15 N = 20 N = 30 N = 40 N = 50|ZOP BH|
|---|---|---|
|LLM (d = 47)<br><br>arxiv book c4 commoncrawl github stackexchange wikipedia<br><br>|12.085 12.303 11.681 12.358 11.861 12.177 12.694 10.046 10.949 10.173 10.722 10.718 10.264 10.265<br><br>10.937 10.949 10.874 10.936 11.115 11.472 10.716 10.445 11.038 11.834 11.710 11.450 11.516 11.256<br><br>17.323 17.385 18.258 17.305 18.434 17.899 18.470 12.488 12.891 12.943 13.162 13.110 13.024 13.073 19.658 19.859 20.044 19.664 19.915 19.739 19.749<br><br>|12.646 12.379<br><br>10.800 10.649<br>11.309 11.314 11.677 11.464<br><br><br>19.882 18.847<br><br>13.620 13.374<br><br>20.529 19.827<br><br><br>|
|LVM (d = 29)<br><br>alttext<br><br>highquality1<br><br>highquality2 synthetic<br><br><br>|4.117 6.703 11.270 10.317 12.237 14.245 14.062 7.634 7.758 9.393 12.712 18.447 16.315 19.492 7.536 10.969 9.483 11.711 15.700 18.769 19.177 11.435 14.736 11.070 13.664 14.441 16.844 21.105<br><br>|13.176 10.130 21.979 11.756 21.367 12.207 29.138 15.884|
|NMM (d = 23)<br><br>captions interleaved text|10.944 12.190 11.921 12.111 12.098 12.596 12.347 10.839 8.768 10.925 11.097 10.969 10.586 10.706<br><br>6.565 9.392 8.811 9.057 9.313 9.174 9.131<br><br>|11.351 11.317 10.178 10.907 8.774 8.120|


- Table 2: Test MRE = |predictionobservation−observation| (%) for fitting full scaling law. (lbfgs steps=10, CPU time=300s). We set γ = 10 and δ = 10−3 at initialization. Results averaged over three seeds.

|Family Domain<br><br>|N = 5 N = 10 N = 15 N = 20 N = 30 N = 40 N = 50|ZOP BH|
|---|---|---|
|LLM (d = 47)<br><br>arxiv book c4 commoncrawl github stackexchange wikipedia<br><br>|12.373 12.445 11.820 12.478 12.318 12.561 12.387<br><br>9.910 10.947 10.529 10.590 10.451 10.295 10.256 11.226 11.266 11.571 11.161 11.201 11.203 10.992<br>10.650 11.254 11.733 11.249 11.321 11.679 11.331 16.579 18.328 18.947 16.835 18.686 18.750 18.329<br>11.735 12.606 13.342 12.858 13.802 13.620 13.517 19.285 19.407 19.909 19.398 19.976 20.077 19.930<br>|12.646 12.269<br><br>10.800 10.629<br><br>11.309 11.060<br><br><br>11.677 11.474<br><br>19.882 18.243<br><br>13.620 13.339<br><br>20.529 19.744<br><br><br><br><br>|
|LVM (d = 29)<br><br>alttext<br><br>highquality1<br>highquality2 synthetic<br>|4.438 6.761 13.017 10.932 13.403 14.336 14.217 7.228 7.850 10.172 12.248 18.583 17.110 19.230 7.305 10.519 9.581 12.259 17.326 18.470 19.405 9.318 11.464 10.898 15.507 18.410 17.687 20.299<br><br>|13.176 10.094 21.979 11.735 21.367 12.217 29.138 18.764|
|NMM (d = 23)<br><br>captions interleaved text<br><br>|10.727 11.847 11.867 12.172 12.224 12.383 12.094 10.561 8.522 10.151 11.040 10.564 10.552 10.649 7.202 8.772 8.902 9.023 9.787 9.147 9.147|11.351 11.308 10.178 10.906 8.774 8.120<br><br>|


- Table 3: Test MRE = |predictionobservation−observation| (%) for fitting full scaling law. (lbfgs steps=5, CPU time=300s). We set γ = 10 and δ = 10−3 at initialization. Results averaged over three seeds.


