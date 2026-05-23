---
type: source
kind: paper
title: The Theta Number of Simplicial Complexes
authors: Christine Bachoc, Anna Gundert, Alberto Passuello
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1704.01836v1
source_local: ../raw/2017-bachoc-theta-number-simplicial-complexes.pdf
topic: general-knowledge
cites:
---

# arXiv:1704.01836v1[math.CO]6Apr2017

## THE THETA NUMBER OF SIMPLICIAL COMPLEXES

CHRISTINE BACHOC, ANNA GUNDERT, AND ALBERTO PASSUELLO

ABSTRACT. We introduce a generalization of the celebrated Lov´asz theta number of a graph to simplicial complexes of arbitrary dimension. Our generalization takes advantage of real simplicial cohomology theory, in particular combinatorial Laplacians, and provides a semideﬁnite programming upper bound of the independence number of a simplicial complex. We consider properties of the graph theta number such as the relationship to Hoffman’s ratio bound and to the chromatic number and study how they extend to higher dimensions. Like in the case of graphs, the higher dimensional theta number can be extended to a hierarchy of semideﬁnite programming upper bounds reaching the independence number. We analyse the value of the theta number and of the hierarchy for dense random simplicial complexes.

1. INTRODUCTION

The theta number ϑ(G) of a graph G was introduced by L. Lov´asz in his seminal paper [32], in order to provide spectral bounds of the independence number and of the chromatic number of G. In modern terms, ϑ(G) is the optimal value of a semideﬁnite program, and as such is computationally easy; in contrast, the independence number α(G) and the chromatic number χ(G) are difﬁcult to compute. These graph invariants satisfy the following inequalities, where G denotes the complement of G:

(1) α(G) ≤ ϑ(G) ≤ χ(G).

The inequality α(G) ≤ ϑ(G) was one of the main ingredients in Lov´asz’ proof of the Shannon conjecture on the capacity of the pentagon [32]. More generally, this inequality plays a central role in extremal combinatorics, sometimes in a disguised form: to cite a few, the Delsarte linear programming method in coding theory [8] and recent generalizations of Erd¨os-Ko-Rado theorems [7, 12, 13] can be interpreted as instances of this inequality. Analogs of the theta number in geometric settings have lead to many advances in packing problems (see [36] and references therein), in particular the very recent solutions to the sphere packing problems in dimensions 8 and 24 [5, 40].

Our aim in this paper is to generalize this graph parameter to higher dimensions, in the framework of simplicial complexes. Let us recall that an (abstract) simplicial complex X on a ﬁnite set V is a family of subsets of V called faces that is closed under taking subsets. We refer to Section 1 for basic deﬁnitions and results about simplicial complexes. Graphs ﬁt in this framework, being simplicial complexes of dimension 1. In recent years, considerable work has been devoted to generalizing the classical theory of graphs to this higher-dimensional setting. Much of the efforts have focused on the notion of expansion (see, e.g., [9, 15, 20, 27, 33, 38]), but other natural concepts such as random walks [37], trees [11, 26], planarity [35], girth [10, 34], independence and chromatic numbers [14, 19] have been extended to higher dimensions. Some of these notions were introduced and studied previously in the context of hypergraphs. Pure k-dimensional simplicial complexes

Date: July 25, 2018.

1

are essentially (k + 1)-uniform hypergraphs, but the topological point of view brings the machinery of algebraic topology such as homology theory to the subject.

The familiar graph-theoretic notions of independence number and of chromatic number extend in a natural way to this setting: For a k-dimensional simplicial complex X, an independent set is a set of vertices that does not contain any maximal face of X, and the independence number α(X) is the maximal cardinality of an independent set. The chromatic number1 χ(X) is the least number of colors needed to color the vertices so that no maximal face of X is monochromatic, in other words, it is the smallest number of parts of a partition of the vertices into independent sets.

In order to deﬁne the theta number ϑk(X) of a pure k-dimensional simplicial complex X, we will follow an approach that leads in a natural way to the inequality α(X) ≤ ϑk(X). The main idea is to associate to an independent set S a certain matrix, and then to design a semideﬁnite program that captures as many properties of this matrix as possible. The matrix that we associate to an independent set is (up to a multiplicative factor) a submatrix of the down-Laplacian of the complete complex. In the case of dimension 1, the downLaplacian is simply the all-one matrix, and we end up with one of the many formulations of the Lov´asz theta number.

Our ﬁrst task will be to compare ϑk(X) to the eigenvalue upper bound of α(X) proved by Golubev in [19]. This upper bound involves for 0 ≤ i ≤ k − 1, the largest eigenvalues µi of the i-th up-Laplacians of X and the minimal degrees di of the i-faces of X:

(d0 + 1)(d1 + 2)...(dk−2 + k − 1)dk−1 µ0 ...µk−1

### (2) α(X) ≤ n 1 −

.

When every possible (k − 1)-face is contained in at least one k-face, i.e., when X has a complete (k − 1)-skeleton, this inequality simpliﬁes to

dk−1 µk−1

### (3) α(X) ≤ n 1 −

and can thus be seen as a natural generalization of the celebrated ratio bound for graphs attributed to Hoffman (see, e.g., [4, Theorem 3.5.2]). In that case, we will show that

dk−1 µk−1

ϑk(X) ≤ n 1 −

,

therefore ϑk(X) provides an upper bound of α(X) that is at least as good as (3). In the case of a non-complete (k − 1)-skeleton, Golubev’s bound and ϑk(X) turn out to be incomparable, as we will see in examples below.

The theta number of a graph has many very nice properties; some of them, although unfortunately not all of them, can be generalized to higher dimensions. Most of this paper is devoted to determining which of the properties of the graph theta number extend to our notion of the theta number of simplicial complexes.

The relationship to the chromatic number generalizes only partially. Indeed, the inequality α(X) ≤ ϑk(X) immediately leads to the inequality n/ϑk(X) ≤ χ(X). However, in the case of graphs, the stronger inequality ϑ(G) ≤ χ(G) holds. We will see that its natural analog in the setting of k-complexes would be that ϑk(X) ≤ kχ(X) and that this inequality does not hold in general. Instead, we will introduce an ad hoc notion of chromatic number for simplicial complexes, denoted χk(X), and show that the inequality ϑk(X) ≤ χk(X) holds. While χ(X) is deﬁned using vertex colorings, the deﬁnition of

1In the study of hypergraphs, the chromatic number χ(X) is also known as the weak chromatic number while χ(X1), the chromatic number of the 1-skeleton, is known as the strong chromatic number.

χk(X) is based on colorings of (k−1)-faces respecting orientations. Moreover, it is tightly related to a notion of homomorphisms between pure k-dimensional simplicial complexes that we introduce and that may be of interest by itself.

A very interesting beneﬁt of the theta number of a graph is that it is possible to expand it into hierarchies of semideﬁnite upper bounds of the independence number; Lassere’s hierarchy based on polynomial optimization principles is one of the most popular (see [29, 30]). We will see that a similar situation holds in higher dimensions: to a pure kdimensional complex X we will associate a sequence ϑˆ (X) for = k,...,α(X) such that

### α(X) = ϑˆα(X)(X) ≤ ··· ≤ ϑˆ (X) ≤ ··· ≤ ϑˆk(X) ≤ ϑk(X).

In order to deﬁne ϑˆ (X), we will proceed in two steps: in a ﬁrst step, we deﬁne a natural sequence ϑ (X) for = k,k + 1,...,α(X); in a second step, we modify the deﬁnition of ϑ (X) slightly in such a way that the sequence of its values decreases.

Our last results concern the theta number of random simplicial complexes Xk(n,p) from the model proposed by Linial and Meshulam in [31]. This model is a higher-dimensional analog of the Erd˝os-R´enyi model G(n,p) for random graphs and has gained increasing attention in recent years (see [25] for a survey).

We show that ϑk(Xk(n,p)) is of the order of (n − k)(1 − p)/p for probabilities p such that c0 log(n)/n ≤ p ≤ 1 − c0 log(n)/n for some constant c0. This result extends the known estimates for the value of the theta number of the random graph G(n,p).

The paper is organized as follows: Sections 2 and 3 recall basic deﬁnitions and properties of simplicial complexes and semideﬁnite programming. Section 4 recalls properties of the theta number of a graph that serve as a guideline for the theta number of a k-dimensional simplicial complex, which is introduced in Section 5. Section 6 computes the theta number of certain basic families of 2-dimensional simplicial complexes. Section 7 discusses chromatic numbers and Section 8 the hierarchy of theta numbers. The ﬁnal Section 9 contains the analysis of the theta number of random simplicial complexes.

2. SIMPLICIAL COMPLEXES

Let V = {v1,...,vn} be a ﬁnite set. We will use the notation Vk for the set of ksubsets of V . Let us recall that an (abstract) simplicial complex X on a vertex set V is a family of subsets of V (called the faces of X), such that if F ∈ X, then all subsets of F also belong to X. The dimension of a face F ∈ X is |F| − 1, and we denote by Xi the set of i-dimensional faces of X, with the convention X−1 = {∅}. Note that we do not require every element in V to be a 0-face of X, so X0 can be a proper subset of V . The i-skeleton of X is the simplicial complex X−1 ∪ X0 ∪ ··· ∪ Xi.

A simplicial complex X is said to be of dimension k ≥ 0, if k is the maximal dimension of any of its faces. For example, a graph is a simplicial complex of dimension 1. Going back to the general case, if X is of dimension k, and if moreover all maximal (with respect to inclusion) faces of X are of dimension k, then X is said to be pure. Unless explicitly mentioned, we will only consider pure complexes.

A basic example of a pure k-dimensional simplicial complex is the complete k-complex Knk, whose faces are all the subsets of [n] = {1,...,n} that have at most (k+1) elements.

We note that in order to deﬁne a pure simplicial complex of dimension k, it is enough to specify its set of k-dimensional faces. In particular, the complementary complex X of a pure simplicial complex of dimension k, is again a pure simplicial complex of dimension k, whose k-dimensional faces are those (k + 1)-subsets of V that do not belong to Xk

(we adopt the convention that the empty complex, whose set of faces is empty, is pure of dimension k for all k ≥ 0).

Let X be a simplicial complex; we assume that every face of X is endowed with an orientation, i.e., a local ordering of its vertices. Then, if F ∈ Xi and K ∈ Xi−1, an oriented incidence number [F : K] ∈ {0,±1} can be deﬁned. Often, the orientation of the faces is induced by a global ordering of the vertex set V ; in that case, if F = {x0,x1,...,xi} where x0 < x1 < ··· < xi with respect to this ordering,

(−1)j if K ⊂ F and F \ K = {xj}, 0 otherwise.

[F : K] =

The vector space of functions from Xi to R is denoted by Ci(X;R) and its elements are called i-dimensional cochains of X with coefﬁcients in R. The coboundary map δi : Ci(X;R) → Ci+1(X;R) is deﬁned for −1 ≤ i < dim(X) by

(δif)(H) =

[H : F]f(F).

F∈Xi

The image of δi−1 is the subspace Bi(X;R) of i-dimensional coboundaries, and the kernel of δi is the subspace Zi(X;R) of i-dimensional cocycles. Because the coboundary maps satisfy δi ◦ δi−1 = 0, we have Bi(X;R) ⊆ Zi(X;R). The quotient group

### Hi(X;R) := Zi(X;R)/Bi(X;R).

is then called the i-th cohomology group of X with coefﬁcients in R.

Analogously, we can deﬁne the homology groups of a simplicial complex. For this, the spaces Ci(X;R) are endowed with the standard inner product f,g = F∈X

### f(F)g(F)

i

and the boundary map ∂i+1 = δi∗ : Ci+1(X;R) → Ci(X;R) is deﬁned as the adjoint of the coboundary map δi. We have, for F ∈ Xi,

(∂i+1f)(F) =

[H : F]f(H).

H∈Xi+1

The spaces of boundaries Bi(X;R) := im∂i+1 and of cycles Zi(X;R) := ker∂i are subspaces of Ci(X;R) satisfying Bi(X;R) ⊆ Zi(X;R) and thus deﬁne the i-th reduced homology group of X

### Hi(X;R) := Zi(X;R)/Bi(X;R).

Moreover, by duality we have that Zi(X;R) = Bi(X;R)⊥ and Zi(X;R) = Bi(X;R)⊥. The following diagram summarizes these linear maps for 0 ≤ i ≤ dim(X) − 1:

δi−1

δi

Ci(X;R)

Ci−1(X;R)

### Ci+1(X;R)

∂i

∂i+1

The i-th up-Laplacian L↑i and i-th down-Laplacian L↓i of X are the following selfadjoint and positive semideﬁnite operators on Ci(X;R):

L↓i := δi−1∂i, L↑i := ∂i+1δi.

By deﬁnition, L↑i L↓i = L↓i L↑i = 0. Furthermore, it is not hard to see that kerL↓i = Zi(X;R), imL↓i = Bi(X;R), kerL↑i = Zi(X;R), and imL↑i = Bi(X;R). For

Hi(X;R) := Zi(X;R) ∩ Zi(X;R),

we have the Hodge decomposition of Ci(X;R) into pairwise orthogonal subspaces

### Ci(X;R) = Hi(X;R) ⊕ Bi(X;R) ⊕ Bi(X;R).

### In particular, Hi(X;R) Hi(X;R) Hi(X;R).

The characteristic functions eF of faces F ∈ Xi are called elementary cochains; they form an orthonormal basis of Ci(X;R). In order to express the matrices of the Laplacian operators in this basis we introduce the following notation: for F ∈ Xi, let deg(F) denote the degree of F, i.e., the number of (i + 1)-faces of X that contain F. For (F,F ) ∈ Xi2, such that |F ∩ F | = i, let

F,F := [F : F ∩ F ][F : F ∩ F ]. We note that, if F ∪ F ∈ Xi+1, we can express F,F also as

F,F = −[F ∪ F : F][F ∪ F : F ].

For (F,F ) ∈ Xi2, such that |F ∩ F | = i, we set F,F = 0. Then, it is easy to see that

i + 1 if F = F

(L↓i )F,F =

F,F otherwise and

 

deg(F) if F = F − F,F if F ∪ F ∈ Xi+1 0 otherwise

(L↑i )F,F =



where we use the same notations for the operators and for their matrices in the basis of elementary cochains.

- Example 2.1. In the case of the simplicial complex associated to a graph G = (V,E), deﬁned by X−1 = {∅}, X0 = V and X1 = E, we ﬁnd that L↓0 = J is the all-ones matrix

and L↑0 is equal to the combinatorial Laplacian L = D−A where D is the diagonal matrix with the degrees of the vertices as diagonal elements and A is the adjacency matrix of the graph.

- Example 2.2. For the complete k-complex Knk, and for 0 ≤ i ≤ k − 1, it is easy to verify that


### L↑i + L↓i = nI.

Together with the property L↑i L↓i = 0, we obtain that (L↑i )2 = nL↑i and that (L↓i )2 = nL↓i . So n is the only non zero eigenvalue of the up and down Laplacians. Computing the traces

of these operators gives the multiplicities of this eigenvalue, namely n−i 1 for L↓i and n−1 i+1 for L↑i . So we have

n − 1 i + 1

ker(L↑i − nI) = im(L↑i ) = Bi, dim(Bi) =

,

n − 1 i

ker(L↓i − nI) = im(L↓i ) = Bi, dim(Bi) =

,

and, as these dimensions add up to i+1 n = dim(Ci), Hi = {0}. We conclude this section by recalling the deﬁnition of the adjacency matrix of a k-

dimensional simplicial complex X: it is the matrix A such that L↑k−1 = D − A where D is the diagonal matrix encoding the degrees of the (k − 1)-faces. In other words,

if F ∪ F ∈ Xk 0 otherwise

AF,F = F,F

We note that in dimension 1 this deﬁnition coincides with the usual notion of the adjacency matrix of a graph.

3. SEMIDEFINITE PROGRAMMING

In this section, we gather basic facts about semideﬁnite programs. For further information we refer to standard references such as [2], [3], [39].

Semideﬁnite programs (SDP for short) are special cases of convex optimization programs that admit efﬁcient algorithms, such as algorithms based on the so-called interior point method. They generalize linear programs and have turned out to be very useful for providing polynomial time approximations of hard problems in many areas, especially in combinatorics (see, e.g., [18] and [1, Chapter 6]).

For a matrix A ∈ Rn×n we say that A is positive semideﬁnite, denoted by A 0, if A is real-valued, symmetric, and if all its eigenvalues are nonnegative. If moreover none of its eigenvalues are equal to zero, A is positive deﬁnite (A 0). The set of all positive semideﬁnite matrices is a cone denoted by Rn× 0n. The space of real symmetric matrices is endowed with the standard inner product A,B = trace(AB).

Given (c1,...,cm) ∈ Rm and symmetric matrices A0,...,Am of size n, the following optimization problem is a semideﬁnite program in primal form:

### p∗ = sup{ A0,Z : Z ∈ Rn× 0n, Ai,Z = ci for all 1 ≤ i ≤ m}.

In other words, this program asks for the supremum of a linear form, where this supremum is taken over the intersection of the cone of positive semideﬁnite matrices with an afﬁne space.

A feasible solution of this program is a matrix Z that satisﬁes the required constraints:

Z ∈ Rn× 0n and Ai,Z = ci. It is an optimal solution if its objective value A0,Z is equal to p∗. If there is no feasible solution, we let p∗ = −∞.

The following dual program is attached to the primal program:

### d∗ = inf{c1x1 +···+cmxm : (x1,...,xm) ∈ Rm, −A0 +x1A1 +···+xmAm 0}.

The terms ’primal’ and ’dual’ do not refer to a speciﬁc class of programs: Despite their apparent difference, any of these programs can be put in the form of the other, and, as expected, dualizing twice returns the initial program.

The inequality p∗ ≤ d∗, referred to as weak duality, always holds, and under some mild conditions even strong duality, i.e., p∗ = d∗, holds. Strong duality is guaranteed if the SDP satisﬁes the so-called Slater’s conditions, of which we will use the following version: If an SDP has a strictly feasible primal solution, i.e., if there is a feasible solution Z of the primal program such that Z 0, and a strictly feasible dual solution, i.e., there exists (x1,...,xm) such that −A0 + x1A1 + ··· + xmAm 0, then strong duality holds and, moreover, there are optimal solutions for both the primal and the dual program.

4. THE THETA NUMBER OF A GRAPH

In this section, we introduce the theta number of a graph G = (V,E). Our presentation will serve as a guideline for the generalization to higher dimensional simplicial complexes.

Let S be an independent set of G, i.e., a subset of V not containing any edges. The set S naturally deﬁnes a vector 1S ∈ RV , namely its characteristic vector. We consider the matrix Y S := 1S1TS, whose entries are given by:

- 0 if {v,v } S
- 1 otherwise.


Yv,vS =

The following properties of Y S motivate the deﬁnition of ϑ(G): Y S is a positive semidefinite matrix such that Yv,vS = 0 if {v,v } ∈ E. Furthermore, the cardinality of S can be

recovered in two different ways from Y S: If I and J stand as usual for the identity matrix and the all-ones matrix, we have I,Y S = |S| and J,Y S = |S|2. So, if we set

- (4) ϑ(G) = sup{ J,Y : Y ∈ RV ×V , Y 0, I,Y = 1, Yv,v = 0 if {v,v } ∈ E}

the matrix |S|−1Y S is feasible for (4) and we get that |S| ≤ ϑ(G).

Because (4) is a semideﬁnite program, its optimal value ϑ(G) can be approximated numerically up to arbitrary precision in polynomial time in the size of G. If, instead of a sharp numerical value, one aims for a rougher upper bound of ϑ(G), the dual formulation of (4) is often more convenient:

- (5) ϑ(G) = inf{λmax(Z) : Z ∈ RV ×V , Z = J + T, Tv,v = 0 if {v,v } ∈/ E}.

Here, λmax(Z) denotes the largest eigenvalue of Z.

To illustrate this principle we consider a classical example. For any matrix T such that Tv,v = 0 for all {v,v } ∈/ E, the dual formulation of ϑ(G) provides the inequality α(G) ≤ λmax(J + T). A possible choice for T is a multiple of the adjacency matrix A of G, say T = tA. The best bound is obtained for t minimizing λmax(J + tA). For d-regular graphs, the matrices J and A commute, so the eigenvalues of J + tA are easy to analyze. The optimal choice of t then leads to the so-called ratio bound attributed to Hoffman (see, e.g., [4, Theorem 3.5.2]):

- (6) α(G) ≤

−|V |λmin(A) d − λmin(A)

.

5. THE THETA NUMBER OF A SIMPLICIAL COMPLEX

We now move to higher dimensions and deﬁne the theta number of a k-dimensional simplicial complex X. As suggested in the introduction, the down-Laplacian L↓k−1 of the complete complex Knk will play the role of the all-ones matrix J in (4) and (5). Recall that L↓k−1 is the matrix indexed by Vk that is deﬁned by:

(L↓k−1)F,F =

k if F = F F,F otherwise

We note that this matrix may not be the down-Laplacian of the complex X. Obviously, this is the case if and only if X has a complete (k − 1)-skeleton, otherwise the downLaplacian of X is a principal submatrix of L↓k−1. From now on, to avoid confusion, we will denote the matrices associated to X by L↓i (X), L↑i (X) and reserve the notations L↓i , L↑i for the complete complex.

Let S ⊂ V be an independent set of X. Following the same strategy as in the case of graphs, we consider the following matrix Y S, indexed by Vk :

- (7) (Y S)F,F =


0 if F ∪ F S (L↓k−1)F,F otherwise.

We have Y S = δ(S

, where as a generalization of the characteristic vector of S, we consider the matrix δ(S

)δT

(S

)

k

k

) deﬁned as follows:

k

### δ(S

) K,F =

k

0 if F S (δS)K,F otherwise,

where K ∈ k V−1 , F ∈ Vk and δ is the matrix of the boundary operator δk−2 with respect to the basis of elementary cochains. The properties of Y S lead to the following deﬁnition

of ϑk(X): Deﬁnition 5.1. Let X be a pure k-dimensional complex on V , and let L↓k−1 be the down Laplacian of the complete complex on V . Let:

- (8)

ϑk(X) := sup L↓k−1,Y : Y ∈ R(V

k

)×(V

k

), Y 0, I,Y = 1, YF,F = 0 if F ∪ F ∈ Xk, YF,F = 0 if |F ∪ F | ≥ k + 2,

F,F YF,F = F ,F†YF ,F† if F ∪ F = F ∪ F†

- Proposition 5.2. We have α(X) ≤ ϑk(X).

Proof. Let S be an independent set with |S| = α(X). As Y S = δ(S

k

)δT

(S

k

)

, the matrix Y S is clearly positive semideﬁnite. We have

(9) Y S,I = k |S|

k and

(10)

Y S,L↓k−1 = k2 |S|

k

+

|F∪F |=k+1 F∪F ⊆S

1

= k2 |S| k

+ (k + 1)k |S| k + 1

= k |S|

k |S|. Moreover, from the fact that S is an independent set, and from the deﬁnition of Y S (7), it is clear that (Y S)F,F = 0 if F ∪ F ∈ Xk, or if |F ∪ F | ≥ k + 2.

The conditions F,F YF,F = F ,F†YF ,F† if F ∪ F = F ∪ F† are satisﬁed by the entries of L↓k−1, so the matrix Y S inherits this property.

To sum up, we have proved that the matrix k−1 |Sk| −1Y S is feasible for ϑk(X). Since its objective value is equal to |S|, we can conclude that α(X) ≤ ϑk(X).

Now we consider the dual program of (8), in order to obtain another formulation of ϑk(X), similar to (5).

- Proposition 5.3. We have


- (11)


ϑk(X) = inf λmax(Z) : Z = L↓k−1 + T, TF,F = 0 for all F ∈ Vk F∪F =H F,F TF,F = 0 if H ∈ k V+1 \ Xk

Proof. This is just a straightforward rewriting of the dual program. Both programs have the same objective value because Slater’s condition holds: Y = nk −1I is a strictly feasible solution of (8) and T = 0 gives rise to a strictly feasible solution of (11).

Remark 5.4. Let us make a few obvious observations about ϑk(X). The ﬁrst one, is that, as expected, k ≤ ϑk(X) ≤ n. Indeed, the lower bound follows by taking Y = nk −1I in (8) while the upper bound follows by taking T = 0 in (11).

The second observation is that ϑk(X) is easy to determine for the empty and the com-

plete k-complexes. Indeed, if X is the empty k-complex, the matrix Y = k−1 nk −1L↓k−1 is feasible for (8) giving that ϑk(X) = n. If X is the complete k-complex, the semideﬁnite

program (8) has only one feasible solution which is Y = nk −1I so ϑk(X) = k. We note that, in these trivial cases, the equality α(X) = ϑk(X) holds.

The beneﬁt of the formulation (11) is that any feasible matrix T leads to an upper bound of ϑk(X) and therefore to an upper bound of the independence number of X. Let us illustrate this principle by showing that we can recover the upper bound proved by Golubev [19] in the case of a k-dimensional simplicial complex X with complete (k − 1)-skeleton.

We take T = γ(L↑k−1(X) − Dk−1(X)) for some γ ∈ R that will be chosen later. Clearly T satisﬁes the conditions required by (11). Then

λmax(L↓k−1 + T) ≤ λmax(L↓k−1 + γL↑k−1(X)) + max

(−γ deg(F)).

F∈Xk−1

We assume that X has complete (k − 1)-skeleton, so we have L↓k−1 = L↓k−1(X) and L↓k−1L↑k−1(X) = 0. Let us denote by Λ the set of non zero eigenvalues of L↑k−1(X). Then, the eigenvalues of the matrix L↓k−1+γL↑k−1(X) are: n, associated to the eigenspace Bk−1, and γλ, for λ ∈ Λ, corresponding to eigenvectors in Bk−1. For γ = λ n

max(L↑k−1(X)), we have λmax(L↓k−1 + γL↑k−1(X)) = n and we get:

degmin(X) λmax(L↑k−1(X))

α(X) ≤ ϑk(X) ≤ n 1 −

.

We note that, if X is regular, i.e., if deg(F) is a constant number for F ∈ Vk , then this upper bound is the exact analog of the ratio bound for graphs (6).

We have just seen that, in the case of a k-complex with complete (k − 1)-skeleton, ϑk(X) is an upper bound of the independence number of X which is as least as good as the bound (2). The case of complexes with noncomplete (k − 1)-skeleton turns out to be more tricky; indeed, in some cases ϑk(X) provides a good bound of α(X), even a sharp one, and beats the bound (2) given by Golubev, while in other cases, Golubev’s bound is better. We provide examples illustrating this situation in the next section, where we explicitly work out the computation of ϑ2(X) for certain families of 2-dimensional complexes. This will also yield counterexamples for certain properties of the theta number related to the chromatic number that we might expect (see Section 7). It will also be interesting to observe the prominent role plaed by the eigenvalues and eigenspaces of the Laplacian operators in these examples .

6. THE THETA NUMBER OF CERTAIN FAMILIES OF 2-COMPLEXES

- 6.1. The complete tripartite 2-complex. To deﬁne this complex, we let n = 3m and partition V = [n] into three subsets A, B, C of equal size m. As 2-dimensional faces we select all triangles with exactly one vertex in each of these subsets; as 1-dimensional faces all edges with at most one vertex in each of these subsets. A natural notation for this complex is Km,m,m2 . It is clear that α(Km,m,m2 ) = 2m because A ∪ B is a maximal independent set with 2m vertices. We will show that ϑ2(Km,m,m2 ) = 2m.


With the notations of (2), d0 = 2m, d1 = m, µ0 = 3m, µ1 = 3m and the bound in (2) equals (7m − 1)/3, so this is an example where the theta number beats Golubev’s bound.

We will also show that, for the complementary complex Km,m,m2 , we have ϑ2(Km,m,m2 ) =

- 3 = α(Km,m,m2 ). This complex has a complete 1-skeleton with d1 = 2m − 2 and µ1 = 3m, so Golubev’s bound (2) equals (m + 2), which is not tight.


### Proposition 6.1. We have ϑ2(Km,m,m2 ) = 2m and ϑ2(Km,m,m2 ) = 3.

Proof. To keep notations light we use the generic notation X for X = Km,m,m2 throughout the proof. We will verify that ϑ2(X) = 2m, by constructing a suitable matrix T feasible for

- (11). The matrix T will be constructed from the projection matrices associated to certain


eigenspaces of L↑1(X) and L↓1(X).

We denote by A × B the set of edges connecting one vertex in A and one vertex in B, and similarly for the other kinds of edges. So, X1 = (A × B) ∪ (B × C) ∪ (C × A). We choose the orientations of the triangular faces and of the edges of X following the rule A → B → C → A; this way, [G : F] = +1 for all G ∈ X2 and F ∈ X1.

It turns out that the up-Laplacian L↑1(X) has three non zero eigenvalues, 3m, 2m and m, respectively with multiplicity 1, 3(m − 1), and 3(m − 1)2. We will need the projection matrices P3↑m and P2↑m associated to the eigenvalues 3m and 2m.

The all-one vector is clearly an eigenvector of L↑1(X) for the eigenvalue 3m, so P3↑m = J3m2/(3m2). The space VA = { a∈A xa(1a×B + 1a×C) : a∈A xa = 0} is easily seen to be an eigenspace of L↑1(X) for the eigenvalue 2m. Similarly, we have two other (m − 1)-dimensional eigenspaces VB and VC, and these spaces are pairwise orthogonal. In order to express the projection matrix P2↑m associated to the sum of these spaces, we introduce the following notation: for (F,F ) ∈ X12, we denote F ∼ F if F and F both belong to A × B (respectively to B × C, C × A). Then,



2(m − 1) if F = F −2 if F ∼ F and F ∩ F = ∅ (m − 2) if F ∼ F and F ∩ F = ∅,F = F



- 1

- 2m2 ·


(P2↑m)F,F =

−1 if F  ∼ F and F ∩ F = ∅ (m − 1) if F  ∼ F and F ∩ F = ∅



The down Laplacian L↓1(X) has two non zero eigenvalues: 3m with multiplicity 2 and 2m with multiplicity 3(m − 1). The vector space {γ1A×B + α1B×C + β1A×C : α+β+γ = 0} is a two-dimensional space of eigenvectors for L↓1(X) and for the eigenvalue 3m, and the corresponding projection matrix P3↓m is given by:

2 if F ∼ F −1 otherwise.

1 3m2 ·

(P3↓m)F,F =

So far the matrices that we have deﬁned are indexed by X1 = (A×B)∪(B×C)∪(A×

C). We now will consider matrices indexed by the whole set V2 , therefore we extend the matrices introduced above by adding zero rows and columns for the indices not belonging

to X1 (we keep the same notation for the enlarged matrices). We are now ready to deﬁne the matrix T that will do the job for ϑ2(X):

Lemma 6.2. With the previous notations, let

T = 2m(P3↑m + P2↑m + P3↓m) − L↓1(X). This matrix satisﬁes the following properties:

- (1) TF,F = 0 for all F ∈ V2
- (2) TF,F = 0 for all F,F such that F ∩ F = ∅ and F ∪ F ∈ / X2
- (3) 2mI − L↓1 − T 0.


Proof. Properties (1) and (2) follow by direct veriﬁcation. In order to prove (3), we write L↓1 +T = U +V +W where U = 2m(P3↑m+P2↑m), V = 2mP3↓m and W = L↓1(X)−L↓1, and make the remark that the product of any two of these matrices is zero. Indeed, for U,V and for U,W it follows immediately from the property that the product of up and down Laplacians is zero; for V,W, it is due to the fact that the image of P3↓m is an eigenspace for the eigenvalue 3m not only for L↓1(X) but also for L↓1. So, we need to prove that 2mI−U, 2mI − V and 2mI − W are positive semideﬁnite. For the ﬁrst two it is obvious because 2mI−U = 2m(I−P3↑m −P2↑m) and 2mI−V = 2m(I−P3↓m). So now the only missing piece is a proof that 2mI − (L↓1 − L↓1(X)) 0.

For this, we arrange the elements of V2 so that those in X1 = (A × B) ∪ (B × C) ∪ (C × A) come before those in (A × A) ∪ (B × B) ∪ (C × C), and we accordingly write L↓1 by blocks:

L↓1(X) M MT N

L↓1 =

. We want to prove that

2mI −M −MT 2mI − N

0.

By the Schur complement lemma, this is equivalent to 2mI − N − (2m)−1MTM 0. A direct computation shows that MTM = 2mN, so all boils down to mI−N 0, which is indeed true because N is a block-diagonal matrix with three blocks equal to L↓1(Km2 ).

Now, we turn our attention to Km,m,m2 = X. In order to prove that ϑ2(X) = 3, we will use the primal formulation (8) and apply a symmetry argument. In the next section we will see a second, simpler, proof, using chromatic numbers, see Example 7.6.

With the previous notations, a feasible matrix Y must be of the form:

Y =

Y1 0 0 τI

where Y1 is supported on the diagonal and on the triangles that belong to X2, i.e., the triangles with one vertex in each of A, B, C. It is clear that the automorphism group of

- X permutes transitively the elements of X2 and of X1, and that, by convexity, (8) has a


symmetric solution. So, without loss of generality, we can assume that Y1 = βL↑1(X)+γI. Restricting the semideﬁnite program on this set of matrices leads to a linear program in the variables β, γ, τ that can be easily solved and leads to the optimal value 3. We skip the details here.

We note that this approach would not work for ϑ2(X) because X2 has two orbits: the triangles that are fully contained in one of the subsets A, B, C and the ones that have two vertices in one of these sets and one vertex in another one.

- 6.2. The complete bipartite 2-complex. Now n = 2m and V = [n] is partitioned in two subsets A, B, of equal size m. As 2-dimensional faces we select the triangles that meet both sets A and B, thus having two vertices in one of the parts and the third vertex in the


other. We denote this complex by Km,m2 . It is clear that α(Km,m2 ) = m since A is an independent set with m vertices. This complex has a complete 1-skeleton and d1 = m,

µ1 = 2m so the bound (3) equals m, showing that ϑ2(Km,m2 ) = m and that the theta number agrees with Golubev’s bound.

For the complementary complex Km,m2 , which is nothing else than the disjoint union of two complete complexes Km2 , we have α(Km,m2 ) = 4. Golubev’s bound is twice the value corresponding to Km2 , thus 4, and it is sharp again. As we will see know, ϑ2(Km,m2 ) is much larger:

- Proposition 6.3. We have ϑ2(Km,m2 ) = m and ϑ2(Km,m2 ) = 8mm+1−4.


Proof. We let X = Km,m2 . To compute ϑ2(X), we again apply the symmetry principle, like in the case of the complement of the tripartite complex. The automorphism group of

Km,m2 has two orbits in X1 = V2 : the set X1in of edges contained in A or in B, having degree m, and the set X1out of ’crossing’ edges, with degree 2(m − 1). It acts transitively on the 2-faces. So without loss of generality a feasible matrix Y of the primal formulation of ϑ2(X) can be assumed to be

Y = βL↑1(X) + γIout + τIin where Iout and Iin denote the 0 − 1 diagonal matrices associated to respectively X1out and X1in. The expressions of I,Y and of L↓1,Y are linear in the variables β,γ,τ, but the condition that Y is positive semideﬁnite is slightly more complicated because L↑1(X) does not commute with Iout and Iin. In fact, this condition leads to quadratic constraints, as it will become clear if we write the matrices by blocks according to V2 = X1in ∪ X1out. It is easy to verify that

mI −M −MT 2mI − N

L↑1(X) =

, MTM = mN − 2J

and that N has two non zero eigenvalues: 2m, with multiplicity 1 and eigenvector the allone vector, and m, with multiplicity 2(m − 1). Then, by the Schur complement lemma, the condition

(mβ + τ)I −βM βMT (2mβ + γ)I − βN

βL↑1(X) + γIout + τIin =

0

leads to quadratic inequalities. It is a bit technical but not difﬁcult to see that an optimal solution satisﬁes γ = τ, and ﬁnally that it is

Y = −1 m2(m + 1)

2 m(m + 1)

L↑1(X) +

## I,

leading to the optimal value L↓1,Y = (8m − 4)/(m + 1).

7. CHROMATIC NUMBERS

Let us ﬁrst review the case of graphs. For a graph G, the clique number ω(G) = α(G) and the chromatic number χ(G) are related by the obvious inequality α(G) ≤ χ(G), and the theta number ϑ(G) lies in between these numbers ([32, Lemma 3, Corollary 3]):

- (12) α(G) ≤ ϑ(G) ≤ χ(G).


Moreover, the inequality ϑ(G) ≤ χ(G) is always at least as strong as the inequality n/ϑ(G) ≤ χ(G); indeed, we know that n ≤ ϑ(G)ϑ(G) from [32, Corollary 2].

Let us consider the situation for pure k-dimensional simplicial complexes. By analogy with graphs, the chromatic number χ(X) of a complex X, is usually deﬁned to be the least number of colors needed to color the vertices of X such that no k-face is monochromatic.

We remark that for the complete k-complex Knk, the color classes of an admissible coloring cannot have more than k elements, and consequently that χ(Knk) = n/k . So, for all k-dimensional complexes X, we have α(X) ≤ kχ(X). Given that we have deﬁned a generalization of the theta number to k-complexes, that satisﬁes α(X) ≤ ϑk(X), it is natural to wonder if the inequality

### (13) ϑk(X) ≤ kχ(X).

is also satisﬁed. Unfortunately, this is not true in general. Indeed, from the results of Section 6, one can see that (13) is satisﬁed for the complete tripartite complex and for its complement, but fails for the complete bipartite complex Km,m2 , for which ϑ2(Km,m2 ) = (8m − 4)/(m + 1) (Proposition 6.3) while χ(Km,m2 ) = 2.

Let us now see if we can modify the deﬁnition of the chromatic number of a simplicial complex, so that it ﬁts better with our theta number. To achieve this, we will adapt the concept of graph homomorphisms to simplicial complexes. Indeed, a nice way to understand the notions of chromatic and clique numbers of graphs is through their connection to graph homomorphisms, as we will recall now.

A homomorphism f from a graph G to a graph G is a mapping from the vertices of G to the vertices of G that sends an edge of G to an edge of G . Then, the clique number and the chromatic number have the following interpretations: the clique number ω(G) is the largest number such that there is a homomorphism from the complete graph K to G, and similarly χ(G) is the smallest number such that there is a homomorphism from G to K . Moreover, one can prove that, if there is a homomorphism from G to G , then ϑ(G) ≤ ϑ(G ). The combination of these properties immediately leads to (12).

In order to follow a similar approach for simplicial complexes, we introduce an ad-hoc notion of homomorphism.

Deﬁnition 7.1. Let X and X be two pure k-dimensional simplicial complexes. A homomorphism f from X to X is a mapping f : Xk−1 → X k−1 with the following property: There exist orientations of X and X such that for every H ∈ Xk, there is H ∈ X k such that

- (1) {f(F) : F ∈ Xk−1, F ⊂ H} = {F ∈ X k−1 : F ⊂ H },
- (2) [H : f(F)] = [H : F] for all F ∈ Xk−1 with F ⊂ H.


We note that this deﬁnition coincides in dimension 1 with the usual notion of a graph homomorphism as one can always ﬁnd suitable orientations.

Remark 7.2. In this deﬁnition, it is important to understand that a homomorphism f may not necessarily be induced by a global mapping f0 between the vertices, i.e., it may be the case that there is no mapping f0 : X0 → X 0 such that f(F) = f0(F) for all F ∈ Xk−1. As an example consider the 2-dimensional complex X depicted in Figure 1.

Furthermore, condition (2) is not automatically fulﬁlled. The 2-dimensional complex X depicted in Figure 2 possesses a map f : X1 → (K32)1 satisfying condition (1) but there is no homomorphism from X to K32.

- Proposition 7.3. Let X and X be two pure k-dimensional simplicial complexes, and let f be a homomorphism from X to X . Then,


#### (14) ϑk(X) ≤ ϑk(X ). Proof. Our strategy will be to start with an optimal solution Y of the primal formulation

(8) of ϑk(X), from which we construct a matrix Y , feasible for ϑk(X ), and having the same objective value as Y .

K32

X

X

FIGURE 1. The homomorphism of X to K32 is not induced by a vertex map.

?

K32

X

X

FIGURE 2. A complex X with no homomorphism to K32

So, let Y be primal optimal for the semideﬁnite program deﬁning ϑk(X). We remark that, if F ∈/ Xk−1, then, for all F = F, F ∪ F ∈ / Xk, and so YF,F = 0. As a consequence, by the optimality of Y , we have YF,F = 0.

For (K,K ) ∈ Xk2−1, we set

Y K,K =

YF,F

(F,F )∈Xk2−1 f(F)=K, f(F )=K

where the sum is zero if K or K does not belong to the image of f. We have trace(Y ) = K∈(V

### YF,F = trace(Y ).

### ) Y K,K = F∈X

k−1

k

By the property 1) of homomorphisms, if K = K and K ∪K is not an element of X k, and if K = f(F) and K = f(F ), then F ∪ F cannot belong to Xk, and so YF,F = 0. So, we have that Y K,K = 0.

Thanks to property 2), if K ∪K ∈ X k and K ∪K = K ∪K†, the required condition that K,K Y K,K = K ,K†Y K ,K† holds. So, we have proved that Y is primal feasible for ϑk(X ).

It remains to analyze the objective value L↓k−1,Y . We have

L↓k−1,Y = k trace(Y ) +

K,K : K∪K ∈X k

K,K Y K,K .

But

K,K Y K,K =

YF,F

K,K

(F,F )∈Xk2−1 f(F)=K, f(F )=K

K,K K∪K ∈X k

K,K K∪K ∈X k

=

F,F YF,F

(F,F )∈Xk2−1 F∪F ∈Xk

where in the last equality we ignore the terms corresponding to F ∪F ∈ / Xk because they are equal to zero, and we apply the property 2). It follows that L↓k−1,Y = L↓k−1,Y .

Deﬁnition 7.4. Let X be a pure k-dimensional simplicial complex. Let χk(X) denote the smallest number such that there exists a homomorphism from X to the complete k-complex Kk .

It is not hard to see that χk(X) ≤ χ(X1) holds for any pure simplicial complex X as a vertex coloring with colors that is a proper graph coloring for X1 gives rise to a homomorphism from X to Kk . The complex X depicted in Figure 1 serves as an example that the three notions of chromatic numbers considered here differ. It has χ2(X) = 3, χ(X) = 2 and χ(X1) = 4.

- Proposition 7.5. We have ϑk(X) ≤ χk(X).


Proof. If there is f : X → Kk then applying (14) leads to ϑk(X) ≤ ϑk(Kk ) = (see Remark 5.4).

Example 7.6. Consider the complex X = Km,m,m2 deﬁned in Section 6. Clearly, χ2(X) = χ(X1) = 3, so we have 3 = α(X) ≤ ϑ2(X) ≤ χ2(X) = 3 and hence ϑ2(X) = 3.

A k-dimensional subcomplex C of a pure k-dimensional simplicial complex X is a connected component of X if for every (k−1)-face F of C any k-face of X that contains F is also in C. Note that this condition does not need to hold for lower dimensional simplices, so two distinct connected components can, e.g., share a common vertex. Further observe that the connected components of X correspond to the connected components of the graph that has the k-faces of X as vertices with two vertices forming an edge if the correponding k-faces intersect in a common (k − 1)-face.

As different connected components do not share (k −1)-faces, the inequality χk(X) ≤ χ(X1) can actually be extended to the connected components of X.

- Proposition 7.7. Let C be the collection of connected components of X. Then


χk(X) ≤ max C∈C

χ(C1).

It is well-known that a d-regular graph G has a bipartite connected component if and only if the largest eigenvalue of the Laplacian is 2d. In [23] Horak and Jost present a combinatorial criterion that can be considered as a higher-dimensional analog of this: They

show that for a d-regular k-complex X the largest eigenvalue of the Laplacian L↑k−1(X) is (k + 1)d if and only if there is a connected component C of X and an orientation of the

k-faces of X such that [H : F] = [H : F] for all F ∈ Ck−1, F ⊂ H,H . Note that for a connected graph the existence of such an orientation is equivalent to bipartiteness.

If a k-dimensional simplicial complex X has chromatic number χk(X) = k + 1, this guarantees the existence of such an orientation. Hence, we have the following observation.

- Proposition 7.8. Let X be a d-regular k-dimensional simplicial complex. If χk(X) = k + 1, then the maximal eigenvalue of the up-Laplacian L↑k−1 is (k + 1)d.


We remark that these results extend to arbitrary complexes for a normalized version of the Laplacian that we do not study here.

8. A HIERARCHY OF SEMIDEFINITE RELAXATIONS FOR THE INDEPENDENCE NUMBER OF A k-SIMPLICIAL COMPLEX

In this section, X is again a pure k-dimensional simplicial complex. We consider a straightforward generalization of ϑk(X) that leads to higher order theta numbers ϑ (X) for

> k. We will see that all these numbers provide upper bounds of α(X), until = α(X),

where ϑα(X) = α(X). Finally, we will modify this sequence of theta numbers in order to get a decreasing sequence.

It will be convenient to denote by Indi the set of independent sets of dimension i. We make the remark that Ind := Ind−1 ∪··· ∪ Indα(X)−1 is a simplicial complex, the independence complex of X, and that it has complete (k−1)-skeleton, i.e., Indk−1 = Vk . For > k, the matrices involved in the program deﬁning ϑ (X) are indexed by Ind −1. We deﬁne, for k ≤ ≤ α(X):

- (15) ϑ (X) = sup L↓ −1(Ind),Y : Y ∈ RInd −1 ×Ind −1, Y 0, I,Y = 1,

YF,F = 0 if F ∪ F ∈ +1 V \ Ind , YF,F = 0 if |F ∪ F | ≥ + 2,

F,F YF,F = F ,F†YF ,F† if F ∪ F = F ∪ F† and its dual formulation:

- (16)


ϑ (X) = inf λmax(Z) : Z = L↓ −1(Ind) + T, TF,F = 0 for all F ∈ Ind −1, F∪F =H F,F TF,F = 0 if H ∈ Ind

The above deﬁnition matches for = k with that of ϑk(X). Both primal and dual programs are strictly feasible: Y = I/ I,I and respectively T = 0 give rise to strictly feasible solutions. We note that, if = α(X), the feasible matrices of the primal program are diagonal matrices and hence ϑ (X) = = α(X). We have

- Proposition 8.1. α(X) ≤ ϑ (X).


Proof. The same proof as the one of Proposition 5.2 works. For an independent set S such that |S| ≥ , we deﬁne Y S ∈ RInd −1 ×Ind −1 by

0 if F ∪ F S (L↓ −1(Ind))F,F otherwise.

(Y S)F,F =

It is then easy to verify, as every subset of an independent set S is also an independent set, that −1 |S| −1Y S is feasible for the primal program (15) and that its objective value is equal to |S|.

However, it is not clear that the sequence (ϑ (X))k≤ ≤α(X) is decreasing, because the constraints on the -sets involved in ϑ −1(X) do not occur explicitly in ϑ (X). We now deﬁne a variant of ϑ (X) that provides a decreasing sequence of upper bounds of α(X).

To start with, we note that, if a matrix Y is feasible for (15), then the value of F,F YF,F

for (F,F ) such that |F ∪F | = +1 only depends on F ∪F . So, we can associate to Y a function y ∈ RInd such that F,F YF,F = y(H) if H = F ∪F . If we extend y to Ind −1 by y(F) := YF,F, we see that y encodes every nonzero entry of Y . Said differently, we have a one to one correspondence between RInd −1 ∪Ind and the set

YF,F = 0 if F ∪ F ∈ +1 V \ Ind , YF,F = 0 if |F ∪ F | ≥ + 2,

- Y −1 = Y ∈ RInd −1 ×Ind −1 :


F,F YF,F = H,H YH,H if F ∪ F = H ∪ H

We record for later use that, if y ∈ RInd −1 ∪Ind corresponds to Y ∈ Y as above, then

- (17) I,Y = F∈Ind −1

y(F)

and

- (18) L↓ −1(Ind),Y = F∈Ind −1

y(F) + ( + 1)

H∈Ind

y(H).

Now, we introduce, for ≥ 2, a map τ −1 : Y −1 → Y −2. It will be more convenient

to deﬁne τ −1 on the corresponding functions y ∈ RInd −1 ∪Ind , in the following way: let τ −1 : RInd −1 ∪Ind → RInd −2 ∪Ind −1

y  → τ −1(y) = z where

z(K) = 1 F∈Ind

−1 :K⊂F y(F) if K ∈ Ind −2

z(F) = ( 1 −1)y(F) + −11 H∈Ind :F⊂H y(H) if F ∈ Ind −1 We are now in the position to deﬁne our strengthening of ϑ (X): Let

- (19)

ϑˆ (X) = sup L↓ −1(Ind),Y : Y ∈ RInd −1 ×Ind −1, Y 0, I,Y = 1, τi ◦ τi+1 ◦ ··· ◦ τ −1(Y ) 0 for all i = 1,...,  − 1, YF,F = 0 if F ∪ F ∈ +1 V \ Ind , YF,F = 0 if |F ∪ F | ≥ + 2,

F,F YF,F = F ,F†YF ,F† if F ∪ F = F ∪ F† .

- Theorem 8.2. The numbers ϑˆ (X), k ≤ ≤ α(X), satisfy:


- (1) ϑˆ (X) ≤ ϑ (X)
- (2) α(X) = ϑˆα(X)(X) ≤ ϑˆα(X)−1(X) ≤ ··· ≤ ϑˆk(X).


Proof. That ϑˆ (X) ≤ ϑ (X) is clear since we have only added constraints on Y in the deﬁnition of ϑˆ (X).

Let S be an independent set, with |S| ≥ . Let, like in the proof of Proposition 8.1, Y S −1 ∈ RInd −1 ×Ind −1 be deﬁned by:

- (20) (Y S −1)F,F =


0 if F ∪ F S (L↓ −1(Ind))F,F otherwise.

The element yS −1 ∈ RInd −1 ∪Ind corresponding to Y S −1 is given by: yS −1(F) = if F ⊂ S, yS −1(H) = 1 if H ⊂ S, and otherwise yS −1 takes the value 0. We will need the following lemma:

## Lemma 8.3. We have

τ −1(yS −1) = |S| − + 1

yS −2

− 1

for yS −1 as deﬁned in (20). Proof. Let z := τ −1(yS −1). Let K ∈ Ind −2. Every subset of S is independent so the number of F ∈ Ind −1 such that K ⊂ F ⊂ S is |S| − + 1. So,

1

yS −1(F) = |S| − + 1.

z(K) =

F∈Ind −1 : K⊂F

Now let F ∈ Ind −1. It is clear that, if F is not contained in S, z(F) = 0. If F ⊂ S,

1 − 1 H∈Ind :F⊂H⊂S

1 ( − 1)

+

1

z(F) =

(|S| − ) = |S| − + 1 − 1

1 − 1

1 − 1

=

+

.

Lemma 8.3 shows that τ (Y S −1) is positive semideﬁnite, and so, iteratively, that τi ◦ τi+1 ◦···◦τ −1(Y S −1) is positive semideﬁnite for every i ≤ −1. We conclude that Y S −1 (after a suitable rescaling) is feasible for ϑˆ (X), and consequently that α(X) ≤ ϑˆ (X). We have already remarked that ϑα(X) = α(X) so also ϑˆα(X) = α(X).

It remains to prove that the sequence of ϑˆ is decreasing. For this, we start from an optimal solution Y of ϑˆ , and we show that Z := τ −1(Y ) is feasible for ϑˆ −1 and that

L↓ −1(Ind),Y = L↓ −2(Ind),Z .

It is clear that Z ∈ Y −2 and that Z is positive semideﬁnite, as well as τi ◦ τi+1 ◦ ··· ◦ τ −2(Z) 0 for all i ≤ − 2. That I,Z = 1 follows easily from (17) and from the deﬁnition of τ −1. It remains to take care of the objective value. Applying (18),

L↓ −2(Ind),Z = ( − 1)

z(K) + ( − 1)

z(F)

K∈Ind −2

F∈Ind −1

1 ( − 1)

1 − 1 H :F⊂H

1

y(F) + ( − 1)

= ( − 1)

y(F) +

y(H)

F : K⊂F

F

K

where in the sums we restrict to elements in Ind. Taking account of the fact that every subset of an independent set is also an independent set, we obtain

L↓ −2(Ind),Z =

y(F) + ( + 1)

F∈Ind −1

H∈Ind

y(H) = L↓ −1(Ind),Y .

9. THETA NUMBERS OF RANDOM COMPLEXES

A random model Xk(n,p) for simplicial complexes of arbitrary ﬁxed dimension k was introduced by Linial and Meshulam [31] as a higher dimensional analog of the Erd¨osR´enyi model G(n,p) for random graphs. It has vertex set [n] = {1,...,n}, complete

(k − 1)-skeleton, and each element of k [+1n] is added as a k-dimensional face of Xk(n,p) independently with probability p. Here p = p(n) is a function of n, and we let q := 1 − p. In this section we analyze the theta number of Xk(n,p) for ’dense’ complexes, i.e., for p in the range [c0 log(n)/n,1 − c0 log(n)/n].

The study of the theta number of random graphs G(n,p) was initiated by Juh´asz in [24] who proved that, in the case of constant probability p, ϑ(G(n,p)) = Θ( nq/p) holds with probability tending to 1. In subsequent works, the range of probabilities for which Juh´asz’ result holds was extended, until in [6], Coja-Oghlan was able to cover c0/n ≤ p ≤ 1−c0/n for some sufﬁciently large constant c0.

We will restrict ourselves to the range c0 log(n)/n ≤ p ≤ 1 − c0 log(n)/n because we will need the following estimates:

- Theorem 9.1 ([16, 22]). Let A denote the adjacency matrix of G(n,p). For every c > 0 there exists c0 > 0,c > 0,c > 0 such that, if c0 log(n)/n ≤ p ≤ 1 − c0 log(n)/n,


- (21) λmax(pJ − A) ≤ c pq(n − 1) and

- (22) |λmin(A)| ≤ c pq(n − 1). with probability at least equal to 1 − n−c.

With the above, it is rather straightforward to obtain:

- Theorem 9.2. For every c > 0 there exists c0 > 0,c1 > 0,c2 > 0 such that, if c0 log(n)/n ≤ p ≤ 1 − c0 log(n)/n,

(23) c1 (n − 1)q/p ≤ ϑ(G(n,p)) ≤ c2 (n − 1)q/p. with probability at least equal to 1 − n−c.

Indeed, following the method of Juh´asz, the upper bound is obtained via the dual formulation for the theta number (5) and the matrix Z = J − A/p, where A is the adjacency matrix of G(n,p), while the lower bound follows from the choice Y = Y / I,Y in the primal formulation (4), where Y = A − λmin(A)I, A being the adjacency matrix of the complementary graph of G(n,p).

9.1. The theta number of Xk(n,p). We will establish the following similar result for random simplicial complexes Xk(n,p):

- Theorem 9.3. For every k ≥ 1 and c > 0, there exists c0 > 0,c1 > 0,c2 > 0 such that, if c0 log(n)/n ≤ p ≤ 1 − c0 log(n)/n,




c1 (n − k)q/p ≤ ϑk(Xk(n,p)) ≤ c2 (n − k)q/p. with probability at least equal to 1 − n−c.

For comparison, the independence number of Xk(n,p) is of the order (log(nkp)/p)1/k (see [28]). In the range c0 log(n)/n ≤ p ≤ 1 − c0 log(n)/n, the eigenvalues of the adjacency matrix of Xk(n,p) have been studied in [21]. We will closely follow the methods developed in [21], in particular the role played by the so-called links of X, an

idea going back to the work of Garland [17]. By deﬁnition, for a k-dimensional simplicial complex X and a (k − 2)-face K of X, the link lkX(K) is the graph with vertices {v ∈ V : K ∪ {v} ∈ Xk−1}, and edges {{v,w} : K ∪ {v,w} ∈ Xk}. In view of the proof of Theorem 9.3, we will ﬁrst establish a relationship between the theta number of a simplicial complex and that of its links.

- Proposition 9.4. Let X be a k-dimensional simplicial complex with complete (k − 1)skeleton. Then


- (24) ϑk(X) ≤ k max K∈Xk−2

ϑ(lkX(K)).

Proof. Let K ∈ Xk−2. For a matrix Y ∈ R(V

k

)×(V

k

), we introduce its localization at K denoted YK and deﬁned by:

(YK)F,F =

YF,F if K ⊂ F ∩ F 0 otherwise.

Let ρK ∈ R(V

k

)×(V

k

) denote the diagonal matrix with [F : K] as diagonal entries. Then we observe that

- (25) L↓k−1 = K∈Xk−2

ρKJKρK.

and that, if YF,F = 0 for all (F,F ) such that |F ∪ F | ≥ k + 2,

- (26) Y = K∈Xk−2


YK − (k − 1)diag(Y ).

Now let Y be an optimal solution of (8). Taking account of (25) and (26),

ϑk(X) = L↓k−1,Y =

K

ρKJKρK,

K

YK − (k − 1) L↓k−1,diag(Y )

If K = K , we have

=

K,K

ρKJKρK,YK − k(k − 1).

ρKJKρK,YK =

YF,F if K ∪ K = F 0 otherwise

so, since trace(Y ) = 1,

ϑk(X) =

ρKJKρK,YK =

JK,ρKYKρK .

K

K

Now, the crucial observation is that the matrix ρKYKρK gives rise to a feasible matrix of the semideﬁnite program (4) deﬁning the theta number of lkX(K). Indeed, let ZK be the matrix indexed by V \ K and deﬁned by (ZK)v,w = (ρKYKρK)K∪{v},K∪{w}. This matrix inherits some properties of Y : The matrix ZK is positive semideﬁnite, the entries of ZK associated to edges of lkX(K) are equal to 0. With obvious notations, we have

JK,ρKYKρK = J,ZK and I,ZK = I,YK so we obtain ϑk(X) ≤

I,YK ϑ(lkX(K)).

K

We have K I,YK = k I,Y = k so the announced inequality follows immediately.

Proof of Theorem 9.3. For the upper bound, we apply Proposition 9.4. The link lkX(K) of a (k − 2)-face K in a random complex X = Xk(n,p) is an Erd¨os-Renyi random graph on V \K with the same probability p. We can thus apply Theorem (9.2) and a union bound to obtain the result. We note that, since the number of such faces is of the order of nk−1, for the probability of the bad event to be, say, less than n−c we need to apply Theorem (9.2) for the larger value c + k − 1 instead of c, explaining the need for an arbitrary large power of n in the convergence speed of probabilities.

In order to ﬁnd a lower bound of ϑk(X), we consider the matrix Y = A − λmin(A)I where A denotes the adjacency matrix of the complementary k-complex X. The feasibility conditions of (8) are fulﬁlled by Y except for the normalization condition I,Y = 1. We

have I,Y = − nk λmin(A). Moreover, L↓k−1,Y = k(k + 1)|Xk| − k nk λmin(A), so

(k + 1)|Xk| − nk λmin(A)

ϑk(X) ≥ k 1 +

.

The number |Xk| of k-faces of X = Xk(n,q) is a random variable binomially distributed in [ k+1 n ] with probability q. Hence, by a straightforward application of a Chernoff bound, for every c > 0, |Xk| is at least of the order k+1 n q with probability at least 1 − n−c. It remains to upper bound |λmin(A)|. For this, we apply the localization procedure that we have already encountered in the proof of Proposition 9.4:

### A =

### AK.

K∈Xk−2

Then, for every x = (xF)F∈(V

), if xK denotes the vector obtained from x by setting to 0 the coordinates of x associated to faces F not containing K,

k

Ax,x =

AKx,x =

AKxK,xK .

K

K

The matrix AK has the same spectrum as ρKAKρK. The latter is identical to the adjacency matrix Alk

X(K) of the graph lkX(K) on the entries indexed by {F = K∪{v}, v ∈ V \K}, and zero elsewhere. So, its non-zero spectrum is that of Alk

X(K) and hence: Ax,x ≥

X(K)) xK,xK .

λmin(Alk

K

The links lkX(K) are random graphs G(n−k+1,q) so, applying (22) and a union bound, we ﬁnd that, with probability at least equal to 1 − n−c, for a large enough constant c ,

Ax,x ≥ −c pq(n − k)

xK,xK = −c k pq(n − k) x,x .

K

We have obtained the desired upper bound |λmin(A)| ≤ c pq(n − k). Putting everything together, we obtain the announced lower bound for ϑk(X).

9.2. The hierarchy of theta numbers of G(n,p). In this last subsection, we restrict ourselves to the case of random graphs G(n,p) and analyze the hierarchy of theta numbers ϑ (G(n,p)) for constant values of . The restriction to random graphs, i.e., random complexes of dimension 1, is purely for simplicity. The assumption of constant , however, is essential. Analyzing the complete hierarchy ϑˆ (X) of a random complex X for nonconstant appears to be a difﬁcult task. It would be interesting to know for which values of the theta number ϑ (G(n,p)) is close to the independence number. Unfortunately, such questions seem to be out of the reach of the methods we apply here.

Theorem 9.5. For every ≥ 1 and c > 0, there exists c0 > 0,c1 > 0,c2 > 0 such that, if q ≥ c0 log(n)/n and pq −1 ≥ c0 log(n)/n,

c1 nq /p ≤ ϑ (G(n,p)) ≤ c2 nq /p. with probability at least equal to 1 − n−c.

Proof. We will sometimes use the expression with high probability for an inequality that holds with probability at least 1 − n−c for all c > 0, with appropriate constants depending on c.

For an upper bound of ϑ (G(n,p)), we apply

ϑ (G) ≤ max K∈( V

ϑ(lkG(K)).

)

−1

Here, lkG(K) is the graph on VK := {v ∈ V : {v,k} ∈/ E(G(n,p)) for all k ∈ K} with edges {v,w} if K ∪ {v,w} ∈ +1 V \ Ind . If K is independent, this condition simply means that {v,w} is an edge of G, so lkG(K) is the graph G[VK] induced by G on VK. If G = G(n,p), the number of vertices nK = |VK| is itself a random variable. Since |K| = − 1, nK follows a binomial distribution with parameters (n − + 1) and q −1. For nK to be concentrated around its expected value q −1(n − + 1) we need q −1 ≥ c0 log(n)/n for some c0 > 0.

Assuming nK ≤ cq −1n for some c > 0, we have

### ϑ(G[VK]) ≤ ϑ(G(cq −1n,p))

because G[VK] can be viewed as an induced subgraph of G(cq −1n,p). We would like to apply Theorem 9.2. It requires p and q to be greater that c 0 log(q −1n)/(q −1n) and holds with probability at least 1 − (q −1n)c. All this will be ﬁne if we assume:

### pq −1 ≥ c1 log(n)/n and q ≥ c1 log(n)/n

for a sufﬁciently large c1. With a union bound we obtain with high probability:

### ϑ (G) ≤ c nq /p.

For the lower bound, we consider the matrix Y = A − λmin(A)I where A is the adjacency matrix of the -skeleton of Ind and we apply (15). We obtain

L↓ −1(Ind),Y I,Y

( + 1)|Ind | −λmin(A)|Ind −1 |

ϑ (X) ≥

= 1 +

.

In order to estimate |λmin(A)| we use A = K∈Ind

AK and remark that AK has the same non-zero eigenvalues as the adjacency matrix of the graph lkInd(K), itself being the graph G[VK] induced by G on VK. We have

−2

Ax,x =

AKx,x =

AKxK,xK

K∈Ind −2

K∈Ind −2

≥

λmin(AK) xK,xK

K∈Ind −2

≥ min

λmin(AK)

xK,xK

K∈Ind −2

K∈Ind −2

≥ min

λmin(AK) x,x ,

K∈Ind −2

so

−λmin(A) = |λmin(A)| ≤ · max

|λmin(G[VK])|.

K

Like for the upper bound we have with high probability nK ≤ cq −1n for some c > 0 and thus

### |λmin(G[VK])| ≤ |λmin(G(cq −1n,q))| ≤ c pq n for some c > 0, under the same conditions on p and q.

It remains to deal with the ratio |Ind |/|Ind −1 |. For this we will argue that Ind is almost regular. To be more precise we apply double counting to the set

D = {(A,B) ∈ Ind −1 ×Ind : A ⊂ B}. The number of -subsets of B is + 1 so |D| = ( + 1)|Ind |. For a given A, the number XA of B containing A follows a binomial distribution with parameters n − and q , with expected value q (n − ). With high probability (requires q ≥ clog(n)/n) XA is larger that c q (n − ) and so

c q (n − )

|Ind | |Ind −1 |

≥

.

+ 1

Putting everything together and applying another union bound we obtain

### ϑ (G) ≥ c nq /p.

REFERENCES

- [1] M. Anjos and J.B. Lasserre, Handbook on Semideﬁnite, Conic and Polynomial Optimization, Springer, 2012
- [2] A. Ben-Tal and A. Nemirovski, Lectures on Modern Convex Optimization: Analysis, Algorithms, and Engineering Applications, SIAM, Philadelphia, 2001.
- [3] S. Boyd and L. Vandenberghe Convex Optimization, Cambridge University Press, 2004.
- [4] A.E. Brouwer and W.H. Haemers, Spectra of Graphs, Springer, New York (2012).
- [5] H. Cohn, A. Kumar, S.D. Miller, D. Radchenko, and M.S. Viazovska, The sphere packing problem in dimension 24, preprint, arXiv:1603.06518 [math.NT], 2016, 12pp.
- [6] A. Coja-Oghlan, The Lov´asz number of random graphs, Combinatorics, Probability and Computing 14

(2005), 439-465.

- [7] P.E.B. DeCorte, D. de Laat, and F. Vallentin, Fourier analysis on ﬁnite groups and the Lov´asz theta-number of Cayley graphs , Experimental Mathematics 23 (2014), 146-152.
- [8] P. Delsarte, An algebraic approach to the association schemes of coding theory, Philips Research Repts Suppl. 10, (1973), 1-97.
- [9] D. Dotterrer, T. Kaufman, and U. Wagner, On Expansion and Topological Overlap, preprint, arXiv.math:1506.04558.
- [10] D. Dotterrer, L. Guth, and M. Kahle. 2-complexes with large homological systoles, preprint, arXiv.math:1509.03871.
- [11] A.M. Duval, C.J. Klivans, and J.L. Martin, Simplicial and Cellular Trees, in Recent Trends in Combinatorics, The IMA Volumes in Mathematics and its Applications, Springer (2016), 713–752.
- [12] D. Ellis and E. Friedgut, H. Pilpel, Intersecting families of permutations, Journal of the American Mathematical Society 24 (2011), 649-682.
- [13] D. Ellis, Y. Filmus, and E. Friedgut, Triangle-intersecting families of graphs, Journal of the European Mathematical Society 14 (2012), 841-885
- [14] S. Evra, K. Golubev and A. Lubotzky, Mixing properties and the chromatic number of Ramanujan complexes International Mathematics Research Notices 22 (2015), 11520-11548.
- [15] S. Evra, T. Kaufman, Bounded Degree Cosystolic Expanders of Every Dimension preprint, arXiv.math:1510.00839.
- [16] U. Feige and E. Ofek, Spectral techniques applied to sparse random graphs, Random Structures Algorithms 27 (2) (2005), 251–275.
- [17] H. Garland, p-adic curvature and the cohomology of discrete subgroups of p-adic groups, Annals of Mathematics (2), 97(3) (1973), 375–423.


- [18] B. G¨artner and J. Matouˇsek, Approximation Algorithms and Semideﬁnite Programming, Springer, 2012
- [19] K. Golubev, On the chromatic number of a simplicial complex, to appear in Combinatorica.
- [20] M. Gromov, Singularities, expanders and topology of maps. Part 2: From combinatorics to topology via algebraic isoperimetry, Geometric and Functional Analysis, 20 (2) (2010), 416–526.
- [21] A. Gundert and U. Wagner, On eigenvalues of random complexes, Israel Journal of Mathematics,216 (2)

(2016), 545–582.

- [22] C. Hoffman, M. Kahle, and E. Paquette, Spectral gaps of random graphs and applications to random topology, preprint, arXiv.math:1201.0425.
- [23] D. Horak and J. Jost, Spectra of combinatorial Laplace operators on simplicial complexes, Advances in Mathematics, 244:303 – 336, 2013.
- [24] F. Juh´asz, The aymptotic behaviour of Lov´asz theta function for random graphs, Combinatorica 2 (2) (1982), 153–155.
- [25] M. Kahle, Random simplicial complexes, preprint, arXiv.math:1607.07069.
- [26] G. Kalai, Enumeration of Q-acyclic simplicial complexes, Israel Journal of Mathematics, 45 (1983), 337– 351.
- [27] T. Kaufman, D. Kazhdan and A. Lubotzky, Isoperimetric Inequalities for Ramanujan Complexes and Topological Expanders, Geometric and Functional Analysis, 26 (1) (2016), 250–287.
- [28] M. Krivelevich, B. Sudakov, The chromatic numbers of random hypergraphs, Random Structures Algorithms, 12 (4) (1998), 381–403.
- [29] J.B. Lasserre, An explicit equivalent positive semideﬁnite program for nonlinear 0-1 programs, SIAM J. Optim. 12 (2002), 756769.
- [30] M. Laurent, A comparison of the Sherali-Adams, Lov´asz-Schrijver and Lasserre relaxations for 0 1 programming, Math. Oper. Res. 28 (2003), 470496.
- [31] N. Linial and R. Meshulam, Homological connectivity of random 2-complexes, Combinatorica 26 (4)

(2006), 475–487.

- [32] L. Lov´asz, On the Shannon capacity of a graph, IEEE Transactions on Information Theory 25 (1979), 1–7.
- [33] A. Lubotzky, Ramanujan complexes and high dimensional expanders, Japanese Journal of Mathematics 9

(2) (2014), 137–169.

- [34] A. Lubotzky and R. Meshulam, A Moore bound for simplicial complexes, Bulletin of the London Mathematical Society, 39 (3) (2007), 353–358.
- [35] J. Matou¸sek, M. Tancer and U. Wagner, Hardness of embedding simplicial complexes in Rd, Journal of the European Mathematical Society, 13 (2) (2011), 259-295.
- [36] F.M. de Oliveira Filho and F. Vallentin, Computing upper bounds for packing densities of congruent copies of a convex body, 30 pages, arXiv:1308.4893 [math.MG]
- [37] O. Parzanchevski and R. Rosenthal, Simplicial complexes: Spectrum, homology and random walks, Random Structures Algorithms, 50 (2) (2017), 225–261.
- [38] O. Parzanchevski, R. Rosenthal, and R. J. Tessler, Isoperimetric inequalities in simplicial complexes, Combinatorica, 36 (2) (2016), 195–227.
- [39] L. Vandenberghe and S. Boyd, Semideﬁnite Programming, SIAM Review 38 (1996), pp. 4995.
- [40] M.S. Viazovska, The sphere packing problem in dimension 8, arXiv:1603.04246 [math.NT], 2016, 22pp.


INSTITUT DE MATHEMATIQUES´ DE BORDEAUX, UMR 5251, UNIVERSITE´ DE BORDEAUX, 351 COURS

DE LA LIBERATION´ , 33400 TALENCE, FRANCE. E-mail address: christine.bachoc@u-bordeaux.fr MATHEMATISCHES INSTITUT, UNIVERSITAT¨ ZU KOLN¨ , WEYERTAL 86-90, 50931 KOLN¨ , GERMANY. E-mail address: anna.gundert@uni-koeln.de INSTITUT DE MATHEMATIQUES´ DE BORDEAUX, UMR 5251, UNIVERSITE´ DE BORDEAUX, 351 COURS

DE LA LIBERATION´ , 33400 TALENCE, FRANCE. E-mail address: alberto.passuello@u-bordeaux.fr

