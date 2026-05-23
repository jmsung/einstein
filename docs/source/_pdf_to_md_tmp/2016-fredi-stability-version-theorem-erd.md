# arXiv:1608.05741v2[math.CO]5Apr2017

## A stability version for a theorem of Erdo˝s on nonhamiltonian graphs

Zolta´n Fu¨redi∗ Alexandr Kostochka† Ruth Luo‡

August 23, 2016

Abstract

Let n,d be integers with 1 ≤ d ≤ n−21 , and set h(n,d) := n−2d + d2 and e(n,d) :=

max{h(n,d),h(n, n−21 )}. Because h(n,d) is quadratic in d, there exists a d0(n) = (n/6)+O(1) such that

e(n,1) > e(n,2) > ··· > e(n,d0) = e(n,d0 + 1) = ··· = e(n,

n − 1 2

).

A theorem by Erd˝s states that for d ≤ n−21 , any n-vertex nonhamiltonian graph G with minimum degree δ(G) ≥ d has at most e(n,d) edges, and for d ≥ d0(n) the unique sharpness example is simply the graph Kn − E(K (n+1)/2 ). Erdo˝s also presented a sharpness example Hn,d for each 1 ≤ d ≤ d0(n).

We show that if d < d0(n) and a 2-connected, nonhamiltonian n-vertex graph G with δ(G) ≥ d has more than e(n,d+1) edges, then G is a subgraph of Hn,d. Note that e(n,d)−e(n,d+1) = n − 3d − 2 ≥ n/2 whenever d < d0(n) − 1.

Mathematics Subject Classiﬁcation: 05C35, 05C38. Keywords: Tura´n problem, hamiltonian cycles, extremal graph theory.

Dedicated to the memory of Professor H. Sachs.

### 1 Introduction

We use standard notation. In particular, V (G) denotes the vertex set of a graph G, E(G) denotes the edge set of G, and e(G) = |E(G)|. Also, if v ∈ V (G), then N(v) denotes the neighborhood of v and d(v) = |N(v)|. Ore [4] proved the following Tur´n-type result:

Theorem 1 (Ore [4]). If G is a nonhamiltonian graph on n vertices, then e(G) ≤ n−21 + 1.

This bound is achieved only for the n-vertex graph obtained from the complete graph Kn−1 by adding a vertex of degree 1. Erd˝s [2] reﬁned the bound in terms of the minimum degree of the graph:

∗Alfre´d R´enyi Institute of Mathematics, Hungary E-mail: furedi.zoltan@renyi.mta.hu. Research supported in part by the Hungarian National Science Foundation OTKA 104343, by the Simons Foundation Collaboration Grant 317487, and by the European Research Council Advanced Investigators Grant 267195.

†University of Illinois at Urbana–Champaign, Urbana, IL 61801 and Sobolev Institute of Mathematics, Novosibirsk 630090, Russia. E-mail: kostochk@math.uiuc.edu. Research of this author is supported in part by NSF grants DMS1266016 and DMS-1600592 and grants 15-01-05867 and 16-01-00499 of the Russian Foundation for Basic Research.

‡University of Illinois at Urbana–Champaign, Urbana, IL 61801, USA. E-mail: ruthluo2@illinois.edu.

- Theorem 2 (Erd˝s [2]). Let n,d be integers with 1 ≤ d ≤ n−21 , and set h(n,d) := n−2d + d2. If G is a nonhamiltonian graph on n vertices with minimum degree δ(G) ≥ d, then

e(G) ≤ max h(n,d),h(n,

n − 1 2

) =: e(n,d).

This bound is sharp for all 1 ≤ d ≤ n−21 .

To show the sharpness of the bound, for n,d ∈ N with d ≤ n−21 , consider the graph Hn,d obtained from a copy of Kn−d, say with vertex set A, by adding d vertices of degree d each of which is adjacent to the same d vertices in A. An example of H11,3 is below.

Figure 1: H11,3

By construction, Hn,d has minimum degree d, is nonhamiltonian, and e(Hn,d) = n−2d + d2 = h(n,d). Elementary calculation shows that h(n,d) > h(n, n−21 ) in the range 1 ≤ d ≤ n−21 if and only if d < (n + 1)/6 and n is odd or d < (n + 4)/6 and n is even. Hence there exists a d0 := d0(n) such that

e(n,1) > e(n,2) > ··· > e(n,d0) = e(n,d0 + 1) = ··· = e(n,

n − 1 2

),

where d0(n) := n+16 if n is odd, and d0(n) := n+46 if n is even. Let H n,d denote the graph that is an edge-disjoint union of two complete graphs Kn−d and Kd+1 sharing one vertex.

The result of this note is the following reﬁnement of Theorem 2.

- Theorem 3. Let n ≥ 3 and d ≤ n−21 . Suppose that G is an n-vertex nonhamiltonian graph with minimum degree δ(G) ≥ d such that

e(G) > e(n,d + 1) = max h(n,d + 1),h(n,

n − 1 2

) . (1)

(So we have d < d0(n).) Then G is a subgraph of either Hn,d or H n,d.

This is a stability result in the sense that for d < n/6, each 2-connected, nonhamilitonian n-vertex graph with minimum degree at least d and “close” to h(n,d) edges is a subgraph of the extremal graph Hn,d. Note that h(n,d) − h(n,d + 1) = n − 3d − 2 is at least n/2 for d < d0 − 1. Note also that e(H n,d) > e(n,d + 1) only when d = O(√n).

We will use the following well-known theorems of P´sa.

- Theorem 4 (P´sa [5]). Let n ≥ 3. If G is a nonhamiltonian n-vertex graph, then there exists


- 1 ≤ k ≤ n−21 such that G has a set of k vertices with degree at most k.


- Theorem 5 (P´sa [6]). Let n ≥ 3, 1 ≤ < n and let G be an n-vertex graph such that d(u) + d(v) ≥ n + for every non-edge uv in G. Then for every linear forest F with edges contained in G, the graph G has a hamiltonian cycle containing all edges of F.


### 2 Proof of Theorem 3

Call a graph G saturated if G is nonhamiltonian but for each uv ∈/ E(G), G+uv has a hamiltonian cycle. Ore’s proof [4] of Dirac’s Theorem [1] yields that

for every n-vertex saturated graph G and for each uv ∈/ E(G), d(u) + d(v) ≤ n − 1. (2)

First we show two facts on saturated graphs with many edges.

- Lemma 6. Let G be a saturated n-vertex graph with e(G) > h(n, n−21 ). Then for some 1 ≤ k ≤ n−1

2 , V (G) contains a subset D of k vertices of degree at most k such that G − D is a complete graph.

Proof. Since G is nonhamiltonian, by Theorem 4, there exists some 1 ≤ k ≤ n−21 such that G has k vertices with degree at most k. Pick the maximum such k, and let D be the set of the vertices

with degree at most k. Since e(G) > h(n, n−21 ), k < n−21 . So, by the maximality of k, |D| = k. Suppose there exist x,y ∈ V (G) − D such that xy ∈/ E(G). Among all such pairs, choose x and y with the maximum d(x). Since y ∈/ D, d(y) > k. Let D := V (G) − N(x) − {x} and k := |D | = n − 1 − d(x). By (2),

d(z) ≤ n − 1 − d(x) = k for all z ∈ D . (3)

So D is a set of k vertices of degree at most k . Since y ∈ D , k ≥ d(y) > k. Thus by the maximality of k, we get k = n − 1 − d(x) > n−21 . Equivalently, d(x) < n−21 . For all z ∈ D +{x}, either z ∈ D where d(z) ≤ k ≤ n−21 , or z ∈ V (G)−D, and so d(z) ≤ d(x) ≤ n−21 . It follows that e(G) ≤ h(n, n−21 ), a contradiction.

- Lemma 7. Under the conditions of Lemma 6, if k = δ(G), then G = Hn,δ(G) or G = H n,δ(G).


Proof. Set d := δ(G), and let D be a set of d vertices with degree at most d. Let u ∈ D. Since δ(G) ≥ |D| = d, u has a neighbor w ∈ V (G) − D. Consider any v ∈ D − {u}. By Lemma 6, w is adjacent to all of V (G) − D − {w}. It also is adjacent to u, therefore its degree is at least n − d. We obtain

d(w) + d(v) ≥ (n − d) + d = n. Then by (2), w is adjacent to v, and hence w is adjacent to all vertices of D. Let W be the set of vertices in V (G) − D having a neighbor in D. We have obtained that W = ∅ and

N(u) ∩ (V (G) − D) = W for all u ∈ D. (4)

Let G = G[D ∪ W]. If |W| = 1, then G = H n,d. If |V (G )| = 2d, then by (4), each vertex u ∈ D has the same d neighbors in V (G)−D. Because d(u) = d, D is an independent set. Thus G = Hn,d. Otherwise, d + 2 ≤ |V (G )| ≤ 2d − 1, |D| ≥ 2.

Fix a pair of vertices w1,w2 ∈ W. For any x,y ∈ V (G ), d(x) + d(y) ≥ d + d ≥ |V (G )| + 1.

Therefore by Theorem 5, G has a hamiltonian cycle C that uses the edge w1w2. Since G := G − (V (G ) − {w1,w2}) is a complete graph, it contains a hamiltonian w1,w2-path P. Then P ∪ (C − w1w2) is a hamiltonian cycle of G, a contradiction.

Proof of Theorem 3. Suppose that an n-vertex, nonhamiltonian graph G satisﬁes the constraints of Theorem 3 for some 1 ≤ d ≤ n−21 . We may assume G is saturated, since if a graph containing G is a subgraph of Hn,d or H n,d, then G is as well.

By Lemma 6, G has a set D of k ≤ n−21 vertices with degree at most k such that G − D is a complete graph. Therefore e(G) ≤ n−2k + k2 = h(n,k). If k > d, then e(G) ≤ max{h(n,d + 1),h(n, n−21 )} = e(n,d+1), a contradiction. Thus k ≤ d. Furthermore, k ≥ δ(G) ≥ d, and hence k = d. Also, since e(G) > h(n, n−21 )), we have d + 1 ≤ d0(n) ≤ (n + 8)/6. Applying Lemma 7 completes the proof.

Acknowledgment. We thank both referees for their helpful comments. Acknowledgment added on April 5, 2017. We have learned that Theorem 3 has already been proved by Li and Ning as a lemma in [3] with a somewhat diﬀerent proof.

### References

- [1] G. Dirac, Some theorems on abstract graphs, Proc. London Math. Soc. (3) 2 (1952), 69–81.
- [2] P. Erd˝s, Remarks on a paper of P´sa, Magyar Tud. Akad. Mat. Kutat´ Int. K¨zl. 7 (1962), 227–229.
- [3] B. Li and B. Ning, Spectral analougues of Erd˝s’ and Moon-Moser’s theorems on Hamilton cycles, Linear Multilinear Algebra, 64 (2016), no.11, 1152–1169.
- [4] O. Ore, Arc coverings of graphs, Acta Math. Acad. Sci. Hung. 10 (1959), 337–356.
- [5] L. P´sa, A theorem concerning Hamilton lines, Magyar Tud. Akad. Mat. Kutat´ Int. K¨zl. 7

(1962), 225–226.

- [6] L. P´sa, On the circuits of ﬁnite graphs, Magyar. Tud. Akad. Mat. Kutat´ Int. K˝zl. 8 (1963/1964), 355–361.


