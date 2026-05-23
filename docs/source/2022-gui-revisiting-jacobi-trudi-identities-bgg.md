---
type: source
kind: paper
title: Revisiting Jacobi-Trudi identities via the BGG category $\mathcal{O}$
authors: Tao Gui, Arthur L. B. Yang
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2209.12632v3
source_local: ../raw/2022-gui-revisiting-jacobi-trudi-identities-bgg.pdf
topic: general-knowledge
cites:
---

arXiv:2209.12632v3[math.RT]9Nov2024

REVISITING JACOBI–TRUDI IDENTITIES VIA THE BGG CATEGORY O

TAO GUI AND ARTHUR L. B. YANG

Abstract. By interpreting Kostka numbers as tensor product multiplicities in the BGG category O for the special linear Lie algebras, we provide a new proof of the classical Jacobi–Trudi identities for skew Schur polynomials, derived from the celebrated Weyl character formula. We re-establish the Schur positivity of certain truncations in the Jacobi–Trudi expansion of skew Schur polynomials and obtain Schur positivity results for similar truncations in the Jacobi–Trudi-type expansion of the product of two Schur polynomials. Furthermore, we interpret the coeﬃcients in the Schur polynomial expansions of these Jacobi–Trudi truncations as tensor product multiplicities in the BGG category O.

1. Introduction

Many open problems in symmetric function theory are related to the Schur positivity questions, that is, showing that certain symmetric functions can be expressed as non-negative linear combinations of Schur functions; see, for example, [5, 7, 8, 11, 15]. For our purpose here, we only need to consider Schur polynomials, which are obtained from Schur functions by reducing the number of variables. The signiﬁcance of Schur positivity stems from the fact that Schur polynomials not only have interesting combinatorial interpretations but also admit natural algebraic or geometric meanings. In combinatorics, Schur polynomials can be deﬁned as generating functions of weighted semi-standard Young tableaux. In representation theory, they appear as characters of ﬁnite-dimensional irreducible polynomial representations (known as Schur modules) of the general linear groups GLn(C), as well as Frobenius images of irreducible representations of the symmetric group. The relationship between Schur polynomials and representation theory was discovered by Schur, hence these important polynomials are named after him. In geometry, Schur polynomials appear as the cohomology classes of the Schubert cycles of the corresponding Grassmannian. For more information on Schur polynomials, we refer the reader to [6,13,16]. Due to these connections, whether a particular symmetric polynomial can be expanded positively in terms of Schur polynomials is of particular interest in symmetric function theory, representation theory, and classical Schubert calculus.

The main objective of this paper is to study the Schur positivity of certain truncations of the Jacobi–Trudi expansion of skew Schur polynomials and the Jacobi– Trudi-type expansion of the product of two Schur polynomials. For ordinary partitions, this positivity can be implied by the existence of a conjectural resolution (due to Lascoux [12]) of irreducible polynomial representations of GLn(C), which

![image 1](<2022-gui-revisiting-jacobi-trudi-identities-bgg_images/imageFile1.png>)

Key words and phrases. Jacobi–Trudi identity, Schur positivity, Kostka number, BGG category O, Weyl character formula, BGG resolution.

1

was later constructed by Akin[1] and Zelevinskii[17] independently. Zelevinskii’s approach could also handle the case of skew partitions. However, it is an open problem to give a combinatorial interpretation of these non-negative coeﬃcients in these Schur polynomial expansion[16, p.461]. By the work of Akin and Zelevinskii, one can interpret these coeﬃcients as multiplicities of irreducible representations of some polynomial representation of GLn(C). Using the classical BGG resolution and techniques from the BGG category O of the special linear Lie algebras sln(C), we can prove the Schur positivity for the case of skew partitions and for the case of products. We interpret these coeﬃcients as tensor product multiplicities in the BGG category O of sln(C), thus providing a new algebraic interpretation.

In order to state our results explicitly, let us now recall some related deﬁnitions and results. We will adopt the terminology and notation of symmetric functions in [16]. An integer partition λ of a positive integer d, denoted by λ ⊢ d, is a weakly decreasing sequence (λ1,λ2,...,λn) of non-negative integers such that |λ| := ni=1 λi = d. For each partition λ, let mλ, hλ, sλ denote the corresponding monomial symmetric polynomial, the complete symmetric polynomial, and the Schur polynomial, respectively. It is known that each of {mλ |λ ⊢ d}, {hλ |λ ⊢ d}, and {sλ |λ ⊢ d} is a basis of the space of homogeneous symmetric polynomials of degree d. Here we adopt the deﬁnition of the Schur polynomial sλ given by

- (1.1) sλ := µ

Kλ,µmµ,

where each Kλ,µ, called the Kostka number, is equal to the number of semistandard Young tableaux of shape λ and type µ.

If µ,ν are two partitions of length at most n such that µi ≥ νi for each i, then one can deﬁne a skew partition µ/ν. Let sµ/ν denote the corresponding skew Schur polynomial indexed by µ/ν, which can be deﬁned by the property

- (1.2) sµ/ν,sλ = sµ,sλsν ,

where the scalar product is deﬁned by claiming that Schur polynomials form an orthonormal basis. The classical Jacobi–Trudi identity states that

- (1.3) sµ/ν = det hµ

i−νj−i+j

n i,j=1 ,

where we set h0 = 1 and hk = 0 for k < 0. There is also a Jacobi–Trudi-type identity for the product of two Schur polynomials :

- (1.4) sµsν = det hµ


n i,j=1 ,

i+νn+1−j−i+j

see [13, Examples 3.8, pp. 46-47].

There are several proofs of the Jacobi–Trudi identity. The classical combinatorial proof is by relating the semi-standard Young tableaux with non-intersection lattice paths and then using the Lindstr¨m–Gessel–Viennot lemma; see [14, Section 4.5], or the ﬁrst proof of [16, Theorem 7.16.1]. A purely algebraic proof can also be given; see [13, Section 1.3], or the second proof of [16, Theorem 7.16.1]. Since Schur polynomials also appear as characters of Schur modules of the general linear groups, the alternating sum format of the spanning of the right hand side determinant in

- (1.3) resembles an Euler–Poincare´ characteristic, so it is natural to ask whether there is a resolution of Schur modules to realize the identity (1.3) at least for the case of ν = ∅. The existence of such a resolution was conjectured by Lascoux [12] and was later constructed by Akin in [1–3] and independently by Zelevinskii in [17].


The existence of such a resolution has the following implication, see [16, Exercise 7.38].

- Theorem 1 (Akin–Zelevinskii theorem). For 0 ≤ k ≤ n2 , the symmetric polynomial

(1.5) gµ/νk = (−1)k

w∈Sn,ℓ(w)≥k

(−1)ℓ(w)hµ+δ−w(ν+δ),

a truncation of the Jacobi–Trudi expansion of sµ/ν, is Schur positive, where µ and ν are partitions of length at most n, ℓ(w) is the number of inversions of the

permutation w ∈ Sn, and δ = (n − 1,n − 2,...,1,0).

In this paper, We provides a new proof of the above theorem via the BGG category O of sln(C). Using the duality of ﬁnite dimensional simple modules, we prove the following result.

- Theorem 2. With the same notations as in the above theorem, for 0 ≤ k ≤ n2 , the symmetric polynomial

(1.6) tkµ,ν = (−1)k

w∈Sn,ℓ(w)≥k

(−1)ℓ(w)hµ+δ+w(w

0ν−δ),

a truncation of the following Jacobi–Trudi-type expansion of sµsν, is Schur positive, where w0 is the longest element of Sn.

Actually, we give a following new interpretation of the coeﬃcients in the Schur

polynomial expansion of gµ/νk and tkµ,ν via the BGG category O of sln(C), which in turn leaves the above two theorems as immediate corollaries.

- Theorem 3. For 0 ≤ k ≤ n2 , we have


- (1.7) gµ/νk = λ

[L(λ) ⊗ V (ν,k) : L(µ)]sλ, and

- (1.8) tkµ,ν = λ

[L(λ) ⊗ V (−w0ν,k) : L(µ)]sλ,

where L(λ) (and L(µ), respectively) denotes the simple module of highest weight λ (and µ, respectively) of the special linear Lie algebra sln(C), V (ν,k) is the image of the boundary map dk in the BGG resolution of L(ν):

- (1.9) 0 → C(ν


d(

2) −→ C(ν

n

)−1 → ··· → C1ν −→d1 C0ν −→d0 L(ν) → 0,

)

n 2

n 2

V (−w0ν,k) is similarly the image of a boundary map in the BGG resolution of L(−w0ν) and the bracket denotes the composition factor multiplicity in the BGG category O.

Our approach is diﬀerent in the sense that we transform the Schur positivity problem into the positivity problem of a virtual character in the BGG category O and then use classical BGG resolution to prove the positivity. It also allows us to give a new proof of the Jacobi–Trudi identity (1.3). Actually, we can derive it from the Weyl character formula, as illustrated in subsequent sections.

We observed that truncations of the Jacobi–Trudi expansion of a skew Schur polynomial seem to share similar convexity of Schur polynomials, see [9]. Speciﬁcally, with Candice X. T. Zhang, we have checked that for partitions µ and ν with |µ| + |ν| ≤ 9, all normalized truncations of the Jacobi–Trudi expansion of a skew Schur polynomial gµ/νk are Lorentzian. It would be interesting to see whether our approach can be used to understand the Lorentzian property for the skew Schur polynomials, see [9, Conjecture 19].

The remaining part of this paper is organized as follows. In Section 2, we provide preliminary results on the BGG category O and the classical BGG resolution. In Section 3, we ﬁrst give a new interpretation of Kostka numbers in the BGG category O, and then leave the world of symmetric functions and use Verma module characters to prove the Jacobi–Trudi identity and Theorem 3.

2. Preliminaries

In this section, we recall the relevant representation theory of complex semisimple Lie algebras. For a more detailed background, we refer the reader to the comprehensive reference [10].

- 2.1. The BGG category O. Let g be a ﬁnite-dimensional complex semi-simple Lie algebra (for our application, g = sln(C)). We ﬁx a Cartan decomposition g = n− ⊕ h ⊕ n+. (In the case of g = sln(C), we could choose n+ and n− to be the strictly upper-triangular and strictly lower-triangular matrices, respectively, and h to be the diagonal matrices.) We consider the Bernstein–Gelfand–Gelfand category O, which is a full subcategory of ModU(g) (the category of left-modules of the enveloping algebra of g). Each object of O is a module M satisfying the following three conditions:


- (O1) M is a ﬁnitely generated U(g)-module.
- (O2) M is h-semi-simple, that is, M is a weight module: M = λ∈h∗ Mλ, where Mλ = {m ∈ M : h · m = λ(h)m for all h ∈ h}.
- (O3) M is locally n+-ﬁnite, that is, for each v ∈ M, the subspace U(n+)·v of M is ﬁnite-dimensional.


For example, all ﬁnite-dimensional modules lie in O. It follows from the axioms that all weight spaces of M ∈ O are ﬁnite-dimensional. Thus one could deﬁne the (formal) character of M ∈ O by

dim (Mλ)xλ,

ch(M) =

λ

where the symbols xλ denote formal exponentials, multiplying by the rule xλxµ = xλ+µ. Furthermore, if M ∈ O and L is ﬁnite-dimensional, then L ⊗ M ∈ O and ch(L ⊗ M) = chL chM.

For each λ ∈ h∗, there is a one-dimensional representation Cλ of b := h ⊕ n+, where h acts via λ and n+ acts by zero. Now consider the Verma (or standard) module ∆(λ), deﬁned as ∆(λ) := U(g) ⊗U(b) Cλ, where U(g) and U(b) are the universal enveloping algebras of g and b, respectively. It can be proved that simple objects L(λ) (simple highest weight module) in O are parametrized by λ ∈ h∗ and can be uniformly constructed as the unique simple quotient of the corresponding ∆(λ).

Since each M ∈ O is both artinian and noetherian, it follows that M possesses a composition series with simple quotients isomorphic to various L(λ). The multiplicity of L(λ) in M is independent of the choice of composition series and is denoted by [M : L(λ)]. It is known that category O is an abelian category and if 0 → M′ → M → M′′ → 0 is a short exact sequence in O, then chM = chM′ + chM′′. Thus any chM is determined uniquely by the formal characters of the composition factors of M, taken with multiplicity.

- 2.2. Weyl character formula and BGG resolution. One of the basic questions in the representation theory of the complex semi-simple Lie algebra g is to compute the character of L(λ). Those L(λ) with λ dominant and integral are precisely all the ﬁnite-dimensional simple modules of g, and the characters are given by the celebrated Weyl character formula 1


(−1)ℓ(w)xw(λ+ρ) w∈W(−1)ℓ(w)xw(ρ)

- (2.1) chL(λ) = w∈W


,

![image 2](<2022-gui-revisiting-jacobi-trudi-identities-bgg_images/imageFile2.png>)

where W is the Weyl group, and ρ is the Weyl vector, deﬁned as half the sum of positive roots. For g = sln(C), the Weyl group W is the permutation group Sn, and ρ corresponds to the partition δ = (n − 1,n − 2,...,1,0). It can be implied from the Weyl character formula that the dual space L(λ)∗, with the standard action (x · f)(v) = −f(x · v) for x ∈ g,v ∈ L(λ),f ∈ L(λ)∗, is isomorphic to L (−w0λ) (where w0 ∈ W is the longest element).

In terms of characters of Verma modules, the Weyl character formula is equivalent to

- (2.2) chL(λ) = w∈W

(−1)ℓ(w) ch∆(w · λ),

where the dot action is deﬁned as w·λ = w(λ+ρ)−ρ, in other words, this shifts the standard action of W to have center −ρ, and the characters of the Verma modules are given by

- (2.3) ch(∆(λ)) = xλ/ 1 − x−α ,

where α ranges over all positive roots of the complex semi-simple Lie algebra g.

In a classical paper [4], Bernstein, Gelfand and Gelfand studied the Weyl character formula and constructed a resolution of L(λ) for λ dominant and integral to realize the alternating sum in the Weyl character formula (2.2) as an Euler– Poincar´e characteristic of a complex, which is now known as the BGG resolution. Speciﬁcally, they proved the following theorem.

Theorem 4. [4, Theorem 10.1] Let λ be a dominant and integral weight and L(λ) be the irreducible ﬁnite-dimensional g-module with highest weight λ. Then there exists an exact sequence of g-modules

- (2.4) 0 → C(λn


d(

2) −→ C(λn

n

)−1 → ··· → C1λ −→d1 C0λ −→d0 L(λ) → 0, where Ckλ = w∈W,ℓ(w)=k ∆(w · λ).

)

2

2

![image 3](<2022-gui-revisiting-jacobi-trudi-identities-bgg_images/imageFile3.png>)

1It is easy to see that Cauchy’s bialternant formula for the Schur polynomial sλ (x1, x2, . . . , xn) = det xλj i+n−i / det xnj −i , where λ = (λ1, λ2, . . . , λn) is a partition, is a special case of the Weyl character formula for g = sln(C) and W = Sn.

For general λ ∈ h∗, it is not hard 2 to show that b(λ,w)ch ∆(w · λ) with b(λ,w) ∈ Z and b(λ,λ) = 1,

- (2.5) chL(λ) = w·λ≤λ


where the partial ordering is deﬁned by µ ≤ λ if and only if λ−µ is a non-negative linear combination of simple roots. That is, b(λ,w) is uni-triangular with respect to the partial ordering. It follows that formal characters chL(λ) with λ ∈ h∗ are linearly independent and form a Z-basis of the additive group generated by all ch∆(λ), while formal characters of Verma modules provide an alternative Z-basis. The multiplicity [M : L(λ)] of L(λ) in M is equal to the coeﬃcient of chL(λ) in the expansion of chM in terms of irreducible characters.

3. Proofs of the Main results

The purpose of this section is two-fold: ﬁrst, we give a new proof of the Jacobi– Trudi identity, and secondly, we use BGG resolution to prove Theorem 3.

Our approach given here relies on an interpretation of the Kostka numbers as tensor product multiplicities in the BGG category O of sln(C). Note that

- (3.1) hτ = λ


Kλ,τsλ,

which is equivalent to the deﬁnition (1.1) of the Schur polynomial, see [6, Section 6.1]. On the other hand, since the Schur polynomial sλ is the character of the ﬁnite-dimensional irreducible polynomial representation Vλ (the Schur module) of GLn(C), by restricting to the special linear group SLn(C) and diﬀerentiating, it is also the formal character of the simple module L(λ) of the special linear Lie algebra sln(C), namely,

- (3.2) chL(λ) = sλ, for λ dominant and integral, i.e., λ is a partition.

It follows that the Kostka number Kλ,τ is also the weight multiplicity of τ in L(λ), namely,

- (3.3) Kλ,τ = dim(L(λ)τ),

where λ is a partition, regarded as a dominant weight of sln(C), and τ is any sequence (τ1,...,τn) ∈ Zn with |λ| = |τ|. By the Weyl character formula (2.2) and the characters of the Verma modules (2.3), we have

- (3.4)

Kλ,τ = dim(L(λ)τ)

=

v∈Sn

(−1)ℓ(v) dim(∆((v · λ)τ)

=

v∈Sn

(−1)ℓ(v)p(v · λ − τ),

where p is the Kostant partition function. Recall that p is deﬁned by

- (3.5)


1 (1 − e−α)

p(µ)e−µ,

=

![image 4](<2022-gui-revisiting-jacobi-trudi-identities-bgg_images/imageFile4.png>)

µ

where α ranges over all positive roots of sln(C).

![image 5](<2022-gui-revisiting-jacobi-trudi-identities-bgg_images/imageFile5.png>)

2However, the determination of the coeﬃcients b(λ, w) is rather diﬃcult, and they are given by the famous Kazhdan–Lusztig polynomials in virtue of the Kazhdan–Lusztig conjecture. We do not need the exact formula in this paper.

To prove Theorem 3, we use (3.4) to give an alternative interpretation of the Kostka numbers. In view of (1.5) and (3.1), we directly consider the Kostka numbers of the form Kλ,µ+δ−w(ν+δ). The following result plays a key role for our proof of Theorem 3.

Proposition 5. The Kostka number Kλ,µ+δ−w(ν+δ) is equal to [L(λ) ⊗ ∆(w · ν) : L(µ)], the multiplicity of irreducible composition factor L(µ) in L(λ) ⊗ ∆(w · ν), where λ, µ and ν are partitions, regarded as dominant weights for sln(C), and δ = (n − 1,n − 2,...,1,0). In particular, Kλ,µ = [L(λ) ⊗ ∆(0) : L(µ)].

Proof. One can use the standard ﬁltration (also known as the Verma ﬂag) to prove this proposition; see ([10, Theorem 3.6]). Note that µ corresponds to a dominant weight, so the multiplicity with which ∆(µ) occurs in a standard ﬁltration of L(λ)⊗ ∆(w · ν) is equal to the multiplicity of L(µ) in a Jordan-Ho´lder series of L(λ) ⊗ ∆(w · ν).

Here we give a direct computational proof using formal characters. If f is a formal character, let [chL(λ)]f denote the coeﬃcient of chL(λ) in the expansion of f in terms of irreducible characters, [ch∆(λ)]f denote the coeﬃcient of ch∆(λ) in its expansion by Verma module characters, and let [xλ]f denote the coeﬃcient of xλ in f. Note that

[L(λ) ⊗ ∆(w · ν) : L(µ)] = [chL(µ)]chL(λ)ch∆(w · ν). Since µ is dominant, ﬁrstly we have

[chL(µ)]chL(λ)ch∆(w · ν) =[ch∆(µ)]chL(λ)ch∆(w · ν) by the uni-triangularity (2.5). Then, by the Weyl character formula (2.2), we obtain

[ch∆(µ)]chL(λ)ch∆(w · ν) =[ch∆(µ)]

(−1)l(v) ch∆(v · λ)ch∆(w · ν) .

v∈Sn

Furthermore, by (2.3) and (3.5), we have [ch∆(µ)]ch ∆(v · λ)ch∆(w · ν) =[xµ]xv·λ+w·ν/ 1 − x−α

=p(v · λ + w · ν − µ). Combining the above identities and (3.4) leads to

(−1)l(v)p(v · λ + w · ν − µ) = Kλ,µ+δ−w(ν+δ),

[chL(µ)]chL(λ)ch∆(w · ν) =

v∈Sn

as desired. In particular, taking w = id and ν = ∅, we get

Kλ,µ = [L(λ) ⊗ ∆(0) : L(µ)]. The proof is complete.

The above proposition interprets Kostka numbers as tensor product multiplicities in the BGG category O. With this interpretation, now we are able to give a new proof of the Jacobi–Trudi identity.

A new proof of (1.3). On the one hand, in view of chL(λ) = sλ and (1.2), we have sµ/ν,sλ = sµ,sλsν = [chL(µ)]chL(λ)chL(ν) = [L(λ) ⊗ L(ν) : L(µ)],

and thus

[L(λ) ⊗ L(ν) : L(µ)]sλ. On the other hand, by (3.1) and proposition 5, we have

sµ/ν =

λ

n i,j=1 =

(−1)ℓ(w)hµ+δ−w(ν+δ)

det hµ

i−νj+j−i

w∈Sn

(−1)ℓ(w)Kλ,µ+δ−w(ν+δ)sλ

=

w∈Sn λ

(−1)ℓ(w)[L(λ) ⊗ ∆(w · ν) : L(µ)]sλ

=

w∈Sn λ

[L(λ) ⊗ L(ν) : L(µ)]sλ,

=

λ

where the last equality follows from the Weyl character formula (2.2). This completes the proof of the Jacobi–Trudi identity (1.3).

- Remark 6. In particular, for the case ν = ∅ of the Jacobi–Trudi identity, we have

det(hµ

i+j−i) =

w∈Sn λ

(−1)ℓ(w)[L(λ) ⊗ ∆(w · 0) : L(µ)]sλ

=

λ

[L(λ) ⊗ L(0) : L(µ)]sλ

=

λ

[L(λ) : L(µ)]sλ

=sµ, which follows from the Weyl character formula (2.2) for the trivial module L(0).

- Remark 7. Similar arguments give a new proof of the Jacobi–Trudi-type expansion (1.4) of the product of Schur polynomials:


n i,j=1 =

(−1)ℓ(w)hµ+δ+ww

det hµ

i+νn+1−j−i+j

0ν−wδ

w∈Sn

(−1)ℓ(w)Kλ,µ+δ−w(−w

=

0ν+δ)sλ

w∈Sn λ

(−1)ℓ(w)[L(λ) ⊗ ∆(w · (−w0ν)) : L(µ)]sλ

=

w∈Sn λ

=

=

[L(λ) ⊗ L(−w0ν) : L(µ)]sλ

λ

[L(λ) ⊗ L(ν)∗ : L(µ)]sλ

λ

[L(µ) ⊗ L(ν) : L(λ)]sλ

=

λ

=sµsν, where the last but one equality follows from tensor-hom adjunction of ﬁnite-dimensional modules of sln(C).

We proceed to prove Theorem 3.

Proof of Theorem 3. By Theorem 4, there exists an exact sequence of sln(C)modules

- (3.6) 0 → C(ν

n 2

)

d(

n

2) −→ C(ν

n 2

)−1 → ··· → C1ν −→d1 C0ν −→d0 L(ν) → 0, where Ckν = w∈S

n,ℓ(w)=k ∆(w · ν). For 0 ≤ k ≤ n2 , let V (ν,k) be the image of the boundary map dk in the BGG resolution of L(ν), and consider the exact sequence by truncating (3.6):

- (3.7) 0 → C(ν

n 2

) → C(ν

n 2

)−1 → ··· → Ckν −→dk V (ν,k) → 0. Taking the formal characters of the exact sequence (3.7), we obtain

- (3.8) ch(V (ν,k)) = ch(Im(dk)) = (−1)k w∈Sn,ℓ(w)≥k


(−1)ℓ(w) ch(∆(w · ν)) .

Now by Proposition 5, we have gµ/νk =(−1)k

(−1)ℓ(w)hµ+δ−w(ν+δ)

w∈Sn,ℓ(w)≥k

=(−1)k

(−1)ℓ(w)Kλ,µ+δ−w(ν+δ)sλ

w∈Sn,ℓ(w)≥k λ

=(−1)k

(−1)ℓ(w)[L(λ) ⊗ ∆(w · ν) : L(µ)]sλ

w∈Sn,ℓ(w)≥k λ

=(−1)k

(−1)ℓ(w)[chL(µ)]chL(λ)ch∆(w · ν)sλ

w∈Sn,ℓ(w)≥k λ

=

[chL(µ)]chL(λ)chV (ν,k)sλ

λ

[L(λ) ⊗ V (ν,k) : L(µ)]sλ.

=

λ

Almost the same arguments give the proof of (1.8), see also Remark 7. The proof is complete.

- Remark 8. The usual representation theory approach to establish Schur positivity of a given symmetric polynomial is to show that it is the characters of some ﬁnitedimensional polynomial representation of the general linear groups or the Frobenius images of some representation of the symmetric groups. As it can be seen from the proof, our approach is to transform the Schur positivity problem into the positivity


problem of a virtual character in the BGG category O of sln(C), see (3.8). It would be interesting to know whether there are other Schur positivity problems can be handled using BGG category O techniques.

Acknowledgments

The ﬁrst author would like to thank Ming Fang, Hongsheng Hu, and Nanhua Xi for useful comments. The second author is supported in part by the Fundamental Research Funds for the Central Universities and the National Natural Science Foundation of China (Nos.11522110, 11971249).

References

- [1] Kaan Akin, On complexes relating the Jacobi-Trudi identity with the Bernstein-GelfandGelfand resolution, J. Algebra 117 (1988), no. 2, 494–503.
- [2] , Resolutions of representations, Contemp. Math. 88 (1989), 209–217.

![image 6](<2022-gui-revisiting-jacobi-trudi-identities-bgg_images/imageFile6.png>)

- [3] , On complexes relating the Jacobi-Trudi identity with the Bernstein-Gelfand-Gelfand resolution, II, J. Algebra 152 (1992), no. 2, 417–426.

![image 7](<2022-gui-revisiting-jacobi-trudi-identities-bgg_images/imageFile7.png>)

- [4] IN Bernstein, Israel M Gelfand, and Sergei I Gelfand, Diﬀerential operators on the base aﬃne space and a study of g-modules, Lie groups and their representations (Proc. Summer School, Bolyai Ja´nos Math. Soc., Budapest, 1971) (1975), 21–64.
- [5] Vyjayanthi Chari, Ghislain Fourier, and Daisuke Sagaki, Posets, tensor products and Schur positivity, Algebra Number Theory 8 (2014), no. 4, 933–961.
- [6] William Fulton, Young tableaux: With applications to representation theory and geometry, Cambridge University Press, 1997.
- [7] Mark Haiman, Hecke algebra characters and immanant conjectures, J. Amer. Math. Soc. 6

(1993), no. 3, 569–595.

- [8] , Hilbert schemes, polygraphs, and the Macdonald positivity conjecture, J. Amer. Math. Soc. 14 (2001), 941–1006.

![image 8](<2022-gui-revisiting-jacobi-trudi-identities-bgg_images/imageFile8.png>)

- [9] June Huh, Jacob Matherne, Karola M´esz´ros, and Avery St Dizier, Logarithmic concavity of Schur and related polynomials, Trans. Amer. Math. Soc. 375 (2022), no. 06, 4411–4427.
- [10] James E Humphreys, Representations of semisimple lie algebras in the bgg category O, Vol. 94, American Mathematical Society, Providence, RI, 2008.
- [11] Thomas Lam, Alexander Postnikov, and Pavlo Pylyavskyy, Schur positivity and Schur logconcavity, Amer. J. Math 129 (2007), no. 6, 1611–1622.
- [12] Alain Lascoux, Polynoˆmes syme´triques, foncteurs de schur et grassmanniennes, Ph.D. Thesis, 1977.
- [13] Ian Grant Macdonald, Symmetric functions and hall polynomials, Oxford university press, 1998.
- [14] Bruce E Sagan, The symmetric group: Representations, combinatorial algorithms, and symmetric functions, Vol. 203, Springer Science & Business Media, 2001.
- [15] Richard P Stanley, Graph colorings and related symmetric functions: ideas and applications A description of results, interesting applications, & notable open problems, Discrete Mathematics 193 (1998), no. 1-3, 267–286.
- [16] Richard P. Stanley, Enumerative combinatorics. Volume 2, Camb. Stud. Adv. Math., vol. 62, Cambridge: Cambridge University Press, 1999 (English).
- [17] Andrei Vladlenovich Zelevinskii, Resolvents, dual pairs, and character formulas, Funct. Anal. Appl. 21 (1987), no. 2, 152–154.


Beijing International Center for Mathematical Research, Peking University, Bei-

jing, 100871, P.R. China Email address: guitao18@mails.ucas.ac.cn Center for Combinatorics, LPMC, Nankai University, Tianjin 300071, P. R. China Email address: yang@nankai.edu.cn

