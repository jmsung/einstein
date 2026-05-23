---
type: source
kind: paper
title: Moments of Two-Variable Functions and the Uniqueness of Graph Limits
authors: Christian Borgs, Jennifer Chayes, Laszlo Lovasz
year: 2008
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/0803.1244v2
source_local: ../raw/2008-borgs-moments-two-variable-functions-uniqueness.pdf
topic: general-knowledge
cites:
---

arXiv:0803.1244v2[math.CO]8Dec2008

# Moments of Two-Variable Functions and the Uniqueness of Graph Limits

Christian Borgs Jennifer Chayes

Microsoft Research, Cambridge, MA L´aszl´ Lova´sz

Institute of Mathematics, E¨tvo¨s Lor´and University, Budapest, Hungary December 2008

Abstract

For a symmetric bounded measurable function W on [0,1]2 and a simple graph F, the homomorphism density

t(F,W) =

W(xi,xj)dx.

[0,1]V (F) ij∈E(F)

can be thought of as a “moment” of W. We prove that every such function is determined by its moments up to a measure preserving transformation of the variables.

The main motivation for this result comes from the theory of convergent graph sequences. A sequence (Gn) of dense graphs is said to be convergent if the probability, t(F,Gn), that a random map from V (Gn) into V (F) is a homomorphism converges for every simple graph F. The limiting density can be expressed as t(F,W) for a symmetric bounded measurable function W on [0,1]2. Our results imply in particular that the limit of a convergent graph sequence is unique up to measure preserving transformation.

## Contents

- 1 Introduction 2
- 2 Results 4

- 2.1 Graphons and Graph Densities . . . . . . . . . . . . . . . . . 4
- 2.2 Main results . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 2.3 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


- 3 Isomorphism 9

- 3.1 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
- 3.2 Push-Forward and Quotients . . . . . . . . . . . . . . . . . . . 11
- 3.3 Reductions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

- 3.3.1 Making a graphon strong . . . . . . . . . . . . . . . . . 14
- 3.3.2 Countable generation . . . . . . . . . . . . . . . . . . . 14
- 3.3.3 Merging inseparable elements . . . . . . . . . . . . . . 15
- 3.3.4 Lebesgue property . . . . . . . . . . . . . . . . . . . . 15
- 3.3.5 Partitions into Twin-Classes . . . . . . . . . . . . . . . 15


- 3.4 Isomorphism and Weak Isomorphism . . . . . . . . . . . . . . 17


- 4 Canonical Ensembles 18

- 4.1 Measure theoretic preparation . . . . . . . . . . . . . . . . . . 19
- 4.2 Anchor Sequences . . . . . . . . . . . . . . . . . . . . . . . . . 22


- 5 Coupling 23

- 5.1 Partially Labeled Graphs and Marginals . . . . . . . . . . . . 23
- 5.2 Multiple Edges . . . . . . . . . . . . . . . . . . . . . . . . . . 24
- 5.3 Coupling Anchor Sequences . . . . . . . . . . . . . . . . . . . 26
- 5.4 Conclusion of proofs . . . . . . . . . . . . . . . . . . . . . . . 30


- 6 Appendix: Moments and coupling of probability distributions 33


## 1 Introduction

Let W be the set of bounded symmetric measurable functions W : [0, 1]2 →

- R, and let W0 denote the set of functions in W with values in [0, 1]. For


every W ∈ W and every ﬁnite graph F, we deﬁne the integral t(F, W) =

W(xi, xj)

dxi . (1)

[0,1]n ij∈E(F)

i∈V (F)

Our interest in these integrals stems from graph theory (see next paragraph), but such integrals appear in physics, statistics, and other areas. In many respects, these integrals can be thought of as 2-variable analogues of moments of 1-variable functions, so instead of moment sequences, such 2-variable functions have a ”moment graph parameter” (function deﬁned on graphs). Just like moments of a 1-variable function determine the function up to measure preserving transformations, these “moments” determine the 2-variable function up to measure preserving transformations. The exact formulation and proof of this fact is the main goal of this paper.

Our main motivation for this study comes from the theory of convergent graph sequences. Let F and G be two simple graphs (graphs without loops and multiple edges). Let us map the nodes of F randomly into V (G), and let t(F, G) denote the probability that this map preserves adjacency. For example, t(K2, G) denotes the edge density of G. In general, we call t(F, G) the homomorphism density or simply the density of F in G.

We call a sequence of simple graphs (Gn) convergent, if t(F, Gn) has a limit for every simple graph F. The notion of convergent graph sequences was introduced by Borgs, Chayes, Lova´sz, S´os and Vesztergombi [2], see also [3], and further studied in [4] and [5]. Lova´sz and Szegedy [11] proved that every convergent graph sequence has a “limit object” in the form of a function W ∈ W0 in the sense that

t(F, Gn) −→ t(F, W) as n → ∞ (2)

for every simple graph F. In this case we say that Gn converges to W. It was also shown in [11] that for every function W ∈ W0 there is a convergent sequence (Gn) of simple graphs converging to W. To complete the picture, the results in this paper imply that the limit object is unique up to measure preserving transformations.

## 2 Results

For the precise statement of our results, we need some deﬁnitions. Instead of the interval [0, 1], we consider two-variable functions on an arbitrary probability space; while this does not add real generality it leads to a cleaner picture. We need a few deﬁnitions.

We start by recalling some basic notions from probability theory. Let (Ω, A, π) be a probability space (where Ω is the underlying set, A is a σalgebra on Ω, and π is a probability measure on A). As usual, (Ω, A, π) is called complete if A contains all sets of external measure 0, and the completion of (Ω, A, π) is obtained by replacing A with the σ-algebra generated by A and all subsets N ⊂ Ω of external measure 0.

Let (Ω, A, π) and (Ω′, A′, π′) be probability spaces, and let φ be a measure preserving map from Ω to Ω′. The map φ is called an isomorphism if it is a bijection between Ω and Ω′ and both φ and φ−1 are measure preserving, and it is called an isomorphism mod 0 if there are null sets N ∈ A and N′ ∈ A′ such that the restriction of φ to Ω \ N is an isomorphism between Ω \ N and Ω′ \ N′ (equipped with the suitable restrictions of (A, π) and (A′, π′), respectively). In the last case (Ω, A, π) and (Ω′, A′, π′) are called isomorphic mod 0.

It turns out that several of our results require a little bit more structure than that of an arbitrary probability space. In particular, we will consider Lebesgue spaces, i.e., complete probability spaces that are isomorphic mod 0 to the disjoint union of a closed interval (equipped with the standard Lebesgue sets and Lebesgue measure) and a countable set of atoms.1

- 2.1 Graphons and Graph Densities We are now ready to introduce the main objects studied in this paper.


![image 1](<2008-borgs-moments-two-variable-functions-uniqueness_images/imageFile1.png>)

1See [13], Section 2.2 for an axiomatic deﬁnition of Lebesgue spaces, and Section 2.4 for the proof that a probability space is Lebesgue if and only if it is isomorphic mod 0 to the disjoint union of a closed interval and a countable set of atoms.

Starting from an arbitrary probability space (Ω, A, π), let W : Ω×Ω → R be a bounded, symmetric function measurable with respect to the completion of (Ω×Ω, A×A, π×π). We call the quadruple H = (Ω, A, π, W) a graphon, and refer to W as a graphon on the probability space (Ω, A, π). (As discussed above, such functions can be thought of as limits convergent graph sequences, which explains the name).

From our point of view, graphons obtained by changing W on a set of measure 0, or changing the σ-algebra A so that W remains measurable, do not diﬀer essentially from the original. However, for technical reasons we have to distinguish them. We say that a graphon is strong, if W is measurable with respect to A×A (not just the completion of it). We can always change W on a set of measure 0 to make the graphon strong (Theorem 3.2(i)).

We say that H is complete, if the underlying probability space is complete, and we say that it is Lebesguian, if the underlying probability space is a Lebesgue space. The completion, H, of H is obtained by completing the underlying probability space, i.e., by replacing A by its completion A.

![image 2](<2008-borgs-moments-two-variable-functions-uniqueness_images/imageFile2.png>)

![image 3](<2008-borgs-moments-two-variable-functions-uniqueness_images/imageFile3.png>)

Let H = (Ω, A, π, W) be a graphon, and let F be a ﬁnite graph with

- V (F) = {1, . . ., k}. The deﬁnition (1) then can be extended as


t(F, H) =

Ωk

W(xi, xj)

ij∈E(F)

k

dπ(xi). (3)

i=1

Let H = (Ω, A, π, W) and H′ = (Ω′, A′, π′, W′) be two graphons. The goal of this paper is to determine necessary and suﬃcient conditions under which

t(F, H) = t(F, H′) (4) for all graphs F.

To this end, we will introduce two diﬀerent notions of isomorphism. Both will be expressed in terms of the following operation: given a graphon H′ = (Ω′, A′, π′, W′) and a measure preserving map φ from a probability space (Ω, A, W) into (Ω′, A′, π′), let (W′)φ be “pull-back” of W′, deﬁned by (W′)φ(x, y) = W(φ(x), φ(y)). If H = (Ω, A, π, W) and G = (Γ, B, ρ, U) are

two graphons and φ : Ω → Gamma is measure preserving from the completion A into B such that W = Uφ almost everywhere, then we call φ a weak isomorphism from H to G. Note that a weak isomorphism is not necessarily invertible.

![image 4](<2008-borgs-moments-two-variable-functions-uniqueness_images/imageFile4.png>)

We say that H and H′ are isomorphic mod 0 (in notation H′ ∼= H′), if there exists a map φ : Ω → Ω′ such that φ is an isomorphism mod 0 and (W′)φ = W almost everywhere in Ω × Ω. For simplicity, we often drop the qualiﬁer mod 0.

We call H and H′ weakly isomorphic if there is a third graphon G and weak isomorphisms from H and H′ into G. It will follow from Theorems 3.2 and 2.1 that we could require here that G is a strong Lebesguian graphon.

The isomorphism relation ∼= is clearly an equivalence relation, and it will follow from Theorem 2.1 (ii) below that weak isomorphism is an equivalence relation as well. Every graphon is weakly isomorphic with its completion, and every pair of isomorphic graphons is weakly isomorphic. It is clear that if two graphons H and H′ are weakly isomorphic then (4) holds for every graph H. Theorem 2.1 (ii) below will show that the converse also holds.

To state our results, we need one more notion, the notion of twins. Let H = (Ω, A, π, W) be a graphon. Two points x1, x2 ∈ Ω are called twins if

- W(x1, y) = W(x2, y) for almost all y ∈ Ω. Note that relation of being twins is an equivalence relation. We call the graphon H almost twin-free if all there exists a set N of measure zero such that no two points in Ω \ N are twins.


- 2.2 Main results With these deﬁnitions, we can state our main result:


- Theorem 2.1 (i) If H and H′ are almost twin-free Lebesguian graphons, then (4) holds for every simple graph F if and only if H ∼= H′.


(ii) If H and H′ are general graphons, then (4) holds for every simple graph F if and only if H and H′ are weakly isomorphic.

A natural idea of the proof of Theorem 2.1 is the following: can we bring a graphon (Ω, A, π, W) to a “canonical form”, so that isomorphic or weakly isomorphic graphons would have identical canonical forms? In the case of functions in a single variable, this is possible, through “monotonization”: for every bounded real function on [0, 1] there is an unique monotone increasing left-continuous function on [0, 1] that has the same moments.

In Section 4 we’ll construct not quite a canonical form, but a “canonical ensemble”, a probability distribution (Hα) of graphons on the same σ-algebra such that H ∼= Hα for almost all α, and two graphons are isomorphic if and only if their ensembles can be coupled so that corresponding graphons are identical (up to sets of measure 0).

An important element of the proof is a curious measure-theoretic fact. Consider a 2-variable function for which all 1-variable functions obtained by ﬁxing one of the variables are measurable. This of course does not in general imply that the 2-variable function is measurable, but it does imply it in some circumstances (see e.g. Corollary 4.2).

As we will see, the second statement of Theorem 2.1 can easily be deduced from the ﬁrst. In fact, we’ll show that every graphon is weakly isomorphic to a twin-free Lebesguian graphon. (See Theorem 3.2 for more details of this isomorphism.)

We can also transform a Lebesguian graphon into a graphon whose underlying probability space is the unit interval with the Lebesgue measure, by “resolving” the atoms into intervals of the appropriate length. This form is the most elementary and therefore useful in applications; however, it is not so convenient for the purposes of this paper because we loose twin-freeness.

It is easy to see that if H and H′ are weakly isomorphic, then (4) holds not only for simple graphs F but also for graphs with multiple edges (which we’ll call multigraphs if we want to emphasize that multiple edges are allowed; but we don’t allow loops). Thus (4) for simple graphs implies this equation for multigraphs. (This fact will be an important step in the proof, see Section 5.2.)

We can formulate our results in a probabilistic way. Recall that a coupling between two probability spaces (Ω, A, π) and (Ω′, A′, π′) is a probability distribution on A × A′ whose marginals are π and π′, respectively. A coupling between two graphons means a coupling between their underlying probability spaces. Let H = (Ω, A, π, W) be a graphon, and let X1, . . ., Xn be independent random samples from π. Then we have

t(F, H) = E

W(Xi, Xj) .

ij∈E(F)

Let H = (Ω, A, π, W) and H′ = (Ω′, A′, π′, W′) two graphons, and suppose that there exists a coupling γ between them such that W(X1, Y1) = W′(X2, Y2) holds with probability 1 for two independent samples (X1, X2) and (Y1, Y2) from γ. In this case clearly (4) holds for every graph F. As we will see, Theorem 2.1 implies that in the Lebesguian case the converse also holds.

We sum up the results for the most important special case of functions in W, i.e., bounded, symmetric functions W : [0, 1]2 → R which are measurable with respect to the Lebesgue sets on [0, 1]2 (the Corollary would remain valid for arbitrary Lebesguian graphons, but this would not be essentially more general).

- Corollary 2.2 For two functions W, W′ ∈ W the following are equivalent.


- (a) For every simple graph F, t(F, W′) = t(F, W).
- (b) For every multigraph F, t(F, W′) = t(F, W).
- (c) There exists a function U ∈ W and two measure preserving maps

ϕ, ψ : [0, 1] → [0, 1] such that W = Uϕ and W′ = Uψ almost everywhere.

- (d) There exist two measure preserving maps ϕ, ψ : [0, 1] → [0, 1] such

that (W′)ϕ = Wψ almost everywhere.

- (e) There exists a probability measure γ on [0, 1] × [0, 1] such that each


marginal of γ is the Lebesgue measure, and if (X, X′) and (Y, Y ′) are two independent samples from γ, then W(X, Y ) = W′(X′, Y ′)) with probability

- 1.


- 2.3 Examples The property of being twin-free is crucial for Theorem 2.1 (i).


- Example 1 Let φk : [0, 1] → [0, 1] be the map φk(x) = kx (mod 1). For

any function W ∈ W, the functions Wφ

2

and Wφ

3

deﬁne graphons that are weakly isomorphic but in general not isomorphic. Indeed, for a “generic” W (say W = xy), every point has two twins in Wφ

2

and three twins in Wφ

3

.

The pair of maps in Corollary 2.2 (c) go from W, while in (d), they go into (Wφ

3

)φ

2

= (Wφ

2

)φ

3

= Wφ

6

. Our next example shows that the Lebesgue property is also needed.

- Example 2 Let Ω be a subset of [0, 1] with inner Lebesgue measure 0 and outer Lebesgue measure 1, and let Ω′ be its complement. Let A and A′ consist of the traces of Lebesgue measurable sets on Ω and Ω′, respectively. Let W and W′ be the restrictions of the function xy to Ω × Ω and Ω′ × Ω′, respectively. The identical embeddings ϕ : Ω → [0, 1] and ϕ′ : Ω′ → [0, 1] are measure preserving, and hence H = (Ω, A, π, W) and H′ = (Ω′, A′, π′, W′) are weakly isomorphic. But for every x ∈ Ω, we have

2

Ω

W(x, y) dπ(y) = x ∈/ Ω′,

which shows that there is no way to “match up” the points in Ω and Ω′ to get an isomorphism mod 0. The same example shows that conclusions (d), (e) in Corollary 2.2 could not be extended to the non-Lebesgue case either.

- 3 Isomorphism


The main goal of this section is to describe how a general graphon can be transformed into a twin-free Lebesguian graphon. To this end, we have to recall some basic notions from measure theory (mostly because their usage does not seem standard), and then discuss diﬀerent “isomorphism-like” mappings between graphons.

### 3.1 Preliminaries

For a set S of subsets of a set Ω, we denote by σ(S) the σ-algebra generated by S. We call a σ-algebra A countably generated if there is countable set

- S ⊆ A such that σ(S) = A. This is equivalent to the existence of a sequence


A1 ⊆ A2 ⊆ . . . of ﬁnite σ-algebras whose union generates A.

We say that a set S ⊆ A is a basis for the probability space (Ω, A, π), if σ(S) is dense in A, i.e., for every X ∈ A there is a Y ∈ σ(S) such that π(X△Y ) = 0.

Given sets A ⊂ Ω and two points x, y ∈ Ω, we say that A separates x and y if |{x, y} ∩ A| = 1. We say that a set S of subsets of Ω separates x and y if there exists a set A ∈ S that separates x and y. This leads to a partition P[S] of Ω by placing two points in the same class if and only if they are not separated by S. We say that S is separating if it separates any two points in Ω. We’ll say that a graphon is separating if its underlying σ-algebra is separating.

A probability space (Ω′, A′, π′) is called a full subspace of (Ω, A, π) if Ω′ is a (not necessarily measurable) subset of Ω of external measure 1, A′ = {A ∩ Ω′ | A ∈ A}, and π′(A ∩ Ω′)) = π(A) for all A ∈ A.

Consider two probability spaces (Ω, A, π) and (Ω′, A′, π′) and a measure preserving map φ : Ω → Ω′. The map φ is called an embedding of the ﬁrst space into the second if φ is an isomorphism between (Ω, A, π) and a full subspace of (Ω′, A′, π′). We call φ an embedding of a graphon H = (Ω, A, π, W) into a graphon H′ = (Ω′, A′, π′, W′) if φ is an embedding of (Ω, A, π) into (Ω′, A′, π′) and (W′)φ = W almost everywhere.

Let (Ω, A, π) be a probability space and f : Ω → R, a bounded Ameasurable function. Let A0 ⊆ A be a sub-σ-algebra. The conditional expectation E(f | A0) is the set of all A0-measurable function f′ such that

f′ dπ for all A0 ∈ A0. It is well known that such functions exist and any two such functions diﬀer only on a set of π-measure 0. We’ll write (somewhat sloppily) f′ = E(f | A0) instead of f′ ∈ E(f | A0). We say that f is almost A0-measurable, if there is an A0-measurable function f′ such

A0 f dπ = A

0

that f = f′ π-almost everywhere. Clearly we must have f′ ∈ E(f | A0), and it does not matter which representative of E(f | A0) we choose, so (again somewhat sloppily) we can say that f is almost A0-measurable if and only if f = E(f | A0) almost everywhere.

### 3.2 Push-Forward and Quotients

Let (Ω, A, π) and (Ω′, A′, π′) be probability spaces and let φ : Ω → Ω′ be a measure preserving map. We have described how to “pull back” a graphon on (Ω′, A′, π′) to a (weakly isomorphic) graphon on (Ω, A, π). It is also possible to “push-forward” a graphon H = (Ω, A, π, W) to a graphon (Ω′, A′, π′, Wφ). This is deﬁned by the requirement that

Wφ(x′, y′)dπ′(x′)dπ′(y′) =

W(x, y) dπ(x) dπ(y) (5)

A′1×A′2

φ−1(A′1)×φ−1(A′2)

for all A′1, A′2 ∈ A′. The next lemma states that the “push-forward” Wφ is well deﬁned, and that (Wφ)φ is a certain conditional expectation of W.

- Lemma 3.1 Let (Ω, A, π) and (Ω′, A′, π′) be probability spaces, let φ : Ω → Ω′ be a measure preserving map, and let W be a graphon on (Ω, A, π).


(i) There exists a bounded, symmetric function Wφ : Ω′ × Ω′ → R that is A′ × A′ measurable and satisﬁes (6). It is unique up to changes on a set of measure zero in Ω′ × Ω′.

- (ii) Let Aφ = φ−1(A′). Then (Wφ)φ = E(W | Aφ×Aφ) almost everywhere.
- (iii) If φ is an embedding of (Ω, A, π) into (Ω′, A′, π′), then (Wφ)φ = W


almost everywhere.

Proof. (i) By linearity, it is easy to see that we can restrict ourselves to the case where W takes values in [0, 1]. Deﬁne a measure µ on A′ × A′ by

µ(A′1 × A′2) =

W(x, y) dπ(x) dπ(y)

φ−1(A′1)×φ−1(A′2)

for A′1, A′2 ∈ A. With this deﬁnition, we have that 0 ≤ µ(A′1 × A′2) ≤ π(φ−1(A′1))π(φ−1(A′2)) = (π′ × π′)(A′1 × A′2),

implying in particular that µ is absolutely continuous with respect to π′×π′. Hence the Radon-Nikodym derivative,

dµ d(π′ × π′)

Wφ =

, (6)

![image 5](<2008-borgs-moments-two-variable-functions-uniqueness_images/imageFile5.png>)

is well deﬁned. Using the above bound once more, together with the fact that µ(A1 × A2) = µ(A2 × A1), we furthermore have that

0 ≤ Wφ(x, y) ≤ 1 and Wφ(x, y) = Wφ(y, x) (7)

almost everywhere. Changing Wφ on a set of measure zero, we may assume that these relations hold everywhere. To deﬁne Wφ for a general bounded function W, we use linearity.

(ii) Let A1, A2 ∈ Aφ, i.e., let A1 = φ−1(A′1) and A2 = φ−1(A′2) for some

- A′1, A′2 ∈ A′. By the deﬁnition of Wφ, the fact that φ is measure preserving, and the deﬁnition of (Wφ)φ, we have that


W(x, y) dπ(x) dπ(y) =

Wφ(x′, y′) dπ′(x′) dπ′(y′)

A1×A2

A′1×A′2

=

Wφ(φ(x), φ(y)) dπ(x) dπ(y)

A1×A2

=

(Wφ)φ(x, y) dπ(x) dπ(y).

A1×A2

This implies that (Wφ)φ = E(W | Aφ × Aφ) almost everywhere.

(iii) Since φ is an isomorphism between (Ω, A, π) and a subspace of (Ω′, A′, π′), we know that given any A ∈ A, we can ﬁnd an A′ ∈ A′ such that φ(A) = A′ ∩ φ(Ω). But then φ−1(A′) = φ−1(φ(A)) = A, proving that A ∈ Aφ. Thus Aφ = A, which implies that (Wφ)φ = W almost everywhere.

We can use the “push-forward” construction to deﬁne quotients of graphons. Let H = (Ω, A, π, W) be a graphon, let P be an arbitrary partition of Ω into disjoint sets, and for x ∈ Ω, let [x] denote the class in P that contains the point x. We then deﬁne a graphon H/P = (Ω/P, A/P, π/P, W/P) and a measure preserving map φ : Ω → Ω/P as follows: the points in Ω/P are the classes of the partition P, φ is the map φ : x  → [x], A/P is the σ-algebra consisting of the sets A′ ⊂ Ω/P such that φ−1(A′) ∈ A, and (π/P)(A′) := π(φ−1(A′)). Then φ is measure preserving, and the function W/P = Wφ is deﬁned by (5).

### 3.3 Reductions

Now we are able to state the theorem that allows us to reduce every graphon to a twin-free Lebesguian graphon.

- Theorem 3.2 (i) Let H = (Ω, A, π, W) be a graphon. Then one can change the value of W on a set of π × π-measure 0 to get a strong graphon.


- (ii) Let H = (Ω, A, π, W) be a graphon. Then there exists a countably

generated σ-algebra A0 ⊂ A such that W is (A0 × A0)-measurable.

- (iii) Let H = (Ω, A, π, W) be a graphon. Then the graphon H/P[A] is

separating. If H is countably generated, then so is H/P[A].

- (iv) Let H = (Ω, A, π, W) be a separating graphon on a probability space


with a countable basis. Then the completion of H can be embedded into a Lebesguian graphon.

(v) Let H = (Ω, A, π, W) be a graphon, and let P be the partition into the twin-classes of H. Then H/P is almost twin-free. If H is Lebesguian, then H/P is Lebesguian as well. Furthermore, the projection H → H/P is a weak isomorphism.

- Corollary 3.3 Every graphon has a weak isomorphism into a strong Lebesguian graphon.


The proof of this theorem (which is not hard, but technical) will be given in the rest of this section.

- 3.3.1 Making a graphon strong

Let H = (Ω, A, π, W) be a graphon, and let W′ = E(W | A × A). Then W′ is A × A-measurable, and changing W′ on a set of measure 0, we may assume that W′ is symmetric and bounded. Moreover, A×A

′

(W′ − W) = 0

- for all A, A′ ∈ A, which implies that S(W′ − W) = 0 for all sets S in the completion of A × A, so W = W′ almost everywhere. These observations prove part (i) of the Theorem.


- 3.3.2 Countable generation


We prove a simple lemma, which implies Theorem 3.2(ii), and will also be used at several other places (Sections 4.1 and 5.2).

- Lemma 3.4 Let (Ω, A) and (Ω′, A′) be measurable spaces, and let W : Ω × Ω′ → R be a bounded, (A × A′)-measurable function. Then there exist countably generated σ-algebras A0 ⊂ A and A′0 ⊂ A′ such that W is (A0 × A′0)-measurable.


Proof. Let C be the set of bounded, (A × A′)-measurable functions W for which the statement of the lemma is true. The set C is clearly a vector space that contains the constant function 1 as well as the indicator functions of all rectangles A × B with A ∈ A and B ∈ A′. If is further not hard to show that if (Wk) is a sequence of non-negative functions in C and Wk ↑ W for a bounded function W, then the limiting function W is in C as well. By the monotone class theorem (see, e.g., Theorem 3.14 in [14]), we conclude that C contains all bounded functions which are measurable with respect to the σ-algebra generated by the rectangles A × B, i.e., the σ-algebra A × A′.

- 3.3.3 Merging inseparable elements

If we identify elements in the same class of the partition P[A], we get a σ-algebra which is isomorphic under the obvious map. This implies (iii) of Theorem 3.2.

- 3.3.4 Lebesgue property

Consider a separating graphon H = (Ω, A, π, W), and assume that A is generated by the countable set S. Then S is a basis for the completion of (Ω, A, π). We invoke the fact (see e.g. [13], Section 2.2) that any separating complete probability space with a countable basis can be embedded into a Lebesgue space. Thus there exists an embedding ψ of the completion of (Ω, A, π) into a Lebesgue space (Ω′, L′, λ′). Let W′ be the push-forward of W, W′ = Wψ. By Lemma 3.1, we have that (W′)ψ = W almost everywhere, which shows that ψ is an embedding of the completion of H into (Ω′, L′, λ′, W′). This proves part (iv) of Theorem 3.2.

- 3.3.5 Partitions into Twin-Classes


We prove (v) in Theorem 3.2. We may assume that A is countably generated. Indeed, by Lemma 3.4, we can replace A by a countably generated σ-algebra A0. This does not change the relation of being twins: Two points x, x′ ∈ Ω are twins if and only if the set Ax,x′ = {y ∈ Ω : W(x, y) = W(x, y′)} has measure 1. Since W is measurable with respect to A0 ×A0, the set Ax,x′ lies in A0 ⊂ A, implying that x and x′ are twins with respect to H if and only if they are twins with respect to H0.

Let AP consists of those sets in A that do not separate any pair of twin points. Clearly AP is a σ-algebra. Claim 1 W is almost AP × AP-measurable.

Let W = E(W | AP × AP). We want to prove that

W(x, y)dπ(x)dπ(y) =

A×B

W(x, y)dπ(x)dπ(y) (8)

A×B

- for all A, B ∈ A. Deﬁne the functions


gA = E(1A | AP), UA(y) =

W(x, y)dπ(x), VA(x) = W(x, y)gA(y)dπ(y).

A

Since UA(y) = UA(z) if y, z are twins, the function UA is AP-measurable, similarly for VA, and obviously for gA. Repeatedly using the fact that fg =

fE(g | A0) if f is A0-measurable, this implies

W(x, y)dπ(x)dπ(y) = 1B(y)UA(y)dπ(y) = gB(y)UA(y)dπ(y)

A×B

= VB(x)1A(x)dπ(x) = VB(x)gA(x)dπ(x)

= W(x, y)gA(x)gB(y)dπ(x)dπ(y)

= W(x, y)gA(x)gB(y)dπ(x)dπ(y)

=

W˜ (x, y)dπ(x)dπ(y).

A×B

(where the last equality follows since W is AP × AP-measurable). This implies (8) and completes the proof of Claim 1.

Let W = E(W | AP × AP) as before, then HP = (Ω, AP, π, W) is a graphon, which is clearly weakly isomorphic to (Ω, A, π, W). Let N be the set of points x ∈ Ω for which {y ∈ Ω : W(x, y) = W(x, y)} has positive measure. Then clearly N is a null set, and two points x, x′ ∈ Ω\N are twins in H if and only if they are twins in HP. The graphon H/P is obtained from HP by identifying indistinguishable elements, which implies that H/P is twin-free.

To prove that H/P is Lebesguian if H is Lebesguian, we invoke the fact (established in Section 3.2 of [13]) that (Ω/P, A/P, π/P) is a Lebesgue space provided (Ω, A, π) is a Lebesgue space and there exists a countable set S ⊆ A that separates two points if and only they are in diﬀerent partition classes.

To construct such a set S, let T be a countable set generating A, closed

under ﬁnite intersections. For A ∈ A and x ∈ Ω, let

µx(A) =

W(x, y)dπ(y).

A

Since W is a bounded A × A-measurable function, the function A  → µx(A) is a ﬁnite measure for all x ∈ Ω, while the function x  → µx(A) is a Ameasurable function on Ω for all A ∈ A.

By deﬁnition, x, x′ ∈ Ω are twins iﬀ the set {y ∈ Ω : W(x, y) = W(x, y′)} has measure zero. This is equivalent to the condition that µx(A) = µx′(A) for all A ∈ A. Since the measure µx(·) on A is uniquely determined by the sets in T , we have that x and x′ are twins if and only if µx(T) = µx′(T) for all T ∈ T .

For every T ∈ T and rational number r, consider the sets ST,r = {x ∈ Ω : µx(T) ≥ r}. There is a countable number of these. Furthermore, if

- x and x′ are twins, then they belong to exactly the same sets ST,r; if they are not twins, then there is a T ∈ T such that µx(T) = µx′(T), and for any rational number between µx(T) and µx′(T), the set ST,r separates x and x′.


This completes the proof of Theorem 3.2.

- 3.4 Isomorphism and Weak Isomorphism We conclude this section with relating isomorphism and weak isomorphism.


- Lemma 3.5 Let Hi = (Ωi, Ai, πi, Wi) be graphons with the Lebesgue property (i = 1, 2), and let φ : Ω1 → Ω2 be measure-preserving. If H1 is almost twinfree, and W1 = W2φ almost everywhere, then φ is an isomorphism mod 0, so in particular H1 ∼= H2. Proof. Let


Ω′1 = {x ∈ Ω1: W2(φ(x), φ(y)) = W1(x, y) for almost all y},

and let N1 = Ω1 \ Ω′1. Then π1(N1) = 0 by Fubini and our assumption that W1 = W2φ almost everywhere.

Let N1′ be a nullset such that all twin-classes of H1 have at most one point in Ω1 \ N1′, and let φ′ to be the restriction of φ to Ω′1 \ N1′. Then φ′ is injective: indeed, if x1, x2 ∈ Ω′1 \ N1′ and φ(x1) = φ(x2), then W1(x1, y) = W2(φ(x1), φ(y)) = W2(φ(x2), φ(y)) = W1(x2, y) for almost all

- y by the deﬁnition of Ω′1, hence x1 and x2 are twins, a contradiction. As shown in [13], Section 2.5, an injective measure preserving map between Lebesgue spaces has a measurable inverse deﬁned almost everywhere. This


implies that φ′ : Ω′1 \ N1′ → Ω2 is an isomorphism mod 0, which shows that φ is an isomorphism mod 0 as well.

- Corollary 3.6 If two twin-free graphons with the Lebesgue property are weakly isomorphic, then they are isomorphic.


## 4 Canonical Ensembles

We could try to construct a “canonical form” of a graphon by assigning “tags” to the points in Ω. For example, we could tag a point x with its marginal d(x) = W(x, y) dπ(y), or by the sequence of marginals of higher powers of W. This, however, would not work: for example, there could be a transitive group of measure-preserving permutations of Ω leaving W invariant, and then all points would still have the same tag.

To break the symmetry, we select an inﬁnite sequence α = (a1, a2, . . .) of points in Ω, which we call anchor points. Now we can tag each point x ∈ Ω with the sequence

Φα(x) = (W(x, a1), W(x, a2), . . .) ∈ [0, 1]N (9)

(where we assume that 0 ≤ W ≤ 1) The map x  → Φα(x) deﬁnes a measurable map from Ω into [0, 1]N (with respect to the standard Borel σ-algebra L on [0, 1]N), which in turn deﬁnes a measure λα on the sets S ∈ L by

λα(S) = π(Φ−α1(S)), (10)

on ([0, 1]N, L, λα) by (5). We denote the completion of ([0, 1]N, L, λα, WΦ

and a graphon WΦ

α

) by Hα.

α

We will show that if α1, α2, . . . are taken i.i.d. at random with distribution π then with probability one, then Hα is isomorphic mod 0 to the original graphon H (see Section 4.2 for details). So using an inﬁnite sequence of independent random points as anchor points, the tags of the points contain all information about the points.

These tags are almost canonical, except for the choice of the sequence α. So instead of a canonical form, we get a “canonical ensemble”, a probability distribution (Hα) of graphons such that H ∼= Hα for almost all α, and two graphons are isomorphic if and only if their ensembles can be coupled so that corresponding graphons are isomorphic.

To prove Theorem 2.1 (i), we will therefore have to show that if H and H′ satisfy (4), then we can “couple” the choice of anchor points α in H and β in H′ so that Hα ∼= Hβ′ , thus yielding an isomorphism of H and H′. This second step in the proof will be carried out in Section 5.3.

### 4.1 Measure theoretic preparation

The next technical lemma will be important in the construction of “canonical ensembles”.

- Lemma 4.1 Let (Ω, A, π) and (Ω′, A′, π′) be probability spaces, and let W : Ω × Ω′ → R be a bounded A × A′-measurable function. Let Y1, Y2, . . . be independent random points from Ω′. Let A0 ⊆ A be the (random) σ-algebra generated by the functions W(·, Yk). Then with probability 1, W is almost A0 × A′-measurable.


Proof. By Lemma 3.4, we may assume that A and A′ are countably generated. Let A′1 ⊂ A′2 ⊂ . . . and A′1 ⊂ A′2 ⊂ . . . be a sequence of ﬁnite σ-algebras with σ(∪nAn) = A and σ(∪nA′n) = A′, and let Pn′ denote the

partition of Ω′ into the atoms of A′n. For y ∈ S ∈ Pn′ with π′(S) > 0, deﬁne Un,m(x, y) =

1 mπ(S)

W(x, Yj)

![image 6](<2008-borgs-moments-two-variable-functions-uniqueness_images/imageFile6.png>)

j≤m Yj∈S

We deﬁne Un,m(x, y) = 0 if y ∈ S ∈ Pn′ with π′(S) = 0.

First we prove that for every n ≥ 1, every A ∈ A and A′ ∈ A′n, we have with probability 1

Un,m dπ dπ′ −→

W dπ dπ′ (m → ∞). (11)

A×A′

A×A′

It suﬃces to prove this in the case when A′ = S ∈ Pn′ and π′(S) > 0. Then for every y0 ∈ A′, we have

A

1 mπ(S)

Un,m(x, y0) dπ(x) =

![image 7](<2008-borgs-moments-two-variable-functions-uniqueness_images/imageFile7.png>)

j≤m Yj∈S A

W(x, Yj) dπ(x).

hence by the Law of Large Numbers,

A

1 π(S)

Un,m(x, y0) dπ(x) −→

![image 8](<2008-borgs-moments-two-variable-functions-uniqueness_images/imageFile8.png>)

A×S

W dπ dπ′ (m → ∞).

Since both sides are independent of y0 ∈ S, integrating over y0 ∈ S equation

(11) follows.

The number of choices of n, A ∈ ∪kAk and A′ ∈ A′n is countable, and hence it follows that with probability 1, (11) holds for all n ≥ 1, every A ∈ ∪kAk and A′ ∈ A′n. Since ∪kAk is dense in A, this implies that (11) holds for all n ≥ 1, every A ∈ A and A′ ∈ A′n.

From now on, we suppose that the choice of the Yi is such that this holds. For a ﬁxed n, the indices m have a subsequence m1 < m2 < . . . such that

converges to some function Un in the weak-∗-topology of L∞(A0×A′n). Hence by (11),

Un,m

j

A×A′

Un dπ dπ′ = lim

j→∞

A×A′

Un,m

j

dπ dπ′ =

W dπ dπ′

A×A′

for all n ≥ 1, every A ∈ A and A′ ∈ A′n. Thus Un is a representative of E(W | A × A′n). Since Un is A0 × A′n measurable, it is also a representative of E(W | A0 × A′n). This shows that for every n ≥ 1 we have

E(W | A × A′n) = E(W | A0 × A′n) (12) almost everywhere.

By Levy’s Upward Theorem, the left hand side of (12) tends to E(W | A×A′) = W almost everywhere. The right hand side of (12) tends to E(W | A0 × A′) almost everywhere, so W = E(W | A0 × A′) almost everywhere, which proves the Lemma.

We formulate a couple of corollaries, the ﬁrst of which is immediate:

- Corollary 4.2 Let (Ω, A, π) and (Ω′, A′, π′) be probability spaces, let W : Ω × Ω′ → R be a bounded function that is measurable with respect to A × A′, and let A0 ⊂ A be a sub-σ-algebra. If W(·, y) is A0-measurable for almost all x ∈ Ω, then W is almost A0 × A′-measurable.


Corollary 4.3 Let (Ω, A, π, W) be a graphon, and let X1, X2, . . . be independent random points from Ω. Let A0 ⊆ A be the (random) σ-algebra generated by the functions W(·, Xk). Then with probability 1, W is almost A0 × A0-measurable.

Proof. Let A1 denote the σ-algebras generated by the functions W(·, X2k). Clearly A1 ⊆ A0. By Lemma 4.1, W is almost A1 × A measurable with probability 1, so we can change it on a set of measure 0 to get an A1 × A measurable function W′. Let A′2 be the σ-algebras generated by the functions W′(X2k+1, ·). Applying the lemma again, we get that W′ is almost A1 ×

- A′2 measurable. With probability 1, each function W(X2k+1, ·) diﬀers from W′(X2k+1, ·) on a set of measure 0 only (since the X2k+1 are independent of A1), and so A′2 ⊆ σ(A0). So W′ is A0 × σ(A0) measurable, which implies that W′, and hence W, are almost A0 × A0 measurable.


### 4.2 Anchor Sequences

Let us consider the σ-algebra L on [0, 1]N generated by the sets A1×A2×. . . , where each Ai is a Borel subset of [0, 1] and only a ﬁnite number of factors Ai are diﬀerent from [0, 1]. Fix a graphon H = (Ω, A, π, W) with 0 ≤

- W ≤ 1. For every α ∈ ΩN, the map Φα : Ω → [0, 1]N deﬁned by (9) is measurable, and (10) deﬁnes a probability measure on L with respect to which Φα is measure preserving. Thus (6) leads to a symmetric, L × L-


: [0, 1]N × [0, 1]N → [0, 1] which we denote by Wα. We say that α ∈ ΩN is regular if W = WΦ

measurable function WΦ

α

α almost everywhere.

α

- Lemma 4.4 Almost all α ∈ ΩN are regular.

Proof. Let Aα denote the σ-algebra of subsets of Ω of the form Φ−α1(A), where A ∈ L. Note that Aα ⊆ A by the fact that Φα is measurable. Further, almost by deﬁnition, Aα is the smallest sub-σ-algebra of A such that all the functions W(·, αi) are measurable. As a consequence, we may apply Lemma 4.3 to conclude that for almost all α, W is almost Aα × Aα)-measurable, which by Lemma 3.1 gives that W = WΦ

α

α almost everywhere.

Let Lα be the completion of L with respect to λα. Then ([0, 1]N, Lα, λα) is a complete, Polish space and hence Lebesgue, so Hα = ([0, 1]N, Lα, λα, Wα) deﬁnes a Lebesguian graphon.

- Lemma 4.5 Let H be a twin free graphon with the Lebesgue property. If α is regular, then Φα is an isomorphism mod 0 and Hα ∼= H.


Proof. By (10), Φα is a measure preserving map from (Ω, A, π) into ([0, 1]N, L, λα). Since (Ω, A, π) is complete, Φα is measurable (and measure preserving) from (Ω, A, π) into ([0, 1]N, Lα, λα) as well. By the deﬁnition of a regular α, Hφ

α = H almost everywhere, and by Lemma 3.5, Φα is an isomorphism mod 0.

α

## 5 Coupling

### 5.1 Partially Labeled Graphs and Marginals

We recall some notions from [8]. A partially labeled graph is a ﬁnite graph in which some of the nodes are labeled by diﬀerent nonnegative integers. Two partially labeled graphs are isomorphic, if there is a label-preserving isomorphism between them. A k-labeled graph is a partially labeled graph with labels 1, . . ., k.

Let F1 and F2 be two partially labeled graphs. Their product F1F2 is deﬁned as follows: we take their disjoint union, and then identify nodes with the same label (retaining the labels, and any multiple edges which this might create). For two unlabeled graphs, F1F2 is their disjoint union. Clearly this multiplication is associative and commutative.

Let H = (Ω, A, π, W) be a graphon, and let α = (a0, a1, . . .) be an inﬁnite sequence of points in Ω. Let F be a partially labeled graph with nodes V (F) = {1, . . ., k}, where nodes 1, . . ., r are labeled by distinct nonnegative integers ℓ1, . . ., ℓr. Let Xi = aℓ

for 1 ≤ i ≤ r, and let Xr+1, . . ., Xk ∈ Ω be independent points from the distribution π. Deﬁne

i

tα(F, H) = E

W(Xj, Xj) .

ij∈E(F)

Of course, this value only depends on those elements of α whose subscripts occur as labels, and we’ll sometimes omit the tail of α if it contains no labels. For example, if F is a 2-labeled triangle, then

ta

1a2(F, H) = tα(F, W) = E(W(a1, a2)W(a2, X)W(a1, X))

=

W(a1, a2)W(a2, x)W(a1, x) dπ(x).

Ω

It is easy to see that if F1 and F2 are two k-labeled graphs, then t(F1F2, H) =

tx

1...xk(F1, W)tx

1...xk(F2, W) dπ(x1) . . .dπ(xk).

Ωk

### 5.2 Multiple Edges

- Lemma 5.1 Let H = (Ω, A, π, W) and H′ = (Ω′, A′, π′, W′) be two graphons, and assume that t(F, H) = t(F, H′) for every simple graph F. Then t(F, H) = t(F, H′) for every multigraph F.


Proof. We use induction on the number of parallel edges in F. Suppose that F has two nodes, say i and j, connected by more than one edge. Let Fk denote the multigraph obtained from F by subdividing one of these edges by k − 1 new nodes. Let F′ denote the multigraph obtained by removing one copy of the edge ij. So F1 = F, but for k > 1, Fk has fewer parallel edges than F, and so we may assume that

t(Fk, H) = t(Fk, H′)

holds for every k ≥ 2. We consider all the multigraphs Fk and F′ as 2-labeled graphs, with i and j labeled 1 and 2.

Since Fk can be thought of as the product of F′ and a path Pk+1 with k + 1 nodes (the endpoints labeled), we can write

t(F, H) =

W(x, y)txy(F′, H) dπ(x) dπ(y),

Ω2

and

t(Fk, H) =

txy(Pk+1, H)txy(F′, H) dπ(x) dπ(y).

Ω2

The ﬁrst factor inside the integral can be expressed as

txy(Pk+1, H) =

W(x, x1) · · ·W(xk−1y) dπ(x1) . . .dπ(xk−1),

Ωk

which we can recognize as k-th power of the kernel W as an integral operator.

At this point, it will be useful to assume that H and H′ are countably generated graphons (this can be done without loss of generality by Lemma 3.4). As a consequence, W is an integral operator on the separable Hilbert space

L2(Ω, A, π), and since W is bounded, this implies that W is Hilbert-Schmidt and thus compact, which in turn implies that W has a spectral representation:

∞

λnϕn(x)ϕn(y). (13) It follows that for every k ≥ 2,

W(x, y) ∼

n=0

txy(Pk+1, H) =

∞

λknϕn(x)ϕn(y),

n=0

and hence

∞

λkn

t(Fk, H) =

n=0

Ω2

ϕn(x)ϕn(y)txy(F′, H) dπ(x) dπ(y).

Similarly, let

∞

W′(x, y) ∼

µnψn(x)ψn(y)

i=0

be the spectral representation of W′, then we get that for every k ≥ 2,

0 = t(Fk, H) − t(Fk, H′) =

∞

anλkn − bnµkn, (14)

n=0

where

an =

ϕn(x)ϕn(y)txy(F′, U) dπ(x) dπ(y)

and

Ω2

bn =

ψn(x)ψn(y)txy(F′, W) dπ(x) dπ(y)

(Ω′)2

are independent of k. (The integrals exist since tx,y(F′, H) is a bounded function of x and y.) It follows that in (14) everything must cancel, in other words, for every value c,

{an : λn = c} = {bn : µn = c}

(it is known that the sums on both sides have a ﬁnite number of terms, since the multiplicities of the eigenvalues are ﬁnite).

Now while (13) may not be true with equality, the “trace” with any other kernel gives an equation; in particular,

∞

t(F, H) =

λn

n=0

Ω2

W(x, y)txy(F′, H) dπ(x) dπ(y) =

∞

anλn,

n=0

and similarly

∞

t(F, H′) =

bnµn, which shows that t(F, H) = t(F, H′) as claimed.

n=0

It will be convenient to assume that 0 ≤ W, W′ ≤ 1. If this does not hold, we can apply a linear transformation to the values of the functions, to get two functions W0 and W0′ with 0 ≤ W0, W0′ ≤ 1. Expanding the product in the deﬁnition (3), t(F, W0) can be written as a linear combination of the values t(F′, W), where F′ is a subgraph of F. Thus t(F, W) = t(F, W′) for every graph F if and only if t(F, W0) = t(F, W0′) for every graph F (where “graph” could mean either simple graph or multigraph). So (4) holds for W0 and W0′ if and only if it holds for W and W′. If we prove that this implies (Ω, A, π, W0) ∼= (Ω′, A′, π′, W0′), then H ∼= H′ follows trivially.

### 5.3 Coupling Anchor Sequences

Consider two graphons H = (Ω, A, π, W) and H′ = (Ω′, A′, π′, W′) satisfying the conditions in Theorem 2.1 (i) and 0 ≤ W, W′ ≤ 1. Given two “anchor” sequences α = (a1, a2, . . .) from Ω and β = (b1, b2, . . .) from Ω′, let Hα = ([0, 1]N, Lα, λα, Wα) and Hβ′ = ([0, 1]N, L′β, λ′β, Wβ′). We would like to select α and β in such a way that λα = λ′β and Wα = Wβ′ almost everywhere. This will complete the proof of the theorem. By Lemma 4.4, we can guarantee that both α and β are regular by selecting a1, a2, . . . as well as b1, b2 . . . independently and uniformly from π and π′, respectively; however, the equality of Wα and Wβ′ will only be true if we couple α and β carefully.

The condition on the coupling is described in the following lemma.

- Lemma 5.2 Let H = (Ω, A, π, W) and H′ = (Ω′, A′, π′, W′) be two


graphons, and let α = (a1, a2, . . .) and β = (b1, b2, . . .) be regular sequences for H and H′, respectively. Suppose that for every partially labeled multigraph F,

tα(F, H) = tβ(F, H′). Then λα = λ′β and Wα = Wβ′ almost everywhere (with respect to λα = λ′β).

Proof. First, we show that λα = λ′β. These probability measures are deﬁned on the σ-algebra L as the distribution measures of the random vari-

ables W(X, a1), W(X, a2), . . .) and W′(Y, b1), W′(Y, b2), . . .), where X and

- Y are random points from π and π′, respectively. By Lemma 6.1 it therefore suﬃces to prove that these random variables have the same mixed moments.

Let (k1, k2, . . .) be a sequence of nonnegative integers, of which only a ﬁnite number is nonzero; say ki = 0 for i > m. Then

E(

i

W(X, ai)k

i

) = tα(F, H),

where F is the star on m + 1 nodes, with the endnodes labeled 1, . . ., m, and the edge between the center and endnode i replaced by ki parallel edges. Similarly,

E(

i

W′(Y, bi)k

i

) = tβ(F, H′).

These numbers are equal by the hypothesis of the Lemma. This proves that λα = λ′β.

Second, we show that Wα(x, y) = Wβ′(x, y) for almost all x, y ∈ [0, 1]N. It suﬃces to show that the random variables Z1 = (X, Y, Wα(X, Y )) and

- Z2 = (X, Y, Wβ′(X, Y )) (with values from [0, 1]N × [0, 1]N × [0, 1]) have the same distribution, where X and Y are independent points in (ΩN, λα).


We can generate Z1 by choosing independent uniform random points X′

- and Y ′ from Ω, and letting X = Φα(X′) and Y = Φβ(Y ′). Since α is regular,


we have that

Wα(X, Y ) = W(X′, Y ′) with probability one, and hence

- Z1 = (W(X′, a1), W(X′, a2), . . ., W(Y ′, a1), W(Y ′, a2), . . ., W(X′, Y ′)).

Similarly, we have

- Z2 = (W′(X′′, b1), W′(X′′, b2), . . ., W′(Y ′′, b1), W′(Y ′′, b2), . . ., W′(X′′, Y ′′)),


where X′′ and Y ′′ are independent random points from π′. To prove that Z1

- and Z2 have the same distribution, it again suﬃces to prove that they have the same mixed moments.


A particular mixed moment is given by nonnegative integers (k1, k2, . . .), (l1, l2, . . .) and m (of which only a ﬁnite number is nonzero; say ki = li = 0 for i > n). Let us deﬁne the multigraph F as follows. F has two unlabeled nodes vx and vy, and n further nodes labeled 1, . . ., n. We connect vx to i by ki edges, vy to i by li edges (i = 1, . . ., n), and vx to vy by m edges. Then

E W(X′, a1)k

· · ·W(X′, an)k

W(Y ′, a1)k

· · ·W(Y ′, an)k

W(X′, Y ′) = tα(F, H). and similarly

1

1

n

n

E W′(X′′, b1)k

1

· · ·W′(X′′, bn)k

n

W′(Y ′′, b1)k

1

· · ·W′(Y ′′, bn)k

n

W′(X, Y ) = tβ(F, H′).

These two numbers are the same by hypothesis. This completes the proof of the Lemma.

To prove Theorem 2.1, we next show:

- Lemma 5.3 Let H = (Ω, A, π, W) and H′ = (Ω′, A′, π′, W′) be two Lebesguian graphons such that


t(F, H) = t(F, H′).

for every multigraph F. Then we can couple sequences α ∈ ΩN with sequences β ∈ Ω′N so that if α, β) is a sequence from this joint distribution, then

tα(F, H) = tβ(F, H′). holds almost surely for every partially labeled multigraph F.

Proof. Let Fk be the set of k-labeled multigraphs. We deﬁne recursively a coupling of sequences α ∈ Ωk with sequences β ∈ Ω′k so that tα′(F, H) = tβ′(F, H′) holds almost surely for every F ∈ Fk. Let (a1, . . ., ak) and (b1, . . ., bk) be chosen from this coupled distribution. Consider two random points X from π and Y from π′, and the random variables

1...akX(F, H) : F ∈ Fk+1) and

A = (ta

B = (tb

1...bkY (F, H) : F ∈ Fk+1)

with values in [0, 1]Fk+1. We claim that the variables A and B have the same distribution. It suﬃces to show that A and B have the same mixed moments. Consider any moment of A; in other words, let F1, . . ., Fm ∈ Fk+1, let q1, . . ., qm be nonnegative integers, and let Fq

i be obtained from Fi by replacing each edge in Fi by qi edges. Then the corresponding moment of A is

i

E

m

i=1

1...akX(Fi, H)q

ta

i

1...akX(Fq

1 . . .Fq

1

= E ta

m , H) = ta

1...ak(F, H),

m

where the multigraph F is obtained by unlabeling the node labeled k + 1 in the multigraph Fq

1 . . .Fq

1

m . Expressing the moments of B in a similar way, we see that they are equal by the induction hypothesis. This proves that A and B have the same distribution.

m

Using Lemma 6.2 it follows that we can couple the variables X and Y so that A = B with probability 1. In other words, we can replace X and Y by

a random variable (X′, Y ′) ∈ Ω × Ω′ so that X′ has distribution π, Y ′ has distribution π′, and their joint distribution satisﬁes

1...bkY′(F, H′)

1...akX′(F, H) = tb

ta

for every F ∈ Fk+1 with probability 1. Thus we have extended the coupling to Ωk × Ω′k.

It is clear that this sequence of couplings deﬁnes a coupling of ΩN with Ω′N as claimed.

### 5.4 Conclusion of proofs

Proof of Theorem 2.1. Part (i) follows easily: if we choose random sequences (α, β) from the coupled distribution given by Lemma 5.3, then these sequences will be regular with probability 1, and so they satisfy the conditions of Lemma 5.2.

To prove (ii), suppose that H = (Ω, A, π, W) and H′ = (Ω′, A′, π′, W′) satisfy (4) for every simple graph F. By Corollary 3.3, we can ﬁnd twinfree Lebesguian graphons G = (Γ, B, ρ, U) and G′ = (Γ′, B′, ρ′, U′) and weak isomorphisms φ and φ′ from H and H′ to G and G′, respectively. It follows by Theorem 2.1(i) that the G and G′ are isomorphic mod 0, so in particular U = (U′)ψ′ almost everywhere for some measure preserving map ψ′ : Γ → Γ′. Deﬁning ψ : Ω → Γ′ by ψ(x) = ψ′(φ(x)), we conclude that W = (U′)ψ almost everywhere. The maps ψ and φ′ are measure preserving from the completions H and H′ into G′.

![image 9](<2008-borgs-moments-two-variable-functions-uniqueness_images/imageFile9.png>)

![image 10](<2008-borgs-moments-two-variable-functions-uniqueness_images/imageFile10.png>)

Proof of Corollary 2.2. The equivalence of (a), (b) and (c) follows by Theorem 2.1 (ii) and the fact that a function which is measurable with respect to the completion of L × L is almost everywhere equal to a function which is measurable with respect to L × L. In the proof of (c), Theorem 2.1 may give a graphon containing atoms, but it is easy to replace these atoms by intervals of appropriate length.

To prove that (c)=⇒(e), assume that ϕ, ψ and U exist as in (c). Let

- X, X′ ∈ [0, 1] be independent random points from the uniform distribution


λ on [0, 1]. Since ϕ and ψ are measure preserving, ϕ(X) and ψ(Y ) have the same distribution, and hence by Lemma 6.2 there is a coupling measure γ on [0, 1] × [0, 1] with marginals λ such that if (X, X′) is a random sample from γ, then ϕ(X) = ψ(X′) with probability 1. So if (X, X′) and (Y, Y ′) are independent random points from γ, then

W(X, Y ) = U(phi(X), phi(Y )) = U′(psi(X′), psi(Y ′)) = W′(X′, Y ′).

To prove that (e)=⇒(d), consider the projections Φ, Ψ : [0, 1]2 → [0, 1] deﬁned by Φ(x, x′) = x and Ψ(x, x′) = x′. Then

WΦ((X, X′), (Y, Y ′)) = W(X, Y )

and

(W′)Ψ((X, X′), (Y, Y ′)) = W′(X′, Y ′)

Thus, WΦ = (W′)Ψ almost everywhere. Furthermore, Φ and Ψ are measure preserving if we consider the coupling measure γ on [0, 1].

Since the completion of ([0, 1]2, L2, γ) is a Lebesgue space, we can ﬁnd a measure preserving map ρ : ([0, 1], λ) → ([0, 1]2, γ). Setting ϕ = Φ ◦ ρ and ψ = Ψ◦ρ, we obtain the desired measure preserving maps ϕ, ψ : [0, 1] → [0, 1] such that Wϕ = (W′)ψ almost everywhere.

Finally, (d)⇒(a) is trivial.

## Acknowledgement

We are grateful to Mikl´os Laczkovich, Ron Peled, Yuval Peres and Oded Schramm for many useful discussions on the topic of this paper, and to Kati Vesztergombi and Svante Janson for carefully reading an earlier version and suggesting several improvements.

## References

- [1] N. Alon, W. Fernandez de la Vega, R. Kannan and M. Karpinski: Random sampling and approximation of MAX-CSPs, J. Comput. System Sci. 67 (2003), 212–243.
- [2] C. Borgs, J. Chayes, L. Lova´sz, V.T. S´os, K. Vesztergombi, unpublished, 2004.
- [3] C. Borgs, J. Chayes, L. Lova´sz, V.T. S´os, K. Vesztergombi: Counting graph homomorphisms, in: Topic in Discrete Mathematics (Klazar, Kratochvil, Loebl, Matousek, Thomas, Valtr, eds.) Springer, Berlin– Heidelberg (2006), 315–371.
- [4] C. Borgs, J. Chayes, L. Lova´sz, V.T. S´os, K. Vesztergombi: Convergent Sequences of Dense Graphs I: Subgraph Frequencies, Metric Properties and Testing, preprint (2006), http://research.microsoft.com/~borgs/Papers/ConvMetric.pdf
- [5] C. Borgs, J.T. Chayes, L. Lova´sz, V.T. S´os, and K. Vesztergombi: Convergent Graph Sequences II. H-Colorings, Statistical Physics and Quotients, manuscript (2006)
- [6] P. Erd¨os, L. Lova´sz, J. Spencer: Strong independence of graphcopy functions, in: Graph Theory and Related Topics, Academic Press, 165172.
- [7] Feller, W.: An Introduction to Probability Theory and its Applications, Vol. II, Second edition, Wiley, NewYork, (1971).
- [8] M. Freedman, L. Lova´sz, A. Schrijver: Reﬂection positivity, rank connectivity, and homomorphism of graphs Journal of The American Mathematical Society (to appear)
- [9] O. Goldreich, S. Goldwasser and D. Ron: Property testing and its connection to learning and approximation, J. ACM 45 (1998), 653–750.


- [10] P.R. Halmos: Measure Theory, Graduate Texts in Mathematics 18, Springer, New York, Heidelberg, Berlin (1991).
- [11] L. Lova´sz and B. Szegedy: Limits of dense graph sequences, Microsoft Research Technical Report TR-2004-79.
- [12] L. Lova´sz, B. Szegedy: Szemer´edi’s Lemma for the analyst, Microsoft Research Technical Report MSR-TR-2005-90, ftp://ftp.research.microsoft.com/pub/tr/TR-2005-90.pdf
- [13] V. A. Rohlin: On the fundamental ideas of measure theory, Translations of the American Mathematical Society, Series 1, Vol. 10, 1-54 (1962). The Russian original appeared in Mat. Sb. 25, 107-150 (1949).
- [14] D. Williams: Probability with Martingales, Cambridge University Press,


(1991).

## 6 Appendix: Moments and coupling of probability distributions

In this section we prove some probability theory lemmas, that are “well known” but not easy to reference. We start with the fact that if two vector valued random variables have the same mixed moments, then they have the same distribution (cf Feller [7], Problem XV.9.21.).

- Lemma 6.1 Let (Ω, A, π) and (Ω′, A′, π′) be probability spaces, and let


- f : Ω → [0, 1]N and g : Ω′ → [0, 1]N be measurable functions, with f(x) = (f1(x), f2(x), . . .) and g(y) = (g1(y), g2(y), . . .). If


f1(x)k

1

. . .fn(x)k

n

dπ(x) = g1(y)k

1

. . .gn(y)k

n

dπ′(y)

for every ﬁnite sequence of nonnegative integers k1, . . ., kn, then π(f−1(B)) = π′(g−1(B)) for every Borel set B ⊆ [0, 1]N.

Proof. It suﬃces to prove that π(f−1(B)) = π′(g−1(B)) for every Borel set of the form B = I1 × I2 × . . .In × [0, 1] × . . ., where I1, . . ., In are intervals. Let pj,m(x) be a polynomial that approximates the indicator function 1I

on [0, 1] in L1 with error less than 1/m (j = 1, . . ., n). Then

j

p1,m(f1(x)) · · ·pn,m(fn(x)) dx −→

Ω

Ω

=

f−1(B)

Similarly,

(f1(x)) · · ·1I

1I

1

n

(fn(x)) dx

1 dx = π(f−1(B)) (m → ∞).

p1,m(g1(x)) · · ·pn,m(gn(x)) dx −→ π(g−1(B)) (m → ∞).

Ω

But the left hand sides of these two relations are equal for all m, which proves the Lemma.

We need the following natural fact about coupling.

Lemma 6.2 Assume that (Ω, A, π) and (Ω′, A, π′) are Lebesgue spaces, and (Γ, B, ρ), a countably generated separating space. Let f : Ω → Γ and

- g : Ω′ → Γ be measure preserving maps. Then there exists a coupling ν of (Ω, A, π) and (Ω′, A, π′) such that


ν (x, y) : f(x) = g(y) = 1.

Proof. For A ∈ A, consider the measure λA(B) = π(A ∩ f−1(B)) deﬁned for B ∈ B, and its Radon-Nikodym derivative fA = dλA/dρ. Since λA ≤ π(f−1(B)) = ρ(B), this derivative exists, and 0 ≤ fA ≤ 1 almost everywhere. Furthermore, f∅ = 0 and fΩ = 1 almost everywhere.

Similarly, for C ∈ A′, deﬁne µC(B) = π′(C ∩ g−1(B)) and gC = dµC/dρ. Finally, let

ν(A × C) = fAgC dρ. (15)

Clearly

ν(A × C) ≤ fA dρ = π(A),

and similarly ν(A × C) ≤ π′(C). Hence in particular ν(A × C) = 0 if either π(A) = 0 or π′(C) = 0.

- Claim 2 If Ai ∈ A, Ci ∈ A′ (i ∈ I) and the sets Ai × Ci form a (ﬁnite or


countably inﬁnite) partition of A×C (A ∈ A, C ∈ A′), then i ν(Ai×Ci) = ν(A × C).

It is easy to see that if A1, A2 ∈ A are disjoint sets and A = Ai ∪A2, then fA

= fA almost everywhere. It follows that for every C ∈ A′, we have ν(A1 × C) + ν(A2 × C) = ν(A × C). This implies by standard arguments that the claim holds if |I| is ﬁnite. This in turn implies that ν extends to a ﬁnitely additive measure on the algebra F of sets that can be written as the union of a ﬁnite number of product sets A × C (A ∈ A, C ∈ A′).

+fA

1

2

In the case of inﬁnite |I|, it follows that i ν(Ai × Ci) ≤ ν(A × C); in fact, for every ﬁnite J ⊆ I, we have ∪i∈JAi × Ci ⊆ A × C, and hence by the ﬁnite additivity of ν, we have

ν(Ai × Ci) = ν ∪i∈JAi × Ci ≤ ν(A × C).

i∈J

Since this holds for every ﬁnite subset J of I, it also holds for I.

Suppose that there is a partition where {Ai × Ci : i = 1 ∈ N} of A × C and an ε > 0 for which

i

ν(Ai × Ci) < ν(A × C) − 4ε

on a set B of positive measure. Now we use that (Ω, A, π) and (Ω′, A, π′) are Lebesgue spaces, so we may assume that they are intervals [0, a] and [0, b] respectively, together with a countable set of atoms. Thinking of the atoms as converging to a from above, we have a compact topology on them. For every i, we can ﬁnd an open sets Ui ⊇ Ai and Vi ⊇ Ci such that π(Ui) ≤ π(Ai)+ε2−i

and π′(Vi) ≤ π′(Ci) + ε/2i. Also, we can ﬁnd closed sets U ⊆ A and V ⊆ C such that π(U) ≥ π(A) − ε and π′(V ) ≥ π′(C) − ε. Then

ν(Ui × Vi) ≤ ν(Ai × Ci) + ν((Ui \ Ai) × Ci) + ν(Ui × (Vi \ Ci))

≤ ν(Ai × Ci) + π(Ui \ Ai) + π′(Vi \ Ci) ≤ ν(Ai × Ci) + 2ε2−i. It follows similarly that

ν(U × V ) ≥ ν(A × C) − 2ε.

Hence

i

ν(Ui × Vi) ≤

i

ν(Ai × Ci) + 2ε < ν(A × C) − 2ε ≤ ν(U × V ).

The open sets Ui × Vi cover the compact set U × V , and so a ﬁnite number of them also covers. But the contradicts the ﬁnite additivity of ν which we already established.

- Claim 3 The setfunction ν extends to a measure on A × A′.


We have seen already that ν extends to F; it follows by Claim 2 that this extension is σ-additive. Thus the Claim follows by the Measure Extension Theorem.

Deﬁne ∆ = {(x, y) ∈ Ω × Ω′ : f(x) = g(y)}. To complete the proof of the Lemma, we want to prove that ν is a coupling between (Ω, A, π) and (Ω′, A, π′) (which is trivial), and that ν(Ω × Ω′ \ ∆) = 0. Let S ⊆ B be a countable family separating the elements of Γ. Then

Ω × Ω′ \ ∆ =

f−1(S) × g−1(Γ \ S) ∪

S∈S

f−1(Γ \ S) × g−1(S).

S∈S

Consider any term here, say f−1(S) × g−1(Γ \ S) = A × C. Then

ν(A × C) = fAgC dρ =

+

S

.

Γ\S

Here

fAgC dρ ≤

S

gC dρ = µC(S) = π′(g−1(Γ \ S) ∩ g−1(S)) = 0,

S

and similarly

fAgC dρ = 0. This proves that ν(Ω × Ω′ \ ∆) = 0.

Ω\S

