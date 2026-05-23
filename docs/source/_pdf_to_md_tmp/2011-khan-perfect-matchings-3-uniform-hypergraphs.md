## arXiv:1101.5830v3[cs.DM]7Jul2012

### Perfect matching in 3-uniform hypergraphs with large vertex degree

Imdadullah Khan∗

Department of Computer Science College of Computing and Information Systems Umm Al-Qura University Makkah, Saudi Arabia

iikhan@uqu.edu.sa

###### Abstract

A perfect matching in a 3-uniform hypergraph on n = 3k vertices is a subset of n3 disjoint edges. We prove that if H is a 3-uniform hypergraph on n = 3k vertices such that every vertex belongs to at least n−21 − 2n/2 3 + 1 edges then H contains a perfect matching. We give a construction to show that this result is best possible.

##### 1 Introduction and Notation

For graphs we follow the notation in [2]. For a set T, we refer to all of its k-element subsets (k-sets for short) as Tk and to the number of such k-sets as |Tk| . We say that H = (V (H),E(H)) is an r-uniform hypergraph or r-graph for short, where V (H) is the set of vertices and E ⊂ V (rH) , a family of r-sets of V (H), is the set of edges of H. We say that H(V1,...,Vr) is an r-partite r-graph, if there is a partition of V (H) into r sets, i.e. V (H) = V1 ∪ ··· ∪ Vr and every edge of H uses exactly one vertex from each Vi. We call it a balanced r-partite r-graph if all Vi’s are of the same size. Furthermore H(V1,...,Vr) is a complete r-partite r-graph if every r-tuple that uses one vertex from each Vi belongs to E(H). We denote a complete balanced r-partite r-graph by K(r)(t), where t = |Vi|. When the graph referred to is clear from the context we will use V instead of V (H) and will identify H with E(H) and er(H) = |E(H)|. A matching in H is a set of disjoint edges of H and a perfect matching is a matching that contains all vertices. For U ⊂ V , H|U is the restriction of H to U.

∗Research supported in part by a DIMACS research grant.

For an r-graph H and a set D = {v1,...,vd} ∈ Vd ,1 ≤ d ≤ r, the degree of D in H, degH(D) = degr(D) denotes the number of edges of H that contain D. For 1 ≤ d ≤ r, let

V d

δd = δd(H) = min degr(D) : D ∈

.

When H is an r-graph and A and B are disjoint subsets of V (H), for a vertex v ∈ A we denote by degr(v, r B−1 ) the number of (r − 1)-sets of B that make edges with v, while dr(v, r B−1 ) = degr(v, r B−1 )/ r |B−1| denotes the density. For such A and B, er(A, r B−1 ) is the sum of degr(v, r B−1 )

er(A, r B−1 ) |A| r |B−1|

over all v ∈ A while dr(A, r B−1 ) =

. We denote by H(A, r B−1 ) such an r-graph when

all edges of H use one vertex from A and r − 1 vertices from B. When A1,...,Ar are disjoint subsets of V , for a vertex v ∈ A1 we denote by degr(v,(A2 × ··· × Ar)) the number of edges in the r-partite r-graph induced by the subsets {v},A2,...,Ar, and e(A1,(A2 × ··· × Ar)) is the sum of degr(v,(A2 × ··· × Ar)) over all v ∈ A1. Similarly

e(A1,(A2 × ··· × Ar)) |A1 × A2 × ··· × Ar|

dr(A1,(A2 × ··· × Ar)) =

.

An r-graph H on n vertices is η-dense if it has at least η nr edges. We use the notation dr(H) ≥ η to refer to an η-dense r-graph H. A bipartite graph G = (A,B) is η-dense if d(A,B) ≥ η. For

U ⊂ V , for simplicity we refer to dr(H|U) as dr(U) and to E(H|U) as E(U). Throughout the paper log denotes the base 2 logarithm. Moreover we will only deal with r-graphs on n vertices where n = rk for some integer k, we denote this by n ∈ rZ.

Deﬁnition 1. Let d,r and n be integers such that 1 ≤ d < r, and n ∈ rZ. Denote by md(r,n) the smallest integer m, such that every r-graph H on n vertices with δd(H) ≥ m contains a perfect matching.

For graphs (r = 2), by the Dirac’s theorem on Hamiltonicity of graphs [5], it is easy to see that m1(2,n) ≤ n/2, and since the complete bipartite Kn/2−1,n/2+1 does not have a perfect matching we get m1(2,n) = n/2. For r ≥ 3 and d = r − 1, it follows from a result of R¨dl, Rucin´ski and Szemer´edi on Hamiltonicity of r-graph [18] that mr−1(r,n) ≤ n/2 + o(n). Ku¨hn and Osthus [9] improved this result to mr−1(r,n) ≤ n/2 + 3r2√nlog n. This bound was further sharpened in [17] to mr−1(r,n) ≤ n/2 + C log n. In [15] the bound was improved to almost the true value; it was proved that mr−1(r,n) ≤ n/2 + r/4. Finally [19] settled the problem for d = r − 1. Ku¨hn and Osthus [9] and Aharoni, Georgakopoulos and Spru¨ssel [1] studied the minimum degree threshold for perfect matching in r-partite r-graphs.

The case d < r − 1 is rather hard. Pikhurko [13] proved that for all d ≥ r/2, md(r,n) is close to n−d r−d . For 1 ≤ d < r/2, H`n, Person and Schacht [7] proved that

- 1

- 2


r − d r

n − d r − d

md(r,n) ≤

+ o(1)

A recent survey of these and other related results appear in [14]. In [7] the authors posed the following conjecture.

Conjecture 2 ([7], see [14] P. 23 ). For all 1 ≤ d < r/2,

r−d n − d

r − 1 r

- 1

- 2


md(r,n) ∼ max

,1 −

r − d Note that for r = 3 and d = 1 the above bound yields

n − 1 2 Improving an old result of Daykin and H¨ggvist [4], the authors of [7] proved an approximate version of their conjecture for the case r = 3 and d = 1, they showed that m1(3,n) ≤ 9 5 + o(1) n2 for large n. For the case r = 4 and d = 1, Markstr¨m and Rucin´ski [12] proved that m1(4,n) ≤

5 9

m1(3,n) ∼

42 64 + o(1) n−31 . Lo and Markstr¨m [11] determined the exact degree threshold for r = 3 and

d = 1 for the case of 3-partite 3-graphs.

In this paper we settle Conjecture 2 for the case r = 3 and d = 1. Parallel to this work, independently Ku¨hn, Osthus and Treglown [10] proved the same result. We believe our techniques are more general and have many other applications. In our subsequent work [8] we use similar techniques to prove Conjecture 2 for the case r = 4 and d = 1 as well. Our main result in this paper is the following theorem.

Theorem 3. There exist an integer n0 such that if H is a 3-graph on n ≥ n0 vertices (n ∈ 3Z), and

n − 1 2 −

2n/3 2

δ1(H) ≥

+ 1 (1)

then H has a perfect matching. On the other hand the following construction from [7] shows that the result is best possible.

Construction 4. Let H = (V (H),E(H)) be a 3-graph on n vertices (n ∈ 3Z), such that V (H) is partitioned into A and B, |A| = n3 −1 and |B| = n−|A| and E(H) is the set of all 3-sets of V (H), T, such that |T ∩ A| ≥ 1 (see Figure 1).

We have δ1(H) = n−21 − 2n/2 3 (the degree of a vertex in B) but since every edge in a matching must use at least one vertex from A, the maximum matching in H is of size |A| = n3 − 1.

|A| = n3 − 1

|B| = 23n + 1

Figure 1: The extremal example: every edge intersects the set A.

##### 2 The main result

We distinguish two cases to prove Theorem 3. In Section 4 we show that a slightly relaxed minimum degree condition implies that either H has an ‘almost perfect matching’ or H is ‘close to’ the extremal example of Construction 4. In case H is not close to the extremal example we ﬁrst ﬁnd an almost perfect matching and extend it to a perfect matching in H using the ‘absorbing’ technique. On the other hand, when H is close to the extremal example, in Section 5 we build a perfect matching in H with a greedy approach.

Deﬁnition 5 (Extremal Case with parameter α). For a constant 0 < α < 1, we say that H is α-extremal, if the following is satisﬁed otherwise it is α-non-extremal. There exists a B ⊂ V (H) such that

- • |B| ≥ 3 2 − α n

- • d3 (B) < α.


When H is α-non-extremal, we use the absorbing lemma, which roughly states that in H there exists a small matching M with the property that every ‘not too large’ subset of vertices W can be absorbed into a matching covering V (M) ∪ W.

Lemma 6. (Absorbing Lemma, [7]) For every η > 0, there is an integer n0 = n0(η) such that if H is a 3-graph on n ≥ n0 vertices with δ1(H) ≥ (1/2 + 2η) n2 , then there exists a matching M in H of size |M| ≤ η3n such that for every set W ⊂ V \ V (M) of size at most η6n ≥ |W| ∈ 3Z, there exists a matching covering all the vertices in V (M) ∪ W.

After removing an absorbing matching M from H we ﬁnd an almost perfect matching in

H|V \V (M). The few vertices not covered by this almost perfect matching are absorbed into M to get a perfect matching in H. Theorem 7 in Section 4, using the tools developed in Section 3, guarantees the existence of an almost perfect matching in the non-extremal case.

- Theorem 7. For all 0 < η α 1, there is an n0 such that if H is a 3-graph on n ≥ n0 vertices with

δ1(H) ≥

5 9 − 10η

n 2

, then either

- • H contains a matching leaving strictly less than η2n vertices unmatched or
- • H is α-extremal.


When H is α-extremal then almost all vertices of A make edges with almost all 3-sets in B3 , where B is as in Deﬁnition 5 and A = V (H) \ B. In Section 5 we ﬁrst match the few vertices of A that do make edges with almost all 3-sets in B3 and the remaining vertices are matched using a Ko¨nig-Hall type argument.

- Theorem 8. For all 0 < α 1, there is an n0 such that if H is an α-extremal 3-graph on n ≥ n0 vertices with


n − 1 2 −

2n/3 2

δ1(H) ≥

+ 1, then H contains a perfect matching.

Proof of Theorem 3. Let 0 < α 1 be given. Applying Lemma 6 with parameter √α, Theorem 7 with parameter α3/2 and Theorem 8 with parameter α, we get n 0,n 0 and n 0 respectively. Let n0 = 2max{n 0,n 0,n 0 }. Now assume that we have a 3-graph H on n ≥ n0 vertices satisfying (1).

From (1) when n is large we have δ1(H) ≥

> 1/2 + 2√α

n − 1 2 −

n − 1 2 −

n 3

n 2

2n/3 2

5 9

.

+ 1 >

Hence H satisﬁes the conditions of Lemma 6 with parameter √α. We remove from H an absorbing matching M of size at most α3/2n.

Let H = H|V \V (M) be the remaining hypergraph (after removing M) on n = n − |V (M)| vertices. Since |V (2M)| + |V (M)| · n < 7α3/2 n2 ≤ 10α3/2 n 2 , it is easy to see that

5 9 − 10α3/2

n 2

δ1(H ) ≥

As n > n 0, using Theorem 7 (with η = α3/2), in H we ﬁnd an almost perfect matching that leaves out a set of at most α3n < α3n vertices. As guaranteed by Lemma 6 the vertices that are left out from this almost perfect matching are absorbed into M, and we get a perfect matching in H.

In case H is α-extremal, using Theorem 8 we get a perfect matching in H, which concludes the proof of Theorem 3.

##### 3 Tools

We use the following result of Erd¨s [6] to ﬁnd complete balanced r-partite subhypergraphs of r-graphs.

Lemma 9. For every integer l ≥ 1 there is an integer n0 = n0(r,l) such that every r-graph on n > n0 vertices, that has at least nr−1/lr−1 edges, contains a K(r)(l).

Corollary 10. For 0 < η 1 and r ≤ 3, if H is an r-graph on n > n0(η,r) vertices with

n r

|E(H)| ≥ η

then H contains a K(r)(t), where

t = η(log n)1/(r−1).

ηnr 2r! ≥

nr 21/ηr−1

nr n1/(ηr−1 logn)

nr n1/t(r−1)

2r! 21/η(r−1)

This is so because η nr ≥

=

=

. The following lemma is a very useful tool in this section.

, as η >

- Lemma 11. Let m be a suﬃciently large integer. If G(A,B) is an η-dense bipartite graph with |A| = c1m and B ≥ c22m for some constants 0 < c1,c2 < 1, then there exists a complete bipartite subgraph

- G (A ,B ) of G such that A ⊂ A, B ⊂ B, |A | ≥ η|A|/2 and |B | ≥


η 2 ·

|B| 2c1m ≥

ηc2 2 · 2(1−c1)m.

Proof. First we show that there is a set B1 ⊂ B such that |B1| ≥ η|B|/2 and for every vertex b ∈ B1, deg(b,A) ≥ η|A|/2. Such a subset exists because otherwise the total number of edges in G would be strictly less than

η|B| 2 · |A| + |B| ·

η|A| 2

= η|A||B|

a contradiction to the fact that G(A,B) is η-dense. Now we show that there is the required complete bipartite subgraph in G(A,B1). To see this consider the neighborhoods in A, of the vertices in B1. Since there can be at most 2|A| = 2c1m such neighborhoods, by averaging there must be a neighborhood that appears for at least |B1|

2c1m ≥

η 2 ·

|B| 2c1m ≥

ηc2 2 ·

2m 2c1m =

ηc2

2 · 2(1−c1)m vertices of B1. Hence we get the desired complete bipartite graph.

The following two lemmas are repeatedly used in Section 4.

- Lemma 12. Let m be a suﬃciently large integer and let H(X,Y,Z) be a 3-partite 3-graph with


|X| = |Y | = c1m and |Z| ≥ c22m2 for some constants 0 < c1,c2 < 1. If d3(Z,(X × Y )) ≥ η, then there exists a complete 3-partite 3-graph H (X ,Y ,Z ) as a subgraph of H, such that |X | = |Y | =

|Z | ≥ η4 log |X|.

Proof. First consider the auxiliary bipartite graph G1(A,Z), where A = X ×Y and a vertex z ∈ Z is connected to a pair (a,b) ∈ A if {a,b,z} is an edge of H. Clearly G1 satisﬁes the conditions of Lemma11. Applying Lemma 11 on G1 we get a complete bipartite graph G2(A ,Z ) such that

- A ⊂ A = X ×Y , Z ⊂ Z, |A | ≥ η|X||Y |/2 and |Z | ≥ c22η2m2(1−c21) > |X| where the last inequality follows when m is large.


Now Let G3 be a graph on vertex set X ∪ Y and (a,b) is an edge in G3 if (a,b) ∈ A . Since |A | ≥ η|X||Y |/2, we have |E(G3)| ≥

η 4

|X∪Y |

2 . Applying Corollary 10 (for r = 2), in G3 we get a

complete bipartite graph G4(X ,Y ) with X ⊂ X and Y ⊂ Y such that |X | = |Y | ≥ η4 log |X|. Clearly X , Y and a subset of Z (of size |X |), correspond to the color classes of required complete

- 3-partite 3-graph.


- Lemma 13. Let m be a suﬃciently large integer and let H A, B2 be a 3-graph such that |A| =

c1m, |B| ≥ c22m2, for some constants 0 < c1,c2 < 1. If d3 A, B2 ≥ η, then there exists a complete 3-partite 3-graph H (A ,B ,B ), with A ⊂ A, B and B are disjoint subsets of B such that |A | = |B | = |B | = η|A|/2.

Proof. First consider the auxiliary bipartite graph G1(A,P), where P = B2 and a vertex a ∈ A is connected to a pair (b1,b2) ∈ P if (a,b1,b2) is an edge of H. Applying Lemma 11 on G1 we get a complete bipartite graph (A ,P ) in G1 with A ⊂ A and P ⊂ P such that |A | ≥ η|A|/2 and

|P | ≥

η 2 ·

|P| 2c1m ≥

η 5 ·

|B|2 2c1m ≥

η 5 ·

|B|2 |B| c2

c1/m =

c22η 5

|B| c2

2−c1/m

≥ |B|2−2/η|A|

where the last inequality follows when m is large and η, c1 and c2 are small constants.

Now construct an auxiliary graph G2 where V (G2) = B and edges of G2 corresponds to pairs in P . Since |E(G2) ≥ |B|2−2/η|A|, applying lemma 9 on G2 (for r = 2) we get a complete bipartite graph with color classes B and B each of size η|A|/2. Clearly A , B , and B corresponds to color classes of a complete 3-partite 3-graph in H as in the statement of the fact.

We also use the following simple facts about graphs.

- Lemma 14. Any graph on n vertices with m edges has a subgraph of minimum degree m/n.
- Lemma 15. Any graph on n vertices has a matching of size min{δ(G), n2 }.


- 4 Proof of Theorem 7 Let H be a 3-uniform hypergraph on n vertices where n is suﬃciently large and


δ1(H) ≥

5 9 − 10η

n 2

. (2)

In H we will ﬁnd an almost perfect matching (covering at least (1 − η2)n vertices). In fact, we will prove a much stronger result. We are going to build a cover T = {T1,T2,...} where each Ti is a disjoint complete 3-partite 3-graph in H. These complete 3-partite 3-graphs will be balanced and will be of the same size. We refer to them as tripartite graphs. We say that such a cover is optimal if it covers at least (1 − η2)n vertices. We will show that either we can ﬁnd an optimal cover or H is α-extremal. It is easy to see that such an optimal cover readily gives us a matching in H that leaves out at most η2n vertices.

- Proof of Theorem 7. We begin with a cover T obtained by repeatedly applying Lemma 9 in the remaining part of H as long as there are at least η2n vertices left and the condition of Lemma 9 is satisﬁed, to get disjoint K(3)(t)’s where t = η log(η2n). Note that by Lemma 9 we can ﬁnd larger tripartite graphs in H (at least initially) but since we want all tripartite graphs to be of the same size we ﬁnd all tripartite graphs of size 3t.


Identify by T the set of tripartite graphs in the cover and let V (T ) be the union of vertices in the tripartite graphs in T . We refer to |V (T )| as size of the cover and to a subset of T as a subcover in T . Let I = V (H)\V (T ) be the set of remaining vertices. If T is not an optimal cover, then since we cannot apply Lemma 9 in H|I (with parameters η to get another K3(t)), we must have that |I| > η2n and

d3(I) < η. (3) Note that from (2) and (3) we immediately get that |V (T )| > ηn. We show that if H is α-nonextremal and T is not optimal then using the iterative procedure outlined below we can signiﬁcantly increase the size of our cover (by at least η4n vertices). After every iteration all tripartite graphs in T will be of the same size. Furthermore, all tripartite graphs in T will be balanced and if the size of a color class in the tripartite graphs at a given iteration is t, then after the iteration it will be η4 log t. We take n to be suﬃciently large so that till the end of the procedure the size of each color class is large enough for Lemma 12 and Lemma 13 to be applicable.

Let Ti = (V1i,V2i,V3i) be a tripartite graph in T . For 1 ≤ l,k ≤ 3, we say that Ti is k-sided, if d3 Vli, I2 ≥ 2η, for k color classes Vli of Ti. We will show that most of the tripartite graphs in T are at most 1-sided or we can signiﬁcantly increase the size of our cover.

Claim 16. If the number of vertices in the at least 2-sided tripartite graphs in T is more than η|V (T )|, then we can increase the size of T by at least η3n/8 vertices, such that all tripartite graphs in the cover are balanced and are of the same size.

We repeatedly use Claim 16 to increase the size of our cover as long as the condition of Claim

- 16 is satisﬁed. Hence in at most 8η−3 iterations we either get an optimal cover or the number of vertices in the at least 2-sided tripartite graphs is reduced to at most η|V (T )|. For simplicity we still denote the cover by T and I = V (H) \ V (T ). The size of a color class in each tripartite graph is still denoted by t.


Suppose that T is not optimal and we cannot apply Claim 16, then the number of 2-sided vertices in T is at most η|V (T )|. Note that if Ti ∈ T is at most 1-sided, then by deﬁnition d Ti, I2 ≤ (1/3 + 4η). This together with the bound on the number of 2-sided tripartite graphs gives us

e3 V (T ), I 2 ≤

|I| 2

1 3

+ 5η |V (T )|

. (4) For the sum of the degrees of vertices in I, (2) gives us

5 9 − 10η

n 2

deg3(v) ≥ |I|

. (5)

v∈I

On the other hand considering the number of times each edge is counted, by (3) and (4)

deg3(v) = e3 I,

v∈I

≤ e3 I,

V (T ) 2

V (T ) 2

Combining (5) and (6) we get

+ 2 · e3 V (T ), I 2

+ 3 · e3 (H|I)

+ 2 ·

1 3

+ 5η |V (T )|

|I| 2

+ 3 · η |I| 3

(6)

e3 I,

V (T ) 2 ≥ |I|

|I| 2 − 3 · η |I|

5 9 − 10η

n 2 − 2 ·

1 3

+ 5η |V (T )|

3 ≥ |I|

|I| 2 − 3 · η |I|

n 2 − 2 ·

1 3

5 9 − 10η

+ 5η |V (T )|

2 ≥ |I|

5 9 − 38η |V (T )|

.

2

In (5) and (6) using e3 I, V (2T ) ≤ |I| · |V (2T )| and the fact that η is a small constant we get |V (T )| ≥ n/2.

For a vertex v ∈ V (H), consider the edges that v makes with pairs of vertices within a tripartite graph. Since the size of a tripartite graph is 3t ≤ 3η log(η2n), the number of pairs of vertices of any tripartite graph Ti ∈ T is O(log n). Hence the total number of pairs of vertices within the tripartite graphs in T is O(nlog n) = o n2 . We ignore the at most o n3 edges that use more than one vertex from a tripartite graph. By the above observation we still have

d3 I,

V (T ) 2 ≥

5 9 − 40η (7)

Let Ti = (V1i,V2i,V3i) and Tj = (V1j,V2j,V3j) be two tripartite graphs in T . We say that I is connected to a pair of color classes (Vpi,Vqj), 1 ≤ p,q ≤ 3, if d3(I,(Vpi×Vqj)) ≥ 2η. For (Ti,Tj) ∈ T2

we deﬁne the link graph, Lij, to be a balanced bipartite graph, where the vertex set of each color class of Lij corresponds to the color classes in Ti and Tj. A pair of vertices is an edge in Lij iﬀ I is connected to the corresponding pair of color classes. We will use the following fact from [7] for the analysis of the link graph.

B320 B311

Figure 2: The balanced bipartite graphs on 6 vertices, B320 and B311

Fact 17. Let B320 and B311 be as deﬁned in Figure 2. If B is a balanced bipartite graph on 6 vertices with |E(B)| ≥ 5, then at least one of the following must be true.

- • B has a perfect matching.
- • B contains B320 as a subgraph.
- • B is isomorphic to B311.


Claim 18. If there are η |T2| pairs of tripartite graphs (Ti,Tj) such that Lij has a perfect matching or contains a B320, then we can increase the size of T by at least η3n/8 vertices such that all tripartite graphs in the cover are balanced and are of the same size.

We can repeatedly use Claim 18 to increase the size of our cover as long as the condition of

- Claim 18 is satisﬁed. Hence in at most 8η−3 iterations we either get an optimal cover or we have


that there are at most η |T2| pairs of tripartite graphs (Ti,Tj) such that the link graph Lij has at least 5 edges and contains either a perfect matching or B320 as a subgraph. For simplicity we still denote the cover by T and I = V (H) \ V (T ).

Assume that T is not optimal. We show that if we cannot apply Claim 18, then for most of the pairs of tripartite graphs in T2 , the link graph has exactly 5 edges and is isomorphic to B311. Indeed, if there are many (≥

√η-fraction) pairs of tripartite graphs (Ti,Tj) for which |E(Lij)| ≤ 4 then there is another set of at least η-fraction of pairs of tripartite graphs (Ti,Tj) for which |E(Lij)| ≥ 6. To see this let P4 = {(Ti,Tj) ∈ T2 : |E(Lij)| ≤ 4} and P6 = {(Ti,Tj) ∈ T2 : |E(Lij)| ≥ 6}. Note that for any (Ti,Tj) ∈ P4 by deﬁnition d3(I,V (Ti) × V (Tj)) ≤ (4/9 + 10η).

√η |T2| and |P6| < η |T2| then

Now if |P4| ≥

d3 I,

V (T ) 2 ≤

√η ·

4 9

+ 10η + η ·

√η) ·

9 9

+ (1 −

5 9

+ 8η

√η) |T2| pairs of tripartite graphs (Ti,Tj) ∈ T2 , Lij has at least 5 edges. Since we cannot apply Claim 18, for at least (1 − 2√η) |T2| of them the Lij is isomorphic to B311 and |E(Lij)| = 5.

a contradiction to (7). Therefore for at least (1 −

- Claim 19. If there are at least (1 − 2√η) |T2| pairs of tripartite graphs (Ti,Tj) such that Lij is isomorphic to B311, then either


- • we can increase the size of T by at least η4n vertices such that all tripartite graphs in the cover are balanced and are of the same size, or
- • H is α-extremal.


We repeatedly use Claim 19 to increase the size of our cover as long as the condition of Claim 19 is satisﬁed.

Hence proceeding in iterations applying the appropriate claim at each iteration, it is clear that in at most 8η−4 iterations we either get an optimal cover or that H is α-extremal. The optimal cover readily gives us an almost perfect matching.

###### 4.1 Proof of Claim 16

Let T = {T1,T2,...} ⊂ T be the subcover of the at least 2-sided tripartite graphs such |V (T )| ≥ η|V (T )| ≥ η2n. Without loss of generality, say in each Ti ∈ T we have

d3 V1i, I

2 ≥ 2η and d3 V2i, I

2 ≥ 2η.

For each such Ti, we have |V1i| = |V2i| = t ≤ η log(η2n) = ηm and |I| ≥ η2n > η22m2. By Lemma 13 (with parameter η ) we ﬁnd two disjoint balanced complete tripartite graphs (U1i,Ai1,B1i) and (U2i,Ai2,B2i) where U1i and U2i are subsets of V1i and V2i respectively, and Ai1,Ai2,B1i and B2i are disjoint subsets of I (see Figure 3). The size of each color class of these tripartite graphs is η|V1i|/2 (we assume it is an integer). Note that we can ﬁnd larger tripartite graphs but we keep the size of these new tripartite graphs 3η|V1i|/2 only. We remove the vertices of these new tripartite graphs from their respective sets and add the tripartite graphs to our cover. Removing these vertices from V1i and V2i creates an imbalance in the leftover part of Ti (V3i has more vertices). To restore the balance in the leftover of Ti we discard (add to I) some arbitrary |U1i| = |U2i| = η|V1i|/2 vertices from V3i. The new tripartite graphs use at least 2|Ai1| + 2|B1i| = 2η|V1i| vertices from I. Therefore, after discarding the vertices from V3i the net increase in the size of our cover is 3η|V1i|/2, while all the tripartite graphs in T are balanced.

V1i V2i V3i

###### Ti

I

- Figure 3: Shaded triangles represent 2-sided color classes. Solid triangles represent the new complete tripartite graphs. V3i has extra vertices.


We proceed as above for the remaining tripartite graphs in T one by one until we remove at least η|I|/8 ≥ η3n/8 vertices from I. Since each Ti ∈ T is at least 2-sided we can continue as above. Indeed, until we remove η|I|/8 vertices from I, for the remaining tripartite graphs in T

and the remaining part of I the condition of Lemma 13 is still satisﬁed (with parameter η). Since |V (T )| ≥ η|V (T )| ≥ η2n, it is easy to see that with this procedure we increase the size of our cover by at least η3n/8 vertices. Note that the newly made tripartite graphs have color classes of size ηt/2 while the remaining parts of tripartite graphs in T and those in T \ T are bigger. To make all tripartite graphs in the cover of the same size, we split each tripartite graph in the cover, into disjoint balanced complete tripartite graphs, such that each color class of every tripartite graph is of size ηt/2 (we assume divisibility).

###### 4.2 Proof of Claim 18

We ﬁrst ﬁnd a set of disjoint pairs of tripartite graphs such that for each pair the link graph either has a perfect matching or contains a B320. Consider the auxiliary graph where vertices are the tripartite graphs in T and two vertices are connected if for the corresponding tripartite graphs Ti and Tj, Lij has a perfect matching or contains a B320. Since this auxiliary graph has at least η |T2| edges, by Lemma 14 and Lemma 15, we ﬁnd a matching of size η|T |/3 in this graph. Clearly, this matching corresponds to a set of disjoint pairs of tripartite graphs, P ⊂ T2 , such that for the each pair (Ti,Tj) ∈ P, Lij has a perfect matching or contains a B320. The number of vertices in the 2|P| tripartite graphs in P is at least ηn/3 as |V (T )| ≥ n/2. We distinguish the following two cases for each pair in P, to make new tripartite graphs using some vertices from I.

Case 1: Lij has a perfect matching. Without loss of generality assume that the perfect matching in Lij corresponds to the pairs (V1i,V1j), (V2i,V2j) and (V3i,V3j). Note that by construction of Lij, I is connected to (V1i,V1j), (V2i,V2j) and (V3i,V3j). By deﬁnition of connectedness, d3(I,V1i × V2j) ≥ 2η and |V1i| = |V1j| = t ≤ η log(η2n) and |I| ≥ η2n > η22t2, hence the 3-partite 3-graph H(V1i,V1j,I) satisﬁes the conditions of Lemma 12. Applying Lemma 12 (with parameter η) we ﬁnd a complete balanced tripartite graph T1 = (U1i,U1j,I1), such that

η 4

I1 ⊂ I, U1i ⊂ V1i , U1j ⊂ V1j and |I1| = |U1i| = |U1j| =

log t.

Similarly, we ﬁnd such complete balanced tripartite graphs T2 and T3 in H(V2i,V2j,I) and H(V3i,V3j,I)

- respectively (see Figure 4). Clearly we can have that T1,T2 and T3 are disjoint from each other as |I| ≥ η2n .


We remove the vertices in T1,T2 and T3 from their respective sets and add these three new tripartite graphs to our cover. In the remaining parts of Ti and Tj we remove another such set of

###### 3 disjoint tripartite graphs. By deﬁnition of connectedness until we remove at least η2t/2 vertices

from each color class of Ti and Tj we still have d3(I,(V1i × V1j)) > η. Hence by Lemma 12 we continue removing such three tripartite graphs until from each color class of Ti and Tj we remove η2t/2 vertices. Note that the new tripartite graphs use 3η2t/2 vertices from I. Therefore adding these new tripartite graphs to our cover increases the size of the cover by 3ηt2/2 vertices while all tripartite graphs in the cover are still balanced.

Case 2: Lij contains a B320. Again without loss of generality assume that in the B320 the vertices of degree 3 and 2 correspond to the color classes V1i and V2i respectively. Furthermore, we may assume that I is connected to (V1i,V1j), (V1i,V2j), (V2i,V2j) and (V2i,V3j). By deﬁnition of connectedness the 3-partite subhypergraph of H induced by I and any of the above four pairs of color classes satisﬁes the conditions of Lemma 12.

V3j

V3i

#### Ti Tj

- Figure 4: The new tripartite graphs T1, T2 and T3 using vertices from Ti, Tj and I when Lij has a perfect matching. Shaded rectangles represent pairs connected to I. Solid lines represent the new complete tripartite graphs.


Similarly as in the previous case, applying Lemma 12 (with parameter η) we ﬁnd the following four disjoint complete tripartite graphs: (V11i ,V11j ,I1), (V22i ,V32j ,I2), (V13i ,V23j ,I3) and (V24i ,V24j ,I4) such that for 1 ≤ p ≤ 3 and 1 ≤ q ≤ 4, Iq,Vpqi and Vpqj are disjoint subsets of I,Vpi and Vpj

- respectively (see Figure 5). For the sizes of these new tripartite graphs we have


η log t 4 and

|I1| = |I2| = |V11i | = |V11j | = |V22i | = |V32j | =

η log t 8

|I3| = |I4| = |V13i | = |V23j | = |V24i | = |V24j | =

.

In the remaining parts of Ti and Tj we remove another such set of 4 disjoint tripartite graphs. Again by deﬁnition of connectedness and Lemma 12 we can continue this process until we remove η2t/2 vertices each from V1i and V2i. Note that when we remove the vertices of these new tripartite graphs from their respective color classes in Ti and Tj, the remaining part of Tj is still balanced while it creates an imbalance in the remaining part of Ti, as V3i has η2t/2 more vertices than the other two color classes To restore the balance we discard (add to I) an arbitrary subset of vertices in V3i (of size η2t/2). These new tripartite graphs use at least η2t vertices from I. Therefore, after discarding the vertices from V3i the net increase in the number of vertices in the cover is η2t/2.

We proceed in similar manner for all pairs in P one by one until we remove at least η|I|/8 ≥ η3n/8 vertices from I. Applying the appropriate procedure in Case 1 or Case 2 we increase the size

V3j

V3i

#### Ti Tj

- Figure 5: The new tripartite graphs using vertices from Ti, Tj and I when Lij contains a B320. Shaded rectangles represent pairs connected to I. Solid lines represent the new complete tripartite graphs. V3i has extra vertices.


of the cover by η3n/8 vertices (as the size of P is at least ηn/3 and for every pair the increase is η2t/2) while keeping all the tripartite graphs in the cover balanced. Note that even after removing η|I|/8 vertices from I for the remaining pairs (Ti,Tj) ∈ P, the conditions of Lemma 12 are satisﬁed (with parameter η).

Again as above we make all tripartite graphs in the cover of the same size, by arbitrarily splitting each larger tripartite graph into disjoint tripartite graphs with color classes of size η log t/4.

###### 4.3 Proof of Claim 19

Similarly as above, ﬁrst consider the auxiliary graph where vertices are the tripartite graphs in T and two vertices are connected if for the corresponding tripartite graphs Ti and Tj, Lij is isomorphic to B311. This auxiliary graph has T vertices and at least (1 − 2√η) |T2| edges. By Lemma 14 and Lemma 15, in this graph we can ﬁnd a matching of size (1−2√η)|T |/2. This matching corresponds to a set of disjoint pairs of tripartite graphs, Pg ⊂ T2 , such that for each pair (Ti,Tj) ∈ Pg, Lij is isomorphic to B311. Let the set of tripartite graphs in Pg be Tg and let V (Pg) be the set of vertices in these tripartite graphs, we have

|V (Pg)| ≥ (1 − 2√η)|V (T )|. (8)

Without loss of generality assume that for each (Ti,Tj) ∈ Pg, the vertices of degree 3 in the B311 in Lij correspond to the color classes V1i and V1j. Thus by deﬁnition of connectedness for each (Ti,Tj) ∈ Pg, (see Figure 6)

for 1 ≤ q ≤ 3 d3 I,(V1i × Vqj) ≥ 2η and d3 I,(Vqi × V1j) ≥ 2η. (9)

V1i (V2 and V3 are similarly deﬁned). We have

Let V1 =

Ti∈Tg

V2 ∪ V3 2

d3 I,

< 2η. (10)

V1 V2 V3

| |
|---|


# ......

- Figure 6: The pairs of tripartite graphs in Pg. All Lij’s are isomorphic to B311. Shaded rectangles represent pairs connected to I.

For each (Ti,Tj) ∈ Pg the conditions of Lemma 12 are satisﬁed for H(V1i,V2j,I), H(V1i,V3j,I), H(V2i,V1j,I) and H(V3i,V1j,I). We ﬁnd a disjoint complete tripartite graphs in each of these four 3-partite 3-graphs (see Figure 7). The size of each color class in the new tripartite graphs is

η log t 4

. Again we continue removing such sets of four tripartite graphs until we remove η3t vertices each from V1i and V1j. By construction, these new tripartite graphs remove η3t/2 vertices each from V2i, V3i, V2j and V3j.

- V1i
- V2i
- V3i


- V1j
- V2j
- V3j


I

Ti Tj

- Figure 7: The new tripartite graphs using vertices from Ti, Tj and I when Lij is isomorphic to B311. Shaded rectangles represent pairs connected to I. Solid lines represent the new complete tripartite graphs.


###### These new tripartite graphs use 2η3t vertices from I. Removing these new tripartite graphs creates an imbalance among the color classes of the remaining parts of Ti and Tj, to restore the

balance we will have to discard η3t/2 vertices from each color class of Ti and Tj except V1i and V1j. This leaves us with no net gain in the size of the cover. Therefore we will not discard any vertices from these color classes at this time and say that these color classes have η3t/2 extra vertices.

We proceed in similar manner for each pair in Pg. Since in total we will use |Tg|·η3t ≤ η3n ≤ η|I| vertices from I for the remaining pairs of tripartite graphs in Pg the conditions of Lemma 12 (with parameter η) are satisﬁed. So we can continue to make new tripartite graphs.

Let V1g ⊂ V1,V2g ⊂ V2,V3g ⊂ V3 be the union of the corresponding color classes of remaining parts of tripartite graphs in Tg. Since the number of vertices used in the newly made tripartite graphs above is at most η3n, by (8) we have

|V2g| = |V3g| ≥ (1 − 3√η)|V (T )|/3. (11)

Next we show that if at least one of the following density conditions is true then we can increase the size of our cover:

√η, (12)

d3 (V2g ∪ V3g) ≥

d3 V2g ∪ V3g, I

√η. (13)

2 ≥

√η. We will show that in H|V2g∪V3g there exist disjoint balanced complete tripartite 3-graphs of size η3t/4 (half the number of extra vertices in a color class) covering at least η4n vertices. Furthermore, we can ﬁnd such tripartite graphs in H|V2g∪V3g such that from no color class we use more than the number of extra vertices in that color class.

Assume that d3(V2g ∪ V3g) ≥

To see this, call a color class ‘full’ if these new tripartite graphs use at least η3t/4 vertices. We remove all vertices of each full color class and ﬁnd tripartite graphs of size η3t/4 in the remaining vertices. Let k be the number of full color classes at a given time and suppose that the total number of vertices covered by the new tripartite graphs is at most η4n. Then, k·η3t/4 < η4n which implies that tk < 4ηn i.e. the total number of vertices in the full color classes is at most 4ηn. Let H be

the remaining part of H|V2g∪V3g (after removing all vertices in every full color class). By the above observation V (H ) ≥ (1 − 3√η)|V (T )|/3 − 4ηn − η4n and d3(H ) ≥

√η/2. Hence by Lemma 9 we can continue to ﬁnd complete tripartite graphs of size η3t/4 in H . Note that we do not use more than the number of extra vertices from any color classes.

√η − 6(η + η4) ≥

We remove some of these new tripartite graphs so that the total number of vertices covered by them is at least η4n. Now adding these new tripartite graphs to our cover increases the size of our cover by at least η4n vertices, as we did not discard vertices from V2g ∪ V3g for rebalancing. Instead the extra vertices are part of these new tripartite graphs. Now in the remaining parts of each Ti ∈ Tg we arbitrarily remove some extra vertices to restore the balance in the tripartite graphs

and as above make all tripartite graphs of the same size.

√η, then since both |I| and |V2g ∪ V3g| are at least η2n, by Lemma 9 we ﬁnd disjoint complete tripartite graphs with one color class in V2g ∪ V3g and two color classes in I covering at least η4n vertices. Again as above we make these tripartite graphs so as to not use more than the number of extra vertices in any color class. Adding these tripartite graphs increases the size of our cover by at least η4n vertices.

On the other hand if d3(V2g ∪ V3g, I2 ) ≥

In case none of the above density conditions hold then by (10), (12), (13) and the fact that

d3(I) < η, we get d3(V1g ∪ V2g ∪ I) < 10√η < α. By (11) we have |V1g ∪ V2g ∪ I| ≥ (2/3 − α)n. Hence H is α-extremal. This concludes the proof of Claim 19.

##### 5 Proof of Theorem 8

1 α

Let α be given and let n ∈ 3Z

. Our hypergraph H is α-extremal i.e. there exists a B ⊂ V (H) such that

- • |B| ≥ (32 − α)n

- • d3(B) < α.


Let A = V (H) \ B, by shifting some vertices between A and B we can have that A = n/3 and

- B = 2n/3 (we keep the notation A and B). It is easy to see that we still have d3(B) < 6α (14)


Since we have

δ1(H) ≥

n − 1 2 −

2n/3 2

+ 1 =

n − 1 2 −

|B| 2

+ 1 (15)

together with (14) this implies that almost all 3-sets of V (H) are edges of H except 3-sets of B. Thus roughly speaking almost every vertex b ∈ B makes edges with almost all pairs of vertices in A2 and with almost all pairs of vertices in B \ {b} × A and vice versa. Therefore, we will basically match every vertex in A with a distinct pair of vertices in B2 to get the perfect matching. However, there may be a few vertices making edges with diﬀerent pairs of vertices than the typical ones. Hence we will ﬁrst match those few vertices and then we will use a K¨nig-Hall type argument to match every remaining vertex in A with a distinct pair of remaining vertices in B.

- Proof of Theorem 8. We ﬁrst identify vertices in A and B that do not satisfy the typical degree conditions as follows.


###### Deﬁnition 20.

- • XA (Exceptional vertices in A) := {a ∈ A | deg3 a,

B 2

< 1 −

√α |B|

2 }

- • XB (Exceptional vertices in B) := {b ∈ B | deg3(b,(B × A)) < (1 −

√α)|A|(|B| − 1)}

- • SA (Strongly Exceptional vertices in A) := {a ∈ A | deg3 a,

B 2

< α1/3 |B| 2 }

- • SB (Strongly Exceptional vertices in B) := {b ∈ B | deg3(b,(B × A)) < α1/3|A|(|B| − 1)}


We will show that there are few vertices in XA and XB and very few vertices in SA and SB.

- Claim 21. We have the following bounds on the sizes of the sets deﬁned above.


- (i) |XA| ≤ 18√α|A|.

- (ii) |XB| ≤ 18√α|B|.

- (iii) |SB| ≤ 40α|B|.
- (iv) |SA| ≤ 40α|A|.


Proof. We only prove the bounds on |XB| and |SA| (the others are similar). Assume that |XB| ≥ 18√α|B|. By (15) and the deﬁnition of XB, for any vertex b ∈ XB, deg3 b, B2 ≥

√α|A|(|B| − 1)/2. Therefore for the number of edges inside B we have

√α|A|(|B| − 1)/2 ≥ 9√α|B| ·

√α|A|(|B| − 1) ≥ 9α|B|(|B| − 1)|A| ≥ 27α |B|

3|E(B)| ≥ |XB| ·

3 where the last inequality uses |A| = |B|/2. This implies that d3(B) ≥ 9α, a contradiction to (14). To see the bound on |SA|, note that by (15), if there is a set of k vertices {a1,a2,...,ak} in

- A and a pair {b1,b2} of vertices in B such that for 1 ≤ i ≤ k, {ai,b1,b2} ∈/ E(H), then to make up the minimum degree of b1, there are at least k + 1 edges in E(B) containing b1. Similarly (not necessarily distinct) k + 1 edges exist in B to make up the minimum degrees of b2. This, together


with the fact that every a ∈ SA does not make edges with at least (1 − α1/3) |B2| pairs of vertices in B, implies that

3|E(B)| > |SA|(1 − α1/3 |B| 2

. If |SA| > 40α|A|, then

|B| 2 ≥ 40α |B| 3 where the last inequality holds when α is a small constant and is a contradiction to (14).

3|E(B)| > 40α|A|(1 − α1/3) |B| 2

= 40α(1 − α1/3)|B| 2

- Claim 22. There exists a matching M in H such that M covers all the strongly exceptional vertices and if A = A \ V (M), B = B \ V (M) and n = n − |V (M)|, then |B | = 2|A | = 2n /3.


Proof. We ﬁrst show that if both SB and SA are non empty, then we can reduce the sizes of both. To see this assume b ∈ SB and a ∈ SA. By deﬁnition, deg3(a, B2 ) < α1/3 |B2| and deg3(b,(B × A)) < α1/3|A|(|B| − 1). Hence by (15), deg3(a,A × B) ≥ (1 − 2α1/3)(|A| − 1)|B| and deg3(b, B2 ) ≥ (1 − 2α1/3) |B2| . We can exchange a with b and reduce the size of both SB and SA,

- as both a and b are not strongly exceptional in their new sets. Applying the above procedure we


take the sets A and B such that |SA| + |SB| is as small as possible (and one of the sets SA and SB is empty).

First assume that SB = ∅. As observed above by the minimum degree condition and deﬁnition of SB, for every vertex b ∈ SB, deg3(b, B2 ) ≥ (1 − 2α1/3) |B2| . Since |SB| is very small and every vertex in SB makes many edges insides B we can greedily ﬁnd |SB| vertex disjoint edges in H|B each containing exactly one vertex of SB. Indeed after removing at most |SB|−1 disjoint edges from H|B the remaining vertex in SB still makes edges with at least (1−2α1/3) |B2| − |S2B| −|B|×3|SB| > 1 pairs of the remaining vertices. Hence we can greedily match each vertex in SB in a matching M in H|B. To keep the ratio of the sizes of the remaining parts of A and B intact, we add to M, |SB| other vertex disjoint edges such that each edge has a vertex in B \ XB and the two other vertices are in A. We can clearly ﬁnd such edges because by (15) and (14) almost every vertex in

- B \ XB makes edges with at least (1 − 2√α) |A2| pairs of vertices in A (as otherwise d3(B) will be very large). We remove the vertices of M from A and B and by construction n = n − 6|SB|,


- |A | = |A| − 2|SB| and |B | = |B| − 4|SB|, hence |B | = 2|A | = 2n /3.


In case SA = ∅ (and SB = ∅), we will ﬁnd a matching such that each edge contain a vertex in SA. Note that in this case for any vertex b ∈ B we have deg3(b, B2 ) < α1/3 |B2| . Indeed, if there is a vertex b ∈ B such that deg3(b, B2 ) ≥ α1/3 |B2| then we can replace b with any vertex a ∈ SA to reduce the size of SA (as the vertex b is not strongly exceptional in A and a is not strongly exceptional in the set B). We say that vertices in SA are exchangeable with vertices in B and consider the whole set SA ∪ B. By (15) for any vertex v ∈ SA ∪ B

SA ∪ B 2 ≥

|SA ∪ B| − 1 2 −

|B| 2

+ 1 = |SA| − 1 2

+ (|SA| − 1)|B| + 1.

deg3 v,

We will prove by induction on |SA| that we can ﬁnd a matching M in H|SA∪B of size |SA|. Note that this also follows from a result of Bollob´s, Daykin and Erd¨s [3]. If |SA| = 1 then clearly we get an edge in H|SA∪B and we are done. Now assume that |SA| > 1 and that the assertion is true for smaller values of |SA|. Let v be a maximum degree vertex in H|SA∪B and let H = H|SA∪B\{v}.

For any vertex u ∈ V (H ) the number of pairs of vertices in SA ∪ B, containing v but not u, is

- at most |SA ∪ B| − 2. Therefore we get that


|SA| − 1 2

+ (|SA| − 1)|B| + 1 − (|SA| + |B| − 2)

δ1(H ) ≥

= |SA| − 2 2

+ (|SA| − 2)|B| + 1

where the last equality follows by a simple calculation. Hence by induction hypothesis there is a matching in H of size at least |SA|−1. Let M1 be a maximum matching in H , if |M1| ≥ |SA| then we are done so assume that |M1| = |SA| − 1 and every edge in H intersects V (M1). This gives us a lower bound on the maximum degree of a vertex in V (M1) and since v is the overall maximum degree vertex we get

|E(H )| |V (M1)|

|V (H )| · δ1(H ) 3|V (M1)|

deg3(v) ≥

≥

(|SA| + |B| − 1) |SA2|−2 + (|SA| − 2)|B| + 1 9(|SA| − 1)

≥

(|SA| + |B| − 1) 27(|SA| − 1)2 9(|SA| − 1) > 3(|SA| − 1)(|SA| + |B| − 2)

>

where the last inequality uses the fact that |B| is much larger compared to |SA|. Since the last quantity is larger then the number of pairs that use at least one vertex from V (M1), there is a pair of vertices in SA ∪ B \ V (M1) that makes an edge with v. Adding this edge to M1 we get a matching M which is the required matching. Using the fact that vertices in SA are exchangeable with vertices in B, we get n = n − 3|SA|, |A | = |A| − |SA| and |B | = |B| − 2|SA|, hence we get

- |B | = 2|A | = 2n /3.


Having dealt with the strongly exceptional vertices, the vertices of XA and XB in A and B

can be eliminated using the fact that their sizes are much smaller than the crossing degrees of vertices in those sets. We have |XA| ≤ 18√α|A| while for any vertex a ∈ XA, we have that deg3(a, B 2 ) ≥ α1/3 |B2 | /2 (because a ∈/ SA). For each a ∈ XA we remove a disjoint edge that contains a and two vertices from B . This can be done greedily as after covering |XA| − 1 vertices of XA, the total number of edges removed is at most 50√α |B2 | . So there are pairs of vertices in the remaining part of B making edges with the next vertex of XA. Similarly for each b ∈ XB we

remove an edge that contains b and uses one vertex from A and the other vertex is from B distinct from b. Clearly we can ﬁnd such disjoint edges by a simple greedy procedure. Hence we removed a partial matching that covers all vertices in the exceptional sets.

Denote the leftover sets of A and B by A and B respectively. By construction |B | = 2|A |). We will ﬁnd |A | disjoint edges each containing one vertex from A and two vertices from B . Note that for every vertex a ∈ A we have deg3(a, B 2 ) ≥ (1 − 2α1/3) |B2 | (as a ∈/ XA). We say that a pair (b1,b2) of vertices in B is good if (bi,bj,ak) ∈ E(H) for at least (1 − 40α1/4)|A | vertices ak

- in A . Any vertex bi ∈ B makes a good pair with at least (1 − 40α1/4)|B | other vertices in B (again this is so because bi ∈/ XB).

We randomly select a set P1 of 100α1/4|B | vertex disjoint good pairs of vertices in B . By the above observation with high probability every vertex a ∈ A make edges in H with at least 3|P1|/4 pairs in P1 and every pair in P1 makes an edge with at least 3|A |/4 vertices in A . In B \ V (P1) still every vertex makes good pairs with almost all other vertices. We pair up each vertex of B \ V (P1) with a distinct vertex in B \ V (P1) such that they make a good pair. This can be done by considering a 2-graph with vertex set B \V (P1) and all the good pairs as its edges. A simple application of Dirac’s theorem on this 2-graph gives such a perfect matching of vertices

- in B \ V (P1). Let the set of these pairs be P2. Now construct an auxiliary bipartite graph G(L,R), such that L = A and vertices in R


correspond to the pairs in P1 and P2. A vertex in ak ∈ L is connected to a vertex y ∈ R if the pair corresponding to y (say bi,bj) is such that (bi,bj,ak) ∈ E(H). We will show that G(L,R) satisﬁes the K¨nig-Hall criteria. Considering the sizes of A and P1 it is easy to see that for every set Q ⊂ R if |Q| ≤ (1 − 40α1/4)|A | then |N(Q)| ≥ |Q|. When |Q| > (1 − 40α1/4)|A | (using |B | = 2|A |) any such Q must have at least 6|P1|/10 vertices corresponding to pairs in P1, hence with high probability |N(Q)| = |L| ≥ |Q|. Therefore there is a perfect matching of R into L. This perfect matching in G readily gives us a matching in H covering all vertices in A and B , which together with the edges we already removed (covering exceptional and strongly exceptional vertices) is a perfect matching in H.

##### References

- [1] R. Aharoni, A. Georgakopoulos, and P. Spru¨ssel, Perfect matchings in r-partite r-graphs, Eur. J. Comb. 30(1) (2009), pp. 39–42.
- [2] B. Bollob´s, Extremal Graph Theory, Academic Press, London (1978).
- [3] B. Bollob´s, D. Daykin and P. Erd¨s, Sets of Independent edges of a hypergraph, Qurart. J. Math. Oxford, 21 (1976), pp. 25-32.


- [4] D. Daykin and R. H¨ggkvist, Degrees giving independent edges in a hypergraph, Bull. Austral. Math. Soc., 23(1) (1981), pp. 103109.
- [5] G.A. Dirac, Some theorems on abstract graphs, Proc. Lond. Math. Soc., 2 (1952), pp. 69-81.
- [6] P. Erd¨s, On extremal problems of graphs and generalized graphs, Israel J. Math., 2 (1964), pp. 183–190.
- [7] H. H`n, Y. Person and M. Schacht, On perfect matchings in uniform hypergraphs with large minimum vertex degree, SIAM J. Discret. Math., 23(2) (2009), pp. 732–748.
- [8] I. Khan, Perfect matchings in 4-uniform hypergraphs, Submitted.
- [9] D. Ku¨hn and D. Osthus, Matchings in hypergraphs of large minimum degree, J. Graph Theory, 51(4) (2006), pp. 269–280.
- [10] D. Ku¨hn, D. Osthus and A. Treglown, Matchings in 3-uniform hypergraphs, Submitted .
- [11] A. Lo and K. Markstr¨m, Perfect matchings in 3-partite 3-uniform hypergraphs, Preprint.
- [12] K. Markstr¨m and A. Rucin´ski, Perfect matchings (and Hamilton cycles) in hypergraphs with large degrees, Eur. J. Comb., 32(5) (2011), pp. 677–687.
- [13] O. Pikhurko, Perfect matchings and K43-tilings in hypergraphs of large codegree, Graphs Combin., 24(4) (2008), pp. 391-404.
- [14] V. R¨dl and A. Rucin´ski, Dirac-type questions for hypergraphs – a survey (or more problems for Endre to solve), An Irregular Mind (Szemer´edi is 70), Bolyai Soc. Math. Studies, 21 (2010).
- [15] V. R¨dl, A. Rucin´ski, M. Schacht and E. Szemer´edi, A note on perfect matchings in uniform hypergraphs with large minimum collective degree, Commentationes Mathematicae Universitatis Carolinae, 49(4) (2008), pp. 633-636.
- [16] V. R¨dl, A. Rucin´ski and E. Szemere´di, A Dirac-type theorem for 3-uniform hypergraphs, Comb. Probab. Comput., 15 (2006), pp. 229–251.
- [17] V. R¨dl, A. Ruci´nski and E. Szemer´edi, Perfect matchings in uniform hypergraphs with large minimum degree, Europ. J. Combin., 27 (2006), pp. 1333-1349.
- [18] V. R¨dl, A. Rucin´ski and E. Szemer´edi, An approximate Dirac-type theorem for k-uniform hypergraphs, Combinatorica, 28(2) (2008), pp. 229-260.


###### [19] V. R¨dl, A. Ruci´nski and E. Szemer´edi, Perfect matchings in large uniform hypergraphs with large minimum collective degree, J. Comb. Theory Ser. A, 116(3) (2009), pp. 613–636.

