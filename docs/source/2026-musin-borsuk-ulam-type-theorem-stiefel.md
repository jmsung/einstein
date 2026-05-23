---
type: source
kind: paper
title: Borsuk-Ulam type theorem for Stiefel manifolds and orthogonal mass partitions
authors: Oleg R. Musin
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2603.18550v2
source_local: ../raw/2026-musin-borsuk-ulam-type-theorem-stiefel.pdf
topic: general-knowledge
cites:
---

# Borsuk–Ulam type theorem for Stiefel manifolds and orthogonal mass partitions

## arXiv:2603.18550v2[math.AT]16Apr2026

##### Oleg R. Musin

###### Abstract

A generalization of the Borsuk–Ulam theorem to Stiefel manifolds is considered. This theorem is applied to derive bounds on d that guarantee—for a given set of m measures in Rd—the existence of k mutually orthogonal hyperplanes, any n of which partition each of the measures into 2n equal parts. If n = k, the result corresponds to the bound obtained in [11], but with the stronger conclusion that the hyperplanes are mutually orthogonal.

Keywords: Borsuk–Ulam theorem, ham–sandwich theorem, mass partition problem.

### 1 Introduction

In this section, we review and formulate the main results of the present paper. Section

###### 2 presents necessary results concerning equivariant cobordisms and proves Borsuk–Ulamtype theorems for products of spheres and Stiefel manifolds. Section 3 discusses conditions imposed on k hyperplanes in Rd under which any subset of n such hyperplanes partitions each of m measures into 2n equal parts. Section 4 proves the main theorem on orthogonal mass partitions.

#### 1.1 Borsuk–Ulam theorems for spheres and Stiefel manifolds.

In Section 2 we consider Borsuk–Ulam type (BUT) theorems for G–manifolds. In our opinion, the most useful tool for BUT–manifolds is equivariant cobordism theory, which goes back to the work of Conner and Floyd in the early 1960s [7]. In terms of equivariant cobordism theory, we obtained Theorems 1 and 3 in [17], see Theorems 2.1 and 2.2 in this paper. We applied these theorems to prove the BUT–theorem with G = (Z/2)k (Theorem 2.8 ). Here we formulate two Borsuk-Ulam type theorems for the product of spheres and Stiefel manifolds which follow from Theorem 2.8.

Let G = (Z/2)k = Z/2×...×Z/2. The group has k generators (λ1 = (1,0,...,0),...,λk = (0,...,0,1)) of order 2. Then each element q ∈ G can be represented in the form

q = ε1λ1 + ... + εkλk ∈ G, εi ∈ F2, i.e. εi = 0,1.

It is well known that every irreducible linear representation of G is one–dimensional and to every q ∈ G corresponds an irreducible representation ρq : G → Rq, where ρq(λi)(x) = −x if εi = 1 and ρq(λi)(x) = x otherwise. Here x ∈ Rq.

###### = {(v1,...,vk)|vℓ ∈ Si

###### × ... × Si

Let the action of the group (Z/2)k on Si

, ℓ = 1,...,k} be defined for all q = ε1λ1 + ... + εkλk ∈ G as q(v1,...,vk) = ((1 − 2ε1)v1,...,(1 − 2εk)vk).

1

ℓ

k

Let

1 ,...,ai

k+1

P(i1,...,ik) := F2[a1,...,ak]/(ai

1+1

k ). In other words, P(i1,...,ik) is the group ring F2(Ci

1+1 × ... × Ci

k+1), where Cn is a cyclic group of order n.

- Theorem 1.1. Let qℓ = εℓ,1λ1+...+εℓ,kλk, ℓ = 1,...,m, be elements of G = (Z/2)k. Suppose


m

(εℓ,1a1 + ... + εℓ,kak) ̸= 0 in P(i1,...,ik).

ℓ=1

Then for any continuous equivariant mapping f : Si

###### × ... × Si

→ Rmρ = Rq

1

k

the zeros set Zf := f−1(0) is non-empty.

1 ⊕ Rq

2 ⊕ · · · ⊕ Rq

m

- Remark 1. A special case of this theorem was first proved in [17, Cor. 4]. In [3, 4, 6, 9, 11, 14, 20, 25, 27], and many others papers the cohomological theory of the G–index is used. Many results, such as the upper bounds in [14], obtained using this technique can be easily deduced from Theorem 1.1. The proofs then become an algebraic exercise with polynomials over F2 and do not require complex calculations, see Section 4.


The Stiefel manifold Vn,k is the set of all orthonormal k–frame (u1,...,uk) in Rn, i.e. Vn,k := {(u1,...,uk) ∈ (Sn−1)k = Sn1−1 × ... × Snk−1 |ui · uj = 0 for all 1 ≤ i < j ≤ k}

= {(u1,...,uk) ∈ (Sn−1)k |ui · u1 = 0,...,ui · ui−1 = 0 for all 1 < i ≤ k}. This definition yields that the dimension of Vn,k is

n − 1 + n − 2 + ... + n − k = nk − k(k + 1)/2.

- Let G = (Z/2)k with generators λ1,...,λk acting on Vn,k by λj(u1,...,uj,...,uk) = (u1,...,−uj,...,uk), j = 1,...,k.


###### Theorem 1.2. Let qℓ = εℓ,1λ1+...+εℓ,kλk, ℓ = 1,...,m, be elements of G = (Z/2)k. Suppose

m

(εℓ,1a1 + ... + εℓ,kak) ̸= 0 in P(n − 1,...,n − k).

ℓ=1

Then for any continuous equivariant mapping f : Vn,k → Rmρ = Rq

1 ⊕ Rq

the zeros set Zf is non-empty.

2 ⊕ · · · ⊕ Rq

m

- Remark 2. Theorem 1.1 in [6] is a particular case of Theorem 1.2. In this case


###### )n−1 ⊕ · · · ⊕ (Rλ

)n−k.

m = dimVn,k = nk − k(k + 1)/2, Rmρ = (Rλ

1

k

- 1.2 Orthogonal mass partition. The well-known ham–sandwich theorem states:


For every (three–dimensional) sandwich made out of three ingredients there is a planar cut that simultaneously divides each of the ingredients in half, i.e. it can be fairly divided between two guests using a single straight cut.

This theorem was proposed by Steinhaus and proved by Banach, for details see [2]. Stone & Tukey [26] proved the d–dimensional version of the theorem in a more general setting involving measures.

Mass partition theorems are usually stated in one of two settings: discrete or continuous. The continuous versions deal with measures in Rd. In this paper we assume that all measures are finite absolutely continuous with respect to the Lebesgue measure or, see [15, Sec. 3.1], they are finite Borel measures such that every hyperplane has measure 0. (A measure µ on Rd is called finite if 0 < µ(Rd) < ∞.)

We say that a hyperplane H bisects µ (or divides µ in half) if

µ(H+) =

- 1

- 2


µ(Rd),

where H+ denotes one of the half–spaces defines by H. Ham Sandwich Theorem. Let µ1,...,µd be measures on Rd. Then there exists a hyperplane that simultaneously bisects all d measures.

A discrete version of this theorem states as follows, see [15, Theorem 3.1.2]:

Discrete Ham Sandwich Theorem. Let X1,...,Xd be finite sets in Rd. Then there exists a hyperplane that simultaneously bisects X1,...,Xd.

Let ∆(m,k) denote the minimal dimension d of Euclidean space such that for any set of m (finite absolutely continuous) measures in Rd there exist k hyperplanes in Rd that divide

each of the m measures into 2k parts of equal size. There are lower and upper bounds for this number:

2k − 1 k

m ≤ ∆(m,k) ≤ m + (2k−1 − 1)2⌊log

2m⌋ (1.1)

The lower bound was proved in 1996 by Ramos [21], and this upper bound was obtained in 2006 by Mani-Levitska, Vrec´ica, and Zivaljevi´cˇ [14]. The only instance in which lower and upper bounds coincide is in the case when k = 1 or k = 2 and m = 2j − 1, j = 1,2,...

Consider the case when the hyperplanes are mutually orthogonal. For a plane, this fact is well known, see [24, Sec.7]: Pancake theorem. Given one finite area, two–dimensional pancake. Then there exists two perpendicular straight lines that cut the area of the pancake into four equal pieces.

Let ∆∗(m,k) denote the minimal dimension d of Euclidean space such that for any set of m measures in Rd there exist k mutually orthogonal hyperplanes in Rd that divide each of the m measures into 2k parts of equal size. The following theorem generalizes (1.1):

- Theorem 1.3. 2k − 1


k

k − 1 2 ≤ ∆∗(m,k) ≤ m + (2k−1 − 1)2⌊log

2m⌋ (1.2)

m +

The lower and upper bounds in (1.2) coincide in the following two cases:

(i) k = 2, m = 2j − 1, j = 1,2,...; (ii) k = 2, m = 2j − 2, j = 2,3,...; ∆∗(2j − 1,2) = ∆(2j − 1,2) = 3 · 2j−1 − 1, ∆∗(2j − 2,2) = 3 · 2j−1 − 2.

It is clear that ∆∗(m,k) ≥ ∆(m,k), however the upper bounds in (1.2) and (1.1) are the same.

Note that the bound in case (i) is also tight for (1.1). Let’s explain what’s happening. For k = 2 the lower bound in (1.1), b1 = ⌈y⌉, y = 3m/2. In (1.2) we have b2 = ⌈y + 1/2⌉. If

- m is odd, then b1 = b2 = (3m + 1)/2. Actually, Theorem 1.3 is a particular case of a more general theorem. Let ℓ ≥ 1 and


ℓ−1

ℓ

j − 1 i

s i

j i

0 0

αℓ(j) :=

, βℓ(j) :=

, where

= 1,

= 0, s < i.

i=1

i=0

Let 1 ≤ n ≤ k and ∆∗(m,k,n) denote the minimal dimension d of Euclidean space such that for any set of m finite measures in Rd there exist k mutually orthogonal hyperplanes in Rd such that any n of these k hyperplanes divide each of the m measures into 2n parts of equal size.

Note that this quantity—without the orthogonality condition—was first considered in [5]. Recently, in [16], some upper bounds for ∆∗(m,k,n) were obtained for n = 2 and 3.

The main result of this paper regarding orthogonal mass partitioning is the following theorem.

###### Theorem 1.4. mαn(k)

+

k

It is easy to see that

k − 1 2 ≤ ∆∗(m,k,n) ≤ m + (βn(k) − 1)2⌊log

2m⌋ (1.3)

αk(k) = 2k − 1, βk(k) = 2k−1, ∆∗(m,k,k) = ∆∗(m,k). If n = k then (1.3) is equal to (1.2), i.e. Theorem 1.4 yields Theorem 1.3.

Let n = 2. Since α2(k) = k(k + 1)/2 and β2(k) = k, so by (1.3) we have m(k + 1) + k − 1 2 ≤ ∆∗(m,k,2) ≤ m + (k − 1)2⌊log

2m⌋ (1.4)

It is easy to see that if m = 2j − 1, j ≥ 1, then the lower bound (1.4) is equal to the upper, which implies the following theorem.

###### Theorem 1.5. ∆∗(2j − 1,k,2) = 2j−1(k + 1) − 1, j ≥ 1, k ≥ 2,

i.e, if m = 2j − 1, d = 2j−1(k + 1) − 1, and µ1,...,µm are m finite measures in Rd, then there exist k mutually orthogonal hyperplanes in Rd such that any pair of these k hyperplanes divide each of the m measures into four parts of equal size.

In the case j = 1, i.e. m = 1, we have ∆∗(1,k,2) = k.

Corollary 1.6. Let µ be a finite measure in Rd. Then there exist d mutually orthogonal hyperplanes such that every pair of these hyperplanes divides Rd into four parts of equal measure µ.

- Remark 3. This fact is contained in Makeev’s paper [13, Theorem 4]. However, in our opinion, this statement has not proven there.


These theorems have versions involving additional equivariant constraints—for instance, when the hyperplanes pass through a given set of points (see Section 3). Here, we consider one possible extension of Theorem 1.4.

- Theorem 1.7. Let 1 ≤ n ≤ k, d = 2m + (βn(k) − 1)2⌊log2m⌋, and µ1,...,µm be m finite measures in Rd. Then there exist k mutually orthogonal hyperplanes in Rd such that any n of these k hyperplanes divide each of the m measures into 2n parts of equal size and each hyperplane passes through the centers of mass of all the measures.


It is easy to see that the analogue of Corollary 1.6 is the following statement.

Corollary 1.8. Let µ be a finite measure in Rd. Then there exist (d−1) mutually orthogonal hyperplanes, each passing through the center of mass of this measure, such that every pair of these hyperplanes divides Rd into four parts of equal measure µ.

#### 1.3 Algorithms for mass partitioning.

In discrete versions of mass-partitioning results, the task involves partitioning several finite families of points in Rd in a prescribed manner. If the total number of points is N, it is desirable to have an algorithm for finding such a partition whose running time is expressed in terms of N.

In two dimensions a ham–sandwich cut is a line h that bisects X1 and X2 with N points in total. Edelsbrunner and Waupotitsch [8] find an algorithm that can compute h in time O(N log N). Finally, Lo, Matousˇek, and Steiger [12] proved that in the plane ham–sandwich cut can be computed in O(N) time. The paper also presents polynomial algorithms for finding ham–sandwich cuts in every dimension d > 1.

Previously known algorithm for the pancake theorem is discovered in [23] and has

- O(N log N) time complexity. Recently, we improve this result:


Theorem [10]. For any set of N points P in R2, a partition of P by two orthogonal lines into four equal parts can be found in optimal time, linearly dependent on N, i.e. in Θ(N) time.

In [10] we also proved that the computational complexity of the discrete versions of

- Theorem 1.4 (the case where n = k = 2) and Corollary 1.6 is polynomial. However, the algorithms proposed in [10] are not optimal. An interesting problem is finding efficient and optimal algorithms for the orthogonal partitioning of masses for arbitrary parameters m,k, and n.


Acknowledgment. I would like to thank Pavle Blagojevi´c, Florian Frick, Roman Karasev, Pablo Soberon, and Rade Zivaljevi´cˇ for the helpful discussions, valuable comments, and useful references.

### 2 Borsuk–Ulam type theorems

In this section we deal with G–BUT manifolds, where G = (Z/2)k, using the theory of equivariant cobordism. Let m ≥ n, we say that a G–manifold Mm is BUT (Borsuk–Ulam type) if for any continuous equivariant f : Mm → Rn the set of zeros Zf := f−1(0) is not empty. The BUT–manifolds and spaces we considered in [17, 18, 19, 20].

#### 2.1 G–BUT manifolds and equivariant cobordisms.

Consider closed (compact and without boundary) PL manifolds with an H-structure, such as unoriented, oriented, complex, etc. One can define a “cobordism with H-structure”, but there are various technicalities. In each particular case, cobordism is an equivalence relation on manifolds. A basic question is to determine the equivalence classes for this relationship, called the cobordism classes of manifolds. These form a graded ring called the cobordism ring

ΩH∗ , with grading by dimension, addition by disjoint union, and multiplication by cartesian product.

Let ΩH∗ (G) denote the PL cobordism group with H-structure of free simplicial actions of a finite group G. Let ρ : G → GL(n,R) be a representation of a group G on Rn which also has H-structure. [17, Lemma 2.4] shows that for a generic simplicial equivariant map f : Mm → Rn, m ≥ n, the cobordism class of the manifold Zf is uniquely defined up to cobordism and so well defines a homomorphism

µGρ : ΩHm(G) → ΩHm−n(G). (2.1) Note that this homomorphism depends only on a representation ρ of a group G on Rn. The invariant µGρ is an obstruction for the existence of equivariant maps f : M → Rn \ {0}.

Namely, we proved the following theorem [17, Th. 3].

- Theorem 2.1. Let Mm be a closed PL G-manifold with a free action τ. Let ρ be a linear action of G on Rn with the fixed–point set (Rn)G = {0}. Let us assume that actions, mani-


folds, and maps are with H-structure. If µGρ ([M,τ]) ̸= 0 in ΩHm−n(G), then for any continuous equivariant map f : Mm → Rn the set of zeros Zf is not empty.

In the case m = n the dimension of ΩHm−n(G) is 0. In [17, Sec. 3] we defined an invariant degG(f) ∈ Z2. In this case, condition µGρ ([M,τ]) ̸= 0 in the theorem can be replaced by degG(f) = 1, see [17, Th. 1]. Given a finite group G acting free on a closed PL-manifold Mn and acting linearly on Rn with (Rn)G = {0}. Let f : Mn → Rn be a continuous equivariant transversal to zeros map. Since Zf is a finite free G-invariant subset of M, we have |Zf| = k |G|, where k ≥ 0 is integer. Set degG(f) = 1 if k is odd, and degG(f) = 0 if k is even. The following theorem can be easily derived from Theorem 1 in our paper [17].

- Theorem 2.2. Let G be a finite group acting linearly on Rm with the fixed–point set (Rm)G = {0}. Let Mm be a PL (or smooth) free G–manifold. If there is a G–manifold Nm which is free G–cobordant to Mm and a continuous equivariant transversal to zeros h : Nm → Rm with degG(h) = 1, then Zf ̸= ∅ for any continuous equivariant f : Mm → Rm.


#### 2.2 BUT – theorem for G = Z/2.

- Let H = O (unoriented cobordisms). The set of cobordism classes of closed unoriented n–dimensional manifolds is usually denoted by Nn (= ΩOn). In 1954 Rene´ Thom proved


N∗ =

Nn = F2[xk |k ≥ 1, k ̸= 2i − 1]

n≥0

Let G = Z/2. We denote by N∗(Z/2) the unoriented cobordism module of free involutions. Actually, N∗(Z/2) is a free N∗-module with basis [Sn,A], n ≥ 0, where [Sn,A] is

the cobordism class of the antipodal involution on the n–sphere [7, Th. 23.2]. Thus, every manifold Mm with a free involution T can be uniquely represented in Nm(Z/2) in the form:

[M,T] =

m

[Vk][Sm−k,A], Vk ∈ Nk.

k=0

Let ν be the 1–dimensional linear representation of Z/2 defined by ν(x) = −x, x ∈ R. In this case µZ

ν2 = ∆ν = ∆, where

∆ : Nk(Z/2) → Nk−1(Z/2) is the Smith homomorphism, and if

Rnρ = Rν ⊕ · · · ⊕ Rν, i.e. ρ = (ν,...,ν), ρ(u) = −u, u ∈ Rn, then µZ

ρ2 = ∆n [7, Th. 26.1]. This fact yields, see Lemma 5.1 [17], the following equality

µZρ/2([Mm,T]) = ∆n

m

[Vk][Sm−k,A] =

k=0

m−n

[Vk][Sm−n−k,A].

k=0

Our generalization of the classical Borsuk–Ulam theorem is Theorem 2 from [17].

- Theorem 2.3. Let Mn be a closed connected PL-manifold with a free simplicial involution T. Then the following statements are equivalent:


- (a) M is a Z/2–BUT manifold.
- (b) M admits an antipodal continuous map h : Mn → Rn with degZ/2(h) = 1.
- (c) [Mn,T] = [Sn,A] + [V 1][Sn−1,A] + ... + [V n][S0,A] in Nn(Z/2).


- Remark 4. The class of BUT manifolds is very wide. For instance, “half” of two-dimensional


oriented manifolds are Z/2–cobordant to [S2,A], namely, any [Mg2,T], where the genus g is even and T is a free involution, is Z/2–cobordant to [S2,A].

- 2.3 (Z/2)k–cobordisms. Let G = (Z/2)k = Z/2 × ... × Z/2. In this case, see [7, Sec. 29], we have


N∗((Z/2)k) = N∗(Z/2) ⊗ ... ⊗ N∗(Z/2). (2.2) Equivalently, N∗((Z/2)k) is a free N∗-module with generators {γi

k}, where i1,...,ik are non–negative integers and γi := [Si,A] ∈ Ni(Z/2).

1⊗...⊗γi

###### in N∗((Z/2)k), i.e. that is [M]G, where M = Si

1 ⊗...⊗γi

Let Γ(i1,...,ik) denote the generator γi

k

###### × ... × Si

###### with a group action by λℓ(x) = −x, x ∈ Si

⊂ Ri

ℓ+1, ℓ = 1,...,k. .

1

k

ℓ

###### Let ρq : G → Rq be an irreducible 1–dimensional linear representation of G and ∆q := µGρ

. Then by (2.1) we have a homomorphism

q

∆q : Nm((Z/2)k) → Nm−1((Z/2)k). Let us denote

, i = 1,...,k. It is not hard to see that (2.1), Theorem 2.3(c), and (2.2) yield the following lemmas

ai := ∆λ

i

- Lemma 2.4. a1(Γ(i1,...,ik)) = Γ(i1−1,i2,...,ik)), i1 ≥ 1, ..., ak(Γ(i1,...,ik)) = Γ(i1,...,ik−1,ik−1)), ik ≥ 1.
- Lemma 2.5. Let 0 ≤ j1 ≤ i1,...,0 ≤ jk ≤ ik. Then

aj

1

1 ...aj

k

k (Γ(i1,...,ik)) = Γ(i1 − j1,...,ik − jk).

- Lemma 2.6. Let q = ε1λ1 + ... + εkλk ∈ G = (Z/2)k. Then

∆q = ε1a1 + ... + εkak, ∆q (Γ(i1,...,ik)) =

k

ℓ=1

εℓ Γ(i1,...,iℓ − 1,...,ik).

- Lemma 2.7. Let ρ = (ρq


###### ), qi ∈ G = (Z/2)k. Then ∆ρ := µGρ = ∆q

###### ,...,ρq

n

1

###### ...∆q

.

n

1

- 2.4 General BUT – theorem for G = (Z/2)k. The following theorem follows directly from Theorem 2.1 and Lemma 2.7.


Theorem 2.8. Let G = (Z2)k. If Mm is a PL closed G–manifold then we write [M]G for the corresponding element in Nm((Z/2)k). Let

Rnρ = Rq

1 ⊕ Rq

2 ⊕ · · · ⊕ Rq

, Zρ := ∆ρ([M]G) ∈ Nm−n((Z/2)k),

n

and f : Mm → Rnρ be a continuous equivariant map. If Zρ ̸= 0, then the zeros set Zf is not empty. Moreover, if f is transversal to zeros, i.e. Zf is a G–manifold, then

[Zf]G = Zρ in Nm−n((Z/2)k).

#### 2.5 Borsuk–Ulam theorem for the product of spheres. Let q = ε1λ1 + ... + εkλk ∈ G = (Z/2)k,

= {(v1,...,vk)|vℓ ∈ Si

S(i1,...,ik) := Si

× ... × Si

, ℓ = 1,...,k}, q(v1,...,vk) = ((1 − 2ε1)v1,...,(1 − 2εk)vk).

1

ℓ

k

Lemma 2.6 implies the following fact:

- Lemma 2.9.


∆q([S(i1,...,ik)]G) = (ε1a1 + ... + εkak)(Γ(i1...,ik)) =

k

εℓ Γ(i1,...,iℓ − 1,...,ik).

ℓ=1

- Proof of Theorem 1.1. Proof. Let d = i1 + ... + ik. We have [S(i1,...,ik]G = Γ(i1...,ik) in Nd((Z/2)k). From Lemma


- 2.9 it follows that


∆ρ([S(i1,...,ik]G) = ∆q

...∆q

1

(Γ(i1...,ik)) =

m

m

(εℓ,1a1 + ... + εℓ,kak)(Γ(i1...,ik)).

ℓ=1

It is clear that ∆ρ([S(i1,...,ik]G) ̸= 0 in Nd−m((Z/2)k) if and only if

m

1 ,...,ai

k+1

(εℓ,1a1 + ... + εℓ,kak) ̸= 0 in P(i1,...,ik) = F2[a1,...,ak]/(ai

1+1

k ).

ℓ=1

Thus Theorem 2.8 yields Theorem 1.1.

| |
|---|


#### 2.6 Borsuk–Ulam type theorems for Stiefel manifolds. The Stiefel manifold

Vn,k = {(u1,...,uk) ∈ (Sn−1)k |ui · u1 = 0,...,ui · ui−1 = 0 for all 1 < i ≤ k}

fit into a family of fiber bundles; for their sequential construction, they can be represented as a tower of fiber bundles.

The first unit vector u1 lies in Sn−1. Once we have chosen this first vector, the remaining k−1 vectors must be orthonormal to it. This means they must all lie in the (n−1)-dimensional orthogonal complement of the first vector. This gives us the projection map:

p : Vn,k −→ Sn−1

where p takes a k–frame and retains only the first vector. The fiber of this projection (the space of “remaining choices”) is Vn−1,k−1. We can repeat this logic recursively. By successively discarding one vector at a time, we obtain a sequence of nested bundles.

- Vn−1,k−1 −→ Vn,k −→ Sn−1.
- Vn−2,k−2 −→ Vn−1,k−1 −→ Sn−2


... and so on, until we reach V (n−k+1,1), which is just the sphere Sn−k. In short, the Stiefel manifold is “built” by attaching spheres of decreasing dimensions (Sn−1,Sn−2,...,Sn−k) to one another through these fiber bundle relations. Thus, u1 ∈ Sn−1, u2 ∈ Sn−2, ..., uk ∈ Sn−k.

Let G = (Z/2)k with generators λ1,...,λk acting on Vn,k by λj(u1,...,uj,...,uk) = (u1,...,−uj,...,uk), j = 1,...,k.

- Lemma 2.10. [Vn,k]G = Γ(n − 1,...,n − k) ∈ Nm((Z/2)k), m = nk − k(k + 1)/2.


Proof. Since ui ∈ Sni −i, we have ani −i+1 = 0 for all i = 1,...,k. If i1 + ... + ik ≤ m and (i1,...,ik) ̸= (n − 1,...,n − k), then Lemma 2.5 yields

an1−1...ank−k(Γ(i1,...,ik)) = 0. Therefore

an1−1...ank−k([Vn,k]G) = ε0Γ(0,...,0) ∈ N0((Z/2)k) = F2, ε0 = 0 or 1.

To prove that ε0 = 1, we use Theorem 2.2 ([17, Th. 1]). It follows from this theorem that it is sufficient to construct an example of a proper map

###### )n−1 ⊕ (Rλ

)n−k with degG(h) = 1.

###### )n−2 ⊕ · · · ⊕ (Rλ

h : Vn,k −→ RmΛ := (Rλ

1

2

k

Let ui = (xi,0,xi,1,...,xi,n−1) ∈ Sni −1, wi = (xi,i,...,xi,n−1) for all i = 1,...,k, hi(u1,...,uk) := hi(ui) = wi ∈ Rn−i, h = (h1,...,hk) : Vn,k −→ RmΛ . Now we show that |Zh| = |G| = 2k, i.e. degG(h) = 1. If w1 = 0, then x1,0 = ±1, i.e. Zh

###### = (±1,0,...,0). Zh

1

= {u3 ∈ Sn3−1 |w3 = 0, u3 ·u1 = 0, u3 ·u2 = 0},... Then

###### = {u2 ∈ Sn2−1 |w2 = 0, u2 ·u1 = 0},Zh

- 2


3

###### = (0,...,0,±1), |Zh| = 2k. Theorem 2.8 implies that ZΛ = [Zh]G = Γ(0,...,0) ̸= 0. Thus, ε0 = 1.

###### = (0,±1,0,...,0), Zh

###### = (0,0,±1,0,...,0),...,Zh

Zh

2

3

k

| |
|---|


###### Proof of Theorem 1.2.

Proof. Let d = nk − k(k + 1)/2. By Lemma 2.10 we have [Vn,k]G = Γ(n − 1,...,n − k) in Nd((Z/2)k). Since the assumption of the theorem is that

∆ρ([Vn,k]G) =

m

(εℓ,1a1 + ... + εℓ,kak)(Γ(n − 1,...,n − k)) ̸= 0 in Nd−m((Z/2)k),

ℓ=1

- Theorem 2.8 yields Theorem 1.2.


| |
|---|


- 3 Equipartition of measures: functions gµ


#### 3.1 Hyperplanes in Rd

We represent hyperplanes in Rd as points in Sd. Let v = (t0,t1,...,td) be a point (unit vector) in the unit sphere Sd ⊂ Rd+1. If at least one of the components t1,...,td is nonzero, we assign to the point v a hyperplane H0(v) in Rd. Let

H0(v) := {(x1,...,xd) ∈ Rd : t1x1 + ... + tdxd = t0}. H(v) := {(x1,...,xd) ∈ Rd : t1x1 + ... + tdxd ≤ t0},

then half–spaces H(v) and H(−v) are bounded by H0(v). For v = ±e0, e0 := (1,0,...,0), H0(v) is not defined, but we have

H(e0) = Rd, H(−e0) = ∅.

We are interested in hyperplanes that bisect finite measures in Rd, i.e. µ(H(v)) = µ(H(−v)), this cannot happen when v = ±e0, so this case can be ignored. Then, for any set of unit vectors v1,...,vk, vi = (ti0,ti1,...,tik) ̸= ±e0, in Sd ⊂ Rd+1 we have a corresponding set of hyperplanes H0(v1),...,H0(vk) in Rd. Thus, (v1,...,vk) ∈ Sd,k.

#### 3.2 Function gµ.

Let v = {v1,...,vn} ∈ Sd,n := (Sd)n = S(d,...,d), s = {s1,...,sn} be a vector of signs, i.e. si is +1 or −1, i = 1,...,n, and

n

H(v,s) :=

H(sjvj).

j=1

Let µ be a finite measure on Rd. We denote by r(s) the number of negative si in s, gµ(n)(v) = gµ(v) :=

(−1)r(s)µ(H(v,s)), Cn := ({−1,+1})n.

s∈Cn

Let G = (Z/2)n, λ1,...,λn are generators of G, and ωn := λ1 + ... + λn ∈ G. The next lemma follows easily from the definition of gµ(n)(v).

- Lemma 3.1. gµ(n) : Sd,n → Rω

n

is a continuous symmetric equivariant function with respect to the action G = (Z/2)n on Sd,n.

- Lemma 3.2. Let µ be a finite measure on Rd. Let v = (v1,...,vn) ∈ Sd,n. Suppose gµ(1)(v1) = 0,...,gµ(1)(vn) = 0,gµ(2)(v1,v2) = 0,...,gµ(2)(vn−1,vn) = 0,...,gµ(n)(v1,...,vn) = 0.

Then hyperplanes {H0(v1),...,H0(vn)} divide µ into 2n equal parts. Proof. 1. Let n = 1. By definition, gµ(1)(v1) = µ(H(v1)) − µ(H(−v1)), v1 ∈ Sd. Suppose

- gµ(1)(v1) = 0. Then µ(H(v1)) = µ(H(−v1)) = 21µ(Rd), i.e. H0(v1) bisects µ.

- 2. Let v = (v1,v2) ∈ Sd,2 and h(s) = µ(H(v),s), s ∈ C2. Since gµ(1)(v1) = gµ(1)(v2) = 0 by 1 we have

h(1,1)+h(−1,1) = h(1,−1)+h(−1,−1) = h(1,1)+h(1,−1) = h(−1,1)+h(−1,−1) =

- 1

- 2


µ(Rd).

As a result, we obtain h(1,1) = h(−1,−1) = a and h(−1,1) = h(1,−1) = b. The equality gµ(2)(v1,v2) = 0 gives us a new equation

2a = h(1,1) + h(−1,−1) = h(1,−1) + h(−1,1) = 2b,

i.e. a = b = 14µ(Rd). Thus hyperplanes {H0(v1) and,H0(v2)} divide µ into four equal parts.

- 3. Let us assume that the statement of the lemma is true for all n > k. Let us prove it for




n = k. We call s1 and s2 from Ck neighbors if they differ in only one position. In other words, the Hamming distance between them is 1. Using the same arguments as in 2, we can prove that for neighbors

h(s1) + h(s2) =

µ(Rd) 2k−1 and h(s) = h(s′) if and only if r(s) = r(s′).

Let h(s) be denoted by a for even r(s), otherwise h(s) = b. Then the equation gµ(k)(v1,...,vk) = 0 implies 2k−1a = 2k−1b, i.e. a = b and h(s) = µ(R

d)

2k for all s ∈ Ck.

| |
|---|


Note that Lemma 3.2 contains 2n − 1 independent equations. Now we consider an extension of this lemma.

- Lemma 3.3. Let 1 ≤ n ≤ k ≤ d and µ be a finite measure in Rd. Suppose (v1,...,vk) ∈ Sd,k


is such that for all j, 1 ≤ j ≤ n, and all j–subsets {vi

j} of {v1,...,vk}, we have gµ(j)(vi

,...,vi

1

) = 0, 1 ≤ i1 < ... < ij ≤ k. (3.1)

###### ,...,vi

1

j

Then (3.1) contains αn(k) independent equations and each n–subset of hyperplanes {H0(v1),...,H0(vk)} divides µ into 2n equal parts.

Proof. It is clear that the number of equations in (3.1) is equal to

αn(k) = k +

k 2

+ ... +

k n

.

If {vi

j} is an n–subset of {v1,...,vk}, then it satisfies the conditions of Lemma 3.2. Applying this lemma to all n–subsets proves Lemma 3.3.

,...,vi

1

| |
|---|


Repeated application of the Lemma 3.3 leads to the following theorem:

- Theorem 3.4. Let 1 ≤ n ≤ k ≤ d. Let µ1,...,µm be finite measure in Rd. Suppose


(v1,...,vk) ∈ Sd,k is such that for all j, 1 ≤ j ≤ n, and all j–subsets {vi

j} of {v1,...,vk} with 1 ≤ i1 < ... < ij ≤ k we have

,...,vi

1

gµ(j)

(vi

,...,vi

) = 0, ℓ = 1,...,m. (3.2)

1

j

ℓ

Then each n–subset of hyperplanes {H0(v1),...,H0(vk)} divides Rd into 2n parts of equal size in each of the m measures.

#### 3.3 Additional constraints in Theorem 3.4. Let p = (x1,...,xd) be a point in Rd, v = (t0,t1,...,td) ∈ Sd, and

gp(v) := t0 − (t1x1 + ...tdxd).

Then gp(−v) = −gp(v), i.e. gp is an equivariant function. If gp(v) = 0, then H0(v) passes through the point p in Rd. Therefore, if S = {p1,...,pℓ} then equations

(vj) = 0, i = 1,...,ℓ, j = 1,...,k, (3.3) yield that all hyperplanes H0(v1),...,H0(vk) pass through S.

gp

i

- Corollary 3.5. If we add to the assumptions of Theorem 3.4 equations (3.3) hyperplanes {H0(v1),...,H0(vk)} are mutually orthogonal, then we obtain existence of hyperplanes {H0(v1),...,H0(vk)} that divide each of the m measures into 2n equal and pass through S.

Another set of equivariant constraints arises when the hyperplanes are required to be mutually orthogonal.

- Corollary 3.6. If we add to the assumptions of Theorem 3.4 another k(k − 1)/2 conditions


- namely, that the hyperplanes {H0(v1),...,H0(vk)} are mutually orthogonal, then we obtain existence of such hyperplanes that divide each of the m measures into 2n equal parts.

### 4 Proof of the theorem on orthogonal partitions

###### Lemma 4.1.

∆∗(m,k,n) ≥

k − 1 2

mαn(k) k

+

Proof. This follows from the argument in [21, Th. 4.7] showing that ∆(m,k) ≥ m(2k − 1)/k and from the fact that in order for k hyperplanes to be mutually orthogonal, k(k − 1)/2 equations are needed.

Place m mass distributions, each one-dimensional and uniform on an interval, along the d–dimensional moment curve Md := {(t,t2,...,td) : t ∈ R}, with no overlap. By Lemma 3.3 and Theorem 3.4 simultaneous k-partition of the m masses would need at least mαn(k) independent equations. On the other hand, the dimension of the Stiefel manifold M is dk − k(k − 1)/2. Therefore, we have the inequality

k(k − 1)

2 ≥ mαn(k). That proves the lemma.

dk −

| |
|---|


Let 1 ≤ j ≤ n ≤ k Qk,j(a1,...,ak) :=

(ε1a1 + ... + εkak), where all εi = 1 or 0.

ε1+...εk=j

Pk,n(a1,...,ak) :=

n

Qk,j(a1,...,ak).

j=1

Then Qk,1 = a1...ak, Qk,2 = (a1 + a2)...(a1 + ak)...(ak−1 + ak),.... It is clear that

deg Qk,j =

k j

, deg Pk,n = deg Qk,1 + ... + deg Qk,n = αn(k). (4.1)

###### Lemma 4.2. Let 2 ≤ n ≤ k ≤ d and (Pk,n(a1,...,ak))m ̸= 0 in P(d,d − 1,...,d − k + 1).

Then for any set of m finite measures in Rd there exist k mutually orthogonal hyperplanes such that any n of these k hyperplanes divide each of the m measures into 2n equal parts.

Proof. 1. Let

R(a1,...,ak) := Qk,2(a1,...,ak)...Qk,n(a1,...,ak)(Pk,n(a1,...,ak))m−1, i.e. Pk,nm = Qk,1R. By the assumption, Pk,nm ̸= 0 in P(d,d − 1,...,d − k + 1); therefore

R(a1,...,ak) ̸= 0 in P(d − 1,d − 2,...,d − k). (4.2)

- 2. Let the hyperplane H0(v), v = (t0,t1,...td) ∈ Sd, be defined by the equation t1x1 + ... + tdxd = t0, (x1,...,xd) ∈ Rd. (As above we assume that at least one of the components t1,...,td is non-zero.) Let n(v) denote the unit normal vector to H0(v). Then

n(v) = (t1,...,td)/ t21 + ... + t2d ∈ Sd−1.

Let a finite measure µ and a unit vector u in Rd be given. It is easy to prove that there exists a unique hyperplane with normal vector u that bisects this measure. This establishes a correspondence between vectors uµ in Sd−1 and hyperplanes H0(vµ), i.e. vectors vµ ∈ Sd, that bisect the measure µ. Therefore, if we have v = (v1,...,vk) ∈ Sd,k then v uniquely determines uµ = ((u1)µ,...,(uk)µ) ∈ Sd−1,k and k hyperplanes {H((vi)µ)} in Rd that bisect µ, i.e. {(vi)µ} satisfy the equations

gµ(1)((vi)µ) = 0, i = 1,...,k. (4.3)

- 3. Let µ1,...,µm be finite measures in Rd and µ = µ1. Suppose v ∈ Sd,k satisfies (4.3), then the correspondent vector uµ is a unit vector in Rd. Then the remaining equations in (3.2) can be considered as equations on u ∈ Sd−1,k. The orthogonality conditions for the hyperplanes are also equations in u, which implies that equations (3.2)—without (4.3)—are equations on the Stiefel manifold Md,k. It is not difficult to see that the solution of these equations in


- P(d − 1,d − 2,...,d − k) is R(a1,...,ak)(Γ(d − 1,...,d − k)), see subsection 2.6. Thus, (4.2), Theorem 1.2, and Corollary 3.6 prove the lemma.


| |
|---|


- Lemma 4.3. Let 2 ≤ n ≤ k. Then


aβσn(1)(k)aσβn(2)(k−1)...aβσn(k(1)) . (4.4)

Pk,n(a1,...,ak) =

σ∈Σk

The highest and lowest monomials of a polynomial Pk,n in F2(a1,...,ak) with the lexicographic order a1 > ... > ak are

aβ1n(k)aβ2n(k−1)...aβk−n(2)1 akβn(1), aβ1n(1)a2βn(2)...aβk−n(1k−1)akβn(k).

Proof. In the proof of Theorem 38 [14] there is an explicit formula for Pk,k in the polynomial ring F2(a1,...,ak):

k−1

k−2

a2

σ(1) a2

Pk,k(a1,...,ak) =

σ(2) ...aσ(k). (4.5)

σ∈Σk

Note that βk(k − i) = 2k−i−1, 0 ≤ i ≤ k − 1, and in particular, βk(1) = 1. Then (4.5) can be written as

k(k−1)

aβ

σ(1) aβ

k(k)

σ(2) ...aβ

k(1)

Pk,k(a1,...,ak) =

σ(k) . (4.6)

σ∈Σk

This fact is easily proven by induction on k. Moreover, its generalization for Pk,n can be proven using double induction on n and k.

| |
|---|


- Lemma 4.4. Let i,k,n,q,r ∈ Z, 2 ≤ n ≤ k, 0 ≤ i ≤ k − 1, q > 0, and 0 ≤ r < 2q. Then d0 − di ≥ i, di := 2qβn(k − i) + rβn(i + 1).


Proof. Obviously, d0 − di is minimal when r takes its maximum possible value—that is, r = 2q − 1. Then

d0 − di ≥ 2qβn(k) + 2q − 1 − (2qβn(k − i) + (2q − 1)βn(i + 1)) = 2qA(i) + B(i),

n−1

- i
- j


A(i) := βn(k) + 1 − βn(k − i) − βn(i + 1), B(i) := βn(i + 1) − 1 =

.

j=1

It is not difficult to prove that A(i) ≥ 0 (with equality holding at i = 0 or k − 1) and that B(i) ≥ i (with equality holding at n = 2). Consequently, d0 − di ≥ i.

| |
|---|


Proof of Theorem 1.4 Proof. The lower bound in the theorem is proven in Lemma 4.1.

Let m = 2q + r, where 0 ≤ r < 2q, d∗ := 2qβn(k) + r = m + (βn(k) − 1)2⌊log2m⌋, and

2q

r

p∗ = aβ1n(k)aβ2n(k−1)...aβk−n(2)1 ak

a1aβ2n(2)...akβ−n(1k−1)aβkn(k)

.

Lemma 4.4 implies that p∗ is not equal zero in P(d∗,...,d∗ − k + 1). By Lemma 4.3, p∗ is a monomial of (Pk,n)m, therefore (Pk,n)m ̸= 0 in P(d∗,...,d∗ − k + 1) Thus, Lemma 4.2 proves the theorem.

| |
|---|


Proof of Theorem 1.7 Proof. Note that for finite measures, the center of mass is well-defined. Therefore, we have m points—centers of mass c1,...,cm—through which all k hyperplanes pass. Let

P˜k,n = a1...akPk,n. Since (Pk,n)m ̸= 0 in P(d∗,...,d∗ − k + 1), we have that

(P˜k,n)m ̸= 0 ∈ P(d∗ + m,...,d∗ + m − k + 1). Thus, Theorem 1.4 and Corollary 3.5 prove the theorem.

| |
|---|


### References

- [1] David Avis, Non–partitionable point sets, Inform. Process. Letters, 19:3, (1984), 125– 129
- [2] W. A. Beyer and Andrew Zardecki, The early history of the ham sandwich theorem, Amer. Math. Monthly, 111 (2004): 58–61
- [3] Pavle Blagojevic´, Florian Frick, Albert Haase, and Gu¨nter M. Ziegler, Hyperplane mass partitions via relative equivariant obstruction theory, Doc. Math. 21 (2016), 735–771
- [4] Pavle Blagojevi´c, Florian Frick, Albert Haase, and Gu¨nter M. Ziegler, Topology of the Gru¨nbaum–Hadwiger–Ramos hyperplane mass partition problem, Trans. Amer. Math. Soc. 370:10 (2018), 6795–6824.
- [5] Pavle Blagojevic´ and Roman Karasev, Extensions of theorems of Rattray and Makeev, Topol. Methods Nonlinear Anal. 40:1 (2012), 189–213.
- [6] Yu Hin Chan, Shujian Chen, Florian Frick, and J. Tristan Hull, Borsuk-Ulam theorems for products of spheres and Stiefel manifolds revisited, Topol. Methods Nonlinear Anal. 55 (2020), no. 2, 553–564
- [7] Pierre E. Conner and Edwin E. Floyd, Differentiable periodic maps, Springer-Verlag, 1964.
- [8] Herbert Edelsbrunner and Roman Waupotitsch. Computing a ham sandwich cut in two dimensions. J. Symbolic Comput. 2 (1986), 171–178.
- [9] Edward Fadell and Sufian Husseini, An ideal-valued cohomological index theory with applications to Borsuk–Ulam and Bourgin–Yang theorems, Ergodic Theory Dynam. Systems, 8:8 (1988), 73–85.
- [10] Alexey Fakhrutdinov and Oleg R. Musin, Algorithms for orthogonal partitioning into four parts, preprint, arXiv:2511.20866
- [11] Deron Lessure and Pablo Sobero´n, Partitions of mass assignments with spheres and wedges, preprint, arXiv:2507.06919
- [12] Chi -Yuan Lo, Jiˇr´ı Matouˇsek, and William L. Steiger. Algorithms for Ham-Sandwich Cuts. Discrete Comput. Geom. 11 (1994), 433–452.
- [13] Vladimir V. Makeev, Equipartition of a continuous mass distribution, Journal of Mathematical Sciences, 140 (2007), no. 4, 551–557.
- [14] Peter Mani-Levitska, Sinisˇa Vrec´ica, and Rade Zivaljevi´c,ˇ Topology and combinatorics of partitions of masses by hyperplanes, Adv. Math. 207 (2006), no. 1, 266–296.


- [15] Jiˇrı´ Matousˇek, Using the Borsuk–Ulam theorem, Universitext, Springer-Verlag, Berlin, 2003.
- [16] Andres Mejia, Steven Simon, and Jialin Zhang, The generalized Makeev problem revisited, Beitr Algebra Geom. 66 (2025), 253–274.
- [17] Oleg R.Musin, Borsuk–Ulam type theorems for manifolds, Proc. Amer. Math. Soc. 140

(2012), 2551–2560.

- [18] Oleg R. Musin, Generalizations of Tucker–Fan–Shashkin lemmas, Arnold Math. J., 2:3

(2016), 299–308.

- [19] Oleg R. Musin and Alexey Yu. Volovikov, Borsuk–Ulam type spaces. Mosc. Math. J., 15 (2015), 749–766
- [20] Oleg R. Musin and Alexey Yu. Volovikov, Borsuk–Ulam type theorems for G–spaces with applications to Tucker type lemmas, J. Fixed Point Theory Appl., 25:1 (2023), Article: 32
- [21] Edgar A. Ramos, Equipartition of mass distributions by hyperplanes, Discrete Comput. Geom. 15 (1996), no. 2, 147–167.
- [22] Edgardo Rolda´n-Pensado and Pablo Sobero´n. A survey of mass partitions. Bull. Amer. Math. Soc. (N.S.), 59(2), (2022), 227–267.
- [23] Sambuddha Roy and William Steiger, Some Combinatorial and Algorithmic Applications of the Borsuk–Ulam Theorem. Graphs and Combinatorics, 23(Suppl 1), 331–341

(2007).

- [24] Yuri A. Shashkin, Fixed Points, Amer. Math. Soc., Providence, RI, 1991.
- [25] Pablo Sober´on and Yuki Takahashi, Lifting methods in mass partition problems, Int. Math. Research Notices, 2023:16, (2023), 14103–14130.
- [26] Arthur H. Stone and John W. Tukey, Generalized “sandwich” theorems, Duke Math. J., 9 (1942), 356–359
- [27] Rade T. Zivaljevi´c,ˇ Topological methods in discrete geometry, Chapter 21, Handbook of Discrete and Computational Geometry, Third Edition, CRC Press, 2017.


O. R. Musin, University of Texas Rio Grande Valley, School of Mathematical and Statistical Sciences, One West University Boulevard, Brownsville, TX, 78520, USA.

E-mail address: oleg.musin@utrgv.edu

