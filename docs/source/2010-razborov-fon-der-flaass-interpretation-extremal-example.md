---
type: source
kind: paper
title: On the Fon-der-Flaass Interpretation of Extremal Examples for Turan's (3,4)-problem
authors: Alexander Razborov
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1008.4707v1
source_local: ../raw/2010-razborov-fon-der-flaass-interpretation-extremal-example.pdf
topic: general-knowledge
cites:
---

arXiv:1008.4707v1[math.CO]27Aug2010

# On the Fon-der-Flaass Interpretation of Extremal Examples for Tur´an’s (3,4)-problem

Alexander A. Razborov∗ March 15, 2018

Abstract In 1941, Tura´n conjectured that the edge density of any 3-graph without independent sets on 4 vertices (Tura´n (3,4)-graph) is ≥ 4/9(1−

- o(1)), and he gave the ﬁrst example witnessing this bound. Brown

(1983) and Kostochka (1982) found many other examples of this density. Fon-der-Flaass (1988) presented a general construction that converts an arbitrary C4-free orgraph Γ into a Tura´n (3,4)-graph. He

- observed that all Tura´n-Brown-Kostochka examples result from his construction, and proved the bound ≥ 3/7(1 − o(1)) on the edge density of any Tura´n (3,4)-graph obtainable in this way.


In this paper we establish the optimal bound 4/9(1 − o(1)) on the edge density of any Tura´n (3,4)-graph resulting from the Fon-derFlaass construction under any of the following assumptions on the undirected graph G underlying the orgraph Γ:

- • G is complete multipartite;
- • the edge density of G is ≥ (2/3 − ǫ) for some absolute constant ǫ > 0.


We are also able to improve Fon-der-Flaass’s bound to 7/16(1 − o(1)) without any extra assumptions on Γ.

![image 1](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile1.png>)

∗University of Chicago, razborov@cs.uchicago.edu. Part of this work was done while the author was with Steklov Mathematical Institute, supported by the Russian Foundation for Basic Research, and with Toyota Technological Institute at Chicago.

## 1. Introduction

In the classical paper [Man07], Mantel determined the minimal number of edges a graph G must have so that every three vertices span at least one edge. In the paper [Tur41] (that essentially started oﬀ the ﬁeld of extremal combinatorics), Tura´n generalized Mantel’s result to independent sets of arbitrary size. He also asked if similar generalizations can be obtained for hypergraphs, and these questions became notoriously known ever since as one of the most diﬃcult open problems in discrete mathematics.

To be more speciﬁc, for a family H of r-uniform hypergraphs (r-graphs in what follows) and an integer n, let exmin(n; H) be the minimal possible number of edges in an n-vertex r-graph not containing any of H ∈ H as an induced subgraph, and let

exmin(n; H) n r

πmin(H) def= nlim→∞

![image 2](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile2.png>)

(it is well-known that this limit exists).

For ℓ > r ≥ 2, let Iℓr be the empty r-graph on ℓ vertices. Then we still do not know πmin(Iℓr) (not even to mention the exact value of exmin(n; Iℓr)) for any pair ℓ > r ≥ 3, although plausible conjectures do exist [Sid95]. The simplest unresolved case that has also received most attention is r = 3, ℓ = 4; it is sometimes called Tur´n’s (3, 4)-problem (see e.g. [Kos82]). Tura´n himself exhibited an inﬁnite family of 3-graphs witnessing πmin(I43) ≤ 4/9 and conjectured that this is actually the right value. [Cae91], Giraud (unpublished), [CL99] proved increasingly stronger lower bounds on πmin(I43), with the current record

πmin(I43) ≥ 0.438334 [Raz10]. The latter bound in fact represents the result of the numerical computation of a natural positive semi-deﬁnite program associated with the Tura´n’s (3, 4)-problem; the best bound for which a “human” proof is available is

√17 12 ≥ 0.406407

![image 3](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile3.png>)

9 −

πmin(I43) ≥

![image 4](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile4.png>)

[CL99]. [Raz10] also proved that πmin(I43, G3) = 4/9, where G3 is the 3-graph on 4 vertices with 3 edges. As an induced subgraph, G3 is also missing in Tura´n’s original example, and Pikhurko [Pik09] proved that asymptotically

this is the only example of a {I43, G3}-free 3-graph attaining the equality here.

✕

❑

✲

☛ ❯

![image 5](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile5.png>)

I3 P¯3 K1,2 K2,1

✕ ✕ ✕

❯ ❯ ❯

✛

✲

![image 6](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile6.png>)

![image 7](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile7.png>)

P3 C3 T3

Figure 1: Simple orgraphs on 3 vertices

One prominent way to attack any extremal problem is by better understanding the structure of its (conjectured) extremal conﬁgurations. And one of the (many) diﬃculties associated with Tura´n’s (3, 4)-problem is that this set is extraordinarily complex and consists of a continuous family of principally diﬀerent conﬁgurations (in terminology of [Raz07], a family of diﬀerent homomorphisms φ ∈ Hom+(A0, R) attaining φ(ρ3) = 4/9) parameterized by probability distributions on the real line. These examples were constructed by Brown [Bro83] and Kostochka [Kos82], and the only (to the best of our knowledge) successful attempt to “explain” them in “external” terms was undertaken by Fon-der-Flaass [FdF88].

More speciﬁcally, let Γ be an orgraph without induced (oriented) cycles C4. Fon-der-Flaass deﬁned the 3-graph FDF(Γ) with the same vertex sets by letting (a, b, c) span an edge iﬀ the induced orgraph Γ|{a,b,c} is isomorphic to one of I3, P¯3, K1,2, T3 on Figure 1. In his brief note, Fon-der-Flaass proved the following remarkable facts:

- 1. for any C4-free orgraph Γ, the 3-graph FDF(Γ) is I43-free;
- 2. all known extremal conﬁgurations [Tur41, Bro83, Kos82] have the form FDF(Γ), where Γ runs through a special class of orientations of the almost balanced complete 3-partite graph;
- 3. for any C4-free Γ, the edge density of FDF(Γ) is ≥ 3/7(1 − o(1)).


The question of improving the latter bound to its conjectured optimal value

≥ 4/9(1 − o(1)), that we refer to as Fon-der-Flaass conjecture1, is still open, and this is precisely the question that motivated our paper.

While we have not been able to solve it completely, our main result (Theorem 2.3) achieves this goal under any one of the following two assumptions:

- 1. Γ is an orientation of a complete multipartite graph (possibly unbalanced and with more than three parts);
- 2. the edge density of Γ is ≥ 2/3−ǫ, where ǫ > 0 is an absolute constant.


Note that both these assumptions are fulﬁlled by the orgraphs underlying Tura´n-Brown-Kostochka examples, an, therefore, both these results can be interpreted as proving the desired bound 4/9(1−o(1)) for classes of I43-free 3graphs containing all known conjectured extremal conﬁgurations and having a “reasonably invariant” description. To the best of our knowledge, this is the ﬁrst result of this kind for Tura´n’s (3, 4)-problem.

Remarkably, our second restriction (on the edge density) is precisely the same as the one used by Lova´sz and Simonovits in their early work on the density of triangles in graphs [LS83] (for further developments see [Fis89, Raz08, Nik07]), and this bound is used as one of our starting points (see (7)). But we have not been able to make more formal connection between the two results and techniques used in their proofs.

Also, our second result readily implies that, provided there indeed are no extremal conﬁgurations with edge density asymptotically diﬀerent from 2/3, Fone-der-Flaass conjecture can be in principle proved by brute-force using methods similar to those from [Raz10]: as the number of vertices ℓ increases, the lower bound on the edge density for which the semi-deﬁnite program gives the desired result, must converge to 2/3. At the moment, however, this observation is of purely theoretical value: the best one can achieve with brute force on 5 vertices (when we already have 559 C4-free orgraphs) is to prove the desired bound 4/9(1−o(1)) when the edge density of Γ is ≤ 2/3−1.3·10−2.

- 1.3·10−2 is, however, way above any lower bound on ǫ in Theorem 2.3 b) one can realistically hope to achieve with our methods.


Our proofs rely on a very substantial amount of (double) counting, and they are presented in the same framework of Flag Algebras they were found

![image 8](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile8.png>)

1in [FdF88] it was actually asked in more elusive form it remains unclear if this gap suffices for constructing in this way a counterexample to Tura´n’s conjecture

in. As an additional beneﬁt of this approach, we get “stable” versions of our results for free (that is, without using hypergraph regularity lemmas): all of them hold even if we only know that the density of induced C4 (and the density of P¯3 in the part regarding complete multipartite graphs) is o(1). At this point, we assume certain familiarity with [Raz07] and instead of trying to duplicate basic deﬁnitions, simply give pointers to relevant places in [Raz07] as we go along. We also try to provide as much combinatorial intuition, examples and informal explanations as possible. In this way we are in particular able to include a few interesting observations about Tura´nBrown-Kostochka examples that hardly qualify as independent theorems but nonetheless might turn out to be useful for future research on Tura´n’s (3,4)problem.

The paper is organized as follows. In Section 2 we remind some necessary facts (recast in our language) that pertain to the previous work on Tura´n’s (3, 4)-problem and state our main results. This is interlaced with introducing some new general notation pertaining to Flag Algebras (Section 2.1.1), as well as with providing a registry of all concrete theories, types, ﬂags etc. needed for our work (Section 2.1.2). In Section 2.2 we give a relatively easy improvement of Fon-der-Flaass’s bound (without any extra assumptions on Γ) to 7/16(1 − o(1)), at the same time introducing some prerequisites for proving our main result, Theorem 2.3. This theorem itself is proved in Section

- 4. We conclude with a few remarks in Section 5.


## 2. Preliminaries

A 3-uniform hypergraph will be called a 3-graph. Given a 3-graph H and an integer n, let exmin(n; H) be the minimal possible number of edges in an n-vertex 3-graph not containing H as an induced subgraph, and let

exmin(n; H) n 3

πmin(H) def= nlim→∞

![image 9](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile9.png>)

(it is well-known that this limit exists). In this paper we are interested in πmin(I43), where I43 is the empty 3-graph on 4 vertices. We call a 3-graph Tur´n if it does not contain copies of I43. An oriented graph, or an orgraph is a directed graph without loops, multiple edges and pairs of edges of the form v, w , w, v . For an orgraph Γ and V ⊆ V (Γ), Γ|V is the induced

subgraph spanned by vertices in V . C4 is an oriented cycle on 4 vertices, and an orgraph Γ is C4-free if it does not contain induced copies of C4.

This whole paper is motivated by the famous Tur´n’s (3, 4)-problem:

Determine πmin(I43). Let us ﬁrst review, in appropriate terms, the set of conjectured extremal conﬁgurations [Tur41, Bro83, Kos82, FdF88].

Let Ω = Z3 × R, and consider the (inﬁnite) orgraph ΓK = (Ω, EK) on Ω given by

EK def= { (a, x), (b, y)  | (x + y < 0 ∧ b = a + 1) ∨ (x + y > 0 ∧ b = a − 1)}.

- Fact 1 ΓK is C4-free. Proof. Any C4-cycle in ΓK must clearly be of the form (a, x1), (a +

- 1, y1), (a, x2), (a + 1, y2) for some a ∈ Z3. But then (a, x1), (a + 1, y1) ∈ EK and (a, x2), (a+1, y2) ∈ EK imply x1+y1+x2+y2 = (x1+y1)+(x2+y2) < 0, and, by considering the other two edges, x1+y1+x2+y2 > 0. Contradiction.


![image 10](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile10.png>)

Let now Γ = (V, E) be an arbitrary (possibly inﬁnite) orgraph. We deﬁne FDF(Γ) as the 3-graph on V in which (u, v, w) spans an edge if and only if Γ|{u,v,w} either contains an isolated vertex of both in-degree and out-degree 0, or it contains a vertex of out-degree 2.

- Fact 2 ([FdF88]) If Γ is an arbitrary C4-free orgraph then the 3-graph FDF(Γ) is Tur´n.

Let now S ⊆ R be a ﬁnite subset such that x + y = 0 for any x, y ∈ S.

- Fact 3 ([FdF88]) The edge density of FDF (ΓK|Z3×S) tends to 4/9 as |S| → ∞.


Facts 1-3 together imply that πmin(I43) ≤ 4/9. Tura´n’s original construction [Tur41] corresponds to the case when all elements in S are positive. Brown’s examples [Bro83] are obtained when negative entries in S are allowed, but are always smaller in absolute value than all positive entries. Kostochka’s examples [Kos82] correspond to arbitrary sets S. While tiny variations of these examples are known in terms of conjectured exact values exmin(n; I43), asymptotically Tura´n 3-graphs of the form FDF(ΓK|Z3 × S) constitute the complete set of known extremal conﬁgurations. Statements of this sort are best formulated and viewed in a “limit” framework, and we defray further discussion until we review some material from Flag Algebras.

### 2.1. Flag Algebras

As we stated in Introduction, we do not attempt to give here a self-contained account of the general theory developed in [Raz07]. The sole purpose of this section is to introduce a little bit more of handy notation in addition to [Raz07] and ﬁx names (many of them are listed on the corresponding pictures) for concrete theories, interpretations, types, ﬂags etc. used in the rest of the paper.

- 2.1.1. Add-ons


We will call an open interpretation (U, I) : Tσ

1 Tσ

2 ([Raz07, Deﬁnition 4]) total if the relativizing predicate U is trivial, that is U(x) ≡ ⊤. All interpretations considered in this paper are total, and we omit U from all deﬁnitions and notation. A total interpretation I is global if additionally σ1 = σ2 = 0 are trivial types (global interpretations were considered in [Raz07, §2.3.3]). For a global interpretation I : T1 T2 and a type σ of the theory T2, we have the induced interpretation Iσ : T2I(σ) T1σ.

1

2

Any total interpretation I : Tσ

1 Tσ

2 deﬁnes an algebra homomorphism πI : Aσ

1

2

[T1] −→ Aσ

[T2] ([Raz07, Theorem 2.6]). If I is global and σ is a type of T2, π(Iσ) will be abbreviated to πI,σ. For any total interpretation I : Tσ

1

2

1 Tσ

2 and φ ∈ Hom+(Aσ

[T2], R), we abbreviate φπI ∈ Hom+(Aσ

1

2

2

[T1], R) to φ|I. Likewise, for φ ∈ Hom+(Aσ, R) and an injective mapping η : [k′] −→ [|σ|], φπσ,η ∈ Hom+(Aσ, R) ([Raz07, §2.3.1]) will be abbreviated to φ|η. η itself will be normally written down as its table [η(1), . . ., η(k′)] and, moreover, when k′ = 1, the brackets will be omitted. For example, for φ ∈ Hom+(Aσ, R), φ|2 means the composed homomorphism φπσ,2 def= φπσ,η, where η : [1] −→ [|σ|]; η(1) = 2.

1

Recall [Raz07, Deﬁnition 6] that f ≤σ g for f, g ∈ Aσ means that φ(f) ≤ φ(g) for any φ ∈ Hom+(Aσ, R). We naturally extend this notation to the case of arbitrary functions g1, . . ., gℓ, h1, . . ., hℓ : Rt −→ R, an arbitrary propositional formula A(p1, . . ., pℓ) and elements f1, . . ., ft ∈ Aσ as follows: A(g1(f1, . . ., ft) ≥ h1(f1, . . ., ft), . . ., gℓ(f1, . . ., ft) ≥ hℓ(f1, . . ., ft)) by deﬁnition means that A(g1(φ(f1), . . ., φ(ft)) ≥ h1(φ(f1), . . ., φ(ft)), . . ., gℓ(φ(f1), . . ., φ(ft)) ≥

hℓ(φ(f1), . . ., φ(ft))) is true for any φ ∈ Hom+(Aσ, R). For a non-degenerate type σ0 of size k0, φ ∈ Hom+(Aσ

, R) and an extension (σ, η) of σ0 with φ0((σ, η)) > 0, we well denote by Sσ,η(φ) the support of the probability measure Pσ,η [Raz07, Deﬁnition 8]. This is the minimal

0

closed subset of Hom+(Aσ, R) with the property P[φσ,η ∈ Sσ,η(φ)] = 1, and, as always, when σ0 = 0, η will be dropped from notation.

- 2.1.2. Names


In this section, we ﬁx notation for almost all concrete objects used in our paper.

Theories.

TTuran – the theory of 3-graphs without copies of I43. TFDF – the theory of C4-free orgraphs. TGraph – the theory of ordinary (simple, undirected) graphs. For a theory T, we denote by T∗ its extension obtained by introducing

three new unary predicate symbols χ0, χ1, χ2, together with the axioms

χa(v), ¬(χa(v) ∧ χb(v)) (a = b ∈ Z3).

a∈Z3

In other words, we augment the theory T with a Z3-coloring χ of the vertices not a priori related to the original structure provided by T.

Interpretations. For the general set-up see [Raz07, Section 2.3].

FDF : TTuran TFDF is the Fon-der-Flaass interpretation. Denoting the (only) predicate of the theory TTuran by E3, and the predicate of TFDF by E, we set

 

FDF(E3)(v0, v1, v2) def=

(va = vb) ∧

(E(va, va+1) ∧ E(va, va−1))

a∈Z3

a =b∈Z3

 .

∨

(¬E(va, va+1) ∧ ¬E(va, va−1) ∧ ¬E(va−1, va) ∧ ¬E(va+1, va))

a∈Z3

Orientation-erasing interpretation OE : TGraph TFDF is deﬁned in the obvious way. When working in the theory TFDF, we will systematically omit πOE and, for f ∈ A0[TGraph], abbreviate πOE(f) to f.

Color-erasing interpretation CET : T T∗ is also obvious. The subscript T is omitted whenever it is clear from the context.

I3 P¯3 P3 K3 Figure 2: Ordinary graphs on 3 vertices

The generalization OE∗ : T∗

Graph T∗

FDF is also straightforward (this interpretation does not aﬀect the Z3-coloring). Again, given f ∈ A0[T∗

Graph], we will abbreviate the element πOE∗πCE

TGraph(f) = πCE

TFDFπOE(f) to f.

All these interpretations are global. We will deﬁne one crucial non-global interpretation a little bit later, after introducing some more notation.

Models, Types and Flags.

For any theory T, 0 is the trivial type of size 0. In vertex-uniform ([Raz07, Deﬁnition 11]) theories TTuran, TFDF, TGraph, 1 is the only type of size 1.

TTuran ρ3 ∈ M3[TTuran] is an edge.

TGraph

M2[TGraph] consists of two elements: ρ (an edge) and ν (non-edge). |M3[TGraph]| = 4. Its elements, along with their adopted names, are listed

on Figure 2.

E is the type of size 2 that is an edge, and N is the type of size 2 that is non-edge.

e ∈ F21[TGraph] is an edge with one distinguished vertex. There are two ways to turn P¯3 into an 1-ﬂag: P¯31,c (by selecting the isolated vertex) and P¯31,b (by selecting any other). F3E[TGraph], F3N[TGraph] consist of four elements each; they are depicted on Figures 3, 4 respectively.

TFDF

α ∈ F21[TFDF] is a directed edge in which the tail vertex is labeled by 1. A is the type of size 2 with E(A) = { 1, 2 }, and B is the type of size 2 with E(B) = { 2, 1 }.

1 2 1 2 P¯3E P3E,b

1 2 1 2 P3E,c K3 Figure 3: E-ﬂags on 3 vertices

1 2 1 2 I3N P¯3N,c

1 2 1 2 P¯3N,b P3N Figure 4: N-ﬂags on 3 vertices

T∗

Graph

pa ∈ M1[T∗

Graph] is the one-vertex model colored by a ∈ Z3. ρa[νa] ∈ M2[T∗

Graph] is an edge [none-edge, respectively], in which both ends are colored by a, and ρa,b[νa,b] ∈ M2[T∗

Graph] is an edge [none-edge, respectively], in which the two ends are colored by a = b ∈ Z3.

T∗

FDF

For a ∈ Z3, (a) is the type of size 1 based on pa. For a = 1, 2, αa,3−a ∈ F2(a) is a directed edge in which the tail is colored by a and is labeled by 1, and the head is colored by 3 − a.

3 ∈ FN

Na is the type of size 2 based on νa. In the ﬂag PN

3 , the only free vertex v is colored by (3 − a), and it has the edges θ(1), v , v, θ(2) . PN

a

a

a,∗

3 ∈ FN

3 is obtained from PN

3 by reversing edges. Interpretations C, OC

a

a

One of our main tools in this paper is the (total) interpretation C : T∗

Graph TGraphE that acts identically on TGraph and, combinatorially, given an edge E of our graph, colors all other vertices in 3 colors according to Figure 5 (dotted lines mean the absence of an edge). Formally, the predicate

χ1 χ2

c1 c2

χ0

Figure 5: Interpretation C

symbol E(v, w) of the theory TGraph is interpreted by itself, and the new symbols χ0, χ1, χ2 are interpreted as



- C(χ0)(v) def= (E(c1, v) ≡ E(c2, v))
- C(χ1)(v) def= v = c1 ∧ E(c2, v) ∧ ¬E(c1, v)
- C(χ2)(v) def= v = c2 ∧ E(c1, v) ∧ ¬E(c2, v).




(1)



This construction commutes well with orientation. That is, we have a total interpretation OC : TFDF∗ TFDFA preserving oriented edges and introducing colors analogously to (1) but ignoring orientation on edges (formally, E(v, w) gets replaced by E(v, w) ∨ E(w, v)). We have the following commu-

tative diagram of interpretations: T∗

−−−→C TGraphE

Graph

OE∗  OEA

−−−→OC TFDFA

T∗

FDF

### 2.2. Main results and related conjectures

In the language of ﬂag algebras, we have:

(2)

- Conjecture 1 (Tur´an’s (3, 4)-conjecture) ρ3 ≥ 4/9.
- Conjecture 2 (Fon-der-Flaass conjecture) πFDF(ρ3) ≥ 4/9.

Let µ be any probability measure on Borel subsets of Z3 × R that is invariant under the action of S3 on the ﬁrst coordinate. This naturally (by replacing densities with obvious integrals, cf. [LS06]) leads to a homomorphism φµ ∈ Hom+(A0[TFDF], R). φµ|FDF(ρ3) = 4/9 for any such measure µ, and these φµ|FDF constitute the set of all known ψ ∈ Hom+(A0[TTuran], R) with the property ψ(ρ3) = 4/9.

Proposition 2.1 ([FdF88]) πFDF(ρ3) ≥ 3/7. Our new results are as follows:

- Theorem 2.2 πFDF(ρ3) ≥ 7/16.
- Theorem 2.3 a) P¯3 = 0 =⇒ πFDF(ρ3) ≥ 4/9. b) ρ ≥ 2/3−ǫ =⇒ πFDF(ρ3) ≥ 4/9, where ǫ > 0 is an absolute constant.


- 3. Warm-up: proof of Theorem 2.2


In this section we work in the theory TFDF; recall from Section 2.1.2 that we also use in this theory all notation introduced in TGraph via the orientationerasing interpretation OE.

It turns out that all computations become much more instructive and transparent if we replace critical quantities by the deviations from their values in (conjectured) extremal examples. In particular, we let



δ def= 4/9 − πFDF(ρ3); δρ def= 2/3 − ρ;



(3)

def= 2/9 − K3; δα def= 1/3 − α.

δK

3



Our ultimate goal is to prove δ ≤ 0, and our starting point is to re-write δ in the form

- 1

![image 11](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile11.png>)

- 2


3 − δρ − P¯3) − 3 δα2 1 (4)

δ =

(δK

(for the deﬁnition and properties of the averaging operator · σ see [Raz07, Section 2.2]). This is easily checked by expanding all these elements as linear combinations of the seven orgraphs on Figure 1.

The ﬁrst part

- 1

![image 12](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile12.png>)

- 2


f def=

3 − δρ − P¯3) (5)

(δK

in (4) actually belongs to (the image of) A0[TGraph] and, moreover, if we ignore for the time being the term P¯3, it corresponds to the classical problem of bounding from below the number of triangles in a graph with a given number of edges. Let us ﬁrst apply here Goodman’s simple bound K3 ≥ ρ(2ρ − 1) [Goo59]. In the tangential coordinates (3) it can be re-written as

5 3

δρ − 2δρ2 (6)

δK

3 ≤

![image 13](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile13.png>)

and, thus, since δα 1 = 12δρ, from (4) we get δ ≤

![image 14](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile14.png>)

1 3

1 3

- 1

![image 15](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile15.png>)

- 2


7 4

P¯3 − 3 δα2 1 ≤

δρ − δρ2 −

δρ2.

δρ −

![image 16](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile16.png>)

![image 17](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile17.png>)

![image 18](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile18.png>)

Note that Proposition 2.1 (that is, δ ≤ 631 ) already follows from this. Also, δρ ≤ 0 now implies the desired inequality δ ≤ 0, so in what follows we can and will assume δρ ≥ 0 (i.e., ρ ≤ 2/3).

![image 19](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile19.png>)

The optimal upper bound on K3 in terms of ρ in the range ρ ∈ [1/2, 2/3] was proved in [Fis89] and re-proved with diﬀerent methods in [Raz08, Nik07]. While it is not very intuitive in terms of K3: K3 ≥ (1−

√4−6ρ)(2+√4−6ρ)2

![image 20](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile20.png>)

![image 21](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile21.png>)

18 , it makes much more sense in the tangential coordinates (3):

![image 22](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile22.png>)

√6 3

![image 23](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile23.png>)

δρ3/2

δρ ≥ 0 =⇒ δK

3 ≤ δρ +

![image 24](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile24.png>)

(note that the bound is still formally true in the trivial region ρ ∈ [0, 1/2], although it is no longer optimal there). Combining this with (4), we get:

√6 6

![image 25](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile25.png>)

δρ3/2 − P¯3 − 3 δα2 1. (7) Theorem 2.2 is now immediate:

δ ≤

![image 26](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile26.png>)

√6 6

√6 6

![image 27](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile27.png>)

![image 28](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile28.png>)

- 3

![image 29](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile29.png>)

- 4


1 144

δρ3/2 − P¯3 − 3 δα2 1 ≤

δρ3/2 −

δρ2 ≤

δ ≤

![image 30](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile30.png>)

![image 31](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile31.png>)

![image 32](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile32.png>)

(the maximum is attained at δρ = 1/6), that is, πFDF(ρ3) ≥ 7/16.

## 4. Proof of Main Result

We begin with (4) as our starting point, and we ﬁrst give two examples illustrating that the task of improving Theorem 2.2 to δ ≤ 0 is more elaborate than it may appear.

Note that neither Proposition 2.1 nor our improvement Theorem 2.2 use C4-freeness. Our ﬁrst example shows that in order to get any further, it has to be used somehow.

- Example 1 Consider a random orientation of a complete balanced bipartite graph. This leads to φ ∈ Hom+(A0[TOrgraph], R) with φ(πFDF(ρ3)) = 7/16


(TOrgraph is the theory of arbitrary orgraphs, not necessarily C4-free). This can be checked either by a direct calculation or by observing that for this particular φ all inequalities that were used in the proof of Theorem 2.2 are tight.

Thus, we have to use the C4-freeness, and, looking at the proof of Theorem 2.2, our only chance is to use this assumption to show that the orientation

should be suﬃciently far from out-regular, i.e. that δα2 1 must be substantially larger than the trivial Cauchy-Schwarz bound δα2 1 ≥ 41δρ2 used in the proof of Theorem 2.2. Our second example demonstrates that even without induced copies of C4, it still can be of order only δρ3/2 (cf. (7)); in particular we can not hope to get away with Goodman’s bound (6).

![image 33](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile33.png>)

- Example 2 There exists φ ∈ Hom+(A0[TFDF], R) with φ(P¯3) = 0 and φ(f), φ( δα2 1) = Θ(φ(δρ3/2)). We deﬁne φ from a probability measure on Z3×R (cf. Section 2.2), only this time µ is not Z3-invariant, albeit very close to this. More precisely, let µ be the Lebesque measure on the set S def= {0}×[−1/6+δ0/2, 1/6−δ0/2] ∪ {1}×[−1/6−δ0/2, 1/6] ∪ {2}×[−1/6, 1/6+δ0/2],

and let φ ∈ Hom+(A0[TFDF], R) be the corresponding homomorphism. Then it is easy to calculate that

φ(δρ) =

3 2

![image 34](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile34.png>)

δ02 and (see (5))

φ(f) =

- 3

![image 35](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile35.png>)

- 4


δ03. (8)

On the other hand, φ( δα2 1) is the expectation of (α[(a, x)]−4/9)2, where (a, x) is sampled at random from S, and α[(a, x)] is relative out-degree of the vertex (a, x) ∈ S. Our set S, however, was speciﬁcally designed in such a way that α[(a, x)] can be diﬀerent from 4/9 only for x  ∈ [−1/6+δ0/2, 1/6−δ0/2] (that is, on a set of measure O(δ0)), and the diﬀerence itself is also O(δ0). Therefore, φ( δα2 1) = Θ(δ03) = Θ(φ(δρ))3/2.

The latter example is pivotal for our proof in the sense that our overall strategy is to show that it is as bad as it gets. Accordingly, the rest of the proof is split into two rather independent part. Firstly, we, arguing in the theory TGraph, prove that f ≥ 0 implies that the undirected graph resulting from our orgraph by ignoring orientation can be rather well approximated by a complete tripartite graph in which part 0 has density p0 < 1/3 with

- 3

![image 36](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile36.png>)

- 4


1 3 − p0 3 δ03 ≥ f (cf. (8)). This is done in Section 4.1, and this is where we use the full computational power of Flag Algebras. Then we concentrate on parts 1 and 2 in our tripartite graph and show that, like in Example

![image 37](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile37.png>)

- 2, the induced orgraph must contain Ω(δ0) vertices of relative out-degree signiﬁcantly smaller than δ0 that will give us the desired contribution to


δα2 1 (Section 4.2).

### 4.1. Finding a good coloring

In this section we will be mostly working with the theories TGraph, T∗

Graph. Keeping in line with (3), we also let

1 3 − p0.

δ0 =

![image 38](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile38.png>)

Further, deﬁne

κ def=

ρa +

νa,b;

a∈Z3

a =b∈Z3

this element measures the distance between our original (undirected) graph and the complete tripartite graph deﬁned by the coloring χ. We also let

κ def= ρ1 + ρ2 + ν1,2 and

κ′ def=

νa,b. (9) Our goal in this section is to prove the following. Theorem 4.1 Let φ ∈ Hom+(A0[TFDF], R) be such that

a =b∈Z3

φ(f) ≥ 0 (10) and either φ(P¯3) = 0 or φ(δρ) ≤ 10−6. Then there exists φ∗ ∈ Hom+(A0[T∗

FDF], R) with φ∗|CE = φ such that ψ∗ def= φ∗|OE∗ ∈ Hom+(A0[T∗

Graph], R) satisﬁes the following.

- a) δ0 ≥ 0;
- b) in the case φ(P¯3) = 0, κ = ρ0 (and, therefore, κ = κ′ = 0);
- c) δ02 ≤ 6δρ;
- d) f + 10−5κ ≤ 43δ03.


![image 39](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile39.png>)

Proof. Our coloring will not depend on the orientation (that is, ψ∗ will be completely determined by ψ def= φ|OE). Intuitively, we pick an edge e and Z3color our graph as shown on Figure 5. We choose e to minimize the density of bad edges κ. Then we permute colors if necessary (note that the element κ

is invariant under such permutation) to make sure that 0 is the least frequent color, ensuring property a).

Let us now begin the formal proof. Consider the random homomorphism φA rooted at φ, and choose a particular φA ∈ SA(φ) that:

- 1. minimizes πOE,A(K3E) if φ(P¯3) = 0;
- 2. minimizes πOE,AπC(κ) (see the commutative diagram (2)) if φ(δρ) ≤ 10−6.


Let ψ def= φ|OE and ψE def= φA|OEA ∈ Hom+(AE[TGraph], R). Note that in the ﬁrst case (φ(P¯3) = 0) the fact φA ∈ SA(φ) readily implies

ψE(P¯3E) = ψE|i(P¯31,b) = ψE|i(P¯31,c) = 0 (i = 1, 2), (11)

that is, copies of P¯3 are missing even if they contain one or two distinguished vertices.

In the ﬁrst case we simply let

φ∗ = φA|OC

(see again (2)). In the second case we additionally compose φA|OC with an appropriate color permuting automorphism of A0[TFDF∗ ] to make sure that the resulting homomorphism satisﬁes property a) in Theorem 4.1.

Let ψ∗ def= φ∗|OE∗ ∈ Hom+(A0[T∗

Graph], R). We check all four properties claimed in Theorem 4.1 one by one.

- Property a). In the second case (φ(δρ) ≤ 10−6) it follows from the construction.


If φ(P¯3) = 0 then we ﬁrst note that (by (11)) ψ∗(δ0) = ψE(1/3 − K3E). Now, we have the following calculation in TGraph:

1/3 − K3E E = 4f +

7 3

P¯3 + 2 (e − 2/3)2 1 ≥ 4f,

![image 40](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile40.png>)

which, along with φ(f) ≥ 0, implies φ( 1/3 − K3E E) ≥ 0 and thus there exists at least one extension ψE ∈ SE(ψ) such that

ψEK3E ≤ 1/3. (12) But by [Raz07, Theorem 4.1], the distribution of ψE is a convex combination of distributions of φA|OEA and φB|OEB. Since K3E is symmetric w.r.t. permuting labels, all three real-valued random variables ψEK3E, φA|OEA(K3E)

and φB|OEB(K3E) have identical distributions. And since our particular choice of φA minimizes φA|OEA(K3E), property a) follows from (12).

- Property b): by inspecting Figure 3. φ(P¯3) = 0 and (11) readily imply that the only non-zero contribution to ψ∗(κ) can be made by copies of K4E and, therefore, ψ∗(κ) = ψ∗(ρ0).

Checking the critical properties c) and d) is a typical (and rather cumbersome in the second case) calculation in the ﬂag algebras found with the help of a computer. Before we proceed, let us note that even if in the ﬁrst case φA|OEA was chosen to minimize K3E, it nonetheless minimizes φA(κ) (which in this case is the same as K4E by property b)) as well. Combinatorially this is obvious: ψ corresponds to a complete k-partite graph (with k possibly being countably inﬁnite) and both K3E and K4E are minimized by the same edges connecting the two largest parts. We omit a straightforward formal proof.

- Property c). Note that ψ∗(κ) = ψE(πC(κ)) (since κ is invariant under color-permuting automorphisms). On the other hand,


πC(κ) E ψ(ρ)

E ψE(πC(κ)) =

![image 41](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile41.png>)

([Raz07, Deﬁnition 10]). Since our chosen ψE ∈ SE(ψ) minimizes πC(κ) (as before, due to the fact that πC(κ) ∈ F3E[TGraph] is symmetric under the permutation of labels), we conclude that

ψ( πC(κ) E) ≥ ψ∗(κ)ψ(ρ). Lifting πC(κ) E and ρ to A0[T∗

Graph] via the color-erasing interpretation, we can simply say that ψ∗ obeys the inequality

πCE( πC(κ) E) ≥ κ · πCE(ρ). (13) Let



4 9

f1 def=

(1 − 9(p0p1 + p0p2 + p1p2)2)



![image 42](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile42.png>)

(14)

1 3

(p1 − p2)2)(1 + 3(p0p1 + p0p2 + p1p2)) ≥ δ02.

= (δ02 +

![image 43](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile43.png>)



a

a

a a

2/9

a

a

a b

- a
- b b


a

- a
- b c


a

−1/9 Figure 6: Values of 12f1

2/9

−1/9

![image 44](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile44.png>)

Let f2 ∈ A04[TGraph] be deﬁned as f2 def= 4( e2 1 − ρ2) + (P3N − 2I3N)2 N ≥ 0. (15)

Then the inequality in the property c) follows from (10), (13) (14), (15) and the inequality

f1 +2(πCE( πC(κ) E)−κ·πCE(ρ))+20πCE(f)+2πCE(f2) ≤ 6πCE(δρ). (16)

(16) itself is checked by a direct calculation of coeﬃcients in front of all models from A0[T∗

Graph] (there are 357 of them). It might be helpful to note that there is only one additive term in (16) that mixes up the two structures and re-write it as

- 1

![image 45](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile45.png>)

- 2


f1 + πCE( πC(κ) E + 10f + f2 − 3δρ); (17) note also that both sides here are invariant under permuting colors.

κπCE(ρ) ≥

Figure 6 tabulates the values of 21f1 for models in A0[T∗

Graph] where χ colors vertices according to the scheme shown in this ﬁgure (a, b, c ∈ Z3 are pairwise diﬀerent).

![image 46](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile46.png>)

Likewise, Figure 7 represents the element πC(κ) E + 10f + f2 − 3δρ ∈ A04[TGraph]. Then the inequality (17) basically says that if we arbitrarily align the ﬁrst or the second picture on Figure 6 with the third or fourth picture on Figure 7 (all other cases result in a non-positive coeﬃcient in the righthand side of (17) and hence are trivial), then for at least two edges their complement will contribute to κ. This is clear.

| |
|---|


| |
|---|


−2/9 −2/9

1/9

1/9

| |
|---|


−2/9 −85/18 −67/18 −68/9

−38/9 −29/9 −7/18 Figure 7: TGraph-part

- Property d). We form the element




- 3

![image 47](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile47.png>)

- 4


87 40

1 39240

f3 def=

δ03 − f +

κ′δρ −

κ −

![image 48](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile48.png>)

![image 49](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile49.png>)



43 160

(πCE( πC(κ) E) − κ · πCE(ρ)) ≤

(18)

![image 50](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile50.png>)

87 40

- 3

![image 51](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile51.png>)

- 4


δ03 − f +

κ′δρ − 2 · 10−5κ.

![image 52](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile52.png>)



We claim that f3 ≥ 0; let us ﬁrst check that is suﬃces for ﬁnishing the proof of property d). We only have to take care of the term 8740κ′δρ in (18).

![image 53](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile53.png>)

Indeed, if φ(P¯3) = 0 then ψ∗(κ′) = 0 by already proven part b), and we

are done. On the other hand, if 0 ≤ δρ ≤ 10−6 then 4087κ′δρ ≤ 4087κδρ ≤ 10−5κ, and f3 ≥ 0 still implies property d).

![image 54](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile54.png>)

![image 55](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile55.png>)

Our proof of f3 ≥ 0 is of distinct brute-force nature, and it is obtained by

ﬁnding a suﬃciently good rational approximation to the numerical outcome of the corresponding semi-deﬁnite program. Namely,

f3 ≥ δ0p0

8

491 654

1 5232

9 4

(p1 − p2)2 +

κ +

![image 56](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile56.png>)

![image 57](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile57.png>)

![image 58](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile58.png>)

i=1

Qi( gi) σ

, (19)

i

) tuples of elements from Aσ

where σ1, . . ., σ8 are types,  gi = (gi1, . . ., gid

, and Qi are positive semideﬁnite quadratic forms with integer coeﬃcients given by (di × di) positive semideﬁnite matrices Mi. More precisely, σ1 = σ2 def= 0. d1 = 4,  g1 def= (ν12, v01 + ν02, ρ1 + ρ2, ρ0), and

i

i



M1 def=

 



6549 5619 −598 −1468 5619 7868 −832 −2094 −598 −832 99 150 −1468 −2094 150 1406

.

 

d2 = 3,  g2 = (ν2 − ν1 − ρ02 + ρ01, ν02 − ν01, ρ2 − ρ1), and





1308 −598 −209

M2 def=

 .

−598 279 95 −209 95 39

 

The remaining types σ3, . . ., σ8 have size 2 and are based on the models ρ0, ν12, ρ1, ν01, ρ2, ν02, respectively. We assume that in the non-symmetric types σ4, σ6, σ8 the label 1 is received by the vertex that has smaller (o < 1 < 2) color. di = 12 (3 ≤ i ≤ 8), and  gi simply enumerates all ﬂags in Fσ

i

3

in a certain order. Let us specify this order, uniformly for all 3 ≤ i ≤ 8. For any type σ of size 2, every ﬂag F = (M, θ) ∈ F3σ[T∗

Graph] is uniquely determined by a triple (a, ǫ1, ǫ2) (a ∈ Z3, ǫi ∈ {0, 1}), where a is the color of the unique free vertex v ∈ V (M), and ǫi = 1 if and only if (θ(i), v) ∈ E(M). We enumerate F3σ by assigning the number j = 1 + 4a+ 2ǫ1 + ǫ2 to this ﬂag, and, for σ = σi, it is the jth element in  gi.

The matrices Mi are given by



837 0 0 999 470 −222 −222 −2 470 −222 −222 −2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 999 0 0 1209 565 −267 −267 −2 565 −267 −267 −2 470 0 0 565 1235 1487 1487 1317 −697 −1738 −1738 −1320 −222 0 0 −267 1487 6186 −661 2209 −1738 778 −6063 −2209 −222 0 0 −267 1487 −661 6186 2209 −1738 −6063 778 −2209

M3 def=



−2 0 0 −2 1317 2209 2209 1812 −1320 −2209 −2209 −1807

470 0 0 565 −697 −1738 −1738 −1320 1235 1487 1487 1317 −222 0 0 −267 −1738 778 −6063 −2209 1487 6186 −661 2209 −222 0 0 −267 −1738 −6063 778 −2209 1487 −661 6186 2209

 

 

−2 0 0 −2 −1320 −2209 −2209 −1807 1317 2209 2209 1812



2916 3470 3470 −4218 5950 6718 4584 −2394 5950 4584 6718 −2394 3470 4660 4128 −4644 6626 7794 5940 −3322 6464 6048 8854 −2436 3470 4128 4660 −4644 6464 8854 6048 −2436 6626 5940 7794 −3322



−4218 −4644 −4644 9928 −8710 −12116 −6680 3014 −8710 −6680 −12116 3014

M4 def=

5950 6626 6464 −8710 20386 19018 8784 −3532 7288 7046 5488 −6446 6718 7794 8854 −12116 19018 26982 13098 −2558 5488 10994 10042 −7774 4584 5940 6048 −6680 8784 13098 8742 −3386 7046 8466 10994 −4004

−2394 −3322 −2436 3014 −3532 −2558 −3386 3196 −6446 −4004 −7774 880

5950 6464 6626 −8710 7288 5488 7046 −6446 20386 8784 19018 −3532 4584 6048 5940 −6680 7046 10994 8466 −4004 8784 8742 13098 −3386 6718 8854 7794 −12116 5488 10042 10994 −7774 19018 13098 26982 −2558

 

−2394 −2436 −3322 3014 −6446 −7774 −4004 880 −3532 −3386 −2558 3196





16258 8232 8232 6430 3311 −1191 −1191 −3036 5681 −128 −128 −3056 8232 10089 7010 6750 −3325 −651 −1830 −3146 1142 −1394 −2761 −2975 8232 7010 10089 6750 −3325 −1830 −651 −3146 1142 −2761 −1394 −2975 6430 6750 6750 5338 −2682 −980 −980 −2485 862 −1657 −1657 −2348 3311 −3325 −3325 −2682 6397 485 485 1219 3141 2273 2273 1007

 

M5 def=

−1191 −651 −1830 −980 485 411 −47 456 −164 564 39 431 −1191 −1830 −651 −980 485 −47 411 456 −164 39 564 431 −3036 −3146 −3146 −2485 1219 456 456 1163 −424 763 763 1094

5681 1142 1142 862 3141 −164 −164 −424 2681 753 753 −503

 

−128 −1394 −2761 −1657 2273 564 39 763 753 1237 620 679 −128 −2761 −1394 −1657 2273 39 564 763 753 620 1237 679 −3056 −2975 −2975 −2348 1007 431 431 1094 −503 679 679 1045

 



M6 def=

25636 28299 16944 7514 4589 1193 7024 −8103 3037 450 3967 −11616 28299 35709 23685 8218 7024 3660 14870 −11277 3761 1519 5820 −14960 16944 23685 16839 5342 5547 3036 13047 −8122 2485 945 4210 −10189 7514 8218 5342 16801 −6821 −8516 −3230 −1058 −7132 −11326 −3312 −1718 4589 7024 5547 −6821 17546 4336 19158 −7091 10937 4364 6238 −7398 1193 3660 3036 −8516 4336 6926 5276 −1747 4273 7886 3242 −2104 7024 14870 13047 −3230 19158 5276 27620 −10496 10353 3134 7497 −10810



−8103 −11277 −8122 −1058 −7091 −1747 −10496 5243 −3855 −802 −3230 6125 3037 3761 2485 −7132 10937 4273 10353 −3855 7738 5140 4274 −4235

450 1519 945 −11326 4364 7886 3134 −802 5140 9786 3345 −1212 3967 5820 4210 −3312 6238 3242 7497 −3230 4274 3345 2958 −3730

 

−11616 −14960 −10189 −1718 −7398 −2104 −10810 6125 −4235 −1212 −3730 7536





16258 8232 8232 6430 5681 −128 −128 −3056 3311 −1191 −1191 −3036 8232 10089 7010 6750 1142 −1394 −2761 −2975 −3325 −651 −1830 −3146 8232 7010 10089 6750 1142 −2761 −1394 −2975 −3325 −1830 −651 −3146 6430 6750 6750 5338 862 −1657 −1657 −2348 −2682 −980 −980 −2485 5681 1142 1142 862 2681 753 753 −503 3141 −164 −164 −424

 

M7 def=

−128 −1394 −2761 −1657 753 1237 620 679 2273 564 39 763 −128 −2761 −1394 −1657 753 620 1237 679 2273 39 564 763 −3056 −2975 −2975 −2348 −503 679 679 1045 1007 431 431 1094

3311 −3325 −3325 −2682 3141 2273 2273 1007 6397 485 485 1219

−1191 −651 −1830 −980 −164 564 39 431 485 411 −47 456 −1191 −1830 −651 −980 −164 39 564 431 485 −47 411 456 −3036 −3146 −3146 −2485 −424 763 763 1094 1219 456 456 1163

 

 



25636 28299 16944 7514 3037 450 3967 −11616 4589 1193 7024 −8103 28299 35709 23685 8218 3761 1519 5820 −14960 7024 3660 14870 −11277 16944 23685 16839 5342 2485 945 4210 −10189 5547 3036 13047 −8122 7514 8218 5342 16801 −7132 −11326 −3312 −1718 −6821 −8516 −3230 −1058 3037 3761 2485 −7132 7738 5140 4274 −4235 10937 4273 10353 −3855 450 1519 945 −11326 5140 9786 3345 −1212 4364 7886 3134 −802 3967 5820 4210 −3312 4274 3345 2958 −3730 6238 3242 7497 −3230 −11616 −14960 −10189 −1718 −4235 −1212 −3730 7536 −7398 −2104 −10810 6125

M8 def=



.

4589 7024 5547 −6821 10937 4364 6238 −7398 17546 4336 19158 −7091 1193 3660 3036 −8516 4273 7886 3242 −2104 4336 6926 5276 −1747 7024 14870 13047 −3230 10353 3134 7497 −10810 19158 5276 27620 −10496

 

−8103 −11277 −8122 −1058 −3855 −802 −3230 6125 −7091 −1747 −10496 5243

We have little to add here but what was already said before: this is a sufﬁciently close rational approximation to a numerical solution of the corresponding SDP. (19) is checked by comparing coeﬃcients in front of all 357 models from A04[T∗

Graph]. The only noticeable piece of structure here is the observation that the inequality (19) is invariant under the automorphism permuting colors 1 and 2. Accordingly, Q1 and Q2 represent positive and

 

negative parts of the corresponding quadratic form (cf. [Raz10, Section 4]), and in the pairs (M5, M7) and (M6, M8) one matrix is obtained from the other by permuting rows and columns according to this automorphism.

Theorem 4.1 is proved.

![image 59](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile59.png>)

### 4.2. Finding vertices of low out-degree

Now we are ready to ﬁnish the proof of Theorem 2.3. Fix φ ∈ Hom+(A0[TFDF], R) such that either φ(P¯3) = 0 or φ(δρ) ≤ 10−6. We have to show that φ(δ) ≤ 0, where δ is given by (4).

If φ(f) ≤ 0, we are done. Otherwise we apply Theorem 4.1 and ﬁnd an extension φ∗ ∈ Hom+(A0[T∗

FDF], R) such that ψ∗ def= φ∗|OE∗ has all the properties required in its statement.

Before starting the formal argument, let us brieﬂy outline its combinatorial essence. What we have so far, is a Z3-coloring of our orgraph such that the color 0 is underrepresented (part a) of Theorem 4.1) by an amount δ0 that is relatively large with respect to f (part d)) and such that the tripartite (unordered) graph deﬁned by this coloring is very close to our original graph after disregarding its orientation.

Our argument focusses on the subgraph induced by colors 1 and 2. Let us imagine for a moment that κ = 0 (which is true anyway in the simple case φ(P¯3) = 0 by part b) of Theorem 4.1). Then this subgraph is an orientation of a complete bipartite graph that does not contain C4 and hence is acyclic. Therefore, there exists a vertex of out-degree 0 and in the original graph it has (relative) out-degree ≤ p0 = 13 −δ0. Proceeding by an obvious induction, we conclude that for any x, the fraction of vertices of relative out-degree ≤ 31 − δ0 + x is at least x, that gives us δα2 1 ≥ δ

![image 60](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile60.png>)

3 0

0 (δ0 − x)2dx = δ

3 . By part d) of Theorem 4.1, this suﬃces for our purposes.

0

![image 61](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile61.png>)

![image 62](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile62.png>)

The main complication is that in general the restriction of our original graph to colors 1 and 2 is not complete bipartite. But, fortunately, by part d) of Theorem 4.1, the diﬀerence between them is very small, namely, of order δ03, and we are going to exploit this fact. By Markov’s inequality, there are at most O(δ03/2) “bad” vertices of relative degree Ω(δ03/2) in the diﬀerence graph, and we ignore them. This leaves us with the situation when all vertices have a low (≪ δ0) degree in the diﬀerence graph, and the only non-trivial thing we have to show is that our previous argument (when the diﬀerence graph is empty) is suﬃciently stable to tolerate this imperfection.

Now we begin the formal proof. φ∗ ∈ Hom+(A0[T∗

FDF], R) is ﬁxed throughout the rest of the argument, so we will abbreviate φ∗(f) (f ∈ A0[T∗

FDF]) simply to f.

Let

√

ξ def=

![image 63](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile63.png>)

κ, and assume that x is a real parameter satisfying

7ξ < x ≤ min(p1, p2). (20) For a ∈ {1, 2} we let

Bada def= φ ∈ Hom+(A(a)[TFDF∗ ], R) φ(µ2(a)( κ)) > ξ

(recall from [Raz07, Section 4.3] that µ2(a)( κ) is the sum of all κ-based ﬂags F ∈ F2(a)[T∗

FDF]). Let also Bada(x) def= Bada ∪ φ ∈ Hom+(A(a)[TFDF∗ ], R) | φ(αa,3−a) < x .

p1, p2 > 0 by (20), thus we may consider random homomorphisms (φ∗)(a) rooted at φ∗ that we will abbreviate to φa. Let

ba def= pa · P[φa ∈ Bada] ; ba(x) def= pa · P[φa ∈ Bada(x)] . Note that

2

µ2(a)( κ) (a) which (by [Raz07, Deﬁnition 10]) translates to

κ =

a=1

2

pa · E φa(µ2(a)( κ)) . From this we conclude

κ =

a=1

2

paξ · P φa(µ2(a)( κ)) > ξ = ξ(b1 + b2). Thus,

κ ≥

a=1

κ ξ

b1 + b2 ≤

= ξ. (21)

![image 64](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile64.png>)

Our goal is to prove the lower bound b1(x) + b2(x) ≥ x − 6ξ, (22)

from which the main result will follow relatively easy by an integration on x, as explained in our informal description above.

If b1(x) = p1 or b2(x) = p2 then the bound trivially follows from the constraint (20).

Otherwise, closed subsets S(a)(φ∗) \ Bada(x) ⊆ Hom+(A(a), R) are nonempty, and we ﬁx φa ∈ S(a)(φ∗) \ Bada(x) that minimizes αa,3−a. Note that by the deﬁnition of Bada(x), φa(αa,3−a) ≥ x.

Next, we apply [Raz07, Theorem 4.1] to the label-removing interpretation T∗

FDF)(1) described in [Raz07, Section 2.3.1] and the homomorphism φ1 ∈ Hom+(A(1)[T∗

FDF (T∗

FDF], R). We conclude that the random homomorphism φ2 can be generated by ﬁrst choosing (under a speciﬁc distribution irrelevant to our purposes) a type σ of size 2 such that σ|a = (a) (a = 1, 2) and then computing (φ1)σ,1|2. Since φ2 ∈ S(2)(φσ), and Hom+(Aσ, R) are compact spaces, this implies the existence of a type σ with σ|a = (a) (a = 1..2) and φσ ∈ Sσ,1(φ1) such that φσ|2 = φ2.

φσ and φa = φσ|a will be ﬁxed for the rest of the argument, and we will also drop them from all our equations and inequalities.

Let Fa = (Γ, θ) ∈ F3σ be the ﬂag in which the only free vertex v ∈ V (Γ) receives color a, and the only new edge is θ(3 − a), v . Then

Fa ≥ πσ,2(α3−a,a) − πσ,1(µa2( κ)) ≥ x − ξ > 0, (23) where we used the fact φa  ∈ Bada(x) (a = 1, 2) and the restriction (20).

Next, F1F2 = 12(G0 + G1 + G2), where the ﬂags Ga = (Γa, θa) ∈ F4σ are deﬁned as follows. V (Γa) = {θa(1), θa(2), v1, v2}, Ga|θa(1),θa(2),vb = Fb (b =

![image 65](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile65.png>)

- 1..2) and the vertices v1, v2 are independent in G0 and span the edge v3−a, va in Ga. Note that G0 ≤ πσ( κ), thus we have


- 1

![image 66](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile66.png>)

- 2


(G1 + G2 + κ). (24)

F1F2 ≤

Let σa be the type of size 3 based on Fa (σa|[1,2] = σ, and the free vertex receives label 3). Given that φσ(Fa) > 0 by (23), we can form random extensions (φσ)σ

a,[1,2] of φσ that we will denote simply by φσ

. Let also G+a ∈ Fσ

a

4 be obtained from Ga ∈ F3σ by additionally labeling the vertex va

a

with label 3 (v3−a remains unlabeled). Then

E φσ

a

(G+a ) =

1 2

Ga Fa

.

![image 67](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile67.png>)

![image 68](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile68.png>)

Substituting this into (24), we get

F1F2 ≤

- 1

![image 69](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile69.png>)

- 2


κ +

a

FaE φσ

a

(G+a ) .

Next, we condition according to the event φσ

|3 ∈ Bada(x) and get the

a

estimate E φσ

(G+a ) ≤ F3−a · P[φσ

(G+a ) |φσ

|3 ∈ Bada(x)] + E φσ

|3  ∈ Bada(x)

a

a

a

a

(note that since G+a ≤ πσ

a,[1,2](F3−a), φσ

(G+a ) ≤ F3−a with probability 1). This leads us to

a



- 1

![image 70](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile70.png>)

- 2


F1F2P[φσ

F1F2 ≤

κ +

|3 ∈ Bada(x)]



a

a

(25)

(G+a ) |φσ

FaE φσ

+

|3  ∈ Bada(x) .

a

a



a

Applying once more [Raz07, Theorem 4.1] to the label-erasing interpretation T∗

FDF)σ, we can generate φa as a convex combination of distributions φσa′

FDF (T∗

|3 taken over those σ′

a ∈ Ext(σ, η) (η : [2] −→ [3], η(i) = i) in which χ(3) = a. In particular, looking at σ′

a = σa, we conclude that FaP[φσ

|3 ∈ Bada(x)] ≤ paP[φa ∈ Bada(x)] = ba(x). This takes care of the second term in (25):

a

F1F2 ≤

- 1

![image 71](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile71.png>)

- 2


κ +

a

F3−aba(x) +

a

FaE φσ

a

(G+a ) |φσ

a

|3  ∈ Bada(x) . (26)

(G+a ) |φσ

In order to bound the remaining term E[φσ

|3  ∈ Bada(x)], we ﬁx any particular φσ

a

a

∈ Sσ

a,[1,2](φσ) with φσ

|3  ∈ Bada(x). The already made observation based on [Raz07, Theorem 4.1] readily implies that φσ

a

a

|3 ∈ S(a)(φ∗). Given the way φa(= φσ

|a) was deﬁned, we conclude that

a

a

φσ

|3(αa,3−a) ≥ φσ

|a(αa,3−a), or, dropping as always the ﬁxed homomorphism φσ

a

a

from notation, πσ

a

a,a(αa,3−a). (27) Next,

a,3(αa,3−a) ≥ πσ

G+a ≤ πσ

a,[a,3]( PN

3 ). (28) We now use the fact that our orgraph is C4-free which implies

a

- 1

![image 72](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile72.png>)

- 2


3 PN

a,∗

PN

3 ≤

a

πN

( κ). (29)

a

This is simply because in every F = (Γ, θ) ∈ FN

4 , V (Γ) = {θ(1), θ(2), v, w} with F|{θ(1),θ(2),v} = PN

a

3 and F|{θ(1),θ(2),w} = P3Na,∗, v and w can not be independent (otherwise, we would have obtained a copy of C4) and thus the pair (v, w) contributes to κ.

a

a,1(αa,3−a). Similarly, PN

a,∗

3 + KN

Now, PN

3 + KN

2,1 ≤ πN

a,2(αa,3−a)− πN

2,1 ≥ πN

a

a

a

a,1(µ2(a)( κ)). Substracting, PN

a,1(µ2(a)( κ)). We lift this inequality to the algebra Aσ

a,∗

3 − PN

3 ≥ πN

a,2(αa,3−a) − πN

a,1(αa,3−a) − πN

a

a,[a,3]. Using also (27) and the fact φa  ∈ Bada, we see that

via πσ

a

a,[a,3]( PN

a,∗

πσ

3 ) ≥ πσ

a,[a,3]( PN

3 ) − ξ. Lifting to this algebra also the inequality (29), we conclude that πσ

a

a,[a,3]( PN

3 )· (πσ

a

![image 73](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile73.png>)

a,[a,3]( PN

a,[a,3]( PN

3 ) − ξ) ≤ 12 κ, from which we ﬁnd πσ

3 ) ≤ ξ + κ/2 ≤

a

a

![image 74](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile74.png>)

- 2ξ. Comparing this inequality with (28), we ﬁnally ﬁnd that for any φσ


∈ Sσ

a

a,[1,2](φσ) with φσ

|3  ∈ Bada(x), we have φσ

(G+a ) ≤ 2ξ. Thus, the bound (26) implies

a

a

F1F2 ≤

- 1

![image 75](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile75.png>)

- 2


κ +

a

F3−aba(x) + 2ξ

a

- 1

![image 76](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile76.png>)

- 2


κ +

Fa =

a

F3−a(ba(x) + 2ξ).

We can assume w.l.o.g. that F1 ≥ F2. Then we further have F1F2 ≤ 21 κ + F1(b1(x) + b2(x) + 4ξ). Dividing by F1 and taking into account (23), we complete the proof of (22) in the non-trivial case b1(x) < p1, b2(x) < p2.

![image 77](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile77.png>)

Comparing (22) with (21), and consulting the deﬁnitions of Bada and Bada(x), we see that

a

paP φa(αa,3−a) < x ∧ φa(µ2(a)( κ)) ≤ ξ ≥ x − 7ξ. (30)

On the other hand, applying once more [Raz07, Theorem 4.1] to the colorerasing interpretation, we observe that the distribution of φ1(α) is the convex combination of distributions φaπCE,(a)(α) (a ∈ Z3) with weights pa. Also,

1 3 − (δ0 − αa,3−a − µ2(a)( κ)).

πCE,(a)(α) ≤ αa,3−a + µ2(a)( κ) + p0 =

![image 78](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile78.png>)

Thus, (30) implies that for every x ∈ (7ξ, min(p1, p2)] we have the estimate

P 1/3 − φ1(α) > δ0 − x − ξ ≥ x − 7ξ. Integrating this inequality from 7ξ to min(p1, p2, δ0 − ξ),



min(p1,p2,δ0−ξ) 7ξ

δα2 1 = E (1/3 − φ1(α))2 ≥

(δ0 − x − ξ)2dx



1 3

(31)

((δ0 − 8ξ)3 − max(0, δ0 − ξ − p1, δ0 − ξ − p2)3) ≥

=

![image 79](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile79.png>)

1 3

((δ0 − 8ξ)3 − max(0, p2 − 2/3, p1 − 2/3)3).

![image 80](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile80.png>)



Now we are only left to take care of the case when either p1 or p2 are abnormally large. This requires one more simple calculation in A03[T∗

Graph]:

1 3

3 4

3 2

- 1

![image 81](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile81.png>)

- 2


p0p3−a + πCE(f) + (pa − 2/3)2 ≤

(pa − 2/3)

+

ρ0 +

(κ − ρ0).

![image 82](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile82.png>)

![image 83](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile83.png>)

![image 84](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile84.png>)

Since ψ(f) ≥ 0 by our assumption, we get from here (pa − 2/3) ≤ 23(κ − ρ0), and, substituting this into (31), we ﬁnally conclude that

![image 85](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile85.png>)

1 3

δα2 1 ≥

![image 86](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile86.png>)

(δ0 − 8ξ)3 −

27 4

(κ − ρ0)3 . (32)

![image 87](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile87.png>)

In the simple case ψ(P¯3) = 0, part b) of Theorem 4.1 implies ξ = κ =

κ−ρ0 = 0 and hence δα2 1 ≥ 13δ03. Now δ ≤ 0 follows from the bound f ≤ 34δ03 provided by part d) of Theorem 4.1.

![image 88](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile88.png>)

![image 89](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile89.png>)

On the other hand, when δρ is arbitrarily small, part c) of Theorem 4.1 implies that δ0 is also arbitrarily small, and then part d) implies κ ≤ κ ≤ O(δ03). Thus, (32) gives us δα2 1 ≥ δ03 13 − o(1) , and, again, δ ≤ 0 follows (for suﬃciently small δρ) from f ≤ 43δ03.

![image 90](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile90.png>)

![image 91](<2010-razborov-fon-der-flaass-interpretation-extremal-example_images/imageFile91.png>)

Theorem 2.3 is proved.

## 5. Conclusion

We have proved Tura´n’s conjecture for a natural class of 3-graphs that contain all Tura´n-Brown-Kostochka examples. This opens up a principal (but, admittedly, somewhat distant at the moment) possibility to attack the general case by trying to construct an inverse interpretation of the Fon-der-Flaass theory in the theory of Tura´n 3-graphs, possibly in some loose sense. It is still too early to tell, however, how promising is this approach.

A more accessible goal might be to remove extra assumptions from Theorem 2.3. Most likely, that should entail a signiﬁcant simpliﬁcation of our proof that, in our opinion, would be interesting in its own right.

## References

[Bro83] W. G. Brown. On an open problem of paul tura´n concerning 3graphs. In Studies in pure mathematics, pages 91–93. Birkh¨auser, 1983.

[Cae91] D. de Caen. The current status of Tura´n problem on hypergraphs. In Extremal Problems for Finite Sets, Visegr´d (Hungary), volume 3, pages 187–197. Bolyai Society Mathematical Studies, 1991.

[CL99] F. Chung and L. Lu. An upper bound for the Tura´n number t3(n, 4). Journal of Combinatorial Theory (A), 87:381–389, 1999.

[FdF88] D. G. Fon-der Flaass. Method for construction of (3,4)-graphs. Mathematical Notes, 44(4):781–783, 1988. Translated from Matematicheskie Zametki, Vol. 44, No. 4, pp. 546-550, 1988.

[Fis89] D. Fisher. Lower bounds on the number of triangles in a graph. Journal of Graph Theory, 13(4):505–512, 1989.

[Goo59] A. W. Goodman. On sets of acquaintances and strangers at any party. American Mathematical Monthly, 66(9):778–783, 1959.

[Kos82] A. V. Kostochka. A class of constructions for Tura´n’s (3, 4)problem. Combinatorica, 2(2):187–192, 1982.

[LS83] L. Lova´sz and M. Simonovits. On the number of complete subgraphs of a graph, II. In Studies in pure mathematics, pages 459–495. Birkha¨user, 1983.

[LS06] L. Lova´sz and B. Szegedy. Limits of dense graph sequences. Journal of Combinatorial Theory, Series B, 96(6):933–957, 2006.

[Man07] W. Mantel. Problem 28, solution by H. Gouwentak, W. Mantel, J. Teixeira de Mattes, F. Schuh and W.A. Wythoﬀ. Wiskundige Opgaven, 10:60–61, 1907.

[Nik07] V. Nikiforov. The number of cliques in graphs of given order and size. Manuscript, available at http://arxiv.org/abs/0710.2305v2 (version 2), 2007.

[Pik09] O. Pikhurko. The minimum size of 3-graphs without a 4-set spanning no or exactly three edges. Manuscript, 2009.

- [Raz07] A. Razborov. Flag algebras. Journal of Symbolic Logic, 72(4):1239– 1282, 2007.
- [Raz08] A. Razborov. On the minimal density of triangles in graphs. Combinatorics, Probability and Computing, 17(4):603–618, 2008.


[Raz10] A. Razborov. On 3-hypergraphs with forbidden 4-vertex conﬁgurations. SIAM Journal on Discrete Mathematics, 24(3):946–963, 2010.

[Sid95] A. F. Sidorenko. What we know and what we do not know about Tura´n numbers. Graphs and Combinatorics, 11:179–199, 1995.

[Tur41] P. Tura´n. Egy gra´felm´eleti sz´els¨o´ert´ekfeladatro´l. Mat. ´es Fiz. Lapok, 48:436–453, 1941.

