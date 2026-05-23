---
type: source
kind: paper
title: "The approximate Loebl-Komlós-Sós Conjecture II: The rough structure of LKS graphs"
authors: Jan Hladký, János Komlós, Diana Piguet, Miklós Simonovits, Maya J. Stein, Endre Szemerédi
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1408.3871v4
source_local: ../raw/2014-hladk-approximate-loebl-koml-s-s-conjecture.pdf
topic: general-knowledge
cites:
---

arXiv:1408.3871v4[math.CO]7Jan2016

The approximate Loebl–Koml´os–So´s Conjecture II: The rough structure of LKS graphs

Jan Hladk´y ∗ J´nos Koml´os† Diana Piguet‡ Mikl´os Simonovits§ Maya Stein¶ Endre Szemer´edi

Abstract

This is the second of a series of four papers in which we prove the following relaxation of the Loebl–Komlo´s–S´os Conjecture: For every α > 0 there exists a number k0 such that for every k > k0 every n-vertex graph G with at least (12 + α)n vertices of degree at least (1 + α)k contains each tree T of order k as a subgraph.

![image 1](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile1.png>)

In the ﬁrst paper of the series, we gave a decomposition of the graph G into several parts of diﬀerent characteristics; this decomposition might be viewed as an analogue of a regular partition for sparse graphs. In the present paper, we ﬁnd a combinatorial structure inside this decomposition. In the last two papers, we reﬁne the structure and use it for embedding the tree T.

Mathematics Subject Classiﬁcation: 05C35 (primary), 05C05 (secondary). Keywords: extremal graph theory; Loebl–Koml´os–So´s Conjecture; tree embedding; regularity lemma; sparse graph; graph decomposition.

![image 2](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile2.png>)

∗Corresponding author. Institute of Mathematics, Academy of Science of the Czech Republic. Zitna´ˇ 25, 110

- 00, Praha, Czech Republic. The Institute of Mathematics of the Academy of Sciences of the Czech Republic is supported by RVO:67985840. Email: honzahladky@gmail.com. The research leading to these results has received funding from the People Programme (Marie Curie Actions) of the European Union’s Seventh Framework Programme (FP7/2007-2013) under REA grant agreement umber 628974. Much of the work was done while supported by an EPSRC postdoctoral fellowship while aﬃliated with DIMAP and Mathematics Institute, University of Warwick.


†Department of Mathematics, Rutgers University, 110 Frelinghuysen Rd., Piscataway, NJ 08854-8019, USA ‡Institute of Computer Science, Czech Academy of Sciences, Pod Vod´arenskou veˇzˇı´ 2, 182 07 Prague, Czech Republic. With institutional support RVO:67985807. Supported by the Marie Curie fellowship FIST, DFG grant TA 309/2-1, Czech Ministry of Education project 1M0545, EPSRC award EP/D063191/1, and EPSRC Additional Sponsorship EP/J501414/1. The research leading to these results has received funding from the European Union Seventh Framework Programme (FP7/2007-2013) under grant agreement no. PIEF-GA-2009-253925. The work leading to this invention was supported by the European Regional Development Fund (ERDF), project “NTIS – New Technologies for Information Society”, European Centre of Excellence, CZ.1.05/1.1.00/02.0090.

§Re´nyi Institute, Budapest, Hungary. Supported by OTKA 78439, OTKA 101536, ERC-AdG. 321104 ¶Department of Mathematical Engineering, University of Chile, Santiago, Chile. Supported by Fondecyt Iniciacion

grant 11090141, Fondecyt Regular grant 1140766 and CMM Basal. Re´nyi Institute, Budapest, Hungary. Supported by OTKA 104483 and ERC-AdG. 321104

i

CONTENTS

![image 3](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile3.png>)

# Contents

- 1 Introduction 1
- 2 Notation and preliminaries 1

- 2.1 General notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
- 2.2 Regular pairs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
- 2.3 LKS graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3


- 3 Decomposing sparse graphs 3
- 4 Augmenting a matching 6

- 4.1 Regularized matchings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 4.2 Augmenting paths for matchings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


- 5 Rough structure of LKS graphs 17

- 5.1 Motivation for and intuition behind Lemma 5.4 . . . . . . . . . . . . . . . . . . . . . 17 5.1.1 Rough versus ﬁne structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
- 5.2 The role of Lemma 4.8 in the proof of Lemma 5.4 . . . . . . . . . . . . . . . . . . . . 21
- 5.3 Finding the structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23


- 6 Acknowledgements 32 Symbol index 34 General index 35 Bibliography 36


ii

![image 4](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile4.png>)

# 1 Introduction

This is the second of a series of four papers [HKP+a, HKP+b, HKP+c, HKP+d] in which we provide an approximate solution of the Loebl–Koml´os–So´s Conjecture. The conjecture reads as follows.

Conjecture 1.1 (Loebl–Koml´os–So´s Conjecture 1995 [EFLS95]). Suppose that G is an n-vertex graph with at least n/2 vertices of degree more than k − 2. Then G contains each tree of order k.

We discuss the history and state of the art in detail in the ﬁrst paper [HKP+a] of our series. The main result, which will be proved in [HKP+d], is the approximate solution of the Loebl–Koml´os–So´s Conjecture.

Theorem 1.2 (Main result [HKP+d]). For every α > 0 there exists a number k0 such that for any k > k0 we have the following. Each n-vertex graph G with at least (12 + α)n vertices of degree at least (1 + α)k contains each tree T of order k.

![image 5](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile5.png>)

In the ﬁrst paper [HKP+a] we exposed the techniques we use to decompose the host graph. In particular, we saw in [HKP+a, Lemma 3.14] that any graph satisfying the assumptions of Theorem 1.2 may be decomposed into a set of huge degree vertices, regular pairs, an expanding subgraph, and another set with certain expansion properties, which we call the avoiding set. We call this a sparse decomposition of a graph. We will recall the necessary notions from [HKP+a] in Section 3.

Many embedding problems for dense host graphs are attacked using the following three-step approach: (a) the regularity lemma is applied to the host graph, (b) a suitable combinatorial structure is found in the cluster graph, and (c) the target graph is embedded into the combinatorial structure using properties of regular pairs. If we consider the sparse decomposition as a sparse counterpart to (a) then the main result of the present paper, Lemma 5.4, should be regarded as a counterpart to (b). More precisely, for each graph satisfying the assertions of Theorem 1.2 that is given together with its sparse decomposition, Lemma 5.4 gives a combinatorial structure whose building blocks are the elements of the sparse decomposition. As in tree embedding problems in the dense setting (e.g. in [AKS95, PS12]), the core of this combinatorial structure is a well-connected matching consisting of regular pairs. We call such matchings regularized.

With the structure given by Lemma 5.4, one can convince oneself that the tree T from Theorem 1.2 can be embedded into the host graph, and indeed we provide such motivation in Section 5.1. However, the rigorous argument is far from trivial. One needs to reﬁne the structure found here, which is done in [HKP+c]. For this reason, we call the output of Lemma 5.4 the rough structure. In the last paper [HKP+d] of our series we will develop embedding techniques for trees, and ﬁnally prove Theorem 1.2.

# 2 Notation and preliminaries

## 2.1 General notation

The set {1,2,... ,n} of the ﬁrst n positive integers is denoted by [n]. We frequently employ indexing by many indices. We write superscript indices in parentheses (such as a(3)), as opposed to notation of powers (such as a3). We use sometimes subscripts to refer to parameters appearing in a fact/lemma/theorem. For example αT1.2 refers to the parameter α from Theorem 1.2. We omit rounding symbols when this does not aﬀect the correctness of the arguments.

- 2.2 Regular pairs Table 2.1: Speciﬁc notation used in the series.


![image 6](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile6.png>)

![image 7](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile7.png>)

![image 8](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile8.png>)

lower case Greek letters small positive constants (≪ 1)

![image 9](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile9.png>)

φ reserved for embedding; φ : V (T) → V (G) upper case Greek letters large positive constants (≫ 1)

![image 10](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile10.png>)

![image 11](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile11.png>)

![image 12](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile12.png>)

![image 13](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile13.png>)

one-letter bold sets of clusters bold (e.g., trees(k),LKS(n,k,η)) classes of graphs blackboard bold (e.g., H,E,Sη,k(G),XA) distinguished vertex sets except for

![image 14](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile14.png>)

![image 15](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile15.png>)

![image 16](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile16.png>)

![image 17](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile17.png>)

![image 18](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile18.png>)

N which denotes the set {1,2,...} script (e.g., A,D,N) families (of vertex sets, “dense spots”, and regular pairs)

![image 19](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile19.png>)

![image 20](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile20.png>)

![image 21](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile21.png>)

![image 22](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile22.png>)

∇(=nabla) sparse decomposition (see Deﬁnition 3.5)

![image 23](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile23.png>)

Table 2.1 shows the system of notation we use in the series. We write V (G) and E(G) for the vertex set and edge set of a graph G, respectively. Further, v(G) = |V (G)| is the order of G, and e(G) = |E(G)| is its number of edges. If X,Y ⊆ V (G) are two, not necessarily disjoint, sets of vertices we write e(X) for the number of edges induced by X, and e(X,Y ) for the number of ordered pairs (x,y) ∈ X × Y such that xy ∈ E(G). In particular, note that 2e(X) = e(X,X).

For a graph G, a vertex v ∈ V (G) and a set U ⊆ V (G), we write deg(v) and deg(v,U) for the degree of v, and for the number of neighbours of v in U, respectively. We write mindeg(G) for the minimum degree of G, mindeg(U) := min{deg(u) : u ∈ U}, and mindeg(V1,V2) = min{deg(u,V2) :

- u ∈ V1} for two sets V1,V2 ⊆ V (G). Similar notation is used for the maximum degree, denoted by


maxdeg(G). The neighbourhood of a vertex v is denoted by N(v). We set N(U) := u∈U N(u). The symbol − is used for two graph operations: if U ⊆ V (G) is a vertex set then G − U is the

subgraph of G induced by the set V (G) \ U. If H ⊆ G is a subgraph of G then the graph G − H is deﬁned on the vertex set V (G) and corresponds to deletion of edges of H from G. Any graph with zero edges is called empty. A family A of pairwise disjoint subsets of V (G) is an ℓ-ensemble in G if |A| ℓ for each A ∈ A.

Finally, trees(k) denotes the class of all trees of order k.

## 2.2 Regular pairs

Given a graph H and a pair (U,W) of disjoint sets U,W ⊆ V (H) the density of the pair (U,W) is deﬁned as

e(U,W) |U||W|

.

d(U,W) :=

![image 24](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile24.png>)

For a given ε > 0, a pair (U,W) of disjoint sets U,W ⊆ V (H) is called an ε-regular pair if |d(U,W) − d(U′,W′)| < ε for every U′ ⊆ U, W′ ⊆ W with |U′| ε|U|, |W′| ε|W|. If the pair (U,W) is not ε-regular, then we call it ε-irregular.

We shall need a useful and well-known property of regular pairs.

Fact 2.1. Suppose that (U,W) is an ε-regular pair of density d. Let U′ ⊆ W,W′ ⊆ W be sets of vertices with |U′| α|U|, |W′| α|W|, where α > ε. Then the pair (U′,W′) is a 2ε/α-regular pair of density at least d − ε.

The regularity lemma [Sze78] has proved to be a powerful tool for attacking graph embedding problems; see [KO09] for a survey.

- 2.3 LKS graphs


![image 25](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile25.png>)

Lemma 2.2 (Regularity lemma). For all ε > 0 and ℓ ∈ N there exist n0,M ∈ N such that for every n n0 the following holds. Let G be an n-vertex graph whose vertex set is pre-partitioned into sets V1,... ,Vℓ′, ℓ′ ℓ. Then there exists a partition U0,U1,... ,Up of V (G), ℓ < p < M, with the following properties.

- (1) For every i,j ∈ [p] we have |Ui| = |Uj|, and |U0| < εn.
- (2) For every i ∈ [p] and every j ∈ [ℓ′] either Ui ∩ Vj = ∅ or Ui ⊆ Vj.
- (3) All but at most εp2 pairs (Ui,Uj), i,j ∈ [p], i = j, are ε-regular.


We shall use Lemma 2.2 for auxiliary purposes only as it is helpful only in the setting of dense graphs (i.e., graphs which have ℓ vertices and Ω(ℓ2) edges).

- 2.3 LKS graphs It will be convenient to restrict our attention to a class of graphs which is in a way minimal


for Theorem 1.2. Write LKS(n,k,α) for the class of all n-vertex graphs with at least (12 + α)n vertices of degrees at least (1 + α)k. With this notation Conjecture 1.1 states that every graph in

![image 26](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile26.png>)

LKS(n,k,0) contains every tree from trees(k + 1).

Given a graph G, denote by Sη,k(G) the set of those vertices of G that have degree less than (1 + η)k and by Lη,k(G) the set of those vertices of G that have degree at least (1 + η)k. When proving Theorem 1.2, we may of course restrict our attention to LKS-minimal graphs, that is, to graphs that are edge-minimal with respect to belonging to LKS(n,k,α). It is easy to show that in each such graph the set Sη,k(G) is independent, all the neighbours of every vertex v ∈ V (G) with deg(v) > ⌈(1 + η)k⌉ have degree exactly ⌈(1 + η)k⌉, and |Lη,k(G)| ⌈(1/2 + η)n⌉ + 1. It turns out that our main decomposition result [HKP+a, Lemma 3.14] outputs a graph with slightly weaker properties than being LKS-minimal. Let us therefore introduce the following class of graphs.

- Deﬁnition 2.3. Suppose that n,k ∈ N, and η > 0. Let LKSsmall(n,k,η) be the class of those graphs G ∈ LKS(n,k,η) for which we have the following three properties:


- (i) All the neighbours of every vertex v ∈ V (G) with deg(v) > ⌈(1 + 2η)k⌉ have degrees at most ⌈(1 + 2η)k⌉.
- (ii) All the neighbours of every vertex of Sη,k(G) have degree exactly ⌈(1 + η)k⌉.
- (iii) We have e(G) kn.


# 3 Decomposing sparse graphs

In [HKP+a] we introduced the notion of sparse decomposition, and proved that every graph can be (almost perfectly) decomposed. We deﬁne the sparse decomposition after introducing its basic building blocks: dense spots and avoiding sets. For motivation and more details we refer the reader to [HKP+a, Section 3.2], of which this section is a condensed version.

We start by deﬁning dense spots. These are bipartite graphs having positive density, and will (among other things) serve as a basis for regularization.

- Deﬁnition 3.1 ((m,γ)-dense spot, (m,γ)-nowhere-dense). Suppose that m ∈ N and γ > 0. An (m,γ)-dense spot in a graph G is a non-empty bipartite subgraph D = (U,W;F) of G with d(D) > γ and mindeg(D) > m. We call a graph G (m,γ)-nowhere-dense if it does not contain any (m,γ)-dense spot.


When the parameters m and γ are irrelevant, we refer to D simply as a dense spot. Note that dense spots do not have any speciﬁed orientation. That is, we view (U,W;F) and

(W,U;F) as the same object.

- Deﬁnition 3.2 ((m,γ)-dense cover). Suppose that m ∈ N and γ > 0. An (m,γ)-dense cover of a given graph G is a family D of edge-disjoint (m,γ)-dense spots such that E(G) = D∈D E(D).

We now deﬁne the avoiding set. Informally, a set E of vertices is avoiding if for each set U of size up to Λk (where Λ ≫ 1 is a large constant) and each vertex v ∈ E there is a dense spot containing v and almost disjoint from U. Favourable properties of avoiding sets for embedding trees are shown in [HKP+a, Section 3.5].

- Deﬁnition 3.3 ((Λ,ε,γ,k)-avoiding set). Suppose that k ∈ N, ε,γ > 0 and Λ > 0. Suppose

that G is a graph and D is a family of dense spots in G. A set E ⊆ D∈D V (D) is (Λ,ε,γ,k)avoiding with respect to D if for every U ⊆ V (G) with |U| Λk the following holds for all but at

most εk vertices v ∈ E. There is a dense spot D ∈ D with |U ∩ V (D)| γ2k that contains v.

We can now introduce an auxiliary notion of bounded decomposition on which we can build the key concept of sparse decomposition (see below). The main result in [HKP+a] tells us that every graph has an almost perfect sparse decomposition. This sparse decomposition (and the bounded decomposition included in it) will provide us with control on the behaviour of the diﬀerent edge and vertex sets involved, and thus be helpful to embed the tree.

- Deﬁnition 3.4 ((k,Λ,γ,ε,ν,ρ)-bounded decomposition). Suppose that k ∈ N and ε,γ,ν,ρ > 0 and Λ > 0. Let V = {V1,V2,... ,Vs} be a partition of the vertex set of a graph G. We say that (V,D,Greg,Gexp,E) is a (k,Λ,γ,ε,ν,ρ)-bounded decomposition of G with respect to V if the following properties are satisﬁed:


- 1. Gexp is a (γk,γ)-nowhere-dense subgraph of G with mindeg(Gexp) > ρk.
- 2. V is a family of disjoint subsets of V (G).
- 3. Greg is a subgraph of G − Gexp on the vertex set V. For each edge xy ∈ E(Greg) there are distinct Cx ∋ x and Cy ∋ y from V, and G[Cx,Cy] = Greg[Cx,Cy]. Furthermore, G[Cx,Cy] forms an ε-regular pair of density at least γ2.
- 4. We have νk |C| = |C′| εk for all C,C′ ∈ V.
- 5. D is a family of edge-disjoint (γk,γ)-dense spots in G − Gexp. For each D = (U,W;F) ∈ D all the edges of G[U,W] are covered by D (but not necessarily by D).
- 6. If Greg contains at least one edge between C1,C2 ∈ V then there exists a dense spot D = (U,W;F) ∈ D such that C1 ⊆ U and C2 ⊆ W.
- 7. For all C ∈ V there is a set V ∈ V so that either C ⊆ V ∩V (Gexp) or C ⊆ V \ V (Gexp). For all C ∈ V and D = (U,W;F) ∈ D we have C ∩ U,C ∩ W ∈ {∅,C}.


- 8. E is a (Λ,ε,γ,k)-avoiding subset of V (G) \ V with respect to the family of dense spots D.


We say that the bounded decomposition (V,D,Greg,Gexp,E) respects the avoiding threshold b if for each C ∈ V we either have maxdegG(C,E) b, or mindegG(C,E) > b.

The members of V are called clusters. Deﬁne the cluster graph Greg as the graph on the vertex set V that has an edge C1C2 for each pair (C1,C2) which has density at least γ2 in the graph Greg. Further, we deﬁne the graph GD as the union (both edge-wise, and vertex-wise) of all dense spots D.

We now enhance the structure of bounded decomposition by adding one new feature: vertices of very large degree.

- Deﬁnition 3.5 ((k,Ω∗∗,Ω∗,Λ,γ,ε,ν,ρ)-sparse decomposition). Suppose that k ∈ N and ε,γ,ν,ρ > 0 and Λ,Ω∗,Ω∗∗ > 2. Let V = {V1,V2,... ,Vs} be a partition of the vertex set of a graph G. We say that ∇ = (H,V,D,Greg,Gexp,E) is a (k,Ω∗∗,Ω∗,Λ,γ,ε,ν,ρ)-sparse decomposition of G with respect to V1,V2,... ,Vs if the following hold.

- 1. H ⊆ V (G), mindegG(H) Ω∗∗k, maxdegH(V (G) \ H) Ω∗k, where H is spanned by the edges of D, Gexp, and edges incident with H,
- 2. (V,D,Greg,Gexp,E) is a (k,Λ,γ,ε,ν,ρ)-bounded decomposition of G − H with respect to V1 \ H,V2 \ H,... ,Vs \ H.


If the parameters do not matter, we call ∇ simply a sparse decomposition, and similarly we speak about a bounded decomposition.

- Deﬁnition 3.6 (captured edges). In the situation of Deﬁnition 3.5, we refer to the edges in E(Greg) ∪ E(Gexp) ∪ EG(H,V (G)) ∪ EG(E,E ∪ V) as captured by the sparse decomposition. We write G∇ for the subgraph of G on the vertex set V (G) which consists of the captured edges. Likewise, the captured edges of a bounded decomposition (V,D,Greg,Gexp,E) of a graph G are those in E(Greg) ∪ E(Gexp) ∪ EGD(E,E ∪ V).

It will be useful to have the following shorthand notation at hand.

- Deﬁnition 3.7 (G(n,k,Ω,ρ,ν,τ) and G¯(n,k,Ω,ρ,ν)). Suppose that k,n ∈ N and ν,ρ,τ > 0 and Ω > 0. We deﬁne G(n,k,Ω,ρ,ν,τ) to be the class of all quadruple (G,D,H,A) with the following properties:


- (i) G is a graph of order n with maxdeg(G) Ωk,
- (ii) H is a bipartite subgraph of G with colour classes AH and BH and with e(H) τkn,
- (iii) D is a (ρk,ρ)-dense cover of G,
- (iv) A is a (νk)-ensemble in G, and AH ⊆ A,
- (v) A ∩ U,A ∩ W ∈ {∅,A} for each A ∈ A and for each D = (U,W;F) ∈ D.


Those G, D and A satisfying all conditions but (ii) and the last part of (iv) will make up the triples (G,D,A) of the class G¯(n,k,Ω,ρ,ν).

# 4 Augmenting a matching

In previous papers [AKS95, Zha11, PS12, Coo09, HP15] concerning the LKS Conjecture in the dense setting the crucial turn was to ﬁnd a matching in the cluster graph of the host graph possessing certain properties. We will prove a similar “structural result” in Section 5. In the present section, we prove the main tool for Section 5, namely Lemma 4.8. All statements preceding Lemma 4.8 are only preparatory. The only exception is (the easy) Lemma 4.4 which is recycled later, in [HKP+c].

- 4.1 Regularized matchings We prove our ﬁrst auxiliary lemma on our way towards Lemma 4.8.


Lemma 4.1. For every Ω ∈ N and ε,ρ,τ > 0 there is a number α > 0 such that for every ν ∈ (0,1) there exists a number k0 ∈ N such that for each k > k0 the following holds.

For every (G,D,H,A) ∈ G(n,k,Ω,ρ,ν,τ) there are (U,W;F) ∈ D, A ∈ A and X,Y ⊆ V (G) such that

- (1) |X| = |Y | ανk,
- (2) X ⊆ A ∩ U ∩ AH and Y ⊆ W ∩ BH, where AH and BH are the colour classes of H, and
- (3) (X,Y ) is an ε-regular pair in G of density d(X,Y ) 4Ω τρ .


![image 30](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile30.png>)

Proof. Let Ω, ε, ρ and τ be given. Applying Lemma 2.2 to εL2.2 := min{ε, 8Ωρ2 } and ℓL2.2 := 2, we obtain numbers n0 and M. We set

![image 31](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile31.png>)

τρ Ω2M

α :=

, (4.1) and given ν ∈ (0,1), we set

![image 32](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile32.png>)

2n0 ανM

. Now suppose we are given k > k0 and (G,D,H,A) ∈ G(n,k,Ω,ρ,ν,τ).

k0 :=

![image 33](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile33.png>)

Property (i) of Deﬁnition 3.7 gives that e(G) Ωkn/2, and Property (ii) says that e(H) τkn. So e(H)/e(G) 2τ/Ω. Averaging over all dense spots D in the dense cover of G we ﬁnd a dense spot D = (U,W;F) ∈ D such that

2τ|F| Ω

e(H) e(G)

|F|

eD(AH,BH) = |F ∩ E(H)|

. (4.2) Without loss of generality, we assume that

![image 34](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile34.png>)

![image 35](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile35.png>)

- 1

![image 36](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile36.png>)

- 2


· eD(AH,BH) eD(U ∩ BH,W ∩ AH) , (4.3) as otherwise one can just interchange the roles of U and W. Then, eG(U ∩ AH,W ∩ BH)

eD(U ∩ AH,W ∩ BH)

(4.2) τ Ω

(4.3) 1 2

· eD(AH,BH)

· |F|. (4.4)

![image 37](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile37.png>)

![image 38](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile38.png>)

Let A′ ⊆ A denote the family of those A ∈ A with 0 < eG(A ∩U ∩ AH,W ∩BH) < Ωτ · |F| · ||UA||. Note that for each A ∈ A′ we have A ⊆ U by Deﬁnition 3.7 (v). Therefore,

![image 39](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile39.png>)

![image 40](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile40.png>)

eG A′ ∩ U ∩ AH,W ∩ BH <

|A′| |U|

τ Ω

· |F| ·

![image 41](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile41.png>)

![image 42](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile42.png>)

(4.4)

τ Ω

· |F|

![image 43](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile43.png>)

eG(U ∩ AH,W ∩ BH) .

As A covers AH, G has an edge xy with x ∈ U ∩AH ∩A for some A ∈ A \A′ and y ∈ W ∩ BH. Set X′ := A ∩ U ∩ AH = A ∩ AH and Y ′ := W ∩ BH. Then directly from the deﬁnition of A′ and since D is a (ρk,ρ)-dense spot, we obtain that

eG(X′,Y ′) |X′||Y ′|

dG(X′,Y ′) =

![image 45](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile45.png>)

τ Ω · |F| · ||UA||

![image 46](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile46.png>)

![image 47](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile47.png>)

>

![image 48](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile48.png>)

|A||W|

τρ Ω

. (4.5)

![image 49](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile49.png>)

Also, since (U,W;F) ∈ D, we have

|F| ρk|U| . (4.6) This enables us to bound the size of X′ as follows.

|X′|

eG(X′,Y ′) maxdeg(G)

![image 50](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile50.png>)

(as A  ∈ A′ and by D3.7(i))

(by (4.6))

τ Ω · ||UF|| · |A|

![image 51](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile51.png>)

![image 52](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile52.png>)

![image 53](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile53.png>)

Ωk

τ · ρk · |A| Ω2k τρνk Ω2

![image 54](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile54.png>)

![image 55](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile55.png>)

(4.1)= ανkM .

(4.7)

Similarly,

|Y ′| ανkM . (4.8)

Applying Lemma 2.2 to G[X′,Y ′] with prepartition {X′,Y ′} we obtain a collection of sets C = {Ci}pi=0, with p < M. By (4.7), and (4.8), we have that |Ci| ανk for every i ∈ [p]. It is easy to deduce from (4.5) that there is at least one εL2.2-regular (and thus ε-regular) pair (X,Y ), X,Y ∈ C \ {C0}, X ⊆ X′, Y ⊆ Y ′ with d(X,Y ) 4Ω τρ . Indeed, it suﬃces to count the number of edges incident with C0, lying in εL2.2-irregular pairs or belonging to too sparse pairs. The number of these “bad” edges is strictly smaller than

![image 56](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile56.png>)

ρ2 4Ω

)|X′||Y ′|

(εL2.2 + εL2.2 +

![image 57](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile57.png>)

ρ2 2Ω

(4.5)

|X′||Y ′|

e(X′,Y ′).

![image 58](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile58.png>)

Thus not all edges between X′ and Y ′ are bad in the sense above. This ﬁnishes the proof of Lemma 4.1.

![image 59](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile59.png>)

![image 60](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile60.png>)

![image 61](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile61.png>)

![image 62](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile62.png>)

Instead of just one pair (X,Y ), as it is given by Lemma 4.1, we shall later need several disjoint pairs for embedding larger trees. For this purpose we introduce the following deﬁnition, generalizing the notion of a matching in the cluster graph in the traditional regularity setting.

Deﬁnition 4.2 ((ε,d,ℓ)-regularized matching). Suppose that ℓ ∈ N and d,ε > 0. A collection N of ordered pairs (A,B) with A,B ⊆ V (H) is called an (ε,d,ℓ)-regularized matching of a graph H if

- (i) |A| = |B| ℓ for each (A,B) ∈ N,
- (ii) (A,B) induces in H an ε-regular pair of density at least d, for each (A,B) ∈ N, and
- (iii) all involved sets A and B are pairwise disjoint.


Sometimes, when the parameters do not matter (as for instance in Deﬁnition 4.5 below) we simply call it a regularized matching.

For a regularized matching N, we shall write V1(N) := {A : (A,B) ∈ N}, V2(N) := {B : (A,B) ∈ N} and V(N) := V1(N) ∪ V2(N). Furthermore, we set V1(N) := V1(N), V2(N) :=

V2(N) and V (N) := V1(N) ∪ V2(N) = V(N). As these deﬁnitions suggest, the orientations of the pairs (A,B) ∈ N are important. The sets A and B are called N-vertices and the pair (A,B) is an N-edge.

We say that a regularized matching N absorbs a regularized matching M if for every (S,T) ∈ M there exists (X,Y ) ∈ N such that S ⊆ X and T ⊆ Y . In the same way, we say that a family of dense spots D absorbs a regularized matching M if for every (S,T) ∈ M there exists (U,W;F) ∈ D such that S ⊆ U and T ⊆ W.

We later need the following easy bound on the size of the elements of V(M). Fact 4.3. Suppose that M is an (ε,d,ℓ)-regularized matching in a graph H. Then |C| maxdeg(d H) for each C ∈ V(M). Proof. Let for example (C,D) ∈ M. The maximum degree of H is at least as large as the average degree of the vertices in D, which is at least d|C|.

![image 64](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile64.png>)

![image 65](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile65.png>)

![image 66](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile66.png>)

![image 67](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile67.png>)

![image 68](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile68.png>)

The second step towards Lemma 4.8 is Lemma 4.4. Whereas Lemma 4.1 gives one dense regular pair, in the same setting Lemma 4.4 provides us with a dense regularized matching. Lemma 4.4. For every Ω ∈ N and ρ,ε,τ ∈ (0,1) there exists α > 0 such that for every ν ∈ (0,1) there is a number k0 ∈ N such that the following holds for every k > k0.

For each (G,D,H,A) ∈ G(n,k,Ω,ρ,ν,τ) there exists an (ε, 8Ωτρ ,ανk)-regularized matching M of G such that

![image 69](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile69.png>)

- (P1) for each (X,Y ) ∈ M there are A ∈ A, and D = (U,W;F) ∈ D such that X ⊆ U ∩ A ∩ AH and Y ⊆ W ∩ BH, and
- (P2) |V (M)| 2Ω τ n.


![image 70](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile70.png>)

Proof. Let α := αL4.1 > 0 be given by Lemma 4.1 for the input parameters ΩL4.1 := Ω, εL4.1 := ε, τL4.1 := τ/2 and ρL4.1 := ρ. For νL4.1 := ν, Lemma 4.1 yields a number k0 ∈ N.

Now let (G,D,H,A) ∈ G(n,k,Ω,ρ,ν,τ). Let M be an inclusion-maximal (ε, 8Ωτρ,ανk)-regularized matching with property (P1). We claim that

![image 71](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile71.png>)

eG(AH \ V1(M),BH \ V2(M)) <

τ 2

kn. (4.9)

![image 72](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile72.png>)

Indeed, suppose the contrary. Then the bipartite subgraph H′ of G induced by the sets AH \ V1(M) = AH \ V (M) and BH \ V2(M) = BH \ V (M) satisﬁes Property (ii) of Deﬁnition 3.7, with τD3.7 := τ/2. So, we have that (G,D,H′,A) ∈ G(n,k,Ω,ρ,ν,τ/2).

Thus Lemma 4.1 for (G,D,H′,A) yields a dense spot D = (U,W;F) ∈ D and a set A ∈ A, together with two sets X ⊆ U ∩ A ∩ (AH \ V (M)), Y ⊆ W ∩ (BH \ V (M)) such that |X| = |Y | > αL4.1νk = ανk, and such that (X,Y ) is εL4.1-regular and has density at least

τρ 8Ω

τL4.1ρL4.1 4ΩL4.1

=

.

![image 74](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile74.png>)

![image 75](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile75.png>)

This contradicts the maximality of M, proving (4.9).

In order to see (P2), it suﬃces to observe that by (4.9) and by Property (ii) of Deﬁnition 3.7, the set V (M) is incident with at least τkn − τ2kn = τ2kn edges. By Deﬁnition 3.7 (i), it follows that |V (M)| τ2kn · Ω1k 2Ω τ n, as desired.

![image 76](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile76.png>)

![image 77](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile77.png>)

![image 78](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile78.png>)

![image 79](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile79.png>)

![image 80](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile80.png>)

![image 81](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile81.png>)

![image 82](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile82.png>)

![image 83](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile83.png>)

![image 84](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile84.png>)

## 4.2 Augmenting paths for matchings

We now prove the main lemma of Section 4, namely Lemma 4.8. We will use an augmenting path technique for our regularized matchings, similar to the augmenting paths commonly used for traditional matching theorems. For this, we need the following deﬁnitions.

Deﬁnition 4.5 (Alternating path, augmenting path). Suppose that n,s ∈ N and δ > 0. Given an n-vertex graph G, and a regularized matching M, we call a sequence S = (Y0,A1,Y1,A2,Y2,... ,Ah,Yh) (where h 0 is arbitrary) a (δ,s)-alternating path for M from Y0 if for all i ∈ [h] we have

- (i) Ai ⊆ V1(M) and the sets Ai are pairwise disjoint,
- (ii) Y0 ⊆ V (G) \ V (M) and Yi = (A,B)∈M,A∈A

i

B,

- (iii) |Yi−1| δn, and
- (iv) e(A,Yi−1) s · |A|, for each A ∈ Ai.

If in addition there is a set C of disjoint subsets of V (G) \ (Y0 ∪ V (M)) such that

- (v) e( C,Yh) t · n,


then we say that S′ = (Y0,A1,Y1,A2,Y2,... ,Ah,Yh,C) is a (δ,s,t)-augmenting path for M from Y0 to C.

The number h is called the length of S (or of S′). Next, we show that a regularized matching either has an augmenting path or admits a partition

into two parts so that only few edges cross these parts in a certain way.

Lemma 4.6. Given an n-vertex graph G with maxdeg(G) Ωk, a number τ ∈ (0,1), a regularized matching M, a set Y0 ⊆ V (G) \ V (M), and a set C of disjoint subsets of V (G) \ (V (M) ∪Y0), one of the following holds:

(M1) There is a regularized matching M′′ ⊆ M with

e C ∪ V1(M \ M′′),Y0 ∪ V2(M′′) < τnk,

(M2) M has a (2Ωτ , 8Ωτ2 k, 16Ωτ2 k)-augmenting path of length at most 2Ω/τ from Y0 to C.

![image 85](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile85.png>)

![image 86](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile86.png>)

![image 87](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile87.png>)

Proof. If |Y0| 2Ω τ n then (M1) is satisﬁed for M′′ := ∅. Let us therefore assume the contrary.

![image 89](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile89.png>)

Choose a (2Ωτ , 8Ωτ2 k)-alternating path S = (Y0,A1,Y1,A2, Y2,... ,Ah,Yh) for M with | hℓ=1 Aℓ| maximal.

![image 90](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile90.png>)

![image 91](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile91.png>)

Now, let ℓ∗ ∈ {0,1,... ,h} be maximal with |Yℓ∗| 2Ω τ n. Then ℓ∗ ∈ {h,h − 1}. Moreover, as |Yℓ| 2Ω τ n for all ℓ ℓ∗, we have that (ℓ∗ + 1) · 2Ωτ n | ℓ ℓ∗ Yℓ| n and thus

![image 92](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile92.png>)

![image 93](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile93.png>)

![image 94](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile94.png>)

ℓ∗ + 1

2Ω τ

. (4.10)

![image 95](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile95.png>)

Let M′′ ⊆ M consist of all M-edges (A,B) ∈ M with A ∈ ℓ∈[h] Aℓ. Then, by the choice of S,

ℓ∗

e V1(M \ M′′),

ℓ=0

ℓ∗

e V1(M \ M′′),Yℓ

Yℓ =

ℓ=0

τ2 8Ω

< (ℓ∗ + 1) ·

k · |V1(M \ M′′)|

![image 96](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile96.png>)

(4.10) τ 4

kn. (4.11)

![image 97](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile97.png>)

Furthermore, if ℓ∗ = h − 1 (that is, if |Yh| < 2Ωτ n) then e V1(M \ M′′) ∪ C,Yh <

![image 98](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile98.png>)

τ 2Ω

n · maxdeg(G)

![image 99](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile99.png>)

τ 2Ω

Ωkn =

![image 100](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile100.png>)

τ 2

kn. (4.12)

![image 101](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile101.png>)

So, regardless of whether h = ℓ∗ or h = ℓ∗ + 1, we get from (4.11) and (4.12) that

e V1(M \ M′′) ∪ C,Y0 ∪ V2(M′′) <

ℓ∗

- 3

![image 102](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile102.png>)

- 4


τkn + e C,

Yℓ .

ℓ=0

Thus, if e( C, ℓℓ∗=0 Yℓ) τ4kn, we see that (M1) is satisﬁed for M′′. So, assume the contrary. Then, by (4.10), there is an index j ∈ {0,1,... ,ℓ∗} for which

![image 103](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile103.png>)

e C,Yj >

τ2 16Ω

kn,

![image 104](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile104.png>)

and thus, (Y0,A1,Y1,A2, Y2,... ,Aj,Yj,C) is a (2Ωτ , 8Ωτ2 k, 16Ωτ2 k)-augmenting path for M. This proves (M2).

![image 105](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile105.png>)

![image 106](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile106.png>)

![image 107](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile107.png>)

![image 108](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile108.png>)

![image 109](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile109.png>)

![image 110](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile110.png>)

![image 111](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile111.png>)

The aim of this section is to ﬁnd a regularized matching covering as many vertices from the graph as possible. This is done by iteratively improving a matching. Below, Lemma 4.7 provides with such an iterative step: given a regularized matching M we either ﬁnd (II) a better regularized matching M′, or there is (I) a natural barrier to ﬁnding such a matching. This barrier is a separation of the previous regularized matching into two blocks (M′′ and M \ M′′) such that very few edges “cross” this separation. The absence of such a separation guarantees the existence of an augmenting path for M, which can be used to ﬁnd a better regularized matching. This matching M′ has (C1) to improve M substantially and (C2) respect the structure of the graph and of M.

- Lemma 4.7. For every Ω ∈ N and τ ∈ (0, 2Ω1 ) there is a number τ′ ∈ (0,τ) such that for every ρ ∈ (0,1) there is a number α ∈ (0,τ′/2) such that for every ε ∈ (0,α) there is a number π > 0


![image 112](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile112.png>)

such that for every γ > 0 there is k0 ∈ N such that the following holds for every k > k0 and every h ∈ (γk,k/2).

Let G be a graph of order n with maxdeg(G) Ωk, with an (ε3,ρ,h)-regularized matching M and with a (ρk,ρ)-dense cover D that absorbs M. Let Y ⊆ V (G) \ V (M), and let C be an hensemble in G with C ∩(V (M)∪Y ) = ∅. Assume that U ∩C ∈ {∅,C} for each D = (U,W;F) ∈ D and each C ∈ C ∪ V1(M).

Then one of the following holds.

- (I) There is a regularized matching M′′ ⊆ M such that

e C ∪ V1(M \ M′′),Y ∪ V2(M′′) < τnk.

- (II) There is an (ε,α,πh)-regularized matching M′ such that


(C1) |V (M) \ V (M′)| εn, and |V (M′)| |V (M)| + τ2′n, and (C2) for each (T,Q) ∈ M′ there are sets C1 ∈ V1(M) ∪ C, C2 ∈ V2(M) ∪ {Y } and a dense

![image 114](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile114.png>)

spot D = (U,W;F) ∈ D such that T ⊆ C1 ∩ U and Q ⊆ C2 ∩ W. Proof. We divide the proof into ﬁve steps.

- Step 1: Setting up the parameters. Suppose that Ω and τ are given. For ℓ = 0,1,... ,⌈2Ω/τ⌉, we deﬁne the auxiliary parameters


⌈2Ωτ ⌉−ℓ+2

τ2 32Ω

![image 115](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile115.png>)

τ(ℓ) :=

, (4.13) and set

![image 116](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile116.png>)

τ(0) 2Ω

τ′ :=

. Given ρ, we deﬁne

![image 117](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile117.png>)

τ′ρ 16Ω

α :=

. Then, given ε, for ℓ = 0,1,... ,⌈2Ω/τ⌉, we deﬁne the further auxiliary parameters µ(ℓ) := αL4.4 Ω,ρ,ε3,τ(ℓ)

![image 118](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile118.png>)

which are given by Lemma 4.4 for input parameters ΩL4.4 := Ω, ρL4.4 := ρ, εL4.4 := ε3, and τL4.4 := τ(ℓ). Set

ε 2

· min µ(ℓ) : ℓ = 0,... ,⌈2Ω/τ⌉ .

π :=

![image 119](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile119.png>)

Given the next1 input parameter γ, Lemma 4.4 for parameters as above and the ﬁnal input νL4.4 := γ yields k0L4.4 =: k0(ℓ), set

k0 := max k0(ℓ) : ℓ = 0,... ,⌈2Ω/τ⌉ .

![image 120](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile120.png>)

1in the order of quantiﬁcation from the statement of the lemma

- Step 2: Finding an augmenting path. We apply Lemma 4.6 to G, τ, M, Y and C. Since (M1) corresponds to (I), let us assume that the outcome of the lemma is (M2). Then there is a (2Ωτ , 8Ωτ2 k, 16Ωτ2 k)-augmenting path S′ = (Y0,A1,Y1,A2, Y2,... , Aj∗,Yj∗,C) for M starting from Y0 := Y such that j∗ 2Ω/τ.

![image 122](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile122.png>)

![image 123](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile123.png>)

![image 124](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile124.png>)

Our aim is now to show that (II) holds.

- Step 3: Creating parallel matchings. Inductively, for ℓ = j∗,j∗ − 1,... ,0 we shall deﬁne auxiliary bipartite induced subgraphs H(ℓ) ⊆ G with colour classes P(ℓ) and Yℓ that satisfy


- (a) e(H(ℓ)) τ(ℓ)kn, and (ε3,2α,µ(ℓ)h)-regularized matchings M(ℓ) that satisfy
- (b) V1(M(ℓ)) ⊆ P(ℓ),
- (c) for each (A′,B′) ∈ M(ℓ) there are a dense spot (U,W;F) ∈ D and a set A ∈ V1(M) (or a set A ∈ C if ℓ = j∗) such that A′ ⊆ U ∩ A and B′ ⊆ W ∩ Yℓ,
- (d) |V (M(ℓ))| τ2Ω(ℓ)n, and

![image 125](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile125.png>)

- (e) |B ∩ V2(M(ℓ))| = |A ∩ P(ℓ−1)| for each edge (A,B) ∈ M, if ℓ > 0. We take H(j∗) as the induced bipartite subgraph of G with colour classes P(j∗) := C and Yj∗.


- Deﬁnition 4.5 (v) together with (4.13) ensures (a) for ℓ = j∗. Now, for ℓ j∗, suppose H(ℓ) is already deﬁned. Further, if ℓ < j∗ suppose also that M(ℓ+1) is already deﬁned. We shall deﬁne


- M(ℓ), and, if ℓ > 0, we shall also deﬁne H(ℓ−1). Observe that (G,D,H(ℓ),Aℓ) ∈ G(n,k,Ω,ρ, hk,τ(ℓ)), because of (a) and the assumptions of the


![image 126](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile126.png>)

lemma. So, applying Lemma 4.4 to (G,D,H(ℓ),Aℓ) and noting that τ8Ω(ℓ)ρ 2α, we obtain an (ε3,2α,µ(ℓ)h)-regularized matching M(ℓ) that satisﬁes conditions (b)–(d).

![image 127](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile127.png>)

If ℓ > 0, we deﬁne H(ℓ−1) as follows. For each (A,B) ∈ M take a set A˜ ⊆ A of cardinality |A˜| = |B ∩ V (M(ℓ))| so that

τ2 8Ω

k · |A˜| . (4.14)

e(A,Y˜ ℓ−1)

![image 128](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile128.png>)

This is possible by Deﬁnition 4.5 (iv): just choose those vertices from A for A˜ that send most edges to Yℓ−1. Let P(ℓ−1) be the union of all the sets A˜. Then, (e) is satisﬁed. Furthermore,

So, by (4.14),

|P(ℓ−1)| = |V2(M(ℓ))|

(d) τ(ℓ) 4Ω

n.

![image 129](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile129.png>)

e(P(ℓ−1),Yℓ−1)

τ2 8Ω

k · |P(ℓ−1)|

![image 130](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile130.png>)

τ2 · τ(ℓ) 32Ω2

kn (4.13)= τ(ℓ−1)kn . (4.15)

![image 131](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile131.png>)

We let H(ℓ−1) be the bipartite subgraph of G induced by the colour classes P(ℓ−1) and Yℓ−1. Then (4.15) establishes (a) for H(ℓ−1). This ﬁnishes step ℓ.2

![image 132](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile132.png>)

2Recall that the matching M(ℓ−1) is only to be deﬁned in step ℓ − 1.

- Step 4: Harmonising the matchings. Our regularized matchings M(0),... ,M(j∗) will be a good base for constructing the regularized matching M′ we are after. However, we do not know

anything about |B ∩ V2(M(ℓ))| − |A ∩ V1(M(ℓ−1))| for the M-edges (A,B) ∈ M. But this term will be crucial in determining how much of V (M) gets lost when we replace some of its M-edges with M(ℓ)-edges. For this reason, we reﬁne M(ℓ) in a way that its M(ℓ)-edges become almost equal-sized.

Formally, we shall inductively construct regularized matchings N(0),... ,N(j∗) such that for ℓ = 0,... ,j∗ we have

- (A) N(ℓ) is an (ε,α,πh)-regularized matching,
- (B) M(ℓ) absorbs N(ℓ),
- (C) if ℓ > 0 and (A,B) ∈ M with A ∈ Aℓ then |A ∩ V (N(ℓ−1))| |B ∩ V (N(ℓ))|, and
- (D) |V2(N(ℓ))| |V1(N(ℓ−1))| − 2ε · |V2(M(ℓ))| if ℓ > 0 and |V2(N(0))| τ2Ω(0)n = τ′n.


![image 134](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile134.png>)

![image 135](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile135.png>)

Set N(0) := M(0). Clearly (B) holds for ℓ = 0, (A) is easy to check, and (C) is void. Finally, Property (D) holds because of (d). Suppose now ℓ > 0 and that we already constructed matchings

- N(0),... ,N(ℓ−1) satisfying Properties (A)–(D). Observe that for any (A,B) ∈ M we have that


|B ∩ V2(M(ℓ))|

(b),(e)

|A ∩ V1(M(ℓ−1))| |A ∩ V1(N(ℓ−1))|, (4.16) where the last inequality holds because of (B) for ℓ − 1.

So, we can choose a subset X(ℓ) ⊆ V2(M(ℓ)) such that |B ∩ X(ℓ)| = |A ∩ V (N(ℓ−1))| for each (A,B) ∈ M. Now, for each (S,T) ∈ M(ℓ) write T := T ∩ X(ℓ), and choose a subset S of S of size | T|. Set

N(ℓ) := ( S, T) : (S,T) ∈ M(ℓ),| T|

ε 2

![image 136](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile136.png>)

· |T| . (4.17) Then (B) and (C) hold for ℓ.

For (A), note that Fact 2.1 implies that N(ℓ) is an ε,2α − ε3, 2εµ(ℓ)h -regularized matching. In order to verify (D), it suﬃces to observe that

![image 137](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile137.png>)

|V2(N(ℓ))| =

( S, T)∈N(ℓ)

| T| |X(ℓ)| −

(S,T)∈M(ℓ)

ε 2

![image 138](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile138.png>)

· |T|

(A,B)∈M

|A ∩ V1(N(ℓ−1))| −

ε 2

![image 139](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile139.png>)

· |V2(M(ℓ))| = |V1(N(ℓ−1))| −

ε 2

![image 140](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile140.png>)

· |V2(M(ℓ))|.

- Step 5: The ﬁnal matching. Suppose that (A,B) ∈ M with A ∈ Aℓ for some ℓ ∈ {1,2,... ,j∗}. Then, set A′ := A \ V1(N(ℓ−1)). Also, choose a set B′ ⊆ B \ V2(N(ℓ)) of cardinality |A′|. This is possible by (C). By (4.17) we deduce that


|B \ V2(N(ℓ))| − |B′|

ε 2

|B| . (4.18)

![image 141](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile141.png>)

We consider the set L ⊆ M consisting of all M-edges (A,B) ∈ M with |A′| > 2ε · |A|.

![image 142](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile142.png>)

Set

K := {(A′,B′) : (A,B) ∈ L}.

By the assumption of the lemma, for every (A′,B′) ∈ K there are an edge (A,B) ∈ M and a dense spot D = (U,W;F) ∈ D such that

A′ ⊆ A ⊆ U and B′ ⊆ B ⊆ W. (4.19)

Since M is (ε3,ρ,h)-regularized, Fact 2.1 implies that K is an (ε,ρ − ε3, 2εh)-regularized matching. Set

![image 144](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile144.png>)

j∗

M′ := K ∪

N(ℓ).

ℓ=0

It is easy to check that M′ is an (ε,α,πh)-regularized matching. Using (4.19) together with (B) and (c), we see that (C2) holds for M′.

In order to see (C1), we calculate |V (M) \ V (M′)| =

∗

∗

ℓ=0N(ℓ) ∪ K)| + |B \ V2(∪j

|A \ V1(∪j

ℓ=0N(ℓ) ∪ K)|

(A,B)∈M

ε 2

(4.18)

|A \ V1(∪jℓ=1∗ N(ℓ−1) ∪ K))| + |B \ V2(∪jℓ=1∗ N(ℓ) ∪ K)|

|A′ ∪ B′| +

|B|

+

![image 145](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile145.png>)

(A,B)∈M\L

(A,B)∈L

![image 146](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile146.png>)

![image 147](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile147.png>)

![image 148](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile148.png>)

![image 149](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile149.png>)

(sum1)

(sum2)

.

In (sum2), consider an arbitrary term corresponding to (A,B). By the deﬁnition of K, the term |A\V1(∪j

∗

∗

ℓ=1N(ℓ−1)∪K)| is zero. To treat the term |B\V2(∪j

ℓ=1N(ℓ)∪K)|, we recall that |A| = |B| and |A′| = |B′| (in the deﬁnition of K). This gives that |B \V2(∪j

∗

∗

ℓ=1N(ℓ) ∪K)| = |A∩V1(∪j

ℓ=1N(ℓ−1))|− |B ∩ V2(∪j

∗

ℓ=1N(ℓ))|. This leads to |V (M) \ V (M′)|

ε 2

|A′ ∪ B′| +

|B|

![image 150](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile150.png>)

(A,B)∈M\L

j∗

|A ∩ V1(N(ℓ−1))| − |B ∩ V2(N(ℓ))|

+

ℓ=1

(A,B)∈L

(A,B)∈M\L

ε 2

|A| + ε|B| +

![image 151](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile151.png>)

j∗

ℓ=1

|V1(N(ℓ−1))| − |V2(N(ℓ))|

(D) 3ε 4

n +

![image 152](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile152.png>)

j∗

ℓ=1

ε 2

· |V2(M(ℓ))| εn .

![image 153](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile153.png>)

Using the fact that V2(N(0)) ⊆ V (M′) \ V (M) the last calculation also implies that

τ′ 2

(D)

|V (M′)| − |V (M)| |V2(N(0))| − |V (M) \ V (M′)|

τ′n − εn >

n , since ε < α τ′/2 by assumption.

![image 154](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile154.png>)

![image 155](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile155.png>)

![image 156](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile156.png>)

![image 157](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile157.png>)

![image 158](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile158.png>)

Iterating Lemma 4.7 we prove the main result of the section.

- Lemma 4.8. For every Ω ∈ N and ρ ∈ (0,1/Ω) there exists a number β > 0 such that for every ε ∈ (0,β), there are ε′,π > 0 such that for each γ > 0 there exists a number k0 ∈ N such that the following holds for every k > k0 and c ∈ (γk,k/2).


Let G be a graph of order n, with maxdeg(G) Ωk. Let D be a (ρk,ρ)-dense cover of G, and let M be an (ε′,ρ,c)-regularized matching that is absorbed by D. Let C be a c-ensemble in G with C ∩ (V (M)) = ∅. Let Y ⊆ V (G) \ (V (M) ∪ C). Assume that for each (U,W;F) ∈ D, and for each C ∈ V1(M) ∪ C we have that

U ∩ C ∈ {∅,C} . (4.20) Then there exists an (ε,β,πc)-regularized matching M′ such that

- (i) |V (M) \ V (M′)| εn,
- (ii) for each (T,Q) ∈ M′ there are sets C1 ∈ V1(M) ∪ C, C2 ∈ V2(M) ∪ {Y } and a dense spot D = (U,W;F) ∈ D such that T ⊆ C1 ∩ U and Q ⊆ C2 ∩ W, and
- (iii) M′ can be partitioned into M1 and M2 so that e ( C ∪ V1(M)) \ V1(M1) , (Y ∪ V2(M)) \ V2(M2) < ρkn .


Proof. Let Ω and ρ be given. Let τ′ := τL4′ .7 be the output given by Lemma 4.7 for input parameters ΩL4.7 := Ω and τL4.7 := ρ/2.

Set ρ(0) := ρ, set L := ⌈2/τ′⌉ + 1, and for ℓ ∈ [L], inductively deﬁne ρ(ℓ) to be the output αL4.7 given by Lemma 4.7 for the further input parameter ρL4.7 := ρ(ℓ−1) (keeping ΩL4.7 = Ω and τL4.7 = ρ/2 ﬁxed). Then ρ(ℓ+1) ρ(ℓ) for all ℓ. Set β := ρ(L).

Given ε < β we set ε(ℓ) := (ε/2)3L−ℓ for ℓ ∈ [L] ∪ {0}, and set ε′ := ε(0). Clearly,

L

ε(ℓ) ε. (4.21)

ℓ=0

Now, for ℓ + 1 ∈ [L], let π(ℓ) := πL4.7 be given by Lemma 4.7 for input parameters ΩL4.7 := Ω, τL4.7 := ρ/2, ρL4.7 := ρ(ℓ) and εL4.7 := ε(ℓ+1). For ℓ ∈ [L] ∪ {0}, set Π(ℓ) := 2Ωρ j ℓ−=01 π(j). Let π := Π(L).

![image 160](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile160.png>)

Given γ, let k0 be the maximum of the lower bounds k0L4.7 given by Lemma 4.7 for input

- parameters ΩL4.7 := Ω, τL4.7 := ρ/2, ρL4.7 := ρ(ℓ−1), εL4.7 := ε(ℓ), γL4.7 := γΠ(ℓ), for ℓ ∈ [L].


Suppose now we are given G, D, C, Y and M. Suppose further that c > γk > γk0. Let ℓ ∈ {0,1,... ,L} be maximal subject to the condition that there is a matching M(ℓ) with the following properties:

- (a) M(ℓ) is an (ε(ℓ),ρ(ℓ),Π(ℓ)c)-regularized matching,
- (b) |V (M(ℓ))| ℓ · τ2′n,

![image 161](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile161.png>)

- (c) |V (M) \ V (M(ℓ))| ℓi=0 ε(i)n, and


- (d) for each (T,Q) ∈ M(ℓ) there are sets C1 ∈ V1(M) ∪ C, C2 ∈ V2(M) ∪ {Y } and a dense spot D = (U,W;F) ∈ D such that T ⊆ C1 ∩ U and Q ⊆ C2 ∩ W.


Observe that such a number ℓ exists, as for ℓ = 0 we may take M(0) = M. Also note that ℓ 2/τ′ < L because of (b).

We now apply Lemma 4.7 with input parameters ΩL4.7 := Ω, τL4.7 := ρ/2, ρL4.7 := ρ(ℓ), εL4.7 := ε(ℓ+1) < β ρ(ℓ+1) = αL4.7, γL4.7 := γΠ(ℓ) to the graph G with the (ρ(ℓ)k,ρ(ℓ))-dense cover D, the (ε(ℓ),ρ(ℓ),Π(ℓ)c)-regularized matching M(ℓ), the set

Y := (Y ∪ V2(M)) \ V2(M(ℓ)), and the (Π(ℓ)c)-ensemble

C := C \ V (M(ℓ)) : C ∈ V1(M) ∪ C, |C \ V1(M(ℓ))| Π(ℓ)c .

Lemma 4.7 yields a regularized matching which either corresponds to M′′L4.7 as in Assertion (I) or

to M′L4.7 as in Assertion (II). Note that in the latter case, the matching M′L4.7 actually constitutes an (ε(ℓ+1),ρ(ℓ+1),Π(ℓ+1)c)-regularized matching M(ℓ+1) fulﬁlling all the above properties for ℓ+1

L. In fact, (b) and (c) hold for M(ℓ+1) because of (C1), and it is not diﬃcult to deduce (d) from (C2) and from (d) for ℓ. But this contradicts the choice of ℓ. We conclude that we obtained a regularized matching M′′L4.7 ⊆ M(ℓ) as in Assertion (I) of Lemma 4.7.

Thus, in other words, M(ℓ) can be partitioned into M1 and M2 so that e C ∪ V1(M2) , Y ∪ V2(M1) < τL4.7kn = ρkn/2. (4.22)

Set M′ := M(ℓ). Then M′ is (ε,β,πc)-regularized by (a). Note that Assertion (i) of the lemma holds by (4.21) and by (c). Assertion (ii) holds because of (d).

Since

(Y ∪ V2(M)) \ V2(M2) ⊆ Y ∪ V2(M1), and because of (4.22) we know that in order to prove Assertion (iii) it suﬃces to show that

X := ( C ∪ V1(M)) \ V1(M1) \ C ∪ V1(M2)

= C ∪ V1(M) \ C ∪ V1(M(ℓ))

sends at most ρkn/2 edges to the rest of the graph. For this, it would be enough to see that |X| 2Ω ρ n, since by assumption, G has maximum degree Ωk.

![image 163](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile163.png>)

To this end, note that by assumption, |V1(M) ∪ C| nc . Further, the deﬁnition of C implies that for each A ∈ C ∪ V1(M) we have that |A \ C ∪ V1(M(ℓ) | Π(ℓ)c. Combining these two observations, we obtain that

![image 164](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile164.png>)

ρ 2Ω

|X| < Π(ℓ)n

n , as desired.

![image 165](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile165.png>)

![image 166](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile166.png>)

![image 167](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile167.png>)

![image 168](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile168.png>)

![image 169](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile169.png>)

![image 170](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile170.png>)

# 5 Rough structure of LKS graphs

In this section we give a structural result for graphs G ∈ LKSsmall(n,k,η), stated in Lemma 5.4. Similar structural results were essential also for proving Conjecture 1.1 in the dense setting in [AKS95, PS12]. There, a certain matching structure was proved to exist in the cluster graph of the host graph. This matching structure then allowed us to embed a given tree into the host graph. We motivate the structure asserted by Lemma 5.4 in more detail in Section 5.1.

Naturally, in our possibly sparse setting the sparse decomposition ∇ of G will enter the picture (instead of just the cluster graph of G. For more on sparse decomposition, see [HKP+a]). There is an important subtlety though: we may need to “re-regularize” the cluster graph Greg of ∇. In this case, we have to ﬁnd another regularization of parts of G, partially based on Greg. Lemma 4.8 is the main tool to this end. The re-regularization is captured by the regularized matchings MA and MB.

Let us note that this step is one of the biggest diﬀerences between our approach and the announced solution of the Erd˝os–So´s Conjecture by Ajtai, Komlo´s, Simonovits and Szemere´di. In other words, the nature of the graphs arising in the Erd˝os–So´s Conjecture allows a less careful approach with respect to regularization, still yielding a structure suitable for embedding trees. We discuss the necessity of this step in further detail in Section 5.2. The main result of this paper Lemma 5.4, is given in Section 5.3.

## 5.1 Motivation for and intuition behind Lemma 5.4

Recall that [HKP+a, Lemma 3.14] asserts that each graph G = GT1.2 satisfying the conditions of Theorem 1.2 has a sparse decomposition which captures almost all its edges. With this preprocessing at hand, we want Lemma 5.4 to provide speciﬁc structural properties of G under which we could make the embedding of the tree T = TT1.2 work. The complexity of these assertions (which span more than half a page) stems from the complicated nature of the sparse decomposition, and from the delicate features of the embedding techniques (worked out in [HKP+d, Section 6]). In this section we try to explain and motivate the key assertions of Lemma 5.4. The reader may skip the section at his or her convenience. The only bit from this section needed for the main result is

- Deﬁnition 5.3. At this stage, let us introduce informally the notion of ﬁne partition which we use to cut up


the tree T. Let τ ≪ 1. We ﬁnd a constant number of cut vertices of T so that the components (which we refer to as shrubs) in the remainder of T are of order at most τk. The cut vertices will decompose into two sets WA and WB so that the distance from any vertex of WA to any vertex in WB is odd. It can be shown that we can do the cutting so that each shrub either neighbours only one cut vertex from WA ∪ WB, or it neighbours two, in which case both these cut vertices are in WA. Thus, the set of all shrubs can be decomposed as SA∪S˙ B depending on the cut vertices that surround individual shrubs. The last property of the ﬁne partition we shall use is that

v(t)

t∈SA

v(t) . (5.1)

t∈SB

The quadruple (WA,WB,SA,SB) is then called a (τk)-ﬁne partition of T. The full deﬁnition which includes several additional properties is given in [HKP+d, Section 3].

As said earlier, Lemma 5.4 is an extensive generalization of previous structural results on the LKS Conjecture in the dense setting. So, as a starting point for our motivation, let us explain the

structural result Piguet and Stein [PS12] use to prove the dense approximate version of the LKS Conjecture.

Theorem 5.1 ([PS12]). For every η > 0 and q > 0 there exists a number n0 such that for every n > n0 and k > qn we have the following. For every graph G ∈ LKS(n,k,η) contains each tree from trees(k).

Here, of course, the structure we work with is encoded in the cluster graph (in the sense of the original regularity lemma) Greg of the graph GT5.1. Note that Greg ∈ LKS(N,K,η/2), where N is the number of clusters and K = k · Nn . The main structural result of Piguet and Stein then reads

![image 172](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile172.png>)

- as follows.


Informal Lemma 5.2 ([PS12, Lemma 8], simpliﬁed). Suppose that Greg ∈ LKS(N,K,α) and let us write L = LK,α(Greg). Then we have at least one of the following two cases.

- (H1) There exists a matching M ⊆ Greg and an edge A1A2 so that degGreg(Ai,L ∪ V (M)) K, for i = 1,2.
- (H2) There exists a matching M ⊆ Greg and an edge AB with degGreg(A,L ∪ V (M)) K, and degGreg(B,L ∪ V (M)) K2 . Further,


![image 173](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile173.png>)

for every e ∈ M, |NGreg(A) ∩ e| 1 . (5.2)

Piguet and Stein use structures (H1) and (H2) to embed any given tree T ∈ trees(k) into G using the regularity method. A comprehensive description of the embedding procedure is given in Sections 3.6 and 3.7 in [PS12]. The embedding itself is quite technical but it follows a relatively pedestrian strategy which we present next. The regularity method tells us that a regular pair can be ﬁlled up by an arbitrary family of shrubs, provided that the colour classes of these shrubs (viewed

- as one bipartite graph) do not overﬁll the end-clusters of that regular pair. The degree conditions in Informal Lemma 5.2 suggest that we will utilize the clusters of M and of L. More precisely, some of the shrubs will be accommodated in the edges of the matching M. Suppose next that we would like to proceed with embedding some shrubs using a cluster X ∈ L. This can be done as follows. Using the high-degree property of X we can ﬁnd a cluster Y adjacent to X that is not ﬁlled up completely by the image of T. We then use the pair XY to accommodate further shrubs. We


keep embedding T by mapping WA to A1 (in (H1)) or to A (in (H2)), WB to A2 or to B, and the shrubs pendent from these cut-vertices either into the regular edges of M, or to edges incident to clusters L as described above. Thus, the degree conditions in Informal Lemma 5.2 guarantee that we can accommodate shrubs of total order up to k from A1, A2, and A. The degree bound for B guarantees that we can embed shrubs of total order up to k/2 from B, recall that this is suﬃcient, thanks to (5.1). The fact that A1A2 or AB forms an edge allows us to make connections between images of WA and WB.

So far, we have not explained the role of condition (5.2). We include a relatively detailed explanation in Figure 5.1. However, this condition is independent of the rest of the argument, and it may be suﬃcient for the reader to take granted that (5.2) is crucial for the embedding to work.

We now try to give an analogue to Informal Lemma 5.2 in the sparse setting when the structure of G is encoded in the sparse decomposition rather than in the cluster graph. Recall that in the dense setting sets suitable for embedding shrubs were clusters of a regular matching (that is, M),

Figure 5.1: The reason for requiring (5.2) in the setting of (H2). Consider two edges C1D1,C2D2 ∈ M such that only C2D2 satisﬁes (5.2). At some point during the embedding of T, we may need to use the high-degree property of clusters in L. When doing so we cannot guarantee that we will ﬁll the edges of M in an eﬃcient way. That is, we may end up ﬁlling D1 and D2 completely and leaving C1 and C2 untouched. If this happens, both regular pairs C1D1 and C2D2 are useless for embedding further shrubs. The used space in C2D2 equals the degree from A to C2D2. That is, we do not expect to embed anything more in the edge C2D2. The condition degG

(A,L ∪ V (M)) K ensures that we ﬁnd free space somewhere else in the cluster graph to complete our embedding. Clearly, the pair C1D1 does not have this favourable feature: the number of vertices used by the embedding is only half the degree of A to C1D1. In this case, the condition degG

reg

(A,L ∪ V (M)) K is not strong enough. We do not need a counterpart of (5.2) for NG

reg

(B). The reason is that we can schedule our embedding process in such a way that when we use the high-degree property of L we have already exhausted the degree from B to M.

reg

and clusters of large degree (that is, L). In the sparse setting, in addition to using a suitable matching of regular pairs M and large degree vertices Lk,η(G) we can make use of two further sets for embedding shrubs: V (Gexp) (as explained in [HKP+a, Section 3.6]) and the set E (as explained in [HKP+a, Section 3.5]). Thus, the counterpart of clusters A1, A2 and A from Informal Lemma 5.2 is the set XA of vertices, which have degree at least k into the set Lk,α(G)∪V (M)∪V (Gexp)∪E.3 Likewise, the counterpart of cluster B in Informal Lemma 5.2 are vertices of XB, which have degree

- at least k/2 into Lk,α(G)∪V (M)∪V (Gexp)∪E.4 We see that a sparse counterpart to (H1) would be two disjoint well-connected sets XA1,XA2 ⊆ XA. In Lemma 5.4 we achieve this in one of two possible ways. One way is ﬁnding a large regularized matching Mgood inside XA; one can then take XA1 = V1(Mgood) and XA2 = V2(Mgood). This corresponds to (K2) in Lemma 5.4(h). Next, suppose that XA induces suﬃciently many edges. Then we take XA1 and XA2 to be a bipartition of XA corresponding to a maximum cut. Hence, the sets XA1 and XA2 are again well-connected. This corresponds to the case e(XA) ηkn/12 in (K1) in Lemma 5.4(h). Similarly, if the sets XA and XB are well-connected, we are on a good track to getting a sparse version of (H2).


It remains to translate condition (5.2). The right counterpart to this condition is

for every XY ∈ M, NG∇(XA) ∩ X = ∅ or NG∇(XA) ∩ Y = ∅ . (5.3) The actual statement of Lemma 5.4 deviates quite substantially from the informal account given

![image 175](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile175.png>)

- 3The rather diﬀerent looking formal deﬁnition of XA is given in (5.4). Below, we give an explanation for this

diﬀerence.

- 4The formal deﬁnition of XB is given again in (5.4).


above. So, let us now state an informal version of Lemma 5.4. After that, we explain how it relates to the description above. Also, we mark the correspondence between this informal version and the actual lemma by using the same numbering. In particular, assertions (d), (f), (g) in Lemma 5.4 are needed for reasons that cannot be explained in this high-level overview and are not reﬂected in the informal version. Further, statement of (c’) of our informal lemma carries only half of the information compared to the full version in Lemma 5.4.

Let us now give the actual deﬁnitions of the sets XA, XB. Later, we explain how these deﬁnitions imply the features described above. Deﬁnition 5.3. Suppose that k ∈ N, γ,η,ε,ε′,ν,ρ > 0 and Λ,Ω∗,Ω∗∗ > 0. Suppose that G is a graph with a (k,Ω∗∗,Ω∗,Λ,γ,ε,ν,ρ)-sparse decomposition

∇ = (H,V,D,Greg,Gexp,E)

with respect to Lη,k(G) and Sη,k(G). Suppose further that MA,MB are regularized matchings in G. We then deﬁne the triple (XA,XB,XC) = (XA,XB,XC)(η,∇,MA,MB) by setting

XA := Lη,k(G) \ V (MB) , XB := v ∈ V (MB) ∩ Lη,k(G) : deg(v) < (1 + η)

k 2

, XC := Lη,k(G) \ (XA ∪ XB) ,

![image 177](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile177.png>)

(5.4)

where deg(v) on the second line is deﬁned by

deg(v) := degG v,Sη,k(G) \ (V (Gexp) ∪ E ∪ V (MA ∪ MB) . (5.5)

It is enough to restrict ourselves for the proof to the class LKSsmall(n,k,η) ⊆ LKS(n,k,η). We intentionally leave out (or simplify) almost all numerical parameters in this informal statement. Informal version of Lemma 5.4. Suppose ∇ = (H,V,D,Greg,Gexp,E) is a sparse decomposition of a graph G ∈ LKSsmall(n,k,η). We write S0 := Sη,k(G) \ (V (Gexp) ∪ E). Then there exist regularized matchings MA and MB, such that for the sets XA and XB deﬁned as in Deﬁnition 5.3 we have

- (a) V (MA) ∩ V (MB) = ∅,
- (b) V1(MB) ⊆ S0,
- (c′) for each X ∈ V(MA) ∪ V(MB) we have that X ⊆ Sη,k(G) or X ⊆ Lη,k(G), (e) e XA,S0 \ V (MA) = 0,


(h) if XA induces almost no edges and does not contain a substantial regularized matching5 then there is a substantial amount of edges between XA and XB.

![image 178](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile178.png>)

5The exact quantiﬁcation of “almost no edges” and “substantial regularized matching” does not in guarantee the former property to imply the latter. See also Remark 5.5

The regularized matching MA ∪ MB from the lemma plays the role of M in the motivation above. It remains to justify the dissimilarities between the statement of the lemma and the text above. The ﬁrst discrepancy is that the deﬁnitions of the sets XA and XB in (5.4) are quite diﬀerent from the ones in the motivation above. The other discrepancy is a seeming absence of (5.3) in the statement. As for the ﬁrst issue, consider an arbitrary vertex v ∈ XA. Property (e) tells us that v sends no edges to S0 \ V (MA) ⊇ S0 \ (V (MA) ∪ V (MB)). As v ∈ Lη,k(G), we have that deg(v,Lη,k(G) ∪ V (MA) ∪ V (MB) ∪ V (Gexp) ∪ E) (1 + η)k, as needed. Next, consider a vertex v ∈ XB. The fact that v ∈ Lη,k(G) together with the deﬁnition of deg immediately gives that deg(v,Lη,k(G) ∪ V (MA) ∪ V (MB) ∪ V (Gexp) ∪ E) > (1 + η)k2, again as needed.

![image 180](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile180.png>)

Let us now turn to deriving (5.3). This property is required only for the counterpart of (H2). So, we can assume that we do not have the counterpart of (H1), that is, the set XA induces (almost) no edges. Let us now consider an arbitrary regular pair (X,Y ) in MA ∪ MB. First assume that (X,Y ) ∈ MB. Then (b) tells us that X ⊆ S0. We then have N(XA) ∩ X = ∅ by Property (e), as needed for (5.3). Next, assume that (X,Y ) ∈ MA. Then Deﬁnition 2.3(ii) (together with (c’) of our informal lemma) tells us that at least one of X and Y is contained in Lη,k(G). Say this is X. We then have X ⊆ XA. But the absence of edges inside XA tells us that e(X,XA) = 0, again as needed for (5.3).

5.1.1 Rough versus ﬁne structure

In the dense case [PS12] we can proceed with embedding T using the regularity method immediately after having established a statement like Informal Lemma 5.2. That is, we can zigzag-embed consecutive cut vertices WA ∪ WB of T in AB, or A1A2. When we arrive at a shrub t ∈ SA ∪ SB stemming from cut vertex u ∈ WA∪WB embedded to a cluster D (that is, D = A, D = B, D = A1, or D = A2) we can use (H1) or (H2) to ﬁnd an edge XY ∈ E(Greg) such that DX ∈ E(Greg) and the pair (X,Y ) has not been ﬁlled-up. Then, (i) using that DX ∈ E(Greg) we traverse from D to XY , (ii) we embed t in (X,Y ), and (iii) if t is an internal shrub, we again use that XD ∈ E(Greg) to traverse back6 to D and continue embedding cut vertices in AB or A1A2.

In the current setting of the sparse decomposition, the structure given by Lemma 5.4 would allow us to carry out counterparts to (i) and (ii) (even though there is a number of technical obstacles). That is, we would be able to embed consecutive cut vertices, to traverse to locations suitable for shrubs and to embed these shrubs. However, carrying a counterpart to (iii) is a major problem. The symmetry-based argument from the dense case “if DX is an edge then XD is an edge and thus we can traverse in both directions” does not work when the shrub is not to be embedded in a cluster, but in a subset of E or Gexp. This is going to be addressed in [HKP+c], where we clean the rough structure in such a way that it will allow a counterpart to (iii).

## 5.2 The role of Lemma 4.8 in the proof of Lemma 5.4

In this section, we explain the role of Lemma 4.8 in our proof of Lemma 5.4. That is, we want to explain why it is not possible in general to ﬁnd regular matchings MA and MB from the informal version of Lemma 5.4 inside the cluster graph Greg. Because of this we will have to ﬁnd a suitable “re-regularization” which turns out to be provided by Lemma 4.8.

![image 181](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile181.png>)

6As said at the beginning of Section 5.1, if t is internal, then both of its neighboring cut vertices are in WA. In particular, the distance between these two cut vertices is even. That means that to traverse back to D, we really use the pair XD ∈ E(Greg).

Recall the motivation from Section 5.1. We wish to ﬁnd two sets XA and XB (or two sets within XA) which are suitable for embedding the cut vertices WA and WB of a (τk)-ﬁne partition (WA,WB,SA,SB) of T. In this sketch we just focus on ﬁnding XA; the ideas behind ﬁnding a suitable set XB are similar. To accommodate all the shrubs from SA — which might contain up to k − 2 vertices in total — we need XA to have total degree at least k into the sets Lη,k(G), V (Gexp), E, together with vertices of any ﬁxed matching M consisting of regular pairs. This motivates us to look for a regularized matching M which covers as much as possible of the set S0 := Sη,k(G)\(V (Gexp) ∪ E). as these are the vertices that are not utilizable otherwise. As a next step one would prove that there is a set XA with

mindeg XA,V (G) \ (S0 \ V (M)) k . (By k we mean larger than k by a suitable small additional approximation factor.)

In the dense setting [PS12], where the structure of G is determined by Greg, and where S0 = Sη,k(G), such a matching M can be found inside Greg using the Gallai–Edmonds Matching Theorem. But here, just working with Greg is not enough for ﬁnding a suitable regularized matching as the following example shows.

![image 183](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile183.png>)

|![image 184](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile184.png>)|
|---|


| |
|---|


![image 185](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile185.png>)

![image 186](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile186.png>)

Figure 5.2: An example of a graph G ∈ LKS(n,k,η := 101 ) in which Greg is empty, yet there is no candidate set for XA of vertices which have degrees at least k outside the set S0. Sample

![image 187](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile187.png>)

dense spots are shown in grey.

Figure 5.2 shows a graph G with Lη,k(G) = E. Let us describe the construction of such a graph G. We partition the vertex sets into to-be sets Sη,k(G) and Lη,k(G). We further gather vertices of Sη,k(G) into clusters. We now insert edges into G. All the edges inserted will be in the form of dense spots. These dense spots have either both parts in Lη,k(G), or one part Lη,k(G) and the other in Sη,k(G). We do this so that each inserted dense spot in the Sη,k(G)-part respects the cluster structure, while it behaves in a random-like way in the Lη,k(G)-part. Further, we require that each Lη,k(G)-vertex sends 0.7k edges to Lη,k(G) and 0.4k edges to Sη,k(G), and each Sη,k(G)-vertex receives 0.5k edges from Lη,k(G). Clearly, such a construction is possible.

The point of the construction is that E = Lη,k(G), and that S0 = Sη,k(G) form clusters which do not induce any dense regular pairs. No vertex has degree k outside S0, and the cluster graph Greg contains no matching.

However, in this situation we can still ﬁnd a large regularized matching M between Lη,k(G) and Sη,k(G), by regularizing the crossing dense spots D (which we can assume to be the original dense spots inserted in our construction). In general, obtaining a regularized matching is, of course, more

complicated. Given the above example, one may ask whether the graph Greg has any role at all. The answer is that for constructing M, we can either use directly the edges of Greg, or, if we do not have these edges the information about their lack helps us to ﬁnd M elsewhere.

- 5.3 Finding the structure We can now state the main result of this paper. Lemma 5.4. For every η ∈ (0,1), Ω > 0,γ ∈ (0,η/3) there is a number β > 0 so that for every


ε ∈ (0, γ122η) there exist ε′,π > 0 such that for every ν > 0 there exists a number k0 ∈ N such that for every Ω∗ with Ω∗ < Ω, every Ω∗∗ with Ω∗∗ > max{2,Ω∗} and every k with k > k0 the following holds.

![image 189](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile189.png>)

Suppose ∇ = (H,V,D,Greg,Gexp,E) is a (k,Ω∗∗,Ω∗,Λ,γ,ε′,ν,ρ)-sparse decomposition of a graph G ∈ LKSsmall(n,k,η) with respect to S := Sη,k(G) and L := Lη,k(G) which captures all but

- at most ηkn/6 edges of G. Let c be the size of the clusters V.7 Write S0 := S \ (V (Gexp) ∪ E) . (5.6)


Then GD contains two (ε,β,πc)-regularized matchings MA and MB such that for the triple (XA,XB,XC) := (XA,XB,XC)(η,∇,MA,MB) we have

- (a) V (MA) ∩ V (MB) = ∅,
- (b) V1(MB) ⊆ S0,
- (c) for each (X1,X2) ∈ MA∪MB, there is a dense spot (D1,D2;ED) ∈ D with X1 ⊆ D1, X2 ⊆ D2, and furthermore, either X1 ⊆ S or X1 ⊆ L, and X2 ⊆ S or X2 ⊆ L,
- (d) for each X1 ∈ V1(MA ∪ MB) there exists a cluster C1 ∈ V such that X1 ⊆ C1, and for each X2 ∈ V2(MA ∪ MB) we have X2 ⊆ L ∩ E or there exists C2 ∈ V such that X2 ⊆ C2,
- (e) eG∇ XA,S0 \ V (MA) γkn,
- (f) eGreg(V (G) \ V (MA ∪ MB)) εΩ∗kn,
- (g) for the regularized matching NE := {(X1,X2) ∈ MA ∪ MB : (X1 ∪ X2) ∩ E = ∅} we have eGreg V (G) \ V (MA ∪ MB),V (NE) εΩ∗kn,
- (h) for Mgood := {(X1,X2) ∈ MA : X1 ∪ X2 ⊆ XA} we have that each Mgood-edge is an edge of Greg, and at least one of the following conditions holds


- (K1) 2eG(XA) + eG(XA,XB) ηkn/3,
- (K2) |V (Mgood)| ηn/3.


Remark 5.5. As explained in Section 5.1, property (h) is the most important part of Lemma 5.4. Note that the assertion (K2) implies a quantitatively weaker version of (K1). Indeed, consider (X1,X2) ∈ MA. An average vertex v ∈ X1 sends at least β · πc β · πνk edges to X2. Thus, if |V (Mgood)| ηn/3 then Mgood induces at least (ηn/6) · β · πνk = Θ(kn) edges in XA. Such

![image 190](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile190.png>)

7The number c is irrelevant when V = ∅. In particular, note that in that case we necessarily have MA = MB = ∅ for the regularized matchings given by the lemma.

a bound, however, would be insuﬃcient for our purposes as later η ≫ π,ν. So, the deﬁcit in the number of edges asserted in (K2) (compared to the eG(XA) ηkn/12 part of (K1)) is compensated by the fact that these edges are already regularized.

For the proof we need the well-known Gallai–Edmonds Matching Theorem, which we state next. A graph H is called factor-critical if H − v has a perfect matching for each v ∈ V (H). Theorem 5.6 (Gallai–Edmonds matching theorem (see for instance [Die05, Theorem 2.2.3])). Let H be a graph. Then there exist a set Q ⊆ V (H) and a matching M of size |Q| in H such that

- (1) every component of H − Q is factor-critical, and
- (2) M matches every vertex in Q to a diﬀerent component of H − Q. The set Q in Theorem 5.6 is often referred to as a separator.


Proof of Lemma 5.4. The idea of the proof is to ﬁrst obtain some information about the structure of the graph Greg with the help of Theorem 5.6. Then the structure given by Theorem 5.6 is reﬁned by Lemma 4.8 to yield the assertions of the lemma.

Let us begin with setting the parameters. Let β := βL4.8 be given by Lemma 4.8 for input

- parameters ΩL4.8 := Ω, ρL4.8 := γ2, and let ε′ and π be given by Lemma 4.8 for further input parameter εL4.8 := ε. Last, let k0 be given by Lemma 4.8 with the above parameters and γL4.8 := ν.


Without loss of generality we assume that ε′ ε and β < γ2. We write S := {C ∈ V : C ⊆ S} and L := {C ∈ V : C ⊆ L}. Further, let S0 := {C ∈ S : C ⊆ S0}.

Let Q be a separator and let N0 be a matching given by Theorem 5.6 applied to the graph Greg. We will presume that the pair (Q,N0) is chosen among all the possible choices so that the number of vertices of S0 that are isolated in Greg − Q and are not covered by N0 is minimized. Let SI denote the set of vertices in S0 that are isolated in Greg − Q. Recall that the components of Greg − Q are factor-critical.

Deﬁne SR ⊆ V (Greg) as a minimal set such that

- • SI \ V (N0) ⊆ SR, and
- • if C ∈ S and there is an edge DZ ∈ E(Greg) with Z ∈ SR, D ∈ Q, CD ∈ N0 then C ∈ SR.


Then each vertex from SR is reachable from SI\V (N0) by a path in Greg that alternates between SR and Q, and has every second edge in N0. Also note that for all CD ∈ N0 with C ∈ Q and D ∈ S0 \ SR we have

degGreg(C,SR) = 0 . (5.7) Let us prove another property of SR.

- Claim 5.5.1. SR ⊆ SI ⊆ SR ∪ V (N0). In particular, SR ⊆ S0.


Proof of Claim 5.5.1. By the deﬁnition of SR, we only need to show that SR ⊆ SI. So suppose there is a vertex C ∈ SR \ SI. By the deﬁnition of SR there is a non-trivial path R going from SI \ V (N0) to C that alternates between SR and Q, and has every second edge in N0. Then, the matching N0′ := N0△E(R) covers more vertices of SI than N0 does. Further, it is straightforward to check that the separator Q together with the matching N0′ satisﬁes the assertions of Theorem 5.6. This is a contradiction, as desired.

![image 192](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile192.png>)

![image 193](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile193.png>)

![image 194](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile194.png>)

![image 195](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile195.png>)

Using a very similar alternating path argument we see the following.

- Claim 5.5.2. If CD ∈ N0 with C ∈ Q and D ∈/ SI then degGreg(C,SR) = 0. Using the factor-criticality of the components of Greg − Q we extend N0 to a matching N1

as follows. For each component K of Greg − Q which meets V (N0), we add a perfect matching of K − V (N0). Furthermore, for each non-singleton component K of Greg − Q which does not meet V (N0), we add a matching which meets all but exactly one vertex of L ∩ V (K). This is possible as by the deﬁnition of the class LKSsmall(n,k,η) we have that Greg − L is edgeless, and so L ∩ V (K) = ∅. This choice of N1 guarantees that

eGreg(V \ V (N1)) = 0 . (5.8) We set

M := C1C2 ∈ N0 : C1 ∈ SR,C2 ∈ Q . We have that

eGreg V \ V (N1),V (M) ∩ SR = 0 . (5.9) As S is an independent set in Greg, we have that

QM := V (M) ∩ Q ⊆ L . (5.10)

The matching M in Greg corresponds to an (ε′,γ2,c)-regularized matching M in the underlying graph Greg, with V2(M) ⊆ Q (recall that regularized matchings have orientations on their edges). Likewise, we deﬁne N1 as the (ε′,γ2,c)-regularized matching corresponding to N1. The N1-edges are oriented so that V1(N1) ∩ Q = ∅; this condition does not specify orientations of all the N1-edges and we orient the remaining ones in an arbitrary fashion. We write SR := SR.

- Claim 5.5.3. eG∇ L \ (E ∪ V (M)),SR = 0.


- Proof of Claim 5.5.3. We start by showing that for every cluster C ∈ L \ V (M) we have


degGreg(C,SR) = 0 . (5.11)

First, if C  ∈ Q, then (5.11) is true since SR ⊆ SI by Claim 5.5.1. So suppose that C ∈ Q, and let D ∈ V (Greg) be such that DC ∈ N0. Now if D ∈/ SI then (5.11) follows from Claim 5.5.2. On the other hand, suppose D ∈ SI ⊆ S0. As C ∈/ V (M), we know that D ∈/ SR, and thus, (5.11) follows from (5.7).

Now, by (5.11), Greg has no edges between L \ (E ∪ V (M)) and SR. Also, no such edges can be in Gexp or incident with E, since SR ⊆ S0 by Claim 5.5.1. Finally, since G ∈ LKSsmall(n,k,η) and Ω∗∗ > 2 > (1 + η), there are no edges between H and S. This proves the claim.

![image 197](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile197.png>)

![image 198](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile198.png>)

![image 199](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile199.png>)

![image 200](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile200.png>)

We prepare ourselves for an application of Lemma 4.8. The numerical parameters of the lemma are ΩL4.8,ρL4.8,εL4.8 and γL4.8 as above. The input objects for the lemma are the graph GD of order n′ n, the collection of (γk,γ)-dense spots D, the matching M, the (νk)-ensemble CL4.8 := SR \ V (N1), and the set YL4.8 := L ∩ E. Note that Deﬁnition 3.4, item 6, implies that D absorbs M. Further, (4.20) is satisﬁed by Deﬁnition 3.4, item 7.

The output of Lemma 4.8 is an (ε,β,πc)-regularized matching M′ with the following properties.

![image 202](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile202.png>)

![image 203](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile203.png>)

|![image 204](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile204.png>)|
|---|


![image 205](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile205.png>)

![image 206](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile206.png>)

![image 207](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile207.png>)

![image 208](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile208.png>)

Figure 5.3: The situation in G after applying Lemma 4.8. The dotted line illustrates the separation as in (III).

- (I) |V (M) \ V (M′)| < εn′ εn.
- (II) For each (X1,X2) ∈ M′ there are sets C ∈ SR and (D1,D2;ED) ∈ D such that X1 ⊆ C ∩D1 and either X2 ⊆ L ∩ E ∩ D2 or there exists C′ ∈ QM such that X2 ⊆ L ∩ E ∩ C′.

(Indeed, to see this we use that V1(M) ⊆ SR and that V2(M) ⊆ QM by the deﬁnition of M.)

- (III) There is a partition of M′ into M1 and MB such that eGD SR \ V (N1) ∪ V1(M) \ V1(M1) , ((L ∩ E) ∪ V2(M)) \ V2(MB) < γkn′ .


We claim that also (IV) V (M′) ∩ V (N1 \ M) = ∅.

Indeed, let (X1,X2) ∈ M′ be arbitrary. Then by (II) there is C ∈ SR such that X1 ⊆ C. By Claim 5.5.1, C is a singleton component of Greg − Q. In particular, if C is covered by N1 then C ∈ V (M). It follows that X1 ∩ V (N1 \ M) = ∅. In a similar spirit, the easy fact that (Y ∪ QM) ∩ V (N1 \ M) = ∅ together with (II) gives X2 ∩ V (N1 \ M) = ∅. This establishes (IV).

Observe that (II) implies that V1(M′) ⊆ SR, and so, by Claim 5.5.1 we know that

V1(MB) ⊆ SR ⊆ SI ⊆ S0. (5.12) Set

MA := (N1 \ M) ∪ M1 . (5.13)

Then MA is an (ε,β,πc)-regularized matching. Note that from now on, the sets XA,XB and XC are deﬁned. The situtation is illustrated in Figure 5.3. By (IV), we have V (MA)∩V (MB) = ∅, as required for Lemma 5.4(a). Lemma 5.4(b) follows from (5.12). The claim below asserts that the next two properties are satisﬁed as well.

- Claim 5.5.4. Lemma 5.4(c) and Lemma 5.4(d) are satisﬁed.

- Proof of Claim 5.5.4. Consider an arbitrary pair (X1,X2) ∈ MA ∪ MB. Either we have that (X1,X2) ∈ N1 or (X1,X2) ∈ M′. In the former case, X1X2 is an edge in Greg. Then the properties for (X1,X2) asserted in Lemma 5.4(c) and Lemma 5.4(d) follow from the fact that the cluster graph is prepartitioned with respect to S and L, and from Deﬁnition 3.4(6).

In the case (X1,X2) ∈ M′, the asserted properties are given by (II). We now turn to Lemma 5.4(e). First we prove some auxiliary statements.

![image 210](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile210.png>)

![image 211](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile211.png>)

![image 212](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile212.png>)

![image 213](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile213.png>)

Claim 5.5.5. We have S0 \ V (N1 \ M) ⊆ SR.

- Proof of Claim 5.5.5. Let C ∈ S0 \ V (N1 \ M). Note that if C ∈/ SI, then C ∈ V (N1). On the other hand, if C ∈ SI, then we use Claim 5.5.1 to see that C ∈ SR ∪ V (N1). We deduce that in either case C ∈ SR ∪ V (N1). The choice of C implies that C ∈ SR ∪ V (M). Now, if C ∈ V (M), then C ∈ SR, by (5.10) and by the deﬁnition of M. Thus C ∈ SR, as desired.

![image 214](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile214.png>)

![image 215](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile215.png>)

![image 216](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile216.png>)

![image 217](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile217.png>)

It will be convenient to work with a set S¯0 ⊆ S0, S¯0 := (S ∩ V) \ V (Gexp) = S0. The next two easy claims assert absence of edges of certain types incident to S0 and S¯0. Claim 5.5.6. The vertices in S0 \ S¯0 are isolated in G∇.

- Proof of Claim 5.5.6. Indeed, let us check Deﬁnition 3.6. Clearly, S0 \ S¯0 is disjoint from V (Greg) and V (Gexp). Further, S0 \ S¯0 sends no edges to H, by Deﬁnition 2.3(ii). Lastly, the set S0 \ S¯0 is disjoint from the “avoiding edges” spanned by the vertex sets E and E ∪ V.

![image 218](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile218.png>)

![image 219](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile219.png>)

![image 220](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile220.png>)

![image 221](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile221.png>)

Claim 5.5.7. We have G∇[L ∩ E,S¯0] = GD[L ∩ E,S¯0].

- Proof of Claim 5.5.7. The ⊇-inclusion of the edge-sets is clear. Next, recall that Deﬁnition 3.6 tells us that each edge in G∇ between E and V is either in


- Claim 5.5.8. We have


Gexp or in GD. As S¯0 ∩ V (Gexp) = ∅, the ⊆-inclusion follows. By Claim 5.5.5, we have

![image 222](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile222.png>)

![image 223](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile223.png>)

![image 224](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile224.png>)

![image 225](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile225.png>)

S¯0 \ V (MA) ⊆ S0 \ V (N1 \ M) \ V (MA) ⊆ SR \ V (MA). (5.14) As every edge incident to S0 \ S¯0 is uncaptured, we see that

EG∇ XA ∩ E,S0 \ V (MA) = EG∇ XA ∩ E,S¯0 \ V (MA) (XA∩E = (L∩E)\V(MB), C5.5.7) = EGD (L ∩ E) \ V (MB),S¯0 \ V (MA) (by (5.14)) ⊆ EGD (L ∩ E) \ V (MB) , SR \ V (MA) . (5.15)

EGreg XA ∩ V,S0 \ V (MA) ⊆ EGD ((L ∩ E) ∪ V2(M)) \ V2(MB),SR \ V (MA) .

Before proving Claim 5.5.8, let us see that it implies Lemma 5.4(e). As G ∈ LKSsmall(n,k,η), there are no edges between H and S. That means that any captured edge from XA to S0 \ V (MA) must start in E or in V, and must be contained in GD. Thus Lemma 5.4(e) follows by plugging (III) into (5.15) and into Claim 5.5.8. Let us now turn to proving Claim 5.5.8.

- Proof of Claim 5.5.8. First, observe that by the deﬁnition of XA and by the deﬁnition of M (and M) we have


XA ∩ V ⊆ (V2(M) \ V2(MB)) ∪ (L \ (E ∪ V (M))) . (5.16) Further, by applying (5.14) and Claim 5.5.3 we get

EGreg L \ (E ∪ V (M)),S¯0 \ V (MA) = ∅ . (5.17) Therefore, we obtain

EGreg XA ∩ V,S0 \ V (MA) C5.5.6= EGreg XA ∩ V,S¯0 \ V (MA)

(by (5.16)) ⊆ EGreg V2(M) \ V2(MB),S¯0 \ V (MA) ∪ EGreg L \ (E ∪ V (M)),S¯0 \ V (MA)

(by (5.14), (5.17)) ⊆ EGreg V2(M) \ V2(MB),SR \ V (MA) , as needed.

In order to prove (f) we ﬁrst observe that

![image 227](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile227.png>)

![image 228](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile228.png>)

![image 229](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile229.png>)

![image 230](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile230.png>)

V (N1) \ V (MA ∪ MB) (5.13)= V (N1) \ V (N1 \ M) ∪ M1 ∪ MB

= (V (N1) ∩ V (M)) \ V (MB ∪ M1) (III)= (V (N1) ∩ V (M)) \ V (M′) = V (M) \ V (M′) . (5.18)

Now, we have

eGreg(V (G) \ V (MA ∪ MB)) eGreg(V (G) \ V (N1)) +

degG∇(v)

v∈V (N1)\V (MA∪MB)

degG∇(v) |V (M) \ V (M′)|Ω∗k (by (I)) < εΩ∗kn ,

(by (5.8) and (5.18))

v∈V (M)\V (M′)

which proves (f).

Let us turn to proving (g). First, recall that we have V (NE) ⊆ V (M′)∪V (N1) (cf. 5.13). Since V (N1) ∩ E = ∅ we actually have

V (NE) = V (NE) ∩ V (M′) . (5.19) Using (5.19) and (II) we get

eGreg (V (G) \ V (N1),V (NE)) eGreg V (G) \ V (N1),V (M′) ∩ SR

(by (5.9)) eGreg V (G) \ V (N1),(V (M′) \ V (M)) ∩ SR (by (IV)) eGreg V (G) \ V (N1),(V (M′) \ V (N1)) ∩ SR

2eGreg (V (G) \ V (N1)) (5.8)= 0 . (5.20)

We have

eGreg (V (G) \ V (MA ∪ MB),V (NE)) eGreg (V (G) \ V (N1),V (NE))

+ eGreg (V (N1) \ V (MA ∪ MB),V (G)) (by (5.20)) 0 + |V (N1) \ V (MA ∪ MB)|Ω∗k

(by (5.18), (I)) εΩ∗kn , as needed.

We have thus shown Lemma 5.4(a)–(g). It only remains to prove Lemma 5.4(h), which we will do in the remainder of this section.

We ﬁrst collect several properties of XA and XC. The deﬁnitions of XC and S0 give

k 2

|XC|(1 + η)

![image 232](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile232.png>)

eG XC,S0 \ V (MA ∪ MB) |S0 \ V (MA ∪ MB)|(1 + η)k . (5.21)

Each vertex of XC has degree at least (1 + η)k2 into S, and so,

![image 233](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile233.png>)

k 2

eG(S,XC) |XC| (1 + η)

![image 234](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile234.png>)

. (5.22)

Also, for each vertex v ∈ XC, Deﬁnition 2.3(ii) gives that

degG(v) = ⌈(1 + η)k⌉ (5.23) Consequently (using ⌈a⌉ − ⌈a2⌉ a2),

![image 235](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile235.png>)

![image 236](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile236.png>)

eG XA,XC

(5.23)

|XC|⌈(1 + η)k⌉ − eG(S,XC) (5.22)

k 2

|XC|(1 + η)

(5.24)

![image 237](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile237.png>)

(5.21)

|S0 \ V (MA ∪ MB)|(1 + η)k . (5.25)

Let Mgood be deﬁned as in Lemma 5.4(h), that is, Mgood := {(X1,X2) ∈ MA : X1∪X2 ⊆ XA}. Note that (5.12) implies that X1 ⊆ S for every (X1,X2) ∈ MB. Thus by the deﬁnition of XA,

if (X1,X2) ∈ MA ∪ MB with X1 ∪ X2 ⊆ L, then (X1,X2) ∈ Mgood. (5.26)

We will now prove the ﬁrst part of Lemma 5.4(h), that is, we show that each Mgood-edge is an edge of Greg. Indeed, by (II), we have that V1(M1) ⊆ S, so as XA ∩ S = ∅, it follows that M1 ∩ Mgood = ∅. Thus Mgood ⊆ N1. As N1 corresponds to a matching in Greg, all is as desired.

Finally, let us assume that neither (K1) nor (K2) is fulﬁlled. After ﬁve preliminary observations (Claim 5.5.9–Claim 5.5.13), we will derive a contradiction from this assumption.

- Claim 5.5.9. We have |S ∩ V (MA)| |XA ∩ V (MA)|.


- Proof of Claim 5.5.9. To see this, recall that each MA-vertex X ∈ V(MA) is either contained in S, or in L. Further, if X ⊆ S then its partner in MA must be in L, as S is independent. Now, the claim follows after noticing that L ∩ V (MA) = XA ∩ V (MA).


![image 238](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile238.png>)

![image 239](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile239.png>)

![image 240](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile240.png>)

![image 241](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile241.png>)

- Claim 5.5.10. We have |S \ V (MA ∪ MB)| + 2ηn < |XA \ V (MA)| + ηn/3.

- Proof of Claim 5.5.10. As G ∈ LKS(n,k,η), we have |S| + 2ηn |L|. Therefore,

|S \ V (MA ∪ MB)| + 2ηn |L \ V (MA ∪ MB)| +

(X1,X2)∈MA∪MB X1∪X2⊆L

|X1 ∪ X2|

(5.26)= |XA \ V (MA)| + |V (Mgood)|

¬(K2)

< |XA \ V (MA)| + ηn/3 .

![image 243](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile243.png>)

![image 244](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile244.png>)

![image 245](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile245.png>)

![image 246](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile246.png>)

Claim 5.5.11. We have eG∇ XA ∩ (E ∪ V (M)),SR \ V (MA) < ηkn/2.

- Proof of Claim 5.5.11. As

XA ∩ (E ∪ V (M)) ⊆ ((L ∩ E) ∪ V2(M)) \ V2(MB) and

SR \ V (MA) ⊆ SR \ V (N1) ∪ V1(M) \ V1(M1) , we get from (III) that

eGD XA ∩ (E ∪ V (M)),SR \ V (MA) γkn . (5.27)

Observe now that both sets XA∩(E∪V (M)) and SR\V (MA) avoid H. Further, no edges between them belong to Gexp, because Claim 5.5.1 implies that SR \ V (MA) ⊆ S0 ⊆ V (G) \ V (Gexp). Therefore, we can pass from GD to G∇ in (5.27) to get

eG∇ XA ∩ (E ∪ V (M)),SR \ V (MA) γkn < ηkn/2 .

![image 247](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile247.png>)

![image 248](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile248.png>)

![image 249](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile249.png>)

![image 250](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile250.png>)

Claim 5.5.12. We have S \ (SR ∪ V (MA)) ⊆ S \ (S¯0 ∪ V (MA ∪ MB)).

- Proof of Claim 5.5.12. The claim follows directly from the following two inclusions.


- Claim 5.5.13. We have


SR ∪ V (MA) ⊇ S ∩ V (MA ∪ MB) , and (5.28) SR ∪ V (MA) ⊇ S¯0 . (5.29)

Now, (5.28) is trivial, as by (II) we have that SR ⊇ S ∩ V (MB). To see (5.29), it suﬃces by (5.13) to prove that V (N1 \ M) ∪ SR ⊇ S0. This is however the assertion of Claim 5.5.5.

![image 251](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile251.png>)

![image 252](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile252.png>)

![image 253](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile253.png>)

![image 254](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile254.png>)

Next, we bound eG∇ XA,S .

- 1

![image 255](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile255.png>)

- 2


eG∇ XA,S |S ∩ V (MA)|(1 + η)k + |S \ (S0 ∪ V (MA ∪ MB))|(1 + η)k +

ηkn .

![image 257](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile257.png>)

![image 258](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile258.png>)

![image 259](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile259.png>)

![image 260](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile260.png>)

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | |![image 261](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile261.png>)<br><br>![image 262](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile262.png>)<br><br>![image 263](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile263.png>)<br><br>![image 264](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile264.png>)|![image 265](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile265.png>)<br><br>![image 266](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile266.png>)|
| | | | | | | |


![image 267](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile267.png>)

![image 268](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile268.png>)

![image 269](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile269.png>)

![image 270](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile270.png>)

![image 271](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile271.png>)

![image 272](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile272.png>)

![image 273](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile273.png>)

![image 274](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile274.png>)

![image 275](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile275.png>)

![image 276](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile276.png>)

![image 277](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile277.png>)

![image 278](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile278.png>)

![image 279](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile279.png>)

![image 280](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile280.png>)

Figure 5.4: A simpliﬁed computation showing that ¬(K1), ¬(K2) leads to a contradiction. Denoting by x the size of S0\V (MA∪MB) we get ① |XC| 2x. On the other hand, each vertex of XA emanates k edges which are absorbed by the sets V1(MA), S \ (V (MA ∪ MB) ∪ S0), and XC. The vertices of V1(MA) and S \ (V (MA ∪ MB) ∪ S0) can absorb k edges. The vertices of XC receive k2 edges of XA by (5.24). This leads to ② |XC| > 2x, doubling the size of the “excess” vertices of XA.

![image 281](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile281.png>)

- Proof of Claim 5.5.13. We have


eG∇ XA,S = eG∇ XA,S ∩ V (MA) + eG∇ XA,S \ (SR ∪ V (MA))

+ eG∇ XA \ (E ∪ V (M)),SR \ V (MA) + eG∇ XA ∩ (E ∪ V (M)),SR \ V (MA) .

To bound the ﬁrst term we use that each vertex in S ∩ V (MA) has degree at most (1 + η)k, and thus obtain eG∇(XA,S ∩ V (MA)) |S ∩ V (MA)|(1 + η)k. To bound the second term, we again use a bound on degree of vertices of S \ (SR ∪ V (MA)) ∪ (S0 \ S¯0)), together with Claim 5.5.12. The third term is zero by Claim 5.5.3. The fourth term can be bounded by Claim 5.5.11.

![image 282](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile282.png>)

![image 283](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile283.png>)

![image 284](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile284.png>)

![image 285](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile285.png>)

A relatively short double counting below will lead to the ﬁnal contradiction. The idea behind this computation is given in Figure 5.4.

|XA|(1 + η)k

(by ¬(K1), (5.25), C5.5.13)

degG∇(v) + 2 e(G) − e(G∇)

degG(v)

v∈XA

v∈XA

ηkn 3

2eG∇(XA) + eG∇(XA,XB) + eG∇ XA,XC + eG∇ XA,S +

![image 287](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile287.png>)

7 6

ηkn + S0 \ V (MA ∪ MB) (1 + η)k

![image 288](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile288.png>)

+ |S ∩ V (MA)|(1 + η)k

+ |S \ (S0 ∪ V (MA ∪ MB))|(1 + η)k

- (by C5.5.9)

7 6

![image 289](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile289.png>)

ηkn + |S \ V (MA ∪ MB)|(1 + η)k

+ |XA ∩ V (MA)|(1 + η)k

- (by C5.5.10)


7 6

5 3

ηkn + |XA \ V (MA)| −

ηn (1 + η)k

![image 290](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile290.png>)

![image 291](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile291.png>)

+ |XA ∩ V (MA)|(1 + η)k < |XA|(1 + η)k −

- 1

![image 292](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile292.png>)

- 2


ηkn ,

a contradiction. This completes the proof of Lemma 5.4.

(5.30)

![image 293](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile293.png>)

![image 294](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile294.png>)

![image 295](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile295.png>)

![image 296](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile296.png>)

# 6 Acknowledgements

The work on this project lasted from the beginning of 2008 until 2014 and we are very grateful to the following institutions and funding bodies for their support.

During the work on this paper Hladky´ was also aﬃliated with Zentrum Mathematik, TU Munich and Department of Computer Science, University of Warwick. Hladky´ was funded by a BAYHOST fellowship, a DAAD fellowship, Charles University grant GAUK 202-10/258009, EPSRC award EP/D063191/1, and by an EPSRC Postdoctoral Fellowship during the work on the project.

Komlo´s and Szemere´di acknowledge the support of NSF grant DMS-0902241. Piguet has been also aﬃliated with the Institute of Theoretical Computer Science, Charles University in Prague, Zentrum Mathematik, TU Munich, the Department of Computer Science and DIMAP, University of Warwick, and the School of Mathematics, University of Birmingham. Piguet acknowledges the support of the Marie Curie fellowship FIST, DFG grant TA 309/2-1, a DAAD fellowship, Czech Ministry of Education project 1M0545, EPSRC award EP/D063191/1, and the support of the EPSRC Additional Sponsorship, with a grant reference of EP/J501414/1 which facilitated her to travel with her young child and so she could continue to collaborate closely with her coauthors on this project. This grant was also used to host Stein in Birmingham. Piguet was supported by the European Regional Development Fund (ERDF), project “NTIS — New Technologies for Information Society”, European Centre of Excellence, CZ.1.05/1.1.00/02.0090.

Stein was aﬃliated with the Institute of Mathematics and Statistics, University of Sa˜o Paulo, the Centre for Mathematical Modeling, University of Chile and the Department of Mathematical Engineering, University of Chile. She was supported by a FAPESP fellowship, and by FAPESP travel grant PQ-EX 2008/50338-0, also CMM-Basal, FONDECYT grants 11090141 and 1140766. She also received funding by EPSRC Additional Sponsorship EP/J501414/1.

We enjoyed the hospitality of the School of Mathematics of University of Birmingham, Center for Mathematical Modeling, University of Chile, Alfre´d R´enyi Institute of Mathematics of the Hungarian Academy of Sciences and Charles University, Prague, during our long term visits.

The yet unpublished work of Ajtai, Komlo´s, Simonovits, and Szemere´di on the Erd˝os–So´s Conjecture was the starting point for our project, and our solution crucially relies on the methods developed for the Erd˝os-So´s Conjecture. Hladky´, Piguet, and Stein are very grateful to the former group for explaining them those techniques.

A doctoral thesis entitled Structural graph theory submitted by Hladky´ in September 2012 under the supervision of Daniel Kra´l at Charles University in Prague is based on the series of the papers [HKP+a, HKP+b, HKP+c, HKP+d]. The texts of the two works overlap greatly. We are grateful to PhD committee members Peter Keevash and Michael Krivelevich. Their valuable comments are reﬂected in the series.

We thank the referees for their very detailed remarks. The contents of this publication reﬂects only the authors’ views and not necessarily the views

of the European Commission of the European Union.

SYMBOL INDEX

![image 298](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile298.png>)

# Symbol index

[n], 1

- d(U,W), 2 deg, 2 maxdeg, 2 mindeg, 2 M-edge, 8 E(G), 2
- e(G), 2 ℓ-ensemble, 2 e(X), 2 e(X,Y ), 2 G¯(n,k,Ω,ρ,ν), 5 G(n,k,Ω,ρ,ν,τ), 5 GD, 5 Greg, 5 G∇, 5 Lη,k(G), 3 LKS(n,k,η), 3 LKSsmall(n,k,η), 3 N(v), 2 Sη,k(G), 3 V1(M), V2(M), V (M), 8 V1(M), V2(M), V(M), 8 M-vertex, 8 V (G), 2 v(G), 2 XA(η,∇,MA,MB), 20 XB(η,∇,MA,MB), 20 XC(η,∇,MA,MB), 20 trees(k), 2


GENERAL INDEX

![image 299](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile299.png>)

# General index

absorb, 8 alternating path, 9 augmenting path, 9 avoiding, 4 avoiding threshold, 5

bounded decomposition, 4 captured edges, 5 cluster, 5 dense cover, 4 dense spot, 4 density, 2 M-edge, 8 empty graph, 2 ensemble, 2 factor-critical, 24 irregular, 2 length of alternating path, 9 nowhere-dense, 4 regular pair, 2 regularized matching, 7 separator, 24 sparse decomposition, 5 M-vertex, 8

REFERENCES

![image 300](<2014-hladk-approximate-loebl-koml-s-s-conjecture_images/imageFile300.png>)

# References

[AKS95] M. Ajtai, J. Komlo´s, and E. Szemere´di. On a conjecture of Loebl. In Graph theory, combinatorics, and algorithms, Vol. 1, 2 (Kalamazoo, MI, 1992), Wiley-Intersci. Publ., pages 1135–1146. Wiley, New York, 1995.

[Coo09] O. Cooley. Proof of the Loebl-Koml´os-So´s conjecture for large, dense graphs. Discrete Math., 309(21):6190–6228, 2009.

[Die05] R. Diestel. Graph theory, volume 173 of Graduate Texts in Mathematics. Springer-Verlag, Berlin, third edition, 2005.

[EFLS95] P. Erd˝os, Z. Fu¨redi, M. Loebl, and V. T. So´s. Discrepancy of trees. Studia Sci. Math. Hungar., 30(1-2):47–57, 1995.

- [HKP+a] J. Hladky´, J. Komlo´s, D. Piguet, M. Simonovits, M. Stein, and E. Szemere´di. The approximate Loebl–Koml´os–So´s Conjecture I: The sparse decomposition. Manuscript (arXiv:1408.3858).
- [HKP+b] J. Hladky´, J. Komlo´s, D. Piguet, M. Simonovits, M. Stein, and E. Szemere´di. The approximate Loebl–Koml´os–So´s Conjecture II: The rough structure of LKS graphs. Manuscript (arXiv:1408.3871).
- [HKP+c] J. Hladky´, J. Komlo´s, D. Piguet, M. Simonovits, M. Stein, and E. Szemere´di. The approximate Loebl–Koml´os–So´s Conjecture III: The ﬁner structure of LKS graphs. Manuscript (arXiv:1408.3866).
- [HKP+d] J. Hladky´, J. Komlo´s, D. Piguet, M. Simonovits, M. Stein, and E. Szemere´di. The approximate Loebl–Koml´os–So´s Conjecture IV: Embedding techniques and the proof of the main result. Manuscript (arXiv:1408.3870).


[HP15] J. Hladky´ and D. Piguet. Loebl–Koml´os–So´s Conjecture: dense case. J. Combin. Theory Ser. B, 2015. http://dx.doi.org/10.1016/j.jctb.2015.07.004.

[KO09] D. Ku¨hn and D. Osthus. Embedding large subgraphs into dense graphs. In Surveys in combinatorics 2009, volume 365 of London Math. Soc. Lecture Note Ser., pages 137–167. Cambridge Univ. Press, Cambridge, 2009.

[PS12] D. Piguet and M. J. Stein. An approximate version of the Loebl-Koml´os-So´s conjecture. J. Combin. Theory Ser. B, 102(1):102–125, 2012.

[Sze78] E. Szemere´di. Regular partitions of graphs. In Proble`mes combinatoires et the´orie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), volume 260 of Colloq. Internat. CNRS, pages 399–401. CNRS, Paris, 1978.

[Zha11] Y. Zhao. Proof of the (n/2 − n/2 − n/2) conjecture for large n. Electron. J. Combin., 18(1):Paper 27, 61, 2011.

