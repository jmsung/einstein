---
type: source
kind: paper
title: Very large graphs
authors: Laszlo Lovasz
year: 2009
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/0902.0132v1
source_local: ../raw/2009-lovasz-very-large-graphs.pdf
topic: general-knowledge
cites:
---

arXiv:0902.0132v1[math.CO]1Feb2009

Very large graphs

Laszl´ o´ Lovasz´ ∗ December 2008

Dedicated to the memory of Oded Schramm

## Contents

- 1 Introduction 3

- 1.1 Huge networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
- 1.2 What to ask about them? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- 1.3 How to obtain information about them? . . . . . . . . . . . . . . . . . . . . . . . 5

- 1.3.1 Local sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 1.3.2 Observing global processes . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 1.3.3 Left and right homomorphisms . . . . . . . . . . . . . . . . . . . . . . . . 6


- 1.4 How to model them? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

- 1.4.1 Random graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
- 1.4.2 Randomly growing graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
- 1.4.3 Quasirandom graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8


- 1.5 How to approximate them? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

- 1.5.1 The distance of two graphs . . . . . . . . . . . . . . . . . . . . . . . . . . 9
- 1.5.2 Approximation by smaller: Regularity Lemma . . . . . . . . . . . . . . . 9
- 1.5.3 Approximation by inﬁnite: convergence and limits . . . . . . . . . . . . . 10
- 1.5.4 Optimization problems for graphs . . . . . . . . . . . . . . . . . . . . . . 12


- 1.6 Mathematical tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


- 2 Graph parameters 13


- 2.1 Connection matrices and reﬂection positivity . . . . . . . . . . . . . . . . . . . . 13
- 2.2 Homomorphisms from the left . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

- 2.2.1 Versions of homomorphism numbers . . . . . . . . . . . . . . . . . . . . . 13
- 2.2.2 Spectra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


- 2.3 Homomorphisms to the right . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15


- 2.3.1 Colorings and independent sets . . . . . . . . . . . . . . . . . . . . . . . . 15
- 2.3.2 Multicuts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15


![image 1](<2009-lovasz-very-large-graphs_images/imageFile1.png>)

∗Research sponsored by OTKA Grant No. 67867.

- 2.3.3 Statistical physics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
- 2.4 Homomorphisms densities in the sparse case . . . . . . . . . . . . . . . . . . . . . 18
- 2.5 Characterizing homomorphism numbers . . . . . . . . . . . . . . . . . . . . . . . 18

- 2.5.1 Reﬂection positivity and extremal graph theory . . . . . . . . . . . . . . . 19
- 2.5.2 Finite connection rank . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19


- 2.6 Graph algebras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20


- 3 Graph-like structures on probability spaces 22

- 3.1 Graphons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

- 3.1.1 Homomorphisms into graphons and from graphons . . . . . . . . . . . . . 23
- 3.1.2 W-random graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24


- 3.2 Graphings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24


- 3.2.1 Measure preserving graphs . . . . . . . . . . . . . . . . . . . . . . . . . . 24
- 3.2.2 Graphings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
- 3.2.3 Random countable rooted graphs . . . . . . . . . . . . . . . . . . . . . . . 26


- 4 The cut-distance of two graphs 26

- 4.1 Two graphs on the same set of nodes . . . . . . . . . . . . . . . . . . . . . . . . . 26
- 4.2 Two graphs with the same number of nodes . . . . . . . . . . . . . . . . . . . . . 27
- 4.3 Two arbitrary graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
- 4.4 Distance of graphons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28


- 5 Szemer´edi partitions 29

- 5.1 ε-regular bipartite graphs and the original lemma . . . . . . . . . . . . . . . . . . 29
- 5.2 Weak Regularity Lemma and distance of graphs . . . . . . . . . . . . . . . . . . 30
- 5.3 Strong Regularity Lemma and compactness . . . . . . . . . . . . . . . . . . . . . 31
- 5.4 Partitions into sets with small diameter . . . . . . . . . . . . . . . . . . . . . . . 32

- 5.4.1 Small diameter sets and regularity . . . . . . . . . . . . . . . . . . . . . . 32
- 5.4.2 Computational applications . . . . . . . . . . . . . . . . . . . . . . . . . . 32


- 5.5 Regularity Lemmas for bounded degree graphs? . . . . . . . . . . . . . . . . . . . 34


- 6 Convergence and limits I: the dense case 34


- 6.1 Subgraph sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
- 6.2 Convergence in distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
- 6.3 Convergence from the right . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
- 6.4 Sampling and distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
- 6.5 Dense limit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

- 6.5.1 Equivalent descriptions of the limit . . . . . . . . . . . . . . . . . . . . . . 39
- 6.5.2 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40


- 6.6 Convergence from the right . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
- 6.7 Limits of other dense combinatorial structures . . . . . . . . . . . . . . . . . . . . 42


- 7 Convergence and limits II: bounded degree graphs 42 7.1 Neighborhood sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42 7.2 Local (weak) limit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

7.2.1 Diﬀerent forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43 7.2.2 Is the limit informative enough? . . . . . . . . . . . . . . . . . . . . . . . 43

7.3 Convergence from the right . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

- 8 Testing 45

- 8.1 Sample concentration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
- 8.2 Parameter estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
- 8.3 Dense property testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
- 8.4 Sparse property testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49


- 9 Extremal graph theory 50


- 9.1 Some classical results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
- 9.2 Algebraic proofs of extremal graph results . . . . . . . . . . . . . . . . . . . . . . 51
- 9.3 Positivstellensatz for graphs and spectral norms . . . . . . . . . . . . . . . . . . . 53
- 9.4 The maximum distance from a hereditary graph property . . . . . . . . . . . . . 54
- 9.5 Which graphs are extremal? (Finitely forcible graphons) . . . . . . . . . . . . . . 54


## 1 Introduction

- 1.1 Huge networks


In the last decade it became apparent that a large number of the most interesting structures and phenomena of the world can be described by networks: separable elements, with connections (or interactions) between certain pairs of them.

- • Among such a networks, the best known and the most studied is the internet. Moreover, the internet (as the physical underlying network) gives rise to many of the networks: the network of hyperlinks (web, logical Internet), Internet based social networks, distributed data bases, etc. The size of the internet is growing fast: currently the number of web pages may be 30 billion or more, and the number of devices is probably more than a billion.
- • Social networks are basic objects of many studies in the area of sociology, history, epidemiology and economics. The largest social network is the acquaintance graph of all living people, with about 7 billion nodes.
- • Biology contributes ecological networks, networks of interactions between proteins, and the human brain, just to mention a few. The human brain is really large for its mass, having about 1011 nodes.
- • Statistical physics studies the interactions between large numbers of discrete particles, where the underlying structure is often described by a graph. For example, a crystal can be though of as a graph whose nodes are the atoms and whose edges represent chemical


- bonds. A perfect crystal is a rather boring graph, but impurities and imperfections create interesting graph-theoretical digressions. 12 gram of a diamond has about 6 × 1023 nodes.
- • Some of the largest networks in engineering occur in chip design. Even though these networks are man-made and planned, many of their properties are diﬃcult to determine by computation due to their huge size. There can be more than a billion transistors on a chip now.
- • To be pretentious, we can say that the whole universe is a single (really huge, possibly inﬁnite) network, where the nodes are events (interactions between elementary particles), and the edges are the particles themselves. This is a network with perhaps 1080 nodes.


These huge networks pose exciting challenges for the mathematician. Graph Theory (the mathematical theory of networks) has been one of the fastest developing areas of mathematics in the last decades; with the appearance of the Internet, however, it faces fairly novel, unconventional problems. In traditional graph theoretical problems the whole graph is exactly given, and we are looking for relationships between its parameters or eﬃcient algorithms for computing its parameters. On the other hand, very large networks (like the Internet) are never completely known, in most cases they are not even well deﬁned. Data about them can be collected only by indirect means like random local sampling or by monitoring the behavior of various global processes.

Dense networks (in which a node is adjacent to a positive percent of others nodes) and sparse networks (in which a node has a bounded number of neighbors) show a very diverse behavior. From a practical point of view, sparse networks are more important, but at present we have more complete theoretical results for dense networks.

- 1.2 What to ask about them?


Let us discuss three possible questions that can be asked about a really large graph, say the internet.

Question 1. Does the graph have an odd number of nodes? This is a very basic property of a graph in the classical setting. For example, it is one of

the ﬁrst theorems or exercises in a graph theory course that every graph with an odd number of nodes has a node with even degree.

But for the internet, this question is clearly nonsense. Not only does the number of nodes change all the time, with devices going online and oﬄine, but even if we ﬁx a speciﬁc time like 12:00am today, it is not well-deﬁned: there will be computers just in the process of booting up, breaking down etc.

Question 2. What is the average degree of nodes?

This, on the other hand, is a meaningful question. Of course, the average degree can only be determined with a certain error, and it will change with technology or the social composition of users; but at a given time, a good approximation can be sought (I am not speaking now about how to ﬁnd it).

Question 3. Is the graph connected?

To this question, the answer is almost certainly no: somewhere there will be a faulty router with some unhappy users on the wrong side of it. But this is not the interesting way to ask the question: we should consider the internet disconnected if, say, an earthquake combined with a sunﬂare severs all connections between the Old and New worlds. So we want to ignore small components that are negligible with respect to the whole graph, and consider the graph disconnected only if it decomposes into two parts which are commeasurable with the whole. On the other hand, we may want to allow that the two parts be connected by a few edges, and still consider the graph disconnected.

Question 4. Find the largest cut in the graph.

(This means to ﬁnd the partition of the nodes into two classes so as to maximize the number of edges connecting the two classes.) This example shows that even if the question is meaningful, it is not clear in what form can we expect the answer. The fraction of edges contained in the largest cut can be determined relatively easily (with and error that is small with large probability); but how to specify the largest cut itself (or even an approximate version of it)?

- 1.3 How to obtain information about them?


If we face a large network (think of the internet) the ﬁrst challenge is to obtain information about it. Often, we don’t even know the number of nodes.

- 1.3.1 Local sampling


Properties of very large graphs can be studied by sampling small subgraphs. The theory of this, called property testing in computer science, emerged in the last decade, and will be one of the main concerns of this paper.

In the case of dense graphs G, the sampling process is simple: we select independently a ﬁxed number k of random nodes, and determine the edges between them, to get a random induced subgraph. We’ll call this subgraph sampling. For each graph F, this deﬁnes a probability of seeing F when |V (F)| nodes are sampled, and so it gives a probability distribution σG,k on all graphs with k (labeled) nodes. It turns out that this sample contains enough information to determine many properties and parameters of the graph (with an error that is with large probability arbitrarily small if k is suﬃciently large depending only on the error bound).

To get a mathematically exact description of algorithms for very large graphs, we deﬁne a subgraph sampling oracle as a black box that, for a given positive integer m, returns a random mnode graph from some (otherwise unknown) distribution. We think of this as a random induced subgraph of a very large, otherwise unknown graph G. We assume that the oracle is consistent in the sense that for any k there is a graph G such that the distribution of the k-samples from G is arbitrarily close to the distribution of the answers by the oracle. (Theorem 6.13 will give a characterization of consistent distributions.)

In the case of sparse graphs with bounded degree, the subgraph sampling method gives a trivial result: the sampled subgraph will almost certainly be edgeless. Probably the most natural

way to ﬁx this is to consider neighborhood sampling. Let Gd denote the class of ﬁnite graphs with all degrees bounded by d. For G ∈ Gd, select a random node and explore its neighborhood to a given depth m. This provides a probability distribution ρG,m on graphs in Gd, with a speciﬁed root node, such that all nodes are at distance at most m from the root. We will shortly refer to these rooted graphs as m-balls. Note that the number of possible m-balls is ﬁnite if d and m are ﬁxed. We can formulate this abstractly as a neighborhood sampling oracle, a black box that, for a given positive integer m, returns an m-ball.

The situation for sparse graphs is, however, less satisfactory than for dense graphs, for two reasons. First, a full characterization of consistent neighborhood sampling oracles is not known (cf. Conjecture 7.2). Second, neighborhood sampling does not reveal important global properties of the graph like expansion. This suggests looking at further possibilities. Suppose, for example, that instead of exploring the neighborhood of a single random node, we could select two (or more) random nodes and determine simple quantities associated with them, like pairwise distances, maximum ﬂow, electrical resistance, hitting times of random walks. What information can be gained by such tests? Is there a “complete” set of tests that would give enough information to determine the global structure of the graph to a reasonable accuracy? These methods should lead to diﬀerent theories of large graphs and their limit objects, largely unexplored.

Sample distribution (in both the dense and sparse cases) are equivalent to counting induces subgraphs of a given type. Instead of this, we could count homomorphism (or injective homomorphisms) of a “small” graphs into the graph. The connection with sample distribution can be expressed by inclusion-exclusion formulas, and it is not essential. Often homomorphism numbers are algebraically better behaved, and they also have the advantage that they suggest diﬀerent, “dual” approaches by reversing the arrows in the category of graph homomorphisms.

- 1.3.2 Observing global processes

Another source of information about a network is the observation of the behavior of various global processes either globally (through measuring some global parameter), or locally (at one node, or a few neighboring nodes, but for a longer time). Statistical physical models on the graph are examples of the ﬁrst kind of approach (we return to them in section 2.3.3). Crawlers can be considered as examples of the second, and there are some sporadic results about the local observation of simpler, random processes [14, 15]. A general theory of such local observation has not emerged yet though.

- 1.3.3 Left and right homomorphisms


Instead of testing, it is often more convenient to talk about homomorphisms (adjacencypreserving maps) between graphs. This leads to the following setup. If we are given a (large) graph G, we may try to study its local structure by counting homomorphisms from various “small” graphs F into G; and we can study its global structure by counting its homomorphisms into various small graphs H. The ﬁrst type of information is closely related (in many cases, equivalent) to sampling, while the second is related to statistical physics. As in statistical physics, one needs weighted graphs H here to get meaningful results.

- 1.4 How to model them?


- 1.4.1 Random graphs

We are celebrating the 50-th birthday of random graphs this year: The simplest random graph model was developed by Erdo˝s and R´enyi [44] and Gilbert [55] in 1959. Given a positive integer n and a real number 0 ≤ p ≤ 1, we generate a random graph G(n,p) by taking n nodes, say [n] = {1,...,n}, and connecting any two of them with probability p, making an independent decision about every pair.

There are alternate models, essentially equivalent: we could ﬁx the number of edges m, and then choose a random m-element subset of the set of pairs in [n], uniformly from all such subsets. This random graph G(n,m) is very similar to G(n,p) when m = p n2 . Another model, closer to some of the more recent developments, is evolving random graphs, where edges are added one by one, always choosing uniformly from the set of unconnected pairs. Stopping this process after m steps, we get G(n,m).

Erdo˝s–R´enyi random graphs have many interesting, often surprising properties, and a huge literature, see [20, 68]. One conventional wisdom about random graphs with a given edge density is that they are all alike. Their basic parameters, like chromatic number, maximum clique, triangle density, spectra etc. are highly concentrated. This fact will be an important motivation when deﬁning the right measure of global similarity of graphs.

Many generalizations of this random graph model have been studied. For example, one could have diﬀerent probabilities assigned to diﬀerent edges. A variation of this idea, discovered independently in [85], [22] and perhaps elsewhere, is the notion of W-random graphs, to be discussed in section 3.1.2 and used throughout these notes.

- 1.4.2 Randomly growing graphs


Random graph models on a ﬁxed set of nodes, discussed above, fail to reproduce important properties of real-life networks. For example, the degrees of Erdo˝s–R´enyi random graphs follow a binomial distribution, and so they are asymptotically normal if the edge probability p is a constant, and asymptotically Poisson if the expected degree is constant (i.e., p = p(n) ∼ c/n). In either case, the degrees are highly concentrated around the mean, while the degrees of real life networks tend to obey the “Zipf phenomenon”, which means that the tail of the distribution decreases according to a power law.

In 2002 Albert and Baraba´si [1, 13] created a random network model growing according to natural rules, which could reproduce this behavior. Since then a lot of variations of growing networks were introduced. The process of graph generation usually consists of random steps obeying some local rules.

This is perhaps the ﬁrst point which suggests one of our main tools, namely assigning limits to sequences of graphs. Just as the Law of Large Numbers tells us that adding up more and more independent random variables we get an increasingly deterministically behaving number, these growing graph sequences tend to have a well-deﬁned structure, independent of the random choices made along the way. In the limit, the randomness disappears, and the asymptotic

behavior of the sequence can be described by a well-deﬁned limit object. You will ﬁnd more on this in Sections 1.5.3 and 6.5.

- 1.4.3 Quasirandom graphs


The theory of quasirandom graphs, introduced by Thomason [117] and Chung, Graham and Wilson [33], is based on the following observation: not only have random graphs a variety of quite strict properties (with large probability), but for several of these basic properties, the exceptional graphs are the same. In other words, any of these properties implies the others, regardless of any stochastic consideration.

To make this idea precise, we consider a sequence of graphs (Gn) with |V (Gn)| → ∞. For simplicity, assume that |V (Gn)| = n. Let 0 < p < 1 be a real number. Consider the following properties of these graphs.

- (P1) All degrees are asymptotically pn and all codegrees (numbers of common neighbors of

two nodes) are asymptotically p2n.

- (P2) For every ﬁxed graph F, the number of homomorphisms of F into Gn is asymptotically

p|E(F)|n|V(F)|.

- (P3) The number of edges is asymptotically pn2/2 and the number of 4-cycles is asymptoti-

cally p4n4/8.

- (P4) The number of edges induced by a set of nodes of size αn is asymptotically pα2n2/2.


All these properties hold with probability 1 if Gn = G(n,p). However, more is true: if a graph sequence satisﬁes either one of them, then it satisﬁes all [33]. Such graph sequences are called quasirandom. The four properties above are only a sampler; there are many other random-like properties that are also equivalent to these [33, 108, 109].

Many interesting deterministic graph sequences are quasirandom. We mention an important example from number theory:

- Example 1.1 Paley graphs. Let pn be the n-th prime congruent 1 modulo 4, and let us deﬁne a graph on {1,...,pn} by connecting i and j if and only if i − j is a quadratic residue. The Paley graphs converge to the function W ≡ 1/2.


The theory of convergent graph sequences (Section 6) can be considered as a rather farreaching generalization of quasirandom sequences.

- 1.5 How to approximate them?


We want a compact approximate description of a very large network, usually in the form a (relatively) small networks or at least a network with a compact description. To make this mathematically precise, we need to deﬁne what we mean by two graphs to be “similar” or “close”, and describe what kind of structures we use for approximation.

- 1.5.1 The distance of two graphs

There are many ways of deﬁning the distance of two graphs G and G′. Suppose that the two graphs have a common node set [n]. Then a natural notion of distance is the edit distance, deﬁned as the number of edges to be changed to get from one graph to the other. Since our graphs are very large, we want to normalize this, and deﬁne

d1(G,G′) = |E(G)△E(G′)|

![image 2](<2009-lovasz-very-large-graphs_images/imageFile2.png>)

n 2

.

While this distance plays an important role in the study of testable graph properties, it does not reﬂect structural similarity well. To raise one objection, consider two random graphs on [n] with edge-density 1/2. As mentioned in the introduction, these graphs are very similar from almost every aspect, but their normalized edit distance is large (about 1/2 with large probability). One might try to improve this by relabeling one of them to get the best overly minimizing the edit distance; but the improvement would be marginal (o(1)).

Another trouble with the notion of edit distance is that it is only deﬁned when the two graphs have the same number of nodes.

We could base the measurement of distance on sampling. We deﬁne the sampling distance of two graphs G and G′ by

dsample(G,G′) =

∞

k=1

- 1

![image 3](<2009-lovasz-very-large-graphs_images/imageFile3.png>)

- 2k


dtv(σG,k,σG′,k) (1)

(where dtv(α,β) = supX |α(X) − β(X)| denotes the total variation distance of the distributions α and β). Here the coeﬃcients 1/2k are quite arbitrary, only to make the sum convergent. This distance, however, would not directly reﬂect any structural similarity.

In section 4 we will deﬁne a further distance between graphs, which will be satisfactory from all these points of view: it will be deﬁned for two graphs with possibly diﬀerent number of nodes, the distance of two random graphs with the same edge density will be very small, and it will reﬂect global structural similarity. It will deﬁne the same topology as dsample.

The construction of the sampling distance can be carried over to bounded degree graphs, by replacing in (1) the sampling distributions σG,k by the neighborhood distributions ρG,k. We must point out, however, that it seems to be diﬃcult to deﬁne a notion of distance between two graphs with bounded degree reﬂecting global similarity.

- 1.5.2 Approximation by smaller: Regularity Lemma


As the exact description of huge networks is not known, and they are too big for direct study (e.g., for testing diﬀerent algorithms or protocols directly on the whole internet), an important operation would be to “scale down” by producing a smaller network with similar properties. The main tool for doing so is the “Szemer´edi-partition” or “regularity Lemma”. Szemer´edi developed his Regularity Lemma for his celebrated proof of the Erdo˝s–Tur´an Conjecture on arithmetic progressions in dense sets of integers in 1975. Since then, the Lemma has emerged as a fundamental tool in graph theory, with many applications in extremal graph theory, combinatorial number theory, graph property testing etc., and became a true focus of research in the past years.

This lemma can be viewed as an archetypal example of dichotomy between randomness and structure, where we try to decompose a (large and complicated) object A into a more highly structured object A′ with a (quasi)random perturbation (cf. Tao [116]). The highly structured part may be easier to handle, the quasirandom part will often be simpler due to Laws of Large Numbers. We’ll introduce this partition in section 5 (and use it throughout).

Finding the Szemer´edi partition of a huge dense graph is an example of the problem posed in Question 4 in Section 1.2. Algorithm 5.4.2 will be an example of a possible solution: how a partition of the nodes can be determined in an implicit form, even if describing for each node which class it belongs to would take too much space.

- 1.5.3 Approximation by inﬁnite: convergence and limits


This idea can be motivated by how we look at a large piece of metal. This is a crystal, that is a really large graph consisting of atoms and bonds between them. But from many points of view (e.g., the use of the metal in building a bridge), it is more useful to consider it as a continuum with a few important parameters (density, elasticity etc.). Its behavior is governed by diﬀerential equations. Can we consider a more general very large graph as some kind of continuum?

One way to make this intuition precise is to consider a growing sequence (Gn) of graphs whose number of nodes tends to inﬁnity, and to deﬁne when such a sequence is convergent. (We have mentioned this idea in connection with randomly growing graphs, but now we don’t assume anything about how the graphs in the sequence are obtained.) Our discussion of sampling suggests a general principle leading to a deﬁnition: we consider samples of a ﬁxed size k from Gn, and their distribution. We say that the sequence is locally convergent (with respect to the given sampling method) if this distribution tends to a limit as n → ∞ for every ﬁxed k. The family of limiting distributions (one for each k) can be considered as a limit object of the sequence.

For dense graphs, this notion of convergence was suggested by Erdo˝s, Lov´asz and Spencer [43], and elaborated by Borgs, Chayes, Lov´asz, So´s, Szegedy and Vesztergombi [28, 29, 30]. For sparse graphs, this kind of convergence was introduced by Aldous [2] and by Benjamini and Schramm [16]. These notions will be discussed in Sections 6.1 and 7.1, respectively.

The deﬁnition above represents the limit of a graph sequence as a collection of probability distributions on graphs, one for each sample size. This is not always a helpful representation of the limit object, and a more explicit description is desirable. A next step is to represent the family of distributions on ﬁnite graphs (the samples) by a single probability distribution on countable graphs. For sparse graphs, Benjamini and Schramm provide such a description as certain measures on countable rooted graphs with bounded degree (see section 3.2, and a similar description for dense graph limits is also known as certain ergodic measures on countable graphs ([111]; see Theorem 6.13).

More explicit descriptions of these limit objects can also be given. Let us start with the dense case. Here the limit object can be described as a two-variable measurable function W : [0,1]2 → [0,1], called a graphon (Lov´asz and Szegedy [85]; see Section 3.1). These limit objects can be considered as weighted graphs with a continuum underlying set, or (if you wish) as graphs on a nonstandard model of the unit interval.

Let us describe an example here; more to follow in Section 6.5.2. The picture on the left hand side of Figure 1 is the adjacency matrix of a graph G with 100 nodes, where the 1’s are represented by black squares and the 0’s, by white squares. The graph itself is constructed by a simple randomized growing rule: Starting with a single node, we either add a new node or a new edge; a new node is born with probability 1/n, where n is the current number of nodes. (A closely related graph sequence (randomly grown uniform attachment graphs) will be discussed in detail in Section 6.5.2.)

|![image 4](<2009-lovasz-very-large-graphs_images/imageFile4.png>)|
|---|


Figure 1: A randomly grown uniform attachment graph with 100 nodes

The picture on the right hand side is a grayscale image of the function U(x,y) = 1−max(x,y). The similarity with the picture on the left is apparent; and suggests that the limit of the graph sequence on the left is this function. This turns out to be the case in a well deﬁned sense. It follows that to approximately compute various parameters of the graph on the left hand side, we can compute related parameters of the function on the right hand side. For example, the triangle density of the graph on the left tends (as n → ∞) to the integral

U(x,y)U(y,z)U(z,x)dxdy dz.

[0,1]3

Two more remarks on the dense case. Of course, a graphon can be inﬁnitely complicated. But in many cases limits of growing graph sequences have a limit graphon that is a continuous function described by a simple formula (see a couple of examples in Section 6.5.2). Such a limit graphon provides a very useful approximation of a large dense graph.

Instead of the interval [0,1], we can consider any probability space (Ω,A,π) with a symmetric measurable function W : Ω × Ω → [0,1]. This would not give a greater generality, but it is sometimes useful to represent the limit object by other probability spaces. We’ll see an example of this in Section 6.5.2.

In the sparse case, the limit object can be described as a graphing (known from group theory or ergodic theory, Elek [37]), or as a measure preserving graph (see Section 3.2), or as a distribution on rooted countable graphs with special properties.

Instead of sampling, we can use dual (global) measurements, more precisely, homomorphisms into ﬁxed small graphs, to deﬁne convergence. The remarkable fact is that under the right conditions, this leads to an equivalent notion! (See Sections 6.6, 7.3.)

- 1.5.4 Optimization problems for graphs


We have presented the theory of convergent graph sequences and their limits as an answer to problems coming from very large networks, but a very strong motivation comes from extremal graph theory.

Consider the following two optimization problems. Classical optimization problem. Find the minimum of x3 − 6x where x is a nonnegative

real number.

Graph optimization problem. Find the minimum of t(C4,G) over all graphs G with t(K2,G) ≥ 1/2. (Here t(F,G), the homomorphism density of F in G, denotes the probability that a random map of V (F) into V (G) preserves the edges. C4 denotes the 4-cycle and K2 is the complete graph with 2 nodes.)

The solution of the classical optimization problem is of course x = √2. This means that it has no solution over the rationals, but we can ﬁnd rational numbers that are arbitrarily close to being optimal. If we want a single solution, we have to go to the completion of the rationals, i.e., to the reals.

![image 5](<2009-lovasz-very-large-graphs_images/imageFile5.png>)

The graph optimization problem may take a bit more eﬀort to solve, but it is not hard to show that if the edge-density is 1/2, then the 4-cycle density is larger than 1/16. Furthermore, this density gets arbitrarily close to 1/16 for appropriate families of graphs: the most important example is a random graph with edge-density 1/2 (cf. also Section 1.4.3 and Theorem 9.5).

This suggests that we could try to enlarge the set of (ﬁnite) graphs with new objects so that the appropriate extension of our optimization problem has a solution among the new objects. Furthermore, we want that these new objects should be approximable by graphs, just like real numbers are approximable by rationals.

Many of the basic tools in the theory of very large graphs have been ﬁrst applied in extremal graph theory: the Regularity Lemma [113], convergent graph sequences [43], quasirandom graphs [117, 33].

The example above shows that limit objects may provide cleaner formulations of extremal graph theory results, with no error terms. In some cases this goes further, and the limit objects provide a way to state, in an exact way, questions like ”How do extremal graphs look like?”. They have similar uses in the theory of computing. We discuss these applications in Sections 8 and 9.

- 1.6 Mathematical tools


It is clear from the above that this area is at the crossroads of diﬀerent ﬁelds of mathematics. Graph theory and computer science are the main sources, and probability and mathematical statistics are crucial tools. Group theory, in particular ﬁnitely generated groups, have provided many of the questions and ideas in the theory of limits of graphs with bounded degree. Ergodic theory may play a similar role in the dense case. Measure theory is needed, and an important new general proof method uses nonstandard analysis.

We will discuss one further tool, namely Frobenius algebras, which are used in the proofs of characterization theorems of homomorphism functions, but also in some other studies of graph parameters; see Section 2.6.

## 2 Graph parameters

A graph parameter is a real valued function deﬁned on isomorphism types of graphs (including the graph K0 with no nodes and edges). A simple graph parameter is deﬁned only on isomorphism types of simple graphs (i.e., on graphs with no loops or multiple edges). A graph parameter f is multiplicative if f(G) = f(G1)f(G2) whenever G is the disjoint union of G1 and G2. We say that a graph parameter is normalized if its value on K1, the graph with one node and no edge, is 1. Note that if a graph parameter is multiplicative and not identically 0, then its value on K0 (the graph with no nodes and no edges) is 1.

- 2.1 Connection matrices and reﬂection positivity

A k-labeled graph is a graph in which k of the nodes are labeled by 1,...,k (there may be any number of unlabeled nodes). A 0-labeled graph is just an unlabeled graph.

Let F1 and F2 be two k-labeled graphs. We deﬁne the k-labeled graph F1F2 by taking their disjoint union, and then identifying nodes with the same label. Clearly this multiplication is associative and commutative. For two 0-labeled graphs, F1F2 is their disjoint union.

Let f be any graph parameter and ﬁx an integer k ≥ 0. We deﬁne the k-th connection matrix of the graph parameter f as the (inﬁnite) symmetric matrix M(f,k), whose rows and columns are indexed by (isomorphism types of) k-labeled graphs, and the entry in the intersection of the row corresponding to F1 and the column corresponding to F2 is f(F1F2).

We call the graph parameter reﬂection positive if all the corresponding connection matrices are positive semideﬁnite.

- 2.2 Homomorphisms from the left


- 2.2.1 Versions of homomorphism numbers


For two ﬁnite graphs F and G, let hom(F,G) denote the number of homomorphisms of F into G (adjacency-preserving maps from V (F) to V (G)), inj(F,G), the number of injective homomorphisms of F into G, and ind(F,G), the number of embedding of F into G as an induced subgraph.

These quantities are closely related:

ind(F′,G),

inj(F,G) =

F′⊇F

where F′ ranges over all graphs obtained from F by adding edges, and

hom(F,G) =

inj(F′′,G),

F′′

where F′′ ranges over all graphs obtained from F by identifying nodes. Conversely, ind can be expressed by inj, which in turn can be expressed by hom using inclusion-exclusion.

This deﬁnition can be extended to the case when G has nodeweights αv and edgeweights βuv: hom(F,G) =

βϕ(u),ϕ(v)(G).

αϕ(u)(G)

uv∈E(F)

ϕ: V (F)→V (G) u∈V (F)

We often normalize these homomorphism numbers, and consider the homomorphism densities t(F,G) =

hom(F,G) |V (G)||V (F)|

,

![image 6](<2009-lovasz-very-large-graphs_images/imageFile6.png>)

which is the probability that a random map of V (F) into V (G) is a homomorphism. We can deﬁne similarly

inj(F,G) n(n − 1)···(n − k + 1)

tinj(F,G) =

(2) and

![image 7](<2009-lovasz-very-large-graphs_images/imageFile7.png>)

ind(F,G) n(n − 1)···(n − k + 1)

tind(F,G) =

. (3) We have

![image 8](<2009-lovasz-very-large-graphs_images/imageFile8.png>)

tind(F′,G) (4)

tinj(F,G) =

F′⊇F

and the inversion formula tind(F,G) =

′)\E(F)|tinj(F′,G). (5)

(−1)|E(F

F′⊇F

For hom and inj the relationship is not so simple due to the diﬀerent normalization, but recalling that we are interested in large graphs G, the following fact is usually enough to go between them:

1 |V (G)|

tinj(F,G) − t(F,G) = O(

). (6)

![image 9](<2009-lovasz-very-large-graphs_images/imageFile9.png>)

We note that tind(F,G) is the probability that sampling V (F) nodes of G, we see the graph

- F. So it follows that (for very large graphs, up to the error in (6)) subgraph sampling provides the same information as any of the homomorphism densities t,tinj,tind.


- 2.2.2 Spectra


Homomorphisms of “small” graphs into G are related to sampling, as mentioned earlier. There are less obvious applications of these numbers.

- Example 2.1 If Ck denote the cycle on k nodes, then hom(Ck,G) is the trace of the k-th power of the adjacency matrix of the graph G. In other words,


n

λki ,

hom(Ck,G) =

i=1

where λ1,...,λn are the eigenvalues of the adjacency matrix of G. From here, eigenvalues with large absolute value can be recovered. For example, hom(C2k,G)1/(2k) tends to the largest eigenvalue of G as k → ∞.

- 2.3 Homomorphisms to the right


- 2.3.1 Colorings and independent sets

Several important graph parameters can be expressed in terms of homomorphisms into ﬁxed “small” graphs.

- Example 2.2 If Kq denotes the complete graph with q nodes (no loops), then hom(G,Kq) is the number of colorings of the graph G with q colors, satisfying the usual condition that adjacent nodes must get diﬀerent colors.
- Example 2.3 Let H be obtained from K2 by adding a loop at one of the nodes. Then hom(G,H) is the number of independent sets of nodes in G.


- 2.3.2 Multicuts


An important graph parameter is the maximum cut Maxcut(G), the maximum number of edges between a set S ⊆ V (G) of nodes and its complement. While ﬁnding minimum cuts is perhaps more natural, the maximum cut problem comes up when we want to approximate general graphs by bipartite graphs, in computing ground states in statistical physics (see next section), and in many other applications. For our purposes, it will be more convenient to consider the normalized maximum cut, deﬁned by

eG(S,V \ S) |V |2

Maxcut(G)) |V |2

maxcut(G) =

= max

![image 10](<2009-lovasz-very-large-graphs_images/imageFile10.png>)

![image 11](<2009-lovasz-very-large-graphs_images/imageFile11.png>)

S⊆V

(here eG(X,Y ) denotes the number of edges in G connecting node sets X and Y ).

The following easy fact relates maximum cuts and homomorphism numbers. Let H be the weighted graph on {1,2} with nodeweights and edgeweights 1 except for the non-loop edge, which has weight 2. Then we have the trivial inequalities

2Maxcut(G) ≤ hom(G,H) ≤ 2|V(G)|2Maxcut(G),

which upon taking the logarithm and dividing by |V (G)|2 becomes

1 |V (G)|

log2 hom(G,H) |V (G)|2

≤ maxcut(G) +

maxcut(G) ≤

. (7)

![image 12](<2009-lovasz-very-large-graphs_images/imageFile12.png>)

![image 13](<2009-lovasz-very-large-graphs_images/imageFile13.png>)

So the homomorphism number into this simple 2-node graph determines maxcut(G) asymptotically.

An important extension of the maximum cut problem involves partitions into q ≥ 1 classes instead of 2. Instead of just counting edges between diﬀerent classes, we specify in advance numbers βij (i,j ∈ [q]) such that βij = βji. We deﬁne the maximum multicut density (with the target weights βij) as

1 |V (G)|2 i,j

βijeG(Si,Sj),

mmcut(G,β) = max

![image 14](<2009-lovasz-very-large-graphs_images/imageFile14.png>)

where the maximum is taken over all partitions {S1,...,Sq} of V (G).

A further important extension is to ﬁx the proportion into which the cut separates the node set. For example, the “maximum bisection problem” asks for the maximum size of a cut that separates the nodes into two equal parts (we allow a diﬀerence of 1 if the number of nodes is even). More precisely, we can formulate the restricted multicut problem as follows. We specify (in addition to the βij) numbers α1,...,αq > 0 with α1 + ··· + αq = 1. It is convenient to consider the parameters αi and βij as the nodeweights and edge weights of a weighted graph H with V (H) = [q]. Then are interested in

1 |V (G)|2 i,j

E(G,H) = max

βijeG(Si,Sj), (8)

![image 15](<2009-lovasz-very-large-graphs_images/imageFile15.png>)

where {S1,...,Sq} ranges over all partitions of V (G) such that

|Si| − αi|V (G)| < 1 (i = 1,...,q). (9)

(This can be deﬁned for all graphs H with positive nodeweights, by scaling the nodeweights so that they sum to 1.)

The following extension of (7) is easy to prove: for H ﬁxed and |V (G)| → ∞,

log2 hom(G,H) |V (G)|2

1 |V (G)|

= mmcut(G,β) + O(

). (10)

![image 16](<2009-lovasz-very-large-graphs_images/imageFile16.png>)

![image 17](<2009-lovasz-very-large-graphs_images/imageFile17.png>)

(Note that log2 hom(G,H)/|V (G)|2 is asymptotically independent of the node weights of H.)

The restricted maximum multicut problem is also related to counting homomorphisms, but the relationship is a little more complicated. Let G be a (very large) simple graph and H, a weighted graph with V(H)=[q]. In the deﬁnition of t(G,H) we considered random maps

- V (G) → V (H), where the image of each node is chosen independently from the distribution on
- V (H) deﬁned by the node weights. For most of these random maps ϕ, |ϕ−1(i)| ≈ αi(H)|V (G)|| by the law of large numbers. It turns out that often it is advantageous to restrict ourselves to maps that are ”typical” in this sense. More precisely, let S(G,H) denote the set of those maps


ϕ : V (G) → V (H) for which |ϕ−1(i)| − αi|V (G)| < 1 for all i ∈ V (H). Using this notation, we can write

βϕ(u),ϕ(v).

rmcut(G,H) = max

ϕ∈S(G,H)

u,v∈V (G)

Let H be the weighted graph in which the edge weights are βij = exp(βij) instead of βij. If we deﬁne

hom∗(G, H) =

βϕ(u),ϕ(v),

ϕ∈S(G,H) uv∈E(G)

then the following inequality analogous to (10) holds for |V (G)| → ∞:

log hom∗(G, H) |V (G)|2

1 |V (G)|

+ O(

). (11)

rmcut(G,H) =

![image 18](<2009-lovasz-very-large-graphs_images/imageFile18.png>)

![image 19](<2009-lovasz-very-large-graphs_images/imageFile19.png>)

- 2.3.3 Statistical physics


Graph homomorphism functions can be used to express partition functions of various statistical physical models. Two basic types of such models are “hard-core” and “soft-core”.

To describe an example of a hard-core model, let G be an n×n grid, and suppose that every node of G (every “site”) can be in one of two states, “UP” or “DOWN”. The properties of the system are such that no two adjacent sites can be “UP”. A “conﬁguration” is a valid assignment of states to each node. The number of conﬁgurations is the number of independent sets of nodes in G, which in turn can be expressed as the number of homomorphisms of G into the graph H consisting of two nodes, ”UP” and ”DOWN”, connected by an edge, and with an additional loop at ”DOWN”.

In a soft-core spin model the sites are again nodes of a graph G, which can be in one of q possible states. For any two states i and j, we specify an “energy of interaction” in the form of a real number Jij. A given conﬁguration (assignment of states) is given by a map ϕ : V (G) → [q], and its “energy density” is expressed as

2 |V (G)|2

Eϕ =

Jϕ(u),ϕ(v), (12)

![image 20](<2009-lovasz-very-large-graphs_images/imageFile20.png>)

uv∈E(G)

From this, one deﬁnes the partition function as Z(G,J) =

exp(−Eϕ). (13)

ϕ:V (G)→[q]

Another important quantity is the ground state energy E(G,J) = min

Eϕ. (14)

ϕ:V (G)→[q]

Note that both of these quantities are familiar: if we take β = −J, then E(G,J) = −rmcut(G,β), and if we take βij = exp(Jij), then Z(G,J) = hom(G,exp(β)). Even restricted multiway cuts correspond to a quantity studied in statistical physics: it is called microcanonical ground state energy there.

The above deﬁnitions don’t work well for dense graphs G: as remarked after (10), the num-

bers log2 hom(G,H)/|V (G)|2 are essentially independent of the node weights of H, so we loose information here. In the mean-ﬁeld theory, we deﬁne the mean ﬁeld partition function of a simple graph G by

e−|V(G)|E

Z(G,J) =

ϕ:V (G)→[q]

The free energy is deﬁned by

. (15)

ϕ

lnZ(G,H) |V (G)|

F(G,H) = −

. (16)

![image 21](<2009-lovasz-very-large-graphs_images/imageFile21.png>)

Note that the normalization is diﬀerent from (13) in the exponent and therefore we only divide by |V (G)| (as opposed to (10)).

For more about this connection, we refer to [30].

- 2.4 Homomorphisms densities in the sparse case The best analogue for sparse graphs of the homomorphism density t(F,G) is

s(F,G) =

hom(F,G) |V (G)|

![image 22](<2009-lovasz-very-large-graphs_images/imageFile22.png>)

, (17)

which we consider for connected graphs F. We can interpret this number as follows. For u ∈ V (F) and v ∈ V (G), let homv→u(F,G) denote the number of homomorphisms ϕ of F into G with ϕ(u) = v. Now we ﬁx any node u of F and select a uniform random node v of G. Then s(F,G) is the expectation of homv→u(F,G). We can interpret

sinj(F,G) =

inj(F,G) |V (G)|

![image 23](<2009-lovasz-very-large-graphs_images/imageFile23.png>)

, sind(F,G) =

ind(F,G) |V (G)| similarly.

![image 24](<2009-lovasz-very-large-graphs_images/imageFile24.png>)

Remark 2.4 For bounded degree graphs the order of magnitude of hom(F,G) (where F is ﬁxed and V (G) tends to inﬁnity) is |V (G)|c(F), where c(F) is the number of connected components of F. But since hom(F,G) is multiplicative over the connected components of F, we don’t loose any information if we restrict the deﬁnition s(F,G) to connected graphs F.

The sparse homomorphism densities (17) contain the same information as the distribution of neighborhood samples. The proof of this is a bit trickier here than in the dense case.

From the interpretation of s(F,G) given above, we see that it can be obtained as the expectation of the number of homu→vs(F,B), where B is a random ball from the neighborhood sample distribution ρG,r, with center v and radius r = |V (F).

To compute the neighborhood sample distributions from the quantities s(F,G), we ﬁrst express the quantities sinj(F,G) via inclusion-exclusion. By a similar argument, we can express the quantities sind(F,G).

Next, we consider graphs F together with maps δ : V (F) → {0,...,d}, and we determine the numbers

sind(F,δ,G) =

ind(F,δ,G) |V (G)|

![image 25](<2009-lovasz-very-large-graphs_images/imageFile25.png>)

,

where ind(F,δ,G) is the number injections ϕ : V (F) → V (G) which embed F in G as an induced subgraph, so that the degree of ϕ(v) is δ(v). This is again done by an inclusion-exclusion argument.

Given a ball B of radius r, the fraction of nodes v ∈ V (G) for which B(v,r) = B is

δ ind(B,δ,G), where the summation extends over all functions δ which assigns to each node of B at distance < r from the root its degree in B. This proves that homomorphism densities and neighborhood sampling are equivalent.

- 2.5 Characterizing homomorphism numbers


Multigraph parameters of the form hom(·,H), where H is a weighted graph, were characterized by Freedman, Lov´asz and Schrijver [51].

- Theorem 2.5 Let f be a graph parameter deﬁned on multigraphs without loops. Then f is equal to hom(.,H) for some weighted graph H on q nodes if and only if it is reﬂection positive and rk(M(f,k)) ≤ qk for all k.


Several improvements and versions of this result have been obtained. It is shown in [89] that it is enough to assume the rank condition for k ≤ 2. Analogous characterizations can be given for graph parameters of the form hom(·,H) where the nodeweights in H are all 1 [106], and where H is an unweighted graph without multiple edges (but with loops allowed) [81]. There is also an analogous (dual) characterization of graph parameters of the form hom(F,.), deﬁned on simple graph with loops, where F is also a simple graph with loops [81]. These results can be extended to directed graphs, hypergraphs, semigroups, and indeed, to all categories satisfying reasonable conditions [82].

The two conditions on connection matrices in the theorem have interesting uses of their own.

- 2.5.1 Reﬂection positivity and extremal graph theory

Theorem 6.13 will give a number of equivalent (cryptographic) descriptions of limit objects of growing graph sequences, and it can be used to characterize all reﬂection positive graph parameters, see Corollary 6.14.

Reﬂection positivity implies a number of very useful relations between the densities of various subgraphs in a given graph, which in turn can be used to prove results in extremal graph theory. We will illustrate this in Section 9.

We’ll return to applications of reﬂection positivity of connection matrices in the context of continuous generalizations of graphs (Section 9) and in extremal graph theory (Section 9).

- 2.5.2 Finite connection rank


The ﬁniteness of the rank of connection matrices is also interesting. One reason to be interested in this question is the fact that such a graph parameter can be evaluated in polynomial time for graphs with bounded treewidth [78].

There are several examples of graph parameters with ﬁnite connection rank [77]: the number of perfect matchings, the number of all matchings, the number of Hamiltonian cycles, any evaluation of the Tutte polynomial.

A challenging problem is to determine all graph parameters for which all the connection matrices have ﬁnite rank. Homomorphism functions hom(.,H) are examples for every weighted graph H (here the nodeweights and edgeweights can be negative). Dual homomorphism densities hom(F,.) also have ﬁnite connection rank. Every evaluation of the Tutte polynomial is a further example.

Very recently Godlin and Makowski proved that all graph parameters which are evaluations of graph polynomials deﬁnable in Monadic Second Order Logic have ﬁnite connection rank. This result can be used mostly as a tool to prove that certain properties are not deﬁnable this way.

Further variants of this problem ask for the characterization of graph parameters with exponentially bounded connection rank, or polynomially bounded connection rank.

- 2.6 Graph algebras


A quantum graph is deﬁned as a formal linear combination of a ﬁnite number of graphs with real coeﬃcients. For every quantum graph x, let N(x) be the maximum number of nodes in the graphs occurring in x with nonzero coeﬃcient. The deﬁnition of hom(F,G) and t(F,G) extends to quantum graphs linearly: if f = ni=1 λiFi and g = mj=1 µjGj, then we deﬁne

n

hom(f,g) =

i=1

m

λiµjhom(Fi,Gj).

j=1

Quantum graphs are useful in expressing various combinatorial situations. For example, for any graph F we deﬁne

F =

F′:V (F ′)=V (F) E(F ′)⊇E(F )

′)|F′. (18)

(−1)|E(F

Then t( F,G) is just the probability that a random map V (F) → V (G) preserves adjacency as well as non-adjacency.

Let f be any graph parameter and ﬁx an integer k ≥ 0. Let Qk denote the (inﬁnite dimensional) vector space of all k-labeled quantum graphs. We can turn Qk into an algebra by using F1F2 introduced above as the product of two generators, and then extending this multiplication to the other elements linearly. Clearly Qk is associative and commutative. The graph Ok on k nodes with no edges is the multiplicative unit in Qk. If all nodes of F are labeled, then both F and the quantum graph F introduced above (keeping the node labels) are idempotent: F2 = F and F2 = F.

Every graph parameter f can be extended linearly to quantum graphs, and deﬁnes an inner product on Qk by

x,y := f(xy). (19)

This means that our graph algebra is a Frobenius algebra (see [70]). This inner product has nice properties, for example

x,yz = xy,z . (20)

Let Nk(f) denote the kernel of this inner product, i.e.,

Nk(f) := {x ∈ Qk : f(xy) = 0 ∀y ∈ Qk}. Then we can deﬁne the factor algebra

Qk/f := Qk/Nk(f).

Example 2.6 As an example, consider the number pm(G) of perfect matchings in the graph G. It is a basic property of this value that subdividing an edge by two nodes does not change it. This can be expressed as P4 − P2 ∈ N2(pm), where Pk denotes the paths with k nodes, of which the two endnodes are labeled.

We can introduce a third “product”: the tensor product G ⊗ H of a k-labeled graph G and an l-labeled graph H is deﬁned as the (k + l)-labeled graph obtained as the disjoint union of G and H, where the labels in H are increased by k. If k = l = 0, then the tensor product is the same as the product in the algebra Qk.

The parameter f is reﬂection positive if and only if the inner product (19) is positive semideﬁnite on Qk; equivalently, positive deﬁnite on Qk/f, so it turns Qk/f into a Hilbert space. In fact, the factor algebra Qk/f is a ﬁnite dimensional commutative ∗-algebra, which has both a commutative and associative product and a positive deﬁnite inner product, related by x,yz = xy,z .

The dimension of Qk/f is the rank of the connection matrix. If this rank is a ﬁnite number

- m and the parameter is reﬂection positive, it follows that Qk/f is isomorphic Rm endowed with the coordinate-wise product and the usual inner product.


There are many algebraically interesting connections between these algebras, for example, there is an embedding given by the tensor product

Qk/f ⊗ Ql/f ֒→ Qk+l/f, (21)

which shows that dim(Qk/f) is a superadditive function of k.

This nice algebraic structure can be exploited in various ways [51, 78, 84, 86]. Let us sketch the proof of Theorem 2.5 in an (easier) special case: when there is no degeneracy in the sense that the embedding in (21) is an isomorphism (this is in fact the generic case, which occurs whenever f = hom(.,H), where H has no “twin” nodes nor any nontrivial automorphism). So we have dim(Qk/f) = qk for all k.

Let p1,...,pq be the basis of Q1/f consisting of idempotents (corresponding to the standard basis vectors in Rq). Deﬁne pϕ = pϕ(1) ⊗ ··· ⊗ pϕ(k) for all ϕ : [k] → [q], then the k-labeled quantum graphs pϕ form a basis of Qk/f consisting of idempotents.

We can deﬁne a weighted complete graph H on [q] as follows: let αi = f(pi) and deﬁne βij by expressing the graph k2 (a single edge with both nodes labeled) in the idempotent basis:

βij(pi ⊗ pj)

k2 =

i,j∈[q]

This deﬁnes nodeweights αi and edgeweights βij for H. The nodeweights are positive, since

αi = f(pi) = f(p2i) > 0. The deﬁnition of the βij implies that k2(pi ⊗ pj) = βij(pi ⊗ pj). (22)

We claim that the weighted graph H obtained this way satisﬁes f(G) = hom(G,H) for every multigraph G. Indeed, we may assume that V (G) = [k] and all nodes of G are labeled. Then we can write

Kuv,

G =

uv∈E(G)

where Kuv consists of k labeled nodes and a single edge connecting u and v. Equation (22) implies that

pϕKuv = βϕ(u)ϕ(v)pϕ. Using (20) repeatedly, we get G =

pϕ

pϕ G =

ϕ: [k]→[q]

ϕ: [k]→[q]

and so f(G) =

βϕ(u)ϕ(v)

ϕ: [k]→[q] uv∈E(G)

βϕ(u)ϕ(v)pϕ,

Kuv =

ϕ: [k]→[q] uv∈E(G)

uv∈E(G)

αϕ(u) = hom(G,H).

u∈V (G)

## 3 Graph-like structures on probability spaces

The aim of this section is to introduce certain analytic objects, which will serve as limit objects for graph sequences, separately in the dense and sparse case. It is an interesting feature of these structures that they have come up in diﬀerent studies.

In the dense case, several versions of these objects turn out to be equivalent; graphons are very simple objects (2-variable measurable functions), but they turn out to be equivalent, among others, to exchangeable random variables.

In the bounded degree case, several related, but non-equivalent notions have been proposed, at least one of which (graphings) is also known from group theory.

- 3.1 Graphons


Let W denote the space of all bounded symmetric measurable functions W : [0,1]2 → R (i.e., W(x,y) = W(y,x) for all x,y ∈ [0,1]). Let W0 denote the set of all functions W ∈ W such that 0 ≤ W ≤ 1.

A function W ∈ W is called a stepfunction, if there is a partition S1 ∪ ··· ∪ Sk of [0,1] into measurable sets such that W is constant on every product set Si × Sj. The number k is the number of steps of W.

For every weighted graph G, we deﬁne a stepfunction WG ∈ W0 as follows. Let V (G) = [n]. Split [0,1] into n intervals J1,...,Jn of length λ(Ji) = αi/αG. For x ∈ Ji and y ∈ Jj, let

WG(x,y) = βij(G).

Let W ∈ W and let ϕ : [0,1] → [0,1] be a measure preserving map. We can deﬁne another function Wϕ by

Wϕ(x,y) = W(ϕ(x),ϕ(y)). From the point of view of using these functions as continuous analogues of graphs, the functions

- W and Wϕ are not essentially diﬀerent (they are related like two isomorphic graphs in which the nodes are labeled diﬀerently). One has to be a little careful though, because measure preserving


maps are not necessarily invertible, and so the relationship between W and Wϕ is not symmetric. We call two graphons W and W′ weakly isomorphic, if there is a third graphon U and measure preserving maps ϕ,ϕ′ : [0,1] → [0,1] such that W = Uϕ and W′ = Uϕ

′

almost everywhere. It is not hard to show that weak isomorphism is an equivalence relation.

Equivalence classes of functions in W0 under weak isomorphism are called graphons. (Sometimes we call a function W ∈ W0 a graphon; by analogy with graphs, these functions could be called “labeled graphons”.)

- 3.1.1 Homomorphisms into graphons and from graphons


Counting homomorphism into graphs extends to counting homomorphism into graphons in the following sense: For every W ∈ W and simple graph F = (V,E), deﬁne

t(F,W) =

W(xi,xj)

dxi

[0,1]V ij∈E

i∈V

Then it is easy to verify that for every graph G,

t(F,G) = t(F,WG). (23)

Of the two modiﬁed versions of homomorphism densities (2) and (3), the former has not signiﬁcance in this context since a random assignment i  → xi (i ∈ V (F),xi ∈ [0,1] is injective with probability 1. But the induced subgraph density is worth deﬁning, and in fact it can be expressed as

tind(F,W) =

We have then

W(xi,xj)

[0,1]V ij∈E

ij∈(

(1 − W(xi,xj))

V 2

)\E

dxi. (24)

i∈V

tind(F,G) = tind(F,WG), (25) and the inclusion-exclusion formula (5) follows by expanding the parentheses in the integrand

(24).

Borgs, Chayes and Lov´asz [26] proved that the homomorphism densities determine the graphon:

- Theorem 3.1 Two graphons are weakly isomorphic if and only if t(F,W) = t(F,W′) for every simple graph F.


A natural idea of the proof of this theorem would be to bring every graphon to a “canonical form”, so that weakly isomorphic graphons would have identical canonical forms. In the case of functions in a single variable, a canonical form that works in many situations can be obtained through “monotonization”: for every bounded real function on [0,1] there is an unique monotone increasing left-continuous function on [0,1] that has, among others, the same moments. For graphons this does not seem to be doable, but the proof of Theorem 3.1 goes by constructing, for every graphon W, a “canonical ensemble”: a probability distribution on graphons on the

same canonical σ-algebra and weakly isomorphic to W, such that two graphons are isomorphic if and only if their ensembles can be coupled so that corresponding graphons are identical.

Alternate proofs of Theorem 3.1 have been given by Diaconis and Janson [35] using the theory of exchangeable random variables, and by Bollob´s and Riordan [24] combining Theorem 6.2 below with measure-theoretic arguments.

There is probably no good way to deﬁne homomorphism numbers from graphons into graphs or into other graphons. The parameters related to such homomorphisms that extend naturally to graphons are deﬁned by maximization, like the normalized maximum cut, and more generally, restricted maximum multiway cuts. Let H be a weighted graph with V (H) = [q] and W, a graphon. Then we can deﬁne

E(W,H) = sup

βij

Si

i,j∈V (H)

W(x,y)dxdy,

Si×Sj

where {S1,...,Sq} ranges over all partitions of [0,1] into measurable sets with λ(Si) = αi(H). This quantity does not exactly extend E(G,H) as deﬁned in (8), but the error is small: it was proved in [30] that for a ﬁxed weighted graph H,

E(G,H) − E(WG,H) = O

- 3.1.2 W-random graphs


1 |V (G)|

![image 26](<2009-lovasz-very-large-graphs_images/imageFile26.png>)

(|V (G)| → ∞). (26)

A graphon W gives rise to a way of generating random graphs that are more general than the Erdo˝s–R´enyi graphs. This construction was introduced by Lov´asz and Szegedy [85] and Bollob´as, Janson and Riordan [22].

Given a graphon W and an integer n > 0, we can generate a random graph G(n,W) on node set [n] as follows: We generate n independent numbers X1,...,Xn from the uniform distribution on [0,1], and then connect nodes i and j with probability W(Xi,Xj), making an independent decision for distinct pairs (i,j).

As a special case, if W is the identically p function, we get “ordinary” random graphs G(n,p). We can extend this construction to generating a countable random graph G(W) on N: We

generate an inﬁnite sequence X1,X2,... of uniformly distributed random points from [0,1], and (as before) connect nodes i and j with probability W(Xi,Xj).

Graphons will come up in several ways in our discussions. In Theorem 6.13 we will collect the many disguises in which they occur.

- 3.2 Graphings


- 3.2.1 Measure preserving graphs


Let G be a graph with node set [0,1], with all degrees bounded by d. We call G measurable, if for every (Lebesgue) measurable set B the neighborhood N(B) in G is also measurable.

For every set A ⊆ [0,1] and x ∈ [0,1], let dA(x) denote the number of neighbors of x in B. One can prove using the measurability of G that dA(x) is a measurable function of x. We say

that G is measure preserving, if it is measurable and for any two measurable sets A,B,

dB(x)dx =

A

dA(x)dx. (27)

B

Assuming that this relation holds, we can deﬁne a measure µ on the Borel sets of [0,1]2

by µ(A × B) = A dB(x)dx. This measure is concentrated on the set of edges (which can be considered as a subset of [0,1]2). Furthermore, the marginals of µ are absolutely continuous with

respect to the Lebesgue measure, and their Radon-Nikodym derivative is the degree function.

In every measure preserving graph G, we can deﬁne the density s(F,G) of a graph F. Indeed, let us recall that s(F,G) is the expectation of homv→u(F,G), where v is a ﬁxed node of F and u is a random node of G. Since we have a probability distribution on V (G), and homv→u(F,G) is a bounded measurable function of u, this deﬁnition carries over verbatim.

Similarly, we can talk about the neighborhood distributions ρG,m in a measure preserving graph.

- 3.2.2 Graphings


Let A1,...,Ad,B1,...,Bd be measurable subsets of [0,1], and let ϕi : Ai → Bi be bijective measure preserving maps. The tuple H = ([0,1],ϕ1,...,ϕd) is called a graphing (see [53, 69]). From every graphing H we get a directed graph −→G on [0,1] by connecting x and y in [0,1] if there is an i such that y = ϕi(x). The edges of this digraph are colored with d colors in such a way that each color-class deﬁnes a measure preserving bijection between two subsets of [0,1].

Forgetting the orientation and the edge-colors of this digraph, we get a measure preserving graph with degrees bounded by 2d. A measure preserving graph with its edges colored and oriented so that each color deﬁnes a measure preserving bijection is equivalent to a graphing.

It would be perhaps more natural to assume that the maps ϕ1,...,ϕd are involutions, in which case we get an undirected graph, and we can extend the ϕi to measure preserving involutions [0,1] → [0,1]. It is true that for every graphing there is such an involutive graphing deﬁning the same measure preserving graph; but the number of maps may become much larger.

Every measure preserving graph arises from a graphing:

- Theorem 3.2 Let G be a measure preserving graph with degrees bounded by d. Then there is a graphing H = ([0,1],ϕ1,...,ϕr), where r ≤ d2, such that the underlying graph is G.


One way of looking at a representation of a measure preserving graph as a graphing is that it provides a certiﬁcate that the graph is measure preserving. The graphing representing a given measure preserving graph may not be unique.

Theorem 3.2 can be viewed as a measure preserving graph version of Shannon’s Theorem, which asserts that the edges of a multigraph with maximum degree d can be colored by 3d/2 colors. (For simple graphs, Vizing’s Theorem gives the better bound of d + 1.) The bound d2 is probably not optimal in the measure preserving version either.

We will talk about s(F,H) if F is a (ﬁnite) graph and H is a graphing. This will mean simply

- s(F,G), where G is the underlying measure preserving graph.


We note that both in measure preserving graphs and graphings, we could replace the probability space [0,1] by any other standard probability space, but this would not lead to any gain in generality. However, in some cases the presentation of the measure preserving graph or graphing is more natural on other probability spaces.

- 3.2.3 Random countable rooted graphs

Measure preserving graphs are also related to certain probability distributions on rooted countable graphs, introduced by Benjamini and Schramm [16].

Let G be a measure preserving graph and choose a uniform random point x ∈ [0,1]. The connected component Gx of G containing x is a countable graph with degrees bounded by d, and with a “root” node x.

Let Gd denote the set of connected countable graphs with all degrees bounded by d, rooted at a node. Let Ad denote the σ-algebra on Gd generated by subsets obtained by ﬁxing a ﬁnite neighborhood of the root. The map x  → Gx is measurable as a map [0,1] → (Gd,Ad), and thus every measure preserving graph G deﬁnes a probability distribution π on (Gd,Ad).

Condition 27 implies the following property of the measure π. Selecting a rooted graph G from π and then selecting a uniform random edge from the root, we get a probability distribution π∗ on the set G′d of rooted graphs in Gd with an edge (the “root edge”) from the root also speciﬁed. We say that π is unimodular, if the map G′d → G′d obtained by shifting the root node to the other endnode of the root edge is measure preserving with respect to π.

The measure on Gd obtained from a measure preserving graph is unimodular. Vice versa, every such measure is obtained from a graphing (and hence from a measure preserving graph; Elek [37]).

- 4 The cut-distance of two graphs


The deﬁnition of the distance of two arbitrary graphs is quite involved, and we will approach the problem in steps: starting with two graphs on the same node set, then moving to graphs with the same number of nodes (but unrelated), then moving to the general case.

In this section we consider dense graphs. The deﬁnitions are of course valid for all graphs, but they give a distance of o(1) between two graphs with edge-density o(1).

- 4.1 Two graphs on the same set of nodes


Let G and G′ be two graphs with a common node set [n]. The distance notion discussed here was initiated by Frieze and Kannan [52], and elaborated, e.g., in [29]. For an unweighted graph G = (V,E) and sets S,T ⊆ V , let eG(S,T) denote the number of edges in G with one endnode in S and the other in T (the endnodes may also belong to S ∩T; so eG(S,S) is twice the number of edges spanned by S). For two graphs G and G′ on the same node set [n], we deﬁne their cut distance by

d (G,G′) =

1 n2

|eG(S,T) − eG′(S,T)|.

max

![image 27](<2009-lovasz-very-large-graphs_images/imageFile27.png>)

S,T⊆V (G)

Note that we are dividing by n2 and not by |S| × |T|, which would look more natural. However, dividing by |S|×|T| would emphasize small sets too much, and the maximum would be attained when |S| = |T| − 1. With our deﬁnition, the contribution of a pair S,T is at most |T| · |S|/n2 (for simple graphs).

It is easy to see that d (G,G′) ≤ d1(G,G′), and in general the two sides are quite diﬀerent. For example, if G and G′ are two independent random graphs on [n] with edge probability 1/2, then with large probability d (G,G′) = O(1/√n).

![image 28](<2009-lovasz-very-large-graphs_images/imageFile28.png>)

- 4.2 Two graphs with the same number of nodes If G and G′ are unlabeled unweighted graphs on diﬀerent node sets but of the same cardinality


- n, then we deﬁne their distance by


δˆ (G,G′) = min G,˜ G˜′

d (G,˜ G˜′), (28)

where G˜ and G˜′ range over all labelings of G and G′ by 1,...,n, respectively. (The hat above the δ indicates that the “ultimate” deﬁnition will be somewhat diﬀerent.)

- 4.3 Two arbitrary graphs


Let G = (V,E) and G′ = (V ′,E′) be two graphs with (say) V = [n] and V ′ = [n′]. To deﬁne their distance, we need a graph operation: for every graph G and positive integer m, let G(m) denote the graph obtained from G by replacing each node of G by m nodes, where two new nodes are connected if and only if their predecessors were.

We can use the distance δˆ to deﬁne the distance δ (G,G′) = lim

δˆ (G[kn′],G′[kn]). (Here G(kn′) and G′(kn) have the same number of nodes.)

k→∞

A more complicated but “ﬁnite” deﬁnition of the same quantity can be given as follows. A fractional overlay of G and G′ is a nonnegative n × n′ matrix X such that n

′

u=1 Xiu = n1 and

![image 29](<2009-lovasz-very-large-graphs_images/imageFile29.png>)

n i=1 Xiu = n1′ . If n = n′ and σ : V → V ′ is a bijection, then Xiu = n11σ(i)=u is a fractional

![image 30](<2009-lovasz-very-large-graphs_images/imageFile30.png>)

![image 31](<2009-lovasz-very-large-graphs_images/imageFile31.png>)

overlay (which in this case is an honest-to-good overlay). We denote by X(G,G′) the set of all fractional overlays.

For a matrix M, let Σ(M) denote the sum of its entries. Then the distance of the two graphs can be described by the following optimization problem:

δ (G,G′) = min

max

Y,Z⊆V ×V ′

X∈X(G,G′)

XiuXjv −

XiuXjv . (29)

iu∈Y, jv∈Z uv∈E′

iu∈Y, jv∈Z ij∈E

To illuminate this deﬁnition a little, we can think of a fractional overlay as a coupling of the uniform distribution on V (G) with the uniform distribution on V (G′): it gives a probability distribution χ on V (G) × V (G′) whose marginals are uniform. Select two pairs (i,u) and (j,v) from the distribution χ. Then the ﬁrst sum in (29) is the probability that “iu ∈ Y and jv ∈ Z and ij ∈ E”, and the second sum is the probability that “iu ∈ Y and jv ∈ Z and uv is an edge”. Thus (29) expresses some form of correlation between ij being an edge and uv being an edge.

One word of warning: δ is only a pseudometric, not a true metric, because δ (G,G′) may be zero for diﬀerent graphs G and G′. This is the case e.g. if G′ = G(k) for some k.

Deﬁnition (29) can be extended to weighted graphs, but instead of going through the hairy formulas, we postpone this to the next section.

We conclude with a problem for which only partial results are available. If G and G′ have the same number of nodes, then the deﬁnition of δ does not give back δˆ . It was proved in [29] that

δ (G,G′) ≤ δˆ (G,G′) ≤ 32δ (G,G)1/67. (30)

This is a rather weak result, its signiﬁcance being that δ and δˆ deﬁne the same Cauchy sequences. Alon (unpublished) proved that

δˆ (G,G′) ≤ (1 + o(1))δ (G,G) (31) if |V (G)| = |V (G′)| → ∞. We conjecture:

Conjecture 4.1 For any two graphs G and G′ on n nodes, δˆ (G,G′) ≤ 2δ (G,G′). An analogous result for the edit distance was proved by Pikhurko [96].

- 4.4 Distance of graphons


This notion of distance extends to graphons as follows (and it is perhaps more natural in that context). We consider on W the cut norm

W = sup

W(x,y)dxdy

S,T⊆[0,1] S×T

where the supremum is taken over all measurable subsets S and T. It is sometimes convenient the use the corresponding metric d1(U,W) = U − W} . We deﬁne the cut distance

d (U,Wϕ),

δ (U,W) = inf

ϕ

where ϕ ranges over all invertible measure preserving maps from [0,1] → [0,1], and Wϕ(x,y) = W(ϕ(x),ϕ(y)).

The distance δ of graphons is only a pseudometric, since diﬀerent graphons can have distance zero. This happens precisely when they are weakly isomorphic.

If G and G′ are weighted graphs, then we have

δ (G,G′) = δ (WG,WG′). (32)

This could serve as a more natural (but not combinatorial) deﬁnition of the distance of two graphs, and we will use it to deﬁne the distance of two weighted graphs. Let K denote the graph with a single node of weight 1, endowed with a loop with weight 1/2. Then for a random graph G = G(n,1/2), we have δ (G,K) = O(1/√n) with large probability.

![image 32](<2009-lovasz-very-large-graphs_images/imageFile32.png>)

Going into all the complications with using the cut norm and then minimizing over measure preserving transformations is justiﬁed by the following important fact.

- Theorem 4.2 The pseudometric space (W0,δ ) is compact.

The proof depends on Szemer´edi partitions, to be discussed in section 5. Convergence in the . norm is stronger than weak-∗-convergence. To be more precise, if

Wn − W → 0 (n → ∞), then it follows immediately from the deﬁnition that

S×T

Wn →

S×T

W, (33)

and hence by standard arguments we get that

[0,1]2

U · Wn →

[0,1]2

U · W (34)

for every integrable function U. However, weak-∗-convergence is not equivalent of convergence in the . norm; a counterexample can be obtained e.g. from Example 6.19 (see [31]).

Similar construction can be applied to other norms, e.g., from the L1-norm

W 1 =

[0,1]2

|W(x,y)|dx

we get

d1(U,W) = U − Wϕ 1 and δ1(U,W) = inf

ϕ

δ1(U,W).

5 Szemer´edi partitions

One of the most important tools in understanding large dense graphs is the Regularity Lemma of Szemer´edi [112, 113] and its extensions. This lemma has many interesting connections to other areas of mathematics, including analysis [87, 23] and information theory [114]. It also has weaker (but more eﬀective) and stronger versions. Here we survey as much as we need from this rich theory.

- 5.1 ε-regular bipartite graphs and the original lemma


For a graph G = (V,E) and for X,Y ⊆ V , let eG(X,Y ) denote the number of edges with one endnode in X and another in Y ; edges with both endnodes in X ∩ Y are counted twice. We denote by dG(X,Y ) = e

G(X,Y ) |X|·|Y| the density of edges between X and Y . If X and Y are disjoint,

![image 33](<2009-lovasz-very-large-graphs_images/imageFile33.png>)

we denote by G[X,Y ] the bipartite graph on X ∪ Y obtained by keeping just those edges of G that connect X and Y .

Let P = {V1,...,Vk} be a partition of V . We say that P is an equipartition if ⌊|V |/k⌋ ≤ |Vi| ≤ ⌈|Vi|/k⌉ for all 1 ≤ i ≤ k. We deﬁne the weighted graph GP on V by taking the complete graph and weighting its edge uv by dG(Vi,Vj) if u ∈ Vi and v ∈ Vj.

The Regularity Lemma says, roughly speaking, that every graph has a partition P into a “small” number of classes such that GP is “close” to G. There are (non-equivalent) forms of this lemma, depending on how we measure the error.

Let G be a bipartite graph G with bipartition {U,W}. On the average, we expect that for

- X ⊆ U and Y ⊆ W,


eG(X,Y ) ≈ dG(X,Y )|X| · |Y |.

For two arbitrary subsets of the nodes, eG(X,Y ) may be very far from this “expected value”, but if G is a random graph, then, however, it will be close; random graphs are very “homogeneous” in this respect. We say that G is ε-regular, if

eG(X,Y ) |X| · |Y |

− d ≤ ε (35)

![image 34](<2009-lovasz-very-large-graphs_images/imageFile34.png>)

holds for all subsets X ⊆ U and Y ⊆ W such that |X| > ε|U| and |Y | > ε|W|.

Notice that we could not require condition (35) to hold for small X and Y : for example, if both have one element, then the quotient eG(X,Y )/(|X| · |Y |) is either 0 or 1. However, we could replace it by the condition

eG(X,Y ) − d|X| · |Y | ≤ ε|U| · |W| (36)

for all Y ⊆ U and Y ⊆ W. Indeed, (35) implies (36) for |X| > ε|U| and |Y | > ε|W|, while if e.g. |X| ≤ ε|U|, then eG(X,Y ) ≤ ε|U| · |W| and d|X| · |Y || ≤ ε|U| · |W|, so (36) holds trivially. Conversely, if (36) holds with ε replaced by ε3, then

ε3|U| · |W| |X| · |Y |

eG(X,Y ) |X| · |Y |

− d ≤

< ε

![image 35](<2009-lovasz-very-large-graphs_images/imageFile35.png>)

![image 36](<2009-lovasz-very-large-graphs_images/imageFile36.png>)

if |X| > ε|U| and |Y | > ε|W|. With these deﬁnitions, the Regularity Lemma can be stated as follows:

- Lemma 5.1 (Szemer´edi Regularity Lemma, usual form) For every ε > 0 there is a k =

k(ε) such that every graph G = (V,E) on at least k nodes has an equipartition {V1,...,Vk} (1/ε ≤ k ≤ k(ε)) such that for all but εk2 pairs of indices 1 ≤ i < j ≤ k, the bipartite graph G[Vi,Vj] is ε-regular.

One feature of the Regularity Lemma, which unfortunately forbids practical applications, is that k(ε) is very large: the best proof gives a tower of height about 1/ε2, and unfortunately this is not far from the truth, as was shown by Gowers [60].

5.2 Weak Regularity Lemma and distance of graphs

A version with a weaker conclusion but with a more reasonable error bound was proved by Frieze and Kannan [52].

- Lemma 5.2 (Weak Regularity Lemma) For every k ≥ 1 and every graph G = (V,E), V has a partition P into k classes such that


2 √log k

d (G,GP) ≤

.

![image 37](<2009-lovasz-very-large-graphs_images/imageFile37.png>)

![image 38](<2009-lovasz-very-large-graphs_images/imageFile38.png>)

Note that we do not require here that P be an equipartition; it is not hard to see that this version implies that there is also an equipartition with similar property, just we have to increase the error bound to 4/√log k.

![image 39](<2009-lovasz-very-large-graphs_images/imageFile39.png>)

To see the connection with the original lemma, we note that if G is an ε-regular bipartite graph say in the sense of (36), and H is the weighted complete bipartite graph with the same bipartition {U,W} and with edge weights d, then (36) says that d (G,H) ≤ ε. Hence if P is a Szemer´edi partition in the sense of Lemma 5.1, then the distance between the bipartite subgraph of G induced by Vi and Vj, and the corresponding weighted bipartite subgraph of GP, is at most ε for all but εk2 pairs (i,j), and at most 1 for the remaining εk2 pairs. It is easy to see that this implies that the distance between G and GP is at most ε. So the partition in Lemma 5.2 has indeed weaker properties than the partition in Lemma 5.1. Of course, this is compensated for by the relatively decent number of partition classes.

If we keep in GP an edge with weight p with probability p and delete it with probability 1−p, then we get a random graph H, and it is easy to see that with large probability d (GP,H) ≤ √ 10

. This implies the following version of the Weak Regularity Lemma:

![image 40](<2009-lovasz-very-large-graphs_images/imageFile40.png>)

![image 41](<2009-lovasz-very-large-graphs_images/imageFile41.png>)

|V (G)|

- Lemma 5.3 For every k ≥ 1 and graph G, there is a graph H with k nodes such that

δ (G,H) ≤

10 √log k

![image 42](<2009-lovasz-very-large-graphs_images/imageFile42.png>)

![image 43](<2009-lovasz-very-large-graphs_images/imageFile43.png>)

.

5.3 Strong Regularity Lemma and compactness

Other versions of the Regularity Lemma strengthen, rather than weaken, the conclusion (of course, at the cost of replacing the tower function by an even more formidable value). Such a “super-strong” Regularity Lemma was proved by Alon, Fisher, Krivelevich and Szegedy [5]. We state the following equivalent version from [87].

- Lemma 5.4 (Strong Regularity Lemma) For every sequence (ε0,ε1,...) of positive numbers there is a positive integer k0 such that for every graph G = (V,E), there is a graph G′ on V , and V has a partition P into k ≤ k0 classes such that


d1(G,G′) ≤ ε0 and d (G′,G′P) ≤ εk. (37)

Note that the ﬁrst inequality involves the normalized edit distance, and so it is stronger than a similar condition with the cut distance would be. The second error bound εk in (37) can be thought of very small. If we choose εk = ε0, we get the Frieze–Kannan version 5.2 (with ε = 2ε0). Choosing εk = ε0/k2, the partition obtained satisﬁes the requirements of the original Regularity

- Lemma 5.1.


The strong version itself follows rather easily from the compactness of the space (W0,δ ) (Theorem 4.2); see [85] for details.

- 5.4 Partitions into sets with small diameter


- 5.4.1 Small diameter sets and regularity


We can equip every graph G = (V,E) with a metric as follows. Let A be the adjacency matrix of G. We deﬁne the similarity distance of two nodes i,j ∈ V as the ℓ1 distance of the corresponding rows of A2 (squaring the matrix seems unnatural, but it is crucial; it turns out to get rid of random ﬂuctuations). The following was proved (in somewhat diﬀerent form) in [87].

- Theorem 5.5 Let G be a graph and let P = {V1,...,Vk} be a partition of V .


- (a) If d (G,GP) = ε, then there is a set S ⊆ V with |S| ≤ 8√ε|V | such that for each partition

![image 44](<2009-lovasz-very-large-graphs_images/imageFile44.png>)

class, Vi \ S has diameter at most 8√ε in the d2 metric.

![image 45](<2009-lovasz-very-large-graphs_images/imageFile45.png>)

- (b) If there is a set S ⊆ V with |S| ≤ δ|V | such that for each partition class, Vi \ S has


diameter at most δ in the d2 metric, then d (G,GP) ≤ 24δ.

Theorem 5.5 suggests to deﬁne the dimension of a family G of graphs as the inﬁmum of real numbers d > 0 for which the following holds: for every ε > 0 and G ∈ G the node set of G can be partitioned into a set of at most ε|V (G)| nodes and into at most ε−d sets of diameter at most ε. (This number can be inﬁnite.) In the cases when the graphs have a natural dimensionality, this dimension tends to give the right value. For example, let G be obtained by selecting n random points on the d-dimensional unit sphere, and connecting two of these points x and y with a probability W(x,y), which is a continuous function of x and y. With probability 1, this sequence has dimension Θ(d).

- 5.4.2 Computational applications


As an easy application of Theorem 5.5, we give an algorithm to compute a weak Szemer´edi partition in a huge graph. Our goal is to illustrate how an algorithm works in the pure sampling model, as well as in what form the result can be returned. This way of presenting the output of an algorithm for a large graph was proposed by Frieze and Kannan [52].

We start with an auxiliary algorithm that computes (approximately) the d2 distance of two nodes.

- Algorithm 5.6 Input: A graph G given by an sampling oracle, two nodes u,v ∈ V , and an error bound


ε > 0. Output: A number D2(u,v) ≥ 0 such that with probability at least 1 − ε, D2(u,v) − ε ≤ d2(u,v) ≤ D2(u,v) + ε.

To see how this can be done, we rewrite the deﬁnition of the d2 distance as follows. For x,y ∈ V (G), let a(x,y) be the corresponding entry of the adjacency matrix of G: this is 1 if they are adjacent and 0 otherwise. Deﬁne

a2(x,y) = Eza(x,z)a(y,z),

where z is a uniform random node in V ; this is the corresponding entry of the square of the adjacency matrix, normalized by |V (G)|. Finally, let

d2(x,y) = Ez(|a2(x,z) − a2(y,z)|),

where again z is a uniform random node in V . Drawing a suﬃciently large sample (depending on ε), these expectations can be approximated by averaging.

Algorithm 5.6 enables us to encode a partition of V (G) as a subset R ⊆ V (G): for each r ∈ R, we deﬁne the partition class Vr as the set of nodes u ∈ V such that the node in R closest to u is r. Ties will be broken arbitrarily, and nodes to which there are several “almost closest” nodes may be misclassiﬁed, but this is the best one can hope for. To formalize,

- Algorithm 5.7 Input: A graph G given by an sampling oracle, a subset R ⊆ V (G), a node u ∈ V , and an

error bound ε > 0. Output: An r ∈ R such that with probability at least 1 − ε, d2(u,r) ≤ (1 + ε)d2(u,r). The way this second algorithm works is that it uses Algorithm 5.6 to compute (approximately)

the distances d2(u,r), r ∈ R, and returns the node r ∈ R that it ﬁnds closest to u. Borrowing a phrase from geometry, we compute the Voronoi cells of the set R.

Using this encoding of the partition, the following algorithm computes a weak Szemer´edi partition.

- Algorithm 5.8 Input: A graph G given by an sampling oracle, and an error bound ε.


2

Output: A set R ⊆ V (G) with |R| ≤ 22/ε

such that, with probability at least 1 − ε, d2(u,R) ≤ ε for all but an ε fraction of the nodes u.

The set R is grown step by step, starting with the empty set. At each step, a new uniform random node w of G is generated, and the approximate distances D2(u,v) are computed for all r ∈ R with error less than ε/|R|. If all of these are larger than ε/2, w is added to R. Else,

- w is thrown out and a new random node is generated. If R is not increased in 1/ε2 steps, the algorithm halts.


It is clear that if more than an ε fraction of the nodes are farther than ε from R, then in 1/ε2 iterations we are very likely to sample one of these, and then with large probability we get the distances right and so we increase R.

Theorem 5.5 says in this context that the partition determined by Algorithms 5.6–5.8 satisﬁes d (G,GP) ≤ (4ε)1/4 with large probability.

We conclude with an answer to Question 4 in Section 1.2. For the partition P implicitly determined above, we can also compute the edge densities between the partition classes, which we use to weight the edges of the complete graph on R, so that we get a weighted graph H. We ﬁnd the maximum cut in H by brute force, to get a partition R = R1∪R2. This gives an implicit deﬁnition of a cut in G, where a node u if put on the left side of the cut iﬀ D2(u,R1) < D2(u,R2) for the approximate distances computed by Algorithm 5.6.

- 5.5 Regularity Lemmas for bounded degree graphs?

The Regularity Lemma as discussed above does not say anything for non-dense graphs. Several extensions for this case are known [71, 54], but they are meaningless for graphs that are very sparse, in particular if they have bounded degree.

Is there a Regularity Lemma for graphs with bounded degree? There are great diﬃculties here, but three results justify cautious optimism.

An observation of Alon (unpublished) implies that a weak analogue of the Regularity Lemma, version 5.3, holds. Using the sampling distance introduced in Section 1.3.1, we can state this as follows:

Proposition 5.9 For every d ≥ 1 and ε > 0 there is a n = n(d,ε) such that for every graph G with degrees bounded by d there is a graph H with degrees bounded by d and |V (H)| ≤ n, such that dsample(G,H) ≤ ε.

Unfortunately, no eﬀective bound on n follows from the proof. It would be very interesting to give any explicit bound on the function n(d,ε), or to give an algorithm to construct H from G. Ideally, one would like to design an algorithm that would work in the sampling framework, similarly as the algorithm in Section 5.4.2 works in the dense case.

It was proved recently by Elek and Lippner [41], and independently by Angel and Szegedy [11] that every graph with degrees bounded by d can be decomposed by deleting εn edges into “highly homogeneous” parts, where the number of these parts is bounded by a function of d and ε. Unfortunately, the highly homogeneous parts can still have a complex structure, but this may be a ﬁrst important step in the direction of ﬁnding an analogue of the Regularity Lemma.

A third idea of decomposition is related to Følner sequences in the theory of amenable groups, and is called hyperﬁniteness for general graph sequences [40, 102]. A family G of graphs with bounded degree is called hyperﬁnite, if for every ε > 0 there is a kε ≥ 1 such that from every graph G ∈ G we can delete ε|V (G)| edges so that every connected component of the remaining graph has at most kε nodes. Schramm [102] showed that for a convergent graph sequence, hyperﬁniteness is reﬂected by the limit object.

A special case of a hyperﬁnite family is a family G of graphs with subexponential growth, familiar from group theory. This property is deﬁned by requiring that there is a function f : N → N such that (ln f(m))/m → 0 (m → ∞), and for any graph G ∈ G, any v ∈ V (G) and any m ∈ N, the number of nodes in the m-neighborhood of v is at most f(m).

It is likely that large real-life networks can be thought of as hyperﬁnite; on the other hand, hyperﬁnite families of graphs seem to be much better behaved, and some of the theory of dense graph sequences can be extended at least to this case.

6 Convergence and limits I: the dense case

- 6.1 Subgraph sampling


Recall that we can deﬁne a notion of convergence if we ﬁx a sampling method. For dense graphs, we use subgraph sampling: We select uniformly a random k-element subset of V (G), and return

the subgraph G[k] induced by them. The probability that we see a given graph F is the quantity tind(F,G) introduced in (3). A sequence of graphs (Gn) with |V (Gn)| → ∞ is convergent if the induced subgraph densities tind(F,Gn) converge for all ﬁnite graphs F.

We use this sampling method for dense graphs (otherwise all these densities tend to 0).

Instead of the induced subgraph densities tind(F,Gn), we could use the subgraph densities tinj(F,Gn) or the homomorphism densities t(F,Gn). Indeed, the subgraph densities can be expressed as linear combinations of induced subgraph densities and vice versa, while the diﬀerence

- t(F,G) − tinj(F,G) = O(1/|V (G)|), and so it tends to 0 if |V (G)| → ∞. We can extend this sampling procedure to graphons, and we get to the construction of W-


random graphs.

- 6.2 Convergence in distance


The deﬁnition of convergence can be reformulated using the notion of sampling distance 1: a sequence (Gn) of simple graphs with |V (Gn)| → ∞ is convergent if for every graph F, (tind(F,Gn) : i = 1,2,...) is a Cauchy sequence (equivalently, (t(F,Gn) : i = 1,2,...) is a Cauchy sequence). This is equivalent to saying that the graph sequence is Cauchy in the dsample metric. The following theorem, which is one of the main results in this theory, justiﬁes the use of the cut metric δ .

- Theorem 6.1 A sequence (Gn) of simple graphs (|V (Gn)| → ∞) is convergent if and only if it is a Cauchy sequence in the metric δ .


A quantitative form of this equivalence is given by the following theorem. Part (a) is a generalization of what is called the “Counting Lemma” in the theory of Szemer´edi partitions; part (b) may be called the “Anti-counting” lemma.

- Theorem 6.2 Let U,W ∈ W0. (a) For every simple ﬁnite graph F,


|t(F,U) − t(F,W)| ≤ |E(F)| · δ (U,W).

(b) Let k be a positive integer, and assume that for every simple graph F on k nodes, we have

2

|t(F,U) − t(F,W)| ≤ 2−k

.

Then

20 √log k

δ (U,W) ≤

.

![image 46](<2009-lovasz-very-large-graphs_images/imageFile46.png>)

![image 47](<2009-lovasz-very-large-graphs_images/imageFile47.png>)

The proof of part (a) is quite simple; part (b) depends on the sampling lemmas to be discussed in Section 6.4.

Theorem 6.1 can be generalized to characterize convergence in the space W:

- Theorem 6.3 Let (Wn) be a sequence of graphons in W0 and let W ∈ W0. Then t(F,Wn) converges for all ﬁnite simple graphs F if and only if Wn is a Cauchy sequence in the δ metric. Furthermore t(F,Wn) → t(F,W) for all ﬁnite simple graphs F if and only if δ (Wn,W) → 0.

6.3 Convergence from the right

Convergence of a graph sequence can also be characterized in terms of mappings “to the right”. Several characterizations along these lines were given in [30]; here we state one:

- Theorem 6.4 Let (Gn) be a sequence of simple graphs such that |V (Gn)| → ∞ as n → ∞. Then the sequence (Gn) is left-convergent if and only if the sequence E(Gn,H) is convergent for every weighted graph H.


- 6.4 Sampling and distance


The proof of the results in the previous section depends on a couple of probabilistic lemmas, which relate sampling to cut distance. The ﬁrst of these lemmas is due to Alon, Fernandez de la Vega, Kannan and Karpinski [6], with an improvement from [29]. Its proof is quite involved. Its main implication is that the d -distance of two graphs G and H on the same set of nodes can be estimated by sampling. It should be noted that the bound given is quite sharp.

- Lemma 6.5 Let k be a positive integer and let G and H be graphs with V (G) = V (H), |V (G)| ≥ k and edge weights in [0,1]. Let S be chosen uniformly from all subsets of V (G) of size k. Then


√

![image 48](<2009-lovasz-very-large-graphs_images/imageFile48.png>)

with probability at least 1 − 2e−

k/8. d (G[S],H[S]) − d (G,H) ≤

10 k1/4

.

![image 49](<2009-lovasz-very-large-graphs_images/imageFile49.png>)

The second lemma about sampling [29] shows that a sample is close to the original graph with large probability. Note that here we have to sue the δ distance (since no overlaying is given a priori), and also that the bound on the distance is much weaker than in the previous lemma.

- Lemma 6.6 Let k ≥ 1, and let G be a simple graph on at least k nodes. If S is a random subset of V (G) of size k, then with probability at least 1 − 2−k,


10 √log k

δ (G,G[S]) ≤

.

![image 50](<2009-lovasz-very-large-graphs_images/imageFile50.png>)

![image 51](<2009-lovasz-very-large-graphs_images/imageFile51.png>)

This lemma follows from Lemma 6.5 and the Weak Regularity Lemma 5.2. Let us sketch this proof. Proof. Fix some m ≥ 1. By Lemma 5.2, there is an equipartition P = {V1,...,Vm} of V (G) into m classes such that

4 √log m

d (G,GP) ≤

.

![image 52](<2009-lovasz-very-large-graphs_images/imageFile52.png>)

![image 53](<2009-lovasz-very-large-graphs_images/imageFile53.png>)

Now let S be a random k-subset. By Lemma 6.5, we have

10 k1/4

|d (G[S],GP[S]) − d (G,GP)| ≤

![image 54](<2009-lovasz-very-large-graphs_images/imageFile54.png>)

with large probability. If k is suﬃciently large relative to m, then every class Vi will contain about k/m nodes from S. Indeed, a simple application of Chebyshev’s Inequality gives that with probability at least 3/4,

√

k m ≤ 2

![image 55](<2009-lovasz-very-large-graphs_images/imageFile55.png>)

|Vi ∩ S| −

k holds for all i.

![image 56](<2009-lovasz-very-large-graphs_images/imageFile56.png>)

Now blow up each node of GP[S] into n/k twins to get a weighted graph G′ (in notation:

G′ = GP[S](nk)). Then each set Vi ∩ S is blown up into a set Vi′ of size nk|Vi ∩ S| ≈ |Vi| = mn . In fact,

![image 57](<2009-lovasz-very-large-graphs_images/imageFile57.png>)

![image 58](<2009-lovasz-very-large-graphs_images/imageFile58.png>)

![image 59](<2009-lovasz-very-large-graphs_images/imageFile59.png>)

m

|Vi′| − |Vi| ≤ 2

i=1

√

![image 60](<2009-lovasz-very-large-graphs_images/imageFile60.png>)

km

n k

2nm √

=

.

![image 61](<2009-lovasz-very-large-graphs_images/imageFile61.png>)

![image 62](<2009-lovasz-very-large-graphs_images/imageFile62.png>)

![image 63](<2009-lovasz-very-large-graphs_images/imageFile63.png>)

k

It follows that we can overlay G′ and GP so that corresponding edges have the same weight except for edges inside the classes Vi and edges incident with at most mi=1 |Vi′| − |Vi| nodes. This is only a fraction of m1 + 4√mk of all edges, which shows that

![image 64](<2009-lovasz-very-large-graphs_images/imageFile64.png>)

![image 65](<2009-lovasz-very-large-graphs_images/imageFile65.png>)

![image 66](<2009-lovasz-very-large-graphs_images/imageFile66.png>)

4m √

1 m

δ (GP,GP[S]) = δ (GP,G′) ≤

+

.

![image 67](<2009-lovasz-very-large-graphs_images/imageFile67.png>)

![image 68](<2009-lovasz-very-large-graphs_images/imageFile68.png>)

![image 69](<2009-lovasz-very-large-graphs_images/imageFile69.png>)

k

Hence

δ (G,G[S]) ≤ δ (G,GP) + δ (GP,GP[S]) + δ (GP[S],G[S]) ≤

1 m

10 k1/4

4 √log m

4m √

+

+

+

.

![image 70](<2009-lovasz-very-large-graphs_images/imageFile70.png>)

![image 71](<2009-lovasz-very-large-graphs_images/imageFile71.png>)

![image 72](<2009-lovasz-very-large-graphs_images/imageFile72.png>)

![image 73](<2009-lovasz-very-large-graphs_images/imageFile73.png>)

![image 74](<2009-lovasz-very-large-graphs_images/imageFile74.png>)

![image 75](<2009-lovasz-very-large-graphs_images/imageFile75.png>)

k

Choosing m = k1/4, we get

10 k1/4

1 k1/4

4 k1/4

10 √log k if k is large enough.

8 √log k

δ (G,G[S]) ≤

+

+

+

<

![image 76](<2009-lovasz-very-large-graphs_images/imageFile76.png>)

![image 77](<2009-lovasz-very-large-graphs_images/imageFile77.png>)

![image 78](<2009-lovasz-very-large-graphs_images/imageFile78.png>)

![image 79](<2009-lovasz-very-large-graphs_images/imageFile79.png>)

![image 80](<2009-lovasz-very-large-graphs_images/imageFile80.png>)

![image 81](<2009-lovasz-very-large-graphs_images/imageFile81.png>)

![image 82](<2009-lovasz-very-large-graphs_images/imageFile82.png>)

Both lemmas 6.5 and 6.6 extend to graphons. We only formulate the second one, which can be stated in terms of the W-random graphs G(k,W).

- Lemma 6.7 Let k ≥ 1, and let W be a graphon. Then with probability at least 1 − 2−k,


11 √log k

δ (G(k,W),W) ≤

.

![image 83](<2009-lovasz-very-large-graphs_images/imageFile83.png>)

![image 84](<2009-lovasz-very-large-graphs_images/imageFile84.png>)

To illustrate how these lemmas ﬁt in the proofs, let us ﬁrst sketch how Lemma 6.7 implies the “anti-counting lemma” (Theorem 6.2(b)). Assume that U,W ∈ W0 satisfy

2

|t(F,U) − t(F,W)| ≤ 2−k

for every graph F with k nodes. In terms of the W-random graphs G(k,U) and G(k,W), this implies (by inclusion-exclusion) that

Pr(G(k,U) ∼= F) − Pr(G(k,W) ∼= F) ≤ 2(k

)2−k

2

,

2

and hence

F

2

Pr(G(k,U) ∼= F) − Pr(G(k,W) ∼= F) ≤ 2k(k−1)2−k

= 2−k.

This means that we can couple G(k,U) and G(k,W) so that G(k,U) ∼= G(k,W) with probability at least 1 − 2−k. Lemma 6.7 implies that with probability at least 1 − 2−k, we have

10 √log k

δ (U,G(k,U)) ≤

,

![image 85](<2009-lovasz-very-large-graphs_images/imageFile85.png>)

![image 86](<2009-lovasz-very-large-graphs_images/imageFile86.png>)

and similar assertion holds for W. Whenever all three happen, we get

20 √log k

δ (U,W) ≤ δ (U,G(k,U)) + δ (G(k,U),G(k,W)) + δ (W,G(k,W)) ≤

.

![image 87](<2009-lovasz-very-large-graphs_images/imageFile87.png>)

![image 88](<2009-lovasz-very-large-graphs_images/imageFile88.png>)

- 6.5 Dense limit The main motivation behind considering graphons is the following theorem [85]:


- Theorem 6.8 For any convergent sequence (Gn) of simple graphs there exists a graphon W such that t(F,Gn) → t(F,W) for every simple graph F.

We say that this graphon W is the limit of the graph sequence, and write Gn → W. One might wonder if we really need complicated objects like integrable functions to describe these limits; would perhaps piecewise linear, or monotone, or continuous functions suﬃce? The following two results tell us that (up to weak isomorphism) all measurable functions are needed: every graphon W can be obtained as the limit of a sequence of simple graphs [85], and the limit is essentially unique [26].

- Theorem 6.9 For any W ∈ W0, the graph sequence G(n,W) converges to the graphon W with probability 1.

On the other hand, Theorem 3.1 implies:

- Theorem 6.10 ([26]) The limit graphon of a convergent graph sequence is uniquely determined up to weak isomorphism.


There are two quite diﬀerent proofs of the (main) theorem 6.8. The original one in [85] uses Szemer´edi partitions and the Martingale Convergence Theorem; a more recent proof by Elek and Szegedy [42] ﬁrst constructs a diﬀerent limit object in the form of an uncountable graph by taking the ultraproduct, and them obtains the graphon as an appropriate projection of this (in terms of non-standard analysis, the graphon is a non-standard Szemer´edi partition of this graph on a non-standard [0,1] interval).

The ﬁrst proof has the obvious advantage of being a constructive; but the second proof is very general, it extends to hypergraphs and many other structures, and leads to new understanding of the Regularity Lemma for hypergraphs [60, 61, 100] and its consequences [115].

Convergence to the limit object can also be characterized by the distance function introduced above [29]:

- Theorem 6.11 For a sequence (Gn) of graphs with |V (Gn)| → ∞ and graphon W, we have

Gn → W if and only if δ (WG

n

,W) → 0. Note that the function WG

n

depends on the labeling of the nodes of Gn (the distance δ (WG

n

,W) does not, since relabeling Gn results in weak isomorphism of WG

n

). Choosing the labeling appropriately, we can say more:

- Theorem 6.12 For a sequence (Gn) of graphs with |V (Gn)| → ∞ and graphon W, we have

Gn → W if and only if the graphs Gn can be labeled so that WG

n − W → 0. 6.5.1 Equivalent descriptions of the limit

A random graph model is a probability distribution on simple graphs on [n], for every n ≥ 1, which is invariant under the reordering of the nodes. In other words, it is a sequence of random variables Gn, whose values are simple graphs on [n], and isomorphic graphs have the same probability. We say that a random graph model is consistent if deleting node n from Gn, the distribution of the resulting graph is the same as the distribution of Gn−1. We say that the model is local, if for every 1 < k < n, the subgraphs of Gn induced by [k] and {k + 1,...,n} are independent as random variables.

It is easy to see that for every graphon W ∈ W0, G(n,W) is a consistent and local random graph model.

A related notion is the following. Let G be the set of graphs on N; we can think of G as the product space {0,1}E, where E = N2 is the set of all (unordered) pairs of elements of N. This also equips G with a σ-algebra. Let Σ be the group of permutations of N, and let Σ2 be the action of Σ on E. Recall that a probability measure π on G is called ergodic with respect to Σ2 if it is invariant under Σ2 and G has no measurable subset G′ with 0 < π(G′) < 1 invariant under Σ2.

It is easy to see for that every W ∈ W, the random graph G(W) deﬁnes a probability measure on G invariant under Σ2. B. Szegedy [111] showed that this measure is also ergodic.

After this preparation, we can formulate the theorem describing the many notions equivalent to graphons.

- Theorem 6.13 The following structures are cryptomorphic:


- (a) a graphon W ∈ W0, up to weak isomorphism;
- (b) A graph parameter f that is the limit of graph parameters t(.,Gn) for some convergent

graph sequence (Gn).

- (c) A multiplicative, reﬂection positive graph parameter f satisfying f(K1) = 1,
- (d) a consistent local random graph model;
- (e) an ergodic measure on G invariant under Σ2.


The equivalences of these structures are mostly contained in results mentioned previously. Let us sketch these constructions.

(a)→(b): Every graphon W ∈ W0 gives rise to the graph parameter t(.,W); furthermore, W is the limit of a convergent graph sequence (Gn) (for example, of the sequence of W-random graphs), and for this sequence t(F,Gn) → t(F,W) for all F.

- (b)→(c): If a graph parameter is the limit of graph parameters t(.,Gn), which satisfy the

conditions in (c), then clearly so does their limit.

- (c)→(d): In the special case when f = t(.,G) is the probability that a random map from F

to some graph G is a homomorphism, we can express the probability that a sample of n points gives a given graph F0, by inclusion-exclusion in terms of the numbers f(F). We can apply the same formula to any graph parameter f satisfying (c), and get a probability distribution on n-point graphs (here the conditions in (c) are used), which is a consistent local random graph model.

- (d)→(a): Generating a random graph Gn from the consistent local random graph model,


it can be shown that we get a convergent graph sequence with probability 1, which tends to a graphon W. For this graphon, G(n,W) gives back the random graph model we started with.

(d)↔(e): It is easy to see that a consistent random graph model is equivalent to a probability distribution on G invariant under Σ2. The proof that locality is equivalent to ergodicity [111] is trickier and not given here.

Corollary 6.14 A graph parameter f is reﬂection positive if and only if it is either identically 0, or there is a probability distribution ρ on the Borel sets of (W0,δ ) such that if W denotes a random function from this distribution, then

f(F) = Et(F,W).

- 6.5.2 Examples We start with two easy examples.


- Example 6.15 Complete bipartite graphs. It is natural to guess, and easy to prove, that com-

plete bipartite graphs Kn,n converge to the function deﬁned by W(x,y) = 1 if 0 ≤ x ≤ 1/2 ≤ y ≤ 1 or 0 ≤ y ≤ 1/2 ≤ x ≤ 1, and W(x,y) = 0 otherwise.

- Example 6.16 Threshold graphs. These graphs are deﬁned on the set {1,...,n} by connecting i and j if and only if i+j ≤ n. These graphs converge to the function deﬁned by W(x,y) = 1x+y≤1.
- Example 6.17 A sequence of graphs tending to the identically-p function is exactly what we called a quasirandom sequence with density p.

Two examples of randomly growing graph sequences:

- Example 6.18 Randomly grown uniform attachment graph. We start with a single node. At the n-th iteration, a new node is born, and then every pair of nonadjacent nodes is connected with probability 1/n. We call this graph sequence a randomly grown uniform attachment graph sequence.


Let us do some simple calculations. After n steps, let {0,1,...,n − 1} be the nodes (born in

this order). The probability that nodes i < j are not connected is j+1j · jj+2+1 ··· n−n1 = nj . These events are independent for all pairs (i,j). From here, one can easily ﬁgure out that the expected

![image 89](<2009-lovasz-very-large-graphs_images/imageFile89.png>)

![image 90](<2009-lovasz-very-large-graphs_images/imageFile90.png>)

![image 91](<2009-lovasz-very-large-graphs_images/imageFile91.png>)

![image 92](<2009-lovasz-very-large-graphs_images/imageFile92.png>)

number of edges is (n2 − 1)/6.

To describe the limit function, note that the probability that nodes i and j are not connected is max(i,j)/n. If i = xn and j = yn, then this is max(x,y). Using that these events are independent, we can prove that the graph sequence Guan tends to the limit function 1−max(x,y) with probability 1.

- Example 6.19 Randomly grown preﬁx attachment graph. In this construction, it will be more convenient to label the nodes starting with 1. At the n-th iteration, a new node n is born, a node z ≤ n is selected at random, and the new node is connected to nodes 1,...,z − 1. We


denote the n-th graph in the sequence by Gpfxn , and call this graph sequence a randomly grown preﬁx attachment graph sequence.

The expected number of edges is n(n − 1)/4, and one can compute subgraph densities with some eﬀort to see that the sequence is convergent with probability 1. It is more diﬃcult to ﬁgure out the limit graphon.

We can try to proceed similarly as in the case of uniform attachment graphs. The probability that i and j are connected is |j−i|/ max(i,j); if i = xn and j = yn, then this is |x−y|/ max(x,y). Does this mean that the function U(x,y) = |x − y|/ max(x,y) is the limit? Surprisingly, the answer is negative, which we can see by computing triangle densities.

The key to describe the limit is the remark at the end of Section 1.5.3, namely that instead of the uniform distribution over the interval [0,1], we can use other probability spaces. Let us label a node born in step k, connected to {1,...,m}, by the pair (k/n,m/k) ∈ [0,1] × [0,1]. Then we can observe that nodes with label (x1,y1) and (x2,y2) are connected if and only if either

- x1 < x2y2 or x2 < x1y1.


From this observation one can prove that the preﬁx attachment graphs Gpfxn converge, with probability 1, to the function W : [0,1]2 × [0,1]2 → [0,1], given by

Wpfx((x1,y1),(x2,y2)) =

1, if x1 < x2y2 or x2 < x1y1, 0, otherwise.

This gives a nice and simple representation of the limit object with the underlying probability space [0,1]2 (with the uniform measure). If we want a representation on [0,1], we can map [0,1] into [0,1]2 by any measure preserving map ϕ; then Wpfxϕ (x,y) = Wpfx(ϕ(x),ϕ(y)) gives a weakly isomorphic graphon. This function is 0 − 1 valued, but its support is fractal-like.

It is interesting to note that the graphs G(n,W) form a diﬀerent growing sequence of random graphs tending to the same limit W with probability 1.

- 6.6 Convergence from the right


Paper [30] contains several conditions that characterize convergent dense graph sequences in terms of homomorphisms “to the right” (we have seen that these correspond to parameters with meaning in statistical physics). We only state one of these, in our terms:

- Theorem 6.20 Let (Gn) be a sequence of graphs such that |V (Gn)| → ∞ as n → ∞. Then the sequence (Gn) is convergent if and only if the restricted multicut densities rmcut(Gn,H) are convergent for every weighted graph H.


By (11), the value rmcut in this theorem could be replaced by hom∗(G,H), and by our discussion in Section 2.3.3, we could talk about microcanonical ground state energies instead of restricted multicuts.

- 6.7 Limits of other dense combinatorial structures


Limit objects can be deﬁned for multigraphs, directed graphs, colored graphs, hypergraphs etc. In many cases, like directed graphs without parallel edges, or graphs with nodes colored with a ﬁxed number of colors, this can be done along the same lines as for simple graphs.

But in other cases there are some surprises. For example, limits of multigraphs with edgemultiplicities are not real valued functions, but 2-variable functions whose values are random variables with nonnegative integral values [89]. If W is such a function, we can generate a W-random multigraph by selecting n independent random points X1,...,Xn from the uniform distribution on [0,1], and then connecting nodes i and j with W(Xi,Xj) parallel edges (which is a random integer).

The case of hypergraphs is much more interesting and important. Formulating regularity lemmas and constructing limits of sequences of r-uniform hypergraphs, where r is ﬁxed, is a highly nontrivial task, but it is essentially solved now, thanks to the work of Ro¨dl and Skokan and Gowers [100, 59]; see also [114, 42].

However, it seems that no good extension of the distance δ has been found to hypergraphs (just as for the regularity lemma, the ﬁrst natural guesses are wrong). Another open question is to extend these results to nonuniform hypergraphs, with unbounded edge-size.

The semideﬁniteness conditions for homomorphism functions can be extended to hypergraphs (see e.g. [80]). One area of applications of these conditions is extremal graph theory, and it is natural to ask if the semideﬁniteness conditions can be useful in extremal hypergraph theory, especially since extremal problems for hypergraphs tend to be much harder than for graphs, and even basic questions are unsolved.

## 7 Convergence and limits II: bounded degree graphs

- 7.1 Neighborhood sampling


Recall the sampling process for bounded degree graphs: For a ﬁxed nonnegative integer r, we select uniformly a random node v ∈ V (G), and return the ball BG(v,r) with center v and radius r (i.e., the subgraph induced by those nodes that can be reached from v on a path of length r or less). For a given rooted graph F, we denote by ρG,r(F) the probability that this sampling method returns F (with the root as the center). So ρG,r(F) deﬁnes a probability distribution on rooted graphs F with radius at most k, which we denote by ρG,r.

We use this method if the degrees of nodes in G are bounded by a ﬁxed number d; then the number of possible neighborhoods is ﬁnite.

A sequence of graphs (Gn) with degrees uniformly bounded by d and |V (Gn)| → ∞ is convergent (or more precisely locally convergent) if the neighborhood densities ρG

n,r(F) converge for all r and all ﬁnite rooted graphs F.

Similarly as for the subgraph sampling, there are equivalent density type parameters whose convergence could be used instead of the neighborhood densities, for example, we could stipulate the convergence of s(F,Gn) for every connected graph F.

- 7.2 Local (weak) limit


- 7.2.1 Diﬀerent forms


A weakly convergent bounded degree graph sequence has several, not quite equivalent limit objects, which we have introduced in Section 3.2. Part (a) of the following theorem is due to Benjamini and Schramm [16]; part (b) was formulated by R. Kleinberg (unpublished); part (c), which implies (b), is due to Elek [37].

- Theorem 7.1 Let (Gn) be a locally convergent sequence of graphs with degrees bounded by d. Then


- (a) There is a unique unimodular distribution τ on countable rooted graphs with degrees

bounded by d such that ρG

n,r → ρτ.

- (b) There is a measure preserving graph G such that ρG

n,r → ρG,r for every k ≥ 1.

- (c) There is a graphing G such that ρG


n,r → ρG,r for every k ≥ 1.

Note that in (b) we don’t claim uniqueness. We could replace “graphing” by “measure preserving graph”.

A big diﬀerence from the dense case is that there does not seem to be any easy way to construct a sequence that converges to a given graphing in this sense.

Conjecture 7.2 (Aldous–Lyons) Every graphing is the limit of a convergent sequence of bounded-degree graphs. Equivalently, every unimodular distribution on rooted countable graphs with bounded degree is the limit of a bounded degree graph sequence.

- 7.2.2 Is the limit informative enough?


The problem of the Regularity Lemma is related to conjecture 7.2. Indeed, suppose that we have a constructive way of ﬁnding, for an arbitrarily large graph G with bounded degree, a graph H of size bounded by a function of r and ε that approximates the distribution of r-neighborhoods in G with error ε. The same construction should also work with a graphing instead of G. Letting r → ∞ and ε → 0, this would give a sequence of ﬁnite bounded degree graphs converging to the given graphing.

Part of the problem is to recognize “globally” when H is a good approximation of G. Is there a good notion of “distance” (analogous to δ ) for graphs with bounded degree?

The limit graphon of a dense sequence of graphs contains very much information about the asymptotic properties of the sequence. This is not so for the dense case, unfortunately.

Problem 7.3 Is there a notion of convergence for graphs with bounded degree that is stronger than Benjamini–Schramm? (For example, one should be able to read oﬀ from the limit that the graphs are expanders.)

Let us illustrate this by a couple of simple examples.

- Example 7.4 Let (Gn) be a sequence of 3-regular bipartite expander graphs with their girth tending to inﬁnity. Let Hi consist of two disjoint copies of Gi. The Benjamini–Schramm limit of both sequences is a distribution concentrated on a single 3-regular rooted tree. In the Elek

description, we get a graphing (Ω,T1,T2,T3), where T1,T2 and T3 generate a free group which acts on Ω without ﬁxed points.

This limit graphing is not uniquely determined. One feels that in the case of the limit of the sequence (Gn), the action of the free group should ergodic, while in the case of the Hn, Ω should split into two invariant subsets of measure 1/2. So it appears that in the limit object, the underlying σ-algebra also carries combinatorial information. This is in stark contrast with the dense case [26].

- Example 7.5 Let Gn denote the n × n grid. The Benjamini-Schramm limit object is a probability distribution concentrated on the inﬁnite grid with a speciﬁed root (the “origin”). A limit graphing can be described as the uniform measure on the 2-dimensional torus, together with the rotations by an irrational number α in one coordinate and the other.


However, in many respects the “right” limit object of the sequence of grids is a solid square. In other words, instead of larger and larger pieces of the inﬁnite grid, we consider ﬁner and ﬁner subdivisions of the unit square.

This last example suggests that we can consider our graphs “on a diﬀerent scale”, and study them as metric spaces with the usual graph distance as metric, normalized by the diameter. We can then consider the limit of these metric spaces in the sense of Gromov [62]. For example, the limit of a sequence of larger and larger square grids in this sense is a (full) square. This global structure is not revealed by the Benjamini–Schramm limit.

It is easy to construct examples where the interesting structure of the graphs appears on an intermediate scale. It would be very interesting to describe and possibly unify limit objects belonging to diﬀerent scales. Perhaps we can we understand diﬀerent limit objects using ultraproducts, similarly to the work of Elek and Szegedy in the dense case.

- 7.3 Convergence from the right


While the description of convergent sequences in the bounded degree case lacks some of the key results that hold in the dense case, most notably a good notion of distance, we can formulate a result (Borgs, Chayes, Kahn and Lov´asz [25]) which shows that convergence deﬁned in terms

of homomorphisms from the left and homomorphisms to the right are equivalent under some circumstances.

To state this, let us deﬁne for every simple graph G and weighted graph H the quantity u(G,H) =

log hom(G,H) |V (G)|

,

![image 93](<2009-lovasz-very-large-graphs_images/imageFile93.png>)

To see the meaning of u(G,H), consider the case when H is simple. Then hom(G,H) ≤ q|V (G)|, and so after taking the logarithm and dividing by |V (G)|, we get a number less than q. So

- u(G,Kq) expresses the freedom (entropy) we have in choosing the image of a node v ∈ V (G) in a homomorphism G → H.


For a weighted graph H, we deﬁne and βmax = max

αiαj α2H

βij βmax

1 −

βij, D(H) =

.

![image 94](<2009-lovasz-very-large-graphs_images/imageFile94.png>)

![image 95](<2009-lovasz-very-large-graphs_images/imageFile95.png>)

i,j

i,j∈V (H)

- Theorem 7.6 Let (Gn) be a sequence of graphs with maximum degree at most d.

- (a) If (Gn) is convergent, then for every weighted graph H be a weighted graph with D(H) ≤

- 1

![image 96](<2009-lovasz-very-large-graphs_images/imageFile96.png>)

- 2d, the sequence u(Gn,H) is convergent.


- (b) Assume that for every q ≥ 1 there is an εq > 0 such that for every weighted graph H


on q nodes with D(H) ≤ εq the sequence q(Gn,H) is convergent. Then the sequence (Gn) is convergent.

In the special case H = Kq is the complete graph on q nodes (without loops), we have D(Kq) = 1/q, and hom(G,Kq) is the number of q-colorings of G. So it follows that if (Gn) is convergent and q ≥ 2d, then the number of q-colorations grows as c|V (G

n)| for some c. It is easy to see that some condition on q is needed: for example, if Gn is the n-cycle and q = 2, then q(Gn,K2) oscillates between −∞ and ≈ 0 as a function of n.

8 Testing

What can we learn about a huge graph G from sampling? There are two related, but slightly diﬀerent ways of asking this question, property testing and parameter estimation.

- 8.1 Sample concentration


Before discussing these tasks, let us address the following concern: if we take a bounded size sample from a graph, we can see very diﬀerent graphs. For a random graph, for example, we can see anything. The natural way to use the sample G[S] is to compute some graph parameter

- f(G[S]). But this parameter can vary wildly with the choice of the sample, so what information do we get?


The following two theorems assert that every reasonably smooth parameter of a sample is highly concentrated. (Note: we don’t say anything here about the value of the parameter on the whole graph.)

The ﬁrst version applies to parameters where smoothness is deﬁned locally. The proof depends on the theory of martingales (Azuma’s Inequality).

- Theorem 8.1 Let f be a graph parameter and assume that |f(G) − f(G′)| ≤ 1 for any two graphs on the same node set which diﬀer only in edges incident with a single node. Then for


every graph G and 1 ≤ k ≤ |V (G)| there is a value f0 such that if S ⊆ V (G) is a random k-subset, then for every t > 0,

√

![image 97](<2009-lovasz-very-large-graphs_images/imageFile97.png>)

|f(G[S]) − f0| <

2tk with probability at least 1 − e−t.

The second version applies to parameters which are smooth with respect to our global distance function. The proof follows from a modiﬁcation of the proof of Theorem 6.6.

- Theorem 8.2 Let f be a graph parameter and assume that |f(G) − f(G′)| ≤ d (G,G′) for any two graphs on the same node set. Then for every graph G and 1 ≤ k ≤ |V (G)| there is a value f0 such that if S ⊆ V (G) is a random k-subset, then

|f(G[S]) − f0| <

20 √

![image 98](<2009-lovasz-very-large-graphs_images/imageFile98.png>)

![image 99](<2009-lovasz-very-large-graphs_images/imageFile99.png>)

k with probability at least 1 − 2−k.

8.2 Parameter estimation

We want to determine some parameter of a very large graph G. Of course, we’ll not be able to determine the exact value of this parameter; the best we can hope for is that if we take a suﬃciently large sample, we can ﬁnd the approximate value of the parameter with large probability.

To be precise, a graph parameter f is testable, if for every ε > 0 there is a positive integer k such that if G is a graph with at least k nodes and we select a set X of k independent uniform random nodes of G, then from the subgraph G[X] induced by them we can compute an estimate g(G[X]) of f such that

P(|f(G) − g(G[X])| > ε) < ε. It is an easy observation that we can always use g(G[X]) = f(G[X]) (cf. [57]).

It is easy to see that testability is equivalent to saying that for every convergent graph sequence (Gn), the sequence of numbers (f(Gn)) is convergent. (So graph parameters of the form t(F,.) are testable by the deﬁnition of convergence.) This is, however, more-or-less just a reformulation of the deﬁnition. Paper [29] contains a number of more useful conditions characterizing testability of a graph parameter. We formulate one, which is perhaps easiest to verify:

- Theorem 8.3 A graph parameter f is testable if and only if the following three conditions hold:


- (i) For every ε > 0 there is an ε′ > 0 such that if G and G′ are two simple graphs on the

same node set and d (G,G′) ≤ ε′ then |f(G) − f(G′)| ≤ ε.

- (ii) For every simple graph G, f(G(m)) has a limit as m → ∞. (Recall that G(m) denotes

the graph obtained from G by blowing up each node into m twins. )

- (iii) If G+ is obtained from G by adding a single isolated node, then f(G+) − f(G) → 0 if


|V (G)| → ∞.

Note that all three conditions are special cases of the statement that

- (iv) if |V (Gn)|,|V (G′n)| → ∞ and δ (Gn,G′n) → 0, then f(Gn) − f(G′n) → 0. This condition is also necessary, so it is equivalent to its own three special cases (i)–(iii) in


the Theorem.

- Example 8.4 As a basic example, consider the density of maximum cuts (recall Section 2.3.2). One of the ﬁrst substantial results on property testing [56, 12] is that this parameter is testable. It is relatively easy to see (using high concentration results like Azuma’s inequality) that if S is a suﬃciently large random subset of nodes of G, then maxcut(G[S]) ≥ maxcut(G) − ε: a large cut in G, when restricted to S, gives a large cut in G[S]. It is harder, and in fact quite surprising, that if most subgraphs G[S] have a large cut, then so does G. This follows from Theorem 8.3 above, since conditions (i)–(iii) are easily veriﬁed for f = maxcut.
- Example 8.5 The free energy (16) for a ﬁxed weighted graph H is a more complicated example of a testable parameter, which illustrates the power of Theorem 8.3. It is diﬃcult to verify directly either the deﬁnition, or say condition (iv). The theorem splits this into three: condition (i) is easy by the deﬁnition of d (G,G′); (ii) is a matter of classical combinatorics, counting mappings that split the twin classes in given proportions; ﬁnally, (iii) is trivial.


- 8.3 Dense property testing


Instead of estimating a numerical parameter, we may want to determine some property of G: Is G 3-colorable? Is it connected? Does it have a triangle? The answer will of course have some uncertainty. A precise deﬁnition was given by Rubinfeld and Sudan [101] and Goldreich, Goldwasser and Ron [56]. In the slightly diﬀerent context of “additive approximation”, closely related problems were studied by Arora, Karger and Karpinski [12] (see e.g. [45] for a survey). Many extensions deal with situations where we are allowed to sample more than a constant number of nodes of the large graph G; our concern will be the original setup, where the sample size is bounded.

A graph property P is testable, if there exists another property P′ (called a “test property”) such that

- (a) if a graph G has property P, then for all 1 ≤ k ≤ |V (G)| at least 2/3 of its k-node induced subgraphs have property P′, and
- (b) for every ε > 0 there is a kε ≥ 1 such that if G is a graph whose edit distance from P is at least ε|V (G)|2, then for all kε ≤ k ≤ |V (G)| at most a fraction of 1/3 of the k-node induced subgraphs of G have property P′.


This notion of testability is usually called oblivious testing, which refers to the fact that no information about the size of G is assumed. The constants 1/3 and 2/3 are arbitrary, and it would not change the notion of testability if we replaced them by any two real numbers 0 < a < b < 1.

It is surprising that this rather restrictive deﬁnition allows many testable graph properties: for example, bipartiteness, triangle-freeness, every property deﬁnable by a ﬁrst order formula [5].

A surprisingly general result was proved by Alon and Shapira [8]. A graph property P is called hereditary if G ∈ P implies that G′ ∈ P for every induced subgraph G′ of G.

- Theorem 8.6 (Alon–Shapira) Every hereditary graph property is testable.

Fischer and Newman [46] proved that a property is testable if and only if the normalized edit distance from the property a testable parameter. Alon at al. characterized testable graph properties in terms of Szemer´edi partitions [7].

Going to the limit gives a tool of studying testability in a “cleaner” form (Lov´asz and Szegedy [88]). It turns out that this leads to an interesting interplay between the cut-norm and the L1norm on W0.

A graph property P can be thought of as a subset of W0 (through the correspondence G  → WG), and we can consider its closure P in the metric space (W0,P). For example, the closure of the set of triangle-free graphs is the set of triangle-free graphons, which can be characterized by the property t(K3,W) = 0. More generally, let P be a hereditary graph property. Then its closure is characterized by the (inﬁnitely many) equations

![image 100](<2009-lovasz-very-large-graphs_images/imageFile100.png>)

tind(F,W) = 0 for all F ∈/ P. (38)

Closures of testable graph properties will be called testable graphon properties. These graphon properties can also be characterized in terms of a sampling method: we consider the W-random graph G(k,W) as the sample of size k from W.

- Theorem 8.7 A graphon property R is testable if and only if there is a graph property R′ such that

- (a) Pr(G(k,W) ∈ R′) ≥ 2/3 for every function W ∈ R and every k ≥ 1, and
- (b) for every ε > 0 there is a kε ≥ 1 such that Pr(G(k,W) ∈ R′) ≤ 1/3 for every k ≥ kε and


every function W ∈ W0 with d1(W,R) ≥ ε.

We quote an analytic characterization of testable graphon properties [88]. Recall that the distances d1 and d are related trivially by d ≤ d1. Testability of a property concerns an inverse relation:

- Theorem 8.8 A graphon property R is testable if and only if either one of the following conditions hold:


- (a) For every ε > 0 there is an ε′ > 0 such that if d (W,R) ≤ ε′ for some graphon W, then

d1(W,R) ≤ ε.

- (b) d1(W,R) is a continuous function of W in the cut norm.


Condition (b) can be viewed as the graphon analogue of the theorem of Fischer and Newman mentioned above (and the ﬁnite theorem can be derived from it). Condition (a) is a special case of (b).

- Example 8.9 Let R = {U}, where U ∈ W is the identically 1/2 function. Clearly this property


n− U → 0 with probability 1, but WG

is invariant under weak isomorphism. Consider the random graphs Gn = G(n,1/2); then WG

n −U 1 = 1/2 for every n. So this property is not testable by Theorem 8.8.

Let us sketch how the graphon version of Theorem 8.6 follows from this. A property R of functions W ∈ W0 is called ﬂexible if for every function U such that U(x,y) = W(x,y) for all x,y with W(x,y) ∈ {0,1}, we also have U ∈ R. First, one proves that

- Lemma 8.10 The closure of a hereditary property is ﬂexible.


Indeed, each of the equations (38) is preserved if we change the value of W at points where this value is positive.

Next, we assume that R is a closed ﬂexible property which is not testable. By Theorem 8.8, there is a sequence of functions Wn such that d (Wn,R) → 0 but d1(Wn,R) ≥ ε for some ﬁxed ε > 0. By Theorem 4.2, we may assume that Wn converges to some W ∈ R in the . norm. Let S0 = W−1(0) , S1 = W−1(1) and let Zn ∈ W0 denote the function which is 1 on S1, 0 on S0 and is identical with Wn anywhere else. By ﬂexibility, we have Zn ∈ R, and by (34),

Wn − Zn 1 =

Wn +

S0

(1 − Wn) →

S1

W +

S0

(1 − W) = 0 (n → ∞),

S1

and so d1(Wn,R) → 0, a contradiction. So it follows that the closure of every hereditary property is testable.

From this, one can derive that hereditary properties are testable. There is some further arguments needed, since a graph property can have a testable closure without itself being testable. (An example is the property that the graph is complete if the number of nodes is even but edgeless if the number of nodes is odd.) One can add further conditions that lead to a characterization, but we don’t go into these technical issues here.

- 8.4 Sparse property testing


We say that a graph property P is testable for graphs in Gd if for every ε > 0 there are integers r = r(d,ε) ≥ 1 and k = k(d,ε) such that sampling k neighborhoods of radius r from a graph G with degree bounded by d, we can compute “YES” or “NO” so that:

- (a) if we answer “NO”, then G ∈/ P;
- (b) if we answer “YES”, then we can change at most ε|V (G)| edges in G to get a graph in P. An important analogue of the result of Alon and Shapira discussed above is the following


theorem of Benjamini, Schramm and Shapira [17]. We must recall a fundamental notion from graph theory: a minor of a graph G is any other graph obtained from G by deleting edges and/or nodes, and contracting edges. A graph property is minor-closed, if it is preserved by these operations. Planarity of a graph is an example of a minor-closed property.

- Theorem 8.11 Every minor-closed property is testable for graphs with bounded degrees.


A related result was proved by Elek [38]:

- Theorem 8.12 If a graph property is preserved by edge/node deletion and disjoint union, then it is testable for graphs with bounded degrees and subexponential growth.


## 9 Extremal graph theory

- 9.1 Some classical results


In this section we describe applications of the theory of graph homomorphisms and graph limits to extremal graph theory. As an introduction, let us recall some classical results.

Deﬁne the Tur´n graph T(n,r) (1 ≤ r ≤ n) as follows: we partition [n] into r classes as equitably as possible, and connect two nodes if and only if they belong to diﬀerent classes.

- Theorem 9.1 (Tur´an’s Theorem) Among all graphs on n nodes containing no Kk, the graph T(n,k − 1) has the maximum number of edges.


Since we are interested in large n and ﬁxed k, the complication that the classes cannot be exactly equal in size (which causes the formula for the number of edges of T(n,k − 1) to be a bit ugly) should not worry us. We will be interested in the following corollary:

Corollary 9.2 If a graph on n nodes has more than k−21 k− n1 2 edges, then it contains a Kk.

![image 101](<2009-lovasz-very-large-graphs_images/imageFile101.png>)

The case k = 3 was proved by Mantel before Tur´an. We will use this case to illustrate the ideas, but the general case could be treated similarly.

One can ask for not just the existence of complete k-graphs, but for their number. Generalizing Tur´an’s Theorem, the following lower bound was proved by Goodman (for k = 3) and by Moon and Moser.

- Theorem 9.3 If a graph on n nodes has a n2 edges (0 ≤ a ≤ 1), then it contains at least a(2a − 1)...((k − 2)a − k + 1) nk complete k-graphs.

This bound is tight for Tur´an graphs, but their edge density attains only certain values of a. The best lower bound in terms of a and n is quite complicated. To illustrate these complications, we represent each graph G by the points (t(K2,G),t(K3,G) in the unit square (see Figure 2). The lower bounding curve consists of inﬁnitely many concave cubic arcs, and its validity was only recently proved by Razborov [98]. This was extended to the best lower bound on the number of K4-s by Nikiforov [95], but even the edge–Kq diagram is only conjectural [83] for q ≥ 5.

One can also ask for an upper bound on the number of complete k-graphs in a graph with given number of edges. A special case of the Kruskal–Katona Theorem answers this (the whole theorem gives the precise value, not just asymptotics, and concerns uniform hypergraphs, not just graphs).

- Theorem 9.4 If a graph on n nodes has a n2 edges (0 ≤ a ≤ 1), then it contains at most ak/2 nk complete k-graphs.


1

triangle density

edge density

0 1/2 2/3 3/4 1

Figure 2: Possible edge and triangle densities of a graph

Asymptotic equality is attained when the graph consists of a clique and isolated nodes. Not every edge density a can be realized by such graphs, but the attainable edge densities are dense in [0,1], and so Theorem 9.4 is asymptotically tight for all values of a.

Instead of counting complete graphs, we one can consider the number of copies of some other graph F in G. We have already come across counting 4-cycles twice: in Section 1.4.3 and in Section 1.5.4. Giving just the simpler asymptotic version:

- Theorem 9.5 (Erdo˝s) If a graph on n nodes has a n2 edges (0 < a ≤ 1), then it contains at least (18 + o(1))a4n4 4-cycles.

![image 102](<2009-lovasz-very-large-graphs_images/imageFile102.png>)

Graphs with asymptotic equality here are quasirandom graphs. The number of paths of length k is a more diﬃcult question, but it turns out to be equivalent

to a theorem of Blakley and Roy [18] in matrix theory. Again asymptotically,

- Theorem 9.6 If a graph on n nodes has a n2 edges (0 < a ≤ 1), then it contains at least (21 + o(1))ak−1nk paths of length k.


![image 103](<2009-lovasz-very-large-graphs_images/imageFile103.png>)

Regular graphs give asymptotic equality here.

- 9.2 Algebraic proofs of extremal graph results


The classical extremal problems in the previous section can be expressed as algebraic inequalities between the subgraph densities t(F,W) that hold for all graphons W. Often “going to the inﬁnity” provides cleaner formulations (no error terms). Here are a few examples:

- Example 9.7 (a) Tur´n’s theorem. We state just the case of triangles (due to Mantel):


t(K3,W) = 0 ⇒ t(K2,W) ≤ 1/2, (39) which follows from the algebraic inequality due to Goodman [58]:

t(K3,W) ≥ t(K2,W)(2t(K2,W) − 1). (40)

- (b) The Kruskal–Katona theorem for graphs: t(K3,W) ≤ t(K2,W)3/2. (41)
- (c) Erdo˝s’s bound on the number of quadrilaterals: t(C4,W) ≥ t(K2,W)4. (42)
- (d) The Blakley–Roy inequality: t(Pk,W) ≥ t(K2,W)k−1. (43)
- (e) The Sidorenko Conjecture (unsolved) generalizes the last two results in the direction that


for every bipartite graph F,

t(F,W) ≥ t(K2,W)|E(F)|. (44)

This conjecture is proved for trees, many small graphs, complete bipartite graphs (Sidorenko [107]) and also for cubes (Hatami [64]).

Using the formalism introduced above, the results in example 9.7 can be expressed as follows:

- (a) K3 ≥ 2K22 − K2;
- (b) K23 ≥ K32;
- (c) C4 ≥ K24; (c) P4 ≥ K23;
- (d) F ≥ K2|E(F)| (if F is bipartite).


The ﬁrst three inequalities can be proved easily using the reﬂection positivity of the graph parameters t(.,W). We will illustrate the method by deriving (a) through formal algebraic manipulations.

Proof of (a) (Goodman’s extension of the Mantel–Tur´an Theorem). Let F denote the graph K2K1 (an edge and an isolated node), and let F1, F2 and F3 be obtained from F by labeling all three nodes, one endpoint of the edge, and the isolated node, respectively. Consider the quantum graph F12 + 2(F2 − F3)2, which is obviously nonnegative. Unlabeling the nodes and deleting isolated nodes, we get K3 − 2K22 + K2, which is thus nonnegative (see Figure 3).

Of the above inequalities, also (b) and (c) can be proved by similar arguments. The BlakleyRoy inequality (c) is more diﬃcult, but some extension of this kind of argument does work [74]. Sidorenko’s conjecture (d) would of course be very nice to prove this way (or by any other means).

Using related methods, Razborov [98] solved the long-standing problem of characterizing the possible (edge-density, triangle-density) pairs, which in this setting means a description of the set (t(K2,W),t(K3,W)) : W ∈ W0) by algebraic inequalities.

The inequality in (c) also follows from reﬂection positivity if k is even. It is not known whether (c) for odd k (or perhaps every valid algebraic inequality between subgraph densities) follows

- - + 2+2

- 2

| |
|---|


# =

- - + +2 -4 +2

| |
|---|


# ≃

# + -2

Figure 3: A computation proving the Mantel-Tur´an Theorem

from a ﬁnite number of semideﬁniteness inequalities. However, every valid linear inequality between homomorphism densities follows from semideﬁniteness constraints (equivalently, from “sums of squares” computations in graph algebras), as we shall see in the next section.

- 9.3 Positivstellensatz for graphs and spectral norms


The machinery introduced in the previous sections allows us to suggest a very general approach to extremal graph theory.

We can deﬁne the following partial order on Q0: we say that a quantum graph x ≥ 0, if t(x,W) ≥ 0 for all W ∈ W0.

Let us call a quantum graph y a square-sum if there are k-labeled quantum graphs y1,...,yk

for some k such that y can be obtained from i yi2 by forgetting the labels. It is easy to see that every square-sum satisﬁes y ≥ 0.

As an example, recall the deﬁnition (18) of the “inclusion-exclusion” quantum graph F. Let us label all nodes of F, square it, and then forget the labels: we obtain F itself. This implies that F ≥ 0 for all F. In the special case when W = WG for some graph G, this also follows from our previous remark that t( F,G) is a probability, and hence nonnegative.

Is there a quantum graph x ≥ 0 which is not a square sum? I suspect that such quantum graphs exist, but it might be diﬃcult to prove this property. However, the following weaker result can be proved [91].

- Theorem 9.8 Let x be a quantum graph. Then x ≥ 0 if and only if for every ε > 0 there is a square-sum y such that N(y) ≤ N(x) and x − y 2 < ε.


The proof depends on the duality theory of semideﬁnite programs. Note that we do not claim that the k-labeled quantum graphs yi in the square-sum representation of y also have bounded N(yi); the proof gives arbitrarily large graphs if ε is small.

In analogy with the Positivstellensatz for real polynomials, we may try to represent quantum graphs x ≥ 0 as quotients of square-sums: if y and z are square-sums and y = zx + x, then x ≥ 0.

We mention a couple of related questions. For every even positive integer k, the functional t(Ck,W)1/k deﬁnes a norm on W (the Neumann-Schatten norm). This suggests the question:

For which other simple graphs F is t(F,W)1/|E(F)| a norm (or seminorm) on W? Hatami [64] proved that if a simple graph F has the property that W = t(F,|W|)1/|E(F)| is a norm, then it satisﬁes Sidorenko’s conjecture 9.7(d). He also proved that all cubes have this property.

In view of the usefulness of extending graphs to graphons, it seems natural to deﬁne graph algebras of inﬁnite linear combinations of graphs with appropriate convergence properties. It is not worked out, however, what the structure of the resulting algebra is, and how it is related to graphons.

- 9.4 The maximum distance from a hereditary graph property


A surprisingly general result is the theorem of Alon and Stav [9], proving that for every hereditary property, a random graph with appropriate density is asymptotically the farthest from the property in edit distance. The analytic results developed in this paper allow us to state and prove a simple analytic analogue of this fact, from which the original result follows along with generalizations.

- Theorem 9.9 (Alon and Stav) For every hereditary graph property P there is a number p, 0 ≤ p ≤ 1, such that for every graph G with |V (G)| = n,

d1(G,P) ≤ E(d1(G(n,p),P)) + o(1) (n → ∞). The following theorem [88] states a graphon version of this fact.

- Theorem 9.10 If R is the closure of a hereditary graph property, then the maximum of d1(.,R) is attained by a constant function.


Our point in giving this generalization is to illustrate the power of extending graph problems to a continuum. The key observation is the following, which follows from Lemma 8.10.

- Lemma 9.11 If R is the closure of a hereditary graph property, then the set W0 \ R is convex.


Hence it follows that the d1 distance from P is a concave function on W0 \ R. Since W0 \ R is obviously invariant under the group of invertible measure preserving transformations of [0,1], it is not hard to argue that there is a point (graphon) in W0 \R maximizing the distance from P which is invariant under these measure preserving transformations, and so it must be a constant function.

9.5 Which graphs are extremal? (Finitely forcible graphons)

We call a graphon W ∈ W0 ﬁnitely forcible if there exist a ﬁnite list of graphs F1,...,Fm and real numbers a1,...,am such that the equations t(F1,U) = a1,...,t(Fm,U) = am are satisﬁed by precisely those functions U ∈ W0 which arise from W by measure preserving transformations.

Let us consider a very general type of graph theoretic extremal problem: maximize t(f,W) subject to t(g1,W) = a1 t(g2,W) = a1 (45)

. t(gk,W) = a1

where f,g1,...,gk are given quantum graphs. Most of the graphon versions of extremal problems discussed so far ﬁt in this scheme.

It is easy to see that every ﬁnitely forcible graphon is the solution of an extremal problem of the type (45). We conjecture the following converse:

Conjecture 9.12 Every extremal problem has a ﬁnitely forcible optimum. In other words, if a ﬁnite set of constraints of the form t(Fi,W) = ai is satisﬁed by some graphon, then it is satisﬁed by a ﬁnitely forcible graphon.

This may seem far fetched, but the following heuristic supports it. Suppose that t(F1,W) = a1,...,t(Fk,W) = ak has a solution in W, but this is not forced by these constraints. Then there is a graph F such that t(F,W) is not determined, i.e., a = mint(F,W) < max t(F,W) = b (the max and min are taken over all solutions W of the system). Now add one of the conditions t(F,W) = a or t(F,W) = b to the system and repeat. It seems that in very few (2-3) steps we always get a unique solution, i.e., a ﬁnitely forcible graphon.

Almost all classical extremal problems have a solution that is a stepfunction. It was shown by Lov´asz and So´s [84] that every stepfunction is ﬁnitely forcible, and it was conjectured that these are the only ones. Recently B. Szegedy and Lov´asz [90] found other ﬁnitely forcible graphons, and so the problem of characterizing ﬁnitely forcible graphons is wide open.

We mention two examples of ﬁnitely forcible graphons that are not stepfunctions (the proof is not quite easy).

- Example 9.13 Let p(x,y) is a symmetric real polynomial that is monotone increasing on [0,1]2. Deﬁne

W(x,y) =

1, if p(x,y) > 0, 0, otherwise,

Then W is ﬁnitely forcible. It is conjectured that monotonicity is not needed here.

In contrast, one can show that if W(x,y) is a polynomial in x and y (not a function of the sign), then it is not ﬁnitely forcible.

- Example 9.14 Let


 

1, if the ﬁrst bit where the binary expansions of x and y diﬀer

W(x,y) =

is at an odd position, 0, otherwise,



The W is ﬁnitely forcible.

## References

- [1] R. Albert, A.-L. Baraba´si: Statistical mechanics of complex networks, Rev. Modern Phys. 74 (2002), 47–97.
- [2] D.J. Aldous: Tree-valued Markov chains and Poisson-Galton-Watson distributions, in: Microsurveys in Discrete Probability (D. Aldous and J. Propp, editors), DIMACS Ser. Discrete Math. Theoret. Comput. Sci. 41 (1998) Amer. Math. Soc., Providence, RI. (1998), 1–20.
- [3] D. Aldous, R. Lyons: Processes on Unimodular Random Networks, Electron. J. Probab. 12, Paper 54 (2007), 1454–1508.
- [4] D.J. Aldous and M. Steele: The Objective Method: Probabilistic Combinatorial Optimization and Local Weak Convergence, in: Discrete and Combinatorial Probability (H. Kesten, ed.), Springer (2003) 1–72.
- [5] N. Alon, E. Fischer, M. Krivelevich and M. Szegedy: Eﬃcient testing of large graphs, Combinatorica 20 (2000) 451–476.
- [6] N. Alon, W. Fernandez de la Vega, R. Kannan and M. Karpinski: Random sampling and approximation of MAX-CSPs, J. Comput. System Sci. 67 (2003) 212–243.
- [7] N. Alon, E. Fischer, I. Newman and A. Shapira: A Combinatorial Characterization of the Testable Graph Properties: It’s All About Regularity, Proc. of the 38th ACM Symp. Theor. of Comp. (STOC) (2006) 251–260.
- [8] N. Alon and A. Shapira: A Characterization of the (natural) Graph Properties Testable with One-Sided Error, SIAM J. Computing 37 (2008), 1703–1727.
- [9] N. Alon and U. Stav: What is the furthest graph from a hereditary property? Random Struc. Alg. 33 (2008), 87–104.
- [10] N. Alon, A. Naor: Approximating the Cut-Norm via Grothendieck’s Inequality SIAM J. Computing 35 (2006), 787-803.
- [11] O. Angel and B. Szegedy (unpublished)
- [12] S. Arora, D. Karger and M. Karpinski: Polynomial time approximation schemes for dense instances of NP-hard problems, Proc. 27-th ACM STOC (1995), 284–293.
- [13] A.-L. Barabsi: Linked: The New Science of Networks, Perseus, Cambridge, MA (2002).
- [14] I. Benjamini, L. Lov´asz: Global Information from Local Observation, Proc. 43rd Ann. Symp. on Found. of Comp. Sci. (2002), 701-710.
- [15] I. Benjamini, G. Kozma, L. Lov´asz, D. Romik, G. Tardos: Waiting for a bat to ﬂy by (in polynomial time), Combinatorics, Probability and Computing 15 (2006), 673–683.
- [16] I. Benjamini and O. Schramm: Recurrence of Distributional Limits of Finite Planar Graphs, Electronic J. Probab. 6 (2001), paper no. 23, 1–13.


- [17] I. Benjamini, O. Schramm, A. Shapira: Every Minor-Closed Property of Sparse Graphs is Testable, http://front.math.ucdavis.edu/0801.2797
- [18] G.R. Blakley and P.A. Roy: A Ho¨lder type inequality for symmetric matrices with nonnegative entries, Proc. Amer. Math. Soc. 16 (1965) 1244–1245.
- [19] B. Bollob´s: Relations between sets of complete subgraphs, in: Combinatorics, Proc. 5th British Comb. Conf. (ed. C.St.J.A. Nash-Williams, J. Sheehan), Utilitas Math. (1975), 79– 84.
- [20] B. Bollob´s: Random Graphs, Second Edition, Cambridge University Press, 2001.
- [21] B. Bollobas, C. Borgs, J. Chayes, O. Riordan: Percolation on dense graph sequences, http://arxiv.org/abs/math/0701346
- [22] B. Bollobas, S. Janson, O. Riordan: The phase transition in inhomogeneous random graphs, http://arxiv.org/abs/math/0701346
- [23] B. Bollobas, V. Nikiforov: An Abstract Regularity Lemma, http://arxiv.org/abs/0704.2450
- [24] B. Bollobas, O. Riordan: Sparse graphs: metrics and random models, http://arxiv.org/abs/0708.1919
- [25] C. Borgs, J. Chayes, J. Kahn and L. Lov´asz: Left and right convergence of graphs with bounded degree (in preparation).
- [26] C. Borgs, J. Chayes, L. Lov´asz: Moments of Two-Variable Functions and the Uniqueness of Graph Limits, http://www.cs.elte.hu/~lovasz/limitunique.pdf
- [27] C. Borgs, J. Chayes, L. Lov´asz, V.T. So´s, K. Vesztergombi: Counting graph homomorphisms, in: Topics in Discrete Mathematics (ed. M. Klazar, J. Kratochvil, M. Loebl, J. Matouˇsek, R. Thomas, P. Valtr), Springer (2006), 315–371.
- [28] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s, B. Szegedy and K. Vesztergombi: Graph Limits and Parameter Testing, Proc. 38th Annual ACM Symp. on Theory of Computing 2006, 261–270.
- [29] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s, and K. Vesztergombi: Convergent Graph Sequences I: Subgraph frequencies, metric properties, and testing, Advances in Math. (2008), 10.1016/j.aim.2008.07.008.
- [30] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s, and K. Vesztergombi: Convergent Graph Sequences II: Multiway Cuts and Statistical Physics (submitted), http://www.cs.elte.hu/~lovasz/ConvRight.pdf


- [31] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s, and K. Vesztergombi: Limits of randomly grown graph sequences (manuscript).
- [32] M.-D. Choi: Tricks or Treats with the Hilbert Matrix, Amer. Math. Monthly 90 (1983), 301–312.
- [33] F. Chung, R.L. Graham and R.M. Wilson: Quasi-random graphs, Combinatorica 9 (1989), 345–362.
- [34] F. Chung, R.L. Graham: Quasi-Random Hypergraphs, Proc. Nat. AcadSci.˙ 86 (1989), pp. 8175–8177.
- [35] P. Diaconis and S. Janson: Graph limits and exchangeable random graphs, http://eprintweb.org/S/authors/math/ja/Janson/3
- [36] L. Devroye: Branching processes and their applications in the analysis of tree structures and tree algorithms”, in: Probabilistic Methods for Algorithmic Discrete Mathematics, ed. M. Habib, C. McDiarmid, J. Ramirez-Alfonsin and B. Reed, pp. 249-314, Springer-Verlag, Berlin, 1998.
- [37] G. Elek: On limits of ﬁnite graphs, Combinatorica 27 (2007), 503–507.
- [38] G. Elek: A Regularity Lemma for Bounded Degree Graphs and Its Applications: Parameter Testing and Inﬁnite Volume Limits, http://arxiv.org/abs/0711.2800
- [39] G. Elek: The Strong Approximation Conjecture holds for amenable groups, http://arxiv.org/abs/math/0511655.
- [40] G. Elek: The combinatorial cost, http://arxiv.org/PS_cache/math/pdf/0608/0608474v1.pdf
- [41] G. Elek and G. Lippner: An analogue of the Szemeredi Regularity Lemma for bounded degree graphs, http://arxiv.org/abs/0809.2879
- [42] G. Elek, B. Szegedy: Limits of Hypergraphs, Removal and Regularity Lemmas. A Nonstandard Approach, http://arxiv.org/0705.2179
- [43] P. Erdo¨s, L. Lov´asz, J. Spencer: Strong independence of graphcopy functions, in: Graph Theory and Related Topics, Academic Press, 165-172.
- [44] P. Erdo¨s, A. R´enyi: On random graphs I, Publ. Math. Debrecen 6 (1959), 290–297.


- [45] E. Fischer: The art of uninformed decisions: A primer to property testing, The Computational Complexity Column of the Bulletin of the European Association for Theoretical Computer Science 75 (2001), 97-126.
- [46] E. Fischer, I. Newman: Testing versus Estimation of Graph Properties, Proc. 37-th ACM STOC (2005), 138–146.
- [47] D.C. Fisher: Lower bounds on the number of triangles in a graph, J. Graph Theory 13

- (1989), 505–512.

[48] D.C. Fisher and J. Ryan: Conjectures on the number of complete subgraphs, in: Proc. of the 20-th Southeastern Conf. on Comb., Graph Theory, and Computing, Congr. Numer. 70

- (1990), 217–219.


- [49] D.C. Fisher and A. Solow: Dependence polynomials, Discrete Math. 82 (1990), 251–258.
- [50] P. Frankl and J. Pach: An extremal problem on Kr-free graphs, J. Graph Theory 12 (1988), 519–523.
- [51] M. Freedman, L. Lov´asz, A. Schrijver: Reﬂection positivity, rank connectivity, and homomorphisms of graphs, J. Amer. Math. Soc. 20 (2007), 37–51.
- [52] A. Frieze and R. Kannan: Quick approximation to matrices and applications, Combinatorica 19, 175–220.
- [53] D. Gaboriau: Invariants l2 de relations dequivalence et de groupes, Publ. Math. Inst. Hautes. Etudes` Sci. 95 (2002), 93–150.
- [54] S. Gerke, A. Steger: The sparse regularity lemma and its applications, Surveys in Combinatorics (2005), 227–258.
- [55] E.N. Gilbert: Random graphs, Ann. Math. Stat. 30 (1959), 1141-1144.
- [56] O. Goldreich, S. Goldwasser and D. Ron: Property testing and its connection to learning and approximation, J. ACM 45 (1998), 653–750.
- [57] O. Goldreich and L. Trevisan: Three theorems regarding testing graph properties, Random Structures and Algorithms, 23 (2003), 23–57.
- [58] A.W. Goodman: On sets of aquaintences and strangers at any party, Amer. Math. Monthly 66 (1959) 778–783.
- [59] W.T. Gowers: Lower bounds of tower type for Szemer´edi’s Uniformity Lemma, Geom. Func. Anal. 7 (1997), 322–337.
- [60] W.T. Gowers: Quasirandomness, counting and regularity for 3-uniform hypergraphs, Combin. Probab. Comput. 15 (2006), 143–184.
- [61] W.T. Gowers: Hypergraph regularity and the multidimensional Szemeredi theorem, Annals of Math. 166 (2007), 897–946.


- [62] M. Gromov: Metric structures for Riemannian and non-Riemannian spaces, Birkh¨auser

(1999).

- [63] E. Gy¨ori, J. Pach, M. Simonovits: On the maximal number of certain subgraphs in Kr-free graphs, Graphs and Combin. 7 (1991), 31–37.
- [64] H. Hatami: Graph norms and Sidorenko’s conjecture, http://arxiv.org/abs/0806.0047
- [65] J. Haviland, A. Thomason: Pseudo-random hypergraphs. Graph theory and combinatorics (Cambridge, 1988). Discrete Math. 75 (1989), 255–278.
- [66] J. Haviland, A. Thomason: On testing the ”pseudo-randomness” of a hypergraph. Discrete Math. 103 (1992), 321–327.
- [67] P. Hell and J. Neˇsetˇril: Graphs and Homomorphisms, Oxford University Press, 2004.
- [68] S. Janson, T. Luczak and A. Ruczynski: Random Graphs, Wiley, 2000.
- [69] A. Kechris and B.D. Miller: Topics in orbit equivalence theory, Lecture Notes in Mathematics 1852. Springer-Verlag, Berlin, 2004.
- [70] J. Kock: Frobenius Algebras and 2D Topological Quantum Field Theories, London Math. Soc. student texts, Cambridge University Press (2003).
- [71] Y. Kohayakawa: Szemer´edi’s regularity lemma for sparse graphs, in: Sel. Papers Conf. Found. of Comp. Math., Springer (1997), 216–230.
- [72] Y. Kohayakawa, V. Ro¨dl: Szemerdi’s´ regularity lemma and quasi-randomness, in: Recent Advances in Algorithms and Combinatorics, CMS Books Math./Ouvrages Math. SMC 11, Springer, New York (2003), 289–351.
- [73] J. Koml´os and M. Simonovits: Szemer´edi’s Regularity Lemma and its applications in graph theory, in: Combinatorics, Paul Erdos is Eighty (D. Miklos et. al, eds.), Bolyai Society Mathematical Studies 2 (1996), pp. 295–352.
- [74] G. Kun (personal communication).
- [75] L. Lov´asz: Operations with structures, Acta Math. Hung. 18, 321-328.
- [76] L. Lov´asz: Direct product in locally ﬁnite categories, Acta Sci. Math. Szeged 23, 319-322.
- [77] L. Lov´asz: Connection matrices, in: Combinatorics, Complexity and Chance, A Tribute to Dominic Welsh Oxford Univ. Press (2007), 179–190.
- [78] L. Lov´asz: The rank of connection matrices and the dimension of graph algebras, Eur. J. Comb. 27 (2006), 962–970.


- [79] L. Lov´asz: Discrete Analytic Functions: An Exposition, in: Surveys in Diﬀerential Geometry IX, Eigenvalues of Laplacians and other geometric operators (Ed. Grigor’yan A., Yau S.-T.), Int. Press, Somerville, MA (2004), 241–273.
- [80] L. Lov´asz, A. Schrijver: Graph parameters and semigroup functions, European Journal of Combinatorics (2007), doi:10.1016/j.ejc.2007.11.008
- [81] L. Lov´asz, A. Schrijver: Dual graph homomorphisms (manuscript)
- [82] L. Lov´asz, A. Schrijver: Semideﬁnite functions on categories (manuscript)
- [83] L. Lov´asz, M. Simonovits: On the number of complete subgraphs of a graph II, in: Studies in Pure Math., To the memory of P. Tur´an (ed. P. Erdo¨s), Akad´emiai Kiado´, 459-495.
- [84] L. Lov´asz, V.T. So´s: Generalized quasirandom graphs, J. Comb. Th. B 98 (2008), 146–163.
- [85] L. Lov´asz, B. Szegedy: Limits of dense graph sequences, J. Comb. Theory B 96 (2006), 933–957.
- [86] L. Lov´asz, B. Szegedy: Contractors and connectors in graph algebras, J. Comb. Th. B (to appear), http://arxiv.org/abs/math/0505162
- [87] L. Lov´asz and B. Szegedy: Szemer´edi’s Lemma for the analyst, Geom. Func. Anal. 17

(2007), 252–270.

- [88] L. Lov´asz, B. Szegedy: Testing properties of graphs and functions, to appear in Isr. J. Math, ftp://ftp.research.microsoft.com/pub/tr/TR-2005-110.pdf
- [89] L. Lov´asz and B. Szegedy: The moment problem for 2-variable functions and reﬂection positive graph parameters (manuscript) http://www.cs.elte.hu/~lovasz/moment.pdf
- [90] L. Lov´asz and B. Szegedy: Finitely forcible graphons (manuscript) http://arxiv.org/abs/0901.0929
- [91] L. Lov´asz and B. Szegedy: Random Graphons and a Weak Positivstellensatz for Graphs (manuscript)
- [92] R. Lyons: Asymptotic enumeration of spanning trees Combin. Prob. Comput. 14 (2005) 491–522.
- [93] J. Matouˇsek: Using the Borsuk-Ulam Theorem: Lectures on Topological Methods in Combinatorics and Geometry Springer, 2003.
- [94] J.W. Moon, L. Moser: Mat. Kut. Int. K¨ozl. 7 (1962), 283–286.
- [95] V. Nikiforov: The number of cliques in graphs of given order and size, http://arxiv.org/abs/0710.2305


- [96] O. Pikhurko: An Analytic Approach to Stability, http://arxiv.org/abs/0812.0214
- [97] A. Pultr: Isomorphism types of objects in categories determined by numbers of morphisms, Acta Sci. Math. Szeged 35 (1973), 155–160.
- [98] A.A. Razborov: Flag Algebras, Journal of Symbolic Logic, 72 (2007), 1239–1282.
- [99] A.A. Razborov: On the minimal density of triangles in graphs, Combinatorics, Probability and Computing (to appear).
- [100] V. Ro¨dl, J. Skokan: Regularity lemma for k-uniform hypergraphs, Random Structures Algorithms 25 (2004), 1–42.
- [101] R. Rubinfeld and M. Sudan: Robust characterization of polynomials with applications to program testing, SIAM J. on Computing 25 (1996), 252–271.
- [102] O. Schramm: Hyperﬁnite graph limits, http://arxiv.org/PS_cache/arxiv/pdf/0711/0711.3808v1.pdf
- [103] A. Schrijver: Graph invariants in the edge model, in: Building Bridges—Between Mathematics and Computer Science (M. Gr¨otschel, G.O.H. Katona, eds.), Springer, Berlin, 2008, pp. 487–498.
- [104] A. Schrijver, Polynomial and tensor invariants and combinatorial parameters, http://homepages.cwi.nl/~lex/files/tensorc_long.pdf
- [105] A. Schrijver, Tensor subalgebras and ﬁrst fundamental theorems in invariant theory, Journal of Algebra 319 (2008) 1305–1319.
- [106] A. Schrijver, Graph invariants in the spin model, http://homepages.cwi.nl/~lex/files/grvm.pdf
- [107] A. Sidorenko: A correlation inequality for bipartite graphs, Graphs and Combin. 9 (1993), 201–204.
- [108] M. Simonovits, V.T. So´s: Hereditary extended properties, quasi-random graphs and induced subgraphs, Combinatorics, Probability and Computing 12 (2003), 319–344.
- [109] M. Simonovits, V.T. So´s: Hereditarily extended properties, quasi-random graphs and not necessarily induced subgraphs. Combinatorica 17 (1997), 577–596.
- [110] B. Szegedy: Edge coloring models and reﬂection positivity, J. Amer. Math. Soc. 20 (2007), 969–988.
- [111] B. Szegedy (private communication).
- [112] E. Szemer´edi: On sets of integers containing no k elements in arithmetic progression”, Acta Arithmetica 27 (1975) 199-245.


- [113] E. Szemer´edi: Regular partitions of graphs, Colloque Inter. CNRS (J.-C. Bermond, J.C. Fournier, M. Las Vergnas and D. Sotteau, eds.) (1978) 399–401.
- [114] T. Tao: A variant of the hypergraph removal lemma, J. of Comb. Theory, Series A 113, 1257–1280.
- [115] T.C. Tao: Szemer´edis regularity lemma revisited, Contrib. Discrete Math. 1 (2006), 8–28.
- [116] T.C. Tao: The dichotomy between structure and randomness, arithmetic progressions, and the primes, in: Proc. Intern. Congress of Math. I, Eur. Math. Soc., Zrich, 2006.
- [117] A. Thomason: Pseudorandom graphs, in: Random graphs ’85 North-Holland Math. Stud. 144, North-Holland, Amsterdam, 1987, 307–331.
- [118] W.T. Tutte: On the Birkhoﬀ-Lewis equations, Discrete Math. 92 (1991), 417–425.
- [119] W.T. Tutte: On the matrix of chromatic joins, J. Comb. Theory B 57 (1993), 269–288.
- [120] H. Whitney: The coloring of graphs, Ann. of Math. 33 (1932), 688-718.


