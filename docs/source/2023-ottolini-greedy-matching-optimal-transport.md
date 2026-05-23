---
type: source
kind: paper
title: Greedy Matching in Optimal Transport with concave cost
authors: Andrea Ottolini, Stefan Steinerberger
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2307.03140v2
source_local: ../raw/2023-ottolini-greedy-matching-optimal-transport.pdf
topic: general-knowledge
cites:
---

# arXiv:2307.03140v2[math.CA]27Aug2025

## GREEDY MATCHING IN OPTIMAL TRANSPORT WITH CONCAVE COST

ANDREA OTTOLINI AND STEFAN STEINERBERGER

Abstract. We consider the optimal transport problem between a set of n red points and a set of n blue points subject to a concave cost function such as c(x, y) = ∥x − y∥p for 0 < p < 1. Our focus is on a particularly simple matching algorithm: match the closest red and blue point, remove them both and repeat. We prove that it provides good results in any metric space (X, d) when the cost function is c(x, y) = d(x, y)p with 0 < p < 1/2. Empirically, the algorithm produces results that are remarkably close to optimal – especially as the cost function gets more concave; this suggests that greedy matching may be a good toy model for Optimal Transport for very concave transport cost.

1. Introduction

1.1. The problem. The original motivation behind this paper is to understand the geometry of optimal transport with concave cost. Perhaps the easiest instance of this problem is the following: let X = {x1,...,xn} and Y = {y1,...,yn} be two sets of real numbers, what can be said about the optimal transport cost

n

|xi − yπ(i)|p,

Wpp(X,Y ) = min π∈Sn

i=1

where π : {1,2,...,n} → {1,2,...,n} ranges over all permutations? The answer is trivial when p ≥ 1: order both sets in increasing order and send the i−th largest element xi to the i−th largest element yi. After ordering the points, the optimal permutation is the identity permutation π(i) = i. The problem becomes highly nontrivial when the cost function is concave.

Figure 1. 20 (right: 50) red points on R being optimally matched to 20 (right: 50) blue points on R (shown displaced to illustrate the matching) and subject to cost c(x,y) = |x − y|1/2.

2020 Mathematics Subject Classification. 82B44, 90B80. Key words and phrases. Optimal Transport, Euclidean Random Assignment Problems.

1

As was already pointed out by Gangbo & McCann [17]

For concave functions of the distance, the picture which emerges is rather different. Here the optimal maps will not be smooth, but display an intricate structure which – for us – was unexpected; it seems equally fascinating from the mathematical and the economic point of view. [...] To describe one effect in economic terms: the concavity of the cost function favors a long trip and a short trip over two trips of average length [...] it can be efficient for two trucks carrying the same commodity to pass each other traveling opposite directions on the highway: one truck must be a local supplier, the other on a longer haul. (Gangbo & McCann, [17])

The problem has received increased attention in recent years, we refer to results of Bobkov and Ledoux [6, 7], Boerma, Tsyvinski, Wang and Zhang [8], Caracciolo, D’Achille, Erba and Sportiello [10], Caracciolo, Erba and Sportiello [11, 12], Delon, Salomon and Sobolevski [13, 14], Juillet [20] and McCann [21].

Figure 2. Left: 50 red points on R being matched to 50 blue points on R when c(x,y) = log |x − y|. Right: same points and same cost function matched with the greedy algorithm. The two matchings are very similar: why?

A reason why the problem is interesting is illustrated in Figure 2: as suggested by Gangbo-McCann, there is a very curious dichotomy where most points get matched to points that are very close with a few exceptional points being transported a great distance. It is somewhat clear, in a qualitative sense, that this is to be expected (considering, for example, the Jensen inequality for concave functions). However, on a more quantitative level, the non-locality poses considerable difficulties.

- 1.2. Dyck and Greedy Matching. If the cost function is given by c(x,y) = h(|x − y|) with h concave, it appears there exist two natural toy models that are effective in different regimes: the Dyck matching and the greedy matching.


Figure 3. A collection of n = 5 red and blue points, the function g(x) (left, rescaled for clarity) and the Dyck matching (right).

The first such model is the Dyck matching of Caracciolo-D’Achille-Erba-Sportiello [10]: their idea is to introduce g : [0,1] → Z

g(x) = #{1 ≤ i ≤ n : xi ≤ x} − #{1 ≤ i ≤ n : yi ≤ x} The function is increasing whenever x crosses a new element of X while it decreases every time it crosses an element of Y . The Dyck matching is then obtained by matching across level sets of the function g (see Fig. 3). The Dyck matching is independent of the cost function. It is shown numerically in [10] (and reproduced in §2.6) that the Dyck matching produces a nearly optimal matching whose costs exceeds the optimal cost by very little. The second toy model is given by a simple greedy matching which works in general metric spaces.

## Greedy Matching.

- (1) Determine

m = min

1≤i,j≤n

c(xi,yj).

- (2) Find a pair (xi,yj) with c(xi,yj) = m and set π(i) = j.
- (3) Remove xi from X and yj from Y and repeat.


If the cost function is strictly monotonically increasing in the distance c(x,y) = h(|x − y|), this greedy matching is, like the Dyck matching, independent of the cost function. This algorithm leads to mediocre results when the cost function is convex. This was already observed in the PhD thesis of d’Achille [1, Section 1.4] who explicitly considers the algorithm when c(x,y) = |x−y|p and p ≥ 1 and shows that the results are not particularly good. One of the main points of our paper is to point out that the greedy matching is very good for very concave cost functions.

|x − y|0.01

|x − y|0.99

greedy

Dyck

Figure 4. Four different matchings of the exact same set of n = 100 points illustrated using McCann circles (§2.2): the optimal matching for c(x,y) = |x − y|0.01 is very similar to the greedy matching, for c(x,y) = |x−y|0.99 it is close to the Dyck matching.

2. Results

- 2.1. Main Result. It is clear that a greedy matching will initially perform well since it is matching points that are very close to each other. The main concern is that the greedy matching ends up maneuvering itself into a situation where all remaining choices are bad. We will now show that, in a suitable sense, this does


not happen. The result will be phrased in terms of the Wasserstein distance W1 between the sets X and Y where the sets will be assumed to lie in a metric space

W1(X,Y ) = inf

π∈Sn

n

d(xi,yπ(i)).

i=1

When 0 < p < 1 it follows from H¨lder’s inequality with coefficients 1/p and 1/(1 − p) that we can bound the size of the optimal matching by

n

d(xi,yπ(i))p ≤ W1(X,Y )p · n1−p.

Wpp(X,Y ) = inf

π∈Sn

i=1

Our main result shows that, in any arbitrary metric space, the greedy matching, proceeding at each step blindly and without any foresight into the future, achieves the same rate up to a constant when 0 < p < 1/2. Note that the greedy matching will usually be very different from the one that minimizes W1.

- Theorem 1 (Main Result). For any 0 < p < 1 there is a constant cp > 0 such that for any two sets of n points X,Y in any metric space, the greedy matching produces matching satisfying, with respect to the cost function c(x,y) = d(x,y)p,


 

n1−p if 0 < p < 21 √n · log n if p = 12 np if 12 < p < 1.

Greedyp(X,Y ) ≤ cp · W1(X,Y )p ·



The result is optimal up to constants when 0 < p < 1/2. We illustrate this on [0,1] equipped with the Euclidean distance (see Fig. 5). If the blue point are close to 0 and the red points are close to 1, then the greedy algorithm takes Greedyp(X,Y ) ∼ n while W1(X,Y ) ∼ n. If all the points alternate in an equispaced way, Greedyp(X,Y ) ∼ n1−p and W1(X,Y ) ∼ 1. The proof shows that cp ∼ 1 + 2p for p small. There is a clear change around p = 1/2, the greedy matching becomes less effective (see also Fig. 8). We also note a result of Bobkov-Ledoux [6] in one dimension: the optimal transport cost for d(x,y)p and 0 < p < 1 is, in expectation, smaller than the one induced by the ordered optimal p = 1 matching.

0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0

### Figure 5. Examples where the Theorem is sharp (0 < p < 1/2).

- 2.2. Greedy is non-crossing. It is known (see McCann [21]) that if we match

points {x1,...,xn} to {y1,...,yn} under a cost function c(x,y) = h(|x − y|) with h ≥ 0 concave, then the optimal matching satisfies a non-crossing condition which

can be described as follows: if the optimal matching sends xi to yπ(i), then the n circles Ci that go tangentially though xi and yπ(i), the circles

Ci = z ∈ R2 : z −

xi + yπ(i) 2

=

yπ(i) − xi 2

,

do not intersect. The greedy matching has this desirable property for trivial reasons.

Figure 6. The circles Ci for an example of n = 100 points greedily matched with another n points under c(x,y) = |x − y|0.01.

- Proposition 1. The greedy matching is non-crossing.


Proof. The argument is very simple. Suppose i < j and circle Ci intersects circle Cj. Ci intersects xi and yπ(i) while Cj intersects xj and xπ(j). Suppose w.l.o.g. xi < yπ(i) (otherwise relabel X and Y ). Since Ci and Cj intersect we have to either have xi < xj < yπ(i) or xi < yπ(j) < yπ(i) but either of these cases leads to a contradiction at stage i of the greedy algorithm. □

- 2.3. Random Points I. One of the most interesting cases is naturally that of matching random points to random points. Here, we can show that the greedy matching leads to nontrivial results.


- Corollary 1. Let X,Y be two sets of n uniform i.i.d. random variables on [0,1]d. The greedy matching subject to c(x,y) = ∥x − y∥p for 0 < p < 1/2 satisfies


 

n1−p when d = 1 and p < 1/4

- n1−p/2 when d = 1 and 1/4 ≤ p < 1/2
- n1−p/2 when d = 2 n1−p/d when d ≥ 3.


E Greedyp(X,Y ) ≤ cp ·



Of these, the first inequality (d = 1 and 0 < p < 1/4) is optimal up to constants. It seems likely to assume that, when d = 1 and p < 1/2, we have E Greedyp(X,Y ) ≤ cp · n1−p. Even stronger results seem to be true: the greedy matching appears to be remarkably close to the cost function, even at the pointwise level. The Dyck matching is known to produce an optimal rate.

- Theorem 2 (Caracciolo-D’Achille-Erba-Sportiello [10]). For various different models of n random points on [0,1], we have

E(Dyckn) ∼

 



n1−p if 0 < p < 12 n1/2 log n if p = 12 n1/2 if 21 < p ≤ 1.

The Dyck matching is an a priori global construction that is naturally connected to the structure of a Brownian bridge, a fact that allows for a variety of tools to be applied. Conversely, the greedy algorithm is a ‘blind’ local algorithm: it is difficult to predict what it will do without running it. As such, proving a result along the lines of Caracciolo-D’Achille-Erba-Sportiello [10] for the greedy matching appears to be difficult and in need of new ideas.

- 2.4. Random points II. More can be said if we assume that the points are chosen uniformly at random with respect to a fixed probability measure µ since one would then expect a certain limiting behavior to arise. This is indeed the case.


- Theorem 3 (Barthe-Bordenave [3], special case). Let 0 < p < d/2 and µ be the uniform measure on a bounded set Ω ⊂ Rd. If X,Y are i.i.d. copies from µ, then

lim

n→∞

n

p

d−1 · Wpp(X,Y ) = βp(d) · |Ω|

p

d.

When d = 1, the result has recently been extended by Goldman-Trevisan [18] to also allow for randomness with respect to variable absolutely continuous density.

- Theorem 4 (Goldman-Trevisan [18], special case). Let 0 < p < 1/2. There exists cp > 0 such that for compactly supported µ with a.c. density f(x)dx


np−1 · Wpp(X,Y ) = cp

f(x)1−pdx.

lim

n→∞

R

The restriction p < 1/2 is necessary, the behavior is strictly different at p = 1/2 (this is the scale where the fluctuations of the empirical distribution of the points starts to come into play). Since the uniform measure is a special case of a measure of the form f(x)dx, the implicit (universal) constants are the same as in the result of Barthe-Bordenave in the sense of cp = βp(1). We provide an easy explicit lower bound on these constants.

- Proposition 2. Let 0 < p < d/2. Then


p d

p d

βp(d) ≥ ω−

d · Γ 1 +

, where ωd is the volume of the unit ball in Rd.

The argument is not terribly difficult and somewhat standard for these types of problems, see [22]. The bound seems to be rather accurate for small values of p. As a consequence, we obtain two-sided bounds in the one-dimensional setting when p is close to 0. There is an interesting heuristic: we expect that the optimal matching will send most points distance ∼ c · n−1 with c ∼ 1 ranging over some different values but being approximately at order ∼ 1 and thus the cost should be close to ∼ cp · n1−p. However, since p ∼ 0+, one expects cp ∼ 1 and thus that the optimal transport cost is perhaps given by (1 + O(p)) · n1−p.

- Corollary 2 (Prop. 2 and [10]). For 0 < p < 1/2,


2p Γ(1 − p)

1 1 − 2p

2−p · Γ(1 + p) ≤ β1(p) ≤

In particular, we conclude that β1(p) = 1 + O(p) when p ∼ 0 is small.

- 2.5. Extreme concave matching. The cost c(x,y) = |x − y|p is particularly natural. There is, in a suitable sense, a canonical limit as p → 0+ since

lim

p→0+

|x − y|p − 1 p

= log |x − y|.

- As suggested by Fig. 2, the greedy algorithm performs very well in this setting. We prove a basic result suggesting that this is not a coincidence.


- Proposition 3. Let X,Y be two sets of n distinct points in a metric space such


that d(xi,yj) ≤ 1 and assume that all pairwise distances are unique. Then there exists K ∈ N such that for all k ≥ K the solution of the optimal matching problem

min

π∈Sn

n

i=1

log d(xi,yπ(i)) 2k+1 is given by the greedy matching.

The argument is quite simple and there is nothing particularly special about the logarithm, similar results could be attained with many other cost functions that are dramatically different across different length scales. The main point of this simple Proposition is to illustrate that the effectiveness of the greedy matching in the setting of very concave cost functions is perhaps not entirely surprising: the dramatic separation of scales puts a heavy reward on having matching with very small distance which, coupled with the separation of scales, then suggests the greedy algorithm as a natural object.

- 2.6. Numerics. The purpose of this section is to consider the behavior of the greedy algorithm and the Dyck matching when matching n i.i.d. random points on [0,1] given the cost function c(x,y) = |x − y|p for 0 ≤ p ≤ 1/2. The results suggest that, at least for random points, the greedy matching leads to results that are remarkably close to the ground truth: this effect becomes more pronounced when p becomes smaller (also at least partially suggested by the Proposition).


Approximation

greedy

1.15

1.10

1.05

Dyck

1.00

p

0.2 0.4 0.6 0.8 1.0

Figure 7. Average ratio of cost divided by the minimal cost for both the Dyck matching and the greedy matching for n = 250 iid points subject to the cost function c(x,y) = |x − y|p.

The effectiveness of the greedy algorithm is strictly restricted to the region 0 < p < 1/2: for p ≥ 1/2, the greedy algorithm starts to scale differently and becomes less effective. This can already be observed for small values of n (and is pointed out by d’Achille [1, Section 1.4] for p ≥ 1). We also observe that, as p becomes smaller, the effectiveness of the greedy matching increases dramatically while, for p close to 1, the effectiveness of the Dyck matching increases dramatically (see Fig. 8). The Dyck matching is optimal when p = 1 (see [11]).

Approximation

Approximation

1.0025

1.008

1.0020

1.006

1.0015

1.004

### greedy

1.0010

1.002

Dyck

1.0005

p

p

0.02 0.04 0.06 0.08 0.10

0.92 0.94 0.96 0.98 1.00

Figure 8. Ratio of obtained matching cost divided by the minimal cost for n = 100 random points. Left: the greedy matching when p ∼ 0. Right: the Dyck matching when p ∼ 1.

Fig. 8 is well suited to iterate a main contribution of our paper: when d = 1 and considering matchings with c(x,y) = d(x,y)p and 0 < p < 1, there exists a natural dichotomy depending on whether p is close to 0 or whether it is close to 1.

greedy c(x,y) = d(x,y)p Dyck

(d = 1)

0 p 1

A natural question is, for example, whether one can identify the precise value 0 < p∗ < 1 where the effectiveness of the two algorithms undergoes a phase transition and the matching problem for n iid random points is better approximated by the Dyck matching or the greedy matching, respectively.

3. Proof of Theorem 1

Proof. We assume the sets of points are X = {x1,...,xn} and Y = {y1,...,yn} and we will use Xk,Yk to denote the set of points after k − 1 points have been removed following the greedy algorithm. In particular, X = X1 and Y = Y1. We will also abbreviate the cost at stage k via

d(x,y). Our goal is to estimate

ck = inf

x∈Xk,y∈Yk

the cost of the greedy algorithm

n

cpk.

k=1

Recalling that, by definition, Xk and Yk have n−k+1 elements each, the Wasserstein distance W1 can be written as

W1(Xk,Yk) = min

d(x,π(x))

π:Xk→Yk

π bijective x∈Xk

where the minimum ranges over all bijections. At this point, we remark that the definition of W1 is slightly more comprehensive (the infimum ranges over all ways of splitting and rearranging points): at this point, we employ the celebrated result of Birkhoff [4] and von Neumann [24] ensuring that in the case of n equal masses being transported to n equal masses, the optimal solution can be realized by a permutation (no mass is ‘split’), we refer to [19] for a generalization. Our first observation uses averaging. Let us use π to denote the permutation achieving the optimal W1 transport cost. Then the distance achieved by the greedy matching in the k−th step can be bounded from above by

W1(Xk,Yk) n − k + 1

1 n − k + 1 x∈X

d(x,y) ≤

d(x,π(x)) =

.

ck = inf

x∈Xk,y∈Yk

k

The second ingredient will be to show that W1(Xk+1,Yk+1) cannot be much larger than W1(Xk,Yk). For this purpose, let us assume that Xk is given by the points x1,x2,...,xn−k+1 and, similarly, Yk is given by y1,y2,...,yn−k+1. Then, after possibly relabeling the points, we have that

n−k+1

d(xi,yi).

W1(Xk,Yk) =

i=1

Let us now assume that the greedy matching at this point matches xi and yj, meaning that d(xi,yj) is the smallest pairwise distance in Xk × Yk. Then the greedy matching is going to match these two points up and the remaining sets of points are given by

Xk+1 = Xk \ {xi} and Yk+1 = Yk \ {yj}.

We will provide an upper bound on W1(Xk+1,Yk+1) by taking the original matching between Xk and Yk and then modify it a little to obtain a matching for Xk+1 with Yk+1. This is done by a simple modification: the point xj is now mapped to yi (note that xi has been mapped to yj and both have been removed from the set). We preserve all other matchings. Then

W1(Xk+1,Yk+1) ≤ W1(Xk,Yk) + d(xj,yi) − d(xi,yi) − d(xj,yj).

- At this point, we invoke the triangle inequality and argue that d(xj,yi) ≤ d(xj,yj) + d(yj,yi)


≤ d(xj,yj) + d(yj,xi) + d(xi,yi)

Combining the last two inequalities, we realize that we can bound the increase in the W1-distance between the two sets in terms of the cost function of the greedy matching at the k−th step by

W1(Xk+1,Yk+1) ≤ W1(Xk,Yk) + d(xj,yi) − d(xi,yi) − d(xj,yj) ≤ W1(Xk,Yk) + d(xi,yj)

= W1(Xk,Yk) + ck.

Combining these two ingredients, we arrive W1(Xk+1,Yk+1) ≤ W1(Xk,Yk) + ck ≤ W1(Xk,Yk) +

W1 (Xk,Yk) n − k + 1

1 n − k + 1

= W1(Xk,Yk) 1 +

By induction, we obtain

.

Observe that

k−1

W1(Xk,Yk) ≤ W1(X,Y ) ·

ℓ=1

1 n − ℓ + 1

1 +

.

k−1

k−1

n − ℓ + 2 n − ℓ + 1

n + 1 n − k + 2

1 n − ℓ + 1

=

=

.

1 +

ℓ=1

ℓ=1

Therefore

n + 1 n − k + 2 · W1(X,Y ). Applying the pigeonhole principle one more time, we see that

W1(Xk,Yk) ≤

n + 1

W1 (Xk,Yk) n − k + 1 ≤

(n − k + 1)2 · W1(X,Y ). Thus

ck ≤

n

n

1 (n − k + 1)2p

cpk ≤ W1(X,Y )p · (n + 1)p ·

.

k=1

k=1

We have

n

n

1 (n − k + 1)2p

1 k2p

=

.

k=1

k=1

When 0 < p < 1/2, we have

n

n+1

(n + 1)1−2p 1 − 2p

1 k2p ≤ 1 +

1 x2p

dx ≤ 1 +

.

1

k=1

Dealing with the remaining cases in the usual fashion, we obtain

 

n1−p if 0 < p < 12 √n · log n if p = 12 np if 12 < p < 1.

n

cpk ≤ cp · W1(X,Y )p ·



k=1

The argument also shows that, for p < 1/2 we have

1 1 − 2p

+ o(1) · n1−p · W1(X,Y ).

Greedyp(X,Y ) ≤

In particular, for p close to 0, we have that that 1/(1−2p) ∼ 1+2p and the implicit constant is close to 1. □

## 3.1. Proof of Corollary 1.

Proof. Corollary 1 follows immediately from the Theorem. The missing ingredient is a good estimate on W1(X,Y ) where X and Y are two sets of n i.i.d. uniformly distributed points in [0,1]d. The case d = 2 is arguably the most famous, the celebrated result of Ajtai, Komlos, Tusnady [2] ensures that

n

c1 nlog n ≤ min π∈Sn

∥xi − yπ(i)∥ ≤ c2 nlog n.

i=1

with high probability. The one-dimensional case is a bit simpler and one has (see, for example, [5]), with high probability,

n

∥xi − yπ(i)∥ ≤ c√n. The case d ≥ 3 where

min

π∈Sn

i=1

n

|xi − yπ(i)| ≤ c · n1−1/d

min

π∈Sn

i=1

was already remarked by Ajtai, Komlos, Tusnady [2]. A modern treatment of a much more general case is given in [16]. This proves that, for X and Y i.i.d. random points and p < 1/2

 

n1−p/2 when d = 1 n1−p/2 · (log n)p/2 when d = 2 n1−p/d when d ≥ 3.

E Greedyp(X,Y ) ≤ cp ·



There is a slight improvement that was pointed out to us by an anonymous referee. For any 0 < α < 1, we can write

n

n

∥xi − yπ(i)∥α p/α .

∥xi − yπ(i)∥p =

i=1

i=1

If d(x,y) is a metric, then d(x,y)α is also a metric for every 0 < α < 1. Moreover, since x → xα is monotonically increasing, the greedy algorithm with respect to the metric d(x,y)α picks the exact same matching as the greedy algorithm with respect to d(x,y). We use W1,α to denote the Wasserstein-1 distance with respect to the metric dα(x,y) = ∥x − y∥α. Applying Theorem 1 to this new metric, we get that, assuming xi ↔ yi to be the greedy matching and 0 < p/α < 1 instead of p, then

 

n1−p/α if 0 < p/α < 12 √n · log n if p/α = 12 np/α if 12 < p < 1,

n

∥xi − yi∥p ≤ cp,α (W1,α(X,Y ))p/α ·



i=1

where

n

∥xi − yπ(i)∥α.

W1,α(X,Y ) = inf

π∈Sn

i=1

The result of Barthe-Bordenave [3] implies that as long as α < d/2 and the X,Y are i.i.d. random variables with respect to the uniform measure, then

n

∥xi − yπ(i)∥α ≲ n1−α/d.

inf

π∈Sn

i=1

### Combining all these results, assuming that 0 < α < 1 as well as 0 < p < α and α < d/2, then

 

n1−p/d if 0 < p/α < 21 n1−p/d · log n if p/α = 12 np(2/α−d) if 12 < p/α < 1.

n

∥xi − yi∥p ≤ cp,α



i=1

The first case improves on the previous estimate when d = 1, this requires α < 1/2 and thus p < 1/4. When d = 2, then for any p < 1/2 we can find p < α < 1 such that p/α < 1/2 which implies the upper bound n1−p/2 without logarithmic corrections. Altogether, this gives, for 0 < p < 1/2

 

n1−p when d = 1 and p < 1/4

- n1−p/2 when d = 1 and 1/4 ≤ p < 1
- n1−p/2 when d = 2 n1−p/d when d ≥ 3.


E Greedyp(X,Y ) ≤ cp ·



□

- 3.2. Proof of Proposition 2. Since the constant is independent of the domain, it will be enough to derive an upper bound in a fixed, arbitrary domain. We choose the unit cube [0,1]d for convenience, however, we emphasize that there is nothing particularly special about the unit cube.


Lemma. Given n i.i.d. uniform points X1,...,Xn in [0,1]d and an independent uniform point Y , we have for all sufficiently small 0 < ε < ε0 that whenever Y is sufficiently far from the boundary of the unit cube d(Y,∂[0,1]d) ≥ ε, then

|Y − Xi| ≥ ε) = 1 − ωdεd n ,

P( min

1≤i≤n

where ωd is the volume of the unit ball in Rd. Proof. Conditional on Y , since the Xi’s are all independent, we obtain

|Y − Xi| ≥ ε|Y ) = 1 − |BY (ε) ∩ [0,1]d| n .

P( min

1≤i≤n

Since d(Y,∂[0,1]d) ≥ ε, we have 1 − |BY (ε) ∩ [0,1]d| n = (1 − ωdεd)n.

A simple monotonicity argument guarantees that for all ε the conclusion still holds, up to replacing = with ≥. □

Proof of Proposition 2. We assume the sets of points {X1,...,Xn} ⊂ [0,1]d and {Y1,...,Yn} ⊂ [0,1]d are both sets of independent uniformly distributed random variables in [0,1]d. The main idea is the use of the trivial bound

n

n

d(xi,yπ(i))p ≥

E inf

π∈Sn

i=1

i=1

|Yi − x|p = nE min

|Xi − Y |p

E inf

x∈X

1≤i≤n

We introduce a change of coordinates ε = cp/np/d. Then, for all sufficiently small ε (i.e., for fixed c,p,d and n → +∞), we have

c n1/d

|Xi − Y |p ≥ ε = P min

P min

|Xi − Y | ≥

1≤j≤n

1≤j≤n

n

ωdcd n

dcd. As we remarked earlier, for all ε ≥ 0 (i.e., for all c) we have

→ e−ω

= 1 −

dcp, so that we obtain, as n → +∞,

|Xi − Y |p ≥ ε ≥ e−ω

P min

1≤j≤n

∞

|Xi − Y |p = n

|Xi − Y |p ≥ ε dϵ

n · E inf

P min

1≤i≤n

1≤j≤n

0

+∞

dcddc

pcp−1e−ω

=

0

p d

p d

· w−

p d

= n1−

d · Γ 1 +

.

We note that the argument slightly improves when Xi is close to the boundary (since then the volume of a neighborhood intersected with [0,1]d has smaller volume). However, since the number of points distance ∼ n−1/d close to the boundary is ∼ n(d−1)/d ≪ n, exploiting this fact would not lead to better asymptotics. □

## 3.3. Proof of Proposition 3.

Proof. Since 0 < d(xi,yj) < 1, all the summands are negative and can use the trivial estimate

n

log d(xi,yπ(i)) 2k+1

log d(xi,yπ(i)) 2k+1 ≤

n min

1≤i≤n

i=1

log d(xi,yπ(i)) 2k+1 . Suppose now that

≤ min

1≤i≤n

d(xi,yj). Then, for all k ≥ K1 sufficiently large,

min

d(xi,yπ(i)) > min

1≤i≤n

1≤i,j≤n

log d(xi,yπ(i)) 2k+1 > min

(log d(xi,yj))2k+1

n min

1≤i≤n

1≤i,j≤n

since one grows exponentially larger than the other. This shows that any optimal matching has to at least coincide with the greedy matching in the first step. We emove the closest pair of points (xi,yj) and repeat the procedure on the remaining set of points. We see that for all k ≥ K2, the next step has to coincide with that of the greedy matching. Repeating the procedure, we see that for all K ≥ max(K1,...,Kn−1) the minimum can only be given by the greedy matching. □

Acknowledgment. The authors gratefully acknowledge support from the Kantorovich Initiative. A.O. is supported by an AMS-Simons Travel Grant. S.S. was

supported by the NSF (DMS-2123224). The authors are indebted to Aleh Tsyvinski for drawing their attention to the problem and to an anonymous referee for suggesting improved rates for Corollary 1.

References

- [1] M. D’Achille, Statistical properties of the Euclidean random assignment problem, PhD Thesis, Universite Paris-Saclay, 2020.
- [2] M. Ajtai, J. Komlos and G. Tusnady, On optimal matchings. Combinatorica, 4 (1984), p. 259-264.
- [3] F. Barthe and C. Bordenave, Combinatorial optimization over two random point sets. In: Seminaire de probabilites XLV. Cham: Springer, 2013, pp. 483–535
- [4] G. Birkhoff. Tres observaciones sobre el algebra lineal. Universidad Nacional de Tucuman Revista Series A, 5:147–151, 1946
- [5] S. Bobkov and M. Ledoux, M. One-dimensional empirical measures, order statistics, and Kantorovich transport distances (Vol. 261, No. 1259). American Mathematical Society, 2019.
- [6] S. Bobkov and M. Ledoux, Transport inequalities on Euclidean spaces for non-Euclidean metrics. Journal of Fourier Analysis and Applications, 26 (2020), 60.
- [7] S. Bobkov and M. Ledoux, Correction: Transport Inequalities on Euclidean Spaces for NonEuclidean Metrics. Journal of Fourier Analysis and Applications, 30 (2024), 56.
- [8] J. Boerma, A. Tsyvinski, R. Wang, Z. Zhang, Composite Sorting, arXiv:2303.06701
- [9] L. Brown and S. Steinerberger, On the Wasserstein distance between classical sequences and the Lebesgue measure. Transactions of the American Mathematical Society, 373 (2020), p. 8943-8962.
- [10] S. Caracciolo, M. D’Achille, V. Erba and A. Sportiello, The Dyck bound in the concave 1dimensional random assignment model. Journal of Physics A: Mathematical and Theoretical, 53 (2020), 064001.
- [11] S. Caracciolo, V. Erba and A. Sportiello, The number of optimal matchings for Euclidean Assignment on the line, Journal of Statistical Physics 183 (2021), p. 1–27
- [12] S. Caracciolo, V. Erba and A. Sportiello, The p−Airy distribution, arXiv:2010.14468
- [13] J. Delon, J. Salomon and A. Sobolevski, Local matching indicators for concave transport costs. Comptes Rendus Mathematique, 348 (2010), 901-905.
- [14] J. Delon, J. Salomon and A. Sobolevski, Local matching indicators for transport problems with concave costs. SIAM Journal on Discrete Mathematics, 26 (2012), 801-827.
- [15] P. Diaconis, Group representations in probability and statistics. Lecture notes-monograph series, 11 (1988/1/1).
- [16] N. Fournier and A. Guillin, On the rate of convergence in Wasserstein distance of the empirical measure. Probability theory and related fields, 162 (2015), 707-738.
- [17] W. Gangbo and R. McCann, The geometry of optimal transportation, Acta Math. 177 (1996), p. 113-161
- [18] M. Goldman and D. Trevisan, On the concave one-dimensional random assignment problem and Young integration theory, arXiv:2305.09234
- [19] B. Hosseini and S. Steinerberger, Intrinsic Sparsity of Kantorovich solutions. Comptes Rendus. Mathe´matique, 360(G10), 1173-1175, 2022.
- [20] N. Juillet, On a solution to the Monge transport problem on the real line arising from the strictly concave case. SIAM Journal on Mathematical Analysis, 52 (2020), 4783-4805.
- [21] R. McCann, Exact solutions to the transportation problem on the line. Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences, 455

(1999), 1341-1380.

- [22] J. M. Steele, Probability theory and combinatorial optimization. Society for Industrial and Applied Mathematics, 1997.
- [23] S. Steinerberger, A Wasserstein inequality and minimal Green energy on compact manifolds, Journal of Functional Analysis, 281 (2021), 109076.
- [24] J. von Neumann, A certain zero-sum two-person game equivalent to an optimal assignment problem, Ann. Math. Studies 28:5–12, 1953.
- [25] P. Zinterhof, Uber einige Abschatzungen bei der Approximation von Funktionen mit Gleichverteilungsmethoden. Osterreich. Akad. Wiss. Math.-Naturwiss. Kl. S.-B. II 185 (1976), no. 1-3, 121–132.


Cowles Foundation, Yale University Email address: andrea.ottolini@yale.edu

Department of Mathematics, University of Washington, Seattle Email address: steinerb@uw.edu

