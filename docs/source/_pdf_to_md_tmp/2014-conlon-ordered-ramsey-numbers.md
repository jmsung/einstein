arXiv:1410.5292v2[math.CO]25Apr2016

Ordered Ramsey numbers

David Conlon∗ Jacob Fox† Choongbum Lee‡ Benny Sudakov§

Abstract

Given a labeled graph H with vertex set {1,2,...,n}, the ordered Ramsey number r<(H) is the minimum N such that every two-coloring of the edges of the complete graph on {1,2,...,N} contains a copy of H with vertices appearing in the same order as in H. The ordered Ramsey number of a labeled graph H is at least the Ramsey number r(H) and the two coincide for complete graphs. However, we prove that even for matchings there are labelings where the ordered Ramsey number is superpolynomial in the number of vertices. Among other results, we also prove a general upper bound on ordered Ramsey numbers which implies that there exists a constant c such that r<(H) ≤ r(H)clog

2 n for any labeled graph H on vertex set {1,2,...,n}.

# 1 Introduction

Given a graph H, the Ramsey number r(H) is deﬁned to be the smallest natural number N such that every two-coloring of the edges of KN contains a monochromatic copy of H. That these numbers exist was ﬁrst proved by Ramsey [34] and rediscovered independently by Erd˝os and Szekeres [14].

The most famous question in graph Ramsey theory is that of estimating the Ramsey number r(Kn) of the complete graph Kn on n vertices. However, despite some smaller order improvements [9, 35], the standard estimates [13, 14] that 2n/2 ≤ r(Kn) ≤ 22n have remained largely unchanged for nearly seventy years. After the complete graph, the next most classical topic in the area is the study of Ramsey numbers of sparse graphs, that is, graphs with certain upper bound constraints on the degrees of their vertices. This direction was pioneered by Burr and Erd˝os [6] in 1975 and the topic has since played a central role in graph Ramsey theory.

Answering a question of Burr and Erd˝os, Chv´atal, Ro¨dl, Szemere´di and Trotter [7] proved that for every ∆ there is c(∆) such that every graph H on at most n vertices with maximum degree ∆ satisﬁes r(H) ≤ c(∆)n. That is, Ramsey numbers of bounded-degree graphs grow linearly in the number of vertices. Another stronger conjecture of Burr and Erd˝os remained open until very recently. We say that a graph is d-degenerate if every subgraph has a vertex of degree at most d.

![image 1](<2014-conlon-ordered-ramsey-numbers_images/imageFile1.png>)

∗Mathematical Institute, Oxford OX2 6GG, United Kingdom. Email: david.conlon@maths.ox.ac.uk. Research supported by a Royal Society University Research Fellowship.

†Department of Mathematics, Stanford University, Stanford, CA 94305. Email: jacobfox@stanford.edu. Research supported by a Packard Fellowship, by NSF Career Award DMS-1352121 and by an Alfred P. Sloan Fellowship.

‡Department of Mathematics, MIT, Cambridge, MA 02139-4307. Email: cb lee@math.mit.edu. Research supported by NSF Grant DMS-1362326

![image 2](<2014-conlon-ordered-ramsey-numbers_images/imageFile2.png>)

§Department of Mathematics, ETH, 8092 Zurich, Switzerland. Email: benjamin.sudakov@math.ethz.ch. Research supported in part by SNSF grant 200021-149111.

Equivalently, a graph is d-degenerate if there is an ordering v1,v2,... ,vn of its vertices such that each vertex vi has at most d neighbors vj with j < i. Burr and Erd˝os conjectured that for every d there is c(d) such that every d-degenerate graph H on at most n vertices satisﬁes r(H) ≤ c(d)n. Building on earlier work by several authors [2, 20, 21, 26, 27], this conjecture has now been solved by Lee [28].

In this paper, we will study analogues of these results for ordered graphs. An ordered graph or labeled graph H on n vertices is a graph whose vertices have been labeled with {1,2,... ,n}. An ordered graph G on [N] := {1,2,... ,N} contains an ordered graph H on [n] if there is a mapping φ : [n] → [N] such that φ(i) < φ(j) for 1 ≤ i < j ≤ n and (φ(i),φ(j)) is an edge of G whenever (i,j) is an edge of H. Given an ordered graph H, the ordered Ramsey number r<(H) is deﬁned to be the smallest natural number N such that every two-coloring of the edges of the complete graph on [N] contains a monochromatic ordered copy of H. The natural analogue of this function for q colors will be denoted by r<(H;q).

In some sense, the study of ordered Ramsey numbers is as old as Ramsey theory itself. One of the most famous results in the classic 1935 paper of Erd˝os and Szekeres [14] states that every sequence x1,x2,... ,xr of r ≥ (n−1)2+1 distinct real numbers contains an increasing or decreasing subsequence of length n. To prove this, consider a red/blue-coloring of the edges of the complete graph on vertex set [r] where (i,j) with i < j is red if xi < xj and blue otherwise. Note that a subsequence is increasing or decreasing if and only if it forms a monotone monochromatic path in this edge coloring. We may therefore assume that there is no monotone red path of length n. We now label each vertex by the length of the longest monotone red path ending at that vertex. It is easy to see that any set of vertices with the same label forms a blue clique. Therefore, since there are only n−1 possible labels and r ≥ (n−1)2 +1 vertices, we may conclude that there exists a blue clique of order at least n and the result of Erd˝os and Szekeres follows. In proving this result, we have also shown that r<(Pn) ≤ (n − 1)2 + 1, where Pn is the monotone path with n vertices. Since this is easily seen to be tight, we have r<(Pn) = (n − 1)2 + 1. More generally, for q colors instead of 2, the q-color ordered Ramsey number of the monotone path satisﬁes r<(Pn;q) = (n − 1)q + 1.

Another foundational result in Ramsey theory, known as the happy ending theorem, also has a natural proof using ordered Ramsey numbers. This result, again due to Erd˝os and Szekeres [14], states that for each positive integer n there is an integer N such that every set of N points in the plane in general position (that is, with no three on a line) contains n points which are the vertices of a convex polygon. We write g(n) for the smallest such N. To estimate g(n), it will be useful to generalize the concept of ordered Ramsey numbers to hypergraphs. That is, given an ordered k-uniform hypergraph H and a positive integer q, we let r<(H;q) be the smallest natural number N such that every q-coloring of the edges of the complete k-uniform hypergraph on [N] contains a monochromatic ordered copy of H.

Suppose now that we have N points in the plane in general position. By rotating the plane if necessary, we may assume that no two points are on a vertical line. Denote the N points by pi = (xi,yi) with x1 < ... < xN. A set P of points in the plane forms a cup (respectively, cap) if the points in P lie on the graph of a convex (respectively, concave) function. Note that both cups and caps form convex polygons. Consider a red/blue-coloring of the edges of the complete 3-uniform hypergraph on {1,2,... ,N} where {i,j,k} with i < j < k is red if {pi,pj,pk} form a cup and blue

if {pi,pj,pk} form a cap. If we write Pn(k) for the monotone k-uniform tight path on {1,2,... ,n}, where {i,i+1,... ,i+k −1} is an edge for 1 ≤ i ≤ n−k +1, then we see that a sequence of points forms a cap or a cup if and only if the corresponding vertices form a monochromatic ordered copy of Pn(3). Hence, g(n) ≤ r<(Pn(3)), which is known to equal 2nn−−24 + 1.

An extension of the happy ending theorem proved by Pach and T´oth [33] shows that for every positive integer n there is an integer N such that every set of N convex sets in the plane in general position contains n convex sets which are in convex position. We write h(n) for the smallest such N. It was shown by Fox, Pach, Sudakov and Suk [18] that h(n) ≤ r<(Pn(3);3), leading the authors to study the growth of ordered hypergraph Ramsey numbers for monotone paths. The results of [18], and subsequent improvements made by Moshkovitz and Shapira [31], show that for k ≥ 3 the ordered Ramsey number r<(Pn(k);q) grows as a (k − 2)-fold exponential in nq−1. This is in stark contrast to the classical unordered problem, where the Ramsey number of Pn(k) grows linearly in the number of vertices for all uniformities k. More recently, ordered Ramsey numbers for tight paths were also used by Milans, Stolee and West [30] to give bounds on the minimum number of interval graphs whose union is the line graph of Kn.

While there has been much progress on understanding the ordered Ramsey numbers of monotone paths, there has been surprisingly little work on more general ordered graphs and hypergraphs. In this paper, we attempt to bridge this gap by conducting a more systematic study of ordered Ramsey numbers, focusing on the case of graphs. We note that a similar study was conducted independently by Balko, Cibulka, Kra´l and Kyncˇl [4] and that there are overlaps between many of our results.

One of the more striking aspects of the discussion above is the vast diﬀerence between the usual Ramsey number and the ordered Ramsey number for monotone paths of high uniformity. Our ﬁrst result shows that a large gap exists already for graphs, even when the graph is as simple as a matching, where the ordinary Ramsey number is clearly linear. Here and throughout the paper, all logs are taken to base 2.

- Theorem 1.1. There exists a positive constant c such that, for all even n, there exists an ordered matching M on n vertices with


r<(M) ≥ nclogn/log logn. This lower bound actually holds for almost every ordering of a matching on n vertices, so that

- Theorem 1.1 represents typical rather than atypical behavior. An almost matching upper bound is provided by the following simple theorem (which, in a slightly weaker form, also follows from a result of Cibulka, Gao, Krcˇ´l, Valla and Valtr [8]).
- Theorem 1.2. For any ordered matching M on n vertices, r<(M) ≤ n⌈logn⌉.


More generally, we can prove that there exists a constant c such that for any ordered graph H on n vertices with degeneracy d, r<(H) ≤ ncdlogn, where the degeneracy of an ordered graph H is the smallest d for which the corresponding unordered graph is d-degenerate. This is a special case of an even more general result. To state this result, we deﬁne the interval chromatic number χ<(H) of an ordered graph H to be the minimum number of intervals into which the vertex set of

H may be partitioned so that no two vertices in the same interval are adjacent. This is similar to the notion of chromatic number but now the independent sets must also be intervals in the given ordering. For any graph H, it is easy to see that there is an ordering of the vertices of H such that the interval chromatic number is the same as the chromatic number.

Interval chromatic number plays a key role in the study of extremal problems on ordered graphs (see, for example, [32]). In particular, Pach and Tardos [32] observed that the maximum number ex<(n,H) of edges an ordered graph on n vertices can have without containing the ordered graph H is

1 χ<(H) − 1

n 2

1 −

+ o(1)

. The following result shows that it also plays a fundamental role in ordered Ramsey theory.

![image 3](<2014-conlon-ordered-ramsey-numbers_images/imageFile3.png>)

- Theorem 1.3. There exists a constant c such that for any ordered graph H on n vertices with degeneracy d and interval chromatic number χ,

r<(H) ≤ ncdlogχ.

In particular, this result implies that there are orderings under which the ordered Ramsey number of a d-degenerate graph with n vertices is polynomial in n. The following result shows that restricting the interval chromatic number is still not enough to force the ordered Ramsey number to be linear, even for matchings. It is also close to best possible, since an elementary argument (see Section 2) shows that r<(M) ≤ n2 for any matching M with n vertices and interval chromatic number 2.

- Theorem 1.4. There exists a positive constant c such that, for all even n, there exists an ordered matching M on n vertices with interval chromatic number 2 and

r<(M) ≥

cn2 log2 nlog log n

![image 4](<2014-conlon-ordered-ramsey-numbers_images/imageFile4.png>)

.

So far, our results have focused on very sparse graphs. For denser graphs, the ordered Ramsey number behaves more like the usual Ramsey number. Indeed, we have the following result, which generalizes a result of the ﬁrst author [10] in two ways: ﬁrstly, by estimating the ordered Ramsey number rather than just the usual Ramsey number and, secondly, by replacing maximum degree with degeneracy.

- Theorem 1.5. There exists a constant c such that for any ordered graph H on n vertices with degeneracy at most d,


r<(H) ≤ 2cdlog2(2n/d).

This result is close to sharp when d is very large and also, by Theorem 1.1, when d is very small. We note two simple corollaries of this theorem. The ﬁrst, proved for the usual Ramsey number in [10], says that for any graph on n vertices with o(n2) edges, the ordered Ramsey number is 2o(n). This follows by noting that any graph on n vertices with at most δn2 edges has degeneracy at most (2δ)1/2n and substituting into Theorem 1.5. More precisely, we have the following result.

- Corollary 1.6. There exists a constant c such that for any ordered graph H on n vertices with at most δn2 edges,

r<(H) ≤ 2c

√

![image 5](<2014-conlon-ordered-ramsey-numbers_images/imageFile5.png>)

δlog2(1/δ)n.

Since any graph H with degeneracy at least d contains a subgraph of minimum degree at least d, a simple application of the probabilistic method implies that the Ramsey number of H must be at least 2d2. Using also the elementary observation that r(H) ≥ n, we have the following corollary.

![image 6](<2014-conlon-ordered-ramsey-numbers_images/imageFile6.png>)

- Corollary 1.7. There exists a constant c such that for any ordered graph H on n vertices with degeneracy d,


r<(H) ≤ r(H)cγ(H), where γ(H) = min{log2(n/d),dlog(n/d)}.

It is also interesting to deﬁne an oﬀ-diagonal variant of the ordered Ramsey number. Given two ordered graphs G and H, we deﬁne the ordered Ramsey number r<(G,H) to be the smallest natural number N such that any two-coloring of the edges of the complete graph on vertex set [N] in red and blue, say, contains either a red ordered copy of G or a blue ordered copy of H. To give an example, we note that the proof of the Erd˝os–Szekeres theorem on monotone subsequences given earlier actually shows that

r<(Pm,Kn) = (m − 1)(n − 1) + 1. (1)

In the classical case, the most intensively studied oﬀ-diagonal Ramsey number is r(Kn,K3). It is easy to see that r(Kn,K3) ≤ n2 and a well-known result of Ajtai, Komlo´s and Szemere´di [3] improves this to r(Kn,K3) = O(logn2n). In a remarkable breakthrough, Kim [24] showed that this upper bound is essentially tight, that is, that r(Kn,K3) = Ω(logn2n). Recent advances in the study of triangle-free processes [5, 16] have led to further improvements in these bounds, so that r(Kn,K3) is now known up to an asymptotic factor of 4.

![image 7](<2014-conlon-ordered-ramsey-numbers_images/imageFile7.png>)

![image 8](<2014-conlon-ordered-ramsey-numbers_images/imageFile8.png>)

The main oﬀ-diagonal problem that we treat in the ordered case is that of determining the ordered Ramsey number r<(M,K3), where M is an ordered matching. For the upper bound, we could only prove the trivial estimate r<(M,K3) ≤ r<(Kn,K3) = O(logn2n). For the lower bound, we have the following result, which improves considerably on the trivial linear bound.

![image 9](<2014-conlon-ordered-ramsey-numbers_images/imageFile9.png>)

- Theorem 1.8. There exists a positive constant c such that, for all even n, there exists an ordered matching M on n vertices with


n log n

4/3

.

r<(M,K3) ≥ c

![image 10](<2014-conlon-ordered-ramsey-numbers_images/imageFile10.png>)

In the next section, we will study the ordered Ramsey number of matchings, proving Theorems 1.1, 1.2 and 1.4. We will also show that the ordered Ramsey number of matchings with bounded bandwidth is at most polynomial in the number of vertices. In Section 3, we will prove Theorems 1.3 and 1.5. The proof of Theorem 1.8 is given in Section 4. We conclude, in Sections 5 and 6, with some further remarks and a collection of open problems. In particular, we observe a connection between ordered Ramsey numbers and hypergraph Ramsey numbers. We also classify those graphs which have linear ordered Ramsey number in every ordering. Throughout the paper, we omit ﬂoor and ceiling signs whenever they are not essential. We also do not make any serious attempt to optimize absolute constants in our statements and proofs.

# 2 Matchings

We begin with a simple upper bound for the ordered Ramsey number of matchings in terms of the number of vertices n and the interval chromatic number χ. By saying that the χ-partite graph Kn′,n′,...,n′ is trivially ordered, we mean that the vertices of each partite set appear as an interval.

- Theorem 2.1. Let M be an ordered matching on [n] and let K = Kn′,n′,...,n′ be a trivially ordered χ-partite graph with χ ≥ 2. Then


r<(M,K) ≤ n⌈logχ⌉n′. In particular, if M is an ordered matching on n vertices of interval chromatic number χ, then

r<(M) ≤ n⌈logχ⌉+1.

Proof. It suﬃces to prove the statement when χ = 2j for positive integers j. We prove this by induction on j. For the base case j = 1, we have to show that r<(M,Kn′,n′) ≤ nn′. To see this, suppose that we are given a two-coloring of the edges of KN1 with N1 = nn′. Partition [N1] into n consecutive intervals V1,V2,... ,Vn, each of length n′. We try to embed a red copy of M by placing vertex i in the set Vi for each i = 1,2,... ,n. If this procedure does not produce a red copy of M, then there are two indices i1 and i2 such that every edge between Vi1 and Vi2 is blue. That is, we ﬁnd either a red copy of M or a blue copy of Kn′,n′.

Let Nj = njn′ and suppose that any two-coloring of the edges of [Nj−1] contains either a red copy of M or a blue copy of the trivially ordered χ-partite graph Kn′,n′,...,n′ with χ = 2j−1. Partition [Nj] into n consecutive intervals V1,V2,... ,Vn, each of length Nj−1. We again try to embed a red copy of M by placing vertex i in the set Vi for each i = 1,2,... ,n. If this procedure does not produce a red copy of M, then there are two indices i1 and i2 such that every edge between Vi1 and Vi2 is blue. Moreover, by the induction hypothesis, either one of Vi1 or Vi2 contains a red copy of M, in which case we are done, or both Vi1 and Vi2 contain a blue copy of the 2j−1-partite graph Kn′,n′,...,n′. Combining the two gives a blue copy of the 2j-partite graph Kn′,n′,...,n′.

![image 11](<2014-conlon-ordered-ramsey-numbers_images/imageFile11.png>)

![image 12](<2014-conlon-ordered-ramsey-numbers_images/imageFile12.png>)

![image 13](<2014-conlon-ordered-ramsey-numbers_images/imageFile13.png>)

![image 14](<2014-conlon-ordered-ramsey-numbers_images/imageFile14.png>)

Since any ordered matching M on n vertices is a subgraph of Kn = K1,1,...,1, the n-partite graph with parts of size 1, we see that r<(M) ≤ r<(M,Kn) ≤ n⌈logn⌉, establishing Theorem 1.2. We will now prove Theorem 1.1 by showing that r<(M) ≥ nclogn/log logn for almost all orderings. We need a simple lemma which says that in a randomly ordered matching with n vertices, that is, an ordered matching chosen uniformly at random from the set of all possible orderings of a matching with n vertices, any two disjoint intervals of length at least 4√nlog n have an edge between them.

![image 15](<2014-conlon-ordered-ramsey-numbers_images/imageFile15.png>)

Lemma 2.2. Let M be a random matching on vertex set [n]. Then, asymptotically almost surely, there is an edge between any two disjoint intervals of length at least 4√nlog n. Proof. Given two disjoint sets A and B of order t, where t is even, the probability that a random matching has no edges between A and B is at most

![image 16](<2014-conlon-ordered-ramsey-numbers_images/imageFile16.png>)

n − t − 1 n − 1

![image 17](<2014-conlon-ordered-ramsey-numbers_images/imageFile17.png>)

n − t − 3 n − 3 ···

![image 18](<2014-conlon-ordered-ramsey-numbers_images/imageFile18.png>)

n − 2t + 1 n − t + 1 ≤

![image 19](<2014-conlon-ordered-ramsey-numbers_images/imageFile19.png>)

n − t n

![image 20](<2014-conlon-ordered-ramsey-numbers_images/imageFile20.png>)

t/2

≤ e−t2/2n,

where the ﬁrst inequality holds since nn−−t−kk < nn−t for all k > 0 and the second inequality follows from the fact that 1−x ≤ e−x for all x. Since there are at most n2 pairs of intervals of length t, the

![image 21](<2014-conlon-ordered-ramsey-numbers_images/imageFile21.png>)

![image 22](<2014-conlon-ordered-ramsey-numbers_images/imageFile22.png>)

probability that there exist two intervals of length t with no edge between them is at most n2e−t2/2n. For t ≥ 3√nlog n, this tends to zero with n. Therefore, taking t to be an even integer between 3√nlog n and 4√nlog n, we see that asymptotically almost surely any two disjoint intervals of length at least t have an edge between them, completing the proof.

![image 23](<2014-conlon-ordered-ramsey-numbers_images/imageFile23.png>)

![image 24](<2014-conlon-ordered-ramsey-numbers_images/imageFile24.png>)

![image 25](<2014-conlon-ordered-ramsey-numbers_images/imageFile25.png>)

![image 26](<2014-conlon-ordered-ramsey-numbers_images/imageFile26.png>)

![image 27](<2014-conlon-ordered-ramsey-numbers_images/imageFile27.png>)

![image 28](<2014-conlon-ordered-ramsey-numbers_images/imageFile28.png>)

![image 29](<2014-conlon-ordered-ramsey-numbers_images/imageFile29.png>)

- Theorem 2.3. Let M be a random matching on vertex set [n]. Then, asymptotically almost surely, r<(M) ≥ nlogn/20 log logn.


Proof. By Lemma 2.2, we may assume that in M any two intervals of length at least 4√nlog n have an edge between them. Let s = ⌊n1/4⌋ and suppose that c is a two-coloring of the edges of the complete graph on vertex set [s] without a monochromatic clique of order log n (such a coloring exists by Ramsey’s theorem).

![image 30](<2014-conlon-ordered-ramsey-numbers_images/imageFile30.png>)

Let G0 be the graph with a single vertex. For i ≥ 1, we recursively deﬁne edge-colored ordered complete graphs Gi as follows. Let Gi,1,Gi,2,... ,Gi,s be vertex disjoint copies of Gi−1. We form Gi by placing these copies of Gi,j in sequential order, that is, placing the vertices of Gi,j before the vertices of Gi,j+1, and, for each 1 ≤ j < j′ ≤ s, adding a complete bipartite graph in color c(j,j′) between the two graphs Gi,j and Gi,j′.

We prove by induction on i that the graph Gi does not contain a monochromatic copy of a subgraph of M induced on a subinterval of size at least n3/4 · (8log n)i (we refer to such subgraphs as subintervals of M). The claim is trivially true for i = 0 since Gi consists of a single vertex. Suppose now that the claim has been proved for Gi−1 and, for the sake of contradiction, suppose that Gi contains a monochromatic subinterval M′ of M of size at least n3/4 · (8log n)i. Abusing notation, we also let M′ denote this copy in Gi. Without loss of generality, we may assume that it is a red copy. For j = 1,2,... ,s, let Wj = V (Gi,j) ∩ V (M′) and note that each Wj forms a subinterval of M. We call a set Wj small if |Wj| < 4√nlog n and large otherwise.

![image 31](<2014-conlon-ordered-ramsey-numbers_images/imageFile31.png>)

There are at most 4√nlog n · s ≤ 4n3/4√log n vertices of M′ in small sets Wj. Therefore, at

![image 32](<2014-conlon-ordered-ramsey-numbers_images/imageFile32.png>)

![image 33](<2014-conlon-ordered-ramsey-numbers_images/imageFile33.png>)

least 21n3/4 · (8log n)i vertices lie in large sets Wj. By our assumption, there exists a red edge of M between every pair of large sets. However, since c does not contain a monochromatic clique of

![image 34](<2014-conlon-ordered-ramsey-numbers_images/imageFile34.png>)

![image 35](<2014-conlon-ordered-ramsey-numbers_images/imageFile35.png>)

order log n, there are fewer than log n large sets Wj. Therefore, for some index j, we have

1 log n ·

|V (Gi,j) ∩ V (M′)| ≥

![image 36](<2014-conlon-ordered-ramsey-numbers_images/imageFile36.png>)

![image 37](<2014-conlon-ordered-ramsey-numbers_images/imageFile37.png>)

- 1

![image 38](<2014-conlon-ordered-ramsey-numbers_images/imageFile38.png>)

- 2


n3/4(8log n)i ≥ n3/4 · (8log n)i−1,

contradicting the induction hypothesis. Since n3/4 · (8log n)logn/4 log(8 logn) = n,

we see that for t = ⌊4 log(8 loglogn n)⌋ the graph Gt does not contain a monochromatic copy of M. Since Gt has st vertices and, for n suﬃciently large, st ≥ n

![image 39](<2014-conlon-ordered-ramsey-numbers_images/imageFile39.png>)

log n

20loglogn, the claimed lower bound follows.

![image 40](<2014-conlon-ordered-ramsey-numbers_images/imageFile40.png>)

![image 41](<2014-conlon-ordered-ramsey-numbers_images/imageFile41.png>)

![image 42](<2014-conlon-ordered-ramsey-numbers_images/imageFile42.png>)

![image 43](<2014-conlon-ordered-ramsey-numbers_images/imageFile43.png>)

![image 44](<2014-conlon-ordered-ramsey-numbers_images/imageFile44.png>)

The only property of M used in the proof of Theorem 2.3 is that there is at least one edge between any two disjoint intervals of length 4√nlog n. Since it is straightforward to construct

![image 45](<2014-conlon-ordered-ramsey-numbers_images/imageFile45.png>)

such matchings explicitly (see the start of Section 4), we also have explicit examples of ordered matchings with superlinear ordered Ramsey number.

It follows from Theorem 2.1 that if M has interval chromatic number 2 then r<(M) ≤ n2. We now show that this is close to best possible. We will construct our matching using the wellknown van der Corput sequence or rather a collection of permutations derived from the van der Corput sequence. To deﬁne these permutations, we take the integers {0,1,... ,2h − 1}, write each as a binary expansion with h digits and reverse its expansion. We call the resulting permutation π : [2h] → [2h] a van der Corput permutation. For n = 2h, these permutations are known to have the property that for any pair of intervals I,J ⊆ [n],

|I||J| n ≤ C log n, (2)

|π(I) ∩ J| −

![image 46](<2014-conlon-ordered-ramsey-numbers_images/imageFile46.png>)

where C is an absolute constant (see, e.g., [29, Chapter 2]). We note that this is a considerably smaller discrepancy than one could hope to achieve using a random permutation. We are now ready to prove Theorem 1.4 in the following form.

- Theorem 2.4. There exists a positive constant c such that for all n = 2h there is a matching of interval chromatic number 2 with 2n vertices satisfying


cn2 log2 nlog log n

r<(M) ≥

.

![image 47](<2014-conlon-ordered-ramsey-numbers_images/imageFile47.png>)

Proof. Let π be the van der Corput permutation. We take M to be the ordered perfect matching with interval chromatic 2 on [2n] which matches i ∈ [n] with n + π(i).

Let s = 8 logn n and t = logn8log logcn n, where c is a suﬃciently small positive constant. Consider a random red/blue-coloring χ of the edges of the complete graph with loops on [t]. Let Ii = [(i−1)s+ 1,is] for 1 ≤ i ≤ t. Let ψ be the red/blue-coloring of the complete graph on [ts], where every edge between Ii and Ij is of color χ(i,j). We will show that with positive probability the edge coloring ψ does not have a monochromatic ordered copy of M and, therefore, r<(M) > ts = log2 ncnlog log2 n. By symmetry between the two colors, it suﬃces to show that the probability that the red graph contains an ordered copy of M is less than 1/2. Note that the red graph is a blow-up of the random graph with loops on [t], where each vertex i is replaced by an interval Ii of length s.

![image 48](<2014-conlon-ordered-ramsey-numbers_images/imageFile48.png>)

![image 49](<2014-conlon-ordered-ramsey-numbers_images/imageFile49.png>)

![image 50](<2014-conlon-ordered-ramsey-numbers_images/imageFile50.png>)

If the coloring ψ contains a red copy of M, then there exists an integer k with 1 ≤ k ≤ t and partitions [n] = A1 ∪···∪Ak, [n+1,2n] = Bk ∪Bk+1∪···∪Bt of the vertex set of M into intervals such that Ai embeds into Ii for all 1 ≤ i ≤ k and Bj embeds into Ij for all k ≤ j ≤ t. Each Ai and Bj has size at most s and if π(Ai) + n contains an element of Bj, then χ(i,j) must be red. We note that there are at most

2n + t

t ≤ e((4c)−1 log nlog log n + 1) t ≤ e9cn/logn diﬀerent partitions of this form. We now ﬁx such a partition.

Let d = 2log n. Let Ai0 be the (d + 1)th largest interval of the form Ai and Bj0 the (d + 1)th largest interval of the form Bj. If |Ai0||Bj0| > Cnlog n, then every interval Ai with size at least |Ai0| and every interval Bj with size at least |Bj0| has an edge of M between them. Therefore, if

the partition gave rise to a monochromatic red copy of M, χ would contain a red complete bipartite graph with parts of size d. The probability of this event is at most

2−d2

t d

2

t2d d!2

1 4

< 2−d2

<

.

![image 51](<2014-conlon-ordered-ramsey-numbers_images/imageFile51.png>)

![image 52](<2014-conlon-ordered-ramsey-numbers_images/imageFile52.png>)

Otherwise, we may suppose that |Ai0||Bj0| ≤ Cnlog n. As each Ai and each Bj has size at most s, there are at most 2ds edges of M coming from some Ai of size larger than Ai0 or some Bj of size larger than |Bj0|. Therefore, there are at least n − 2ds ≥ n/2 edges of M between those Ai and Bj with |Ai| ≤ |Ai0| and |Bj| ≤ |Bj0| and hence between those Ai and Bj with |Ai||Bj| ≤ Cnlog n. By (2), each such pair Ai,Bj has at most |Ai||nBj| +C log n ≤ 2C log n edges between them and thus there are at least 2Cn/log2 n = 4C logn n pairs Ai,Bj for which there is at least one edge of M between Ai and Bj. But this implies that the coloring χ contains a particular red subgraph with at least

![image 53](<2014-conlon-ordered-ramsey-numbers_images/imageFile53.png>)

![image 54](<2014-conlon-ordered-ramsey-numbers_images/imageFile54.png>)

![image 55](<2014-conlon-ordered-ramsey-numbers_images/imageFile55.png>)

n

4C logn edges, which occurs with probability at most 2−n/4C logn. Since the collection of edges is determined by the choice of the Ai and Bj and there are at most e9cn/logn choices for these sets, we therefore see that the probability the coloring ψ contains a red copy of such a graph is at most

![image 56](<2014-conlon-ordered-ramsey-numbers_images/imageFile56.png>)

1 4

e9cn/logn2−n/4C logn <

,

![image 57](<2014-conlon-ordered-ramsey-numbers_images/imageFile57.png>)

for c suﬃciently small. Hence, we see that the probability ψ contains a red copy of M is at most 1/2, completing the proof.

![image 58](<2014-conlon-ordered-ramsey-numbers_images/imageFile58.png>)

![image 59](<2014-conlon-ordered-ramsey-numbers_images/imageFile59.png>)

![image 60](<2014-conlon-ordered-ramsey-numbers_images/imageFile60.png>)

![image 61](<2014-conlon-ordered-ramsey-numbers_images/imageFile61.png>)

The ordered Ramsey number of a matching is not always controlled by the interval chromatic number. For example, despite having interval chromatic number which is linear in n, the ordered Ramsey number of the matching with edges (1,2),(3,4),... ,(n − 1,n) is clearly linear in n. More generally, if we know that a matching has bounded bandwidth with respect to the given ordering, that is, there exists a k such that |i − j| ≤ k for any edge (i,j), then we can show that the ordered Ramsey number is at most a polynomial whose power is dictated by the bandwidth. The proof of this fact relies on the next lemma.

Given two ordered graphs G and H, we deﬁne their ordered lexicographic product G · H to be the graph consisting of t := |H| consecutive ordered copies of G, which we call G1,G2,... ,Gt, with all vertices of Gi joined to all vertices of Gj if and only if (i,j) is an edge of H.

- Lemma 2.5. For any ordered matching M and any ordered graphs G and H, r<(M,G · H) ≤ r<(M,G) · r<(M,H).


Proof. Suppose that we are given a two-coloring of the edges of KN with N = r<(M,G)·r<(M,H). Partition [N] into s := r<(M,H) consecutive intervals V1,V2,... ,Vs, each of length r<(M,G). We consider the reduced graph with s vertices v1,v2,... ,vs, connecting vi and vj in red if there are any edges between Vi and Vj in red and in blue otherwise, that is, if the bipartite graph between Vi and Vj is completely blue. If the reduced graph contains a red ordered copy of M then so does the original graph. We may therefore assume that the reduced graph has a blue ordered copy of H with vertices vi1,vi2,... ,vit, where t := |H|. This gives vertex sets Vi1,Vi2,... ,Vit such that there are complete blue bipartite graphs between vertex sets corresponding to edges of H. Since Vij has

size r<(M,G), we see that either some Vij contains an ordered red copy of M, in which case we are done, or every Vij contains an ordered blue copy of G. In the latter case, we may use the blue edges between pieces to get an ordered blue copy of G · H, completing the proof.

![image 62](<2014-conlon-ordered-ramsey-numbers_images/imageFile62.png>)

![image 63](<2014-conlon-ordered-ramsey-numbers_images/imageFile63.png>)

![image 64](<2014-conlon-ordered-ramsey-numbers_images/imageFile64.png>)

![image 65](<2014-conlon-ordered-ramsey-numbers_images/imageFile65.png>)

The result about bandwidth mentioned earlier is now an easy consequence of this lemma. We say that an ordered graph has bandwidth at most k if |i−j| ≤ k for every edge (i,j). We also write Pnk for the kth power of a path, the ordered graph on [n] where i and j are adjacent if and only if |i − j| ≤ k. Note that an ordered graph on [n] has bandwidth at most k if and only if it is a subgraph of Pnk.

- Theorem 2.6. For any ordered matching M on n vertices and any positive integer k,


r<(M,Pnk) ≤ n⌈logk⌉+2. In particular, if M is an ordered matching on n vertices with bandwidth at most k, then r<(M) ≤ n⌈logk⌉+2. Proof. To begin, note that Pnk is a subgraph of Kk · Pn. By Lemma 2.5, it follows that r<(M,Pnk) ≤ r<(M,Kk) · r<(M,Pn).

- Theorem 2.1 implies that r<(M,Kk) ≤ n⌈logk⌉ and observation (1) from the introduction implies that r<(M,Pn) ≤ r<(Kn,Pn) ≤ n2. The result follows.

![image 66](<2014-conlon-ordered-ramsey-numbers_images/imageFile66.png>)

![image 67](<2014-conlon-ordered-ramsey-numbers_images/imageFile67.png>)

![image 68](<2014-conlon-ordered-ramsey-numbers_images/imageFile68.png>)

![image 69](<2014-conlon-ordered-ramsey-numbers_images/imageFile69.png>)

3 General graphs

In this section, we will prove Theorems 1.3 and 1.5. We begin with Theorem 1.3, which is contained in the following result.

- Theorem 3.1. Let H be an ordered d-degenerate graph on n vertices with maximum degree ∆ and


let K = Kn′,n′,···,n′ be a trivially ordered complete χ-partite graph. Let s = ⌈log χ⌉ and D = 8χ2n′. Then

r<(H,K) ≤ 2s2d+s∆snsDds+1.

In particular, if H is an ordered d-degenerate graph on n vertices with interval chromatic number χ, then

r<(H) ≤ n32dlogχ.

The next lemma is the key technical step in the proof of Theorem 3.1. It says that if a graph on [N] does not contain a copy of a particular ordered d-degenerate graph H then it contains an ordered collection of large subsets with low density between each pair of subsets. In the unordered case, analogues of this result may be found in [19, 23]. To prove the lemma, we will attempt to embed H greedily. If this fails, we can show that there must be two large vertex sets, say A and B, with low density between them. We then repeat this procedure inside the two vertex sets A and B. If there is no copy of H in A, there will be two large vertex subsets A1 and A2 with low density

between them and, similarly, if there is no copy of H in B, there will be two large vertex subsets B1 and B2 with low density between them. Therefore, we have found four large vertex subsets with low density between each pair of subsets. Iterating this procedure yields the result below.

- Lemma 3.2. Let H be an ordered d-degenerate graph on n vertices with maximum degree ∆. Suppose that a real number 0 < c < 1 and a positive integer s ≥ 1 are given and that N ≥ (2∆n(2sc−1)d s. If an ordered graph on vertex set [N] does not contain an ordered copy of H, then there exist sets W1,W2,... ,W2s ⊂ [N] such that


- (i) for all i, |Wi| ≥ (2sdc+1sdN∆n)s,

![image 70](<2014-conlon-ordered-ramsey-numbers_images/imageFile70.png>)

- (ii) for i < j, all vertices in Wi precede all vertices in Wj,
- (iii) for i < j, the density of edges between Wi and Wj is at most c.


Proof. We will prove the statement by induction on s beginning with the base case s = 1. Let v1,v2,... ,vn be a d-degenerate ordering of the vertices of H. Partition [N] into n intervals, each of length at least 2Nn. If the required ordering of the vertices of H is vi1,vi2,... ,vin, then we will label the intervals in order as Vi1,Vi2,... ,Vin.

![image 71](<2014-conlon-ordered-ramsey-numbers_images/imageFile71.png>)

Consider the following process for embedding an ordered copy of H. We will embed vertices one at a time following the degenerate ordering, at step t embedding the vertex vt into the set Vt. To this end, we will try to ﬁnd, by induction, a sequence of vertices w1,w2,... ,wt with wi ∈ Vi for

- i = 1,2,... ,t and sets Vi,t ⊂ Vi for i = t + 1,... ,n satisfying the following properties:


- 1. If i,j ≤ t and vi is adjacent to vj, then wi is adjacent to wj.
- 2. If j ≤ t < i and vi is adjacent to vj, then wj is adjacent to every vertex in Vi,t.
- 3. |Vi,t| ≥ cdi,t|Vi| for all i > t, where di,t is the number of neighbors of vi in {v1,... ,vt}.


If the process reaches step n, Property 1 implies that mapping vi to wi for each i = 1,2,... ,n gives the required ordered copy of H.

To begin the induction, we let Vi,0 = Vi for all i. The properties stated above are then trivially satisﬁed. Suppose now that we have found w1,w2,... ,wt−1 and Vi,t−1 for all i ≥ t and we wish to deﬁne wt and Vi,t for all i > t. Let It = {i > t : vi is adjacent to vt} and note that |It| ≤ ∆. We have

di,t−1 + 1 if i ∈ It, di,t−1 if i ∈/ It.

di,t =

For every i > t with i ∈/ It, let Vi,t = Vi,t−1 and note that these sets satisfy Properties 2 and 3 above. For a vertex w ∈ Vt,t−1 and an index i ∈ It, let Vi,t(w) be the set of neighbors of w in Vi,t−1. If there exists a vertex w ∈ Vt,t−1 such that

|Vi,t(w)| ≥ c|Vi,t−1| ≥ cdi,t−1+1|Vi| = cdi,t|Vi|

for all i ∈ It, then we may set Vi,t = Vi,t(w) for i ∈ It, take wt = w and proceed to the next step. If this is not the case, then for each vertex w in Vt,t−1 there exists an index i ∈ It for which

|Vi,t(w)| < c|Vi,t−1|. By the pigeonhole principle, there exists an index i ∈ It such that there are at least

1 ∆

N 2∆n

1 |It|

cdt,t−1|Vt| ≥ cdt,t−1

· |Vt,t−1| ≥

![image 72](<2014-conlon-ordered-ramsey-numbers_images/imageFile72.png>)

![image 73](<2014-conlon-ordered-ramsey-numbers_images/imageFile73.png>)

![image 74](<2014-conlon-ordered-ramsey-numbers_images/imageFile74.png>)

vertices in Vt,t−1 which all have at most c|Vi,t−1| neighbors in Vi,t−1. Let W1 be these vertices and W2 = Vi,t−1. Then

cdN 2∆n

|W1|,|W2| ≥

.

![image 75](<2014-conlon-ordered-ramsey-numbers_images/imageFile75.png>)

Relabeling W1 and W2 if necessary, we have found sets W1 and W2 satisfying conditions (i), (ii) and (iii) of the lemma. That is, if we cannot ﬁnd an ordered copy of H, we can ﬁnd sets W1 and W2 satisfying properties (i), (ii), and (iii). In fact, W1 and W2 satisfy the following stronger conditions:

- (i’) |W1|,|W2| ≥ 2∆cdNn,

![image 76](<2014-conlon-ordered-ramsey-numbers_images/imageFile76.png>)

- (ii’) all vertices in W1 precede all vertices in W2 or all vertices in W2 precede all vertices in W1,
- (iii’) each vertex in W1 has at most c|W2| neighbors in W2.


Suppose now that we are given an integer s ≥ 2 and the claim has been proved for all smaller values of s. By the stronger form of the case s = 1 with c′ = 2−sc, we can ﬁnd two sets W1 and W2 such that |W1|,|W2| ≥ 2sdc+1dN∆n and all the vertices in W1 have at most 2cs|W2| neighbors in W2. By applying the inductive hypothesis inside W1, we can ﬁnd sets W1,1,··· ,W1,2s−1 such that (i) for all

![image 77](<2014-conlon-ordered-ramsey-numbers_images/imageFile77.png>)

![image 78](<2014-conlon-ordered-ramsey-numbers_images/imageFile78.png>)

(s−1)d|W1|

(2(s−1)d+1∆n)s−1 ≥ (2sdc+1sdN∆n)s, (ii) for j < j′, the vertices in W1,j precede the vertices in

- j, |W1,j| ≥ c


![image 79](<2014-conlon-ordered-ramsey-numbers_images/imageFile79.png>)

![image 80](<2014-conlon-ordered-ramsey-numbers_images/imageFile80.png>)

- W1,j′, and (iii) for all j and j′, the density of edges between W1,j and W1,j′ is at most c. For each j = 1,2,... ,2s−1, let X2,j ⊂ W2 be the set of vertices which have at least c|W1,j|

neighbors in W1,j. By the degree condition on vertices in W1, we see that |X2,j| · c|W1,j| ≤ |W1,j| ·

c

![image 81](<2014-conlon-ordered-ramsey-numbers_images/imageFile81.png>)

2s|W2|, and hence |X2,j| ≤ 21s|W2|. Therefore, 2j=1s−1 |X2,j| ≤ |W22|.

![image 82](<2014-conlon-ordered-ramsey-numbers_images/imageFile82.png>)

![image 83](<2014-conlon-ordered-ramsey-numbers_images/imageFile83.png>)

Let W2′ = W2 \ 2j=1s−1 X2,j and note that |W2′| ≥ |W22|. All vertices in W2′ have at most c|W1,j| neighbors in W1,j for all j = 1,··· ,2s−1. Now apply the s − 1 case to W2′ to ﬁnd sets

![image 84](<2014-conlon-ordered-ramsey-numbers_images/imageFile84.png>)

- W2,1,··· ,W2,2s−1. We have, for all j,


c(s−1)d|W2′| (2(s−1)d+1∆n)s−1 ≥

csdN (2sd+1∆n)s

|W2,j| ≥

,

![image 85](<2014-conlon-ordered-ramsey-numbers_images/imageFile85.png>)

![image 86](<2014-conlon-ordered-ramsey-numbers_images/imageFile86.png>)

and (relabeling W1 and W2, if necessary) one can easily check that the sets W1,1,··· ,W1,2s−1, W2,1,··· ,W2,2s−1 satisfy the claimed properties.

![image 87](<2014-conlon-ordered-ramsey-numbers_images/imageFile87.png>)

![image 88](<2014-conlon-ordered-ramsey-numbers_images/imageFile88.png>)

![image 89](<2014-conlon-ordered-ramsey-numbers_images/imageFile89.png>)

![image 90](<2014-conlon-ordered-ramsey-numbers_images/imageFile90.png>)

Before moving on to the next ingredient, we note a corollary which we will need later on. Corollary 3.3. Let H be an ordered d-degenerate graph on n vertices. Suppose that a real number

- 0 < c < 12 is given and that N ≥ (n2c−7d)4 log(1/c). If an ordered graph on [N] does not contain an ordered copy of H, then there is a subset of order at least (n2c−7d)−4 log(1/c)N with edge density at most c.


![image 91](<2014-conlon-ordered-ramsey-numbers_images/imageFile91.png>)

Proof. Let s = ⌈log(2/c)⌉ ≤ 4log(1/c). Since N ≥ (n2c−7d)4 log(1/c) ≥ (2∆n(2s(2c−1))d)s,

we may apply Lemma 3.2 with c replaced by c/2. This gives t ≥ 2/c sets W1,... ,Wt satisfying |W1|,... ,|Wt| ≥ (n2c−7d)−4 log(1/c)N and such that the density of edges between Wi and Wj for all i < j is at most c/2. For 1 ≤ i ≤ t, let Wi′ be a subset of Wi of cardinality exactly N′ := ⌈(n2c−7d)−4 log(1/c)N⌉ chosen independently and uniformly at random. A ﬁrst moment calculation now shows that there is a collection of subsets W1′ ⊆ W1,... ,Wt′ ⊆ Wt such that |W1′| = ··· = |Wt′| = N′ and i<j e(Wi′,Wj′) ≤ 2c

t 2 N′2. We claim that ti=1 Wi′ satisﬁes the required condition.

![image 92](<2014-conlon-ordered-ramsey-numbers_images/imageFile92.png>)

To see this, note that the number of edges in this set is at most

c 2

![image 93](<2014-conlon-ordered-ramsey-numbers_images/imageFile93.png>)

t 2

N′2 + t

N′ 2 ≤

c 2

1 t

+

![image 94](<2014-conlon-ordered-ramsey-numbers_images/imageFile94.png>)

![image 95](<2014-conlon-ordered-ramsey-numbers_images/imageFile95.png>)

tN′ 2

.

Since t ≥ 2/c, the claim follows.

![image 96](<2014-conlon-ordered-ramsey-numbers_images/imageFile96.png>)

![image 97](<2014-conlon-ordered-ramsey-numbers_images/imageFile97.png>)

![image 98](<2014-conlon-ordered-ramsey-numbers_images/imageFile98.png>)

![image 99](<2014-conlon-ordered-ramsey-numbers_images/imageFile99.png>)

Lemma 3.2 tells us that if the edges of a graph on vertex set [N] are two-colored in red and blue and there is no red copy of a particular d-degenerate ordered graph H then it contains an ordered collection of large subsets with low red density between each pair of subsets. The next lemma shows that in this situation the blue graph, which has high density between these subsets, must contain a large trivially ordered multipartite graph.

- Lemma 3.4. Let K = Kn,n,···,n be a trivially ordered complete χ-partite graph. If a graph on vertex set [N] is such that there exist sets W1,W2,··· ,Wχ satisfying the following conditions:


- (i) for all i, |Wi| ≥ 4χn,
- (ii) for i < j, the vertices in Wi precede the vertices in Wj,
- (iii) for i < j, the density of non-edges between Wi and Wj is at most 8χ12n, then the graph contains a copy of K.


![image 100](<2014-conlon-ordered-ramsey-numbers_images/imageFile100.png>)

Proof. For each pair of distinct i,j ∈ [χ], deﬁne Wi,j ⊂ Wi as the set of vertices which have at least 4χn|Wj| non-neighbors in Wj. By property (iii), we see that

- 1


![image 101](<2014-conlon-ordered-ramsey-numbers_images/imageFile101.png>)

1

1 4χn|Wj| ≤

8χ2n|Wi||Wj|, and thus |Wi,j| ≤ 21χ|Wi|. For each i, deﬁne

|Wi,j| ·

![image 102](<2014-conlon-ordered-ramsey-numbers_images/imageFile102.png>)

![image 103](<2014-conlon-ordered-ramsey-numbers_images/imageFile103.png>)

![image 104](<2014-conlon-ordered-ramsey-numbers_images/imageFile104.png>)

Wi′ = Wi \

Wi,j ,

j =i

and note that |Wi′| ≥ |Wi| − j =i |Wi,j| ≥ 12|Wi| ≥ 2χn. For distinct i,j, each vertex in Wi′ has at most 4χn1 |Wj| ≤ 2χn1 |Wj′| non-neighbors in Wj′.

![image 105](<2014-conlon-ordered-ramsey-numbers_images/imageFile105.png>)

![image 106](<2014-conlon-ordered-ramsey-numbers_images/imageFile106.png>)

![image 107](<2014-conlon-ordered-ramsey-numbers_images/imageFile107.png>)

Let v1,v2,··· ,vχn be the vertices of K ordered as in the trivial ordering and let σ(vi) ∈ [χ] be the index of the part containing vi. We will embed the vertices of K one at a time. At the

t-th step, we map vt to a vertex wt ∈ Wσ′(v

t). Note that there are at most χn neighbors of vt in {v1,v2,··· ,vt−1}. Each such neighbor can forbid at most 2χn1 |Wσ′(v

t)| vertices from being the image of wt. Also, there are at most n − 1 vertices in Wσ′(v

![image 108](<2014-conlon-ordered-ramsey-numbers_images/imageFile108.png>)

t) already used for embedded vertices. Therefore, the number of possible images of vt in Wσ′(v

t) is at least

- 1

![image 109](<2014-conlon-ordered-ramsey-numbers_images/imageFile109.png>)

- 2χn|Wσ′(v


Wσ′(v

t) − (n − 1) − χn ·

t)| ≥

- 1

![image 110](<2014-conlon-ordered-ramsey-numbers_images/imageFile110.png>)

- 2|Wσ′(v


t)| − (n − 1) ≥ 1.

Thus, we can ﬁnd a vertex wt ∈ Wσ′(v

t) for which {w1,··· ,wt} is a copy of K[{v1,··· ,vt}]. In the end, we ﬁnd a copy of K.

![image 111](<2014-conlon-ordered-ramsey-numbers_images/imageFile111.png>)

![image 112](<2014-conlon-ordered-ramsey-numbers_images/imageFile112.png>)

![image 113](<2014-conlon-ordered-ramsey-numbers_images/imageFile113.png>)

![image 114](<2014-conlon-ordered-ramsey-numbers_images/imageFile114.png>)

By combining Lemmas 3.2 and 3.4, it is now straightforward to prove Theorem 3.1.

Proof of Theorem 3.1. Suppose that the edges of [N] have been two-colored in red and blue and the graph does not contain a red copy of H. Apply Lemma 3.2 with c = D1 , where D = 8χ2n′, and

![image 115](<2014-conlon-ordered-ramsey-numbers_images/imageFile115.png>)

- s = ⌈log χ⌉ to obtain sets W1,··· ,Wχ such that


- (i) for all i, |Wi| ≥ (2sdc+1sdN∆n)s = N

![image 116](<2014-conlon-ordered-ramsey-numbers_images/imageFile116.png>)

![image 117](<2014-conlon-ordered-ramsey-numbers_images/imageFile117.png>)

(2sd+1∆nDd)s ≥ D ≥ 4χn′,

- (ii) for i < j, the vertices in Wi precede the vertices in Wj, and
- (iii) for i < j, the density of red edges between Wi and Wj is at most D1 ≤ 8χ12n′.


![image 118](<2014-conlon-ordered-ramsey-numbers_images/imageFile118.png>)

![image 119](<2014-conlon-ordered-ramsey-numbers_images/imageFile119.png>)

We may therefore apply Lemma 3.4 to ﬁnd a blue copy of K, completing the proof of the ﬁrst part.

To prove that r<(H) ≤ n32dlogχ for any ordered d-degenerate graph on n vertices with interval chromatic number χ, we may clearly assume that n ≥ 3. Since H is contained in the trivially ordered complete χ-partite graph Kn,n,...,n, we may apply the bound from the ﬁrst part with n′ = n. Noting that s ≤ 2log χ and D ≤ 8n3 ≤ n5, we have

r<(H) ≤ 2s2d+s∆snsDds+1 ≤ 22ds2n2sD2ds

≤ χ8dlogχn4 logχn20dlogχ ≤ n32dlogχ, as required.

![image 120](<2014-conlon-ordered-ramsey-numbers_images/imageFile120.png>)

![image 121](<2014-conlon-ordered-ramsey-numbers_images/imageFile121.png>)

![image 122](<2014-conlon-ordered-ramsey-numbers_images/imageFile122.png>)

![image 123](<2014-conlon-ordered-ramsey-numbers_images/imageFile123.png>)

We conclude this section by proving Theorem 1.5. We will need the following result of Erd˝os and Szemere´di [15], which says that if a graph has low density, then it must contain a larger clique or independent set than would be guaranteed by Ramsey’s theorem alone.

- Lemma 3.5. There exists a positive constant a such that any graph on N vertices with density c ≤ 1/2 contains a clique or an independent set of order at least aclog(1logN/c).


![image 124](<2014-conlon-ordered-ramsey-numbers_images/imageFile124.png>)

Using this lemma and Corollary 3.3, it is now easy to prove the following strengthening of Theorem 1.5.

- Theorem 3.6. There exists a constant C such that if H is an ordered graph on n vertices with degeneracy d, then


r<(H,Kn) ≤ 2Cdlog2(2n/d).

Proof. Let c = d/n, a be as in Lemma 3.5 and N = max{(n2c−7d)8 log(1/c),22nclog(1/c)/a}. Note that if c ≥ 1/2, the result follows since r<(H,Kn) ≤ r(Kn,Kn) ≤ 22n ≤ 2Cdlog2(2n/d) for a large enough constant C. We may therefore assume that c < 1/2. Suppose now that the edges of the complete graph on vertex set [N] are colored with two colors, say, red and blue. If there is no red copy of H, Corollary 3.3 tells us that there is a subset of size at least (n2c−7d)−4 log(1/c)N ≥ N1/2 with density at most c in red. But then, by Lemma 3.5, the graph contains either a red or a blue clique of order at least acloglog(1N1/c/2) ≥ n. The result follows by noting that N ≤ 2Cdlog2(2n/d) for a constant C depending only on a.

![image 125](<2014-conlon-ordered-ramsey-numbers_images/imageFile125.png>)

![image 126](<2014-conlon-ordered-ramsey-numbers_images/imageFile126.png>)

![image 127](<2014-conlon-ordered-ramsey-numbers_images/imageFile127.png>)

![image 128](<2014-conlon-ordered-ramsey-numbers_images/imageFile128.png>)

![image 129](<2014-conlon-ordered-ramsey-numbers_images/imageFile129.png>)

# 4 Oﬀ the diagonal

In this section, we will prove Theorem 1.8, that there exists an ordered matching M such that r<(M,K3) ≥ n4/3−o(1). We will show that this holds when M is a jumbled matching, which we deﬁne to be an ordered matching on [n] satisfying the following two properties:

- • every pair of disjoint intervals, each of order at least 2√n, have at least one edge between them;

![image 130](<2014-conlon-ordered-ramsey-numbers_images/imageFile130.png>)

- • every pair of disjoint intervals, each of order at most 2√n, have at most 9 edges between them.


![image 131](<2014-conlon-ordered-ramsey-numbers_images/imageFile131.png>)

To construct such a matching, let n = t2 be an even positive integer. Partition [n] into t intervals I1,... ,It, each of order t. There is an ordered matching M on [n] such that each pair Ii and Ij of distinct intervals has an edge between them. Indeed, this can be easily seen by greedily picking the edges between the intervals. If A and B are disjoint intervals, each of length at least

- 2t, then there must be at least one edge between them, since each of A and B must completely


contain one of the intervals I1,... ,It. Moreover, if A and B each have length at most 2t then there are at most 9 edges between them, since each of A and B intersect at most 3 of the intervals I1,... ,It. Therefore, by considering the largest integer t such that n ≥ t2, Theorem 1.8 follows as an immediate corollary of Theorem 4.2 below. Before tackling this theorem, we recall the famous Lov´asz local lemma, which is a key tool in the proof (see, e.g., [1]).

Lemma 4.1. Let A1,... ,An be events in an arbitrary probability space. A directed graph D = (V,E) on the set of vertices V = [n] is called a dependency digraph for the events A1,... ,An if, for each i ∈ [n], the event Ai is mutually independent of all the events {Aj : (i,j) ∈/ E}. Suppose that D = (V,E) is a dependency digraph for the above events and suppose that there are real numbers x1,... ,xn such that 0 ≤ xi < 1 and P(Ai) ≤ xi (i,j)∈E(1 − xj) for all i ∈ [n]. Then P( ni=1 Ai) ≥ ni=1(1 − xi). In particular, with positive probability no event Ai holds.

![image 132](<2014-conlon-ordered-ramsey-numbers_images/imageFile132.png>)

With this lemma in hand, we are now ready to prove the main result of this section.

- Theorem 4.2. There exists a positive constant c such that if M is a jumbled matching on n vertices, then


n log n

4/3

.

r<(M,K3) ≥ c

![image 133](<2014-conlon-ordered-ramsey-numbers_images/imageFile133.png>)

Proof. For notational convenience, we will suppose that M is a jumbled matching with 800nlog n vertices and prove that n4/3 ≤ r<(M,K3) for n suﬃciently large.

Let G be a given family of ordered graphs on n2/3 vertices, each with at least 40nlog n edges, and suppose that |G| ≤ en2/3 logn. We claim that there exists an edge coloring c1 of the complete graph over the vertex set [n2/3] in two colors, red and blue, that satisﬁes the following list of properties:

- • there is no blue triangle;
- • there is no graph in G all of whose edges are colored red;
- • there is no red clique of order at least 20n1/3 log n.


We will prove this claim later. For now, we will assume that it holds and show how it implies the required result. To this end, let N = n4/3 and partition [N] into consecutive intervals V1,V2,··· ,Vn2/3, each of length n2/3. Let Φ be the set of injective embeddings of M into [N] that respect the given order of vertices of M. For φ ∈ Φ, let G(φ) be the graph over the vertex set [n2/3], where there exists an edge between i and j if and only if there is an edge of M between φ−1(Vi) and φ−1(Vj). Let

G = {G(φ) : φ ∈ Φ, e(G(φ)) ≥ 40nlog n}. Since the maps in Φ respect the order of vertices, any G(φ) can be described by the last vertex in φ−1(Vi) for each i ∈ [n2/3]. Therefore, for n suﬃciently large,

800nlog n + n2/3 n2/3 ≤ e(800n1/3 log n + 1)

n2/3

≤ en2/3 logn.

|G| ≤

By the claim above, we can ﬁnd an edge coloring c1 that satisﬁes the properties listed above with respect to the family G. Let c2 be the coloring of the complete graph on [N] where we color the edges between Vi and Vj with color c1(i,j) for i,j ∈ [n2/3]. We color all the edges within the sets Vi red. Note that this coloring contains no blue triangle, since c1 does not contain a blue triangle.

Suppose that for φ ∈ Φ, the graph φ(M) forms a red copy of M. Let Wi = V (φ(M)) ∩ Vi for each i. Let S ⊂ [n2/3] be the set of indices i for which |Wi| ≤ 2√n, and let L = [n2/3]\S. Note that for a pair of indices i,j ∈ L, since |Wi|,|Wj| > 2√n and M is a jumbled matching, there exists an edge of M between Wi and Wj. Thus, c1(i,j) is red and we can conclude that the set L forms a red clique in c1. Hence, since c1 contains no clique of order 20n1/3 log n, we see that |L| ≤ 20n1/3 log n and

![image 134](<2014-conlon-ordered-ramsey-numbers_images/imageFile134.png>)

![image 135](<2014-conlon-ordered-ramsey-numbers_images/imageFile135.png>)

Wi ≤ |L| · n2/3 ≤ 20nlog n.

i∈L

Deleting all edges of M with an endpoint in Wi for some i ∈ L, we see that there are at least 360nlog n red edges within i∈S Wi. For two indices i,j ∈ S, there are at most 9 edges of M between Wi and Wj. Hence, G(φ) has at least 40nlog n edges, implying that G(φ) ∈ G. However, G(φ) must be red in the coloring c1 and this is a contradiction. Therefore, φ(M) cannot form a red copy of M.

It remains to prove the claim. Recall that G is a given family of graphs on n2/3 vertices with at least 40nlog n edges and |G| ≤ en2/3 logn. Let H be a family of graphs on n2/3 vertices with exactly

40nlog n edges so that for each G ∈ G, there exists a graph H ∈ H satisfying G ⊇ H. We may choose H so that |H| ≤ |G|. We seek a coloring satisfying:

- • there is no blue triangle;
- • there is no graph in H all of whose edges are colored red;
- • there is no red clique of order at least 20n1/3 log n.


Consider a random coloring of the complete graph on [n2/3] obtained by coloring each edge red

with probability 1 − 2n11/3 and blue with probability 2n11/3. Let Pi be the events corresponding to blue triangles, Qi the events corresponding to copies of graphs in H being red, and Ri the events corresponding to red cliques. Let IP,IQ,IR be the index sets for the events Pi,Qi,Ri, respectively. By applying the local lemma, we will prove that there exists a coloring where none of the events Pi,Qi,Ri occur. Note that

![image 136](<2014-conlon-ordered-ramsey-numbers_images/imageFile136.png>)

![image 137](<2014-conlon-ordered-ramsey-numbers_images/imageFile137.png>)

|IP| =

n2/3 3 ≤ n2, |IQ| ≤ |H| ≤ |G| ≤ en2/3 logn, |IR| =

n2/3 20n1/3 log n ≤ e20n1/3 log2 n.

Let x = 41n, y = e−2n2/3 logn and z = e−40n1/3 log2 n. For later usage, we note that y|IQ| = o(1) and z|IR| = o(1).

![image 138](<2014-conlon-ordered-ramsey-numbers_images/imageFile138.png>)

The parameter used in the local lemma will be x for events Pi, y for events Qi, and z for events Ri. We now check the conditions of the local lemma.

Event Pi : Since Pi is an event depending on three edges, there are at most 3n2/3 other events Pj that are adjacent to Pi in the dependency graph. For the events Qj and Rj, we use the trivial bound |IQ| and |IR| for the number of events that depend on Pi. Hence, for Pi, we have

(1 − z)

(1 − y)

(1 − x)

x

j∈IR,j∼i

j∈IQ,j∼i

j∈IP,j∼i

= (1 − o(1))xe−x(3n2/3)e−y|IQ|e−z|IR|

1 4n ≥

1 8n

= (1 − o(1))

= P(Pi).

![image 139](<2014-conlon-ordered-ramsey-numbers_images/imageFile139.png>)

![image 140](<2014-conlon-ordered-ramsey-numbers_images/imageFile140.png>)

Event Qi : Since Qi is an event depending on 40nlog n edges, there are at most 40n5/3 log n events Pj that are adjacent to Qi in the dependency graph. Hence, for Qi, we have

y

(1 − x)

(1 − y)

(1 − z)

j∈IP,j∼i

j∈IQ,j∼i

j∈IR,j∼i

= (1 − o(1))ye−x(40n5/3 logn)e−y|IQ|e−z|IR|

= (1 − o(1))e−2n2/3 logne−10n2/3 logn ≥ e−20n2/3 logn ≥ 1 −

40n log n

- 1

![image 141](<2014-conlon-ordered-ramsey-numbers_images/imageFile141.png>)

- 2n1/3


= P(Qi).

Event Ri : Since Ri is an event depending on 20n1/23 logn ≤ 200n2/3 log2 n edges, there are at most 200n4/3 log2 n events Pj that are adjacent to Ri in the dependency graph. Hence, for Ri, we have

z

(1 − x)

(1 − y)

(1 − z)

j∈IP,j∼i

j∈IQ,j∼i

j∈IR,j∼i

= (1 − o(1))ze−x(200n4/3 log2 n)e−y|IQ|e−z|IR|

= (1 − o(1))e−40n1/3 log2 ne−50n1/3 log2 n

(20n1/23 logn)

- 1

![image 142](<2014-conlon-ordered-ramsey-numbers_images/imageFile142.png>)

- 2n1/3


≥ e−95n1/3 log2 n ≥ 1 −

= P(Ri).

The result follows.

![image 143](<2014-conlon-ordered-ramsey-numbers_images/imageFile143.png>)

![image 144](<2014-conlon-ordered-ramsey-numbers_images/imageFile144.png>)

![image 145](<2014-conlon-ordered-ramsey-numbers_images/imageFile145.png>)

![image 146](<2014-conlon-ordered-ramsey-numbers_images/imageFile146.png>)

While we suspect that r<(M,K3) ≤ n2−ǫ for some ǫ > 0, we have been unable to improve on the trivial bound r<(M,K3) ≤ r(Kn,K3) = O(n2/log n).

# 5 Odds and ends

## 5.1 Connection to hypergraphs

Given a 3-uniform hypergraph H, we deﬁne the Ramsey number r(H) to be the smallest natural number N such that every two-coloring of the edges of the complete 3-uniform hypergraph KN(3) contains a monochromatic copy of H. In this subsection, we will show that for any 3-uniform hypergraph H, there is a family of ordered graphs SH such that the Ramsey number of H is bounded in terms of the ordered Ramsey number of the family SH, where the ordered Ramsey number r<(F) for a family of ordered graphs F is deﬁned to be the smallest N such that every two-coloring of the edges of {1,2,... ,N} contains an ordered copy of some F ∈ F.

For any ordered graph H on {1,2,... ,n}, we deﬁne a 3-uniform hypergraph T (H) on vertex set {1,2,... ,n+1} by taking all triples whose ﬁrst pair is an edge of H. Given a 3-uniform hypergraph H on n+1 vertices, we let SH be the collection of ordered graphs H on {1,2,... ,n} such that H is a subhypergraph of T (H). For example, if H = Kn(3)+1 then SH = {Kn} and if H = K4(3) \e then SH contains three diﬀerent graphs on vertex set {1,2,3}, namely, the complete graph K3 and the two graphs with two edges containing the edge {1,2}. Note that for any graph H, we have H ∈ ST (H). Our main theorem relating upper bounds for Ramsey numbers of 3-uniform hypergraphs to ordered Ramsey numbers is now as follows.

- Theorem 5.1. Let H be a 3-uniform hypergraph. Then r(H) ≤ 2(r<(2SH)) + 1.


Proof. The result follows from the method of Erd˝os and Rado. Suppose that N = 2(r<(SH)

2 ) + 1 and the edges of the complete 3-uniform hypergraph on {1,2,... ,N} have been two-colored, say by red and blue. We will ﬁnd an increasing sequence of vertices v1,v2,... ,vt+1 with t = r<(SH)

such that, for any given i and j with i < j, all triples of the form {vi,vj,vk} with k > j have the same color χ(i,j). Consider the two-coloring of the edges of the complete graph on v1,v2,... ,vt where the edge {vi,vj} receives color χ(i,j). Then, since t = r<(SH), this graph must contain a monochromatic copy of some ordered graph in SH. By construction, the 3-uniform hypergraph on v1,v2,... ,vt+1 must then contain a monochromatic copy of H in the same color. It only remains to ﬁnd the sequence v1,v2,... ,vt+1.

We will prove, by induction, that for any 1 ≤ ℓ ≤ t, there is a sequence of vertices v1,v2,... ,vℓ and a set Vℓ with

|Vℓ| ≥ 2(r<(2SH))−(2ℓ)

such that, for any 1 ≤ i < j ≤ ℓ, all triples {vi,vj,w} with w ∈ {vj+1,... ,vℓ} ∪ Vℓ have the same color χ(i,j) depending only on i and j.

To begin, we let v1 = 1 and V1 = {2,3,... ,N}. Suppose now that v1,v2,... ,vℓ and Vℓ have been constructed satisfying the required conditions and we wish to ﬁnd vℓ+1 and Vℓ+1. We let vℓ+1 be the smallest element of Vℓ. Let Vℓ,0 = Vℓ \ {vℓ+1}. We will construct a sequence of subsets Vℓ,0 ⊃ Vℓ,1 ⊃ ··· ⊃ Vℓ,ℓ such that, for each j, all triples {vj,vℓ+1,w} with w ∈ Vℓ,j are of the same color that depends only on the index j. Note that since Vℓ,ℓ ⊂ ··· ⊂ Vℓ,0 ⊂ Vℓ it follows that all triples {vi,vj,w} with 1 ≤ i < j ≤ ℓ + 1 and w ∈ Vℓ,ℓ have the same color depending only on the values of i and j.

Suppose now that Vℓ,j has been constructed in an appropriate fashion. To construct Vℓ,j+1, we consider the set of vertices w ∈ Vℓ,j for which {vj+1,vℓ+1,w} have color red. If this set has size at least |Vℓ,j|/2, we let Vℓ,j+1 be this set. Otherwise, we let Vℓ,j+1 be the complement of this set in Vℓ,j. In either case, |Vℓ,j+1| ≥ |Vℓ,j|/2. To ﬁnish the construction of Vℓ+1, we let Vℓ+1 = Vℓ,ℓ. Note that for each j ≤ ℓ and every w ∈ Vℓ+1 the triple {vj,vℓ+1,w} has the same color. Furthermore,

|Vℓ| − 1

2ℓ ≥ 2(r<(2SH))−(ℓ+12 ). In particular, |Vt| ≥ 1 and choosing vt+1 ∈ Vt completes the proof.

|Vℓ+1| ≥

![image 147](<2014-conlon-ordered-ramsey-numbers_images/imageFile147.png>)

![image 148](<2014-conlon-ordered-ramsey-numbers_images/imageFile148.png>)

![image 149](<2014-conlon-ordered-ramsey-numbers_images/imageFile149.png>)

![image 150](<2014-conlon-ordered-ramsey-numbers_images/imageFile150.png>)

![image 151](<2014-conlon-ordered-ramsey-numbers_images/imageFile151.png>)

We expect that the bound coming from this theorem is close to sharp in many cases. For example, for H = Kn(3)+1, the complete 3-uniform hypergraph, we have SH = {Kn}, so Theorem 5.1 returns the usual double-exponential bound, which is believed to be tight. However, there are cases where the bound given above is far from the truth. This can be seen by considering the balanced complete tripartite 3-uniform hypergraph H = Kn,n,n(3) . It has Ramsey number 2Θ(n2) but the best bound the theorem above can give is of the form 22O(n) since all ordered graphs in SH contain the complete bipartite graph Kn,n as a subgraph, thus implying that r<(SH) ≥ r(Kn,n) = 2Ω(n).

Another interesting example to consider is the hypergraph T (H) deﬁned earlier. Since H ∈ ST (H), Theorem 5.1 has the following corollary. Corollary 5.2. For any ordered graph H,

r(T (H)) ≤ 2(r<2(H)) + 1.

This implies, for example, that if M is an ordered matching on {1,2,... ,n}, then the Ramsey number of the hypergraph T (M) is at most 2n4logn. For random matchings, we expect that this unusual looking bound is not far from the truth. We hope to discuss this direction further in future work.

## 5.2 Linear ordered Ramsey numbers

In this subsection, we characterize those graphs for which the ordered Ramsey number is linear in every ordering. A vertex cover V of a graph G is a set of vertices such that every edge of G has an endpoint in V . The cover number τ(G) of a graph G is the minimum size of a vertex cover of G. It is easy to show that the cover number of a graph is within a factor two of the size of the largest matching in the graph. We will prove the following theorem.

- Theorem 5.3. A graph G on n vertices has ordered Ramsey number O(n) in every ordering if and only if τ(G) = O(1).

We ﬁrst show that if an ordered graph has cover number O(1), then its ordered Ramsey number is linear in the number of vertices.

- Theorem 5.4. For every positive integer τ, there exists a constant c(τ) such that every ordered graph G on n vertices with a vertex cover of size τ satisﬁes


r<(G) ≤ c(τ)n.

Proof. By Ramsey’s theorem and a standard averaging argument, there is an integer A and a > 0 such that, for N ≥ A, every two-coloring of the edges of the complete graph on [N] contains at least aN2τ+1 monochromatic copies of K2τ+1. Suppose now that we are given an ordered graph G on n vertices with a vertex cover of size τ. Let N = max{A, a2n} and note that every two-coloring of the edges of [N] contains at least aN2τ+1 monochromatic copies of K2τ+1. There exists a collection of vertices v2,v4,... ,v2τ such that at least aNτ+1 copies of K2τ+1 have their 2nd, 4th,... ,(2τ)-th vertex as v2,v4,... ,v2τ, in order. Without loss of generality, we may assume that at least half of these copies are red. We let K be this collection of red copies of K2τ+1, noting that |K| ≥ a2Nτ+1. We also let v0 = 0 and v2τ+2 = N + 1.

![image 152](<2014-conlon-ordered-ramsey-numbers_images/imageFile152.png>)

![image 153](<2014-conlon-ordered-ramsey-numbers_images/imageFile153.png>)

We now show that we can ﬁnd in this coloring a red copy of every ordered graph G on n vertices

which has a vertex cover of size τ. It follows that r<(G) ≤ N so that we may take c(τ) = max(A, a2). For i = 0,... ,τ, let Xi be the set of vertices v between v2i and v2i+2 such that there exists a K ∈ K which has v as its (2i + 1)-th vertex. We see that

![image 154](<2014-conlon-ordered-ramsey-numbers_images/imageFile154.png>)

|K| ≤ |X0| · |X1| · ··· · |Xτ|.

Since |Xi| ≤ N for all i and |K| ≥ a2Nτ+1, we see that |Xi| ≥ a2N ≥ n for all i. Note that the vertices in Xi are incident to all vertices in v2,v4,... ,v2τ by a red edge. Since |Xi| ≥ n for all i, we can ﬁnd a red copy of G. Indeed, we can use the vertices v2,v4,... ,v2τ as the τ vertices of the vertex cover and use common neighbors to embed the remaining vertices in the red copy of G.

![image 155](<2014-conlon-ordered-ramsey-numbers_images/imageFile155.png>)

![image 156](<2014-conlon-ordered-ramsey-numbers_images/imageFile156.png>)

![image 157](<2014-conlon-ordered-ramsey-numbers_images/imageFile157.png>)

![image 158](<2014-conlon-ordered-ramsey-numbers_images/imageFile158.png>)

![image 159](<2014-conlon-ordered-ramsey-numbers_images/imageFile159.png>)

![image 160](<2014-conlon-ordered-ramsey-numbers_images/imageFile160.png>)

Ordered Ramsey numbers are monotone. That is, if H is an ordered subgraph of G, then r<(G) ≥ r<(H). The next theorem improves upon this simple fact if H is a small subgraph of G. We will abuse notation slightly in the statement and proof by using G and H to refer to both the unordered graphs and particular ordered versions of these graphs.

- Theorem 5.5. Let G be a graph on n vertices and H a subgraph on t vertices. Then, for every ordering of H, there is an ordering of G such that r<(G) ≥ ⌊nt ⌋(r<(H) − 1).


![image 161](<2014-conlon-ordered-ramsey-numbers_images/imageFile161.png>)

Proof. Let s = ⌊nt ⌋. Given an ordering of H with vertex set [t], we consider any ordering of G where vertex i of H is in place 1 + (i − 1)s. This is chosen so that H keeps its ordering within G

![image 162](<2014-conlon-ordered-ramsey-numbers_images/imageFile162.png>)

and any interval of s vertices has at most one vertex from H.

Let r = r<(H) − 1. By the deﬁnition of the ordered Ramsey number, there is an edge coloring c of the complete ordered graph on vertex set [r] containing no monochromatic copy of H with the given ordering. We will construct a coloring of the complete ordered graph on N = sr vertices with no monochromatic copy of G with the ordering above. Partition the complete ordered graph on vertex set [N] into r intervals each with s vertices. We color every edge between the ith interval and the jth interval with color c(i,j) and color the edges inside each interval arbitrarily.

We claim that this edge coloring of [N] has no monochromatic copy of G with the ordering deﬁned above. Indeed, if there were such a copy of G, the vertices of the ordered subgraph H would have to be in distinct intervals. This is because the ordering of G was chosen so that no two vertices of H are contained in an interval of s vertices. However, if the vertices of the monochromatic ordered copy of H are in distinct intervals, then we would also get an ordered monochromatic copy of H in the edge coloring c of [r]. This contradicts the deﬁnition of c and completes the proof.

![image 163](<2014-conlon-ordered-ramsey-numbers_images/imageFile163.png>)

![image 164](<2014-conlon-ordered-ramsey-numbers_images/imageFile164.png>)

![image 165](<2014-conlon-ordered-ramsey-numbers_images/imageFile165.png>)

![image 166](<2014-conlon-ordered-ramsey-numbers_images/imageFile166.png>)

We will now use this result to show that if a graph on n vertices has large cover number, then there is an ordering for which the ordered Ramsey number is large. Corollary 5.6. There is a positive constant c such that every graph G with n vertices and cover number τ has an ordering with ordered Ramsey number at least τclogτ/log logτn.

Proof. Since G has cover number τ, it contains a matching with t ≥ τ vertices. Consider the induced subgraph H of G on these t vertices. By Theorem 1.1, there is an ordering of H with Ramsey number at least tclogt/log logt. By Theorem 5.5, there is an ordering of G with Ramsey number at least ⌊nt ⌋(tclogt/log logt−1). By making c a little smaller, we obtain the desired result.

![image 167](<2014-conlon-ordered-ramsey-numbers_images/imageFile167.png>)

![image 168](<2014-conlon-ordered-ramsey-numbers_images/imageFile168.png>)

![image 169](<2014-conlon-ordered-ramsey-numbers_images/imageFile169.png>)

![image 170](<2014-conlon-ordered-ramsey-numbers_images/imageFile170.png>)

![image 171](<2014-conlon-ordered-ramsey-numbers_images/imageFile171.png>)

If G has n vertices and cover number τ(G) = ω(1), Corollary 5.6 implies that there is an ordering of G with ordered Ramsey number ω(n). Hence, Theorem 5.3 follows immediately from Theorem 5.4 and Corollary 5.6.

In fact, as a random ordering of the vertices of a graph will likely space out most of the vertices of a given matching and a random matching almost surely has superlinear ordered Ramsey number, a minor modiﬁcation of the proof above gives the following stronger statement. It shows that if the cover number of a graph is ω(1), then almost all orderings will have superlinear ordered Ramsey number. We leave the details to the interested reader.

- Proposition 5.7. There is a positive constant c such that if G is a graph with n vertices and cover number τ, then almost every ordering of G has ordered Ramsey number at least τclogτ/log logτn.


## 5.3 Density conditions for ordered matchings

For many of the bounds in this paper, we prove stronger oﬀ-diagonal results. For example, when bounding the ordered Ramsey number of an ordered d-degenerate graph H on n vertices, we actually estimate r<(H,Kn). When bounding this quantity, we ﬁrst try to embed H greedily. If this fails, we show that there must be a large subset where the density of edges is at least 1 − n1, so that we can easily embed copies of Kn. However, this seems incredibly wasteful for bounding r<(H), given that unordered copies of H already appear at density roughly 1 − d1. Somewhat surprisingly, this intuition is wrong. Indeed, we will now show the existence of a positive constant c for which there is an ordered matching M on n vertices with interval chromatic number 2 and an ordered graph G on N = 2nc vertices with edge density at least 1 − n−c which does not contain M as an ordered subgraph. Note that for any ﬁxed ordered graph H with interval chromatic number 2, the ordered extremal number ex<(N,H), deﬁned in the introduction, is O(N2−ǫ). However, even for a typical ordered matching, this result shows that this subquadratic behavior is only exhibited for rather large values of N.

![image 172](<2014-conlon-ordered-ramsey-numbers_images/imageFile172.png>)

![image 173](<2014-conlon-ordered-ramsey-numbers_images/imageFile173.png>)

Let H be an ordered graph with interval chromatic number 2 and k+ℓ vertices with every edge going between [k] and [k + 1,k + ℓ]. Let B be an ordered graph with interval chromatic number 2 and N + M vertices with every edge going between [N] and [N + 1,N + M]. We say that H is an interval minor of B if there are partitions [N] = I1 ∪···∪Ik and [N +1,N +M] = Ik+1 ∪···∪Ik+ℓ into intervals with the vertices in Ii coming before the vertices in Ij for i < j such that if (i,j) is an edge of H, then there is at least one edge in B between Ii and Ij.

- Proposition 5.8. There is an ordered matching M on 2n vertices with interval chromatic number 2 and an ordered graph G on 2Ω(n1/12) vertices with edge density 1−O(n−1/6) which does not contain M as an ordered subgraph.


Proof. Let M be an ordered matching on 2n vertices with interval chromatic number 2, where each part is partitioned into n1/2 intervals of size n1/2, with an edge between each interval in the ﬁrst part and each interval in the second part. Such a matching can be constructed greedily.

Let k = 21n1/3 − 2. In the paper [17], the second author constructed an ordered bipartite graph B with parts of size t = 2Ω(k1/4) and density 1 − O(k−1/2) across the two parts which does not contain Jk as an interval minor, where Jk is the ordered graph of interval chromatic number 2 on k + k vertices whose edge set consists of all k2 pairs (i,j) with 1 ≤ i ≤ k < j ≤ 2k. We now construct a graph G on N = 2n1/6t = 2Ω(n1/12) vertices. Partition the vertex set into 2n1/6 consecutive intervals I1,... ,I2n1/6 of t vertices each and place a copy of B between each pair of intervals, while each of the 2n1/6 intervals forms an independent set. The resulting graph G has density at least 1 − 1/(2n1/6) − O(k−1/2) = 1 − O(n−1/6).

![image 174](<2014-conlon-ordered-ramsey-numbers_images/imageFile174.png>)

If G contains M as an ordered subgraph, then, by the pigeonhole principle, there is an interval Ii containing at least n/(2n1/6) = n5/6/2 vertices from the ﬁrst part of M. Recall that the ﬁrst part of the matching M was partitioned into n1/2 intervals of size n1/2. Hence, Ii will contain at least

- 1

![image 175](<2014-conlon-ordered-ramsey-numbers_images/imageFile175.png>)

- 2n5/6/n1/2 −2 = k such intervals. Similarly, there is an interval Ij containing at least k intervals of the second part of M. Therefore, the subgraph induced on Ii ∪Ij contains Jk as an interval minor. However, this contradicts our choice of B, completing the proof.


![image 176](<2014-conlon-ordered-ramsey-numbers_images/imageFile176.png>)

![image 177](<2014-conlon-ordered-ramsey-numbers_images/imageFile177.png>)

![image 178](<2014-conlon-ordered-ramsey-numbers_images/imageFile178.png>)

![image 179](<2014-conlon-ordered-ramsey-numbers_images/imageFile179.png>)

## 5.4 Induced ordered Ramsey numbers

A graph H is said to be an induced subgraph of a graph G if V (H) ⊂ V (G) and two vertices of H are adjacent if and only if they are adjacent in G. The induced Ramsey number r∗(H) is deﬁned to be the minimum N for which there is a graph G such that every two-coloring of the edges of G contains a monochromatic induced copy of H.

That these numbers exist was proved by several groups of authors in the early seventies, though the original methods did not give good bounds for r∗(H). The ﬁrst major breakthrough on quantitative estimates was due to Kohayakawa, Pr¨omel and Ro¨dl [25], who proved that there exists a constant c such that if H is a graph on n vertices, then r∗(H) ≤ 2cnlog2 n (see also [19]). This result was recently improved in [11] to r∗(H) ≤ 2cnlogn, edging closer to resolving the well-known conjecture of Erd˝os that r∗(H) ≤ 2cn.

It is also possible to deﬁne an ordered version of the induced Ramsey number, which we denote

by r<∗ (H). This is the smallest N for which there is an ordered graph G such that every twocoloring of the edges of G contains a monochromatic ordered induced copy of H. A straightforward

modiﬁcation of the proof of Theorem 1.2 in [11] allows one to prove a bound for r<∗ (H) which brings it in line with the bounds mentioned above. We omit the details.

- Theorem 5.9. There exists a constant c such that for any ordered graph H on n vertices,

r<∗ (H) ≤ 2cnlogn.

Moreover, by modifying the proof of Theorem 1.4 from [19], we may prove the following induced variant of Theorem 1.3. We again omit the details.

- Theorem 5.10. There exists a constant c such that for any ordered graph H on n vertices with degeneracy d and interval chromatic number χ,


r<∗ (H) ≤ ncdlogχ.

# 6 Open problems

Many diﬃcult and interesting problems arose in our study of ordered Ramsey numbers. In this section, we would like to draw attention to a few of them.

Our ﬁrst problem relates to the oﬀ-diagonal ordered Ramsey number r<(M,K3). We have already mentioned the trivial upper bound r<(M,K3) ≤ r(Kn,K3) = O(n2/log n) for any matching M on n vertices, while Theorem 1.8 shows that there are matchings M on n vertices such that r<(M,K3) = Ω((n/log n)4/3). We are not sure where the truth should lie, though we expect that the upper bound is far from optimal.

- Problem 6.1. Does there exist an ǫ > 0 such that any ordered matching M on n vertices satisﬁes r<(M,K3) = O(n2−ǫ)?


In Theorem 1.1, we proved that there are matchings M with n vertices for which r<(M) ≥ nclogn/log logn, while Theorem 1.2 showed that this result is not far from the truth, in that r<(M) ≤ n⌈logn⌉ for every ordered matching M on n vertices. It would be very interesting to close the gap between these two bounds.

- Problem 6.2. Close the gap between the upper and lower bounds for ordered Ramsey numbers of matchings.

One of our most elementary observations (see Theorem 2.1) was that if M is a matching on n vertices with interval chromatic number 2, then r<(M) ≤ n2. On the other hand, Theorem 1.4 shows that there are matchings M with n vertices and interval chromatic number 2 for which r<(M) = Ω(n2/log2 nlog log n). It would again be interesting to close the gap between these two bounds.

- Problem 6.3. Close the gap between the upper and lower bounds for ordered Ramsey numbers of matchings with interval chromatic number 2.

The d-dimensional cube is the graph on vertex set {0,1}d where two vertices are connected by an edge if and only if they diﬀer in exactly one coordinate. This is a d-regular bipartite graph with 2d vertices. It is a well-known open problem to determine whether the Ramsey number of the cube is linear in the number of vertices, that is, whether r(Qd) = O(2d). The best known upper bound [12, 28] is quadratic in the number of vertices.

For any ordering of the cube, Theorem 3.1 easily implies that r<(Qd) ≤ 2cd3, while, for a random ordering, Theorem 2.3 and the fact that Qd contains a matching of size 2d−1 easily imply that r<(Qd) ≥ 2c′d2/logd. We believe that the lower bound is closer to the truth.

- Problem 6.4. Improve the upper bound for the ordered Ramsey number of the cube. For orderings of the cube with interval chromatic number 2, Theorem 3.1 again implies that

r<(Qd) ≤ 2cd2, while Theorem 1.4 implies that there exist orderings such that r<(Qd) ≥ c′d22log2d d. Again, it seems more likely that the lower bound is closer to the truth.

![image 180](<2014-conlon-ordered-ramsey-numbers_images/imageFile180.png>)

- Problem 6.5. Improve the upper bound for the ordered Ramsey number of cubes with interval chromatic number 2.

Using a result of Fu¨redi and Hajnal [22], Balko, Cibulka, Kra´l and Kyncˇl [4] noted that there are orderings of the path on n vertices for which the ordered Ramsey number is linear in n. It would also be interesting to decide whether a similar phenomenon holds for other graphs, that is, whether there are orderings where the ordered Ramsey number is close to the usual Ramsey number. In particular, it would be interesting to decide whether there are orderings of the cube for which the ordered Ramsey number is as small as the usual Ramsey number.

- Problem 6.6. Is there an ordering of the cube such that r<(Qd) ≤ 2cd for some absolute constant c?


We have characterized those graphs such that for every ordering of a graph H, the ordered Ramsey number is linear in |H|. These are precisely the graphs H for which the edges of H can be covered by O(1) vertices. A problem of a similar nature is to determine which graphs have some ordering for which the ordered Ramsey number is linear. In particular, since the Ramsey number for graphs of bounded maximum degree is linear in the number of vertices, it is natural to ask whether there are always orderings of d-regular graphs for which the ordered Ramsey number is linear. We think this unlikely for random regular graphs.

- Problem 6.7. Do random 3-regular graphs have superlinear ordered Ramsey numbers for all orderings?

We note that if the answer to this question is positive, as expected, it would also show that there are graphs for which the ordered Ramsey number is always signiﬁcantly larger than the Ramsey number, regardless of the ordering.

We only have a rather poor understanding of ordered Ramsey numbers for more than two colors. For example, we could only prove the bound r<(M;q) ≤ n(2 logn)q−1 for any matching M on n vertices. We believe that something much stronger should hold.

- Problem 6.8. Show that for any natural number q ≥ 3 there exists a constant cq such that r<(M;q) ≤ ncq logn for any matching M on n vertices.

Finally, we recall Theorem 2.6, which says that for any natural number k and any ordered matching M on n vertices with bandwidth at most k, the ordered Ramsey number r<(M) satisﬁes r<(M) ≤ n⌈logk⌉+2. It would be very interesting to know whether this theorem can be extended to graphs other than matchings. That is, we have the following problem.

- Problem 6.9. Show that for any natural number k there exists a constant ck such that r<(H) ≤ nck for any ordered graph H on n vertices with bandwidth at most k.


Note added. Before the ﬁnal version of this article went to print, a solution to Problem 6.9 was found by Balko, Cibulka, Kra´l and Kyncˇl and added to their paper [4]. Their result follows from an iterated application of Theorem 5.4. To see this, consider the ordered graph Ht,k on 2t+k vertices consisting of three successive intervals L,M and R, with |L| = |R| = t and |M| = k, where M is a copy of the complete graph Kk and every vertex in L and R is connected to every vertex in M. Since k is ﬁxed, Theorem 5.4 implies that every two-coloring of the edges of the complete graph on {1,2,... ,n} contains a monochromatic copy of Ht,k with t ≥ cn, where c > 0 depends only on k. Letting L′ and R′ be the intervals corresponding to L and R in this copy of Ht,k, we see that we may again apply Theorem 5.4 to ﬁnd a monochromatic copy of Ht′,k in each of L′ and R′, where

- t′ ≥ ct. Iterating this procedure Ωk(log n) times, it is possible to ﬁnd a monochromatic subgraph which contains all graphs with nǫk vertices and bandwidth at most k. We omit the details, referring the interested reader instead to [4].


Acknowledgements. We would like to thank the anonymous referees for a number of helpful remarks.

# References

- [1] N. Alon and J. H. Spencer, The probabilistic method, 3rd ed., John Wiley & Sons, Hoboken, NJ, 2008.
- [2] N. Alon, M. Krivelevich and B. Sudakov, Tura´n numbers of bipartite graphs and related Ramsey-type questions, Combin. Prob. Comput. 12 (2003), 477–494.


- [3] M. Ajtai, J. Komlo´s and E. Szemere´di, A note on Ramsey numbers, J. Combin. Theory Ser. A 29 (1980), 354–360.
- [4] M. Balko, J. Cibulka, K. Kra´l and J. Kyncˇl, Ramsey numbers of ordered graphs, arXiv preprint, arXiv:1310.7208 [math.CO].
- [5] T. Bohman and P. Keevash, Dynamic concentration of the triangle-free process, arXiv preprint, arXiv:1302.5963 [math.CO].
- [6] S. A. Burr and P. Erd˝os, On the magnitude of generalized Ramsey numbers for graphs, in Inﬁnite and Finite Sets, Vol. 1, (Keszthely, 1973), Colloq. Math. Soc. Ja´nos Bolyai, Vol. 10, 214–240, North-Holland, Amsterdam, 1975.
- [7] V. Chv´atal, V. Ro¨dl, E. Szemere´di and W. T. Trotter, The Ramsey number of a graph with bounded maximum degree, J. Combin. Theory Ser. B 34 (1983), 239–243.
- [8] J. Cibulka, P. Gao, M. Krcˇ´l, T. Valla and P. Valtr, On the geometric Ramsey number of outerplanar graphs, Discrete Comput. Geom. 53 (2015), 64–79.
- [9] D. Conlon, A new upper bound for diagonal Ramsey numbers, Ann. of Math. 170 (2009), 941–960.
- [10] D. Conlon, The Ramsey number of dense graphs, Bull. London Math. Soc. 45 (2013), 483–496.
- [11] D. Conlon, J. Fox and B. Sudakov, On two problems in graph Ramsey theory, Combinatorica 32 (2012), 513–535.
- [12] D. Conlon, J. Fox and B. Sudakov, Short proofs of some extremal results II, to appear in J. Combin. Theory Ser. B.
- [13] P. Erd˝os, Some remarks on the theory of graphs, Bull. Amer. Math. Soc. 53 (1947), 292–294.
- [14] P. Erd˝os and G. Szekeres, A combinatorial problem in geometry, Compos. Math. 2 (1935), 463–470.
- [15] P. Erd˝os and E. Szemere´di, On a Ramsey type theorem, Period. Math. Hungar. 2 (1972), 295–299.
- [16] G. Fiz Pontiveros, S. Griﬃths and R. Morris, The triangle-free process and R(3,k), arXiv preprint, arXiv:1302.6279 [math.CO].
- [17] J. Fox, Stanley–Wilf limits are typically exponential, to appear in Adv. Math.
- [18] J. Fox, J. Pach, B. Sudakov and A. Suk, Erd˝os–Szekeres-type theorems for monotone paths and convex bodies, Proc. London Math. Soc. 105 (2012), 953–982.
- [19] J. Fox and B. Sudakov, Induced Ramsey-type theorems, Adv. Math. 219 (2008), 1771–1800.
- [20] J. Fox and B. Sudakov, Two remarks on the Burr–Erdo˝s conjecture, European J. Combin. 30


(2009), 1630–1645.

- [21] J. Fox and B. Sudakov, Density theorems for bipartite graphs and related Ramsey-type results, Combinatorica 29 (2009), 153–196.
- [22] Z. Fu¨redi and P. Hajnal, Davenport–Schinzel theory of matrices, Discrete Math. 103 (1992), 233–251.
- [23] R. L. Graham, V. Ro¨dl and A. Rucin´ski, On graphs with linear Ramsey numbers, J. Graph Theory 35 (2000), 176–192.
- [24] J. H. Kim, The Ramsey Number R(3,t) has order of magnitude t2/log t, Random Structures Algorithms 7 (1995), 173–207.
- [25] Y. Kohayakawa, H. Pr¨omel and V. Ro¨dl, Induced Ramsey numbers, Combinatorica 18 (1998), 373–404.
- [26] A. Kostochka and V. Ro¨dl, On graphs with small Ramsey numbers II, Combinatorica 24

(2004), 389–401.

- [27] A. Kostochka and B. Sudakov, On Ramsey numbers of sparse graphs, Combin. Probab. Comput. 12 (2003), 627–641.
- [28] C. Lee, Ramsey numbers of degenerate graphs, arXiv:1505.04773 [math.CO].
- [29] J. Matousˇek, Geometric discrepancy: an illustrated guide, Algorithms and Combinatorics 18, Springer-Verlag, Berlin, 1999.
- [30] K. Milans, D. Stolee and D. B. West, Ordered Ramsey theory and track representations of graphs, J. Comb. 6 (2015), 445–456.
- [31] G. Moshkovitz and A. Shapira, Ramsey theory, integer partitions and a new proof of the Erd˝os–Szekeres theorem, Adv. Math. 262 (2014), 1107–1129.
- [32] J. Pach and G. Tardos, Forbidden paths and cycles in ordered graphs and matrices, Israel J. Math. 155 (2006), 359–380.
- [33] J. Pach and G. To´th, Erd˝os–Szekeres-type theorems for segments and noncrossing convex sets, Geom. Dedicata 81 (2000), 1–12.
- [34] F. P. Ramsey, On a problem of formal logic, Proc. London Math. Soc. 30 (1930), 264–286.
- [35] J. H. Spencer, Ramsey’s theorem – a new lower bound, J. Combin. Theory Ser. A 18 (1975), 108–115.


