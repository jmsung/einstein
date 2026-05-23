---
type: source
kind: paper
title: How to determine if a random graph with a fixed degree sequence has a giant component
authors: Felix Joos, Guillem Perarnau, Dieter Rautenbach, Bruce Reed
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1601.03714v3
source_local: ../raw/2016-joos-how-determine-random-graph.pdf
topic: general-knowledge
cites:
---

# arXiv:1601.03714v3[math.CO]31Jan2017

## How to determine if a random graph with a ﬁxed degree sequence has a giant component

##### Felix Joos∗ Guillem Perarnau† Dieter Rautenbach‡ Bruce Reed§ February 1, 2017

###### Abstract

For a ﬁxed degree sequence D = (d1,...,dn), let G(D) be a uniformly chosen (simple) graph on {1,...,n} where the vertex i has degree di. In this paper we determine whether G(D) has a giant component with high probability, essentially imposing no conditions on D. We simply insist that the sum of the degrees in D which are not 2 is at least λ(n) for some function λ going to inﬁnity with n. This is a relatively minor technical condition, and when D does not satisfy it, both the probability that G(D) has a giant component and the probability that G(D) has no giant component are bounded away from 1.

### 1 Introduction

The traditional Erd˝s-R´enyi model of a random network is of little use in modelling the type of complex networks which modern researchers study. Such a graph can be constructed by adding edges one by one such that in every step, every pair of non-adjacent vertices is equally likely to be connected by the new edge. However, 21st century networks are of diverse nature and usually exhibit inhomogeneity among their nodes and correlations among their edges. For example, we observe empirically in the web that certain authoritative pages will have many more links entering them than typical ones. This motivates the study, for a ﬁxed degree sequence D = (d1,...,dn), of a uniformly chosen simple graph G(D) on {1,...,n} where the vertex i has degree di. In this paper, we study the existence of a giant component in G(D).

A heuristic argument suggests that a giant component will exist provided that the sum of the squares of the degrees is larger than twice the sum of the degrees. In 1995, Molloy and Reed essentially proved this to be the case provided that the degree sequence under consideration satisﬁed certain technical conditions [24]. This work has attracted considerable attention and has been applied to random models of a wide range of complex networks such as the World Wide Web or biological systems operating at a sub-molecular level [1, 2, 4, 27, 28]. Furthermore, many authors have obtained related results which formalize the Molloy-Reed heuristic argument under diﬀerent sets of technical conditions [5, 16, 18, 21, 25].

∗School of Mathematics, University of Birmingham, Birmingham, B15 2TT, UK. E-mail: f.joos@bham.ac.uk. This coauthor was supported by the EPSRC, grant no. EP/M009408/1.

†School of Mathematics, University of Birmingham, Birmingham, B15 2TT, UK. E-mail: p.melliug@gmail.com. This coauthor was supported by the European Research Council, ERC Grant Agreement no. 306349.

‡Institute of Optimization and Operations Research, Ulm University, Ulm, Germany. E-mail: dieter.rautenbach@uni-ulm.de

§CNRS, France; Kawarabayashi Large Graph Project, NII, Japan; IMPA, Brasil; E-mail: breed@sophia.inria.fr

Unfortunately, these technical conditions do not allow the application of such results to many degree sequences that describe real-world networks. While these conditions are of diﬀerent nature, here we exemplify their limitations with a well-known example, scale-free networks. A network is scale-free if its degree distribution follows a power-law, governed by a speciﬁc exponent. It is well-known that many real-world networks are scale-free and one of the main research topic in this area is to determine the exponent of a particular network. It has been observed that many scale-free networks have a fat-tailed power-law degree distribution with exponent between 2 and 3. This is the case of the World Wide Web, where the exponent is between 2.15 and 2.2 [9], or the Movie Actor network, with exponent 2.3 [3]. In scale-free networks with exponents between 2 and 3, the vertices of high degree (called hubs) have a crucial role in several of the network properties such as in the “small-world” phenomenon. However, one of the many technical conditions under the previous results on the existence of a giant component in G(D) hold, is that the vertices of high degree do not have a large impact on the structure of the graph. (In particular, it is required that there is no mass of edges in vertices of non-constant degree.) Hence, often these results cannot be directly applied to realworld networks where hubs are present and for each particular network ad-hoc approaches are needed (see e.g. the Aiello-Chung-Lu model for the case of scale-free networks [1]).

Another problem is that all the previous results apply to a sequence of degree sequences (Dn)n≥1 satisfying various technical conditions instead of a single degree sequence D. Finally, all the previous results on the existence of a giant component in G(D) do not cover degree sequences where most of the vertices have degree 2.

In this paper we characterize when G(D) has a giant component for every feasible1 degree sequence D of length n. We only require that the sum of the degrees in the sequence which are not 2 is at least λ(n) for some arbitrary function λ going to inﬁnity with n. Besides the fact that it is a relatively minor technical condition, we also show that if it is not satisﬁed, both the probability that G(D) has a giant component and the probability that G(D) has no giant component are bounded away from 1.

It turns out that the heuristic argument which was used in [24] to describe the existence of a giant component in G(D) for degree sequences satisfying some technical conditions and that was generalized in the subsequent papers [5, 16, 18, 21, 25], actually suggests the wrong answer for general degree sequences. Precisely, if we let S be a smallest set such that (i) no vertex outside of S has degree bigger than a vertex in S, and (ii) the sum of the squares of the degrees of the vertices outside of S is at most twice the sum of their degrees, then whether or not a giant component exists depends on the sum of the degrees of the vertices in S, not on the sum of the squares of the degrees of the vertices in S as suggested by this heuristic argument

This new uniﬁed criterion on the existence of a giant component in G(D) is valid for every sequence D and implies all the previous results on the topic both for arbitrary degree sequences [5, 18, 24] or for particular models [1].

#### 1.1 The Molloy-Reed Approach

Let us ﬁrst describe the result of Molloy and Reed [24]. For every 1 ≤ i ≤ n, one can explore the component containing a speciﬁc initial vertex i of a graph on {1,...,n} via breadth-ﬁrst search. Initially we have di “open” edges out of i. Upon exposing the other endpoint j of such an open edge, it is no longer open, but we gain dj − 1 open edges out of j. Thus, the number of open edges has increased by dj − 2 (note that this is negative if dj = 1).

1A degree sequence is feasible if there is a graph with the given degree sequence.

One can generate the random graph G(D) for D = (d1,...,dn) and carry out this exploration at the same time, by choosing each vertex as j with the appropriate probability.

Intuitively speaking, the probability we pick a speciﬁc vertex j as the other endpoint of the ﬁrst exposed edge is proportional to its degree. So, the expected increase in the number of open edges in the ﬁrst step is equal to k∈{1,..,n},k =i dk(dk−2)

k∈{1,..,n},k =i dk . Thus, it is positive essentially if and only if the sum of the squares of the degrees exceeds twice the sum of the degrees.

Suppose that this expected increase remains the same until we have exposed a linear number of vertices. It seems intuitively clear that if the expected increase is less than 0, then the probability that initial vertex i is in a linear order component is o(1), and hence the probability that G(D) has no linear order component is 1−o(1). If for some positive constant

, the expected increase is at least , then there is some γ = γ( ) > 0 such that the probability that i is in a component with at least γn vertices exceeds γ.

In [24], Molloy and Reed proved, subject to certain technical conditions which required them to discuss sequences of degree sequences rather than one single degree sequence, that we essentially have that (i) if

n k=1 dk(dk−2)

k=1 dk > for some > 0, then the probability that G(D) has a giant component is 1 − o(1), and (ii) if

n

n k=1 dk(dk−2)

k=1 dk < − for some > 0, then the probability that G(D) has no giant component is 1−o(1). We present their precise result and some of its generalizations later in this introductory section.

n

#### 1.2 Our Reﬁnement

It turns out that, absent the imposed technical conditions, the expected increase may change drastically during the exploration process. Consider for example the situation in which n = k2 for some large odd integer k, d1 = d2 = .. = dn−1 = 1 and dn = 2k. Then

n k=1 dk(dk−2)

k=1 dk = 4k2−4k−(n−1)

n

2k+n−1 ≈ 3, and so the Molloy-Reed approach would suggest that with probability 1 − o(1) there is a giant component. However, with probability 1, G(D) is the disjoint union of a star with 2k leaves and n−22k−1 components of order 2 and hence it has no giant component. The problem is that as soon as we explore vertex n, the expected increase drops from roughly

###### 3 to −1, so it does not stay positive throughout (the beginning of) the process. Thus, we see that the Molloy-Reed criterion cannot be extended for general degree se-

quences. To ﬁnd a variant which applies to arbitrary degree sequences, we need to characterize those for which the expected increase remains positive for a suﬃciently long time.

Intuitively, since the probability that we explore a vertex is essentially proportional to its degree, in lower bounding the length of the period during which the expected increase remains positive, we could assume that the exploration process picks at each step a highest degree vertex that has not been explored yet. Moreover, note that vertices of degree 2 have a neutral role in the exploration process as exposing such a vertex does not change the number of open edges, provided we assume that our component locally looks like a tree (which turns out to be a good approximation around the critical window). These observations suggest that we should focus on the following invariants of D deﬁned by considering a permutation π of the vertices that satisﬁes dπ1 ≤ ... ≤ dπn:

- - jD = min j : j ∈ [n] and

j

i=1

dπi(dπi − 2) > 0 ∪ n ,

- - RD =


n

dπi, and

i=jD

- - MD = i∈[n]: di =2


di.

We emphasize that these invariants are determined by the multiset of the degrees given by D and are independent from the choice of π subject to dπ1 ≤ ... ≤ dπn.

Our intuition further suggests that in the exploration process, the expected increase in the number of open edges will be positive until we have explored RD edges and will then become negative. Thus, we might expect to explore a component with about RD edges, and indeed we can show this is the case.

This allows us to prove our main result which is that whether G(D) has a giant component essentially depends on whether RD is of the same order as MD or not. There is however a caveat, this is not true if essentially all vertices have degree 2.

For any function λ : N → N, we say a degree sequence D is λ-well-behaved or simply well-behaved if MD is at least λ(n). Our main results hold for any function λ → ∞ as n → ∞.

- Theorem 1. For any function δ → 0 as n → ∞, for every γ > 0, if D is a well-behaved

feasible degree sequence with RD ≤ δ(n)MD, then the probability that G(D) has a component of order at least γn is o(1).

- Theorem 2. For any positive constant , there is a γ > 0, such that if D is a well-behaved

feasible degree sequence with RD ≥  MD, then the probability that G(D) has a component of order at least γn is 1 − o(1).

As we shall see momentarily, previous results in this ﬁeld apply to sequences of degree sequences, and required that both the proportion of elements of a given degree and the average degree of an element of the degree sequences in the sequence approaches a limit in some smooth way. We can easily deduce results for every sequence of (feasible) degree sequences from the two theorems above, and from our results on degree sequences which are not well-behaved, presented in the next section.

We denote by D = (Dn)n≥1 a sequence of degree sequences where Dn has length n. We say that D is well-behaved if for every b, there is an nb such that for all n > nb, we have MDn > b; D is lower bounded if for some > 0, there is an n such that for all n > n , we have RDn ≥  MDn; and D is upper bounded if for every > 0, there is an n such that for all n > n , we have RDn ≤  MDn.

The following is an immediate consequence of Theorem 1 and 2, and Theorem 6, which will be presented in the next section.

- Theorem 3. For any well-behaved lower bounded sequence of feasible degree sequences D, there is a γ > 0 such that the probability that G(Dn) has a component of order at least γn is


- 1 − o(1). For any well-behaved upper bounded sequence of feasible degree sequences D and every


γ > 0, the probability that G(Dn) has a component of order at least γn is o(1).

If a sequence of feasible degree sequences D is either not well behaved or neither upper bounded nor lower bounded, then for every suﬃciently small positive γ, there is a 0 < δ < 1 such that there are both arbitrarily large n for which the probability that G(Dn) has a component of order at least γn is at least δ, and arbitrarily large n for which the probability that G(Dn) has a component of order at least γn is at most 1 − δ.

#### 1.3 The Special Role of Vertices of Degree 2

At ﬁrst glance, it may be surprising that the existence of a giant component depends on the ratio between RD and MD rather than the ratio between RD and ni=1 di. It may also be unclear why we have to treat diﬀerently degree sequences where the sum of the degrees which are not 2 is bounded.

To clarify why our results are stated as they are, we now highlight the special role of vertices of degree 2.

The non-cyclic components2 of G(D) can be obtained by subdividing the edges of a multigraph H(D) none of whose vertices have degree 2 so that every loop is subdivided at least twice, and all but at most one edge of every set of parallel edges is subdivided at least once. Note that H(D) can be obtained from G(D) by deleting all cyclic components and suppressing all vertices of degree 2.3 Clearly, H(D) is uniquely determined by G(D). Moreover, the degree sequence of H(D) is precisely that of G(D) without the vertices of degree 2.

The number of vertices of a non-cyclic component of G(D) equals the sum of the number of vertices of the corresponding component of H(D) and the number of vertices of degree 2 used in subdividing its edges. Intuitively, the second term in this sum depends on the proportion of the edges in the corresponding component of H(D). Subject to the caveat mentioned above and discussed below, if the number of vertices of degree 2 in G(D) is much larger than the size4 of H(D), then the probability that G(D) has a giant component is essentially the same as the probability H(D) has a component containing a positive fraction of its edges. The same is true, although not as immediately obvious, even if the number of vertices of degree 2 is not this large.

- Theorem 4. For every γ > 0, there exists a ρ > 0 such that for every well-behaved feasible degree sequence D, the probability that G(D) has a component of order at least γn and H(D) has no component of size at least ρMD is o(1).
- Theorem 5. For every ρ > 0, there exists a γ > 0 such that for every well-behaved feasible degree sequence D, the probability that G(D) has no component of order at least γn and H(D) has a component of size at least ρMD is o(1).

As we mentioned above, degree sequences which are not well behaved behave diﬀerently from well-behaved degree sequences. For instance, suppose that MD = 0. Then H(D) is empty and G(D) is a uniformly chosen disjoint union of cycles. In this case it is known that the probability of having a giant component is bounded away both from 0 and 1. Indeed, the latter statement also holds whenever MD is at most b for any constant b.

- Theorem 6. For every b ≥ 0 and every 0 < γ < 18, there exist a positive integer nb,γ and a 0 < δ < 1 such that if n > nb,γ and D is a degree sequence with MD ≤ b, then the probability that there is a component of order at least γn in G(D) lies between δ and 1 − δ.


This theorem both explains why we concentrate on well-behaved degree sequences and sets out how degree sequences which are not well-behaved actually behave (badly obviously). Combining it with Theorem 1 and 2, it immediately implies Theorem 3. We omit the straightforward details.

2A component is cyclic if it is a cycle and non-cyclic if it is not. 3Here and throughout the paper, when we say we suppress a vertex u of degree 2, this means we delete u

and we add an edge between its neighbours. Observe that this may create loops and multiple edges, so the resulting object might not be a simple graph.

4As it is standard, we use order and size to denote the number of vertices and the number of edges of a graph, respectively.

#### 1.4 Previous Results

The study of the existence of a giant component in random graphs with an arbitrary prescribed degree sequence5, started with the result of Molloy and Reed [24]. Although they deﬁne the concept of asymptotic degree sequences, we will state all the previous results in terms of sequences of degree sequences D = (Dn)n≥1. Using a symmetry argument, one can easily translate results for sequences of degree sequences to asymptotic degree sequences, and vice versa. For every Dn = (d(1n),...,dn(n)), we deﬁne ni = ni(n) = |{j ∈ [n] : d(jn) = i}|. Recall that we only consider degree sequences such that n0 = 0.

Before stating their result, we need to introduce a number of properties of sequences of degree sequences. A sequence of degree sequences D is

- - feasible, if for every n ≥ 1, there exists at least one simple graph on n vertices with degree sequence Dn.
- - smooth, if for every nonnegative integer i ≥ 0, there exists λi ∈ [0,1] such that limn→∞ nni = λi.

- - sparse, if there exists λ ∈ (0,∞) such that limn→∞ i≥1 inni = λ.

- - f-bounded, for some function f : N → R, if ni = 0 for every i > f(n).


In particular, observe that random graphs G(Dn) arising from a sparse sequence of degree sequences D have a linear number of edges, provided that n is large enough. Given that D is smooth, we deﬁne the following parameter

i(i − 2)λi .

Q(D) =

i≥1

Note that Q(D) is very close to the notion of initial expected increase described in Section 1.1. We say a sequence of degree sequences D satisﬁes the MR-conditions if

- (a.1) it is feasible, smooth and sparse,
- (a.2) it is n1/4− -bounded, for some > 0,
- (a.3) for every i ≥ 1, i(i−n2)ni converges uniformly to i(i − 2)λi, and

- (a.4) limn→∞ i≥1 i(i − 2)nni exists and converges uniformly to i≥1 i(i − 2)λi. For a precise statement of the uniform convergence on conditions (a.3)–(a.4), we refer the


reader to [24]. Note that these conditions imply that λ = i≥1 iλi. Now we can precisely state the result of Molloy and Reed [24].

- Theorem 7 (Molloy and Reed [24]). Let D = (Dn)n≥1 be a sequence of degree sequences that satisﬁes the MR-conditions. Then,


- 1. if Q(D) > 0, then there exists a constant c1 > 0 such that the probability that G(Dn) has a component of order at least c1n is 1 − o(1).
- 2. if Q(D) < 0 and the sequence is n1/8− -bounded for some > 0, then for every constant c2 > 0, the probability that G(Dn) has no component of order at least c2n is 1 − o(1).


5Random graphs with special degree sequences had been studied earlier (see, e.g. [22, 33]).

Note that the case λ2 = 1 is not considered in Theorem 7, since λ2 = 1 implies Q(D) = 0.

Theorem 7 has been generalized to other sequences of degree sequences, which in particular include the case Q(D) = 0. In Section 8, we show that Theorem 3 implies all the criteria for the existence of a giant component in G(Dn) introduced below.6

We say a sequence of degree sequences D satisﬁes the JL-conditions if

- (b.1) is feasible, smooth, and sparse,
- (b.2) i≥1 i2ni = O(n), and
- (b.3) λ1 > 0.


Observe that if D satisﬁes the JL-conditions, then, by (b.2), it is also O(n1/2)-bounded. Moreover, they also imply that λ = i≥1 iλi. Janson and Luczak in [18] showed that one can prove a variant of Theorem 7 obtained by replacing the MR-conditions by the JL-conditions.7 They also note that if λ2 = 1, then the criterion based on Q(D) does not apply. Our results completely describe the case λ2 = 1.

We say a sequence of degree sequence D satisﬁes the BR-conditions if

- (c.1) it is feasible, smooth and sparse,
- (c.2) i≥3 λi > 0, and
- (c.3) λ = i≥1 iλi.


Bollob´s and Riordan in [5] proved a version of Theorem 7 for sequences of degree sequences obtained by replacing the MR-conditions by the BR-conditions.8

Theorem 7 and its extensions provide easy-to-use criteria for the existence of a giant component and have been widely used by many researchers in the area of complex networks [2, 4, 27]. However, the technical conditions on D to which they can be applied, restrict its applicability, seem to be artiﬁcial and are only required due to the nature of the proofs. It turns out to be the case that many real-world networks do not satisfy these conditions. For this reason, researchers have developed both ad-hoc approaches for proving results for speciﬁc types of degree sequences and variants of the Molloy-Reed result which require diﬀerent sets of technical conditions to be satisﬁed.

An early example of an ad-hoc approach is the work of Aiello, Chung and Lu on PowerLaw Random Graphs [1]. They introduce a model depending on two parameters α,β >

- 0 that deﬁne a degree sequence satisfying ni = eαi−β . One should think about these parameters as follows: α is typically large and determines the order of the graph (we always have α = Θ(log n)), and β is a ﬁxed constant that determines the power-decay of the degree distribution. Among other results, the authors prove that there exists β0 > 0, such that if β > β0 the probability that there is a component of linear order is o(1) and if β < β0 the probability there is a component of linear order is 1 − o(1). Here, the previous conditions are only satisﬁed for certain values of β and the authors need to do additional work to determine when a giant component exists for other values of β. In Section 8 we will show how Theorem 3


6Note that some of these results give a more precise description on the order of the largest component. Our results only deal with the existential question.

- 7Their result gives convergence in probability of the proportion of vertices in the giant component and they

also consider the case Q(D) = 0.

- 8They also proved some results on the distribution of the order of the largest component and also consider


the case Q(D) = 0.

also implies Aiello-Chung-Lu results on the existence of a giant component in the model of Power-Law Random Graphs.

#### 1.5 Future Directions

Beginning with the early results of Molloy and Reed, the study of the giant component in random graphs with prescribed degree sequence has attracted a lot of attention. Directions of study include determining the asymptotic order of the largest component in the subcritical regime or estimating the order of the second largest component in both regimes [5, 16, 18, 20, 21, 25, 30]. It would be interesting to extend these known results to arbitrary degree sequences.

For example, Theorem 1 and 2 precisely describe the appearance of a giant component when the degree sequence is well-behaved. While bounds on the constant γ in terms of δ and respectively, may follow from their respective proofs, these bounds are probably not of the right order of magnitude. Molloy and Reed in [25], precisely determined this dependence for sequences of degree sequences that satisfy the MR-conditions. Precise constants are also given in [5, 14, 18]. We wonder whether it is possible to determine the precise dependence on the parameters for arbitrary degree sequences. It is likely that our methods can be used to ﬁnd this dependence and to determine the order of the second largest component when a giant one exists.

Another direction is the study of site and bond percolation in G(D) for arbitrary degree sequences D. This problem has been already approached for sequences of degree sequences that satisfy certain conditions similar to the ones presented in Section 1.4 [5, 13, 17, 30].

Motivated by some applications in peer-to-peer networks (see, e.g. [6]), one can study eﬃcient sampling of the random graph G(D). Cooper et al. [8] showed that the switching chain rapidly mixes for d-regular graphs for every 3 ≤ d ≤ n − 1. Greenhill [15] recently extended this result to G(D), but, due to some technical reasons, this result only holds if the maximum degree in D is small enough.

Many other basic properties of G(D), such as determining its diameter [11, 31, 32] or the existence of giant cores [7, 10, 19], have already been studied for certain sequences of degree sequences. We believe that our method can help to extend these results to arbitrary degree sequences.

2 A Proof Sketch

#### 2.1 The Approach

The proofs of Theorem 4, 5 and 6 are simpler than the remaining proofs and we delay any discussion of these results to Section 6 and 7. By applying them, we see that in order to prove Theorem 1 and 2 it is enough to prove the following results:

- Theorem 8. For any function δ → 0 as n → ∞ and for every γ > 0, if D is a well-behaved degree sequence with RD ≤ δ(n)MD, then the probability that H(D) has a component of size at least γMD is o(1).
- Theorem 9. For any positive constant , there is a γ > 0 such that if D is a well-behaved degree sequence with RD ≥  MD, then the probability that H(D) has a component of size at least γMD is 1 − o(1).


The proofs of both theorems analyse an exploration process similar to the one discussed in Section 1.1 by combining probabilistic tools with a combinatorial switching argument. However, we will focus on the edges of H(D) rather than the ones of G(D). Again, we will need to bound the expected increase of the number of open edges throughout the process and prove that the (random) increase is highly concentrated around its expected value. In order to do so, we will need to bound the probability that the next vertex of H(D) explored in the process, is a speciﬁc vertex w. One of the key applications of our combinatorial switching technique will be to estimate this probability and show that it is approximately proportional to the degree of w.

Crucial to this approach is that the degrees of the vertices explored throughout the process are not too high. Standard arguments for proving concentration of a random variable require that the change at each step is relatively small. This translates precisely to an upper bound on the maximum degree of the explored graph. Furthermore, without such a bound on the maximum degree, we cannot obtain good bounds on the probability that a certain vertex w is the next vertex explored in the process. So, a second key ingredient in our proofs will be a preprocessing step which allows us to handle the vertices of high degree, ensuring that we will not encounter them in our exploration process.

#### 2.2 The Exploration Process

We consider a variant of the exploration process where we start our exploration at a non-empty set S0 of vertices of H(D), rather than at just one vertex.

Thus, we see that the exploration takes |V (H(D)) \ S0| steps and produces sets S0 ⊂ S1 ⊂ S2 ⊂ ... ⊂ S|V (H(D))\S0| ,

where wt = St \ St−1 is either a neighbour of a vertex vt of St−1 or is a randomly chosen vertex in V (H(D)) \ St−1 if there are no edges between St−1 and V (H(D)) \ St−1.

To specify our exploration process precisely, we need to describe how we choose vt and wt. To aid in this process, for each vertex v ∈ V (H(D)) we will choose a uniformly random permutation of its adjacency list in G(D). For this purpose, an input of our exploration process consists of a graph G equipped with an ordering of its adjacency lists for all vertices v ∈ V (H(D)). Applying the method of deferred decisions (cf. Section 2.4 in [26]), we can generate these random linear orders as we go along with our process. We note that this yields, in a natural manner, an ordering of the non-loop edges of H(D) which have the vertex v as an endpoint. If there are no edges between St−1 and V (H(D)) \ St−1, we choose each vertex of V (H(D)) \ St−1 to be wt with probability proportional to its degree. Otherwise we choose the smallest vertex vt of St−1 (with respect to the natural order in {1,...,n}), which has a neighbour in V (H(D)) \ St−1. We expose the edge of H(D) from vt to V (H(D)) \ St−1 which appears ﬁrst in our random ordering and let wt be its other endpoint. Furthermore, we expose all the edges of H(D) from wt to St−1 \ {vt} as well as the loops incident to wt. Finally, we expose the paths of G(D) corresponding to the edges of H(D) which we have just exposed and the position in the random permutation of the adjacency list of wt in G(D) of the edges we have just exposed.

Thus, after t iterations of our exploration process we have exposed

- • the subgraph of H(D) induced by St,
- • the paths of G(D) corresponding to the exposed edges of H(D), and


- • where each initial and ﬁnal edge of such a path appears in the random permutation of the adjacency list of any of its endpoints which is also an endpoint of the path.


We refer to this set of information as the conﬁguration Ct at time t. A conﬁguration can also be understood as a set of inputs. During our analysis of the exploration process, we will consider all the probabilities of events conditional on the current conﬁguration.

An important parameter for our exploration process is the number Xt of edges of H(D) between St and V (H(D))\St. We note that if Xt = 0, then St is the union of some components of H(D) containing all of S0. We note that if |S0| = 1, then every Xt is a lower bound on the maximum size of a component of H(D) (not necessarily the one containing the vertex in S0).

We prove Theorem 8 by showing that under its hypotheses for every vertex v of H(D), there is a set S0 = S0(v) containing v such that, given we start our exploration process with S0, the probability that there is a t with Xt = 0 for which the number of edges within St is at most γMD, is 1 − o(MD−1). Since H(D) has at most 2MD vertices, it follows that the probability that H(D) has a component of size at least γMD is o(1). The set S0 \ {v} is a set of highest degree vertices the sum of whose degrees exceeds RD. By the deﬁnition of jD and RD, this implies that, unless X0 = 0, the expectation of X1 − X0 is negative. We show that, as the process continues, the expectation of Xt − Xt−1 becomes even smaller. We can prove that the actual change of Xt is highly concentrated around its expectation and hence complete the proof, because S0 contains all the high degree vertices and so in the analysis of our exploration process we only have to deal with low degree vertices.

We prove (a slight strengthening of) Theorem 9 for graphs without large degree vertices by showing that under its hypotheses and setting S0 to be a random vertex v chosen with probability proportional to its degree, with probability 1−o(1), there exists some t such that Xt ≥ γMD (and hence there is a component of H(D) of size at least γMD). Key to doing so is that the expected increase of Xt is a positive fraction of the increase in the sum of the degrees of the vertices in St until this sum approaches RD. To handle the high degree vertices, we expose the edges whose endpoints are in components containing a high degree vertex. If this number of edges is at least a constant fraction of MD, then we can show that in fact all the high degree vertices lie in one component, which therefore contains a constant fraction of the edges of H(D). Otherwise, we show that the conditions of Theorem 9 (slightly relaxed) hold in the remainder of the graph, which has no high degree vertices, so we can apply (a slight strengthening of) Theorem 9 to ﬁnd the desired component of H(D).

### 3 Switching

As mentioned above, the key to extending our branching analysis to arbitrary well-behaved degree sequences is a combinatorial switching argument. In this section, we describe the type of switchings we consider and demonstrate the power of the technique.

Let H be a multigraph. We say a multigraph H is obtained by switching from H on a pair of orientated and distinct edges uv and xy if H can be obtained from H by deleting uv and xy as well as adding the edges ux and vy. Observe that switching ux and vy in H yields H. Observe further that if H is simple and we want to ensure that H is simple, then we must insist that u = x, v = y and, unless u = y or v = x, the edges ux and vy are not edges of H.

Switching was introduced in the late 19th century by Petersen [29]. Much later, McKay [23] reintroduced the method to count graphs with prescribed degree sequences and, together with Wormald, used it in the study of random regular graphs. We refer the interested reader to the survey of Wormald on random regular graphs for a short introduction to the method [34].

In this paper we will consider standard switchings as well as a particular extension of

- them. This extension concerns pairs consisting of a simple graph G and the multigraph HG obtained from G by deleting its cyclic components and suppressing the vertices of degree 2 in the non-cyclic ones. For certain switchings of HG which yield H , our extension constructs a simple graph G from G such that HG = H . We now describe for which switchings in HG we can obtain such an H and how we do so.


Our extension considers directed walks (either a path or a cycle) of G which correspond to (oriented) edges in HG, (note that an edge of HG corresponds to exactly two such directed walks, even if it is a loop and hence has only one orientation). We can switch on an ordered pair of such directed walks in G, corresponding to an ordered pair of orientated distinct edges

- e1 = uv and e2 = xy of HG, such that none of the following hold:


- (i) there is an edge of G between u and x which forms neither e1 nor e2, and the walk

- corresponding to e1 has one edge,

(ii) there is an edge of G between v and y which forms neither e1 nor e2 and the walk

- corresponding to e2 has one edge,


- (iii) u = x and the directed walk corresponding to e1 has at most two edges, or
- (iv) v = y and the directed walk corresponding to e2 has at most two edges.


To do so, let u = w0,w1,...,wr = v be the directed walk corresponding to e1 and let x = z0,z1,...,zs = y be the directed walk corresponding to e2. We delete the edges wr−1v and xz1 and add the edges wr−1x and vz1.

We note that (i)-(iv) ensure that we obtain a simple graph G . Furthermore, we have that HG is obtained from HG by switching on uv and xy. We remark further that if we reverse both the ordering of the edges and the orientation of both edges, we always obtain the same graph G ; that is, it is equivalent to switch the ordered pair (uv,xy) or the ordered pair (yx,vu). Therefore, given two walks between u and v and between x and y (either paths or cycles) of G, we always consider the four following possible switches: (uv,xy), (uv,yx), (vu,xy) and (vu,yx). We note that some of these choices might give rise to the same graph G . However, we consider each of them as a valid switch since it will be simpler to count them considering these multiplicities.

Given any two disjoint sets of (multi)graphs A and B, we can build an auxiliary bipartite graph with vertex set A ∪ B where we add an edge between H ∈ A and H ∈ B for every (extended) switching that transforms H into H , or equivalently, H into H. We can also consider subgraphs of this auxiliary graph where we only add an edge if the switching satisﬁes some special property. Given a lower bound dA on the degrees in A and an upper bound dB on the degrees in B, we obtain immediately that |A| ≤ ddB

|B|. We frequently use this fact without explicitly referring to it.

A

To illustrate our method, we show here that if MD is large with respect to the number of vertices, then there exists a component containing most of the vertices.

- Lemma 10. If MD ≥ nlog log n, then the probability that G(D) has a component of order (1 − o(1))n is 1 − o(1).


In proving the lemma, we will need the following straightforward result on 2-edge cuts of graphs. We defer its proof to the end of the section.

Figure 1: A graph G and its corresponding graph HG before and after switching the directed walks corresponding to ordered pair of oriented edges uv and xy in HG.

- Lemma 11. The number of pairs of orientations of edges uv,xy in a graph G of order n such that by switching on uv and xy we obtain a graph with one more component than G is at most 8n2.


- Proof of Lemma 10. We can assume n is large enough to satisfy an inequality stated below


since the lemma makes a statement about asymptotic behaviour. Let K = (1 − √log log1 n)n . For every integer k ≥ 1, let Fk be the event that G(D) has exactly k components and let F k be the event that G is in Fk and that all components of G have order at most K. Denote by F = ∪k≥2F k. Our goal is to show that P[F ] = o(1). If so, with high probability G has a component of order larger than K. Observe that if one proves for some function

- f : N → R+ with f(n) → 0 as n → ∞ that P[F k+1] ≤ f(n)P[Fk] for every k ≥ 1, then P[F ] = k≥1 P[F k+1] ≤ f(n) k≥1 P[Fk] = f(n) = o(1). We adopt this approach with


f(n) = √log log16 n.

Fix k ≥ 1. Now suppose that there exist s+ and s− such that for every G in Fk, there are at most s+ switchings that transform G into a graph in F k+1, and for every graph G in F k+1, there are at least s− switchings that transform G into a graph in Fk. Then,

P[F k+1]s− ≤ P[Fk]s+ .

Let us now obtain some values for s+ and s−. On the one hand, applying Lemma 11, we can choose

s+ = 8n2 .

On the other hand, if G is in F k+1, in order to merge two components it is enough to perform a switching between an oriented non-cut edge (at least MD − 2n ≥ (log log n − 2)n choices) and any other oriented edge not in the same component as the ﬁrst one (since G has minimum degree at least 1 and the largest component has order at most K, there are at least n − K choices). Since n is large, we can choose

√log log n 2

s− = (log log n − 2)n · (n − K) ≥

n2 .

From the previous bounds, we obtain the desired result

s+ s− · P[Fk] ≤

16 √log log n · P[Fk] .

P[F k+1] ≤

| |
|---|


- Proof of Lemma 11. Any such pair of oriented edges must lie in the same component and swapping on them within the component must yield a disconnected graph. So, as the function x  → 4x2 is convex, we may assume that G is connected.


First, suppose that at least one of the oriented edges, say uv, is an edge cut of the graph. Then, if xy is not an edge cut of G, the switching does not disconnect the graph. Since there are at most n − 1 cut-edges, there are at most 4(n − 1)2 switchings using at least one (and hence two) oriented cut-edges.

Otherwise {uv,xy} is a proper 2-edge cut (that is, both G−uv and G−xy are connected). Consider an arbitrary spanning tree of G. This tree contains at least one edge of every 2-edge cut of G. Thus, select uv among these edges (exactly (n − 1) choices). Observe now that, in order to construct the proper 2-edge cut, we need to select xy as a cut-edge in G − uv (at most (n − 1) choices).

Therefore, in total there are at most 8n2 switchings in G which disconnect it.

| |
|---|


- 4 The Proof of Theorem 8 Theorem 8 follows immediately from the following result.


- Lemma 12. For every suﬃciently small ω > 0 and every degree sequence D such that RD ≤ ωMD and MD is suﬃciently large in terms of ω, for every vertex v of H(D), the probability


1/4

that v lies in a component of H(D) of size larger than ω1/9MD is less than e−M

D .

In order to prove this lemma, we analyse our random exploration process on H(D) using a set S0 of vertices including v and show that the probability that there is a t with Xt = 0 and such that there are at most ω1/9MD edges in the graph induced by St in H(D), is at least

1/4

- 1 − e−M


D .

Since it is diﬃcult to keep track of Xt, we will instead focus on the random variable X t (deﬁned below), which overestimates Xt until Xt = 0. Clearly, X0 is at most

X 0 =

d(u) .

u∈S0

Provided that Xt−1 > 0, the edge vtwt is an edge of H(D), and we can upper bound Xt by

t

(d(wi) − 2) .

X t = X 0 +

i=1

Observe that, provided that Xt−1 > 0, the process X t coincides with Xt if the explored components are trees and S0 is a stable set. More importantly, we observe that if X t = 0,

- then there is a t ≤ t for which Xt = 0. We note further that the number of edges in the graph induced by St in H(D) is at most X t +2t, so we only need to show that the probability


1/4

that there is no t < ω1/29M for which X t = 0 is less than e−M

D .

As suggested by our introductory discussion and proven below, the probability that wt is a speciﬁc vertex w in V (H(D))\St−1 is essentially proportional to the degree of w. Therefore, the expected value of X t − X t−1 = d(wt) − 2 is with high probability close to

1

d(w)(d(w) − 2).

d(w)

w∈V (H(D))\St−1

w∈V (H(D))\St−1

By putting the high degree vertices of H(D) into S0 \{v}, we can ensure that the expectation of X 1 −X 0 is negative. The fact that, if the process has not died out by time t, then the sum of the degrees of the vertices we picked cannot be much less than 2t, allows us to obtain a bound on the expectation of X t − X t−1 which decreases as t increases. Having all the high degree vertices in S0 facilitates our analysis of the exploration process, and allows us to show that the probability that X t drops to 0 before the number of edges in the graph induced by St in H(D) is at least ω1/9MD, is more than 1 − e−M

1/4

D . Forthwith the details.

We use H for H(D), V for V (H(D)), M for MD, R for RD and G for G(D). We implicitly assume that ω is small enough and M is large enough in terms of ω to ensure various inequalities scattered throughout the proof are satisﬁed.

Let S be a smallest set of vertices of H such that i∈S di ≥ 5ω1/4M and there is no vertex outside of S with degree bigger than a vertex in S. Since the sum of the degrees of the vertices in H is M > 5ω1/4M, such a set S exists. Furthermore, since R ≤ ωM < 5ω1/4M, the deﬁnition of jD implies that w∈V \S d(w)(d(w) − 2) ≤ 0. It is straightforward to prove,

- as we do below, the following strengthening, which is important for our analysis.


###### Lemma 13. We have

- (a) w∈V \S

d(w)(d(w) − 2) ≤ −4ω1/4M, and

- (b) there is a vertex of S with degree at most ω−1/4.


The sum of the degrees in S is at most the sum of 5ω1/4M and the minimum degree in S. Let S0 = S ∪ {v}. Since every vertex not in S has degree at most the minimum degree in S and X 0 is the sum of the degrees of the vertices in S ∪ {v}, the following observation holds.

###### Observation 14. We have

- (a) d(u) ≤ ω−1/4 for every u ∈ V \ S0, and
- (b) X 0 ≤ 7ω1/4M.


As we carry out our process, we let Yt = X t − X t−1 − E[d(wt) − 2], where the expectation is conditional on Ct. By construction E[Yt] = 0 and by Lemma 13 (b), the absolute value of Yt is bounded from above by ω−1/4. As we explain below, by applying Azuma’s Inequality we immediately obtain:

- Lemma 15. The probability that there is a t such that t ≤t Yt > M2/3 is less than e−M1/4.


Thus, in order to bound X t from above, we need to bound E[d(wt)] from above for each t ≥ 1. Letting Mt−1 be the sum of the degrees of the vertices of H which are not in St−1 and using our swapping arguments, we can prove the following result, which will be useful to give a precise estimation for E[d(wt)].

- Lemma 16. If t ≤ ω1/9M and X t−1 ≤ ω1/5M, and Xt > 0 for all t < t, then the following statements hold:

- (a) If w ∈ V \ St−1 and d(w) = 1, then

P[wt = w] ≥ 1 − 9ω1/5

1 Mt−1

.

- (b) If w ∈ V \ St−1, then


P[wt = w] ≤ 1 + 9ω1/5

d(w) Mt−1

.

Iteratively applying this result to bound E[d(wt)], we obtain:

- Lemma 17. Letting τ be the minimum of ω1/29M and the ﬁrst t for which t ≤t Yt > M2/3 or Xt = 0, we have the following for all t ≤ τ:

E[d(wt) − 2] ≤ −

t M

+ 19ω1/5. The next lemma completes the proof of Lemma 12 and thus, of Theorem 8.

- Lemma 18. With probability greater than 1 − e−M1/4, there exists t ≤ ω1/39M such that Xt = 0. Proof. By Lemma 15, with probability greater than 1 − e−M1/4 there is no t such that


t ≤t Yt > M2/3. If this event holds, and there is no t ≤ ω1/39M for which Xt = 0, then by applying Lemma 17 we see that for every such t,

t(t − 1) 2M

+ 19ω1/5t + M2/3.

Xt ≤ X t ≤ X 0 −

Since X 0 ≤ 7w1/4M, it follows that for t = ω1/39M , we have Xt < 0, which is a contradiction.

| |
|---|


Therefore, it only remains to prove Lemma 13, 15, 16, and 17.

- 4.1 The Details We start with some simple observations.


- Observation 19. The maximum degree dπn of H is at most ωM. Proof. By deﬁnition, jD ≤ n, which implies dπn ≤ R ≤ ωM.

| |
|---|


We let n1 be the number of vertices of degree 1 in H.

- Observation 20. We have n1 ≥ M3 + 1. Proof. By the deﬁnition of jD, we obtain


dπi ≤

−2n1 +

i∈[jD−1]:dπi =2

jD−1

dπi(dπi − 2) ≤ 0.

i=1

Hence, 2n1 ≥ i∈[jD−1]:dπi =2 dπi ≥ M − R ≥ (1 − ω)M, which implies n1 ≥ (1−2ω)M ≥ M

3 + 1.

| |
|---|


If there is a vertex in S of degree 1, then every vertex outside of S has degree 1. Thus every edge in the components of H containing S0 is incident to a vertex of S0, hence there are

- at most X 0 < ω1/29M such edges and we are done. So every vertex in S has degree at least 3.


Proof of Lemma 13. Let jD∗ be such that ni=j∗

dπi = i∈S di. Since i∈S di > 5ω1/4M > ωM, we have jD∗ < jD. By the deﬁnition of R, we have i j=Dj−∗1

D

dπi ≥ 5ω1/4M − R >

D

4ω1/4M. Now, since S contains only vertices of degree at least 3, the deﬁnition of jD implies ∗ D−1

- w∈V \S d(w)(d(w) − 2) = j


i=1 dπi(dπi − 2) ≤ − ji=Dj−D∗1 dπi(dπi − 2) ≤ − ji=Dj−D∗1 dπi < −4ω1/4M, and the ﬁrst statement follows.

If every vertex in S has degree at least ω−1/4 then, since for suﬃciently small ω, we have that ω−1/4 − 2 > 3ω−41/4. With the above observation, we have i j=Dj−∗1

dπi(dπi − 2) > 3ω−1/4

D

- 4 · 4ω1/4M = 3M. Since there are at most M values of i for which di = 1, it follows


that ji=1D−1 dπi(dπi − 2) ≥ 3M − M > 0, which is a contradiction to the choice of jD, and the second statement follows.

| |
|---|


For the proof of Lemma 15 we recall a standard concentration inequality.

- Lemma 21 (Azuma’s Inequality (see, e.g. [26])). Let X be a random variable determined by a sequence of N random experiments T1,...,TN such that for every 1 ≤ i ≤ N and any possible sequences t1,...,ti−1,ti and t1,...,ti−1,t i:


E[X | T1 = t1,...,Ti = ti] − E[X | T1 = t1,...,Ti = t i] ≤ ci, then

− t2

2 N i=1

c2

P[|X − E[X]| > t] < 2e

i .

- Proof of Lemma 15. Recall that Yt = X t − X t−1 − E[d(wt) − 2], which implies E[Yt] = 0. By Lemma 13, we have |Yt| ≤ ω−1/4. Azuma’s inequality applied to t ≤t Yt with N = t and ci = ω−1/4 gives us

P

 

t ≤t

Yt > M2/3

  < 2e−

M4/3

2ω−1/2t < e−M2/7 ,

where we used that t ≤ M. A union bound over all t ≤ M suﬃces to obtain the desired statement.

| |
|---|


- Proof of Lemma 16. We can assume that there is an edge of H from St−1 to V \ St−1 as


otherwise the probability that w is wt is exactly Md(w)

, by construction of the exploration process, and we are done.

t−1

It is enough to prove this result conditioned on the current conﬁguration Ct−1. In doing so, we partition the inputs within Ct−1 (a graph with an ordering of the adjacency list of each vertex) into diﬀerent equivalence classes. All the inputs in the same equivalence class share the same underlying graph G, a partial order of the adjacency list of each vertex in St and a speciﬁcation of the ﬁrst edge from vt to V \ St−1 in the ordering of the adjacency list for vt. Observe that each equivalence class corresponds to the same number of inputs; these arise from each other by suitably reordering some of the adjacency lists. More precisely,

every equivalence class contains i∈V (d i)! inputs, where d i = di if i ∈ V \ St−1, and d i is the number of edges of H from i to V \ St−1 if i ∈ St−1 \ {vt} and is one less than this number if i = vt.

We generalise the deﬁnition of extended switching from graphs to equivalence classes of inputs, provided that the switching neither uses nor creates an edge of H within St−1. This ensures that after the switching, the set of edges of H within St−1 (and the set of edges of G corresponding to them) remains unchanged. Consider switching the pair of edges (e1 = uv,e2 = xy) as explained in Section 3. Let u = w0,w1,...,wr = v be the directed walk in G corresponding to e1 and let x = z0,z1,...,zs = y be the directed walk in G corresponding

- to e2. When switching, we delete the edges wr−1v and xz1 and add the edges wr−1x and vz1. This naturally preserves the ordering of the adjacency lists of u = w0,w1,...,wr−2 and z2,...,zs−1,z2 = y. The orderings of the adjacency lists of wr−1 and z1 are obtained by preserving the position of the edges wr−2wr−1 and z1z2 in them, respectively. If v = x, after the switching, the ordering of the adjacency list of v is obtained by preserving the position of the edges incident to v and diﬀerent from e1. If v = x, after the switching, the position of the edges e1 and e2 in the adjacency list of v is swapped. This works analogously for x. Note that this generalisation preserves the equivalence class of the input: if a switching is performed to an input, ﬁrst, no edges within St−1 are modiﬁed (neither their position on the corresponding adjacency lists) and, second, the speciﬁcation of the ﬁrst edge from vt to V \ St−1 in the adjacency list of vt is preserved.


For any vertex w ∈ V \ St−1, we let Aw be the set of equivalence classes for which w is wt, and let Bw be the set of equivalence classes for which w is not wt. In order to bound the probability that w is chosen to be the vertex wt that will be added to St−1, we consider switchings between elements of Aw and Bw, which allow us to relate |Aw| and |Bw|.

Since t < M12, the set V \ St−1 contains at least M4 + 1 of the at least M3 + 1 vertices of degree 1 and so Mt−1 ≥ M4 + 1.

Proof of (a). A switching from Aw to Bw involves the oriented edge vtw and one of the remaining Mt−1 − 1 oriented edges with ﬁrst endpoint in V \ St−1 or wvt and one of the remaining Mt−1 −1 oriented edges with last endpoint in V \St−1. This implies that there are less than 4Mt−1|Aw| switchings from Aw to Bw.

Next, we prove a lower bound for the number of switchings from Bw to Aw. The choice of an equivalence class in Bw ﬁxes a choice of the edge vtwt. A vertex in V \ St−1 is bad if it either has a neighbour in St−1, has a common neighbour with wt or is adjacent to wt. If w is not bad, then for the unique neighbour z of w there exists four switchings using vtwt and wz (or their reverses), from Bw to Aw. By the hypothesis of the lemma, at most Xt−1 ≤ X t−1 ≤ ω1/5M vertices in V \ St−1 have a neighbour in St−1. By Observation 14, the degrees of the vertices in V \ St−1 are at most ω−1/4, which implies that there are at most ω1/5M + ω−1/2 + ω−1/4 ≤ 2ω1/5M bad vertices. Since sampling an element of Bw uniformly at random, and applying a random permutation to the at least M/4 vertices of degree 1 in V \(St−1 ∪{wt}), yields an equivalence class of Bw that is still sampled uniformly at random, the proportion of equivalence classes in Bw in which a speciﬁc vertex w of degree 1 is not bad, is at least 1 − 2ωM/1/54M > 1 − 8ω1/5. This implies that there are at least 4 1 − 8ω1/5 |Bw| switchings from Bw to Aw.

1/5)|Bw|

Double-counting these switchings yields |Aw| ≥ (1−8ω

Mt−1 . Since, P[w = wt] = |A |Aw|

w|+|Bw|, and Mt−1 = M − X t−1 − 2(t − 1) is large in terms of ω, it follows that P[w = wt] ≥ 1−M9ω1/5

.

t−1

Proof of (b). Let d = d(w). For a switching from Bw to Aw, we have to switch the ordered edge vtwt with one of the d ordered edges wy or the ordered edge wtvt with one of the d

ordered edges yw. Therefore, the number of switchings from Bw to Aw is at most 4d|Bw|.

Next, we prove a lower bound for the number of switchings from Aw to Bw. We have such a switching involving the ordered edge vtw, and some ordered edge yz provided y is in V \St−1, and vty and wz are not edges. We have such a switching involving the ordered edge wvt, and some ordered edge zy provided y is in V \St−1, and vty and wz are not edges. Since vt has degree at most ωM, and the maximum degree of a vertex in V \ St−1 is ω−1/4, the number of choices for zy is at least Mt−1 − ω3/4M − X t−1 − ω−1/2 > (1 − 2ω1/5)Mt−1. Double-counting the number of switchings, we obtain |Bw| ≥ 1 − 2ω1/5 Mt−1

d |Aw|. As before P[w = wt] = |A |Aw|

1/5)d

w|+|Bw|, and hence P[wt = w] ≤ (1+9ω

Mt−1 .

| |
|---|


- Proof of Lemma 17. The proof is by induction on t. Recall that there are between M4 and M vertices of degree 1 in V \ St−1.


First, let t = 1. Observation 14 (b) gives us X 0 ≤ ω1/25M , hence Lemma 16 implies

(1 + 9ω1/5) w∈V \S

d(w)(d(w) − 2) + 18ω1/5n1 M0

E[d(w1) − 2] ≤

0

.

Thus, by Lemma 13 and the fact that n1 is at most M0 + 1 (recall that there are no vertices of degree 1 in S0), we have E[d(w1) − 2] ≤ −M1 + 19ω1/5.

Now, let 2 ≤ t ≤ ω1/29M . By induction, we obtain

X t−1 = X 0 +

t−1

(E[d(wi)] − 2) +

i=1

Yt ≤

t <t

ω1/5M 2

+ 19ω1/5t + M2/3 ≤ ω1/5M.

- Claim 1. For any sequence of positive integers a1,...,aj distinct from 2 and a nonnegative integer such that ji=1 ai ≥ 2j − , we have ji=1 ai(ai − 2) ≥ j − 2 .


Proof. The proof is by induction on ji=1 ai. The statement is trivially true if j = 0.

If all ai are at least 3, then ji=1 ai(ai − 2) ≥ ji=1 ai ≥ 2j − ≥ j − 2 . Hence, we may assume without loss of generality that aj = 1. Since ji=1−1 ai ≥ 2j − −1 = 2(j −1)−( −1), if = 0, we obtain by induction that ji=1 ai(ai − 2) ≥ (j − 1) − 2( − 1) − 1 = j − 2 .

So, we can assume that = 0. If for all i ∈ [j], the integer ai ∈ {1,3}, then the claim also follows easily, as then |{i ∈ [j] : ai = 3}| ≥ |{i ∈ [j] : ai = 1}|. Since 3(3 − 1) + 1(1 − 2) = 2, the negative contribution of a 1 is compensated by a 3.

Hence, without loss of generality, a1 ≥ 4 and j > 1. If ji=1 ai > 2j then by decreasing a1 by 1 and then applying induction we are done. So, we may assume ji=1 ai = 2j, and thus there must be at least a1 − 2 values of i for which ai = 1. The sum of ak(ak − 2) over these a1 − 2 elements and a1 is (a1 − 1)(a1 − 2) ≥ a1 − 1. So, deleting these a1 − 1 elements from the set and again applying induction, we are done.

| |
|---|


Since Xt−1 > 0, we have X t−1 > 0, and hence ti=1−1 d(wi) = 2(t − 1) + ti=1−1(d(wi) − 2) = 2(t − 1) + X t−1 − X 0 ≥ 2(t − 1) − X 0. By Claim 1,

t−1

d(wi)(d(wi) − 2) ≥ (t − 1) − 2X 0.

i=1

###### Since V \ St−1 = V \ (S0 ∪ {w1,...,wt−1}), Lemma 13 yields

d(w)(d(w) − 2) ≤ 2X 0 − (t − 1) .

w∈V \St−1

Combining this bound with Lemma 16 yields to

(1 + 9ω1/5)(2X 0 − (t − 1)) + 18ω1/5n1 Mt−1

E[d(wt)] − 2 ≤

Since n1 ≤ Mt−1, X 0 ≤ 7ω1/4M, and M4 ≤ Mt−1 < M, we obtain

t − 1 M

t M

+ 4(1 + 9ω1/5)(14ω1/4) + 18ω1/5 ≤ −

E[d(wt)] − 2 ≤ −

.

+ 19ω1/5

which completes the proof of Lemma 17.

| |
|---|


### 5 The Proof of Theorem 9

Again, we use H for H(D), V for V (H(D)), M for MD, R for RD and G for G(D). Since D is well-behaved, we can also assume that M is suﬃciently large to satisfy various inequalities scattered throughout the proof.

As we have already mentioned, in the preprocessing step we need to handle the vertices of large degree. We let L be the set of vertices of degree exceeding

√

M

logM . We will prove the following result using the combinatorial switching approach:

- Lemma 22. The probability that the number of edges in the components of H intersecting L is at least 200R and there exists no component containing at least 200R edges is o(1).

We also need the following straightforward result:

- Lemma 23. Let U be a set of vertices of H that contains all vertices of degree exceeding


√

M

log M and let 14 < c < 1 be such that u∈U d(u) ≤ cR. Then

(1 − c) 2

d(u)(d(u) − 2) ≥

R.

u∈V \U

√

M

logM . Letting U = {i : i ≤ jD, πi ∈ U} and K = i∈U dπi, the deﬁnition of jD implies

≤

Proof. The assumptions imply dπj

D

n

dπi(dπi − 2)

dπi(dπi − 2) +

dπi(dπi − 2) −

d(u)(d(u) − 2) ≥ −

i=jD+1

i∈U

i∈U\U

u∈V \U

− (cR − K)) ≥

≥ −K(dπj

− 2) + (dπj

− 2)(R − dπj

D

D

D

(1 − c) 2

R.

| |
|---|


Starting with the set L, we ﬁrst explore all the components in H that contain at least one vertex in L. Let U be the set of all vertices in such components. If u∈U d(u) ≥ 100R , then by Lemma 22 the probability that there does not exist a component in H with at least 200R edges is o(1). So, in what follows, we condition on u∈U d(u) ≤ 100R .

We let S0 = U ∪ {v}, where v is a random vertex selected with probability proportional to d(v). Since there are no edges from U to V \ U, we have v1 = v. Note that this implies that, for every t, the edges counted by Xt belong to the same component (not necessarily the one of v). In addition, the maximum degree of a vertex in V \ U is at most

√

M

logM and M ≥ M0 ≥ M − 100R − d(v0) ≥ M − 100M −

√

logM ≥ 98100M .

M

For each vertex w ∈ V \ St−1, we let d t(w) be the sum of the number of loops of H at w and the number of edges of H between w and St−1 \ {vt}. Observe that we can control the number of edges between St and V \ St as follows

Xt = Xt−1 + (d(wt) − 2) − 2d t(wt) . (1)

The next lemma shows that the probability of selecting a vertex w at time t is essentially proportional to its degree.

- Lemma 24. Let β < 10−6 be a ﬁxed constant. If Mt−1 ≥ 3M4 and Xt−1 ≤ βM, then for every w ∈ V \ St−1,

(1 − 10 β)

d(w) Mt−1 ≤ P[w = wt] ≤ (1 + 10 β)

d(w) Mt−1

,

and,

P d t(w) ≥ 2 βd(w) + i|w = wt ≤ βi/2 .

We are now in a position to carry out our exploration process. Let At = d(wt) − E[d(wt)] and let Bt = d t(wt) − E[d t(wt)]. By our convention, both expectations are conditional on Ct−1. We let Fbad be the set of those inputs such that for some t either t ≤t At > log logM M or t ≤t Bt > log logM M .

- Lemma 25. P[Fbad] = o(1). Let = MR ≥ , β = 10−6 2, and τ be the smallest t for which either Xt ≥ βM or

Mt ≤ 1 − 4 M0.

- Lemma 26. For any t < τ, E[d(wt) − 2] ≥ 4, E[d t(wt)] ≤ E(d(w3t)−2), and E[Xt − Xt−1] ≥ E[d(wt)−2]


3 ≥ 12. Proof. We have

d(u) =

u∈St−1

d(u) ≤

d(u) +

u∈S0

u∈St−1\S0

R 100

+ M0 − Mt−1 ≤

1 100

1 4

+

R 3

R ≤

.

By the deﬁnition of τ, the hypotheses of Lemma 24 are satisﬁed. Using Lemma 23 as well as

Lemma 24 we conclude E[d(wt) − 2] =

(d(w) − 2)P[w = wt]

w∈V \St−1

1 Mt−1

1 Mt−1

≥

d(w)(d(w) − 2) +

d(w)(d(w) − 2)

(1 − 10 β)

(1 + 10 β)

w∈V \St−1 d(w)≥3

w∈V \St−1 d(w)=1

20√βn1 Mt−1 ≥

1 Mt−1

≥

d(w)(d(w) − 2) −

(1 − 10 β)

w∈V \St−1

1 3

R M − 30 β ≥ 4

1 − 10 β

, since β ≤ 10−6 2. This proves the ﬁrst statement. Again, by Lemma 24, we obtain E[d t(wt)] ≤ 7 βE[d(wt)] = 7 βE[d(wt) − 2] + 14 β ≤

E[d(wt) − 2] 6

E[d(wt) − 2] 3

70 ≤

, where the last inequality follows from the ﬁrst statement of this lemma.

+

Now, since E[Xt − Xt−1] = E[d(wt) − 2] − E[2d t(wt)] the third statement follows directly from the ﬁrst and second one.

| |
|---|


Since all the edges counted by Xt are in the same component of H, this next lemma proves Theorem 9.

- Lemma 27. With probability 1 − o(1), we have Xτ ≥ βM.


Proof. We show that if our conﬁguration is not in Fbad then Xτ ≥ βM. By Lemma 25, the result follows.

Applying (1) recursively, we have Xτ = X0 +

(d(wt) − 2) − 2

d t(wt) .

t≤τ

t≤τ

By adding E[Xτ], subtracting the expectation of the right hand side in the previous equation and since E[X0] = X0, we obtain that

Xτ = E[Xτ] +

(d(wt) − 2 − E[d(wt) − 2]) − 2

t≤τ

= E[Xτ] +

At − 2

Bt

t≤τ

t≤τ

3M log log M

≥ E[Xτ] −

.

(d t(wt) − E[d t(wt)])

t≤τ

If τ > 400 M , then Lemma 26 implies Xτ ≥ 12 τ − log log3M M ≥ βM, and we are done. Now, let τ ≤ 400 M . If Xτ < βM, then, by the deﬁnition of τ, Mτ ≤ 1 − 4 M0. Note that

t≤τ d(wt) = M0 − Mτ ≥ 4 M0 ≥ 5 M, because M0 ≥ 98100M . Using Lemma 26 as before, we obtain

E[d(wt) − 2] 3 −

3M log log M ≥ 15

2τ 3 −

3M log log M ≥ 20

Xτ ≥ X0 +

M −

M > βM,

t≤τ

a contradiction. Thus, Xτ > βM in both cases. It remains to prove Lemma 22, 24 and 25.

| |
|---|


#### 5.1 The Details

We start this section with a result showing that if there are many vertices in L, then they all lie in the same component of H.

- Lemma 28. If |L| ≥ log7 M, then the probability the vertices of L lie in the same component of H is 1 − o(1).


√

√

M

M

Proof. Let L6 and L7 be the vertices of degree at least

log7 M , respectively. We divide the proof into two cases depending on the size of L6.

log6 M and

√

M log6 M .

- Case 1: |L6| ≥


We begin with a claim which shows that every vertex in L is adjacent in H to a large number of vertices in L7.

√

M

- Claim 2. For every u ∈ L, the probability that u is adjacent to at most


log14 M vertices in L7

is at most M−7. Proof. Let K = 2

√

M

log14 M . Assume for a contradiction that the claim fails for u ∈ L. For every k ∈ {0,...,K}, let Fk be the event that u is adjacent to exactly k vertices in L7. By our assumption, there is some k0 ∈ {0,..., K2 } such that P[Fk0] > M−8.

Suppose that G is in Fk. We consider switchings that lead to a multigraph in either Fk+1 or Fk+2. We stress here that we will use a specially adjusted version of switchings. Consider edges uv ∈ E(H) such that v ∈/ L7 or uv is not an edge in G. We have at least

√

√

M

M 2 log M

logM − k ≥

√

√

√

M

M

M

log6 M −

log14 M ≥

choices for such an edge. Moreover, there are at least

2 log6 M vertices

- x ∈ L6 \ NH(v). Now we discuss diﬀerent switching situations depending on the structure of G.

First, suppose that there are at least

√

M

4 logM edges uv such that v ∈/ L7. Choose such an oriented edge uv. Then, for each x ∈ L6 \ NH(v), there are at least

√

M

log6 M −

√

M

log7 M ≥

√

M

2 log6 M edges xy such that y = v and either xy is not an edge in G or vy ∈/ E(H). In both cases we get at least 16 logM313/2M switchings which increase the degree of u in L7.

Otherwise, there are at least

√

M

4 logM edges uv that are not edges in G. Choose such an edge uv. Next, suppose that there are at least

√

M

4 log6 M vertices x ∈ L6 \ NH(v) such that there are at least

√

M

2 log6 M edges xy with y = v. As before this give rise to at least 32 logM313/2M switchings. (Observe that if u = v, then the obtained graph is in Fk+2. Observe also that we chose to switch so that the new edge between y and v corresponds to the edge between u and v and hence has an internal vertex). Otherwise, there are at least

√

M

4 log6 M vertices x ∈ L6 \ NH(v) such that there are at least

√

M

2 log6 M edges xy with y = v. Choose such an xy that it is not an edge in G (all but at most one of them are not edges of G). If either uv or xy corresponds to a path of length at least 3 in G, then there exists at least one switching (the one that switches such an edge to a new loop in y = v) that transforms G into a graph in Fk+1. If both uv and

- xy correspond to paths of length 2, then we perform a special type of switching. Let uwv and xzy be the corresponding paths in G. Then, we obtain the switched graph by deleting the edges uw, wv, xz and zy and by adding the edges ux, vw, wz and zy. This gives a graph in Fk+1. In this case, there are also at least 32 logM313/2M switchings.


Now, for any G in either Fk+1 or Fk+2, consider the switchings that transform it into a multigraph in Fk. We must use an edge uv for v ∈ L7 which is not a parallel edge in H. While there might be many edges between u and L7, note that there are at most k + 2 of

this type. We can select xy in at most M ways. Thus there are at most 4(k + 2)M ≤ log10M143M/2 switchings leading to a multigraph in Fk. The factor 4 comes from the fact that we performed the special type of switching introduced above, that given two edges in a graph can give rise to at most 4 graphs.

Hence P[Fk+1]+P[Fk+2] ≥ log320M P[Fk] ≥ 8P[Fk], and in particular max{P[Fk+1],P[Fk+2]} ≥ 4P[Fk]. Using that P[Fk0] ≥ M−8, we have max{P[FK−1],P[FK]} ≥ 2K−k0P[Fk0] > 1, which is a contradiction.

| |
|---|


Now we use Claim 2 to show that any two vertices in L whose degree is not extremely large, lie in the same component.

- Claim 3. For every u,v ∈ L each of degree at most logM24 M , the probability that they are not in the same component is at most M−4. Proof. Let K = log M . For every k ∈ {0,...,K}, we deﬁne the following events,


A1 : u and v have no common neighbour in H.

- Ak2 : there are k edges between NH(u) and NH(v) in H.
- Ak3 : H has an edge-cut of size at most 2k separating NH(u) and NH(v).


Let Fk be the event A1 ∩Ak2 ∩Ak3. Observe that if F0 is not satisﬁed, then there exists a path between u and v. Thus, it suﬃces to show P[F0] ≤ M−4.

Here, we will show that for every k satisfying P[Fk] ≥ M−4, we have max{P[Fk+1],P[Fk+2]} ≥ log M · P[Fk] . This implies that P[F0] ≤ max{M−4,(log M)−K2 } ≤ M−4 and proves the claim.

So, suppose P[Fk] ≥ M−4. Let F k ⊆ Fk be the event that u,v are in addition adjacent to at least

√

M

log14 M vertices in L7. By Claim 2 and since P[Fk] ≥ M−4, we obtain that P[F k] ≥ 21P[Fk].

We consider switchings from a graph G in F k to Fk+1 or Fk+2, which use no edge incident

- to u or v. We are going to switch using edges from two sets which we now deﬁne. Fix an edge cut F1 of size at most 2k separating NH(u) and NH(v) and let F2 be the set of


k edges between NH(u) and NH(v). These two sets of edges exist by Ak3 and Ak2, respectively. Given that G is in F k, there are at least

√

M

log14 M vertices x ∈ NH(u) ∩ L7 and for each such x, there are at least

√

log7 M edges xy. Since d(u) ≤ logM24 M , essentially all such xy satisfy

M

- y = u. Indeed, we can ﬁnd a set X of

√

M

2 log14 M vertices x ∈ NH(u) ∩ L7 such that x is not an endpoint of F1 ∪ F2 and there are at least

√

M

2 log7 M edges xy with y = u. Let E1 be the set of edges xy such that x ∈ X, y = u and either xy is not an edge of G or y is not an endpoint of any edge of F1 ∪ F2. Since |F1 ∪ F2| ≤ 3k, |E1| ≥ 8 logM21 M .

In the same vein, we can obtain a set of vertices W such that for each w ∈ W, we have

- w ∈ NH(v)∩L7, w is not an endpoint of F1 ∪F2 and there are at least


√

M

2 log7 M edges wz with

- z = v. Moreover, we can also obtain a set of edges E2 with |E2| ≥ 8 logM21 M such that for each


wz ∈ E2, w ∈ W, z = v and either wz is not an edge of G or z is not an endpoint of any edge of F1 ∪ F2.

Observe that for any xy ∈ E1 and any wz ∈ E2, we have y = z. Otherwise, if y = z, there exists a path uxywv non of whose edges are in the edge cut F1, getting a contradiction.

If yz is an edge of H, then yz ∈ F1 and both xy and wz are not edges of G. Note that xw ∈/ E(H). Thus, we can always switch xy and wz to obtain a new graph which is Fk+1 or Fk+2 (it only belong to Fk+2 if y ∈ NH(u) and z ∈ NH(v)). There are at least 64 logM422 M switchings.

Given a graph in Fk+1 ∪ Fk+2, there are at most 4(k + 2)M ≤ M3/2 switchings which

yield a graph in Fk. We conclude that max{P[Fk+1],P[Fk+2]} ≥ log M · P[Fk], as desired. A union bound over all pairs u,v ∈ L together with Claim 3 suﬃces to show that in

| |
|---|


Case 1, with probability 1 − o(1) all the vertices in L with degree at most logM24 M lie in the same component of H.

Now we consider a set S consisting of all the vertices of L of degree at least logM24 M and one other vertex of L, if there are any more. Therefore, |S| ≤ log24 M + 1.

For any u,v ∈ S, we let Au,v be the event that u and v are in the same component and Bu,v be the event that they are in diﬀerent components. We will use switchings involving u and v. On the one hand, for any graph in Bu,v, there are d(u)d(v) ≥ logM253/M2 switchings which yield a graph G in Au,v in which uv is an edge of H. On the other hand, for any graph G in Au,v there are at most 4M switchings using the edge uv and another edge, that transform the graph into a graph in Bu,v. Therefore, P[Bu,v] ≤ M−1/3. So, with probability 1 − o(1) all the vertices in S lie in the same component. This implies that with probability 1 − o(1), all the vertices in L lie in the same component of H and this completes the proof of the lemma for Case 1.

√

M log6 M .

- Case 2: |L6| ≤


Let be the size of L. By the hypothesis of the lemma and of this case, we have

√

M log6 M

log7 M ≤ ≤

. (2)

The following claim shows that with high probability, the multigraph induced in H by the vertices in L, has large minimum degree.

- Claim 4. With probability at least 1 − −7, every vertex u ∈ L is incident to at least √ log edges of H which join it to other vertices of L.


Proof. Fix a vertex u ∈ L. For every 0 ≤ k < 2√ log , let Fk be the event that u is incident to exactly k edges joining it to vertices of L in H. Using (2), we have that k ≤ 2√ log ≤ M1/4.

Let G be a graph in Fk. We will count how many (extended) switchings lead to a graph in Fk+1. By the hypothesis of Case 2, there are at least

√

√

√

M

M

M

logM −

log6 M − k ≥

2 logM edges uv such that either v  ∈ L6 or v  ∈ L and uv corresponds to a path of length at least 2 in G.

For any such edge uv, we can switch with any edge xy disjoint from uv such that x ∈ L\{u} and is not adjacent to u unless one of the following situation happens:

- (i) xy and uv both correspond to edges of G and there is an edge corresponding to an edge of G between y and v, or


- (ii) v = y.


There are at least −k −1 ≥ 2 choices for x ∈ L\NH(v). Given the choice of uv and x, since

√

M

- x ∈ L and if uv is an edge of G then v ∈ L6, there are at least


2 logM choices for an edge xy that do not satisfy (i). Since v  ∈ L, there are in total at most

√

M

logM edges xy satisfying (ii) for uv.

√

√

√

M 4 logM −

M

M

logM ≥

Thus, there are at least

5 logM choices for an edge xy that give a valid switching with uv. So, in total there are at least 10 log M2 M switchings.

If G is in Fk+1, then there are at most 4(k + 1)M ≤ 8√ log  M switchings that lead to a multigraph in Fk.

Using (2), we conclude,

80√ log log2 M

1

P[Fk] ≤

log M · P[Fk+1], In particular, for every k ≤

· P[Fk+1] ≤

√ log , we have P[Fk] ≤ (log M)−

√ log · P[F2√ log ] < −9. A union bound for all k ≤

√ log and all vertices v ∈ L now yields to the desired result.

| |
|---|


To complete Case 2, we will use the minimum degree within the vertices in L to show that the multigraph induced by L in H, denoted by H[L], is connected. For every k ≥ 1, let Fk be the event that H[L] has exactly k components. We show that there is an f(l) which is o(l) such that for every k ≥ 1 that satisﬁes P[Fk+1] ≥ −2, we have P[Fk+1] ≤ f(l)P[Fk]. If so, P[F1] = 1 − o(1), or in other words, with probability 1 − o(1) the multigraph H[L] is connected. This proof follows the same lines as the one in Lemma 10.

Fix k ≥ 1 such that P[Fk+1] ≥ −2. Suppose G is in Fk. Any (extended) switching from G that leads to a graph in Fk+1 creates a new component and hence either uses two cut edges or uses a 2-edge cut which does not contain a cut edge. By Lemma 11, there are at most 8 2 switchings leading to a multigraph in Fk+1.

For every k ≥ 1, let F k be the event Fk with the additional restriction that H[L] has minimum degree at least √ log . Since P[Fk+1] ≥ −2, by Claim 4, P[F k] ≥ 12P[Fk]. Suppose now that G is in F k+1. We will lower bound the number of (extended) switchings to graphs in Fk. In order to merge two components it is enough to select non-cut edge xy and an edge uv in another component. By the deﬁnition of F k+1, there are at least |E(H[L])| − ≥

- 1

- 2
- 3/2√log − ≥ 3/2 choices for xy. Given the choice of xy, there is at least one vertex in


another component, and hence, there are at least √ log choices for uv. The total number of switchings is at least 2√log .

Hence, for every k ≥ 1 and since → ∞ as n → ∞,

- 1

- 2√log · P[Fk] =


16 √log

P[Fk+1] ≤ 2P[F k+1] ≤ 2 · 8 2 ·

P[Fk]).

This completes the proof of Lemma 28. We proceed with the proof of Lemma 22.

| |
|---|


Proof of Lemma 22. If |L| ≥ log7 M, we can use Lemma 28 to show that with probability 1 − o(1), all the vertices in L lie in the same connected component, and hence the statement of the lemma holds in this case.

Therefore, we can assume that |L| ≤ log7 M. Since R ≥  M, this implies that if the union

of the components intersecting L have at least 200R edges there is a component of size at least M2/3 which contains a vertex of L. So, it is enough to prove that for every pair u,v ∈ L, the probability that u is in a component with at least M 23 edges not containing v is o(M−101 ).

Fix u,v ∈ L. Let F− be the event that the component of u in H has at least M 32 edges and u,v are in diﬀerent components. Let F+ be the event that u,v are in the same component of H. We will show that P[F−] = o(M−101 )P[F+].

√

M

Let G be a graph in F−. Since v ∈ L, there are at least

2 logM oriented edges vw (i.e. we count loops twice) and at least M2/3 oriented edges xy in the same component as u ordered in such a way that x is at least as close to u, as y. Thus, the total number of switchings, using an edge xy ordered in such a way leading to a multigraph in F+ with vx an edge is at least logM7M/6 .

Consider G in F+ obtained by such a swap. If v = w and x = y, then there exists a unique edge vx in any shortest path from u to v. Otherwise we can ﬁnd two edges incident

- to v, such that every shortest path from u to v contains one of them. So, the total number of such switchings leading to G is at most 8M.

We conclude the desired result, P[F−] ≤ 8 logM1/M6 · P[F+] = o(M−101 ).

| |
|---|


- Proof of Lemma 24. Recall that for every t ≥ 0, we have L ⊂ St. Moreover, by construction of the exploration process, the component we are exploring at time t has no vertices in L. Thus any vertex that belongs either to the current explored component or to V \ St, has


degree at most

√

M

logM . This implies that, for every vertex v that plays a role in the exploration

process, the number of edges incident to a neighbour of v is at most logM2 M . This property will be crucial in our analysis.

In this proof we consider inputs (graphs equipped with an order of each adjacency list) instead of graphs. As in the proof of Lemma 16, we will perform our switchings between equivalence classes of inputs.

We start by proving the second part of the lemma. We ﬁx w ∈ V \ St−1 and condition on the conﬁguration Ct−1 at time t − 1. For every 0 ≤ i ≤ d(w) − 1, we let Fi be the equivalent class of inputs such that wt = w and that the sum of the number of loops on

- w and edges from w to St−1 is i + 1. For any equivalence class in Fi+1, there are at least


(i+1)(Mt−1 −βM − log2M2 M ) ≥ 2(i+1)3 M switchings that lead to one in Fi. For any equivalence class in Fi, there are at most 8(d(w)−i)(βM +d(w)) switchings that lead to Fi+1. It follows that for i+1 ≥ 2√βd(w), we have P[Fi+1] ≤ 16√βP[Fi]. The second statement of the lemma follows from applying the last inequality recursively.

In the same vein, one can obtain that conditional on wt = w, the probability that w is incident to more than 3√βd(w) edges connecting to St−1, is at most 2√β. We omit the details. This fact will be used at the end of the proof.

As before, we ﬁx w ∈ V \ St−1 and condition on the conﬁguration Ct−1 at time t − 1. We let Aw be the union of the equivalence classes of inputs consistent with this conﬁguration where wt = w and we let Bw be those where wt = w.

Let Bwi be the elements of Bw such that there are i edges between w and vt. For each equivalence class in Bwi+1, we can switch any edge vtw with some other ordered edge xy with

- x ∈ V \ St−1 to get an element of Bwi unless x is a neighbour of vt or y is a neighbour of w. Thus, given a graph in Bwi+1, there are at least (i + 1)(Mt−1 − log2M2 M ) switchings that lead to Bwi . On the other hand, given an element of Bwi , there are at most d(w)d(vt) ≤ logM2 M switchings that lead to Bwi+1. Since Mt−1 ≥ 3M4 , we have that Mt−1 − log2M2 M ≥ M2 . This implies, |Bwi | ≥ log22 M |Bwi+1|. Thus,


1 2log M |Bw| . (3)

|Bw0 | ≥ 1 −

We let Cwi be the elements of Bw0 such that there are i edges between wt and the neighbours of w (recall that w = wt). Given an equivalence class in Cwi+1, there exist at least (i+1)(Mt−1− βM − log2M2 M ) switchings that lead to Cwi and that do not use any edge incident to vt. On the other hand, given an equivalence class in Cwi , there are at most (d(wt) − (i + 1))d(w)

√

M

logM ≤ d(w)logM2 M switchings that lead to Cwi+1.

√βd(w), we have that,

Given that i + 1 ≥

√βd(w)M2 d(w)logM2 M |Cwi+1| ≥ log M|Cwi+1| .

|Cwi | ≥

Using (3), it follows that conditional on our input being in Bw, the probability that w has no edge to vt and wt has at most √βd(w) edges incident to NH(w) is at least

- 1 − 2 log1 M 1 − log2M ≥ 1 − log3M . Combining the statements above, we obtain that the proportion of elements of Bw such


that in the corresponding multigraph H we have that w has no edge to vt, is incident to at most 3√βd(w) edges that are also incident to St−1 and wt is incident to at most √βd(w) edges that are also incident to NH(w), is at least 1 − 2√β − log3M ≥ 1 − 3√β. Note that this implies that wwt is not an edge of H.

We consider switching using an ordered pair of oriented edges vtwt and wx of H such that x is not in St−1. For inputs as in the last paragraph, there are at least (1 − 4√β)d(w) choices for an oriented edge wx to switch with vtwt to construct an input in Aw (we simply cannot choose x in St−1 or such that wx is an edge of G and wtxis an edge of G) . Clearly, for any input in Bw, there are at most d(w) oriented edges to switch that lead to Aw. For any equivalence class in Aw, similarly as before, there are between Mt−1 − βM − log2M2 M and Mt−1 such switchings that lead to Bw( we pick an oriented edge xy of H with both endpoints outside St−1 and say we produced vtw and xy by swapping on vtx and wy, this will work for certain provided x is not incident to a neighbour of vt and y is not incident to a neighbour of w).

Straightforward computations give,

1 − 10 β

d(w) Mt−1 ≤ P[Aw] ≤ 1 + 10 β

d(w) Mt−1

.

| |
|---|


- Proof of Lemma 25. Recall that At = d(wt)−E[d(wt)] and that Bt = d (wt)−E[d (wt)]. Note that E[At] = E[Bt] = 0 and since the maximum degree of the vertices in V (H) \ S0 is at


√

√

logM , we have |At|,|Bt| ≤ 2

M

M

most

logM . We can apply Azuma’s Inequality (see Lemma 21) to t ≤t At with N = t and ci = 2

√

M

logM , to obtain

 

  < 2e−

M log2 M

M log log M

8t(loglogM)2 < e−log3/2 M ,

P

At >

t ≤t

since t ≤ M and M is large enough. A union bound over all t ≤ M suﬃces to obtain that the probability there exists a t such that t ≤t At > log logM M is o(1). The same argument can be used for Bt. Thus, we obtain P[Fbad] = o(1).

| |
|---|


### 6 Handling Vertices of Degree 2

#### 6.1 Disjoint Unions of Cycles

The graph G(D) partitions into a set of cyclic components and a subdivision of H(D). We consider ﬁrst the structure of the graph formed by its cyclic components. We let T be the set of vertices in these components and let J(T) be a union of cycles chosen uniformly at random among all 2-regular graphs with vertex set T. We emphasize that G(D) is a simple graph so these cycles have length at least 3.

Fix some vertex v ∈ T. Let p ,t be the probability that v is in a cycle of length in J(T) if t = |T|. Let Ct be the number of conﬁgurations of t vertices into disjoint cycles of length at least 3. We will use the following result on the asymptotic enumeration of 2-regular graphs (see, e.g. Example VI.2 in [12]).

###### Theorem 29 ([12]). We have

Ct = 1 +

5 8t

+ O(t−2)

e−3/4 √πt

t! .

- Corollary 30. For every integer t ≥ 3 and every 3 ≤ ≤ 34t, we have

p ,t =

- 1 + O( t−2)

- 2 t(t − )


.

Proof. If v belongs to a cycle of length , then there are t− −11 ways to select the remaining vertices in its cycle. In addition, there are ( −21)! possible conﬁgurations for the cycle containing v given we have selected the vertices in this cycle. Hence p ,t = t− −11 ( −21)! Ct−

Ct . The desired results follow from straightforward computations using the bounds from Theorem 29.

| |
|---|


- Corollary 31. For every 0 < δ < 34 and for every suﬃciently large t, the probability that v lies on a cycle of J(T) of length at least δt2 but less than δt is at least 5δ.


Proof. Using Corollary 30 and that t(t − ) < t, we obtain that the desired probability is at least

δt

δt

(1 + ot(1)) 2 t(t − ) ≥

δ 5

p ,t ≥

.

=δt2

=δt2

| |
|---|


- Corollary 32. For every 0 < δ < 83 and for every suﬃciently large t, the probability that J(T) contains a cycle of length at least δt is at least 3δ.

Proof. The probability there exists a cycle of length at least is at least the probability that v is in a cycle of length . Using Corollary 31, we conclude that the probability that v is contained in a cycle of length at least δt (and at most 2δt) is at least 3δ.

| |
|---|


- Corollary 33. For every 0 < < 1, there exists a p > 0 such that for any suﬃciently large t, the probability that J(T) contains no cycle of length at least  t is at least p .


Proof. It suﬃces to prove the statement for < 101 . We let D be the event that the sum of the lengths of the cycles of J(T) which have length

at least  t4 but less than  t2 exceeds (1 − )t. Clearly it is enough to prove a lower bound on P[D ].

For k ≥ 0, we let Ek,  be the event that J(T) contains k cycles P1,...,Pk of length

1,..., k such that for each 1 ≤ i ≤ k, if ti = t − j<i j ≥  t, then Pi is disjoint from Pj for all j < i and the lowest indexed vertex in T \ (∪j<iPj) is in Pi, and  t4 ≤ i ≤  t2 .

We set k∗ = 4 . Observe that P[D ] ≥ P[Ek∗, ], so it suﬃces to lower bound P[Ek∗, ]. Clearly, P[E0, ] = 1. For 1 ≤ k ≤ k∗, we have P[Ek,  | Ek−1, ] = 1 if the number t of vertices not in the union of the Pj for j < i is less than  t as we can simply set Pi = Pi−1. Given that t ≥  t, this conditional probability is at least the probability the vertex v with lowest index in a uniformly random disjoint union of cycles of total length t is in a cycle of length

with  t4 ≤ ≤  t2 . By applying Corollary 31 with the parameters δ = 2 tt ≤ 12 and t , we have P[Ek, ] ≥ P[Ek,  | Ek−1, ]P[Ek−1, ] ≥ 5P[Ek−1, ]. Hence P[Ek∗, ] ≥ (5)k∗ ≥ (5) 4 −1 .

| |
|---|


#### 6.2 The order of the components

In this section we study the number of vertices in the union of some components of G = G(D) conditioned on an (at least partial) choice of H = H(D). As before, we write M = MD. Observe that the degree sequence D ﬁxes the number m = M2 of edges of H and also n2, the number of vertices of degree 2 in G, while a choice of H ﬁxes the number of edges of H(D) in each of its components.

For a given choice of H, we expose edges and vertices of degree 2 in G in two phases. In the ﬁrst phase we do the following.

- (1.1) For each set of parallel edges between two vertices in H, we expose at most one of them as an edge of G. The parallel edges of H that we exposed as edges of G will be called ﬁxed edges of H.
- (1.2) For each non-ﬁxed edge in H with distinct endpoints which is parallel to some other edge (so it corresponds to a path in G of length at least 2), we expose the edge on the corresponding path of G which is incident to its endpoint of lowest index; that is, we expose the other endpoint of such an edge.
- (1.3) For each loop of H rooted at a vertex, we expose the two edges of G incident to this vertex in the cycle of G corresponding to the loop; that is, we expose the other endpoints of these two edges.


We note that if an edge of H is neither a loop nor parallel to another edge, then we do not expose whether it corresponds to an edge or a non-trivial path of G.

Let m be the number of edges of H that are non-ﬁxed. We let n∗2 be the number of vertices of degree 2 which have been exposed in (1.2) or (1.3). Let n 2 = n2 − n∗2 be the vertices of degree 2 that have not been exposed yet.

###### Observation 34. We observe that

- (a) for every component K of H, there are at most |E(2K)| ﬁxed edges, and

- (b) for every component K of H, the number of vertices of degree 2 exposed in (1.2) or (1.3) inside K, is at most 2|E(K)|, and the sum of the number of such vertices and |V (K)| is at most 3|E(K)|.


} of the nH2 vertices of degree

Suppose that we also condition on the set TH = {v1,...,vnH

2

- 2 that have not been exposed yet and which lie in the non-cyclic components of G. Then we can specify the non-cyclic components of the graph G in a second phase.


- (2.1) Fix an arbitrary ordering of the m edges of H that are non-ﬁxed and a direction on each of these edges.
- (2.2) Choose a uniformly random permutation π of length nH2 + m − 1 of TH and a set of m −1 indistinguishable delimiters. We let di be the position of the i-th delimiter in the permutation and add a delimiter d0 = 0 at the start of the permutation and a delimiter dm = nH2 + m at its end.
- (2.3) For every 1 ≤ i ≤ m , let ei = xy be the i-th non-ﬁxed edge of H, with the corresponding direction. We let x (resp. y ) be the neighbour of x (resp. y) on the path of G corresponding to ei if we have exposed it, otherwise we set x = x (resp. y = y). We expose the vertices vj ∈ TH with di−1 ≤ π(j) < di to construct a path in G connecting x and y . We do this by starting at x and by following the order induced by π.


Now, conditional on the choice of TH of size nH2 , the number of choices for the non-cyclic components of G(D) is exactly

(nH2 + m − 1)! (m − 1)!

NH(nH2 ,m ) =

.

Recall that, if we only condition on the information exposed in (1.1)–(1.3), we have m

non-ﬁxed edges in H and n∗2 vertices of degree 2 which were exposed in non-cyclic components. Also recall, n 2 = n2 − n∗2. For each s,t with s + t = n 2 and every m ≥ 1, we let N(s,t,m ) be the number of graphs with t vertices of degree 2 in cyclic components and s + n∗2 vertices of degree 2 in non-cyclic components given our exposure of H.

By the previous observations, N(s,t,m ) = s+t t NH(s,m )Ct, where Ct has been deﬁned in the previous section as the number of conﬁgurations of disjoint cycles using t vertices. Now,

NH(s+1,m )

NH(s,m ) = s + m . Theorem 29 allows us to estimate the ratio Ct/Ct−1. We thus obtain

that there exists some function f such that f(t) = O(t−2) and 0 < 1−f(t) < t−t1, and such that for every t ≥ 4,

- s+t
- t


NH(s,m ) NH(s + 1,m ) ·

t − 1 t

m − 1 s + m

N(s,t,m ) N(s + 1,t − 1,m )

Ct Ct−1

= (1 − f(t))

·

1 −

.

=

s+t t−1

(4)

It is also not hard to see that for non-negative s we have:

N(s,3,m ) N(s + 3,0,m )

=

1 3!

(s + 3)(s + 2)(s + 1) (s + m )(s + m + 1)(s + m + 2)

. (5)

We let N∗(n 2,m ) = N(n 2,0,m ) + nt=3 2 N(n 2 − t,t,m ). For every t ≥ 3, let qt(n 2,M ) =

N(n 2 − t,t,m ) N∗(n 2,m )

.

That is, qt equals the probability that there are t vertices in the cycle components given our choices of H(D) and the exploration explained above. Observe that if g is a function such that g(i) = O(i−2) for each i ≥ 4 and we have g(i) < 1, then there are two positive constants such that for every integer j ≥ 4, the product ji=4 (1 − g(i)) lies between them. Using (4) and letting ft = ti=4 (1 − f(i)), we have that for t ≥ 3,

√3q3ft √t

t

- m − 1

- n 2 − t + m


1 −

qt =

. (6)

i=4

We now provide the proof of Theorem 6.

Proof of Theorem 6. Deﬁne α = γ2. Using (6) and the fact that m ≤ M ≤ b, we can ﬁnd positive constants c1 and c2 such that for every 3 ≤ t < (1 − α2)n 2, we have

c1q3 √t ≤ qt ≤

c2q3 √t

, (7)

where we use that n 2 is large in terms of α and b. From (5), we obtain that q70 ≤ q3 ≤ q50, provided that n 2 is large enough. Recall that q1 = q2 = 0. We also observe that qt ≤ qt−1 for every t ≥ 4 by (4). Thus, qt ≤ q(1−α

√√2t for all t > (1 − α2)n 2. Since qt is a probability distribution, it follows from (7) that

2)n 2 for every t > (1− α2)n 2. Observe that √ 1

(1−α2)n 2 ≤

n 2

n 2

√

1 √t ≤ 7q3 + 3c2q3 n 2 ,

qt ≤ 7q3 +

1 = q0 +

2c2q3

t=3

t=3

from where we obtain that q3 ≥ √c 1

n 2, for some positive constant c 1. Therefore, we conclude that the probability that t ≥ (1 − α)n 2 is at least

(1−α2 )n 2

c1c 1 (1 − α2) · n 2 ·

αn 2 2

c1c 1α 2 (1 − α2)

=: δ∗ .

qt ≥

=

t=(1−α)n 2

Now we are able to conclude the proof. Recall that α = γ2. Observe that n 2 = n2 − n∗2 ≥ n − 2M, since n∗2 ≤ M and n2 ≥ n − M. It follows that with probability δ∗ we have t ≥ (1 − α)n 2 ≥ (1 − 23γ)n. If this is the case, there are at most 23γn vertices in non-cyclic components, and thus, there is no component of order at least γn in such components. First, we apply Corollary 32 with t ≥ (1 − 23γ)n ≥ n2 and δ = 2γ, and obtain that the probability that there exists a cycle of length at least 2γt ≥ γn is at least δ1 > 0. Second, we apply Corollary 33 with t ≥ (1 − 23γ)n and = γ, and obtain that the probability that there exists no cycle of length at least γt ≤ γn is at least δ2 > 0. Let δ = min{δ1,δ2}. Finally, since this holds for every conditioning on H, m and n∗2, it also holds for the unconditioned statement and we have proved the theorem for δ = δ∗δ .

| |
|---|


We ﬁnish this section with two results that will be useful to proof Theorem 4 and 5.

- Lemma 35. For any positive constant β, if n 2 ≥ βM, then the probability that there are more than √nM 2 vertices in cyclic components of G is oM(1). Proof. Recall that by Observation 34 (a), we have M4 ≤ m ≤ M. We split the proof into two cases.

First, suppose that n 2 ≤ 2M. We use (6) to upper bound qt and obtain the desired probability. There exists some constant c > 0 such that

t≥√nM 2

qt ≤ c

t≥√nM 2

1 −

- m − 1

- n 2 + m


t−3

≤ c

t≥√nM 2

1 −

M/4 2M + M/4

t−3

≤ c

t≥√nM 2

- 8

- 9


t−3

≤ 9c

8 9

n 2/

√

M−3

= oM(1) ,

since n 2 ≥ βM.

Now, suppose that n 2 ≥ 2M. We use (6) to lower bound qt for every t ≤ n10 2. There exists some constant c > 0 such that,

qt ≥

cq3 n 2

1 −

m − 1 n 2 − n10 2 + m

t

≥

cq3 n 2

1 −

3M 2n 2

t

.

Since qt is a probability distribution and since n 2 ≥ 2M, we have

1 ≥

n 2/10

t=3

qt ≥

cq3 n 2

n 2/10

t=3

1 −

3M 2n 2

t

≥

cq3 n 2 ·

(1 − 23nM

2

)3 − (1 − 23nM

2

)n 2/10+1 1 − (1 − 23nM

2

)

=

c q3 n 2 M

,

for some c > 0, from which we conclude that q3 ≤ c √M

n 2. Now we use again (6) to upper bound the desired probability

t≥√nM 2

qt ≤

cq3 n 2/

√

M t≥√n 2

M

1 −

M/4 − 1 n 2 + M/4

t

≤

cM5/4 c n 2

t≥√nM 2

1 −

M 8n 2

t

≤

cM5/4 c n 2 ·

1 − 8Mn

2

√ n 2 M

1 − 1 − 8Mn

2

≤

8c c · M1/4e−

√

M/8 = oM(1) .

| |
|---|


- Lemma 36. For every positive constant β < 1001 , if n 2 ≥ βM the following is satisﬁed. Fix a choice of H and let UH be a union of some components of H with |E(UH)| ≥ βM. Let UG be the union of the corresponding components of G. Then, with probability 1 − oM(1),


16|E(UH)| M · n 2 + 4|E(UH)| .

|E(UH)| 8M · n 2 ≤ |V (UG)| ≤

Proof. Observe that the choice of H determines m , the number of edges that have not been ﬁxed in (1.1), and n∗2, the number of vertices of degree 2 which have been exposed in (1.2) or (1.3). We will also condition on nH2 , the number of vertices of degree 2 that have been exposed in (2.3). Since n 2 ≥ βM, by Lemma 35, the probability that nH2 ≤ n2 2 is oM(1). Hence, we may assume that nH2 ≥ n2 2.

We denote by n∗2(UH) the number of vertices of degree 2 exposed in (1.2) or (1.3) in a component of UH. By Observation 34 (b), we have

0 ≤ n∗2(UH) ≤ 2|E(UH)| .

We let m (UH) be the number of non-ﬁxed edges in UH. By Observation 34 (a), we have |E(UH)|

2 ≤ m (UH) ≤ |E(UH)|. Similarly, M4 = m2 ≤ m ≤ m = M2 . Thus, |E(UH)| M ≤

4|E(UH)| M

m (UH) m ≤

.

Let nH2 (UH) be the number of vertices of degree 2 which have been exposed in (2.3) to the edges of UH. Since the ordering of the edges in (2.1) was arbitrary, symmetry amongst the non-ﬁxed edges yields:

nH2 |E(UH)| M ≤ E[nH2 (UH)] =

nH2 m (UH) m ≤

4nH2 |E(UH)| M ≤

n 2|E(UH)| 2M ≤

4n 2|E(UH)| M

.

Since the minimum degree in H is at least one, there are at most 2|E(UH)| vertices in UH. So, the number of vertices in UG satisﬁes

nH2 (UH) ≤ |V (UG)| = |V (UH)| + n∗2(UH) + E[nH2 (UH)] ≤ nH2 (UH) + 4|E(UH)| .

Now, we will use our random permutation model to show that the random variable nH2 (UH) is concentrated around its expected value, which by the previous equation implies that |V (UG)| also is. In (2.1) we insist on choosing an ordering of the non-ﬁxed edges of H in such a way that the m (UH) ﬁrst ones correspond to E(UH).

The probability that nH2 (UH) ≥ conditional on the value of nH2 , is the same as the probability that in choosing m − 1 elements in {1,2,...,(m − 1 + nH2 )}, we choose less than

- m (UH) of them that are smaller than m (UH) + . So, since nH2 ≥ n2 2 ≥ βM2 , letting X be the number of elements chosen from the m − 1 ones which are smaller than m (UH) + , a standard concentration argument on X for = 4E[nH2 (UH)] 9, shows that with probability


- 1 − oM(1) we have nH2 (UH) ≤ 4E[nH2 (UH)]. The same holds for the probability of the event


nH2 (UH) ≥ E[n

H 2 (UH)]

4 , concluding the proof of the lemma.

| |
|---|


### 7 Relating the size of a component of H(D) to the order of a component of G(D)

As usual we use M = MD and R = RD throughout this section. We start with the proof of Theorem 4 and conclude the section with the proof of Theorem 5.

9Observe that X follows a hypergeometric distribution.

- Proof of Theorem 4. By Theorem 9 with = 1/3, there is a γ˜ such that if R ≥ M3 , then the probability that H has no component of size γM˜ is o(1). We will choose ρ to be the minimum of 30γ and γ˜. Hence we can assume that R ≤ M3 .

To complete the proof, we show that under this assumption, the probability G has a component of order 30ρn given H has no component of size ρM is o(1). Under this hypothesis, for every component K of H, we have |E(K)| ≤ ρM. Since each component is connected, this also implies that |V (K)| ≤ ρM + 1.

The following claim allow us to bound M in terms of n.

- Claim 5. If n2 is the number of vertices of degree 2 in D, then R ≥ M − 2(n − n2) .


Proof. Suppose that R < M − 2(n − n2). By the deﬁnition of jD, we obtain jD−1

k=1 dπk ≥ M + 2n2 − R > 2n. Since the function f(x) = x(x − 2) is convex,

jD−1

k=1

dπk(dπk − 2) > (jD − 1)

2n jD − 1

2n jD − 1 − 2 > 0,

which is a contradiction to the choice of jD. Thus R ≥ M − 2(n − n2).

| |
|---|


Since R ≤ M3 , Claim 5 implies M ≤ 3n. Condition now on the choice of H and on the set of ﬁxed edges and let m be the number

of non-ﬁxed ones. These choices determine n 2.

Suppose that n 2 ≤ ρn and recall that n∗2(K) ≤ 2|E(K)| by Observation 34. Then, deterministically, each component of G has at most |V (KH)|+n∗2(K)+n 2 ≤ 4ρM +1 ≤ 13ρn vertices.

Otherwise, n 2 ≥ ρn ≥ ρM3 . Group the components of H in sets U1,...,Us such that ρM

2 ≤ |E(Ui)| ≤ ρM. Clearly such a collection exists and s ≤ 2(ρ)−1. For every 1 ≤ i ≤ s, we apply Lemma 36 with UH = Ui and β = ρ4. Since D is well-behaved, the conclusion of Lemma 36 holds with probability 1−o(1). Using a union bound over all the sets Ui, we obtain that with probability 1 − o(1), for 1 ≤ i ≤ s, we have

|V (Ui)| ≤

16|E(Ui)| M · n 2 + 4|E(Ui)| ≤ 16ρn + 4ρM ≤ 28ρn .

| |
|---|


- Proof of Theorem 5. It is enough to prove the theorem for suﬃciently small positive ρ, for which we will prove it with γ = ρ3.


We can use Lemma 10 to show that if M ≥ nlog log n, then the probability G has no component of order (1 − o(1))n is o(1).

Next, suppose that M ≤ n3. We show that in this case, the probability that G has no component of order ρ3n given that H contains a component of size ρM is o(1). We have that

- n 2 ≥ n − 2M ≥ n3 ≥ M. Letting KH be the component of H of size at least ρM and KG be the component of G corresponding to KH, and applying Lemma 36 with UH = KH and β = ρ, we conclude that with probability 1 − o(1) (since D is well-behaved)


|E(KH)| 8M · n 2 ≥

ρn 24 ≥ ρ3n .

|V (KG)| ≥

Thus, it remains to prove the theorem for n 3 ≤ M ≤ nlog log n .

For any subgraph K of G, let ex(K) = |E(K)| − |V (K)| be the excess of K. We also deﬁne the near-excess of K as nex(K) = ex(K)+|L∩V (K)|, where L is the set of vertices of degree at least

√

M

logM in K. Let S be the set of vertices of G that correspond to a component K in H with nex(K) ≥ ρM2 .

The following claim is crucial to ﬁnish the proof of the theorem.

- Claim 6. We have P S = ∅,|S| < 3ρ2n = o(1) .

We now conclude the proof of the theorem, assuming that the claim is true. Suppose H contains a component KH that satisﬁes |E(KH)| ≥ ρM. If the corresponding component KG in G satisﬁes |V (KG)| ≥ ρ3n, there is nothing to prove. So, suppose |V (KG)| < ρ3n. Then

nex(KH) ≥ ex(KH) = |E(KH)| − |V (KH)| ≥ ρM − ρ3n ≥

ρM 2

, (8)

and S is non-empty.

Since the total excess of the graph is at most M, the total near-excess is at most M +|L| ≤ 3M/2 and there are at most ρ3 components in S. Hence, there exists a component in G with at least ρ|3S| vertices, which by Claim 6 implies that with probability 1−o(1), G has a component of order at least ρ3n.

So, it is indeed enough to prove Claim 6. To do so, we need the following:

- Claim 7. We have P


 S = ∅,

  = o(1) .

d(v) > M2/3

v∈L\S

Proof of Claim 7. We let A be the event that S = ∅, and for any vertex v ∈ L, we let Bv be the event that S = ∅, but v ∈/ S.

Say a graph G is in Bv. We only consider switchings between ordered pairs of oriented edges vx and yz in H, where yz is an edge in a component of H whose vertex set is in S, which is not a cut-edge and we allow that v = x or y = z.

Since yz is in a component of S and S = ∅, there are at least ex(S) ≥ ρM3 choices for yz. Clearly, there are d(v) choices for the (directed) edge vx.

We show below that there are at most 4M such switchings from any element of A \ Bv to Bv. Thus

12P[A \ Bv] ρd(v) ≤

12 ρd(v)

P[Bv] ≤

. So, we have,

 

  =

d(v)P[Bv] ≤ 12ρ−1|L| .

E

d(v)

v∈L

S =∅,v∈L\S

√

Since |L| ≤

M log M, Markov’s inequality implies that

 S = ∅,

  = o(1) ,

d(v) > M2/3

P

v∈L\S

and the claim follows.

It remains to prove the mentioned bound on the number of switchings between A\Bv and Bv. In doing so, we note that (i) if a connected subgraph J contains a subgraph of near-excess a, then J also has near-excess at least a, and (ii) the near-excess of the disjoint union of J1 and J2 is at least the sum of the near-excesses of J1 and J2.

Consider a graph G that is in A \ Bv. Let K be the component of H containing v and let K1,...,K be the components of K − (N(v) ∪ {v}). For each neighbour w of v, let Kw be the graph induced by w and all components in {K1,...,K } in which w has a neighbour.

In the following, we consider a triple of vertices x,y,z such that switching {vy,xz} leads to a graph in Bv such that the edge yz is not a cut-edge and the component containing y and z has near-excess at least ρM2 . We note that unless v = x, this implies there is at most one edge between v and y. We note further that v,x are distinct from y,z but z and y may coincide as may v and x.

- If v = x, then y and z are both neighbours of v in H and there are exactly two edges of

H from H − Kz − Ky to Kz ∪ Ky. Furthermore, there is a path of Kz ∪ Ky from z to y and the near-excess of Kz ∪Ky is at least ρM2−2. So, we see that there are at most two choices for the pair y,z and at most eight choices for switchings of this type.

- If v = x, then z must be in Ky and in H − xz there can be no path from z to any


of N(v) \ {y}. Thus, there is a unique choice of vy for each such ordered xz and at most

- 2M − 2d(v) total choices for such switchings. Proof of Claim 6. Let Z be the number of sets of vertices T that satisfy


| |
|---|


- (1) |T| ≤ 3ρ2n,
- (2) the sum of the degrees of the elements in T is at least ρM,
- (3) v∈L\T d(v) ≤ M2/3,
- (4) there are no edges between T and V (H) \ T.


Observe that S as deﬁned satisﬁes (2), since it is non-empty and each component in S has at least ρM2 edges. Since S is a union of components, it also satisﬁes (4).

We will show that E[Z] = o(1). This directly implies that the probability S satisﬁes (1) and (3) is at most o(1), which combined with Claim 7 yields Claim 6.

Fix a set of vertices T that satisﬁes (1), (2) and (3). For every 0 ≤ k ≤ k∗ := 2 ρn26 , let

AT,k be event that there are exactly k edges that connect T with V (H) \ T. There are at most k2 switchings from a graph in AT,k which yields a graph in AT,k−2. We now lower bound the number of switchings from a graph in AT,k−2, to a graph AT,k. To do so we consider pairs consisting of (i) an edge xy such that x ∈/ T and x is not a neighbour of a vertex in T ∪L, and (ii) an edge uv with both endpoints in T such that y is not adjacent simultaneously to both u and v. For such a pair, we can always switch xy with at least one of uv or vu. There are at least n−|T|−(k−2)−M2/3 > n2 choices for x, since T satisﬁes (3) and M ≤ nlog log n. Since d(x) ≥ 1, there are at least the same number of choices for the edge

√

√

2

= logM2 M edges within T that have both endpoint adjacent to y. Using that T satisﬁes (2) and that n ≤ 3M, we conclude that there are at least ρM2 − (k − 2) − logM2 M ≥ ρM4 choices for the edge uv, given the choice of xy. The total number of switchings is at least ρnM8 .

M

M log M

xy. Since y ∈/ L, we have d(y) ≤

logM which implies that there are at most

So, using that k ≤ k∗ and that n ≤ 3M

k2 ρnM 8

ρn 3M

P[AT,k−2] ≤

P[AT,k] ≤

P[AT,k] ≤ ρP[AT,k] .

Therefore,

∗

ρn

P[AT,0] ≤ ρk

2 P[AT,k∗] ≤ ρ

26 ;.

Since T satisﬁes (1), there are at most 3ρ n2n choices for T. Provided that ρ is small enough, we conclude that E[Z] = o(1).

| |
|---|


This completes the proof of Theorem 5.

| |
|---|


### 8 Applications of Theorem 3

We brieﬂy show that Theorem 3 implies the results mentioned in Section 1.4. We consider a sequence of degree sequence D = (Dn)n≥1 such that

- (d.1) it is feasible, smooth, and sparse,
- (d.2) λ2 < 1, and
- (d.3) λ = i≥1 iλi.


Conditions (d.1)–(d.3) are essentially BR-conditions and they are weaker than MR-conditions and JL-conditions. An interesting consequence of them is the following: for every > 0, there exist positive integers C and n such that if n ≥ n , then

ini ≤  n .

i≥C

Therefore, any sequence of degree sequences that satisﬁes (d.1)–(d.3) has almost all the edges incident to vertices of bounded degree.

The results of Molloy and Reed [24], Janson and Luczak [18], and Bollob´s and Riordan [5] on the existence of a giant component, are of the following form: provided that D satisﬁes certain conditions, if Q(D) > 0 then G(Dn) has a linear order component with probability 1 − o(1), and if Q(D) ≤ 0, then G(Dn) has no linear order component with probability 1 − o(1).10 We will show that if D satisﬁes (d.1)–(d.3), then Theorem 3 implies the same statement.

Theorem 37. Let D = (Dn)n≥1 be a sequence of degree sequences that satisﬁes conditions (d.1)–(d.3). Then,

1. if Q(D) > 0, then there exists a constant c1 > 0 such that the probability that G(Dn) has a component of order at least c1n is 1 − o(1).

10In fact, the Molloy-Reed result does not discuss the case Q(D) = 0.

2. if Q(D) ≤ 0, then for every constant c2 > 0, the probability that G(Dn) has no component of order at least c2n is 1 − o(1).

Proof. First of all, observe that (d.2) implies that D is well-behaved.

Fix δ > 0 small enough. Since λ = i≥1 iλi, there is an integer K such that Ki=1 iλi ≥ λ − δ. Also, since D is smooth and provided that n is large enough, we have

K

ni n

i λi −

< δ ,

i=1

and hence, as D is sparse,

ni n

i ·

< 3δ . (9)

i>K

Recall Q = Q(D) = i≥1 i(i − 2)λi. Assume ﬁrst that Q > 0. We will show that D is lower bounded. Fix γ > 0 such that Q > γ. Now note that there exists a positive integer k such that ki=1 i(i − 2)λi > γ2. Since D is smooth and provided that n is large enough, we have that for every 1 ≤ i ≤ k

ni n − i(i − 2)λi <

γ 4k

i(i − 2)

. Therefore,

k

ni n ≥

i(i − 2)

i=1

k

k

i(i − 2)λi −

i=1

i=1

ni n − i(i − 2)λi ≥

γ 4

i(i − 2)

.

Since every vertex of degree i ∈ [k] contributes in at most i(k − 2) to the previous sum, this implies RDn ≥ 4γk · n. Using that D is sparse and since n is large enough, we have that

i≥1 ini ≤ 2λn and hence MDn ≤ 2λn. Therefore, RDn ≥

γ 8λk · MDn

and thus, the sequence Dn is lower-bounded with = 8λkγ . Since it is also well-behaved, Theorem 3 implies that there exists a constant c1 > 0 such that the probability that G has a component of order at least c1n is 1 − o(1).

Now suppose that Q ≤ 0. We aim to show that D is upper bounded; that is, for every suﬃciently small > 0 and large enough n, we have RDn ≤  MDn. We ﬁx an arbitrary and suﬃciently small > 0. Observe ﬁrst that ki=1 i(i − 2)λi ≤ 0 for any positive integer k, as i(i − 2) ≥ 0 for every i ≥ 2.

Furthermore, for suﬃciently large n, the number of vertices of degree diﬀerent than 2 is at least 1−2λ2n. Since the minimum degree is at least one, MDn ≥ 1−4λ2n.

Using (9), we can choose K large enough such that

ni n

i ·

i>K

(1 − λ2) 8

<

.

As before, since D is smooth, we can consider n large enough such that for every 1 ≤ i ≤ K, we have |i(i − 2)nni − i(i − 2)λi| < (1−8Kλ2) . Therefore,

K

K

K

(1 − λ2) 8

ni n ≤

ni n − i(i − 2)λi ≤ 0 +

i(i − 2)

i(i − 2)λi +

i(i − 2)

.

i=1

i=1

i=1

Because i ≤ i(i − 2) for every i ≥ 3, this implies

(1 − λ2) 8

RDn ≤

i · ni

n +

i>K

(1 − λ2)

4 · n ≤  MDn .

≤

Note that the choice of was arbitrary and thus D is upper-bounded. Since it is also wellbehaved, Theorem 3 implies that for every constant c2 > 0, the probability that G has no component of order at least c2n is 1 − o(1).

| |
|---|


Theorem 3 can be also applied to obtain results on the existence of a giant component in speciﬁc models of random graphs. Here, as an example, we will study the case of the PowerLaw Random Graph introduced by Aiello, Chung and Lu [1]. Let us ﬁrst recall its deﬁnition. Choose two parameters α,β > 0 and consider the sequence of degree sequences D = (Dn)n≥1 where Dn has ni(n) = eαi−β vertices of degree i, for every i ≥ 1. We should think about these parameters as follows: α is typically large and determines the order of the graph (we always have α = Θ(log n)), and β is a ﬁxed constant that determines the power-decay of the degree sequence. The total number of vertices, can be determined in terms of α and β,

 

ζ(β)eα if β > 1 αeα if β = 1

n ≈

α β



e

1−β if 0 < β < 1 and similarly for the number of edges

 

- 1

- 2ζ(β − 1)eα if β > 2


- 1 4αeα if β = 2

- 1

- 2


e

2α β

- 2−β if 0 < β < 2


m ≈



where ζ(x) = i≥1 i−x is the standard zeta function. Moreover, the maximum degree is eα/β.

The Power-Law Random Graph, denoted by G = G(α,β), is a graph on n vertices chosen uniformly at random among all such graphs with degree sequence Dn. There are some values of β (for instance β = 1) for which D does not satisfy the conditions (d.1)–(d.3). Thus,

- Theorem 37 cannot be used in general.


Nevertheless, observe that for every α,β > 0, we have n2 ≤ n2, and thus, the asymptotic degree sequence is well-behaved. This in particular implies that MDn ≥ 2m − n.

Let β0 = 3.47875... be a solution to the equation ζ(β − 2) − 2ζ(β − 1) = 0. This is the important threshold for the appearance of the giant component since β ≥ β0 if and only if

ni n ≤ 0 . (10)

i(i − 2)

i≥1

We refer the reader to the beginning of Section 3 in [1] for a formal proof of this fact. Thus for β ≥ β0, the parameter RDn is simply the maximum degree of G, which is e

α

###### β . Since β0 > 1, we have RDn MDn.

- Theorem 38 (Aiello, Chung and Lu). Let G = G(α,β) be a Power-Law random graph. Then,


- 1. if β < β0, then there exists a constant c1 > 0 such that the probability that G has a component of order at least c1n is 1 − o(1).
- 2. if β ≥ β0, then for every constant c2 > 0, the probability that G has no component of order at least c2n is 1 − o(1).


We want to emphasize that the structural description the authors give in their paper is more precise than the just mentioned result.

Proof. We already addressed the case β ≥ β0 before the theorem. In such a case, the sequence D is upper-bounded and it follows from Theorem 3 that for every constant c2 > 0, the probability that G has no component of order at least c2n is 1 − o(1).

Now, we consider β < β0. We will show that in this case D is lower-bounded. We split its proof into three cases, Case 0 < β ≤ 2: Suppose β = 2. The number of edges is of order e

2α

###### β and thus the average degree is of order e(

2

β−1)α, which tends to ∞ as α → ∞. Thus, provided that n is large

enough, we have RDn ≥ M2Dn . The same argument applies for β = 2, as the average degree is of order α = Θ(log n).

- Case 2 < β < 3: Let k be the smallest integer such that ki=1 i2−β > 4ζ(β − 1). Thus k

i=1

i(i − 2)eαi−β ≥ eα

k

i=1

i2−β − 2

∞

i=1

i1−β ≥

2ζ(β − 1)

ζ(β) · n. Therefore,

RDn ≥

e

α β

i=k+1

i ·

eα iβ ≥ cMDn,

for some small constant c = c(β) > 0. Here we used that MD ≥ 2m−n ≈ (ζ(β −1)−ζ(β))eα.

- Case 3 ≤ β < β0: Suppose now that β > 3 (the case β = 3 is similar to what follows). Let


= ζ(β − 2) − 2ζ(β − 1) and k be the smallest integer i such that (β−3)1kβ−3 < 2. Using an integral approximation of the sum, we obtain ki=1 i2−β ≈ ζ(β − 2) − (β−3)1kβ−3. Thus

k

i(i − 2)eαi−β ≥ eα

i=1

k

i2−β − 2

i=1

∞

i1−β ≥ 2ζ(β) · n.

i=1

As in the previous case, we have RDn ≥ cMDn for some constant c = c(β) > 0.

Since D is well-behaved and lower-bounded for β < β0, we can use Theorem 3 to conclude that there exists a constant c1 > 0 such that the probability that G has a component of order at least c1n is 1 − o(1).

| |
|---|


### References

- [1] W. Aiello, F. Chung, and L. Lu, A random graph model for massive graphs, Proceedings of the thirty-second annual ACM Symposium on Theory of Computing (STOC), ACM, 2000, pp. 171–180.
- [2] R. Albert and A.-L. Barab´si, Statistical mechanics of complex networks, Reviews of modern physics 74 (2002), 47.
- [3] A.-L. Barab´si and R. Albert, Emergence of scaling in random networks, science 286

(1999), no. 5439, 509–512.

- [4] S. Boccaletti, V. Latora, Y. Moreno, M. Chavez, and D.-U. Hwang, Complex networks: Structure and dynamics, Physics reports 424 (2006), 175–308.
- [5] B. Bollob´s and O. Riordan, An old approach to the giant component problem, J. Combin. Theory (Series B) 113 (2015), 236–260.
- [6] V. Bourassa and F. Holt, SWAN: Small-world wide area networks, Proceeding of International Conference on Advances in Infrastructures (SSGRR 2003w), L’Aquila, Italy, 2003.
- [7] C. Cooper, The cores of random hypergraphs with a given degree sequence, Random Structures Algorithms 25 (2004), 353–375.
- [8] C. Cooper, M. Dyer, and C. Greenhill, Sampling regular graphs and a peer-to-peer network, Comb., Probab. Comput. 16 (2007), 557–593.
- [9] M. Faloutsos, P. Faloutsos, and C. Faloutsos, On power-law relationships of the internet topology, ACM SIGCOMM computer communication review, vol. 29, ACM, 1999, pp. 251–262.
- [10] D. Fernholz and V. Ramachandran, Cores and connectivity in sparse random graphs, The University of Texas at Austin, Department of Computer Sciences, technical report TR-04-13 (2004).
- [11] , The diameter of sparse random graphs, Random Structures Algorithms 31

(2007), 482–516.

- [12] P. Flajolet and R. Sedgewick, Analytic combinatorics, Cambridge University Press, 2009.
- [13] N. Fountoulakis, Percolation on sparse random graphs with given degree sequence, Internet Mathematics 4 (2007), 329–356.
- [14] N. Fountoulakis and B. Reed, A general critical condition for the emergence of a giant component in random graphs with given degrees, Electronic Notes in Discrete Mathematics 34 (2009), 639–645.
- [15] C. Greenhill, The switch markov chain for sampling irregular graphs, Proceedings of the Twenty-Sixth Annual ACM-SIAM Symposium on Discrete Algorithms, SIAM, 2015, pp. 1564–1572.
- [16] H. Hatami and M. Molloy, The scaling window for a random graph with a given degree sequence, Random Structures Algorithms 41 (2012), 99–123.


- [17] S. Janson, On percolation in random graphs with given vertex degrees, Electron. J. Probab. 14 (2009), 87–118.
- [18] S. Janson and M. J. Luczak, A new approach to the giant component problem, Random Structures Algorithms 34 (2009), 197–216.
- [19] S. Janson and M.J. Luczak, A simple solution to the k-core problem, Random Structures Algorithms 30 (2007), 50–62.
- [20] A. Joseph, The component sizes of a critical random graph with pre-described degree sequence, The Annals of Applied Probability 24 (2014), 2560–2594.
- [21] M. Kang and T. G. Seierstad, The critical phase for random graphs with a given degree sequence, Comb., Probab. Comput. 17 (2008), 67–86.
- [22] T. Luczak, Sparse random graphs with a given degree sequence, Proceedings of the Symposium on Random Graphs, Poznan, 1989, pp. 165–182.
- [23] B. D. McKay, Subgraphs of random graphs with speciﬁed degrees, vol. 33, 1981, pp. 213– 223.
- [24] M. Molloy and B. Reed, A critical point for random graphs with a given degree sequence, Random Structures Algorithms 6 (1995), 161–180.
- [25] , The size of the giant component of a random graph with a given degree sequence, Comb., Probab. Comput. 7 (1998), 295–305.

- [26] , Graph colouring and the probabilistic method, vol. 23, Springer Science & Business Media, 2013.

- [27] M. E. J. Newman, The structure and function of complex networks, SIAM review 45

(2003), 167–256.

- [28] M. E. J. Newman, D.J. Watts, and S.H. Strogatz, Random graph models of social networks, Proceedings of the National Academy of Sciences 99 (2002), no. suppl 1, 2566– 2572.
- [29] J. Petersen, Die Theorie der regul¨aren graphs, Acta Math. 15 (1891), 193–220.
- [30] O. Riordan, The phase transition in the conﬁguration model, Comb., Probab. Comput. 21 (2012), 265–299.
- [31] H. van den Esker, R. van der Hofstad, G. Hooghiemstra, and D. Znamenski, Distances in random graphs with inﬁnite mean degrees, Extremes 8 (2005), no. 3, 111–141.
- [32] R. van der Hofstad, G. Hooghiemstra, and P. van Mieghem, Distances in random graphs with ﬁnite variance degrees, Random Structures Algorithms 27 (2005), 76–123.
- [33] N. C. Wormald, Some problems in the enumeration of labelled graphs, Doctoral Thesis

(1980).

- [34] , Models of random regular graphs, Surveys in combinatorics, 1999 (Canterbury), London Math. Soc. Lecture Note Ser., vol. 267, Cambridge Univ. Press, Cambridge, 1999, pp. 239–298.


