## ON THE LOWER TAIL VARIATIONAL PROBLEM FOR RANDOM GRAPHS

YUFEI ZHAO

# arXiv:1502.00867v1[math.CO]3Feb2015

Abstract. We study the lower tail large deviation problem for subgraph counts in a random graph. Let XH denote the number of copies of H in an Erdo˝s-Re´nyi random graph G(n, p). We are interested in estimating the lower tail probability P(XH ≤ (1 − δ)EXH) for ﬁxed 0 < δ < 1.

Thanks to the results of Chatterjee, Dembo, and Varadhan, this large deviation problem has been reduced to a natural variational problem over graphons, at least for p ≥ n−αH (and conjecturally for a larger range of p). We study this variational problem and provide a partial characterization of the so-called “replica symmetric” phase. Informally, our main result says that for every H, and 0 < δ < δH for some δH > 0, as p → 0 slowly, the main contribution to the lower tail probability comes from Erd˝os-R´enyi random graphs with a uniformly tilted edge density. On the other hand, this is false for non-bipartite H and δ close to 1.

1. Background

We consider large deviations of subgraph counts in Erd˝s-R´enyi random graphs. Fix a graph H, and let XH denote the number of copies of H in an Erd˝s–Re´nyi random graph G(n,p). For a ﬁxed δ > 0, the problem is to estimate the probabilities

(upper tail) P(XH ≥ (1 + δ)EXH) and (lower tail) P(XH ≤ (1 − δ)EXH).

This problem has a long history (see [6] and its references). For the order of the logarithm of the tail probability, the upper tail problem is considered more diﬃcult and it was resolved only fairly recently [6,12]. We are now interested in the ﬁner question of determining the large deviation rate, or equivalently the ﬁrst order asymptotics of the logarithm of the tail probability.

Chatterjee and Varadhan [10] (the dense setting, with p constant) and more recently Chatterjee and Dembo [7] (the sparse setting, with p → 0 and p ≥ n−αH for some αH > 0) showed that this large deviation problem reduces to a natural variational problems in the space of graphons, which are a certain type of graph limits. We begin by reviewing this connection, and then we shift our attention to analyzing the variational problem.

The language of graph limits is used throughout our discussion, so let us review some terminologies. We refer the readers to the beautifully written monograph by Lov´sz [24] or the original sources, e.g., [4,5,25,26], for more on the subject. A graphon is a symmetric measurable function W : [0,1]2 → [0,1] (here symmetric means W(x,y) = W(y,x)). We write V (H) and E(H) to mean the vertex and edge set of a graph H, respectively, and v(H) = |V (H)| and e(H) = |E(H)| to denote their cardinalities. For any graphs H and G, we write hom(H,G) to denote the number of graph homomorphisms from H to G. We denote by t(H,G) := hom(H,G)/v(G)v(H) the H-density in G. The H-density of a graphon W is deﬁned by (here W could be R-valued):

t(H,W) :=

W(xi,xj)

dxi.

[0,1]V (H) ij∈E(H)

i∈V (H)

The author is supported by a Microsoft Research PhD Fellowship.

1

As usual, Kt denotes the complete graph on t vertices. As an example, we have t(K3,W) =

W(x,y)W(x,z)W(y,z)dxdydz.

[0,1]3

The notion of cut distance is mentioned a few times in this paper, but it is not used in a substantial way, so we refer the readers to [24, Chapter 8] for details.

We write

1 − x 1 − p

x p

+ (1 − x)log

Ip(x) := xlog

for the relative entropy function. For any function f, we write E[f(W)] := [0,1]2 f(W(x,y))dxdy.

We begin with a review of what is known for upper tails. In the dense case, for ﬁxed 0 < p ≤ q < 1, it was shown in [10] that as n → ∞,

n2 2

log P(t(H,G(n,p)) ≥ qe(H)) = −(1 + o(1))

UTp(H,q), (1.1) where UTp(H,q), for any graph H, is given by the upper tail variational problem:

minimize E[Ip(W)] subject to t(H,W) ≥ qe(H).

UTp(H,q) :=

(1.2)

Here W is taken over all graphons. We shall use UTp(H,q) to refer to the variational problem as well as its value, i.e., min{E[Ip(W)] : t(H,W) ≥ qe(H)} (it is known that the minimum is always attained by some W; see Lemma 5.1 below).

Furthermore, as shown in [10, Theorem 3.1], the set of minimizing W in UTp(H,q) represents the most likely models for G(n,p) conditioned on the rare event of t(H,G(n,p)) ≥ qe(H), in the sense that the random graph conditioned on this rare event will be exponentially more likely to be close to the minimizing set of W’s in terms of cut distance. This motiviates the study of UTp(H,q) and related variational problems.

We currently have few tools for solving variational problems of the type (1.2). Note that W ≡ q alway satisﬁes the constraint in (1.2). We focus on the basic question: does the constant graphon W ≡ q minimize UTp(H,q)? The answer depends on the graph H and parameters (p,q). For a ﬁxed H, we wish to determine for each (p,q) whether UTp(H,q) = Ip(q) or UTp(H,q) < Ip(q), and in the former case, whether the constant function W ≡ q is the unique minimizer1. The separation of these two cases can be illustrated via a phase diagram, as in Figure 1, by plotting the phases in the (p,q)-plane according to the behavior of UTp(H,q).

The constant graphon W ≡ q is the limit of random graphs G(n,q) as n → ∞, so if it were the unique minimizer of UTp(H,q) then G(n,p), conditioned on having H-density at least qe(H), approaches the typical G(n,q) in cut distance; this is not the case when W ≡ q is not a minimizer. Borrowing language from statistical physics, informally, when W ≡ q is a minimizer we say that there is replica symmetry2, and otherwise there is symmetry breaking.

In a previous paper with Lubetzky [28], we completely identiﬁed the upper tail replica symmetric phase whenever H is a d-regular graph. The phase diagram depends only on d. The diagram for

- 1We identify graphons diﬀering on a measure zero set, as well as up to a measure-preserving transformation on [0, 1], i.e., W is identiﬁed with Wσ(x, y) := W(σ(x), σ(y)) where σ: [0, 1] → [0, 1] is measure-preserving.
- 2There is a subtle issue of uniqueness of the minimizer. When the constant graphon W ≡ q is the unique minimizer, G(n, q) represents the most likely model for the conditioned random graph (in terms of cut metric). However, it may be the case that W ≡ q is a non-unique minimizer (which provably does not happen for UTp(K3, q) but I suspect that it does happen for the corresponding lower tail problem LTp(K3, q)). When there are multiple distinct minimizers to the variational problem, all minimizers give rise to the same exponential rate, but one minimizer might still dominate by a lower order exp(o(n2)) factor, which I do not know how to discern purely from the variational problem.


- 0.8
- 1


=

q(p)

0.6

<

=

0.4

?

q(p)

0.2

<

0

0 0.2 0.4 0.6 0.8 1

Figure 1. The phase diagram for triangle density upper tail variational problem UTp(K3,q) (when q > p) and lower tail variational problem LTp(K3,q) (when q < p). In regions marked “=”, the constant graphon W ≡ q is the unique minimizer to the variational problem. In regions marked “<”, the constant graphon does not minimize the variational problem. The region marked “?” is unresolved. The boundary curves q and q are from Theorem 2.1.

H = K3 is shown in Figure 1 in the upper portion (i.e., q > p) of the diagram3. The lower portion of the diagram illustrates new results in paper concerning the lower tail problem.

In this paper we study the corresponding lower tail variational problem. For 0 ≤ q ≤ p ≤ 1, let

minimize E[Ip(W)] subject to t(H,W) ≤ qe(H).

LTp(H,q) :=

(1.3)

The connections between the large deviation problem and the variational problem discussed earlier hold for the lower tail just as they do for the upper tail. For example, as in (1.1), for ﬁxed 0 ≤ q ≤ p ≤ 1, we have

n2 2

log P(t(H,G(n,p)) ≤ qe(H)) = −(1 + o(1))

LTp(H,q). (1.4)

As observed in [28], if H is a bipartite graph satisfying Sidorenko’s conjecture [36], which asserts that t(H,W) ≥ E[W]e(H) for all graphons W, then from the constraint of LTp(H,q) we deduce E[W] ≤ q. Since Ip(·) is a convex function, from E[W] ≤ q it follows that W ≡ q is the unique minimizer of LTp(H,q). Sidorenko’s conjecture remains open4, though it has been proved for certain families of bipartite graphs H such as trees, cycles, hypercubes, and bipartite graphs containing one

- 3The boundary curve for the upper tail phase diagram for K3 is given by the equation (1+(q−1 −1)1/(1−2q))p = 1.
- 4The ﬁrst unsettled case of Sidorenko’s conjecture is for the graph H being K5,5 with a Hamiltonian cycle removed


(this H is sometimes called a “Mo¨bius strip”). There is some sentiment in the community that Sidorenko’s conjecture may be false for this graph.

vertex adjacent to all vertices on the opposite side [11,14,21,23,37]. Even if Sidorenko’s conjecture were false, it could still be true that W ≡ q minimizes LTp(H,q) for every bipartite H.

For the ﬁrst non-bipartite case, namely K3, new results in this paper partially characterize the lower tail phase diagram, as depicted in Figure 1. The region marked “?” remains unresolved. For other non-bipartite graph H, it is possible to draw similar partially identiﬁed phase diagrams using techniques in this paper. We will pay special attention to the slopes of the boundary curves at the origin.

The lower tail variational problem seems to be harder than the corresponding upper tail problem5. By analogy, for the classical extremal graph theory problem of determining the range of possible triangle densities in a graph of ﬁxed edge density, the maximization problem (analogous to upper tail) follows as a corollary of the classic Kruskal–Katona theorem [18,22]6, whereas the corresponding minimization problem (analogous to lower tail) was solved only relatively recently by Razborov [34] using his ﬂag algebra machinery (also later solved for K4 by Nikiforov [29] and all Kt by Reiher [35]). Furthermore, the qualitative nature of the phase transition seems to be diﬀerent for the upper tail and the lower tail. It seems likely that the optimizing graphon W changes continuously as (p,q) crosses upper tail phase boundary, while discontinuously for the lower tail.

The sparse setting, with p = pn → 0 and q/p kept constant, is more diﬃcult. Using powerful new methods, Chatterjee and Dembo [7] showed that the large deviation problem in sparse random graphs also reduces to the natural variational problem7, provided that p ≥ n−αH for some explicit αH > 0. A similar conclusion can be made about the lower tail variational problem using their techniques. With Lubetzky [27] we obtained the following asymptotic solution to the corresponding variational problem: for every ﬁxed δ > 0,

UTp(K3,(1 + δ)1/3p) p2 log(1/p)

- 2

- 3


= min δ2/3,

δ , (1.5)

lim

p→0

and as a corollary, as long as p = pn → 0 with pn ≥ n−1/42 log n, we have

δ2/3 2

δ 3

1 p

P(t(K3,G(n,p)) ≥ (1 + δ)p3) = exp −(1 − o(1))min

n2p2 log

,

.

In this paper, we also study the lower tail variational problem as p → 0. A nice feature of the lower tail problem in the sparse limit is that instead of being concerned with the entire phase boundary curve, we can focus on its slope at the origin.8

The lower tail problem was also recently analyzed by Janson and Warnke [17] from a completely diﬀerent perspective (not relating to the variational problem). In the triangle case, for n−1/2

p → 0, they were able to determine the large deviation rate of P(t(K3,G(n,p)) ≤ (1 − δ)p3) for the two extremes δ = o(1) and δ = 1 − o(1). They left as an open question what happens for ﬁxed δ ∈ (0,1), which is the subject of this paper.

There are other variants of the variational problem being studied in literature. For exponential random graphs, see [1,3,9,20,28,33,39–44]. For the variational problem where several subgraph densities are simultaneously constrained (e.g., edge and triangle densities both ﬁxed), see [2,19,30– 32].

- 5despite that the probabilistic problem of determining the order of log P(t(K3, G(n, p))) when p = p(n) → 0 came much later [6,12] compared to the corresponding lower tail result [15,16].
- 6The proof of the triangle upper tail result in [28] actually uses some form of strengthening of the Kruskal-Katona result, as we explain in Section 3.
- 7Some minor modiﬁcations needs to made to the formulation variational problem LTp(H, q) in order to match the statements in [7], namely that we only consider grpahons that correspond to weighted graphs on n vertices. This diﬀerence is minor and does not aﬀect the rest of this paper.
- 8For the upper tail boundary curve, the slope at the origin is always 1.


Section 2 contains statements of the results. Section 3 reviews the techniques used in proof of the upper tail results from [28]. Section 4 concerns the upper tail problem for triangle densities. Section 5 concerns general H-densities. The methods in Sections 4 and 5 are diﬀerent since the techniques for triangles seem to be quantitatively superior but do not extend to all graphs. Section 6 concludes with some open problems.

2. Results

- 2.1. Triangle density. Here is our main result concerning the lower tail variational problem LTp(K3,q) for triangle densities. See Figure 1.

- Theorem 2.1. There exist functions q,q: (0,1) → (0,1) satisfying 0 < q(p) ≤ q(p) ≤ p for 0 < p < 1 with the following properties. Whenever q(p) < q < p, the constant graphon W ≡ q is the unique minimizer for LTp(K3,q). Whenever 0 < q < q(p), the constant graphon W ≡ q does not minimize LTp(K3,q). Furthermore, limp→0 q(p)/p = 0.209... while limp→0 q(p)/p = 0.466....

The two curves q(p) and q(p) are drawn in Figure 1. The nature of LTp(K3,q) remains unresolved for (p,q) between these two curves.

In Theorem 2.1 and elsewhere, 0.466... denotes the unique 0 < r < 1 satisfying 32r log r−r+1 = 0, and 0.209... is deﬁned as the maximum value of r < 1 such that that the function fr(x) in (4.8) (also see Figure 4) has a zero in the open interval (0,r).

2.2. General subgraph density. We extend Theorem 2.1 to general subgraph counts. No serious eﬀort is made here at optimizing the quantitative bounds.

- Theorem 2.2. Let H be a graph. There exists a function q: (0,1) → (0,1) with limp→0 q(p)/p < 1 such that whenever q(p) < q ≤ p, the constant graphon W ≡ q is the unique minimizer for LTp(H,q).




Furthermore, if H is not bipartite, then there exists a function q: (0,1) → (0,1) with limp→0 q(p)/p > 0 such that whenever 0 ≤ q < q(p), the constant graphon W ≡ q does not minimize LTp(K3,q).

The proof of the triangle case, Theorem 2.1, makes use of Goodman’s inequality [13]: t(K3,W) + t(K3,1 − W) ≥ 1/4.

If H satisﬁes t(H,W) + t(H,1 − W) ≥ 2−e(H)+1 for all graphons W (such a graph H is sometimes called “common” in the context of Ramsey multiplicities), then the same method can be used to establish regions where W ≡ q is a minimizer of LTp(H,q) (though the actual regions will not be the same as in Figure 1 due to other technical reasons). However, t(H,W) + t(H,1 − W) ≥ 2−e(H)+1 does not hold in general. For example, Thomason [38] showed that Kt is a counterexample for all t ≥ 4. Consequently, the proof method of Theorem 2.1 does not seem to extend to all H.

- Theorem 2.2 for general H is proved using a diﬀerent method, which seems quantitatively inferior to the method for triangles.


For bipartite H, I conjecture that there is no phase transition:

- Conjecture 2.3. Let H be a bipartite graph. Then the constant function W ≡ q is always the unique minimizer of LTp(H,q).


As mentioned in the introduction, the conjecture holds for any H for which Sidorenko’s conjecture is true, i.e., t(H,W) ≥ E[W]e(H) for all graphons W. Conjecture 2.3 may be true even if Sidorenko’s conjecture were not.

- 2.3. Sparse limit. Since Ip is decreasing in [0,p] and increasing in [p,1], any minimizing W for LTp(H,q) satisﬁes 0 ≤ W ≤ p almost everywhere. Let


h(x) := xlog x − x + 1 so that

p−1Ip(px) = h(x) uniformly for x ∈ [0,1]. It follows that for every graph H and 0 ≤ r ≤ 1 we have lim

lim

p→0

p−1LTp(H,pr) = LT(H,r) (2.1) where

p→0

minimize E[h(W)] subject to t(H,W) ≤ re(H).

LT(H,r) :=

(2.2)

It would be interesting to solve this variational problem. As before, a basic question is whether the constant function W ≡ r is a minimizer. Here is the main conjecture.

- Conjecture 2.4. Let H be a non-bipartite graph and 0 ≤ r ≤ 1. There exists a 0 < rH∗ < 1 so that W ≡ r minimizes LT(H,r) if and only if r ≥ rH∗ . Furthermore, W is the unique minimizer for LT(H,r) if and only if r > rH∗ .

The conjecture remains open for any non-bipartite graph H. For the bipartite case:

- Conjecture 2.5. The constant graphon W ≡ r is the unique minimizer for LT(H,r) for every bipartite graph H and every 0 ≤ r ≤ 1.


In proving Theorem 2.1 and Theorem 2.2, we obtain the following results in the direction of the above conjectures.

- Theorem 2.6. If 0.466··· < r ≤ 1, then the constant graphon W ≡ r uniquely minimizes LT(K3,r). If 0 ≤ r < 0.209..., then the constant graphon W ≡ r does not minimize LT(K3,r).

I conjecture that, in Conjecture 2.4, rK∗

3

= 0.209....

- Theorem 2.7. Let H be a graph. There exists rH < 1 such that W ≡ r uniquely minimizes LT(H,r) whenever rH ≤ r ≤ 1. If H is nonbipartite, then there exists rH > 0 such that W ≡ r does not minimize LT(H,r) for 0 ≤ r < rH.


Combining these results with the framework of Chatterjee and Dembo [7], we obtain

Corollary 2.8. Let H be a graph. There is some explicit αH > 0 so that for p = pn → 0 with p ≥ n−α, the following large deviation results hold.

There exists rH < 1 so that for all r ∈ (rH,1), lim

2 n2p

log P(t(H,G(n,p)) ≤ (rp)e(H)) = −h(r).

n→∞

If H is non-bipartite, then there exists rH > 0 so that for all r ∈ (0,rH), liminf

2 n2p

log P(t(H,G(n,p)) ≤ (rp)e(H)) > −h(r).

n→∞

For H = K3, we may take rK3 = 0.466... and rK3 = 0.209....

3. Review of the proof for triangle upper tails

We begin with a quick review of the proof of the upper tail result from [28], as some of the ideas are used in the proof of Theorem 2.1.

The following extension of H¨lder’s inequality is very useful. See [28, Corollary 3.2].

- Proposition 3.1. Let H be a graph with maximum degree ∆. For any symmetric measurable


- function W : [0,1]2 → R, we have t(H,W) ≤ E[|W|∆]e(H)/∆. In particular, t(K3,W) ≤ E[W2]3/2.


The inequality can be proved via repeated applications of H¨lder’s inequality (when H = K3, it takes three applications of the Cauchy–Schwarz inequality). Observe that the inequality t(K3,W) ≤ E[W2]3/2 strengthens a corollary of the Kruskal–Katona theorem on the maximum possible triangle density in a graph of given edge density: t(K3,W) ≤ E[W]3/2.

The following result from [28] gives the full replica symmetric phase for UTp(K3,q), the upper tail problem for triangle densities.

- Theorem 3.2. Let 0 < p ≤ q < 1. If the point (q2,Ip(q)) lies on the convex minorant of the function x  → Ip(√x), then W ≡ q is the unique minimizer of UTp(K3,q).

The upper tail boundary curve in Figure 1 is characterized by the condition in Theorem 3.2. See [28, Lemma 3.1] for the proof of symmetry breaking, i.e., UTp(K3,q) < Ip(q), to the left of the boundary curve.

Proof. By the convex minorant condition, the tangent line to the function Ip(√x) at x = q2 lies below the function, so that

Ip(√x) ≥ Ip(q) +

I p(q) 2q

(x − q2), ∀x ∈ [0,1].

Replacing x by x2, we get

Ip(x) ≥ Ip(q) +

I p(q) 2q

(x2 − q2), ∀x ∈ [0,1]. (3.1)

Note that I p(q) > 0 since q > p.

Suppose graphon W satisﬁes t(K3,W) ≥ q3. By Proposition 3.1, we have E[W2] ≥ t(K3,W)3/2 ≥ q2. Thus (3.1) implies that

E[Ip(W)] ≥ Ip(q) +

I p(q) 2q

(E[W2] − q2) ≥ Ip(q).

This shows that W ≡ q is a minimizer for UTp(K3,q), and furthermore it is not too hard to check equality conditions to verify that this is the unique minimizer.

4. Triangle lower tails In this section we prove Theorems 2.1 and 2.6.

- 4.1. Replica symmetry phase. We begin with a small modiﬁcation of Goodman’s theorem [13] (which is usually generally stated for U + W ≡ 1).


- Lemma 4.1. If U and W are graphon such that U + W ≥ 2q for some constant q ≥ 0, then t(K3,W) + t(K3,U) ≥ 2q3.


Proof. By decreasing U and W (while remaining nonnegative), we may assume that they are graphons satisfying U + W ≡ 2q. Let U = q + X and W = q − X for some symmetric measurable

- function X : [0,1]2 → R. Then t(K3,W) + t(K3,U) = t(K3,q + X) + t(K3,q − X)


= 2q3 + 6q t(K1,2,X) ≥ 2q3 + 6q(E[X])2 ≥ 2q3.

For any a ∈ R we write a+ := max{a,0}. In the Proposition below, a2+ means (a+)2. The inequality (4.1) below is motivated by considering the tangent line to x  → Ip(2q −

√x) at x = q2, as in the proof of Theorem 3.2.

- Proposition 4.2. Let 0 < q ≤ p < 1 be such that


Ip(x) ≥ Ip(q) + −I p(q) 2q

((2q − x)2+ − q2) ∀x ∈ [0,p]. (4.1)

- Then W ≡ q is the unique minimizer of LTp(K3,q). Proof. Suppose W satisﬁes t(K3,W) ≤ q3. Apply Lemma 4.1 to W and U := (2q − W)+ to obtain


t(K3,(2q − W)+) ≥ 2q3 − t(K3,W) ≥ q3. Next, apply Proposition 3.1 and we obtain

E[(2q − W)2+] ≥ t(K3,(2q − W)+)2/3 ≥ q2. By (4.1) we have (note that I p(q) ≤ 0 as q ≤ p)

E[Ip(W)] ≥ Ip(q) + −I p(q) 2q

(E[(2q − W)2+] − q2) ≥ Ip(q).

It follows that LTp(K3,q) = Ip(q). To show that W ≡ q is the unique minimizer, observe that in order for any other W to be a minimizer, equality must occur at every step above. In particular, if (4.1) has single point of equality, namely for x = q, then the uniqueness of W is clear. Otherwise, one can check (details omitted, but see Figure 2) that that (4.1) has at most two points of equality, with one being x = q, so that if W has any positive mass with value being the other point of equality, then it would be impossible for t(K3,W) = q3 to hold. This shows that W ≡ q is the unique minimizer.

To derive results about the phase diagram, we shall invoke various technical statements (referred to as “Facts”) about the functions Ip and h. Using Fact 4.3 below we obtain the 0 ≤ p ≤ 1/2 portion of the curve q of Theorem 2.1, which is given by the implicit equation Ip(q) + 21qI p(q) = 0, and shown in Figure 1. The rest of the curve in Figure 1 is produced by numerically checking (3.1). Taking the p → 0 limit of the implicit equation, we see that the slope at the origin equals to r = 0.466..., where r satisﬁes h(r) + 12rh (r) = 0. This completes the proof of the replica symmetric phase in Theorem 2.1.

Fact 4.3. For 0 < q ≤ p ≤ 1/2, (4.1) holds for all x ∈ [0,p] if and only if it holds at x = p. Proof. Let

I p(q) 2q

((2q − x)2+ − q2). (4.2) We plotted f for some representative values of (p,q) in Figure 2.

f(x) := fp,q := Ip(x) − Ip(q) +

Suppose f(p) ≥ 0. We have

I p(q) q

f (x) = I p(x) −

(2q − x)+

0.010

0.005

0.000

0.05 0.1

0.05 0.1

0.05 0.1

0.05 0.1

(p, q) = (0.1, 0.045)

(p, q) = (0.1, 0.047)

(p, q) = (0.1, 0.05)

(p, q) = (0.1, 0.06)

Figure 2. Plots of fp,q from (4.2) for p = 0.1 and various values of q.

and

I p(q) q

I p(q) q

1 x(1 − x)

f (x) = I p(x) +

1x<2q =

+

1x<2q.

Since p ≤ 1/2, f (x) is decreasing for 0 < x < min{p,2q}. Clearly f is positive near x = 0. We consider two cases.

- Case I: f (x) > 0 for all 0 < x < min{p,2q}. Then f is convex on (0,min{p,2q}). We know that

f(q) = f (q) = 0. Then f(x) ≥ 0 for all x ∈ [0,min{p,2q}]. If 2q ≥ p, then we are done, otherwise, note that f(x) = Ip(x) − Ip(q) − qI p(q)/2 for x ∈ [2q,p], and it is decreasing on this interval. Since we assumed that f(p) ≥ 0, we obtain f(x) ≥ 0 for all x ∈ [0,p].

- Case II: there is some x0 ∈ (0,min{p,2q}) such that f (x0) = 0. So f is convex on (0,x0) and


concave on (x0,min{p,2q}). We assumed that f(p) ≥ 0, so f(min{p,2q}) ≥ 0 since if 2q < p then f is decreasing on (2q,p). Since f(q) = f (q) = 0, an analysis of the convexity of f shows that it is nonnegative on [0,p].

For the sparse limit p → 0, the proof of the ﬁrst half of Theorem 2.6 is nearly identical. It follows from the following two propositions, whose proofs we omit.

- Proposition 4.4. Let 0 ≤ r ≤ 1 be such that


h(x) ≥ h(r) + −h (r) 2r

((2r − x)2+ − r2) ∀x ∈ [0,1]. (4.3)

- Then W ≡ r is the unique minimizer of LT(K3,r).


- Fact 4.5. The inequality (4.3) holds for all x ∈ [0,1] if and only if holds for x = 1, which holds if and only if r ≥ r = 0.466..., where r satisﬁes h(r) + 21rh (r) = 0.


- 4.2. Symmetry breaking phase. Now we explain the lower curve q in Figure 1. It is obtained by


by restricting the variational problem LTp(K3,q) to graphons W of the form BIPa,b, where BIPa,b, for 0 ≤ a,b ≤ 1, is deﬁned by

- a if (x,y) ∈ [0,1/2]2 ∪ (1/2,1]2,
- b if (x,y) ∈ [0,1/2] × (1/2,1] ∪ (1/2,1] × [0,1/2].


BIPa,b(x,y) :=

(4.4)

There is symmetry breaking as long as we can ﬁnd 0 ≤ a,b ≤ p satisfying E[Ip(BIPa,b)] =

- 1

- 2


- 1

- 2


Ip(b) < Ip(q) (4.5) and

Ip(a) +

- 3

- 4


1 4

a3 +

ab2 ≤ q3. (4.6)

t(K3,BIPa,b) =

We can assume that 0 ≤ a ≤ q ≤ b ≤ p, since otherwise swapping a and b reduces t(K3,W) (observe that t(K3,BIPa,b) − t(K3,BIPb,a) = 41(a − b)3) while keeping E[Ip(W)] constant.

0.002

0.001

0.000

0.01 0.02

−0.001

(p, q) = (0.1, 0.021)

0.01 0.02

(p, q) = (0.1, 0.0215)

0.01 0.02

(p, q) = (0.1, 0.022)

### Figure 3. The plot of fp,q from (4.7) for p = 0.1 and various values of q.

0.020

0.010

0.000

0.1 0.2

r = 0.2

0.1 0.2

r = 0.209

0.1 0.2

r = 0.21

Figure 4. The plot of fr from (4.8) for various values of r.

Set b = (4q3 − a3)/(3a) so that t(K3,BIPa,b) = q3. There is symmetry breaking if

4q3 − x3 3x − Ip(q) (4.7)

- 1

- 2


- 1

- 2


f(x) := fp,q(x) :=

Ip(x) +

Ip

is negative for some 0 ≤ x ≤ q, where f is only deﬁned for (4q3 − x3)/(3x) ≤ p. Some representative examples of f are plotted in Figure 3. For every p, and suﬃciently small q, f(x) becomes negative in a region away from x = q.

Now we prove the claims in Theorem 2.1 more rigorously. For every p > 0, if q is suﬃciently small

so that 21Ip(0) < Ip(q), then W = BIP0,p satisﬁes t(K3,W) = 0 while E[Ip(W)] = 21Ip(0) < Ip(q), so that LTp(K3,q) < Ip(q).

The argument in the previous paragraph does not give the optimal q in Theorem 2.1. To prove that q can be chosen so that limp→0 q(p)/p = 0.209..., it suﬃces, by (2.1), to prove the second half of Theorem 2.6, that LT(K3,r) < h(r) for all r < r1 = 0.209.... As before, we seek 0 ≤ a ≤ r ≤ b ≤ 1 with

- 1

- 2


- 1

- 2


h(b) < h(r) and

h(a) +

1 4

- 3

- 4


ab2 ≤ r3. Let

a3 +

4r3 − x3 3x − h(r). (4.8)

- 1

- 2


- 1

- 2


f(x) := fr(x) :=

h(x) +

h

See Figure 4 for some examples of plots of fr (as before, plotted for values of x ≤ r satisfying (4r3 − x3)/(3x) ≤ 1). At the critical r = r1 = 0.209..., there exists 0 < a1 < r1 < b1 < 1 such

that 41a31 + 34a1b21 = r13 and 12h(a1) + 12h(b1) = h(r1). Now for any 0 ≤ r < r1, let s = r/r1, so that

(a,b) = (sa1,sb1) satisﬁes 41a3 + 43ab2 = r3. Note that h(sx) = sxlog(sx) − sx + 1

= s(xlog x − x + 1) + (slog s)x − s + 1 = sh(x) + (slog s)x − s + 1. We have

- 1

- 2


- 1

- 2


- 1

- 2


- 1

- 2


h(b) − h(r) =

h(sb1) − h(sr1)

h(a) +

h(sa1) +

- 1

- 2


- 1

- 2


- 1

- 2


- 1

- 2


b1 − r1) < 0

h(b1) − h(r1)) + (slog s)(

h(a1) +

a1 +

= s(

where we know (a1 + b1)/2 > r from

- 1

- 2


- 1

- 2


a1 +

b1

3

− r13 =

=

- 1

- 2


- 1

- 2


a1 +

b1

1 2

1 2

b1 −

a1

3

1 4

a31 −

−

3

> 0

- 3

- 4


a1b21

It follows that LT(K3,r) < Ip(r) for all 0 < r < r1 = 0.209....

5. General subgraph lower tails

In this section we prove Theorems 2.2 and 2.7. I will give the details only for Theorem 2.7 concerning the sparse limit LT(H,r) as it is somewhat cleaner and contains all the ideas. Theorem 2.2 regarding LTp(H,q) can be proved analogously by considering suﬃciently small but ﬁxed values of p.

- 5.1. Replica symmetry. For any graph H and graphon W, we deﬁne the functional derivative t (H,W) to be the symmetric measurable function given by


t (H,W) =

e∈E(H)

where for each ab ∈ E(H), we deﬁne the graphon

te(H,W) (5.1)

tab(H,W)(xa,xb) :=

For example,

W(xi,xj)

dxi. (5.2)

[0,1]V (H)\{a,b}

ij∈E(H)\{ab}

i∈V (H)\{a,b}

t (K3,W)(x,y) = 3

W(x,z)W(y,z)dz.

[0,1]

For any symmetric measurable U : [0,1]2 → [−1,1], and δ → 0, we have

t(H,W + δU) = t(H,W) + δ E[t (H,W)U] + O(δ2), which justiﬁes calling t (H,W) the functional derivative.

- Lemma 5.1. Let H be a graph and 0 < r < 1. The variational problem LT(H,r) attains its minimum for some graphon W, and any such W satisﬁes the following Lagrange multiplier condition: for some λ ≥ 0, one has


h (W(x,y)) + λt (H,W)(x,y) = 0, a.e.-(x,y) ∈ [0,1]2.

Proof. That the minimum of LT(H,r) is always attained follows from the compactness of the space of graphons with respect to the cut distance and the convexity of h, as was already observed in [10].9

Suppose W minimizes LT(H,r). We claim that for any symmetric measurable function U : [0,1]2 → [−1,1] such that 0 ≤ W + U ≤ 1 and E[t (H,W)U] < 0, one has E[h (W)U] ≥ 0. Indeed, consider the graphon W + δU for δ 0. One has

t(H,W + δU) − t(H,W) = δE[t (H,W)U] + O(δ2).

Thus t(H,W + δU) < t(H,W) ≤ re(H) for suﬃciently small δ > 0, and hence E[h(W + δU)] ≥ E[h(W)] since W minimizes LT(H,r). On the other hand,

E[h(W + δU) − h(W)] δ

= E[h (W)U],

lim

δ→0

so that E[h (W)U] ≥ 0 as claimed. The interchange of limit and expectation above can be justiﬁed by writing U = U+ − U−, where U+ = max{U,0} and U− = max{−U,0}. Since h is convex, (h(W + δU+) − h(W))/δ is pointwise monotonically decreasing as δ 0, and likewise (h(W − δU−)−h(W))/δ is pointwise monotonically increasing. So the interchange of limit and expectation follows from the monotone convergence theorem.

The lemma follows easily from the claim we just proved.

- Lemma 5.2. Let H be a graph with m edges, and 0 < r ≤ 1. Let W minimize LT(H,r). Then W ≥ rmr−m almost everywhere.

Proof. Let c = rmr−m. Suppose on the contrary that W < c on a set of positive measure. Let λ be the Lagrange multiplier in Lemma 5.1. From (5.1) we have t (H,W) ≤ m everywhere. By considering a positive-measure set of (x,y) such that W(x,y) < c, we ﬁnd

0 = h (W(x,y)) + λt (H,W)(x,y) < h (c) + mλ. So that

λ > −h (c) m

=

log(1/c) m

. Therefore, up to a set of measure zero, for every (x,y) with W(x,y) ≥ rm, we have t (H,W)(x,y) = −h (W(x,y)) λ

< −mh (rm) log(1/c)

=

mlog(r−m) log(r−mr−m)

= mrm.

On the other hand, for every (x,y) with W(x,y) < rm, we have t (H,W)(x,y)W(x,y) < mrm. Thus t (H,W)W < mrm almost everywhere. By (5.1) and (5.2), we have

t(H,W) =

1 m

E[t (H,W)W] < rm.

However, any W with t(H,W) < rm cannot minimize LT(H,r). This gives the desired contradiction.

- Lemma 5.3. If t(H,W) ≤ re(H), then E[log W] ≤ log r.


9We sketch here an alternate proof of the fact that the minimum is always attained. Let Wn be a sequence of graphons with t(H, Wn) ≥ re(H) and E[h(Wn)] → LT(H, r). By compactness of the space of graphons [26], there exists a subsequential limit W so that δ (Wn, W) → 0 along some subsequence. Restrict to this subsequence. We have t(H, Wn) → t(H, W), so that t(H, W) ≥ re(H). It remains to show that E[h(W)] ≤ lim E[h(Wn)] = LT(H, r). We do not lose anything by assuming that Wn − W → 0. Let Pm denote the partition of the unit interval [0, 1] into m equal-length intervals. Let WPm denote W with its value inside each Ii × Ij replaced by its average, for every Ii, Ij ∈ Pm. Deﬁne (Wn)Pm similarly. Then Wn − W → 0 implies that (Wn)Pm → WPm pointwise a.e. as n → ∞. By convexity, we have limn→∞ E[h(Wn)] ≥ lim infn→∞ E[h((Wn)Pm)] = E[h(WPm)]. Furthermore, WPm → W pointwise a.e. by the Lebesgue density theorem, so limm→∞ E[h(WPm)] = E[h(W)]. It follows that E[h(W)] ≤ lim E[h(Wn)] = LT(H, r), as desired.

m 3 4 5 6 7 8 9 10 20 100 rm 0.686 0.735 0.770 0.795 0.815 0.831 0.844 0.855 0.911 0.973

Table 1. Some values of rm from Proposition 5.4.

Proof. The lemma follows from Jensen’s inequality:

 

 

mE[log W] =

W(xi,xj)

dxi

log

[0,1]V (H)

ij∈E(H)

i∈V (H)

  = log t(H,W) ≤ mlog r.

 

≤ log

dxi

W(xi,xj)

[0,1]V (H) ij∈E(H)

i∈V (H)

- Proposition 5.4. Let H be a graph with m ≥ 1 edges. Let r = rm (see Table 1) be the unique solution in the interval (0,1) to the equation


h(rmr−m) = h(r) + r h(r)(log(rmr−m) − log r) Then LT(H,r) is uniquely minimized by the constant function W ≡ r for all r ≥ rm. Proof. Let r ≥ rm. Let W be a minimizer for LT(H,r). By Lemma 5.2, W ≥ rmr−m almost everywhere. Thus it follows by Fact 5.5 below (and it can be checked that rm ≥ 1/e) that

h(W) ≥ h(r) + r log r(log W − log r) a.e. (5.3)

Taking expectation of both sides and using E[log W] ≤ log r from Lemma 5.3 (note that log r ≤ 0), we obtain E[h(W)] ≥ h(r), as desired. To see that W ≡ r is unique, suppose W is another minimizer of LT(H,r). Equality must hold everywhere in the argument. In particular, (5.3) must hold almost everywhere, which easily implies that W ≡ r (for the critical case r = rm, W might also take the value rmr−m, but only on a set of measure zero since E[h(W)] = h(r)).

- Fact 5.5. If h(x) ≥ h(r) + rh (r)(log x − log r) (5.4)


holds for some (x,r) = (x0,r0), with 0 ≤ x0 ≤ r0 ≤ 1 and r0 ∈ [1/e,1], then it holds for all (x,r) ∈ [x0,1] × [r0,1].

Proof. The partial derivative of the RHS of (5.4) with respect to r is −(1 + log r)(log r − log x), which is at most zero as long as x ≤ r and r ≥ 1/e. This shows that if (5.4) holds for some (x,r) = (x0,r0) then it automatically holds for (x,r) = (x0,r) for all r ∈ [r0,1].

Let us now ﬁx r. Let

f(x) := fr(x) := h(x) − h(r) − rh (r)(log x − log r). (5.5) Some examples of fr are plotted in Figure 5. We have

r log r x

x + r log r x2

f (x) = log x −

and f (x) =

.

So f (x) < 0 for x < −r log r and f (x) > 0 for x > −r log r. Note also that f(r) = f (r) = 0, and −r log r ≤ r as long as r ≥ 1/e. By analyzing the convexity of f (see Figure 5), we see that f(x0) ≥ 0 implies f(x) ≥ 0 for all x ∈ [x0,1].

0.150

0.100

0.050

0.000

0.5 1

0.5 1

0.5 1 −0.050

r = 0.5

r = 0.6

r = 0.7

Figure 5. Plot of fr from (5.5) for various values of r.

- 5.2. Symmetry breaking. The proof of the second part of Theorem 2.7 is easy. One can ﬁne tune the bounds as in Section 4.2 though we omit the analysis here.


- Proposition 5.6. Let H be a nonbipartite graph. Then LT(H,r) < h(r) for all r < 0.186.


Proof. The graphon W = BIP0,1 satisﬁes t(H,W) = 0, and E[h(W)] = 12h(0), which is strictly less than h(r) for all r < 0.186.

6. Open problems

We conclude with some open problems concerning the variational problem for upper and lower tails.

- • Upper tail phase diagram. Determine the upper tail replica symmetry phase diagram for non-regular H.
- • Lower tail phase diagram. Determine the lower tail replica symmetry phase diagram

for K3, and more generally for any non-bipartite graph H. In particular, determine rH∗ from Conjecture 2.4. For a bipartite graph H, determine whether there is replica symmetry

everywhere (Conjecture 2.3).

- • Solution in the symmetry breaking phase. Solve the variational problem UT or LT at any non-trivial point where the constant graphon is not a minimizer.


Acknowledgments. I would like to thank Eyal Lubetzky for helpful discussions.

References

- [1] D. Aristoﬀ and C. Radin. Emergent structures in large networks. J. Appl. Probab., 50(3):883–888, 2013.
- [2] D. Aristoﬀ and L. Zhu. Asymptotic structure and singularities in constrained directed graphs. arXiv:1405.2466.
- [3] D. Aristoﬀ and L. Zhu. On the phase transition curve in a directed exponential random graph model. arXiv:1404.6514.
- [4] C. Borgs, J. T. Chayes, L. Lova´sz, V. T. So´s, and K. Vesztergombi. Convergent sequences of dense graphs. I. Subgraph frequencies, metric properties and testing. Adv. Math., 219(6):1801–1851, 2008.
- [5] C. Borgs, J. T. Chayes, L. Lova´sz, V. T. So´s, and K. Vesztergombi. Convergent sequences of dense graphs II. Multiway cuts and statistical physics. Ann. of Math. (2), 176(1):151–219, 2012.
- [6] S. Chatterjee. The missing log in large deviations for triangle counts. Random Structures Algorithms, 40(4):437– 451, 2012.
- [7] S. Chatterjee and A. Dembo. Nonlinear large deviations. arXiv:1401.3495.
- [8] S. Chatterjee and P. S. Dey. Applications of Stein’s method for concentration inequalities. Ann. Probab., 38(6):2443–2485, 2010.
- [9] S. Chatterjee and P. Diaconis. Estimating and understanding exponential random graph models. Ann. Statist., to appear.
- [10] S. Chatterjee and S. R. S. Varadhan. The large deviation principle for the Erdo˝s-Re´nyi random graph. European J. Combin., 32(7):1000–1017, 2011.
- [11] D. Conlon, J. Fox, and B. Sudakov. An approximate version of Sidorenko’s conjecture. Geom. Funct. Anal., 20(6):1354–1366, 2010.


- [12] B. DeMarco and J. Kahn. Upper tails for triangles. Random Structures Algorithms, 40(4):452–459, 2012.
- [13] A. W. Goodman. On sets of acquaintances and strangers at any party. Amer. Math. Monthly, 66:778–783, 1959.
- [14] H. Hatami. Graph norms and Sidorenko’s conjecture. Israel J. Math., 175:125–150, 2010.
- [15] S. Janson. Poisson approximation for large deviations. Random Structures Algorithms, 1(2):221–229, 1990.
- [16] S. Janson, T.  Luczak, and A. Rucin´ski. Random graphs. Wiley-Interscience Series in Discrete Mathematics and Optimization. Wiley-Interscience, New York, 2000.
- [17] S. Janson and L. Warnke. The lower tail: Poisson approximation revisited. arXiv:1406.1248.
- [18] G. Katona. A theorem of ﬁnite sets. In Theory of graphs (Proc. Colloq., Tihany, 1966), pages 187–207. Academic Press, New York, 1968.
- [19] R. Kenyon, C. Radin, K. Ren, and L. Sadun. Multipodal structure and phase transitions in large constrained graphs. arXiv:1405.0599.
- [20] R. Kenyon and M. Yin. On the asymptotics of constrained exponential random graphs. arXiv:1406.3662.
- [21] J. Kim, C. Lee, and J. Lee. Two approaches to sidorenko’s conjecture. Trans. Amer. Math. Soc. to appear.
- [22] J. B. Kruskal. The number of simplices in a complex. In Mathematical optimization techniques, pages 251–278. Univ. of California Press, Berkeley, Calif., 1963.
- [23] J. L. X. Li and B. Szegedy. On the logarithmic calculus and sidorenko’s conjecture. Combinatorica. to appear.
- [24] L. Lova´sz. Large networks and graph limits, volume 60 of American Mathematical Society Colloquium Publications. American Mathematical Society, Providence, RI, 2012.
- [25] L. Lova´sz and B. Szegedy. Limits of dense graph sequences. J. Combin. Theory Ser. B, 96(6):933–957, 2006.
- [26] L. Lova´sz and B. Szegedy. Szemere´di’s lemma for the analyst. Geom. Funct. Anal., 17(1):252–270, 2007.
- [27] E. Lubetzky and Y. Zhao. On the variational problem for upper tails in sparse random graphs. arXiv:1402.6011.
- [28] E. Lubetzky and Y. Zhao. On replica symmetry of large deviations in random graphs. Random Structures Algorithms, to appear.
- [29] V. Nikiforov. The number of cliques in graphs of given order and size. Trans. Amer. Math. Soc., 363(3):1599–1618, 2011.
- [30] C. Radin, K. Ren, and L. Sadun. The asymptotics of large constrained graphs. J. Phys. A, 47(17):175001, 20, 2014.
- [31] C. Radin and L. Sadun. Singularities in the entropy of asymptotically large simple graphs. J. Stat. Phys. to appear.
- [32] C. Radin and L. Sadun. Phase transitions in a complex network. J. Phys. A, 46(30):305002, 12, 2013.
- [33] C. Radin and M. Yin. Phase transitions in exponential random graphs. Ann. Appl. Probab., 23(6):2458–2471, 2013.
- [34] A. A. Razborov. On the minimal density of triangles in graphs. Combin. Probab. Comput., 17(4):603–618, 2008.
- [35] C. Reiher. The clique density theorem. arXiv:1212.2454.
- [36] A. Sidorenko. A correlation inequality for bipartite graphs. Graphs Combin., 9(2):201–204, 1993.
- [37] B. Szegedy. Relative entropy and Sidorenko’s conjecture. arXiv:1406.6738.
- [38] A. Thomason. A disproof of a conjecture of Erdo˝s in Ramsey theory. J. London Math. Soc. (2), 39(2):246–255, 1989.
- [39] M. Yin. Large deviations and exact asymptotics for constrained exponential random graphs. arXiv:1412.6001.
- [40] M. Yin. Critical phenomena in exponential random graphs. J. Stat. Phys., 153(6):1008–1021, 2013.
- [41] M. Yin, A. Rinaldo, and S. Fadnavis. Asymptotic quantization of exponential random graphs.
- [42] M. Yin and L. Zhu. Asymptotics for sparse exponential random graph models. arXiv:1411.4722.
- [43] M. Yin and L. Zhu. Reciprocity in directed networks. arXiv:1412.2187.
- [44] L. Zhu. Asymptotic structure of constrained exponential random graph models. arXiv:1408.1536.


Department of Mathematics, MIT, Cambridge, MA 02139. E-mail address: yufeiz@mit.edu

