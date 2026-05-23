---
type: source
kind: paper
title: On the equivariant log-concavity for the cohomology of the flag varieties
authors: Tao Gui
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2205.05408v2
source_local: ../raw/2022-gui-equivariant-log-concavity-cohomology-flag.pdf
topic: general-knowledge
cites:
---

arXiv:2205.05408v2[math.RT]12May2022

ON THE EQUIVARIANT LOG-CONCAVITY FOR THE COHOMOLOGY OF THE FLAG VARIETIES

TAO GUI

Abstract. We study the Sn-equivariant log-concavity of the cohomology of ﬂag varieties, also known as the coinvariant ring of Sn. Using the theory of representation stability, we give computer-assisted proofs of the equivariant log-concavity in low degrees and high degrees and conjecture that it holds for all degrees. Furthermore, we make a stronger unimodal conjecture which implies the equivariant log-concavity.

The motivation of this notes is the following conjecture

Conjecture 1. For all integer n ≥ 1, the cohomology ring of the ﬂag manifold Un/T, which is also known as the coinvariant ring of Sn: H2∗(Un/T,C) ∼= C[t1,...,tn]/ (σ1,...,σn), is equivariantly log-concave as graded representation of Sn in the sense that H2∗(m−1) ⊗ H2∗(m+1) is isomorphic to a subrepresentation of H2∗m ⊗ H2∗m for all 1 ≤ m ≤ n2 − 1, where the tj’s are of degree 2 and the σi’s are the elementary symmetric polynomials in the variables tj’s.

Acknowledgment The author would like to thank Ming Fang, Hongsheng Hu, Nicolai Reshetikhin, Peng Shan, Nanhua Xi, and Rui Xiong for useful discussions, and is grateful to Matthew H.Y. Xie and Arthur L.B. Yang for the help with computer calculations.

1. Cohomology of flag variaties: the Borel’s picture

We begin with the classical Borel’s picture. Consider the full ﬂag variety Fn over C, parametrizing all complete ﬂags in a n-dimensional C-vector space V :

{0} = V0 ⊂ V1 ⊂ V2 ⊂ ··· ⊂ Vn = V.

Written as a homogeneous space, Fn ∼= GL(n,C)/Bn, where Bn is the group of non-singular upper triangular matrices. In particular, Fn has dimension n(n−1)/2 over C.

The classical Borel’s picture [9] gives a explicit and canonical description of the cohomology of Fn using the so called coinvariant ring.

- Theorem 2 (Borel, [9]). As a graded ring,


- (1.1) H∗(Fn,C) ∼= C[t1,...,tn]/ (σ1,...,σn),

where the tj’s are of degree 2 and the σi’s are the elementary symmetric polynomials in the variables tj’s.

Use this identiﬁcation or use the ﬁber bundle

- (1.2)


Fn−1 ֒→Fn ↓

CPn−1 1

(the vertical map comes from projecting each ﬂag to the containing line) and the Leray–Hirsch theorem, one can easily compute the Betti numbers b2i of Fn (the odd Betti numbers b2i+1 are all 0), which is equal to the cardinality of {w ∈ Sn | l(w) = i} by the Bruhat decomposition, where l(w) is the inversion number of the permutation w, and the Poincar´e polynomial is

n−1

· 1 + q + ··· + qn−1 =

b2iqi = PF

1 + q + ··· + qk .

(q) :=

- (1.3) PF


n−1

n

i

k=0

(q) is a symmetric, unimodal, and log-concave polynomial 1.

It follows that PF

n

Since Fn is a smooth complex projective variety, the symmetry of the Betti numbers comes from the Poincar´e duality, and the unimodality comes from the hard Lefschetz theorem, but where is the log-concavity comes from?

- 2. The action, the graded character, and the graded multiplicity


Actually, Sn as the Weyl group of GL(n,C) can not act naturally on the ﬂag variety Fn ∼= GL(n,C)/Bn. Nevertheless, it is a classical fact that it indeed acts on the cohomology H∗(Fn). For example, one can use the diﬀeomorphism Un/T → GL(n,C)/Bn and the natural action of Sn ∼= NT/T on Un/T to induce the action of Sn on H∗(Fn), where Un is the unitary group, T is the compact torus, NT is the normalizer of T in Un.

Use this action, the Borel isomorphism H∗(Fn,C) ∼= C[t1,...,tn]/ (σ1,...,σn)

becomes an isomorphism of graded representations, where Sn acts on the right hind side by permuting the ti’s. Using equivariant cohomology, it is a classical result that if we forget the grading,

H∗(Fn,C) ∼= C[t1,...,tn]/ (σ1,...,σn)

carries the regular representation of Sn, see for example, [2]. Therefore, the cohomological degrees cut the regular representation into graded pieces, and what we are interested is the log-concavity of the tensor product corresponding to this grading.

Consider the ﬁber bundle

- (2.1)

Fn ∼= Un/T ֒→BT

↓ BU

,

where BT and BU are the classifying spaces of T and Un, respectively. Taking cohomology, we get

- (2.2) C[t1,...,tn] ∼= C[t1,...,tn]/ (σ1,...,σn) ⊗ C[σ1,...,σn]

as graded representations of Sn. Therefore, the graded character of H∗(Fn) is given by

- (2.3) χ(w,q) =


k

n

1 − qλi ,

1 − qi /

i=1

i=1

![image 1](<2022-gui-equivariant-log-concavity-cohomology-flag_images/imageFile1.png>)

1We call a polynomial symmetric (unimodal, log-concave, respectively) if the sequence of coeﬃcients is symmetric (unimodal, log-concave, respectively). It is easy to see that if two polynomials are log-concave with all positive coeﬃcients, so is their product.

where w ∈ Sn is a permutation of cycle type λ = (λ1,··· ,λk). It is easy to see that

- (2.4) qn(n−1)/2χ(w,q−1) = (−1)l(w)χ(w,q)

by the graded character (2.3), therefore representations in complement degrees diﬀer by tensoring the sign representation, which can also be deduced from the Poincare duality. Using the graded character (2.3), one can compute the graded multiplicities of H∗(Fn), and by work of Lusztig and Stanley, the multiplicities have the following combinatorial interpretation

Theorem 3. (Lusztig–Stanley, [15, Prop. 4.11]2) For any partition λ of n, as long as i ≤ n(n − 1)/2, the multiplicity of the irreducible representation V (λ) of Sn corresponding to λ in H2i(Fn) equals the number 3 bλ,i of standard tableaux of shape λ with major index equal to i, where the major index of a tableau4 is the sum of the numbers j so that the box labeled j + 1 is in a lower row than the box labeled j.

Therefore, using the Frobenius characteristic map, one can transform Conjecture 1 into a Schur positivity conjecture in the symmetric function theory.

- Conjecture 4. For all natural number n and 1 ≤ i ≤ n2 − 1, the symmetric function Sn,i ∗ Sn,i − Sn,i−1 ∗ Sn,i+1 is a non-negative linear combination of the

Schur polynomials, where Sn,i := λ⊢n bλ,iSλ, where Sλ is the Schur polynomial corresponding to partition λ, ∗ denote the internal product of symmetric functions.

In terms of Kronecker coeﬃcients, which are the structure coeﬃcients of the tensor product of irreducible representations of Sn, the above conjectures are equivalent to the following numerical inequalities

- Conjecture 5. For all natural number n and 1 ≤ i ≤ n2 − 1, the inequalities


- (2.5)


bλ,i−1bµ,i+1gλµν ≤

bλ,ibµ,igλµν

λ⊢n µ⊢n

λ⊢n µ⊢n

hold for all ν ⊢ n, where gλµν are the Kronecker coeﬃcients.

Conjecture 5 is intriguing because we know so little about Kronecker coeﬃcients5, and a major unsolved problem in representation theory and combinatorics is to ﬁnd some combinatorial descriptions of Kronecker coeﬃcients. Since H∗(Fn,C) carries the regular representation of Sn, each gλµν will actually appears in (2.5).

Using the representation stability theory, we have the following

Theorem 6. For all natural number n, the cohomology ring H2∗(Fn,C) is equivariantly log-concave in degree ≤ 3 and co-degree ≤ 3 as graded representation of

![image 2](<2022-gui-equivariant-log-concavity-cohomology-flag_images/imageFile2.png>)

2See [14, Theorem 8.8] for a proof of this result and the graded character (2.3). 3Known as the “fake degree”, see, for example, [7]. 4There is also a notion of the major index of a permutation, which is equal to the major index of

the recording tableau (the Q-symbol) of that permutation under the Robinson–Schensted–Knuth correspondence.

5One could also consider the somewhat unnatural log-concavity of the induced tensor product by replacing the Kronecker coeﬃcients in (2.5) with the Littlewood–Richardson coeﬃcients, but the resulting inequalities are NOT true in general.

Sn. That is,

- H2∗1 ⊗2 ⊇ H2∗0 ⊗ H2∗2, H2∗((

n 2

)−1)

⊗2

⊇ H2∗(

n 2

) ⊗ H2∗((

n 2

)−2),

- H2∗2 ⊗2 ⊇ H2∗1 ⊗ H2∗3, H2∗((n

2

)−2)

⊗2

⊇ H2∗((n

2

)−1) ⊗ H2∗((n

2

)−3),

- H2∗3 ⊗2 ⊇ H2∗2 ⊗ H2∗4, H2∗((


)−3)

n 2

⊗2

)−4)

)−2) ⊗ H2∗((

⊇ H2∗((

n 2

n 2

for all n. Equivalently, Conjecture 4 and Conjecture 5 holds in these degrees for all n.

Proof. In Sect.5 of [10], H∗(Fn,C) ∼= C[t1,...,tn]/ (σ1,...,σn) is shown to be a co-FI-algebra of ﬁnite type, therefore each {H2∗i}n for ﬁxed i form a uniformly representation stable sequence of Sn-representations, see also [11, Theorem 7.4]. With a little more eﬀort in analyzing the major index, it can be shown that for i ≤ 4, {H2∗i}n stabilized once n ≥ 2i. Therefore, by [13, Lemma 3.2 and Theorem

- 3.3], to prove that H2∗(m−1) ⊗ H2∗(m+1) is isomorphic to a subrepresentation of H2∗m⊗H2∗m for all n and m ≤ 3, it is suﬃcient to check that H2∗(m−1)⊗H2∗(m+1) is isomorphic to a sub-representation of H2∗m ⊗ H2∗m for n ≤ 4m. We have performed these checks for n ≤ 12 using maple. The assertions for the co-degree part follow from the duality (2.4).

3. A unimodal conjecture

By examining the computed data, we observe that the numerical evidence suggests the stronger conjecture Conjecture 7. For all natural number n and 1 ≤ i ≤ n2 − 1, the sequence dν,i is symmetric and unimodal, where

dν,i :=

λ⊢n µ⊢n

bλ,ibµ,igλµν −

λ⊢n µ⊢n

bλ,i−1bµ,i+1gλµν .

That is, when we decompose the virtual representation H2∗i(Fn) ⊗ H2∗i(Fn) − H2∗(i−1)(Fn)⊗H2∗(i+1)(Fn), the multiplicity sequence {dν,i} should be symmetric and unimodal for all n and all partition ν of n. The symmetry comes from the duality (2.4). Conjecture 7 implies Conjecture 1 (equivalently, Conjecture 4 and

Conjecture 5) since dν,1 = dν,(n

2

)−1 ≥ 0 for all ν by Theorem 6.

Remark 8. In [6] and [7], the authors study the distribution of the major index on standard Young tableaux and enumerative questions involving the fake degrees, we note that the sequences of fake degrees bλ,i themselves are NOT always unimodal.

4. Some remarks

- 4.1. Other Coxeter groups. Since the graded dimensions of the coinvariant ring are log-concave for any ﬁnite Coxeter group, see [8, Lemma 7.1.1 and Theorem 7.1.5], it is interesting to ask whether the coinvariant ring of Coxeter groups other than symmetric groups carries log-concave graded representations. Unfortunately, it is easy to show that except m = 2 or 3, all other dihedral groups I2(m) including the Weyl groups of type B2 and type G2 are not the case. We don’t know whether the equivariant log-concavity is true for the simply laced (ADE) types. In [16], the author proved that each sequence of graded piece of the coinvariant ring for


the classical Weyl groups is uniformly representation stable, but we don’t know whether the equivariant log-concavity holds after stabilizing

- 4.2. Relation with the conjectures on the conﬁguration spaces. In [13], the authors made equivariant log concavity conjectures for the cohomology or intersection cohomology of variant conﬁguration spaces. In a series of papers [1–3,5], to answer the Berry-Robbins problem asked by two physicists, Sir Michael Atiyah constructed a continuous map from the conﬁguration space Conf n,R3 to the ﬂag manifold Un/T, which is compatible with the action of the symmetric group Sn 6. Both H∗( Conf n,R3 ) and H∗(Un/T) carry the regular representation of Sn [2]. But we can’s get a formal relationship between log-concave conjectures on both sides using Atiyah’s map. It seems that the unimodal property similar with Conjecture 7 are also true in their case 7.


4.3. The Springer representations. One could ask a further question that whether the equivariant log-concavity hold for other total Springer representations in type A besides the full ﬂag case. If this is true, it will imply that the Betti numbers of Springer ﬁbers are unimodal and log-concave, which was observed in [12] for some special types of partitions and n ≤ 9. By Lusztig’s result, the graded multiplicity is given by the Kostka–Foulkes polynomial, and the Frobenius image is therefore given by the modiﬁed Hall–Littlewood polynomials. Unfortunately, the equivariant log-convity of Springer representations are not true in general, the smallest counterexample appears in S7, all counterexample up to S10 is {(4,1,1,1),(5,1,1,1),(6,1,1,1),(5,2,1,1),(5,1,1,1,1),(7,1,1,1),(6,2,1,1), (6,1,1,1,1),(5,2,1,1,1),(5,1,1,1,1,1)}.

References

- [1] Michael Atiyah, Conﬁgurations of points, Philosophical Transactions of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences 359 (2001), no. 1784, 1375–1387.
- [2] , Equivariant cohomology and representations of the symmetric group, Chinese Annals of Mathematics 22 (2001), no. 01, 23–30.

![image 3](<2022-gui-equivariant-log-concavity-cohomology-flag_images/imageFile3.png>)

- [3] , The geometry of classical particles, Surveys in diﬀerential geometry 7 (2002), no. 1, 1–15.

![image 4](<2022-gui-equivariant-log-concavity-cohomology-flag_images/imageFile4.png>)

- [4] Michael Atiyah and Roger Bielawski, Nahm’s equations, conﬁguration spaces and ﬂag manifolds, Bulletin of the Brazilian Mathematical Society 33 (2002), no. 2, 157–176.
- [5] Michael Atiyah and Paul Sutcliﬀe, The geometry of point particles, Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences 458 (2002), no. 2021, 1089–1115.
- [6] Sara C Billey, Matjaˇz Konvalinka, and Joshua P Swanson, On the distribution of the major index on standard Young tableaux, arXiv preprint arXiv:2005.10341 (2020).
- [7] , Tableau posets and the fake degrees of coinvariant algebras, Advances in Mathematics 371 (2020), 107252.

![image 5](<2022-gui-equivariant-log-concavity-cohomology-flag_images/imageFile5.png>)

- [8] Anders Bjorner and Francesco Brenti, Combinatorics of Coxeter groups, Vol. 231, Springer Science & Business Media, 2006.
- [9] Armand Borel, Sur la cohomologie des espaces ﬁbre´s principaux et des espaces homogenes de groupes de Lie compacts, Annals of Mathematics (1953), 115–207.
- [10] Thomas Church, Jordan S Ellenberg, and Benson Farb, FI-modules and stability for representations of symmetric groups, Duke Mathematical Journal 164 (2015), no. 9, 1833–1910.
- [11] Thomas Church and Benson Farb, Representation theory and homological stability, Advances in Mathematics 245 (2013), 250–314.


![image 6](<2022-gui-equivariant-log-concavity-cohomology-flag_images/imageFile6.png>)

6See [4] for the generalization to other Weyl groups. 7We thank Matthew H.Y. Xie for some veriﬁcations.

- [12] Lucas Fresse, Ronit Mansour, and Anna Melnikov, Unimodality of the distribution of Betti numbers for some Springer ﬁbers, Journal of Algebra 391 (2013), 284–304.
- [13] Jacob P Matherne, Dane Miyata, Nicholas Proudfoot, and Eric Ramos, Equivariant log concavity and representation stability, International Mathematics Research Notices (2021).
- [14] Christophe Reutenauer, Free Lie algebras, London Mathematical Society Monographs. New Series, vol. 7, The Clarendon Press, Oxford University Press, New York, 1993. Oxford Science Publications. MR1231799
- [15] Richard P Stanley, Invariants of ﬁnite groups and their applications to combinatorics, Bulletin of the American Mathematical Society 1 (1979), no. 3, 475–511.
- [16] Jennifer CH Wilson, FIW-modules and stability criteria for representations of classical Weyl groups, Journal of Algebra 420 (2014), 269–332.


Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Beijing, China

Email address: guitao18@mails.ucas.ac.cn

