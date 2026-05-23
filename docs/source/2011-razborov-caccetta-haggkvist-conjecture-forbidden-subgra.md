---
type: source
kind: paper
title: On the Caccetta-Haggkvist conjecture with forbidden subgraphs
authors: Alexander Razborov
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1107.2247v2
source_local: ../raw/2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra.pdf
topic: general-knowledge
cites:
---

arXiv:1107.2247v2[math.CO]17Aug2012

# On the Caccetta-Ha¨ggkvist Conjecture with Forbidden Subgraphs

### Alexander A. Razborov∗ October 8, 2018

Abstract

The Caccetta-H¨aggkvist conjecture made in 1978 asserts that every oriented graph on n vertices without oriented cycles of length ≤ ℓ must contain a vertex of outdegree at most n−ℓ 1. It has a rather elaborate set of (conjectured) extremal conﬁgurations.

![image 1](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile1.png>)

In this paper we consider the case ℓ = 3 that received quite a signiﬁcant attention in the literature. We identify three oriented graphs on four vertices each that are missing as an induced subgraph in all known extremal examples and prove the Caccetta-H¨aggkvist conjecture for oriented graphs missing as induced subgraphs any of these oriented graphs, along with C3. Using a standard trick, we can also lift the restriction of being induced, although this makes graphs in our list slightly more complicated.

## 1. Introduction

One prominent way to attack a diﬃcult problem in extremal combinatorics is by better understanding the nature of its (conjectured) extremal conﬁgurations. What one would hope for is to ﬁnd some property P, as “natural” as possible that is shared by all known extremal conﬁgurations, and then solve

![image 2](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile2.png>)

∗University of Chicago, razborov@cs.uchicago.edu. Part of this work was done while the author was at Steklov Mathematical Institute, supported by the Russian Foundation for Basic Research, and at Toyota Technological Institute, Chicago.

the extremal problem in question for all conﬁgurations possessing this property P. Arguably but conceivably, this may shed some light on the nature of diﬃculties surrounding the problem in question and perhaps even open up a possibility to solve the problem by gradually lifting constraints deﬁning the property P. For the famous Turan’s (3,4)-problem this approach was recently undertaken by the author in [Raz10, Raz11]; another good example of this sort is the recent solution of the local Sidorenko conjecture by Lova´sz [Lov10].

In this paper we address along these lines another major open problem in the area, Caccetta-H¨aggkvist conjecture, that is nearly as famous as those mentioned above. Recall that we are given an oriented graph1 G on n vertices that does not contain (oriented) cycles of length ≤ ℓ or, in other words, has girth ≥ ℓ + 1. Behzad, Chartrand and Wall [BCW70] asked the following question: if G is additionally known to be bi-regular, how large can be its degree? They conjectured that the answer is ⌊n−ℓ1⌋ and presented a simple construction attaining this bound. Eight years later, Caccetta and H¨aggkvist [CH78] proposed to lift in this conjecture the restriction of bi-regularity and, moreover, restrict attention to minimal outdegree only. In other words, they asked if every orgraph without oriented cycles of length ≤ ℓ must contain a vertex of out-degree ≤ n−ℓ 1, and it is this question that became known as the Caccetta-H¨ggkvist conjecture. It turned out to be notoriously diﬃcult, too.

![image 3](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile3.png>)

![image 4](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile4.png>)

The case of higher values of ℓ was studied in [CS83, Ham87, HR87, Nis72, She00, She02].

In this paper we concentrate on the case ℓ = 3, as much of the previous work in this area did. Let c be the minimal constant for which the asymptotic upper bound (c+o(1))n on the minimal outdegree in C3-free orgraphs holds. Caccetta and H¨aggkvist themselves proved in [CH78] that c ≤ 3−

√5

![image 5](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile5.png>)

2 ≈ 0.382. This was improved in the series of papers [Bon97, She98, HHK07] to the current record of c ≤ 0.3465n [HKN09].

![image 6](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile6.png>)

As we already noticed, the ﬁrst example of an orgraph G on n ver-

tices without copies of C3 and minimal degree ⌊n−31⌋ was given in the paper [BCW70]. It is quite simple: assuming that n = 3h+1 for some integer h, we

![image 7](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile7.png>)

let Z3h+1 be the set of vertices, and we connect i to j if and only if j − i ≤ h mod (3h+1). But this example is not unique: Bondy [Bon97, Proposition 1] observed that the class of orgraphs with the above properties is closed under

![image 8](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile8.png>)

- 1 That is, a digraph without loops, parallel or anti-parallel edges. By analogy with the


abbreviation “digraph”, in this paper oriented graphs will be often called orgraphs.

✲ ✒

![image 9](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile9.png>)

✒

❘

❘

✻

![image 10](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile10.png>)

❘✠

✲ ✒

![image 11](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile11.png>)

❘

![image 12](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile12.png>)

❄

In-Pendant

Out-Pendant Figure 1: Forbidden orgraphs.

Twisted Circle

☛ ❯

I3 K1,2

✕❑

K2,1

✕

❯

P3

✕

✛

❯

![image 13](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile13.png>)

C3

Figure 2: Some orgraphs on 3 vertices.

lexicographic product, which leads to many more non-isomorphic extremal examples for the Caccetta-H¨aggkvist conjecture.

The ﬁrst (minor) contribution of our paper (Section 2) consists in a slight generalization of Bondy’s construction which results in what we believe to be the complete set of currently known conjectured extremal conﬁgurations.

All these examples (for the case ℓ = 3) have the property that they are missing (as induced subgraphs) the three orgraphs shown on Figure 1 (cf. [Bon97, Proposition 2]). As our main result, we prove the CH-conjecture (for ℓ = 3) for any C3-free orgraph with this additional property (Theorem 3.1). While this is the ﬁrst result of this kind pertaining to all known extremal conﬁgurations, we would like to mention some previous (unpublished) work regarding forbidden orgraphs on 3 vertices that are missing in the original “cyclic” conﬁguration by Behzad, Chartrand and Wall. On Figure 2, these are represented by I3, K1,2 and K2,1.

The CH-conjecture (as always, for ℓ = 3) is an easy exercise for orgraphs missing C3 and K1,2 as induced subgraphs. Under the additional assumption of out-regularity, Chudnovsky and Seymour [CS06] did the case when C3 and I3 are missing; to the best of our knowledge, the question is still open without the restriction of out-regularity. Seymour [Sey06] proved the CH-conjecture

for orgraphs missing C3 and K2,1 (which is substantially more diﬃcult than the dual case of C3 and K1,2).

Potential usefulness of Theorem 3.1 (at least, of the sort we can think of) as stated above is undermined by the fact that it involves the notion of an induced subgraph. We include a very simple observation (Theorem 3.2) showing that this restriction can be removed at the expense of the forbidden family becoming slightly more complicated (see Figure 3).

The proof of Theorem 3.1 was found mostly in the framework of ﬂag algebras [Raz07]. But the ﬁnal calculation (see the crucial Claim 5.6) does not use multiplicative structure (and, in particular, does not use CauchySchwarz inequality). This makes working in the limit framework unnecessary, and in this paper we adopt a compromise approach. Namely, we exclusively work with ﬁnite objects but still use basic elements of the whole apparatus of ﬂag algebras that in our case boils down to two conventions:

- • systematic and consistent notation for various sets based upon types and ﬂags
- • systematic measurement of all necessary quantities in terms of their “densities” rather than absolute size.


We would like to note that even with this compromise approach lowerorder terms do begin to accumulate in the proof of Claim 5.6, and we can not simply dismiss them due to the inductive nature of the argument. Fortunately, the proof is over before they become a real nuisance.

## 2. Extremal conﬁgurations

We let [n] def= {1, 2, . . ., n}.

An oriented graph, or an orgraph, is a directed graph without loops and such that every pair of vertices is connected by at most one edge, regardless of direction. V (Γ) is the set of vertices of an orgraph Γ, and E(Γ) is its set of edges. For an edge v, w , w is its head and v is its tail. d+Γ(v) is the out-degree of the vertex v. Vertices v and w are independent in Γ if neither

v, w nor w, v is an edge. For an orgraph Γ and V ⊆ V (Γ), Γ|V is the orgraph induced by V .

C3 is the cycle on 3 vertices, and an orgraph Γ is C3-free if it does not contain copies of C3.

Conjecture 1 (Caccetta-H¨aggkvist Conjecture) Any C3-free orgraph Γ on n vertices contains a vertex v with d+Γ(v) ≤ n−31. We will sometimes refer to this as to “the CH-conjecture”.

![image 14](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile14.png>)

In this section we review what we believe to be the complete list of known conﬁgurations attaining this value; as we noted in Introduction, this is a rather straightforward generalization of the examples found in [BCW70, Bon97]. There are two legitimate frameworks in which this question can be addressed; one of them is exact (i.e., describing ﬁnite orgraphs precisely matching the bound in Conjecture 1 precisely). And another is asymptotic: it can be best described in terms of (or)graphons [LS06] or ﬂag algebras [Raz07], but intuitively it corresponds to “convergent” sequences of orgraphs {Γm} with minv d+Γ

(v) ≥ 3 1 − o(1) |V (Γm)|. We treat them simultaneously.

![image 15](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile15.png>)

m

Let S1 be the unit circle, and deﬁne the (inﬁnite) orgraph Γ0 with V (Γ0) def= S1 and E(Γ0) def= { x, y  | y − x < 1/3 mod 1}. Note that Γ0 is C3-free. Let Ω def= (S1)∞ be the inﬁnite-dimensional torus. We let ΓCH be the orgraph with V (ΓCH) = Ω that is the lexicographic product of countably many copies of Γ0. In other words, for any two diﬀerent vertices x = (x1, x2, . . ., xn, . . .), y = (y1, . . ., yn . . .) ∈ Ω we choose the minimal d for which xd = yd and let

x, y ∈ E(ΓCH) if and only if xd, yd ∈ E(Γ0).

Ω is a topological space (under product topology), and therefore every probability measure µ on its Borel subsets gives rise to an oriented graphon [LS06], as well as to a homomorphism φ ∈ Hom+(A0[TCH], R) [Raz07], where TCH is the theory of C3-free orgraphs. We now describe those measures µ that lead to asymptotically extremal examples for Conjecture 1.

Fix a probability measure µ on Borel subsets of Ω. Every ﬁnite string (a1, . . ., ad) ∈ (S1)d deﬁnes the canonical closed set Ωa = {x ∈ Ω| x1 = a1, . . ., xd = ad}. Whenever µ(Ωa) > 0, we have the conditional measure µa on Ωa (µa(X) def=

µ(X) µ(Ωa), X ⊆ Ωa) and then the pushforward measure µa on S1 deﬁned by projecting Ωa onto the (d + 1)st coordinate. Let us call the measure µ extremal if for every preﬁx a for which µ(Ωa) > 0, this measure µa has one of the following two forms:

![image 16](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile16.png>)

- • uniform (Lebesgue) measure on S1;
- • uniform discrete measure on the set 3h 0+1, 3h1+1, . . ., 3h3+1h for some integer h ≥ 1.


![image 17](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile17.png>)

![image 18](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile18.png>)

![image 19](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile19.png>)

A combinatorial way to visualize an extremal measure µ is by a locally ﬁnite rooted tree in which every non-leaf node has outdegree (3h + 1) for some h; the ﬁrst case (of Lebesgue measure) corresponds to a leaf.

- Claim 2.1 For any extremal measure µ on Ω with the above property and for any x ∈ Ω,


µ({y ∈ Ω| x, y ∈ E(ΓCH)}) = 1/3.

Proof. {y ∈ Ω| x, y ∈ E(ΓCH)} splits as the disjoint union ∞d=1 Vd, where Vd is the set of all y such that x1 = y1, . . ., xd−1 = yd−1 and yd − xd mod 1 ∈ (0, 1/3). Our restriction on the measures µa implies that µ(Vd) = 1

1,...,xd) ≤ 4−d (and hence limd→∞ µ(Ωx

- 3 µ(Ωx


1,...,xd−1) − µ(Ωx

1,...,xd) . Summing over all d and noting that µ(Ωx

![image 20](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile20.png>)

1,...,xd) = 0) gives the result.

![image 21](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile21.png>)

This collection of oriented graphons describes what we believe to be the complete set of all known extremal conﬁgurations for Conjecture 1 (more precisely, in the terminology of [Raz07, §4.1], the set of all homomorphisms φ ∈ Hom(A0[TCH], R) with δα(φ) = 1/3). If we additionally require the set {a| µ(Ωa) > 0} to be ﬁnite, we arrive at (again, to the best of our knowledge) the set of all known ﬁnite but in general weighted (conjecturally) extremal orgraphs. Vertices correspond to leaves of the representing tree, and if the product of degrees is the same along all terminal paths, then the measure on leaves becomes uniform, and this gives us (apparently) all known extremal conﬁgurations that are ordinary (unweighted) orgraphs.

One obvious way to ensure the last uniformity property is by requiring that the tree is balanced and all outdegrees are the same on each level. But there are more sophisticated ways to arrive at a tree with the required property. For example, some vertices on the ﬁrst level (we place the root onto level zero) may have (3g+1)(3h+1) leaves as their children, while others may branch to a balanced tree of depth 2 with outdegrees (3g+1) on the ﬁrst level and (3h+1) on the second (and yet another subtrees may have the same form but with the outdegrees on the ﬁrst and second level exchanged). These in particular lead to extremal examples that do not possess a vertex-transitive group of automorphisms. Nonetheless, all these examples are bi-regular and in particular are also good for the original question asked in [BCW70].

Altogether, there are six C3-free orgraphs on four vertices missing in ΓCH

- as an induced subgraph [Bon97, Proposition 2]. Of these, we are interested


only in the three shown on Figure 1, and let us ﬁrst check that they are indeed missing.

- Claim 2.2 None of the three orgraphs on Figure 1 can be realized as an induced subgraph of ΓCH.

Proof. Let xi ∈ Ω (i = 1..4) be four diﬀerent vertices, and let d be the ﬁrst integer for which there exist 1 ≤ i < j ≤ 4 with xid = xjd. The projection onto the dth coordinate deﬁnes an equivalence relation ≈ on [4] with more than one class and such that if i ≈ j  ≈ i′ ≈ j′ then xi, xi′ ∈ E(ΓCH) iﬀ xj, xj′ ∈ E(ΓCH). An easy inspection shows that no non-trivial equivalence relation with these properties exists for any of the orgraphs on Figure 1. Therefore, in fact all xid (i ∈ [4]) are pairwise diﬀerent, and we actually have an embedding into Γ0. But Γ0 does not contain induced copies of K1,2, K2,1 (see Figure 2) as an induced subgraph,while every orgraph on Figure 1 contains one of those. Contradiction.

![image 22](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile22.png>)

- 3. Main results


The main result of this paper is the following.

- Theorem 3.1 Let Γ be an orgraph on n vertices that does not contain either C3 or any of the three orgraphs on Figure 1 as an induced subgraph. Then Γ contains a vertex v with d+Γ(v) ≤ n−31.

![image 23](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile23.png>)

Before we begin the proof of Theorem 3.1, let us show how to drop the restriction of being induced.

- Theorem 3.2 Assume that the CH-conjecture holds for all C3-free orgraphs containing at least one of the orgraphs2 on Figure 3 as a (not necessarily induced) subgraph. Then the CH-conjecture holds for all C3-free orgraphs.


Proof. Let us describe ﬁrst how this list of orgraphs was generated from Figure 1. For every orgraph Γ on that ﬁgure, we took all ordered pairs of independent vertices v, w such that there is no vertex x with v, x , x, w ∈

![image 24](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile24.png>)

2Encircled on this ﬁgure are those vertices that are new w.r.t. Figure 1.

✲ ✒

✲ ✒

❦

![image 25](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile25.png>)

![image 26](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile26.png>)

✒

✻

✻

❑

![image 27](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile27.png>)

![image 28](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile28.png>)

![image 29](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile29.png>)

![image 30](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile30.png>)

✛ ✛

❘

☛ ❘

❘

❄

❄

✸

✸

![image 31](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile31.png>)

![image 32](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile32.png>)

■

✻

■

![image 33](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile33.png>)

![image 34](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile34.png>)

❘✠

✠

✠

❄

Figure 3: Another set of forbidden orgraphs

E(Γ). And then for every such pair we added one new vertex x with precisely these edges. On Figure 3, these auxiliary vertices are encircled.

Assume now that the CH-conjecture holds for all graphs that contain at least one orgraph on Figure 3. Let Γ be an arbitrary C3-free orgraph; we want to show the existence of a vertex v with d+Γ(v) ≤ n−31. W.l.o.g. we may assume that adding any new edges to Γ destroys C3-freeness, or, in other words, that every pair (v, w) of independent vertices appears as a diagonal of a copy of C4 in Γ.

![image 35](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile35.png>)

If Γ does not have induced copies of the three orgraphs shown on Figure 1, we are done by Theorem 3.1.

Otherwise, our construction and the remark above imply that Γ must contain as a (not necessarily induced) subgraph one of the three orgraphs on Figure 3, except that some of the encircled vertices can be identical. It is, however, easy to see by inspection that identifying any two of them leads either to anti-parallel edges or a copy of C3, except for the pair of outer-most vertices on the second or the third orgraph. But it is easy to see that the result of this identiﬁcation will contain the ﬁrst orgraph on Figure 3 and thus does not need a special treatment.

We have shown that Γ must contain one of the three orgraphs on Figure

- 3, and therefore the required vertex v exists by our assumption.


![image 36](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile36.png>)

We hope that this piece of information about the structure of hypothetical counterexamples to the CH-conjecture that separates them from all known extremal conﬁgurations, may turn out helpful, presumably in combination with inductive arguments of the kind that have been already extensively used in previous research on this problem.

The rest of the paper is entirely devoted to the proof of Theorem 3.1. Arguing by induction on the number of vertices, we ﬁx a ﬁnite orgraph Γ

that does not contain either C3 or induced copies of the three orgraphs on Figure 1 and such that the CH-conjecture holds for all its proper induced subgraphs. Our goal is to prove it for Γ.

## 4. Flag Algebras

As indicated in Introduction, in this paper we use only a tiny fragment of the whole theory, in the amount of the ﬁrst four pages of [Raz07, §2.1].

A type is a C3-free orgraph σ with V (σ) = [k] for some non-negative integer k called the size of σ. A σ-ﬂag is a pair F = (Γ, θ), where Γ is a C3-free orgraph and θ : σ −→ Γ is an induced embedding. Thus, from the combinatorial point of view, a type is just a (totally) labeled orgraph, and a ﬂag is a partially labeled one. Vertices from V (Γ) \ im(θ) will be sometimes called free. If F = (Γ, θ) is a σ-ﬂag and V ⊆ V (Γ) contains im(θ), then the sub-ﬂag (Γ|V , θ) will be also denoted by F|V .

A ﬂag embedding α : F −→ F′, where F = (Γ, θ) and F′ = (Γ′, θ′) are σ-ﬂags for the same type σ is an induced embedding of orgraphs α : Γ −→ Γ′ such that θ′ = αθ (i.e., “label-preserving”). F and F′ are isomorphic (denoted by F ≈ F′) if there is a one-to-one ﬂag embedding α : F −→ F′. Fℓσ is the set of all σ-ﬂags on ℓ vertices.

If F ∈ Fℓσ and F′ = (Γ, θ) ∈ FLσ with L ≥ ℓ, the key quantity in the whole theory is the density p(F, F′) of induced copies of F in F′ deﬁned as follows. We choose in V (Γ) uniformly and at random a subset V of cardinality ℓ subject to the condition V ⊇ im(θ), and let p(F, F′) denote the probability of the event F′|V ≈ F. In almost all calculations used in this paper, ℓ = k+1 and hence V can be identiﬁed with a single vertex x chosen uniformly at random from V (Γ) \ im(θ).

From now on, we ﬁx an orgraph Γ that does not contain either C3 or induced copies of the three orgraphs on Figure 1 and such that the CHconjecture holds for all its proper induced subgraphs. If pairwise diﬀerent vertices v1, . . ., vk ∈ V (Γ) induce a copy of a type σ of size k, then, letting θ : [k] −→ V (Γ) be the corresponding embedding deﬁned by θ(i) = vi, (Γ, θ) becomes a σ-ﬂag, and for another ﬂag F (typically, ﬁxed and very small) we introduce the abbreviation

F(v1, . . ., vk) def= p(F, (Γ, θ)). (1) Next, we list concrete types and ﬂags needed for our purposes.

2

2

✒

✒

![image 37](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile37.png>)

![image 38](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile38.png>)

❘

1

1

3

❘

❄ ❘✠

❄

OA

OP

Figure 4: O-ﬂags

2

✒

![image 39](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile39.png>)

❘

1

❘✠

❄

OA

2

2

✒

✒

1 2 ❘

1

1

❘

❘✠

K1A,2

K2N,1

P3A

Figure 5: Miscellaneous ﬂags

✒

1 ❘ 2

P3N

2

✒

✻

![image 40](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile40.png>)

1

■

IA

0 and 1 are the unique type of sizes 0 and 1, respectively. A is the type of size 2 with E(A) def= { 1, 2 }, and N is the type of size 2 without any edges. P is the type of size 3 with E(P) def= { 1, 2 , 2, 3 }.

α ∈ F21 is a directed edge in which the tail vertex is labeled by 1; our ﬁnal goal is to ﬁnd a vertex v with α(v) ≤ 1/3. For a type σ of size k, let Oσ ∈ Fkσ+1 be the ﬂag in which the only free vertex has k incoming edges. Removing from OP label 3, we will get a ﬂag from F4A that we will denote by OA, see Figure 4. We will also need a few other miscellaneous ﬂags from F3A, F3N shown on Figure 5.

## 5. Proof of Theorem 3.1

Let us call an edge v, w critical if OA(v, w) takes the minimal possible value over all edges going out of v. Combinatorially, this means that we are looking at the set A(v) of all out-neighbors of v and pick w ∈ A(v) to have the smallest possible outdegree in Γ|A(v).

- Claim 5.1 For any critical edge v, w , OA(v, w) = 0.

Proof. Assume the contrary, that is Γ contains a pair of other vertices x = y such that { v, x , w, x , w, y , y, x } ∈ E(Γ) while v and y are independent. We are going to prove that

OA(v, x) < OA(v, w), (2) and this will contradict the assumption that v, w is critical.

For that, let us consider an arbitrary vertex z contributing to OA(v, x) (that is, such that v, z , x, z ∈ E(Γ)). Since v, x, y, z do not span an InPendant (see Figure 1), y and z may not be independent and thus y, z ∈ E(Γ) ( z, y would have created a copy of C3). But now since v, w, y, z do not span a Twisted Circle, w and z can not be independent and thus

w, z ∈ E(Γ). Which means that z contributes to OA(v, w) as well.

Finally, let us note that x itself contributes to OA(v, w). This completes the proof of (2) and gives the desired contradiction with the criticality of

v, w .

![image 41](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile41.png>)

In what follows, we argue by contradiction, i.e. we assume that α(v) > 31 for all v ∈ V (Γ).

![image 42](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile42.png>)

- Claim 5.2 For any critical edge v, w , P3A(v, w) > 0. Proof. Note ﬁrst that α(w) = nn−−12 OA(v, w) + P3A(v, w) . Next, we can apply the inductive assumption to the set of all out-neighbors of v. Since w was chosen to have the minimal outdegree in Γ|A(v), OA(v, w) ≤ 13α(v) ≤ 31. The claim follows immediately since α(w) > 1/3 by the assumption we have just made.

![image 43](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile43.png>)

![image 44](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile44.png>)

![image 45](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile45.png>)

![image 46](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile46.png>)

Now we study critical paths of length 2.

- Claim 5.3 If u, v and v, w are critical edges then u and w are independent.


Proof. Assume the contrary, that is u, w ∈ E(Γ). By Claim 5.2, there exists x such that v, x ∈ E(Γ) while u and x are independent. Since (u, v, w, x) do not induce an Out-Pendant, w and x may not be independent, and the edge x, w is ruled out by Claim 5.1. Therefore, w, x ∈ E(Γ).

And now we use the criticality of v, w , and our goal, like in the proof of Claim 5.1, is to arrive at a contradiction by establishing (2). We again choose z with v, z , x, z ∈ E(Γ). The edge u, z is again ruled out by Claim 5.1 (applied to {u, v, x, z}), therefore u and z must be independent.

And now w, z may not be independent (since otherwise {u, v, w, z} would have formed an Out-Pendant). Therefore, w, z ∈ E(Γ), and the rest of the proof is the same as in the proof of Claim 5.1.

![image 47](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile47.png>)

The ﬂag K2N,1 is shown on Figure 5.

- Claim 5.4 If u, v and v, w are critical edges then K2N,1(u, w) = 0.

Proof. Assume the contrary, and let x be any vertex such that u, x , w, x ∈

E(Γ). Then v and x can not be independent (as it would have created a Twisted Circle), x, v can not be an edge since it would have created C3 and

v, x can not be an edge by Claim 5.1.

![image 48](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile48.png>)

- Claim 5.5 If u, v and v, w are critical edges then


1 n − 2

3OA(u, v) ≤ P3N(u, w) −

. (3)

![image 49](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile49.png>)

Proof. Let P3N(u, w) = n−h2, and let U ∋ v be the corresponding set of vertices, |U| = h. Applying to Γ|U our inductive assumption, we ﬁnd a

![image 50](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile50.png>)

vertex v∗ ∈ U that has degree ≤ h−31 in Γ|U (possibly, v∗ = v). We will prove that

![image 51](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile51.png>)

h − 1 3(n − 2)

OA(u, v∗) ≤

(4)

![image 52](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile52.png>)

from which the claim follows since OA(u, v) ≤ OA(u, v∗) due to the criticality of u, v .

To prove (4), it suﬃces to show that every vertex x contributing to OA(u, v∗) in fact belongs to U, that is x, w ∈ E(Γ). But w, x can not be independent (since otherwise we would get a copy of an Out-Pendant), and the edge w, x is ruled out by Claim 5.4 (note that we must apply this

claim to the triple (u, v, w), not (u, v∗, w), as we do not know that u, v∗ is critical!).

![image 53](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile53.png>)

The following is our crucial claim that is a typical computer-assisted calculation in ﬂag algebras, albeit much simpler than in all previous applications of the method. For an explanation of all new ﬂags appearing in its statement and proof, we refer to Figure 5.

- Claim 5.6 If u, v and v, w are critical edges, then


α(u) + α(v) + α(w) + (OA(u, v) + IA(u, v) + K2A,1(u, v)) −(OA(v, w) + IA(v, w) + K2A,1(v, w)) ≤ 1.

 



(5)

Proof. Subtracting the inequality in Claim 5.5 and re-grouping terms, it suﬃces to prove that



α(u) + α(v) + α(w) + (IA(u, v) + K2A,1(u, v) − 2OA(u, v)) −(OA(v, w) + IA(v, w) + K2A,1(v, w)) + P3N(u, w) ≤ 1 +



(6)

1 n − 2

.

![image 54](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile54.png>)



Let us pick x ∈ V (Γ)\{u, v, w} uniformly at random and let us re-calculate all quantities in the left-hand side of (6) with respect to that distribution. More precisely, for {v1, . . ., vk} ⊂ {u, v, w} we replace the quantity p(F, (Γ, θ)) in (1) by the probability of the event (Γ, θ)|{v

1,...,vk,x} ≈ F (thus, the only diﬀerence from the original deﬁnition is that now the random variable x is forbidden to take values from {u, v, w} \ {v1, . . ., vk}). Denoting these recalculated quantities with α(u), . . ., P3N(u, w), we claim that

 

α(u) + α(v) + α(w) + ( IA(u, v) + K2A,1(u, v) − 2 OA(u, v)) −( OA(v, w) + IA(v, w) + K2A,1(v, w)) + P3N(u, w) ≤ 1.

(7)



For that we prove that every individual x  ∈ {u, v, w} contributes at most 1 to the left-hand side3.

We can assume w.l.o.g. that x contributes to at least two terms

α(u), α(v), α(w), IA(u, v), K2A,1(u, v), P3N(u, w),

and we have to show that this excessive (over 1) contribution is compensated by the contribution of x to negative terms.

Firstly we note that x may contribute to at most one of the terms

IA(u, v), K2A,1(u, v), P3N(u, w), depending on whether x, u ∈ E(Γ), x, u are independent or u, x ∈ E(Γ). Thus, we can also assume w.l.o.g. that x contributes to at least one of α(u), α(v), α(w). Which immediately implies

that x may not contribute to IA(u, v), K2A,1(u, v): otherwise we would have had x, v ∈ E(Γ), hence w, x  ∈ E(Γ) and x would not have contributed to α(u) + α(v) + α(w).

Let us now consider the case when x contributes to P3N(u, w), i.e., u, x , x, w ∈

E(Γ). If v, x  ∈ E(Γ), then x does give an excessive contribution of one (to α(u) and P3N(u, w)), but it is compensated by its contribution to one of the negative terms IA(v, w), K2A,1(v, w). If, on the other hand, v, x ∈ E(Γ), then the excessive contribution of two is oﬀset by the term 2 OA(u, v).

We are left with the case when x does not contribute to IA(u, v), K2A,1(u, v), P3N(u, w)

- at all which, in particular implies that it contributes to at least two terms α(u), α(v), α(w).


If x contributes to both α(u), α(v), then this contribution is again oﬀset by 2 OA(u, v). Thus, we can also assume that x contributes to α(w) and to precisely one of the terms α(u), α(v). If v, x ∈ E(Γ) then the excessive conribution is taken care of by the last remaining negative term OA(v, w). And the case u, x ∈ E(Γ), v, x  ∈ E(Γ) is impossible since it gives rise to Twisted Circle.

The proof of (7) is complete.

![image 55](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile55.png>)

3The reader familiar with the formalism of ﬂag algebras may notice that we are simply proving the inequality 3i=1 πP,i(α)+πP,[1,2](OA +IA+ K2A,1)−πP,[2,3](OA +IA+ K2A,1)+ πP,[1,3]( P3N) − 3πP,[1,2](OA) ≤ 1.

On the other hand, we have

- α(u) =

n − 3 n − 1

![image 56](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile56.png>)

α(u) +

1 n − 1

![image 57](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile57.png>)

;

- α(v) =

n − 3 n − 1

![image 58](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile58.png>)

α(v) +

1 n − 1

![image 59](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile59.png>)

;

- α(w) =


n − 3 n − 1

α(w);

![image 60](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile60.png>)

1 n − 2

n − 3 n − 2

P3N(u, w) =

P3N(u, w) +

; F(y, z) =

![image 61](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile61.png>)

![image 62](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile62.png>)

n − 3 n − 2

F(y, z) for any other term F(y, z) in (6), (7).

![image 63](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile63.png>)

Multiplying (7) by nn−−32 and adding n−11 to both sides, we get

![image 64](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile64.png>)

![image 65](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile65.png>)

 

n − 3 n − 2

( α(u) + α(v) + α(w)) + (IA(u, v) + K2A,1(u, v) − 2OA(u, v)) −(OA(v, w) + IA(v, w) + K2A,1(v, w)) + P3N(u, w) ≤ 1.

![image 66](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile66.png>)



Also, since α(u) + α(v) + α(w) > 1 by our assumption, we have

(8)

2 n − 2 ≥ α(u) + α(v) + α(w) −

- n − 1

![image 67](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile67.png>)

- n − 2


n − 3 n − 2

( α(u) + α(v) + α(w)) =

(α(u) + α(v) + α(w)) −

![image 68](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile68.png>)

![image 69](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile69.png>)

1 n − 2

.

![image 70](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile70.png>)

Substituting this into (8) and summing the resulting inequality with (3) gives us (6).

![image 71](<2011-razborov-caccetta-haggkvist-conjecture-forbidden-subgra_images/imageFile71.png>)

Now the proof of Theorem 3.1 is completed by an easy averaging argument. Since for every vertex v there exists at least one critical edge going out of v, there exists a cycle C = (v1, v2, . . ., vℓ) consisting of critical edges. After summing up the inequalities (5) along this cycle, the terms OA(u, v), . . ., K2A,1(v, w) get canceled and we arrive at

α(vi) ≤ ℓ/3.

i∈Zℓ

Therefore, there exists at least one i with α(vi) ≤ 1/3. Theorem 3.1 is proved.

That would be interesting to improve upon our result by removing some (and preferably all) forbidden subgraphs on Figure 1. We have tried it for a while, but all three constraints are very essential in our proof, and removing any one of them immediately creates a new level of diﬃculties that we have not been able to surpass.

## Acknowledgment

I am grateful to Jan Hladk´y for several useful remarks. I am also indebted to both anonymous referees for reading the manuscript very carefully that has resulted in several important changes and corrections.

## Added in proof

Lichiardopol [Lic12] has given an aﬃrmative answer to the question asked in Section 1: the CH-conjecture holds for oriented graphs with independence number 2 (and without restriction of out-regularity).

## References

[BCW70] M. Behzad, G. Chartrand, and C. E. Wall. On minimal regular digraphs with given girth. Fundamenta Mathematicae, 69:227–231, 1970.

[Bon97] J. A. Bondy. Counting subgraphs: A new approach to the Caccetta-H¨aggkvist conjecture. Discrete Math., 165/166:71–80, 1997.

[CH78] L. Caccetta and R. H¨aggkvist. On minimal digraphs with given girth. Congressus Numerantium, 21:181–187, 1978.

[CS83] V. Chva´tal and E. Szemer´edi. Short cycles in directed graphs. J. Combin. Theory Ser. B, 35(3):323–327, 1983.

[CS06] M. Chudnovsky and P. Seymour, 2006. Personal communication. [Ham87] Y. O Hamidoune. A note on minimal directed graphs with given girth. J. Combin. Theory Ser. B, 43(3):343–348, 1987.

[HHK07] P. Hamburger, P. Haxell, and A. Kostochka. On directed triangles in digraphs. Electronic Journal of Combinatorics, 14(1):Note 19, 2007.

[HKN09] J. Hladk´y, D. Kr´al’, and S. Norine. Counting ﬂags in triangle-free digraphs. Manuscript, available at http://arxiv.org/abs/0908.2791, 2009.

[HR87] C. T. Hoa´ng and B. Reed. A note on short cycles in digraphs. Discrete Mathematics, 66(1-2):103–107, 1987.

[Lic12] N. Lichiardopol. Proof of Caccetta-H¨ggkvist conjecture for oriented graphs with positive minimum out-degree and of independence number two. Manuscript, 2012.

[Lov10] L. Lova´sz. Subgraph densities in signed graphons and the local Sidorenko conjecture. Technical Report 1004.3026v1 [math.CO], arXiv, 2010.

[LS06] L. Lova´sz and B. Szegedy. Limits of dense graph sequences. Journal of Combinatorial Theory, Series B, 96(6):933–957, 2006.

[Nis72] T. Nishimura. Short cycles in digraphs. Discrete Mathematics, 1988(1-3):295–298, 72.

[Raz07] A. Razborov. Flag algebras. Journal of Symbolic Logic, 72(4):1239–1282, 2007.

- [Raz10] A. Razborov. On 3-hypergraphs with forbidden 4-vertex conﬁgurations. SIAM Journal on Discrete Mathematics, 24(3):946–963, 2010.
- [Raz11] A. Razborov. On the Fon-der-Flaass interpretation of extremal examples for Turan’s (3,4)-problem. Proceedings of the Steklov Institute of Mathematics, 274:247–266, 2011.


[Sey06] P. Seymour, 2006. Personal communication. [She98] J. Shen. Directed triangles in graphs. Journal of Combinatorial

Theory Ser. B, 74(2):405–407, 1998.

[She00] J. Shen. On the girth of digraphs. Discrete Mathematics, 211(13):167–181, 2000.

[She02] J. Shen. On the Caccetta-Ha¨ggkvist conjecture. Graphs and Combinatorics, 18(3):645–654, 2002.

