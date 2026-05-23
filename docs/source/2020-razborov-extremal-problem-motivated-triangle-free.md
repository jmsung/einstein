---
type: source
kind: paper
title: An Extremal Problem Motivated by Triangle-Free Strongly Regular Graphs
authors: Alexander Razborov
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2006.01937v1
source_local: ../raw/2020-razborov-extremal-problem-motivated-triangle-free.pdf
topic: general-knowledge
cites:
---

arXiv:2006.01937v1[math.CO]2Jun2020

# An Extremal Problem Motivated by Triangle-Free Strongly Regular Graphs

### Alexander Razborov∗ June 4, 2020

Abstract

We introduce the following combinatorial problem. Let G be a triangle-free regular graph with edge density1 ρ. What is the minimum value a(ρ) for which there always exist two non-adjacent vertices such that the density of their common neighborhood is ≤ a(ρ)? We prove a variety of upper bounds on the function a(ρ) that are tight for the values ρ = 2/5, 5/16, 3/10, 11/50, with C5, Clebsch, Petersen and Higman-Sims being respective extremal conﬁgurations. Our proofs are entirely combinatorial and are largely based on counting densities in the style of ﬂag algebras. For small values of ρ, our bound attaches a combinatorial meaning to Krein conditions that might be interesting in its own right. We also prove that for any ǫ > 0 there are only ﬁnitely many values of ρ with a(ρ) ≥ ǫ but this ﬁniteness result is somewhat purely existential (the bound is double exponential in 1/ǫ).

## 1. Introduction

Triangle-free strongly regular graphs (TFSR graphs), sometimes also called SRNT (for strongly regular no triangles) is a fascinating object in algebraic combinatorics. Except for the trivial bipartite series, there are only seven

![image 1](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile1.png>)

∗University of Chicago, USA, razborov@math.uchicago.edu and Steklov Mathematical Institute, Moscow, Russia, razborov@mi.ras.ru.

2

1In this paper all densities are normalized by n, n

2 etc. rather than by n − 1, n2 ,...

![image 2](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile2.png>)

such graphs known (see e.g. [God95]). At the same time, the existing feasibility conditions still leave out many possibilities. For example, there are still 66 prospective values of parameters with λ1 ≤ 10, where λ1 is the second largest eigenvalue of G [Big11, Tables 1,2]; the most prominent of them probably being the hypothetical Moore graph of degree 57. This situation is in sharp contrast with general strongly regular graphs (or, for that matter. with ﬁnite simple groups) where non-trivial inﬁnite series are abundant, see e.g. [GR01, Chapter 10].

Somewhat superﬁcially, the methods employed for studying (triangle-free) strongly regular graphs can be categorized in “combinatorial” and “arithmetic/algebraic” methods. The latter are based upon spectral properties of G or modular counting. The former are to a large extent based on calculating various quantities (that we will highly prefer to normalize in such a way that they become densities in [0, 1]), and these calculations look remarkably similar to those used in asymptotic extremal combinatorics, particularly in the proofs based on ﬂag algebras. The unspoken purpose of this paper is to highlight and distill these connections between the two areas. To that end, we introduce and study a natural extremal problem corresponding to strong regularity.

Before going into some technical details, it might be helpful to digress on the apparent contradiction of studying highly symmetric and inherently ﬁnite objects with methods that are quite analytical and continuous in their nature. The key to resolving this is the simple observation that has been used in extremal combinatorics many times: any ﬁnite graph (or, for that matter, more complicated combinatorial object) can be alternately viewed as an analytical object called its stepfunction graphon [Lov12, §7.1] or, in other words, inﬁnite blow-up. It is obtained by replacing every vertex with a measurable set of appropriate measure. To this object we can already apply all methods based on density calculations, and the conversion of the results back to the ﬁnite world is straightforward.

Let us now ﬁx some notation. All graphs G in this paper are simple and, unless otherwise noted, triangle-free. By n = n(G) we always denote the number of vertices, and let

ρ = ρ(G) def=

2|E(G)| n(G)2

![image 3](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile3.png>)

be the edge density of G. Note that the normalizing factor here is n22, not

![image 4](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile4.png>)

n

2 : the previous paragraph provides a good clue as why this is much more natural choice. A ρ-regular graph is a regular graph G with ρ(G) = ρ. We let

|NG(u) ∩ NG(v)| n(G)

a(G) def= min

,

![image 5](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile5.png>)

(u,v) ∈E(G)

where NG(v) is the vertex neighbourhood of v. For a rational number ρ ∈ [0, 1/2], we let

a(ρ) def= max{a(G) | G is a triangle-free ρ-regular graph} (1) Our goal is to give upper bounds on a(ρ).

- Remark 1 We stress that we do have here maximum, not just supremum, this will be proven below (see Corollary 4.5). In particular, a(ρ) is also rational. Another ﬁniteness result (Corollary 4.6) says that for every ǫ > 0 there exist only ﬁnitely many rationals ρ with a(ρ) ≥ ǫ. While this result is of somewhat existential nature (the bound is double exponential in 1/ǫ), it demonstrates, somewhat surprisingly, that our relaxed version of strong regularity still implies at least some rigidity properties that might be expected from much more symmetric structures in algebraic combinatorics.
- Remark 2 The deﬁnition of a(G) readily extends to graphons, and it is natural to ask whether this would allow us to extend the deﬁnition of a(ρ) to irrational ρ or at least come up with interesting constructions beyond ﬁnite graphs: such constructions are deﬁnitely not unheard of in the extremal combinatorics. Somewhat surprisingly (again), the answer to both questions is negative. Namely, we have the dichotomy: every triangle-free graphon W (we do not even need regularity here) is either a ﬁnite stepfunction of a ﬁnite vertex-weighted graph or satisﬁes a(W) = 0 (Theorem 4.7).
- Remark 3 Every TFSR graph G with parameters (n, k, c), where k is the degree and c is the size of common neighbourhoods of non-adjacent vertices leads to the lower bound a(k/n) ≥ c/n. Thus, optimistically, one could view upper bounding the function a(ρ) as an approach to ﬁnding more feasibility conditions for TFSR graphs based on entirely combinatorial methods. This hope is somewhat supported by the fact that our bound is tight for the values corresponding to four (out of seven) known TSFR graphs, as well as an inﬁnite sequence of values not ruled out by other conditions.


- Remark 4 As we will see below, in the deﬁnition (1) we can replace ordinary ρ-regular triangle-free graphs with weighted twin-free ρ-regular triangle-free graphs that can be additionally assumed to be maximal. A complete description of such graphs with ρ > 1/3 was obtained in [BT05]. Along with very simple Lemma 4.4 below, this allows us to completely compute the value of a(ρ) for ρ > 1/3 and, in particular, determine those values of ρ for which a(ρ) > 0. Using relatively simple methods from Section 5.1, we can prove the bounds a(ρ) ≤ 3ρ (1/3 ≤ ρ ≤ 3/8), a(ρ) ≤ 3ρ − 1 (3/8 ≤ ρ ≤ 2/5) and a(ρ) = 0 (2/5 < ρ < 1/2). But since they are signiﬁcantly inferior (that is, for ρ < 2/5) to those that follow from [BT05], we will save space and in the rest of the paper focus on the range ρ ≤ 1/3.

![image 6](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile6.png>)

Our main result is shown on Figure 1. The analytical expressions for our upper bound a0(ρ) will be given in Theorem 3.1; for now let us brieﬂy comment on a few features of Figure 1.

- Remark 5 The bound is tight for the values ρ = 5011, 103 , 165 corresponding to Higman-Sims, Petersen and Clebsch, respectively. It is piecewise linear for ρ ≥ 9/32 and involves three algebraic functions of degree ≤ 4 when ρ ≤ 9/32.


![image 7](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile7.png>)

![image 8](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile8.png>)

![image 9](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile9.png>)

| | | | |
|---|---|---|---|
| | | | |


| | |
|---|---|
| | |


#### Figure 1: The main result

- Remark 6 Let us explain the reasons for using the term “Krein bound”. It may not be seen well on Figure 1 but this curve has a singular point at


ρ0 def=

3 98

(10 −

![image 10](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile10.png>)

√

![image 11](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile11.png>)

2) ≈ 0.263. (2)

For ρ ≥ ρ0, a0(ρ) is a solution to a polynomial equation gK(ρ, a) = 0 that is most likely an artifact of the proof method (and it gets superseded at ρ ≈ 0.271 by other methods anyway). The bound for ρ ≤ ρ0 is more interesting.

Recall (see e.g. [GR01, Chapter 10.7]) that the Krein parameters K1, K2 provide powerful constraints K1 ≥ 0, K2 ≥ 0 on the existence of strongly regular graphs, and in the special case of triangle-free graphs we are interested in this paper they can be signiﬁcantly simpliﬁed [Big11].

Now, K1, K2 are rational functions of k, c and non-trivial eigenvalues λ1, λ2 of the adjacency matrix. As such, when written as functions of k, c, they become (conjugate) algebraic quadratic functions and thus do not seem to possess any obvious combinatorial meaning. Their product, however, is the rational function in k, c:

K1K2 = (k − 1)(k − c)(k2 − k(3c + 1) − c3 + 4c2 − c) ≥ 0 (3) Re-writing the non-trivial term here in the variables ρ = k/n, c = a/n (and recalling that n = 1 + k(k−c1+c)), we will get a constraint fK(ρ, a) ≥ 0 that holds for all TFSR graphs. What we prove with purely combinatorial methods is that for ρ ≤ ρ0 (and less us remark that all hypothetical TFSR graphs are conﬁned to that region) this inequality holds in much less rigid setting.

![image 12](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile12.png>)

As a by-side heuristical remark, this bound was discovered by ﬂag-algebraic

computer experiments with particular values of ρ corresponding to potential TFSR graphs from [Big11, Tables 1,2]. The result turned out to be tight precisely for those values for which c = λ1(λ1 − 1), which is equivalent to K2 = 0. The connection to Krein parameters and, as a consequence, the hypothesis fK(ρ, a) ≥ 0 suggested itself immediately.

## 2. Preliminaries

We utilize all notation introduced in the previous section. In particular, all graphs G = (V (G), E(G)) are simple and, unless otherwise noted, trianglefree, and n = n(G) is the number of vertices.

Let us now remind some rudimentary notions from the language of ﬂag algebras (see [Raz07, §2.1]) restricted to graphs. A type σ is simply a totally labelled graph, that is a graph on the vertex set [k] def= {1, 2, . . ., k} for some k called the size of σ. Figure 2 shows all types used in this paper, including the trivial type 0 of size 0.

3

3

1

1 2

1 2

1 2

1 2

I

P

- 0 1


N

E

3

3

3 4

1 2

1

2

1

2

Q1

Q2

D

Figure 2: Types

A ﬂag is a graph partially labelled by labels from [k] for some k ≥ 0. Every ﬂag F belongs to the unique type obtained by removing all unlabelled vertices. Figure 3 lists all ﬂags we need in this paper.

Mnemonic rules used in this notation are reasonably consistent: the subscript, when present, normally denotes the overall number of vertices in the ﬂag. The ﬁrst part of the superscript denotes the type of the ﬂag. The remaining part, when present, helps to identify the ﬂag in case of ambiguity. For example, there is only one ﬂag P3N based on the path of length 2 and the type N. There are, however, two ﬂags based on its complement P¯3, and P¯3N.c [P¯3N.b] is the ﬂag in which the ﬁrst labelled vertex is the central [border, respectively] vertex in P¯3.

1

1

P3 P31,b

P31,c

ρ e

- 1 2

P3E,b

2

1

P¯3N,c

1 2

P¯3N,b

1 2

I3N

1 2

1

1 2

S4N

1 2

T4N P4N

1 2

M4N

1 2

- 1 2


P3N

C4

3

1 2

1 2

3

1 2

3

1 2

V4N,1

V4N,2

S4I

T4I

S4P

3

3

1 2

1 2

3

1 2

1 2

K32N

K32I

K32P

U5P

3 3 3 4

1 2

1 2

1 2

V5P,1

V5D,1 Figure 3: Flags

V5P,2

Also, for S ⊆ [3] we denote by FSI the ﬂag with 3 labelled independent vertices and one unlabelled vertex connected to the vertices from S. Thus, S4I = F{I1,2,3} and T4I = F{I3}.

Let F be a ﬂag of type σ with k labelled vertices and ℓ−k unlabelled ones, and v1, . . ., vk be (not necessarily distinct) vertices in the target graph G that span the type σ, that is (vi, vj) ∈ E(G) if and only if (i, j) ∈ E(σ). Then we let F(v1, . . ., vk) be the probability that after picking wk+1, . . ., wℓ ∈ V (G) independently at random, the σ-ﬂag induced in G by v1, . . ., vk, wk+1, . . ., wℓ is isomorphic (in the label-preserving way) to F. We stress that wk+1, . . ., wℓ are chosen completely independently at random; in particular some or all of them may be among {v1, . . ., vk}. When this happens, we treat colliding vertices as non-adjacent twins.

We will also need some basic operations on ﬂags (multiplication, evaluation and lifting operators, to be exact) but since they will not be needed until Section 5.2, we defer it until then.

In this notation ρ = 2|En(G)|

is the edge density, e(v) = |N

G(v)|

n is the relative degree of v and P3N(u, v) = |N

![image 13](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile13.png>)

![image 14](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile14.png>)

2

G(u)∩NG(v)|

n2 is the relative size of the common neighbourhood of u and v. A graph G is ρ-regular if e(v) ≡ ρ. Etc.

![image 15](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile15.png>)

Warning. When evaluating [the density of] say C4, we must take into account not only induced copies, but also contributions made by paths P3 (one collapsing diagonal) and even by edges (both diagonals collapsing).

We let

a(G) def= min

P3N(u, v) and, for a rational ρ ∈ [0, 1/2], we also let

(u,v) ∈E(G)

a(ρ) def= max{a(G) | G a triangle-free ρ-regular graph} (we will prove below that the minimum value here is actually attained).

## 3. The statement of the main result

Many of our statements and proofs, particularly for small values of ρ, involve rather cumbersome computations. A Maple worksheet with supporting evidence can be found at http://people.cs.uchicago.edu/~razborov/files/tfsr.mw

Let2

fK(ρ, a) def= a3 + (3ρ − 4)a2 + (5ρ − 1)a − 4ρ3 + ρ2. Then

fK(ρ, ρ2) = ρ3(ρ3 + 3ρ2 − 4ρ + 1) > 0 (since ρ ≤ 1/3) while

ρ2 1 − ρ

ρ5(1 − 2ρ) (1 − ρ)3

= −

fK ρ,

< 0.

![image 16](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile16.png>)

![image 17](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile17.png>)

Let Krein(ρ) be the largest (actually, the only) root of the cubic polynomial equation fK(ρ, z) = 0 in the interval3 z ∈ ρ2, ρ

2

1−ρ . Next, let

![image 18](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile18.png>)

√

gK(ρ, a) def= a4 + a3((4

+aρ(ρ2 + (15 − 10

√

√

√

![image 19](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile19.png>)

![image 20](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile20.png>)

![image 21](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile21.png>)

2) + a2ρ((6 − 4

2 − 8)ρ + 7 − 4

2)ρ + 8

√

√

√

![image 22](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile22.png>)

![image 23](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile23.png>)

![image 24](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile24.png>)

2 − 3) + ρ3((8

2 − 12)ρ + 3 − 2

2)ρ + 2

![image 25](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile25.png>)

2 − 13)

√

![image 26](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile26.png>)

2)

(the meaning of this expression might become clearer in Section 5.2.1). We again have gK(ρ, ρ2) > 0,

ρ2 1 − ρ

gK ρ,

![image 27](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile27.png>)

ρ7(1 − 2ρ) (1 − ρ)4

= −

< 0, (4)

![image 28](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile28.png>)

and we deﬁne Krein(ρ) as the largest (unique) root of the equation gK(ρ, z) = 0 in the interval z ∈ ρ2, ρ

2

1−ρ . We note that Krein(ρ0) = Krein(ρ0) = ρ

![image 29](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile29.png>)

3 (recall that ρ0 is given by (2)), and that they have the same ﬁrst derivative at ρ = ρ0 as well. It should also be noted that Krein(ρ) ≥ Krein(ρ) and that they are very close to each other. For example, let

0

![image 30](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile30.png>)

ρ1 ≈ 0.271

be the appropriate root of the equation gK(ρ, 1−23ρ) = 0; this is the point at which Krein bounds yield to more combinatorial methods, see Figure 1. Then

![image 31](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile31.png>)

in the relevant interval ρ ∈ [ρ0, ρ1] we have Krein(ρ) ≤ Krein(ρ) + 3 · 10−6.

![image 32](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile32.png>)

- 2This is the non-trivial factor in (3) re-written in terms of ρ,a
- 3The left end of this interval is determined entirely by convenience, but the right end


represents a trivial upper bound on a(ρ) resulting from double counting copies of C4. See the calculation after (41) for more details.

We ﬁnally let

Improved(ρ) def=

15 − 22ρ − 2√242ρ − 27 − 508ρ2 74

![image 33](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile33.png>)

,

![image 34](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile34.png>)

and let

66 + 2√13

![image 35](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile35.png>)

ρ2 def=

269 ≈ 0.272 be the root of the equation Improved(ρ) = 1−23ρ. We can now explain Figure 1 as follows:

![image 36](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile36.png>)

![image 37](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile37.png>)

- Theorem 3.1 For ρ ≤ 1/3 we have a(ρ) ≤ a0(ρ), where




Krein(ρ), ρ ∈ [0, ρ0] Krein(ρ), ρ ∈ [ρ0, ρ1]

- 1−3ρ

![image 38](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile38.png>)

2 , ρ ∈ [ρ1, ρ2] Improved(ρ), ρ ∈ [ρ2, 9/32]

ρ/3, ρ ∈ [9/32, 3/10] 2ρ − 21, ρ ∈ [3/10, 5/16]

![image 39](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile39.png>)

- 2




a0(ρ) def=



5ρ, ρ ∈ [5/16, 1/3].

![image 40](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile40.png>)

## 4. Finiteness results

Before embarking on the proof of Theorem 3.1, let us fulﬁll the promise made in Remarks 1 and 2.

Throughout the paper we will be mostly working with (vertex)-weighted graphs, i.e. with graphs G equipped with a probability measure µ on V (G), ordinary graphs corresponding to the uniform measure. The ﬂag-algebraic notation F(v1, . . ., vk) introduced in Section 2 readily extends to this case simply by changing the sampling distribution from uniform to µ.

The twin relation ≈ on G is given by u ≈ v iﬀ NG(u) = NG(v), and a graph G is twin-free if its twin relation is trivial. Factoring a graph by its twin relation gives us a twin-free weighted graph Gred that preserves all properties of the original graph G (like the values ρ(G) and a(G), ρ-regularity or triangle-freeness) we are interested in this paper.

Our main technical argument in this section is the following

- Theorem 4.1 Let (G, µ) be a vertex-weighted triangle-free twin-free graph and a def= a(G, µ). Then


−1

n(G) ≤ (2a−1)1+a

+ 2a−1.

Proof. Let n def= n(G) and V (G) def= {v1, . . ., vn}, where µ(v1) ≥ . . . ≥ µ(vn). Choose the maximal k with the property µ({vk, . . ., vn}) ≥ a/2. Then, by averaging, we have 1k−−a/12 ≥ n−a/k2+1 which is equivalent to

![image 41](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile41.png>)

![image 42](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile42.png>)

n ≤ 2a−1(n − k + 1). Hence, denoting

W0 def= {vk+1, . . ., vn} (note for the record that µ(W0) < a/2), it suﬃces to prove that |W0| ≤ (2a−1)a

−1

. (5) For W ⊆ V (G) let us deﬁne

K(W) def=

NG(w);

w∈W

note that K(W) ∩ W = ∅. The bound (5) will almost immediately follow from the following two claims.

- Claim 4.2 For any W ⊆ V (G) and v∗  ∈ W ∪ K(W) we have

µ

 

 

v∈K(w)

NG(v)

  ∪ NG(v∗)

  ≥ µ

 

v∈K(w)

NG(v)

  + a.

- Proof of Claim 4.2. Since v∗  ∈ K(W), there exists w ∈ W such that (v∗, w)  ∈ E(G); moreover, w = v∗ since v∗  ∈ W. Now, all vertices in


- NG(v∗) ∩ NG(w) contribute to the diﬀerence NG(v∗) \ v∈K(w) NG(v) (since w ∈ W and G is triangle-free). Claim 4.2


![image 43](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile43.png>)

- Claim 4.3 For every W ⊆ V (G) with µ(W) ≤ a/2 and |W| ≥ 2 there exists v∗  ∈ W ∪ K(W) such that4


a 2|W|.

|W ∩ NG(v∗)| ≥

![image 44](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile44.png>)

![image 45](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile45.png>)

4note that this bound is about absolute sizes, not about measures

- Proof of Claim 4.3. Let L(W) def= {v  ∈ W | NG(v) ∩ W  ∈ {∅, W}} .


Note that L(W) is disjoint from both W and K(W) and that there are no edges between K(W) and L(W). The desired vertex v∗ will belong to L(W), and we consider two (similar) cases.

Case 1. K(W) = ∅. In this case we have

L(W) =

NG(w) \ W. (6)

w∈W

W.l.o.g. we can assume that n ≥ 3 which implies (since G is twin-free) that G is not a star. That is, for every w ∈ V (G) there exists v = w nonadjacent to it and hence we have the bound e(w) ≥ P3N(v, w) ≥ a on the minimum degree. Along with (6) and the assumption µ(w) ≤ a/2, we get µ(NG(w) ∩ L(W)) ≥ a/2 for any w ∈ W. Now the existence of the required v∗ ∈ L(W) follows by standard double counting of edges between W and L(W) (note that, unlike L(W), the set W is not weighted in this argument according to µ).

Case 2. K(W) = ∅.

Then W is independent and the condition v  ∈ W in the deﬁnition of L(W) can be dropped. Fix arbitrarily w = w′ ∈ W (this is how we use the assumption |W| ≥ 2). Then w, w′ are not twins and NG(w)△NG(w′) ⊆ L(W), hence L(W) = ∅. Fix arbitrarily v ∈ L(W) and w ∈ W with (v, w)  ∈ E(G). Then

NG(v) ∩ NG(w) ⊆ L(W) (7) (since there are no edges between L(W) and K(W)) hence µ(L(W)) ≥ a. We claim that actually µ(NG(w) ∩ L(W)) ≥ a for every w ∈ W. Indeed, if

- NG(w) ⊇ L(W) this follows from the bound we have just proved, and if there exists v ∈ L(W) with (v, w)  ∈ E(G), this follows from (7). The analysis of Case 2 is now completed by the same averaging argument as in Case 1 (with the ﬁnal bound improved by a factor of two). Claim 4.3


![image 46](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile46.png>)

The rest of the proof of Theorem 4.1 is easy. We start with the set W0 and then, using Claims 4.3 and 4.2, recursively construct sets W0 ⊃ W1 ⊃

W2 ⊃ . . . such that5 |Wr| ≥ (2a−1)r|W0| and

 

  ≥ ar. (8)

µ

NG(v)

v∈K(Wr)

This process may terminate for only one reason: when the assumption |Wr| ≥ 2 from Claim 4.3 no longer holds. On the other hand, due to (8), it must terminate within a−1 steps. The bound (5) follows, and this also completes the proof of Theorem 4.1.

![image 47](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile47.png>)

- Remark 7 The bound in Theorem 4.1 is essentially tight. Indeed, let us consider the graph Gh on n = 2h + 2h vertices


{uiǫ | i ∈ [h], ǫ ∈ {0, 1}} ∪. va a ∈ {0, 1}h ,

and let E(Gh) consist of the matching {(ui0, ui1) | i ∈ [h]}∪ (va, v1−a) a ∈ {0, 1}h as well as the cross-edges {(uiǫ, va) | a(i) = ǫ}. Then G is a triangle-free twinfree graph and for every (w, w′)  ∈ E(G), NG(w) ∩ NG(w′) either contains an u-vertex or contains at least 2h−2 v-vertices. Hence if we set up the weights as µ(uiǫ) = 41h and µ(va) = 2−h−1, we will have a(G, µ) ≥ 41h and n(G) is inverse exponential in a(G, µ)−1.

![image 48](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile48.png>)

![image 49](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile49.png>)

Before deriving consequences mentioned in the introduction, we need a simple exercise in linear algebra (and optimization).

- Lemma 4.4 Let G be a ﬁnite graph. Then there exists at most one value ρ = ρG for which there exist vertex weights µ such that (G, µ) is ρ-regular. Whenever ρG exists, it is a rational number. Moreover, in that case there are rational weights η such that (G, η) is ρG-regular and


a(G, η) = max{a(G, µ) | (G, µ) is ρG − regular} .

Proof. Fix an arbitrary system of weights µ for which (G, µ) is ρ-regular for some ρ. Let A be the adjacency matrix of G, µ be the (column) vector comprised of vertex weights and j be the identically one vector. Then the regularity condition reads as Aµ = ρ·j. Since j is in the space spanned by the

![image 50](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile50.png>)

5We could have shaved oﬀ an extra factor 2r−1 by observing that Case 1 in Claim 4.3 may occur at most once.

columns of A, there exists a rational vector η such that Aη = j. Now, on the one hand ηTAµ = ρ·(ηTj) and, on the other hand, ηTAµ = jTµ = 1 (the latter equality holds since µ is a probability measure). Hence ρ = (ηTj)−1 is a rational number not depending on µ.

For the second part, we note that the linear program



a → max η(v) ≥ 0 (v ∈ V (G))



v η(v) = 1 e(v) = ρ (v ∈ V (G)) P3N(v, w) ≥ a ((v, w)  ∈ E(G))



with rational coeﬃcients in the variables η(v) is feasible since µ is its solution. Hence it also has an optimal solution with rational coeﬃcients.

![image 51](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile51.png>)

Let us now derive consequences.

- Corollary 4.5 For every rational ρ there exists a ﬁnite triangle-free ρ-regular graph G such that a(G) attains the maximum value a(ρ) among all such graphs.

Proof. We can assume w.l.o.g. that a(ρ) > 0. Let {Gn} be an increasing sequence of graphs such that limn→∞ a(Gn) = a(ρ). Then Theorem 4.1 implies that {Gredn } may assume only ﬁnitely many values. Hence (by going to a subsequence) we can also assume that all Gn correspond to diﬀerent vertex weights µn of the same (twin-free) graph G. But now Lemma 4.4 implies the existence of rational weights η(v), say η(v) = N

v

![image 52](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile52.png>)

N for integers Nv, N such that a(G, η) = a(ρ). We convert (G, η) to an ordinary graph replacing every vertex v with a cloud of Nv twin clones.

![image 53](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile53.png>)

- Corollary 4.6 For every ǫ > 0 there are only ﬁnitely many ρ with a(ρ) ≥ ǫ. In other words, 0 is the only accumulation point of im(a).


Proof. Immediately follows from Theorem 4.1 and Lemma 4.4 since according to the latter, the edge density ρ is completely determined by the skeleton G of a ρ-regular weighted graph (G, µ).

![image 54](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile54.png>)

Now we prove that there are no “inherently inﬁnite” triangle-free graphons W with a(W) > 0. Since this result is somewhat tangential to the rest of

the paper, we will be rather sketchy and in particular we refer the reader to [Lov12] for all missing deﬁnitions.

A graphon W : [0, 1] × [0, 1] −→ [0, 1] is triangle-free if

W(x, y)W(y, z)W(x, z)dxdydz = 0.

Given a graphon W, let P3N : [0, 1]×[0, 1] −→ [0, 1] be deﬁned by P3N(x, y) =

W(x, y)W(x, z)dz; Fubini’s theorem implies that P3N is deﬁned a.e. and is measurable. We deﬁne a(W) as the maximum value a such that

λ (x, y) ∈ [0, 1]2 W(x, y) < 1 =⇒ P3N(x, y) ≥ a = 1. (9)

To every ﬁnite vertex-weighted graph (G, µ) we can associate the naturally deﬁned step-function graphon WG,µ (see [Lov12, §7.1] or Section 1 above), and two graphons are isomorphic if they have the same sampling statistics [Lov12, §7.3].

Theorem 4.7 Let W be a triangle-free graphon. Then we have the following dichotomy: either a(W) = 0 or W is isomorphic to WG,µ for some ﬁnite vertex-weighted triangle-free graph (G, µ).

Proof. (sketch) Assume that a(W) > 0, that is (9) holds for some a > 0. Let Gn be the random sample from the graphon W; this is a probability measure on the set Gn of triangle-free graphs on n vertices up to isomorphism. A standard application of Chernoﬀ’s bound along with (9) gives us that

P[a(Gn) ≤ a/2] ≤ exp(−Ω(n)). (10)

Now, if we equip n∈N Gn with the product measure n Gn, then the fundamental fact from the theory of graph limits is that the sequence of graphs Gn sampled according to this measure converges to W with probability 1, and the same holds for their twin-free reductions Gredn . Since the series n exp(−Ω(n)) converges, Theorem 4.1 along with (10) implies that the number of vertices in Gredn is bounded, also with probability 1. Then a simple compactness argument shows that it contains a sub-sequence converging to WG,µ for some ﬁnite weighted graph (G, µ).

![image 55](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile55.png>)

## 5. The proof of Theorem 3.1

We ﬁx a triangle-free ρ-regular graph G, and for the reasons explained in Remark 4, we assume that ρ ≤ 31. We have to prove that a(G) ≤ a0(ρ), that is there exists a pair of non-adjacent vertices u, v with P3N(u, v) ≤ a0(ρ). We work in the set-up of Section 4, that is we replace G with its weighted twinfree reduction (G, µ); the weights µ will be dropped from notation whenever it may not create confusion. We also let a def= a(G, µ) > 0 throughout.

![image 56](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile56.png>)

- 5.1. ρ ≥ ρ1: exploiting combinatorial structure


The only way in which we will be using twin-freeness is the following claim (that was already implicitly used in the proof of Theorem 4.1).

- Claim 5.1 For any two non-adjacent vertices u = v, P3N(u, v) ≤ ρ − a.

Proof. First we have P3N(u, v) + P¯3N,c(u, v) = e(v) = ρ. Thus it remains to prove that P¯3N,c(u, v) ≥ a. But since u and v are not twins and e(u) = e(v), there exists a vertex w ∈ NG(u) \ NG(v). Then a ≤ P3N(v, w) ≤ P¯3N,c(u, v), the last inequality holds since G is triangle-free.

![image 57](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile57.png>)

We now ﬁx, for the rest of the proof, two non-adjacent vertices v1, v2 with P3N(v1, v2) = a. Let P def= NG(v1) ∩ NG(v2) (thus µ(P) = P3N(u, v) = a) and we also let I def= V (G) \ (NG(v1) ∪ NG(v2)) (note that v1, v2 ∈ I). We can easily compute µ(I) = I3N(v1, v2) by inclusion-exclusion as follows:

I3N(v1, v2) = 1 − e(v1) − e(v2) + P3N(v1, v2) = 1 − 2ρ + a. (11)

- Claim 5.2 For any w ∈ P there exists v3 ∈ I such that (w, v3)  ∈ E. Proof. The assumptions ρ ≤ 13 and a > 0 imply, along with (11), that


![image 58](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile58.png>)

- I3N(v1, v2) > ρ. As e(w) = ρ, Claim 5.2 follows.


![image 59](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile59.png>)

Before proceeding further, let us remark that a0(ρ) ≥ 3ρ for ρ ∈ [ρ1, 1/3] (veriﬁcations of computationally unpleasant statements like this one can be found in the Maple worksheet at http://people.cs.uchicago.edu/~razborov/files/tfsr.mw). Hence we can and will assume w.l.o.g. that

![image 60](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile60.png>)

ρ 3

a >

. (12)

![image 61](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile61.png>)

- Claim 5.3 For any v3 ∈ I we have S4I(v1, v2, v3) > 0, that is there exists a vertex w ∈ P adjacent to v3.


Proof. Since P is non-empty, we can assume w.l.o.g. that ∃w ∈ P ((v3, w)  ∈ E) (otherwise we are done). Now we have the computation (again, since G is triangle-free)

 

ρ = e(v3) ≥ P3N(v3, v1) + P3N(v3, v2) + P3N(v3, w) − S4I(v1, v2, v3) ≥ 3a − S4I(v1, v2, v3).



The claim now follows from (12).

![image 62](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile62.png>)

(13)

Let now c def= |P| be the size of P (weights are ignored). Claims 5.2 and 5.3 together imply that c ≥ 2. The rest of the analysis depends on whether c = 2, c = 3 or c ≥ 4.

- 5.1.1. c = 2 Let P = {w, w′}, where µ(w) ≥ µ(w′), and note that µ(w′) ≤ a2. By Claim 5.2, there exists v3 ∈ I such that (w, v3)  ∈ E. We have S4I(v1, v2, v3) ≤ µ(w′) ≤ a2. Along with (13), this gives us the bound

![image 63](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile63.png>)

![image 64](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile64.png>)

a ≤

2 5

![image 65](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile65.png>)

ρ. (14)

By Claim 5.3, for any v3 ∈ I we have either (w, v3) ∈ E(G) or (w′, v3) ∈ E(G). In other words, the neighbourhoods of v1, v2, w, w′ cover the whole graph or, equivalently, I3N(v1, v2)+I3N(w, w′) = 1. Now, I3N(v1, v2) = 1−2ρ+a by (11), and for (w, w′) this calculation still works in the “right” direction: I3N(w, w′) = 1 − 2ρ + P3N(w, w′) ≥ 1 − 2ρ + a. Thus we get a ≤ 2ρ − 21. Along with (14), we get that a ≤ min 5 2ρ, 2ρ − 12 ≤ a0(ρ) (see the Maple worksheet) and this completes the analysis of the case c = 2.

![image 66](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile66.png>)

![image 67](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile67.png>)

![image 68](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile68.png>)

- 5.1.2. c = 3


Let P = {w1, w2, w3}. We abbreviate F{Ii}(w1, w2, w3) to Fi, F{Ii,j}(w1, w2, w3) to Fij and F{I1,2,3}(w1, w2, w3) (= S4I(w1, w2, w3)) to f3. In our claims below

we will always assume that {i, j, k} = {1, 2, 3} is an arbitrary permutation on three elements.

We begin with noticing that Claim 5.1 applied to the pair (wi, wk) gives us Fik+f3 ≤ ρ−a that can be re-written (since Fi+Fij+Fik+f3 = e(wi) = ρ) as

Fi + Fij ≥ a. (15) On the other hand, the bound P3N(wi, wj) ≥ a re-writes as

Fij + f3 ≥ a. (16) We also note that (15) (along with its analogue obtained by changing Fi

to Fj) implies

Fij = 0 =⇒ (Fi ≥ a ∧ Fj ≥ a). (17)

- Claim 5.4 Fij > 0 =⇒ Fk ≥ a.

Proof. Let v be any vertex contributing to Fij, that is (wi, v), (wj, v) ∈ E(G) while (wk, v)  ∈ E(G). Then a ≤ P3N(wk, v) ≤ Fk.

![image 69](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile69.png>)

Now, (17) along with Claim 5.4 imply that there exist at least two indices i ∈ [3] with Fi ≥ a. Assume w.l.o.g. that F1, F2 ≥ a. Our goal (that, somewhat surprisingly, is the most complicated part of the analysis) is to show that in fact F3 ≥ a as well.

- Claim 5.5 Fi > 0.

Proof. When i = 1.2, we already have the stronger fact Fi ≥ a so we are only left to show that F3 > 0. Assume the contrary. Then F12 = 0 by Claim 5.4, hence f3 ≥ a by (16). Also, F13 ≥ a and F23 ≥ a by (15) (with i = 3). Summing all this up, ρ = e(w3) = F13 + F23 + f3 ≥ 3a, contrary to the assumption (12).

![image 70](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile70.png>)

The next claim, as well as Claim 5.13 below, could have been also written very concisely at the expense of introducing a few more ﬂags; we did not do this since those ﬂags are not used anywhere else in the paper.

- Claim 5.6 There is an edge between [the sets of vertices corresponding to] Fi and Fj.


Proof. Since {i, j} ∩ {1, 2} = ∅, we can assume w.l.o.g. that i = 1. We have

ρ = e(w1) = F1 + F1j + F1k + f3

and F1 ≥ a, F1j + f3 ≥ a (by (16)). Hence F1k < a due to (12). Let now v be an arbitrary vertex contributing to Fj that exists by Claim 5.5. We have P3N(v, w1) ≥ a, and all contributions to it come from either F1k or F1. Since F1k < a, v must have at least one neighbor in F1.

![image 71](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile71.png>)

- Claim 5.7 Fi + Fij + Fik ≥ 2a.

Proof. Let v, v′ be as in Claim 5.6 with i := k, i.e. (v, v′) ∈ E(G), v contributes to Fk and v′ contributes to Fj. Then 2a ≤ P3N(wi, v)+P3N(wi, v′) ≤ Fi +Fij +Fik simply because (v, v′) is an edge, and this implies that the sets corresponding to P3N(wi, v), P3N(wi, v′) are disjoint.

![image 72](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile72.png>)

- Claim 5.8 Fij > 0.

Proof. Assuming the contrary, we get f3 ≥ a from (16) and Fi + Fik ≥ 2a from Claim 5.7. This (again) contradicts e(wi) = ρ < 3a.

![image 73](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile73.png>)

Now we ﬁnally have

- Claim 5.9 Fi ≥ a. Proof. Immediate from Claims 5.4 and 5.8.

![image 74](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile74.png>)

- Claim 5.10 µ(wi) + Fjk ≥ 4a − ρ.


Proof. Let (by Claim 5.9) v be any vertex contributing to Fi. Then we have the computation (cf. (13)):

 

ρ = e(v) = T4I(v1, v2, v) + P3N(v1, v) + P3N(v2, v) − S4I(v1, v2, v) ≥ T4I(v1, v2, v) + 2a − µ(wi).

(18)



On the other hand, 2a ≤ P3N(v, wj) + P3N(v, wk) ≤ T4I(v1, v2, v) + Fjk (19)

(note that v may not be connected to vertices in Fij, Fik, f3 as it would have created a triangle with wi). The claim follows from comparing these two inequalities.

![image 75](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile75.png>)

Let us now extend the notation f3 = F{1,2,3} to fν def=

FS.

[3] ν

)

S∈(

Then Claim 5.3 implies f0 = 0 and hence

f1 + f2 + f3 = µ(I) = 1 − 2ρ + a (20) and also

e(wi) = 3ρ. (21) Next, Claim 5.9 implies

f1 + 2f2 + 3f3 =

i

f1 ≥ 3a (22) and Claim 5.10, after summing it over i ∈ [3] gives us

f2 ≥ 11a − 3ρ. (23) Resolving (20) and (21) in f3, we get

2f1 + f2 = 3 − 9ρ + 3a. (24) Comparing this with (22) and (23) gives us the bound

3 14

a ≤

(1 − 2ρ) (25) which is ≤ a0(ρ) as long as ρ ∈ [9/32, 1/3].

![image 76](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile76.png>)

To complete the analysis of case c = 3 we still have to prove that a(ρ) ≤

Improved(ρ) for ρ1 ≤ ρ ≤ 329 . As it uses some material from the proof of the Krein bound, we defer this to Section 5.2.2.

![image 77](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile77.png>)

- 5.1.3. c ≥ 4


Fix arbitrarily distinct w1, w2, w3, w4 ∈ P and let us employ the same notation Fi, Fij, Fijk as in the previous section; {i, j, k, ℓ} = {1, 2, 3, 4}. As before, let

FS.

fν =

[4] ν

)

S∈(

Note that since we allow c > 4, this time f0 need not necessarily be zero. We further let

FS def=

FT

T⊆[4] T∩S =∅

be the measure of i∈S NG(wi), and we also use abbreviations Fi, Fij, Fijk, F1234 in this case.

To start with, Fi = ρ and Claim 5.1 implies Fij ≥ ρ + a.

- Claim 5.11 Fijk ≥ ρ + 2a.


Proof. For S ⊆ {i, j, k}, let FS∗ def= FS + FS∪{ℓ} be the result of ignoring wℓ and we (naturally) let

fν∗ def=

FS∗.

{i,j,k} ν

)

S∈(

Then (cf. (21))

f1∗ + 2f2∗ + 3f3∗ = 3ρ, and also

f2∗ + 3f3∗ = P3N(wi, wj) + P3N(wi, wk) + P3N(wj, wk) ≤ 3(ρ − a) by Claim 5.1. Besides, Fijk = f1∗ + f2∗ + f3∗.

If f2∗ = 0, we are done: Fijk = 3ρ − 2f3∗ ≥ 3ρ − 2(ρ − a) = ρ + 2a. Hence we can assume that f2∗ > 0, say, Fij∗ > 0. Pick an arbitrary vertex v corresponding to Fij∗ then, as before, Fijk = Fij + Fk∗ ≥ ρ + a + P3N(v, wk) ≥ ρ + 2a.

![image 78](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile78.png>)

- Lemma 5.12 F1234 ≥ ρ + 3a.


Proof. First, F1234 = Fjkℓ + Fi ≥ ρ + 2a + Fi by Claim 5.11. Hence we can assume that Fi < a (for all i ∈ [4], as usual). Also, we can assume that f3 = 0 since otherwise we are done by the same reasoning as in the proof of Claim 5.11.

Now, let Γ be the graph on [4] with the set of edges E(Γ) = {(i, j) | Fij > 0}.

Analogously to (15), we have

Fi + Fij + Fiℓ ≥ a (26) (recall that Fijℓ = 0) and, analogously to Claim 5.4,

Fij > 0 =⇒ Fk + Fkℓ ≥ a. (27)

Next, (26), along with Fi < a, implies that the minimum degree of Γ is ≥ 2, that is Γ is the complement of a matching. Hence there are only three possibilities: Γ = K4, Γ = C4 or Γ = K4 −e, and the last one is ruled out by (27) along with Fk < a.

If Γ = K4 then summing up (27) over all choices of k, ℓ, we get 3f1 + 2f2 ≥ 12a. Adding this with f1 + 2f2 + 4f4 = 4ρ, we get F1234 = f1 + f2 + f4 ≥ ρ + 3a. Thus it remains to deal with the case Γ = C4, say E(Γ) = {(1, 2), (2, 3), (3, 4), (4, 1)}.

First we observe (recall that f3 = 0) that

f4 = P3N(w1, w3)(= P3N(w2, w4)) ≥ a. Next, (26) amounts to

Fi + Fi,i+1 ≥ a (28)

(all summations in indices are mod 4) and hence 2Fi+Fi,i+1+Fi,i−1+f4 ≥ 3a. Comparing with

Fi + Fi,i+1 + Fi,i−1 + f4 = e(wi) = ρ,

we see that Fi ≥ 3a − ρ which is strictly positive by the assumption (12). Likewise, Fi,i+1 = ρ − f4 − (Fi + Fi,i−1) ≤ ρ − 2a < a.

- Claim 5.13 There is an edge between Fi and Fi+1.

- Proof of Claim 5.13. This is similar to the proof of Claim 5.6. Pick up a


vertex v contributing to Fi (Fi > 0 as we just observed). Then P3N(wi+1, v) ≤ Fi+1 + Fi+1,i+2 and since we already know that Fi+1,i+2 < a, there exists a vertex corresponding to Fi+1 and adjacent to v. Claim 5.13

![image 79](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile79.png>)

- Claim 5.14 Fi + Fi+1 + Fi,i+1 ≥ 2a.


- Proof of Claim 5.14. This is similar to the proof of Claim 5.7. Pick vertices v, v′ witnessing Claim 5.13 with i := i + 2, so that in particu-


lar (v, wi+2), (v′, wi−1), (v, v′) are all in E(G) while (v, wi+1), (v′, wi) are not. Then

2a ≤ P3N(v, wi+1) + P3N(v′, wi) ≤ Fi + Fi+1 + Fi,i+1

since P3N(v, wi+1) ≤ Fi+1 + Fi,i+1, P3N(v′, wi) ≤ Fi + Fi,i+1 and the corresponding sets are disjoint since (v, v′) is an edge. Claim 5.14

![image 80](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile80.png>)

Now we can complete the proof of Lemma 5.12:

F1234 = (F1 + F12 + F14 + F1234) + (F2 + F23) + (F3 + F4 + F34) ≥ ρ + 3a by (28) and Claim 5.14.

![image 81](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile81.png>)

This also completes the proof of Theorem 3.1 for ρ ≥ ρ1 (that is, modulo the bound Improved(ρ) deferred to Section 5.2.2). Indeed, since F1234 ≤ 1 − 2ρ+a, Lemma 5.12 implies a ≤ 1−23ρ which is ≤ a0(ρ) as long as ρ ∈ [ρ1, 1/3].

![image 82](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile82.png>)

### 5.2. Analytical lower bounds

In this section we prove the bounds a(ρ) ≤ Krein(ρ) (ρ ≤ ρ0), a(ρ) ≤ Krein(ρ) (ρ ∈ [ρ0, ρ1]) and a(ρ) ≤ Improved(ρ) (ρ ∈ [ρ2, 9/32]). We keep all the notation and conventions from the previous section.

Let us continue a bit our crash course on ﬂag algebras we began in Section 2. The product F1(v1, v2, . . ., vk)F2(v1, v2, . . ., vk), where F1 and F2 are ﬂags of the same type and v1, . . ., vk ∈ V (G) induce this type in G, can be always expressed as a ﬁxed (that is, not depending on G, v1, . . ., vk) linear combination of expressions of the form F(v1, . . ., vk). The general formula is simple (see [Raz07, eq. (5)]) but it will be relatively clear how to do it in all concrete cases we will be dealing with. We stress again that it is only possible because we sample vertices with repetitions, otherwise the whole theory completely breaks down. Also, things can be easily set up in such a way that, after extending it by linearity to expressions f(v1, . . ., vk), where f is a formal R-linear combination of ﬂags, this becomes the product in a naturally deﬁned commutative associative algebra.

We also need the averaging or unlabelling operator6 f  → f σ,η. Let σ be a type of size k, and η: [k′] ֌ [k] be an injective mapping, usually written

![image 83](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile83.png>)

6For the reader familiar with graph limits, let us remark that their operator is diﬀerent but connected to ours via a simple Mo¨bius transformation, followed by summation over several types.

as [η1, . . ., ηk′] or even η1 when k = 1 (here η1, . . ., ηk′ are pairwise diﬀerent elements of [k]). Then we have the naturally deﬁned type σ|η of size k′ given by (i, j) ∈ E (σ|η) if and only if (ηi, ηj) ∈ E(σ). Now, given a linear combination f of σ-ﬂags and w1, . . ., wk′ ∈ V (G) spanning the type σ|η, we consider the expectation E[f(¯v1, . . .v¯k)], where v¯j is wi if j = ηi and picked according to the measure µ, independently of each other, when j  ∈ im(η). Again, there is a very simple general formula computing this expectation as a real linear combination of σ|η-ﬂags, denoted by f σ,[η

1,...,ηk′] that, again, does not depend on G, w1, . . ., wk′ [Raz07, §2.2].

- Remark 8 It is important (and turns out very handy in concrete computa-


tions) to note that we set f(¯v1, . . ., v¯k) def= 0 if v¯1, . . ., v¯k do not induce σ. In particular, we let

σ, η def= 1 σ,η; (29)

this is simply the pair (σ, η) viewed as a σ|η-ﬂag with an appropriate coeﬃcient [Raz07, Theorem 2.5(b)]. In other words, f σ,η is not the conditional expectation by the event “(¯v1, . . ., v¯k) induce σ” but the expectation of f multiplied by the characteristic function of this event.

Finally, we also need the lifting operator πσ,η, where σ, η are as above. Namely, for a σ|η-ﬂag F, let

πσ,η(F)(v1, . . ., vk) def= F(vη

, . . ., vη

)

k′

1

be the result of forgetting certain variables among v1, . . ., vk and possibly re-enumerating the remaining ones according to η. It may look trivial but we will see below that it turns out to be very handy in certain calculations. Also note that, unlike · σ,η, πσ,η does respect the multiplicative structure.

When η is empty, f σ,η and πσ,η are abbreviated to f σ and πσ, respectively.

The main tool in ﬂag algebras is the light version of the Cauchy-Schwartz inequality formalized as

f2 σ,η ≥ 0, (30)

and the power of the method relies on the fact that positive linear combinations of these inequalities can be arranged as a semi-deﬁnite programming problem. But the resulting proofs are often very non-instructive, so in this paper we have decided to use more human-oriented language of optimization.

Let us stress that, if desired, the argument can be also re-cast as a purely symbolic sum-of-squares computation based on statements of the form (30).

After this preliminary work, let us return to the problem at hand. As in the previous section, we ﬁx arbitrarily two non-adjoint vertices v1, v2 with P3N(v1, v2) = a and let P def= NG(v1)∩NG(v2), I def= V (G)\(NG(v1)∪NG(v2)). Recall that µ(P) = a and µ(I) = 1 − 2ρ + a.

- 5.2.1. Krein bounds


We are going to estimate the quantity S4I(T4I + S4I) I,[1,2](v1, v2) from both sides and compare results.

The upper bound does not depend on whether ρ ≤ ρ0 or not and it consists of several typical ﬂag-algebraic computations.

Convention. When the parameters (v1, v2, . . ., vk) in ﬂags are omitted, this means that the inequality in question holds for their arbitrary choice. We specify them explicitly when the fact depends on the speciﬁc property P3N(v1, v2) = a of v1 and v2.

As we have already implicitly computed in the previous section,

1 3

- 1

![image 84](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile84.png>)

- 2


(S4I)2 I,[1,2] =

K32P P,[1,2]. Similarly,

K32N =

![image 85](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile85.png>)

- 1

![image 86](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile86.png>)

- 2


U5P P,[1,2]. Altogether we have

S4IT4I I,[1,2] =

- 1

![image 87](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile87.png>)

- 2


S4I(S4I + T4I) I,[1,2] =

K32P + U5P P,[1,2]. (31)

On the other hand, we note that P3E,b = πE,2(e) = ρ and since 21P31,b = P3E,b E,1, we also have P31,b = 2ρ2. Hence

![image 88](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile88.png>)

2ρ2 = πP,3(P31,b) = K32P + U5P + V5P,1 + V5P,2. (32) Let us compute the right-hand side here. We have

V5P,1 = 2 V5D,1 D,[1,2,3]  D, [1, 2, 3] (v1, v2) = πP,[1,2](P¯3N,b)(v1, v2) = ρ − a (33)

(see the deﬁnition (29)) and

V5D,1 = πD,[3,4](P3N) ≥ a. Putting these together,i

V5P,1(v1, v2, w) ≥ 2a(ρ − a) (w ∈ P)

and, by symmetry, the same holds for V5P,2. Comparing with (32), we ﬁnd that

(K32P + U5P)(v1, v2, w) ≤ 2ρ2 − 4a(ρ − a) = 2((ρ − a)2 + a2). (34)

Averaging this over all w ∈ P and taking into account (31), we arrive at our ﬁrst main estimate

S4I(S4I + T4I) I,[1,2](v1, v2) ≤ a(ρ2 − 2a(ρ − a)). (35)

For the lower bound we ﬁrst claim that T4I ≤ S4I + ρ − 2a. (36)

This was already established in (18), but let us re-cup the argument using the full notation:

ρ = πI,3(e) = T4I + πI,[1,3](P3N) + πI,[2,3](P3N) − S4I ≥ T4I + 2a − S4I.

Next, we need a lower bound on T4N(v1, v2) = T4I I,[1,2](v1, v2), that is on the density of those edges that have both ends in I. For that we ﬁrst classify all edges of G according to the number of vertices they have in I:

πN(ρ) = T4N + S4N +

2

V4N,i + P4N. (37)

i=1

Now,

S4N(v1, v2) = 2 πP,3(e) P,[1,2](v1, v2) = 2aρ. Further we note that

- 1

![image 89](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile89.png>)

- 2


ρ(ρ − a) = πQ

i,3(e) Q

i,[1,2](v1, v2) =

V4N,i + P4N (v1, v2) (i = 1, 2). (38)

Summing this over i = 1, 2 and plugging our ﬁndings into (37), we get ρ = T4N(v1, v2) + 2aρ + 4ρ(ρ − a) − P4N(v1, v2). (39)

So, the only thing that still remains is to estimate P4N(v1, v2) but this time from below. For that it is suﬃcient to compute its contribution to the right-hand side of (38) (letting, say, i := 1):

a(ρ − a) ≤ πQ

1,[2,3](P3N) Q

1,[1,2] =

- 1

![image 90](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile90.png>)

- 2


P4N(v1, v2).

Substituting this into (39), we arrive at our estimate on the number of edges entirely within I:

 

T4I I(v1, v2) = T4N(v1, v2) ≥ ρ − 2aρ − 4ρ(ρ − a) + 2a(ρ − a) = ρ − 2(ρ2 + (ρ − a)2).

(40)



We are now prepared to bound S4I(S4I + T4I) I,[1,2](v1, v2) from below. As a piece of intuition, let us re-normalize S4I and T4I by the known values  I, [1, 2] = 1 + a−2ρ (cf. Remark 8) so that they become random variables in the triangle

T = (S4I, T4I) T4I ≥ 0, T4I ≤ S4I + ρ − 2a, S4I ≤ a .

Then we know the expectation of S4I, have the lower bound (40) on the expectation of T4I, and we need to bound the expectation of S4I(S4I + T4I), also from below. For that purpose we are going to employ duality, i.e. we are looking for coeﬃcients α, β, γ depending on a, ρ only such that

L(x, y) def= x(x + y) − (αx + βy + γ)

is non-negative on T, and applying · I,[1,2] to this relation produces “the best possible result”. As we mentioned above, an alternative would be to write down an explicit “sum-of-squares” expression: the resulting proof would be shorter but it would be less intuitive.

Let us ﬁrst observe the obvious upper bound

ρ2 1 − ρ

a ≤

, (41)

![image 91](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile91.png>)

it follows from the computation 3ρ2 = 3 P31 1 = P3 = 3 P3N N ≥ 3a(1 − ρ). Next, the right-hand side of (40) is a concave quadratic function in a, with

√

√

![image 92](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile92.png>)

![image 93](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile93.png>)

2ρ−4ρ2

2ρ+4ρ2

two roots a1(ρ) def= ρ −

2 , a2(ρ) def= ρ −

2 . Further, a1(ρ) ≤ a0(ρ) ≤ ρ

![image 94](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile94.png>)

![image 95](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile95.png>)

2

1−ρ ≤ a2(ρ). Hence we can assume w.l.o.g. that the right-hand

![image 96](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile96.png>)

side in (40) is non-negative. Therefore, by decreasing T4I if necessary, we can assume that the bound (40) on its expectation is actually tight.

Next, we note that since the quadratic form x(x + y) is indeﬁnite, the function L(x, y) attains its minimum somewhere on the border of the compact region T. Since L is linear on the line x = a we can further assume that the minimum is attained at one of the lines y = 0 or y = x+ρ−2a. Note further that along both these lines L is convex.

We begin more speciﬁc calculations with the bound gK(ρ, a) ≥ 0 that is less interesting but also less computationally heavy. As a motivation for the forthcoming computations, we are looking for two points (x0, 0), (x1, x1+ρ− 2a) on the lines T4I = 0, T4I = S4I + ρ − 2a that are collinear7 with the point (cx, cy), where

ρ − 2(ρ2 + (ρ − a))2 1 − 2ρ + a

aρ 1 − 2ρ + a

cx def=

, cy def=

.

![image 97](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile97.png>)

![image 98](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile98.png>)

and such that the function L(x, 0) has a double root at x0 while L(x, x+ρ−2a) has a double root at x1. Solving all this in α, β, γ, x0, x1 gives us (see the Maple worksheet)

√

![image 99](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile99.png>)

2 − 1)cy (42) x1 = 1 −

x0 = cx + (

√2 2

√

![image 100](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile100.png>)

![image 101](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile101.png>)

2 + 1)x0 − (ρ − 2a))

((

![image 102](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile102.png>)

α = 2x0 β = (3 − 2

√

√

![image 103](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile103.png>)

![image 104](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile104.png>)

2 + 1)x0 − (ρ − 2a)) γ = −x20.

2)(2(

The remarks above imply that indeed L(x, y)|T ≥ 0 hence we have S4I(S4I + T4I) I,[1,2] ≥ αaρ + β(ρ − 2(ρ2 + (ρ − a)2) + γ(1 − 2ρ + a). (43)

![image 105](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile105.png>)

7cf. (40), the normalizing factor 1 − 2ρ + a is suggested by Remark 8. The particular choice of cx,cy is needed only for the “best possible result” part.

Comparing this with (35), we get (up to the positive multiplicative factor

1−2ρ+a

2 ) that gK(ρ, a) ≥ 0. Given the way the function Krein was deﬁned, gK(ρ, a) < 0 whenever a ∈ Krein(ρ), ρ

![image 106](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile106.png>)

2

1−ρ . The required bound a ≤ Krein(ρ) now follows from (41).

![image 107](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile107.png>)

The improvement fK(ρ, a) ≥ 0 takes place when the right-hand side in

(42) is > a since then we can hope to utilize the condition S4I ≤ a. As above, we ﬁrst explicitly write down a solution of the system obtained by replacing

the equation L′(x, 0)|x=x0

= 0 with x0 = a and only then justify the result.

Performing the ﬁrst step in this program gives us somewhat cumbersome rational functions that we attempt to simplify by introducing the abbreviations

- u0(ρ, a) def=

1 7

![image 108](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile108.png>)

(ρ + 2a − 2aρ − 4ρ2)

- u1(ρ, a) def=


1 7

(3ρ − a − 7a2 + 15aρ − 12ρ2) u(ρ, a) def= 4u0(ρ, a) + u1(ρ, a).

![image 109](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile109.png>)

Then we get x0 = a x1 =

a(2a − ρ2 − 3ρa) u(ρ, a) α = 2a +

![image 110](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile110.png>)

7(ρ − a)(u1(ρ, a)2 − 2u0(ρ, a)2) u(ρ, a)2 β =

![image 111](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile111.png>)

a(34u0(ρ, a)2 + 3u1(ρ, a)2 − 4u0(ρ, a)u1(ρ, a) − 2aρ(1 − 3ρ + a)2) u(ρ, a)2 γ = a2 − αa.

![image 112](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile112.png>)

In order to analyze this solution, we ﬁrst note that due to the bound just established we can assume w.l.o.g. that

a ∈ [Krein(ρ), Krein(ρ)].

The function u0(ρ, a) is linear and increasing in a and u0 (ρ, Krein(ρ)) > 0 (ρ = 0) hence u0(ρ, a) ≥ 0. The function u1(ρ, a) is quadratic concave in a and u1 (ρ, Krein(ρ)) , u1 ρ, Krein(ρ) ≥ 0. These two facts imply that u(ρ, a) > 0 (ρ > 0) hence our functions are at least well-deﬁned.

Next, u0, u1 ≥ 0 imply that L′(x, 0)|x=a = 2a−α has the sign opposite to u1(ρ, a)−

√2u0(ρ, a). This expression (that up to a constant positive factor is equal to cx+(√2−1)cy −a) is also concave in a. Moreover, it is non-negative for ρ ∈ [0, ρ0], a ∈ [Krein(ρ), Krein(ρ)] (at ρ = ρ0 the two bounds meet together: Krein(ρ0) = Krein(ρ0) = ρ0/3 and also u1(ρ, ρ/3) −

![image 113](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile113.png>)

![image 114](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile114.png>)

√2u0(ρ, ρ/3) = 0). This completes the proof of L′(x, 0)|x=a ≤ 0 hence (given that L(a, 0) = 0) we have L(x, 0) ≥ 0 for x ≤ a. As we argued above, this gives us L|T ≥ 0 which implies (43), with new values of α, β, γ. Comparing it with (40),

![image 115](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile115.png>)

we get fK(ρ, a) ≥ 0, up to the positive multiplicative factor 2ua((ρρ,a−a)). This concludes the proof of fK(ρ, a) ≥ 0 whenever ρ ≤ ρ0 and hence of the bound a ≤ Krein(ρ) in that interval.

![image 116](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile116.png>)

As a ﬁnal remark, let us note that since the ﬁnal bound fK(ρ, a) ≥ 0 has a very clear meaning in algebraic combinatorics, it looks likely that the disappointingly complicated expressions we have encountered in proving it might also have a meaningful interpretation. But we have not pursued this systematically.

- 5.2.2. The improved bound for c = 3


Let us now ﬁnish the proof of the bound a ≤ Improved(ρ), ρ ∈ [ρ2, 9/32] left over from Section 5.1.2. We utilize all the notation introduced there, assume that c = 3, and we need to prove that fI(ρ, a) ≥ 0. We also introduce the additional notation

ai def= µ(wi) (i = 1..3) for the weights of the vertices comprising the set P; thus, 3i=1 ai = a.

We want to obtain an upper bound on T4N(v1, v2) and then compare it with (40). Let us split I = J ∪. K, where J corresponds to f1 and K corresponds to f2 + f3. Recalling that

T4N = T4I I,[1,2], let us split the right-hand side according to this partition as (with slight abuse of notation)

T4I I,[1,2] = T4I J,[1,2] + T4I K,[1,2]. When v ∈ J corresponds to Fi, we have S4I(v1, v2, v) = ai and hence, by

(36), T4I(v1, v2, v) ≤ ρ − 2a + ai. Thus T4I J,[1,2] ≤

Fi(ρ − 2a + ai).

i

In order to bound T4I K,[1,2], we ﬁrst note that K is independent (every two vertices in K have a common neighbor in P). Furthermore, the only edges between K and J are between parts corresponding to Fi and Fjk. Hence T4I K,[1,2] ≤ i FiFjk and we arrive at the bound

T4N(v1, v2) ≤

i

Fi(ρ − 2a + Fjk + ai). (44)

Next, let us denote by ǫi the (non-negative!) deﬁcits in Claim 5.10:

ǫi def= ai + Fjk − 4a + ρ; ǫi ≥ 0. Then (44) re-writes as follows:

T4N(v1, v2) ≤ 2af1 +

3

Fiǫi.

i=1

Let us now assume w.l.o.g. that F1 ≥ F2 ≥ F3. Then, since all ǫi are non-negative,

3

Fiǫi ≤ F1 ·

i=1

3

ǫi = F1(f2 − 11a + 3ρ) = F1(3 − 6ρ − 8a − 2f1),

i=1

where the last equality follows from (24). Summarizing,

T4N(v1, v2) ≤ 2af1 + F1(3 − 6ρ − 8a − 2f1) = F1(3 − 6ρ − 8a) − 2f1(F1 − a) ≤ F1(3 − 6ρ − 8a) − 2(F1 + 2a)(F1 − a),

where the last inequality holds since F1 ≥ a and f1 = F1 +F2 +F3 ≥ F1 +2a by Claim 5.9. The right-hand side here is a concave quadratic function in F1; maximizing, we ﬁnd

T4N(v1, v2) ≤

33 2

15 2

a2 + 15aρ −

![image 117](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile117.png>)

![image 118](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile118.png>)

9 2

ρ2 −

a +

![image 119](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile119.png>)

9 2

9 8

ρ +

.

![image 120](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile120.png>)

![image 121](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile121.png>)

Comparing with (40), we get a constraint Q(ρ, a) ≥ 0 that is quadratic concave in a, and Improved(ρ) is its smallest root. Moreover, Q ρ, 143 (1 − 2ρ) = −(11ρ−2)(949 −32ρ) ≤ 0 since ρ2 > 112 . Hence the preliminary bound (25) can be improved to a ≤ Improved(ρ).

![image 122](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile122.png>)

![image 123](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile123.png>)

![image 124](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile124.png>)

## 6. Conclusion

In this paper we have taken a prominent open problem in the algebraic graph theory and considered its natural semi-algebraic relaxation in the vein of extremal combinatorics. The resulting extremal problem displays a remarkably rich structure, and we proved upper bounds for it employing methods greatly varying depending on the range of edge density ρ. Many of these methods are based on counting techniques typical for extremal combinatorics, and one bound has a clean interpretation in terms of algebraic Krein bounds for the triangle-free case.

The main generic question left open by this work is perhaps how far can this connection between the two areas go. Can algebraic combinatorics be a source of other interesting extremal problems? In the other direction, perhaps ﬂag algebras and other advanced techniques from extremal combinatorics can turn out to be useful for ruling out the existence of highly symmetric combinatorial objects with given parameters? These questions are admittedly open-ended so we would like to stop it here and conclude with several concrete open problems regarding TFSR graphs and their relaxations introduced in this paper.

Can the Krein bound a(ρ) ≤ Krein(ρ) be improved for small values of ρ? Of particular interest are the values ρ = 1677, ρ = 285 or ρ = 507 , ideally showing that a 1677 = 774 , a 28 5 = 281 or a 50 7 = 501 . In other words, can we show that like the four denser TFSR graphs, the M22 graph, the Gewirtz graph and the Hoﬀman graph are also extremal conﬁgurations for their respective edge densities?

![image 125](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile125.png>)

![image 126](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile126.png>)

![image 127](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile127.png>)

![image 128](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile128.png>)

![image 129](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile129.png>)

![image 130](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile130.png>)

![image 131](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile131.png>)

![image 132](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile132.png>)

![image 133](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile133.png>)

Another obvious case of interest is ρ = 325057 corresponding to the only hypothetical unknown Moore graph. More generally, can we rule out the existence of a TSFR graph for at least one additional pair (ρ, a) by showing that actually a(ρ) ≤ a?

![image 134](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile134.png>)

For some “non-critical” (that is, not corresponding to TFSR graphs) ρ it is sometimes also possible to come up with constructions providing nontrivial lower bounds on a(ρ). A good example8 is provided by the Kneser

2k−1 k

) (

(

and a = 1 (

graphs KG3k−1,k having ρ =

but there does not seem to be any reasons to believe that they are optimal. Are there any other values

![image 135](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile135.png>)

![image 136](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile136.png>)

3k−1 k

3k−1 k

)

)

![image 137](<2020-razborov-extremal-problem-motivated-triangle-free_images/imageFile137.png>)

8Let us remind that we conﬁne ourselves to the region ρ ≤ 1/3. A complete description of all non-zero values a(ρ) for ρ > 1/3 follows from [BT05].

of ρ for which we can compute a(ρ) exactly? Of particular interest here is the value ρ = 1/3 critical for the Erd¨os-Simonovits problem (see again [BT05, Problem 1] and the literature cited therein). Can we compute a(1/3) or at least determine whether a(1/3) = 0 or not?

Speaking of which, is there any rational ρ ∈ (0, 1/3] for which a(ρ) = 0? Equivalently, does there exist ρ ∈ [0, 1/3] for which there are no trianglefree ρ-regular graphs (or, which is the same, weighted twin-free graphs) of diameter 2? Note for comparison that there are many such values for ρ > 1/3; in fact, all examples leading to non-zero a(ρ) fall into one of a few inﬁnite series.

We conclude by remarking in connection with this question that regular weighted triangle-free twin-free graphs of diameter 2 seem to be extremely rare: a simple computer search has shown that Petersen is the only such graph on ≤ 11 vertices with ρ ≤ 1/3.

## References

[Big11] N. Biggs. I. Strongly regular graphs with no triangles. II. Families of parameters for SRNT graphs. III. The Second Subconstituent of some Strongly Regular Graphs. IV. Some Properties of Strongly Regular Graphs. Technical Report 0911.2160, 0911.2455, 1003.0175, 1106.0889 [math.CO], arxiv e-prints, 2009-2011.

[BT05] S. Brandt and S. Thomass´e. Dense triangle-free graphs are four colorable: A solution to the Erd¨os-Simonovits problem. Available at http://perso.ens-lyon.fr/stephan.thomasse/liste/vega11.pdf, 2005.

[God95] C. Godsil. Problems in algebraic combinatorics. Electronic Journal of Combinatorics, 2:F1, 1995.

[GR01] C. Godsil and G. Royle. Algebraic Graph Theory. Springer-Verlag, 2001.

[Lov12] L. Lova´sz. Large Networks and Graph Limits. American Mathematical Society, 2012.

[Raz07] A. Razborov. Flag algebras. Journal of Symbolic Logic, 72(4):1239– 1282, 2007.

