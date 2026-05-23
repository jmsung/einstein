arXiv:1402.6011v3[math.CO]3Feb2016

ON THE VARIATIONAL PROBLEM FOR UPPER TAILS IN SPARSE RANDOM GRAPHS

EYAL LUBETZKY AND YUFEI ZHAO

Abstract. What is the probability that the number of triangles in Gn,p, the Erd˝s-Re´nyi random graph with edge density p, is at least twice its mean? Writing it as exp[−r(n, p)], already the order of the rate function r(n, p) was a longstanding open problem when p = o(1), ﬁnally settled in 2012 by Chatterjee and by DeMarco and Kahn, who independently showed that r(n, p) ≍ n2p2 log(1/p) for p lognn; the exact asymptotics of r(n, p) remained unknown.

![image 1](<2014-lubetzky-variational-problem-upper-tails_images/imageFile1.png>)

The following variational problem can be related to this large deviation question at p lognn: for δ > 0 ﬁxed, what is the minimum asymptotic p-relative entropy of a weighted graph on n vertices with triangle density at least (1 + δ)p3? A beautiful large deviation framework of Chatterjee and Varadhan (2011) reduces upper tails for triangles to a limiting version of this problem for ﬁxed p. A very recent breakthrough of Chatterjee and Dembo extended its validity to n−α ≪ p ≪ 1 for an explicit α > 0, and plausibly it holds in all of the above sparse regime.

![image 2](<2014-lubetzky-variational-problem-upper-tails_images/imageFile2.png>)

In this note we show that the solution to the variational problem is min{21δ2/3 , 13δ} when

![image 3](<2014-lubetzky-variational-problem-upper-tails_images/imageFile3.png>)

![image 4](<2014-lubetzky-variational-problem-upper-tails_images/imageFile4.png>)

n−1/2 ≪ p ≪ 1 vs. 21δ2/3 when n−1 ≪ p ≪ n−1/2 (the transition between these regimes is expressed in the count of triangles minus an edge in the minimizer). From the results of

![image 5](<2014-lubetzky-variational-problem-upper-tails_images/imageFile5.png>)

Chatterjee and Dembo, this shows for instance that the probability that Gn,p for n−α ≤ p ≪ 1 has twice as many triangles as its expectation is exp[−r(n, p)] where r(n, p) ∼ 31n2p2 log(1/p). Our results further extend to k-cliques for any ﬁxed k, as well as give the order of the upper tail rate function for an arbitrary ﬁxed subgraph when p ≥ n−α.

![image 6](<2014-lubetzky-variational-problem-upper-tails_images/imageFile6.png>)

1. Introduction

The following question regarding upper tails for triangle counts in Gn,p, the Erd˝os-Re´nyi random graph with edge density p, has been extensively studied, being a representing example of large deviations for subgraph counts in random graphs (see, e.g., [4,7,8,12–15,21] as well as [2,11] and the references therein):

Question. What is the probability that the number of triangles in Gn,p is at least twice its mean, or more generally, larger by a factor of 1 + δ for δ > 0 ﬁxed?

In the dense case (p ﬁxed), the limiting asymptotics of the rate function — the normalized logarithm of this probability, here denoted by r(n,p,δ) — was reduced to an analytic variational problem on symmetric functions f : [0,1]2 → [0,1] (for a large class of large deviation questions) by Chatterjee and Varadhan [6]. However, for p = o(1), obtaining the order of r(n,p,δ) was already a longstanding open problem. That n2p2 r(n,p,δ) n2p2 log(1/p) followed from the works of Vu [21] and Kim and Vu [15] (see also [12]), and this question was ﬁnally settled in 2012 by Chatterjee [4] and by DeMarco and Kahn [8], where it was independently shown that

- r(n,p,δ) ≍ n2p2 log(1/p) for p lognn (see [4,8] for an account of the rich related literature).


![image 7](<2014-lubetzky-variational-problem-upper-tails_images/imageFile7.png>)

The exact asymptotics of this rate function was not known for any lognn p ≪ 1.

![image 8](<2014-lubetzky-variational-problem-upper-tails_images/imageFile8.png>)

Note that for the dense regime of ﬁxed p, while [6] provided a closed form for the rate function in terms of the above variational problem, its solution is only known in a subset of the range of parameters (p,δ) known as the replica symmetric phase (where the excess in the number of triangles is explained by encountering too many edges that are essentially uniformly distributed), and little is known on its complement (the symmetry breaking phase; see our previous work [19] where this phase diagram was determined).

![image 9](<2014-lubetzky-variational-problem-upper-tails_images/imageFile9.png>)

Y. Zhao was supported by a Microsoft Research Ph.D. Fellowship.

1

The variational problem in [6] can be viewed, via Szemere´di’s regularity lemma [20] and the theory of graph limits by Lov´asz et al. [3,17,18], as the limit of the following problem. Deﬁnition (Discrete variational problem for upper tails of triangles). Let Gn denote the set of weighted undirected graphs on n vertices with edge weights in [0,1], i.e.,

Gn = G = (gij)1≤i<j≤n : 0 ≤ gij ≤ 1 , gij = gji , gii = 0 for all i,j . The variational problem for δ > 0 and 0 < p < 1 is given by

φ(n,p,δ) := inf Ip(G) : G ∈ Gn with t(G) ≥ (1 + δ)p3 , (1.1) where

t(G) := n−3

gijgjkgik

1≤i,j,k≤n

is the density of (labeled) triangles in G, and Ip(G) is its entropy relative to p, i.e., Ip(G) :=

x p

1 − x 1 − p

Ip(gij) with Ip(x) := xlog

+ (1 − x)log

.

![image 10](<2014-lubetzky-variational-problem-upper-tails_images/imageFile10.png>)

![image 11](<2014-lubetzky-variational-problem-upper-tails_images/imageFile11.png>)

1≤i<j≤n

Indeed, it follows from the powerful large deviation framework of [6] that for p ﬁxed (the dense regime) n12 log P t(Gn,p) ≥ (1 + δ)p3 tends as n → ∞ to the limit of −φ(n,p,δ)/n2.

![image 12](<2014-lubetzky-variational-problem-upper-tails_images/imageFile12.png>)

However, in the sparse regime of p = o(1), which lacks the rich set of tools that are based on Szemere´di’s regularity lemma for dense graphs, there were no counterparts to this result until a very recent breakthrough by Chatterjee and Dembo [5]. There it was shown that the discrete variational problem (1.1) does govern the rate function of subgraph counts as long as p ≥ n−α for a suitable constant α. In particular, for triangle counts (see [5, Theorem 1.2] and the remark following it, yielding a slightly wider range than the one stated next) one has that

P t(Gn,p) ≥ (1 + δ)p3 = exp [−(1 − o(1))φ(n,p,δ)] (1.2) whenever n−1/42 log n ≤ p ≪ 1 (this should extend to smaller p, as commented in [5]; in fact, it is plausible that this result holds throughout the sparse regime of lognn ≪ p ≪ 1.)

![image 13](<2014-lubetzky-variational-problem-upper-tails_images/imageFile13.png>)

In this note we establish the following for the discrete variational problem (1.1).

- Theorem 1.1. Fix δ > 0. If n−1/2 ≪ p ≪ 1, then


φ(n,p,δ) n2p2 log(1/p)

lim

= min

![image 14](<2014-lubetzky-variational-problem-upper-tails_images/imageFile14.png>)

n→∞

On the other hand, if n−1 ≪ p ≪ n−1/2, then lim

φ(n,p,δ) n2p2 log(1/p)

=

![image 15](<2014-lubetzky-variational-problem-upper-tails_images/imageFile15.png>)

n→∞

δ2/3 2

,

![image 16](<2014-lubetzky-variational-problem-upper-tails_images/imageFile16.png>)

δ 3

![image 17](<2014-lubetzky-variational-problem-upper-tails_images/imageFile17.png>)

. (1.3)

δ2/3 2

. (1.4)

![image 18](<2014-lubetzky-variational-problem-upper-tails_images/imageFile18.png>)

One can then deduce the following from the above result (1.2) of Chatterjee and Dembo. Corollary 1.2. For any δ > 0, if n−1/42 log n ≤ p ≪ 1 then

P t(Gn,p) ≥ (1 + δ)p3 = exp −(1 − o(1))min 12δ2/3 , 13δ n2p2 log(1/p) .

![image 19](<2014-lubetzky-variational-problem-upper-tails_images/imageFile19.png>)

![image 20](<2014-lubetzky-variational-problem-upper-tails_images/imageFile20.png>)

The lower bound is explained by forcing either a set of k = δ1/3np vertices to be a clique

(with probability p(k2) = p(δ2/3/2+o(1))n2p2) or a set of ℓ = 31δnp2 vertices to be connected to all other vertices (with probability pℓ(n−ℓ) = p(δ/3+o(1))n2p2), the latter being preferable if and only if δ < 27/8.

![image 21](<2014-lubetzky-variational-problem-upper-tails_images/imageFile21.png>)

In fact, these constructions for the lower bound on P t(Gn,p) ≥ (1 + δ)p3 further explain the two separate regimes in Theorem 1.1. When p ≪ 1/√n, the second (bipartite) construction — involving ℓ ≍ np2 vertices — ceases to be a viable option, as then we have ℓ = o(1). As remarked next, this translates into a qualitative diﬀerence between the solutions of the variational problem in each of these regimes, expressed in terms of

![image 22](<2014-lubetzky-variational-problem-upper-tails_images/imageFile22.png>)

gij 2 ,

s(G) := n−3

1≤i≤n 1≤j≤n

equivalent to the asymptotic density of triangles minus an edge (i.e., K1,2 homomorphisms, which in Gn,p have average density p2, and so an excess of 31δp2 in their density, of which a p-fraction forms triangles via an extra edge, translates to δp3 additional labeled triangles).

![image 23](<2014-lubetzky-variational-problem-upper-tails_images/imageFile23.png>)

Remark 1.3. The proof of Theorem 1.1 shows that for any ﬁxed 0 < δ < 278 , if Gn ∈ Gn is a sequence of weighted graphs satisfying t(Gn) ≥ (1 + δ)p3 and Ip(Gn) ∼ φ(n,p,δ) then

![image 24](<2014-lubetzky-variational-problem-upper-tails_images/imageFile24.png>)

1 + δ/3 if n−1/2 ≪ p ≪ 1, 1 if n−1 ≪ p ≪ n−1/2 .

s(Gn) p2

=

lim

![image 25](<2014-lubetzky-variational-problem-upper-tails_images/imageFile25.png>)

n→∞

For ﬁxed δ > 278 , the term 1 + δ/3 in the ﬁrst case (n−1/2 ≪ p ≪ 1) is replaced by 1.

![image 26](<2014-lubetzky-variational-problem-upper-tails_images/imageFile26.png>)

Regarding the behavior when p ≍ n−1/2, there one expects a similar structure: i.e., whenever the bipartite construction is preferable, the optimal solution should feature a large bipartite subgraph while adhering to the integrality restrictions. It is plausible that methods similar to those used in this work can establish the solution in that regime as well.

Our arguments extend to yield analogous results for k-clique counts, where, for instance, the right-hand side of (1.3) (giving the asymptotics of the rate function provided n−α′ ≪ p ≪ 1 for α′(k) > 0) is replaced by min{12δ2/k,δ/k}; see Theorem 4.1 and Corollary 4.2. For a general graph on k vertices, the order of the rate function at p ≥ n−α′′ is given by Corollary 4.5.1

![image 27](<2014-lubetzky-variational-problem-upper-tails_images/imageFile27.png>)

Finally, it is worthwhile mentioning that even without appealing to the new machinery of [5], if p tends to 0 suﬃciently slowly with n — namely, (log n)−1/6 ≪ p ≪ 1 — then Eq. (1.2) (stating that the variational problem (1.1) gives the asymptotic rate function for large deviations of triangles) follows essentially from the framework of Chatterjee and Varadhan [6] (and similarly for any ﬁxed subgraph); instead of using the theory of graph limits or Szemere´di’s regularity lemma, one can derive this statement by appealing in their framework to the weak regularity lemma of Frieze and Kannan [10] (we include this reduction for completeness; see §5).

Notation and organization. On occasion we will write fn gn instead of fn = O(gn) for brevity, as well as fn ≪ gn instead of fn = o(gn) (similarly for fn gn and fn ≫ gn); we let fn ∼ gn denote fn = (1 + o(1))gn, and f ≍ g denotes fn gn fn.

![image 28](<2014-lubetzky-variational-problem-upper-tails_images/imageFile28.png>)

1In our follow-up work [1] jointly with Bhattacharya and Ganguly, we extend this and ﬁnd the asymptotic rate function for every graph H. The rate is given in terms of a certain independence polynomial, and exhibits a dichotomy with respect to δ if and only if H is a regular graph. See [1] for the statements of these newer results.

This paper is organized as follows. In §2 we give upper and lower bounds for the discrete variational problem (1.1): the construction of a clique/bipartite subgraph, and a (relaxed) continuous variational problem, whose solution we denote by φ(δ,p) (notice this variant no longer depends on n; see Eq. (2.1) below). The analysis of the latter appears in §3, and §4 contains the extension of these results to k-cliques for any ﬁxed k. Finally, §5 contains the reduction of the upper tail to the variational problem (1.1) when p → 0 as a poly-log of n.

2. A continuous variational problem

In this section we compare the optimum φ(n,p,δ) of the variational problem (1.1) with an analogue, φ(p,δ), that eliminates the dependence on n. Before introducing this variant, we begin with the straightforward upper bound on φ(n,p,δ), which involves constructing G ∈ Gn with Ip(G) that attains the right-hand side of (1.3). There are two competing candidates.

- • Let gij = 1 whenever 1 ≤ i < j ≤ a for some integer a to be speciﬁed later, and gij = p for all other i,j. Then we have

t(G) ≥ n−3 a(a − 1)(a − 2) + (n(n − 1)(n − 2) − a(a − 1)(a − 2))p3 and

Ip(G) = a2 Ip(1) = a2 log(1/p). So, we can choose a = (δ1/3 + o(1))pn so that t(G) ≥ (1 + δ)p3 and

Ip(G) =

δ2/3 2

![image 29](<2014-lubetzky-variational-problem-upper-tails_images/imageFile29.png>)

+ o(1) n2p2 log(1/p).

- • Let gij = 1 whenever 1 ≤ i ≤ a and i < j and gij = p otherwise. Then t(G) ≥ n−3 3a(n − a)(n − a − 1)p + (n − a)(n − a − 1)(n − a − 2)p3


and

a + 1 2

a + 1 2

Ip(G) = a n −

log(1/p). So, we can choose a = (δ/3 + o(1))p2n so that t(G) ≥ (1 + δ)p3 and Ip(G) =

Ip(1) = a n −

![image 30](<2014-lubetzky-variational-problem-upper-tails_images/imageFile30.png>)

![image 31](<2014-lubetzky-variational-problem-upper-tails_images/imageFile31.png>)

δ 3

+ o(1) n2p2 log(1/p).

![image 32](<2014-lubetzky-variational-problem-upper-tails_images/imageFile32.png>)

When p ≫ n−1/2, both constructions are valid, and taking the one with smaller Ip(G) (the choice depends on the value of δ; when δ ≥ 27/8 we use the ﬁrst construction and when δ < 27/8 we use the second construction) yields the upper bound on φ(n,p,δ) in (1.3).

When n−1 ≪ p ≪ n−1/2, the second construction is no longer valid (since a ≪ 1), but the ﬁrst construction remains valid. Thus, we obtain the upper bound on φ(n,p,δ) in (1.4).

Next, consider the following variant of the above variational problem. Whereas in φ(n,p,φ) the variational problem occurs in the space of weighted graphs on n vertices, in the new variational problem φ(p,φ), we consider the space of graphons, so that n does not appear (and the dependence of p on n plays no role). Here a graphon is a symmetric measurable function W : [0,1]2 → [0,1]. Let W denote the set of all graphons.

Given any graphon W and function f : R → R, we use the shorthand notation E[f(W)] :=

f(W(x,y))dxdy .

[0,1]2

For example, EW2 = [0,1]2 W2 dxdy, and E[Ip(W)] = [0,1]2 Ip(W(x,y))dxdy. Deﬁnition (Continuous variational problem). For δ > 0 and 0 < p < 1, let

- 1

![image 33](<2014-lubetzky-variational-problem-upper-tails_images/imageFile33.png>)

- 2


E[Ip(W)] : W ∈ W such that t(W) ≥ (1 + δ)p3 , (2.1) where the triangle density t(W) of W is deﬁned by

φ(p,δ) := inf

t(W) :=

W(x,y)W(x,z)W(y,z)dxdydz .

[0,1]3

The two variational problems (1.1) and (2.1) are related by the following inequality.

- Lemma 2.1. For any p,n,δ, we have


1 n2

φ(p,δ) ≤

φ(n,p,δ) +

![image 34](<2014-lubetzky-variational-problem-upper-tails_images/imageFile34.png>)

- 1

![image 35](<2014-lubetzky-variational-problem-upper-tails_images/imageFile35.png>)

- 2n


Ip(0). (2.2)

Proof. For any G ∈ Gn, we can construct a WG ∈ W by dividing [0,1] into n equal intervals I1,... ,In, and setting W(x,y) = gij whenever x ∈ Ii and y ∈ Ij. Then t(WG) = t(G) and

- 1

![image 36](<2014-lubetzky-variational-problem-upper-tails_images/imageFile36.png>)

- 2E[Ip(WG)] = n−2Ip(G) + (2n)−1Ip(0), where the extra term (2n)−1Ip(0) is due to the zero entries gii = 0 which were not included in Ip(G).


The following theorem, providing a solution to the variational problem φ(p,δ), is proved in the next section (see §3.1).

- Theorem 2.2. Fix δ > 0. Then


φ(p,δ) p2 log(1/p)

= min

lim

![image 37](<2014-lubetzky-variational-problem-upper-tails_images/imageFile37.png>)

p→0

δ2/3 2

,

![image 38](<2014-lubetzky-variational-problem-upper-tails_images/imageFile38.png>)

δ 3

![image 39](<2014-lubetzky-variational-problem-upper-tails_images/imageFile39.png>)

. (2.3)

It can already be seen that the solution to the variational problem (1.1) when n−1/2 ≪ p ≪ 1 (i.e., Eq. (1.3)) will readily follow from the combination of Lemma 2.1 and Theorem 2.2. We defer the full details — together with the treatment of the regime n−1 ≪ p ≪ n−1/2 (which will entail a short modiﬁcation of the proof of Theorem 2.2) to the next section following the proof of Theorem 2.2 (see §3.2).

For now, let us give the constructions that give tight upper bounds on φ(p,δ) for (2.3) precisely the graphon analogs of the above given constructions for Theorem 1.1.

- • Let W(x,y) = 1 whenever x,y ∈ [0,a] for some a ∈ [0,1] to be speciﬁed later, and W(x,y) = p elsewhere. Then we have


t(W) ≥ a3 + (1 − a)3p3 and

- 1

![image 40](<2014-lubetzky-variational-problem-upper-tails_images/imageFile40.png>)

- 2


- 1

![image 41](<2014-lubetzky-variational-problem-upper-tails_images/imageFile41.png>)

- 2


- 1

![image 42](<2014-lubetzky-variational-problem-upper-tails_images/imageFile42.png>)

- 2


a2Ip(1) =

a2 log(1/p).

E[Ip(W)] =

So, we can choose a = (δ1/3 + o(1))p so that t(W) ≥ (1 + δ)p3 and

δ2/3 2

- 1

![image 43](<2014-lubetzky-variational-problem-upper-tails_images/imageFile43.png>)

- 2


+ o(1) p2 log(1/p).

E[Ip(W)] =

![image 44](<2014-lubetzky-variational-problem-upper-tails_images/imageFile44.png>)

- • Let W(x,y) = 1 whenever min{x,y} ≤ a and W(x,y) = p otherwise. Then t(W) ≥ 3a(1 − a)2p + (1 − a)3p3


and

- 1

![image 45](<2014-lubetzky-variational-problem-upper-tails_images/imageFile45.png>)

- 2


a 2

a 2

E[Ip(W)] = a 1 −

log(1/p). So, we can choose a = (δ/3 + o(1))p2 so that t(G) ≥ (1 + δ)p3 and E[Ip(W)] =

Ip(1) = a 1 −

![image 46](<2014-lubetzky-variational-problem-upper-tails_images/imageFile46.png>)

![image 47](<2014-lubetzky-variational-problem-upper-tails_images/imageFile47.png>)

δ 3

- 1

![image 48](<2014-lubetzky-variational-problem-upper-tails_images/imageFile48.png>)

- 2


+ o(1) p2 log(1/p).

![image 49](<2014-lubetzky-variational-problem-upper-tails_images/imageFile49.png>)

Depending on the value of δ (when δ ≥ 27/8 use the ﬁrst construction; when δ < 27/8 use the second), these two examples together prove the upper bound to φ(p,δ) in (2.3).

3. Solving the variational problem

- 3.1. Proof of Theorem 2.2. Throughout this proof, we will occasionally require various


technical properties of the function Ip when p → 0; the proofs of these are deferred to §3.3. Let W ∈ W satisfy t(W) ≥ (1 + δ)p3. We wish to show that

δ2/3 2

δ 3

- 1

![image 50](<2014-lubetzky-variational-problem-upper-tails_images/imageFile50.png>)

- 2


p2Ip(1).

E[Ip(W)] ≥ (1 − o(1))min

,

![image 51](<2014-lubetzky-variational-problem-upper-tails_images/imageFile51.png>)

![image 52](<2014-lubetzky-variational-problem-upper-tails_images/imageFile52.png>)

Since Ip is decreasing in [0,p] and increasing in [p,1], we may assume without loss of generality that W ≥ p and t(W) = (1 + δ)p3. Write W = U + p, so that 0 ≤ U ≤ 1 − p. Letting

2

s(U) :=

U(x,y)U(x,z)dxdydz =

[0,1]3

U(x,y)dy

[0,1] [0,1]

dx,

we have

t(W) − p3 = t(U) + 3ps(U) + 3p2EU = δp3 . (3.1) Now write

t(U) = δ1p3, s(U) = δ2p2, and EU = δ3p. Then δ1 + 3δ2 + 3δ3 = δ. We may assume, for instance, that

√plog(1/p) = o(1), so that EU = o(p), since otherwise by the convexity of Ip and the fact that Ip(p + x) ∼ x2/(2p) for x ≪ p (see

δ3 ≤

![image 53](<2014-lubetzky-variational-problem-upper-tails_images/imageFile53.png>)

- Lemma 3.3 below) we would already have


E[Ip(W)] ≥ Ip(EW) = Ip(p + EU) ≥ Ip(p + p3/2 log(1/p)) ≫ p2Ip(1). The above decomposition reduces the problem to studying the following: φ′(p,δ1,δ2) := inf

- 1

![image 54](<2014-lubetzky-variational-problem-upper-tails_images/imageFile54.png>)

- 2


E[Ip(p+U)] : U ∈ W so that 0 ≤ U ≤ 1−p, t(U) ≥ δ1p3, and s(U) ≥ δ2p2 . The (asymptotic) solution to this variational problem is given by the following key lemma.

- Lemma 3.1. Fix D > 0. Then

φ′(p,δ1,δ2) =

δ12/3 2

![image 55](<2014-lubetzky-variational-problem-upper-tails_images/imageFile55.png>)

+ δ2 + o(1) p2Ip(1) uniformly for all δ1,δ2 ∈ [0,D] as p → 0.

Assuming Lemma 3.1, let us ﬁnish the proof of Theorem 2.2. We have E[Ip(W)] ≥ min{φ′(p,δ1,δ2) : δ1 + 3δ2 = δ − o(1)}

- 1

![image 56](<2014-lubetzky-variational-problem-upper-tails_images/imageFile56.png>)

- 2


= (1 − o(1))min

δ12/3 2

![image 57](<2014-lubetzky-variational-problem-upper-tails_images/imageFile57.png>)

+ δ2 : δ1 + 3δ2 = δ − o(1) p2Ip(1).

Note that if we ﬁx the value of δ1 + 3δ2, then δ12/3/2 + δ2 is minimized when one of δ1 and δ2 is set to zero. It follows that

- 1

![image 58](<2014-lubetzky-variational-problem-upper-tails_images/imageFile58.png>)

- 2


E[Ip(W)] ≥ (1 − o(1))min

δ2/3 2

![image 59](<2014-lubetzky-variational-problem-upper-tails_images/imageFile59.png>)

,

δ 3

![image 60](<2014-lubetzky-variational-problem-upper-tails_images/imageFile60.png>)

p2Ip(1).

We have thus established the desired lower bound for φ(p,δ) in Theorem 2.2, while the upper bound was already given in §2 (immediately after the statement of the theorem). This completes the proof of the Theorem 2.2 modulo Lemma 3.1.

Towards the proof of Lemma 3.1, we need the following result, showing how to lower bound E[Ip(p + U)] given t(U).

- Lemma 3.2. For any U ∈ W with 0 ≤ U ≤ 1 − p we have


E[Ip(p + U)] ≥ (1 − o(1)) Ip(1)t(U)2/3 . where o(1) is some quantity that goes to zero as p → 0. Proof. For p = o(1) and any 0 ≤ x ≤ 1−p one has Ip(p+x) ≥ (1+o(1))x2Ip(1) (as established in Corollary 3.5 below); thus,

E[Ip(p + U)] =

Ip(p + U(x,y))dxdy

[0,1]2

U(x,y)2 dxdy ≥ (1 − o(1)) Ip(1)t(U)2/3 , where we will justify the last inequality using the fact that

≥ (1 − o(1)) Ip(1)

[0,1]2

t(U) ≤

U(x,y)2 dxdy

[0,1]2

3/2

for any U ∈ W . (3.2)

Indeed, (3.2) follows from the Cauchy–Schwarz inequality: t(U) =

U(x,y)U(x,z)U(y,z)dxdydz

[0,1]3

1/2

U(x,z)2 dx

U(x,y)2 dx

≤

[0,1]2 [0,1]

[0,1]

1/2

U(y,z)dydz

which, by two more applications of the Cauchy–Schwarz inequality, is at most

≤

U(x,y)2 dxdy

[0,1] [0,1]2

U(x,y)2 dxdy

[0,1]2

1/2

1/2

U(x,z)2 dx

[0,1]

1/2

U(x,z)2 dxdz

[0,1]2

1/2

U(y,z)2 dy

[0,1]

1/2

dz

U(y,z)2 dydz

[0,1]2

1/2

,

as required.

- Lemma 3.2 already shows that φ′(p,δ1,δ2) ≥ (δ12/3/2 − o(1))p2Ip(1). However, this is not


enough. To obtain the additional δ2p2Ip(1) term in the lower bound of φ′, we isolate the high degree vertices and consider their contributions.

- Proof of Lemma 3.1. First we prove an upper bound on φ′(p,δ1,δ2). Let A be the union of the rectangles


[0,δ11/3p]2 , [0,δ2p2] × [0,1], and [0,1] × [0,δ2p2]. Set U to be 1 − p on A and 0 elsewhere. Then we have t(U) ≥ δ2p3, and s(U) ≥ δ2p2, whereas

- 1

![image 61](<2014-lubetzky-variational-problem-upper-tails_images/imageFile61.png>)

- 2E[Ip(p + U)] = 12λ(A)Ip(1) = (21δ12/3 + δ2 + o(1))p2Ip(1), where here and in what follows λ denotes Lebesgue measure. This proves the upper bound on φ′(p,δ1,δ2).


![image 62](<2014-lubetzky-variational-problem-upper-tails_images/imageFile62.png>)

![image 63](<2014-lubetzky-variational-problem-upper-tails_images/imageFile63.png>)

Assume that E[Ip(p + U)] = O(p2 log(1/p)) (with an implicit constant that may depend on D), or else we are done.

Let f(x) = [0,1] U(x,y)dy. Let b = p1/3 (any choice of b with plog(1/p) ≪ b ≪ 1 suﬃces), and B = {x | f(x) > b} ⊆ [0,1]. By the convexity of Ip we have

![image 64](<2014-lubetzky-variational-problem-upper-tails_images/imageFile64.png>)

E[Ip(p + U)] =

Ip(p + U(x,y))dxdy ≥

[0,1]2

Ip(p + f(x))dx ≥ λ(B)Ip(p + b).

[0,1]

Since Ip(p + b) = (1 + o(1))blog(b/p) (see Lemma 3.3 below),

E[Ip(p + U)] Ip(p + b)

λ(B) ≤

=

![image 65](<2014-lubetzky-variational-problem-upper-tails_images/imageFile65.png>)

O(p2 log(1/p)) (1 + o(1))blog(b/p)

= O

![image 66](<2014-lubetzky-variational-problem-upper-tails_images/imageFile66.png>)

p2 b

![image 67](<2014-lubetzky-variational-problem-upper-tails_images/imageFile67.png>)

. (3.3)

Next, we have Ip(p + x) ≥ (x/b)2Ip(p + b) for x ∈ [0,b] (see Lemma 3.4 below); hence,

Ip(p + b) b2 [0,1]\B

f(x)2 dx.

Ip(p + f(x))dx ≥

E[Ip(p + U)] ≥

![image 68](<2014-lubetzky-variational-problem-upper-tails_images/imageFile68.png>)

[0,1]\B

Therefore,

E[Ip(p + U)]b2 Ip(p + b)

= O(p2b), (3.4)

f(x)2 dx ≤

![image 69](<2014-lubetzky-variational-problem-upper-tails_images/imageFile69.png>)

[0,1]\B

where the last step is by (3.3). Since [0,1] f(x)2 dx = s(U) ≥ δ2p2, we have

f(x)2 dx ≥ (δ2 − O(b))p2 = (δ2 − o(1))p2 .

B

First applying the convexity of Ip, then the fact (shown in Corollary 3.5 below) that Ip(p + x) is at least (1 − o(1))x2Ip(1) for p = o(1), and ﬁnally (3.4), we obtain

Ip(p + U(x,y))dxdy ≥

B×[0,1]

Ip(p + f(x))dx

B

f(x)2Ip(1)dx ≥ (δ2 − o(1))p2Ip(1). Since U(x,y) = U(y,x), we have

≥ (1 − o(1))

B

- 1

![image 70](<2014-lubetzky-variational-problem-upper-tails_images/imageFile70.png>)

- 2 B×[0,1]∪[0,1]×B


- 1

![image 71](<2014-lubetzky-variational-problem-upper-tails_images/imageFile71.png>)

- 2


λ(B)2Ip(1) ≥ (δ2 −o(1))p2Ip(1),

Ip(p+U(x,y))dxdy ≥ (δ2 −o(1))p2Ip(1) −

(3.5) where the last step is due to λ(B) = O(p2/b) = o(p).

We have E[Ip(p + U)] ≥ Ip(p + EU) by convexity of Ip. As Ip(p + x) is increasing for x ∈ [0,1 −p], and Lemma 3.3 tells us that Ip(p +Cp3/2 log(1/p)) ∼ 12C2p2 log(1/p) for each ﬁxed C > 0 as p → 0, we see that E[Ip(p+U)] = O(p2 log(1/p)) implies that EU = O(p3/2 log(1/p)). Let U′ = U1Bc×Bc where Bc = [0,1] \ B. We have

![image 72](<2014-lubetzky-variational-problem-upper-tails_images/imageFile72.png>)

![image 73](<2014-lubetzky-variational-problem-upper-tails_images/imageFile73.png>)

![image 74](<2014-lubetzky-variational-problem-upper-tails_images/imageFile74.png>)

t(U) − t(U′) ≤ 3

U(x,y)U(x,z)U(y,z)dxdydz

B×[0,1]×[0,1]

U(y,z)dxdydz = 3λ(B)EU = O b−1p7/2 log(1/p) = o(p3).

![image 75](<2014-lubetzky-variational-problem-upper-tails_images/imageFile75.png>)

≤ 3

B×[0,1]×[0,1]

(3.6) Thus,

t(U′) ≥ (δ1 − o(1))p3. By Lemma 3.2,

- 1

![image 76](<2014-lubetzky-variational-problem-upper-tails_images/imageFile76.png>)

- 2 Bc×Bc


- 1

![image 77](<2014-lubetzky-variational-problem-upper-tails_images/imageFile77.png>)

- 2


E[Ip(p + U′)]

Ip(p + U(x,y))dxdy =

δ12/3

- 1

![image 78](<2014-lubetzky-variational-problem-upper-tails_images/imageFile78.png>)

- 2 − o(1) Ip(1)t(U′)2/3 ≥


2 − o(1) p2Ip(1). (3.7) Combining (3.5) and (3.7), we deduce that

≥

![image 79](<2014-lubetzky-variational-problem-upper-tails_images/imageFile79.png>)

- 1

![image 80](<2014-lubetzky-variational-problem-upper-tails_images/imageFile80.png>)

- 2 [0,1]2


Ip(p + U(x,y))dxdy ≥

This proves the lower bound on φ′(p,δ1,δ2).

δ12/3 2

+ δ2 − o(1) p2Ip(1).

![image 81](<2014-lubetzky-variational-problem-upper-tails_images/imageFile81.png>)

- 3.2. Discrete variational problem — proof of Theorem 1.1. First consider the case n−1/2 ≪ p ≪ 1. The upper bound on the left-hand side of (1.3) was already proved in §2. For the lower bound, by applying Lemma 2.1 and then Theorem 2.2 we have


φ(p,δ) p2 log(1/p) − lim

φ(n,p,δ) n2p2 log(1/p) ≥ lim

lim

![image 82](<2014-lubetzky-variational-problem-upper-tails_images/imageFile82.png>)

![image 83](<2014-lubetzky-variational-problem-upper-tails_images/imageFile83.png>)

n→∞

n→∞

p→0

Ip(0) 2np2 log(1/p)

= min

![image 84](<2014-lubetzky-variational-problem-upper-tails_images/imageFile84.png>)

δ2/3 2

,

![image 85](<2014-lubetzky-variational-problem-upper-tails_images/imageFile85.png>)

δ 3 − 0.

![image 86](<2014-lubetzky-variational-problem-upper-tails_images/imageFile86.png>)

The last zero is due to Ip(0)/(np2 log(1/p)) ∼ 1/(nplog(1/p)) → 0. This proves (1.3).

It remains to treat the regime n−1 ≪ p ≪ n−1/2. When δ ≥ 27/8, so that δ2/3/2 ≤ δ/3, the desired result again follows from Theorem 2.2 by the same argument as given above. However, when δ < 27/8, second upper bound construction (stated immediately following Theorem 1.1) is invalid. In order to prove a matching lower bound for (1.4), we need to eliminate the second construction as a possibility. We sketch the modiﬁcations to the proof here. It suﬃces to show that s(U) = o(p2) (using the notation of the previous subsection). Indeed, once we know that s(U) = o(p2), the decomposition (3.1) implies t(U) = (δ − o(1))p3, from which we obtain 1 2E[Ip(p + U)] ≥ (δ2/3/2 − o(1))p2Ip(1) by Lemma 3.2.

![image 87](<2014-lubetzky-variational-problem-upper-tails_images/imageFile87.png>)

From now on assume that n−1 ≪ p ≪ n−1/2. Assume b is chosen so that max{p2n, plog(1/p)} ≪ b ≪ 1.

![image 88](<2014-lubetzky-variational-problem-upper-tails_images/imageFile88.png>)

Then (3.3) gives λ(B) = O(p2/b) ≪ 1/n. Since we are in the discrete setting of Theorem 1.1, λ(B) ≪ 1/n implies that B must be an empty set. Therefore, from (3.4) we can infer that

- s(U) = [0,1] f(x)2 dx = O(p2b) = o(p2), as claimed. This completes the proof.


- 3.3. Properties of the function Ip as p → 0. Here we collect the various facts about Ip that were referred to throughout the proof of Theorem 2.2.


- Lemma 3.3. Let p → 0. If 0 ≤ x ≪ p, then Ip(p + x) ∼ x2/(2p). If p ≪ x ≤ 1 − p, then Ip(p + x) ∼ xlog(x/p).

Proof. We use Taylor expansion for Ip(x) around x = p, noting that Ip(p) = Ip′(p) = 0, Ip′′(p) = 1/(p(1−p)) and Ip′′′(x) = 1/(1−x)2−1/x2. We have Ip(p+x) = x2Ip′′(p)/2+x3Ip′′′(ξ)/6 for some ξ ∈ (p,p+x); thus, Ip(p+x) = x2/(2p(1−p))+O(x3/p2) ∼ x2/(2p) when 0 ≤ x ≪ p.

If p ≪ x < 1 − p (the required statement trivially holds for x = 1 − p), then

Ip(p + x) = (p + x)log

p + x p

![image 89](<2014-lubetzky-variational-problem-upper-tails_images/imageFile89.png>)

+ (1 − p − x)log

1 − p − x 1 − p

![image 90](<2014-lubetzky-variational-problem-upper-tails_images/imageFile90.png>)

= (1 + o(1))xlog

x p

![image 91](<2014-lubetzky-variational-problem-upper-tails_images/imageFile91.png>)

+ O(x), (3.8)

where the bound O(x) comes from |log y| ≤ y−1 −1 which is valid for all y ∈ (0,1]. This shows that Ip(p + x) ∼ xlog(x/p) when p ≪ x ≤ 1 − p.

- Lemma 3.4. There exists p0 > 0 so that for all 0 < p ≤ p0 and 0 ≤ x ≤ b ≤ 1−p−1/log(1/p), Ip(p + x) ≥ (x/b)2Ip(p + b). (3.9)


Proof. Let xp = 1 − p − 1/log(1/p). We will show that the function f(x) = Ip(p + √x) is concave for x ∈ [0,x2p]. The inequality (3.9) then follows because for each b ≤ xp, the chord joining (0,0) and (b2,Ip(p + b)) lies below f, so that f(x) ≥ (x/b2)Ip(p + b) for all 0 ≤ x ≤ b2. Replacing x by x2 yields (3.9).

![image 92](<2014-lubetzky-variational-problem-upper-tails_images/imageFile92.png>)

We have

√x)p (p + √x)(1 − p)

![image 93](<2014-lubetzky-variational-problem-upper-tails_images/imageFile93.png>)

1 4(1 − p −

(1 − p −

1 4x3/2

f′′(x) =

√x)(p + √x)x

log

+

. Let

![image 94](<2014-lubetzky-variational-problem-upper-tails_images/imageFile94.png>)

![image 95](<2014-lubetzky-variational-problem-upper-tails_images/imageFile95.png>)

![image 96](<2014-lubetzky-variational-problem-upper-tails_images/imageFile96.png>)

![image 97](<2014-lubetzky-variational-problem-upper-tails_images/imageFile97.png>)

![image 98](<2014-lubetzky-variational-problem-upper-tails_images/imageFile98.png>)

![image 99](<2014-lubetzky-variational-problem-upper-tails_images/imageFile99.png>)

(1 − p − x)p (p + x)(1 − p)

x (1 − p − x)(p + x)

g(x) = 4x3f′′(x2) =

+ log

.

![image 100](<2014-lubetzky-variational-problem-upper-tails_images/imageFile100.png>)

![image 101](<2014-lubetzky-variational-problem-upper-tails_images/imageFile101.png>)

It now suﬃces to show that g(x) ≤ 0 for x ∈ [0,xp], which implies that f is concave in [0,x2p]. We have g(0) = 0 and

p log(1/p)(1 − 1/log(1/p))(1 − p)

1 − p − 1/log(1/p) 1 − 1/log(1/p)

+ log

g(xp) = log(1/p)

![image 102](<2014-lubetzky-variational-problem-upper-tails_images/imageFile102.png>)

![image 103](<2014-lubetzky-variational-problem-upper-tails_images/imageFile103.png>)

≤ log(1/p) − log(1/p) − log log(1/p) + O (1/log(1/p)) = −log log(1/p) + o(1). So, we can choose p0 so that g(xp) ≤ 0 for all p ≤ p0. Furthermore, we have

(−1 + 2p + 2x)x (1 − p − x)2(p + x)2

g′(x) =

.

![image 104](<2014-lubetzky-variational-problem-upper-tails_images/imageFile104.png>)

It follows that g is decreasing when x < 1/2 − p and increasing when x > 1/2 − p. Since g(0),g(xp) ≤ 0, we conclude that g(x) ≤ 0 for all x ∈ [0,xp].

- Corollary 3.5. There is some p0 > 0 so that for all 0 < p ≤ p0 and all 0 ≤ x ≤ 1 − p one has Ip(p + x) ≥ x2Ip(1 − 1/log(1/p)) = (1 + o(1))x2Ip(1) (3.10)

where the o(1)-term goes to zero as p → 0. Proof. Let b = 1 − p − 1/log(1/p). When 0 ≤ x ≤ b, the ﬁrst inequality in (3.10) follows from

- Lemma 3.4 since b < 1, and when b < x ≤ 1−p, it follows from Ip(p+x) ≥ Ip(p+b) ≥ x2Ip(p+b) since Ip(p+x) is increasing for x ∈ [0,1−p]. The last step in (3.10) follows from Lemma 3.3.


4. Extension to cliques In this section we extend Theorem 1.1 and Corollary 1.2) to upper tails for clique counts.

Deﬁnition (Discrete variational problem for upper tails of H-counts). Let H be a graph on k vertices. Recall that Gn denotes the set of weighted undirected graphs on n vertices with edge weights in [0,1]. The corresponding variational problem for δ > 0 and 0 < p < 1 is given by

φH(n,p,δ) := inf Ip(G) : G ∈ Gn with t(H,G) ≥ (1 + δ)p|E(H)| , (4.1) where

t(H,G) := n−k

1≤x1,...,xk≤n ij∈E(H)

gxixj

is the probability that a random map V (H) → V (G) is a graph homomorphism. Theorem 4.1. Let Kk be the k-clique for a ﬁxed k ≥ 3, and let δ > 0. Then

lim

n→∞

φKk(n,p,δ) n2pk−1 log(1/p)

![image 105](<2014-lubetzky-variational-problem-upper-tails_images/imageFile105.png>)

=

min 12δ2/k , δ/k if n−1/(k−1) ≪ p ≪ 1,

![image 106](<2014-lubetzky-variational-problem-upper-tails_images/imageFile106.png>)

- 1

![image 107](<2014-lubetzky-variational-problem-upper-tails_images/imageFile107.png>)

- 2δ2/k if n−2/(k−1) ≪ p ≪ n−1/(k−1) .


Given Theorem 4.1, the analogue of Corollary 1.2 again follows from the new framework of Chatterjee and Dembo, which establishes (see [5, Theorem 1.2]) that for any ﬁxed k ≥ 3, the rate function of upper tails for Kk counts in G(n,p) is (1 + o(1))φKk(n,p,δ) provided that p ≥ n−α for some α = α(k) > 0 (in particular, any ﬁxed 0 < α < (4k3 −8k2 +k+3)−1 suﬃces).

- Corollary 4.2. For any ﬁxed k ≥ 3 there exists some α = α(k) > 0 so the following holds. For any ﬁxed δ > 0, if n−α ≤ p ≪ 1 then


P t(Kk,Gn,p) ≥ (1 + δ)p(k2) = exp −(1 − o(1))min 2 1δ2/k , δ/k n2pk−1 log(1/p) .

![image 108](<2014-lubetzky-variational-problem-upper-tails_images/imageFile108.png>)

- 4.1. Proof of Theorem 4.1. Let K1,ℓ−1 be the star on ℓ vertices, and let e(H) and ∆(H) denote the number of edges and maximum degree in H, resp. The proof will follow from the same arguments used to prove Theorem 1.1, once we establish the next lemma.


- Lemma 4.3. Fix k ≥ 4 and let H be a non-edgeless k-vertex graph other than Kk and K1,k−1. If U ∈ W is a graphon with 0 ≤ U ≤ 1−p and Ip(p+U) pk−1 log(1/p), then t(H,U) ≪ pe(H).


Towards the proof of this lemma, we need the following simple claim.

Claim 4.4. Let H = (V,E) be a nonempty graph on k ≥ 4 vertices other than Kk and K1,k−1. Then H has a spanning subgraph H′ = (V,E′) with ∆(H′) ≤ 2 and e(H′) > 2e(H)/(k − 1).

Proof. First, we may assume that ∆(H) > 2, since if ∆(H) ≤ 2 then H′ = H suﬃces (as e(H) > 2e(H)/(k − 1) for k ≥ 4). Second, if H is acyclic then 2e(H)/(k − 1) ≤ 2, so one can form H′ via 2 edges incident to a vertex (recall ∆ > 2), along with another edge if needed (either disjoint or extending that path, recalling H = K1,k−1). Thus, if we suppose H is a counterexample to the claim with a minimum number of edges, then H must contains a cycle.

Let C = (v0,... ,vℓ−1) be a longest cycle of H (so that vivi+1 ∈ E, indices taken modulo ℓ). Then ℓ < k, otherwise we could take E(H′) = E(C), since k > 2e(H)/(k − 1) for H = Kk.

Denote by ∂C the set of edges in H with at least one endpoint in Cℓ. We claim that |∂C| < ℓ(k − 1)/2. Indeed, for any i, the vertices vi and vi+1 cannot have any common neighbors outside C (as otherwise a longer cycle can be formed). Hence, every u ∈/ C can be

connected to at most ⌊ℓ/2⌋ vertices in C, and unless all 2 ℓ potential edges between the vertices of C are present, |∂C| < (k − ℓ)⌊ℓ/2⌋ + 2 ℓ ≤ ℓ(k − 1)/2. On the other hand, if these 2 ℓ edges all belong to H, then every u ∈/ C can be connected to at most one vertex in C (otherwise a longer cycle exists), whence |∂C| ≤ k−ℓ+ 2 l < ℓ(k−1)/2 (the last inequality used 2 < ℓ < k).

It follows that e(H) > |∂C|, or else 2e(H)/(k−1) < ℓ and again we can take E(H′) = E(C). Finally, let H1 = (V,E(H)\∂C). As established above, e(H1) > e(H)−ℓ(k −1)/2, so it would suﬃce to ﬁnd a subgraph H1′ of it with ∆(H1′) ≤ 2 and e(H1′) ≥ 2e(H1)/(k − 1), to which we can add the cycle C as a separate connected component. Indeed such a subgraph H1′ exists, since 0 < e(H1) < e(H) and H was assumed to be a counterexample minimizing e(H).

- Proof of Lemma 4.3. By Corollary 3.5 (as used in the ﬁrst step in the proof of Lemma 3.2),


E[U2] ≤ (1+o(1))E[Ip(p+U)]/Ip(1) pk−1. Next, as a consequence of the generalized H¨older’s inequality [9] (see [19, Corollary 3.2]),

t(F,U) ≤ E Ud e(F)/d for any graph F with ∆(F) ≤ d . (4.2)

So, by combining these inequalities, t(H′,U) p(k−1)e(H′)/2 holds for any H′ with ∆(H′) ≤ 2. Taking H′ as provided by Claim 4.4, we ﬁnd that t(H,U) ≤ t(H′,U) ≪ pe(H), as desired.

The upper bound of Theorem 4.1 on φKk is obtained via the same constructions of §2, with modiﬁed part sizes: a copy of Kr for r = δ1/knp(k−1)/2 or a copy of Kr,n−r for r = (δ/k)npk−1. For the lower bound, one decomposes t(Kk,W) as in (3.1), in which, by Lemma 4.3, all terms other than t(Kk,U) and t(K1,k−1,U) are negligible. The remaining terms, resp. analogous to t(U) and s(U) in §3, are treated as in §3 (e.g., λ(B) pk−1/b replaces λ(B) p2/b in Lemma 3.1) with one exception: instead of (3.6), write t(Kk,U)−t(Kk,U′) ≤ kλ(B)t(Kk−1,U); we wish this quantity to be o p(k2) , and indeed, since t(Kk−1,U) ≤ t(H′,U) p(k−1)e(H)/2 for

any H′ ⊂ Kk−1 with ∆(H′) ≤ 2 (as in the proof of Lemma 4.3), letting H′ = Ck−1 (recall that k ≥ 4) yields t(Kk−1,U) p(k−1)2/2, and using λ(B) pk−1/b with b ≫ p(k−1)/2 completes the proof.

- 4.2. General subgraph counts. It is worthwhile noting that the analysis of cliques from the previous section readily implies that, for any ﬁxed graph F with maximum degree ∆,


φF(n,p,δ) ≍ n2p∆ log(1/p) whenever p ≫ n−1/∆ . (4.3) Consequently (again via [5]), there is some α = α(F) > 0 such that the rate function R(n,p,δ) for observing a number of F-copies that is (1+δ) times its mean in Gn,p for p ≥ n−α is of order n2p∆ log(1/p) (the best previous bounds here, cf. [12], were n2p∆ R(n,p,δ) n2p∆ log(1/p)).

- Corollary 4.5. Let F be a ﬁxed graph with maximum degree ∆. There exist α = α(F) > 0 such that, for any ﬁxed δ > 0 and any p ≥ n−α,


−log P t(F,Gn,p) ≥ (1 + δ)pe(F) ≍ n2p∆ log(1/p).

Indeed, assume ∆ ≥ 2 (the case ∆ = 1 is trivial). For the upper bound on φF in (4.3), take a copy of Kr,n−r for r = δnp∆ (as in §2). For the lower bound, let W be such that

- t(F,W) ≥ (1 + δ)pe(F) and write U = W − p (so 0 ≤ U ≤ 1 − p). As in (3.1), we decompose


t(F,W) − pe(F) into H⊆F θF,H pe(F)−e(H) t(H,U) for some positive constants {θF,H}, and by the assumption on t(F,W) there must exist some H ⊆ F with t(H,U) pe(H). However, by (4.2), t(H,U) ≤ E[U∆]e(H)/∆, which is at most E[U2]e(H)/∆ as ∆ ≥ 2. Combining these, E[U2] p∆, and yet (by Corollary 3.5, as before) E[U2] E[Ip(p + U)]/Ip(1), as claimed.

5. Weak regularity

In this section, we give a short proof establishing (1.2) and Corollary 1.2 for slowly decreasing p, namely (log n)−1/6 ≪ p ≪ 1, without requiring the new results of Chatterjee and Dembo. The lower bound on the tail probability is explained in the paragraph immediately following Corollary 1.2. The upper bound is established through the following proposition.

Proposition 5.1. Let 0 < η < δ and 0 < p < 1. Then

P(t(Gn,p) ≥ (1 + δ)p3) ≤ R exp (−φ(n,p,δ − η)) , (5.1) with R = Mnε−M2 where ε = ηp3/6 < 1 and M = 41/ε2.

Assume δ > 0 is ﬁxed and (log n)−1/6 ≪ p ≪ 1. Take a slowly decreasing η = ηn so that p−3(log n)−1/2 ≪ η ≪ 1. Then ε = ηp3/6 ≫ (log n)−1/2, and so, M = 4o(logn) = no(1). Thus,

log R = nlog M + M2 log(1/ε) ≪ nlog n + no(1) log log n

≪ n2p2 log(1/p) ≍ φ(n,p,δ) ∼ φ(n,p,δ − o(1)). It then follows by Proposition 5.1 that

P(t(Gn,p) ≥ (1 + δ)p3) ≤ exp (−(1 − o(1))φ(n,p,δ)) ,

which implies the upper bound in (1.2). More generally, one needs p ≫ (log n)−1/(2e(H)) in order to use this method for upper tails of H-counts, where e(H) is the number of edges in H.

We proceed to prove Proposition 5.1. Deﬁne the relative edge-density between two nonempty subsets of vertices A,B ⊆ V (G) as dG(A,B) := |{(a,b) ∈ A × B : ab ∈ E(G)}|/(|A||B|).

- Lemma 5.2. Let A1,... ,Am be a partition of V = {1,... ,n} into nonempty sets. Let δ > 0, let 0 < p < 1 and take 0 ≤ dij ≤ 1 and dij = dji for each 1 ≤ i,j ≤ m. Suppose that


1

n3 i,j,k |Ai||Aj| |Ak|dijdikdjk ≥ (1 + δ)p3 . Then for a random graph G ∼ Gn,p on the vertex set V we have

![image 109](<2014-lubetzky-variational-problem-upper-tails_images/imageFile109.png>)

P(dG(Ai,Aj) ≥ dij for all 1 ≤ i ≤ j ≤ m) ≤ exp (−φ(n,p,δ)) .

Proof. Deﬁne Ip>(x) := Ip(max{x,p}). We know that a binomial random variable X ∼ Bin(N,p) satisﬁes P(X ≥ δN) ≤ exp(−NIp>(δ)). We have

P(dG(Ai,Aj) ≥ dij) ≤ exp −|Ai||Aj|Ip>(dij) if i = j , P(dG(Ai,Ai) ≥ dii) ≤ exp − |A2i| Ip>(dii) .

Let

m

|Ai|

2 Ip>(dii). Since A1,... ,Am are disjoint, we have

Ip>(A,d) :=

|Ai||Aj|Ip>(dij) +

i=1

1≤i<j≤m

P(dG(Ai,Aj) ≥ dij for all 1 ≤ i ≤ j ≤ m) ≤ exp −Ip>(A,d) ≤ exp (−φ(n,p,δ)) , where the last step follows from the following observation: if G′ ∈ Gn is the weighted graph on vertex set V obtained by setting gxy = max{dij,p} whenever x ∈ Ai and y ∈ Aj, then t(G′) ≥ (1 + δ)p3n3, so that Ip>(A,d) = Ip(G′) ≥ φ(n,p,δ) by our deﬁnition (1.1) of φ.

The following lemma is a consequence of the Frieze–Kannan weak regularity lemma and an associated counting lemma (see [16, §9.1, §10.5]).

- Lemma 5.3. Let ε > 0 and let G be a graph with n vertices. Then there exists a partition P of the vertices of G into at most 41/ε2 parts A1,... ,Am so that if dij = dG(Ai,Aj), then


m

t(G) − n−3

|Ai| |Aj||Ak|dijdikdjk ≤ 3ε.

i,j,k=1

Proof of Proposition 5.1. Let G be any graph on n vertices satisfying t(G) ≥ (1+δ)p3. By Lemma 5.3, there exists a partition of its vertices into m ≤ M parts A1,A2,... ,Am, so that

m

n−3

|Ai| |Aj||Ak| dijdikdjk ≥ (1 + δ)p3 − 3ε,

i,j,k=1

where dij = dG(Ai,Aj). Let d′ij be dij rounded down to the nearest multiple of ε. Then n−3

m

|Ai||Aj| |Ak|d′ijd′ikd′jk ≥ (1 + δ)p3 − 6ε = (1 + δ − η)p3 .

i,j,k=1

For any ﬁxed choice of {Ai}i, {d′ij}i,j, by Lemma 5.2 we have P(dG(Ai,Aj) ≥ d′ij for all 1 ≤ i ≤ j ≤ m) ≤ exp (−φ(n,p,δ − η)) . A union bound over the Ai’s (≤ Mn choices) and d′ij’s (≤ ε−M2 choices) now yields (5.1).

References

- [1] B. B. Bhattacharya, S. Ganguly, E. Lubetzky, and Y. Zhao. Upper tails and independence polynomials in random graphs. Preprint, available at arXiv:1507.04074.
- [2] B. Bollob´s. Random graphs, volume 73 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, second edition, 2001.
- [3] C. Borgs, J. T. Chayes, L. Lova´sz, V. T. S´os, and K. Vesztergombi. Convergent sequences of dense graphs.

I. Subgraph frequencies, metric properties and testing. Adv. Math., 219(6):1801–1851, 2008.

- [4] S. Chatterjee. The missing log in large deviations for triangle counts. Random Structures Algorithms, 40(4):437–451, 2012.
- [5] S. Chatterjee and A. Dembo. Nonlinear large deviations. Preprint, available at arXiv:1401.3495.
- [6] S. Chatterjee and S. R. S. Varadhan. The large deviation principle for the Erd˝s-Re´nyi random graph. European J. Combin., 32(7):1000–1017, 2011.
- [7] B. Demarco and J. Kahn. Tight upper tail bounds for cliques. Random Structures Algorithms, 41(4):469–487, 2012.
- [8] B. DeMarco and J. Kahn. Upper tails for triangles. Random Structures Algorithms, 40(4):452–459, 2012.
- [9] H. Finner. A generalization of H¨older’s inequality and some probability inequalities. Ann. Probab., 20(4):1893–1901, 1992.
- [10] A. Frieze and R. Kannan. Quick approximation to matrices and applications. Combinatorica, 19(2):175–220, 1999.
- [11] S. Janson, T.  Luczak, and A. Rucinski. Random graphs. Wiley-Interscience Series in Discrete Mathematics and Optimization. Wiley-Interscience, New York, 2000.
- [12] S. Janson, K. Oleszkiewicz, and A. Rucin´ski. Upper tails for subgraph counts in random graphs. Israel J. Math., 142:61–92, 2004.
- [13] S. Janson and A. Rucin´ski. The infamous upper tail. Random Structures Algorithms, 20(3):317–342, 2002. Probabilistic methods in combinatorial optimization.
- [14] S. Janson and A. Rucin´ski. The deletion method for upper tail estimates. Combinatorica, 24(4):615–640, 2004.
- [15] J. H. Kim and V. H. Vu. Divide and conquer martingales and the number of triangles in a random graph. Random Structures Algorithms, 24(2):166–174, 2004.
- [16] L. Lova´sz. Large networks and graph limits, volume 60 of American Mathematical Society Colloquium Publications. American Mathematical Society, Providence, RI, 2012.
- [17] L. Lova´sz and B. Szegedy. Limits of dense graph sequences. J. Combin. Theory Ser. B, 96(6):933–957, 2006.
- [18] L. Lova´sz and B. Szegedy. Szemere´di’s lemma for the analyst. Geom. Funct. Anal., 17(1):252–270, 2007.
- [19] E. Lubetzky and Y. Zhao. On replica symmetry of large deviations in random graphs. Random Structures Algorithms, 47:109—146, 2015.
- [20] E. Szemere´di. Regular partitions of graphs. In Probl`emes combinatoires et th´eorie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), volume 260 of Colloq. Internat. CNRS, pages 399–401. CNRS, Paris, 1978.
- [21] V. H. Vu. A large deviation result on the number of small subgraphs of a random graph. Combin. Probab. Comput., 10(1):79–94, 2001.


E. Lubetzky

Courant Institute of Mathematical Sciences, New York University, New York, NY 10012, USA E-mail address: eyal@courant.nyu.edu Y. Zhao

Mathematical Institute, University of Oxford, Oxford OX2 6GG, United Kingdom E-mail address: yufei.zhao@maths.ox.ac.uk

