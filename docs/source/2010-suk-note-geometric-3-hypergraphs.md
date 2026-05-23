---
type: source
kind: paper
title: A note on geometric 3-hypergraphs
authors: Andrew Suk
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1010.5716v3
source_local: ../raw/2010-suk-note-geometric-3-hypergraphs.pdf
topic: general-knowledge
cites:
---

arXiv:1010.5716v3[math.CO]9Nov2011

A note on geometric 3-hypergraphs

Andrew Suk∗ November 22, 2018

Abstract

In this note, we prove several Tur´an-type results on geometric hypergraphs. The two main theorems are 1) Every n-vertex geometric 3-hypergraph in the plane with no three strongly crossing edges has at most O(n2) edges, 2) Every n-vertex geometric 3-hypergraph in 3-space with no two disjoint edges has at most O(n2) edges. These results support two conjectures that were raised by Dey and Pach, and by Akiyama and Alon.

# 1 Introduction

A geometric r-hypergraph H in d-space is a pair (V,E), where V is a set of points in general position in Euclidean d-space, and E is a set of closed (r−1)-dimensional simplices (edges) induced by some r-tuple of V . The sets V and E are called the vertex set and edge set of H, respectively. Two edges in H are crossing if they are vertex disjoint and have a point in common. Notice that if k edges are pairwise crossing, it does not imply that they all have a point in common. Hence we say that H contains k strongly crossing edges if H contains k vertex disjoint edges that all share a point in common. See Figure 1.

(a) Three strongly crossing edges.

(b) Three pairwise crossing edges with an empty intersection.

(c) Three edges not strongly crossing since two share a vertex.

Figure 1: Three edges of a geometric 3-hypergraph in the plane. A direct application of the colored Tverberg theorem (see [3],[20]) gives

![image 1](<2010-suk-note-geometric-3-hypergraphs_images/imageFile1.png>)

∗Courant Institute, New York and EPFL, Lausanne. Email: suk@cims.nyu.edu. The author gratefully acknowledges the support from the Swiss National Science Foundation, Grant No. 200021-125287/1.

- Theorem 1.1. Let exd(SCkd+1,n) denote the maximum number of edges an n-vertex geometric (d + 1)-hypergraph in d-space has with no k strongly crossing edges. Then

exd(SCkd+1,n) = O nd+1−

1

![image 2](<2010-suk-note-geometric-3-hypergraphs_images/imageFile2.png>)

(2k−1)d .

Dey and Pach [5] showed that exd(SC2d+1,n) = Θ(nd), and conjectured exd(SCkd+1,n) = Θ(nd) for every ﬁxed d and k. The lower bound can easily be seen by taking all edges with a vertex in

common. The main motivation for their conjecture is for deriving upper bounds on the maximum number of k-sets of an n-point set in Rd. See [12] for more details. In this note, we settle the DeyPach conjecture for geometric 3-hypergraphs in the plane with no three strongly crossing edges, and improve the upper bound of ex2(SCk3,n).

- Theorem 1.2. ex2(SC33,n) = Θ(n2).
- Theorem 1.3. For ﬁxed k ≥ 4, ex2(SCk3,n) ≤ O(n3−k1 ).

![image 3](<2010-suk-note-geometric-3-hypergraphs_images/imageFile3.png>)

As a related result, Akiyama and Alon [2] used the Borsuk-Ullam Theorem [4] to show the following.

- Theorem 1.4. Let exd(Dkd,n) denote the maximum edges that an n-vertex geometric d-hypergraph in d-space has with no k pairwise disjoint edges. Then

exd(Dkd,n) ≤ nd−(1/k)d−1.

They conjecture that for every ﬁxed d and k, exd(Dkd,n) = Θ(nd−1). Again the lower bound can easily be seen by taking all edges with a vertex in common. Pach and To¨ro˝csik [15] showed

that ex2(Dk2,n) = O(k4n), which was later improved to O(k2n) by To´th [17]. Here we settle the Akiyama-Alon conjecture for geometric 3-hypergraphs in 3-space with no two disjoint edges.

- Theorem 1.5. ex3(D23,n) = Θ(n2). For clarity of the proofs, we do not make any attempts to optimize the constants.


# 2 Strongly crossing edges in the plane

In this section we will prove Theorems 1.2 and 1.3. Recall that a geometric graph is a graph drawn in the plane with vertices represented by points and edges by straight line segments connecting the corresponding pairs. Recently Ackerman [1] showed the following.

Lemma 2.1. Let G = (V,E) be an n-vertex geometric graph in the plane with no four pairwise crossing edges. Then |E(G)| ≤ O(n).

We note that Lemma 2.1 holds for topological graphs. Before we give the proofs, we will introduce some terminology. Consider a family S = {s1,...,sk} of pairwise crossing segments in the plane, and let L = {l1,...,lk} be a family of lines such that li is the line supported by segment si. Recall that the level of a point x ∈ ∪L is deﬁned as the number of lines of L lying strictly below x. We

Figure 2: The top level of four pairwise crossing segments is drawn thick.

deﬁne the top level of L as the closure of the set of points in ∪L with level k −1. We deﬁne the top level of S to be the top level of L. See Figure 2. Notice that L is a (not strictly) convex function.

For each edge t in a geometric 3-hypergraph in the plane, we deﬁne its base as the side with the longest x-projection. We deﬁne the other two sides of t as its left and right side. See Figure 2. Notice that every edge in a geometric 3-hypergraph is incident to a vertex that lies strictly above or below its base. We are now ready to prove Theorem 1.2.

right side left side

base

Figure 3: The base, left side, and right side.

- Proof of Theorem 1.2. Let H = (V,E) be an n-vertex geometric 3-hypergraph in the plane with no three strongly crossing edges. We can assume that |E(H)| ≥ 20n2 (since otherwise we would be done) and at most |E(H)|/2 edges in H are incident to a vertex that lies strictly below its base. We will discard all such edges, leaving us with at least |E(H)|/2 edges left. Let Euv be the set of edges in H with base uv. We discard all sets Euv for which |Euv| ≤ |E(H)|/(2n2). Since we have thrown away at most |E(H)|/4 edges in this process, we have at least |E(H)|/4 edges left. Therefore |Euv| = 0 or |Euv| ≥ |E(H)|/(2n2) ≥ 10.


Now let Gv = (V,E) denote the geometric graph with V (Gv) = V (H) and xy ∈ E(Gv) if conv(x ∪ y ∪ v) ∈ E(H) with base xy. Observation 2.2. Gv does not contain four pairwise crossing edges (bases).

Proof. For sake of contradiction, suppose Gv contains four pairwise crossing edges b1,b2,b3,b4 ∈ E(Gv). Then v lies above bi for all i. Let L denote the top level of the arrangement S = {b1,b2,b3,b4}. Now the proof falls into three cases.

- Case 1. Suppose L intersects exactly two members of S, say bases b1 and b2 (in order from left to right along L). Let p be the intersection point of b1 and b2. Then the vertical line through p must intersect b3 below p. Moreover, since segments b1 and b3 cross, v and the right-endpoint of b3 must lie on the same half-plane generated by the line supported by b1. Likewise, v and the left-endpoint of b3 must lie on the same half-plane generated by the line supported by b2. Therefore


- p ∈ conv(v ∪ b3). See Figure 4(a). Since |Eb1|,|Eb2| ≥ 10, there exists vertices x,y ∈ V (H) such that conv(v ∪ b3),conv(x ∪ b1),conv(y ∪b2) are three (vertex disjoint) strongly crossing edges in H and we have a contradiction.
- Case 2. Suppose L intersects exactly three members of S, say bases b1,b2,b3 (in order from left to right along L). Now b4 must intersect b2 either to the left or right of b2 ∩ L. Without loss of generality, we can assume that b4 intersects b2 to the right of b2 ∩L. Let p be the intersection point of segments b2 and b3. By the same argument as above, p ∈ conv(v ∪ b4). See Figure 4(b). Since

- |Eb1|,|Eb2| ≥ 10, there exists vertices x,y ∈ V (H) such that conv(v ∪ b4),conv(x ∪ b1),conv(y ∪ b2) are three strongly crossing edges in H and we have a contradiction.

Case 3. Suppose L intersects b1,b2,b3,b4 in order from left to right along L. Let p be the intersection point of segments b2 and b3, and let l be the vertical line through v. Since the right endpoint of b4 lies to the right of l, and the left endpoint of b1 lies to the left of l, we have p ∈ conv(v∪b1)∪conv(v∪b4). Therefore, either conv(v ∪ b1) or conv(v ∪ b4) (say conv(v ∪ b1)) contains p. See Figure 4(c). Since

- |Eb2|,|Eb3| ≥ 10, there exists vertices x,y ∈ V (H) such that conv(v ∪ b1),conv(x ∪ b2),conv(y ∪ b3) are three strongly crossing edges in H and we have a contradiction.




v

### L

b

1

b3

b

2

(a) Case 1.

v

L

b b

1 2

b4

b

3

(b) Case 2.

Figure 4: Three cases.

v L

b1 b

- 2
- 3


b

b

4

(c) Case 3.

Therefore by Lemma 2.1, |E(Gv)| ≤ O(n) for every vertex v ∈ V (H). Hence

|E(H)| 4

![image 4](<2010-suk-note-geometric-3-hypergraphs_images/imageFile4.png>)

|E(Gv)| = O(n2),

≤

v∈V (H)

which implies |E(H)| = O(n2).

Before we prove Theorem 1.3, we will need the following lemma due to Valtr [18].

- Lemma 2.3. Let G = (V,E) be an n-vertex geometric graph in the plane such that all of the edges in G intersect the y-axis. If G does not contain k pairwise crossing edges, then |E(G)| ≤ ckn where ck depends only on k.


- Proof of Theorem 1.3. Let H be an n-vertex geometric 3-hypergraph in the plane with no k strongly crossing edges for k ≥ 4. Just as before, we can assume at most |E(H)|/2 of the edges in


H are incident to a vertex that lies strictly below its base. We discard all such edges, leaving us with at least |E(H)|/2 edges left in H. Now we make the following observation.

Observation 2.4. Suppose b1,...,bk are k pairwise crossing bases and v1,...,vk ∈ V (H) such that conv(vi ∪ bj) ∈ E(H) with base bj for all i,j. Then H contains k strongly crossing edges.

Proof. Let L denote the top level of the segment arrangement S = {b1,...,bk} and assume that b1,...,bk are ordered by increasing slopes. See Figure 5.

L

b

- 1
- 2


b

b

- 3
- 4


b

Figure 5: Arrangement of b1,b2,b3,b4.

Now we deﬁne edges t1,t2,...,tk ∈ E(H) as follows. Among the k edges conv(b1 ∪v1),conv(b1 ∪ v2),...,conv(b1 ∪ vk) ∈ E(H), (with slight abuse of notation) let t1 = conv(b1 ∪ v1) be the edge whose right side has the rightmost intersection with L. Then among the k − 1 edges conv(b2 ∪ v2),conv(b2 ∪ v3),...,conv(b2 ∪ vk), (again with slight abuse of notation) let t2 = conv(b2 ∪ v2) be the edge whose right side has the rightmost intersection with L. We continue this procedure until we have k edges t1,t2,...,tk. Clearly these k edges are vertex disjoint.

Now notice that (ti ∩L)∩(tj ∩L) = ∅ for all pairs i,j. Indeed for sake of contradiction, suppose there exists two edges ti and tj for i < j such that either ti ∩ L lies completely to the left of tj ∩ L or vice versa. See Figure 6.

vi

vj

vj

L

vi

b

bi

i

b

j

b

j

##### L

Figure 6: Assume (ti ∩ L) ∩ (tj ∩ L) = ∅.

- Case 1. Suppose ti ∩ L lies completely to the left of tj ∩ L. Then the vertical line through vj intersects the right side of ti below vj. Therefore the right side of conv(bi ∪vj) intersects L more to the right than the right side of ti = conv(bi ∪ vi) does. This contradicts the deﬁnition of ti and tj.


- Case 2. Suppose ti ∩ L lies completely to the right of tj ∩ L. Then there exists a base bs that has a point p on L between ti ∩ L and tj ∩ L. Base bs must


- 1. lie below vi and vj,
- 2. cross bi and bj, and
- 3. contain point p.


However this impossible by the following argument. Let l be the vertical line through p. Clearly l intersects bi and bj. Since bs lies below vi and vj, bs must intersect bj to the left of l, and intersect bi to the right of l. Since bs intersects bj to the left of l, the slope of bs must be greater than the slope of bj. However since the slope of bi is less than the slope of bj, this implies that bs cannot intersect bi to the right of l. Hence we have a contradiction.

l

vi L

vj

p

b

i

b

j

Figure 7: Case 2.

Since (ti ∩ L) ∩ (tj ∩ L) = ∅ for every i,j ∈ {1,2,..,k}, by Helly’s Theorem [6] t1,...,tk has a nonempty intersection on L.

Notice that no k points in V (H) have ckn bases in common. Indeed, otherwise the vertical line through any of these k points would intersect all ckn bases, and by Lemma 2.3 there would be k pairwise crossing bases. By Observation 2.4, we would have k strongly crossing edges.

Now let G = (A ∪ B,E) be a bipartite graph where A = V (H) and B = V 2(H), such that

(v,xy) ∈ E(G) if conv(x ∪ y ∪ v) ∈ E(H) with base xy. Since G does not contain Kk,ckn as a subgraph, we can use the following well known result of Ko˝v´ari, So´s, Tura´n [10].

Theorem 2.5. If G = (A ∪ B,E) is a bipartite graph with |A| = n and |B| = m containing no subgraph Kr,s with the r vertices in A and the s vertices in B, then

|E(G)| ≤ (s − 1)1/rnm1−1/r + (r − 1)m.

By plugging in the values m = n2,r = k,s = ckn into Theorem 2.5, we obtain

|E(H)| 2

≤ |E(G)| ≤ O n3−k1 . Hence

![image 5](<2010-suk-note-geometric-3-hypergraphs_images/imageFile5.png>)

![image 6](<2010-suk-note-geometric-3-hypergraphs_images/imageFile6.png>)

|E(H)| ≤ O n3−k1 .

![image 7](<2010-suk-note-geometric-3-hypergraphs_images/imageFile7.png>)

## 2.1 Convex geometric 3-hypergraphs

In the case when the vertices are in convex position in the plane, extremal problems on geometric 3-hypergraphs become easier due to the linear ordering of its vertices. The proof of Observation 2.4 can be copied almost verbatim to conclude the following.

Observation 2.6. Let H = (V,E) be a geometric 3-hypergraph in the plane with vertices in convex position. Suppose H contains k edges of the form ti = conv(xi ∪ yi ∪ zi), such that the vertices (x1,...,xk,y1,...,yk,z1,...,zk) appear in clockwise order along the boundary of their convex hull. Then t1,...,tk are k strongly crossing edges.

Marcus and Klazar [9] extended the Marcus-Tardos theorem [13] by showing that the number of 1-entries in a r-dimensional (0,1)-matrix with side length n which avoids an r-dimensional permutation matrix is O(nr−1). As pointed out by Marcus and Klazar, it is not diﬃcult to modify their proof to obtain an O(nr−1) bound on the number of edges in an ordered n-vertex r-uniform hypergraph that does not contain a ﬁxed ordered matching. Hence by Observation 2.6, we can conclude the following.

Theorem 2.7. Let H = (V,E) be a geometric 3-hypergraph in the plane with vertices in convex position. If H does not contain k strongly crossing edges, then |E(H)| ≤ ckn2 where ck is a constant that depends only on k.

# 3 Disjoint edges in 3-space

In this section, we will prove Theorem 1.5. Recall that two edges in a geometric graph are parallel if they are the opposite edges of a convex quadrilateral. Katchalski and Last [7] and Pinchasi [16] showed that all n-vertex geometric graphs with more than 2n − 2 edges contain two parallel edges. By following Pinchasi’s argument almost verbatim, one can prove the following.

- Lemma 3.1. Let G be a graph drawn on the unit sphere S with vertices represented as points such that no three lie on a great circle, and edges uv ∈ E(G) are drawn as arcs along the great circle containing points u and v of length less than π (the shorter arc). We say that edges e1,e2 ∈ E(G) are avoiding if the great circle supported by e1 is disjoint to e2, and the great circle supported by e2 is disjoint from e1. If |E(G)| > 2n − 2, then G contains two avoiding edges.


Proof of Theorem 1.5. Let H = (V,E) be an n-vertex geometric 3-hypergraph in 3-space with no two disjoint edges. Fix a pair of vertices u,v ∈ V (H), and just consider the edges Euv = {t ∈ E(H) : u,v are vertices of t}. We color t ∈ Euv red if all of the members of Euv lie in one of the closed half-spaces generated by the plane supported by t. Notice that there are at most two red edges in Euv. Repeat this procedure for each pair of vertices, which will leave us with at most n2 red edges in the end. Color the remaining edges blue, and let db(v) denote the number of blue edges incident to v. Then we have

db(v) ≥ 3E(H) − 3n2.

v∈V (H)

Therefore, there exists a vertex v incident to at least (3|E(H)| − 3n2)/n blue edges. Now consider a small 2-dimensional sphere S2 centered at v. Then the intersection of S2 and the blue edges incident to v forms a graph G with at most n vertices and at least (3E(H) − 3n2)/n edges.

If (3|E(H)|−3n2)/n > 2n−2, then by Lemma 3.1 we know that G contains two avoiding edges xy and wz. Let h be the plane supported by the blue edge conv(w ∪ z ∪ v) ∈ E(H). Then the blue edge conv(x ∪ y ∪ v) must lie in one of the closed half-spaces generated by the plane h. Since

- conv(w ∪ z ∪ v) is blue, there must be a red edge conv(w ∪ z ∪ p) such that h separates it from
- conv(x∪y ∪v). Hence conv(x∪y ∪v) and conv(w ∪z ∪p) are disjoint and we have a contradiction. See Figure 8. Therefore (3|E(H)| − 3n2)/n ≤ 2n − 2, which implies |E(H)| ≤ O(n2).


p

y

z

v w

x

Figure 8: Disjoint edges conv(w ∪ z ∪ p) and conv(x ∪ y ∪ v).

# 4 Remarks

By applying the Abstract Crossing Lemma (see [19]) to Theorem 1.2, every n-vertex geometric 3-hypergraph H in the plane has either O(n2) edges or Ω(|E(H)|7/n12) triples that have a point in common. In the latter case, by the fractional Helly theorem [8] this implies one can always ﬁnd a point inside at least Ω(|E(H)|5/n12) edges of H. However, this is not as strong as the

Ω

bound obtained by Nivasch and Sharir [14].

|E(H)|3 n6 log2 n

![image 8](<2010-suk-note-geometric-3-hypergraphs_images/imageFile8.png>)

# References

- [1] Ackerman, E.: On the maximum number of edges in topological graphs with no four pairwise crossing edges. In Proceedings of the Twenty-Second Annual Symposium on Computational Geometry (Sedona, Arizona, USA, June 05 - 07, 2006). SCG ’06. ACM, New York, NY, 259-263.
- [2] Akiyama, J. and Alon, N.: Disjoint simplices and geometric hypergraphs. In Proceedings of the Third international Conference on Combinatorial Mathematics (New York City, New York, United States). G. S. Bloom, R. L. Graham, and J. Malkevitch, Eds. New York Academy of Sciences, New York, NY, 1-3, 1989.
- [3] Alon, N., B´ara´ny, I., Fu¨redi, Z., and Kleitman, D.J.: Point selections and weak ǫ-nets for convex hulls. Combin. Probab. Comput., 1:189-200, 1992.
- [4] Borsuk, K.: Drei Sa¨tze ber die n-dimensionale euklidische Sph¨are, Fund. Math., 20 (1933), 177-190.
- [5] Dey, T. K. and Pach, J.: Extremal Problems for Geometric Hypergraphs. In Proceedings of the 7th international Symposium on Algorithms and Computation (December 16-18, 1996).
- [6] Helly, E.: Uber¨ Mengen konvexer Ko¨rper mit gemeinschaftlichen Punkten, Jber. Deutsch. Math. Vereinig. 32, 175-176 (1923).
- [7] Katchalski, M. and Last, L.: On geometric graphs with no two edges in convex position, Discrete Comput. Geom. 19 (1998), no. 3, Special Issue, 399-404.
- [8] Katchalski, M., Liu, A.: A problem of geometry in Rn . Proc. Am. Math. Soc. 75, 284-288

(1979).

- [9] Klazar, M., Marcus, A.: Extensions of the linear bound in the Fu¨redi-Hajnal conjecture, Adv. in Appl. Math. 38 (2006), no. 2, 258-266.
- [10] Ko˝v´ari, T., So´s, V., Tura´n, P.: On a problem of K. Zarankiewicz. Coll. Math., 3:50-57, 1954.
- [11] Marcus, A. and Tardos, G.: Excluded permutation matrices and the Stanley-Wilf conjecture. J. Comb. Theory Ser. A 107, 1 (Jul. 2004), 153-160, 2004.
- [12] Matousˇek, J.: 2002 Lectures on Discrete Geometry. Springer-Verlag New York, Inc.
- [13] Marcus, A. and Tardos, G.: Excluded permutation matrices and the Stanley-Wilf conjecture, J. Combin. Theory Ser. A 107 (2004), no. 1, 153-160.
- [14] Nivasch, G. and Sharir, M.: Note: Eppstein’s bound on intersecting edges revisited. J. Comb. Theory Ser. A 116, 2 (Feb. 2009), 494-497.
- [15] Pach, J. and To¨ro˝csik, J.: Some geometric applications of Dilworth’s theorem. In Proceedings of the Ninth Annual Symposium on Computational Geometry (San Diego, California, United States, May 18 - 21, 1993). SCG ’93. ACM, New York, NY, 264-269.
- [16] Pinchasi, R.: Geometric graphs with no two parallel edges. Combinatorica 28, 1 (Jan. 2008), 127-130, 2008.


- [17] To´th, G.: Note on geometric graphs. J. Comb. Theory Ser. A 89, 1 (Jan. 2000), 126-132, 2000.
- [18] Valtr, P.: Graph drawings with no k pairwise crossing edges, In Graph Drawing (Rome), Lecture Notes in Computer Science, vol. 1353, 1997, pp. 205-218.
- [19] Wagner. U.: k-Sets and k-Facets, Discrete and Computational Geometry - 20 Years Later (Eli Goodman, Ja´nos Pach, and Ricky Pollack, eds.), Contemporary Mathematics 453, American Mathematical Society, 2008.
- [20] Zivaljevic´,ˇ R. T. and Vrec´ica, S. T.: The colored Tverberg’s problem and complexes of injective functions. J. Comb. Theory Ser. A 61, 2 (Nov. 1992), 309-318, 1992.


