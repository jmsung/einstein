---
type: source
kind: paper
title: Conjectures on the reduced Kronecker coefficients
authors: Tao Gui
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2210.14668v4
source_local: ../raw/2022-gui-conjectures-reduced-kronecker-coefficients.pdf
topic: general-knowledge
cites:
---

## arXiv:2210.14668v4[math.RT]30Jan2026

Séminaire Lotharingien de Combinatoire XX (2025) Proceedings of the 37th Conference on Formal Power Article #1, 12 pp. Series and Algebraic Combinatorics (Sapporo)

# Conjectures on the Reduced Kronecker Coefficients

Tao Gui*1

1Beijing International Center for Mathematical Research, Peking University, No. 5 Yiheyuan Road, Haidian District, Beijing 100871, P.R. China

Abstract. We formulate a series of conjectures on the stable tensor product of irreducible representations of symmetric groups, which are closely related to the reduced Kronecker coefficients. These conjectures are certain generalizations of Okounkov’s conjecture on the log-concavity of the Littlewood–Richardson coefficients and the Schur log-concavity theorem of Lam–Postnikov–Pylyavskyy. We prove our conjectures in some special cases and discuss some implications of these conjectures.

Keywords: log-concavity, tensor products, representations of symmetric groups, reduced Kronecker coefficients, Schur polynomials

### 1 Introduction

The main purpose of this article is to announce and provide supporting evidence for some conjectures on the stable tensor product of irreducible representations of symmetric groups, which are closely related to the reduced Kronecker coefficients.

Recall that a sequence of real numbers a0, a1, . . . is called log-concave if

a2i ≥ ai−1ai+1 for all i ≥ 1.

Log-concave sequences are very common in algebra, geometry, and combinatorics. In addition, many log-concave phenomena appear in representation theory.

In an influential article [18], based on heuristics and analogies of physical principles, Okounkov made a remarkable conjecture (see Theorem 2.1) that the Littlewood– Richardson coefficients cνλµ are log-concave in (λ, µ, ν). Although Okounkov’s conjecture is false in general [3], many consequences and interesting special cases are true. In particular, Okounkov’s conjecture implies that tensor products of finite-dimensional irreducible polynomial representations of the general linear group are log-concave, which is proved in [13] and called Schur log-concavity.

Motivated by the Schur–Weyl duality, we would like to consider the corresponding conjectures for the symmetric groups, that is, by replacing the Littlewood–Richardson

*guitao18@mails.ucas.ac.cn.

coefficients in Okounkov’s conjecture with the Kronecker coefficients. It turns out the naive analogs for Kronecker coefficients are false, but it seems that certain log-concavity properties (see conjectures 5.1, 5.2, 5.5, ?? and theorems 5.3, 5.4, 5.6) reappears for the stable tensor product of irreducible representations of symmetric groups, whose structure constants are the reduced Kronecker coefficients.

The remaining part of this article is organized as follows. In Section 2, we recall Okounkov’s conjecture on the log-concavity of the Littlewood–Richardson coefficients and some interesting implications and known special cases. In Section 3, we recall the Kronecker coefficients and discuss the convexity property of the Kronecker coefficients. In Section 4, we recall the reduced Kronecker coefficients. In Section 5, we state our conjectures and evidence on the reduced Kronecker coefficients and some implications.

### 2 Okounkov conjecture on the Littlewood–Richardson coefficients

Recall that the Littlewood–Richardson coefficients cνλµ are the structure constants of the tensor product of irreducible polynomial representations of general linear group GLn(C):

#### V(λ) ⊗ V(µ) =

ν

cνλµV(ν),

where λ, µ, and ν are partitions with lengths less than or equal to n. Okounkov made the following remarkable conjecture.

Conjecture 2.1. (Disproved; Okounkov conjecture, see [18, Conjecture 1])

The function

(λ, µ, ν) → log cνλµ

is concave. That is, suppose (λi, µi, νi) ,i = 1,2,3, are partitions such that

- 1

- 2


- 1

- 2


(λ3, µ3, ν3) , then we have

(λ1, µ1, ν1) +

(λ2, µ2, ν2) =

2µ2)2 ≥ cνλ1

1µ1cνλ3

(cνλ2

3µ3.

Okounkov’s conjecture 2.1 is a very strong statement, which holds in the “classical limit” (see [18, Section 3]), but it is refuted in general in [3]. To describe the counterexamples, we use the multiplicity/exponential notation for a partition (λ1m1, λ2m2, λ3m3 · · · , where m1 is the number of λ1 ’s, m2 is the number of λ2 ’s, etc.

- Theorem 2.2 ([3, Theorem 1.2]). Let n ⩾ 1 be an integer and let λ(n), µ(n) be two partitions defined by


λ(n) = 4n,32n,2n and µ(n) = (3n,2n,1n) . Then

n + 2 2

n + 5 5

and c22λµ((nn)),2µ(n) =

cλµ((nn)),µ(n) =

.

Consequently, when n ⩾ 21, Theorem 2.1 fails for λ1 = 2λ(n), µ1 = ν1 = 2µ(n), λ2 = λ(n), µ2 = ν2 = µ(n), λ3 = µ3 = ν3 = 0.

However, several interesting implications and special cases of Theorem 2.1 are true. First, as Okounkov observed in [18, Section 2.6], concavity of log cνλµ implies that

supp cνλµ = (λ, µ, ν), cνλµ ̸= 0

is convex. In particular, since it contains the origin (0,0,0), it is saturated. This shows that Theorem 2.1 implies the saturation property of Littlewood–Richardson coefficients1:

ckkνλ,kµ ̸= 0 for some k ≥ 1 ⇒ cνλµ ̸= 0, (2.1)

which was established before Okounkov’s conjecture by A. Knutson and T. Tao in [12] using the honeycomb model of GLn(C) tensor products.

Note that Knutson and Tao’s proof of the Saturation Conjecture implies that the

decision problem “whether cλµν > 0” is in P; as a comparison, the famous Littlewood– Richardson rule, which gives a positive combinatorial interpretation for the Littlewood–

Richardson coefficients cνλµ, shows that “computing cνλµ” is in #P (counting problems associated with the decision problems in the set NP); in fact, it is #P-complete, see [17].

Another interesting implication of Okounkov’s conjecture is also already observed by Okounkov in [18, Section 2.5]. Theorem 2.1 would have implied that for all ν,

cνλ+µ

λ+µ 2

2

≥ cνλµ, (2.2)

provided λ+2µ is an integral weight (a.k.a., a partition). It is equivalent to the inclusion of representations

⊗2

λ + µ 2

, (2.3) which can be interpreted as saying that the representation valued function

V(λ) ⊗ V(µ) ⊂ V

V : λ  → V(λ) (2.4)

1In fact, since c00,0 = 1, Theorem 2.1 implies that ckλ,kµ,kν ≤ cλ,µ,ν k .

is concave with respect to the natural ordering and tensor multiplication of representations. Since Schur polynomials are the characters of the corresponding irreducible polynomial representations of GLn(C), this remarkable implication is called Schur logconcavity and has been established by T. Lam, A. Postnikov, and P. Pylyavskyy.

- Theorem 2.3 ([13, Theorem 12], weak version). For two partitions λ and µ, suppose λ+µ has only even parts and let sλ, sµ, and sλ+µ

2

be the corresponding Schur polynomials, then s2λ+µ

2

−sλsµ is a non-negative linear combination of Schur polynomials.

Last but not least, a special but interesting case of Theorem 2.1 is recently obtained in [7]. The Kostka number Kλµ—the coefficient of monomials xµ in the Schur polynomial sλ, also known as the weight multiplicity dimV(λ)µ of the Schur module V(λ)—is a special case of the Littlewood–Richardson coefficients: we have

Kλµ = cκλν ,

where ν and κ are the partitions given by νi = ∑nj=i µj and κi = ∑nj=i+1 µj. One of the main results in [7] states that the Kostka number Kλµ is log-concave along the root directions: let ei be the i-th standard unit vector in Nm, for µ ∈ Zm and distinct i, j ∈ [m], set

µ(i, j) = µ + ei − ej, then the sequence of weight multiplicities of V(λ) we encounter is always log-concave if we walk in the weight diagram along any root direction ei − ej.

- Theorem 2.4 ([7, Theorem 2]). For any partition λ and any µ ∈ Nm, we have Kλµ2 ⩾ Kλµ(i,j)Kλµ(j,i) for any i, j ∈ [m].


### 3 Kronecker Coefficients and Their Convexity Property

Recall that the Kronecker coefficients gλµν are the structure constants of the tensor product (Kronecker product) of irreducible representations of the symmetric group Sd:

Vλ ⊗ Vµ =

ν

gλµν Vν,

where λ, µ and ν are partitions of d. They were introduced by Murnaghan in 1938 and they play an important role algebraic combinatorics and geometric complexity theory.

By the representation theory of finite groups, these coefficients can be computed as

1

n! ∑

gλµν =

χλ(σ)χµ(σ)χν(σ),

σ∈Sd

where χλ(σ) is the character value of the irreducible representation corresponding to partition λ on a permutation σ ∈ Sd. Since irreducible representations of the symmetric group Sd have integral character values, the Kronecker coefficient gλµν is invariant under permutations of the three partitions. This should be compared with Littlewood– Richardson coefficients cνλµ, where it is only invariant under transposition of λ and µ.

The Kronecker coefficients are very different beasts from their cousins Littlewood– Richardson coefficients. For example, computing Kronecker coefficients is #P-hard and contained in GapP [2]. A recent work [8] shows that the decision problem “whether gµνλ > 0” is NP-hard. They lack “nice” formulas and what we can hope is to understand their asymptotic behavior in various regimes and inequalities they could satisfy. Finding a combinatorial interpretation for them has been described by Richard Stanley as “one of the main problems in the combinatorial representation theory of the symmetric group”.

Let us now only focus on one particular aspect—the convexity property of the Kronecker coefficient. The verbatim translation of the saturation property (2.1) that holds for the Littlewood–Richardson coefficients is known to be false for the Kronecker coefficients

[1]. The simplest counterexample might be g((1,11,1)() 1,1) = 0 but g((2,22,2)() 2,2) = 1. Indeed,

g((NN,,NN)),(N,N) =

- 0 for odd N,
- 1 for even N.


Additionally, the verbatim translation of the property (2.2) or equivalently the property (2.3) that holds for the Littlewood–Richardson coefficients is also false for the Kronecker coefficients. One can locate a counterexample

V⊗2

3,3,1,1 − V4,4 ⊗ V2,2,2,2 = V8 + 3V6,2 + V7,1 + V2,2,2,2 + V2,2,2,1,1 + V2,2,1,1,1,1 − V1,1,1,1,1,1,1,1 + 5V4,2,2 + 3V5,1,1,1 + 5V5,2,1 + 6V4,2,1,1 + 5V3,2,2,1 + 3V4,1,1,1,1 + 5V3,2,1,1,1 + 2V3,1,1,1,1,1 + V6,1,1 + 2V5,3 + V4,4 + 5V4,3,1 + 2V3,3,2 + 4V3,3,1,1

(3.1)

in the ring of virtual representations of S8. The triple of partitions (6,4), (2,2,2,2,2) and (4,3,1,1,1) is a counterexample for S10 and there are many more counterexamples for S12.

Nevertheless, we conjecture that the verbatim translation of the property (2.2) or equivalently the property (2.3) that holds for the Littlewood–Richardson coefficients is also true for another closely related structure constant—the reduced Kronecker coefficients.

### 4 Reduced Kronecker Coefficients

For λ a partition and d ≥ |λ| + λ1, the “padded” partition λ[d] is defined as (d − |λ|, λ), which is a partition of size d with a “very long top row”.

It was noticed by Murnaghan in [16] that the sequence gλν[[dd]],µ[d]

stabilizes and the stable value of the sequence was called the reduced (or stable) Kronecker coefficient g¯λµν

d>>0

associated with the triple (λ, µ, ν). Given λ and µ, only finitely many g¯λµν are nonzero. Moreover, g¯λµν = 0 unless the Murnaghan–Littlewood inequality holds:

#### |ν| ≤ |µ| + |λ|, |µ| ≤ |λ| + |ν|, |λ| ≤ |µ| + |ν|.

In contrast to Kronecker coefficients, reduced Kronecker coefficients are defined for any triple of partitions (not necessarily of the same size) and in general, there is no relationship between λ, µ, and ν. However, surprisingly, when |ν| = |λ| + |µ|, the reduced Kronecker coefficient g¯λµν recovers the Littlewood–Richardson coefficient cνλµ!

Theorem 4.1 (Murnaghan–Littlewood theorem, see [14]). If |ν| = |λ| + |µ|, then the reduced Kronecker coefficient g¯λµν is equal to the Littlewood–Richardson coefficients cνλµ: g¯λµν = cνλµ.

Additionally, every Kronecker coefficient is equal to an explicit reduced Kronecker coefficient of not much larger partitions (see [9, Theorem 1.1]).

We would like to ask which convexity/concavity property could be satisfied by the reduced Kronecker coefficients. Whether the verbatim translation of the saturation property (2.1) that holds for the Littlewood–Richardson coefficients is also true for the reduced Kronecker coefficients is a long-standing open problem. It was independently conjectured in 2004 by Kirillov (who called them the extended Littlewood–Richardson coefficients) and Klyachko.

- Conjecture 4.2 (Disproved; Kirillov–Klyachko generalized saturation conjecture, see [10, Conjecture 2.33] and [11, Conjecture 6.2.4]). The reduced Kronecker coefficients satisfy the saturation property:

g¯kkλν,kµ ̸= 0 for some k ≥ 1 ⇒ g¯λµν ̸= 0. (4.1) However, this conjecture is recently refuted in general in [19]:

- Theorem 4.3 ([19, Theorem 2]). For all k ≥ 3, the triple of partitions 1k2−1,1k2−1, kk−1 is a


counterexample to Theorem 4.2. Moreover, for every partition γ s.t. γ2 ≥ 3, there are infinitely many pairs (a, b) ∈ N2 for which the triple of partitions ab, ab, γ is a counterexample to

- Theorem 4.2.


5 Log-concavity Conjectures of Stable Tensor Product of Irreducible Representations of Symmetric Groups

One main contribution of this article is the following conjecture.

- Conjecture 5.1. The reduced Kronecker coefficients satisfy the following inequality: given λ and µ, then for all ν, we have


g¯νλ+µ

≥ g¯λµν , (5.1) provided λ+2µ is still a partition.

λ+µ 2

2

We tested the above statement for all partitions λ and µ with at most 11 boxes. We want an equivalent version of the above conjecture akin to (2.3), which can be

formulated by using the stable representation category of the symmetric group in [22].

Consider the natural embedding Sd → Sd+1 by permuting the first d natural numbers. Let S∞ := d⩾0 Sd be the limit, which is the group of permutations of N that fix all but finitely many numbers. The group S∞ has a natural action on V = C∞ by permuting the basis vectors {ei}i∈N. Sam and Snowden considered the category Rep(S∞) of algebraic representations of S∞, where a representation of S∞ is called algebraic if it appears as a subquotient of a direct sum of some tensor product of V. They proved the following:

- • Rep(S∞) is an abelian C-linear symmetric monoidal category but is not semisimple;
- • Simple objects Vλ[∞] in Rep(S∞) are one-to-one correspondent to the partition λ of arbitrary size;
- • Every object in Rep(S∞) has finite length;
- • The structure constants of the Grothendieck ring K(Rep(S∞)) are the reduced Kronecker coefficients:


g¯λν,µ = Vλ[∞] ⊗ Vµ[∞] : Vν[∞] .

Therefore, the category Rep(S∞) seems to be a natural categorical home of reduced Kronecker coefficients. Let us say that two objects X and Y in Rep(S∞) satisfy X ≥ Y in the Grothendieck ring K(Rep(S∞)) if [X]−[Y] in K(Rep(S∞)) can be expanded in Vλ[∞]’s with nonnegative coefficients. Then, our conjecture 5.1 is equivalent to the following

Conjecture 5.2 (Restatement of Theorem 5.1). The representation valued function

V : P → Rep (S∞) λ  −→ Vλ[∞]

(5.2)

is concave with respect to the natural ordering and tensor products of representations. That is, V⊗2

≥ Vλ[∞] ⊗ Vµ[∞] in the Grothendieck ring K(Rep(S∞)), (5.3)

λ+µ

2 [∞]

provided λ+2µ is still a partition.

In this form, the log-concavity of (2.3) can be seen as a degeneration and a special case of (5.3) by virtue of the Murnaghan–Littlewood theorem (Theorem 4.1); see also [22, Section 8.7]. Additionally, the conjecture predicts that if we pass to infinity, the mysterious minus sign in (3.1) disappears2, and we obtain log-concavity in the limit, which fits well with the conjectures and results in [15, 6].

Using Theorem 2.3, we have the following log-concavity property of the dimensions of representations in (5.3). It greatly generalizes [5, Theorem 1.1 (1)].

2Note that there is no “sign” representation in Rep(S∞).

##### Theorem 5.3. We have

2

≥ dimVλ[d] × dimVµ[d] (5.4) for d ≥ max{|λ| + λ1, |µ| + µ1}. In another form, we have

dimVλ+µ

2 [d]

2

λ+µ

≥ fλ[d] × fµ[d], (5.5) where fλ denotes the number of standard Young tableaux of shape λ. Proof. First, note that λ[d]+2µ[d] = λ+2µ[d] under the condition d ≥ max{|λ| + λ1, |µ| + µ1}. Let sλ denote the Schur function of shape λ. By Theorem 2.3, we have

2 [d]

f

s2λ+µ

2 [d] − sλ[d] × sµ[d] ≥s 0, (5.6) which means the left-hand side is a nonnegative linear combination of Schur functions. Let Λ = ⊕n≥0ΛQn be the algebra of symmetric functions. Then, we have the exponential specialization ex1, which is an algebra homomorphism ex1 : Λ → Q, and

fλ |λ|!

,

ex1 (sλ) =

see, for example, [23]. Applying the exponential specialization ex1 to (5.6)), we obtain (5.5), which is well-known equivalent to the inequality (5.4). The proof is completed.

| |
|---|


Using the existing combinatorial interpretation of Kronecker coefficients with two two-row partitions, we can prove the following

- Theorem 5.4. Theorem 5.1, or equivalently, Theorem 5.2, holds when partitions λ and µ are both one part. Actually, we have the following stronger inequalities: for all partition ν,


g¯(νj)(k) ≥ g¯(νi)(l), (5.7) whenever i < j ≤ k < l with j + k = i + l.

Proof. First, we have g¯(νj),(k) = g(νj[)[n]n],(k)[n] and g¯(νi),(l) = g(νi[)[n]n],(l)[n] for n sufficiently large. It is well known that gλµν = 0 when λ and µ are both two-row partitions but ν has more than 4 parts. Therefore, we assume ν[n] = (ν1, ν2, ν3)[n]. By [21, Theorem 1], we have

g¯(νj[)[n]n],(k)[n] =Γ (ν2 + ν3, ν1 − ν2, ν1 + ν3 + 1, ν2 − ν3) (j, k + 1)

− Γ (ν2 + ν3, ν1 − ν2, n − ν1 − ν2 + 2, ν2 − ν3) (j, k + 1), g¯(νi[)[n]n],(l)[n] =Γ (ν2 + ν3, ν1 − ν2, ν1 + ν3 + 1, ν2 − ν3) (i, l + 1)

− Γ (ν2 + ν3, ν1 − ν2, n − ν1 − ν2 + 2, ν2 − ν3) (i, l + 1),

(5.8)

where Γ(a, b, c, d)(x, y) := (u, v) ∈ R ∩ N2 : (x, y) ⇝ (u, v) . Here, R is the rectangle with vertices (a, c), (a + b, c), (a, c + d), and (a + b, c + d), and (x, y) ⇝ (u, v) means (u, v) can be reached from (x, y) by moving any number of steps south west or north west. Let n be large enough (that is, we pull up the rectangle R to live very high) such that both minus terms in (5.8) are 0. Then, it is clear from the definition that

Γ (ν2 + ν3, ν1 − ν2, ν1 + ν3 + 1, ν2 − ν3) (j, k + 1)

≥ Γ (ν2 + ν3, ν1 − ν2, ν1 + ν3 + 1, ν2 − ν3) (i, l + 1), since (i, l + 1) is in the northwest of (j, k + 1). Therefore, we have

g¯(νj)(k) = g(νj[)[n]n],(k)[n] ≥ g(νi[)[n]n],(l)[n] = g¯(νi)(l).

| |
|---|


Let us now discuss a conjecture related to Theorem 5.2. For two partitions λ and µ, let λ ∪ µ = (ν1, ν2, ν3, . . .) be the partition obtained by rearranging all parts of λ and µ in the weakly decreasing order. Let sort1(λ, µ) := (ν1, ν3, ν5, . . .) and sort2(λ, µ) := (ν2, ν4, ν6, . . .). Then, we have the following conjecture, which generalizes the conjecture of Fomin, Fulton, Li, and Poon in [4, Conjecture 2.7].

Conjecture 5.5. For two partitions λ and µ, we have

Vsort1(λ,µ)[∞] ⊗ Vsort2(λ,µ)[∞] ≥ Vλ[∞] ⊗ Vµ[∞] in the Grothendieck ring K(Rep(S∞)).

As observed in [13], Theorem 5.5 is related to Theorem 5.2 by conjugating the shapes. However, since we have to add a “very long top row”, Theorem 5.5 can not be directly deduced from (even a stronger version of) Theorem 5.2, unlike the case in [13]. Indeed, we can not even prove the following inequality for dimensions of representations

fsort1(λ,µ)[d] × fsort2(λ,µ)[d] ≥ fλ[d] × fµ[d] for d ≥ max{|λ| + λ1, |µ| + µ1} (5.9)

by directly using results in [13]. Nevertheless, using the existing combinatorial interpretation of Kronecker coefficients with two hook-shape partitions, we have the following

- Theorem 5.6. Theorem 5.5 holds when partitions λ and µ are both one column. Actually, we have the following stronger inequalities


g¯(ν1j)(1k) ≥ g¯(ν1i)(1l), for all partition ν, (5.10) whenever i < j ≤ k < l with j + k = i + l.

Proof. First, we have g¯(ν1j)(1k) = g(ν1[nj)[] n],(1k)[n] and g¯(ν1i)(1l) = g(ν1[ni)[] n],(1l)[n] for n sufficiently large. By [21, Theorem 3], the only possible values for these Kronecker coefficients are 0, 1 or 2. We use the following notation

#### ((P)) =

1, if proposition P is true, 0, otherwise.

We have the following 4 cases:

- 1. If ν[n] is one-row (i.e. ν = ∅), then g(ν1[nj)[] n],(1k)[n] = δj,k, g(ν1[ni)[] n],(1l)[n] = δi,l.
- 2. If ν[n] is not contained in a double hook, then g(ν1[nj)[] n],(1k)[n] = g(ν1[ni)[] n],(1l)[n] = 0.
- 3. Let ν[n] = 1d12d2n3n4 be a double hook. Let x = 2d2 + d1. Then,

g(ν1[nj)[] n],(1k)[n] = n3 − 1 ≤

j + k − x 2 ≤ n4 ((|k − j| ≤ d1))

+ n3 ≤

j + k − x + 1

2 ≤ n4 ((|k − j| ≤ d1 + 1)) g(ν1[ni)[] n],(1l)[n] = n3 − 1 ≤

i + l − x 2 ≤ n4 ((|l − i| ≤ d1))

+ n3 ≤

i + l − x + 1

2 ≤ n4 ((|l − i| ≤ d1 + 1)) . Note that if n4 = 0, then we shall rewrite ν[n] = 1d12d2−12n3 .

- 4. Let ν[n] = 1dw be a hook shape. Let n be sufficiently large. Then,


#### g(ν1[nj)[] n],(1k)[n] = ((j ≤ d + k))((d ≤ j + k))((k ≤ j + d)), g(ν1[ni)[] n],(1l)[n] = ((i ≤ d + l))((d ≤ i + l))((l ≤ i + d)).

It is not hard to see that (5.10) holds in any case, which easily implies Theorem 5.5 when partitions λ and µ are both one column. The proof is completed.

| |
|---|


We note that inequality (5.7) and inequality (5.10) show a beautiful symmetry that is not transparent if we do not remove the “very long top rows”.

Theorem 5.5 is useful. For example, it implies that the intersection cohomology of the symmetric reciprocal plane Xn (see in [20, Theorem 1.2]) is equivariant log-concave at degree i as a graded representation of the symmetric group Sn for n large enough.

We note that Conjectures 5.2 and 5.5 can also be formalized as Schur positivity conjectures using the Schur functions and the Kronecker (internal) product between them, provided that the related partitions all have “long enough top rows”. These conjectures could also be formalized using the Deligne category or partition algebra, which might shed some

light on these conjectures. However, due to the lack of general knowledge of the (reduced) Kronecker coefficients, proving these conjectures, in general, seems to be beyond the reach of existing technology.

As informed by Mike Zabrocki, Conjectures 5.1 is false. The first counterexamples that he found are partitions λ and µ with 12 boxes: all of g4422,4422λ for λ in {(116), (115), (2,114), (3,114), (2,2,113)} are equal to 0, while g5511,3333λ are all greater than 0 (in fact they are 1,2,3,1,1, respectively). Those are the only examples where the conjecture fails for two partitions of 12. The fact that Conjecture 5.1 first fails for |λ| = |µ| = 12 is somewhat surprising. It is interesting to see whether one can revise or refine the conjecture.

### Acknowledgements

The author is very grateful to Mike Zabrocki for finding and telling him the counterexamples. The author would like to thank Brendon Rhoades, Peng Shan, and Arthur L. B. Yang for helpful discussions and is especially grateful to Matthew H.Y. Xie for the help with the computer computations of tensor product multiplicities. The author also thanks the anonymous referees for the comments and suggestions.

### References

- [1] E. Briand, R. Orellana, and M. Rosas. “Reduced Kronecker coefficients and counter– examples to Mulmuley’s strong saturation conjecture SH”. Computational Complexity 18.4

(2009), pp. 577–600.

- [2] P. Bürgisser and C. Ikenmeyer. “The complexity of computing Kronecker coefficients”. Discrete Mathematics and Theoretical Computer Science. Discrete Mathematics and Theoretical Computer Science. 2008, pp. 357–368.
- [3] C. Chindris, H. Derksen, and J. Weyman. “Counterexamples to Okounkov’s log-concavity conjecture”. Compositio Mathematica 143.6 (2007), pp. 1545–1557.
- [4] S. Fomin, W. Fulton, C.-K. Li, and Y.-T. Poon. “Eigenvalues, singular values, and LittlewoodRichardson coefficients”. American Journal of Mathematics 127.1 (2005), pp. 101–127.
- [5] A. L. L. Gao, M. H. Y. Xie, and A. L. B. Yang. “Schur positivity and log-concavity related to longest increasing subsequences”. Discrete Math. 342.9 (2019), pp. 2570–2578.
- [6] T. Gui. “On the equivariant log-concavity for the cohomology of the flag varieties”. 2022. arXiv:2205.05408.
- [7] J. Huh, J. P. Matherne, K. Mészáros, and A. St. Dizier. “Logarithmic concavity of Schur and related polynomials”. Trans. Am. Math. Soc. 375.6 (2022), pp. 4411–4427. doi.


- [8] C. Ikenmeyer, K. D. Mulmuley, and M. Walter. “On vanishing of Kronecker coefficients”. Computational Complexity 26.4 (2017), pp. 949–992.
- [9] C. Ikenmeyer and G. Panova. “All Kronecker coefficients are reduced Kronecker coefficients”. 2023. arXiv:2305.03003.
- [10] A. N. Kirillov. “An invitation to the generalized saturation conjecture”. Publications of the Research Institute for Mathematical Sciences 40.4 (2004), pp. 1147–1239.
- [11] A. Klyachko. “Quantum marginal problem and representations of the symmetric group”.

2004. arXiv:preprint quant-ph/0409113.

- [12] A. Knutson and T. Tao. “The honeycomb model of GLn(C) tensor products I: Proof of the saturation conjecture”. Journal of the American Mathematical Society 12.4 (1999), pp. 1055– 1090.
- [13] T. Lam, A. Postnikov, and P. Pylyavskyy. “Schur positivity and Schur log-concavity”. American Journal of Mathematics 129.6 (2007), pp. 1611–1622.
- [14] D. E. Littlewood. “Products and plethysms of characters with orthogonal, symplectic and symmetric groups”. Canadian Journal of Mathematics 10 (1958), pp. 17–32.
- [15] J. P. Matherne, D. Miyata, N. Proudfoot, and E. Ramos. “Equivariant Log Concavity and Representation Stability”. International Mathematics Research Notices (2021).
- [16] F. D. Murnaghan. “The analysis of the Kronecker product of irreducible representations of the symmetric group”. American Journal of Mathematics 60.3 (1938), pp. 761–784.
- [17] H. Narayanan. “On the complexity of computing Kostka numbers and Littlewood-Richardson coefficients”. Journal of Algebraic Combinatorics 24.3 (2006), pp. 347–354.
- [18] A. Okounkov. “Why would multiplicities be log-concave?” The orbit method in geometry and physics. Springer, 2003, pp. 329–347.
- [19] I. Pak and G. Panova. “Breaking down the reduced Kronecker coefficients”. Comptes Rendus. Mathématique 358.4 (2020), pp. 463–468.
- [20] N. Proudfoot, M. Wakefield, and B. Young. “Intersection cohomology of the symmetric reciprocal plane”. Journal of Algebraic Combinatorics 43.1 (2016), pp. 129–138.
- [21] M. H. Rosas. “The Kronecker product of Schur functions indexed by two-row shapes or hook shapes”. Journal of Algebraic Combinatorics 14.2 (2001), pp. 153–173.
- [22] S. V. Sam and A. Snowden. “Stability patterns in representation theory”. Forum of Mathematics, Sigma. Vol. 3. Cambridge University Press. 2015.
- [23] R. P. Stanley. Enumerative combinatorics. Volume 2. Vol. 62. Camb. Stud. Adv. Math. Cambridge: Cambridge University Press, 1999.


