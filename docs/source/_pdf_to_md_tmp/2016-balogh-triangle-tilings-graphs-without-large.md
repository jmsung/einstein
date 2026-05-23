arXiv:1607.07789v1[math.CO]26Jul2016

# Triangle-tilings in graphs without large independent sets

### J´zsef Balogh∗, Andrew McDowell†, Theodore Molla‡, Richard Mycroft§ November 25, 2018

Abstract

We study the minimum degree necessary to guarantee the existence of perfect and almost-perfect triangle-tilings in an n-vertex graph G with sublinear independence number. In this setting, we show that if δ(G) ≥ n/3 + o(n) then G has a triangle-tiling covering all but at most four vertices. Also, for every r ≥ 5, we asymptotically determine the minimum degree threshold for a perfect triangle-tiling under the additional assumptions that G is Kr-free and n is divisible by 3.

## 1 Introduction

A triangle-tiling in a graph G is a collection T of vertex-disjoint triangles in G. We say that T is perfect if |T | = n/3, where n is the order of G. A trivial necessary condition for the existence of a perfect triangle-tiling is that 3 divides n. We let V (T ) := T∈T V (T) and say T covers U ⊆ V (G) (respectively v ∈ V (G)) when U ⊆ V (T ) (respectively v ∈ V (T )), so a perfect triangle-tiling covers every vertex of the host graph. Given disjoint sets A and B which partition V (G), we say that a triangle T in G is an Atriangle if T contains two vertices of A and one vertex of B, and likewise that T is a B-triangle if T contains two vertices of B and one vertex of A. Observe that if |A| = 1 (mod 3) and |B| = 2 (mod 3), there are no B-triangles in G and also there is no pair of vertex-disjoint A-triangles in G, then G does not have a perfect triangle-tiling. In that case, we call the ordered pair (A, B) a divisibility barrier in G (note that order is

![image 1](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile1.png>)

∗Department of Mathematical Sciences, University of Illinois at Urbana-Champaign, Urbana, Illinois 61801, USA. jobal@math.uiuc.edu. Research is partially supported by NSA Grant H98230-15-1-0002, NSF Grant DMS-1500121 and Arnold O. Beckman Research Award (UIUC Campus Research Board 15006).

†School of Mathematics, University of Birmingham, Birmingham, B15 2TT, United Kingdom. a.j.mcdowell@bham.ac.uk.

‡Department of Mathematical Sciences, University of Illinois at Urbana-Champaign, Urbana, Illinois 61801, USA. molla@illinois.edu. Research is partially supported by NSF Grant DMS-1500121.

§School of Mathematics, University of Birmingham, Birmingham, B15 2TT, United Kingdom. r.mycroft@bham.ac.uk. Research is partially supported by EPSRC grant EP/M011771/1.

The authors are grateful to the BRIDGE strategic alliance between the University of Birmingham and the University of Illinois at Urbana-Champaign. This research was conducted as part of the Building Bridges in Mathematics BRIDGE Seed Fund project.

important here). Similarly, if A ⊆ V (G) has size |A| ≥ 2n/3 + r for some r > 0, but G[A] has no triangles, then every triangle-tiling in G contains at most n − |A| ≤ n/3 − r triangles, and so leaves at least 3r vertices uncovered. We call such a set A a space barrier.

The classical Corr´di-Hajnal theorem [4] states that if G has minimum degree δ(G) ≥ 2n/3, and n is divisible by 3, then G contains a perfect triangle-tiling. The minimum degree condition of this result is easily seen to be best-possible by considering, for an arbitrary m ∈ N, the complete tripartite graph G1(m) with vertex classes of size m−1, m and m+1. Indeed, G1(m) then has n := 3m vertices and δ(G1(m)) ≥ 2m−1 = 2n/3−1, but G1(m) has no perfect triangle-tiling, as the union of the two largest vertex classes is a space barrier. Observe, however, that G1(m) contains large independent sets. By proving the following theorem, Balogh, Molla and Sharifzadeh [2] recently showed that the minimum degree condition can be signiﬁcantly weakened if we additionally assume that G has no large independent set. Throughout this paper we write α(G) to denote the independence number of G.

- Theorem 1.1 ([2, Theorem 1.2]). For every ω > 0 there exist n0, γ > 0 such that the following holds for every integer n ≥ n0 which is divisible by 3. If G is a graph on n

- vertices with δ(G) ≥ n/2 + ωn and α(G) ≤ γn, then G contains a perfect triangle-tiling.

For an arbitrary m ∈ N, the graph G2(m) consisting of two copies of K3m+2 intersecting in a single vertex has n := 6m + 3 vertices, minimum degree δ(G2(m)) = 3m + 1 = ⌊n/2⌋ and independence number two. Moreover, G2(m) has a divisibility barrier (A, B), where B is the vertex set of one of the copies of K3m+2 and A = V (G2(m))\B. This example demonstrates that the minimum degree condition of Theorem 1.1 is bestpossible up to the ωn additive error term. Noga Alon suggested that if one only wants a triangle-tiling that covers all but a constant number of vertices, then perhaps the condition δ(G) ≥ (1/3+o(1))n is suﬃcient. In this paper, we show that this is indeed the case, by proving that if δ(G) ≥ (1/3 + o(1))n and α(G) = o(n), then G has a triangle-tiling covering all but at most four vertices. Furthermore, under the additional assumptions that G has no divisibility barrier and 3 divides n, we show that G contains a perfect triangle-tiling.

Theorem 1.2. For every ω > 0 there exist n0, γ > 0 such that if G is a graph on n ≥ n0

- vertices with δ(G) ≥ n/3 + ωn and α(G) ≤ γn, then




- (a) G contains a triangle-tiling covering all but at most four vertices of G, and
- (b) if 3 divides n and G contains no divisibility barrier, then G contains a perfect triangle-tiling.


Observe that for an arbitrary m ∈ N, the graph G3(m) consisting of two disjoint copies of K3m+2 has n := 6m+4 vertices, minimum degree δ(G3(m)) = 3m+1 = n/2−1 and independence number two, but every triangle-tiling in G3(m) covers at most n − 4 vertices. This demonstrates that the conditions of Theorem 1.2 do not guarantee a triangle-tiling which leaves fewer than four vertices uncovered. Furthermore, in Section 5 we give a construction showing that the ωn error term in the minimum degree condition of Theorem 1.2 cannot be removed completely.

The relationship between the results in this paper and the Corra´di-Hajnal theorem is clearly analogous to the relationship between Ramsey-Tura´n theory and Tura´n’s theorem,

- as Ramsey-Tura´n theory is concerned with the maximum possible number of edges in an H-free graph on n vertices with some upper bound on α(G). More precisely, in classical Ramsey-Tura´n theory the principle object of study is the function RT(n, H, m), which is deﬁned to be the maximum number of edges in an H-free, n-vertex graph with independence number at most m, whenever such a graph exists for n, H and m. The

asymptotic value of RT(n, Kr, o(n)) was established for odd r by Erd˝os and S´os [5] and for even r by Erd˝os, Hajnal, S´os and Szemer´edi [6], giving the following theorem.

Theorem 1.3 ([5, Theorem 1] and [6, Theorem 1]). For every r ≥ 3, we deﬁne

fRT(r) :=

r−3

![image 2](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile2.png>)

r−1 if r is odd,

3r−10

![image 3](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile3.png>)

3r−4 if r is even.

- (a) For every ω > 0, there exists γ, n0 > 0 such that if G is a graph on n ≥ n0 vertices

with α(G) ≤ γn and with at least (fRT(r) + ω) n2 edges, then G contains a copy of Kr.

- (b) For every ω > 0 and γ > 0, there exists n0 > 0 such that for every n ≥ n0, there exists a Kr-free graph G := GRT(n, r, ω, γ) on n vertices such that δ(G) ≥ (fRT(r) − ω)n and α(G) ≤ γn.


Observe that for any r ≥ 3, ω, γ > 0 and each suﬃciently large n divisible by 6, the graph G4(n) on n vertices consisting of the disjoint union of GRT(n2 − 1, r, ω, γ) and GRT(n2 + 1, r, ω, γ) is Kr-free, has minimum degree δ(G4(n)) ≥ f

![image 4](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile4.png>)

![image 5](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile5.png>)

RT(r)

![image 6](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile6.png>)

2 − ω n and independence number at most γn. However, as G4(n) contains a divisibility barrier, it has no perfect triangle-tiling. Although the construction of GRT(n, r, ω, γ) was given in [5] (when r is odd) and [6] (when r is even), for completeness, we describe GRT(n, r, ω, γ)

- at the end of Section 5. By combining Theorems 1.2 and 1.3 we determine, for every r ≥ 5, the asymptotic


minimum degree threshold for a perfect triangle-tiling in a Kr-free graph with sublinear independence number. Indeed, Corollary 1.4 does this for r ≥ 7, and the thresholds for r = 5 and r = 6 follow, as discussed after the proof.

Corollary 1.4. For every r ≥ 7 and ω > 0 there exist n0, γ > 0 such that the following holds for every integer n ≥ n0 which is divisible by 3. If G is a Kr-free graph on n vertices with δ(G) ≥ f

RT(r)

2 n + ωn and α(G) ≤ γn, then G contains a perfect triangle-tiling.

![image 7](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile7.png>)

Proof. Given ω > 0, choose γ small enough and n0 large enough to apply Theorem 1.2 with the same constants there as here and so that we may apply Theorem 1.3(a) with 3γ and n0/3 in place of γ and n0 respectively. We also insist that γn0 + 2 ≤ ωn0/2. Since fRT(r)

2 ≥ 31 for r ≥ 7, by Theorem 1.2(b) it suﬃces to prove that no Kr-free graph on n ≥ n0 vertices with δ(G) ≥ f

![image 8](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile8.png>)

![image 9](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile9.png>)

RT(r)

2 n + ωn and α(G) ≤ γn contains a divisibility barrier. So let G be such a graph, and suppose for a contradiction that (X, Y ) is a divisibility barrier in G. Let A be the smaller of X and Y , and let B be the larger, so |A| ≤ n/2. By deﬁnition of a divisibility barrier, if A = Y then there is no pair of vertex-disjoint B-triangles in G, whilst if A = X then there are no B-triangles in G at all. It follows that at most one vertex a ∈ A has more than γn + 2 neighbours in B, as given two such vertices a, a′ ∈ A we could use the fact that α(G) ≤ γn to choose an edge bc in N(a) ∩B

![image 10](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile10.png>)

and then an edge b′c′ in (N(a′)∩B)\e to obtain a pair of vertex-disjoint B-triangles abc and a′b′c′ in G. So at least |A|−1 vertices of A have at least δ(G)−γn−2 ≥ f

RT(r)

2 n+ ω2n neighbours in A. So in particular |A| ≥ f

![image 11](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile11.png>)

![image 12](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile12.png>)

RT(r)

2 n ≥ n3. Moreover we have

![image 13](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile13.png>)

![image 14](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile14.png>)

e(G[A]) ≥

- 1

![image 15](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile15.png>)

- 2


(|A|−1)

ω 2

fRT(r) 2

+

![image 16](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile16.png>)

![image 17](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile17.png>)

n 2|A|

n =

(fRT(r) + ω)

![image 18](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile18.png>)

|A| 2

≥ (fRT(r) + ω)

|A| 2

,

so G[A] contains a copy of Kr by Theorem 1.3(a). This contradicts our assumption that G was Kr-free and so completes the proof.

![image 19](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile19.png>)

![image 20](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile20.png>)

![image 21](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile21.png>)

![image 22](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile22.png>)

2 < f

RT(7)

Note that f

RT(5)

2 = 13. In Section 5 we give a construction of a K5-free graph on n vertices with minimum degree at least n/3 and sublinear independence number which contains a space barrier. This demonstrates that the minimum degree condition in Corollary 1.4 is best-possible up to the ωn error term for r = 7, and cannot be lowered by requiring G to be K5-free as opposed to K7-free. Furthermore, the graph G4(n) presented after Theorem 1.3 shows that the minimum degree condition in Corollary 1.4 is best-possible up to the ωn error term for r ≥ 8 also.

![image 23](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile23.png>)

![image 24](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile24.png>)

![image 25](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile25.png>)

In a K4-free graph, we can only construct space barriers when δ(G) < n/6, so it may be true that, in a K4-free graph, the conditions δ(G) ≥ (1/6 + o(1))n and α(G) = o(n) are suﬃcient to guarantee a perfect triangle-tiling when n is divisible by 3; we discuss this further in Section 5. Also in Section 5, we consider the problem of determining the minimum degree condition which guarantees a perfect Kk-tiling in a graph with sublinear independence number when k ≥ 4.

## 2 Notation and preliminary results

In this section we introduce various results which we will use in the proof of Theorem 1.2, beginning with helpful notation. We write x = y ± z to mean y − z ≤ x ≤ y + z, and [n] to denote the set of integers from 1 to n. We omit ﬂoors and ceilings throughout this paper wherever they do not aﬀect the argument. We write x ≪ y to mean that for every y > 0 there exists x0 > 0 such that the subsequent statements hold for x and y whenever 0 < x ≤ x0. Similar statements with more variables are deﬁned similarly.

### 2.1 Regularity

In a graph G, for each pair of disjoint non-empty sets A, B ⊆ V (G) we write G[A, B] for the bipartite subgraph of G with vertex classes A and B and whose edges are all edges of G with one endvertex in A and the other in B, and denote the density of G[A, B]

by dG(A, B) := e(G|A[A,B||B|]). We say that G[A, B] is (d, ε)-regular if dG(X, Y ) = d ± ε for every X ⊆ A and Y ⊆ B with |X| ≥ ε|A| and |Y | ≥ ε|B|, and we write that G[A, B] is (≥d, ε)-regular to mean that G[A, B] is (d′, ε)-regular for some d′ ≥ d. Also, we say that G[A, B] is (d, ε)-super-regular if G[A, B] is (≥d, ε)-regular, every vertex of A has at least (d − ε)|B| neighbours in B and every vertex of B has at least (d − ε)|A| neighbours in

![image 26](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile26.png>)

- A. The following well-known results are elementary consequences of the deﬁnitions.


- Lemma 2.1 (Slicing Lemma). For every d, ε, β > 0, if G[A, B] is (d, ε)-regular, and X ⊆ A and Y ⊆ B have sizes |X| ≥ β|A| and |Y | ≥ β|B|, then G[X, Y ] is (d, ε/β)regular.
- Lemma 2.2. For every d, ε > 0 with ε < 21, if G[A, B] is (≥d, ε)-regular, then there are sets X ⊆ A and Y ⊆ B with sizes |X| ≥ (1 − ε)|A|, and |Y | ≥ (1 − ε)|B| such that G[X, Y ] is (d, 2ε)-super-regular.


![image 27](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile27.png>)

We make use of Chernoﬀ bounds on the concentration of binomial and hypergeometric distributions in the following form. Theorem 2.3 ([7, Corollary 2.3 and Theorem 2.10]). Suppose X has binomial or hypergeometric distribution and 0 < a < 3/2. Then P(|X − EX| ≥ aEX) ≤ 2e−

a2

3 EX.

![image 28](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile28.png>)

The following lemma is similar to lemmas of Csaba and Mydlarz [3, Lemma 14] and Martin and Skokan [13, Lemma 10]. It states that if we randomly select a collection of disjoint subsets from each of the vertex classes of a super-regular pair, every pair of sets from diﬀerent classes is super-regular with high probability.

- Lemma 2.4 (Random Slicing Lemma). Suppose that 1/n ≪ β, ε ≪ d. Let G[A, B] be (d, ε)-super-regular (respectively (d, ε)-regular) where |A|, |B| ≤ n and let x1, . . ., xs and y1, . . ., yt be positive integers each of size at least βn such that i∈[s] xi ≤ |A| and


j∈[t] yj ≤ |B|. If {X1, . . ., Xs} is a collection of disjoint subsets of A and {Y1, . . ., Yt} is a collection of disjoint subsets of B such that |Xi| = xi and |Yj| = yj for all i ∈ [s] and j ∈ [t] selected uniformly at random from all such collections, then, with probability at least 1−e−Ω(n), G[Xi, Yj] is (d, ε′)-super-regular (respectively (d, ε′)-regular) for all i ∈ [s] and j ∈ [t], where ε′ := (33ε)1/5.

For completeness we present a proof of Lemma 2.4 in the Appendix. To make use of regularity properties, we apply the degree form of Szemer´edi’s Regularity Lemma (see [11,

- Theorem 1.10]).
- Theorem 2.5 (Degree form of Szemer´edi’s Regularity Lemma). For every ε > 0, real number d ∈ [0, 1] and integers t and q there exists integers n0 and T such that the following statement holds. Let G be a graph on n ≥ n0 vertices, and let U1, . . ., Uq be a partition of V (G) into q parts. Then there is a partition of V (G) into an exceptional set V0 and k clusters V1, . . ., Vk, and a spanning subgraph G′ ⊆ G such that


- (a) t ≤ k ≤ T,
- (b) |V1| = |V2| = . . . = |Vk| and |V0| ≤ εn,
- (c) for every i ∈ [k] there exists j ∈ [q] such that Vi ⊆ Uj,
- (d) dG′(v) ≥ dG(v) − (ε + d)n for all v ∈ V (G),
- (e) e(G′[Vi]) = 0 for all i ∈ [k], and
- (f) for each distinct i, j ∈ [k] either G′[Vi, Vj] is (≥d, ε)-regular or G′[Vi, Vj] is empty. Theorem 2.5 as stated above is stronger than the form given in [11] in that it allows


us to specify an initial partition of V (G) and to insist that the clusters V1, V2, . . ., Vk are each a subset of some part of this partition (property (c) above). However, this statement follows from the same proof, which proceeds iteratively by alternately reﬁning a partition of V (G) and deleting some vertices of V (G) (which are then placed in the exceptional set V0). So to prove Theorem 2.5 we take our speciﬁed partition as the initial partition of this process.

### 2.2 Robustly-matchable sets

The following application of the regularity lemma is critical to the entire proof. Given a graph G, a small A ⊆ V (G) and a small matching B ⊆ E(G), we form an auxiliary bipartite graph F with vertex set A ∪ B in which there is an edge between a ∈ A and bc ∈ B if and only if abc is a triangle in G. So matchings in F correspond to triangletilings in G. In this setting, Lemma 2.6 allows us to choose subsets X ⊆ A and Y ⊆ B such that if we can ﬁnd a triangle-tiling in G that covers every vertex of G except for the vertices incident to edges in Y and exactly |Y | of the vertices in X, then we obtain a perfect triangle-tiling in G.

- Lemma 2.6. Suppose that 1/n ≪ φ ≪ ε ≪ d. Let F be a bipartite graph with vertex


classes A and B such that n/10 ≤ |A|, |B| ≤ n and dF(A, B) ≥ d. Then there exist subsets X ⊆ A and Y ⊆ B of sizes |X| = φn and |Y | = (1 − ε)φn such that F[X′, Y ] contains a perfect matching for every subset X′ ⊆ X with |X′| = |Y |.

Proof. Let n0 and T be the integers returned by Theorem 2.5 given inputs ε, d′ := d/200 and t = q = 2. We may assume that φ ≤ 1/4T. We use Theorem 2.5 with initial partition U1 = A and U2 = B to obtain a spanning subgraph F′ ⊆ F and a partition of V (F) into sets V0, V1, . . ., Vk which satisfy properties (a)–(f) of Theorem 2.5. In particular, by Theorem 2.5(d) at most (ε + d/200)n2 edges of F are not edges of F′. Also, by Theorem 2.5(e) there are no edges in F′[Vi] for any i ∈ [k], and since |V0| ≤ εn by Theorem 2.5(b), at most εn2 edges of F contain a vertex of V0. Since

e(F) = dF(A, B)|A||B| ≥ d

n 10

![image 29](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile29.png>)

d 200

2

> ε +

![image 30](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile30.png>)

n2 + εn2,

there must exist distinct i, j ∈ [k] such that F′[Vi, Vj] is non-empty, and since F is bipartite, by Theorem 2.5(c) we may assume without loss of generality that Vi ⊆ A and Vj ⊆ B. Observe that F′[Vi, Vj] is (≥d′, ε)-regular by Theorem 2.5(f). Write m for the common size of Vi and Vj, so m = |V (F)\V0|/k ≥ n/2T ≥ 2φn by Theorem 2.5(a) and (b). By Lemma 2.2 we may delete at most εm vertices from each of Vi′ and Vj′ to obtain subsets Vi′ ⊆ Vi and Vj′ ⊆ Vj such that F[Vi′, Vj′] is (d′, 2ε)-super-regular. Having done so, choose X ⊆ Vi′ and Y ⊆ Vj′ uniformly at random with sizes φn and (1 − ε)φn respectively (this is possible since |Vi′|, |Vj′| ≥ (1 − ε)m ≥ φn). Then Lemma 2.4 tells us that F′[X, Y ] is (d′, ε′)-super-regular with high probability, where ε′ := (66ε)1/5, so we may ﬁx sets X and Y with this property. It then follows that every vertex of X has at least (d′ − ε′)|Y | ≥ ε′|X| neighbours in Y , whilst every set of at least ε′|X| vertices of

- X has at least (1 − ε′)|Y | ≥ (1 − 2ε′)|X| neighbours in Y (where we say that a vertex y is a neighbour of a set X′ if y is a neighbour of some element of X′). Finally, since every vertex of Y has at least (d′ − ε′)|X| > 2ε′|X| neighbours in X, every set of at least (1 − 2ε′)|X| vertices of X has every vertex of Y as a neighbour. So Hall’s criterion is satisﬁed for every X′ ⊆ X of size |X′| ≤ |Y |, so for every X′ ⊆ X with |X′| = |Y | there is a perfect matching in F′[X′, Y ].


![image 31](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile31.png>)

![image 32](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile32.png>)

![image 33](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile33.png>)

![image 34](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile34.png>)

### 2.3 Spanning bounded degree trees

Our proof requires us to ﬁnd a spanning tree of bounded maximum degree in the reduced graph R of G. For this, we use the following theorem of Win [15].

Theorem 2.7. If k ≥ 2 and R is a connected graph such that

d(v) ≥ |R| − 1 for every independent set S of size k,

v∈S

then R contains a spanning tree T such that ∆(T) ≤ k. In particular, if R is a connected graph with δ(R) ≥ (|R| − 1)/k, then R contains a spanning tree T with maximum degree at most k.

### 2.4 Fractional weighted matchings via linear programming

In our proof of Theorem 1.2, we will consider regular pairs of clusters of vertices of G and use the regularity of each pair to ﬁnd a triangle-tiling covering a given proportion of vertices from each cluster. We want to choose these proportions so that collectively these triangle-tilings cover (almost) all of the vertices of G. To do this we look for a generalized form of weighted matching in the reduced graph; the proportion of vertices to be covered by a triangle-tiling within a pair of clusters then corresponds to the weight in this matching of the corresponding edge of the reduced graph.

A fractional matching w in a graph G assigns a weight we ≥ 0 to each edge e ∈ E(G) such that for every vertex u ∈ V (G) we have e∋u we ≤ 1. In other words, if we consider each edge uv to place weight wuv at each of u and v, then the the combined weight placed at each vertex is at most one. This is a relaxation of an integer matching M, in which we insist that for each e ∈ E(G) we have we = 1 (meaning that e ∈ M) or we = 0 (meaning that e ∈/ M). Here we work with a more general notion of an (η, ξ)-weighted fractional matching, in which we consider each edge to place diﬀerent weights at each end, subject to the restriction that the ratio of these weights is at most η : ξ. It is most natural to express these matchings in terms of directed graphs, as we can then consider a directed edge −→uv of weight w−→uv to place weight ηw−→uv on its tail u and weight ξw−→uv on its head v;

- as before, we insist that the combined weight placed at each vertex is at most one.


Deﬁnition 2.8. Let Γ be a directed graph on n vertices and let η and ξ be positive real numbers. An (η, ξ)-weighted fractional matching w in Γ is an assignment of a weight w−→uv ≥ 0 to each edge −→uv of Γ such that for every vertex u ∈ V (Γ) we have

ξw−→vu ≤ 1. (1)

ηw−→uv +

v∈NΓ+(u)

v∈NΓ−(u)

The total weight of w is deﬁned to be W := −→uv∈E(Γ)(η +ξ)w−→uv. By (1) we have W ≤ n; we say that w is perfect if W = n. Note that in this case we have equality in (1) for every vertex.

Given an undirected graph G, we consider (η, ξ)-weighted fractional matchings in the directed graph Γ formed by replacing every edge uv of G with both a directed edge −→uv from u to v and a directed edge −→vu from v to u. In particular, a (21, 21)-weighted fractional matching w in Γ then corresponds to a fractional matching w′ in G (in the standard notion of fractional matching as deﬁned above). Indeed, given w, for each edge e = uv ∈ E(G) we may take we′ = w−→uv +w−→vu. In our proof we will instead consider (η, ξ)weighted fractional matchings in Γ where ξ is close to twice as large as η. The advantage

![image 35](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile35.png>)

![image 36](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile36.png>)

of this is shown by Lemma 2.10, which states that the minimum degree condition on G needed to guarantee the existence of a perfect (η, ξ)-weighted fractional matching in Γ is then approximately n/3, well below the n/2 threshold needed to guarantee the existence of a perfect fractional matching in G.

Let Γ be a directed graph on n vertices v1, . . ., vn, and ﬁx η, ξ > 0. Then we deﬁne the (η, ξ)-weighted characteristic vector of an edge −→uv ∈ E(Γ) to be the vector χη,ξ(−−→vivj) ∈ Rn whose ith coordinate is equal to η, whose jth coordinate is equal to ξ, and in which all other coordinates are equal to zero. So an assignment w of non-negative weights to edges of Γ is an (η, ξ)-weighted fractional matching in Γ if and only if

w−−→vivjχη,ξ(−−→vivj) ≤ 1, (2)

−−→vivj∈E(Γ)

where 1 is the vector in Rn with each coordinate equal to 1 and the inequality is treated pointwise. As before, w is perfect if and only if we have equality for each coordinate.

To prove the existence of a (η, ξ)-weighted fractional matching in a directed graph of high minimum indegree, we use the following version of Farkas’ Lemma, for which we need the following deﬁnition; a vertex v ∈ Rn is a weighted sum of vectors in X = {x1, . . ., xm} ⊆ Rn if

v ∈

m

λixi : λi ≥ 0 for every i ∈ [m] ,

i=1

otherwise v is not a weighted sum of the vectors in X.

- Lemma 2.9 (Farkas’ Lemma). For every v ∈ Rn and every ﬁnite X ⊆ Rn, if v is not a weighted sum of the vectors in X, then there exists y ∈ Rn such that y · x ≥ 0 for every

- x ∈ X and y · v < 0. We now give the main result of this section.


- Lemma 2.10. For every η > 0, every directed graph Γ on n vertices with δ−(Γ) ≥ ηn admits a perfect fractional (η, 1 − η)-matching. Furthermore, if η = p/q for positive integers p and q, then we can assume that the weights of the matching are rational numbers with common denominator D bounded above by some function of p, q and n.


Proof. Let v1, . . ., vn be an arbitrary ordering of the vertices of Γ. Then by (2), a perfect (η, 1−η)-weighted fractional matching in Γ corresponds to a weighted sum of the vectors in

X := {χη,1−η(−−→vivj) : −−→vivj ∈ E(Γ)} that equals 1.

If we assume that Γ does not have a perfect (η, 1 − η)-weighted fractional matching, then, by Farkas’ lemma (Lemma 2.9), as 1 is not a weighted sum of the vectors in X, there exists a vector y ∈ Rn such that y · 1 < 0 but y · χη,1−η(−−→vivj) ≥ 0 for every −−→vivj ∈ E(Γ). By reordering the vertices if necessary, we may assume that y1 ≥ . . . ≥ yn. Let i be maximal such that −−→vivn ∈ E(Γ), so i ≥ δ−(Γ) ≥ ηn. Then,

- i
- j=1


- 0 > y · 1 =


yj +

n

yj ≥ iyi + (n− i)yn ≥ ηnyi + (1 − η)nyn = ny · χη,1−η(−−→vivn) ≥ 0,

j=i+1

a contradiction.

The second statement is implied by basic linear programming theory, if we take the perfect fractional (η, 1 − η)-matching to be one with the smallest possible number of non-zero weights, as then w is a basic feasible solution.

![image 37](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile37.png>)

![image 38](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile38.png>)

![image 39](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile39.png>)

![image 40](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile40.png>)

Note that if a directed graph Γ admits a perfect (η, ξ)-weighted fractional matching w with η ≤ ξ and η + ξ = 1, then α(Γ) ≤ ξn, because for every independent set A in Γ we have

 

  ≤ ξ

 

  ≤ ξW ≤ ξn,

|A| =

ηw−→

ab +

ξw−→

w−→

ab +

w−→

ba

ba

a∈A

a∈A

b∈N+(a)

b∈N+(a)

b∈N−(a)

b∈N−(a)

where the initial equality holds since we have equality in (1), and the penultimate inequality holds because (since A is an independent set) every edge of Γ contributes at most once to the sum. This shows that the minimum indegree condition of Lemma 2.10 is best possible for η ≤ 1/2, since weaker conditions do not preclude the existence of independent sets of size greater than (1 − η)n.

## 3 Triangle-tilings in regular pairs and triples

Loosely speaking, the proof of Theorem 1.2 proceeds by iteratively constructing a triangletiling in G which covers all of the vertices outside of a small ‘core’ subset of vertices but leaves most vertices inside this ‘core’ uncovered. This gives a perfect triangle-tiling in G, because the ‘core’ is robust in the sense that it has a perfect triangle-tiling after the removal of any suﬃciently small set of vertices (provided that the number of vertices remaining is divisible by 3). Depending on the structure of the graph G, this ‘core’ will either consist of sets A and B which form a super-regular pair with density greater than

- 1

![image 41](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile41.png>)

- 2, or of sets A, B and C which form three super-regular pairs each with density bounded below by a small constant.


We begin with the case where the ‘core’ consists of a super-regular pair of density

greater than 12 (part (c) of Lemma 3.1). Let G be a graph whose vertex set is the disjoint union of sets A and B. Recall that a triangle T in G is an A-triangle if T contains two

![image 42](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile42.png>)

- vertices of A and one vertex of B, and likewise that T is a B-triangle if T contains two
- vertices of B and one vertex of A.


- Lemma 3.1. Suppose that 1/n ≪ γ ≪ ε ≪ φ, ε′ ≪ d ≪ ω. Let A and B be disjoint sets of vertices with n/3 + ωn ≤ |A|, |B| ≤ 2n/3 − ωn and |A ∪ B| = n, and let G be a graph on vertex set V := A ∪ B with α(G) ≤ γn. Then the following statements hold.


- (a) If G[A, B] is (≥ d, ε)-regular then G admits a triangle-tiling covering all but at most 2εn vertices of G. Moreover, for every a and b with 2a + b ≤ |A| − εn and

- a + 2b ≤ |B| − εn there is a triangle-tiling in G which consists of a A-triangles and
- b B-triangles.


- (b) If G[A, B] is (d, ε)-super-regular then, provided |A \ S| + |B| + ⌊φε′n⌋ is divisible by 3, for every S ⊆ A of size |S| = φn there is a triangle-tiling in G which covers every vertex of G[V \ S] and which covers precisely ⌊φε′n⌋ vertices of S.


- (c) If n is divisible by 3 and G[A, B] is (1/2 + d, ε)-super-regular then G contains a perfect triangle-tiling.


Proof. For (a) the triangles may be chosen greedily. Indeed, suppose that we have already chosen a triangle-tiling T consisting of at most a A-triangles and at most b B-triangles, then T covers at most 2a + b vertices of A, and at most a + 2b vertices of B. Taking

- A′ = A \ V (T ) and B′ = B \ V (T ), we ﬁnd that |A′|, |B′| ≥ εn. Since G[A, B] is


(≥d, ε)-regular it follows that dG(A′, B′) ≥ d − ε, therefore some vertex x ∈ A′ has at least (d − ε)|B′| ≥ (d − ε)εn > γn neighbours in B′. Since α(G) ≤ γn it follows that some two of these neighbours are adjacent, giving a B-triangle which can be added to T . The same argument with the roles of A′ and B′ reversed yields instead an A-triangle which may be added to T . This proves the second statement of (a); the ﬁrst follows by setting a = 31(2|A| − |B| − εn) and b = 13(2|B| − |A| − εn).

![image 43](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile43.png>)

![image 44](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile44.png>)

Next, for (b), let z := ⌊φε′n⌋, t4 := ⌊z/2⌋ and z′ := z − 2t4 ∈ {0, 1}, so we will construct a triangle-tiling that covers all of (A\S)∪B and exactly z = 2t4+z′ vertices of S. Let B1′ ⊆ B consist of all vertices in B with fewer than (d−φε)|S| neighbours in S; since G[S, B] is (≥d, φε)-regular we have |B1′| ≤ φεn. Form B1 by adding at most 2 arbitrarily selected vertices from B \ B1′ to B1′ so that |B \ B1| − t4 is divisible by 3. Since G[A, B] is (d, ε)-super-regular, every vertex of B1 has at least (d − ε)|A| − |S| ≥ dn3 > 2|B1| + γn neighbours in A \ S. Since α(G) ≤ γn, we may greedily form a triangle-tiling T1 of A-triangles in G of size |B1| which covers every vertex of B1 and does not use any vertex from S. We now select uniformly at random a subset B2 ⊆ B \B1 of size |B2| = t4. Since every vertex in A has at least (d − ε)|B| − |B1| ≥ dn3 neighbours in B \ B1, Theorem 2.3 implies that, with probability 1 − o(1), every vertex of A has at least φε

![image 45](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile45.png>)

![image 46](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile46.png>)

![image 47](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile47.png>)

![image 48](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile48.png>)

![image 49](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile49.png>)

′d

7 n neighbours in

![image 50](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile50.png>)

- B2. Fix a choice of B2 for which this event occurs. Let S′ be an arbitrarily selected subset


- of S of size z′ (so S′ is either empty or a singleton) and let A′ := (A \ (S ∪ V (T1))) ∪ S′ and B′ := B \(B1 ∪B2). Recall that, by assumption, |A\S|+|B|+z is divisible by 3, so


|A′| + |B′| = |A \ S| + z′ + |B| − |B2| − |V (T1)| = (|A \ S| + |B| + z) − (3t4 + |V (T1)|) is divisible by 3. Since |B′| is divisible by 3 by our selection of B1 and B2, it follows that |A′| is divisible by 3 as well. Let t3 = φε

′d

15 n , a := 23|A′|−13|B′| and b := 23|B′|−13|A′|−t3. Since G[A′, B′] is (≥d, 2ε)-regular, (a) implies that there is a triangle-tiling T2 in G[A′∪B′] such that A′′ := A′\V (T2) and B′′ := B′\V (T2) have sizes precisely |A′′| = |A′|−(2a+b) = t3 and |B′′| = |B′| − (a + 2b) = 2t3. Since by the choice of B2 each vertex of A′′ has

![image 51](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile51.png>)

![image 52](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile52.png>)

![image 53](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile53.png>)

![image 54](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile54.png>)

![image 55](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile55.png>)

![image 56](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile56.png>)

′d

- at least φε


7 n > 2|A′′| + γn neighbours in B2, we may greedily form a triangle-tiling T3 in G[A′′ ∪ B2] consisting of exactly t3 B-triangles which covers every vertex of A′′ and which covers precisely 2t3 vertices of B2. At this point we have obtained a triangle-tiling T1 ∪ T2 ∪ T3 in G which covers every vertex of A except for those in S \ S′ and every vertex of B except for the precisely 2t3 vertices in B′′ and the precisely t4−2t3 vertices in B2\V (T3). Therefore, in total, precisely t4 vertices of B remain uncovered, each of which has at least (d − φε)|S| − |S′| > 2|B2| + γn neighbours in S \ S′ by the choice of B1. We may therefore greedily form a triangle-tiling T4 of A-triangles in G which covers all the remaining uncovered vertices in B and precisely 2t4 vertices of S\S′. Then T1∪T2∪T3∪T4 is the claimed triangle-tiling.

![image 57](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile57.png>)

![image 58](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile58.png>)

Finally, since none of the assumptions for (c) involve φ or ε′, we may assume that φ ≪ ε′. We also assume without loss of generality that |B| ≥ |A|. Since α(G) ≤ γn,

we may greedily form a matching M of size at least (|B| − γn)/2 ≥ n/10 in G[B]. Fix such a matching M, and form an auxiliary bipartite graph H with vertex classes A and M where a ∈ A and e = xy ∈ M are adjacent if and only if xyz is a triangle in G. Note that for every edge e = xy ∈ M we have that

degH(e) = |NG(x) ∩ NG(y) ∩ A| ≥ 2((1/2 + d) − ε)|A| − |A| ≥ d|A|,

so H has density at least d. By Lemma 2.6, applied to H with ε′ here in place of ε there, we may choose subsets X ⊆ A and M′ ⊆ M such that |X| = φn, |M′| = (1 − ε)φn and such that H[X′, M′] contains a perfect matching for every subset X′ ⊆ X with |X′| = |M′|. Let B′ := B\V (M′) and n′ := |A|∪|B′|. Then, since we assumed that |B| ≥ |A|, we have n′/3 + ωn′ ≤ |A|, |B′| ≤ 2n′/3 − ωn′, so we can apply (b) to G[A ∪ B′] with A, B′ and X in place of A, B and S respectively to obtain a triangle-tiling T1 in G which covers every vertex of G except for the vertices of V (M′) and precisely (1 − ε′)φn vertices of X. So, taking X′ to be the vertices of X not covered by T1, we have |X′| = |M′|. By the choice of X and M′ it follows that H[X′, M′] contains a perfect matching, which corresponds to a perfect triangle-tiling T2 in G[X′ ∪ V (M′)]. This gives a perfect triangle-tiling T1 ∪ T2 in G.

![image 59](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile59.png>)

![image 60](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile60.png>)

![image 61](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile61.png>)

![image 62](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile62.png>)

We now turn to the case where the ‘core’ consists of three sets which form three super-regular pairs, for which the following lemma is analogous to Lemma 3.1.

- Lemma 3.2. Suppose that 1/n ≪ γ, ε ≪ d, ω, and that 3 divides n. Let V1, V2 and V3 be disjoint sets of vertices with |Vi| ≥ n/6 + ωn for each i ∈ [3] such that V := i∈[3] Vi has size |V | = n. Let G be a graph on vertex set V with α(G) ≤ γn such that G[Vi, Vj] is (d, ε)-super-regular for each distinct i, j ∈ [3]. Then G contains a perfect triangle-tiling.


To prove Lemma 3.2 we use the celebrated Blow-up Lemma of Koml´os, S´ark¨ozy and Szemer´edi [10] to obtain a perfect triangle-tiling. For simplicity, we state this only in the (very) special case that we use. Note that our deﬁnition of super-regularity diﬀers slightly from theirs, but it is not hard to show that the two deﬁnitions are equivalent up to some modiﬁcation of the constants involved (see, for example, [14, Fact 2]), so the validity of Theorem 3.3 is unaﬀected.

Theorem 3.3 (Blow-up Lemma for triangle-tilings). Suppose that 1/n ≪ ε ≪ d. Let

- A, B and C be disjoint sets of vertices with |A| = |B| = |C| = n, and let G be a graph on vertex set V := A ∪ B ∪ C such that G[A, B], G[B, C] and G[C, A] are each (d, ε)-superregular. Then G contains a perfect triangle-tiling.


The proof of Lemma 3.2 proceeds by iteratively deleting triangles from G with two vertices in one cluster and one in another cluster, until the same number of vertices remain in each cluster. We complete the proof by applying the Blow-up Lemma to obtain a perfect triangle-tiling covering all remaining vertices.

Proof of Lemma 3.2. Throughout this proof we perform addition on subscripts modulo 3. For each i ∈ [3], the fact that G[Vi, Vi+1] is (d, ε)-super-regular implies that each vertex v ∈ Vi has |N(v)∩Vi+1| ≥ (d−ε)|Vi+1| ≥ dn/6. So if we choose uniformly at random a set Zj ⊆ Vj of size ωn for each j ∈ [3], then |N(v) ∩ Zi+1| is hypergeometrically distributed with expectation at least dωn/6. By Theorem 2.3 the probability that v has fewer than

dωn/7 neighbours in |Zi+1| declines exponentially with n, and likewise the same is true of the probability that v has fewer than dωn/7 neighbours in |Zi+2|. Taking a union bound, with positive probability it holds that for each i ∈ [3] every vertex v ∈ Vi has at least dωn/7 neighbours in each of Zi+1 and Zi+2. We ﬁx such an outcome of our random selection of the sets Zj, and deﬁne Xi0 = Vi\Zi for each i ∈ [3]. Without loss of generality we may assume that n6 ≤ |X10| ≤ |X20| ≤ |X30| ≤ 23n − 3ωn.

![image 63](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile63.png>)

![image 64](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile64.png>)

We now proceed by an iterative process. At time step t ≥ 0, if we have |X1t| = |X2t| = |X3t| then we terminate. Otherwise, we choose a triangle xyz in G with x ∈ X2t and

- y, z ∈ X3t (we shall explain shortly why this will always be possible). We then set Yjt+1 := Xjt \ {x, y, z} for j ∈ [3] and deﬁne X1t+1, X2t+1 and X3t+1 such that {X1t+1, X2t+1, X3t+1} =


{Y1t+1, Y2t+1, Y3t+1} and |X1t+1| ≤ |X2t+1| ≤ |X3t+1|, before proceeding to the next time step t + 1.

Suppose that this procedure does not terminate prior to some time step T. Using the fact that 3 divides n it is easily checked that we must then have |X3t+2| − |X1t+2| ≤ |X3t| − |X1t| − 3 for each t ∈ [T − 2]. In other words, the size diﬀerence between the smallest and largest set decreases by at least 3 over each two time steps. Similarly we ﬁnd that |X1t| − |X1t+2| ≤ 1 for each t ∈ [T − 2], meaning that the smallest set size decreases by at most 1 over each two time steps. Furthermore, if at some time t we have 0 < |X3t| − |X1t| < 3, then (since 3 divides n) we must have |X1t| + 2 = |X2t| + 1 = |X3t|, whereupon the procedure will terminate at time t+1. It follows that the procedure must terminate at some time T, and moreover that

- 2

![image 65](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile65.png>)

- 3


T ≤

- 2

![image 66](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile66.png>)

- 3


|X30| − |X10| ≤

- 2n

![image 67](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile67.png>)

- 3


n 6

− 3ωn −

![image 68](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile68.png>)

n 3

− 2ωn.

=

![image 69](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile69.png>)

This implies that at each time t < T we have |X3t| ≥ |X2t| ≥ |X1t| ≥ |X10| − 2 t ≥ |X10| − T2 ≥ ωn, and so throughout the procedure it is always possible to pick a triangle

![image 70](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile70.png>)

![image 71](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile71.png>)

- as desired. Indeed, G[X2t, X3t] is (≥d, ε/ω)-regular by the Slicing Lemma (Lemma 2.1),


so some vertex of X2t has at least (d − ε/ω)|X3t| ≥ ωdn/2 neighbours in X3t. Since α(G) ≤ γn < ωdn/2 some two of these neighbours must be adjacent, giving the desired triangle.

After the procedure terminates, deﬁne Vi′ := XiT ∪ Zi for each i ∈ [3]. Then |V1′| = |V2′| = |V3′| ≥ 2ωn, so by Lemma 2.1 and our choice of the sets Zj it follows that G[Vi′, Vj′] is (dω/7, ε/2ω)-super-regular for each distinct i, j ∈ [3]. By Theorem 3.3 there is a

perfect triangle-tiling in G[ i∈[3] Vi′]; together with the triangles selected by the iterative procedure this gives a perfect triangle-tiling in G.

![image 72](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile72.png>)

![image 73](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile73.png>)

![image 74](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile74.png>)

![image 75](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile75.png>)

## 4 Proof of Theorem 1.2

In this section we prove Theorem 1.2. The following lemma is the central part of the proof, showing that if a graph G can be decomposed into clusters which form regular and super-regular pairs, indexed by a graph R which admits a bounded degree spanning tree, then by ‘working inwards’ from the leaves of the tree we can form a perfect triangle-tiling in G.

- Lemma 4.1. Suppose that 1/m ≪ γ ≪ 1/k ≪ ε ≪ d, ω. Let G be a graph whose vertex set is partitioned into k sets V1, . . ., Vk, and let R be a graph with vertex set [k] which


admits a spanning tree T of maximum degree at most 10. Suppose also that the following statements hold.

- (a) |V1| ≥ (1 − ε)m.
- (b) V1 admits either a partition into parts A1 and B1 with |A1|, |B1| ≥ (1/3+ω)|V1| such that G[A1, B1] is (1/2 + d, ε)-super-regular, or a partition into parts A1, B1 and C1 with |A1|, |B1|, |C1| ≥ (1/6 + ω)|V1| such that G[A1, B1], G[A1, C1] and G[B1, C1] are each (d, ε)-super-regular.
- (c) For each 2 ≤ i ≤ k, (1 − ε)m ≤ |Vi| ≤ m and Vi admits a partition into parts Ai and Bi with |Ai|, |Bi| ≥ (1/3 + ω)m such that G[Ai, Bi] is (d, ε)-super-regular.
- (d) If ij ∈ E(R), then at least m/5 vertices of Vi have at least dm/5 neighbours in Vj.
- (e) α(G) ≤ γm.


Then G contains a triangle-tiling covering all but at most two vertices of G.

Proof. Introduce new constants φ and ε′ with ε ≪ φ ≪ ε′ ≪ d and iterate the following process. Pick a leaf of T other than vertex 1, say vertex i, and let j be the neighbour of i in T. We will show that there exists a triangle-tiling in G[Vi ∪ Vj] that covers every vertex of Vi and at most 2φm vertices of Vj. We then delete the vertices covered by this tiling from G and delete vertex i from T. We proceed in this way until only vertex 1

- of T remains. We then arbitrarily delete at most two further vertices of V1 so that the number of remaining vertices in V1 is divisible by three. Since, at this point, we have removed at most 2φm · ∆(T) + 2 ≤ 21φm ≤ ε′m/7 vertices from V1, by (a), (b) and (e) there exists a bipartition or tripartition of the remaining vertices of V1 which satisﬁes the conditions of Lemma 3.1(c) or Lemma 3.2 respectively (with ω/2, ε′ and 2γ in place of ω, ε and γ respectively). In either case there is a perfect triangle-tiling in the graph induced


by the remaining vertices of V1, which together with the deleted triangle-tilings gives a triangle-tiling in G covering every vertex except for the at most two deleted vertices.

It therefore suﬃces to show that we can ﬁnd the desired triangle-tiling in G[Vi ∪ Vj]

- at each step of this process. To this end, let S′ be the set of vertices of Vi which have at least dm/6 neighbours in Vj. Observe that previous deletions can have removed at most 2φm · ∆(T) ≤ dm/30 vertices from each of Vi and Vj, so by (d) we have |S′| ≥ m/6, and by (c) the remaining vertices of Vi can be partitioned into parts Ai and Bi with |Ai|, |Bi| ≥ (1/3 + ω/2)m such that G[Ai, Bi] is (d, ε′)-super-regular. Without loss of generality we may assume that |S′ ∩ Ai| ≥ |S′ ∩ Bi|, so |S′ ∩ Ai| ≥ |S′|/2 ≥ m/12 and we can arbitrarily select S ⊆ S′ ∩ Ai of size φn. Now we may use Lemma 3.1(b) (again with ω/2, ε′ and 2γ in place of ω, ε and γ respectively) to ﬁnd a triangle-tiling T in G[Vi] which covers every vertex of Vi \ S. Since each uncovered vertex has at least dm/6 ≥ 2φm + γm neighbours in Vj, we may greedily extend T to a triangle-tiling T ′ in G which covers every vertex of Vi and which covers at most 2φm vertices of Vj.


![image 76](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile76.png>)

![image 77](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile77.png>)

![image 78](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile78.png>)

![image 79](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile79.png>)

It now suﬃces to show that for every graph G satisfying the conditions of Theorem 1.2, we can delete triangles and/or vertices from G to obtain a subgraph whose structure meets the conditions of Lemma 4.1. The following lemma shows how to do this under the additional assumption that G has no large sparse cut; this assumption is useful as it allows us to assume that the reduced graph R of G is connected, and so has spanning trees of bounded maximum degree. For this we make the following deﬁnition: given a

graph G and a partition {A, B} of V (G), we say that an edge of G is crossing if it has one endvertex in A and one endvertex in B.

- Lemma 4.2. For every ω, ψ > 0 there exist n0, γ > 0 such that the following statement holds. Let G be a graph on n ≥ n0 vertices with δ(G) ≥ n/3+ωn and α(G) ≤ γn. Suppose additionally that for every partition {A, B} of V (G) with |A|, |B| ≥ n/3 there are at least ψn2 crossing edges of G. Then G contains a triangle-tiling covering all but at most two vertices of G (so in particular, if 3 divides n then G contains a perfect triangle-tiling). Proof. Introduce new constants satisfying the following hierarchy:


1/n ≪ γ ≪ 1/D ≪ 1/T ≪ 1/t ≪ ε′ ≪ ε ≪ d ≪ ω, ψ.

Then we may assume that n and T are large enough to apply Theorem 2.5 with constants ε′/2, d, t and q = 1. We also assume without loss of generality that ω−1 is an integer, and deﬁne D′ := 30ω−1(D!). Let G be as in the statement of the lemma, and apply Theorem 2.5 to G to obtain a spanning subgraph G′ ⊆ G, an integer k′ with t ≤ k′ ≤ T,

- an exceptional set U0 of size at most ε′n/2 and clusters U1, . . ., Uk′ of equal size. We now remove at most D′ vertices from each cluster so that the number of remaining vertices in


each cluster is divisible by D′, and add all removed vertices to the exceptional set U0. Since the total number of vertices moved in this way is at most D′k′ ≤ 30ω−1(D!)T ≤ ε′n/2, and at most D′ ≤ ε′n/2T ≤ ε′/2|Ui| vertices are removed from each cluster Ui, by Lemma 2.1 the resulting partition of V (G) into U0, U1, . . ., Uk′ has the following properties.

- (i) |U0| ≤ ε′n and |U1| = |U2| = . . . = |Uk′| =: m′, where D′ divides m′.
- (ii) dG′(v) ≥ dG(v) − (ε′ + d)n ≥ n/3 + 2ωn/3 for all v ∈ V (G).
- (iii) e(G′[Ui]) = 0 for all i ∈ [k′].
- (iv) for each distinct i, j ∈ [k′] either G′[Ui, Uj] is (≥d, ε′)-regular or G′[Ui, Uj] is empty.


In particular (i) implies that (1 − ε′)n/k′ ≤ m′ ≤ n/k′. We form the reduced graph R on vertex set [k′] in the usual way, that is, with ij ∈ E(R) if and only if e(G′[Ui, Uj]) > 0. For each i ∈ [k′] the number of edges of G′ with an endvertex in Ui is at least m′(n/3+2ωn/3) by (ii). Also, by (iii) there is no edge in G′[Ui], and by (i) there are at most at most m′ε′n edges in G′[U0, Ui]. Since for each j ∈ [k′] there are at most (m′)2 edges in G′[Ui, Uj], it follows that

m′(n/3 + 2ωn/3) − m′ε′n (m′)2

δ(R) ≥

≥

![image 80](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile80.png>)

1 3

- 2ω

![image 81](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile81.png>)

- 3


− ε′

+

![image 82](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile82.png>)

n m′

≥

![image 83](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile83.png>)

1 3

ω 2

+

![image 84](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile84.png>)

![image 85](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile85.png>)

k′. (3)

Now consider a partition {AR, BR} of [k′] with |AR|, |BR| ≥ δ(R), and deﬁne A :=

- U0 ∪ i∈A


Ui and B := i∈[k′]\BR Ui. Then

R

|A|, |B| ≥ δ(R)m′ ≥

ω 2

1 3

+

![image 86](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile86.png>)

![image 87](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile87.png>)

(1 − ε′)n k′

n 3

k′ ·

≥

,

![image 88](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile88.png>)

![image 89](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile89.png>)

so by assumption G has at least ψn2 crossing edges. By (ii) at most (d + ε′)n2 edges of G are not in G′, and by (i) at most ε′n2 edges of G intersect U0, so G′ contains at least ψn2 − (d + ε′)n2 − ε′n2 > 0 crossing edges which do not intersect U0. Let Ui and Uj be clusters containing the endvertices of some such edge; then ij is a crossing edge

of R. In other words, for every partition {AR, BR} of [k′] with |AR|, |BR| ≥ δ(R) there is a crossing edge of R. Since every connected component of R has size at least δ(R), it follows that R is connected.

We now form a set V1 from which we shall form the ‘core’ set of vertices mentioned in the proof overview at the beginning of Section 3. Suppose ﬁrst that there exist i, j ∈ [k′] with d(G′[Ui, Uj]) ≥ 2/3. Then G′[Ui, Uj] is (≥3/5, ε′)-regular by (iv). In this case we deﬁne V1 := Ui ∪ Uj, and for convenience of notation later we deﬁne X1 := Ui and

- Y1 := Uj. Now suppose instead that d(G′[Ui, Uj]) < 2/3 for every i, j ∈ [k′], that is, that each G′[Ui, Uj] has at most 2(m′)2/3 edges. Then we have an extra factor of 2/3 in the denominator of the second term of (3), so we have δ(R) ≥ k′/2, and so R contains a triangle ijℓ by Mantel’s theorem. In this case we take V1 := Ui∪Uj ∪Uℓ and set X1 := Ui, Y1 := Uj, and Z1 := Uℓ. We deﬁne an auxiliary graph R0 to be the subgraph of R formed by deleting vertices i and j in the former case, and by deleting vertices i, j and ℓ in the latter case.


Since ω−1 is an integer, we may write η := 1/3 + ω/10 as a rational number with denominator L := 30 · ω−1. Let

−→ R0 be the directed graph formed from R0 by replacing

each edge by a pair of edges, one in each direction. Then by Lemma 2.10, we can ﬁnd a perfect (η, 1 − η)-weighted fractional matching w in

−→

R0 in which all weights are rational, and the least common denominator L′ of all weights is bounded above by a function of |V (R0)| and L, that is, a function of k′ and ω. Since k′ ≤ 1/T and we assumed that 1/D ≪ 1/T, ω, we may assume that L′ ≤ D, so L′ divides D!, and so D!w−→

ij is an integer for every

−→ R0. Deﬁne m := m′/D!, and observe that that since D′ = D!L divides m

−→ ij ∈

by (i), both m and ηm are integers.

We now partition each cluster not contained in V1 into parts of size ηm and (1 − η)m according to the weights in w, using the following probabilistic argument. For every

- i ∈ V (R0), we select a partition Ui of Ui uniformly at random from all such partitions


in which exactly j∈N+(i) D!w−→

ij sets are of size ηm and exactly j∈N−(i) D!w−→

ji sets are of size (1 − η)m. Since w is a perfect fractional (η, 1 − η)-weighted matching, by (1) we have

ji = D!m = m′ = |Ui|,

ij + (1 − η)m

D!w−→

D!w−→

ηm

j∈N+(i)

j∈N−(i)

so we can indeed partition Ui in this way. We also consider the two or three clusters contained in V1 to be partitioned into a single part. That is, for each i ∈ [k′] \ V (R0) we set Ui to be the trivial partition {Ui} of Ui. Now consider any edge ij ∈ E(R), and recall that G′[Ui, Uj] is (≥d, ε′)-regular by (iv), so by Lemma 2.41, with probability at least 1 − e−Ω(n) we have that G′[Ui′, Uj′] is (≥d, ε)-regular for every Ui′ ∈ Ui and for every Uj′ ∈ Uj. Taking a union bound over all of the at most k

′

2 edges of R we ﬁnd that with positive probability this property holds for every edge of R. Fix a choice of partitions Ui for i ∈ [k′] for which this is the case.

We now deﬁne another auxiliary graph R1 with vertex set i∈[k′] Ui in which, for each distinct i, j ∈ [k′], each X ∈ Ui and each Y ∈ Uj, there is an edge XY if and only if G′[X, Y ] is (≥d, ε)-regular. Observe that by our choice of partitions Ui the graph R1 is then a blow-up of R, formed by replacing each vertex i ∈ [k′] by a set of |Ui| vertices and

![image 90](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile90.png>)

1Note that m is much smaller than ε′m′ (since D is much larger than 1/ε′) so we must use the random slicing lemma (Lemma 2.4) here, as opposed to, say, the standard slicing lemma (Lemma 2.1).

replacing each edge ij ∈ E(R) by a complete bipartite graph between the corresponding sets. In particular, R1 is connected. Also note that for each distinct i, j ∈ [k′] with ij ∈/ E(R), each X ∈ Ui and each Y ∈ Uj, the graph G′[X, Y ] is empty by (iv).

−→ R0), we deﬁne sij := D! · w−→

−→ ij ∈ E(

ij. We then label sij of the sets in Ui of size ηm as Xij1, . . ., Xijsij and label sij of the sets in Uj of size (1 − η)m as Yij1, . . ., Yijsij. Since Ui has exactly j∈N+(i) sij sets of size ηm and exactly j∈N−(i) sji sets of size (1 − η)m, we may do this so that for each i ∈ [k′] each set in Ui is uniquely labelled. We now relabel the sets Xijℓ and Yijℓ for

Next, for every edge

−→ R0) and ℓ ∈ sij as X2, . . ., Xk

−→ ij ∈ E(

R0) wij = D!|V (R0)| since w is perfect, so k′ ≤ k ≤ D!k′. Then for each 2 ≤ ℓ ≤ k our choice of partition implies that G′[Xℓ, Yℓ] is (≥ d, ε)-regular; we deﬁne Vℓ := Xℓ ∪ Yℓ, and observe that |Vℓ| = m.

and Y2, . . ., Yk respectively, where k−1 := −→

R0) sij = D! −→

−→

−→

ij∈E(

ij∈E(

We now deﬁne a ﬁnal auxiliary graph R∗ with vertex set [k] in which ij is an edge of R∗ if and only if e(G′[Vi, Vj]) > 0. Observe that R∗ is then a contraction of R1, in which the vertices of R1 corresponding to the sets X1 and Y1 (and Z1 if deﬁned) are contracted to the single vertex 1 of R∗, and for 2 ≤ i ≤ k the vertices of R1 corresponding to Xi and Yi are contracted to the single vertex i of R∗. So, since R1 is connected, R∗ is connected also. Now suppose that ij is an edge of R∗. Since G′[Vi, Vj] is nonempty there must exist sets S ∈ {Xi, Yi, Zi} and T ∈ {Xj, Yj, Zj} such that G′[S, T] is non-empty (ignore Zi unless i = 1 and Z1 exists, and likewise for Zj). We then have S ∈ Ui′ and T ∈ Uj′ for some i′, j′ ∈ [k′], so ST is an edge of R1, and so G′[S, T] is (≥d, ε)-regular. Also, a similar calculation to (3) shows that we must have δ(R∗) ≥ k/3, so by Theorem 2.7 there is a spanning tree T in R∗ with ∆(T) ≤ 3.

To recap, at this point we have a formed a partition {U0, V1, . . ., Vk} of V (G) and a graph R∗ with vertex set [k] which contains a spanning tree of maximum degree at most 3, such that the following statements hold.

- (v) V1 admits either a partition {X1, Y1} with |X1| = |Y1| = m′ such that G′[X1, Y1] is (≥3/5, ε′)-regular, or a partition {X1, Y1, Z1} with |X1| = |Y1| = |Z1| = m′ such that G′[X1, Y1], G′[X1, Z1] and G′[Y1, Z1] are each (≥d, ε′)-regular.
- (vi) For each 2 ≤ i ≤ k, we have |Vi| = m and Vi admits a partition {Xi, Yi} with |Xi|, |Yi| ≥ ηm = (1/3 + ω/10)m such that G′[Xi, Yi] is (≥d, ε)-regular.
- (vii) If ij ∈ E(R∗), then there are sets S ⊆ Vi and T ⊆ Vj with |S| ≥ |Vi|/3 and |T| ≥ |Vj|/3 such that G′[S, T] is (≥d, ε)-regular.


If we are in the ﬁrst case of (v), then by Lemma 2.2 we may choose subsets A1 ⊆ X1 and B1 ⊆ Y1 with |A1|, |B1| ≥ (1−ε′)m′ such that G′([A1, B1]) is (3/5, 2ε′)-super-regular, and we then deﬁne W1 := A1 ∪ B1. If we are instead in the second case, by three applications of Lemma 2.2 we may choose subsets A1 ⊆ X1, B1 ⊆ Y1 and C1 ⊆ Z1

- with |A1|, |B1|, |C1| ≥ (1 − 2ε′)m′ such that G′([A1, B1]), G′([B1, C1]) and G′([C1, A1]) are each (d, 3ε′)-super-regular, and we then deﬁne W1 := A1 ∪ B1 ∪ C1. Next, for each 2 ≤ ℓ ≤ k, by (vi) and Lemma 2.2 we may choose subsets Aℓ ⊆ Xℓ and Bℓ ⊆ Yℓ with |Aℓ| ≥ (1 − ε)|Xℓ| and |Bℓ| ≥ (1 − ε)|Yℓ| such that G′[Aℓ, Bℓ] is (d, 2ε)-super-regular, and deﬁne Wℓ := Aℓ ∪ Bℓ. Finally, deﬁne W0 := U0 ∪ i∈[k] Vi \ Wi. Then {W0, W1, . . ., Wk} is a partition of V (G) and, since |Wi| ≥ (1 − ε)|Vi| for each i ∈ [k], we have |W0| ≤ 2εn.


Write W0 := {x1, . . ., xq}, so q ≤ 2εn. To complete the proof we greedily form a triangle-tiling T = {T1, . . ., Tq} such that xi ∈ Ti for each i ∈ [q] and |V (T ) ∩ Wj| ≤ 20ε|Wj| for each j ∈ [k]. To see that this is possible, suppose that we have already chosen triangles T1, . . ., Ts−1 for some s ∈ [q], let X := i∈[s−1] V (Ti) be the set of vertices covered by these triangles, and let the set X′ consist of all vertices in sets Wi with |X ∩ Wi| ≥ 18ε|Wi| (that is, from which the previously-chosen triangles cover more than a 18ε-proportion of the vertices). Then we have 18ε|X′| ≤ |X| ≤ 3q ≤ 6εn, so |X′| ≤ n/3, and so xs has at least δ(G) − |X| − |X′| − |W0| ≥ ωn − 10εn ≥ ωn/2 neighbours not in X, X′ or W0, so (since α(G) ≤ γn < ωn/2) two of these neighbours must be adjacent, giving the desired triangle Ts containing xs. Having chosen Ts in this way for every s ∈ [q] to obtain T , observe that since we chose each Ts to avoid every set Wi from which at least 18ε|Wi| vertices were covered by previously-chosen triangles, we must have |V (T ) ∩ Wi| ≤ 20ε|Wi| for each i ∈ [k], as desired.

Finally, for each i ∈ [k] deﬁne A′i := Ai \ V (T ), Bi′ := Bi \ V (T ), Vi′ := Wi \ V (T ). Also deﬁne V ′ := V (G)\V (T ) and H := G[V ′]. We claim that the graphs H and R∗ and the partition {V1′ . . ., Vk′} of V (H) meet the properties of Lemma 4.1 with ε∗ := 200ε, ω′ := ω/20 and γ′ := 2γk′(D!) in place of ε, ω and γ respectively and with m, d and k playing the same role there as here. Indeed, our constant hierarchy allows us to assume that 1/m ≪ γ′ ≪ 1/k ≪ ε∗ ≪ d ≪ ω′, as required. Also observe that for each i ∈ [k] we have |Vi′| ≥ |Vi| − 20ε|Vi| − ε|Vi| = (1 − 21ε)|Vi|, so certainly |Vi′| ≥ (1 − ε∗)m for each i ∈ [k]. So Lemma 4.1(a) holds, and Lemma 4.1(b) and (c) follow immediately from our choice of sets Aℓ and Bℓ (and possible C1). Also, for each ij ∈ E(R∗) by (vii) there exist sets S ⊆ Vi′ and T ⊆ Vj′ with |S| ≥ |Vi′|/4 and |T| ≥ |Vj′|/4 such that G′[S, T] is (≥d, 2ε)-regular, which implies that at least (1−2ε)|S| ≥ m/5 vertices in S have at least

- (d − 2ε)|T| ≥ dm/5 neighbours in T, so Lemma 4.1(d) holds. Last of all, Lemma 4.1(e) holds since α(H) ≤ α(G) ≤ γn ≤ γ(2k′m′) = γ′m. So we may apply Lemma 4.1 to obtain a triangle-tiling covering all but at most two vertices of H; together with T this yields a triangle-tiling in G covering all but at most two vertices.


![image 91](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile91.png>)

![image 92](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile92.png>)

![image 93](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile93.png>)

![image 94](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile94.png>)

Finally, to complete the proof of Theorem 1.2 it remains only to consider graphs G which admit a large sparse cut. In this case we show that can remove a small number of vertices to obtain two vertex-disjoint subgraphs GA and GB of G whose vertex sets partition V (G) and each of which satisﬁes a stronger minimum degree condition. We then apply Theorem 1.1 to obtain a perfect triangle-tiling in each of GA and GB (alternatively, one could note that the stronger minimum degree conditions preclude either GA or GB from having a large sparse cut and apply Lemma 4.2).

Proof of Theorem 1.2. Fix ω > 0 and choose n0 suﬃciently large and γ suﬃciently small for Lemma 4.2 with ω2/40 in place of ψ and also so that we can apply Theorem 1.1 with ω/2, n0/3 and 3γ in place of ω, n0 and γ respectively. Now let G be a graph on n ≥ n0 vertices with δ(G) ≥ n/3 + ωn and α(G) ≤ γn. If for every partition {A, B} of V (G) with |A|, |B| ≥ n/3 there are at least ω2n2/40 crossing edges of G, then G contains a triangle-tiling covering all but at most two vertices by Lemma 4.2, so we are done. So we may assume that some partition {A, B} of V (G) with |A|, |B| ≥ n/3 has fewer than ω2n2/40 crossing edges. Fix such a partition with the smallest number of crossing edges. Note that we cannot have |A| ≤ n/3 + 1, as then there would be at least |A|(δ(G) − n/3 − 1) ≥ (n/3) · (ωn − 1) ≥ ωn2/4 crossing edges. It follows that every

vertex x ∈ A lies in at most deg(x)/2 crossing edges, as otherwise moving a from A to

- B would yield a partition of V (G) with parts of size at least n/3 and with fewer crossing edges. So we must have δ(G[A]) ≥ δ(G)/2 ≥ n/6 + ωn/2, and the same argument with


- B in place of A shows that δ(G[B]) ≥ n/6 + ωn/2. Our proof now diverges according to whether we are proving conclusion (a) or conclu-


sion (b) of Theorem 1.2. For conclusion (a) we simply choose arbitrarily a set S of at most four vertices of G so that |A \ S| and |B \ S| are each divisible by 3. For conclusion (b) we instead use our additional assumptions that G has no divisibility barrier and that 3 divides n. Indeed, the latter implies that we must have one of the following three cases:

- (a) |A| ≡ |B| ≡ 0 (mod 3). In this case we take S = ∅.
- (b) |A| ≡ 1 (mod 3) and |B| ≡ 2 (mod 3). Since (A, B) is not a divisibility barrier, either G contains an B-triangle or a pair of vertex-disjoint A-triangles, and we take S to be the vertices covered by some such triangle or pair of triangles.
- (c) |A| ≡ 2 (mod 3) and |B| ≡ 1 (mod 3). Since (B, A) is not a divisibility barrier, either G contains an A-triangle or a pair of vertex-disjoint B-triangles, and we take S to be the vertices covered by some such triangle or pair of triangles.


Observe that in all cases we have |S| ≤ 6 and that both |A \ S| and |B \ S| are divisible by 3. The remaining part of the proof is the same for both cases.

Let XA ⊆ A consist of all vertices of A with degG[A](x) < n/3 + ωn/2. Then each vertex of XA is contained in more than ωn/2 crossing edges, and since there are at most ω2n2/40 crossing edges in total, each with one vertex in A, it follows that |XA| ≤ ωn/20. Since α(G) ≤ γn and δ(G[A]) ≥ n/6 ≥ 2|XA|+|S|+γn we may greedily form a triangletiling TA of size at most |XA| in G[A] which covers every vertex of XA but which does not intersect S. We then deﬁne A′ := A\(V (TA)∪S), GA := G[A′] and nA := |A′|. Then δ(GA) ≥ n/3+ωn/2−|V (TA)|−|S| ≥ n/3+ωn/3, so n/3+ωn/3 ≤ nA ≤ 2n/3. It follows that GA is a graph on nA vertices with δ(GA) ≥ nA/2+ωnA/2 and α(GA) ≤ γn ≤ 3γnA. Also nA is divisible by 3 (since 3 divides each of |A \ S| and |V (TA)|), so GA contains a perfect triangle-tiling TA′ by Theorem 1.1.

By exactly the same argument with B in place of A we obtain a triangle-tiling TB in G[B] and a graph GB on vertex set B′ := B \ (V (TB) ∪ S) which contains a perfect triangle-tiling TB′. Finally, for conclusion (a) observe that T := TA ∪TB ∪TA′ ∪TB′ is then a triangle-tiling in G covering all vertices outside S, that is, all but at most four vertices of G, and for conclusion (b) note that adding the triangle or triangles covering S to T gives a perfect triangle-tiling in G.

![image 95](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile95.png>)

![image 96](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile96.png>)

![image 97](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile97.png>)

![image 98](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile98.png>)

## 5 Constructions and questions

Many of the ideas of this section are due to Balogh, Molla and Sharifzadeh [2], but we include them here for completeness. In the following constructions, we call an n-vertex triangle-free graph with sublinear independence number and minimum degree ω(1) an Erd˝s graph, which we denote by ER(n).2

To show that the minimum degree conditions of Theorem 1.2 and Corollary 1.4 are asymptotically tight, we use the Erd˝os graph to form a graph G on n vertices with a space

![image 99](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile99.png>)

2 Strictly speaking, for any ﬁxed n, both ER(n) and BE(n) (deﬁned shortly) are families of graphs.

barrier, δ(G) ≥ n/3+ω(1) and α(G) = o(n). We form G by taking the complete bipartite graph whose vertex classes U and V have sizes 2n/3+1 and n/3−1 respectively, and then placing copies of ER(|U|) and ER(|V |) on U and V respectively. The graph G formed in this way has δ(G) ≥ n/3 + ω(1) and sublinear independence number. Furthermore, G is K5-free since G[U] and G[V ] are each triangle-free and, because U is a space barrier, G has no perfect triangle-tiling.

The previous example can be modiﬁed slightly to give lower bounds for the following question.

- Question 5.1. Let k ≥ 4 and let G be an n-vertex graph with α(G) = o(n). What is the best-possible minimum degree condition on G that guarantees a perfect Kk-tiling in G?

The construction is slightly diﬀerent depending on the parity of k ≥ 4. We start with the odd case, so let k = 2(ℓ−1)+1 for some integer ℓ ≥ 3. Consider the complete ℓ-partite graph with one part V1 of size n/k−1, another part V2 of size 2n/k+1 and the remaining parts V3, . . ., Vℓ each of size 2n/k, and place the Erd˝os graph ER(|Vi|) on each of the parts Vi. When k = 2ℓ for some integer ℓ ≥ 1, the construction is essentially the same but we have one part of size 2n/k + 1, one part of size 2n/k − 1 and the remaining parts are each of size 2n/k. In either case we obtain a graph G with δ(G) ≥ 1 − k2 n + ω(1), sublinear independence number and no Kk-factor. It is worth noting that in the odd case the graph G is Kk+2-free and in the even case G contains no Kk+1.

![image 100](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile100.png>)

We feel that the following is another interesting related question.

- Question 5.2. Let G be an n-vertex K4-free graph with α(G) = o(n). What is the bestpossible minimum degree condition on G that guarantees a perfect triangle-tiling in G?


We use a modiﬁed version of the Bollob´s-Erd˝os graph [1] to construct a K4-free graph without a perfect triangle-tiling and with high minimum degree. For every large even n, the Bollob´s-Erd˝os graph is an n-vertex, K4-free graph with sublinear independence number, which we denote by BE(n). The vertex set of BE(n) is the disjoint union of two sets V1 and V2 of the same order such that the graphs G[V1] and G[V2] are triangle-free and every vertex in V1 has at least (1/4−o(1))n neighbors in V2 and every vertex in V2 has at least (1/4 − o(1))n) neighbors in V1. To construct our example, start with BE(4n/3 + 2) and then remove a randomly selected subset of size n/3 + 2 from one of the two parts. Note that the two parts now have sizes n/3 − 1 and 2n/3 + 1, the resulting graph clearly is K4-free and since the larger part is a space barrier, it has no perfect triangle-factor. Furthermore, with high probability, the minimum degree is (1/6−o(1))n. We conjecture that (1/6 + o(1))n is the proper minimum degree condition.

Conjecture 5.3. For every ω > 0 there exist γ, n0 > 0 such that every K4-free graph on n ≥ n0 vertices with δ(G) ≥ n/6 + ωn and α(G) ≤ γn contains a perfect triangle-tiling.

Using methods similar to those used in our proof of Theorem 1.2 we can show that every graph G which satisﬁes the conditions of Conjecture 5.3 has a triangle-tiling covering almost all of the vertices of G. More precisely, we can show that for 1/n ≪ γ ≪ ω, if G is a K4-free graph on n vertices with δ(G) ≥ (1/6+ω)n and α(G) ≤ γn, then G contains a triangle-tiling which covers all but at most ωn vertices. What follows is a brief sketch of the argument.

Apply Theorem 2.5 with γ ≪ ε ≪ d ≪ ω to obtain a spanning subgraph G′ ⊆ G,

- an exceptional set V0 and clusters V1, . . ., Vk of equal size m. Deﬁne the corresponding reduced graph R on vertex set [k] in the usual way. The fact that G is K4-free implies the following two important facts about these clusters and the graph R. (These facts were ﬁrst observed by Szemer´edi in [12].)


- (a) there is no pair i, j ∈ [k] for which G′[Vi, Vj] is (1/2 + d, ε)-regular, and
- (b) R is triangle-free.


Using a standard argument, it is not hard to see that (a) and the fact that δ(G) ≥ (1/6 + ω)n together imply that δ(R) ≥ k/3. So R must be connected, as otherwise Mantel’s theorem would give a triangle in the smallest connected component of R, contradicting (b). By a result of Enomoto, Kaneko and Tuza [8], the fact that R is a connected graph on k vertices with δ(R) ≥ k/3 implies that R contains ⌊|R|/3⌋ vertexdisjoint copies of P2 (the path on three vertices). In a manner similar to the proof of Lemma 3.1, for each such path ijk we can use the fact that α(G) ≤ γn to greedily construct a triangle-tiling covering all but at most 3.1εm of the vertices of G[Vi ∪ Vj ∪ Vk], where each triangle has one vertex in Vj, the central cluster in the path, and the other two vertices either both in Vi or both in Vk. The union of these ⌊|R|/3⌋ triangle-tilings is then a triangle-tiling in G which covers all but at most ωn vertices.

We can generalize Question 5.2 in the following way.

Question 5.4. Let k ≥ 3 and let G be an n-vertex Kk+1-free graph with α(G) = o(n). What is the best-possible minimum degree condition on G that guarantees a perfect Kktiling in G?

When k is even, we have previously shown that the minimum degree must be at least k−k2 + o(1) n. When k = 2ℓ + 1 ≥ 5, we form G by starting with the complete ℓ-partite graph that has one part V1 of size 3n/k + 1, one part V2 of size 2n/k − 1, and the remaining parts, V3, . . ., Vℓ, each of size 2n/k. In V1, we place BE(|V1|) on V1, and, for every 2 ≤ i ≤ ℓ, we place a copy of ER(|Vi|) on Vi. We then have δ(G) ≥

![image 101](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile101.png>)

k−3

k + 41 · k3 − o(1) n = 4k4−k9 − o(1) n. Furthermore, G has sublinear independence number, is Kk+1-free, and has no perfect Kk-tiling, because each copy of Kk in G has at most 3 vertices in V1.

![image 102](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile102.png>)

![image 103](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile103.png>)

![image 104](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile104.png>)

![image 105](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile105.png>)

Finally, for r ≥ 3, ω, γ > 0 and suﬃciently large n, we give the construction of G := GRT(n, r, ω, γ) from Theorem 1.3(b). For odd r the construction was ﬁrst given in [5] and for even r the construction is from [6]. We say that a partition V1, . . ., Vℓ of the vertices of a graph is equitable if ||Vi| − |Vj|| ≤ 1 for all 1 ≤ i < j ≤ ℓ.

When r = 2ℓ + 1 is odd, we let V1, . . ., Vℓ be an equitable partition of V (G) and form the complete ℓ-partite graph with vertex classes V1, . . ., Vℓ. For every i ∈ [ℓ], we then place a copy of ER(|Vi|) on Vi, so

δ(G) ≥ n −

n ℓ

![image 106](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile106.png>)

≥

r − 3 r − 1

− ω n.

![image 107](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile107.png>)

We can assume that n is large enough so that for each i ∈ [ℓ] the independence number of G[Vi] is at most γn, which implies that α(G) ≤ γn. Note that G is Kr-free, as G[Vi] is K3-free for i ∈ [ℓ].

When r = 2ℓ is even, we let U1, . . ., U3ℓ−2 be a equitable partition of V (G), so |Ui| ∈

2n 3r−4 , 3r 2−n4 for every i ∈ [3ℓ − 2]. Let V1 := U1 ∪ U2 ∪ U3 ∪ U4 and Vi := U3i−1 ∪ U3i ∪ U3i+1 for 2 ≤ i ≤ ℓ − 1,

![image 108](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile108.png>)

![image 109](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile109.png>)

and form the complete (ℓ − 1)-partite graph with vertex classes V1, . . ., Vℓ−1. On V1, we then place a copy of BE(|V1|) and assume n is large enough so that G[V1] has minimum degree at least

1 4

6 3r − 4

− ω |V1| ≥ |V1| −

+ ω n

![image 110](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile110.png>)

![image 111](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile111.png>)

and independence number at most γn. For every 2 ≤ i ≤ ℓ − 1, we place a copy of ER(|Vi|) on Vi and we ensure that n is large enough so that the independence number of G[Vi] is at most γn. Because every vertex in G is adjacent to all but at most 3r 6−4 + ω n vertices of G, we have that

![image 112](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile112.png>)

δ(G) ≥

3r − 10 3r − 4

− ω n.

![image 113](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile113.png>)

Furthermore, α(G) ≤ γn and G is Kr-free as G[V1] is K4-free and each of the subgraphs G[V2], . . ., G[Vℓ−1] is K3-free.

## References

- [1] B. Bollob´s and P. Erd˝os, On a Ramsey-Tur´n type problem, J. Combin. Theory B 21 (1976), 166–168.
- [2] J. Balogh, T. Molla and M. Sharifzadeh with an Appendix by C. Reiher and M. Schacht, Triangle factors of graphs without large independent sets and of weighed graphs, Random Struct. and Algorithms, accepted.
- [3] B. Csaba, and M. Mydlarz, On the maximal number of independent circuits in a graph, J. Combin. Theory B 102 (2012), 395–410.
- [4] K. Corr´di and A. Hajnal, On the maximal number of independent circuits in a graph, Acta Mathematica Academiae Scientiarum Hungaricae 14 (1963), 423–439.
- [5] P. Erd˝os and V.T. S´os, Some remarks on Ramsey’s and Tur´n’s theorems, Combinatorial theory and its applications, (Proc. Colloq., Balatonf¨ured, 1969), (1970), 395–404.
- [6] P. Erd˝os, A. Hajnal, V.T. S´os and E. Szemer´edi, More results on Ramsey-Tur´n type problems, Combinatorica 3 (1983), 69–81.
- [7] S. Janson, T.  Luczak and A. Ruci´nski, Random graphs, Wiley-Interscience, 2000.
- [8] H. Enomoto, A. Kaneko and Zs. Tuza, P3-factors and covering cycles in graphs of minimum degree n/3, Combinatorics, (Eger, 1987), Colloq. Math. Soc. Ja´nos Bolyai 52 (1987), 213–220.


- [9] Y. Kohayakawa and V. Ro¨dl, Szemer´edi’s regularity lemma and quasi-randomness, Recent advances in algorithms and combinatorics, Springer, (2003), 289–351.
- [10] J. Koml´os, G. S´ark¨ozy and E. Szemer´edi, Blow-up lemma, Combinatorica 17 (1997), 109–123.
- [11] J. Koml´os and M. Simonovits, Szemer´edi’s regularity lemma and its applications in graph theory, Combinatorics, Paul Erd˝os is eighty, (Keszthely, 1993), Bolyai Soc. Math. Stud., vol. 2, J´nos Bolyai Math. Soc., Budapest, (1996), 295–352.
- [12] E. Szemer´edi, On graphs containing no complete subgraph with 4 vertices, (in Hungarian), Mat. Lapok 23 (1972), 111–116.
- [13] R. Martin and J. Skokan, Asymptotic multipartite version of the Alon-Yuster theorem, preprint, arXiv:1307.5897 (2013).
- [14] V. Ro¨dl and A. Ruci´nski, Perfect matchings in ε-regular graphs and the blow-up lemma, Combinatorica 19 (1999), 437–452.
- [15] S. Win, Existenz von Ger¨usten mit vorgeschreibenem Maximalgrad in Graphen, Abh. Math. Sem. Univ. Hamburg 43 (1975), 263–267


## 6 Appendix

The purpose of this appendix is to prove Lemma 2.4. The lemma is essentially a corollary to the following two theorems of Kohayakawa and Ro¨dl [9]. For this we use the following notation: let G be a bipartite graph with vertex classes A and B, and deﬁne d := d(G[A, B]). Then for any ε we deﬁne DAB(ε) to be the graph with vertex set A in which x, x′ ∈ A are adjacent if and only if

|NG(x)|, |NG(x′)| > (d − ε)|B| and |NG(x) ∩ NG(x′)| < (d + ε)2|B|.

- Theorem 6.1 ([9, Theorem 45]). Let 0 < ε < 1, and let G[A, B] be a bipartite graph with

|A| ≥ 2/ε. If e(DAB(ε)) > (1 − 5ε)|A|2/2, then G[A, B] is (d, (16ε)1/5)-regular, where d := d(G[A, B]).

- Theorem 6.2 ([9, Theorem 46]). Let 0 < ε < 1, and let G[A, B] be a bipartite graph


- with |B| ≥ 1/d, where d := d(G[A, B]). If G[A, B] is (d, ε)-regular, then e(DAB(ε)) ≥ (1 − 8ε)|A|2/2.


The following two similar lemmas do most of the remaining work required to complete the proof.

- Lemma 6.3. Suppose that 1/n ≪ ξ ≪ ξ′ and that 1/n ≪ β. Let G[A, B] be a bipartite graph such that |A|, |B| ≤ n, and let x1, . . ., xs and y1, . . ., yt be positive integers each of size at least βn such that i∈[s] xi ≤ |A| and j∈[t] yj ≤ |B|. If {X1, . . ., Xs} is a collection of disjoint subsets of A and {Y1, . . ., Yt} is a collection of disjoint subsets of B with |Xi| = xi and |Yj| = yj for all i ∈ [s] and j ∈ [t] selected uniformly at random from all such collections, then, with probability at least 1 − e−Ω(n), for every i ∈ [s], j ∈ [t], x, x′ ∈ A and y, y′ ∈ B we have


- (a) |NG(x) ∩ Yj|/yj = |NG(x)|/|B| ± ξ,
- (b) |NG(y) ∩ Xi|/xi = |NG(y)|/|A| ± ξ,
- (c) |NG(x) ∩ NG(x′) ∩ Yj|/yj = |NG(x) ∩ NG(x′)|/|B| ± ξ,
- (d) |NG(y) ∩ NG(y′) ∩ Xi|/xi = |NG(y) ∩ NG(y′)|/|A| ± ξ, and
- (e) d(G[Xi, Yj]) = d(G[A, B]) ± ξ′.


Proof. Note that the at most t(|A|+|A|2)+s(|B|+|B|2) ≤ 2β−1(n+n2) random variables of the form |NG(x) ∩Yj|, |NG(y)∩ Xi|, |NG(x) ∩NG(x′) ∩Yj|, and |NG(y)∩NG(y′)∩ Xi|, where i ∈ [s], j ∈ [t], x, x′ ∈ A and y, y′ ∈ B, are hypergeometrically distributed, so the fact that (a)-(d) hold with probability 1 −eΩ(n) follows directly from Theorem 2.3 by taking a union bound. For (e), let ℓ := ξ−1/2 and deﬁne Dk := {v ∈ A : 2(k − 1)ξ ≤ |N(v)|/|B| < 2kξ} for each k ∈ [ℓ]. Then, with probability 1−eΩ(n), for every i ∈ [s] and k ∈ [ℓ], we have that

|Dk ∩ Xi| xi

|Dk| |A|

± ξ2.

=

![image 114](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile114.png>)

![image 115](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile115.png>)

Fix a choice of X1, . . ., Xs and Y1, . . ., Yt, for which (a)-(d) hold and this event occurs. Note that for every k ∈ [ℓ], v ∈ Dk, and j ∈ [t],

|NG(v)| |B|

= (2k − 1)ξ ± ξ so

![image 116](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile116.png>)

|NG(v) ∩ Yj| yj

= (2k − 1)ξ ± 2ξ.

![image 117](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile117.png>)

We compute d(G[A, B]) to be

|NG(v)| |B|

1 |A|

![image 118](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile118.png>)

![image 119](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile119.png>)

k∈[ℓ] v∈Dk

=

k∈[ℓ]

|Dk| |A|

((2k − 1)ξ ± ξ) ·

![image 120](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile120.png>)

Then for any i ∈ [s] and j ∈ [t] we have

= 

  ± ξ.

|Dk| |A|

(2k − 1)ξ

![image 121](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile121.png>)



k∈[ℓ]

d(G[Xi, Yj]) =

so (e) holds.

= 



|NG(v) ∩ Yj| yj

|Dk| |A|

1 xi

± ξ2

((2k − 1)ξ ± 2ξ) ·

=

![image 122](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile122.png>)

![image 123](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile123.png>)

![image 124](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile124.png>)

k∈[ℓ] v∈Dk∩Xi

k∈[ℓ]

  ± (ℓ2ξ3 + 2ξ + 2ℓξ3) = d(G[A, B]) ± ξ′,

|Dk| |A|

(2k − 1)ξ

![image 125](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile125.png>)

k∈[ℓ]

![image 126](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile126.png>)

![image 127](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile127.png>)

![image 128](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile128.png>)

![image 129](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile129.png>)

- Lemma 6.4. Suppose that 1/n ≪ ξ ≪ ξ′ and 1/n ≪ β, and that x1, . . ., xs are positive integers each of size at least βn such that i∈[s] xi ≤ n. If G is a graph on n vertices and {X1, . . ., Xs} is a collection of disjoint subsets of V (G) with |Xi| = xi for all i ∈ [s] selected uniformly at random from all such collections, then, with probability at least 1 − e−Ω(n), for every i ∈ [s] and x, x′ ∈ V (G) we have


- (a) |NG(x) ∩ Xi|/xi = |NG(x)|/n ± ξ,
- (b) |NG(x) ∩ NG(x′) ∩ Xi|/xi = |NG(x) ∩ NG(x′)|/n ± ξ, and
- (c) 2e(G[Xi])/x2i = 2e(G)/n2 ± ξ′.


Proof. It is straightforward to modify the proof of Lemma 6.3 to prove this lemma; we omit the details.

![image 130](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile130.png>)

![image 131](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile131.png>)

![image 132](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile132.png>)

![image 133](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile133.png>)

Now we give the proof of Lemma 2.4.

Proof of Lemma 2.4. Introduce a new constant η with 1/n ≪ η ≪ ε. Suppose that G[A, B] is (≥d, ε)-regular, let d∗ := d(G[A, B]), so d∗ = d ± ε, and deﬁne D := DAB(ε). Note that, by Theorem 6.2, we have that 2e(D)/|A|2 ≥ 1 − 8ε. We apply Lemma 6.3 to G[A, B] and Lemma 6.4 to D, with ξ′ replaced by η in each case, to ﬁnd that with probability 1 − e−Ω(n) our random selection satisﬁes the conclusions of each of these lemmas. We ﬁx such an outcome of our random selection, and consider any i ∈ [s] and

- j ∈ [t]. Deﬁne dij := d(Xi, Yj), so dij = d∗ ± η, and dij = d ± (ε + η). (4)


We also have that

2e(D[Xi]) x2i

≥

![image 134](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile134.png>)

2e(D) |A|2

![image 135](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile135.png>)

Recall that, if xx′ ∈ E(D[Xi]), then

− η ≥ 1 − 8ε − η ≥ 1 − 5(2ε).

|NG(x′)| |B|

|NG(x) ∩ NG(x′)| |B|

|NG(x)| |B|

< (d∗ + ε)2, so

> d∗ − ε and

,

![image 136](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile136.png>)

![image 137](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile137.png>)

![image 138](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile138.png>)

|NG(x′) ∩ Yj| yj

|NG(x) ∩ Yj| yj

> (d∗ − ε) − η > dij − 2ε, and, as we can assume η is small enough so that η1/2 + η < ε,

,

![image 139](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile139.png>)

![image 140](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile140.png>)

|NG(x) ∩ NG(x′) ∩ Yj| yj

< (d∗ + ε)2 + η < (dij + η + ε)2 + (ε − η)2 < (dij + 2ε)2.

![image 141](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile141.png>)

This proves that xx′ ∈ E(DX

iYj(2ε). Therefore, by Lemma 6.1 with d and ε replaced by dij and 2ε, respectively, G[Xi, Yj] is (dij, (32ε)1/5)regular, and is therefore (d, (32ε)1/5 + 2ε)-regular, because, by (4), d = dij ± 2ε. Since we can assume that ε is small enough so that (32ε)1/5 + 2ε ≤ (33ε)1/5, it follows that G[Xi, Yj] is (d, (33ε)1/5)-regular.

iYj(2ε)), so D is a subgraph of DX

Clearly, if G[A, B] is (d, ε)-super-regular, then, by (a) and (b) of Lemma 6.3, we can also ensure that G[Xi, Yj] is (d, (33ε)1/5)-super-regular for each i ∈ [s] and j ∈ [t].

![image 142](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile142.png>)

![image 143](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile143.png>)

![image 144](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile144.png>)

![image 145](<2016-balogh-triangle-tilings-graphs-without-large_images/imageFile145.png>)

