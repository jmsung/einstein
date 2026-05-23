arXiv:1506.04558v2[math.GT]17Sep2016

On Expansion and Topological Overlap∗

Dominic Dotterrer1, Tali Kaufman2, and Uli Wagner3

- 1 University of Chicago Department of Mathematics 5734 S. University Avenue, Chicago, Illinois 60637, USA., d.dotterrer@math.uchicago.edu
- 2 Bar-Ilan University, Department of Computer Science, 5290002 Ramat Gan, Israel., kaufmant@macs.biu.ac.il
- 3 IST Austria, Am Campus 1, 3400 Klosterneuburg, Austria., uli@ist.ac.at


October 15, 2018

Abstract

We give a detailed and easily accessible proof of Gromov’s Topological Overlap Theorem. Let X be a ﬁnite simplicial complex or, more generally, a ﬁnite polyhedral cell complex of dimension d. Informally, the theorem states that if X has suﬃciently strong higher-dimensional expansion properties (which generalize edge expansion of graphs and are deﬁned in terms of cellular cochains of X) then X has the following topological overlap property: for every continuous map X → d there exists a point p ∈ d that is contained in the images of a positive fraction µ > 0 of the d-cells of X. More generally, the conclusion holds if d is replaced by any d-dimensional piecewise-linear (PL) manifold M, with a constant µ that depends only on d and on the expansion properties of X, but not on M.

# 1 Introduction

Let X be a ﬁnite polyhedral cell complex1 of dimension dimX = d. Gromov [8] recently showed that if X has suﬃciently strong higher-dimensional expansion properties (which generalize edge expansion of graphs, see below for the precise deﬁnition) then X has the following topological overlap property: For every every continuous map f : X → d, there exists a point p ∈ d that is contained in the images of some positive fraction of the d-cells of X, i.e.,

|{σ ∈ Σd(X): p ∈ f(σ)}| ≥ µ · |Σd(X)|, (1)

![image 1](<2015-dotterrer-expansion-topological-overlap_images/imageFile1.png>)

∗Research supported by the Swiss National Science Foundation (Project SNSF-PP00P2-138948). An extended abstract of this paper [5] appeared in the Proceedings of the 32nd International Symposium on Computational Geometry (SoCG 2016).

1See [3, Sec. 12] or [16, Ch. I] for more background on polyhedral cell complexes (in [16], they are called convex linear cell complexes).

where Σk(X) denotes the set of k-dimensional cells of X, 0 ≤ k ≤ d, and µ > 0. More generally, the same conclusion holds if the target space d is replaced by a ddimensional manifold M, and the overlap constant µ > 0 depends only on the dimension d and on the constants quantifying the expansion properties of X, but not on M. For technical reasons, we will assume that the manifold M admits a piecewise-linear (PL) triangulation, so that we can apply standard tools to perturb a given map to general position. We refer to the book by Rourke and Sanderson [15] or to the lecture notes by Zeeman [16] for background and standard facts about piecewise-linear topology.

In the special case where X is the n-dimensional simplex ∆n (or its d-dimensional skeleton), determining the optimal overlap constant for maps ∆n → d is a classical problem in discrete geometry, also known as the point selection problem [2, 1] and originally only considered for aﬃne maps. Apart from the generalization from aﬃne to arbitrary continuous maps, Gromov’s proof also led to improved estimates for the point selection problem, and a number of papers have appeared with expositions and simpliﬁed proofs of Gromov’s result in this special case X = ∆n, see [9, 13] and [4, Sec. 7.8].

The goal of the present paper is to provide a detailed and easily accessible proof of Gromov’s result for general complexes X, see Theorem 8 below. This is a crucial ingredient for obtaining examples of simplicial complexes X of bounded degree (i.e., such that every vertex is incident to a bounded number of simplices) that have the topological overlap property [7, 6]. The basic idea of the proof is the same as Gromov’s, but we present a simpliﬁed and streamlined version of the proof that uses only elementary topological notions (general position for piecewise-linear maps, algebraic intersection numbers, cellular chains and cochains, and chain homotopies) and avoids much of the machinery used in Gromov’s original paper (in particular, the simplicial set of cocycles).

For stating the result formally, we need to discuss higher-dimensional expansion properties of cell complexes. The relevant notion of expansion originated in the work of Linial and Meshulam [10] and of Gromov [8] and generalizes edge expansion of graphs (which corresponds to 1-dimensional expansion). To deﬁne k-dimensional expansion, we need two ingredients: ﬁrst, information about incidences between cells of dimensions k and k−1 and, second, a notion of discrete volumes in X. To deﬁne these, it is convenient to use the language of cellular cochains of X.

Cellular Cochains

Let X be a polyhedral cell complex, let Σk(X) denote the set of k-dimensional cells of X, and let Ck(X) := Ck(X; 2) := 2Σk(X) be the space of k-dimensional cellular cochains with coeﬃcients in the ﬁeld 2; in other words Ck(X) is the space of functions a: Σk(X) → 2 = {0,1}. For a pair (σ,τ) ∈ Σk(X) × Σk−1(X), let [σ: τ] be 1 or 0 depending on whether τ is incident to σ (i.e., whether τ is contained in the boundary ∂σ) or not. This incidence information is recorded in the coboundary operator, which is a linear map δ: Ck−1(X) → Ck(X) given by δa(σ) := τ∈Σ

k−1(X)[σ: τ]a(τ).

The elements of the subspaces Zk(X) := ker(δ: Ck(X) → Ck+1(X)) and Bk(X) := im(δ: Ck−1(X) → Ck(X)) are called k-dimensional cocycles and coboundaries, respec-

tively. The composition of consecutive coboundary operators is zero, i.e., Bk(X) ⊆ Zk(X), and Hk(X) = Zk(X)/Bk(X) is the k-dimensional homology group (with 2coeﬃcients) of X. This information is customarily recorded in the cellular cochain complex2 of X:

- 0 2 = C−1(X) δ C0(X) δ C1(X) δ ··· δ Cd−1(X) δ Cd(X) 0

![image 2](<2015-dotterrer-expansion-topological-overlap_images/imageFile2.png>)

![image 3](<2015-dotterrer-expansion-topological-overlap_images/imageFile3.png>)

![image 4](<2015-dotterrer-expansion-topological-overlap_images/imageFile4.png>)

![image 5](<2015-dotterrer-expansion-topological-overlap_images/imageFile5.png>)

![image 6](<2015-dotterrer-expansion-topological-overlap_images/imageFile6.png>)

![image 7](<2015-dotterrer-expansion-topological-overlap_images/imageFile7.png>)

![image 8](<2015-dotterrer-expansion-topological-overlap_images/imageFile8.png>)

(2)

Norm, coﬁlling, expansion and systoles

For α ∈ Ck(X), let |α| denote the Hamming norm of α, i.e., the cardinality of the support supp(α) := {σ ∈ Σk(X): α(σ) = 0}, which we think of as a measure of “discrete k-dimensional volume.” In fact, it will be convenient to allow more general norms on cochains; the following deﬁnition summarizes the properties that we will need.

- Deﬁnition 1 (Norm on cochains). A norm on the group C∗(X) = dk=0 Ck(X) of cellular cochains of X with 2-coeﬃcients is a function · : C∗(X; 2) → ≥0 that satisﬁes the following properties for all cochains α,β ∈ Ck(X), 0 ≤ k ≤ d:

- 1. 0 = 0.
- 2. Triangle inequality: α + β ≤ α + β .

Furthermore, we will assume throughout that the norm satisﬁes the following:

- 3. Monotonicty: α ≤ β whenever supp(α) ⊆ supp(β).


From now on, we work with a ﬁxed norm on the cochains of X. We assume that

the norm is normalized such that kX = 1 for 0 ≤ k ≤ d, where kX ∈ Ck(X) assigns 1 to every k-cell of X. In particular, when working with the Hamming norm, we will

consider its normalized version

α H :=

|α| |Σk(X)|

![image 9](<2015-dotterrer-expansion-topological-overlap_images/imageFile9.png>)

.

Given β ∈ Bk(X), we say that α ∈ Ck−1(X) coﬁlls b if β = δα. Once we have a notion of discrete volumes, we can consider the following (co)isoperimetric question: Can we bound the minimum norm of a coﬁlling for a coboundary β in terms of the norm of β?

- Deﬁnition 2 (Coﬁlling/Coisoperimetric Inequality). Let L > 0. We say that X satisﬁes a L-coﬁlling inequality (or coisoperimetric inequality) in dimension k if, for every β ∈ Bk(X), there exists some α ∈ Ck−1(X) such that δα = β and α ≤ L β .




![image 10](<2015-dotterrer-expansion-topological-overlap_images/imageFile10.png>)

2More precisely, we work with the augmented cellular cochain complex of X, unless stated otherwise, i.e., we consider X to have a unique (−1)-dimensional cell, the empty cell ∅, which is incident to every vertex of X.

Any two coﬁllings of a given coboundary diﬀer by a cocycle. Thus, X satisﬁes an L-coﬁlling inequality in dimension k if and only if

1 L

· min{ α + ζ : ζ ∈ Zk−1(X)} for all α ∈ Ck−1(X). (3)

δα ≥

![image 11](<2015-dotterrer-expansion-topological-overlap_images/imageFile11.png>)

We can strengthen (3) by replacing cocycles with coboundaries and obtain a condition that also allows us to draw conclusions about the cohomology of X. For α ∈ Ck−1(X), let

[α] := min{ α + β : β ∈ Bk−1(X)} (4)

denote the distance (with respect to the norm · ) of α to the space Bk−1(X) of coboundaries.

- Deﬁnition 3 (Coboundary Expansion). Let η > 0. We say that X is η-expanding in dimension k, if for every (k − 1)-cochain α ∈ Ck−1(X),


δα ≥ η · [α] . (5)

Lemma 4. Let η > 0. A complex X is η-expanding in dimension k if and only if Hk−1(X) = 0 and X satisﬁes a 1/η-coisoperimetric inequality in dimension k.

Proof. Suppose that X is η-expanding in dimension k. Clearly, (5) implies (3), i.e., X satisﬁes a 1/η-coﬁlling inequality. Moreover, if α ∈ Ck−1(X) \ Bk−1(X) then [α] > 0, hence δα > 0, hence α  ∈ Zk−1(X). Thus, Zk−1(X) = Bk−1(X), i.e., Hk−1(X) = 0.

Conversely, assume that Hk−1(X) = 0. Then Zk−1(X) = Bk−1(X), so (5) and (3) are equivalent.

![image 12](<2015-dotterrer-expansion-topological-overlap_images/imageFile12.png>)

![image 13](<2015-dotterrer-expansion-topological-overlap_images/imageFile13.png>)

![image 14](<2015-dotterrer-expansion-topological-overlap_images/imageFile14.png>)

![image 15](<2015-dotterrer-expansion-topological-overlap_images/imageFile15.png>)

In some cases, however, vanishing of Hk−1(X) turns out to be too stringent a requirement, and we can replace it by the condition that every nontrivial cocycle has large norm:

Deﬁnition 5 (Large Cosystoles). Let ϑ > 0. We say that X has ϑ-large cosystoles in dimension j if α ≥ ϑ for every α ∈ Zj(X) \ Bj(X).

Example 6. Consider the case k = 1, with the normalized Hamming norm. In this case, η-expansion in dimension 1 corresponds to η-edge expansion of a graph (the 1-skeleton of the complex). An L-coﬁlling inequality in dimension 1 means that every connected component of the graph is 1/L-edge expanding. Having ϑ-large cosystoles in dimension 0 means that every connected component contains at least a ϑ-fraction of the vertices.

Local Sparsity of X

For the formal statement of the overlap theorem, we need one more technical condition on X. For a cell τ of X, let ιkτ be the k-dimensional cochain that assigns 1 to k-cells of X that have nonempty intersection with τ and 0 otherwise.

Deﬁnition 7. (Local Sparsity) Let ε > 0. We say that X is locally ε-sparse (with respect to a given norm · ) if ιkτ ≤ ε for every nonempty cell τ of X and every k, 0 ≤ k ≤ d.

For example, in the case of the normalized Hamming norm · H, local sparsity means that

|{σ ∈ Σk(X): τ ∩ σ = ∅}| ≤ ε|Σk(X)|,

for every nonempty cell τ of X. Formal Statement of the Theorem We are now ready to state Gromov’s theorem. Theorem 8 (Gromov’s Topological Overlap Theorem [8])). For every d ≥ 1 and L,ϑ >

- 0 there exists ε0 = ε0(d,L,ϑ) > 0 such that the following holds: Let X be a ﬁnite cell complex of dimension d, and let  ·  be a norm on the cochains


of X. Suppose that

- 1. X satisﬁes a L-coﬁlling inequality in dimensions 1,... ,d;
- 2. X has ϑ-large cosystoles in dimensions 0,... ,d − 1; and
- 3. X is locally ε-sparse for some ε ≤ ε0.


Then for every continuous map f : X → M into a compact connected d-dimensional piecewise-linear (PL) manifold M, there exists a point p ∈ M such that3

 {σ ∈ Σd(X) | p ∈ f(σ)}  ≥ µ, (6) where µ = µ(d,ε,L,ϑ) > 0.

Remark 9. The assumption that the manifold M is compact is not essential; moreover, we may assume without loss of generality that M has no boundary. Indeed, since X is compact, the image f(X) is compact and hence contained in a compact submanifold N of M with boundary ∂N; we can turn N into a compact manifold without boundary by doubling, i.e., by glueing two copies of N along their boundary.

If a complex X satisﬁes the conclusion of the theorem, we also say that X is topologically µ-overlapping for maps into d-dimensional PL manifolds. If the conclusion holds true just for aﬃne maps and M = d, we say that X is geometrically µ-overlapping.

![image 16](<2015-dotterrer-expansion-topological-overlap_images/imageFile16.png>)

3Here, we use that a subset of Σk(X) can be identiﬁed with a k-dimensional cellular cochain, its indicator function.

# 2 Preliminaries from Piecewise-Linear Topology

## 2.1 Assumptions on M

We assume that M is a compact connected piecewise-linear (PL) d-dimensional manifold, without boundary. That is, we assume that M admits a triangulation4 T with the property that the link of every nonempty simplex τ of T is a PL sphere of dimension d − 1 − dim(τ); throughout this paper, we only consider triangulations of M that have this property.

## 2.2 Approximation by PL maps

We can ﬁx a metric on M, e.g., by ﬁxing a triangulation T of M and by considering each simplex of T as a regular simplex with edge length 1. By subdividing a given triangulation T suﬃciently often, we can pass to a new triangulation T′ in which each simplex has diameter at most ρ > 0, for a given ρ (see, e.g., [12, Sec. 1.7]).

By the standard simplicial approximation theorem [14], given the triangulation T′ of M and a continuous map f : X → M, there is a simplicial approximation of f, i.e., there is a subdivision X′ of X and a simplicial map g: X′ → T′ such that, for each point x ∈ X, the image g(x) belongs to the (uniquely deﬁned) simplex of T′ whose relative interior contains f(x). (In fact, g is even homotopic to f, but we will not need that.) This map g is a PL map X → M and the distance between g(x) and f(x) is at most the maximum diameter of any simplex in T′, hence at most ρ, for every x ∈ X.

Thus, by the preceding discussion and the following lemma, it suﬃces to prove Thm. 8 for PL maps.

Lemma 10. Let f : X → M be a continuous map, and let gn: X → M be a sequence of continuous maps that converges to f pointwise, i.e., gn(x) → f(x) as n → ∞, for every x ∈ X. Suppose that for every gn there exists a point pn ∈ M such that  {σ ∈ Σd(X) | pn ∈ gn(σ)}  ≥ µ. Then there exists a point p ∈ M such that (6) holds.

Proof. By compactness, there is a subsequence of the points pn that converges to a point p. We claim that p is the desired point. Since there are only ﬁnitely many cells in X, there is some ρ > 0 such that for every d-cell σ of X with p  ∈ f(σ), the distance between p and f(σ) is at lest ρ. Choose n suﬃciently large so that the distance between pn and p is less than ρ/2, and the distance between f(x) and gn(x) is at most ρ/2, for every x ∈ X. If pn ∈ gn(σ), then the distance between p and f(σ) is less than ρ, so by the choice of ρ, we have p ∈ f(σ). Therefore, {σ ∈ Σd(X) | p ∈ f(σ)} ⊆ {σ ∈ Σd(X) | pn ∈ gn(σ)}, and the desired conclusion follows by the monotonicity property of the norm.

![image 17](<2015-dotterrer-expansion-topological-overlap_images/imageFile17.png>)

![image 18](<2015-dotterrer-expansion-topological-overlap_images/imageFile18.png>)

![image 19](<2015-dotterrer-expansion-topological-overlap_images/imageFile19.png>)

![image 20](<2015-dotterrer-expansion-topological-overlap_images/imageFile20.png>)

## 2.3 General Position

We refer to [16, Ch. VI] for a comprehensive treatment of general position for PL maps. The following deﬁnition summarizes the properties that we will need.

![image 21](<2015-dotterrer-expansion-topological-overlap_images/imageFile21.png>)

4The triangulation is necessarily ﬁnite, since M is compact.

Deﬁnition 11. Let X be a ﬁnite polyhedral cell complex, M a PL manifold, and let f : X → M be a PL map.

- 1. We say that f is in strongly general position (with respect to the given decomposition of X into polyhedral cells) if, for every r ≥ 1 and pairwise disjoint cells σ1,... ,σr of X,

dim ri=1 f(σi) ≤ max − 1, ri=1 dimσi − d(r − 1) . (7)

In particular, if the number of the right-hand side is −1, then the intersection is empty.

- 2. Given a triangulation T of M, we that that f is in general position with respect to T if, for every simplex σ of X and every simplex τ of T, dim(f(σ) ∩ τ) ≤ max{−1,dimσ + dimτ − d}; moreover, if dimσ + dimτ = d then we require that f(σ) and τ intersect transversely (either the intersection is empty, or they intersect locally like complementary linear subspaces).


The main fact that we will need is that any map f : X → M can be approximated arbitrarily closely by a PL map that is in general position:

Lemma 12 ([16, Ch. VI]). Let f : X → M be a PL map and let T be a triangulation of M. Then, up to a small perturbation, we may assume that f is general position with respect to T and in strongly general position.

Furthermore, we will need the following notion of suﬃciently ﬁne triangulations:

Deﬁnition 13. Let T be a triangulation of M and let f : X → M be a PL map in general position with respect to T. We say that T is suﬃciently ﬁne with respect to f if, for every k > 0 and every k-simplex τ of T,

 {σ ∈ Σd−k(X): f(σ) ∩ τ = ∅}  ≤

d k

max{ ιdσ−′ k : σ′ ∈ Σd−k(X)}.

![image 22](<2015-dotterrer-expansion-topological-overlap_images/imageFile22.png>)

Lemma 14. Suppose that f : X → M be a PL map in strongly general position and in general position with respect to a triangulation T of M. Then (by reﬁning T, if necessary), we may assume furthermore that T is suﬃciently ﬁne with respect to f.

Proof. If f is in general position with respect to T, then by choosing points at which we subdivide T in a suﬃciently generic way, we can assume that f is also in general position with respect to the subdivision T′. Thus, we may assume that T already has the property that every simplex of T has diameter smaller than some speciﬁed parameter ρ > 0.

Now suppose that σ1,... ,σr are pairwise distinct simplices of X with f(σ1) ∩ ... ∩ f(σr) = ∅. By compactness, there exists ρ = ρ(σ1,... ,σr) > 0 such that no matter how we select xi ∈ f(σi), some pair xi,xj has distance at least ρ. Since X is ﬁnite, there is some ρ > 0 that works for all ﬁnite collections of simplices whose images do not

have a common point of intersection. Suppose now that we have chosen T such that all simplices in T have diameter at most ρ/2.

Given τ ∈ T of dimension k > 0 consider S(τ) := {σ ∈ Σd−k(X): f(σ) ∩ τ = ∅}. We claim that σ∈S(τ) f(σ) = ∅. Otherwise, for every choice of points xσ ∈ f(σ), σ ∈ S(τ), there would be some pair σ,σ′ such that xσ and xσ′ have distance at least ρ. However, by the deﬁnition of S(τ), we can choose each xσ to lie in the intersection f(σ) ∩ τ, from which it follows that for every pair σ,σ′ ∈ S(τ), the distance between xσ and xσ′ is at most the diameter of τ, i.e., at most ρ/2.

Let {σ1,... ,σr} ⊆ S(τ) be an inclusion-maximal subset with σi ∩ σj = ∅ (i.e., the σi are pairwise vertex-disjoint; we can pick this subset greedily). Since f is in strongly general position and σ∈S(τ) f(σ) = ∅, it follows that ri=1(d − k) − d(r −

- 1) ≥ 0; this implies r ≤ d/k. Now, every other simplex σ ∈ S(τ) intersects one of


the σi. Thus, by monotonicity of the norm and by the triangle inequality, S(τ) ≤ d k max1≤i≤r ιdσ−i k .

![image 23](<2015-dotterrer-expansion-topological-overlap_images/imageFile23.png>)

![image 24](<2015-dotterrer-expansion-topological-overlap_images/imageFile24.png>)

![image 25](<2015-dotterrer-expansion-topological-overlap_images/imageFile25.png>)

![image 26](<2015-dotterrer-expansion-topological-overlap_images/imageFile26.png>)

![image 27](<2015-dotterrer-expansion-topological-overlap_images/imageFile27.png>)

## 2.4 Intersection Numbers

Deﬁnition 15 (Intersection numbers). If T is a PL triangulation of M and if f : X → M is a PL map in general position with respect to T, then for every pair of chains a ∈ Cd−k(X; 2) and b ∈ Ck(T; 2), we can deﬁne their (algebraic) intersection number

f(a) · b ∈ 2

as follows: If σ is a (d − k)-dimensional cell of X and if τ is a k-dimensional simplex of T, then by general position, the intersection f(σ) ∩ τ consists of a ﬁnite number of points, and the intersection number f(σ) · τ is deﬁned as the number of intersections5 modulo 2. This deﬁnition is extended by linearity (over 2) to arbitrary chains.

This yields, for 0 ≤ k ≤ d, an intersection number homomorphism

f⋔: Ck(T) → Cd−k(X), (8) deﬁned by f⋔(b)(a) = f(a) · b for each a ∈ Cd−k(X).

It is well-known that the intersection number homomorphism is a chain-cochain map, i.e., it commutes with the boundary and coboundary operators in the following sense (see, e.g., [11, Sec. 2.2] for a detailed review of this and other properties of intersection numbers).

Lemma 16.

f⋔(∂a) = δf⋔(a). For the proof of the main theorem, we need the following deﬁnition:

![image 28](<2015-dotterrer-expansion-topological-overlap_images/imageFile28.png>)

5There is a small caveat: In the case k = 0, an intersection point in f(σ)·τ may have several preimages in σ and should be counted with the corresponding multiplicity; equivalently, the intersection number is deﬁned as the number of points in σ ∩ f−1(τ) modulo 2.

Deﬁnition 17 (Chain-cochain homotopy). Consider two chain-cochain maps ϕ,ψ: Ck(M) →

Cd−k(X) from the (non-augmented) chain complex of M to the cochain complex of X. A chain-cochain homotopy between ϕ and ψ is a family of linear maps h: Ck(M) → Cd−k−1(X) such that ϕ − ψ = h∂ + δh. To keep track of the various maps, it is convenient to keep in mind the following diagram:

∂ C1(M)

∂

∂

∂

···

0 Cd(M)

C0(M)

Cd−1(M) ϕ ψ

0

![image 29](<2015-dotterrer-expansion-topological-overlap_images/imageFile29.png>)

![image 30](<2015-dotterrer-expansion-topological-overlap_images/imageFile30.png>)

![image 31](<2015-dotterrer-expansion-topological-overlap_images/imageFile31.png>)

![image 32](<2015-dotterrer-expansion-topological-overlap_images/imageFile32.png>)

![image 33](<2015-dotterrer-expansion-topological-overlap_images/imageFile33.png>)

![image 34](<2015-dotterrer-expansion-topological-overlap_images/imageFile34.png>)

✈✈✈✈✈h✈✈✈✈✈

✈✈✈✈✈✈✈h✈✈✈

③③③③③③h③③③

![image 35](<2015-dotterrer-expansion-topological-overlap_images/imageFile35.png>)

![image 36](<2015-dotterrer-expansion-topological-overlap_images/imageFile36.png>)

![image 37](<2015-dotterrer-expansion-topological-overlap_images/imageFile37.png>)

![image 38](<2015-dotterrer-expansion-topological-overlap_images/imageFile38.png>)

![image 39](<2015-dotterrer-expansion-topological-overlap_images/imageFile39.png>)

![image 40](<2015-dotterrer-expansion-topological-overlap_images/imageFile40.png>)

![image 41](<2015-dotterrer-expansion-topological-overlap_images/imageFile41.png>)

![image 42](<2015-dotterrer-expansion-topological-overlap_images/imageFile42.png>)

ϕ ψ

ϕ ψ

ϕ ψ h

h

0 C0(X) δ C1(X) δ ··· δ Cd−1(X) δ Cd(X) 0

![image 43](<2015-dotterrer-expansion-topological-overlap_images/imageFile43.png>)

![image 44](<2015-dotterrer-expansion-topological-overlap_images/imageFile44.png>)

![image 45](<2015-dotterrer-expansion-topological-overlap_images/imageFile45.png>)

![image 46](<2015-dotterrer-expansion-topological-overlap_images/imageFile46.png>)

![image 47](<2015-dotterrer-expansion-topological-overlap_images/imageFile47.png>)

![image 48](<2015-dotterrer-expansion-topological-overlap_images/imageFile48.png>)

(9)

# 3 Proof of the Overlap Theorem

Proof of Theorem 8. Let µ and ε0 be parameters that we will determine in the course of the proof. We assume that X satisﬁes the assumptions of the theorem, in particular that it is locally ε-sparse for some ε ≤ ε0.

Let f : X → M be a map. By the discussion in Sec. 2.2 and by Lemmas 12 and 14, we may assume that f is PL and in general position with respect to a suﬃciently ﬁne PL triangulation T of M.

We wish to show that there is a vertex v of T such that the intersection number cochain f⋔(v) ∈ Cd(X) satisﬁes f⋔(v) ≥ µ. We assume that this is not the case and we proceed to derive a contradiction.

Let v0 be a ﬁxed vertex of T; by assumption, f⋔(v0) < µ. (Note that if f is not surjective then we can choose the triangulation T and v0 so that f⋔(v0) = 0.)

We deﬁne a chain-cochain map6 G: C∗(T) → Cd−∗(X)

by setting G(v) := f⋔(v0) for every vertex v of T and G(c) = 0 for every c ∈ Ck(T; 2), k > 0.

We will construct a chain-cochain homotopy H : C∗(T) → Cd−1−∗(X) between f⋔ and G; that is, for every k, we construct a homomorphism

H : Ck(T) → Cd−1−k(X) such that

f⋔(c) − G(c) = H(∂c) + δH(c) (10)

for c ∈ Ck(T). We stress that for this proof, we work with non-augmented chain and cochain complexes as in (9), i.e., we use the convention that C−1(X) = 0. It follows

that G(c) = 0 for k > 0 and that H(c) = 0 for c ∈ Cd(M).

The chain-cochain homotopy H will yield the desired contradiction: Given the triangulation T of M, the formal sum of all d-dimensional simplices of T is a d-dimensional

![image 49](<2015-dotterrer-expansion-topological-overlap_images/imageFile49.png>)

6That is, a homomorphism G: Ck(T) → Cd−k(X) for every k such that G(∂c) = δG(c) for c ∈ Ck(T).

cycle ζM (here we use that M has no boundary). Note that f⋔(ζM) = 0X (every vertex v of X is mapped into the interior of a unique d-simplex of M) but G(ζM) = 0. This is a contradiction, since

0 = 0X = f⋔(ζM) − G(ζM) = H(∂ζM)

+δ H(ζM)

= 0.

![image 50](<2015-dotterrer-expansion-topological-overlap_images/imageFile50.png>)

![image 51](<2015-dotterrer-expansion-topological-overlap_images/imageFile51.png>)

![image 52](<2015-dotterrer-expansion-topological-overlap_images/imageFile52.png>)

![image 53](<2015-dotterrer-expansion-topological-overlap_images/imageFile53.png>)

=0

=0 since ∂ζM=0

To complete the proof, it remains construct H, which we will do by induction on k. For k = 0, we observe that for every vertex v of T, the cochains f⋔(v) and G(v) =

f⋔(v0) are cohomologous, i.e., their diﬀerence is a coboundary: We assume that M is connected, hence there is a 1-chain (indeed, a path) c in T with ∂c = v − v0, and so f⋔(v)−G(v) = f⋔(v−v0) = δf⋔(c). For every vertex v of T, we set H(v) to be a coﬁlling of f⋔(v) − G(v) of minimal norm (if there is more than one minimal coﬁlling, we choose one arbitrarily). Thus, the homotopy condition (10) is satisﬁed for 0-chains (since chains and cochains of dimension less than zero or larger than d are, by convention, zero).

By choice of H(v) and the coisoperimetric assumption on X, we have H(v) ≤ L f⋔(v) − f⋔(v0)

< s0 := 2Lµ.

![image 54](<2015-dotterrer-expansion-topological-overlap_images/imageFile54.png>)

![image 55](<2015-dotterrer-expansion-topological-overlap_images/imageFile55.png>)

<2µ

Inductively, assume that we have already deﬁned H on chains of dimension less than k and that H(ρ) < si for every i-simplex of T, i < k, where si is a parameter that we will determine inductively. Thus, if τ is a k-simplex of T, then H(∂τ) is already deﬁned and has norm less than (k + 1)sk−1.

Moreover, we have f⋔(τ) ≤ kdε ≤ dε, by the sparsity assumption on X and since the triangulation T is suﬃciently ﬁne.

![image 56](<2015-dotterrer-expansion-topological-overlap_images/imageFile56.png>)

By construction, z := f⋔(τ) − H(∂τ) is a (d − k)-dimensional cocycle, and z ≤ f⋔(τ) − H(∂τ) < dε + (k + 1)sk−1. (11)

If z is cohomologically trivial, i.e., z ∈ Bd−k(X), then we deﬁne H(τ) to be a minimal coﬁlling of z and extend H to Ck(T) by linearity. By assumption on X, we get

H(τ) < sk := L(dε + (k + 1)sk−1) . Note that this recursion yields sk = dε(L + ··· + Lk) + (k + 1)!Lk+12µ. If z is nontrivial,7 then by the assumption on large cosystoles and (11), ϑ ≤ z < dε + (k + 1)sk−1,

which is a contradiction if we choose µ and ε0 (and hence ε) suﬃciently small with respect to d, L and ϑ.

![image 57](<2015-dotterrer-expansion-topological-overlap_images/imageFile57.png>)

![image 58](<2015-dotterrer-expansion-topological-overlap_images/imageFile58.png>)

![image 59](<2015-dotterrer-expansion-topological-overlap_images/imageFile59.png>)

![image 60](<2015-dotterrer-expansion-topological-overlap_images/imageFile60.png>)

![image 61](<2015-dotterrer-expansion-topological-overlap_images/imageFile61.png>)

7Note that in the special case that X is connected and k = d, the only nontrivial 0-cocycle is z = 0X, hence z = 1.

Remarks 18. 1. In many interesting cases, X belongs to an inﬁnite family of complexes for which the local sparsity parameter ε tends to zero as the size of the complex increases. For instance, if X is the d-skeleton of the n-simplex, n → ∞, then we have ε = O(1/n). For complexes with local sparsity ε = o(1), the above

proof yields µ ≥ 2(k+1)!ϑ Lk + o(1). If M is unbounded, then, as remarked in the proof, we can take the vertex v0 to satisfy f⋔(v0) = 0, which improves the estimate by a factor of 2.

![image 62](<2015-dotterrer-expansion-topological-overlap_images/imageFile62.png>)

More quantitative information and better bounds on the overlap constant (which are of interest for speciﬁc families of complexes, e.g., skeleta of simplices) can be gleaned from the proof by a more reﬁned analysis through the coﬁlling proﬁles of X [8], which estimate the size of a minimal coﬁlling of a cocycle b as a possibly nonlinear function of b . Further improvements in the estimates are possible trough the notion of pagodas [13].

- 2. The proof of the overlap theorem is very robust and easily generalizes to other settings, in particular to other coeﬃcient rings and other norms. Suppose that R is a ﬁxed ring of coeﬃcients (commutative, with 1), and consider (co)chains and (co)homology with R-coeﬃcients. If R is not of characteristic 2, we need to add some minor assumptions to deal with orientations. First, we need to assume

that he target manifold M is R-orientable, i.e., that Hd(M;R) ∼= R, generated by a fundamental homology class [M]. The deﬁnition of the intersection number changes slightly: if two oriented linear simplices σ,τ of complementary dimensions in M intersect transversely in a single point, then their orientations determine a local orientation of M, and we set the intersection number σ · τ to be +1 or −1 depending on whether this orientation agrees with the chosen global orientation of M or not.

Second, we need to assume that the norm of a cochain is invariant under sign changes in the values of the cochain, i.e., if two k-cochains c,c′ ∈ Ck(X;R) satisfy c(σ) = ±c′(σ) for every orientated k-cell σ of X (the signs may be diﬀerent for diﬀerent σ), then c = c .

With these additional assumptions, the proof of Theorem 8 goes through also for R-coeﬃcients and yields that for every f : X → M, there exists p ∈ M such (6) holds.

- 3. For norms other than the normalized Hamming norm, f⋔(p) ≥ µ does not necessarily imply that (1) holds. For instance, suppose that R = and that we

work with the ℓ2-norm. In this case, large norm f⋔(p) might be caused by a single d-simplex σ such that f⋔(p)(σ) is a large integer, i.e., f(σ) intersects p with large multiplicity. However, this problem does not occur if we impose additional assumptions on the map f, e.g., that f⋔(p)(σ) is bounded by some constant K in absolute value (e.g., if f is linear, then we can take K = 1).

- 4. We used the assumption that M is piecewise-linear in order to apply standard general position arguments from piecewise-linear topology. We believe that the result


holds more generally if M is a homology manifold. General position arguments for homology manifolds are much more subtle, but for the proof we do not really need to perturb the map f to general position (which may not be possible), we only need a general position chain map that is close to the chain map induced by f. We plan to investigate this in more detail in a future paper.

Acknowledgement.

We would like to thank the anonymous referees for many helpful remarks concerning the presentation.

# References

- [1] I. B´ara´ny. A generalization of Carathe´odory’s theorem. Discrete Math. 40 (2–3), 141–152, 1982.
- [2] E. Boros and Z. Fu¨redi. The number of triangles covering the center of an n-set. Geom. Dedicata 17, 69–77, 1984.
- [3] A. Bjo¨rner. Topological Methods. In: R. L. Graham, M. Gro¨tschel and L. Lov´asz (eds.), Handbook of Combinatorics, Vol. 2, pp. 1819–1872. Elsevier, Amsterdam, 1995.
- [4] D. Burago, Y. Eliashberg, M. Bestvina, F. Forstnericˇ, L. Guth. A. Nabutovsky, A. Phillips, J. Roe, and A. Vershik. A Few Snapshots from the Work of Mikhail Gromov. In: H. Holden and R. Piene (Eds.). The Abel Prize, 2008–2012, SpringerVerlag, Berlin 2014, pp. 139–234.
- [5] Dominic Dotterrer, Tali Kaufman, and Uli Wagner. On Expansion and Topological Overlap. In: Sa´ndor Fekete and Anna Lubiw (eds.). 32nd International Symposium on Computational Geometry (SoCG 2016), volume 51 of Leibniz International Proceedings in Informatics (LIPIcs), pp. 35:1–35:10, Dagstuhl, Germany, 2016. Schloss Dagstuhl–Leibniz-Zentrum fuer Informatik.
- [6] S. Evra and T. Kaufman. Systolic Expanders of Every Dimension. Preprint, http://arxiv.org/abs/1510.00839v2.
- [7] T. Kaufman, D. Kazhdan, A. Lubotzky. Isoperimetric Inequalities for Ramanujan Complexes and Topological Expanders. Proceedings of the 55th Annual Symposium on Foundations of Computer Science (FOCS), 2014.
- [8] M. Gromov. Singularities, expanders and topology of maps. Part 2: From combinatorics to topology via algebraic isoperimetry, Geometric and Functional Analysis, 20(2):416–526, 2010.
- [9] R. Karasev. A simpler proof of the Boros–Fu¨redi–B´ar´any–Pach–Gromov theorem. Discrete & Computational Geometry 47(3), 492–495, 2012.


- [10] N. Linial and R. Meshulam. Homological connectivity of random 2-complexes, Combinatorica, 26(4):475–487, 2006.
- [11] I. Mabillard and U. Wagner. Eliminating higher-multiplicity intersections, I. A Whitney trick for Tverberg-type problems. Preprint, http://arxiv.org/abs/1508.02349v1.
- [12] J. Matousˇek. Using the Borsuk–Ulam theorem. Springer-Verlag, Berlin, 2003.
- [13] J. Matousˇek and U. Wagner. On Gromov’s method of selecting heavily covered points. Discrete & Computational Geometry 52(1), 1–33, 2014.
- [14] V. Prasolov. Elements of combinatorial and diﬀerential topology. American Mathematical Society, Providence, RI, 2006.
- [15] C. P. Rourke and B. J. Sanderson, Introduction to piecewise-linear topology. Springer-Verlag, New York, 1972.
- [16] E. C. Zeeman. Seminar on Combinatorial Topology. Lecture Notes, Institut des Hautes Etudes´ Scientiﬁques, 1963. Scanned notes available at http://www.maths.ed.ac.uk/ aar/papers/zeemanpl.pdf.


