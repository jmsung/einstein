---
type: source
kind: paper
title: On Min-Max affine approximants of convex or concave real valued functions from $\mathbb R^k$, Chebyshev equioscillation and graphics
authors: Steven B. Damelin, David L. Ragozin, Michael Werman
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1812.02302v10
source_local: ../raw/2018-damelin-min-max-affine-approximants-convex.pdf
ingested_for_concept: equioscillation-escape.md
cites:
  - ../wiki/concepts/equioscillation-escape.md
  - ../wiki/problems/1-*.md
  - ../wiki/problems/2-*.md
  - ../wiki/problems/4-*.md
---

# arXiv:1812.02302v10[math.OC]17Aug2021

## On Min-Max aﬃne approximants of convex or concave real valued functions from R𝒌, Chebyshev equioscillation and graphics.

Steven B. Damelin, David L. Ragozin and Michael Werman

Abstract We study Min-Max aﬃne approximants of a continuous convex or concave function 𝑓 : Δ ⊂ R𝑘 −→ R where Δ is a convex compact subset of R𝑘. In the case when Δ is a simplex we prove that there is a vertical translate of the supporting hyperplane in R𝑘+1 of the graph of 𝑓 at the vertices which is the unique best aﬃne approximant to 𝑓 on Δ. For 𝑘 = 1, this result provides an extension of the Chebyshevequioscillationtheoremforlinearapproximants.Ourresulthasinteresting connections to the computer graphics problem of rapid rendering of projective transformations.

Keywords: Optimization, Control, Computer Vision.

### 1 Introduction

We will work in R𝑘, 𝑘 ≥ 1 where x ∈ R𝑘 is the column vector [𝑥1 𝑥2 · · · 𝑥𝑘]𝑇 and 𝑇 denotes transpose. A function 𝑔 : R𝑘 → R is an aﬃne function provided there exists 𝜶 ∈ R𝑘, and 𝛽 ∈ R such that 𝑔(x) = 𝜶𝑇 x + 𝛽.

Steven B. Damelin Department of Mathematics, University of Michigan, 530 Church Street, Ann Arbor, MI 48109, USA. e-mail: damelin@umich.edu

David L. Ragozin Department of Mathematics, University of Washington, Seattle, WA 98195, USA. e-mail: rag@uw.edu

Michael Werman Department of Computer Science, The Hebrew University, 91904, Jerusalem, Israel. e-mail: michael.werman@mail.huji.ac.il

1

#### 1.1 Min-Max approximation

In this paper, we are interested in Min-Max approximation to a continuous 𝑓 : Δ ⊂ R𝑘 −→ R by aﬃne approximants to 𝑓 . See for example [4, 3, 7, 9, 11]. By imposing the restriction Δ is a simplex with non-empty interior, we obtain a complete characterization of these approximants and an explicit formula for a unique best approximant. Even in the case of an interval, 𝑘 = 1, our main result Theorem

###### 2.1 provides an extension of [[3], Corollary 7.6.3]. For 𝑘 = 1, our main result also provides an extension of the Chebyshev equioscillation theorem for linear approximants with an explicit unique formula for the best approximant. See Section 4. We show interesting connections of Theorem 2.1 to graphics. See Section 5.

In order to state our results, we need the following notation. For a continuous function 𝑔 : R𝑘 → R, and simplex Δ, we adopt the usual convention of:

𝑔(x) ∞(Δ) := sup x∈Δ

|𝑔(x)| .

We will answer the following

#### 1.2 Problem

Let 𝑓 : Δ ⊂ R𝑘 → R be a continuous function where Δ is a compact domain in R𝑘. Find conditions on Δ and 𝑓 which allow for the construction of the Min-Max aﬃne approximation problem (1) to 𝑓 over Δ. Equivalently, ﬁnd conditions on Δ and 𝑓 which allow for the explicit construction of an 𝜶 ∈ R𝑘 and a 𝛽 ∈ R which solve

𝑓 (x) − (𝜶𝑇 x + 𝛽) ∞(Δ) . (1)

min

{𝜶,𝛽}

### 2 Main result: Theorem 2.1

##### Our main result is

Theorem 2.1 Let {a1, . . . , a𝑘+1} be 𝑘 + 1 aﬃnely independent points in R𝑘 so that their convex hull Δ = CH(a1 . . . a𝑘+1) is a 𝑘-simplex and assume 𝑓 : Δ ⊂ R𝑘 → R is a continuous convex or concave function over Δ. Then the Min-Max aﬃne approximant to 𝑓 over Δ is the hyperplane average 𝜎 := 𝜋2+𝜌, where 𝜋 is the aﬃne hyperplane AS((a1, 𝑓 (a1)) . . . (a𝑘+1, 𝑓 (a𝑘+1))) in R𝑘+1 and 𝜌 is the supporting hyperplane to the graph of 𝑓 parallel to 𝜋.

Here AS denotes the aﬃne span and any hyperplane 𝜏 is identiﬁed with its graph {(x, 𝜏(x)) ∈ R𝑘+1 : 𝑥 ∈ R𝑘}.

- Theorem 2.1 belongs to an interesting class of related optimization problems


which can be found for example in [1, 2, 3, 4, 6, 7, 8, 9, 11].

We know of no convex domain other than a 𝑘-simplex where we can generate a hyperplane 𝜋 as in Theorem 2.1 for which we can verify that the graph of 𝑓 over the domain lies entirely above or entirely below that hyperplane.

We now present two remarks regarding Theorem 2.1.

- Remark 2.1 The following stronger version of Theorem 2.1 holds which has an identical proof as Theorem 2.1.

Theorem 2.2 Given a continuous function 𝑓 on a simplex Δ with the following property: The graph of 𝑓 lies entirely above or below its secant hyperplane 𝜋 through the graph points of 𝑓 over the vertices of Δ. Then an expression for the Min-Max aﬃne approximation of 𝑓 on the simplex Δ has graph given by the hyperplane 𝜋 + 𝑑 where 2d is the non-zero extremum value of 𝑓 − 𝜋 on Δ. An alternative deﬁnition of 𝜋 is the aﬃne interpolant to 𝑓 at the 𝑘 + 1 vertices of the simplex Δ.

- Remark 2.2 In this remark, we speak to a geometric description of the hyperplane average in Theorem 2.1 and write formulae for the optimal 𝜶 and 𝛽 in the notation of Problem 1.2, expression (1).

Let the vector 𝜶 and the scalar 𝛽 be deﬁned as the solution to the following equation.



 

a𝑇1 1 . 1 . 1 . 1

a𝑇𝑘+1 1



 

𝜶 𝛽

=



 

𝑓 (a1) . . . 𝑓 (a𝑘+1)



 

. (1)

Secondly deﬁne:

𝛽 =

minx∈Δ( 𝑓 (x) − (𝜶 𝑇 x + 𝛽 )), if 𝑓 is convex. maxx∈Δ( 𝑓 (x) − (𝜶 𝑇 x + 𝛽 )), if 𝑓 is concave.

(2)

Then set 𝜶 := 𝜶 and 𝛽 := 12 (𝛽 + 𝛽 ). It is easily checked that Problem 1.2, expression (1) is optimized at (𝜶, 𝛽).

We end this remark by saying that the computation of the optimal 𝛽 above costs a minimization of a convex function (a linear shift of ± 𝑓 ) over the set Δ.

- 3 The proof of Theorem 2.1


The key ideas in our proof of Theorem 2.1 are the two equivalent deﬁnitions of a convex function. 𝑓 : Δ ⊂ R𝑘 → R is convex provided for all 𝛾𝑖 ≥ 0 : Σ𝑘+1

𝑖=1 𝛾𝑖 = 1, and any aﬃne independent set of 𝑘 + 1 points {a 1, . . . , a 𝑘+1}, 𝑓 (Σ𝑘+1

𝑖=1 𝛾𝑖a 𝑖) ≤ Σ𝑘+1

𝑖=1 𝛾𝑖 𝑓 (a 𝑖), i.e. the graph of 𝑓 over the convex hull of 𝑘 + 1 aﬃnely independent points lies below the convex hull of the 𝑘 + 1 image points {[a 𝑖𝑇 𝑓 (a 𝑖)]𝑇 : 1 ≤

𝑖 ≤ 𝑘 + 1}, or equivalently, for each x ∈ Δ, and each support plane at [x𝑇 𝑓 (x)]𝑇

with slope 𝜂 ∈ R𝑘, 𝑓 (y) ≥ 𝑓 (x) + 𝜂𝑇 (y − x), for all y ∈ Δ, i.e. the graph of 𝑓 lies on or above any supporting hyperplane.

For our proof of Theorem 2.1, we advise the reader to use Figure 1 for intuition. Proof First assume that 𝑓 is convex, so its graph over Δ lies on or below the hyperplane 𝜋. Let −2𝑑 := inf{𝑙 : 𝜋 + 𝑙e𝑘+1 ∩ 𝑔𝑟𝑎𝑝ℎ( 𝑓 ) ≠  }. Then any admissible 𝑙 must satisfy 𝑙 ≤ 0 and so this in turn means 𝑑 ≥ 0. Here, e𝑘+1 is the 𝑘 + 1𝑠𝑡 basis vector in R𝑘+1 so each admissible 𝑙 gives a downward translate of 𝜋 with non-empty intersection with the graph of 𝑓 . Since Δ is compact and 𝑓 is continuous, the inf is actually a min and so their exists at least one graph point (𝑦, 𝑓 (𝑦)) on 𝜌 := 𝜋 − 2𝑑.

Thus 𝜌 is a supporting hyperplane (tangent plane if 𝑓 is diﬀerentiable at y). Moreover, at the points a𝑖 an easy computation shows 𝜋 − 𝑑 = (2𝜋 − 2𝑑)/2 = (𝜋 + 𝜌)/2 = 𝜌 + 𝑑. These and the construction of 𝜎 imply 𝑓 (a𝑖) − 𝜎(a𝑖) = 𝑑 = 𝜎(𝑦) − 𝑓 (𝑦). We also observe that ∀𝑧 ∈ Δ, | 𝑓 (𝑧) − 𝜎(𝑧)| ≤ 𝜎(𝑦) − 𝑓 (𝑦) = 𝑑, as 𝑓 (𝑧) is between 𝜋 and 𝜌 whose midplane is 𝜎. Now with the above in hand we are able to argue as follows. Assume 𝜇 is a best aﬃne approximating plane. Then ﬁrst 𝜇(a𝑖) ≥ 𝜎(a𝑖), 𝑖 ∈ [1 . . . 𝑘 + 1] otherwise the maximal distance increases. On the other hand, writing 𝑦 = 𝑖 𝑘=+11 𝛾𝑖a𝑖 for constants 𝛾𝑖 ≥ 0 : Σ𝑘+1

𝑖=1 𝛾𝑖 = 1, we have

𝜇(𝑦) = 𝑖 𝑘=+11 𝛾𝑖𝜇(a𝑖) ≤ 𝜎(𝑦) otherwise the maximal distance increases. We deduce that 𝜇 = 𝜎. This concludes the proof of Theorem 2.1 in case 𝑓 is convex.

In the case that 𝑓 is concave, since 𝜋 = AS((𝑎1, 𝑓 (a1)) . . . (a𝑘+1, 𝑓 (a𝑘+1))) and the graph of 𝑓 over Δ lies on or above 𝜋, we can repeat the convex argument replacing 𝑑 by − 𝑑, inf by sup and interchanging ≤ and ≥. Alternatively note − 𝑓 is convex and one checks that the negative of the solution for − 𝑓 is just 𝜋2+𝜌.

Note that even if 𝑓 is not convex (or concave) and not even smooth the method produces a best uniform approximation for the 𝑘 + 2 points comprised of the 𝑘 + 1 points (a1, 𝑓 (a1)) . . . , (a𝑘+1, 𝑓 (a𝑘+1)) and (y, 𝑓 (y)).

### 4 Theorem 2.1: The case 𝒌 = 1.

For 𝑘 = 1, our main result Theorem 2.1 provides an extension of the classical Chebyshev equioscillation theorem, see Theorem 4.1 below, for linear approximants with an explicit unique formula for the best approximant.

We now explain this.

#### 4.1 Chebyshev systems and Chebyshev-Markov equioscillation

We will work with the real interval [𝑝, 𝑞] where 𝑝 < 𝑞 and the space of real valued continuous functions 𝑓 : [𝑝, 𝑞] → R. As per convention, we denote this space by 𝐶([𝑝, 𝑞]).

![image 1](<2018-damelin-min-max-affine-approximants-convex_images/imageFile1.png>)

- Fig. 1 Illustration of Theorem 2.1. The secant 𝜋 is the convex hull of 𝑘 + 1 values (x𝑖, 𝑓 (x𝑖)) and 𝜌 the supporting hyperplane. The convexity of 𝑓 leads to the fact that the plane, 𝜎, with same slope halfway between 𝜋 and 𝜌 is the best aﬃne approximation.


A set of 𝑙 + 1, 𝑙 ≥ 0 functions 𝑢𝑗(𝑡) 𝑙𝑗=0, 𝑢𝑗 ∈ 𝐶([𝑝, 𝑞]) is called a Chebyshev (Haar) system on the interval [𝑝, 𝑞] if any linear combination

∑︁𝑙

𝑢(𝑡) =

𝑐𝑗𝑢𝑗(𝑡), 𝑡 ∈ [𝑝, 𝑞]

𝑗=0

with not all coeﬃcients 𝑐𝑗 zero, has at most 𝑙 distinct zeros in [𝑝, 𝑞].

The 𝑙 +1 dimensional subspace 𝑈𝑙 ⊂ 𝐶([𝑝, 𝑞)]) spanned by a Chebyshev system 𝑢𝑗(𝑡) 𝑙𝑗=0 on [𝑝, 𝑞] deﬁned by

𝑈𝑙 :=   

𝑐𝑗𝑢𝑗(𝑡)  

∑︁𝑙

𝑢(𝑡) : 𝑢(𝑡) =

𝑗=0

is called a Chebyshev space on [𝑝, 𝑞].

Alfred Haar, 1885-1933, was a Hungarian mathematician. In 1904 he began to study at the University of Göttingen. His doctorate was supervised by David Hilbert.

The classical Chebyshev equioscillation theorem, see for example [[5], Chapter 9, Theorem 4.4] and [10] is the following:

- Theorem 4.1 Let 𝑓 ∈ 𝐶([𝑝, 𝑞]) and let 𝑈𝑙 be a 𝑙 + 1 Chebyschev space on an interval [𝑝, 𝑞]. Then 𝑢ˆ ∈ 𝑈𝑙 is a best uniform approximant to 𝑓 on [𝑝, 𝑞], that is 𝑢 satisﬁes

𝑓 − 𝑢ˆ ∞[𝑝,𝑞] = inf𝑢∈𝑈𝑙 𝑓 − 𝑢 ∞[𝑝,𝑞]

if and only there exists 𝑙 + 2 points {𝑥1, ..., 𝑥𝑙+2} with 𝑝 ≤ 𝑥1 < ... < 𝑥𝑙+2 ≤ 𝑞 such that

𝑓 (𝑥𝑖) − 𝑢ˆ(𝑥𝑖) = 𝑤(−1)𝑖 𝑓 − 𝑢ˆ ∞[𝑝,𝑞], 𝑤 = ±1. (1)

Motivated by Theorem 4.1 we have:

4.2 Chebyshev equioscillation

Let 𝑓 ∈ 𝐶([𝑝, 𝑞)]. A Chebyshev polynomial ℎˆ𝑙 (when it exists) of degree at least 𝑙 ≥ 1, is the polynomial which best uniformly approximates 𝑓 on [𝑝, 𝑞], i.e, 2

ℎˆ𝑙 = arg min

ℎ𝑙 ∈Π𝑙

𝑓 − ℎ𝑙 ∞[𝑝,𝑞] where Π𝑙 is the set of polynomials of degree at most 𝑙.

The following is often called the Chebyshev equioscillation theorem.

- Theorem 4.2 Let 𝑓 ∈ 𝐶([𝑎, 𝑏]).Then ℎˆ𝑙 existsifthereexists𝑙+2points {𝑥1, ..., 𝑥𝑙+2} with 𝑝 ≤ 𝑥1 < ... < 𝑥𝑙+2 ≤ 𝑞 such that


𝑓 (𝑥𝑖) − ℎˆ𝑙(𝑥𝑖) = 𝑤(−1)𝑖 𝑓 − ℎˆ𝑙 ∞[𝑝,𝑞], 𝑤 = ±1. (2)

#### 4.3 The case 𝒍 = 1 of Theorem 4.2

We now show how Theorem 4.2 with 𝑙 = 1 corresponds to Theorem 2.1 for 𝑘 = 1.

We may assume that 𝑝 < 𝑞 and for the moment we do not assume anything about 𝑓 : [𝑝, 𝑞] → R. Deﬁne now a linear function 𝐿 : [𝑝, 𝑞] → R from 𝑓 in terms of parameters 𝑑 and 𝑦 to be determined later as follows:

𝐿(𝑥) = 𝑓 (𝑦) + 𝑑 + 𝑚(𝑥 − 𝑦), 𝑥 ∈ [𝑝, 𝑞]. (3) Now since 𝐿(𝑦) − 𝑓 (𝑦) = 𝑑, if we assume 𝐿(𝑝) − 𝑓 (𝑝) = −𝑑 = 𝐿(𝑞) − 𝑓 (𝑞) then

𝑑 = 𝑓 (𝑝) − 𝐿(𝑝) = 𝑓 (𝑝) − 𝑓 (𝑦) − 𝑑 − 𝑚(𝑝 − 𝑦). Thus

𝑓 (𝑝) − 𝑓 (𝑦) 2 −

𝑚 2 (𝑝 − 𝑦).

𝑑 =

Also,

𝑑 = 𝑓 (𝑞) − 𝐿(𝑞) = 𝑓 (𝑞) − 𝑓 (𝑦) − 𝑑 − 𝑚(𝑞 − 𝑦). So:

𝑓 (𝑝) − 𝑓 (𝑦) 2 −

𝑓 (𝑞) − 𝑓 (𝑦) 2 −

𝑚 2 (𝑝 − 𝑦) =

𝑚 2 (𝑞 − 𝑦).

Thus 𝑚 = 𝑓 (𝑞𝑝)−−𝑞𝑓 (𝑝) inthecasewhen 𝑓 or− 𝑓 isaconvexanddiﬀerentiablefunction, by the mean value theorem.

It is clear that we have proved Theorem 2.1 once we are able to choose 𝑟 to maximize 𝑑 if this is possible for the given 𝑓 . In the case when 𝑓 is convex, we see that 𝑚 = 𝑓 (𝑟). It is clear that the argument works when 𝑓 is concave, which implies − 𝑓 is convex,

In the case of 𝑘 = 1, we could write

𝑎𝑥 + 𝑏 𝑐𝑥 + 𝑑

𝑎 𝑐 x + 𝑑𝑐 − 𝑑𝑐 + 𝑏𝑐

==

x + 𝑑𝑐

𝑏 𝑐 − 𝑎𝑐 𝑑𝑐

𝑎 𝑐 +

=

x + 𝑑𝑐

which is either an upward or downward hyperbola for which the secant between [𝑝, 𝑞] lies above (or below) the curve. Then following the "mean value " argument, leads to 𝑟 with derivative =slope and via our visualization leads to a line with the same slope but halfway between the secant and tangent to 𝑟.

### 5 Connections of Theorem 2.1 to graphics

One consequence of Theorem 2.1 gives an interesting connection to graphics. We provide our ideas below.

We are given a ﬂat object O and want to render it from a given perspective, camera setup. The resulting image is a projective (AKA perspective or homography) transformation of O, 𝑃(O). Thus, each pixel (color) in O, (an ordered pair (𝑥1, 𝑦1) in R2) is transformed to a new pixel location (point) 2 via the action of 𝑃

𝑃 :

1 𝑑𝑥1 + 𝑒𝑦1 + 𝑗

𝑥1 𝑦1 ↦→

- 𝑎1𝑥1 + 𝑏1𝑦1 + 𝑐1
- 𝑎2𝑥1 + 𝑏2𝑦1 + 𝑐2


. (1)

Practically, to render this object which can have 10’s of millions of pixels it is useful to have a good fast approximation of the transformation not entailing division which can cause numerical instabilities. Thus, we seek aﬃne approximants to 𝑃. One known method is to simply take the aﬃne approximant to be the linear terms of the Taylor expansion around one point, the tangent approximation.

We aim to provide a better 2d-aﬃne approximant to 𝑃 than the tangent approximation. From Equation 1 the components of 𝑃(x) are given by

𝑎𝑖𝑥 + 𝑏𝑖𝑦 + 𝑐𝑖 𝑑𝑥 + 𝑒𝑦 + 𝑗

𝑓𝑖(x) :=

, 𝑖 = 1, 2. (2)

From our main Theorem 2.1 we know that if we can ﬁnd a triangle, Δ, containing (a large part of) O such that each 𝑓𝑖(x) is convex or concave then there exist Min-Max aﬃne approximations 𝜶𝑖𝑇 x + 𝛽𝑖 to each 𝑓𝑖. Then forming the aﬃne transformation 𝐴 of 2-space given by

- 𝜶1𝑇 x + 𝛽1
- 𝜶2𝑇 x + 𝛽2


𝐴(x) :=

, (3) provides, component wise, the best uniform aﬃne approximants on Δ.

Since a diﬀerentiable function is convex or concave on a domain exactly when it’s Hessian is respectively positive or negative semideﬁnite the following is a key tool for the application of our main result.

- 𝑝11 𝑝12
- 𝑝12 𝑝22


Proposition 5.1 A symmetric 2𝑥2 matrix 𝐷 =

is positive or negative semideﬁnite according as 𝑠𝑖𝑔𝑛𝑢𝑚(𝑝11) = ±signum (𝑝11𝑝22 − 𝑝212).

The Hessian of

𝛽𝑌 − 𝛼𝛿 + 𝛾 𝑋 + 𝛿

𝛼𝑋 + 𝛽𝑌 + 𝛾 𝑋 + 𝛿

(4) is

= 𝛼 +

1 (𝑋 + 𝛿)3

2(𝛽𝑌 − 𝛼𝛿 + 𝛾) −𝛽(𝑋 + 𝛿)

𝐻 =

−𝛽(𝑋 + 𝛿) 0

< >

2

with determinant −𝛽

𝛼𝛿−𝛾

𝛽 . When we combine Proposition 5.1 with the Hessian of Eq. 4 we see that 𝛼𝑋𝑋++𝛽𝑌𝛿+𝛾

(𝑋+𝛿)4 . The sign of 𝐻[1, 1] = 2(𝛽𝑌 −𝛼𝛿+𝛾) depends on𝑌

in each of the connected components of R2 \ {{𝑋 = −𝛿} ∪ {𝑌 = 𝛼𝛿𝛽−𝛾 }} is either convex or concave. With the 2 coordinate functions of the projective transformation

(𝑋 and 𝑌) we end with 6 regions in R2 where Theorem 2.1 holds, Figure 2.

In order to transform a general projective transformation as in Eq. 3 to the form in Eq. 4, with a simple denominator, we rotate the axes so that 𝑋 is in the direction of

𝑑 𝑒

and normalize so that the coeﬃcient of 𝑋 in the denominator is 1.

In Figure 3 we show a few examples of the various aﬃne approximations 𝐴 of projective transformations 𝑃 using this idea.

- Fig. 2 The black line is where the projective transformation is inﬁnite, 𝑋 = −𝛿. The blue line is where the 𝜕𝑥𝜕2 term of the Hessian of the 𝑋 transformation is 0 and the red line is where the 𝜕𝑥𝜕2 term of the Hessian of the 𝑌 transformation is 0. The blue and yellow simplices deﬁne domains of transformations that are convex (or concave) while the red simplex is not.

The ﬁrst column is the original image O, the second column is the image transformed by a projective transformation 𝑃, modelling a new viewpoint, the third column is the transformation based on the aﬃne approximation 𝐴 of 𝑃 using Theorem 2.1 and a user deﬁned triangle while the fourth column is computed using a Taylor series approximation of 𝑃 around the image’s center. The images in column

- 3 should visually look closer to those in column 2 than those in column 4, the Taylor approximation.


![image 2](<2018-damelin-min-max-affine-approximants-convex_images/imageFile2.png>)

![image 3](<2018-damelin-min-max-affine-approximants-convex_images/imageFile3.png>)

![image 4](<2018-damelin-min-max-affine-approximants-convex_images/imageFile4.png>)

![image 5](<2018-damelin-min-max-affine-approximants-convex_images/imageFile5.png>)

![image 6](<2018-damelin-min-max-affine-approximants-convex_images/imageFile6.png>)

![image 7](<2018-damelin-min-max-affine-approximants-convex_images/imageFile7.png>)

![image 8](<2018-damelin-min-max-affine-approximants-convex_images/imageFile8.png>)

![image 9](<2018-damelin-min-max-affine-approximants-convex_images/imageFile9.png>)

![image 10](<2018-damelin-min-max-affine-approximants-convex_images/imageFile10.png>)

![image 11](<2018-damelin-min-max-affine-approximants-convex_images/imageFile11.png>)

![image 12](<2018-damelin-min-max-affine-approximants-convex_images/imageFile12.png>)

![image 13](<2018-damelin-min-max-affine-approximants-convex_images/imageFile13.png>)

![image 14](<2018-damelin-min-max-affine-approximants-convex_images/imageFile14.png>)

![image 15](<2018-damelin-min-max-affine-approximants-convex_images/imageFile15.png>)

![image 16](<2018-damelin-min-max-affine-approximants-convex_images/imageFile16.png>)

![image 17](<2018-damelin-min-max-affine-approximants-convex_images/imageFile17.png>)

Fig. 3 Original image / projective transformation of the image/ best uniform aﬃne approximation/ Taylor expansion.

### References

- 1. J.H. Ahlberg, E.N. Nilson, J.F. Walsh, Theory of splines and their applications, Acad. Press

(1967).

- 2. Y.A. Brudnyi, Approximation of functions deﬁned in a convex polyhedron, Soviet Math. Doklady, 11. 6 (1970), (pp. 1587-1590), Dokl. Akad. Nauk SSSR, 195 (1970), (pp. 1007-1009).
- 3. P.J. Davis, Interpolation and approximation, New York, 1963.
- 4. F. Deutsch, Best approximation in inner product spaces, CMS Books in Mathematics, 2001.
- 5. M.Krein,A.Nudelman,TheMarkovMomentproblemandextremalproblems,AMStranslation from the Russian edition of 1973.
- 6. N.P. Korneichuk, Extremal problems in approximation theory , Moscow (1976) (In Russian).
- 7. P.J. Laurent, Approximation et optimization, Hermann (1972).
- 8. V.L. Miroshichenko, Methods of spline functions, Moscow (1980).


- 9. S.M. Nikol’skii, Approximation of functions of several variables and imbedding theorems, Springer (1975) (Translated from Russian).
- 10. L. Schumaker, Spline Functions: basic theory, Academic Press, NY, 1983.
- 11. V.N. Teml’yakov, Best approximations for functions of two variables, Soviet Math. Doklady, 16: 4 (1975), (pp. 1051-1055), Dokl. Akad. Nauk SSSR, 223 (1975), (pp. 1079-1082).


