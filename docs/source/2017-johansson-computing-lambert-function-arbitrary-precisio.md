---
type: source
kind: paper
title: Computing the Lambert W function in arbitrary-precision complex interval arithmetic
authors: Fredrik Johansson
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1705.03266v1
source_local: ../raw/2017-johansson-computing-lambert-function-arbitrary-precisio.pdf
topic: general-knowledge
cites:
---

# arXiv:1705.03266v1[cs.MS]9May2017

## Computing the Lambert W function in arbitrary-precision complex interval arithmetic

##### Fredrik Johansson∗

###### Abstract

We describe an algorithm to evaluate all the complex branches of the Lambert W function with rigorous error bounds in interval arithmetic, which has been implemented in the Arb library. The classic 1996 paper on the Lambert W function by Corless et al. provides a thorough but partly heuristic numerical analysis which needs to be complemented with some explicit inequalities and practical observations about managing precision and branch cuts.

### 1 Introduction

The Lambert W function W(z) is the inverse function of f(w) = wew, meaning that W(z)eW(z) = z holds for any z. Since f is not injective, the Lambert W function is multivalued, having an inﬁnite number of branches Wk(z), k ∈ Z, analogous to the branches lnk(z) = log(z) + 2πik of the natural logarithm which inverts g(w) = ew.

The study of the equation wew = z goes back to Lambert and Euler in the 18th century, but a standardized notation for the solution only appeared in the 1990s with the introduction of LambertW in the Maple computer algebra system, along with the paper [2] by Corless, Gonnet, Hare, Jeﬀrey and Knuth which collected and proved the function’s main properties. There is now a vast literature on applications, and in 2016 a conference was held to celebrate the ﬁrst 20 years of the Lambert W function.

The paper [2] sketches how Wk(z) can be computed for any z ∈ C and any k, using a combination of series expansions and iterative root-ﬁnding. Numerical implementations are available in many computer algebra systems and numerical libraries; see for instance [6, 1, 8]. However, there is no published work to date addressing interval arithmetic or discussing a complete rigorous implementation of the complex branches.

The equation wew−z = 0 can naturally be solved with any standard interval root-ﬁnding method like subdivision or the interval Newton method [7]. Another possibility, suggested in [2], is to use a posteriori error analysis to bound the error of an approximate solution. The Lambert W function can also be evaluated as the solution of an ordinary diﬀerential equation, for which rigorous solvers are available. Regardless of the approach, the main diﬃculty is to make sure that correctness and eﬃciency are maintained near singularities and branch cuts.

This paper describes an algorithm for rigorous evaluation of the Lambert W function in complex interval arithmetic, which has been implemented in the Arb library [4]. This implementation was designed to achieve the following goals:

• W(z) is only a constant factor more expensive to compute than elementary functions like log(z) or exp(z). For rapid, rigorous computation of elementary functions in arbitrary precision, the methods in [3] are used.

∗LFANT project-team, INRIA Bordeaux-Sud-Ouest. Contact: fredrik.johansson@gmail.com.

- 0
- 1
- 2


| | | | |
|---|---|---|---|
| | | | |
| | |W0(x),ε = 0.5 W (x),ε = 0.1| |
| || |
|---|
<br><br>| |
|---|
<br><br>| |
|---|
<br><br>| |
|---|
|0<br><br>W0(x),ε = 0.01 W−1(x),ε = 0.5 W−1(x),ε = 0.1| |
| | | | |
|1 −1/e 0<br><br>of the real branches W0(x) output intervals given wide<br><br>until the output rad<br><br>enclosures are reasonably complex branches Wk are sup<br><br>to compute derivatives|1 2 x<br><br>and W−1(x) computed with Arb. The<br><br>input intervals. In this plot, the input ius is smaller than ε.<br><br>tight. ported, with a stringent treatment of W(n)(z) eﬃciently, for arbitrary n.| | |


W(x)k

−1

−2

−3

−4− 3

- Figure 1: Plot boxes show the size of the o t intervals have been subdivided


- • The output
- • All the com branch cuts.
- • It is possible


The main contribution of this paper is to derive bounds with explicit constants for a posteriori certiﬁcation and for the truncation error in certain series expansions, in cases where previous publications give big-O estimates. We also discuss the implementation of the complex branches in detail.

Arb uses (extended) real intervals of the form [m ± r], shorthand for [m − r,m + r], where the midpoint m is an arbitary-precision ﬂoating-point number and the radius r is an unsigned ﬁxed-precision ﬂoating-point number. The exponents of m and r are bignums which can be arbitrarily large (this is useful for asymptotic problems, and removes edge cases with underﬂow or overﬂow). Complex numbers are represented in rectangular form x + yi using pairs of real intervals. We will occasionally rely on these implementation details, but generally speaking the methods translate easily to other interval formats.

#### 1.1 Complex branches

In this work, Wk(z) always refers to the standard k-th branch as deﬁned in [2]. We sometimes write W(z) when referring to the multivalued Lambert W function or a branch implied by the context. Before we proceed, we summarize the branch structure of W. A more detailed description with illustrations can be found in [2].

Figure 1 demonstrates evaluation of the Lambert W function in the two real-valued regions. The principal branch W0(z) is real-valued and monotone increasing for real z ≥ −1/e, with the image [−1,∞), while W−1(z) is real-valued and monotone decreasing for real −1/e ≤ z < 0, with the image (−∞,−1]. Everywhere else, Wk(z) is complex. There is a square root-type singularity at the branch point z = −1/e connecting the real segments, where W0(−1/e) = W−1(−1/e) = −1. The principal branch contains the root W0(0) = 0,

which is the only root of W. For all k = 0, the point z = 0 is a branch point with a logarithmic singularity.

W0(z) has a single branch cut on (−∞,−1/e), while the branches Wk(z) with |k| ≥ 2 have a single branch cut on (−∞,0). The branches W±1 are more complicated, with a set of adjacent branch cuts: in the upper half plane, W−1 has a branch cut on (−∞,−1/e) and one on (−1/e,0); in the lower half plane, W−1 has a single branch cut on (−∞,0). W1 is similar to W−1, but with the sides exchanged. The branch cuts on (−∞,0) or (−∞,−1/e) connect Wk with Wk+1, while the branch cuts on (−1/e,0) connect W−1 with W1.

We follow the convention that the function value on a branch cut is continuous when approaching the cut in the counterclockwise direction around a branch point. For the standard branches Wk(z), this is the same as continuity with the upper half plane, i.e. Wk(x + 0i) = limy→0+ Wk(x + yi). When Im(z) = 0, we have Wk(z) = W−k(z). By the same convention, the principal branch of the natural logarithm is deﬁned to satisfy Im(log(z)) ∈ (−π,+π].

We do not use signed zero in the sense of IEEE 754 ﬂoating-point arithmetic, which would allow preserving continuity from either side of a branch cut. This is a trivial omission since we can distinguish between W(x+0i) and W(x−0i) using Wk(x−0i) = W−k(x + 0i).

In interval arithmetic, we need to enclose the union of the images of W(z) on both sides of the cut when the interval representing z straddles a branch cut. The jump discontinuity between the cuts will prevent the output intervals from converging when the input intervals shrink (unless the input intervals lie exactly on a branch cut, say z = [−5,−4] + 0i). This problem is solved by providing a set of alternative branch cuts to complement the standard cuts, as discussed in Section 4.

### 2 The main algorithm

The algorithm to evaluate the Lambert W function has three main ingredients:

- • (Asymptotic cases.) If |z| is extremely small or large, or if z is extremely close to the branch point at −1/e when W(z) ≈ −1, use the respective Taylor, Puiseux or asymptotic series to compute W(z) directly.
- • (Approximation.) Use ﬂoating-point arithmetic to compute some w˜ ≈ W(mid(z)).
- • (Certiﬁcation.) Given w˜, use interval arithmetic (or ﬂoating-point arithmetic with directed rounding) to determine a bound r such that |W(z) − w˜| ≤ r, and return w˜ + [±r] + [±r]i, or simply [ ˜w ± r] when W(z) is real-valued.


The special treatment of asymptotic cases is not necessary, but improves performance since the error can be bounded directly without a separate certiﬁcation step. We give error bounds for the truncated series expansions in Section 3.

Computing a ﬂoating-point approximation with heuristic error control is a well understood problem, and we avoid going into too much detail here. Essentially, Arb uses the Halley iteration

wjewj − mid(z) ewj+1 −

wj+1 = wj −

(wj + 2)(wjewj − mid(z)) 2wj + 2

suggested in [2] to solve wew − mid(z) = 0, starting from a well-chosen initial value. In the most common cases, machine double arithmetic is ﬁrst used to achieve near 53-bit accuracy (with care to avoid overﬂow or underﬂow problems or loss of signiﬁcance near z = −1/e).

For typical accuracy goals of less than a few hundred bits, this leaves at most a couple of iterations to be done using arbitrary-precision arithmetic.

In the arbitrary-precision phase, the working precision is initially set low and then increases with each Halley iteration step to match the estimated number of accurate bits (which roughly triples with each iteration). This ensures that obtaining p accurate bits costs O(1) full-precision exponential function evaluations instead of O(log p).

#### 2.1 Certiﬁcation

To compute a certiﬁed error bound for w˜, we use backward error analysis, following the suggestion of [2]. We compute z˜ = we˜ w˜ with interval arithmetic, and use

w˜ = W(˜z) = W(z) +

z ˜

W (t)dt. (1)

z

to bound the error Wk(˜z) − Wk(z). This approach relies on having a way to bound |W k|, which we address in Section 3.

The formal identity (1) is only valid provided that the correct integration path is taken on the Riemann surface of the multivalued W function. During the certiﬁcation, we verify that the straight-line path γ from z to z˜ for Wk is correct in (1), so that the error is bounded by |z − z˜|supt∈γ |W k(t)|. This is essentially to say that we have approximated Wk(z) for the right k, since a poor starting value (or rounding error) in the Halley iteration could have put w˜ on the wrong branch, or closer to a solution on the wrong branch than the intended solution.

- Algorithm 1 Compute certiﬁed enclosure of Wk(z). The input is a complex interval z, a branch index k ∈ Z, and a complex ﬂoating-point number w˜.


- 1. Verify that w˜ = x + yi lies in the range of the branch Wk:

- (a) Compute t = xsinc(y), v = −cos(y), u = sgn(k)y/π using interval arithmetic.
- (b) If k = 0, check (|u| < 1) ∧ (t > v).
- (c) If k = 0, check P1 ∧ (P2 ∨ P3 ∨ P4) where

- P1 = (u > 2|k| − 2) ∧ (u < 2|k| + 1)
- P2 = (u > 2|k| − 1) ∧ (u < 2|k|)
- P3 = (u < 2|k|) ∧ (t < v)
- P4 = (u > 2|k| − 1) ∧ (t > v).


- (d) If the check fails, return [±∞] + [±∞]i.


- 2. Compute z˜ = we˜ w˜ using interval arithmetic.
- 3. Compute a complex interval U ⊇ z ∪ z˜ (U will contain the straight line from z to z˜).
- 4. Verify that U does not cross a branch cut: check

(Im(U) ≥ 0) ∨ (Im(U) < 0) ∨

Re(eU + 1) > 0 if k = 0 Re(U) > 0 if k = 0

.

If the check fails, return [±∞] + [±∞]i.

- 5. Compute a bound C ≥ |W k(U)| and return w˜ + [±r] + [±r]i where r = C|z − z˜|.


The complete certiﬁcation procedure is stated in Algorithm 1. In the pseudocode, all pointwise predicates are extended to intervals in the strong sense; for example, x ≥ 0 evalu-

ates to true if all points in the interval representing x are nonnegative, and false otherwise. A predicate that should be true for exact input in inﬁnite precision arithmetic can therefore evaluate to false due to interval overestimation or insuﬃcient precision.

In the ﬁrst step, we use the fact that the images of the branches in the complex W-plane are separated by the line (−∞,−1/e] together with the curves {−η cotη+ηi} for −π < η < π and 2kπ < ±η < (2k +1)π (this is proved in [2]). In the k = 0 case, the predicates P2,P3,P4 cover overlapping regions, allowing the test to pass even if w˜ falls very close to one of the curves with 2kπ < ±η < (2k + 1)π where a sign change occurs, i.e. when z crosses the real axis to the right of the branch point.

The test in Algorithm 1 always fails when z lies on a branch cut, or too close to a cut to resolve with a reasonable precision, say if z = −21010 + 10i or z = −10 + 2−1010i. This problem could be solved by taking the location of z into account in addition that of w˜. In Arb, a diﬀerent solution has been implemented, namely to perturb z away from the branch cut before calling Algorithm 1 (together with an error bound for this perturbation). This works well in practice with the use of a few guard bits, and seemed to require less extra logic to implement.

Due to the cancellation in evaluating the residual z − z˜, the quantity z˜ = we˜ w˜ needs to be computed to at least p-bit precision in the certiﬁcation step to achieve a relative error bound of 2−p. Here, a useful optimization is to compute ewj with interval arithmetic in the last Halley update w˜ = wj+1 = H(wj) and then compute ew˜ as ewjew˜−wj. Evaluating ew˜−wj costs only a few series terms of the exponential function since |w˜ − wj| ≈ 2−p/3.

A diﬀerent possibility for the certiﬁcation step would be to guess an interval around w˜ and perform one iteration with the interval Newton method. This can be combined with the main iteration, simultaneously extending the accuracy from p/2 to p bits and certifying the error bound. An advantage of the interval Newton method is that it operates directly on the function f(w) = wew − z and its derivative without requiring explicit knowledge about W . This method was tested but ultimately abandoned in the Arb implementation since it seemed more diﬃcult to handle the precision and make a good interval guess in practice, particularly when z is represented by a wide interval. In any case the branch certiﬁcation would still be necessary.

#### 2.2 The main algorithm in more detail

- Algorithm 2 describes the main steps implemented by the Arb function with signature


void acb_lambertw(acb_t res, const acb_t z, const fmpz_t k, int flags, slong prec)

where acb t denotes Arb’s complex interval type, res is the output variable, fmpz t is a multiprecision integer type, and prec gives the precision goal p in bits.

- In step 2, we switch to separate code for real-valued input and output (calling the func-

tion arb lambertw which uses real arb t interval variables). The real version implements essentially the same algorithm as the complex version, but skips most branch cut related logic.

- In step 3, we reduce the working precision to save time if the input is known to less than


p accurate bits. The precision is subsequently adjusted in step 5, accounting for the fact that we gain accurate bits in the value of Wk(z) from the exponent of mid(z) or k when |Wk(z)| is large. Step 5 is cheap, as it only requires inspecting the exponents of the ﬂoating-point components of z and computing bit lengths of integers.

The constants T,L,M,P appearing in steps 4, 6 and 7 are tuning parameters to control the number of series expansion terms allowed to compute W directly instead of falling back to

Algorithm 2 Main algorithm for Wk(z) implemented in acb lambertw. The input is a complex interval z, a branch index k ∈ Z, and a precision p ∈ Z≥2.

- 1. If z is not ﬁnite or if k = 0 and 0 ∈ z, return indeterminate ([±∞] + [±∞]i).
- 2. If k = 0 and z ⊂ (−1/e,∞), or if k = −1 and z ⊂ (−1/e,0), return Wk(z) computed using dedicated code for the real branches.
- 3. Set the accuracy goal to q ← min(p,max(10,−log2 rad(z)/|mid(z)|)).
- 4. If k = 0 and |mid(z)| < 2−q/T, return W0(z) computed using T terms of the Taylor series.
- 5. Compute positive integers b1 ≈ log2(|log(z) + 2πik|), b2 ≈ log2(b1). If |z| is near ∞, or near 0 and k = 0, adjust the goal to q ← min(p,max(q + b1 − b2,10)).
- 6. Let s = 2 − b1, t = 2 + b2 − b1. If b1 − max(t + Ls,Mt) > q, return Wk(z) computed using the asymptotic series with (L,M) terms.
- 7. Check if z is near the branch point at −1/e: if |ez + 1| < 2−2q/P−6, and |k| ≤ 1 (and

Im(z) < 0 if k = 1, or Im(z) ≥ 0 if k = −1) return Wk(z) computed using P terms of the Puiseux series.

- 8. If z contains points on both sides of a branch cut, set za = Re(z) + (Im(z) ∩ [0,∞))i and zb = Re(z) + (−Im(z) ∩ [0,∞))i. Then compute wa = Wk(za) and wb = W−k(zb) and return wa ∪ wb.

- 9. Let x+yi = mid(z). If x lies to the left of a branch point (0 or −1/e) and |y| < 2−q|x|, set z = Re(z) + [ε ± ε]i where ε = 2−q|x| (if y < 0 in this case, modify the following steps to compute W−k(z ) instead of Wk(z )). Otherwise, set z = z.

- 10. Compute a ﬂoating-point approximation w˜ ≈ Wk(mid(z )) to a heuristic accuracy of q bits plus a few guard bits.
- 11. Convert w˜ to a certiﬁed complex interval w for Wk(mid(z )) by calling Algorithm 1.
- 12. If z is inexact, bound |W k(z )| ≤ C and add [±r] + [±r]i to w, where r = C rad(z ). Return w.


root-ﬁnding. These parameters could be made precision-dependent to optimize performance, but for most purposes small constants work well.

Step 8 ensures that z lies on one side of a branch cut, splitting the evaluation of Wk(z) into two subcases if necessary. This step ensures that step 12 (which bounds the propagated error due to the uncertainty in z) is correct, since our bound for W does not account for the branch cut jump discontinuity (and in any case diﬀerentiating a jump discontinuity would give the output [±∞] + [±∞]i which is needlessly pessimistic). We note that conjugation is used to get a continuous evaluation of Wk(Re(z) + (Im(z) ∩ (−∞,0))i), in light of our convention to work with closed intervals and make the standard branches Wk continuous from above on the cut.

We perform step 8 after checking if the asymptotic series or Puiseux series can be used, since correctly implemented complex logarithm and square root functions take care of branch cuts automatically. If z needs to be split into za and zb in step 8, then the main algorithm can be called recursively, but the ﬁrst few steps can be skipped. However, step 7 should be repeated when k = ±1 since the Puiseux series near −1/e might be valid for za or zb even when it is not applicable for the whole of z. This ensures a ﬁnite enclosure when z contains the branch point −1/e.

1.0

h = 0.5

0.5

- h = 0.1

| |
|---|


- h = 0.02


0.0

−0.5

− (W(1+yi))1

−1.0

−1.5

−2.0

−2.5

−3.0

−3 −2 −1 0 1 2 3 y

- Figure 2: Plot of the real part of W1(z) on the vertical segment z = −1 + yi,|y| ≤ 3. The boxes show the range of the output intervals given input intervals y = [a,a+h]. The picture demonstrates continuity between the branch cut and the upper half plane: as intended, an imaginary part of [−h,0] (or [−h/2,h/2], say, though not pictured here) in the input captures the jump discontinuity while [0,h] does not. Where continuous, the output intervals converge nicely when h → 0.
- 3 Bounds and series expansions We proceed to state the inequalities needed for various error bounds in the algorithm.


- 3.1 Taylor series Near the origin of the k = 0 branch, we have the Taylor series


∞

(−n)n−1 n!

zn.

W0(z) =

n=1

Since |nn−1/n!| < en, the truncation error on stopping before the n = T term is bounded by eT|z|T/(1 − e|z|) if |z| < 1/e.

#### 3.2 Puiseux series

Near the branch point at −1/e when W(z) ≈ −1, the Lambert W function can be computed by means of a Puiseux series. This especially useful for intervals containing the point −1/e itself, since we can compute a ﬁnite enclosure whereas enclosures based on W (z) blow up. If α = 2(ez + 1), then provided that |α| < √2, we have

 

B (α) if k = 0 B (−α) if k = −1 and Im(z) ≥ 0 B (−α) if k = +1 and Im(z) < 0

Wk(z) =



where

B(ξ) = W

ξ2 − 2 2e

∞

cnξn. (2)

=

n=0

Note that W±1 have one-sided branch cuts on (−∞,0) and (−1/e,0). In the opposite upper and lower half planes, there is only a single cut on (−∞,0) so the point −1/e does not need to be treated specially.

In (2), the appropriate branches of W are implied so that B(ξ) is analytic on |ξ| < √2. In terms of the standard branch cuts Wk, that is

 

- 0 if − π/2 < arg(ξ) ≤ π/2
- 1 if π < arg(ξ) < −π/2 −1 otherwise.


k =



The coeﬃcients cn are rational numbers

1 3

11 72

43 540

c0 = −1, c1 = 1, c2 = −

, c4 = −

, c3 =

,...

which can be computed recursively. From singularity analysis, |cn| = O((1/√2)n), but we need an explicit numerical bound for computations. The following estimate is not optimal, but adequate for practical use.

Theorem 1. The coeﬃcients in (2) satisfy |cn| < 2 · (4/5)n, or more simply, |cn| ≤ 1. Proof. Numerical evaluation of W shows that |2 + B(ξ)| < 2 on the circle |ξ| = 5/4, so the Cauchy integral formula gives the result.

| |
|---|


The veriﬁcation can of course be done using interval arithmetic, as demonstrated in Figure 4. We stress that there is no circular dependency on Theorem 1 since the Puiseux series is not used for evaluation that far from from the branch point.

- 3.3 Asymptotic series The Lambert W function has the asymptotic expansion


∞

Wk(z) ∼ L1 − L2 +

l=0

∞

cl,mσlτm (3)

m=1

where

L1 = log(z) + 2πki, L2 = log(L1), σ = 1/L1, τ = L2/L1 (4) and

(−1)m m!

l + m l + 1

(5)

cl,m =

where nk denotes an (unsigned) Stirling number of the ﬁrst kind.

This expansion is valid for all k when |z| → ∞, and also for k = 0 when |z| → 0. In fact, (3) is not only an asymptotic series but (absolutely and uniformly) convergent for all suﬃciently small |σ|,|τ|. These properties of the expansion (3) were proved in [2].

The asymptotic behavior of the coeﬃcients cl,m was studied further in [5], but that work did not give explicit inequalities. We will give an explicit bound for |cl,m|, which permits us to compute Wk(z) directly from (3) with a bound on the error in the relevant asymptotic regimes.

- Lemma 2. For all n,k ≥ 0, n k ≤

2nn! k!

. Proof. This follows by induction on the recurrence relation

n + 1 k

= n

n k

+

n k − 1

.

| |
|---|


- Lemma 3. For all l,m ≥ 0, |cl,m| ≤ 4l+m. Proof. By the previous lemma,


2l+m(l + m)! (l + 1)!m! ≤ 2l+m

|cl,m| ≤

l + m m ≤ 4l+m.

| |
|---|


We can now restate (3) in the following eﬀective form.

- Theorem 4. With σ,τ,L1,L2 deﬁned as above, if |σ| < 1/4 and |τ| < 1/4, and if |z| > 1 when k = 0, then


L−1

M−1

cl,mσlτm + εL,M(z) with

Wk(z) = L1 − L2 +

m=1

l=0

4|τ|(4|σ|)L + (4|τ|)M (1 − 4|σ|)(1 − 4|τ|)

|εL,M(z)| ≤

.

Proof. Under the stated conditions, the series (3) converges to Wk(z), by the analysis in [2]. We can bound the tail as

∞

∞

∞

cl,mσlτm ≤

m=M

l=L

l=0

∞

∞

(4|σ|)l(4|τ|)m +

m=M

l=L

∞

(4|σ|)l(4|τ|)m.

m=1

Evaluating the bivariate geometric series gives the result.

| |
|---|


#### 3.4 Bounds for the derivative

Finally, we give an rigorous global bound for the magnitude of W . Since we want to compute W with small relative error, the estimate for |W (z)| should be optimal (up to a small constant factor) anywhere, including near singularities. We did not obtain a single neat expression that covers Wk(z) adequately for all k and z, so a few case distinctions are made.

W like W is a multivalued function, and whenever we ﬁx a branch for W, we ﬁx the corresponding branch for W . Exactly on a branch cut, W is therefore ﬁnite (except at a branch point) and equal to the directional derivative taken along the branch cut, so we must deal with the branch cut discontinuity separately when bounding perturbations in W if z crosses the cut.

The derivative of the Lambert W function can be written as W (z) =

W(z) 1 + W(z)

1 z

1 (1 + W(z))eW(z)

=

where a limit needs to be taken in the rightmost expression for W0(z) near z = 0. The rightmost expression also shows that W (z) ≈ 1/z when |W(z)| is large. Bounding |Im(Wk(z))| from below gives the following.

###### Theorem 5. For |k| ≥ 2,

(2k − 2)π (2k − 2)π − 1 ≤

1 |z|

- 1 |z|

2π

- 2π − 1 ≤


1.2 |z|

|W k(z)| ≤

.

Also, if k = 1 and Im(z) ≥ 0, or if k = −1 and Im(z) < 0, then

π π − 1 ≤

1.5 |z|

1 |z|

|W k(z)| ≤

.

For large |z|, the following two results are convenient.

###### Theorem 6. If |z| > e, then for any k,

W0(|z|) W0(|z|) − 1

1 |z|

|W k(z)| ≤

.

Proof. The inequality |Wk(z)| ≥ W0(|z|) holds for all z (this is easily proved from the inverse function relationship deﬁning W), giving the result.

| |
|---|


###### Theorem 7. If |z| ≥ 12 + (2|k| + 1)π e−1/2, or more simply if |z| ≥ 4(|k| + 1), then

1 |z|

|W k(z)| ≤

.

Proof. Let a = Re(Wk(z)). We have |Wk(z)/(1 + Wk(z))| ≤ 1 when a ≥ −1/2. If a < −1/2, then |z| = |Wk(z)eWk(z)| < (|a| + (2|k| + 1)π)ea < (12 + (2|k| + 1)π)e−1/2.

| |
|---|


It remains to bound |W k(z)| for k ∈ {−1,0,1} in the cases where z may be near the branch point at −1/e. This can be accomplished as follows.

###### Theorem 8. For any k,

1 |z|

1.5 |ez + 1|

|W k(z)| ≤

max 3,

.

Proof. If |W(z)+1| ≥ 1/2, then |W(z)/(W(z)+1)| ≤ 3. Now consider the case W(z)+1 = ε for some |ε| ≤ 1/2. Then we must have |ez + 1| ≤ |ε|2, due to the Taylor expansion

ε2 2

ε2 3

ε2 8

1 e

(−1 + ε)e−1+ε + e−1 =

+

+

+ ... .

This implies that

W(z) W(z) + 1

= |ε − 1| |ε|

≤

1 + |ε| |ε|

≤

1.5 |ez + 1|

.

| |
|---|


Theorem 8 can be used practice, provided that we use a diﬀerent bound when k = 0

and z ≈ 0 (also, when z ≈ −1/e and Wk(z)  ≈ −1). However, it is worth making a few case distinctions and slightly complicating the formulas to tighten the error propagation for k = −1,0,1. For these branches, we implement the following inequalities.

###### Theorem 9. Let t = |ez + 1|.

- 1. If |z| ≤ 64, then


2.25 t(1 + t)

|W 0(z)| ≤

.

- 2. If |z| ≥ 1, then

|W 0(z)| ≤

1 |z|

.

- 3. If Re(z) ≥ 0, or if Im(z) < 0 when k = −1 (respectively Im(z) ≥ 0 when k = 1), then

|W±1(z)| ≤

1 |z|

1 +

1 4 + |z|2

.

- 4. For all z,


1 |z|

23 32

1 √t

|W±1(z)| ≤

1 +

.

Proof. The inequalities can be veriﬁed by interval computations on a bounded region (since

- 1/|z| is an upper bound for suﬃciently large |z|) excluding the neighborhoods of the branch points. These computations can be done by bootstrapping from Theorem 8. Close to −1/e, Theorem 1 applies, and an argument similar to that in Theorem 8 can be used close to 0. (We omit the straightforward but lengthy numerical details.)


| |
|---|


It is clearly possible to make the bounds sharper, not least by adding more case distinctions, but these formulas are suﬃcient for our purposes, easy to implement, and cheap to evaluate. The implementation requires only the extraction of lower or upper bounds of intervals and unsigned ﬂoating-point operations with directed rounding (assuming that ez + 1 has been computed using interval arithmetic).

### 4 Alternative branch cuts

If the input z is an exact ﬂoating-point number, then we can always pinpoint its location in relation to the standard branch cuts of W. However, if the input is generated by an interval computation, it might look like z = −10 + [±ε]i where the sign of Im(z) is ambiguous. If we want to compute solutions of wew = z in this case, the standard branches Wk do not work well because the jump discontinuity on the branch cut prevents the output intervals from converging when ε → 0.

Likewise, when evaluating an integral or a solution of a diﬀerential equation involving

W, say a b f(z,W(g(z)))dz, we might need to consider paths that would cross the standard branch cuts. We already saw an example with the application of the Cauchy integral formula

to the Puiseux series coeﬃcients in Section 3.2.

It is instructive to consider the treatment of square roots and logarithms, where the branch cut can be moved from (−∞,0) to (0,∞) quite easily. The solutions of w2 = z are given by w = √z,−

√z, but switching to w = i√

−z,−i√

−z gives continuity along paths crossing the negative real axis. Similarly, for the solutions of ew = z, we can switch from w = log(z) + 2kπi to w = log(−z) + (2k + 1)πi.

The Lambert W function lacks a functional equation that simply would allow us to negate z. Instead, we deﬁne a set of alternative branches for W as follows:

• Wleft|k(z) joins Wk(z) for z in the upper half plane with Wk+1(z) in the lower half plane, providing continuity to the left of the branch point at 0 (when k ∈/ {−1,0}) or −1/e (when k ∈ {−1,0}). The branch cuts of this function thus extend from 0 or −1/e to +∞.

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |


15

10

πiθW(e)

5

0

−5

0 1 2 3 4 5 θ

- Figure 3: Plot of the real part (even function) and imaginary part (odd function) of W(eπiθ) with continuous analytic continuation on the Riemann surface of W. The branch used for evaluation is W0 on θ ∈ [−0.5,0.5], Wleft|0 on [0.5,1.5], W1 on [1.5,2.5], Wleft|1 on [2.5,3.5], W2 on [3.5,4.5], and Wleft|2 on [4.5,5.5]. Continuity is preserved whenever θ crosses an integer, that is, when z = eπiθ crosses the real axis. The input intervals for θ have width


- 1/13.


• Wmiddle(z) joins W−1(z) in the upper half plane with W1(z) in the lower half plane, with continuity through the central segment (−1/e,0). This function extends the real analytic function W−1(x),x ∈ (−1/e,0) to a complex analytic function on z ∈ C \ (−∞,−1/e] ∪ [0,∞), unlike the standard branch W−1(z) where the real-valued segment lies precisely on the branch cut.

We follow the principle of counter-clockwise continuity to deﬁne the values of these alternative branches on their branch cuts (absent use of signed zero).

In the Arb implementation, the user can select the respective modiﬁed branch cuts by passing a special value in the ﬂags ﬁeld instead of the default value 0, namely

acb_lambertw(res, z, k, ACB_LAMBERTW_LEFT, prec) acb_lambertw(res, z, k, ACB_LAMBERTW_MIDDLE, prec)

where k = −1 should be set in the second case.

We implement the alternative branch cuts by splitting the input into za = Re(z)+(Im(z)∩ [0,∞))i and zb = Re(z)+(−Im(z)∩[0,∞))i. If the standard branches to be taken below and above the cut have index k and k respectively, then we compute W(z) as Wk(za)∪W−k (zb). Conjugation is used to get a continuous evaluation of Wk (Re(z) + (Im(z) ∩ (−∞,0))i), in light of our convention to work with closed intervals and make the standard branches Wk continuous from above on the cut.

We observe that for Wmiddle(z) the Puiseux expansion at −1/e is valid in all directions, as is the asymptotic expansion at 0 with L1 = log(−z) and L2 = log(−L1). Further, Wleft|k(z) is given by the asymptotic expansion with L1 = log(−z) + (2k + 1)πi,L2 = log(L1) when |z| → ∞. These formulas could be used directly instead of case splitting where applicable.

- 0

- 1

- 2

- 3


2πiθ−W((z2)/(2e)),z=1.25e

−1

−2

0.0 0.5 1.0 1.5 2.0 θ

- Figure 4: Plot of the real and imaginary part and the absolute value (black) of 2+W((z2 −

- 2)/(2e)),z = 1.25eπiθ with continuous analytic continuation. The function argument (z2 −


2)/(2e) traces two loops around the branch point at −1/e, passing through the branches 0,+1,−1, and back to 0. From left to right, the branch used for evaluation cycles through W0,Wleft|0,W1,Wmiddle,W−1,Wleft|−1,W0. Input intervals have been subdivided adaptively to show the absolute value bound.

- 5 Testing and benchmarks


|z|10 100 1000 10000|
|---|---|
|10 1010 101020 10i −101020 −1/e + 10−100 −1/e − 10−100<br><br>|3.36 7.12 1.60 1.50 3.64 6.92 1.65 1.53<br><br>3.46 8.39 1.91 1.67<br><br>13.20 8.68 4.71 3.27<br><br>3.69 29.75 7.53 4.59<br>4.57 2.33 2.23 1.97<br><br><br>4.43 2.36 7.08 2.89<br>|


Table 1: Time to compute w = W0(z), relative to the time to compute ew, at a precision of 10, 100, 1000 and 10000 decimal digits.

We have tested the implementation in Arb in various ways, most importantly to verify that correct inclusions are being computed, but also to make sure that output intervals are reasonably tight.

The automatic unit test included with the library generates overlapping random input intervals z1,z2 (sometimes placed very close to −1/e), computes w1 = Wk(z1) and w2 = Wk(z2) at diﬀerent levels of precision (sometimes directly invoking the asymptotic expansion with a random number of terms instead of calling the main Lambert W function implementation), checks that the intervals w1 and w2 overlap, and also checks that w1ew1 contains z1. The conjugate symmetry is also tested. These checks give a strong test of correctness.

We have also done separate tests to verify that the error bounds converge for exact ﬂoating-point input when the precision is increased, and further ad hoc tests have been done

to test a variety of easy and diﬃcult cases at diﬀerent precisions.

At low precision, the absolute time to evaluate W for a “normal” input z is about 10−6 seconds when W is real and 10−5 seconds when W is complex (on an Intel i5-4300U CPU). For instance, creating a 1000 by 1000 pixel domain coloring plot of W0(z) on [−5,5]+[−5,5]i takes 12 seconds.

Table 1 shows normalized timings for acb lambertw. The higher relative overhead when W is complex mainly results from less optimized precision handling in the ﬂoating-point code (which could be improved in a future version), together with some extra overhead for the branch test.

We show the output (converted to decimal intervals using arb printn) for a few of the test cases in the benchmark. For z = 10, the following results are computed at the respective levels of precision:

[1.745528003 +/- 3.82e-10] [1.7455280027{...79 digits...}0778883075 +/- 4.71e-100] [1.7455280027{...979 digits...}5792011195 +/- 1.97e-1000]

- [1.7455280027{...9979 digits...}9321568319 +/- 2.85e-10000] For z = 101020, we get:
- [2.302585093e+20 +/- 3.17e+10] [230258509299404568354.9134111633{...59 digits...}5760752900 +/- 6.06e-80] [230258509299404568354.9134111633{...959 digits...}8346041370 +/- 3.55e-980] [230258509299404568354.9134111633{...9959 digits...}2380817535 +/- 6.35e-9980]


For z = −1/e + 10−100, the input interval overlaps with the branch point at 10 and 100 digits, showing a potential small imaginary part in the output, but at higher precision the imaginary part disappears:

[-1.000 +/- 3.18e-5] + [+/- 2.79e-5]i [-1.0000000000{...28 digits...}0000000000 +/- 3.81e-50] + [+/- 2.76e-50]i [-0.9999999999{...929 digits...}9899904389 +/- 2.99e-950] [-0.9999999999{...9929 digits...}9452369126 +/- 5.45e-9950]

### 6 Automatic diﬀerentiation

Finally, we consider the computation of derivatives W(n), or more generally (W ◦ f)(n) for an arbitrary function f. That is, given a power series f ∈ C[[x]], we want to compute the power series W(f) truncated to length n + 1.

The higher derivatives of W can be calculated using recurrence relations as discussed in [2], but it is more eﬃcient to use formal Newton iteration in the ring C[[x]] to solve the equation wew = f. That is, given a power series wj correct to n terms, we compute

wjewj − f ewj + wjewj which is correct to 2n terms.

wj+1 = wj −

Indeed, this approach allows us to compute the ﬁrst n derivatives of W or W ◦ f (when the ﬁrst n derivatives of f are given) in O(M(n)) operations where M(n) is the complexity of polynomial multiplication. With FFT based multiplication, we have M(n) = O(nlog n).

This method is implemented by the Arb functions arb poly lambertw series (for real polynomials) and acb poly lambertw series (for complex polynomials).

Since the low n coeﬃcients of wj+1 and wj are identical mathematically, we simply copy these coeﬃcients instead of performing the full subtraction (avoiding needless inﬂation of the enclosures). A further important optimization in this algorithm is to save the constant

term e0 = [x0]ew so that ewj can be computed as e0ewj−[x0]wj. This avoids a transcendental function evaluation, which is expensive and moreover can be ill-conditioned, leading to greatly inﬂated enclosures. The performance could be improved further by a constant factor by saving the partial Newton iterations done internally for power series division and exponentials.

Empirically, the Newton iteration scheme is reasonably numerically stable, permitting the evaluation of high order derivatives with modest extra precision even in interval arithmetic. For example, computing 10000 terms in the series expansion of h(x) = W0(e1+x) at 256-bit precision takes 2.8 seconds, giving [x10000]h(x) as

[-6.02283194399026390e-5717 +/- 5.56e-5735].

### 7 Discussion

A number of improvements could be pursued in future work.

The algorithm presented here is correct in the sense that it computes a validated enclosure for Wk(z), absent any bugs in the code. It is also easy to see that the enclosures converge when the input intervals converge and the precision is increased accordingly (as long as a branch cut is not crossed), under the assumption that the ﬂoating-point approximation is computed accurately. However, we have made no attempt to prove that the ﬂoating-point approximation is computed accurately beyond the usual heuristic reasoning and experimental testing.

Although the focus is on interval arithmetic, we note that applying Ziv’s strategy [9] allows us to compute ﬂoating-point approximations of Wk(z) with certiﬁed correct rounding. This requires only a simple wrapper around the interval implementation without the need for separate analysis of ﬂoating-point rounding errors. A rigorous ﬂoating-point error analysis for computing the Lambert W function without the use of interval arithmetic seems feasible, certainly for real variables but probably also for complex variables.

We use a ﬁrst order bound based on |W (z)| for error propagation when z is inexact. For wide z, more accurate bounds could be achieved using higher-order estimates. Simple and tight bounds for |W(n)(z)| for small n would be a useful addition.

For very wide intervals z, optimal enclosures could be determined by evaluating W at two or more points to ﬁnd the extreme values. This is most easily done in the real case, but suitable monotonicity conditions could be determined for complex variables as well.

The implementation in Arb is designed for arbitrary precision. For low precision, the main approximation is usually computed using double arithmetic, but the certiﬁcation uses arbitrary-precision arithmetic which consumes the bulk of the time. Using validated double or double-double arithmetic for the certiﬁcation would be signiﬁcantly faster.

### References

- [1] F. Chapeau-Blondeau and A. Monir. Numerical evaluation of the Lambert W function and application to generation of generalized Gaussian noise with exponent 1/2. IEEE Transactions on Signal Processing, 50(9):2160–2165, 2002.
- [2] R. M. Corless, G. H. Gonnet, D. E. G. Hare, D. J. Jeﬀrey, and D. E. Knuth. On the Lambert W function. Advances in Computational Mathematics, 5(1):329–359, 1996.
- [3] F. Johansson. Eﬃcient implementation of elementary functions in the medium-precision range. In 22nd IEEE Symposium on Computer Arithmetic, ARITH22, pages 83–89, 2015.


- [4] F. Johansson. Arb: Eﬃcient arbitrary-precision midpoint-radius interval arithmetic. IEEE Transactions on Computers, PP(99):1–1, 2017. http://dx.doi.org/10.1109/ TC.2017.2690633 (to appear).
- [5] G. A. Kalugin and D. J. Jeﬀrey. Convergence in C of series for the Lambert W function. arXiv preprint arXiv:1208.0754, 2012.
- [6] P. W. Lawrence, R. M. Corless, and D. J. Jeﬀrey. Algorithm 917: complex doubleprecision evaluation of the Wright ω function. ACM Transactions on Mathematical Software, 38(3):20, 2012.
- [7] R. E. Moore. Methods and applications of interval analysis. SIAM, 1979.
- [8] D. Veberiˇc. Lambert W function for applications in physics. Computer Physics Communications, 183(12):2622–2628, 2012.
- [9] A. Ziv. Fast evaluation of elementary mathematical functions with correctly rounded last bit. ACM Transactions on Mathematical Software, 17(3):410–423, 1991.


