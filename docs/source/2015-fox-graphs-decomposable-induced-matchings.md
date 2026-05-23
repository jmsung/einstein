---
type: source
kind: paper
title: On graphs decomposable into induced matchings of linear sizes
authors: Jacob Fox, Hao Huang, Benny Sudakov
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1512.07852v1
source_local: ../raw/2015-fox-graphs-decomposable-induced-matchings.pdf
topic: general-knowledge
cites:
---

arXiv:1512.07852v1[math.CO]24Dec2015

On graphs decomposable into induced matchings of linear sizes

Jacob Fox ∗ Hao Huang † Benny Sudakov ‡

Abstract

We call a graph G an (r,t)-Ruzsa-Szemer´edi graph if its edge set can be partitioned into t edge-disjoint induced matchings, each of size r. These graphs were introduced in 1978 and has been extensively studied since then. In this paper, we consider the case when r = cn. For c > 1/4, we determine the maximum possible t which is a constant depending only on c. On the other hand, when c = 1/4, there could be as many as Ω(log n) induced matchings. We prove that this bound is tight up to a constant factor. Finally, when c is ﬁxed strictly between 1/5 and 1/4, we give a short proof that the number t of induced matchings is O(n/ log n). We are also able to further improve the upper bound to o(n/ log n) for ﬁxed c > 1/4 − b for some positive constant b.

# 1 Introduction

We call a graph G = (V,E) an (r,t)-Ruzsa-Szemer´edi graph, or (r,t)-RS graph for short, if its edge set E(G) can be partitioned into t pairwise edge-disjoint induced matchings M1,··· ,Mt, each consists of r edges. These graphs were ﬁrst introduced in the famous paper by Ruzsa and Szemer´edi [20], in which they show that there is no n-vertex (r,t)-RS graph for r,t both linear in n. They also proved that this result implies the celebrated theorem of Roth [19], that a subset S of [n] = {1,··· ,n} without nontrivial 3-term arithmetic progressions has size at most

- o(n). Ruzsa and Szemer´edi also constructed (n/eO(

√logn),n/3)-RS graphs on n vertices, based

![image 1](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile1.png>)

- on a result of Behrend [6] that there is a surprisingly large subset of [n] without non-trivial 3-term arithmetic progressions. They used these graphs together with the regularity lemma of Szemer´edi [22] to solve an extremal problem of Brown, Erdo˝s, and So´s [9, 10], showing that the maximum number of edges in a 3-uniform n-vertex hypergraph in which no 6 vertices span at least 3 edges is at least n2−o(1) and at most o(n2) for suﬃciently large n. In this paper we consider the following natural question. Problem 1.1. For which values of r and t does there exist an (r,t)-RS graph on n vertices?


This question has been studied in depth for decades, and has found several applications in combinatorics, complexity theory and information theory (see e.g. [1, 3, 4, 5, 15, 12]). One line of research was to ﬁnd very dense RS-graphs decomposable into large induced matchings. An early result of this type by Frankl and F¨uredi [14] implies that for any ﬁxed r there are (r,t)-RS graphs on n vertices with rt = (1 − o(1)) n2 edges. However the techniques employed in their

![image 2](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile2.png>)

∗Department of Mathematics, Stanford University, CA 94305-2125. Email: jacobfox@stanford.edu. Research

supported by a Packard Fellowship, by NSF Career Award DMS-135212, and by an Alfred P. Sloan Fellowship. †Department of Math and CS, Emory University, Atlanta, GA 30322. Email: hao.huang@emory.edu. ‡Department of Mathematics, ETH, 8092 Zurich, Switzerland. Email: benjamin.sudakov@math.ethz.ch. Research

supported in part by SNSF grant 200021-149111.

proof cannot provide induced matchings of size larger than Θ(log n). Later Birk, Linial and Meshulam [7] noticed that such very dense (r,t)-RS graphs with r → ∞ are useful for designing a communication protocol over a shared directional multi-channel. For this application, they construct (r,t)-RS graphs on n vertices with r = (log n)Ω(loglogn/(log loglogn)

2) and rt is roughly equal to n2/24. Note that none of the constructions mentioned so far gives an n-vertex (r,t)-RS graph with positive edge density and at the same time being an edge-disjoint union of induced matchings of size nε for some constant ε. This range of parameters is important for some applications when there is a tradeoﬀ between the number of missing edges and the number of induced matchings. Indeed Meshulam [16] conjectures that there exist no such graphs. This conjecture was recently disproved by Alon, Moitra and Sudakov [3] with a surprising construction of graphs with edge density 1 − o(1) that can be partitioned into induced matchings of size n1−o(1), which is nearly linear in n. Their constructions have also found a couple of interesting applications for communication problems over shared channels, linearity testing, communication complexity and the directed Steiner tree problem.

Another appealing direction is to determine the maximum number of induced matchings when their sizes are linear in n. Fischer et al. in [12] gave a family of (n/6−o(n),nΩ(1/log logn))RS graphs. They use these graphs to establish an nΩ(1/log logn) lower bound for testing monotonicity in general posets. A slight twist of their construction gives (cn,nΩ(1/loglogn))-RS graphs for any positive constant c < 1/4. In this paper, we ﬁrst study the range c > 1/4. It was noticed earlier by Alon [2] that for this range, there can only be constantly many matchings. Our ﬁrst result determines the maximum number of induced matchings for c > 1/4. Its proof combines techniques from coding theory together with properties of Kneser graphs.

- Theorem 1.2. Suppose G is an (r,t)-RS graph on n vertices, then

r ≤

 



n 4

![image 3](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile3.png>)

1 +

1 t

![image 4](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile4.png>)

if 2 ∤ t,

n 4

![image 5](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile5.png>)

1 +

1 t + 1

![image 6](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile6.png>)

if 2 | t

. (1)

Moreover, these bounds are tight for every positive integer t and inﬁnitely many n.

For r = n/4, it was known that there are RS-graphs with logarithmically many induced matchings [18, 2] but there were no good upper bounds in this case. Our second theorem shows that up to a constant factor the maximum number of induced matchings when r = n/4 is indeed logarithmic.

- Theorem 1.3. If an n-vertex graph G is an (n/4,t)-RS graph, then t ≤ (6 + o(1))log2 n.

The Problem 1.1 becomes much more diﬃcult when the size r = cn of the induced matching is below the threshold n/4. For this range, the best known upper bound is due to Fox [13], who improved estimates which one obtaines from the Szemer´edi regularity lemma [22]. His result implies that the number of matchings is at most n/ log(x) n = o(n), where x = O(log(1/c)) and log(x) n denotes the x-fold iterated logarithm. This shows that the number of induced matchings has to be sublinear. On the other hand, the example of Fischer et al. [12] shows that for c < 1/4, the number of matchings could be nΩ(1/loglogn), which is much larger than log n but smaller than nε. It would be very interesting to close the huge gap between the upper and lower bounds for some ranges of c < 1/4. Here we are able to make some progress on this problem and to improve the upper bound to O(n/ log n), when c is ﬁxed strictly between 1/5 and 1/4.

- Theorem 1.4. For every ε > 0, if G is an (r,t)-RS graph on n vertices with r = cn for 1/5 + ε ≤ c < 1/4, then t = O(n/ log n).


- By a more careful analysis, we are able to further improve the upper bound to o(n/ log n), when c is slightly below 1/4. To be more precise, the little-o term comes from the best known bound in the triangle removal lemma proved in [13].
- Theorem 1.5. There exists an absolute constant b > 0, such that for r ≥ (1/4 − b)n, if G is


∗ n)) = o(n log n).

an (r,t)-RS graph G on n vertices, then t = n/((log n)2Ω(log

The rest of the paper is organized as follows. In the next section we describe a counting proof of the upper bound in Theorem 1.2, and verify its tightness by a construction based on Kneser graphs. In Section 3, we prove Theorem 1.3 and discuss potential improvements. Section 4 consists of the proof of Theorem 1.4 and 1.5, and some remarks on the case of regular graphs. The last section contains some concluding remarks and open problems.

# 2 The size of matchings is cn with c > 1/4

In this section, we determine the maximum number of induced matchings in an (r,t)-RS graph G for r = cn and c > 1/4. To prove an upper bound, we use ideas similar to the Plotkin bound [17] in coding theory, with a small twist. The lower bound construction is based on the properties of Kneser graphs.

- Proof of Theorem 1.2: Suppose the edge set of G can be partitioned into induced matchings


- M1,··· ,Mt, each containing exactly r edges. Denote by Vi the set of vertices contained in the edges of Mi. Then |Vi| = 2r. Moreover, each of the r edges of Mi intersects Vj in at most one vertex, since otherwise Vi and Vj must span a common edge of G. This implies that |Vi∩Vj| ≤ r. Let vi ∈ {0,1}n be the characteristic vector of Vi. Then for all 1 ≤ i < j ≤ t, the Hamming distance satisﬁes


dist(vi,vj) = |Vi| + |Vj| − 2|Vi ∩ Vj| ≥ 2r + 2r − 2r = 2r.

This is already enough to show that t is constant, using bounds from coding theory. But one can do slightly better. Let v0 be the all-zero vector. To get a tight upper bound, notice that the above inequality can be extended to all 0 ≤ i < j ≤ t since, for 1 ≤ i ≤ t, |Vi| = 2r. Denote by ai (resp. bi) the number of vectors vj equal to 0 (resp. 1) in the i-th coordinate, then ai + bi = t + 1. By double counting,

2r

t + 1 2

≤

dist(vi,vj)

0≤i<j≤t

n

aibi

=

i=1

≤

n(t + 1)2/4 if 2 ∤ t, nt(t + 2)/4 if 2 | t

(2)

The last inequality follows from that aibi is maximized when ai = bi = (t + 1)/2 for odd t, and {ai,bi} = {(t + 2)/2,t/2} for even t. By simplifying the inequality we immediately obtain (1).

To show that the bound is tight, it suﬃces to consider the case t = 2k + 1. Let H be KG(2k + 1,k), the Kneser graph whose vertices correspond to all the k-subsets of a set of

- 2k + 1 elements, and where two vertices are adjacent if and only if the two corresponding sets are disjoint. We deﬁne the matchings M1,··· ,M2k+1 in the following way: the edge (A,B) belongs to Mi if and only if A ∩ B = ∅ and A ∪ B = [2k + 1] \ {i}. It is easy to see that B is


determined after ﬁxing A and i, which implies that Mi forms a matching. In order to show that every matching is induced in H, we take (A,B) and (C,D) both from Mi with A = C,D, then

- A ∪ B = C ∪ D = [2k + 1] \ {i}, it is not hard to check that A ∩ C, A ∩ D are both nonempty and therefore (A,C) and (A,D) are not contained in any Mj. By calculation, n = 2kk+1 , while


- r = 12 2kk = n4(1 + 2k1+1). Hence H is a (n4(1 + 2k1+1),2k + 1)-RS graph on n vertices. Remark. By taking m vertex-disjoint copies of the Kneser graph KG(2k + 1,k), we can construct an inﬁnite family of n-vertex (r,2k + 1)-RS graphs with r = n(1 + 1/t)/4. Moreover,


![image 7](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile7.png>)

![image 8](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile8.png>)

![image 9](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile9.png>)

![image 10](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile10.png>)

![image 11](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile11.png>)

![image 12](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile12.png>)

![image 13](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile13.png>)

![image 14](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile14.png>)

![image 15](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile15.png>)

solving n = 2kk+1 gives k ∼ 21 log2 n+Θ(loglog n), therefore we obtain a (n4 +Θ(lognn),log2 n+ Θ(log log n))-RS graph H on n vertices.

![image 16](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile16.png>)

![image 17](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile17.png>)

![image 18](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile18.png>)

# 3 The size of matchings is n/4

From Theorem 1.2, we know that in a Ruzsa-Szemer´edi graph, if every matching has size r = cn where c > 1/4, then the number of matchings is at most a constant which depends on c. On the other hand, when c = 1/4, we saw in the end of the previous section that one can have logarithmic number of induced matching. The following very natural construction [18, 2] does better and gives 2 log2 n induced matchings.

Proposition 3.1. There exists (n/4,2 log2 n)-RS graph for every integer n that is a power of 2.

Proof. Let k = log2 n and consider the k-dimensional hypercube graph H with vertex set {0,1}k, where two vectors are adjacent if their Hamming distance is 1. We ﬁrst partition the vertices into odd and even vectors, according to the parity of the sum of their coordinates. For

- 1 ≤ i ≤ k, we let the i-th matching Mi consist of edges between vectors  v and  v + ei, such that  v is even and its i-th coordinate is 0; and the (k +i)-th matching Mk+i consist of edges between an odd vector  v whose i-th coordinate equals 0 and the vector  v +  ei. This construction gives
- 2k = 2 log2 n matchings, and obviously each matching involves exactly half of the vertices. In order to verify that the matchings are induced, we consider two distinct edges from Mi, which are ( u, u +  ei) and ( v, v +  ei), such that both  u and  v are even and their i-th coordinates are


- 0. Clearly the pairs ( u, v) and ( u +  ei, v +  ei) cannot form edges of H since they have the same parity. Moreover,  u and  v +  ei (similarly,  v and  u +  ei) diﬀer in at least two coordinates. Therefore for all 1 ≤ i ≤ k, the matchings Mi we deﬁned are induced. Using a similar argument, we can also show that the matchings Mi+k are induced.


When log2 n is an even integer, we can improve slightly the above construction by adding two additional induced matchings. The ﬁrst one consists of ( u, v) where  u + v = 1 and both are even vectors. The second matching contains all edges ( u, v) where  u +  v = 1 and both are odd vectors. This gives the following corollary.

Corollary 3.2. There exists (n/4,2(log2 n + 1))-RS graphs on n vertices for every n that is an even power of 2.

One should naturally ask how good are these constructions, i.e., what upper bound can we

prove on the number t of induced matchings in an n-vertex (r,t)-RS-graph with r = n4. Note that in the proof of Theorem 1.2, when r = n/4, the inequalities in (2) are always true for

![image 19](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile19.png>)

every t. Indeed, in this case there might be linearly many n-dimensional binary vectors such that their pairwise Hamming distance is equal to n/2 by modifying the well-known Hadamard matrix into a (0,1)-matrix and taking the row vectors. In the rest of this section, we develop a

diﬀerent approach which shows that when every induced matching has size exactly n/4, there can be no more than O(log n) matchings. Therefore the above constructions are best possible up to a constant factor. Below is a quick outline of our proof.

First we show that in any graph G which is decomposable into induced matchings of size n/4, there are many pairs of adjacent vertices whose sum of degrees is large. This gives an auxiliary graph H which is the subgraph of G whose edges have large degree sum. Using additional properties of induced matchings, we can show that H has nice expansion properties. From there we can easily derive some estimates on the number of induced matchings. To illustrate this idea, we ﬁrst prove a slightly weaker upper bound. The following lemma allows us to only consider bipartite graphs for this case.

Lemma 3.3. If G is an (r,t)-RS graph on n vertices, then its bipartite double cover G × K2 is an (2r,t)-RS graph on 2n vertices.

Proof. Denote by G′ = G × K2 the bipartite double cover of the graph G. The vertices of G′ are (v,i) with v ∈ V (G) and i ∈ {0,1}. Two vertices (u,0) and (v,1) are adjacent whenever u

and v form an edge in G. Note that an induced matching Mi = {(uj,vj)}rj=1 in G corresponds to a matching M′ = {((uj,0),(vj,1))}rj=1 ∪ {((uj,1),(vj,0))}rj=1 in G′, which is of size 2r. It is also straightforward to check by deﬁnition that M′ is an induced matching. Therefore G′ is an (2r,t)-RS graph on 2n vertices,

Theorem 3.4. If G is an (n4,t)-RS graph on n vertices, then t ≤ 8(log2 n + 1).

![image 20](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile20.png>)

Proof. From Lemma 3.3, it suﬃces to show that for all n-vertex bipartite graphs G whose edges can be decomposed into induced matchings M1,··· ,Mt, each of size n/4, t is at most 8 log2 n.

Denote by dv the degree of vertex v in G. We consider the subgraph H of G, with edges

being the pair of vertices u,v such that du + dv ≥ t and (u,v) ∈ E(G). Note that e(G) = nt4 . By the Cauchy-Schwarz inequality,

![image 21](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile21.png>)

(du + dv − t) = 



v∈V (G)

(u,v)∈E(G)

nt/2 n

= n

![image 22](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile22.png>)

d2v

2

dv n

nt2 4

 − t · e(G) ≥ n v∈V(G)

−

![image 23](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile23.png>)

![image 24](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile24.png>)

2

nt2 4

−

= 0. (3)

![image 25](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile25.png>)

For any edge (u,v) ∈ E(G), all the edges incident to either u or v must belong to diﬀerent matchings. Therefore du + dv ≤ t + 1. If we denote by Ei the number of edges (u,v) such that du + dv = t + i, we have E1 + E0 + E−1 + ··· + E−t = nt/4, while inequality (3) implies that E1 − tj=1 jE−j ≥ 0. Summing these two inequalities gives 2E1 + E0 ≥ nt/4 and so E1 + E0 ≥ nt/8. So H is a n-vertex graph with at least nt/8 edges and thus its average degree is at least t/4. Hence, H has a subgraph F of minimum degree at least t/8.

Set s = t/8. For each vertex v of G, let Av denote the set of induced matchings containing

- v. Clearly |Av| = dv. We claim that if v and u are at distance k in F, then when k is odd,


|Au ∩ Av| ≤ k; and when k is even, |Au ∩ Acv| ≤ k. This statement can be proved using induction. The base cases when k = 0 and 1 are obvious. Now we assume that it is true for all k ≤ i. For k = i + 1, suppose u and v are at distance k. Let w be a vertex at distance 1 from v and i = k − 1 from u. When i is odd, from the inductive hypothesis we have |Acv ∩ Acw| = t − |Av ∪ Aw| = t − |Av| − |Aw| + |Av ∩ Aw| ≤ 1 and |Aw ∩ Au| ≤ i. Therefore,

|Au ∩ Acv| ≤ |Au ∩ Aw| + |Acw ∩ Acv| ≤ i + 1.

Similarly, when i is even, we have |Av ∩ Aw| ≤ 1 and |Acw ∩ Au| ≤ i, and hence |Au ∩ Av| ≤ |Av ∩ Aw| + |Acw ∩ Au| ≤ i + 1.

Now choose an arbitrary vertex v in F, the degree of v in F is at least s = t/8. For every integer i ≥ 0, let Ni be the set of vertices at distance i from v in graph F. By the assumption that G is bipartite, each Ni induces an independent set. We denote by ei the number of edges of F that are between Ni and Ni+1 and contained in matchings in Av (resp. Acv) when i is odd (resp. even). For odd i, we estimate the number of edges of F between Ni and Ni+1 that are contained in matchings in Acv in two diﬀerent ways. Since every vertex u ∈ Ni is contained in at least s − |Au ∩ Av| ≥ s − i such edges, and every vertex w ∈ Ni+1 is contained in no more than |Aw ∩ Acv| ≤ i + 1 such edges, we have

(s − i)|Ni| − ei−1 ≤ (i + 1)|Ni+1| − ei+1.

Similarly when n is even, by bounding the number of edges between Ni and Ni+1 that belong to matchings in Av, we obtain the same inequality as above. Summing up the inequalities for i = 0,··· ,k, we have

k−1

k

ei ≤

(s − i)|Ni| −

i=0

i=0

Simplifying this inequality gives

k+1

k+1

i|Ni| −

ei.

i=1

i=1

(k + 1)|Nk+1| ≥

k

(s − 2i)|Ni| − e0 + ek+1 + ek ≥

i=0

k

(s − 2i)|Ni|.

i=0

The second inequality follows from the observation that e0 = 0 since all edges between N0 and

- N1 are in Av.


In the next step, we prove by induction that |Ni| ≥ si . For i = 0 and 1 this is obvious. Now, assuming it is true for all i ≤ k, we have

1 k + 1

|Nk+1| ≥

![image 26](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile26.png>)

1 k + 1

=

![image 27](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile27.png>)

1 k + 1

=

![image 28](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile28.png>)

s k + 1

=

![image 29](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile29.png>)

k

1 k + 1

(s − 2i)|Ni| ≥

![image 30](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile30.png>)

i=0

k

k

s i

(s − i)

−

i

i=0

i=0

k

k

s − 1 i

−

s

s

i=0

i=0

s − 1 k

s k + 1

=

.

k

(s − 2i)

i=0

s i

s − 1 i − 1

s i

Note that the number of vertices in N0 ∪ N1 ∪ ··· ∪ Ns is at most n. We therefore have

s

s

n ≥

|Ni| ≥

k=0

k=0

s k

= 2s,

Solving this inequality gives s ≤ log2 n and hence t ≤ 8 log2 n.

As we mentioned in the introduction, this bound can be further improved to (6+o(1))log2 n by the following modiﬁcation of the above proof.

- Proof of Theorem 1.3: Recall that the proof above uses the fact that H contains E1 + E0 edges and therefore it contains a subgraph F with minimum degree at least (E1 + E0)/n, and


later on we obtained the inequality n ≥ 2(E

1+E0)/n. Let H′ be the subgraph of G consisting of edges (u,v) such that du + dv = t + 1, so e(H′) = E1. Graph H′ contains a subgraph F′ of minimum degree at least E1/n = s′. By an argument similar to the one in the previous proof, we can show that if a vertex u is at distance k from v, then |Au ∩ Av| ≤ (k + 1)/2 if k is odd, and |Au ∩ Acv| ≤ k/2 if k is even. Therefore, if we ﬁx a vertex v and let N′

i be the set of vertices having distance i from v, and deﬁne e′

i in a similar way, we have

(s′ − ⌈i/2⌉)|Ni′| − e′i−1 ≤ ⌈(i + 1)/2⌉|Ni′+1| − e′i+1. Summing up the inequalities from i = 0 to k, and using e′

−1 = e′

0 = 0 and e′

⌈(k + 1)/2⌉|Nk′+1| ≥

k

(s′ − 2⌈i/2⌉)|Ni′|.

i=0

k,e′

k+1 ≥ 0, gives

′

s′−1

′

s′−1

2i| ≥ s

2i+1| ≥ s

We can use induction to show that |N′

i and |N′

i . The i = 0 case follows from |N0′| ≥ 1 and |N1′| ≥ s′. Moreover, using the inductive hypothesis,

i

i+1

i · |N2′i| ≥

≥

- i−1
- j=0


(s′ − 2j)|N2′j| +

- i−1
- j=0


(s′ − 2(j + 1))|N2′j+1|

- i−1
- j=0


(s′ − 2j)

s′ j

s′ − 1 j

- i−1
- j=0


(s′ − 2(j + 1))

+

s′ j + 1

s′ − 1 j

′

s′−1

′

s′−1

Substituting in the identity (s′ − j) s

j = (j + 1) s

j , and then the identity (s′ − j − 1) s

j

j+1

′−1

′−1

j = (j + 1) s

j+1 , and ﬁnally computing a telescoping sum, we obtain

- i−1
- j=0


(s′ − j − 1)

i · |N2′i| ≥

s′ j + 1

s′ − 1 j

− j

s′ j

s′ − 1 j

- i−1
- j=0


s′ j + 1

s′ − 1 j + 1

s′ j

s′ − 1 j

− j

(j + 1)

=

s′ i

s′ − 1 i Similarly, it can be veriﬁed that |N′

= i

′

s′−1

2i+1| ≥ s

i by the inductive hypothesis. By counting the number of vertices in F′, we have

i+1

n ≥ |N0′| + 

s′−1



i=1

≥ 1 + 

s′−1



i=1

= 1 + 

s′−1



i=1

|N2′i−1| + |N2′i|

 + |N2s′|

s′ i

s′ − 1 i

s′ i

s′ − 1 i − 1

+

s′ i

  + 1 =

2

2s′ s′

.

  + 1

Therefore

- 1

![image 31](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile31.png>)

- 2


E1/n = s′ ≤ (

+ o(1))log2 n.

Together with the previously established inequalities (E1 + E0)/n = s ≤ log2 n and 2E1 + E0 ≥ nt/4, we have

3 2

nt/4 ≤ 2E1 + E0 ≤ n(E1/n + (E1 + E0)/n) ≤ (

![image 32](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile32.png>)

+ o(1))n log2 n,

and t ≤ (6 + o(1))log2 n, which completes the proof. Remark. If the (n/4,t)-RS graph G is regular, then we can improve the upper bound to

![image 33](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile33.png>)

![image 34](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile34.png>)

![image 35](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile35.png>)

![image 36](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile36.png>)

- t ≤ 2(log2 n + 1). In the proof of Theorem 3.4, the auxiliary graph H is the same with G, in which every vertex has degree exactly t/2. Therefore for bipartite graph G, we have n ≥ 2t/2


and t ≤ 2 log2 n, and for general graphs we have t ≤ 2(log2 n + 1). This bound is the the best we could hope for by Corollary 3.2.

# 4 The size of matchings is below n/4

For the purpose of simplicity, we will use log in place of log2 throughout this section.

- Proof of Theorem 1.4: Let G = (V,E) and E(G) be the disjoint union of t induced matchings from M such that each matching consists of r = cn edges with 1/5 + ε ≤ c < 1/4. Suppose for contradiction t = Kn/ logn and K = 100/ε. We start by deﬁning V0 = V (G). For each positive integer i, let vi be a vertex of maximum degree in the induced subgraph of G on the vertex set Vi−1, Ni be the set of neighbors of vi in Vi−1, and Vi = Vi−1 \Ni. Suppose |Ni| = ni, then by deﬁnition n1 ≥ n2 ≥ ··· and ni ≤ di, where di is the degree of vi in G. Let k be the maximum integer such that nk ≥ 2n/ logn. Since all the Ni’s are disjoint, we have n ≥ ki=1 |Ni| ≥ k · (2n/ logn), hence k ≤ (log n)/2. Note that |Vi| = n − ij=1 nj, and its


number of edges e(Vi) is at least e(G) − ij=1 n2j, since every vertex in Nj has degree at most nj in Vj−1. By the choice of k, we also know that e(Vk) ≤ 1/2 · (2n/ logn) · n = n2/ logn.

Here is the key observation: for every i, an induced matching M ∈ M containing the vertex

- vi can only contain one vertex in Ni. Suppose this is not true, then M contains distinct x,y ∈ Ni, without loss of generality we may assume that vix and yz are edges of M for some vertex z. Since vi and y are adjacent, this violates the assumption that M is induced. It follows immediately from this observation that if S is a subset of {v1,··· ,vk} and a matching M ∈ M contains


precisely those vertices in S, then M has at least r − |S| edges inside the set V \ ( i∈S Ni). Now we let M be a matching chosen uniformly at random from M, and let S be the subset

of {v1,...,vk} that M contains. Deﬁne YM to be a random subset YM = V \ ( i∈S Ni). Observe that the probability that a random matching in M contains a vertex vi is equal to di/t. Therefore, using di ≥ ni,

k

k

n2i/t

P(vi ∈ M) · |Ni| ≤ n −

E[|YM|] = n −

i=1

i=1

≤ n − 1/t · (e(G) − e(Vk)) ≤ n − 1/t · (rt − n2/ log n) (4)

= (1 − c + 1/K)n.

Now we partition the t induced matchings from M into 2k ≤ 2(logn)/2 = n1/2 classes according to the set V (M) ∩ {v1,··· ,vk}. For a ﬁxed constant α ∈ (0,1), note that at most αt

matchings in M come from those classes of sizes less than αKn1/2/(2 logn), since otherwise bounding the number of matchings gives αt ≤ αKn1/2/(2 logn) · n1/2, which results in a contradiction. Therefore the probability that a random matching M belongs to one of the small classes ≤ α. On the other hand, by Markov’s inequality and (4),

E[|YM|] (1 − c + 1/K + α)n

P(|YM| ≥ (1 − c + 1/K + α)n) ≤

![image 37](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile37.png>)

α 1 − c + 1/K + α

≤ 1 −

.

![image 38](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile38.png>)

Since c > 1/5 and K > 100/ε > 100, we have

α 1 − c + 1/K + α

>

![image 39](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile39.png>)

α 1 − 1/5 + 1/100 + α

> α

![image 40](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile40.png>)

if α ≤ 1/10. Therefore, by the union bound, we can ﬁnd a class containing t′ ≥ αKn1/2/(2 logn) =

- n1/2−o(1) matchings, each of size at least r′ = r − (log n)/2 = (c − o(1))n, on the same vertex set of size at most n′ = (1 − c + 1/K + α)n. When c > 1/5 + ε, K = 100/ε and α is suﬃciently small,

r′/n′ = (c − o(1))/(1 − c + 1/K + α) ≥ 1/4. However, from Theorem 1.3, we know that in this case t′ is at most (6 + o(1))log n′ ≤ (6 +

- o(1))log n, which contradicts that t′ ≥ n1/2−o(1).


![image 41](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile41.png>)

![image 42](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile42.png>)

![image 43](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile43.png>)

![image 44](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile44.png>)

Remark. When the graph G is regular or nearly regular, we can prove the O(n/ log n) upper bound for a wider range 1/6 + ε ≤ c < 1/4. It is easy to see that every vertex has degree about (2rt)/n = 2ct in this case. We start with all the vertices uncovered and in each step we pick a vertex covering the most number of uncovered vertices. Let Xi be the set of uncovered vertices in the i-th step. The sum of degrees of vertices in Xi is equal to 2ct|Xi|. Therefore, there exists a vertex vi covering at least 2ct|Xi|/n vertices of Xi. After k steps, there are at most n(1 − 2ct/n)k uncovered vertices left. When k = (log n)/2, t > Kn/ logn and K is suﬃciently large, this gives o(n) uncovered vertices. Note that from the proof of Theorem 1.4, the probability that a random matching from M covers a ﬁxed vertex is equal to di/t, which is about 2ct/t = 2c. Therefore the expected number of vertices that are uncovered by vertices of {v1,··· ,vk} ∩V (M) is equal to n − 2c(n − o(n)) = (1 − 2c + o(1))n. Similarly as before we ﬁnd a large class of induced matchings which are of size (c − o(1))n and on the same vertex set of size at least (1 − 2c + o(1))n. When c > 1/6 + ε, we are able to apply Theorem 1.3 and derive a contradiction.

- Proof of Theorem 1.5: Let b = 10−9. Suppose for contradiction t > 2n/(C log n) and n is suﬃciently large. Here C = C(n) is a function that tends to inﬁnity slowly when n → ∞, which


we will choose later. By Lemma 3.3, F = G×K2 is a (2r,t)-RS graph with parts A and B, each of order n. Denote by M the collection of t induced matchings that make up F. The number of edges of F is 2rt = (1/2 − 2b)tn. We will pick a sequence of disjoint subsets A1,··· ,As from A, such that for each i, |Ai| = Ct, and s is the smaller integer so that sCt ≥ n/2 (thus

- s ∼ n/(2Ct) < (log n)/4), moreover there is a subcollection of induced matchings Mi ⊂ M such that |Mi| ≥ t/16 and each matching in Mi contains at most qCt vertices from Ai, where


- q = 1/100. We ﬁrst show that such a sequence of disjoint subsets would complete the proof. So suppose


such a sequence of disjoints subsets exists. Deﬁne an auxiliary bipartite graph X with ﬁrst part being [s] = {1,··· ,s}, and the second part being the matchings in M, where (i,M) is an edge of X if and only if M ∈ Mi. The minimum degree of vertices in [s] is at least t/16, therefore

the average degree of vertices in M is at least (t/16)s/|M| = s/16. We can ﬁnd a complete bipartite subgraph in X with one part |S| = s/16, and the other part M′ ⊂ M with

|M′| ≥ |M|/

s s/16

≥ |M|/2s ≥ t/2(logn)/4 > n1/2.

Such a subgraph exists because the number of stars with a center in some M ∈ M and s/16 leaves in [s] is equal to M∈M d

s/16 , where dM is the degree of M. By convexity and M dM ≥ |M|(s/16), this number is at least |M|. Therefore, there exists such a subset S of [s] of size

M

- s/16, whose vertices have at least |M|/ s/ s16 common neighbors in M. Let Y be the union of Ai with i ∈ S, thus |Y | = Ct(s/16) ≥ n/32. Each matching in M′


contains at most qCts/16 ≤ n/3200 elements of Y ; thus it contains at least 2r − n/3200 = (1/2 − 2b − 1/3200)n > 0.499n edges going between A \ Y (which has size at most 31n/32) and

- B (which has size n). Note that 0.499n > 41|B ∪ (A \ Y )| = 12863 n. Hence, by Theorem 1.2 there can only be a constant number of such induced matchings, a contradiction. So it suﬃces to


![image 45](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile45.png>)

![image 46](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile46.png>)

show the existence of the desired disjoint subsets A1,··· ,As of A.

We ﬁrst show that the graph F is nearly regular. Let p = 1/2000, and A = A′ ∪ A′′ be the partition of A where v ∈ A′ if and only if |dF(v)−(t+1)/2| ≤ p(t+1). We will show that A′′ is quite small. Consider the paths of length two with both end points in A. The number of such paths is equal to

v∈B

dF(v) 2

- 1

![image 47](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile47.png>)

- 2 v∈B


- 1

![image 48](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile48.png>)

- 2 v∈B


dF(v)2 − rt ≥

(2rt/n)2 − rt

=

1 4

1 8

1 4

− b)2t2n − (

− 2b)(t + 1)2n. (5)

− b)tn > (

= 2(

![image 49](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile49.png>)

![image 50](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile50.png>)

![image 51](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile51.png>)

Note that since F is a (2r,t)-RS graph, every edge of F has sum of degrees of its two vertices at most t+1. In particular, for any v ∈ A and every its neighbor u ∈ B we have d(u) ≤ (t+1−d(v)). Therefore, every vertex v ∈ A is the end point of at most d(v)(t+1−d(v)) ≤ (t+1)2/4 paths of length two in F. Moreover, each vertex in A′′ is the end point of at most (14 −p2)(t+1)2 paths of length 2 in F. Therefore the number of paths of length two with both endpoints in A is at most

![image 52](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile52.png>)

- 1

![image 53](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile53.png>)

- 2(n−4p2|A′′|)(t+1)2/4. This estimate together with (5) implies that |A′′| < (4b/p2)n = 2n/125. Similarly, let B = B′ ∪ B′′ be the partition of B where B′ consists of vertices which have


degree within p(t + 1) of (t + 1)/2, analogously we get |B′′| < 2n/125. Let A∗ be those vertices in A with at least t/4 neighbors in B′′. Since the number of edges coming out of B′′ is at most |B′′|t, then A∗ has at most |B′′|t/(t/4) = 4|B′′| < 8n/125 elements. Thus there are at least n − 2n/125 − 8n/125 ≥ 0.9n elements of A neither in A′′ nor A∗. Let a1 be one such element in A, so a1 is adjacent to at most t/4 neighbors in B′′. Let B1 be those vertices in B′ adjacent to a1. So |B1| ≥ (1/2 − p)(t + 1) − t/4 > t/8, and |B1| ≤ t. Let A# be those vertices in A adjacent to at least one vertex in B1. The number of edges coming out from B1 is at least |B1|(1/2 − p)(t + 1) ≥ (t/8)(1/2 − p)(t + 1) > t2/20. If |A#| < Ct, then we would have a bipartite graph between A# and B1 with parts of size at most Ct and t respectively but with at least t2/20 edges. This graph is an RS-graph on at most (C(n) + 1)t vertices with at least t2/20 edges which can be decomposed into t induced matchings. It is well known that this leads to a graph R on ∼ C(n)t vertices with Ω(t2) edges, in which every edge is contained in exactly one triangle (see e.g. Proposition 3.1 in [3]). We take C(n) to be 2Ω(log

∗ n), where log∗ is the iterated logarithm. The best known bound on the triangle removal lemma [13] (see also [11] for an alternative proof) guarantees that such a graph R cannot exist. We therefore have |A#| ≥ Ct. Let A1 be an arbitrary subset of A# of size Ct.

Let M′ be the collection of matchings in M containing a1, and M′′ be the matchings not containing a1, then |M′| ≥ (1/2−p)(t+1) and |M′′| ≤ t−(1/2−p)(t+1). Each vertex v ∈ B1 is in at least (1/2 − p)(t + 1) matchings, and all but one of them is in M′′. Thus a vertex u in A1 (which is adjacent to some v ∈ B1) cannot be contained in these matchings except for one, so u is in at most t − (1/2 − p)(t + 1) − (1/2 − p)(t + 1) + 1 = 2p(t + 1) matchings in M′′. Therefore the number of matchings in M′′ that contain at least qCt elements of A1 is at most 2p(t + 1)(Ct)/(qCt) = 2p(t + 1)/q < t/8 ≤ |M′′|/2. Therefore at least half the matchings in M′′ contain at most qCt elements of A1. Let M1 be the set of these matchings, we have |M1| ≥ t/16.

We have thus pulled out the desired sets A1 and M1 and ﬁnished the ﬁrst step. In the second step, we ﬁnd A2 in A \ A1 and M2 in a similar fashion. After the i-th step, we have pulled out disjoint sets A1,··· ,Ai and also found sets of matchings M1,··· ,Mi. Note that |A′′ ∪A∗∪A1∪···∪Ai| ≤ 2n/125+8n/125+sCt ≤ 0.7n. Let A0 = A\(A′′∪A∗∪A1 ∪···∪Ai), then |A0| ≥ 0.3n. Note that by similar arguments, every vertex in A0 is adjacent to at least t/8 neighbors in B′. Moreover let ev be the number of paths vuv′ with v,v′ ∈ A0 and u ∈ B′. Note that ev,v ∈ A0 counts precisely the number of edges between the neighbors of v in B′ and the second neighborhood of v in A0. For u ∈ B′, let d′

u be the number of vertices in A0 adjacent to

- u, then


v

ev = 2

u∈B′

d′u 2

≥ 2

e(A0,B′)/|B′| 2

Therefore there exists a vertex ai+1 ∈ A0, such that

|B′|

≥ 2

ea

i+1

e(A0,B′)/|B′| 2

e(A0,B′) |A0|

|B′|/|A0| =

![image 54](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile54.png>)

e(A0,B′) |B′|

− 1 .

![image 55](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile55.png>)

Since every vertex in A0 is adjacent to at least t/8 vertices in B′, we have e(A0,B′)/|A0| ≥

≥ (t/8)(0.3nt/8n − 1) ≥ t2/300. Once again the triangle removal lemma implies that we can pick Ai+1 to be any Ct vertices from A0 that are second neighbors of ai+1. Let Mi+1 be the collections of matchings in M not containing ai+1 and containing at most qCt elements of Ai+1, similarly we have |Mi+1| ≥ t/16. In the end we obtain the disjoint subsets A1,··· ,As and collections of matchings M1,··· ,Ms as desired.

- t/8, and e(A0,B′) ≥ 0.3nt/8. Hence ea


i+1

![image 56](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile56.png>)

![image 57](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile57.png>)

![image 58](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile58.png>)

![image 59](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile59.png>)

# 5 Concluding Remarks

In this paper we consider the problem of determining the maximum number of induced matchings

- t as a function in the size of matchings r and number of vertices n, and settle the problem for


- r = cn when c > 1/4 and c = 1/4. Several intriguing problems remain open.


- • When r = n/4, we prove that t ≤ (6 + o(1))log2 n, while the hypercube construction and


its reﬁnement only gives a t = (2 + o(1))log2 n lower bound. For regular graphs, we know this lower bound is tight. It seems plausible that for r,n satisfying r = n/4 and n tending to

inﬁnity, we always have t ≤ 2 log2 n + 2. The expansion part of our proof of Theorem 1.3 is pretty robust in that it uses nothing about the number t of matchings. However, there are two places we lost a constant factor in the proof. We ﬁrst pass from G to H (resp. H′), keeping only edges whose sum of degrees is at least t (resp. t + 1). Maybe it is possible to somehow incorporate negative edges (i.e., whose sum of degrees of its two vertices is less than t) in the

argument. In the second step, we pass from H (or H′) to its subgraph by keeping only high degree vertices. It would be great to do a more careful analysis and eventually improve the constant before log2 n from 6 to 2.

- • When the size of matchings is close to n/4, there are two quite diﬀerent constructions of Ruzsa-Szemer´edi graphs. One is the Kneser graph KG(2k + 1,k) with k ∼ 12 log2 n, which is an (n/4 + Θ(n/ logn),(1 + o(1))log2 n)-RS graph. The other is the hypercube {0,1}log2 n, which is an (n/4,2 log2 n)-RS graph. Can we ﬁnd a family of (r,t)-RS graphs that bridge between these two examples, say with r = c log2 n for some c ∈ [1,2], and t−n/4 = Ω(log n)?

![image 60](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile60.png>)

- • In Section 4 we obtained an upper bound O(n/ log n) on the number of matchings when c

is between 1/5 and 1/4, and improved the bound to n/((log n)2Ω(log

∗ n)) for c > 1/4 − b for some constant b > 0. However the best construction [12] so far only gives nΩ(1/log logn). It remains a challenging question to close this gap for this range, and in general for all r linear in n.

- • Another interesting open problem is to maximize the size of induced matchings, when the number of matchings is linear in n. It is somewhat complementary to the questions we studied in this paper. The Ruzsa-Szemer´edi theorem [20] gives an upper bound o(n), which in turn gives a similar bound for Roth’s theorem. On the other hand, for Roth’s theorem, much better results are known. The current best upper bound on the size of the largest subset of [n] with no 3-term arithmetic progression is of the form O(n/ log1−o(1) n), ﬁrst proved by Sanders [21] using Fourier analysis on Bohr sets and subsequently improved slightly further by Bloom [8]. It would be very interesting to see whether a similar bound holds for the Ruzsa-Szemer´edi theorem. Moreover, the best known lower bound for both problems is still


√logn) obtained by Behrend [6] about seventy years ago. Closing the gap between these bounds is an important open problem.

![image 61](<2015-fox-graphs-decomposable-induced-matchings_images/imageFile61.png>)

essentially n/eO(

# References

- [1] N. Alon, Testing subgraphs in large graphs. Random Structures Algorithms 21 (2002), 359–370.
- [2] N. Alon, private communication.
- [3] N. Alon, A. Moitra, and B. Sudakov, Nearly complete graphs decomposable into large induced matchings and their applications. J. Eur. Math. Soc. (JEMS) 15 (2013), no. 5, 1575–1596.
- [4] N. Alon and A. Shapira, Testing subgraphs in directed graphs. J. Comput. System Sci. 69

(2004), 354–382.

- [5] N. Alon and A. Shapira, A characterization of easily testable induced subgraphs. Combin.

- Prob. Comput. 15 (2006), 791–805.

[6] F. Behrend, On sets of integers which contain no three terms in arithmetic progression.

- Proc. Natl. Acad. Sci. USA, 32 (1946), 331–332.


- [7] Y. Birk, N. Linial and R. Meshulam. On the uniform-traﬃc capacity of single-hop interconnections employing shared directional multichannels. IEEE Trans. Inform. Theory (1993), 186–191.
- [8] T. F. Bloom, A quantitative improvement for Roth’s theorem on arithmetic progressions, preprint. http://arxiv.org/abs/1405.5800v2


- [9] W. Brown, P. Erdo˝s, and V. So´s, Some extremal problems on r-graphs. New Directions in the Theory of Graphs, Proc. 3rd Ann Arbor Conference on Graph Theory, Academic Press, New York, 1973, 55–63.
- [10] W. Brown, P. Erdo˝s and V. So´s, On the existence of triangulated spheres in 3-graphs and related problems. Period. Math. Hungar. 3 (1973), 221–228.
- [11] D. Conlon and J. Fox, Graph removal lemmas, Surveys in combinatorics 2013, 1–49, London Math. Soc. Lecture Note Ser., 409, Cambridge Univ. Press, Cambridge, 2013.
- [12] E. Fischer, E. Lehman, I. Newman, S. Raskhodnikova, R. Rubinfeld, and A. Samorodnitsky, Monotonicity testing over general poset domains. Proc. 34th Annual ACM Symposium on Theory of Computing, ACM, New York, 2002, 474–483.
- [13] J. Fox. A new proof of the graph removal lemma. Ann. of Math. 174 (2011), 561–579.
- [14] P. Frankl and Z. F¨uredi, Colored packing of set, in: Combinatorial Design Theory. Ann. Discrete Math. 34 (1987), 165–178.
- [15] J. Ha˚stad and A. Wigderson, Simple analysis of graph tests for linearity and PCP. Random Structures Algorithms 22 (2003), 139–160.
- [16] R. Meshulam. Private communication, 2011.
- [17] M. Plotkin, Binary codes with speciﬁed minimum distance. IRE Transactions on Information Theory 6 (1960), 445–450.
- [18] S. Rashodnikova, Property Testing: Theory and Applications, PhD Thesis, Massachusetts Institute of Technology, 2003.
- [19] K. Roth, On certain sets of integer. J. London Math. Soc. 28 (1953), 104–109.
- [20] I. Ruzsa and E. Szemer´edi, Triple systems with no six points carrying three triangles. Colloquia Mathematica Societatis J´anos Bolyai (1978), 939–945.
- [21] T. Sanders, On Roth’s theorem on progressions. Ann. of Math. 174 (2011), 619–636.
- [22] E. Szemer´edi. Regular partitions of graphs. In Colloques Internationaux CNRS 260 Probl´emes Combinatoires et Th´eorie des Graphes, Orsay (1976), 399–401.


