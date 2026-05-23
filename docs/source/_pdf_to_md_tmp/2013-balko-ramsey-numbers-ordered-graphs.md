# arXiv:1310.7208v5[math.CO]28Nov2019

## Ramsey numbers of ordered graphs∗†

##### Martin Balko1 Josef Cibulka2 Karel Kr´al2 Jan Kynˇcl1,3,4

1 Department of Applied Mathematics and Institute for Theoretical Computer Science, Charles University, Faculty of Mathematics and Physics, Malostranske´ na´m. 25, 118 00 Praha 1, Czech Republic; balko@kam.mff.cuni.cz, cibulka@kam.mff.cuni.cz, kyncl@kam.mff.cuni.cz

2 Department of Applied Mathematics, Charles University, Faculty of Mathematics and Physics, Malostranske´ na´m. 25, 118 00 Praha 1, Czech Republic; kralka@kam.mff.cuni.cz

3 Alfre´d R´enyi Institute of Mathematics, Rea´ltanoda u. 13-15, Budapest 1053, Hungary 4 Ecole´ Polytechnique Fe´de´rale de Lausanne, Chair of Combinatorial Geometry, EPFL-SB-MATHGEOM-DCG, Station 8, CH-1015 Lausanne, Switzerland

###### Abstract

An ordered graph is a pair G = (G,≺) where G is a graph and ≺ is a total ordering of its vertices. The ordered Ramsey number R(G) is the minimum number N such that every ordered complete graph with N vertices and with edges colored by two colors contains a monochromatic copy of G.

In contrast with the case of unordered graphs, we show that there are arbitrarily large ordered matchings Mn on n vertices for which R(Mn) is superpolynomial in n. This implies that ordered Ramsey numbers of the same graph can grow superpolynomially in the size of the graph in one ordering and remain linear in another ordering.

We also prove that the ordered Ramsey number R(G) is polynomial in the number of vertices of G if the bandwidth of G is constant or if G is an ordered graph of constant degeneracy and constant interval chromatic number. The ﬁrst result gives a positive answer to a question of Conlon, Fox, Lee, and Sudakov.

For a few special classes of ordered paths, stars or matchings, we give asymptotically tight bounds on their ordered Ramsey numbers. For so-called monotone cycles we compute their ordered Ramsey numbers exactly. This result implies exact formulas for geometric Ramsey numbers of cycles introduced by K´rolyi, Pach, T´th, and Valtr.

∗An extended abstract of this paper appeared in the proceedings of Eurocomb 2015 [2]. †The ﬁrst and the fourth author were supported by the grants SVV-2013-267313 (Discrete Models and Algorithms), GAUK 1262213 of the Grant Agency of Charles University and by the project CE-ITI (GACRˇ P202/12/G061) of the Czech Science Foundation. The third author acknowledges the support from the European Research Council under the European Union’s Seventh Framework Programme (FP/2007-2013) / ERC Grant Agreement n. 616787. The fourth author was also supported by ERC Advanced Research Grant no 267165 (DISCONV) and by Swiss National Science Foundation Grants 200021-137574 and 200020-14453.

### 1 Introduction

Ramsey’s theorem [35] states that for every given graph G, every suﬃciently large complete graph with edges colored by a constant number of colors contains a monochromatic copy of G. We study the analogue of Ramsey’s theorem for graphs with ordered vertex sets. The concept of ordered graphs appeared earlier in the literature [29, 30, 32, 34], but we are not aware of any Ramsey-type results for such graphs except for the case of monotone paths and hyperpaths [8, 18, 22, 32, 33].

The main goal of this paper is to understand the eﬀects of diﬀerent vertex orderings on the ordered Ramsey number of a given graph, and to compare the ordered and unordered Ramsey numbers. We state our results after introducing the necessary notation. Then we present a few examples that provide the motivation to study ordered Ramsey numbers.

During the preparation of this paper, we learned that Conlon, Fox, Lee, and Sudakov [15] have independently obtained results that overlap with ours. Ramsey numbers of ordered graphs are also discussed by Conlon, Fox, and Sudakov in their survey of recent developments in Ramsey theory [17].

Throughout the paper, we omit the ceiling and ﬂoor signs whenever they are not crucial. Unless indicated otherwise, all logarithms in this paper are base 2.

Graphs. We consider only ﬁnite graphs with no multiple edges and no loops. A coloring of a graph G = (V,E) is a mapping f : E → C where C is a ﬁnite set of colors. Unless speciﬁed otherwise, we assume that C = [c] = {1,2,...,c}. A coloring with c colors is called a c-coloring. In a 2-coloring of a graph G with colors red and blue, we call a vertex u of G a red neighbor (a blue neighbor) of a vertex v of G if the edge uv is colored red (blue, respectively).

Ramsey’s theorem states that for given positive integers c and n, there is an integer N such that every c-coloring of KN contains a monochromatic copy of Kn. The minimum such N is called the Ramsey number and we denote it by R(Kn;c). Classical results of Erdo˝s [19] and Erd˝s and Szekeres [20] give the exponential bounds

2n/2 ≤ R(Kn;2) ≤ 22n. (1)

Despite many improvements during the last sixty years (see [14] for example), the constant factors in the exponents have remained the same.

Since every graph on n vertices is contained in Kn, we can consider the following generalization of Ramsey numbers. Let c be a positive integer and let G1,...,Gc be graphs. Ramsey’s theorem then implies that there exists a smallest number R(G1,...,Gc) such that every c-coloring of a complete graph with at least R(G1,...,Gc) vertices contains a monochromatic copy of Gi in color i for some i ∈ [c]. The case when all the graphs G1,...,Gc are isomorphic to G is called the diagonal case and we just write R(G;c) instead of R(G1,...,Gc). We also abbreviate R(G;2) as R(G).

We note that the deﬁnitions above can be generalized to hypergraphs of uniformity k larger than 2. In particular, for a k-uniform hypergraph H, it is known that its Ramsey number Rk(H) is ﬁnite.

Ordered graphs. An ordered graph G is a pair (G,≺) where G is a graph and ≺ is a total ordering of its vertex set. The ordering ≺ is called a vertex ordering of G. Many notions related to graphs, such as vertex degrees or a coloring, can be deﬁned analogously for ordered graphs.

For an ordered graph G = (G,≺) and its vertices x,y, we say that x is a left neighbor of y and that y is a right neighbor of x if x and y belong to a common edge and x ≺ y. We say that two ordered graphs (G1,≺1) and (G2,≺2) are isomorphic if G1 and G2 are isomorphic via a one-to-one correspondence g: V (G1) → V (G2) that also preserves the orderings; that is, for every x,y ∈ V (G1), x ≺1 y ⇔ g(x) ≺2 g(y). An ordered graph H = (H,≺1) is an ordered subgraph of G = (G,≺2), written H ⊆ G, if H is a subgraph of G and ≺1 is a suborder of ≺2.

We now introduce Ramsey numbers of ordered graphs, called ordered Ramsey numbers. For given ordered graphs G1,...,Gc, we denote by R(G1,...,Gc) the smallest number N such that every c-coloring of KN contains, for some i, a monochromatic copy of Gi in color i as an ordered subgraph. If all Gi are isomorphic to G, we write the ordered Ramsey number as R(G;c). We abbreviate R(G;2) as R(G). If a coloring f of an ordered graph G contains no monochromatic copy of H, we say that f avoids H.

Up to isomorphism, there is only one ordered complete graph on n vertices, which we denote by Kn. Hence, for arbitrary positive integers c,r1,...,rc we have R(Kr1,...,Krc) = R(Kr1,...,Krc). Since every ordered graph on r vertices is an ordered subgraph of Kr, we have R(G1,...,Gc) ≤ R(Kr1,...,Krc) where ri is the number of vertices of Gi. We have thus proved the following fact.

Observation 1. Let c be an arbitrary positive integer and let G1 = (G1,≺1),...,Gc = (Gc,≺c) be an arbitrary collection of ordered graphs. Then we have

R(G1,...,Gc) ≤ R(G1,...,Gc) ≤ R K|V (G1)|,...,K|V (Gc)| .

To study the asymptotic growth of ordered Ramsey numbers, we introduce ordering schemes for some classes of graphs. An ordering scheme is a particular rule for ordering the vertices of the graphs consistently in the whole class. For example, a monotone path (Pn, mon) is an ordered graph with vertices v1 mon ··· mon vn and n − 1 edges, each consisting of two consecutive vertices. Throughout the paper we use the symbol instead of ≺ to emphasize the fact that the vertex ordering follows some ordering scheme.

For an ordered graph (G,≺), we say that a vertex v of G is to the left (right) of a subset U of vertices of G if v precedes (is preceded by, respectively) every vertex of U in ≺. More generally, for two subsets U and W of vertices of G, we say that U is to the left of W and W is to the right of U if every vertex of U precedes every vertex of W in ≺. We say that a subset I of vertices of G is an interval if for every pair of vertices u and v of I such that u ≺ v, every vertex w of G satisfying u ≺ w ≺ v is contained in I.

Again, all the deﬁnitions, as well as Observation 1, can be extended to k-uniform hyper-

graphs with k > 2. In particular, we know that the ordered Ramsey number Rk(H) of an arbitrary ordered k-uniform hypergraph H is ﬁnite.

#### 1.1 Our results

We are interested in the eﬀects of vertex orderings on the ordered Ramsey numbers of various classes of graphs. The Ramsey number of a graph and the ordered Ramsey number of its ordering can be asymptotically diﬀerent: for example, Proposition 10 implies that R((Pn, mon)) is quadratic while R(Pn) is linear [24].

The gap is much wider for hypergraphs. Let th denote the tower function of height h deﬁned by t1(x) = x and th(x) = 2th−1(x). It is known that for positive integers ∆ and k, there exists a constant C(∆,k) such that if H is a k-uniform hypergraph with n vertices and

a) b)

Figure 1: a) The monotone cycle (C6, mon). b) The ordered complete bipartite graph K4,3.

maximum degree ∆, then Rk(H) ≤ C(∆,k) · n [16]. On the other hand, Moshkovitz and Shapira [33] showed that for every k ≥ 3 we have Rk((Pnk, mon)) = tk−1(2n − o(n)), where (Pnk, mon) is a k-uniform tight monotone hyperpath on n vertices, a natural generalization of monotone paths to k-uniform hypergraphs.

In Section 2, we derive lower and upper bounds on ordered Ramsey numbers of a few basic classes of ordered graphs: stars, paths and cycles. First, in Subsection 2.1 we show that ordered Ramsey numbers of all ordered stars are linear with respect to the number of vertices and at most exponential with respect to the number of colors.

Theorem 2. For all integers c ≥ 2, n1,...,nc ≥ 3, and for every collection of ordered stars S1,...,Sc where ni is the number of vertices of Si, we have

c

c

R(S1,...,Sc) ≤ 2c + 2c+1 ·

(ni − 3) < 2c+1 ·

ni.

i=1

i=1

For certain ordered stars we also provide an almost matching lower bound. In Subsection 2.2, we show an ordering (Pn, alt) of the path Pn whose ordered Ramsey number is linear in n. Proposition 3. For every integer n > 2, we have

5 n/2 − 4 ≤ R((Pn, alt)) ≤ 2n − 3 + 2n2 − 8n + 11.

In Subsection 2.3 we study ordered cycles. First, we compute Ramsey numbers for all possible orderings of C4 (Proposition 17). Then we derive an exact formula for ordered Ramsey numbers of monotone cycles. A monotone cycle (Cn, mon) on n vertices consists of a monotone path v1 mon ··· mon vn and the edge v1vn; see part a) of Figure 1.

- Theorem 4. For all integers r ≥ 2 and s ≥ 2 we have R((Cr, mon),(Cs, mon)) = 2rs − 3r − 3s + 6.

As a consequence, we obtain tight bounds for geometric and convex geometric Ramsey numbers of cycles introduced by K´rolyi et al. [27, 28]; see Corollary 20.

Using a standard probabilistic argument, one can show that there is a constant c > 0 such that the Ramsey number R(G) of every graph G with n vertices and n1+ε edges is at least 2cnε. On the other hand, it is well-known that if G is an n-vertex graph of bounded maximum degree, then R(G) is linear in n [11].

In a sharp contrast to the latter fact, we construct ordered matchings whose ordered Ramsey numbers grow superpolynomially.

- Theorem 5. There are arbitrarily large ordered matchings M on n vertices such that


log n

R(M) ≥ n

5loglogn.

###### Independently, Conlon et al. [15] showed that a random ordered matching M on n vertices asymptotically almost surely satisﬁes R(M) ≥ n

log n

20loglogn.

In Section 3 we give polynomial upper bounds on ordered Ramsey numbers for two classes of sparse ordered graphs. The ﬁrst class consists of ordered graphs that admit the following decomposition.

For given positive integers k and q ≥ 2, we say that an ordered graph G = (G,≺) is (k,q)decomposable if G has at most k vertices or if it admits the following recursive decomposition: there is a nonempty interval I ⊆ V (G) with at most k vertices such that the interval IL of vertices of G that are to the left of I and the interval IR of vertices of G that are to the right of I satisfy

- 1) |IL|,|IR| ≤ q−q1 · |V (G)|,

- 2) there is no edge between IL and IR, and
- 3) the induced ordered subgraphs (G[IL],≺ IL) and (G[IR],≺ IR) are (k,q)-decomposable.


- Theorem 6. Let k and q ≥ 2 be ﬁxed positive integers. There is a constant C k such that every (k,q)-decomposable ordered graph G on n vertices satisﬁes


R(G) ≤ C k · n128k(q−1).

The constant C k depends on k and the proof of Theorem 6 gives a bound C k ≤ 2O(klogk). We say that the length of an edge uv in an ordered graph (G,≺) is |i − j| if u is the ith

vertex and v is the jth vertex of G in the ordering ≺. The bandwidth of G is the length of the longest edge in G. Since every ordered graph with bandwidth k is (k,2)-decomposable, Theorem 6 implies the following.

Corollary 7. For every ﬁxed positive integer k, there is a constant C k such that every n-vertex ordered graph G with bandwidth k satisﬁes

R(G) ≤ C k · n128k.

A graph G is k-degenerate if there is an ordering v1,...,vn of its vertices such that every vertex vi has at most k neighbors vj in G with j < i. The degeneracy of G is the smallest k such that G is k-degenerate. The degeneracy of an ordered graph G = (G,≺) is the degeneracy of the underlying graph G.

We give a polynomial upper bound for ordered Ramsey numbers of ordered graphs with constant degeneracy and constant interval chromatic number. For an ordered graph G, the interval chromatic number of G is the minimum number of intervals the vertex set of G can be partitioned into such that there is no edge between vertices of the same interval.

- Theorem 8. Every ordered k-degenerate graph G with n vertices and interval chromatic number p satisﬁes


R(G) ≤ n(1+2/k)(k+1) logp −2/k.

We obtain Theorem 8 in Subsection 3.2 as a consequence of Theorem 26, which is a stronger, asymmetric statement.

Finally, we consider the situation when the given ordered graph G is ﬁxed and we study the asymptotics of R(G;c) as a function of the number c of colors. We show that the following

dichotomy applies: R(G;c) is either polynomial in c or exponential in c for every ordered graph G. We use n · Kn,n to denote the ordered graph consisting of n disjoint consecutive copies of Kn,n.

- Theorem 9. Every ordered graph G on n vertices satisﬁes one of the following conditions.


- 1. We have G ⊆ n · Kn,n and R(G;c) ≤ (2cn)n+1.

- 2. One of the ordered graphs from Figure 12 is an ordered subgraph of G and R(G;c) > 2c.


The work by Conlon et al. While presenting the results of this paper at the conference Summit 240 in Budapest (2014), we learned about a recent work by Conlon, Fox, Lee, and Sudakov [15] who independently investigated Ramsey numbers of ordered graphs. There are some overlaps with our results.

Among many other results, Conlon et al. [15] proved that as n goes to inﬁnity, almost every ordering Mn of a matching on n vertices satisﬁes R(Mn) ≥ n

log n

20loglogn. This gives a similar bound as Theorem 5, where we construct one particular ordered matching on n vertices.

Conlon et al. [15] also showed that there is a constant c such that every n-vertex ordered graph G with degeneracy k and interval chromatic number p satisﬁes R(G) ≤ ncklogp. This gives a much better estimate than Theorem 8.

On the other hand, Corollary 7 gives a solution to Problem 6.9 in [15].

#### 1.2 Motivation

In this subsection we show various examples in which Ramsey-type problems on ordered hypergraphs appear. The examples consist of both classical and recent results. Some results and deﬁnitions are also used later in the paper.

Erd˝s–Szekeres lemma. This well-known fact proved by Erd˝os and Szekeres [20] states that every sequence of at least (k − 1)2 + 1 distinct integers contains a decreasing or an increasing subsequence of length k. It is easy to see that the bound (k − 1)2 + 1 is sharp. The Erd˝os–Szekeres lemma has many proofs [37] and it is a special case of a Ramsey-type result for ordered graphs.

Given a sequence S = (s1,...,sN) of integers, we construct an ordered graph (KN,≺) with vertex set S and the ordering of the vertices given by their positions in S. That is, for si,sj ∈ S, we have si ≺ sj if i < j. Then we color an edge sisj with i < j red if si < sj and blue otherwise. Afterwards, red monotone paths correspond to increasing subsequences of S and blue monotone paths to decreasing subsequences of S. The lemma now follows from the following result by Choudum and Ponnusamy [8] (Milans, Stolee, and West [32] gave a proof in the language of ordered Ramsey theory).

Proposition 10 ([8]). For integers c,r1,...,rc ≥ 1, we have

c

R((Pr1, mon),...,(Prc, mon)) = 1 +

i=1

(ri − 1).

Erd˝s–Szekeres theorem. The Erdo˝s–Szekeres theorem [20] was one of the earliest results that contributed to the development of Ramsey theory [25]. It states that for every k ∈ N, there is an integer ES(k) such that every set of at least ES(k) points in the plane in general position (no three points on a line) contains k points in convex position.

Erdo˝s and Szekeres [20] proved that ES(k) ≤ 2kk−−24 + 1. Fox, Pach, Sudakov and Suk [22]

observed that this bound follows from the equality R((Pk3, mon)) = 2kk−−24 + 1. Moshkovitz and Shapira [33] discovered a connection between ordered Ramsey numbers of monotone

hyperpaths and high-dimensional integer partitions.

Discrete geometry. We arrived at studying Ramsey numbers of ordered graphs while investigating a variant of the Erdo˝s–Szekeres problem for so-called 2-page drawings of Kn [9].1 Although this direction of research did not give any interesting results on 2-page drawings, it lead to Theorem 6.

In discrete geometry, geometric Ramsey numbers [13, 27, 28] are natural analogues of ordered Ramsey numbers. For a ﬁnite set of points P ⊂ R2 in general position, we denote

- as KP the complete geometric graph on P, which is a complete graph drawn in the plane so that its vertices are represented by the points in P and the edges are drawn as straight-line


segments between the pairs of points in P. The graph KP is convex if P is in convex position. The geometric Ramsey number of a graph G, denoted by Rg(G), is the smallest N such that every complete geometric graph KP on N vertices with edges colored by two colors contains a noncrossing monochromatic drawing of G. If we consider only convex complete geometric graphs KP in the deﬁnition, then we get so-called convex geometric Ramsey number Rc(G). Note that these numbers are ﬁnite only if G is outerplanar and that Rc(G) ≤ Rg(G) for every outerplanar graph G.

For the cycles Cn with n ≥ 3, K´arolyi et al. [28] showed the upper bound Rg(Cn) ≤ 2n2 − 6n + 6 and also observed that Rc(Cn) ≥ (n − 1)2 + 1.

Using Theorem 4, we show that the geometric and convex geometric Ramsey numbers of cycles are equal to the ordered Ramsey numbers of monotone cycles; see Corollary 20. First we observe that the ordered and convex geometric Ramsey numbers of cycles are the same.

- Observation 11. For every n ≥ 3, we have Rc(Cn) = R((Cn, mon)).


Proof. Consider a set of n points in convex position. Order the points v1 ≺ ··· ≺ vn in the clockwise order starting at an arbitrary vertex. The observation follows from the fact that a cycle with vertex set {v1,...,vn} is noncrossing if and only if it is the monotone cycle with respect to ≺.

| |
|---|


We also sketch a connection between ordered Ramsey numbers and convex geometric Ramsey numbers of outerplanar graphs in Section 5.

- 1A 2-page drawing of Kn is a drawing where the vertices of Kn are placed on a horizontal line (the spine),


the edges between consecutive vertices are subsegments of the spine and each of the remaining edges goes either above or below the spine. The edges going above the spine are red and the edges going below are blue. Let v1, . . . , vn be the vertices in the order in which they occur on the spine. A triple vi, vj, vk, where i < j < k, is colored red if vj lies below the edge vivk and blue otherwise. The color of vivjvk is thus equal to the color of vivk. A monochromatic monotone 3-uniform path corresponds to a monochromatic (2-uniform) ordered graph with pairs of vertices vi, vj connected if and only if |i − j| = 2.

Sr,s

r − 1 s − 1

Figure 2: The ordered star Sr,s.

Extremal problems on matrices. Extremal theory of {0,1}-matrices [12, 23] is essentially concerned with ordered Tura´n numbers of ordered bipartite graphs. We use some results from this theory in Subsection 2.2.

A {0,1}-matrix A contains an r × s submatrix M if A contains a submatrix B that has 1-entries at all the positions where M does. A matrix A avoids M if it does not contain M. The extremal function of M is the maximum number exM(m,n) of 1-entries in an m × n {0,1}-matrix avoiding M.

Let Kn1,n2 be the complete bipartite graph with parts of sizes n1 and n2. We use Kn1,n2 to denote the ordering of Kn1,n2 in which the two parts form disjoint intervals such that the interval of size n1 is to the left of the interval of size n2; see part b) of Figure 1.

Let G and H be ordered graphs. The ordered Tur´an number of G in H is the maximum number of edges in an ordered subgraph H of H such that G is not an ordered subgraph of H .

Let G = ((A ∪ B,E),≺), with |A| = r and |B| = s, be a a subgraph of Kr,s. Then G corresponds to an r × s {0,1}-matrix M(G) where M(G)i,j = 1 if the ith vertex in A and the jth vertex in B are adjacent in G, and M(G)i,j = 0 otherwise. It is easy to see that the ordered Tur´n number of G in Km,n equals exM(G)(m,n).

### 2 Ordered Ramsey numbers for speciﬁc classes of graphs

In this section we compute ordered Ramsey numbers of certain ordered stars, paths and cycles. We compare the formulas and bounds obtained with known Ramsey numbers of the corresponding unordered graphs.

#### 2.1 Ordered stars

- A star with n vertices is the complete bipartite graph K1,n−1. Ramsey numbers of unordered stars are known exactly [6] and they are given by


- c(n − 2) + 1 if c ≡ n − 1 ≡ 0 (mod 2),
- c(n − 2) + 2 otherwise.


R(K1,n−1;c) =

The position of the central vertex of an ordered star determines the ordering of the star uniquely up to isomorphism. We use Sr,s to denote the ordered star with r − 1 vertices to the left and s − 1 vertices to the right of the central vertex; see Figure 2.

For c,r1,...,rc ≥ 2, computing R(S1,r1,...,S1,rc) is straightforward. In the diagonal case, the ordered Ramsey numbers R(S1,n;c) are equal to the Ramsey numbers R(K1,n−1;c) for every n and c, if n is even or c is odd.

- Observation 12. For all integers c,r1,...,rc ≥ 2 we have


c

R(S1,r1,...,S1,rc) = 2 +

(ri − 2).

i=1

Proof. Let KN be an ordered complete graph with N ≥ 2 + ci=1(ri − 2) vertices and edges colored with c colors. By the pigeonhole principle, for some i ∈ [c], the leftmost vertex in KN has at least ri − 1 incident edges of color i. These edges form a copy of S1,ri.

The following c-coloring of the edges of KN with N := 1+ ci=1(ri −2) has no star S1,ri in color i. Partition all the vertices of KN except for the leftmost vertex into c subsets V1,...,Vc such that |Vi| = ri − 2. Then color each edge with its right vertex in Vi by color i. Thus no color i contains a copy of S1,ri, since otherwise all ri − 1 right neighbors of the central vertex of S1,ri are in Vi, which is impossible.

| |
|---|


Choudum and Ponnusamy [8] determined the ordered Ramsey numbers of all pairs of ordered stars by the following recursive formulas. Theorem 13 ([8]). For all integers r1,r2 > 2, we have

R(S1,r1,Sr2,1) = −1 + 1 + 8(r1 − 2)(r2 − 2)

2

+ r1 + r2 − 2.

Moreover, for all integers r1,r2,s1,s2 ≥ 2, we have

R(S1,r1,Sr2,s2) = R(S1,r1,Sr2,1) + r1 + s2 − 3 and

R(Sr1,s1,Sr2,s2) = R(Sr1,1,Sr2,s2) + R(S1,s1,Sr2,s2) − 1. General upper bound for ordered stars

Proof of Theorem 2. For every i ∈ [c], let ri and si be positive integers such that Si = Sri,si. Let N be a positive integer. Suppose that the edges of KN are colored by colors from [c] so that for every i ∈ [c], there is no Sri,si in color i. Thus, in the ordered subgraph Gi of KN formed by the edges of color i, every vertex has at most ri − 2 left neighbors or at most si − 2 right neighbors. Let Hi be the ordered subgraph of Gi obtained by deleting every edge incident from the left to a vertex with at most ri − 2 left neighbors, and every edge incident from the right to a vertex with at most si − 2 right neighbors. Clearly, |E(Gi)\E(Hi)| ≤ N ·(ri+si−4) = N ·(ni−3). It follows that the ordered graph H := ci=1 Hi has at least N2 − N · ci=1(ni − 3) = N · (N/2 − 1/2 − ci=1(ni − 3)) edges.

By the construction, each of the ordered graphs Hi is bipartite. Hence, the ordered graph H is 2c-partite (in other words, 2c-colorable). Therefore, by the AM–GM inequality or by Tura´n’s theorem, |E(H)| ≤ (1−1/2c)·N2/2 = N ·(N/2−N/2c+1). Putting the two estimates together, we obtain that N/2c+1 ≤ 1/2 + ci=1(ni − 3), from which the theorem follows.

| |
|---|


###### Lower bound for ordered stars with interval chromatic number 3

We give a lower bound for ordered Ramsey numbers of ordered stars that have at least one edge incident to the central vertex from each side. For “symmetric” stars Sri,ri with ri ≥ 2, the lower bound is within a constant multiplicative factor from the upper bound in Theorem 2. For r1 = ··· = rc = s1 = ··· = sc = 2, the bound is exactly the same as in Proposition 10.

Proposition 14. For all integers c ≥ 2 and r1,...,rc,s1,...,sc ≥ 2, we have

c

R(Sr1,s1,...,Src,sc) > 2c−1 · max max i∈[c]

{ri + si − 2},2 + 2 ·

(min(ri,si) − 2) .

i=1

Figure 3: An inductive construction of the coloring avoiding stars Sri,si with ri,si ≥ 2.

Proof. Let a := maxi∈[c]{ri + si − 2}, b := 1 + ci=1(min(ri,si) − 2), and N1 := max(a,2b). Without loss of generality, we assume that a = r1 + s1 − 2. We construct c-colorings of the complete ordered graphs with 2i−1 · N1 vertices, for i = 1,2,...,c, by induction on i.

We start the construction with coloring the edges of KN1. If N1 = a, we color every edge of KN1 by color 1. Now suppose that N1 = 2b. For every i ∈ [c], let ti := min(ri,si) − 2, and let bi be the partial sum ij=1 tj. In particular, bc = b − 1. Let b0 := 0 and let v1,v2,...,vN1 be the vertices of KN1 from left to right. For every k,l ∈ [b], k < l, color the edge vkvl by color i if bi−1 < l − k ≤ bi. In this coloring of the subgraph Kb = KN1[v1,...,vb], every vertex has at most ti left neighbors and at most ti right neighbors joined by an edge of color i. Color the subgraph KN1[vb+1,...,v2b] analogously as Kb, and ﬁnally, color every edge vivj with i ≤ b < j by color 1.

For i ∈ {2,3,...,c}, let Ni := 2i−1 · N1. Once KNi is colored, we split the vertices v1,...,vNi+1 of KNi+1 into two intervals of length Ni, and color the subgraph induced by each of the two intervals using the coloring of KNi. Then we color every edge between the two intervals by color i. See Figure 3.

It remains to verify that there is no monochromatic copy of Sri,si in the resulting coloring of KNc. In the case N1 = a, every vertex has at most r1 + s1 − 3 neighbors joined by an edge of color 1 and for every other i ∈ [c], it either has no left or no right neighbors in color i. In

the case N1 = 2b, for every i ∈ [c], every vertex has at most ri − 2 left neighbors or at most si − 2 right neighbors in color i.

| |
|---|


#### 2.2 Ordered paths

Gerencse´r and Gya´rfa´s [24] determined the exact values for the Ramsey numbers R(Pr,Ps) of two paths Pr and Ps.

Theorem 15 ([24]). For 2 ≤ r ≤ s, we have R(Pr,Ps) = s + 2 r − 1.

Here we prove Proposition 3, which shows that ordered Ramsey numbers for a particular ordering scheme of paths are linear in the number of vertices. This result contrasts with Proposition 10 and even more strongly with Theorem 5. Let v1,...,vn be the vertices of Pn in the order as they appear along the path. The alternating path (Pn, alt) is an ordered path where v1 alt v3 alt v5 alt ··· alt vn alt vn−1 alt vn−3 alt ··· alt v2 for n odd and v1 alt v3 alt v5 alt ··· alt vn−1 alt vn alt vn−2 alt ··· alt v2 for n even. See Figure 4. Obviously, the alternating path (Pn, alt) is an ordered subgraph of K n/2 , n/2 , and so it has interval chromatic number 2.

To prove Proposition 3, we use a result from extremal theory of {0,1}-matrices (see Subsection 1.2 for deﬁnitions). The following deﬁnitions are taken from [12]. We say that an r × s matrix M is minimalist if exM(m,n) = (s − 1)m + (r − 1)n − (r − 1)(s − 1) when m ≥ r

###### Figure 4: The alternating path (P7, alt).

a) b) c) d)

Figure 5: a)–d) Various constructions for the lower bound on R((Pn, alt)). The red entries represent 1, the blue entries represent 0.

and n ≥ s. Clearly, the 1 × 1 identity matrix is minimalist. If the matrix M was created from a matrix M by adding a new row (or a column) as the new ﬁrst or last row (column) and this new row (column) contains a single 1-entry next to a 1-entry of M, then we say that M was created by an elementary operation from M. Fu¨redi and Hajnal [23] proved the following lemma.

Lemma 16 ([23]). Let M be an r × s minimalist matrix and let M be an r × s matrix obtained from M by applying a sequence of elementary operations. Then M is minimalist. Proof of Proposition 3. We show that, for n > 2, we have 5 n/2 − 4 ≤ R((Pn, alt)) ≤

√

2n2 − 8n + 11. For the lower bound, let r := n/2 − 1 and N := 5r. We use an upper triangular {0,1}-matrix A = (ai,j)Ni,j=1 to represent a red-blue coloring c of KN that avoids (Pn, alt). The construction of A is sketched in part a) of Figure 5. For 1 ≤ i < j ≤ N, the edge ij of KN is blue in c if Ai,j = 0 and red in c if Ai,j = 1. For integers k and l with

- 2n − 3 +


- 1 ≤ k ≤ l ≤ 5, we use Bk,l to denote the r ×r blocks that partition A. The block Bk,l contains entries ai,j with (k − 1)r + 1 ≤ i ≤ kr and (l − 1)r + 1 ≤ j ≤ lr. There are two types of blocks. Red blocks, containing only 1-entries, and blue blocks, containing only 0-entries. The blocks B1,5,B2,2,B2,3,B3,3,B3,4,B4,4 are red and all the other blocks are blue.


Suppose for contradiction that c contains a monochromatic copy P of (Pn, alt). Then there are entries ai1,j1 = ··· = ain−1,jn−1 in A such that, for t = 1,...,n − 2, we have it < it+1 and jt = jt+1 if t is odd and it = it+1 and jt > jt+1 if t is even. Every block Bk,l has at most r rows and at most r columns of A, but P spans at least r + 1 rows and r + 1 columns. Therefore there are three blocks B1,B2,B3 of the same color that satisfy one of the following two conditions. Either the block B1 is above B2 and B3 is to the left of B2 or the block B1 is to the right of B2 and B3 is below B2. However, the matrix A contains no such triples of blocks, a contradiction.

Several alternative constructions of A are illustrated in parts b), c), and d) of Figure 5. Now we show the upper bound. Let N be a positive integer. Suppose that the edges of K N/2 , N/2 are colored red and blue. Without loss of generality, at least half of the edges are red. Consider the n/2 × n/2 {0,1}-matrix M := M((Pn, alt)), which is deﬁned in

Subsection 1.2. By Lemma 16, M is minimalist, as M is obtained from the 1 × 1 matrix with a single 1-entry by alternately adding a new last row with a single 1-entry just below another 1-entry and a new ﬁrst column with a single 1-entry to the left of another 1-entry. Therefore,

exM( N/2 , N/2 ) = ( n/2 − 1) N/2 + ( n/2 − 1) N/2 − ( n/2 − 1)( n/2 − 1) ≤

1 4

(2nN + 4n − 4N − 3 − n2).

The subgraph of K N/2 , N/2 formed by red edges has at least 12 N/2 · N/2 ≥ (N2 − 1)/8 edges. Hence, if there is no red copy of (Pn, alt), the inequality

N2 − 1 ≤ 4nN + 8n − 8N − 6 − 2n2 is satisﬁed. Consequently, N ≤ 2n − 4 +

√

2n2 − 8n + 11 and the result follows.

| |
|---|


We do not know the precise multiplicative factor in R((Pn, alt)). Our computer experiments [3] indicate that R(Pn, alt) could be of the form (n − 2)1+

√5 2 + n; see Table 1. In

our experiments we used the Glucose SAT solver [1].

|n|2<br><br>|3<br><br>|4<br><br>|5<br><br>|6|7<br><br>|8<br><br>|9|10<br><br>|11|12<br><br>|13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R(n)<br><br>|2|4<br><br>|7|9<br><br>|12|15<br><br>|17<br><br>|≥ 20|≥ 22<br><br>|≥ 25<br><br>|≥ 28<br><br>|≥ 30|


Table 1: Estimates of the ordered Ramsey numbers R(n) := R((Pn, alt)) for n ≤ 13.

For general ordered paths, Cibulka et al. [13] showed that for every ordered path Pr and the ordered complete graph Ks we have

R(Pr,Ks) ≤ 2 logs ( logr +1).

That is, for every ordered path Pn we have R(Pn) ≤ nO(logn). This bound also follows from a result of Conlon et al. [15] who showed that there is a constant c such that every n-vertex ordered graph G with degeneracy k and interval chromatic number p satisﬁes R(G) ≤ ncklogp.

The best known lower bound on R(Pn) comes from Theorem 5, which implies that there are arbitrarily long ordered paths Pn on n vertices such that R(Pn) ≥ nlogn/(5 log logn).

#### 2.3 Ordered cycles

It is a folklore result in Ramsey theory that R(C3) = R(C4) = 6 [10]. The ﬁrst results on Ramsey numbers of cycles were obtained by Chartrand and Chuster [7] and by Bondy and Erdo˝s [5]. These were later extended by Rosta [36] and by Faudree and Schelp [21]. Together, these results give exact formulas for Ramsey numbers of cycles in the two-color case.

 

2r − 1 if (r,s) = (3,3),r ≥ s ≥ 3,s is odd, r + s/2 − 1 if (r,s) = (4,4),r ≥ s ≥ 4,r,s are even, max{r + s/2,2s} − 1 if r > s ≥ 4,s is even and r is odd.

R(Cr,Cs) =



The smallest cycle whose ordered Ramsey numbers are nontrivial to determine is C4. There are three pairwise nonisomorphic orderings of C4; see Figure 6. We determine the ordered Ramsey number of each of the three orderings of C4.

(C4,≺A) (C4,≺B) (C4,≺C)

Figure 6: Three possible orderings of C4.

###### Proposition 17. We have

- 1) R((C4,≺A)) = 14,

- 2) R((C4,≺B)) = 10,

- 3) R((C4,≺C)) = 11.


Proof. We provide colorings showing the lower bounds on a separate webpage [3]. We now show the upper bounds.

- 1) This result follows from Theorem 4, which is proved later in this subsection.
- 2) Consider (K10,≺) with vertices v1 ≺ v2 ≺ ··· ≺ v10 and edges colored red and blue. We put each of the vertices {v4,v5,...,v10} into one of the following six classes. Class (i,c), where i ∈ {1,2,3} and c ∈ {red,blue}, contains vertices connected by an edge of color c to both vertices in {v1,v2,v3} \ {vi}. Note that each of the seven vertices {v4,v5,...,v10} is in one or three of these classes. Consequently, one of the six classes contains at least two vertices. Thus there are two vertices that share two left neighbors of the same color, which implies a monochromatic copy of (C4,≺B).
- 3) Exhaustive computer search showed that R((C4,≺C)) = 11 [3]. Here we prove a weaker upper bound R((C4,≺C)) ≤ 13.


Consider (K13,≺) with vertices v1 ≺ ··· ≺ v13, edges colored red and blue, and no monochromatic (C4,≺C). Without loss of generality, v1 has six red neighbors among {v2,v3,...,v12}. If v1 and v13 had two common red neighbors then they would form a red copy of (C4,≺C). Thus there is a set R ⊆ {v2,v3,...,v12} of at least ﬁve vertices such that each of them is adjacent to v1 by a red edge and to v13 by a blue edge. By Theorem 13 we have R(S1,3,S3,1) = 5. Therefore the complete graph formed by the ﬁve vertices of R contains either a vertex with at least two red edges incident from the left or a vertex with at least two blue edges incident from the right. In both cases we obtain a monochromatic copy of (C4,≺C).

| |
|---|


###### Monotone cycles

- Here we prove Theorem 4. We use the following simple lemma, which is implicitly proved in [27]. We include its proof for completeness. Lemma 18 ([27]). For positive integers r and s, we have


R((Pr, mon),Ks) = R((Pr, mon),(Ps, mon)) = (r − 1)(s − 1) + 1.

Figure 7: A coloring of K13 with no monochromatic monotone cycle of length 4.

Proof. The lower bound (r − 1)(s − 1) + 1 ≤ R((Pr, mon),(Ps, mon)) follows from Proposition 10. For the upper bound R((Pr, mon),Ks) ≤ (r − 1)(s − 1) + 1, we apply induction on r. Let G be an ordered complete graph with (r − 1)(s − 1) + 1 vertices and with edges colored red and blue. The statement is true for r = 2, since either G is a blue copy of Ks or G has a red edge. Let r ≥ 3. By the induction hypothesis, G has either a blue copy of Ks or at least (r − 1)(s − 1) + 1 − (r − 2)(s − 1) = s distinct vertices that are the rightmost vertices of a red copy of (Pr−1, mon). Either every edge between these vertices is blue, which gives a blue copy of Ks, or a red edge extends one of the red paths (Pr−1, mon) to a red copy of (Pr, mon).

| |
|---|


Proof of Theorem 4. The upper bound was proved by K´arolyi et al. [28, Theorem 2.1]. We include the proof here for completeness.

Let G be an ordered complete graph with N := 2rs − 3r − 3s + 6 vertices and with edges colored red and blue. The leftmost vertex, v1, has either at least (r−2)(s−1)+1 red neighbors or at least (r − 1)(s − 2) + 1 blue neighbors. In the ﬁrst case, by Lemma 18, G has a red copy of (Pr−1, mon) that forms a red copy of (Cr, mon) together with v1, or a blue copy of (Cs, mon). The second case is symmetric.

Now we prove the lower bound. Let N := 2rs − 3r − 3s + 5. We construct a coloring of KN = (KN,≺) that avoids a red copy of (Cr, mon) and a blue copy of (Cs, mon). See Figure 7 for an example of such coloring for r = s = 4. We partition the vertices of KN into disjoint intervals I1,...,I2r−3, from left to right. For r odd, the (r − 1)/2 leftmost and (r − 1)/2 rightmost intervals are of size s − 1 and the remaining r − 2 intervals are of size s − 2. For r even, the (r − 2)/2 leftmost and (r − 2)/2 rightmost intervals are of size s − 2 and the remaining r − 1 intervals are of size s − 1. In both cases we have N vertices in total.

We call the intervals of size s − 1 long and the intervals of size s − 2 short. We label the vertices of Ii as v1i,v2i,...,v|iI

i| from left to right. We call the index j the index of the vertex vji.

The coloring of the edges of KN is deﬁned as follows. For every i ∈ [2r − 3], we color all

T<: T≥:

Ii Ij Ii Ij

T>: T≤:

Ii Ij Ii Ij

Figure 8: The types of pairs (Ii,Ij) for s = 5 and colorings of corresponding edges.

the edges among the vertices of Ii blue. We deﬁne four types of edges with vertices in diﬀerent intervals. The type of an edge is determined by the pair of intervals containing its vertices. The color of an edge is determined by its type and by the relative value of the indices of its vertices. We say that an edge e = vkivlj between intervals Ii and Ij with i < j is of type

- • T< if j − i ≤ r − 2 and |Ii| ≤ |Ij|. In this case we color e blue if k < l and red otherwise.
- • T≥ if j − i > r − 2 and |Ii| < |Ij|. In this case we color e blue if k ≥ l and red otherwise.
- • T> if j − i > r − 2 and |Ii| ≥ |Ij|. In this case we color e blue if k > l and red otherwise.
- • T≤ if j − i ≤ r − 2 and |Ii| > |Ij|. In this case we color e blue if k ≤ l and red otherwise.


The deﬁnition of the types and the distribution of the types in KN are illustrated in Figures 8 and 9, respectively.

The distribution of long and short intervals implies the following claim.

Claim 19. Every monochromatic monotone path P in the constructed coloring of KN contains

- at most one edge uv, u ≺ v, with u in a long interval and v in a short interval, and at most one edge u v , u ≺ v , with u in a short interval and v in a long interval.


Proof. Let uv, where u ≺ v, be the ﬁrst edge of P with u in a long interval and v in a short interval. If r is odd, then u lies in Jr = (i=1r−1)/2 Ii and v lies to the right of Jr. If r is even, then u ∈ Jr = (5i=(r−r−4)2)/2/2+1 Ii and v is to the right of Jr. Any other edge of P with the left vertex in a long interval and with the right one in a short interval would have the left vertex in Jr and also to the right of v. However, this is impossible, as v is to the right of Jr. The argument for the edge u v is analogous.

| |
|---|


First we show that our coloring of KN contains no red copy of (Cr, mon). Suppose for contradiction that there is such a copy C. Let P be the monotone path on r vertices contained in C. Let u be the leftmost vertex of P and v the rightmost vertex of P. The edge uv is thus the longest edge of C. Note that C contains at most one vertex from each interval Ii, as every interval contains only blue edges. The path P contains no edge of type T> or T≥, since otherwise P would skip vertices from at least r − 2 intervals, leaving at most

- 2r − 3 − (r − 2) = r − 1 intervals. Hence the vertex indices in P are nonincreasing from left to right, as P uses red edges of types T< and T≤ only.


T> T≥ T> T< T< T≤ T< T< T< T≤

a) b)

###### T> T≤ T<

s − 2

s − 2 s − 1 s − 1 s − 1 s − 2

s − 1 s − 1

I1 I2 I3

I1 I2 I3 I4 I5

Figure 9: Distribution of types of pairs (Ii,Ij) in KN for a) r = 3 and b) r = 4.

Since the edge uv skips at least r − 2 intervals, it is of type T> or T≥, and thus the index of v is at least as large as the index of u. In combination with the previous observation, this implies that the indices of u and v are equal. Consequently, uv is of type T>, and every edge of P is of type T<. Since there are at most r − 1 long intervals and at most r − 1 short intervals, the path P contains at least one vertex from a long interval and at least one vertex from a short interval. Since every edge of P is of type T<, this implies that u is in a short interval and v is in a long interval. This is a contradiction since uv is of type T>.

Now we show that our coloring of KN contains no blue copy of (Cs, mon). Suppose for contradiction that there is such a copy C. Let P be the monotone path on s vertices contained in C. Let u be the leftmost vertex of P and v the rightmost vertex of P. This time, C can contain edges between vertices from the same interval. However, u and v belong to diﬀerent intervals, as no interval contains s vertices. We distinguish a few cases.

- 1. First, assume that P contains only edges with both vertices in the same interval, edges of type T<, and edges of type T≤. Then the vertex indices along P are nondecreasing from left to right. By Claim 19, at most one edge of P is of type T≤. Thus there is at most one edge of P between vertices with the same vertex index. Since every vertex has

index at most s − 1, we see that P has exactly one edge of type T≤ and that the index of v is s − 1. In particular, v is in a long interval. This implies that from left to right, P visits a long, a short, and a long interval, in this order. The distribution of short and long intervals implies that r is odd, u is in a long interval Ii, v is in a long interval Ij, and j − i > r − 2. This further implies that uv is of type T>, but this contradicts the fact that the index of u is 1 and the index of v is s − 1.

- 2. In the remaining case, P has an edge f between intervals Ii and Ij with j − i > r − 2. There is exactly one such edge since the total number of intervals is 2r − 3. Every other edge of P is of type T<, or of type T≤, or has both vertices in the same interval. Since e = uv is longer than f, it is of type T> or T≥. Therefore the index of u is larger than or equal to the index of v. Let x be the left vertex of f and y the right vertex of f. Let


P1 be the subpath of P with endpoints u and x, and let P2 be the subpath of P with endpoints y and v.

- (a) Suppose that P has no edge of type T≤. Then the indices of vertices in both paths P1 and P2 are strictly increasing from left to right. Since P1 and P2 have s − 2 edges in total, it follows that the index of u is equal to the index of v, the index of y is 1 and the index of x is s − 1. In particular, x is in a long interval and e is of type T≥. This implies that u is in a short interval and v is in a long interval, but this


- is in contradiction with the distribution of long and short intervals. In particular, there should be at least r − 2 intervals between the long intervals that contain x and v, but then there is no short interval to the left of the interval containing x if r is odd and there are only at most r − 3 intervals between two long intervals if r is even.
- (b) Suppose that P has an edge g of type T≤. By Claim 19, there is exactly one such edge. Since g goes from a long interval to a short interval, the edge e cannot go from a short interval to a long interval, by the distribution of long and short intervals. Thus e is of type T>. Consequently, the index of u is larger than the index of v. The indices of vertices in both paths P1 and P2 are strictly increasing from left to right, with the exception of the edge g, whose vertices can have equal indices. It follows that the index of x is s − 1 and the index of y is 1. Consequently, x is in a long interval and so f is of type T>. This is a contradiction, since P cannot have an edge of type T> together with an edge of type T≤, by the distribution of long and short intervals. In particular, y is in a long interval by Claim 19 and then there is either no short interval to the right nor to the left of f if r is odd or there is no edge of type T> between two long intervals if r is even.


This ﬁnishes the proof that our coloring of KN contains no blue copy of (Cs, mon), and the proof of Theorem 4.

Note that we have proved a slightly stronger statement: in our coloring of KN, there is no red monotone cycle of length at least r and no blue monotone cycle of length at least s.

As noted by Cibulka et al. [13], Theorem 4 implies an exact formula for geometric and convex geometric Ramsey numbers of cycles (see Subsection 1.2 for deﬁnitions). Corollary 20. For every integer n ≥ 3, we have Rc(Cn) = Rg(Cn) = 2n2 − 6n + 6.

Proof. We recall that Rc(G) ≤ Rg(G) for every outerplanar graph G. The upper bound Rg(Cn) ≤ 2n2−6n+6 was proved by Ka´rolyi et al. [28]. The lower bound 2n2−6n+6 ≤ Rc(Cn) follows from Observation 11 and Theorem 4.

| |
|---|


#### 2.4 Lower bound for matchings

- Here we prove Theorem 5. Let r ≥ 3 and let Rr := R(Kr) − 1. We construct a sequence of ordered matchings Mr,k,


k ≥ 1, with nr,k vertices and a sequence of 2-colorings cr,k of ordered complete graphs KNr,k such that cr,k avoids Mr,k. Then we choose k(r) so that nr,k(r) is exponential in r. This will imply that Nr,k(r) is superpolynomial in nr,k(r) when r grows to inﬁnity.

First we show an inductive construction of the colorings cr,k. Let Nr,1 := Rr and let cr,1 be a 2-coloring of KNr,1 avoiding Kr. Let k ≥ 1 and suppose that a coloring cr,k of KNr,k has been constructed. Let Nr,k+1 := Rr · Nr,k. Partition the vertex set of KNr,k+1 into Rr disjoint consecutive intervals I1,I2,...,IRr, each of size Nr,k. Color the complete subgraph induced by each Ii by cr,k. The remaining edges of KNr,k+1 form a complete Rr-partite ordered graph Fr,k+1, which can be colored to avoid Kr in the following way. Suppose that v1,v2,...,vRr are the vertices of KNr,1. Then for every i,j, 1 ≤ i < j ≤ Rr, and for every edge e of Fr,k+1 with one vertex in Ii and the other vertex in Ij, let cr,k+1(e) := cr,1(vivj). Clearly, Nr,k = (Rr)k for every k ≥ 1.

M3,1

Figure 10: The matching M3,1.

M3,k+1

M3,1

M3,k M3,k

J1 L1 J2 L2 J3

Figure 11: The construction of M3,k+1.

The matchings Mr,k are also constructed inductively. We start with constructing Mr,1, which serves as a basic building block. Roughly speaking, we expand the vertices of Kr to form a matching and take Rr shifted copies of this matching; see Figure 10. More precisely, consider the integers 1,2,...,r2Rr as vertices, and let li := (i − 1)rRr, for 1 ≤ i ≤ r. For every pair i,j, where 1 ≤ i < j ≤ r, we add the Rr edges {li + j,lj + i},{li + j + r,lj + i + r}, {li + j + 2r,lj + i + 2r},...,{li + j + (Rr − 1)r,lj + i + (Rr − 1)r}. Note that the vertices li + i + mr, where 1 ≤ i ≤ r and 0 ≤ m < Rr, are isolated. After removing these vertices we obtain an ordered matching Mr,1 with tr := r(r − 1)Rr vertices.

Let nr,1 := tr. Now let k ≥ 1 and suppose that Mr,k has been constructed. Let J1,L1,J2, L2,...,Lr−1,Jr be an ordered sequence of disjoint intervals of vertices, of size |Li| = nr,k and |Ji| = (r − 1)Rr. The matching Mr,k+1 is obtained by placing a copy of Mr,k on each of the

- r − 1 intervals Li and a copy of Mr,1 on the union of the r intervals Ji. See Figure 11. We have nr,k+1 = (r − 1)nr,k + tr.


Now we show that for every k, the coloring cr,k of KNr,k avoids Mr,k. Trivially, cr,1 avoids Mr,1 since nr,1 = tr > Rr = Nr,1. Let k ≥ 1 and suppose that cr,k avoids Mr,k. Let I1,...,IRr be the intervals of vertices of KNr,k+1 from the construction of cr,k+1 and let J1,L1,...,Lr−1, Jr be the intervals of vertices of Mr,k+1 from the construction of Mr,k+1. Let the edges of KNr,k+1 be colored by cr,k+1. Consider a copy of Mr,k+1 in KNr,k+1. If two intervals Jj and Jj+1 intersect some interval Ii, then Lj ⊂ Ii. Since Lj induces Mr,k in Mr,k+1 and Ii induces KNr,k colored with cr,k in KNr,k+1, the copy of Mr,k+1 is not monochromatic by induction. Thus we may assume that every interval Ii is intersected by at most one interval Jj.

Partition each interval Jj into Rr intervals Jj1,Jj2,...,JjRr of length r −1, in this order. At most Rr − 1 of the rRr intervals Jjl contain vertices from at least two intervals Ii, 1 ≤ i ≤ Rr. Thus there is an l such that for every j, 1 ≤ j ≤ r, the whole interval Jjl is contained in some interval Ii(j). Moreover, all the intervals Ii(j) are pairwise distinct by our assumption. By the construction of Mr,k+1, there is exactly one edge ej,j in Mr,k+1 between every pair of intervals Jjl, Jjl . By the coloring of Fr,k+1, we have cr,k+1(ej,j ) = cr,1(vi(j)vi(j )). Since the edges vi(j)vi(j ) form a complete subgraph with r vertices in KNr,1 and cr,1 avoids Kr, the copy

of Mr,k+1 in KNr,k+1 is not monochromatic. Thus cr,k+1 avoids Mr,k+1. Solving the recurrence for nr,k, we get

nr,k = (1 + (r − 1) + ··· + (r − 1)k−1) · tr < (r − 1)k · tr < rk+2 · Rr.

Now we assume that r is suﬃciently large and we choose k(r) as follows. Let c := (log Rr)/r, where we recall that log denotes the base 2 logarithm. By (1), we have c ∈ [1/2,2). Let k(r) := (cr/log r) − 2 = (cr/log r) − 2 − ε, where ε ∈ [0,1). Let n := nr,k(r), N := Nr,k(r) and M := Mr,k(r). We have

n = nr,k(r) < rk(r)+2 · Rr ≤ 2cr+logRr = 22cr and N = Nr,k(r) = (Rr)k(r) = 2crk(r) > 2(c2r2/logr)−3cr.

Using these bounds together with the trivial bound 2cr = Rr < n, we get

log2 n 5log log n

c2r2 log r − 3cr −

4c2r2 5(log r + log c)

log N −

>

4 5(log r + log c) > 0

1 log r −

3 cr −

= c2r2

where the last inequality is satisﬁed for r > 540. The theorem follows.

We remark that our colorings cr,k of KNr,k are not constructive, since we use the probabilistic lower bound from Ramsey’s theorem.

### 3 Upper Bounds

- 3.1 Proof of Theorem 6 We prove the following general form of Theorem 6, which allows us to use induction.


Theorem 21. For ﬁxed positive integers k, q ≥ 2 and (k,q)-decomposable ordered graphs G and H with r and s vertices, respectively, we have

R(G,H) ≤ Ck · 264k( logq/(q−1) r + logq/(q−1) s ) where Ck is a suﬃciently large constant with respect to k. Lemma 22. Let the edges of KN be colored red and blue. Then there is a set U with at least

N/(16 · 105) vertices of KN satisfying at least one of the following conditions:

- (a) every vertex of U has at least N/11 blue neighbors to the left and N/11 blue neighbors to the right of U,
- (b) every vertex of U has at least N/11 red neighbors to the left and N/11 red neighbors to the right of U.


Proof. We assume that N ≥ 16·105, otherwise the statement is trivial. We deﬁne the following two conditions for a vertex v of KN:

- (i) v has at least 21720 N blue left and at least 21720 N blue right neighbors,

- (ii) v has at least 21720 N red left and at least 21720 N red right neighbors.


First, we show that there is a set W with at least N/2000 vertices such that either every vertex of W satisﬁes (i) or every vertex of W satisﬁes (ii). Let B be the set of vertices of KN that satisfy the condition (i) and let R be the set of vertices of KN that satisfy (ii). Suppose that |B| < N/2000 and |R| < N/2000, otherwise we are done.

Let K be the ordered complete graph obtained from KN by removing the vertices of

- B ∪R. From the assumptions K has more than (1− 20002 )N = 1000999 N vertices and contains no


monochromatic ordered star St,t for t := 217 20 N + 1. Therefore K has fewer than R(St,t,St,t) vertices.

Using Theorem 13 and the fact that R(St,1,St,t) = R(S1,t,St,t), we have R(St,t,St,t) = R(St,1,St,t) + R(S1,t,St,t) − 1 = 2(R(S1,t,St,1) + 2t − 3) − 1

√

= 2 −1 + 1 + 8(t − 2)2 2

+ 4t − 5 − 1 < (8 + 2

2)t.

Altogether we have |V (K )| < (8 + 2√2)( 217 20 N + 1) < 1000999 N < |V (K )|, a contradiction. Thus there is a set W such that all its vertices satisfy one of the two conditions, say, (i).

Now, we ﬁnd the set U as a subset of W. To do so, we partition the vertex set of KN into 16·105

2000 = 800 intervals I1,...,I800 such that each contains at least N/(16 · 105) vertices of W. This is possible as |W| ≥ N/2000. Clearly, there is an interval Ii with at most N/800 vertices of KN. We set U := Ii ∩ W.

Since every vertex of U has at least 21720 N blue left neighbors, it also has at least 21720 N − N/800 > N/11 blue neighbors to the left of Ii and thus to the left of U. Analogously, every vertex of U has at least N/11 blue neighbors to the right of U. Therefore, U satisﬁes condition (a) of the lemma.

| |
|---|


We use the following two classical results further in the proof. The K˝ov´ari–S´os–Tur´an theorem [31] gives an upper bound on the maximum number of edges in a bipartite graph that contains no copy of a given complete bipartite graph.

- Theorem 23 ([4, 26, 31]). Let Z(m,n;s,t) be the maximum number of edges in a bipartite

graph G = (A ∪ B,E) with |A| = m and |B| = n that does not contain Ks,t as a subgraph with s vertices in A and t vertices in B. Assuming 2 ≤ s ≤ m and 2 ≤ t ≤ n, we have

Z(m,n;s,t) < (s − 1)1/t(n − t + 1)m1−1/t + (t − 1)m < s1/tnm1−1/t + tm.

Erdo˝s and Szekeres proved the following upper bound on oﬀ-diagonal Ramsey numbers of complete graphs.

- Theorem 24 ([20]). For every r,s ≥ 2, we have R(Kr,Ks) ≤ r+r−s−12 ≤ (r + s)r ≤ (rs)r.


By Observation 1, we have the same upper bound for the ordered Ramsey numbers R(Kr,Ks).

Proof of Theorem 21. Let G and H be (k,q)-decomposable ordered graphs with r and s vertices, respectively. Let N = Nk,q(r,s) := Ck · 264k( logq/(q−1) r + logq/(q−1) s ) where Ck is a constant suﬃciently large with respect to k. Assume that the edges of KN are colored red and blue. We show that there is a blue copy of G or a red copy of H in KN. We proceed by induction on logq/(q−1) r + logq/(q−1) s . For the induction basis, we assume that either

logq/(q−1) r = 0 or logq/(q−1) s = 0. In these cases we have r = 1 or s = 1, respectively, and the statement is trivial.

Now assume that the theorem is true for every pair G , H of (k,q)-decomposable ordered graphs with r and s vertices, respectively, such that logq/(q−1) r + logq/(q−1) s <

logq/(q−1) r + logq/(q−1) s .

Let U be the subset of vertices of KN from Lemma 22. Without loss of generality, we assume that U satisﬁes part (a) of the lemma. That is, U has at least N/(16 · 105) vertices such that each of them has at least N/11 blue neighbors to the left and N/11 blue neighbors to the right of U.

By Theorem 24, there is a blue copy of K61k or a red copy of Ks in KN[U] if |U| ≥ (61ks)61k. This condition is satisﬁed if Ck ≥ 16 · 105 · (61k)61k, since (61ks)61k ≤ (61k)61k · 261k·logs ≤ (61k)61k · 261k(logq/(q−1) s). If KN[U] contains a red copy of Ks, we are done. Thus, assume that KN[U] contains a blue copy of K61k, and let U1 ⊂ U be its vertex set.

Next we will apply Theorem 23 to obtain a set U2 ⊂ U1 of size 6k whose vertices have at least N/264k common blue neighbors to the left of U. Then we apply Theorem 23 again to obtain a set V ⊂ U2 of size k whose vertices have at least N/264k common blue neighbors to the right of U.

Let JL be the interval of vertices of KN that are to the left of U and JR the interval of vertices of KN that are to the right of U. By the construction of U, we have the trivial bound |JL|,|JR| ≥ N/11, and thus |JL|,|JR| ≤ 10N/11. Without loss of generality, we assume that |JR| ≤ N/2.

Since |JL| ≤ 10N/11, the number of blue edges between JL and U1 is at least (N/11)·|U1| ≥ |JL| · |U1|/10. By Theorem 23, we have

Z(|JL|,|U1|;|JL|/260k,6k) < (|JL|/260k)1/(6k) · 61k · |JL|1−1/(6k) + 6k · |JL|

= |JL| · (61k/210 + 6k) ≤ |JL| · 61k/10 = |JL| · |U1| 10

.

Thus, there is a blue complete bipartite graph between at least |JL|/260k vertices in JL and 6k vertices in U1. These 6k vertices form the set U2.

Since |JR| ≤ N/2, the number of blue edges between U2 and JR is at least (N/11) · |U2| ≥ |U2| · |JR| · 2/11. By Theorem 23, we have

Z(|JR|,|U2|;|JR|/27k,k) < (|JR|/27k)1/k · 6k · |JR|1−1/k + k · |JR|

2|JR| · |U2| 11

= |JR| · (6k/27 + k) ≤ |JR| · 6k · 2/11 =

.

Thus, there is a blue complete bipartite graph between at least |JR|/27k vertices in JR and k vertices in U2. These k vertices form the set V . Since |JL|,|JR| ≥ N/11, the vertices of V have at least N/(260k · 11) > N/264k common blue neighbors to the left of V and at least N/(27k · 11) > N/264k common blue neighbors to the right of V .

Since G is (k,q)-decomposable, we can partition the vertices of G into three intervals IL, I, and IR where 0 < |I| ≤ k and |IL|,|IR| ≤ r(q − 1)/q such that I is to the right of IL and to

the left of IR, the intervals IL and IR induce (k,q)-decomposable ordered graphs GL and GR, respectively, and there is no edge between GL and GR.

From our choice of N, we have N/264k = Ck · 264k( logq/(q−1) r + logq/(q−1) s −1)

= Ck · 264k( logq/(q−1) r(q−1)/q + logq/(q−1) s ) ≥ Nk,q( r(q − 1)/q ,s)

and so R(GL,H),R(GR,H) ≤ N/264k. Therefore, using the inductive assumption, we can ﬁnd either a blue copy of GL or a red copy of H in the common blue left neighborhood of V . Similarly, we can ﬁnd a blue copy of GR or a red copy of H in the common blue right neighborhood of V . Suppose that we do not obtain a red copy of H in any of these two cases. Then we ﬁnd a blue copy of G by choosing |I| vertices of V as a copy of I and connect them to the blue copies of GL and GR.

| |
|---|


#### 3.2 Proof of Theorem 8

We derive Theorem 8 as a consequence of a stronger Theorem 26, which gives an upper bound on oﬀ-diagonal ordered Ramsey numbers of graphs with constant interval chromatic number.

The ﬁrst step in the proof of Theorem 26 is the following lemma, whose proof is motivated by the proof of the upper bound on ordered Ramsey numbers of ordered paths by Cibulka et al. [13].

Lemma 25. Let k,t,n be positive integers and let G be an ordered k-degenerate graph on n vertices. Then R(G,Kt,t) ≤ n2tk+1.

Proof. Assume that G = (G,≺). Let N := n2tk+1 and assume that the edges of KN are colored red and blue. We partition the vertices of KN into n disjoint consecutive intervals of length ntk+1. The ith such interval is denoted by I(v) where v is the ith vertex of G in the ordering ≺.

We try to construct a blue copy h(G) of G in KN in n steps. In each step of the construction we ﬁnd an image h(w) ∈ I(w) of a new vertex w of G or a red copy of Kt,t.

For every vertex v of G that has no image h(v) yet, we keep a set U(v) ⊆ I(v) of possible candidates for h(v). At the beginning we set U(v) := I(v) for every v ∈ V (G). Throughout the proof, we will keep the property that the size of U(v) is a multiple of t.

Let be an ordering of the vertices of G such that every vertex v of G has at most k left neighbors in . This ordering exists as G is k-degenerate. Note that the ordering might diﬀer from the ordering ≺.

Let w be the leftmost vertex of G in the ordering that has no image h(w) yet. Suppose that u1,...,us ∈ V (G) are the right neighbors of w in . We show how to ﬁnd the image h(w) or a red copy of Kt,t in KN.

Let i ∈ [s]. We claim that in U(w) every vertex except for at most t − 1 vertices has at least |U(ui)|/t blue neighbors in U(ui) or there is a red copy of Kt,t with edges between U(w) and U(ui).

Suppose ﬁrst that there is a subset W ⊆ U(w) of size t such that each vertex of W has fewer than |U(ui)|/t blue neighbors in U(ui). In such a case we delete from U(ui) every vertex that is a blue neighbor of some vertex of W. Afterwards, there are still at least

|U(ui)| − |W| ·

|U(ui)| t − 1 = |U(ui)| − t ·

|U(ui)| t − 1 = t

vertices left in U(ui) and every such vertex has only red neighbors in W. Thus we have a red copy of Kt,t in KN.

By our claim, there is a red copy of Kt,t in KN or a set Z(w) ⊆ U(w) of size at least |U(w)| − s(t − 1) > |U(w)| − nt such that for every i ∈ [s], every vertex of Z(w) has at least |U(ui)|/t blue neighbors in U(ui). We may assume that the latter case occurs, as otherwise we are done.

We choose an arbitrary vertex h(w) of Z(w) to be the image of w in the constructed blue copy h(G) of G. For this we need to know that Z(w) is nonempty; we show this at the end of the proof. For every i ∈ [s], we update the set U(ui) to be a set of |U(ui)|/t blue neighbors of h(w) in U(ui).

After these updates, we choose the ﬁrst vertex in that does not have an image yet and proceed with the next step. If every vertex of G has an image, then we have found a blue copy of G.

It remains to show that the set Z(w) is nonempty in each step. Since w has at most k left neighbors in , we have updated U(w) at most k times. The size of U(w) is initially ntk+1 and it is divided by t in every update. Thus, in the end, |U(w)| ≥ nt. Consequently, |Z(w)| > |U(w)| − nt ≥ 0.

| |
|---|


Let Kp(n) be the ordered complete p-partite graph with parts of size n forming consecutive intervals.

- Theorem 26. Let k, n, and p ≥ 2 be positive integers and let G be an ordered k-degenerate graph on n vertices. Then


R(G,Kp(n)) ≤ n(1+2/k)(k+1) logp −2/k. Proof. First, we deﬁne a function fk,n(q): N → N as

fk,n(q) := n(1+2/k)(k+1)q−2/k.

This function satisﬁes the recurrence fk,n(1) = nk+3 and fk,n(q) = n2 · (fk,n(q − 1))k+1 for every integer q ≥ 2.

We assume without loss of generality that p = 2q for some positive integer q. We proceed by induction on q. The case q = 1 follows immediately from Lemma 25 applied with t := n.

Now let q ≥ 2. Let KN be an ordered complete graph with N := fk,n(q) vertices and edges colored red and blue. We show that there is always a blue copy of G or a red copy of Kp(n) in KN.

According to Lemma 25, there is a blue copy of G or a red copy of Kt,t for t := fk,n(q − 1). In the ﬁrst case we are done, thus we assume that the latter case occurs. Let A be the left part of size t and B the right part of size t in the red copy of Kt,t.

Since the induced ordered subgraph KN[A] has fk,n(q − 1) vertices, there is a blue copy of G or a red copy of Kp/2(n) in KN[A] by the inductive assumption. An analogous statement holds for the ordered subgraph KN[B].

Thus, if there is no blue copy of G in KN[A] and in KN[B], then the two red copies of Kp/2(n) together with the red edges between KN[A] and KN[B] form a red copy of Kp(n) in KN.

| |
|---|


Figure 12: Minimal nonseparable ordered graphs with interval chromatic number at least 3.

### 4 Fixed ordered graph, variable number of colors

Here we discuss the asymptotics of ordered Ramsey numbers R(G;c) of a ﬁxed ordered graph G as a function of the number of colors. That is, for the rest of the section we assume that G is a ﬁxed ordered graph and that the number c of colors can be arbitrarily large.

The unordered Ramsey numbers are at most polynomial for bipartite graphs and at least exponential otherwise; this follows from the K˝ov´ari–S´os–Tur´an theorem (Theorem 23) and from the existence of a decomposition of Kn into log n bipartite subgraphs, respectively. For ordered Ramsey numbers we observe a similar dichotomy, but the characterization is more subtle.

An ordered graph G is separable if the vertex set of G can be partitioned into two nonempty intervals I1,I2 such that there is no edge between I1 and I2. An ordered graph is nonseparable if it is not separable.

We ﬁnd that R(G;c) is exponential in c if G contains a nonseparable ordered graph with interval chromatic number 3, and polynomial otherwise. Moreover, there are only ﬁnitely many minimal nonseparable ordered graphs with interval chromatic number at least 3. Therefore, the class of ordered graphs with polynomial ordered Ramsey numbers can be characterized by a ﬁnite number of forbidden ordered subgraphs.

Proof of Theorem 9. For part 1, let G be a given n-vertex ordered graph contained in n · Kn,n. For N := (2cn)n+1, let the edges of KN be colored with c colors. We ﬁnd a monochromatic copy of G.

For t := cn, we partition the vertex set of KN into 2t intervals A1,B1,...,At,Bt in this order, such that each interval has size K := (2cn)n. For every i = 1,...,t, it follows from the pigeonhole principle that there is a color ci that colors at least K2/c edges of KN[Ai ∪ Bi].

By Theorem 23, we have Z(K,K;n,n) < 2nK2−1/n = K2/c. Consequently, for every i = 1,...,t, there is a copy of Kn,n of color ci in KN[Ai ∪ Bi]. By the pigeonhole principle, we have a monochromatic copy of n · Kn,n. Since G ⊆ n · Kn,n, we have a monochromatic copy of G as well.

To prove part 2, we ﬁrst show that if G is not contained in n · Kn,n, then G contains one of the ordered graphs from Figure 12.

The ordered graph G contains a nonseparable ordered graph H with interval chromatic number t ≥ 3, since G is not an ordered subgraph of n · Kn,n. Let I1,...,It be a partitioning of the vertex set of H into t consecutive intervals such that there is no edge of H with both vertices in the same interval. Then H has an edge e between intervals I1 and I2 and an edge f between intervals I2 and I3. If e and f share a vertex, they form a monotone path on three vertices, which is the ﬁrst ordered graph in Figure 12.

Assume that no vertex of I2 has a neighbor in both I1 and I3 ∪ ··· ∪ It. Then we partition I2 into sets A1, A2, and A3 such that every vertex of A1 has a neighbor in I1, no vertex in A2

has a neighbor in I1 ∪ I3, and every vertex of A3 has a neighbor in I3. If A3 is to the left of A1, then we can move some vertices of I2 into I1 and some into I3 to obtain a partitioning of the vertex set of H into t − 1 intervals such that there is no edge with both vertices in the same interval. This is impossible, as the interval chromatic number of H is t. Thus we can assume that the vertex in e ∩ I2 is to the left of the vertex in f ∩ I2 and that every vertex between e ∩ I2 and f ∩ I2 lies in A2.

Since H is nonseparable, there is an edge g of H with one vertex to the left of e ∩ I2 and the other one to the right of f ∩ I2. The left vertex of g either lies to the left of e ∩ I1, or is in e ∩ I1, or lies between e ∩ I1 and e ∩ I2. Similarly, the right vertex of g is either to the right of f ∩ I3, or is in f ∩ I3 or lies between f ∩ I3 and f ∩ I2. This gives us nine pairwise nonisomorphic ordered graphs formed by the edges g, e, and f. Each of these ordered graphs is in Figure 12.

To ﬁnish the proof, note that every color in the coloring of K2c from the proof of Proposition 14 with r1 = ··· = rc = 2 = s1 = ··· = sc induces an ordered subgraph of 2c · K2c,2c. In particular, there is no monochromatic copy of G. Therefore we have R(G;c) > 2c.

| |
|---|


We note that the coloring of K2c from the previous proof is an ordered variant of a particular “optimal” decomposition of the edges of K2c into c bipartite graphs.

### 5 Open problems

Theorem 8 implies that ordered Ramsey numbers of graphs that have bounded degree and bounded interval chromatic number are polynomial in the number of vertices. However, we have no nontrivial lower bounds.

- Problem 1. Is there an absolute constant c > 0 such that for every ﬁxed ∆ there is a sequence {Gn}n∈N of ordered ∆-regular graphs Gn with n vertices and interval chromatic number 2 such that R(Gn) ≥ nc∆?

Similarly, it would be interesting to ﬁnd some nontrivial lower bounds on ordered Ramsey numbers of ordered graphs of constant bandwidth. Let Pn(p) be the ordered graph on n vertices v1,...,vn, in this order, such that vivj is an edge if and only if 0 < |i − j| ≤ p. In particular, Pn(1) = (Pn, mon). Note that every ordered graph with n vertices and with bandwidth at most p is an ordered subgraph of Pn(p).

- Problem 2. For an integer p ≥ 2, what is the growth rate of R(Pn(p)) with respect to n?

We know that the ordered Ramsey numbers of alternating paths are linear with respect to the number of vertices. Is it true that these orderings minimize ordered Ramsey numbers of ordered paths?

- Problem 3. For some positive integer n, is there an ordering Pn of the path Pn on n vertices such that R(Pn) < R((Pn, alt))?


Finally, we mention a problem with an application in the theory of geometric Ramsey numbers (see the deﬁnition in Section 1.2). A crossing in an ordered graph (G,≺) is a pair of edges vivk, vjvl such that vi ≺ vj ≺ vk ≺ vl. An ordered graph is noncrossing if it contains no crossing.

vn(3) = vn(4)

G(4) G(3)

v1(2) = v1(3)

v1(1) = v1(4)

G(2)

G(1)

vn(1) = vn(2)

Figure 13: Construction of the graph H in the proof of Theorem 27.

Let Rnc(n) be the largest ordered Ramsey number of a noncrossing ordered graph on n vertices. Since noncrossing ordered graphs are outerplanar, they are 2-degenerate, and thus, by a result of Conlon et al. [15], we have Rnc(n) ≤ nO(logn).

- Problem 4. What is the growth rate of Rnc(n)? In particular, is it polynomial in n?


It is an open problem whether there is a general polynomial upper bound for geometric Ramsey numbers of outerplanar graphs [13]. The following theorem shows that Problem 4 is equivalent to the question of determining the asymptotics of the maximum convex geometric Ramsey number of an outerplanar graph on n vertices.

- Theorem 27. Let Rc(n) be the maximum convex geometric Ramsey number of an outerplanar graph on n vertices. For every n ≥ 2, we have


Rc(n) ≤ Rnc(n) ≤ Rc(4n − 4).

Proof. Let G be an outerplanar graph drawn in the plane so that its vertices are the vertices of a convex n-gon, and the edges are drawn as straight-line segments with no crossings. Let v1 ≺ v2 ≺ ··· ≺ vn be a clockwise ordering of the vertices of G along the n-gon with v1 chosen arbitrarily. In this way, we obtain a noncrossing ordered graph G. If we ﬁnd a monochromatic

- copy of G in every 2-coloring of KN for some N, we can ﬁnd a monochromatic noncrossing copy of the graph G in every 2-coloring of the complete convex geometric graph on N vertices. This proves of the ﬁrst inequality.


Now we prove the second inequality. The case n = 2 is trivial, so we assume that n ≥ 3. Since adding edges to an ordered graph never decreases its ordered Ramsey number, we know that Rnc(n) is attained by a noncrossing ordered graph G with vertices v1 ≺ ··· ≺ vn that contains the Hamiltonian cycle v1,v2,...,vn,v1. We form an outerplanar graph H as follows. We take four unordered copies G(1),...,G(4) of G. For every i ∈ [4], let v1(i),...,vn(i) be the set of vertices of G(i). We identify vn(1) with vn(2), v1(2) with v1(3), vn(3) with vn(4), and v1(4) with v1(1). See Figure 13. The resulting graph H is Hamiltonian and thus there is only one planar straight-line drawing of H on a given set of 4n − 4 points in convex position, up to rotation and mirroring.

Let K be a complete geometric graph whose vertices u1,u2,...,uN form, in this order, the vertices of a convex polygon. In every noncrossing copy of H in K, at least three of the graphs G(i), where i ∈ [4], satisfy the property that the images of the vertices v1(i),...,vn(i) form a monotone sequence in the ordering u1 ≺ u2 ≺ ··· ≺ uN. Consequently, in at least one G(i), the vertices form an increasing sequence. If N ≥ Rc(4n − 4), every 2-coloring of the complete convex geometric graph on N vertices contains a monochromatic noncrossing

- copy of H. Therefore, every 2-coloring of KN contains a monochromatic copy of the ordered graph G.


| |
|---|


By the ﬁrst inequality in Theorem 27, the upper bound Rnc(n) ≤ nO(logn) by Conlon et al. [15] gives a quasipolynomial upper bound on Rc(n), improving the previous exponential bound (see, e.g., [13]).

### Acknowledgments

The authors would like to thank to Jiˇr´ı Matouˇsek for many helpful comments. Part of the research was conducted during the DIMACS REU 2013 program.

### References

- [1] G. Audemard and L. Simon, Glucose 2.3 in the SAT 2013 Competition, Department of Computer Science Series of Publications B vol. B-2013-1, University of Helsinki (2013), 42–43.
- [2] M. Balko, J. Cibulka, K. Kra´l, and J. Kyncˇl, Ramsey numbers of ordered graphs, Electron. Notes Discrete Math. 49 (2015), 419–424.
- [3] M. Balko, J. Cibulka, K. Kr´al, and J. Kynˇcl, http://kam.mﬀ.cuni.cz/˜balko/ordered ramsey

- [4] B. Bollob´as, Extremal Graph Theory, New York: Dover publications, ISBN 978-0-48643596-1 (2004).
- [5] J. A. Bondy and P. Erdo˝s, Ramsey numbers for cycles in graphs, J. Combin. Theory Ser. B 14(1) (1973), 46–54.
- [6] S. A. Burr and J. A. Roberts, On Ramsey numbers for stars, Utilitas Math. 4 (1973), 217–220.
- [7] G. Chartrand and S. Schuster, On the existence of speciﬁed cycles in complementary graphs, Bull. Amer. Math. Soc. 77 (1971), 995–998.
- [8] S. A. Choudum and B. Ponnusamy, Ordered Ramsey numbers, Discrete Math. 247(1–3)

(2002), 79–92.

- [9] F. R. K. Chung, F. T. Leighton, and A. L. Rosenberg, Embedding graphs in books: a layout problem with applications to VLSI design, SIAM J. on Algebraic Discrete Methods 8(1) (1987), 33–58.
- [10] V. Chv´atal and F. Harary, Generalized Ramsey theory for graphs, II, Small diagonal numbers, Proc. Amer. Math. Soc. 32(2) (1972), 389–394.
- [11] V. Chv´atal, V. R¨odl, E. Szemer´edi, and W. T. Trotter Jr., The Ramsey number of a graph with bounded maximum degree, J. Combin. Theory Ser. B 34(3) (1983), 239–243.
- [12] J. Cibulka, Extremal combinatorics of matrices, sequences and sets of permutations, Ph.D. Thesis, Charles University, Prague (2013).


- [13] J. Cibulka, P. Gao, M. Krcˇ´l, T. Valla, and P. Valtr, On the geometric Ramsey number of outerplanar graphs, Discrete Comput. Geom. 53(1) (2015), 64–79.
- [14] D. Conlon, A new upper bound for diagonal Ramsey numbers, Ann. of Math. 170(2)

(2009), 941–960.

- [15] D. Conlon, J. Fox, C. Lee, and B. Sudakov, Ordered Ramsey numbers, J. Combin. Theory Ser. B 122 (2017), 353–383.
- [16] D. Conlon, J. Fox, and B. Sudakov, Ramsey numbers of sparse hypergraphs, Random Structures Algorithms 35(1) (2009), 1–14.
- [17] D. Conlon, J. Fox, and B. Sudakov, Recent developments in graph Ramsey theory, Surveys in combinatorics 2015, 49–118, London Math. Soc. Lecture Note Ser., 424, Cambridge Univ. Press, Cambridge, 2015.
- [18] M. Elia´sˇ and J. Matousˇek, Higher-order Erdo˝s–Szekeres theorems, Adv. Math. 244 (2013), 1–15.
- [19] P. Erd˝os, Some remarks on the theory of graphs, Bull. Amer. Math. Soc 53(4) (1947), 292–294.
- [20] P. Erdo˝s and G. Szekeres, A combinatorial problem in geometry, Compos. Math 2 (1935), 463–470.
- [21] R. J. Faudree and R. H. Schelp, All Ramsey numbers for cycles in graphs, Discrete Math. 8(4) (1974), 313–329.
- [22] J. Fox, J. Pach, B. Sudakov, and A. Suk, Erd˝os–Szekeres-type theorems for monotone paths and convex bodies, Proc. London Math. Soc. 105(5) (2012), 953–982.
- [23] Z. Fu¨redi and P. Hajnal, Davenport–Schinzel theory of matrices, Discrete Math. 103(3)

(1992), 233–251.

- [24] L. Gerencs´er and L. Gy´arf´as, On Ramsey-type problems, Ann. Univ. Sci. E¨otv¨os Sect. Math. 10 (1967), 167–170.
- [25] R. Graham and J. Nesˇetrˇil, Ramsey theory and Paul Erdo˝s (recent results from a historical perspective), Paul Erdo˝s and his mathematics. II (Budapest, 1999), 339–365, Bolyai Soc. Math. Stud. 11, J´nos Bolyai Math. Soc., Budapest (2002).
- [26] C. Hylt´en-Cavallius, On a combinatorial problem, Colloq. Math. 6 (1958), 59–65.
- [27] Gy. Ka´rolyi, J. Pach, and G. To´th, Ramsey-type results for geometric graphs, I, Discrete Comput. Geom. 18(3) (1997), 247–255.
- [28] Gy. K´arolyi, J. Pach, G. T´oth, and P. Valtr, Ramsey-type results for geometric graphs, II, Discrete Comput. Geom. 20(3) (1998), 375–388.
- [29] M. Klazar, Extremal problems for ordered (hyper)graphs: applications of Davenport– Schinzel sequences, European J. Combin. 25(1) (2004), 125–140.


- [30] M. Klazar, Extremal problems for ordered hypergraphs: small patterns and some enumeration, Discrete Appl. Math. 143(1–3) (2004), 144–154.
- [31] T. K˝ov´ari, V. S´os, and P. Tur´an, On a problem of K. Zarankiewicz, Colloq. Math., 3

(1954), 50–57.

- [32] K. G. Milans, D. Stolee, and D. B. West, Ordered Ramsey theory and track representations of graphs, J. Comb., 6(4) (2015), 445–456.
- [33] G. Moshkovitz and A. Shapira, Ramsey theory, integer partitions and a new proof of the Erd˝s–Szekeres theorem, Adv. in Math. 262 (2014), 1107–1129.
- [34] J. Pach and G. Tardos, Forbidden paths and cycles in ordered graphs and matrices, Israel J. Math. 155(1) (2006), 359–380.
- [35] F. P. Ramsey, On a Problem of Formal Logic, Proc. London Math. Soc. S2-30(1) (1930), 264–286.
- [36] V. Rosta, On a Ramsey-type problem of J. A. Bondy and P. Erd˝os, J. Combin. Theory Ser. B 15(1) (1973), 94–120.
- [37] J. M. Steele, Variations on the monotone subsequence theme of Erd˝os and Szekeres, in: Discrete Probability and Algorithms (Minneapolis, MN, 1993), 111–131, IMA Vol. Math. Appl. 72, Springer, New York (1995).


