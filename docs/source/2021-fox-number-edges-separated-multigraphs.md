---
type: source
kind: paper
title: On the number of edges of separated multigraphs
authors: Jacob Fox, Janos Pach, Andrew Suk
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2108.11290v2
source_local: ../raw/2021-fox-number-edges-separated-multigraphs.pdf
topic: general-knowledge
cites:
---

arXiv:2108.11290v2[math.CO]22Feb2022

On the number of edges of separated multigraphs

Jacob Fox∗ J´nos Pach† Andrew Suk‡

Abstract

We prove that the number of edges of a multigraph G with n vertices is at most O(n2 log n), provided that any two edges cross at most once, parallel edges are noncrossing, and the lens enclosed by every pair of parallel edges in G contains at least one vertex. As a consequence, we prove the following extension of the Crossing Lemma of Ajtai, Chv´atal, Newborn, Szemer´edi and Leighton, if G has e ≥ 4n edges, in any drawing of G with the above property, the number of crossings is Ω e

3

n2 log(e/n) . This answers a question of Kaufmann et al. and is tight up to the logarithmic factor.

![image 1](<2021-fox-number-edges-separated-multigraphs_images/imageFile1.png>)

# 1 Introduction

A topological graph is a graph drawn in the plane such that its vertices are represented by points, and the edges are represented by simple continuous arcs connecting the corresponding pairs of points. In notation and terminology, we do not distinguish between the vertices and the points representing them and the edges and the arcs representing them. The edges are allowed to intersect, but they cannot pass through any vertex other than their endpoints. If two edges share an interior point, then they must properly cross at that point, i.e., one edge passes from one side of the other edge to its other side.

A multigraph is a graph in which two vertices can be joined by several edges. Two edges that join the same pair of vertices are called parallel.

According to the crossing lemma of Ajtai, Chv´atal, Newborn, Szemere´di [1] and Leighton [6],

every topological graph G with n vertices and e > 4n edges has at least cne32 edge crossings, where c > 0 is an absolute constant. In notation, we have

![image 2](<2021-fox-number-edges-separated-multigraphs_images/imageFile2.png>)

e3 n2

. (1)

cr(G) ≥ c ·

![image 3](<2021-fox-number-edges-separated-multigraphs_images/imageFile3.png>)

In a seminal paper which was an important step towards the solution of Erd˝os’s famous problem on distinct distances [4], Sze´kely [14] generalized the crossing lemma to multigraphs: for every

![image 4](<2021-fox-number-edges-separated-multigraphs_images/imageFile4.png>)

∗Stanford University, Stanford, CA. Supported by a Packard Fellowship and by NSF award DMS-1855635. Email: jacobfox@stanford.edu.

†Re´nyi Institute, Budapest and MIPT, Moscow. Supported by NKFIH grants K-176529, KKP-133864, Austrian Science Fund Z 342-N31, Ministry of Education and Science of the Russian Federation MegaGrant No. 075-15-20191926, ERC Advanced Grant “GeoScape.” Email: pach@cims.nyu.edu.

‡Department of Mathematics, University of California at San Diego, La Jolla, CA, 92093 USA. Supported an NSF CAREER award, NSF award DMS-1952786, and an Alfred Sloan Fellowship. Email: asuk@ucsd.edu.

topological multigraph G with n vertices and e > 4n edges, in which the multiplicity of every edge is at most m, we have

e3 mn2

. (2)

cr(G) ≥ c

![image 5](<2021-fox-number-edges-separated-multigraphs_images/imageFile5.png>)

As the maximum multiplicity m increases, (2) gets weaker. However, as was shown in [11] and [5], under certain special conditions on the multigraphs, the inequality (1) remains true, independently of m. Some related results were established in [12]. In all of these papers, one of the key elements of the argument was to ﬁnd an analogue of Euler’s theorem for the corresponding classes of “nearly planar” multigraphs.

Throughout this paper, we consider only single-crossing topological multigraphs, i.e., we assume that any two edges cross at most once. Hence, two edges that share an endpoint may also have a common interior point. Two edges are said to be independent if they do not share an endpoint, and they are called disjoint if they are independent and do not cross.

Deﬁnition 1.1. A multigraph G is called separated if no two parallel edges of G cross, and the “lens” enclosed by them has at least one vertex in its interior.

It was conjectured in [5] that any separated single-crossing topological multigraph with n vertices has at most O(n2) edges. The aim of this note is to verify this conjecture apart from a logarithmic factor.

Theorem 1.2. The number of edges of a separated single-crossing topological multigraph G on n vertices satisﬁes |E(G)| ≤ 64n2 log n.

Note that in a separated multigraph, any pair of vertices can be connected by at most n − 1 edges. This immediately implies the bound |E(G)| ≤ n2 (n − 1) = O(n3).

If we plug in Theorem 1.2 into the machinery of [11] and [5], a routine calculation gives the following. Corollary 1.3. Every separated single-crossing topological multigraph on n vertices and e ≥ 4n edges has at least 10−25n2 log(e3e/n) crossings.

![image 6](<2021-fox-number-edges-separated-multigraphs_images/imageFile6.png>)

For simplicity, we will assume that a multigraph does not have loops. It is easy to see that Theorem 1 also holds for topological multigraphs with loops, assuming that each loop contains a vertex.

Theorem 1.2 does not remain true if we replace the assumption that G is single-crossing by the weaker one that any two edges cross at most twice. To see this, let the vertices of G lie on the x-axis: set V (G) = {1,2,... ,n}. Let each edge consist of a semicircle in the upper half-plane and a semicircle below it that meet at a point of the x-axis. More precisely, for any pair of integers i,j ∈ V (G) with i < j, and for any k with i ≤ k < j, pick a distinct point pikj in the open interval (k,k + 1). Let γikj be the union of two semicircles centered at the x-axis: an upper semicircle connecting i to pikj and a lower one connecting pikj to j. Let E(G) consist of all arcs γikj over all triples i ≤ k < j. Observe that any two edges of G cross at most twice: once above the x-axis and once below it. No two parallel edges, γihj and γikj with h < k, cross each other, and the region enclosed by them contains the vertex k ∈ V (G). Therefore, G is a separated topological multigraph with i,j(i<j)(j − i) = Ω(n3).

The proof of Theorem 1.2 is presented in the next section, and the proof of Corollary 1.3 can be found in the subsequent section.

All logarithms used in the sequel are of base 2. We omit all ﬂoor and ceiling signs wherever they are not crucially important.

- 2 Proof of Theorem 1.2 We will need the following simple lemma.


- Lemma 2.1. Let G be a single-crossing topological graph on n vertices with no parallel edges, in which every pair of independent edges cross. Then we have |E(G)| ≤ 4n.


Proof. Let V (G) = A ∪ B be a bipartition of the vertex set such that at least half of the edges of G run between A and B. Denote the corresponding bipartite graph by G(A,B). Any pair of independent edges of G(A,B) cross once, that is, an odd number of times. Assume without loss of generality that A and B are separated by a horizontal line. By “ﬂipping” one of the half-planes bounded by this line from left to right, we obtain a drawing of G(A,B), in which any pair of independent edges cross an even number of times. According to the Hanani-Tutte theorem [15, 13], this implies that G(A,B) is a planar graph. Any bipartite planar graph on n ≥ 3 vertices has at most 2n − 4 edges. Therefore, |E(G)| ≤ 2|E(G(A,B))| ≤ 4n − 8.

![image 7](<2021-fox-number-edges-separated-multigraphs_images/imageFile7.png>)

![image 8](<2021-fox-number-edges-separated-multigraphs_images/imageFile8.png>)

![image 9](<2021-fox-number-edges-separated-multigraphs_images/imageFile9.png>)

![image 10](<2021-fox-number-edges-separated-multigraphs_images/imageFile10.png>)

Proof of Theorem 1.2. Let G = (V,E) be a separated single-crossing topological multigraph on n vertices. If two vertices, u and v, are joined by j > 1 parallel edges, then they cut the plane into j pieces, one of which is unbounded. The bounded pieces are called lenses. Each lens is bounded by two adjacent edges joining a pair of vertices. Let L denote the set of lenses determined by G.

If |L| ≤ |E(2G)|, then keeping only one edge between every pair of adjacent vertices, we obtain a simple graph G′ whose number of edges satisﬁes

![image 11](<2021-fox-number-edges-separated-multigraphs_images/imageFile11.png>)

|E(G)| 2 ≤ |E(G′)| ≤

![image 12](<2021-fox-number-edges-separated-multigraphs_images/imageFile12.png>)

This implies that |E(G)| < n2, and we are done. From now on, we can and will assume that

n 2

.

|E(G)| 2

|L| ≥

. (3)

![image 13](<2021-fox-number-edges-separated-multigraphs_images/imageFile13.png>)

For any lens ℓ ∈ L, let |ℓ| denote the number of vertices in the interior of ℓ. For t = log n, we partition L into t parts, L1 ∪ L2 ∪ ··· ∪ Lt, where ℓ ∈ Li if and only of 2i−1 ≤ |ℓ| < 2i. By the pigeonhole principle, there is an integer k,1 ≤ k ≤ t, such that

|L| log n

. (4)

|Lk| ≥

![image 14](<2021-fox-number-edges-separated-multigraphs_images/imageFile14.png>)

Fix an integer k with the above property, and let dk(v) denote the number of lenses in Lk that contain vertex v in its interior. Then we have

|ℓ| ≥ |Lk|2k−1.

dk(v) =

v∈V

ℓ∈Lk

Hence, there is a vertex v ∈ V that lies in the interior of at least |Lk|2kn−1 lenses from Lk. Assume without loss of generality that v is located at the origin o, and let Lo denote the set of lenses in Lk which contain the origin. Hence, we have

![image 15](<2021-fox-number-edges-separated-multigraphs_images/imageFile15.png>)

2k−1 n

|Lo| ≥ |Lk| ·

.

![image 16](<2021-fox-number-edges-separated-multigraphs_images/imageFile16.png>)

Combining this with (3) and (4), we obtain

|E(G)| nlog n · 2k−2. (5)

|Lo| ≥

![image 17](<2021-fox-number-edges-separated-multigraphs_images/imageFile17.png>)

Let Go denote the subgraph of G consisting of all vertices and the edges that bound a lens in Lo. Any two vertices of Go are connected by 0 or 2 edges of Go.

Now we use the idea of the probabilistic proof of the crossing lemma; see [8]. Let W be a random subset of V in which each vertex is picked independently with probability p = 2−k. Let Go[W] be the subgraph of Go induced by W. Let Lo(W) denote the set of empty lenses in Go[W] (that is, the set of lenses with empty interiors). For the expected values of |W| and |Lo(W)|, we have

E[|W|] = pn and

E[|Lo(W)|] ≥ p2(1 − p)2k|Lo|. By linearity of expectation, there is a subset W′ of V such that

|Lo(W′)| − 4|W′| ≥ E[|Lo(W)|] − 4E[|W|] ≥ p2(1 − p)2k|Lo| − 4pn. (6)

For each lens in ℓ ∈ Lo(W′), we arbitrarily pick one of the two edges enclosing ℓ, and denote the resulting simple topological graph by G′. We now make the following observation.

- Lemma 2.2. Any two independent edges of G′ cross each other.


Proof. Suppose, for contradiction, that G′ has two independent edges, e and e′, which do not cross. Let ℓ and ℓ′ be the corresponding empty lenses in Go[W′]. Since the interiors of ℓ and ℓ′ are empty, neither of them can contain an endpoint of the other. Both of these lenses contain the origin o, which implies that they cannot be disjoint. Therefore, both sides of ℓ must cross both sides of ℓ′, contradicting the choice of e and e′. Here, we used the assumption that G and, hence, G′ are single-crossing.

![image 18](<2021-fox-number-edges-separated-multigraphs_images/imageFile18.png>)

![image 19](<2021-fox-number-edges-separated-multigraphs_images/imageFile19.png>)

![image 20](<2021-fox-number-edges-separated-multigraphs_images/imageFile20.png>)

![image 21](<2021-fox-number-edges-separated-multigraphs_images/imageFile21.png>)

In view of Lemma 2.2, we can apply Lemma 2.1 to G′. We obtain |E(G′)| = |Lo(W′)| ≤ 4|W′| and hence by (6) we have p2(1 − p)2k|Lo| ≤ 4pn. It follows that

|Lo| ≤ 4p−1(1 − p)−2kn. Substituting p = 2−k, we get

|Lo| ≤ 16 · 2kn. Comparing this with (5), we conclude that

|E(G)| ≤ 64n2 log n. This completes the proof of Theorem 1.2.

![image 22](<2021-fox-number-edges-separated-multigraphs_images/imageFile22.png>)

![image 23](<2021-fox-number-edges-separated-multigraphs_images/imageFile23.png>)

![image 24](<2021-fox-number-edges-separated-multigraphs_images/imageFile24.png>)

![image 25](<2021-fox-number-edges-separated-multigraphs_images/imageFile25.png>)

# 3 Proof of Corollary 1.3

The bisection width of a graph is deﬁned as the minimum number of edges whose deletion separates the graph into parts each containing at most a fraction 4/5 of the vertices. For our purposes, the constant 4/5 is not so important, and any positive constant less than 1 will do. A bound on the bisection width of a graph in terms of the crossing number and the degree sequence of the graph was established by Pach, Shahrokhi, and Szegedy [9] through an application of the Lipton-Tarjan separator theorem [7]. It was applied to obtain a new proof and various generalizations of the crossing lemma [10], [3], [5].

The proof of Corollary 1.3 follows the same general strategy as the new proof of the crossing lemma in [10], although, importantly, we need to work with a topological variant of the bisection width, introduced in [11]. Given a separated single-crossing topological graph G = (V,E), let b(G) denote the minimum number of edges we need to delete from G so that there is a vertex partition V = V1 ∪ V2 such that

- (i) |V1|,|V2| ≤ 4|V (G)|/5,
- (ii) there is no remaining edge between V1 and V2, and
- (iii) for i = 1,2, the subgraph Gi ⊂ G[Vi] formed by the remaining edges of G[Vi] is a separated


single-crossing topological graph. Our proof of Corollary 1.3 is based on the following statement.

Lemma 3.1. Let G be a separated single-crossing topological graph on n vertices with degree sequence d1,... ,dn and c(G) crossings. Then

![image 26](<2021-fox-number-edges-separated-multigraphs_images/imageFile26.png>)

n

d2i + n.

b(G) ≤ 22 c(G) +

i=1

Lemma 3.1 was proved in [11], in the special case where no two edges of G incident to the same vertex cross each other. The argument in [11] goes through to the general case without any change. In fact, it also remains valid for other “drawing styles” (see [5], Theorem 2).

Proof of Corollary 1.3. Let G be a separated single-crossing topological graph on n vertices with e edges, degree sequence d1,... ,dn, and c(G) crossings. Similar to (Corollary 2.2 of [11]), we have

- c(G) ≥ e − 3n through an application of Euler’s polyhedral formula. This bound is suﬃcient for e < 1012n. We may therefore assume e ≥ 1012n.

Let ∆ := ⌈2e/n⌉. By locally splitting each vertex of G whose degree is larger than ∆ into vertices of degree ∆, with possibly one additional vertex of degree less than ∆, we obtain another separated single-crossing topological graph G′ with e edges, c(G) crossings, and with at most 2n vertices of maximum degree at most ∆ := ⌈2e/n⌉. Denoting the number of vertices of G′ by n′, we have n ≤ n′ ≤ 2n.

Let k = 10−10 n2 log(e2e/n). Note that k ≥ ∆, as e ≥ 1012n. Let F0 = {G′}. We consider a process where at step i = 1,2,... we create a family Fi of vertexdisjoint subgraphs of G′, each of which is a separated single-crossing topological graph. Throughout the process, we maintain the property, true for i = 0, that each member H ∈ Fi either satisﬁes

![image 27](<2021-fox-number-edges-separated-multigraphs_images/imageFile27.png>)

- c(H) ≥ ke(H) or has at most (4/5)in′ vertices. Assume that this property is satisﬁed at step i. At step i + 1, we construct Fi+1 from Fi, as follows. For each H ∈ Fi, if c(H) ≥ ke(H) or H has at most (4/5)i+1n′ vertices, then place H in Fi+1. Otherwise, we have c(H) < ke(H) and the number


of vertices of H is at least (4/5)i+1n′ and at most (4/5)in′. In this case, we apply Lemma 3.1 to H: by deleting b(H) edges from H, we obtain two vertex-disjoint separated single-crossing topological subgraphs, H1 and H2, each of which has at most 54v(H) vertices. We place H1 and H2 in Fi+1. Obviously, the resulting family Fi+1 has the desired property.

![image 28](<2021-fox-number-edges-separated-multigraphs_images/imageFile28.png>)

Next, we bound the number of edges that were deleted from the members of Fi to obtain Fi+1. For each H ∈ Fi which does not belong to Fi+1, we have c(H) < ke(H). It follows from Lemma 3.1 that the number of edges we deleted from H to obtain H1 and H2 is at most

- b(H) ≤ 22 c(H) + ∆e(H) + v(H) ≤ 22 ke(H) + ∆e(H) + v(H) ≤ 40 ke(H) + v(H) .

![image 29](<2021-fox-number-edges-separated-multigraphs_images/imageFile29.png>)

![image 30](<2021-fox-number-edges-separated-multigraphs_images/imageFile30.png>)

![image 31](<2021-fox-number-edges-separated-multigraphs_images/imageFile31.png>)

![image 32](<2021-fox-number-edges-separated-multigraphs_images/imageFile32.png>)

Since each H ∈ Fi which does not belong to Fi+1 has at least (4/5)i+1n′ vertices, the number of H with this property is at most n′/ (4/5)in′ = (5/4)i+1. As the sum of e(H) with H ∈ Fi is at most e, we obtain H∈F

i\Fi+1 e(H) ≤ (5/4)i+1√e. Similarly, H∈F

![image 33](<2021-fox-number-edges-separated-multigraphs_images/imageFile33.png>)

![image 34](<2021-fox-number-edges-separated-multigraphs_images/imageFile34.png>)

![image 35](<2021-fox-number-edges-separated-multigraphs_images/imageFile35.png>)

i\Fi+1 v(H) ≤ (5/4)i+1√n′. Hence, in going from Fi to Fi+1, at most 40(5/4)(i+1)/2 √ke + √n edges were deleted, in total.

![image 36](<2021-fox-number-edges-separated-multigraphs_images/imageFile36.png>)

![image 37](<2021-fox-number-edges-separated-multigraphs_images/imageFile37.png>)

![image 38](<2021-fox-number-edges-separated-multigraphs_images/imageFile38.png>)

![image 39](<2021-fox-number-edges-separated-multigraphs_images/imageFile39.png>)

![image 40](<2021-fox-number-edges-separated-multigraphs_images/imageFile40.png>)

We stop at the last step i0 such that (5/4)i0/2 ≤ 10−3(e/k)1/2. In total, in getting from step 0 to step i0, the number of edges we have deleted is at most

i0−1

i=0

40(5/4)(i+1)/2

√

![image 41](<2021-fox-number-edges-separated-multigraphs_images/imageFile41.png>)

ke + √n ≤ 500(5/4)i0/2

![image 42](<2021-fox-number-edges-separated-multigraphs_images/imageFile42.png>)

√

![image 43](<2021-fox-number-edges-separated-multigraphs_images/imageFile43.png>)

ke ≤ e/2.

Hence, the members of Fi0 contain, in total, at least e/2 edges. On the other hand, each graph H ∈ Fi0 either satisﬁes c(H) ≥ ke(H) or has at most v := (4/5)i0n′ ≤ 3 · 106kn/e vertices. By Theorem 1.2, each graph H of the latter type has at most 64v2 log v edges. In total, the number of edges in all members H in Fi0 of the latter type is at most 64n′v log v ≤ 2·109kn2e−1 log(n/e) = e/5. Hence, there are at least e/2 − e/5 = 3e/10 edges of G′ which are in graphs H in Fi0 with

- c(H) ≥ ke(H). Therefore, in these subgraphs altogether we have at least k(3e/10) ≥ 10−11n2 log(e3e/n) crossings. All of them are distinct crossings in the original graph G, which completes the proof. References


![image 44](<2021-fox-number-edges-separated-multigraphs_images/imageFile44.png>)

![image 45](<2021-fox-number-edges-separated-multigraphs_images/imageFile45.png>)

![image 46](<2021-fox-number-edges-separated-multigraphs_images/imageFile46.png>)

![image 47](<2021-fox-number-edges-separated-multigraphs_images/imageFile47.png>)

![image 48](<2021-fox-number-edges-separated-multigraphs_images/imageFile48.png>)

- [1] M. Ajtai, V. Chv´atal, M. N. Newborn, and E. Szemere´di: Crossing-free subgraphs, in: Theory and Practice of Combinatorics, North-Holland Mathematics Studies 60, North-Holland, Amsterdam, 9–12, 1982.
- [2] N. Alon, P. Seymour, and R. Thomas: Planar separators, SIAM J. Discrete Math. 7 (1994), no. 2, 184–193.
- [3] D. Bokal, E.´ Czabarka, L. Sze´kely, and I. Vrt’o: General lower bounds for the minor crossing number of graphs, Discrete Comput. Geom. 44 (2010), no. 2, 463–483.
- [4] L. Guth and N. H. Katz: On the Erd˝os distinct distances problem in the plane, Ann. of Math. 181 (2015), no. 1, 155–190.
- [5] M. Kaufmann, J. Pach, G. To´th, and T. Ueckerdt: The number of crossings in multigraphs with no empty lens, J. Graph Algorithms Appl. 25 (2021), no. 1, 383–396.


- [6] T. Leighton: Complexity Issues in VLSI, Foundations of Computing Series, MIT Press, Cambridge, 1983.
- [7] R. J. Lipton and R. E. Tarjan, A separator theorem for planar graphs, SIAM J. Appl. Math. 36 (1979), no. 2, 177–189.
- [8] J. Matousˇek: Lectures on Discrete Geometry. Graduate Texts in Mathematics 212, SpringerVerlag, New York, 2002.
- [9] J. Pach, F. Shahrokhi, and M. Szegedy: Applications of the crossing number, Algorithmica 16

(1996), no. 1, 111–117.

- [10] J. Pach, J. Spencer, and G. To´th: New bounds on crossing numbers, Discrete Comput. Geom. 24 (2000), no. 4, 623–644.
- [11] J. Pach and G. To´th: A crossing lemma for multigraphs, Discrete Comput. Geom. 63 (2020), no. 4, 918–933.
- [12] J. Pach, G. Tardos, and G. To´th: Crossings between non-homotopic edges, in: Graph Drawing and Network Visualization, Lecture Notes in Comput. Sci. 12590, Springer-Verlag, Cham, 2020, 359–371.
- [13] M. Schaefer: Toward a theory of planarity: Hanani-Tutte and planarity variants, J. Graph Algorithms Appl. bf 17 (2013), no. 4, 367–440.
- [14] L. A. Sze´kely: Crossing numbers and hard Erd˝os problems in discrete geometry, Combin. Probab. Comput. 6 (1997), no. 3, 353–358.
- [15] W. T. Tutte: Toward a theory of crossing numbers, J. Combinatorial Theory 8 (1970), 45–53.


