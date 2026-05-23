arXiv:1204.6645v2[math.CO]16Oct2013

Extremal results in sparse pseudorandom graphs

David Conlon∗ Jacob Fox† Yufei Zhao ‡ Accepted for publication in Advances in Mathematics

Abstract

Szemer´edi’s regularity lemma is a fundamental tool in extremal combinatorics. However, the original version is only helpful in studying dense graphs. In the 1990s, Kohayakawa and Ro¨dl proved an analogue of Szemer´edi’s regularity lemma for sparse graphs as part of a general program toward extending extremal results to sparse graphs. Many of the key applications of Szemer´edi’s regularity lemma use an associated counting lemma. In order to prove extensions of these results which also apply to sparse graphs, it remained a well-known open problem to prove a counting lemma in sparse graphs.

The main advance of this paper lies in a new counting lemma, proved following the functional approach of Gowers, which complements the sparse regularity lemma of Kohayakawa and Ro¨dl, allowing us to count small graphs in regular subgraphs of a suﬃciently pseudorandom graph. We use this to prove sparse extensions of several well-known combinatorial theorems, including the removal lemmas for graphs and groups, the Erdo˝s-Stone-Simonovits theorem and Ramsey’s theorem. These results extend and improve upon a substantial body of previous work.

## Contents

- 1 Introduction 2

- 1.1 Pseudorandom graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
- 1.2 Extremal results in pseudorandom graphs . . . . . . . . . . . . . . . . . . . . . . . . 4
- 1.3 Regularity and counting lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8


- 2 Counting strategy 13

- 2.1 Two-sided counting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
- 2.2 One-sided counting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16


- 3 Counting in Γ 18


- 3.1 Example: counting triangles in Γ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
- 3.2 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
- 3.3 Counting graphs in Γ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
- 3.4 Counting partial embeddings into Γ . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
- 3.5 Exceptional sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22


![image 1](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile1.png>)

∗Mathematical Institute, Oxford OX1 3LB, United Kingdom. E-mail: david.conlon@maths.ox.ac.uk. Research supported by a Royal Society University Research Fellowship.

†Department of Mathematics, MIT, Cambridge, MA 02139-4307. Email: fox@math.mit.edu. Research supported by a Simons Fellowship and NSF grant DMS-1069197.

‡Department of Mathematics, MIT, Cambridge, MA 02139-4307. Email: yufeiz@math.mit.edu. Research supported by an Akamai Presidential Fellowship.

- 4 Counting in G 23

- 4.1 Doubling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
- 4.2 Densiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
- 4.3 Counting C4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
- 4.4 Finishing the proof of the counting lemma . . . . . . . . . . . . . . . . . . . . . . . . 30
- 4.5 Tutorial: determining jumbledness requirements . . . . . . . . . . . . . . . . . . . . . 31


- 5 Inheriting regularity 34

- 5.1 C4 implies DISC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
- 5.2 K1,2,2 implies inheritance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39


- 6 One-sided counting 40
- 7 Counting cycles 42

- 7.1 Subdivision densiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
- 7.2 One-sided cycle counting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50


- 8 Applications 51

- 8.1 Erd˝os-Stone-Simonovits theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
- 8.2 Ramsey’s theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
- 8.3 Graph removal lemma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
- 8.4 Removal lemma for groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55


- 9 Concluding remarks 56


- 9.1 Sharpness of results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
- 9.2 Relative quasirandomness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
- 9.3 Induced extensions of counting lemmas and extremal results . . . . . . . . . . . . . . 59
- 9.4 Other sparse regularity lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
- 9.5 Algorithmic applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
- 9.6 Multiplicity results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64


## 1 Introduction

Szemere´di’s regularity lemma is one of the most powerful tools in extremal combinatorics. Roughly speaking, it says that the vertex set of every graph can be partitioned into a bounded number of parts so that the induced bipartite graph between almost all pairs of parts is pseudorandom. Many important results in graph theory, such as the graph removal lemma and the Erd˝os-StoneSimonovits theorem on Tura´n numbers, have straightforward proofs using the regularity lemma.

Crucial to most applications of the regularity lemma is the use of a counting lemma. A counting lemma, roughly speaking, is a result that says that the number of embeddings of a ﬁxed graph H into a pseudorandom graph G can be estimated by pretending that G were a genuine random graph. The combined application of the regularity lemma and a counting lemma is known as the regularity method, and has important applications in graph theory, combinatorial geometry, additive combinatorics and theoretical computer science. For surveys on the regularity method and its applications, see [57, 62, 76].

One of the limitations of Szemere´di’s regularity lemma is that it is only meaningful for dense graphs. While an analogue of the regularity lemma for sparse graphs has been proven by Kohayakawa [54] and by Ro¨dl (see also [44, 80]), the problem of proving an associated counting

lemma for sparse graphs has turned out to be much more diﬃcult. In random graphs, proving such an embedding lemma is a famous problem, known as the K LR conjecture [55], which has only been resolved very recently [10, 26].

Establishing an analogous result for pseudorandom graphs has been a central problem in this area. Certain partial results are known in this case [59, 61], but it has remained an open problem to prove a counting lemma for embedding a general ﬁxed subgraph. We resolve this diﬃculty, proving a counting lemma for embedding any ﬁxed small graph into subgraphs of sparse pseudorandom graphs.

As applications, we prove sparse extensions of several well-known combinatorial theorems, including the removal lemmas for graphs and groups, the Erd˝os-Stone-Simonovits theorem, and Ramsey’s theorem. Proving such sparse analogues for classical combinatorial results has been an important trend in modern combinatorics research. For example, a sparse analogue of Szemere´di’s theorem was an integral part of Green and Tao’s proof [52] that the primes contain arbitrarily long arithmetic progressions.

### 1.1 Pseudorandom graphs

The binomial random graph Gn,p is formed by taking an empty graph on n vertices and choosing to add each edge independently with probability p. These graphs tend to be very well-behaved. For example, it is not hard to show that with high probability all large vertex subsets X,Y have density approximately p between them. Motivated by the question of determining when a graph behaves in a random-like manner, Thomason [88, 89] began the ﬁrst systematic study of this property. Using a slight variant of Thomason’s notion, we say that a graph on vertex set V is (p,β)-jumbled if, for all vertex subsets X,Y ⊆ V ,

![image 2](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile2.png>)

|e(X,Y ) − p|X||Y || ≤ β |X||Y |.

The random graph Gn,p is, with high probability, (p,β)-jumbled with β = O(√pn). It is not hard to show [33, 35] that this is optimal and that a graph on n vertices with p ≤ 1/2 cannot be (p,β)jumbled with β = o(√pn). Nevertheless, there are many explicit examples which are optimally jumbled in that β = O(√pn). The Paley graph with vertex set Zp, where p ≡ 1(mod 4) is prime, and edge set given by connecting x and y if their diﬀerence is a quadratic residue is such a graph with p = 21 and β = O(√n). Many more examples are given in the excellent survey [64].

![image 3](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile3.png>)

![image 4](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile4.png>)

![image 5](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile5.png>)

![image 6](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile6.png>)

![image 7](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile7.png>)

A fundamental result of Chung, Graham and Wilson [19] states that for graphs of density p, where p is a ﬁxed positive constant, the property of being (p,o(n))-jumbled is equivalent to a number of other properties that one would typically expect in a random graph. The following theorem details some of these many equivalences.

Theorem. For any ﬁxed 0 < p < 1 and any sequence of graphs (Γn)n∈N with |V (Γn)| = n the following properties are equivalent.

- P1: Γn is (p,o(n))-jumbled, that is, for all subsets X,Y ⊆ V (Γn), e(X,Y ) = p|X||Y | + o(n2);
- P2: e(Γn) ≥ p n2 +o(n2), λ1(Γn) = pn+o(n) and |λ2(Γn)| = o(n), where λi(Γn) is the ith largest eigenvalue, in absolute value, of the adjacency matrix of Γn;
- P3: for all graphs H, the number of labeled induced copies of H in Γn is p(2ℓ)nℓ + o(nℓ), where ℓ = V (H);
- P4: e(Γn) ≥ p n2 +o(n2) and the number of labeled cycles of length 4 in Γn is at most p4n4+o(n4).


Any graph sequence which satisﬁes any (and hence all) of these properties is said to be pquasirandom. The most surprising aspect of this theorem, already hinted at in Thomason’s work, is that if the number of cycles of length 4 is as one would expect in a binomial random graph then this is enough to imply that the edges are very well-spread. This theorem has been quite inﬂuential. It has led to the study of quasirandomness in other structures such as hypergraphs [16, 47], groups [49], tournaments, permutations and sequences (see [18] and it references), and progress on problems in diﬀerent areas (see, e.g., [22, 48, 49]). It is also closely related to Szemere´di’s regularity lemma and its recent hypergraph generalization [48, 69, 77, 87] and all proofs of Szemere´di’s theorem [85] on long arithmetic progressions in dense subsets of the integers use some notion of quasirandomness.

For sparser graphs, the equivalences between the natural generalizations of these properties are not so clear cut (see [17, 56, 61] for discussions). In this case, it is natural to generalize the jumbledness condition for dense graphs by considering graphs which are (p,o(pn))-jumbled. Otherwise, we would not even have control over the density in the whole set. However, it is no longer the case that being (p,o(pn))-jumbled implies that the number of copies of any subgraph H agrees approximately with the expected count. For H = K3,3 and p = n−1/3, it is easy to see this by taking the random graph Gn,p and changing three vertices u, v and w so that they are each connected to everything else. This does not aﬀect the property of being (p,o(pn))-jumbled but it does aﬀect the K3,3 count, since as well as the roughly p9n6 = n3 copies of K3,3 that one expects in a random graph, one gets a further Ω(n3) copies of K3,3 containing all of u, v and w.

However, for any given graph H one can ﬁnd a function βH := βH(p,n) such that if Γ is a (p,βH)-jumbled graph then Γ contains a copy of H. Our chief concern in this paper will be to determine jumbledness conditions which are suﬃcient to imply other properties. In particular, we will be concerned with determining conditions under which certain combinatorial theorems continue to hold within jumbled graphs.

One particularly well-known class of (p,β)-jumbled graphs is the collection of (n,d,λ)-graphs. These are graphs on n vertices which are d-regular and such that all eigenvalues of the adjacency matrix, save the largest, are smaller in absolute value than λ. The famous expander mixing lemma tells us that these graphs are (p,β)-jumbled with p = d/n and β = λ. Bilu and Linial [11] proved a converse of this fact, showing that every (p,β)-jumbled d-regular graph is an (n,d,λ)-graph with λ = O(β log(d/β)). This shows that the jumbledness parameter β and the second largest in absolute value eigenvalue λ of a regular graph are within a logarithmic factor of each other.

Pseudorandom graphs have many surprising properties and applications and have recently attracted a lot of attention both in combinatorics and theoretical computer science (see, e.g., [64]). Here we will focus on their behavior with respect to extremal properties. We discuss these properties in the next section.

### 1.2 Extremal results in pseudorandom graphs

In this paper, we study the extent to which several well-known combinatorial statements continue to hold relative to pseudorandom graphs or, rather, (p,β)-jumbled graphs and (n,d,λ)-graphs.

One of the most important applications of the regularity method is the graph removal lemma [4, 78]. In the following statement and throughout the paper, v(H) and e(H) will denote the number of vertices and edges in the graph H, respectively. The graph removal lemma states that for every ﬁxed graph H and every ǫ > 0 there exists δ > 0 such that if G contains at most δnv(H) copies of H then G may be made H-free by removing at most ǫn2 edges. This innocent looking result, which follows easily from Szemere´di’s regularity lemma and the graph counting lemma, has surprising applications in diverse areas, amongst others a simple proof of Roth’s theorem on 3-term arithmetic progressions in dense subsets of the integers. It is also much more diﬃcult to prove than

one might expect, the best known bound [37] on δ−1 being a tower function of height on the order of log ǫ−1.

An analogue of this result for random graphs (and hypergraphs) was proven in [25]. For pseudorandom graphs, the following analogue of the triangle removal lemma was recently proven by Kohayakawa, Ro¨dl, Schacht and Skokan [59].

Theorem. For every ǫ > 0, there exist δ > 0 and c > 0 such that if β ≤ cp3n then any (p,β)jumbled graph Γ on n vertices has the following property. Any subgraph of Γ containing at most δp3n3 triangles may be made triangle-free by removing at most ǫpn2 edges.

Here we extend this result to all H. The degeneracy d(H) of a graph H is the smallest nonnegative integer d for which there exists an ordering of the vertices of H such that each vertex has at most d neighbors which appear earlier in the ordering. Equivalently, it may be deﬁned as

- d(H) = max{δ(H′) : H′ ⊆ H}, where δ(H) is the minimum degree of H. Throughout the paper, we will also use the standard notation ∆(H) for the maximum degree of H.


The parameter we will use in our theorems, which we refer to as the 2-degeneracy d2(H), is related to both of these natural parameters. Given an ordering v1,... ,vm of the vertices of H and i ≤ j, let Ni−1(j) be the number of neighbors vh of vj with h ≤ i − 1. We then deﬁne d2(H) to be the minimum d for which there is an ordering of the edges as v1,... ,vm such that for any edge vivj with i < j the sum Ni−1(i)+Ni−1(j) ≤ 2d. Note that d2(H) may be a half-integer. For comparison with degeneracy, note that d(2H) ≤ d2(H) ≤ d(H) − 21 and both sides can be sharp.

![image 8](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile8.png>)

![image 9](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile9.png>)

- Theorem 1.1. For every graph H and every ǫ > 0, there exist δ > 0 and c > 0 such that if β ≤ cpd2(H)+3n then any (p,β)-jumbled graph Γ on n vertices has the following property. Any subgraph of Γ containing at most δpe(H)nv(H) copies of H may be made H-free by removing at most ǫpn2 edges.


We remark that for many graphs H, the constant 3 in the exponent of this theorem may be improved, and this applies equally to all of the theorems stated below. While we will not dwell on this comment, we will call attention to it on occasion throughout the paper, pointing out where the above result may be improved. Note that the above theorem generalizes the graph removal lemma by considering the case Γ = Kn, which is (p,β)-jumbled with p = 1 and β = 1. For the same reason, the other results we establish extend the original versions.

Green [51] developed an arithmetic regularity lemma and used it to deduce an arithmetic removal lemma in abelian groups which extends Roth’s theorem. Green’s proof of the arithmetic regularity lemma relies on Fourier analytic techniques. Kra´l, Serra and Vena [63] found a new proof of the arithmetic removal lemma using the removal lemma for directed cycles which extends to all groups. They proved that for each ǫ > 0 and integer m ≥ 3 there is δ > 0 such that if G is a group of order n and A1,... ,Am are subsets of G such that there are at most δnm−1 solutions to the equation x1x2 ··· xm = 1 with xi ∈ Ai for all i, then it is possible to remove at most ǫn elements from each set Ai so as to obtain sets A′i for which there are no solutions to x1x2 ··· xm = 1 with xi ∈ A′i for all i.

By improving the bound in Theorem 1.1 for cycles, we obtain the following sparse extension of the removal lemma for groups. The Cayley graph G(S) of a subset S of a group G has vertex set G and (x,y) is an edge of G if x−1y ∈ S. We say that a subset S of a group G is (p,β)jumbled if the Cayley graph G(S) is (p,β)-jumbled. When G is abelian, if x∈S χ(x) ≤ β for all nontrivial characters χ: G → C, then S is (||GS||,β)-jumbled (see [59, Lemma 16]). Let k3 = 3, k4 = 2, km = 1 + m1−3 if m ≥ 5 is odd, and km = 1 + m1−4 if m ≥ 6 is even. Note that km tends to

![image 10](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile10.png>)

![image 11](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile11.png>)

![image 12](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile12.png>)

- 1 as m → ∞.


- Theorem 1.2. For each ǫ > 0 and integer m ≥ 3, there are c,δ > 0 such that the following holds. Suppose B1,... ,Bm are subsets of a group G of order n such that each Bi is (p,β)-jumbled with β ≤ cpkmn. If subsets Ai ⊆ Bi for i = 1,... ,m are such that there are at most δ|B1|··· |Bm|/n solutions to the equation x1x2 ··· xm = 1 with xi ∈ Ai for all i, then it is possible to remove at most ǫ|Bi| elements from each set Ai so as to obtain sets A′i for which there are no solutions to x1x2 ··· xm = 1 with xi ∈ A′i for all i.


This result easily implies a Roth-type theorem in quite sparse pseudorandom subsets of a group. We say that a subset B of a group G is (ǫ,m)-Roth if for all integers a1,... ,am which satisfy a1 + ··· + am = 0 and gcd(ai,|G|) = 1 for 1 ≤ i ≤ m, every subset A ⊆ B which has no nontrivial solution to xa11xa22 ··· xamm = 1 has |A| ≤ ǫ|B|.

Corollary 1.3. For each ǫ > 0 and integer m ≥ 3, there is c > 0 such that the following holds. If G is a group of order n and B is a (p,β)-jumbled subset of G with β ≤ cpkmn, then B is (ǫ,m)-Roth.

Note that Roth’s theorem on 3-term arithmetic progressions in dense sets of integers, follows from the special case of this result with B = G = Zn, m = 3, and a1 = a2 = 1, a3 = −2. The rather weak pseudorandomness condition in Corollary 1.3 shows that even quite sparse pseudorandom subsets of a group have the Roth property. For example, if B is optimally jumbled, in that β = O(√pn) and p ≥ Cn−

- 1

![image 13](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile13.png>)

- 2km−1, then B is (ǫ,m)-Roth. This somewhat resembles a key part of the


![image 14](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile14.png>)

proof of the Green-Tao theorem that the primes contain arbitrarily long arithmetic progressions, where they show that pseudorandom sets of integers have the Szemere´di property. As Corollary 1.3 applies to quite sparse pseudorandom subsets, it may lead to new applications in number theory.

Our methods are quite general and also imply similar results for other well-known combinatorial theorems. We say that a graph Γ is (H,ǫ)-Tura´n if any subgraph of Γ with at least

1 χ(H) − 1

1 −

+ ǫ e(Γ)

![image 15](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile15.png>)

edges contains a copy of H. Tura´n’s theorem itself [91], or rather a generalization known as the Erd˝os-Stone-Simonovits theorem [30], says that Kn is (H,ǫ)-Tura´n provided that n is large enough.

To ﬁnd other graphs which are (H,ǫ)-Tura´n, it is natural to try the random graph Gn,p. A recent result of Conlon and Gowers [25], also proved independently by Schacht [79], states that for every t ≥ 3 and ǫ > 0 there exists a constant C such that if p ≥ Cn−2/(t+1) the graph Gn,p is with high probability (Kt,ǫ)-Tura´n. This conﬁrms a conjecture of Haxell, Kohayakawa,  Luczak and Ro¨dl [53, 55] and, up to the constant C, is best possible. Similar results also hold for more general graphs H and hypergraphs.

For pseudorandom graphs and, in particular, (n,d,λ)-graphs, Sudakov, Szabo´ and Vu [84] showed the following. A similar result, but in a slightly more general context, was proved by Chung [15].

Theorem. For every ǫ > 0 and every positive integer t ≥ 3, there exists c > 0 such that if λ ≤ cdt−1/nt−2 then any (n,d,λ)-graph is (Kt,ǫ)-Tura´n.

For t = 3, an example of Alon [2] shows that this is best possible. His example gives something even stronger, a triangle-free (n,d,λ)-graph for which λ ≤ c

√

d and d ≥ n2/3. Therefore, no combinatorial statement about the existence of triangles as subgraphs can surpass the threshold λ ≤ cd2/n. It has also been conjectured [38, 64, 84] that λ ≤ cdt−1/nt−2 is a natural boundary for ﬁnding Kt as a subgraph in a pseudorandom graph, but no examples of such graphs exist for t ≥ 4. Finding such graphs remains an important open problem on pseudorandom graphs.

![image 16](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile16.png>)

For triangle-free graphs H, Kohayakawa, Ro¨dl, Schacht, Sissokho and Skokan [58] proved the following result which gives a jumbledness condition that implies that a graph is (H,ǫ)-Tura´n.

Theorem. For any ﬁxed triangle-free graph H and any ǫ > 0, there exists c > 0 such that if β ≤ cpν(H)n then any (p,β)-jumbled graph on n vertices is (H,ǫ)-Tura´n. Here ν(H) = 21(d(H) + D(H) + 1), where D(H) = min{2d(H),∆(H)}.

![image 17](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile17.png>)

More recently, the case where H is an odd cycle was studied by Aigner-Horev, H`an and Schacht [1], who proved the following result, optimal up to the logarithmic factors [6]. Theorem. For every odd integer ℓ ≥ 3 and any ǫ > 0, there exists c > 0 such that if β logℓ−3 n ≤ cp1+1/(ℓ−2)n then any (p,β)-jumbled graph on n vertices is (Cℓ,ǫ)-Tura´n.

In this paper, we prove that a similar result holds, but for general graphs H and, in most cases, with a better bound on β.

- Theorem 1.4. For every graph H and every ǫ > 0, there exists c > 0 such that if β ≤ cpd2(H)+3n then any (p,β)-jumbled graph on n vertices is (H,ǫ)-Tura´n.

We may also prove a structural version of this theorem, known as a stability result. In the dense case, this result, due to Erd˝os and Simonovits [82], states that if an H-free graph contains almost 1 − χ(H1)−1 n2 edges, then it must be very close to being (χ(H) − 1)-partite.

![image 18](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile18.png>)

- Theorem 1.5. For every graph H and every ǫ > 0, there exist δ > 0 and c > 0 such that if β ≤ cpd2(H)+3n then any (p,β)-jumbled graph Γ on n vertices has the following property. Any H-free subgraph of Γ with at least 1 − χ(H1)−1 − δ p n2 edges may be made (χ(H) − 1)-partite by removing at most ǫpn2 edges.

![image 19](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile19.png>)

The ﬁnal main result that we will prove concerns Ramsey’s theorem [71]. This states that for any graph H and positive integer r, if n is suﬃciently large, any r-coloring of the edges of Kn contains a monochromatic copy of H.

To consider the analogue of this result in sparse graphs, let us say that a graph Γ is (H,r)Ramsey if, in any r-coloring of the edges of Γ, there is guaranteed to be a monochromatic copy of H. For Gn,p, a result of Ro¨dl and Rucin´ski [75] determines the threshold down to which the random graph is (H,r)-Ramsey with high probability. For most graphs, including the complete graph Kt, this threshold is the same as for the Tura´n property. These results were only extended to hypergraphs comparatively recently, by Conlon and Gowers [25] and by Friedgut, Ro¨dl and Schacht [41].

Very little seems to be known about the (H,r)-Ramsey property relative to pseudorandom graphs. In the triangle case, results of this kind are implicit in some recent papers [28, 67] on Folkman numbers, but no general theorem seems to be known. We prove the following.

- Theorem 1.6. For every graph H and every positive integer r ≥ 2, there exists c > 0 such that if β ≤ cpd2(H)+3n then any (p,β)-jumbled graph on n vertices is (H,r)-Ramsey.


One common element to all these results is the requirement that β ≤ cpd2(H)+3n. It is not hard to see that this condition is almost sharp. Consider the binomial random graph on n vertices where each edge is chosen with probability p = cn−2/d(H), where c < 1. By the deﬁnition of degeneracy, there exists some subgraph H′ of H such that d(H) is the minimum degree of H′. Therefore,

- e(H′) ≥ v(H′)d(H)/2 and the expected number of copies of H′ is at most pe(H′)nv(H′) ≤ (pd(H)/2n)v(H′) < 1.


We conclude that with positive probability Gn,p does not contain a copy of H′ or, consequently, of H. On the other hand, with high probability, it is (p,β)-jumbled with

β = O(√pn) = O(p(d(H)+2)/4n).

![image 20](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile20.png>)

Since d2(H) diﬀers from d(H) by at most a constant factor, we therefore see that, up to a multiplicative constant in the exponent of p, our results are best possible.

If H = Kt, it is suﬃcient, for the various combinatorial theorems above to hold, that the graph Γ be (p,cptn)-jumbled. For triangles, the example of Alon shows that there are (p,cp2n)-jumbled graphs which do not contain any triangles and, for t ≥ 4, it is conjectured [38, 64, 84] that there are (p,cpt−1n)-jumbled graphs which do not contain a copy of Kt. If true, this would imply that in the case of cliques all of our results are sharp up to an additive constant of one in the exponent. A further discussion relating to the optimal exponent of p for general graphs is in the concluding remarks.

### 1.3 Regularity and counting lemmas

One of the key tools in extremal graph theory is Szemere´di’s regularity lemma [86]. Roughly speaking, this says that any graph may be partitioned into a collection of vertex subsets so that the bipartite graph between most pairs of vertex subsets is random-like. To be more precise, we introduce some notation. It will be to our advantage to be quite general from the outset.

A weighted graph on a set of vertices V is a symmetric function G: V × V → [0,1]. Here symmetric means that G(x,y) = G(y,x). A weighted graph is bipartite (or multipartite) if it is supported on the edge set of a bipartite (or multipartite graph). A graph can be viewed as a weighted graph by taking G to be the characteristic function of the edges.

Note that here and throughout the remainder of the paper, we will use integral notation for summing over vertices in a graph. For example, if G is a bipartite graph with vertex sets X and Y , and f is any function X × Y → R, then we write

1 |X| |Y | x∈X y∈Y

f(x,y).

f(x,y) dxdy :=

![image 21](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile21.png>)

- x∈X
- y∈Y


The measure dx will always denote the uniform probability distribution on X. The advantage of the integral notation is that we do not need to keep track of the number of vertices in G. All our formulas are, in some sense, scale-free with respect to the order of G. Consequently, our results also have natural extensions to graph limits [66], although we do not explore this direction here.

Deﬁnition 1.7 (DISC). A weighted bipartite graph G: X × Y → [0,1] is said to satisfy the discrepancy condition DISC(q,ǫ) if

(G(x,y) − q)u(x)v(y) dxdy ≤ ǫ (1)

- x∈X
- y∈Y


for all functions u: X → [0,1] and v: Y → [0,1]. In any weighted graph G, if X and Y are subsets of vertices of G, we say that the pair (X,Y )G satisﬁes DISC(q,ǫ) if the induced weighted graph on

- X × Y satisﬁes DISC(q,ǫ). The usual deﬁnition for discrepancy of an (unweighted) bipartite graph G is that for all X′ ⊆ X,
- Y ′ ⊆ Y , we have |e(X′,Y ′) − q |X′| |Y ′|| ≤ ǫ|X| |Y |. It is not hard to see that the two notions of discrepancy are equivalent (with the same ǫ).


A partition V (G) = V1 ∪ ··· ∪ Vk is said to be equitable if all pieces in the partition are of comparable size, that is, if ||Vi| − |Vj|| ≤ 1 for all i and j. Szemere´di’s regularity lemma now says the following.

Theorem (Szemere´di’s regularity lemma). For every ǫ > 0 and every positive integer m0, there exists a positive integer M such that any weighted graph G has an equitable partition into k pieces with m0 ≤ k ≤ M such that all but at most ǫk2 pairs of vertex subsets (Vi,Vj) satisfy DISC(qij,ǫ) for some qij.

On its own, the regularity lemma would be an interesting result. But what really makes it so powerful is the fact that the discrepancy condition allows us to count small subgraphs. In particular, we have the following result, known as a counting lemma.

Proposition 1.8 (Counting lemma in dense graphs). Let G be a weighted m-partite graph with vertex subsets X1,X2,... ,Xm. Let H be a graph with vertex set {1,... ,m} and with e(H) edges. For each edge (i,j) in H, assume that the induced bipartite graph G(Xi,Xj) satisﬁes DISC(qij,ǫ). Deﬁne

G(H) :=

G(xi,xj) dx1 ··· dxm

x1∈X1,...,xm∈Xm (i,j)∈E(H)

and

q(H) :=

qij.

(i,j)∈E(H)

Then

|G(H) − q(H)| ≤ e(H)ǫ.

The above result, for an unweighted graph, is usually stated in the following equivalent way: the number of embeddings of H into G, where the vertex i ∈ V (H) lands in Xi, diﬀers from |X1||X2| ··· |Xm| (i,j)∈E(H) qij by at most e(H)ǫ|X1||X2| ··· |Xm|. Our notation G(H) can be viewed as the probability that a random embedding of vertices of H into their corresponding parts in G gives rise to a valid embedding as a subgraph.

Proposition 1.8 may be proven by telescoping (see, e.g., Theorem 2.7 in [12]). Consider, for example, the case where H is a triangle. Then G(x1,x2)G(x1,x3)G(x2,x3) − q12q13q23 may be rewritten as

(G(x1,x2) − q12)G(x1,x3)G(x2,x3) + q12(G(x1,x3) − q13)G(x2,x3) + q12q13(G(x2,x3) − q23). (2)

Applying the discrepancy condition (1), we see that, after integrating the above expression over all x1 ∈ X1,x2 ∈ X2,x3 ∈ X3, each term in (2) is at most ǫ in absolute value. The result follows for triangles. The general case follows similarly.

In order to prove extremal results in sparse graphs, we would like to transfer some of this machinery to the sparse setting. Because the number of copies of a subgraph in a sparse graph G is small, the error between the expected count and the actual count must also be small for a counting lemma to be meaningful. Another way to put this is that we aim to achieve a small multiplicative error in our count.

Since we require smaller errors when counting in sparse graphs, we need stronger discrepancy hypotheses. In the following deﬁnition, we should view p as the order of magnitude density of the graph, so that the error terms should be bounded in the same order of magnitude. In a dense graph, p = 1. We assume that q ≤ p. It may be helpful to think of q/p as bounded below by some positive constant, although this is not strictly required.

- Deﬁnition 1.9 (DISC). A weighted bipartite graph G: X×Y → [0,1] is said to satisfy DISC(q,p,ǫ) if

- x∈X
- y∈Y


(G(x,y) − q)u(x)v(y) dxdy ≤ ǫp

for all functions u: X → [0,1] and v: Y → [0,1].

Unfortunately, discrepancy alone is not strong enough for counting in sparse graphs. Consider the following example. Let G be a tripartite graph with vertex sets X1,X2,X3, such that (X1,X2)G and (X2,X3)G satisfy DISC(q,p, 2ǫ). Let X2′ be a subset of X2 with size 2ǫp|X2|. Let G′ be modiﬁed from G by adding the complete bipartite graph between X1 and X2′, as well as the complete bipartite graph between X2′ and X3. The resulting pairs (X1,X2)G′ and (X2,X3)G′ satisfy DISC(q,p,ǫ). Consider the number of paths in G and G′ with one vertex from each of X1,X2,X3 in turn. Given the densities, we expect there to be approximately q2 |X1||X2||X3| such paths, and we would like the error to be δp2 |X1||X2| |X3| for some small δ that goes to zero as ǫ goes to zero. However, the number of paths in G′ from X1 to X2′ to X3 is 2ǫp|X1||X2||X3|, which is already too large when p is small.

![image 22](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile22.png>)

![image 23](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile23.png>)

![image 24](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile24.png>)

For our counting lemma to work, G needs to be a relatively dense subgraph of a much more pseudorandom host graph Γ. In the dense case, Γ can be the complete graph. In the sparse world, we require Γ to satisfy the jumbledness condition. In practice, we will use the following equivalent deﬁnition. The equivalence follows by considering random subsets of X and Y , where x and y are chosen with probabilities u(x) and v(y), respectively.

- Deﬁnition 1.10 (Jumbledness). A bipartite graph Γ = (X ∪ Y,EΓ) is (p,γ |X| |Y |)-jumbled if


![image 25](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile25.png>)

![image 26](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile26.png>)

![image 27](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile27.png>)

(Γ(x,y) − p)u(x)v(y) dxdy ≤ γ

- x∈X
- y∈Y


u(x) dx

x∈X

v(y) dy (3)

y∈Y

for all functions u: X → [0,1] and v: Y → [0,1].

With the discrepancy condition deﬁned as in Deﬁnition 1.9, we may now state a regularity lemma for sparse graphs. Such a lemma was originally proved independently by Kohayakawa [54] and by Ro¨dl (see also [44, 80]). The following result, tailored speciﬁcally to jumbled graphs, follows easily from the main result in [54].

- Theorem 1.11 (Regularity lemma in jumbled graphs). For every ǫ > 0 and every positive integer m0, there exists η > 0 and a positive integer M such that if Γ is a (p,ηpn)-jumbled graph on n vertices any weighted subgraph G of Γ has an equitable partition into k pieces with m0 ≤ k ≤ M such that all but at most ǫk2 pairs of vertex subsets (Vi,Vj) satisfy DISC(qij,p,ǫ) for some qij.


The main result of this paper is a counting lemma which complements this regularity lemma. Proving such an embedding lemma has remained an important open problem ever since Kohayakawa and Ro¨dl ﬁrst proved the sparse regularity lemma. Most of the work has focused on applying the sparse regularity lemma in the context of random graphs. The key conjecture in this case, known as the K LR conjecture, concerns the probability threshold down to which a random graph is, with high probability, such that any regular subgraph contains a copy of a particular subgraph H. This conjecture has only been resolved very recently [10, 26]. For pseudorandom graphs, it has been a wide open problem to prove a counting lemma which complements the sparse regularity lemma. The ﬁrst progress on proving such a counting lemma was made recently in [59], where they proved a counting lemma for triangles. Here, we prove a counting lemma which works for any graph H.

Even for triangles, our counting lemma gives an improvement over the results in [59], since our results have polynomial-type dependence on the discrepancy parameters, whereas the results in [59] require exponential dependence since a weak regularity lemma was used as an immediate step during their proof of the triangle counting lemma.

Our results are also related to the work of Green and Tao [52] on arithmetic progressions in the primes. What they really prove is the stronger result that Szemere´di’s theorem on arithmetic progressions holds in subsets of the primes. In order to do this, they ﬁrst show that the primes, or rather the almost primes, are a pseudorandom subset of the integers and then that Szemere´di’s theorem continues to hold relative to such pseudorandom sets. In the language of their paper, our counting lemma is a generalized von Neumann theorem.

Here is the statement of our ﬁrst counting lemma. Note that, given a graph H, the line graph L(H) is the graph whose vertices are the edges of H and where two vertices are adjacent if their corresponding edges in H share an endpoint. Recall that d(·) is the degeneracy and ∆(·) is the maximum degree.

- Theorem 1.12. Let H be a graph with vertex set {1,... ,m} and with e(H) edges. For every θ > 0, there exist c,ǫ > 0 of size at least polynomial in θ so that the following holds.


Let p > 0 and let Γ be a graph with vertex subsets X1,... ,Xm and suppose that the bipartite

graph (Xi,Xj)Γ is (p,cpk |Xi| |Xj|)-jumbled for every i < j, where k ≥ min ∆(L(H2 ))+4, d(L(H2))+6 . Let G be a subgraph of Γ, with the vertex i of H assigned to the vertex subset Xi of G. For each edge ij in H, assume that (Xi,Xj)G satisﬁes DISC(qij,p,ǫ). Deﬁne

![image 28](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile28.png>)

![image 29](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile29.png>)

![image 30](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile30.png>)

G(H) :=

G(xi,xj) dx1 ··· dxm

x1∈X1,...,xm∈Xm (i,j)∈E(H)

and

q(H) :=

qij.

(i,j)∈E(H)

Then

|G(H) − q(H)| ≤ θpe(H). For some graphs H, our methods allow us to achieve slightly better values of k in Theorem

- 1.12. However, the value given in the theorem is the cleanest general statement. See Table 1 for some example of hypotheses on k for various graphs H. To see that the value of k is never far from best possible, we ﬁrst note that ∆(H) − 1 ≤ d(L(H)) ≤ ∆(H) + d(H) − 2.


Let H have maximum degree ∆. By considering the random graph Gn,p with p = n−1/∆, we can ﬁnd a (p,cp∆/2n)-jumbled graph Γ containing approximately pe(H)nv(H) labeled copies of H. We modify Γ to form Γ′ by ﬁxing one vertex v and connecting it to everything else. It is easy to check that the resulting graph Γ′ is (p,c′p∆/2n)-jumbled. However, the number of copies of H disagrees with the expected count, since there are approximately pe(H)nv(H) labeled copies from the original graph Γ and a further approximately pe(H)−∆nv(H)−1 = pe(H)nv(H) labeled copies containing v. We conclude that for k < ∆/2 we cannot hope to have such a counting lemma and, therefore, the value of k in Theorem 1.12 is close to optimal.

Since we are dealing with sparse graphs, the discrepancy condition 1.9 appears, at ﬁrst sight, to be rather weak. Suppose, for instance, that we have a sparse graph satisfying DISC(q,p,ǫ) between each pair of sets from V1,V2 and V3 and we wish to embed a triangle between the three sets. Then, a typical vertex v in V1 will have neighborhoods of size roughly q|V2| and q|V3| in V2 and V3, respectively. But now the condition DISC(q,p,ǫ) tells us nothing about the density of edges between the two neighborhoods. They are simply too small.

Table 1: Suﬃcient conditions on k in the jumbledness hypothesis (p,cpk |Xi||Xj|) for the counting lemmas of various graphs. Two-sided counting refers to results of the form |G(H) − q(H)| ≤ θpe(H) while one-sided counting refers to result of the form G(H) ≥ q(H) − θpe(H).

![image 31](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile31.png>)

![image 32](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile32.png>)

Two-sided counting One-sided counting H k ≥ k ≥

![image 33](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile33.png>)

Kt t t t ≥ 3 Cℓ 2 2 ℓ = 4

2 1 + 2⌊(ℓ−13)/2⌋ ℓ ≥ 5 K2,t t+22 52 t ≥ 3 Ks,t s+2t+1 s+32 3 ≤ s ≤ t Tree ∆(H2)+1 No jumbledness needed See Prop. 4.9 and 7.7 K1,2,2 4 4

![image 34](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile34.png>)

![image 35](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile35.png>)

![image 36](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile36.png>)

![image 37](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile37.png>)

![image 38](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile38.png>)

![image 39](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile39.png>)

![image 40](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile40.png>)

To get around this, Gerke, Kohayakawa, Ro¨dl and Steger [42] showed that if (X,Y ) is a pair satisfying DISC(q,p,ǫ) then, with overwhelmingly high probability, a small randomly chosen pair of subsets X′ ⊆ X and Y ′ ⊆ Y will satisfy DISC(q,p,ǫ′), where ǫ′ tends to zero with ǫ. We say that the pair inherits regularity. This may be applied eﬀectively to prove embedding lemmas in random graphs (see, for example, [43, 60]). For pseudorandom graphs, the beginnings of such an approach may be found in [59].

Our approach in this paper works in the opposite direction. Rather than using the inheritance property to aid us in proving counting lemmas, we ﬁrst show how one may prove the counting lemma and then use it to prove a strong form of inheritance in jumbled graphs. For example, we have the following theorem.

Proposition 1.13. For any α > 0, ξ > 0 and ǫ′ > 0, there exists c > 0 and ǫ > 0 of size at least polynomial in α,ξ,ǫ′ such that the following holds.

Let p ∈ (0,1] and qXY ,qXZ,qYZ ∈ [αp,p]. Let Γ be a tripartite graph with vertex sets X, Y and

- Z and G be a subgraph of Γ. Suppose that


- • (X,Y )Γ is (p,cp4 |X| |Y |)-jumbled and (X,Y )G satisﬁes DISC(qXY ,p,ǫ); and

![image 41](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile41.png>)

- • (X,Z)Γ is (p,cp2 |X| |Z|)-jumbled and (X,Z)G satisﬁes DISC(qXZ,p,ǫ); and

![image 42](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile42.png>)

- • (Y,Z)Γ is (p,cp3 |Y | |Z|)-jumbled and (Y,Z)G satisﬁes DISC(qY Z,p,ǫ).


![image 43](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile43.png>)

Then at least (1−ξ)|Z| vertices z ∈ Z have the property that |NX(z)| ≥ (1−ξ)qXZ |X|, |NY (z)| ≥ (1 − ξ)qYZ |Y |, and (NX(z),NY (z))G satisﬁes DISC(qXY ,p,ǫ′).

The question now arises as to why one would prove that the inheritance property holds if we already know its intended consequence. Surprisingly, there is another counting lemma, giving only a lower bound on G(H), which is suﬃcient to establish the various extremal results but typically requires a much weaker jumbledness assumption. The proof of this statement relies on the inheritance property in a critical way. The notations G(H) and q(H) were deﬁned in Theorem 1.12.

Theorem 1.14. For every ﬁxed graph H on vertex set {1,2,... ,m} and every α,θ > 0, there exist constants c > 0 and ǫ > 0 such that the following holds.

Let Γ be a graph with vertex subsets X1,... ,Xm and suppose that the bipartite graph (Xi,Xj)Γ is (p,cpd2(H)+3 |Xi| |Xj|)-jumbled for every i < j with ij ∈ E(H). Let G be a subgraph of Γ, with the vertex i of H assigned to the vertex subset Xi of G. For each edge ij of H, assume that (Xi,Xj)G satisﬁes DISC(qij,p,ǫ), where αp ≤ qij ≤ p. Then

![image 44](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile44.png>)

G(H) ≥ (1 − θ)q(H).

We refer to Theorem 1.14 as a one-sided counting lemma, as we get a lower bound for G(H) but no upper bound. However, in order to prove the theorems of Section 1.2, we only need a lower bound. The proof of Theorem 1.14 is a sparse version of a classical embedding strategy in regular graphs (see, for example, [20, 40, 50]). Note that, as in the theorems of Section 1.2, the exponent d2(H) + 3 can be improved for certain graphs H. We will say more about this later. Moreover, one cannot hope to do better than β = O(p(d(H)+2)/4n), so that the condition on β is sharp up to a multiplicative constant in the exponent of p. We suspect that the exponent may even be sharp up to an additive constant.

Organization. We will begin in the next section by giving a high level overview of the proof of our counting lemmas. In Section 3, we prove some useful statements about counting in the pseudorandom graph Γ. Then, in Section 4, we prove the sparse counting lemma, Theorem 1.12. The short proof of Proposition 1.13 and some related propositions about inheritance are given

- in Section 5. The proof of the one-sided counting lemma, which uses inheritance, is then given
- in Section 6. In Section 7, we take a closer look at one-sided counting in cycles. The sparse counting lemma has a large number of applications extending many classical results to the sparse setting. In Section 8, we discuss a number of them in detail, including sparse extensions of the Erd˝os-Stone-Simonovits theorem, Ramsey’s theorem, the graph removal lemma and the removal lemma for groups. In Section 9 we brieﬂy discuss a number of other applications, such as relative quasirandomness, induced Ramsey numbers, algorithmic applications and multiplicity results.


## 2 Counting strategy

In this section, we give a general overview of our approach to counting. There are two types of counting results: two-sided counting and one-sided counting. Two-sided counting refers to results of the form |G(H) − q(H)| ≤ θpe(H) while one-sided counting refers to results of the form G(H) ≥ q(H) − θpe(H). One-sided counting is always implied by two-sided counting, although sometimes we are able to obtain one-sided counting results under weaker hypotheses.

### 2.1 Two-sided counting

There are two main ingredients to the proof: doubling and densiﬁcation. These two procedures reduce the problem of counting embeddings of H to the same problem for some other graphs H′.

If a ∈ V (H), the graph H with a doubled, denoted Ha×2, is the graph created from V (H) by adding a new vertex a′ whose neighbors are precisely the neighbors of a. In the assignment of vertices of Ha×2 to vertex subsets of Γ, the new vertex a′ is assigned to the same vertex subset of Γ. For example, the following ﬁgure shows a triangle with a vertex doubled.

×2

=

A typical reduction using doubling is summarized in Figure 1. Each graph represents the claim that the number of embeddings of the graph drawn, where the straight edges must land in G and the wavy edges must land in Γ, is approximately what one would expect from multiplying together the appropriate edge densities between the vertex subsets of G and Γ.

The top arrow in Figure 1 is the doubling step. This allows us to reduce the problem of counting H to that of counting a number of other graphs, each of which may have some edges which embed into G and some which embed into Γ. For example, if we let H−a be the graph that we get by omitting every edge which is connected to a particular vertex a, we are interested in the number of copies of H−a in both G and Γ. We are also interested in the original graph H, but now on the understanding that the edges incident with a embed into G while those that do not touch a embed into Γ. Finally, we are interested in the graph Ha×2 formed by doubling the vertex a, but again the edges which do not touch a or its copy a′ only have to embed into Γ. This reduction, which is justiﬁed by an application of the Cauchy-Schwarz inequality, will be detailed in Section 4.1.

The bottom two arrows in Figure 1 are representative of another reduction, where we can reduce the problem of counting a particular graph, with edges that map to both G and Γ, into one where we only care about the edges that embed into G. We can make such a reduction because counting embeddings into Γ is much easier due to its jumbledness. We will discuss this reduction, amongst other properties of jumbled graphs Γ, in Section 3.

a

G(H)

# ⇑

G(H−a) g(Ha×2)

g(H)

Γ(H−a)

⇑

⇑

G(Ha,a×2) G(Ha)

Figure 1: The doubling reduction. Each graph represents some counting lemma. The straight edges must embed into G while wavy edges must embed into the jumbled graph Γ.

For triangles, a similar reduction is shown in Figure 2. In the end, we have changed the task of counting triangles to the task of counting the number of cycles of length 4. It would be natural now to apply doublng to the 4-cycle but, unfortunately, this process is circular. Instead, we introduce an alternative reduction process which we refer to as densiﬁcation.

# ⇑ ⇑

Figure 2: The doubling reduction for counting triangles.

In the above reduction from triangles to 4-cycles, two of the vertices of the 4-cycle are embedded into the same part Xi of G. We actually consider the more general setting where the vertices of the 4-cycle lie in diﬀerent parts, X1,X2,X3,X4, of G.

Assume without loss of generality that there is no edge between X1 and X3 in G. Let us add a weighted graph between X1 and X3, where the weight on the edge x1x3 is proportional to the number of paths x1x4x3 for x4 ∈ X4. Since (X1,X4)G and (X3,X4)G satisfy discrepancy, the number of paths will be on the order of q14q34 |X4| for most pairs (x1,x3). After discarding a negligible set of pairs (x1,x3) that give too many paths, and then appropriately rescaling the weights of the other edges x1x3, we create a weighted bipartite graph between X1 and X3 that behaves like a dense weighted graph satisfying discrepancy. Furthermore, counting 4-cycles in X1,X2,X3,X4 is equivalent to counting triangles in X1,X2,X3 due to the choice of weights. We call this process densiﬁcation. It is illustrated below. In the ﬁgure, a thick edge signiﬁes that the bipartite graph that it embeds into is dense.

# ⇐

More generally, if b is a vertex of H of degree 2, with neighbors {a,c}, such that a and c are not adjacent, then densiﬁcation allows us to transform H by removing the edges ab and bc and adding a dense edge ac, as illustrated below. For more on this process, we refer the reader to Section 4.2.

b

a

c

⇐

a c

We needed to count 4-cycles in order to count triangles, so it seems at ﬁrst as if our reduction from 4-cycles to triangles is circular. However, instead of counting triangles in a sparse graph, we now have a dense bipartite graph between one of the pairs of vertex subsets. Since it is easier to

⇑

⇑

⇑

Figure 3: The doubling reduction for triangles with one dense edge.

count in dense graphs than in sparse graphs, we have made progress. The next step is to do doubling again. This is shown in Figure 3. The bottommost arrow is another application of densiﬁcation.

We have therefore reduced the problem of counting triangles in a sparse graph to that of counting triangles in a dense weighted graph, which we already know how to do. This completes the counting lemma for 4-cycles.

In Figure 1, doubling reduces counting in a general H to counting H with one vertex deleted (which we handle by induction) as well as graphs of the form K1,t and K2,t. Trees like K1,t are not too hard to count. It therefore remains to count K2,t. As with counting C4 (the case t = 2), we ﬁrst perform a densiﬁcation.

# ⇐

The graph on the right can be counted using doubling and induction, as shown in Figure 4. Note that the C4 count is required as an input to this step. This then completes the proof of the counting lemma.

### 2.2 One-sided counting

For one-sided counting, we embed the vertices of H into those of G one at a time. By making a choice for where a vertex a of H lands in G, we shrink the set of possible targets for each neighbor of a. These target sets shrink by a factor roughly corresponding to the edge densities of G, as most vertices of G have close to the expected number of neighbors due to discrepancy. This allows us to obtain a lower bound on the number of embeddings of H into G.

The above argument is missing one important ingredient. When we shrink the set of possible targets of vertices in H, we do not know if G restricted to these smaller vertex subsets still satisﬁes

a

⇑

⇑

# ⇑ ⇑

induction

Figure 4: The doubling reduction for counting K2,t.

the discrepancy condition, which is needed for embedding later vertices. When G is dense, this is not an issue, since the restricted vertex subsets have size at least a constant factor of the original vertex subsets, and thus discrepancy is inherited. When G is sparse, the restricted vertex subsets can become much smaller than the original vertex subsets, so discrepancy is not automatically inherited.

To address this issue, we observe that discrepancy between two vertex sets follows from some variant of the K2,2 count (and the counting lemma shows that they are in fact equivalent). By our counting lemma, we also know that the graph below has roughly the expected count. This in turn implies that discrepancy is inherited in the neighborhoods of G since, roughly speaking, it implies that almost every vertex has roughly the expected number of 4-cycles in its neighborhood. The onesided counting approach sketched above then carries through. For further details on inheritance of discrepancy, see Section 5. The proof of the one-sided counting lemma may be found in Section 6.

We also prove a one-sided counting lemma for large cycles using much weaker jumbledness hypotheses. The idea is to extend densiﬁcation to more than two edges at a time. We will show how to transform a multiply subdivided edge into a single dense edge, as illustrated below.

# ⇐

Starting with a long cycle, we can perform two such densiﬁcations, as shown below. The resulting

triangle is easy to count, since a typical embedding of the top vertex gives a linear-sized neighborhood. The full details may be found in Section 7.

# ⇐

- 3 Counting in Γ In this section, we develop some tools for counting in Γ. Here is the setup for this section.


- Setup 3.1. Let Γ be a graph with vertex subsets X1,... ,Xm. Let p,c ∈ (0,1] and k ≥ 1. Let H be a graph with vertex set {1,... ,m}, with vertex a assigned to Xa. For every edge ab in H, one of the following two holds:


- • (Xa,Xb)Γ is (p,cpk |Xa||Xb|)-jumbled, in which case we set pab = p and say that ab is a sparse edge, or

![image 45](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile45.png>)

- • (Xa,Xb)Γ is a complete bipartite graph, in which case we set pab = 1 and say that ab is a dense edge.


Let Hsp denote the subgraph of H consisting of sparse edges.

### 3.1 Example: counting triangles in Γ

We start by showing, as an example, how to prove the counting lemma in Γ for triangles. Most of the ideas found in the rest of this section can already be found in this special case.

- Proposition 3.2. Assume Setup 3.1. Let H be a triangle with vertices {1,2,3}. Assume that k ≥ 2. Then Γ(H) − p3 ≤ 5cp3.


Proof. In the following integrals, we assume that x,y and z vary uniformly over X1,X2 and X3, respectively. We have the telescoping sum

Γ(H) − p3 =

(Γ(x,y) − p)Γ(x,z)Γ(y,z) dxdydz

x,y,z

+

p(Γ(x,z) − p)Γ(y,z) dxdydz +

x,y,z

p2(Γ(y,z) − p) dxdydz. (4)

x,y,z

The third integral on the right-hand side of (4) is bounded in absolute value by cp3 by the jumbledness of Γ. In particular, this implies that y,z Γ(y,z) dydz ≤ (1 + c)p. Similarly we have

x,z Γ(x,z) dxdz ≤ (1 + c)p. Using (3), the second integral is bounded in absolute value by

![image 46](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile46.png>)

![image 47](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile47.png>)

cp3

y

Γ(y,z) dz dy ≤ cp3

z

Γ(y,z) dydz ≤ c (1 + c)pp3.

![image 48](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile48.png>)

y,z

Finally, the ﬁrst integral on the right-hand side of (4) is bounded in absolute value by, using (3) and the Cauchy-Schwarz inequality,

![image 49](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile49.png>)

![image 50](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile50.png>)

![image 51](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile51.png>)

![image 52](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile52.png>)

cp2

z

Γ(x,z) dx

x

Γ(y,z) dy dz ≤ cp2

y

Γ(x,z) dxdz

x,z

Γ(y,z) dydz ≤ c(1 + c)p3.

y,z

(5)

Therefore, (4) is bounded in absolute value by 5cp3. Remark. (1) In the more general proof, the step corresponding to (5) will be slightly diﬀerent but is similar in its application of the Cauchy-Schwarz inequality.

![image 53](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile53.png>)

![image 54](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile54.png>)

![image 55](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile55.png>)

![image 56](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile56.png>)

(2) The proof shows that we do not need the full strength of the jumbledness everywhere—we only need (p,cp3/2 |X| |Z|)-jumbledness for (X,Z)Γ and (p,cp |Y ||Z|)-jumbledness for (Y,Z)Γ. In Section 6, it will be useful to have a counting lemma with such non-balanced jumbledness assumptions in order to optimize our result. To keep things simple and clear, we will assume balanced jumbledness conditions here and remark later on the changes needed when we wish to have optimal non-balanced ones.

![image 57](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile57.png>)

![image 58](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile58.png>)

### 3.2 Notation

In the proof of the counting lemmas we often meet expressions such as G(x1,x2)G(x1,x3)G(x2,x3) and their integrals. We introduce some compact notation for such products and integrals. Note that if we are counting copies of H, we will usually assign each vertex a of H to some vertex subset Xa and we will only be interested in counting those embeddings where each vertex of H is mapped into the vertex subset assigned to it. If U ⊆ V (H), a map U → V (G) or U → V (Γ) is called compatible if each vertex of U gets mapped into the vertex set assigned to it. We can usually assume without loss of generality that the vertex subsets Xa are disjoint for diﬀerent vertices of H, as we can always create a new multipartite graph with disjoint vertex subsets Xa with the same H-embedding counts as the original graph.

If f is a symmetric function on pairs of vertices of G (actually we only care about its values on Xa × Xb for ab ∈ E(H)) and x: V (H) → V (G) is any compatible map (we write x(a) = xa), then we deﬁne

f (H | x) :=

f(xa,xb).

ab∈E(H)

By taking the expectation as x varies uniformly over all compatible maps V (H) → V (G), we can deﬁne the value of a function on a graph.

f(H) := Ex [f (H | x)] =

f (H | x) dx.

x

We shall always assume that the measure dx is the uniform probability measure on compatible maps.

For unweighted graphs, we use G and Γ to denote also the characteristic function of the edge set of the graph, so that G(H) is the probability that a uniformly random compatible map V (H) → V (G) is a graph homomorphism from H to G. For weighted graphs, the value on the edges are the edge weights. For counting lemmas, we are interested in comparing G(H) with q(H), which comes from setting q(xa,xb) to be some constant qab for each ab ∈ E(H).

It will be useful to have some notation for the conditional sum of a function f given that some vertices have been ﬁxed. If U ⊆ V (H) and y: U → V (G) is any compatible map, then

f (H | y) := Ex [f (H | x) | x|U = y] =

f (H | y,z) dz,

z

where, in the integral, z varies uniformly over all compatible maps V (H) \ U → V (G), and the notation y,z denotes the compatible map V (H) → V (G) built from combining y and z. Note that when U = ∅, f (H | y) = f(H). When U = V (H), the two deﬁnitions of f (H | y) agree.

When U = {a1,... ,at}, we sometimes write y as a1 → y1, ... , at → yt, so we can write

- f (H | a1 → y1,... ,at → yt). Since we work with approximations frequently, it will be convenient if we introduce some short-


hand. If A,B,P are three quantities, we write

A ≈P c,ǫ

B

to mean that for every θ > 0, we can ﬁnd c,ǫ > 0 of size at least polynomial in θ (i.e., c,ǫ ≥ Ω(θr)

- as θ → 0 for some r > 0) so that |A − B| ≤ θP. Sometimes one of c or ǫ is omitted from the ≈ notation if θ does not depend on the parameter. Note that the dependencies do not depend on the parameters p and q, but may depend on the graphs to be embedded, e.g., H. For instance, a counting lemma can be phrased in the form


G(H)p(≈H)

q(H).

c,ǫ

### 3.3 Counting graphs in Γ

We begin by giving a counting lemma in Γ, which is signiﬁcantly easier than counting in G. We remark that a similar counting lemma for Γ an (n,d,λ) regular graph was proven by Alon (see [64, Thm. 4.10]).

sp))+2 2 , then

- Proposition 3.3. Assume Setup 3.1. If k ≥ d(L(H


![image 59](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile59.png>)

|Γ(H) − p(H)| ≤ (1 + c)e(Hsp) − 1 p(H).

The exact coeﬃcient of p(H) in the bound is not important. Any bound of the form O(c)p(H) suﬃces.

Dense edges play no role, so it suﬃces to consider the case when all edges of H are sparse. We prove Proposition 3.3 by iteratively applying the following inequality.

- Lemma 3.4. Let H be a graph with vertex set {1,... ,m}. Let Γ be a graph with vertex subsets X1,... ,Xm. Let ab ∈ E(H). Let H−ab denote H with the edge ab removed. Let H−a,−b denote H with all edges incident to a or b removed. Assume that Γ(Xa,Xb) is (p,γ |Xa||Xb|)-jumbled. Let f : V (Γ) × V (Γ) → [0,1] be any symmetric function. Then


![image 60](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile60.png>)

![image 61](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile61.png>)

(Γ(x,y) − p)f (H−ab | a → x,b → y) dxdy ≤ γ f(H−ab)f(H−a,−b).

- x∈Xa
- y∈Xb


Proof. Let Ha,−ab denote the edges of H−ab incident to a, and let Hb,−ab be the edges of H−ab incident to b. Then H−ab = H−a,−b ⊎ Ha,−ab ⊎ Hb,−ab, as a disjoint union of edges. In the following calculation, z varies uniformly over compatible maps V (H) \ {a,b} → V (Γ), x varies uniformly over Xa, and y varies uniformly over Xb. The three inequalities that appear in the calculation follow from, in order, the triangle inequality, the jumbledness condition, and the Cauchy-Schwarz inequality.

(Γ(x,y) − p)f (H−ab | a → x,b → y) dxdy

x,y

=

f (H−a,−b | z)

z

(Γ(x,y) − p)f (Ha,−ab | a → x,z) f (Hb,−ab | b → y,z) dxdydz

x,y

≤

f (H−a,−b | z)

z

(Γ(x,y) − p)f (Ha,−ab | a → x,z) f (Hb,−ab | b → y,z) dxdy dz

x,y

![image 62](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile62.png>)

![image 63](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile63.png>)

≤

f (H−a,−b | z) γ

z

f (Ha,−ab | a → x,z) dx

x

f (Hb,−ab | b → y,z) dydz

y

= γ

![image 64](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile64.png>)

![image 65](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile65.png>)

f (H−a,−b | z) f (Ha,−ab | z) f (Hb,−ab | z)dz

z

![image 66](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile66.png>)

![image 67](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile67.png>)

≤ γ

f (H−a,−b | z) dz

z

![image 68](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile68.png>)

= γ f(H−a,−b)f(H−ab).

f (H−a,−b | z) f (Ha,−ab | z) f (Hb,−ab | z) dz

z

![image 69](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile69.png>)

![image 70](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile70.png>)

![image 71](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile71.png>)

![image 72](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile72.png>)

- Proof of Proposition 3.3. As remarked after the statement of the proposition, it suﬃces to prove the result in the case when all edges of H are sparse. We induct on the number of edges of H. If H has no


edges, then Γ(H) = p(H) = 1. So assume that H has at least one edge. Since k ≥ 21(d(L(H)) + 2), we can ﬁnd an edge ab of H such that degH(a) + degH(b) ≤ d(L(H)) + 2 ≤ 2k. Let H−ab and H−a,−b be as in Lemma 3.4. Since L(H) is (2k − 2)-degenerate, the line graph of any subgraph of H is also (2k − 2)-degenerate. By the induction hypothesis, we have |Γ(H−ab) − p(H−ab)| ≤ ((1 + c)e(H)−1 − 1)p(H−ab) and |Γ(H−a,−b) − p(H−a,−b)| ≤ ((1 + c)e(H)−1 − 1)p(H−a,−b). We have

![image 73](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile73.png>)

Γ(H) − p(H) = p · (Γ(H−ab) − p(H−ab)) + x∈X

a y∈Xb

(Γ(x,y) − p)Γ(H−ab | a → x,b → y) dxdy.

The ﬁrst term on the right is bounded in absolute value by ((1+c)e(H)−1 −1)p(H). For the second term, by Lemma 3.4 and the induction hypothesis, we have

![image 74](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile74.png>)

(Γ(x,y) − p)Γ(H−ab | a → x,b → y) dxdy ≤ cpk Γ(H−ab)Γ(H−a,−b)

x,y

(6)

![image 75](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile75.png>)

≤ cpk(1 + c)e(H)−1 p(H−ab)p(H−a,−b) ≤ c(1 + c)e(H)−1p(H).

The last inequality is where we used 2k ≥ degH(a) + degH(b). Combining the two estimates gives the desired result.

![image 76](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile76.png>)

![image 77](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile77.png>)

![image 78](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile78.png>)

![image 79](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile79.png>)

- 3.4 Counting partial embeddings into Γ As outlined in Section 2, we need to count embeddings of H where some edges are embedded into


- G (the straight edges in the ﬁgures) and some edges are embedded into Γ (the wavy edges). We prove counting estimates for these embeddings here. The main result of this section is summarized in the ﬁgure below. The proofs are almost identical to that of Proposition 3.3. We just need to be a little more careful with the exponents on the jumbledness parameter.


# ⇐

First we consider the case where exactly one edge needs to be embedded into Γ and the other edges are embedded into some subgraph of Γ. To state the result requires a little notation. Suppose that H = H′ ∪ H′′ is an edge disjoint partition of the graph H into two subgraphs H′ and H′′. We deﬁne d(L(H′,H′′)) to be the smallest d such there is an ordering of the edges of H with the edges of H′ occurring before the edges of H′′ such that every edge e has at most d neighbors, that is, edges containing either of the endpoints of e, which appear earlier in the ordering.

- Lemma 3.5. Assume Setup 3.1. Let ab ∈ E(H) and H−ab be the graph H with edge ab removed.

Assume k ≥ d(L(H

sp −ab,absp))+2

![image 80](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile80.png>)

2 . Let G be any weighted subgraph of Γ (i.e., 0 ≤ G ≤ Γ as functions). Let g denote the function that agrees with Γ on Xa × Xb and with G everywhere else. Then

|g(H) − pabG(H−ab)| ≤ c(1 + c)e(Hsp)−1p(H).

The lemma follows from essentially the same calculation as (6), except that we take ab as our ﬁrst edge to remove (this is why there is a stronger requirement on k) and then use G ≤ Γ.

Iterating the lemma, we obtain the following result where multiple edges need to be embedded into Γ. It can be proved by iterating Lemma 3.5 or mimicking the proof of Proposition 3.3.

- Lemma 3.6. Assume Setup 3.1. Let H′ be a subgraph of H. Assume k ≥ d(L(H

′sp,(H\H′)sp))+2

![image 81](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile81.png>)

2 .

- Let G be a weighted subgraph of Γ. Let g be a function that agrees with Γ on Xa × Xb when ab ∈ E(H \ H′) and with G otherwise. Then


g(H) − p(H \ H′)G(H′) ≤ (1 + c)e(Hsp) − 1 p(H).

3.5 Exceptional sets

This section contains a couple of lemmas about Γ that we will need later on. The reader may choose to skip this section until the results are needed.

We begin with a standard estimate for the number of vertices in a jumbled graph whose degrees deviate from the expected value. The proof follows immediately from the deﬁnition of jumbledness.

- Lemma 3.7. Let Γ be a (p,γ |X||Y |)-jumbled graph between vertex subsets X and Y . Let v: Y → [0,1] and let ξ > 0. If

![image 82](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile82.png>)

U ⊆ x ∈ X

y∈Y

Γ(x,y)v(y) dy ≥ (1 + ξ)pEv

or

U ⊆ x ∈ X

y∈Y

Γ(x,y)v(y) dy ≤ (1 − ξ)pEv , then

|U| |X|

![image 83](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile83.png>)

≤

γ2 ξ2p2Ev

![image 84](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile84.png>)

.

The next lemma says that restrictions of the count Γ(H) to small sets of vertices or pairs of vertices yield small counts. This will be used in Section 4.2 to bound the contributions from exceptional sets.

- Lemma 3.8. Assume Setup 3.1 with k ≥ d(L(H


sp))+2 2 . Let x: V (H) → V (Γ) vary uniformly over

![image 85](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile85.png>)

compatible maps. Let u: V (Γ) → [0,1] be any function and write u(x) = a∈V (H) u(xa). Let E′ be

a weighted graph with the same vertices as Γ whose edge set is supported on Xa ×Xb for ab ∈/ Hsp.

- Let H′ be any graph with the same vertices as H. Then


Γ(H | x)u(x)E′ H′ x dx ≤ (1 + c)e(Hsp) − 1 +

x

u(x)E′ H′ x dx p(H).

x

Lemma 3.8 follows by showing that

(Γ(H | x) − p(H)) u(x)E′ H′ x dx ≤ (1 + c)e(Hsp) − 1 p(H).

x

The proof is similar to that of Proposition 3.3. In the step analogous to (6), after applying the jumbledness condition as our ﬁrst inequality, we bound u and E′ by 1 and then continue exactly the same way.

## 4 Counting in G

In this section we develop the counting lemma for subgraphs G of Γ, as outlined in Section 2. The two key ingredients are doubling and densiﬁcation, which are discussed in Sections 4.1 and 4.2, respectively. Here is the common setup for this section.

- Setup 4.1. Assume Setup 3.1. Let ǫ > 0. Let G be a weighted subgraph of Γ. For every edge ab ∈ E(H), assume that (Xa,Xb)G satisﬁes DISC(qab,pab,ǫ), where 0 ≤ qab ≤ pab.


Unlike in Section 3, we do not make an eﬀort to keep track of the unimportant coeﬃcients of p(H) in the error bounds, as it would be cumbersome to do so. Instead, we use the ≈ notation introduced in Section 3.2.

The goal of this section is to prove the following counting lemma. This is slightly more general than Theorem 1.12 in that it allows H to have both sparse and dense edges. Proposition 4.2. Assume Setup 4.1 with k ≥ min ∆(L(H

sp))+6 2 . Then

sp))+4

2 , d(L(H

![image 86](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile86.png>)

![image 87](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile87.png>)

G(H)p(≈H)

q(H).

c,ǫ

The requirement on k stated in Proposition 4.2 is not necessarily best possible. The proof of the counting lemma will be by induction on the vertices of H, removing one vertex at a time. A better bound on k can sometimes be obtained by tracking the requirements on k at each step of the procedure, as explained in a tutorial in Section 4.5.

### 4.1 Doubling

Doubling is a technique used to reduce the problem of counting embeddings of H in G to the problem of counting embeddings of H with one vertex deleted.

If a ∈ V (H), Ha×2 is the graph H with vertex a doubled. In the assignment of vertices of Ha×2 to vertex subsets of Γ, the new vertex a′ is assigned to the same vertex subset as a. Let Ha be the subgraph of H consisting of edges with a as an endpoint, and let Ha,a×2 be Ha with a doubled. Let H−a be the subgraph of H consisting of edges not having a as an endpoint. We refer to Figure 1 for an illustration.

- Lemma 4.3 (Doubling). Let H be a graph with vertex set {1,... ,m}. Let Γ be a weighted graph with vertex subsets X1,... ,Xm, and let G be a weighted subgraph of Γ. For each edge bc of H, we have numbers 0 ≤ qbc ≤ pbc ≤ 1. Let g be a function that agrees with G on Xi × Xj whenever


- a ∈ {i,j} and with Γ on Xi × Xj whenever a ∈/ {i,j}. Then |G(H) − q(H)|

≤ q(Ha)|G(H−a) − q(H−a)| + G(H−a)1/2 g(Ha×2) − 2q(Ha)g(H) + q(Ha)2Γ(H−a) 1/2 . (7) Proof. Let y vary uniformly over compatible maps V (H) \ {a} → V (G) where y(b) ∈ Xb for each

- b ∈ V (H) \ {a}. We have


G(H) − q(H) = q(Ha)(G(H−a) − q(H−a)) +

(G(Ha | y) − q(Ha)) G(H−a | y) dy.

y

It remains to bound the integral, which we can do using the Cauchy-Schwarz inequality.

(G(Ha | y) − q(Ha)) G(H−a | y) dy

y

2

≤

G(H−a | y) dy

y

(G(Ha | y) − q(Ha))2 G(H−a | y) dy

y

= G(H−a)

(G(Ha | y) − q(Ha))2 G(H−a | y) dy

y

(G(Ha | y) − q(Ha))2 Γ(H−a | y) dy

≤ G(H−a)

y

= G(H−a) g(Ha×2) − 2q(Ha)g(H) + q(Ha)2Γ(H−a) .

![image 88](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile88.png>)

![image 89](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile89.png>)

![image 90](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile90.png>)

![image 91](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile91.png>)

Using Lemma 3.6, we know that under appropriate hypotheses, we have

g(Ha×2) p(H≈a×2)

p(H−a)G(Ha,a×2), g(H) p(≈H)

c

p(H−a)G(Ha)

c

and Γ(H−a) p(H≈−a)

p(H−a). If we can show that

c

p(Ha,a×2)

≈

G(Ha,a×2)

q(Ha,a×2)

c,ǫ

and G(Ha)p(≈Ha)

q(Ha),

c,ǫ

then the rightmost term in (7) is ≈pc,ǫ(H) 0, which would reduce the problem to showing that G(H−a)≈pc,ǫ(H−a) q(H−a). This reduction step is spelled out below. See Figure 5 for an illustration.

a

G(H)

# ⇑

G(H−a) G(Ha,a×2) G(Ha) Figure 5: The doubling reduction.

sp a,a×2,H−spa))+2

- Lemma 4.4. Assume Setup 4.1. Let a ∈ V (H). Suppose that k ≥ d(L(H


2 . Suppose that G(H−a)p(H≈−a)

![image 92](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile92.png>)

p(Ha,a×2)

q(H−a), G(Ha)p(≈Ha)

≈

q(Ha,a×2). Then

q(Ha) and G(Ha,a×2)

c,ǫ

c,ǫ

c,ǫ

G(H)p(≈H)

q(H).

c,ǫ

Remark. We do not always need the full strength of Setup 4.1 (although it is convenient to state it as such). For example, when H is a triangle with vertices {1,2,3}, H−1 is a single edge, so we do not need discrepancy on (X2,X3)G to obtain G(H−a)≈pc,ǫ q23. In particular, our approach gives the triangle counting lemma in the form stated in Kohayakawa et al. [59], where discrepancy is assumed for only two of the three pairs of vertex subsets of G.

### 4.2 Densiﬁcation

Densiﬁcation is the technique that allows us to transform a subdivided edge of H into a single dense edge, as summarized in the ﬁgure below. This section also contains a counting lemma for trees (Proposition 4.9).

# ⇐

We introduce the following notation for the density analogues of degree and codegree. If Γ (and similarly G) is a weighted graph with vertex subsets X,Y,Z, then for x ∈ X and z ∈ Z, we write

G(x,Y ) =

G(x,y) dy,

y∈Y

G(x,y)G(y,z) dz. Now we state the goal of this section.

and G(x,Y,z) =

y∈Y

sp))+2 2 . Let 1,2,3 be vertices in H

- Lemma 4.5 (Densiﬁcation). Assume Setup 4.1 with k ≥ d(L(H


![image 93](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile93.png>)

such that 1 and 3 are the only neighbors of 2 in H, and 13 ∈/ E(H). Replace the induced bipartite graph (X1,X3)G by the weighted bipartite graph deﬁned by

1 2p12p23

min {G(x1,X2,x3),2p12p23}.

G(x1,x3) =

![image 94](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile94.png>)

Let H′ denote the graph obtained from H by deleting edges 12 and 23 and adding edge 13. Let q13 = 2qp12q23

12p23 and p13 = 1. Then (X1,X3)G satisﬁes DISC(q13,1,2ǫ + 18c) and G(H) − 2p12p23G(H′) ≤ ((1 + c)e(Hsp) − 1 + 26c2)p(H).

![image 95](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile95.png>)

Note that q(H) = 2p12p23q(H′). So we obtain the following reduction step as a corollary. Corollary 4.6. Continuing with Lemma 4.5. If G(H′)≈p(H

′)

c,ǫ q(H′) then G(H)≈pc,ǫ(H) q(H) in the original graph.

The proof of Lemma 4.5 consists of the following steps:

- 1. Show that the weighted graph on X1 × X3 with weights G(x1,X2,x3) satisﬁes discrepancy.
- 2. Show that the capping of weights has negligible eﬀect on discrepancy.
- 3. Show that the capping of weights has negligible eﬀect on the H-count.


Steps 2 and 3 are done by bounding the contribution from pairs of vertices in X1 × X3 which have too high co-degree with X2 in Γ.

We shall focus on the more diﬃcult case when both edges 12 and 23 are sparse. The case when

- at least one of the two edges is dense is analogous and much easier. Let us start with a warm-up by showing how to do step 1 for the latter dense case. We shall omit the rest of the details in this case.


- Lemma 4.7. Let 0 ≤ q1 ≤ p1 ≤ 1, 0 ≤ q2 ≤ 1, ǫ > 0. Let G be a weighted graph with vertex subsets X,Y,Z, such that (X,Y )G satisﬁes DISC(q1,p1,ǫ) and (Y,Z)G satisﬁes DISC(q2,1,ǫ). Then the graph G′ on (X,Z) deﬁned by G′(x,z) = G(x,Y,z) satisﬁes DISC(q1q2,p1,2ǫ).

Proof. Let u: X → [0,1] and w: Z → [0,1] be arbitrary functions. In the following integrals, let x,y and z vary uniformly over X,Y and Z, respectively. We have

x,z

u(x)(G(x,Y,z) − q1q2)w(z) dxdz

=

x,y,z

u(x)(G(x,y)G(y,z) − q1q2)w(z) dxdydz

=

x,y,z

u(x)(G(x,y) − q1)G(y,z)w(z) dxdydz + q1

x,y,z

u(x)(G(y,z) − q2)w(z) dxdydz. (8)

Each of the two integrals in the last sum is bounded by ǫp1 in absolute value by the discrepancy hypotheses. Therefore (X,Z)G′ satisﬁes DISC(q1q2,p1,2ǫ).

![image 96](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile96.png>)

![image 97](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile97.png>)

![image 98](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile98.png>)

![image 99](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile99.png>)

The next lemma is step 1 for the sparse case.

- Lemma 4.8. Let c,p,ǫ ∈ (0,1] and q1,q2 ∈ [0,p]. Let Γ be a graph with vertex subsets X,Y,Z,


- and G a weighted subgraph of G. Suppose that


- • (X,Y )Γ is (p,cp3/2 |X| |Y |)-jumbled and (X,Y )G satisﬁes DISC(q1,p,ǫ); and

![image 100](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile100.png>)

- • (Y,Z)Γ is (p,cp3/2 |Y ||Z|)-jumbled and (Y,Z)G satisﬁes DISC(q2,p,ǫ).


![image 101](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile101.png>)

Then the graph G′ on (X,Z) deﬁned by G′(x,z) = G(x,Y,z) satisﬁes DISC(q1q2,p2,3ǫ + 6c). Remark. By unraveling the proof of Lemma 3.8, we see that the exponent of p in the jumbledness of (X,Y )Γ can be relaxed from 23 to 1. Proof. We begin the proof the same way as Lemma 4.7. In (8), the second integral is bounded in absolute value by ǫp2. We need to do more work to bound the ﬁrst integral.

![image 102](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile102.png>)

Deﬁne v: Y → [0,1] by

G(y,z)w(z) dz. So the ﬁrst integral in (8), the quantity we need to bound, equals

v(y) =

z

u(x)(G(x,y) − q1)v(y) dxdy. (9)

x,y

If we apply discrepancy immediately, we get a bound of ǫp, which is not small enough, as we need a bound on the order of o(p2). The key observation is that v(y) is bounded above by 2p on most of Y . Indeed, let

Y ′ = {y ∈ Y | Γ(y,Z) > 2p}.

By Lemma 3.7 we have |Y ′| ≤ c2p|Y |. Since v1Y \Y ′ is bounded above by 2p, we can apply discrepancy on (X,Y )G with the functions u and 21pv1Y \Y ′ to obtain

![image 103](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile103.png>)

u(x)(G(x,y) − q1)v(y)1Y \Y ′ dxdy ≤ 2ǫp2.

x,y

In the following calculation, the ﬁrst inequality follows from the triangle inequality; the second inequality follows from expanding v(y) and using G ≤ Γ and u,w ≤ 1; the third inequality follows from Lemma 3.8 (applied with u in the Lemma being the function 1Y ′ on Y and 1 everywhere else,

- and H′ the empty graph so that E′ (H′ | x) = 1 always).


u(x)(G(x,y) − q1)v(y)1Y ′(y) dxdy

x,y

≤

u(x)G(x,y)v(y)1Y ′ dxdy +

x,y

u(x)q1v(y)1Y ′(y) dxdy

x,y

≤

Γ(x,y)1Y ′(y)Γ(y,z) dxdydz + q1

1Y ′(y)Γ(y,z) dydz

x,y,z

y,z

p2 + q1 (1 + c) − 1 + |Y ′| |Y |

≤ (1 + c)2 − 1 + |Y ′| |Y |

p ≤ 6cp2.

![image 104](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile104.png>)

![image 105](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile105.png>)

Therefore, (9) is at most (2ǫ + 6c)p2 in absolute value. Recall that the second integral in (8) was bounded by ǫp2. The result follows from combining these two estimates.

![image 106](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile106.png>)

![image 107](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile107.png>)

![image 108](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile108.png>)

![image 109](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile109.png>)

The technique used in Lemma 4.8 also allows us to count trees in G.

sp)+1 2 . Then

- Proposition 4.9. Assume Setup 4.1 with H a tree and k ≥ ∆(H


![image 110](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile110.png>)

G(H)p(≈H)

q(H).

c,ǫ

In fact, it can be shown that the error has the form

|G(H) − q(H)| ≤ MH(c + ǫ)p(H) for some real number MH > 0 depending on H.

To prove Proposition 4.9, we formulate a weighted version and induct on the number of edges. The weighted version is stated below.

- Lemma 4.10. Assume the same setup as in Proposition 4.9. Let u: V (G) → [0,1] be any function. Let x vary uniformly over all compatible maps V (H) → V (G). Write u(x) = a∈V (H) u(xa). Then,

x

G(H | x)u(x) dxp(≈H)

c,ǫ

q(H)

x

u(x) dx.

To prove Lemma 4.10, we remove one leaf of H at a time and use the technique in the proof of

- Lemma 4.8 to transfer the weight of the leaf to its unique neighboring vertex and use Lemma 3.8 to bound the contributions of the vertices with large degrees in Γ. We omit the details.


Continuing with the proof of densiﬁcation, the following estimate is needed for steps 2 and 3.

- Lemma 4.11. Let Γ be a graph with vertex subsets X,Y,Z, such that (X,Y )Γ is (p,cp |X| |Y |)jumbled and (Y,Z)Γ is (p,cp3/2 |Y | |Z|)-jumbled. Let

![image 111](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile111.png>)

![image 112](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile112.png>)

E′ = (x,z) ∈ X × Z Γ(x,Y,z) > 2p2 .

Then |E′| ≤ 26c2 |X| |Z|. Proof. Let

X′ = x ∈ X |Γ(x,Y ) − p| >

p 2

![image 113](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile113.png>)

. Then, by Lemma 3.7, |X′| ≤ 8c2 |X|. For every x ∈ X, let

Zx′ = z ∈ Z Γ(x,Y,z) > 2p2 .

For x ∈ X \ X′, we have, again by Lemma 3.7, that |Zx′ | ≤ 18c2 |Z|. The result follows by noting that E′ ⊆ (X′ × Z) ∪ {(x,z) | x ∈ X \ X′,z ∈ Zx′ }.

![image 114](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile114.png>)

![image 115](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile115.png>)

![image 116](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile116.png>)

![image 117](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile117.png>)

The following lemma is step 2 in the program.

- Lemma 4.12. Let c,ǫ,p ∈ (0,1] and q1,q2 ∈ [0,p]. Let Γ be a graph with vertex subsets X,Y,Z, and G a weighted subgraph of Γ. Suppose that


- • (X,Y )Γ is (p,cp |X| |Y |)-jumbled and (X,Y )G satisﬁes DISC(q1,p,ǫ); and

![image 118](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile118.png>)

- • (Y,Z)Γ is (p,cp3/2 |Y ||Z|)-jumbled and (Y,Z)G satisﬁes DISC(q2,p,ǫ).


![image 119](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile119.png>)

Then the graph G′ on (X,Z) deﬁned by G′(x,z) = min G(x,Y,z),2p2 satisﬁes DISC(q1q2,p2,3ǫ+ 35c).

Proof. Let u: X → [0,1] and w: Z → [0,1] be any functions. In the following integrals, x,y and z vary uniformly over X,Y and Z, respectively. We have

(G′(x,z) − q1q2)u(x)w(z) dxdz

x,z

=

(G(x,Y,z) − q1q2)u(x)w(z) dxdz −

x,z

(G(x,Y,z) − G′(x,z))u(x)w(z) dxdz.

x,z

The ﬁrst integral on the right-hand side can be bounded in absolute value by (3ǫ + 6c)p2 by

- Lemma 4.8. For the second integral, let E′ = (x,z) ∈ X × Z Γ(x,Y,z) > 2p2 . We have


0 ≤

(G(x,Y,z) − G′(x,z))u(x)w(z) dxdz

x,z

≤

G(x,Y,z)1E′(x,z) dxdz

x,z

≤

Γ(x,y)Γ(y,z)1E′(y,z) dxdz

x,y,z

≤ (1 + c)2 − 1 + |E′| |X| |Z|

p2 ≤ 29cp2

![image 120](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile120.png>)

by Lemmas 3.8 and 4.11. The result follows by combining the estimates. Finally we prove step 3 in the program, thereby completing the proof of densiﬁcation.

![image 121](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile121.png>)

![image 122](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile122.png>)

![image 123](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile123.png>)

![image 124](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile124.png>)

Proof of Lemma 4.5. We prove the result when both edges 12 and 23 are sparse. When at least one of 12 and 23 is dense, the proof is analogous and easier.

Lemma 4.12 implies that (X1,X3)G satisﬁes DISC(q13, 12,3ǫ+35c), and hence it must also satisfy DISC(q13,1,2ǫ + 18c).

![image 125](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile125.png>)

Let E′ = {(x1,x3) | Γ(x1,X2,x3) > 2p12p23}. We have |E′| ≤ 26c2 |X1||X3| by Lemma 4.11. In the following integrals, let x: V (H) → V (Γ) vary uniformly over all compatible maps. Then

0 ≤ G(H) − 2p12p23G(H′) ≤

Γ(H | x) 1E′(x1,x2) dx ≤ ((1 + c)e(Hsp) − 1 + 26c2)p(H)

x

by Lemma 3.8.

![image 126](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile126.png>)

![image 127](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile127.png>)

![image 128](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile128.png>)

![image 129](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile129.png>)

### 4.3 Counting C4

With the tools of doubling and densiﬁcation, we are now ready to count embeddings in G. We start by showing how to count C4, as it is an important yet tricky step.

- Proposition 4.13. Assume Setup 4.1 with H = C4 and k ≥ 2. Then |G(C4) − q(C4)| ≤ 100(c + ǫ)1/2p(C4).


The constant 100 is unimportant. It can be obtained by unraveling the calculations. We omit the details.

Proposition 4.13 follows from repeated applications of doubling (Lemma 4.4) and densiﬁcation (Corollary 4.6). The chain of implications is summarized in Figure 6 in the case when all four

⇑

⇑

⇑

Figure 6: The proof that G(C4)≈pc,ǫ4 q(C4). The vertical arrows correspond to densiﬁcation, doubling the top vertex and densiﬁcation, respectively.

edges of C4 are sparse (the other cases are easier). In the ﬁgure, each graph represents a claim of the form G(H)≈pc,ǫ(H) q(H). The sparse and dense edges are distinguished by thickness. The claim for the dense triangle follows from the counting lemma for dense graphs (Proposition 1.8) and the claim for the rightmost graph follows from Lemma 4.7.

### 4.4 Finishing the proof of the counting lemma

Given a graph H, we can use the doubling lemma, Lemma 4.4, to reduce the problem of counting

- H in G to the problem of counting H−a in G, where H−a is H with some vertex a deleted, provided we can also count Ha and Ha,a×2. Suppose a has degree t in H and degree t′ in Hsp. The graph Ha is isomorphic to some K1,t. Since K1,t is a tree, we can count copies using Proposition 4.9,


provided that the exponent of p in the jumbledness of Γ satisﬁes k ≥ t′+12 . The following lemma shows that we can count embeddings of Ha,a×2 as well.

![image 130](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile130.png>)

- Lemma 4.14. Assume Setup 4.1 where H = K2,t with vertices {a1,a2;b1,... ,bt}. Assume that the edges aibj are sparse for 1 ≤ j ≤ t′ and dense for j > t′. If k ≥ t′+22 , then


![image 131](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile131.png>)

G(H)p(≈H)

q(H).

c,ǫ

Proof. When t′ = 0, all edges of H are dense, so the result follows from the dense counting lemma. So assume t′ ≥ 1. First we apply densiﬁcation as follows:

# ⇐

When t′ = 1, we get a dense graph so we are done. Otherwise, the result follows by induction using doubling as shown below, where we use Propositions 4.13 and 4.9 to count C4 and K1,2, respectively.

# ⇑

![image 132](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile132.png>)

![image 133](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile133.png>)

![image 134](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile134.png>)

![image 135](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile135.png>)

Once we can count Ha and Ha,a×2, we obtain the following reduction result via doubling.

sp a,a×2,H−spa))+2

- Lemma 4.15. Assume Setup 4.1. Let a be a vertex of H. If k ≥ d(L(H


2 , then

![image 136](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile136.png>)

G(H)p(≈H)

q(Ha)G(H−a).

c,ǫ

The proof of the counting lemma follows once we keep track of the requirements on k.

- Proof of Proposition 4.2. When H has no sparse edges, the result follows from the dense counting lemma (Proposition 1.8). Otherwise, using Lemma 4.15, it remains to show that if k ≥


sp a,a×2,H−spa))+2

sp))+6 2 , then there exists some vertex a of H satisfying k ≥ d(L(H

sp))+4

2 , d(L(H

min ∆(L(H

2 .

![image 137](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile137.png>)

![image 138](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile138.png>)

![image 139](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile139.png>)

Actually, the hypothesis on k is strong enough that any a will do. Indeed, we have ∆(L(Hsp))+2 ≥ ∆(L(Hasp×2)) ≥ d(L(Ha,asp ×2,H−spa)) since doubling a increases the degree of every vertex by at most 1. We also have d(L(Hsp)) ≥ d(L(Ha,asp ×2,H−spa)) − 4 since every edge in H−spa shares an endpoint with at most 4 edges in Ha,asp ×2.

![image 140](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile140.png>)

![image 141](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile141.png>)

![image 142](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile142.png>)

![image 143](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile143.png>)

### 4.5 Tutorial: determining jumbledness requirements

The jumbledness requirements stated in our counting lemmas are often not the best that come out of our proofs. We had to make a tradeoﬀ between strength and simplicity while formulating the results. In this section, we give a short tutorial on ﬁnding the jumbledness requirements needed for our counting lemma to work for any particular graph H. These ﬁne-tuned bounds can be extracted from a careful examination of our proofs, with no new ideas introduced in this section.

We work in a more general setting where we allow non-balanced jumbledness conditions between vertex subsets of Γ. This will arise naturallly in Section 6 when we prove a one-sided counting lemma.

Setup 4.16. Let Γ be a graph with vertex subsets X1,... ,Xm. Let p,c ∈ (0,1]. Let H be a graph with vertex set {1,... ,m}, with vertex a assigned to Xa. For every edge ab in H, one of the following two holds:

- • (Xa,Xb)Γ is (p,cpkab |Xa||Xb|)-jumbled for some kab ≥ 1, in which case we set pab = p and say that ab is a sparse edge, or

![image 144](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile144.png>)

- • (Xa,Xb)Γ is a complete bipartite graph, in which case we set pab = 1 and say that ab is a dense edge.


Let Hsp denote the subgraph of H consisting of sparse edges.

Let ǫ > 0. Let G be a weighted subgraph of Γ. For every edge ab ∈ E(H), assume that (Xa,Xb)G satisﬁes DISC(qab,pab,ǫ), where 0 ≤ qab ≤ pab.

In the ﬁgures in this section, we label the edges by the lower bounds on kab that are suﬃcient for the two-sided counting lemma to hold. For instance, the ﬁgure below shows the jumbledness conditions that are suﬃcient for the triangle counting lemma1, namely kab ≥ 3, kbc ≥ 2, kac ≥ 23.

![image 145](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile145.png>)

c

23 2

![image 146](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile146.png>)

a b

3

Although we are primarily interested in embeddings of H into G, we need to consider partial embeddings where some of the edges of H are allowed to embed into Γ. So we encounter three types of edges of H, summarized in Table 2. (Note that for dense edges ab, (Xa,Xb)Γ is a complete bipartite graph, so such embeddings are trivial and ab can be ignored.)

Table 2: Types of edges in H.

![image 147](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile147.png>)

Figure Name Description κ Jumbled edge An edge to be embedded in (Xa,Xb)Γ with pab = p and kab ≥ κ.

![image 148](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile148.png>)

Dense edge An edge to be embedded in (Xa,Xb)G with pab = 1. κ Sparse edge An edge to be embedded in (Xa,Xb)G with pab = p and kab ≥ κ.

![image 149](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile149.png>)

Our counting lemma is proved through a number of reduction procedures. At each step, we transform H into one or more other graphs H′. At the end of the reduction procedure, we should arrive at a graph which only has dense edges. To determine the jumbledness conditions required to count some H, we perform these reduction steps and keep track of the requirements at each step. We explain how to do this for each reduction procedure.

Removing a jumbled edge. To remove a jumbled edge ab from H, we need kab to be at least the average of the sparse degrees (i.e., counting both sparse and jumbled edges) at the endpoints

of ab, i.e., kab ≥ 12(degHsp(a) + degHsp(b)). See Lemma 3.5. For example, kab ≥ 25 is suﬃcient to remove the edge ab in the graph below.

![image 150](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile150.png>)

![image 151](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile151.png>)

# ⇐

5 2

![image 152](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile152.png>)

a b

![image 153](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile153.png>)

1As mentioned in the remark after Lemma 4.4, we do not actually need DISC on (Xa, Xb)G, since edge density is enough. We do not dwell on this point in this section and instead focus on jumbledness requirements.

By removing jumbled edges one at a time, we can ﬁnd conditions that are suﬃcient for counting embeddings into Γ (Proposition 3.3). The following ﬁgure shows how this is done for a 4-cycle.

3/2 1

3/2

2

3/2

1 ⇐

⇐ 3/2

3/2

# 1 ⇐ 1

Doubling The ﬁgure below illustrates doubling. If the jumbledness hypotheses are suﬃcient to count the two graphs on the right, then they are suﬃcient to count the original graph. The ﬁrst graph is produced by deleting all edges with a as an endpoint, and the second graph is produced by doubling a and then, for all edges not adjacent to a, deleting the dense edges and converting sparse edges to jumbled ones.

a

# ⇐

Densiﬁcation To determine the jumbledness needed to perform densiﬁcation, delete all dense edges, transform all sparse edges into jumbled edges, and use the earlier method to determine the jumbledness required to count embeddings into Γ. For example, the jumbledness on the left ﬁgure below shows the requirements on C4 needed to perform the densiﬁcation step. It may be the case that even stronger hypotheses are needed to count the new graph (although for this example this is not the case).

3/2 1

# ⇐

3/2

2

Trees To determine the jumbledness needed to count some tree H, delete all dense edges in H and transform all sparse edges into jumbled edges and use the earlier method, removing one leaf at a time to determine the jumbledness required to count embeddings into Γ (Proposition 4.9).

- Example 4.17 (C4). Let us check that the labeling of C4 in the densiﬁcation paragraph gives sufﬁcient jumbledness to count C4. It remains to check that the jumbledness hypotheses are suﬃcient to count the triangle with a single edge. We can double the top vertex so that it remains to check the ﬁrst graph below (the other graph produced from doubling is a single edge, which is trivial to count). We can remove the jumbled edge, and then perform densiﬁcation to get a dense triangle, which we know how to count.

3 2

![image 154](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile154.png>)

3 2

![image 155](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile155.png>)

2

⇐ 3

![image 156](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile156.png>)

2

3

![image 157](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile157.png>)

2 ⇐

- Example 4.18 (K3). The following diagram illustrates the process of checking suﬃcient jumbledness hypotheses to count triangles (again, the ﬁrst graph resulting from doubling is a single edge


and is thus omitted from the ﬁgure). The suﬃciency for C4 follows from the previous example.

32 2

![image 158](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile158.png>)

3

# ⇐

32 32 2 2

![image 159](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile159.png>)

![image 160](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile160.png>)

3

# ⇐

32 32 2 2

![image 161](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile161.png>)

![image 162](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile162.png>)

- Example 4.19 (K2,t). The following diagram shows suﬃcient jumbledness to count K2,4. The same pattern holds for K2,t. The reduction procedure was given in the proof of Lemma 4.14. First we perform densiﬁcation to the two leftmost edges, and then apply doubling to the remaining middle vertices in order from left to right.

- 1

3

![image 163](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile163.png>)

- 2


3 2

![image 164](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile164.png>)

2 2

5 2

![image 165](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile165.png>)

5

![image 166](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile166.png>)

- 2

- 3


⇐

3 2

![image 167](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile167.png>)

2 2

5 2

![image 168](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile168.png>)

5

![image 169](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile169.png>)

- 2

- 3


⇐

2

5 2

![image 170](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile170.png>)

5

![image 171](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile171.png>)

- 2

- 3


⇐ 3

![image 172](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile172.png>)

2

- 2

- 3 2


![image 173](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile173.png>)

2

2

5 2

![image 174](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile174.png>)

5

![image 175](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile175.png>)

- 2

- 3


- Example 4.20 (K1,2,2). The following diagram shows suﬃcient jumbledness to count K1,2,2. This example will be used in the next section on inheriting regularity.


7

7 2

![image 176](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile176.png>)

![image 177](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile177.png>)

- 2

- 3

- 4


- 3 2


2 52

![image 178](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile178.png>)

3

![image 179](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile179.png>)

⇐

⇐

- 5 Inheriting regularity


Regularity is inherited on large subsets, in the sense that if (X,Y )G satisﬁes DISC(q,1,ǫ), then for any U ⊆ X and V ⊆ Y , the induced pair (U,V )G satisﬁes DISC(q,1,ǫ′) with ǫ′ = ||XU||||VY||ǫ. This is a trivial consequence of the deﬁnition of discrepancy, and the change in ǫ comes from rescaling

![image 180](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile180.png>)

the measures dx and dy after restricting the uniform distribution to a subset. The loss in ǫ is a constant factor as long as ||XU|| and ||YV || are bounded from below. So if G is a dense tripartite graph with vertex subsets X,Y,Z, with each pair being dense and regular, then we expect that for most vertices z ∈ Z, its neighborhoods NX(z) and NY (z) are large, and hence they induce regular pairs with only a constant factor loss in the discrepancy parameter ǫ.

![image 181](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile181.png>)

![image 182](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile182.png>)

The above argument does not hold in sparse pseudorandom graphs. It is still true that if (X,Y )G satisﬁes DISC(q,p,ǫ) then for any U ⊆ X and V ⊆ Y the induced pair (U,V )G satisﬁes DISC(q,1,ǫ′) with ǫ′ = ||XU||||VY||ǫ. However, in the tripartite setup from the previous paragraph, we expect most NX(z) to have size on the order of p|X|. So the naive approach shows that most z ∈ Z induce a bipartite graph satisfying DISC(q,p,ǫ′) where ǫ′ is on the order of pǫ2. This is undesirable, as we do not want ǫ to depend on p.

![image 183](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile183.png>)

![image 184](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile184.png>)

It turns out that for most z ∈ Z, the bipartite graph induced by the neighborhoods satisﬁes DISC(q,p,ǫ′) for some ǫ′ depending on ǫ but not p. In this section we prove this fact using the counting lemma developed earlier in the paper. We recall the statement from the introduction.

Proposition 1.13 For any α > 0, ξ > 0 and ǫ′ > 0, there exists c > 0 and ǫ > 0 of size at least polynomial in α,ξ,ǫ′ such that the following holds.

Let p ∈ (0,1] and qXY ,qXZ,qYZ ∈ [αp,p]. Let Γ be a tripartite graph with vertex subsets X, Y and Z and G be a subgraph of Γ. Suppose that

- • (X,Y )Γ is (p,cp4 |X| |Y |)-jumbled and (X,Y )G satisﬁes DISC(qXY ,p,ǫ); and

![image 185](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile185.png>)

- • (X,Z)Γ is (p,cp2 |X| |Z|)-jumbled and (X,Z)G satisﬁes DISC(qXZ,p,ǫ); and

![image 186](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile186.png>)

- • (Y,Z)Γ is (p,cp3 |Y | |Z|)-jumbled and (Y,Z)G satisﬁes DISC(qY Z,p,ǫ).


![image 187](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile187.png>)

Then at least (1−ξ)|Z| vertices z ∈ Z have the property that |NX(z)| ≥ (1−ξ)qXZ |X|, |NY (z)| ≥ (1 − ξ)qYZ |Y |, and (NX(z),NY (z))G satisﬁes DISC(qXY ,p,ǫ′).

The idea of the proof is to ﬁrst show that a bound on the K2,2 count implies DISC and then to use the K1,2,2 count to bound the K2,2 count between neighborhoods.

We also state a version where only one side gets smaller. While the previous proposition is suﬃcient for embedding cliques, this second version will be needed for embedding general graphs H.

- Proposition 5.1. For any α > 0, ξ > 0 and ǫ′ > 0, there exists c > 0 and ǫ > 0 of size at least polynomial in α,ξ,ǫ′ such that the following holds.


Let p ∈ (0,1] and qXY ,qXZ ∈ [αp,p]. Let Γ be a tripartite graph with vertex subsets X, Y and Z and G be a subgraph of Γ. Suppose that

- • (X,Y )Γ is (p,cp5/2 |X| |Y |)-jumbled and (X,Y )G satisﬁes DISC(qXY ,p,ǫ); and

![image 188](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile188.png>)

- • (X,Z)Γ is (p,cp3/2 |X| |Z|)-jumbled and (X,Z)G satisﬁes DISC(qXZ,p,ǫ).


![image 189](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile189.png>)

Then at least (1 − ξ)|Z| vertices z ∈ Z have the property that |NX(z)| ≥ (1 − ξ)qXZ |X| and (NX(z),Y )G satisﬁes DISC(qXY ,p,ǫ′).

### 5.1 C4 implies DISC

From our counting lemma we already know that if G is a subgraph of a suﬃciently jumbled graph with vertex subsets X and Y such that (X,Y )G satisﬁes DISC(q,p,ǫ), then the number of K2,2 in

G across X and Y is roughly q4 |X|2 |Y |2. In this section, we show that the converse is true, that the K2,2 count implies discrepancy, even without any jumbledness hypotheses.

In what follows, for any function f : X × Y → R, we write

t

s

f(xi,yj) dx1 ··· dxsdy1 ··· dyt.

f(Ks,t) = x

1,...,xs∈X y1,...,yt∈Y

j=1

i=1

The following lemma shows that a bound on the “de-meaned” C4-count implies discrepancy.

- Lemma 5.2. Let G be a bipartite graph between vertex sets X and Y . Let 0 ≤ q ≤ p ≤ 1 and


ǫ > 0. Deﬁne f : X × Y → R by f(x,y) = G(x,y) − q. If f(K2,2) ≤ ǫ4p4 then (X,Y )G satisﬁes DISC(q,p,ǫ).

- Proof. Let u: X → [0,1] and v: Y → [0,1] be any functions. Applying the Cauchy-Schwarz inequality twice, we have


f(x,y)u(x)v(y) dydx

x∈X y∈Y

4

≤

=

≤

=

≤

=

≤

2

2

dx

f(x,y)u(x)v(y) dy

x∈X y∈Y

2

2

u(x)2

dx

f(x,y)v(y) dy

y∈Y

x∈X

2

2

dx

f(x,y)v(y) dy

x∈X y∈Y

2

f(x,y)f(x,y′)v(y)v(y′) dydy′dx

x∈X y,y′∈Y

2

dydy′

f(x,y)f(x,y′)v(y)v(y′) dx

y,y′∈Y x∈X

2

dydy′

v(y)2v(y′)2

f(x,y)f(x,y′) dx

y,y′∈Y

x∈X

2

dydy′

f(x,y)f(x,y′) dx

y,y′∈Y x∈X

Thus

f(x,y)f(x,y′)f(x′,y)f(x′,y′) dxdx′dydy′

=

y,y′∈Y x,x′∈X

= f(K2,2) ≤ ǫ4p4.

(G(x,y) − q)u(x)v(y) dydx ≤ ǫp.

x∈X y∈Y

Hence (X,Y )G satisﬁes DISC(q,p,ǫ).

![image 190](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile190.png>)

![image 191](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile191.png>)

![image 192](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile192.png>)

![image 193](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile193.png>)

- Lemma 5.3. Let G be a bipartite graph between vertex sets X and Y . Let 0 ≤ q ≤ p ≤ 1


and ǫ > 0. Let U ⊆ X and V ⊆ Y . Let µ = ||XU|| and ν = ||VY||. Deﬁne f : X × Y → R by f(x,y) = (G(x,y) − q)1U(x)1V (y). If f(K2,2) ≤ ǫ4p4µ2ν2, then (U,V )G satisﬁes DISC(q,p,ǫ).

![image 194](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile194.png>)

![image 195](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile195.png>)

Proof. This lemma is equivalent to Lemma 5.2 after appropriate rescaling of the measures dx and dy.

![image 196](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile196.png>)

![image 197](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile197.png>)

![image 198](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile198.png>)

![image 199](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile199.png>)

The above lemmas are suﬃcient for proving inheritance of regularity, so that the reader may now skip to the next subsection. The rest of this subsection contains a proof that an upper bound on the actual C4 count implies discrepancy, a result of independent interest which is discussed further in Section 9.2 on relative quasirandomness.

- Proposition 5.4. Let G be a bipartite graph between vertex sets X and Y . Let 0 ≤ q ≤ 1 and ǫ > 0. Suppose G(K1,1) ≥ (1 − ǫ)q and G(K2,2) ≤ (1 + ǫ)4q4, then (X,Y )G satisﬁes DISC(q,q,4ǫ1/36).


The hypotheses in Proposition 5.4 actually imply two-sided bounds on G(K1,1), G(K1,2), G(K2,1), and G(K2,2), by the following lemma.

- Lemma 5.5. Let G be a bipartite graph between vertex sets X and Y and f : X × Y → R be any function. Then f(K1,1)4 ≤ f(K1,2)2 ≤ f(K2,2). Proof. The result follows from two applications of the Cauchy-Schwarz inequality.

f(K2,2) =

y,y′∈Y x,x′∈X

f(x,y)f(x,y′)f(x′,y)f(x′,y′) dxdx′dydy′

=

y,y′∈Y x∈X

f(x,y)f(x,y′) dx

2

dydy′

≥

y,y′∈Y x∈X

f(x,y)f(x,y′) dx dydy′

2

= f(K1,2)2

=

x∈X y∈Y

f(x,y) dy

2

dx

2

≥

x∈X y∈Y

f(x,y) dy dx

4

= f(K1,1)4.

![image 200](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile200.png>)

![image 201](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile201.png>)

![image 202](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile202.png>)

![image 203](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile203.png>)

A bound on K1,2 is a second moment bound on the degree distribution, so we can bound the number of vertices of low degree using Chebyshev’s inequality, as done in the next lemma. Recall the notation G(x,S) = y∈Y G(x,y)1S(y) dy for S ⊆ Y as the normalized degree.

- Lemma 5.6. Let G be a bipartite graph between vertex sets X and Y . Let 0 ≤ q ≤ 1 and ǫ > 0. Suppose G(K1,1) ≥ (1 −ǫ)q and G(K1,2) ≤ (1 + ǫ)2q2. Let X′ = x ∈ X G(x,Y ) < (1 − 2ǫ1/3)q .


- Then |X′| ≤ 2ǫ1/3 |X|. Proof. We have


Thus |X′| ≤ 54ǫ1/3 |X|.

![image 204](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile204.png>)

|X′| |X|

![image 205](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile205.png>)

2ǫ1/3q

2

(G(x,Y ) − q)2 dx

≤

x∈X

= G(K1,2) − 2qG(K1,1) + q2 ≤ (1 + ǫ)2q2 − 2(1 − ǫ)q2 + q2 ≤ 5ǫq2.

![image 206](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile206.png>)

![image 207](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile207.png>)

![image 208](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile208.png>)

![image 209](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile209.png>)

We write

G(x,y)G(x′,y)G(x′,y′) dxdx′dydy′.

G = x,x′∈X y,y′∈Y

The next lemma proves a lower bound on G by discarding vertices of low degree.

- Lemma 5.7. Let G be a bipartite graph between vertex sets X and Y . Let 0 ≤ q ≤ 1 and ǫ > 0. Suppose G(K1,1) ≥ (1 − ǫ)q, G(K1,2) ≤ (1 + ǫ)2q2 and G(K2,1) ≤ (1 + ǫ)2q2. Then G ≥ (1 − 14ǫ1/9)q3.


Proof. Let

X′ = x ∈ X G(x,Y ) < (1 − 2ǫ1/3)q .

Let G′ denote the subgraph of G where we remove all edges with an endpoint in X′. Then G′(K2,1) ≤ G(K2,1) ≤ (1 + ǫ)2q2 and, by Lemma 5.6

|X \ X′| |X|

G′(K1,1) ≥

(1 − 2ǫ1/3)q ≥ (1 − 2ǫ1/3)2q ≥ (1 − 4ǫ1/3)q.

![image 210](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile210.png>)

Let

Y ′ = y ∈ Y G(X \ X′,y) < (1 − 4ǫ1/9)q .

So |Y ′| ≤ 4ǫ1/9 by applying Lemma 5.6 again. Restricting to paths with vertices in X \ X′,Y \ Y ′,X \ X′,Y , we ﬁnd that

2

|Y \ Y ′| |Y |

G(X \ X′,y)

G ≥

min

min

G(x,Y )

![image 211](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile211.png>)

y∈Y \Y ′

x∈X\X′

≥ (1 − 4ǫ1/9)3(1 − 2ǫ1/3)q3 ≥ (1 − 14ǫ1/9)q3.

![image 212](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile212.png>)

![image 213](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile213.png>)

![image 214](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile214.png>)

![image 215](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile215.png>)

The above argument can be modiﬁed to show that a bound on K1,2 implies one-sided counting for trees. We state the generalization and omit the proof.

- Proposition 5.8. Let H be a tree on vertices {1,2,... ,m}. For every θ > 0 there exists ǫ > 0 of size polynomial in θ so that the following holds.


Let G be a weighted graph with vertex subsets X1,... ,Xm. For every edge ab of H, assume there is some qab ∈ [0,1] so that the bipartite graph (Xa,Xb)G satisﬁes G(K1,1) ≥ (1 − ǫ)qab, G(K1,2) ≤ (1 + ǫ)2qab2 and G(K2,1) ≤ (1 + ǫ)2qab2 . Then G(H) ≥ (1 − θ)q(H).

Proof of Proposition 5.4. Using Lemma 5.5, we have G(K1,2) ≤ (1 + ǫ)2q2, G(K2,1) ≤ (1 + ǫ)2q2 and G(K1,1) ≤ (1 + ǫ)q. Let f(x,y) = G(x,y) − q. Applying Lemma 5.7, we have

f(K2,2) = G(K2,2) − 4qG + 2q2G(K1,1)2 + 4q2G(K1,2) − 4q3G(K1,1) + q4 ≤ (1 + ǫ)4q4 − 4(1 − 14ǫ1/9)q4 + 2(1 + ǫ)2q4 + 4(1 + ǫ)2q4 − 4(1 − ǫ)q4 + q4 ≤ 100ǫ1/9q4.

Thus, by Lemma 5.2, (X,Y )G satisﬁes DISC(q,q,4ǫ1/36).

![image 216](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile216.png>)

![image 217](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile217.png>)

![image 218](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile218.png>)

![image 219](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile219.png>)

- 5.2 K1,2,2 implies inheritance We now prove Propositions 1.13 and 5.1 using Lemma 5.3.


Proof of Proposition 1.13. First we show that only a small fraction of vertices in Z have very few neighbors in X and Y . Let Z1 be the set of all vertices in Z with fewer than (1 − ξ)qXZ |X| neighbors in X. Applying discrepancy to (X,Z1) yields ξqXZ |Z1| ≤ ǫp|Z|. If we assume that ǫ ≤ 13αξ2, we have |Z1| ≤ ξqǫp

|Z| ≤ 3ξ |Z|. Similarly let Z2 be the set of all vertices in Z with fewer than (1 − ξ)qYZ |Y | neighbors in Y , so that |Z2| ≤ 3ξ |Z| as well.

![image 220](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile220.png>)

![image 221](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile221.png>)

![image 222](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile222.png>)

XZ

![image 223](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile223.png>)

Deﬁne f : V (G) × V (G) → R to be a function which agrees with G on pairs (X,Z) and (Y,Z), and agrees with G − qXY on (X,Y ). Let us assign each vertex of K2,2,1 to one of {X,Y,Z} as follows (two vertices are assigned to each of X and Y ).

X Y

Z

The stated jumbledness hypotheses suﬃce for counting K1,2,2 and its subgraphs; we refer to the tutorial in Section 4.5 for an explanation.

By expanding all the (G(x,y) − qXY ) factors and using our counting lemma, we get

f = G − 4qXY G + 2qXY2 G

+ 4qXY2 G − 4qXY3 G + qXY4 G

p≈8 c,ǫ

q − 4qXY q + 2qXY2 q

+ 4qXY2 q − 4qXY3 q + qXY4 q

= 0.

Therefore, by choosing ǫ and c to be suﬃciently small (but polynomial in ξ,α,ǫ′), we can guarantee that

1 3

ξ(1 − ξ)4ǫ′4α4p8.

f ≤

![image 224](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile224.png>)

Let K2,2 denote the subgraph of the above K1,2,2 that gets mapped between X and Y . For each z ∈ Z, let fz : X × Y → R be deﬁned by (G(x,y) − qXY )1NX(z)(x)1NY (z)(y). We have

f =

fz(K2,2) dz.

z∈Z

By Lemma 5.5, fz(K2,2) ≥ 0 for all z ∈ Z. Let Z3 be the set of vertices z in Z such that fz(K2,2) > ǫ′4(1 − ξ)4α4p8. Then |Z3| ≤ 3ξ |Z|.

![image 225](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile225.png>)

Let Z′ = Z \ (Z1 ∪ Z2 ∪ Z3). So |Z′| ≥ (1 − ξ)|Z|. Furthermore, for any z ∈ Z1,

2 |NY (z)| |Y |

2

fz(K2,2) ≤ ǫ′4(1 − ξ)4α4p8 ≤ ǫ′4(1 − ξ)4p4qXZ2 qY2 Z ≤ ǫ′4p4 |NX(z)|

.

![image 226](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile226.png>)

![image 227](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile227.png>)

|X|

It follows by Lemma 5.3 that (NX(z),NY (z))G satisﬁes DISC(qXY ,p,ǫ′). Proof of Proposition 5.1. The proof is essentially the same as the proof of Proposition 1.13 with the diﬀerence being that we now use the following graph. We omit the details.

![image 228](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile228.png>)

![image 229](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile229.png>)

![image 230](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile230.png>)

![image 231](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile231.png>)

X Y

Z

![image 232](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile232.png>)

![image 233](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile233.png>)

![image 234](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile234.png>)

![image 235](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile235.png>)

## 6 One-sided counting

We are now in a position to prove Theorem 1.14, which we now recall. Theorem 1.14 For every ﬁxed graph H on vertex set {1,2,... ,m} and every α,θ > 0, there exist constants c > 0 and ǫ > 0 such that the following holds.

Let Γ be a graph with vertex subsets X1,... ,Xm and suppose that the bipartite graph (Xi,Xj)Γ is (p,cpd2(H)+3 |Xi| |Xj|)-jumbled for every i < j with ij ∈ E(H). Let G be a subgraph of Γ, with the vertex i of H assigned to the vertex subset Xi of G. For each edge ij of H, assume that (Xi,Xj)G satisﬁes DISC(qij,p,ǫ), where αp ≤ qij ≤ p. Then G(H) ≥ (1 − θ)q(H).

![image 236](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile236.png>)

The idea is to embed vertices of H one at a time. At each step, the set of potential targets for each unembedded vertex shrinks, but we can choose our embedding so that it doesn’t shrink too much and discrepancy is inherited.

Proof. Suppose that v1,v2,... ,vm is an ordering of the vertices of H which yields the 2-degeneracy

- d2(H) and that the vertex vi is to be embedded in Xi. Let L(j) = {v1,v2,... ,vj}. For i > j, let N(i,j) = N(vi) ∩ L(j) be the set of neighbors vh of vi with h ≤ j. Let q(j) = qab, where the


product is taken over all edges vavb of H with 1 ≤ a < b ≤ j and q(i,j) = v

h∈N(i,j) qhi. Note that q(j) = q(j,j − 1)q(j − 1).

We need to deﬁne several constants. To begin, we let θm = θ and ǫm = 1. Given θj and

ǫj, we deﬁne ξj = 6θmj2 and θj−1 = θ2j . We apply Propositions 1.13 and 5.1 with α,ξj and ǫj to ﬁnd constants cj−1 and ǫ∗j−1 such that the conclusions of the two propositions hold. We let

![image 237](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile237.png>)

![image 238](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile238.png>)

2 j

ǫj−1 = min(ǫ∗j−1, αθ

72m), c = 21αd2(H)c0 and ǫ = ǫ0.

![image 239](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile239.png>)

![image 240](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile240.png>)

We will ﬁnd many embeddings f : V (H) → V (G) by embedding the vertices of H one by one in increasing order. We will prove by induction on j that there are (1 − θj)q(j)|X1||X2|... |Xj| choices for f(v1),f(v2),... ,f(vj) such that the following conditions hold. Here, for each i > j, we let T(i,j) be the set of vertices in Xi which are adjacent to f(vh) for every vh ∈ N(i,j). That is, it is the set of possible vertices into which, having embedded v1,v2,... ,vj, we may embed vi.

- • For 1 ≤ a < b ≤ j, (f(va),f(vb)) is an edge of G if (va,vb) is an edge of H;
- • |T(i,j)| ≥ (1 − θ6j )q(i,j)|Xi| for every i > j;

![image 241](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile241.png>)

- • For each i1,i2 > j with vi1vi2 an edge of H, the graph (T(i1,j),T(i2,j))G satisﬁes the discrepancy condition DISC(qab,p,ǫj).


The base case j = 0 clearly holds by letting T(i,0) = Xi. We may therefore assume that there are (1 − θj−1)q(j − 1)|X1||X2|... |Xj−1| embeddings of v1,... ,vj−1 satisfying the conditions above. Let us ﬁx such an embedding f. Our aim is to ﬁnd a set W(j) ⊆ T(j,j − 1) with

|W(j)| ≥ (1 − θ2j )q(j,j − 1)|Xj| such that for every w ∈ W(j) the following three conditions hold.

![image 242](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile242.png>)

- 1. For each i > j with vi ∈ N(vj), there are at least (1 − θ6j )q(i,j)|Xi| vertices in T(i,j − 1) which are adjacent to w;

![image 243](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile243.png>)

- 2. For each i1,i2 > j with vi1vi2, vi1vj and vi2vj edges of H, the induced subgraph of G between N(w) ∩ T(i1,j) and N(w) ∩ T(i2,j) satisﬁes the discrepancy condition DISC(qab,p,ǫj);
- 3. For each i1,i2 > j with vi1vi2 and vi1vj edges of H and vi2vj not an edge of H, the induced subgraph of G between N(w) ∩ T(i1,j) and T(i2,j − 1) satisﬁes the discrepancy condition DISC(qab,p,ǫj).


Note that once we have found such a set, we may take f(vj) = w for any w ∈ W(j). By using the induction hypothesis to count the number of embeddings of the ﬁrst j − 1 vertices, we see that there are at least

θj 2

1 −

![image 244](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile244.png>)

q(j,j − 1)|Xj|(1 − θj−1)q(j − 1)|X1||X2|... |Xj−1| ≥ (1 − θj)q(j)|X1||X2|... |Xj|

ways of embedding v1,v2,... ,vj satisfying the necessary conditions. Here we used that q(j) = q(j,j−1)q(j−1) and θj−1 = θ2j . The induction therefore follows by letting T(i,j) = N(w)∩T(i,j−1) for all i > j with vi ∈ N(vj) and T(i,j) = T(i,j − 1) otherwise.

![image 245](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile245.png>)

It remains to show that there is a large subset W(j) of T(j,j − 1) satisfying the required conditions. For each i > j, let Ai(j) be the set of vertices in T(j,j − 1) for which |N(w) ∩ T(i,j − 1)| ≤ (1 − 12θj )qij|T(i,j − 1)|. Then, since the graph between T(i,j − 1) and T(j,j − 1) satisﬁes DISC(qji,p,ǫj−1), we have that ǫj−1p|T(j,j − 1)| ≥ 12θj qij|Ai(j)|. Hence, since qij ≥ αp,

![image 246](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile246.png>)

![image 247](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile247.png>)

12ǫj−1

|Ai(j)| ≤

αθj |T(j,j − 1)|. Note that for any w ∈ T(j,j − 1) \ Ai(j),

![image 248](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile248.png>)

θj 12

θj 6

|N(w) ∩ T(i,j − 1)| ≥ 1 −

qij|T(i,j − 1)| ≥ 1 −

q(i,j)|Xi|.

![image 249](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile249.png>)

![image 250](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile250.png>)

For each i1,i2 > j with vi1vi2, vi1vj and vi2vj edges of H, let Bi1,i2(j) be the set of vertices w in T(j,j − 1) for which the graph between N(w) ∩ T(i1,j − 1) and N(w) ∩ T(i2,j − 1) does not satisfy DISC(qi1i2,p,ǫj). Note that

θj−1 6

q(i1,j − 1)q(i2,j − 1)|Xi1||Xi2|

|T(i1,j − 1)||T(i2,j − 1)| ≥ 1 −

![image 251](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile251.png>)

α2d2(H)−2 2

p2d2(H)−2|Xi1||Xi2|,

≥

![image 252](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile252.png>)

where we get 2d2(H)−2 because j is a neighbor of both i1 and i2 with j < i1,i2. Similarly, |T(i1,j− 1)||T(j,j − 1)| and |T(i2,j − 1)||T(j,j − 1)| are at least α2d22(H)p2d2(H)|Xj| and α2d22(H)p2d2(H)|Xi2|, respectively.

![image 253](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile253.png>)

![image 254](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile254.png>)

Since

- 1

![image 255](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile255.png>)

- 2


![image 256](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile256.png>)

αd2(H)c0p4 p2d2(H)−2|Xi1||Xi2| ≤ c0p4 |T(i1,j − 1)||T(i2,j − 1)|,

cpd2(H)+3 |Xi1||Xi2| ≤

![image 257](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile257.png>)

![image 258](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile258.png>)

the induced subgraph of Γ between T(i1,j−1) and T(i2,j−1) is (p,c0p4 |T(i1,j − 1)||T(i2,j − 1)|)jumbled. Similarly, the induced subgraph of Γ between the sets T(j,j − 1) and T(i1,j − 1) is (p,c0p3 |T(j,j − 1)||T(i1,j − 1)|)-jumbled and the induced subgraph between T(j,j − 1) and T(i2,j −1) is (p,c0p3 |T(j,j − 1)||T(i2,j − 1)|)-jumbled. By our choice of ǫj−1, we may therefore apply Proposition 1.13 to show that |Bi1,i2(j)| ≤ ξj|T(j,j − 1)|.

![image 259](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile259.png>)

![image 260](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile260.png>)

![image 261](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile261.png>)

For each i1,i2 > j with vi1vi2 and vi1vj edges of H and vi2vj not an edge of H, let Ci1,i2(j) be the set of vertices w in T(j,j − 1) for which the graph between N(w) ∩T(i1,j − 1) and T(i2,j −1) does not satisfy DISC(qi1i2,p,ǫj). As with Bi1,i2(j), we may apply Proposition 5.1 to conclude that |Ci1,i2(j)| ≤ ξj|T(j,j − 1)|.

Counting over all possible bad events and using that |T(j,j −1)| ≥ (1 − θj6−1)q(j,j −1)|Xj|, we see that the set W(j) of good vertices has size at least (1 − σ)q(j,j − 1)|Xj|, where

![image 262](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile262.png>)

12mǫj−1 αθj

θj 6

θj 6 ≤

θj 2

θj 12

θj−1 6

m 2

ξj ≤

σ ≤

+

+ 2

+

+

,

![image 263](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile263.png>)

![image 264](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile264.png>)

![image 265](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile265.png>)

![image 266](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile266.png>)

![image 267](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile267.png>)

![image 268](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile268.png>)

2 j

- as required. Here we used θj = θj2−1, ǫj−1 ≤ αθ


72m and ξj = 6θmj2. This completes the proof.

![image 269](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile269.png>)

![image 270](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile270.png>)

![image 271](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile271.png>)

![image 272](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile272.png>)

![image 273](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile273.png>)

![image 274](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile274.png>)

![image 275](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile275.png>)

Note that for the clique Kt, we have d2(Kt) + 3 = t + 1. In this case, it is better to use the bound coming from two-sided counting, which gives the exponent t.

Another case of interest is when the graph H is triangle-free. Here it is suﬃcient to always apply the simpler inheritance theorem, Proposition 5.1, to maintain discrepancy. Then, since

![image 276](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile276.png>)

pd2(H)+2 |Xi1||Xi2| = p25 p2d2(H)−1|Xi1||Xi2|,

![image 277](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile277.png>)

![image 278](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile278.png>)

we see that an exponent of d2(H) + 2 is suﬃcient in this case. In particular, for H = Ks,t, we get an exponent of d2(Ks,t) + 2 = s−21 + 2 = s+32 , as quoted in Table 1.

![image 279](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile279.png>)

![image 280](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile280.png>)

It is also worth noting that a one-sided counting lemma for Γ holds under the slightly weaker assumption that β ≤ cpd2(H)+1n. We omit the details since the proof is a simpler version of the previous one, without the necessity for tracking inheritance of discrepancy.

- Proposition 6.1. For every ﬁxed graph H on vertex set {1,2,... ,m} and every α,θ > 0 there exist constants c > 0 and ǫ > 0 such that the following holds.

Let Γ be a graph with vertex subsets X1,... ,Xm where vertex i of H is assigned to the vertex subset Xi of Γ and suppose that the bipartite graph (Xi,Xj)Γ is (p,cpd2(H)+1 |Xi||Xj|)-jumbled for every i < j with ij ∈ E(H). Then Γ(H) ≥ (1 − θ)p(H).

![image 281](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile281.png>)

7 Counting cycles

Using the tools of doubling and densiﬁcation, we already know how to count all cycles. For cycles of length 4 or greater, (p,cp2n)-jumbledness suﬃces.

- Proposition 7.1. Assume Setup 4.1 with H = Cℓ and k ≥ 3 if ℓ = 3 or k ≥ 2 if ℓ ≥ 4. Then G(Cℓ)≈c,ǫp(Cℓ) q(Cℓ).


Proof. When ℓ = 4, see Proposition 4.13. When ℓ = 3, see Section 2 for the doubling procedure. For ℓ ≥ 5, we can perform densiﬁcation to reduce the problem to counting Cℓ−1 with at least one dense edge, so we proceed by induction.

![image 282](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile282.png>)

![image 283](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile283.png>)

![image 284](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile284.png>)

![image 285](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile285.png>)

# ⇐

The goal of this section is to prove a one-sided counting lemma for cycles that requires much weaker jumbledness.

Proposition 7.2. Assume Setup 4.1 with H = Cℓ, where ℓ ≥ 5, and all edges sparse. Let k ≥ 1+ ℓ−13 if ℓ is odd and 1+ ℓ−14 if ℓ is even. Then G(Cℓ) ≥ q(Cℓ)−θp(Cℓ) with θ ≤ 100(ǫ1/(2ℓ)+ℓc2/3).

![image 286](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile286.png>)

![image 287](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile287.png>)

The strategy is via subdivision densiﬁcation, as outlined in Section 2.

### 7.1 Subdivision densiﬁcation

In Section 4.2 we showed how to reduce a counting problem by transforming a singly subdivided edge of H into a dense edge. In this section, we show how to transform a multiply subdivided edge of H into a dense edge, using much weaker hypotheses on jumbledness, at least for one-sided counting. The idea is that a long subdivision allows more room for mixing, and thus requires less jumbledness at each step.

# ⇐

We introduce a weaker variant of discrepancy for one-sided counting.

Deﬁnition 7.3. Let G be a graph with vertex subsets X and Y . We say that (X,Y )G satisﬁes DISC≥(q,p,ǫ) if

(G(x,y) − q)u(x)v(y) dxdy ≥ −ǫp (10)

- x∈X
- y∈Y


for all functions u: X → [0,1] and all v: Y → [0,1].

In a graph H, we say that a0a1a2 ··· am is a subdivided edge if the neighborhood of ai in H is {ai−1,ai+1} for 1 ≤ i ≤ m − 1. Say that it is sparse if every edge aiai+1, 0 ≤ i ≤ m − 1, is sparse.

For a graph Γ or G with vertex subsets X0,X1,... ,Xm, x0 ∈ X0, xm ∈ Xm and Xi′ ⊆ Xi, we write

G(x0,X1′,X2′,... ,Xm′ ) = x

1∈X1

··· xm∈Xm

m(xm) dx1dx2 ··· dxm,

(x1)··· G(xm−1,xm)1X′

G(x0,x1)1X′

1

G(x0,X1′,X2′,... ,xm) = x1∈X1

(x1)··· G(xm−1,xm) dx1dx2 ··· dxm−1.

G(x0,x1)1X′

1

··· xm−1∈Xm−1

These quantities can be interpreted probabilistically. The ﬁrst expression is the probability that a randomly chosen sequence of vertices with one endpoint ﬁxed is a path in G with the vertices landing in the chosen subsets. For the second expression, both endpoints are ﬁxed.

Lemma 7.4 (Subdivision densiﬁcation). Assume Setup 4.1. Let ℓ ≥ 2 and let a0a1 ··· aℓ be a sparse subdivided edge and assume that a0aℓ is not an edge of H. Assume k ≥ 1 + 2ℓ1−2. Replace the induced bipartite graph (Xa0,Xaℓ) by the weighted bipartite graph given by

![image 288](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile288.png>)

G(x0,xℓ) =

1 4pℓ

min G(x0,X1,X2,... ,Xℓ−1,xℓ),4pℓ

![image 289](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile289.png>)

for (x0,xℓ) ∈ X0 × Xℓ. Let H′ be H with the path a0a1 ··· aℓ deleted and the edge a0aℓ added. Let pa0aℓ = 1 and qa0aℓ = 41pℓqa0a1qa1a2 ··· qaℓ−1aℓ. Then G(H) ≥ 4pℓG(H′) and (X0,Xℓ)G satisﬁes DISC≥(qa0aℓ,1,18(ǫ1/(2ℓ) + ℓc2/3)).

![image 290](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile290.png>)

Remark. If there is at least one dense edge in the subdivision, then using arguments similar to the ones in Section 4.2, modiﬁed for one-sided counting, we can show that k ≥ 1 suﬃces for subdivision densiﬁcation.

The idea of the proof is very similar to densiﬁcation in Section 4.2. The claim G(H) ≥ 4pℓG(H′) follows easily from the new edge weights. It remains to show that (X0,Xℓ)G satisﬁes DISC≥. So

- Lemma 7.4 follows from the next result.
- Lemma 7.5. Let m ≥ 2, c,ǫ,p ∈ (0,1], and q1,q2,... ,qm ∈ [0,p]. Let Γ be any weighted graph with vertex subsets X0,X1,... ,Xm and let G be a subgraph of Γ. Suppose that, for each i = 1,... ,m,

(Xi−1,Xi)Γ is (p,cp1+

1 2m−2

![image 291](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile291.png>)

![image 292](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile292.png>)

|Xi−1| |Xi|)-jumbled and (Xi−1,Xi)G satisﬁes DISC≥(qi,p,ǫ). Then the weighted graph G′ on (X0,Xm) deﬁned by

G′(x0,xm) = min {G(x0,X1,X2,... ,Xm−1,xm),4pm} satisﬁes DISC≥(q1q2 ··· qm,pm,72(ǫ1/(2m) + mc2/3)).

Here are the steps for the proof of Lemma 7.5.

- 1. Show that the graph on X0 ×Xm with weights G(x0,X1,X2,... ,Xm−1,xm) satisﬁes DISC≥.
- 2. Under the assumption that every vertex Xi has roughly the same number of neighbors in Xi+1 for every i, show that capping of the edge weights has negligible eﬀect on discrepancy.
- 3. Show that we can delete a small subset from each vertex subset Xi so that the assumption in step 2 is satisﬁed.


Step 2 is the most diﬃcult. Since we are only proving lower bound discrepancy, it is okay to delete vertices in step 3. This is also the reason why this proof, without signiﬁcant modiﬁcation, cannot prove two-sided discrepancy (which may require stronger hypotheses), as we may have deleted too many edges in the process. Also, unlike the densiﬁcation in Section 4.2, we do not have to worry about the eﬀect of the edge weight capping on the overall H-count, as we are content with a lower bound.

The next two lemmas form step 1 of the program.

- Lemma 7.6. Let G be a weighted graph with vertex subsets X,Y,Z. Let p1,p2,ǫ ∈ (0,1] and q1 ∈ [0,p1], q2 ∈ [0,p2]. If (X,Y )G satisﬁes DISC≥(q1,p1,ǫ) and (Y,Z)G satisﬁes DISC≥(q2,p2,ǫ), then the induced weighted bipartite graph G′ on (X,Z) whose weight is given by


G′(x,z) = G(x,Y,z) satisﬁes DISC≥(q1q2,p1p2,6√ǫ).

![image 293](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile293.png>)

Note that no jumbledness hypothesis is needed for the lemma.

- Proof. Let u: X → [0,1] and w: Z → [0,1] be arbitrary functions. Let


√ǫp1 .

Y ′ = y ∈ Y

![image 294](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile294.png>)

(G(x,y) − q1)u(x) dx ≤ −

x∈X

√ǫ|Y |. Similarly, let

Then applying (10) to u and 1Y ′ yields |Y ′| ≤

![image 295](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile295.png>)

√ǫp2 .

Y ′′ = y ∈ Y

![image 296](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile296.png>)

(G(y,z) − q2)w(z) dx ≤ −

z∈Z

√ǫ|Y | as well. So

- Then |Y ′′| ≤


![image 297](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile297.png>)

G′(x,z)u(x)w(z) dxdz = x∈X

u(x)G(x,y)G(y,z)w(z) dxdydz

x∈X z∈Z

- y∈Y
- z∈Z


≥

G(y,z)w(z) dz dy

G(x,y)u(x) dx

y∈Y \(Y ′∪Y ′′) x∈X

z∈Z

√ǫp1)(q2Ew −

√ǫp2) dy ≥ (1 − 2√ǫ)(q1Eu −

![image 298](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile298.png>)

![image 299](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile299.png>)

(q1Eu −

≥

y∈Y \(Y ′∪Y ′′)

√ǫp2) ≥ q1q2EuEw − 6√ǫp1p2.

√ǫp1)(q2Ew −

![image 300](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile300.png>)

![image 301](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile301.png>)

![image 302](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile302.png>)

![image 303](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile303.png>)

![image 304](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile304.png>)

![image 305](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile305.png>)

![image 306](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile306.png>)

![image 307](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile307.png>)

The above proof can be extended to prove a one-sided counting lemma for trees without any jumbledness hypotheses. We omit the details. Proposition 7.7. Let H be a tree on vertices {1,2,... ,m}. For every θ > 0, there exists ǫ > 0 of size at least polynomial in θ such that the following holds.

Let G be a weighted graph with vertex subsets X1,... ,Xm. For each edge ab of H, suppose that (Xa,Xb)G satisﬁes DISC≥(qab,pab,ǫ) for some 0 ≤ qab ≤ pab ≤ 1. Then G(H) ≥ q(H) − θp(H).

By Lemma 7.6 and induction, we obtain the following lemma about counting paths in G.

- Lemma 7.8. Let G be a weighted graph with vertex subsets X0,X1,... ,Xm. Let 0 < ǫ < 1. Suppose that for each i = 1,2,... ,m, (Xi−1,Xi)G satisﬁes DISC≥(qi,pi,ǫ) for some numbers 0 ≤ qi ≤ pi ≤ 1. Then the induced weighted bipartite graph G′ on X0 × Xm whose edge weights are given by


G′(x0,xm) = G(x0,X1,X2,... ,Xm−1,xm) satisﬁes DISC≥(q1q2 ··· qm,p1p2 ··· pm,36ǫ1/(2m)).

Proof. Applying Lemma 7.6, we see that the auxiliary weighted graphs on (X0,X2),(X2,X4),... satisfy DISC≥(q1q2,p1p2,36ǫ1/2), etc. Applying Lemma 7.6 again, we ﬁnd that the auxiliary weighted graph on (X0,X4),(X4,X8) satisfy DISC≥(q1q2q3q4,p1p2p3p4,36ǫ1/4), etc. Continuing, we ﬁnd that (X0,Xm)G′ satisﬁes DISC≥(q1q2 ··· qm,p1p2 ··· pm,ǫ′) with ǫ′ = 36ǫ2−(log2m+1) = 36ǫ1/(2m).

![image 308](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile308.png>)

![image 309](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile309.png>)

![image 310](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile310.png>)

![image 311](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile311.png>)

For step 2 of the proof, we need to assume some degree-regularity between the parts. We note that the order of X and Y is important in the following deﬁnition.

Deﬁnition 7.9. Let Γ be a weighted graph with vertex subsets X and Y . We say that (X,Y )Γ is (p,ξ,η)-bounded if |Γ(x,Y ) − p| ≤ ξp for all x ∈ X and Γ(x,y) ≤ η for all x ∈ X and y ∈ Y .

Here is the idea of the proof. Fix a vertex x0 ∈ X0, and consider its successive neighborhoods in X1,X2,... . Let us keep track of the number of paths from x0 to each endpoint. We expect the number of paths to be somewhat evenly distributed among vertices in the successive neighborhoods and, therefore, we do not expect many vertices in Xi to have disproportionately many paths to x0. In particular, capping the weights of Γ(x0,X1,... ,Xm−1,xm) has a negligible eﬀect.

![image 312](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile312.png>)

Here is a back-of-the-envelope calculation. Suppose every pair (Xi,Xi+1)Γ is (p,γ |Xi||Xi+1|)jumbled. First we remove a small fraction of vertices from each vertex subset Xi so in the remaining graph Γ is bounded, i.e., every vertex has roughly the expected number of neighbors in the next vertex subset. Let S ⊆ Xi, and let N(S) be its neighborhood in Xi+1. Then the number of edges

- e(S,N(S)) between S and N(S) is roughly p|S||Xi+1| by the degree assumptions on Xi. On the other hand, by jumbledness, e(S,Ni+1(S)) ≤ γ |Xi| |Xi+1||S| |N(S)| + p|S||N(S)|. When S is


![image 313](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile313.png>)

small, the ﬁrst term dominates, and by comparing the two estimates we get that ||NX(S)|

i+1| is at least roughly p2γ−2||XS|

![image 314](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile314.png>)

i|. Now ﬁx a vertex x0 ∈ X0. It has about p|X1| neighbors in X1. At each step, the fraction of Xi occupied by the successive neighborhood of x0 expands by a factor of about p2γ−2, until the successive neighborhood saturates some Xi. Note that for γ = cp1+ p(p2γ−2)m−1 ≫ 1, so the successive neighborhood of x0 in Xm is essentially all of Xm. So we can expect the resulting weighted graph to be dense.

![image 315](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile315.png>)

- 1

![image 316](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile316.png>)

- 2m−2, we have


We will use induction. We show that from a ﬁxed x0 ∈ X0, if we can bound the number of paths to each vertex in Xi, then we can do so for Xi+1 as well.

The next result is the key technical lemma. It is an induction step for the lemma that follows. One should think of X,Y and Z as X0,Xi and Xi+1, respectively.

- Lemma 7.10. Let p1,p2,ξ1,ξ2,ξ3 ∈ (0,1], and η1,γ2 > 0. Let Γ be a weighted graph with vertex subsets X,Y,Z. Assume that (X,Y )Γ is (p1,ξ1,η1)-bounded and (Y,Z)Γ is (p2,ξ2,1)-bounded and


(p2,γ2 |Y ||Z|)-jumbled. Let η′ = max 4γ22p−2 1ξ3−1η1,4p1p2 and ξ′ = ξ1 + 2ξ2 + 2ξ3. Then the weighted graph Γ′ on (X,Z) given by

![image 317](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile317.png>)

Γ′(x,z) = min Γ(x,Y,z),η′ is (p1p2,ξ′,η′)-bounded.

Proof. We have Γ′(x,z) ≤ η′ for all x ∈ X,z ∈ Z. Also, by the boundedness assumptions, we have Γ′(x,Z) ≤ Γ(x,Y,Z) ≤ (1 + ξ1)(1 + ξ2)p1p2 ≤ (1 + ξ′)p1p2. It only remains to prove that Γ′(x,Z) ≥ (1 − ξ′)p1p2 for all x ∈ X.

Fix any x ∈ X. Let

Zx′ = z ∈ Z Γ(x,Y,z) > η′ . Note that Γ′(x,Z) ≥ Γ(x,Y,Z)−Γ(x,Y,Zx′ ), so we would like to ﬁnd an upper bound for Γ(x,Y,Zx′ ).

Apply the jumbledness criterion (3) to (Y,Z)Γ with the functions u(y) = Γ(x,y)η1−1 and v(z) = 1Z′

x. Note that 0 ≤ u ≤ 1 due to boundedness. We have

![image 318](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile318.png>)

![image 319](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile319.png>)

x(z) dydz ≤ γ2 Γ(x,Y )η1−1|Zx′ |

≤ γ2 (1 + ξ1)p1η1−1|Zx′ |

Γ(x,y)η1−1(Γ(y,z) − p2)1Z′

.

![image 320](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile320.png>)

![image 321](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile321.png>)

|Z|

|Z|

- y∈Y
- z∈Z


′ x|

The integral equals η1−1 Γ(x,Y,Zx′ ) − p2Γ(x,Y )|Z

|Z| , so we have

![image 322](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile322.png>)

![image 323](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile323.png>)

Γ(x,Y,Zx′ ) − p2Γ(x,Y )|Zx′ |

≤ γ2 (1 + ξ1)p1η1|Zx′ | |Z|

. (11)

![image 324](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile324.png>)

![image 325](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile325.png>)

|Z|

On the other hand, we have

|Zx′ | |Z|

≥ η′|Zx′ | |Z|

− (1 + ξ1)p1p2|Zx′ | |Z|

η′ 2

Γ(x,Y,Zx′ ) − p2Γ(x,Y )|Zx′ |

≥

. (12) Combining (12) with (11), we get

![image 326](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile326.png>)

![image 327](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile327.png>)

![image 328](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile328.png>)

![image 329](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile329.png>)

![image 330](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile330.png>)

|Z|

4γ22(1 + ξ1)p1η1 η′2

|Zx′ | |Z|

≤

. (13) Substituting (13) back into (11), we have

![image 331](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile331.png>)

![image 332](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile332.png>)

Therefore,

![image 333](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile333.png>)

Γ(x,Y,Zx′ ) ≤ (1 + ξ1)p1p2|Zx′ |

+ γ2 (1 + ξ1)p1η1|Zx′ |

![image 334](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile334.png>)

![image 335](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile335.png>)

|Z| ≤

|Z|

4γ22(1 + ξ1)2p21p2η1 η′2

2γ22(1 + ξ1)p1η1 η′ ≤

+

![image 336](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile336.png>)

![image 337](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile337.png>)

2γ22(1 + ξ1)p1η1 4γ22p−2 1ξ3−1η1

4γ22(1 + ξ1)2p21p2η1 (4γ22p−2 1ξ3−1η1)(4p1p2)

+

![image 338](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile338.png>)

![image 339](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile339.png>)

1 4

- 1

![image 340](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile340.png>)

- 2


(1 + ξ1)2ξ3p1p2 +

=

(1 + ξ1)ξ3p1p2 ≤ 2ξ3p1p2.

![image 341](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile341.png>)

Γ′(x,Z) ≥ Γ(x,Y,Z) − Γ(x,Y,Zx′ ) ≥ (1 − ξ1)(1 − ξ2)p1p2 − 2ξ3p1p2 ≥ (1 − ξ′)p1p2. This completes the proof that Γ′ is (p1p2,ξ′,η′)-bounded.

![image 342](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile342.png>)

![image 343](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile343.png>)

![image 344](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile344.png>)

![image 345](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile345.png>)

By repeated applications of Lemma 7.10, we obtain the following lemma for embedding paths in Γ.

- Lemma 7.11. Let 0 < 4c2 < ξ < 41m and 0 < p ≤ 1. Let Γ be a graph with vertex subsets X0,X1,... ,Xm. Suppose that, for each i = 1,... ,m, (Xi−1,Xi)Γ is (p,ξ,1)-bounded and


![image 346](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile346.png>)

1 2m−2

(p,cp1+

|Xi−1||Xi|)-jumbled. Then the weighted bipartite graph Γ′ on (X0,Xm) deﬁned by

![image 347](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile347.png>)

![image 348](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile348.png>)

Γ′(x0,xm) = min {Γ(x0,X1,X2,... ,Xm−1,xm),4pm} is (pm,4mξ,4pm)-bounded. Proof. Since Γ′(x0,Xm) ≤ Γ(x0,X1,X2,... ,Xm) ≤ (1 + ξ)mpm ≤ emξpm ≤ (1 + 4mξ)pm for all x0 ∈ X0, it remains to show that Γ′(x0,Xm) ≥ (1 − 4mξ)pm for all x0 ∈ X0.

For every i = 1,... ,m, deﬁne a weighted graph Γ(i) on vertex sets X0,Xi,Xi+1 (with Γ(m) only deﬁned on X0 and Xm) as follows. Set (Xi,Xi+1)Γ(i) = (Xi,Xi+1)Γ for each 1 ≤ i ≤ m − 1. Set (X0,X1)Γ(1) = (X0,X1)Γ and

Γ(i+1)(x0,xi+1) = min Γ(i)(x0,Xi,xi+1),ηi+1 for each 1 ≤ i ≤ m − 1, where

ηi = max (4c2ξ−1)i−1p(i−1)(1+m1−1),4pi

![image 349](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile349.png>)

for every i. So Γ(i)(x0,xi) ≤ Γ(x0,X1,... ,Xi−1,xi) for every i and every x0 ∈ X0,xi ∈ Xi. Let γ = cp1+

- 1

![image 350](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile350.png>)

- 2m−2. Note that ηi+1 = max 4γ2p−1ξ−1ηi,4pi+1 for every i. So it follows by


- Lemma 7.10 and induction that (X0,Xi)Γ(i) is (pi,4iξ,ηi)-bounded for every i. Since ηm = 4pm, Γ′(x0,Xm) ≥ Γ(m)(x0,Xm) ≥ (1 − 4mξ)pm, as desired.


![image 351](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile351.png>)

![image 352](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile352.png>)

![image 353](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile353.png>)

![image 354](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile354.png>)

To complete step 2 of the proof, we show that the boundedness assumptions imply that the edge weight capping has negligible eﬀect on discrepancy.

- Lemma 7.12. Let 0 < 4c2 < ξ and 0 < p ≤ 1. Let Γ be a graph with vertex subsets X0,X1,... ,Xm and let G be a subgraph of Γ. Suppose that, for each i = 1,... ,m, (Xi−1,Xi)Γ is (p,ξ,1)-

bounded and (p,cp1+

1 2m−2

![image 355](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile355.png>)

![image 356](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile356.png>)

|Xi−1| |Xi|)-jumbled and (Xi−1,Xi)G satisﬁes DISC≥(qi,pi,ǫ). Then the weighted graph G′ on (X0,Xm) deﬁned by

G′(x0,xm) = min {G(x0,X1,X2,... ,Xm−1,xm),4pm} satisﬁes DISC≥(q1q2 ··· qm,pm,36ǫ1/(2m) + 8mξ).

Proof. We may assume that ξ < 41m since otherwise the claim is trivial as every graph satisﬁes DISC≥(q,p,ǫ) when ǫ ≥ 1. Let Γ′ be constructed as in Lemma 7.11. To simplify notation, let us write

![image 357](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile357.png>)

G(x0,xm) = G(x0,X1,··· ,Xm−1,xm) and Γ(x0,xm) = Γ(x0,X1,··· ,Xm−1,xm)

for x0 ∈ X0, xm ∈ Xm. We have G(x0,xm) − G′(x0,xm) = max{0,G(x0,xm) − 4pm}

≤ max{0,Γ(x0,xm) − 4pm} = Γ(x0,xm) − Γ′(x0,xm). Let q = q1q2 ··· qm. For any functions u: X → [0,1] and v: Y → [0,1], we have

x0∈X0 xm∈Xm

(G′(x0,xm) − q)u(x0)v(xm) dx0dxm ≥

x0∈X0 xm∈Xm

(G(x0,xm) − q)u(x0)v(xm) dx0dxm

−

x0∈X0 xm∈Xm

(Γ(x0,xm) − Γ′(x0,xm))u(x0)v(xm) dx0dxm.

The ﬁrst term is at least −36ǫ1/(2m)pm by Lemma 7.8. For the second term, we use the boundedness of Γ and Γ′ to get

x0∈X0 xm∈Xm

(Γ(x0,xm) − Γ′(x0,xm))u(x0)v(xm) dx0dxm ≤

x0∈X0 xm∈Xm

(Γ(x0,xm) − Γ′(x0,xm) dx0dxm

≤ (1 + ξ)mpm − (1 − 4ξm)pm ≤ 8ξmpm.

It follows that G′ satisﬁes DISC≥(q,pm,36ǫ1/(2m) + 8mξ).

![image 358](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile358.png>)

![image 359](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile359.png>)

![image 360](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile360.png>)

![image 361](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile361.png>)

This completes step 2 of the program. Finally, we need to show that we have a large subgraph of Γ satisfying boundedness, so that we can apply Lemma 7.12 and then transfer the results back to the original graph.

- Lemma 7.13. Let 0 < δ,γ,ξ,p < 1 satisfy 2γ2 ≤ δξ2p2. Let Γ be a graph with vertex subsets X0,X1,... ,Xm and suppose that, for each i = 1,... ,m, (Xi−1,Xi)Γ is (p,(1 − δ)γ |Xi−1||Xi|)jumbled. Then we can ﬁnd Xi ⊆ Xi with Xi ≥ (1 − δ)|Xi| for every i such that, for every


![image 362](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile362.png>)

![image 363](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile363.png>)

- 0 ≤ i ≤ m − 1, the induced bipartite graph ( Xi, Xi+1)Γ is (p,ξ,1)-bounded and (p,γ Xi Xi+1 )jumbled.


Proof. The jumbledness condition follows directly from the size of |Xi|, so it suﬃces to make the bipartite graphs bounded. Let Xm = Xm. For each i = m − 1,m − 2,... ,0, in this order, set Xi to be the vertices in Xi with (1 ± ξ)p Xi+1 neighbors in Xi+1. So ( Xi, Xi+1) is (p,ξ,1)-bounded.

Lemma 3.7 gives us Xi \ Xi ≤ ξ22γp22 |Xi| ≤ δ |Xi|.

![image 364](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile364.png>)

![image 365](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile365.png>)

![image 366](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile366.png>)

![image 367](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile367.png>)

![image 368](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile368.png>)

- Lemma 7.14. Let 0 ≤ q ≤ p ≤ 1 and ǫ,δ,δ′ > 0. Let G be a weighted bipartite graph with vertex sets X and Y . Let X ⊆ X and Y ⊆ Y satisfy X ≥ (1 − δ)|X| and Y ≥ (1 − δ)|Y |. Let G be a weighted bipartite graph on ( X, Y ) such that G(x,y) ≥ (1 − δ′) G(x,y) for all x ∈ X,y ∈ Y . If ( X, Y ) G satisﬁes DISC≥(q,p,ǫ), then (X,Y )G satisﬁes DISC≥(q,p,ǫ + 2δ + δ′).


Proof. For this proof we use sums instead of integrals since the integrals corresponding to (X,Y )G and ( X, Y )G have diﬀerent normalizations and can be somewhat confusing. Let u: X → [0,1] and

- v: Y → [0,1]. We have


G(x,y)u(x)v(y) ≥ (1 − δ′)

G(x,y)u(x)v(y)

x∈X y∈Y

x∈ X y∈ Y

  − ǫp X Y

 

 

 

≥ q(1 − δ′)

v(y)

u(x)

y∈ Y

x∈ X

  − ǫp|X||Y |



≥ q(1 − δ′)

 y∈Y

v(y) − δ |Y |

u(x) − δ |X|

x∈X

≥ qu(X)v(Y ) − (ǫ + 2δ + δ′)p|X| |Y |.

![image 369](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile369.png>)

![image 370](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile370.png>)

![image 371](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile371.png>)

![image 372](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile372.png>)

Proof of Lemma 7.5. We apply Lemma 7.13 to ﬁnd large subsets of vertices for which the induced subgraph of Γ is bounded and then apply Lemma 7.12 to show that G restricted to this subgraph satisﬁes DISC≥. Finally, we use Lemma 7.14 to pass the result back to the original graph.

Here are the details. Let ξ = 8c2/3 and δ = 14c2/3, so that the hypotheses of Lemma 7.13 are satisﬁed with γ = 1−cδp1+ each i so that ( Xi, Xi+1)Γ is (p,ξ,1)-bounded and (p, 1−cδp1+

![image 373](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile373.png>)

- 1

![image 374](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile374.png>)

- 2m−2 . Therefore, we can ﬁnd Xi ⊆ Xi with Xi ≥ (1 − δ)Xi for


![image 375](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile375.png>)

![image 376](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile376.png>)

- 1

![image 377](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile377.png>)

- 2m−2 Xi Xi+1 )-jumbled for every


![image 378](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile378.png>)

- 0 ≤ i ≤ m − 1. Let G denote the graph G restricted to X0,... , Xm. Note that the normalizations


- of G and G are diﬀerent. For instance, for any S ⊆ X1 and any x0 ∈ X0 and x2 ∈ X2, we write


1 |X1| x

G(x0,S,x2) =

G(x0,x1)G(x1,x2)

![image 379](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile379.png>)

1∈S

while

1 X1 x1∈S

G(x0,S,x2) =

G(x0,x1)G(x1,x2).

![image 380](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile380.png>)

So ( Xi−1, Xi) G satisﬁes DISC≥(qi,p,ǫ′) with ǫ′ ≤ (1−ǫδ)2 ≤ 2ǫ. Let G′ denote the weighted bipartite graph on ( X0, Xm) given by

![image 381](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile381.png>)

G′(x0,xm) = min G(x0, X1,... , Xm−1,xm),4pm .

Since 4(1−cδ)2 ≤ 8c2 ≤ ξ, we can apply Lemma 7.12 to G to ﬁnd that ( X0, Xm) G′ satisﬁes DISC≥(q1 ··· qm,pm,72ǫ1/(2m) + 8mξ). To pass the result back to G′, we note that

![image 382](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile382.png>)

G′(x0,xm) = min {G(x0,X1,... ,Xm−1,xm),4pm} ≥ min G(x0, X1,... , Xm−1,xm),4pm

 

 

X1 ··· Xm−1 |X1|··· |Xm−1|

G(x0, X1,... , Xm−1,xm),4pm

= min

![image 383](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile383.png>)





≥ (1 − δ)m−1 G′(x0,xm) ≥ (1 − (m − 1)δ) G′(x0,xm).

It follows by Lemma 7.14 that (X0,Xm)G′ satisﬁes DISC≥(q1 ··· qm,pm,ǫ′) with ǫ′ ≤ 72ǫ1/(2m) + 8mξ + 2δ + (m − 1)δ ≤ 72(ǫ1/(2m) + mc2/3).

![image 384](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile384.png>)

![image 385](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile385.png>)

![image 386](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile386.png>)

![image 387](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile387.png>)

### 7.2 One-sided cycle counting

If we can perform densiﬁcation to reduce H to a triangle with two dense edges, then we have a counting lemma for H, as shown by the following lemma. Note that we do not even need any jumbledness assumptions on the remaining sparse edge.

- Lemma 7.15. Let K3 denote the triangle with vertex set {1,2,3}. Let G be a weighted graph with vertex subsets X1,X2,X3 such that, for all i = j, (Xi,Xj)G satisﬁes DISC≥(qij,pij,ǫ), where p13 = p23 = 1, 0 ≤ p12 ≤ 1, and 0 ≤ qij ≤ pij. Then G(K3) ≥ q12q13q23 − 3ǫp12. Proof. We have


G(K3) − q12q13q23 =

(G(x1,x2) − q12)G(x1,x3)G(x2,x3) dx1dx2dx3

x1,x2,x3

+ q12

(G(x1,x3) − q13)G(x2,x3) dx1dx2dx3 + q12q13

x1,x2,x3

(G(x2,x3) − q13) dx1dx2dx3.

x1,x2,x3

The ﬁrst integral can be bounded below by −ǫp12 and the latter two integrals by −ǫq12. This gives the desired bound.

![image 388](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile388.png>)

![image 389](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile389.png>)

![image 390](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile390.png>)

![image 391](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile391.png>)

The one-sided counting lemma can be proved by performing subdivision densiﬁcation as shown below.

# ⇐

Proof of Proposition 7.2. Let the vertices of Cℓ be {1,2,... ,ℓ} in that order. Apply subdivision densiﬁcation (Lemma 7.4) to the subdivided edge (1,2,... ,⌈ℓ/2⌉), as well as to the subdivided edge (⌈ℓ/2⌉ ,⌈ℓ/2⌉ + 1,... ,ℓ). Conclude with Lemma 7.15.

![image 392](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile392.png>)

![image 393](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile393.png>)

![image 394](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile394.png>)

![image 395](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile395.png>)

## 8 Applications

It is now relatively straightforward to prove our sparse pseudorandom analogues of Tura´n’s theorem, Ramsey’s theorem and the graph removal lemma. All of the proofs have essentially the same ﬂavour. We begin by applying the sparse regularity lemma for jumbled graphs, Theorem 1.11. We then apply the dense version of the theorem we are considering to the reduced graph to ﬁnd a copy of our graph H. The counting lemma then implies that our original sparse graph must also contain many copies of H.

In order to apply the counting lemma, we will always need to clean up our regular partition, removing all edges which are not contained in a dense regular pair. The following lemma is suﬃcient for our purposes.

- Lemma 8.1. For every ǫ,α > 0 and positive integer m, there exists c > 0 and a positive integer M such that if Γ is a (p,cpn)-jumbled graph on n vertices then any subgraph G of Γ is such that there is a subgraph G′ of G with e(G′) ≥ e(G) − 4αe(Γ) and an equitable partition of the vertex set into k pieces V1,V2,... ,Vk with m ≤ k ≤ M such that the following conditions hold.


- 1. There are no edges of G′ within Vi for any 1 ≤ i ≤ k.
- 2. Every non-empty subgraph (Vi,Vj)G′ has dG′(Vi,Vj) = qij ≥ αp and satisﬁes DISC(qij,p,ǫ).


Proof. Let m0 = max(32α−1,m) and θ = 32α . An application of Theorem 1.11, the sparse regularity lemma for jumbled graphs, using min {θ,ǫ} as the parameter ǫ in the regularity lemma, tells us

![image 396](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile396.png>)

that there exists an η > 0 and a positive integer M such that if Γ is (p,ηpn)-jumbled then there is an equitable partition of the vertices of G into k pieces with m0 ≤ k ≤ M such that all but θk2 pairs of vertex subsets (Vi,Vj)G satisfy DISC(qij,p,ǫ). Let c = min(η, 8M1 2).

![image 397](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile397.png>)

Since Γ is (p,β)-jumbled with β ≤ cpn, c ≤ 8M1 2 and n ≤ 2M|Vi| for all i, the number of edges between Vi and Vj satisﬁes

![image 398](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile398.png>)

|e(Vi,Vj) − p|Vi||Vj|| ≤ cpn2 ≤

- 1

![image 399](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile399.png>)

- 2


p|Vi||Vj|

and thus lies between 21p|Vi||Vj| and 23p|Vi||Vj|. Note that this also holds for i = j, allowing for the fact that we will count all edges twice.

![image 400](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile400.png>)

![image 401](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile401.png>)

Therefore, if we remove all edges contained entirely within any Vi, we remove at most 2pk 2kn 2 = 8pn2

![image 402](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile402.png>)

k ≤ α4pn2 edges. Here we used that |Vi| ≤ ⌈nk⌉ ≤ 2kn for all i. If we remove all edges contained within pairs which do not satisfy the discrepancy condition, the number of edges we are removing is

![image 403](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile403.png>)

![image 404](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile404.png>)

![image 405](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile405.png>)

![image 406](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile406.png>)

- at most 2pθk2 2kn 2 = 8pθn2 = α4pn2. Finally, if we remove all edges contained within pairs whose


![image 407](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile407.png>)

![image 408](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile408.png>)

density is smaller than αp, we remove at most αp n2 ≤ α2pn2 edges. Overall, we have removed at most αpn2 ≤ 4αe(Γ) edges. We are left with a graph G′ with e(G′) ≥ e(G) − 4αe(Γ) edges, as

![image 409](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile409.png>)

required.

![image 410](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile410.png>)

![image 411](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile411.png>)

![image 412](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile412.png>)

![image 413](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile413.png>)

### 8.1 Erdo˝s-Stone-Simonovits theorem

We are now ready to prove the Erd˝os-Stone-Simonovits theorem in jumbled graphs. We ﬁrst recall the statement. Recall that a graph Γ is (H,ǫ)-Tura´n if any subgraph of Γ with at least

1 − χ(H1)−1 + ǫ e(Γ) edges contains a copy of H.

![image 414](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile414.png>)

Theorem 1.4 For every graph H and every ǫ > 0, there exists c > 0 such that if β ≤ cpd2(H)+3n then any (p,β)-jumbled graph on n vertices is (H,ǫ)-Tura´n.

Proof. Suppose that H has vertex set {1,2,... ,m}, Γ is a (p,β)-jumbled graph on n vertices, where β ≤ cpd2(H)+3n, and G is a subgraph of Γ containing at least 1 − χ(H1)−1 + ǫ e(Γ) edges.

![image 415](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile415.png>)

We will need to apply the one-sided counting lemma, Lemma 1.14, with α = 8ǫ and θ. We get constants c0 and ǫ0 > 0 such that if Γ is (p,c0pd2(H)+3 |Xi||Xj|)-jumbled and G satisﬁes DISC(qij,p,ǫ0), where αp ≤ qij ≤ p, between sets Xi and Xj for every 1 ≤ i < j ≤ m with ij ∈ E(H), then G(H) ≥ (1 − θ)q(H).

![image 416](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile416.png>)

![image 417](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile417.png>)

Apply Lemma 8.1 with α = ǫ/8 and ǫ0. This yields constants c1 and M such that if Γ is (p,c1pn)-jumbled then there is a subgraph G′ of G with

1 χ(H) − 1

ǫ 2

1 χ(H) − 1

e(G′) ≥ 1 −

+ ǫ − 4α e(Γ) ≥ 1 −

+

e(Γ),

![image 418](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile418.png>)

![image 419](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile419.png>)

![image 420](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile420.png>)

where we used that α = 8ǫ. Moreover, there is an equitable partition of the vertex set into k ≤ M pieces V1,... ,Vk such that every non-empty subgraph (Vi,Vj)G′ has d(Vi,Vj) = qij ≥ αp and satisﬁes DISC(qij,p,ǫ0).

![image 421](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile421.png>)

We now consider the reduced graph R, considering each piece Vi of the partition as a vertex

- vi and placing an edge between vi and vj if and only if the graph between Vi and Vj is nonempty. Since Γ is (p,cpn)-jumbled and n ≤ 2M|Vi|, the number of edges between any two pieces diﬀers from p|Vi||Vj| by at most cpn2 ≤ 20ǫ p|Vi||Vj| provided that c ≤ 80Mǫ 2. Note, moreover, that


![image 422](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile422.png>)

![image 423](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile423.png>)

|Vi| ≤ ⌈nk⌉ ≤ (1 + 20ǫ )nk provided that n ≥ 20ǫM . Therefore, the number of edges in the reduced graph R is at least

![image 424](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile424.png>)

![image 425](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile425.png>)

![image 426](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile426.png>)

![image 427](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile427.png>)

(1 − χ(H1)−1 + 2ǫ)e(Γ) (1 + 20ǫ )3p(nk)2 ≥ 1 −

e(G′) (1 + 20ǫ )p⌈nk⌉2

k 2

ǫ 4

1 χ(H) − 1

![image 428](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile428.png>)

![image 429](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile429.png>)

≥

e(R) ≥

+

,

![image 430](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile430.png>)

![image 431](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile431.png>)

![image 432](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile432.png>)

![image 433](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile433.png>)

![image 434](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile434.png>)

![image 435](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile435.png>)

![image 436](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile436.png>)

![image 437](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile437.png>)

where the ﬁnal step follows from e(Γ) ≥ (1 − 20ǫ )p n2 .

![image 438](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile438.png>)

Applying the Erd˝os-Stone-Simonovits theorem to the reduced graph implies that it contains a copy of H. But if this is the case then we have a collection of vertex subsets X1,... ,Xm such that, for every edge ij ∈ E(H), the induced subgraph (Xi,Xj)G′ has d(Xi,Xj) = qij ≥ αp and satisﬁes DISC(qij,p,ǫ0). By the counting lemma, provided c ≤ 2cM0 , we have G(H) ≥ G′(H) ≥ (1 − θ)(αp)e(H)(2M)−v(H). Therefore, for c = min(2cM0 ,c1, 80Mǫ 2), we see that G contains a copy of H.

![image 439](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile439.png>)

![image 440](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile440.png>)

![image 441](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile441.png>)

![image 442](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile442.png>)

![image 443](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile443.png>)

![image 444](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile444.png>)

![image 445](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile445.png>)

The proof of the stability theorem, Theorem 1.5, is similar to the proof of Theorem 1.4, so we conﬁne ourselves to a sketch. Suppose that Γ is a (p,β)-jumbled graph on n vertices, where β ≤ cpd2(H)+3n, and G is a subgraph of Γ containing 1 − χ(H1)−1 − δ e(Γ) edges. An application of Lemma 8.1 as in the proof above allows us to show that there is a subgraph G′ of G formed by removing at most 4δpn2 edges and a regular partition of G′ into k pieces such that the reduced graph has at least 1 − χ(H1)−1 − 2δ k2 edges. This graph can contain no copies of H - otherwise the original graph would have many copies of H as in the last paragraph above. From the dense version of the stability theorem [82] it follows that if δ is suﬃciently small then we may make R into a (χ(H) − 1)-partite graph by removing at most 16ǫ k2 edges. We imitate this removal process in the graph G′. That is, if we remove edges between vi and vj in R then we remove all of the edges between Vi and Vj in G′. Since the number of edges between Vi and Vj is at most 2p|Vi||Vj|, we will remove at most

![image 446](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile446.png>)

![image 447](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile447.png>)

![image 448](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile448.png>)

![image 449](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile449.png>)

ǫ 2

n k

ǫ 16

2

k22p

pn2

≤

![image 450](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile450.png>)

![image 451](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile451.png>)

![image 452](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile452.png>)

edges in total from G′. Since we have already removed all edges which are contained within any Vi the resulting graph is clearly (χ(H) − 1)-partite. Moreover, the total number of edges removed is

at most 4δpn2 + 2ǫpn2 ≤ ǫpn2, as required.

![image 453](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile453.png>)

![image 454](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile454.png>)

### 8.2 Ramsey’s theorem

In order to prove that the Ramsey property also holds in sparse jumbled graphs, we need the following lemma which says that we may remove a small proportion of edges from any suﬃciently large clique and still maintain the Ramsey property.

- Lemma 8.2. For any graph H and any positive integer r ≥ 2, there exist a,η > 0 such that if n is suﬃciently large and G is any subgraph of Kn of density at least 1 − η, any r-coloring of the edges


- of G will contain at least anv(H) monochromatic copies of H.


Proof. Suppose ﬁrst that the edges of Kn have been r-colored. Ramsey’s theorem together with a standard averaging argument tells us that for n suﬃciently large there exists a0 such that there are at least a0nv(H) monochromatic copies of H. Since G is formed from Kn by removing at most ηn2 edges, this deletion process will force us to delete at most ηnv(H) copies of H. Therefore, provided that η ≤ a20, the result follows with a = a20.

![image 455](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile455.png>)

![image 456](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile456.png>)

![image 457](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile457.png>)

![image 458](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile458.png>)

![image 459](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile459.png>)

![image 460](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile460.png>)

We also need a slight variant of the sparse regularity lemma, Theorem 1.11, which allows us to take a regular partition which works for more than one graph.

- Lemma 8.3. For every ǫ > 0 and integers ℓ,m0 ≥ 1, there exist η > 0 and a positive integer M such that if Γ is a (p,ηpn)-jumbled graph on n vertices and G1,G2,... Gℓ is a collection of weighted subgraphs of Γ then there is an equitable partition into m0 ≤ k ≤ M pieces such that for each Gi,

1 ≤ i ≤ ℓ, all but at most ǫk2 pairs of vertex subsets (Va,Vb)Gi satisfy DISC(qab(i),p,ǫ) for some qab(i). There is also an appropriate analogue of Lemma 8.1 to go with this regularity lemma.

- Lemma 8.4. For every ǫ,α > 0 and positive integer m, there exist c > 0 and a positive integer M such that if Γ is a (p,cpn)-jumbled graph on n vertices then any collection of subgraphs


G1,G2,... ,Gℓ of Γ will be such that there are subgraphs G′i of Gi with e(G′i) ≥ e(Gi) − 4αe(Γ) and an equitable partition of the vertex set into k pieces V1,V2,... ,Vk with m ≤ k ≤ M such that the following conditions hold.

- 1. There are no edges of G′i within Va for any 1 ≤ i ≤ ℓ and any 1 ≤ a ≤ k.
- 2. Every subgraph (Va,Vb)G′


(Va,Vb) = qab(i) ≥ αp and satisﬁes DISC(qab(i),p,ǫ).

containing any edges from G′i has dG′

i

i

The proof of the sparse analogue of Ramsey’s theorem now follows along the lines of the proof of Theorem 1.4 above. Theorem 1.6 For every graph H and every positive integer r ≥ 2, there exists c > 0 such that if β ≤ cpd2(H)+3n then any (p,β)-jumbled graph on n vertices is (H,r)-Ramsey.

Proof. Suppose that H has vertex set {1,2,... ,m}, Γ is a (p,β)-jumbled graph on n vertices, where β ≤ cpd2(H)+3n, and G1,G2,... ,Gr are subgraphs of Γ where Gi is the subgraph whose edges have been colored in color i.

Let a,η be the constants given by Lemma 8.2. That is, for n ≥ n0, any subgraph of Kn of density at least 1−η is such that any r-coloring of its edges contains at least anv(H) monochromatic

copies of H. We will need to apply the one-sided counting lemma, Theorem 1.14, with α = 8ηr and θ. We get constants c0 and ǫ0 > 0 such that if Γ is (p,c0pd2(H)+3 |Xi||Xj|)-jumbled and G satisﬁes DISC(qij,p,ǫ0), where αp ≤ qij ≤ p, between sets Xi and Xj for every 1 ≤ i < j ≤ m with ij ∈ E(H), then G(H) ≥ (1 − θ)q(H).

![image 461](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile461.png>)

![image 462](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile462.png>)

We apply Lemma 8.4 to the collection Gi with α = 8ηr, ǫ0 and m = n0. This yields c1 > 0 and a positive integer M such that if Γ is (p,c1pn)-jumbled then there is a collection of graphs G′i such that e(G′i) ≥ e(Gi) − 4αe(Γ) and every subgraph (Va,Vb)G′

![image 463](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile463.png>)

containing any edges from G′i has dG′

i

(Va,Vb) = qab(i) ≥ αp and satisﬁes DISC(qab(i),p,ǫ). Adding over all r graphs, we will have removed at most 4rαe(Γ) = η2e(Γ) edges. Let G′ be the union of the G′i. This graph has density at least 1 − η2 in Γ.

i

![image 464](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile464.png>)

![image 465](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile465.png>)

We now consider the colored reduced (multi)graph R, considering each piece Va of the partition

- as a vertex va and placing an edge of color i between va and vb if the graph between Va and Vb contains an edge of color i. Since Γ is (p,cpn)-jumbled and n ≤ 2M|Vi|, the number of edges between any two pieces diﬀers from p|Vi||Vj| by at most cpn2 ≤ 20η p|Vi||Vj| provided that c ≤ 80Mη 2.


![image 466](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile466.png>)

![image 467](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile467.png>)

Note, moreover, that |Vi| ≤ ⌈nk⌉ ≤ (1 + 20η )nk provided that n ≥ 20ηM . Therefore, the number of edges in the reduced graph R is at least

![image 468](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile468.png>)

![image 469](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile469.png>)

![image 470](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile470.png>)

![image 471](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile471.png>)

(1 − η2)e(Γ) (1 + 20η )3p(nk)2 ≥ (1 − η)

e(G′) (1 + 20η )p⌈nk⌉2

k 2

![image 472](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile472.png>)

≥

e(R) ≥

,

![image 473](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile473.png>)

![image 474](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile474.png>)

![image 475](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile475.png>)

![image 476](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile476.png>)

![image 477](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile477.png>)

![image 478](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile478.png>)

where the ﬁnal step follows from e(Γ) ≥ (1 − 20η )p n2 .

![image 479](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile479.png>)

We now apply Lemma 8.2 to the reduced graph. Since k ≥ m = n0, there exists a monochromatic copy of H in the reduced graph, in color i, say. But if this is the case then we have a collection of vertex subsets X1,... ,Xm such that, for every edge ab ∈ E(H), the induced subgraph (Xa,Xb)G′

(Xa,Xb) = qab(i) ≥ αp and satisﬁes DISC(qab(i),p,ǫ0). By the counting lemma, provided c ≤ 2cM0 , we have G(H) ≥ G′i(H) ≥ (1 − θ)(αp)e(H)(2M)−v(H). Therefore, for c = min(2cM0 ,c1,n−0 1, 80Mη 2), we see that G contains a copy of H.

has dG′

i

i

![image 480](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile480.png>)

![image 481](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile481.png>)

![image 482](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile482.png>)

![image 483](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile483.png>)

![image 484](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile484.png>)

![image 485](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile485.png>)

![image 486](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile486.png>)

### 8.3 Graph removal lemma

We prove that the graph removal lemma also holds in sparse jumbled graphs. The proof is much the same as the proof for Tura´n’s theorem, though we include it for completeness.

- Theorem 1.1 For every graph H and every ǫ > 0, there exist δ > 0 and c > 0 such that if β ≤ cpd2(H)+3n then any (p,β)-jumbled graph Γ on n vertices has the following property. Any subgraph of Γ containing at most δpe(H)nv(H) copies of H may be made H-free by removing at most ǫpn2 edges.


Proof. Suppose that H has vertex set {1,2,... ,m}, Γ is a (p,β)-jumbled graph on n vertices, where β ≤ cpd2(H)+3n, and G is a subgraph of Γ containing at most δpe(H)nv(H) copies of H.

We will need to apply the one-sided counting lemma, Lemma 1.14, with α = 16ǫ and θ = 21. We get constants c0 and ǫ0 > 0 such that if Γ is (p,c0pd2(H)+3 |Xi||Xj|)-jumbled and G satisﬁes DISC(qij,p,ǫ0), where αp ≤ qij ≤ p, between sets Xi and Xj for every 1 ≤ i < j ≤ m with ij ∈ E(H) then G(H) ≥ 21q(H).

![image 487](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile487.png>)

![image 488](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile488.png>)

![image 489](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile489.png>)

![image 490](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile490.png>)

Apply Lemma 8.1 with α = ǫ/16 and ǫ0. This yields constants c1 and M such that if Γ is (p,c1pn)-jumbled then there is a subgraph G′ of G with

e(G′) ≥ e(G) − 4αe(Γ) ≥ e(G) −

ǫ 4

e(Γ) ≥ e(G) − ǫpn2,

![image 491](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile491.png>)

where we used that α = 16ǫ . Moreover, there is an equitable partition into k ≤ M pieces V1,... ,Vk such that every non-empty subgraph (Vi,Vj)G′ has d(Vi,Vj) = qij ≥ αp and satisﬁes DISC(qij,p,ǫ0).

![image 492](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile492.png>)

Suppose now that there is a copy of H left in G′. If this is the case then we have a collection of vertex subsets X1,... ,Xm such that, for every edge ij ∈ E(H), the induced subgraph (Xi,Xj)G′ has dG′(Xi,Xj) = qij ≥ αp and satisﬁes DISC(qij,p,ǫ0). By the counting lemma, provided c ≤

c0

- 2M , we have G(H) ≥ G′(H) ≥ 21(αp)e(H)(2M)−v(H). Therefore, for c = min(2cM0 ,c1) and δ =


![image 493](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile493.png>)

![image 494](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile494.png>)

![image 495](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile495.png>)

- 1

![image 496](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile496.png>)

- 2αe(H)(2M)−v(H), we see that G contains at least δpe(H)nv(H) copies of H, contradicting our assumption about G.


![image 497](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile497.png>)

![image 498](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile498.png>)

![image 499](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile499.png>)

![image 500](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile500.png>)

### 8.4 Removal lemma for groups

We recall the following removal lemma for groups. Its proof is a straightforward adaption of the proof of the dense version given by Kra´l, Serra and Vena [63].

For the rest of this section, let k3 = 3, k4 = 2, km = 1+ m1−3 if m ≥ 5 is odd, and km = 1+ m1−4 if m ≥ 6 is even.

![image 501](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile501.png>)

![image 502](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile502.png>)

- Theorem 1.2 For each ǫ > 0 and positive integer m, there are c,δ > 0 such that the following holds. Suppose B1,... ,Bm are subsets of a group G of order n such that each Bi is (p,β)-jumbled with β ≤ cpkmn. If subsets Ai ⊆ Bi for i = 1,... ,m are such that there are at most δ|B1|··· |Bm|/n solutions to the equation x1x2 ··· xm = 1 with xi ∈ Ai for all i, then it is possible to remove at most ǫ|Bi| elements from each set Ai so as to obtain sets A′i for which there are no solutions to x1x2 ··· xm = 1 with xi ∈ A′i for all i.


We saw above that the one-sided counting lemma gives the graph removal lemma. For cycles, the removal lemma follows from Proposition 7.2. The version we need is stated below.

- Proposition 8.5. For every m ≥ 3 and ǫ > 0, there exist δ > 0 and c > 0 so that any graph


Γ with vertex subsets X1,... ,Xm, each of size n, satisfying (Xi,Xi+1)Γ being (p,β)-jumbled with β ≤ cp1+kmn for each i = 1,... ,m (index taken mod m) has the following property. Any subgraph of Γ containing at most δpmnm copies of Cm may be made Cm-free by removing at most ǫpn2 edges, where we only consider embeddings of Cm into Γ where the i-th vertex of Cm embeds into Xi.

Proof of Theorem 1.2. Let Γ denote the graph with vertex set G×{1,... ,m}, the second coordinate taken modulo m, and with vertex (g,i) colored i. Form an edge from (y,i) to (z,i + 1) in Γ if and only if z = yxi for some xi ∈ Bi, and let G0 be a subgraph of Γ consisting of those edges with xi ∈ Ai. Observe that colored m-cycles in the graph G0 correspond exactly to (m + 1)-tuples (y,x1,x2,... ,xm) with y ∈ G and xi ∈ Ai for each i satisfying x1x2 ... xm = 1. The hypothesis implies that there are at most δ |B1| ··· |Bm| ≤ δ2mpmnm colored m-cycles in the graph G0, where we assumed that c < 21 so that 12pn ≤ |Bi| ≤ 23pn by jumbledness. Then by the cycle removal lemma (Proposition 8.5) we can choose c and δ so that G0 can be made Cm-free by removing at most 2ǫmpn2 edges.

![image 503](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile503.png>)

![image 504](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile504.png>)

![image 505](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile505.png>)

![image 506](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile506.png>)

In Ai, remove the element xi if at least mn edges of the form (y,i)(yxi,i+1) have been removed. Since we removed at most 2ǫmpn2 edges, we remove at most 2ǫpn ≤ ǫ|Bi| elements from each Ai. Let A′i denote the remaining elements of Ai. For any solution to x1x2 ··· xm = 1 for xi ∈ Ai, consider the n edge-disjoint m-cycles (g,1)(gx1,2)(gx1x2,3)··· (gx1 ··· xm,m) in the graph G0 for g ∈ G. We must have removed at least one edge from each of the n cycles, and so we must have removed

![image 507](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile507.png>)

![image 508](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile508.png>)

![image 509](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile509.png>)

- at least mn edges of the form (y,i)(yxi,i + 1) for some i, which implies that xi ∈/ A′i. It follows that there is no solution to x1x2 ··· xm = 1 with xi ∈ Ai for all i.


![image 510](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile510.png>)

![image 511](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile511.png>)

![image 512](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile512.png>)

![image 513](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile513.png>)

![image 514](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile514.png>)

In [63], the authors also proved removal lemmas for systems of equations which are graph

representable. For instance, the system

x1x2x−4 1x−3 1 = 1 x1x2x−5 1 = 1

can be represented by the graph below, in the sense that solutions to the above system correspond to embeddings of this graph into some larger graph with vertex set G × {1,... ,4}, similar to how solutions to x1x2 ··· xn = 1 correspond to cycles in the proof of Theorem 1.2. We refer to the paper [63] for the precise statements. These results can be adapted to the sparse setting in a manner similar to Proposition 8.5.

x1 x2

x5

x3 x4

## 9 Concluding remarks

We conclude with discussions on the sharpness of our results, a sparse extension of quasirandom graphs, induced extensions of the various counting and extremal results, other sparse regularity lemmas, algorithmic applications and sparse Ramsey and Tura´n-type multiplicity results.

### 9.1 Sharpness of results

We have already noted in the introduction that for every H there are (p,β)-jumbled graphs Γ on n vertices, with β = O(pd(H)+2)/4n), such that Γ does not contain a copy of H. On the other hand, the results of Section 6 tell us that we can always ﬁnd copies of H in Γ provided that β ≤ cpd2(H)+1 and in G provided that β ≤ cpd2(H)+3. So, since d2(H) and d(H) diﬀer by at most a constant factor, our results are sharp up to a multiplicative constant in the exponent for all H. However, we believe that our results are likely to be sharp up to an additive constant for the exponent of p in the jumbledness parameter, with some caveats.

An old conjecture of Erd˝os [32] asserts that if H is a d-degenerate bipartite graph then there exists C > 0 such that every graph G on n vertices with at least Cn2−d1 edges contains a copy of H. This conjecture is known to hold for some bipartite graphs such as Kt,t but remains open in general. The best result to date, due to Alon, Krivelevich and Sudakov [7], states that if G has Cn2−41d edges then it contains a copy of H.

![image 515](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile515.png>)

![image 516](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile516.png>)

If Erd˝os’ conjecture is true then this would mean that copies of bipartite H begin to appear already when the density is around n−1/d(H), without any need for a jumbledness condition. If d2(H) = d(H)− 12 then, even for optimally jumbled graphs, our results only apply down to densities of about n−1/(2d(H)−1).

![image 517](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile517.png>)

However, we considered embeddings of H into Γ such that each vertex {1,2,... ,m} of H is to be embedded into a separate vertex subset Xi. We believe that in this setting our results are indeed sharp up to an additive constant, even in the case H is bipartite. Without this caveat of embedding each vertex of H into a separate vertex subset in Γ, we still believe that our results should be sharp for many classes of graphs. In particular, we believe the conjecture [38, 64, 84] that there is a (p,cpt−1n)-jumbled graph which does not contain a copy of Kt.

One thing which we have left undecided is whether the jumbledness condition for appearance of copies of H in regular subgraphs G of Γ should be the same as that for the appearance of copies

- of H in Γ alone. For this question, it is natural to consider the case of triangles where we know that there are (p,cp2n)-jumbled graphs on n vertices which do not contain any triangles. That is, we know the embedding result for Γ is best possible. The result of Sudakov, Szabo´ and Vu [84] mentioned in the introduction also gives us a sharp result for the (K3,ǫ)-Tura´n property. In the next subsection, we will obtain a similar sharp bound for the (K3,2)-Ramsey property.


While these Tura´n and Ramsey-type results are suggestive, we believe that the jumbledness condition for counting in G should be stronger than that for counting in Γ. The fact that the results mentioned above are sharp is because there are alternative proofs of Tura´n’s theorem for cliques and Ramsey’s theorem for the triangle which only need counting results in Γ rather than within some regular subgraph G. Such a workaround seems unlikely to work for the triangle removal lemma. Kohayakawa, Ro¨dl, Schacht and Skokan [59] conjecture that the jumbledness condition in the sparse triangle removal lemma, Theorem 1.2, can be improved from β = o(p3n) to β = o(p2n). We conjecture that the contrary holds.

### 9.2 Relative quasirandomness

The study of quasirandom graphs began in the pioneering work of Thomason [88, 89] and Chung, Graham, and Wilson [19]. As brieﬂy discussed in Section 1.1, they showed that a large number of interesting graph properties satisﬁed by random graphs are all equivalent. Perhaps the most surprising aspect of this work is that if the number of cycles of length 4 in a graph is as one would expect in a binomial random graph of the same density, then this is enough to imply that the edges are very well-spread and the number of copies of any ﬁxed graph is as one would expect in a binomial random graph of the same density.

There has been a considerable amount of research aimed at extending quasirandomness to sparse graphs, see [17, 18, 56, 61]. However, the key property of counting small subgraphs was missing from previous results in this area. The following theorem extends the fundamental results in this area to the setting of subgraphs of (possibly sparse) pseudorandom graphs. The case p = 1 and Γ is the complete graph corresponds to the original setting. We prove that the natural analogues of the original quasirandom properties in this more general setting are all equivalent. Of particular note is the inclusion of the count of small subgraphs, a key property missing from previous results in this area. The proof of some of the implications extend easily from the dense case. However, to imply the notable counting properties, we use the counting lemma, Theorem 1.12, which acts as a transference principle from the sparse setting to the dense setting.

Such quasirandomness of a structure within a sparse but pseudorandom structure is known as relative quasirandomness. This concept has been instrumental in the development of the hypergraph regularity and counting lemma [48, 69, 77, 87]. In the 3-uniform case, for example, one repeatedly has to deal with 3-uniform hypergraphs which are subsets of the triangles of a very pseudorandom graph.

To keep the theorem statement simple, we ﬁrst describe some notation. The co-degree dG(v,v′) of two vertices v,v′ in a graph G is the number of vertices which are adjacent to both v and v′. For a graph H, we let s(H) = min ∆(L(H2 ))+4, d(L(H2))+6 . For a graph H and another graph G, let NH(G) denote the number of labeled copies of H (as a subgraph) in G.

![image 518](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile518.png>)

![image 519](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile519.png>)

Theorem 9.1. Let k ≥ 2 be a positive integer. For n ≥ 1, let Γ = Γn be a (p,β)-jumbled graph on n vertices with p = p(Γ) and β = β(Γ) = o(pkn), and G = Gn be a spanning subgraph of Γn. The following are equivalent.

- P1: For all vertex subsets S and T, |eG(S,T) − q|S||T|| = o(pn2).


- P2: For all vertex subsets S, eG(S) − q|S|2

![image 520](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile520.png>)

2

= o(pn2).

- P3: For all vertex subsets S with |S| = ⌊n2⌋,

![image 521](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile521.png>)

eG(S) − q

n2 8

![image 522](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile522.png>)

= o(pn2).

- P4: For each graph H with k ≥ s(H), NH(G) = qe(H)nv(H) + o(pe(H)nv(H)).
- P5: e(G) ≥ qn22 + o(pn2) and NC4(G) ≤ q4n4 + o(p4n4).

![image 523](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile523.png>)

- P6: e(G) ≥ (1 + o(1))qn22 , λ1 = (1 + o(1))qn, and λ2 = o(pn), where λi is the ith largest eigenvalue, in absolute value, of the adjacency matrix of G.

![image 524](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile524.png>)

- P7:


|dG(v,v′) − q2n| = o(p2n3).

v,v′∈V (G)

We brieﬂy describe how to prove the equivalences between the various properties in Theorem 9.1, with a ﬂow chart shown below.

P4

P3 P2 P1

P5 P6

P7

The equivalence between the discrepancy properties P1, P2, P3 is fairly straightforward and similar to the dense case. Theorem 1.12 shows that P1 implies P4. As P5 is a special case of P4, we have that P4 implies P5. Proposition 5.4 shows that P5 implies P1. The fact P5 implies P6 follows easily from the identity that the trace of the fourth power of the adjacency matrix of G is both the number of closed walks in G of length 4, and the sum of the fourth powers of the eigenvalues of the adjacency matrix of G. The fact that P6 implies P1 is the standard proof of the expander mixing lemma. The fact P5 implies P7 follows easily from the identity

NC4(G) = 4

v,v′∈V (G)

dG(v,v′) 2

, (14)

where the sum is over all n2 pairs of distinct vertices, as well as the identity

dG(v,v′) =

v,v′

v

dG(v) 2

,

and two applications of the Cauchy-Schwarz inequality. Finally, we have P7 implies P5 for the following reason. From (14), we have P5 is equivalent to

dG(v,v′)2 =

v,v′

- 1

![image 525](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile525.png>)

- 2


q4n4 + o(p4n4). (15)

To verify (15), we split up the sum on the left into three sums. The ﬁrst sum is over pairs v,v′ with |dG(v,v′) − q2n| = o(p2n), the second sum is over pairs v,v′ with dG(v,v′) > 2p2n, and the third sum is over the remaining pairs v,v′. From P7, almost all pairs v,v′ of vertices satisfy |dG(v,v′) − q2n| = o(p2n), and so the ﬁrst sum is 21q4n4 + o(p4n4). The second sum satisﬁes

![image 526](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile526.png>)

dG(v,v′)2 ≤

dΓ(v,v′)2 = o(p4n4),

v,v′:dG(v,v′)>2p2n

v,v′:dΓ(v,v′)>2p2n

where the ﬁrst inequality follows from G is a subgraph of Γ, and the second inequality follows from pseudorandomness in Γ. Finally, as P7 implies there are o(n2) pairs v,v′ not satisfying |dG(v,v′) − q2n| = o(p2n), and the terms in the third sum are at most 2p2n, the third sum is o(p4n4). This completes the proof sketch of the equivalences between the various properties in

- Theorem 9.1.

9.3 Induced extensions of counting lemmas and extremal results

With not much extra eﬀort, we can establish induced versions of the various counting lemmas and extremal results for graphs. We assume that we are in Setup 4.1 with the additional condition that, in Setup 3.1, the graph Γ satisﬁes the jumbledness condition for all pairs ab of vertices and not just the sparse edges of H. Deﬁne a strongly induced copy of H in G to be a copy of H in G such that the nonedges of the copy of H are nonedges of Γ. Since G is a subgraph of Γ, a strongly induced copy of H is an induced copy of H. Deﬁne

G∗(H) :=

x1∈X1,...,xm∈Xm (i,j)∈E(H)

G(xi,xj)

(i,j) ∈E(H)

(1 − Γ(xi,xj)) dx1 ··· dxm

and

q∗(H) :=

(i,j)∈E(H)

qij

(i,j) ∈E(H)

(1 − pij)

Note that G∗(H) is the probability that a random compatible map forms a strongly induced copy of H, and q∗(H) is the idealized version. Also note that if Γ is (p,β)-jumbled, then its complement Γ¯ is (1−p,β)-jumbled. Hence, for p small, we expect that most copies of H guaranteed by Theorem 1.14 are strongly induced. This is formalized in the following theorem, which is an induced analogue of the one-sided counting lemma, Theorem 1.14.

- Theorem 9.2. For every ﬁxed graph H on vertex set {1,2,... ,m} and every θ > 0, there exist constants c > 0 and ǫ > 0 such that the following holds.


Let Γ be a graph with vertex sets X1,... ,Xm and suppose that p ≤ m1 and the bipartite graph (Xi,Xj)Γ is (p,cpd(H)+52 |Xi||Xj|)-jumbled for every i < j. Let G be a subgraph of Γ, with the vertex i of H assigned to the vertex set Xi of G. For each edge ij in H, assume that (Xi,Xj)G satisﬁes DISC(qij,p,ǫ). Then

![image 527](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile527.png>)

![image 528](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile528.png>)

![image 529](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile529.png>)

G∗(H) ≥ (1 − θ)q∗(H).

We next discuss how the proof of Theorem 9.2 is a minor modiﬁcation of the proof of Theorem 1.14. As in the proof of Theorem 1.14, after j − 1 steps in the embedding, we have picked f(v1),... ,f(vj−1) and have subsets T(i,j − 1) ⊂ Xi for j ≤ i ≤ m which consist of the possible vertices for f(vi) given the choice of the ﬁrst j − 1 embedded vertices. We are left with the task of picking a good set W(j) ⊂ T(j,j − 1) of possible vertices w = f(vj) to continue the embedding with the desired properties. We will guarantee, in addition to the three properties stated there (which may be maintained since d2(H) + 3 ≤ d(H) + 52), that

![image 530](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile530.png>)

√c)|T(i,j − 1)| for each i > j which is not adjacent to j.

4. |NΓ¯(w) ∩ T(i,j − 1)| ≥ (1 − p −

![image 531](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile531.png>)

As for each such i, if w is chosen for f(vj), T(i,j) = NΓ¯(w) ∩ T(i,j − 1), this will guarantee that |T(i,j)| ≥ (1 − p −

√c)|T(i,j − 1)|. As for each such i, the set T(i,j) is only slightly smaller than T(i,j − 1), this will aﬀect the discrepancy between each pair of sets by at most a factor (1−p−

![image 532](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile532.png>)

√c)2. This additional fourth property makes the set W(j) only slightly smaller. Indeed, to guarantee this property, we need that for each of the nonneighbors i > j of j, the vertices w with fewer than (1−p−

![image 533](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile533.png>)

√c)|T(i,j−1)| nonneighbors in T(i,j−1) in graph Γ¯ are not in W(j), and there are at most c|T(i,jβ2−1)| such vertices for each i by Lemma 3.7. As there are at most m choices of i, and |T(i,j − 1)| ≥ 1 − θj6−1 q(i,j − 1)|Xi|, we get that satisfying this additional fourth property requires that the number of additional vertices deleted to obtain W(j) is at most

![image 534](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile534.png>)

![image 535](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile535.png>)

![image 536](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile536.png>)

β2 c|T(i,j − 1)|

m

![image 537](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile537.png>)

mcp2d(H)+5 1 − θj6−1 q(i,j − 1)

|Xj| ≤

≤

![image 538](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile538.png>)

![image 539](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile539.png>)

mcp2d(H)+5 1 − θj6−1

|T(j,j − 1)|,

![image 540](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile540.png>)

2

q(i,j − 1)q(j,j − 1)

![image 541](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile541.png>)

which is neglible since both q(i,j −1) and q(j,j −1) are at most pd(H). We therefore see that, after changing the various parameters in the proof of Theorem 1.14 slightly, the simple modiﬁcation of the proof sketched above completes the proof of Theorem 9.2. We remark that the assumption p ≤ m1 can be replaced by p is bounded away from 1, which is needed as we must guarantee that the nonedges of the induced copy of H must be nonedges of Γ. We also note that the exponent of p in the jumbledness assumption in Theorem 9.2 is d(H) + 25 and not d2(H) + 3 for the following reason. In addition to using the inheritance of regularity to get that edges of H map to edges of G in the strongly induced copies of H we are counting, we also use jumbledness of Γ¯ to get that the nonedges of H map to nonedges of Γ.

![image 542](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile542.png>)

![image 543](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile543.png>)

In the greedy proof sketched above, to conclude that the good set W(j) ⊂ T(j,j −1) of possible vertices w = f(vj) is large, we use the jumbledness of Γ¯ and that, for the vertices i > j not adjacent to j, the product |T(j,j − 1)||T(i,j − 1)| is large. The sizes of these sets are related to the number of neighbors of j less than j and the number of neighbors of i less j, respectively.

The induced graph removal lemma was proved by Alon, Fischer, Krivelevich, and Szegedy [5]. It states that for each graph H and ǫ > 0 there is δ > 0 such that every graph on n vertices with at most δnv(H) induced copies of H can be made induced H-free by adding or deleting at most ǫn2 edges. This clearly extends the original graph removal lemma. To prove the induced graph removal lemma, they developed the strong regularity lemma, whose proof involves iterating Szemere´di’s regularity lemma many times. A new proof of the induced graph removal lemma which gives an improved quantitative estimate was recently obtained in [23].

The ﬁrst application of Theorem 9.2 we discuss is an induced extension of the sparse graph removal, Theorem 1.1. It does not imply the induced graph removal lemma above.

- Theorem 9.3. For every graph H and every ǫ > 0, there exist δ > 0 and c > 0 such that if β ≤ cpd(H)+52n then any (p,β)-jumbled graph Γ on n vertices with p ≤ v(1H) has the following


![image 544](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile544.png>)

![image 545](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile545.png>)

property. Any subgraph of Γ containing at most δpe(H)nv(H) (strongly) induced copies of H may be made H-free by removing at most ǫpn2 edges.

The proof of Theorem 9.3 is the same as the proof of Theorem 1.1, except we replace the one-sided counting lemma, Theorem 1.14, with its induced variant, Theorem 9.2. Note that unlike the standard induced graph removal lemma, here it suﬃces only to delete edges. Furthermore, all copies of H, not just induced copies, are removed by the deletion of few edges.

The induced Ramsey number rind(H;r) is the smallest natural number N for which there is a graph G on N vertices such that in every r-coloring of the edges of G there is an induced monochromatic copy of H. The existence of these numbers was independently proven in the early 1970s by Deuber [27], Erd˝os, Hajnal and Posa [34], and Ro¨dl [74]. The bounds that these original proofs give on rind(H,r) are enormous. However, Trotter conjectured that the induced Ramsey number of bounded degree graphs is at most polynomial in the number of vertices. That is, for each ∆ there is c(∆) such that rind(H;2) ≤ nc(∆). This was proved by  Luczak and Ro¨dl [68], who gave an enormous upper bound on c(∆), namely, a tower of twos of height O(∆2). More recently, Fox and Sudakov [39] proved an upper bound on c(∆) which is O(∆log ∆). These results giving a polynomial bound on the induced Ramsey number of graphs of bounded degree do not appear to extend to more than two colors.

A graph G is induced Ramsey (∆,n,r)-universal if, for every r-edge-coloring of G, there is a color for which there is a monochromatic induced copy in that color of every graph on n vertices with maximum degree ∆. Clearly, if G is induced Ramsey (∆,n,r)-universal, then rind(H;r) ≤ |G| for every graph H on n vertices with maximum degree ∆.

- Theorem 9.4. For each ∆ and r there is C = C(∆,r) such that for every n there is an induced Ramsey (∆,n,r)-universal graph on at most Cn2∆+8 vertices.


The exponent of n in the above result is best possible up to a multiplicative factor. This is because even for the much weaker condition that G contains an induced copy of all graphs on n vertices with maximum degree ∆, the number of vertices of G has to be Ω(n∆/2) (see, e.g., [14]).

We have the following immediate corollary of Theorem 9.4, improving the bound for induced Ramsey numbers of bounded degree graphs. It is also the ﬁrst polynomial upper bound which works for more than two colors.

Corollary 9.5. For each ∆ and r there is C = C(∆,r) such that rind(H;r) ≤ Cn2∆+8 for every n-vertex graph H of maximum degree ∆.

We next sketch the proof of Theorem 9.4. The proof builds on ideas used in the proof of Chvatal, Ro¨dl, Szemere´di, and Trotter [20] that Ramsey numbers of bounded degree graphs grow linearly in the number of vertices. We claim that any graph G on N = Cn2∆+8 vertices which is (p,β)-jumbled with p = n1 and β = O(√pN) is the desired induced Ramsey (∆,n,r)-universal graph. Such a graph exists as almost surely G(N,p) has this jumbledness property. Note that β = cpd(H)+52N with c = O(p2). We consider an r-coloring of the edges of G and apply the multicolor sparse regularity lemma so that each color satisﬁes a discrepancy condition between almost all pairs of parts. Using Tura´n’s theorem and Ramsey’s theorem in the reduced graph, we ﬁnd ∆ + 1 parts X1,... ,X∆+1, each pair of which has density at least 2pr in the same color, say red, and satisﬁes a discrepancy condition. Let H be a graph on n vertices with maximum degree ∆, so H has chromatic number at most ∆ + 1. Assign each vertex a of H to some part so that the vertices assigned to each part form an independent set in H. We then use the induced counting lemma, Theorem 9.2, to get an induced monochromatic red copy of H. We make a couple of observations which are vital for this proof to work, and one must look closely into the proof

![image 546](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile546.png>)

![image 547](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile547.png>)

![image 548](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile548.png>)

![image 549](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile549.png>)

of the induced counting lemma to verify these claims. First, we can choose the constants in the regularity lemma and the counting lemma so that they only depend on the maximum degree ∆ and the number of colors r and not on the number n of vertices. Indeed, in addition to the at most 2∆ times that we apply inheritance of regularity, the discrepancy-parameter increases by a factor of at most (1 − p −

√c)−2n = (1 − O(p))−2n = (1 − O(n1))−2n = O(1) due to the restrictions imposed by the non-edges of H. So we lose a total of at most a constant factor in the discrepancy, which does not aﬀect the outcome. Second, as we assigned some vertices of H to the same part, they may get embedded to the same vertex. However, one easily checks that almost all the embeddings of H in the proof of the induced counting lemma are one-to-one, and hence there is a monochromatic induced copy of H. Indeed, as there are less than n vertices which are previously embedded at each step of the proof of the induced counting lemma, and W(j) ≫ n, then there is always a vertex w ∈ W(j) to pick for f(vj) to continue the embedding. This completes the proof sketch.

![image 550](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile550.png>)

![image 551](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile551.png>)

In the proof sketched above, the use of the sparse regularity lemma forces an enormous upper bound on C(∆,r), of tower-type. However, all we needed was ∆ + 1 parts such that the graph between each pair of parts has density at least 2pr in the same color and satisﬁes a discrepancy condition. To guarantee this, one does not need the full strength of the regularity lemma, and the sparse version of the Duke-Lefmann-R¨dl weak regularity lemma discussed in Subsection 9.4 is suﬃcient. This gives a better bound on C(∆,r), which is an exponential-tower of constant height.

![image 552](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile552.png>)

The last application we mention is an induced extension of the sparse Erd˝os-Stone-Simonovits theorem, Theorem 1.4. We say that a graph Γ is induced (H,ǫ)-Tura´n if any subgraph of Γ with at least (1 − χ(H1)−1 + ǫ)e(Γ) edges contains a strongly induced copy of H.

![image 553](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile553.png>)

Theorem 9.6. For every graph H and every ǫ > 0, there exists c > 0 such that if β ≤ cpd(H)+52n then any (p,β)-jumbled graph on n vertices with p ≤ v(1H) is induced (H,ǫ)-Tura´n.

![image 554](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile554.png>)

![image 555](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile555.png>)

The proof of Theorem 9.6 is the same as the proof of Theorem 1.4, except we replace the one-sided counting lemma, Theorem 1.14, with its induced variant, Theorem 9.2.

### 9.4 Other sparse regularity lemmas

The sparse regularity lemma, in the form due to Scott [80], states that for every ǫ > 0 and positive integer m, there exists a positive integer M such that every graph G has an equitable partition into k pieces V1,V2,... ,Vk with m ≤ k ≤ M such that all but ǫk2 pairs (Vi,Vj)G satisfy DISC(pij,pij,ǫ) for some pij. The additional condition of jumbledness which we imposed in our regularity lemma, Theorem 1.11, was there so as to force all of the pij to be p. If this were not the case, it could easily be that all of the edges of the graph bunch up within a particular bad pair, so the result would tell us nothing.

In our results, we made repeated use of sparse regularity. While convenient, this does have its limitations. In particular, the bounds which the regularity lemma gives on the number of pieces M in the regular partition is (and is necessarily [23, 46]) of tower-type in ǫ. This means that the constants c−1 which this method produces for Theorems 1.1, 1.4, 1.6, and 1.5 are also of tower-type.

In the dense setting, there are other sparse regularity lemmas which prove suﬃcient for many of our applications. One such example is the cylinder regularity lemma of Duke, Lefmann and Ro¨dl [29]. This lemma says that for a k-partite graph, between sets V1,V2,... ,Vk, there is an ǫ-regular partition of the cylinder V1×···×Vk into a relatively small number of cylinders K = W1×···×Wk, with Wi ⊆ Vi for 1 ≤ i ≤ k. The deﬁnition of an ǫ-regular partition here is that all but an ǫ-fraction of the k-tuples (v1,... ,vk) ∈ V1 ×···×Vk are in ǫ-regular cylinders, where a cylinder W1 ×···×Wk is ǫ-regular if all k2 pairs (Wi,Wj), 1 ≤ i < j ≤ k, are ǫ-regular in the usual sense.

For sparse graphs, a similar theorem may be proven by appropriately adapting the proof of Duke, Lefmann and Ro¨dl using the ideas of Scott. Consider a k-partite graph, between sets V1,V2,... ,Vk. We will say that a cylinder K = W1×···×Wk, with Wi ⊆ Vi for 1 ≤ i ≤ k, satisﬁes DISC(qK,pK,ǫ) with qK = (qij)1≤i<j≤k and pK = (pij)1≤i<j≤k if all k2 pairs (Wi,Wj), 1 ≤ i < j ≤ k, satisfy DISC(qij,pij,ǫ). The sparse version of the cylinder regularity lemma is now as follows.

- Proposition 9.7. For every ǫ > 0 and positive integer k, there exists γ > 0 such that if G = (V,E) is a k-partite graph with k-partition V = V1 ∪ ··· ∪ Vk then there exists an ǫ-regular partition K of V1 × ··· × Vk into at most γ−1 cylinders such that, for each K ∈ K with K = W1 × ··· × Wk and 1 ≤ i ≤ k, |Wi| ≥ γ|Vi|.


The constant γ is at most exponential in a power of kǫ−1. Moreover, this theorem is suﬃcient for our applications to Tura´n’s theorem and Ramsey’s theorem. This results in constants c−1 which are at most double exponential in the parameters |H|, ǫ and r for Theorems 1.4 and 1.6.

For the graph removal lemma, we may also make some improvement, but it is of a less dramatic nature. As in the dense case [37], it shows that in Theorem 1.1 we may take δ−1 and c−1 to be a tower of twos of height logarithmic in ǫ−1. The proof essentially transfers to the sparse case using the sparse counting lemma, Theorem 1.14.

### 9.5 Algorithmic applications

The algorithmic versions of Szemere´di’s regularity lemma and its variants have applications to fundamental algorithmic problems such as max-cut, max k-sat, and property testing (see [9] and its references). The result of Alon and Naor [8] approximating the cut-norm of a graph via Grothendieck’s inequality allows one to obtain algorithmic versions of Szemeredi’s regularity lemma [3], the FriezeKannan weak regularity lemma [21], and the Duke-Lefmann-R¨odl weak regularity lemma. Many of these algorithmic applications can be transferred to the sparse setting using algorithmic versions of the sparse regularity lemmas, allowing one to substantially improve the error approximation in this setting. Our new counting lemmas allows for further sparse extensions. We describe one such extension below.

Suppose we are given a graph H on h vertices, and we want to compute the number of copies of H in a graph G on n vertices. The brute force approach considers all possible h-tuples of vertices and computes the desired number in time O(nh). The Duke-Lefmann-R¨dl regularity lemma was originally introduced in order to obtain a much faster algorithm, which runs in polynomial time with an absolute constant exponent, at the expense of some error. More precisely, for each ǫ > 0, they found an algorithm which, given a graph on n vertices, runs in polynomial time and approximates the number of copies of H as a subgraph to within ǫnh. The running time is of the form C(h,ǫ)nc, where c is an absolute constant and C(h,ǫ) is exponential in a power of hǫ−1. We have the following extension of this result to the sparse setting. The proof transfers from the dense setting using the algorithmic version of the sparse Duke-Lefmann-R¨dl regularity lemma, Proposition 9.7, and the

sparse counting lemma, Theorem 1.12. For a graph H, we let s(H) = min ∆(L(H2 ))+4, d(L(H2))+6 . Proposition 9.8. Let H be a graph on h vertices with s(H) ≤ k and ǫ > 0. There is an absolute constant c and another constant C = C(ǫ,h) depending only exponentially on hǫ−1 such that the following holds. Given a graph G on n vertices which is known to be a spanning subgraph of a (p,β)-pseudorandom graph with β ≤ C−1pkn, the number of copies of H in G can be computed up to an error ǫpe(H)nv(H) in running time Cnc.

![image 556](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile556.png>)

![image 557](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile557.png>)

### 9.6 Multiplicity results

There are many problems and results in graph Ramsey theory and extremal graph theory on the multiplicity of subgraphs. These results can be naturally extended to sparse pseudorandom graphs using the tools developed in this paper. Indeed, by applying the sparse regularity lemma and the new counting lemmas, we get extensions of these results to sparse graphs. In this subsection, we discuss a few of these results.

Recall that Ramsey’s theorem states that every 2-edge-coloring of a suﬃciently large complete graph Kn contains at least one monochromatic copy of a given graph H. Let cH,n denote the fraction of copies of H in Kn that must be monochromatic in any 2-edge-coloring of G. By an averaging argument, cH,n is a bounded, monotone increasing function in n, and therefore has a positive limit cH as n → ∞. The constant cH is known as the Ramsey multiplicity constant for the graph H. It is simple to show that cH ≤ 21−m for a graph H with m = e(H) edges, where this bound comes from considering a random 2-edge-coloring of Kn with each coloring equally likely.

Erd˝os [31] and, in a more general form, Burr and Rosta [13] suggested that the Ramsey multiplicity constant is achieved by a random coloring. These conjectures are false as was demonstrated by Thomason [90] even for H being any complete graph Kt with t ≥ 4. Moreover, as shown in [36], there are graphs H with m edges and cH ≤ m−m/2+o(m), which demonstrates that the random coloring is far from being optimal for some graphs.

For bipartite graphs the situation seems to be very diﬀerent. The edge density of a graph is the fraction of pairs of vertices that are edges. The conjectures of Erd˝os-Simonovits [83] and Sidorenko [81] suggest that for any bipartite H the number of copies of H in any graph G on n vertices with edge density p bounded away from 0 is asymptotically at least the same as in the n-vertex random graph with edge density p. This conjecture implies that cH = 21−m if H is bipartite with m edges. The most general results on this problem were obtained in [24] and [65], where it is shown that every bipartite graph H which has a vertex in one part complete to the other part satisﬁes the conjecture.

More generally, let cH,Γ denote the fraction of copies of H in Γ that must be monochromatic in any 2-edge-coloring of Γ. For a graph Γ with n vertices, by averaging over all copies of Γ in Kn, we have cH,Γ ≤ cH,n ≤ cH. It is natural to try to ﬁnd conditions on Γ which imply that cH,Γ is close to cH. The next theorem shows that if Γ is suﬃciently jumbled, then cH,Γ is close to cH. The proof follows by noting that the proportion of monochromatic copies of H in the weighted reduced graph R is at least cH,|R|. This count then transfers back to Γ using the one-sided counting lemma. We omit the details.

- Theorem 9.9. For each ǫ > 0 and graph H, there is c > 0 such that if Γ is a (p,β)-jumbled graph on

n vertices with β ≤ cpd2(H)+3n then every 2-edge-coloring of Γ contains at least (cH − ǫ)pe(H)nv(H) labeled monochromatic copies of H.

Maybe the earliest result on Ramsey multiplicity is Goodman’s theorem [45], which determines cK3,n and, in particular, implies cK3 = 41. The next theorem shows an extension of Goodman’s theorem to pseudorandom graphs, giving an optimal jumbledness condition to imply cH,Γ = 14−o(1).

![image 558](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile558.png>)

![image 559](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile559.png>)

- Theorem 9.10. If Γ is a (p,β)-jumbled graph on n vertices with β ≤ 101 p2n, then every 2-edgecoloring of Γ contains at least (p3 − 10pβn)n243 monochromatic triangles.


![image 560](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile560.png>)

![image 561](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile561.png>)

![image 562](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile562.png>)

The proof of this theorem follows by ﬁrst noting that T = A+2M, where A denotes the number of triangles in Γ, M the number of monochromatic triangles in Γ, and T the number of ordered triples (a,b,c) of vertices of Γ which form a triangle such that (a,b) and (a,c) are the same color.

We then give an upper bound for A and a lower bound for T using the jumbledness conditions and standard inequalities. We omit the precise details.

The previous theorem has the following immediate corollary, giving an optimal jumbledness condition to imply that a graph is (K3,2)-Ramsey. Corollary 9.11. If Γ is a (p,β)-jumbled graph on n vertices with β < 10p2n, then Γ is (K3,2)Ramsey.

![image 563](<2012-conlon-extremal-results-sparse-pseudorandom_images/imageFile563.png>)

Deﬁne the Tura´n multiplicity ρH,d,n to be the minimum, over all graphs G on n vertices with edge density at least d, of the fraction of copies of H in Kn which are also in G. Let ρH,d be the limit of ρH,d,n as n → ∞. This limit exists by an averaging argument. The conjectures of Erd˝osSimonovits [83] and Sidorenko [81] mentioned earlier can be stated as ρH,d = de(H) for bipartite H. Recently, Reiher [73], extending work of Razborov [72] and Nikiforov [70] for t = 3 and 4, determined ρKt,d for all t ≥ 3.

We can similarly extend these results to the sparse setting. Let ρH,d,Γ be the minimum, over all subgraphs G of Γ with at least de(Γ) edges, of the fraction of copies of H in Γ which are also in G. We have the following result, which gives jumbledness conditions on Γ which imply that ρH,d,Γ is close to ρH,d.

Theorem 9.12. For each ǫ > 0 and graph H there is c > 0 such that if Γ is a (p,β)-jumbled graph on n vertices with β ≤ cpd2(H)+3n then every subgraph of Γ with at least de(Γ) edges contains at least (ρH,d − ǫ)pe(H)nv(H) labeled copies of H.

## References

- [1] E. Aigner-Horev, H. H`an, and M. Schacht. Extremal results for odd cycles in sparse pseudorandom graphs. Submitted.
- [2] N. Alon. Explicit Ramsey graphs and orthonormal labelings. Electron. J. Combin., 1:Research Paper 12, approx. 8 pp. (electronic), 1994.
- [3] N. Alon, A. Coja-Oghlan, H. H`an, M. Kang, V. Ro¨dl, and M. Schacht. Quasi-randomness and algorithmic regularity for graphs with general degree distributions. SIAM J. Comput., 39(6):2336–2362, 2010.
- [4] N. Alon, R. A. Duke, H. Lefmann, V. Ro¨dl, and R. Yuster. The algorithmic aspects of the regularity lemma. J. Algorithms, 16(1):80–109, 1994.
- [5] N. Alon, E. Fischer, M. Krivelevich, and M. Szegedy. Eﬃcient testing of large graphs. Combinatorica, 20(4):451–476, 2000.
- [6] N. Alon and N. Kahale. Approximating the independence number via the θ-function. Math. Programming, 80(3, Ser. A):253–264, 1998.
- [7] N. Alon, M. Krivelevich, and B. Sudakov. Tura´n numbers of bipartite graphs and related Ramsey-type questions. Combin. Probab. Comput., 12(5-6):477–494, 2003. Special issue on Ramsey theory.
- [8] N. Alon and A. Naor. Approximating the cut-norm via Grothendieck’s inequality. SIAM J. Comput., 35(4):787–803 (electronic), 2006.


- [9] N. Alon, A. Shapira, and B. Sudakov. Additive approximation for edge-deletion problems. Ann. of Math. (2), 170(1):371–411, 2009.
- [10] J. Balogh, R. Morris, and W. Samotij. Independent sets in hypergraphs. Submitted.
- [11] Y. Bilu and N. Linial. Lifts, discrepancy and nearly optimal spectral gap. Combinatorica, 26(5):495–519, 2006.
- [12] C. Borgs, J. T. Chayes, L. Lov´asz, V. T. So´s, and K. Vesztergombi. Convergent sequences of dense graphs. I. Subgraph frequencies, metric properties and testing. Adv. Math., 219(6):1801– 1851, 2008.
- [13] S. A. Burr and V. Rosta. On the Ramsey multiplicities of graphs—problems and recent results. J. Graph Theory, 4(4):347–361, 1980.
- [14] S. Butler. Induced-universal graphs for graphs with bounded maximum degree. Graphs Combin., 25(4):461–468, 2009.
- [15] F. R. K. Chung. A spectral Tur´an theorem. Combin. Probab. Comput., 14(5-6):755–767, 2005.
- [16] F. R. K. Chung and R. L. Graham. Quasi-random set systems. J. Amer. Math. Soc., 4(1):151– 196, 1991.
- [17] F. R. K. Chung and R. L. Graham. Sparse quasi-random graphs. Combinatorica, 22(2):217– 244, 2002. Special issue: Paul Erd˝os and his mathematics.
- [18] F. R. K. Chung and R. L. Graham. Quasi-random graphs with given degree sequences. Random Structures Algorithms, 32(1):1–19, 2008.
- [19] F. R. K. Chung, R. L. Graham, and R. M. Wilson. Quasi-random graphs. Combinatorica, 9(4):345–362, 1989.
- [20] V. Chvat´l, V. Ro¨dl, E. Szemere´di, and W. T. Trotter, Jr. The Ramsey number of a graph with bounded maximum degree. J. Combin. Theory Ser. B, 34(3):239–243, 1983.
- [21] A. Coja-Oghlan, C. Cooper, and A. Frieze. An eﬃcient sparse regularity concept. In Proceedings of the Twentieth Annual ACM-SIAM Symposium on Discrete Algorithms, pages 207–216, Philadelphia, PA, 2009. SIAM.
- [22] D. Conlon. A new upper bound for diagonal Ramsey numbers. Ann. of Math. (2), 170(2):941– 960, 2009.
- [23] D. Conlon and J. Fox. Bounds for graph regularity and removal lemmas. to appear in GAFA.
- [24] D. Conlon, J. Fox, and B. Sudakov. An approximate version of Sidorenko’s conjecture. Geom. Funct. Anal., 20(6):1354–1366, 2010.
- [25] D. Conlon and W. T. Gowers. Combinatorial theorems in sparse random sets. Submitted.
- [26] D. Conlon, W. T. Gowers, W. Samotij, and M. Schacht. On the K LR conjecture in random graphs. Submitted.
- [27] W. Deuber. Generalizations of Ramsey’s theorem. In Inﬁnite and ﬁnite sets (Colloq., Keszthely, 1973; dedicated to P. Erdo˝s on his 60th birthday), Vol. I, pages 323–332. Colloq. Math. Soc. Ja´nos Bolyai, Vol. 10. North-Holland, Amsterdam, 1975.


- [28] A. Dudek and V. Ro¨dl. On the Folkman number f(2,3,4). Experiment. Math., 17(1):63–67, 2008.
- [29] R. A. Duke, H. Lefmann, and V. Ro¨dl. A fast approximation algorithm for computing the frequencies of subgraphs in a given graph. SIAM J. Comput., 24(3):598–620, 1995.
- [30] P. Erd˝os and A. H. Stone. On the structure of linear graphs. Bull. Amer. Math. Soc., 52:1087– 1091, 1946.
- [31] P. Erd˝os. On the number of complete subgraphs contained in certain graphs. Magyar Tud. Akad. Mat. Kutat´ Int. K¨zl., 7:459–464, 1962.
- [32] P. Erd˝os. Some recent results on extremal problems in graph theory. Results. In Theory of Graphs (Internat. Sympos., Rome, 1966), pages 117–123 (English); pp. 124–130 (French). Gordon and Breach, New York, 1967.
- [33] P. Erd˝os, M. Goldberg, J. Pach, and J. Spencer. Cutting a graph into two dissimilar halves. J. Graph Theory, 12(1):121–131, 1988.
- [34] P. Erd˝os, A. Hajnal, and L. Po´sa. Strong embeddings of graphs into colored graphs. In Inﬁnite and ﬁnite sets (Colloq., Keszthely, 1973; dedicated to P. Erdo˝s on his 60th birthday), Vol. I, pages 585–595. Colloq. Math. Soc. Ja´nos Bolyai, Vol. 10. North-Holland, Amsterdam, 1975.
- [35] P. Erd˝os and J. Spencer. Imbalances in k-colorations. Networks, 1:379–385, 1971/72.
- [36] J. Fox. There exist graphs with super-exponential Ramsey multiplicity constant. J. Graph Theory, 57(2):89–98, 2008.
- [37] J. Fox. A new proof of the graph removal lemma. Ann. of Math. (2), 174(1):561–579, 2011.
- [38] J. Fox, C. Lee, and B. Sudakov. Chromatic number, clique subdivisions, and the conjectures of Haj´os and Erd˝os-Fajtlowicz. Submitted.
- [39] J. Fox and B. Sudakov. Induced Ramsey-type theorems. Adv. Math., 219(6):1771–1800, 2008.
- [40] J. Fox and B. Sudakov. Two remarks on the Burr-Erdo˝s conjecture. European J. Combin., 30(7):1630–1645, 2009.
- [41] E. Friedgut, V. Ro¨dl, and M. Schacht. Ramsey properties of random discrete structures. Random Structures Algorithms, 37(4):407–436, 2010.
- [42] S. Gerke, Y. Kohayakawa, V. Ro¨dl, and A. Steger. Small subsets inherit sparse ǫ-regularity. J. Combin. Theory Ser. B, 97(1):34–56, 2007.
- [43] S. Gerke, M. Marciniszyn, and A. Steger. A probabilistic counting lemma for complete graphs. Random Structures Algorithms, 31(4):517–534, 2007.
- [44] S. Gerke and A. Steger. The sparse regularity lemma and its applications. In Surveys in Combinatorics 2005, volume 327 of London Math. Soc. Lecture Note Ser., pages 227–258. Cambridge Univ. Press, Cambridge, 2005.
- [45] A. W. Goodman. On sets of acquaintances and strangers at any party. Amer. Math. Monthly, 66:778–783, 1959.


- [46] W. T. Gowers. Lower bounds of tower type for Szemere´di’s uniformity lemma. Geom. Funct. Anal., 7(2):322–337, 1997.
- [47] W. T. Gowers. Quasirandomness, counting and regularity for 3-uniform hypergraphs. Combin. Probab. Comput., 15(1-2):143–184, 2006.
- [48] W. T. Gowers. Hypergraph regularity and the multidimensional Szemere´di theorem. Ann. of Math. (2), 166(3):897–946, 2007.
- [49] W. T. Gowers. Quasirandom groups. Combin. Probab. Comput., 17(3):363–387, 2008.
- [50] R. L. Graham, V. Ro¨dl, and A. Rucin´ski. On graphs with linear Ramsey numbers. J. Graph Theory, 35(3):176–192, 2000.
- [51] B. Green. A Szemere´di-type regularity lemma in abelian groups, with applications. Geom. Funct. Anal., 15(2):340–376, 2005.
- [52] B. Green and T. Tao. The primes contain arbitrarily long arithmetic progressions. Ann. of Math. (2), 167(2):481–547, 2008.
- [53] P. E. Haxell, Y. Kohayakawa, and T.  Luczak. Tura´n’s extremal problem in random graphs: forbidding even cycles. J. Combin. Theory Ser. B, 64(2):273–287, 1995.
- [54] Y. Kohayakawa. Szemere´di’s regularity lemma for sparse graphs. In Foundations of computational mathematics (Rio de Janeiro, 1997), pages 216–230. Springer, Berlin, 1997.
- [55] Y. Kohayakawa, T.  Luczak, and V. Ro¨dl. On K4-free subgraphs of random graphs. Combinatorica, 17(2):173–213, 1997.
- [56] Y. Kohayakawa and V. Ro¨dl. Regular pairs in sparse random graphs. I. Random Structures Algorithms, 22(4):359–434, 2003.
- [57] Y. Kohayakawa and V. Ro¨dl. Szemere´di’s regularity lemma and quasi-randomness. In Recent advances in algorithms and combinatorics, volume 11 of CMS Books Math./Ouvrages Math. SMC, pages 289–351. Springer, New York, 2003.
- [58] Y. Kohayakawa, V. Ro¨dl, M. Schacht, P. Sissokho, and J. Skokan. Tura´n’s theorem for pseudorandom graphs. J. Combin. Theory Ser. A, 114(4):631–657, 2007.
- [59] Y. Kohayakawa, V. Ro¨dl, M. Schacht, and J. Skokan. On the triangle removal lemma for subgraphs of sparse pseudorandom graphs. In An Irregular Mind (Szemere´di is 70), volume 21 of Bolyai Soc. Math. Stud., pages 359–404. Springer Berlin, 2010.
- [60] Y. Kohayakawa, V. Ro¨dl, M. Schacht, and E. Szemere´di. Sparse partition universal graphs for graphs of bounded degree. Adv. Math., 226(6):5041–5065, 2011.
- [61] Y. Kohayakawa, V. Ro¨dl, and P. Sissokho. Embedding graphs with bounded degree in sparse pseudorandom graphs. Israel J. Math., 139:93–137, 2004.
- [62] J. Komlo´s and M. Simonovits. Szemere´di’s regularity lemma and its applications in graph theory. In Combinatorics, Paul Erdo˝s is eighty, Vol. 2 (Keszthely, 1993), volume 2 of Bolyai Soc. Math. Stud., pages 295–352. Ja´nos Bolyai Math. Soc., Budapest, 1996.


- [63] D. Kra´l, O. Serra, and L. Vena. A combinatorial proof of the removal lemma for groups. J. Combin. Theory Ser. A, 116(4):971–978, 2009.
- [64] M. Krivelevich and B. Sudakov. Pseudo-random graphs. In More sets, graphs and numbers, volume 15 of Bolyai Soc. Math. Stud., pages 199–262. Springer, Berlin, 2006.
- [65] J. Li and B. Szegedy. On the logarithmic calculus and Sidorenko’s conjecture. Submitted.
- [66] L. Lov´asz and B. Szegedy. Limits of dense graph sequences. J. Combin. Theory Ser. B, 96(6):933–957, 2006.
- [67] L. Lu. Explicit construction of small Folkman graphs. SIAM J. Discrete Math., 21(4):1053– 1060, 2007.
- [68] T.  Luczak and V. Ro¨dl. On induced Ramsey numbers for graphs with bounded maximum degree. J. Combin. Theory Ser. B, 66(2):324–333, 1996.
- [69] B. Nagle, V. Ro¨dl, and M. Schacht. The counting lemma for regular k-uniform hypergraphs. Random Structures Algorithms, 28(2):113–179, 2006.
- [70] V. Nikiforov. The number of cliques in graphs of given order and size. Trans. Amer. Math. Soc., 363(3):1599–1618, 2011.
- [71] F. P. Ramsey. On a problem of formal logic. Proc. London Math. Soc. Ser. 2, 30:264–286, 1930.
- [72] A. A. Razborov. On the minimal density of triangles in graphs. Combin. Probab. Comput., 17(4):603–618, 2008.
- [73] C. Reiher. The clique density theorem. Submitted.
- [74] V. Ro¨dl. The dimension of a graph and generalized ramsey theorems. Master’s thesis, Charles University, 1973.
- [75] V. Ro¨dl and A. Rucin´ski. Threshold functions for Ramsey properties. J. Amer. Math. Soc., 8(4):917–942, 1995.
- [76] V. Ro¨dl and M. Schacht. Regularity lemmas for graphs. In Fete of Combinatorics and Computer Science, volume 20 of Bolyai Soc. Math. Stud., pages 287–325. Ja´nos Bolyai Math. Soc., Budapest, 2010.
- [77] V. Ro¨dl and J. Skokan. Regularity lemma for k-uniform hypergraphs. Random Structures Algorithms, 25(1):1–42, 2004.
- [78] I. Z. Ruzsa and E. Szemere´di. Triple systems with no six points carrying three triangles. In Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Vol. II, volume 18 of Colloq. Math. Soc. J´anos Bolyai, pages 939–945. North-Holland, Amsterdam, 1978.
- [79] M. Schacht. Extremal results for discrete random structures. Submitted.
- [80] A. Scott. Szemere´di’s regularity lemma for matrices and sparse graphs. Combin. Probab. Comput., 20(3):455–466, 2011.
- [81] A. Sidorenko. A correlation inequality for bipartite graphs. Graphs Combin., 9(2):201–204, 1993.


- [82] M. Simonovits. A method for solving extremal problems in graph theory, stability problems. In Theory of Graphs (Proc. Colloq., Tihany, 1966), pages 279–319. Academic Press, New York, 1968.
- [83] M. Simonovits. Extremal graph problems, degenerate extremal problems, and supersaturated graphs. In Progress in graph theory (Waterloo, Ont., 1982), pages 419–437. Academic Press, Toronto, ON, 1984.
- [84] B. Sudakov, T. Szabo´, and V. H. Vu. A generalization of Tur´an’s theorem. J. Graph Theory, 49(3):187–195, 2005.
- [85] E. Szemere´di. On sets of integers containing no k elements in arithmetic progression. Acta Arith., 27:199–245, 1975.
- [86] E. Szemere´di. Regular partitions of graphs. In Proble`mes combinatoires et the´orie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), volume 260 of Colloq. Internat. CNRS, pages 399–401. CNRS, Paris, 1978.
- [87] T. Tao. A variant of the hypergraph removal lemma. J. Combin. Theory Ser. A, 113(7):1257– 1280, 2006.
- [88] A. Thomason. Pseudorandom graphs. In Random graphs ’85 (Poznan´, 1985), volume 144 of North-Holland Math. Stud., pages 307–331. North-Holland, Amsterdam, 1987.
- [89] A. Thomason. Random graphs, strongly regular graphs and pseudorandom graphs. In Surveys in Combinatorics 1987 (New Cross, 1987), volume 123 of London Math. Soc. Lecture Note Ser., pages 173–195. Cambridge Univ. Press, Cambridge, 1987.
- [90] A. Thomason. A disproof of a conjecture of Erd˝os in Ramsey theory. J. London Math. Soc.

(2), 39(2):246–255, 1989.

- [91] P. Tura´n. Eine Extremalaufgabe aus der Graphentheorie. Mat. Fiz. Lapok, 48:436–452, 1941.


