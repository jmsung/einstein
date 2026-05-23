---
type: source
kind: paper
title: Left and right convergence of graphs with bounded degree
authors: Christian Borgs, Jennifer Chayes, Jeff Kahn, László Lovász
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1002.0115v1
source_local: ../raw/2010-borgs-left-right-convergence-graphs.pdf
topic: general-knowledge
cites:
---

arXiv:1002.0115v1[math.CO]31Jan2010

Left and right convergence of graphs with bounded degree

Christian Borgs, Jennifer Chayes, Jeﬀ Kahn∗, La´szlo´ Lova´sz† (January 31, 2010)

# Contents

- 1 Introduction 2
- 2 Preliminaries 2

- 2.1 Homomorphism numbers and densities . . . . . . . . . . . . . . . . . . . . . . . . 3
- 2.2 Local convergence of a graph sequence . . . . . . . . . . . . . . . . . . . . . . . . 4
- 2.3 Chromatic polynomial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- 2.4 Subtree counts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 2.5 Weighted subtrees and weighted chromatic invariants . . . . . . . . . . . . . . . . 6


- 3 Left-convergence implies right-convergence 8

- 3.1 Proof via Dobrushin Uniqueness . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
- 3.2 Proof via Mayer expansion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13


- 3.2.1 Stable sets, Mayer expansion, and Dobrushin’s lemma . . . . . . . . . . . 13
- 3.2.2 Mayer expansion for lnt(G,H) . . . . . . . . . . . . . . . . . . . . . . . . 14
- 3.2.3 Proof of Theorem 3.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17


- 4 Right convergence implies left convergence 18

- 4.1 Linear independence of homomorphism functions . . . . . . . . . . . . . . . . . . 18
- 4.2 Convergence of graph sequences . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19


- 5 Food for thought 21


Abstract

The theory of convergent graph sequences has been worked out in two extreme cases, dense graphs and bounded degree graphs. One can deﬁne convergence in terms of counting homomorphisms from ﬁxed graphs into members of the sequence (left-convergence), or counting homomorphisms into ﬁxed graphs (right-convergence). Under appropriate conditions, these two ways of deﬁning convergence was proved to be equivalent in the dense case by Borgs, Chayes, Lova´sz, S´os and Vesztergombi. In this paper a similar equivalence is established in the bounded degree case.

In terms of statistical physics, the implication that left convergence implies right convergence means that for a left-convergent sequence, partition functions of a large class of

![image 1](<2010-borgs-left-right-convergence-graphs_images/imageFile1.png>)

∗Research supported by NSF grant DMS0701175 †Research supported by OTKA grant No. 67867

statistical physics models converge. The proof relies on techniques from statistical physics, like cluster expansion and Dobrushin Uniqueness.

# 1 Introduction

The theory of convergent graph sequences has been worked out in two extreme cases, dense graphs and bounded degree graphs. The case of dense graphs is probably easier; convergence of such graphs was introduced and characterized in diﬀerent ways in [5, 6]. Convergence of bounded degree graph sequences was deﬁned by Benjamini and Schramm [2], and has inspired a lot of work [3, 15, 8, 22]. While this is perhaps the more important case from the point of view of applications, the theory is less complete, and, for example, some of the characterizations of convergence in the dense case have no analogues. The goal of this paper is to prove, for bounded degree graphs, an analogue of one of these characterizations.

For a simple ﬁnite graph G and node v ∈ V (G), let BG(v,r) denote the subgraph of G induced by the nodes at distance at most r from v. We consider this as a rooted graph, with v designated as its root. Following [2], a sequence (G1,...,Gn) of simple graphs with degrees uniformly bounded by D is called locally convergent (weakly convergent, left-convergent) if for every ﬁxed integer r ≥ 1, selecting a random node v uniformly from V (G), the probability that BG

(v,r) is a ﬁxed rooted graph U tends to a limit as n → ∞. It is not hard to see that this deﬁnition is equivalent to saying that for every connected graph F, hom(F,Gn)/|Gn| tends to a limit, where hom(F,Gn) is the number of homomorphisms (adjacency preserving maps) of F into Gn, and |Gn| = |V (Gn)| is the number of nodes of Gn.

n

This reformulation raises the possibility of deﬁning convergence by turning the arrows around, i.e., in terms of hom(Gn,H) for ﬁxed graphs H. It is easy to see that the “right” normalization in this case is lnhom(Gn,H)/|Gn|.

In general, convergence of lnhom(Gn,H)/|Gn| does not follow from left-convergence. As an example, if Gn is the n-cycle, then the sequence (Gn) is trivially locally convergent. But if K2 is the complete graph with 2 nodes, then lnhom(Gn,K2)/|Gn| alternates between (ln2)/n and −∞ depending on the parity of n.

We will prove (Theorem 3.1 that if H is suﬃciently dense (depending on D), then local convergence does imply that lnhom(Gn,H)/|Gn| is convergent. Conversely (4.3), if lnhom(Gn,H)/|Gn| is convergent for every suﬃciently dense H, then (Gn) is locally convergent.

# 2 Preliminaries

A graph is simple if it has no loops or parallel edges. A simple looped graph is a simple graph with a loop added at each of its node. A weighted graph H is a graph with a weight αi(H) > 0 associated with each node i and a real weight βij(H) associated with each edge ij. (The weights βij(H) may be negative.) We will consider each weighted graph as a complete graph with loops at all nodes; absence of an edge is indicated by weight 0. (No parallel edges are allowed in a weighted graph.) If the graph H is understood from the context, we use the notation αi and

βij. We can consider every simple graph (looped or not looped) as a weighted graph on the same node set, where the original edges have weight 1 and the missing edges have weight 0. Let

αH = i∈V (H) αi(H) denote the total nodeweight of H.

![image 2](<2010-borgs-left-right-convergence-graphs_images/imageFile2.png>)

We denote by H the weighted graph obtained from H by replacing each edgeweight βij by 1 − βij. (Note that this also applies to loops. So if H is the weighted graph corresponding to a simple graph, then H corresponds to the complement of H with a loop added at each node.)

![image 3](<2010-borgs-left-right-convergence-graphs_images/imageFile3.png>)

Let Sub(G) denote the set of nonempty subgraphs of G without isolated nodes, Con(G), the set of connected subgraphs of G with at least two nodes, CInd(G), the set of connected induced subgraphs of G with at least two nodes, and CSpan(G), the set of connected spanning subgraphs of G (with one or more nodes).

To simplify notation, we will write |G| = |V (G)|. Let {A1,...,An} be a family of sets. We denote by L(A1,...,An) their intersection graph,

i.e., the graph on V = [n] in which we connect i and j by an edge if Ai ∩ Aj = ∅. For a set V , we denote by Π(V ) the set of its partitions.

- 2.1 Homomorphism numbers and densities


For two (ﬁnite) simple graphs F and G, hom(F,G) denotes the number of homomorphisms (adjacency preserving maps) from F to G. We deﬁne t(F,G) to be the probability that a random map of V (F) into V (G) is a homomorphism, i.e.,

hom(F,G) |G||F|

.

t(F,G) =

![image 4](<2010-borgs-left-right-convergence-graphs_images/imageFile4.png>)

We call t(F,G) the homomorphism density of F in G.

Sometimes we need to consider the number of injective homomorphisms inj(F,G), the number of embeddings as induced subgraphs, ind(F,G), and the number of homomorphisms surjective on both the nodes and the edges, surj(F,G). We denote by aut(F) = ind(F,F) = surj(F,F) the number of automorphisms of F. The quotients inj0(F,G) = inj(F,G)/inj(F,F) and ind0(F,G) = ind(F,G)/ind(F,F) count the numbers of subgraphs and induced subgraphs of G isomorphic to

- F, respectively. We extend these notions to the case when the target graph (denoted by H in this case) is


weighted:

βφ(u),φ(v)(H)

αφ(u)(H)

hom(F,H) =

uv∈E(F)

φ: V (F)→V (H) u∈V (F)

where the sum runs over all maps from V (F) to V (HG). The homomorphism density is now deﬁned as

hom(F,H) αH|F|

.

t(F,H) =

![image 5](<2010-borgs-left-right-convergence-graphs_images/imageFile5.png>)

We will also need the following related quantity:

(−1)|E(F)|t(F,H). (1)

z(G,H) =

F∈CSpan(G)

This quantity plays an important role in the sequel, and it would be interesting to explore its combinatorial signiﬁcance. We have the inverse relation

(−1)|E(J)|t(J,H)

(−1)|E(F)|

(−1)|E(F)|z(F,H) =

J∈CSpan(F)

F∈CSpan(G)

F∈CSpan(G)

t(J,H)

=

J∈CSpan(G)

(−1)|E(F)|−|E(J)| = t(G,H). (2)

J⊆F⊆G

- 2.2 Local convergence of a graph sequence

Let G = (V,E) be a graph with degrees bounded by D, and ﬁx an integer r ≥ 0. For v ∈ V , let N(v) = NG(v) denote set of nodes adjacent to v. For v ∈ V , let B(v,r) = BG(v,r) denote the subgraph of G induced by all nodes at a distance at most r from v (the r-neighborhood of node v, or the r-ball about v). So B(v,1) is the subgraph induced by N(v)∪{v}. We consider B(v,r) as a rooted graph, i.e., the node v is speciﬁed as the center of B(v,r). For ﬁxed r, there is a ﬁnite number (depending on D and r only) of possible r-balls U1,...,UN. Let µ(G,Ui) denote the fraction of nodes of G whose r-neighborhood is Ui. We can think of µ as a probability distribution on possible r-balls.

We call a sequence (Gn) of graphs with degrees bounded by D locally convergent, or leftconvergent if µ(Gn,U) tends to a limit µ(U) as n → ∞ for every r and every r-ball U.

It is easy to see that if (Gn) is left-convergent, then for every connected graph F the sequence hom(F,Gn)/|Gn| is convergent. It is also quite easy to see that this property is suﬃcient for local convergence. By formulas (1) and (2), we could also require that z(F,Gn) is convergent for every simple graph F.

We can also talk about right-convergence, meaning that lnhom(Gn,H)/|Gn| tends to a limit

- as n → ∞ (here H can be a weighted graph; we’ll see that the normalization is appropriate). However, we will not formally deﬁne right-convergence, since there seem to be diﬀerent ways of specifying which weighted graphs H to consider here. Rather, we want to ﬁnd a reasonable class of weighted graphs H for which right-convergence is equivalent to local (left-) convergence.


- 2.3 Chromatic polynomial


- Let G = (V,E) be a simple graph with n nodes. For every nonnegative integer y, we denote by chr(G,y) the number of y-colorations of G. Note that chr(G,q) = hom(G,Kq).


Let chr0(G,k) denote the number of k-colorations of G in which all colors occur. Then clearly

∞

chr(G,y) =

chr0(G,k)

k=0

y k

. (3)

This implies that chr(G,y) is a polynomial in y with leading term yn and constant term 0, which is called the chromatic polynomial of G. It is easy to see that if G is a simple graph, then for every e ∈ E(G),

chr(G,q) = chr(G \ e,q) − chr(G/e,q), (4)

where G \ e and G/e arise from G by deleting and contracting e, respectively (in G/e, parallel edges are collapsed to one). From this recurrence a number of properties of the chromatic polynomial are easily proved, for example, that its coeﬃcients alternate in sign.

The coeﬃcient of the linear term in the chromatic polynomial is

′)|, (5)

(−1)|E(G

cr(G) =

G′∈CSpan

which is called the Crapo invariant or chromatic invariant of the graph. Trivially, cr(G) = 0 if

- G is disconnected. It follows from (4) that if G is a simple graph, then for every e ∈ E(G),


cr(G) = cr(G\e) − cr(G/e). (6)

This implies by induction that (−1)|G|−1cr(G) > 0 if G is connected.

- 2.4 Subtree counts


Let tree(G) denote the number of spanning trees in G. More generally, let tree(G;v,k) denote the number of subtrees of G with k nodes, containing a given node v ∈ V (G). Let TD be an inﬁnite rooted D-ary tree, with root r. The following formula is well known ([24], Theorem 5.3.10):

kD k − 1

1 k

. (7)

tree(TD;r,k) =

![image 6](<2010-borgs-left-right-convergence-graphs_images/imageFile6.png>)

The right hand side has this more convenient estimate:

(kD)k−1 k!

ekDk−1 k

(eD)k−1 2

1 k

kD k − 1 ≤

√

<

<

![image 7](<2010-borgs-left-right-convergence-graphs_images/imageFile7.png>)

![image 8](<2010-borgs-left-right-convergence-graphs_images/imageFile8.png>)

![image 9](<2010-borgs-left-right-convergence-graphs_images/imageFile9.png>)

![image 10](<2010-borgs-left-right-convergence-graphs_images/imageFile10.png>)

![image 11](<2010-borgs-left-right-convergence-graphs_images/imageFile11.png>)

2πk

(assuming k ≥ 3, but the bound is trivially true for k = 2 as well).

- Lemma 2.1 Let G be a graph with maximum degree D and let v ∈ V (G).


- (a) The number of subtrees of G with k nodes containing v is at most k1 k kD−1 .

![image 12](<2010-borgs-left-right-convergence-graphs_images/imageFile12.png>)

- (b) The number of connected subgraphs of G with m edges containing v is at most


(m+1)D

1 m+1

m . (c) The number of connected induced subgraphs of G with k nodes containing v is at most

![image 13](<2010-borgs-left-right-convergence-graphs_images/imageFile13.png>)

kD k−1 .

- 1 k


![image 14](<2010-borgs-left-right-convergence-graphs_images/imageFile14.png>)

(d) The number of connected subgraphs of G with k nodes containing v is at most 2Dk.

Proof. Throughout this proof, we drop the subscript D from TD.

- (a) It suﬃces to note the easy fact that for any graph G with maximum degree D, the number


of subtrees with k nodes containing v is not larger than the corresponding number in T. Indeed, we could replace T by the rooted tree in which the root has degree D, all the other nodes have (down-)degree D − 1.

- (b) Similarly as in (a) it suﬃces to prove that for any graph G with maximum degree D,


the number of connected subgraphs of G with m edges containing v is not larger than the corresponding number in T.

Let us label the edges going out of any given node v of G arbitrarily by 1,...,dG(v). Also, label the edges going from a node of T to its children arbitrarily 1,...,D. Let F be a connected subgraph of G containing v. Let T0 be a spanning tree in F. Orient F so that T0 is oriented away from the root v (the other edges are oriented arbitrarily).

There is a unique embedding φ : V (F) ֒→ V (T) that preserves the edges of F, and for at each node u ∈ V (F), the edges of T0 leaving u in T0 are mapped onto edges in T with the same label. For every edge ab ∈ E(F) \ E(T0), map it onto the edge of T leaving φ(a) with the same label. This assigns to F a subtree F′ of T with m edges.

Clearly, F′ uniquely determines F: starting from the root, we can map the edges of T back

into G. This proves (b). (c) is a trivial consequence of (a). (d) We can select the edges of F incident with v in less than 2D ways; then going to one of

the neighbors v1 of v, we can select the set of edges of F incident with v1 in less than 2D ways, etc. Repeating this k times, we have ﬁnished selecting F.

- 2.5 Weighted subtrees and weighted chromatic invariants


- Let H be a weighted graph. We extend the deﬁnitions of the number of subtrees and of the chromatic invariant to weighted graphs:


(−1)|E(F)|

cr(H) =

e∈F

F∈CSpan(H)

βe, tree(H) =

βe.

F∈SpTr(G) e∈F

We note that if all edgeweights of H are 1, then tree(H) is the number of spanning trees and cr(H) is the chromatic invariant of the underlying simple graph. (The nodeweights play no role in these deﬁnitions.)

For e ∈ E(H), let H − e denote the weighted graph obtained from H by deleting the edge e. We need two versions of the operation of contracting an edge. Let H/e denote the graph obtained by contracting e, where the arising parallel edges are replaced by a single edge whose weight is the sum of the weights of its pre-images. Let H ÷e denote the graph obtained from H similarly, except that the new edgeweight is the sum minus the product of the weights of its pre-images. (Note that for graphs H with edgeweights between 0 and 1, the resulting edgeweight again lies between 0 and 1, which is not necessarily the case for H/e). The two quantities introduced above satisfy the recurrence relations

cr(H) = cr(H − e) − βecr(H ÷ e), tree(H) = tree(H − e) + βetree(H/e). (8)

For graphs with edge weights between 0 and 1, the ﬁrst of these relations implies that (−1)|H|−1cr(H) > 0.

Let G be a simple graph and H, a weighted graph, and let α˜ be the normalized weight α˜i = αi(F)/αF. By a random map G → H we mean a map V (G) → V (H), where the image of each node of G is chosen independently from the probability distribution α˜.

For any map φ : V (G) → V (H), we can deﬁne a weighting of G, where the weight of an edge of G is the weight of its image in H. We denote this weighted graph by Gφ. Note that for a random map G → H we have

βφ(i)φ(j),

t(G,H) = Eφ

ij∈E(G)

and so z(G,H) =

(−1)|E(F)|t(F,H)

F∈CSpan(G)

(−1)|E(F)|Eφ

=

ij∈E(F)

F∈CSpan(G)

βφ(i)φ(j) = Eφcr(Gφ). (9)

- Lemma 2.2 Let H be a weighted graph with node weights 1 and edge weights in [0,1], then |cr(H)| ≤ tree(H).

Proof. By equation (8), |cr(H)| ≤ |cr(H − e)| + βe(H)|cr(H ÷ e)|.

Since the edgeweights in H ÷ e are not larger than the corresponding edgeweights in H/e, we get by induction on the number of edges that

|cr(H)| ≤ tree(H − e) + βe(H)tree(H/e) = tree(H).

To state our next lemma, we deﬁne c(H) = max

u∈V (H)

v∈V (H)

αv αH |βuv|.

![image 15](<2010-borgs-left-right-convergence-graphs_images/imageFile15.png>)

- Lemma 2.3 Let G be a simple graph, and let H be a weighted graph. Let φ be a random map G → H. Then


Eφ|tree(Gφ)| ≤ tree(G)c(H)|G|−1. Proof. We may assume the edgeweights in H are nonnegative. We have Eφ(tree(Gφ)) = Eφ

βφ(i)φ(j) (10)

βφ(i)φ(j) =

Eφ

ij∈E(T)

T∈SpTr(G)

T∈SpTr(G) ij∈E(T)

Fix the tree T, and let p be one of its endpoints, with single neighbor q. Then picking the random map ψ of V (G) \ {p} ﬁrst and the the image u of p last, we get

βφ(i)φ(j)Eu(βψ(q)u)

βφ(i)φ(j) = Eψ

Eφ

ij∈E(T−p)

ij∈E(T)

αu αH

βφ(i)φ(j)

= Eψ

βψ(q)u

![image 16](<2010-borgs-left-right-convergence-graphs_images/imageFile16.png>)

u

ij∈E(T−p)

≤ Eψ

βφ(i)φ(j)c(H) = c(H)Eψ

ij∈E(T−p)

βφ(i)φ(j) ,

ij∈E(T−p)

whence by induction

Eφ

βφ(i)φ(j) ≤ c(H)|T|−1.

ij∈E(T)

By (10), the Lemma follows.

- Lemma 2.4 Let G be a simple graph, and let H be a weighted graph with edge weights in [0,1]. Then


|z(G,H)| ≤ tree(G)c(H)|G|−1.

Proof. Let φ be a random map G → T. Then by (9) and Lemmas 2.2 and 2.3,

|z(G,H)| ≤ Eφ|cr(Gφ)| ≤ Eφtree(Gφ) ≤ tree(G)c(H)|G|−1.

# 3 Left-convergence implies right-convergence

Our ﬁrst main theorem is the following.

- Theorem 3.1 Let (Gn) be a left-convergent sequence of graphs with maximum degree at most D. Let H be a weighted graph with 0 ≤ βij ≤ 1 and c(H) < 1/(2D). Then ln t(Gn,H)/|Gn| is convergent as n → ∞.


![image 17](<2010-borgs-left-right-convergence-graphs_images/imageFile17.png>)

![image 18](<2010-borgs-left-right-convergence-graphs_images/imageFile18.png>)

Recall that the condition on c(H) means that

- 1

![image 19](<2010-borgs-left-right-convergence-graphs_images/imageFile19.png>)

- 2D


αk αH

(1 − βik) <

![image 20](<2010-borgs-left-right-convergence-graphs_images/imageFile20.png>)

k∈V (H)

(11)

for all i ∈ V (H). It is clear that we may assume that αH = 1.

We give two proofs of this Theorem: one, using the Dobrushin Uniqueness Theorem, and another one using cluster expansion techniques. In fact, the second proves a weaker result only, where in (11), the 2D in the denominator is replaced by the stronger condition 8D. The reason for giving it at all is that (a) it uses a completely diﬀerent technique, (b) it gives approximation formulas for lnt(G,H)/|G| with explicit error bounds, and (c) the method can also be used to prove the converse of the theorem (see Theorem 4.3).

- 3.1 Proof via Dobrushin Uniqueness We brieﬂy recall two basic notions (see e.g. [12] for a more informative discussion):


- (i) A coupling of probability distributions µ and ν is a random pair (X,Y ) deﬁned on some probability space such that the marginal distribution of X is µ and that of Y is ν. A coupling of (not necessarily real-valued) random variables φ,ψ is a random pair (X,Y ) such that the laws of X and Y are those of φ and ψ (respectively).


- (ii) The total variation distance between discrete probability distributions µ and ν on Ω is


= 21 ω∈Ω |µ(ω) − ν(ω)|; it is equal to the minimum over couplings (X,Y ) of µ and ν of Pr(X = Y ). The total variation distance of a pair of random variables φ,ψ is the total variation distance of their distributions.

ν − µ

![image 21](<2010-borgs-left-right-convergence-graphs_images/imageFile21.png>)

TV

For the rest of this section we ﬁx H as in Theorem 3.1, and set t(G,H) = hom(G,H) = t(G). For any G and φ : V (G) → V (H), set

βφ(u),φ(v).

αφ(u)

W(φ) =

uv∈E(G)

u∈V (G)

The natural associated probability measure on V (H)V (G) is given by PrG(φ) ∝ W(φ) (that is, PrG(φ) = W(φ)/t(G)). We write EG for expectation with respect to this measure.

Given Λ ⊆ V (G) and α : V (G) \ Λ → V (H), let φα : V (G) → V (H) be chosen according to Pr(φα = τ) = PrG(φ = τ|φ ≡ α oﬀ Λ) ∀τ : V (G) → V (H). For ζ = (ζ1,...,ζs) with ζi ∈ V (H), deﬁne the probability distribution νζ on V (H) by νζ(i) ∝ αi

s

.

βi,ζ

j

j=1

(Thus νζ is the conditional distribution of φ(v) given that d(v) = s and the φ-values of the neighbors of v are ζ1,...,ζs.) The following version of Dobrushin Uniqueness is convenient for our purposes, but see e.g. [10] for a more usual statement.

- Theorem 3.2 Let G be a graph with maximum degree at most D, and let H be a weighted graph such that with notation as above, there is a 0 < κ < 1 such that for any s ≤ D and ζ = (ζ1,...,ζs) and ζ′ = (ζ1,...,ζs−1,ζs′) with ζ1,...,ζs,ζs′ ∈ V (H), we have


κ D

TV ≤

νζ − νζ′

. (12)

![image 22](<2010-borgs-left-right-convergence-graphs_images/imageFile22.png>)

Let Λ ⊆ V (G), Λ′ = V (G) \ Λ and α,β : Λ′ → V (H). Then there is a coupling (φ˜α,φ˜β) of φα and φβ such that

′) ∀x ∈ V (G). In particular, for any Ω ⊆ Λ the total variation distance of the restrictions of φα and φβ to Ω is ′). To apply this theorem, we need a couple of simple facts.

Pr(φ˜α = φ˜β) ≤ κd(x,Λ

- at most x∈Ω κd(x,Λ


- Proposition 3.3 Let γi ≥ µi,νi ≥ 0 for i = 1,...,n, γ = γi, µ = µi, ν = νi and ξ ≥ 0 and suppose (γ ≥) ν,µ ≥ γ − ξ. Then


n

µi µ −

νi ν ≤

2ξ γ − ξ

;

![image 23](<2010-borgs-left-right-convergence-graphs_images/imageFile23.png>)

![image 24](<2010-borgs-left-right-convergence-graphs_images/imageFile24.png>)

![image 25](<2010-borgs-left-right-convergence-graphs_images/imageFile25.png>)

i=1

that is, the total variation distance of the distributions {µi/µ}i∈[n] and {νi/ν}i∈[n] is at most ξ/(γ − ξ).

Proof. Assuming (w.l.o.g.) that ν ≥ µ, we have (with sums over i ∈ [n]),

µi µ −

νi ν ≤ µi

1 ν

1 ν |µi − νi|

1 µ −

+

![image 26](<2010-borgs-left-right-convergence-graphs_images/imageFile26.png>)

![image 27](<2010-borgs-left-right-convergence-graphs_images/imageFile27.png>)

![image 28](<2010-borgs-left-right-convergence-graphs_images/imageFile28.png>)

![image 29](<2010-borgs-left-right-convergence-graphs_images/imageFile29.png>)

![image 30](<2010-borgs-left-right-convergence-graphs_images/imageFile30.png>)

ν − µ ν

1 ν

((γi − µi) + (γi − νi))

≤

+

![image 31](<2010-borgs-left-right-convergence-graphs_images/imageFile31.png>)

![image 32](<2010-borgs-left-right-convergence-graphs_images/imageFile32.png>)

γ − µ ν ≤ 2

ξ γ − ξ

= 2

.

![image 33](<2010-borgs-left-right-convergence-graphs_images/imageFile33.png>)

![image 34](<2010-borgs-left-right-convergence-graphs_images/imageFile34.png>)

![image 35](<2010-borgs-left-right-convergence-graphs_images/imageFile35.png>)

- Proposition 3.4 The conditions on H in Theorem 3.1 imply that (12) holds with κ = 2Dc(H).


Proof. Suppose H is as in Theorem 3.1 and let ζ,ζ′ be as in Theorem 3.2. For i ∈ V (H), let γi = αi j s=1−1 βi,ζ

, and set γ = γi. Then µi,νi ≤ γi and (using the inequality ηi ≥ 1 − (1 − ηi) for ηi ∈ [0,1]) we have

and νi = γiβi,ζ′

, µi = γiβi,ζ

s

j

s

s−1

s−1

![image 36](<2010-borgs-left-right-convergence-graphs_images/imageFile36.png>)

) ≥ 1 − (D − 1)c(H), (13)

αi(1 − βi,ζ

)] = 1 −

(1 − βi,ζ

αi[1 −

γi ≥

j

j

j=1 i

j=1

i

i

and

i

µi =

i

)] ≥ γ −

γi[1 − (1 − βi,ζ

s

i

![image 37](<2010-borgs-left-right-convergence-graphs_images/imageFile37.png>)

) ≥ γ − c(H), (14)

αi(1 − βi,ζ

s

![image 38](<2010-borgs-left-right-convergence-graphs_images/imageFile38.png>)

and similarly νi ≥ γ − c(H); so Proposition 3.3 shows that (12) holds as claimed.

Proof of Theorem 3.1. Our approach here via (15) is similar to that of [1], which in turn was inspired by the “cavity” method of statistical physics; see e.g. [17].

Given an ordering v1,...,vn (with n = |G|) of V (G), set Gk = G − {v1,...,vk}. We have

W(φ)

t(Gk) =

φ:V (Gk)→H

and may write

t(Gk−1) =

φ:V (Gk)→H

Thus

t(Gk−1) t(Gk)

= EG

![image 39](<2010-borgs-left-right-convergence-graphs_images/imageFile39.png>)

k

i∈V (H)

and

n

lnt(G) =

lnEG

k

k=1

αi

W(φ)

i∈V (H)

βi,φ(w).

w∈NGk−1(vk)

βi,φ(w),

αi

w∈NGk−1(vk)

βi,φ(w). (15)

αi

w∈NGk−1(vk)

i∈V (H)

We will use Theorem 3.2 to say that for large r the expectation in (15) is nearly determined by the r-neighborhood of vk in Gk−1. To say this properly set, for a graph K and v ∈ V (K),

αi

ΨK(v) = EK−v

i∈V (H)

βi,φ(w). (16)

w∈NK(v)

We note right away that

- 1

![image 40](<2010-borgs-left-right-convergence-graphs_images/imageFile40.png>)

- 2


αi

<

i∈V (H)

βi,φ(w) ≤ 1, and so

w∈NK(v)

- 1

![image 41](<2010-borgs-left-right-convergence-graphs_images/imageFile41.png>)

- 2


< ΨK(v) ≤ 1. (17)

The upper bound is trivial, while the lower bound follows from a computation similar to (13):

αi

i∈V (H)

βi,φ(w) ≥

w∈NK(v)

= 1 −

(1 − βi,φ(w))

αi 1 −

w∈NK(v)

i∈V (H)

- 1

![image 42](<2010-borgs-left-right-convergence-graphs_images/imageFile42.png>)

- 2


![image 43](<2010-borgs-left-right-convergence-graphs_images/imageFile43.png>)

αi(1 − βi,φ(w)) ≥ 1 − Dc(H) >

.

w∈NK(v) i∈V (H)

The assertion is then that for K of maximum degree at most D, ΨK(v) is determined to within or(1) by (the isomorphism type of) BK(v,r) (where or(1) → 0 as r → ∞); that is:

- Lemma 3.5 For any K,K′ of maximum degree at most D, v ∈ V (K) and v′ ∈ V (K′) with BK′(v′,r) ∼= BK(v,r), we have


- (a) |ΨK(v) − ΨK′(v′)| < Dκr,
- (b) |lnΨK(v) − lnΨK′(v′)| < 2Dκr.


Proof. (a) The sum in (16) is a function of the multiset M(v,φ) = {φ(w) : w ∈ NK(v)}. By Theorem 3.2 there is a coupling (φ,˜ φ˜′) of φ and φ′ chosen according to PrK−v and PrK′−v′ so that Pr(M(v,φ˜) = M(v′,φ˜′)) ≤ |NK(v)|κr. With this coupling, using the upper bound in (17),

|ΨK(v) − ΨK′(v′)| ≤ Pr(M(v,φ˜) = M(v′,φ˜′)) ≤ Dκr.

(b) This is implied by (a) once we observe that ΨK(v) is bounded below by (17).

Returning to the proof of Theorem 3.1, it’s convenient to speak of an ordering σ of V (G), thought of as a bijection from V (G) to [n] (again with n = |V (G)|). For such a σ and v ∈ V (G), set G(v,σ) = G[{w ∈ V (G) : σ(w) ≥ σ(v)}]. Then with σ a random (uniform) permutation of V (G), (15) gives

lnt(G) =

Eσ lnΨG(v,σ)(v). (18)

v∈V (G)

By Lemma 3.5 the contribution of v to (18) is determined up to or(1) by BG(v,r). Precisely, let U = BG(v,r) and Uσ = BG(v,σ)(v,r), then

Eσ lnΨG(v,σ)(v) = XU + R, (19)

(v) depends on the ball U = BG(v,r) only, and |R| < 2Dκr. By (17), we have |XU| < 1.

where XU = Eσ lnΨU

σ

Thus |G|−1 lnt(G) = µ(G,U)XU + or(1) (with the sum over r-balls U) and |Gm|−1 lnt(Gm) − |Gn|−1 lnt(Gn) < |µ(Gm,U) − µ(Gn,U)| + or(1). (20)

Finally, the right hand side of (20) can be made as small as desired by choosing a suﬃciently large r and then m,n large enough to make the sum small.

- Remark 1 Of course the condition on H in Theorem 3.1 can be replaced by any assumption

that supports the conclusions of Lemma 3.5 (with some or(1) in place of the explicit bounds given there). One notable example involves the hard-core model, in which V (H) = {0,1} and the weights are α0 = 1/(1+λ), α1 = λ/(1+λ), β0,1 = β0,0 = 1 and β1,1 = 0. Here the present results combined with [25] give the convergence in Theorem 3.1 provided λ ≤ (D − 1)D−1/(D − 2)D ≈ e/D (whereas Theorem 3.2 gives this for λ < 1/D).

Another very interesting example is that of counting q-colorings; thus H is the complete graph on [q] (without weights, though to put it in the above framework we should replace αi = 1 by αi = 1/q ∀i). Here Theorem 3.2 gives convergence for q > 2D, but it seems reasonable to expect that q ≥ D + 1 suﬃces. That this is at least true for large girth (that is, if we add the requirement that the girth of Gn tends to inﬁnity), follows from the present arguments with

- Theorem 3.2 replaced by a result of Jonasson [11] which says (informally) that for a uniform q-coloring of an r-branching tree with q ≥ r+2, the color of the root becomes nearly independent of the colors of the leaves as the depth of the tree grows. (We actually need this for trees in which each internal node has at most r children, but this version is easily seen to follow from the original.)


If we assume, in addition to large girth, that the Gn are D-regular, then we have (again for q ≥ D + 1) the explicit limit

lnhom(Gn,H) |Gn|

![image 44](<2010-borgs-left-right-convergence-graphs_images/imageFile44.png>)

→ lnq +

D 2

![image 45](<2010-borgs-left-right-convergence-graphs_images/imageFile45.png>)

ln(1 −

1 q

![image 46](<2010-borgs-left-right-convergence-graphs_images/imageFile46.png>)

). (21)

This is one of the main results of [1], obtained there by combining the cavity method with a “rewiring” device (another idea from statistical physics [17]), used to maintain regularity. Here we have the result more easily: it follows from the observation that Johansson’s theorem (which is also needed in [1]) implies that the expectations in (18) tend to (D/2)ln(1 − 1/q) as the girth grows; namely, it implies that for each i ∈ [q] the events {σ(w) > σ(v) and φ(w) = i} (w ∈ N(v)) are, for large girth, nearly independent, each with probability about 1/q. (The key diﬀerence between the present argument and that of [1] is the use of the random ordering σ.)

- Remark 2 An argument similar to the one above gives (for a left-convergent sequence {Gn})


convergence of {|Gn|−1H(φG

: V (Gn) → H is chosen according to PrG

)}, where H is (say binary) entropy and φG

n

n

. Here we should replace (15) by the “chain rule” expansion H(φ) = v H(φ(v)|(φ(w) : σ(w) > σ(v))). Getting to the analogue of (19) now requires an extra step:

n

we should choose r1 so that for any σ the law of φ(v) given (φ(w) : σ(w) > σ(v)) is “nearly

determined” by (φ(w) : σ(w) > σ(v),w ∈ B(v,r1)), and then r (> r1) so that the law of the latter vector is nearly unaﬀected by the values taken by φ outside B(v,r).

- 3.2 Proof via Mayer expansion


Our second proof relies on techniques which are well know in the mathematical statistical physics literature. To apply these techniques, we express t(G,H) as the partition function of a so called abstract polymer system, express its logarithm in terms of an inﬁnite series whose terms can be written down explicitly, and ﬁnally prove that for c(H) < 1/(8D), the series for |G1| lnt(G,H) is absolutely convergent uniformly in |G|. This will allow us to take the limit in Theorem 3.1 term by term.

![image 47](<2010-borgs-left-right-convergence-graphs_images/imageFile47.png>)

![image 48](<2010-borgs-left-right-convergence-graphs_images/imageFile48.png>)

- 3.2.1 Stable sets, Mayer expansion, and Dobrushin’s lemma


We start with some preliminaries from mathematical physics, reformulated here in a more combinatorial language. Let G be a graph and let I(G) denote the set of stable (independent) subsets of V (G). We assign a variable xi to each node i, and deﬁne the multivariate stable set polynomial as

stab(G,x) =

xi.

S∈I(G) i∈S

Note that stab(G,1,...,1) = hom(G,H), where H is the graph on two adjacent nodes, with a loop at one of them (all weights being 1).

In the language of mathematical physics, the pair (G,x) is called an abstract polymer system, and stab(G,x) is called the partition function of the abstract polymer system (G,x) (see, e.g., [20], where the notion of an abstract polymer system was ﬁrst introduced). Here we will be interested in the Taylor expansion of lnstab(G,x) about x = (0,...,0), known under the name of Mayer expansion in statistical physics. In a slightly less general context than the one considered here, this expansion was ﬁrst derived in Malyshev [16], who in turn relied heavily on the work of Rota [18]. In the general context of an abstract polymer system, it goes back to [20].

For a sequence v ∈ V m of nodes of a simple graph G, let G[v] denote the graph on [m] in which i and j are adjacent if and only if vi and vj are equal or adjacent in G. (Note that v may contain repetitions.) The following lemma is a reformulation of a result of Seiler [20].

- Lemma 3.6 Let G = (V,E) be a simple graph. For every x ∈ RV such that the series below is absolutely convergent, we have


∞

1 m! v∈V

lnstab(G,x) =

![image 49](<2010-borgs-left-right-convergence-graphs_images/imageFile49.png>)

m=1

m

m

cr(G[v])

i=1

, (22)

xv

i

To prove absolute convergence of the expansion in (22), we use the following lemma which goes back to Dobrushin. In the form stated here, it can be found, e.g., in [4].

- Lemma 3.7 Let G = (V,E) be a simple graph, and let x ∈ RV and b ∈ [0,∞)V be such

j∈V ij∈E or j=i

ln 1 + |xj|eb

j

≤ bi. (23)

for all i ∈ V . Then the series in (22) is absolutely convergent, and

lnstab(G,x) ≤

i∈V

ln(1 + |xi|eb

i

). (24)

- 3.2.2 Mayer expansion for lnt(G,H)


We can rewrite hom(G,H) in terms of the intersection graph G = L(CInd(G)) of connected induced subgraphs.

- Lemma 3.8 For every simple graph G and weighted graph H, deﬁne a vector z ∈ RCInd(G) by zF = z(F,H). Then t(G,H) = stab(G,z).


![image 50](<2010-borgs-left-right-convergence-graphs_images/imageFile50.png>)

Proof. By easy computation,

t(G,H) =

E′⊆E

′|t(G′,H), (25)

(−1)|E

![image 51](<2010-borgs-left-right-convergence-graphs_images/imageFile51.png>)

where G′ = (V (G),E′). Using that t(G′,H) is multiplicative over the components of G′ and that singleton components give a factor of 1, we get

![image 52](<2010-borgs-left-right-convergence-graphs_images/imageFile52.png>)

t(G,H) =

E′⊆E F

(−1)|E(F)|t(F,H), (26)

![image 53](<2010-borgs-left-right-convergence-graphs_images/imageFile53.png>)

where the product extends over all non-singleton components of G′. Collecting terms that induce the same partition, we get

(−1)|E(F)|t(F,H)

![image 54](<2010-borgs-left-right-convergence-graphs_images/imageFile54.png>)

t(G,H) =

P∈Π(V ) Y ∈P F∈CSpan(G[Y ])

![image 55](<2010-borgs-left-right-convergence-graphs_images/imageFile55.png>)

z(G[Y ],H) = stab(G,z).

=

P∈Π(V ) Y ∈P

For any multiset {F1,...,Fk} of subgraphs, let L(F1,...,Fk) denote the intersection graph of V (F1),...,V (Fk). Combining Lemma 3.8 and Lemma 3.6, we get the following formula.

Corollary 3.9 Let G be a simple graph and H, a weighted graph. If the series below is absolute convergent, we have

∞

lnt(G,H) =

m=1

m

1 m!

cr(L(F1,...,Fm))

![image 56](<2010-borgs-left-right-convergence-graphs_images/imageFile56.png>)

j=1

F1,...,Fm∈CInd(G)

![image 57](<2010-borgs-left-right-convergence-graphs_images/imageFile57.png>)

z(Fj,H). (27)

Next we establish the convergence condition (23) for b of the form bF = b|F|. For vectors b of this form, it is clearly enough to prove that for all i ∈ V , we have

ln 1 + |zF|eb|F| ≤ b. (28)

F∈CInd(G): i∈V (F )

We in fact prove a stronger inequality. To state our result, we deﬁne

b + eb ln(1 + be−b)

, ǫ = − ln(DKc(H)) and z˜F = eǫ(|F|−1)zF. (29)

![image 58](<2010-borgs-left-right-convergence-graphs_images/imageFile58.png>)

K =

![image 59](<2010-borgs-left-right-convergence-graphs_images/imageFile59.png>)

We will assume that c(H) < 1/(DK), so that ε > 0.

In the special case of colorings, i.e., the case where H is the complete graph without loops, the next lemma was already shown in [4].

- Lemma 3.10 For every simple graph G with maximum degree D, every weighted graph H with edge weights in [0,1], and every node i ∈ V (G), we have


|z˜F|eb|F| ≤ b. (30)

F∈CInd(G) V (F)∋i

- Remark 3 The lemma clearly implies condition (28). In fact, (28) holds even if z is replaced by z˜.


Proof. Using the bound in Lemma 2.4, it is enough to show that

tree(G[W])λ|W|−1 ≤ be−b. (31)

W ⊆V : i∈W, |W |≥2

where λ = eb/(KD). Consider a tree T contributing to tree(G[W]). After removing the point i from T, the tree T decomposes into a certain number of connected components T1,...,Tk, with vertex sets U1,...,Uk. Note that Π{U1,...,Uk} is a partition of W \ {i} into disjoint subsets. Classifying the spanning trees of G[W] according to these partitions, one easily obtains the identity

  , (32)

  tree(G[U])

tree(G[W]) =

1

Π U∈Π

j∈U ij∈E

where the sum runs over partitions of W \{i} into disjoint subsets. With the help of this identity, one easily bounds the left hand side of (31) by induction on the number of vertices in V . Indeed,

we ﬁrst rewrite the left hand side as

tree(G[W])λ|W|−1

W⊆V : i∈W, |W|≥2

  tree(G[Us])λ|U

  

D

k

1 k!

s|

=

1

![image 60](<2010-borgs-left-right-convergence-graphs_images/imageFile60.png>)

s=1

j∈Us ij∈E

k=1

W⊆V : i∈W, |W|≥2

U1,...,Uk⊆W\{i} W\{i}= s Us Us∩Ur=∅ for s =r

  

  tree(G[Us])λ|U

k

D

1 k!

s|

1

=

![image 61](<2010-borgs-left-right-convergence-graphs_images/imageFile61.png>)

s=1

j∈Us ij∈E

k=1

U1,...,Uk⊆V \{i} Us∩Ur=∅ for s =r

D

k

1 k!

tree(G[Us])λ|U

s|.

=

![image 62](<2010-borgs-left-right-convergence-graphs_images/imageFile62.png>)

s=1

k=1

j1,...,jk∈N(i) jr =js for s =r

U1,...,Uk⊆V \{i}

Us∩Ur=∅ for s =r js∈Us for all s

(33)

Rewriting the ﬁrst two sums as a sum over subsets of N(i) and neglecting the non-overlap constraints on the sets Us, we obtain the bound

  

  

tree(G[W])λ|W|−1 ≤

tree(G[Uj])λ|U

j|

R⊆N(i) j∈R

W⊆V : i∈W, |W|≥2

Uj⊆V \{i} Uj∋j





tree(G[Uj])λ|U

j|−1

=

λ + λ

 

 

R⊆N(i) j∈R

Uj⊆V \{i} Uj ∋j |Uj|≥2

λ + λbe−b = 1 + λ(1 + be−b) |N(i)| − 1

≤

R⊆N(i) j∈R

−b) − 1 = be−b.

≤ eDλ(1+be

(34)

The above lemma gives a bound on the tails

∞

Ak =

m=1

1 m!

|cr(L(F1,...,Fm))|

![image 63](<2010-borgs-left-right-convergence-graphs_images/imageFile63.png>)

j=1

F1,...,Fm∈CInd(G) (|Fi|−1)≥k

of the expansion (27):

m

![image 64](<2010-borgs-left-right-convergence-graphs_images/imageFile64.png>)

|z(Fj,H)|

- Lemma 3.11 Let b > 0, let G be a graph with maximum degree D, and let H be a weighted graph with edgeweights in [0,1]. Then for every k ≥ 2,


Ak ≤ be−εk|G|.

Proof. Bounding Ak by

∞

Ak ≤ e−εk

m=1

m

1 m!

j|,

|z˜F

|cr(L(F1,...,Fm))|

![image 65](<2010-borgs-left-right-convergence-graphs_images/imageFile65.png>)

j=1

F1,...,Fm∈CInd(G) (|Fi|−1)≥k

we can ignore the condition on (|Fi| − 1) to get

∞

m

1 m!

Ak ≤ e−εk

|cr(L(F1,...,Fm))|

![image 66](<2010-borgs-left-right-convergence-graphs_images/imageFile66.png>)

m=1

j=1

F1,...,Fm∈CInd(G)

j| = e−εk lnstab(G,zˆ),

|z˜F

where ˆz denotes the vector (−|z˜F| : F ∈ CInd(G)). We use Theorem 3.7 and Lemma 3.10 to obtain the estimate

ln 1 + |z˜F|eb|F| ≤ e−εk

ln 1 + |z˜F|eb|F|

|Ak| ≤ e−εk

i∈V F∈CInd(G)

F∈CInd(G)

V (F)∋i

≤ e−εk

|z˜F|eb|F| ≤ e−εk|G|b.

i∈V F∈CInd(G)

V (F )∋i

- 3.2.3 Proof of Theorem 3.1


We group the terms in Corollary 3.9 according to the subgraph of G induced by the union of the Fi. More precisely, for every graph F, deﬁne

∞

v(F,H) =

m=1

1 m!

cr(L(F1,...,Fm))

![image 67](<2010-borgs-left-right-convergence-graphs_images/imageFile67.png>)

i=1

F1,...,Fm∈CInd(F ) ∪iV (Fi)=V (F)

m

![image 68](<2010-borgs-left-right-convergence-graphs_images/imageFile68.png>)

z(Fi,H). (35)

We note that v(H,F) = 0 if F is disconnected, since then cr(L(F1,...,Fm)) = 0. With this notation, we can also write (27) as

v(F,H) =

lnt(G,H) =

F∈CInd(G)

F

ind0(F,G)v(F,H), (36)

where the last summation is extended over all isomorphism types of connected graphs F (clearly, graphs F with more than |G| nodes contribute 0).

Hence

lnt(Gn,H) |Gn|

ind0(F,Gn) |Gn|

=

v(F,H). (37)

![image 69](<2010-borgs-left-right-convergence-graphs_images/imageFile69.png>)

![image 70](<2010-borgs-left-right-convergence-graphs_images/imageFile70.png>)

F

Here ind0(F,Gn)/|Gn| tends to some value as n → ∞ by left-convergence of the sequence (Gn). Hence

lnt(Gn,H) |Gn|

ind0(F,Gn) |Gn|

lnt(Gm,H) |Gm|

ind0(F,Gm) |Gm|

−

−

≤

|v(F,H)|

![image 71](<2010-borgs-left-right-convergence-graphs_images/imageFile71.png>)

![image 72](<2010-borgs-left-right-convergence-graphs_images/imageFile72.png>)

![image 73](<2010-borgs-left-right-convergence-graphs_images/imageFile73.png>)

![image 74](<2010-borgs-left-right-convergence-graphs_images/imageFile74.png>)

|F|≤k

ind0(F,Gm) |Gm|

ind0(F,Gn) |Gn|

|v(F,H)|

+

+

![image 75](<2010-borgs-left-right-convergence-graphs_images/imageFile75.png>)

![image 76](<2010-borgs-left-right-convergence-graphs_images/imageFile76.png>)

|F|>k

ind0(F,Gn) |Gn|

ind0(F,Gm) |Gm|

−

≤

|v(F,H)| + 2Ak.

![image 77](<2010-borgs-left-right-convergence-graphs_images/imageFile77.png>)

![image 78](<2010-borgs-left-right-convergence-graphs_images/imageFile78.png>)

|F|≤k

We can choose k large enough so that the last term is less than ε/2, and then the ﬁrst term will be less than ε/2 if n and m are large enough.

This proves the theorem for c(H¯) < KD1 . We choose b so as to minimize K. For b = 2/5 we get K = 7.964 ··· < 8 (which is not far from the best we get by this method).

![image 79](<2010-borgs-left-right-convergence-graphs_images/imageFile79.png>)

# 4 Right convergence implies left convergence

- 4.1 Linear independence of homomorphism functions The following lemmas extend some of the lemmas in [9].


- Lemma 4.1 Let F1,...,Fk be non-isomorphic simple graphs. Then the matrices

Minj = inj(Fi,Fj)

k i,j=1

and

Msurj = surj(Fi,Fj)

k i,j=1

are nonsingular.

Proof. We may assume that the Fi are ordered so that for i < j, |Fi| ≤ |Fj| and |E(Fi)| ≤ |E(Fj)|. Then the matrix Minj is upper triangular and Msurj is lower triangular. Since both matrices have positive diagonal entries, they are nonsingular.

- Lemma 4.2 Let m ≥ 1 and let {F1,...,Fk} be a ﬁnite family of non-isomorphic simple graphs closed under surjective homomorphic image. Then the matrix


k i,j=1

Mhom = hom(Fi,Fj)

is nonsingular.

Examples of such families are all simple graphs with at most q nodes, or all connected simple graphs with at most q nodes, or with at most m edges. We don’t know if this proposition holds for more general (perhaps all?) families of graphs.

Proof. We can express homomorphisms by surjective and injective homomorphisms as follows:

hom(Fi,Fj) =

J

surj(Fi,J)inj(J,Fj) aut(J)

,

![image 80](<2010-borgs-left-right-convergence-graphs_images/imageFile80.png>)

where the summation extends over all simple graphs J for which surj(Fi,J) > 0. All such graphs J belong to the family {F1,...,Fk}, which implies that if Minj and Msurj are as in Lemma 4.1, and Daut is the k × k diagonal matrix with the values aut(Fi) in the diagonal, then

Mhom = MsurjDaut−1Minj , proving by Lemma 4.1 that Mhom is nonsingular.

4.2 Convergence of graph sequences

- Theorem 4.3 Let (G1,G2,...) be a sequence of simple graphs with degrees bounded by D, and assume that there is a δ > 0 such that for every simple looped graph H with all degrees at least (1 − δ)|H|, the sequence lnhom(Gn,H)/|Gn| is convergent as n → ∞. Then the sequence (G1,G2,...) is left-convergent.


Proof. Let m ≥ 1 and let Fm = {F1,...,FN} be the set of all connected simple graphs with 2 ≤ |Fi| ≤ m. By Lemma 4.2, the matrix

N i,j=1

M = hom(Fi,Fj)

is nonsingular.

Let q > m. Add q −|Fi| isolated nodes to Fi and take the complement to get a simple graph Hi on [q] with loops added at the nodes. We think of Hi as a weighted graph with all weights 1. Every node in Hi has degree at least q − m, so if we choose q large enough, the condition on H in the theorem is satisﬁed by every Hi.

Consider any graph G with all degrees at most D. We can rewrite (27) as follows: lnt(G,Hi) =

inj0(F,G)u(F,Hi), (38)

F

where the summation extends over all connected graphs F, and

∞

u(F,Hi) =

k=1

Here

1 k!

cr(L(J1,...,Jk))

![image 81](<2010-borgs-left-right-convergence-graphs_images/imageFile81.png>)

r=1

J1,...,Jk∈Con(F ) ∪Ji=F

k

t(Jr,Hi−1). (39)

r)|hom(Jr,Fi), and so

t(Jr,Hi−1) = q−|J

r|(−1)|E(J

k

k

t(Jr,Hi−1) = (−1) r |E(Jr)|q− r |Jr|

r=1

r=1

hom(Jr,Fi).

Note that the exponent of q is less than −|F| except for k = 1 (when J1 = F). Hence u(Fj,Hi) = q−|F

j)|(hom(Fj,Fi) + O(q−1)), (40) for all 1 ≤ i,j ≤ N and

j|(−1)|E(F

u(F,Hi) = O(q−|F|−1) (41)

if |F| > m. Here and in what follows, the constants implied in the O may depend on D and m (and so also on N), but not on q, G and ε.

By Lemma 4.2 it follows that if q is large enough, then the matrix (u(Fi,Hj))Ni,j=1 is invertible. Furthermore, if (wij)ni,j=1 denotes its inverse, then

wij = q|F

j|(−1)|E(F

j)|(M−1)ij + O(q|F

j|−1),

and so

j|) = O(qm). (42) Write

|wij| = O(q|F

lnt(G,Hj) =

N

inj0(Fi,G)u(Fi,Hj) + R(G,Hj), (43)

i=1

where

R(G,Hj) =

inj0(F,G)u(F,Hj) (44)

|F|>m

is a remainder term, which we can estimate as follows, using Lemma 2.1(d):

∞

∞

inj0(F,G)O(q−r−1)

inj0(F,G)|u(F,Hj)| =

|R(G,Hj)| ≤

r=m+1 |F|=r

r=m+1 |F|=r

∞

2Dr|G|O(q−r−1) = O(q−m−2)|G|. (45)

=

r=m+1

We can view (43) as a system of N equations in the N unknowns inj0(Fi,G), from which these unknowns can be expressed:

inj0(F,G) =

N

wji lnt(G,Hj) + ri(G), (46)

j=1

where

ri(G) =

N

wjiR(G,Hj) = O(qm)O(q−m−2)|G| = O(q−2)|G|.

j=1

Now let ε > 0 be given. Choosing q large enough, we have |ri(G)| < ε|G| for all 1 ≤ i ≤ N and every graph G. By hypothesis, if q is suﬃciently large, then the sequence ln(t(Gn,Hj))/|Gn| will be convergent for every 1 ≤ j ≤ N as n → ∞, and so we can choose a positive integer n0 such that for n,n′ > n0, we have

lnt(Gn,Hj) |Gn|

![image 82](<2010-borgs-left-right-convergence-graphs_images/imageFile82.png>)

Then by (46),

lnt(Gn′,Hj) |Gn|

−

![image 83](<2010-borgs-left-right-convergence-graphs_images/imageFile83.png>)

≤ εq−m.

inj0(Fi,Gn) |Gn|

inj0(Fi,Gn′) |Gn′|

−

![image 84](<2010-borgs-left-right-convergence-graphs_images/imageFile84.png>)

![image 85](<2010-borgs-left-right-convergence-graphs_images/imageFile85.png>)

N

lnt(Gn′,Hj) |Gn′|

ri(Gn) |Gn|

lnt(Gn,Hj) |Gn|

− wji

−

+

wji

=

![image 86](<2010-borgs-left-right-convergence-graphs_images/imageFile86.png>)

![image 87](<2010-borgs-left-right-convergence-graphs_images/imageFile87.png>)

![image 88](<2010-borgs-left-right-convergence-graphs_images/imageFile88.png>)

i=1

N

lnt(Gn′,Hj) |Gn′|

lnt(Gn,Hj) |Gn|

−

|wji| ·

≤

+ O(ε)

![image 89](<2010-borgs-left-right-convergence-graphs_images/imageFile89.png>)

![image 90](<2010-borgs-left-right-convergence-graphs_images/imageFile90.png>)

i=1

≤ O(qm)εq−m + O(ε) = O(ε).

ri(Gn′) |Gn′|

![image 91](<2010-borgs-left-right-convergence-graphs_images/imageFile91.png>)

This proves that the sequence (inj0(Fi,Gn)/|Gn| : n = 1,2,...) is convergent for all Fi ∈ Fm. Since this holds for every m ≥ 1, this proves the Theorem.

In the proof above, the graphs Hi have many twin nodes (all the added nodes). We can always replace these by a single node of large weight, to get a weighted graph Hi′ on at most

- m + 1 nodes. The argument would remain essentially the same if we replaced the 0 edgeweights in Hi by 1 − δ for any ﬁxed δ > 0. Hence we get the following variant:

Theorem 4.4 Let (G1,G2,...) be a sequence of simple graphs with degrees bounded by D, and let F be a simple graph. Assume that there is a δ > 0 such that for every weighted graph H on |F| + 1 nodes with all edgeweights in [1 − δ,1], the sequence (ln t(Gn,H))/|Gn| is convergent as

- n → ∞. Then the sequence hom(F,Gn)/|Gn| is convergent.


# 5 Food for thought

We mention some directions for further research.

Quantitative bounds. It would be interesting to make the relationship between the numbers hom(F,G)/|G| and (lnt(G,H))/|G| more explicit.

Limit objects. Benjamini and Schramm [2] associated a limit object with every leftconvergent sequence of bounded degree graphs, in the form of a probability distribution (with some special properties) on countable rooted graphs with the same degree bound. Other constructions of limit objects include graphings [8] and measure preserving graphs [14]. The “left” quantities like t(F,G) can be deﬁned easily when G is replaced by such a limit object. Our Theorem 3.1 suggests that the quantities lnt(G,H)/|G| can also be extended. However, the deﬁnition (in other words, the description of the limiting value in terms of the limit object) is not clear at all.

Temperature. Most of the time we have considered weighted graphs H with αH = 1, whose edgeweights are between 0 and 1, and close to 1. Let us consider edgeweights of the form βij = exp(−Bij), where Bij ≥ 0, and normalize so that maxi,j Bij = 1. Also consider the weighted graph H1/T, where T is a parameter which in statistical physics would be called the temperature, and the edge weights are raised to the 1/T power. In this notation

hom(G,H1/T) = Eφ exp

1 T

Bφ(i)φ(j) ,

![image 92](<2010-borgs-left-right-convergence-graphs_images/imageFile92.png>)

ij∈E(G)

where φ is a random map G → H. Furthermore, c(H) = max

1 T

1 T j

![image 93](<2010-borgs-left-right-convergence-graphs_images/imageFile93.png>)

αjBij ≤

αj(1 − βij) ≤ max

.

![image 94](<2010-borgs-left-right-convergence-graphs_images/imageFile94.png>)

![image 95](<2010-borgs-left-right-convergence-graphs_images/imageFile95.png>)

i

i

j

So it follows that if the temperature T is larger than 2D then for every left-convergent graph sequence (Gn), the partition functions hom(Gn,H1/T) are convergent.

What kind of convergence does it mean if the partition functions are convergent at smaller temperature as well? This is not a local property any more; still, is it related to some property “from the left”?

Distance. One would like to deﬁne a cut-distance type metric for bounded degree graphs. Let G1 and G2 be two graphs with degrees bounded by D on the same node set V = [n]. Let ei(S,T) denote the number of edges in Gi connecting S and T (S,T ⊆ V ). Suppose that we have

|e1(S,T) − e2(S,T)| ≤ εn (47)

for all S,T ⊆ V . Then for every weighted graph H with V (H) = [q], αH = 1 and 1/B ≤ βu,v ≤ B for some B ≥ 1, we have

1(φ−1(u),φ−1(v)) uv

βe

βφ(i)φ(j) = Eφ

t(G1,H) = Eφ

u,v∈V (H)

ij∈E(G1)

uv Bεn(q

)

2(φ−1(u),φ−1(v))

βe

≤ Eφ

2

u,v∈V (H)

= Bεn(q

)t(G2,H). Hence

2

lnt(G1,H) n −

lnt(G2,H) n ≤ ε

![image 96](<2010-borgs-left-right-convergence-graphs_images/imageFile96.png>)

![image 97](<2010-borgs-left-right-convergence-graphs_images/imageFile97.png>)

q 2

lnB.

By Theorem 4.4, this implies that hom(F,G1)/|G1| and hom(F,G2)/|G2| are also close if n is large enough.

The trouble is that condition (47) is too strong: it does not hold for two random D-regular graphs, for example. Perhaps it is possible to replace it by some condition asserting that it holds “on the average”?

# References

- [1] A. Bandyopadhyay and D. Gamarnik, Counting without sampling. Asymptotics of the logpartition function for certain statistical physics models, Random Structures & Algorithms 33, 2008.
- [2] I. Benjamini and O. Schramm: Recurrence of Distributional Limits of Finite Planar Graphs, Electronic J. Probab. 6 (2001), paper no. 23, 1–13.
- [3] I. Benjamini, O. Schramm, A. Shapira: Every Minor-Closed Property of Sparse Graphs is Testable, 40th Ann. ACM Symp. on Th. Comp. (2008), 393–402.
- [4] C. Borgs: Absence of Zeros for the Chromatic Polynomial on Bounded Degree Graphs, Combinatorics, Probability and Computing 15 (2006), 63-74.
- [5] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s, and K. Vesztergombi: Convergent Graph Sequences I: Subgraph frequencies, metric properties, and testing, Advances in Math. 219


(2008), 1801–1851.

- [6] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s, and K. Vesztergombi: Convergent Graph Sequences II: Multiway Cuts and Statistical Physics (submitted), http://www.cs.elte.hu/~lovasz/ConvRight.pdf
- [7] R.L. Dobrushin: Estimates of semi-invariants for the Ising model at low temperatures. In: Topics in Statistical and Theoretical Physics, Vol. 177 of American Mathematical Society Translations, Ser. 2 (1996), 59-81.
- [8] G. Elek: On limits of ﬁnite graphs, Combinatorica 27 (2007), 503–507.
- [9] P. Erdo¨s, L. Lov´asz, J. Spencer: Strong independence of graphcopy functions, in: Graph Theory and Related Topics, Academic Press, 165–172.
- [10] H.-O. Georgii, Gibbs Measures and Phase Transitions, de Gruyter, Berlin, 1988.
- [11] J. Jonasson, Uniqueness of uniform random colorings of regular trees, Statistics and Probability Letters 57 (2002), 243-248.
- [12] D. Levin, Y. Peres and E. Wilmer, Markov Chains and Mixing Times, AMS, Providence, 2008.
- [13] L. Lov´asz: Combinatorial Problems and Exercises, North-Holland Publishing Co., Amsterdam, 1993; AMS Chelsea Publishing, 2007.
- [14] L. Lov´asz: Very large graphs, in: Current Developments in Mathematics 2008 (eds. D. Jerison, B. Mazur, T. Mrowka, W. Schmid, R. Stanley, and S. T. Yau), International Press, Somerville, MA 2009, 67–128.
- [15] R. Lyons: Asymptotic enumeration of spanning trees Combin. Prob. Comput. 14 (2005) 491–522.
- [16] Malyshev, V.A.: Uniform Cluster Estimates for Lattice Models. Commun. Math. Phys. 64

(1979) 131–157.

- [17] M. Mezard and G. Parisi, The cavity method at zero temperature, J. Statist. Phys. 111

(2003), 1-34.

- [18] G.-C. Rota: On the foundations of combinatorial theory, I Theory of M¨obius functions. Z. Wahrsch. Verw. Gebiete 2 (1964) 340-368.
- [19] A.D.Scott and A.D.Sokal: On Dependency Graphs and the Lattice Gas, Combinatorics, Probability and Computing (2006) 15, 253–279.
- [20] E. Seiler: Gauge theories as a problem of constructive ﬁeld theory and statistical mechanics. Lecture notes in physics, Springer, Berlin-Heidelberg-New York, 1982.
- [21] J.B. Shearer: On a problem of Spencer. Combinatorica 5 (1985), 241–245.


- [22] O. Schramm: Hyperﬁnite graph limits, http://arxiv.org/PS_cache/arxiv/pdf/0711/0711.3808v1.pdf
- [23] A. Sokal: Bounds on the Complex Zeros of (Di)Chromatic Polynomials and Potts-Model Partition Functions, Combin. Probab. Comput. 10 41–77.
- [24] R. Stanley: Enumerative combinatorics, Volume 2, Cambridge University Press, Cambridge, 1999.
- [25] D. Weitz, Counting independent sets up to the tree threshold, pp. 140-149 in Proc. 38th Annual ACM Symposium on Theory of Computing, ACM, New York, 2006.


# Appendix: Grids, a case study

Let Pn Pm denote the n×m grid (the Cartesian product of a path with n nodes and a path with m nodes); let Cn Pm denote the n×m cylindrical grid (the Cartesian product of a cycle with n nodes and a path with m nodes), and let Cn Cm denote the n × m toroidal grid (the Cartesian product of a cycle with n nodes and a cycle with m nodes). The sequences of n × m grids, cylindrical grids and toroidal grids (and any merging of these three) are trivially left-convergent

- if m,n → ∞. Grids are also right-convergent in a strong sense:

- Proposition 5.1 For every weighted graph H, the sequence lnhom(Pn Pm)/nm is convergent as n,m → ∞.


Proof. Let

s0 = inf n,m

lnhom(Pn Pm) nm

![image 98](<2010-borgs-left-right-convergence-graphs_images/imageFile98.png>)

.

Fix an ε > 0, and choose a,b ≥ 1 so that lnhom(Pa Pb) ab ≤ s0 + ε, and write n = au + r and m = bv + s where 0 ≤ r < a and 0 ≤ s < b. Using that trivially hom(Pn

![image 99](<2010-borgs-left-right-convergence-graphs_images/imageFile99.png>)

1+n2 Pm,H) ≤ hom(Pn

1

Pm,H)hom(Pn

2

Pm,H), (48) it follows by an argument which could be called “2-dimensional Fekete Lemma” that

lnhom(Pn Pm) nm ≤

![image 100](<2010-borgs-left-right-convergence-graphs_images/imageFile100.png>)

u lnhom(Pa Pm) + lnhom(Pr Pm) nm ≤

![image 101](<2010-borgs-left-right-convergence-graphs_images/imageFile101.png>)

uv lnhom(Pa Pb) + u lnhom(Pa Ps) + v lnhom(Pr Pb) + lnhom(Pr Ps) nm ≤ s0 + ε + O(

![image 102](<2010-borgs-left-right-convergence-graphs_images/imageFile102.png>)

1 n

![image 103](<2010-borgs-left-right-convergence-graphs_images/imageFile103.png>)

+

1 m

![image 104](<2010-borgs-left-right-convergence-graphs_images/imageFile104.png>)

)

- if n,m → ∞. The situation is more complicated with cylindrical grids:


- Proposition 5.2 (a) If n is restricted to even numbers, then for every weighted graph H, the sequence lnhom(Cn Pm)/nm is convergent as n,m → ∞.


(b) If H is connected and nonbipartite, then the sequence lnhom(Cn Pm)/nm is convergent as n,m → ∞.

Proof. (a) We may assume that the edgeweights of H are in [0,1]. Then

hom(Cn Pm) ≤ hom(Pn Pm), and hence

ln hom(Cn Pm) nm ≤ limsup

lnhom(Pn Pm) nm ≤ s0.

limsup

![image 105](<2010-borgs-left-right-convergence-graphs_images/imageFile105.png>)

![image 106](<2010-borgs-left-right-convergence-graphs_images/imageFile106.png>)

n,m→∞

n,m→∞

On the other hand, consider the subsets of nodes A1 = {(0,x) : x = 1 ...m} and A1 = {(n/2,x) : x = 1 ...m} in L′n,m. We think of L′n,m as two (n/2+1)×m grids B1 and B2, glued together along A1 and A2. For any ﬁxed map σ : A1 ∪ A2 → V (H), let Mσ denote the number of H-colorings of B1 extending σ. Then the number of H-colorings of L′n,m extending σ is Mσ2, and so

hom(Cn Pm,H) =

σ

Mσ2,

while

hom(Pn/2+1 Pm,H) =

σ

Mσ.

Thus by Cauchy-Schwartz,

2

1 |V (H)|2m σ

Mσ2 ≥

Mσ

hom(Cn Pm,H) =

![image 107](<2010-borgs-left-right-convergence-graphs_images/imageFile107.png>)

σ

1 |V (H)|2m

hom(Pn/2+1 Pm,H)2,

=

![image 108](<2010-borgs-left-right-convergence-graphs_images/imageFile108.png>)

and so

1 nm

2 lnhom(Pn/2+1 Pm,H) − 2mln|V (H)|

hom(Cn Pm,H) ≥

![image 109](<2010-borgs-left-right-convergence-graphs_images/imageFile109.png>)

lnhom(Pn/2+1 Pm,H) (n/2 + 1)m −

2 n

2 m

)

= (1 +

![image 110](<2010-borgs-left-right-convergence-graphs_images/imageFile110.png>)

![image 111](<2010-borgs-left-right-convergence-graphs_images/imageFile111.png>)

![image 112](<2010-borgs-left-right-convergence-graphs_images/imageFile112.png>)

2 m

2 n

≥ (1 +

)s0 −

.

![image 113](<2010-borgs-left-right-convergence-graphs_images/imageFile113.png>)

![image 114](<2010-borgs-left-right-convergence-graphs_images/imageFile114.png>)

This lower bound tends to s0 as n,m → ∞. (b) As before, it is trivial that

ln hom(Cn Pm) nm ≤ s0,

limsup

![image 115](<2010-borgs-left-right-convergence-graphs_images/imageFile115.png>)

n,m→∞

so our task is to estimate hom(Cn Pm) from below.

Fix any ε > 0, and then ﬁx an n0 > 0 so that if n,m ≥ n0 then lnhom(Pn Pm)/(nm) ≥ s0−ε. For a given m ≥ n0, we construct an auxiliary weighted graph G as follows. The nodes

of G are all maps V (Pm) → V (H) with positive weight, where the weight of a map φ is i∈V (Pm) αφ(i)(H) ij∈E(P

m) βφ(i)φ(j)(H). Two maps φ,ψ are connected by an edge with weight bφ,ψ = i∈V(P

m) βφ(i)ψ(i) if this weight is positive. Claim. No connected component of G is bipartite. Consider any node x of G; we want to show that there is a walk in G of odd length starting

and ending at x.

The node x is a map of Pm into H, which can also be viewed as a walk W in H with m nodes. Since H is connected and nonbipartite, we can extend W to a closed walk W′ = (v1,v2,...,vp) of odd length p (so W = (v1,...,vm)). Let Wi = (vi,vi+1,...,vi+m−1) (where the indices are taken modulo p). The Wi corresponds to a node in H and (W1,...,Wp) is a walk in H of odd length containing W. This proves the Claim.

Now observe that

hom(Pn Pm,H) = hom(Pn,G) and

hom(Cn Pm,H) = hom(Cn,G).

Since G is connected and nonbipartite, it is easy to show that lnhom(Pn Pm)/(nm) and lnhom(Cn Pm)/(nm) tend to the same value as n → ∞, and we know that this value is at least s0 − ε. So for a ﬁxed m ≥ n0, if n ≥ n0(m,ε), then lnhom(Pn Pm)/(nm) ≥ s0 − 2ε. Choose

2 lnq ε

, and let

m0 = max n0,

![image 116](<2010-borgs-left-right-convergence-graphs_images/imageFile116.png>)

s0 ε

N0 = max{

m0,n0(m0,ε)}. Assume that n,m ≥ N0. Consider the cylindrical grid Cn Pm

![image 117](<2010-borgs-left-right-convergence-graphs_images/imageFile117.png>)

. Since n ≥ n0(m0,ε), this grid has at least exp((s0 − 2ε)nm0) H-colorings. Hence there is a way to ﬁx the map on the two “boundary” cycles so that after ﬁxing it, we still have at least

0

exp((s0 − 2ε)nm0) q2n ≥ exp((s0 − 3ε)nm0)

![image 118](<2010-borgs-left-right-convergence-graphs_images/imageFile118.png>)

extensions. Let α1 and α2 denote these maps of the two boundary cycles. Now consider the cylindrical grid Cn Pm

. Map the ﬁrst, m0-th, (2m0 − 1)-st etc. n-cycles alternatingly according to α1 and α2. Then the number of ways to extend this to the layer between two such cycles is at least exp((s − 3ε)nm0), so the number of ways to extend the mapping to the whole graph is at least

0

exp (s0 − 3ε)nm0

m m0 ≥ exp (s0 − 3ε)nm0

![image 119](<2010-borgs-left-right-convergence-graphs_images/imageFile119.png>)

m m0 − 1 ≥ exp((s0 − 4ε)nm).

![image 120](<2010-borgs-left-right-convergence-graphs_images/imageFile120.png>)

Hence

lnhom(Cn Pm)/(nm) ≥ s0 − 4ε.

For toroidal grids, the situation is similar (and so are the proofs), and we only state the result:

- Proposition 5.3 (a) If n and m are restricted to even numbers, then for every weighted graph H, the sequence lnhom(Cn Cm)/(nm) is convergent as n,m → ∞.


(b) If H is connected and nonbipartite, then the sequence lnhom(Cn Cm)/(nm) is convergent as n,m → ∞.

