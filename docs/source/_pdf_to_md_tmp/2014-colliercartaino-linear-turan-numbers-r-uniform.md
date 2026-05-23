arXiv:1404.5015v2[math.CO]22Apr2014

# Linear Tura´n numbers of r-uniform linear cycles and related Ramsey numbers

Clayton Collier-Cartaino∗ Nathan Graber† Tao Jiang‡

Abstract

An r-uniform hypergraph is called an r-graph. A hypergraph is linear if every two edges intersect in at most one vertex. Given a linear r-graph H and a positive integer n, the linear Tur´n number exL(n,H) is the maximum number of edges in a linear r-graph G that does not contain H as a subgraph. For each ℓ ≥ 3, let Cℓr denote the r-uniform linear cycle of length ℓ, which is an r-graph with edges e1,...,eℓ such that ∀i ∈ [ℓ − 1], |ei ∩ ei+1| = 1, |eℓ ∩ e1| = 1 and ei ∩ ej = ∅ for all other pairs {i,j},i = j. For all r ≥ 3 and ℓ ≥ 3, we show that there exist positive constants cm,r and c′m,r, depending only m and r, such that exL(n,C2rm) ≤ cm,rn1+

1 m

![image 1](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile1.png>)

1

and exL(n,C2rm+1) ≤ c′m,rn1+

m. This answers a question of Kostochka, Mubayi, and Verstra¨ete [29]. For even cycles, our result extends the result of Bondy and Simonovits [7] on the Tur´an numbers of even cycles to linear hypergraphs.

![image 2](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile2.png>)

Using our results on linear Tur´an numbers we also obtain bounds on the cycle-complete hypergraph Ramsey numbers. We show that there are positive constants am,r and bm,r, depending only on m and r, such that R(C2rm,Ktr) ≤ am,r(lntt)

m

m

m−1 and R(C2rm+1,Ktr) ≤ bm,rt

m−1.

![image 3](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile3.png>)

![image 4](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile4.png>)

![image 5](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile5.png>)

## 1 Introduction

A hypergraph H = (V,E) consists of a set V of vertices and a set E of edges, where each edge is a subset of V . If all the edges of H have size r, then H is said to be r-uniform and will be called an r-graph for brevity. The complete r-graph on n vertices will be denoted by Knr. A hypergraph H is linear if ∀e,e′ ∈ E(H),|e∩e′| ≤ 1. Given a family H of r-graphs, the Tura´n number of H for a given positive integer n, denoted by ex(n,H), is the maximum number of edges of an r-graph on n vertices that does not contain any member of H as a subgraph. If H is a family of linear r-graphs, then we deﬁne, for a given positive integer n, the linear Tura´n number of H to be the maximum number of edges of a linear r-graph on n vertices that does not contain any member of H as a subgraph, and denote it by exL(n,H). When H consists of a single graph H, we write ex(n,H) and exL(n,H) for ex(n,H) and exL(n,H), respectively.

A linear cycle of length ℓ is a hypergraph with edges e1,... ,eℓ such that ∀i ∈ [ℓ−1], |ei∩ei+1| = 1, |eℓ ∩ e1| = 1 and ei ∩ ej = ∅ for all other pairs {i,j},i = j. We denote an r-uniform linear cycle of

![image 6](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile6.png>)

∗Dept. of Mathematics, Miami University, Oxford, OH 45056, USA. E-mail:colliec@miamioh.edu †Dept. of Mathematics, Miami University, Oxford, OH 45056, USA. E-mail: grabernt@miamioh.edu ‡Dept. of Mathematics, Miami University, Oxford, OH 45056, USA. E-mail: jiangt@miamioh.edu. Research sup-

ported in part by Simons Foundation Collaboration Grant #282906. 2010 Mathematics Subject Classiﬁcations: 05D05, 05C65, 05C35. Key Words: Ramsey number, Tur´an number, cycle, linear hypergraphs.

1

length ℓ by Cℓr. In particular, 2-uniform linear cycles are just the usual graph cycles. The Tura´n problem for graph cycles has been much studied. For odd cycles, the answer is ⌊n42⌋ for all suﬃciently large n, with equality achieved by a balanced complete bipartite graph on n vertices. The problem for even cycles remains unresolved except for C4 [17]. A general upper bound of ex(n,C2m) ≤ γmn1+m1 for some positive constant γm was asserted by Erd˝os (unpublished). The ﬁrst published proof was obtained by Bondy and Simonovits [7], who showed that ex(n,C2m) ≤ 20mn1+m1 for all suﬃciently large n. This was improved by Verstrae¨te [39] to 8(m−1)n1+m1 and by Pikhurko [33] to (m−1)n1+m1 . Very recently, Bukh and Jiang [9] improved the upper bound to 80√mlog m · n1+m1 + 10m2n for all n ≥ (2m)8m2. For m = 2,3,5, constructions of C2m-free n-vertex graphs with Ω(n1+m1 ) edges are known (see [21]). Thus ex(n,C2m) = Θ(n1+m1 ), for m ∈ {2,3,5}. However, the order of magnitude of ex(n,C2m) remains undetermined for all m  ∈ {2,3,5}.

![image 7](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile7.png>)

![image 8](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile8.png>)

![image 9](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile9.png>)

![image 10](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile10.png>)

![image 11](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile11.png>)

![image 12](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile12.png>)

![image 13](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile13.png>)

![image 14](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile14.png>)

![image 15](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile15.png>)

The Tura´n problem for hypergraph cycles has also been explored. There are several diﬀerent notions of hypergraph cycles. A hypergraph H is a Berge cycle of length ℓ if it consists of ℓ distinct edges e1,... ,eℓ such that there exists a list of distinct vertices x1,... ,xℓ satisfying that ∀i ∈ [ℓ − 1] ei contains both xi and xi+1 and that eℓ contains both xℓ and x1. Note that a 2-uniform Berge cycle of length ℓ is just the usual graph cycle of length ℓ. For r ≥ 3, however, r-uniform Berge cycles are not unique as there are no constraints on how the ei’s intersect outside {x1,... ,xℓ}. Let Bℓr denote the family of r-graphs that are Berge cycles of length ℓ. Gy˝ori and Lemons [22, 23] showed that for all r ≥ 3,ℓ ≥ 3, there exists a positive constant βr,ℓ, depending on r and ℓ such that ex(n,Bℓr) ≤ βr,ℓn1+

1

⌊ℓ/2⌋. Another notion of hypergraph cycles that has been actively investigated recently is that of a linear cycle deﬁned earlier. For ﬁxed r,ℓ, the r-uniform linear cycle Cℓr of length ℓ is unique up to isomorphism. We can also describe an r-uniform linear cycle using the notion of expansions. Given a 2-graph G, the r-expansion G(r) is the r-graph obtained from G by enlarging each edge of G into an r-set using r−2 new vertices, called expansion vertices, such that for diﬀerent edges of G we use disjoint sets of expansion vertices. So an r-uniform linear cycle of length ℓ is precisely the r-expansion of a cycle of length ℓ. Fu¨redi and Jiang [20] determined for all r ≥ 5,ℓ ≥ 3 and suﬃciently large n the exact value of ex(n,Cℓr), showing that ex(n,C2rm+1) = nr − n−rm and ex(n,C2rm) = nr − n−mr +1 + n−m2 −1 , respectively. Kostochka, Mubayi, and Verstrae¨te [30] have subsequently showed that the same holds for all r ≥ 3, ℓ ≥ 3, and suﬃciently large n. In this paper, we study the linear Tura´n number of Cℓr.

![image 16](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile16.png>)

Determining exL(n,C33) is equivalent to the famous (6,3)-problem,which is a special case of an old and general extremal problem of Brown, Erd˝os, and So´s [8]. The Brown-Erdo˝s-So´s problem asks to determine the function fr(n,v,e), which denotes the maximum number of edges in an r-graph on n vertices in which no v vertices spans e or more edges. The problem of estimating f3(n,6,3) is known as the (6,3)-problem. It is easy to see that exL(n,C33) = f3(n,6,3). In one of the classical results in extremal combinatorics, Ruzsa and Szemere´di [37] showed that for some constant c > 0,

√logn < f3(n,6,3) = o(n2). (1) Proposition 1.1 n2−c

![image 17](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile17.png>)

n2−c

√logn < exL(n,C33) = o(n2).

![image 18](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile18.png>)

Let us reiterate the following connection in the literature between f3(n,6,3) and the function r3(n), which denotes the largest size of a set of integers in [n] not containing a 3-term arithmetic progression.

Given n, let N = ⌊n6⌋ and let A be a subset of size r3(N) that contains no 3-term arithmetic

![image 19](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile19.png>)

progression. Let X,Y,Z be disjoint sets with X = [N],Y = [2N],Z = [3N], respectively. The 3-partite 3-graph H = {{x,y,z} : x ∈ X,y ∈ Y,z ∈ Z,∃a ∈ A y = x + a,z = x + 2a} satisﬁes that no six points spanns three or more edges and |H| = Nr3(N). Hence f(n,6,3) ≥ ⌊n6⌋ · r3(⌊n6⌋).

![image 20](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile20.png>)

![image 21](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile21.png>)

The upper bound in (1), established with a short proof using regularity lemma in [37], implies Roth’s theorem [35] that r3(n) = o(n). Conversely, the lower bound in (1) was established using Behrend’s [4] construction of large subsets of [n] not containing a 3-term arithmetic progression. Behrend’s construction has size Ω(n1−c′

√logn), for some constant c′ > 0. Ever since Roth’s theorem [35], the problem of estimating r3(n) has drawn much interest. The best current bounds are as follows: for some constant c > 0

![image 22](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile22.png>)

n ec

n (log n)1−o(1)

√logn ≤ r3(n) ≤

. (2)

![image 23](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile23.png>)

![image 24](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile24.png>)

![image 25](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile25.png>)

Back to the linear cycle problem, observe that the graph H constructed above is linear and contains no linear triangle. Using a construction similar to H and so-called 2-fold Sidon sets, Lazebnik and Verstrae¨te [31] constructed linear 3-graphs with girth 5 and Ω(n3/2) edges. On the other hand, it is not hard to show that exL(n,C43) = O(n3/2). Hence exL(n,C43) = Θ(n3/2). Kostochka, Mubayi, and Verstrae¨te [29] obtained the following bounds for exL(n,C53).

- Theorem 1.2 [29] There are constants a,b > 0 such that an3/2 < exL(n,C53) < bn3/2.

No lower or upper bounds on exL(n,Cℓr) were formerly known for ℓ  ∈ {3,4,5}. Kostochka, Mubayi, and Verstrae¨te [29] asked if for all r ≥ 3,ℓ ≥ 3, exL(n,Cℓr) = O(n1+

1

![image 26](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile26.png>)

⌊ℓ/2⌋) holds. We answer their question in the aﬃrmative in our main theorem below.

- Theorem 1.3 (Main theorem) For all r,ℓ ≥ 3, there exists a constant αr,ℓ > 0, depending on r and ℓ, such that


1

exL(n,Cℓr) ≤ αr,ℓn1+

⌊ℓ/2⌋.

![image 27](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile27.png>)

Another motivation for our study of exL(n,Cℓr) comes from the study of the hypergraph Ramsey number R(Cℓr,Ktr) of a linear cycle versus a complete graph. Such a study was initiated by Kostochka, Mubayi, and Verstrae¨te in [28]. Using Theorem 1.3 and other tools, we obtain nontrivial upper bounds on R(Cℓr,Ktr). Since our main emphasis of the paper is on the linear Tura´n problem of linear cycles, we delay the discussion of the related Ramsey numbers to Section 7.

The rest of the paper is organized as follows. Section 2 contains some notation and terminology. Section 3 contains some lemmas needed for our main theorem. Section 4 contains the proof of the main theorem for even cycles. Section 5 contains some additional tools needed for the proof for odd cycles. Section 6 contains the proof of the main theorem for odd cycles (which is much more involved than for even cycles). Section 7 contains results on cycle-complete hypergraph Ramsey numbers. Section 8 contains concluding remarks, including some discussion on the lower bounds on exL(n,Cℓr).

Our main method has roots in [15] and [24], but requires a substantial innovation for the odd cycle case. The new ideas used there could potentially have applications in other problems.

## 2 Notation and terminology

### 2.1 Degrees, neighborhoods, link graphs

Let G be a hypergraph. Given a set S ⊆ V (G), we deﬁne the degree of S in G, denoted by dG(S), to be the number of edges of G that contain S. Given a vertex x ∈ V (G), we deﬁne the link graph LG(x) of x in G as LG(x) = {e \ {x} : x ∈ e ∈ G}. Hence if G is an r-graph, then LG(x) is an (r − 1)-graph. The neigborhood NG(x) of x in G is deﬁned as NG(x) = {u ∈ V (G) : dG({u,x}) ≥ 1}. When the context is clear, we will drop the subscripts in the above deﬁnitions.

### 2.2 r-expansions

Let k,r be position integers where r > k ≥ 2. Given a k-graph H the r-expansion of H, denoted by H(r), is the r-graph obtained from H enlarging each edge e of H into an r-set through a set Ae of r − k new vertices, called expansion vertices, such that whenever e = e′ we have Ae ∩ Ae′ = ∅. So, for instance, the r-expansion of a 2-uniform ℓ-cycle is precisely an r-uniform linear ℓ-cycle. We will call H the skeleton of H(r).

### 2.3 Leveled linear trees

Given a 2-uniform tree T rooted at w, ∀i ≥ 0, let Li = {x : distT(w,x) = i}. We call Li level i. The height of T is the maximum i for which Li = ∅. For each x ∈ V (T), let Tx denote the subtree of T under x. Let H = T(r). Let f be a speciﬁc mapping of T to H that maps each e ∈ T to e ∪ A(e) where A(e) is the set of expansion vertices for e. We call H a leveled linear r-tree rooted at w and will refer to the Li’s as levels of H. The height of H is deﬁned to be the height of T. If x is a vertex in Li for some i, then the subtree under x in H, denoted by Hx, is the image under f of Tx in H.

### 2.4 Proper, rainbow, strongly proper, strongly rainbow edge-colorings

Let c be an edge-coloring of a 2-graph G using natural numbers. We say that c is proper if whenever e and e′ are incident edges in G, c(e) = c(e′) and we say that c is rainbow if for every two diﬀerent edges e and e′ in G we have c(e) = c(e′). Let φ be an edge-coloring of a 2-graph G using p-subsets of some ground set S. We say that φ is strongly proper if whenever e and e′ are incident edges in G, c(e) ∩ c(e′) = ∅. We say that φ is strongly rainbow if for every two diﬀerent edges e and e′ in G we have c(e) ∩ c(e′) = ∅.

### 2.5 Default edge-colorings

Let G be an r-graph. The 2-shadow ∂2(G) of G is the 2-graph consisting of all pairs (a,b) that are contained in some edge of G. If G is linear then each edge in ∂2(G) is contained in a unique edge of G. We deﬁne the default edge-coloring φ of ∂2(G) by letting φ({a,b}) = e \ {a,b}, where e is the unique edge of G containing {a,b}. So φ is a coloring whose colors are (r − 2)-sets. If B ⊆ ∂2(G) then the default edge-coloring of B is deﬁned to be φ restricted to B.

## 3 Lemmas

In this section, we prove some lemmas that will be needed in our main proofs. Let H be a hypergraph. A vertex cover of H is a set Q of vertices in H that contains at least one vertex of each edge of H. A cross-cut of H is a set S of vertices in H that contains exactly one vertex of each edge of H. A matching in H is a set of pairwise disjoint edges. The size of a matching is the number of edges in it.

- Lemma 3.1 Let H be a k-graph, where k ≥ 2. Let Q be a minimum vertex cover of H. Then H contains a matching of size at least |Q|/k.

Proof. Let M be a maximum matching in H and S the set of vertices contained in edges of M. If some edge e of H contains no vertex in S then M ∪e is a larger matching in H than M, contradicting our choice of M. So S is a vertex cover of H of size k|M|. Since Q is a minimum vertex cover of H, we have k|M| ≥ |Q|. Thus, |M| ≥ |Q|/k.

![image 28](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile28.png>)

- Lemma 3.2 Let H be a k-graph, where k ≥ 2. Let S be a vertex cover of H. Then there exist a subgraph H′ ⊆ H and a subset S′ ⊆ S such that |H′| ≥ 2kk|H| and that S′ is a cross-cut of H′. Proof. Let S be a random subset of S with each vertex of S chosen independently with probability

![image 29](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile29.png>)

- 1

![image 30](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile30.png>)

- 2. For each e ∈ H, the probability that exactly one vertex of e ∩ S is included in S is 2|e|e∩∩SS|| ≥ 2kk . So the expected number of edges e that intersects S in exactly one vertex is at least 2kk|H|. Thus,


![image 31](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile31.png>)

![image 32](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile32.png>)

![image 33](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile33.png>)

there exists a subset S of S such that at least 2kk|H| edges intersect S′ in exactly one vertex. Let H′ denote the subgraph of H consisting of these edges and S′ = S ∩ V (H′). The claim follows.

![image 34](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile34.png>)

![image 35](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile35.png>)

- Lemma 3.3 Let r ≥ 3. Let G be a linear r-graph. Let B ⊆ ∂2(G) satisfy that each edge of G contains at most one edge of B. Let φ be the default edge-coloring of B. Then φ is strongly proper.

Proof. Let f1,f2 be two edges in B that share a vertex, say u. Let e1,e2 be the unique edges of G containing f1,f2 respectively. By our assumption, e1 = e2. If e1 \ f1 and e2 \ f2 share a vertex v, then e1,e2 both contain {u,v}, contradicting G being linear. Thus φ({a,b}) ∩ φ({a,c}) = ∅.

![image 36](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile36.png>)

- Lemma 3.4 Let k,ℓ,s be positive integers, where k ≥ 2. Let G be a 2-graph with minimum degree at least (k +1)ℓ+s. Let φ be a strongly proper edge-coloring of G using k-subsets of some set S. Let x ∈ V (G) and S0 ⊆ S with |S0| ≤ s. Then there exists a path P in G of length ℓ starting at x such that (1) P is strongly rainbow under φ and (2) ∀f ∈ V (P), φ(f) ∩ S0 = ∅.


Proof. We use induction on ℓ. For the basis step, let ℓ = 1. By our assumption, there are at least k + s + 1 edges of G incident to x. Since φ is strongly proper, the colors used on these edges are pairwise disjoint k-sets. Certainly one of them is completely disjoint from S0. Let e be an edge incident to x with φ(e) ∩ S0 = ∅. The claim holds with P = e. For the induction step, let ℓ > 1. By induction hypothesis, there is a path P of length ℓ − 1 starting at x such that (1) P is strongly rainbow under φ and (2) ∀f ∈ P,φ(f) ∩ S0 = ∅. Let S1 = f∈P φ(f). Then |S1| = k(ℓ − 1). Let y denote the other endpoint of P. There at least (k + 1)ℓ + s edges incident to y. More than kℓ + s of

these join y to vertices outside P. Since φ is strongly proper, the colors on these edges are pairwise disjoint k-subsets of S. Since kℓ + s > k(ℓ − 1) + s = |S0 ∪ S1|, for one of these edges e, we have φ(e)∩(S0 ∪S1) = ∅. Now, P ∪e is a path of length ℓ in G starting at x such that (1) P ∪e is strongly rainbow under φ and (2) ∀f ∈ P ∪ e,φ(f) ∩ S0 = ∅.

![image 37](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile37.png>)

- Lemma 3.5 Let G be a graph with average degree d. There exists a subgraph G′ ⊆ G such that δ(G′) ≥ d4 and that |G′| ≥ |G2|. Proof. Suppose G has n vertices. Iteratively remove a vertex (and its incident edges) whose degree in the remaining subgraph is less than d4 until no such vertex exists. Let G′ denote the remaining subgraph. In the process, fewer than nd4 ≤ 12|G| edges have been removed. So |G′| ≥ |G2|. In particular, G′ is nonempty. By our rule, we also have δ(G′) ≥ d4.

![image 38](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile38.png>)

![image 39](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile39.png>)

![image 40](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile40.png>)

![image 41](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile41.png>)

![image 42](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile42.png>)

![image 43](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile43.png>)

![image 44](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile44.png>)

![image 45](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile45.png>)

- Lemma 3.6 Let G be an r-graph with average degree d. Then G contains a subgraph G′ with δ(G′) ≥ d/r.

Proof. Suppose G has n vertices. Starting with G, whenever some vertex has at most d/r in the remaining graph, we remove this vertex and all the edges in the remaining graph that contains this vertex. We repeat this procedure until there is no such vertex left. Let G′ denote the remaining graph. Clearly by our procedure at most (n − 1)(d/r) < nd/r = e edges have been removed in the process. So G′ is nonempty. Also, by our condition, δ(G′) ≥ d/r.

![image 46](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile46.png>)

Below we give a version of the Chernoﬀ bound from [32].

- Lemma 3.7 (Chernoﬀ bound) Let X be the sum of n independent random variables X1,... ,Xn, where for each i ∈ [n], Pr(Xi = 1) = p and Pr(Xi = 0) = 1 − p. Then for any real 0 ≤ α ≤ 1


- 2

![image 47](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile47.png>)

- 3 np.


Pr(|X − np| > αnp) < 2e−α

Recall that given a hypergraph G and a vertex x, the link graph LG(x) of x in G is the graph {e \ {x},e ∈ G,x ∈ e}. Given set S of vertices in G, the subgraph G[S] of G induced by S is the graph with vertex set S and edge set {e : e ∈ G,e ⊆ S}.

Proposition 3.8 Let c > 0 be a ﬁxed real. Let m,r,t ≥ 2 be ﬁxed positive integers. There exists a positive integer n0 depending on c,m,r,t such that for all n ≥ n0 the following holds. Let G be a linear r-graph with δ(G) ≥ cnm1 . Then there exists a partition of V (G) into t sets S1,... ,St such that for each u ∈ V (G) and each i ∈ [t], |LG(u) ∩ G[Si]| ≥ 2trc−1nm1 .

![image 48](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile48.png>)

![image 49](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile49.png>)

![image 50](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile50.png>)

Proof. Independently and uniformly at random assign each vertex in G a color from [t]. For each i ∈ [t] let Si be the set of vertices receiving color i. For each u ∈ V (G),i ∈ [t], let Yu,i be the random variable that counts the number of edges in LG(u) completely contained in Si. For ﬁxed u,i, clearly each edge of LG(u) has probability tr1−1 of being contained in Si. Since G is a linear r-graph, the edges of LG(u) are pairwise vertex-disjoint. So Yu,i is the sum of d(u) independent random variables each of which equals 1 with probability p = tr1−1 and 0 with probability 1 − p. By Lemma 3.7,

![image 51](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile51.png>)

![image 52](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile52.png>)

Pr Yu,i <

d(u) tr−1

- 1

![image 53](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile53.png>)

- 2


![image 54](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile54.png>)

d(u) tr−1 | >

< Pr |Yu,i −

![image 55](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile55.png>)

d(u) tr−1

- 1

![image 56](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile56.png>)

- 2


![image 57](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile57.png>)

d(u) tr−1

1 12

< 2exp −

![image 58](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile58.png>)

![image 59](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile59.png>)

.

Since d(u) ≥ cnm1 , this yields

![image 60](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile60.png>)

cnm1 12tr−1 .

cnm1 2tr−1 < 2exp −

![image 61](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile61.png>)

![image 62](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile62.png>)

Pr Yu,i <

![image 63](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile63.png>)

![image 64](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile64.png>)

Thus,

cnm1 2tr−1

![image 65](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile65.png>)

Pr ∃u ∈ V (G),∃i ∈ [t],Yu,i <

![image 66](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile66.png>)

cnm1 12tr−1

![image 67](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile67.png>)

< 2tn · exp −

![image 68](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile68.png>)

< 1,

for all n ≥ n0, where n0 depends only on c,m,r, and t. Thus there exists a particular coloring for which Yu,i ≥ cn

1 m

![image 69](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile69.png>)

2mr−1 for all u ∈ V (G) and i ∈ [t]. Let S1,... ,St be the color classes of this coloring. Then (S1,... ,St) forms a desired partition.

![image 70](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile70.png>)

![image 71](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile71.png>)

- 4 Linear Tur´an numbers of r-uniform even cycles The following lemma provides the main ingredient of our proof of Theorem 1.3 for even cycles.


- Lemma 4.1 Let r,m,h be ﬁxed integers, where r ≥ 3,m ≥ 2,0 ≤ h ≤ m − 1. Let positive integer


- i, let ci = (rm21r+2)i. Let G be a linear r-graph such that C2rm  ⊆ G. Let H be an r-uniform leveled linear trees of height h rooted at w that is contained in G. Let L0,... ,Lh denote the levels of H. Let E be a set of edges in G each of which contains one vertex in Lh and r − 1 vertices outside H. Suppose that |E| ≥ (m2r+3)h|Lh|. Then there exists a subset E∗ of E such that |E∗| ≥ ch|E| and that E∗ \ Lh is a matching. In particular, H ∪ E∗ is a leveled linear trees of height h + 1 rooted at


![image 72](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile72.png>)

- w, with Lh+1 consist of one vertex of e \ Lh for each e ∈ E∗.


- Proof. We use induction on h. For the basis step let h = 0 and H consists of a single vertex w. By our assumption, E is a set of edges containing w. Since G is linear, every two of these edges intersect only at w. Let E∗ = E. It is easy to see that the claim holds.


For induction step, let h ≥ 1. Suppose T is a 2-uniform tree of height h rooted at w with levels L0,L1,... ,Lh and H = T(r) ⊆ G. By our assumption, each edge in E contains one vertex in Lh and r −1 vertices outside H. Let F = {e\Lh : e ∈ E}. Then F is an (r −1)-graph. Since G is linear and r ≥ 3, the mapping σ : E → F that maps e to e\L1 is a bijection. So |F| = |E|. Let Q be a minimum vertex cover of F. By Lemma 3.2, there exist F′ ⊆ F and Q′ ⊆ Q such that |F′| ≥ 2rr−−11|F| = 2rr−−11|E| and that Q′ is a cross-cut of F′. Let E′ be the set of edges of E corresponding to edges of F′ (via σ−1). Then |E′| = |F′| and each edge of E′ contains exactly one vertex of Lh, one vertex of Q′, and r − 2 vertices outside V (H) ∪ Q′. Let B = {e ∩ (Lh ∪ Q′) : e ∈ E′}. By deﬁnition, B is a bipartite 2-graph with a bipartition (X,Q′) where X = V (B) ∩ Lh. The mapping f : e → e ∩ (Lh ∪ Q′) is a bijection from E′ to B ⊆ ∂2(G). So

![image 73](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile73.png>)

![image 74](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile74.png>)

r − 1 2r−1 |E|.

|B| = |E′| = |F′| ≥

![image 75](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile75.png>)

Clearly, no edge of G contains more than one edge of B and in the default edge-coloring φ of B the colors are disjoint from V (B) ∪ V (H).

Let x1,... ,xp denote the children of w in T. For each i ∈ [p], let Ai = V (Txi)∩Lh. So Ai consists of vertices in Lh that are descendants of xi (in T). Note that A1,... ,Ap are pairwise disjoint. Let

Q+ = {x ∈ Q′ : NB(x) ∩ Ai = ∅ for at least 2rm diﬀerent Ai’s} Q− = {x ∈ Q′ : NB(x) ∩ Ai = ∅ for fewer than 2rm diﬀerent Ai’s}

- Then Q+ and Q− partition Q′. Let B+ denote the subgraph of B induced by X ∪ Q+ and B− the subgraph of B induced by X ∪ Q−. Then B = B+ ∪ B−.


Claim 1. |Q′| ≥ ch8−rm1|B|. Proof of Claim 1. We consider two cases.

![image 76](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile76.png>)

Case 1. |B+| ≥ 12|B|. By our earlier discussion, |B| ≥ 2rr−−11|E|. So |B+| ≥ |B2| > (r−21)r|E|. We claim that |Q+| ≥ |B

![image 77](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile77.png>)

+| 4rm . Suppose for contradiction that |Q+| < |B

![image 78](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile78.png>)

![image 79](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile79.png>)

![image 80](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile80.png>)

![image 81](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile81.png>)

+|

4rm . Then |B+| ≥ 4rm|Q+|. By our assumption |E| ≥ (m2r+3)h|Lh| ≥ (m2r+3)h|X|. Hence |B+| ≥ (r−1)(m2

![image 82](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile82.png>)

r+3)h

2r |X| ≥ 4rm|X|. So |B+| ≥ 2rm(|X| + |Q′|) = 2rm|V (B+)|. Thus, B+ has average degree at least 4rm. By a well-known fact, B+ contains a subgraph B∗ with minimum degree at least 2rm. Let φ be the default edge-coloring of B∗. By Lemma 3.3, φ is strongly proper. Let x be any vertex in V (B∗) ∩ Q+. By Lemma 3.4, B∗ contains a path P of length 2m − 2h − 2 starting at x that is strongly rainbow under φ. Since B∗ is bipartite and 2m − 2h − 2 is even, the other endpoint y of P lies in Q+. Now the r-graph P+ with edge set {e ∪ φ(e) : e ∈ P} is a linear path of length 2m − 2h − 2 with endpoints x and y using edges of

![image 83](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile83.png>)

- E′ ⊆ E. By the deﬁnition of E, V (P+) ∩ V (H) ⊆ Lh. Now, since x ∈ Q+, by deﬁnition, NB(x) ∩ Ai = ∅ for at least 2rm diﬀerent i’s. Without loss of


generality suppose NB(x) ∩ Ai = ∅ for i = 1,... ,2rm. For each i ∈ [2rm], let ui ∈ NB(x) ∩ Ai and let ei be the unique edge of E containing xui. Since G is linear, e1 \ {x},... ,e2rm \ {x} are pairwise disjoint. Since there are clearly fewer than 2rm vertices contained in P+, for some i ∈ [2rm], ei \{x} is vertex disjoint from P+. Without loss of generality, suppose e1 \ {x} is vertex disjoint from P+. Likewise, since y ∈ Q+, we can ﬁnd an edge f1 ∈ E′ containing y intersecting some Aj such that

- j = 1 and that f1 \ {y} is disjoint from V (P+) ∪ e1. Without loss of generality, suppose j = 2. Let {v1} = f1 ∩ A2. Let P1 be the unique u1,w-path and P2 the unique v1,w-path in H, respectively. Since x1 and x2 are diﬀerent children of w in T, P1,P2 are two internally disjoint paths of length h,


sharing only w. Now P+ ∪{e1,f1} ∪P1 ∪ P2 is a linear cycle of length 2m −2h −2 +2 +2h = 2m in

+|

4rm ≥ 8|rmB| and thus |Q′| ≥ 8|rmB| ≥ ch8−rm1|B|. Case 2. |B−| ≥ 21|B|.

- G, contradicting our assumption about G. Hence |Q+| ≥ |B


![image 84](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile84.png>)

![image 85](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile85.png>)

![image 86](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile86.png>)

![image 87](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile87.png>)

![image 88](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile88.png>)

We have |B−| ≥ |B2| ≥ (r−21)r|E|. For each vertex x ∈ B−, by our assumption, NB(x) ∩ Ai = ∅ for fewer than 2rm diﬀerent i’s. Among the Ai’s that receive edges of B− from x, let Ai(x) be one that receives the most edges of B from x. We now form a subgraph B1− of B− by including for each

![image 89](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile89.png>)

![image 90](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile90.png>)

- x ∈ Q− the edges from x to Ai(x). By our procedure,


|B−| 2rm ≥

(r − 1)|E| rm2r+1 ≥

|B1−| ≥

![image 91](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile91.png>)

![image 92](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile92.png>)

r − 1 rm2r+1

(m2r+3)h|Lh| ≥ 2(m2r+3)h−1|Lh|. (3)

![image 93](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile93.png>)

Recall that A1,... ,Ap are disjoint subsets of Lh. In B1−, each vertex in Q− sends edges to at most one Ai. For each Ai, call Ai light if the number of edges of B1− incident to Ai is less than (m2r+3)h−1|Ai|; otherwise call Ai heavy. Clearly the total number of edges of B− that are incident to light Ai’s is at most (m2r+3)h−1|Lh|, which is at most 12|B1−| by (3). So the number of edges of B1− that are incident to heavy Ai’s is at least 12|B1−|.

![image 94](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile94.png>)

![image 95](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile95.png>)

Without loss of generality, suppose that A1,... ,At are the heavy Ai’s. For each i ∈ [t], let Qi be the set of vertices in Q− that are joined by edges of B1− to Ai. By our deﬁnition of B1−, Q1,... ,Qt are pairwise disjoint. Also, for each i ∈ [t], let Ei be the set of edges of E′ corresponding to the set of edges of B1− that are incident to Ai. By our assumption |Ei| ≥ (m2r+3)h−1|Ai|. Recall that x1,... ,xp denote the children of w in T. For each i ∈ [t], Hxi is a linear tree of height h − 1 rooted at xi whose (h − 1)-th level is Ai. Each edge of Ei contains one vertex of Ai and r − 1 vertices outside Hxi and |Ei| ≥ (m2r+3)h−1|Ai|. By induction hypothesis, there exists Ei′ ⊆ Ei such that |Ei′| ≥ ch−1|Ei| and Ei′ \ Ai is a matching. In particular, this yields |Qi| ≥ ch−1|Ei|. Hence |Q′| ≥ |Q−| ≥ ti=1 |Qi| ≥ ch−1 ti=1 |Ei| ≥ ch−1|B

−

−|

- 1 |

![image 96](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile96.png>)

- 2 ≥ ch−1|B


4rm ≥ ch8−rm1|B| by (3). This proves

![image 97](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile97.png>)

![image 98](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile98.png>)

- Claim 1.


![image 99](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile99.png>)

By Claim 1, we have |Q| ≥ |Q′| ≥ ch8−rm1|B| ≥ (r−2r1)−c1h8−rm1|E| = (r−rm1)c2hr−+21|E|. By Lemma 3.1, F contains

![image 100](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile100.png>)

![image 101](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile101.png>)

![image 102](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile102.png>)

a matching F∗ of size at least rmch−21r|+2E| = ch|E|. Let E∗ be the set of edges of E corresponding to F∗. Then |E∗| = |F∗| and H ∪E∗ is a leveled linear tree of height h+1 rooted at w with Lh+1 consisting of one vertex of each edges in F∗.

![image 103](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile103.png>)

![image 104](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile104.png>)

Theorem 4.2 Let m,r be positive integers where m ≥ 2 and r ≥ 3. There exist a positive real cm,r

- and a positive integer n1 such that for all n ≥ n1 we have


exL(n,C2rm) ≤ cm,rn1+m1 .

![image 105](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile105.png>)

1 m

Proof. Let β = (rm2r+2)m and cm,r = 2mr−1β. Choose n1 such that cm,rn

![image 106](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile106.png>)

1 ≥ n0, where n0 is given in Lemma 3.8. Let G be an n-vertex linear r-graph with at least cm,rn1+m1 edges, where n ≥ n1. We prove that G contains a copy of C2rm. By our assumption, G has average degree at least rcm,rnm1 . By Lemma 3.6, there exists a subgraph G′ of G with δ(G′) ≥ cm,rnm1 . Let N = n(G′). Then N ≥ cm,rnm1 ≥ n0 and δ(G′) ≥ cm,rN m1 . By Lemma 3.8 (with t = m), there exists a partition of V (G′) into S1,... ,Sm such that for each u ∈ V (G′) and i ∈ [m], we have |LG′(u) ∩ G′[Si]| ≥ 2mcm,rr−1N m1 = βN m1 .

![image 107](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile107.png>)

![image 108](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile108.png>)

![image 109](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile109.png>)

![image 110](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile110.png>)

![image 111](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile111.png>)

![image 112](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile112.png>)

![image 113](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile113.png>)

![image 114](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile114.png>)

Let w be any vertex in S1. Let L0 = {w}. Inside G′, we will construct a leveled linear tree H of height m rooted at w with levels L1,... ,Lm such that for each i ∈ [m], Li ⊆ Si and |Li| ≥ N m1 |Li−1|. This will imply that |Lm| ≥ N, which is a contradiction, which will then complete our proof.

![image 115](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile115.png>)

We construct H as follows. Let E1 be the set of edges of G′ containing w that correspond to LG′(w) ∩ G′[S1]. By our assumption, |E1| ≥ βN m1 ≥ N m1 , by our deﬁnition of β. Also, each edge of E1 consists of w and r − 1 vertices in S1. Let L1 consists of a vertex from e \ {w} for each e ∈ E1. In general, suppose we have grown i levels L1,... ,Li, where i ≤ m − 1, such that for each j ∈ [i], Lj ⊆ Sj and |Lj|/|Lj−1| ≥ N m1 . Let Ei denote the set of edges in G′ that contain one vertex in Li and r − 1 vertices in Si+1. By our assumption about the partition (S1,... ,Sm), |Ei| ≥ βN m1 |Li| ≥ (m2r+3)m|Li|, noting that β ≥ (m2r+3)m. Since C2rm  ⊆ G′, by Lemma 4.1, there exists a subset Ei∗ ⊆ Ei such that |Ei∗| ≥ (rm21r+2)i|Ei| such Ei∗ \ Li is a matching. Let

![image 116](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile116.png>)

![image 117](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile117.png>)

![image 118](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile118.png>)

![image 119](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile119.png>)

![image 120](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile120.png>)

Hi+1 = Hi ∪ Ei∗ and let Li+1 consists of one vertex from e \ Li for each e ∈ Ei∗. Then Hi+1 is a leveled linear tree rooted at w of height i + 1 whose i + 1-th level Li+1 is contained in Si+1. Furthermore, |Li+1| = |Ei∗| ≥ (rm21r+2)i|Ei| ≥ (rm2βr+2)iN m1 |Li| ≥ N m1 |Li|. We can continue like this to construct H and derive the desired contradiction.

![image 121](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile121.png>)

![image 122](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile122.png>)

![image 123](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile123.png>)

![image 124](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile124.png>)

![image 125](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile125.png>)

## 5 Leveled linear quasi-trees 5.1 Leveled linear quasi-trees

To study the odd cycle case, we generalize the notion of leveled linear trees as follows. Let r ≥ 3. A linear r-graph H is called a leveled linear quasi-tree of height h rooted at w if it is the union of a sequence of r-graphs H0,H1,... ,Hh−1 satisfying the following: (1) Each Hi is an r-partite r-graph with no isolated vertex and has parts Li,L′i,Ji(1),... ,Ji(r−2) such that with Bi = {e ∩ (Li ∪ L′i) : e ∈ Hi}, Hi is the r-expansion of Bi. (2) For each i = 0,1,... ,h − 1, Ji(r−2) = Li+1. (3) For each i = 0,1,... ,h − 2, V (Hi) ∩ V (Hi+1) = Li+1 and V (Hi) ∩ V (Hj) = ∅ whenever |i − j| > 1. (4) L0 = {w}. For each i = 0,... ,h, we call Li the ith main level of H. For each i = 0,... ,h − 1, we call L′i the ith companion level of H.

For each i ∈ {0,1,... ,h − 1}, we call Hi the i-th segment of H and Bi the deﬁning bipartite graph of Hi. For each edge f of Bi the unique vertex in Li+1 that corresponds to f is said to be a presentative of e. Given x ∈ V (Bi) and y ∈ Li+1, we say that y is a child of x and that x is a parent of y if y is a representative of an edge of Bi incident to x. Observe that every two diﬀerent vertices u,v in the same main level Li or in the same companion level L′i, where i ≤ h−1, must have disjoint sets of children in Li+1 since the sets of edges of Bi incident to u and v, respectively, are disjoint.

Given a vertex x ∈ Li ∪ L′i, where i ≤ h − 1, deﬁne the down tree Tx, rooted at x, to be the 2-graph obtained by including all the edges between A0 = {x} and its set A1 of children in Li+1, and then including all the edges joining vertices in A1 and the set A2 of their children in Li+2 and etc, until we run out of levels. It is easy to see that Tx is a tree rooted at x of height at most h−i. Also, if x,y ∈ Li or x,y ∈ L′i, x = y, then the earlier observation about disjoint sets of children implies that V (Tx) ∩ V (Ty) = ∅. Furthermore, in Tw, where w is the root of H, for each i = 0,... ,h, the i-th distance class from w is precisely all of Li.

Given a vertex x ∈ Li ∪ L′i, where i ≤ h − 1, deﬁne the down graph Hx, rooted at x, to be the subgraph of H obtained by replacing each edge f of Tx with the corresponding edge e of H that contains f. The following lemma follows immediately from the deﬁnitions and our discussions above.

- Lemma 5.1 Let H be an r-uniform leveled linear quasi-tree of height h rooted at w with segments


- H1,... ,Hh−1. Let x ∈ Li ∪ L′i, where 0 ≤ i ≤ h − 1. Then Hx is a leveled quasi-tree of height at most h − i rooted at x. Also, ∀a,b ∈ Li ∪ L′i, a = b, if either a,b ∈ Li or a,b ∈ L′i, then (V (Ha) ∩ V (Hb)) ∩ Lj = ∅ for all j ≥ i + 1.


In a linear r-graph, a path P is just the r-expansion of a 2-uniform path. An endpoint of P is a vertex in the ﬁrst or last edge that has degree 1 in P. An x,y-path is a path where x is an endpoint in the ﬁrst edge of P and y is an endpoint in the last edge of P (or vice versa).

- Lemma 5.2 Let H be an r-uniform leveled linear quasi-tree of height h rooted at w with segments

H1,... ,Hh−1, where L0,L1,... ,Lh and L′0,... ,L′h−1 denote the main levels and companion levels, respectively. Let x,y ∈ Li,x = y, where 1 ≤ i ≤ h − 1. Then there exists an x,y-path P of an even length at most 2i that is contained in ij−=01 Hj and intersects Li only in x and y.

Proof. We use induction on i. The claim is trivial when i = 1. So assume i ≥ 2. Let e be the unique edge of Hi that contains x and f the unique edge of Hi that contains y. If e and f share a vertex, then e ∪ f is an x,y-path of length 2. Otherwise e ∩ f = ∅. Let {x′} = e ∩ Li−1 and {y′} = f ∩ Li−1. By induction hypothesis, there is an x′,y′-path P of an even length at most 2(i−1) that is contained in ij−=02 Hj and intersects Li−1 only in x′ and y′. Now, P ∪ {e,f} is an x,y-path of an even length at most 2i that is contained in ij−=01 Hj and intersects Li only in x and y.

![image 126](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile126.png>)

Given a leveled linear quasi-tree H rooted at w, a monotone path is a path in H that hits each main level at most once. It is easy to see that for every vertex x in the i-th main level, there is a unique monotone w,x-path, and that path has length i. For every vertex y in the ith companion level, there exists at least one monotone w,y-path and such a path has length i + 1.

An r-uniform spider F with t legs consists of p r-uniform linear paths P1,... ,Pt (called the legs) sharing one endpoint x but are otherwise vertex-disjoint.

- Lemma 5.3 Let h,p,r be positive integes, where r ≥ 3. Let H be an r-uniform leveled linear quasi-


tree of height h rooted at w with segments H1,... ,Hh−1. Let L0,... ,Lh and L′0,... ,L′h−1 be the main levels and companion levels, respectively. Let S ⊆ Lh such that |S| ≥ (hpr)h. Then exists a vertex x ∈ V (H) such that 1) |V (Hx) ∩ S| ≥ (hpr1)h−1|S| and (2) Hx contains a spider centered at x that has p legs each of which is a monotone path from x to V (Hx) ∩ S.

![image 127](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile127.png>)

Proof. We use induction on h. For the basis step let h = 1. In this case, the claim clearly holds by choosing x to be w and p of the edges containing x to form the required spider. For the induction step, let h ≥ 2. Clearly there is at least one monotone path from the root w to S, so there exist spiders centered at w with legs being monotone paths from w to S. Let us call these (w,S)-spiders. Among all (w,S)-spiders, let M be one that has the maximum number of legs. If M has p legs, then the claim holds with x = w. So assume M has fewer than p legs. For each y ∈ S, let Py be the unique monotone path in H from w to y. The maximality of M implies that each y ∈ S, Py intersects M somewhere besides at w. Let y ∈ S. If Py intersects M at a vertex u in V (Hi)\{Li,L′

i} for some i ≤ h−1 then such a vertex is an expansion vertex in Hi and both Py and M must contain the corresponding edge e of Hi that contains u and hence both contain e ∩ Li and e ∩ Li+1. Thus, for each y ∈ S, Py contains a vertex in U = (V (F) \ {w}) ∩ ( hi=1−1(Li ∪ L′i)).

Since U has fewer than phr vertices, by the pigeonhole principle, there exists a vertex z in U that is contained in at least ⌈hprs ⌉ diﬀerent Py’s. Suppose that z ∈ La ∪ L′a. Let S′ be the set of vertices

![image 128](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile128.png>)

- y in S such that Py contains z. Then |S′| ≥ hpr|S| . For each y ∈ S′, let Py′ be the z,y-path contained in Py. Let H′ = y∈S Py′. Then H′ ⊆ Hz. Now, Hz is a leveled linear quasi-tree with height at most


![image 129](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile129.png>)

- h − 1 and S′ is a set of vertices in its last level. By the induction hypothesis, there is a vertex x in


′|

[(h−1)pr]h−2 ≥ (hpr|S)h|−1 and that (Hz)x contains a (z,V (Hz(x)) ∩ S′)spider with p legs. Consider now the relationship between (Hz)x and Hx. Since x sends multiple

Hz such that |V ((Hz)x) ∩ S′| ≥ |S

![image 130](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile130.png>)

![image 131](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile131.png>)

internally disjoint monotone paths to S it is easy to see that either x = z or x ∈ Lj ∪ L′j for some

- j ≥ a + 1. In either case, we have (Hz)x = Hx.


![image 132](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile132.png>)

## 6 Linear Tur´an numbers of odd cycles

The following lemma provides the key ingredient for our proof of Theorem 1.3 for odd cycles. Before presenting the technical details, let us point out what the main technical challenge is for the odd cycle case and what the key new ideas are in overcoming the diﬃculty. The general plan is similar to the even cycle case. We use a linear quasi-tree as a framework for growing levels and argue that in the absence of C2rm+1 the graph must expand quickly. The main diﬀculty we face is that linear quasi-trees have a interweaving structure and no longer possess a clean tree structure. Therefore, we cannot hope to link vertices cleanly back to the root. The key idea to overcome this diﬃculty is to apply Lemma 5.3 to locate a set of vertices (called “dominators”) at some earlier level to act as a group of roots for diﬀerent vertices. This idea of untangling via a buﬀer can be useful elsewhere.

- Lemma 6.1 Let r,m,h be integers, where r ≥ 3, m ≥ 2, and 0 ≤ h ≤ m − 1. Let p = 2mr and c = 2r+2(mpr)m. Let G be a linear r-graph such that C2m+1  ⊆ G. Let H be an r-uniform leveled linear quasi-tree of height h in G rooted at w with segments H0,H1,... ,Hh−1, levels L0,L1,... ,Lh and companion levels L′1,... ,L′h−1. Let S be a set of vertices in G outside H and E a set of edges in


- G each of which contains one vertex in Lh and r − 1 vertices outside H. Suppose that |E| ≥ ch|Lh|.


Then there exists a subset E∗ of E and a set S of vertices outside H such that (1) |E∗| ≥ c1h|E|, (2) S is a cross-cut of E∗, (3) E∗ is the r-expansion of the 2-graph Γ = {e ∩ (Lh ∪ S) : e ∈ E∗} and (4) either δ(Γ) ≥ p or each vertex in S has degree 1 in Γ. In particular, H ∪ E∗ is a leveled

![image 133](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile133.png>)

linear quasi-tree of height h+1 rooted at w, where L′h = S and Lh+1 consists of one vertex from each member of E∗ \ (Lh ∪ S).

Proof. We use induction on h. For the basis step, let h = 0. Then H consists of the single vertex w and E is a set of edges containing w. Let E∗ = E and let S consist of one vertex of e \ {w} for each

- e ∈ E∗. It is easy to see that the claim holds. For the induction step, let h ≥ 1. Let E be deﬁned as in the statement of the lemma. Let


- F = {e \ Lh : e ∈ E}. Then F is an (r − 1)-graph with |F| = |E|. Let Q be a minimum vertex cover


- of F. First suppose that |Q| ≥ rc−h1|E|. By Lemma 3.1, F contains a matching F∗ of size at leat |Q| r−1 ≥ c1h|E|. Let E∗ be the set of edges of E corresponding to F∗. Let S = E∗ ∩ Q′. It is easy to check that E∗ and S satisfy the four conditions and we are done. We henceforth assume that


![image 134](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile134.png>)

![image 135](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile135.png>)

![image 136](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile136.png>)

r − 1 ch |E|. (4)

|Q| <

![image 137](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile137.png>)

By Lemma 3.2, there exists F′ ⊆ F and Q′ ⊆ Q such that |F′| ≥ 2rr−−11|F| and that Q′ is a cross-cut of F′. Let E′ be the set of edges in E corresponding to F′. Then |E′| = |F′| and each edge in E intersects each of Lh and Q′ in exactly one vertex. Let B = {e ∩ (Lh ∪ Q′) : e ∈ E′}. Then B satisﬁes the condition of Lemma 3.3 and there is a bijection between edges of B and edges of E′. In particular,

![image 138](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile138.png>)

r − 1 2r−1 |E|. (5)

|B| = |E′| ≥

![image 139](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile139.png>)

h

2r−1 |Lh| ≥ 32hmr|Lh|. Also, by (5), |B| ≥ 2rr−−11|E| ≥ 2rc−h1|Q′| ≥ 32hmr|Q′|. So, |B| ≥ 32hmr(|Lh| + |Q′|) ≥ 16hmr|V (B)|. Thus B has average degree at least 32hmr.

Now, |B| ≥ 2rr−−11|E| ≥ (r−1)c

![image 140](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile140.png>)

![image 141](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile141.png>)

![image 142](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile142.png>)

![image 143](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile143.png>)

We now partition Q′ as follows. Let

Q− = {y ∈ Q′ : dB(y) < (mpr)m} and Q+ = {y ∈ Q′ : dB(y) ≥ (mpr)m}.

Let B− be the subgraph of B induced by Lh ∪ Q− and the subgraph of B induced by Lh ∪ Q+.

- Case 1. |B−| ≥ |B2|.

![image 144](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile144.png>)

In this case, we have |Q| ≥ |Q−| > |B

−|

![image 145](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile145.png>)

(mpr)m ≥ 2(mpr|B|)m ≥ 2r((rmpr−1))m |E| > rc−h1|E|, contradicting (4).

![image 146](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile146.png>)

![image 147](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile147.png>)

![image 148](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile148.png>)

- Case 2. |B+| ≥ |B2|. In this case, we partition Q+ as follows. Let y ∈ Q+. Then NB(y) ⊆ Lh and |NB(y)| ≥ (mpr)m.


![image 149](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile149.png>)

By Lemma 5.3, there exists x ∈ V (H) such that |V (Hx) ∩ NB(y)| ≥ (|hprNB)(hy−)|1 and such that Hx contains a spider M with p legs from x to NB(y) using monotone paths. Let us call such an x a dominator of y in H. Suppose V (M) ∩ NB(y) = {y1,... ,yp}. For each j = 1,... ,p, let fj be the unique edge of E containing yyi. It is easy to see that M ∪ {f1,... ,fp} form a collection of p internally disjoint x,y-paths that intersect each main level of H at most once. In particular, if x ∈ Li ∪ L′i, where i ≤ h − 1, then these paths all have length h − i + 1.

![image 150](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile150.png>)

For each y ∈ Q+, ﬁx a dominator α(y) of y in H. Note that either α(y) = w or α(y) ∈ Li ∪L′i for some 1 ≤ i ≤ h−1, since other vertices in H have degree 1 in H and cannot possibly be a dominator of y. Let Q0 = {y ∈ Q+ : α(y) = w}. For each i = 1,... ,h − 1, let Qi = {y ∈ Q+ : α(y) ∈ Li} and Q′i = {y ∈ Q+ : α(y) ∈ L′i}. Then Q0,Q1,Q′1,... ,Qh−1,Q′h−1 partition Q+. Let B0 denote the subgraph of B+ induced by Q0 ∪ Lh. For each i = 1,... ,h − 1, let Bi denote the subgraph of B+ induced by Qi∪Lh and Bi′ the subgraph of B+ induced by Q′i∪Lh. Then B0,B1,B1′ ,... ,Bh−1,Bh′ −1 partition B+. One of these graphs must then have size at least |B

+| 2h . Subcase 2.1. |B0| ≥ |B

![image 151](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile151.png>)

+| 2h .

![image 152](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile152.png>)

In this subcase, we have |B0| ≥ |4Bh|. Since V (B0) ⊆ V (B) and B has average degree at least 32hmr by earlier discussion, B0 has average at least 8mr. By Lemma 3.5, B0 contains a subgraph B0′ with δ(B0′ ) ≥ 2mr and |B0′| ≥ |B20| ≥ |8Bh|.

![image 153](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile153.png>)

![image 154](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile154.png>)

![image 155](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile155.png>)

Claim 1. The default coloring φ on B0′ is strongly rainbow.

Proof of Claim 1. Let e,e′ ∈ B0′ . First suppose that they are incident in B0′ . Then since φ is strongly properly on B0′ by Lemma 3.3, we have φ(e) = φ(e′). Next, suppose e,e′ are independent in B0′. Suppose for contradiction that φ(e) ∩ φ(e′) = ∅. Let v ∈ φ(e) ∩ φ(e′). Since H is linear, we have φ(e)∩φ(e′) = {v}. Suppose e = xy,e′ = x′y′ where x,x′ ∈ Lh and y,y′ ∈ Q0. Since B0′ has minimum degree at least 2rm, applying Lemma 3.4 with k = r − 2,ℓ = 2m − 2 − 2h and S0 = φ(e) ∪ φ(e′), B0′ contains a path P of length 2m − 2 − 2h starting at y′ such that P is strongly rainbow under φ and that ( f∈P φ(f)) ∩ (φ(e) ∪ φ(e′)) = ∅. Let y′′ denote the other endpoint of P; it is possible that y′′ = y′. The set of edges of E that correspond to those in P ∪ {e,e′} forms a linear path R of length 2m − 2h in which we may view x as one endpoint at one end and y′′ as an endpoint at the other end. Let Rx be a monotone path in H from w to x. Then R ∪ Rx is a linear path of

- length 2m − 2h + h = 2m − h with w being an endpoint at one end and y′′ being an endpoint at the


other end. Since y′′ ∈ Q0, w is a dominator of y′′. Hence there exist p pairwise internally disjoint

- w,y′′-paths of length h + 1. Since p = 2mr > |V (R ∪ Rx)|, one of these paths, say R′, is internally disjoint from R ∪ Rx. Now R ∪ Rx ∪ R′ is a linear cycle of length 2m + 1 in G, a contradiction. This proves Claim 1.


![image 156](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile156.png>)

+|

Let E∗ be the set of edges in E corresponding to those in B0′ . Then |E∗| = |B0′ | ≥ |B20| ≥ |B

4h ≥

![image 157](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile157.png>)

![image 158](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile158.png>)

- |B|


- 8h ≥ 2rr+2−1h|E|, by (5). So, certainly |E∗| ≥ c1h|E|. Since φ is strongly rainbow on B0, E∗ is the r-expansion of B0′. Also, δ(B0′ ) ≥ 2mr = p. The lemma holds with S = V (B0′) ∩ Q′ and Γ = B0′.


![image 159](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile159.png>)

![image 160](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile160.png>)

![image 161](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile161.png>)

+|

Subcase 2.2 |Bi| ≥ |B

2h for some 1 ≤ i ≤ h − 1.

![image 162](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile162.png>)

Fix such an i. We deﬁne a subgraph D of Bi as follows. For each y ∈ Qi, by deﬁnition, α(y) ∈ Li, we include all the edges of Bi from y to V (Hα(y)) ∩ NB(y) in D. Since ∀y ∈ Qi, |V (Hα(y) ∩ NB(y)| ≥ (|hprNB)(hy−)|1, using (5) we have

![image 163](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile163.png>)

ch 2r+1m(mpr)m−1|Lh|. (6)

|B| 4h(hpr)h−1 ≥

r − 1 2r+1m(mpr)m−1|E| >

|Bi| (hpr)h−1 ≥

|D| ≥

![image 164](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile164.png>)

![image 165](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile165.png>)

![image 166](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile166.png>)

![image 167](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile167.png>)

For each x ∈ Li, let Ax = Lh ∩ V (Hx). By Lemma 5.1, ∀x,x′ ∈ Li,x = x′ we have Ax ∩ Ax′ = ∅. For each x ∈ Li, let Dx denote the subgraph of D consisting of edges of D that are incident to Ax and let Cx = V (Dx) ∩ Qi. By our deﬁnition of D, the sets Cx are pairwise disjoint over diﬀerent vertices

- x in Li. Let Ex denote the set of edges in E correspond to the edges of Dx. Then |Ex| = |Dx|. Furthermore, each edge in Ex contains exactly one vertex in Ax and exactly one vertex in Cx.


For each x ∈ Li we call x light if |Dx| ≤ ch−1|Ax| and heavy if |Dx| > ch−1|Ax|. Clearly, the combined size of Dx over all light x in Li is at most ch−1|Lh|. By our deﬁnition of c, one can check that 2r+2m(cmprh )m−1 ≥ 2ch−1. So by (6) and our discussion above,

![image 168](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile168.png>)

- 1

![image 169](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile169.png>)

- 2|D|. (7)


| {Dx : x ∈ Li,x is heavy }| ≥

Now, consider any heavy x ∈ Li. Since Hx is a leveled linear quasi-tree rooted at x of height

- h − i ≤ h − 1 with last level Ax and Ex is a set of at least ch−1|Ax| edges each of which contains one vertex in Ax and r − 1 vertices outside Hx, we can apply the induction hypothesis to obtain


Ex∗ and Sx, described as below. Here Ex∗ is a subset of Ex with |Ex∗| ≥ ch1−1|Ex|, Sx∗ is a cross-cut of Ex∗ outside Hx. By our deﬁnition of E, Sx∗ is outside H. Further, the default edge-coloring of Γx = {e ∩ (Lh ∪ Sx) : e ∈ Ex∗} is strongly rainbow and either δ(Γx) ≥ p or ∀v ∈ Sx,dΓx(v) = 1. We say that x is of type 1 if δ(Γx) ≥ p and that x is of type 2 otherwise. Observe that if x is of type 2, then Ex∗ \ Lh is a matching of size |Ex∗|. Since each edge in Ex∗ ⊆ Ex contains a vertex of Cx, this implies that |Cx| ≥ |Ex∗|.

![image 170](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile170.png>)

Let Li,1 = {x ∈ Li,x is heavy and is of type 1} and Li,2 = {x ∈ Li,x is heavy and is of type 2}. Suppose ﬁrst that x∈L

|Dx| ≥ 41|D|. By (6),

|Ex| ≥ 41|D|. Then x∈L

![image 171](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile171.png>)

![image 172](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile172.png>)

i,2

i,2

|Q| ≥ |Qi| ≥

|Cx| ≥

x∈Li,2

x∈Li,2

r − 1 ch−12r+3m(mpr)m−1|E| ≥

r − 1 ch |E|,

1 4ch−1|D| ≥

1 ch−1

|Ex∗| ≥

|Ex| ≥

![image 173](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile173.png>)

![image 174](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile174.png>)

![image 175](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile175.png>)

![image 176](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile176.png>)

x∈Li,2

contradicting (4). Hence, by (7), we may assume that

1 4|D|. (8)

|Dx| ≥

![image 177](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile177.png>)

x∈Li,1

Recall that φ denotes the default edge-coloring of ∂2(G). Recall also that ∀x,y ∈ Li, x = y, we

have Ax ∩ Ay = ∅ and Cx ∩ Cy = ∅. So V (Γx) ∩ V (Γy) = ∅. Claim 2. Let x,y ∈ Li,1,x = y. Let e ∈ Γx and f ∈ Γy. Then φ(e) ∩ φ(f) = ∅. Proof of Claim 2. By Lemma 5.2, there exists an x,y-path R0 of some even length 2j ≤ 2i in

t≤i Ht that intersects Li only in x and y. Since x,y ∈ Li,1, we have δ(Γx) ≥ p and δ(Γy) ≥ p. Suppose for contradiction that φ(e) ∩ φ(f) = ∅. Let v ∈ φ(e) ∩ φ(f). Since H is linear, we have φ(e) ∩ φ(f) = {v}. Suppose e = ab and f = a′b′, where a ∈ Ax,b ∈ Cx and a′ ∈ Ay,b′ ∈ Cy. Let ℓ = 2m−[2j +2(h−i)+2] = 2m−2−2h+2(i−j). Note that ℓ is even and satisﬁes 2m−2−2h ≤ ℓ ≤ 2m − 4. Since δ(Γy) ≥ p = 2mr > rℓ + 2r, by Lemma 3.4, there exists a path P in Γy of length ℓ starting at b′ that is strongly rainbow under φ and such that ( e′∈P φ(e′)) ∩ (φ(e) ∪ φ(f)) = ∅. Let b′′ denote the other endpoint of P. Since P has an even length, b′′ ∈ Cy. Let P+ denote the set of the edges of E that correspond to the edges of P ∪ {e,f}. Then P+ is linear path of length 2m − 2h + 2(i − j) in G where a is an endpoint at one and b′′ is an endpoint at the other end. Furthermore, V (P+) ∩ V (H) ⊆ Lh. Let R be a monotone path in H from x to a. Then R has length h − i and is internally disjoint from R0 and P+. Since b′′ ∈ Cy, y is a dominator of b′′. By deﬁnition, there exist p internally disjoint y,b′′-paths that intersect each main level of H at most once. In particular these paths have length h − i + 1. Since p = 2mr > |V (P+ ∪ R ∪ R0)|, one of these paths, say R′, is internally disjoint from P+ ∪ R ∪ R0. Now P+ ∪ R ∪ R0 ∪ R′ is a linear cycle of length 2m − 2h + 2(i − j) + h − i + 2j + h − i + 1 = 2m + 1 in G, a contradiction. This proves

- Claim 2.


![image 178](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile178.png>)

Now by Claim 2 and earlier discussion, ∀x,y ∈ Li,1,x = y, we have V (Ex) ∩ V (Ey) = ∅. Let E∗ = {Ex : x ∈ Li,1}, S = {Cx : x ∈ Li,1}, and Γ = {Γx : x ∈ Li,1}. Then |E∗| ≥ 41|D|. By

![image 179](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile179.png>)

(6), we have

r − 1 2r+3m(mpr)m−1|Lh| ≥

1 c|E|.

|E∗| ≥

![image 180](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile180.png>)

![image 181](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile181.png>)

By our discussion, φ is strongly rainbow on Γ and hence E∗ is the r-expansion of Γ. It is easy to check that E∗,S, and Γ satisfy the other requirements of the Lemma.

Subcase 2.3 |Bi′| ≥ B2h+ for some 1 ≤ i ≤ h − 1.

![image 182](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile182.png>)

The arguments are similar in this subcase as in Subcase 2.3, except that the proof of an analogous statement of Claim 2 is more delicate. As in Subcase 2.2, we deﬁne D and Dx analogously with Li being replaced by L′i in the deﬁnitions. Let L′i,1 = {x ∈ L′i,x is heavy and is of type 1}. Let L′i,2 = {x ∈ L′i,x is heavy and is of type 2}. As in Subcase 2.3, we may assume that

1 4|D|. (9)

|Dx| ≥

![image 183](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile183.png>)

x∈L′i,1

Claim 3. Let x,y ∈ L′i,1,x = y. Let e ∈ Γx and f ∈ Γy. Then φ(x) ∩ φ(y) = ∅. Proof of Claim 3. We proceed like in the proof of Claim 2, with adjustments at the end. Since

- x,y are of type 1, we have δ(Γx) ≥ p and δ(Γy) ≥ p. Suppose for contradiction that φ(e) ∩ φ(f) = ∅.


Let v ∈ φ(e) ∩ φ(f). Then φ(e) ∩ φ(f) = {v}. Suppose e = ab and f = a′b′, where a ∈ Ax,b ∈ Cx and a′ ∈ Ay,b′ ∈ Cy. Let ℓ = 2m − 2 − 2h. Since δ(Γy) ≥ p = 2mr > rℓ + 2r, by Lemma 3.4, there exists a path P in Γy of length ℓ starting at b′ that is strongly rainbow under φ and such that ( e′∈P φ(e′))∩(φ(e)∪φ(f)) = ∅. Let b′′ denote the other endpoint of P. Since P has an even length, b′′ ∈ Cy. Let P+ denote the set of the edges of E that correspond to the edges of P ∪ {e,f}. Then P+ is linear path of length 2m − 2h in G where a is an endpoint at one and b′′ is an endpoint at the other end. Furthermore, V (P+) ∩ V (H) ⊆ Lh. Let R be a monotone path in H from x to a.

- Then R has length h − i and is internally disjoint from P+. Since b′′ ∈ Cy, y is a dominator of b′′. By deﬁnition, there exist p internally disjoint y,b′′-paths that intersect each main level of H at most once. In particular these paths have length h − i + 1. Since p = 2mr > |V (P+ ∪ R)|, one of these paths, say R′, is internally disjoint from P+ ∪ R. Now W = P+ ∪ R ∪ R′ is a linear x,y-path of


- length 2m − 2i + 1 in G. Let ex denote the edge of W containing x and ey the edge of W containing


- y. Each of ex,ey intersects Li in exactly one vertex. Suppose ex ∩ Li = {x∗} and ey ∩ Li = {y∗}. Then V (W) ∩ ( ij=0 V (Hj)) = {x∗,y∗}.


By Lemma 5.2 there is an x∗,y∗-path R0 of length 2t ≤ 2i in ij=0 Hj such that V (R0) ∩ Li = {x∗,y∗}. If t = i then W ∪R0 is a linear cycle in G of length 2m+1, a contradiction. So suppose t < i. The idea now is to keep R,R0 and ey and redeﬁne P and R′ to get a linear cycle of length 2m+1. Let ℓ = 2m−2h+2(i−t)−3. Note that ℓ > 0 and is odd. Since δ(Γy) ≥ p = 2mr > rℓ+2r, by Lemma

- 3.4, there exists a path P in Γy of length ℓ starting at a′ that is strongly rainbow under φ and such


that ( e′∈P φ(e′))∩(φ(e)∪φ(f)) = ∅. Let b′′ denote the other endpoint of P. Since ℓ is odd, b′′ ∈ Cy. Let P+ denote the set of the edges of E that correspond to the edges of P ∪{e,f}. Then P+ is linear path of length 2m−2h+2(i−t)−1 in G where a is an endpoint at one and b′′ is an endpoint at the other end. Furthermore, V (P+) ∩ V (H) ⊆ Lh. As before, there are p internally disjoint y,b′′-paths of length h − i + 1 hitting each main level at most once. Since p = 2mr > |V (P+ ∪ R ∪ ey)|, one of these paths, say R′, is internally disjoint from P+ ∪ R ∪ ey. It is also internally disjoint from R0 by the deﬁnition of R0. Now P+ ∪ R ∪ R0 ∪ {ey} ∪ R′ is a linear cycle of length 2m + 1 in G, a contradiction.

![image 184](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile184.png>)

Now by Claim 3 and earlier discussion, ∀x,y ∈ L′i,1,x = y, we have V (Ex) ∩ V (Ey) = ∅. Let E∗ = {Ex : x ∈ L′i,1}, S = {Ax : x ∈ L′i,1}, and Γ = {Γx : x ∈ L′i,1}. Then |E∗| ≥ 41|D|. By

![image 185](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile185.png>)

(6), we have

r − 1 2r+3m(mpr)m−1|E| ≥

1 c|E|.

|E∗| ≥

![image 186](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile186.png>)

![image 187](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile187.png>)

As in Subcase 2.2, it is easy to check that E∗,S, and Γ satisfy the four conditions of the Lemma.

![image 188](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile188.png>)

- Theorem 6.2 Let m,r be positive integers where m ≥ 2 and r ≥ 3. There exist a positive real c′m,r


- and a positive integer n2 such that for all n ≥ n2 we have exL(n,C2rm+1) ≤ c′m,rn1+m1 .


![image 189](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile189.png>)

Proof. We follow the steps in Theorem 4.2, using Lemma 6.1 in place of Lemma 4.1. Let p = 2mr. Let c = 2r+2(mpr)m as in Lemma 6.1. Let c′m,r = 2mr−1cm. Choose n2 such that c′m,rn

- 1 m

![image 190](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile190.png>)

- 2 ≥ n0,


- where n0 is given in Lemma 3.8. Let G be an n-vertex linear r-graph with at least c′m,rn1+m1 edges, where n ≥ n2. Suppose that G does not contain a copy of C2rm+1, we derive a contradiction. By our assumption, G has average degree at least rc′m,rnm1 . By Lemma 3.6, there exists a subgraph G0 of G


![image 191](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile191.png>)

![image 192](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile192.png>)

with δ(G0) ≥ c′m,rnm1 . Let N = n(G0). Then N ≥ c′m,rnm1 ≥ n0 and δ(G′) ≥ c′m,rN m1 . By Lemma 3.8 (with t = m), there exists a partition of V (G′) into S0,... ,Sm−1 such that for each u ∈ V (G′) and i ∈ {0,... ,m − 1}, we have |LG′(u) ∩ G′[Si]| ≥ c

![image 193](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile193.png>)

![image 194](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile194.png>)

![image 195](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile195.png>)

′ m,r

2mr−1N m1 = cmN m1 . Let w be any vertex in S0. Let L0 = {w}. Inside G′, we will construct a leveled linear quasi tree

![image 196](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile196.png>)

![image 197](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile197.png>)

![image 198](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile198.png>)

- H of height m rooted at w with segments H0,... ,Hm−1 and main levels L0,L1,... ,Lm such that ∀i ∈ {0,... ,m − 1} V (Hi) ⊆ Si. (Note that this means ∀i ∈ [m],Li ⊆ Si−1). Furthermore, we will maintain that ∀i ∈ [m], |Li| ≥ N m1 |Li−1|. This will imply that |Lm| ≥ N, which is a contradiction.


![image 199](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile199.png>)

We construct H as follows. Let H0 consist of the edges of G′[S0] containing w. By our assumption, |H0| ≥ cmN m1 ≥ N m1 , by our deﬁnition of c. Let L1 consists of a vertex from e\{w} for each e ∈ H0. We have |L1| = |H0| ≥ N m1 |L0|. In general, suppose 1 ≤ i ≤ m − 1 and suppose we have deﬁned H0,... ,Hi−1 and L0,L1,... ,Li that satisfy the requirements. Let E denote the set of edges in G′ that contain one vertex in Li ⊆ Si−1 and r − 1 vertices in Si. By the deﬁnition of the partition (S0,... ,Sm−1), |E| ≥ cmN m1 |Li| ≥ ci|Li|. Since C2rm+1  ⊆ G′, by Lemma 6.1, there exists a subset

![image 200](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile200.png>)

![image 201](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile201.png>)

![image 202](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile202.png>)

![image 203](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile203.png>)

- E∗ ⊆ E such that (1) |E∗| ≥ c1i|E|, (2) E∗ is the r-expansion of some bipartite 2-graph Γ with one part in Li and the other part outside ij−=01 Hi−1. Now, let Hi be the r-graph formed by E∗ and let Li consist of one vertex from e\V (Γ) for each e ∈ E∗ (note that this implies that |Li| = |E∗|). Now,


![image 204](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile204.png>)

- i
- j=0 Hi is a leveled linear quasi-tree in G′ rooted at w with heigh i and main levels L0,L1,... ,Li.


Furthermore, |Li| = |E∗| ≥ c1i|E| ≥ ccmi N m1 |Li| ≥ N m1 |Li|. We can continue like this to construct H and derive the desired contradiction.

![image 205](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile205.png>)

![image 206](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile206.png>)

![image 207](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile207.png>)

![image 208](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile208.png>)

![image 209](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile209.png>)

## 7 Cycle-complete Ramsey numbers

Given two r-graphs G and H, the Ramsey number R(G,H) is the smallest positive integer n such that in every coloring of the edges of Knr using two colors red and blue there exists either a red copy

- of G or a blue copy of H. As mentioned in the introduction, part of the motivitation behind our study of the linear Tura´n number of linear cycles comes from the study by Kostochka, Mubayi, and Vertrae¨te [28] on the hypergraph Ramsey number of a linear triangle versus a complete graph. Their work is further inspired by the work of graph Ramsey number R(C3,Kt). A celebrated result of Kim


- [27] together with earlier upper bounds by Ajtai, Komlo´s, and Szemere´di [1] shows that


t2 log t

), as t → ∞.

R(C3,Kt) = Θ(

![image 210](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile210.png>)

Kostochka, Mubayi, and Verstrae¨te’s main theorem [28] is

- Theorem 7.1 [28] There exist constants a,br > 0 such that for all t ≥ 3,


at32 (log t)34

![image 211](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile211.png>)

≤ R(C33,Kt3) ≤ b3t23,

![image 212](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile212.png>)

![image 213](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile213.png>)

![image 214](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile214.png>)

and for r ≥ 4,

t32 (log t)34+o(1) ≤ R(C3r,Ktr) ≤ brt32.

![image 215](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile215.png>)

![image 216](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile216.png>)

![image 217](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile217.png>)

![image 218](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile218.png>)

In addition, they showed Theorem 7.2 [28] For ﬁxed r,k ≥ 3,

1

R(Ck,Ktr) = Ω∗(t1+

3k−1), as t → ∞.

![image 219](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile219.png>)

There exists a constant cr > 0 such that

t ln t

R(C5,Ktr) ≥ cr(

![image 220](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile220.png>)

)45, as t → ∞.

![image 221](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile221.png>)

Here the authors use f = O∗(g) to denote that for some constant c > 0,f(t) = O((ln t)cg(t)), and

- f = Ω∗(g) is equivalent to g = O∗(f). The key point of Theorem 7.2 is that the exponent 1+ 3k1−1 of t is bounded away from 1 by a constant independent of r. The authors made the following conjecture.


![image 222](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile222.png>)

Conjecture 7.3 [28] For all ﬁxed r ≥ 3, R(C3,Ktr) = o(t3/2) and R(C5,Ktr) = O(t5/4), as t → ∞. Using our bounds on the linear Tura´n numbers, we can quickly derive nontrivial upper bounds

on R(Cℓr,Ktr) for all r,ℓ ≥ 3. Before getting into that, we give some recount on the cycle-complete Ramsey numbers of graphs. As mentioned above, the behavior of R(C3,Kt) is now quite well understood, particularly with the recent deep works in [6], [16]. For longer cycles, the best known

m+1 m

m

upper bounds are R(C2m,Kt) = O((lntt)

m−1) due to Caro et al [11] and R(C2m+1,Kt) = O( t

![image 223](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile223.png>)

(lnt)1/m), due to Sudakov [38] and Li and Zang [25]. The best known lower bound is R(Cℓ,Kt) = Ω(t

![image 224](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile224.png>)

![image 225](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile225.png>)

![image 226](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile226.png>)

- ℓ−1

![image 227](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile227.png>)

- ℓ−2


lnt ), due to Bohman and Keevash [5].

![image 228](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile228.png>)

We now obtain some upper bounds on R(Cℓr,Ktr) using linear Tura´n numbers and a reduction process via the well-known sunﬂower lemma. A sunﬂower (or ∆-system) F with core C is a collection of distinct sets A1,... ,Ap such that ∀i,j ∈ [p] we have Ai ∩Aj = C. We call the Ai’s members of the sunﬂower. If a sunﬂower has p members and the core has size a, then we call it a (a,p)-sunﬂower. Note that the core is allowed to be empty and hence a matching is considered to be a sunﬂower.

- Lemma 7.4 (Sunﬂower Lemma [14]) If F is a collection of sets of size at most k and |F| ≥ k!(p − 1)k, then F contains a sunﬂower with p members.


Partly following the approach in [28], we consider non-uniform hypergraphs, but will disallow singletons as edges. Recall that a linear cycle of length ℓ is a list of sets A1,... ,Aℓ such that |Ai ∩ Ai+1| = 1 for i = 1,... ,ℓ − 1, |Aℓ ∩ A1| = 1 and Ai ∩ Aj = ∅ for all other pairs i,j, i = j. A set

- S in a hypergraph G is an independent set in G if no edge of G is contained in S. Let α(G) denote the maximum size of an independent set in G. The next lemma is similar to the ones in [28], except that we use the sunﬂower lemma. A hypergraph is simple if no edge contains another.


- Lemma 7.5 Let m,r ≥ 2 be integers. Let G be a hypergraph whose edges have sizes between 2 and r. Suppose G does not contain a linear cycle of length ℓ. Then there exists a simple hypergraph G′ on V (G) whose edges have sizes between 2 and r such that G′ contains no linear cycle of length ℓ,


- G′ contains no (a,rℓ)-sunﬂower for any a ≥ 2, and α(G′) ≤ α(G).


Proof. We iterate the following process. Let F be an (a,rℓ)-sunﬂower in G with core C, where

- |C| = a ≥ 2. Let G1 be obtained from G by replacing some edge e in F with C. If G1 contains a linear cycle L of length ℓ, then L must use C as an edge. Since L contains at most rℓ vertices and C is the core of a sunﬂower F with rℓ members, we can ﬁnd some edge e′ in F such that e′ \ C is disjoint from V (L). Now if we replace C with e′ in L, we obtain a linear cycle of length ℓ in G, a contradiction. So, G1 has no linear cycle of length ℓ. Clearly, any independent set S in G is also an independent set in G1. So α(G1) ≤ α(G). We now replace G with G1 and repeat this process until there is no longer an (a,rℓ)-sunﬂower for some a ≥ 2. The process must end since the total edge-size decreases at each step. Denote the ﬁnal graph by G′. If G′ is not simple then we make it simple by removing edges that contain other edges. This cannot create a linear cycle of length ℓ, or a new sunﬂower, or increase the independence number. Then G′ satisﬁes the claim.


![image 229](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile229.png>)

A hypergraph G is (2,q)-linear if no pair of vertices is contained in q or more edges of G.

- Lemma 7.6 Let a,p,r ≥ 2 be integers. Let G be a simple hypergraph whose edges have sizes between 2 and r and contains no (a,p)-sunﬂower for any a ≥ 2. Then G is (2,q)-linear, where q = r!(p−1)r.

Proof. Otherwise some pair {a,b} is contained in a set H of least q edges of G. Let H′ = {e\{a,b} : e ∈ H}. Since H ⊆ G is simple |H′| = |H| ≥ q = r!(p − 1)r. By Lemma 7.4, H′ contains a sunﬂower F with p members. Now, adding {a,b} to each member of F yields an (a,p)-sunﬂower in G, where a ≥ 2, contradicting our assumption about G.

![image 230](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile230.png>)

- Lemma 7.7 Let r ≥ 2,q ≥ 1 be integers. Let G be a hypergraph whose edges have sizes between 2 and r. Suppose G is (2,q)-linear. Then G contains a linear subgraph G′ with |G′| ≥ qr22|G|.

![image 231](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile231.png>)

Proof. By our assumption, each edge e of G shares a pair of vertices with at most 2 r (q − 1) other edges. Let H be a graph whose vertices are the edges of G such that two vertices u,v are adjacent

in H if the corresponding edges in G share a pair of vertices. Then ∆(H) < 2 r q − 1. Hence H contains an independent set S of size at least ∆(|VH(H)+1)| ≥ 2|Vqr(H2 )|. Let G′ be the subgraph of G whose edges correspond to S. Then G′ is a linear subgraph of G with |G′| ≥ qr22|G|.

![image 232](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile232.png>)

![image 233](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile233.png>)

![image 234](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile234.png>)

![image 235](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile235.png>)

- Lemma 7.8 Let H be a linear hypergraph whose edges have sizes between 2 and r. Suppose H does not contain a linear cycle of length ℓ. Let D = ∂2(H). Let v be any vertex in V (D) = V (H). Then |D[NH(v)]| ≤ rr+4ℓ|NH(v)|.


Proof. Since H is linear, the link graph LH(x) consists of disjoint edges each of size at most r − 1. Let U = V (LH(v)) = NH(v). The edges of LH(x) form a partition of U into parts of size at most r−1 (with each part being an edge of LH(x)). Also since H is linear no edge of H[U] contains more than one vertex from any of those parts. Let us randomly and independently pick one vertex from each part, and call the resulting set S. For each edge in H[U] the probability of it being in H[S] is at least (r−11)r. So there is a choice of S for which H[S] ≥ (r−11)r |H[U]|. If H[S] has average degree at least r2ℓ, then it contains a subgraph H′ with minium degree at least rℓ and since H′ is linear, one can easily ﬁnd a linear path P of length ℓ−2 say with endpoint a and b. Let ea be the edge of H that contains {x,a} and eb the edge of H that contains {x,b}. Then ea ∩ S = {a},eb ∩ S = {b}. In particular,

![image 236](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile236.png>)

![image 237](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile237.png>)

we see that P ∪ {ea,eb} is a linear cycle of length ℓ, a contradiction. So H[S] has average degree less than r2ℓ. So, |H[U]| ≤ (r − 1)r|H[S]| < rr r22ℓ|S| < rr+2ℓ|U|. So |D[U]| ≤ r2 |H[U]| < rr+4ℓ|U|.

![image 238](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile238.png>)

![image 239](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile239.png>)

We need the following lemma due to Alon [2]. The version stated below is implicit in the proof of Proposition 2.1 in [2]. Alternatively, one could also apply [3]. Logarithms below are in base 2.

- Lemma 7.9 [2] Let G be an n-vertex graph with maximum degree at most d ≥ 1, in which for any vertex v, G[N(v)] contains an independent set of size at least |Np(v)|. Then α(G) ≥ 160dnlog(logpd+1).


![image 240](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile240.png>)

![image 241](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile241.png>)

Theorem 7.10 Let m,r be integers where m ≥ 2 and r ≥ 3. There exists a constant am,r, depending on m and r such that R(C2rm,Ktr) ≤ am,r(lntt)

m

m−1.

![image 242](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile242.png>)

![image 243](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile243.png>)

Proof. The deﬁnition of am,r depends on various constants we deﬁned earlier and will be implit in our proof. Let n ≥ am,r(lntt)

m

m−1. By choosing am,r to be large enough, we may assume that n ≥ n1,

![image 244](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile244.png>)

![image 245](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile245.png>)

- where n1 is given in Theorem 4.2. It suﬃces to show that if G is an n-vertex r-graph that does not contain C2rm then G contains an independent set of size at least t. Let such G be given. By Lemma


- 7.5, there exists a simple hypergraph G′ with V (G′) = V (G) such that α(G′) ≤ α(G), G′ contains no linear cycle of length 2m, and that G′ contains no (a,2mr)-sunﬂower for any a ≥ 2. By Lemma
- 7.6, G′ is (2,q)-linear, where q = r!(2mr − 1)r. By Lemma 7.7, G′ contains a linear subgraph with |G′′| ≥ c1|G′|, where c1 is a positive constant depending on m and r. Clearly, G′′ contains no linear cycle of length 2m. Applying the O(n1+m1 ) bound [7] on ex(n,C2m) and Theorem 4.2, by considering edges of various sizes, we have |G′′| ≤ c2n1+m1 , for some constants c2, depending on m and r. Hence |G′| ≤ c3n1+m1 for some constant c3, depending on m and r. So G′ has average degree at most rc3nm1 . Clearly, at most n/2 vertices in G′ can have degree at least 2rc3nm1 . Let H be the subgraph of G′


![image 246](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile246.png>)

![image 247](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile247.png>)

![image 248](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile248.png>)

![image 249](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile249.png>)

![image 250](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile250.png>)

induced by vertices of degree at most 2rc3nm1 . Then |V (H)| ≥ n2 and ∆(H) ≤ 2rc3nm1 .

![image 251](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile251.png>)

![image 252](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile252.png>)

![image 253](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile253.png>)

Let D = ∂2(H). Then ∆(D) ≤ 2r2c3nm1 . Note that for each vertex v we have ND(v) = NH(v), which we will denote by N(v). Since H does not contain a linear cycle of length 2m, by Lemma 7.8, for each vertex v in V (H) = V (D), we have |D[N(v)]| ≤ 2mrr+4|N(v)|. So D[N(v)] has average degree at most 4mrr+4. By Caro and Wei [10, 41], D[N(v)] contains an independent set of size at least 4mr|Nr(+4v)|+1. By Lemma 7.9, with d = 2r2c3nm1 , α(D) ≥ c5|V (D)|lnn

![image 254](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile254.png>)

≥ c25nmm−1 ln n, for some positive constant c5, depending on m and r. Since n ≥ am,r(lntt)

![image 255](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile255.png>)

![image 256](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile256.png>)

![image 257](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile257.png>)

![image 258](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile258.png>)

![image 259](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile259.png>)

nm1

![image 260](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile260.png>)

m

m−1, by choosing am,r to be large enough, we can ensure α(D) ≥ t. Certainly any indepdent set in D is also an independent set in G′. Hence α(G′) ≥ t and α(G) ≥ α(G′) = t.

![image 261](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile261.png>)

![image 262](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile262.png>)

![image 263](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile263.png>)

For odd cycle-complete Ramsey numbers, we need some more deﬁnitions and a lemma. Let H be a hyergraph whose vertices are ordered by a total order π. Let P be a linear path of length ℓ, that is, P consists of a list of edges e1,... ,eℓ such that |ei ∩ ei+1| = 1 for each i ∈ [ℓ − 1] and ei ∩ ej = ∅ whenever |i − j| > 1. For each i ∈ [ℓ − 1], let ei ∩ ei+1 = {xi}. We say that P is an increasing linear path under π if for all v ∈ e1 \ {x1},π(v) < π(x1), ∀v ∈ eℓ \ xℓ−1,π(xℓ−1) < π(v), and for each

- i = 2,... ,ℓ − 1 and v ∈ ei \ {xi−1,xi}, we have π(xi−1) < π(v) < π(xi). If P is an increasing linear path and v is the largest vertex on P under π, then we say that P ends at v.


- Lemma 7.11 Let H be a hypergraph and π a total order on V (H). If H does not contain an increasing linear path of length ℓ, then V (H) can be partitioned into ℓ independent sets.


Proof. For each i = 0,... ℓ − 1, let Si denote the set of vertices v such that the longest increasing linear path in H that ends at v has length i. Then S0,... ,Sℓ−1 partition V (H). Suppose for some

- i ∈ {0,... ,ℓ − 1}, Si contains an edge e. Let v and v′ be the vertices in e that are smallest and largest under π, respectively. By deﬁnition, H contains an increasing linear path P of length i that ends at v. Now P ∪ e is an increasing path of length i + 1 that ends at v′, contradicting v′ ∈ Si. Hence for each i, Si contains no edge of H and hence is an independent set in H.


![image 264](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile264.png>)

The following lemma is a variant of Theorem 1 in [13]. The proof is similar.

- Lemma 7.12 Let H be a hypergraph whose edges have sizes between 2 and r. Suppose H does not contain a linear cycle of length 2m + 1. Let H∗ be the subgraph of H consisting of all the edges of size 2 in H. Let v ∈ V (G). For each i, let Si be the set of vertices in H∗ that are at distance i from v. Then for each i ≤ m, H[Si] contains an independent set of size at least 2m|S−i|1.


![image 265](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile265.png>)

Proof. Grow a breadth-ﬁrst search tree T in H∗ from v. So the levels of T are precisely the distance classes from v in H∗. For each i ≥ 1, deﬁne a linear order πi of Si as follows. Let π1 be an arbitrary linear order on S1. For each i ≥ 2, let πi be a linear order on Si obtained by listing the children of the ﬁrst vertex in πi−1, followed by the children of the second vertex in πi−1, and etc. For each 1 ≤ i ≤ m, we claim that H[Si] contains no increasing linear path of length 2m−1. Otherwise, ﬁx an i for which H[Si] contains an increasing linear path P of length 2m−1 with edges e1,e2,... ,e2m−1 in order. Let x1 be the least vertex in e1 under πi. Let x2m be the largest vertex in e2m−1 under πi. For each k ∈ {2,... ,2m − 1}, let ek−1 ∩ ek = {xk}. Then x1 < x2 < ... < x2m in πi. Let w be a closest common anchester of x1,... ,x2m in T. Suppose w ∈ Sj, where j < i. Let k be the smallest positive integer such that xk and xk+1 are under diﬀerent children of w. Such k exists by our choice of w. By our ordering on each level, the anchesters of x1,... ,xk in Sj precede anchesters of xk+1,... ,x2m in Sj under πj. Hence for any a ∈ [k],b ∈ [2m] \ [k], the unique xa,xb-path Qa,b in T must pass through w and has length 2(i − j). Based on the value of k, we can ﬁnd a ∈ [k],b ∈ [2m] \ [k] such that b − a = 2m + 1 − 2(i − j). Now Qa,b ∪ {ea,ea+1,··· ,eb−1,eb} is a linear cycle of length 2m + 1 in H, a contradiction. Hence H[Si] contains no increasing linear path of length 2m − 1. By Lemma 7.11, H[Si] contains an independent set of size at least 2m|S−i|1.

![image 266](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile266.png>)

![image 267](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile267.png>)

Theorem 7.13 Let m,r be positive integers where m ≥ 2,r ≥ 3. There exists a positive constant bm,r, depending on r and m, such that R(C2rm+1,Ktr) ≤ bm,rt

m

m−1.

![image 268](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile268.png>)

Proof. Our choice of bm,r will depend on other constants deﬁned earlier and will be implicit in the proof. Let n ≥ bm,rt

m

m−1. By choosing bm,r to be large enough, we may assume that n ≥ n2, where n2 is speciﬁed in Theorem 6.2. Let G be any n-vertex r-graph on n vertices not containing a copy of C2rm+1. We show that G contains an independent set of size at least t.

![image 269](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile269.png>)

By Lemma 7.5, there exists a simple hypergraph G′ on V (G) whose edges have sizes between 2 and r such that α(G′) ≤ α(G), G′ contains no linear cycle of length 2m +1, and that G′ contains no (a,(2m+1)r)-sunﬂower for any a ≥ 2. By Lemma 7.6, G′ is (2,q)-linear where q = r![(2m+1)r−1]r. For each j = 3,... ,r, let Gj denote the subgraph of G′ consisting of edges of size j. Let G′′ = rj=3 Gj. Then G′′ is (2,q)-linear. By Lemma 7.7, G′′ contains a linear subgraph G∗ with |G∗| ≥ qr22|G′′|. By Theorem 6.2, |G∗| ≤ c′1n1+m1 for some positive constant c′1 depending on m and r. Hence

![image 270](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile270.png>)

![image 271](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile271.png>)

|G′′| ≤ c′2n1+m1 for some positive constant c′2 depending on m and r. The number of vertices of G′′ of degree at least 2rc′2nm1 is at most n/2. Let U be the set of vertices of degree at most 2rc′2nm1 in G′′. Then |U| ≥ n2. Let H = G′[U]. Let H∗ be the subgraph of H consisting of edges of size 2. Let H′ be subgraph of H consisting of edges of size 3 or more. By our deﬁnition of H, ∆(H′) ≤ 2rc′2nm1 . We obtain a large independent set W in H as follows. Initially set W = ∅. Let v be any vertex in H and for each i ≥ 0 let Si denote the set of vertices at distance i from v in H∗. Let 0 ≤ k ≤ m − 1 be the smallest integer such that |S|Si+1|

![image 272](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile272.png>)

![image 273](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile273.png>)

![image 274](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile274.png>)

![image 275](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile275.png>)

![image 276](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile276.png>)

i| ≤ nm1 . Such k exists since otherwise we would have |Sm| > n, a contradiction. Since H contains no linear cycle of length 2m + 1, by Lemma 7.12, H[Sk] contains an independent set S′ of size at least 2|mS−k|1. Let S = Sk−1 ∪ Sk ∪ Sk+1 (or S = S0 ∪ S1, if k = 0). Then the neighbors in H∗ of vertices in S′ lie in S. By our choice of k, | S| < (nm1 + 2)|Sk| < (2m − 1)(nm1 + 2)|S′| < 3mnm1 |S′|. Let Z be a set of vertices in H obtained by picking a vertex in e \ S, if exists, for each edge e in H′ that contains a vertex in S′. Since ∆(H′) ≤ 2rc′2nm1 , we have |Z| ≤ 8rc′2nm1 |S′|. By our discussion above, | S ∪ Z| ≤ c′3nm1 |S′| for some positive constant c′3 depending on m and r. We add S′ to U and delete S ∪ Z from H and iterate the process until we run out of vertices. By design, the ﬁnal W is an independent set in H that has size at least n/2

![image 277](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile277.png>)

![image 278](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile278.png>)

![image 279](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile279.png>)

![image 280](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile280.png>)

![image 281](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile281.png>)

![image 282](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile282.png>)

![image 283](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile283.png>)

![image 284](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile284.png>)

![image 285](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile285.png>)

m−1 m

m

≥ n

![image 286](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile286.png>)

2c′3 . Since n ≥ bm,rt

m−1, by choosing bm,r to be large enough, we can ensure α(H) ≥ t. Since H = G′[U], we have α(G) ≥ α(G′) ≥ t.

![image 287](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile287.png>)

![image 288](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile288.png>)

![image 289](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile289.png>)

c′3nm1

![image 290](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile290.png>)

![image 291](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile291.png>)

## 8 Concluding Remarks

Our main objective in this paper is to establish an O(n1+⌊2ℓ⌋) bound on exL(n,Cℓr). We chose constants cr,ℓ and c′r,ℓ in Theorem 4.2 and Theorem 6.2. larger than necessary in order to simplify our presentation. It is possible that like in the graph case one could ﬁnd a constant cr, depending on r, such that exL(n,C2rm) ≤ crmn1+m1 . It will be interesting to see whether that indeed is the case.

![image 292](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile292.png>)

![image 293](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile293.png>)

The study of exL(n,C23m) has a natural connection to the so-called rainbow Tura´n number ex∗(n,C2m) of a cycle of length 2m, which denotes the maximum number of edges in an n-vertex graph that admits a proper edge-coloring that contains no cycle of length 2m all of whose edges have diﬀerent colors. The main conjecture from [26] is that ex∗(n,C2m) = O(n1+m1 ), which remains open except for C4 and C6. See Das, Lee, and Sudakov [12] for some recent progress on the problem. Interestingly, there it is not too hard to obtain an Ω(n1+m1 ) lower bound on ex∗(n,C2m) through an explicit construction using Bk∗-sets. Here, the diﬃculty in ﬁnding a good lower bound on exL(n,Cℓr) for r ≥ 3 is similar to that for ex(n,Cℓ) for even cycles Cℓ. Verstrae¨te [40] observed that by taking a random subgraph of a Steiner triple system one can show that ex(n,Cℓ3) ≥ Ω(n1+

![image 294](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile294.png>)

![image 295](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile295.png>)

1

ℓ−1). Similarly, by taking a random subgraph H of a linear n-vertex r-graph G with (1 − o(1))

![image 296](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile296.png>)

(n2) (r2)

edges (such G exists by the well-known packing result of Ro¨dl [34]) and the usual deletion argument, one can show that Proposition 8.1 For all integers r,ℓ ≥ 3, ∃ a constant c′′r,ℓ > 0 such that exL(n,Cℓr) > c′′r,ℓn1+

![image 297](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile297.png>)

1

ℓ−1. Using generalized Sidon sets such as the ones considered in [36] and [31], it is conceivable that

![image 298](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile298.png>)

one can obtain a similar (or better) constructive lower bound on exL(n,Cℓ3) (and maybe also for all r ≥ 3.) This is an area worth some exploration.

Our Ramsey bounds on R(Cℓr,Ktr) are similar to those for graphs. However, as speculated in

ℓ

- [28], for r ≥ 3 perhaps R(Cℓr,Ktr) = Θ∗(t


ℓ−1) holds, where O∗ and Ω∗ are deﬁned in Section 7. It will

![image 299](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile299.png>)

be interesting to further sharpen our bounds on R(Cℓr,Ktr). By anaylzing the proof of Theorem 6.2, together with Lemma 7.8 and Lemma 7.9, one might be able to improve our bound on R(C2rm+1,Ktr) by a factor of (ln t)c. On the other hand, perhaps a more substantial improvement is possible.

As in [28], let RL(Cℓr,Ktr) denote the smallest n such that every linear r-graph not containg Cℓr has an independent set of size t. Using our linear Tua´n bounds and the usual random sampling arugment, one readily obtains RL(Cℓr,Ktr) = O(t

ℓ

ℓ−1).

![image 300](<2014-colliercartaino-linear-turan-numbers-r-uniform_images/imageFile300.png>)

## 9 Acknowledgment

The authors would like to thank Kostochka, Mubayi, and Verstrae¨te for informative communications and Verstrae¨te for fruitful and stimulating discussions.

## References

- [1] M. Ajtai, J. Koml´os, E. Szemer´edi: A note on Ramsey numbers, J. Combin. Th. Ser. A 29 (1980), 354-360.
- [2] N. Alon, Independence numbers of locally sparse graphs and a Ramsey type problem, Random Structures and Algorithms 9 (1996), 271-278.
- [3] N. Alon, M. Krivelevich, B. Sudakov, Coloring graphs with sparse neighborhoods, J. Combin. Th. Ser. B 77 (1999), 73-82.
- [4] F. Behrend: On sets of integers which contain no three elements in arithmetic progression, Proc. Nat. Acad. Sci. 32 (1946), 331-332.
- [5] T. Bohman, P. Keevash: The early evolution of the H-free process, Invent. Math 181 (2010), 291-336.
- [6] T. Bohman, P. Keevash: Dyanamic concentration of the triangle-free process, arXiv:1302.5963.
- [7] J.A. Bondy, M. Simonovits: Cycles of even length in graphs, J. Combin. Th. Ser. B 16 (1974), 97-105.
- [8] W.G. Brown, P. Erdo˝s, V. So´s: On the existence of triangulated spheres in 3-graphs and related problems, Periodica Mathematica Hungaria 3 (1973), 221-228.
- [9] B. Bukh, Z. Jiang: A bound on the number of edges in graphs without an even cycle, arXiv:1403.1601v1.
- [10] Y. Caro: New results on the independence number, Technical Report, Tel Aviv University, 1979.
- [11] Y. Caro, Y. Li, C. Rousseau, Y. Zhang: Asymptotic bounds for some bipartite graph: complete graph Ramsey numbers, Discrete Math. 220 (2000), 51-56.
- [12] S. Das, C. Lee, B. Sudakov: Rainbow Tur´an problem for even cycles, European J. Combinatorics 34

(2013), 905-915

- [13] P. Erdo˝s, R. Faudree, C. Rousseau, R. Schelp: On cycle-complete graph Ramsey numbers, J. Graph Theory 2 (1978), 53-64.
- [14] P. Erdo˝s, R. Rado: Intersection theorems for systems of sets, J. London Math Soc., Second Series 35


(1) (1960), 85-90.

- [15] R. Faudree, M. Simonovits: On a class of degenerate extremal graph problems, Combinatorica 3 (1983), 83-93.
- [16] G. Fiz Pontiveros, S. Griﬃths, R. Morris: The triangle-free process and R(3,k), arXiv:1302.6279.
- [17] Z. F¨uredi: On the number of edges of quadrilateral-free graphs, J. Combin. Th. Ser. B 68 (1996), 1-6.
- [18] Z. F¨uredi, A. Naor, J. Verstra¨ete: On the Tur´an number for the hexagon, Adv. Math. 203 (2006), 476-496.
- [19] Z. F¨uredi, T. Jiang, R. Seiver: Exact Solution of the hypergraph Tur´an problem for k-uniform linear paths, Combinatorica, to appear.
- [20] Z. F¨uredi, T. Jiang: Hypergraph Tur´an numbers of linear cycles, J. Combin. Th. Ser. A 123 (2014), 252-270.
- [21] Z. F¨uredi, M. Simonovits: The history of degenerate (bipartite) extremal graph problems, arXiv:1306.5167.
- [22] E. Gy˝ori, N. Lemons: 3-uniform hypergraphs avoiding a given odd cycle, Combinatorica 32 (2012), 187-203.
- [23] E. Gy˝ori, N. Lemons: Hypergraphs with no cycle of a given length, Combin. Probab. Comput. 21 (2012), 193-201.
- [24] T. Jiang, R. Seiver: Tur´an numbers of subdivided graphs, SIAM J. Discrete Math. 26 (2012), 1238-1255.
- [25] Y. Li, W. Zang: The independence number of graphs with forbidden cycle and Ramsey numbers, J. Combin. Optimization 7 (2003), 353-359.
- [26] P. Keevash, D. Mubayi, B. Sudakov, J. Verstra¨ete: Rainbow Tur´an problems, Combin. Probab. Comput. 16 (2006), 109-126.
- [27] J. Kim: The Ramsey number R(3,t) has order of magnitude t2/ logt, Random Structure and Algorithms 7 (1995), 173-207.
- [28] A. Kostochka, D. Mubayi, J. Verstra¨ete: Hypergraph Ramsey numbers: triangles versus cliques, J. Combin. Th. Ser. A, 120 (2013), 1491-1507.
- [29] A. Kostochka, D. Mubayi, J. Verstra¨ete: personal communications.
- [30] Kostochka, Mubayi, and Verstra¨ete: Tur´an Problems and Shadows I: Paths and Cycles, submitted (arXiv:1308.4120v1).
- [31] F. Lazebnik, J. Verstra¨ete: On hypergraphs of girth 5, Electronic J. Combinatorics 10 (2003), #R25.
- [32] M. Molloy, B. Reed: Graph colouring and the probabilistic method, Algorithms and Combinatorics, 23. Springer-Verlag, Berlin, 2002.
- [33] O. Pikhurko: A note on the Tur´an function of even cycles, Proc. American Math. Soc. 140 (2012), 3687-3992.
- [34] V. Ro¨dl: On a packing and covering problem, Euro. J. Combin. 6 (1985), 69-78.
- [35] K.F. Roth: On a problem of Heilbronn, J. London Math. Soc. 26 (1951), 198-204.
- [36] I. Ruzsa: Solving a linear equation in a set of integers. I. Acta Arithmetica 65 (1993), #3, 259-282.


- [37] I. Ruzsa, E. Szemer´edi: Triple systems with no six points carrying three triangles, in Combinatorics, Keszthely, 1976, Colloq. Math. Soc. J. Bolyai 18, Vol II, 939-945.
- [38] B. Sudakov: A note on odd cycle-complete graph Ramsey numbers, Electronic. J. Combinatorics 9

(2002), #N1.

- [39] J. Verstra¨ete: On arithmetic progressions of cycle lengths in graphs, Combin. Probab. Comput. 9 (2000), 369-373.
- [40] J. Verstra¨ete: personal communications.
- [41] V. K. Wei, A lower bound on the stability number of a simple graph, Technical Memorandum, TM 81-11217-9, Bell Laboratories, 1981.


