---
type: source
kind: paper
title: Regularity partitions and the topology of graphons
authors: László Lovász, Balázs Szegedy
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1002.4377v1
source_local: ../raw/2010-lovsz-regularity-partitions-topology-graphons.pdf
topic: general-knowledge
cites:
---

arXiv:1002.4377v1[math.CO]23Feb2010

Regularity partitions and the topology of graphons

La´szlo´ Lova´sz∗ Institute of Mathematics Eo¨tvos Lor´and University and Bal´zs Szegedy Department of Mathematics University of Toronto

October 31, 2018

# Contents

- 1 Introduction 2
- 2 Preliminaries 3
- 3 The topology of graphons 5

- 3.1 The neighborhood distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 3.2 Pure [bi]graphons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 3.3 Density functions on pure [bi]graphons . . . . . . . . . . . . . . . . . . . . . . . . 8
- 3.4 The similarity distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
- 3.5 Compact Graphons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11


- 4 Thin graphons 12

- 4.1 The main theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
- 4.2 Vapnik-Cervonenkisˇ dimension . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
- 4.3 VC-dimension and graphons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
- 4.4 Hereditary properties and thin bigraphons . . . . . . . . . . . . . . . . . . . . . . 16


- 5 Regularity partitions 18


- 5.1 Weak and strong regularity partitions . . . . . . . . . . . . . . . . . . . . . . . . 18
- 5.2 Voronoi cells and regularity partitions . . . . . . . . . . . . . . . . . . . . . . . . 20
- 5.3 Edit distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22


Abstract

We highlight a topological aspect of the graph limit theory. Graphons are limit objects for convergent sequences of dense graphs. We introduce the representation of a graphon

![image 1](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile1.png>)

∗Research supported by OTKA grant No. 67867 and ERC Advanced Research Grant No. 227701

on a unique metric space and we relate the dimension of this metric space to the size of regularity partitions. We prove that if a graphon has an excluded induced sub-bigraph then the underlying metric space is compact and has ﬁnite packing dimension. It implies in particular that such graphons have regularity partitions of polynomial size.

# 1 Introduction

One can deﬁne convergence of a growing graph sequence [4, 3, 5], and construct a limit object to such a sequence [11] in the form of a symmetric measurable function W : J × J → [0,1], where J is any probability space (one may assume here that J = [0,1] with the Lebesgue measure, but this is not always convenient). We call the pair (J,W) a graphon.

The goal of this paper is to show that one can introduce also a topology on J (in fact, a metric), and that topological properties of this space are related to combinatorial properties of the graphon (or of the graphs whose limit it represents). A related metric was introduced in [12], and the topology on J was used in [13].

The theory of graph limits is tied to the Regularity Lemma of Szemer´edi [14, 15] in several ways. In [12] it was shown that the Regularity Lemma is equivalent to the compactness of the space of graphons in an appropriate metric, and also to a “dimensionality” of particular graphons. This paper relates to the latter result.

The metric in question is simply the L1 metric on functions W(x,.), x ∈ J. This metric itself can be weird (it may not even be deﬁned on all points of J). We show in Section 3 that that every graphon is “equivalent” (technically: weakly isomorphic, see the end of Section 2) to a graphon (J,W) with special properties: J is a complete separable metric space, and the probability measure on J has full support. We call such graphons pure. We also prove that the pure version of a graphon is uniquely determined up to changing the function W on a 0-set in each row. We deﬁne another metric in which J is compact, and characterize the cases when the two deﬁne the same topology. We prove that several important functions deﬁned on J are continuous in this topology, which shows that it is indeed the “right” topology to deﬁne on J.

In Section 4 we show that topological properties of pure graphons are related to their graphtheoretic properties. Our main result states tha if we exclude any bipartite graph from the graphon, then J must be compact and ﬁnite dimensional.

In [12] it was shown that weak regularity partitions of a graphon (J,W) (which generalize weak regularity partitions of graphs in a natural way) correspond to covering J with sets of small diameter. In Section 5 we give a stronger and cleaner version of this result. Combined with the results in Section 4, we obtain the following fact: If a graph does not contain a ﬁxed bipartite graph F as an induced sub-bigraph, then it has polynomial size strong regularity partitions (in the error bound ε).

A motivation for our paper comes from extremal combinatorics. In [13] we study the structure of graphons that arise as unique solutions of extremal problems involving the densities of ﬁnitely many subgraphs (we call such graphons ﬁnitely forcible). Such graphons come up naturally in extremal graph theory. Quite interestingly, all the examples of ﬁnitely forcible graphons produced in [13] have a compact and ﬁnite dimensional underlying metric space. The question

arises wether every extremal problem (involving a ﬁnite number of subgraph densities) has a solution of this type.

Finally we mention that graph limit theory has a close connection to the theory of dynamical systems. Probability spaces with measure preserving actions can often be endowed by a natural topology in which the action is continuous. The corresponding theory is called topological dynamics. Informally speaking, we can say that the relationship between graphons and topological graphons is similar to the relationship between dynamics and topological dynamics.

# 2 Preliminaries

We make a technical but useful distinction between bipartite graphs and bigraphs. A bipartite graph is a graph (V,E) whose node set has a partition into two classes such that all edges connect nodes in diﬀerent classes. A bigraph is a triple (U1,U2,E) where U1 and U2 are ﬁnite sets and E ⊆ U1 × U2. So a bipartite graph becomes a bigraph if we ﬁx a bipartition and specify which bipartition class is ﬁrst and second. On the other hand, if F = (V,E) is a graph, then (V,V,E′) is an associated bigraph, where E′ = {(x,y) : xy ∈ E}. This bigraph is obtained from F by a standard construction of doubling the nodes.

If G = (V,E) is a graph, then an induced sub-bigraph of G is determined by two subsets S,T ⊆ V , and its edge set consists of those pairs (x,y) ∈ S × T for which xy ∈ E (so this is an induced subgraph of the bigraph associated with G).

Let Ji = (Ωi,Ai,πi) (i = 1,2) be (standard) probability spaces. A measurable function W : J1 × J2 → [0,1] is called a bigraphon. A graphon is a special bigraphon where J1 = J2 = J and W is symmetric: W(x,y) = W(y,x) for all x,y ∈ J.

For a ﬁxed probability space J, graphons can be considered as elements of the space L∞(J × J). The norm that it most important in their is study is, however, not the L∞ norm, but the cut-norm, deﬁned by

We will also use the L1 norm

W = sup

S,T⊆J

S×T

W(x,y)dxdy .

|W(x,y)|dxdy.

W 1 =

J×J

A graphon (J,W) is called a stepfunction, if there is a partition of J into a ﬁnite number of measurable sets S1,...,Sn so that W is constant on every Si × Sj. The partition classes will be called the steps of the stepfunction.

Every graph F = (V,E) can be considered as a graphon, if we consider V as a ﬁnite probability space with the uniform measure, and E, as the indicator function of adjacency. We can resolve the atoms into intervals of length 1/|V |, to get a graphon ([0,1],WF) (which is a stepfunction). More explicitly, we split [0,1] in |V | equal intervals Li, and deﬁne WF(x,y) = E(i,j) for ix ∈ Li and y ∈ Lj. This graphon is weakly isomorphic to (V,E) (see below).

In a similar way, every bigraph can be considered as a ﬁnite bigraphon, and deﬁnes a bigraphon ([0,1],[0,1],WF).

- Remark 2.1 We could consider the version of this notion where J1 = J2 but W is not necessarily symmetric. Such a structure arises as the limit object of a convergent sequence of directed graphs with no parallel edges, and therefore can be called a digraphon. We do not need them in this paper.


Every bigraphon (J1,J2,W) can be considered as a linear kernel operator L1(J1) → L∞(J2), deﬁned by

f  →

J

W(.,y)f(y)dy.

Of course, this operator reamin well-deﬁned if we increase the subscript in L1 in the domain and lower the subscript in L∞ in the range. In the case of a graphon (J,W), it is useful to consider it as an operator L2(J) → L2(J), since it is then a Hilbert-Schmidt operator, and a rich theory is applicable. In particular, we know that it has a discrete spectrum.

If (J1,J2,U) and (J2,J3,W) are two bigraphons, we can deﬁne their operator product (J1,J3,U ◦ W) by

(U ◦ W)(x,y) =

U(x,z)W(z,y)dz.

J2

(We will write dz instead of dπ2(z), where π2 is the measure on J2: integrating over J2 means that we integrate with respect to the probability measure of J2.)

The notion of the density of a graph in a graphon has been introduced in [7]. Here we need several versions, which unfortunately leads to some messy notation. For a graphon (J,W) and graph F = (V,E), we associate a variable xv ∈ J with every node v ∈ V , and deﬁne

W(xu,xv), t(F,W) =

t(F,W;x) =

uv∈E(F)

JV

t(F,W;x)dx.

We can think of t(F,W) as “counting subgraphs isomorphic to F”. We also need the induced version:

(1 − W(xu,xv))

W(xu,xv)

tind(F,W;x) =

u,v∈V uv/∈E(F )

uv∈E(F)

tind(F,W) =

tind(F,W;x)dx.

JV

For any subset S ⊆ V , we deﬁne tS(F,W;.) : JS → R by integrating only over variables corresponding to V \S: If x′ and x′′ denote the restrictions of x ∈ JV to S and V \S, respectively, then

t(F,W;x)dx′′.

tS(F,W;x′) =

JV \S

Note that t∅(F,W) = t(F,W) and tV (F,W;.) = t(F,W;.).

These quantities have obvious analogues for bigraphs and bigraphons. For a bigraphon (J1,J2,W) and bipartite graph (U1,U2,E), we introduce variables xu ∈ J1 (u ∈ U1) and yv ∈ J2

(v ∈ U2), and deﬁne

W(xu,yv), tb(F,W) =

tb(F,W;x,y) =

uv∈E(F)

J1U1 J2U2

tb(F,W;x,y)dy dx.

Again, we deﬁne an induced version:

tbind(F,W;x,y) =

(1 − W(xi,yj))

W(xi,yj)

i∈U1,j∈U2 ij∈/E(F)

ij∈E(F)

tbind(F,W) =

tbind(F,W;x,y)dy dx.

J1U1 J2U2

1 × JS

Assume that subsets Si ⊆ Ui are speciﬁed. We deﬁne the function tb(F,W;.) : JS

2 → R by

2

1

tb(F,W;x,y)dy′′ dx′′,

1,S2(F,W;x′,y′) =

tbS

J1U1\S1 J2U2\S2

where, similarly as above, x′ and x′′ denote the restrictions of x ∈ JU

1 to S1 and U1 \ S1, respectively, and similarly for y. We can deﬁne tbind;S

1

1,S2(F,W)(x′,y′) analogously.

Two graphons (J,W) and (J′,W′) are weakly isomorphic if for every graph F, t(F,W) = t(F,W′). Various characterizations of weak isomorphism were given in [2]. Every graphon is weakly isomorphic to a graphon on [0,1] (with the Lebesgue measure), and also to a (possibly diﬀerent) graphon which is twin-free in the sense that W(x,.) and W(x′,.) diﬀer on a set of positive measure for all x = x′.

# 3 The topology of graphons

- 3.1 The neighborhood distance Let (J,W) be a graphon. We can endow the space J with a distance function by


rW(x,y) = W(x,.) − W(y,.) 1.

This function is deﬁned for almost all pairs x,y; we can delete those points from J where W(x,.) ∈/ L1(W) (a set of measure 0), to have rW deﬁned on all pairs. It is clear that rW is a pre-metric (it is symmetric and satisﬁes the triangle inequality). We call rW the neighborhood distance on W.

We also deﬁne metrics on bigraphons, endowing the spaces J1 and J2 with distance functions by

- r1(x,y) = W(x,.) − W(y,.) 1 (x,y ∈ J1),
- r2(x,y) = W(.,x) − W(.,y) 1 (x,y ∈ J2).


These functions are deﬁned for almost all pairs x,y.

- Example 1 Let Sk denote the unit sphere in Rk+1, consider the uniform probability measure on it, and let W(x,y) = 1 if x · y ≥ 0 and W(x,y) = 0 otherwise. Then (Sk,W) is a graphon, in which the neighborhood distance of two points a,b ∈ Sk is just their spherical distance (normalized by dividing by π). Furthermore, 1 − 2(W ◦ W)(x,y) is just the spherical distance of x and y, and from here is is easy to see that the similarity distance is within constant factors of the neighborhood distance.
- Example 2 Let (M,d) be a metric space, and let π be a Borel probability measure on M. Assume that the diameter of M is at most 1. Then d can be viewed as a graphon on (M,d). For x,y ∈ M, we have

rd(x,y) =

M

|d(x,z) − d(y,z)|dπ(z) ≤

M

d(x,y)dπ(z) = d(x,y),

so the identity map (M,d) → (M,rd) is contractive. This implies that if (M,d) is compact, and/or ﬁnite dimensional (in many senses of dimension), then so is (M,rd). For most ”everyday” metric spaces like (like segments, spheres, or balls) rd(x,y) can be bounded from below by Ω(d(x,y)), in which case (M,d) and (M,rd) are homeomorphic.

More generally, if F : [0,1] → [0,1] is a continuous function, then W(x,y) = F(d(x,y)) deﬁnes a graphon, and the identity map (M,d) → (M,rW ) is continuous.

- Example 3 Finitely forcible graphons, mentioned in the introduction, give interesting examples, for whose details we refer to [13]. One class is stepfuctions (equivalent to ﬁnite weighted graphs), which were proved to be ﬁnitely forcible by Lov´asz and So´s [10]; for these, the underlying metric space is ﬁnite. Other examples introduced in [13] provide as underlying topologies an interval, the Cantor set, and the one-point compactiﬁcation of N.


- 3.2 Pure [bi]graphons


A bigraphon (J1,J2,W) is pure if (Ji,ri) is a complete separable metric space and the probability measure has full support (i.e., every open set has positive measure). This deﬁnition includes that ri(x,y) is deﬁned for all x,y ∈ Ji and ri(x,y) > 0 if x = y, i.e., the bigraphon has no ”twin points”. We say that a graphon is pure, if the underlying metric probability space is complete, separable and the probability measure has full support.

Theorem 3.1 Every [bi]graphon is weakly isomorphic to a pure [bi]graphon.

- Remark 3.2 It was shown in [2] that every graphon is weakly isomorphic to a graphon on a standard probability space with no parallel points, which means that for any two points x,x′ ∈ J, W(x,.) and W(x′,.) diﬀer on a set of positive measure. Lemma 3.4 can be considered as a strengthening of this result.


Proof. We give the proof for bigraphons; the case of graphons is similar. We assume that J1 and J2 are standard probability spaces; this can be achieved similarly as for graphons. Let

- T1 be the set of functions f ∈ L1[J2] such that for every L1-neighborhood U of f, the set {x ∈ J1 : W(x,.) ∈ U} has positive measure.

- Claim 3.3 For almost every point x ∈ J1, W(x,.) ∈ T1.


Indeed, it is clear that for almost all x ∈ J1, W(x,.) ∈ L1[J2]. Every function g ∈ L1[J2]\T1 has an open neighborhood Ug in L1[J2] such that π1{x ∈ J1 : W(x,.) ∈ Ug} = 0. Let

- U = g/∈T


Ug. Since L1[J2] is separable, U equals the union of some countable subfamily {Ug

1

: i ∈ N} and thus π1{x ∈ J1 : W(x,.) ∈ U} = 0. Since if W(x,.) ∈/ T1 then W(x,.) ∈ U, this proves the Claim.

i

Clearly T1 inherits a metric from L1[J2], and it is complete and separable in this metric. The functions W(x,.) are everywhere dense in T1(W) and have measure 1. It also inherits a probability measure π1′ from J1 through

π1′ (X) = π1{x ∈ Ω1 : W(x,.) ∈ X}.

So T1 is a complete separable metric space with a probability measure on its Borel sets. It also follows from the deﬁnition of T1 that every open set has positive measure.

Deﬁne W : T1 × J2 → [0,1] by W(f,y) = f(y) for f ∈ T1 and y ∈ J2. Then we can replace J1 by T1 and W by W, to get a weakly isomorphic graphon. Similarly, we can replace J2 by T2.

We say that two graphons (J,W) and (J′,W′) are isometric if there is an isometric bijection φ : J → J′ that is measure preserving, and W′(φ(x),φ(y)) = W(x,y) for almost all x,y ∈ J. The deﬁnition for bigraphons is slightly more complicated: two bigraphons (J1,J2,W) and (J1′,J2′,W′) are isometric if there are isometric, measure preserving bijections φ1 : J1 → J1′ and φ2 : J2 → J2′ such that W′(φ1(x),φ2(y)) = W(x,y) for almost all (x,y) ∈ J1 × J2.

- Theorem 3.4 If two pure [bi]graphons are weakly isomorphic, then they are isometric.


Proof. We describe the proof for graphons. Theorem 2.1 (a) in [2] says that if two graphons (J,W) and (J′,W′) are weakly isomorphic, and they have no twins, then one can delete delete 0-sets S ⊆ J and S′ ⊆ J′ such that there is a bijective measure preserving map φ : J\S → J′\S′ such that W′(φ(x),φ(y)) = W(x,y) for almost all (x,y) ∈ J × J. We may even assume that for every x ∈ J \ S, W′(φ(x),φ(y)) = W(x,y) holds for almost all y (and vice versa), since this can be achieved by deleting further 0-sets. Clearly φ preserves the metric.

We also know that J \ S is dense in J (since (J,W) is pure and so its probability measure has full support), and so J is the completion of J \ S (and similarly for J′). Hence φ extends to an isometry between J and J′, which shows that (J,W) and (J′,W′) are isometric graphons.

Remark 3.5 Is purity the ultimate normalization of a graphon? There is still some freedom left: we can change the value of W on a symmetric subset of J × J that intersects every ﬁber J × {v} in a set of measure. We can take the integral of W (which is a measure ω on J), and then the derivative of ω wherever this exists. This way we get back W almost everywhere,

and a well deﬁned value for some further points. What is left undeﬁned is the set of “essential discontinuity” of W (of measure 0). It would be interesting to relate this set to combinatorial properties of W.

- 3.3 Density functions on pure [bi]graphons


The following technical Lemma will be very useful in the study of rW and related distance functions.

- Lemma 3.6 (a) Let (J,W) be a graphon, F, a graph, and S ⊆ V , an independent set of nodes. Then the function t = tS(F,W;.) : JS → R satisﬁes


|t(x) − t(x′)| ≤ |E|max

rW(xi,x′i).

i∈S

(b) Let (J1,J2,W) be a bigraphon, let F = (U1,U2,E) be a bigraph, and let Si ⊆ Ui be such that no edge connects S1 to S2. Then the function t = tbS

1,S2(F,W,.) : JS

1 × JS

2 → R satisﬁes |t(x,y) − t(x′,y′)| ≤ |E|max{max

1

2

r1(xi,x′i),max j∈S2

r2(yj,yj′)}.

i∈S1

- Remark 3.7 (i) It follows that the functions t in (a) and (b) are Lipschitz (and hence continuous).


(ii) In both parts (a) and (b) of the Lemma, the graph F could have multiple edges.

Proof. We describe the proof of (a); the proof of (b) is similar. For each i ∈ U \ S, let xi = x′i be a variable. Let E = {u1v1,...umvm}, where we may assume that vi ∈ U \ S. Then

m

m

,x′v

W(x′u

t(x) − t(x′) =

)dy −

)dy

,xv

W(xu

i

i

i

i

i=1

i=1

JU\S

JU\S

m

,x′v

W(x′u

,x′v

) − W(x′u

),dy

))

,xv

)(W(xu

,xv

W(xu

=

j

j

i

i

i

i

j

j

j>i

i<j

j=1

JU\S

and hence

m

|t(x) − t(x′)| ≤

|W(xu

j=1

JU\S

By the assumption that vi ∈ U \ S, we have xv

j

m

,x′u

|t(x) − t(x′)| ≤

rW(xu

j

j=1

,x′v

) − W(x′u

)|dy.

,xv

j

j

j

j

= x′v

j

for every j, and so

rW(xi,x′i),

) ≤ |E| max

j

1≤i≤k

which proves the assertion. Lemma 3.6 has an important corollaries for pure graphons, which are closely related to

- Lemma 2.8 in [13]. We do not formulate all versions, just a few that we need.


- Corollary 3.8 Let (J,W) be a pure graphon, and let F be a graph and let S ⊆ V , where S is independent. Then tS(F,W;x) is a continuous function of x ∈ JS.


- Applying this when F is a path of length 2, we get:
- Corollary 3.9 For every pure graphon (J,W), W ◦ W is a continuous function on J. Another application of Corollary 3.8 gives:
- Corollary 3.10 Let (J,W) be a pure graphon, and let F1,...,Fm be graphs whose node set contains a common set S, which is independent in each. Let T ⊆ S, and let a1,...,am be real numbers. Let x ∈ JT, and assume that the equation

m

i=1

aitS(Fi,W;x,y) = 0 (1)

holds for almost all y ∈ JS\T. Then it holds for all y ∈ JS\T.

Proof. By Corollary 3.8, the left hand side of (1) is a continuous function of (x,y), and so it remains a continuous function of y if we ﬁx x. Hence the set where it is not 0 is an open subset of JS\T. Since the graphon is pure, it follows that this set is either empty of has positive measure.

We formulate one similar corollary for bigraphons.

- Corollary 3.11 Let (J1,J2,W) be a pure bigraphon, and let F1,...,Fm be bigraphs with the same bipartition classes U1 and U2. Let a1,...,am be real numbers. Assume that the equation


m

aitbU

(Fi,W;x) = 0 (2)

1

i=1

holds for almost all x ∈ JU

1 . Then it holds for all x ∈ JU

1 .

1

1

- 3.4 The similarity distance


It turns out (it was already noted in [12]) that the distance function rW◦W deﬁned by the operator square of W is also closely related to combinatorial properties of a graphon. We call this the similarity distance (for reasons that will become clear later). In explicit terms, we have

rW◦W(a,b) =

J J

W(a,y)W(y,x)dy −

J

W(b,y)W(y,x)dy dx

=

J J

W(x,y) W(y,a) − W(y,b) dy dx. (3)

- Remark 3.12 Let X,Y,Z be independent uniform random points from J, then we can rewrite the deﬁnitions of these distances as


rW(a,b) = EX|W(X,a) − W(X,b)|, (4) rW◦W(a,b) = EX EY(W(X,Y)(W(Y,a) − W(Y,b))) . (5)

This formulation shows that this distance can be computed with arbitrary precision from a bounded size sample. We do not go into the details of this.

- Lemma 3.13 If (J,W) is a pure graphon, then the similarity distance rW◦W is a metric.


So (J,rW◦W) is a metric space, and hence Huasdorﬀ. We will show later that it is always compact.

Proof. The only nontrivial part of this lemma is that rW◦W(x,y) = 0 implies that x = y. The condition rW◦W(x,y) = 0 implies that for almost all u ∈ J we have (W ◦ W)(x,u) = (W ◦ W)(y,u), or more explicitly

J

(W(x,z) − W(y,z))W(z,u)dz = 0.

Using that (J,W) is pure, Corollary 3.11 implies that this holds for every u ∈ J. in particular, it holds for u = x and u = y. Taking the diﬀerence, we get that

J

(W(x,z) − W(y,z))(W(z,x) − W(z,y))dz = 0,

and hence W(x,z) = W(y,z) almost everywhere. Using again that (J,W) is pure, we get that x = y.

For every x ∈ J, the function W(x,.) is in L∞(J), and hence the weak topology of L1(J) gives a topology on J. It is well known that when restricted to L∞(J), this topology is the weak-∗ topology on L∞(J), and hence it is metrizable, and the unit ball of L∞(J) is compact in it (Alaoglu’s Theorem). A sequence of points (xn) is convergent in this topology if and only if

W(xn,y)dy →

A

W(x,y)dy

A

for every measurable set A ⊆ J. We call this the weak topology on J. We need this name only temporarily, since we are going to show that rW◦W gives a metrization of the weak topology.

- Theorem 3.14 For any pure graphon, the metric rW◦W deﬁnes exactly the weak topology.


Proof. First we show that the weak topology is ﬁner than the topology of (J,rW◦W). Suppose that xn → x in the weak topology, and consider

rW◦W(xn,x) =

J J

W(xn,y) − W(x,y) W(y,z)dy dz.

Here the inner integral tends to 0 for every z, by the weak convergence xn → x. Since it also remains bounded, it follows that the outer integral tends to 0. This implies that xn → x in (J,rW◦W).

From here, the equality of the two topologies follows by general arguments: the weak topology is compact, and the coarser topology of rW◦W is Hausdorﬀ, which implies that they are the same.

Corollary 3.15 For every pure graphon (J,W), the space (J,rW◦W) is compact.

To compare the topology of (J,rW) with these, note that for any two points x,y ∈ J, we have

rW◦W(x,y) ≤ rW(x,y), (6) which implies that the topology of (J,rW) is ﬁner than the topology of (J,rW◦W ).

- 3.5 Compact Graphons


Graphons for which the ﬁner space (J,rW) is also compact seem to have a special importance in combinatorics. Let us call such a graphon a compact graphon.

- Proposition 3.16 A pure graphon (J,W) is compact if and only if (J,rW) and (J,rW◦W) deﬁne the same topologies.


Proof. If the topologies (J,rW) and (J,rW◦W) are the same, then (J,rW) is compact by

- Corollary 3.15. Conversely, if (J,rW) is compact then, by the argument used before in the proof of Theorem 3.14, the coarser Hausdorﬀ topology of (J,rW◦W) must be the same.


- Example 4 Let J = [0,1], f(y) = ⌊log(1/y)⌋, and deﬁne


 

xf(y), if x > 1/2 and y ≤ 1/2, yf(x), if x ≤ 1/2 and y > 1/2, 0, otherwise,

W(x,y) =



where x = 0.x1x2 ... and y = 0.y1y2 ... are the binary expansions of x and y, respectively. Then selecting one point from each interval [2−k+1,2−(k)], we get an inﬁnite number of points in ([0,1],r2) mutually at distance 1/4, so (J,Wr) is not compact, but by Corollary 3.15, (J,rW◦W) is compact. So the two topologies are diﬀerent.

We conclude this section with an observation relating the topology of J to spectral theory.

- Lemma 3.17 Let (J,W) be a pure graphon. Then every eigenfunction f ∈ L2(J) of W as a kernel operator belonging to a nonzero eigenvalue is continuous in the metric rW◦W (and therefore also in rW).


Proof. It suﬃces to prove that f is continuous in (J,rW), since we can apply the argument to the graphon (J,W ◦ W), which also has f as an eigenvector.

First, we have

1 |λ|

1 |λ|

1 |λ| J

f 1 ≤

W(x,y)f(y)dy ≤

|f(x)| =

f 2,

![image 2](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile2.png>)

![image 3](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile3.png>)

![image 4](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile4.png>)

and so f is bounded. We know by Corollary 3.9 that W ◦ W is continuous in (J,rW), and hence so is

1 λ2

(W ◦ W)(x,y)f(y)dy.

f =

![image 5](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile5.png>)

J

# 4 Thin graphons

- 4.1 The main theorem


We say that a bigraphon W is thin if there is a bigraph F such that tbind(F,W) = 0. Trivially, if W is thin, then so is its complementary bigraphon 1 − W.

We call a graphon thin if it is thin as a bigraphon. (Note: for this, it is not enough to require tind(F,W) = 0 for some bipartite graph F. For example, consider the graphon U : [0,1]2 → [0,1] deﬁned by U(x,y) = U(y,x) = 1/2 if x ∈ [0,1/2] and y ∈ (1/2,1], and U(x,y) = 1 otherwise. As a bigraphon, this is not thin, but satisﬁes tind(F,W) = 0 for every bigraph with at least 3 nodes in one of the classes.

The (upper) packing dimension of a metric space (M,d) is deﬁned as

log N(ε) log(1/ε)

limsup

,

![image 6](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile6.png>)

ε→0

where N(ε) is the maximum number of points in M mutually at distance at least ε. So this dimension is ﬁnite if and only if there is a d ≥ 0 such that every set of points mutually at distance at least ε has at most ε−d elements. It is easy to see that we could use instead of N(ε) the minimum number of sets of diameter at most ε covering the space.

Our main goal is to prove:

- Theorem 4.1 If a pure bigraphon (J1,J2,W) is thin, then (a) W(x,y) ∈ {0,1} almost everywhere, (b) J1,J2 are compact, and (c) J1,J2 have ﬁnite packing dimension.


- Remark 4.2 The proof will show that if tind(F,W) = 0 for a bigraph F with k nodes, then the packing dimension of Ji is bounded by 10|F|.


Before giving the proof, we describe a class of examples, and then recall some facts about the Vapnik-Cervonenkisˇ dimension.

- Example 5 Let V be a ﬁnite or countable set, π, a probability measure on V , and deﬁne


- J1 = [0,1]V , J2 = [0,1] × V , with the power measure µ1 on J1 and the product measure µ2 on
- J2. We deﬁne a bigraphon on J1 × J2 by


W(x,y) = 1t≤x

i

for x = (xi : i ∈ S) and y = (t,i). We can metrize this bigraphon by

r1(x,x′) =

π(i)|xi − x′i|

i∈V

- for x = (xi : i ∈ S), x′ = (x′i : i ∈ S) ∈ J1, and

r2(y,y′) = |t − t′| if i = 1′, t + t′ − 2tt′ otherwise.

- for y = (t,i), y′ = (t′,i′) ∈ J2.


If V is ﬁnite, then (J1,r1) has dimension |V |, while (J2,r2) has dimension 1, and both are compact. These facts also follow if we observe that W is thin. Indeed, if F denotes the matching with |V | + 1 edges, then tbind(F,W) = 0, since among any |V | + 1 points in J2, there are two points of the form y = (t,i) and y′ = (t′,i) with t < t′, and then W(.,(t,i)) ≥ W(.,(t′,i)).

If V is inﬁnite, then (J1,r1) is inﬁnite dimensional but compact, while (J2,r2) is not compact.

- Example 6 Let J1 = J2 = [0,1], and let W(x,y) = xf(y), where x = 0.x1x2 ... is the binary expansion of x, and f(y) = ⌈log(1/y)⌉. Then for x = 0.x1x2 ... and x′ = 0.x′1x′2 ... we have


r1(x,x′) = ∞k=1 2−k|xk − x′k|, and from here is is easy to see that ([0,1],r1) is compact. Furthermore, if S ⊆ [0,1] is a set of points mutually more than 2−n apart, then any two elements of S must diﬀer in one of their ﬁrst n digits, and so their number is at most 2n. Hence the packing dimension of ([0,1],r1) is 1.

On the other hand, selecting a point yk ∈ [2−k,2−(k−1)], we get an inﬁnite number of points in ([0,1],r2) mutually at distance 1/2, so this space is not compact and inﬁnite dimensional.

- 4.2 Vapnik-Cervonenkisˇ dimension


For any set V and family of subsets H ⊆ 2V , a set S ⊆ V is called shattered, if for every X ⊆ S there is a Y ∈ H such that X = Y ∩ S. The Vapnik-Cervonenkisˇ dimension or VC-dimension dimVC(H) of a family of sets is the supremum of cardinalities of shattered sets [16]. For us, k will be always ﬁnite.

Let V be a probability space and H, a family of measurable subsets of V . A ﬁnite subfamily H′ is qualitatively independent if all the 2|H

′| atoms of the set algebra they generate have positive measure. The dual essential Vapnik-Cervonenkisˇ dimension, or brieﬂy DE-dimension, of H is a supremum of all cardinalities of qualitatively independent subfamilies of H.

We recall two basic facts about VC-dimension:

- Lemma 4.3 (Sauer-Shelah Lemma) If a family H of subsets of an m-element set has VCdimension k, then


m k

|H| ≤ 1 + m + ··· +

.

For a family H of sets, we denote by τ(H) the minimum cardinality of a set meeting every member of H. The following basic fact about VC-dimension was proved by Koml´os, Pach and Woeginger [9], based on the results of Vapnik and Cervonenkisˇ [16] (we do not state it in its sharpest form):

- Theorem 4.4 Let J be a probability space and, H a family of measurable subsets of J such that every A ∈ H has measure at least ε. Suppose that H has ﬁnite VC-dimension k. Then


1 ε

1 ε

τ(H) ≤ 8k

log

.

![image 7](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile7.png>)

![image 8](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile8.png>)

We need a couple of further facts. For a family H of sets, let H(△)H = {A△B : A,B ∈ H}.

- Lemma 4.5 For every family of sets, dimVC(H(△)H) ≤ 10 dimVC(H).


Proof. Set k = dimVC(H). Let S be a subset of V = ∪H with m elements that is shattered by H(△)H). Then every X ⊆ S arises as X = (A△B) ∩ S, where A,B ∈ H. Since (A△B) ∩ S = (A ∩ S)△(B ∩ S), the number of diﬀerent sets of the form A ∩ S is at least 2m/2. By the Sauer-Shelah Lemma, this implies that

2m/2 ≤ 1 + m + ··· +

m k

,

whence m ≤ 10k follows by standard calculation.

- Lemma 4.6 Let H be a family of measurable sets in a probability space with VC-dimension k such that π(A△B) ≥ ε for all A,B ∈ H. Then |H| ≤ (80k)kε−20k.

Proof. Consider the family H′ = H(△)H. Every A ∈ H′ has π(A) ≥ 1/ε, and dimVC(H′) ≤ 10k by Lemma 4.5. Hence by Theorem 4.4, we have

τ(H′) ≤ 80k

1 ε

![image 9](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile9.png>)

ln

1 ε

![image 10](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile10.png>)

.

Let S ⊆ ∪H be a set of size τ(H′) meeting every symmetric diﬀerence A△B (A,B ∈ H). Then the sets S ∩ A, A ∈ H are all diﬀerent. By the Sauer-Shelah Lemma, this implies that

|H| ≤ 1 + |S| + ··· + |S| 10k

< |S|10k ≤ 80k

1 ε

![image 11](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile11.png>)

ln

1 ε

![image 12](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile12.png>)

10k

< (80k)10kε−20k.

- 4.3 VC-dimension and graphons


- Lemma 4.7 Let (J1,J2,W) be a pure 0-1 valued bigraphon. Then W is thin if and only if the DE-dimension of the family RW = {supp(W(x,.)) : x ∈ T1} is ﬁnite.


Proof. Suppose that this dimension is inﬁnite. We claim that tbind(F,W) > 0 for every bipartite graph F = (U,U′,E). Let S ⊆ J1 be a set such that the subfamily {supp(W(x,.)) : x ∈ T1} is qualitatively independent. To each i ∈ U, assign a value xi ∈ S bijectively. By Corollary 3.11, the set of points y ∈ J2 such that supp(W(.,y)) ∩ S = {xi : i ∈ N(j)} has positive measure for each j ∈ U′. Hence tbind(F,W) > 0.

Conversely, suppose that k = dim(RW) is ﬁnite. Let F denote the bipartite graph with k +1 nodes in one class U and 2k+1 nodes in the other class U′, in which the nodes in U′ have all diﬀerent neighborhoods. Then tbind(F,W) = 0.

- Remark 4.8 The proof above in fact gives the following quantitative result: tbind(F,W) = 0 for some bigraph F with k nodes in its smaller bipartition class if and only if dimDE(RW ) < k.


Proof of Theorem 4.1. We may assume that W is pure.

(a) Suppose that the bigraph F = (U1,U2,E) satisﬁes tbind(F,W) = 0. Then for almost all x ∈ JU

1,ind(F,W;x) = 0. By Corollary 3.11, it follows that tbU

1 , we have tbU

1,ind(F,W;x) = 0 for every x. In particular, tbU

1

1,ind(F,W;x0,...,x0) = 0 for all x0 ∈ J1. But for this substitution,

tbU

1,ind(F,W;x0,...,x0) =

J2V2

F(j)(1 − W(x0,yj))|U

1|−dF(j),

W(x0,yj)d

j∈J2

and so for every x0 we must have W(x0,y0) ∈ {0,1} for almost all y0.

(b) By Theorem 3.16 it suﬃces to prove that if W(xn,.), n = 1,2,... weakly converges to f, i.e.,

lim

n→∞

S

W(xn,y)dy →

S

f(y)dy

for every measurable set S ⊆ J2, then it is also convergent in L1.

- Claim 4.9 The weak limit function f is almost everywhere 0-1 valued.


Suppose not, then there is an ε > 0 and a set Y ⊆ J2 with positive measure such that ε ≤ f(x) ≤ 1 − ε for x ∈ Y . Let Sn = supp(W(xn,.)) ∩ Y . We select, for every k ≥ 1, k indices n1,...nk so that the Boolean algebra generated by Sn

has 2k atoms of positive measure. If we have this for some k, then for every atom A of the boolean algebra

,...Sn

1

k

λ(A ∩ Sn) =

A

W(x,yn)dx −→

A

f(x)dx (n → ∞),

and so if n is large enough then

ε 2

ε 2

λ(A) ≤ λ(A ∩ Sn) ≤ 1 −

![image 13](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile13.png>)

![image 14](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile14.png>)

λ(A).

If n is large enough, then this holds for all atoms A, and so Sn cuts every previous atom into two sets with positive measure, and we can choose nk+1 = n.

But this means that the DE-dimension of the supports of the W(x,.) is inﬁnite, contradicting Lemma 4.7. This proves Claim 4.9.

So we know that f(x) ∈ {0,1} for almost all x, and hence

(1 − W(x,yn))dx +

f − W(.,yn) 1 =

{f=0}

{f=1}

W(x,yn)dx −→ 0.

Thus W(.,yn) → f in L1, which we wanted to prove.

(c) Let F = (U1,U2,E) be a bigraph such that tbind(F,W) = 0, and let Ui = [ki]. We show that the packing dimension of J1 is at most 10k2. To this end, we show that if any two elements of a ﬁnite set Z ⊆ J1 are at a distance at least ε, then |Z| ≤ c(k)ε−2k

. Let H = {supp(W(x,.)) : x ∈ Z}, then

2

π2(X△Y ) ≥ ε (7) for any two distinct sets X,Y ∈ H.

Let A be the union of all atoms of the set algebra generated by H that have measure 0. Clearly A itself has measure 0, and hence the family H′ = {X \ A : X ∈ H} still has property

(7).

We claim that H′ has VC-dimension less than k2. Indeed, suppose that J2 \ A contains a shattered set S with |S| = k2. To each j ∈ U2, assign a point qj ∈ S bijectively. To each i ∈ U1, assign a point pi ∈ Z such that qj ∈ supp(W(pi,.)) if and only if ij ∈ E. This is possible since S is shattered. Now ﬁxing the pi, for each j there is a subset of J2 of positive measure whose points are contained in exactly the same members of H′ as qj, since qj ∈/ A. This means that the function t = tbJ

1,ind(F,W;.) : V J

1 → R satisﬁes t(p) > 0. Corollary 3.11 implies that t(x) > 0 for a positive fraction of the choices of x ∈ JV

1

1 , and hence tbind(F,W) > 0, a contradiction. Applying Lemma 4.6 we conclude that |Z| = |H| ≤ (80k2)10k

1

ε−20k

.

2

2

- 4.4 Hereditary properties and thin bigraphons


A graph property P is a class of ﬁnite graphs closed under isomorphism. The property is called hereditary, if whenever G ∈ P, then every induced subgraph is also in P.

![image 15](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile15.png>)

Let P be any graph property. We denote by P its closure, i.e., the class of graphons (J,W) that arise as limits of graph sequences in P. For every graphon W, let I(W) denote the set of those graphs F for which tind(F,W) > 0. Clearly, I(W) is a hereditary graph property.

Let P be a hereditary property of graphs. Then

∪W∈P I(W) ⊆ P. (8)

![image 16](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile16.png>)

Indeed, if F ∈/ P, then tind(F,G) = 0 for every G ∈ P, since P is hereditary. This implies that tind(F,W) = 0 for all W ∈ P, and so F ∈/ I(W).

![image 17](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile17.png>)

Equality does not always hold in (8). For example, we can always add a bigraph G and all its induced subgraphs to P without changing P. As a less trivial example, consider all bigraphs with degrees bounded by 10. This property is hereditary, and P consists of a single bigraphon (the identically 0 function).

![image 18](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile18.png>)

![image 19](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile19.png>)

- Proposition 4.10 For a hereditary property P of graphs equality holds in (8) if and only if for every graph G ∈ P and v ∈ V (G), if we add a new node v′ and connect it to all neighbors of v, then at least one of the two graphs obtained by joining or not joining v and v′ has property P.


Proof. Suppose that this condition holds. Let F ∈ P have n nodes, and let F(k) denote a graph in P obtained from F by a repetition of this operation so that each original node has k copies. Then tind(F,F(k)) ≥ 1/nn. Let W be the limit graphon of some subsequence of the F(k) (k → ∞), then W ∈ P. Furthermore, clearly tind(F,W) > 0, and so F ∈ I(W).

![image 20](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile20.png>)

Conversely, assume that F = (V,E) ∈ I(W) for some W ∈ P, so that tind(F,W) > 0. Let F′ and F′′ be the two graphs obtained from F by doubling a node v (vv′ ∈/ E(F′), but vv′ ∈ E(F′′)), then

![image 21](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile21.png>)

tind(F,W;x)dx > 0

JV

implies that there is a positive measure of choices for the values of xu (u ∈ V (F) \ v), for which the set X of the choices of xv with tind(F,W;x) > 0 has positive measure. Clearly either W(x,y) < 1 for a positive measure of choices of (x,y) ∈ Y or this holds for W(x,y) > 0. One or the alternative, say the ﬁrst one, holds for a positive measure of choices for the values of xu (u ∈ V (F) \ v). But then t(F′,W) > 0.

All of the above notions and simple facts extend to bigraphs and bigraphons trivially. Let us turn to thin graphons and bigraphons. The signiﬁcance of thin bigraphons is supported

by the following observation:

Proposition 4.11 Let P be a hereditary bigraph property that does not contain all bigraphs. Then every bigraphon in its closure is thin.

Proposition 4.11 and Theorem 4.1 imply:

- Corollary 4.12 Let P be a hereditary bigraph property that does not contain all bigraphs. Then for every pure bigraphon (J1,J2,,W) in its closure, W is 0-1 valued almost everywhere, and J1 and J2 are compact and their dimension is bounded by a ﬁnite number depending on P only.


By this corollary, we can deﬁne, for every nontrivial hereditary property of bigraphs, a ﬁnite dimension. It would be interesting to ﬁnd further combinatorial properties of this dimension.

The natural analogue of this corollary for graph properties fails to hold.

- Example 7 Let P be the property of a graph that it is triangle-free. Then every bipartite graphon is in its closure, but such graphons need not be 0-1 valued, and their topology need not be ﬁnite dimensional or compact.


However, if we include the (seemingly) simplest of the conclusions of Corollary 4.12 as a hypothesis, then we can extend it to all graphs. A graph property P is random-free, if every W ∈ P is 0-1 valued almost everywhere.

![image 22](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile22.png>)

- Theorem 4.13 Let P be a hereditary random-free graph property. Then for every pure graphon (J,W) in its closure, J is compact and ﬁnite dimensional.


Before proving this theorem, we need some preparation.

- Lemma 4.14 For a hereditary graph property P, the following are equivalent:


- (i) P is random-free;
- (ii) there is a bigraph F such that tb(F,W) = 0 for all W ∈ P;

![image 23](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile23.png>)

- (iii) there is a bipartite graph F with bipartition (U1,U2) such that no graph obtained from F


by adding edges within U1 and U2 has property P.

Proof. (i)⇒(iii): Assume that (iii) does not hold, then for every bigraph F there is a graph Fˆ ∈ P and a partition V (Fˆ) = {U1(Fˆ),U2(Fˆ)} such that the bigraph between U1(Fˆ) and U2(Fˆ) is isomorphic to F. We want to show that P is not random-free.

Let (F1,F2,...) be a quasirandom sequence of bigraphs with edge density 1/2, with the same number of nodes in each bipartition class. Consider the graphs Fˆn, and let Fn′ and Fn′′ denote the subgraphs of Fˆn induced by U1(Fˆn) and U2(Fˆn), respectively. By selecting a subsequence we may assume that the graph sequences (F1′,F2′,...) (F1′′,F2′′,...) are convergent. By Lemma 4.16 in [5], we can order the nodes of Fn′ so that WF′

converges to a graphon ([0,1],W′) in the cut norm . , and similarly, WF′′

n

converges to a graphon ([0,1],W′′) in the cut norm. We order the nodes of Fˆn so that the nodes in Fn′ preceed the nodes of Fn′′, and keep the above ordering otherwise. Then trivially WFˆ

n

converges to the graphon

n

 

W′(2x,2y) if x,y < 1/2, W′′(2x − 1,2y − 1) if x,y > 1/2, 1/2 otherwise.

U(x,y) =



![image 24](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile24.png>)

So U ∈ P is not 0-1 valued, and so P is not random-free.

- (ii)⇒(i): Suppose that P is not random-free, and let (J,W) ∈ P be a graphon that is not

![image 25](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile25.png>)

0-1 valued almost everywhere. Then by Theorem 4.1, it is not thin as a bigraphon, which means that for every bigraph F = (U1,U2,E), tbind(F,W) > 0, so (ii) is not satisﬁed.

- (iii)⇒(ii): Consider a bigraph F = (U1,U2,E) as in (iii), and consider it as a bipartite graph


on V = U1 ∪ U2 (we assume that U1 ∩ U2 = ∅). Suppose that it does not satisfy (ii), then there is a graphon W ∈ P such that t(F,W;x) > 0 for a positive measure of choices of the x ∈ JV . For every such choice, we deﬁne a graph F′ by connecting those pairs {i,j} of nodes of F for which W(xi,xj) > 0 and either i,j ∈ U1 or i,j ∈ U2. The same supergraph F′ will occur for a positive measure of choices of the xi, and for this F′ we have tind(F′,W) > 0, so using (8), we get F′ ∈ I(W) ⊆ P, a contradiction.

![image 26](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile26.png>)

Proof of Theorem 4.13. By Lemma 4.14, there is a bigraph F such that tb(F,W) = 0 for all W ∈ P. Thus Theorem 4.1 implies the assertion.

![image 27](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile27.png>)

# 5 Regularity partitions

- 5.1 Weak and strong regularity partitions


The Regularity Lemma of Szemer´edi [14, 15], and various weaker and stronger versions of it are basic tools in the study of large graphs and graphons [12]. Our goal is to show that it is also closely related to the topology of graphons.

Let (J,W) be a graphon and P, a partition of J into measurable sets with positive measure. For x ∈ J, let S(x) denote the partition class containing x. Deﬁne

1 π(S(x))

fP(x) =

f(x)dx

![image 28](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile28.png>)

S(x)

for a function f ∈ L1(J), and WP(x,y) =

1 π(S(x))π(S(y))

W(x,y)dx.

![image 29](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile29.png>)

S(x)×S(y)

We say that P is a weak regularity partition with error ε, if W − WP ≤ ε.

We deﬁne a Szemere´di partition of a graphon with error ε as a partition P = {S1 ∪ ··· ∪ Sk} of J into measurable sets such that

| W − WP,H | ≤ ε (9)

for every function H : J × J → [0,1] that is 0-1 valued and whose support is the union of product sets Rij = Rij′ × Rij′ ⊆ Si × Sj (i,j ∈ [k]). To relate this to the weak partitions, we note that W − WP ≤ ε can be expressed as (9) for all functions h of the form 1S×T. (The formulation above is not a direct generalization of Szemer´edi’s deﬁnition, but it is closest in our setting; cf. [12].)

A strong regularity partition of a graph was introduced by Alon, Fischer, Krivelevich and M. Szegedy [1]. Here the error is speciﬁed by an inﬁnite sequence E = (ε0,ε1,...) of positive numbers. Again recasting it in our setting, P is a strong regularity partition with error E of a graphon (J,W) if there is a graphon (J,U) such that

W − U 1 ≤ ε0 and U − WP ≤ ε|P|.

Even stronger would be, of course, to require that W −WP 1 ≤ ε (equivalently, (9) holds for all measurable functions H : J × J → [−1,1]). In this case we call P an ultra-strong regularity partition with error ε.

The following result is a graphon version of the original Szemer´edi’s Regularity Lemma [14, 15], its “weak” form due to Frieze and Kannan [8], and its strong form due to Alon, Fischer, Krivelevich and M. Szegedy [1]. It was proved for graphons in [12].

- Theorem 5.1 Let (J,W) be a graphon on an atomfree probability space. Then


- (a) for every ε > 0 (J,W) has a Szemere´di partition with error ε into no more than T(ε)

classes, where T(ε) depends only on ε;

- (b) for every ε > 0 (J,W) has a weak regularity partition with error ε into no more than

22/ε

2

classes.

- (c) for every sequence E = (ε0,ε1,...) of positive numbers, (J,W) has a strong regularity


partition of (J,W) with error E into no more than T(E) classes, where T(E) depends only on E.

- Remark 5.2 (i) We note that every graphon has an ultra-strong partition with error ε by standard results in analysis, but the number of classes cannot be bounded uniformly by any function of ε.


(ii) In the usual formulation, partitions in the Regularity Lemma are equitable, i.e., the partition classes are as equal as possible. For graphons on atomless probability spaces, the classes can be required to have the same measure. In fact, it is easy to see that the partitions constructed e.g. in Corollary 5.4 and Theorem 5.8 below can be repartitioned so that the classes will be as equal as possible, the error is at most doubled, and the number of classes is increased by a factor of at most ⌈1/ε⌉.

Several other analytic aspects and versions of the Regularity Lemma were proved in [12]. One of these results made a connection between regularity partitions and partitions of J into sets with small diameter in the rW◦W metric. Here we prove a stronger, cleaner version of that result, and then show how to combine it with our results on thin graphons to get better bounds on the number of partition classes in weak regularity partitions of this graphons.

- 5.2 Voronoi cells and regularity partitions


We show that Voronoi cells in the metric spaces (J,RW) and (J,RW◦W) are intimately related to diﬀerent versions of the Regularity Lemma.

Let (J,d) be a metric space and let π be a probability measure on its Borel sets. We say that a set S ⊆ J is an average ε-net, if J d(x,S)dπ(x) ≤ ε.

Let S ⊆ J be a ﬁnite set and s ∈ S. The Voronoi cell of S with center s is the set of all points x ∈ J for which d(x,s) ≤ d(x,y) for all y ∈ S. Clearly, the Voronoi cells of S cover J. (We can break ties arbitrarily to get a partition.)

- Theorem 5.3 Let (J,W) be a graphon, and let ε > 0.


- (a) Let S be an average ε-net in the metric space (S,rW◦W ). Then the Voronoi cells of S

form a weak regularity partition with error at most 8√ε.

![image 30](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile30.png>)

- (b) Let P = {J1,...,Jk} be a weak regularity partition with error ε. Then there are points


vi ∈ Ji such that the set S = {v1,...,vk} is an average (4ε)-net in the metric space (S,rW◦W).

Proof. (a) Let P be the partition into the Voronoi cells of S. Let us write R = W − WP. We want to show that R ≤ 8√ε. It suﬃces to show that for any 0-1 valued function f,

![image 31](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile31.png>)

f,Rf ≤ 2√ε. (10)

![image 32](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile32.png>)

Let us write g = f − fP, where fP(x) is obtained by replacing f(x) by the average of f over the class of P containing x. Clearly fP,RfP = 0, and so

f,Rf = g,Rf + fP,Rf = f,Rg + fP,Rg ≤ 2 Rg 1 ≤ 2 Rg 2. (11)

For each x ∈ J, let ϕ(x) ∈ S be the center of the Voronoi cell containing x, and deﬁne W′(x,y) = W(x,φ(y)) and similarly R′(x,y) = R(x,φ(y)). Then using that (W − R)g = WPg = 0, W − W′ = R − R′ and R′g = 0, we get

Rg 22 = Rg,Rg = Wg,(R − R′)g = Wg,(W − W′)g = g,W(W − W′)g ≤ W(W − W′) 1 =

W(x,y)(W(y,z) − W(y,ϕ(z))dy dxdz

J2 J

=

J

rW(z,ϕ(z)) = EX(rW(X,S)) ≤ ε.

This proves (10).

(b) Suppose that P is a weak Szemer´edi partition with error ε. Let R = W − WP, then we know that R ≤ ε.

For every x ∈ [0,1], deﬁne

F(x) =

R(x,y)W(y,z)dy dz.

J J

Then we have

F(x)dx =

s(x,z)R(x,y)W(y,z)dxdy dz,

J

J3

where s(x,z) is the sign of R(x,y)W(y,z). For every z ∈ J,

s(x,z)R(x,y)W(y,z)dxdy ≤ 2 R ≤ 2ε,

J2

and hence

J

F(x)dx ≤ 2ε. (12)

Let x,y ∈ J be two points in the same partition class of P. Then WP(x,s) = WP(y,s) for every s ∈ J, and hence

rW(x,y) =

J J

(W(x,s) − W(y,s))W(s,z)ds dz

=

J J

(R(x,s) − R(y,s))W(s,z)ds dz

≤

R(x,s)W(s,z)ds dz +

J J

J J

= F(x) + F(y).

R(y,s)W(s,z)ds dz

For every set T ∈ P, let vT ∈ T be a point “below average” in the sense that

1 π(T)

F(vT) ≤

F(x)dx,

![image 33](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile33.png>)

T

and let S = {vT : T ∈ P}. Then using (12),

EXd(X,S) ≤

≤

J

This proves the Theorem.

T∈P T

d(x,vT )dx ≤

T∈P T

(F(x) + F(vT))dx

λ(T)F(vT) ≤ 2

F(x)dx +

T∈P

J

F(x)dx ≤ 4ε.

Theorems 5.3 and 4.1 imply the following Corollary (we prove a stronger result in the next section).

Corollary 5.4 For every bigraph F = (V,E) there is a constant cF > 0 such that if G is a graph not containing F as an induced sub-bigraph, then for every ε > 0, G has a weak regularity partition with error ε with at most cFε−10|V| classes.

- Remark 5.5 The conclusion does not remain true if the subgraph we exclude is nonbipartite. Any bipartite graph will then satisfy the condition, and some bipartite graphs are known to need an exponential (in 1/ε) number of classes in their weak regularity partitions.


- 5.3 Edit distance


We conclude with deriving bounds on the size of the Szemer´edi partitions and approximations in L1, using the packing dimension of (J,rW). In the graph theoretic case, this corresponds to approximation in edit distance.

- Lemma 5.6 Let W be a graphon such that (J,rW) can be covered by m balls of radius ε. Then there is a stepfunction U with m(1/ε)m steps such that W − U 1 ≤ 2ε.


Remark 5.7 If W is 0-1 valued, then the bound on the number of classes can be improved to m2m.

Proof. Let P = {J1,J2,...,Jm} be a partition of J into measurable sets such that for every i there is xi ∈ J with W(xi,.) − W(x,.) 1 ≤ ε for every x ∈ Ji. Let W′(x,y) = W(xi,y) for x ∈ Ji, then trivially W − W′ 1 ≤ ε. Let Qi be a partition of J into 1/ε measurable classes so that W(xi,.) varies at most ε on each class of Qi. For x ∈ Ji and y ∈ S ∈ Qi, deﬁne

1 π(S) S

W′(x,z)dz.

U(x,y) =

![image 34](<2010-lovsz-regularity-partitions-topology-graphons_images/imageFile34.png>)

Then clearly |U(x,y) − W′(x,y)| ≤ ε for all x,y ∈ J, and hence U − W 1 ≤ U − W′ 1 +

W − W′ 1 ≤ 2ε. It is obvious that U is a stepfunction in the partition generated by P and Q1,...,Qm, which has at most m(1/ε)m classes.

We obtain from this lemma:

- Theorem 5.8 Let W be a graphon such that (J,rW) has packing dimension d, then for every


−d) classes.

0 < ε < 1 it has an ultra-strong partition with error ε and with at most ε−O(ε

Proof. Consider a maximal packing in (J,rW) of balls with radius ε/8; this consists of m = O(ε−d) balls. The balls with the same centers and with radius ε/4 cover J, so Lemma 5.6 there is a stepfunction U with m(4/ε)m ≤ ε−cε

−d

steps such that W − U 1 ≤ ε/2. For the partition P into the steps of U, we have

W − WP 1 ≤ 2 W − U 1 ≤ ε (the ﬁrst inequality follows by easy computation).

For thin graphons, we get a stronger bound.

Theorem 5.9 Let W be a thin graphon in which a bigraph F = (V,E) is excluded as an induced sub-bigraph. Then for every 0 < ε < 1, it has an ultra-strong partition with error ε and with O(ε−10|V |

2

) classes.

Proof. Theorem 4.1 implies that W is 0-1 valued and it has ﬁnite packing dimension at most 10|V |. Similarly to the proof of lemma 5.6, let P = {J1,J2,...,Jm} be a partition of J with m = O(ε−|V |) into measurable sets such that for every i there is an xi ∈ J with

W(xi,.)−W(x,.) 1 ≤ ε for every x ∈ Ji. Let W′(x,y) = W(xi,y) for x ∈ Ji, then W′−W 1 ≤ ε. Let Si be the support of the function W(xi,.), and let A be the set of atoms of the Boolean algebra generated by {S1,S2,...,Sm} with positive measure. For every atom a ∈ A, let Fa ⊆ [m] denote the index set {i|a ⊆ Si} and let F denote the set system {Fa|a ∈ A}. Since F is not an induced sub-bigraph, F has VC-dimension less than |V |, and so by lemma 4.3 we obtain that |A| ≤ O(m|V |−1). The joint reﬁnement P2 of A and P is of size at most O(ε−10|F|

2

). This completes the proof since W′ is a stepfunction with steps in P2.

It is easy to see that in the deﬁnition of ultra-strong regularity partitions of 0-1 valued graphons, we can replace WP by a 0-1 valued stepfunction with the same steps, at the cost of doubling the error. Together with Remark 5.2, we can apply this to a (large) ﬁnite graph G. To state the result, we need a deﬁnition. Let H be a simple graph, and let us replace each node v of H by a set Sv of “twin” nodes, where two nodes x ∈ Su and y ∈ Sv are connected if and only if uv ∈ E(H). For each u ∈ V (H), either connect all pairs of nodes in Su, or none of them. We call every graph obtained this way a blow-up of H.

Corollary 5.10 For every bigraph F there is a constant cF > 0 such that if G is a graph not containing F as an induced sub-bigraph, then for every ε > 0, we can change ε|G|2 edges of G so that the resulting graph is a blow-up of a graph with at most cFε−10|F|

2

nodes.

Let us say that a graphon W has polynomial L1-complexity if there is a d > 0 such that for every ε > 0 there is a stepfunction W′ with O(ε−d) steps satisfying W − W′ 1 ≤ ε. We can deﬁne polynomial -complexity analogously. As we have pointed out, polynomial -complexity corresponds to the ﬁnite dimensionality of the metric space of W ◦W. Theorem 5.9 implies that every thin graphon has polynomial L1-complexity.

If W has polynomial complexity, then the structure of W can be described by a polynomial number (in 1/ε) of real parameters with an error ε in the appropriate norm. The set of graphons with polynomial complexity is closed under many natural operations such as operator product, tensor product, etc.

It could be interesting to study other aspects of this complexity notion. We oﬀer a conjecture relating our complexity notion to extremal combinatorics. It is supported by examples in [13].

Conjecture 5.11 Let F1,F2,...,Fn be a set of ﬁnite graphs, t1,t2,...,tm be real numbers in [0,1] and S be the set of graphons W with t(Fi,W) = ti for 1 ≤ i ≤ n. Then S is either empty or it contains a graphon of polynomial L1-complexity.

# References

- [1] N. Alon, E. Fischer, M. Krivelevich and M. Szegedy: Eﬃcient testing of large graphs, Combinatorica 20 (2000), 451–476.
- [2] C. Borgs, J. Chayes, L. Lov´asz: Moments of Two-Variable Functions and the Uniqueness of Graph Limits, Geometric and Functional Analysis (to appear) http://www.cs.elte.hu/~lovasz/limitunique.pdf
- [3] C. Borgs, J. Chayes, L. Lov´asz, V.T. So´s, K. Vesztergombi: Counting graph homomorphisms, in: Topics in Discrete Mathematics (ed. M. Klazar, J. Kratochvil, M. Loebl, J. Matouˇsek, R. Thomas, P. Valtr), Springer (2006), 315–371.
- [4] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s, B. Szegedy and K. Vesztergombi: Graph Limits and Parameter Testing, Proc. 38th Annual ACM Symp. on Theory of Computing 2006, 261–270.
- [5] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s, and K. Vesztergombi: Convergent Graph Sequences I: Subgraph frequencies, metric properties, and testing, Advances in Math. (2008), 10.1016/j.aim.2008.07.008.
- [6] P. Erdo¨s, L. Lov´asz, J. Spencer: Strong independence of graphcopy functions, in: Graph Theory and Related Topics, Academic Press, 165-172.
- [7] M. Freedman, L. Lov´asz, A. Schrijver: Reﬂection positivity, rank connectivity, and homomorphisms of graphs, J. Amer. Math. Soc. 20 (2007), 37–51.
- [8] A. Frieze and R. Kannan: Quick approximation to matrices and applications, Combinatorica 19, 175–220.
- [9] J. Koml´os, J. Pach and G. Woeginger: Almost Tight Bounds for epsilon-Nets, Discr. Comput. Geometry 7 (1992), 163–173.
- [10] L. Lov´asz, V.T. So´s: Generalized quasirandom graphs, J. Comb. Th. B 98 (2008), 146–163.
- [11] L. Lov´asz, B. Szegedy: Limits of dense graph sequences, J. Comb. Theory B 96 (2006), 933–957.
- [12] L. Lov´asz and B. Szegedy: Szemer´edi’s Lemma for the analyst, Geom. Func. Anal. 17

(2007), 252–270.

- [13] L. Lov´asz and B. Szegedy: Finitely forcible graphons (submitted) http://arxiv.org/abs/0901.0929
- [14] E. Szemer´edi: On sets of integers containing no k elements in arithmetic progression”, Acta Arithmetica 27 (1975) 199-245.
- [15] E. Szemer´edi: Regular partitions of graphs, Colloque Inter. CNRS (J.-C. Bermond, J.C. Fournier, M. Las Vergnas and D. Sotteau, eds.) (1978) 399–401.


## [16] V. Vapnik, A. Chervonenkis: On the uniform convergence of relative frequencies of events to their probabilities, Theor. Prob. Appl. 16 (1971), 264–280.

