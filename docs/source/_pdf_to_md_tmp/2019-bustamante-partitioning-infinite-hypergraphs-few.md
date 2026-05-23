arXiv:1905.05100v1[math.CO]13May2019

# Partitioning inﬁnite hypergraphs into few monochromatic Berge-paths

### Sebastián Bustamante Jan Corsten∗ Nóra Frankl∗ 14th May 2019

Extending a result of Rado to hypergraphs, we prove that for all s,k,t ∈ N with k ≥ t ≥ 2, the vertices of every r = s(k − t + 1)-edge-coloured countably inﬁnite complete k-graph can be partitioned into the cores of at most s monochromatic t-tight Berge-paths of diﬀerent colours. We further describe a construction showing that this result is best possible.

## 1 Introduction

Lehel’s conjecture (ﬁrst seen in [2]) states that the vertices of every 2-edge-coloured complete graph can be partitioned into two monochromatic cycles, one of each colour. Here, single vertices and edges are considered to be cycles and this convention is used throughout this paper. The conjecture was proved for very large graphs by Łuczak, Rödl and Szemerédi [14] in 1998, for large graphs by Allen [1] in 2008, and for all graphs by Bessy and Thomassé [3] in 2010.

Erdős, Gyárfás and Pyber [6] conjectured in 1991 that this can be extended to r colours (allowing r monochromatic cycles). This was however disproved by Pokrovskiy [17], who showed that for every r ≥ 3, there are inﬁnitely many r-edge-coloured complete graphs whose vertices cannot be covered by r monochromatic vertex-disjoint cycles. Finding the minimum number of monochromatic vertex-disjoint cycles needed to cover the vertices of any r-edge-coloured complete graph remains a big open problem. We note that a priori it is not obvious that this minimum is independent of the size of the complete graph we wish to cover. The fact that this is the case was proved by Erdős, Gyárfás and Pyber [6], who also presented a simple construction in which r cycles are needed. The currently best-known upper bound is 100r logr, due to Gyárfás, Ruszinkó, Sárközy and Szemerédi [9].

![image 1](<2019-bustamante-partitioning-infinite-hypergraphs-few_images/imageFile1.png>)

∗Department of Mathematics, London School of Economics, Houghton St, WC2A 2AE London, Email: j.corsten@lse.ac.uk, n.frankl@lse.ac.uk.

An inﬁnite analogue of the conjecture of Erdős, Gyárfás and Pyber is true as proved by Rado [18] already in 1978.

- Theorem 1.1 ([18]). The vertices of every countablyinﬁniter-edge-colouredcomplete graph can be partitioned into r monochromatic paths (inﬁnite or ﬁnite), one of each colour.

Rado’s theorem is best possible, as the construction for ﬁnite graphs in [6] can be extended to inﬁnite graphs.

In this note we consider extensions of this result to hypergraphs. A k-uniform hypergraph (or shortly, a k-graph) is a tuple H = (V, E) where V and E are sets with E ⊆ Vk . The complete k-graph with vertex-set V, denoted by KV(k), is the k-graph with edge-set E = Vk .

There are diﬀerent notions of paths in hypergraphs, loose paths, tight paths and Bergepaths; all of these coincide with the notion of paths when k = 2. In this note, we will mainly consider Berge-paths. Given integers 2 ≤ t ≤ k and ℓ ≥ 1, a ﬁnite (k-uniform) t-tight Berge-path of length ℓ is a pair (X, F) deﬁned as follows. X = { 1, . . ., ℓ+t−1} ⊆ V is a set of ℓ + t − 1 distinct vertices, F = {e1, . . .,eℓ} ⊆ E is a set of ℓ distinct edges and

i, i+1, . . ., i+t−1 ∈ ei for all i ∈ [ℓ]. For technical reasons we deﬁne a t-tight Bergepath of length 0 as a pair ({ }, ∅). A (one-way) inﬁnite t-tight Berge-path is a pair (X, F) where X = { i : i ∈ N} ⊆ V, F = {ei : i ∈ N} ⊆ E, and i, i+1, . . . i+t−1 ∈ ei for all i ∈ N. For a t-tight Berge-path P = (X, F), X is called the core of P. A family P1 = (X1, F1), . . .,Pr = (Xr, Fr) of t-tight Berge-paths core-partitionsV if X1 ∪ · · · ∪ Xr is a partition of V. Given an edge-colouring φ of a k-graph H, a t-tight Berge-path P = (X, F) in H is said to be monochromatic in colour c if φ(f ) = c for all f ∈ F.

A 2-tight Berge-path is simply called a Berge-path and a k-tight Berge-path is called a tight path. The k-uniform loose path of length ℓ consists of n = k(ℓ − 1) + 1 vertices { 1, . . ., n} and the ℓ edges { i(k−1)+1, . . ., i(k−1)+k} for i = 0, . . ., ℓ − 1. The inﬁnite loose path consists of the vertices { 1, 2, . . .} and edges { i(k−1)+1, . . ., i(k−1)+k} for all i = 0, 1, . . ..

Many extensions of path partition problems to hypergraphs have been studied, considering loose paths [10, 11, 20], tight paths [5, 4] and Berge-paths [10]. Most relevant for the topic of this note are the following two extensions of Theorem 1.1.

- Theorem 1.2 (Gyárfás–Sárközy [10]). The vertices of every countably inﬁnite r-edgecoloured complete k-graph can be partitioned into r monochromatic loose paths (inﬁnite or ﬁnite), one of each colour.
- Theorem 1.3 (Elekes–Soukup–Soukup–Szentmiklóssy [5]). The vertices of every countably inﬁniter-edge-coloured completek-graph can be partitioned intor monochromatictight paths (inﬁnite or ﬁnite), one of each colour.


The latter result answers a question of Gyárfás and Sárközy from [10]. Note that both Theorems 1.2 and 1.3 reduce to Theorem 1.1 when k = 2. Our main result extends Theorem 1.1 in a similar way to Berge-paths. It turns out that ⌈r/(k − 1)⌉ paths suﬃce.

- Theorem 1.4. For all s,k ∈ N with k ≥ 2 and every r = s(k − 1)-edge-colouring of KN(k), the vertices can be core-partitioned into s monochromatic Berge-paths of diﬀerent colours.

Note that Theorem 1.4 reduces to Theorem 1.1 when k = 2 as well. We shall actually prove the following more general result about t-tight Berge-paths.

- Theorem 1.5. For all s,k,t ∈ N with k ≥ t ≥ 2 and every r = s(k −t +1)-edge-colouring of

KN(k), the verticescan be core-partitionedintos monochromatict-tightBerge-pathsofdiﬀerent colours.

Note that the case k = 2 reduces to Theorem 1.4, and the case k = t reduces to Theorem 1.3. The following theorem shows that Theorem 1.5 is best possible.

- Theorem 1.6. For all s,k,t ∈ N with k ≥ t ≥ 2, there is an edge-colouring of KN(k) with r = s(k−t +1)+1 colours in which the vertices cannot be covered by the cores ofs monochromatic t-tight Berge-paths.


We will prove Theorem 1.6 in Section 2 and Theorem 1.5 in Section 3.

## 2 Proof of Theorem 1.6

The construction described in the proof generalises the construction from [6].

Proof of Theorem 1.6. We denote the lexicographical ordering of [rs] by ≺. First, we partition N into sets BI : I ∈ [rs] so that all BI’s but B{r−s+1,...,r} are ﬁnite and |BI| ≥ st ·

≺I(|B | + 1) for every I ∈ [rs] .1 For x ∈ N, let I(x) be the s-subset of [r] for which x ∈ BI(x). We deﬁne an r-edge-colouring φ of KN(k) as follows.

For every e ∈ E(KN(k)) we consider an order xe1, . . .,xek of e satisfying I(xei) I(xej) for all 1 ≤ i < j ≤ k, and deﬁne φ(e) as an arbitrary member of [r] \ i≤k−t+1 I(xei).

Assume for contradiction that there are monochromatic t-tight Berge-paths P1, . . .,Ps

with cores X1, . . .,Xs so that i Xi = N and let C ⊆ [r] be a set of size s which contains all colours used by these t-tight Berge-paths.

Observe that for every edge e with e ∩ BC ∅ and φ(e) ∈ C we have

e ∩ ≺C B ≥ k − t + 1. (2.1) Indeed, if e ∩ ≺C B < k − t + 1, then C I(xek−t+1) and thus φ(e) C.

For i ∈ C, let Fi be the set of all f ∈ Xti which consist of t consecutive vertices of Xi with at least one element in BC. Let f ∈ Fi and let e ∈ E(Pi) be some edge with f ⊆ e. By

![image 2](<2019-bustamante-partitioning-infinite-hypergraphs-few_images/imageFile2.png>)

1This growth rate of the B|I| can be improved by a more careful analysis.

(2.1), we have e \ ≺C B ≤ t − 1 and therefore some vertex in f must be in ≺C B . Since every ∈ N is contained in at most t sets f ∈ Fi, it follows that

|Fi| ≤ t ≺C B . (2.2) Observe now that for all but at most t − 1 vertices ∈ Xi ∩ BC, there is a unique f ∈ Fi

starting at and thus

|Xi ∩ BC| ≤ |Fi| + t − 1. (2.3) Combining (2.2) and (2.3), we get

|Xi ∩ BC| ≤ t · ≺C |B | + t − 1 < |BC|/r for every i ∈ [r] and hence |BC| = |BC ∩ ( i Xi)| < |BC|, a contradiction.

## 3 Proof of Theorem 1.5

Our proof is based on ideas from [5]. First, we need to introduce some notation. An rmulti-colouring of a k-graph G is a function χ : E(G) → 2[r]. Given a set F ⊆ E(G), we denote by χ(F) = e∈F χ(e) the set of colours they have in common and say that F is (χ)monochromatic if χ(F) is non-empty. For a given r-colouring φ of K := KN(k) and i, j ∈ N with j < k, we deﬁne an r-multi-colouring φi,j : N\{j i} → 2[r] by

φi,j(f ) = {φ(e) : e ∈ E(K) and {i} ∪ f ⊆ e}.

Furthermore, we call {Ki : i ∈ N} a j-clique-chain w.r.t. an r-colouring φ of K if K1 is a φ1,j-monochromatic copy of KN(j) with V(K1) ⊆ N and Ki is a φi,j-monochromatic copy of KN(j) with V(Ki) ⊆ V(Ki−1) for every i ∈ N.

Observe that, by Ramsey’s theorem [19] for inﬁnite hypergraphs, there exists a j-cliquechain for every r-colouring of K and every j ∈ [k − 1].

For a j-clique-chain {Ki : i ∈ N} we deﬁne a vertex-multi-colouring χ : N → 2[r] by

χ(i) = e∈E(Ki) φi,j(e) for every i ∈ N. We call χ the clique-colouring induced by {Ki : i ∈ N}.

Lemma 3.1. For all s,k,t ∈ N with k ≥ t ≥ 2 and every r = s(k − t + 1)-colouring of KN(k), there is a (t − 1)-clique-chain that induces a clique-colouring using at most s colours.

Proof. Let φ be the given r-colouring of K := KN(k). Furthermore, let C1 ∪ · · · ∪ Cr be a partition of the set of r = s(k − t + 1) colours into r blocks of size s. We will show that

there is a (t − 1)-clique-chain and some i ∈ [r] such that for the induced clique-colouring we have χ( ) ∩Ci ∅ for all ∈ N.

We call an inﬁnite (t − 1)-uniform clique K′ maximally-monochromatic w.r.t. a multicolouring ψ of K′ and a set C ⊆ [r] if there is no inﬁnite clique K′′ ⊆ K′ with

| {i : ψ(K′′) ∩Ci ∅} ∩ C| > | {i : ψ(K′) ∩Ci ∅} ∩ C|. Note that a maximallymonochromatic clique is not necessarily monochromatic (since all its inﬁnite monochromatic subcliques might have colours not in C). Further note that every inﬁnite clique contains a maximally-monochromatic inﬁnite clique (since r is ﬁnite).

We build a (t − 1)-clique-chain as follows. Let K1 be any φ1,t−1-monochromatic, maximally-monochromatic (t − 1)-uniform clique w.r.t. φ1,t−1 and D = [r], and let D1 :=

- i : φ1,t−1(K1) ∩Ci ∅ . Now, for every j ∈ N, let Kj+1 be a φj+1,t−1-monochromatic,

maximally-monochromatic clique w.r.t. φj+1,t−1 and Di with V(Kj+1) ⊆ V(Kj) and let Di+1 = i : φj+1,t−1(Kj+1) ∩Ci ∅ . If there is some i ∈ [r] such that Ci ∩ Dj ∅ for all

- j ∈ N, then {K1, K2, . . .} is a (t − 1)-clique-chain with the desired property. Hence we may assume that there is no such i.


Thus, there exist j1, . . ., jr, such that Ci ∩ Dji = ∅ but Ci ∩ Dij−1 ∅ for every i ∈ [r]. Without loss of generality we may assume that j1 ≤ . . . ≤ jr. Let X = V(Kjr) and note that V(Kji) ⊇ X for every i ∈ [r]. Deﬁne Φ : t X−1 → 2[r] by

Φ(f ) = {φ(e) : e ∈ E(K) and {j1, . . ., jr} ∪ f ⊆ e}.

Note that every f ∈ t X−1 receives at least one colour, and that Φ(f ) ⊆ φji,t−1(f ) for every f ∈ t X−1 and every i ∈ [r]. By Ramsey’s theorem for hypergraphs there is a Φ-monochromatic inﬁnite clique K′ in X. Therefore, there is some ℓ ∈ [r] such that Φ(K′) ∩Cℓ ∅ and consequently Kjℓ is not maximally monochromatic.

We proceed now with the proof of Theorem 1.5.

Proof of Theorem 1.5. Letφ be the givenr-colouring of K = KN(k). By Lemma 3.1, there is a (t − 1)-clique-chain {Ki : i ∈ N} that induces a clique-colouring χ using at most s colours (without loss of generality these colours are 1, . . .,s). For i ∈ [s], let Ai ⊆ N be the set of vertices of colour i according to χ.

By repeating the following process we will simultaneously buildt-tight monochromatic Berge-paths P1, . . .,Pr with core-vertex sequences {bi,1,bi,2, . . .} for every i ∈ [s]. Let bi,1 := minAi for every i ∈ [s]. In every step, we will add to each path t or t − 1 vertices making sure that for every i ∈ [s], the last new vertex, saybi,ni, is in Ai, and that the other new vertices are in V(Kbi,n

). Right after choosing the vertex bi,j, we will choose a unique edge ei,j ∈ E(K) of colour i which contains the t consecutive vertices bi,j−t+1, . . .,bi,j for every j ≥ t and i ∈ [s]. Let X = {b1,1, . . .,bs,1} and let Y = ∅. We will use X to keep track of already used vertices and Y to keep track of already used edges.

i

For each i ∈ [s] do the following.2 Suppose the current path Pi ends in bi,n ∈ Ai for some n ∈ N. We will now extend Pi by t or t − 1 vertices as follows. Let a be the smallest vertex in Ai \ X (if Ai \ X is empty, the path Pi is complete and we move to the next step). Add a to X and do the following for every j = 1, . . .,t − 2. Choose a vertex bi,n+j ∈ V(Ka)\ ( Y) and add it to X (note that this is always possible sinceV(Ka) is inﬁnite and Y is ﬁnite). Let fi,n+j = {bi,n+j−t+1, . . .,bi,n+j} be the set of the t consecutive vertices in

![image 3](<2019-bustamante-partitioning-infinite-hypergraphs-few_images/imageFile3.png>)

2To avoid unnecessary subscripts for ‘local variables’, we treat i as being ﬁxed in the following.

the core of the Berge-path Pi ending at bi,n+j. Note that fi,n+j \ {bi,n} ∈ E(Kbi,n) and thus i ∈ φbi,n,t−1(fi,n+j \ {bi,n}). Hence, by the deﬁnition of φbi,n,t−1, there exist ei,n+j ∈ E(K) with fi,n+j ⊆ ei,n+j and φ(ei,n+j) = i. Add ei,n+j to Y. Since bi,n+j Y, we have ei,n+j Y and we can therefore use ei,n+j as the edge for fi,n+j in our Berge-path.

Choosing the next vertex will be slightly more complicated (since a might be in some edge in Y). Let b ∈ V(Ka) \ Y and let f1′ = {bi,n, . . .,bi,n+t−2,b} and f2′ = {bi,n+1, . . .,bi,n+t−2,b,a}, and note that f1′ \ {bi,n} ∈ E(Kbi,n) and f2′ \ {a} ∈ E(Ka). As before, i ∈ φbi,n,t−1(f1′ \ {bi,n}) ∩ φa,t−1(f2′ \ {a}) and thus there exist e1′,e2′ ∈ E(K) with fs′ ⊆ es′ and φ(es′) = i for both s = 1, 2. If e1′ e2′, let bi,n+t−1 := b and bi,n+t = a and let ei,n+t−1 := e1′ and ei,n+t = e2′. Add bi,n+t−1 to X and ei,n+t−1,ei,n+t to Y. Note that ei,n+t−1 and ei,n+t can be chosen as the edges for the t consecutive vertices of Pi ending in bi,n+t−1 and bi,n+t. If e1′ = e2′, let bi,n+t−1 = a and ei,n+t−1 = e1′ = e2′, and add ei,n+t−1 to Y. Note that the t consecutive vertices of Pi ending in bi,n+t−1 are contained in ei,n+t−1 and ei,n+t−1 Y. Hence, ei,n+t−1 can be chosen as the edge for the t consecutive vertices of Pi ending in bi,n+t−1.

By construction, P1, . . .,Ps are monochromatict-tight Berge-paths whose cores are disjoint. Furthermore, since at the beginning of every step the smallest uncovered vertex a of Ai is chosen, we have i V(Pi) = N.

## 4 Further remarks and open problems

Theorems 1.1 to 1.4 remain true when we consider cycles instead of paths, where an inﬁnite cycle is a two-way inﬁnite path. It is not clear to us however if one can replace paths by cycles in Theorem 1.5 when 2 < t < k. Diﬃculties only arise when trying to close ﬁnite paths to cycles, hence we can replace paths by cycles if we allow ﬁnitely many vertices to be uncovered.

A natural question to ask is if similar results hold in the ﬁnite setting. Gyárfás, Lehel, Sárközy and Schelp [8] conjectured that every ﬁnite (k − 1)-edge-coloured complete k-graph contains a monochromatic Hamiltonian Berge-cycle. Note that, in the inﬁnite setting, this is a special case of Theorem 1.4. After partial results in [8, 12, 13, 15], Omidi [16] announced a proof of this conjecture.

We believe that a generalisation of this to more colours, similar as in Theorem 1.4, is true as well.

- Conjecture 4.1. For all s,k ∈ N with k ≥ 2, there is some c = c(s,k) ∈ N such that


the following is true for all n ∈ N. In every r = s(k − 1)-edge-colouring of Kn(k), there is a collection of at most s monochromatic t-tight Berge-cycles whose cores are disjoint and cover all but c vertices.

For k = 2, this reduces to a conjecture of Pokrovskiy [17]. We further believe that this can be extended to t-tight Berge-cycles similarly to Theorem 1.5.

- Conjecture 4.2. For all s,k,t ∈ N with k ≥ t ≥ 2, there is some c = c(s,k,t) ∈ N such that


the following is true for all n ∈ N. In every r = s(k −t + 1)-edge-colouring of Kn(k), there is a collection of at most s monochromatic t-tight Berge-cycles whose cores are disjoint and cover all but c vertices.

A simple modiﬁcation of the construction in Section 2 shows that these conjectures are best possible (if true) apart from the ﬁnite leftover.

Recently we learned that Gerbner, Methuku, Omidi and Vizer [7, unpublished] made some progress towards these conjectures.

## Acknowledgments

The authors would like to thank Peter Allen and Jan van den Heuvel for their helpful suggestions on the manuscript. The ﬁrst author was supported by CONICYT Doctoral Fellowship 21141116. Part of this research was done while the second and third author visited Universiad de Chile with the support of the Santander Travel Research Fund.

## References

- [1] Peter Allen, Covering two-edge-coloured complete graphs with two disjoint monochromatic cycles, Combinatorics, Probability and Computing 17 (2008), no. 4, 471–486.
- [2] JacquelineAyel, Sur l’existencede deuxcyclessupplémentairesunicolores, disjointset de couleurs diﬀérentes dans un graphe complet bicolore, Ph.D. thesis, Université JosephFourier-Grenoble I, 1979.
- [3] Stéphane Bessy and Stéphan Thomassé, Partitioning a graph into a cycle and an anticycle, a proof of Lehel’s conjecture, Journal of Combinatorial Theory, Series B 100

(2010), no. 2, 176–180.

- [4] Sebastián Bustamante, Jan Corsten, Nóra Frankl, Alexey Pokrovskiy, and Jozef Skokan, Partitioning edge-coloured hypergraphs into few monochromatic tight cycles, arXiv:1903.04471 (2019).
- [5] Márton Elekes, Dániel Soukup, Lajos Soukup, and Zoltán Szentmiklóssy, Decompositions of edge-colored inﬁnite complete graphs into monochromatic paths, Discrete Mathematics 340 (2017), no. 8, 2053–2069.
- [6] Paul Erdős, András Gyárfás, and László Pyber, Vertex coverings by monochromatic cycles and trees, Journal of Combinatorial Theory, Series B 51 (1991), no. 1, 90–95.
- [7] Dániel Gerbner, Abhishek Methuku, Gholamreza Omidi, and Máté Vizer, Monochromatic berge cycles in uniform hypergraphs, unpublished manuscript (2019+).


- [8] András Gyárfás, Jenő Lehel, Gábor Sárközy, and Richard Schelp, Monochromatic Hamiltonian Berge-cycles in colored complete uniform hypergraphs, Journal of Combinatorial Theory, Series B 98 (2008), no. 2, 342–358.
- [9] András Gyárfás, Miklós Ruszinkó, Gábor Sárközy, and Endre Szemerédi, An improved bound for the monochromatic cycle partition number, Journal of Combinatorial Theory, Series B 96 (2006), no. 6, 855–873.
- [10] András Gyárfás and Gábor Sárközy, Monochromatic path and cycle partitions in hypergraphs, The Electronic Journal of Combinatorics 20 (2013), no. 1, 18.
- [11] , Monochromatic loose-cycle partitions in hypergraphs, The Electronic Journal of Combinatorics 21 (2014), no. 2, 2–36.

![image 4](<2019-bustamante-partitioning-infinite-hypergraphs-few_images/imageFile4.png>)

- [12] András Gyárfás, Gábor Sárközy, and Endre Szemerédi, Long monochromatic Berge cycles in colored 4-uniform hypergraphs, Graphs and Combinatorics 26 (2010), no. 1, 71–76.
- [13] , Monochromatic matchings in the shadow graph of almost complete hypergraphs, Annals of Combinatorics 14 (2010), no. 2, 245–249.

![image 5](<2019-bustamante-partitioning-infinite-hypergraphs-few_images/imageFile5.png>)

- [14] Tomasz Łuczak, Vojtěch Rödl, and Endre Szemerédi, Partitioning two-coloured complete graphs into two monochromatic cycles, Combinatorics, Probability and Computing 7 (1998), no. 4, 423–436.
- [15] Leila Maherani and Gholam Reza Omidi, Monochromatic Hamiltonian Berge-cycles in colored hypergraphs, Discrete Mathematics 340 (2017), no. 8, 2043–2052.
- [16] Gholam R. Omidi, A proof for a conjecture of Gyárfás, Lehel, Sárközy and Schelp on Berge-cycles, arXiv:1404.3385 (2014).
- [17] Alexey Pokrovskiy, Partitioning edge-coloured complete graphs into monochromatic cycles and paths, Journal of Combinatorial Theory, Series B 106 (2014), 70–97.
- [18] Richard Rado, Monochromatic paths in graphs, Annals of Discrete Mathematics 3

(1978), 191–194. MR 0485504

- [19] Frank P. Ramsey, On a problem of formal logic, Proceedings of the London Mathematical Society 2 (1930), no. 1, 264–286.
- [20] Gábor Sárközy, Improved monochromatic loose cycle partitions in hypergraphs, Discrete Mathematics 334 (2014), 52–62.


