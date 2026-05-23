---
type: source
kind: paper
title: Nut graphs with a given automorphism group
authors: Nino Bašić, Patrick W. Fowler
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2405.04117v1
source_local: ../raw/2024-bai-nut-graphs-given-automorphism.pdf
topic: general-knowledge
cites:
---

Nut graphs with a given automorphism group

Nino Bašić1,2,3 and Patrick W. Fowler4 1FAMNIT, University of Primorska, Koper, Slovenia 2IAM, University of Primorska, Koper, Slovenia 3Institute of Mathematics, Physics and Mechanics, Ljubljana, Slovenia 4Department of Chemistry, University of Sheﬃeld, Sheﬃeld S3 7HF, UK

arXiv:2405.04117v1[math.CO]7May2024

May 8, 2024

Abstract

A nut graph is a simple graph of order 2 or more for which the adjacency matrix has a single zero eigenvalue such that all non-zero kernel eigenvectors have no zero entry (i.e. are full). It is shown by construction that every ﬁnite group can be represented as the group of automorphisms of inﬁnitely many nut graphs. It is further shown that such nut graphs exist even within the class of regular graphs; the cases where the degree is 8,12,16,20 or 24 are realised explicitly.

Keywords: Nut graph, graph automorphism, automorphism group, nullity, graph spectra, f-universal.

Math. Subj. Class. (2020): 05C25, 05C50.

# 1 Introduction

A problem posed in Kőnig’s 1936 book on Graph Theory [36, p. 5] asks when a given abstract group can be represented as the group of automorphisms of a (ﬁnite) graph G, and when this is the case, how the graph can be constructed1. In response, Frucht ﬁrst solved the problem in its original form [30]. Later, he showed that solution is still possible under the extra requirement that G is a cubic graph [31]. In both cases he gave an explicit construction. Sabidussi [42] reﬁned the question and proved that every group can be represented by a graph with additional properties such as: prescribed chromatic number, prescribed vertex-connectivity, or regularity with prescribed degree. An early survey paper by Babai [5] reviews this research direction and deﬁnes the term f-universal: a class of graphs C is f-universal if for every ﬁnite group G there exists a graph G ∈ C such that Aut(G) ∼= G. Not all famous graph classes are f-universal; for example, Babai has shown that there are inﬁnitely many ﬁnite groups which cannot be realised by a planar graph [2, 4]. Kőnig’s question has also been extended from graphs to other combinatorial objects, such as tournaments [39], Steiner triple and quadruple systems [38], and cycle systems [34, 37]. Here, we consider Kőnig’s original question, but for nut graphs.

A nut graph is a singular simple graph with nullity 1, where the non-trivial kernel eigenvector has only non-zero entries. Nut graphs occur in several chemical applications [45]: they are connected, leaﬂess and non-bipartite [48]. Catalogues have been constructed [15, 16, 11, 14]: nut graphs may be regular, vertex-transitive [28, 8] (including GRRs [40, 41] and non-Cayley graphs), but are not edge-transitive [7]; they may be chemical graphs [29], including some cubic polyhedra [46] and, in particular, fullerenes [47]. Recently, a comprehensive theory of circulant nut graphs has been developed [24, 21, 20, 22]. The study of polycirculant nut graphs [23] has also been initiated.

![image 1](<2024-bai-nut-graphs-given-automorphism_images/imageFile1.png>)

1“Wann kann eine gegebene abstrakte Gruppe als die Gruppe eines Graphen aufgefaßt werden und – ist des der Fall

– wie kann die entsprechende Graph konstruoert werden?”

Here, we prove a Sabidussi-type result for the class of nut graphs: we show that the graph G that realises a given automorphism group can be chosen to satisfy the requirements of the nut-graph deﬁnition; hence, nut graphs are f-universal (in the sense of [5]). We prove that:

- Theorem 1. For every ﬁnite group G there exist inﬁnitely many ﬁnite nut graphs G, such that

- Aut(G) ∼= G. Furthermore, we can require that the graph G is also regular.


- Theorem 2. For every ﬁnite group G and d ∈ {8,12,16,20,24} there exist inﬁnitely many ﬁnite d-regular nut graphs G, such that Aut(G) ∼= G.


# 2 Preliminaries

All graphs considered in this paper are ﬁnite, simple and connected. The adjacency matrix of graph G is A(G) and the dimension of the nullspace of A(G) is the nullity, η(G). An automorphism α of a graph G is a permutation α: V (G) → V (G) of the vertices of G that maps edges to edges and non-edges to non-edges. The set of all automorphisms of a graph G forms a group, the (full) automorphism group of G, denoted by Aut(G). The image of a vertex v ∈ V (G) under automorphism α will be denoted vα. For other standard deﬁnitions we refer the reader to one of the many comprehensive treatments of the theory of graph spectra (e.g. [18, 19, 13, 17, 12]). and algebraic graph theory (e.g. [33, 26, 9]).

Nut graphs [48] are graphs that have a one-dimensional nullspace (i.e., η(G) = 1), where the nontrivial kernel eigenvector x = [x1 ... xn]⊺ ∈ ker A(G) is full (i.e., |xi| > 0 for all i = 1,... ,n). As the deﬁning paper considered the isolated vertex to be a trivial case [48], non-trivial nut graphs have seven or more vertices. If G is a regular nut graph, then δ(G) = d(G) = ∆(G) ≥ 3. Note that there are no nut graphs with ∆(G) = 2, as no cycle has nullity 1.

In what follows, it will be useful to have constructions that are guaranteed to produce a nut graph, when applied to a starting graph of speciﬁed type. For example, let G be a nut graph and e ∈ E(G) an arbitrary edge. Then the graph obtained from G by subdividing the edge e four times is again a nut graph; this is the subdivision construction [48]. Two further constructions that will prove useful in what follows are now described.

The ﬁrst is the coalescence construction: Let G1 and G2 be graphs and let v1 ∈ V (G1) and v2 ∈ V (G2). The coalescence of (G1,v1) and (G2,v2), which we denote here as (G1,v1) ⊙ (G2,v2), is the graph obtained from the disjoint union of G1 and G2 by identifying root vertices v1 and v2. Sciriha obtained the following result [44, Corollary 21].

Lemma 3 ([44]). Let G1 and G2 be nut graphs. Then the coalescence (G1,v1) ⊙ (G2,v2) is a nut graph.

The coalescence construction must be provided with an initial collection of nut graphs. The second construction is diﬀerent in that it produces a nut graph from any (2t)-regular graph.

- Proposition 4 ([7]). Let G be a connected (2t)-regular graph, where t ≥ 1. Let M3(G) be the graph obtained from G by fusing a bouquet of t triangles to every vertex of G. Then M3(G) is a nut graph.

The construction M3(G) is called the triangle-multiplier construction [7]. The choice of name is justiﬁed by the fact that |V (M3(G))| = (2t + 1)|V (G)|. Its eﬀect on the automorphism group is described by the following proposition.

- Proposition 5 ([7]). Let G be a connected (2t)-regular graph, where t ≥ 1. Then Aut(G) ≤ Aut(M3(G)) and |Aut(M3(G))| = (2tt!)|V (G)||Aut(G)|.


The group Aut(G) also acts on M3(G). The additional automorphisms in Aut(M3(G)) are wellunderstood. They arise from swapping the two degree-2 endvertices of the attached triangles and from permuting the triangles attached to a given vertex of graph G.

As mentioned above, Sabidussi showed for a range of properties, that they can be required of the graph that realises a given ﬁnite group. Theorem 3.7 in [42] is more general than we need here; in a version tailored for our purposes, it is:

Theorem 6 ([42]). For every ﬁnite group G of order |G| > 1 and d ≥ 3 there exist inﬁnitely many connected d-regular graphs G, such that Aut(G) ∼= G.

The theorem of Sabidussi requires the group G to be non-trivial. However, as Bollobás has shown, a consequence of [10, Theorem 6] is that for d ≥ 3 almost every d-regular graph is asymmetric. Thus it is easy to incorporate the trivial case into Theorem 6 and the requirement |G| > 1 could be omitted. Theorem 6 is the jumping-oﬀ point for our proofs.

# 3 Proof of Theorem 1

We are now ready to prove the main theorem. We will exploit a combination of the triangle-multiplier and coalescence constructions.

- Proof of Theorem 1. If |G| > 1, then by Theorem 6, there exists a 4-regular graph H, such that


- Aut(H) ∼= G. In the case |G| = 1, simply take H to be the graph from Figure 3(a), i.e. an asymmetric 4-regular graph of the minimum order. By Proposition 4, the graph M3(H) is a nut graph such that Aut(H) ≤ Aut(M3(H)). By Proposition 5, |Aut(M3(H))| = 8|V (H)||Aut(H)|.


Let us denote κ = |V (H)| and V (H) = {h1,h2,... ,hκ}. By deﬁnition, H ⊂ M3(H). Let the extra vertices be denoted t(ij,k) for 1 ≤ i ≤ κ and j,k ∈ {1,2} such that the new neighbours of hi are t(1i ,1),t(1i ,2),t(2i ,1) and t(2i ,2). Moreover, ti(j,1) and t(ij,2) are adjacent; see Figure 1.

t(12 ,2) t(22 ,1)

t(12 ,1)

t(22 ,2)

- t(21 ,1)

- t(21 ,2)


H

h2

h1

- t(11 ,1)

- t(11 ,2)


···

Figure 1: The graph M3(H).

The automorphisms of M3(H) are well-understood. Every α ∈ Aut(H) is extended to an automorphism α ∈ Aut(M3(H)) by the following natural deﬁnition:

α(v) =

α(v), if v ∈ V (H); t(ℓj,k), if v = t(ij,k) and hℓ = α(hi).

In addition to α for α ∈ Aut(H), there are the following extra automorphisms in Aut(M3(H)):

(1)

βi,j = (t(ij,1) t(ij,2)), (2)

γi = (t(1i ,1) t(2i ,1))(t(1i ,2) t(2i ,2)), (3) for i = 1,... ,κ and j = 1,2.

We will remove the extra automorphisms by attaching ‘gadgets’ to vertices t(1i ,1) and t(2i ,1) for i = 1,... ,κ. Consider the graph Q0 in Figure 2. It is easy to verify that Q0 is a nut graph of order 8 with |Aut(Q0)| = 2, and that vertices labelled q1 and q2 belong to diﬀerent vertex orbits. Moreover, the respective stabilisers Aut(Q0)q1 and Aut(Q0)q2 are trivial.

Let G be the graph obtained from M3(H) by a series of coalescence constructions. Start with

- G0 := M3(H). For i = 1,... ,κ deﬁne Gi := (Gi−1,t(1i ,1)) ⊙ (Q0,q1). (The graph Gi is obtained from Gi−1 by adding a new copy of Q0 to Gi−1 and identifying q1 with the vertex t(1i ,1).) For i = 1,... ,κ


deﬁne Gi+κ := (Gi+κ−1,t(2i ,1)) ⊙ (Q0,q2). By Lemma 3, G1,G2,... ,G2κ are all nut graphs. Let G := G2κ.

q2

q1

- Figure 2: The gadget graph Q0. The root vertices used in the ﬁrst and second attachment are labelled q1 and q2, respectively.

Next, observe that automorphisms α can be extended naturally from M3(H) to G. However, all

automorphisms βi,j have been removed, since vertices t(ij,1) now carry gadgets, while vertices t(ij,2) do not (they are still of degree 2). Similarly, all automorphisms γi have been removed, since the gadget

attached to t(1i ,1) does not map to the gadget attached to t(1i ,2), as vertices q1 and q2 are in diﬀerent vertex orbits of Q0. Moreover, no new automorphisms have been introduced, as vertices q1,q2 ∈ V (Q0) have trivial stabilisers. Therefore, Aut(G) ∼= Aut(H) ∼= G.

We provided one nut graph G which realises the group G. To obtain an inﬁnite family, we can

subdivide each edge from {hit(1i ,2) | i = 1,... ,κ} with 4σ vertices for any choice of σ ≥ 0, i.e. we use the subdivision construction on these edges.

![image 2](<2024-bai-nut-graphs-given-automorphism_images/imageFile2.png>)

![image 3](<2024-bai-nut-graphs-given-automorphism_images/imageFile3.png>)

![image 4](<2024-bai-nut-graphs-given-automorphism_images/imageFile4.png>)

![image 5](<2024-bai-nut-graphs-given-automorphism_images/imageFile5.png>)

Note that there are many ‘degrees of freedom’ in the proof of Theorem 1. In our construction, we could have taken H to be any 4-regular graph that realises the given group G. In case |G| > 1, Theorem 6 already provides inﬁnitely many starting graphs H (which in turn produce inﬁnitely many non-isomorphic nut graphs G). If |G| = 1, by [10], there are also inﬁnitely many startings graphs H. At the coalescence stage, we could have picked diﬀerent vertices as q1 and q2 in Q0 (so long as they are in diﬀerent vertex orbits). We could also have choosen a diﬀerent gadget graph for Q0, or taken two diﬀerent gadget graphs. We could have decorated both triangles with the same gadget and taken q1 = q2; that choice would have removed only elements βi,j; to further remove elements γi, we could have used the subdivision construction on edges hit(1i ,2).

The multiplier-coalescence construction is prodigal in terms of the number of vertices of the nut graphs obtained. The order of graph G provided by the proof of Theorem 1 is 19|V (H)|, where |V (H)| is the order of the graph H. For a given group G, |G| > 3, with ν generators, the smallest 4-regular graph of the family constructed by Sabidussi in [42] is of order 4(ν + 2)|G|. Therefore, the order of the smallest graph obtained from Sabidussi’s starting graph is 76(ν + 2)|G|.

(a) (b) (c)

- Figure 3: Graphs that realise the minimum order among 4-regular graphs with automorphism groups


Z1,Z2 and Z3, respectively. These graphs are not uniquely determined; they are selected from sets of

- 4, 3 and 8 candidates, respectively.


Typically, much smaller examples can exist. Instead of the graph provided by the construction in the proof by Sabidussi, we could take the starting graph H to be a minimal 4-regular graph that realises G. For groups Z1,Z2 and Z3, minimal graphs H are shown in Figure 3. These have orders 10,9 and 14, respectively. Application of the multiplier-coalescence construction gives rise to nut graphs of respective orders 190,171 and 266.

# 4 Proof of Theorem 2

- Proof of Theorem 2. The proof proceeds as for Theorem 1 to the point where gadgets are attached to M3(H).


First, we prove the case d = 8. Consider the graphs P1,P2 and P3 in Figure 4. They are nonisomorphic graphs; each of them contains six degree-3 vertices and six degree-4 vertices. The gadget Qi, 1 ≤ i ≤ 3, is obtained from Pi by adding a new vertex wi to its complement Pi and joining wi to all degree-7 vertices of Pi. Observe that Q1,Q2 and Q3 are non-isomorphic graphs of order 13. All vertices of Qi are of degree 8, except for wi which is of degree 6. It is easy to verify that Q1,Q2 and Q3 are nut graphs and that their automorphism groups are trivial.

![image 6](<2024-bai-nut-graphs-given-automorphism_images/imageFile6.png>)

![image 7](<2024-bai-nut-graphs-given-automorphism_images/imageFile7.png>)

(a) P1 (b) P2 (c) P3

Figure 4: The proto-gadget graphs for the proof of Theorem 2 in the case d = 8. As in the proof of Theorem 1, we obtain G by a series of coalescence constructions. Start with

- G0 := M3(H). For i = 1,... ,κ deﬁne Gi := (Gi−1,t(1i ,1)) ⊙ (Q1,w1). For i = 1,... ,κ deﬁne Gi+κ := (Gi+κ−1,t(2i ,1)) ⊙ (Q1,w1). For i = 1,... ,κ deﬁne Gi+2κ := (Gi+2κ−1,t(1i ,2)) ⊙ (Q2,w2). For


i = 1,... ,κ deﬁne Gi+3κ := (Gi+3κ−1,t(2i ,2)) ⊙ (Q3,w3). In other words, gadgets Q1,Q2 and Q3 are attached to degree-2 vertices of the triangles as indicated schematically in Figure 5(a). By Lemma 3,

G1,G2,... ,G4κ are all nut graphs. Let G := G4κ.

By similar reasoning to that used in the proof of Theorem 1, we can see that automorphisms α can be extended naturally from M3(H) to G. Moreover, the gadgets Q1,Q2 and Q3 were attached in a manner such that automorphisms βi,j and γi were removed. Further, attachment has introduced no new automorphisms, as these gadgets all have trivial symmetry. Hence, Aut(G) ∼= Aut(H) ∼= G. Finally, observe that all vertices of G are of degree 8. This proves the case d = 8. For higher values of d the proof is similar, but the search for the requisite number of proto-gadgets becomes rapidly more tedious.

To prove the result for a given d, we start with a (d/2)-regular graph H that realises the group

- G. If |G| > 1, Theorem 6 provides us with inﬁnitely many such graphs H. If |G| = 1, by [10], there

are also inﬁnitely many such graphs H. By Proposition 4, M3(H) is a nut graph. In this graph, there are d/4 triangles attached at every vertex of H. To remove the unwanted symmetries, every

triangle is decorated by a diﬀerent pair of gadgets. (See Figure 5.) With s gadgets, we can form 2 s diﬀerent pairs. We choose the smallest s such that 2 s ≥ d/4. Figure 6 tabulates a suﬃcient set of proto-gadgets for degrees 12,16,20 and 24. The complement of Pi(d) contains d − 2 vertices of degree d−1, and the remaining vertices are of degree d. To obtain Qi(d), add a new vertex to the complement of Pi(d) and connect it to all vertices of degree d − 1. Graph Qi(d) has exactly one vertex of degree d − 1, while the rest are of degree d. It is easy to verify that graphs Q1(d),Q2(d),... are non-isomorphic and that they all have trivial symmetry.

![image 8](<2024-bai-nut-graphs-given-automorphism_images/imageFile8.png>)

![image 9](<2024-bai-nut-graphs-given-automorphism_images/imageFile9.png>)

![image 10](<2024-bai-nut-graphs-given-automorphism_images/imageFile10.png>)

![image 11](<2024-bai-nut-graphs-given-automorphism_images/imageFile11.png>)

We note that there are other strategies for the choice of gadgets in the proof. For example, one may prefer to ﬁnd one gadget and then, to generate the others, repeatedly apply a construction that preserves symmetry but does not produce vertices of unwanted degree. One candidate is the so-called Fowler construction [7]. This approach would lead to a nut graph of yet larger order than the one generated by the present proof. The order of graph G constructed in the proof of Theorem 2 is ω(d)|V (H)|, where ω(8) = 53, ω(12) = 99, ω(16) = 161, ω(20) = 241, and ω(24) = 337. Recall that

- H denotes a (d/2)-regular starting graph that realises G.


Q1

- Q1
- Q2


hi

Q3

(a) d = 8

Q1

Q2

Q1

hi

- Q2

Q3

- Q3


(b) d = 12

- Figure 5: Arrangements of gadgets Qi on degree-2 vertices of a bouquet of triangles that remove unwanted automorphisms (for the cases d = 8 and d = 12).

(a) P1(12) (b) P2(12) (c) P3(12)

(d) P1(16) (e) P2(16) (f) P3(16) (g) P4(16)

(h) P1(20) (i) P2(20) (j) P3(20) (k) P4(20)

(l) P1(24) (m) P2(24) (n) P3(24) (o) P4(24)

- Figure 6: The proto-gadget graphs for the proof of Theorem 2 for cases d ∈ {12,16,20,24}. The set Pi(d) is used to construct the decorating gadgets Qi, as described in the proof.


# 5 Discussion

Constructive methods used to answer Kőnig’s question typically do not provide minimal examples. Let α(G) be the smallest order of the graphs representing the group G. Sabidussi [43] opened the question by studying the order of α(G) with respect to |G|. The value α(G) has been determined for various families of groups (see [1] for abelian groups and a survey in [50]). Babai [3] gave α(G) ≤ 2|G| provided that G ∈/ {Z3,Z4,Z5}; Deligeorgaki [25] improved this to α(G) ≤ |G|, with a longer list of exceptions that includes some inﬁnite families. Planar graphs have also been considered from this point of view (for a survey see [35]).

Nut graphs raise analogous questions. It is clear that the constructions using in proving Theorems 1 and 2 are far from minimal. As an example, consider the group G288 of order 288, deﬁned by its permutation representation

G288 = (1,2,3)(4,5)(6, 7, 8), (1,8)(2,7)(3,6)(4,9)(5,10), (7,8) .

In GAP [32], this group can be obtained by calling SmallGroup(288, 889). The smallest 4-regular graph representing this group that is given by Sabidussi’s construction (Theorem 6) is of order 5760. Expansion to a nut graph by the construction used in the proof of Theorem 1 gives order 109440. A much smaller 4-regular parent graph could have been used as the basis for that construction, since the smallest 4-regular graph representing G288 is of order 11; see Figure 7(a), leading to a nut graph of order 209. However, the database obtained by nutgen [15] reveals that the smallest nut graph that represents G288 has only 10 vertices; see Figure 7(b).

(a) (b)

Figure 7: (a) The smallest 4-regular graph, and (b) the smallest nut graph, that represent G288.

Let β(G) be the smallest order of the nut graphs representing the group G. It is evident that β(G) ≥ α(G). For groups up to order 6, the values are

α(Z1) = 1,β(Z1) = 9; α(Z2) = 2,β(Z2) = 8; α(Z3) = 9,β(Z3) = 11; α(Z4) = 10,β(Z4) = 11; α(Z2 × Z2) = 4,β(Z2 × Z2) = 7; α(Z5) = 15,β(Z5) = 15;

α(Z3 × Z2) = 11,β(Z3 × Z2) = 11; α(Z3 ⋊ Z2) = 3,β(Z3 ⋊ Z2) = 7.

These numbers were found by computer search of the available censuses of nut graphs [11, 14]. For Z5, [1, Lemma 5.2] gives us α(Z5) = 15 ≤ β(Z5). The equality β(Z5) = 15 was established by ﬁnding an example.

- Problem 7. Given any ﬁnite group G, ﬁnd a nut graph G of minimum order, such that Aut(G) ∼= G. Find an upper bound on β(G) in terms of |G|.

Another question relates to the degrees of regular nut graphs that represent groups G.

- Problem 8. Given a ﬁnite group G and an integer d ≥ 3, ﬁnd a d-regular nut graph G, such that Aut(G) ∼= G.


Theorem 2 supplies the answer for small cases d ≡ 0 (mod 4), and the same technique could be used to extend the list, but this still leaves unresolved all cases with d  ≡ 0 (mod 4). A missing case of particular interest is d = 3. The graphs that can be used to model conjugated carbon frameworks in Hückel theory and similar applications [49] are known as chemical graphs. A chemical graph in this deﬁnition is connected and subcubic. Cubic chemical graphs form an important subclass that includes the fullerenes [27]. Applications of nut graphs in theories of radical chemistry and molecular

conduction are described in [45]. Interestingly, the eponymous Frucht graph, introduced in [31] as a small graph that has trivial symmetry, is both cubic (in fact polyhedral) and a nut graph. It has order 12 and is the smallest cubic nut graph of trivial symmetry. Frucht also threated the group Z2 separately; his graph that realises this group (see [31, Fig. 2]) is not a nut graph. It is straightforward to show that his general constructions [31] for groups of order greater than 2 do not yield nut graphs. The repeated motifs devised by Frucht (the ‘corners’ [31]) give rise to at least one non-trivial kernel eigenvector with some zero entries in the constructed graph. Hence, it would be interesting to ﬁnd a construction that yields cubic nut graphs directly.

# Acknowledgements

We would like to thank our colleague Prof. Primož Potočnik for fruitful discussion and for drawing our attention to [31] during a research visit to Sheﬃeld. The work of Nino Bašić is supported in part by the Slovenian Research Agency (research program P1-0294 and research projects N1-0140 and J1-2481). PWF thanks the Leverhulme Trust for an Emeritus Fellowship on the theme of ‘Modelling molecular currents, conduction and aromaticity’ and the Francqui Foundation for the award of an International Francqui Professorship.

# References

- [1] W. C. Arlinghaus, The Classiﬁcation of Minimal Graphs with Given Abelian Automorphism Group, volume 330 of Memoirs of the American Mathematical Society, American Mathematical Society, Providence, RI, 1985, doi:10.1090/memo/0330.
- [2] L. Babai, Automorphism groups of planar graphs. I, Discrete Math. 2 (1972), 295–307, doi: 10.1016/0012-365x(72)90010-6.
- [3] L. Babai, On the minimum order of graphs with given group, Canad. Math. Bull. 17 (1974), 467–470, doi:10.4153/cmb-1974-082-9.
- [4] L. Babai, Automorphism groups of planar graphs. II, in: Inﬁnite and Finite Sets, North-Holland, Amsterdam-London, volume 10 of Colloq. Math. Soc. János Bolyai, pp. 29–84, 1975.
- [5] L. Babai, On the abstract group of automorphisms, in: Combinatorics, Cambridge University Press, Cambridge, volume 52 of London Mathematical Society Lecture Note Series, pp. 1–40, 1981.
- [6] N. Bašić and P. W. Fowler, Nut graphs with a given automorphism group: supplementary material (GitHub repository), https://github.com/nbasic/nut-graphs-automorphisms.
- [7] N. Bašić, P. W. Fowler and T. Pisanski, Vertex and edge orbits in nut graphs, Electron. J. Comb.

(2024), in press.

- [8] N. Bašić, M. Knor and R. Škrekovski, On 12-regular nut graphs, Art Discrete Appl. Math. 5

(2022), #P2.01, doi:10.26493/2590-9770.1403.1b1.

- [9] N. Biggs, Algebraic Graph Theory, Cambridge Mathematical Library, Cambridge University Press, Cambridge, 2nd edition, 1993.
- [10] B. Bollobás, Distinguishing vertices of random graphs, in: Graph Theory, North-Holland, Amsterdam-New York, volume 62 of North-Holland Mathematics Studies, pp. 33–49, 1982.
- [11] G. Brinkmann, K. Coolsaet, J. Goedgebeur and H. Mélot, House of Graphs: A database of interesting graphs, Discrete Appl. Math. 161 (2013), 311–314, doi:10.1016/j.dam.2012.07.018, available at https://hog.grinvin.org/.


- [12] A. E. Brouwer and W. H. Haemers, Spectra of Graphs, Universitext, Springer, New York, 2012, doi:10.1007/978-1-4614-1939-6.
- [13] F. R. K. Chung, Spectral Graph Theory, volume 92 of CBMS Regional Conference Series in Mathematics, American Mathematical Society, Providence, RI, 1997.
- [14] K. Coolsaet, S. D’hondt and J. Goedgebeur, House of graphs 2.0: A database of interesting graphs and more, Discrete Appl. Math. 325 (2023), 97–107, doi:10.1016/j.dam.2022.10.013.
- [15] K. Coolsaet, P. W. Fowler and J. Goedgebeur, Nut graphs, homepage of Nutgen, http://caagt.ugent.be/nutgen/.
- [16] K. Coolsaet, P. W. Fowler and J. Goedgebeur, Generation and properties of nut graphs, MATCH Commun. Math. Comput. Chem. 80 (2018), 423–444, http://match.pmf.kg.ac.rs/electronic_versions/Match80/n2/match80n2_423-444.pdf.
- [17] D. M. Cvetković, M. Doob and H. Sachs, Spectra of Graphs: Theory and Applications, Johann Ambrosius Barth, Heidelberg, 3rd edition, 1995.
- [18] D. M. Cvetković, P. Rowlinson and S. Simić, Eigenspaces of Graphs, volume 66 of Encyclopedia of Mathematics and its Applications, Cambridge University Press, Cambridge, 1997, doi:10.1017/ cbo9781139086547.
- [19] D. M. Cvetković, P. Rowlinson and S. Simić, An Introduction to the Theory of Graph Spectra, volume 75 of London Mathematical Society Student Texts, Cambridge University Press, Cambridge, 2010.
- [20] I. Damnjanović, On the nullities of quartic circulant graphs and their extremal null spaces, 2022, arXiv:2212.12959 [math.CO].
- [21] I. Damnjanović, Two families of circulant nut graphs, 2022, arXiv:2210.08334 [math.CO].
- [22] I. Damnjanović, Complete resolution of the circulant nut graph order-degree existence problem, Ars. Math. Contemp. (2023), doi:10.26493/1855-3974.3009.6df.
- [23] I. Damnjanović, N. Bašić, T. Pisanski and A. Žitnik, Classiﬁcation of cubic tricirculant nut graphs, Electron. J. Comb. (2024), in press.
- [24] I. Damnjanović and D. Stevanović, On circulant nut graphs, Linear Algebra Appl. 633 (2022), 127–151, doi:10.1016/j.laa.2021.10.006.
- [25] D. Deligeorgaki, Smallest graphs with given automorphism group, J. Algebraic Combin. 56 (2022), 609–633, doi:10.1007/s10801-022-01125-2.
- [26] T. Dobson, A. Malnič and D. Marušič, Symmetry in Graphs, volume 198 of Cambridge Studies in Advanced Mathematics, Cambridge University Press, Cambridge, 2022, doi:10.1017/ 9781108553995.
- [27] P. Fowler and D. Manolopoulos, An Atlas of Fullerenes, Dover Publications, 2007.
- [28] P. W. Fowler, J. B. Gauci, J. Goedgebeur, T. Pisanski and I. Sciriha, Existence of regular nut graphs for degree at most 11, Discuss. Math. Graph Theory 40 (2020), 533–557, doi:10.7151/ dmgt.2283.
- [29] P. W. Fowler, T. Pisanski and N. Bašić, Charting the space of chemical nut graphs, MATCH Commun. Math. Comput. Chem. 86 (2021), 519–538, https://match.pmf.kg.ac.rs/electronic_versions/Match86/n3/match86n3_519-538.pdf.
- [30] R. Frucht, Herstellung von Graphen mit vorgegebener abstrakter Gruppe, Compositio Math. 6


(1939), 239–250, http://www.numdam.org/item?id=CM_1939__6__239_0.

- [31] R. Frucht, Graphs of degree three with a given abstract group, Canad. J. Math. 1 (1949), 365–378, doi:10.4153/cjm-1949-033-6.
- [32] The GAP Group, GAP – Groups, Algorithms, and Programming, Version 4.13.0, 2024, https://www.gap-system.org.
- [33] C. Godsil and G. Royle, Algebraic Graph Theory, volume 207 of Graduate Texts in Mathematics, Springer-Verlag, New York, 2001, doi:10.1007/978-1-4613-0163-9.
- [34] M. J. Grannell, T. S. Griggs and G. J. Lovegrove, Even-cycle systems with prescribed automorphism groups, J. Combin. Des. 21 (2013), 142–156, doi:10.1002/jcd.21334.
- [35] C. J. Jones, L.-K. Lauderdale, S. E. Lubow and C. J. Triplitt, Vertex-minimal planar graphs with a prescribed automorphism group, J. Algebraic Combin. 53 (2021), 355–367, doi:10.1007/ s10801-019-00932-4.
- [36] D. Kőnig, Theorie Der Endlichen Und Unendlichen Graphen, AMS Chelsea Publishing Series, American Mathematical Society, 2001, originally published in 1936.
- [37] G. J. Lovegrove, Odd-cycle systems with prescribed automorphism groups, Discrete Math. 314

(2014), 6–13, doi:10.1016/j.disc.2013.09.006.

- [38] E. Mendelsohn, On the groups of automorphisms of Steiner triple and quadruple systems, J. Combin. Theory Ser. A 25 (1978), 97–104, doi:10.1016/0097-3165(78)90072-9.
- [39] J. W. Moon, Tournaments with a given automorphism group, Canadian J. Math. 16 (1964), 485–489, doi:10.4153/cjm-1964-050-9.
- [40] L. A. Nowitz and M. E. Watkins, Graphical regular representations of non-abelian groups. I, Canadian J. Math. 24 (1972), 993–1008, doi:10.4153/cjm-1972-101-5.
- [41] L. A. Nowitz and M. E. Watkins, Graphical regular representations of non-abelian groups. II, Canadian J. Math. 24 (1972), 1009–1018, doi:10.4153/cjm-1972-102-3.
- [42] G. Sabidussi, Graphs with given group and given graph-theoretical properties, Canadian J. Math. 9 (1957), 515–525, doi:10.4153/cjm-1957-060-7.
- [43] G. Sabidussi, On the minimum order of graphs with given automorphism group, Monatsh. Math. 63 (1959), 124–127, doi:10.1007/bf01299094.
- [44] I. Sciriha, Coalesced and embedded nut graphs in singular graphs, Ars Math. Contemp. 1 (2008), 20–31, doi:10.26493/1855-3974.20.7cc.
- [45] I. Sciriha and A. Farrugia, From Nut Graphs to Molecular Structure and Conductivity, volume 23 of Mathematical Chemistry Monographs, University of Kragujevac and Faculty of Science Kragujevac, Kragujevac, 2021.
- [46] I. Sciriha and P. W. Fowler, Nonbonding orbitals in fullerenes: Nuts and cores in singular polyhedral graphs, J. Chem. Inf. Model. 47 (2007), 1763–1775, doi:10.1021/ci700097j.
- [47] I. Sciriha and P. W. Fowler, On nut and core singular fullerenes, Discrete Math. 308 (2008), 267–276, doi:10.1016/j.disc.2006.11.040.
- [48] I. Sciriha and I. Gutman, Nut graphs: Maximally extending cores, Util. Math. 54 (1998), 257–272.
- [49] A. Streitwieser, Molecular Orbital Theory for Organic Chemists, Wiley International Edition, Wiley, 1961.
- [50] J. A. Woodruﬀ, A Survey of Graphs of Minimum Order with Given Automorphism Group, Master’s thesis, The University of Texas at Tyler, 2016, http://hdl.handle.net/10950/423.


