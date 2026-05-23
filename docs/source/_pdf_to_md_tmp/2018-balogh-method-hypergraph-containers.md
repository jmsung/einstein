arXiv:1801.04584v1[math.CO]14Jan2018

THE METHOD OF HYPERGRAPH CONTAINERS

JOZSEF´ BALOGH, ROBERT MORRIS, AND WOJCIECH SAMOTIJ

Abstract. In this survey we describe a recently-developed technique for bounding the number (and controlling the typical structure) of ﬁnite objects with forbidden substructures. This technique exploits a subtle clustering phenomenon exhibited by the independent sets of uniform hypergraphs whose edges are suﬃciently evenly distributed; more precisely, it provides a relatively small family of ‘containers’ for the independent sets, each of which contains few edges. We attempt to convey to the reader a general high-level overview of the method, focusing on a small number of illustrative applications in areas such as extremal graph theory, Ramsey theory, additive combinatorics, and discrete geometry, and avoiding technical details as much as possible.

1. Introduction

Numerous well-studied problems in combinatorics concern families of discrete objects which avoid certain forbidden conﬁgurations, such as the family of H-free graphs1 or the family of sets of integers containing no k-term arithmetic progression. The most classical questions about these families relate to the size and structure of the extremal examples; for example, Tura´n [90] determined the unique Kr-free graph on n vertices with the most edges and Szemere´di [87] proved that every set of integers of positive upper density contains arbitrarily long arithmetic progressions. In recent decades, partly motivated by applications to areas such as Ramsey theory and statistical physics, there has been increasing interest in problems relating to the typical structure of a (e.g., uniformly chosen) member of one of these families and to extremal questions in (sparse) random graphs and random sets of integers. Signiﬁcant early developments in this direction include the seminal results obtained by Erd˝os, Kleitman, and Rothschild [36], who proved that almost all triangle-free graphs are bipartite, by Kleitman and Winston [56], who proved that there are 2Θ(n3/2) C4-free graphs on n vertices, and by Frankl and Ro¨dl [39], who proved that if p ≫ 1/√n, then with high probability every 2-colouring of the edges of G(n,p) contains a monochromatic triangle.

![image 1](<2018-balogh-method-hypergraph-containers_images/imageFile1.png>)

An important recent development in this area was the discovery that, perhaps surprisingly, it is beneﬁcial to consider such problems in the more abstract (and signiﬁcantly more general) setting of independent sets in hypergraphs. This approach was taken with stunning success by Conlon and Gowers [25], Friedgut, Ro¨dl, and Schacht [43], and Schacht [83] in their breakthrough papers on extremal and Ramsey-type results in sparse random sets. To give just one example of the many

![image 2](<2018-balogh-method-hypergraph-containers_images/imageFile2.png>)

JB is partially supported by NSF Grant DMS-1500121 and by the Langan Scholar Fund (UIUC); RM is partially supported by CNPq (Proc. 303275/2013-8), by FAPERJ (Proc. 201.598/2014), and by ERC Starting Grant 680275 MALIG; WS is partially supported by the Israel Science Foundation grant 1147/14.

1A graph is H-free if it does not contain a subgraph isomorphic to H.

important conjectures resolved by their work, let us consider the random variable ex G(n,p),H = max e(G) : H  ⊂ G ⊂ G(n,p) ,

which was ﬁrst studied (in the case H = K3) by Frankl and Ro¨dl [39]. The following theorem was conjectured by Haxell, Kohayakawa, and  Luczak [52, 53] and proved (independently) by Conlon and Gowers [25] and by Schacht [83].

- Theorem 1.1. Let H be a graph with at least two edges and suppose that p ≫ n−1/m2(H), where m2(H) is the so-called 2-density2 of H. Then


1 χ(H) − 1

n 2

ex G(n,p),H = 1 −

+ o(1) p

![image 3](<2018-balogh-method-hypergraph-containers_images/imageFile3.png>)

asymptotically almost surely (a.a.s.), that is, with probability tending to 1 as n → ∞.

It is not hard to show that ex G(n,p),H = 1 + o(1) p n2 a.a.s. if n−2 ≪ p ≪ n−1/m2(H) and so the assumption on p in Theorem 1.1 is optimal. We remark that in the case when H is a clique even more precise results are known, due to work of DeMarco and Kahn [30, 31], who proved that if p ≫ n−1/m2(H)(log n)2/(r+1)(r−2), then with high probability the largest Kr+1-free subgraph of G(n,p) is r-partite, which is again essentially best possible. We refer the reader to an excellent recent survey of Ro¨dl and Schacht [74] for more details on extremal results in sparse random sets.

In this survey we will describe an alternative approach to the problem of understanding the family of independent sets in a hypergraph, whose development was inspired by the work in [25, 43, 83] and also strongly inﬂuenced by that of Kleitman and Winston [56] and Sapozhenko [77, 78, 79]. This technique, which was developed independently by the authors of this survey [13] and by Saxton and Thomason [81], has turned out to be surprisingly powerful and ﬂexible. It allows one to prove enumerative, structural, and extremal results (such as Theorem 1.1) in a wide variety of settings. It is known as the method of hypergraph containers.

To understand the essence of the container method, it is perhaps useful to consider as an illustrative example the family Fn(K3) of triangle-free graphs on (a given set of) n vertices. Note that the number of such graphs is at least 2⌊n2/4⌋, since every bipartite graph is triangle-free.3 However, it turns out that there exists a vastly smaller family Gn of graphs on n vertices, of size nO(n3/2), that forms a set of containers for Fn(K3), which means that for every H ∈ Fn(K3), there exists a G ∈ Gn such that H ⊂ G. A remarkable property of this family of containers is that each graph

- G ∈ Gn is ‘almost triangle-free’ in the sense that it contains ‘few’ triangles. It is not diﬃcult to use this family of containers, together with a suitable ‘supersaturation’ theorem, to prove Theorem 1.1


in the case H = K3 or to show, using a suitable ‘stability’ theorem, that almost all triangle-free graphs are ‘almost bipartite’. We will discuss these two properties of the family of triangle-free graphs in much more detail in Section 2.

In order to generalize this container theorem for triangle-free graphs, it is useful to ﬁrst restate it in the language of hypergraphs. To do so, consider the 3-uniform hypergraph H with vertex set

![image 4](<2018-balogh-method-hypergraph-containers_images/imageFile4.png>)

2To be precise, m2(H) = max v e((FF))−−12 : F ⊂ H, v(F) 3 . 3In particular, every subgraph of the complete bipartite graph with n vertices and ⌊n2/4⌋ edges is triangle-free.

![image 5](<2018-balogh-method-hypergraph-containers_images/imageFile5.png>)

V (H) = E(Kn) and edge set E(H) = {e1,e2,e3} ⊂ E(Kn) : e1,e2,e3 form a triangle .

We shall refer to H as the ‘hypergraph that encodes triangles’ and emphasize that (somewhat confusingly) the vertices of this hypergraph are the edges of the complete graph Kn. Note that Fn(K3) is precisely the family I(H) of independent sets of H, so we may rephrase our container theorem for triangle-free graphs as follows:

“There exists a relatively small family C of subsets of V (H), each containing only few edges of H, such that every independent set I ∈ I(H) is contained in some member of C.”

There is nothing special about the ﬁne structure of the hypergraph encoding triangles that makes the above statement true. On the contrary, the method of containers allows one to prove that a similar phenomenon holds for a large class of k-uniform hypergraphs, for each k ∈ N. In the case k = 3, a suﬃcient condition is the following assumption on the distribution of the edges of a 3-uniform hypergraph H with average degree d: each vertex of H has degree at most O(d) and each pair of vertices lies in at most O(√d) edges of H. For the hypergraph that encodes triangles, both conditions are easily satisﬁed, since each edge of Kn is contained in exactly n − 2 triangles and each pair of edges is contained in at most one triangle. The conclusion of the container lemma (see Sections 2 and 3) is that each independent set I in a 3-uniform hypergraph H satisfying these conditions has a ﬁngerprint S ⊂ I of size O v(H)/

![image 6](<2018-balogh-method-hypergraph-containers_images/imageFile6.png>)

√

![image 7](<2018-balogh-method-hypergraph-containers_images/imageFile7.png>)

d that is associated with a set X(S) of size Ω v(H) which is disjoint from I. The crucial point is that the set X(S) depends only on S (and not on I) and therefore the number of sets X(S) is bounded from above by the number of subsets of the vertex set V (H) of size O v(H)/

√

![image 8](<2018-balogh-method-hypergraph-containers_images/imageFile8.png>)

d . In particular, each independent set of H is contained in one of at most v(H)O(v(H)/

√

![image 9](<2018-balogh-method-hypergraph-containers_images/imageFile9.png>)

d) sets of size at most (1−δ)v(H), for some constant δ > 0. By iterating this process, that is, by applying the container lemma repeatedly to the subhypergraphs induced by the containers obtained in earlier applications, one can easily prove the container theorem for triangle-free graphs stated (informally) above.

Although the hypergraph container lemma (see Section 3) was discovered only recently (see [13, 81]), several theorems of the same ﬂavour (though often in very speciﬁc settings) appeared much earlier in the literature. The earliest container-type argument of which we are aware appeared (implicitly) over 35 years ago in the work of Kleitman and Winston on bounding the number of lattices [54] and of C4-free graphs [56], which already contained some of the key ideas needed for the proof in the general setting; see [76] for details. Nevertheless, it was not until almost 20 years later that Sapozhenko [77, 78, 79] made a systematic study of containers for independent sets in graphs (and coined the name containers). Around the same time, Green and Ruzsa [50] obtained (using Fourier analysis) a container theorem for sum-free subsets of Z/pZ.

More recently, Balogh and Samotij [15, 16] generalized the method of [56] to count Ks,t-free graphs, using what could be considered to be the ﬁrst container theorem for hypergraphs of uniformity larger than two. Finally, Alon, Balogh, Morris, and Samotij [6, 7] proved a general container theorem for 3-uniform hypergraphs and used it to prove a sparse analogue of the Cameron–Erd˝os

conjecture. Around the same time, Saxton and Thomason [80] developed a simpler version of the method and applied it to the problem of bounding the list chromatic number of hypergraphs. In particular, the articles [6] and [80] can be seen as direct predecessors of [13] and [81].

The rest of this survey is organised as follows. In Section 2, we warm up by stating a container lemma for 3-uniform hypergraphs, giving three simple applications to problems involving trianglefree graphs and a more advanced application to a problem in discrete geometry that was discovered recently by Balogh and Solymosi [17]. Next, in Section 3, we state the main container lemma and provide some additional motivation and discussion of the statement and in Section 4 we describe an application to counting H-free graphs. Finally, in Sections 5–8, we state and discuss a number of additional applications, including to multi-coloured structures (e.g., metric spaces), asymmetric structures (e.g., sparse members of a hereditary property), hypergraphs of unbounded uniformity (e.g., induced Ramsey numbers, ε-nets), number-theoretic structures (e.g., Sidon sets, sum-free sets, sets containing no k-term arithmetic progression), sharp thresholds in Ramsey theory, and probabilistic embedding in sparse graphs.

2. Basic applications of the method

In this section we will provide the reader with a gentle introduction to the container method, focusing again on the family of triangle-free graphs. In particular, we will state a version of the container lemma for 3-uniform hypergraphs and explain (without giving full details) how to deduce from it bounds on the largest size of a triangle-free subgraph of the random graph G(n,p), statements about the typical structure of a (sparse) triangle-free graph, and how to prove that every r-colouring of the edges of G(n,p) contains a monochromatic triangle. To give a simple demonstration of the ﬂexibility of the method, we will also describe a slightly more complicated application to a problem in discrete geometry.

In order to state the container lemma, we need a little notation. Given a hypergraph H, let us write ∆ℓ(H) for the maximum degree of a set of ℓ vertices of H, that is,

∆ℓ(H) = max dH(A) : A ⊂ V (H), |A| = ℓ , where dH(A) = B ∈ E(H) : A ⊂ B , and I(H) for the collection of independent sets of H.

The hypergraph container lemma for 3-uniform hypergraphs. For every c > 0, there exists δ > 0 such that the following holds. Let H be a 3-uniform hypergraph with average degree d δ−1 and suppose that

√

![image 10](<2018-balogh-method-hypergraph-containers_images/imageFile10.png>)

∆1(H) c · d and ∆2(H) c ·

d. Then there exists a collection C of subsets of V (H) with

v(H) v(H)/√d such that

|C|

![image 11](<2018-balogh-method-hypergraph-containers_images/imageFile11.png>)

- (a) for every I ∈ I(H), there exists C ∈ C such that I ⊂ C,
- (b) |C| (1 − δ)v(H) for every C ∈ C.


In order to help us understand the statement of this lemma, let us apply it to the hypergraph

- H that encodes triangles in Kn, deﬁned in the Introduction. Recall that this hypergraph satisﬁes


n 2

v(H) =

, ∆2(H) = 1, and dH(v) = n − 2

for every v ∈ V (H). We may therefore apply the container lemma to H, with c = 1, to obtain a collection C of nO(n3/2) subsets of E(Kn) (that is, graphs on n vertices) with the following properties:

- (a) Every triangle-free graph is a subgraph of some C ∈ C.
- (b) Each C ∈ C has at most (1 − δ)e(Kn) edges.


Now, if there exists a container C ∈ C with at least εn3 triangles, then take each such C and apply the container lemma to the subhypergraph H[C] of H induced by C, i.e., the hypergraph that encodes triangles in the graph C. Note that the average degree of H[C] is at least 6εn, since each triangle in C corresponds to an edge of H[C] and v(H[C]) = |C| e(Kn). Since (trivially) ∆ℓ(H[C]) ∆ℓ(H), it follows that we can apply the lemma with c = 1/ε and replace C by the collection of containers for I(H[C]) given by the lemma.

Let us iterate this process until we obtain a collection C of containers, each of which has fewer than εn3 triangles. How large is the ﬁnal family C that we obtain? Note that we apply the lemma only to hypergraphs with at most n2 vertices and average degree at least 6εn and therefore produce at most nO(n3/2) new containers in each application, where the implicit constant depends only on ε. Moreover, each application of the lemma shrinks a container by a factor of 1−δ, so after a bounded (depending on ε) number of iterations every container will have fewer than εn3 triangles (since ∆1(H) < n, then every graph with at most εn2 edges contains fewer than εn3 triangles). The above argument yields the following container theorem for triangle-free graphs.

- Theorem 2.1. For each ε > 0, there exists C > 0 such that the following holds. For each n ∈ N, there exists a collection G of graphs on n vertices, with


|G| nCn3/2, (1) such that

- (a) each G ∈ G contains fewer than εn3 triangles;
- (b) each triangle-free graph on n vertices is contained in some G ∈ G.


In order to motivate the statement of Theorem 2.1, we will next present three simple applications: bounding the largest size of a triangle-free subgraph of the random graph G(n,p), determining the typical structure of a (sparse) triangle-free graph, and proving that G(n,p) cannot be partitioned into a bounded number of triangle-free graphs.

- 2.1. Mantel’s theorem in random graphs. The oldest result in extremal graph theory, which states that every graph on n vertices with more than n2/4 edges contains a triangle, was proved by Mantel [64] in 1907. The corresponding problem in the random graph G(n,p) was ﬁrst studied by Frankl and Ro¨dl [39], who proved the following theorem (cf. Theorem 1.1).


Theorem 2.2. For every α > 0, there exists C > 0 such that the following holds. If p C/√n, then a.a.s. every subgraph G ⊂ G(n,p) with

![image 12](<2018-balogh-method-hypergraph-containers_images/imageFile12.png>)

- 1

![image 13](<2018-balogh-method-hypergraph-containers_images/imageFile13.png>)

- 2


n 2

e(G)

+ α p

contains a triangle.

As a simple ﬁrst application of Theorem 2.1, let us use it to prove Theorem 2.2 under the marginally stronger assumption that p ≫ log n/√n. The proof exploits the following crucial property of n-vertex graphs with o(n3) triangles: each such graph has at most 12 + o(1) n2 edges. This statement is made rigorous in the following supersaturation lemma for triangles, which can be proved by simply applying Mantel’s theorem to each induced subgraph of G with O(1) vertices. Lemma 2.3 (Supersaturation for triangles). For every δ > 0, there exists ε > 0 such that the following holds. If G is a graph on n vertices with

![image 14](<2018-balogh-method-hypergraph-containers_images/imageFile14.png>)

![image 15](<2018-balogh-method-hypergraph-containers_images/imageFile15.png>)

then G has at least εn3 triangles.

e(G)

1 4

+ δ n2,

![image 16](<2018-balogh-method-hypergraph-containers_images/imageFile16.png>)

Applying Lemma 2.3 with δ = α/2 and Theorem 2.1 with ε = ε(δ) given by the lemma, we obtain a family of containers G such that each G ∈ G has fewer than εn3 triangles and thus

n 2

- 1 + α

![image 17](<2018-balogh-method-hypergraph-containers_images/imageFile17.png>)

- 2


e(G)

for every G ∈ G. Since every triangle-free graph is a subgraph of some container, if G(n,p) contains a triangle-free graph with m edges, then in particular e G ∩ G(n,p) m for some G ∈ G. Noting that e G ∩ G(n,p) ∼ Bin e(G),p , standard estimates on the tail of the binomial distribution yield

- 1

![image 18](<2018-balogh-method-hypergraph-containers_images/imageFile18.png>)

- 2


n 2

e−βpn2,

P e G ∩ G(n,p)

+ α p

for some constant β = β(α) > 0. Therefore, taking a union bound over all containers G ∈ G and using the bound (1), we have (using the notation of Theorem 1.1)

- 1

![image 19](<2018-balogh-method-hypergraph-containers_images/imageFile19.png>)

- 2


n 2

nO(n3/2) · e−βpn2 → 0 (2)

P ex G(n,p),K3

+ α p

as n → ∞, provided that p ≫ log n/√n. This gives the conclusion of Theorem 2.2 under a slightly stronger assumption on p. In Section 3, we show how to remove the extra factor of log n.

![image 20](<2018-balogh-method-hypergraph-containers_images/imageFile20.png>)

We remark here that Theorem 2.2, as well as numerous results of this type that now exist in the literature, cannot be proved using standard ﬁrst moment estimates. Indeed, since there are at least ⌊n2m/4⌋ triangle-free graphs with n vertices and m edges, then letting Xm denote the number of such graphs that are contained in G(n,p), we have

E[Xm] pm ⌊n2/4⌋ m

=

(e/2 + o(1))p n2 m

![image 21](<2018-balogh-method-hypergraph-containers_images/imageFile21.png>)

m

≫ 1

if m e/2 + o(1) p n2 = o(n2). This means that a ﬁrst moment estimate would yield an upper bound on ex G(n,p),K3 that is worse than the trivial upper bound of 1 + o(1) p n2 .

- 2.2. The typical structure of a sparse triangle-free graph. A seminal theorem of Erd˝os, Kleitman, and Rothschild [36] states that almost all triangle-free graphs are bipartite. Our second application of Theorem 2.1 is the following approximate version of this theorem for sparse graphs, ﬁrst proved by  Luczak [63]. Let us say that a graph G is t-close to bipartite if there exists a bipartite subgraph G′ ⊂ G with e(G′) e(G) − t.


Theorem 2.4. For every α > 0, there exists C > 0 such that the following holds. If m Cn3/2, then almost all triangle-free graphs with n vertices and m edges are αm-close to bipartite.

We will again (cf. the previous subsection) prove this theorem under the marginally stronger assumption that m ≫ n3/2 log n. To do so, we will need a ﬁner characterisation of graphs with o(n3) triangles that takes into account whether or not a graph is close to bipartite. Proving such a result is less straightforward than Lemma 2.3; for example, one natural proof combines the triangle removal lemma of Ruzsa and Szemere´di [75] with the classical stability theorem of Erd˝os and Simonovits [33, 86]. However, an extremely simple, beautiful, and elementary proof was given recently by Fu¨redi [45] (see also [8]).

Lemma 2.5 (Robust stability for triangles). For every δ > 0, there exists ε > 0 such that the following holds. If G is a graph on n vertices with

e(G)

- 1

![image 22](<2018-balogh-method-hypergraph-containers_images/imageFile22.png>)

- 2 − ε


n 2

,

then either G is δn2-close to bipartite or G contains at least εn3 triangles.

Applying Lemma 2.5 with δ = δ(α) > 0 suﬃciently small and Theorem 2.1 with ε = ε(δ) given by the lemma, we obtain a family of containers G such that every G ∈ G is either δn2-close to bipartite or

- 1

![image 23](<2018-balogh-method-hypergraph-containers_images/imageFile23.png>)

- 2 − ε


n 2

e(G)

. (3)

Let us count those triangle-free graphs H with n vertices and m edges that are not αm-close to bipartite; note that each such graph is a subgraph of some container G ∈ G.

Suppose ﬁrst that G satisﬁes (3); in this case we simply use the trivial bound

e(G) m

- 1

![image 24](<2018-balogh-method-hypergraph-containers_images/imageFile24.png>)

- 2 − ε n2


m

(1 − ε)m

n2/4 m

for the number of choices for H ⊂ G. On the other hand, if G is δn2-close to bipartite, then there is some bipartite G′ ⊂ G with e(G′) e(G) − δn2. Since e(H ∩ G′) (1 − α)m by our assumption on H, we bound the number of choices for H by

e(G) − e(G′) αm

e(G) (1 − α)m

δn2 αm

n 2

(1 − α)m

2−m

n2/4 m

,

provided that δ = δ(α) is suﬃciently small. Summing over all choices of G ∈ G and using (1), it follows that if m ≫ n3/2 log n, then there are at most

n2/4 m ≪

⌊n2/4⌋ m

nO(n3/2) · (1 − ε)m

triangle-free graphs H with n vertices and m edges that are not αm-close to bipartite. However, there are clearly at least ⌊nm2/4⌋ triangle-free graphs H with n vertices and m edges, since every bipartite graph is triangle-free, so the conclusion of Theorem 2.4 holds when m ≫ n3/2 log n. We again postpone a discussion of how to remove the unwanted factor of log n to Section 3.

- 2.3. Ramsey properties of sparse random graphs. A folklore fact that is presented in each introduction to Ramsey theory states that every 2-colouring of the edges of K6 contains a monochromatic triangle. With the aim of constructing a small K4-free graph that has the same property, Frankl and Ro¨dl [39] proved that if p ≫ 1/√n, then a.a.s. every 2-colouring of the edges of G(n,p) contains a monochromatic triangle. Ramsey properties of random graphs were later thorougly investigated by Ro¨dl and Rucin´ski [70, 71, 72]. The following theorem is the main result of [71].


![image 25](<2018-balogh-method-hypergraph-containers_images/imageFile25.png>)

Theorem 2.6. For every r ∈ N, there exists C > 0 such that the following holds. If p ≫ C/√n, then a.a.s. every r-colouring of the edges of G(n,p) contains a monochromatic triangle.

![image 26](<2018-balogh-method-hypergraph-containers_images/imageFile26.png>)

We will present a simple proof of this theorem that was discovered recently by Nenadov and Steger [69]. For the sake of simplicity, we will again use the marginally stronger assumption that p ≫ log n/√n. The proof exploits the following property of n-vertex graphs with o(n3) triangles: the union of any bounded number of such graphs cannot cover a 1−o(1) -proportion of the edges of Kn. This property is a straightforward corollary of the following lemma, which can be proved by applying Ramsey’s theorem to the colourings induced by all subsets of V (Kn) of size O(1).

![image 27](<2018-balogh-method-hypergraph-containers_images/imageFile27.png>)

Lemma 2.7. For every r ∈ N, there exist n0 and ε > 0 such that for all n n0, every (r + 1)colouring of the edges of Kn contains at least (r + 1)εn3 monochromatic triangles.

Applying Theorem 2.1 with ε = ε(r) given by the lemma, we obtain a family of containers G such that every G ∈ G has fewer than εn3 triangles. If G(n,p) does not have the desired Ramsey property, then there are triangle-free graphs H1,... ,Hr such that H1∪...∪Hr = G(n,p). It follows that G(n,p) ⊂ G1 ∪...∪Gr, where each Gi ∈ G is a container for Hi. Since each Gi has fewer than εn3 triangles, then Lemma 2.7 implies that Kn \ (G1 ∪ ... ∪ Gr) contains at least εn3 triangles.4 Since each edge of Kn belongs to fewer than n triangles, we must have e Kn\(G1∪...∪Gr) εn2. Consequently, for each ﬁxed G1,... ,Gr ∈ G,

P G(n,p) ⊂ G1 ∪ ... ∪ Gr = (1 − p)e(Kn\(G1∪···∪Gr)) (1 − p)εn2 e−εpn2. Taking a union bound over all r-tuples of containers, we conclude that

P G(n,p) admits a ‘bad’ r-colouring nO(n3/2) · e−εpn2 → 0

![image 28](<2018-balogh-method-hypergraph-containers_images/imageFile28.png>)

4To see this, consider an (r + 1)-colouring of the edges of Kn that assigns to each edge e ∈ G1 ∪ . . . ∪ Gr some colour i such that e ∈ Gi and assigns colour r + 1 to all edges of Kn \ (G1 ∪ . . . ∪ Gr).

- as n → ∞, provided that p ≫ log n/√n. As before, the unwanted factor of log n can be removed with a somewhat more careful analysis that we shall discuss in Section 3.


![image 29](<2018-balogh-method-hypergraph-containers_images/imageFile29.png>)

- 2.4. An application in discrete geometry. In order to give some idea of the ﬂexibility of the container method, we will next present a somewhat more elaborate application of the container lemma for 3-uniform hypergraphs, which was discovered recently by Balogh and Solymosi [17], to the following question posed by Erd˝os [34]. Given n points in the Euclidean plane R2, with at most three on any line, how large a subset are we guaranteed to ﬁnd in general position (i.e., with at most two on any line)? Fu¨redi [44] proved that one can always ﬁnd such a subset of size Ω √nlog n and gave a construction (which relied on the density Hales–Jewett theorem of Furstenberg and Katznelson [46]) in which the largest such set has size o(n). Using the method of hypergraph containers, Balogh and Solymosi [17] obtained the following stronger upper bound.


![image 30](<2018-balogh-method-hypergraph-containers_images/imageFile30.png>)

Theorem 2.8. There exists a set S ⊂ R2 of size n, containing no four points on a line, such that every subset of S of size n5/6+o(1) contains three points on a line.

The key idea in [17] is to ﬁrst construct a set P of points that contains ‘few’ collinear quadruples, but such that every ‘large’ subset of P contains ‘many’ collinear triples. Then a random subset R of P of a carefully chosen density will typically contain only o(|R|) collinear quadruples, since the density is not too large and there are few collinear quadruples. On the other hand, every subset of R with more than |R|5/6+o(1) elements will still contain a collinear triple; this follows from the hypergraph container lemma, as large sets contain many collinear triples and the density is not too small. Removing one element from each collinear quadruple in R gives the desired set A.

Formally, we ﬁrst deﬁne the following 3-uniform hypergraph H. We let V (H) = [m]3 (so the vertices are lattice points in R3) and let E(H) be the collection of triples of points that lie on a common line. Thus, a subset of V (H) is in general position if and only if it is an independent set of H. The following lemma was proved in [17].

Lemma 2.9 (Supersaturation for collinear triples). For every 0 < γ < 1/2 and every S ⊂ [m]3 of size at least m3−γ, there exist at least m6−4γ−o(1) collinear triples of points in S.

We now repeatedly apply the hypergraph container lemma for 3-uniform hypergraphs to subhypergraphs of H. Suppose that s m8/3+o(1) and let S ⊂ [m]3 be an arbitrary s-element set. Lemma 2.9 gives

e H[S] s4/m6+o(1) and ∆2 H[S] ∆2(H) m. Moreover, it is not diﬃcult to deduce that there exists a subhypergraph H′ ⊂ H[S] with v(H′) = |S| = s, e(H′) = s4/m6+o(1), and ∆1(H′) = O e(H′)/v(H′) .

We may therefore apply the container lemma for 3-uniform hypergraphs to H′ to obtain a collection C of at most exp m3+o(1)/√s subsets of S with the following properties:

![image 31](<2018-balogh-method-hypergraph-containers_images/imageFile31.png>)

- (a) Every set of points of S in general position is contained in some C ∈ C,
- (b) Each C ∈ C has size at most (1 − δ)|S|.


Starting with S = [m]3 and iterating this process for O(log m) steps, we obtain the following container theorem for sets of points in general position.

Theorem 2.10. For each m ∈ N, there exists a collection C of subsets of [m]3 with

|C| exp m5/3+o(1) (4) such that

- (a) |C| m8/3+o(1) for each C ∈ C;
- (b) each set of points of [m]3 in general position is contained in some C ∈ C.


Now, let p = m−1+o(1) and consider a p-random subset R ⊂ [m]3, that is, each element of [m]3 is included in R independently at random with probability p. Since [m]3 contains m6+o(1) sets of four collinear points5, it follows that, with high probability, |R| = pm3+o(1) = m2+o(1) and R contains p4m6+o(1) = o(|R|) collinear 4-tuples. Moreover, since |C| m8/3+o(1) for each C ∈ C, it follows from (4) and standard estimates on the tail of the binomial distribution that with high probability we have |R ∩ C| m5/3+o(1) for every C ∈ C. In particular, removing one element from each collinear 4-tuple in R yields a set A ⊂ [m]3 of size m2+o(1) with no collinear 4-tuple and containing no set of points in general position of size larger than m5/3+o(1). Finally, project the points of A to the plane in such a way that collinear triples remain collinear, and no new collinear triple is created. In this way, we obtain a set of n = m2+o(1) points in the plane, no four of them on a line, such that no set of size greater than n5/6+o(1) = m5/3+o(1) is in general position, as required.

3. The key container lemma

In this section, we state a container lemma for hypergraphs of arbitrary uniformity. The version of the lemma stated below, which comes from [65], diﬀers from the statement originally proved by the authors of this survey [13, Proposition 3.1] only in that the dependencies between the various constants have been made more explicit here; a careful analysis of the proof of [13, Proposition 3.1] will yield this slightly sharper statement.6 Let us recall that for a hypergraph H and an integer ℓ, we write ∆ℓ(H) for the maximum degree of a set of ℓ vertices of H, that is,

∆ℓ(H) = max dH(A) : A ⊂ V (H), |A| = ℓ ,

where dH(A) = B ∈ E(H) : A ⊂ B , and I(H) for the collection of independent sets of H. The lemma states, roughly speaking, that each independent set I in a uniform hypergraph H can be assigned a ﬁngerprint S ⊂ I in such a way that all sets with the same ﬁngerprint are contained in a single set C = f(S), called a container, whose size is bounded away from v(H). More importantly, the sizes of these ﬁngerprints (and hence also the number of containers) can be bounded from above (in an optimal way!) by basic parameters of H.

![image 32](<2018-balogh-method-hypergraph-containers_images/imageFile32.png>)

5This is because there are O(m6/t4) lines in R3 that contain more than t points of [m]3. 6A complete proof of the version of the container lemma stated here can be found in [65].

The hypergraph container lemma. Let k ∈ N and set δ = 2−k(k+1). Let H be a k-uniform hypergraph and suppose that

ℓ−1 e(H) r

b v(H)

∆ℓ(H)

(5)

![image 33](<2018-balogh-method-hypergraph-containers_images/imageFile33.png>)

![image 34](<2018-balogh-method-hypergraph-containers_images/imageFile34.png>)

for some b,r ∈ N and every ℓ ∈ {1,... ,k}. Then there exists a collection C of subsets of V (H) and a function f : P V (H) → C such that:

- (a) for every I ∈ I(H), there exists S ⊂ I with |S| (k − 1)b and I ⊂ f(S);
- (b) |C| v(H) − δr for every C ∈ C.


The original statement of the container lemma [13, Proposition 3.1] had r = v(H)/c for some constant c, since this choice of parameters is required in most standard applications. In particular, the simple container lemma for 3-uniform hypergraphs presented in Section 2 is easily derived from the above statement by letting b = v(H)/(2

√

![image 35](<2018-balogh-method-hypergraph-containers_images/imageFile35.png>)

d) and r = v(H)/(6c), where d = 3e(H)/v(H) is the average degree of H. There are, however, arguments that beneﬁt from setting r = o(v(H)); we present one of them in Section 5.

Even though the property |C| v(H) − δr that is guaranteed for all containers C ∈ C seems rather weak at ﬁrst sight, it can be easily strengthened with repeated applications of the lemma. In particular, if for some hypergraph H, condition (5) holds (for all ℓ) with some b = o(v(H)) and r = Ω(v(H)), then recursively applying the lemma to subhypergraphs of H induced by all the containers C for which e(H[C]) εe(H) eventually produces a collection C of containers indexed by sets of size O(b) such that e(H[C]) < εe(H) for every C ∈ C. This is precisely how (in Section 2) we derived Theorem 2.1 from the container lemma for 3-uniform hypergraphs. For a formal argument showing how such a family of ‘tight’ containers may be constructed, we refer the reader to [13].

One may thus informally say that the hypergraph container lemma provides a covering of the family of all independent sets of a uniform hypergraph with ‘few’ sets that are ‘almost independent’. In many natural settings, these almost independent sets closely resemble truly independent sets. In some cases, this is a straightforward consequence of corresponding removal lemmas. A more fundamental reason is that many sequences of hypergraphs Hn of interest possess the following selfsimilarity property: For all (or many) pairs m and n with m < n, the hypergraph Hn admits a very uniform covering by copies of Hm. For example, this is the case when Hn is the hypergraph encoding triangles in Kn, simply because every m-element set of vertices of Kn induces Km. Such selfsimilarity enables one to use elementary averaging arguments to characterise almost independent sets; for example, the standard proof of Lemma 2.3 uses such an argument.

The fact that the ﬁngerprint S of each independent set I ∈ I(H) is a subset of I is not merely a by-product of the proof of the hypergraph container lemma. On the contrary, it is an important property of the family of containers that can be often exploited to make union bound arguments tighter. This is because each I ∈ I(H) is sandwiched between S and f(S) and consequently when enumerating independent sets one may use a union bound over all ﬁngerprints S and enumerate only over the sets I \ S (which are contained in f(S)). In particular, such ﬁner arguments can be used to remove the superﬂuous logarithmic factor from the assumptions of the proofs outlined in Section 2. For example, in the proof of Theorem 2.2 presented in Section 2.1, the ﬁngerprints of

triangle-free subgraphs of Kn form a family S of n-vertex graphs, each with at most Cεn3/2 edges. Setting m = 2 1 + α p n2 , this allows us to replace (2) with the following estimate:

![image 36](<2018-balogh-method-hypergraph-containers_images/imageFile36.png>)

P ex G(n,p),K3 m

P S ⊂ G(n,p) and e f(S) \ S ∩ G(n,p) m − |S| . (6)

S∈S

Since the two events in the right-hand side of (6) concern the intersections of G(n,p) with two disjoint sets of edges of Kn, they are independent. If p ≫ n−1/2, then |S| ≪ p n2 and consequently, recalling that e(f(S)) 1+2α n2 , we may bound the right-hand side of (6) from above by

![image 37](<2018-balogh-method-hypergraph-containers_images/imageFile37.png>)

s

e n2 p s

n 2 s · pse−βpn2

p|S|e−βpn2

e−βpn2 e−βpn2/2

![image 38](<2018-balogh-method-hypergraph-containers_images/imageFile38.png>)

S∈S

s Cεn3/2

s Cεn3/2

for some β = β(α) > 0.

Finally, what is the intuition behind condition (5)? A natural way to deﬁne f(S) for a given (independent) set S is to let f(S) = V (H) \ X(S), where X(S) comprises all vertices v such that A ⊂ S ∪ {v} for some A ∈ E(H). Indeed, every independent set I that contains S must be disjoint from X(S). (In reality, the deﬁnition of X(S) is – and has to be – more complicated than this, and some vertices are placed in X(S) simply because they do not belong to S.) Suppose, for the sake of argument, that S is a random set of b vertices of H. Letting τ = b/v(H), we have

P |A ∩ S| = k − 1 k · τk−1 · e(H). (7)

E |X(S)|

A∈E(H)

Since we want X(S) to have at least δr elements for every ﬁngerprint S, it seems reasonable to require that

k δ · τk−1 ·

e(H) r

∆k(H) = 1

,

![image 39](<2018-balogh-method-hypergraph-containers_images/imageFile39.png>)

![image 40](<2018-balogh-method-hypergraph-containers_images/imageFile40.png>)

which is, up to a constant factor, condition (5) with ℓ = k. For some hypergraphs H however, the ﬁrst inequality in (7) can be very wasteful, since some v ∈ X(S) may have many A ∈ E(H) such

- that A ⊂ S ∪{v}. This can happen if for some ℓ ∈ {1,... ,k −1}, there is an ℓ-uniform hypergraph

- G such that each edge of H contains an edge of G; note that e(G) can be as small as e(H)/∆ℓ(H). Our assumption implies that I(G) ⊂ I(H) and thus, letting Y (S) be the set of all vertices w such


- that B ⊂ S ∪{w} for some B ∈ E(G), we have X(S) ⊂ Y (S). In particular, we want Y (S) to have


- at least δr elements for every ﬁngerprint S of an independent set I ∈ I(G). Repeating (7) with X replaced by Y , H replaced by G, and k replaced by ℓ, we arrive at the inequality


e(H) ∆ℓ(H)

δr ℓ · τℓ−1 · e(G) = ℓ · τℓ−1 ·

,

![image 41](<2018-balogh-method-hypergraph-containers_images/imageFile41.png>)

which is, up to a constant factor, condition (5).

One may further develop the above argument to show that condition (5) is asymptotically optimal, at least when r = Ω(v(H)). Roughly speaking, one can construct k-uniform hypergraphs that have (1−o(1))m v(H) independent m-sets for every m = o(b), where b is minimal so that condition (5) holds, whereas the existence of containers of size at most (1 − δ)v(H) indexed by ﬁngerprints of size o(b) would imply that the number of such sets is at most (1−εm)v(H) for some constant ε > 0.

4. Counting H-free graphs

How many graphs are there on n vertices that do not contain a copy of H? An obvious lower bound is 2ex(n,H), since each subgraph of an H-free graph is also H-free. For non-bipartite graphs, this is not far from the truth. Writing Fn(H) for the family of H-free graphs on n vertices, if χ(H) 3, then

|Fn(H)| = 2(1+o(1))ex(n,H) (8)

- as n → ∞, as was ﬁrst shown by Erd˝os, Kleitman, and Rothschild [36] (when H is a complete graph) and then by Erd˝os, Frankl, and Ro¨dl [35]. For bipartite graphs, on the other hand, the problem is much more diﬃcult. In particular, the following conjecture (ﬁrst stated in print in [56]), which played a major role in the development of the container method, remains open. Conjecture 4.1. For every bipartite graph H that contains a cycle, there exists C > 0 such that


|Fn(H)| 2Cex(n,H) for every n ∈ N.

The ﬁrst signiﬁcant progress on Conjecture 4.1 was made by Kleitman and Winston [56]. Their proof of the case H = C4 of the conjecture introduced (implicitly) the container method for graphs. Nevertheless, it took almost thirty years7 until their theorem was generalized to the case H = Ks,t, by Balogh and Samotij [15, 16], and then (a few years later) to the case H = C2k, by Morris and Saxton [66]. More precisely, it was proved in [16, 66] that

|Fn(Ks,t)| = 2O(n2−1/s) and |Fn(C2k)| = 2O(n1+1/k) for every 2 s t and every k 2, which implies Conjecture 4.1 when t > (s−1)! and k ∈ {2,3,5}, since in these cases it is known that ex(n,Ks,t) = Θ(n2−1/s) and ex(n,C2k) = Θ(n1+1/k).

Very recently, Ferber, McKinley, and Samotij [38], inspired by a similar result of Balogh, Liu, and Sharifzadeh [10] on sets of integers with no k-term arithmetic progression, found a very simple proof of the following much more general theorem.

- Theorem 4.2. Suppose that H contains a cycle. If ex(n,H) = O(nα) for some constant α, then |Fn(H)| = 2O(nα).


Note that Theorem 4.2 resolves Conjecture 4.1 for every H such that ex(n,H) = Θ(nα) for some constant α. Moreover, it was shown in [38] that the weaker assumption that ex(n,H) ≫ n2−1/m2(H)+ε for some ε > 0 already implies that the assertion of Conjecture 4.1 holds for inﬁnitely many n; we refer the interested reader to [38] for details. Let us also note here that, while it is natural to suspect that in fact the stronger bound (8) holds for all graphs H that contain a cycle, this is false for H = C6, as was shown by Morris and Saxton [66]. However, it may still hold for

- H = C4 and it would be very interesting to determine whether or not this is indeed the case.


![image 42](<2018-balogh-method-hypergraph-containers_images/imageFile42.png>)

7An unpublished manuscript of Kleitman and Wilson from 1996 proves that |Fn(C6)| = 2O(ex(n,C6)).

The proof of Theorem 4.2 for general H is somewhat technical, so let us instead sketch the proof in the case H = C4. In this case, the proof combines the hypergraph container lemma stated in the previous section with the following supersaturation lemma.

Lemma 4.3. There exist constants β > 0 and k0 ∈ N such that the following holds for every k k0 and every n ∈ N. Given a graph G with n vertices and k · ex(n,C4) edges, there exists a collection H of at least βk5 · ex(n,C4) copies of C4 in G that satisﬁes:

- (a) Each edge belongs to at most k4 members of H.
- (b) Each pair of edges is contained in at most k2 members of H.


The proof of Lemma 4.3 employs several simple but important ideas that can be used in a variety of other settings, so let us sketch the details. The ﬁrst key idea, which was ﬁrst used in [66], is to build the required family H one C4 at a time. Let us say that a collection H of copies of C4 is legal if it satisﬁes conditions (a) and (b) and suppose that we have already found a legal collection Hm of m copies of C4 in G. Note that we are done if m βk5 · ex(n,C4), so let us assume that the reverse inequality holds and construct a legal collection Hm+1 ⊃ Hm of m + 1 copies of C4 in G.

We claim that there exists a collection Am of βk5 · ex(n,C4) copies of C4 in G, any of which can be added to Hm without violating conditions (a) and (b), that is, such that Hm ∪ {C} is legal for any C ∈ Am. (Let us call these good copies of C4.) Since m < βk5 · ex(n,C4), then at least one element of Am is not already in Hm, so this will be suﬃcient to prove the lemma.

To ﬁnd Am, observe ﬁrst that (by simple double-counting) at most 4βk · ex(n,C4) edges of G lie in exactly k4 members of Hm and similarly at most 6βk3 · ex(n,C4) pairs of edges of G lie in exactly k2 members of Hm. Now, consider a random subset A ⊂ V (G) of size pn, where p = D/k2 for some large constant D. Typically G[A] contains about p2k · ex(n,C4) edges. After removing from G[A] all saturated edges (i.e., those belonging to k4 members of Hm) and one edge from each saturated pair (i.e., pair of edges that is contained in k2 members of Hm), we expect to end up with at least

p2k · ex(n,C4) − 4βp2k · ex(n,C4) − 6βp3k3 · ex(n,C4)

p2k · ex(n,C4) 2

![image 43](<2018-balogh-method-hypergraph-containers_images/imageFile43.png>)

2 · ex(pn,C4)

edges, where the ﬁrst inequality follows since p = D/k2 and β is suﬃciently small, and the second holds because ex(n,C4) = Θ(n3/2) and D is suﬃciently large. Finally, observe that any graph on pn vertices with at least 2 · ex(pn,C4) edges contains at least

ex pn,C4 = Ω p3/2 · ex(n,C4) copies of C4. But each copy of C4 in G was included in the random subgraph G[A] with probability

- at most p4 and hence (with a little care) one can show that there must exist at least Ω p−5/2 · ex(n,C4) copies of C4 in G that avoid all saturated edges and pairs of edges. Since p−5/2 = k5/D5/2 and β is suﬃciently small, we have found βk5 · ex(n,C4) good copies of C4 in G, as required.


We now show how one may combine Lemma 4.3 and the hypergraph container lemma to construct families of containers for C4-free graphs. Let β and k0 be the constants from the statement of

- Lemma 4.3 and assume that G is an n-vertex graph with at least k · ex(n,C4) and at most 2k ·


ex(n,C4) edges, where k k0. Denote by HG the 4-uniform hypergraph with vertex set E(G), whose edges are the copies of C4 in G given by Lemma 4.3. Since

v(HG) = e(G), e(HG) βk5 · ex(n,C4), ∆1(HG) k4, ∆2(HG) k2,

and ∆3(HG) = ∆4(HG) = 1, the hypergraph HG satisﬁes the assumptions of the container lemma with r = βk ·ex(n,C4) and b = 2k−1/3 ·ex(n,C4). Consequently, there exist an absolute constant δ and a collection C of subgraphs of G with the following properties:

(a) every C4-free subgraph of G is contained in some C ∈ C, (b) each C ∈ C has at most (1 − δ)e(G) edges,

and moreover

|C|

3b

s=0

e(G) s

e(G) b

![image 44](<2018-balogh-method-hypergraph-containers_images/imageFile44.png>)

3b

k4b exp 8k−1/3 log k · ex(n,C4) .

Note that we have just replaced a single container for the family of C4-free subgraphs of G (namely G itself) with a small collection of containers for this family, each of which is somewhat smaller than G. Since every C4-free graph with n vertices is contained in Kn, by repeatedly applying this ‘breaking down’ process, we obtain the following container theorem for C4-free graphs.

- Theorem 4.4. There exist constants k0 > 0 and C > 0 such that the following holds for all n ∈ N and k k0. There exists a collection G(n,k) of at most


C log k

exp

k1/3 · ex(n,C4) graphs on n vertices such that

![image 45](<2018-balogh-method-hypergraph-containers_images/imageFile45.png>)

e(G) k · ex(n,C4) for every G ∈ G(n,k) and every C4-free graph on n vertices is a subgraph of some G ∈ G(n,k).

To obtain the claimed upper bound on |G(n,k)|, note that if k · ex(n,C4) n2 then we may take G(n,k) = {Kn}, and otherwise the argument presented above yields

|G(n,k)| G n,k/(1 − δ) · exp 8k−1/3 log k · ex(n,C4) .

In particular, applying Theorem 4.4 with k = k0, we obtain a collection of 2O(ex(n,C4)) containers for C4-free graphs on n vertices, each with O ex(n,C4) edges. This immediately implies that Conjecture 4.1 holds for H = C4. The proof for a general graph H (under the assumption that ex(n,H) = Θ(nα) for some α ∈ (1,2)) is similar, though the details are rather technical.

- 4.1. Tura´n’s problem in random graphs. Given that the problem of estimating |Fn(H)| for bipartite graphs H is notoriously diﬃcult, it should not come as a surprise that determining the


typical value of the Tura´n number ex G(n,p),C4 for bipartite H also poses considerable challenges. Compared to the non-bipartite case, which was essentially solved by Conlon–Gowers [25] and Schacht [83], see Theorem 1.1, the typical behaviour of ex G(n,p),H for bipartite graphs H is much more subtle.

For simplicity, let us restrict our attention to the case H = C4. Recall from Theorem 1.1 that

the typical value of ex G(n,p),C4 changes from 1 + o(1) p n2 to o(pn2) when p = Θ(n−2/3), as was ﬁrst proved by Haxell, Kohayakawa, and  Luczak [53]. However, already several years earlier

Fu¨redi [44] used the method of Kleitman and Winston [56] to prove8 the following much ﬁner estimates of this extremal number for p somewhat above the threshold.

- Theorem 4.5. Asymptotically almost surely,

ex G(n,p),C4 =

 



1 + o(1) p n2 if n−1 ≪ p ≪ n−2/3, n4/3(log n)O(1) if n−2/3 p n−1/3(log n)4, Θ √p · n3/2 if p n−1/3(log n)4.

![image 46](<2018-balogh-method-hypergraph-containers_images/imageFile46.png>)

We would like to draw the reader’s attention to the (somewhat surprising) fact that in the middle range n−2/3+o(1) p n−1/3+o(1), the typical value of ex G(n,p),C4 stays essentially constant. A similar phenomenon has been observed in random Tura´n problems for other forbidden bipartite graphs (even cycles [58, 66] and complete bipartite graphs [66]) as well as Tura´n-type problems in additive combinatorics [27, 28]. It would be very interesting to determine whether or not a similar ‘long ﬂat segment’ appears in the graph of p  → ex G(n,p),H for every bipartite graph H. We remark that the lower bound in the middle range is given (very roughly speaking) by taking a random subgraph of G(n,p) with density n−2/3+o(1) and then ﬁnding9 a large C4-free subgraph of this random graph; the lower bound in the top range is given by intersecting G(n,p) with a suitable blow-up of an extremal C4-free graph and destroying any C4s that occur; see [58, 66] for details.

Even though Theorem 4.4 immediately implies that ex G(n,p),C4 = o(pn2) if p ≫ n−2/3 log n, it is not strong enough to prove Theorem 4.5. A stronger container theorem for C2ℓ-free graphs (based on a supersaturation lemma that is sharper than Lemma 4.3) was obtained in [66]. In the case ℓ = 2, the statement is as follows.

- Theorem 4.6. There exist constants k0 > 0 and C > 0 such that the following holds for all n ∈ N and k0 k n1/6/log n. There exists a collection G(n,k) of at most


C log k

exp

k · ex(n,C4) graphs on n vertices such that

![image 47](<2018-balogh-method-hypergraph-containers_images/imageFile47.png>)

e(G) k · ex(n,C4) for every G ∈ G(n,k) and every C4-free graph on n vertices is a subgraph of some G ∈ G(n,k).

Choosing k to be a suitable function of p, it is straightforward to use Theorem 4.6 to prove a slightly weaker version of Theorem 4.5, with an extra factor of log n in the upper bound on ex G(n,p),C4 . As usual, this logarithmic factor can be removed via a more careful application of

![image 48](<2018-balogh-method-hypergraph-containers_images/imageFile48.png>)

- 8To be precise, Fu¨redi proved that, if m 2n4/3(log n)2, then there are at most (4n3/m2)m C4-free graphs with n vertices and m edges, which implies the upper bounds in Theorem 4.5. For the lower bounds, see [58, 66].
- 9One easy way to do this is simply to remove one edge from each copy of C4. A more eﬃcient method, used by Kohayakawa, Kreuter, and Steger [58] to improve the lower bound by a polylogarithmic factor, utilizes a version of the general result of [1] on independent sets in hypergraphs obtained in [32]; see also [38].


the container method, using the fact that the ﬁngerprint of an independent set is contained in it, cf. the discussion in Section 3; see [66] for the details. However, we are not able to determine the correct power of log n in ex G(n,p),C4 in the middle range n−2/3+o(1) ≪ p ≪ n−1/3+o(1) and we consider this to be an important open problem. It would also be very interesting to prove similarly sharp container theorems for other bipartite graphs H.

5. Containers for multicoloured structures

All of the problems that we have discussed so far, and many others, are naturally expressed as questions about independent sets in various hypergraphs. There are, however, questions of a very similar ﬂavour that are not easily described in this way but are still amenable to the container method. As an example, consider the problem of enumerating large graphs with no induced copy of a given graph H. We shall say that a graph G is induced-H-free if no subset of vertices of G induces a subgraph isomorphic to H. As it turns out, it is beneﬁcial to think of an n-vertex graph G as the characteristic function of its edge set. A function g: E(Kn) → {0,1} is the characteristic function of an induced-H-free graph if and only if for every set W of v(H) vertices of Kn, the restriction of g to the set of pairs of vertices of W is not the characteristic function of the edge set of H. In particular, viewing g as the set of pairs (e,g(e)) : e ∈ E(Kn) , we see that if g represents an induced-H-free graph, then it is an independent set in the v(2H) -uniform hypergraph H with vertex set E(Kn) × {0,1} whose edges are the characteristic functions of all copies of H in Kn; formally, for every injection ϕ: V (H) → V (Kn), the set

ϕ(u)ϕ(v),1 : uv ∈ E(H) ∪ ϕ(u)ϕ(v),0 : uv ∈/ E(H)

is an edge of H. Even though the converse statement is not true and not every independent set of H corresponds to an induced-H-free graph, since we are usually interested in bounding the number of such graphs from above, the above representation can be useful. In particular, Saxton

- and Thomason [81] applied the container method to the hypergraph H described above to reprove the following analogue of (8), which was originally obtained by Alekseev [2] and by Bollob´s and


Thomason [20, 21]. Letting Fnind(H) denote the family of all induced-H-free graphs with vertex set {1,... ,n}, we have

|Fnind(H)| = 2(1−1/col(H))(n2)+o(n2), where col(H) is the so-called colouring number10 of H.

This idea of embedding non-monotone properties (such as the family of induced-H-free graphs) into the family of independent sets of an auxiliary hypergraph has been used in several other works. In particular, Ku¨hn, Osthus, Townsend, and Zhao [62] used it to describe the typical structure of oriented graphs without a transitive tournament of a given order. The recent independent works of Falgas-Ravry, O’Connell, Stro¨mberg, and Uzzell [37] and of Terry [89] have developed a general framework for studying various enumeration problems in the setting of multicoloured graphs [37] and, more generally, in the very abstract setting of ﬁnite (model theoretic) structures [89]. In order

![image 49](<2018-balogh-method-hypergraph-containers_images/imageFile49.png>)

10The colouring number of a graph H is the largest integer r such that for some pair (r1, r2) satisfying r1 +r2 = r, the vertex set of H cannot be partitioned into r1 cliques and r2 independent sets.

to illustrate some of the ideas involved in applications of this kind, we will discuss the problem of counting ﬁnite metric spaces with bounded integral distances.

- 5.1. Counting metric spaces. Let MMn denote the family of metric spaces on a given set of n points with distances in the set {1,... ,M}. Thus MMn may be viewed as the set of all functions d: E(Kn) → {1,... ,M} that satisfy the triangle inequality d(uv) d(uw) + d(wv) for all u,v,w. Since x y + z for all x,y,z ∈ {⌈M/2⌉,... ,M}, we have


(n2)

(n2)

M 2

M + 1 2

MMn

. (9)

,... ,M

=

![image 50](<2018-balogh-method-hypergraph-containers_images/imageFile50.png>)

![image 51](<2018-balogh-method-hypergraph-containers_images/imageFile51.png>)

Inspired by a continuous version of the model suggested Benjamini (and ﬁrst studied in [61]), Mubayi and Terry [68] proved that for every ﬁxed even M, the converse of (9) holds asymptotically,

that is, |MMn | 1+o(1) M2+1 (n2) as n → ∞. The problem becomes much more diﬃcult, however, when one allows M to grow with n. For example, if M ≫

![image 52](<2018-balogh-method-hypergraph-containers_images/imageFile52.png>)

√n then the lower bound

![image 53](<2018-balogh-method-hypergraph-containers_images/imageFile53.png>)

(n2)

- 1

![image 54](<2018-balogh-method-hypergraph-containers_images/imageFile54.png>)

- 2


c √n

MMn

+

M

![image 55](<2018-balogh-method-hypergraph-containers_images/imageFile55.png>)

![image 56](<2018-balogh-method-hypergraph-containers_images/imageFile56.png>)

for some absolute constant c > 0, proved in [61], is stronger than (9). Balogh and Wagner [18] proved strong upper bounds on |MMn | under the assumption that M ≪ n1/3/(log n)4/3+o(1). The following almost optimal estimate was subsequently obtained by Kozma, Meyerovitch, Peled, and Samotij [61].

- Theorem 5.1. There exists a constant C such that


(n2)

2 M

C √n

- 1

![image 57](<2018-balogh-method-hypergraph-containers_images/imageFile57.png>)

- 2


MMn

+

+

(10) for all n and M.

M

![image 58](<2018-balogh-method-hypergraph-containers_images/imageFile58.png>)

![image 59](<2018-balogh-method-hypergraph-containers_images/imageFile59.png>)

![image 60](<2018-balogh-method-hypergraph-containers_images/imageFile60.png>)

Here, we present an argument due to Morris and Samotij that derives a mildly weaker estimate using the hypergraph container lemma. Let H be the 3-uniform hypergraph with vertex set E(Kn)× {1,... ,M} whose edges are all triples (e1,d1),(e2,d2),(e3,d3) such that e1,e2,e3 form a triangle in Kn but dσ(1) + dσ(2) < dσ(3) for some permutation σ of {1,2,3}. The crucial observation, already made in [18], is that every metric space d: E(Kn) → {1,... ,M}, viewed as the set of pairs (e,d(e)) : e ∈ E(Kn) , is an independent set of H. This enables the use of the hypergraph container method for bounding MMn from above. Deﬁne the volume of a set A ⊂ E(Kn) × {1,... ,M}, denoted by vol(A), by

d ∈ 1,... ,M : (e,d) ∈ A

vol(A) =

e∈E(Kn)

and observe that A contains at most vol(A) elements of MMn . The following supersaturation lemma was proved by Morris and Samotij.

- Lemma 5.2. Let n 3 and M 1 be integers and suppose that A ⊂ E(Kn)×{1,... ,M} satisﬁes


(n2)

- 1

![image 61](<2018-balogh-method-hypergraph-containers_images/imageFile61.png>)

- 2


vol(A) =

+ ε M

for some ε 10/M. Then there exist m M and a set A′ ⊂ A with |A′| mn2, such that the hypergraph H′ = H[A′] satisﬁes

εm2M 50log M

n 3

e(H′)

, ∆1(H′) 4m2n, and ∆2(H′) 2m.

![image 62](<2018-balogh-method-hypergraph-containers_images/imageFile62.png>)

It is not hard to verify that the hypergraph H′ given by Lemma 5.2 satisﬁes the assumptions of the hypergraph container lemma stated in Section 3 with r = εn2M/(211 log M) and b = O(n3/2). Consequently, there exist an absolute constant δ and a collection C of subsets of A′, with

|C| exp O n3/2 log(nM) , such that, setting AC = C ∪ (A \ A′) = A \ (A′ \ C) for each C ∈ C, the following properties hold:

- (a) every metric space in A, viewed as a subset of E(Kn) × {1,... ,M}, is contained in AC for some C ∈ C, and
- (b) |C| |A′| − δr for every C ∈ C.


Observe that

|A′\C|

M − 1 M

vol(A) e−δr/M vol(A)

vol(AC)

![image 63](<2018-balogh-method-hypergraph-containers_images/imageFile63.png>)

(n2)

- 1

![image 64](<2018-balogh-method-hypergraph-containers_images/imageFile64.png>)

- 2


δ 212 log M

e−δεn2/(211 logM) vol(A)

+ 1 −

.

ε M

![image 65](<2018-balogh-method-hypergraph-containers_images/imageFile65.png>)

Since every metric space in MMn is contained in E(Kn) × {1,... ,M}, by recursively applying this ‘breaking down’ process to depth O(log M)2, we obtain a family of

exp O n3/2(log M)2 log(nM)

subsets of E(Kn)×{1,... ,M}, each of volume at most M/2+10 (n2), that cover all of MMn . This implies that

(n2)

C(log M)2 log(nM) √n

10 M

1 2

MMn

+

+

, which, as promised, is only slightly weaker than (10).

M

![image 66](<2018-balogh-method-hypergraph-containers_images/imageFile66.png>)

![image 67](<2018-balogh-method-hypergraph-containers_images/imageFile67.png>)

![image 68](<2018-balogh-method-hypergraph-containers_images/imageFile68.png>)

![image 69](<2018-balogh-method-hypergraph-containers_images/imageFile69.png>)

6. An asymmetric container lemma

The approach to studying the family of induced-H-free graphs described in the previous section has one (rather subtle) drawback: it embeds Fnind(H) into the family of independent sets of a v(2H) uniform hypergraph with Θ(n2) vertices. As a result, the hypergraph container lemma produces ﬁngerprints of the same size as for the family of graphs without a clique on v(H) vertices. This precludes the study of various threshold phenomena in the context of sparse induced-H-free graphs with the use of the hypergraph container lemma presented in Section 3; this is in sharp contrast with the non-induced case, where the container method proved very useful.

In order to alleviate this shortcoming, Morris, Samotij, and Saxton [65] proved a version of the hypergraph container lemma for 2-coloured structures that takes into account the possible asymmetries between the two colours. We shall not give the precise statement of this new container

lemma here (since it is rather technical), but we would like to emphasize the following key fact: it enables one to construct families of containers for induced-H-free graphs with ﬁngerprints of size Θ(n2−1/m2(H)), as in the non-induced case.

To demonstrate the power of the asymmetric container lemma, the following application was given in [65]. Let us say that a graph G is ε-close to a split graph if there exists a partition V (G) = A ∪ B such that e(G[A]) (1 − ε) |A2| and e(G[B]) εe(G).

- Theorem 6.1. For every ε > 0, there exists a δ > 0 such that the following holds. Let G be a uniformly chosen induced-C4-free graph with vertex set {1,... ,n} and m edges.


(a) If n ≪ m ≪ δn4/3(log n)1/3, then a.a.s. G is not 1/4-close to a split graph. (b) If n4/3(log n)4 m δn2, then a.a.s. G is ε-close to a split graph.

- Theorem 6.1 has the following interesting consequence: it allows one to determine the number

of edges in (and, sometimes, also the typical structure of) the binomial random graph G(n,p) conditioned on the event that it does not contain an induced copy of C4. Let us denote by Gindn,p(C4) the random graph chosen according to this conditional distribution.

Corollary 6.2. The following bounds hold asymptotically almost surely as n → ∞:

e Gindn,p(C4) =

 



1 + o(1) p n2 if n−1 ≪ p ≪ n−2/3, n4/3(log n)O(1) if n−2/3 p n−1/3(log n)4, Θ p2n2/log(1/p) if p n−1/3(log n)4.

We would like to emphasize the (surprising) similarity between the statements of Theorem 4.5 and Corollary 6.2. In particular, the graph of p  → e Gindn,p(C4) contains exactly the same ‘long ﬂat segment’ as the graph of p  → ex G(n,p),C4 , even though the shape of the two graphs above this range is quite diﬀerent. We do not yet fully understand this phenomenon and it would be interesting to investigate whether or not the function p  → e Gindn,p(H) exhibits similar behaviour for other bipartite graphs H.

7. Hypergraphs of unbounded uniformity

Since the hypergraph container lemma provides explicit dependencies between the various parameters in its statement, it is possible to apply the container method even when the uniformity of the hypergraph considered is a growing function of the number of its vertices. Perhaps the ﬁrst result of this ﬂavour was obtained by Mousset, Nenadov, and Steger [67], who proved an upper bound of 2ex(n,Kr)+o(n2/r) on the number of n-vertex Kr-free graphs for all r (log2 n)1/4/2. Subsequently, Balogh, Bushaw, Collares, Liu, Morris, and Sharifzadeh [8] strengthened this result by establishing the following precise description of the typical structure of large Kr-free graphs.

- Theorem 7.1. If r (log2 n)1/4, then almost all Kr-free graphs with n vertices are (r −1)-partite.


Around the same time, the container method applied to hypergraphs with unbounded uniformity was used to analyse Ramsey properties of random graphs and hypergraphs, leading to improved

upper bounds on several well-studied functions. In particular, Ro¨dl, Rucin´ski, and Schacht [73] gave the following upper bound on the so-called Folkman numbers.

- Theorem 7.2. For all integers k 3 and r 2, there exists a Kk+1-free graph with exp Ck4 log k + k3r log r


vertices, such that every r-colouring of its edges contains a monochromatic copy of Kk.

The previously best known bound was doubly exponential in k, even in the case r = 2. Not long afterwards, Conlon, Dellamonica, La Fleur, Ro¨dl, and Schacht [24] used a similar method to prove the following strong upper bounds on the induced Ramsey numbers of hypergraphs. Deﬁne the tower functions tk(x) by t1(x) = x and ti+1(x) = 2ti(x) for each i 1.

- Theorem 7.3. For each k 3 and r 2, there exists c such that the following holds. For every


k-uniform hypergraph F on m vertices, there exists a k-uniform hypergraph G on tk(cm) vertices, such that every r-colouring of E(G) contains a monochromatic induced copy of F.

Finally, let us mention a recent result of Balogh and Solymosi [17], whose proof is similar to that of Theorem 2.8, which we outlined in Section 2.4. Given a family F of subsets of an n-element set Ω, an ε-net of F is a set A ⊂ Ω that intersects every member of F with at least εn elements. The concept of an ε-net plays an important role in computer science, for example in computational geometry and approximation theory. In a seminal paper, Haussler and Welzl [51] proved that every set system with VC-dimension11 d has an ε-net of size O (d/ε)log(d/ε) . It was believed for more than twenty years that for ‘geometric’ families, the log(d/ε) factor can be removed; however, this was disproved by Alon [5], who constructed, for each C > 0, a set of points in the plane such that the smallest ε-net for the family of lines (whose VC-dimension is 2) has size at least C/ε.

By applying the container method to the hypergraph of collinear k-tuples in the k-dimensional 2k2 × ··· × 2k2 integer grid, Balogh and Solymosi [17] gave the following stronger lower bound.

- Theorem 7.4. For each ε > 0, there exists a set S ⊂ R2 such that the following holds. If T ⊂ S intersects every line that contains at least ε|S| elements of S, then


1/3+o(1)

1 ε

1 ε

|T|

.

log

![image 70](<2018-balogh-method-hypergraph-containers_images/imageFile70.png>)

![image 71](<2018-balogh-method-hypergraph-containers_images/imageFile71.png>)

It was conjectured by Alon [5] that there are sets of points in the plane whose smallest ε-nets (for the family of lines) contain Ω 1/εlog(1/ε) points.

8. Some further applications

There are numerous applications of the method of containers that we do not have space to discuss in detail. Still, we would like to ﬁnish this survey by brieﬂy mentioning just a few of them.

![image 72](<2018-balogh-method-hypergraph-containers_images/imageFile72.png>)

11The VC-dimension (VC stands for Vapnik–Chervonenkis) of a family F of subsets of Ω is the largest size of a set X ⊂ Ω such that the set {A ∩ X : A ∈ F} has 2|X| elements.

- 8.1. List colouring. A hypergraph H is said to be k-choosable if for every assignment of a list Lv of k colours to each vertex v of H, it is possible to choose for each v a colour from the list Lv in such a way that no edge of H has all its vertices of the same colour. The smallest k for which H is k-choosable is usually called the list chromatic number of H and denoted by χℓ(H). Alon [3, 4] showed that for graphs, the list chromatic number grows with the minimum degree, in


stark contrast with the usual chromatic number; more precisely, χℓ(G) 1/2+o(1) log2 δ(G) for every graph G. The following generalisation of this result, which also improves the constant 1/2, was proved by Saxton and Thomason [81], see also [80, 82].

- Theorem 8.1. Let H be a k-uniform hypergraph with average degree d and ∆2(H) = 1. Then, as d → ∞,


1 (k − 1)2

χℓ(H)

+ o(1) logk d. Moreover, if H is d-regular, then

![image 73](<2018-balogh-method-hypergraph-containers_images/imageFile73.png>)

1 k − 1

+ o(1) logk d.

χℓ(H)

![image 74](<2018-balogh-method-hypergraph-containers_images/imageFile74.png>)

We remark that proving lower bounds for the list chromatic number of simple hypergraphs was one of the original motivations driving the development of the method of hypergraph containers.

- 8.2. Additive combinatorics. The method of hypergraph containers has been applied to a number of diﬀerent number-theoretic objects, including sum-free sets [6, 7, 11, 12], Sidon sets [82], sets containing no k-term arithmetic progression [10, 13], and general systems of linear equations [82]. (See also [49, 50, 78] for early applications of the container method to sum-free sets


and [28, 29, 27, 59] for applications of graph containers to Bh-sets.) Here we will mention just three of these results.

Let us begin by recalling that a Sidon set is a set of integers containing no non-trivial solutions of the equation x+y = z+w. Results of Chowla, Erd˝os, Singer, and Tura´n from the 1940s imply that the maximum size of a Sidon set in {1,... ,n} is 1 + o(1) √n and it was conjectured by Cameron and Erd˝os [23] that the number of such sets is 2(1+o(1))

![image 75](<2018-balogh-method-hypergraph-containers_images/imageFile75.png>)

√n. This conjecture was disproved by Saxton √n Sidon sets (for some ε > 0), and also used

![image 76](<2018-balogh-method-hypergraph-containers_images/imageFile76.png>)

![image 77](<2018-balogh-method-hypergraph-containers_images/imageFile77.png>)

- and Thomason [82], who gave a construction of 2(1+ε)


the hypergraph container method to reprove the following theorem, which was originally obtained in [59] using the graph container method.

√n) Sidon sets in {1,... ,n}.

![image 78](<2018-balogh-method-hypergraph-containers_images/imageFile78.png>)

- Theorem 8.2. There are 2O(


Dellamonica, Kohayakawa, Lee, Ro¨dl, and Samotij [27] later generalized these results to Bh-sets, that is, set of integers containing no non-trivial solutions of the equation x1+...+xh = y1+...+yh.

The second result we would like to state was proved by Balogh, Liu, and Sharifzadeh [10], and inspired the proof presented in Section 4. Let rk(n) be the largest size of a subset of {1,... ,n} containing no k-term arithmetic progressions.

- Theorem 8.3. For each integer k 3, there exist a constant C and inﬁnitely many n ∈ N such that there are at most 2Crk(n) subsets of {1,... ,n} containing no k-term arithmetic progression.


We recall (see, e.g., [48]) that obtaining good bounds on rk(n) is a well-studied and notoriously diﬃcult problem. The proof of Theorem 8.3 avoids these diﬃculties by exploiting merely the ‘self-similarity’ property of the hypergraph encoding arithmetic progressions in {1,... ,n}, cf. the discussion in Section 3 and the proof of Lemma 4.3.

The ﬁnal result we would like to mention was one of the ﬁrst applications of (and original motivations for the development of) the method of hypergraph containers. Recall that the Cameron–Erd˝os conjecture, proved by Green [49] and, independently, by Sapozhenko [78], states that there are only O(2n/2) sum-free subsets of {1,... ,n}. The following sparse analogue of the Cameron–Erd˝os conjecture was proved by Alon, Balogh, Morris, and Samotij [7] using an early version of the hypergraph container lemma for 3-uniform hypergraphs.

- Theorem 8.4. There exists a constant C such that, for every n ∈ N and every 1 m ⌈n/2⌉, the set {1,... ,n} contains at most 2Cn/m ⌈n/m2⌉ sum-free sets of size m.

We remark that if m √n, then Theorem 8.4 is sharp up to the value of C, since in this case

![image 79](<2018-balogh-method-hypergraph-containers_images/imageFile79.png>)

there is a constant c > 0 such that there are at least 2cn/m n/m2 sum-free m-subsets of {1,... ,n}. For smaller values of m the answer is diﬀerent, but the problem in that range is much easier and

can be solved using standard techniques. Let us also mention that in the case m ≫

√nlog n, the structure of a typical sum-free m-subset of {1,... ,n} was also determined quite precisely in [7].

![image 80](<2018-balogh-method-hypergraph-containers_images/imageFile80.png>)

Finally, we would like to note that, although the statements of Theorems 8.2, 8.3 and 8.4 are somewhat similar, the diﬃculties encountered during their proofs are completely diﬀerent.

- 8.3. Sharp thresholds for Ramsey properties. Given an integer k 3, let us say that a


set A ⊂ Zn has the van der Waerden property for k if every 2-colouring of the elements of A contains a monochromatic k-term arithmetic progression; denote this by A → (k-AP). Ro¨dl and Rucin´ski [72] determined the threshold for the van der Waerden property in random subsets of Zn for every k ∈ N. Combining the sharp threshold technology of Friedgut [40] with the method of hypergraph containers, Friedgut, H´an, Person, and Schacht [41] proved that this threshold is sharp. Let us write Zn,p to denote a p-random subset of Zn (i.e., each element is included independently with probability p).

- Theorem 8.5. For every k 3, there exist constants c1 > c0 > 0 and a function pc: N → [0,1] satisfying c0n−1/(k−1) < pc(n) < c1n−1/(k−1) for every n ∈ N, such that, for every ε > 0,


 

- 0 if p (1 − ε)pc(n),
- 1 if p (1 + ε)pc(n),


P Zn,p → k-AP →

 as n → ∞.

The existence of a sharp threshold in the context of Ramsey’s theorem for the triangle was obtained several years earlier, by Friedgut, Ro¨dl, Rucin´ski, and Tetali [42]. Very recently, using similar methods to those in [41], Schacht and Schulenburg [84] gave a simpler proof of this theorem and also generalised it to a large family of graphs, including all odd cycles.

- 8.4. Maximal triangle-free graphs and sum-free sets. In contrast to the large body of work devoted to counting and describing the typical structure of H-free graphs, relatively little is known about H-free graphs that are maximal (with respect to the subgraph relation). The following construction shows that there are at least 2n2/8 maximal triangle-free graphs with vertex set {1,... ,n}. Fix a partition X ∪Y = {1,... ,n} with |X| even. Deﬁne G by letting G[X] be a perfect matching, leaving G[Y ] empty, and adding to E(G) exactly one of xy or x′y for every edge xx′ ∈ E(G[X]) and every y ∈ Y . It is easy to verify that all such graphs are triangle-free and that almost all of them are maximal.

Using the container theorem for triangle-free graphs (Theorem 2.1), Balogh and Petrˇı´cˇkov´a [14] proved that the construction above is close to optimal by showing that there are at most 2n2/8+o(n2) maximal triangle-free graphs on {1,... ,n}. Following this breakthrough, Balogh, Liu, Petrˇı´cˇkov´a, and Sharifzadeh [9] proved the following much stronger theorem, which states that in fact almost all maximal triangle-free graphs can be constructed in this way.

Theorem 8.6. For almost every maximal triangle-free graph G on {1,... ,n}, there is a vertex partition X ∪ Y such that G[X] is a perfect matching and Y is an independent set.

A similar result for sum-free sets was obtained by Balogh, Liu, Sharifzadeh, and Treglown [11, 12], who determined the number of maximal sum-free subsets of {1,... ,n} asymptotically. However, the problem of estimating the number of maximal H-free graphs for a general graph H is still wide open. In particular, generalizing the results of [9, 14] to the family of maximal Kk-free graphs seems to be a very interesting and diﬃcult open problem.

- 8.5. Containers for rooted hypergraphs. A family F of ﬁnite sets is union-free if A ∪ B = C for every three distinct sets A,B,C ∈ F. Kleitman [55] proved that every union-free family in


{1,... ,n} contains at most 1 + o(1) n/ n2 sets; this is best possible as the family of all ⌊n/2⌋element subsets of {1,... ,n} is union-free. Balogh and Wagner [19] proved the following natural

counting counterpart of Kleitman’s theorem, conﬁrming a conjecture of Burosch, Demetrovics, Katona, Kleitman, and Sapozhenko [22].

- Theorem 8.7. There are 2(1+o(1))(n/n2) union-free families in {1,... ,n}.

It is natural to attempt to prove this theorem by applying the container method to the 3-uniform hypergraph H that encodes triples {A,B,C} with A ∪ B = C. However, there is a problem: for any pair (B,C), there exist 2|B| sets A such that A∪B = C and this means that ∆2(H) is too large for a naive application of the hypergraph container lemma. In order to overcome this diﬃculty, Balogh and Wagner developed in [19] a new container theorem for ‘rooted’ hypergraphs (each edge has a designated root vertex) that exploits the asymmetry of the identity A∪B = C. In particular, note that while the degree of a pair (B,C) can be large, the pair {A,B} uniquely determines C; it turns out that this is suﬃcient to prove a suitable container theorem. We refer the reader to [19] for the details.

- 8.6. Probabilistic embedding in sparse graphs. The celebrated regularity lemma of Szemere´di [88] states that, roughly speaking, the vertex set of every graph can be divided into a


bounded number of parts in such a way that most of the bipartite subgraphs induced by pairs of parts are pseudorandom; such a partition is called a regular partition. The strength of the regularity lemma stems from the so-called counting and embedding lemmas, which tell us approximately how many copies of a particular subgraph a graph G contains in terms of basic parameters of the regular partition of G. While the original statement of the regularity lemma applied only to dense graphs (i.e., n-vertex graphs with Ω(n2) edges), the works of Kohayakawa [57], Ro¨dl (unpublished), and Scott [85] provide extensions of the lemma that are applicable to sparse graphs. However, these extensions come with a major caveat: the counting and embedding lemmas do not extend to sparse graphs; this unfortunate fact was observed by  Luczak. Nevertheless, it seemed likely that such atypical graphs that fail the counting or embedding lemmas are so rare that they typically do not appear in random graphs. This belief was formalised in a conjecture of Kohayakawa,  Luczak, and Ro¨dl [60], which can be seen as a ‘probabilistic’ version of the embedding lemma.

The proof of this conjecture, discovered by the authors of this survey [13] and by Saxton and Thomason [81], was one of the original applications of the hypergraph container lemma. Let us mention here that a closely related result was proved around the same time by Conlon, Gowers, Samotij, and Schacht [26]. A strengthening of the K LR conjecture, a ‘probabilistic’ version of the counting lemma, proposed by Gerke, Marciniszyn, and Steger [47], remains open.

Acknowledgements

The authors would like to thank Noga Alon, Be´la Bollob´s, David Conlon, Yoshi Kohayakawa, Gady Kozma, Tom Meyerovitch, Ron Peled, David Saxton, and Andrew Thomason for many stimulating discussions over the course of the last several years. These discussions have had a signiﬁcant impact on the development of the container method. Last but not least, we would like to again acknowledge David Conlon, Ehud Friedgut, Tim Gowers, Daniel Kleitman, Vojta Ro¨dl, Mathias Schacht, and Kenneth Wilson, whose work on enumeration of C4-free graphs and on extremal and Ramsey properties of random discrete structures inspired and inﬂuenced our investigations that led to the hypergraph container theorems.

References

- 1. M. Ajtai, J. Koml´os, J. Pintz, J. Spencer, and E. Szemere´di, Extremal uncrowded hypergraphs, J. Combin. Theory Ser. A 32 (1982), 321–335.
- 2. V. E. Alekseev, Range of values of entropy of hereditary classes of graphs, Diskret. Mat. 4 (1992), 148–157.
- 3. N. Alon, Restricted colorings of graphs, Surveys in Combinatorics, 1993 (Keele), London Math. Soc. Lecture Note Ser., vol. 187, Cambridge Univ. Press, Cambridge, 1993, pp. 1–33.
- 4. , Degrees and choice numbers, Random Structures Algorithms 16 (2000), 364–368.

![image 81](<2018-balogh-method-hypergraph-containers_images/imageFile81.png>)

- 5. , A non-linear lower bound for planar epsilon-nets, Discrete Comput. Geom. 47 (2012), 235–244.

![image 82](<2018-balogh-method-hypergraph-containers_images/imageFile82.png>)

- 6. N. Alon, J. Balogh, R. Morris, and W. Samotij, Counting sum-free sets in abelian groups, Israel J. Math. 199

(2014), 309–344.

- 7. , A reﬁnement of the Cameron-Erd˝os Conjecture, Proc. London Math. Soc. 108 (2014), 44–72.

![image 83](<2018-balogh-method-hypergraph-containers_images/imageFile83.png>)

- 8. J. Balogh, N. Bushaw, M. Collares, H. Liu, R. Morris, and M. Sharifzadeh, The typical structure of graphs with no large cliques, Combinatorica 37 (2017), 617–632.


- 9. J. Balogh, H. Liu, S.ˇ Petrˇı´cˇkova´, and M. Sharifzadeh, The typical structure of maximal triangle-free graphs, Forum Math. Sigma 3 (2015), e20, 19.
- 10. J. Balogh, H. Liu, and M. Sharifzadeh, The number of subsets of integers with no k-term arithmetic progression, Int. Math. Res. Not. IMRN (2017), no. 20, 6168–6186.
- 11. J Balogh, H. Liu, M. Sharifzadeh, and A. Treglown, Sharp bound on the number of maximal sum-free subsets of integers, submitted.
- 12. , The number of maximal sum-free subsets of integers, Proc. Amer. Math. Soc. 143 (2015), no. 11, 4713– 4721.

![image 84](<2018-balogh-method-hypergraph-containers_images/imageFile84.png>)

- 13. J. Balogh, R. Morris, and W. Samotij, Independent sets in hypergraphs, J. Amer. Math. Soc. 28 (2015), 669–709.
- 14. J. Balogh and S.ˇ Petrˇı´cˇkova´, The number of the maximal triangle-free graphs, Bull. Lond. Math. Soc. 46 (2014), 1003–1006.
- 15. J. Balogh and W. Samotij, The number of Km,m-free graphs, Combinatorica 31 (2011), 131–150.
- 16. , The number of Ks,t-free graphs, J. Lond. Math. Soc. 83 (2011), 368–388.

![image 85](<2018-balogh-method-hypergraph-containers_images/imageFile85.png>)

- 17. J. Balogh and J. Solymosi, On the number of points in general position in the plane, Discrete Anal., to appear.
- 18. J Balogh and A. Z. Wagner, Further applications of the container method, Recent trends in combinatorics, IMA Vol. Math. Appl., vol. 159, Springer, Cham, 2016, pp. 191–213.
- 19. , On the number of union-free families, Israel J. Math. 219 (2017), 431–448.

![image 86](<2018-balogh-method-hypergraph-containers_images/imageFile86.png>)

- 20. B. Bollob´s and A. Thomason, Projections of bodies and hereditary properties of hypergraphs, Bull. London Math. Soc. 27 (1995), 417–424.
- 21. , Hereditary and monotone properties of graphs, The mathematics of Paul Erd˝s, II, Algorithms Combin., vol. 14, Springer, Berlin, 1997, pp. 70–78.

![image 87](<2018-balogh-method-hypergraph-containers_images/imageFile87.png>)

- 22. G. Burosch, J. Demetrovics, G.O.H. Katona, D.J. Kleitman, and A.A. Sapozhenko, On the number of databases and closure operations, Theoretical Computer Science 78 (1991), 377–381.
- 23. P. Cameron and P. Erd˝s, On the number of sets of integers with various properties, In: Number Theory (Mollin, R.A., ed.), 61–79, Walter de Gruyter, Berlin, 1990.
- 24. D. Conlon, D. Dellamonica, Jr., S. La Fleur, V. Ro¨dl, and M. Schacht, A note on induced Ramsey numbers, A Journey Through Discrete Mathematics: A Tribute to Jirˇı´ Matousˇek, Springer, 2017, pp. 357–366.
- 25. D. Conlon and W. T. Gowers, Combinatorial theorems in sparse random sets, Ann. of Math. (2) 184 (2016), 367–454.
- 26. D. Conlon, W.T. Gowers, W. Samotij, and M. Schacht, On the K LR conjecture in random graphs, Israel J. Math. 203 (2014), 535–580.
- 27. D. Dellamonica, Jr., Y. Kohayakawa, S. J. Lee, V. Ro¨dl, and W. Samotij, The number of Bh-sets of a given cardinality, Proc. London Math. Soc. (2), to appear.
- 28. , The number of B3-sets of a given cardinality, J. Combin. Theory Ser. A 142 (2016), 44–76.

![image 88](<2018-balogh-method-hypergraph-containers_images/imageFile88.png>)

- 29. , On the number of Bh-sets, Combin. Probab. Comput. 25 (2016), 108–129.

![image 89](<2018-balogh-method-hypergraph-containers_images/imageFile89.png>)

- 30. B. DeMarco and J. Kahn, Tur´an’s theorem for random graphs, arXiv:1501.01340 [math.PR].
- 31. , Mantel’s theorem for random graphs, Random Structures Algorithms 47 (2015), 59–72.

![image 90](<2018-balogh-method-hypergraph-containers_images/imageFile90.png>)

- 32. R. A. Duke, H. Lefmann, and V. Ro¨dl, On uncrowded hypergraphs, Proceedings of the Sixth International Seminar on Random Graphs and Probabilistic Methods in Combinatorics and Computer Science, “Random Graphs ’93” (Poznan´, 1993), vol. 6, 1995, pp. 209–212.
- 33. P. Erd˝s, Some recent results on extremal problems in graph theory. Results, Theory of Graphs (Internat. Sympos., Rome, 1966), Gordon and Breach, New York; Dunod, Paris, 1967, pp. 117–123 (English); pp. 124–130 (French).
- 34. , Some old and new problems in combinatorial geometry, Applications of discrete mathematics (Clemson, SC, 1986), SIAM, Philadelphia, PA, 1988, pp. 32–37.

![image 91](<2018-balogh-method-hypergraph-containers_images/imageFile91.png>)

- 35. P. Erd˝s, P. Frankl, and V. Ro¨dl, The asymptotic number of graphs not containing a ﬁxed subgraph and a problem for hypergraphs having no exponent, Graphs Combin. 2 (1986), 113–121.


- 36. P. Erd˝s, D. J. Kleitman, and B. L. Rothschild, Asymptotic enumeration of Kn-free graphs, Colloquio Internazionale sulle Teorie Combinatorie (Rome, 1973), Tomo II, Accad. Naz. Lincei, Rome, 1976, pp. 19–27. Atti dei Convegni Lincei, No. 17.
- 37. V. Falgas-Ravry, K. O’Connell, J. Str¨omberg, and A. Uzzell, Multicolour containers and the entropy of decorated graph limits, arXiv:1607.08152 [math.CO].
- 38. A. Ferber, G. A. McKinley, and W. Samotij, Supersaturated sparse graphs and hypergraphs, arXiv:1710.04517 [math.CO].
- 39. P. Frankl and V. Ro¨dl, Large triangle-free subgraphs in graphs without K4, Graphs Combin. 2 (1986), 135–144.
- 40. E. Friedgut, Sharp thresholds of graph properties, and the k-sat problem, J. Amer. Math. Soc. 12 (1999), 1017– 1054, With an appendix by Jean Bourgain.
- 41. E. Friedgut, H. H`an, Y. Person, and M. Schacht, A sharp threshold for van der Waerden’s theorem in random subsets, Discrete Anal. (2016), Paper No. 7, 20.
- 42. E. Friedgut, V. Ro¨dl, A. Rucin´ski, and P. Tetali, A sharp threshold for random graphs with a monochromatic triangle in every edge coloring, Mem. Amer. Math. Soc. 179 (2006), vi+66.
- 43. E. Friedgut, V. Ro¨dl, and M. Schacht, Ramsey properties of random discrete structures, Random Structures Algorithms 37 (2010), 407–436.
- 44. Z. Fu¨redi, Maximal independent subsets in Steiner systems and in planar sets, SIAM J. Discrete Math. 4 (1991), 196–199.
- 45. , A proof of the stability of extremal graphs, Simonovits’ stability from Szemer´edi’s regularity, J. Combin. Theory Ser. B 115 (2015), 66–71.

![image 92](<2018-balogh-method-hypergraph-containers_images/imageFile92.png>)

- 46. H. Furstenberg and Y. Katznelson, A density version of the Hales-Jewett theorem, J. Anal. Math. 57 (1991), 64–119.
- 47. S. Gerke, M. Marciniszyn, and A. Steger, A probabilistic counting lemma for complete graphs, Random Structures Algorithms 31 (2007), 517–534.
- 48. W.T. Gowers, Erd˝os and arithmetic progressions, In: Lova´sz L., Ruzsa I.Z., S´os V.T. (eds.) Erd˝s Centennial, Bolyai Society Mathematical Studies, vol. 25, Springer, Berlin, Heidelberg, 2013.
- 49. B. Green, The Cameron-Erd˝os conjecture, Bull. London Math. Soc. 36 (2004), 769–778.
- 50. B. Green and I. Z. Ruzsa, Counting sumsets and sum-free sets modulo a prime, Studia Sci. Math. Hungar. 41

(2004), 285–293.

- 51. D. Haussler and E. Welzl, ǫ-nets and simplex range queries, Discrete Comput. Geom. 2 (1987), 127–151.
- 52. P. E. Haxell, Y. Kohayakawa, and T.  Luczak, Tur´an’s extremal problem in random graphs: forbidding odd cycles, Combinatorica 16 (1996), 107–122.
- 53. P.E. Haxell, Y. Kohayakawa, and T.  Luczak, Tur´an’s extremal problem in random graphs: forbidding even cycles, J. Combin. Theory Ser. B 64 (1995), 273–287.
- 54. D. J. Kleitman and K. J. Winston, The asymptotic number of lattices, Ann. Discrete Math. 6 (1980), 243–249, Combinatorial mathematics, optimal designs and their applications (Proc. Sympos. Combin. Math. and Optimal Design, Colorado State Univ., Fort Collins, Colo., 1978).
- 55. D.J. Kleitman, Extremal properties of collections of subsets containing no two sets and their union, J. Combin. Theory Ser. A 20 (1976), 390–392.
- 56. D.J. Kleitman and K.J. Winston, On the number of graphs without 4-cycles, Discrete Math. 41 (1982), 167–172.
- 57. Y. Kohayakawa, Szemer´edi’s regularity lemma for sparse graphs, Foundations of computational mathematics (Rio de Janeiro, 1997), Springer, Berlin, 1997, pp. 216–230.
- 58. Y. Kohayakawa, B. Kreuter, and A. Steger, An extremal problem for random graphs and the number of graphs with large even-girth, Combinatorica 18 (1998), 101–120.
- 59. Y. Kohayakawa, S. J. Lee, V. Ro¨dl, and W. Samotij, The number of Sidon sets and the maximum size of Sidon sets contained in a sparse random set of integers, Random Structures Algorithms 46 (2015), 1–25.


- 60. Y. Kohayakawa, T.  Luczak, and V. Ro¨dl, On K4-free subgraphs of random graphs, Combinatorica 17 (1997), 173–213.
- 61. G. Kozma, T. Meyerovitch, R. Peled, and W. Samotij, What does a typical metric space look like?, manuscript.
- 62. D. Ku¨hn, D. Osthus, T. Townsend, and Y. Zhao, On the structure of oriented graphs and digraphs with forbidden tournaments or cycles, J. Combin. Theory Ser. B 124 (2017), 88–127.
- 63. T.  Luczak, On triangle-free random graphs, Random Structures Algorithms 16 (2000), 260–276.
- 64. W. Mantel, Problem 28, Wiskundige Opgaven 10 (1907), 60–61.
- 65. R. Morris, W. Samotij, and D. Saxton, An asymmetric container lemma and the structure of graphs with no induced 4-cycle, manuscript.
- 66. R. Morris and D. Saxton, The number of C2ℓ-free graphs, Adv. Math. 298 (2016), 534–580.
- 67. F. Mousset, R. Nenadov, and A. Steger, On the number of graphs without large cliques, SIAM J. Discrete Math. 28 (2014), 1980–1986.
- 68. D. Mubayi and C. Terry, Discrete metric spaces: structure, enumeration, and 0-1 laws, J. Symb. Log., to appear.
- 69. R. Nenadov and A. Steger, A short proof of the random Ramsey theorem, Combin. Probab. Comput. 25 (2016), 130–144.
- 70. V. Ro¨dl and A. Rucin´ski, Lower bounds on probability thresholds for Ramsey properties, Combinatorics, Paul Erd˝s is eighty, Vol. 1, Bolyai Soc. Math. Stud., J´anos Bolyai Math. Soc., Budapest, 1993, pp. 317–346.
- 71. , Random graphs with monochromatic triangles in every edge coloring, Random Structures Algorithms 5

![image 93](<2018-balogh-method-hypergraph-containers_images/imageFile93.png>)

(1994), 253–270.

- 72. , Threshold functions for Ramsey properties, J. Amer. Math. Soc. 8 (1995), 917–942.

![image 94](<2018-balogh-method-hypergraph-containers_images/imageFile94.png>)

- 73. V. Ro¨dl, A. Rucin´ski, and M. Schacht, An exponential-type upper bound for Folkman numbers, Combinatorica 37 (2017), 767–784.
- 74. V. Ro¨dl and M. Schacht, Extremal results in random graphs, Erd˝s centennial, Bolyai Soc. Math. Stud., vol. 25, J´anos Bolyai Math. Soc., Budapest, 2013, pp. 535–583.
- 75. I.Z. Ruzsa and E. Szemere´di, Triple systems with no six points carrying three triangles, Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Vol. II, Colloq. Math. Soc. J´anos Bolyai, vol. 18, North-Holland, Amsterdam, 1978, pp. 939–945.
- 76. W. Samotij, Counting independent sets in graphs, European J. Combin. 48 (2015), 5–18.
- 77. A. A. Sapozhenko, On the number of independent sets in extenders, Diskret. Mat. 13 (2001), 56–62.
- 78. , The Cameron-Erd˝os conjecture, Dokl. Akad. Nauk 393 (2003), 749–752.

![image 95](<2018-balogh-method-hypergraph-containers_images/imageFile95.png>)

- 79. , Systems of containers and enumeration problems, Stochastic Algorithms: Foundations and Applications: Third International Symposium, SAGA 2005 (Moscow, Russia), Lecture Notes in Computer Science, vol. 3777, 2005, pp. 1–13.

![image 96](<2018-balogh-method-hypergraph-containers_images/imageFile96.png>)

- 80. D. Saxton and A. Thomason, List colourings of regular hypergraphs, Combin. Probab. Comput. 21 (2012), 315– 322.
- 81. , Hypergraph containers, Invent. Math. 201 (2015), 925–992.

![image 97](<2018-balogh-method-hypergraph-containers_images/imageFile97.png>)

- 82. , Online containers for hypergraphs, with applications to linear equations, J. Combin. Theory Ser. B 121

![image 98](<2018-balogh-method-hypergraph-containers_images/imageFile98.png>)

(2016), 248–283.

- 83. M. Schacht, Extremal results for random discrete structures, Ann. of Math. (2) 184 (2016), 333–365.
- 84. M. Schacht and F. Schulenburg, Sharp thresholds for Ramsey properties of strictly balanced nearly bipartite graphs, Random Structures Algorithms 52 (2018), 3–40.
- 85. A. Scott, Szemer´edi’s regularity lemma for matrices and sparse graphs, Combin. Probab. Comput. 20 (2011), 455–466.
- 86. M. Simonovits, A method for solving extremal problems in graph theory, stability problems, Theory of Graphs (Proc. Colloq., Tihany, 1966), Academic Press, New York, 1968, pp. 279–319.
- 87. E. Szemere´di, On sets of integers containing no k elements in arithmetic progression, Acta Arith. 27 (1975), 199–245.


- 88. , Regular partitions of graphs, Proble`mes combinatoires et the´orie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), Colloq. Internat. CNRS, vol. 260, CNRS, Paris, 1978, pp. 399–401.

![image 99](<2018-balogh-method-hypergraph-containers_images/imageFile99.png>)

- 89. C. Terry, Structure and enumeration theorems for hereditary properties in ﬁnite relational languages, arXiv:1607.04902 [math.LO].
- 90. P. Tur´an, Eine Extremalaufgabe aus der Graphentheorie, Mat. Fiz. Lapok 48 (1941), 436–452.


Department of Mathematics, University of Illinois at Urbana-Champaign, Urbana, Illinois 61801, USA

E-mail address: jobal@math.uiuc.edu

IMPA, Estrada Dona Castorina 110, Jardim Botanico,ˆ Rio de Janeiro, 22460-320, Brazil E-mail address: rob@impa.br

School of Mathematical Sciences, Tel Aviv University, Tel Aviv 6997801, Israel E-mail address: samotij@post.tau.ac.il

