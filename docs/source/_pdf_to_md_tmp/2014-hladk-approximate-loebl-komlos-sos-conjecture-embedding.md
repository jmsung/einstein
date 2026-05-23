arXiv:1406.3935v2[math.CO]14Apr2015

THE APPROXIMATE LOEBL–KOMLOS–S´ OS´ CONJECTURE AND EMBEDDING TREES IN SPARSE GRAPHS

JAN HLADKY,´ DIANA PIGUET, MIKLOS´ SIMONOVITS, MAYA STEIN, AND ENDRE SZEMEREDI´

Abstract. Loebl, Koml´os and S´os conjectured that every n-vertex graph G with at least n/2 vertices of degree at least k contains each tree T of order k + 1 as a subgraph. We give a sketch of a proof of the approximate version of this conjecture for large values of k.

For our proof, we use a structural decomposition which can be seen as an analogue of Szemer´edi’s regularity lemma for possibly very sparse graphs. With this tool, each graph can be decomposed into four parts: a set of vertices of huge degree, regular pairs (in the sense of the regularity lemma), and two other objects each exhibiting certain expansion properties. We then exploit the properties of each of the parts of G to embed a given tree T.

The purpose of this note is to highlight the key steps of our proof. Details can be found in [arXiv:1211.3050].

1. Introduction

Szemer´edi’s Regularity Lemma from 1975 allows to decompose each dense graph into a bounded collection of random-like subgraphs. The lemma and its variants have found numerous applications in graph theory, number theory, and theoretical computer science. In particular, it is crucial to some developments on extremal problems concerning dense graphs, in the last two decades. On the other hand, extremal problems concerning sparse graphs have been lacking a general framework. We present a new tool which generalizes the Regularity Lemma and which applies to all graphs. This tool seems particularly suitable for embedding trees, even in very sparse graphs. As an application, we prove an approximate version of the Loebl–Komlo´s–S´os Conjecture.

The Loebl–Komlo´s–S´os Conjecture is a typical example of a problem in extremal graph theory. These often are of the following type: Does a certain density condition imposed on a graph of order n guarantee a given subgraph? Statements of this spirit include Mantel’s theorem, which states that an average degree of more than n/2 ensures a triangle as a subgraph, the more general Tur´an theorem, and Dirac’s theorem, which states that a minimum degree of at least n/2 forces the appearance of a Hamilton cycle. Other prominent results include the Erdo˝s–Stone–Simonovits theorem which determines asymptotically the average degree threshold for appearance of any ﬁxed graph, or the solution [KSS98a] of the Po´sa–Seymour conjecture about containment of powers of Hamilton cycles.

![image 1](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile1.png>)

Key words and phrases. Extremal graph theory, tree-containment problems, Loebl–Koml´os– S´os conjecture, regularity lemma, sparse graphs

Mathematics Subject Classiﬁcation: 05C35 (primary), 05C05 (secondary).

1

Some of the progress in the area in the last two decades has been enabled by the developments around the regularity lemma. The regularity lemma allows to approximate an original graph by a so-called cluster graph. The point in doing so is that an original combinatorial problem translates to an easier one on the cluster graph. Let us illustrate this fundamental feature with the examples mentioned above: the modern, regularity lemma based approach reduces the Erdo˝s–Stone– Simonovits theorem to Tur´an’s theorem on the cluster graph. In a similar spirit, the proof of the Po´sa–Seymour conjecture about the appearance of the k-th power of a Hamilton cycle can be reduced to an easier question of tiling with copies of Kk+1 on the cluster graph level, an answer to which is given by the Hajnal–Szemer´edi theorem. These and other applications of the regularity lemma in extremal graph theory are surveyed in [KSSS02, KO09].

Containment of trees is a particularly important case to study, as trees constitute a relatively simple graph class. An easy greedy embedding argument shows that each graph with a minimum degree of at least k contains each tree with k edges. A graph formed by a union of cliques of order k shows that this result is optimal.

Two important conjectures have been made as to how the minimum degree condition can be relaxed. The ﬁrst of these is the famous Erdo˝s–S´os conjecture from 1963:

Conjecture 1. Every graph of average degree greater than k − 1 contains all trees with k edges as subgraphs.

- Conjecture 1 trivially holds for the containment of a star with k leaves, and it is

a classical result of Erdo˝s and Gallai [EG59] that it also holds for paths (for more history, see [FS13]). Further partial results include [BD96, Hax01, SW97, Wo´z96]. A proof of the conjecture for large graphs has been announced by Ajtai, Koml´os, Simonovits and Szemer´edi [AKSS].

Loebl, Koml´os, and So´s (see [EFLS95]) conjectured the same assertion holds when replacing the average degree condition with the median degree.

- Conjecture 2. Every graph of median degree at least k contains all trees with k edges as subgraphs.


Previous work on Conjecture 2 includes solutions which use additional restrictions on the host graph [Sof00, Dob02], or on the trees [BLW00, PS08]. Most notably, Conjecture 2 has been solved for large dense graphs, i.e. for k linear in n, in [HP, Coo09], building on an approximate version given in [PS12]. For the exact value k = n/2, this had been achieved earlier in [AKS95, Zha11].

Note that because of the stars, the median degree in Conjecture 2 has to be at least k. Further note that Conjecture 2 is almost best possible in the sense that we cannot decrease much the number of vertices, namely n/2, that are required to have degree at least k. For this, ﬁrst assume that n is even, and that n = k + 1. Let G∗ be obtained from the complete graph on n vertices by deleting all edges inside a set of n2 + 1 vertices. Then G∗ has n2 − 1 vertices of degree k. It is easy to check that G∗ does not contain the path with k edges (or any other tree with k edges and independence number less than n2 + 1). Now, taking the union of several disjoint copies of G∗ we obtain examples for other values of n. (And adding a small complete component we can get to any value of n.) See Figure 1 for an illustration.

![image 2](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile2.png>)

![image 3](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile3.png>)

![image 4](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile4.png>)

![image 5](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile5.png>)

![image 6](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile6.png>)

Figure 1. An extremal graph for the Loebl–Komlo´s–S´os Conjecture.

It is not diﬃcult to see that each of the two conjectures implies that the Ramsey number of two trees Tk and Tm with k and m edges, respectively, is at most k +m. This is best possible for stars of even order, but not for all trees [GG67, HLT02].

Our main result is an approximate version of Conjecture 2, which reads as follows.

- Theorem 3. For every ε > 0 there exists k0 such that for every k > k0, every n-vertex graph G with at least (1+ε)n/2 vertices of degree at least (1+ε)k contains each tree T with k edges.

Previous results [AKS95, PS12, Zha11, HP, Coo09] on the dense case of Conjecture 2 relied on Szemer´edi’s regularity lemma. The strategy of these proofs is explained in the next section. The (original) regularity lemma is void when the host graph is sparse, i.e., when k = o(n). To circumvent this shortcoming, we present an extension of the regularity lemma which is tailored to tree-embedding problems, and which applies even to sparse graphs. We then show how this decomposition, which we call sparse decomposition, can be used to embed the tree T given by Theorem 3.

In this paper we show some of the key ideas behind the proof. The actual implementation of these ideas is technical and can be found in [HKP+a], split into four parts [HKP+b, HKP+c, HKP+d, HKP+e] for publication purposes.

2. The dense case

In this section, we recall the solution of the dense approximate version of Conjecture 2 due to Piguet and Stein. Their proof provides several key ingredients which are common to the proof of Theorem 3.

- Theorem 4 ([PS12]). For every C,ε > 0 there exists k0 such that for every k > k0 we have that every graph G of order n < Ck with at least n/2 vertices of degree at least (1 + ε)k contains each tree T with k edges.


The proof follows a strategy typical for graph theory results which employ the regularity lemma. It has three main steps: partitioning T, ﬁnding a suitable matching structure in the cluster graph G of the graph G, and embedding T into G using this matching structure. The right way to partition T is given by the following lemma. We say that a subtree F ⊂ T is adjacent to a vertex v ∈ V (T) \ V (F) if there is an edge from v to a vertex in F.

- Lemma 5. For each τ > 0, k ∈ N, for any tree T with k edges there is a set


W = WA ∪ WB ⊂ V (T), and a set T = TA ∪ TB of disjoint subtrees covering all of V (T) − W such that

- (a) the trees in T have order less than τk,
- (b) the trees in T are not adjacent to each other,
- (c) |W| < 100/τ,
- (d) each side of the bipartition of V (T) contains one of the sets WA, WB,
- (e) each tree in TB is adjacent to only one vertex of W, and that vertex lies in WB,
- (f) each tree in TA is adjacent to at most two vertices of W, and these lie in WA,
- (g) |V ( TB)| < k/2.


We call a tree in T internal if it is adjacent to two vertices of W, and call it an end tree otherwise. Note that TB only contains end trees by property (e).

In order to obtain the partition from Lemma 5, we traverse T from the leaves to a ﬁxed root, sequentially chopping oﬀ ‘branches’ of T that have reached the critical size of τk. Similar strategies of dividing larger objects into smaller pieces have been used in other proofs employing embedding with the regularity method. As we shall see, the partition of T from Lemma 5 will be useful for the sparse case as well.

The bulk of the work is on ﬁnding a suitable structure in the graph G. To this end we use the regularity lemma [Sze78]. Let us ﬁrst introduce the key notion of regular pairs. Given η > 0, a pair (A,B) of disjoint sets is η-regular if |d(A,B)−d(U,W)| < η for each U ⊆ A,W ⊆ B with |U| > η|A|,|W| > η|B|. The regularity lemma then reads as follows.

- Lemma 6 (Regularity lemma). For each η > 0,m ∈ N there are n0,M such that every graph on n > n0 vertices allows for a partition of all but at most ηn of its vertices into m < k < M sets (the ‘clusters’) such that all but at most ηk2 pairs of clusters form η-regular pairs.


With the help of Lemma 6, we regularize the graph G and obtain a cluster graph G with clusters of size νk. Let L be the set of those clusters of G whose typical vertices have degree more than k. Piguet and Stein show that G contains a matching M plus two adjacent vertices A,B ∈ L such that the vertices in A have degree more than k into M, and those in B have degree larger than k/2 into V (M) ∪ L.

The tree T can be embedded into G by suitably mapping the vertices of WA into A, the vertices of WB into B, and packing subtrees T (viewed as bipartite graphs) into the edges of M and the edges EL emanating from L using basic properties of regular pairs. Here, it is crucial we choose the parameter τ for Lemma 5 such that τ ≪ ν. That is, individual subtrees of T are much smaller than the clusters.

The large degrees of A and B into V (M) ∪ L guarantee that there is enough space for embedding all trees from T . More precisely, each time we wish to embed a tree T′ ∈ T , there are two things we have to ensure. The ﬁrst is that we have enough free space in the neighbourhood of either A or B to map the root of T′. The second is that we have suﬃcient free space in some regular pair meeting this neighbourhood, to map the rest of T′. For this, a degree of about k for the vertices in A and a degree of about k/2 for the vertices in B is suﬃcient.

3. The sparse decomposition

In this section we introduce the basis of our proof of Theorem 3, the sparse decomposition. This tool has been conceived by Ajtai, Koml´os, Simonovits and Szemer´edi during their work on the Erdo˝s–S´os conjecture. It allows to decompose any given graph, after a removal of a small fraction of the edges, into four sets: a set

Ψ of vertices of high degree, a graph Greg whose edges that span regular pairs, an expanding graph Gexp, and a set A of vertices which has a yet diﬀerent expansion property.

Throughout this section, let us ﬁx a graph G on n vertices, and let k have the same order of magnitude as the average degree of G.1 We use Greek majuscules, and minuscules to denote suﬃciently large, and suﬃciently small constants, respectively. Some of these constants may depend on G and k, but are absolutely bounded from above and from below. We make the subtle relations between these constants explicit only when it adds to the clarity of this rough sketch.

The ﬁrst step of the sparse decomposition is to separate the vertices of very high degree from those of comparatively low degree. By deleting only a few well-chosen edges, we arrive at a subgraph G′ of G that has a gap in its degree sequence. More precisely, there are numbers Ω∗ and Ω∗∗ with Ω∗ ≪ Ω∗∗ such that no vertex of G′ has degree between Ω∗k and Ω∗∗k in G′. Let us indicate how to create the gap. We ﬁx constants 1 ≪ Ω1 ≪ Ω2 ≪ ... ≪ Ω⌈1

ε⌉+1 := ∞. There is an index i ∈ [⌈1ε⌉ + 1] such the total degree of the vertices v with deg(v) ∈ [Ωik,Ωi+1k) is at most εkn. Deleting the edges incident with these vertices almost yields the gap with Ω∗ = Ωi, and Ω∗∗ = Ωi+1. The problem is that the edge deletion may cause degrees of other vertices fall into the forbidden region [Ωik,Ωi+1k). This can be resolved using an additional argument, which we omit here.

![image 7](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile7.png>)

![image 8](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile8.png>)

Let Ψ denote the set of all vertices of degree at least Ω∗∗k. The mere structural information about the vertices Ψ is that they have huge degrees. On the other hand, this property turns out to be so powerful for tree embeddings that it compensates the lack of any ﬁner description.

Before proceeding with the decomposition, we need a few concepts. The density

of a bipartite graph D = (U,W;F) is d(D) := |U|||FW| |, where F = E(D) are the edges of D. An (m,γ)-dense spot in a graph is a non-empty bipartite subgraph D with density d(D) > γ and minimum degree δ(D) > m. A graph H is (m,γ)nowhere-dense if it does not contain any (m,γ)-dense spot.

![image 9](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile9.png>)

Let D be a maximal set of edge-disjoint (γk,γ)-dense spots in G′ − Ψ. Let Gexp be the (γk,γ)-nowhere dense graph obtained from G′ − Ψ by removing the edges of D. (We chose the name Gexp for this graph in order to emphasize its expansion property given by the fact it is nowhere dense.) We now sequentially remove from Gexp any vertex of degree less than ρk, where ρ is a certain constant much smaller than ε, but greater than γ ≪ ρ ≪ ε. Note that in the cleaning procedure we lose less than ρkn edges, and the obtained graph, which we still call Gexp, has minimum degree at least ρk.

The next step consists of regularizing the dense spots in D. By this we mean we wish to ﬁnd a graph spanning almost all of D, and consisting of clusters that pairwise mostly form highly regular pairs, in the sense above. For each single one of these spots this is possible by Lemma 6 above, but such a naive regularization of each dense spot separately is useless. Indeed, for embedding T we may need to traverse many diﬀerent spots D. Thus the cluster structure of diﬀerent dense spots must agree on their intersection.

![image 10](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile10.png>)

1This setting is compatible with the one of Theorem 3. Indeed, a straightforward calculation gives that in that case the average degree d of G satisﬁes d > k/2. If, on the other hand, d ≥ 2k then there is no need to use the sparse decomposition as we can pass to a subgraph with minimum degree at least d/2 ≥ k, and embed T greedily.

So, consider all the Venn cells V with respect to the system {U,W : (U,W;F) ∈ D}. We shall not attempt to regularize those Venn cells A ⊂ V which are of size less than αk (for α ≪ η), as those cells themselves may be smaller than the anticipated cluster sizes. We now construct an auxiliary graph G = (V \ A,E) on the larger Venn cells, joining two Venn cells X,Y with an edge if there is a dense spot (U,W;F) ∈ D with X ⊂ U,Y ⊂ W.

Let us sketch how to regularize simultaneously all the dense pairs corresponding to the edges of G in this setting. It can be shown that the maximum degree of G is bounded from above by a constant ∆ that is independent of k. By Vizing’s theorem, we can cover G with ∆ + 1 matchings M1,...,M∆+1. We follow the idea of Szemer´edi’s proof of the regularity lemma, pumping up the mean square energy when reﬁning an irregular partition. The key diﬀerence is that we track ∆ + 1 mean-square energies, one for each matching Mi, rather than just a single one. This is similar to the proof of the multi-coloured version of the regularity lemma, which tracks a mean-square energy for each colour separately. We thus obtain a system of clusters, of size νk, say, reﬁning V \ A and regular pairs between some of these clusters. Let Greg be the graph spanned by the regular pairs of positive density.

It remains to make use of vertices in A := A, i.e., those in small Venn cells. An elementary double-counting argument gives the following expansion property of A, which we call the (Λ,β,γ)-avoiding property: For every X ⊆ V (G) with |X| ≤ Λk for all but at most βk vertices v ∈ A there is a dense spot D ∈ D which contains v and which satisﬁes |X ∩V (D)| ≤ γ2k. The constant β will be chosen much smaller than γ, but still larger than τ ≪ β ≪ γ.

Putting all of the above together, we obtained a sparse decomposition (Ψ,Greg,Gexp,A) which captures all but at most o(kn) edges of G.

4. Embedding the tree T

The proof of Theorem 4 as outlined in Section 2 is a combination of two elements: a global embedding strategy based on the matching structure given by the clusters A,B, and the matching M, and a local strategy applied sequentially for embedding the individual subtrees from T . The local strategy there is the standard technique of ﬁlling up regular pairs.

Also in the proof of Theorem 3 we shall ﬁnd a suitable global structure, now in the sparse decomposition instead of in the cluster graph. We will discuss this structure later on. Before, we indicate local strategies for embedding subtrees T in each of the ingredients Ψ, Greg, Gexp, A of the sparse decomposition. The starting point of using either Ψ, Greg, Gexp, or A is that in our sequential embedding procedure we wish to extend the partial embedding from a vertex with a substantial degree into the respective object. For this, suppose that U ⊂ V (G) is the set of vertices used in earlier steps of the embedding.

To work with A, we use the avoiding property. Say we have to embed a tree T′ ∈ T . For simplicity, let us assume that T′ ∈ TB; this guarantees that T′ is an end tree. Suppose its parent in WB has been embedded already in a vertex v of degree more than βk into A \ U. Then, by the deﬁnition of the avoiding property, there is a neighbour of v in A \ U that is contained in a dense spot D which does not meet U much. We can place the ﬁrst vertex of T′ appropriately into D. We

then use the minimum degree γk of D to embed the rest of T′ greedily. Here, we use that τ + γ2 ≤ γ.

Next, we show how to use Gexp. Again, suppose we are in the process of embedding a subtree T′ ∈ TB. Say x is the last vertex of T′ that has been embedded already, and we now wish to embed the children of x. Assume the image v of x has neighbourhood Nv ⊂ V (Gexp) of size at least ρk/2 in Gexp − U. (Below it will become clear why we may assume this.) Since Gexp does not contain any (γk,γ)dense spots, in particular not between U and Nv, we know that most vertices in Nv have less than ρk/3 neighbours in U. (Here, we used that γ ≪ ρ.) Thus, it is possible to embed the children of x in vertices that have degree at least ρk/2 in Gexp − (U ∪ x), placing them in equally good positions as x earlier. Following this strategy successively, we manage to embed all of T′.

Regular pairs in Greg are used in the usual way for embedding trees of T . That is, we view these trees as bipartite graphs, and embed them in regular pairs using the regularity property.

It only remains to explain the role of Ψ. This set is used very rarely for embedding; in particular we always have |U ∩ Ψ| < λk/2. The idea is that after mapping a vertex x ∈ T to a vertex v ∈ Ψ, we have an aﬄuence of choices to extend the embedding. However, the huge degree of v alone is not enough. For example, we cannot map non-leaf vertices of T to leaves of G, and these may potentially comprise the entire neighbourhood of v. To circumvent this issue, we employ a rather delicate cleaning procedure prior to starting the embedding. That is, we ﬁnd a set Ψ′ ⊂ Ψ of vertices which have degree at least Ω′k (for suitable Ω∗ ≪ Ω′ ≪ Ω∗∗) into a ‘useful part of G’ in such a way that we do not lose many edges during the cleaning. Having done so, we wish to map the neighbours of x to neighbours of v that send not more than a few edges to U. This will guarantee that we can extend the embedding avoiding U in subsequent steps. To this end, consider the set U˜ = {u ∈ V (G) : deg(u,U) ≥ λk}. We have U˜ ⊂ {u ∈ V : deg(u,U \ Ψ) > λk/2}, and double-counting the edges between U˜ and U \ Ψ gives

Ω∗k|U| λk/2

|U˜| <

≪ Ω′k . In particular, the neighbours of x can be embedded outside of U˜.

![image 11](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile11.png>)

In Lemma 7, we describe the structural counterpart of the matching structure (A,B,M) from the dense case (again, the structure is much simpliﬁed for presentation reasons). Note that this global structure must combine properties of all the objects Ψ, Greg, Gexp, A as it could happen that none of them alone suﬃces for embedding T.

We write L for the set of those vertices of G that have degree at least (1 + ε)k in G. We call a collection M of η-regular pairs of positive density with clusters of sizes µk an (η,µ)-regular matching if all the regular pairs are disjoint.

- Lemma 7. The graph G contains two disjoint sets X,Y ⊆ L, and an (η,µ)-regular matching M with the following properties.


- (i) The bipartite graph G[X,Y] has minimum degree at least 100/τ.
- (ii) The vertices in X each have degree at least (1 + ε/2)k into Q := Ψ ∪ V (Gexp) ∪ A ∪ L ∪ V (M) \ (X ∪ Y) ,
- (iii) The vertices in Y have degrees at least (1 + ε/2)k/2 into Q, and


- (iv) M and X ∪ Y are disjoint.

The sets X and Y will host WA and WB, that is, we can think of X and Y being counterparts to the sets A and B from the dense case. Property (i) then guarantees that the edges between WA and WB can be embedded greedily (cf. Lemma 5(c)). Properties (ii) and (iii) guarantee that subtrees TA and TB can be embedded. Instead of embedding TA and TB using the matching M and edges EL as in the proof of Theorem 4, we have to make use of embedding techniques developed above.

There are two major issues with the indicated approach. The ﬁrst diﬃculty is encountered when embedding an internal tree T′ ∈ TA. As such a tree may be adjacent to two vertices of WA, and we plan to embed WA in X, we have to return to A after embedding T′.

To understand this diﬃculty better, it is instructive to ﬁrst see how an internal tree T′ with head x ∈ WA and tail y ∈ WA is embedded in the dense case (head and tail are the two vertices from Lemma 5(f)). Say x has been embedded into vertex

- v ∈ A. We choose an edge XY ∈ M ∪ EL that will host T′, such that X is an edge in the cluster graph. The regularity of (A,X) guarantees that the embedding of T′ can be extended from x, but also, that after embedding T′ we can embed y back in A.


In the sparse case, we do not have any similar property for the set Q. To resolve this issue, we introduce certain cleaning procedures which guarantee that the last vertex before a tail of an internal tree is always embedded in a vertex of Q which has degree at least 100/τ into X.

![image 12](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile12.png>)

![image 13](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile13.png>)

|![image 14](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile14.png>)|
|---|


| |
|---|


![image 15](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile15.png>)

![image 16](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile16.png>)

Figure 2. The graph G has a set L of 59n vertices of degree 1.1k, and a set S of 49n vertices of degree 0.5k. For each v ∈ L, we have deg(v,L) = 0.7k and deg(v,S) = 0.4k. For each v ∈ S, we have deg(v,L) = 0.5k and deg(v,S) = 0. Further, there is a sparse decomposition of G such that the union of the dense spots D covers all the edges of G. The dense spots D intersect in such a way that the small Venn cells A cover L. The cluster graph Greg is edgeless, and all vertices have degree less than k into Ψ ∪ V (Gexp) ∪ A ∪ L. Thus, for our set X, we need to ﬁnd M elsewhere. In this particular case, one can show that there is a regular matching between L and S covering almost all of S, and that such a matching is a good choice for M.

![image 17](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile17.png>)

![image 18](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile18.png>)

The second diﬃculty arises when constructing the regular matching M. In analogy to the dense case, it would be a natural guess that M is a matching in Greg. In Figure 1 we give an example that it is not always possible to choose M like this.

Given the example of Figure 1, one might wonder why we bother to construct the cluster graph Greg at all. The answer is that for constructing the regular matching M, the graph Greg is of help, either directly, or via the information it gives by lacking a suitable matching.

5. Concluding remarks Let us conclude with several comments.

- • Our proof builds on techniques developed by Ajtai, Koml´os, Simonovits and Szemer´edi for their work on the Erdo˝s–S´os conjecture. However, there is a substantial diﬀerence between the proofs already on the level of the sparse decomposition. In their proof, a suitable matching structure can

always be found in the cluster graph Greg. That means examples like the one in Figure 2 do not enter the picture in the Erdo˝s–S´os conjecture.

- • Similarly as in the Erdo˝s-S´os setting, it seems that our approach can be combined with the stability approach of Simonovits. We hope to resolve the Loebl–Komlo´s–S´os conjecture exactly, for k suﬃciently large (this is work in progress).
- • The sparse decomposition of a graph is not uniquely determined, and can actually vary vastly. This is caused by the arbitrariness in the choice of

the dense spots from which we obtain the regularized graph Greg. This situation is in acute contrast with the situation of decomposition of dense graphs (given by the regularity lemma). Indeed, in the dense setting the structure of the cluster graph is essentially unique, cf. [ASS09].2

- • Another important question is whether there is an alternative approach to proving Conjecture 2 that avoids the notion of sparse decomposition, and even the notion of regular pairs. Such a programme has been developed in the dense setting by Szemer´edi and his collaborators, see [LSS10] for a particular instance of “deregularizing” a result originally resolved [KSS98b] using the regularity method. However, this programme has not given a general alternative view, as of yet.


Acknowledgements

The work on this project lasted from the beginning of 2008 and we are very grateful to the funding bodies for their support.

JH was funded by a BAYHOST fellowship, a DAAD fellowship, Charles University grant GAUK 202-10/258009, EPSRC award EP/D063191/1, and by an EPSRC Postdoctoral Fellowship hosted by the Mathematics Institute at the University of Warwick. JK and ESz acknowledge the support of NSF grant DMS-0902241. DP

![image 19](<2014-hladk-approximate-loebl-komlos-sos-conjecture-embedding_images/imageFile19.png>)

2In order to have uniqueness, the setting needs to be somewhat strengthened; see Theorem 1 and Theorem 2 in [ASS09]. The uniqueness phenomenon can be nicely expressed in the language of graph limits [BCL09].

acknowledges the support of the Marie Curie fellowship FIST, DFG grant TA 309/2-

- 1, a DAAD fellowship, Czech Ministry of Education project 1M0545, EPSRC award EP/D063191/1, grant PIEF-GA-2009-253925 of the European Union’s FP7/20072013, and EPSRC Additional Sponsorship EP/J501414/1. MS was supported by a FAPESP fellowship, and by FAPESP travel grant PQ-EX 2008/50338-0, also CMM-Basal, and FONDECYT grants 11090141 and 1140766.


References

[AKS95] M. Ajtai, J. Koml´os, and E. Szemer´edi. On a conjecture of Loebl. In Graph theory, combinatorics, and algorithms, Vol. 1, 2 (Kalamazoo, MI, 1992), Wiley-Intersci. Publ., pages 1135–1146. Wiley, New York, 1995.

[AKSS] M. Ajtai, J. Koml´os, M. Simonovits, and E. Szemer´edi. Proof of the Erd˝s-T. S´os conjecture for large trees. In preparation. [ASS09] N. Alon, A. Shapira, and U. Stav. Can a graph have distinct regular partitions? SIAM J. Discrete Math., 23(1):278–287, 2008/09. [BCL09] C. Borgs, J. Chayes, and L. Lova´sz. Moments of two-variable functions and the uniqueness of graph limits. J. Geom. and Func. Anal, 19:1597–1619, 2009. [BD96] S. Brandt and E. Dobson. The Erd˝s–So´s conjecture for graphs of girth 5. Discr. Math., 150:411–414, 1996. [BLW00] C. Bazgan, H. Li, and M. Wo´zniak. On the Loebl-Koml´os-So´s conjecture. J. Graph Theory, 34(4):269–276, 2000. [Coo09] O. Cooley. Proof of the Loebl-Koml´os-So´s conjecture for large, dense graphs. Discrete Math., 309(21):6190–6228, 2009. [Dob02] E. Dobson. Constructing trees in graphs whose complement has no K2,s. Combin. Probab. Comput., 11(4):343–347, 2002. [EFLS95] P. Erd˝s, Z. Fu¨redi, M. Loebl, and V. T. S´os. Discrepancy of trees. Studia Sci. Math. Hungar., 30(1-2):47–57, 1995. [EG59] P. Erd˝s and T. Gallai. On maximal paths and circuits of graphs. Acta Math. Acad. Sci. Hungar, 10:337–356 (unbound insert), 1959.

[FS13] Z. Fu¨redi and M. Simonovits. The history of degenerate (bipartite) extremal graph problems. In Erdo¨s centennial, volume 25 of Bolyai Soc. Math. Stud., pages 169–264. Ja´nos Bolyai Math. Soc., Budapest, 2013.

[GG67] L. Gerencs´er and A. Gya´rf´s. On Ramsey-type problems. Ann. Univ. Sci. Budapest. E¨otv¨os Sect. Math., 10:167–170, 1967. [Hax01] P. E. Haxell. Tree embeddings. J. Graph Theory, 36(3):121–130, 2001.

- [HKP+a] J. Hladky´, J. Koml´os, D. Piguet, M. Simonovits, M. Stein, and E. Szemer´edi. The approximate Loebl-Koml´os-So´s conjecture. arXiv: 1211.3050.
- [HKP+b] J. Hladky´, J. Koml´os, D. Piguet, M. Simonovits, M. Stein, and E. Szemer´edi. The ap-

- proximate Loebl-Koml´os-So´s conjecture I: The sparse decomposition. arXiv: 1408:3858.

[HKP+c] J. Hladky´, J. Koml´os, D. Piguet, M. Simonovits, M. Stein, and E. Szemer´edi. The ap-

- proximate Loebl-Koml´os-So´s conjecture II: The rough structure of LKS graphs. arXiv: 1408:3871.


- [HKP+d] J. Hladky´, J. Koml´os, D. Piguet, M. Simonovits, M. Stein, and E. Szemer´edi. The approximate Loebl-Koml´os-So´s conjecture III: The ﬁner structure of LKS graphs. arXiv: 1408:3866.
- [HKP+e] J. Hladky´, J. Koml´os, D. Piguet, M. Simonovits, M. Stein, and E. Szemer´edi. The approximate Loebl-Koml´os-So´s conjecture IV: Embedding techniques and the proof of the main result. arXiv: 1408:3870.


[HLT02] P. E. Haxell, T. Luczak, and P. W. Tingley. Ramsey numbers for trees of small maximum degree. Combinatorica, 22(2):287–320, 2002. Special issue: Paul Erd˝s and his mathematics.

[HP] J. Hladky´ and D. Piguet. Loebl-Koml´os-So´s Conjecture: dense case. arXiv:0805.4834. [KO09] D. Ku¨hn and D. Osthus. Embedding large subgraphs into dense graphs. In Surveys

in combinatorics 2009, volume 365 of London Math. Soc. Lecture Note Ser., pages 137–167. Cambridge Univ. Press, Cambridge, 2009.

- [KSS98a] J. Koml´os, G. S´ark¨zy, and E. Szemer´edi. Proof of the Seymour conjecture for large graphs. Ann. Comb., 2(1):43–60, 1998.
- [KSS98b] J. Koml´os, G. N. S´ark¨zy, and E. Szemer´edi. Proof of the Seymour conjecture for large graphs. Ann. Comb., 2(1):43–60, 1998.


[KSSS02] J. Koml´os, A. Shokoufandeh, M. Simonovits, and E. Szemer´edi. The regularity lemma and its applications in graph theory. In Theoretical aspects of computer science (Tehran, 2000), volume 2292 of Lecture Notes in Comput. Sci., pages 84–112. Springer, Berlin, 2002.

[LSS10] I. Levitt, G. N. S´ark¨zy, and E. Szemer´edi. How to avoid using the regularity lemma: P´osa’s conjecture revisited. Discrete Math., 310(3):630–641, 2010. [PS08] D. Piguet and M. J. Stein. Loebl-Koml´os-So´s conjecture for trees of diameter 5. Electron. J. Combin., 15(1):Research Paper 106, 11 pp. (electronic), 2008. [PS12] D. Piguet and M. J. Stein. An approximate version of the Loebl-Koml´os-So´s conjecture. J. Combin. Theory Ser. B, 102(1):102–125, 2012. [Sof00] S. N. Soﬀer. The Koml´os-So´s conjecture for graphs of girth 7. Discrete Math., 214(1– 3):279–283, 2000. [SW97] J.-F. Sacl´e and M. Wo´zniak. A note on the Erd˝s–So´s conjecture for graphs without C4. J. Combin. Theory (Series B), 70(2):229–234, 1997.

[Sze78] E. Szemer´edi. Regular partitions of graphs. In Proble`mes combinatoires et the´orie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), volume 260 of Colloq. Internat. CNRS, pages 399–401. CNRS, Paris, 1978.

[Wo´z96] M. Wo´zniak. On the Erd˝s–So´s conjecture. J. Graph Theory, 21(2):229–234, 1996. [Zha11] Y. Zhao. Proof of the (n/2 − n/2 − n/2) conjecture for large n. Electron. J. Combin.,

18(1):Paper 27, 61, 2011.

Institute of Mathematics, Czech Academy of Science. Zitnˇ a´ 25, 110 00, Praha, Czech Republic. The Institute of Mathematics of the Czech Academy of Sciences is supported by RVO:67985840.

E-mail address: honzahladky@gmail.com Institute of Computer Science, Czech Academy of Sciences, Pod Vodarenskou´ vˇeˇz´ı

- 2, 182 07 Prague, Czech Republic. With institutional support RVO:67985807 E-mail address: piguet@cs.cas.cz


R´enyi Institute, Budapest, Hungary E-mail address: miki@renyi.hu

Centro de Modelamiento Matematico,´ Universidad de Chile, Beauchef 851, Santiago

Centro, RM, Chile E-mail address: mstein@dim.uchile.cl Department of Mathematics, Rutgers University, 110 Frelinghuysen Rd., Piscataway,

NJ 08854-8019, USA

