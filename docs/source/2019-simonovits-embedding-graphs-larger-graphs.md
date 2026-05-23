---
type: source
kind: paper
title: "Embedding graphs into larger graphs: results, methods, and problems"
authors: Miklós Simonovits, Endre Szemerédi
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1912.02068v1
source_local: ../raw/2019-simonovits-embedding-graphs-larger-graphs.pdf
topic: general-knowledge
cites:
---

## arXiv:1912.02068v1[math.CO]4Dec2019

### Embedding graphs into larger graphs: results, methods, and problems

Mikl´os Simonovits and Endre Szemer´edi

Alfre´d Re´nyi Institute of Mathematics, Hungarian Academy of Sciences,

email: miki@renyi.hu, szemered@rutgers.edu

# Contents

- 1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 2 The beginnings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

- 2.1 Very early results . . . . . . . . . . . . . . . . . . . . . . . 9
- 2.2 Constructions . . . . . . . . . . . . . . . . . . . . . . . . . 13
- 2.3 Some historical remarks . . . . . . . . . . . . . . . . . . . 13
- 2.4 Early results . . . . . . . . . . . . . . . . . . . . . . . . . 14
- 2.5 Which Universe? . . . . . . . . . . . . . . . . . . . . . . . 16
- 2.6 Ramsey or density? . . . . . . . . . . . . . . . . . . . . . 21
- 2.7 Why are the extremal problems interesting? . . . . . . . . 22
- 2.8 Ramsey Theory and the birth of the Random Graph Method 23
- 2.9 Dichotomy, randomness and matrix graphs . . . . . . . . 24
- 2.10 Ramsey problems similar to extremal problems . . . . . . 25
- 2.11 Applications in Continuous Mathematics . . . . . . . . . 26
- 2.12 The Stability method . . . . . . . . . . . . . . . . . . . . 26
- 2.13 The “typical structure” . . . . . . . . . . . . . . . . . . . 29
- 2.14 Supersaturated Graphs . . . . . . . . . . . . . . . . . . . 31
- 2.15 Lov´asz-Simonovits Stability theorem . . . . . . . . . . . . 32
- 2.16 Degenerate vs Non-degenerate problems . . . . . . . . . . 33
- 2.17 Dirac theorem: introduction . . . . . . . . . . . . . . . . . 36
- 2.18 Equitable Partition . . . . . . . . . . . . . . . . . . . . . . 36
- 2.19 Packing, Covering, Tiling, L-factors . . . . . . . . . . . . 37


- 3 “Classical methods” . . . . . . . . . . . . . . . . . . . . . . . . . 40

- 3.1 Detour I: Induction? . . . . . . . . . . . . . . . . . . . . . 40
- 3.2 Detour II: Applications of Linear Algebra . . . . . . . . . 41


- 4 Methods: Randomness and the Semi-random method . . . . . . . 43


- 4.1 Various ways to use randomness in Extremal Graph Theory 44
- 4.2 The semi-random method . . . . . . . . . . . . . . . . . . 45
- 4.3 Independent sets in uncrowded graphs . . . . . . . . . . . 45
- 4.4 Uncrowded hypergraphs . . . . . . . . . . . . . . . . . . . 47
- 4.5 Ramsey estimates . . . . . . . . . . . . . . . . . . . . . . 48
- 4.6 Inﬁnite Sidon sequences . . . . . . . . . . . . . . . . . . . 49
- 4.7 The Heilbronn problem, old results . . . . . . . . . . . . . 50
- 4.8 Generalizations of Heilbronn’s problem, new results . . . 50
- 4.9 The Heilbronn problem, an upper bound . . . . . . . . . . 51
- 4.10 The Gowers problem . . . . . . . . . . . . . . . . . . . . . 51


3

- 4.11 Pippenger-Spencer theorem . . . . . . . . . . . . . . . . . 52
- 4.12 Erdo˝s-Faber-Lov´asz conjecture . . . . . . . . . . . . . . . 52


- 5 Methods: Regularity Lemma for graphs . . . . . . . . . . . . . . 54

- 5.1 Ramsey problems, cycles . . . . . . . . . . . . . . . . . . . 56
- 5.2 Ramsey Theory, general case . . . . . . . . . . . . . . . . 59
- 5.3 Ramsey-Tur´an theory . . . . . . . . . . . . . . . . . . . . 59
- 5.4 Ruzsa-Szemer´edi theorem, Removal Lemma . . . . . . . . 62
- 5.5 Applications of Ruzsa-Szemer´edi Theorem . . . . . . . . . 65
- 5.6 Hypergraph Removal Lemma? . . . . . . . . . . . . . . . 66
- 5.7 The Universe of Random Graphs . . . . . . . . . . . . . . 67
- 5.8 Embedding large trees . . . . . . . . . . . . . . . . . . . . 68
- 5.9 Extremal subgraphs of Pseudo-Random graphs . . . . . . 69
- 5.10 Extremal results on “slightly randomized” graphs . . . . . 69
- 5.11 Algorithmic aspects . . . . . . . . . . . . . . . . . . . . . 70
- 5.12 Regularity Lemma for the Analyst . . . . . . . . . . . . . 70
- 5.13 Versions of the Regularity Lemma . . . . . . . . . . . . . 71
- 5.14 Regularity Lemma for sparse graphs . . . . . . . . . . . . 72
- 5.15 Quasi-Random Graph Sequences . . . . . . . . . . . . . . 74
- 5.16 Blow-up Lemma . . . . . . . . . . . . . . . . . . . . . . . 74
- 5.17 Regularity lemma in Geometry . . . . . . . . . . . . . . . 76


- 6 With or without Regularity Lemma? . . . . . . . . . . . . . . . . 77

- 6.1 Without Regularity Lemma . . . . . . . . . . . . . . . . . 79
- 6.2 Embedding spanning or almost-spanning trees . . . . . . 80
- 6.3 Po´sa-Seymour conjecture . . . . . . . . . . . . . . . . . . 81
- 6.4 Ore type results/Pancyclic graphs . . . . . . . . . . . . . 83
- 6.5 Absorbing Method . . . . . . . . . . . . . . . . . . . . . . 84
- 6.6 Connecting Lemma, Stability, Reservoir . . . . . . . . . . 87
- 6.7 Ramsey-Tur´an Matching . . . . . . . . . . . . . . . . . . . 88


- 7 Colouring, Covering and Packing, Classiﬁcation . . . . . . . . . . 89

- 7.1 The One-colour Covering Problem . . . . . . . . . . . . . 90
- 7.2 Embedding monochromatic trees and cycles . . . . . . . . 91
- 7.3 Bollob´s-Eldridge conjecture . . . . . . . . . . . . . . . . 93
- 7.4 Vertex-partitioning into monochromatic subgraphs of given type . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93


- 8 Hypergraph extremal problems, small excluded graphs . . . . . . 96

- 8.1 Codegree conditions in the Fano case . . . . . . . . . . . . 101

9 Large excluded hypergraphs . . . . . . . . . . . . . . . . . . . . . 101

- 9.1 Hypergraph cycles and Ramsey theorems . . . . . . . . . 102




- 9.2 Hamilton cycles . . . . . . . . . . . . . . . . . . . . . . . . 103
- 9.3 Problems: Hypergraph Hamiltonicity . . . . . . . . . . . . 105
- 9.4 Lower bounds, constructions . . . . . . . . . . . . . . . . 106
- 9.5 Upper bounds, asymptotic and sharp . . . . . . . . . . . . 107
- 9.6 Tiling hypergraphs . . . . . . . . . . . . . . . . . . . . . . 110
- 9.7 Vertex-partition for hypergraphs . . . . . . . . . . . . . . 111
- 9.8 Generalizing Gy´arf´s-Ruszink´o-Sa´rk¨ozy-Szemer´edi theorem to hypergraphs . . . . . . . . . . . . . . . . . . . . . 112


CONTENTS 5

9.9 A new type of hypergraph results, strong degree . . . . . 112

Dedicated to Laci Lov´asz on his 70th birthday

Keywords: Extremal graphs, Stability, Regularity Lemma, Semi-random methods, Embedding. Subject Classiﬁcation: Primary 05C35; Secondary 05D10, 05D40, 05C45, 05C65, 05C80.

#### 1. Introduction

We dedicate this survey paper to Laci Lov´asz, our close friend, on the occasion of his 70th birthday. Beside learning mathematics from our professors, we learned a lot of mathematics from each other, and we emphasise that we learned a lot of beautiful mathematics from Laci.

Extremal Graph Theory is a very deep and wide area of modern combinatorics. It is very fast developing, and in this long but relatively short survey we select some of those results which either we feel very important in this ﬁeld or which are new breakthrough results, or which – for some other reasons – are very close to us. Some results discussed here got stronger emphasis, since they are connected to Lov´asz (and sometimes to us).1 The same time, we shall have to skip several very important results; often we just start describing some areas but then we refer the reader to other surveys or research papers, or to some survey-like parts of research papers. (Fortunately, nowadays many research papers start with excellent survey-like introduction.)

Extremal graph theory became a very large and important part of Graph Theory, and there are so many excellent surveys on parts of it that we could say that this one is a “survey of surveys”. Of course, we shall not try to cover the whole area, that would require a much longer survey or a book.

Also we could say that there are many subareas, “rooms” in this area, and occasionally we just enter a “door”, or “open a window” on a new area, point out a few theorems/phenomena/problems, explain their essence, refer to some more detailed surveys, and move on, to the next “door”.

It is like being in our favourite museum, having a very limited time, where we must skip many outstanding paintings. The big diﬀerence is that here we shall see many very new works as well.

One interesting feature of Extremal Graph Theory is its very strong connection and interaction with several other parts of Discrete Mathematics, and more generally, with other ﬁelds of Mathematics. It is connected to Algebra, Commutative Algebra, Eigenvalues, Geometry, Finite Geometries, Graph Limits (and through this to Mathematical Logic, e.g., to Ultra Product, to Undecidability), to Probability Theory, application of Probabilistic Methods, to the evolution of Random Structures, and to many other topics. It is also strongly connected

![image 1](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile1.png>)

1We shall indicate the given names mostly in case of ambiguity, in cases where there are two mathematicians with the same family name, (often, but not always, father and son). We shall ignore this “convention” for Erd˝s, Lova´sz and Tur´an.

- 1. Introduction, 7


to Theoretical Computer Science through its methods, (e.g., using random and pseudo-random structures), expanders, property testing, and also it is strongly connected to algorithmic questions. This connection is fruitful for both sides.

One reason of this fascinating, strong interaction is that in Extremal Graph Theory often seemingly simple problems required the invention of very deep new methods (or their improvements). Another one can be that combinatorial methods start becoming more and more important in other areas of Mathematics. A third reason is, perhaps, – as Tur´an thought and used to emphasise, – that Ramsey’s theorem and his theorem are applicable because they are generalizations of the Pigeon Hole Principle. Erdo˝s wrote several papers on how to apply these theorems in Combinatorial Number Theory, (we shall discuss [258], but see also, e.g., [272, 273, 275, 276, 282, 284], Erdo˝s, A. Sa´rk¨ozy, and T. So´s [311], Alon and Erdo˝s [31]).2 Beside putting emphasis on the results we shall emphasise the development of methods also very strongly. We shall skip discussing our results on the Erdo˝s-S´os and Loebl-Koml´os-S´os conjectures on tree embedding, since they are well described in [386], 3 however, we shall discuss some other tree-embedding results. We are writing up the proof of the Erdo˝s-S´os Conjecture [8].4

Since there are several excellent books and surveys, like Bollob´s [119, 120], F¨uredi [370, 372], F¨uredi-Simonovits [386], Lov´asz [589, 591], Simonovits [756, 760, 761, 762], Simonovits and So´s [766], about Extremal Graph Theory, or some parts of it, here we shall often shift the discussion into those directions which are less covered by the “standard” sources.5 Also, we shall emphasise/discuss the surprising connections of Extremal Graph Theory and other areas of Mathematics. We had to leave out several important new methods, e.g,

- • We shall mostly leave out results on Random Graphs;
- • Razborov’s Flag Algebras [668], (see also Razborov [669], Pikhurko and Razborov [650], Grzesik [423], Hatami, Hladk´y, Kr´al’, Norine, and Razborov, [453], and many others);
- • the Hypergraph Container Method, “recently” developed, independently, by J. Balogh, R. Morris, and W. Samotij [77], and by D. Saxton and A. Thomason [730]. Very recently Balogh, Morris, and Samotij published a survey on the Container method in the ICM volumes [78];
- • the method of Dependent Random Choice, see e.g. Alon, Krivelevich, and Sudakov [38] or, for a survey on this topic see J. Fox and B. Sudakov [353], or many other sources...


![image 2](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile2.png>)

2Sometimes we list papers in their time-order, in some other cases in alphabetical order.

- 3The proof of the approximate Loebl-Koml´os-So´s conjecture was ﬁrst attacked in [12] and

then proved in a sequence of papers, from Yi Zhao [823], Cooley [202], . . . Hladky´, KomPiguet, Simonovits, M. Stein, [466]-[469].

- 4The ﬁrst result on the Loebl Conjecture was an “approximate” solution of Ajtai, Koml´os,


and Szemer´edi [12].

5Essential parts of this survey are connected to Regularity Lemmas, Blow-up lemmas, applications of Absorbing techniques, where again, there are several very important and nice surveys, covering those parts, e.g., Alon [22], Gerke and Steger [392], Koml´os and Simonovits [546], Ku¨hn and Osthus [563, 565], Ro¨dl and Rucin´ski [688], Steger [781], and many others.

• and we have to emphasise, we had to leave out among others almost everything connected to the Universe of Integers, e.g., Sum-free sets, the Cameron-Erd˝os conjecture, the Sum-Product problems, ...

Further, we skipped several areas, referring the readers to more authentic sources. Thus, e.g., one of the latest developments in Extremal Graph Theory is the surprising, strong development in the area of Graph Limits, coming from several sources. A group of researchers meeting originally at Microsoft Research, started investigating problems connected to graph limits, for various reasons. We mention here only Laci Lov´asz and Bal´azs Szegedy [595], Borgs, Chayes, Lov´asz, So´s, and Vesztergombi [139], [138], [140], [137], [141], and M. Freedman, Lov´asz and Schrijver [360]. Lov´asz has published a 500pp book [591] about this area.

How do we refer to papers? We felt that in a survey like this it is impossible to refer to all the good papers. Also, we tried to “introduce” many authors. So if a paper is missing from this survey that does not mean that we felt it was not worth including it. Further, wherever we referred to a paper, we mentioned (all) its authors, unless the paper and its authors had been mentioned a few lines earlier. (We never use at al!) In the “References” we mentioned the given names as well, mostly twice: (i) ﬁrst occurrence and (ii) ﬁrst occurrence as the ﬁrst author.

— · —

Extremal Graph Theory could have started from a number theoretical question of Erdo˝s [258], however, he missed to observe that this is a starting point of a whole new theory. Next came Tur´an’s theorem [807], with his questions, which somewhat later triggered a fast development of this area. In between, starting from a topological question, Erdo˝s and Stone [321] proved their theorem (here Theorem 2.8), which later turned out to be very important in this area. Among others, this easily implies the Erdo˝s-Simonovits Limit Theorem [312], strengthened to the Erdo˝s-Simonovits Stability theory [271, 750], and much later led to Szemer´edi’s Regularity Lemma [791]. All these things will be explained in more details.

We shall also discuss several important methods: Stability, Regularity Lemma, Blow-up Lemma, Semi-random Methods, Absorbing Lemma, and also some further, sporadic methods.

In this survey we mention hypergraph extremal problems only when this does not become too technical for most of the readers: thus we shall not discuss, among others, the very important Hypergraph Regularity Lemmas.6

Repetitions. This paper “covers” a huge area, with a very involved structure. So we shall occasionally repeat certain assertions, to make the paper more readable.

![image 3](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile3.png>)

6For a concise “description” of this topic, see Ro¨dl, Nagle, Skokan, Schacht, and Kohayakawa [686], and also Solymosi [769].

Notation. Below, for a while we shall consider simple graphs, (hypergraphs, loops and multiple edges are excluded) and for graphs (or hypergraphs) the ﬁrst subscript almost always denotes the number of vertices: Gn, Sn, Tn,p ...are graphs on n vertices. There will be just two exceptions: Kd(n1,...,nd) means a d-partite complete graph with ni vertices in its ith class; if we list a family of graphs L = {L1,...,Lt}, then again, the subscript is not necessarily the number of vertices. The maximum and minimum degrees will be denoted by dmax(G) and dmin(G), respectively. (In the hypergraph section δ1(H(k)) is also the minimum degree.) Cℓ, Pℓ, Kℓ denote the cycle, path, and the complete graph of ℓ vertices, respectively. Further, e(G), v(G), χ(G) and α(G) denote the number of edges, vertices, the chromatic number, and the independence number,7 respectively. For a graph G, V (G) and E(G) denote the sets of vertices and edges. If U ⊆ V (G) then G[U] is the subgraph induced by U.

Given a family L of excluded graphs, ex(n,L) denotes the maximum of e(Gn) for a graph Gn not containing excluded subgraphs, and EX(n,L) denotes the family of extremal graphs for L: the graphs not containing excluded subgraphs but attaining the maximum number of edges. Let Tn,p be the Tur´an graph: the graph obtained by partitioning n vertices into p classes as equally as possible and joining two vertices if and only if they are in distinct classes.

Figure 1: Tur´an graph

Given some graphs L1,...,Lr, R(L1,...,Lr) is the Ramsey number: the smallest integer R for which all r-edge-coloured KR have a (monochromatic) subgraph Li in some colour i. If all these graphs are complete graphs, Li = Kp

, then we use the abbreviation R(p1,...,pr) for this Ramsey number.

i

- Remark 1.1 (Graph Sequences). Speaking of o(n2) edges, or o(n) vertices, ..., we cannot speak of an individual graph, only about a sequence of graphs. In this paper, using o(.), we always assume that n → ∞. Also, since A(n) + o(n) and A(n)−o(n) mathematically are exactly the same, we shall be cautious with formulating some of our theorems.


#### 2. The beginnings

- 2.1. Very early results The ﬁrst, simplest extremal graph result goes back to Mantel.


- Theorem 2.1 (Mantel, (1907), [606]). If a graph Gn does not contain a K3


2

then it has at most ⌊n

4 ⌋ edges. Tur´an, not knowing of this theorem,8 proved the following generalization:

![image 4](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile4.png>)

![image 5](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile5.png>)

7often called stability number. 8The last paragraph of Tura´n’s original paper is as follows: “. . . Further on, I learned from

the kind communication of Mr. Jo´zsef Krausz that the value of dk(n) given on p438 for k = 3 was found already in 1907 by W. Mantel (Wiskundige Opgaven, vol 10, pp. 60-61). I know this paper only from the reference Fortschritte d. Math. vol 38, p. 270.”

Theorem 2.2 (Tur´an, (1941), [807, 808, 810]9). If a graph Gn does not contain a Kp+1 then e(Gn) ≤ e(Tn,p), and the equality is achieved only for Gn = Tn,p.

The above theorems are sharp, since Tn,p is p–chromatic and therefore it does not contain Kp+1. These theorems have very simple proofs and there was also an earlier extremal graph theorem discovered and proved by Erdo˝s. He set out from the following “combinatorial number theory” problem.

Problem 2.3 (Erdos˝ (1938), [258]). Assume that A := {a1,...,am} ⊆ [1,n] satisﬁes the “multiplicative Sidon property” that all the pairwise products are diﬀerent. More precisely, assume that

if aiaj = akaℓ then {i,j} = {k,ℓ}. (2.1) How large can |A| be?

The primes in [2,n] satisfy (2.1). Can one ﬁnd many more integers with this “multiplicative Sidon property”? To solve Problem 2.3, Erdo˝s proved

- Theorem 2.4 (Erd˝os, [258]). If G ⊆ K(n,n) and C4  ⊆ G then e(G) ≤ 3n√n.

![image 6](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile6.png>)

This may have been the ﬁrst non-trivial extremal graph result. It is interesting to remark that this paper contained the ﬁrst ﬁnite geometric construction, due to Eszter Klein, to prove the lower bound ex(n,C4) ≥ cn√n. Let π(n) be the number of primes in [2,n]. Using Theorem 2.4, Erdo˝s proved

![image 7](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile7.png>)

- Theorem 2.5. Under condition (2.1), |A| ≤ π(n) + O(n3/4).


As to the sharpness of this theorem, Erdo˝s wrote:

“Now we prove that the error term cannot be better than O(n3/4/(log n)3/2). First we prove the following lemma communicated to me by Miss E. Klein:

Lemma. Given p(p+1)+1 elements, (p a prime), we can construct p(p+1)+1 combinations taken p + 1 at a time, having no two elements in common.”

Though the language is somewhat archaic, it states the existence of a ﬁnite geometry on p2 + p + 1 points: this seems to be the ﬁrst application of ﬁnite geometric constructions in this area. Later Erdo˝s applied graph theory in number theory several times. Among others, he returned to the above question in [272] and proved that the lower bound is sharp.

Much later a whole theory developed around these types of questions. Here we mention only some results of A. Sa´rk¨ozy, Erdo˝s, and So´s [311], the conjecture of Cameron and Erdo˝s [174], and the papers of Ben Green [413], and of Alon, Balogh, Morris, and Samotij [25].

![image 8](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile8.png>)

9Tura´n’s papers originally written in Hungarian were translated into English after his death, thus [810] contains the English translation of [807].

- Remark 2.6. (a) One could ask, what is the connection between ex(n,C4) and Theorem 2.5. Erdo˝s wrote each non-prime integer ai ∈ A as ai = bj(i)dj(i),


where bj are the primes in [n2/3,n] and all the integers in [1,n2/3], and dj are the integers in [1,n2/3] . So the non-prime numbers deﬁned a bipartite graph G[B,D], and each ai deﬁned an edge in it. If this graph contained a C4, the corresponding four integers would have violated (2.1). Consider those integers for which aj(i) ≤ 10√n and bj(i) ≤ 10√n. Not having C4 in the corresponding subgraph, we can have at most c√n3/2 = cn3/4 such integers. This does not cover all the cases, however, we can partition all the integers into a “few” similar subclasses.10 This proves that

![image 9](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile9.png>)

![image 10](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile10.png>)

![image 11](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile11.png>)

|A| ≤ π(n) + O(n3/4).

- (b) There is another problem solved in [258], also by reducing it to an ex-

tremal graph problem. It is much simpler, and we skip it.

- (c) The “additive Sidon” condition assumes that ai +aj = ak +aℓ implies


{i,j} = {k,ℓ}. In case of Sum-free sets we exclude ai + aj = ak. See e.g. Cameron [173], Bilu [109] and many other papers on integers, or groups.

(d) Some related results can be found, e.g., in Chan, Gy˝ori, and A. Sa´rk¨ozy [176]. Remarks 2.7. (a) Many extremal problems formulated for integers automatically extend to ﬁnite Abelian groups, or sometimes to any ﬁnite group.

Thus, e.g., a Sidon sequence can be (and is) deﬁned in any Abelian group as a subset for which ai+aj = ak+aℓ, unless {i,j} = {k,ℓ}. A paper of Erdo˝s and Tur´an [324] estimates the maximum size Sidon subset of [1,n]. Several papers of Erdo˝s investigate Sidon problems, e.g., [259, 262]. This problem was extended to groups, ﬁrst by Babai [55], Babai and So´s [57]. (Surprisingly, for integers there are sharp diﬀerences in analysing the density of ﬁnite and of inﬁnite Sidon sequences, see Subsection 4.6.) Problems on “sum-free sets” were generalized to groups by Babai, So´s, and then by Gowers [405], by Balogh, Morris, and Samotij [76], and by Alon, Balogh, Morris and Samotij [25].11

(b) A few more citations from this area are: Alon [21], Green and Ruzsa [415], Lev,  Luczak, and Schoen [574], Sapozhenko [718, 719, 720], ...

— · The next extremal graph result was motivated by topology. It is

Theorem 2.8 (Erd˝os-Stone Theorem (1946), [321]). For any ﬁxed t ≥ 1,

n 2

1 p

+ o(n2).

ex(n,Kp+1(t,...,t)) = 1 −

![image 12](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile12.png>)

![image 13](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile13.png>)

- 10E.g. we can put ai into Ai if the smallest prime divisor of at is in (2t, 2t+1] and use a slight generalization of Theorem 2.4 to K(m, n).
- 11A longer annotated bibliography of O’Bryant can be downloaded from the Electronic Journal of Combinatorics [160] on Sidon sets.


We mention here one more “early extremal graph theorem”, strongly connected to the Erdo˝s-Stone Theorem: Theorem 2.9 (Erd˝os, K˝ova´ri-T. So´s-Tur´an (1954), [554]). 12 13

- 1

![image 14](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile14.png>)

- 2


ex(n,K(a,b)) ≤

√a

1

b − 1 · n2−

![image 15](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile15.png>)

a + O(n). (2.2)

![image 16](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile16.png>)

Below let a ≤ b. A very important conjecture is the sharpness of (2.2):

Conjecture 2.10 (KST is sharp). For every pair of positive integers a ≤ b, there exists a constant ca,b > 0 for which

1

ex(n,K(a,b)) > ca,b n2−

a. (2.3)

![image 17](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile17.png>)

We can replace ca,b by ca,a. The conjecture follows from Erdo˝s [258] if a = 2. A sharp construction can be found in [554] for the bipartite case14, (and later an even sharper one from Reiman [674]), and a sharp construction is given by Erdo˝s, R´enyi, and So´s [308] and by Brown for C4 = K(2,2) and not necessarily bipartite Gn. Brown also found a sharp construction [150], for K(3,3)15. Much later, Conjecture 2.10 was proved for a ≥ 4 and b > a! by a Koll´ar-R´onyai-Szab´o construction [532]. This was slightly improved by Alon-Ro´nyai-Szab´o [42]: the weaker condition b > (a − 1)! is also enough for (2.3).

— · —

Theorems of Erdo˝s and Stone and of K˝va´ri, T. So´s, and Tur´an have a very important consequence.

- Corollary 2.11. ex(n,L) = o(n2) if and only if L contains a bipartite graph.

Actually, the theorem of K˝va´ri, T. So´s, and Tur´an and the fact that Tn,2 is bipartite imply the stronger dichotomy:

- Corollary 2.12. If L ∈ L is bipartite, then ex(n,L) = O(n2−(2/v(L))) = o(n2)


2

and if L contains no bipartite graphs, then ex(n,L) ≥ ⌊n

4 ⌋.

![image 18](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile18.png>)

The case when L contains at least one bipartite graph will be called Degenerate. It is one of the most important and fascinating areas of Extremal Graph Theory, and F¨uredi and Simonovits have a long survey [386] on this. Here we shall deal only very shortly with Degenerate extremal graph problems.

— · —

![image 19](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile19.png>)

- 12Mostly we call this result the K˝va´ri-T. S´os-Tura´n theorem. Here we added the name of Erd˝s, since [554] starts with a footnote according to which “As we learned after giving the manuscript to the Redaction, from a letter of P. Erd˝s, he has found most of the results of this paper.” Erd˝s himself quoted this result as K˝va´ri-T. S´os-Tura´n theorem.
- 13For Hungarian authors we shall mostly use the Hungarian spelling of their names, though occasionally this may diﬀer from the way their name was printed in the actual publications.
- 14Here “sharp” means that not only the exponent 2 − 1p but the value of ca,b is also sharp. 15The sharpness of the multiplicative constant followed from a later result of Fu¨redi.


![image 20](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile20.png>)

The main contribution of Tur´an was that he had not stopped at proving

- Theorem 2.2 but continued, asking the “right” questions:


What is the maximum of e(Gn) if instead of excluding Kp+1 we exclude some arbitrary other subgraph L?16

To provide a starting point, Tur´an asked for determining the extremal numbers and graphs for the Platonic bodies: Cube, Octahedron, Dodecahedron, and Icosahedron,17 for paths, and for lassos [267],18 see Figure 2.1. Here the extremal graph problem of the Cube was (partly) solved by Erdo˝s and Simonovits [313]. We return to this problem in Subsection 2.16. The problems of the Dodecahedron and Icosahedron were solved by Simonovits, [755],[754], using the Stability method, see Subsection 2.12.

Cube Octahedron Icosahedron, Dodecahedron Figure 2: Excluded platonic graphs The general question can be formulated as follows:

Given a family L of forbidden graphs, what is the maximum of e(Gn) if Gn does not contain subgraphs L ∈ L?

- 2.2. Constructions

Mostly in an extremal graph problem ﬁrst we try to ﬁnd out how do the extremal structures look like. In the nice cases this is equivalent to ﬁnding a construction providing the lower bound in our extremal problems, and then we try to ﬁnd the matching upper bound. Here we shall not go into more details, however, we shall return to this question in Section 9, on Matchings, 1-factors, and the Hamiltonicity of Hypergraphs.

- 2.3. Some historical remarks


Here we make two remarks.

(A) When Tur´an died in 1976, several papers appeared in his memory, analysing, among others, his inﬂuence on Mathematics. Erdo˝s himself wrote

![image 21](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile21.png>)

16Later this question was generalized to excluding an arbitrary family of subgraphs, however,

that was only a small extension. 17The tetrahedron is K4, covered by Tura´n theorem. 18Lasso is a graph where we attach a path to a cycle. Perhaps nobody considered the

lasso-problem carefully, however, very recently Sidorenko solved a very similar problem of the keyrings [749].

several such papers, e.g., [281, 283]. In [280] he wrote, on Tur´an’s inﬂuence on Graph Theory:

“ In this short note, I will restrict myself to Tur´an’s work in Graph Theory, even though his main work was in analytic number theory and various other branches of real and complex analysis. Tur´an had the remarkable ability to write perhaps only one paper or to state one problem in various ﬁelds distant from his own; later others would pursue his idea and a new subject would be born. In this way Tur´an initiated the ﬁeld of Extremal Graph Theory. . . .

. . . Tur´an also formulated several other extremal problems on graphs, some of which were solved by Gallai and myself [289]. I began a systematic study of extremal problems in Graph Theory in 1958 on the boat from Athens to Haifa and have worked on it since then. The subject has grown enormously and has a very large literature;. . . ”

Observe that Erdo˝s implicitly stated here that until the early 60’s most of the results in this area were sporadic.

(B) Here we write about Extremal Graph Theory at length, still, if one wants to tell what Extremal Graph Theory is, and what it is not, that is rather diﬃcult. We shall avoid answering this question, however, we remark that since the Goodman paper [400] and the Moon-Moser paper [617] an alternative answer was the following. Consider some “excluded subgraphs” L1,...,Lt, count the multiplicities of their copies, m(Li,Gn), in Gn, and Extremal Graph Theory consists of results asserting some inequalities among them. Since the emergence of Graph Limits this approach became stronger and stronger. One early “counting” example is

- Theorem 2.13 (Moon and Moser (1962), [617]). If tk is the number of Kk in Gn, then

k(k − 2)tk ≥ tk−1

(k − 1)2tk−1 tk−2 − n .

![image 22](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile22.png>)

2.4. Early results

If we restrict ourselves to simple graphs, some central theorems assert that for ordinary graphs the general situation is almost the same as for Kp+1: the extremal graphs Sn and the almost extremal graphs Gn are very similar to Tn,p. The similarity of two graph sequences (Gn) and (Hn) means that one can delete o(n2) edges of Gn and add o(n2) edges to obtain Hn.

The general asymptotics of ex(n,L) and the asymptotic structure of the extremal graphs are described by

- Theorem 2.14 (Erd˝os-Simonovits, (1966), [269],[271],[750]). Let


p := min

χ(L) − 1. (2.4)

L∈L

If Sn ∈ EX(n,L), then one can delete from and add to Sn o(n2) edges to obtain Tn,p.

A much weaker form of this result immediately follows from Erdo˝s-Stone Theorem. Theorem 2.15 (Erd˝os-Simonovits (1966), [312]). Deﬁning p by (2.4),

1 p

ex(n,L) = 1 −

![image 23](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile23.png>)

n 2

+ o(n2).

One important message of these theorems is that for simple graphs the extremal number and the extremal structure are determined up to o(n2) by the minimum chromatic number of the excluded subgraphs. In some sense this is a great luck: there are many generalizations of the Tur´an type extremal graph problems, but we almost never get so nice answers for the natural questions in other areas.

Speaking about the origins of Extremal Graph Theory, we have to mention the dichotomy that occasionally we have very nice extremal structures but in the Degenerate case the extremal graphs seem to have much more complicated structures (unless L contains a tree or a forest). Actually this may explain why Erdo˝s missed to observe the importance of his Theorem 2.4, on ex(n,C4).

To solve some extremal graph problems, Simonovits deﬁned the Decomposition Family (see, e.g., [757]).

- Definition 2.16 (Decomposition, M = M(L)). Given a family L with p :=

min{χ(L) : L ∈ L} − 1, then M ∈ M if L ⊆ M ⊗ Kp−1(t,...,t) for t = v(M), where L ⊗ H denotes the graph obtained by joining each vertex of L to each vertex of H.

The meaning of this is that M ∈ M if we cannot embed M into one class of a Tn,p without obtaining an excluded L ∈ L. Thus, e.g, if we put a C4 into the ﬁrst class of Tn,p, then the resulting graph contains a Kp+1(2,2,...,2). Therefore C4 is in the decomposition class of Kp+1(2,...,2).

...Given a family L of excluded subgraphs, the decomposition family M = M(L) determines (in some sense) the error terms and the ﬁner structure of the L-extremal graphs. Namely, the error terms depend on ex(n,M), see [750].

The next theorem “explains”, why is Tn,p extremal for Kp+1.

- Definition 2.17 (Colour-critical edge). The edge e ∈ E(L) is called critical, if χ(L − e) < χ(L).


Of course, in such cases, χ(L − e) = χ(L) − 1. Each edge of an odd cycle is critical. In Figure 2.4, e.g., one can see the Gr¨otzsch graph (often incorrectly called Mycielski graph). It is 4-chromatic but all its edges are critical. On the other hand, in the Petersen, or the Dodecahedron graphs, there are no critical edges.19 20 The next theorem solves all cases when L has a critical edge.

![image 24](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile24.png>)

- 19If the automorphism group of G is edge-transitive, then either all the edges are critical, or none of them. By the way, in [761], Simonovits discusses these questions in more details, among others, the extremal problems of generalized Petersen graphs.
- 20The deﬁnition applies to hypergraphs as well, the triples of the Fano hypergraph are also critical.


1

3

2

2

1

3

2 2

1

3

Petersen graph, Gr¨otzsch graph, Fano hypergraph

Theorem 2.18 (Simonovits). 21 Deﬁne p = p(L) by (2.4). The following statements are equivalent:

- (a) Some (p + 1)-chromatic L ∈ L has a critical edge.
- (b) There exists an n0 such that for n > n0, Tn,p is extremal for L.
- (c) There exists an n1 such that for n > n1, Tn,p is the only extremal graph


for L.22

Here (a) is equivalent to that adding an edge to Kp(t,...,t), for t = v(L), we get a graph containing L, and equivalent to that K2 ∈ M. The extremal results on the Dodecahedron D20 and Icosahedron I12 follow from [755], and [754]. We skip the details referring the reader to the survey of Simonovits [761].

Meta-Theorem 2.19 (Simonovits). “Whatever” we can prove for L = Kp+1, with high probability, we can also prove it for any L having a critical edge.

2.5. Which Universe?

Extremal problems exist in a much more general setting: Theorem 2.5 is, e.g., an extremal theorem on sets of integers. In general, we ﬁx the family of some objects, e.g., integers, graphs, hypergraphs, r-multigraphs, where some r is ﬁxed and the edge-multiplicity is bounded by r. We exclude some substructures, and try to optimize some (natural) parameters. More generally, putting some bounds on the number of one type of substructures, we try to maximize (or minimize) the number of some other substructures. This approach can be found in the paper of Moon and Moser [617], or in Lov´asz and Simonovits, [593].23 The paper of Alon and Shikhelman [47] is also about this question, in a more general setting. (We should also mention here the famous conjecture of Erdo˝s, on the number of pentagons in a triangle-free graph, well approximated by Gy˝ori [441], (and by F¨uredi, unpublished) and then solved by Grzesik [423] and by Hamed Hatami, Hladk´y, Kr´al, Norine and Razborov [453].) With the development of the theory of graph limits this view point became more and more important. Below we list some most common Universes, and some related papers/surveys.

(a) Integers, as we have seen above, in Problem 2.3 or Theorem 2.5. Among many other references, here we should mention the book of Tao and Vu

![image 25](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile25.png>)

21For p = 2 this was also known (at least, implicitly) by Erd˝s. 22Here (c)→(b) is trivial, and one can prove that (b) implies (c) with n1 = n0 + 3p. 23Bollob´as [117] also contains similar, strongly related results.

on Additive Combinatorics [800], the Geroldinger-Ruzsa book [393], and also a new book of Bajnok [59].

- (b) Abelian Groups, see e.g. Babai-So´s, [57] Gowers [403, 405] and also [393], a survey of Tao and Vu [801] and [59].24
- (c) Graphs: this is the main topic of this survey;
- (d) Digraphs and multigraphs, with bounded arc/edge multiplicity,25 see Brown-Harary [156], Brown-Erd˝s-Simonovits [152, 153]; Sidorenko, [747], for longer surveys see Brown and Simonovits [158] and [159], Bermond and Thomassen [105], Thomassen [804], Bang-Jensen and Gutin [88], Jackson and Ordaz [474];
- (e) Hypergraphs, see e.g. de Caen [171], F¨uredi [370], Sidorenko [748], Keevash [498];26
- (f) Extremal subgraphs of random graphs: Babai, Simonovits, Spencer [56], Brightwell, Panagiotou, and Steger [148], Ro¨dl-Schacht [702], Ro¨dl [685], Schacht [731], ...DeMarco and J. Kahn [234], [235], [236], or
- (g) Extremal subgraphs of Pseudo-random graphs, see e.g., Krivelevich and Sudakov [559] Aigner-Horev, Ha`n, and Schacht [5], Conlon and Gowers [199, 193], or Conlon, Fox and Zhao [198], or e.g., Allen, B¨ottcher, Kohayakawa, Person, [16, 17].


Perhaps one of those who ﬁrst tried to compare various universes and analyze their connections was Vera T. So´s [773, 774]. In [773] she considered the connections between Graph Theory, Finite Geometries, and Block Designs. The emphasis in these papers was on the fact that basically the same problems occur in these areas in various settings, and these areas are in very strong connection, interaction, with each other.27 Most of the above universes we shall skip here, to keep this survey relatively short, however, below we consider some extremal problems on integers.

Integers

We do not intend to describe this very wide area in details, yet we start with some typical, important questions in this area, i.e., in the theory of extremal problems on subsets of integers. As we have stated in Problem 2.3, Erdo˝s considered the multiplicative Sidon problem in [258]. Even earlier Erdo˝s and Tur´an formulated the following conjecture for subsets of integers:

Conjecture 2.20 (Erd˝os-Tur´an (1936), [323]). 28 If A ⊆ [1,n] does not contain a k-term arithmetic progression, then |A| = o(n) (as n → ∞).29

![image 26](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile26.png>)

- 24There are several earlier results on similar questions, e.g., Yap, [818, 819], Diananda and Yap [240], yet they are slightly diﬀerent, or several papers of A. Street, see [784].
- 25One has to assume that the edge-multiplicity is bounded, otherwise even for the excluded K3 in the Universe of multigraphs we would get arbitrary many edges. As an exception, in the Fu¨redi-Ku¨ndgen theorem [378] no such bound is assumed.
- 26and many others, see e.g. Ro¨dl and Rucinski [688], or the much earlier Bermond, Germa,


Heydemann, and Sotteau [104], and the corresponding Sections 8 and 9. 27Vera S´os did not call these areas Universes. 28Actually, here they formulated this for r3(n). 29Speaking of arithmetic progressions we always assume that its terms are distinct.

The proof seemed those days very diﬃcult. Even the simplest case k = 3 is highly non-trivial: it was ﬁrst proved by K.F. Roth, in 1953 [678], and for k = 4 those days the conjecture seemed even more diﬃcult.30 The conjecture was proved by Szemer´edi, ﬁrst for k = 4 [788], and then for any k:

Theorem 2.21 (Szemer´edi (1975), [790]). Let k be a ﬁxed integer. If rk(n) is the maximum number of integers, a1,...,am ∈ [1,n] not containing a k-term arithmetic progression, then rk(n) = o(n).

Ergodic theory and Szemer´edi Theorem. Not much later that Szemer´edi proved this theorem, F¨urstenberg gave an alternative proof, in 1977, using ergodic theory [387]. This again is an example where seemingly simple combinatorial problems led to very deep theories. One advantage of F¨urstenberg’s approach was that it made possible for him and Katznelson and their school to prove several important generalizations, e.g., the high dimensional version [388], Bergelson and Leibman [102] proved some polynomial versions of the original theorem, and later the density version of Hales-Jewett theorem [389].

Polymath on Hales-Jewett theorem. As we just stated, one of the important generalizations of Theorem 2.21 is the density version of Hales-Jewett theorem, obtained by F¨urstenberg and Katznelson [389] which earlier seemed hopeless.

There is a big diﬀerence between the Hales-Jewett Theorem and Szemere´di’s theorem: just to explain the meaning of the Hales-Jewett Theorem or its density version, is more diﬃcult than to explain the earlier ones. It is one of the most important Ramsey type theorems, asserting, that – ﬁxing the parameters appropriately – a high dimensional r-coloured structure will contain a (small) monochromatic substructure, a so called “combinatorial line”. We remark that there was a similar result of Graham and Rothschild (on n-parameter sets) earlier, [409].

A simpliﬁed version of this was given by Austin [52].31 The Polymath project [656] provided a completely elementary proof of this theorem. A nice description of this is the MathSciNet description of the “PolyMath” proof of this (see MathSciNet MR2912706, or the original paper, [656]).32

Erd˝s conjecture on the sum of reciprocals. One of the central questions in this area was if there are arbitrary long arithmetic progressions consisting of

![image 27](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile27.png>)

30The conjectures on rk(n) were not always correct. Vera S´os wrote a paper [775] on the letters between Erd˝s and Tura´n during the war, where one can read that Szekeres e.g. conjectured that for n = 21(3ℓ + 1) rk(n) ≤ 2ℓ. This was later disproved by Behrend [96]. (This conjecture is also mentioned in [323].)

![image 28](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile28.png>)

- 31See also Austin [51], Beiglebo¨ck [97], (?) Bergelson and Leibman [103] Gowers, [406],

Polymath [655],.. .

- 32Similarly to the proof of r3(n) = o(n) from the Ruzsa-Szemer´edi Triangle Removal


Lemma, (see Theorem 5.26) Ro¨dl, Schacht, Tengen and Tokushige proved rk(n) = o(n) and several of its generalizations in [699] “elementarily”, i.e. not using ergodic theoretical tools. On the other hand, they remarked that those days no elementary proof was known on the Density Hales-Jewett theorem.

primes. In 1993, Erdo˝s wrote a paper on his favourite theorems [287], where he wrote that in those days the longest arithmetic progression of primes had 17 integers (and was obtained with the help of computers). Now we all know the celebrated result:

Theorem 2.22 (Green and Tao (2008), [416]). The set of primes contains arbitrary long arithmetic progressions.

We close this part with the related famous open problem of Erdo˝s which would imply Theorem 2.22. Then we list some estimates on rk(n). Problem 2.23 (Erd˝os [287]). Let A = {a1,...,an,...} ⊆ Z be a set of positive integers. Is it true that if a 1

= ∞, then for each integer k > 2, A contains a k-term arithmetic progression?

![image 29](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile29.png>)

i

Estimates on rk(n). First Roth proved that r3(n) = O(log logn n).33 Many researchers worked on improving the estimates on r3(n), or more generally, on rk(n). Roth’s estimate was followed by the works of Heath-Brown [462] and Szemer´edi [792], and then Bourgain [145]. One of the last breakthroughs was

![image 30](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile30.png>)

Theorem 2.24 (Sanders, [716]). Suppose that A ⊆ {1,...,N} contains no 3term arithmetic progressions. Then

|A| = O

(log log N)5 log N

N .

![image 31](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile31.png>)

The exponent of log log n was brought down to 4 by T. Bloom [112].

- Remark 2.25 (Lower bounds). Clearly, for k ≥ 3, rk(n) ≥ r3(n). Behrend [96] proved that there exists a c > 0 for which


n ec

√logn. (2.5)

r3(n) ≥

![image 32](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile32.png>)

![image 33](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile33.png>)

This was improved by Elkin [254], and then, in a much more compact way, by Green and Wolf [420].

— · —

One could ask, what do we know about r4(n). A major breakthrough was due to Gowers [402], according to which for every k ≥ 3 there exists a ck > 0 for which

rk(n) = O

n log logc

![image 34](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile34.png>)

n

k

k+9) works.)

. (Actually, ck = 2−(2

Green and Tao improved this for k = 4 to

r4(n) = O

n logc n

![image 35](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile35.png>)

for some constant c > 0.

![image 36](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile36.png>)

33Using log log n we always assume that n ≥ 100, and therefore log log n > 3/2.

See also Green and Tao [417], [419] and the survey of Sanders [717].

Other important problems on Integers: We start with the following remark. A property P is always a family of subsets of some ﬁxed set. It is monotone decreasing if X ∈ P and Y ⊆ X implies that Y ∈ P. (Two examples of this are (i) the sets of integers not containing solutions of some given equations, and (ii) the family of graphs not containing an L.) When we ﬁx a Universe and a “monotone” property P, then, beside asking for the size of the extremal sets X for P, we may also ask, e.g., how many X ∈ Pn are there, where Pn ⊆ P is deﬁned by some parameter n of these objects. We may also ask, what is their typical structure. For graphs these are the Erdo˝s-KleitmanRothschild type problems [297], discussed in Section 2.13. The same questions can also be asked for extremal problems on integers, and we shall not return to them later, therefore we list some of them here, together with “their extremal problems”.

- • We have started with the multiplicative Sidon problem (Thm 2.5), and there is also the problem of additive Sidon sets.
- • We wrote about excluding the k-term arithmetic progressions, in this subsection.34
- • Another important area is the problem of sum-free sets, see, e.g., Cameron and Erdo˝s [174], Alon, Balogh, Morris, and Samotij [26],  Luczak and Schoen [603, 604], Sapozhenko [718],...Balogh, Liu, Sharifzadeh, and Treglown [72], Balogh, Morris, and Samotij [76].
- • Very active research characterises the Sum-Product problems, introduced by Erdo˝s and Szemer´edi [322], see also Gy. Elekes [253], Bourgain, Gambourd, and Sarnak [146], Solymosi [770] among the very many related papers.
- • Important and deep questions can be listed in connection with FreimanRuzsa type results (see e.g. [361]).


Recommended surveys, papers: Ruzsa [707, 708], Solymosi [770], Granville and Solymosi [412], Pomerance and A. Sa´rk¨ozy [657], ...and the survey of Shkredov [741].

Groups

We have considered some problems about the Universe of Integers. It is, of course, natural to ask the analogous questions for groups. There are many results of this type. Here we mention only a few papers on groups. Most of the deﬁnitions immediately generalize from integers to any Abelian group. We have already mentioned that Sidon sets in groups were investigated by Babai and So´s [57]. From among the many-many further similar extensions we mention only Alon, Balogh, Morris and Samotij [26], [76], Gowers [405], on quasi-random groups, Green [414], Green and Ruzsa [415], Lev,  Luczak and Schoen [574], Sapozhenko [718, 720], and B. Szegedy on Gowers norms and groups [787].

![image 37](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile37.png>)

34Subsubsections will also be called Subsections.

There are also results on non-Abelian groups, e.g., Sanders [715], and the paper of Babai and So´s [57] considers both Abelian and non-Abelian groups (and try to determine the maximum size of a Sidon set in them), and we refer the reader to these papers.

- Remark 2.26. For each property P, one can also investigate the P-maximal, or the P-minimal structures. Here, e.g., one can try to count the maximal subsets of property P, in [1,n], or in a group G, ...Thus e.g., Balogh, Liu, Sharifzadeh and Treglown [72] count the maximal sum-free subsets, while Balogh, Bushaw, Collares, Liu, Morris, Sharifzadeh [65] describe the typical structure of graphs with no large cliques35.
- Remark 2.27. There are several results on subsets of G without non-trivial arithmetic progressions where G is a group, or a linear vector space. Here we mention only the paper of Croot, Lev, and P´eter P. Pach [210] on the linear


vector space Zn4. J. Wolf provides a very clear and detailed description of this paper and related results, in the MathSciNet-MR3583357. See also the related post of T. C. Tao, and the paper of Ellenberg and Gijswijt [255], building on [210].

2.6. Ramsey or density?

One diﬀerence between Ramsey and Tur´an theory is that in the Tur´an case we have density statements, while in the Ramsey case the densities are not enough to ensure the occurrence of a monochromatic structure. A trivial example of this is the problem of R(4,4), yet, instead of this we consider another trivial example: the connectedness. If we RED-BLUE-edge-colour a Kn, then either we have a RED connected spanning subgraph, or a BLUE one. However, we may have ≈ 12

n 2 edges in both colours, not enough for a connected spanning

![image 38](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile38.png>)

subgraph.

More generally, if we r-colour the edges of a graph G, and consider its subgraphs Gi deﬁned by the ith colour, and we assert that – under some conditions, – G has a monochromatic L, because it has at least 1re(G) edges, that is a Tur´an type, density theorem.

![image 39](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile39.png>)

The Erdo˝s-Tur´an conjecture, and its proof, the Szemer´edi theorem, came from the van der Waerden theorem, [812] according to which, if r and k are ﬁxed, and we r-colour the integers in an arbitrary way, then there will be a monochromatic arithmetic progression of length k. The Erdo˝s-Tur´an conjecture was the corresponding density conjecture: any inﬁnite sequence of integers of positive lower density contains an arithmetic progression of k terms.

Many Ramsey problems are very diﬀerent from density problems, however, in some other cases a Ramsey problem may be basically a density problem. Sometimes a density theorem generalizes a Ramsey type results in a very nontrivial way. In this survey mostly we are interested in density problems.

![image 40](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile40.png>)

35The description of the typical structure is a stronger result than just counting them.

Example 2.28. For any tree Tk, trivially, ex(n,Tk) < (k − 2)n. This implies that R(Tk,Tk) < 4k, and for r colours Rr(Tk,...,Tk) ≤ 2kr.

So, for trees the Ramsey problem is a density problem, up to a constant. For more details, see e.g. the paper of Faudree and Simonovits [336].

2.7. Why are the extremal problems interesting?

Extremal graph problems are interesting on their own, they emerge in several branches of Discrete Mathematics, e.g., in some parts of Graph Theory not directly connected to Extremal Graph Theory, in Combinatorial Number Theory, and also they are strongly connected to Ramsey Theory.

Erdo˝s wrote several papers on how can Graph Theory be applied in Combinatorial Number Theory, or in Geometry, see e.g. [272]. Andra´s Sa´rk¨ozy returned to the investigation and generalization of Erdo˝s’ results discussed in Problem 2.3: the next step was to analyze the case when no product of six distinct numbers from A was a square36. The corresponding graph theoretical lemmas were connected to ex(n,m,C6)37 and were established by Erdo˝s, A. Sa´rk¨ozy, and So´s, [311] by G.N. Sa´rk¨ozy [721] and by E. Gy˝ori [442]. (Similar cycle-extremal results and similar methods were used also in a paper of Dietmann, Elsholz, Gyarmati and Simonovits [241], but for somewhat diﬀerent problems.)

Extremal graph theory is strongly connected to many other parts of Mathematics, among others, to Number Theory, Geometry, the theory of Finite Geometries, Random Graphs, Quasi-Randomness, Linear Algebra, Coding Theory.

The application of constructions based on ﬁnite geometry became important and interesting research problems, we mention here just a few, like Reiman [674], Hoﬀman-Singleton [472], Benson [101], W.G. Brown [150]. Erdo˝s, R´enyi, T. So´s [308] ...and refer the reader again to the surveys of Vera So´s [773], F¨uredi and Simonovits [386] or the papers of Lazebnik, Ustimenko, Woldar, e.g., [567] and others.

These constructions are connected to the construction of expander graphs (Ramanujan graphs) by Margulis [609, 610, 611], and Lubotzky, Phillips and Sarnak [599], which use highly non-trivial mathematics, and in some sense are strongly connected to Extremal Graph Theory.38 Here we recommend the survey of Alon in the Handbook of Combinatorics [22] and several of his results on the eigenvalues of graphs, e.g. [20] or the Alon-Milman paper [39]. Another surprise was that in [532] deeper results from algebra also turned out to be very useful. In some other cases (e.g., Bukh and Conlon [161, 162]) randomly chosen polynomial equations were used for constructions in extremal graph theory. We return to this question in Section 2.16.

![image 41](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile41.png>)

36If (2.1) is violated then aiajakaℓ is a square. 37ex(n, m, L) is the maximum number of edges an L-free graph G ⊂ K(n, m) can have.

This problem may produce surprising phenomena when n = o(m).

38The Margulis-Lubotzky-Phillips-Sarnak papers are eigenvalue-extremal, however, as Alon pointed out, (see the last pages of [599]), these constructions are “extremal” for many other graph problems as well.

Remark 2.29. There are cases, when important methods came from that part of Discrete Mathematics which is not directly Extremal Graph Theory, however, is very strongly connected to it. One example is (perhaps) the Lov´asz Local Lemma [299], originally invented for problems very strongly connected to Extremal Graph Theory.39

2.8. Ramsey Theory and the birth of the Random Graph Method

There are many cases when some Ramsey type theorem is very near to a density theorem. In graph theory perhaps one of the ﬁrst such results was that of Chv´atal [186]. Faudree, Schelp and others also proved many results on the Ramsey topic, where in one colour we exclude a large tree. Faudree and Simonovits discussed in [336] this connection.

Erd˝s Magic. Tur´an thought that two-colouring Kn, say, in RED and BLUE, we shall always have a monochromatic Km with m > √n. The reason he thought this was (most probably) that for n = m2, Tn,m yields a 2-colouring of Kn (where the edges of Tn,m are RED, the others are BLUE), and thus Kn does not contain any RED Km+1, neither a BLUE Km+1 and this construction seemed to be very nice. So Tur´an thought this maybe the best. When Tur´an asked Erdo˝s about this, right after the war, Erdo˝s answered that in a random colouring of Kn the largest monochromatic Kp has order at most (2+o(1))log2 n (for sharper results see e.g., Bollob´s and Erdo˝s [125]). In some sense, this was the beginning of the Theory of Random graphs. Joel Spencer calls this “the Erdo˝s Magic” and discusses this story in details, e.g., in [778], or in [779], where he describes this and also the whole story of R(3,k), its estimate by Erdo˝s [261], by Ajtai, Koml´os and Szemer´edi [9], the application of the Lov´asz Local Lemma [299] by Spencer[776], and ﬁnally the matching deep result of Jeong Han Kim [515], using the Ro¨dl nibble and many other deep tools.

![image 42](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile42.png>)

So we see that most of the graphs Gn are counterexamples to this conjecture of Tur´an, however, we cannot construct graph sequences (Gn) without complete graphs on ⌊c log n⌋ vertices and independent set of vertices of size ⌊c log n⌋. Actually, to construct such graphs is a famous open problem of Paul Erdo˝s, weakly approximated, but still unsolved.40

One of the beautiful conjectures is Conjecture 2.30 (Vera So´s). A Ramsey graph is quasi-random.

![image 43](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile43.png>)

- 39The Lova´sz Local Lemma is one of the most important tools in Probabilistic Combinatorics (including the application of probabilistic methods). Its proof is very short, and it is described, among others, in the Alon-Spencer book [48], in Spencer [777], or in the original paper, available at the “Erd˝s homepage” [826].
- 40One problem with this sentence is that the notion of “construction” is not well deﬁned, one of us witnessed a discussion between Erd˝s and another excellent mathematician about this, but they strongly disagreed. As to the constructions, we mention the Frankl-Wilson construction of Ramsey graphs [359], or some papers of Barak, Rao, Shaltiel, and Wigderson [89] and others.


Of course, here we should know what is a Ramsey graph and when is a graph quasi-random. We formulate this only in the simplest case. Given an integer m, let N = R(m,m) be the smallest integer for which 2-colouring KN we must have a monochromatic Km. A Ramsey graph is a graph on R(m,m) − 1 vertices not containing Km, nor m independent vertices. The notion of quasi-randomness came originally, in a slightly hidden form from the works of Andrew Thomason [802] (connected to some Ramsey problems). Next it was formulated in a more streamlined form by Chung, Graham, and Wilson [185] and here, without going into details, we “deﬁne” it as follows.

Definition 2.31. For p > 0 ﬁxed, a sequence (Gn) of graphs is p-quasi-random if e(Gn) = p n2 + o(n2), and the number of C4’s in Gn is 6 n4 p4 + o(n4), as in the random Binomial graph Rn,p, with edge-probability p.

The following beautiful theorem also supports the So´s Conjecture.

Theorem 2.32 (Pro¨mel and Ro¨dl [661]). For any c > 0 there exists a c∗ > 0 such that if neither Gn nor its complementary graph contains a K[clogn] then Gn contains all the graphs Hℓ of ℓ = [c∗ log n] vertices.

— · —

Lovasz´ Meta-Theorem. Many years ago Lov´asz formulated the principle that the easier is to obtain a “construction” for a problem by Random Methods, the more complicated it is to obtain it by “real construction”.

Supporting examples were those days, among others,

- • the above “missing” Ramsey Construction,
- • the Expander Graph problem, and
- • also some good codes from Information Theory. The random graphs have good expander properties. Expander graphs are


important in several areas, among others, in Theoretical Computer Science. The fact that the random graphs are expanders were there in several early papers implicitly or explicitly, see e.g. Erdo˝s and R´enyi, [307], Po´sa [660].

Remark 2.33. Pinsker [651] proved the existence of bounded degree expanders, using Random Methods, and the construction of Margulis [607] was a breakthrough in this area. They were used e.g. in the AKS Sorting networks [11].

2.9. Dichotomy, randomness and matrix graphs

In the areas considered here, there are two extreme cases: (a) sometimes for some small constant ν we partition the n vertices into ν classes U1,...,Uν and join the vertices according to the partition classes they belong to: if some vertices x ∈ Ui and y ∈ Uj, x = y are joined then all the pairs x′,y′ are joined for which x′ ∈ Ui and y′ ∈ Uj, x′ = y′. These graphs can be described by a ν×ν

matrix, and therefore can be called matrix-graphs. 41 (Similar approach can be used in connection with edge-coloured graphs, multigraphs and digraphs.)

Often such structures are the extremal ones, in some others the random graphs. We could say that a dichotomy can be observed: sometimes the extremal structures are very simple, in some other cases they are very complicated, randomlike, fuzzy. (One very important feature of the random graphs is that they are expanders. This is why in a random graph much fewer edges ensure Hamiltonicity than in an arbitrary graph.)

2.10. Ramsey problems similar to extremal problems

In some cases the Ramsey graphs are chaotic, see above, in some other (mainly oﬀ-diagonal) cases they are very similar to Tn,k. Below we shall discuss only those cases of oﬀ-diagonal Ramsey Numbers that are strongly connected to Extremal Graph Theory.42 The area where the required monochromatic subgraphs are not complete graphs started with a paper of Gerencs´er and Gy´arf´as [390]. Given two graphs, L and M, the Ramsey number N = R(L,M) is the minimum integer N for which any RED-BLUE-colouring of KN contains a RED L or a BLUE M. Gy´arf´as and Gerencs´er started investigating these problems, Bondy and Erdo˝s [135] discussed the case when both L and M are cycles. Chv´atal [186] proved that

Theorem 2.34. If Tm is any ﬁxed m-vertex tree, then R(Tm,Kℓ) = (ℓ − 1)(m − 1) + 1. A construction yielding a lower bound is obvious: consider the Tur´an graph

T(ℓ−1)(m−1),m−1. Colour its edges in RED and the complementary graph in BLUE. Observe that the construction yielding a lower bound in this theorem is

the Tur´an graph Kℓ−1(m − 1,...,m − 1). Faudree, Schelp and others proved many results on these types of oﬀ-diagonal Ramsey problems.

Remark 2.35 (Simple Ramsey extremal structures). In several cases the Ramsey-

extremal, or at least the Ramsey-almost extremal structures can be obtained from partitioning n vertices into a bounded number C1,...,Cm of classes of vertices and colouring an edge xy according to the classes of their endpoints: all the edges where x ∈ Ci and y ∈ Cj have the same colour, for all 1 ≤ i,j ≤ m. This applies, e.g., to the path Ramsey numbers described by Gerencs´er and Gy´arf´s [390].

Occasionally some slight perturbation of such structures also provides Ramsey-

extremal colourings. Such examples occur in connection with the cycle Ramsey numbers, e.g., the ones in the Bondy-Erdo˝s conjecture on the Ramsey numbers on odd cycles [135], and in many other cases.

![image 44](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile44.png>)

- 41A generalization of these graphs is the generalized random graph, where we join the two vertices with probability pij, independently.
- 42The Ramsey numbers R(L, M) form a twice inﬁnite matrix whose rows and columns are indexed by the graphs L and M. If L = M, then R(L, M) is called “oﬀ-diagonal”.


- 2.11. Applications in Continuous Mathematics

Toward the end of his life Tur´an wrote a series of papers, starting perhaps with [809], the last ones with Erdo˝s, Meir, and So´s, [301, 300, 302, 303] on the application of his theorem in estimating the number of short distances in various metric spaces, or in estimating some integrals, potentials.43 He also liked mentioning a similar result of G.O.H. Katona [488] where Katona applied Tur´an’s theorem to distributions of random variables. Perhaps the ﬁrst result of Katona in this area was

Theorem 2.36. Let a1,...,an be d-dimensional vectors, (d ≥ 1), with |ai| ≥ 1 for i = 1,...,n. Then the number of pairs (ai,aj) (i = j) satisfying |ai+aj| ≥ 1 is at least

t(t − 1) if n=2t (even) t2 if n=2t+1 (odd).

Somewhat later A. Sidorenko (under the inﬂuence of Katona) also joined this research [742, 744]. They proved continuous versions of discrete (extremal graph) theorems, mostly to apply it in analysis and probability theory.

Remark 2.37. Sidorenko also reformulated the Erdo˝s-Simonovits conjecture [759] in the language of integrals, [745, 746]. The original conjecture had various forms, but all these forms asserted that if L is bipartite, and E is noticeably larger than ex(n,L), then among all the graphs Gn with E edges, the Random Graph has the fewest copies of L. The weakest form of this conjecture is that

Conjecture 2.38 (Erd˝os-Simonovits [759]). For any bipartite L, there exist two constants, C = CL > 0 and γ = γL > 0, such that if e(Gn) > Cex(n,L), then Gn contains at least

γ · nv

E n2

![image 45](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile45.png>)

e

copies of L, for e = e(L) and v = v(L).

These forms were primarily referring to the sparse case, when E is slightly above ex(n,L). On the other hand, Sidorenko’s form becomes meaningful only for dense graph sequences. For some more details on this, see F¨uredi and Simonovits, [386] or Simonovits [759], or Sidorenko [745].

- 2.12. The Stability method


In this section we shall describe the Stability method in a somewhat abstract form, but not in its most general form. Stability in these cases mostly means that for a property P we conjecture that the optimal objects have some simple structure, and the almost optimal structures are very similar to the (conjectured) optimal ones, in some mathematically well deﬁned sense. There are

![image 46](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile46.png>)

43We mention just a few related papers, for a more detailed description of this area see the remarks of Simonovits in [810], and the surveys of Katona [490, 491].

various forms of the stability methods, here we restrict ourselves to one of them. A “property” below is always a subset of the Universe. Generally we have two properties, P and a much simpler property/subset Q ⊆ P. If a family L of excluded graphs is given, then Pn := P(n,L) is the family of n-vertex L-free graphs.

The Stability method means that the optimization is easy on Qn and we reduce the “optimization on Pn” to “optimization on Qn”, e.g., – when we try to maximize the number of edges, – by considering a conjectured extremal graph Sn and showing that if Gn ∈ Pn − Qn, then e(Gn) < e(Sn). So, since the maximum is at least e(Sn) it must be attained in Qn.

We start with three examples. We wish to maximize some function e(G) on the n-element objects of P, denoted by Pn. Examples: (where e(Gn) is the number of edges).

- (a) P means that Kp+1  ⊆ G and Q is the family of p-chromatic graphs. It is easy to maximize e(Gn) for ≤ p-chromatic graphs.
- (b) P is the family of Dodecahedron-free graphs: P := {G : D12  ⊆ G},

Pn := P(n,D12), and Qn = Q(n,p,s) is the family of n-vertex graphs from which one can delete ≤ s − 1 vertices to get a ≤ p-chromatic graph. It is easy to prove that Q(n,6,2) ⊆ P.44

Simonovits conjectured that the extremum is attained by a graph H(n,2,6), where H(n,p,s) is the generalization of Tn,p: the n-vertex graph having the maximum number of edges in Q(n,p,s). Next he proved

that if Gn ∈ P −Q(n,2,6) then e(Gn) < e(H(n,2,6))− 12n+O(1). So, to maximize e(Gn) was reduced to maximizing it in Q(n,2,6), which is easy.

![image 47](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile47.png>)

- (c) P is the family of Octahedron-free graphs and Qn is the family of those graphs Gn where V (Gn) can be partitioned into V1 and V2 so that G[V1] does not contain C4 and G[V2] does not contain P3. Again, it is not too diﬃcult to prove that Qn ⊆ P. Using this, Erdo˝s and Simonovits, applying a stability argument [314], determined the exact extremal graphs for large n. (Actually, they proved a much more general theorem on EX(n,Kp+1(a1,...,ap)).)


It is worth mentioning the simplest case of (c):

Theorem 2.39 (Erd˝os-Simonovits [314]). There exists an n0 such that if n > n0 and Sn is extremal for the Octahedron graph K(2,2,2), then V (Sn) can be partitioned into into two parts, A and B so that A spans a C4-extremal graph in Sn, B spans a P3-extremal graph and each x ∈ A is joined to each y ∈ B.

The product conjecture asserts that

![image 48](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile48.png>)

44This is equivalent to that deleting any 5 vertices of D12 one gets ≥ 3-chromatic graphs.

Conjecture 2.40 (Simonovits, see [758]). If the decomposition class M of a ﬁnite L does not contain trees or forests, then each Sn ∈ EX(n,L) is a product of p subgraphs of (n/p) + o(n) vertices, where p is deﬁned by (2.4).

— · —

Let us ﬁx a Universe, for the sake of simplicity, the universe of graphs or hypergraphs. Now we repeat what we said above, in a slightly more detailed form. The method of stability means that

- (a) We consider an extremal graph problem, where some property P, and two parameters n and e are given (mostly n is the number of vertices and e is the number of the edges) and we try to optimize, say maximize e for

ﬁxed n, on Pn ⊆ P, where Pn is the family of objects in P having the parameter n.

- (b) We have a property Q ⊆ P “strongly” connected to the considered extremal problem. Qn is the corresponding subfamily of Q with parameter n. We assume that the maximization is diﬃcult on Pn but easy on Qn.
- (c) We prove that the maximum is smaller on Pn −Qn than on Pn, therefore the extremal objects in Pn, (i.e. the ones achieving the maximum) must be also in Qn, where it is easy to ﬁnd them.


This approach, introduced by Simonovits [750], turned out to be very fruitful for many problems, e.g., for the extremal problems of the icosahedron, dodecahedron, and octahedron, and for several other graph problems, and in several hard hypergraph problems, e.g. in case of the Fano hypergraph extremal problem [385, 504], or the results of F¨uredi, Pikhurko, and Simonovits [380, 381], (and many similar hypergraph results) see Subsection 8. We can say that in the last twenty-thirty years it became widely used. Below we list some papers connected to the stability method, from a much longer list. See e.g. Balogh, Mousset, Skokan, [80], D. Ellis, [256], E. Friedgut [362], F¨uredi, Kostochka and Luo [375], F¨uredi, Kostochka, Luo and Verstra¨ete [377, 376] W.T. Gowers and O. Hatami [408], Gy´arf´s, G.N. Sa´rk¨ozy, and Szemer´edi, [438], Keevash [495], Keevash and Mubayi [503] Nikiforov and Schelp [633], Mubayi [623], Patk´os [642], Samotij [714], Tyomkyn and Uzzell [811].

Stability method is used, e.g., in Subsection 6.3, more precisely, in the corresponding paper [446] of P. Hajnal, S. Herdade, and Szemer´edi, – however, in a much more complicated form, – to provide a new proof of the Po´sa-Seymour conjecture, without using the Regularity Lemma, or the Blow-up Lemma.

These papers were selected from many-many more and below we add to them some on the stability of the Erdo˝s-Ko-Rado [298] which started with the paper of A.J. Hilton and E.C. Milner [463], Balogh, Bollob´as, and Narayanan [61] and continued with several further works, like Das and Tran [226], Bollob´as, Narayanan and A. Raigorodskii [129], Devlin and Jeﬀ Kahn [239], D. Ellis, N. Keller, and N. Lifshitz, [257], ...

Remark 2.41. In [750], where Simonovits introduced this Stability Method, another stability proof method was also introduced, the Progressive Induction. That meant that the extremal graphs became more and more similar

to the conjectured extremal graphs as n increased, and ﬁnally they coincided. This approach was useful when the conjectured theorem could have been proved easily by induction, but it was diﬃcult to prove the Induction Basis.

- 2.13. The “typical structure”


The results considered here are related to the situation described in the previous section, on the P − Q-stability, and have the following form: we have two properties, a complicated one, P, and a simpler one, Q ⊂ P and we assert:

Almost all n-vertex P-graphs have property Q.

Among the simplest ones we have already mentioned or will discuss the following ones.

- (a) Almost all Kp+1-free graphs are p-chromatic [297, 531].
- (b) Almost all Berge graphs are perfect [664] (cf Remark 8.11).
- (c) Almost all K(2,2,2)-free graphs have a vertex-partition, where the ﬁrst class is C4-free and the second one is P3-free, [64].


— · —

Erdo˝s conjectured that, given a family L of forbidden graphs, it may happen that a large part of the L-free graphs are subgraphs of some extremal graphs Sn ∈ EX(n,L), in the following sense. Denote by P(n,L) the family of n-vertex L-free graphs. The subgraphs of an L-extremal graph Sn provide 2ex(n,L) L-free graphs.

Conjecture 2.42 (Erd˝os). If L contains no bipartite L, then |P(n,L)| = O(2(1+o(1))ex(n,L)).

The ﬁrst such result, by Erdo˝s, Kleitman, and Rothschild [297] asserted that for L = {Kp+1},

log2 |P(n,L)| = (1 + o(1))ex(n,L).

Later Erdo˝s, Frankl, and Ro¨dl [288] proved Erdo˝s’ conjecture, for any nondegenerate case. Kolaitis, H.J. Pr¨mel, B.L. Rothschild, [531] extended some related results to the case of L with critical edges, see Meta-Theorem 2.19. An important related result is that of Pr¨mel and Steger [665]. Slowly a whole theory was built up around this question. Here we mention in details just a few results, and then list a few related papers.

Theorem 2.43 (Erd˝os, Frankl, and Ro¨dl [288]). If L does not contain bipartite graphs, and P(n,L) denotes the family of n-vertex L-free graphs, then

2).

|P(n,L)| < 2ex(n,L)+o(n

For sharper results, see Balogh, Bollob´s, and Simonovits [62, 63, 64]. The cases (a) and (c) mentioned above are also connected to this Erd˝os-Frankl-Ro¨dl theory.

If one counts the number of L-free graphs Gn for a bipartite L, then one faces several diﬃculties. We recommend the papers of Kleitman and Winston [523], Kleitman and D. Wilson [522] and of Morris and Saxton [618].

We get another “theory” if we exclude induced subgraphs, see e.g. Pr¨omel and Steger [662, 665], Alekseev [13], Bollob´s and Thomason [130, 131]. The theory is similar, however, the minimum chromatic number of L ∈ L must be replaced by another, similar colouring number. For some further, related results see Alon, Balogh, Bollob´s, and Morris [24]. ...

A more general and sharper question is when the considered family of graphs is P, and the property Q is strongly connected to P, then one can ask: is it true that almost all graphs Gn ∈ P are also in Q. This often holds, e.g., almost all K3-free graphs are bipartite. Again, a ﬁner result, explained below, is

Theorem 2.44 (Osthus, Pr¨mel and Taraz [636]). Let Tp(n,Γ) denote the family of Kp-free graphs with Γ edges. If

√3 4

![image 49](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile49.png>)

![image 50](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile50.png>)

n3/2 log n,

t3 = t3(n) :=

![image 51](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile51.png>)

then for any ﬁxed ε > 0, the probability that a random K3-free graph on n vertices and Γ edges is bipartite,

 

1 if Γ = o(n),

- 0 if 21n ≤ Γ ≤ (1 − ε)t3(n);

![image 52](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile52.png>)

- 1 if Γ ≥ (1 + ε)t3(n).


(2.6)

P(Gn ∈ T3(n,Γ) =⇒ χ(Gn) = 2) →



The most important line of (2.6) is the third line. Actually, this “story” started with a result of Pr¨mel and Steger [666], where the threshold-estimate was around n7/4 for the third line of (2.6). Pr¨mel and Steger conjectured that the right exponent is 3/2.  Luczak [601] proved a slightly weaker related result, where the exponent was 3/2, however, instead of asking for bipartite graphs, he asked only for “almost bipartite” graphs.

The meaning of this theorem is that for very small Γ = e(Gn) most of the graphs will have no cycles, therefore they will be bipartite. For slightly larger e(Gn) odd cycles will (also) appear, so there will be a “slightly irregular” interval, and then, somewhat above t3(n) everything becomes nice: almost all triangle-free graphs are bipartite.

Remark 2.45. (a) One could ask why cn√n log n is the threshold for our problem. As [636] explains, this is connected to the fact that this is the threshold where the diameter of a random graph becomes 2.

![image 53](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile53.png>)

- (b) A nice result of this paper extends the theorems from K3-free graphs to

C2h+1-free random graphs.

- (c) Another important generalization of this result is due to Balogh, Morris,


Samotij, and Warnke [79] to any complete graph Kp.

Further information can be found on these questions in the paper of Balogh, Morris, Samotij, and Warnke [79], which, besides formulating the main results of [79], i.e., extending Theorem 2.44 to any Kp,45 provides an excellent survey of this area and its connection to several other areas, among them to the problems on extremal subgraphs of Random Graphs, investigated also by Conlon and Gowers [199], ..., see Section 2.5/§(f).

As we have mentioned, here the situation for the degenerate (bipartite) case is completely diﬀerent. Related results are, e.g., Balogh and Samotij [85, 86, 87], or Morris and Saxton [618].

Historical Remarks 2.46. This whole story started (perhaps) outside of Graph Theory, with some works of Kleitman and Rothschild, see [519, 520, 521].

A hypergraph analog of these results was proved by Nagle and Ro¨dl [628]. Among the newer results we have mentioned or should mention several results of Pr¨omel and Steger, e.g., [663, 664], Alon, Balogh, Bollob´s, and Morris [24] and, on hypergraphs, Person and Schacht [645], Balogh and Mubayi [81, 82], ...

- 2.14. Supersaturated Graphs When Tur´an proved his theorem, Rademacher immediately improved it:


- Theorem 2.47 (Rademacher, unpublished). If e(Gn) > ⌊n

2

![image 54](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile54.png>)

4 ⌋ then Gn contains at least n2 copies of K3.

![image 55](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile55.png>)

This is sharp: putting an edge into a larger class of Tn,2 we get n2 triangles. More generally, putting k edges into the larger class of Tn,p we get ≈ k(np)p−1 copies of Kp+1, and in particular, for p = 2 we get k n2 triangles. So Erdo˝s generalized Rademacher Theorem:

![image 56](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile56.png>)

![image 57](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile57.png>)

![image 58](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile58.png>)

- Theorem 2.48 (Erd˝os (1962), [265]). There exists a c > 0 such that for any


2

4 ⌋ + k then Gn contains at least k n2 copies of K3.

0 < k < cn, if e(Gn) ≥ ⌊n

![image 59](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile59.png>)

![image 60](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile60.png>)

Erdo˝s conjectured that his result holds for any c ≤ 12.46 He also generalized his result to Kp+1 in [274].47 Lov´asz and Simonovits proved the Erdo˝s conjecture, in [592], and a much more general theorem in [593].

![image 61](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile61.png>)

Let F(n,L,E) be the minimum number of copies of L ⊆ Gn with e(Gn) = E > ex(n,L) edges. Lov´asz and Simonovits determined F(n,Kp+1,E), for

- e(Tn,p) < E < e(Tn,p) + cpn2, for an appropriately small cp > 0, using the stability method, and, more generally, for any q ≥ p, and e(Tn,q) ≤ E <
- e(Tn,q) + cqn2. In Subsection 2.15 we formulate the related, widely applicable Lov´asz-Simonovits Stability Theorem.


- Remark 2.49. The Lov´asz-Simonovits method did not work in the general case, farther away from the Tur´an numbers. Their Supersaturated Graph result, on


![image 62](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile62.png>)

45The Master Thesis of Warnke contained results on K4. 46Again, there is some diﬀerence between the cases of even and odd n. 47Erd˝s’ paper contains many further interesting and important results.

the number of complete subgraphs, was extended by Fisher and Ryan [343], by Razborov [669], then by Nikiforov [632], and ﬁnally, by Reiher [672]. For a related structural stability theorem see also the paper of Pikhurko and Razborov [650].

We complete this section with a C5-Supersaturated theorem:

- Theorem 2.50 (Erd˝os (1969), [274]). If e(G2n) = n2 + 1 then G2n contains at least n(n − 1)(n − 2) pentagons.

As Erdo˝s remarks, a K(n,n) with an extra edge added shows that his theorem is sharp. For some generalizations see Mubayi [624]. For early results on supersaturated graph results see e.g. the survey of Simonovits [759], explaining how the proofs of some extremal theorems depend on supersaturated graph results, the papers of Blakley and Roy [111], of Erdo˝s [265, 274], Erdo˝s and Simonovits [316, 317], Brown and Simonovits [158], the next subsection, and many further results.

2.15. Lov´asz-Simonovits Stability theorem

To prove and generalize Erdo˝s’ conjecture on K3-supersaturated graphs, Lov´asz and Simonovits proved a “sieve”, the simplest form of which is the following:

- Theorem 2.51. For any constant C > 0, there exists an ε > 0 such that if

|k| < εn2 and Gn has ⌊n

2

![image 63](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile63.png>)

4 ⌋ + k edges and fewer than C|k|n triangles K3, then one can change O(|k|) edges in Gn to get a bipartite graph.

Here mostly we use k > 0, but if we have the theorem for k > 0, that immediately implies its extension for k ≤ 0 as well. Let m(L,G) denote the number of labeled copies of L in G. The more general form is related to any Kp and not only around ex(n,Kp), but more generally, when we wish to estimate m(Kp,G) and e(Gn) is around any ex(n,Kq), for q ≥ p.

In the next, more general theorem t and d are deﬁned by

e(Gn) = 1 −

1 t

![image 64](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile64.png>)

n2 2

![image 65](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile65.png>)

and d = ⌊t⌋.

- Theorem 2.52 (Lov´asz–Simonovits [593]). Let C ≥ 0 be an arbitrary constant. There exist positive constants δ > 0 and a C′ > 0 such that if −δn2 < k < δn2 and Gn is a graph with


e(Gn) = e(Tn,p) + k edges and

p

t p

n p

+ Cknp−2,

m(Kp,Gn) <

![image 66](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile66.png>)

then there exists a Kd(n1,...,nd) such that ni = n, |ni − nd| < C′√

![image 67](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile67.png>)

k and Gn can be obtained from Kd(n1,...,nd) by changing at most C′k edges.

![image 68](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile68.png>)

Here t can be regarded as a “fractional Tur´an-class-number”. To explain the meaning of this theorem, remember that if one puts k edges into the ﬁrst class of a Tn,p, that creates ≈ c1knp−2 copies of Kp. This theorem asserts that in a graph Gn with e(Tn,p) + k edges, either we get much more copies of Kp, or Gn must be very similar in structure to Tn,p.48

Theorem 2.52 can be used in many cases, e.g., it provides a clean and simple proof of the Erdo˝s-Simonovits Stability Theorem.

- Remark 2.53. Assume that p ≥ 3 and k = γn2, for some constant γ > 0.

If one knows Theorem 2.52 for Kp, then one has it for any p-chromatic L, by applying the Erdo˝s Hypergraph Theorem 8.1 to the v-uniform hypergraph on V (Gn), for v := v(L), whose hyperedges are the vertices of the copies of L in Gn. (For the details see, e.g., Brown and Simonovits [158].) Hence Theorem 2.52 is more general than the Erdo˝s-Simonovits Stability theorem, since it does not completely exclude L ⊂ Gn, only assumes that Gn does not contain too many copies of L.

- Remark 2.54. One could ask why do we call Theorem 2.52 a “sieve”. Without answering this question, we make two remarks.

- (a) The methods used here could be considered in some sense “primitive”

predecessors of what today is called Razborov’s Flag algebras.

- (b) This whole story started with a “survey” paper of Lov´asz [585], written


in Hungarian, the title of which was “Sieve methods”.

- Remark 2.55. Often the Lov´asz-Simonovits sieve can be replaced by the Removal Lemma.
- Remark 2.56. The original proofs of the Erdo˝s-Simonovits Limit theorem could have used the Regularity Lemma, (described in Section 5), or this theorem, but they had not: actually they were proved earlier. An alternative approach to prove the Erdo˝s-Simonovits Stability theorem is to use the Regularity Lemma, however, then one needs the stability theorem itself for complete graphs. A


simple, beautiful proof of that the stability holds for Kp was found by F¨uredi [374], who used for this purpose the Zykov symmetrization [825].

- 2.16. Degenerate vs Non-degenerate problems


We remind the reader that an extremal graph problem is Degenerate if ex(n,L) = o(n2), or in case of r-uniform hypergraphs, ex(n,L) = o(nr). Another way to describe a Degenerate extremal problem is that L contains a bipartite L (and for hypergraphs, L contains an L with strong chromatic number r, see Claim 8.2). The survey of F¨uredi and Simonovits [386] describes the

![image 69](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile69.png>)

48This theorem may remind us of the Removal Lemma, (see Subsection 5.4) yet, it is diﬀerent in several aspects. Both they assert that either we have many copies of L in Gn, or we can get an L-free graph from Gn by deleting a few edges. However, the Removal Lemma has no condition on e(Gn) and the Lova´sz-Simonovits theorem provides a much stricter structure.

This result can also be used for negative values of k, (and sometimes we need this), however, then we should replace k by |k| in some of the formulas.

details. Here we shall be very brief, describe just a few results and formulate three conjectures and describe some connections to Geometry, Finite Geometry, and Commutative Algebra.

So let us restrict ourselves to simple graphs. The simplest questions are when L = K(a,b) and when L = C2k. (The extremal problem of the paths Pk is a theorem of Erdo˝s and Gallai [289].)

For a = 2 and a = 3 the sharp lower bounds came from ﬁnite geometric constructions of Erdo˝s, R´enyi, V. T. So´s, [308] and W. G. Brown [150]. The random methods gave only much weaker lower bounds. By [306],49

a−1b .

1

ex(n,K(a,b)) > can2−

![image 70](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile70.png>)

![image 71](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile71.png>)

The Koll´ar-R´onyai-Szab´o construction [532] and its improvement, the AlonRo´nyai-Szab´o [42] construction, (proving the sharpness of Theorem 2.9 when a is much smaller than b) used Commutative Algebra, and Lazebnik, Ustimenko, and Woldar have several more involved algebraic constructions.

Remark 2.57. One of Erdo˝s’ favourite geometry problem was the following: Given n points in Ed, how many equal (e.g., unit) distances can occur among them. Among others, he observed that if in E3 we join two points iﬀ their distance is 1, then the resulting graph does not contain K(3,3). In Brown’s construction this is turned around: the vertices of a graph Gn are the n = p3 points of a ﬁnite 3-dimensional aﬃne space AG(p,3). W.G. Brown joined two points (x,y,z) and (x′,y′,z′) if their “distance” was “appropriate”:

(x − x′)2 + (y − y′)2 + (z − z′)2 = α, (mod p).

Then Brown proved that (for some primes p and some α) the resulting graph contains no K(3,3) and has ≈ 12n2−(1/3) edges. (Surprisingly, as F¨uredi proved in [373], – as to the multiplicative constant 21, – for K(3,3) the Brown construction is the sharp one, not the upper bound of Theorem 2.9.) The Commutative Algebra constructions [532, 42] can be regarded as extensions of Brown’s construction, however, with deeper mathematics in the background.

![image 72](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile72.png>)

![image 73](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile73.png>)

Question 2.58. Sometimes in our constructions we use commutative structures, sometimes non-commutative ones. One could ask, what is the advantage of using non-commutative structures.

The same question can also be asked in connection with the so called Ramanujan graphs, see e.g., [598, 599], or [609]. The answer is simple: the Cayley graphs of commutative groups are full of short even cycles. We illustrate this through the girth problem.

Theorem 2.59 (Bondy-Simonovits, Even Cycle: C2k [136]). ex(n,C2k) ≤ c1kn1+(1/k). (2.7)

![image 74](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile74.png>)

49Actually, the First Moment Method yields a little better estimate, but far from being satisfactory. One can also see that as a is ﬁxed and b gets larger, the “random construction” exponents converge to the optimal one. This motivates, among others, [532, 42]

Conjecture 2.60 (Sharpness). The exponent 1 + (1/k) is sharp, i.e. ex(n,C2k) ≥ ckn1+(1/k) for some ck > 0.

The ﬁrst unknown case is k = 4, ex(n,C8). Theorem 2.59 is sharp for C4, C6, C10, see [258], [308], [150] and [101]. For some related constructions see also Wenger [813].

Now, to answer Question 2.58, observe, that we often use in our algebraic constructions Cayley graphs, where in the commutative cases we have many “coincidences”, leading to many C2k ⊂ Gn, which can be avoided in the noncommutative cases. A very elegant (and important) example of this is:

Construction 2.61 (Margulis, [608]). There exist inﬁnite Cayley graph sequences (Gn,d) of degree d = 2ℓ with girth greater than clog(logd−n1).

![image 75](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile75.png>)

- Remark 2.62. We have emphasized that Extremal Graph Theory is connected to many other areas in Mathematics. The Margulis constructions [608] are connected to Coding Theory. In somewhat diﬀerent ways, several papers of F¨uredi and Ruszink´ are also extremal hypergraph results strongly connected to (or motivated by) Coding Theory, e.g., [383].

A more detailed analysis of these questions can be found, e.g., in Alon’s survey [22], or in the F¨uredi-Simonovits survey [386].

- Remark 2.63. (a) It was a longstanding open question if one can improve the coeﬃcient of n1+(1/k) in the Bondy-Simonovits theorem, from ck to o(k). After several “constant”-improvements, Boris Bukh and Zilin Jiang [163]50 proved that


√

![image 76](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile76.png>)

k log k · n1+(1/k) + O(n). (2.8)

ex(n,C2k) ≤ 80

According to [163], Bukh thinks that Conjecture 2.60 does not hold: he conjectures that for suﬃciently large, but ﬁxed k,

ex(n,C2k) = o(n1+(1/k)). It is very “annoying” that we cannot decide this, not even for C8.

- (b) Related constructions were provided by Lazebnik, Ustimenko, and Woldar [567, 568, 569] and by Imrich [473].
- (c) For some ordered versions of the C2k problem see, e.g., the (very new) results of Gy˝ori, Kor´ndi, Tomon, Tompkins, and Vizer [443].


Historical Remarks 2.64. (a) Actually, before the Erdo˝s-Simonovits paper [313] Erdo˝s conjectured that the exponents can be only either (2− k1) or (1+ k1). This conjecture was “killed” in [313], by some “blow-up” of the cube.

![image 77](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile77.png>)

![image 78](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile78.png>)

(b) Later Erdo˝s and Simonovits conjectured that (i) for any rational exponent α ∈ [1,2) there exist degenerate extremal problems ex(n,L) for which

ex(n,L)/nα → cL > 0, (2.9)

![image 79](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile79.png>)

50The original version claimed a slightly better estimate.

and (ii) for any degenerate problem ex(n,L) there exists a rational α ∈ [1,2) for which (2.9) holds. Recently, Bukh and Conlon [162] proved (i). (For hypergraphs Frankl [354] has some earlier, corresponding results, see also Fitch [344]).

- 2.17. Dirac theorem: introduction

Diﬃcult problems always played a central role in the development of Graph Theory. We shall mention here two important problems, the Dirac theorem on Hamiltonian cycles (which is not so diﬃcult) and the Hajnal-Szemer´edi theorem on equitable partitions.

Theorem 2.65 (Dirac (1952), [242]). If n ≥ 3 and dmin(Gn) ≥ n/2, then Gn contains a Hamiltonian cycle.

If n = 2h, then K(h − 1,h + 1) has no Hamiltonian cycle, showing that Theorem 2.65 is sharp.51 One beautiful feature of this theorem is that as soon as we can guarantee a 1-factor, we get a Hamiltonian cycle.

This theorem triggered a wide research, see, e.g., Ore’s theorem [635], Po´sa’s theorem on Hamiltonian graphs [658], and related results. We shall return to discuss generalizations of Dirac’s Theorem, above all, the Po´sa-Seymour conjecture and the hypergraph generalizations in Sections 6.3 and 9.

- 2.18. Equitable Partition


We close this introductory part with a famous conjecture of Erdo˝s, proved by Andra´s Hajnal and Szemer´edi.

Definition 2.66 (Equitable colouring). A proper vertex-colouring of a graph G is Equitable if the sizes of any two colour classes diﬀer by at most one.

Theorem 2.67 (Hajnal-Szemer´edi (1969), [444]). For every positive integer r, every graph with maximum degree at most r has an equitable colouring with r+1 colours.

The theorem is often quoted in its complementary form. The sharpness is shown by the complementary graph of an almost-Tur´an graph, i.e. the union of complete graphs Kr and Kr+1.

The theorem was proved ﬁrst only for K3, by K. Corr´adi and A. Hajnal [209]. Then came the proof of Hajnal and Szemer´edi. Much shorter and simpler proofs of Theorem 2.67 were found independently by Kierstead and Kostochka, [510] and Mydlarz and Szemer´edi [627]. The paper of Kierstead, Kostochka, Mydlarz and Szemer´edi [513] provides a faster (polynomial) algorithm to obtain the equitable colouring.52

![image 80](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile80.png>)

- 51The union of two complete graphs of n/2 vertices having at most one common vertex in common also shows the sharpness. For = 2ℓ − 1 one can use K(ℓ, ℓ − 1) for sharpness.
- 52See the introduction of [513]. They also point out the applications of this theorem, e.g., in [36], [478] for “deviation bounds” for sums of weekly dependent random variables, and in the Ro¨dl-Rucin´ski proof of the Blow-up Lemma [687].


Multipartite case. This theorem was generalized in several diﬀerent ways, also, considered for multipartite graphs Gn by Martin and Szemer´edi [613], Csaba and Mydlarz [216], Extensions towards multipartite hypergraphs can be found, e.g., in Lo-Markstr¨m [576]. It is applied to prove some other graph theorems, e.g., in Koml´os-S´ark¨ozy-Szemer´edi [540, 542, 543], and many other cases. We shall return to these questions in Section 7.

The theorem was extended also to directed graphs, by Czygrinow, DeBiasio, Kierstead, and Molla [219].

Random Graphs. The problem of equitable partitions in Random Graphs was also discussed (and in some sense solved) in works of Bohman, Frieze, Ruszink´o, and Thoma [114]. Their result was improved by Johansson, Jeﬀ Kahn, and Van Vu [480].

- 2.19. Packing, Covering, Tiling, L-factors


When speaking of “packing”, sometimes we mean edge-disjoint embedding of just two graphs (this is connected to some complexity questions from Theoretical Computer Science) and sometimes we try to cover the whole graph with some vertex-disjoint copies of a graph.53

There was a period, when – because of Theoretical Computer Science, – packing a graph into the complementary graph of another (i.e. the above problem for two edge-disjoint graphs) was a very actively investigated topic. This was connected to Evasiveness, i.e. to the problem, how many “questions” are needed to decide if a graph Gn has property P.

The whole area is described in a separate chapter of Bollob´s’ “Extremal Graph Theory” [119]. For some further related details see also the papers of Bollob´s and Eldridge, e.g., [123] with the title “Packing of Graphs and Applications to Computational Complexity”. Here we mention also the result of P. Hajnal [445], (improving some important earlier results). He proves that the randomized decision tree complexity of any nontrivial monotone graph property of a graph with n vertices is Ω(n4/3). See also Bollob´s [118], and [517, 518]. This is again a nice example where Combinatorics and Theoretical Computer Science are in a very strong interaction.

— · —

Given a graph Gn, and a sample graph L, a perfect tiling is a covering of V (Gn) with vertex-independent copies of L, and an almost-tiling is covering at least n − o(n) vertices of it. Tiling is sometimes a tool, a method, in other cases it is the aim. The Corr´adi-Hajnal and the Hajnal-Szemer´edi theorems, in Section 2.18, were also about packing=tiling of graphs.

Perhaps the ﬁrst case when tiling was used in a proof was the RademacherTur´an theorem of Erdo˝s [265], Here Erdo˝s covered as many vertices of Gn by vertex-independent triangles as he could, to prove the theorem.

![image 81](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile81.png>)

53In the Gya´rf´s Conjecture we try to pack many diﬀerent trees into a complete graph.

We can consider the problem of Tilings in a more general way. Here we have a (small) sample graph L and wish to embed into Gn as many vertexindependent copies54 of L as possible. The question is, given an integer t, which conditions on Gn ensure, e.g, t vertex-independent copies of L. We shall return to this question later, here we mention just a few related results, as illustrations. As we mentioned, Theorem 2.67 is an example of such results. Below we formulate some more general results.

Definition 2.68. Given two graphs L and G, where v(L) divides v(G), an L-factor of G is a family of v(G)/v(L) vertex-disjoint copies of L,

- Theorem 2.69 (Alon and Yuster (1996), [49]). For every ε > 0, and for every positive integer h, there exists an n0 = n0(ε,h), such that for every “sample” graph Lh, every “host” graph Gn with n = hℓ > n0 vertices and minimum degree

dmin(Gn) ≥ 1 −

1 χ(L)

![image 82](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile82.png>)

+ ε n (2.10)

contains an L-factor.

As to the usage of names, tiling, packing, and perfect L-factor are almost the same: given a graph G and a sample graph L, we wish to embed into G as many vertex-independent copies of L as possible, and if they (almost) cover V (G), then we speak about an (almost) perfect tiling/packing.

Koml´os extended the notion of L-factor by saying that G has an L-factor, if it contains ⌊v(G)/v(L)⌋ vertex-independent copies of L. Alon and Yuster conjectured and Koml´os, G.N. Sa´rk¨ozy and Szemer´edi [543] proved the following55

- Theorem 2.70 (Komlo´s, Sa´rk¨ozy, and Szemer´edi). For every L there is a constant K = KL such that if


1 χ(L)

dmin(Gn) ≥ 1 −

![image 83](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile83.png>)

n + KL,

then Gn has an L-factor.

Koml´os surveyed the tiling situation in [534] in a more general way. He considered degree conditions for ﬁnding many disjoint copies of a ﬁxed graph L in a large graph G. Let τ(n,L,M) be the minimum m for which if dmin(Gn) ≥ m, then there is an L-matching covering at least M vertices in G. For any ﬁxed x ∈ (0,1), Koml´os determined

1 n

fL(x) = lim

τ(n,L,xn).

![image 84](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile84.png>)

n→∞

Thus, e.g, Theorem 8 of [534] determines (for a ﬁxed but arbitrary L) a sharp min-degree condition on Gn to enable us to cover ≈ xn vertices of Gn by copies

![image 85](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile85.png>)

- 54or, in other cases edge-disjoint copies. Here “vertex-independent” and “vertex-disjoint” are the same.
- 55Actually, they formulated two “similar” conjectures, we consider only one of them.


of L. Among others, Koml´os analyzed the strange and surprising diﬀerences between the cases when we try to cover Gn with vertex-independent copies of L completely, and when we try only to cover it almost completely, or when we try to cover only a large part, ⌊xn⌋ vertices of it. Several further details and a careful analysis of this situation can be found in the paper of Koml´os [534].

— · —

Kawarabayashi conjectured that Theorem 2.70 can be improved by taking into account the particular “colouring structure” of L. This was proved by Cooley, K¨uhn, and Osthus [203], and then by K¨uhn, and Osthus [562]. Koml´os, in [534] deﬁned a chromatic number χcr(L), improving the earlier results, by using this χcr. K¨uhn and Osthus deﬁned another “colouring parameter” hcχ depending on the sizes of the colour-classes in the optimal colourings of L. Using hcχ, they deﬁned a χ∗(L) ∈ [χ(L) − 1,χ(L)] and proved

- Theorem 2.71 (K¨uhn and Osthus (2007), [562]). If δ(L,n) is the smallest integer m for which every Gn with dmin(Gn) ≥ m has a perfect L-packing then

δ(L,n) = 1 −

1 χ∗(L)

![image 86](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile86.png>)

n + O(1).

Bipartite Packing. The packing problems, as many similar problems, have also bipartite versions. Hladk´y and Schacht – extending some results of Yi Zhao [822] – proved

- Theorem 2.72 (Hladk´y and Schacht (2010), [471]). Let 1 ≤ s < t, n = k(s+t). If


- 1

![image 87](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile87.png>)

- 2n + s − 1 if k is even


Φ2(n,L) :=

- 1

![image 88](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile88.png>)

- 2(n + t + s) − 1 if k is odd,


then each subgraph G ⊆ K(n,n) with minimum degree at least Φ2(n,L) contains a K(s,t)-factor, and this is sharp, except if t ≥ 2s + 1 and k is odd.

For the “missing case” (when t ≥ 2s + 1 and k is odd) see Czygrinow and DeBiasio [218].

- Remark 2.73. Here we have to be careful with using the word “factor”: Lov´asz, in his early papers [583, 584] called a subgraph Hn ⊆ Gn an f-factor if


f : V (Gn) → N, and degH(x) = f(x) for each x ∈ V (Gn).

Directed graphs. There are many further results connected to this area. We shall return to some of them later, e.g., in Sections 6.7 and 9.6.

Here we close this area with two analogous results on oriented graphs: directed graphs without loops, where between any two vertices there is at most one arc. δ0(G) is the minimum of all the in- and out-degrees.

- Theorem 2.74 (Keevash and Sudakov [505]). There exist a ﬁxed c > 0, and an


n0 such that if Gn is an oriented graph on n > n0 vertices and δ0(Gn) > (12−c)n, then Gn contains a “cyclic triangle” tiling which leaves out at most 3 vertices. This is sharp.

![image 89](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile89.png>)

- Figure 3: Cyclic triangles

Actually, Keevash and Sudakov [505] describe the history of this theorem in details, explain several related results, and prove that the theorem is sharp in the sense that if n ≡ 3 (mod 18) then one cannot guarantee covering the whole graph with

cyclic triangles, even under a stronger degree-condition. Further, they prove some other packing theorems where the lengths of some cycles are prescribed but they need not be triangles. We close with

Theorem 2.75 (Balogh, Lo, and Molla [73]). There exists an n0 such that for every n ≡ 0 (mod3), if n > n0, then any oriented graph Gn on n vertices with δ0(Gn) ≥ 718n contains a TT3-tiling, where TT3 is the transitively oriented triangle.

![image 90](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile90.png>)

- Figure 4: Transitive triangles


This area is fairly active nowadays, we refer to several papers on equitable colouring of Kostochka and others, e.g., [509, 550, 551], and we mention just some extensions to bipartite tiling, e.g., Czygrinow and DeBiasio [218], and to oriented graphs, by Czygrinow, DeBiasio, Kier-

stead, and Molla [223], [219], Yuster on tournaments [820] or [218], [221], or to hypergraphs, e.g., Pikhurko [647] or Czygrinow, DeBiasio, and Nagle [221], and several papers of Yi Zhao and Jie Han, e.g., [451], and many-many others. Some of these results are good examples of the application of the Absorbing methods, discussed in Subsection 6.5. This is, e.g., the case with the BaloghLo-Molla theorem or the Czygrinow-DeBiasio-Nagle result just mentioned.

#### 3. “Classical methods”

Here, (giving some preference to results connected to Laci Lov´asz) we still skip the area of graph limits, we skipped the applications of Lov´asz Local Lemma (though Lov´asz Local Lemma is among the most important tools in this area and it came from research strongly connected to extremal graph problems [299]), but we mention two other, less known results of Lov´asz, strongly connected to extremal graph theory.

3.1. Detour I: Induction?

Speaking of methods in Extremal Graph theory, we mostly avoided speaking of hypergraph results, partly because they are often much more involved than the corresponding results on ordinary graphs. One is the construction of graphs with high girth and high chromatic number. Erdo˝s used Random Graphs to prove the existence of such graphs [263, 264] and there was a long-standing challenge to construct them.56 Lov´asz often solved “such problems” by trying

![image 91](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile91.png>)

56We must repeat that the meaning of “to construct them” is not quite well deﬁned. Let us agree for now that the primary aim was to eliminate the randomness.

- 3. “Classical methods”, 41


to use induction, and when this did not work directly, to look for and ﬁnd a stronger/more general assertion where the induction was already applicable. In this case Lov´asz generalized the problem to hypergraphs and used induction [582]. His proof was a tour de force, rather involved but worked. It was the ﬁrst “construction” to get graphs of high girth and high chromatic number.

How is this problem connected to Extremal Graph Theory?

- Theorem 3.1. If L is a ﬁnite class of excluded graphs, then ex(n,L) = O(n) iﬀ L contains some tree (or forest).


To prove this, one needs the Erdo˝s result [264] about high girth graphs Gn with e(Gn) > n1+α edges, or the Erdo˝s-Sachs theorems [310], ..., or some corresponding Lubotzky-Phillips-Sarnak-Margulis graphs, see e.g. [598, 599]. (Lov´asz’ tour de force construction was a big breakthrough into this direction though it was not quantitative, which is needed above).

- Remark 3.2. Since that several alternative constructions were found. We mention here the construction of Neˇsetˇril and Ro¨dl [630]. Perhaps one of the best is the construction of Ramanujan graphs by Lubotzky, Phillips, and Sarnak [599] and Margulis [611]: it is very direct and elegant. It has only one “disadvantage”: to verify that it is a good construction, one has to use deep Number Theory. (For more detailed description of the topic, see [599], or the books of Lubotzky [597] and of Davidov, Sarnak, and Valette [227].)


- 3.2. Detour II: Applications of Linear Algebra We start with repeating a deﬁnition.


Definition 3.3. H is a colour-critical graph57 if for any edge e of H, χ(H−e) < χ(H). It is k-colour-critical if, in addition, it is k-chromatic.

The theory of colour-critical graphs is a fascinating area. Erdo˝s writes about its beginnings, e.g., in his article in the memory of Gabriel Dirac [286]. Gallai also had several interesting conjectures on colour critical graphs. One of them, on the independence number of a 4-chromatic colour-critical graph, was disproved by a construction of Brown and Moon [157], and then by Simonovits [752] and Toft [806]. The disproof was strongly connected to a hypergraph extremal problem discussed also by Brown, Erdo˝s, and So´s [154]. Lov´asz

Figure 5: Double Cone

improved the corresponding results, proving the following sharp and much more general result.

- Theorem 3.4 (Lov´asz, (1973), [586, 587]). Let αk(n) denote the maximum number of independent vertices in a k-critical graph on n vertices. Then


n − 2kn1/(k−2) ≤ αk(n) ≤ n − (k/6)n1/(k−2).

![image 92](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile92.png>)

57more precisely, edge-colour-critical graph.

The lower bound is based on generalizing the Brown-Moon construction and the upper bound improves the result of Simonovits, α4(n) ≤ n − c2n2/5. Simonovits in [752] and [753] used a hypergraph extremal problem, where the excluded hypergraphs were 3-uniform double-cones.58 One of his results was basically equivalent to a results of Brown, Erdo˝s, So´s [154], where the excluded graphs were all the triangulations of a 3-dimensional sphere (the double cones are among these hypergraphs). Actually, Simonovits proved

Theorem 3.5 (Simonovits [752]). If Cr3 denotes the (inﬁnite) family of 3-uniform r-cones, then

1

ex3(n,Cr3) = O(n3−

r ).

![image 93](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile93.png>)

(Watch out, here the subscript r is not the number of vertices!) Simonovits, and then Toft, and Lov´asz, reduced the general case of the Gallai problem to the case when each x ∈ X had degree d(x) = k − 1, and these vertices x deﬁned a (k − 1)-uniform hypergraph Hm on the remaining vertex-set M := V (Gn) − X. Simonovits proved (for k = 4) that this hypergraph Hm does not contain any double-cone. Therefore e(Hm) = O(m5/2). This led to his estimate. Lov´asz – starting with the same approach – excluded many more (k−1)-uniform hypergraphs. To make his argument easier to follow, we restrict ourselves to the case k = 4. Let M := {u1,...,um}. The neighbourhoods of ui’s deﬁned a

- 3-uniform hypergraph on [1,m], and Lov´asz attached to each ui a 0-1 vector of length m2 , where, for a neighbourhood N(ui) = {a,b,c}, Lov´asz put 1’s into

the places (a,b), (b,c), and (c,a), thus obtaining a 0-1 vector xi of length m2 , with three coordinates equal to 1’s (and all the others were equal to 0). The

- 4-criticality implied that these vectors were linearly independent.59 Therefore,


their number was at most m2 , i.e., we obtained that e(Hm) = |X| ≤ m2 . This gave the upper bound in Theorem 3.4.

So he used the Linear Algebra method, basically unknown those days, to get the sharp result in his extremal graph problem. That gave sharp result also in the Gallai problem.

Remark 3.6. For any monotone graph property P we may deﬁne the critical structures: Gn belonging to P but after the deletion of any edge (or, in other cases, any vertex) we get a graph outside of P. If we have a graph-parameter on graphs, then criticality mostly means increasing/decreasing this parameter by deleting any edge. Criticality was discussed for the stability number, chromatic numbers, diameter, and can be investigated for many other monotone properties. Among criticality problems colour-criticality seems to be one of the most interesting ones.

The fascinating area of colour critical graphs was started by G. Dirac, see e.g., Dirac [243, 245] and Erdo˝s [286]. There are several results on it in the Lov´asz book [589]. We skip here the topic of colour-critical hypergraphs, listing

![image 94](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile94.png>)

- 58An r-cone is a 3-uniform hypergraph obtained from a cycle x1, . . . , xk by adding r new vertices y1, . . . , yr and all the triples yjxixi+1 (where xk+1 = x1).
- 59In graph-theoretical language, Lova´sz excluded all the 3-graphs for which the Sperner Lemma holds: for which each pair was contained by an even number of triples.


just a few fascinating results on them: e.g., Abbott and Liu [2] and results of Krivelevich [556]. Deuber, Kostochka, Sachs [238], Ro¨dl and Siggers [703] and Anstee, Fleming, F¨uredi and Sali [50, 384]. Toft [806], and Simonovits [752], Ro¨dl and Tuza [706], Sachs and Stiebitz [711, 712, 713] Stiebitz, [782] Kostochka and Stiebitz [552], Stiebitz, Tuza, and Voigt [783].

See also the survey of Sachs and Stiebitz, [713]. We conclude this part with two open problems.

- Problem 3.7 (Erd˝os). Is it true that if (Gn) is a sequence of 4-critical graphs, then dmin(Gn) = o(n)?

Simonovits [752] and Toft [806] constructed 4-colour-critical graph sequences (Gn) with dmin(Gn) > c

3

√n.

![image 95](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile95.png>)

- Problem 3.8 (Linial). How many triples can a 3-uniform Hn have without containing a triangulation of the torus.60


- Remark 3.9. In some sense this geometric/linear algebraic approach helped Lov´asz to solve the famous Shannon conjecture on the capacity of C5, in [588].
- 4. Methods: Randomness and the Semi-random method


Of course, the title of this chapter may seem too pretentious. We shall skip several important methods and related results here, or just touch on them, primarily since they are well described in several other places, and partly since the bounded length of this survey does not allow us to go into details.

Thus we shall skip most of the results directly connected to random graphs or random graph constructions, while we shall touch on the pseudo-random graphs. For random methods, the readers are referred to the books of Alon and Spencer [48], Bollob´s [121], or that of Janson,  Luczak, and Ruci´nski [476], the survey of Molloy [614], or the book of Molloy and Reed [615].

Here of course most of these sources are well known, like e.g., the books [48] or [476]; we mention only Molloy’s excellent chapter [614], which is a survey on this topic, and perhaps got less attention than it deserves. It contains many important details and explanations, and perhaps would ﬁt the best to our topic, with the exception that it concentrates more on colouring and we concentrate more on independent sets in particular graphs.61

Listing the methods left out here, we should mention the extremely important works on Hypergraph Regularity Lemma, primarily that of Frankl and Ro¨dl [358] on 3-uniform hypergraphs, (This was among the ﬁrst ones). Of course, we should mention the whole school of Ro¨dl, among others, e.g., the papers of Ro¨dl,

![image 96](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile96.png>)

- 60Observe that this is motivated by [154], and that we formulated it in its simplest case, however, we (more precisely, Nati Linial) meant a whole family of problems. He spoke about them in his talk in the Lova´sz Conference, 2018.
- 61The same applies to the book of Molloy and Reed [615].


Nagle, Skokan, Schacht, and Kohayakawa, [686, 527]62 Ro¨dl and Schacht [700], Ro¨dl and Skokan [704, 705], and Kohayakawa, and many further results, and, on the other hand, related to this, several works of Tim Gowers [403, 404], Green and Tao [418] Terry Tao [797] ...

4.1. Various ways to use randomness in Extremal Graph Theory

Random graphs are used in the area discussed here in several diﬀerent ways.

- (a) There are many cases where constructions seem unavailable but random graphs may be used to replace them. We have mentioned the Erdo˝s Magic [261]. Another similar direct approach of Erdo˝s and R´enyi [306] was that

ex(n,L) ≥ cLn2−v(L)/e(L). (4.1)

- (b) In other cases we use modiﬁed random graphs: (4.1) is useless for cycles, but the modiﬁed random graph (in the simplest case the First Moment Method) worked in the papers of Erdo˝s [263] and [264], and in many similar cases. We mention here the Erdo˝s-Spencer book [320], and its follower, the very popular book of Alon and Spencer [48].
- (c) Since the very important paper of Erdo˝s and R´enyi [306] – on the evolution of Random Graphs, – the investigation of the changes/phase-transitions in the structure of Random Graphs, as the number of edges is slowly increasing – became a central topic of Combinatorics. Probably the ﬁrst profound book on this was that of Bollob´s [121]. Also we should deﬁnitely mention here the newer book of Janson,  Luczak and Ruci´nski [476], and the Molloy-Reed book [615].
- (d) Extremal graph theory optimizes on a Universe, and this Universe may be the family of Random Graphs.63 Since a question of Erdo˝s was answered by Babai, Simonovits, and Spencer [56], (here Theorem 5.43) this also became a very interesting and popular topic. We shall return to this question in Section 5.7.
- (e) The Semi-random method was introduced by Ajtai, Koml´os, and Szemer´edi, for graphs in [10] (to be applied in Combinatorial Number Theory, to Sidon Sequences), and later Ro¨dl, in his famous solution of Erdo˝sHanani problem [296] about block designs developed the absolutely important method, now called Ro¨dl Nibble [683].


In this short part we describe the Semi-Random method and the Ro¨dl Nibble very superﬁcially. According to their importance we should provide here a longer

![image 97](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile97.png>)

62This is a PNAS “survey”, with an accompanying paper of Solymosi [769]. 63Again, this case diﬀers from the others: if we try to optimize some parameter on all nvertex graphs, or on the subgraphs if the d-dimensional cube,. . . , that problem is well deﬁned for individual graphs, while the assertions on the subgraphs of a random graphs make sense only in some asymptotic sense, the assertions always contain the expression “almost surely as n → ∞”.

description, but the Ro¨dl Nibble has an excellent description, a whole chapter, in the Alon-Spencer book [48], and it is more complicated and technical than that we could easily provide a suﬃciently detailed description of it. (Beside referring to the Ro¨dl Nibble, described in [48], we also mention the original Koml´osPintz-Szemer´edi paper [536], to see the origins, and also the Pippenger-Spencer paper [652], and the Jeﬀ Kahn paper [482] proving the asymptotic weakening of the very famous Erdo˝s-Faber-Lov´asz conjecture. (The Jeﬀ Kahn paper also contains a fairly detailed description of the method.) The more recent paper of Alon, Kim, and Spencer [37] is also related to the previous topic.

- 4.2. The semi-random method


The semi-random method was introduced for graphs by Ajtai, Koml´os, and Szemer´edi [10], in connection with the inﬁnite Sidon sequences. Later it was extended by Koml´os, Pintz, and Szemer´edi to 3-uniform hypergraphs in [536], to disprove a famous conjecture of Heilbronn, discussed in Subsections 4.7-4.9. The method was further extended by Ajtai, Koml´os, Pintz, Spencer, and Szemer´edi in [7] and by Duke, Lefmann, and Ro¨dl [248].

Here we are concerned with three topics, strongly connected to each other and to the estimates of the independence number of K3-free graphs, or analogous hypergraph results. The semi-random method had the form where the independence number of a graph or a hypergraph had to be estimated from below, under the condition that the graph had no short cycles. The topics are

- (a) Sidon’s problem on inﬁnite sequences. A Sidon sequence is a sequence of integers in which no two (distinct pairs) have the same sum. What is the maximum density of such a sequence?
- (b) Heilbronn problem for the “minimum areas” in geometric situations.
- (c) Ramsey problem R(3,k). This will be obtained as a byproduct, for free.


- 4.3. Independent sets in uncrowded graphs


- A graph, hypergraph H is called Uncrowded if it does not contain short cycles. For graphs we excluded triangles, for hypergraphs cycles of length 2, 3, or 4. In a hypergraph a cycle can be deﬁned in several ways. Here a k-cycle (k ≥ 2)64 is a sequence of k diﬀerent vertices: x1,...,xk−1,xk = x0, and a sequence of k diﬀerent edges: E1,...,Ek such that xi−1,xi ∈ Ei for i = 1,2 ...,k. The cycle above is called simple if Ei ∩ (∪j =iEj) = {xi−1,xi} for i = 1,2 ...,k. In a hypergraph H, a 2-cycle is a pair of two hyperedges intersecting in at least two vertices; a vertex set A ⊂ H is independent if it does not contain hyperedges. The maximum size of an independent set in H is denoted by α(H). There are several lower bounds concerning independent sets in k-uniform uncrowded hypergraphs, mostly having the following form:


“Hypergraphs having no short cycles have large independent sets.”

![image 98](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile98.png>)

64often called a Berge k-cycle: in Figure 14(b) the edges of a C6 are covered by 3-tuples.

For ordinary graphs the following theorem, connected to inﬁnite Sidon sequences, was the starting point.

- Theorem 4.1 (Ajtai, Koml´os, Szemer´edi (1980), [9, 10]). If in a triangle-free

graph Gn the average degree is t := 2e(G

n)

![image 99](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile99.png>)

n , then the independence number α(Gn) ≥

1 100 ·

![image 100](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile100.png>)

n t

![image 101](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile101.png>)

log t. (4.2)

Tur´an’s theorem, or the greedy algorithm would give only n/t and in the random graphs we have the extra log t factor. The meaning of this theorem is, perhaps, that excluding K3 forces a much larger independent set and a randomlike behaviour.

Ajtai, Erdo˝s, Koml´os, and Szemer´edi also proved

- Theorem 4.2 ([6]). If Gn is Kp-free then α(Gn) ≥ c′(n/t)lnA where A = (lnt)/p and c′ is an absolute constant.


See also Shearer [737, 738, 739, 740] and Denley [237].

Proof-Sketch

Originally Theorem 4.1 had two diﬀerent proofs. One of them was an induction on the number of vertices, [9], (and a similar, perhaps more elegant proof – also using induction on n – was given by Shearer for its sharpening, see [737]). The other proof, from [10] used an iterated random construction which later developed into the Ro¨dl Nibble. This approach turned out to be fairly important, so we “sketch” its main idea, suppressing most of the technical details, and following the description from p10 of [10].

- (a) Since Gn is triangle-free, α(Gn) > dmax(Gn) ≥ t. So we may assume that the degrees are smaller than 1001 · nt log t. Similarly, we may assume that

![image 102](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile102.png>)

![image 103](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile103.png>)

t ≥

√n log n, since otherwise t > 1001 logt tn, implying (4.2): F(t) = t−2 log t

![image 104](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile104.png>)

![image 105](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile105.png>)

![image 106](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile106.png>)

is monotone decreasing; for t = √n log n we have F(t) ≈ 21n. This proves the assertion.

![image 107](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile107.png>)

![image 108](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile108.png>)

- (b) We select a subset K ⊂ V (Gn) of 1101 (n/t) independent vertices.

![image 109](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile109.png>)

- (c) Next we consider a vertex-set M ⊆ V (Gn) − K of ≈ n/2 vertices not joined to K: we need a lemma about the existence of such an M.
- (d) Another lemma assures us that the crucial quantity n/t does not drop too much when we move from Gn to Gm = G[M]. (It drops only by a factor ϑ := 1 − 1t − c10 t/n > 1 − t1/3.)

![image 110](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile110.png>)

![image 111](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile111.png>)

- (e) If we are lucky, then we can iterate this step ≈ 12 log t times: we gain a

![image 112](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile112.png>)

- 1

![image 113](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile113.png>)

- 2 log t factor and get Theorem 4.1.


- (f) On the other hand, if we are “unlucky” and get stuck in the rth step, then


for the corresponding tr we have that it is too large: tr−1/3 > 1/ logt. But then we get in this last step alone enough independent vertices:

n 2r

nr tr + 1

> (log t)−3

![image 114](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile114.png>)

![image 115](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile115.png>)

n(log t)−3 √t

log t t

> n

>

.

![image 116](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile116.png>)

![image 117](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile117.png>)

![image 118](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile118.png>)

Summarizing: In the typical case we can choose small independent subsets in V (Gn) basically log t times to gain a log t factor. It is important that discarding these small vertex sets, we do not ruin the structure of the remaining part.

- 4.4. Uncrowded hypergraphs


Most probably, the earliest result on hypergraphs using the semi-random method was the following one.

- Theorem 4.3 (Komlo´s, Pintz, and Szemer´edi [536], Lemma 1). There exists a threshold t0 and a constant c > 0 such that if H(3)n is a 3-uniform hypergraph on n vertices, with average degree t(3)(H(3)n ), and not containing simple cycles of length at most 4, then for t := t(3)(H(3)n ) > t0, t = O(n1/10), we have


![image 119](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile119.png>)

n t

α(H(3)n ) > c

![image 120](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile120.png>)

![image 121](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile121.png>)

log t.

The problems we discuss here were reduced to ﬁnding lower bounds on the independence number α(H) of a graph or hypergraph H under the assumption that H has no short cycles.65 The above theorem and its versions were enough for the early applications, in 1980’s, however, as it turned out in [248], only hypergraph cycles of length 2 had to be excluded: the following much newer generalization can be very useful in some new applications.

Theorem 4.4 (Duke, Lefmann, and Ro¨dl [248], Theorem 2). Let H be a kuniform hypergraph on n vertices. Let ∆ be the maximum degree of H. Assume that ∆ ≤ tk−1 and t > t0. If H doesn’t contain 2-cycles (two hyperedges with at least two common vertices), then

α(H) = Ω

n t

1

(log t)

k−1 .

![image 122](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile122.png>)

![image 123](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile123.png>)

Theorem 4.4 for k = 3 implies Theorem 4.3. One advantage of it is that in our applications we may have many simple cycles of length 3 and 4, but

- Theorem 4.4 still can be applied.


— · —

There are many results in this ﬁeld. We mention here only (i) Duke, Lefmann, and Ro¨dl [248] on Uncrowded Hypergraphs, (ii) C. Bertram-Kretzberg, T. Hofmeister and H. Lefmann [106, 107], some generalizations and results on the algorithmic aspects of the Heilbronn Problem: ﬁnding eﬃciently the large independent set in an uncrowded hypergraph, and (iii) Lefmann and Schmitt [573] and Lefmann [571], on the higher dimensional Heilbronn problem.

In [10] it is remarked that it is enough to assume that the number of triangles is small, instead of assuming that there are no K3’s at all. Shearer [737, 738] improved the constant in Theorem 4.1 in an ingenious way:

![image 124](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile124.png>)

65Actually, in[536] one needs to exclude only cycles of length 2,3, and 4, where a cycle of length 2 is a pair of hyperedges intersecting in at least two vertices. Even this is improved in the next theorem.

- Theorem 4.5 (Shearer [737]). Let f(t) = tlog(t−t−1)t2+1. Then for any triangle-free Gn, with average degree t,

![image 125](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile125.png>)

α(Gn) ≥ f(t) · n. (4.3)

This improves (4.2), and (in some sense) this is sharp. Related extensions were found by T. Denley [237], and by Shearer in cases when we assume that the odd girth of the graph is large [739], and also when we wish to use ﬁner information on the degree distribution. Kostochka, Mubayi, and Verstra¨ete [549] proved some hypergraph versions of this theorem, giving lower bounds on the stability number under the condition that certain cycles are excluded.

4.5. Ramsey estimates

Observe that – as a byproduct, – Theorem 4.1 immediately yields that

- Theorem 4.6 (Ajtai, Koml´os, Szemer´edi, on Ramsey theorem [9]). There exists a constant c > 0 such that

R(3,m) ≤

m2 c log m

![image 126](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile126.png>)

. (4.4)

Proof. Indeed, if n > m

2

![image 127](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile127.png>)

clogm, and K3  ⊆ Gn, then either Gn has a vertex x of degree δG(x) ≥ m, yielding an independent m-set NG(x), or by Theorem 4.1,

α(Gn) > c

m2 c log m

![image 128](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile128.png>)

![image 129](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile129.png>)

m

log m = m

proving Theorem 4.6.

Theorem 4.6 improves Erdo˝s’ old result [263], by a log m factor.66 For many years it was open if (4.4) is just an improvement of the Erdo˝s result or it is a breakthrough. Jeong Han Kim [515] proved much later, (using among others the Ro¨dl Nibble) that this bound is sharp.

- Theorem 4.7 (J.H. Kim, Ramsey (1995), [515]). 67


m2 log m

R(3,m) ≥ c˜

. (4.5)

![image 130](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile130.png>)

So the r(3,m)-problem is one of the very few nontrivial inﬁnite cases on Ramsey numbers where the order of magnitude is determined. Bohman and Keevash [115] and Fiz Pontiveros, Griﬃths, and Morris [345] independently proved that

2

R(3,k) ≥ (14 + o(1)) k

logk. Recently Shearer’s estimate was “strengthened” as follows.

![image 131](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile131.png>)

![image 132](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile132.png>)

![image 133](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile133.png>)

66Of course, Shearer’s improvement yields an improvement of c in (4.4). 67Actually, the proof works with c˜ = 1621 − o(1).

![image 134](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile134.png>)

- Theorem 4.8 (Davies, Jenssen, Perkins, and Roberts [228]). If Gn is a trianglefree graph with maximum degree t, and I(Gn) is the family of independent sets


in Gn, then

log t t

1 |I(Gn)|

|I| ≥ (1 + o(1))

n.

![image 135](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile135.png>)

![image 136](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile136.png>)

I∈I(Gn)

This is a strengthening in the sense that here the average size is large, but it is a weakening: it uses the maximum degree, instead of the average degree. For further details see, e.g., the introduction of [228].

- Remark 4.9. The above questions are connected to another important question: under some condition, what can be said about the number of independent sets in a graph or a hypergraph? Without going into details, we remark that these questions are connected to the container method, (for references see the Introduction).
- Remark 4.10. Further related results can be found, e.g., in papers of Cooper and Mubayi, and Dutta [207, 208, 206] which count the number of independent sets in triangle-free graphs and hypergraphs.


- 4.6. Inﬁnite Sidon sequences


The ﬁnite Sidon sequences are well understood, the maximum size of a Sidon subset of [1,n] is around √n, [324, 178], however, the inﬁnite Sidon sequences seem much more involved. The greedy algorithm provides an inﬁnite Sidon sequence (an) with an > cn1/3. This was slightly improved by using Theorem 4.1, but only by

![image 137](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile137.png>)

√log n:

![image 138](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile138.png>)

3

- Theorem 4.11 (Ajtai, Koml´os, and Szemer´edi (1981), [10]). There exists an inﬁnite Sidon sequence B for which, if B(n) denotes the number of elements of it in [1,n], then

B(n) ≥ c(n log n)1/3.

As it is remarked in [10], Erdo˝s conjectured that B(n) > n(1/2)−ε is possible. As to Sidon sets, later Theorem 4.11 was improved “dramatically”:

- Theorem 4.12 (Ruzsa (1998), [709]). There exists an inﬁnite Sidon sequence

B for which, if B(n) denotes the number of elements in [1,n], then B(n) ≥ n

√2−1+o(1).

![image 139](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile139.png>)

So the importance of this Ajtai-Komlo´s-Szemer´edi result [10] was that this was the beginning of the Semi-Random method. The following generalization was proved by Cilleruelo [189]. Call a sequence A = {ai}∞i=1 h-Sidon if all the sums ai

1

+ ··· + ai

h

are distinct for ai

1 ≤ ··· ≤ ai

h

.

- Theorem 4.13 (Cilleruelo, (2014), [189]). For any h ≥ 2 there exists an inﬁnite h-Sidon sequence A with


√

![image 140](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile140.png>)

(h−1)2+1−(h−1)+o(1),

A(n) = n

where A(n) counts the number of elements of A not exceeding n.

For h = 2 Cilleruelo provides an explicit construction. We remark also that, by a “random construction” of Erdo˝s and R´enyi [305], for any δ > 0, there exits an inﬁnite sequence Q := (a1,...,an,...) for which the number of solutions of ai + aj = h is bounded, for all h, and ak = O(k2+δ).

- 4.7. The Heilbronn problem, old results

Problem 4.14 (Heilbronn’s problem on the area of small triangles). Consider n points in the unit square (or in the unit disk) no three of which are collinear What is the maximum of the minimum area of triangles, deﬁned by these points where the maximum is taken for all point-sets?68.

This maximum of the minimum will be denoted by ∆n. Erdo˝s gave a simple construction where this minimum area was at least 2n12 : for a prime p ≈ n, consider all the points (1p(i,f(i)), where f(i) = i2 (mod p). So

![image 141](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile141.png>)

![image 142](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile142.png>)

- 1

![image 143](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile143.png>)

- 2n2


< ∆n ≤

1 n − 1

![image 144](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile144.png>)

.

Heilbronn conjectured that ∆ = O(n12 ). This was disproved by

![image 145](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile145.png>)

Theorem 4.15 (Komlo´s, Pintz, and Szemer´edi (1981), [535]). ∆n = Ω(logn2n): For some constant c > 0, for inﬁnitely many n, there exist n points in the unit

![image 146](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile146.png>)

square for which the minimum area is at least clogn2n. The proof of Theorem 4.15 is based on Theorem 4.3.

![image 147](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile147.png>)

- 4.8. Generalizations of Heilbronn’s problem, new results


P´eter Hajnal and Szemer´edi [448] used the Duke-Lefmann-R¨odl lower bound (Theorem 4.4) to prove two new geometrical results. The ﬁrst one [448] is closely related to Heilbronn’s triangle problem, discussed in [677, 733, 679, 681, 682, 535].

Consider an n-element point set P ⊂ E2. Instead of triangles we can take k-tuples from P and consider the area of the convex hull of the k chosen points. Denote the minimum area by Hk(P), its maximum for the n-element sets P by Hk(n). So ∆n = H3(n). The best lower bound on H3(n) from [536], and some trivial observations are summarized in the next line: there exists a constant c > 0 such that

√log n n2 ≤ ∆n = H3(n) ≤ H4(n) ≤ H5(n) ≤ ... = O

![image 148](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile148.png>)

1 n

c

.

![image 149](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile149.png>)

![image 150](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile150.png>)

We mention two major open problems:

![image 151](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile151.png>)

68If three of them are collinear that provides 0.

- Problem 4.16. Is it true that for any ε > 0, H3(n) = O(1/n2−ε)? Is it true that H4(n) = o(1/n)?


One is also interested in ﬁnding good lower bounds on H4(n). Schmidt [733] proved that H4(n) = Ω(n−3/2). The proof is a construction of a point set P by a simple greedy algorithm. In [106], Bertram-Kretzberg, Hofmeister and Lefmann provided a new proof, and extensions of this result. They also asked whether Schmidt’s bound can be improved by a logarithmic factor. Using the semi-random method, P´eter Hajnal and Szemer´edi improved Schmidt’s bound and settled the problem of [106].

- Theorem 4.17 (P. Hajnal and E. Szemer´edi [448]). For some appropriate constant c > 0, for any n > 3, there exist n points in the unit square for which the convex hull of any 4 points has area at least cn−3/2(log n)1/2.

- 4.9. The Heilbronn problem, an upper bound The ﬁrst upper bound was Roth’s fundamental result that ∆n ≪ n√log1log n.69 Schmidt [733] improved this to ∆n ≪ n√log1 n. Roth returned to the problem and improved the earlier results to ∆n ≪ 1/n1.117. Not only his bound was much better, his method was also groundbreaking. He combined methods from analysis, geometry, and functional analysis. On these results see the survey of Roth [682]. Roth’s result was improved by Pintz, Koml´os, and Szemer´edi:

![image 152](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile152.png>)

![image 153](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile153.png>)

![image 154](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile154.png>)

![image 155](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile155.png>)

Theorem 4.18 (Pintz, Koml´os, Szemer´edi [535]). ∆n ≪ ec

√lognn−8/7.

![image 156](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile156.png>)

- 4.10. The Gowers problem




P. Hajnal and E. Szemer´edi considered the following related but “projective” question:70

Problem 4.19 (Gowers [407]). Given a planar point set P, what is the minimum size of P that guarantees that one can ﬁnd n collinear points (points on a line) or n independent points (no three on a line) in P?

Gowers noted that in the grid at least Ω(n2) points are needed, and if we have 2n3 points without n points on a line, then a simple greedy algorithm ﬁnds n independent points. Payne and Wood [643] improved the upper bound O(n3) to O(n2 log n). They considered an arbitrary point set with much fewer than n3 points, and without n points on a line, but they replaced the greedy algorithm by a Spencer lemma, based on a simple probabilistic sparsiﬁcation.71

P´eter Hajnal and Szemer´edi improved the Payne-Wood upper bounds by improving the methods. They also started with a random sparsiﬁcation, but

![image 157](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile157.png>)

69Here f ≪ g is the same as f ≤ cg, for some absolute constant c > 0.

- 70Actually, Hajnal and Szemer´edi found this problem on Gowers’ homepage, but, as it

turned out, from [643], originally the problem was asked by Paul Erd˝s, [285].

- 71Actually, above we spoke about the “diagonal case” but [643] covers some oﬀ-diagonal


cases too.

after some additional preparation (getting rid of 2-cycles) they could use the semi-random method (see [248]) to ﬁnd a large independent set.

Theorem 4.20 (P. Hajnal and E. Szemer´edi [448]). There exists a constant C > 0 such that in any planar point set P of size C · n

2 log n

loglogn, there are n points that are collinear or independent.

![image 158](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile158.png>)

- 4.11. Pippenger-Spencer theorem

In the theory developing around the semi-random methods, one should mention the papers of Ro¨dl [683], and of Frankl and Ro¨dl [357], ...

One important step was the Pippenger-Spencer result [652], asserting that if the degrees in a k-uniform hypergraph are large and the codegrees are relatively small, then the hypergraph has an almost-1-factor.

Definition 4.21. A matching of a hypergraph H is a collection of pairwise disjoint hyperedges. The chromatic index χ′(H) of H is the least number of matchings whose union covers the edge set of H. The codegree δℓ(X) is the number of hyperedges containing the ℓ-tuple X ⊆ V (H), and δℓ(H) is the minimum of this, taken over all the ℓ-tuples of vertices in H.

We formulate the theorem, in a slightly simpliﬁed form.

Theorem 4.22 (Pippenger and Spencer [652]). For every k ≥ 2 and δ > 0 there exists a δ′ > 0 and an n0 such that if Hn is a k-uniform hypergraph with n > n0 vertices, and

dmin(Hn) > (1 − δ)dmax(Hn), and the codegrees are small:

δ2(Hn) < δ′dmin(Hn) then the chromatic index

χ′(Hn) ≤ (1 + δ)dmax(Hn).

The meaning of the conclusion is that the set of hyperedges can be partitioned into packings (or matchings), almost all of which are almost perfect. Also the edges can be partitioned into coverings, almost all of which are almost perfect. This theorem strengthens and generalizes a result of Frankl and Ro¨dl [357].

- 4.12. Erdo˝s-Faber-Lov´asz conjecture


We close this part with the beautiful result of Jeﬀ Kahn on the famous Erdo˝sFaber-Lov´asz conjecture. Faber writes in [326]:72

![image 159](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile159.png>)

72In citations we use our numbers, not the original ones.

In 1972, Paul Erd˝s, L´aszl´o Lova´sz and I got together at a tea party in my apartment in Boulder, Colorado. This was a continuation of the discussions we had had a few weeks before in Columbus, Ohio, at a conference on hypergraphs. We talked about various conjectures for linear hypergraphs analogous to Vizing’s theorem for graphs (see [327]). Finding tight bounds in general seemed diﬃcult so we created an elementary conjecture that we thought would be easy to prove. We called this the n sets problem: given n sets, no two of which meet more than once and each with n elements, color the elements with n colors so that each set contains all the colors. In fact, we agreed to meet the next day to write down the solution. Thirty-eight years later, this problem is still unsolved in general. (See [675] for a survey of what is known.)

The original conjecture says:

- Conjecture 4.23. If Gn is the union of k complete graphs Kk, any two of which has at most one common vertex, then χ(Gn) ≤ k.


As we stated, originally the conjecture was formulated using Linear Hypergraphs.73 A weakened asymptotic form of this was proved by Jeﬀ Kahn:

- Theorem 4.24 (Jeﬀ Kahn (1991), [482]). If A1,...,Ak ⊆ [n] are nearly disjoint, in the sense that |Ai ∩ Aj| ≤ 1 for all pairs i = j, then χ′(H) ≤ (1 + o(1))n.


Jeﬀ Kahn gave an elegant proof of this assertion, and also a clear description of the sketch of his proof, which is also a nice description of the Semi-Random method. The proof is based on a technical generalization of the PippengerSpencer Theorem [652].

- Remark 4.25. (a) Originally the Erdo˝s-Faber-Lov´asz conjecture had a slightly diﬀerent form, see above, or, e.g., Erdo˝s [279]. Jeﬀ Kahn refers to Hindman [464] who rephrased it in this form. Kahn also remarks that Koml´os suggested to prove an asymptotic weakening.

- (b) We also remark that the fractional form of this problem was solved by Kahn and Seymour [483].
- (c) Vance Faber proved [326] that if there are some counter-examples to the Erdo˝s-Faber-Lov´asz conjecture, they should be in some sense in the “middle range”, according to their densities.


- Remark 4.26 (On Keevash’ existence-proof of Block designs). One of the recent results that is considered a very important breakthrough is that of Peter Keevash [500, 501], according to which, if we ﬁx some parameters for some block-designs, and the corresponding trivial divisibility conditions are also satisﬁed, then the corresponding block designs do exist, assumed that the set of elements is suﬃciently large. Important but simpler results in the ﬁeld were obtained by Richard Wilson [814, 815, 816, 817], Vojta Ro¨dl [683], using – among others – the methods described above, above all, the Ro¨dl Nibble. The excellent paper of Gil Kalai [484] explains this area: what one tries to prove and how the semi-random methods are used. As a very important contribution, approach,


![image 160](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile160.png>)

73Perhaps the expression “linear hypergraph” was unknown those days.

see also the papers of Glock, K¨uhn, Lo, and Osthus [396, 397]. We do not go into details but again, refer the interested readers to the paper of Kalai written for the general audience, or, at least, for most of the combinatorists.

#### 5. Methods: Regularity Lemma for graphs

As we have already stated, Regularity Lemma is applicable in many areas of Discrete Mathematics. A weaker, “bipartite” version was used in the proof of Szemer´edi Theorem [790] according to which rk(n) = o(n). Also weaker versions were used in the ﬁrst applications in Graph Theory [710, 789]. The ﬁrst case when its standard form (Theorem 5.3) was needed was the Chv´atal-Szemer´edi theorem [188] on the parametrized form of the Erdo˝s-Stone theorem74. The Regularity Lemma is so successful, perhaps because of the following.

To embed a graph H into G is much easier if G is a random graph than if it is an arbitrary graph. The Regularity Lemma asserts that every graph G can be approximated by a “generalized random graph”, more precisely, by a “generalized quasi-random graph”. But then we may embed H into an almost random graph which is much easier. (Also, many other things are easier for Random Graphs.)

Lov´asz and Szegedy [595] wrote a beautiful paper on the Regularity Lemma, where they wrote75:

“Roughly speaking, the Szemer´edi Regularity Lemma says that the node set of every (large) graph can be partitioned into a small number of parts so that the subgraphs between the parts are random-like. There are several ways to make this precise, some equivalent to the original version, some not....”

To formulate the Regularity Lemma, we deﬁne (i) the ε-regular pairs of vertex-sets in a graph, (ii) the generalized random graphs, and (iii) the generalized quasi-random graphs.

Given a graph G, with the disjoint vertex sets X,Y ⊆ V (G), the edge-density between X and Y is

e(X,Y ) |X||Y |

.

d(X,Y ) :=

![image 161](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile161.png>)

Regular pairs are highly uniform bipartite graphs, namely ones in which the density of any “large” induced subgraph is about the same as the overall density of the whole graph.

Definition 5.1 (Regular pairs). Let ε > 0. Given a graph G and two disjoint vertex sets A ⊆ V (G), B ⊆ V (G), we say that the pair (A,B) is ε-regular if for every X ⊆ A and Y ⊆ B satisfying

|X| > ε|A| and |Y | > ε|B|

![image 162](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile162.png>)

- 74The question was that if e(Gn) = e(Tn,p) + εn2, how large Kp+1(m, . . . , m) can be guaranteed in Gn? This maximum m = m(p, ε) had a very weak estimate in [321]. This was improved to c(p, ε)log n by Bollob´as and Erd˝s [124], which was improved by Bollob´as, Erd˝s, and Simonovits [127]. Chva´tal and Szemer´edi needed the Regularity Lemma to get the “ﬁnal” result, sharp up to a multiplicative absolute constant.
- 75This was formulated by many researchers.


we have

|d(X,Y ) − d(A,B)| < ε. 76 (5.1)

We can also describe the Regularity Lemma as a statement asserting that any graph Gn can be approximated well by generalized random graphs. However, ﬁrst we have to deﬁne the generalized Erdo˝s-R´enyi random graph, then the generalized quasi-random graph sequences.

Definition 5.2 (Generalized Random Graphs). Given a matrix of probabilities, A := (pij)r×r and integers n1,...,nr. We choose the subsets U1,...,Ur with |Ui| = ni and join x ∈ Ui to y ∈ Uj with probability pij, independently.

The generalized quasi-random graphs are obtained when we also ﬁx an ε > 0 and instead of joining Ui to Uj using random independent edges, we join

- them with ε-regular bipartite graphs of the given density pij. Regularity Lemma asserts that the graphs can be approximated by general-


ized quasi-random graphs well.

- Theorem 5.3 (Szemer´edi, 1978 [791]). For every ε > 0 and M0 there are two constants M(ε,M0) and N(ε,M0) with the following property: for every graph Gn with n ≥ N(ε,M0) vertices there is a partition of the vertex set into ν classes


V = V1 ∪ V2 ∪ ... ∪ Vν such that

- • M0 ≤ ν ≤ M(ε,M0),
- • ||Vi| − |Vj|| ≤ 1, (1 ≤ i < j ≤ ν)
- • all but at most εν2 of the pairs (Vi,Vj) are ε-regular.


The lower bound on the number of classes is needed mostly to make the number of edges within the clusters small. If e.g. M0 > 1/ε, then e(Vi) <

- 1

![image 163](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile163.png>)

- 2εn2. So mostly we can choose M0 = 1/ε. We do not really need that ||Vi| − |Vj|| ≤ 1, however, we do need that the Vi’s are not too large. In the applications we very often use the Reduced graph or Cluster graph Hν deﬁned as follows:77


Definition 5.4 (Cluster Graph Hν = Hν(Gn)). Given a graph Gn, and two constants ε,τ > 0, the corresponding Cluster Graphs are obtained as follows. We apply the Regularity Lemma with ε, obtaining the partition V1,...,Vν. The vertices of Hν are the vertex-sets Vi (called Clusters) and we connect the Cluster Vi to Vj if (Vi,Vj) is ε-regular in Gn and d(Vi,Vj) > τ.

Remark 5.5. Mostly we use the cluster graph as follows: (i) We set out with a graph sequence (Gn), satisfying some conditions P, (ii) take the cluster graphs Hν, (iii) derive that (Hν) must have some properties P∗ (because of the combinatorial conditions on Gn), (iv) therefore we can apply some “classical” graph

![image 164](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile164.png>)

76In random graphs this holds for suﬃciently large disjoint vertex sets. 77Perhaps the name “Reduced Graph” comes from Simonovits, the “Cluster Graph” from

Koml´os, and the theorem itself was originally called “Uniformity Lemma”: the name “Regularity Lemma” became popular only later.

theorem to Hν, (v) this helps to describe Hν78 and (vi) having this information on Hν helps us to prove what we wanted.

...Or, in case (v-vi), instead of, say, estimating e(Gn), we embed some given graph Uµ into Hν, and using this, we embed a (much larger) Wm into Gn.

Remark 5.6. Given a graph sequence (Gn), it may happen that we have very diﬀerent regular partitions, e.g., in one of them the densities are around 0 and

1, in the other they are around 12.

![image 165](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile165.png>)

The natural question if (ε,τ) and Gn determine Hν is considered in the paper of Alon, Shapira, and Stav [46]. The answer is “No, but under some conditions YES”. However, here the reader should be cautions, we have not deﬁned when do we consider two regular partitions near to each other.

So the cluster graph is not determined by these parameters, (neither the ε-regular partition), and τ is much larger than ε, however, in the applications τ → 0 as ε → 0. (If e.g. we try to embed a relatively small graph (?) with bounded degree ∆, then τ ≈ ε1/(2∆) is mostly enough for our proofs, see also, e.g., G.N. Sa´rk¨ozy, [724].).

There are many surveys on Regularity Lemmas and its applications, e.g., Koml´os and Simonovits [546], Koml´os, Shokoufandeh, Simonovits, and Szemer´edi [545]; the survey of Koml´os [533] (formally on the Blow-up Lemma) is also very informative, and we also recommend a more recent survey of Szemer´edi [794].

There are several results on sparse graphs, see e.g. surveys of Kohayakawa and Ro¨dl [528] or of Gerke and Steger on the Sparse Regularity Lemma [392].

There are several works on some other aspects of the Regularity Lemma (or Regularity Lemmas), e.g., whether one needs exceptional classes, or how many clusters are needed (see e.g. Gowers [401]), or how can it be viewed from other points of views, e.g., Tao [797], however, we skip most of them.

Regularity Lemma and Parameters. The Regularity Lemma is very inefﬁcient in the sense that it works only for very-very large graphs.

There are three natural questions concerning this: (a) do we need the exceptional cluster-pairs, and (b) How large the threshold n0(M0,ε) must be, (c) how many clusters are needed. The answer to the ﬁrst question was given by the “half-graph” where one must use exceptional pairs. It is not quite clear how many exceptional pairs are needed in general.

Several results are known of that if we ﬁx ε > 0 and M0, then we have to use many-many clusters. The ﬁrst such result was due to Gowers [401]. (See also Moshkovitz and Shapira, [621].) For sharper results we refer the reader to Fox, La´szl´ Miklo´s Lov´asz, and Yufei Zhao [350], ...

5.1. Ramsey problems, cycles

As to the Ramsey Theory, we shall not introduce the standard notation here. For an excellent source, see the book of Graham, Rothschild, and Spencer [410].

![image 166](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile166.png>)

78estimate e(Hν) or prove some structural property of Hν.

The Ramsey problems were extended to arbitrary graphs ﬁrst by Gerencs´er and Gy´arf´s [390]. Several results were proved in this area by Faudree and Schelp [333, 334, 335], (and some parallel to Faudree and Schelp, by Vera Rosta [676]) and more generally, by Erdo˝s, Faudree, Rousseau, and Schelp, and others. Bondy and Erdo˝s [135] formulated several important conjectures for the case when the excluded graphs are paths, or cycles. In case of cycles, it turned out that the parity of the length of cycles is also very important. Again, we shall mention only a few related results, and then mention a few papers: this area is too large to describe it here in more details.

We have to start with the remark that in most cases considered below the (conjectured) extremal structures come from some “matrix-graph-sequence”: n vertices of a Kn are partitioned into a few classes and then we colour E(Kn) so that the colours depend only on the classes of the endvertices. These structures are very simple and nice, not chaotic/randomlike at all, so the proofs are also similar to the proofs of some extremal problems. Often we have some stability of the Ramsey-extremal structures.

One of the many questions Bondy and Erdo˝s [135] asked was whether for an odd n ≥ 3, is it true that Rr(Cn,Cn,...,Cn) = 2r−1(n − 1) + 1? The construction suggesting/motivating this conjecture is recursive: for two colours we take two BLUE complete Kn−1 and join them completely by GREEN edges. If we have already constructions on r − 1 colours, take two such constructions, and a new colour, say, RED, and join the two constructions completely with this new colour. (Watch out, if we use diﬀerent sets of colours, there are other, similar but more complicated constructions, colour-connections between them. As r increases, the number of non-equivalent constructions increases. For r = 3 we have two similar, yet diﬀerent con-

U1 U2

U3 U4

U

U

1 2

U

U

3 4

Figure 6: CycleRamsey with three colours

structions.)

- Conjecture 5.7 (Bondy and Erdo˝s). Let n be odd. If we r-colour KN for N = 2r−1(n − 1) + 1, then we shall have a monochromatic Cn.


The following approximation of the Bondy-Erdo˝s conjecture, for three colours, was a breakthrough in this area.

- Theorem 5.8 ( Luczak (1999), [600]). If n is odd, then


R(Cn,Cn,Cn) = 4n + o(n).

The proof was highly non-trivial. Applying stability methods, the o(n) was eliminated:

- Theorem 5.9 (Kohayakawa, Simonovits, and Skokan [530]). If n is a suﬃciently


large odd integer, then79

R(Cn,Cn,Cn) = 4n − 3.

Recently Jenssen and Skokan proved the corresponding general conjecture, [479], for odd cycles, at least if n is large. They use both the Regularity Lemma and the Stability method, adding some non-linear optimization tools to the usual methods, too.

The situation with the paths and the even cycles is diﬀerent. We could say that the reason is that the above colouring contains many monochromatic even cycles. This is why for three colours the Ramsey number is half of the previous one. Figaj and  Luczak proved

Theorem 5.10 (Figaj,  Luczak [341]). If α1 ≥ α2,α3 > 0, then for mi := 2⌊αin⌋ (i = 1,2,3)

) = (2α1 + α2 + α3)n + o(n). Corollary 5.11. If m1 ≥ m2 ≥ m3 are even, then

,Cm

,Cm

R(Cm

3

2

1

- 1

![image 167](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile167.png>)

- 2


(m2 + m3) + o(m1).

) = m1 +

,Pm

,Pm

R(Pm

3

2

1

In a recent paper Figaj and  Luczak [342] determined the asymptotic value of R(Cℓ,Cm,Cn), when the parities are arbitrary and the asymptotic values of ℓ/n = α and m/n = β are given, as n → ∞. We mention here just the following theorem, that proves a conjecture of Faudree and Schelp.

- Theorem 5.12 (Gya´rf´s, Ruszink´, G.N. Sa´rk¨ozy, and Szemer´edi [432]). There exists an n0 such that if n > n0 is even then R(Pn,Pn,Pn) = 2n−2, if n is odd then R(Pn,Pn,Pn) = 2n − 1.

The results listed above use the Regularity Lemma, and one thinks they could be proved without it, too. The diﬀerence between paths and even cycles is not that large:

- Theorem 5.13 (Benevides and Skokan, (2009), [99]). If n is even, and suﬃciently large, then R(Cn,Cn,Cn) = 2n.


These proofs use (among others) the Coloured Regularity Lemma. Hence all the assertions not using o(..) are proved only for very large values of n. This area is again large and ramiﬁed. We shall return to some corresponding Ramsey hypergraph results in Section 9.1.

![image 168](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile168.png>)

79Watch out, mostly it does not matter, but here, in case of sharp Ramsey results one has to distinguish the lower and upper Ramsey numbers. The upper one is the smallest one for which there is no good colouring, here 4k−3. The lower Ramsey number is R(L1, . . . , Lr)−1.

- 5.2. Ramsey Theory, general case


Burr and Erdo˝s conjectured [164] that the 2-colour Ramsey number R(Hn,Hn) is linear in n for bounded degree graphs.80 First some weaker bound was found by J´ozsef Beck, but then the conjecture was proved by

Theorem 5.14 (Chv´atal-R¨odl-Szemer´edi-Trotter (1983), [187]). For any ∆ > 0 there exists a constant Γ = Γ(∆) such that for any Hn with dmax(Hn) < ∆, we have R(Hn,Hn) < Γn.

The proof was based on the Regularity Lemma, applied to a graph GN deﬁned by the RED edges of a RED-BLUE-coloured KN. Then Tur´an’s theorem and Ramsey’s theorem were applied to the Coloured Cluster Graph Hν. The RED-BLUE colouring of KN deﬁnes a RED-BLUE colouring of Hν: the clusteredge ViVj gets the colour which has the majority. Then the proof is completed by building up a RED copy of Hn in the RED-BLUE KN, if Hν contained a suﬃciently large RED complete subgraph. The next, stronger conjecture is still open.

Conjecture 5.15 (Burr-Erdo˝s). If condition dmax(Hn) < ∆ is replaced by the weaker condition that for any H∗ ⊂ Hn we have dmin(H∗) < ∆, then R(Hn,Hn) = O(n).

Remark 5.16. The actual bound of [187] on the multiplicative constant in Theorem 5.14 was fairly weak. This was improved in several steps, ﬁrst by N. Eaton [250], then by Graham, Ro¨dl, and Ruci´nski [411], and ﬁnally by Conlon [192], and Fox and Sudakov [352].

5.3. Ramsey-Tur´an theory

When Tur´an, around 1969 [809], started a series of applications of his graph theorem in other ﬁelds of Mathematics, in some sense it turned out that Tn,p is too regular, has too simple structure: from the point of view of applications perhaps it would be better to have a version of his theorem for graphs with less regular, more complicated structure, but providing better estimates.81 This led Vera So´s, in [772] to ask more general questions than the original Tur´an question, and that led her to the Tur´an-Ramsey theory. One of her questions was

Problem 5.17 (S´os (1969), [772]). Fix r sample graphs L1,...,Lr. What is the maximum of e(Gn) if the edges of Gn can be r-coloured so that the ith colour does not contain Li.

The answer was given by

![image 169](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile169.png>)

80Here by linear we mean O(n). 81Actually, Tura´n’s corresponding results, or the Erd˝s-So´s type Ramsey-Tura´n theorems were not used in “applications”, however the Ajtai-Koml´s-Szemer´edi type results are also in this category and, as we have seen in Sections 4.2-4.10, they were used in several beautiful and important results.

Theorem 5.18 (Burr, Erdo˝s and Lov´asz (1976), [167]). For a family {L1,...,Lr}

of ﬁxed graphs, let R be the smallest integer for which there exists an m such that if Tm,R is arbitrarily r-coloured, then for some i the ith colour contains an Li. Then

RT(n;L1,...,Lr) = ex(n,KR−1) + o(n2).

Actually, this easily follows from the Erdo˝s-Stone theorem. (Further, obviously, we can choose m = v(Li).) Later it turned out that the really interesting problem is to determine RT(n;L1,...,Lr−1,o(n)), which in the simplest case r = 2 means the following.82

Problem 5.19 (Erd˝os-S´os (1970), [319]). Consider a graph sequence (Gn). Estimate e(Gn) if L  ⊂ Gn, and the independence number, α(Gn) = o(n).

The case of odd complete graphs was solved by

- Theorem 5.20 (Erd˝os and So´s (1970), [319]). Let (Gn) be a graph sequence. If K2ℓ+1  ⊂ Gn and α(Gn) = o(n), then

e(Gn) ≤ 1 −

1 ℓ

![image 170](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile170.png>)

n 2

+ o(n2),

and this is sharp.

Here the sharpness, i.e. the lower bound is easy: let m = ⌊n/ℓ⌋ and embed into each class of a Tn,ℓ a graph Gm not containing K3, with α(Gm) = o(m). By the “probabilistic constructions” of Erdo˝s [264] we know the existence of such graphs.83 The obtained graph Sn provides the lower bound in Theorem 5.20: it does not contain K2ℓ+1 and α(Sn) = o(n).

The problem of estimating RT(n,K4,o(n)) turned out to be much more diﬃcult and this was among the ﬁrst ones solved (basically!) by the Regularity Lemma, where the upper bound was given by Szemer´edi [789] and the sharpness of this upper bound was proved by Bollob´s and Erdo˝s [126]. It turned out that

- Theorem 5.21 (Szemer´edi (1972), [789], Bollob´s and Erdo˝s (1976), [126]).


RT(n,K4,o(n)) =

1 8

+ o(1) n2.

![image 171](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile171.png>)

The proof of the upper bound used (a simpler (?) form of) the Regularity Lemma. The ﬁrst graph theoretical successes of the Regularity Lemma were on the f(n,6,3)-problem, see Theorem 5.26, and the Ramsey-Tur´an theory: Theorem 5.21, and its generalization by Erdo˝s, Hajnal, So´s, and Szemer´edi [295], see also [292], and [294] by Erdo˝s, Hajnal, Simonovits, So´s, and Szemer´edi. Since those days this area has gone through a very fast development, Simonovits and So´s have a longer survey on Ramsey-Tur´an problems [766]. However, even since

![image 172](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile172.png>)

82One has to be cautious with this notation, when we write o(n) instead of a function f(n). 83These are the graphs we considered in connection with R(n, 3) in Section 2.16. There are

many such graphs obtained by various, more involved constructions.

the publication of [766], many beautiful new results have been proved, e.g., by Mubayi and So´s [626], Schelp [732], Fox, Loh, Zhao [349], Sudakov [785], Balogh and Lenz [70] and [71], and many further ones.

In the proof of the upper bound of Theorem 5.21 one needed something more than what was used in the earlier arguments: Until this point in most applications of the Regularity Lemmas the densities were near to 0 or near to

1. Here the densities in the Regular Partitions turned out to be near 0 or 12. Fixing the appropriate ε and τ =

![image 173](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile173.png>)

√ε, one important step was that the Cluster Graph Hν was triangle-free: K3  ⊂ Hν, and another was that in the Regular Partition, d(Ui,Uj) ≤ 21 +o(1). This implies the upper bound in Theorem 5.21, namely

![image 174](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile174.png>)

4

![image 175](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile175.png>)

e(Gn) ≤ ex(ν,K3) ·

1 2

+ o(1)

![image 176](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile176.png>)

n ν

![image 177](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile177.png>)

2

+ negligible terms =

1 8

+ o(1) n2.

![image 178](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile178.png>)

As to the lower bound in Theorem 5.21, the Erdo˝s-Bollob´as construction used a high dimensional isoperimetric inequality, similar to a related construction of Erdo˝s and Rogers [309]. One remaining important open question is

- Problem 5.22 (Erd˝os). Is RT(n,K(2,2,2),o(n)) = o(n2) or not? Ro¨dl proved that


Theorem 5.23 (R¨odl [684]). There exist a graph sequence (Gn) with α(Gn) =

- o(n) and K4  ⊂ Gn, K(3,3,3)  ⊂ Gn for which e(Gn) ≥ 81n2 + o(n2).84

![image 179](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile179.png>)

Phase transition. It can happen that f(n) is a “small” function, much smaller than “just” o(n), say f(n) = o(√n), and then we see kind of a phase transition:

![image 180](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile180.png>)

- one can prove better estimates on RT(n,L,f(n)). In other words, sometimes when f(n) is replaced by a slightly smaller g(n), the Ramsey-Tur´an function noticeably drops. Such result can be found, e.g., in Sudakov [785], in Balogh, Hu, and Simonovits [69], or in Bennett and Dudek [100],...Bennett and Dudek also list several related results and papers. Some roots of this phenomenon go back to [295, 293].


We close this part with a two remarks on phase transition results. Perhaps the simplest approach is to investigate RT(L1,...,Lr,f(n)), when we know of f(n) only that f(n) = o(n), however, f(n)/n → 0 can be arbitrary slow. There are two directions from here:

- (a) when we know of f(n) that f(n)/n → 0 relatively fast, so fast that

lim n12RT(L1,...,Lr,f(n)) becomes smaller than for a slightly larger g(n).

![image 181](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile181.png>)

- (b) The other direction is when we investigate the δ-dependence of


liminf

1 n2

RT(L1,...,Lr,δn).

![image 182](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile182.png>)

There are some very new interesting results in both areas, we refer the reader to the above mentioned [785] and [69], and also to papers of L¨uders and

![image 183](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile183.png>)

84Actually, Ro¨dl proved a slightly stronger theorem, answering a question of Erd˝s, but the original one, Problem 5.22, is still open.

Reiher [605] and of Kim, Kim and Liu [516] settling several phase-transition problems earlier unsolved. They determined RT(n,K3,Ks,δn) for s = 3,4,5 and suﬃciently small δ, conﬁrming – among others – a conjecture of Erdo˝s and So´s from 1979, and settling some conjectures of Balogh, Hu, and Simonovits, according to which RT(n,K8,o(√n log n)) = n

2

4 + o(n2).

![image 184](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile184.png>)

![image 185](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile185.png>)

5.4. Ruzsa-Szemere´di theorem, Removal Lemma

We start with a slightly simpliﬁed version of a result of G. Dirac [244], a generalization of Tur´an’s theorem:

Theorem 5.24 (Dirac (1963), [244]). Let p ≥ 2, q ∈ [1,p] and n ≥ p + q be integers. If Gn is a graph with e(Gn) > e(Tn,p) edges, then Gn contains a subgraph of p + q vertices and p+2q − (q − 1) edges.

Some related results were also independently obtained by Erdo˝s, see [286], and also [267]. Erdo˝s asked the following problem. Problem 5.25 ([267]). Let Lk,ℓ be the family of graphs L with k vertices and ℓ edges. Determine (or estimate) f(n,k,ℓ) := ex(n,Lk,ℓ).

Several results were proved on this problem by Erdo˝s [267], Simonovits [751], Griggs, Simonovits, and Rubin G. Thomas [421], Simonovits [761] and others. Extending these types of results to 3-uniform hypergraphs in [154] and then to r-uniform hypergraphs in [155], W. G. Brown, P. Erdo˝s and V. T. So´s started a systematic investigation of fr(n,k,ℓ) deﬁned as the maximum number of hyperedges an r-uniform n-vertex hypergraph Hn(r) can have without containing some k-vertex subgraphs with at least ℓ hyperedges.

Below mostly we shall restrict ourselves to the case of 3-uniform hypergraphs, i.e. r = 3. Several subcases were solved in [154], but the problem of f(n,6,3), i.e. the case when no 6 vertices contain 3 triplets, turned out to be very diﬃcult. One can easily show that f(n,6,3) ≤ 61n2. Ruzsa and Szemer´edi proved that

![image 186](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile186.png>)

- Theorem 5.26 (Ruzsa-Szemer´edi (1978), [710]). cn · r3(n) < f(n,6,3) = o(n2). (5.2)

The crucial tool was a consequence of the Regularity Lemma:

- Theorem 5.27 (Ruzsa-Szemer´edi Triangle Removal Lemma). If (Gn) is a graph sequence with o(n3) triangles, then we can delete o(n2) edges from Gn to get a triangle-free graph.

Clearly, (5.2) implies Roth theorem that r3(n) = o(n). There is a more general form of Theorem 5.27, the so called Removal Lemma:

- Theorem 5.28 (Removal Lemma). If v(L) = h, then for every ε > 0 there is a δ > 0 for which, if a Gn contains at most δnh copies of L, then one can delete εn2 edges to destroy all the copies of L in Gn.


Remark 5.29 (Induced matchings). Let us call some edges of a graph Gn Strongly Independent, if there are no edges joining two of them. The Ruzsa-Szemer´edi theorem can be formulated also without using hypergraphs. Indeed, for each x ∈ V (H), the link of x, i.e. the pairs uv forming a hyperedge in H with x, form a so-called induced matching: not only its edges are independent but they are pairwise strongly independent.85 So the RuzsaSzemer´edi theorem has the following alternative form:

Theorem 5.30 (Ruzsa-Szemer´edi [710]). If E(Gn) can be covered by n induced matchings, then e(Gn) = o(n2).

For some further applications86 and results connected to Induced Matchings see also the papers of Alon, Moitra, and Sudakov [40], and also of Birk, Linial, and Meshulam [110]. Alon, Moitra, and Sudakov describe several constructions and their applications (in theoretical computer science) connected to the Ruzsa-Szemer´edi theorem, more precisely, to dense graphs that can be covered by a given number of induced matchings.

- Remark 5.31. Among the original questions of Brown, Erdo˝s, and So´s, the estimate of f(n,7,4) is still unsolved. For some special graphs connected to groups, Solymosi [771] has a solution. Actually, very recently Nenadov, Schreiber, and Sudakov [631] extended this result.
- Remark 5.32. (a) Though Theorem 5.28 was not explicitly formulated in [710], implicitly it was there. Later it was explicitly formulated, e.g., in the paper of Erdo˝s, Frankl, and Ro¨dl [288] and F¨uredi [371], [372], and soon it became a central research topic, partly because it is often applicable and partly because


– though for ordinary graphs the Removal Lemma easily follows from the Regularity Lemma, for hypergraphs everything is much more involved.

- (b) The Ruzsa-Szemer´edi theorem was extended by Erdo˝s, Frankl, and Ro¨dl

[288] to r-uniform hypergraphs. They proved that fr(n,3r − 3,3) = o(n2).

- (c) Actually, f(n,6,3) is a ﬁxed function of n, and – though [710] asserts


only that f(n,6,3) = o(n2), – it has some better asymptotics and they are very interesting and important, since these results have many applications. J. Fox gave a new, more eﬀective proof of the Removal Lemma [347], not using the Regularity Lemma, leading also to better estimates on f(n,6,3), according to which

n2 2log∗ n

f(n,6,3) <

. (5.3)

![image 187](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile187.png>)

(d) A more detailed description of this topic can be found in two surveys of Conlon and Fox [194, 195]. We skip all the details connected to “Tower” functions and “Wowzer” functions,87 (which show that the Regularity-Lemma

![image 188](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile188.png>)

85Here we assume that the mindegree is at least 3. 86Some applications of the Ruzsa-Szemer´edi theorem are given in Subsection 5.5. 87with the exception of the next theorem.

methods are very ineﬃcient). Conlon and Fox discuss the estimates connecting the various parameters, in details.

- (e) Some related results and generalizations were proved by G.N. S´ark¨ozy

- and Selkow [726, 727], and by Alon and Shapira [45]. The emphasis in [45] is on obtaining a new lower bound to generalize Theorem 5.26.88

(f) Ruzsa-Szemer´edi removal lemma was applied also by Balogh and Petˇr´ıˇckov´a [84], to give a sharp estimate on the number of maximal triangle-free graphs Gn.

We close this part with quoting a result of Jacob Fox. Let TF(t) be the “tower” of 2’s of height t: TF(1) = 2 and TF(t + 1) = TF(2TF(t)).

Theorem 5.33 (J. Fox [347]). Fix a sample graph Lh (on h vertices) and an ε > 0. Let δ := 1/TF(⌈5h4 log 1/ε⌉). Every Gn with at most δnh copies of Lh can be made Lh-free by removing at most εn2 edges.

- Remark 5.34. The surveys of Conlon and Fox, e.g., [195] also discuss the

connection of property testing if Gn contains an induced copy of H, and its connection to the “Induced Removal Lemma”.

The interested reader is recommended to read [347] or the survey of Conlon and Fox [195].

— · —

- Remark 5.35. (a) Mostly we skip the references to graph limits, however, here we should mention the Elek-Szegedy Ultra-product approach to graph limits, and within that to the Removal Lemma, see [252].

(b) T. Tao also has a variant of the Hypergraph removal lemma [798] which he uses to prove a Szemer´edi type theorem on the Gaussian primes [799].

- Remark 5.36 (Szemer´edi theorem and the Clique-union Lemma). V. Ro¨dl, as an invited speaker of the ICM 2014, in Seoul, spoke about the relations described above. Generalizing the above approach, Peter Frankl and he tried to

prove rk(n) = o(n), using this combinatorial approach. The reader is suggested to look up the movie about his lecture. (ICM 2014 Video Series, Aug 21)

Some generalizations. The Ruzsa-Szemer´edi theorem has two parts, and both have several important and interesting generalizations, yet, in this paper we mostly skip the results connected to the lower bounds. Several related results can be found in the papers of Erdo˝s, Frankl, and Ro¨dl [288], or e.g., in the paper of F¨uredi and Ruszink´ on excluding the grids [383], and also in G.N. Sa´rk¨ozy and Selkow [727], and Alon and Shapira [45].

- Remark 5.37. Solymosi tried to formulate a non-trivial Removal Lemma for bipartite excluded graphs, however Timmons and Verstra¨ete [805] provided inﬁnitely many “counterexamples”.






![image 189](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile189.png>)

88Actually, this assertion is somewhat more involved, see the introduction of [45].

5.5. Applications of Ruzsa-Szemere´di Theorem

As we have mentioned, one of the early successes of a simpler form of the Regularity Lemma was the answer to the question of Brown, Erdo˝s, and So´s, according to which f(n,6,3) = o(n2), (and the proof of the triangle removal lemma, implying this). Fox writes in [347]: “The graph removal lemma has many applications in graph theory, additive combinatorics, discrete geometry, and theoretical computer science.” Here we mention two graph theoretical applications, one of which is strongly connected to Turing Machines.

F¨uredi theorem on diameter critical graphs

Call a graph G diameter-d-Critical, if it has diameter d and deleting any edge the diameter becomes at least d+1 (or G gets disconnected). Such graphs are, e.g., Ck or Tn,p. Restrict ourselves to d = 2: consider diameter-critical graphs of diameter 2. As F¨uredi describes in [371], Plesn´ık observed [653] that for all known diameter-2-critical graphs Gn, e(Gn) ≤ ⌊n

2

4 ⌋. Independently,

![image 190](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile190.png>)

Simon and Murty conjectured [170] that Conjecture 5.38. If Gn is a diameter-2-critical graph, then e(Gn) ≤ ⌊n

2

4 ⌋.

![image 191](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile191.png>)

This seemed to be a beautiful but very diﬃcult conjecture. F¨uredi [371] proved it for large n, using the Ruzsa-Szemer´edi theorem: Theorem 5.39 (F¨uredi (1992), [371]). There exists an n0 such that if n > n0,

- then the Murty-Simon conjecture holds.


Remark 5.40. In the proof of Theorem 5.39 we get a very large n0. In some sense Theorem 5.39 settles the conjecture, at least for most of us. Yet a lot of work has been done to prove it for reasonable values of n, too. Plesn´ık

proved, instead of e(Gn) ≤ 14n2, that e(Gn) ≤ 38n2, Caccetta and Ha¨ggkvist [170] improved this to e(Gn) ≤ 0.27n2, and G. Fan [328] proved for n > 25 that e(Gn) ≤ 0.2532n2. 89

![image 192](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile192.png>)

![image 193](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile193.png>)

There are many related results proved and some conjectures on the d-diameter-

critical graphs, see e.g. a survey of Haynes, Henning, van der Merwe, and Yeo, [460], or Po-Shen Loh and Jie Ma [580]. This later one disproves a CaccettaHa¨ggkvist conjecture on the average edge-degree of diameter-critical graphs (and contains some further nice results as well).

Triangle Removal Lemma in Dual Anti-Ramsey problems

Burr, Erdo˝s, Graham and So´s started investigating the following “dual AntiRamsey” problem [166], (see also [165]):

Given a sample graph L, n, and E, what is the minimum number of colours t = χS(n, E, L) such that any graph Gn with E edges can be edge-coloured with

![image 194](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile194.png>)

89Watch out, some of these papers, e.g., [328] are from before Fu¨redi’s result, some others are from after it.

t colours so that all the copies L ⊂ Gn be Rainbow coloured (i.e. its edges be coloured without colour-repetition? 90

They observed that for L = P4 this question can be solved using f(n,6,3) =

- o(n2). Actually, their solution for L = P4 is reducing the problem to the problem
- of estimating f(n,6,3). For L = C5 (which seemed one of the most interesting cases), they proved:


- Theorem 4.1 of [166]. There exists an n0 such that if n > n0 and e = ⌊n

2

![image 195](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile195.png>)

4 ⌋+1, then

c1n ≤ χS(n,e,C5) ≤

n 2

![image 196](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile196.png>)

+ 3. (5.4)

Erdo˝s and Simonovits [318], using the Lov´asz-Simonovits Stability theorem, (see Subsection 2.15) proved that the upper bound (obtained from a simple construction) is sharp.

- Theorem 5.41 (Erd˝os and Simonovits). There exists a threshold n0 such that


2

if n > n0, and a graph Gn has E = ⌊n

4 ⌋ + 1 edges and we colour its edges so that every C5 is 5–coloured, then we have to use at least n2 + 3 colours.

![image 197](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile197.png>)

![image 198](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile198.png>)

To apply the Lov´asz-Simonovits Stability, they needed the result of [166] on P4. So, again, the removal lemma was one of the crucial tools. (The application of the Lov´asz-Simonovits Stability can be replaced here by a second application of the Removal Lemma and the Erdo˝s-Simonovits Stability, however that approach would be less elementary and eﬀective.) They also proved several further results, however, we skip them. Simonovits has also some further results in this area, e.g., on the problem of C5 when e(Gn) = ⌊n

2

4 ⌋ + k, and k is any ﬁxed number, or tending to ∞ very slowly, and also on the problem of C7. Another conjecture of Burr, Erdo˝s, Graham, and So´s was (almost completely) proved by G.N. Sa´rk¨ozy and Selkow [728].

![image 199](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile199.png>)

5.6. Hypergraph Removal Lemma?

There are several ways to approach the Removal Lemma and the Hypergraph Removal Lemma. Ro¨dl and Schacht [701] describe a hypergraph generalization of the Removal Lemma. In the nice introduction of [701] they also write

. . . the result of Alon and Shapira [44] is a generalization which extends all the previous results of this type where the triangle is replaced by a possibly inﬁnite family F of graphs and the containment is induced.. . .

We have promised to avoid some areas that are much more diﬃcult/technical than the others. Unfortunately, it is not easy to decide what is “technical”.

![image 200](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile200.png>)

90The corresponding extremal value will be denoted by χS(n, E,L). Here S stands for “strong” in χS. It is the strong chromatic number of the v(L)-uniform hypergraph whose hyperedges are the v(L)-sets of vertices of the copies of L ⊂ Gn.

Koml´os and Simonovits [546] tried to provide an easy introduction to the Regularity Lemma. If one knows enough non-discrete mathematics, e.g., compactness, metric spaces, then the Lov´asz-Szegedy paper [595] is an easy introduction

- to the area of connections of Regularity Lemma and other, related areas. The situation with hypergraphs is diﬀerent. That area seems inherently dif-

ﬁcult to “learn”. The paper of Ro¨dl, Nagle, Skokan, Schacht, and Kohayakawa [686] and the companion paper of Solymosi [769] helps a lot to bridge this difﬁculty. The diﬃculties come from two sources. The ﬁrst one is that there are useful and not so useful versions of the Hypergraph Regularity Lemma, and the useful ones are diﬃcult to formulate. Layers come in, e.g., for 3-uniform hypergraphs: beside considering the vertices and hyperedges, we have to consider some auxiliary graphs.

In [686] twelve theorems are formulated, the last two are the hypergraph regularity and the hypergraph counting lemmas. It is nice that the hypergraph removal lemma keeps its simple form.

- Theorem 5.42 (See Theorem 5 of [686]). For any ﬁxed integers ℓ ≥ k ≥ 2

and ε > 0, there exists a ξ = ξ(ℓ,k,ε) and an n0(ℓ,k,ε), such that if F(ℓk) is a k-uniform hypergraph on ℓ vertices and H(nk) in a k-uniform hypergraph of n vertices, with fewer than ξnℓ copies of F(ℓk), then it may be transformed into an Fℓ(k)-free hypergraph by deleting εnk hyperedges.

Solymosi remarked that the appropriate hypergraph removal lemma implies the higher dimensional version of the Szemer´edi theorem. We close this part by quoting Solymosi [769]:

“There is a test to decide whether a hypergraph regularity is useful or not. Does it imply the Removal Lemma? If the answer is yes, then it is a correct concept of regularity indeed. On the contrary, applications of the hypergraph regularity could go beyond the Removal Lemma. There are already examples for which the hypergraph regularity method, combined with ergodic theory, analysis, and number theory, are used eﬃciently to solve diﬃcult problems in mathematics.”

The hypergraph removal lemma was approached from several directions. Among others, Tao considered it in [798], Elek and B. Szegedy [251] approached it from the direction of Non-Standard Analysis, Ro¨dl and Schacht from their general hypergraph regularity theory.

5.7. The Universe of Random Graphs

The following result answers a question of Erdo˝s:

- Theorem 5.43 (Babai, Simonovits and Spencer (1990), [56]). There exists a


- p0 < 21 such that a random graph Rn,p with edge-probability p > p0 almost surely has the following property BL, for L = K3: all its triangle-free subgraphs with maximum number of edges are bipartite91.


![image 201](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile201.png>)

![image 202](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile202.png>)

91where “almost surely” means that its probability tends to 1 as n → ∞.

Actually, they proved much more general results. Consider the following assertion, depending on L and p.

(BL,p) All the L-free subgraphs Fn ⊂ Rn,p having maximum number of edges are χ(L)-chromatic, almost surely, if n > n0(L, p).

They proved (BL,p) for all cases when L has a critical edge 92 and p is nearly

- 1

![image 203](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile203.png>)

- 2. They also proved several related weaker results in the general case, when L was arbitrary, and p > 0. They could not extend their results to sparse graphs, primarily because that time the sparse Regularity Lemma did not exist. Soon it was “invented” by Kohayakawa.93 The results of Babai, Simonovits and Spencer were generalized, ﬁrst by Brightwell, Panagiotou and Steger [148], and then, in various ways, by others. So the ﬁrst breakthrough towards sparse graphs was


- Theorem 5.44 (Brightwell, Panagiotou and Steger (2012), [148]). There exists

a constant c > 0 for which choosing a random graph Rn,p where each edge is taken independently, with probability p = n−(1/2)+ε, the largest triangle-free subgraph Fn of Rn,p is bipartite, with probability tending to 1.

They remarked that the conclusion cannot hold when p = 101 log√nn, since these Rn,p contain, almost surely, such an induced C5 whose edges are not contained in triangles of this Rn,p. All the edges of Rn,p not covered by some K3 ⊂ Rn,p must belong to Fn. Therefore now C5 ⊂ Fn: Fn is not bipartite. The proof of [148], similarly to that of the original proof of Babai, Simonovits and Spencer, uses a stability argument, however, instead of the original Regularity Lemma it uses the Sparse Regularity Lemma. In some sense the “ﬁnal” result was found by DeMarco and Jeﬀ Kahn [235, 236]. They proved (among others) that

![image 204](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile204.png>)

![image 205](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile205.png>)

![image 206](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile206.png>)

- Theorem 5.45 (DeMarco and Kahn (2015), [236]). For each r there exists a


constant C = Cr > 0 for which choosing a random graph Rn,p where each edge is taken independently, with probability

2

2

p > Cn−

(r+1)(r−2) n, the largest Kr-free subgraph Tn of Rn,p is almost surely r − 1-partite.

(r+1) log

![image 207](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile207.png>)

![image 208](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile208.png>)

A hypergraph analog was proved by Balogh, Butterﬁeld, Hu, and Lenz [66]. (They again used the stability approach.)

5.8. Embedding large trees

There are many results where one ﬁxes a sample graph L and tries to embed it into a Random Graph Rn,p. (See e.g. Erdo˝s-R´enyi [306].) Here we try to embed a ﬁxed tree Tm of m ≈ (1 − α)n vertices into a (random) graph Rn. However, we use a slightly diﬀerent language.

![image 209](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile209.png>)

92see Meta-Theorem 2.19. 93Ro¨dl also knew it, but it seems that he had not published it.

A relatively new notion of resilience was introduced by Sudakov and Vu [786]. Fix a graph property P. The resilience of Gn is its “edit” distance94 to graphs not having property P.95 Balogh, Csaba, and Samotij [68] proved

- Theorem 5.46. Let α and γ be (small) positive constants and assume that ∆ ≥ 2. There exists a constant C > 0 (depending on α,γ, and ∆) such that for all p = p(n) ≥ C/n, the local resilience of Rn,p with respect to the property of containing all trees Tm of m := ⌊(1 − α)n⌋ vertices and maximum degree dmax(Tm) ≤ ∆ is almost surely greater than 21 − γ.

![image 210](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile210.png>)

As a subcase, this contains

- Theorem 5.47 (Balogh, Csaba, and Samotij [68]). Let α be a positive constant, and assume that ∆ ≥ 2. There exists a constant C > 0 (depending on α, and ∆) such that for all p = p(n) ≥ C/n, Rn,p contains all trees Tm of m ≤ (1−α)n vertices and maximum degree dmax(Tm) ≤ ∆, almost surely, as n → ∞.


The proof uses a sparse Regularity Lemma and a theorem of Penny Haxell [457] on embedding bounded degree trees into “expanding” graphs.

- 5.9. Extremal subgraphs of Pseudo-Random graphs

Another direction of research is when the Universe consists of more general objects, say of pseudo-random graphs. These are natural directions:

- (a) whenever we can prove a result for complete graphs Kp, we have a hope

to extend it to any L with critical edges, and

- (b) whenever we know something for Random Graphs, there is a chance that


it can be extended to random-looking objects (say to quasi-random graphs, or Pseudo-Random graphs, or to expanders graphs.96.)

We mention here a few such papers: Thomason [802, 803], Krivelevich and Sudakov [559] are nice and detailed surveys on Pseudorandom graphs. AignerHorev, Ha`n, and Schacht [5], and D. Conlon, J. Fox, and Yufei Zhao [198] also are two more recent nice papers (surveys?) on this topic. We recommend these papers, and also K¨uhn and Osthus [564]. For hypergraphs see, e.g., Haviland and Thomason, [454, 455], or Kohayakawa, Mota and Schacht [526].

- 5.10. Extremal results on “slightly randomized” graphs


Bohman, Frieze, and Martin [113] proved Hamiltonicity for graphs Rn obtained from a non-random graph G0n whose minimum degree was d < n/2 where Rn is

![image 211](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile211.png>)

- 94The “edit” distance is the same used in [750]: the minimum number of edges to be changed

to get from Gn a graph isomorphic to Hn.

- 95Though we formulate a theorem on the local resilience of graphs for some graph property,


we shall not deﬁne here the notion of local and global resilience: we refer the reader to the papers of Sudakov and Vu [786], or Balogh, Csaba, and Samotij [68], or suggest to read only

- Theorem 5.47. 96We have deﬁned only the quasi-random graphs here, for pseudo-random graphs see e.g.


[802, 559], for expanders see e.g. [20].

obtained by adding to G0n a random binomial graph Rn,p whose edge-probability is a small p = pn > 0. Dudek, Reiher, Ruci´nski, and Schacht continued this line, using this model, and proving in [247] that the stronger conclusion of Po´sa-Seymour conjecture holds almost surely for the obtained graph, under their conditions: instead of a Hamiltonian cycle they obtained a power of it.

- 5.11. Algorithmic aspects

Whenever we use an existence-proof in combinatorics, it is natural to ask if we can turn it into an algorithm. This was the case with the Lov´asz Local Lemma, and this is the case with the Regularity Lemma, and also with the Blow-up Lemma.

The algorithmic aspects of the Lov´asz Local Lemma were investigated ﬁrst by J´ozsef Beck [95], and later by R.A. Moser and G. Tardos [619], [620], and many others.

— · —

Alon, Duke, Lefmann, Ro¨dl, and Yuster in [30] showed that one can ﬁnd the Regular Partition, and the Cluster Graph of a Gn fairly eﬃciently. Actually, they proved two theorems: (a) to decide if a partition is ε-regular is diﬃcult, but (b) to ﬁnd an ε-regular partition of a given graph is easy. More precisely,

- Theorem 5.48 ([30]). Given a graph Gn and an ε > 0, and a partition (V0,...,Vk),97 it is Co-NP-complete to decide if this partition is ε-regular.
- Theorem 5.49 ([30]). For every ε > 0 and every t > 0, there exists a Q(ε,t)


such that for every Gn with n > Q(ε,n) one can ﬁnd an ε-Regular Partition (described in Thm 5.3) in O(M(n)) steps, where M(n) is the “number of steps” needed to multiply two 0 − 1 matrices over the integers.98 99

The algorithmic problem with the Regularity Lemma is that we may have too many clusters. Therefore a direct way to transform it into an eﬃcient algorithm may be hopeless. The Frieze-Kannan version often solves this problem, see Subsection 5.13, or [485, 364, 365], or Lov´asz-Szegedy [595].

The above methods were needed and extended to hypergraphs, see e.g. Nagle, Ro¨dl, and Schacht [629]. Remark 5.50. We needed this short section here, since it helps to understand the next part better: otherwise it would come later.

- 5.12. Regularity Lemma for the Analyst


As soon as the theory of Graph Limits turned into a fast-developing research area, it became interesting, what happens with the regularity lemmas in this

![image 212](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile212.png>)

97Here we have k+1 classes, since originally there was also an exceptional class V0, diﬀerent

from the others. This V0 can be forgotten: its vertices can be distributed in the other classes. 98The theorem also has a version on parallel computation. 99Here we do not deﬁne the “steps” and ignore again the diﬀerence caused by neglecting V0

in Theorem 5.3.

area. As we have mentioned, Lov´asz wrote ﬁrst a long survey [590], then a thick book on graph limits [591], so we shall not discuss it here, but mention just one aspect. The paper of Lov´asz and Szegedy [595] with the title “Szemer´edi Lemma for the analyst” not only described the Regularity Lemma in terms of the Mathematical Analysis, but also described the Weak Regularity Lemma (i.e. the Frieze-Kannan version [365]), and the Strong Regularity Lemma [33] of Alon, Fischer, Krivelevich, and M. Szegedy, and connected the Regularity Lemma to ε-nets in metric spaces, and to Compactness. We quote part of the Introduction of their paper.

”Szemere´di’s regularity lemma was ﬁrst used in his celebrated proof of the Erd˝sTur´an Conjecture on arithmetic progressions in dense sets of integers.100 Since then, the lemma has emerged as a fundamental tool in Graph Theory: it has many applications in Extremal Graph Theory, in the area of ‘Property Testing’ in computer science, combinatorial Number Theory, etc. . . . Tao described the lemma as a result in probability. Our goal is to point out that Szemere´di’s lemma can be thought of as a result in analysis. We show three diﬀerent analytic interpretations. The ﬁrst one is a general statement about approximating elements in Hilbert spaces which implies many diﬀerent versions of the Regularity Lemma, and also potentially other approximation results. The second one presents the Regularity Lemma as the compactness of an important metric space of 2-variable functions. . . . The third analytic interpretation shows the connection between a weak version of the regularity lemma and covering by small diameter sets, i.e., dimensionality. . . . We describe two applications of this third version: . . . and an algorithm that constructs the weak Szemere´di partition as Voronoi cells in a metric space.”

Actually, it is surprising that such a short paper can describe such an involved situation in such a compact way, also including the proofs.

- 5.13. Versions of the Regularity Lemma


There are many versions of the Regularity Lemma. Below we list some of them, with very short descriptions. Many of them are diﬃcult to invent but have you invented them, their proofs are often very similar to the original proof. (In case of Hypergraph Regularity Lemmas the situation is completely diﬀerent.)

We have already described the Regularity Lemma.

Coloured version. There is an easy generalization of the Regularity Lemma in which the edges of a graph Gn are r-coloured, for some ﬁxed r, so we have r edge-disjoint graphs, and we wish to ﬁnd a vertex-partition which satisﬁes the Regularity Lemma in all the colours, simultaneously. This is possible and often needed, e.g., in the Erdo˝s-Hajnal-S´s-Szemer´edi extension of Theorem

- 5.21 (in [295]), and more generally, this was used in Ramsey type theorems and Ramsey-Tur´an type theorems, and later in many similar cases.


![image 213](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile213.png>)

100As we have mentioned, this is not quite true. It was invented to prove a conjecture of Bollob´as, Erd˝s, and Simonovits on the parametrized Erd˝os-Stone theorem, and was ﬁrst used in the paper of Chva´tal and Szemer´edi [188]. A weaker, bipartite, asymmetric version of it was used to prove that rk(n) = o(n).

Weak Regularity Lemma. There is an important weakening of the Regularity Lemma, namely the Frieze-Kannan Weak Regularity Lemma [365], see also [364, 366] and the Frieze-Kannan-Vempala approach [367]. The diﬀerence between the Regularity Lemma and the Weak Regularity Lemma is that the later one ensures ε-regularity only for “much larger subsets”, and (therefore) needs much fewer clusters. Here the Weak ε-regularity means that given a partition U1,...,Uk, for a subset X ⊂ V (Gn) we hope to have

E(X) := d(Ui,Uj) · |Ui ∩ X||Uj ∩ X| edges in G[X], so we conclude that E(X) is close to e(X).

— · —

While the original algorithm of Frieze and Kannan is randomized, Dellamonica, Kalyanasundaram, Martin, Ro¨dl, and Shapira [233] provided a deterministic O(n2) algorithm, analogous to Theorem 5.49, to ﬁnd the Frieze-Kannan Partition.

This regularity lemma is more connected to Statistics101, and in many cases, where one can apply a regularity lemma for an existence proof, the algorithmic versions of the regularity lemmas provide algorithms in these applications too.

As we wrote, these algorithms are slow because of the very large number of clusters.102 but in many such cases the Algorithmic Weak Regularity Lemma can also be used, and then it provides a much faster algorithm, basically because it requires much fewer classes in the ε-regular partition.

One should remark that the Frieze-Kannan Regularity Lemma can be iterated and then it provides a proof of the original Szemer´edi Regularity Lemma.

On the other end, there is the Strong Regularity Lemma of Alon, Fischer, Krivelevich, and M. Szegedy [33]. The advantage of the Strong Regularity Lemma is that it can be applied in several cases where the original Regularity Lemma is not enough, primarily when we are interested in induced subgraphs.

We shall not formulate this strong lemma but include an explanation of it, from Alon-Shapira [43] (with a slight simpliﬁcation). Alon and Shapira write:

. . . This lemma can be considered a variant of the standard Regularity Lemma, where one can use a function that deﬁnes ε > 0 as a function of the size of the partition, rather then having to use a ﬁxed ε as in Lemma 2.2.

Large part of this is described in the paper of Lov´asz and B. Szegedy [595].

5.14. Regularity Lemma for sparse graphs

The Regularity Lemma can be used in many cases but has several important limitations.

![image 214](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile214.png>)

101Principal component analysis, see e.g. Frieze, Kannan, Vempala, and Drineas [367, 246]. 102There are many results showing that the number of clusters must be very large. The ﬁrst

such result is due to Gowers [401].

- (a) Because of the large threshold n0, one cannot combine it with computer

programs, checking the small cases. In other words, it is a theoretical result but it cannot be used in practice.

- (b) The most serious limitation is that we can apply it for embedding H into

G only if the degrees in H are (basically) bounded.

- (c) Another one is that it can be applied only to dense graphs Gn. This


problem is partly solved by the Sparse Regularity Lemma, established by Kohayakawa [524], and Ro¨dl, see also [528].

For sparse graph sequences, i.e. when e(Gn) = o(n2), the original Regularity Lemma is trivial but does not give any information. Having a bipartite subgraph H[U,V ] ⊆ Gn, consider the following “rescaled” density:

e(U,V ) p · |U||V |

. (5.5)

dH,p(U,V ) :=

![image 215](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile215.png>)

If p > 0 is very small, e.g., p := n−2/3, then the condition |dH,p(X,Y ) − dH,p(U,V )| < ε

does not say anything without 1/p in (5.5), but with 1/p it is a reasonable and strong restriction for sparse graphs. The Sparse Regularity lemma says that for “nice” graphs Hn there is a partition V1,...,Vν, described in the Regularity Lemma, even if we use this stronger regularity requirement (5.5). Which are the “nice” graphs?

(d) Sparse regularity lemmas are well applicable when the graph Gn to be approximated by generalized quasi-random graphs does not contain subgraphs whose density is much above the edge-density of Gn, e.g, for some bound b and the edge density p = e(Gn)/ n2 ,

E(V1,V2) < bp|V1||V2| if |V1|,|V2| > ηn. (5.6)

This is the situation, e.g., when we consider (non-random) subgraphs of random graphs, see Section 5.7.

The sparse Regularity Lemma sounds the same as the original Regularity Lemma, with two diﬀerences: we use the modiﬁed uniformity: (5.5), instead of (5.1), and the extra condition (5.6), for some ﬁxed b.

One of the latest developments in this area is a sparse version of the Regularity Lemma due to Alex Scott [734]. Scott succeeded in eliminating the extra condition on the sparse graph that it had no (relatively) high density subgraphs. However, this had some price, discussed by Scott in Section 4 of [734]. This new sparse Regularity Lemma was used in several cases, e.g. by P. Allen, P. Keevash, B. Sudakov, and J. Verstra¨ete, in [19].

- Remark 5.51. As we wrote, the Sparse Regularity Lemma can be used ba-


sically if Gn does not contain subgraphs much denser than the whole graph. Gerke and Steger wrote an important survey about it and about its applicability [392], see also [391]. Its applicability is discussed (among others) in the

paper of Conlon, Gowers, Samotij, and Schacht [200], with its connection to the Kohayakawa- Luczak-R¨dl conjecture [525]. We also warmly recommended the paper of Conlon, Fox, and Yufei Zhao [198].

- 5.15. Quasi-Random Graph Sequences

Quasi-random sequences are very important, e.g., in Theoretical Computer Science, and also very interesting, for their own sake. In Graph Theory they emerged in connection with some Ramsey problems. The ﬁrst detailed, pioneering results in this direction are due to A. Thomason, see e.g. [802, 803]. He was motivated by some Ramsey Problems.

Chung, Graham and Wilson [185] developed a theory in which six properties of random graphs were formulated which are equivalent for any inﬁnite sequence (Gn) of graphs. The graphs having these properties are called quasi-random.

Quasi-randomness exists in other universes as well, e.g., there exist quasirandom subsets of integers, groups, see Gowers [405], tournaments, see Chung and Graham [184, 183], of real numbers, digraphs [338], of hypergraphs, e.g., Chung [180, 181, 182], Ro¨dl and Kohayakawa [528], permutations, see J. Cooper [205],Kr´al and Pikhurko [555], and in many other settings...

Quasi-randomness and the Regularity Lemmas are very strongly connected. This was ﬁrst established in a paper of Simonovits and So´s [764]:

Theorem 5.52 (Simonovits, So´s (1991), [764]). A sequence of graphs (Gn) is p-quasi-random iﬀ for every κ > 0 and ε > 0, there exist two thresholds k0(ε,κ) and n0(ε,κ) such that for n > n0(ε,κ) Gn has an ε-Regular Partition where all the pairs (Vi,Vj) are ε-regular with densities between p − ε < d(Vi,Vj) < p + ε and κ < k < k0(ε,κ).

Remark 5.53. Actually, a slightly stronger theorem holds. On the one hand, we may allow ε k2 exceptional pairs (Vi,Vj) to ensure p-quasi-randomness. On the other hand, if (Gn) is p-quasi-random, we can ﬁnd a partition where there are no exceptional pairs.

The corresponding generalization for sparse graphs was proved by Kohayakawa and Ro¨dl. For a longer and detailed survey see their paper [528].

For further related results see, e.g., Simonovits and So´s [765, 767], Skokan and Thoma [768], Yuster [821], Shapira and Yuster [736], Gowers on Counting Lemma [403], on quasi-random groups [405], and also Janson [475], Janson and So´s [477] on the connections to Graph Limits.

A generalization of the notion of Quasi-random graphs was investigated by Lov´asz and So´s [594] which corresponds to generalized random matrix-graphs.

- 5.16. Blow-up Lemma


Several results exist about embedding spanning subgraphs into dense graphs. Many of the proofs use a relatively new and very powerful tool, called Blowup Lemma. Here we describe it in a fairly concise way. The Blow-up Lemma is

mostly used to embed a bounded degree graph H into a graph G as a spanning subgraph. The reader is also referred to the excellent “early” survey of Koml´os [533] (explaining a lot of important background details about the Regularity Lemma and the Blow-Up lemma, and how to use them) or to the surveys of Koml´os and Simonovits, [546], Koml´os, Simonovits, Shokoufandeh, and Szemer´edi, [545]. The “Doctor of Sciences” Thesis of Sa´rk¨ozy [722] is also an excellent source in this area. For some newer results on the topic see e.g., Ro¨dl and Ruci´nski [687], Keevash [497] who extended the method to hypergraphs, Sa´rk¨ozy [724], B¨ottcher, Kohayakawa, Taraz, and W¨urﬂ [143] extended it to ddegenerate graphs.103 A long survey of Allen, B¨ottcher, Han, Kohayakawa, and Person [18] discusses several features of the Blow-up Lemma applied to random and pseudo-random graphs. Recently Allen, B¨ottcher, Ha`n, Kohayakawa, and Person extended the Blow-up lemma to sparse graphs [18].

— · We start with a deﬁnition.

- Definition 5.54 ((ε,δ)-super-regular pair). Let G be a graph, U,W ⊆ V (G) be two disjoint vertex sets, |U| = |W|. The vertex-set pair (U,W) is (ε,δ)-superregular if it is ε-regular and dmin(G[U,W]) ≥ δ|U|.


The Blow-up Lemma asserts that (ε,δ)-regular pairs behave as complete bipartite graphs from the point of view of embedding bounded degree subgraphs. In other words, for every large ∆ > 0 and small δ > 0 there exist an ε > 0 such that if in the Cluster graph Hν the min-degree condition also holds and we replace the (ε,δ)-regular pairs (Ui,Uj) by complete graphs and then we can embed (the bounded degree) Hn into this new graph Gn, then we can embed it into the original Gn as well. The low degree vertices of Gn could cause problems. Therefore, for embedding spanning subgraphs, one needs all degrees of the host graph large. That’s why using regular pairs is not suﬃcient any more, we need super-regular pairs. Again, the Blow-up Lemma plays crucial role in embedding spanning graphs Hn into Gn.

The diﬃculty is in embedding the “last few” vertices. The original proof of the Blow-up Lemma starts with a probabilistic greedy algorithm, and then uses a K¨nig-Hall argument to complete the embedding. The proof is quite involved.

- Theorem 5.55 (Blow-up Lemma, Koml´os-S´ark¨ozy-Szemer´edi1994 [539]). Given a graph Hν of order ν and two positive parameters δ,∆, there exists an ε > 0 such that if n1,n2,...,nr are arbitrary positive integers and we replace the vertices of Hν with pairwise disjoint sets V1,V2,...,Vν of sizes n1,n2,...,nν, and construct two graphs on the same vertex-set V = Vi so that


- (i) the ﬁrst graph Hν(n1,...,nν) is obtained by replacing each edge {vi,vj}

of Hν with the complete bipartite graph K(ni,nj) between the corresponding vertex-sets Vi and Vj,

- (ii) and second, much sparser graph Hν∗(n1,...,nν) is obtained by replacing


each {vi,vj} with an (ε,δ)-super-regular pair between Vi and Vj,

![image 216](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile216.png>)

103They call it d-arrangable.

then if a graph L with dmax(L) ≤ ∆ is embeddable into Hν(n1,...,nν) then it is embeddable into the much sparser Hν∗(n1,...,nν) as well.

The Blow-up Lemma has several diﬀerent proofs, e.g., Koml´os, Sa´rk¨ozy, and Szemer´edi ﬁrst gave a randomized embedding [539], and then they gave a derandomized version [541] as well. Other proofs were given, e.g., by Ro¨dl, Ruci´nski [687], Ro¨dl, Ruci´nski and Taraz [698], and Ro¨dl, Ruci´nski and Wagner [698].

Remark 5.56. G.N. Sa´rk¨ozy gave a very detailed version of the proof of the Blow-up lemma, [724], where he calculated all the related details very carefully in order that he and Grinshpun could use it in their later work [422], Theorems 7.22,7.23: without this they could prove only a weaker result.

5.17. Regularity lemma in Geometry

Until now we restricted our consideration to applications of the Regularity Lemma to embed sparse graphs into dense graphs. The Regularity Lemma has several applications in other ﬁelds as well, and beside this, versions tailored to these other ﬁelds. Here we mention only a few such versions, very brieﬂy.

A theorem of Green and Tao [418] is a good example of this. They prove a so called arithmetic regularity lemma that can be applied in Additive Combinatorics, in several problems similar to Szemer´edi theorem on arithmetic progressions. However, here we wish to speak of Geometry.

There are several cases where we restrict our consideration to some particular graphs, e.g., to graphs coming from geometry. In this case one may hope for much better estimates in some cases than for arbitrary graphs. A whole theory was built up around such problems, see, e.g., Erdo˝s [260, 270], a survey Szemer´edi [795], Szemer´edi and Trotter [796], Pach and Sharir [640] ...or the book of Pach and Agarwal [639]. We remark here only that the Regularity Lemma also has some strengthened form, see, e.g., the improvement of some results of Fox, Gromov, Laﬀorgue, Naor, and Pach [348] by Fox, Pach and Suk [351]...

So the Regularity Lemma can be applied in Geometry in many cases and the fact that we apply it to geometric situation implies that in many cases the connection between the clusters will be a (basically) complete connection, or very few edges, instead of having randomlike connections. This is not so surprising, since many of the geometric relations are described by polynomials, or analytic functions, (?) and in these cases, if we have “many” 0’s of a polynomial (of several variables) then the corresponding polynomial must vanish everywhere.104 It seems that in most cases where Regularity Lemma is used in Geometry, its use can be eliminated.

The interested reader is suggested to read, e.g., the survey of J. Pach [638], or his book with Agarwal [639], the papers of Alon, Pach, Pinchasi, Radoiˇci´c, and Sharir [41], on semi-algebraic sets, or the paper of Fox, Gromov, Laﬀorgue, Naor, and Pach [348], or the paper of Pach and Solymosi, [641], or of J. Pach

![image 217](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile217.png>)

104One form of this is expressed in the Combinatorial Nullstellensatz of Alon [23].

[637]. The result of Karasev, Kynˇcl, Pat´ak, Pat´akov´a, and Martin Tancer [487] is also related to this topic.

#### 6. With or without Regularity Lemma?

Regularity Lemma is one of the most eﬀective, most eﬃcient lemmas in Extremal Graph Theory. In several cases we can prove a result with the Regularity Lemma, but later we ﬁnd out that it can easily be proven without the Regularity Lemma as well. So it is natural to ask if it is worth getting rid of the application of Regularity Lemma, if we can. The answer is not so simple. We should mention a disadvantage and two advantages of using the Regularity Lemma.

The disadvantage is that it can be applied only to very large graphs. This means that “in practice it is of no use”. This bothers some people, e.g., those who wish to ﬁnd out, – sometimes with the help of computers – the truth for the smaller values as well. Many of us feel this unimportant, some others deﬁnitely prefer eliminating the use of Regularity Lemma if it is possible. First we quote an opinion against the usage of the Regularity Lemma. In Subsection 5.5 we discussed the beautiful conjecture of Murty and Simon on the maximum number of edges a diameter-2-critical graph can have. We have mentioned that F¨uredi [371] solved this problem in 1992, using the Ruzsa-Szemer´edi theorem that f(n,6,3) = o(n2). Much later, in 2015, a survey [460] on the topic described this area very active and wrote:

“The most signiﬁcant contribution to date is an astonishing asymptotic result due to Fu¨redi (1992) who proved that the conjecture is true for large n, that is, for n > n0 where n0 is a tower of 2’s of height about 1014. As remarked by Madden (1999), ‘ n0 is an inconceivably (and inconveniently) large number: it is a tower of 2’s of height approximately 1014.’ Since, for practical purposes, we are usually interested in graphs which are smaller than this, further investigation is warranted. . . ”

First of all, it is not clear if it is correct to call F¨uredi theorem an “asymptotic result”. The advantage of applying the Regularity Lemma is that it often provides a proof where we have no other proofs, and, in other cases, a much more transparent proof than the proof without it. (Thus for example, the beautiful theorem of Erdo˝s, Kleitman, and Rothschild [297] was proved originally without the Regularity Lemma, but for many of us the Regularity Lemma provides a more transparent proof.)

Perhaps one of the ﬁrst cases where we met a situation where the Regularity Lemma could be eliminated was a paper of Bollob´s, Erdo˝s, Simonovits, and Szemer´edi, [128] discussing several distinct extremal problems, and one of them was which could be considered as one germ of Property Testing:

Problem 6.1 (Erd˝os). Is it true that there exists a constant Mε such that if one cannot delete εn2 edges from Gn to make it bipartite then it has an odd cycle Cℓ with ℓ < Mε?

The answer was

Theorem 6.2 (Bolloba´s, Erdo˝s, Simonovits, and Szemer´edi [128]). YES, if one cannot delete εn2 edges from Gn to make it bipartite then one can ﬁnd an odd cycle Cℓ with ℓ < 1ε.

![image 218](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile218.png>)

In [128] we gave two distinct proofs of this theorem, one using the Regularity Lemma and another one, without the Regularity Lemma. Interestingly enough, these questions later became very central and important in the theory of Property Testing, but there, in the works of Alon, Krivelevich, Shapira, and others, (see e.g., [33]) it turned out that such property testing results depend primarily on whether one can apply the Regularity Lemma or not. Just to illustrate this, we mention from the many similar results the paper of N. Alon, E. Fischer, I. Newman and A. Shapira [34], the title of which is “A combinatorial characterization of the testable graph properties: It’s all about regularity”.105

Remark 6.3. Duke and Ro¨dl [249] extended Theorem 6.2 to higher chromatic number, answering another question of Erdo˝s, see also the ICM lecture of Ro¨dl [685], and also the result of Alon and Shapira on property testing [43]. (R¨odl: “Further reﬁnement was given by Austin and Tao” [53].)

So we emphasise again that there are several cases where certain results can be proved with and without the Regularity Lemma, and the proof with the Regularity Lemma may be much more transparent, however, the obtained constants are much worse. Before proceeding we formulate a meta-conjecture about the “elimination”.

Meta-Conjecture 6.4 (Simonovits). The use of the Regularity Lemma can be eliminated from those proofs where

- (i) the conjectured extremal structures are “generalized random graphs”

with a ﬁxed number of classes and densities 0 and 1, and

- (ii) at least one of the densities is 0 and one of them is 1. One has to be very careful with this – otherwise informative - Meta-Conjecture:


- (a) First of all, mathematically it is not quite well deﬁned, what do we mean

by “eliminating the Regularity Lemma”.

- (b) Further, without (ii) the Ruzsa-Szemer´edi Theorem could be regarded

as a “counter-example”.106

- (c) It is not well deﬁned if using graph limits we regard as elimination of the

Regularity Lemma or not?

- (d) The ﬁrst two-three results which we like proving nowadays to illustrate


the usage of the Regularity Lemma, e.g. the Ramsey-Tur´an estimate for K4 (Thm 5.21) and Ruzsa-Szemer´edi Theorem, originally were proved using some weaker forms of the Regularity Lemma.

![image 219](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile219.png>)

- 105Two remarks should be made here: (a) Originally Property Testing was somewhat diﬀerent, see e.g. O. Goldreich, S. Goldwasser and D. Ron [399]. (b) The theory of graph limits also has a part investigating property testing, see e.g., [138, 140],. . . , [596].
- 106Actually, J. Fox eliminated the application of the Regularity Lemma from the proof of the Triangle Removal Lemma, see Section 5.4 or [347].


In several cases originally the Regularity Lemma was used to obtain some results, but then it was easily eliminated. Such examples are Erdo˝s and Simonovits [315], or Pach and Solymosi [641], on Geometric Graphs, or results in the paper of Erdo˝s, S.B. Rao, Simonovits, and So´s, [304]. Often in the published versions we do not even ﬁnd the traces of the original proof with Regularity Lemma, anymore ...

One interesting case of this discussion is the proof of

Conjecture 6.5 (Lehel’s conjecture [54]). If we 2-colour the edges of Kn, then V (Kn) can be covered by two vertex-disjoint monochromatic cycles of distinct colours.

- Remark 6.6. The ﬁrst reference to Conjecture 6.5 can be found in the PhD thesis of Ayel [54]. The conjecture was ﬁrst proved by  Luczak, Ro¨dl, and Szemer´edi [602], using the Regularity Lemma. Of course, this worked only for very large values of n. The Regularity Lemma type arguments were eliminated by


Peter Allen [14]. The diﬀerence between the two proofs is that Allen covers Kn by monochromatic cliques, using Ramsey’s theorem, instead of using Regularity type arguments. Hence the threshold in the ﬁrst proof is very large, and in Allen’s proof it is “only” 218000. Finally, surprisingly, Bessy and Thomass´e [108] found a simple and short proof of the conjecture, without using the Regularity Lemma, or any deep tool, and which worked for all n.

— · Conjecture 6.5 was extended by Gy´arf´s to any number of colours:

Conjecture 6.7 (Gya´rf´s, [424, 291]). If the edges of Kn are r-coloured, then V (Kn) can be covered by p(r) = r vertex-disjoint monochromatic cycles (where K1,K2 are also considered as cycles).

- Remark 6.8. This was “slightly” disproved for k ≥ 3 by Pokrovskiy [654]. Here “slightly” means that in his counterexample there is one vertex which could not be covered, however, p(r) = r+1 is still possible. We shall return to the Gy´arf´as conjecture (often called Gy´arf´s-Lehel conjecture) in Subsection 7.4.
- Remark 6.9. The results of Bessy and Thomass´e and of Erdo˝s, Gy´arf´as, and Pyber, (from Section 6.5) were extended to local r-colouring by Conlon and Maya Stein [201], where local r-colouring means that each vertex is adjacent only to at most r distinct colours, but the total number of colours may be much larger.


- 6.1. Without Regularity Lemma


There are several cases where eliminating the use of Regularity Lemma from the proof is or would be important. Above we discussed this and listed such cases. Here we mention two further cases. Fox gave a proof of the Removal Lemma without using the Regularity Lemma, in [347] (slightly simpliﬁed in the

beautiful survey of Conlon and Fox [194]). This improves several estimates in some related cases. Conlon, Fox and Sudakov [197] recently removed using the Regularity Lemma from the proof of a theorem of Simonovits and So´s [765], which helped to understand the situation better.

6.2. Embedding spanning or almost-spanning trees

Originally we planned to write – among others, – about our results on tree embeddings: about the solutions of the Erdo˝s-S´os conjecture and the Koml´osSo´s conjecture. However, they are described in [386] and in [470],[465]-[469], respectively, and we shall return to these topics elsewhere.

There are many results where we try to embed large or actually spanning trees into a graph Gn. We mention a few of them. Some of them describe a case when Gn is a random or randomlike graph, e.g., pseudo-random, expanding,...If we know something for random graphs, that often can (easily?) be extended to these cases: quasi-random, pseudo-random, or expander graphs. The “Resilience results” of Subsections 5.8 and 5.9 were of this type. One of the early results on expander graphs was

Theorem 6.10 (Friedman and Pippenger [363]). If for every X ⊆ V (Gn), with |X| ≤ 2k − 2,

|Γ(X)| ≥ (d + 1)|X|, then Gn contains all trees Tk with dmax(Tk) ≤ d.

Remark 6.11. The Friedman-Pippenger theorem “embeds” only relatively small trees. It was extended by Balogh, Csaba, Pei, and Samotij [67], where a result of Haxell [456] was simpliﬁed, and then used. This guaranteed embedding almost spanning trees into “expanding graphs”. We skip the precise formulation and the details, because they may look technical at ﬁrst sight.

For some earlier related works see Alon-Chung [29], and Beck [94].

— · —

Now we consider a conjecture of Bollob´s [119], on embedding bounded degree trees, proved by

Theorem 6.12 (Komlo´s, G.N. Sa´rk¨ozy, and Szemer´edi [537, 544]). For every ε > 0 and ∆ > 0, there exists an n0 for which, if Tn is a tree on n vertices with dmax(Tn) ≤ ∆, and Gn is a graph on n vertices with

n 2

+ εn, (6.1)

dmin(Gn) ≥

![image 220](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile220.png>)

then Tn ⊆ Gn, assuming that n > n0(∆). This was improved by

- Theorem 6.13 (Csaba, Levitt, Nagy-Gyo¨rgy, and Szemer´edi [215]). (a) For any constant ∆ > 0 there exists a constant c∆ > 0 such that if Tn is a tree on n vertices with dmax(Tn) ≤ ∆, and Gn is a graph on n vertices with


n 2

+ c∆ log n, (6.2)

dmin(Gn) ≥

![image 221](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile221.png>)

then Tn ⊆ Gn, assuming that n > n0(∆).

(b) There exist inﬁnitely many graphs Gn with dmin(Gn) ≥ 12n+ 171 log n not containing the complete ternary tree Tn[3].

![image 222](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile222.png>)

![image 223](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile223.png>)

So the bound in (6.2) is tight. The proofs in [537, 544] used the Regularity Lemma and the Blow-up lemma, while [215] did not use them, and provided smaller n0 and a sharper theorem. B. Csaba also extended the above results to well-separable graphs:

- Definition 6.14. An inﬁnite graph sequence (Hn) is well-separable, if one can delete o(n) vertices of Hn so that each connected component of the remaining graph has o(n) vertices, as n → ∞.


- Theorem 6.15 (Csaba [214]). For every ε,∆ > 0, there exists an n0 = n0(ε,∆) such that if (Hn) is well-separable, n > n0, and dmax(Hn) ≤ ∆, and


1 2(χ(H) − 1)

+ ε n, (6.3)

dmin(Gn) > 1 −

![image 224](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile224.png>)

then Hn can be embedded into Gn. For trees (or, more generally, for bipartite graphs Hn) (6.3) reduces to

dmin(Gn) ≥ 21n+εn: Theorem 6.15 is a generalization of Theorem 6.12. Another version is where we assume that Gn is bipartite, see Csaba [213].

![image 225](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile225.png>)

- 6.3. Po´sa-Seymour conjecture


Speaking of extremal problems, we could consider problems where we ask one of the following questions:

- (a) how large e(Gn) ensures a property P?
- (b) how large dmin(Gn) ensures P?
- (c) which (Ore type) degree sum conditions d(x)+d(y) ≥ fO(n,P) ensure P, where we assume this only for independent vertices x,y;
- (d) Given a graph Gn with the degree sequence d1,d2,...,dn, does it ensure P?


In the next part we consider two of these questions: (b), called Dirac type problems, and (c) called Ore type problems.

— · —

Hamiltonicity of graphs is a central problem in graph theory. There are many results of type (d), where some conditions on the degrees ensure the Hamiltonicity. In the Introduction we formulated one of the ﬁrst such results, Theorem 2.65:

Dirac Theorem. If dmin(Gn) ≥ n/2, and n ≥ 3, then Gn contains a Hamiltonian cycle.

Figure 7: Square of a cycle

As we have mentioned, this is sharp. We shall go into two distinct directions from Dirac’s Theorem: here we shall consider some generalizations for simple graphs, while in Section 9 we shall

discuss some hypergraph extensions. A natural question analogous to Dirac’s theorem was asked by Po´sa (see Erdo˝s [267] in 1965). The reader is reminded that the kth power L := Mk of a graph M is obtained from M by joining all the pairs of vertices x = y having distance ρM(x,y) ≤ k.

- Conjecture 6.16 (P´osa). If for a graph Gn dmin(Gn) ≥ 23n, then Gn contains the square of a Hamiltonian cycle.

![image 226](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile226.png>)

This was generalized by Seymour in 1973:

- Conjecture 6.17 (Seymour [735]). Let Gn be a graph on n vertices. If dmin(Gn) ≥ k


k+1n, then Gn contains the kth power of a Hamiltonian cycle.

![image 227](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile227.png>)

For k = 1, this is just Dirac’s theorem, for k = 2 the Po´sa conjecture. The validity of the general conjecture implies the notoriously hard Hajnal-Szemer´edi theorem (i.e. Theorem 2.67).107

Remark 6.18. Observe that for ℓ ≥ k + 1, we have Kk+1 = Pkk+1 ⊆ Pℓk. Hence Tn,k does not contain Pℓk. On the other hand, Pnk ⊂ Tn,k+1. This provides some further motivation for the above conjectures.

In the earlier parts we mostly considered embedding problems where the graph Hm to be embedded into the “host graph” Gn had noticeably fewer vertices than Gn, and thus one could use the Regularity Lemma. As we mentioned, when we embed spanning subgraphs, the embedding of the last few vertices may create serious diﬃculties and this diﬃculty was overcome by using the Regularity Lemma – Blow-up Lemma method. First in [540] Koml´os, Sa´rk¨ozy and Szemer´edi proved Conjecture 6.17 in its weaker, asymptotic form:

Theorem 6.19 (P´osa-Seymour conjecture - approximate form, (1994), [540]). For any ε > 0 and positive integer k there is an nk(ε) such that if n > nk(ε) and

1 k + 1

+ ε n,

dmin(Gn) > 1 −

![image 228](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile228.png>)

then Gn contains the kth power of a Hamilton cycle.

Next they got rid of ε in [538] and [542]: they proved both conjectures for n ≥ nk, without the extra ε > 0.

![image 229](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile229.png>)

107Actually, this was the motivation for P´osa.

- Theorem 6.20 (Komlo´s, Sa´rk¨ozy, and Szemer´edi [542]). For every integer k > 0 there exists an nk such that if n ≥ nk, and

dmin(Gn) ≥ 1 −

1 k + 1

![image 230](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile230.png>)

n, (6.4)

then the graph Gn contains the kth power of a Hamilton cycle.

The proofs used the Regularity Lemma [791], the Blow-up Lemma [539], [541] and the Hajnal-Szemer´edi Theorem [444]. Since the proofs used the Regularity Lemma, the resulting nk was very large (it involved a tower function). The use of the Regularity Lemma was removed by Levitt, Sa´rk¨ozy and Szemer´edi in a new proof of Po´sa’s conjecture in [575]. Much later, ﬁnally, P´eter Hajnal, Simao Herdade, and Szemer´edi found a new proof of the Seymour conjecture [446] that avoids the use of the Regularity Lemma, thus resulting in a “completely elementary” proof and a much smaller nk.

Historical Remarks. Partial results were obtained earlier on the Po´saSeymour conjecture, e.g., by Jacobson (unpublished), Faudree, Gould, Jacobson and Schelp [331], Ha¨ggkvist (unpublished), Genghua Fan and Ha¨ggkvist [329], and Fan and Kierstead [330]. Fan and Kierstead also announced a proof of the Po´sa conjecture if the Hamilton cycle is replaced by Hamilton path. (Noga Alon observed that this already implies the Alon-Fischer theorem mentioned in Subsection 2.19, since the square of a Hamilton path contains all unions of cycles.) We skip the exact statements of these papers, but mention that Chaˆu, DeBiasio, and Kierstead [177] proved Po´sa Conjecture for all n > 8 × 109.

Stability Remark. A crucial lemma of the proof in [446] is a “structural stability” assertion that for some constant γ > 0, either Gn contains an “almost independent” set of size k+1n or dmin(Gn) < (k+1k − γ)n.

![image 231](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile231.png>)

![image 232](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile232.png>)

6.4. Ore type results/Pancyclic graphs

As we have mentioned, the Hamiltonian problems, above all, Dirac Theorem on Hamiltonicity of graphs, led to several important research directions. Here there is a signiﬁcant diﬀerence between the graph and hypergraph versions. We shall return to the Hamiltonicity of hypergraphs in Section 9. As to ordinary graphs, some generalizations are the Ore-type problems, some other ones are the Po´sa-Seymour type generalizations, discussed in the previous subsection. In an Ore type theorem we assume that any two independent vertices have large degree sums. The ﬁrst such result was

- Theorem 6.21 (Ore, (1960), [635]). If for any two independent vertices x,y of Gn, deg(x) + deg(y) ≥ n, then Gn is Hamiltonian.


Bondy had an important “meta-theorem” according to which conditions implying Hamiltonicity imply also “pancyclicity”, which means that Gn contains

cycles of all length between 3 and n.108 A beautiful illustration is

- Theorem 6.22 (Bondy (1971), [134]). (a) If Gn is Hamiltonian and e(Gn) ≥

⌊n

2

![image 233](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile233.png>)

4 ⌋, then either Gn is pancyclic or Gn = K(n/2,n/2).

(b) Under the Ore condition, for any k ∈ [3,n], Gn contains a Ck, or Gn = K(n/2,n/2).

Of course, (b) follows from (a) and Ore theorem. Generalizations of these theorems can be found in Broersma, Jan van Heuvel, and Veldman, [149], and in general, there are very many “pancyclicity” theorems, see e.g. Erdo˝s [278], Keevash, Lee, and Sudakov [570, 506], Stacho [780], Brandt, Faudree, and Goddard [147], and many others. (In some sense the Bondy-Simonovits theorem in [136] is also a “weak pancyclic theorem”.) There are also very many results on pancyclic digraphs, see e.g. Ha¨ggkvist and Thomassen [461], Krivelevich, Lee, and Sudakov [557].

For some related results see e.g., Bollob´s and Thomason [132, 133] Brandt, Faudree, and Goddard [147], Favaron, Flandrin, Hao Li, and F. Tian [337], L. Stacho [780], Bar´at, Gy´arf´s, Lehel, and G.N. Sa´rk¨ozy [90], Bar´at and Sa´rk¨ozy [91], Kierstead and Kostochka [509], Kostochka109 and Yu [553] DeBiasio, Faizullah, and Khan [230], and many others.

Weakly pancyclic graphs. There are cases, when we cannot hope for all cycles between 3 and n. If a graph Gn contains all cycles between girth(Gn) and its circumference circ(Gn)110, then we call it weakly pancyclic, see e.g. Bollob´s and Thomason [132, 133]. We mention a theorem of [132], on the girth, answering some questions of Erdo˝s.

- Theorem 6.23 (Bolloba´s and Thomason). Let Gn be a graph with (at least) two distinct Hamiltonian cycles. Then n ≥ ⌊(g(G) + 1)2/4⌋, and therefore

girth(G) ≤

√4n + 1 − 1.

![image 234](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile234.png>)

There is a pancyclicity deﬁned for bipartite graphs, which considers only even cycles. The original Bondy-Simonovits theorem was also about such pancyclicity.

- Theorem 6.24 (Bondy and Simonovits (1974), [136]). If e(Gn) > 100kn1+(1/k), then Gn contains cycles of all lengths 2ℓ, for ℓ = k,...,⌊e(Gn)/(100n)⌋.


6.5. Absorbing Method

As we mentioned, when we try to embed a spanning subgraph Hm into a graph Gn, i.e. m = n, some diﬃculties may occur at embedding the “last few vertices”. This problem is often solved by using the Blow-up Lemma, or the Absorbing

![image 235](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile235.png>)

- 108In some cases we have only weaker conclusions, e.g., in the Bondy-Simonovits theorem [136], and also it may happen in some cases that we get only even cycles! See also the paper of Brandt, Faudree, and Goddard [147] on weakly pancyclic graphs.
- 109Kierstead, Kostochka and others have several results where Ore type conditions imply Hajnal-Szemer´edi type theorem [509, 512], or a Brooks type theorem [511].
- 110The circumference is the length of the longest cycle. Here we exclude the trees.


Method, some “Connecting Lemma”, or by some Stability Argument. Mostly we combine more than one of them. The stability argument in most of these papers has the form that we distinguish the “nearly extremal” and the “farfrom-extremal” cases. Then we handle these two cases separately: mostly we can handle the far-from extremal structure “easily”.

We mention among papers combining the Stability and the Absorbing methods the newest results of P. Hajnal, Herdade, and Szemer´edi [446] on the Po´sa-Seymour Conjecture, or Balogh, Lo, and Molla, Mycroft, and Sharifzadeh [73, 74, 75], on (Ramsey-Tur´an-) tiling, (see Subsection 6.7). Below we describe the Absorbing Method.

In the Absorbing Method, depending on the problem, we “invent” an Absorbing Structure, e.g., in the Erdo˝s-Gya´rf´s-Pyber theorem [291], the Triangle-Cycle TC2ℓ, (deﬁned below) see Figure 8. Then we start with choosing a special subset of vertices, A ⊆ V (Gn), deﬁning this special, absorbing

substructure G[A] in our graph/hypergraph, e.g., in [291] an A spanning a Triangle-Cycle. Next we put aside A and start building up the whole spanning structure in Gm = Gn − A as we would do this if m were “noticeably smaller” than n. If the “Absorbing Structure” G[A] is chosen appropriately, then we will be able to add the last few unembedded vertices of A at the end: A will absorb/pick up these remaining, uncovered vertices.

y

1

y x

2

x

1 2

x x

- 3
- 4


We illustrate this, using a proof-sketch of the Erdo˝sGy´arf´s-Pyber theorem. We shall return to some related newer, sharper results in Subsections 6.7 and 7.4.111

Figure 8: TriangleCycle TC2ℓ

- Theorem 6.25 (Erd˝os, Gy´arf´s, and Pyber [291]). In any r-colouring of the


edges of Kn, we can cover V (Gn) by p(r) = O(cr2 log r) vertex-disjoint monochromatic cycles.

- Remark 6.26. The analogous result for bipartite graphs was proved by Haxell [456].


The basic structure of the proof is as follows. First we deﬁne a “TriangleCycle” TC2ℓ (Figure 8). Its vertices are x1,...,xℓ and y1,...,yℓ; and its 3ℓ edges are xixi+1 (where xℓ+1 := x1), yixi, and yixi+1, for i = 1,...,ℓ.

- (a) First, for some c1 > 0, we ﬁnd a monochromatic Triangle-Cycle TC2ℓ in Gn, with ℓ > c1n.
- (b) Next we cover Gm = Gn − TC2ℓ with cr2 log r vertex-disjoint monochromatic cycles, also allowing to use some vertices from Y = {y1,...,yℓ}.
- (c) Finally, we can cover the remaining uncovered vertices with one more monochromatic cycle, since our triangle-cycle TC2ℓ has the nice property that deleting any subset Y ′ ⊆ Y , the remaining TC2ℓ − Y ′ is still Hamiltonian.


![image 236](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile236.png>)

111A stronger statement is Theorem 7.19.

The Absorbing Method was used in the paper of Ro¨dl, Ruci´nski, and Szemer´edi [692], to ﬁnd a matching in a hypergraph. This seems to be the breakthrough point: soon this method became very popular, both for graphs and hypergraphs. (In Tables 1-2 we list several graph- and hypergraph applications.) Replacing the regularity method by the Absorption Method is discussed, e.g., in Szemer´edi [793], Levitt, Sa´rk¨ozy and Szemer´edi [575].

In several cases one uses the Absorbing Method to get sharp results for n > n0 after having already a weaker, asymptotic result. Thus, DeBiasio and Nelsen [232], improving a result of Balogh, Bar´at, Gerbner, Gy´arf´as and Sa´rk¨ozy [60] proved a conjecture from [60]:

Theorem 6.27 (DeBiasio and Nelsen [232]). For any γ > 0 there exists an n0(γ) such that if n > n0(γ) and dmin(Gn) > (3/4+γ)n and E(Gn) is 2-coloured, then Gn contains two vertex-disjoint monochromatic cycles covering V (Gn).

Similarly, the 3-uniform hypergraph tiling results of Czygrinow, DeBiasio, and Nagle [221] are the sharp versions of some earlier results of K¨uhn and Osthus [560] on hypergraph tiling. Let us repeat that the essence of the Absorption Method is to construct certain “advantageous conﬁgurations”, substructures G[A], in Gn, called Absorbing Structure, covering a large part (say cn vertices) of the host-graph. Next – using the standard methods, – we cover all the vertices of Gn − G[A] with the given conﬁgurations and ﬁnally we can expand the embedded conﬁguration into a spanning conﬁguration, using the particular properties of this Absorbing Structure. Often the large Absorbing Structure consists of many small substructures, and we gain on each of them an uncovered vertex, obtaining at the end a spanning subgraph, as wanted.

We refer the interested reader to the Ro¨dl-Ruci´nski-Szemer´edi paper [695], using the “Absorbing Method”, and to the Ro¨dl-Ruci´nski survey [688], however here we mostly avoid the hypergraphs: we return to them in Section 9.112.

— · —

In Table 1 we list just a few successful graph-applications of the Absorbing Method. In some other cases, later, we shall just “point out” that the Absorbing Method was successful, when we discuss the corresponding results, e.g., in Sections 6.3, 6.7, 9,...We collected some papers using the Absorbing Method for hypergraphs in Table 3 (primarily on hypergraph matching) and in Table 2, in Section 9 (primarily on Hamiltonian hypergraphs).

These three tables are self-explanatory, however, they contain just a short list of the applications. We could include several further results, like the results of Lo and Markstr¨om on multipartite Hajnal-Szemer´edi results [576, 579], on graphs and hypergraphs, or [578]...

![image 237](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile237.png>)

112In several cases we must distinguish subcases also by some divisibility conditions: not only the proofs but the results also strongly depend on some divisibility conditions.

![image 238](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile238.png>)

![image 239](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile239.png>)

![image 240](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile240.png>)

![image 241](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile241.png>)

![image 242](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile242.png>)

![image 243](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile243.png>)

![image 244](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile244.png>)

Authors Year About what? (or title) Methods Where Erdo˝s, Gy´arf´as, 1991 cycle partition Absorbing [291] Pyber Perhaps the ﬁrst absorbing? JCTB Levitt, S´ark¨ozy, 2010 Po´sa, How to avoid Absorbing DM Szemer´edi Regularity Lemma Connecting [575]

![image 245](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile245.png>)

![image 246](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile246.png>)

![image 247](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile247.png>)

![image 248](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile248.png>)

![image 249](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile249.png>)

![image 250](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile250.png>)

![image 251](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile251.png>)

![image 252](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile252.png>)

![image 253](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile253.png>)

![image 254](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile254.png>)

![image 255](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile255.png>)

![image 256](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile256.png>)

![image 257](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile257.png>)

![image 258](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile258.png>)

![image 259](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile259.png>)

![image 260](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile260.png>)

![image 261](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile261.png>)

![image 262](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile262.png>)

![image 263](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile263.png>)

![image 264](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile264.png>)

![image 265](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile265.png>)

![image 266](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile266.png>)

![image 267](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile267.png>)

![image 268](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile268.png>)

![image 269](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile269.png>)

![image 270](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile270.png>)

![image 271](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile271.png>)

![image 272](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile272.png>)

![image 273](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile273.png>)

![image 274](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile274.png>)

![image 275](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile275.png>)

![image 276](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile276.png>)

![image 277](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile277.png>)

+ Stability Reservoir Keevash 2014 Existence of designs Absorption Arxiv 2018 One of the most celebrated Nibble [500]

![image 278](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile278.png>)

![image 279](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile279.png>)

![image 280](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile280.png>)

![image 281](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile281.png>)

![image 282](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile282.png>)

![image 283](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile283.png>)

![image 284](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile284.png>)

![image 285](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile285.png>)

![image 286](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile286.png>)

![image 287](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile287.png>)

![image 288](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile288.png>)

![image 289](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile289.png>)

![image 290](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile290.png>)

![image 291](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile291.png>)

![image 292](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile292.png>)

![image 293](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile293.png>)

![image 294](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile294.png>)

![image 295](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile295.png>)

![image 296](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile296.png>)

results of these years . . . [501] Ferber, Nenadov, 2014 Robust Hamiltonicity Connecting Arxiv Noever, Peter 2014 of random directed Absorbing Arxiv Skoric´ˇ graphs (resilience) [339] Balogh, Molla, 2016 Triangle factor + small Absorption RSA Sharifzadeh stable sets, Weighted graphs [75] Barber, K¨uhn, 2016 Edge decomposition of Iterative Advances Lo, Osthus graphs with high mindeg Absorption [93] Balogh-Lo-Molla 2017 Digraph packing Stability JCTB

![image 297](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile297.png>)

![image 298](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile298.png>)

![image 299](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile299.png>)

![image 300](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile300.png>)

![image 301](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile301.png>)

![image 302](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile302.png>)

![image 303](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile303.png>)

![image 304](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile304.png>)

![image 305](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile305.png>)

![image 306](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile306.png>)

![image 307](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile307.png>)

![image 308](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile308.png>)

![image 309](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile309.png>)

![image 310](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile310.png>)

![image 311](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile311.png>)

![image 312](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile312.png>)

![image 313](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile313.png>)

![image 314](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile314.png>)

![image 315](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile315.png>)

![image 316](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile316.png>)

![image 317](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile317.png>)

![image 318](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile318.png>)

![image 319](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile319.png>)

![image 320](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile320.png>)

![image 321](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile321.png>)

![image 322](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile322.png>)

![image 323](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile323.png>)

![image 324](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile324.png>)

![image 325](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile325.png>)

![image 326](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile326.png>)

![image 327](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile327.png>)

![image 328](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile328.png>)

![image 329](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile329.png>)

![image 330](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile330.png>)

![image 331](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile331.png>)

![image 332](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile332.png>)

![image 333](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile333.png>)

![image 334](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile334.png>)

![image 335](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile335.png>)

![image 336](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile336.png>)

![image 337](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile337.png>)

![image 338](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile338.png>)

![image 339](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile339.png>)

![image 340](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile340.png>)

![image 341](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile341.png>)

![image 342](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile342.png>)

![image 343](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile343.png>)

![image 344](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile344.png>)

![image 345](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile345.png>)

![image 346](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile346.png>)

![image 347](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile347.png>)

![image 348](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile348.png>)

![image 349](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile349.png>)

![image 350](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile350.png>)

![image 351](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile351.png>)

![image 352](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile352.png>)

![image 353](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile353.png>)

![image 354](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile354.png>)

in-out-degree ≥ 7n/18 Absorption [73]

![image 355](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile355.png>)

![image 356](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile356.png>)

![image 357](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile357.png>)

![image 358](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile358.png>)

![image 359](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile359.png>)

![image 360](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile360.png>)

![image 361](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile361.png>)

DeBiasio, Nelsen 2017 Strengthening Lehel conj. Absorbing JCTB

![image 362](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile362.png>)

![image 363](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile363.png>)

![image 364](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile364.png>)

![image 365](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile365.png>)

![image 366](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile366.png>)

![image 367](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile367.png>)

[232] Glock, K¨uhn, Lo, 2018 Existence of designs Iterative Arxiv Osthus Absorption [397]

![image 368](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile368.png>)

![image 369](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile369.png>)

![image 370](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile370.png>)

![image 371](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile371.png>)

![image 372](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile372.png>)

![image 373](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile373.png>)

![image 374](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile374.png>)

![image 375](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile375.png>)

![image 376](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile376.png>)

![image 377](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile377.png>)

![image 378](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile378.png>)

![image 379](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile379.png>)

![image 380](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile380.png>)

![image 381](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile381.png>)

![image 382](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile382.png>)

![image 383](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile383.png>)

![image 384](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile384.png>)

![image 385](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile385.png>)

![image 386](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile386.png>)

Connection

![image 387](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile387.png>)

![image 388](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile388.png>)

![image 389](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile389.png>)

![image 390](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile390.png>)

![image 391](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile391.png>)

![image 392](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile392.png>)

![image 393](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile393.png>)

Montgomery 2018 Embedding bounded degree Iterative Arxiv trees into Random Graphs Absorption? [616] until p = ∆log5 n/n

![image 394](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile394.png>)

![image 395](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile395.png>)

![image 396](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile396.png>)

![image 397](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile397.png>)

![image 398](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile398.png>)

![image 399](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile399.png>)

![image 400](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile400.png>)

![image 401](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile401.png>)

![image 402](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile402.png>)

![image 403](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile403.png>)

![image 404](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile404.png>)

![image 405](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile405.png>)

![image 406](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile406.png>)

![image 407](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile407.png>)

![image 408](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile408.png>)

![image 409](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile409.png>)

![image 410](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile410.png>)

![image 411](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile411.png>)

![image 412](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile412.png>)

P. Hajnal, Her- 2018 Po´sa-Seymour Absorption Arxiv dade, Szemer´edi without Regularity Lemma Connection [446]

![image 413](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile413.png>)

![image 414](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile414.png>)

![image 415](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile415.png>)

![image 416](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile416.png>)

![image 417](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile417.png>)

![image 418](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile418.png>)

![image 419](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile419.png>)

Table 1: Absorbing method for graphs

- 6.6. Connecting Lemma, Stability, Reservoir


In Table 1 we see several papers using the Absorbing and the Stability Methods. We illustrate this on the example of the new proof of the Po´sa-Seymour conjecture [446], by P´eter Hajnal, Herdade, and Szemer´edi. It has two subcases. A small α > 0 is ﬁxed and Case 1 (the “non-extremal” one) is when each X ⊂ Gn of ⌊k+1n ⌋ vertices has e(X) ≥ αn2 edges. The remaining situation is Case 2, where we use the stability:

![image 420](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile420.png>)

- Theorem 6.28 (Hajnal-Herdade-Szemer´edi: Po´sa-Seymour, stability [446]). Given an integer k ≥ 2 and an α > 0, there exists an η = η(α,k) > 0 such


that in Case 1 (called α-non-extremal), if dmin(Gn) ≥ (1 − k+11 − η)k, then Gn contains the kth power of a Hamiltonian cycle.

![image 421](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile421.png>)

Whenever we use the Absorbing method, mostly we use some other tools

as well, tailored speciﬁcally to the problem in consideration. The Connecting Lemma and the Reservoir method are combined with the Absorbing Method, e.g., in the earlier paper of Levitt, Sa´rk¨ozy, and Szemer´edi [575] on how to eliminate the use of the Regularity Lemma and the Blow-up Lemma in the proof of the Po´sa conjecture. The Regularity Lemma, and the Blow-Up Lemma are eliminated in the tree-embedding paper of Csaba, Levitt, Nagy-Gyo¨rgy, and Szemer´edi [215], using the stability and some “elementary embedding methods”.

The very recent new proof of the Seymour conjecture, by P. Hajnal, Herdade, and Szemer´edi [446] is much more involved and much longer than the original proof. Here the authors use a “Connecting Lemma”, asserting that certain parts of Gn can be connected in many advantageous ways. This means that we have a Gn (with large minimum degree) and wish to ﬁnd a Cnk+1 ⊆ Gn. We cover most of the vertices by Tur´an graphs Tm,k+1 and Tm,k+2, where m → ∞. Inside these “blocks” we can easily connect some vertices by (k + 1)th power of a path covering this block, and we must connect these vertices from the various blocks so that altogether we get a (k + 1)th power of a Hamiltonian cycle. The Connecting Lemma does this.

6.7. Ramsey-Tur´an Matching

This subsection is about the ﬁfth line of Table 1, about [75]. The question is:

Does there a new, interesting phenomenon appear when we wish to ensure an almost perfect tiling, or a Hamiltonian cycle, or some other (almost) spanning conﬁguration in a graph Gn and assume that

α(Gn) = o(n). (6.5)

We have to decide if we wish to use that e(Gn) is large or that dmin(Gn) is large. We know that for ordinary non-degenerate extremal graph problems the edge-extremal and the degree-extremal problems do not diﬀer too much: if dex(n,L) is the maximum integer ∆ for which, if Gn is L-free, then dmin(Gn) ≤ ∆, then

2 n

ex(n,L), (6.6)

dex(n,L) ≈

![image 422](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile422.png>)

and asymptotically Tn,p is the degree-extremal graph (where p is deﬁned by (2.4)). We also saw that if we assume (6.5) then in some cases (6.6) can be noticeably improved, see e.g. Theorem 5.20. In other cases (6.5) changes the maximum only in a negligible way. However, one can also ask what happens if we assume (6.5) in cases when we wish to ensure a spanning (or an almostspanning) subgraph, e.g., a 1-factor, or a Hamilton cycle. Anyway, to ensure an (almost) 1-factor, or a Hamilton cycle we had better to have lower bounds on dmin(Gn) than on e(Gn). Without too much explanation, we formulate two related results.

Balogh, McDowell, Molla, and Mycroft studied the minimum degree necessary to guarantee the existence of perfect and almost-perfect triangle-tilings in Gn with α(Gn) = o(n). Among others, they proved

- Theorem 6.29 (Balogh, McDowell, Molla, and Mycroft (2018), [74]). Fix an ε > 0. If (Gn) is a graph sequence with α(Gn) = o(n) and dmin(Gn) ≥ n/3+εn, then Gn has a triangle-tiling covering all but at most four vertices, if n > n0(ε).

Of course, without the extra condition α(Gn) = o(n) we get back to the

Corradi-Hajnal theorem, where dmin(Gn) ≥ 23n is needed. The case when we do not “tolerate” the four exceptional vertices is described by [75]:

![image 423](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile423.png>)

- Theorem 6.30 (Balogh, Molla, Sharifzadeh [75]). For every ε > 0, there exists a γ > 0 such that if 3|n and


- 1

![image 424](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile424.png>)

- 2


dmin(Gn) ≥

+ ε n, and α(Gn) < γn,

then Gn has a K3-factor.113

The proofs in [75] also use the Stability method and the Absorbing technique of Ro¨dl, Ruci´nski, and Szemer´edi [693], discussed in Subsection 6.5.

#### 7. Colouring, Covering and Packing, Classiﬁcation

The setup. In this section we consider an r-edge-colouring of a Kn, or of a random graph Rn,p, or of any Gn satisfying some conditions. We have r families of potential subgraphs, Li, (i = 1,...,r), and try to cover Kn with as few monochromatic subgraphs Li ∈ Li in the ith colour as possible. However, there are several types of problems to be considered:

- (A) sometimes we wish to cover all or almost all the edges of the coloured graph,
- (B) in other cases we wish to cover all the vertices or almost all the vertices with the vertices of our monochromatic subgraphs.


These are quite diﬀerent problems and in the next subsection we shall list several versions of these problems, and in some sense, classify them.

There are several problems/results in Extremal Graph Theory simple to formulate, and when we combine some of them, we get very interesting new problems. However, sometimes it is diﬃcult to “classify” these problems. The reader could ask: “Why to classify them?” The answer is that without some classiﬁcation one may end up with a chaotic picture about the whole ﬁeld. Mostly,

we have a “host graph” Gn satisfying some conditions, e.g., it may be a complete graph Kn, or a random graph Rn,p, or a pseudo-random graph

![image 425](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile425.png>)

113The paper has an Appendix written by Reiher and Schacht, about a version of this problem, also using the Absorption technique. In this version they replace the condition that any linear sized vertex-set contains an edge by a condition that any linear sized set contains “many edges”.

with many edges, or with large minimum degree. There is also a family L of “sample” graphs114. Now, E(Gn) is r-coloured, and

- (a) either we wish to partition the vertices of Gn into a few classes, U1,...,Ut so that each G[Ui] spans a monochromatic Li ∈ L, or
- (b) we wish to cover the edges, E(Gn), by a few copies of monochromatic sample graphs, Li ∈ L, or
- (c) we wish to approximate the situation (a) or (b), allowing a few uncovered vertices.


Historical remarks. The case of one colour and vertex-disjoint packing goes back to several early papers in Extremal Graph Theory: several proofs, e.g., Erdo˝s [265], or later Simonovits [750], used that large part of the considered Gn can be covered by vertex-disjoint copies of some L.115 Also this was used in the new proof of the Po´sa-Seymour conjecture, in [446].

Mostly we deﬁne K1 and K2 also as monochromatic graphs from L: this is needed to ensure the existence of suitable colourings. The graphs in L may have more restricted or less restricted structure, e.g., they may be (A) all the connected graphs, or (B) all the trees, or (C) the sets of independent edges, or (D) all the cycles, or (E) the kth powers of the cycles, or (F) the Hamiltonian graphs, (G) on the other hand, they may be copies of the same ﬁxed graph L.

We start with Covering Problems where we have only one colour. We could continue with Ramsey problems, when we wish to ﬁnd just one monochromatic subgraph of a particular type, however, we have already written about Ramsey problems, and we shall not consider them here.

7.1. The One-colour Covering Problem

In this section we consider edge-coverings. Here is an early problem of Gallai, corresponding to the simplest case, to the monochromatic Gn i.e. r = 1.

Question 7.1. Given a sample graph L and a graph Gn, how many copies of L and edges are enough to cover E(Gn) (in the worst case)? In principle, we may require that the selected copies of L be (i) edge-disjoint, or (ii) vertex-disjoint, or (iii) we may allow them to overlap.

Of course, the L-free graphs need e(L) edges, so the L-extremal graphs need ex(n,L) copies of L or edges. One feels that if e(Gn) is much larger than ex(n,L), then one may use many copies of L and only a few edges. This motivates many results in this area. Here one of the ﬁrst important results is

Theorem 7.2 (Erd˝os, Goodman, and Po´sa (1966), [290]). Any graph Gn can be edge-covered by ⌊n

2

4 ⌋ complete subgraphs of Gn.

![image 426](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile426.png>)

![image 427](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile427.png>)

114Here we took Li = L. 115In some sense, this is used also in the original proof of Erd˝s-Stone theorem [321].

- Remark 7.3. (a) As it is stated in [290], to cover the edges, we may restrict ourselves to edges and triangles in Theorem 7.2.


- (b) Theorem 7.2 is sharp, as shown by Tn,2.
- (c) Theorem 7.2 was also proved by Lov´asz, as remarked in [290].


The extremal number for cycles is n − 1. Erdo˝s and Gallai conjectured (see [290]) and Pyber proved

- Theorem 7.4 (Pyber (1985), [667]). Every graph on n vertices can be edgecovered by n − 1 cycles and edges.


Note that for trees this is sharp. Pyber in [667] proved also some stronger results, and mentioned that the crucial tool in his proof was the following

- Theorem 7.5 (Lov´asz (1966), [581]). A graph on n vertices can be edge-covered by n2 disjoint paths and cycles.


![image 428](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile428.png>)

Lov´asz proved also several related theorems, e.g.,

- Theorem 7.6 (Lov´asz (1966), [581]). Any graph Gn can be edge-covered by 32n double-stars (trees of diameter ≤ 3).


![image 429](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile429.png>)

Another result of this (early) Lov´asz paper is a generalization of the Erdo˝sGoodman-P´osa theorem.116

- 7.2. Embedding monochromatic trees and cycles


In the following parts we consider edge-coloured graphs Gn and try to partition V (Gn) into a few subsets Vi spanning some monochromatic Hamiltonian cycles,117 or monochromatic powers of Hamiltonian cycles, or spanning trees.

These problems and results are related to Lehel’s Conjecture 6.5 about partitioning the vertices of edge-coloured graphs into two monochromatic cycles, and the Gy´arf´s Conjecture 7.7, (see [429]), about partitioning the vertices of edge-coloured graphs into given monochromatic trees. Here the colourings are always edge-colourings.118

Gy´arf´as tree-conjecture

The topic of graph packing has at least two larger parts: the vertex-packing and the edge-packing. Here we are interested in packing some given graphs Hi into a Gn in an edge-disjoint way. This problem is interesting on its own and also was originally motivated by Theoretical Computer Science, more precisely, by computational complexity, see e.g. the paper of Bollob´as and

![image 430](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile430.png>)

116For some related result for random or quasi-random graphs see [547],[558], [395],[398], and

many others. 117Here “G[Vi] is Hamiltonian” means that it has a spanning cycle. 118We used vertex-colouring in connection with colouring properties of excluded subgraphs,

or equipartitions in Hajnal-Szemer´edi theorem, . . .

Eldridge [123]. Given some graphs H1,...,Hℓ, their packing means ﬁnding the automorphisms π1,...,πℓ which map them into Kn in an edge-disjoint way.

For a family H1,...,Hm of graphs, we say that they pack into G, if they have edge-disjoint embeddings into G.

Conjecture 7.7 (Gya´rf´s (1978), [429]). Let for i = 1,2,...,n, Ti be an ivertex tree. Then Kn can be decomposed into these trees: {Ti} pack into Kn.

An asymptotic weakening of the conjecture was proved by B¨ottcher, Hladk´y, Piguet, and Taraz [142], for bounded degree trees.119 This was improved to a sharp version:

- Theorem 7.8 (Joos, J. Kim, K¨uhn, and Osthus (2016), [481]). For any ∆ > 0 there exists an n∆ such that for n > n∆, if T1,...,Tn are trees with dmax(Ti) < ∆ and v(Ti) = i (i = 1,...,n), then E(Kn) has a decomposition120 into T1,...,Tn.

Hence the tree packing conjecture of Gy´arf´s holds for all bounded degree trees, and suﬃciently large n. Beside several further results, [481] also contains the following fairly general result.

- Theorem 7.9. Let δ > 0 and ∆ be ﬁxed. Let F be a family of trees Tm of the following properties121:


- (i) For each Tm ∈ F, v(Tm) ≤ n, and dmax(Tm) ≤ ∆.
- (ii) For at least (12 + δ)n values of m v(Tm) ∈ [δn,(1 − δ)n].

![image 431](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile431.png>)

- (iii) m e(Tm) = n2 .


Then Kn can be decomposed into the trees Tm.

Remark 7.10. There is a vast literature on this topic and we recommend the reader to read the introduction of [481], and Gy´arf´s [426]. For results where we consider fewer trees, see e.g., Balogh and Palmer [83]. (The main tool of the proof in [83] is the Koml´os-S´ark¨ozy-Szemer´edi theorem [544] on embedding spanning trees.) Several related but slightly diﬀerent problems are discussed, e.g., in the survey of Kano and Li [486], e.g., it describes several Anti-Ramsey decomposition problems as well.

— · —

One could ask what happens if we wish to embed some trees into a noncomplete graph Gn. A nice result on this is Theorem 7.11 (Gya´rf´s [425]). If a sequence T1,T2,...,Tn−1 of trees can be packed into Kn then they can be packed also into any n-chromatic graph.

![image 432](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile432.png>)

119In fact, one can allow the ﬁrst o(n) trees to have arbitrary degrees. 120i.e. T1, . . . , Tn pack into Kn. 121We used superscript since here v(Tm) is not necessarily m.

- 7.3. Bollob´as-Eldridge conjecture

The packing problems (strongly connected to Theoretical Computer Science) were discussed roughly the same time by Bollob´s and Eldridge [123], Catlin [175], and Sauer and Spencer [729]. One of the most important conjectures in the ﬁeld of graph-packing is

- Conjecture 7.12 (Bolloba´s-Eldridge [123]). Let H1 and H2 be two n-vertex graphs. If

(dmax(H1) + 1)(dmax(H2) + 1) ≤ n + 1,

then there is a packing of H1 and H2, i.e., there are two edge-disjoint subgraphs of a complete graph Kn isomorphic to H1 and H2, respectively.

The complementary form of this problem is

- Conjecture 7.13 (Bolloba´s–Eldridge). Let dmax(Hn) ≤ k. If Gn is a simple graph, with


dmin(Gn) ≥

kn − 1 k + 1

![image 433](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile433.png>)

, then it contains Hn.

Aigner and Brandt [3], and Alon and Fischer [32] proved the conjecture for dmax(Hn) = 2, i.e. when Hn is the union of cycles. Csaba, Shokoufandeh, and Szemer´edi proved this for dmax(Hn) = 3.

- Theorem 7.14 (Csaba, Shokoufandeh, and Szemer´edi [217]). If Gn is a simple


graph, with dmin(Gn) ≥ 41(3n−1), then it contains any Hn for which dmax(Hn) ≤ 3, if n is suﬃciently large.

![image 434](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile434.png>)

Csaba [211] also proved this conjecture for dmax(Hn) = 4, and in [212] for bipartite Hn, (where Gn is not necessarily bipartite) and dmax(Hn) ≤ ∆.

Improving some results of Sauer and Spencer [729] and of Catlin, P. Hajnal and M. Szegedy [447] considered some bipartite packing problems where they proved an asymmetric version: for the ﬁrst graph they considered the maximum degree but for the second one only the average degree, thus improving the previous results for bipartite graphs.

The reader interested in more details will ﬁnd a lot of information, e.g., in the survey of Kierstead, Kostochka, and Yu [514].

- 7.4. Vertex-partitioning into monochromatic subgraphs of given type


This area has two parts: one about ordinary graphs and the second one about hypergraphs. The hypergraph results can be found in Subsection 9.8. Here we consider edge-colourings. Gerencs´er and Gy´arf´s [390] proved that the vertices of any 2-coloured Kn can be partitioned into the vertex sets of two monochromatic paths of distinct colours. Here we consider problems where the vertex set of an r-coloured graph has to be partitioned into the vertex sets Ui of some

given types of monochromatic subgraphs. We mention just a few such theorems, to give the ﬂavour of these results.

- Problem 7.15. Given a graph Gn and a family L of graphs. What is the minimum integer t for which every r-colouring of E(Gn) has a vertex partition

V (Gn) =

•

Ui into t vertex sets so that each G[Ui] contains a monochromatic spanning Hi ∈ L.122

Gy´arf´s, Sa´rk¨ozy, and Selkow [436] discussed a natural but much more general family of problems:

- Problem 7.16. Given a family L of graphs, (trees, connected subgraphs, matchings, cycles,...) and two integers, r ≥ s ≥ 1. At least how many vertices of an r-edge-coloured Kn can be covered by s monochromatic subgraphs Hi ∈ L in this Kn?123


The simplest case is r = 1, where we use only one colour. Another simple subcase is when we RED-BLUE-colour the edges of a Kn and study how many monochromatic cycles are needed (in the worst case) to cover the vertices. We can not always partition the edges into monochromatic cycles, unless we agree that the vertices and the edges are also regarded as cycles.124 In this case we can always partition E(Gn) into e(Gn) monochromatic “cycles”: real cycles, edges and vertices. The next part contains some repetition from Section 6, primarily from Subsection 6.5. We start with

Conjecture 7.17 (Gya´rf´s (1989), [424], proved). There exists an integer f(r) independent of n such that if E(Kn) is r-coloured, then V (Kn) can always be covered by f(r) vertex-disjoint monochromatic paths.

Actually, Gy´arf´s formulated three conjectures in [424]. In the ﬁrst one he wanted to cover V (Kn) by f(r) = r vertex-disjoint monochromatic paths, in the second, weaker one, the vertex-disjointness was not assumed, and the third, weakest one, was Conjecture 7.17. (f(r) = r would yield the ﬁrst conjecture.) Gy´arf´s proved the following weakening of his conjectures:

Theorem 7.18 (Gya´rf´s [424]). There exists an integer f(r) > 0 such that in any r-colouring of E(Kn) one can cover the vertices by f(r) monochromatic paths.

This result does not assert that the covering paths are vertex-disjoint. The proof of Gy´arf´s gave an explicit f(r) ≈ r4. This was improved by Erdo˝s, Gy´arf´s, and Pyber in Theorem 6.25: In any r-edge-colouring of Kn, one can cover V (Gn) by p(r) = O(r2 log r) vertex-disjoint monochromatic cycles. This was further improved by

![image 435](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile435.png>)

- 122More generally, we may ﬁx for each colour i a family Li and may try to cover V (Gn) by vertex disjoint subgraphs Hi ∈ Li.
- 123Formally we have here two problems, one when we r-colour E(Kn), the other when we r-colour E(Gn), however, the diﬀerence “disappears” if r is large. Further, we may also ask for the largest subgraph H ⊆ Kn that is coloured by at most t colours, which is diﬀerent from asking for the largest number of edges covered by t monochromatic Hi ∈ L.
- 124If for a ﬁxed x, all edges xy are Red, and the other edges are Blue, then we need this.


- Theorem 7.19 (Gya´rf´s-Ruszink´o-Sa´rk¨ozy-Szemer´edi [431]). If E(Kn) is rcoloured, then V (Kn) can be partitioned into O(r log r) vertex-sets of monochromatic cycles.


We have to point out two things. (a) While the problems with cycles and paths are basically of the same

diﬃculty in the Erdo˝s-Gallai theorems, here the problems on covering with cycles are much more diﬃcult.

(b) Covering with vertex-disjoint paths/cycles is signiﬁcantly more diﬃcult than the case when vertex-disjointness is not assumed.

Here the most important conjecture was

Conjecture 7.20 (Erd˝os, Gy´arf´s, and Pyber [291]). In Theorem 7.19 p(r) = r vertex-disjoint monochromatic cycles are enough.

This was proved for r = 2 by Bessy and Thomass´e (see Subsection 7.4) but “slightly disproved” for r ≥ 3 by Pokrovskiy [654], see Remark 6.8. A whole theory emerged around this conjecture, and below we provide a very short description of it, basically following Sa´rk¨ozy’s paper [725], which starts with a good “minisurvey” about this area. He extends the problem to covering by powers of cycles, (as Po´sa and Seymour extended Dirac’s Hamiltonicity theorem). Sa´rk¨ozy proved

- Theorem 7.21 (S´ark¨ozy (2017), [725]). For every integer k ≥ 1 there exists a

constant c(k) such that in any 2-colouring of E(Kn) at least n−c(k) vertices can be covered by 200k2 log k vertex-disjoint monochromatic kth powers of cycles.

The interested reader is referred to [725]. We shall return to the corresponding hypergraph problems in Section 9.8. We close this part with a result of Grinshpun and Sa´rk¨ozy [422] on a conjecture of Gy´arf´s where the cycles are replaced by an arbitrary ﬁxed family of bounded degree graphs. (This covers the case of the kth powers of cycles.)

Fix a degree bound ∆ and let F = {F1,F2,...} be any given family of graphs, where Fr is an r-vertex graph of maximum degree at most ∆.

- Theorem 7.22 (Grinshpun and Sa´rk¨ozy [422]). There exists an absolute constant C such that for any 2-colouring of E(Kn), there is a vertex partition of Kn into (vertex sets of) monochromatic copies of members of F with at most 2C∆ log ∆ parts.

If F consists of bipartite graphs then 2C∆ log ∆ can be replaced by 2c∆, which is best possible, apart from the value of the constant c:

- Theorem 7.23 (Grinshpun and Sa´rk¨ozy [422]). Let F be a family of bipartite graphs with maximum degree ∆. There is an absolute constant c such that for any 2-edge colouring of Kn, there is a vertex partition of Kn into (vertex sets of) monochromatic copies of Fr ∈ F with at most 2c∆ parts.


These results are strongly connected to some results of Conlon, Fox and Sudakov [196]. We close this section with an open problem. Problem 7.24. Do the Grinshpun-S´ark¨zy theorems extend to three colours?

#### 8. Hypergraph extremal problems, small excluded graphs

Until now we primarily concentrated on two Universes: graphs and integers. Here we include a short section on the Universe of hypergraphs. We used hypergraphs, e.g., in estimating independence numbers in Section 4.3 in “uncrowded graphs and hypergraphs”, to improve a Ramsey number estimate, R(3,k), to disprove the Heilbronn conjecture, see Subsection 4.7, and in case of the inﬁnite Sidon sequences, and several further results, in Subsections 4.3-4.11. The parts in Section 5.5 connected to the Removal Lemma were also in some sense hypergraph results. Here we “start again”, but go into other directions. We refer the readers interested in more details to the surveys of Sidorenko, [748], F¨uredi [369, 370], G.O.H. Katona [489], Keevash [498], of K¨uhn and Osthus [563], and of Ro¨dl and Ruci´nski [688].

Below, to emphasize that we consider hypergraphs, occasionally we shall use a diﬀerent typesetting, e.g., for r-uniform hypergraphs, for the excluded hypergraphs we may use L(r), instead of L, and L(r) for the family of excluded hypergraphs.

a

x2 x3

d

c x b

1

- Figure 9: Small excluded hypergraphs: Complete hypergraph, Fano hypergraph and the Octahedron hypergraph

We start with the case of “Small excluded subhypergraphs”. Here “small” means that the excluded hypergraphs have bounded number of vertices. In Section 9 we shall consider the case of 1-factors and the problem of ensuring Hamiltonian cycles and other “spanning” or “almost spanning” conﬁgurations. For the sake of simplicity, we mostly (but not always) restrict ourselves to 3uniform hypergraphs. The extremal number for r-uniform hypergraphs will be denoted

also by ex(n,L), or, to emphasise that we consider r-uniform hypergraphs, we may write exr(n,L), or exr(n,L(r)).125 There are many interesting results on hypergraph extremal problems. We mention the easy theorem of Katona, Nemetz and Simonovits [493], according to which exr(n,L)/ nr is monotone decreasing, non-negative, and therefore convergent.

- Figure 10: Three-partite 3-uniform hypergraph.


As for simple graphs, for hypergraphs we can also distinguish degenerate and non-degenerate extremal graph problems: an r-uniform problem is degenerate if exr(n,L) = o(nr). For graphs the K˝va´ri-So´s-Tur´an theorem was the key in this. A fairly simple result of Erdo˝s [266] generalizes the K˝va´ri-So´s-Tur´an theorem. Let Kr(r)(t1,t2,...,tr) denote the r-uniform hypergraph in which the vertex set V is parti-

![image 436](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile436.png>)

125Here we use L for an excluded graph, L for a hypergraph, and L for a family of graphs or hypergraphs.

tioned

into V1,...,Vr, |Vi| = ti, and the hyperedges are the “transversals”: r-tuples intersecting each Vi in one vertex.

- Theorem 8.1 (Erd˝os, (1964), [266]). If t = t1 ≤ t2 ≤ ... ≤ tr, then


r−1

exr(n,K(rr)(t,t2,...,tr)) = O(nr−1/t

). This implies, exactly as for r = 2, that

Corollary 8.2. exr(n,L(r)) = o(nr) if and only if there is an L ∈ L(r) of strong chromatic number r.126

- Remark 8.3. As in Corollary 2.12, if the problem is non-degenerate, then the “density constant jumps up”:


exr(n,L(r)) >

1 rr

+ o(1) nr. (8.1)

![image 437](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile437.png>)

A famous problem of Erdo˝s was whether for 3-uniform hypergraphs 1/27 is a “jumping constant”: does there exist a constant c > 0 such that if for some η > 0 exr(n,L(r)) > 27 1 + η + o(1) nr then exr(n,L(r)) > 27 1 + c + o(1) nr also holds. There are many related results, here we mention only the breakthrough paper of Frankl and Ro¨dl [356], which however, does not decide if 1/27 is a “jumping constant” or not. We mention that according to Pikhurko [648] there are continuum many limit densities and there are among them irrational ones even for ﬁnite families of excluded r-graphs. We also recommend to read Baber and Talbot [58] and several papers of Y. Peng, e.g., [644], in this area.

![image 438](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile438.png>)

![image 439](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile439.png>)

Tur´an’s conjecture

Consider now 3-uniform hypergraphs: H(3) = (V,E). To formulate the famous hypergraph conjectures of Paul Tur´an in the two simplest cases, we need two constructions. We shall call an r-uniform hypergraph h-partite if its vertices can be partitioned into h classes, none of which contains hyperedges.

(a) For the excluded 3-uniform complete 4-graph K(3)4 , consider the 3-uniform hypergraph H(3)n obtained by partitioning n vertices into 3 classes U1, U2 and U3 as equally as possible and taking the triples of form (x,y,z) where x,y, and z belong to diﬀerent classes, and the triplets (x,y,z) where x and y belong to Ui and z to Ui+1, for i = 1,2,3, where U4 := U1, see Figure 11. Tur´an conjectured that this is the extremal hypergraph for K(3)4 . This is unknown, we do not know even if this is asymptotically sharp.

Figure 11: K(3)4 extremal?

![image 440](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile440.png>)

126The strong chromatic number χS(F(r)) of F(r) is the minimum ℓ for which the vertices of F(r) can be ℓ-coloured so that each hyperedge gets r distinct colours. Our condition is equivalent with that some F(r) ∈ L(r) is a subgraph of K(rr)(a, . . . , a) for some large a.

Actually, ﬁrst Katona, Nemetz, and Simonovits [493] gave examples (for n = 3m + 1) showing that if Tur´an’s conjecture holds, then the uniqueness of extremal graphs does not always hold.

A more general construction of Brown [151], generalized by Kostochka [548], shows that if the conjecture holds, then there are many-many extremal graph structures for the extremal hypergraph problem of K(3)4 and n = 3t. For a slightly more detailed description of this see e.g. Fon-der-Flaass [346], Razborov, [671], Simonovits [763].

(b) For the excluded complete 5-graph K(3)5 Tur´an had a construction – for the potential extremal hypergraph – with four classes and another one with two classes. The one with two classes is simple, see Figure 12. It is a complete bipartite hypergraph: we partition the vertices into A and B and consider all the triples intersecting both classes. V.T. So´s observed that the construction with two classes can be obtained from the construction with four classes by moving around some triples in some simple way. Probably J.

Figure 12: K(3)5 extremal?

Sur´nyi found a construction showing that Tur´an’s conjecture for K(3)5 is false for n = 9. Kostochka (perhaps) generalized this, founding counterexamples for every n = 4k + 1.127 Still Tur´an’s conjecture may be sharp, or, at least, asymptotically sharp.128

Among the new achievements we mention Razborov’s Flag Algebra method and his results on hypergraphs [668, 670, 671].

A simple hypergraph extremal problem

As we have often emphasized, to solve a hypergraph extremal problem is mostly hopeless, despite that recently many nice results were proved on hypergraphs. Keevash described this situation by writing (in MathSciNet, on [379], in 2008):

“An important task in extremal combinatorics is to develop a theory of Tur´an problems for hypergraphs. At present there are very few known results, so it is interesting to see a new example that can be solved.”

Consider 3-uniform hypergraphs. The diﬃculties are reﬂected, among oth-

ers, by that we do not know the extremal graph for L(3)4,3, i.e. when we exclude the 4-vertex hypergraph with 3 triples.129 The next question is among the easier ones. G.O.H. Katona asked and Bollob´s solved the following extremal problem.

![image 441](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile441.png>)

127These constructions seem to be forgotten, “lost” and are not that important. 128Since for hypergraphs we have at least two popular chromatic numbers, therefore the

expression r-uniform ℓ-partite may have at least two meanings in the related literature. 129Generally, L(k,ℓr) is the family of r-uniform hypergraphs of k vertices and ℓ hyperedges.

As we have mentioned, the problem of ex(n, L(k,ℓr)) was considered in two papers of Brown, Erd˝s, and S´os [154, 155] and turned out to be very important in this ﬁeld. Originally Erd˝s

conjectured a relatively simple asymptotic extremal structure, for L(3)4,3 but his conjecture was devastated by a better construction of Frankl and Fu¨redi [355]. This construction made this problem rather hopeless.

- Theorem 8.4 (Bolloba´s (1974), [116]). If a 3-graph has 3n vertices and n3 + 1 triples, then there are two triples whose symmetric diﬀerence is contained in a third one.


K(3)3 (n,n,n) – which generalizes T2n,2, to 3-uniform hypergraphs,– shows the sharpness of Theorem 8.4. So Theorem 8.4 is a natural generalization of Tur´an’s theorem: an ordinary triangle-free graph Gn is just a graph where no edge of Gn contains the symmetric diﬀerence of two other edges. So the excluded hypergraph can be viewed as a hypergraph-triangle. Bollob´s generalized Katona’s conjecture to r-uniform hypergraphs. The generalized conjecture was proved for r = 4 by Sidorenko [743], for r = 5,6 by Norin and Yepremyan [634]. For related results see e.g. Sidorenko [743], Mubayi and Pikhurko [625], Pikhurko [646].

The Fano hypergraph extremal problem

Here the excluded graph is the 3-uniform Fano hypergraph F(3)7 on 7 vertices, with seven hyperedges any two of which intersect in exactly one vertex, see Figure 13: F(3)7 is the simplest ﬁnite geometry. The nice thing about the extremal problem of F(3)7 is that it is natural, non-trivial, but has a nice solution.

Figure 13: Fano

Conjecture 8.5 (V. T. So´s). Partition n vertices into two classes A and B with ||A|−|B|| ≤ 1 and take all the triples in-

tersecting both A and B. The obtained 3-uniform complete bipartite hypergraph H[A,B] is extremal for F(3)7 (if n is suﬃciently large).

Using some multigraph extremal results of K¨undgen and F¨uredi [378], ﬁrst de Caen and F¨uredi proved

- Theorem 8.6 (de Caen and F¨uredi (2000), [172]).


3 4

ex(n,F(3)7 ) =

![image 442](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile442.png>)

n 3

+ O(n2).

Next, applying the stability method, the sharp result was obtained, independently, by F¨uredi and Simonovits and by Keevash and Sudakov. Since χ(F(3)7 ) = 3, a 3-uniform bipartite hypergraph cannot contain F(3)7 .

- Theorem 8.7 (F¨uredi-Simonovits (2005), [385]/Keevash-Sudakov [504]). If H(3)n


is a triple system on n > n1 vertices not containing F(3)7 and of maximum number of hyperedges under this condition, then H(3)n is bipartite: χ(H(3)n ) = 2.

Theorem 8.7 implies that

ex3(n,F(3)7 ) =

n 3 −

⌊n/2⌋ 3 −

⌈n/2⌉ 3

.

There are two important ingredients of the proof. The ﬁrst one is a multigraph extremal theorem:

- Theorem 8.8 (F¨uredi-K¨undgen [378]). If Mn is an arbitrary multigraph (without restriction on the edge multiplicities, except that they are non-negative) and each 4-vertex subgraph of Mn has at most 20 edges (with multiplicity), then

e(Mn) ≤ 3

n 2

+ O(n).

The other ingredient of the proof of Theorem 8.7 was that it is enough to prove the theorem for those hypergraphs where the low-degree vertices are deleted, and it is enough to prove a corresponding stability theorem.

- Theorem 8.9. There exist a γ2 > 0 and an n2 such that if F(3)7  ⊆ H(3)n and

deg(x) >

3 4 − γ2

![image 443](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile443.png>)

n 2

for each x ∈ V (H(3)n ),

then H(3)n is bipartite.

Recently L. Bellmann and C. Reiher [98] proved that Theorem 8.7 holds for any n ≥ 7. One could ask, what is the essence of their proof. Often when we use stability arguments for extremal problems, one thinks that perhaps induction would also work. Unfortunately, for hypergraphs this mostly breaks down. As an exception, Bellmann and Reiher have found the good way to use here induction. (A similar situation was when the Lehel Conjecture was proved by Bessy and Thomass´e [108], yet for hypergraphs we do not know of such cases.)

— · —

F¨uredi, Pikhurko, and Simonovits used the stability method also in [381], to prove a conjecture of Mubayi and Ro¨dl. For further related results see, e.g., Keevash [494], F¨uredi, Pikhurko, and Simonovits [381, 382], ...and many similar cases.

— · We should mention here a beautiful result of Person and Schacht:

- Theorem 8.10 (Person and Schacht (2009), [645]). Almost all Fano-free 3uniform hypergraphs are bipartite.


Remark 8.11. (a) One could ask what is the connection between Theorems 8.7 and 8.10. Here one should be careful, e.g., Pr¨mel and Steger [664] proved that almost all Berge graphs are perfect, which means that for most graphs the Berge Strong Perfect Graph Conjecture is true. This was a beautiful result, however, the actual proof of the Perfect Graph Conjecture [179] (which came much later) was much more diﬃcult.

- (b) Several similar results are known, where the typical structure of F-free

graphs are nicely described. For graphs this was discussed in Subsection 2.13. Several related results were also proved for hypergraphs, e.g., Lefmann, [572]

- (c) Some further related results can be found in the papers of Cioab˘a [191],


Keevash [494], Balogh-Morris-Samotij-Warnke [79], or Balogh and Mubayi [81], and in many further cases.

- 8.1. Codegree conditions in the Fano case


As we have already discussed, as soon as we move to hypergraphs, many notions, e.g., the notion of path, cycles and of degrees also can be deﬁned in several diﬀerent ways. Restricting ourselves to the simplest case of 3-uniform hypergraphs, let δ2(x,y) be the number of vertices z for which (x,y,z) is a hyperedge, and δ2(H(3)n ) = minδ2(x,y). Usually δ2(x,y) is called the codegree of x and y. Often it is more natural to have conditions on the minimum codegree than on the min-degree.

- Theorem 8.12 (Mubayi [622]). For any α > 0, there exists an n0(α) for which, if n > n0 and δ2(H(3)n ) ≥ (21 + α)n, then H(3)n contains the Fano plane F(3)7 .

![image 444](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile444.png>)

The sharpness comes from the complete bipartite 3-uniform hypergraph.

Mubayi conjectured that, for large n, (12 + α) can be replaced by 12. This was proved ﬁrst by Keevash, and then, in a simpler way, by DeBiasio and Jiang:

![image 445](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile445.png>)

![image 446](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile446.png>)

- Theorem 8.13 (Keevash [496]/DeBiasio and Jiang [231]). There is an n0 such that if n > n0 and δ2(H(3)n ) > ⌊21n⌋ then H(3)n contains F(3)7 .


![image 447](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile447.png>)

Actually, there are more and more extremal results where we derive the existence of some substructure by knowing that the minimum codegree is high. Later we shall see several further such examples, e.g., in Section 9: to ensure a tight Hamiltonian cycle,130 Theorem 9.12 will use the minimum vertex-degree, while Theorem 9.13 uses that the minimum codegree is large.

Remark 8.14. (a) DeBiasio and Jiang gave a fairly elementary proof, not using the Regularity Method. They had to assume that n is suﬃciently large only to use some supersaturation argument.

- (b) In their paper DeBiasio and Jiang [231] start with a nice introduction

and historical description of the situation.

- (c) Both the Keevash paper and the DeBiasio-Jiang paper go beyond just


proving the above formulated extremal result.

- 9. Large excluded hypergraphs


While for ordinary graphs the deﬁnition of cycles is very natural, for hypergraphs there are several distinct ways to deﬁne them, leading to completely diﬀerent

![image 448](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile448.png>)

130deﬁned after Deﬁnition 9.2.

problems and results. Below mostly we shall restrict ourselves to 3-uniform hypergraphs, within that to Loose (also called Linear) and Tight cycles, and we mostly skip Berge cycles.131 The reader interested in more details about Berge cycles is referred to Gy´arf´s, Sa´rk¨ozy, and Szemer´edi [440, 433] and also to the excellent surveys of Ro¨dl and Ruci´nski [688], K¨uhn and Osthus [565].

We start this section with a short subsection on Hypergraph cycle Ramsey problems which could be regarded as medium range extremal problems, since we get in a hypergraph on N vertices a (monochromatic) subgraph of (1 − c)N vertices. Then we shall consider hypergraph extremal problems where the excluded conﬁguration is a spanning subhypergraph, or at least an almost spanning one. To make the life of the reader (interested in more details) easier, we follow the deﬁnitions and notation of [688], as much as we could.

9.1. Hypergraph cycles and Ramsey theorems

We shall need the deﬁnition of the so called (k,ℓ)-cycles, covering the matchings, the loose cycles and the tight cycles.

- Definition 9.1 (Tight/loose cycles). Consider 3-uniform hypergraphs. Let

E1,...,Eℓ be a cyclically arranged family of triples. If the consecutive ones intersect in 2 vertices, and there are no other intersections among them, then

this conﬁguration Cℓ3 will be called a Tight ℓ-cycle. If the consecutive ones intersect in 1 vertex, and there are no other intersections among them, then

this conﬁguration Cℓ3 will be called a Loose ℓ-cycle.

2

5 3

6

| | |
|---|---|
| | |


4

1

(a) Tight cycle (b) Loose cycle (c) Berge cycle

Figure 14: Various hypergraph cycles We could have started with the more general

- Definition 9.2 ((k,ℓ)-cycle). Fix some 0 ≤ ℓ ≤ k − 1. In a k-uniform hy-


pergraph H(nk) the cyclically ordered vertices a1,...,at and the hyperedges E1,...,Et form a (k,ℓ)-cycle, if the vertices of Ei are cyclically consecutive (form a segment), and |Ei ∩ Ei+1| = ℓ, for i = 1,...,t. (Here Et+1 := E1).

If ℓ = 1, that we call a loose cycle, (or linear cycle) and if ℓ = k − 1 that is the tight cycle.

![image 449](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile449.png>)

131Hamiltonicity for Berge cycles were discussed by Bermond, Germa, Heydemann, and Sotteau [104]. Perhaps the ﬁrst Tight Hamiltonicity was discussed in [492], however, the tight Hamilton cycles were called there as Hamilton chains.

For ℓ = 0, this reduces to a matching: a family of t/k independent edges. Divisibility. Mostly we have some hidden divisibility conditions, e.g., speaking of a (k,ℓ)-cycle Cmk,ℓ on m vertices, we assume that m is divisible by k − ℓ.

— · —

It was known from the beginning that the (ordinary) Ramsey number for cycles strongly depends of the parity: R(Cn,Cn) = 23n − 1 if n is even and R(Cn,Cn) = 2n − 1 if n is odd (Bondy [135], Faudree and Schelp [332], Vera Rosta [676]). So it is not too surprising that for hypergraphs the parity also strongly inﬂuences the results. (Analogous results are known for ordinary graphs and 3 or more colours, e.g., as we have mentioned, R(n,n,n) = 4n − 3 for odd n > n0, see  Luczak, [600], Kohayakawa, Simonovits, and Skokan [530], but it is 2n + o(n) if n is even, see Figaj and  Luczak [341, 342].)132 For hypergraphs the situation is even more involved, since the Ramsey numbers depend on the types of cycles we consider (loose, tight, Berge). Haxell,  Luczak, Peng, Ro¨dl, Ruci´nski, Simonovits, and Skokan proved the following

![image 450](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile450.png>)

- Theorem 9.3 ((2006), [458]). Consider 3-uniform hypergraphs. If Cn3 denote the loose n-vertex hypergraph cycle, then R(Cn3,Cn3,Cn3) = 5n/4 + o(n).


Here the upper bound is the diﬃcult part: an easy construction shows that R(Cn3,Cn3,Cn3) > 5n/4−c, for an appropriate constant c > 0. This was generalized from 3-uniform to k–uniform graphs and loose cycles by Gy´arf´s, Sa´rk¨ozy, and Szemer´edi [437]. As to the tight cycles, Haxell,  Luczak, Peng, R¨odl, Ruci´nski, and Skokan proved the following

- Theorem 9.4 ((2006), [459]). Consider 3-uniform hypergraphs. If Cn3 denotes


the tight n-vertex hypergraph cycle, then R( Cn3, Cn3, Cn3) = 4n/3 + o(n) when n is divisible by 3, and ≈ 2n otherwise.

On Ramsey numbers for Berge cycles see the papers of Gy´arf´s, Sa´rk¨ozy, and Szemer´edi [439], and Gy´arf´s and Sa´rk¨ozy [433], or Gy´arf´as, Lehel, G. Sa´rk¨ozy, and Schelp [430].

- 9.2. Hamilton cycles


This research area has two roots:

(A) For simple graphs the extremal graph problem of k independent edges goes back to Erdo˝s and Gallai [289]. It may be surprising, but to ensure k independent edges, or a path P2k requires basically the same degree condition. On the other hand, maybe it is not so surprising. Ro¨dl and Ruci´nski [688] write: “...for ℓ = 0 a Hamiltonian ℓ-cycle in a k-graph H becomes a perfect matching in H. Moreover, any Hamiltonian (k − ℓ)-cycle contains a matching of size ⌊n/k⌋. Hence, not surprisingly, the results for Hamiltonian cycles and

![image 451](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile451.png>)

132The breakthrough result of  Luczak [600] was improved by Kohayakawa, Simonovits, and Skokan [530] and generalized by Jenssen and Skokan [479], see also Gya´rf´s, Ruszinko´, S´ark¨zy and Szemer´edi [432] and Benevides and Skokan [99] and others.

perfect (or almost perfect) matchings are related.” The Erdo˝s-Gallai results were extended to hypergraphs, by Erdo˝s [268]. Bollob´s, Daykin, and Erdo˝s [122] ensured t independent hyperedges, Daykin and Ha¨ggkvist [229] guaranteed a perfect matching.

(B) Katona and Kierstead [492] deﬁned the tight Hamilton cycle and tried to generalize Dirac’s theorem to hypergraphs.

The area described in the next few subsections in a fairly concise way is described in much more details, e.g., in the excellent surveys of K¨uhn and Osthus [563] and of Ro¨dl and Ruci´nski [688], in the Introduction of the paper of Alon, Frankl, Huang, Ro¨dl, Ruci´nski, and Sudakov [35], and in the survey of Yi Zhao [824].

The beginnings: Hamiltonicity

Since hypergraph problems seemed mostly too technical even for combinatorists working outside of hypergraph extremal problems, the research on hypergraph Hamiltonicity started relatively late, with a paper of G.Y. Katona and Kierstead [492].133 For k-uniform hypergraphs, for a subset S ⊆ V (H(nk)) with ℓ := |S| we deﬁne the ℓ-degree δℓ(S) as the number of k-edges of H(nk) containing S and δℓ(H(nk)) is the minimum of δℓ(S) for the ℓ-tuples S ⊆ V (H(nk)). G.Y. Katona and Kierstead considered the tight cycles134 and paths and proved

Theorem 9.5 (G.Y. Katona, H. Kierstead (1999), [492]). If H(nk) = (V,E) is a k-uniform hypergraph and

- 1

![image 452](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile452.png>)

- 2k


δk−1(H(nk)) ≥ 1 −

5 2k

n + 4 − k −

,

![image 453](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile453.png>)

then it contains a tight Hamiltonian cycle Cnk. This is far from being sharp:

Conjecture 9.6 (G.Y. Katona, H. Kierstead [492]). If δk−1(H(nk)) > n−2k+3 , then H(nk) has a tight Hamilton cycle.

![image 454](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile454.png>)

Katona and Kierstead also provided the construction supporting this:

Theorem 9.7 (Katona and Kierstead [492]). For any integers k ≥ 2 and n > k2 there exists a k-uniform hypergraph H(nk) without tight Hamilton cycles for which δk−1(H(nk)) = n−2k+3 .

![image 455](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile455.png>)

Ro¨dl and Ruci´nski write in [688]:

“In 1952 Dirac [242] proved a celebrated theorem. . . In 1999, Katona and Kierstead initiated a new stream of research to studying similar questions for hypergraphs, and subsequently, for perfect matchings. . . ”

![image 456](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile456.png>)

- 133For Berge cycle Hamiltonicity there were earlier results, e.g., by Bermond, Germa, Heydemann, and Sotteau [104].
- 134They called it chain.


- 9.3. Problems: Hypergraph Hamiltonicity


We restrict our attention primarily to 3-uniform hypergraphs. As Ro¨dl, Ruci´nski, Schacht, and Szemer´edi [691] describe, here there are (at least) six diﬀerent questions:

- (i) how large vertex-degree ensures a tight Hamiltonian cycle,
- (ii) how large vertex-degree ensures a loose Hamiltonian cycle,
- (iii) how large co-degree ensures a tight Hamiltonian cycle,
- (iv) how large co-degree ensures a loose Hamiltonian cycle, (v-vi) and how large degrees/co-degrees ensure a perfect matching or an


almost perfect matching? In all these problems some divisibility questions should also be handled.

The goal. As a ﬁrst step, we would say that most of the research in this area is related to describing two functions deﬁned for k-uniform n-vertex graphs, the thresholds for the Hamiltonicity, hℓd(k,n), and for the Matching, mrd(k,n):

What is the minimum integer t for which, if the d-degree δd(H(nk)) ≥ t in a kuniform hypergraph H(nk), then H(nk) contains

- (i) a Hamilton ℓ-cycle Cnk,ℓ
- (ii) an almost-matching Mk,rn , leaving out at most r vertices,


respectively.

Before going into details, we formulate two typical theorems, for 3-uniform hypergraphs, for Tight cycles.

- Theorem 9.8 (Reiher, Ro¨dl, Ruci´nski, Schacht, and Szemer´edi (2016), [673]). For any η > 0, there exists an n0(η) such that if n > n0 and in an n-vertex 3-uniform hypergraph H(3)n the minimum degree


dmin(H(3)n ) ≥

5 9

+ η

![image 457](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile457.png>)

n 2

,

then it contains a tight Hamiltonian cycle. The estimate (59+o(1)) n2 is sharp. The codegree problem is answered by

![image 458](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile458.png>)

Theorem B (Rodl,¨ Rucinski,´ and Szemer´edi (2011), [696]). There exists an n0 such that if n > n0 and in a 3-uniform hypergraph H(3)n , for any x = y,

δ2(x,y) ≥

n 2

![image 459](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile459.png>)

,

then H(3)n contains a tight Hamiltonian cycle. This is sharp: for any n > 4, there exists a 3-uniform hypergraph with δ2(H(3)n ) = n2 −1, without containing a tight Hamiltonian cycle.

![image 460](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile460.png>)

Table 2 contains some of the results, discussed below, and some others.

![image 461](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile461.png>)

![image 462](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile462.png>)

![image 463](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile463.png>)

![image 464](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile464.png>)

![image 465](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile465.png>)

![image 466](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile466.png>)

![image 467](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile467.png>)

Authors Year About what? Methods Journal H`an, Schacht 2010 Dirac, loose Hamilton cycles Absorb. [450] Ro¨dl, Ruci´nski 2010 Dirac type questions, Survey [688] Ro¨dl, Ruci´nski, 2011 Dirac 3-hyper, approx Advances Szemer´edi [696] Glebov-Person-Weps 2012 Hypergraph Hamiltonicity ????. [394] Czygrinow-Molla 2014 Loose Hamilton 3-unif Absorb. SIDMA

![image 468](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile468.png>)

![image 469](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile469.png>)

![image 470](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile470.png>)

![image 471](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile471.png>)

![image 472](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile472.png>)

![image 473](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile473.png>)

![image 474](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile474.png>)

![image 475](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile475.png>)

![image 476](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile476.png>)

![image 477](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile477.png>)

![image 478](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile478.png>)

![image 479](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile479.png>)

![image 480](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile480.png>)

![image 481](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile481.png>)

![image 482](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile482.png>)

![image 483](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile483.png>)

![image 484](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile484.png>)

![image 485](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile485.png>)

![image 486](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile486.png>)

![image 487](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile487.png>)

![image 488](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile488.png>)

![image 489](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile489.png>)

![image 490](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile490.png>)

![image 491](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile491.png>)

![image 492](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile492.png>)

![image 493](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile493.png>)

![image 494](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile494.png>)

![image 495](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile495.png>)

![image 496](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile496.png>)

![image 497](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile497.png>)

![image 498](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile498.png>)

![image 499](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile499.png>)

![image 500](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile500.png>)

![image 501](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile501.png>)

![image 502](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile502.png>)

![image 503](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile503.png>)

![image 504](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile504.png>)

![image 505](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile505.png>)

![image 506](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile506.png>)

![image 507](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile507.png>)

![image 508](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile508.png>)

![image 509](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile509.png>)

![image 510](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile510.png>)

![image 511](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile511.png>)

![image 512](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile512.png>)

![image 513](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile513.png>)

![image 514](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile514.png>)

![image 515](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile515.png>)

codegree, perfect matching Stabil. [224] *

![image 516](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile516.png>)

![image 517](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile517.png>)

![image 518](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile518.png>)

![image 519](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile519.png>)

![image 520](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile520.png>)

![image 521](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile521.png>)

![image 522](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile522.png>)

Czygrinow, 2014 Tiling with K4(3) − 2e Absorb. JGT, DeBiasio, Nagle [221]

![image 523](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile523.png>)

![image 524](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile524.png>)

![image 525](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile525.png>)

![image 526](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile526.png>)

![image 527](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile527.png>)

![image 528](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile528.png>)

![image 529](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile529.png>)

![image 530](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile530.png>)

![image 531](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile531.png>)

![image 532](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile532.png>)

![image 533](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile533.png>)

![image 534](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile534.png>)

![image 535](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile535.png>)

Jie Han, Yi Zhao 2015 Minimum codeg threshold Absorb. [451] Lo, Allan, 2015 F-factors in hypergraphs via Absorb. GC Markstr¨om Absorb. [579] Reiher-R¨odl-Ruci´n- 2016 Tight Hamiltonian 3-hyper Absorb. SIDMA ski-Schacht-Szem Absorb. [673] Ferber, Nenadov, Universality of Random Absorb. RSA Peter graphs Absorb. [340] Ro¨dl, Ruci´nski, 2017 Hamiltonicity of triple Annales Schacht, systems Comb Szemer´edi [691]

![image 536](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile536.png>)

![image 537](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile537.png>)

![image 538](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile538.png>)

![image 539](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile539.png>)

![image 540](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile540.png>)

![image 541](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile541.png>)

![image 542](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile542.png>)

![image 543](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile543.png>)

![image 544](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile544.png>)

![image 545](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile545.png>)

![image 546](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile546.png>)

![image 547](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile547.png>)

![image 548](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile548.png>)

![image 549](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile549.png>)

![image 550](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile550.png>)

![image 551](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile551.png>)

![image 552](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile552.png>)

![image 553](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile553.png>)

![image 554](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile554.png>)

![image 555](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile555.png>)

![image 556](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile556.png>)

![image 557](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile557.png>)

![image 558](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile558.png>)

![image 559](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile559.png>)

![image 560](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile560.png>)

![image 561](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile561.png>)

![image 562](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile562.png>)

![image 563](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile563.png>)

![image 564](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile564.png>)

![image 565](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile565.png>)

![image 566](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile566.png>)

![image 567](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile567.png>)

![image 568](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile568.png>)

![image 569](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile569.png>)

![image 570](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile570.png>)

![image 571](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile571.png>)

![image 572](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile572.png>)

![image 573](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile573.png>)

![image 574](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile574.png>)

![image 575](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile575.png>)

![image 576](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile576.png>)

![image 577](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile577.png>)

![image 578](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile578.png>)

![image 579](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile579.png>)

![image 580](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile580.png>)

![image 581](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile581.png>)

![image 582](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile582.png>)

![image 583](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile583.png>)

![image 584](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile584.png>)

![image 585](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile585.png>)

![image 586](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile586.png>)

![image 587](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile587.png>)

![image 588](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile588.png>)

![image 589](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile589.png>)

![image 590](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile590.png>)

![image 591](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile591.png>)

![image 592](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile592.png>)

![image 593](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile593.png>)

![image 594](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile594.png>)

Table 2: Using the absorption method (explained in Subsection 6.5), now for hypergraph Hamiltonicity

9.4. Lower bounds, constructions

In all cases considered here we have some relatively simple constructions providing a hypergraph not containing the required conﬁguration and having large minimum degree (of a given type). The proofs of that “the constructed hypergraphs do not contain the excluded conﬁgurations” mostly follow from a Pigeon Hole principle argument or from some parity arguments. A new feature is (compared to ordinary non-degenerate extremal graph problems) that here the results and constructions often depend on parities, divisibilities, and they may be more complicated.

We start with some constructions, conjectured extremal structures (see e.g. Figure 15). In the corresponding papers/proofs it turns out that these are indeed, (almost) extremal constructions. They can be found, e.g., in Han, Person, Schacht, [449], or earlier, in Daykin and Ha¨ggkvist [229], K¨uhn and Osthus [561], Ro¨dl, Ruci´nski and Szemer´edi [692], and Pikhurko [647].

Construction 9.9. Assume that n is divisible by k and 0 ≤ t < k. Let H(nk) have two vertex classes A and B, |A| = nk −1, |B| = k−k1n+1, and the hyperedges be all the k-tuples intersecting A. This hypergraph has no perfect matchings.

![image 595](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile595.png>)

![image 596](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile596.png>)

Further,

k−t n k − t

k − 1 k

+ o(nk−t). (9.1)

δt(H(nk)) = 1 −

![image 597](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile597.png>)

Construction 9.10. Assume that n is divisible by k and 0 ≤ t < k. Let Hn(k) have two vertex classes A and B, |A| be the maximum odd integer ≤ n/2, |B| = n−|A|, and the hyperedges be all the k-tuples intersecting A in a positive even number of vertices. This hypergraph has no perfect matchings. Further,

n k − t

- 1

![image 598](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile598.png>)

- 2


+ O(nk−t−1). (9.2)

δt( H(nk)) =

These constructions provide the lower bounds in many results in this area. Thus, e.g., for k = 3 the obtained coeﬃcients of k n−t are 59 for mindegree and

![image 599](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile599.png>)

- 1

![image 600](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile600.png>)

- 2 for codegree, respectively, which will turn out to be sharp in Theorems 9.11,


- 9.12 and 9.13 below.135


- 9.5. Upper bounds, asymptotic and sharp


Most of the above questions ﬁrst were solved only in asymptotic forms, then in sharp forms. But, as it is remarked in [691], one of these problems, namely Theorem 9.12 below, the ﬁrst one, (i), in the above list, is more diﬃcult than the others. There, even the asymptotic result (i.e. to prove ≈ 59

n 2 + o(n2)

![image 601](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile601.png>)

“needed” four steps: ﬁrst Glebov, Person and Weps improved the trivial n−21 to (1−ε) n−21 , then Ro¨dl and Ruci´nski [689] improved (1−ε) to 31(5−

√5) ≈ 0.91, next Ro¨dl, Ruci´nski, and Szemer´edi [694] to 0.8, and only then, they with Reiher and Schacht, obtained the sharp 5/9 = 0.555, in [673].

![image 602](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile602.png>)

![image 603](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile603.png>)

— · Below we write about this theory, staying mostly with the simplest cases. For

k = 3 the above codegree threshold is n2 in (9.2). One could ask, what is the appropriate degree condition. Cooley and Mycroft [204], using an appropriate

![image 604](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile604.png>)

Regularity Lemma of Allen, B¨ottcher, Cooley, and Mycroft [15], proved

- Theorem 9.11 (Cooley and Mycroft (2017), [204]). For any η > 0 there exists an n0(η) such that if n > n0(η), then any 3-uniform hypergraph H(3)n with dmin(H(3n)) ≥ (95 + η) n2 contains a tight cycle Cm3 with n − m = o(n).

![image 605](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile605.png>)

In other words, H(3)n contains an almost-Hamiltonian cycle: only o(n) vertices

are left out. The constant 59 is asymptotically best possible. Reiher, Ro¨dl, Ruci´nski, Schacht, and Szemer´edi improved Theorem 9.11:

![image 606](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile606.png>)

- Theorem 9.12 ((2016), [673]). For any η > 0, there exists an n0(η) such that if n > n0 and in an n-vertex 3-uniform hypergraph H(3)n the minimum degree


dmin(H(3)n ) ≥

![image 607](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile607.png>)

135identical with Theorems A,B, above.

5 9

+ η

![image 608](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile608.png>)

n 2

,

then it contains a tight Hamiltonian cycle.

The sharpness follows from the sharpness of Theorem 9.11. Actually, [673] describes three constructions proving the sharpness of Theorem 9.12. The difference between Theorems 9.11 and 9.12 is that Theorem 9.12 has no left-out vertices. The proof of Theorem 9.12 uses the hypergraph regularity and then the “absorption” method, to pick up the last few vertices.136

As to the codegree, we have

Theorem 9.13 (R¨odl, Ruci´nski, and Szemer´edi [696]). There exists an n0 such that if n > n0 and in a 3-uniform hypergraph H(3)n , for any x = y,

δ2(x,y) ≥

n 2

![image 609](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile609.png>)

,

then H(3)n contains a tight Hamiltonian cycle. This is sharp: for any n > 4, there exists a 3-uniform hypergraph with δ2(H(3)n ) = n2 −1, without containing a tight Hamiltonian cycle.

![image 610](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile610.png>)

The sharpness follows from the constructions of Subsection 9.4. A similar result holds for Hamiltonian paths.

Matchings

We deﬁne a perfect matching in a k-uniform hypergraph H on n vertices as a set of ⌊n/k⌋ disjoint hyperedges. To ensure a 1-factor in hypergraphs is a fascinating and important topic and would deserve a much longer survey. Here we again restrict ourselves to just a few related results and references. First we formulate two results on the degree-extremal problem of a 1-factor, for 3-uniform and 4-uniform hypergraphs. Both results are sharp. The following theorem was obtained independently, by Lo and Markstr¨om [579], K¨uhn, Osthus, and Treglown and by Imdadullah Khan:

Figure 15: Extremal structures for 4-uniform graphs and perfect matching in [222]: (a) 4-tuples intersecting both classes in 2 vertices, (b) 4-tuples intersecting one of the classes in 1 vertex.

![image 611](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile611.png>)

136This, with a sketch of the proof, is nicely explained by Ro¨dl and Rucin´ski, in [688]. The introduction of [673] and a survey of Yi Zhao [824] are also good descriptions of the otherwise fairly complicated situation.

- Theorem 9.14 (K¨uhn, Osthus, and Treglown [566] / I. Khan [507]). There is an n0 such that if n > n0 is divisible by 3 and in a 3-uniform hypergraph H(3)n

dmin(H(3)n ) >

n − 1 2 −

2n/3 2

+ 1 ≈

5 9

![image 612](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile612.png>)

n − 1 2

, (9.3)

- then H(3)n contains a 1-factor. Observe that the LHS of (9.3) is ≈ 95

![image 613](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile613.png>)

n 2 , i.e. the same what we need for

a tight Hamilton cycle. Khan also proved the analog theorem for 4-uniform hypergraphs:

Theorem 9.15 (Imdadullah Khan [508]). There exists a threshold n0 such that if n > n0 is divisible by 4 and in a 4-uniform hypergraph H(4)n

dmin(H(4)n ) >

n − 1 3 −

3n/4 3

+ 1,

- then H(4)n contains a 1-factor.




For related results see also Pikhurko [647], Han, Person, and Schacht [449], Czygrinow and Kamat [222] providing sharp results and describing the earlier asymptotic results, and Alon, Frankl, Huang, Ro¨dl, Ruci´nski, and Sudakov [35].

Upper bounds and the Absorbing method

In the proofs of the results discussed in this section one often uses the Absorbing Method, – described in Section 6.5, – to ensure spanning or almostspanning substructures, where Almost-Spanning means a subhypergraph covering the whole hypergraph with the exception of at most O(1) (or, occasionally, o(n)) vertices. As we wrote, in most cases considered in these subsections we have a simple, nice conjectured extremal structure, enabling us to use stability arguments. Yet, the actual “upper bounds” (non-construction parts) are fairly complicated.

In Section 9.3 we wrote about the thresholds for the Hamiltonicity, hℓd(k,n), and for the Matching, mrd(k,n). We have mentioned that sometimes we get the same results for Hamiltonicity and Perfect Matching.

Conjecture 9.16 (Informal/Formal [688]). The d-degree threshold δd(H(nk)) for the Hamiltonian problem and the Matching problem are roughy the same. More formally, hd(k,n) ≈ md(k,n), if d,k are ﬁxed, n → ∞.

There are many related results but we skip them, mentioning only that, as it is emphasized in [688], not only these two quatities are often near to each other, but in several cases they are proved to be equal, see e.g. Theorem 3.1 of [688], quoted from [695].

Theorem 9.17 (Han, Person, and Schacht (2009), [449]). For any γ > 0, if δ1(H(3)n ) ≥ (59 + γ) n2 and n > n0(γ), then H(3)n contains a 1-factor.

![image 614](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile614.png>)

There is a surprising, sharp diﬀerence between the cases when n is divisible by k and when it is not. Consider the simplest hypergraph case, k = 3.

Theorem 9.18. For any γ > 0, if δ2(H(nk)) ≥ (21 + γ) n2 and n > n0(γ), then H(nk) contains a Tight Hamiltonian cycle. 137 If n is not divisible by 3 and H(3)n does not contain a 1-factor, then δ2(H(3)n ) ≤ nk + o(n).

![image 615](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile615.png>)

![image 616](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile616.png>)

So in case of non-divisibility, much smaller degrees ensure a perfect matching.

— · —

One of the ﬁrst results where the Absorbing Lemma was used is the theorem of Ro¨dl, Ruci´nski, and Szemer´edi [695], on ensuring a perfect matching in a k-uniform hypergraph. As we have mentioned, an appropriate construction of Bollob´s, Daykin, and Erdo˝s [122] and further similar constructions shows the sharpness of these results.

There is a sequence of papers of Ro¨dl, Ruci´nski, and Szemer´edi on this topic: [692] assumes large minimum degree, [695] assumes large codegree. To ensure Hamiltonian cycles in hypergraphs, see [693], [694], [696], and see also the above authors with Schacht [690], and Reiher [673].

The problem of 1-factors, or almost 1-factors is, of course, connected to (almost perfect) tilings, and there are several results in that direction, as well, see, e.g., Markstr¨om and Ruci´nski [612], Pikhurko [647], Lo and Markstr¨om [577, 578, 579]. 138

Several results mentioned above or discussed below use the Absorption Method, as is shown in Tables 2, 3. (See also the earlier Ro¨dl-Ruci´nski survey [688] on these hypergraph problems and results.)

The ﬁrst line of Table 3 diﬀers from the other ones by that it is connected to Graph Packing, and within that to the Sauer-Spencer theorem. The subsequent lines try to show in time order some important papers using the absorption method, on loose and tight hypergraph Hamilton cycles (Table 2) and matching (Table 3)

These tables also contain some results on random graphs, and also some lines on Universal graphs, but we skip explaning them. For details see the papers of Alon and Capalbo, e.g., [27], or Alon, Capalbo, Kohayakawa, Ro¨dl, Rucinski, and Szemer´edi [28]. Further, Table 1 has an item on monochromatic cycle partitions as well.

9.6. Tiling hypergraphs

Of course, a matching that (almost) covers a hypergraph V (Hk(n)) is an (almost) tiling. One can also ask if for k-uniform hypergraphs do we get interesting

![image 617](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile617.png>)

- 137This implies Theorem 9.17.
- 138The earlier excellent surveys of Fu¨redi [369, 372] are primarily on small excluded sub-


graphs.

results when we wish to tile them for a ﬁxed F by vertex-disjoint copies of F. The outstanding results of Keevash [500]139 on designs and the related results are also tiling theorems, however, here we mention only that Pikhurko, beside investigating codegree matching problems, in [647] also investigated the problem

of ensuring K4(3)-tilings in a hypergraph with large codegree. These problems were connected to each other.

![image 618](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile618.png>)

![image 619](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile619.png>)

![image 620](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile620.png>)

![image 621](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile621.png>)

![image 622](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile622.png>)

![image 623](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile623.png>)

![image 624](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile624.png>)

Authors Year About what? Methods Where

![image 625](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile625.png>)

![image 626](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile626.png>)

![image 627](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile627.png>)

![image 628](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile628.png>)

![image 629](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile629.png>)

![image 630](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile630.png>)

![image 631](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile631.png>)

![image 632](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile632.png>)

Ro¨dl, Ruci´nski, 1999 Hypergraph packing, Mislead- CPC Taraz 1999 embedding ing! [697] K¨uhn and Osthus 2006 Matching, implied by min Stability [561]

![image 633](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile633.png>)

![image 634](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile634.png>)

![image 635](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile635.png>)

![image 636](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile636.png>)

![image 637](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile637.png>)

![image 638](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile638.png>)

![image 639](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile639.png>)

![image 640](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile640.png>)

![image 641](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile641.png>)

![image 642](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile642.png>)

![image 643](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile643.png>)

![image 644](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile644.png>)

![image 645](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile645.png>)

![image 646](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile646.png>)

![image 647](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile647.png>)

![image 648](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile648.png>)

![image 649](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile649.png>)

![image 650](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile650.png>)

![image 651](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile651.png>)

deg in r-partite hypergraph ??? JGT Pikhurko 2008 Matching, Tiling, min codeg ??? GC [647] Han, Person, 2009 Perfect Matching, mindegree Absorb. SIDMA Schacht [449] Czygrinow-Kamat 2012 perfect matching Sharp Absorb. ELECT

![image 652](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile652.png>)

![image 653](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile653.png>)

![image 654](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile654.png>)

![image 655](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile655.png>)

![image 656](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile656.png>)

![image 657](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile657.png>)

![image 658](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile658.png>)

![image 659](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile659.png>)

![image 660](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile660.png>)

![image 661](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile661.png>)

![image 662](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile662.png>)

![image 663](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile663.png>)

![image 664](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile664.png>)

![image 665](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile665.png>)

![image 666](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile666.png>)

![image 667](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile667.png>)

![image 668](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile668.png>)

![image 669](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile669.png>)

![image 670](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile670.png>)

![image 671](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile671.png>)

![image 672](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile672.png>)

![image 673](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile673.png>)

![image 674](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile674.png>)

![image 675](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile675.png>)

![image 676](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile676.png>)

![image 677](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile677.png>)

![image 678](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile678.png>)

![image 679](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile679.png>)

![image 680](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile680.png>)

![image 681](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile681.png>)

![image 682](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile682.png>)

![image 683](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile683.png>)

![image 684](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile684.png>)

codegree condition, 4-unif Stability JC [222] Alon, Frankl, Huang, 2012 Large matchings in uniform Fractional JCTA Ro¨dl, Ruci´nski, hypergraphs and the conjec- matching [35] Sudakov: ture of Erdo˝s and Samuels,

![image 685](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile685.png>)

![image 686](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile686.png>)

![image 687](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile687.png>)

![image 688](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile688.png>)

![image 689](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile689.png>)

![image 690](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile690.png>)

![image 691](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile691.png>)

![image 692](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile692.png>)

![image 693](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile693.png>)

![image 694](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile694.png>)

![image 695](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile695.png>)

![image 696](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile696.png>)

![image 697](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile697.png>)

![image 698](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile698.png>)

![image 699](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile699.png>)

![image 700](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile700.png>)

![image 701](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile701.png>)

![image 702](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile702.png>)

![image 703](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile703.png>)

![image 704](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile704.png>)

![image 705](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile705.png>)

![image 706](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile706.png>)

![image 707](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile707.png>)

![image 708](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile708.png>)

![image 709](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile709.png>)

![image 710](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile710.png>)

I. Khan 2013 Perfect matching, min degree Absorb. SIDMA

![image 711](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile711.png>)

![image 712](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile712.png>)

![image 713](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile713.png>)

- 3-uniform Stability [507]

![image 714](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile714.png>)

![image 715](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile715.png>)

![image 716](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile716.png>)

![image 717](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile717.png>)

![image 718](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile718.png>)

I. Khan 2016 Perfect matching, min degree Absorb. JCTB

![image 719](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile719.png>)

![image 720](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile720.png>)

![image 721](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile721.png>)

![image 722](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile722.png>)

![image 723](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile723.png>)

![image 724](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile724.png>)

![image 725](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile725.png>)

![image 726](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile726.png>)

- 4-uniform Stability [508]


![image 727](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile727.png>)

![image 728](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile728.png>)

![image 729](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile729.png>)

![image 730](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile730.png>)

Table 3: Absorbing for hypergraphs, Matching, ...

9.7. Vertex-partition for hypergraphs

The vertex-partition results of Subsection 7.4 can also be extended to hypergraphs, see Gy´arf´s and G.N. Sa´rk¨ozy [434, 435] and of G.N. Sa´rk¨ozy [723]. Thus, e.g., G.N. Sa´rk¨ozy proved the following.

Theorem 9.19 (G.N. Sa´rk¨ozy (2014), [723]). For all integers k,r ≥ 2, there exists an n0 = n0(k,r) such that if n > n0(k,r) and K(nk) is r-edge-coloured, then its vertex set can be partitioned into at most 50rk log(rk) vertex disjoint loose monochromatic cycles.

For the case of two colours and loose/tight cycles Bustamante, Han, and M. Stein [168] proved some hypergraph versions of Lehel’s conjecture, where, however, a few vertices remain uncovered. Bustamante, Corsten, No´ra Frankl, Pokrovskiy and Skokan [169] proved the tight-cycle version.

![image 731](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile731.png>)

139see also Keevash, [502], Barber, Ku¨hn, Lo, and Osthus [93], Barber, Ku¨hn, Lo, Montgomery, and Osthus [92],.. .

- Theorem 9.20. There exists a constant c(k,r) such that if H(k) is a k-uniform hypergraph whose edges are coloured by r colours, then V (H(k)) can be partitioned into c(k,r) subsets, each deﬁning monochromatic Tight hypergraphcycles.

For some related results see also the surveys of Gy´arf´as [426], and Fujita, H. Liu, and Magnant [368].

9.8. Generalizing Gy´arf´as-Ruszinko´-S´ark¨ozy-Szemere´di theorem to hypergraphs

We have mentioned that several graph results were generalized to hypergraphs. Theorem 7.19 was generalized to hypergraphs ﬁrst by Gy´arf´as and G.N. Sa´rk¨ozy [435]: they covered the coloured K(nk) by Berge paths, by Berge cycles, and by loose cycles. Perhaps their loose cycle result was the deepest. Its proof followed the method of Erdo˝s, Gy´arf´s, and Pyber [291] and used the linearity of Ramsey number for a “crown” that was a generalization of the Triangle-Cycle used in Subsection 6.5. The loose cycle result was improved by G.N. Sa´rk¨ozy:

- Theorem 9.21 ([723]). For any integers r,k ≥ 2, there exists a threshold n0(k,r) for which, if n > n0(k,r), then for any r-edge-colouring of a k-uniform complete hypergraph K(nk), we can partition the vertices into at most 50rk log(rk) classes Ui, each deﬁning a monochromatic Loose k-cycle.


9.9. A new type of hypergraph results, strong degree

This subsection is motivated by a paper of Gy´arf´s, Gy˝ori, and Simonovits [427]. Their original motivation was to prove the following conjecture that is still open.

Conjecture 9.22 (Gya´rf´s–G.N. Sa´rk¨ozy, [435]). One can partition the vertex set of every 3-uniform hypergraph H(3)n into α(H(3)n ) linear (i.e. loose) cycles, hyperedges and subsets of hyperedges.

A theorem of Po´sa [659] is

- Theorem 9.23 (P´osa (1964), [659]). For every graph G one can partition V (G) into at most α(G) cycles, where a vertex or an edge is accepted as a cycle.

Conjecture 9.22 would extend Po´sa theorem, see [589] from graphs to 3uniform hypergraphs. Conjecture 9.22 was proved in [435] for “weak cycles” instead of linear cycles, where “weak cycle” diﬀers from a “loose cycle” by that the consecutive edges must intersect, but not necessarily in 1 vertex. Here one has to consider subsets of hyperedges also as cycles, in Conjecture 9.22, as

shown, e.g., by the complete hypergraph K5(3). The following weaker version of Conjecture 9.22 was proved recently:

- Theorem 9.24 (Ergemlidze, Gy˝ori, and Methuku [325]). One can cover the


vertices of any 3-uniform hypergraph H(3)n by α(H(3)n ) edge-disjoint linear (i.e. loose) cycles, hyperedges and subsets of hyperedges.

— · —

Let ρ(H(3)n ) denote the minimum number of linear cycles, hyperedges or subsets of hyperedges needed to partition V (H(3)n ) as described in Conjecture 9.22 and let χ(H(3)n ) denote the chromatic number of H(3)n , the minimum number of colors in a vertex coloring of H(3)n without monochromatic edges. The following result proves that Conjecture 9.22 is true if there are no linear cycles in H(3)n .

- Theorem 9.25 (Gya´rf´s-Gyo˝ri-Simonovits [427]). If H(3)n is a 3-uniform hypergraph without linear cycles, then ρ(H(3)n ) ≤ α(H(3)n ). Moreover, χ(H(3)n ) ≤ 3.

The family of hypergraphs without linear cycles seems to be intriguing. [427] uses a new degree concept: the strong degree. Let H(3)n = (V,E) be a 3-uniform hypergraph, for v ∈ V the link graph of v in H(3)n is the graph with vertex set V − v and edge set {(x,y) : (v,x,y) ∈ E}. The strong degree d+(v) for v ∈ V is the maximum number of independent edges (i.e. the size of a maximum matching) in the link graph of v. The main results of [427] are motivated by the following trivial assertions: a graph of minimum degree 2 contains a cycle; if Gn has no cycles then α(Gn) ≥ n/2.

- Theorem 9.26 (Gya´rf´s-Gyo˝ri-Simonovits [427]). If H(3)n is a 3-uniform hypergraph with d+(v) ≥ 3 for all v ∈ V , then H(3)n contains a linear cycle.

Theorem 9.26 is “self-improving”:

- Theorem 9.27 ([427]). Suppose that H(3)n is a 3-uniform hypergraph with d+(v) ≥


- 3 for all but at most one v ∈ V . Then H contains a linear cycle.


The proofs are not easy. One thinks that several interesting embedding results can be proved where one uses minv∈V(G) d+(v) instead of dmin(G).

Acknowledgement. We thank to several friends and colleagues the useful discussions about the many topics discussed in this survey. We thank above all to J´ozsef Balogh and Andra´s Gy´arf´s, and also to Zolt´an F¨uredi, J´anos Pach, Jan Hladk´y, Zolt´an L. Nagy, J´anos Pintz, Andrzej Ruci´nski, Imre Ruzsa, G´abor Sa´rk¨ozy, Andrew Thomason, and G´eza T´th.

# Bibliography

- [1] S. Abbasi: How tight is the Bollob´s-Komlo´s conjecture?, Graphs Combin. 16

(2) (2000), 129–137.

140

- [2] Harvey L. Abbott and Andrew C.F. Liu: The existence problem for colour critical linear hypergraphs, Acta Math. Acad Sci Hung Tomus 32 (3-4) (1978), 273–282.
- [3] Martin Aigner and Stephan Brandt: Embedding arbitrary graphs of maximum degree two, J. London Math. Soc. (2), 48 (1993), 39–51.
- [4] Elad Aigner-Horev, David Conlon, Hiep H`an, and Yury Person: Quasirandomness in hypergraphs, Electronic Notes in Discrete Mathematics 61 (2017) 13–19.
- [5] Elad Aigner-Horev, Hiep H`an, and Mathias Schacht: Extremal results for odd cycles in sparse pseudorandom graphs, Combinatorica 34 (4) (2014), 379–406.
- [6] Mikl´os Ajtai, Paul Erd˝s, J´anos Koml´os, and Endre Szemere´di: On Tur´an’s theorem for sparse graphs, Combinatorica 1 (4) (1981) 313–317.
- [7] M. Ajtai, J. Koml´os, J´anos Pintz, Joel Spencer, and E. Szemere´di: Extremal uncrowded hypergraphs, J. Combin. Theory Ser A 32 (1982), 321–335.
- [8] M. Ajtai, J. Koml´os, Mikl´os Simonovits, and E. Szemer´edi: Erd˝s-So´s Conjecture. (In preparation, in several manuscripts)
- [9] M. Ajtai, J. Koml´os, and E. Szemere´di: A note on Ramsey numbers. J. Combin. Theory Ser. A 29 (3) (1980) 354–360.
- [10] M. Ajtai, J. Koml´os, and E. Szemere´di: A dense inﬁnite Sidon sequence, European J. Combin. 2 (1981), 1–11.
- [11] M. Ajtai, J. Koml´os, and E. Szemere´di: Sorting in c log n parallel steps. Combinatorica 3 (1) (1983) 1–19.
- [12] M. Ajtai, J. Koml´os, and E. Szemere´di: On a conjecture of Loebl, in Graph Theory, Combinatorics, and Algorithms, Vols. 1, 2 (Kalamazoo, MI, 1992), Wiley-Intersci. Publ., Wiley, New York, (1995), 1135–1146.
- [13] Vladimir E. Alekseev.: Range of values of entropy of hereditary classes of graphs (in Russian), Diskret. Mat. 4 (1992), 148–157. see also On the entropy values of hereditary classes of graphs. Discrete Math. Appl. 3 (1993) 191–199.
- [14] Peter Allen: Covering two-edge-coloured complete graphs with two disjoint monochromatic cycles, Combinatorics, Probability and Computing, 17 (4)


(2008) 471–486.

![image 732](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile732.png>)

140Below (to be more informative) we shall often use the full name in the author’s ﬁrst or second occurrence, and/or in his ﬁrst occurrence as the ﬁrst author but this rule is not too strict. Also in some exceptional cases the authors originally were not in alphabetic order and we switched their order to alphabetic.

115

- [15] P. Allen, Julia B¨ottcher, Oliver Cooley, and Richard Mycroft: Tight cycles and regular slices in dense hypergraphs. J. Combin. Theory Ser. A 149 (2017), 30–100.
- [16] P. Allen, J. B¨ottcher, Hiep H`an, Y. Kohayakawa, and Y. Person: Powers of Hamilton cycles in pseudorandom graphs. LATIN 2014: theoretical informatics, 355–366, Lecture Notes in Comput. Sci., 8392, Springer, Heidelberg, 2014.
- [17] P. Allen, J. B¨ottcher, Hiep H`an, Yoshiharu Kohayakawa, and Yury Person: Powers of Hamilton cycles in pseudorandom graphs. Combinatorica 37 (4) (2017), 573–616.
- [18] P. Allen, J. B¨ottcher, H. H`an, Y. Kohayakawa, and Y. Person: Blow-up lemmas for sparse graphs, Submitted for publication, arXiv:1612.00622. (2018+)
- [19] P. Allen, Peter Keevash, Benny Sudakov, and Jacques Verstrae¨te: Tur´an numbers of bipartite graphs plus an odd cycle, J. Combin. Theory Ser. B 106 (2014), 134–162.
- [20] Noga Alon: Eigenvalues and expanders, Combinatorica 6 (1986), 83–96.
- [21] N. Alon: Independent sets in regular graphs and sum-free subsets of ﬁnite groups. Israel J. Math. 73 (1991) 247–256.
- [22] N. Alon: Tools from Higher Algebra, Chapter 32 of Handbook of Combinatorics (ed. Graham, Lova´sz, Gro¨tschel), (1995) pp. 1749–1783, North-Holland, Amsterdam.
- [23] N. Alon: Combinatorial Nullstellensatz, Combinatorics, Probability and Computing 8 (1999), 7–29.
- [24] N. Alon, J´ozsef Balogh, Be´la Bollob´s, and Robert Morris: The structure of almost all graphs in a hereditary property. J. Combin. Theory Ser. B, 101 (2)

(2011) 85–110.

- [25] N. Alon, J. Balogh, R. Morris, and Wojciech Samotij: A reﬁnement of the Cameron-Erd˝os conjecture, Proc. London Math. Soc. (3) 108 (1) (2014), no. 1, 44–72.
- [26] N. Alon, J. Balogh, R. Morris, and W. Samotij: Counting sum-free sets in Abelian groups, Israel J. Math. 199 (1) (2014), 309–344.
- [27] N. Alon and M. Capalbo: Sparse universal graphs for bounded-degree graphs, Random Struct Algorithms 31 (2) (2007), 123–133.
- [28] N. Alon, M. Capalbo, Y. Kohayakawa, V. Ro¨dl, A. Rucin´ski, and E. Szemere´di: Near-optimum universal graphs for graphs with bounded degrees (extended abstract), In Approximation, randomization, and combinatorial optimization (Berkeley, CA, 2001), Lecture Notes in Computer Science Vol. 2129, Springer, Berlin, 2001, pp. 170–180.
- [29] N. Alon and Fan R.K. Chung: Explicit construction of linear sized tolerant networks, Discrete Mathematics 72 (1988), Proceedings of the First Japan Conference on Graph Theory and Applications (Hakone, 1986), 15–19.
- [30] N. Alon, Richard A. Duke, Hanno Lefmann, Vojtech Ro¨dl, and Raphael Yuster: The algorithmic aspects of the Regularity Lemma. J. Algorithms 16 (1994) 80-

109. see also: the extended abstract, 33rd Annu Symp Foundations of Computer Science, Pittsburgh, IEEE Comput Soc. Press, New York, 1992, pp. 473–481.

- [31] N. Alon and P. Erd˝s: An application of graph theory to additive number theory, European J. Combin. 6 (3) (1985) 201–203.
- [32] N. Alon and Elgar Fischer: 2-factors in dense graphs, Discrete Math., 152

(1996), 13–23.

- [33] N. Alon, E. Fischer, Michael Krivelevich, and M´rio Szegedy: Eﬃcient testing of large graphs, Combinatorica 20 (2000), 451–476. see also its extended abstract,


- Proc. 40th Ann. Symp. on Found. of Comp. Sci. IEEE (1999), 656–666.
- [34] N. Alon, E. Fischer, Ilan Newman, and Asaf Shapira: A combinatorial characterization of the testable graph properties: It’s all about regularity, SIAM J. Comput., 39 (1) 143–167, 2009. STOC ’06: Proceedings of the 38th Annual ACM Symposium on Theory of Computing, ACM, New York, 2006, pp. 251–260.
- [35] N. Alon, P. Frankl, H. Huang, V. Ro¨dl, A. Rucin´ski, and B. Sudakov: Large matchings in uniform hypergraphs and the conjecture of Erd˝os and Samuels, J. Combin. Theory Ser. A, 119 (2012), pp. 1200–1215.
- [36] N. Alon and Zolta´n Fu¨redi: Spanning subgraphs of random graphs, Graphs and Combin. 8 (1) (1992) 91–94.
- [37] N. Alon, Jeong-Han Kim, and J. Spencer: Nearly perfect matchings in regular simple hypergraphs. Israel J. Math. 100 (1997), 171–187.
- [38] N. Alon, M. Krivelevich, and B. Sudakov: Tur´an numbers of bipartite graphs and related Ramsey-type questions, Combin. Probab. Comput 12 (2003), 477– 494.
- [39] N. Alon and Vitalij D. Milman: Eigenvalues, expanders and superconcentrators, in Proceedings of the 25th FOCS, IEEE, New York, 1984, pp. 320–322.
- [40] N. Alon, Ankur Moitra, and B. Sudakov: Nearly complete graphs decomposable into large induced matchings and their applications. J. Eur. Math. Soc. (JEMS) 15 (5) (2013) 1575–1596. See also in Proc. 44th ACM STOC,(2012) 1079–1089.
- [41] N. Alon, J´anos Pach, Ron Pinchasi, Radosˇ Radoicˇic´, and Micha Sharir: Crossing patterns of semi-algebraic sets, J. Combin. Theory, Ser. A 111 (2005) 310–326.
- [42] N. Alon, Lajos Ro´nyai, and Tibor Szab´o: Norm-graphs: Variations and application, J. Combin. Theory Ser. B 76 (1999), 280–290.
- [43] N. Alon and Asaf Shapira: Every monotone graph property is testable, Proc. of the 37th ACM STOC, Baltimore, ACM Press (2005), 128–137.
- [44] N. Alon and A. Shapira: A characterization of the (natural) graph properties testable with one-sided error, Proc. 46th IEEE FOCS (2005), 429–438.
- [45] N. Alon and A. Shapira: On an extremal hypergraph problem of Brown, Erd˝s and S´os, Combinatorica 26 (2006), 627–645.
- [46] N. Alon, A. Shapira, and Uri Stav: Can a graph have distinct regular partitions?, SIAM J. Discrete Math., 23 (2008/09), 278–287.
- [47] N. Alon and Clara Shikhelman: Many T copies in H-free graphs. J. Combin. Theory Ser. B 121 (2016), 146–172.
- [48] Noga Alon and Joel Spencer: ”The Probabilistic Method”, Wiley-Interscience Series in Discrete Mathematics and Optimization, John Wiley & Sons, Inc., Hoboken, NJ, 2016. xiv+375 pp. 4th, updated edition.
- [49] N. Alon and R. Yuster: H-factors in dense graphs. J. Combin. Theory Ser. B 66 (1996) 269–282.
- [50] Richard P. Anstee, Balin Fleming, Z. Fu¨redi, and Attila Sali: Color critical hypergraphs and forbidden conﬁgurations, in: S. Felsner, (Ed.) Discrete Mathematics and Theoretical Computer Science Proceedings, vol. AE, 2005, pp. 117– 122.
- [51] Tim Austin: Deducing the multidimensional Szemere´di Theorem from an inﬁnitary removal lemma. J. Anal. Math. 111 (2010) 131–150.
- [52] T. Austin: Deducing the density Hales-Jewett theorem from an inﬁnitary removal lemma, J. Theoret. Probab. 24 (2011), 615–633.
- [53] T. Austin and Terrence C. Tao: Testability and repair of hereditary hypergraph properties, Random Struct Algor 36 (2010), 373–463.


- [54] Jacqueline Ayel: Sur l’existence de deux cycles suppl´ementaires unicolores, disjoints et de couleurs diﬀe´rentes dans un graph complet bicolore, PhD thesis, Univ. Grenoble, 1979.
- [55] L´aszl´o Babai: An anti-Ramsey theorem, Graphs Combin., 1 (1985), 23–28.
- [56] L. Babai, M. Simonovits, and J. Spencer: Extremal subgraphs of random graphs, J. Graph Theory 14 (1990), 599–622.
- [57] L. Babai and Vera T. S´os: Sidon sets in groups and induced subgraphs of Cayley graphs, Europ. J. Combin. 6 (1985) 101–114.
- [58] Rahil Baber and John Talbot: Hypergraphs do jump. Combin. Probab. Comput. 20 (2) (2011), 161–171.
- [59] Be´la Bajnok: Additive Combinatorics, a menu of research problems, arXiv1705:07444, to appear as a book.
- [60] J´ozsef Balogh, J´anos Bara´t, D´aniel Gerbner, Andr´as Gya´rfa´s and G´bor N. S´ark¨ozy: Partitioning 2-edge-colored graphs by monochromatic paths and cycles, Combinatorica 34 (2014), 507–526.
- [61] J. Balogh, B. Bollob´s, and Bhargav Narayanan: Transference for the Erd˝sKo-Rado theorem. Forum of Math. Sigma, (2015), e23, 18 pp.
- [62] J. Balogh, B. Bollob´s, and M. Simonovits: The number of graphs without forbidden subgraphs, J. Combin. Theory Ser. B 91 (1) (2004) 1–24.
- [63] J. Balogh, B. Bollob´s, and M. Simonovits: The typical structure of graphs without given excluded subgraphs, Random Structures and Algorithms 34 (2009), 305–318.
- [64] J. Balogh, B. Bollob´s, and M. Simonovits: The ﬁne structure of octahedron-free graphs, J. Combin. Theory Ser. B 101 (2011) 67–84.
- [65] J. Balogh, Neal Bushaw, Maurı´cio Collares, Hong Liu, R. Morris, and Maryam Sharifzadeh: The typical structure of graphs with no large cliques. Combinatorica 37 (4) (2017) 617–632.
- [66] J. Balogh, Jane Butterﬁeld, Ping Hu, and John Lenz: Mantel’s theorem for random hypergraphs. Random Structures and Algorithms 48 (4) (2016) 641– 654.
- [67] J. Balogh, Be´la Csaba, Martin Pei, and W. Samotij: Large bounded degree trees in expanding graphs. Electron. J. Combin. 17 (1) (2010), Research Paper 6, 9 pp.
- [68] J. Balogh, B. Csaba, and W. Samotij: Local resilience of almost spanning trees in random graphs. Random Struct. Algor. 38 (2011) 121–139.
- [69] J. Balogh, P. Hu, and M. Simonovits: Phase transitions in Ramsey-Tur´an theory, J. Combin. Theory Ser. B 114 (2015) 148–169.
- [70] J. Balogh and John Lenz: Some exact Ramsey-Tur´an numbers, Bull. London Math. Soc. 44 (2012), 1251–1258.
- [71] J. Balogh and J. Lenz: On the Ramsey-Tur´an numbers of graphs and hypergraphs, Israel J. Math. 194 (2013), 45–68.
- [72] J. Balogh, Hong Liu, M. Sharifzadeh, and Andrew Treglown: The number of maximal sum-free subsets of integers, Proc. Amer. Math. Soc. 143 (11) (2015), 4713–4721.
- [73] J. Balogh, Allan Lo, and Theodore Molla: Transitive triangle tilings in oriented graphs. J. Combin. Theory Ser. B 124 (2017), 64–87.
- [74] J. Balogh, Andrew McDowell, T. Molla, and Richard Mycroft: Triangle-tilings in graphs without large independent sets, Combinatorics, Probability and Computing, 27 (4) (2018) 449–474.
- [75] J. Balogh, T. Molla, and M. Sharifzadeh: Triangle factors of graphs without


- large independent sets and of weighted graphs. Random Structures and Algorithms 49 (4) (2016), 669–693. // Lingli Sun)
- [76] J. Balogh, R. Morris, and W. Samotij: Random sum-free subsets of Abelian groups, Israel J. Math. 199 (2) (2014), 651–685.
- [77] J. Balogh, R. Morris, and W. Samotij: Independent sets in hypergraphs. J. Amer. Math. Soc. 28 (3) (2015), 669–709.
- [78] J. Balogh, R. Morris, and W. Samotij: The method of Hypergraph containers, ICM 2018, also 1801.04584v1 (2018)
- [79] J. Balogh, R. Morris, W. Samotij, and Lutz Warnke: The typical structure of sparse Kr+1-free graphs. Trans. Amer. Math. Soc. 368 (9) (2016), 6439–6485.
- [80] J. Balogh, Frank Mousset, and Jozef Skokan: Stability for vertex cycle covers. Electron. J. Combin. 24 (3) (2017), Paper 3.56, 25 pp.
- [81] J. Balogh and Dhruv Mubayi: Almost all triple systems with independent neighborhoods are semi-bipartite, J. Combin. Theory Ser. A 118 (4) (2011), 1494– 1518.
- [82] J. Balogh and D. Mubayi: Almost all triangle-free triple systems are tripartite, Combinatorica 32 (2) (2012), 143–169,
- [83] J. Balogh and Cory Palmer: On the tree packing conjecture, SIAM Journal on Discrete Mathematics 27 (2013), 1995–2006.
- [84] J. Balogh and S´arkaˇ Petrˇı´cˇkova´: The number of the maximal triangle-free graphs. Bull. London Math. Soc. 46 (5) (2014), 1003–1006.
- [85] J. Balogh and W. Samotij: Almost all C4-free graphs have fewer than (1 − ǫ)ex(n, C4) edges, SIAM J. Discrete Math. 24 (2010) 1011–1018.
- [86] J. Balogh and W. Samotij: The number of Km,m-free graphs, Combinatorica 31 (2) (2011) 131–150.
- [87] J. Balogh and W. Samotij: The number of Ks,t-free graphs, J. London Math. Soc. (2) 83 (2) (2011) 368–388.
- [88] J. Bang-Jensen and G. Gutin: Digraphs. Theory, algorithms and applications, Springer Monographs in Mathematics, Springer-Verlag, London, 2009.
- [89] Boaz Barak, Anup Rao, Ronen Shaltiel, and Avi Wigderson: 2-source dispersers for no(1) entropy, and Ramsey graphs beating the Frankl-Wilson construction. Ann. of Math. (2) 176 (3) (2012), 1483–1543.
- [90] J. Bara´t, A. Gya´rfa´s, Jeno˝ Lehel, and G.N. S´ark¨ozy: Ramsey number of paths and connected matchings in Ore-type host graphs. Discrete Math. 339 (6)

(2016), 1690–1698.

- [91] J. Bara´t and G.N. S´ark¨ozy: Partitioning 2-edge-colored Ore-type graphs by monochromatic cycles. J. Graph Theory 81 (4) (2016), 317–328.
- [92] Ben Barber, Daniela Ku¨hn, Allan Lo, Richard Montgomery, and Deryk Osthus: Fractional clique decompositions of dense graphs and hypergraphs. J. Combin. Theory Ser. B 127 (2017), 148–186.
- [93] Ben Barber, D. Ku¨hn, Allan Lo, and D. Osthus: Edge-decompositions of graphs with high minimum degree. Advances Math. 288 (2016), 337–385.
- [94] J´ozsef Beck: On size Ramsey number of paths, trees, and circuits. I, J. Graph Theory 7 (1) (1983) 115–129.
- [95] J. Beck: An algorithmic approach to the Lova´sz local lemma. Rand. Struct. Algor. 2 (4) (1991) 343–365.
- [96] Felix A. Behrend: ”On sets of integers which contain no three terms in arithmetical progression,” Proc. Nat. Acad. Sci. USA, 32 (12) (1946), 331–332, 1946.
- [97] Mathias Beiglbo¨ck: A variant of the Hales-Jewett theorem. Bull. London Math.


- Soc. 40 (2) (2008), 210–216. (2009c:05247)
- [98] Louis Bellmann and Christian Reiher: Tur´an’s theorem for the Fano plane, Arxiv 1804.07673
- [99] Fabricio S. Benevides and J. Skokan: The 3-colored Ramsey number of even cycles. J. Combin. Theory Ser. B 99 (4) (2009) 690–708.
- [100] Patrick Bennett and Andrzej Dudek: On the Ramsey-Tur´an number with small s-independence number. J. Combin. Theory Ser. B 122 (2017), 690–718.
- [101] Clark T. Benson: Minimal regular graphs of girth 8 and 12, Canad. J. Math. 18 (1966) 1091–1094.
- [102] Vitaly Bergelson and Alexander Leibman: Polynomial extensions of van der Waerden’s and Szemere´di’s theorems, J. Amer. Math. Soc. 9 (3) (1996) 725– 753.
- [103] V. Bergelson, A. Leibman: Set-polynomials and polynomial extension of the Hales-Jewett theorem, Ann. of Math. (2) 150 (1) (1999) 33-75.
- [104] J.C. Bermond, A. Germa, M.C. Heydemann, D. Sotteau: Hypergraphes hamiltoniens, in: Proble`mes combinatoires et the´orie des graphes, Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976, in: Colloq. Internat., vol. 260, CNRS, Paris, 1973, pp. 39–43.
- [105] J.-C. Bermond and Carsten Thomassen: Cycles in digraphs—a survey, J. Graph Theory 5 (1981), 1–43.
- [106] Claudia Bertram-Kretzberg, Thomas Hofmeister, H. Lefmann: An algorithm for Heilbronn’s problem, SIAM J. Comput., 30 (2) (2000) 383–390.
- [107] C. Bertram-Kretzberg and H. Lefmann: The Algorithmic Aspects of Uncrowded Hypergraphs, SIAM Journal on Computing 29 (1999) 201–230.
- [108] Ste´phane Bessy and Ste´phan Thomasse´: Partitioning a graph into a cycle and an anticycle, a proof of Lehel’s conjecture, Journal of Combinatorial Theory, Series B, 100 (2) (2010) 176–180.
- [109] Yuri Bilu: Sum-free sets and related sets, Combinatorica 18 (1998), 449–459.
- [110] Yitzhak Birk, Nati Linial, and Roy Meshulam: On the uniform-traﬃc capacity of single-hop interconnections employing shared directional multichannels. IEEE Trans. Information Theory 39 (1993) 186–191.
- [111] G.R. Blakley and P. Roy: A H¨older type inequality for symmetric matrices with nonnegative entries, Proc. Amer. Math. Soc.16 (1965), 1244–1245.
- [112] Thomas F. Bloom: A quantitative improvement for Roth’s theorem on arithmetic progressions. J. London Math. Soc. (2) 93 (3) (2016), 643–663.
- [113] Tom Bohman, Alan Frieze, and Ryan Martin: How many random edges make a dense graph Hamiltonian? Random Structures and Algorithms 22 (1) (2003), 33–42.
- [114] T. Bohman, A. Frieze, Mikl´os Ruszink´o, and Lubos Thoma: Vertex covers by edge disjoint cliques. Paul Erd˝s and his mathematics (Budapest, 1999). Combinatorica 21 (2) (2001), 171–197.
- [115] T. Bohman and P. Keevash: Dynamic concentration of the triangle-free process.

(2013), in The Seventh European Conference on Combinatorics, Graph Theory and Applications, CRM Series 16, Ed. Norm., Pisa, 2013, pp. 489–495.

- [116] B. Bollob´s: Three-graphs without two triples whose symmetric diﬀerence is contained in a third, Discrete Mathematics 8 (1974), 21–24.
- [117] B. Bollob´s: Relations between sets of complete subgraphs, in Proceedings of the Fifth British Combinatorial Conference (Univ. Aberdeen, Aberdeen, 1975), Congressus Numerantium, Vol. 15, Utilitas Mathematica, Winnipeg, MB, (1976), pp. 79–84.


- [118] B. Bollob´s: Complete subgraphs are elusive. J. Combinatorial Theory Ser. B 21 (1) (1976), no. 1, 1–7.
- [119] B. Bollob´s: Extremal Graph Theory, Academic Press, London (1978). / Lond Math. Soc. Monogr 11, Academic Press, London-New York, 1978, pp. 488.
- [120] B. Bollob´s: Extremal Graph Theory, Handbook of Combinatorics, Vol. 2, Elsevier, Amsterdam, (1995) pp. 1231–1292.
- [121] B. Bollob´s: Random Graphs, second ed., Cambridge Stud. Advances Math., vol. 73, Cambridge Univ. Press, Cambridge, (2001).
- [122] B. Bollob´s, David E. Daykin, and P. Erd˝s: Sets of independent edges of a hypergraph, Quart. J. Math. Oxford 21 (1976) 25–32.
- [123] B. Bollob´s and Stephen E. Eldridge: Packing of Graphs and Applications to Computational Complexity, Journal of Combinatorial Theory, Series B 25

(1978), 105–124.

- [124] B. Bollob´s and P. Erd˝s: On the structure of edge graphs, Bull. London Math. Soc. 5 (1973) 317–321.
- [125] B. Bollob´s and P. Erd˝s: Cliques in random graphs. Math. Proc. Cambridge Philos. Soc. 80 (3) (1976), 419–427.
- [126] B. Bollob´s and P. Erd˝s: On a Ramsey-Tur´an type problem, J. Combin. Theory Ser. B 21 (1976), 166–168.
- [127] B. Bollob´s, P. Erd˝s, and M. Simonovits: On the structure of edge graphs II, J. London Math. Soc., 12 (2) (1976) 219–224.
- [128] B. Bollob´s, P. Erd˝s, M. Simonovits, and E. Szemer´edi: Extremal graphs without large forbidden subgraphs. Advances in graph theory (Cambridge Combinatorial Conf., Trinity Coll., Cambridge, 1977). Ann. Discrete Math. 3 (1978), 29–41.
- [129] B. Bollob´s, B. Narayanan and Andrei Raigorodskii: On the stability of the Erd˝os-Ko-Rado theorem, J. Combin. Theory Ser. A 137 (2016), 64–78.
- [130] B. Bollob´s and Andrew G. Thomason: Projections of bodies and hereditary properties of hypergraphs, Bull. London Math. Soc. 27 (1995) 417–424.
- [131] B. Bollob´s and A. Thomason: Hereditary and monotone properties of graphs, in: R.L. Graham and J. Nesˇetrˇil (Eds.): The Mathematics of Paul Erd˝s II, vol 14 of Algorithms Combin. Springer, Berlin Heidelberg, (1997) 70–78.
- [132] B. Bollob´s and A. Thomason: On the girth of Hamiltonian weakly pancyclic graphs. J. Graph Theory 26 (3) (1997), 165–173.
- [133] B. Bollob´s and A. Thomason: Weakly pancyclic graphs. J. Combin. Theory Ser. B 77 (1) (1999), 121–137.
- [134] J. Adrian Bondy: Pancyclic graphs. I. J. Combin. Theory, Ser. B 11 (1971), 80–84.
- [135] J.A. Bondy and P. Erd˝s: Ramsey numbers for cycles in graphs. J. Combinatorial Theory Ser. B 14 (1973), 46–54.
- [136] J.A. Bondy and M. Simonovits: Cycles of even length in graphs, J. Combin. Theory Ser. B 16 (1974) 97–105.
- [137] Christian Borgs, Jennifer T. Chayes, L´aszl´o Lova´sz: Moments of two-variable functions and the uniqueness of graph limits, Geom. Func. Anal., 19 (2010), 1597-1619. http://wuw.cs.elte.hu/∼lovasz/limitunique.pdf
- [138] C. Borgs, J. Chayes and L. Lova´sz, V.T. S´os, Bal´azs Szegedy, and Katalin Vesztergombi: Graph limits and parameter testing, STOC ’06: Proceedings of the 38th Annual ACM Symposium on Theory of Computing, ACM, New York, 2006, pp. 261–270.
- [139] C. Borgs, J. Chayes, L. Lova´sz, V.T. S´os, and K. Vesztergombi: Counting graph


- homomorphisms. Topics in discrete mathematics, 315–371, Algorithms Combin. 26, Springer, Berlin, 2006.
- [140] C. Borgs, J. Chayes, L. Lova´sz, V.T. S´os, and K. Vesztergombi: Convergent sequences of dense graphs I: Subgraph frequencies, metric properties and testing, Advances Math. 219 (6) (2008), 1801–1851
- [141] C. Borgs, J.T. Chayes, L. Lova´sz, V.T. S´os, and K. Vesztergombi: Convergent sequences of dense graphs II. Multiway cuts and statistical physics. Ann. of Math. (2) 176 (1) (2012), 151–219.
- [142] J. B¨ottcher, Jan Hladk´y, Diana Piguet, Anush Taraz: An approximate version of the tree packing conjecture, Israel J. Math. 211 (1) (2016) 391–446.
- [143] J. B¨ottcher, Y. Kohayakawa, A. Taraz, and Andreas Wu¨rﬂ: An extension of the blow-up lemma to arrangeable graphs, SIAM J. Discrete Math. 29 (2) (2015) 962-1001.
- [144] J. B¨ottcher, M. Schacht, and A. Taraz: Proof of the bandwidth conjecture of Bollob´s and Koml´os. Math. Ann. 343 (1) (2009), 175–205.
- [145] Jean Bourgain: On triples in arithmetic progression, Geom. Funct. Anal. 9

(1999), 968–984.

- [146] J. Bourgain, Alexander Gamburd, and Peter Sarnak: Aﬃne linear sieve, expanders, and sum-product. Invent. Math. 179, (2010) 559–644.
- [147] S. Brandt, Ralph Faudree, and W. Goddard: Weakly pancyclic graphs, J. Graph Theory 27 (1998) 141–176.
- [148] Graham Brightwell, Konstantinos Panagiotou, and Angelika Steger: Extremal subgraphs of random graphs, Random Structures and Algorithms 41 (2012), 147–178. (Extended abstract: pp. 477–485 in SODA ‘07 (Proc. 18th ACM-SIAM Symp. Discrete Algorithms).
- [149] Hajo Broersma, Jan van den Heuvel, and Henk J. Veldman: A generalization of Ore’s Theorem involving neighborhood unions, Discrete Math. 122 (1993), 37–49.
- [150] William G. Brown: On graphs that do not contain a Thomsen graph, Can. Math. Bull. 9 (1966), 281–285.
- [151] W.G. Brown: On an open problem of Paul Tur´an concerning 3-graphs. In Studies in Pure Mathematics, (1983) Birkh¨auser, Basel, pp. 91–93.
- [152] W.G. Brown, P. Erd˝s, and M. Simonovits: Extremal problems for directed graphs, J. Combin. Theory Ser B 15 (1973), 77–93.
- [153] W.G. Brown, P. Erd˝s, and M. Simonovits: Algorithmic solution of extremal digraph problems, Trans Amer Math. Soc. 292 (1985), 421–449.
- [154] W.G. Brown, P. Erd˝s, and V.T. S´os: On the existence of triangulated spheres in 3-graphs and related problems, Period. Math. Hungar. 3 (1973) 221–228.
- [155] W.G. Brown, P. Erd˝s, and V.T. S´os: Some extremal problems on r-graphs, in “New Directions in the Theory of Graphs,” Proc. 3rd Ann Arbor Conf. on Graph Theory, University of Michigan, 1971, pp. 53–63, Academic Press, New York, (1973).
- [156] W.G. Brown and Frank Harary: Extremal digraphs, Combinatorial theory and its applications, Colloq. Math. Soc. J. Bolyai, 4 (1970) I. 135–198;
- [157] W.G. Brown and John W. Moon: Sur les ensembles de sommets inde´pendants dans les graphes chromatiques minimaux. (French) Canad. J. Math. 21 (1969) 274–278.
- [158] W.G. Brown and M. Simonovits: Digraph extremal problems, hypergraph extremal problems, and the densities of graph structures, Discrete Math., 48


(1984) 147–162.

- [159] W.G. Brown and M. Simonovits: Extremal multigraph and digraph problems, Paul Erd˝s and his mathematics, II (Budapest, 1999), pp. 157–203, Bolyai Soc. Math. Stud., 11, J´anos Bolyai Math. Soc., Budapest, (2002).
- [160] K. O’Bryant: A complete annotated bibliography of work related to Sidon sequences, Electron. J. Combin. (2004), Dynamic Surveys 11, 39 pp. (electronic).
- [161] Boris Bukh and David Conlon: Random algebraic construction of extremal graphs. Bull. London Math. Soc. 47 (2015), 939–945.
- [162] B. Bukh and D. Conlon: Rational exponents in extremal graph theory. J. Eur. Math. Soc. (JEMS) 20 (7) (2018), 1747–1757.
- [163] B. Bukh and Zilin Jiang: A bound on the number of edges in graphs without an even cycle. Combin. Probab. Comput. 26 (1) (2017) 1–15. see also the erratum.
- [164] S.A. Burr and P. Erd˝s: On the magnitude of generalized Ramsey numbers for graphs, in: Inﬁnite and Finite Sets, vol. 1, Keszthely, 1973, in: Colloq. Math. Soc. J´anos Bolyai, vol. 10, North-Holland, Amsterdam, 1975, pp. 214–240.
- [165] S.A. Burr, P. Erd˝s, Peter Frankl, Ron L. Graham, and V.T. S´os: Further results on maximal antiramsey graphs, In Graph Theory, Combinatorics and Applications, Vol. I, Y. Alavi, A. Schwenk (Editors), John Wiley and Sons, New York, 1988, pp. 193–206.
- [166] S.A. Burr, P. Erd˝s, R.L. Graham, and V.T. S´os: Maximal antiramsey graphs and the strong chromatic number, J. Graph Theory 13 (1989), 263–282.
- [167] S.A. Burr, P. Erd˝s, and L. Lova´sz: On graphs of Ramsey type. Ars Combinatoria 1 (1) (1976) 167–190.
- [168] Sebasti´an Bustamante, H. H`an, and Maya Stein: Almost partitioning 2-coloured complete 3-uniform hypergraphs into two monochromatic tight or loose cycles. arXiv:1701.07806v1.
- [169] S. Bustamante, Jan Corsten, N´ora Frankl, Alexey Pokrovskiy, and J. Skokan: Partitioning edge-coloured hypergraphs into few monochromatic tight cycles, Arxiv 1903.04771v1 (2019)
- [170] Louis Caccetta and Roland H¨aggkvist: On diameter critical graphs, Discrete Math. 28 (1979) 223–229.
- [171] Dominic de Caen: The current status of Tur´an’s problem on hypergraphs, Extremal problems for ﬁnite sets (Visegra´d, 1991), 187–197, Bolyai Soc. Math. Stud. 3 (1994), J´anos Bolyai Math. Soc., Budapest.
- [172] Dominic de Caen and Zolta´n Fu¨redi: The maximum size of 3-uniform hypergraphs not containing a Fano plane, Journal of Combinatorial Theory. Series B 78 (2000), 274–276.
- [173] Peter J. Cameron: ‘Portrait of a typical sum-free set’, Surveys in combinatorics, London Mathematical Society Lecture Note 123 (ed. C. Whitehead; Cambridge University Press, Cambridge, 1987) 13–42.
- [174] Peter J. Cameron and P. Erd˝s: ‘Notes on sum-free and related sets’, Recent trends in combinatorics (M´trah´aza, 1995), Combinatorics, Probability and Computing 8 (Cambridge University Press, Cambridge, 1999) 95–107.
- [175] Paul A. Catlin: Subgraphs of graphs I., Discrete Math. 10 (1974), 225–233.
- [176] Chan, Tsz Ho, Ervin Gyo˝ri, and Andr´as S´ark¨ozy: On a problem of Erd˝s on integers, none of which divides the product of k others. European J. Combin. 31 (1) (2010) 260–269.
- [177] Phong Chˆau, Louis DeBiasio, and Henry A. Kierstead: Po´sa’s conjecture for graphs of order at least 8 × 109, Random Struct Algorithms 39 (4) (2011), 507–525.
- [178] Sarvadaman Chowla: Solution of a problem of Erd˝s and Tur´an in additive-


- number theory. Proc. Nat. Acad. Sci. India. Sect. A 14 (1–2) (1944).
- [179] Maria Chudnovsky, Neil Robertson, Paul Seymour, and Robin Thomas: The strong perfect graph theorem. Ann. of Math. 164 (2006) 51–229.
- [180] Fan R.K. Chung: Quasi-random classes of hypergraphs. Random Struct. Algorithms 1 (1980) 363–382 MR1138430 Corrigendum: Quasi-random classes of hypergraphs, Random Struct Algorithms 1 (1990), 363–382.
- [181] F.R.K. Chung: Regularity lemmas for hypergraphs and quasi-randomness. Random Structures and Algorithms 2 (2) (1991) 241–252.
- [182] F.R.K. Chung: Quasi-random hypergraphs revisited. Random Structures and Algorithms 40 (1) (2012), 39–48.
- [183] F.R.K. Chung and R.L. Graham: Quasi-random tournaments. J. Graph Theory 15 (2) (1991), 173–198.
- [184] F.R.K. Chung and R.L. Graham: Quasi-random subsets of Zn, J. Combin. Theory Ser. A 61 (1) (1992), 64–86.
- [185] F.R.K. Chung, R.L. Graham, and Richard M. Wilson: Quasi-random graphs, Combinatorica 9 (1989), 345–362.
- [186] Vaclav Chva´tal: Tree-complete graph Ramsey numbers. J. Graph Theory 1 (1)

(1977), 93.

- [187] V. Chva´tal, V. Ro¨dl, E. Szemere´di, and W. Tom Trotter Jr.: The Ramsey number of a graph with bounded maximum degree, J. Combin. Theory Ser. B 34 (3) (1983) 239–243.
- [188] V. Chva´tal and E. Szemere´di: On the Erd˝s-Stone Theorem, J. London Math. Soc. (2) 23 (1981/2), 207–214.
- [189] Javier Cilleruelo: Inﬁnite Sidon sequences. Advances Math. 255 (2014), 474– 486.
- [190] J. Cilleruelo and Craig Timmons: k-fold Sidon sets. Electron. J. Combin. 21

(4) (2014) Paper 4.12, 9 pp.

- [191] Sebastian M. Cioab˘: Bounds on the Tur´an density of PG3(2), Electronic J. Combin. 11 (2004) 1–7.
- [192] David Conlon: Hypergraph packing and sparse bipartite Ramsey numbers, Combin. Probab. Comput. 18 (2009) 913-923.
- [193] D. Conlon: Combinatorial theorems relative to a random set, in: Proceedings of the International Congress of Mathematicians, Vol. IV (2014), 303–327. 2014.
- [194] D. Conlon and Jacob Fox: Bounds for graph regularity and removal lemmas, Geom. Funct. Anal. 22 (2012) 1191–1256.
- [195] D. Conlon and J. Fox: Graph removal lemmas, Surveys in combinatorics 2013, Vol. 409,London Mathematical Society Lecture Note Series, Cambridge University Press, Cambridge, (2013), 1–49.
- [196] D. Conlon, J. Fox, and B. Sudakov: On two problems in graph Ramsey theory, Combinatorica 32 (2012), 513–535.
- [197] D. Conlon, J. Fox, and B. Sudakov: Hereditary quasirandomness without regularity. Math. Proc. Cambridge Philos. Soc. 164 (3) (2018), 385–399. Pending
- [198] D. Conlon, J. Fox, and Yufei Zhao: Extremal results in sparse pseudorandom graphs. Advances Math., 256 (2014), 206–290.
- [199] D. Conlon and W. Timothy Gowers: Combinatorial theorems in sparse random sets, Ann. of Math. (2) 184 (2) (2016) 367–454.
- [200] D. Conlon, W.T. Gowers, W. Samotij, and M. Schacht: On the K LR conjecture in random graphs. Israel J. Math., 203 (2014), 535–580.
- [201] D. Conlon and M. Stein: Monochromatic cycle partitions in local edge colorings. J. Graph Theory 81 (2) (2016), 134–145.


- [202] O. Cooley: Proof of the Loebl-Komlo´s-So´s conjecture for large, dense graphs, Discrete Math., 309 (2009), 6190–6228.
- [203] O. Cooley, D. Ku¨hn, and D. Osthus: Perfect packings with complete graphs minus an edge, European J. Combin., 28 (2007), 2143–2155.
- [204] O. Cooley and R. Mycroft: The minimum vertex degree for an almost-spanning tight cycle in a 3-uniform hypergraph. Discrete Math. 340 (6) (2017), 1172– 1179.
- [205] Joshua N. Cooper: Quasirandom permutations. J. Combin. Theory Ser. A 106

(1) (2004), 123–143.

- [206] Jeﬀ Cooper, Kunal Dutta, and Dhruv Mubayi: Counting independent sets in hypergraphs. Combin. Probab. Comput. 23 (4) (2014), 539–550.
- [207] Jeﬀ Cooper and Dhruv Mubayi: Counting independent sets in triangle-free graphs, Proc. Amer. Math. Soc. 142 (10) (2014) 3325–3334,
- [208] J. Cooper and D. Mubayi: Sparse hypergraphs with low independence numbers, Combinatorica, 37 (1) (2017), 31–40.
- [209] Kereszte´ly Corr´adi and Andr´as Hajnal: On the maximal number of independent circuits in a graph, Acta Math. Acad. Sci. Hungar 14 (1963) 423–439.
- [210] Ernie Croot, Vsevolod F. Lev, and Pe´ter Pa´l Pach: Progression-free sets in Zn4 are exponentially small. Ann. of Math. (2) 185 (1) (2017) 331–337.
- [211] Be´la Csaba: The Bollob´s-Eldridge conjecture for graphs of maximum degree four. Manuscript (2003).
- [212] B. Csaba: On the Bolloba´s-Eldridge conjecture for bipartite graphs. Combin. Probab. Comput 16 (2007), 661–691.
- [213] B. Csaba: Regular spanning subgraphs of bipartite graphs of high minimum degree. Electron. J. Combin. 14 (1) (2007), Note 21, 7 pp.
- [214] B. Csaba: On embedding well-separable graphs. Discrete Math. 308 (19)

(2008), 4322–4331.

- [215] B. Csaba, Ian Levitt, Judit Nagy-Gyo¨rgy, and E. Szemere´di: Tight bounds for embedding bounded degree trees, in Fete of Combinatorics and Computer Science, Bolyai Soc. Math. Stud. 20, J´anos Bolyai Math. Soc., Budapest, 2010, pp. 95–137.
- [216] B. Csaba and Marcello Mydlarz: Approximate multipartite version of the Hajnal-Szemere´di theorem. J. Combin. Theory Ser. B 102 (2) (2012), 395–410.
- [217] B. Csaba, Ali Shokoufandeh, and E. Szemere´di: Proof of a conjecture of Bolloba´s and Eldridge for graphs of maximum degree three. Paul Erd˝s and his mathematics (Budapest, 1999). Combinatorica 23 (1) (2003), 35–72.
- [218] Andrzej Czygrinow and Louis DeBiasio: A note on bipartite graph tiling. SIAM J. Discrete Math. 25 (4) (2011), 1477–1489.
- [219] A. Czygrinow, L. DeBiasio, H.A. Kierstead, and T. Molla: An extension of the Hajnal-Szemere´di theorem to directed graphs. Combin. Probab. Comput. 24

(5) (2015), 754–773.

- [220] A. Czygrinow, DeBiasio, Louis; Molla, Theodore; Treglown, Andrew: Tiling directed graphs with tournaments. Forum Math. Sigma 6 (2018), e2, 53 pp.
- [221] A. Czygrinow, L. DeBiasio, and Brendan Nagle: Tiling 3-uniform hypergraphs with K43 − 2e. J. Graph Theory 75 (2) (2014), 124–136.
- [222] A. Czygrinow, Vikram Kamat: Tight co-degree condition for perfect matchings in 4-graphs. Electron. J. Combin. 19 (2) (2012) Paper 20, 16 pp.
- [223] A. Czygrinow, H.A. Kierstead, and T. Molla: On directed versions of the Corr´adi-Hajnal corollary. European J. Combin. 42 (2014) 1–14.
- [224] A. Czygrinow, T. Molla: Tight codegree condition for the existence of loose


- Hamilton cycles in 3-graphs, SIAM J. Discrete Math. 28 (2014) 67–76.
- [225] A. Czygrinow, S. Poljak, and V. Ro¨dl: Constructive quasi-Ramsey numbers and tournament ranking, SIAM J. Discrete Math 12 (1999), 48–63.
- [226] S. Das and T. Tran: Removal and stability for Erd˝s-Ko-Rado. SIAM J. Discrete Math. 30 (2) (2016), 1102–1114.
- [227] Giuliana Davidoﬀ, Peter Sarnak, and Alain Valette: Elementary number theory, group theory, and Ramanujan graphs, London Math. Soc. Stud. Texts 55, Cambridge University Press, Cambridge 2003.
- [228] Evan Davies, Matthew Jenssen, Will Perkins, and Barnaby Roberts: On the average size of independent sets in triangle-free graphs. Proc. Amer. Math. Soc. 146 (1) (2018), 111–124.
- [229] David Daykin and R. H¨aggkvist: Degrees giving independent edges in a hypergraph, Bull. Austral. Math. Soc., 23 (1981), 103–109.
- [230] L. DeBiasio, Saﬁ Faizullah, and Imdadullah Khan: Ore-degree threshold for the square of a Hamiltonian cycle. Discrete Math. Theor. Comput. Sci. 17 (1)

(2015), 13–32.

- [231] Louis DeBiasio and Tao Jiang: On the co-degree threshold for the Fano plane. European J. Combin. 36 (2014), 151–158.
- [232] L. DeBiasio and Luke L. Nelsen: Monochromatic cycle partitions of graphs with large minimum degree, Journal of Combinatorial Theory, Ser. B 122 (2017), 634–667.
- [233] Domingos Dellamonica, Kalyanasundaram Subrahmanyam, Daniel Martin, V. Ro¨dl and Asaf Shapira: An optimal algorithm for ﬁnding Frieze-Kannan regular partitions. Combin. Probab. Comput. 24 (2) (2015) 407–437.
- [234] Bobby DeMarco: Triangles in Random Graphs, thesis defense, Rutgers University, May 3, (2012).
- [235] B. DeMarco and Jeﬀ Kahn: Mantel’s theorem for random graphs. Random Structures and Algorithms 47 (1) (2015), 59–72.
- [236] B. DeMarco and J. Kahn: Tur´an’s theorem for random graphs, Submitted for publication, arXiv:1501.01340 (2015).
- [237] Tristan Denley: The independence number of graphs with large odd girth. Electron. J. Combin. 1 (1994), Research Paper 9, approx. 12 pp.
- [238] Walther A. Deuber, Alexander V. Kostochka, and Horst Sachs: A shorter proof of Dirac’s theorem on the number of edges in chromatically critical graphs, Diskretnyi Analiz Issledovanie Operacii 3 (4) (1996) 28–34 (in Russian).
- [239] Pat Devlin and Jeﬀ Kahn: On ”stability” in the Erd˝s-Ko-Rado theorem. SIAM J. Discrete Math. 30 (2) (2016), 1283–1289.
- [240] Palahenedi H. Diananda and Hian Poh Yap: Maximal sum-free sets of elements of ﬁnite groups, Proceedings of the Japan Academy 45 (1969), 1–5.
- [241] Rainer Dietmann, Christian Elsholtz, Katalin Gyarmati, and M. Simonovits: Shifted products that are coprime pure powers. J. Combin. Theory Ser. A 111

(1) (2005), 24–36.

- [242] Gabor A. Dirac: Some theorems on abstract graphs, Proc. London Math. Soc., 2 (1952), 68–81.
- [243] G.A. Dirac: A property of 4-chromatic graphs and some remarks on critical graphs, J. London Math. Soc. 27 (1952) 85–92.
- [244] G.A. Dirac: Extension of Tur´an’s theorem on graphs. Acta Math. Acad. Sci. Hungar 14 (1963) 417–422.
- [245] G.A. Dirac: The number of edges in critical graphs, J. Reine Angew. Math. 268/269 (1974) 150–164.


- [246] P. Drineas, P., A. Frieze, R. Kannan, S. Vempala, and V. Vinay: Clustering large graphs via the singular value decomposition. Mach. Learn. 56 (2004) 9–33.
- [247] Andrzej Dudek, C. Reiher, Andrzej Rucinski, and M. Schacht: Powers of Hamiltonian cycles in randomly augmented graphs, Arxiv:1805.10676v1, 2018 May 17
- [248] Richard A. Duke, H. Lefmann, and V. Ro¨dl: On uncrowded hypergraphs, In: Proceedings of the Sixth International Seminar on Random Graphs and Probabilistic Methods in Combinatorics and Computer Science, ”Random Graphs ’93” (Poznan´, 1993), Random Struct Algorithms 6 (1995), 209–212.
- [249] R.A. Duke and V. Ro¨dl: On graphs with small subgraphs of large chromatic number, Graphs Combin. 1 (1) (1985) 91–96.
- [250] Nancy Eaton: Ramsey numbers for sparse graphs, Discrete Math. 185 (1998) 63–75.
- [251] G´bor Elek and B. Szegedy: Limits of hypergraphs, removal and regularity lemmas. A non-standard approach, preprint. arXiv:0705.2179.
- [252] G. Elek and B. Szegedy: A measure-theoretic approach to the theory of dense hypergraphs. Advances Math. 231 (3-4) (2012), 1731–1772.
- [253] Gyo¨rgy Elekes: On the number of sums and products. Acta Arithmetica 81 (4)

(1997): 365–367.

- [254] Michael Elkin: An improved construction of progression-free sets. Israel J. Math. 184 (2011), 93–128. (See also: ACM-SIAM Symposium on Discrete Algorithms, SODA’10, Austin, TX, USA, (2010) pp. 886–905.
- [255] Jordan Ellenberg and Dion Gijswijt: On large subsets of Fnq with no three-term arithmetic progression. Ann. of Math. (2) 185 (1) (2017) 339–343.
- [256] David Ellis: Stability for t-intersecting families of permutations, J. Combin. Theory Ser. A 118 (2011) 208–227.
- [257] D. Ellis, Nathan Keller, and Noam Lifshitz: Stability versions of Erd˝s-Ko-Rado type theorems, via isoperimetry, arXiv:1604.02160 (2016).
- [258] Paul Erd˝s: On sequences of integers no one of which divides the product of two others and on some related problems, Mitt. Forsch.-Inst. Math. Mech. Univ. Tomsk 2 (1938) 74–82.
- [259] P. Erd˝s: On a problem of Sidon in additive number theory and on some related problems. Addendum, J. London Math. Soc. 19 (1944), 208.
- [260] P. Erd˝s: On sets of distances of n points, Amer. Math. Monthly 53 (1946), 248–250.
- [261] P. Erd˝s, ‘Some remarks on the theory of graphs’, Bull. Amer. Math. Soc. 53

(1947) 292–294.

- [262] P. Erd˝s: On a problem of Sidon in additive number theory, Acta Sci Math. Szeged 15 (1954), 255–259.
- [263] P. Erd˝s: Graph theory and probability. Canad. J. Math. 11 (1959) 34–38.
- [264] P. Erd˝s: Graph theory and probability. II. Canad. J. Math. 13 (1961) 346–352.
- [265] P. Erd˝s: On a theorem of Rademacher-Tur´an, Illinois J. Math. 6 (1962), 122–127.
- [266] P. Erd˝s: On extremal problems of graphs and generalized graphs, Israel J. Math. 2 (3) (1964) 183–190.
- [267] P. Erd˝s: Extremal problems in graph theory, in: M. Fiedler (Ed.), Theory of Graphs and Its Applications, 2nd ed., Proc. Symp., Smolenice, 1963, Academic Press, New York, 1965, pp. 29–36.
- [268] P. Erd˝s: A problem on independent r-tuples, Ann. Univ. Sci. Budapest. 8


(1965) 93–95.

- [269] P. Erd˝s: Some recent results on extremal problems in graph theory. Results, Theory of Graphs (Internat. Sympos., Rome, 1966), Gordon and Breach, New York; Dunod, Paris, (1967), pp. 117–123 (English); pp. 124–130 (French). ***
- [270] P. Erd˝s: On some applications of graph theory to geometry, Canad. J. Math. 19 (1967), 968–971.
- [271] P. Erd˝s: On some new inequalities concerning extremal properties of graphs. In Theory of Graphs (Proc. Colloq., Tihany, 1966), Academic Press, New York,

(1968), 77–81.

- [272] P. Erd˝s: On some applications of graph theory to number theoretic problems, Publ. Ramanujan Inst. No. (1968/1969), 131–136.
- [273] P. Erd˝s: Some applications of graph theory to number theory, The Many Facets of Graph Theory (Proc. Conf., Western Mich. Univ., Kalamazoo, Mich., 1968), pp. 77–82, Springer, Berlin, (1969).
- [274] P. Erd˝s: On the number of complete subgraphs and circuits contained in graphs. Casopisˇ Peˇst. Mat. 94 (1969) 290–296.
- [275] P. Erd˝s: Some applications of graph theory to number theory, Proc. Second Chapel Hill Conf. on Combinatorial Mathematics and its Applications (Univ. North Carolina, Chapel Hill, N.C., 1970), pp. 136–145,
- [276] P. Erd˝s: On the application of combinatorial analysis to number theory, geometry and analysis, Actes du Congre`s International des Mathe´maticiens (Nice, 1970), Tome 3, pp. 201–210, Gauthier-Villars, Paris, 1971.
- [277] P. Erd˝s: The Art of Counting. Selected writings of P. Erd˝os, (J. Spencer ed.) Cambridge, The MIT Press (1973).
- [278] P. Erd˝s, Some problems in graph theory, in: Hypergraph Seminar, Ohio State Univ., Columbus, Ohio, 1972, in: Lecture Notes in Math., vol. 411, Springer, Berlin, (1974), pp. 187–190.
- [279] P. Erd˝s: Problems and results in graph theory and combinatorial analysis, in: Proceedings of the Fifth British Combinatorial Conference, Univ. Aberdeen, Aberdeen, 1975, Congr. Numer. 15 (1976) 169–192.
- [280] P. Erd˝s: Paul Tur´an, 1910–1976: his work in graph theory, J. Graph Theory 1 (2) (1977) 97–101,
- [281] P. Erd˝s: Some personal reminiscences of the mathematical work of Paul Tur´an. Acta Arith. 37 (1980), 4–8.
- [282] P. Erd˝s: Some applications of Ramsey’s theorem to additive number theory, European J. Combin. 1 (1) (1980) 43–46.
- [283] P. Erd˝s: Some notes on Tur´an’s mathematical work. P. Tur´an memorial volume. J. Approx. Theory 29 (1) (1980), 2–5.
- [284] P. Erd˝s: Some applications of graph theory and combinatorial methods to number theory and geometry, Algebraic methods in graph theory, Vol. I, II (Szeged, 1978), Colloq. Math. Soc. J´anos Bolyai, 25, pp. 137–148, NorthHolland, Amsterdam-New York, 1981.
- [285] P. Erd˝s: Some old and new problems in combinatorial geometry, Applications of discrete mathematics (Clemson, SC, 1986), pp. 32–37, SIAM, Philadelphia, PA, 1988
- [286] P. Erd˝s: On some aspects of my work with Gabriel Dirac, in: L.D. Andersen,

I.T. Jakobsen, C. Thomassen, B. Toft, P.D. Vestergaard (Eds.), Graph Theory in Memory of G.A. Dirac, Annals of Discrete Mathematics, Vol. 41, NorthHolland, Amsterdam, 1989, pp. 111–116.

- [287] P. Erd˝s: On some of my favourite theorems. Combinatorics, Paul Erd˝s is eighty, Vol. 2 (Keszthely, 1993), 97–132, Bolyai Soc. Math. Stud., 2, J´anos


- Bolyai Math. Soc., Budapest, 1996.
- [288] P. Erd˝s, P. Frankl, and V. Ro¨dl: The asymptotic number of graphs not containing a ﬁxed subgraph and a problem for hypergraphs having no exponent, Graphs Combin., 2 (1986), 113–121.
- [289] P. Erd˝s and Tibor Gallai: On maximal paths and circuits of graphs, Acta Math. Sci. Hungar. 10 (1959) 337–356.
- [290] P. Erd˝s, A.W. Goodman, and Lajos Po´sa: The representation of a graph by set intersections, Canad. J. Math, 18 (1966), 106–112.
- [291] P. Erd˝s, A. Gya´rfa´s, and L´aszl´o Pyber: Vertex coverings by monochromatic cycles and trees, J. Combin. Theory Ser. B 51 (1991) 90–95.
- [292] P. Erd˝s, A. Hajnal, M. Simonovits, V.T. S´os, and E. Szemere´di: Tur´an-Ramsey theorems and simple asymptotically extremal structures, Combinatorica 13

(1993), 31–56.

- [293] P. Erd˝s, A. Hajnal, M. Simonovits, V.T. S´os, and E. Szemere´di: Tur´an-Ramsey theorems and Kp-independence number, in: Combinatorics, geometry and probability (Cambridge, 1993), Cambridge Univ. Press, Cambridge, 1997, 253–281.
- [294] P. Erd˝s, A. Hajnal, M. Simonovits, V.T. S´os, and E. Szemere´di: Tur´an-Ramsey

theorems and Kp-independence numbers, Combin. Probab. Comput. 3 (1994) 297–325.

- [295] P. Erd˝s, A. Hajnal, V.T. S´os, and E. Szemere´di: More results on Ramsey-Tur´an type problem, Combinatorica 3 (1983), 69–81.
- [296] P. Erd˝s and Haim Hanani: On a limit theorem in combinatorial analysis, Publ. Math. Debrecen 10 (1963) 10–13.
- [297] P. Erd˝s, Daniel J. Kleitman, and Bruce L. Rothschild: Asymptotic enumeration of Kn-free graphs, in Colloquio Internazionale sulle Teorie Combinatorie, Tomo II, Atti dei Convegni Lincei, no. 17 (Accad. Naz. Lincei, Rome) (1976), 19–27.
- [298] P. Erd˝s, Chao Ko, and Richard Rado: Intersection theorems for systems of ﬁnite sets, Quart. J. Math. Oxford Ser. (2), 12 (1961), 313–320.
- [299] P. Erd˝s and L. Lova´sz: Problems and results on 3-chromatic hypergraphs and some related questions, A. Hajnal (Ed.), Inﬁnite and Finite Sets, North Holland, 1975, pp. 609–628.
- [300] P. Erd˝s, Amram Meir, V.T. S´os, and P. Tur´an: On some applications of graph theory II, Studies in Pure Mathematics (presented to R. Rado), Academic Press, London, (1971) pp. 89-99.
- [301] P. Erd˝s, A. Meir, V.T. S´os, and P. Tur´an: On some applications of graph theory I, Discrete Math. 2 (3) (1972) 207–228.
- [302] P. Erd˝s, A. Meir, V.T. S´os, and P. Tur´an: On some applications of graph theory III, Canadian Math. Bull. 15 (1972) 27–32.
- [303] P. Erd˝s, A. Meir, V.T. S´os, and P. Tur´an, Corrigendum: ‘On some applications of graph theory, I’. [Discrete Math. 2 (3) (1972) 207–228],; Discrete Math. 4

(1973) 90.

- [304] P. Erd˝s, S.B. Rao, M. Simonovits, and V.T. S´os: On totally supercompact graphs. Combinatorial mathematics and applications (Calcutta, 1988). Sankhya Ser. A 54 (1992), Special Issue, 155–167.
- [305] P. Erd˝s and Alfre´d Re´nyi: Additive properties of random sequences of positive integers, Acta Arith. 6 (1960) 83–110.
- [306] P. Erd˝s and A. Re´nyi: On the evolution of random graphs. Magyar Tud. Akad. Mat. Kut. Int. K¨zl. 5 (1960) 17–61. (Also see [277], 574–617)
- [307] P. Erd˝s, A. Re´nyi: On the strength of connectedness of a random graph, Acta Math. Acad. Sci. Hungar. 12 (1961) 261–267.


- [308] P. Erd˝s, A. Re´nyi, and V.T. S´os: On a problem of graph theory. Stud. Sci. Math. Hung. 1 (1966) 215–235 (Also see [277], 201–221)
- [309] P. Erd˝s and C. Ambrose Rogers: ‘The construction of certain graphs’, Canad. J. Math. 14 (1962) 702–707.
- [310] P. Erd˝s and H. Sachs: Regul¨are Graphen gegebener Taillenweite mit minimaler Knotenzahl. (German) Wiss. Z. Martin-Luther-Univ. Halle-Wittenberg Math.Natur. Reihe 12 (1963) 251–257.
- [311] P. Erd˝s, Andr´as S´ark¨ozy, and V.T. S´os: On product representations of powers, I, European J. Combin. 16 (1995) 567–588.
- [312] P. Erd˝s and M. Simonovits: A limit theorem in graph theory, Studia Sci. Math. Hungar. 1 (1966) 51–57. (Reprinted in [277], 1973, pp. 194–200.).
- [313] P. Erd˝s and M. Simonovits: Some extremal problems in graph theory, Combinatorial theory and its applications, Vol. I, Proceedings Colloqium, Balatonfu¨red, (1969), North-Holland, Amsterdam, 1970, pp. 377–390.(Reprinted in [277]).
- [314] P. Erd˝s and M. Simonovits: An extremal graph problem, Acta Math. Acad. Sci. Hungar. 22 (1971/72), 275–282.
- [315] P. Erd˝s and M. Simonovits: On the chromatic number of Geometric graphs, Ars Combin. 9 (1980) 229–246.
- [316] P. Erd˝s and M. Simonovits: Supersaturated graphs and hypergraphs, Combinatorica 3 (1983) 181–192.
- [317] P. Erd˝s and M. Simonovits: Cube supersaturated graphs and related problems, in: J.A. Bondy, U.S.R. Murty (Eds.), Progress in Graph Theory, Acad. Press, 203–218 (1984)
- [318] P. Erd˝s and M. Simonovits: How many colours are needed to colour every pentagon of a graph in ﬁve colours? (manuscript, to be published)
- [319] P. Erd˝s and V.T. S´os: Some remarks on Ramsey’s and Tur´an’s theorem, in: Combinatorial theory and its applications, II (Proc. Colloq., Balatonfu¨red, 1969), North-Holland, Amsterdam, (1970), 395–404.
- [320] P. Erd˝s and J. Spencer: Probabilistic methods in combinatorics, Probability and Mathematical Statistics, Vol. 17, Academic, New York, London, (1974),
- [321] P. Erd˝s and Arthur H. Stone: On the structure of linear graphs, Bull. Amer. Math. Soc. 52 (1946) 1087–1091.
- [322] P. Erd˝s and E. Szemere´di: On sums and products of integers. In: Studies in Pure Mathematics, Birkh¨auser, Basel, 213–218 (1983).
- [323] P. Erd˝s and P. Tur´an: On some sequences of integers, J. London Math. Soc. 11 (1936), 261–264.
- [324] P. Erd˝s and P. Tur´an: On a problem of Sidon in additive number theory, and on some related problems, J. London Math. Soc. 16 (1941), 212–215. Addendum (by P. Erd˝s) J. London Math. Soc. 19 (1944), 208.
- [325] Beka Ergemlidze, Ervin Gyo˝ri, and Abhishek Methuku: A note on the linear cycle cover conjecture of Gya´rfa´s and S´ark¨ozy. Electron. J. Combin. 25 (2)

(2018), Paper 2.29, 4 pp.

- [326] Vance Faber: The Erd˝s-Faber-Lova´sz conjecture-the uniform regular case. J. Combin. 1 (2) (2010), 113–120.
- [327] V. Faber and L. Lova´sz: Unsolved problem #18, page 284 in Hypergraph Seminar, Ohio State University, 1972, edited by C. Berge and D. Ray-Chaudhuri.
- [328] Genghua Fan: On diameter 2-critical graphs, Discrete Math., 67 (3) (1987) 235–240
- [329] G. Fan and R. H¨aggkvist: The square of a Hamiltonian cycle, SIAM J. Discrete


- Math. (1994) 203–212.
- [330] G. Fan and H.A. Kierstead: The square of paths and cycles, Journal of Combinatorial Theory, Ser. B, 63 (1995), 55–64.
- [331] R.J. Faudree, Ronald J. Gould, Mike S. Jacobson, and Richard H. Schelp: On a problem of Paul Seymour, Recent Advances in Graph Theory (V. R. Kulli ed.), Vishwa International Publication (1991), 197–215.
- [332] R.J. Faudree, R.H. Schelp: All Ramsey numbers for cycles in graphs. Discrete Math. 8 (1974) 313–329.
- [333] R.J. Faudree and R.H. Schelp: Ramsey type results, in: A. Hajnal, et al. (Eds.), Inﬁnite and Finite Sets, in: Colloq. Math. J. Bolyai, vol. 10, North-Holland, Amsterdam, (1975) pp. 657–665.
- [334] R. J. Faudree and R.H. Schelp: Path Ramsey numbers in multicolorings, Journal of Combinatorial Theory, Ser. B 19 (1975), 150–160.
- [335] R.J. Faudree and R.H. Schelp: Path-path Ramsey-type numbers for the complete bipartite graph, J. Combin. Theory Ser. B 19, (1975), 161–173.
- [336] R.J. Faudree and M. Simonovits: Ramsey problems and their connection to Tur´an-type extremal problems. J. Graph Theory 16 (1992) 25–50.
- [337] Odile Favaron, Evelyne Flandrin, Hao Li, and Feng Tian: An Ore-type condition for pancyclability, Discrete Math. 206 (1999), 139–144.
- [338] Asaf Ferber, Gal Kronenberg, and Eoin Long: Packing, Counting and Covering Hamilton cycles in random directed graphs. Electron. Notes Discrete Math. 49

(2015) 813–819.

- [339] A. Ferber, Rajko Nenadov, Andreas Noever, Ueli Peter, and N. Skoric´:ˇ Robust hamiltonicity of random directed graphs, Proceedings of the 26th Annual ACMSIAM Symposium on Discrete Algorithms (SODA 15) (2015), 1752–1758.
- [340] A. Ferber, Rajko Nenadov, and U. Peter: Universality of random graphs and rainbow embedding, Random Structures and Algorithms 48 (2016), 546–564.
- [341] Agnieszka Figaj and Tomasz  Luczak: The Ramsey number for a triple of long even cycles. J. Combin. Theory Ser. B 97 (4) (2007) 584–596
- [342] A. Figaj and T.  Luczak: The Ramsey Numbers for A Triple of Long Cycles. Combinatorica 38 (4) (2018), 827–845.
- [343] David C. Fisher: Lower bounds on the number of triangles in a graph. J. Graph Theory 13 (1989) 505–512.
- [344] Mathew Fitch: Rational exponents for hypergraph Tur´an problems. arXiv:1607.05788
- [345] G. Fiz Pontiveros, Simon Griﬃths, R. Morris: The triangle-free process and R(3, k), arXiv:1302.6279.
- [346] Dmitrii G. Fon-Der-Flaass: “Method for Construction of (3,4)-Graphs”, Mat. Zametki 44 (4) (1998), 546–550; [Math. Notes 44, 781–783 (1988)].
- [347] Jacob Fox: A new proof of the graph removal lemma, Ann. of Math. 174 (2011) 561–579.
- [348] J. Fox, Mikhail Gromov, Vincent Laﬀorgue. Assaf Naor, and J. Pach: Overlap properties of geometric expanders. J. Reine Angew. Math. 671 (2012), 49–83.
- [349] J. Fox, Po-Shen Loh, and Yufei Zhao: The critical window for the classical Ramsey-Tur´an problem. Combinatorica 35 (4) (2015) 435–476.
- [350] J. Fox, L´aszl´o Mikl´os Lova´sz, and Yufei Zhao: On regularity lemmas and their algorithmic applications. Combin. Probab. Comput. 26 (4) (2017), 481–505.
- [351] J. Fox, J. Pach, and Andrew Suk: Density and regularity theorems for semi-algebraic hypergraphs. Proceedings of the Twenty-Sixth Annual ACMSIAM Symposium on Discrete Algorithms, 1517–1530, SIAM, Philadelphia, PA,


- (2015).
- [352] J. Fox and B. Sudakov: Density theorems for bipartite graphs and related Ramsey-type results, Combinatorica 29 (2009) 153–196.
- [353] J. Fox and B. Sudakov: Dependent random choice, Random Structures and Algorithms 38 (2011) 68–99.
- [354] Peter Frankl: All rationals occur as exponents, J. Combin. Theory Ser. A 42

(1985) 200–206.

- [355] P. Frankl and Z. Fu¨redi: An exact result for 3-graphs, Discrete Math. 50 (1984) 323–328.
- [356] P. Frankl and V. Ro¨dl: Hypergraphs do not jump, Combinatorica 4 (1984), 149–159.
- [357] P. Frankl and V. Ro¨dl: Near perfect coverings in graphs and hypergraphs, European Journal of Combinatorics 6 (1985), 317–326.
- [358] P. Frankl and V. Ro¨dl: The uniformity lemma for hypergraphs. Graphs Combin. 8 (4) (1992) 309–312.
- [359] P. Frankl and R.M. Wilson: Intersection theorems with geometric consequences, Combinatorica 1 (1981) 357–368.
- [360] Mike Freedman, L. Lova´sz, and Alex Schrijver: Reﬂection positivity, rank connectivity, and homomorphism of graphs. J. AMS 20 (2007), 37–51.
- [361] G.A. Freiman: Foundations of a structural theory of set addition, Kazan Gos. Ped. Inst., Kazan, 1966 (Russian). English translation in Translations of Mathematical Monographs 37, American Mathematical Society, Providence, 1973.
- [362] Ehud Friedgut: On the measure of intersecting families, uniqueness and stability; Combinatorica 28 (5) (2008), 503–528.
- [363] Joel Friedman and Nick Pippenger: Expanding graphs contain all small trees, Combinatorica 7 (1987), 71–76.
- [364] Alan Frieze and Ravi Kannan: The Regularity Lemma and approximation schemes for dense problems, Proc IEEE Symp Found Comput Sci, 1996, pp. 12–20.
- [365] A. Frieze and R. Kannan: Quick approximation to matrices and applications, Combinatorica 19 (1999), 175–220.
- [366] A. Frieze and R. Kannan: A simple algorithm for constructing Szemere´di’s regularity partition. Electron. J. Combin., 6, (1999). 74
- [367] A. Frieze, R. Kannan, and Santosh Vempala: Fast Monte-Carlo algorithms for ﬁnding low-rank approximations. J. ACM 51 (6) (2004), 1025–1041.
- [368] Shinya Fujita, Henry Liu, and Colton Magnant: Monochromatic structures in edge-coloured graphs and hypergraphs-a survey, International Journal of Graph Theory and its Applications, 1 (1) (2015) pp3–56.
- [369] Zolta´n Fu¨redi: Matchings and covers in hypergraphs, Graphs Combin. 4 (1988) 115–206.
- [370] Z. Fu¨redi: Tur´an type problems, in Surveys in Combinatorics (1991), Proc. of the 13th British Combinatorial Conference, (A. D. Keedwell ed.) Cambridge Univ. Press. London Math. Soc. Lecture Note Series 166 (1991), 253–300.
- [371] Z. Fu¨redi: The maximum number of edges in a minimal graph of diameter 2, J. Graph Theory 16 (1992) 81–98.
- [372] Z. Fu¨redi: Extremal hypergraphs and combinatorial geometry, in: Proc. Internat. Congress of Mathematicians, vols. 1, 2, Zu¨rich, 1994, Birkh¨auser, Basel,

(1995), pp. 1343–1352.

- [373] Z. Fu¨redi: An upper bound on Zarankiewicz’ problem. Combin. Probab. Comput. 5 (1996) 29–33


- [374] Z. Fu¨redi: A proof of the stability of extremal graphs, Simonovits’ stability from Szemere´di’s regularity. J. Combin. Theory Ser. B 115 (2015), 66–71.
- [375] Z. Fu¨redi, Alexander Kostochka, and Ruth Luo: A stability version for a theorem of Erd˝s on nonhamiltonian graphs. Discrete Math. 340 (11) (2017), 2688–2690.
- [376] Z. Fu¨redi, A. Kostochka, Ruth Luo, and J. Verstrae¨te: Stability in the Erd˝sGallai Theorem on cycles and paths, II. Discrete Math. 341 (5) (2018), 1253– 1263.
- [377] Z. Fu¨redi, A. Kostochka, and J. Verstrae¨te: Stability in the Erd˝s-Gallai theorems on cycles and paths. J. Combin. Theory Ser. B 121 (2016), 197–228.
- [378] Z. Fu¨redi and Andre´ Ku¨ndgen: Tur´an problems for weighted graphs, J. Graph Theory 40 (2002), 195–225.
- [379] Z. Fu¨redi, D. Mubayi, and O. Pikhurko: Quadruple systems with independent neighborhoods. J. Combin. Theory Ser. A 115 (8) (2008), 1552–1560.
- [380] Z. Fu¨redi, O. Pikhurko, and M. Simonovits: The Tur´an density of the hypergraph {abc, ade,bde, cde}. Electronic J. Combin. 10 # R18 (2003)
- [381] Z. Fu¨redi, O. Pikhurko, and M. Simonovits: On triple systems with independent neighbourhoods, Combin. Probab. Comput. 14 (5-6) (2005), 795–813,
- [382] Z. Fu¨redi, O. Pikhurko, and M. Simonovits: 4-books of three pages. J. Combin. Theory Ser. A 113 (5) (2006), 882–891.
- [383] Z. Fu¨redi and M. Ruszink´o: Uniform hypergraphs containing no grids. Advances Math. 240 (2013), 302–324.
- [384] Z. Fu¨redi and A. Sali: Some new bounds on partition critical hypergraphs. European J. Combin. 33 (5) (2012), 844–852.
- [385] Z. Fu¨redi and M. Simonovits: Triple systems not containing a Fano conﬁguration, Combin. Probab. Comput. 14 (4) (2005), 467–484.
- [386] Z. Fu¨redi and M. Simonovits: The history of degenerate (bipartite) extremal graph problems, in Erd˝s Centennial, Bolyai Soc. Math. Stud., 25, J´anos Bolyai Math. Soc., Budapest, (2013) 169–264. arXiv:1306.5167.
- [387] Hillel Fu¨rstenberg: Ergodic behavior of diagonal measures and a theorem of Szemere´di on arithmetic progressions, J. Analyse Math. 31 (1977), 204–256.
- [388] H. Fu¨rstenberg and Yitzhak Katznelson: An ergodic Szemere´di theorem for commuting transformations, J. Analyse Math. 34 (1978) 275–291.
- [389] H. Fu¨rstenberg and Y. Katznelson: A density version of the Hales-Jewett theorem, J. Analyse Math. 57 (1991), 64–119.
- [390] L´aszl´o Gerencse´r and Andr´as Gya´rfa´s: On Ramsey-type problems, Ann. Univ. Sci. Budapest. Eo¨tv¨os Sect. Math., 10 (1967), 167–170.
- [391] Stefanie Gerke, Y. Kohayakawa, V. Ro¨dl, and A. Steger: Small subsets inherit sparse ε-regularity, J. Combin. Theory Ser. B 97 (1) (2007) 34–56.
- [392] S. Gerke and A. Steger: The sparse regularity lemma and its applications, in: B.S. Webb (Ed.), Surveys Combinatorics 2005, University of Durham, 2005, in: London Math. Soc. Lecture Note Ser., vol. 327, Cambridge Univ. Press, Cambridge, 2005, pp. 227–258.
- [393] Alfred Geroldinger and Imre Z. Ruzsa: Combinatorial number theory and additive group theory. Courses and seminars from the DocCourse in Combinatorics and Geometry held in Barcelona, 2008. Advanced Courses in Mathematics. CRM Barcelona. Birkh¨auser Verlag, Basel, 2009. xii+330 pp. ISBN: 978-3-7643-8961-1
- [394] Roman Glebov, Y. Person, and Wilma Weps: On extremal hypergraphs for Hamiltonian cycles. European J. Combin. 33 (4) (2012) 544–555.
- [395] Stephan Glock, D. Ku¨hn, Allan Lo, R. Montgomery, and D. Osthus: On the


- decomposition threshold of a given graph, arXiv:1603.04724, 2016.
- [396] S. Glock, D. Ku¨hn, Allan Lo, and D. Osthus: The existence of designs via iterative absorption, arXiv:1611.06827, (2016).
- [397] S. Glock, D. Ku¨hn, Allan Lo, and D. Osthus: Hypergraph F-designs for arbitrary F, arXiv:1706.01800, (2017).
- [398] S. Glock, D. Ku¨hn, and D. Osthus: Optimal path and cycle decompositions of dense quasirandom graphs. J. Combin. Theory Ser. B 118 (2016), 88–108.
- [399] O. Goldreich, S. Goldwasser and D. Ron: Property testing and its connection to learning and approximation, Journal of the ACM 45 (1998), 653–750.
- [400] Adolph W. Goodman: On sets of acquaintances and strangers at any party. Amer. Math. Monthly 66 (1959) 778–783.
- [401] W. Timothy Gowers: Lower bounds of tower type for Szemere´di’s uniformity lemma, GAFA, Geom. Func. Anal. 7 (1997), 322–337.
- [402] W.T. Gowers: A new proof of Szemere´di’s theorem for arithmetic progressions of length four, Geom. Funct. Anal. 8 (1998), 529–551. MR 1631259 132, 138 MR1631259 // A new proof of Szemere´di’s theorem, Geom. Funct. Anal. 11

(2001), 465–588; Erratum, Geom Funct. Anal. 11 (2001), 869

- [403] W.T. Gowers: Quasirandomness, counting and regularity for 3-uniform hypergraphs, Combinatorics, Probability and Computing 15 (2006), 143–184.
- [404] W.T. Gowers: Hypergraph regularity and the multidimensional Szemere´di theorem, Ann. of Math. (2) 166 (3) (2007) 897–946.
- [405] W.T. Gowers: Quasirandom groups. Combin. Probab. Comput. 17, (2008) 363–387
- [406] W.T. Gowers: Polymath and the density Hales-Jewett theorem. An irregular mind, 659–687, Bolyai Soc. Math. Stud., 21, J´anos Bolyai Math. Soc., Budapest,

(2010).

- [407] W.T. Gowers: A Geometric Ramsey Problem, http://mathoverﬂow.net/ questions/50928/a-geometric-ramsey-problem, accessed May 2016.
- [408] W.T. Gowers and Omid Hatami: Inverse and stability theorems for approximate representations of ﬁnite groups, arXiv:1510.04085 [math.GR].
- [409] R.L. Graham and B.L. Rothschild: Ramsey’s theorem for n-parameter sets, Trans. Amer. Math. Soc. 159 (1971), 257–292.
- [410] R.L. Graham, B.L. Rothschild, and J.H. Spencer: Ramsey Theory, Wiley, New York, 1990. 2nd edition
- [411] R.L. Graham, V. Ro¨dl, and A. Rucin´ski: On graphs with linear Ramsey numbers, J. Graph Theory 35 (2000) 176–192.
- [412] Andrew Granville and J´ozsef Solymosi: Sum-product formulae. Recent trends in combinatorics, 419–451, IMA Vol. Math. Appl., 159, Springer, [Cham], 2016.
- [413] J. Ben Green: The Cameron-Erd˝os conjecture, Bull. London Math. Soc. 36

(2004) 769–778.

- [414] J. B. Green: A Szemere´di-type regularity lemma in abelian groups, with applications, Geom. Funct. Anal. 15 (2) (2005) 340–376.
- [415] B. Green and I.Z. Ruzsa: Sum-free sets in abelian groups, Israel J. Math. 147

(2005), 157–188.

- [416] B. Green and T.C. Tao: The primes contain arbitrarily long arithmetic progressions, Annals of Mathematics 167 (2008), 481–547.
- [417] B. Green and T.C. Tao: New bounds for Szemere´di’s theorem. I. Progressions of length 4 in ﬁnite ﬁeld geometries. Proc. London Math. Soc. (3) 98 (2) (2009), 365–392.
- [418] B. Green and T.C. Tao: An arithmetic regularity lemma, an associated counting


- lemma, and applications. In: I. B´ar´any, J. Solymosi (eds.) An Irregular Mind. Bolyai Soc. Math. Stud., Vol. 21, pp. 261–334. J´anos Bolyai Mathematical Society, Budapest (2010)
- [419] B. Green and T.C. Tao: New bounds for Szemere´di’s theorem, III: a polylogarithmic bound for r4(N). Mathematika 63 (3) (2017) 944–1040.
- [420] B. Green and Julia Wolf: A note on Elkin’s improvement of Behrend’s construction. Additive number theory, 141–144, Springer, New York, 2010.
- [421] Jerrold R. Griggs, M. Simonovits, and G. Rubin Thomas: Extremal graphs with bounded densities of small graphs, J. Graph Theory 29 (1998), 185–207.
- [422] Andrey Grinshpun and G.N. S´ark¨ozy: Monochromatic bounded degree subgraph partitions, Discrete Math. 339 (2016) 46–53.
- [423] Andrzei Grzesik: On the maximum number of ﬁve-cycles in a triangle-free graph, J. Combin. Theory Ser. B 102 (5) (2012) 1061–1066.
- [424] A. Gya´rfa´s: Covering complete graphs by monochromatic paths, in: Irregularities of Partitions, in: Algorithms Combin., 8 (1989), Springer-Verlag, pp. 89–91.
- [425] A. Gya´rfa´s: Packing trees into n-chromatic graphs. Discuss. Math. Graph Theory 34 (1) (2014), 199–201.
- [426] A. Gya´rfa´s: Vertex covers by monochromatic pieces-a survey of results and problems. Discrete Math. 339 (7) (2016) 1970–1977. Arxiv 2015
- [427] A. Gya´rfa´s, E. Gyo˝ri, and M. Simonovits: On 3-uniform hypergraphs without linear cycles. J. Combin. 7 (1) (2016), 205–216.
- [428] A. Gya´rfa´s, G.N. S´ark¨ozy, and E. Szemere´di: Long monochromatic Berge cycles in colored 4-uniform hypergraphs. Graphs Combin. 26 (1) (2010) 71–76.
- [429] A. Gya´rfa´s and J. Lehel: Packing trees of diﬀerent order into Kn, in: Combinatorics, Proc. Fifth Hungarian Colloq., Keszthely, 1976, in: Colloq. Math. Soc. J´anos Bolyai, vol. 18, North-Holland, Amsterdam-New York, (1978), pp. 463–469,
- [430] A. Gya´rfa´s, J. Lehel, G. S´ark¨ozy, and R. Schelp: Monochromatic Hamiltonian Berge-cycles in colored complete uniform hypergraphs, J. Combin. Theory Ser. B 98 (2008) 342–358.
- [431] A. Gya´rfa´s, M. Ruszink´o, G.N. S´ark¨ozy, and E. Szemere´di: An improved bound for the monochromatic cycle partition number. J. Combin. Theory Ser. B 96

(6) (2006) 855–873.

- [432] A. Gya´rfa´s, M. Ruszink´o, G.N. S´ark¨ozy, and E. Szemere´di: Three-color Ramsey number for paths, Combinatorica 28 (4) (2008), 499–502; Corrigendum: ”Three-color Ramsey numbers for paths” [Combinatorica 27 (1) (2007) 35–69; MR2310787].
- [433] A. Gya´rfa´s and G.N. S´ark¨ozy: The 3-colour Ramsey number of a 3-uniform Berge cycle. Combin. Probab. Comput. 20 (1) (2011) 53–71.
- [434] A. Gya´rfa´s and G.N. S´ark¨ozy: Monochromatic path and cycle partitions in hypergraphs, Electronic Journal of Combinatorics, 20 (1) (2013) #P18.
- [435] A. Gya´rfa´s and G.N. S´ark¨ozy: Monochromatic loose-cycle partitions in hypergraphs, Electronic J. of Combinatorics 21 (2) (2014) P2.36.
- [436] A. Gya´rfa´s, G.N. S´ark¨ozy, and Stanley M. Selkow: Coverings by few monochromatic pieces: a transition between two Ramsey problems. Graphs Combin. 31

(1) (2015), 131–140.

- [437] A. Gya´rfa´s, G.N. S´ark¨ozy, and E. Szemere´di: The Ramsey number of diamondmatchings and loose cycles in hypergraphs. Electron. J. Combin. 15 (1) (2008), Research Paper 126, 14 pp.


- [438] A. Gya´rfa´s, G.N. S´ark¨ozy, and E. Szemere´di: Stability of the path-path Ramsey number. Discrete Math. 309 (13) (2009), 4590–4595.
- [439] A. Gya´rfa´s, G.N. S´ark¨ozy, and E. Szemere´di: Long monochromatic Berge cycles in colored 4-uniform hypergraphs. Graphs Combin. 26 (1) (2010), 71–76.
- [440] A. Gya´rfa´s, G.N. S´ark¨ozy, and E. Szemere´di: Monochromatic Hamiltonian 3tight Berge cycles in 2-colored 4-uniform hypergraphs. J. Graph Theory 63 (4)

(2010), 288–299.

- [441] Ervin Gyo˝ri: On the number of C5 in a triangle-free graph, Combinatorica 9

(1989) 101–102.

- [442] E. Gyo˝ri: C6-free bipartite graphs and product representation of squares, Discrete Math. 165/166 (1997) 371–375.
- [443] E. Gyo˝ri, D´aniel Kor´andi, Abhishek Methuku, Istv´an Tomon, Casey Tompkins, and M´te´ Vizer: On the Tur´an number of some ordered even cycles. European J. Combin. 73 (2018), 81–88.
- [444] Andr´as Hajnal and E. Szemere´di: Proof of a conjecture of Erd˝s, Combinatorial Theory and its Applications vol. II (P. Erd˝s, A. Re´nyi and V.T. S´os eds.), Colloq. Math. Soc. J. Bolyai 4,North-Holland, Amsterdam (1970), pp. 601–623.
- [445] Pe´ter Hajnal: An Ω(n4/3) lower bound on the randomized complexity of graph properties, Combinatorica 11 (2) (1991) 131–143.)
- [446] P. Hajnal, Simao Herdade, and E. Szemere´di: Proof of the Po´sa-Seymour conjecture (2018), Arxiv
- [447] P. Hajnal and M. Szegedy: (1992) On packing bipartite graphs. Combinatorica 12 295–301.
- [448] P. Hajnal and E. Szemere´di: Two Geometrical Applications of the Semi-random Method, Chapter 8 in G. Ambrus et al. (eds.), New Trends in Intuitive Geometry, Bolyai Society Mathematical Studies 27 (2018).
- [449] Hiep H`an, Y. Person, and M. Schacht: On perfect matchings in uniform hypergraphs with large minimum vertex degree. SIAM J. Discrete Math. 23 (2)

(2009), 732–748

- [450] H. H`an and M. Schacht: Dirac-type results for loose Hamilton cycles in uniform hypergraphs, J. Combin. Theory Ser. B 100 (3) (2010) 332–346.
- [451] Jie Han and Yi Zhao: Minimum vertex degree threshold for C43-tiling. J. Graph Theory 79 (2015) 300–317.
- [452] Christoph Hundack, Hans Ju¨rgen Pro¨mel, and Angelika Steger: Extremal graph problems for graphs with a color-critical vertex. Combin. Probab. Comput. 2

(4) (1993) 465–477.

- [453] Hamed Hatami, Jan Hladk´y, Daniel Kr´l’, Serguei Norine, and Alexander A. Razborov: On the number of pentagons in triangle-free graphs. J. Combin. Theory Ser. A 120 (2013) 722–732.
- [454] Julie Haviland and A.G. Thomason: Pseudo-random hypergraphs, in ”Graph Theory and Combinatorics (Cambridge, 1988)” Discrete Math. 75 (1-3) (1989), 255–278.
- [455] J. Haviland and A.G. Thomason: On testing the ”pseudo-randomness” of a hypergraph, Discrete Math. 103 (3) (1992), 321–327.
- [456] Penny E. Haxell: Partitioning complete bipartite graphs by monochromatic cycles, Journal of Combinatorial Theory, Ser. B 69 (1997) pp. 210–218.
- [457] P.E. Haxell: Tree embeddings, J. Graph Theory, 36 (2001), 121–130.
- [458] P.E. Haxell, T.  Luczak, Yuejian Peng, V. Ro¨dl, A. Rucin´ski, M. Simonovits, and J. Skokan: The Ramsey number for hypergraph cycles I, J. Combin. Theory Ser. A 113 (2006) 67–83.


- [459] P.E. Haxell, T.  Luczak, Y. Peng, V. Ro¨dl, A. Rucin´ski, and J. Skokan: The Ramsey number for 3-uniform tight hypergraph cycles. Combin. Probab. Comput. 18 (1-2) (2009) 165–203.
- [460] Teresa Haynes, Michael Henning, Lucas C. van der Merwe, and Anders Yeo: Progress on the Murty-Simon Conjecture on diameter-2 critical graphs: a survey, J. Comb. Optim. 30 (3) (2015) 579–595.
- [461] R. H¨aggkvist and C. Thomassen: On pancyclic digraphs, J. Combin. Theory Ser. B 20 (1976) 20–40.
- [462] D.R. Heath-Brown: Integer sets containing no arithmetic progressions, J. London Math. Soc. 35 (1987), 385–394.
- [463] Anthony J.W. Hilton and Eric C. Milner: Some intersection theorems for systems of ﬁnite sets, Quart. J. Math. Oxf. 2 18 (1967) 369–384.
- [464] Neil Hindman: On a conjecture of Erd˝s, Faber, and Lova´sz about n-colorings. Canad. J. Math. 33 (3) (1981), 563–570.
- [465] Jan Hladk´y, J. Koml´os, D. Piguet, M. Simonovits, Maya Stein, and E. Szemere´di: An approximate version of the Loebl-Komlo´s-So´s Conjecture for sparse graphs, arXiv:1211.3050.v1,(2012) Nov 13.
- [466] J. Hladk´y, J. Koml´os, D. Piguet, M. Simonovits, M. Stein, and E. Szemere´di: The approximate Loebl-Komlo´s-So´s Conjecture I: The sparse decomposition, SIAM J. Discrete Math., 31 (2017), 945–982,
- [467] J. Hladk´y, J. Koml´os, D. Piguet, M. Simonovits, M. Stein, and E. Szemere´di: The approximate Loebl-Komlo´s-So´s Conjecture II: The rough structure of LKS graphs, SIAM J. Discrete Math., 31 (2017), 983–1016,
- [468] J. Hladk´y, J. Koml´os, D. Piguet, M. Simonovits, M. Stein, and E. Szemere´di: The approximate Loebl-Komlo´s-So´s Conjecture III: The ﬁner structure of LKS graphs, SIAM J. Discrete Math., 31 (2017), 1017–1071,
- [469] J. Hladk´y, J. Koml´os, D. Piguet, M. Simonovits, M. Stein, and E. Szemere´di: The approximate Loebl-Komlo´s-So´s conjecture IV: Embedding techniques and the proof of the main result. SIAM J. Discrete Math. 31 (2) (2017) 1072–1148.
- [470] J. Hladk´y, D. Piguet, M. Simonovits, M. Stein, and E. Szemere´di: The approximate Loebl-Komlo´s-So´s conjecture and embedding trees in sparse graphs, Electron. Res. Announc. Math. Sci., 22, (2015), 1–11.
- [471] J. Hladk´y and M. Schacht: Note on bipartite graph tilings. SIAM J. Discrete Math. 24 (2) (2010), 357–362.
- [472] Alan J. Hoﬀman and Robert R. Singleton: Moore graphs with diameter 2 and 3, IBM Journal of Res. Develop. 4 (1960) 497–504.
- [473] W. Imrich: Explicit construction of graphs without small cycles, Combinatorica 4 (1984), 53–59.
- [474] B. Jackson and O. Ordaz: Chva´tal-Erd˝os condition for path and cycles in graphs and digraphs. A survey, Discrete Math. 84 (1990), 241–254.
- [475] S. Janson: Quasi-random graphs and graph limits, European J. Combin. 32

(2011), 1054–1083.

- [476] Svante Janson, Tomasz  Luczak, and A. Rucin´ski: Random graphs. Wiley-Interscience Series in Discrete Mathematics and Optimization. WileyInterscience, New York, (2000). xii+333 pp.
- [477] Janson, Svante and S´os, Vera T.: More on quasi-random graphs, subgraph counts and graph limits. European J. Combin. 46 (2015), 134–160.
- [478] S. Janson and A. Rucin´ski: The infamous upper tail. Probabilistic methods in combinatorial optimization. Random Structures and Algorithms 20 (3) (2002) 317–342.


- [479] Matthew Jenssen and J. Skokan: Exact Ramsey numbers of Odd cycles via nonlinear optimization, Arxiv 1608.05705V1
- [480] Anders Johansson, J. Kahn, and Van H. Vu: Factors in random graphs, Random Structures and Algorithms, 33 (2008), 1–28.
- [481] F. Joos, Jaehoon Kim, D. Ku¨hn, and D. Osthus: Optimal packings of bounded degree trees. arXiv1606.03953 (Submitted on 13 Jun 2016)
- [482] Jeﬀ Kahn: Coloring nearly-disjoint hypergraphs with n+o(n) colors, J. Combin. Theory Ser. A 59 (1991) 31–39.
- [483] Jeﬀ Kahn and Paul Seymour: A fractional version of the Erd˝os-Faber-Lova´sz conjecture. Combinatorica 12 (2) (1992), 155–160.
- [484] Gil Kalai: Designs exist! [after Peter Keevash]. Ast´erisque No. 380, Se´minaire Bourbaki. Vol. 2014/2015 (2016), Exp. No. 1100, 399–422.
- [485] Ravi Kannan: Markov chains and polynomial time algorithms. 35th Annual Symposium on Foundations of Computer Science (Santa Fe, NM, 1994), 656– 671, IEEE Comput. Soc. Press, Los Alamitos, CA, 1994.
- [486] Mikio Kano and Xueliang Li: Monochromatic and heterochromatic subgraphs in edge colored graphs – A Survey, Graphs and Combinatorics 24 (2008) 237–263.
- [487] Roman Karasev, Jan Kyncˇl, Pavel Pat´ak, Zuzana Pat´akova´, and Martin Tancer: Bounds for Pach’s selection theorem and for the minimum solid angle in a simplex. Discrete Comput. Geom. 54 (3) (2015), 610–636.
- [488] Gyula Katona: Graphs, vectors and inequalities in probability theory. (Hungarian) Mat. Lapok 20 (1969) 123–127. 141
- [489] G.O.H. Katona: Extremal problems for hypergraphs, in: M. Hall, J.H. van Lint (Eds.), Combinatorics Part II, in: Math. Centre Tracts, vol. 56 (1974), Mathematisch Centre Amsterdam, pp. 13–42.
- [490] G. Katona: Probabilistic inequalities from extremal graph results (a survey), Random Graphs ’83, Poznan, 1983, Ann. Discrete Math. 28 (1985) 159–170.
- [491] G.O.H. Katona: Tur´an’s graph theorem, measures and probability theory. Number theory, analysis, and combinatorics, 167–176, De Gruyter Proc. Math., De Gruyter, Berlin, (2014).
- [492] Katona, G.Y., Kierstead, H.A.: Hamiltonian chains in hypergraphs. J. Graph Theory 30 (3) (1999) 205–212
- [493] Gy. Katona, Tibor Nemetz, and M. Simonovits: On a graph problem of Tur´an, Mat. Fiz. Lapok 15 (1964) 228–238 (in Hungarian).
- [494] Peter Keevash: The Tur´an problem for projective geometries, J. Combin. Theory Ser. A, 111 (2005), 289–309.
- [495] P. Keevash: Shadows and intersections: stability and new proofs, Advances Math. 218 (5) (2008) 1685–1703.
- [496] P. Keevash: A hypergraph regularity method for generalised Tur´an problems, Random Struct Algorithm 34 (2009), 123–164.
- [497] P. Keevash: A hypergraph blow-up lemma, Random Struct. Algorithms 39

(2011) 275–376.

- [498] P. Keevash: Hypergraph Tur´an problems, in: R. Chapman (Ed.), Surveys in Combinatorics, Cambridge Univ. Press, 2011, pp. 83–140.
- [499] P. Keevash and R. Mycroft: A multipartite Hajnal-Szemere´di theorem. The Seventh European Conference on Combinatorics, Graph Theory and Applications, 141–146, CRM Series, 16, Ed. Norm., Pisa, 2013.


![image 733](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile733.png>)

141Mostly we refer to the same Gyula Katona, but occasionally to his son Y.=Younger Gyula Katona, e.g., [492].

- [500] P. Keevash: The existence of designs, arXiv:1401.3665. (see also P. Keevash – ”The existence of designs”, videotaped lectures https://www.youtube.com/watch?v=tN6oGXqS2Bs, 2015.)
- [501] P. Keevash: The existence of designs, II. arXiv:1802.05900.
- [502] P. Keevash: Counting designs. J. Eur. Math. Soc. (JEMS) 20 (4) (2018), 903– 927.
- [503] P. Keevash and Dhruv Mubayi: Stability theorems for cancellative hypergraphs. J. Combin. Theory Ser. B 92 (1) (2004), 163–175.
- [504] P. Keevash and B. Sudakov: The Tur´an number of the Fano plane. Combinatorica 25 (5) (2005) 561–574.
- [505] P. Keevash and B. Sudakov: Triangle packings and 1-factors in oriented graphs. J. Combin. Theory Ser. B 99 (4) (2009) 709–727.
- [506] P. Keevash and B. Sudakov: Pancyclicity of Hamiltonian and highly connected graphs. J. Combin. Theory Ser. B 100 (5) (2010), 456–467.
- [507] Imdadullah Khan: Perfect matchings in 3-uniform hypergraphs with large vertex degree. SIAM J. Discrete Math. 27 (2) (2013) 1021–1039
- [508] I. Khan: Perfect matchings in 4-uniform hypergraphs. J. Combin. Theory Ser. B 116 (2016), 333–366.
- [509] Henry A. Kierstead and A.V. Kostochka: An Ore-type theorem on equitable coloring, J. Combinatorial Theory Series B 98 (2008), 226–234.
- [510] H.A. Kierstead and A.V. Kostochka: A short proof of the Hajnal-Szemere´di Theorem on equitable coloring, Combinatorics, Probability and Computing 17

(2008), 265–270.

- [511] H.A. Kierstead and A.V. Kostochka: Ore-type versions of Brooks’ theorem. J. Combin. Theory Ser. B 99 (2) (2009) 298–305.
- [512] H.A. Kierstead, A.V. Kostochka, T. Molla, and Elyse C. Yeager: Sharpening an Ore-type version of the Corr´adi-Hajnal theorem. Abh. Math. Semin. Univ. Hambg. 87 (2) (2017) 299–335. (Reviewer: Colton Magnant)
- [513] H.A. Kierstead, A.V. Kostochka, M. Mydlarz, and E. Szemere´di: A fast algorithm for equitable coloring. Combinatorica 30 (2) (2010) 217–224.
- [514] H.A. Kierstead, A.V. Kostochka and Gexin Yu: Extremal graph packing problems: Ore-type versus Dirac-type. In Surveys in Combinatorics 2009 Vol. 365 of London Mathematical Society Lecture Note Series, Cambridge Univ. Press, 113–136.
- [515] Jeong Han Kim: The Ramsey number R(3, t) has order of magnitude t2/log t. Random Struct. Algorithms 7 (3) (1995) 173–207.
- [516] Jaehoon Kim, Younjin Kim, and Hong Liu: Two conjectures in Ramsey-Tur´an theory, SIAM J. Discrete Math. 33 (1) (2019) 564–586.
- [517] Valerie King: ”Lower bounds on the complexity of graph properties,” In Proceedings of the 20th Annual ACM Symposium on the Theory of Computing, Chicago, IL, 1988, pp. 468–476.
- [518] V. King: A Lower Bound for the Recognition of Digraph Properties. Combinatorica, 1990, 10: 53–59
- [519] D.J. Kleitman and B.L. Rothschild: The number of ﬁnite topologies, Proc Amer Math. Soc. 25 (2) (1970), 276–282.
- [520] Daniel J. Kleitman and B.L. Rothschild: Asymptotic enumeration of partial orders on a ﬁnite set, Trans Amer Math. Soc. 205 (1975), 205–220.
- [521] D.J. Kleitman, B.L. Rothschild, and J.H. Spencer: The number of semigroups of order n. Proc. Amer. Math. Soc. 55 (1) (1976) 227–232.
- [522] D.J. Kleitman and David B. Wilson: On the number of graphs which lack small


- cycles, preprint, 1997.
- [523] D.J. Kleitman and Kenneth J. Winston: On the number of graphs without 4-cycles, Discrete Math. 41 (2) (1982) 167–172.
- [524] Yoshiharu Kohayakawa: Szemere´di’s regularity lemma for sparse graphs, in Foundations of Computational Mathematics (Rio de Janeiro, 1997), Springer, Berlin, 1997, pp. 216–230.
- [525] Y. Kohayakawa, T.  Luczak, and V. Ro¨dl: On K4-free subgraphs of random graphs. Combinatorica 17 (2) (1997), 173–213.
- [526] Y. Kohayakawa; Guilherme Oliveira Mota, and M. Schacht; A. Taraz: Counting results for sparse pseudorandom hypergraphs II. European J. Combin. 65

(2017), 288–301.

- [527] Y. Kohayakawa, B. Nagle, V. Ro¨dl, and M. Schacht: Weak hypergraph regularity and linear hypergraphs, Journal of Combinatorial Theory. Series B 100

(2010), 151–160.

- [528] Y. Kohayakawa and V. Ro¨dl: Szemere´di’s regularity lemma and quasirandomness, in: Recent Advances in Algorithms and Combinatorics, in: CMS Books Math./Ouvrages Math. SMC, vol. 11, Springer, New York, 2003, pp. 289–351.
- [529] Y. Kohayakawa, V. Ro¨dl, M. Schacht, and J. Skokan: On the triangle removal lemma for subgraphs of sparse pseudorandom graphs, in: An Irregular Mind (Szemere´di is 70), in: Bolyai Soc. Math. Stud., vol. 21 (2010) Springer, Berlin, pp. 359–404.
- [530] Y. Kohayakawa, M. Simonovits, and J. Skokan: The 3-colored Ramsey number of odd cycles, Proceedings of GRACO2005, pp. 397–402 (electronic), Electron. Notes Discrete Math., 19, Elsevier, Amsterdam, (2005).
- [531] Phokion G. Kolaitis, Hans Ju¨rgen Pro¨mel, and B.L. Rothschild: Kℓ+1-free graphs: asymptotic structure and a 0-1 law, Trans. Amer. Math. Soc. 303 (2)

(1987) 637–671.

- [532] J´anos Koll´r, L. Ro´nyai, and Tibor Szab´o: Norm-graphs and bipartite Tur´an numbers. Combinatorica 16 (1996), 399–406.
- [533] J´anos Koml´os: The Blow-up lemma, Combin. Probab. Comput. 8 (1999) 161– 176.
- [534] J. Koml´os: Tiling Tur´an theorems, Combinatorica 20 (2000), 203–218.
- [535] J. Koml´os, J´anos Pintz, and E. Szemere´di: On Heilbronn’s triangle problem. J. London Math. Soc. (2) 24 (3) (1981), 385–396.
- [536] J. Koml´os, J. Pintz, and E. Szemere´di: A lower bound for Heilbronn’s problem. J. London Math. Soc. (2) 25 (1) (1982) 13–24.
- [537] J. Koml´os, G.N. S´ark¨ozy, and E. Szemere´di: Proof of a packing conjecture of Bollob´s, Combinatorics, Probability and Computing 4 (1995), 241–255.
- [538] J. Koml´os, G.N. S´ark¨ozy, and E. Szemere´di: On the square of a Hamiltonian cycle in dense graphs, Random Structures and Algorithms, 9, (1996), 193–211.
- [539] J. Koml´os, G.N. S´ark¨ozy, and E. Szemere´di: Blow-up Lemma, Combinatorica, 17 (1) (1997), pp. 109–123.
- [540] J. Koml´os, G.N. S´ark¨ozy, and E. Szemere´di: On the Po´sa-Seymour conjecture, Journal of Graph Theory 29 (1998) 167–176.
- [541] J. Koml´os, G.N. S´ark¨ozy, and E. Szemere´di: An algorithmic version of the blow-up lemma, Random Structures and Algorithms 12 (3) (1998) 297–312.
- [542] J. Koml´os, G.N. S´ark¨ozy and E. Szemere´di: Proof of the Seymour conjecture for large graphs, Annals of Combinatorics, 2, (1998), 43–60.
- [543] J. Koml´os, G.N. S´ark¨ozy, and E. Szemere´di: Proof of the Alon-Yuster conjec-


- ture. Combinatorics (Prague, 1998). Discrete Math. 235 (1-3) (2001) 255–269.
- [544] J. Koml´os; G.N. S´ark¨ozy; E. Szemere´di: Spanning trees in dense graphs. Combin. Probab. Comput. 10 (5) (2001) 397–416.
- [545] J. Koml´os, Ali Shokoufandeh, M. Simonovits, and E. Szemere´di: The regularity lemma and its applications in graph theory, in Theoretical Aspects of Computer Science (Tehran, 2000), Lecture Notes in Comput. Sci., 2292, Springer, Berlin,

(2002), 84–112.

- [546] J. Koml´os and M. Simonovits: Szemere´di’s regularity lemma and its applications in graph theory, in Combinatorics, Paul Erd˝s Is Eighty, Vol. 2 (Keszthely, 1993), Bolyai Soc. Math. Stud. 2, J´anos Bolyai Math. Soc., Budapest, 1996, pp. 295–352.
- [547] D´aniel Kor´andi, M. Krivelevich, and B. Sudakov: Decomposing random graphs into few cycles and edges. Combin. Probab. Comput. 24 (6) (2015) 857–872.
- [548] Alexander V. Kostochka: ”A Class of Constructions for Tur´an’s (3,4)-Problem,” Combinatorica 2 (2) (1982) 187–192.
- [549] A.V. Kostochka, D. Mubayi, and J. Verstrae¨te: Hypergraph Ramsey numbers: triangles versus cliques. J. Combin. Theory Ser. A 120 (7) (2013) 1491–1507.
- [550] A.V. Kostochka, K. Nakprasit, and S. Pemmaraju: On equitable coloring of d-degenerate graphs, SIAM J. Discrete Math. 19 (2005) 83–95.
- [551] A.V. Kostochka, M.J. Pelsmajer, and Doug B. West: A list analogue of equitable coloring. J. Graph Theory 44 (3) (2003) 166–177.
- [552] A.V. Kostochka and Michael Stiebitz: A list version of Dirac’s theorem on the number of edges in colour-critical graphs. J. Graph Theory 39 (3) (2002), 165– 177.
- [553] A.V. Kostochka and G. Yu: Ore-type graph packing problems, Combin. Probab. Comput., 16 (2007), pp. 167–169.
- [554] Tama´s K˝v´ari, V.T. S´os, and P. Tur´an: On a problem of Zarankiewicz, Colloq Math. 3 (1954), 50–57.
- [555] Daniel Kr´l’ and Oleg Pikhurko: Quasirandom permutations are characterized by 4-point densities. Geom. Funct. Anal. 23 (2) (2013) 570–579.
- [556] Michael Krivelevich: On the minimal number of edges in color-critical graphs, Combinatorica 17 (1997) 401–426.
- [557] M. Krivelevich, Choongbum Lee, and B. Sudakov: Resilient pancyclicity of random and pseudorandom graphs. SIAM J. Discrete Math. 24 (1) (2010) 1– 16.
- [558] M. Krivelevich and W. Samotij: Optimal packings of Hamilton cycles in sparse random graphs, SIAM J. Discrete Math. 26 (3) (2012) 964–982.,
- [559] M. Krivelevich and B. Sudakov: Pseudo-random graphs, in: More Sets, Graphs and Numbers, in: Bolyai Soc. Math. Stud., vol. 15 (2006) Springer, pp. 199– 262.
- [560] D. Ku¨hn and D. Osthus: Loose Hamilton cycles in 3-uniform hypergraphs of high minimum degree. J. Combin. Theory Ser. B 96 (6) (2006) 767–821.
- [561] D. Ku¨hn, D. Osthus: Matchings in hypergraphs of large minimum degree, J. Graph Theory 51 (2006) 269–280.
- [562] D. Ku¨hn and D. Osthus: The minimum degree threshold for perfect graph packings, Combinatorica 29 (2009), 65–107.
- [563] D. Ku¨hn and D. Osthus: Embedding large subgraphs into dense graphs. Surveys in combinatorics 2009, 137–167, London Math. Soc. Lecture Note Ser., 365

(2009), Cambridge Univ. Press, Cambridge.

- [564] D. Ku¨hn and D. Osthus: Hamilton decompositions of regular expanders: A proof


- of Kelly’s conjecture for large tournaments, Advances Math., 237 (2013), pp. 62–146.
- [565] D. Ku¨hn and D. Osthus: Hamilton cycles in graphs and hypergraphs: an extremal perspective. Proceedings of the International Congress of Mathematicians 2014. Vol. IV, 381–406, Kyung Moon Sa, Seoul.
- [566] D. Ku¨hn, D. Osthus, and A. Treglown: Matchings in 3-uniform hypergraphs. J. Combin. Theory Ser. B 103 (2) (2013) 291–305.
- [567] Felix Lazebnik, Vasyl A. Ustimenko, and Andrew J. Woldar: Properties of certain families of 2k-cycle-free graphs. J. Combin. Theory Ser. B 60 (2) (1994), 293–298.
- [568] Lazebnik, F.; Ustimenko, V. A.; Woldar, A. J.: A new series of dense graphs of high girth. Bull. Amer. Math. Soc. (N.S.) 32 (1) (1995) 73–79.
- [569] Felix Lazebnik; Woldar, Andrew J.: General properties of some families of graphs deﬁned by systems of equations. J. Graph Theory 38 (2) (2001) 65– 86.
- [570] Choongbum Lee and B. Sudakov: Hamiltonicity, independence number, and pancyclicity. European J. Combin. 33 (4) (2012) 449–457.
- [571] Hanno Lefmann: On Heilbronn’s problem in higher dimension. Combinatorica 23 (4) (2003), 669–680.
- [572] H. Lefmann, Y. Person, V. Ro¨dl, and M. Schacht: On colourings of hypergraphs without monochromatic Fano planes, Combin. Probab. Comput., 18 (2009), pp. 803–818.
- [573] H. Lefmann and Niels Schmitt: A deterministic polynomial-time algorithm for Heilbronn’s problem in three dimensions. SIAM J. Comput. 31 (6) (2002) 1926– 1947.
- [574] Vsevolod F. Lev, T.  Luczak, and Tomasz Schoen: Sum-free sets in abelian groups, Israel Journal of Mathematics 125 (2001), 347–367.
- [575] Ian Levitt, G.N. S´ark¨ozy, and E. Szemere´di: How to avoid using the regularity lemma: Po´sa’s conjecture revisited, Discrete Math., 310 (2010), 630–641.
- [576] Allan Lo and Klas Markstr¨om: A multipartite version of the Hajnal-Szemere´di theorem for graphs and hypergraphs. Combin. Probab. Comput. 22 (1) (2013) 97–111.
- [577] Allan Lo and K. Markstr¨om: Minimum codegree threshold for (K43 −e)-factors. J. Combin. Theory Ser. A 120 (2013) 708–721.
- [578] Allan Lo and K. Markstr¨om: Perfect matchings in 3-partite 3-uniform hypergraphs, J. Combin. Theory Ser. A 127 (2014) 22–57.
- [579] Allan Lo and K. Markstr¨om: F-factors in hypergraphs via absorption. Graphs Combin. 31 (3) (2015), 679–712.
- [580] Po-Shen Loh and Jie Ma: Diameter critical graphs. J. Combin. Theory Ser. B 117 (2016) 34–58.
- [581] L´aszl´o Lova´sz: On covering of graphs. Theory of Graphs (Proc. Colloq., Tihany,

1966) pp. 231–236 (1967) Academic Press, New York

- [582] L. Lova´sz: On chromatic number of ﬁnite set-systems, Acta Math. Acad. Sci. Hungar. 19 (1968) 59–67.
- [583] L. Lova´sz: The factorization of graphs. Combinatorial Structures and their Applications (Proc. Calgary Internat. Conf., Calgary, Alta., 1969) pp. 243–246 Gordon and Breach, New York (1970).
- [584] L. Lova´sz: Subgraphs with prescribed valencies. J. Combinatorial Theory 8

(1970) 391–416.

- [585] L. Lova´sz: On the sieve formula. (Hungarian) Mat. Lapok 23 (1972), 53–69


- (1973).
- [586] L. Lova´sz: Independent sets in critical chromatic graphs, Stud. Sci. Math. Hung. 8 (1973) 165–168.
- [587] L. Lova´sz: Chromatic number of hypergraphs and linear algebra. Studia Sci. Math. Hungar. 11 (1-2) (1976) 113–114 (1978).
- [588] L. Lova´sz: On the Shannon capacity of a graph, IEEE Transactions on Information Theory 25 (1979) 1–7.
- [589] L. Lova´sz: Combinatorial Problems and Exercises, Akade´miai Kiado´, Budapest. North-Holland Publishing Co., Amsterdam-New York, (1979). 551 pp. 2nd Edition, American Mathematical Society, Providence, Rhode Island, 2007.
- [590] L. Lova´sz: Very large graphs. Current developments in mathematics, (2008) 67–128, Int. Press, Somerville, MA, 2009.
- [591] L. Lova´sz: Large networks and graph limits. American Mathematical Society Colloquium Publications, 60. American Mathematical Society, Providence, RI,

(2012) xiv+475 pp.

- [592] L. Lova´sz and M. Simonovits: On the number of complete subgraphs of a graph, in Proc. 5th British Combinatorial Conference, Aberdeen 1975. Congress. Numer. XV (1976) 431–441.
- [593] L. Lova´sz and M. Simonovits: On the number of complete subgraphs of a graph II, Studies in Pure Math. (dedicated to P. Tur´an) (1983) 459–495 Akade´miai Kiado´+Birkha¨user Verlag.
- [594] L. Lova´sz and V.T. S´os: Generalized quasirandom graphs, J. Combin. Theory Ser B 98 (2008), 146–163.
- [595] L. Lova´sz and B. Szegedy: Szemere´di’s lemma for the analyst. Geom. Funct. Anal. 17 (1) (2007) 252–270.
- [596] L. Lova´sz and B. Szegedy: Testing properties of graphs and functions. Israel J. Math. 178 (2010), 113–156.
- [597] Alex Lubotzky: Discrete Groups, Expanding Graphs and Invariant Measures. Progr. Math. 125 (1994) Birkh¨auser, Basel (1994)
- [598] A. Lubotzky, Ralph Phillips, and P. Sarnak: Ramanujan Conjecture and explicit construction of expanders (Extended Abstract), Proceedings of the STOC

(1986), pp. 240–246.

- [599] A. Lubotzky, R. Phillips, and P. Sarnak: Ramanujan graphs, Combinatorica 8

(1988), 261–277.

- [600] Tomasz J.  Luczak: R(Cn, Cn, Cn) ≤ (4 + o(1))n, Journal of Combinatorial Theory, Ser. B 75 (2) (1999) 174–187.
- [601] T.  Luczak: On triangle-free random graphs, Random Struct. Algorithms 16 (3)

(2000), 260–276.

- [602] T.  Luczak, V. Ro¨dl, and E. Szemere´di: Partitioning two-colored complete graphs into two monochromatic cycles, Combinatorics, Probability and Computing, 7

(1998) pp. 423–436.

- [603] T.  Luczak and T. Schoen: On the maximal density of sum-free sets. Acta Arith. 95 (3) (2000) 225–229.
- [604] T.  Luczak and T. Schoen: On the number of maximal sum-free sets, Proc. Amer. Math. Soc. 129 (2001) 2205–2207.
- [605] Clara Lu¨ders and C. Reiher: The Ramsey–Tur´an problem for cliques, Arxiv 1709.03352.
- [606] W. Mantel: Problem 28 (solution by H. Gouwentak, W. Mantel, J. Texeira de Mattes, F. Schuh and W. A. Wythoﬀ), Wiskundige Opgaven 10 (1907), 60–61.
- [607] Gregory A. Margulis: Explicit constructions of expanders. (Russian) Problemy


- Peredacˇi Informacii 9 (4) (1973), 71–80. English transl.: Problems Inform. Transmission 9 (1975) 325–332.
- [608] G.A. Margulis: Explicit constructions of graphs without short cycles and low density codes, Combinatorica 2 (1982), 71–78.
- [609] G.A. Margulis: Arithmetic groups and graphs without short cycles, 6th Internat. Symp. on Information Theory, Tashkent 1984, Abstracts, Vol. 1, pp. 123–125 (in Russian).
- [610] G.A. Margulis: Some new constructions of low-density paritycheck codes. 3rd Internat. Seminar on Information Theory, convolution codes and multi–user communication, Sochi 1987, pp. 275–279 (in Russian).
- [611] G.A. Margulis: Explicit group theoretic constructions of combinatorial schemes and their applications for the construction of expanders and concentrators, Journal of Problems of Information Transmission, 24 (1988) 39–46, (in Russian).
- [612] K. Markstr¨om and A. Rucin´ski: Perfect matchings (and Hamilton cycles) in hypergraphs with large degrees. European J. Combin. 32 (5) (2011), 677–687
- [613] Ryan Martin and E. Szemere´di: Quadripartite version of the Hajnal-Szemere´di theorem. Discrete Math. 308 (19) (2008), (special edition in honor of Mikl´os Simonovits), 4337–4360.
- [614] Michael Molloy: The Probabilistic Method. Book chapter in ”Probabilistic Methods for Algorithmic Discrete Mathematics”, M. Habib, C. McDiarmid, J. Ramirez-Alfonsin and B. Reed, editors. pp. 1–35. Springer, 1998.
- [615] M. Molloy and Bruce Reed: Graph colouring and the probabilistic method, Algorithms and Combinatorics, vol. 23 (2002), Springer-Verlag, Berlin.
- [616] Richard Montgomery: Embedding Bounded Degree Spanning Trees in Random Graphs, preprint, https://arxiv.org/abs/1405.6559, 2014.
- [617] John W. Moon and Leo Moser: On a problem of Tur´an. Magyar Tud. Akad. Mat. Kutato´ Int. K¨zl. 7 (1962) 283–286.
- [618] Robert Morris and David Saxton: The number of C2ℓ-free graphs, Advances in Mathematics 298 (2016), 534–580.
- [619] Robin A. Moser: Derandomizing the Lova´sz local lemma more eﬀectively. (2008) Eprint arXiv:0807.2120v2.
- [620] R.A. Moser and G´bor Tardos: A constructive proof of the general Lova´sz local lemma. J. ACM 57 (2) (2010), Art. 11, 15 pp.
- [621] Guy Moshkovitz and A. Shapira: A short proof of Gowers’ lower bound for the regularity lemma. Combinatorica 36 (2016) 187–194.
- [622] Dhruv Mubayi: The co-degree density of the Fano plane, J. Combin. Theory Ser. B 95 (2) (2005) 333–337.
- [623] D. Mubayi: Structure and stability of triangle-free set systems, Trans. Amer. Math. Soc., 359 (2007), 275–291.
- [624] D. Mubayi: Counting substructures I: color critical graphs, Advances Math. 225 (5) (2010) 2731–2740.
- [625] D. Mubayi and O. Pikhurko: A new generalization of Mantel’s theorem to kgraphs. J. Combin. Theory Ser. B 97 (4) (2007), 669–678.
- [626] D. Mubayi and V.T. S´os: Explicit constructions of triple systems for Ramsey– Tur´an problems. J. Graph Theory 52 (3) (2006), 211–216.
- [627] Marcello Mydlarz and E. Szemere´di: Algorithmic Brooks’ theorem, 2007, manuscript.
- [628] Brendan Nagle and V. Ro¨dl: The asymptotic number of triple systems not containing a ﬁxed one, in: Combinatorics, Prague, 1998, Discrete Math. 235


(2001) 271–290.

- [629] B. Nagle, V. Ro¨dl, and M. Schacht: An algorithmic hypergraph regularity lemma. Random Structures Algorithms 52 (2) (2018), 301–353.
- [630] Jarik Nesˇetrˇil and V. Ro¨dl: A short proof of the existence of highly chromatic hypergraphs without short cycles. J. Combin. Theory Ser. B 27 (2) (1979), 225–227.
- [631] Rajko Nenadov, B. Sudakov, and Mykhaylo Tyomkyn: Proof of the BrownErd˝os-So´s conjecture in groups, Arxiv 1902.07614
- [632] Vladimir Nikiforov: The number of cliques in graphs of given order and size. Trans. Amer. Math. Soc. 363 (2011) 1599–1618.
- [633] V. Nikiforov and R.H. Schelp: Cycles and stability, J. Combin. Theory Ser. B 98 (2008) 69–84.
- [634] S. Norin and L. Yepremyan: Tur´an number of generalized triangles. J. Combin. Theory Ser. A 146 (2017), 312–343.
- [635] Oystein Ore: Note on Hamilton circuits, Amer. Math. Monthly 67 (1960) 55.
- [636] Deryk Osthus, H.J. Pro¨mel, and A. Taraz: ‘For which densities are random triangle-free graphs almost surely bipartite?’, Combinatorica 23 (2003), 105– 150.
- [637] J´anos Pach: A Tverberg-type result on multicolored simplices. Comput. Geom. 10 (2) (1998) 71–76.
- [638] J. Pach: Geometric intersection patterns and the theory of topological graphs. Proceedings of the International Congress of Mathematicians—Seoul 2014. Vol. IV, 455–474, Kyung Moon Sa, Seoul, (2014).
- [639] J. Pach and Pankaj K. Agarwal: Combinatorial geometry. Wiley-Interscience Series in Discrete Mathematics and Optimization. A Wiley-Interscience Publication. John Wiley & Sons, Inc., New York, (1995). xiv+354 pp.
- [640] Pach, J´anos:; Sharir, Micha: On the number of incidences between points and curves. Combin. Probab. Comput. 7 (1) (1998) 121–127.
- [641] J. Pach and J´ozsef Solymosi: Crossing patterns of segments, Journal of Combinatorial Theory, Ser. A 96 (2001), 316–325.
- [642] Bal´azs Patk´os: Supersaturation and stability for forbidden subposet problems, J. Combin. Theory Ser. A 136 (2015) 220–237.
- [643] Michael S. Payne and David R. Wood: On the general position subset selection problem, SIAM J. Discrete Math., 27 (4) (2013), 1727–1733.
- [644] Y. Peng and C. Zhao: Generating non-jumping numbers recursively, Discrete Applied Mathematics 156 (2008), 1856–1864.
- [645] Yury Person and M. Schacht: Almost all hypergraphs without Fano planes are bipartite, Proceedings of the Twentieth Annual ACM–SIAM Symposium on Discrete Algorithms, SIAM, Philadelphia, PA, 2009, pp. 217–226.
- [646] Oleg Pikhurko: An exact Tur´an result for the generalized triangle, Combinatorica 28 (2008), 187–208.
- [647] O. Pikhurko: Perfect matchings and K43-tilings in hypergraphs of large codegree, Graphs Combin. 24 (4) (2008) 391–404.
- [648] O. Pikhurko: On possible Tur´an densities. Israel J. Math. 201 (1) (2014), 415– 454.
- [649] O. Pikhurko and Zelealem B. Yilma: Supersaturation problem for color-critical graphs. J. Combin. Theory Ser. B 123 (2017), 148–185.
- [650] Oleg Pikhurko and Alexandr Razborov: Asymptotic structure of graphs with the minimum number of triangles. Combin. Probab. Comput. 26 (1) (2017) 138–160.
- [651] Mark S. Pinsker: On the complexity of a concentrator, in: Proc. of the 7th


- International Teletraﬃc Conference, 1973, pp. 318/1–318/4.
- [652] Nick Pippenger and J. Spencer: Asymptotic behavior of the chromatic index for hypergraphs, J. Combin. Theory Ser A 51 (1989), 24–42.
- [653] J´an Plesnı´k: Critical graphs of given diameter. (Slovak, Russian summary) Acta Fac. Rerum Natur. Univ. Comenian. Math. 30 (1975), 71–93.
- [654] Alexey Pokrovskiy: Partitioning edge-coloured complete graphs into monochromatic cycles and paths, J. Combin. Theory Ser. B 106 (2014) 70–97.
- [655] D. H.J. Polymath, Density Hales-Jewett and Moser numbers, in An Irregular Mind: Szemere´di is 70, Springer–Verlag, New York, 2010, pp. 689–753.
- [656] Polymath, D.H.J.: A new proof of the density Hales-Jewett theorem. Ann. of Math. (2) 175 (3) (2012), 1283–1327.
- [657] Carl Pomerance and A. S´ark¨ozy: Combinatorial number theory, Handbook of combinatorics, Vol. 1, 2, pp. 967–1018, Elsevier, Amsterdam, 1995.
- [658] Lajos Po´sa: A theorem concerning Hamilton lines, Publ. Math. Inst. Hung. Acad. Sci. 7 (1962), 225–226.
- [659] Lajos Po´sa: On the circuits of ﬁnite graphs. Magyar Tud. Akad. Mat. Kutato´ Int. K¨zl. 8 (1963) 355–361 (1964)
- [660] L. Po´sa: Hamiltonian circuits in random graphs, Discrete Math., 14 (1976), pp. 359–364.
- [661] H.J. Pro¨mel and V. Ro¨dl: Non-Ramsey graphs are c log n-universal, J. Comb. Th. (A) 88 (1999) 378–384.
- [662] Hans Ju¨rgen Pro¨mel and Angelika Steger: Excluding induced subgraphs: quadrilaterals, Random Structures and Algorithms 2 (1991) 55–71.
- [663] H.J. Pro¨mel and A. Steger: A. Excluding induced subgraphs. III. A general asymptotic. Random Structures and Algorithms 3 (1) (1992) 19–31.
- [664] H.J. Pro¨mel and A. Steger: Almost all Berge graphs are perfect, Combin. Probab. Comput. 1 (1992) 53–79.
- [665] H.J. Pro¨mel and A. Steger: ‘The asymptotic number of graphs not containing a ﬁxed color-critical subgraph’, Combinatorica 12 (1992), 463–473.
- [666] H.J. Pro¨mel and A. Steger: On the asymptotic structure of sparse triangle free graphs, J. Graph Theory 21 (2) (1996), 137–151,
- [667] L´aszl´o Pyber: An Erd˝s-Gallai conjecture. Combinatorica 5 (1) (1985), 67–79.
- [668] Alexander A. Razborov: Flag algebras. J. Symbolic Logic 72 (2007) 1239–1282.
- [669] A.A. Razborov: On the minimal density of triangles in graphs. Combinatorics, Probability and Computing, 17 (4) (2008) 603–618.
- [670] A.A. Razborov: On 3-hypergraphs with forbidden 4-vertex conﬁgurations, SIAM J. Discrete Math. 24 (3) (2010) 946–963.
- [671] A.A. Razborov: On the Fon-der-Flaass interpretation of extremal examples for Tur´an’s (3,4)-problem. Proceedings of the Steklov Institute of Mathematics 274

(2011), 247–266 Algoritmicheskie Voprosy Algebry i Logiki, 269–290; translation in Proc. Steklov Inst. Math. 274 (1) (2011), 247–266.

- [672] Christian Reiher: The clique density theorem, Ann. of Math. 184 (2016) 683– 707.
- [673] C. Reiher, V. Ro¨dl, A. Rucin´ski, M. Schacht, and E. Szemere´di: Minimum vertex degree condition for tight Hamiltonian cycles in 3-uniform hypergraphs

(2016) Arxiv1611.03118v1

- [674] Istv´an Reiman: Uber¨ ein Problem von K. Zarankiewicz, Acta Math. Acad. Sci. Hungar. 9 (1958), 269–278.
- [675] D. Romero and A. S´anchez-Arroyo: ”Advances on the Erd˝s-Faber-Lova´sz conjecture”, in G. Grimmet and C, McDiarmid, Combinatorics, Complexity, and


- Chance: A Tribute to Dominic Welsh, Oxford Lecture Series in Mathematics and Its Applications, Oxford University Press, (2007) pp. 285–298.
- [676] Vera Rosta: On a Ramsey-type problem of J.A. Bondy and P. Erd˝s. I, J. Combin. Theory Ser. 15 (1973) 94–104; and V. Rosta: On a Ramsey-type problem of J.A. Bondy and P. Erd˝s. II, J. Combin. Theory Ser. B 15 (1973) 105–120.
- [677] Klaus F. Roth: On a problem of Heilbronn, J. London Math. Soc. 26 (1951), 198–204.
- [678] K.F. Roth: On certain sets of integers, J. London Math. Soc. 28 (1953), 104– 109.
- [679] K.F. Roth: On a problem of Heilbronn II, Proc. London Math. Soc. 25 (3)

(1972), 193–212.

- [680] K.F. Roth: On a problem of Heilbronn III, Proc. London Math. Soc. 25 (3)

(1972), 543–549.

- [681] K.F. Roth: Estimation of the Area of the Smallest Triangle Obtained by Selecting Three out of n Points in a Disc of Unit Area, AMS, Providence, Proc. of Symposia in Pure Mathematics 24 (1973) 251–262.
- [682] K.F. Roth: Developments in Heilbronn’s triangle problem, Advances in Math. 22 (3) (1976), 364–385.
- [683] Vojteˇch Ro¨dl: On a packing and covering problem, European J. Combin. 6

(1985) 69–78.

- [684] V. Ro¨dl: Note on a Ramsey-Tur´an type problem, Graphs and Combin. 1 (3)

(1985), 291–293.

- [685] V. Ro¨dl: Quasi-randomness and the regularity method in hypergraphs. Proceedings of the International Congress of Mathematicians—Seoul 2014. Vol. 1, 573–601, Kyung Moon Sa, Seoul, (2014).
- [686] V. Ro¨dl, B. Nagle, J. Skokan, M. Schacht, and Y. Kohayakawa: The hypergraph regularity method and its applications, Proc. Natl. Acad. Sci. USA 102 (23)

(2005) 8109–8113.

- [687] V. Ro¨dl and A. Rucin´ski: Perfect matchings in ε-regular graphs and the blow-up lemma, Combinatorica 19 (3) (1999) 437–452.
- [688] V. Ro¨dl and A. Rucin´ski: Dirac-type questions for hypergraphs – a survey (or more problems for Endre to solve). In: I. B´ar´any, J. Solymosi, G. S´agi (eds.) An Irregular Mind, pp. 561–590. J´anos Bolyai Math. Soc., Budapest (2010)
- [689] V. Ro¨dl and A. Rucin´ski: Families of triples with high minimum degree are Hamiltonian. Discuss. Math. Graph Theory 34 (2) (2014), 361–381.
- [690] V. Ro¨dl, A. Rucin´ski, M. Schacht, and E. Szemere´di: A note on perfect matchings in uniform hypergraphs with large minimum collective degree. Comment. Math. Univ. Carolin. 49 (4) (2008) 633–636.
- [691] V. Ro¨dl, A. Rucin´ski, M. Schacht, and E. Szemere´di: On the Hamiltonicity of triple systems with high minimum degree. Annales Comb. 21 (1) (2017), 95–117.
- [692] V. Ro¨dl, A. Rucin´ski, and E. Szemere´di: Perfect matchings in uniform hypergraphs with large minimum degree, European J. Combin. 27 (8) (2006) 1333–1349.
- [693] V. Ro¨dl, A. Rucin´ski, and E. Szemere´di: A Dirac-type theorem for 3-uniform hypergraphs, Combinatorics, Probability, and Computing 15 (1-2) (2006) 229– 251.
- [694] V. Ro¨dl, A. Rucin´ski, and E. Szemere´di: An approximate Dirac-type theorem for k-uniform hypergraphs. Combinatorica 28 (2) (2008) 229–260.


- [695] V. Ro¨dl, A. Rucin´ski, and E. Szemere´di: Perfect matchings in large uniform hypergraphs with large minimum collective degree. J. Combin. Theory Ser. A 116 (3) (2009) 613–636.
- [696] V. Ro¨dl, A. Rucin´ski, and E. Szemere´di: Dirac-type conditions for Hamiltonian paths and cycles in 3-uniform hypergraphs. Advances Math. 227 (3) (2011), 1225–1299.
- [697] V. Ro¨dl, A. Rucin´ski, and A. Taraz: Hypergraph packing and graph embedding, Combinatorics, Probab. Comput. 8 (1999) 363–376.
- [698] V. Ro¨dl, A. Rucin´ski, and Michelle Wagner: An algorithmic embedding of graphs via perfect matchings. Randomization and approximation techniques in computer science (Barcelona, 1998), 25–34, Lecture Notes in Comput. Sci., 1518, Springer, Berlin, 1998.
- [699] V. Ro¨dl, M. Schacht, E. Tengan and N. Tokushige: Density theorems and extremal hypergraph problems, Israel J. Math. 152 (2006), 371–380.
- [700] V. Ro¨dl and M. Schacht: Regular partitions of hypergraphs: Regularity lemmas, Combin. Probab. Comput. 16 (2007), 833–885.
- [701] V. Ro¨dl and M. Schacht: Generalizations of the removal lemma, Combinatorica 29 (4) (2009) 467–501.
- [702] V. Ro¨dl and M. Schacht: Extremal results in random graphs, Erd˝s centennial, Bolyai Soc. Math. Stud., vol. 25, J´anos Bolyai Math. Soc., Budapest, (2013), pp. 535–583,
- [703] V. Ro¨dl and Mark H. Siggers: Color critical hypergraphs with many edges, J. Graph Theory 53 (2006) 56–74.
- [704] V. Ro¨dl and J. Skokan: Regularity lemma for k-uniform hypergraphs, Random Structures and Algorithms 25 (1) (2004) 1–42.
- [705] V. Ro¨dl and J. Skokan: Applications of the regularity lemma for uniform hypergraphs, Random Structures and Algorithms 28 (2) (2006) 180–194.
- [706] V. Ro¨dl and Zsolt Tuza: On color critical graphs. J. Combin. Theory Ser. B 38

(3) (1985), 204–213.

- [707] Imre Z. Ruzsa: Solving a linear equation in a set of integers. I, Acta Arith. 65

(3) (1993) 259–282.

- [708] I.Z. Ruzsa: Solving a linear equation in a set of integers II, Acta Arith. 72

(1995) 385–397.

- [709] I.Z. Ruzsa: An inﬁnite Sidon sequence, J. Number Theory 68 (1998) 63–71.
- [710] I.Z. Ruzsa and E. Szemere´di: Triple systems with no six points carrying three triangles. Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Vol. II, pp. 939–945, Colloq. Math. Soc. J´anos Bolyai, 18, North-Holland, Amsterdam– New York, 1978.
- [711] Horst Sachs and Michael Stiebitz: Construction of colour-critical graphs with given major-vertex subgraph. Combinatorial mathematics (Marseille–Luminy, 1981), 581–598, North-Holland Math. Stud., 75, Ann. Discrete Math., 17 (1983) North-Holland, Amsterdam.
- [712] H. Sachs and M. Stiebitz: Colour-critical graphs with vertices of low valency. Graph theory in memory of G.A. Dirac (Sandbjerg, 1985), 371–396, Ann. Discrete Math., 41, North-Holland, Amsterdam, 1989.
- [713] H. Sachs and M. Stiebitz: On constructive methods in the theory of colourcritical graphs. Graph colouring and variations. Discrete Math. 74 (1-2) (1989) 201–226.
- [714] Wojciech Samotij: Stability results for discrete random structures, Random Structures & Algorithms 44 (2014), 269–289. /


- [715] Tom Sanders: On a non-abelian Balog-Szemere´di-type lemma, J. Aust. Math. Soc. 89 (2010), 127–132.
- [716] T. Sanders: On Roth’s theorem on progressions. Ann. of Math. (2) 174 (1)

(2011), 619–636.

- [717] T. Sanders: Roth’s theorem: an application of approximate groups. Proceedings of the International Congress of Mathematicians—Seoul 2014. Vol. III, 401–423, Kyung Moon Sa, Seoul, (2014).
- [718] Alexander A. Sapozhenko: On the number of sum-free sets in Abelian groups, Vestnik Moskov. Univ. Ser. Mat. Mekh. 4 (2002) 14–18.
- [719] A. A. Sapozhenko: Asymptotics of the number of sum-free sets in abelian groups of even order, Rossiiskaya Akademiya Nauk. Dokladi Akademii Nauk 383 (2002), 454–457.
- [720] A.A. Sapozhenko: ‘Solution of the Cameron-Erd˝os problem for groups of prime order’, Zh. Vychisl. Mat. Mat. Fiz. 49 (2009) 1435–1441.
- [721] G´bor N. S´ark¨ozy: Cycles in bipartite graphs and an application in number theory. J. Graph Theory 19 (3) (1995), 323–331.
- [722] G.N. S´ark¨ozy: The regularity method, and the Blow-up method and their application, Thesis for Doctor of Sciences of Hungarian Acad Sci (with an Introduction in Hungarian).
- [723] G.N. S´ark¨ozy: Improved monochromatic loose cycle partitions in hypergraphs. Discrete Math. 334 (2014), 52–62.
- [724] G.N. S´ark¨ozy: A quantitative version of the Blow-up Lemma, submitted for publication. (2014)
- [725] G.N. S´ark¨ozy: Monochromatic cycle power partitions. Discrete Math. 340 (2)

(2017) 72–80.

- [726] G.N. S´ark¨ozy and Stanley M. Selkow: An extension of the Ruzsa-Szemere´di theorem, Combinatorica 25 (1) (2004) 77–84.
- [727] G.N. S´ark¨ozy and S.M Selkow: On a Tur´an-type hypergraph problem of Brown, Erd˝os and T. S´os. Discrete Math. 297 (1-3) (2005), 190–195.
- [728] G.N. S´ark¨ozy and S.M. Selkow: On an anti-Ramsey problem of Burr, Erd˝s, Graham, and T. S´os. J. Graph Theory 52 (2) (2006), 147–156.
- [729] Norbert Sauer and J. Spencer: Edge disjoint placement of graphs. J. Combin. Theory Ser. B 25 (1978) 295–302.
- [730] David Saxton and A. Thomason: Hypergraph containers, Invent. Math. 201

(2015), 925–992.

- [731] Mathias Schacht: Extremal results for random discrete structures, Ann. Math. 184 (2016) 333–365.
- [732] Richard H. Schelp: Some Ramsey-Tur´an type problems and related questions, Discrete Math. 312 (2012) 2158–2161.
- [733] Wolfgang M. Schmidt: On a Problem of Heilbronn, Journal of the London Mathematical Society (2) 4 (1972) 545–550.
- [734] Alex Scott: Szemere´di’s Regularity Lemma for matrices and sparse graphs, Combin. Probab. Comput. 20 (2011) 455–466.
- [735] Paul Seymour: Problem section, Combinatorics: Proceedings of the British Combinatorial Conference 1973 (T. P.McDonough and V.C. Mavron eds.), Lecture Note Ser., No. 13 (1974), pp. 201–202. London Mathematical Society, Cambridge University Press, London.
- [736] Asaf Shapira and R. Yuster: The eﬀect of induced subgraphs on quasirandomness. Random Structures and Algorithms 36 (1) (2010), 90–109.
- [737] James B. Shearer: A note on the independence number of triangle-free graphs.


- Discrete Math. 46 (1) (1983) 83–87.
- [738] J.B. Shearer: A note on the independence number of triangle-free graphs. II. J. Combin. Theory Ser. B 53 (2) (1991) 300–307.
- [739] J.B. Shearer: The independence number of dense graphs with large odd girth, Electron. J. Combin. 2 (1995), Note 2 (electronic).
- [740] J.B. Shearer: On the independence number of sparse graphs. Random Struct. Alg. 7 (1995) 269–271.
- [741] Ilja D. Shkredov: Szemere´di’s theorem and problems of arithmetic progressions. Uspekhi Mat. Nauk 61 (6) (2006) 6(372), 111–178; translation in Russian Math. Surveys 61 (6) (2006), 1101–1166
- [742] Alexander F. Sidorenko: Extremal estimates of probability measures and their combinatorial nature. (Russian) Izv. Akad. Nauk SSSR Ser. Mat. 46 (3) (1982), 535–568,
- [743] A.F. Sidorenko: The maximal number of edges in a homogeneous hypergraph containing no prohibited subgraphs, Mathematical Notes 41 (1987), 247–259. Translated from Matematicheskie Zametki.
- [744] A.F. Sidorenko: An unimprovable inequality for the sum of two symmetrically distributed random vectors. (Russian) Teor. Veroyatnost. i Primenen. 35 (3)

- (1990), 595–599; translation in Theory Probab. Appl. 35 (3) (1990), 613–617
- (1991)


- [745] A.F. Sidorenko: Inequalities for functional generated by bipartite graphs, Discrete Math. Appl. 3 (3) (1991) 50–65 (in Russian); English transl., Discrete Math. Appl. 2 (5) (1992) 489–504.
- [746] A.F. Sidorenko: A correlation inequality for bipartite graphs, Graphs Combin. 9 (1993) 201–204.
- [747] A.F. Sidorenko: Boundedness of optimal matrices in extremal multigraph and digraph problems, Combinatorica 13 (1993), 109–120.
- [748] A.F. Sidorenko: What we know and what we do not know about Tur´an numbers, Graphs and Combinatorics 11 (1995), 179–199.
- [749] A.F. Sidorenko: An Erd˝s-Gallai-type theorem for keyrings, submitted,
- [750] M. Simonovits: A method for solving extremal problems in graph theory, Theory of Graphs, Proc. Colloq. Tihany, (1966), (Ed. P. Erd˝s and G. Katona) Acad. Press, N.Y., (1968) pp. 279–319.
- [751] M. Simonovits: On the structure of extremal graphs, PhD thesis (1969), (Actually, “Candidate”, in Hungarian).
- [752] M. Simonovits: On colour-critical graphs. Studia Sci. Math. Hungar. 7 (1972), 67–81.
- [753] M. Simonovits: Note on a hypergraph extremal problem, in: C. Berge, D. RayChaudury (Eds.), Hypergraph Seminar, Columbus, Ohio, USA, 1972, Lecture Notes in Mathematics, Vol. 411, Springer, Berlin, (1974), pp. 147–151.
- [754] M. Simonovits: The extremal graph problem of the icosahedron. J. Combinatorial Theory Ser. B 17 (1974) 69–79.
- [755] M. Simonovits: Extremal graph problems with symmetrical extremal graphs, additional chromatic conditions, Discrete Mathematics 7 (1974), 349–376.
- [756] M. Simonovits: On Paul Tur´an’s inﬂuence on graph theory, J. Graph Theory 1

(2) (1977), 102–116.

- [757] M. Simonovits: Extremal graph theory, in: L.W. Beineke, R.J. Wilson (Eds.), Selected Topics in Graph Theory II., Academic Press, London, (1983), pp. 161– 200.
- [758] M. Simonovits: Extremal graph problems and graph products, in Studies in


- Pure Mathematics, Birkh¨auser, Basel, 1983, pp. 669–680.
- [759] M. Simonovits: Extremal graph problems, Degenerate extremal problems and Supersaturated graphs, Progress in Graph Theory (Acad. Press, ed. Bondy and Murty) (1984) 419–437.
- [760] M. Simonovits: Paul Erd˝s’ inﬂuence on extremal graph theory, The mathematics of Paul Erd˝s, II, 148–192, Algorithms Combin., 14 (1997), Springer, Berlin. (See also with the same title an updated version, in “The Mathematics of Paul Erd˝s” (eds Graham, Butler, Nesˇetrˇil, 2013)
- [761] M. Simonovits: How to solve a Tur´an type extremal graph problem? (linear decomposition), Contemporary trends in discrete mathematics (Stirin Castle, 1997), pp. 283–305, DIMACS Ser. Discrete Math. Theoret. Comput. Sci., 49

(1999), Amer. Math. Soc., Providence, RI.

- [762] M. Simonovits: Paul Erd˝s’ Inﬂuence on Extremal Graph Theory (Updated/Extended version of [760]), Springer, (2013) (eds Baker, Graham and Nesˇetrˇil).
- [763] M. Simonovits: Paul Tur´an’s inﬂuence in Combinatorics, in Tur´an Memorial: Number Theory, Analysis, and Combinatorics 309–392, De Gruyter, (2013).
- [764] M. Simonovits and V.T. S´os: Szemere´di’s partition and quasirandomness, Random Struct. Algorithms 2 (1991), 1–10.
- [765] M. Simonovits and V.T. S´os: Hereditarily extended properties, quasi-random graphs and not necessarily induced subgraphs, Combinatorica 17 (1997), 577– 596.
- [766] M. Simonovits and V.T. S´os: Ramsey-Tur´an theory. Combinatorics, graph theory, algorithms and applications. Discrete Math. 229 (1-3) (2001) 293–340.
- [767] M. Simonovits and V.T. S´os: Hereditarily extended properties, quasi-random graphs and induced subgraphs, Combin. Probab. Comput. 12 (2003), 319–344.
- [768] Jozef Skokan and Lubosˇ Thoma: Bipartite subgraphs and quasi-randomness. Graphs Combin. 20 (2) (2004), 255–262.
- [769] J´ozsef Solymosi: Regularity, uniformity, and quasirandomness. Proc. Natl. Acad. Sci. USA 102 (23) (2005), 8075–8076.
- [770] J. Solymosi: On the number of sums and products. Bulletin of the London Mathematical Society 37 (2005) 491–494.
- [771] J. Solymosi: The (7, 4)-conjecture in ﬁnite groups. Combin. Probab. Comput. 24 (4) (2015) 680–686.
- [772] Vera T. S´os: On extremal problems in graph theory, Combinatorial Structures and their Applications (Proc. Calgary Internat. Conf., Calgary, Alta., 1969) pp. 407–410 Gordon and Breach, New York (1970)
- [773] V.T. S´os: Remarks on the connection of graph theory, ﬁnite geometry and block designs; in: Teorie Combinatorie, Tomo II, Accad. Naz. Lincei, Rome, (1976), 223–233.
- [774] V.T. S´os: An additive problem in diﬀerent structures, in: Proc. of the Second Int. Conf. in Graph Theory, Combinatorics, Algorithms, and Applications, San Fra. Univ., California, July 1989, SIAM, Philadelphia, (1991), pp. 486–510.
- [775] V.T. S´os: Turbulent years: Erd˝s in his correspondence with Tur´an from 1934 to 1940. Paul Erd˝s and his mathematics, I (Budapest, 1999), 85–146, Bolyai Soc. Math. Stud., 11 (2002), J´anos Bolyai Math. Soc., Budapest.
- [776] Joel Spencer: Ramsey’s theorem – a new lower bound. J. Combinatorial Theory Ser. A 18 (1975), 108–115.
- [777] J. Spencer: “Ten Lectures on the Probabilistic Method,” SIAM, Philadelphia,


(1987).

- [778] J. Spencer: Eighty years of Ramsey R(3, k). . . and counting! Ramsey theory, 27–39, Progress in Math., 285 (2011) Birkh¨auser/Springer, New York.
- [779] J. Spencer: Erd˝s magic. The mathematics of Paul Erd˝os. I, 43–46, Springer, New York, (2013).
- [780] Ladislas Stacho: Locally pancyclic graphs, J. Combin. Theory Ser. B 76 (1999), 22–40.
- [781] Angelika Steger: The determinism of randomness and its use in combinatorics. Proceedings of the International Congress of Mathematicians—Seoul 2014. Vol. IV, 475–488, Kyung Moon Sa, Seoul, (2014).
- [782] Michael Stiebitz: Subgraphs of colour-critical graphs. Combinatorica 7 (3)

(1987) 303–312.

- [783] M. Stiebitz, Zs. Tuza, and Margit Voigt: On list critical graphs. Discrete Math. 309 (15) (2009) 4931–4941.
- [784] Anne P. Street: Sum-free sets. In: Lecture Notes in Math. 292 (1972), 123–272. Springer.
- [785] Benny Sudakov: A few remarks on Ramsey-Tur´an-type problems, J. Combin. Theory Ser. B 88 (1) (2003) 99–106.
- [786] B. Sudakov and V.H. Vu: Local resilience of graphs. Random Structures and Algorithms 33 (4) (2008), 409–433.
- [787] Bal´azs Szegedy: Gowers norms, regularization and limits of functions on abelian groups, preprint. arXiv1010.6211.
- [788] E. Szemere´di: On sets of integers containing no four elements in arithmetic progression. Acta Math. Acad. Sci. Hungar. 20 (1969) 89–104.
- [789] E. Szemere´di: On graphs containing no complete subgraph with 4 vertices (Hungarian), Mat. Lapok 23 (1972), 113–116.
- [790] E. Szemere´di: On sets of integers containing no k elements in arithmetic progression, Acta Arith. 27 (1975) 199–245, Collection of articles in memory of Jurii Vladimirovich Linnik.
- [791] E. Szemere´di: Regular partitions of graphs. In Proble`mes combinatoires et the´orie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), volume 260 of Colloq. Internat. CNRS, pages 399–401. CNRS, Paris, 1978.
- [792] E. Szemere´di: Integer sets containing no arithmetic progressions, Acta Math. Hungar, 56 (1990), 155–158.
- [793] E. Szemere´di: Is laziness paying oﬀ? (“Absorbing” method). Colloquium De Giorgi 2010–2012, 17–34, Colloquia, 4, Ed. Norm., Pisa, 2013.
- [794] E. Szemere´di: Arithmetic progressions, diﬀerent regularity lemmas and removal lemmas. Commun. Math. Stat. 3 (3) (2015), 315–328.
- [795] E. Szemere´di: Erd˝s’s unit distance problem. Open problems in mathematics, 459–477, Springer, [Cham], 2016.
- [796] E. Szemere´di and W.T. Trotter Jr.: Extremal problems in discrete geometry. Combinatorica 3 (3-4) (1983), 381–392.
- [797] Terrence C. Tao: Szemere´di’s regularity lemma revisited. Contrib. Discrete Math. 1 (1) (2006), 8–28.
- [798] T.C. Tao: A variant of the hypergraph removal lemma, Journal of Combinatorial Theory, Ser. A 113 (2006), 1257–1280.
- [799] T.C. Tao: The Gaussian primes contain arbitrarily shaped constellations, J. Anal. Math. 99 (2006), 109–176.
- [800] T.C. Tao and V.H. Vu: Additive Combinatorics, volume 105 of Cambridge Studies in Advanced Mathematics, Cambridge University Press, 2006.
- [801] T.C. Tao and V.H. Vu: Sum-free sets in groups: a survey. J. Comb. 8 (3) (2017)


- 541–552.
- [802] Andrew Thomason: Pseudorandom graphs, Random graphs ’85 (Poznan´, 1985), North-Holland Math. Stud., 144 (1987) North-Holland, Amsterdam, 307–331.
- [803] A. Thomason: Random graphs, strongly regular graphs and Pseudorandom graphs, in: Surveys in combinatorics 1987 (New Cross, 1987), 173–195.
- [804] C. Thomassen: Long cycles in digraphs with constraints on the degrees, in: B. Bollob´s (Ed.), Surveys in Combinatorics, in: London Math. Soc. Lecture Notes, vol. 38 (1979) pp. 211–228. Cambridge University Press.
- [805] Craig Timmons and Jacques Verstrae¨te: A counterexample to sparse removal. European J. Combin. 44 (2015), part A, 77–86.
- [806] Bjarne Toft: Two theorems on critical 4-chromatic graphs. Studia Sci. Math. Hungar. 7 (1972), 83–89.
- [807] Paul Tur´an: On an extremal problem in graph theory (in Hungarian). Mat. Fiz. Lapok 48 (1941) 436–452. (For its English version see [810].)
- [808] P. Tur´an: On the theory of graphs, Colloq. Math. 3 (1954) 19–30.
- [809] P. Tur´an: Applications of graph theory to geometry and potential theory. Combinatorial Structures and their Applications (Proc. Calgary Internat. Conf., Calgary, Alta., 1969) pp. 423–434 Gordon and Breach, New York (1970)
- [810] P. Tur´an: Collected papers. Akade´miai Kiado´, Budapest, 1989. Vol. 1-3, (with comments of Simonovits on Tur´an’s papers in Combinatorics and by others on other topics).
- [811] Michail Tyomkyn and Andrew J. Uzzell: Strong Tur´an stability. Electron. J. Combin. 22 (3) (2015), Paper 3.9, 24 pp.
- [812] Bartel L. van der Waerden: Beweis einer Baudetschen Vermutung, Nieuw Arch. Wisk. 15 (1927), 212–216.
- [813] Richard Wenger: Extremal graphs with no C4,s, C6,s or C10,s J. Combin. Theory Ser. B, 52 (1991), 113–116.
- [814] Richard M. Wilson: An existence theory for pairwise balanced designs. I. Composition theorems and morphisms. J. Combinatorial Theory Ser. A 13 (1972), 220–245.
- [815] R.M. Wilson: An existence theory for pairwise balanced designs. II. The structure of PBD-closed sets and the existence conjectures. J. Combinatorial Theory Ser. A 13 (1972), 246–273.
- [816] R.M. Wilson: An existence theory for pairwise balanced designs. III. Proof of the existence conjectures. J. Combinatorial Theory Ser. A 18 (1975) 71–79.
- [817] R.M. Wilson: Decompositions of complete graphs into subgraphs isomorphic to a given graph, in: Proceedings of the Fifth British Combinatorial Conference, Univ. Aberdeen, Aberdeen, 1975, Congressus Numerantium, No. XV, Utilitas Math., Winnipeg, Man., 1976, pp. 647–659.
- [818] Hian Poh Yap: Maximal sum-free sets of group elements, Journal of the London Mathematical Society 44 (1969), 131–136.
- [819] H.P. Yap: Maximal sum-free sets in ﬁnite abelian groups. V., Bull. Austral. Math. Soc. 13 (3) (1975) 337–342.
- [820] Raphael Yuster: Tiling transitive tournaments and their blow-ups. Order 20

(2) (2003), 121–133.

- [821] R. Yuster: Quasi-randomness is determined by the distribution of copies of a ﬁxed graph in equicardinal large sets, In Proceedings of the 12th International Workshop on Randomization and Computation (RANDOM), Springer Verlag, Boston, MA, 2008, pp. 596–601.
- [822] Yi Zhao: Bipartite graph tiling. SIAM J. Discrete Math. 23 (2) (2009), 888–900.


- [823] Yi Zhao: Proof of the (n/2 − n/2 − n/2) Conjecture for large n, Electron. J. Combin., 18 (2011), 27. 61 pp.
- [824] Yi Zhao: Recent advances on Dirac-type problems for hypergraphs, in: Recent Trends in Combinatorics, the IMA Volumes in Mathematics and its Applications, vol. 159, Springer, New York, 2016.
- [825] Alexander A. Zykov: On some properties of linear complexes. Mat. Sb. 24 (66)

(1949), 163–188. (in Russian); English translation in Amer. Math. Soc. Transl., 1952 (1952), 79.

— · —

- [826] Paul Erd˝s’ homepage is: www.renyi.hu/˜p erdos

![image 734](<2019-simonovits-embedding-graphs-larger-graphs_images/imageFile734.png>)

- [827] Mikl´os Simonovits’ homepage is: www.renyi.hu/˜miki


