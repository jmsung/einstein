# arXiv:1407.4095v1[math.OC]15Jul2014

## POSITIVE SEMIDEFINITE RANK

HAMZA FAWZI, JOAO˜ GOUVEIA, PABLO A. PARRILO, RICHARD Z. ROBINSON, AND REKHA R. THOMAS

Abstract. Let M ∈ Rp×q be a nonnegative matrix. The positive semideﬁnite rank (psd rank) of M is the smallest integer k for which there exist positive semideﬁnite matrices Ai, Bj of size k × k such that Mij = trace(AiBj). The psd rank has many appealing geometric interpretations, including semideﬁnite representations of polyhedra and information-theoretic applications. In this paper we develop and survey the main mathematical properties of psd rank, including its geometry, relationships with other rank notions, and computational and algorithmic aspects.

Contents

- 1. Introduction 2

- 1.1. Paper outline 2

2. Deﬁnition and interpretations 3

- 2.1. Psd rank 3


- 3. Motivation and examples 9

- 3.1. Geometric interpretation 9
- 3.2. Information theoretic interpretation 13


- 4. Psd rank two and convex programming 15
- 5. Relationships between ranks 17

- 5.1. Square root rank: an upper bound for psd rank 18
- 5.2. Lower bounds for psd rank 19
- 5.3. Comparisons between ranks 21


- 6. Properties of factors 23

- 6.1. Rank of factors 23
- 6.2. Norms of factors 23


- 7. Space of factorizations 25
- 8. Symmetric factorizations 30
- 9. Open questions 31


- 2.2. Dependence on the ﬁeld 6
- 2.3. First properties 6
- 2.4. Lower semicontinuity of psd rank 9


- 9.1. Psd rank of special matrices 31
- 9.2. Geometry of psd rank 31
- 9.3. Complexity and algorithms 31
- 9.4. Slack matrices 32
- 9.5. Completely positive semideﬁnite matrices 33


References 33

Fawzi and Parrilo were supported in part by AFOSR FA9550-11-1-0305. Gouveia was supported by the Centre for Mathematics at the University of Coimbra and Fundac¸a˜o para a Cieˆncia e a Tecnologia, through the European program COMPETE/FEDER. Robinson was supported by the US NSF Graduate Research Fellowship through grant DGE-1256082 and Thomas was supported by NSF grant DMS-1115293.

1

1. Introduction

Matrix factorizations (or more generally, factorizations of linear maps) are a classical and important topic in applied mathematics. For instance, in the standard low-rank matrix factorization problem, given a matrix M ∈ Rp×q one constructs matrices A ∈ Rp×k and B ∈ Rk×q such that M = AB, where the intermediate dimension k is as small as possible. Letting ai and bj be the rows of A and columns of B, respectively, ﬁnding such a factorization can be interpreted as a realizability problem, where we want to produce vectors in Rk that realize the inner products given by Mij = ai,bj . The smallest such k is, of course, the usual rank of the matrix M.

In applications, low-rank factorizations often have appealing interpretations (e.g., reduced-order or “simple” models), since they provide a decomposition of a linear map Rq → Rp in terms of mappings Rq → Rk → Rp through a “small” subspace. Many classical and successful methods in systems theory (e.g., realization theory, model order reduction), or statistics and machine learning (e.g., principal component analysis, factor analysis) are based on these techniques; see e.g. [Kal63, Moo81, Jol02].

In many situations, however, one often requires additional conditions on the possible factors. A well-known example is the case of nonnegative factorizations [CR93], where M is a given nonnegative matrix and the factors A,B are also required to be nonnegative (here and throughout the paper, a nonnegative matrix is a matrix where all the entries are nonnegative). These requirements often arise from probabilistic interpretations (if M corresponds to a joint distribution, in which case the factors can be interpreted in terms of conditional independence; see e.g. [MSvS03]), or modeling choices (additive representations in terms of features and latent variables; see e.g., [LS99]). Another well-known case is when the factors A,B are required to be “small” with respect to a given matrix norm. This is a situation that has been well-studied in contexts such as Banach space theory, communication complexity and machine learning, where factorization norms are used to capture this notion; see e.g. [LMSS07, LS09].

Over the last couple of years, a new and intriguing class of matrix factorization problems has been introduced, by considering conic factorizations of nonnegative linear maps through a convex cone K, i.e., mappings Rq+ → K → Rp+ (nonnegative factorizations correspond to the case when K is the nonnegative orthant). A particularly interesting case, which is the focus of this paper, occurs when K is the cone of positive semideﬁnite matrices [GPT13].

More concretely, a positive semideﬁnite factorization of a nonnegative matrix M ∈ Rp×q is a collection of symmetric k × k positive semideﬁnite matrices {A1,...,Ap} and {B1,...,Bq} such that

Mij = trace(AiBj), i = 1,...,p, j = 1,...,q. The positive semideﬁnite rank (psd rank) of M can then be deﬁned as the smallest k for which such a factorization exists [GPT13]. As we explain in Section 3, a natural and important source of these factorizations is their relationship with representability of polytopes by semideﬁnite programming. These results extend the connections, ﬁrst explored by Yannakakis in the context of polytopes and linear programming [Yan91], between “algebraic” factorizations of the slack matrix and the “geometric” question of existence of extended formulations. Since this quantity exactly characterizes semideﬁnite representability, positive semideﬁnite rank is an essential component of the burgeoning area of convex algebraic geometry [BPT12].

Besides these geometric and complexity-theoretic considerations, however, there are many other reasons to study these natural factorizations and ranks as independent mathematical objects, and this is the viewpoint we emphasize in this paper. Our main goal is to study the positive semideﬁnite rank of a matrix from the algebraic-geometric perspective, as well as survey and collect most of the existing results to date.

- 1.1. Paper outline. In Section 2 we present the formal deﬁnition and basic properties of psd rank. We analyze its behavior under natural matrix operations, its continuity properties, as well as its


dependence on the underlying ﬁeld. Throughout, we present numerous examples illustrating these notions.

Section 3 presents several complementary interpretations and motivations for psd rank. We discuss extensively its main geometric interpretation in terms of the “complexity” of a convex body that is contained in between two polytopes, a topic initially studied in [GPT13] and further elaborated in [FMP+12]. We also discuss a quantum analogue of the well-known probabilistic interpretations of nonnegative factorizations in terms of conditional independence, where the psd rank characterizes the minimum amount of quantum information that must be shared between two parties to generate samples of a correlated random variable [JSWZ13].

Like nonnegative rank, psd rank can be computationally challenging, although in some situations it can be nicely characterized. In Section 4 we show that the case of psd rank equal to 2 can be decided using convex optimization (in particular, semideﬁnite programming). The positive semideﬁnite rank of a matrix has natural relations with other rank notions, such as the usual (or “standard”) rank and the nonnegative rank; we discuss these in Section 5. We also present the related notion of “square root rank,” a reﬁnement of psd rank to the case of rank-one factors. We show that in general, these rank notions are incomparable (Table 1), and provide explicit examples/counterexamples for all pairwise comparisons between them.

In Section 6 we analyze the situation where additional properties are imposed on the factor matrices Ai,Bj. We show how to guarantee uniform bounds on the factors for diﬀerent norms (trace, spectral norm), as well as upper bounds on their ranks.

Since psd factorizations are not unique, it is also of interest to study the space of all possible factorizations. In Section 7 we study the topological properties of the space of factorizations, and show that in certain cases it is connected, in contrast to the case of nonnegative factorizations. This geometric insight also allows a better understanding on the rank of possible factors; see e.g., Example 7.8.

In Section 8 we specialize the situation to symmetric matrices with symmetric factorizations, and discuss the connections with some classical matrix cones (completely positive, doubly nonnegative).

We conclude in Section 9 with a list of open problems, and questions for future research.

2. Definition and interpretations

For a positive integer k, let S+k denote the cone of k × k real symmetric positive semideﬁnite (psd) matrices. Recall that S+k is a closed convex cone in the vector space Sk of all k × k real symmetric matrices. We equip Sk with the standard inner product deﬁned by:

A,B = trace(AB) =

AijBij.

1≤i,j≤k

The inner product of any two psd matrices is nonnegative, i.e., if A,B ∈ S+k , then A,B ≥ 0. In fact the cone S+k is self-dual, meaning that:

A ∈ S+k ⇐⇒ A,X ≥ 0 ∀X ∈ S+k . The following well-known fact about orthogonal matrices in S+k will be useful later: Proposition 2.1. If A,B ∈ S+k are such that A,B = 0, then AB = 0. Proof. If we let A = i aiaTi and B = j bjbTj then A,B = i,j(aTi bj)2. Thus since A,B = 0 we get aTi bj = 0 for all i,j. Hence this means that AB = i,j(aTi bj)aibTj = 0.

- 2.1. Psd rank. We now give the formal deﬁnitions of psd factorizations and psd rank, which are the main objects of study in this paper:


Deﬁnition 2.2 ([GPT13]). Given a nonnegative matrix M ∈ Rp+×q, a psd factorization of M of size k is a collection of psd matrices A1,...,Ap ∈ S+k and B1,...,Bq ∈ S+k such that Mij = Ai,Bj for all i = 1,...,p and j = 1,...,q. The psd rank of M, denoted rankpsd (M), is the smallest integer k for which M admits a psd factorization of size k.

- Remark 2.3. A psd factorization of M is equivalent to the existence of linear maps Rq+ → S+k → Rp+.


Indeed, given a psd factorization, the linear maps x  → qj=1 xjBj and Y  → Ai,Y (for i = 1,...,p) have the desired property. The converse is also easy, by considering the image of the coordinate

vectors e1,...,eq under the ﬁrst map, and self-duality of the cone S+k .

The psd rank is related to another notion of rank for nonnegative matrices, namely the nonnegative rank [CR93].

- Deﬁnition 2.4. Given a nonnegative matrix M ∈ Rp+×q, a nonnegative factorization of M of size


k is a collection of nonnegative vectors a1,...,ap ∈ Rk+ and b1,...,bq ∈ Rk+ such that Mij = aTi bj for all i = 1,...,p and j = 1,...,q. The nonnegative rank of M, denoted rank+(M), is the smallest integer k for which M admits a nonnegative factorization of size k.

The ﬁrst proposition below establishes simple inequalities between the diﬀerent notions of rank, namely the usual rank, the psd rank and the nonnegative rank. Proposition 2.5. If M ∈ Rp+×q is a nonnegative matrix, then

- 1

- 2 ≤ rankpsd (M) ≤ rank+(M) ≤ min(p,q).


- 1

- 2


1 + 8rank(M) −

- (1)


Proof. The last inequality is trivially true since M = MIq = IpM where Ik is the k × k identity matrix.

Suppose a1,...,ap ∈ Rk+ and b1,...,bq ∈ Rk+ give a nonnegative factorization of M ∈ R+p×q.

Then the diagonal matrices Ai := diag(ai) and Bj := diag(bj) give a S+k -factorization of M, and we obtain the second inequality.

Now suppose A1,...Ap,B1,...,Bq give a S+k -factorization of M. Consider the vectors

ai = vec(Ai) and bj = vec(Bj) where for X ∈ Sk we deﬁne vec(X) ∈ R(k+12 ) by:

√

√

√

√

2X12,...,

2X1r,

2X23,...,

2X(k−1)k).

vec(X) = (X11,...,Xkk,

Then ai,bj = Ai,Bj = Mij so M has rank at most k+12 . By solving for k we get the desired inequality.

- Example 2.6. To illustrate the notion of a psd factorization, consider the following matrix M known as the 3 × 3 derangement matrix:


 

 .

- 0 1 1
- 1 0 1 1 1 0


M =

This matrix M satisﬁes rank(M) = rank+(M) = 3. One can show that M admits a psd factorization of size 2. Indeed, deﬁne:

- A1 =

1 0 0 0

A2 =

- 0 0
- 0 1


A3 =

1 −1 −1 1

- B1 =


- 0 0
- 0 1


B2 =

1 0 0 0

B3 =

1 1 1 1

.

One can easily check that the matrices Ai and Bj are positive semideﬁnite, and that Mij = Ai,Bj for all i = 1,...,3 and j = 1,...,3. This factorization shows that rankpsd (M) ≤ 2. In fact one has rankpsd (M) = 2 since the ﬁrst inequality in (1) gives rankpsd (M) ≥ 21

√1 + 8 · 3 − 12 = 2. ♦

- Example 2.7. Consider more generally the following 3 × 3 circulant matrix, where a,b,c are nonnegative real numbers:


- (2) M(a,b,c) =

 

- a b c c a b
- b c a


 .

One can check that the usual rank of M(a,b,c) is 3 unless a = b = c in which case the rank is one. When rank(M(a,b,c)) = 3, the bounds in (1) say that 2 ≤ rankpsd (M(a,b,c)) ≤ 3. Using the geometric interpretation of the psd rank (cf. Section 3) one can show that

rankpsd (M(a,b,c)) ≤ 2 ⇐⇒ a2 + b2 + c2 ≤ 2(ab + bc + ac). Figure 1 shows the region described by the inequality above when a = 1. ♦

0 1 2 3 4 b

- 0

- 1

- 2

- 3

- 4


c

Figure 1. The blue region shows the values of (b,c) for which rankpsd (M(1,b,c)) ≤ 2, where M(a,b,c) is the 3 × 3 circulant matrix deﬁned in (2). This region is deﬁned by the inequality 1 + b2 + c2 ≤ 2(b + c + bc).

If M is a matrix such that rank(M) = 1 or rank(M) = 2, then the psd rank is equal to the rank, as stated in the next proposition:

- Proposition 2.8. For a nonnegative matrix M ∈ Rp+×q the following is true:


- (3) rank(M) = 1 ⇔ rank+(M) = 1 ⇔ rankpsd (M) = 1. Furthermore, we have the following implication:
- (4) rank(M) = 2 ⇒ rank+(M) = rankpsd (M) = 2.


Proof. The proof of (3) is clear from the inequalities (1). For (4), we can use a result from [CR93] which states that if rank(M) = 2 then rank+(M) = 2, from which it easily follows that rankpsd (M) = 2. In Section 3 (Remark 3.4), we give a geometric argument for (4).

- 2.2. Dependence on the ﬁeld. In the deﬁnition of psd rank, Deﬁnition 2.2, we required the factors (Ai)i=1,...,p and (Bj)j=1,...,q to have real entries. When the matrix M has rational entries, it is natural to deﬁne a notion of psd rank where the factors (Ai)i=1,...,p and (Bj)j=1,...,q are required to have rational entries. If we denote this by rankQpsd (M), then we clearly have:

(5) rankpsd (M) ≤ rankQpsd (M). In [GFR14] it was shown on a 8 × 6 matrix M that the inequality (5) can be strict.

It is also natural to consider a related notion of psd rank where the factors (Ai)i=1,...,p and (Bj)j=1,...,q in the psd factorizations are positive semideﬁnite Hermitian matrices. Denote by rankCpsd (M) the associated psd rank. It is not diﬃcult to see that the following inequalities hold:

rankCpsd (M) ≤ rankpsd (M) ≤ 2rankCpsd (M). The second inequality comes from the fact that if A is a Hermitian positive semideﬁnite matrix, then the 2n × 2n real symmetric matrix

(6)

1 √2

ReA ImA −ImA ReA

is positive semideﬁnite. Furthermore the function which maps any n × n Hermitian matrix A to the 2n × 2n block matrix (6) preserves inner products.

One can show that the Hermitian psd rank can be strictly smaller than the real psd rank. Consider the 4 × 4 derangement matrix:

M =

  

- 0 1 1 1
- 1 0 1 1


- 1 1 0 1
- 1 1 1 0


  .

Using the inequalities (1) one can show that rankpsd (M) ≥ 3. However one can ﬁnd a psd factorization of M with Hermitian matrices of size 2, as given below:

- A1 =

1 0 0 0

A2 =

- 0 0
- 0 1


A3 =

1 −1 −1 1

A4 =

1 e2iπ/3 e−2iπ/3 1

- B1 =


- 0 0
- 0 1


B2 =

1 0 0 0

B3 =

1 1 1 1

B4 =

1 −e2iπ/3 −e−2iπ/3 1

.

Actually in [LWdW14], the authors exhibit a sequence of matrices (Mk) of increasing size such that rankCpsd (Mk) < rankpsd (Mk) for all k and where the gap rankpsd (Mk) − rankCpsd (Mk) grows with k (the ratio rankpsd (Mk)/rankCpsd (Mk) goes asymptotically to √2).

In this survey we will focus on the real psd rank, given in Deﬁnition 2.2.

- 2.3. First properties. The next theorem establishes some structural properties satisﬁed by the psd rank


- Theorem 2.9. Given a nonnegative matrix M ∈ Rp+×q, we have:


- (i) rankpsd (M) = rankpsd (MT).
- (ii) If D1 ∈ Rp+×p,D2 ∈ Rq+×q are diagonal matrices with strictly positive elements on the diagonal, then rankpsd (D1MD2) = rankpsd (M).
- (iii) If N ∈ Rp+×q, then rankpsd (M + N) ≤ rankpsd (M) + rankpsd (N).
- (iv) If N ∈ Rq+×r then rankpsd (MN) ≤ min(rankpsd (M),rankpsd (N)).
- (v) rankpsd (M ◦ M) ≤ rank(M), where ◦ denotes Hadamard (entrywise) product.


Proof.

- (i) Property (i) is clear.


- (ii) If Mij = Ai,Bj is a psd factorization of M, then (D1MD2)ij = (D1)iiAi,(D2)jjBj

is a psd factorization of D1MD2 of the same size. Thus since the diagonal elements of D1 and D2 are strictly positive we easily get that rankpsd (M) = rankpsd (D1MD2).

- (iii) Let Mij = Ai,Bj and Nij = A i,B j be psd factorizations of M and N of size respectively rankpsd (M) and rankpsd (N). Deﬁne

Ci =

Ai 0 0 A i

and Dj =

Bj 0 0 B j

.

Note that Ci and Dj are psd matrices of size rankpsd (M) + rankpsd (N). Furthermore we clearly have Mij + Nij = Ci,Dj . Thus rankpsd (M + N) ≤ rankpsd (M) + rankpsd (N).

- (iv) Let k = rankpsd (M) and let Mij = Ai,Bj be a psd factorization of M of size k. For j ∈ [r], deﬁne Cj = qt=1 NtjBt. Note that Cj ∈ S+k since Ntj ≥ 0 and Bt ∈ S+k . Then we verify that Ai,Cj = qt=1 Ntj Ai,Bt = qt=1 NtjMit = (MN)ij and so we get a psd factorization of MN of size k. This shows that rankpsd (MN) ≤ rankpsd (M). A similar argument shows that rankpsd (MN) ≤ rankpsd (N).
- (v) Let Mij = ai,bj be a factorization of M where ai,bj ∈ Rr where r = rank(M). Deﬁne


Ai = aiaTi ∈ S+r and Bj = bjbTj for i = 1,...,p and j = 1,...,q. Then Ai,Bj give a psd factorization of M ◦ M of size r. Indeed:

Ai,Bj = aiaTi ,bjbTj = ( ai,bj )2 = Mij2 = (M ◦ M)ij. Hence rankpsd (M ◦ M) ≤ rank(M).

The next theorem analyzes the psd rank of block-triangular matrices (the result below was also found independently by G´abor Braun and Sebastian Pokutta as well as in [LWdW14]):

- Theorem 2.10. Let P ∈ Rp+1×q1,Q ∈ Rp+2×q1,R ∈ Rp+2×q2 be nonnegative matrices and let M be the block matrix of size (p1 + p2) × (q1 + q2):


- P 0
- Q R


M =

.

Then

- (7) rankpsd (M) ≥ rankpsd (P) + rankpsd (R). Furthermore, when Q = 0 we have equality.

Proof. We ﬁrst show the inequality (7). Assume the matrix M has a psd factorization of size k where the p1 + p2 row factors are called A1,...,Ap1, A1,..., Ap2 ∈ S+k and the q1 + q2 column factors are B1,...,Bq1, B1,..., Bq2 ∈ S+k . Since the upper-right block of M is zero, we have for all (i,j) ∈ [p1] × [q2], Ai, Bj = 0. Hence, by Proposition 2.1, Ai Bj = 0. Thus if we let

- F = qi=12 range( Bj) ⊆ Rk, we have that F ⊆ ker(Ai) for all i = 1,...,p1. Since Ai is symmetric this is equivalent to range(Ai) ⊆ F⊥. Let U be an orthonormal matrix whose columns consist of an orthonormal basis for F⊥ concatenated with an orthonormal basis of F. Since range(Ai) ⊆ F⊥ we know that Ai has the form:


- (8) Ai = U


A i 0 0 0

UT

- where A i is of size d where d = dimF⊥. Furthermore, since range( Bj) ⊆ F we have:

(9) Bj = U

0 0 0 B j

UT

- where B j is of size k −d = dimF. Note that if we conjugate all the factors of the psd factorization of M by U (i.e., replace Ai by UTAiU, etc.) we get another valid psd factorization of M of the


same size. Thus we can assume without loss of generality that U = I and that Ai and Bj are block-diagonal.

If we now let B j be the upper-left d × d block of Bj, then we have Pij = Ai,Bj = A i,B j , since Ai has the block-diagonal structure (8) (with U = I). Thus this shows that rankpsd (P) ≤ d. Similarly, if we let A i be the bottom-right (k−d)×(k−d) block of Ai, then we get Rij = Ai, Bj =

A i, B j and thus rankpsd (R) ≤ k − d. Thus we ﬁnally get that rankpsd (P) + rankpsd (R) ≤ d + (k − d) = k which is the inequality we want.

We now show that when Q = 0 we have rankpsd (M) = rankpsd (P) + rankpsd (R). Indeed let Pij = Ci,Dj and Rij = Ei,Fj be psd factorizations of P and R respectively of size rankpsd (P) and rankpsd (R). Deﬁne:

and

Ai =

Ci 0 0 0 ∀i ∈ [p1], Ai =

0 0 0 Ei ∀i ∈ [p2]

Bj =

Dj 0 0 0 ∀j ∈ [q1], Bj =

0 0 0 Fj ∀j ∈ [q2].

It is easy to see that the factors A1,...,Ap1, A1,..., Ap2 and B1,...,Bq1, B1,..., Bq2 give a psd factorization of the block-diagonal matrix

P 0 0 R

of size rankpsd (P) + rankpsd (R). Thus this shows, together with the inequality proved above, that

rankpsd

P 0 0 R

= rankpsd (P) + rankpsd (R).

- Example 2.11. A consequence of Theorem 2.10 is that the psd rank of the identity matrix In is equal to n, since In = diag(1,...,1). In fact more generally the psd rank of a nonnegative diagonal matrix is equal to the number of nonzero diagonal elements.


Kronecker product. The Kronecker (tensor) product of two matrices M ∈ Rp×q and N ∈ Rp ×q is the pp × qq matrix M ⊗ N deﬁned by:

  

  .

M11N ... M1qN . . Mp1N ... MpqN

M ⊗ N =

It is well-known that the rank of the Kronecker product M ⊗N is equal to the product of the ranks of M and N: rank(M ⊗ N) = rank(M)rank(N). A natural question is to know whether the same is true for the psd rank. In [LWdW14] the authors give a counterexample to this, where they show that the psd rank of M ⊗ N can be strictly smaller than rankpsd (M)rankpsd (N) (note that the inequality rankpsd (M ⊗ N) ≤ rankpsd (M)rankpsd (N) is always true).

- 2.4. Lower semicontinuity of psd rank. In this subsection we show that for any k ∈ N, the set of matrices of psd rank ≤ k is closed (under the standard topology in Rp×q). We prove the following:


- Theorem 2.12. Let (Mn)n∈N be a sequence of nonnegative matrices converging to M ∈ Rp+×q such that rankpsd (Mn) ≤ k for all n ∈ N. Then rankpsd (M) ≤ k.


Proof. The main ingredient to prove this result is to show that the factors Ai,Bj in a psd factorization can always be chosen to be bounded. We have the following lemma:

Lemma 2.13. Let M ∈ Rp+×q and assume that M has a psd factorization of size k. Then M admits a psd factorization Mij = Ai,Bj of size k where the factors satisfy trace(Ai) ≤ k and trace(Bj) = pi=1 Mij.

Proof. We defer the proof of this Lemma to Section 6 where we discuss in more detail the issue of scaling the factors in a psd factorization.

Let (Mn) be a sequence of nonnegative matrices converging to M. Since (Mn) is a convergent sequence the entries of Mn are all bounded from above by some positive constant (independent of n). The previous lemma shows that for each n, one can ﬁnd a psd factorization of Mn of the form:

(Mn)ij = Ani ,Bjn

where Ani ,Bjn ∈ S+k and such that the sequences (Ani )n∈N and (Bjn)n∈N are all bounded in Sk. Thus one can extract convergent subsequences (Aφi (n)), (Bjφ(n)) where φ : N → N is increasing and Aφi (n) → Ai and Bjφ(n) → Bj when n → +∞. Since S+k is closed we have Ai,Bj ∈ S+k and we get:

Aφi (n),Bjφ(n) = Ai,Bj which is a valid psd factorization of M of size k. Thus rankpsd (M) ≤ k.

Mij = lim

n→+∞

- Remark 2.14. The result above shows that the function rankpsd : R+p×q → N is lower semicontinuous, i.e., for any convergent sequence Mn → M it holds:


rankpsd (Mn).

rankpsd (M) ≤ liminf n→+∞

It is well-known that the usual rank is also lower-semicontinuous, as well as the nonnegative rank (cf. [BCR11] for the lower semi-continuity property of the nonnegative rank). However, some notions of rank can fail to have this property. A well-known example is the rank of tensors of order ≥ 3 which is not lower-semicontinuous, giving rise to the notion of border rank.

3. Motivation and examples

- 3.1. Geometric interpretation. In this section we discuss the geometric interpretation of the psd rank. This interpretation was in fact the original motivation that led to the deﬁnition of the psd rank in [GPT13].


Semideﬁnite programming is the problem of optimizing a linear function over an aﬃne slice of the psd cone:

minimize L(X) subject to X ∈ S+k ∩ L

where L : Sk → R is a linear function and L is an aﬃne subspace of Sk. The feasible set S+k ∩ L of a semideﬁnite program is known as a spectrahedron and can also be written as the solution set

of a linear matrix inequality {x ∈ Rd : A0 + x1A1 + ··· + xdAd 0} where the Ai are symmetric matrices that span the subspace L. Semideﬁnite programs can be solved to arbitrary precision in polynomial-time, and have many applications in diﬀerent areas of science and engineering [VB96].

Let P ⊂ Rn be a polytope and assume we want to minimize a linear function over P, i.e., we want to compute min{ (x) : x ∈ P}. Observe that if P admits a representation of the form

- (10) P = π(S+k ∩ L)

where L ⊂ Sk is an aﬃne subspace and π is a linear map, then one can write the linear optimization problem over P as a semideﬁnite program of size k, since:

min

x∈P

(x) = min

y∈S+k ∩L

◦ π(y)

and ◦ π is linear. A representation of the polytope P of the form (10) is called a psd lift of size k. Such a representation is interesting in practice when the size d of the lift is much smaller than the number of facets of P, which is the size of the trivial representation of P using linear inequalities. A natural question to ask is thus: what is the smallest k such that P admits a psd lift of size k?

It turns out that the answer to this question is tightly related to the psd rank considered in this paper. For this we need to introduce the notion of a slack matrix:

Deﬁnition 3.1. Let P ⊂ Rn be a polytope (i.e., a bounded polyhedron) and Q ⊂ Rn be a polyhedron with P ⊆ Q. Let x1,...,xv be such that P = conv(x1,...,xv) and let aj ∈ Rn,bj ∈ R, (j = 1,...,f) be such that Q = {x ∈ Rn : aTj x ≤ bj ∀j}. Then the slack matrix of the pair P,Q, denoted SP,Q is the nonnegative v × f matrix whose (i,j)-th entry is bj − aTj xi. When P = Q we write SP := SP,P and we call it the slack matrix of P.

- Remark 3.2. Note that the entries of slack matrix of SP,Q can depend on the inequality description of Q and the vertex description of P (e.g., diﬀerent scalings, redundant inequalities), however it is not hard to see that these do not aﬀect the various ranks of the matrix, namely the usual rank, nonnegative rank and psd rank. Thus we will often refer to a slack matrix of a pair P,Q as “the” slack matrix of P,Q.


The next theorem gives an answer to the question of psd lifts formulated above, using the psd rank: it shows that the size of the smallest psd lift of a polytope P is equal to the psd rank of the slack matrix SP of P (this is the case P = Q of the statement below).

- Theorem 3.3 (cf. Proposition 3.6 in [GRT13b]). Let P ⊂ Rn be a polytope and Q ⊂ Rn be a polyhedron such that P ⊆ Q, and let SP,Q be the slack matrix of the pair P,Q (cf. Deﬁnition 3.1). Then rankpsd SP,Q is the smallest integer k for which there exists an aﬃne subspace L of Sk and a linear map π such that P ⊆ π(S+k ∩ L) ⊆ Q.


Sketch of proof. Let k = rankpsd SP,Q. We ﬁrst show how to construct a spectrahedron S+k ∩L of size k such that P ⊆ π(S+k ∩ L) ⊆ Q for some linear map π. Let x1,...,xv be the vertices of P and let Q = {x ∈ Rn : aTj x ≤ bj ∀j = 1,...,f} be a facet description of Q. Let A1,...,Av,B1,...,Bf ∈ S+k be a psd factorization of SP,Q of size k:

bj − aTj xi = Ai,Bj ∀i = 1,...,v, j = 1,...,f. Consider the convex set C:

- (11) C = {x ∈ Rn : ∃A ∈ S+k such that bj − aTj x = A,Bj ∀j = 1,...,f}. It is easy to verify that C is contained between P and Q: indeed C ⊆ Q because any x ∈ C satisﬁes bj − aTj x ≥ 0 for all j = 1,...,f; also P ⊆ C because the vertices xi of P satisfy (11) with A = Ai.


Also it is not too diﬃcult to show that C can be expressed in the desired form C = π(S+k ∩L) where L is an aﬃne subspace of Sk and π is a linear projection map (we refer to [GRT13b, Proposition 3.6] for the details). Thus this proves the ﬁrst direction.

Assume now that we can write P ⊆ π(S+k ∩ L) ⊆ Q where L is an aﬃne subspace of Sk and π is

a linear map. We show how to construct a psd factorization of SP,Q of size k. Let C = π(S+k ∩ L). Using a suitable choice of basis for L, we can assume that C has the form:

C = {x ∈ Rn : ∃y ∈ Rm such that T(x,y) ∈ S+k }

where T : Rn × Rm → Sk is an aﬃne linear map (i.e., T has the form T(x,y) = U0 + x1U1 + ··· + xnUn + y1V1 + ··· + ymVm for some U0,U1,...,Un,V1,...,Vm ∈ Sk). Observe that since C ⊆ Q we have for any (x,y) ∈ Rn × Rm:

T(x,y) ∈ S+k ⇒ bj − aTj x ≥ 0 ∀j = 1,...,f. By Farkas’ lemma this means that, for any j = 1,...,f, there exists Bj ∈ S+k such that:

- bj − aTj x = T(x,y),Bj ∀(x,y) ∈ Rn × Rm.

Furthermore, since P ⊆ C we know that for any xi vertex of P there exists yi such that T(xi,yi) ∈ S+k . Thus if we let Ai = T(xi,yi) then we get the following psd factorization of size k of the slack matrix SP,Q:

- bj − aTj xi = Ai,Bj ∀i = 1,...,v,j = 1,...,f.


This completes the proof.

Note that the proof of Theorem 3.3 is constructive: it shows how to construct the spectrahedron S+k ∩ L and the linear map π from a psd factorization of SP,Q, and vice-versa.

- Remark 3.4. The geometric interpretation of the psd rank given in Theorem 3.3 can be used to study the psd rank of any arbitrary nonnegative matrix M, since one can show that any nonnegative matrix M is the slack matrix of some pair of polytopes P,Q. We use this geometric interpretation in Section 4 to show that one can use semideﬁnite programming to decide if rankpsd M ≤ 2. Note that if P,Q are full-dimensional polytopes in Rn, then the usual rank of the slack matrix SP,Q is equal to n+1. For example if M is a nonnegative matrix with rank two, then it is the slack matrix of two nested intervals in the real line. It thus follows easily from this geometric interpretation and from Theorem 3.3 that the psd rank of any rank-two matrix is equal to 2 (this was already shown in Proposition 2.8 using a result from [CR93]).


We now illustrate Theorem 3.3 using two simple examples.

- Example 3.5. Let P = Q = [−1,1]2 be the square in the plane. The polytope P has 4 facets and 4 vertices and the slack matrix of P can be shown to be equal to the following 4 × 4 matrix:


  

  .

1 1 0 0 0 1 1 0

- (12) M =


- 0 0 1 1
- 1 0 0 1


One can construct the following psd factorization of M of size 3, showing that rankpsd M ≤ 3: Mij = Ai,Bj where Ai = uiuTi ∈ S+3 ,Bj = vjvjT ∈ S+3 , i,j = 1,...,4 with:

- u1 = (1,0,0), u2 = (0,1,0), u3 = (0,0,1), u4 = (1,1,1)
- v1 = (1,0,0), v2 = (1,−1,0), v3 = (0,1,−1), v4 = (0,0,1).


Thus by Theorem 3.3, this means that one can represent the polytope P = [−1,1]2 as the linear image of a spectrahedron of size 3. One can in fact show that P is the projection onto the (x,y) coordinates of the following spectrahedron T of size 3:

 

 

  0

 

1 x y x 1 z y z 1

(x,y,z) ∈ R3 :

.

T =





### The spectrahedron T (also known as the elliptope) is depicted in Figure 2. Note that no smaller representation of the square [−1,1]2 is possible: it was proved in [GRT13a] that the psd rank of any n-dimensional polytope is at least n + 1 which in this case means that rankpsd M ≥ 2 + 1 = 3.

![image 1](<2014-fawzi-positive-semidefinite-rank_images/imageFile1.png>)

Figure 2. A psd lift of the square [−1,1]2 of size 3: the elliptope {X ∈ S+3 : diag(X) = } linearly projects onto the square [−1,1]2.

Example 3.6. We now give another illustration of Theorem 3.3 where the polytopes P and Q are diﬀerent. Let Q = [−1,1]2 and let now P = [−a,a] × [−b,b] be the rectangle centered at the origin with side lengths 2a and 2b with 0 ≤ a,b ≤ 1 (cf. Figure 3). The slack matrix of the pair P,Q can be easily computed and is given by:

  

  .

1 + a 1 + b 1 − a 1 − b 1 − a 1 + b 1 + a 1 − b 1 − a 1 − b 1 + a 1 + b 1 + a 1 − b 1 − a 1 + b

- (13) M =


- 0

−1−1 0 1

- 1


| |
|---|


b

−b

−a a

Figure 3. The geometric problem associated to the slack matrix M of Equation (13). The inner polytope is P = [−a,a] × [−b,b] and the outer polytope is Q = [−1,1]2. The right ﬁgure shows an instance where there exists an ellipse E such that P ⊂ E ⊂ Q.

Theorem 3.3 says that rankpsd M is equal to the smallest size of a spectrahedron which has a linear projection that is contained between P and Q. In the previous example we saw a spectrahedron of size 3 which projects onto Q = [−1,1]2 and thus this shows that rankpsd M ≤ 3 for all a,b ≤ 1. It is natural to ask whether the psd rank of M can be equal to 2 for some values of a,b? One can actually show that the psd rank of M is equal to 2 if, and only if, there is an ellipse E such that P ⊆ E ⊆ Q (cf. e.g., [GRT13b, Section 4]). It is not hard to see that such an ellipse exists if and only if a2 + b2 ≤ 1. Thus we have the following:

 

3 if a2 + b2 > 1 2 if 0 < a2 + b2 ≤ 1 1 if a = b = 0

rankpsd M =

.



3.2. Information theoretic interpretation. We now describe a diﬀerent application of the psd rank in the area of quantum information theory. Let M be a p×q nonnegative matrix and assume that the entries of M all sum up to 1. Then M can be seen as a joint probability distribution of a pair of random variables (X,Y ), where Mij = P(X = i,Y = j). It is known that a nonnegative factorization of M can be interpreted as a representation of (X,Y ) as a mixture of independent random variables, see e.g., [CR93, Section 6]. As such the nonnegative rank of M deﬁnes a certain measure of correlation between random variables X and Y . In this section we show that a similar interpretation of the psd rank holds, and that rankpsd M gives a measure of correlation between X and Y in terms of quantum information theory. This quantum interpretation of the psd rank was ﬁrst pointed out in the paper [JSWZ13].

- Remark 3.7. We remark that this is not the only known interpretation of the psd rank in quantum information theory: in [FMP+12] the authors show that the psd rank of a matrix M is equal to the one-way quantum communication complexity of computing the matrix M in expectation. Also the psd rank is tightly related to the problem of determining the smallest dimension of a Hilbert space that explains certain measured correlations, see e.g., [BPA+08, WCD08] for more details. For space reasons, however, we focus only on the interpretation of [JSWZ13] in terms of correlation of two random variables X,Y .


3.2.1. Correlation generation. Given a pair of random variables (X,Y ), consider the following correlation generation game: Two parties, Alice and Bob (for short, A and B), want to generate samples from the pair of variables (X,Y ). Alice outputs samples from X and Bob outputs samples from Y and they want to do it in such a way that the samples follow the joint distribution of (X,Y ). Note that if X and Y were independent each party could independently sample from the marginals and they would successfully achieve their objective. However if X and Y are correlated then the two parties A and B must either communicate together or share some common information in order to achieve their task. We will show here that the minimum amount of quantum information that A and B need to have in common is precisely log rankpsd M where M is the matrix giving the joint distribution of (X,Y ). Thus this shows that log rankpsd M gives a measure of the correlation between X and Y in terms of quantum information theory.

i j

#### A B

{Fi} POVM {Gj} POVM

ρ

Central server

Figure 4. Quantum correlation generation problem: A and B generate samples from the joint distribution (X,Y ) using shared information provided by a central server. The psd rank characterizes the minimum amount of quantum information that has to be shared between the two parties.

We ﬁrst recall some basic terminology from quantum information theory. The state of a ﬁnitedimensional quantum system is represented by a Hermitian positive semideﬁnite matrix ρ with trace 1, called a density operator. For convenience, we will work here with real symmetric matrices (instead of complex Hermitian) since our deﬁnition of psd rank involves real symmetric matrices. The state of a bipartite system is described by a density operator ρ of dimension n1n2 where n1 is the dimension of the ﬁrst part (or subsystem) and n2 is the dimension of the second part.

Measurements in quantum mechanics are formalized using the concept of POVM (short for Positive Operator-Valued Measure). A POVM is a ﬁnite collection of psd matrices F1,...,Fp ∈ S+k that satisfy pi=1 Fi = Ik where Ik is the identity matrix. The outcome of measuring a state ρ using a POVM {F1,...,Fp} is i ∈ {1,...,p} with probability trace(Fiρ). Note that trace(Fiρ) ≥ 0 and

p i=1 trace(Fiρ) = trace(ρ) = 1.

Let M be a p × q nonnegative matrix such that Mij = P(X = i,Y = j) where (X,Y ) is a pair of random variables. Assume we have a decomposition of M of the form:

- (14) Mij = trace((Fi ⊗ Gj)ρ) ∀i = 1,...,p, j = 1,...,q


where ρ ∈ Sk2 is a bipartite quantum state (where each subsystem has dimension k) and where {Fi} and {Gj} are POVMs, i.e., Fi,Gj ∈ S+k and pi=1 Fi = qj=1 Gj = Ik. The notation ⊗ here indicates Kronecker product. If there is such a decomposition of M, then one can produce samples from the pair (X,Y ) using the help of a central server as follows (cf. Figure 4): the central server sends the ﬁrst part of the state ρ to Alice and the second part to Bob (each part has dimension k). Alice and Bob perform measurements using POVMs {Fi} and {Gj} respectively and output the outcomes i and j of their measurements. The laws of quantum mechanics say that the outcome (i,j) occurs with probability trace((Fi ⊗ Gj)ρ). Identity (14) thus guarantees that the outputs of Alice and Bob follow the joint distribution of (X,Y ).

The cost of the protocol described above is the number of quantum bits communicated by the central server to Alice and Bob, which in this case is log k (a quantum system of dimension n is represented using log n qubits). We are thus interested in the smallest k for which a decomposition of M of the form (14) exist. It turns out that this is equal to the psd rank of M as we show in the next proposition.

- Proposition 3.8. [JSWZ13] Let M be a p × q nonnegative matrix where all the entries sum up to one. Let k ≥ 1. Then the following are equivalent:


- (i) M admits a psd factorization of size k, i.e., there exist Ai,Bj ∈ S+k such that Mij = Ai,Bj for all i = 1,...,p and j = 1,...,q.
- (ii) There is a quantum protocol for the correlation generation problem using log k qubits, i.e., M admits a factorization of the form (14) of size k. Proof. (ii) ⇒ (i): Assume we have a decomposition of M of the form


Mij = trace((Fi ⊗ Gj)ρ) ∀i = 1,...,p, j = 1,...,q

where Fi ∈ S+k and Gj ∈ S+k are psd matrices such that pi=1 Fi = qj=1 Gj = Ik and ρ ∈ Sk2 is psd such that trace(ρ) = 1. Assume for simplicity that ρ is rank-one, i.e., ρ = ψψT where ψ ∈ Rk2 (the general case is very similar). Since ψ ∈ Rk2 ∼= Rk×k we know that rankψ ≤ k and so we can write:

k

vs ⊗ ws,

ψ =

s=1

where vk,wk ∈ Rk. Let V and W be the matrices with the vs and ws in columns, i.e., V = [v1|...|vk] and W = [w1|...|wk]. Deﬁne Ai = V TFiV and Bj = WTGjW for i = 1,...,p and j = 1,...,q. Clearly Ai and Bj are psd and have size k. We claim that Ai,Bj give a psd factorization of M of

size k. Indeed we have: trace((Fi ⊗ Gj)ψψT) = ψT(Fi ⊗ Gj)ψ

(vs ⊗ ws)T(Fi ⊗ Gj)(vt ⊗ wt)

=

1≤s,t≤k

(=∗)

(vsTFivt)(wsTGjwt)

1≤s,t≤k

= V TFiV,WTGjW = Ai,Bj .

where in (∗) we used the mixed-product property of the Kronecker product (A ⊗ B)(C ⊗ D) = (AC) ⊗ (BD).

(i) ⇒ (ii): We now prove the other direction. Assume we have a psd factorization of M of the form Mij = Ai,Bj where Ai,Bj ∈ S+k . We show how to construct a factorization of the form

- (14). Let ΣA,ΣB be deﬁned respectively by ΣA = pi=1 Ai and ΣB = qj=1 Bj. Note that ΣA and ΣB can be assumed to be invertible (otherwise we can reduce the size of the psd factorization). Consider the matrices Fi and Gj deﬁned by:


Fi = Σ−A1/2AiΣ−A1/2 (i = 1,...,p) and Gj = Σ−B1/2BjΣ−B1/2 (j = 1,...,q).

Then Fi,Gj 0 and pi=1 Fi = qj=1 Gj = Ik. We now construct the state ρ ∈ Sk2 of the protocol. To do so recall that we have the following simple fact: If A and B are symmetric matrices of size k, then

trace(AB) = eT(A ⊗ B)e

where e = vec(Ik) ∈ Rk2 is the vector obtained by stacking all the columns of Ik into a single column of dimension k2. Let ρ ∈ Sk2 be deﬁned by ρ = ψψT where

ψ = (Σ1A/2 ⊗ ΣB1/2)e. First note that ρ is a valid state and trace(ρ) = 1 since

trace(ρ) = ψTψ = eT(ΣA ⊗ ΣB)e = trace(ΣAΣB) =

trace(AiBj) =

Mij = 1.

- 1≤i≤p
- 1≤j≤q


1≤i≤p 1≤j≤q

We now claim that the choice of {Fi},{Gj} and ρ gives a valid decomposition of M as in (14). Indeed we have:

trace((Fi ⊗ Gj)ρ) = ψT(Fi ⊗ Gj)ψ

= eT(Σ1A/2 ⊗ ΣB1/2)(ΣA−1/2AiΣA−1/2 ⊗ ΣB−1/2BjΣB−1/2)(ΣA1/2 ⊗ ΣB1/2)e

= eT(Ai ⊗ Bj)e = trace(AiBj) = Mij.

4. Psd rank two and convex programming

In Proposition 2.8 we showed that if M is a nonnegative matrix with rank(M) ≤ 2 then rankpsd (M) = rank(M). When rank(M) = 3, then inequalities 2.5 imply that rankpsd (M) ≥ 2. In this section we show that one can decide whether rankpsd (M) = 2 using semideﬁnite programming.

We saw in section 3 that any nonnegative matrix M can always be interpreted as the slack matrix of a pair of polyhedra P,Q where P ⊂ Q and where P is bounded. In fact one can always choose the outer polyhedron Q to be bounded as well, as is explained for example in [GG12, Theorem 1]:

- Lemma 4.1. Let M ∈ Rp+×q be a nonnegative matrix and assume that M = . Let r = rankM. Then there exist polytopes P,Q in Rr−1 (where P and Q are bounded) such that P ⊂ Q and such that M is the slack matrix of the pair P,Q.


Proof. The proof is in [GG12] and we reproduce it here for completeness. In [GG12] it is shown that one can always ﬁnd a factorization of M of the form M = AB where A ∈ Rp×r,B ∈ Rr×q and A = and B = . Write A and B as:

  

   B =

  

  ,

aT1 t1

bT1 . bTr

A =

. aTp tp

where ai ∈ Rr−1, ti ∈ R for i = 1,...,p and bj ∈ Rq for all j = 1,...,r. Note that since A = we have ti = 1 − Tai. Deﬁne the polytopes P and Q as follows:

P = conv(a1,...,ap) ⊂ Rr−1 and

r−1

r−1

Q = x ∈ Rr−1 :

xibi + 1 −

xi br ≥ 0 .

i=1

i=1

Note that Q is deﬁned using q linear inequalities. It is not diﬃcult to verify that M is the slack matrix of the pair P,Q. It remains to show that Q is bounded. Assume for contradiction that x0 + αz ∈ Q for all α ≥ 0 where x0 ∈ Q. Then one can show that this implies that

r−1

r−1

zibi −

zi br ≥ 0.

w :=

i=1

i=1

Note that we have Tw = 0 since Tbi = 1 for all i = 1,...,r. Thus since w ≥ 0 and Tw = 0, this means that w = 0, i.e., ri=1−1 zibi − ri=1−1 zi br = 0. Since B is full-rank this necessarily means that z = 0. We have thus shown that Q is bounded.

Assume that rankM = 3 and let P ⊂ Q ⊂ R2 be two polytopes in the plane such that M is the slack matrix of P with respect to Q. From [GRT13b, Proposition 4.1], we know that rankpsd M = 2 if, and only if, there exists an ellipse E such that P ⊂ E ⊂ Q. Since we have a vertex description of P, and a facet description of Q, this can be decided using semideﬁnite programming: Indeed, let x1,...,xv be the vertices of P, and let Q = {x ∈ R2 : Gx ≤ h} be a facet description of Q where

- G has f rows. One can show that there exists an ellipse sandwiched between P and Q if, and only if, there exist A ∈ S2,b ∈ R2 and c ∈ R such that:


- 1. A 0, trace(A) = 1;
- 2.

xj 1

T A b bT c

xj 1 ≤ 0 ∀j = 1,...,v;

- 3. ∃λi ≥ 0 :


0 giT/2

A b bT c

gi/2 −hi ∀i = 1,...,f. The ellipse E that satisﬁes P ⊂ E ⊂ Q is then deﬁned by:

λi

T A b bT c

x 1

x 1 ≤ 0 .

E = x ∈ R2 :

Note that the constraint (2) above corresponds to the condition P ⊆ E and the constraint (3) corresponds to E ⊆ Q. The latter uses the following result commonly known as the S-lemma [BV04, Appendix B]:

- Lemma 4.2. Let Ai ∈ Sn,bi ∈ Rn,ci ∈ R for i = 1,2 and assume that the following implication holds for all x ∈ Rn:


xTA1x + 2bT1 x + c1 ≤ 0 =⇒ xTA2x + 2bT2 x + c2 ≤ 0. Then there exists a λ ≥ 0 such that:

A2 b2 bT2 c2

A1 b1 bT1 c1

λ

.

5. Relationships between ranks Recall from Proposition 2.5 that for a nonnegative matrix M ∈ Rp+×q,

1

1 2

- (15) 2 ≤ rankpsd (M) ≤ rank+ (M). The ﬁrst inequality is equivalent to saying that for all nonnegative matrices M,

rank(M) ≤

rankpsd (M) + 1 2

- (16) .


1 + 8rank(M) −

This says that while rank may be larger than psd rank, it cannot be much larger, since it is bounded above by a quadratic function of the psd rank. In this section, we examine the relationships between the three ranks present in inequality (15) and a fourth type of rank called square root rank. We begin by showing that all inequalities in (15) can be tight. An easy example for the second inequality is the n × n identity matrix for which rankpsd (In) = rank+ (In) = n.

Example 5.1 (Derangement matrices). The n × n derangement matrix Dn is the matrix with zeros on the diagonal and ones elsewhere. It veriﬁes rank(Dn) = n for all n. Fix a positive integer k and let n := k+12 . We will exhibit a factorization of Dn through S+k which will show that rankpsd (Dn) ≤ k, making the ﬁrst inequality tight.

To construct a psd factorization of Dn through S+k choose factors as follows: For i = 1,...,k, let Ai = eieTi where ei is the ith standard basis vector in Rk. Since k+12 = k2 + k, we need to deﬁne k2 further Ai matrices. Let F =

1 −1 −1 1

. For each i,j ∈ {1,...,k} with i < j, deﬁne

Fi,j to be equal to the k × k matrix that has its i,j principal submatrix equal to F and all other entries equal to 0. Let Ak+1 = F1,2, Ak+2 = F1,3, ..., A2k = F2,3,A2k+1 = F2,4, and so on. Now we deﬁne matrices B1,...,Bn for the columns. First, let E be the (k − 1) × (k − 1) matrix with ones on the diagonal and 12 everywhere else. For i = 1,...,k, let Bi be the matrix whose ith row and column are identically zero and whose remaining entries form the matrix E. For i > k, we obtain the matrix Bi from Ai by the following: First change all nonzero entries and all diagonal entries of Ai to ones. Then change all remaining zero entries to 12. Call the resulting matrix Bi. The matrices Ai,Bj form a psd factorization of Dn.

We present the case k = 3 below:





0 1 1 1 1 1 1 0 1 1 1 1

- 1 1 0 1 1 1
- 1 1 1 0 1 1


D6 =

 

 

- 1 1 1 1 0 1
- 1 1 1 1 1 0


Then A1,...,A6 are:

 

  ,

 

  ,

 

 

 

  ,

 

  ,

 

  ,

1 −1 0 −1 1 0

1 0 −1 0 0 0

1 0 0 0 0 0 0 0 0

- 0 0 0
- 0 1 0 0 0 0


0 0 0

- 0 0 0
- 0 1 −1 0 −1 1


- 0 0 0
- 0 0 1


−1 0 1

0 0 0

### and B1,...,B6 are:

 

  ,

 

  ,

 

  ,

 

  ,

 

  .

  ,

 

1 12 1

1 12 12

1 1 12 1 1 12

1 0 12

1 21 0 1 2 1 0 0 0 0

- 0 0 0
- 0 1 12 0 12 1


- 1

- 2 1 12 1 12 1


- 1

- 2 1 1


- 0 0 0
- 1

- 2 0 1


- 1

- 2


- 1

- 2 1


- 1

- 2 1 1


We showed that rankpsd (Dn) = k whenever n = k+12 . Now suppose that n is strictly between

k 2 and k+12 . Then the rank lower bound (ﬁrst inequality in (15)) implies that rankpsd (Dn) > k−1.

Since Dn is a submatrix of D(k+12 ) for which we know a size k psd factorization, rankpsd (Dn) ≤ k. Thus, rankpsd (Dn) = k for these intermediate values of n, or equivalently,

rankpsd (Dn) = min k : n ≤

k + 1 2

for all n.

- 5.1.√ Square root rank: an upper bound for psd rank. Given a nonnegative matrix M, let M denote a Hadamard square root of M obtained by replacing each entry in M by one of its two


possible square roots. Deﬁnition 5.2. The square root rank of a nonnegative matrix M, denoted as rank√ (M), is the minimum rank of a Hadamard square root of M.

For a quick example of square root rank, note that the following matrix M (of rank 3) has rank√ (M) = 2 as evidenced by the shown square root.

 

 

  −→

 

1 0 1

1 0 1 0 1 −2 1 1 −1

√

- 0 1 4
- 1 1 1


M =

M =

Recall from the proof of Theorem 2.9 (v) that if a Hadamard square root of M has rank r then

there is a psd factorization of M by matrices of rank one lying in the psd cone S+r . This implies the following corollary.

Corollary 5.3. For a nonnegative matrix M ∈ Rp×q, rankpsd (M) ≤ rank√ (M). In particular, if M is a 0/1 matrix, then rankpsd (M) ≤ rank(M).

The second statement of Corollary 5.3 says that if a matrix has only the two distinct entries 0 and 1, then its psd rank is bounded above by rank. This was extended by Barvinok [Bar12] to an upper bound on the psd rank of a matrix in terms of its rank and number of distinct entries.

- Lemma 5.4. [Bar12, Lemma 4.4] Let A = (aij) be a real matrix and f : R → R be a polynomial of degree k. If B = (bij) is such that bij = f(aij) for all i,j, then


rank(B) ≤

k + rank(A) k

.

Corollary 5.5. [Bar12, Lemma 4.6] If the number of distinct entries in a nonnegative matrix M does not exceed k, then rankpsd (M) ≤ k−1+rank (k−1 M) .

Proof. Let M be the set of distinct entries in M and φ : M → R be the square root function. Since |M| ≤ k, there exists a polynomial f(t) of degree k − 1 such that φ(t) = f(t) on M. Then by Lemma 5.4 and Corollary 5.3 we have that

√

k − 1 + rank(M) k − 1

M) ≤

rankpsd (M) ≤ rank(

.

While we strongly suspect that it is NP-hard to compute psd rank, there is no proof of this fact at the moment. The situation is clearer for square root rank.

Theorem 5.6. The square root rank of a nonnegative matrix is NP-hard to compute.

Proof. Recall that given a list of n positive integers a1,...,an, the partition problem asks whether there exist sign choices s1,...,sn ∈ {−1,1} such that ni=1 siai = 0. This problem is known to be NP-complete [GJ79].

Given the integers a1,...,an, deﬁne an (n + 1) × (n + 1) matrix A of the form: 



1 0 0 ··· 0 a21 0 1 0 ··· 0 a22 0 0 1 ··· 0 a23 . . .

.

... . .

 

 

- 0 0 0 ··· 1 a2n
- 1 1 1 ··· 1 0


Since A contains the n × n identity matrix as a submatrix, the square root rank of A must be either n or n+1. If

√

√

A by −1 and not aﬀect the rank. Thus, we may assume that the ﬁrst n columns of

A is a Hadamard square root, then we may scale rows and columns of

√

A are composed of zeros and positive ones. With this assumption, we see immediately that there exists a Hadamard square root of rank n if and only if the partition problem for a1,...,an is satisﬁable.

- Remark 5.7. Although the partition problem is NP-complete, it is only weakly NP-complete and admits a pseudo-polynomial time algorithm. Thus, the above theorem does not rule out the existence of an algorithm for deciding rank√ that runs in time polynomial in the problem dimension and the magnitude (not encoding length) of the matrix entries. Furthermore, this embedding of the partition problem cannot hope to show that psd rank is NP-hard to compute. To see this, consider


the matrix A corresponding to the partition problem with integers 5, 12, and 13:

  

  .

1 0 0 25 0 1 0 144

- 0 0 1 169
- 1 1 1 0


This instance of the partition problem is not satisﬁable, yet the matrix A has a 3 × 3 psd factorization. Such a factorization is obtained by placing the matrices

 ,

 

 

 

1 0 −135 0 1 −1213

25 60 65 60 144 156 65 156 169

−135 −1213 1

on the fourth row and the fourth column, respectively, of A and by placing the standard basis factorization of the identity in the ﬁrst three rows and columns.

- 5.2. Lower bounds for psd rank. Lower bounding the psd rank has shown to be a diﬃcult task. In this section, we discuss the known lower bounding techniques and their limitations.


We say that two matrices of the same dimensions have the same support if they share the same zero/nonzero pattern in their entries. Lower bounds based solely on the support of the matrix have been shown to be quite powerful in the case of nonnegative rank (see [FKPT13] for an overview). In the case of psd rank, their power is much more limited. Given a matrix M, the entry-wise square M ◦ M has the same support as M and has psd rank bounded above by rank(M) (Theorem 2.9, part (v)). Thus, a purely support-based bound cannot produce a lower bound that is higher than the rank of M. This observation was extended by Lee and Theis in [LT12] as follows:

- Theorem 5.8. [LT12, Theorem 1.1] Fix a support Z and let MZ be the set of all matrices sharing this support. Then


min

rank(A) = min

rankpsd (A).

A∈MZ

A∈MZ,A≥0

If a nonnegative matrix has the property that it achieves the minimum rank possible among all matrices sharing its support, then the rank is a lower bound to the psd rank. In particular, slack matrices of polytopes have this property. In [GRT13a], the authors showed the following corollary and characterized those polytopes that achieve this lower bound in R2 and R3.

Corollary 5.9. [GRT13a, Proposition 3.2] If P is an n-dimensional polytope with slack matrix SP, then rank(SP) = n + 1 ≤ rankpsd (SP).

To obtain stronger lower bounds, we need to move past using only the support of a matrix. The only known lower bounding techniques that are not purely support based rely on the quantiﬁer elimination theory of Renegar [Ren92] as seen in [GPT13].

We give a high level discussion of the idea behind this technique and then the result. For complete proofs, see [GPT13]. Suppose we are given a convex set C ⊂ Rn that has a psd lift into S+k , i.e. there exists a linear map π and an aﬃne subspace L such that C = π(L ∩ S+k ). Then L ∩ S+k is a semialgebraic set where the bounding polynomials have degree at most k.

- Theorem 5.10. [Ren06] Let Q = {z ∈ Rm : C + ziAi 0} be a spectrahedron with E := C + z iAi 0 for some z ∈ Q, and C,Ai are symmetric matrices of size k × k. Then Q is a semialgebraic set described by g(i)(z) ≥ 0 for i = 1,...,k where g(0)(z) := det(C + ziAi) and g(i)(z) is the i-th Renegar derivative of g(0)(z) in direction E.

The work of Renegar says that when we project this set, the degree and number of the resulting bounding polynomials of C are bounded in k and n.

- Theorem 5.11. [Ren92, Theorem 1.1] Given a formula of the form ∃ y ∈ Rm−n : gi(x,y) ≥ 0 ∀i = 1,...,s


where x ∈ Rn and gi ∈ R[x,y] are polynomials of degree at most d, there exists a quantiﬁer elimination method that produces a quantiﬁer free formula of the form

Ji

I

- (17)


(hij(x)∆ij 0)

i=1

j=1

where hij ∈ R[x], ∆ij ∈ {>,≥,=, =,≤,<} such that I ≤ (sd)Kn(m−n), Ji ≤ (sd)K(m−n) and the degree of hij is at most (sd)K(m−n), where K is a constant.

Multiplying all of these polynomials together, we obtain a single polynomial, whose degree is bounded in k and n, that vanishes on the boundary of C. Hence, if we know that every polynomial that vanishes on the boundary of C must have very high degree, then we can say that C does not have a S+k -lift for small k. The Zariski closure of the boundary of C is a hypersurface in Rn since the boundary of C has codimension one. We deﬁne the degree of C to be the minimal degree of a (nonzero) polynomial whose zero set is the Zariski closure of the boundary of C. By construction, this polynomial vanishes on the boundary of C.

- Proposition 5.12. [GPT13, Proposition 6] If C ⊆ Rn is a full-dimensional convex semialgebraic set with a S+k -lift, then the degree of C is at most kO(k2n).


When C is a polytope, the degree of C is equal to the number of facets, i.e. the minimal polynomial vanishing on the boundary of C is the product of all the linear polynomials determining the facets. This lower bounds the psd rank of slack matrices of polytopes.

- Corollary 5.13. [GPT13, Corollary 4] If C ⊂ Rn is a full-dimensional polytope whose slack matrix has psd rank k, then C has at most kO(k2n) facets.


- Example 5.14. Corollary 5.13 shows that as the number of facets in an n-dimensional polytope in Rn increases, the psd rank of the slack matrix of the polytope has to increase. However, the rank of any such slack matrix stays ﬁxed at n + 1. For example, let Sd be the slack matrix of a d-gon in the plane. Then by Corollary 5.13, rankpsd (Sd) grows to inﬁnity as d increases. As we have seen before, however, rank(Sd) = 3 for all d. This provides a ﬁrst example of a family of matrices with arbitrarily large gap between rank and psd rank.

For non-slack matrices, it can still be possible to apply this lower bound by viewing the matrix as a generalized slack matrix.

- Example 5.15. We now construct a matrix family that has the same zero pattern as the derange-


ment matrices and for which rank is three and psd rank grows arbitrarily large. Let Cd be a convex semialgebraic set in the plane whose bounding polynomial has degree d. By results of Scheiderer

[Sch12], Cd has a S+r -lift for some ﬁnite r, and suppose k is the smallest such r. By Proposition 5.12, d ≤ kO(k2).

Now pick d2 + 1 distinct points on the boundary of Cd and let P be the convex hull of these points. Also, let Q be the polyhedron whose facet inequalities are given by the tangent lines to Cd at the vertices of P. Then the slack matrix of the pair P,Q, which was denoted as SP,Q in Section 3.1, is a nonnegative matrix with the same zero pattern as the derangement matrix. Call this nonnegative matrix Md. By construction, the set Cd is sandwiched between P and Q and its boundary passes through the vertices of P. If C is another convex semialgebraic set that is also sandwiched between P and Q, then its boundary must also contain the vertices of P because P and Q touch at these vertices. By Bezout’s theorem, the degree of C must be at least d + 1. By Theorem 3.3, the psd rank of Md is the smallest k such that a slice of S+k projects to a convex set nested between P and Q. Since this smallest k grows as the degree of the polynomial bounding the projected spectrahedron grows, it must be that the psd rank of Md grows with d.

On the other hand, rank(Md) = 3 since it is the slack matrix of a pair of polygons. Therefore, by choosing a family of convex semialgebraic sets in the plane of increasing degree with the requirements speciﬁed above, one can obtain a family of nonnegative matrices of rank three and growing psd rank. For instance, take

Cd=2t := {(x,y) ∈ R2 : x2t + y2t ≤ 1}.

This quantiﬁer elimination lower bound framework has proven useful for showing that certain families of matrices must have growing psd rank. Its usefulness is limited, however, when considering the psd rank of a single matrix. Other techniques have been developed to show matrices with high psd rank. Bri¨et et. al. used a counting argument in [BDP13] to show that most 0/1-polytopes in Rn have psd rank that is at least exponential in n. Gouveia et. al. produced a lower bound for generic polytopes (polytopes whose vertices are algebraically independent) in [GRT13b], but again, these techniques are of limited usefulness when considering a single speciﬁc matrix. An answer to the following problem would likely provide a new technique that is applicable to many open questions in this ﬁeld.

Problem 5.16. Produce a 10×10 nonnegative matrix M with integral entries such that rank(M) = 3 and rankpsd (M) ≥ 5.

- 5.3. Comparisons between ranks. We can now compare all the ranks seen so far. To keep track, we summarize the relationships in Table 1.


The symbol refers to the rank indexing the row being arbitrarily smaller than the one indexing the column (i.e. there does not exist a function of the row rank that upper bounds the column rank). The symbol < indicates that the rank on the row may be smaller than the rank on the column, but the gap cannot not be arbitrarily large. For example, the entry in the (1,2)-position says that rank may be arbitrarily smaller than nonnegative rank, but never larger. The (1,3)-entry

Table 1. Relationships between various ranks

| | | |rank|rank+|rankpsd<br><br>|rank√|
|---|---|---|---|---|---|---|
|rank rank+ rankpsd rank√<br><br>| | |=<br><br><, <,<br><br>|(5.17)<br><br>= ,<br><br>|(5.14, 5.15) , > (5.1) (5.17)<br><br>=|(5.18), > (5.17) (5.18), (5.17) (5.18)<br><br>=|


says that rank may be smaller or larger than psd rank. The gap in the ﬁrst case may be arbitrarily large, but the gap in the second case is controlled (see (16)). The numbers in the table refer to examples exhibiting the relationship.

## Example 5.17 (Euclidean distance matrices). Consider the n × n Euclidean distance matrix

Mn whose (i,j)-entry is (i−j)2. The rank of Mn is three for all n since Mn = ATnBn where column i of An is (i2,−2i,1) and column j of Bn is (1,j,j2).

The square root rank and psd rank of Mn are two for all n since the matrix with (i,j)-entry equal to i − j has usual rank two. So for all n, the matrix Mn has constant size rank, psd rank, and square root rank.

Now we show that Mn has growing nonnegative rank. Suppose Mn has a Rk+-factorization. Then there exists a1,...,an,b1,...,bn ∈ Rk+ such that ai,bj = 0 for all i = j. Notice that if supp(bj) ⊆ supp(bi) then ai,bi = 0 implies ai,bj = 0, and hence, all the bi’s (and also all the ai’s) must have supports that are pairwise incomparable. Since there are at most 2k possibilities for these supports, n ≤ 2k, or equivalently, k ≥ log2 n. Therefore we get that rank+ (Mn) ≥ log2 n.

In [Hru12], Hrubeˇs exhibited a nonnegative factorization to show that the nonnegative rank of this family is actually Θ(log2 n).

### Example 5.18 (Prime matrices). Let n1,n2,n3,... be an increasing sequence of positive integers such that 2nk −1 is prime for each k. Let Pk denote the set of all primes strictly less than 2nk −1. Deﬁne a k × k matrix Qk such that Qkij = ni + nj − 1. Then Qk has usual rank two for all k. Consequently, by Proposition 2.8, the nonnegative rank and psd rank of Qk are also two for all k. For example, suppose our sequence has the form 2,3,4,6,... Then Q1,...,Q4 will have the form:

  

  .

 

 ,

- 3 4 5 7
- 4 5 6 8
- 5 6 7 9 7 8 9 11


- 3 4 5
- 4 5 6
- 5 6 7


- 3 4
- 4 5


3 ,

,

Note that the top left block of each Qk is Qk−1 and that the diagonal entries of Qk are the increasing sequence of primes, 2n1 − 1,2n2 − 1,...

We will prove by induction that Qk has full square root rank for each k. The base case is clear so assume that Qk−1 has full square root rank, i.e. every possible Hadamard square root of Qk−1 has rank equal to k − 1. Fix a Hadamard square root of Qk and let M be the matrix equal to this square root in every entry except Mkk. Let Mkk be the variable x. The determinant of M has the form αx+β where α and β are in the extension ﬁeld Q(√

Pk). By properties of the determinant, α is equal to the determinant of the top left (k−1)×(k−1) block. Thus by the induction assumption, α is nonzero. Hence, any x making the determinant zero must also lie in Q(√

Pk). However, our square root of Qk must have x = ±

√2nk − 1. Thus, the square root of Qk must have full rank.

The remaining relationship shown in Table 1 that we have not discussed is rank > rank√ . In the example after Deﬁnition 5.2, we saw that rank can be larger than square root rank. The possible gap is controlled, however, since square root rank is an upper bound to psd rank and the gap between rank and psd rank is controlled.

6. Properties of factors

The matrices used as factors in a positive semideﬁnite factorization can sometimes be chosen to satisfy speciﬁc constraints. In this section we explore the ranks and norms of the factors used in a psd factorization.

- 6.1. Rank of factors. In [LT12] it has been shown that we can always pick the factors of a factorization to have some bounded rank, depending only on the size of the matrix:


- Proposition 6.1. [LT12, Lemma 4.5] If a p × q nonnegative matrix M has a S+k factorization, then it has one using factors of rank at most √8q + 1/2 for the rows and at most √8p + 1/2 for the columns.


The reason is simple. If we ﬁx the factors corresponding to rows, the set of valid factors for any given column is the feasible set of a semideﬁnite program, and standard results from convex optimization guarantee the existence of a solution with bounded rank ([Pat98],[Bar01]). Fixing these column factors and repeating the process over the rows we get the result.

We are particularly interested in knowing for which cases can the factors be chosen to have rank one. The answer turns out to be given by the rank√ (M) (Deﬁnition 5.2).

- Proposition 6.2. The square root rank of M, rank√ (M), is precisely the smallest size of a psd factorization of M comprised solely of rank one factors.


Proof. As seen in the proof of Theorem 2.9 (v), if M = N ◦ N and N has rank k, then we can take a rank factorization of N, N = ATB, and use it to create the matrices Ai = aiaTi and Bj = bjbTj , where ai and bj range over the columns of A and B respectively. These matrices Ai and Bj have rank one and, by construction, form a S+k factorization of M.

To prove the reverse implication just note that if viviT and wjwjT form a S+k factorization of M then setting V and W to be the matrices whose columns are the vi and the wj respectively, we can obtain a matrix V TW that has rank k and is a Hadamard square root of M.

In general, we expect the gap between rank√ (M) and rankpsd (M) to be arbitrarily high, as illustrated in Example 5.18, but good knowledge of rank one factorizations can potentially provide some insight into general factorizations.

- Remark 6.3. Let M be a p × q nonnegative matrix with rankpsd (M) = k. Suppose Ai, i = 1,...,p and Bj, j = 1,...,q form a S+k factorization of M. Each Ai can be written as kl=1 vi,lvi,lT , and each Bj as kl=1 wj,lwj,lT . Deﬁne N as the matrix indexed by {1,...,p} × {1,...,k} and {1,...,q} × {1,...,k} whose entry N{i,s},{j,r} is given by (vi,sT wj,r)2.


Then, N ∈ R+pk×qk consists of p × q blocks of size k × k and rank√ (N) = k. Furthermore, summing all the entries of block (i,j) of N gives us entry (i,j) of M.

This remark allows us to transfer properties from rank one factorizations to general factorizations, an example can be seen at the end of the next subsection.

6.2. Norms of factors. Besides rank, another useful quantity to control in the factors is their size. In Section 2 we used a lemma showing that the factors of a semideﬁnite factorization can be rescaled to have small trace. This was instrumental in establishing the lower semicontinuity of psd rank. We restate the lemma here and provide a proof:

- Lemma 6.4. Let M ∈ Rp+×q and assume that M has a psd factorization of size k. Then M admits a psd factorization Mij = Ai,Bj of size k where the factors satisfy trace(Ai) ≤ k and trace(Bj) = pi=1 Mij.


Proof. Let Mij = Ai, Bj be an arbitrary psd factorization of M of size k. Let S = pi=1 Ai ∈ S+k . Deﬁne Ai = S−1/2 AiS−1/2 and let Bj = S1/2 BjS1/2. Note that Ai,Bj = Ai, Bj = Mij and so A1,...,Ap,B1,...,Bq give a valid psd factorization of M of size k. Observe that by construction we have pi=1 Ai = I (where I is the k × k identity matrix), thus necessarily each Ai satisﬁes Ai I and thus trace(Ai) ≤ k. Also we have for any j = 1,...,q, trace(Bj) = trace(( pi=1 Ai)Bj) =

p i=1 trace(AiBj) = pi=1 Mij as desired.

Note that this is equivalent to saying that we can choose Ai and Bj all with trace bounded by k M 1,1 where M 1,1 is the matrix norm induced by the 1-norm in Rk. This looks very similar

to another rescaling result that has proven very useful, the rescaling result in [BDP13], which was used to show that there are 0/1-polytopes with only exponential-sized semideﬁnite representations. The result states that if a matrix M has psd rank k, then it has a semideﬁnite factorization where each factor has largest eigenvalue less than or equal to k M ∞, where M ∞ is the maximum absolute value of an entry in M.

In the remainder of this section we present a new, simpliﬁed proof of this fact. As in [BDP13], the main tool we need is a version of John’s ellipsoid theorem.

- Theorem 6.5 (John’s Theorem). Let C be a full dimensional convex set in Rn and let T : Rn → Rn be a linear map such that the image of the unit ball Bn under T is the unique minimum volume ellipsoid E containing C ∪ −C. Then


1 n

TTT ∈ conv({vvT : v ∈ Boundary(C) ∩ Boundary(E)}). A simple consequence of John’s Theorem has to do with scalability of inner product realizations.

- Corollary 6.6. Suppose U,V ⊆ Rn are bounded and each span Rn, and ∆ = maxu∈U,v∈V | u,v |. Then there exists a linear operator L : Rn → Rn such that maxu∈U Lu 2 and maxv∈V (L−1)Tv 2

are both less than or equal to n1/4

√

∆.

Proof. Consider C = conv(U), and T : Rn → Rn such that T(Bn) is the minimum volume ellipsoid containing C ∪−C. For all u ∈ U, T−1(u) 2 ≤ 1 by construction. Furthermore by John’s theorem for any v ∈ V

TT(v) 22 = vTTTTv = vTn(

i

λiuiuTi )v ≤ n

i

λi ui,v 2

with λi ≥ 0 and λi = 1. But this implies TT(v) 22 ≤ n∆2 and therefore TT(v) 2 ≤

√n∆. By making L = n1/4

√

∆T−1 we get the intended result. This immediately gives us the fact that the usual matrix factorization is scalable.

- Corollary 6.7. If M ∈ Rp×q has rank k, then there exist A ∈ Rk×p, B ∈ Rk×q such that M = ATB and the maximum 2-norm of a column of A or B is at most k1/4 M ∞.

Proof. Start with any rank factorization M = UTV and apply Corollary 6.6 to the columns of U and V . Then A = LU and B = (L−1)TV have the intended properties.

As mentioned in the introduction, factorizations where the factors have small norm have been studied in diﬀerent contexts, particularly in Banach space theory. For example, [LMSS07, Lemma 4.2] is closely related to Corollary 6.7. The scalability of psd factorizations also follows readily.

- Corollary 6.8. If M ∈ Rp+×q has psd rank k, then there exist A1,...,Ap,B1,...,Bq ∈ S+k such that Mi,j = Ai,Bj and the largest eigenvalue of Ai and Bj is bounded above by k M ∞. Proof. Start with a factorization A 1,...,A p,B 1,...,B q ∈ S+k , and let


- U = {u ∈ Rk : A i − uuT 0 for some i},


while

- V = {v ∈ Rk : B j − vvT 0 for some j}.


For u ∈ U and v ∈ V , u,v ≤ M ∞, since

u,v 2 = uuT,vvT ≤ Ai,Bj = Mi,j ≤ M ∞. Applying Corollary 6.6 to U and V we get a linear operator L such that (L−1)Tv and Lu have norm at most 4 k M ∞ for all u ∈ U and v ∈ V . Let Ai = LA iLT and Bj = (L−1)TB jL−1 then

LU = {u ∈ Rk : Ai − uuT 0 for some i}, and

(L−1)TV = {v ∈ Rk : Bj − vvT 0 for some j}. But note that if λ is an eigenvalue of a psd matrix A and x a corresponding eigenvector with x 22 = λ, A − xxT 0. This can be seen by considering an eigenvector decomposition A = λiuiuTi where ui = x/ x 2. In particular this implies that all eigenvalues of matrices Ai can be seen as the square of the norm of a vector in LU, and similarly with the Bj and LV . Hence the maximum eigenvalues in each case are at most k M ∞ as intended.

Note that if we are only interested in getting a bound of k5/4 M ∞ (which is already enough for the application in [BDP13]) we can derive it directly from Corollary 6.7, together with Remark 6.3, illustrating that properties valid for rank one factors can sometimes be extended to general factorizations.

- Remark 6.9. It is worth noting that while Lemma 6.4 and Corollary 6.8 look similar, the bounds they provide are in general not comparable. In general, if M is dense, M 1,1 is expected to be much larger than M ∞ so if the psd rank is low compared to the number of rows of M, we expect the bound from Corollary 6.8 to be signiﬁcantly smaller. For sparse matrices, the same is not true: when applied to the identity matrix for example, Corollary 6.8 can only guarantee factors of largest


√

√

eigenvalue at most

k, a worse guarantee than that obtained directly from Lemma 6.4.

k, hence the trace is at most k

7. Space of factorizations

In this section, we ﬁx a nonnegative matrix M and consider the set of all valid psd factorizations of M as a topological space. In the special case where rank(M) = rankpsd2(M)+1 , we show in

- Proposition 7.3 and Corollary 7.4 that this topological space is closely related to the space of all linear images of the psd cone that nest between two polyhedral cones coming from M. An extension of this result to general M is not possible, as seen in Example 7.5. In Examples 7.7 and 7.8, we use this machinery to construct psd factorizations from the linear embedding of the psd cone. Finally in Proposition 7.9, we show that for rank three matrices with psd rank two, the space of psd factorizations is connected. This contrasts with the nonnegative rank case where it is known that the space of nonnegative factorizations can be disconnected for rank three matrices with nonnegative rank three [MSvS03].


For this section, let M ∈ Rp+×q be a nonnegative matrix with psd rank k. As before, we deﬁne a psd factorization to be a set of matrices (A1,...,Ap,B1,...,Bq) ∈ Sk p+q such that each of the component matrices is psd and Mij = Ai,Bj for each entry in M. We deﬁne the set of all such psd factorizations to be the space of psd factorizations associated to M and denote it by SF(M). Note that this deﬁnition only considers matrices whose size is equal to the psd rank of M.

As a warm-up, it is straightforward to see that SF(M) is closed and inﬁnite. To see that SF(M) is inﬁnite, simply note that for any psd factorization (A1,...,Bq) and any matrix L ∈ GL(k) (the group of invertible k × k matrices), the matrices LTA1L,...,L−1BqL−T also form a psd

factorization of M. We refer to the set of all such psd factorizations as the orbit of (A1,...,Bq) in SF(M). In some cases the entire space of psd factorizations is equivalent to a single orbit.

Example 7.1. Let M be the 3×3 derangement matrix from Example 2.6 (i.e. Mii = 0 and Mij = 1 for i = j). This matrix has usual rank three and psd rank two as shown by the factorization

1 −1 −1 1

1 0 0 0

- 0 0
- 0 1


0 0 0 1

1 0 0 0

1 1 1 1

,

,

,

,

,

.

Let X denote an arbitrary psd factorization of M. The zero pattern of M implies that the matrices composing X must all be rank one. Now it is straightforward to see that there exists an invertible matrix such that conjugation by this matrix will send X to the explicit factorization above. Hence, SF(M) is composed of a single orbit.

The next proposition gives a geometric picture of the space of factorizations in the special case

where rankpsd (M) = k and rank(M) = k+12 . Before proceeding, we present a homogenized version of the geometric interpretation of psd rank that was given in Section 3.1, which will be

easier to work with in this section. First, we homogenize Deﬁnition 3.1:

- Deﬁnition 7.2. Let P and Q be polyhedral cones with P ⊂ Q ⊂ Rn. Let x1,...,xv be the extreme rays of P and let aTj x ≥ 0, (j = 1,...,f) be the inequalities deﬁning Q. Then the slack matrix of the pair P,Q, denoted SP,Q, is the nonnegative v × f matrix whose (i,j)th entry is aTj xi.


By taking a rank factorization, it is easy to see that any nonnegative matrix M can be viewed as SP,Q for some polyhedral cones P and Q whose dimension is equal to rank(M). Furthermore, Theorem 3.3 extends straightforwardly to this conic setting: rankpsd (SP,Q) is the smallest integer k for which there exists a subspace L and a linear map π such that P ⊂ π(S+k ∩ L) ⊂ Q.

In the special case where the cones P and Q come from a matrix M with rankpsd (M) = k and rank(M) = k+12 , we can count dimensions to see that the map π is invertible and the subspace L is all of Sk. If we deﬁne ∆k(P,Q) to be the space of all linear maps π : Sk → R(k+12 ) such that P ⊂ π(S+k ) ⊂ Q, then ∆k(P,Q) is nonempty with M, P, and Q as above. We can actually say much more about ∆k(P,Q) in this special case.

- Proposition 7.3. Let M ∈ Rp+×q with rank(M) = k+12 and rankpsd (M) = k. Fix a rank factorization of M = UV where ui is the ith row of U and vj is the jth column of V . Let P =


cone(u1,...,up) and Q = x | vjTx ≥ 0 for all j be the cones generated by this rank factorization so that M = SP,Q. Then SF(M) is homeomorphic to ∆k(P,Q).

Proof. Suppose (A1,...,Bq) is a psd factorization of M. The set (A1,...,Ap) spans Sk (else we could ﬁnd a lower dimensional rank factorization of M), so we can deﬁne a linear map π by making

π(Ai) = ui. This map is well-deﬁned since if i αiAi and j βjAj are two representations of the same matrix in Sk, then we have that i αiui − j βjuj

T

V = 0. Since V has full row rank,

this implies that i αiui = j βjuj. By the deﬁnition of π, it is immediate that P ⊂ π(S+k ). Since π has the property that π(L),vj = L,Bj for each j, we also have that π(S+k ) ⊂ Q. Thus, we have deﬁned a map from SF(M) to ∆k(P,Q).

Next, suppose that we have π ∈ ∆k(P,Q). Deﬁne Ai = π−1(ui) and Bj = π∗(vj) where π∗ is the

adjoint map. Then Ai ∈ S+k and Bj ∈ (S+k )∗ = S+k and these matrices form a psd factorization of M. This map is the inverse of the one deﬁned above and both of the maps are continuous. Hence, the spaces are homeomorphic.

Both of the spaces in the previous proposition permit a natural action by GL(k). The action on SF(M) was mentioned above when we discussed the orbits of SF(M). The action on ∆k(P,Q)

takes the form g · π(L) = π(gLgT), i.e. we compose the map π with an automorphism of the psd cone. The homeomorphism in the previous proposition respects these group actions so we can descend to the quotient to see the following.

Corollary 7.4. Under the same assumptions as the previous proposition, the spaces SF(M)/GL(k) and ∆k(P,Q)/GL(k) are homeomorphic. Furthermore, ∆k(P,Q)/GL(k) is homeomorphic to the space of all linear images C of S+k such that P ⊂ C ⊂ Q. Proof. The ﬁrst statement is shown by descending to the quotient as discussed prior to the corollary. The second homeomorphism is just given by [π]  → π(S+k ). It is straightforward to check that this map is a well-deﬁned homeomorphism.

The next example shows that the conclusion of Corollary 7.4 cannot hold for general M.

Example 7.5. Let M be the slack matrix of the regular hexagon, i.e. M is the 6 × 6 circulant matrix deﬁned by the vector (0,1,2,2,1,0). It was shown in [GRT13a] that M has rank three, psd rank four, and at least two distinct factorization orbits (since there exists a factorization consisting entirely of rank one matrices and another factorization using both rank one and rank two matrices). Since this matrix is a slack matrix of a polytope, however, the cones P and Q must be equal and the only image nested between them must be P itself. Hence, there cannot exist a bijection between factorization orbits and images nested between P and Q.

In the next examples, we apply our machinery to matrices with rank three and psd rank two.

- Remark 7.6. In light of Corollary 7.4, we can gain new insight on Example 7.1. By taking the trivial rank factorization of the 3 × 3 derangement matrix, we obtain the cones


P = cone((0,1,1),(1,0,1),(1,1,0)) ⊂ R3+ = Q. Dehomogenizing these cones gives us the two triangles seen in Figure 5. In this dehomogenized picture, linear images of the psd cone correspond to ellipses and it is straightforward to see that there is a unique ellipse that ﬁts between the two triangles. Hence, ∆2(P,Q)/GL(2) consists of a single point and by the corollary, the space of psd factorizations is composed of a single orbit.

Figure 5. A space of psd factorizations consisting of a single orbit: The yellow and blue triangles correspond to the dehomogenized cones coming from a rank factorization of the 3 × 3 derangement matrix. The green circle is the unique ellipse that can be nested between the two triangles.

We now show how to apply Proposition 7.3 to ﬁnd diﬀerent psd factorizations of a matrix.

- Example 7.7. In this example, we consider the following matrix M of rank three (shown along


with a rank factorization):

   =

  

  

  

 

 .

3 3 1 1 1 3 3 1 1 1 3 3 3 1 1 3

1 1 1 1 1 −1 1 −1 −1 1 −1 1

2 2 2 2

- 0 1 0 −1
- 1 0 −1 0


By forming the cones P and Q corresponding to this rank factorization and then dehomogenizing through the plane {(1,x2,x3)}, we see that P corresponds to the square centered at the origin of side length two and that Q corresponds to the same square scaled by a factor of two (see Figure 6).

Now any linear image of S+2 corresponds to an ellipse in this dehomogenized picture. So to get a psd factorization of M, we just need to pick an ellipse, ﬁgure out a linear image of S+2 that corresponds to it, and apply the homeomorphism discussed in Proposition 7.3.

For the circle centered at the origin with radius √2, we get the following (where α = √12): 1 + α α α 1 − α

1 − α α α 1 + α

1 − α −α −α 1 + α

1 + α −α −α 1 − α

,

,

,

,

1 −α −α 1

1 − α 0 0 1 + α

1 + α 0 0 1 − α

1 α α 1

,

,

,

.

For the ellipse centered at the origin with horizontal axis of length four and vertical axis of length three, we get the factorization:

1/3 −1/2 −1/2 5/3

5/3 −1/2 −1/2 1/3

5/3 1/2 1/2 1/3

1/3 1/2 1/2 5/3

,

,

,

,

1 −1 −1 1

7/4 0 0 1/4

1 1 1 1

1/4 0 0 7/4

,

,

,

.

It is interesting to note how the ranks of the factors change depending on whether the ellipse contacts the vertices of P or the facets of Q. For example, in the second factorization, the matrices corresponding to the columns are rank one exactly when the corresponding facet of the outer square is tight to the ellipse. Of course, this is not a coincidence, but due to how we construct the psd factorization once we know the linear embedding of the psd cone.

Figure 6. This shows the situation described in Example 7.7. The inner and outer squares correspond to the dehomogenized cones P and Q and any ellipse nested between the two squares corresponds to an orbit of psd factorizations. In the example, we showed factorizations corresponding to both the circle and the ellipse drawn in the ﬁgure.

In every example of a psd factorization that has been presented so far, either the matrices corresponding to the rows or the matrices corresponding to the columns can be chosen to be rank one matrices. Initial attempts to construct a matrix without this property proved fruitless. With the machinery of this section, ﬁnding such an example becomes almost trivial.

- Example 7.8. In this example, we present a 4 × 4 matrix with psd rank two such that every 2 × 2 psd factorization must have a rank two matrix on a row and a rank two matrix on a column. To construct this example, we start with the 3 × 3 derangement matrix as in Example 7.1, which


corresponds to the picture shown in Figure 5. Now we add an extra vertex to the inner triangle and an extra facet to the outer triangle so that neither the new vertex nor the new facet touch the circle, as shown in Figure 7. This corresponds to a new matrix

  

   =

  

  

 

 .

0 1 1 2 1 0 1 2 1 1 0 6 1 1 3 3

0 1 1 1 0 1 1 1 0 1 1 3

1 0 0 3 0 1 0 3 0 0 1 −1

M =

The same circle as before is still the unique ellipse nested between the two polytopes so the space of factorizations consists of a single orbit. When we construct a psd factorization in this orbit, the matrix corresponding to the new vertex must lie in the interior of S+2 and the matrix corresponding to the new facet must lie in the interior of (S+2 )∗. Hence, they must have rank two. Such a factorization may be obtained by augmenting our previous factorization for the derangement matrix with the matrix

1 12 1 2 1

2 −1 −1 2

for the new vertex and the matrix

for the new facet.

Figure 7. Here we take the picture corresponding to the 3×3 derangement matrix and add an additional facet to the outer polytope and an additional vertex to the inner polytope (shown in red). Since the new facet and vertex are not incident to the boundary of the linear embedding of S+2 , their corresponding matrices in the psd factorization must have full rank.

For the special case where M has rank three and we are considering 2 × 2 psd factorizations, we can show that the space of factorization orbits is connected. Proposition 7.9. Let M be a nonnegative p × q matrix with psd rank two and usual rank three. Then SF(M)/GL(2) is connected.

Proof. Let P and Q be the cones in R3 arising from a rank factorization as above. By Corollary 7.4, it is enough to show that ∆2(P,Q)/GL(2) is connected. To do this, we will dehomogenize the cones so that we can work with polytopes and ellipses.

The cone Q must be pointed since it was formed from a full-rank matrix. Thus, we can ﬁnd an aﬃne hyperplane such that the dehomogenization of Q through this hyperplane is bounded. We dehomogenize through this hyperplane to get polytopes P ⊂ Q. Any element of ∆2(P,Q)/GL(2) corresponds to an ellipse nested between P and Q. Thus, to ﬁnish the proof, it is enough to show that any two ellipses that are nested between P and Q can be connected by a path of ellipses.

Suppose E0 and E1 are ellipses nested between the two polytopes. Then there exist quadratic polynomials q0 and q1 such that Ei = {x | qi(x) ≥ 0}. For t ∈ [0,1], deﬁne a quadratic polynomial qt = (1−t)q0 +tq1 and the corresponding ellipse Et. Since q0 and q1 are nonnegative on the points of P, so is qt and we have that P ⊂ Et. Similarly, since q0 and q1 are negative on (E0 ∪ E1)c, we have that Et ⊂ E0 ∪ E1 ⊂ Q. Thus, Et gives the desired path of ellipses.

We are not sure if Proposition 7.9 extends to matrices M with rankpsd (M) = k and rank(M) = k+1

- 2 for k > 2. The proof in the k = 2 case relied on the fact that bounded spectrahedra in S+2 can


be represented by a single polynomial inequality. Higher dimensional spectrahedra require several polynomial inequalities and it is not clear if the proof can be extended to this setting. Searching for a counterexample has also been diﬃcult, since the next case involves linear images of S+3 nested between six-dimensional cones.

8. Symmetric factorizations

In this section we consider nonnegative matrices that admit symmetric psd factorizations where the row and column factors Ai and Bj are required to be the same. Matrices that admit such a factorization are called completely psd [LP13], by analogy to completely positive matrices [BSM03]:

- Deﬁnition 8.1. A symmetric matrix M ∈ Sn is called completely psd if there exists k ∈ N and A1,...,An ∈ S+k such that Mij = Ai,Aj for all i,j = 1,...,n.


The set of matrices that are completely psd forms a convex cone in Sn; we denote this cone by

CPnpsd. Completely psd matrices ﬁnd applications in quantum information theory for the computation of certain quantum graph parameters [LP13].

Recall that a matrix M is called completely positive if there exist nonnegative vectors ai such that Mij = ai,aj for all i,j = 1,...,n. The convex cone of n × n completely positive matrices is denoted by CPn. By representing a nonnegative vector as a diagonal psd matrix it is easy to see that

any completely positive matrix is also completely psd, i.e., CPn ⊆ CPnpsd. It is also clear from the deﬁnition that any completely psd matrix M is necessarily nonnegative and positive semideﬁnite. Thus we have the inclusion

- (18) CPn ⊆ CPnpsd ⊆ DNn


where DNn is the cone of matrices that are nonnegative and positive semideﬁnite (also called doubly nonnegative matrices).

When n ≤ 4 it is known that CPn = DNn and thus the inclusions (18) are all equalities. It is known that for n = 5 the two inclusions (18) are strict [LP13, FW10]:

- • To show that CP5 = CP5psd, one can consider the 5 × 5 matrix M deﬁned by: Mij = cos2

- 4π

- 5


(i − j) , i,j = 1,...,5.

The matrix M is completely psd since it admits the factorization Mij = aiaTi ,ajaTj where ai = (cos(4πi/5),sin(4πi/5)) ∈ R2. On the other hand M ∈/ CP5 since H,M < 0 where H is an element of the dual cone (CP5)∗ known as the Horn form (see e.g., [Du¨r10]):

H =



 

1 −1 1 1 −1

−1 1 −1 1 1 1 −1 1 −1 1 1 1 −1 1 −1

−1 1 1 −1 1



 

.

- • In [LP13, FW10] it was shown that any matrix M ∈ DN5 such that rankM = 3 and whose sparsity pattern is the 5-cycle is not completely psd. One can easily exhibit such a matrix;


thus this shows that CP5psd = DN5 (cf. [LP13, Eq. 3.3] or [FW10, Section 3] for concrete examples).

Several fundamental questions are open concerning the cone CPnpsd. One important question

is to know whether the cone CPnpsd is closed. For a completely-psd matrix M one can deﬁne the cpsd-rank of M as the smallest integer k for which M admits a completely-psd factorization of size

k. The closedness question concerning CPnpsd is related to the question of whether the cpsd-rank of a matrix M ∈ CPnpsd can be bounded from above by a function that depends only on n.

9. Open questions

- 9.1. Psd rank of special matrices. There are very few matrices for which one can determine the psd rank precisely, and when we can, it is usually in very special cases where our coarse bounds such as the square root rank or the trivial rank bound turn out to be suﬃcient. As such, any new insight on determining the psd rank of concrete matrices will provide new tools to analyze psd rank in general. In that spirit, we propose a few more or less concrete matrices whose psd ranks we would like to know, and would provide a starting point for this program.


- Problem 9.1. Consider the 10 by 10 matrix A whose rows and columns are indexed by subsets of {1,...,5} of size 2 and 3 respectively, and deﬁned by AI,J = |I ∩ J|. What is the psd rank of A?

One geometric interpretation for the matrix A, is to take the 10-vertices of a rectiﬁed 5-cell inscribed in a 3-sphere and take the generalized slack matrix with respect to the tangents at the 10-points. Since the unit ball in R4 has a semideﬁnite representation of size 4, we know that the psd rank of A is at most 4. The usual rank of A being 5, we know that its psd rank must be at least 3. If one can show that it is 4 it would prove that there is no smaller semideﬁnite representation of the 3-sphere. A more general version of this problem can be attained by allowing diﬀerent set sizes and diﬀerent numbers of elements.

- Problem 9.2. Let A(n) be the matrix whose rows and columns are indexed by subsets of {1,...,n} of size n/2 and n/2 respectively, and deﬁned by AI,J = |I ∩ J|. What is the psd rank of A(n)?

The matrices A(n) again have an interpretation in terms of an inscribed polytope in the (n−2)-

sphere. In general, we know only that their psd rank is at most 2 √n and at least 12√1 + 8n − 12. These matrices are very special, in the sense that they have a rich symmetry structure. In fact

they are related to the Johnson scheme J(n,k), with k = n/2 , since if Ai,i = 0,...,k are the generators of the associated algebra, A(n) = ki=0 iAi. This justiﬁes posing a more ambitious and less well-deﬁned question.

- Problem 9.3. Let A be a matrix in the Bose-Mesner algebra of the Johnson scheme (or any other association scheme). Can one exploit the symmetry in these matrices to provide non-trivial bounds on their psd ranks?

9.2. Geometry of psd rank. In Section 7, we deﬁned SF(M), the space of psd factorizations of size k of a nonnegative matrix M of rank k+12 and psd rank k. We showed that the quotient space SF(M)/GL(k) is connected when k = 2. There is no reason to believe that such a connectivity result holds in general.

- Problem 9.4. If M is a nonnegative matrix with rankpsd (M) = k and rank(M) = k+12 , then is the space of factorization orbits SF(M)/GL(k) always connected?


The analogous question for nonnegative rank was studied in [MSvS03]. The authors showed examples where M has rank three and the space of nonnegative factorization orbits of size three is disconnected (here the orbit is generated by the permutation group S3, acting by permuting the entries of the nonnegative factorization). A natural question to ask is whether these disconnected factorizations remain disconnected when we embed them in the space of 3 × 3 psd factorization orbits. Embedding these factorizations is straightforward (just make the nonnegative vectors into diagonal matrices), but doing so changes the setting of Problem 9.4 since we are now considering the possible 3×3 psd factorizations of a matrix M with rank three and psd rank two. We are able to show that the factorizations that were disconnected in the nonnegative case become connected when we embed them in the set of 3 × 3 psd factorizations. However, this does not settle Problem 9.4.

- 9.3. Complexity and algorithms. Several complexity questions concerning psd rank are open.


- Problem 9.5. For a ﬁxed constant k, is it NP-hard to decide if rankpsd (M) ≤ k? For example, is it NP-hard to decide if rankpsd (M) = 3?

The equivalent question for the nonnegative rank was shown to be decidable in polynomial time [AGKM12]. The complexity of the algorithm proposed in [AGKM12] is polynomial in p,q (the dimensions of the matrix) but doubly-exponential in k; this was later improved to a singlyexponential algorithm in k in [Moi13]. Both algorithms express the problem of ﬁnding a nonnegative factorization of size k as a semialgebraic system which is then solved using quantiﬁer elimination algorithms [Ren92]. Since the complexity of quantiﬁer elimination algorithms has an exponential dependence on the number of variables, one has to make sure that the number of variables in the semialgebraic system is independent of p,q (the size of the nonnegative matrix) in order to get an algorithm that is polynomial in p,q. The semialgebraic formulations proposed in [Moi13] and [AGKM12] rely on the key fact that the solution of any linear program is a rational function of the data. This fact however is far from being true in semideﬁnite programming [NRS10], and this is one major obstacle in extending these algorithms to the psd rank case.

Another important question is to know the complexity of computing the psd rank (here k is not

a ﬁxed constant anymore). In Section 2 we saw that the psd rank of a matrix M ∈ Rp+×q satisﬁes the following inequalities:

(19) rank(M) ≤

rankpsd (M) + 1 2

and rankpsd (M) ≤ min(p,q)

It is already not known whether deciding if any of these inequalities is tight can be achieved in polynomial-time.

- Problem 9.6. Show that the psd rank is NP-hard to compute. More speciﬁcally show that the problems of deciding whether inequalities (19) are tight are NP-hard.

Note that in [GRT13b, Theorem 4.6], an algorithm is proposed to decide whether the ﬁrst inequality of (19) is tight, however the complexity of the algorithm has an exponential dependence on rank(M) (the complexity of the algorithm is polynomial when rank(M) is a ﬁxed parameter). For the case of the nonnegative rank, it was shown [Vav09] that the problem of deciding whether rank+(M) = rank(M) is NP-hard.

Another interesting question is to ﬁnd eﬃcient algorithms to approximate the psd rank.

- Problem 9.7. Is there a polynomial time approximation algorithm for psd rank (or nonnegative rank) that will ﬁnd a factorization of size at most α · rankpsd (or α · rank+ ) for some constant α?

- 9.4. Slack matrices. The psd rank of slack matrices of polytopes have been of special interest due to its applications to semideﬁnite lifts of polytopes as described in Section 3. For most families of polytopes, the growth rate of the psd rank of their slack matrices is unknown. The tight results that are known are for families where the psd rank is small and grows on the same order as the dimension of the polytopes. A 0/1 polytope is one whose vertices are 0/1 vectors. It was shown in [BDP13] that as n grows, most 0/1-polytopes of dimension n must have psd rank exponential in n. The proof works via a counting argument and does not identify speciﬁc families of polytopes with such exponential psd rank.


- Problem 9.8. Find an explicit family of 0/1-polytopes, {Pn ⊂ Rn}, such that the psd rank of a slack matrix of Pn is exponential in n.


Natural candidates for such examples are polytopes that come from NP-hard combinatorial optimization problems such as cut polytopes and TSP polytopes.

It is unknown whether there exists a family of polytopes that can be expressed by liftings to small psd cones but require large polyhedral lifts. In the language of nonnegative and psd rank, this leads to the following question.

- Problem 9.9. Find a family of polytopes that exhibits a large (e.g. exponential) gap between its psd and nonnegative ranks.

There are several families of polytopes with exponentially many facets (in the dimension of the polytope) that can be expressed by small polyhedral lifts or small psd lifts. The stable set polytope of a perfect graph on n vertices has psd rank n + 1 [GRT13a, Theorem 4.12]. On the other hand, Yannakakis [Yan91, Theorem 5] proved that its nonnegative rank is at most O(nlogn). Is nonnegative rank of the stable set polytope of a perfect graph polynomial in n ? Even if it is not, the gap between psd rank and nonnegative rank would not be dramatic for this family. Polytopes with a large gap between psd rank and nonnegative rank as in Problem 9.9 would show that semideﬁnite programming is truly more powerful than linear programming in expressing linear optimization problems over polytopes.

Goemans observed in [Goe14] that the nonnegative rank of a slack matrix is bounded below by log(v) where v is the number of vertices of the polytope. The same argument shows that log( fi) is a lower bound to nonnegative rank of a polytope where fi is the number of i-dimensional faces of the polytope. It would be interesting to know if there are similar lower bounds for the psd rank of a polytope coming from the combinatorial structure of the polytope.

- Problem 9.10. Develop good bounds on the psd rank of a polytope that use information about its combinatorial/facial structure.

We remark that Corollary 5.13 provides a lower bound to the psd rank of a polytope in terms of the number of facets of the polytope. However, the unknown constants in the bound prevent us from using it to understand speciﬁc polytopes. A result in the spirit of Problem 9.10 from [GRT13b] is that generic polytopes of dimension n with v vertices have psd rank at least (nv)1/4.

- 9.5. Completely positive semideﬁnite matrices. The following open question was raised in Section 8 concerning symmetric psd factorizations.


- Problem 9.11. Let CPnpsd be the set of n × n matrices M that admit a factorization of the form


- (20) Mij = Ai,Aj


where A1,...,An are psd matrices. Does there exist a function f(n) such that any matrix M ∈ CPnpsd admits a factorization of the form (20) where the factors A1,...,An have size at most f(n)? Acknowledgments: We thank Troy Lee for sharing his results on the psd rank of Kronecker products as well on the Hermitian psd rank. The authors also thank Thomas Rothvoß for his helpful input in the proof of Corollary 6.8, and his comments on an earlier draft.

References

[AGKM12] S. Arora, R. Ge, R. Kannan, and A. Moitra. Computing a nonnegative matrix factorization–provably. In Proceedings of the 44th Symposium on Theory of Computing (STOC), pages 145–162. ACM, 2012. 32 [Bar01] A. Barvinok. A remark on the rank of positive semideﬁnite matrices subject to aﬃne constraints. Discrete & Computational Geometry, 25(1):23–31, 2001. 23 [Bar12] A. Barvinok. Approximations of convex bodies by polytopes and by projections of spectrahedra. arXiv preprint arXiv:1204:0471, 2012. 18 [BCR11] C. Bocci, E. Carlini, and F. Rapallo. Perturbation of matrices and nonnegative rank with a view toward statistical models. SIAM Journal on Matrix Analysis and Applications, 32(4):1500–1512, 2011. 9

[BDP13] J. Bri¨et, D. Dadush, and S. Pokutta. On the existence of 0/1 polytopes with high semideﬁnite extension complexity. In Algorithms, ESA 2013, volume 8125 of Lecture Notes in Computer Science, pages 217–228. Springer Berlin Heidelberg, 2013. 21, 24, 25, 32

[BPA+08] N. Brunner, S. Pironio, A. Acin, N. Gisin, A.A. Me´thot, and V. Scarani. Testing the dimension of Hilbert spaces. Physical Review Letters, 100(21):210503, 2008. 13 [BPT12] G. Blekherman, P. A. Parrilo, and R. Thomas, editors. Semideﬁnite Optimization and Convex Algebraic Geometry, volume 13 of MOS-SIAM Series on Optimization. SIAM, 2012. 2

[BSM03] A. Berman and N. Shaked-Monderer. Completely Positive Matrices. World Scientiﬁc Pub Co Inc, 2003.

30 [BV04] S.P. Boyd and L. Vandenberghe. Convex Optimization. Cambridge University Press, 2004. 16 [CR93] J.E. Cohen and U.G. Rothblum. Nonnegative ranks, decompositions, and factorizations of nonnegative

matrices. Linear Algebra and its Applications, 190:149–168, 1993. 2, 4, 5, 11, 13 [Du¨r10] M. D¨ur. Copositive programming–a survey. Recent Advances in Optimization and its Applications in Engineering, pages 3–20, 2010. 30 [FKPT13] S. Fiorini, V. Kaibel, K. Pashkovich, and D. O. Theis. Combinatorial bounds on nonnegative rank and extended formulations. Discrete Mathematics, 313(1):67 – 83, 2013. 19

[FMP+12] S. Fiorini, S. Massar, S. Pokutta, H.R. Tiwary, and R. de Wolf. Linear vs. semideﬁnite extended formulations: Exponential separation and strong lower bounds. In Proceedings of the Forty-fourth Annual ACM Symposium on Theory of Computing, STOC ’12, pages 95–106. ACM, 2012. 3, 13

[FW10] P.E. Frenkel and M. Weiner. On vector conﬁgurations that can be realized in the cone of positive matrices. arXiv preprint arXiv:1004.0686, 2010. 30 [GFR14] J. Gouveia, H. Fawzi, and R. Z. Robinson. Rational and real positive semideﬁnite rank can be diﬀerent. arXiv preprint arXiv:1404.4864, 2014. 6 [GG12] N. Gillis and F. Glineur. On the geometric interpretation of the nonnegative rank. Linear Algebra and its Applications, 437(11):2685–2712, 2012. 15, 16 [GJ79] M. R. Garey and D. S. Johnson. Computers and Intractability: A guide to the theory of NP-completeness. W. H. Freeman and Company, 1979. 19 [Goe14] M. Goemans. Smallest compact formulation for the permutahedron. Mathematical Programming Series B, pages 1–7, 2014. 33 [GPT13] J. Gouveia, P.A. Parrilo, and R.R. Thomas. Lifts of convex sets and cone factorizations. Mathematics of Operations Research, 38(2):248–264, 2013. 2, 3, 4, 9, 20 [GRT13a] J. Gouveia, R. Z. Robinson, and R. R. Thomas. Polytopes of minimum positive semideﬁnite rank. Discrete & Computational Geometry, 50(3):679–699, 2013. 12, 20, 27, 33 [GRT13b] J. Gouveia, R. Z. Robinson, and R. R. Thomas. Worst-case results for positive semideﬁnite rank. arXiv preprint arXiv:1305.4600, 2013. 10, 12, 16, 21, 32, 33 [Hru12] P. Hrubesˇ. On the nonnegative rank of distance matrices. Information Processing Letters, 112:457–461,

2012. 22 [Jol02] I. Jolliﬀe. Principal component analysis. Springer Series in Statistics. Springer, 2nd edition, 2002. 2 [JSWZ13] R. Jain, Y. Shi, Z. Wei, and S. Zhang. Eﬃcient protocols for generating bipartite classical distributions

and quantum states. IEEE Transactions on Information Theory, 59(8):5171–5178, 2013. 3, 13, 14 [Kal63] R. E. Kalman. Mathematical description of linear dynamical systems. Journal of the Society for Industrial & Applied Mathematics, Series A: Control, 1(2):152–192, 1963. 2 [LMSS07] N. Linial, S. Mendelson, G. Schechtman, and A. Shraibman. Complexity measures of sign matrices. Combinatorica, 27(4):439–463, 2007. 2, 24 [LP13] M. Laurent and T. Piovesan. Conic approach to quantum graph parameters using linear optimization over the completely positive semideﬁnite cone. arXiv preprint arXiv:1312.6643, 2013. 30 [LS99] D. D. Lee and H. S. Seung. Learning the parts of objects by non-negative matrix factorization. Nature, 401(6755):788–791, 1999. 2 [LS09] N. Linial and A. Shraibman. Lower bounds in communication complexity based on factorization norms. Random Structures & Algorithms, 34(3):368–394, 2009. 2 [LT12] T. Lee and D. O. Theis. Support-based lower bounds for the positive semideﬁnite rank of a nonnegative matrix. arXiv preprint arXiv:1203.3961, 2012. 19, 23

[LWdW14] T. Lee, Z. Wei, and R. de Wolf. Some upper and lower bounds on psd rank. In preparation, 2014. 6, 7, 8 [Moi13] A. Moitra. An almost optimal algorithm for computing nonnegative rank. In SODA, pages 1454–1464.

SIAM, 2013. 32 [Moo81] B. Moore. Principal component analysis in linear systems: Controllability, observability, and model reduction. IEEE Transactions on Automatic Control, 26(1):17–32, 1981. 2

[MSvS03] D. Mond, J. Smith, and D. van Straten. Stochastic factorizations, sandwiched simplices and the topology of the space of explanations. Royal Soc. Proc., Math. Phys. and Engineering Sciences, 459(2039):2821– 2845, 2003. 2, 25, 31

[NRS10] J. Nie, K. Ranestad, and B. Sturmfels. The algebraic degree of semideﬁnite programming. Mathematical Programming, 122(2):379–405, 2010. 32 [Pat98] G. Pataki. On the rank of extreme matrices in semideﬁnite programs and the multiplicity of optimal eigenvalues. Mathematics of operations research, 23(2):339–358, 1998. 23

[Ren92] J. Renegar. On the computational complexity and geometry of the ﬁrst-order theory of the reals. Part I: Introduction. preliminaries. The geometry of semi-algebraic sets. The decision problem for the existential theory of the reals. Journal of Symbolic Computation, 13(3):255 – 299, 1992. 20, 32

[Ren06] J. Renegar. Hyperbolic programs, and their derivative relaxations. Foundations of Computational Mathematics, 6(1):59–79, 2006. 20 [Sch12] C. Scheiderer. Semideﬁnite representation for convex hulls of real algebraic curves. arXiv preprint arXiv:1208.3865, 2012. 21 [Vav09] S. A. Vavasis. On the complexity of nonnegative matrix factorization. SIAM Journal on Optimization,

20(3):1364–1377, 2009. 32 [VB96] L. Vandenberghe and S. Boyd. Semideﬁnite programming. SIAM Review, 38(1):49–95, 1996. 9 [WCD08] S. Wehner, M. Christandl, and A.C. Doherty. Lower bound on the dimension of a quantum system given

measured data. Physical Review A, 78(6):062112, 2008. 13 [Yan91] M. Yannakakis. Expressing combinatorial optimization problems by linear programs. J. Comput. System Sci., 43(3):441–466, 1991. 2, 33

Laboratory for Information and Decision Systems (LIDS), Massachusetts Institute of Technology,

Cambridge, MA 02139, USA E-mail address: hfawzi@mit.edu CMUC, Department of Mathematics, University of Coimbra, 3001-454 Coimbra, Portugal E-mail address: jgouveia@mat.uc.pt Laboratory for Information and Decision Systems (LIDS), Massachusetts Institute of Technology,

Cambridge, MA 02139, USA E-mail address: parrilo@mit.edu Department of Mathematics, University of Washington, Box 354350, Seattle, WA 98195, USA E-mail address: rzr@uw.edu Department of Mathematics, University of Washington, Box 354350, Seattle, WA 98195, USA E-mail address: rrthomas@uw.edu

