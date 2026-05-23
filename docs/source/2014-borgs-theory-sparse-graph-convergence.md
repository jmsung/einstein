---
type: source
kind: paper
title: "An $L^p$ theory of sparse graph convergence I: limits, sparse random graph models, and power law distributions"
authors: Christian Borgs, Jennifer T. Chayes, Henry Cohn, Yufei Zhao
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1401.2906v4
source_local: ../raw/2014-borgs-theory-sparse-graph-convergence.pdf
topic: general-knowledge
cites:
---

# arXiv:1401.2906v4[math.CO]29Dec2014

## AN Lp THEORY OF SPARSE GRAPH CONVERGENCE I: LIMITS, SPARSE RANDOM GRAPH MODELS, AND POWER LAW DISTRIBUTIONS

CHRISTIAN BORGS, JENNIFER T. CHAYES, HENRY COHN, AND YUFEI ZHAO

Abstract. We introduce and develop a theory of limits for sequences of sparse graphs based on Lp graphons, which generalizes both the existing L∞ theory of dense graph limits and its extension by Bolloba´s and Riordan to sparse graphs without dense spots. In doing so, we replace the no dense spots hypothesis with weaker assumptions, which allow us to analyze graphs with power law degree distributions. This gives the ﬁrst broadly applicable limit theory for sparse graphs with unbounded average degrees. In this paper, we lay the foundations of the Lp theory of graphons, characterize convergence, and develop corresponding random graph models, while we prove the equivalence of several alternative metrics in a companion paper.

Contents

- 1. Introduction 1
- 2. Deﬁnitions and results 4
- 3. Lp graphons 15
- 4. Regularity lemma for Lp upper regular graph(on)s 19
- 5. Limit of an Lp upper regular sequence 25
- 6. W-random weighted graphs 29
- 7. Sparse random graphs 30
- 8. Counting lemma for Lp graphons 33 Acknowledgments 36


- Appendix A. Lp upper regularity implies unbounded average degree 36
- Appendix B. Proof of a Chernoﬀ bound 37
- Appendix C. Uniform upper regularity 38 References 42


1. Introduction

Understanding large networks is a fundamental problem in modern graph theory. What does it mean for two large graphs to be similar to each other, when they may diﬀer in obvious ways such as their numbers of vertices? There are many types of networks (biological, economic, mathematical, physical, social, technological, etc.), whose details vary widely, but similar structural and growth phenomena occur in all these domains. In each case, it is natural to consider a sequence of graphs with

Zhao was supported by a Microsoft Research PhD Fellowship and internships at Microsoft Research New England.

1

size tending to inﬁnity and ask whether these graphs converge to any meaningful sort of limit.

For dense graphs, the theory of graphons provides a comprehensive and ﬂexible answer to this question (see, for example, [8, 9, 25, 26, 27]). Graphons characterize the limiting behavior of dense graph sequences, under several equivalent metrics that arise naturally in areas ranging from statistical physics to combinatorial optimization. Because dense graphs have been the focus of much of the graph theory developed in the last half century, graphons and related structural results about dense graphs play a foundational role in graph theory. However, many large networks of interest in other ﬁelds are sparse, and in the dense theory all sparse graph sequences converge to the zero graphon. This greatly limits the applicability of graphons to real-world networks. For example, in statistical physics dense graph sequences correspond to mean-ﬁeld models, which are conceptually important as limiting cases but rarely applicable in real-world systems.

At the other extreme, there is a theory of graph limits for very sparse graphs, namely those with bounded degree or at least bounded average degree [1, 2, 4, 29] (see also [31, 32, 33, 34] for a broader framework based on ﬁrst-order logic). Although this theory covers some important physical cases, such as crystals, it also does not apply to most networks of current interest. And although it is mathematically completely diﬀerent in spirit from the theory of dense graph limits, it is also limited in scope. It covers the case of n-vertex graphs with O(n) edges, while dense graph limits are nonzero only when there are Ω(n2) edges.

Bollob´as and Riordan [6] took an important step towards bridging the gap between these theories. They adapted the theory of graphons to sparse graphs by renormalizing to ﬁx the eﬀective edge density, which captures the intuition that two graphs with diﬀerent densities may nevertheless be structurally similar. Under a boundedness assumption (Assumption 4.1 in [6]), which says that there are no especially dense spots within the graph, they showed that graphons remain the appropriate limiting objects. In other words, sparse graphs without dense spots converge to graphons after rescaling. Thus, these sparse graph sequences are characterized by their asymptotic densities and their limiting graphons.

The Bollob´as-Riordan theory extends the scope of graphons to sparse graphs, but the boundedness assumption is nevertheless highly restrictive. In loose terms, it means the edge densities in diﬀerent parts of the graph are all on roughly the same scale. By contrast, many of the most exciting network models have statistics governed by power laws [11, 30]. Such models generally contain dense spots, and we therefore must broaden the theory of graphons to handle them.

One setting in which these diﬃculties arise in practice is statistical estimation of network structure. Each graphon has a corresponding random graph model converging to it, and it is natural to try to ﬁt these models to an observed network and thus estimate the underlying graphon (see, for example, [5]). Using the Bolloba´sRiordan theory, Wolfe and Olhede [37] developed an estimator and proved its consistency under certain regularity conditions. Their theorems provide valuable statistical tools, but the use of the Bolloba´s-Riordan theory limits the applicability of their approach to graphs without dense spots and thus excludes many important cases.

In this paper, we develop an Lp theory of graphons for all p > 1, in contrast with the L∞ theory studied in previous papers.1 The Lp theory provides for the ﬁrst time the ﬂexibility to account for power laws, and we believe it is the right convergence theory for sparse graphs (outside of the bounded average degree regime). It generalizes dense graph limits and the Bollob´as-Riordan theory, which together are the special case p = ∞, and it extends all the way to the natural barrier of p = 1.

It is also worth noting that, in the process of developing an Lp theory of graphons, we give a new Lp version of the Szemer´edi regularity lemma for all p > 1 in its so-called weak (integral) form, which also naturally suggests the correct formulation for stronger forms. Long predating the theory of graph limits and graphons, it was recognized that the regularity lemma is a cornerstone of modern graph theory and indeed other aspects of discrete mathematics, so attempts were made to extend it to non-dense graphs. Our Lp version of the weak Szemer´edi regularity lemma generalizes and extends previous work, as discussed below.

We will give precise deﬁnitions and theorem statements in §2, but ﬁrst we sketch some examples motivating our theory.

We begin with dense graphs and L∞ graphons. The most basic random graph model is the Erdo˝s-Re´nyi model Gn,p, with n vertices and edges chosen independently with probability p between each pair of vertices. One natural generalization replaces p with a symmetric k × k matrix; then there are k blocks of n/k vertices each, with edge density pi,j between the i-th and j-th blocks. As k → ∞, the matrix becomes a symmetric, measurable function W : [0,1]2 → [0,1] in the continuum limit. Such a function W is an L∞ graphon. All large graphs can be approximated by k × k block models with k large via Szemere´di regularity, from which it follows that limits of dense graph sequences are L∞ graphons.

For sparse graphs the edge densities will converge to zero, but we would like a more informative answer than just W = 0. To determine the asymptotics, we rescale the density matrix p by a function of n so that it no longer tends to zero. In the Bolloba´s-Riordan theory, the boundedness assumption ensures that the densities are of comparable size (when smoothed out by local averaging) and hence remain bounded after rescaling. They then converge to an L∞ graphon, and the known results on L∞ graphons apply modulo rescaling.

For an example that cannot be handled using L∞ graphons, consider the following conﬁguration model. There are n vertices numbered 1 through n, with probability min(1,nβ(ij)−α) of an edge between i and j, where 0 < α < 1 and 0 ≤ β < 2α. In other words, the probabilities behave like (ij)−α, but boosted by a factor of nβ in case they become too small.2 This model is one of the simplest ways to get a power law degree distribution, because the expected degree of vertex i scales according to an inverse power law in i with exponent α. The expected number of edges is on the order of nβ−2α+2, which is superlinear when β > 2α − 1. However, rescaling by the edge density nβ−2α does not yield an L∞ graphon. Instead, we get W(x,y) = (xy)−α, which is unbounded.

- 1The paper [24] and the online notes to Section 17.2 of [25] go a little beyond L∞ graphons to

study graphons in 1≤p<∞ Lp.

- 2The inequalities α < 1 and β < 2α each have a natural interpretation: the ﬁrst avoids having


almost all the edges between a sublinear number of vertices, while the second ensures that the cut-oﬀ from taking the minimum with 1 aﬀects only a negligible fraction of the edges.

Unbounded graphons are of course far more expressive than bounded graphons, because they can handle an unbounded range of densities simultaneously. This issue does not arise for dense graphs: without rescaling, all densities are automatically bounded by 1. However, unboundedness is ubiquitous for sequences of sparse graphs.

To deal with unbounded graphons, we must reexamine the foundations of the theory of graphons. To have a notion of density at all, a graphon must at least be in L1([0,1]2). Neglecting for the moment the limiting case of L1 graphons, we show that Lp graphons are well behaved when p > 1. In the example above, the p > 1 case covers the full range 0 < α < 1, and we think of it as the primary case, while p = 1 is slightly degenerate and requires additional uniformity hypotheses (see Appendix C).

Each graphon W can be viewed as the archetype for a whole class of graphs, namely those that approximate it. It is natural to call these graphs W-quasirandom, because they behave as if they were randomly generated using W. From this perspective, the Lp theory of graphons completes the L∞ theory: it adds the missing graphons that describe sparse graphs but not dense graphs. The remainder of this paper is devoted to three primary tasks:

- (1) We lay the foundations of the Lp theory of graphons.
- (2) We characterize the sparse graph sequences that converge to Lp graphons via the concept of Lp upper regularity, and we establish the theory of convergence under the cut metric.
- (3) For each L1 graphon W, we develop sparse W-random graph models and show that they converge to W.


Our main theorems are Theorems 2.8 and 2.14, which deal with tasks 2 and 3, respectively. Theorem 2.8 says that every Lp upper regular sequence of graphs with

- p > 1 has a subsequence that converges to an Lp graphon, and Theorem 2.14 says that sparse W-random graphs converge to W with probability 1. We also prove a number of other results, which we state in Section 2. One topic we do not address here is “right convergence” (notions of convergence based on quotients or statistical physics models). We analyze right convergence in detail in the companion paper [7].


2. Definitions and results

- 2.1. Notation. We consider weighted graphs, which include as a special case simple unweighted graphs. We denote the vertex set and edge set of a graph G by V (G) and E(G), respectively.


In a weighted graph G, every vertex i ∈ V is given a weight αi = αi(G) > 0, and every edge ij ∈ E(G) (allowing loops with i = j) is given a weight βij = βij(G) ∈ R. We set βij = 0 whenever ij ∈/ E(G). For each subset U ⊆ V , we write

αU :=

αi and αG := αV (G).

i∈U

We say a sequence (Gn)n≥0 of weighted graphs has no dominant nodes if lim

maxi∈V (G

n) αi(Gn) αG

= 0.

n→∞

n

A simple (unweighted) graph is one in which αi = 1 for all i ∈ V , βij = 1 whenever ij ∈ E, and βij = 0 whenever ij ∈/ E. A simple graph contains no loops or multiple edges.

For c ∈ R, we write cG for the weighted graph obtained from G by multiplying all edge weights by c, while the vertex weights remain unchanged.

For 1 ≤ p ≤ ∞ we deﬁne the Lp norms

 

 

1/p

αiαj αG2 |βij|p

when 1 ≤ p < ∞

G p :=

i,j∈V (G)

and

|βij|.

G ∞ := max

i,j∈V (G)

The quantity G 1 can be viewed as the edge density when G is a simple graph. When considering sparse graphs, we usually normalize the edge weights by considering the

weighted graph G/ G 1, in order to compare graphs with diﬀerent edge densities. (Of course this assumes G 1 = 0, but that rules out only graphs with no edges, and we will often let this restriction pass without comment.)

In the previous works [8, 9] on convergence of dense graph sequences, only graphs with uniformly bounded G ∞ were considered. In this paper, we relax this assumption. As we will see, this relaxation is useful even for sparse simple graphs due to the normalization G/ G 1.

Given that we are relaxing the uniform bound on G ∞, one might think, given the title of this paper, that we impose a uniform bound on G p. This is not what we do. A bound on G p is too restrictive: for a simple graph G, an upper bound

1 p −1

on G/ G 1 p = G

1 corresponds to a lower bound on G 1, which forces G to be dense. Instead, we impose an Lp bound on edge densities with respect to vertex set partitions. This is explained next.

- 2.2. Lp upper regular graphs. For any S,T ⊆ V (G), deﬁne the edge density (or average edge weight, for weighted graphs) between S and T by


αsαt αSαT

ρG(S,T) :=

βst.

s∈S,t∈T

We introduce the following hypothesis. Roughly speaking, it says that for every partition of the vertices of G in which no part is too small, the weighted graph derived from averaging the edge weights with respect to the partition is bounded in Lp norm (after normalizing by the overall edge density of the graph).

- Deﬁnition 2.1. A weighted graph G (with vertex weights αi and edge weights βij) is said to be (C,η)-upper Lp regular if αi ≤ ηαG for all i ∈ V (G), and whenever


V1 ∪ ··· ∪ Vm is a partition of V (G) into disjoint vertex sets with αV

i ≥ ηαG for

each i, one has (2.1)

m

p

### αV

### αV

ρG(Vi,Vj) G 1

≤ Cp.

i

j

αG2

i,j=1

Informally, a graph G is (C,η)-upper Lp regular if G/ G 1 has Lp norm at most C after we average over any partition of the vertices into blocks of at least η |V (G)| in size (and no vertex has weight greater than ηαG). We allow p = ∞, in which case (2.1) must be modiﬁed in the usual way to

max

1≤i,j≤m

ρG(Vi,Vj) G 1 ≤ C.

Strictly speaking, we should move G 1 to the right side of this inequality and (2.1), to avoid possibly dividing by zero, but we feel writing it this way makes the connection with G/ G 1 clearer.

We will use the terms upper Lp regular and Lp upper regular interchangeably. The former is used so that we do not end up writing (C,η) Lp upper regular, which looks a bit odd.

Note that the deﬁnition of Lp upper regularity is interesting only for p > 1, since

- (2.1) automatically holds when p = 1 and C = 1. See Appendix C for a more reﬁned deﬁnition, which plays the same role when p = 1.


Previous works on regularity and graph limits for sparse graphs (e.g., [6, 22]) assume a strong hypothesis, namely that |ρG(S,T)| ≤ C G 1 whenever |S|,|T| ≥ η |V (G)|. This is equivalent to what we call (C,η)-upper L∞ regularity, and it is strictly stronger than Lp upper regularity for p < ∞. The relationship between these notions will be come clearer when we discuss the graph limits in a moment. For now, it suﬃces to say that the limit of a sequence of Lp upper regular graphs is a graphon with a ﬁnite Lp norm.

- 2.3. Graphons. In this paper, we deﬁne the term graphon as follows.


- Deﬁnition 2.2. A graphon is a symmetric, integrable function W : [0,1]2 → R.

Here symmetric means W(x,y) = W(y,x) for all x,y ∈ [0,1]. We will use λ to denote Lebesgue measure throughout this paper (on [0,1], [0,1]2, or elsewhere), and measurable will mean Borel measurable.

Note that in other books and papers, such as [8, 9, 25], the word “graphon” sometimes requires the image of W to be in [0,1], and the term kernel is then used to describe more general functions.

We deﬁne the Lp norm on graphons for 1 ≤ p < ∞ by

W p := (E[|W|p])1/p =

[0,1]2

|W(x,y)|p dxdy

1/p

,

and W ∞ is the essential supremum of W.

- Deﬁnition 2.3. An Lp graphon is a graphon W with W p < ∞.


By nesting of norms, an Lq graphon is automatically an Lp graphon for 1 ≤ p ≤

- q ≤ ∞. Note that as part of the deﬁnition, we assumed all graphons are L1. We deﬁne the inner product for graphons by


U,W = E[UW] =

U(x,y)W(x,y)dxdy. H¨lder’s inequality will be very useful:

[0,1]2

| U,W | ≤ U p W p , where 1/p + 1/p = 1 and 1 ≤ p,p ≤ ∞. The special case p = p = 2 is the Cauchy-Schwarz inequality.

Every weighted graph G has an associated graphon WG constructed as follows.

First divide the interval [0,1] into intervals I1,...,I|V (G)| of lengths λ(Ii) = αi/αG for each i ∈ V (G). The function WG is then given the constant value βij on Ii × Ij for all i,j ∈ V (G). Note that WG p = G p for 1 ≤ p ≤ ∞.

### In the theory of dense graph limits, one proceeds by analyzing the associated graphons WG

### for a sequence of graphs Gn, and in particular one is interested in the limit of WG

n

### under the cut metric. However, for sparse graphs, where the density of the graphs tend to zero, the sequence WG

n

converges to an uninteresting limit of zero. In order to have a more interesting theory of sparse graph limits, we consider the normalized associated graphons WG/ G 1 instead.

n

- Deﬁnition 2.4 (Stepping operator). For a graphon W : [0,1]2 → R and a partition P = {J1,...,Jm} of [0,1] into measurable subsets, we deﬁne a step-function WP : [0,1]2 → R by

WP(x,y) :=

1 λ(Ji)λ(Jj) J

i×Jj

W dλ for all (x,y) ∈ Ji × Jj. In other words, WP is produced from W by averaging over each cell Ji × Jj.

A simple yet useful property of the stepping operator is that it is contractive with respect to the cut norm  ·  (deﬁned in the next subsection) and all Lp norms, i.e., WP ≤ W and WP p ≤ W p for all graphon W and 1 ≤ p ≤ ∞.

We can rephrase the deﬁnition of a (C,η)-upper Lp regular graph using the language of graphons. Let V1 ∪ ··· ∪ Vm be a partition of V (G) as in Deﬁnition 2.1, and let P = {J1,...,Jm}, where Ji is the subset of [0,1] corresponding to Vi, i.e., Ji = v∈V

i

Iv, where Iv is as in the deﬁnition of WG. Then (2.1) simply says that (WG)P p ≤ C G 1. This motivates the following notation of Lp upper regularity for graphons.

- Deﬁnition 2.5. We say that a graphon W : [0,1]2 → R is (C,η)-upper Lp regular if whenever P is a partition of [0,1] into measurable sets each having measure at least η,

WP p ≤ C.

Given a weighted graph G, if the normalized associated graphon WG/ G 1 is (C,η)-upper Lp regular and the vertex weights are all at most ηαG, then G must also be (C,η)-upper Lp regular. The converse is not true, as the deﬁnition of upper regularity for graphons involves partitions P of [0,1] that do not necessarily respect the vertex-atomicity of V (G). For example, K3 is a (C,1/2)-upper Lp regular graph for every C > 0 and p > 1 because no valid partition of vertices exist, but the same is not true for the graphon WK

3

/ K3 1.

2.4. Cut metric. The most important metric on the space of graphons is the cut metric. (Strictly speaking, it is merely a pseudometric, since two graphons with cut distance zero between them need not be equal.) It is deﬁned in terms of the cut norm introduced by Frieze and Kannan [18].

- Deﬁnition 2.6 (Cut metric). For a graphon W : [0,1]2 → R, deﬁne the cut norm by


- (2.2) W := sup S,T⊆[0,1] S×T


W(x,y)dxdy ,

where S and T range over measurable subsets of [0,1]. Given two graphons W,W : [0,1]2 → R, deﬁne

d (W,W ) := W − W

and the cut metric (or cut distance) δ by δ (W,W ) := inf

d (Wσ,W ),

σ

where σ ranges over all measure-preserving bijections [0,1] → [0,1] and Wσ(x,y) := W(σ(x),σ(y)).

For a survey covering many properties of the cut metric, see [21]. One convenient reformulation is that it is equivalent to the L∞ → L1 operator norm, which is deﬁned by

W(x,y)f(x)g(y)dxdy ,

W ∞→1 = sup

f ∞, g ∞≤1 [0,1]2

where f and g are functions from [0,1] to R. Speciﬁcally, it is not hard to show that

- (2.3) W ≤ W ∞→1 ≤ 4 W ,


by checking that f and g take on only the values ±1 in the extreme case.

We can extend the d and δ notations to any norm on the space of graphons. In particular, for 1 ≤ p ≤ ∞, we deﬁne

dp(Wσ,W ), with σ ranging overall measure-preserving bijections [0,1] → [0,1] as before.

dp(W,W ) := W − W p and δp(W,W ) := inf

σ

To deﬁne the cut distance between two weighted graphs G and G , we use their associated graphons. If G and G are weighted graphs on the same set of vertices (with the same vertex weights), with edge weights given by βij(G) and βij(G ) respectively, then we deﬁne

d (G,G ) := d (WG,WG ) = max

S,T⊆V (G)

i∈S,j∈T

αiαj αG2

(βst(G) − βst(G )) ,

where WG and WG are constructed using the same partition of [0,1] based on the vertex set. The ﬁnal equality uses the fact that the cut norm for a graphon associated to a weighted graph can always be achieved by S and T in (2.2) that correspond to vertex subsets. This is due to the bilinearity of the expression of inside the absolute value in (2.2) with respect to the fractional contribution of each vertex to the sets S and T.

When G and G have diﬀerent vertex sets, d (G,G ) no longer makes sense, but it still makes sense to deﬁne

δ (G,G ) := δ (WG,WG ). Similarly, for a weighted graph G and a graphon W, deﬁne δ (G,W) := δ (WG,W).

To compare graphs of diﬀerent densities, we can compare the normalized associated graphons, i.e., δ (G/ G 1,G / G 1). We will sometimes refer to this quantity as the normalized cut metric.

## 2.5. Lp upper regular sequences.

- Deﬁnition 2.7. Let 1 < p ≤ ∞ and C > 0. We say that (Gn)n≥0 is a C-upper Lp regular sequence of weighted graphs if for every η > 0 there is some n0 = n0(η) such that Gn is (C + η,η)-upper Lp regular for all n ≥ n0. In other words, Gn is (C + o(1),o(1))-upper Lp regular as n → ∞. An Lp upper regular sequence of graphons is deﬁned similarly.


As an example what kind of graphs this deﬁnition excludes, a sequence of graphs Gn formed by taking a clique on a subset of o(|V (Gn)|) vertices and no other edges is not C-upper Lp regular for any 1 < p ≤ ∞ and C > 0. Furthermore, in Appendix A we show that the average degree in a C-upper Lp regular sequence of simple graphs must tend to inﬁnity.

Now we are ready to state one of the main results of the paper, which asserts the existence of limits for Lp upper regular sequences.

- Theorem 2.8. Let p > 1 and let (Gn)n≥0 be a C-upper Lp regular sequence of weighted graphs. Then there exists an Lp graphon W with W p ≤ C so that

liminf

n→∞

δ

Gn Gn 1

,W = 0.

In other words, some subsequence of Gn/ Gn 1 converges to W in the cut metric. An analogous result holds for Lp upper regular sequences of graphons.

- Theorem 2.9. Let p > 1 and let (Wn)n≥0 be a C-upper Lp regular sequence of graphons. Then there exists an Lp graphon W with W p ≤ C so that


liminf

δ (Wn,W) = 0.

n→∞

These theorems, and all the remaining results in this subsection, are proved in §5. The next proposition says that, conversely, every sequence that converges to an

Lp graphon must be an Lp upper regular sequence.

Proposition 2.10. Let 1 ≤ p ≤ ∞, let W be an Lp graphon, and let (Wn)n≥0 be a sequence of graphons with δ (Wn,W) → 0 as n → ∞. Then (Wn)n≥0 is a

W p-upper Lp regular sequence.

An analogous result about weighted graphs follows as an immediate corollary by setting Wn = WG

/ Gn 1.

n

Corollary 2.11. Let 1 ≤ p ≤ ∞, let W be an Lp graphon, and let (Gn)n≥0 be a sequence of weighted graphs with no dominant nodes and with δ (Gn/ Gn 1 ,W) →

- 0 as n → ∞. Then (Gn)n≥0 is a W p-upper Lp regular sequence.


The two limit results, Theorems 2.8 and 2.9, are proved by ﬁrst developing a regularity lemma showing that one can approximate an Lp upper regular graph(on) by an Lp graphon with respect to cut metric, and then establishing a limit result in the space of Lp graphons. The latter step can be rephrased as a compactness result for Lp graphons, which we state in the next subsection.

We note that a sequence of graphs might not have a limit without the Lp upper regularity assumption. It could go wrong in two ways: (a) a sequence might not have any Cauchy subsequence, and (b) even a Cauchy sequence is not guaranteed to converge to a limit.

Proposition 2.12. (a) There exists a sequence of simple graphs Gn so that

δ (Gn/ Gn 1 ,Gm/ Gm 1) ≥ 1/2 for all n and m with n = m.

(b) There exists a sequence of simple graphs Gn such that (Gn/ Gn 1)n≥0 is a Cauchy sequence with respect to δ but does not converge to any graphon W with

respect to δ .

- 2.6. Compactness of Lp graphons. Lov´asz and Szegedy [27] proved that the space of [0,1]-valued graphons is compact with respect to the cut distance (after identifying graphons with cut distance zero). We extend this result to Lp graphons.

- Theorem 2.13 (Compactness of the Lp ball with respect to cut metric). Let


- 1 < p ≤ ∞ and C > 0, and let (Wn)n≥0 be a sequence of Lp graphons with Wn p ≤ C for all n. Then there exists an Lp graphon W with W p ≤ C so that


liminf

n→∞

δ (Wn,W) = 0.

In other words, BLp(C) := {Lp graphons W : W p ≤ C} is compact with respect to the cut metric δ (after identifying points of distance zero).

For a proof, see §3. The analogous claim for p = 1 is false without additional hypotheses, as Proposition 2.12 implies that the L1 ball of graphons is neither totally bounded nor complete with respect to δ . The example showing that the L1 ball is not totally bounded is easy: the sequence Wn = 22n1[2−n,2−n]×[2−n,2−n] satisﬁes δ (Wn,Wm) > 1/2 for every m = n. Our example showing incompleteness is a bit more involved, and we defer it to the proof of Proposition 2.12(b). See Theorem C.7 for an L1 version of Theorem 2.13 under the hypothesis of uniform integrability.

- 2.7. Sparse W-random graph models. Our main result on this topic is that every graphon W gives rise to a natural random graph model, which produces a sequence of sparse graphs converging to W in the normalized cut metric. When W is nonnegative, the model produces sparse simple graphs. If W is allowed negative values, the resulting random graphs have ±1 edge weights.


We explain this construction in two steps.

- Step 1: From W to a random weighted graph. Given any graphon W, deﬁne H(n,W) to be a random weighted graph on n vertices (labeled by [n] = {1,2,...,n}, with all vertex weights 1) constructed as follows: let x1,...,xn be i.i.d. chosen uniformly in [0,1], and then assign the weight of the edge ij to be W(xi,xj) for all distinct i,j ∈ [n].
- Step 2: From a weighted graph to a sparse random graph. Let H be a weighted graph with V (H) = [n] (with all vertex weights 1) and edge weights βij (with βii = 0), and let ρ > 0. When βij ≥ 0 for all ij, the sparse random simple graph G(H,ρ) is deﬁned by taking V (H) to be the set of vertices and letting ij be an edge with probability min{ρβij,1}, independently for all ij ∈ E(H). If we allow negative edge weights on H, then we take G(H,ρ) to be a random graph with edge weights ±1, where ij is made an edge with probability min{ρ|βij|,1} and given edge weight +1 if βij > 0 and −1 if βij < 0.


Finally, given any graphon W we deﬁne the sparse W-random (weighted) graph to be G(n,W,ρ) := G(H(n,W),ρ).

We also view H(n,W) and G(n,W,ρn) as graphons in the usual way, where the vertices are ordered according to the ordering of x1,...,xn as real numbers and

each vertex is represented by an interval of length 1/n. For example, we use this interpretation in the notation d1(H(n,W),W).

Note that it is also possible to consider other random weighted graph models where the edge weights are chosen from some other distribution (other than ±1). Many of our results generalize easily, but we stick to our model for simplicity.

Here is our main theorem on W-random graphs. Note that we use the same i.i.d. sequence x1,x2,... for constructing H(n,W) and G(n,W,ρn) for diﬀerent values of n, i.e., without resampling the xi’s.

- Theorem 2.14 (Convergence of W-random graphs). Let W be an L1 graphon.


- (a) We have d1(H(n,W),W) → 0 as n → ∞ with probability 1.
- (b) If ρn > 0 satisﬁes ρn → 0 and nρn → ∞ as n → ∞, then


d (ρ−n1G(n,W,ρn),W) → 0 as n → ∞ with probability 1.

Part (a) is proved in §6 and part (b) in §7. Note that we use d1 and d (as opposed to δ1 and δ ) because we have ordered the vertices of the graphs according to the ordering of the sample points x1,...,xn. Of course the sample point ordering is not determined by the graphs alone.

Corollary 2.15. Let W be an L1 graphon with W 1 > 0. Let ρn > 0 satisfy ρn → 0 and nρn → ∞ as n → ∞, and let Gn = G(n,W,ρn). Then

δ (Gn/ Gn 1 ,W/ W 1) → 0 as n → ∞ with probability 1.

Furthermore, for any 1 ≤ p ≤ ∞, if W is an Lp graphon, then H(n,W) p →

W p with probability 1 (this is an immediate consequence of Theorem 6.1 below). Thus H(n,W) generates a sequence of Lp graphons converging to W. Also, by Proposition 2.10 and Theorem 2.14(b), G(n,W,ρn) is a W p-upper Lp regular sequence that converges to W in normalized cut metric.

Note that the sparsity assumption ρn → 0 is necessary since the edges of G(n,W,ρn) are included with probability min{ρn |W(·,·)|,1}, so ρn needs to be arbitrarily close to zero in order to “see” the unbounded part of W. Similarly, the assumption that nρn → ∞ means the expected average degree tends to inﬁnity, which is necessary by Corollary 2.11 and Proposition A.1.

We will prove Theorem 2.14(a) using a theorem of Hoeﬀding on U-statistics, while Theorem 2.14(b) follows from Theorem 2.14(a) via a Chernoﬀ-type argument that shows that if H is a weighted graph with many vertices, then ρ−1G(H,ρ) is close to H in cut metric.

Theorem 2.14 was proved for L∞ graphons as Theorem 4.5 in [8],3 but the proof given there does not seem to extend to Theorem 2.14. The proof here is much shorter than that in [8], though, unlike that proof, our proof gives no quantitative guarantees.

Using sparse W-random graphs, we can fully justify the name W-quasirandom for graphs approximating a graphon W. The following proposition shows that every sequence of sparse simple graphs converging to W is close in cut metric to W-random graphs:

3Technically, Theorem 4.5 in [8] is just a close analogue, since it uses δ instead of d1 and d .

G(H,ρ) sparse random graph §7

Lp upper regular sequence

Lp graphon sequence

densify §4

H(W,n) W-random weighted graph §6

limit§5

limit §3 G(

n,W,ρn)

W

-random sparsegraph§7

Lp graphon limit

Figure 2.1. The relationships between the objects studied in this paper. The arrows are labeled with the relevant sections.

- Proposition 2.16. Let p > 1, and let (Gn)n≥0 be a sequence of simple graphs such that Gn 1 → 0 and δ (Gn/ Gn 1 ,W) → 0, where W is an Lp graphon. Let G n = G(|V (Gn)|,W, Gn 1). Then with probability 1, one can order the vertices of Gn and G n so that

d

Gn Gn 1

,

G n G n 1 → 0. See §7 for the proof, and Proposition C.16 for a generalization to p = 1.

2.8. From upper regular sequences to graphons and back. In Figure 2.1 we summarize the relationship between the objects studied in this paper. The inner set of arrows describe the process of going from a sequence to a limit, while the outer arrows describe the process of starting from a graphon W and constructing a sequence via a W-random graph model. Although we are primarily interested in the diagonal arrows connecting Lp upper regular sequences and Lp graphon limits, the proofs, in both directions, go through Lp graphons as a useful intermediate step.

We have not yet discussed the term densify in Figure 2.1. By densifying we mean approximating (in the sense of cut distance) an Lp upper regular graph by an Lp graphon. The former can be thought of as a sequence of sparse graphs with large edge weights supported on a sparse set of edges (although they do not have to be), and the latter as graphs on a dense set of edges with small weights (in the sense of being Lp bounded). More precisely, we prove the following result, which we think of as a transference theorem in the spirit of Green and Tao [19].

- Proposition 2.17. For every p > 1 and ε > 0 there exists an η > 0 such that for every (C,η)-upper Lp regular weighted graph G (or graphon W), there exists an Lp graphon U with U p ≤ C such that


G G 1

,U ≤ Cε (respectively, δ (W,U) ≤ Cε).

δ

We establish Proposition 2.17 as a weak regularity lemma. In fact, U can be constructed from G by averaging the edge weights over a partition of the vertex set

of G. As with other regularity lemmas, the number of parts used in the partition will be bounded. See §4 for the proof.

The regularity lemma for dense graphs was developed by Szemer´edi [36]. Extensions of Szemere´di’s regularity lemma to sparse graphs were developed independently by Kohayakawa and Ro¨dl [22, 23] under an L∞ upper regularity assumption. Scott [35] gave another proof of a sparse regularity lemma without any assumptions, but as in Szemer´edi’s regularity lemma, it allows for exceptional parts that could potentially hide all the “dense spots.” Frieze and Kannan [18] developed a weak version of regularity lemma with better bounds on the number of parts needed, and it is the version that we extend. This weak regularity lemma was extended to sparse graphs under the L∞ upper regularity assumption in [6] and [12]. In our work, we extend the weak regularity lemma to Lp upper regular graphs.

Our proof of the weak regularity lemma for Lp upper regular graphs is an extension of the usual L2 energy increment argument. However, the extension is not completely straightforward. Due to the nesting of norms, when 1 < p < 2, we do not have very much control over the maximum L2 energy for an Lp upper regular graph. This issue does not arise when p ≥ 2 (e.g., p = ∞ in previous works). We resolve this issue via a careful truncation argument when 1 < p < 2. As it turns out, these truncation arguments can be generalized to the case p = 1, provided we have suﬃcient control over the tails of W; see Appendix C.

- 2.9. Counting lemma for Lp graphons. We have not yet addressed the issue of subgraph counts.4 For simple graphs F and G, a graph homomorphism from F to G is a map V (F) → V (G) that sends every edge of F to an edge of G. Let hom(F,G) be the number of homomorphisms. The homomorphism density, or F-density, is deﬁned by t(F,G) := hom(F,G)/|V (G)||V (F)|, which is equal to the probability that a random map V (F) → V (G) is a homomorphism.


In the theory of dense graph limits, the importance of homomorphism densities is that they characterize convergence under the cut metric: a sequence of dense graphs converges if and only if its F-densities converge for all F, and the limiting F-densities then describe the resulting graphon [8, Theorem 3.8]. This notion of convergence is called left convergence.

The situation is decidedly diﬀerent for sparse graphs, and left convergence is not even implied by cut metric convergence, as we will see below. The irrelevance of left convergence is the most striking diﬀerence between dense and sparse graph limits, and it is an unavoidable consequence of sparsity. By contrast, right convergence (deﬁned by quotients or statistical physics models) remains equivalent to metric convergence, as we show in [7].

4We actually only talk about homomorphism counts in this paper. There is a subtle yet signiﬁcant distinction between homomorphisms and subgraphs, namely that subgraphs arise as homomorphisms for which the map V (F) → V (G) is injective. When G is a large, dense graph and F is ﬁxed, this distinction is not important, since all but a vanishing proportion of maps

- V (F) → V (G) are injective. However, when G is sparse, this distinction could be signiﬁcant (since


the normalization is to divide the subgraph count by G 1 |E(F)| |V (G)||V (F)|). As an example, when ρ = o(n−1/2), we have n4ρ4 = o(n3ρ2), so the main contribution to the number of homomorphisms

from C4 to the random graph G(n, ρ) is no longer coming from 4-cycles, but rather from paths of length 2 (each of which is the image of a homomorphism from C4). However, as it turns out, we will not say much about either homomorphism densities or subgraph counts for sparse graphs anyway (our counting lemmas are for Lp graphons), so let us not dwell on the distinction between subgraphs and homomorphisms.

Before explaining further, we must extend the deﬁnition of homomorphism density to weighted graphs and graphons. For any simple graph F and graphon W, we deﬁne

t(F,W) :=

W(xi,xj)dx1 ...dx|V (F)|.

[0,1]|V (F)| ij∈E(F)

Note that t(F,G) = t(F,WG) for simple graphs G, and we take this as the deﬁnition of t(F,G) for weighted graphs G.

A counting lemma is a claim that any two graphs/graphons that are close in cut metric must have similar F-densities. For dense graphs (or more generally, graphs with uniformly bounded edge weights), this claim is not too hard to show. For example, the following counting lemma appears in [8, Theorem 3.7(a)].

Theorem 2.18 (Counting lemma for L∞ graphons). Let F be a simple graph with m edges. If U and W are graphons with U ∞ ≤ 1, W ∞ ≤ 1, and δ (U,W) ≤ ε, then

|t(F,U) − t(F,W)| ≤ 4mε.

However, for sparse graphs, a general counting lemma of this form is too much to ask for, even for L∞ upper regular graphs. Here is an example illustrating this diﬃculty. Let Gn be an instance of the Erdo˝s-Re´nyi random graph G(n,ρn), where ρn > 0 is the edge probability. If nρn → ∞, then ρ−n3t(K3,Gn) → 1 by a standard second moment argument, e.g., [3, Theorem 4.4.4]. Let G n be obtained from Gn by deleting edges from all triangles in Gn. If we additionally assume ρn = o(n−1/2), so that n3ρ3n = o(n2ρn) and hence only an o(1) fraction of the edges of Gn are deleted, then d (ρ−n1Gn,ρ−n1G n) = o(1). It follows that Gn and G n are close in (normalized) cut distance, but have very diﬀerent (normalized) triangle densities,

- as t(K3,G n) = 0. This example shows that we cannot expect a general counting lemma even for L∞ upper regular sparse graphs, let alone Lp upper regular graphs.


Nevertheless, we will give a counting lemma for Lp graphons (which is the “dense setting,” as opposed to the “sparse setting” of Lp upper regular graphons). There is already an initial diﬃculty, which is that t(F,W) might not be ﬁnite. The next proposition shows the conditions for t(F,W) to be ﬁnite.

Proposition 2.19. Let F be a simple graph with maximum degree ∆. For every p < ∆, there exists an Lp graphon W with t(F,W) = ∞. On the other hand, if W is an L∆ graphon, then t(F,W) is well-deﬁned and ﬁnite. Furthermore,

|t(F,W)| ≤ W |∆E(F)|.

We want a counting lemma which asserts that if U and W are graphons with bounded Lp norms, then |t(F,U) − t(F,W)| is small whenever δ (U,W) is small. Proposition 2.19 suggests we should not expect such a counting lemma to hold when p < ∆. In fact, we give a counting lemma whenever p > ∆ and show that no counting lemma can hold when p ≤ ∆.

We prove the following extension of Theorem 2.18 to Lp graphons. Note that for ﬁxed F and p, the bound in (2.4) is a function of ε that goes to zero as ε → 0. As p → ∞, the bound in Theorem 2.20 converges to that of Theorem 2.18.

Theorem 2.20 (Counting lemma for Lp graphons). Let F be a simple graph with

- m edges and maximum degree ∆. Let ∆ < p < ∞. If U and W are graphons with


U p ≤ 1, W p ≤ 1, and δ (U,W) ≤ ε, then

p−∆ p−∆+m−1

2ε p − ∆

- (2.4) |t(F,U) − t(F,W)| ≤ 2m(m − 1 + p − ∆)


.

The counting lemma implies the following corollary for sequences of graphons that are uniformly bounded in Lp norm. As we saw above, Lp upper regularity would not suﬃce.

Corollary 2.21. Let p > 1 and C > 0, and let Wn be a sequence of graphons converging to W in cut metric. Suppose Wn p ≤ C for all n and W p ≤ C. Then for every simple graph F with maximum degree less than p, we have t(F,Wn) → t(F,W) as n → ∞.

On the other hand, no counting lemma can hold when p ≤ ∆, even if we replace the cut norm by the L1 norm. Proposition 2.22. Let F be a simple graph with maximum degree ∆ ≥ 2, and let

- 1 ≤ p ≤ ∆. Then there exists a sequence (Wn)n≥0 of graphons with Wn p ≤ 4 such that Wn − 1 1 → 0 as n → ∞ yet


t(F,Wn) = 2|{v∈V (G) : degF(v)=∆}| > 1 = t(F,1). See §8 for proofs of these results.

lim

n→∞

3. Lp graphons Recall that an Lp graphon is a symmetric and integrable function W : [0,1]2 → R

with W p < ∞. In this section, we prove Theorem 2.13, which gives a limit theorem for Lp graphons. The results in this section form the (Lp graphon sequence) → (Lp graphon limit) arrow in Figure 2.1.

The proof technique is an extension of that of [27]. We will need a weak regularity lemma for Lp graphons. The standard proof of the weak regularity lemma involving L2 energy increments, based on ideas from §8 of [18], works for L2 graphons and hence Lp graphons for p ≥ 2. Since several of our proofs are based on the same basic idea, we include the proof here. When 1 < p < 2, we use a truncation argument to reduce to the p = 2 case.

- Lemma 3.1 (Weak regularity lemma for L2 graphons). Let ε > 0, let W : [0,1]2 →


- R be an L2 graphon, and let P be a partition of [0,1]. Then there exists a partition


2

Q reﬁning P into at most 41/ε

|P| parts so that W − WQ ≤ ε W 2 .

Proof. We build a sequence P0,P1,P2,... of partitions of [0,1], starting with P0 = P. For each i ≥ 0, the partition Pi+1 reﬁnes Pi by dividing each part of Pi into at most four subparts. So in particular |Pi| ≤ 4i |P0|.

i ≤ ε W 2, then we stop. Otherwise, by the deﬁnition of the cut norm, there exists measurable subsets S,T ⊆ [0,1] with

These partitions are constructed as follows. If for some i, Pi satisﬁes W − WP

| W − WP

### ,1S×T | > ε W 2 .

i

Let Pi+1 be the common reﬁnement of Pi with S and T. Since S and T are both unions of parts in Pi+1,

### ,1S×T = | W − WP

,1S×T | > ε W 2 .

i+1 − WP

WP

i

i

Since Pi+1 is a reﬁnement of Pi, WP

i+1 − WP

= 0. So by the Pythagorean theorem, followed by the Cauchy-Schwarz inequality,

### ,WP

i

i

WP

i+1

### 2 2 − WP

i

2 2 = WP

i+1 − WP

i

2 2 ≥ WP

,1S×T 2 > ε2 W 22 .

i+1 − WP

i

i 2 ≤ W 2 (by the convexity of x  → x2), we see that the process must stop with i ≤ 1/ε2. The ﬁnal Pi is the desired Q.

Since WP

An equipartition of [0,1] is a partition where all parts have equal measure. It will be convenient to enforce that the partitions obtained from the regularity lemma are equipartitions. The following lemma is similar to [25, Lemma 9.15(b)].

- Lemma 3.2 (Equitizing a partition). Let p > 1 and ε > 0, and let k be any positive integer. Let W be an Lp graphon, let P be an equipartition of [0,1], and let Q be a partition reﬁning P. Then there exists an equipartition Q reﬁning P into exactly k |P| parts so that


W − WQ ≤ 2 W − WQ + 2 W p

2|Q| k |P|

1−1/p

.

Proof. For Q we choose any equipartition reﬁning P into exactly k |P| parts, at most |Q| of which intersect more than one part of Q. We can construct such a Q as follows. For each part Pi of P, let Qi1,...,Qim be the parts of Q contained in Pi. Form Q by dividing up each of Qi1,...,Qim into parts of measure exactly 1/(k |P|) plus a remainder part; then group the remainder parts in Pi together and divide

- them into parts of measure 1/(k |P|). This partitions Pi into k parts of equal size. At most m of these new parts intersect more than one part of Q, because there were


- at most m remainder parts, each of size less than 1/(k |P|). Now carrying out this procedure for each part of P gives an equipartition Q with the desired property.


Let R be the common reﬁnement of Q and Q . Because the stepping operator is contractive with respect to the cut norm (i.e., UR ≤ U ),

W − WQ ≤ W − WQ + WQ − WR + WR − WQ

= W − WQ + (WQ − W)R + WR − WQ ≤ 2 W − WQ + WR − WQ .

Thus, it will suﬃce to bound WR − WQ by 2 W p (2|Q|/(k |P|))1−1/p.

Let S be the union of the parts of Q that were broken up in its reﬁnement R. These are exactly the parts that intersect more than one part of Q, so λ(S) ≤ |Q|/(k |P|). Using the agreement of WQ with WR on Sc×Sc (where Sc := [0,1]\S), Ho¨lder’s inequality with 1/p + 1/p = 1, the bound WR p ≤ WQ p ≤ W p, and

the triangle inequality, we get WR − WQ ≤ WR − WQ 1

= (WR − WQ )(1 − 1Sc×Sc) 1 ≤ WR − WQ p 1 − 1Sc×Sc p = WR − WQ p 2λ(S) − λ(S)2 1−1/p

≤ 2 W p 2λ(S) 1−1/p

1−1/p

2|Q| k |P|

≤ 2 W p

,

- as desired.


The following lemma is the L2 version of Corollary 3.4(i) in [8], which in fact never required the L∞ hypothesis implicitly assumed there.

- Lemma 3.3 (Weak regularity lemma for L2 graphons, equitable version). Let 0 < ε < 1/3 and let W : [0,1]2 → R be an L2 graphon. Let P be an equipartition of

[0,1]. Then for every integer k ≥ 410/ε

2

there exists an equipartition Q reﬁning P into exactly k |P| parts so that

- (3.1) W − WQ ≤ ε W 2 .


Proof. Apply Lemma 3.1 to obtain a reﬁnement Q of P into at most 49/ε

2

|P| parts

so that W − WQ ≤ 13ε W 2. Now apply Lemma 3.2 with p = 2 to obtain a reﬁnement Q of P into an equipartition of exactly k |P| parts satisfying

W − WQ ≤ 2 W − WQ +2 W 2

2|Q| k |P|

≤ 2·

ε 3

W 2+2 W 2·

ε 6 ≤ ε W 2 .

Here we used |Q|/|P| ≤ 49/ε

2

≤ ε

2

72410/ε

2

≤ 12(6ε)2k, which holds for 0 < ε < 1/3. So Q is the desired partition.

Lemma 3.3 also works for Lp graphons for all p ≥ 2 by nesting of norms, as (3.1) implies W − WQ ≤ ε W p. Now we deal with the case 1 < p < 2.

- Lemma 3.4 (Weak regularity lemma for Lp graphons). Let 1 < p < 2 and 0 < ε < 1. Let W : [0,1]2 → R be an Lp graphon. Let P be an equipartition of [0,1]. Then for


p/(p−1)

any integer k ≥ 410(3/ε)

there exists an equipartition Q reﬁning P into exactly k |P| parts so that

W − WQ ≤ ε W p . Note that as p 2, the exponent p/(p − 1) of 1/ε in k in the lemma tends to

- 2, which is the best possible exponent in the bound for the weak regularity lemma when p ≥ 2 by [13].


Proof. Set K = (3/ε)1/(p−1) W p, and let W = W1|W|≤K.

We have

W 2 = W1|W|≤K 2 ≤ W(K/|W|)1−p/2

2

2−p

= W p/p 2 K1−p/2 = (3/ε)

2(p−1) W p . By Lemma 3.3 there exists an equitable partition Q reﬁning P into exactly k |P| parts so that

p 2(p−1)

ε 3

ε 3

W − W Q ≤

W 2 ≤

W p . We also have

WQ − W Q 1 = (W − W )Q 1 ≤ W − W 1 = W1|W|>K 1 ≤ W(|W|/K)p−1 1 = W pp /Kp−1 =

ε 3

W p . It follows that

W − WQ ≤ W − W + W − W Q + W Q − WQ ≤ W − W 1 + W − W Q + W Q − WQ 1 ≤

ε 3

ε 3

ε 3

W p = ε W p . Therefore Q is the desired partition.

W p +

W p +

Now we prove that the Lp ball is compact with respect to the cut metric.

Proof of Theorem 2.13. The proof of the theorem is a small modiﬁcation of the argument in [27, Theorem 5.1], with adaptations to the Lp setting. We begin by using the weak regularity lemmas to produce approximations to the sequence (Wn)n≥0. The approximations using a ﬁxed number of parts are easier to analyze than the original sequence, because they involve only a ﬁnite amount of information. We take limits of these approximations and show that they form a martingale as one varies the number of parts. The limit of the original sequence is then derived using the martingale convergence theorem.

By scaling we may assume without loss of generality that C = 1. For each k and

- n we construct an equipartition Pn,k using Lemma 3.3 (when p ≥ 2) or Lemma 3.4 (when 1 < p < 2), so that


Wn − (Wn)P

n,k ≤ 1/k.

In doing so, we may assume that Pn,k+1 always reﬁnes Pn,k and that |Pn,k| is independent of n.

The ﬁrst step is to change variables so the partitions Pn,k become the same. Let Pk be a partition of [0,1] into |Pn,k| intervals of equal length, and for each n and k,

let σn,k be a measure-preserving bijection from [0,1] to itself that transforms Pn,k into Pk. (This can always be done; see, for example, Theorem A.7 in [21].) Now let

σn,k. Then Wn,k is a step-function with interval steps formed from Pk, and δ (Wn,Wn,k) ≤ 1/k.

Wn,k = Wnσn,k P

### = (Wn)P

n,k

k

Since each interval of Pk has length exactly 1/|Pk| and the stepping operator is contractive with respect to the p-norm,

|Pk|−2 Wn,k p∞ ≤ Wn,k pp ≤ Wn pp ≤ 1. Thus Wn,k ∞ ≤ |Pk|2/p.

We next pass to a subsequence of (Wn)n≥0 such that for each k, Wn,k converges to a limit Uk almost everywhere as n → ∞. For each ﬁxed k, this is easily done using compactness of a |Pk|2-dimensional cube, because the function Wn,k is determined by |Pk|2 values corresponding to pairs of parts in Pk and Wn,k ∞ is uniformly bounded. To ﬁnd a single subsequence that ensures convergence for all k, we iteratively choose a subsequence for k = 1,2,....

For each k, the limit Uk is a step function with |Pk| steps such that Wn,k − Uk p → 0 as n → ∞. In particular, this implies that Uk p ≤ 1 for all k, since Wn,k p ≤

Wn p ≤ 1 for all n and k.

The crucial property of the sequence U1,U2,... is that it forms a martingale on [0,1]2 with respect to the σ-algebras generated by the products of the parts of P1,P2,.... In other words, (Uk+1)P

### = Uk. This follows immediately from (Wn,k+1)P

k

σn,k+1 = Wn,k.

= Wnσn,k+1 P

### = (Wn)P

k

n,k

k

(Note that σn,k+1 transforms Pn,k into Pk because it does the same for their reﬁnements Pn,k+1 and Pk+1.)

By the Lp martingale convergence theorem [16, Theorem 5.4.5], there exists some

- W ∈ Lp([0,1]2) such that Uk − W p → 0 as k → ∞. Since Uk p ≤ 1 for all k, we


have W p ≤ 1. Now W is the desired limit, because

δ (Wn,W) ≤ δ (Wn,Wn,k) + δ (Wn,k,Uk) + δ (Uk,W) ≤ δ (Wn,Wn,k) + Wn,k − Uk 1 + Uk − W 1 . Each of the terms in this bound can be made arbitrarily small by choosing k and

- then n large enough. Thus, δ (Wn,W) → 0 as n → ∞, as desired (keeping in mind that we have passed to a subsequence).


4. Regularity lemma for Lp upper regular graph(on)s

In this section we prove a regularity lemma for Lp upper regular graphs and graphons. This forms the (Lp upper regular sequence) → (Lp graphon sequence) arrow in Figure 2.1. We will ﬁrst present the proof for graphons, since the notation is somewhat simpler. Then we will explain the minor modiﬁcations needed to prove the result for weighted graphs. The diﬀerence between the two settings is that for graphs, the partitions of [0,1] in the corresponding graphon need to respect the atomicity of the vertices, but this is only a minor inconvenience since the Lp upper regularity condition ensures that no vertex has weight too large.

The main ideas of the proof are as follows. Suppose W is a (C,η)-upper Lp regular graphon with p ≥ 2. We would like to proceed as in the proof of the L2 weak regularity lemma, by constructing partitions P0,P1,... such that if W − WP

> Cε, then

i

### 2 2 ≥ WP

### 2 2 + (Cε)2.

WP

i+1

i

Furthermore, we would like all the parts of Pi to have measure at least η, so that WP

i p ≤ C. These bounds cannot both hold for all i, so we must eventually have W − WP

i 2 ≤ WP

i ≤ Cε for some i. When we try to do this, we run into two problems:

- (1) While W − WP

i

> Cε gives sets S and T such that | W − WP

i

,1S×T | > Cε, the partition generated by Pi, S, and T may have a part of size less than η. In that case, we cannot use the upper regularity assumption as we proceed.

- (2) When p < 2, the L2 increment argument does not work, since we only have


bounds on WP

i p, not WP

i 2.

To deal with the ﬁrst problem, we will modify S and T to S and T such that the new partition has large enough parts, while | W − WP

,1S ×T  | > Cε/2. To do so, we will need a technical lemma, Lemma 4.2 below, which allows us to bound the diﬀerence between these inner products, and which itself follows from a simpler lemma, Lemma 4.1. After stating and proving these lemmas, we will formulate Theorem 4.3, which is the regularity lemma version of Proposition 2.17 for graphons. In its proof, we deal with the ﬁrst problem as describe above, while we deal with the second by a suitable truncation argument.

i

We begin with a lemma that bounds the weight of W on 1S×T when one of S and T is small. Recall that λ denotes Lebesgue measure.

- Lemma 4.1. Assume η < 1/9. Let W : [0,1]2 → R be a (C,η)-upper Lp regular graphon, and let S,T ⊆ [0,1] be measurable subsets. If λ(S) ≤ δ for some δ ≥ η, then


| W,1S×T | ≤ 10Cδ1−1/p. Proof. We prove the lemma in three steps.

- Step 1. Let P be the smallest partition of [0,1] that simultaneously reﬁnes S and

T (i.e., the parts are S ∩ T,Sc ∩ T,S ∩ Tc,Sc ∩ Tc, excluding empty parts, where Sc := [0,1]\S). If all parts of P have measure at least η, then we can apply Ho¨lder’s inequality (with 1/p + 1/p = 1) and the (C,η)-upper Lp regularity hypothesis to conclude

| W,1S×T | = | WP,1S×T | ≤ WP p 1S×T p ≤ C(λ(S)λ(T))1−1/p.

- Step 2. In this step we assume that 3η ≤ λ(T) ≤ 1 − 3η. The partition P


generated by S and T as in Step 1 might not satisfy the condition of all parts having measure at least η. Deﬁne S1 ⊆ T and S2 ⊆ Tc as follows.

If λ(S ∩ T) < η, then let S1 be an arbitrary subset of T \ S with λ(S1) = η; else, if λ(Sc ∩ T) < η (equivalently, λ(S ∩ T) > λ(T) − η), then let S1 be an arbitrary subset of S ∩ T with λ(S1) = η; else, let S1 = ∅.

Similarly, if λ(S ∩ Tc) < η, then let S2 be an arbitrary subset of Tc \ S with λ(S2) = η; else, if λ(S ∩ Tc) > λ(Tc) − η, then let S2 be an arbitrary subset of

- S ∩ Tc with λ(S2) = η; else, let S2 = ∅. Let S = S S1 S2 (where denotes the symmetric diﬀerence, and here each


Si is either contained in S or disjoint from S). Note that the pairs (S1,T), (S2,T),

(S ,T) all satisfy the hypotheses of Step 1. So we have | W,1S×T | = | W,1S ×T ± 1S

2×T | ≤ | W,1S ×T | + | W,1S

1×T ± 1S

2×T | ≤ C(λ(S )λ(T))1−1/p + C(λ(S1)λ(T))1−1/p + C(λ(S2)λ(T))1−1/p ≤ C(λ(S) + 2η)1−1/p + 2Cη1−1/p ≤ 5Cδ1−1/p.

1×T | + | W,1S

The last step follows from the assumption λ(S) ≤ δ and δ ≥ η.

Step 3. Now we relax the 3η ≤ λ(T) ≤ 1 − 3η assumption. If λ(T) < 3η, then let T1 be any subset of Tc with λ(T1) = 3η; else, if λ(T) > 1 − 3η, then let T1 be any subset of T with λ(T1) = 3η; else, let T1 = ∅. Let T = T T1. Then 3η ≤ λ(T ) ≤ 1 − 3η. So applying Step 2, we have

1 | ≤ 10Cδ1−1/p.

| W,1S×T | ≤ | W,1S×T  | + | W,1S×T

- Lemma 4.2. Assume η < 1/9. Let W : [0,1]2 → R be a (C,η)-upper Lp regular graphon. Let S,S ,T,T ⊆ [0,1] be measurable sets satisfying λ(S S ),λ(T T ) ≤ δ, for some δ ≥ η. Then


| W,1S×T − 1S ×T  | ≤ 40Cδ1−1/p. Proof. We have

1S×T − 1S ×T = 1(S\S )×T + 1(S∩S )×(T\T ) − 1(S \S)×T − 1(S∩S )×(T \T). Applying Lemma 4.1 to each of the four terms below and using λ(S \ S ),λ(S \ S),λ(T \ T ),λ(T \ T) ≤ δ, we have

| W,1S×T − 1S ×T  | ≤ W,1(S\S )×T + W,1(S∩S )×(T\T )

+ W,1(S \S)×T + W,1(S∩S )×(T \T) ≤ 4 · 10Cδ1−1/p.

Theorem 4.3 (Weak regularity lemma for Lp upper regular graphons). Let C > 0, p > 1, and 0 < ε < 1. Set N = (6/ε)max{2,p/(p−1)} and η = 4−N−1(ε/160)p/(p−1). Let W : [0,1]2 → R be a (C,η)-upper Lp regular graphon. Then there exists a partition P of [0,1] into at most 4N measurable parts, each having measure at least η, so that

W − WP ≤ Cε. Proposition 2.17 for graphons follows as an immediate corollary.

Proof. We consider a sequence of partitions P0,P1,P2,...,Pn of [0,1], starting with the trivial partition P0 = {[0,1]}. The following properties will be maintained:

- (1) The partition Pi+1 reﬁnes Pi by dividing each part of Pi into at most four subparts. So in particular |Pi| ≤ 4i.
- (2) For each i, all parts of Pi have measure at least η.


These partitions are constructed as follows. For each 0 ≤ i < n, if Pi satisﬁes W − WP

i ≤ Cε, then we have found the desired partition. Otherwise, there exists measurable subsets S,T ⊆ [0,1] with

- (4.1) | W − WP


### ,1S×T | > Cε.

i

Next we ﬁnd S ,T so that λ(S S ),λ(T T ) ≤ 2|Pi|η, such that if we deﬁne Pi+1 to be the common reﬁnement of P, S , and T , then all parts of Pi have size

- at least η. Indeed, look at the intersection of S with each part of Pi, and obtain S from S by deleting (rounding down) the parts that intersect with S in measure less than η, and then adding (rounding up) the parts that intersect Sc in measure less than η. Let Pi+1/2 be the common reﬁnement of Pi and S , so that all parts of Pi+1/2 have measure at least η, and λ(S S ) ≤ |Pi|η. Next, do a similar procedure


- to T to obtain T so that the common reﬁnement Pi+1 of Pi+1/2 and T has all parts with measure at least η. Here we have λ(T T ) ≤ Pi+1/2 η ≤ 2|Pi|η. So Pi+1 has the desired properties.


If the construction of the sequence P0,...,Pn of partitions stops with n ≤ N, then we are done. Otherwise let us stop the sequence at Pn with n = N . We will derive a contradiction.

Let 0 ≤ i < n, and let S,S ,T,T be the sets used to construct Pi+1 from Pi. Using λ(S S ),λ(T T ) ≤ 2|Pi|η ≤ 2 · 4Nη, we have by Lemma 4.2

- (4.2) | W,1S×T − 1S ×T  | ≤ 40C(2 · 4Nη)1−1/p ≤ Cε/4. Also by H¨lder’s inequality (with 1/p + 1/p = 1),

| WP

i

,1S×T − 1S ×T  | ≤ WP

i p 1S×T − 1S ×T p ≤ C(λ(S S ) + λ(T T ))1/p ≤ C(4 · 4Nη)1−1/p ≤ Cε/160 ≤ Cε/8.

- (4.3)

It follows that | W − WP

i

,1S×T − W − WP

i

,1S ×T  | ≤ | W,1S×T − 1S ×T  |

+ | WP

i

,1S×T − 1S ×T  | ≤ Cε/2.

Combing the above inequality with (4.1) gives us | W − WP

i

,1S ×T  | > Cε/2. Since S and T are both unions of parts in Pi+1, we have W,1S ×T = WP

i+1

,1S ×T , so

- (4.4) WP


i+1 − WP

,1S ×T > Cε/2. We consider two cases: p ≥ 2 and 1 < p < 2.

i

- Case I: p ≥ 2. This case is easier. Since Pi+1 is a reﬁnement of Pi, we have

WP

i+1 − WP

i

,WP

i

= 0. So by the Pythagorean theorem, followed by the CauchySchwarz inequality,

WP

i+1

2 2 − WP

i

2 2 = WP

i+1 − WP

i

2 2 ≥ | W − WP

i

,1S ×T  |2 > C2ε2/4. So WP

n

2 2 > nC2ε2/4 ≥ NC2ε2/4 > C2, which contradicts WP

n 2 ≤ WP

n p ≤ C.

- Case II: 1 < p < 2. In this case, we no longer have an upper bound on WP


n 2

### as before. We proceed by truncation: we stop the partition reﬁnement process at step n, truncate the last step function, and then look back to calculate the energy

increment that would have come from doing the same partition reﬁnement on the truncated graphon. Set

K := C(6/ε)1/(p−1), and deﬁne the truncation

Pn|≤K. We claim that for 0 ≤ i < n,

U := WP

1|W

n

- (4.5) UP

i+1

2 2 > UP

i

2 2 + (Cε/6)2.

Then one has UP

n

2 2 > n(Cε/6)2 ≥ N(Cε/6)2 = C2(6/ε)(2−p)/(p−1), which contra-

dicts UP

n

2 2 = WP

n

1|W

Pn|≤K

2 2 ≤ WP

n

(K/|WP

n|)1−p/2

2 2

= WP

n

p p K2−p ≤ CpK2−p = C2(6/ε)(2−p)/(p−1).

It remains to prove (4.5). We have WP

n − U 1 = WP

n

1|W

Pn|>K 1 ≤ WP

n

(|WP

n|/K)p−1 1

=  |WP

n|p 1 /Kp−1 = WP

n

p p/Kp−1

≤ Cp/Kp−1 = Cε/6. Since Pn is a reﬁnement of Pi, we have (WP

n

)P

i

= WP

i

. So

- (4.6) WP


n − U 1 ≤ Cε/6. Similarly, WP

i − UP

n − U)P

i 1 ≤ WP

i 1 = (WP

i+1 1 ≤ Cε/6. Using the triangle inequality, (4.4), and (4.6), we ﬁnd that

i+1 − UP

i+1 − WP

,1S ×T ≥ WP

i+1 − UP

,1S ×T − WP

UP

i

i

i − UP

i 1 − WP

i+1 − UP

i+1 1

> C(ε/2 − ε/6 − ε/6) = Cε/6. Since Pi+1 is a reﬁnement of Pi, we have UP

i+1 − UP

= 0. So by the Pythagorean theorem, followed by the Cauchy-Schwarz inequality, we have

### ,UP

i

i

### 2 2 − UP

,1S ×T 2 > (Cε/6)2, which proves (4.5), as desired.

2 2 ≥ UP

2 2 = UP

i+1 − UP

i+1 − UP

UP

i+1

i

i

i

This completes the proof of the weak regularity lemma for Lp upper regular graphons.

Remark 4.4. At the cost of slightly worse constants, the statement of Theorem 4.3 can be strengthened to provide an equipartition. To this end, we ﬁrst apply the theorem to W, obtaining a partition P0 into at most 4N parts such that each part has size at least η and W − WP

0 ≤ Cε. Since W is assumed to be Lp upper regular, we obtain a graphon U = WP

such that U p ≤ C. Depending on whether p ≥ 2 or p ∈ (1,2), we then apply Lemma 3.3 or Lemma 3.4 to U and the trivial partition of [0,1] consisting of the single class [0,1]. As a consequence, for k ≥ 4max{10/ε

0

2,10(3/ε)p/(p−1)} we can ﬁnd an equipartition P of [0,1] into k parts such

0 − UP = U − UP ≤ Cε. With the help of the triangle inequality, this implies

that WP

W − UP ≤ 2Cε.

But UP is a step functions with steps in P, and it should approximate W at most as well as WP. While this is not quite true, it is true at the cost of another factor of two. To see this, we use the triangle inequality, UP = (UP)P, and the fact that the stepping operator is a contraction with respect to the cut norm to bound

W − WP ≤ W − UP + WP − UP

= W − UP + (W − UP)P ≤ W − UP + W − UP

= 2 W − UP . Putting everything together, we see that for any k ≥ 4max{10/ε

2,10(3/ε)p/(p−1)} we can ﬁnd an equipartition P of [0,1] into exactly k parts such that

W − WP ≤ 4Cε,

provided W is (C,η)-upper Lp regular with η = 4−N−1(ε/160)p/(p−1), where N = (6/ε)max{2,p/(p−1)}.

Next we state the analogue of Theorem 4.3 for weighted graphs and explain how to modify the above proof to work for weighted graphs.

If G is a weighted graph, and P = {V1,...,Vm} is a partition of V (G), then we denote by GP the weighted graph on V (G) (with the same vertex weights as G) and edge weights as follows. For s ∈ Vi,t ∈ Vj the edge between s and t is given weight

αxαy αV

βst(GP) =

βxy(G)

### αV

i

j

x∈Vi,y∈Vj

(note that we allow x = y). In other words, GP is obtained from G by averaging the edge weights inside each Vi × Vj. In terms of graphons, we have WGP = (WG)P, where we abuse notation by letting P also denote the partition of [0,1] corresponding to the vertex partition.

Theorem 4.5 (Weak regularity lemma for Lp upper regular graphs). Let C > 0,

- p > 1, and 0 < ε < 1. Set N = (6/ε)max{2,p/(p−1)} and η = 4−N−1(ε/320)p/(p−1). Let G = (V,E) be a (C,η)-upper Lp regular weighted graph. Then there exists a partition P of V into at most 4N parts, each having weight at least ηαG, so that


G G 1

GP G 1 ≤ Cε.

d

,

Let us explain how one can modify the proofs in this section to prove Theorem 4.5. The only diﬀerence is that in the proceeding proofs, instead of taking arbitrary measurable sets, we are only allowed to take subsets of [0,1] corresponding to subsets of vertices. Another way to view this is that we are working with a diﬀerent σ-algebra on [0,1], where the new σ-algebra comes from a partition of [0,1] into parts with measure equal to the vertex weights (as a fraction of the total vertex weights) of G. So previously in certain steps of the argument in Lemma 4.1 where we took an arbitrary subset S1 a certain speciﬁed measure (say λ(S1) = η), we have to be content with just having λ(S1) ∈ [η,2η). This can be done since the

(C,η)-upper Lp regularity assumption implies no vertex occupies measure greater than η times the total vertex weight.

With this modiﬁcation in place, Lemma 4.1 then becomes the following.

- Lemma 4.6. Assume η < 1/13. Let G be a (C,η)-upper Lp regular weighted graph


with vertex weights αi and edge weights βij. Let S,T ⊆ V (G). If αS ≤ δαG for some δ ≥ η, then

βst ≤ 20δ1−1/p

|βij|.

s∈S,t∈T

i,j∈V (G)

The conclusion of Lemma 4.2 must be changed similarly, with the bound increased by a factor of 2. To prove Theorem 4.5 we can modify the proof of Theorem 4.3 to allow only subsets of vertices instead of arbitrary measurable sets.

Remark 4.7. As in Remark 4.4, we can achieve an equipartition in Theorem 4.5 at the cost of worse constants. Of course the indivisibility of vertices means we cannot always achieve an exact equipartition. Instead, by an equipartition of a graph G we mean a partition of V (G) into k parts P1,...,Pk such that for each i,

αG k

i −

αP

< max

αj.

j∈V (G)

The argument is the same as in Remark 4.4, except that we must use an equitable weak Lp regularity lemma for graphs, while Lemmas 3.3 and 3.4 were stated for graphons. For p ≥ 2, Corollary 3.4(ii) in [8] supplies what we need, and exactly the same truncation argument used to derive Lemma 3.4 from Lemma 3.3 extends this argument to p < 2. The only diﬀerence is that the bound on η is now inherited from Theorem 4.5 instead of Theorem 4.3. We conclude that for k ≥ 4max{10/ε

2,10(3/ε)p/(p−1)}, we can ﬁnd an equipartition P of V (G) into exactly k parts such that

G G 1

GP G 1 ≤ 4Cε,

d

,

provided G is (C,η)-upper Lp regular with η = 4−N−1(ε/320)p/(p−1), where N = (6/ε)max{2,p/(p−1)}.

5. Limit of an Lp upper regular sequence

Putting together the results in the last two sections, we obtain the limit for an Lp upper regular sequence, thereby completing the (Lp upper regular sequence) → (Lp graphon limit) arrow in Figure 2.1.

Proof of Theorems 2.8 and 2.9. We give the proof of Theorem 2.9 (for graphons). The proof of Theorem 2.8 (for weighted graphs) is nearly identical (using Theorem 4.5 instead of Theorem 4.3).

Let Wn be a upper Lp regular sequence of graphons. In other words, there exists a sequence ηn → 0 so that Wn is (C+ηn,ηn)-upper Lp regular. Applying Theorem 4.3, we can ﬁnd a sequence εn → 0 so that for each n, there exists a partition Pn of [0,1] for which each part has measure at least ηn and Wn − (Wn)P

n ≤ εn. We have (Wn)P

n p ≤ C + ηn due to Lp upper regularity. By Theorem 2.13, there exists an Lp graphon W so that W p ≤ C and δ ((Wn)P

### ,W) → 0 along some subsequence. Since εn → 0, δ (Wn,W) → 0 along this subsequence.

n

The converse, Proposition 2.10, follows as an corollary of the following lemma.

(Note that an Lp graphon W is automatically ( W p ,η)-upper Lp regular for every η ≥ 0.)

- Lemma 5.1. Let C > 0, η > 0, and 1 ≤ p ≤ ∞, and let W : [0,1]2 → R be a (C,η)-upper Lp regular graphon. Let U : [0,1]2 → R be another graphon. If


W − U ≤ η3, then U is (C + η,η)-upper Lp regular.

Proof. For any subsets S,T ⊆ [0,1], we have | W − U,1S×T | ≤ W − U ≤ η3. It follows that

η3 λ(S)λ(T) ≤ η,

1 λ(S)λ(T) S×T

U dλ ≤

W dλ −

S×T

provided λ(S),λ(T) ≥ η. So for any partition P of [0,1] into sets each having measure at least η we have |UP − WP| ≤ η pointwise. Therefore,

UP p ≤  |WP| + η p ≤ WP p + η p ≤ C + η. It follows that U is (C + η,η)-upper Lp regular.

Next we prove Proposition 2.12, which shows that without the Lp upper regularity assumption, a sequence of a graphs might not have a Cauchy subsequence (with respect to δ ). Furthermore, even a Cauchy sequence might not have a limit in the form of a graphon.

Proof of Proposition 2.12. (a) For each n ≥ 2, let Gn be a graph on n2n vertices consisting of a single clique on n vertices. Then Gn 1 = 2−2n(n − 1)/n. Let Wn = WG

/ Gn 1, where the support of Wn is contained in [0,2−n]2. We claim that δ (Wm,Wn) ≥ 1/2 for any m = n. Indeed, for any measure-preserving bijection σ: [0,1] → [0,1],

n

Wm − Wnσ ≥ Wm − Wnσ,1[0,2−m]2 ≥ 1 − 2−2m Wn ∞

= 1 − 2−2(m−n)n/(n − 1) ≥ 1/2 for m > n.

(b) Our proof is inspired by a classic example of an L1 martingale that converges almost surely but not in L1: a martingale that starts at 1 and then at each step either doubles or becomes zero. The analogue of this classic example will be a Cauchy sequence of graphs Gn whose normalized graphons converge to zero pointwise almost everywhere but not in cut distance. We will build this sequence inductively so that Gn+1 is formed from Gn by replacing every edge of Gn with a quasi-random bipartite graph.

More precisely, for every n, let εn = 4−n, and ﬁx a simple graph Hn with δ (Hn,1[0,1]2/2) ≤ εn. Let G1 be the graph with one edge on two vertices. Set Gn+1 := Gn × Hn. In other words, to obtain Gn+1 from Gn, replace every vertex v of Gn by k = |V (Hn)| copies v1,...,vk. The edges of Gn+1 consists of uivj where uv is an edge of Gn and ij is an edge of Hn.

Now we show that (Gn)n≥0 is a Cauchy sequence with respect to the normalized cut metric. First, using the natural overlay between WG

### and WG

### (the intervals

n

n+1

n)| corresponding to the vertices of Gn are each partitioned into |Hn| parts corresponding to the vertices of Gn+1), we see that

I1,...,I|V (G

- 1

- 2


- 1

- 2


- 1

- 2


### ≤ WH

Gn ≤ WG

WG

−

−

1[0,1]2 ≤ εn, since any WG

δ Gn+1,

n

n+1

n

### − WG

/2,1A×B is equal to the sum of the contributions from each of the |V (Gn)|2 cells Ii × Ij, and the contribution from each cell is bounded by

n+1

n

− 1[0,1]2/2 /|V (Gn)|2. Note that Gn+1 1 / Gn 1 ∈ [1/2 − εn,1/2 + εn]. It follows that

WH

n

Gn+1 1 Gn 1

Gn+1 Gn+1 1

Gn Gn 1

1 Gn+1 1

δ

,

=

δ Gn+1,

Gn

- 1

- 2


≤ 3n+1 δ Gn+1,

Gn + εn ≤ 3n+1 · 2εn = 6 · (3/4)n.

Thus the graphs Gn/ Gn 1 form a Cauchy sequence with respect to δ .

Next we show that Gn/ Gn 1 does not converge to any graphon with respect to δ . Let Wn = WG

/ Gn 1 (properly aligned, so that the support of Wn+1 is contained in the support of Wn). Then Wn converges to zero pointwise almost everywhere, but zero cannot be the δ -limit of the sequence since EWn = 1 for all n. Indeed, as we will see shortly, there can be no U such that δ (Wn,U) → 0. Assume by contradiction that there is such a graphon. Since Wn is non-negative,

n

U,1A×B ≥ 0 for every A,B ⊆ [0,1], implying that U is nonnegative as well. Furthermore EU = 1, since EWn = 1 and |EWn − EU| ≤ δ (U,Wn) (note that EU = EUσ for every measure-preserving bijection σ). We will show that U has the following property: for every ε > 0, there exists a subset S ⊆ [0,1]2 with λ(S) ≥ 1−ε and U,1S ≤ ε. It would then follow that U ≡ 0, which is a contradiction.

Now it remains to verify the claim. There exists a sequence of measure-preserving bijections σn: [0,1] → [0,1] such that Wn − Uσ

### → 0. Fix an m with Gm 1 ≤ ε, and let S be the complement of the support of Wm. So S is the disjoint union of at most |V (Gm)|2 rectangles and λ(S) ≥ 1 − ε. Choose an n > m so that δ (Wn,U) < |V (Gm)|−2 ε. Since Wn is also zero on S, we have Uσ

n

,1A×B ≤ δ (Wn,U) < |V (Gm)|−2 ε for every rectangle A × B contained in S. Summing over the at most |V (Gm)|2 such rectangles whose disjoint union is S, we ﬁnd that

n

Uσ

,1S ≤ ε. The claim then follows.

n

The following proposition shows that when dealing with graphs, we can replace the measure-preserving bijection implicit in δ with a permutation of the vertices. Proposition 5.2. Let C > 0 and p > 1, and let (Gn)n≥0 be a C-upper Lp regular sequence of weighted graphs such that δ (Gn/ Gn 1 ,U) → 0 for some Lp graphon U. Then the vertices of the graphs Gn may be ordered in such a way that

WG

/ Gn 1 − U → 0.

n

We recall the following lemma5 from [25, Theorem 9.29], where it is attributed to Alon. Here δˆ (G1,G2) denotes the cut distance with respect to the optimal integral

5In [25], Theorem 9.29 is stated for weighted graphs whose edge weights lie in [0, 1], but it immediately implies the version stated here.

### overlay, i.e., δˆ (G1,G2) := minG

d (G 1,G2), where G 1 is G1 with any reordering of its vertices (assuming |V (G1)| = |V (G2)|). Lemma 5.3. For any two weighted graphs G1 and G2 with the same number v of vertices, unit node weights, and edge weights in [−1,1],

1

34 √log v

δˆ (G1,G2) ≤ δ (G1,G2) +

.

As an immediate corollary, if the graphs in the lemma have edge weights in [−K,K] instead for some K > 0, then the same inequality holds with the ﬁnal term replaced by 34K/√log v.

Note that it was proved in [8, Theorem 2.3] that δ (G1,G2) ≤ δˆ (G1,G2) ≤ 32δ (G1,G2)1/67

under the hypotheses of Lemma 5.3. It remains open whether δˆ (G1,G2) = O(δ (G1,G2)), which would slightly simplify the proof of Proposition 5.2 if true.

Proof of Proposition 5.2. Let Wn = WG

/ Gn 1, which depends on the ordering of the vertices of Gn. We need to show that some such ordering of vertices yields d (Wn,U) → 0, given that δ (Wn,U) → 0.

n

First we prove the lemma by a truncation argument under the additional hypotheses that the graphs Gn all have unit node weights and Wn p ≤ C. We begin by choosing a sequence of truncations Kn so that Kn → ∞ and Kn/ log |V (Gn)| → 0. (Note that |V (Gn)| → ∞ because (Gn)n≥0 is a C-upper Lp regular sequence.)

, where Pn is the partition of [0,1] into |V (Gn)| equal length intervals. By Lemma 5.3, we can reorder the vertices of Gn so that the corresponding graphon Wn satisﬁes

Let Un denote the step function UP

n

34Kn

n|≤Kn ≤ δ Wn1|W

n|≤Kn +

n|≤Kn,Un1|U

n|≤Kn,Un1|U

d Wn1|W

log |V (Gn)| ≤ δ Wn,Wn1|W

n|≤Kn,U

n|≤Kn + δ Un1|U

34Kn log |V (Gn)|

+ δ (Wn,U) +

. Using this inequality to bound the right side of

d (Wn,U) ≤ d (Wn,Wn1|W

n|≤Kn,U)

n|≤Kn) + d (Un1|U

+ d (Wn1|W

n|≤Kn,Un1|U

n|≤Kn) and bounding δ by d yields

34Kn log |V (Gn)|

d (Wn,U) ≤ δ (Wn,U) +

+ 2d (Wn,Wn1|W

n|≤Kn) + 2d (Un1|U

n|≤Kn,U). To estimate 2d (Wn,Wn1|W

n|≤Kn,U), we will bound d by d1. We have

n|≤Kn) + 2d (Un1|U

n|≤Kn ≤ Wn1|W

d1 Wn,Wn1|W

n|>Kn 1

≤ Wn(|Wn|/Kn)p−1 1 = Wn pp /Knp−1 ≤ Cp/Knp−1. Similarly,

n|≤Kn ≤ Un pp /Knp−1 ≤ U pp /Knp−1 ≤ Cp/Knp−1

d1 Un,Un1|U

(note that U p ≤ C by Theorem 2.8). It follows that d (Wn,U) ≤ δ (Wn,U) +

2Cp Knp−1

34Kn log |V (Gn)|

+

+ 2d1(U,Un).

We have d1(U,Un) → 0 by the Lebesgue diﬀerentiation theorem, and all the other terms tend to zero by assumption. Thus d (Wn,U) → 0.

Next we relax the assumption of unit node weights, and instead assume that every vertex in Gn has weight 1+o(|V (Gn)|−1) (i.e., nearly equal node weights). Let Wn be a step function with the same values as Wn, but where the step widths have all been modiﬁed to be exactly 1/|V (Gn)|. We will show that Wn − Wn

= o(1), which suﬃces to reduce this case to the previous one. Indeed, suppose the step widths of Wn are all in the interval [1/|V (Gn)|−αn,1/|V (Gn)|+αn], where αn|V (Gn)|2 → 0. Then Wn and Wn diﬀer on a set Bn of measure at most 2|V (Gn)|2αn = o(1), because each of the lines separating the steps is moved by less than |V (Gn)|αn (typically much less). By H¨lder’s inequality,

1

Wn − Wn

### =

1

Bn

Wn − Wn dλ ≤ Wn − Wn

λ(Bn)1−1/p.

p

We know that Wn p ≤ C, and it is easy to check that Wn

is bounded as well. Since λ(Bn) → 0, it follows that Wn − Wn

p

→ 0. This reduces the case of nearly equal node weights to that of equal node weights.

1

Finally, we prove the result for a C-upper Lp regular sequence of weighted graphs. We may replace C by a larger value if necessary and assume that Gn is (C,ηn)-upper Lp regular with ηn → 0. Let αmax(Gn) denote the largest node weight in Gn, and recall that αmax(Gn)/αG

n ≤ ηn by Deﬁnition 2.1. By Remark 4.7, there is some equipartition Pn of V (Gn) into kn parts, for some slowly growing kn satisfying kn → ∞ and kn2ηn → 0, so that W n := (Wn)P

satisﬁes d (W n,Wn) → 0. Then δ (W n,U) → 0. Furthermore, W n p ≤ C since Gn is (C,ηn)-upper Lp regular. Note that W n is a step function with step widths 1/kn + o(1/kn2), since Pn is an equipartition into kn parts and αmax(Gn)/αG = o(1/kn2). Now we apply the case in the previous paragraph to W n to reorder the parts of Pn so that d (W n,U) → 0. If we order the vertices of Gn according to this ordering of Pn and arbitrarily order the vertices within each part, then d (Wn,U) ≤ d (W n,Wn) + d (W n,U) → 0, as desired.

n

6. W-random weighted graphs

In this section and the next, we prove Theorem 2.14 on W-random graphs, thereby traversing the outer arrows of Figure 2.1. First, in this section, we address the arrow (Lp graphon limit) → (Lp graphon sequence) by proving Theorem 2.14(a), which says that d1(H(W,n),W) → 1 almost surely (i.e., with probability 1) for any L1 graphon W.

The following theorem of Hoeﬀding on U-statistics implies that H(W,n) 1 → W 1 almost surely.

Theorem 6.1 (Hoeﬀding [20]). Let W : [0,1]2 → R be a symmetric, integrable function, and let x1,x2,... be a sequence of i.i.d. random variables uniformly

chosen from [0,1]. Then with probability 1, lim

- 1 n

- 2 1≤i<j≤n


W(xi,xj) →

W(x,y)dxdy.

n→∞

[0,1]2

- Proof of Theorem 2.14(a). All weighted random graphs H(·,n) in this proof come


from the same random sequence x1,x2,... with terms drawn uniformly i.i.d. from [0,1].

Fix ε > 0. It suﬃces to show that limsupn→∞ d1(H(W,n),W) ≤ ε holds with probability 1.

Let P denote the partition of [0,1] into m equal intervals, where m is chosen to

be suﬃciently large that W − WP 1 ≤ ε/2. Fix this m and P. Since the sequence x1,x2,... is equidistributed among the m intervals of P, with probability 1 we have d1(H(WP,n),WP) → 0 as n → ∞.

We have d1(H(W,n),H(WP,n)) = H(W − WP,n) 1, which by Theorem 6.1

converges almost surely to W − WP 1. It follows that, with probability 1, the limit superior (as n → ∞) of

d1(H(W,n),W) ≤ d1(W,WP) + d1(WP,H(WP,n)) + d1(H(WP,n),H(W,n)) is at most 2 W − WP 1 ≤ ε, as claimed.

7. Sparse random graphs In this section we prove Theorem 2.14(b); i.e., we prove that with proba-

bility 1, d (ρ−n1G(n,W,ρn),W) → 0. From Theorem 2.14(a) we know that limn→∞ d1(H(n,W),W) = 0 with probability 1. So it remains to show that

- (7.1) d (ρ−n1G(n,W,ρn),H(n,W)) → 0 as n → ∞.


Here G(n,W,ρn) and H(n,W) are both generated from a common i.i.d. random sequence x1,x2,... ∈ [0,1]. We keep this assumption throughout the section.

We will need the following variant of the Chernoﬀ bound. The proof (a modiﬁcation of the usual proof) is included in Appendix B.

- Lemma 7.1. Let X1,...,Xn be independent random variables, where for each i, Xi is distributed as either Bernoulli(pi) or −Bernoulli(pi). Let X = X1 + ··· + Xn and q = p1 + ··· + pn. Then for every λ > 0,

P(|X − EX| ≥ λq) ≤

2exp −31λ2q if 0 < λ ≤ 1, 2exp −13λq if λ > 1.

For a weighted graph H with unit vertex weights and edge weights βij ∈ [−1,1], we use G(H) to denote the random graph with vertex set V (H) and an edge between i and j with probability |βij|, and we assign the edge weight +1 if βij > 0 and −1 if βij < 0. (In other words, G(H) = G(H,1) in the notation of §2.7.)

The next two lemmas form the (Lp graphon sequence) → (Lp upper regular sequence) arrow in Figure 2.1.

- Lemma 7.2. Let ε > 0. Let H be a weighted graph on n vertices with unit vertex weights, edge weights βij(H) ∈ [−1,1], and βii(H) = 0 for all i,j ∈ V (H). Then


1 24

P(d (G(H),H) ≤ ε H 1) ≥ 1 − 2n+1 exp −

min{ε,ε2} H 1 n2 .

Proof. Let V = V (G) = V (H) = [n]. For any subset U ⊆ V , let βU(H) =

βij(H)

i<j i,j∈U

be the sum of the edge weights of H inside U. Similarly deﬁne βU(G), where G = G(H). We also deﬁne

|β|U (H) =

|βij(H)|.

i<j i,j∈U

Set

εn2 H 1 4|β|U (H) ≥

εn2 H 1 4|β|V (H)

ε 2

λ =

. It follows from Lemma 7.1 that P |βU(G) − βU(H)| ≥

=

1 4

εn2 H 1 = P(|βU(G) − βU(H)| ≥ λ|β|U (H))

1 3

min{λ,1}λ|β|U (H)

≤ 2exp −

1 12

ε 2

,1 εn2 H 1

≤ 2exp −

min

1 24

min{ε2,ε}n2 H 1 . By the union bound, with probability at least 1−2n+1 exp −241 min{ε2,ε}n2 H 1 ,

≤ 2exp −

- (7.2) |βU(G) − βU(H)| ≤

1 4

εn2 H 1 for all U ⊆ [n]. For S,T ⊆ V , let

βS×T =

s∈S,t∈T

βst. We have

βS×T = βS∪T + βS∩T − βS\T − βT\S. We deduce from (7.2) that

|βS×T(G) − βS×T(H)| ≤ εn2 H 1 for all S,T ⊆ [n], which is equivalent to d (G,H) ≤ ε H 1.

The following lemma shows that d (ρ−n1G(Hn,ρn),Hn) → 0 for any sequence of weighted graphs that satisfy certain mild conditions on the edge weights. Recall the deﬁnition of the random graph G(Hn,ρn) from §2.7.

- Lemma 7.3. Let ρn > 0 with ρn → 0 and nρn → ∞. For each n let Hn be a weighted graph with n vertices all with unit vertex weights, and containing no loops. Suppose that Hn 1 is uniformly bounded and the edge weights βij(H) satisfy


- (7.3) lim n→∞


1 n2 1≤i<j≤n

max{|βij(Hn)| − ρ−n1,0} = 0.

Then

d (ρ−n1G(Hn,ρn),Hn) = 0

lim

n→∞

with probability 1. Proof. Deﬁne the weighted graph H n with edge weights

βij(H n) = sign(βij(Hn))min{ρn |βij(Hn)|,1}. So G(Hn,ρn) = G(H n). We have

- (7.4)


1 n2

d1(ρ−n1H n,Hn) =

1 n2

=

n

|ρ−n1βij(H n) − βij(Hn)|

i,j=1

n

max{|βij(Hn)| − ρ−n1,0},

i,j=1

which goes to 0 as n → ∞, by assumption (7.3). It follows that ρ−n1 H n 1 = Hn 1 + o(1) = O(1), as we assumed that Hn 1 is uniformly bounded. By

- Lemma 7.2 for every ε > 0 we have


1 24

ερn H n 1

P(d (G(H n),H n) ≤ ερn) ≥ 1 − 2n+1 exp −

,1 ερnn2

min

1 24

≥ 1 − 2n+1 exp −

min{Ω(ε),1}ερnn2 ≥ 1 − 2−ω(n)

as n → ∞, since nρn → ∞. So by the Borel-Cantelli lemma, lim

ρ−n1d (G(H n),H n) = 0 with probability 1. Combined with (7.4) we obtain the desired conclusion.

n→∞

Finally we put everything together and complete Figure 2.1 with the arrow (Lp graphon limit) → (Lp upper regular sequence).

- Proof of Theorem 2.14(b). We need to show (7.1). We apply Lemma 7.3 with


Hn = H(W,n). By Theorem 6.1, Hn 1 → W 1 almost surely, so in particular Hn 1 is uniformly bounded. It remains to check (7.3). We have

1 n2 1≤i<j≤n

1 n2 1≤i<j≤n

max{|βij(Hn)| − ρ−n1,0} =

max{|W(xi,xj)| − ρ−n1,0},

which converges to 0 as n → ∞ with probability 1 by Theorem 6.1. Indeed, since ρn → 0, for every K > 0 the limit superior of the above expression is bounded by

- 1

- 2 max{|W| − K,0} 1 by Theorem 6.1, and this can be made arbitrarily small by choosing K large.


### Proof of Corollary 2.15. By Theorem 2.14(b), δ (ρ−n1Gn,W) → 0 with probability 1 as n → ∞, and applying the theorem to |W| shows that ρ−n1 Gn 1 → W 1 with

probability 1. It follows that δ

Gn Gn 1

W W 1

ρn Gn 1

,

=

ρn Gn 1

≤

ρn Gn 1

≤

→ 0, as desired.

Gn 1 ρn W 1

δ ρ−n1Gn,

W

Gn 1 ρn W 1

δ ρ−n1Gn,W + δ W,

W

Gn 1 ρn W 1

δ ρ−n1Gn,W + W 1 −

Proof of Proposition 2.16. By Corollary 2.11, the sequence (Gn)n≥0 must be W pupper Lp regular. From δ (Gn/ Gn 1 ,W) → 0 we obtain W 1 = 1 (note that W ≥ 0 because Gn is simple), and by Proposition A.1 we have n G 1 → ∞. It then follows from Corollary 2.15 that δ (G n/ G n 1 ,W) → 0 with probability 1. By Proposition 5.2 we can order the vertices of Gn and G n so that d (Gn/ Gn 1 ,W) → 0 and d (G n/ G n 1 ,W) → 0, and thus

Gn Gn 1

G n

G n 1 → 0, as desired.

d

,

8. Counting lemma for Lp graphons

In this section we establish results relating to counting lemmas for Lp graphons, as stated in §2.9.

We use the following generalization of Ho¨lder’s inequality from [17] (also see [28, Theorem 3.1]). This inequality played a key role in recent work by the fourth author and Lubetzky [28] resolving a conjecture of Chatterjee and Varadhan [10] on large deviations in random graphs, which involves an application of graph limits.

Theorem 8.1 (Generalized Ho¨lder’s inequality). Let µ1,...,µn be probability measures on Ω1,...,Ωn, respectively, and let µ = ni=1 µi be the product measure on Ω = ni=1 Ωi. Let A1,...,Am be nonempty subsets of [n] := {1,...,n} and write ΩA = ∈A Ω and µA = ∈A µ . Let fi ∈ Lp

### ) with pi ≥ 1 for each i ∈ [m] and suppose in addition that i: ∈A

### (ΩA

### ,µA

i

i

i

### (1/pi) ≤ 1 for each ∈ [n]. Then m

i

m

1/pi

|fi|pi dµA

|fi| dµ ≤

.

i

i=1

i=1

Proof of Proposition 2.19. For the ﬁrst assertion, we can give an example in the form of a separable graphon, i.e., one of the form W(x,y) = w(x)w(y). Let w: [0,1] → [0,∞) be in Lp([0,1]) for all p < ∆ but not p = ∆, e.g., w(x) = x−1/∆ (and w(0) = 0).

Then W p = w 2p < ∞ for all p < ∆, but t(F,W) = v∈V (G) w deg

F (v)

degF(v), which is inﬁnite since w ∆ = ∞.

For the second assertion, apply Theorem 8.1 with n = |V (F)|, Ωi = [0,1], µi equal to Lebesgue measure, A1,...,Am the edges of F (i.e., they are two-element subsets of V (F)), and pi = ∆ for all i.

### Lemma 8.2. Let F be a simple graph with maximum degree ∆. Let ∆ < p < ∞ and let q = p/(p − ∆ + 1). For each edge e ∈ E(F), let We be an Lp graphon. Fix an edge e1 ∈ E(F). Then

Wij(xi,xj)dx1 ···dx|V (F)| ≤ We

We p .

1 q

[0,1]|V (F)| ij∈E(F)

e∈E(F)\{e1}

Proof. Apply Theorem 8.1 with n = |V (F)|, Ωi = [0,1], µi equal to Lebesgue measure, A1,...,Am the edges of F (with A1 = e1), p1 = q, and pi = p for i ≥ 2. The inequality i: ∈A

(1/pi) ≤ 1 is satisﬁed for each because q < p and 1/q + (∆ − 1)/p = 1 (at most one term 1/pi with ∈ Ai can equal 1/q, the others equal 1/p, and there are at most ∆ terms).

i

Proof of Theorem 2.20. Let V (F) = {1,2,...,n} and E(F) = {e1,...,em}. Let it,jt be the endpoints of et, for 1 ≤ t ≤ m. We may assume that U − W ≤ ε. We have

m

m

t(F,U) − t(F,W) =

) −

) dx1 ···dxn.

U(xi

### ,xj

W(xi

### ,xj

t

t

t

t

[0,1]n

t=1

t=1

m

### ) − W(xi

### ))·

=

U(xi

### ,xj

### ) (U(xi

### ,xj

### ,xj

s

s

t

t

t

t

t=1 [0,1]n s<t

### ) dx1 ···dxn. It suﬃces to show that for each t = 1,...,m,

W(xi

### ,xj

s

s

s>t

- (8.1)

Let K > 0, which we will choose later. Let U = U≤K+U>K, where U≤K := U1|U|≤K and U>K := U1|U|>K. Similarly, let W≤K := W1|W|≤K and W>K := W1|W|>K. We claim that

[0,1]n s<t

U≤K(xi

s

,xj

s

) (U(xi

t

,xj

t

) − W(xi

t

,xj

t

))·

s>t

W≤K(xi

s

,xj

s

) dx1 ···dxn

≤ 4Km−1ε.

- (8.2)

Indeed, if we ﬁx the value of xi for all i ∈ [n] \ {it,jt}, then the integral in (8.2) has the form

- (8.3) Km−1 [0,1]2


### ) − W(xi

) dx1 ···dxn

U(xi

### ,xj

### ) (U(xi

### ,xj

### ,xj

))

W(xi

### ,xj

s

s

t

t

t

t

s

s

[0,1]n s<t

s>t

p−∆ p−∆+m−1

2ε p − ∆

≤ 2(m − 1 + p − ∆)

.

### ) − W(xi

(U(xi

### ,xj

### ,xj

### ))a(xi

### )b(xj

### )dxi

### dxj

t

t

t

t

t

t

t

t

### for some functions a(·) and b(·) with a ∞ , b ∞ ≤ 1, where a(·) and b(·) depend on the values of xi for i ∈ [n] \ {it,jt}) that we ﬁxed. Thus (8.3) is bounded in

absolute value by Km−1 U − W ∞→1 ≤ 4Km−1ε, using (2.3). The inequality (8.2) then follows.

Next we claim that the diﬀerence between the integral in (8.1) and the integral in (8.2) is bounded in absolute value by 2(m−1)/Kp−∆. Indeed, writing this diﬀerence as a telescoping sum in a similar fashion to what we did at the beginning of this proof, it suﬃces to show that each expression of the following form is bounded in absolute value by 2/Kp−∆:

- (8.4)


U∗(xi

### ,xj

s

[0,1]n s<t

### ) − W(xi

### ) (U(xi

### ,xj

### ,xj

))

s

t

t

t

t

) dx1 ···dxn,

W∗(xi

### ,xj

s

s

s>t

where we replace exactly one of the m − 1 subscript ∗’s by ‘> K’, replace some of the other ∗’s by ‘≤ K’, and then erase the remaining ∗’s. Now we apply Lemma 8.2 with the special edge e0 corresponding to the factor whose subscript is replaced by ‘> K’. We use U≤K p ≤ U p ≤ 1 and W≤K p ≤ W p ≤ 1. Using the triangle inequality we have U − W p ≤ 2. Also,

= U p/qp /Kp/q−1 ≤ 1/Kp−∆.

U>K q ≤ U(|U|/K)p/q−1

q

It then follows from Lemma 8.2 that an integral of the form (8.4) is at most 2/Kp−∆ in absolute value.

Combining the bounds on (8.2) and (8.4), we see that the integral in (8.1) is bounded in absolute value by

4Km−1ε + 2(m − 1)/Kp−∆.

We optimize this bound by choosing K = ((p − ∆)/(2ε))1/(m−1+p−∆), which gives the bound in (8.1) that we claimed.

Next we give an example showing that no counting lemma can hold when p ≤ ∆.

Proof of Proposition 2.22. By nesting of norms, we only need to consider the case p = ∆. For for each n ≥ 1, consider the separable graphon Wn deﬁned by

Wn(x,y) := wn(x)wn(y),

where wn(x) := 1 + un(x) with un(x) := (xlnn)−1/∆1[1/n,1](x). We chose un so that it satisﬁes un ∆ = 1 and limn→∞ un p = 0 for 1 ≤ p < ∆.

We have

Wn ∆ = wn 2∆ ≤ (1 + un ∆)2 = 4. Also, since Wn(x,y) − 1 = un(x) + un(y) + un(x)un(y),

Wn − 1 1 ≤ 2 un 1 + un 21 → 0 as n → ∞. It remains to verify that liminfn→∞ t(F,Wn) > 1. Since Wn is separable, t(F,Wn) =

wn deg

F (v)

degF(v) . For any integer k,

v∈V (F)

k

wn kk = E[(1 + un)k] =

i=0

n i

un ii .

Since un ∆ = 1 and limn→∞ un p = 0 for any 1 ≤ p < ∆, we ﬁnd that limn→∞ wn kk = 1 when 1 ≤ k < ∆, and limn→∞ wn ∆∆ = 2. Therefore,

t(F,Wn) = 2|{v∈V (G) : degF(v)=∆}| > 1, as desired.

lim

n→∞

There has been some recent work by the fourth author along with Conlon and Fox [14, 15] developing counting lemmas for sparse graphs assuming additional hypotheses. Namely one assumes that the sparse graph G is a relatively dense subgraph of another sparse graph Γ that has certain pseudorandomness properties. For example, to obtain a counting lemma for K3 in G, one assumes that t(H,Γ/ Γ 1) = 1 + o(1) whenever H is a subgraph of K2,2,2 (which is the 2-blowup of K3). More generally, an F-counting lemma needs t(H,Γ/ Γ 1) = 1 + o(1) whenever H is a subgraph of the 2-blow-up of F. One might ask whether this result can be extended to Lp upper regular graphs. This is an interesting and non-trivial problem, and we leave it open for future work.

Acknowledgments

We thank Oliver Riordan for suggesting the topic of Appendix C, Svante Janson for providing valuable feedback on our manuscript, Omer Tamuz for helpful discussions, Remco van der Hofstad for comments about U-statistics that led us to [20], Donald Cohn for advice about measure theory, and Patrick Wolfe and Soﬁa Olhede for bringing [37] to our attention.

Appendix A. Lp upper regularity implies unbounded average degree

Proposition A.1. Let C > 0 and p > 1, and let (Gn)n≥0 be a C-upper Lp regular sequence of simple graphs. Then |E(Gn)|/|V (Gn)| → ∞ as n → ∞.

This proposition follows immediately from the following lemma.

Lemma A.2. For every C > 0 and p > 1 there exist η0 > 0 and c > 0 such that if 0 < η < η0 and G is a (C,η)-upper Lp regular simple graph, then |E(G)|/|V (G)| ≥ cη−1+1/p.

Proof. Let η0 = min (2C)−p/(p−1)/2,1/3 , and suppose G is a (C,η)-upper Lp regular simple graph with 0 < η < η0. We will omit all ﬂoor and ceiling signs below in order to keep the notation clean.

Let V = V (G), n = |V |, and m = |E(G)|, let T be a maximal matching (a maximal set of vertex-disjoint edges) in G consisting of t edges, and let A be the set of vertices in T. We begin by showing that our choice of η0 ensures t ≥ η0n.

The proof of t ≥ η0n will amount to applying the deﬁnition (2.1) of (C,η)-upper regularity to the partition {A,V \ A}. To do so, we need both |A| and |V \ A| to be at least ηn. If A is too small, then we simply enlarge it to have size ηn; we will see below that this case never actually occurs. We need not worry about the case when A is too large, because then t ≥ η0n automatically holds (since in that case η0 ≤ 1/3 implies t = |A|/2 ≥ (1 − η)n/2 ≥ η0n).

Now we can apply upper regularity. Every edge of G has a vertex in A due to the maximality of T, and so from the partition {A,V \ A} and the (C,η)-upper Lp

regularity of G we obtain

p

p

|A|2 |V |2

ρG(A,V \ A) G 1

+ |A||V \ A| |V |2

ρG(A,A) G 1

Cp ≥

p

p

= |A|2 |V |2

|E(G) \ E(A)| |A||V \ A| G 1

|E(A)| |A|2 G 1

+ |A||V \ A| |V |2

p

|A| |V |

|E(G)| |A||V | G 1

≥

p

= |A| n

n 2|A|

,

where the last inequality follows from Jensen’s inequality and the convexity of x  → xp. Thus,

|A| ≥ (2C)−p/(p−1)n ≥ 2η0n

and hence t = |A|/2 ≥ η0n. (In particular, A cannot have been enlarged in the previous paragraph, because then |A| = ηn would contradict |A| ≥ 2η0n.)

Let P = {P1,...,P1/η} be a partition of V into sets of size ηn (plus at most one remainder set of size between ηn and 2ηn) so that every edge of T lies entirely in some part of P; in other words, T ⊆ i Pi ×Pi. Then, by the deﬁnition of Lp upper regularity and the convexity of x  → xp,

p 

 

1/p

1/η

|Pi|2 |V |2

2|T ∩ (Pi × Pi)| |Pi|2

2Cm/n2 = C G 1 ≥ GP p ≥

i=1

p 1/p

1/η i=1 |Pi|2

2|T|

≥

|V |2

1/η i=1 |Pi|2

2t n2/p 1i=1/η |Pi|2 (p−1)/p

=

η0n n2/p η−1(nη)2 (p−1)/p

= Ω

= Ω η0η−(p−1)/pn−1 . It follows that m/n = Ωp,C η−(p−1)/p , as desired.

Appendix B. Proof of a Chernoff bound Proof of Lemma 7.1. Let t = ln(1 + λ). We have

(B.1)

P(X − EX ≥ λq) ≤ E[exp(t(X − EX − λq))]

n

E[exp(t(Xi − EXi − λpi))].

=

i=1

If Xi is distributed as Bernoulli(pi), then E[exp(t(Xi − EXi − λpi))] = (1 − pi + piet)exp(−tpi(1 + λ)) ≤ exp(pi(et − 1 − t(1 + λ))).

We have

−13λ2 if 0 < λ ≤ 1, −31λ if λ > 1.

et − 1 − t(1 + λ) = λ − (1 + λ)ln(1 + λ) ≤

On the other hand, if Xi is distributed as −Bernoulli(pi), then E[exp(t(Xi − EXi − λpi))] = (1 − pi + pie−t)exp(tpi(1 − λ))

≤ exp(pi(e−t − 1 + t(1 − λ))) and

e−t − 1 + t(1 − λ) = −λ 1 + λ

+ (1 − λ)ln(1 + λ) ≤

Thus in both cases,

−12λ2 if 0 < λ ≤ 1, −12λ if λ > 1.

exp −13λ2pi if 0 < λ ≤ 1, exp −13λpi if λ > 1.

E[exp(t(Xi − EXi − λpi))] ≤

Using these bounds in (B.1), we ﬁnd that

exp −13λ2q if 0 < λ ≤ 1, exp −31λq if λ > 1.

P(X − EX ≥ λq) ≤

The same upper bound holds for P(X − EX ≤ −λq) since it is equivalent to the previous case after negating all Xi’s. The result follows by combining the two bounds using a union bound.

Appendix C. Uniform upper regularity

In the theory of martingale convergence, Lp boundedness implies Lp convergence when p > 1, but the same is not true for p = 1. Instead, L1 convergence is characterized by uniform integrability. Oliver Riordan asked whether there is a similar characterization of convergence to L1 graphons. In this appendix, we show that the answer is yes. Although bounding the L1 norm itself is insuﬃcient, more detailed tail bounds suﬃce. In fact, the same truncation arguments that work for p > 1 then extend naturally to p = 1.

- Deﬁnition C.1. Let K : (0,∞) → (0,∞) be any function. A graphon W has K-bounded tails if for each ε > 0,


W1|W|≥K(ε) 1 ≤ ε. A set S of graphons is uniformly integrable if there exists a function K : (0,∞) → (0,∞) such that all graphons in S have K-bounded tails.

Every graphon has K-bounded tails for some K, because we have assumed as part of our deﬁnition that all graphons are L1. For purposes of analyzing convergence, we consider a tail bound function K to be the L1 equivalent of a bound on the Lp norm for p > 1. For comparison, note that for K > 0,

W pp Kp−1 ,

p−1

W1|W|≥K 1 ≤ W |W|

=

K

1

which tends to zero as K → ∞ as long as p > 1 and W p < ∞.

Recall that L1 upper regularity is vacuous, since every graphon is L1 upper regular. To get the right notion of upper regularity, we simply replace L1 boundedness with K-bounded tails:

- Deﬁnition C.2. Let K : (0,∞) → (0,∞) and η > 0. A graphon W is (K,η)-upper


regular if WP has K-bounded tails for every partition P of [0,1] with all parts of size at least η.

A sequence (Wn)n≥0 of graphons is uniformly upper regular if there exist K : (0,∞) → (0,∞) and η0,η1,... > 0 such that limn→∞ ηn = 0 and Wn is (K,ηn)-upper regular.

We deﬁne (K,η)-upper regularity of a weighted graph G using the graphon

WG/ G 1, except that we consider only partitions P that correspond to partitions of V (G) for which all the parts have weight at least ηαG, and we require every vertex of G to have weight at most ηαG.

Note that if a graph sequence has no dominant nodes and the corresponding graphon sequence is uniformly upper regular, then so is the graph sequence.

Uniform upper regularity is the proper L1 analogue of Lp upper regularity, and imposing uniform integrability avoids the otherwise pathological behavior of L1 graphons. Our results for Lp graphons with p > 1 then generalize straightforwardly to L1. In the remainder of this appendix, we state the results and describe the minor modiﬁcations required for their proofs.

We will need the following two lemmas, which are standard facts about uniform integrability and conditioning a uniformly integrable set of random variables on diﬀerent σ-algebras.

- Lemma C.3. Let K : (0,∞) → (0,∞) be any function. Then for each ε > 0, there exists δ > 0 such that for every graphon W with K-bounded tails and every subset I of [0,1]2 with Lebesgue measure λ(I) ≤ δ,

I

|W| ≤ ε.

Explicitly, δ can be chosen to be ε/(2K(ε/2)). Proof. For each I satisfying λ(I) ≤ ε/(2K(ε/2)),

W1I 1 ≤ W1|W|≤K(ε/2)1I 1 + W1|W|≥K(ε/2) 1 ≤ K(ε/2)λ(I) + ε/2 ≤ ε.

- Lemma C.4. Let S be a uniformly integrable set of graphons. Then


{WP : W ∈ S and P is a partition of [0,1]} is uniformly integrable.

Proof. Suppose W 1 ≤ C for all W ∈ S (every uniformly integrable set is L1 bounded). Let ε > 0, and let δ be such that W1I 1 ≤ ε whenever W ∈ S and λ(I) ≤ δ, by Lemma C.3. We will show that if K = C/δ, then WP1|W

P|≥K 1 ≤ ε for all W ∈ S and P.

Let W be in S and P be a partition, and let I be the set on which |WP| ≥ K. Then

Kλ(I) ≤ WP 1 ≤ W 1 ≤ C, and hence λ(I) ≤ δ. It follows that W1|W

P|≥K 1 ≤ W1|W

P|≥K 1 ≤ ε, while WP1|W

P|≥K 1 thanks to the triangle inequality (look at each part of P). Thus, WP1|W

P|≥K 1 ≤ ε,

as desired. We begin with the analogue of Proposition 2.10.

Proposition C.5. Let W0,W1,... and W be graphons such that δ (Wn,W) → 0 as n → ∞. Then the sequence (Wn)n≥0 is uniformly upper regular.

It follows immediately that the same also holds for graphs, as long as they have no dominant nodes. Proof. Choose ηn so that ηn → 0 and

≤ ηn3 for some measure-preserving bijection σn on [0,1]. Then (Wn)P − (Wσ

Wn − Wσ

n

)P ∞ ≤ ηn whenever all the parts of P have size at least ηn, as in Lemma 5.1. We would like to show that picking K large enough forces (Wn)P 1|(Wn)P|≥K

n

to be small. We have

1

≤ ((Wσ

(Wn)P 1|(Wn)P|≥K

)P + ηn)1|(Wn)P|≥K

n

1

1 ≤ ((Wσ

.

)P + ηn)1|(Wσn)P|≥K−ηn

n

1

If we take K ≥ 2ηn (which is possible because ηn → 0 as n → ∞), then we have an upper bound of

2 (Wσ

, which tends uniformly to zero as K → ∞ by Lemma C.4.

)P 1|(Wσn)P|≥K−ηn

n

1

The converse is also true: every uniformly upper regular sequence has a convergent subsequence (Theorem C.13). This is the analogue of Theorem 2.9, but we will have to develop machinery for the L1 case before we can prove it.

- Theorem C.6 (Weak regularity lemma). Fix K : (0,∞) → (0,∞). For each ε > 0, there exists an N such that for every natural number k ≥ N, every graphon W with K-bounded tails, and every equipartition P of [0,1], there exists an equipartition Q reﬁning P into k |P| parts such that


W − WQ ≤ ε.

Proof. We start by applying the L2 weak regularity lemma (Lemma 3.3) to the truncation W1|W|≤K(ε/4), which has L2 norm at most K(ε/4). It follows that the theorem statement holds with the conclusion replaced by

W1|W|≤K(ε/4) − W1|W|≤K(ε/4) Q ≤ ε/4. Thus, for U := W1|W|≤K(ε/4) we can ﬁnd a Q such that

U − UQ ≤ ε/4. Then

W − UQ ≤ W1|W|≥K(ε/4) 1 + U − UQ ≤ ε/2,

from which it follows that W − WQ ≤ ε (see the end of Remark 4.4 for this standard inequality). Thus, the same partitions that give an ε/4-approximation of U give an ε-approximation of W.

The compactness of the Lp ball (Theorem 2.13) requires uniform integrability when p = 1:

- Theorem C.7. Let (Wn)n≥0 be uniformly integrable sequence of graphons. Then there exists a graphon W such that


liminf

δ (Wn,W) = 0.

n→∞

Proof. The proof is almost the same as that of Theorem 2.13 with p = 1, but it uses the martingale convergence theorem for uniformly integrable martingales [16, Theorem 5.5.6], rather than Lp martingales, and it uses Theorem C.6 for weak regularity. The only substantive diﬀerence is in verifying that the martingale U1,U2,... is uniformly integrable (using the notation from the proof). To do so, we start by observing that the graphons Wn,k are uniformly integrable by Lemma C.4. Now uniform integrability for Uk follows straightforwardly, since Wn,k converges pointwise to Uk as n → ∞ and has only |Pk| parts.

Corollary C.8. Every set of graphons that is uniformly integrable and closed under the cut metric is compact under that metric.

We will also need analogues of the results of Section 4 for uniform upper regularity. The analogues of Lemmas 4.1 and 4.2 are straightforward (they use Lemma C.3 to replace H¨lder’s inequality):

- Lemma C.9. Let K : (0,∞) → (0,∞) and ε > 0. Then there exists a constant η0 = η0(K,ε) such that the following holds for all η ∈ (0,η0): if W : [0,1]2 → R is a (K,η)-upper regular graphon and S,T ⊆ [0,1] are measurable subsets with λ(S) ≤ η0, then

| W,1S×T | ≤ ε.

- Lemma C.10. Let K : (0,∞) → (0,∞) and ε > 0. Then there exists a constant


η0 = η0(K,ε) such that the following holds for all η ∈ (0,η0) and every (K,η)upper regular graphon W: if S,S ,T,T ⊆ [0,1] are measurable sets satisfying λ(S S ),λ(T T ) ≤ η0, then

| W,1S×T − 1S ×T  | ≤ ε.

Using these two lemmas, one can then prove the analogue of Theorem 4.3. Indeed, (4.2) and (4.3) (with C = 1) follow from Lemmas C.10 and C.3, leading again to a bound of the form (4.4). Once (4.4) is established, the proof then just proceeds as in the truncation argument in Case II of the proof of Theorem 4.3 by setting U = WP

1|W

Pn|≤K(˜ε) for some suitable ε˜. This leads to the following theorem:

n

- Theorem C.11 (Weak regularity lemma for (K,η)-upper regular graphons). Let K : (0,∞) → (0,∞) and 0 < ε < 1. Then there exist constants N = N(K,ε) and


η0 = η0(K,ε) such that the following holds for all η ≤ η0: for every (K,η)-upper regular graphon W, there exists a partition P of [0,1] into at most 4N measurable parts, each having measure at least η, so that

W − WP ≤ ε.

Following the strategy leading to Remark 4.4 for graphons, and that leading to Theorem 4.5 and Remark 4.7 for graphs, one then gets the following version involving equipartitions and holding also for graphs.

- Theorem C.12. Let K : (0,∞) → (0,∞) and 0 < ε < 1. Then there exist constants

N = N(K,ε) and η0 = η0(K,ε) such that the following holds for all η ≤ η0: for every (K,η)-upper regular graphon W and each natural number k ≥ N, there exists a equipartition P of [0,1] into k parts so that

W − WP ≤ ε.

The same holds for a weighted graph G with W = WG/ G 1, in which case we can use an equipartition of the vertex set, as in Remark 4.7.

Theorem C.12 now allows us to prove the analogue of Theorem 2.8 and 2.9.

- Theorem C.13. Every uniformly upper regular sequence of graphons or weighted graphs has a subsequence that converges to an L1 graphon under the normalized cut metric.


The proof is almost identical to that of Theorems 2.8 and 2.9: we use the transference theorem (Theorem C.12) to reduce to the compactness theorem (Theorem C.7).

Finally, we conclude by noting that the proofs of Propositions 5.2, A.1, and 2.16 carry over to uniform upper regularity:

- Proposition C.14. Let (Gn)n≥0 be a uniformly upper regular sequence of weighted

graphs with δ (Gn/ Gn 1 ,W) → 0 for some graphon W. Then the vertices of the graphs Gn may be ordered in such a way that WG

n

/ Gn 1 − W → 0.

- Proposition C.15. Let (Gn)n≥0 be a uniformly upper regular sequence of simple graphs. Then |E(Gn)|/|V (Gn)| → ∞ as n → ∞.
- Proposition C.16. Let W be any graphon, and let (Gn)n≥0 be a sequence of simple graphs such that Gn 1 → 0 and δ (Gn/ Gn 1 ,W) → 0. Let G n = G(|V (Gn)|,W, Gn 1). Then with probability 1, one can order the vertices of Gn and G n so that


Gn Gn 1

G n G n 1 → 0.

d

,

The only substantive modiﬁcation required for the proofs is that the Lp upper regularity and convexity arguments in the proof of Proposition A.1 must be replaced with applications of Lemma C.3.

References

- [1] D. Aldous and R. Lyons, Processes on unimodular random networks, Electron. J. Probab. 12

(2007), 1454–1508. arXiv:math/0603062 doi:10.1214/EJP.v12-463 MR2354165

- [2] D. Aldous and J. M. Steele, The objective method: probabilistic combinatorial optimization and local weak convergence, in H. Kesten, ed., Probability on discrete structures, 1–72, Encyclopaedia Math. Sci. 110, Springer, Berlin, 2004. doi:10.1007/978-3-662-09444-0 1 MR2023650

- [3] N. Alon and J. H. Spencer, The probabilistic method, third edition, John Wiley & Sons, Inc., Hoboken, NJ, 2008. MR2437651
- [4] I. Benjamini and O. Schramm, Recurrence of distributional limits of ﬁnite planar graphs, Electron. J. Probab. 6 (2001), no. 23, 13 pp. arXiv:math/0011019 doi:10.1214/EJP.v6-96 MR1873300
- [5] P. J. Bickel and A. Chen, A nonparametric view of network models and NewmanGirvan and other modularities, Proc. Natl. Acad. Sci. USA 106 (2009), 21068–21073. doi:10.1073/pnas.0907096106
- [6] B. Bolloba´s and O. Riordan, Metrics for sparse graphs, in S. Huczynska, J. D. Mitchell, and C. M. Roney-Dougal, eds., Surveys in combinatorics 2009, pages 211–287, London Math. Soc. Lecture Note Ser. 365, Cambridge University Press, Cambridge, 2009. arXiv:0708.1919 MR2588543


- [7] C. Borgs, J. T. Chayes, H. Cohn, and Y. Zhao, An Lp theory of sparse graph convergence II: LD convergence, quotients, and right convergence, preprint, 2014. arXiv:1408.0744
- [8] C. Borgs, J. T. Chayes, L. Lova´sz, V. T. So´s, and K. Vesztergombi, Convergent sequences of dense graphs I: Subgraph frequencies, metric properties and testing, Adv. Math. 219 (2008), 1801–1851. arXiv:math/0702004 doi:10.1016/j.aim.2008.07.008 MR2455626
- [9] C. Borgs, J. T. Chayes, L. Lova´sz, V. T. So´s, and K. Vesztergombi. Convergent sequences of dense graphs II: Multiway cuts and statistical physics, Ann. of Math. (2) 176 (2012), 151–219. doi:10.4007/annals.2012.176.1.2 MR2925382
- [10] S. Chatterjee and S. R. S. Varadhan, The large deviation principle for the Erd˝osR´enyi random graph, European J. Combin. 32 (2011), 1000–1017. arXiv:1008.1946 doi:10.1016/j.ejc.2011.03.014 MR2825532
- [11] A. Clauset, C. R. Shalizi, and M. E. J. Newman, Power-law distributions in empirical data, SIAM Rev. 51 (2009), 661–703. arXiv:0706.1062 doi:10.1137/070710111 MR2563829
- [12] A. Coja-Oghlan, C. Cooper, and A. Frieze, An eﬃcient sparse regularity concept, SIAM J. Discrete Math. 23 (2010), 2000–2034. doi:10.1137/080730160 MR2594968
- [13] D. Conlon and J. Fox, Bounds for graph regularity and removal lemmas, Geom. Funct. Anal. 22 (2012), 1191–1256. arXiv:1107.4829 doi:10.1007/s00039-012-0171-x MR2989432
- [14] D. Conlon, J. Fox, and Y. Zhao, Extremal results in sparse pseudorandom graphs, Adv. Math. 256 (2014), 206–290. arXiv:1204.6645 doi:10.1016/j.aim.2013.12.004 MR3177293
- [15] D. Conlon, J. Fox, and Y. Zhao, A relative Szemere´di theorem, Geom. Funct. Anal., to appear. arXiv:1305.5440
- [16] R. Durrett, Probability: theory and examples, fourth edition, Cambridge University Press, Cambridge, 2010. MR2722836
- [17] H. Finner, A generalization of H¨older’s inequality and some probability inequalities, Ann. Probab. 20 (1992), 1893–1901. doi:10.1214/aop/1176989534 MR1188047
- [18] A. Frieze and R. Kannan, Quick approximation to matrices and applications, Combinatorica 19 (1999), 175–220. doi:10.1007/s004930050052 MR1723039
- [19] B. Green and T. Tao, The primes contain arbitrarily long arithmetic progressions, Ann. of Math. (2) 167 (2008), 481–547. doi:10.4007/annals.2008.167.481 arXiv:math/0404188 MR2415379
- [20] W. Hoeﬀding, The strong law of large numbers for U-statistics, North Carolina State University, Institute of Statistics Mimeograph Series No. 302, 1961. http://repository.lib.ncsu.edu/ dr/handle/1840.4/2128
- [21] S. Janson, Graphons, cut norm and distance, couplings and rearrangements, New York Journal of Mathematics, NYJM Monographs 4, State University of New York, University at Albany, Albany, NY, 2013. arXiv:1009.2376 MR3043217
- [22] Y. Kohayakawa, Szemere´di’s regularity lemma for sparse graphs, in F. Cucker and M. Shub, eds., Foundations of computational mathematics, pages 216–230, Springer, Berlin, 1997. doi:10.1007/978-3-642-60539-0 16 MR1661982

- [23] Y. Kohayakawa and V. R¨odl, Szemer´edi’s regularity lemma and quasi-randomness, in B. A. Reed and C. L. Sales, eds., Recent advances in algorithms and combinatorics, pages 289–351, CMS Books in Mathematics/Ouvrages de Math´ematiques de la SMC 11, Springer-Verlag, New York, 2003. doi:10.1007/0-387-22444-0 9 MR1952989

- [24] D. Kunszenti-Kov´acs, L. Lov´asz, and B. Szegedy, Multigraph limits, unbounded kernels,and Banach space decorated graphs, preprint, 2014. arXiv:1406.7846
- [25] L. Lov´asz, Large networks and graph limits, American Mathematical Society Colloquium Publications 60, American Mathematical Society, Providence, RI, 2012. MR3012035
- [26] L. Lov´asz and B. Szegedy, Limits of dense graph sequences, J. Combin. Theory Ser. B 96

(2006), 933–957. arXiv:math/0408173 doi:10.1016/j.jctb.2006.05.002 MR2274085

- [27] L. Lova´sz and B. Szegedy, Szemere´di’s lemma for the analyst, Geom. Funct. Anal. 17 (2007), 252–270. doi:10.1007/s00039-007-0599-6 MR2306658
- [28] E. Lubetzky and Y. Zhao, On replica symmetry of large deviations in random graphs, Random Structures Algorithms, to appear. arXiv:1210.7013 doi:10.1002/rsa.20536
- [29] R. Lyons, Asymptotic enumeration of spanning trees, Combin. Probab. Comput. 14 (2005), 491–522. arXiv:math/0212165 doi:10.1017/S096354830500684X MR2160416
- [30] M. Mitzenmacher, A brief history of generative models for power law and lognormal distributions, Internet Math. 1 (2004), 226–251. doi:10.1080/15427951.2004.10129088 MR2077227


- [31] J. Nesˇetrˇil and P. Ossona de Mendez, Sparsity. Graphs, structures, and algorithms, Algorithms and Combinatorics 28, Springer, Heidelberg, 2012. doi:10.1007/978-3-642-27875-4 MR2920058
- [32] J. Nesˇetrˇil and P. Ossona de Mendez, A model theory approach to structural limits, Comment. Math. Univ. Carolin. 53 (2012), 581–603. arXiv:1303.2865 MR3016428
- [33] J. Neˇsetˇril and P. Ossona de Mendez, A uniﬁed approach to structural limits and limits of graphs with bounded tree-depth, preprint, 2013. arXiv:1303.6471
- [34] J. Neˇsetˇril and P. Ossona de Mendez, Modeling limits in hereditary vlasses: reduction and application to trees, preprint, 2013. arXiv:1312.0441
- [35] A. Scott, Szemer´edi’s regularity lemma for matrices and sparse graphs, Combin. Probab. Comput. 20 (2011), 455–466. arXiv:1010.0628 doi:10.1017/S0963548310000490 MR2784637
- [36] E. Szemere´di, Regular partitions of graphs, in J.-C. Bermond, J.-C. Fournier, M. Las Vergnas, and D. Sotteau, eds., Proble`mes combinatoires et the´orie des graphes, pages 309–401, Colloque Inter. CNRS 260, CNRS, Paris, 1978. MR0540024
- [37] P. J. Wolfe and S. C. Olhede, Nonparametric graphon estimation, preprint, 2013. arXiv:1309.5936


Microsoft Research, One Memorial Drive, Cambridge, MA 02142 E-mail address: borgs@microsoft.com

Microsoft Research, One Memorial Drive, Cambridge, MA 02142 E-mail address: jchayes@microsoft.com

Microsoft Research, One Memorial Drive, Cambridge, MA 02142 E-mail address: cohn@microsoft.com

Department of Mathematics, Massachusetts Institute of Technology, Cambridge, MA 02139

E-mail address: yufeiz@mit.edu

