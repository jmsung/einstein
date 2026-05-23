![image 1](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile1.png>)

![image 2](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile2.png>)

![image 3](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile3.png>)

Noname manuscript No.

(will be inserted by the editor)

![image 4](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile4.png>)

![image 5](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile5.png>)

An Erdo˝s–Gallai-type theorem for keyrings

Alexander Sidorenko

arXiv:1705.10254v3[math.CO]19Apr2018

July 31, 2018

Abstract A keyring is a graph obtained by appending r ≥ 1 leaves to one of the vertices of a cycle. We prove that for every r ≤ (k − 1)/2, any graph with average degree more than k − 1 contains a keyring with r leaves and at least k edges.

Keywords Erdo˝s–Gallai theorem, Erdo˝s–S´os conjecture Mathematics Subject Classiﬁcation (2010) 05C35, 05C05

- 1 Introduction


The graphs considered in this paper are simple and undirected. The sets of vertices and edges of a graph G are denoted by V (G) and E(G), respectively. Their sizes are v(G) = |V (G)| and e(G) = |E(G)|. For u ∈ V (G), we denote by NG(u) the set of vertices adjacent to u in G, and dG(u) = |NG(u)| is the degree of u. For a subset of vertices X ⊂ V (G), the number of edges of G with at least one end in X is denoted by dG(X).

Let Dk be the class of all graphs whose average degree is strictly more than k − 1. In other words, G ∈ Dk if 2e(G) > (k − 1)v(G). Erdo˝s and Gallai proved the following two statements.

- Theorem 1.1 (Theorem 2.6 [5]) Any graph G ∈ Dk contains a path of k edges.
- Theorem 1.2 (Theorem 2.7 [5]) Any graph G ∈ Dk contains a cycle with at least k edges.


In fact, the statement of Theorem 2.7 in [5] is even stronger: an n-vertex graph without cycles of length k (or more) has at most (n−1)(k−1)/2 edges, and less than that if n − 1 is not a multiple of k − 2. Faudree and Schelp [8] and independently Kopylov [10] determined (for every n and k) the largest number of edges in an n-vertex graph without a k-edge path. They also described the extremal graphs.

![image 6](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile6.png>)

A. Sidorenko ORCID: 0000-0002-1755-4013 16 Sunrise Drive, Armonk, NY 10504, USA E-mail: sidorenko.ny@gmail.com

Kopylov [10] did the same for 2-connected graphs without cycles of length k and more.

Together, Theorem 1.1 and a simple observation that every graph G ∈ Dk contains a star with k edges, led to the following conjecture formulated by Erdo˝s and S´s (see [4]).

Erd˝os–So´s Conjecture. Any graph G ∈ Dk contains every tree with k edges.

Let Tk be the class of k-edge trees T such that every G ∈ Dk contains T as a subgraph. The Erdo˝s–S´os conjecture states that all k-edge trees belong to Tk. Ajtai, Koml´s, Simonovits, and Szemer´edi [1,2,3] proved that there exists k0 such that the conjecture holds for all k > k0. Still, the general case has not been solved, and only partial results have been obtained.

A spider S(k1, k2, . . . , kr) is a tree obtained from r disjoint paths of lengths k1, k2, . . . , kr by combining their starting vertices into one. The combined vertex has degree r and is called the center. Obviously, S(k1, k2) is just a path of length

- k1 + k2. Wo´zniak [14] proved that S(k1, k2, . . . , kr) ∈ Tk if k1, k2, . . . , kr ≤ 2. Fan and Sun [6] proved that S(k1, k2, . . . , kr) ∈ Tk when r = 3 or k1, k2, . . . , kr ≤ 4. Very recently, Fan, Hong and Liu [7] proved that all spiders belong to Tk. McLennan [11] proved that T ∈ Tk when T is a tree of diameter 4.


It was mentioned in Section 3 of [12] that Perles proved the Erdo˝s–S´os conjecture for caterpillars (those are trees which do not contain S(2,2,2) as a subgraph). The proof was published in [9] only recently.

A vertex which is adjacent to a leaf is called a preleaf. It was proved in [13] that if a tree T has a preleaf which is adjacent to at least (k − 1)/2 leaves then T ∈ Tk. We will prove in Section 2 a stronger statement:

- Theorem 1.3 If a tree T with k edges has p preleaves and one of them is adjacent to at least (k − p − 1)/2 leaves then T ∈ Tk.

Trees and cycles are not the only subgraphs whose existence can be deduced from the graph’s average degree. As a referee of this paper pointed out, it was Tura´n who formulated the very problems for which the Erdo˝s–Gallai theorems provide the answers. He asked the maximal number of edges in an n-vertex graph which does not contain a lasso, that is a cycle and a path having one common vertex. Fan and Sun [6] solved the lasso problem (but did not formulate their result explicitly) within the proof of their Theorem 3.1. In this paper, we consider a similar forbidden pattern. A keyring Cr(l) is a (l+r)-edge graph obtained from a cycle of length l by appending r leaves to one of its vertices. This vertex has degree r + 2 and is called the center of the keyring. In Section 3, we prove an analog of Theorem 1.2 for keyrings:

- Theorem 1.4 For any positive integer r ≤ (k − 1)/2, every graph G ∈ Dk contains a keyring with r leaves and at least k edges.


A graph is called k-minimal if it belongs to Dk but none of its proper subgraphs belongs to Dk. Obviously, any graph from Dk contains a k-minimal subgraph. Thus, in proofs of Theorems 1.4, 1.3 and similar statements, instead of considering all

graphs G ∈ Dk, it is suﬃcient to consider only those which are k-minimal. The main help comes from the simple observation:

Remark 1.5 If a graph G is k-minimal then for any subset of vertices X ⊂ V (G) the number of edges of G with at least one end in X is strictly more than k−21|X|.

![image 9](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile9.png>)

- 2 Proof of Theorem 1.3


Let m(T) denote the largest number of leaves connected to a single preleaf in T, L(T) denote the set of leaves of T, and P(T) denote the set of preleaves. In this proof, we will keep k ﬁxed and use induction in m(T). The basis of induction is the case m(T) = k. In this case, T is a star and belongs to Tk. Now we are going to prove the inductive step. Suppose that m(T) = m < k and the statement of the theorem holds for all trees T′ where m(T′) > m. (We will make use of the assumption m ≥ (k − p − 1)/2 later.)

Consider a k-minimal graph G. We need to show that G contains T as a subgraph. Let u be a preleaf of T with m leaves. Let v be another preleaf of T (since m < k, T is not a star and has at least two preleaves). Now we disconnect in T one of the leaves attached to v and reconnect it to u instead. The resulting tree T′ has k edges and m(T′) = m + 1. Since |P(T′)| ≥ |P(T)| − 1, we have m(T′) = m + 1 ≥ (k − |P(T′)| − 1)/2, and by the induction hypothesis, G must contain a copy of T′. We are going to transform this copy of T′ into a copy of T by changing the assignment of leaves to the preleaves. From now on, we will assume that V (T′) is a subset of V (G), and E(T′) is a subset of E(G). We deﬁne three nonoverlapping sets of vertices: A = P(T′)∪{v}, B = L(T′) \ {v}, C = V (G) \ V (T′). Notice that v in T′ might remain a preleaf or become a leaf or neither. In any case, we want to ensure that v belongs to A and not to B. Thus, |A| = |P(T)| = p, |B| = |L(T)|. Consider a bipartite directed graph F whose vertex set is A ∪ B ∪ C with directed edges of two types:

- 1. (a,b) where a ∈ A, b ∈ (B ∪ C) and {a, b} ∈ E(G); and
- 2. (b,a) where a ∈ A, b ∈ B, a and b are adjacent in T′ (which means that leaf a is connected to preleaf b).


If there exists a path in F from v either to u or to C, we will be able to ﬁnd a copy of T in G. Indeed, let (a0, b0, a1, b1, . . . , aq, bq) be a simple path where a0 = v, bq ∈ C, {ai, bi} ∈ E(G) (i = 0,1, . . . , q), and bi ∈ B, ai+1 ∈ A are adjacent in T′ (i = 0,1, . . . , q − 1). Then we can add to T′ vertex bq as well as edges {ai, bi} for i = 0,1, . . . , q, remove edges {ai+1, bi} for i = 0,1, . . . , q − 1 and remove one of the leaves connected to u. The resulting subgraph of G is a copy of T.

Similarly, let (a0, b0, a1, b1, . . . , aq) be a simple path where a0 = v, aq = u, {ai, bi} ∈ E(G) (i = 0,1,. . . , q − 1), and bi ∈ B, ai+1 ∈ A are adjacent in T′ (i = 0,1, . . . , q − 1). Then we can add to T′ edges {ai, bi} for i = 0,1, . . . , q − 1 and remove edges {ai+1, bi} for i = 0,1,. . . , q−1. The resulting subgraph of G is a copy of T.

Finally, consider the case when C ∪ {u} is unreachable from v in F. We split A into two subsets: X consists of the vertices that are reachable from v in F, and Y consists of the rest. Obviously, v ∈ X and u ∈ Y . Let Z be the set of m + 1 leaves that are attached to u. There are no edges in G between X and C ∪ Y ∪ Z. Since |X|+|Y | = p and |Z| = m+1 ≥ (k−p+1)/2, then for any w ∈ X we can estimate:

|NG(w)\X| ≤ |V (T′)| − (|X| + |Y | + |Z|) ≤ (k + 1) − p +

k − p + 1 2

![image 10](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile10.png>)

=

k − p + 1 2

.

![image 11](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile11.png>)

Using |X| ≤ p − 1, we get

dG(X) ≤

≤

|X|(|X| − 1) 2

k − p + 1 2

+ |X|

![image 13](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile13.png>)

![image 14](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile14.png>)

(p − 1) + k − p 2

k − 1 2

|X| =

|X|

![image 15](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile15.png>)

![image 16](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile16.png>)

|X| + k − p 2

= |X|

![image 17](<2017-sidorenko-erd-gallai-type-theorem-keyrings_images/imageFile17.png>)

which, according to Remark 1.5, contradicts the k-minimality of G. ⊔⊓

- 3 Proof of Theorem 1.4


Lemma 3.1 Fix integers λ ≥ 2 and t ≥ 1. Let H be a Hamiltonian graph with m ≥ λ vertices, and u0 be one of them. If dH(u0) ≥ 2t − 1 + max{2λ − m − 1,2} then there exists l ≥ λ such that H contains a copy of Ct(l) with the center at u0.

Proof Let (u0, u1, . . . , um−1, um = u0) be a Hamiltonian cycle in H. Suppose ﬁrst that m = λ. Since m ≥ 3, we get 2λ−m−1 = m−1 ≥ 2 and dH(u0) ≥ 2t+m−2 ≥ m = v(H) which is impossible. Therefore, we may assume m ≥ λ + 1. Denote

X1 = {u2, u3, . . . , um−λ+1}, X2 = {uλ−1, uλ, . . . , um−2}, X3 = {u1, u2, . . . , um−1} \ (X1 ∪ X2).

Clearly, |X1∪X2| = |X1|+|X2| = 2(m−λ) when m−λ+1 < λ−1, and |X1∪X2| = m − 3 when m − λ + 1 ≥ λ − 1. Thus, |X1 ∪ X2| = min{2m − 2λ,m − 3} and |X3| = (m − 1) − |X1 ∪ X2| = max{2λ − m − 1,2}. Note that

|NH(u0) ∩ (X1 ∪ X2)| ≥ dH(u0) − |X3| ≥ (2t − 1) + max{2λ − m − 1,2} − |X3| = 2t − 1.

Thus, there exist ui1, ui2, . . . , ui2t−1 ∈ NH(u0) ∩ (X1 ∪ X2) where i1 < i2 < . . . < i2t−1. If uit ∈ X1 then it ≤ m−λ+1. In this case, u0 is adjacent to u1, ui1, ui2, . . . , uit−1 and belongs to the cycle (u0, uit, uit+1, . . . , um = u0) whose length is m−it+1. This produces a copy of Ct(l) with the center at u0 where l = m−it+1 ≥ m−(m− λ+1)+1 = λ. Alternatively, if uit ∈ X2 then it ≥ λ−1. In this case, u0 is adjacent to uit+1, uit+2, . . . , ui2t−1, um−1 and belongs to the cycle (u0, u1, . . . , uit, um = u0) whose length is it + 1. This produces a copy of Ct(l) with the center at u0 where

- l = it + 1 ≥ λ. ⊔⊓


Proof of Theorem 1.4 We are going to show that any k-minimal graph G contains a copy of Cr(l). By Theorem 1.2, G contains a cycle (u0, u1, . . . , um−1, um = u0) of length m ≥ k. Let X = {u0, u1, . . . , um−1}. Then dG(ui) = ti + ri where ti = |NG(ui)∩X| and ri = |NG(ui)\X| for i = 0,1, . . . , m−1. According to Remark 1.5,

m−1

(ti + 2ri) = 2dG(X) > m · (k − 1).

i=0

Thus, there is such an index i that ti + 2ri ≥ k. If ri ≥ r then G contains a copy of Cr(m) with the center at ui. Suppose ri < r. Let H be the subgraph of G

induced by X. We are going to apply Lemma 3.1 with parameters t = r − ri and λ = k − r + 1. To be able to invoke it, we need to demonstrate that λ ≥ 2 and

dH(ui) = ti ≥ 2(r − ri) − 1 + max{2(k − r + 1) − m − 1,2}

= max{2k − 2ri − m,2r − 2ri + 1} .

Indeed, on one hand, since ti + 2ri ≥ k, we get ti ≥ k − 2ri = 2k − 2ri − k ≥ 2k−2ri−m. On the other hand, since r ≤ (k−1)/2, we get ti ≥ k−2ri ≥ 2r−2ri+1. Also, r ≤ (k −1)/2 implies λ = k −r + 1 ≥ 2. By Lemma 3.1, H contains a copy of Ct(l) with the center at ui where t = r − ri and l ≥ λ = k − r + 1. Now we use the ri vertices from NG(ui)\X to extend it to a copy of Cr(l) where l + r ≥ k + 1. ⊓⊔

Acknowledgements The author would like to thank the referees for their suggestions and comments.

References

- 1. Ajtai M., Koml´os J., Simonovits M., Szemer´edi E.: On the approximative solution of the Erd˝s–So´s conjecture on trees (manuscript)
- 2. Ajtai M., Koml´os J., Simonovits M., Szemer´edi E.: Some elementary lemmas on the Erd˝s– S´os conjecture for trees (manuscript)
- 3. Ajtai M., Koml´os J., Simonovits M., Szemer´edi E.: The solution of the Erd˝s–So´s conjecture for large trees (manuscript)
- 4. Erd˝s P.: Extremal problems in graph theory. In: Fiedler M. (ed.) Theory of Graphs and its Applications, pp. 29-36. Academic Press (1965)
- 5. Erd˝s P., Gallai T.: On maximal paths and circuits of graphs. Acta Math. Acad. Sci. Hungar. 10, 337-356 (1959)
- 6. Fan G., Sun L.: The Erd˝s–So´s conjecture for spiders. Discrete Math. 307, 3055-3062

(2007)

- 7. Fan G., Hong Y., Liu Q.: The Erd˝s–So´s conjecture for spiders. https://arxiv.org/pdf/1804.06567.pdf (2018). Accessed 19 April 2018
- 8. Faudree R. J., Schelp R. H.: Path Ramsey numbers in multicolorings. J. Combin. Theory B 19, 150-160 (1975)
- 9. Kalai G.: Micha Perles geometric proof of the Erd˝s–So´s conjecture for caterpillars. https://gilkalai.wordpress.com/2017/08/29/micha-perles-geometric-proof-of-theerdos-sos-conjecture-for-caterpillars/ (2017). Accessed 19 April 2018
- 10. Kopylov G. N.: Maximal paths and cycles in a graph. Dokl. Akad. Nauk SSSR 234, 19-21

(1977) (English translation: Soviet Math. Dokl. 18 593-596 (1977))

- 11. McLennan A.: The Erd˝s–So´s conjecture for trees of diameter four. J. Graph Theory 49, 291-301 (2005)
- 12. Moser W., Pach J.: Recent developments in combinatorial geometry. In: Pach J. (ed.) New Trends in Discrete and Computational Geometry, pp. 281–302. Algorithms and Combinatorics, vol. 10, Springer, Berlin, Heidelberg (1993)
- 13. Sidorenko A.: Asymptotic solution for a new class of forbidden r-graphs. Combinatorica 9, 207-215 (1989)
- 14. Wo´zniak M.: On the Erd˝s–So´s conjecture. J. Graph Theory 21 229-234 (1996)


