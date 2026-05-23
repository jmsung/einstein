---
type: source
kind: paper
title: More about sparse halves in triangle-free graphs
authors: Alexander Razborov
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2104.09406v2
source_local: ../raw/2021-razborov-more-about-sparse-halves.pdf
topic: general-knowledge
cites:
---

arXiv:2104.09406v2[math.CO]28Jul2021

# More about sparse halves in triangle-free graphs

### Alexander Razborov∗ July 29, 2021

Abstract

One of Erd˝os’s conjectures states that every triangle-free graph on n vertices has an induced subgraph on n{2 vertices with at most n2{50 edges. We report several partial results towards this conjecture. In particular, we establish the new bound 102427 n2 on the number of edges in general case. We completely prove the conjecture for graphs of girth ě 5, for graphs with independence number ě 2n{5 and for strongly regular graphs. Each of these three classes includes both known (conjectured) extremal conﬁgurations, the 5-cycle and the Petersen graph.

![image 1](<2021-razborov-more-about-sparse-halves_images/imageFile1.png>)

## 1. Introduction

Throughout his long career, Erd˝os repeatedly [Erd76, Erd84, Erd97] asked several questions united by one common theme: how far from being bipartite can a triangle-free graph be. One of them, the “pentagon problem”, was completely solved in [HHK`13, Grz12]. Another question asks what can be the maximum possible ℓ1-distance (which in this case is simply the number of edges deleted) from a triangle-free graph to the class of bipartite graphs. It was studied in [EFPS88, EGS92, BCL21].

This paper is devoted to the third question, “half-graph” conjecture sometimes referred to as “one of Erd˝os’s favorite” [KS06]. Given a triangle-free graph G, is it always possible to remove half of its vertices such that the

![image 2](<2021-razborov-more-about-sparse-halves_images/imageFile2.png>)

∗University of Chicago, USA, razborov@math.uchicago.edu and Steklov Mathematical Institute, Moscow, Russia, razborov@mi.ras.ru.

edge density 2||EVppGGq|q|

becomes ď 1{25? In this direction, there has been more recent work done [EFRS94, Kri95, KS06, NY15] although the conjecture still remains widely open.

![image 3](<2021-razborov-more-about-sparse-halves_images/imageFile3.png>)

2

In this paper we improve on several statements from those papers and oﬀer some new results.

Fix a triangle-free graph G on n vertices and let βpGq be the minimum number of edges in its half-graphs, normalized1 by n2. The half-graph conjecture by Erd˝os says that βpGq ď 501 , for any triangle-free G. The bound βpGq ď 161 is obvious (attained by the random half), [EFRS94] proved that βpGq ď 301 and [Kri95] improved this to βpGq ď 361 .

![image 4](<2021-razborov-more-about-sparse-halves_images/imageFile4.png>)

![image 5](<2021-razborov-more-about-sparse-halves_images/imageFile5.png>)

![image 6](<2021-razborov-more-about-sparse-halves_images/imageFile6.png>)

![image 7](<2021-razborov-more-about-sparse-halves_images/imageFile7.png>)

Theorem. For any triangle-free graph G, βpGq ď 102427 .

![image 8](<2021-razborov-more-about-sparse-halves_images/imageFile8.png>)

The number 102427 here is not arbitrary, it reﬂects what can be achieved with a certain class of methods, and the Clebsch graph is an extremal example for the resulting extremal problem. We will comment more on it below.

![image 9](<2021-razborov-more-about-sparse-halves_images/imageFile9.png>)

The (conjectural) extremal examples in the half-graph conjecture are the pentagon C5 and the Petersen graph. The former does not contain induced matching of size 2 as well.

Theorem. The half-graph conjecture is true for any (triangle-free) graph without induced matchings of size 2.

Before going any further, let us brieﬂy discuss the proofs of these two theorems as they bring about potentially interesting concepts and questions. Digression on quadriliterals counting. Let ρ “ ρpGq and C4 “ C4pGq be the edge density of G and the density of quadriliterals (copies of C4) in it. They are computed in the sense of ﬂag algebras/graph limits: G is replaced ﬁrst with its inﬁnite blow-up (so that in particular copies of the path P3 in G and even individual edges contribute to C4pGq). These two quantities are of fundamental importance in the theory of quasi-random graphs: C4 ě 3ρ4, and an increasing sequence of graphs with the same value of ρpGq is quasirandom if and only if this inequality is asymptotically tight [CGW89].

For triangle-free graphs this bound can be easily improved to

3ρ4 1 ´ ρ

C4 ě

. (1)

![image 10](<2021-razborov-more-about-sparse-halves_images/imageFile10.png>)

![image 11](<2021-razborov-more-about-sparse-halves_images/imageFile11.png>)

2

1It would have been much more natural to normalize by n

2 instead but we prefer our notation to be consistent with the literature.

![image 12](<2021-razborov-more-about-sparse-halves_images/imageFile12.png>)

This is a quantitative reﬁnement of the statement that triangle-free graphs are not quasi-random, and thus it is natural to ask: what is the smallest value of C4pGq as a function of ρpGq? In a sense, it is a dual to Erd˝os’s questions. The latter ask, in one or another form, how far from being bipartite a triangle-free graph can be. The “quadriliteral question”, on the contrary, is asking how far from quasi-random a triangle-free graph must be.

We expect this question to be extremely diﬃcult in general. But it is very tightly related to Erd˝os’s conjectures as was already demonstrated in [EFPS88, Section 2]. In our context, an easy analysis of [part of] Krivelevich’s proof, followed by a straightforward averaging gives:

Proposition 1.1

βpGq ď

C4pGq 12ρpGq

1 8

ρpGq ´

.

![image 13](<2021-razborov-more-about-sparse-halves_images/imageFile13.png>)

![image 14](<2021-razborov-more-about-sparse-halves_images/imageFile14.png>)

Both bounds on βpGq then follow from the following Theorem.

- 1. For any triangle-free graph G,

C4pGq ě

3 2

![image 15](<2021-razborov-more-about-sparse-halves_images/imageFile15.png>)

ρpGq2 ´

81 256

![image 16](<2021-razborov-more-about-sparse-halves_images/imageFile16.png>)

ρpGq.

- 2. For any triangle-free graph G without induced matchings of size 2,


C4pGq ě

3 2

ρpGq2 ´

![image 17](<2021-razborov-more-about-sparse-halves_images/imageFile17.png>)

6 25

ρpGq.

![image 18](<2021-razborov-more-about-sparse-halves_images/imageFile18.png>)

This theorem is proved via a “medium size” ﬂag-algebraic calculation. The second bound is tight for ρ “ 2{5, as it must be since the pentagon C5 is the (conjectural) extremal example for the half-graph conjecture. The ﬁrst inequality beats the trivial bound (1) for 0.257 ď ρ ď 0.366. It is tight for ρ “ 5{16, the extremal example being the Clebsch graph, and this seems to be the only non-trivial value of ρpGq for which we know the exact solution to the quadriliteral problem.

We further remark that our bound βpGq ď 102427 is tight for a reasonably natural restriction of Erd˝os’s conjecture. More speciﬁcally, many previous results, including Proposition 1.1, are based on the following simple construction. Pick an edge e P EpGq. It naturally deﬁnes a splitting of V pGq into three parts. The sparse half constructed by this method is determined by

![image 19](<2021-razborov-more-about-sparse-halves_images/imageFile19.png>)

assigning the same weight within each of these parts. Then the value 102427 in the half-graph conjecture is the best one can achieve using this method,

![image 20](<2021-razborov-more-about-sparse-halves_images/imageFile20.png>)

with the Clebsch graph being (again) an extremal example.

Let us now return to reviewing the remaining results. The half-graph conjecture is obvious if ρpGq ď 4{25 (once more, the random half will do the job). Keevash and Sudakov [KS06] relaxed this to ρpGq ď 1{16. Theorem. The half-graph conjecture is true for any triangle-free graph with ρpGq ď 33´

?161

![image 21](<2021-razborov-more-about-sparse-halves_images/imageFile21.png>)

116 « 0.1751.

![image 22](<2021-razborov-more-about-sparse-halves_images/imageFile22.png>)

Based on this theorem, we prove the following: Theorem. The half-graph conjecture is true for any triangle-free strongly regular graph.

A signiﬁcant amount of activity took place around the critical value ρ “ 2{5. [Kri95, Theorem 3] proved the conjecture for regular triangle-free graphs with ρpGq ě 2{5 and [KS06] removed the restriction of regularity. Norin and Yepremyan [NY15] improved this result by relaxing the assumption ρpGq ě 2{5 to ρpGq ě 2{5 ´ γ, where γ ą 0 is a (calculable) constant. When ρpGq is replaced by the (normalized) minimum degree δpGq, the bound on γ signiﬁcantly improves and the half-graph conjecture is true whenever δpGq ě

5 14 [NY15]. Theorem. Let αpGq be the normalized (by n) independence number of G, and assume that αpGq ě 3{8. Then

![image 23](<2021-razborov-more-about-sparse-halves_images/imageFile23.png>)

βpGq ď

αpGq ˆ

- 1

![image 24](<2021-razborov-more-about-sparse-halves_images/imageFile24.png>)

- 2


- 1

![image 25](<2021-razborov-more-about-sparse-halves_images/imageFile25.png>)

- 2


´ αpGq˙.

Corollary. The half-graph conjecture holds for any triangle-free graph with (normalized) maximum degree ě 2{5.

Note that unlike the previous results we do not require all vertices to have large degree, even on average, but just one. Also, this theorem covers the Petersen graph as well since it has (unnormalized) independence number 4. On the negative side, we have not been able to extend it to an open neighbourhood of 2{5 as the previous work did.

Finally, both conjectured extremal examples have girth 5. Theorem. The half-graph conjecture holds for all graphs of girth ě 5.

The rest of the paper is organized as follows. In Section 2 we give all necessary deﬁnitions. In Section 3 we re-state our results, mostly as a matter

of convenience. Section 4 is devoted to proofs, and we conclude in Section 5 with a few remarks and open questions.

## 2. Preliminaries

Unless speciﬁed otherwise, all graphs G in this paper are ﬁnite, simple and triangle-free. NGpvq is the neighbourhood of v, and n will always stand for the number of vertices. For disjoint sets of vertices X and Y , EpX, Y q is the set of cross-edges between X and Y ; likewise, EpXq is the set of edges induced by X.

A half in a graph G with n vertices is a function µ : V pGq ÝÑ r0, 1s such that

ř

vPVpGq µpvq “ n{2. We let

1 n2 ÿ

βpG, µq def“

µpuqµpvq

![image 26](<2021-razborov-more-about-sparse-halves_images/imageFile26.png>)

pu,vqPEpGq

and

βpGq def“ minpβpG, µq | µ is a halfq.

It is easy to see by a simple convexity argument that when n is even, the minimum is attained at a 0-1 half in which case we will also use the notation βpG, Aq, A P

`VpGq

˘

. When n is odd, it is attained at an almost 0-1 half µ,

n{2

that is µpv0q “ 1{2 for a single vertex v0 and µpvq P t0, 1u for all others. But the analytical form above is extremely handy in concrete constructions, as we shall see.

Conjecture 1 (Half-graph conjecture by Erdo˝s) βpGq ď 501 for any trianglefree graph G.

![image 27](<2021-razborov-more-about-sparse-halves_images/imageFile27.png>)

Let ρpGq and C4pGq be the edge density and the density of quadriliterals deﬁned consistently with ﬂag algebras. That is,

ρpGq def“

2|EpGq| n2

![image 28](<2021-razborov-more-about-sparse-halves_images/imageFile28.png>)

and in order to compute C4pGq we sample vi P V pGq pi P r4sq uniformly and completely independently (that is, with repetitions), form the graph on r4s

!

)

`r4s

˘

pi, jq P

and let C4pGq be the probability that it is isomorphic to C4.

| pvi, vjq P EpGq

with the set of edges

2

For v P V pGq we let

|NGpvq| n be the relative degree of v and

epvq def“

![image 29](<2021-razborov-more-about-sparse-halves_images/imageFile29.png>)

∆pGq def“ maxpepvq | v P V pGqq be the maximum degree, also relative. Likewise, αpGq def“ maxˆ

| A an independent set˙ is the relative independence number.

|A| n

![image 30](<2021-razborov-more-about-sparse-halves_images/imageFile30.png>)

We can assume w.lo.g. that αpGq ď 1{2 since otherwise Conjecture 1 is obvious. Thus,

ρpGq ď ∆pGq ď αpGq ď 1{2. (2) For sets of vertices A, B, C, D, E, . . . we will denote by pa, pb, pc, . . . their

densities:

|X| n

px def“

.

![image 31](<2021-razborov-more-about-sparse-halves_images/imageFile31.png>)

Let ρxy px ‰ y P ta, b, c, d, . . .u, X X Y “ Hq be the normalized density of cross-edges:

2|EpX, Y q| n2

ρxy def“

, and, likewise,

![image 32](<2021-razborov-more-about-sparse-halves_images/imageFile32.png>)

|EpXq| n2

ρx def“

. Finally, for v R X, let

![image 33](<2021-razborov-more-about-sparse-halves_images/imageFile33.png>)

|NGpvq X X| n

eXpvq def“

.

![image 34](<2021-razborov-more-about-sparse-halves_images/imageFile34.png>)

## 3. Results

In this section we collect in one place our main results stated in the introduction.

- Theorem 3.1 a) For any triangle-free graph G,


3 2

81 256

ρpGq2 ´

C4pGq ě

ρpGq (the bound is tight for the Clebsch graph).

![image 35](<2021-razborov-more-about-sparse-halves_images/imageFile35.png>)

![image 36](<2021-razborov-more-about-sparse-halves_images/imageFile36.png>)

b) For any triangle-free graph G without induced matchings of size 2,

C4pGq ě

(the bound is tight for C5).

3 2

ρpGq2 ´

![image 37](<2021-razborov-more-about-sparse-halves_images/imageFile37.png>)

6 25

ρpGq.

![image 38](<2021-razborov-more-about-sparse-halves_images/imageFile38.png>)

- Theorem 3.2 For any triangle-free graph G, βpGq ď 102427 .

![image 39](<2021-razborov-more-about-sparse-halves_images/imageFile39.png>)

- Theorem 3.3 Conjecture 1 is true for any triangle-free graph without induced matchings of size 2.
- Theorem 3.4 Conjecture 1 is true for any triangle-free graph with ρpGq ď

ρ0 def“ 33´

?161

![image 40](<2021-razborov-more-about-sparse-halves_images/imageFile40.png>)

![image 41](<2021-razborov-more-about-sparse-halves_images/imageFile41.png>)

116 .

Recall that a regular triangle-free graph G is strongly regular if |NGpvq X NGpwq| takes the same value c for all pairs pv, wq of non-adjacent vertices.

- Theorem 3.5 Conjecture 1 is true for any triangle-free strongly regular graph.
- Theorem 3.6 For any triangle-free graph G with αpGq ě 3{8 we have


βpGq ď

αpGq ˆ

- 1

![image 42](<2021-razborov-more-about-sparse-halves_images/imageFile42.png>)

- 2


- 1

![image 43](<2021-razborov-more-about-sparse-halves_images/imageFile43.png>)

- 2


´ αpGq˙.

Corollary 3.7 Conjecture 1 is true for any triangle-free graph with αpGq ě 2{5.

Theorem 3.8 Conjecture 1 is true for any triangle-free graph of girth ě 5.

## 4. Proofs

In this section we prove all our results. Some of the proofs, particularly in Sections 4.1 and 4.3, heavily rely on symbolic Maple computations. The corresponding worksheet, along with some supporting material, can be found at http://people.cs.uchicago.edu/˜razborov/ﬁles/halves.zip.

### 4.1. Flag-algebraic calculations

In this section we prove Theorem 3.1. As we remarked in Section 2, our notation for ﬁnite graphs is consistent with ﬂag algebras hence it is suﬃcient to prove the inequalities

3

![image 44](<2021-razborov-more-about-sparse-halves_images/imageFile44.png>)

- 2

ρ2 ´

81 256

![image 45](<2021-razborov-more-about-sparse-halves_images/imageFile45.png>)

ρ ď C4 (3)

- 3


6 25

ρ2 ´

ρ ď C4 ` 2M4 (4)

![image 46](<2021-razborov-more-about-sparse-halves_images/imageFile46.png>)

![image 47](<2021-razborov-more-about-sparse-halves_images/imageFile47.png>)

2

(M4 is the matching with two edges) in the theory TTF of triangle-free graphs and then apply them to the inﬁnite (balanced) blow-up of G.

We do it by a straightforward Cauchy-Schwartz computation in ﬂag algebras. Since quite a number of those have already appeared in the literature, with varying degree of informal explanation, we do ours matter-of-factly strictly adhering to the notation of [Raz07].

Let us start with (3); for that we need to consider triangle-free graphs on 8 vertices. We have |M8| “ 410 and |Fσ

6 | “ di, where d1 “ 110, d2 “ 81, d3 “ 67, d4 “ 46 and the types σi are shown on Figure 1 (with the exception of σ4, these are the same types employed in [HHK`12]). We enumerate ﬂags

i

3 4

3 4

1 2 1 2

1 2

E σ1 σ2

3 4

3 4

1 2

1 2

σ3 σ4

Figure 1: Types.

in Fσ

6 in a rather arbitrary order as Fσ

6 “ tFσ

1 , . . ., Fσ

di u and exhibit PSD

i

i

i

i

matrices Qi of size di ˆ di with rational coeﬃcients such that ÿ4

ÿdi

3 2

81 256

Qipj1, j2qFσ

- i
- j1 Fσ


ρ2 `

- i
- j2 σi !8 C4 ´


ρ, (5)

![image 48](<2021-razborov-more-about-sparse-halves_images/imageFile48.png>)

![image 49](<2021-razborov-more-about-sparse-halves_images/imageFile49.png>)

j1,j2“1

i“1

where !8 means coeﬃcient-wise comparison after expressing both sides of this inequality as linear combinations of the elements of M8.

The only further remark we want to make here is that the matrices Qi are degenerate and their co-ranks di ´ rkpQiq are equal to 2,2,5,4, respectively. This reﬂects the fact (and makes an excellent sanity check for our calculations) that the Clebsch graph GClebsch is an extremal conﬁguration for the inequality (5). Hence every strict homomorphism σi Ñ GClebsch gives rise to an element in the kernel of Qi. The actual computation is deferred to http://people.cs.uchicago.edu/˜razborov/ﬁles/halves.zip.

The inequality (4) is proved similarly, but this time we need only graphs on 6 vertices; on the other hand, instead of σ3 we need the type E. We have |M6| “ 38, |Fσ

6 | “ di, where d1 “ 12, d2 “ 10, d4 “ 7, and also |ME4 | “ 10. The computation has the form

i

ÿdi

ÿ10

6 25

3 2

ÿ

Ripj1, j2qFσ

- i
- j1 Fσ


ρ2`

REpj1, j2qFjE

FjE

- i
- j2 σi !6 C4`2M4´


2 E`

ρ.

![image 50](<2021-razborov-more-about-sparse-halves_images/imageFile50.png>)

![image 51](<2021-razborov-more-about-sparse-halves_images/imageFile51.png>)

1

j1,j2“1

j1,j2“1

iPt1,2,4u

The coeﬃcient 2 in front of M4 is rather arbitrary, we did no attempt to optimize on it. As this inequality is tight on C5, matrices RE, R1, R2, R4 also must be degenerate and indeed they have co-ranks 1,1,1,3, respectively.

### 4.2. Absolute lower bounds on βpGq

In this section we establish Theorems 3.2 and 3.3. As was already mentioned, they immediately follow from Theorem 3.1 and Proposition 1.1 so it only remains to prove the latter. This is simply a part of Krivilevich’s argument [Kri95], slightly re-phrased, but we include it here for the sake of completeness.

Let us start with considering an individual edge pv1, v2q P EpGq. Denote Ai def“ NGpviq, and let ei def“ epviqp“ pa

q; recall that ei ď 1{2 by (2). Let

i

pi def“

1{2 ´ ei 1 ´ e1 ´ e2

![image 52](<2021-razborov-more-about-sparse-halves_images/imageFile52.png>)

so that p1 ` p2 “ 1, and let B def“ V pGqzpA1 Y A2q. For i “ 1, 2 deﬁne the half µi by

$ ’&

1, if v P Ai pi, if v P B 0, if v P A3´i.

µipvq def“

’%

Then

- 2βpGq ď 2βpG, µ1q “ p1ρa

- 1,b ` p21ρb, (6)

2βpGq ď 2βpG, µ2q “ p2ρa

- 2,b ` p22ρb. (7)




Multiplying the ith inequality here by p3´i and adding them together, we get

1 4

pρ ´ C4Epv1, v2qq, where we denoted ρa

2βpGq ď p1p2pρa

1b ` ρa

2b ` ρbq “ p1p2pρ ´ ρa

1a2q ď

![image 53](<2021-razborov-more-about-sparse-halves_images/imageFile53.png>)

1a2 by C4Epv1, v2q to stress that this is the contribution of pv1, v2q to C4pGq. Finally, averaging this over all edges, we get

1 4

- 2

![image 54](<2021-razborov-more-about-sparse-halves_images/imageFile54.png>)

- 3


1 4

ρ ´ CE4 E “

pρ2 ´

C4q that is precisely Proposition 1.1.

2ρβpGq ď

![image 55](<2021-razborov-more-about-sparse-halves_images/imageFile55.png>)

![image 56](<2021-razborov-more-about-sparse-halves_images/imageFile56.png>)

### 4.3. Sparse graphs

- In this section we prove Theorem 3.4. As in the previous work [KS06], the analysis splits into two cases: ∆pGq ě 1{4 and ∆pGq ď 1{4.


The ﬁrst case is taken care of by the following variant of Proposition 1.1: Lemma 4.1

ρpGqp1 ´ 2∆pGqq 8p1 ´ ∆pGqq2

βpGq ď

.

![image 57](<2021-razborov-more-about-sparse-halves_images/imageFile57.png>)

Proof. Pick v P V pGq with epvq “ ∆ pdef“ ∆pGqq, and let A def“ NGpvq (so that pa “ ∆) and B “ NGpvqzA. Construct the following halves µ0 and µ1:

- µ0pwq def“ #

0, if w P A

- 1

![image 58](<2021-razborov-more-about-sparse-halves_images/imageFile58.png>)

- 2p1´∆q, if w P B


- µ1pwq def“ #


1, if w P A

1{2´∆

1´∆ , if w P B

![image 59](<2021-razborov-more-about-sparse-halves_images/imageFile59.png>)

Then

- 2βpGq ď 2βpG, µ0q “

ρb 4p1 ´ ∆q2

![image 60](<2021-razborov-more-about-sparse-halves_images/imageFile60.png>)

(8)

- 2βpGq ď 2βpG, µ1q “


1 ´ ∆ ˙2 ρb. (9) Multiplying (9) by 1 ´ 2∆ and adding it to (8), we get

ρab ` ˆ

1{2 ´ ∆ 1 ´ ∆

1{2 ´ ∆

![image 61](<2021-razborov-more-about-sparse-halves_images/imageFile61.png>)

![image 62](<2021-razborov-more-about-sparse-halves_images/imageFile62.png>)

1 ´ 2∆ 2p1 ´ ∆q

1 ´ 2∆ 2p1 ´ ∆q

pρab ` ρbq “

ρpGq.

4p1 ´ ∆qβpGq ď

![image 63](<2021-razborov-more-about-sparse-halves_images/imageFile63.png>)

![image 64](<2021-razborov-more-about-sparse-halves_images/imageFile64.png>)

![image 65](<2021-razborov-more-about-sparse-halves_images/imageFile65.png>)

Now, the function 8pp11´´2∆∆ q

2q is decreasing for ∆ P r1{4, 1{2s, hence ∆pGq ě 1{4 implies βpGq ď ρp9Gq and then Theorem 3.4 follows since ρ0 ď 509 .

![image 66](<2021-razborov-more-about-sparse-halves_images/imageFile66.png>)

![image 67](<2021-razborov-more-about-sparse-halves_images/imageFile67.png>)

![image 68](<2021-razborov-more-about-sparse-halves_images/imageFile68.png>)

The case ∆pGq ď 1{4 is more diﬃcult. As in the proof of Proposition 1.1, let us ﬁrst consider an individual edge pv1, v2q P EpGq (but this time we will not randomize over this choice but will pick it up in a way to be speciﬁed later). We will re-use the notation ei, Ai, B, pi from that proof so that we still have the bounds (6), (7). But now the condition ∆pGq ď 1{4 allows us to form one more half

µ0pGq def“ #

1, if v P A1 Y A2 q, if v P B,

where

1{2 ´ e1 ´ e2 1 ´ e1 ´ e2

p0 def“

. This leads to the extra bound

![image 69](<2021-razborov-more-about-sparse-halves_images/imageFile69.png>)

2bq ` p20ρb. (10)

2βpGq ď ρa

1a2 ` p0pρa

1b ` ρa

We are now looking for non-negative coeﬃcients α0, α1, α2 such that multiplying by them (10), (6) and (7), respectively, and adding up the results, we will equalize the coeﬃcients in front of ρa

2b, ρb. For that purpose we set

1a2, as well as ρa

1b, ρa

- α0 def“ p1 ´ 2e1q2p1 ´ 2e2q
- α1 def“ p1 ´ 2e1qp1 ´ 2e2q
- α2 def“ 2p1 ´ 2e1qe2.


Then (see the Maple worksheet) 4p1 ´ 2e1qp1 ´ e1 ´ e2 ` 2e1e2qβpGq ď α0pρa

2b ` ρbq “ pα0 ´ γqpρa

1a2 ` ρa

1bq ` γpρa

2b ` ρbq “ pα0 ´ γqpρa

1a2 ` ρa

1b ` ρa

1a2 ` ρa

1bq ` γpρa

1bq ` γρ, where

1a2 ` ρa

p1 ´ 2e1qp1 ´ 2e2qp1 ´ 4e1 ` 4e21 ` 4e1e2q 2p1 ´ e1 ´ e2q

γ def“

. Note for the record that

![image 70](<2021-razborov-more-about-sparse-halves_images/imageFile70.png>)

p1 ´ 2e1qp1 ´ 2e2qp1 ´ 2e1 ´ 2e2q 2p1 ´ e1 ´ e2q

α0 ´ γ “

ě 0

![image 71](<2021-razborov-more-about-sparse-halves_images/imageFile71.png>)

since e1, e2 ď ∆pGq ď 1{4. Hence we need an upper bound on ρa

1a2 ` ρa

1b.

For that purpose we now specify v1, v2. The vertex v is chosen as the vertex of the maximum degree so that e1 “ ∆. We choose v2 to have maximum degree among all vertices in NGpv1q. The latter choice gives us the estimate ρa

1a2 ` ρa

1b ď 2∆e2 since ρa

1a2 ` ρa

1b is simply the overall density of edges incident to A1. Putting all this together, we arrive at the estimate

βpGq ď fpρ, ∆, e2q def“

p1 ´ 2e2qp4∆2ρ ´ 4∆2e2 ` 4∆ρe2 ´ 4∆e22 ´ 4∆ρ ` 2∆e2 ` ρq 8p1 ` 2∆e2 ´ ∆ ´ e2qp1 ´ ∆ ´ e2q

.

![image 72](<2021-razborov-more-about-sparse-halves_images/imageFile72.png>)

Let us also remind that we have the constraints 0 ď ρ, e2 ď ∆ ď 1{4.

This optimization problem is a bit nasty to be fully analyzed, i.e. give an analytical estimate on βpGq in terms of ρpGq. Instead, we compute

Qpρ, ∆, e2q 200p1 ´ ∆ ´ e2qp1 ´ ∆ ´ e2 ` 2∆pe2qq

1 50

´ fpρ, ∆, e2q “

,

![image 73](<2021-razborov-more-about-sparse-halves_images/imageFile73.png>)

![image 74](<2021-razborov-more-about-sparse-halves_images/imageFile74.png>)

where Q is a polynomial. Our goal is to show that ρ ď ρ0 implies Qpρ, ∆, e2q ě 0.

We note that Qpρ0, ρ0, ρ0q “ 0 and that individual degrees of Q in ρ, ∆, e2 are 1, 2 and 3, respectively.

We ﬁrst compute

BQ Bρ

“ ´25p1 ´ 2e2qp4∆2 ` 4∆e2 ´ 4∆ ` 1q ď ´25p1 ´ 2e2qp1 ´ 2∆q2 ď 0.

![image 75](<2021-razborov-more-about-sparse-halves_images/imageFile75.png>)

Hence it is suﬃcient to prove that

Q1p∆, e2q def“ Qpminpρ0, ∆q, ∆, e2q ě 0.

Q1 is no longer smooth in ∆ but it is still a cubic polynomial in e2. We consider two cases: e2 ď ρ0 and e2 ě ρ0.

If e2 ď ρ0 then we consider Taylor’s coeﬃcients at e2 “ ρ0:

BrQ1p∆, e2q pBe2qr ˇ

1 r!

pr “ 0..3q,

![image 76](<2021-razborov-more-about-sparse-halves_images/imageFile76.png>)

![image 77](<2021-razborov-more-about-sparse-halves_images/imageFile77.png>)

e2“ρ0

and it turns out (see the Maple worksheet) that they are non-negative for even r and negative for odd r. The required inequality Q1p∆, e2q ě 0 follows.

In the second case e2 ě ρ0 we also have ∆ ě ρ0 and hence Q1p∆, e2q “ Qpρ0, ∆, e2q is a quadratic polynomial in ∆ P re2, 1{4s. It should be noted that it can be either convex or concave. But in either case the required inequality Q1p∆, e2q ě 0 follows from Q1pe2, e2q ě 0, Q1p1{4, e2q ě 0 and BQ1 B∆ |∆“e

ě 0.

![image 78](<2021-razborov-more-about-sparse-halves_images/imageFile78.png>)

2

### 4.4. Strongly regular case

- In this section we prove Theorem 3.5. For a brief background on triangle-free strongly regular (TFSR in what follows) graphs we follow [Big09].


Except for the complete bipartite graphs Kn,n (for which Erd˝os’s conjecture is vacuously true), there are seven known examples of TFSR graphs; the cycle C5, the Petersen graph and the Clebsch graph being the smallest. The obvious parameters of a TFSR graph G are n, k (the degree of a vertex) and c (the number of common neighbours of a pair of non-adjacent vertices). They are actually related as

n “ 1 `

k c

pk ´ 1 ` cq.

![image 79](<2021-razborov-more-about-sparse-halves_images/imageFile79.png>)

From now on we assume that G is diﬀerent from Kn,n and that it is diﬀerent from C5. Then the quantity s def“

a

![image 80](<2021-razborov-more-about-sparse-halves_images/imageFile80.png>)

c2 ` 4pk ´ cq is an integer, and the only positive eigenvalue of the adjacency matrix diﬀerent from k is given by q def“ s´2c. It is also an integer such that

![image 81](<2021-razborov-more-about-sparse-halves_images/imageFile81.png>)

1 ď c ď qpq ` 1q. (11)

Furthermore, we have

k “ pq ` 1qc ` q2, hence k and n are rational functions in c and q. In particular, we compute

k n

ρpGq “

![image 82](<2021-razborov-more-about-sparse-halves_images/imageFile82.png>)

cpqc ` q2 ` cq pqc ` q2 ` 2c ` qqpqc ` q2 ` c ´ qq

def“ Qpq, cq.

“

![image 83](<2021-razborov-more-about-sparse-halves_images/imageFile83.png>)

Let us now analyze this expression. Firstly,

qpq ` 1qpc2q2 ` 2cq3 ` q4 ` c2q ´ q3 ´ c2 ´ 2qcq pqc ` q2 ` 2c ` qq2pqc ` q2 ` c ´ qq2

BQ Bc

“

ě 0,

![image 84](<2021-razborov-more-about-sparse-halves_images/imageFile84.png>)

![image 85](<2021-razborov-more-about-sparse-halves_images/imageFile85.png>)

hence Q is increasing in c. Next, let

q2 ` 3q ` 1 qpq ` 3q2 (this corresponds to so-called Krein graphs). Then

Q1pqq def“ Qpq, qpq ` 1qq “

![image 86](<2021-razborov-more-about-sparse-halves_images/imageFile86.png>)

q3 ` 3q3 ` 3q ` 3 q2pq ` 3q3

Q1pqq1 “ ´

ă 0,

![image 87](<2021-razborov-more-about-sparse-halves_images/imageFile87.png>)

hence Q1pqq is decreasing. As Q1p4q “ 19629 ă ρ0, the proof of Theorem 3.5 boils down to the three cases q “ 1, 2, 3: all others are taken care of by

![image 88](<2021-razborov-more-about-sparse-halves_images/imageFile88.png>)

Theorem 3.4.

- When q “ 1, we have either the Petersen graph (c “ 1) or the Clebsch

graph (c “ 2). Conjecture 1 for the Clebsch graph is veriﬁed by the half pNGpuq Y NGpvqqztu, vu, where pu, vq is an arbitrary edge.

- When q “ 2, we have Qp2, 1q “ 507 ă ρ0 (this is the Hoﬀman-Singleton


![image 89](<2021-razborov-more-about-sparse-halves_images/imageFile89.png>)

graph) hence it is suﬃcient to consider the cases 2 ď c ď 6. Well-known “arithmetic conditions” rule out c P t3, 5u [Big09, Table 1], and the three other cases correspond precisely to the remaining known TFSR graphs: Gewirtz, M22 and Higman-Sims (they are unique for their values of c, q [Gew69b, Bro83, Gew69a]).

For the Gewirtz graph, we pick up four vertices v1, v2, v3, v4 spanning an induced matching with two edges and consider the half (see the Maple worksheet)

Ť4

i“1 NGpuiqztu1, u2, u3, u4u. It spans 51 edges which proves βpGq ď 0.017.

When G is the M22 graph, we similarly let A def“

Ť3

i“1 NGpuiqztu1, u2, u3u, where pu1, u2q P EpGq and u3 R NGpu1q Y NGpu2q. Then |A| “ 38 and |EpAq| “ 109. Moreover, there exists a vertex v R A such that |NGpvqXA| “ 9. Adding to A half of the vertex v, we get a half witnessing βpGq ď 0.0192.

For the Higman-Sims graph we present an ad hoc half achieving βpGq ď

- 1


50 ´ 10´4. It was found by a simple optimization program remarkably suggesting that this bound is actually tight. If it is true (we did not attempt

![image 90](<2021-razborov-more-about-sparse-halves_images/imageFile90.png>)

to verify the claim with a rigorous argument) then the Higman-Sims graph comes very close to the bound in Erd˝os’s conjecture.

Finally, when q “ 3 we have Qp3, 11q “ 3350583 ă ρ0. Hence the only case to consider is q “ 3, c “ 12 i.e. a hypothetical 57-regular Krein graph on 324 vertices. A simple solution is to note that such a graph is known not to exist [GM05, KO07]. Let us, however, sketch another argument due to Grzesik and Volec (unpublished) that in our opinion is more instructive and may be of independent interest.

![image 91](<2021-razborov-more-about-sparse-halves_images/imageFile91.png>)

As we already noticed, in the bound (10) the quantity ρb can be eliminated via the identity ρ “ ρa

2b ` ρb. If G is also known to be regular, then p0 “ 11{2´´22ρρ and ρa

1a2 ` ρa

1b ` ρa

1a2 “ 2ρ2. Plugging all this into (10) and averaging over all choices of the edge pv1, v2q, as in Section 4.2, we arrive at the bound

ib ` ρa

ib can be also eliminated using ρa

![image 92](<2021-razborov-more-about-sparse-halves_images/imageFile92.png>)

- 2

![image 93](<2021-razborov-more-about-sparse-halves_images/imageFile93.png>)

- 3C4 ` ρ2p1 ´ 4ρq 8ρp1 ´ 2ρq2


βpGq ď

![image 94](<2021-razborov-more-about-sparse-halves_images/imageFile94.png>)

(12)

that holds for any regular (triangle-free) graph G. Now, if G is also strongly regular then C4pGq can be easily calculated as

C4pGq “

3 n3

pk2 ` c2pn ´ k ´ 1qq

![image 95](<2021-razborov-more-about-sparse-halves_images/imageFile95.png>)

(recall from Section 2 that C4pGq counts degenerated cycles as well!) Substituting this into (12), we get

cpcq ` q2 ´ cq 8qpq ` 1qpc ` qqpc ` q ´ 1q

βpGq ď

.

![image 96](<2021-razborov-more-about-sparse-halves_images/imageFile96.png>)

In particular, when q “ 3, c “ 12 we have βpGq ď 56011 .

![image 97](<2021-razborov-more-about-sparse-halves_images/imageFile97.png>)

### 4.5. Graphs with large independence number

In this section we prove Theorem 3.6; as we noted in the introduction, for α ě 2{5 it generalizes several previously known results.

It will be convenient to assume that n is even: this can be always achieved by replacing each vertex with two identical twins. Let A Ď V pGq be an independent set with pa “ α ě 3{8. We build a larger set B Ě A by recursively adding to it vertices that bring with them only a few edges. More exactly, apply the following simple algorithm:

![image 98](<2021-razborov-more-about-sparse-halves_images/imageFile98.png>)

![image 99](<2021-razborov-more-about-sparse-halves_images/imageFile99.png>)

![image 100](<2021-razborov-more-about-sparse-halves_images/imageFile100.png>)

B :“ A while |B| ă n{2 and Dv R B

eBpvq ď 21 ´ α do B :“ B Y tvu. ˘

`

![image 101](<2021-razborov-more-about-sparse-halves_images/imageFile101.png>)

![image 102](<2021-razborov-more-about-sparse-halves_images/imageFile102.png>)

If this algorithm terminates since B reaches size n{2 then βpG, Bq ď `1

˘2

since α ě 83 ą 13 and we are done. Hence we can assume w.l.o.g. that the algorithm stops when the required vertex v no longer exists. Thus, we now have a set B such that:

`1 2 ´ α

which is ď 12α

˘

2 ´ α

![image 103](<2021-razborov-more-about-sparse-halves_images/imageFile103.png>)

![image 104](<2021-razborov-more-about-sparse-halves_images/imageFile104.png>)

![image 105](<2021-razborov-more-about-sparse-halves_images/imageFile105.png>)

![image 106](<2021-razborov-more-about-sparse-halves_images/imageFile106.png>)

![image 107](<2021-razborov-more-about-sparse-halves_images/imageFile107.png>)

$ ’&

pb P rα, 1{2s ρb ď 2

`1 2 ´ α

˘

(13)

ppb ´ αq @v R B

![image 108](<2021-razborov-more-about-sparse-halves_images/imageFile108.png>)

eBpvq ą 21 ´ α

’%

˘

`

.

![image 109](<2021-razborov-more-about-sparse-halves_images/imageFile109.png>)

Let

pb 2 )

!

C def“

v R B ˇ eBpvq ą

.

![image 110](<2021-razborov-more-about-sparse-halves_images/imageFile110.png>)

Then C is independent (as any two vertices of C have a common neighbor in B). Hence pc ď α from the deﬁnition of αpGq. This allows us to choose a set of vertices D disjoint from both B and C and such that pd “ 1 ´ α ´ pb. We now consider two cases, depending on whether there exists a vertex in B that has many neighbors in D or not.

- Case 1. There exists v P B such that eDpvq ě 21 ´ pb. Pick up arbitrarily E Ď NGpvqXD with pe “ 21 ´pb; note that E Ď NGpvq


![image 111](<2021-razborov-more-about-sparse-halves_images/imageFile111.png>)

![image 112](<2021-razborov-more-about-sparse-halves_images/imageFile112.png>)

is independent. Also, for every v P E we have eBpvq ď p

2 since E Ď D. Then we have (note the absence of the coeﬃcient 2 in the last term!)

b

![image 113](<2021-razborov-more-about-sparse-halves_images/imageFile113.png>)

2βpG, B Y Eq ď 2 ˆ

- 1

![image 114](<2021-razborov-more-about-sparse-halves_images/imageFile114.png>)

- 2


´ α˙ppb ´ αq ` pb ˆ

- 1

![image 115](<2021-razborov-more-about-sparse-halves_images/imageFile115.png>)

- 2


´ pb˙.

The right-hand side is a concave quadratic function in pb, with maximum at pb “ 34 ´ α which is ď α since we assumed α ě 3{8. Hence, since pb ě α we can plug in pb :“ α and this completes the analysis of Case 1.

![image 116](<2021-razborov-more-about-sparse-halves_images/imageFile116.png>)

- Case 2. For any v P B we have eDpvq ď 12 ´ pb. This case is slightly more elaborate. Let us ﬁrst ﬁx an individual v0 P B


![image 117](<2021-razborov-more-about-sparse-halves_images/imageFile117.png>)

(we will later average over this choice). Let E def“ NGpv0q X D (so that pe ď 21 ´ pb) and F def“ DzNGpv0q; thus, D “ E Y. F with E independent. Consider the half

![image 118](<2021-razborov-more-about-sparse-halves_images/imageFile118.png>)

$ ’&

1 if v P B Y E p if v P F 0 in all other cases,

µpvq def“

’%

where

1{2 ´ pb ´ pe pf

p “

. Then

![image 119](<2021-razborov-more-about-sparse-halves_images/imageFile119.png>)

2βpG, µq “ ρb ` ρbe ` pρbf ` pρef ` p2ρf. The bound on ρb is given by (13), and we have ρbf ď pbpf; the coeﬃcient

- 2 is absent for the same reasons as above. For ρef we use the trivial bound


2 f

ρef ď 2pepf and, ﬁnally ρf ď p

2 simply because G is triangle-free. Plugging all this into the above bound (we leave ρbe alone for the time being) we get

![image 120](<2021-razborov-more-about-sparse-halves_images/imageFile120.png>)

- `1 2 ´ α

![image 121](<2021-razborov-more-about-sparse-halves_images/imageFile121.png>)

˘

ppb ´ αq ` ρbe ` pb

`1 2 ´ pb ´ pe

![image 122](<2021-razborov-more-about-sparse-halves_images/imageFile122.png>)

˘

- `2pe


$ ’&

2βpG, µq ď 2

˘2 “ 2

`1 2 ´ pb ´ pe

` 21

`1 2 ´ pb ´ pe

˘

![image 123](<2021-razborov-more-about-sparse-halves_images/imageFile123.png>)

![image 124](<2021-razborov-more-about-sparse-halves_images/imageFile124.png>)

![image 125](<2021-razborov-more-about-sparse-halves_images/imageFile125.png>)

(14)

ppb ´ αq ` 21

`1 2 ´ pb ´ pe

˘`1 2 ` pb ` 3pe

`1 2 ´ α

˘

˘ `ρbe.

![image 126](<2021-razborov-more-about-sparse-halves_images/imageFile126.png>)

![image 127](<2021-razborov-more-about-sparse-halves_images/imageFile127.png>)

![image 128](<2021-razborov-more-about-sparse-halves_images/imageFile128.png>)

![image 129](<2021-razborov-more-about-sparse-halves_images/imageFile129.png>)

’%

In this bound, pe and ρbe are the only quantities that depend on the choice of v0 P B, and we now randomize over all such choices.

The bound (14) is concave in pe hence we may simply replace pe with its expected value ρ

2pb.

bd

![image 130](<2021-razborov-more-about-sparse-halves_images/imageFile130.png>)

As for ρbe, pick w PR D uniformly at random; then by a standard double counting we see that

2pd pb

eBpwq2

“

‰

Erρbes “

E

. But we also know that

![image 131](<2021-razborov-more-about-sparse-halves_images/imageFile131.png>)

- 1

![image 132](<2021-razborov-more-about-sparse-halves_images/imageFile132.png>)

- 2


pb 2

´ α ď eBpwq ď

,

![image 133](<2021-razborov-more-about-sparse-halves_images/imageFile133.png>)

where the ﬁrst inequality comes from (13) while the second follows from D X C “ H. Moreover,

ρbd 2pd

EreBpwqs “

. Estimating the second moment in a standard way, we get E

![image 134](<2021-razborov-more-about-sparse-halves_images/imageFile134.png>)

ρbd 2pd ˆ

pb 2 ˙ ´

pb 2 ˆ

´ α˙.

- 1

![image 135](<2021-razborov-more-about-sparse-halves_images/imageFile135.png>)

- 2


- 1

![image 136](<2021-razborov-more-about-sparse-halves_images/imageFile136.png>)

- 2


eBpwq2

“

‰

ď

´ α `

![image 137](<2021-razborov-more-about-sparse-halves_images/imageFile137.png>)

![image 138](<2021-razborov-more-about-sparse-halves_images/imageFile138.png>)

![image 139](<2021-razborov-more-about-sparse-halves_images/imageFile139.png>)

Finally, plugging all our ﬁndings into (13), we get β ď Qpα, pb, ρbdq

8α2p2b ´ 24αp3b ´ 4p4b ` 4αp2b ´ 8αpbρbd ` 12p3b ´ 4p2bρbd ´ 3p2b ` 6pbρbd ´ 3ρ2bd 16p2b (see the Maple worksheet).

def“

![image 140](<2021-razborov-more-about-sparse-halves_images/imageFile140.png>)

Q is quadratic concave in ρbd and, as before, ρbd ď pbpd “ pbp1 ´ α ´ pbq since D X C “ H. Moreover,

Hence

BQ Bρbdˇ

“

![image 141](<2021-razborov-more-about-sparse-halves_images/imageFile141.png>)

ρbd“pbpd

Qpα, pb, ρbdq ď Qpα, pb, pbp1´α´pbqq “

pb ´ α 8pb

ě 0.

![image 142](<2021-razborov-more-about-sparse-halves_images/imageFile142.png>)

9 8

13 16

α2´

![image 143](<2021-razborov-more-about-sparse-halves_images/imageFile143.png>)

![image 144](<2021-razborov-more-about-sparse-halves_images/imageFile144.png>)

αpb´

3 16

1 4

p2b´

α`

![image 145](<2021-razborov-more-about-sparse-halves_images/imageFile145.png>)

![image 146](<2021-razborov-more-about-sparse-halves_images/imageFile146.png>)

- 1

![image 147](<2021-razborov-more-about-sparse-halves_images/imageFile147.png>)

- 2


pb def“ Q1pα, pbq.

Finally, Q1 is quadratic concave in pb and BQ

“ 1´23α ă 0 (as α ě 38). Since pb ě α, we get Q1pα, pbq ď Q1pα, αq “ α2

1

![image 148](<2021-razborov-more-about-sparse-halves_images/imageFile148.png>)

![image 149](<2021-razborov-more-about-sparse-halves_images/imageFile149.png>)

![image 150](<2021-razborov-more-about-sparse-halves_images/imageFile150.png>)

Bpb ˇ

pb“α

`1 2 ´ α

˘

. This completes the proof.

![image 151](<2021-razborov-more-about-sparse-halves_images/imageFile151.png>)

![image 152](<2021-razborov-more-about-sparse-halves_images/imageFile152.png>)

### 4.6. Graphs of girth ě 5

In this section we prove Theorem 3.8, and for this particular proof we resort to absolute sizes of the sets involved rather than their densities. The reason is that the girth assumption does not survive blowing up a graph, and this makes the density-based language unnatural.

So we ﬁx a triangle-free graph G with gpGq ě 5, |V pGq| “ n, and let v0 P V pGq be a vertex of the maximum degree k. We may assume that k ď n´21

![image 153](<2021-razborov-more-about-sparse-halves_images/imageFile153.png>)

(otherwise the result is trivial) and also that G is a minimal counterexample to Erd˝os’s conjecture, that is βpG˚q ď 501 for any proper induced subgraph G˚ of G. We let

![image 154](<2021-razborov-more-about-sparse-halves_images/imageFile154.png>)

A def“ NGpv0q, B def“ V pGqzptv0u Y Aq. Then gpGq ě 5 implies

@v P Bp|NGpvq X A| ď 1q. (15)

We now apply the minimality assumption to the induced subgraph G|B. This gives us a function ν : B ÝÑ r0, 1s such that

#

vPB νpvq “ n´2k´1

![image 155](<2021-razborov-more-about-sparse-halves_images/imageFile155.png>)

2

pu,vqPEpBq νpuqνpvq ď pn´k´1q

ř

50 .

![image 156](<2021-razborov-more-about-sparse-halves_images/imageFile156.png>)

We use it to deﬁne a half µ in the whole graph G as follows:

(16)

$ ’&

- 0, v “ v0
- 1, v P A pνpvq, v P B,


µpvq def“

’%

where

n ´ 2k n ´ k ´ 1

p def“

. Then we have

![image 157](<2021-razborov-more-about-sparse-halves_images/imageFile157.png>)

˜

µpuqµpvq¸. (17)

pn ´ 2kq2 50

1 n2

ÿ

`

βpG, µq ď

![image 158](<2021-razborov-more-about-sparse-halves_images/imageFile158.png>)

![image 159](<2021-razborov-more-about-sparse-halves_images/imageFile159.png>)

pu,vqPEpA,Bq

ř

pu,vqPEpA,Bq µpuqµpvq. Firstly, by (15) we have

We will employ two diﬀerent methods of bounding the term

n 2

ÿ

ÿ

µpuqµpvq ď

µpvq “

´ k

![image 160](<2021-razborov-more-about-sparse-halves_images/imageFile160.png>)

vPB

pu,vqPEpA,Bq

and thus #

´

¯

pn´2kq2

βpG, µq ď n1

50 ` n2 ´ k

![image 161](<2021-razborov-more-about-sparse-halves_images/imageFile161.png>)

![image 162](<2021-razborov-more-about-sparse-halves_images/imageFile162.png>)

![image 163](<2021-razborov-more-about-sparse-halves_images/imageFile163.png>)

2

(18)

“ 501 ´ 5n1

pnp4k ´ 25q ` 50k ´ 4k2q.

![image 164](<2021-razborov-more-about-sparse-halves_images/imageFile164.png>)

![image 165](<2021-razborov-more-about-sparse-halves_images/imageFile165.png>)

2

We now start a case analysis.

- Case 1. k ě 7. In this case, since n ě 2k ` 1, we have np4k ´ 25q ` 50k ´ 4k2 ě p2k `

1qp4k ´ 25q ` 50k ´ 4k2 “ 4k2 ` 4k ´ 25 ě 0, and we are done by (18).

- Case 2. k ď 6. This time, the same condition np4k ´ 25q ` 50k ´ 4k2 ă 0 (that can be


assumed w.l.o.g.) provides a new lower bound on n

n ě R

25 ´ 4k V. (19) To get an upper bound on n, we estimate the term

2kp25 ´ 2kq

![image 166](<2021-razborov-more-about-sparse-halves_images/imageFile166.png>)

ř

pu,vqPEpA,Bq µpuqµpvq

- as pk ´ 1qk, simply because the degree of any vertex in A is ď k, and all of


- them are adjacent to v0 R B. Thus

βpG, µq ď

1 n2 ˆ

![image 167](<2021-razborov-more-about-sparse-halves_images/imageFile167.png>)

pn ´ 2kq2 50

![image 168](<2021-razborov-more-about-sparse-halves_images/imageFile168.png>)

` pk ´ 1qk˙ “

1 50

![image 169](<2021-razborov-more-about-sparse-halves_images/imageFile169.png>)

´

k 25n2

![image 170](<2021-razborov-more-about-sparse-halves_images/imageFile170.png>)

p2n ` 25 ´ 27kq.

Hence we can also assume that

n ď R

27 2

![image 171](<2021-razborov-more-about-sparse-halves_images/imageFile171.png>)

pk ´ 1qV (20)

which immediately rules out the case k “ 1. Also, (19) and (20) rule out the case k “ 6 as well which leaves us with the possibilities k “ 2, 3, 4, 5 and 80 potential values for the pair pk, nq.

Instead of trying to do the remaining analysis manually, we employ a diﬀerent strategy. Namely, we record our argument in the form of “unprocessed” (and recursive) bounds, without attempting to simplify them, and

- then we simply feed the formulas to Maple to ﬁnish the job.


To start with, let C def“ V pGqzpAYNGpAqq be the set of vertices at distance ě 3 from v0; note that

|C| ě n ´ k2 ´ 1.

Let Rp3, uq be the oﬀ-diagonal Ramsey number; we will only use the following well-known small values:

Rp3, 0q “ 0, Rp3, 1q “ 1, Rp3, 2q “ 3, Rp3, 3q “ 6, Rp3, 4q “ 9, Rp3, 5q “ 14.

For every u P r0, rn{2 ´ kss such that Rp3, uq ď n ´ k ´ 1 p“ |B|q we are going to derive its own bound βpGq ď βu, and then we will minimize over all choices of u. So let us ﬁx for the time being some u with the above properties.

` B

˘

Pick a subset Bu P

with the only restriction that it contains as many vertices in C as possible. Then we have

Rp3,uq

|EpA, Buq| “ |BuzC| “ Rp3, uq ´ |C| ď Rp3, uq ´ pn ´ k2 ´ 1q, (21)

where x´y def“ maxp0, x´yq. Finally, let Bu1 Ď Bu be an independent subset of size u existing by the deﬁnition of Ramsey numbers. Further analysis splits into two more cases.

- Case 2.1. u “ rn{2 ´ ks.

If n is even, we take the half A Y B1

u. If n is odd, we can assume w.l.o.g. that B1

uXNGpAq ‰ H (as otherwise we are done). Let µ be the half obtained from A Y Bu1 by removing half a vertex in Bu1 X NGpAq; this will give us an extra saving of half-edge.

We have two diﬀerent estimates on |EpA, B1

uq|: one follows from (21) and, on the other hand we, like before, have the trivial bound |EpA, B1

uq| ď n{2 ´ k ď u coming from (15). Summarizing,

$ ’&

’%

βpGq ď βu def“ n1

![image 172](<2021-razborov-more-about-sparse-halves_images/imageFile172.png>)

2

`

minpu, Rp3, uq ´ pn ´ k2 ´ 1qq ´ 21pn mod 2q

![image 173](<2021-razborov-more-about-sparse-halves_images/imageFile173.png>)

˘ pu “ rn{2 ´ ksq.

(22)

Let us stress that this bound is deﬁned only when Rp3, rn{2 ´ ksq ď n´k´1.

- Case 2.2. u ă rn{2 ´ ks. In this case we have2


βpGq ď βu def“ γpk, n, k ` u, minpu, Rp3, uq ´ pn ´ k2 ´ 1qqq, (23) where the function γpk, n, t, eq pt ď n{2q abstracts our situation as follows:

γpk, n, t, eq def“ max

βpG, µq pt ď tn{2uq.

min

G,A

µ|A”1

Here G runs over all graphs with n vertices and ∆pGq ď k, A runs over all sets of vertices with |A| “ t and |EpAq| ď e and µ runs over all halves

![image 174](<2021-razborov-more-about-sparse-halves_images/imageFile174.png>)

2We do not need the half-edge saving from the previous case.

containing A. What remains is to give suﬃciently good (for our purposes) recursive bounds on γ.

First of all, when n is even and t “ n{2, we clearly have γpk, n, n{2, eq “

e n2

pn is evenq. (24)

![image 175](<2021-razborov-more-about-sparse-halves_images/imageFile175.png>)

Next, assume that n is odd and t “ n´21. Fix the worst-case G, A, and let e˚ ď e be the actual number of edges in G|A. Then |EpA, V pGqzAq| has

![image 176](<2021-razborov-more-about-sparse-halves_images/imageFile176.png>)

- at most kt ´ 2e˚ edges. Hence there exists a vertex v R A with


kt ´ 2e˚

|NGpV q X A| ď Z

n ´ t ^. (25) Adding to A half of that vertex, we conclude

![image 177](<2021-razborov-more-about-sparse-halves_images/imageFile177.png>)

1 n2 ˆe˚ `

γpk, n, t, eq ď max

![image 178](<2021-razborov-more-about-sparse-halves_images/imageFile178.png>)

0ďe˚ďe

kt ´ 2e˚ n ´ t ^˙ pn odd, t “

- 1

![image 179](<2021-razborov-more-about-sparse-halves_images/imageFile179.png>)

- 2 Z


![image 180](<2021-razborov-more-about-sparse-halves_images/imageFile180.png>)

n ´ 1 2

q. (26)

![image 181](<2021-razborov-more-about-sparse-halves_images/imageFile181.png>)

Similarly, for smaller values of t we apply recursion by letting A :“ AYtvu, where v is he vertex satisfying (25). This gives us

γpk, n, t, eq ď γ ˆk, n, t ` 1, max

0ďe˚ďe

kt ´ 2e˚ n ´ t ^˙˙ pt ă tn{2uq. (27)

ˆe˚ ` Z

![image 182](<2021-razborov-more-about-sparse-halves_images/imageFile182.png>)

This completes our description of βu in the case 2.2. Finally, the “master formula” now reads as

βpGq ď mintβu | 0 ď u ď rn{2 ´ ks ^ Rp3, uq ď n ´ k ´ 1u. (28)

The bounds (28), (22), (23), along with recursive estimates (24), (26), (27) on the auxiliary function γ suﬃce to complete the analysis of the 80 remaining cases. See the Maple worksheet for details.

## 5. Conclusion

In this paper we have proved several partial results on Erd˝os’s half-graph conjecture. While they make this conjecture even more plausible, it still remains wide open. The same is true for the last of Erd˝os’s conjectures on

this subject: prove that any triangle-free graph on n vertices can be made bi-partite by removing at most n252 edges.

![image 183](<2021-razborov-more-about-sparse-halves_images/imageFile183.png>)

As for intermediate, and probably more accessible, goals we would like to ask to extend Theorem 3.6 to a neighbourhood of the critical value α “ 2{5, i.e. prove the half-graph conjecture for triangle-free graphs G with αpGq ě 2{5 ´ ǫ for a ﬁxed constant ǫ ą 0. As we noted above, such an improvement if known for the minimum degree and the average degree [Kri95, KS06].

We have highlighted the extremal problem of ﬁnding the minimal density of quadriliterals in triangle-free graphs with given edge density and have given its applications to the sparse half problem. Since this quantity can be viewed (actually, in a quite precise sense) as the measure of non-randomness in a graph, perhaps it might be worth studying in its own right.

## Acknowledgment

I would like to thank Andrzej Grzesik and Jan Volec for pointing out the references [GM05, KO07] and for sharing with me the alternate argument sketched at the end of Section 4.4.

## References

[BCL21] J. Balogh, F.C. Clemen, and B. Lidick´y. Max cuts in triangle-free graphs. Technical Report 2103.14179[math.CO], arxiv e-print, 2021.

[Big09] N. Biggs. Strongly regular graphs with no triangles. Technical Report 0911.2160[math.CO], arxiv e-print, 2009.

[Bro83] A.E. Brouwer. The uniqueness of the strongly regular graph on 77 points. Journal of Graph Theory, 7:455–461, 1983.

[CGW89] F. Chung, R. Graham, and R. Wilson. Quasi-random graphs. Combinatorica, 9:345–362, 1989.

[EFPS88] P. Erd˝os, R. Faudree, J. Pach, and J. Spencer. How to make a graph bipartite. Journal of Combinatorial Theory, series B, 45(1):86–98, 1988.

[EFRS94] P. Erd˝os, R. Faudree, C. Rousseau, and R. H. Schelp. A local density condition for triangles. Discrete Mathematics, 127:153– 161, 1994.

[EGS92] P. Erd˝os, E. Gy˝ori, and M. Simonovits. How many edges should be deleted to make a triangle-free graph bipartite. In Sets, Graphs and Numbers. Colloq. Math. J. Bolyai, volume 60, pages 239–263. North-Holland, 1992.

[Erd76] P. Erd˝os. Problems and results in graph theory and combinatorial analysis. In Proceedings of the Fifth British Combinatorial Conference, 1975, volume 15, pages 169–192, 1976.

[Erd84] P. Erd˝os. On some problems in graph theory, combinatorial analysis and combinatorial number theory. In Graph theory and combinatorics (Cambridge 1983), pages 1–17, 1984.

[Erd97] P. Erd˝os. Some old and new problems in various branches of combinatorics. Discrete Mathematics, 165/166:227–231, 1997.

- [Gew69a] A. Gewirtz. Graphs with maximal even girth. Canad. J. Math., 21:915–934, 1969.
- [Gew69b] A. Gewirtz. The uniqueness of g(2,2,10,56). Trans. New York Acad. Sci., 31:656–675, 1969.


[GM05] A. L. Gavrilyuk and A. A. Makhnev. On Krein graphs without triangles. Doklady Mathematics, 72:591–594, 2005. Russian version in Dokl. Akad. Nauk 403 (2005) 727-730.

[Grz12] A. Grzesik. On the maximum number of ﬁve-cycles in a trianglefree graph. Journal of Combinatorial Theory, ser. B, 102:1061– 1066, 2012.

- [HHK`12] H. Hatami, J. Hladky, D. Kral, S. Norin, and A. Razborov. Nonthree-colorable common graphs exist. Combinatorics, Probability and Computing, 21(5):734–742, 2012.
- [HHK`13] Hatami H, J. Hladky, D. Kral, S. Norin, and A. Razborov. On the number of pentagons in triangle-free graphs. Journal of Combinatorial Series, ser. A, 120(3):722–732, 2013.


[KO07] P. Kaski and P. Ostergard. There are exactly ﬁve biplanes with k = 11. Journal of Combinatorial Designs, 16:117–127, 2007.

[Kri95] M. Krivelevich. On the edge distribution of triangle-free graphs. Journal of Combinatorial Theory, series B, 63:245–260, 1995.

[KS06] P. Keevash and B. Sudakov. Sparse halves in triangle-free graphs. Journal of Combinatorial Theory, series B, 96:614–620, 2006.

[NY15] S. Norin and L. Yepremyan. Sparse halves in dense triangle-free graphs. Journal of Combinatorial Theory, Series B, 115:1–25, 2015.

[Raz07] A. Razborov. Flag algebras. Journal of Symbolic Logic, 72(4):1239–1282, 2007.

