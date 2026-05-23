# Limits of local algorithms over sparse random graphs

### David Gamarnik∗ Madhu Sudan†

arXiv:1304.1831v1[math.PR]5Apr2013

Abstract

Local algorithms on graphs are algorithms that run in parallel on the nodes of a graph to compute some global structural feature of the graph. Such algorithms use only local information available at nodes to determine local aspects of the global structure, while also potentially using some randomness. Recent research has shown that such algorithms show signiﬁcant promise in computing structures like large independent sets in graphs locally. Indeed the promise led to a conjecture by Hatami, Lov´asz and Szegedy [HLS] that local algorithms may be able to compute maximum independent sets in (sparse) random dregular graphs. In this paper we refute this conjecture and show that every independent set produced by local algorithms is multiplicative factor 1/2 + 1/(2√2) smaller than the largest, asymptotically as d → ∞.

![image 1](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile1.png>)

Our result is based on an important clustering phenomena predicted ﬁrst in the literature on spin glasses, and recently proved rigorously for a variety of constraint satisfaction problems on random graphs. Such properties suggest that the geometry of the solution space can be quite intricate. The speciﬁc clustering property, that we prove and apply in this paper shows that typically every two large independent sets in a random graph either have a signiﬁcant intersection, or have a nearly empty intersection. As a result, large independent sets are clustered according to the proximity to each other. While the clustering property was postulated earlier as an obstruction for the success of local algorithms, such as for example, the Belief Propagation algorithm, our result is the ﬁrst one where the clustering property is used to formally prove limits on local algorithms.

## 1 Introduction

Local algorithms are decentralized algorithms that run in parallel on nodes in a network using only information available from local neighborhoods to compute some global function of data that is spread over the network. Local algorithms have been studied in the past in various communities. They arise as natural solution concepts in distributed computing (see, e.g., [Lin92]). They also lead to eﬃcient sub-linear algorithms — algorithms that run in time signiﬁcantly less than the length of the input — and [PR07, NO08, HKNO09, RTVX11] illustrate some of the progress in this direction. Finally local algorithms have also been proposed as natural heuristics for solving hard optimization problems with the popular Belief Propagation algorithm (see for instance [WJ05, MM09]) being one such example.

![image 2](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile2.png>)

∗MIT; e-mail: gamarnik@mit.edu.Research supported by the NSF grants CMMI-1031332. †Microsoft Research New England; e-mail: madhu@mit.edu

In this work we study the performance of a natural class of local algorithms on random regular graphs and show limits on the performance of these algorithms. The motivation for our work comes from the a notion of local algorithms that has appeared in a completely diﬀerent mathematical context, namely that of the theory of graph limits, developed in several papers, including [BCL+08],[BCL+12],[LS06],[BCLK],[BCG13],[EL10], [HLS]. In the realms of this theory it was conjectured that every “reasonable” combinatorial optimization problem on random graphs can be solved by means of some local algorithms. To the best of our knowledge this conjecture for the ﬁrst time was formally stated in Hatami, Lova´sz and Szegedy in [HLS], and thus, from now on, we will refer to it as Hatami-Lova´sz-Szegedy (or HLS) conjecture, though informally it was posed by Szegedy earlier, and was referenced in several papers, including Lyons and Nazarov [LN11], and Cs´oka and Lippner [CL12]. In a concrete context of the problem of ﬁnding largest independent sets in sparse random regular graphs, the conjecture is stated as follows. Let Td,r be a rooted d-regular tree with depth r. Namely, every node including the root, has degree r, except for the leaves, and the distance from the root to every leaf is r. Consider a function fr : [0, 1]Td,r

→ {0, 1} which maps every such tree whose nodes are decorated with real values from [0, 1] to a ”decision” encoded by 0 and 1. In light of the fact that in a random d-regular graph Gd(r) the typical node has depth-r neighborhood isomorphic to Td,r, for any constant r, such a function fr can be used to generate (random) subsets I of Gd(r) as follows: decorate nodes of Gd(r) using i.i.d. uniform random values from [0, 1] and apply function fr in every node. The set of nodes for which fr produces value 1 deﬁnes I, and is called ”i.i.d. factor”. It is clear that fr essentially describes a local algorithm for producing sets I (sweeping issue of computability of fr under the rug). The HLS conjecture postulates the existence of a sequence of fr, r = 1, 2, . . ., such that the set I thus produced is an independent subset of Gd(r) and asymptotically achieves the largest possible value as r → ∞. Namely, largest independent subsets of random regular graphs are i.i.d. factors. The precise connection between this conjecture and the theory of graph limits is beyond the scope of this paper. Instead we refer the reader to the relevant papers [HLS],[EL10]. The concept of i.i.d. factors appears also in one of the open problem by David Aldous [Ald] in the context of coding invariant processes on inﬁnite trees.

It turns out that an analogue for the HLS conjecture is indeed valid for another important combinatorial optimization problem - matching. Lyons and Nazarov [LN11] established it for the case of bi-partite locally Td,r-tree-like graphs, and Cs´oka and Lippner established this result for general locally Td,r-tree-like graphs. Further, one can modify the framework of i.i.d. factors by encapsulating non-Td,r type neighborhoods, for example by making fr depend not only on the realization of random uniform in [0, 1] values, but also on the realization of the graph-theoretic neighborhoods around the nodes. Some probabilistic bound on a degree might be needed to make this deﬁnition rigorous (though we will not attempt this formalization in this paper). In this case one can consider, for example, i.i.d. factors when neighborhoods are distributed as r generations of a branching process with Poisson distribution, and then ask which combinatorial optimization problems deﬁned now on sparse Erd¨os-R´enyi graphs G(n, d/n) can be solved as i.i.d. factors. Here G(n, d/n) is a random graph on n nodes with each of the n2 edges selected with probability d/n, independently for all edges, and d > 0 is a ﬁxed constant. In this case it is possible to show that when c ≤ e, the maximum independent set problem on G(n, d/n) can be solved nearly optimally by the well known Belief Propagation (BP) algorithm with constantly many rounds. Since the BP is a local algorithm, then the maximum independent set on G(n, d/n) is an i.i.d. factor, in the extended framework deﬁned above. (We should note that the original proof of Karp

and Sipser [KS81] of the very similar result, relied on a diﬀerent method.) Thus, the framework of local algorithms viewed as i.i.d. factors is rich enough to solve several interesting combinatorial optimization problems.

Nevertheless, in this paper we refute the HLS conjecture in the context of maximum independent set problem on random regular graphs Gd(n). Speciﬁcally, we show that for large enough d, with high probability as n → ∞, every independent set producible as an i.i.d. factor is a multiplicative factor γ < 1 smaller than the largest independent subset of Gd(n). We establish that γ is asymptotically at most 21 + 2√12 (though we conjecture that the result holds simply for γ = 1/2, as we discuss in the body of the paper).

![image 3](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile3.png>)

![image 4](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile4.png>)

![image 5](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile5.png>)

Our result is based on a powerful, though fairly simple to establish in our case, so-called clustering or shattering property of some combinatorial optimization problem on random graphs, ﬁrst conjectured in the theory of spin glasses and later conﬁrmed by rigorous means. For the ﬁrst time this clustering property was discussed in terms of so-called overlap structure of the solutions of the Sherrington-Kirkpatrick model [Tal10]. Later, it featured in the context of random K-SAT problem and was proved rigorously by Achlioptas, Coja-Oghlan and Ricci-Tersenghi [ACORT11], and by Mezard, Mora and Zecchina [MMZ05], independently. We do not deﬁne the random KSAT problem here and instead refer the reader to the aforementioned papers. What these results state is that in certain regimes, the set of satisfying assignments, with high probability, can be clustered into groups such that two solutions within the same cluster agree on a certain minimum number of variables, while two solutions from diﬀerent clusters have to disagree on a certain minimum number of variables. In particular, one can identify a certain non-empty interval [z1, z2] ⊂ [0, 1] such that no two solutions of the random K-SAT problem agree on precisely z fraction of variables for all z ∈ [z1, z2]. One can further show that the onset of clustering property occurs when the density of clauses to variables becomes at least 2K/K, while at the same time the formula remains satisﬁable with high probability, when the density is below

- 2K log 2. Interestingly, the known algorithms for ﬁnding solutions of random instances of KSAT problem also stop working around the 2K/K threshold. It was widely conjectured that the onset of the clustering phase is the main obstruction for ﬁnding such algorithms. In fact, Coja Oghlan [CO11] showed that the BP algorithm, which was earlier conjectured to be a good contender for solving the random instances of K-SAT problems, also fails when the density of clauses to variables is at least 2K log K/K, though Coja-Oghlan’s approach does not explicitly rely on the clustering property, and one could argue that the connection between the clustering property and the failure of the BP algorithm is coincidental.


Closer to the topic of this paper, the clustering property was also recently established for independent sets in Erd¨os-R´enyi graphs. In particular Coja-Oghlan and Efthymiou [COE11] established the following result. It is known that the largest independent subset of G(n, d/n) has size approximately (2 logd/d)n, when d is large, see the next section for precise details. The authors of [COE11] show that the set of independent sets of size at least approximately (log d/d)n (namely those within factor 1/2 of the optimal), are also clustered. Namely, one can split them into groups such that intersection of two independent sets within a group has a large cardinality, while intersection of two independent sets from diﬀerent groups has a small cardinality. One should note that algorithms for producing large independent subsets of random graphs also stop short factor 1/2 of the optimal, both in the case of sparse and in the dense random graph cases, as exhibited by the well-known Karp’s open problem regarding independent subsets of G(n, 1/2) [AS92].

This is almost the result we need for our analysis with two exceptions. First, we need to establish this clustering property for random regular as opposed Erd¨os-R´enyi graphs. Second, the result in [COE11] applies to typical independent sets and does not rule out the possibility that there are two independent sets with some ”intermediate” intersection cardinality, though the number of such pairs is insigniﬁcant compared to the total number of independent sets. For our result we need to show that, without exception, every pair of ”large” independent sets has either large or small intersection. We indeed establish this, but at the cost of loosing additional factor 1/(2√2). In particular, we show that for large enough d, with high probability as n → ∞, every two independent subsets of Gd(n) with cardinality asymptotically (1+β)(log d/d)n, where

![image 6](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile6.png>)

- 1 ≥ β > 21+2√12 either have intersection size at least (1+z)(log d/d)n or at most (1−z)(log d/d)n, for some z < β. The result is established using a straightforward ﬁrst moment argument: we compute the expected number of pairs of independent sets with intersection lying in the interval [(1 − z)(log d/d)n, (1 + z)(log d/d)n], and show that this expectation converges to zero exponentially fast.

![image 7](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile7.png>)

![image 8](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile8.png>)

![image 9](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile9.png>)

With this result at hand, the refutation of the HLS conjecture is fairly simple to derive. We prove that if local algorithms can construct independent sets of size asymptotically (1 + β)(log d/d)n, then, by means of a simple coupling construction, we can construct two independent sets with intersection size z for all z in the interval [(1+β)2(log d/d)2n, (1+β)(log d/d)n], clearly violating the clustering property. The additional factor 1/(2√2) is an artifact of the analysis, and hence we believe that our result holds for all β ∈ (0, 1]. Namely, no local algorithm is capable of producing independent sets with size larger than factor 1/2 of the optimal, asymptotically in d. We note again that this coincides with the barrier for known algorithms. It is noteworthy that our result is the ﬁrst one where algorithmic hardness derivation relies directly on the the geometry of the solution space, vis-a-vis the clustering phenomena, and thus the connection between algorithmic hardness and clustering property is not coincidental.

![image 10](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile10.png>)

The remainder of the paper is structured as follows. We introduce some basic material and the HLS conjecture in the next section. In the same section we state our main theorem non-validity of the conjecture (Theorem 2.5). We also state two secondary theorems, the ﬁrst describing the overlap structure of independent sets in random graphs (Theorem 2.6) - the main tool in the proof of our result, and the second describing overlaps that can be found if local algorithms work well (Theorem 2.7). We prove our main theorem easily from the two secondary theorems in Section 3. We prove Theorem 2.7 in Section 4. Sections 5 and 6 are devoted to proofs of the theorem regarding the overlap property, for the case of Erd¨os-R´enyi and random regular graph, respectively. While technically we do not need such a result for the Erd¨os-R´enyi graph, it is very simple to derive and provides the roadmap for the case of the regular graphs (where the calculations are a bit more tedious). The Erd¨os-R´enyi case might also be useful for further studies of i.i.d. factors on Erd¨os-R´enyi graphs as opposed to random regular graphs, in the framework described above.

- 2 Preliminaries and main result


For convenience, we repeat here some of the notions and deﬁnitions already introduced in the ﬁrst section.

Basic graph terminology All graphs in this paper are understood to be simple undirected graphs. Given a graph G with node set V (G) and edge set E(G), a subset of nodes I ⊂ V (G) is an independent set if (u, v) ∈/ E(G) for all u, v ∈ I. A path between nodes u and v with length r is a sequence of nodes u1, . . ., ur−1 such that (u, u1), (u1, u2), . . ., (ur−1, v) ∈ E(G). The distance between nodes u and v is the length of the shortest path between them. For every positive integer value r and every node u ∈ V (G), BG(u, r) denotes the depth-r neighborhood of u in G. Namely, BG(u, r) is the subgraph of G induced by nodes v with distance at most r from u. When G is clear from context we drop the subscript. The degree of a vertex u ∈ V (G) is the number of vertices v such that (u, v) ∈ E(G). The degree of a graph G is the maximum degree of a vertex of G. A graph G is d-regular if the degree of every node is d.

Random graph preliminaries Given a positive real d, G(n, d/n) denotes the Erd¨os-R´enyi graph on n nodes {1, 2, . . ., n} [n], with edge probability d/n. Namely each of the n2 edges of a complete graph on n nodes belongs to E(G(n, d/n)) with probability d/n, independently for all edges. Given a positive integer d, Gd(n) denotes a graph chosen uniformly at random from the space of all d-regular graphs on n nodes. This deﬁnition is meaningful only when nd is an even number, which we assume from now on. Given a positive integer m, let I(n, d, m) denote the set of all independent sets in G(n, d/n) with cardinality m. Id(n, m) stands for a similar set for the case of random regular graphs. Given integers 0 ≤ k ≤ m, let O(n, d, m, k) denote the set of pairs I, J ∈ I(n, d, m) such that |I ∩ J| = k. The deﬁnition of the set Od(n, m, k) is similar. The sizes of the sets O(n, d, m, k) and Od(n, m, k), and in particular whether these sets are empty or not, is one of our focuses.

Denote by α(n, d) the size of a largest in cardinality independent subset of G(n, d/n), normalized by n. Namely,

α(n, d) = n−1 max{m : I(n, d, m) = ∅}.

αd(n) stands for the similar quantity for random regular graphs. It is known that α(n, d) and αd(n) have deterministic limits as n → ∞.

Theorem 2.1. For every d ∈ R+ there exists α(d) such that w.h.p. as n → ∞,

α(n, d) → α(d). (1) Similarly, for every positive integer d there exists αd such that w.h.p. as n → ∞

αd(n) → αd. (2) Furthermore

as d → ∞.

2 log d d

(1 − o(1)), (3)

α(d) =

![image 11](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile11.png>)

2 log d d

(1 − o(1)), (4)

αd =

![image 12](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile12.png>)

The convergence (1) and (2) was established in Bayati, Gamarnik and Tetali [BGT10]. The limits (3) and (4) follow from much older results by Frieze [Fri90] for the case of Erd¨os-R´enyi graphs and by Frieze and  Luczak [F L92] for the case of random regular graphs, which established these limits in the limsupn and liminfn sense. The fallout of these results is that graphs G(n, d/n) and Gd(n) have independent sets of size up to approximately (2 log d/d)n, when n and d are large, namely in the doubly asymptotic sense when we ﬁrst take n to inﬁnity and then d to inﬁnity.

Local graph terminology A decision function is a measurable function f = f(u, G, x) where G is a graph on vertex set [n] for some positive integer n, u ∈ [n] is a vertex and x ∈ [0, 1]N is a sequence of real numbers for some N ≥ n and returns a Boolean value {0, 1}. A decision function f is said to compute an independent set if for every graph G and every sequence x and for every pair (u, v) ∈ E(G) it is the case that either f(u, G, x) = 0 or f(v, G, x) = 0, or both. We refer to such an f as an independence function. For an independence function f, graph G on vertex set [n] and x ∈ [0, 1]N for N ≥ n, we let IG(f, x) denote the independent set of G returned by f, i.e., IG(f, x) = {u ∈ [n] | f(u, G, x) = 1}. We will assume later that X is chosen randomly according to some probability distribution. In this case IG(f, x) is a randomly chosen independent set in G.

We now deﬁne the notion of a “local” decision function, i.e., one whose actions depend only on the local structure of a graph and the local randomness. The deﬁnition is a natural one, but we formalize it below for completeness. Let G1 and G2 be graphs on vertex sets [n1] and [n2] respectively. Let u1 ∈ [n1] and u2 ∈ [n2]. We say that π : [n1] → [n2] is an r-local isomorphism mapping u1 to u2 if π is a graph isomorphism from BG

(u2, r) (so in particular it is a bijection from BG

(u1, r) to BG

1

2

(u1, r) and BG

(u1, r) to BG

(u2, r), and further it preserves adjacency within BG

1

2

1

(u2, r)). For G1, G2, u1, u2 and an r-local isomorphism π, we say sequences x(1) ∈ [0, 1]N

1

2

(u1, r) we have x(1)v = x(2)π(v). Finally we say f(u, G, x) is an r-local function if for every pair of graphs G1, G2, for every pair of vertices u1 ∈ V (G1) and u2 ∈ V (G2), for every r-local isomorphism π mapping u1 to u2 and r-locally equivalent sequences x(1) and x(2) we have f(u1, G1, x(1)) = f(u2, G2, x(2)). We often use the notation fr to denote an r-local function.

and x(2) ∈ [0, 1]N

are r-locally equivalent if for every v ∈ BG

2

1

Let nd,r 1 + d · ((d − 1)r − 1)/(d − 2) denote the number of vertices in a rooted tree of degree d and depth r. We let Td,r denote a canonical rooted tree on vertex set [nd,r] with root being 1. For n ≥ nd,r, x ∈ [0, 1]n and an r-local function fr, we let fr(x) denote the quantity fr(1, Td,r, x). Let X be chosen according to a uniform distribution on [0, 1]n. The set subset of nodes IG

d(n)(fr, X) is called i.i.d. factor produced by the r-local function fr. As we will see below

the α(fr) n 1 · EX[fr(X)] accurately captures (to within an additive o(1) factor) the density of an independent returned by an r-local independence function fr on Gd(n).

![image 13](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile13.png>)

First we recall the following folklore proposition which we will also use often in this paper.

- Proposition 2.2. As n → ∞, with probability tending to 1 almost all local neighborhoods in Gd(n) look like a tree. Formally, for every d, r and ǫ, for suﬃciently large n,


d(n)(u, r) ∼= Td,r}| ≥ ǫn ≤ ǫ. This immediately implies that the expected value of the independent set IG

d(n) |{u ∈ [n] | BG

PG

d(n)(fr, X) produced by fr is α(fr)n + o(n). In fact the following concentration result holds.

- Proposition 2.3. As n → ∞, with probability tending to 1 the independent set produced by a


r-local function f on Gd(n) is of size α(f)·n+o(n). Formally, for every d, r, ǫ and every r-local function f, for suﬃciently large n,

d(n)(fr, X)| − α(fr)n| ≥ ǫn ≤ ǫ. Proof. The proof follows from by the fact that the variance of |IG

d(n),X∈[0,1]N ||IG

PG

d(n),X| is O(n) and its expectation is α(fr)n + o(n), and so the concentration follows by Chebychev’s inequality. The bound on the variance in turn follows from the fact that for every graph G, there are at most O(n) pairs of vertices u and v for which the events f(u, G, X) and f(v, G, X) are not independent for random X. Details omitted.

![image 14](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile14.png>)

![image 15](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile15.png>)

![image 16](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile16.png>)

![image 17](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile17.png>)

The Hatami-Lov´asz-Szegedy Conjecture and our result We now turn to describing the Hatami-Lova´sz-Szegedy (HLS) conjecture and our result. Recall αd deﬁned by (2). The HLS conjecture can be stated as follows.

Conjecture 2.4. There exists a sequence of r-local independence functions fr, r ≥ 1 such that almost surely I(fr, n) is an independent set in Gd(n) and α(fr) → αd as r → ∞.

Namely, the conjecture asserts the existence of a local algorithm (r-local independence function fr) which is capable of producing independent sets in Gd(r) of cardinality close to the largest that exist. For such an algorithm to be eﬃcient the function fr(u, G, x) should also be eﬃciently computable uniformly. Even setting this issue aside, we show that there is a limit on the power of local algorithms to ﬁnd large independent sets in Gd(n) and in particular the HLS conjecture does not hold. Let αˆd = supr supf

α(fr), where the second supremum is taken over all r-local independence functions fr.

r

- Theorem 2.5. [Main] For every ǫ > 0 and all suﬃciently large d,


αˆd αd ≤

- 1

![image 18](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile18.png>)

- 2


![image 19](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile19.png>)

- 1

![image 20](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile20.png>)

- 2√2


+

+ ǫ.

![image 21](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile21.png>)

That is, for every ǫ > 0 and for all suﬃciently large d, a largest independent set obtainable by r-local functions is at most 21 + 2√12 + ǫ for all r.

![image 22](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile22.png>)

![image 23](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile23.png>)

![image 24](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile24.png>)

Thus for all large enough d there is a multiplicative gap between αˆd and the independence ratio αd. That being said, our result does not rule out that for small d, αˆd in fact equals αd, thus leaving the HLS conjecture open in this regime.

The two main ingredients in our proof of Theorem 2.5 both deal with the overlaps between independent sets in random regular graphs. Informally, our ﬁrst result on the size of the overlaps shows that in random graphs the overlaps are not of “intermediate” size — this is formalized in Theorem 2.6. We then show that we can apply any r-local function fr twice, with coupled randomness, to produce two independent sets of intermediate overlap where the size of the overlap depends on the size of the independent sets found by fr and the level of coupling. This is formalized in Theorem 2.7 Theorem 2.5 follows immediately by combinig the two theorems (and appropriate setting of parameters).

Overlaps in random graphs We now state our main theorem about the overlap of large independent sets. We interpret the statement after we make the formal statement.

- Theorem 2.6. For β ∈ (1/√2, 1) and 0 < z < 2β2 − 1 < β and d, let s = (1+β)d−1 log d and


![image 25](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile25.png>)

![image 26](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile26.png>)

let K(z) denote the set of integers between (1−z)dnlogd and (1+z)dnlogd. Then, for all large enough d, we have

![image 27](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile27.png>)

![image 28](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile28.png>)

P ∪k∈K(z) O(n, d, ⌊sn⌋, k) = ∅ = 0, (5) and

lim

n→∞

P ∪k∈K(z) Od(n, ⌊sn⌋, k) = ∅ = 0. (6)

lim

n→∞

In other words, both in the Erd¨os-R´enyi and in the random regular graph models, when β > 1/√2, and d is large enough, with probability approaching unity as n → ∞, one cannot ﬁnd a pair of independent sets I and J with size ⌊ns⌋, such that their overlap (intersection) has

![image 29](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile29.png>)

cardinality at least n(1−zd) logd and at most n(1+zd) logd.

![image 30](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile30.png>)

![image 31](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile31.png>)

Note that for all β > 1/√2, there exists z satisfying 0 < z < 2β2 − 1 and so the theorem is not vacuous in this setting. Furthermore as β → 1, z can be chosen arbitrarily close to 1 making the forbidden overlap region extremely broad. That is, as the size of the independent sets in consideration approaches the maximum possible (namely as β ↑ 1), and as d → ∞, we can take z → 1. In other words, with probability approaching one, two nearly largest independent sets either overlap almost entirely or almost do not have an intersection. This is the key result for establishing our hardness bounds for existence of local algorithms.

![image 32](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile32.png>)

![image 33](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile33.png>)

A slightly diﬀerent version of the ﬁrst of these results can be found as Lemma 12 in [COE11]. The latter paper shows that if an independent set I is chosen uniformly at random from the set with size nearly (1 + β)nlog d/d, then with high probability (with respect to the choice of I), there exists an empty overlap region in the sense described above. In fact, this empty overlap region exists for every β ∈ (0, 1), as opposed to just 1 > β > 1/2 + 1/(2√2) as in our case. Unfortunately, this result cannot be used for our purposes, since this result does not rule out the existence of rare sets I for which no empty overlap exists.

![image 34](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile34.png>)

Overlapping from local algorithms Next we turn to the formalizing the notion of using a local function fr twice on coupled randomness to produce overlapping independent sets.

Fix an r-local independence function fr. Given a vector X = (Xu, 1 ≤ u ≤ n) of variables Xu ∈ [0, 1], recall that IG(fr, X) denotes the independent set of G given by u ∈ IG(fr, X) if and only if fr(u, G, X) = 1.

Recall that X is chosen according to the uniform distribution on [0, 1]n. Namely, Xu are independent and uniformly distributed over [0, 1]. In what follows we consider some joint distributions on pairs of vectors (X, Y) such that marginal distributions on the vector X and Y are uniform on [0, 1]n, though X and Y are dependent on each other. The intuition behind the proof of Theorem 2.5 is as follows. Note that if X = Y then IG(fr, X) = IG(fr, Y). As a result the overlap IG(fr, X) ∩ IG(fr, Y) between IG(fr, X) and IG(fr, Y) is α(fr)n + o(n) in expectation. On the other hand, if X and Y are independent, then the overlap between IG(fr, X) and IG(fr, Y) is α2(fr)n + o(n) in expectation, since the decision to pick a vertex u in I is independent for most vertices when X and Y are independent. (In particular, note that if the local

neighborhood around u is a tree, which according to Proposition 2.2 happens with probability approaching unity, then the two decisions are independent, and u ∈ I with probability α(fr).) Our main theorem shows that by coupling the variables, the overlap can be arranged to be of any intermediate size, to within an additive o(n) factor. In particular, if α(fr) exceeds 21 + 2√12 we will be able to show that the overlap can be arranged to be between the values (1−z)dnlogd and (1+z)n log d

![image 35](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile35.png>)

![image 36](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile36.png>)

![image 37](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile37.png>)

![image 38](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile38.png>)

d , described in Theorem 2.6 which contradicts the statement of this theorem.

![image 39](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile39.png>)

- Theorem 2.7. Fix a positive integer d. For constant r, let fr(u, G, x) be an r-local independence function and let α = α(fr). For every γ ∈ [α2, α] and ǫ > 0, and for every suﬃciently large n, there exists a distribution on variables (X, Y) ∈ [0, 1]n × [0, 1]n such that


d(n),(X,Y) |IG

d(n)(fr, X) ∩ IG

d(n)(fr, Y)|  ∈ [(γ − ǫ)n, (γ + ǫ)n] ≤ ǫ.

PG

## 3 Proof of Theorem 2.5

We now show how Theorems 2.6 and 2.7 immediately imply Theorem 2.5.

Proof of Theorem 2.5. Fix an r-local function fr and let α = α(fr). Fix 0 < η < 1. We will prove below that for suﬃciently large d we have α/αd ≤ 1/2 + 1/(2√2) + η. The theorem will then follow.

![image 40](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile40.png>)

Let ǫ = ηlog2d d. By Proposition 2.3 we have that almost surely an independent set returned by fr on Gd(n) is of size at least (α−ǫ)n. Furthermore for every γ ∈ [α2, α] we have, by Theorem 2.7, that Gd(n) almost surely has two independent sets I and J, with

![image 41](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile41.png>)

|I|, |J| ≥ (α − ǫ)n and |I ∩ J| ∈ [(γ − ǫ)n, (γ + ǫ)n]. (7)

Finally, by Theorem 2.1, we have that for suﬃciently large d, |I|, |J| ≤ (2d−1 log d)(1 + η)n ≤ 4d−1 log dn and so α2 ≤ d−1 log d, allowing us to set γ = d−1/ log d.

![image 42](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile42.png>)

Now we apply Theorem 2.6 with z = ǫd/ log d and β > 1+2z2. (Note that for this choice we have z < 1 and z < 2β2 − 1 < β < 1. We will also use later the fact that for this choice we have β ≤ 1/√2 + z = 1/√2 + ǫd−1 log d.) Theorem 2.6 asserts that almost surely Gd(n) has no independent sets of size at least (1+β)d−1 log dn with intersection size in [(1−z)d−1 log dn, (1+ z)d−1 log dn]. Since |I ∩ J| ∈ [(γ − ǫ)n, (γ + ǫ)n] = [(1 − z)d−1 log dn, (1 + z)d−1 log dn], we conclude that min{|I|, |J|} ≤ (1 + β)d−1 log dn. Combining with Equation (7) we get that (α − ǫ)n ≤ min{|I|, |J|} ≤ (1 + β)d−1 log dn and so α ≤ (1 + β)d−1 log d + ǫ, which by the given bound on β yields α ≤ (1 + 1/√2)d−1 log d + 2ǫ = (1 + 1/√2 + η)d−1 log d. On the other hand we also have αd ≥ (2 − η)d−1 log d. It follows that α/αd ≤ 1/2 + 1/2√2 + η as desired.

![image 43](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile43.png>)

![image 44](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile44.png>)

![image 45](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile45.png>)

![image 46](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile46.png>)

![image 47](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile47.png>)

![image 48](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile48.png>)

![image 49](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile49.png>)

![image 50](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile50.png>)

![image 51](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile51.png>)

![image 52](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile52.png>)

![image 53](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile53.png>)

## 4 Proof of Theorem 2.7

For parameter p ∈ [0, 1], we deﬁne the p-correlated distribution on vectors of random variables (X, Y) to be the following: Let X, Z be independent uniform vectors over [0, 1]n. Now let Zu = Xu with probability p and Yu with probability 1 − p independently for every u ∈ V (G).

Let f(u, G, x) and α be as in the theorem statement. Recall that f(x) = f(1, Td,r, x) is the decision of f on the canonical tree of degree d and depth r rooted at the vertex 1. Let γ(p) be the probability that f(X) = 1 and f(Y) = 1, for p-correlated variables (X, Y). As with Proposition 2.3 we have the following.

Lemma 4.1. For every d, r, ǫ > 0 and r-local function f, for suﬃciently large n we have: PG

d(n)(f, Y)| − γ(p) · n| ≥ ǫn ≤ ǫ, where (X, Y) are p-correlated distributions on [0, 1]n.

d(n),(X,Y) ||IG

d(n)(f, X) ∩ IG

Proof. By Proposition 2.2 we have that almost surely almost all local neighborhoods are trees and so for most vertices u the probability that u is chosen to be in the independent sets I(f, X) and I(f, Y) is γ(p). By linearity of expectations we get that E[|I(f, X) ∩ I(f, Y)|] = γ(p) · n + o(n). Again observing that most local neighborhoods are disjoint we have that the variance of |I(f, X)∩ I(f, Y)| is O(n). We conclude, by applying the Chebychev bound, that |I(f, X) ∩ I(f, Y)| is concentrated around the expectation and the lemma follows.

![image 54](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile54.png>)

![image 55](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile55.png>)

![image 56](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile56.png>)

![image 57](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile57.png>)

We also note that for p = 1 and p = 0 the quantity γ(p) follow immediately from their deﬁnition.

- Proposition 4.2. γ(1) = α and γ(0) = α2.


Now to prove Theorem 2.7 it suﬃces to prove that for every γ ∈ [α2, α] there exists a p such that γ(p) = γ. We show this next by showing that γ(p) is continuous. Lemma 4.3. For every r, γ(p) is a continuous function of p.

Proof. Let (Wu, u ∈ Td,r) be random variables associated with nodes in Td,r, uniformly distributed over [0, 1], which are independent for diﬀerent u and also independent from Xu and Zu. We use Wu as generators for the events Yu = Xu vs Yu = Zu. In particular, given p, set Yu = Xu if Wu ≤ p and Yu = Zu otherwise. This process is exactly the process of setting variables Yu to Xu and Zu with probabilities p and 1 − p respectively, independently for all nodes u. Now ﬁx any p1 < p2, and let δ < (p2 − p1)/dr+1. We use the notation fr(Xu, Zu, Wu, p) to denote the value of fr when the seed variables realization is (Wu, u ∈ Td,r), and the threshold value p is used. Namely, fr(Xu, Zu, Wu, p) = fr (Xu1{Wu ≤ p} + Zu1{Wu > p}, u ∈ Td,r). Here, for ease of notation, the reference to the tree Td,r is dropped. Utilizing this notation we have

γ(p) = P (fr(Xu) = fr(Xu, Zu, Wu, p) = 1). Therefore,

γ(p2) − γ(p1) = P (fr(Xu) = fr(Xu, Zu, Wu, p2) = 1) − P (fr(Xu) = fr(Xu, Zu, Wu, p1) = 1)

= E[fr(Xu)fr(Xu, Zu, Wu, p2) − fr(Xu)fr(Xu, Zu, Wu, p1)].

Observe that the event Wu ∈/ [p1, p2] for all u ∈ Td,r implies fr(Xu, Zu, Wu, p1) = fr(Xu, Zu, Wu, p2) for every realization of Xu and Zu. Therefore, by the union bound and since |Td,r| < dr+1, we have

|γ(p2) − γ(p1)| ≤ dr+1(p2 − p1). Since r is ﬁxed, the continuity of γ(p) is established.

![image 58](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile58.png>)

![image 59](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile59.png>)

![image 60](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile60.png>)

![image 61](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile61.png>)

We are now ready to prove Theorem 2.7.

Proof of Theorem 2.7. Given γ ∈ [α2, α] by Lemma 4.3 we have that there exists a p such that γ = γ(p). For this choice of p, let (X, Y) be a pair of p-correlated distributions. Applying Lemma 4.1 to this choice of p, we get that with probability at least 1 − ǫ we have |IG

d(n)(f, X) ∩ IG

d(n)(f, Y)| ∈ [(γ − ǫ)n, (γ + ǫ)n] as desired.

![image 62](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile62.png>)

![image 63](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile63.png>)

![image 64](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile64.png>)

![image 65](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile65.png>)

## 5 Theorem 2.6: Case of the Erdo¨s-R´enyi graph G(n,d/n)

In this section we prove Theorem 2.6 for the case of the random Erd¨os-R´enyi graph. Speciﬁcally we show that the overlap of two independent sets of near maximum cardinality can not be of some intermediate sizes.

The proof is based on a simple moment argument. We ﬁrst determine the expected number of pairs of independent sets with a prescribed overlap size and show that this expectation converges to zero as n → ∞ and in fact converges to zero exponentially fast when the overlap size falls into the corresponding inverval. The result then follows from Markov inequality.

Fix positive integers k ≤ m ≤ n. Recall that O(n, d, m, k) is the set of all pairs of independent sets of cardinality m with intersection size k in the random graph G(n, d/n). It is straightforward to see that

2m−k 2

)−(m−k)2

(

d n

n! k!(m − k)!(m − k)!(n − 2m + k)!

1 −

E[|O(n, d, m, k)|] =

(8)

![image 66](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile66.png>)

![image 67](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile67.png>)

Let m = ⌊ns⌋, where we remind that s = (1 + β)d−1 log d is given by the statement of the theorem. Set k = ⌊nx⌋ for any

(1 − z) log d d

(1 + z) log d d

x ∈

(9)

,

![image 68](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile68.png>)

![image 69](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile69.png>)

It suﬃces to show that there exists γ > 0 such that limsup

n−1 log E[|O(n, d, ⌊ns⌋, ⌊nx⌋)|] ≤ −γ, (10)

n→∞

for all x in the interval (9), as then we can use a union bound on the integer choices

(1 − z) log d d

k ∈ n

, n

![image 70](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile70.png>)

(1 + z) log d d

![image 71](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile71.png>)

.

From this point on we ignore ⌊·⌋ notation for the ease of exposition. It should be clear that this does not aﬀect the argument. From (8), after simplifying using Stirling’s approximation (a! ≈ (a/e)a) and the fact that ln(1 − y) ≈ −y as y → 0, we have

n−1 logE[|O(n, d, ⌊ns⌋, ⌊nx⌋)|]

limsup

n

= xlog x−1 + 2(s − x) log(s − x)−1 + (1 − 2s + x) log(1 − 2s + x)−1 − d

(2s − x)2 2 − (s − x)2 (11)

![image 72](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile72.png>)

We further simplify this expression as

xlog x−1 + 2(s − x) log(s − x)−1 + (1 − 2s + x) log(1 − 2s + x)−1 − ds2 + dx2/2. We have from (9) that for large enough d

x−1 ≤ d. Also, for large enough d, since z < β, then

(s − x)−1 ≤

(1 + β) log d d −

(1 + z) log d d

![image 73](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile73.png>)

![image 74](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile74.png>)

−1

≤ d.

Finally, we use the following following asymptotics valid as d → ∞:

log d d

(1 − 2s + x) log(1 − 2s + x)−1 = O

![image 75](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile75.png>)

, (12)

which applies since 0 ≤ x ≤ s = O(log d/d). Substituting the expression for s = (1+β)d−1 log d, we obtain a bound

(1 + β) log d

n−1 log E[|O(ns, nx)|] ≤ xlog d + 2

d − x log d + O(log d/d) − d

![image 76](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile76.png>)

2

(1 + β) log d d

+ dx2/2.

![image 77](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile77.png>)

Writing x = (1 + zˆ) log d/d, where according to (9) zˆ varies in the interval [−z, z], we can conveniently rewrite our bound as

log2 d d

2(1 + β) − (1 + β)2 − (1 + zˆ) + (1 + zˆ)2/2 + O(log d/d). Now we can force the expression to be negative for large enough d, provided that 2(1 + β) − (1 + β)2 − (1 + zˆ) + (1 + zˆ)2/2 < 0,

![image 78](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile78.png>)

![image 79](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile79.png>)

which is equivalent to |zˆ| < 2β2 − 1 which in turn follows from the conditions on z in the hypothesis of the theorem statement.

This completes the proof of (5) and thus the proof of the theorem for the case of Erd¨os-R´enyi graph.

## 6 Theorem 2.6: Case of the random regular graph Gd(n)

We now turn to the case of random regular graphs Gn(d). We use a conﬁguration model of Gd(n) [Bol85],[J LR00], which is obtained by replicating each of the n nodes of the graph d times, and then creating a random uniformly chosen matching connecting these dn nodes. Since nd is assumed to be even, such a matching exists. Then for every two nodes u, v ∈ [n] an edge is created between u and v, if there exists at least one edge between any of the replicas of u and

any of the replicas of v. This step of creating edges between nodes in [n] from the matching on nd nodes we call projecting. It is known that, conditioned on the absence of loops and parallel edges, this gives a model of a random regular graph. It is also known that the probability of appearing of at least one loop or at least two parallel edges is bounded away from zero when d is bounded. Since we are only concerned with statements taking place with high probability, such a conditioning is irrelevant to us and thus we assume that Gd(n) is obtained simply by taking a random uniformly chosen matching and projecting. The conﬁguration model is denoted by G¯d(n), with nodes denoted by (i, r) where i = 1, 2, . . ., n and r = 1, . . ., d. Namely, (i, r) is the r-th replica of node i in the original graph. Given any set A ⊂ [n], let A¯ be the natural extension of A into the conﬁguration model. Namely A¯ = {(i, r) : i ∈ I, r = 1, . . ., d}.

Recall that Od(n, m, k) stands for the set of pairs of independent sets I, J in Gd(n) such that |I| = |J| = m and |I ∩ J| = k. Note that there are possibly some edges between I¯\ J¯ and J¯\ I¯ resulting in edges between I \ J and J \ I. Let R(m, k, l) ⊂ Od(n, m, k) be the set of pairs I, J such that the number of edges between I¯\ J¯ and J¯\ I¯ in the conﬁguration graph model G¯d(n) is exactly l. Here, for the ease of notation we dropped the references to d and n. Observe that l is at most d(m − k) and ∪ld=0(m−k)R(m, k, l) = Od(n, m, k). In what follows we will bound the expected size of R(m, k, l) for every l, and thus the expected size of their union.

For (I, J) ∈ R(m, k, l) the number of edges between the set I∪J and its complement [n]\(I∪J) is precisely (2m−k)d−2l, since |I ∪J| = 2m−k. The same applies to the conﬁguration model: the number of edges between I¯∪ J¯ and its complement [nd] \ (I¯∪ J¯) is precisely (2m− k)d − 2l. The value of E[|R(m, k, l)|] is then computed as follows. Let R = 2m − k and l ≤ d(m − k).

- Lemma 6.1.


2 nd − Rd Rd − 2l

md − kd l

n k, m − k, m − k, n − R

l!(Rd − 2l)!×

E|R(m, k, l)| =

nd 2

(nd − 2Rd + 2l)! (nd/2 − Rd + l)!2nd/2−Rd+l

(nd/2)!2

![image 80](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile80.png>)

×

.

![image 81](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile81.png>)

![image 82](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile82.png>)

(nd)!

Proof. The proof is based on the fact that the number of matchings on a set of m nodes (for even m) is m!

nd 2

. So the term (nd/2)!2

![image 83](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile83.png>)

(nd)! is precisely the inverse of the number of conﬁguration

(m/2)!2m2

![image 84](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile84.png>)

![image 85](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile85.png>)

![image 86](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile86.png>)

graphs G¯d(n). The term k,m−k,m n−k,n−R is the number of ways of selecting a pair of sets I and J with cardinality m each and intersection size k. Finally,

2 nd − Rd Rd − 2l

(nd − 2Rd + 2l)! (nd/2 − Rd + l)!2nd/2−Rd+l

md − kd l

l!(Rd − 2l)!

![image 87](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile87.png>)

is the number of graphs Gd(n) such that for a given choice of sets I and J, both sets are independent sets, and the number of edges between I \J and J \I is l. Here md−l kd 2 represents the number of choices for end points of the l edges between I \ J and J \ I; l! represents the number of matchings once these choices are made; ndRd−−Rd2l represents the number of choices for the end points of edges connecting I ∪ J with its complement; (Rd − 2l)! represents the number of matchings once these choices are made; and ﬁnally

(nd − 2Rd + 2l)! (nd/2 − Rd + l)!2nd/2−Rd+l

![image 88](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile88.png>)

represents the number of matching choices between the remaining nd − 2Rd + 2l nodes in the complement of I¯∪ J¯.

![image 89](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile89.png>)

![image 90](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile90.png>)

![image 91](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile91.png>)

![image 92](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile92.png>)

We write k = xn, m = sn, l = dyn, where x ≤ s ≤ 1. Then R = (2s − x)n and y ≤ s − x. Our main goal is establishing the following analogue of (10).

- Lemma 6.2. There exists γ > 0 such that


n−1 log E[|R(⌊ns⌋, ⌊nx⌋, ⌊ny⌋)|] ≤ −γ, (13)

limsup

n→∞

for s = (1 + β)d−1 log d, for all x in the interval (9) and all 0 ≤ y ≤ s − x.

The claim (6) of Theorem 2.5 follows from Lemma 6.2 by an argument similar to the one for the Erd¨os-R´enyi graph. The rest of this section is devoted to proving Lemma 6.2.

By Lemma 6.1, we have

E[|R(m, k, l)|] =

=

=

2 nd − Rd Rd − 2l

md − kd l

n k, m − k, m − k, n − R

l!(Rd − 2l)!(1 + o(1))

(nd−2Rd+2l) 2

nd 2

(nd − 2Rd + 2l)

e

![image 93](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile93.png>)

![image 94](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile94.png>)

×

(1 + o(1))

![image 95](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile95.png>)

![image 96](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile96.png>)

nd 2

(nd−2Rd+2l) 2

(nd)

e

![image 97](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile97.png>)

![image 98](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile98.png>)

((md − kd)!)2 (l!)2((md − kd − l)!)2

(nd − Rd)! (Rd − 2l)!(nd − 2Rd + 2l)! ×l!(Rd − 2l)!(nd − 2Rd + 2l)

n! k!((m − k)!)2(n − R)!

![image 99](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile99.png>)

![image 100](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile100.png>)

![image 101](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile101.png>)

(nd−2Rd+2l)

2 eRd−l(nd)−nd2 (1 + o(1))

![image 102](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile102.png>)

![image 103](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile103.png>)

((md − kd)!)2 l!((md − kd − l)!)2

(nd − Rd)! (nd − 2Rd + 2l)! ×(nd − 2Rd + 2l)

n! k!((m − k)!)2(n − R)!

![image 104](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile104.png>)

![image 105](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile105.png>)

![image 106](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile106.png>)

(nd−2Rd+2l)

2 eRd−l(nd)−nd2 (1 + o(1))

![image 107](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile107.png>)

![image 108](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile108.png>)

We now consider the logarithm of the expression above normalized by n. Thus n−1 log E[|R(m, k, l)|]

= −xlog x − 2(s − x) log(s − x) − (1 − 2s + x) log(1 − 2s + x)

+2(sd − xd) log(sd − xd) − 2(sd − xd) − dy log dy + dy −2(sd − xd − dy) log(sd − xd − dy) + 2(sd − xd − dy)

+(d − 2ds + dx) log(d − 2ds + dx) − (d − 2ds + dx) −(d − 4ds + 2dx + 2dy) log(d − 4ds + 2dx + 2dy) + (d − 4ds + 2dx + 2dy)

- 1

![image 109](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile109.png>)

- 2


(d − 4ds + 2dx + 2dy) log(d − 4ds + 2dx + 2y)

+

d 2

+d(2s − x − y) −

log d

![image 110](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile110.png>)

= −xlog x − 2(s − x) log(s − x) − (1 − 2s + x) log(1 − 2s + x)

+2(sd − xd) log(sd − xd) − dy log dy −2(sd − xd − dy) log(sd − xd − dy)

+(d − 2ds + dx) log(d − 2ds + dx) −

- 1

![image 111](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile111.png>)

- 2


d 2

(d − 4ds + 2dx + 2dy) log(d − 4ds + 2dx + 2dy) −

log d −2(sd − xd) + dy + 2(sd − xd − dy) − (d − 2ds + dx)

![image 112](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile112.png>)

+(d − 4ds + 2dx + 2dy) + d(2s − x − y)

The term not involving log is easily checked to be zero. Consider terms of the form log(dA) = log d + log A and consider the log d terms. The corresponding multiplier is

2(sd − xd) − dy − 2(sd − xd − dy) + (d − 2ds + dx) − 21(d − 4ds + 2dx + 2dy) − d2, which again is found to be zero. The ﬁnal expression we obtain is then

![image 113](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile113.png>)

![image 114](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile114.png>)

= −xlog x − 2(s − x) log(s − x) − (1 − 2s + x) log(1 − 2s + x)

+2d(s − x) log(s − x) − dy log y −2d(s − x − y) log(s − x − y)

+d(1 − 2s + x) log(1 − 2s + x) −

d 2

(1 − 4s + 2x + 2y) log(1 − 4s + 2x + 2y). (14)

![image 115](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile115.png>)

We now recall that s = (1 + β) log d/d and x lies in the interval (9). We consider now two cases. Speciﬁcally, we ﬁrst consider the case

log2 d

(β + z + 1)2

d2 ≤ y ≤ s − x, (15) and then consider the case

![image 116](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile116.png>)

0 ≤ y ≤ (β + z + 1)2

log2 d d2

. (16)

![image 117](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile117.png>)

Assume ﬁrst that (15) holds. Consider the terms containing y:

d 2

(1 − 4s + 2x + 2y) log(1 − 4s + 2x + 2y) Then

f(y) −dy log y − 2d(s − x − y) log(s − x − y) −

![image 118](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile118.png>)

d−1f˙(y) = −log y − 1 + 2 log(s − x − y) + 2 − log(1 − 4s + 2x + 2y) − 1

= −log y + 2 log(s − x − y) − log(1 − 4s + 2x + 2y). Now by our assumption (15), we have y ≥ (β + z + 1)2d−2 log2 d implying −log y ≤ −2 log(β + z + 1) + 2 log d − 2 log log d

Also 4s−2x−2y ≤ 4s < 8 log d/d = O(log d/d), implying that log(1−4s+2x+2y) = O(log d/d). Finally, from (9) we have s − x − y ≤ s − x = (β + z) log d/d, implying that log(s − x − y) ≤ −log d + log log d + log(β + z). Combining, we obtain that

d−1f˙(y) ≤ −2 log(β + z + 1) + 2 log d − 2 log log d − 2 log d + 2 loglog d + 2 log(β + z)

+ O(log d/d)

= −2 log(β + z + 1) + 2 log(β + z) + O(log d/d).

In particular, the derivative is negative for large enough d and thus the largest value of f(y) when y is in the interval (15) is obtained at the left end of this interval. Thus, without the loss of generality, we may assume from now on that the bound (16) holds.

For convenience we start with the term (1 − 2s + x) log(1 − 2s + x) in (14). Using the ﬁrst order Taylor approximation log(1 − t) = −t + o(t), and the fact s = O(log d/d), x = O(log d/d), we have

(1 − 2s + x) log(1 − 2s + x) = O(logd/d)

= o(log2 d/d). Next we analyze the term d(1 − 2s + x) log(1 − 2s + x). Using the approximation

(1 − t) log(1 − t) = −t + t2/2 + O(t3), we obtain

d(1 − 2s + x) log(1 − 2s + x) = −d(2s − x) +

d 2

(2s − x)2 + O(d(2s − x)3).

![image 119](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile119.png>)

Before we expand this term in terms of d, it will be convenient to obtain a similar expansion for the last term in (14)

d 2

(1 − 4s + 2x + 2y) log(1 − 4s + 2x + 2y)

![image 120](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile120.png>)

d 2

d 4

(4s − 2x − 2y)2 + O(d(4s + 2x + 2y)3)

= −

(4s − 2x − 2y) +

![image 121](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile121.png>)

![image 122](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile122.png>)

= −d(2s − x) + dy + d(2s − x)2 − 2d(2s − x)y + dy2 + O(d(4s + 2x + 2y)3)

Applying the upper bound (16) we have O(d(2s − x)3) = O(log3 d/d2) = o(log2 d/d), O(d(4s + 2x + 2y)3) = o(log2 d/d), and dy2 = O(log4 d/d3) = o(log2 d/d). Combining, we obtain

d 2

d(1 − 2s + x) log(1 − 2s + x) −

(1 − 4s + 2x + 2y) log(1 − 4s + 2x + 2y)

![image 123](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile123.png>)

d 2

(2s − x)2 − dy + 2d(2s − x)y + o(log2 d/d)

= −

![image 124](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile124.png>)

d 2

(2s − x)2 − dy + o(log2 d/d), (17) where again applying bound (16) on y we have used

= −

![image 125](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile125.png>)

log2 d d2

log d d

2d(2s − x)y = O d

![image 126](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile126.png>)

![image 127](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile127.png>)

= o(log2 d/d).

Next it is convenient to analyze the following two terms together: 2d(s − x) log(s − x) − 2d(s − x − y) log(s − x − y)

= 2d(s − x) log(s − x) − 2d(s − x) log(s − x − y) + 2dy log(s − x − y)

= 2d(s − x) log(s − x) − 2d(s − x) log(s − x) − 2d(s − x) log(1 − y(s − x)−1)

+2dy log(s − x) − 2dy log(1 − y(s − x)−1))

= −2d(s − x) log(1 − y(s − x)−1) + 2dy log(s − x) − 2dy log(1 − y(s − x)−1))

= 2d(s − x)y(s − x)−1 + O(dy2(s − x)−1)

+2dy log(s − x) + 2dy2(s − x)−1 + O(dy3(s − x)−2)

= 2dy + 2dy log(s − x) + 2dy2(s − x)−1 + O(dy2(s − x)−1) + O(dy3(s − x)−2)

= 2dy + 2dy log(s − x) + o(log2 d/d), where we have used the asymptotics y = O(log2 d/d2) implied by (16) in the last equality.

We now analyze the remaining terms involving y. From (17) we have the term −dy. Combining with the asymptotics above and the remaining term −dy log y from (14) we obtain

2dy + 2dy log(s − x) − dy − dy log y = dy + 2dy log(s − x) − dy log y. (18)

We compute the maximum value of this quantity in the relevant range of y given by (16). The ﬁrst derivative of this expression is

d + 2d log(s − x) − d − d log y = 2d log(s − x) − d log y which is positive (inﬁnite) at y = 0. At y = (β + z + 1)2 log2 d/d2, the ﬁrst derivative is 2d log(s − x) − 2d log(β + z + 1) − 2d log log d + 2d log d

≤ 2d log(β + z) + 2d loglog d − 2d log d − 2d log(β + z + 1) − 2d loglog d + 2d logd

= 2d log(β + z) − 2d log(β + z + 1) < 0,

where the inequality relies on x ≥ (1 − z) log d/d implied by (9), which gives s − x ≤ (β + z) log d/d.

The second derivative is −d/y which is negative since y ≥ 0. Thus, the function is strictly concave with positive and negative derivatives at the ends of the relevant interval (16). The maximum is then achieved at the unique point y∗ where the derivative is zero, namely when 2d log(s − x) − d log y∗ = 0, giving

y∗ = (s − x)2. Plugging this into the right-hand side of (18) we obtain dy∗+2dy∗ log(s − x) − dy∗ log y∗

= d(s − x)2 + 2d(s − x)2 log(s − x) − d(s − x)2 log(s − x)2

= d(s − x)2. Summarizing, and using (17), we ﬁnd that the expression in (14) is at most

= −xlog x − 2(s − x) log(s − x) −

d 2

(2s − x)2 + d(s − x)2 + o(log2 d/d),

![image 128](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile128.png>)

which is precisely the expression (11) we have derived for the case of Erd¨os-R´enyi graph G(n, c/n), with the exception of the term (1−2s+x) log(1−2s+x), which is o(log2 d/d) by (12). We have obtained the expression we have analyzed for the case of graphs G(n, c/n), for which we have shown that the expression is negative for the speciﬁed choices of s and x for suﬃciently large d. This completes the proof of Lemma 6.2 and of Theorem 2.6.

## Acknowledgements

The ﬁrst author wishes to thank Microsoft Research New England for providing exciting and hospitable environment during his visit in 2012 when this work was conducted. The same author also wishes acknowledge the general support of NSF grant CMMI-1031332.

## References

[ACORT11] D. Achlioptas, A. Coja-Oghlan, and F. Ricci-Tersenghi, On the solution space geometry of random formulas, Random Structures and Algorithms 38 (2011), 251–268.

[Ald] D. Aldous, Some open problems. http://www.stat.berkeley.edu/∼aldous/ Re-

search/OP/index.html. [AS92] N. Alon and J. Spencer, Probabilistic method, Wiley, 1992. [BCG13] Christian Borgs, Jennifer Chayes, and David Gamarnik, Convergent sequences of

sparse graphs: A large deviations approach, arXiv preprint arXiv:1302.4615 (2013).

[BCL+12] C. Borgs, J.T. Chayes, L. Lova´sz, V.T. S´os, and K. Vesztergombi, Convergent graph sequences II: Multiway cuts and statistical physics, Ann. of Math. 176 (2012), 151– 219.

[BCL+08] , Convergent graph sequences I: Subgraph frequencies, metric properties, and testing, Advances in Math. 219 (208), 1801–1851.

![image 129](<2013-gamarnik-limits-local-algorithms-sparse_images/imageFile129.png>)

[BCLK] C. Borgs, J.T. Chayes, L. Lova´sz, and J. Kahn, Left and right convergence of graphs with bounded degree, http://arxiv.org/abs/1002.0115.

[BGT10] M. Bayati, D. Gamarnik, and P. Tetali, Combinatorial approach to the interpolation method and scaling limits in sparse random graphs, Annals of Probability, to appear. Conference version in Proc. 42nd Ann. Symposium on the Theory of Computing (STOC) (2010).

[Bol85] B. Bollobas, Random graphs, Academic Press, Inc., 1985. [CL12] E. Csoka and G. Lippner, Invariant random matchings in cayley graphs, arXiv

preprint arXiv:1211.2374 (2012).

[CO11] A. Coja-Oghlan, On belief propagation guided decimation for random k-sat, Proceedings of the Twenty-Second Annual ACM-SIAM Symposium on Discrete Algorithms, SIAM, 2011, pp. 957–966.

[COE11] A. Coja-Oghlan and C. Efthymiou, On independent sets in random graphs, Proceedings of the Twenty-Second Annual ACM-SIAM Symposium on Discrete Algorithms, SIAM, 2011, pp. 136–144.

[EL10] G. Elek and G. Lippner, Borel oracles. an analytical approach to constant-time algorithms, Proc. Amer. Math. Soc, vol. 138, 2010, pp. 2939–2947.

[F L92] A.M. Frieze and T.  Luczak, On the independence and chromatic numbers of random

regular graphs, Journal of Combinatorial Theory, Series B 54 (1992), no. 1, 123–132. [Fri90] A. Frieze, On the independence number of random graphs, Discrete Mathematics 81

(1990), 171–175.

[HKNO09] Avinatan Hassidim, Jonathan A. Kelner, Huy N. Nguyen, and Krzysztof Onak, Local graph partitions for approximation and testing, FOCS, IEEE Computer Society, 2009, pp. 22–31.

[HLS] H. Hatami, L. Lova´sz, and B. Szegedy, Limits of local-global convergent graph sequences, Preprint at http://arxiv.org/abs/1205.4356.

[J LR00] S. Janson, T.  Luczak, and A. Rucinski, Random graphs, John Wiley and Sons, Inc., 2000.

[KS81] R. Karp and M. Sipser, Maximum matchings in sparse random graphs, 22nd Annual Symposium on Foundations of Computer Science, 1981, pp. 364–375.

[Lin92] Nathan Linial, Locality in distributed graph algorithms, SIAM J. Comput. 21 (1992), no. 1, 193–201.

[LN11] R. Lyons and F. Nazarov, Perfect matchings as iid factors on non-amenable groups, European Journal of Combinatorics 32 (2011), no. 7, 1115–1125.

[LS06] L. Lova´sz and B. Szegedy, Limits of dense graph sequences, Journal of Combinatorial Theory, Series B 96 (2006), 933–957.

[MM09] M. Mezard and A. Montanari, Information, physics and computation, Oxford graduate texts, 2009.

[MMZ05] M. M´ezard, T. Mora, and R. Zecchina, Clustering of solutions in the random satisﬁability problem, Physical Review Letters 94 (2005), no. 19, 197205.

[NO08] Huy N. Nguyen and Krzysztof Onak, Constant-time approximation algorithms via local improvements, FOCS, IEEE Computer Society, 2008, pp. 327–336.

[PR07] Michal Parnas and Dana Ron, Approximating the minimum vertex cover in sublinear time and a connection to distributed algorithms, Theor. Comput. Sci. 381 (2007), no. 1-3, 183–196.

[RTVX11] Ronitt Rubinfeld, Gil Tamir, Shai Vardi, and Ning Xie, Fast local computation algorithms, ICS (Bernard Chazelle, ed.), Tsinghua University Press, 2011, pp. 223– 238.

[Tal10] M. Talagrand, Mean ﬁeld models for spin glasses: Volume I: Basic examples, Springer, 2010.

[WJ05] M. J. Wainwright and M. I. Jordan, A variational principle for graphical models, New Directions in Statistical Signal Processing: From Systems to Brain. Cambridge, MA: MIT Press, 2005.

