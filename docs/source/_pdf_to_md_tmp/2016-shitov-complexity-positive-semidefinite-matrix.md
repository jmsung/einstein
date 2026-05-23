arXiv:1606.09065v1[math.CO]29Jun2016

THE COMPLEXITY OF POSITIVE SEMIDEFINITE MATRIX FACTORIZATION

YAROSLAV SHITOV

Abstract. Let A be a matrix with nonnegative real entries. The PSD rank of A is the smallest integer k for which there exist k × k real PSD matrices B1, . . . , Bm, C1, . . . , Cn satisfying A(i|j) = tr(BiCj) for all i, j. This paper determines the computational complexity status of the PSD rank. Namely, we show that the problem of computing this function is polynomial-time equivalent to the existential theory of the reals.

1. Introduction

Let A be a nonnegative matrix, that is, a matrix with real nonnegative entries. The positive semideﬁnite (PSD) rank of A is the smallest integer k for which there exist k × k real PSD matrices B1,...,Bm, C1,...,Cn satisfying A(i|j) = tr(BiCj) for all i,j. (Here and in what follows, A(i|j) stands for an (i,j)th entry of A.) As explained in [4], the motivation for the deﬁnition of PSD rank came from geometric problems concerning the representation of convex sets for linear optimization. Namely, the PSD rank is a lower bound on the sizes of semideﬁnite programs that formulate a linear optimization problem over the polytope corresponding to a given matrix, see the discussion in [1, p. 10]. A strongly related quantity is the nonnegative rank, and it is deﬁned in the same way but with an additional assumption that the matrices Bi and Cj are diagonal. Actually, the PSD rank has been introduced as a semideﬁnite analogue of the nonnegative rank, which serves as a lower bound for the sizes of linear programs [10]. We note that the semideﬁnite and linear programming relaxations are concepts that belong to a rapidly developing area of modern computer science. We mention the paper [3], which provides an exponential lower bound for sizes of linear relaxations of several classical NP-complete problems, and the paper [6], which solves the same problem for semideﬁnite relaxations.

In our paper, we discuss the computational complexity of evaluating the PSD rank. The decision version of this problem can be formulated as follows.

- Problem 1.1. (PSD RANK.) Given A ∈ Zm×n and r ∈ Z. Is PSDrank(A) r?


The complexity status of this problem has been wide open. Actually, it was conjectured that PSD rank is NP-hard to compute, see Problem 9.6 in [1] and a discussion in [4, p. 10]. In this paper, we deduce this conjecture as a corollary of a stronger result. Namely, we prove that PSD RANK is polynomial-time equivalent to the problem known as the Existential theory of the reals. A similar equivalence is still an open question for the nonnegative rank, which is only known to be NP-hard, see the original paper by Vavasis [9] and a short proof in [8].

![image 1](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile1.png>)

2010 Mathematics Subject Classiﬁcation. 15A23, 90C22. Key words and phrases. PSD rank, semialgebraic set, computational complexity.

- 1


- 2. ∃R


In this section, we recall the known facts on the existential theory of the reals and formulate our main result. To begin with, we recall the standard description of the yes-instances in Problem 1.1 as a semialgebraic set. If Bi and Cj are k × k PSD matrices, we can write their Cholesky decompositions Bi = kt=1 uitu⊤it and Cj = kτ=1 vjτvjτ⊤ with uit,vjτ ∈ Rk. We get

tr(BiCj) =

tr uitu⊤itvjτvjτ⊤ =

t,τ

(u⊤itvjτ)2.

t,τ

Therefore, a matrix A has PSD rank at most k if and only if the equations (2.1) A(i|j) =

(uit1vjτ1 + ... + uitkvjτk)2

t,τ

have a simultaneous solution uits,vjτσ ∈ R. In other words, PSD RANK is the problem to decide whether the semialgebraic set (2.1) is non-empty. The existential theory of the reals (ETR) is a more general problem in which we allow arbitrary ﬁrst-order quantiﬁer free formulas over (R,+,−,∗,0,1) instead of (2.1).

- Problem 2.1. (EXISTENTIAL THEORY OF THE REALS.) Is a given ﬁrst-order quantiﬁer-free formula over R satisﬁable?


Deﬁning ∃R as the class of decision problems that admit a polynomial reduction from ETR, we see that PSD RANK lies in ∃R.

Remark 2.2. If k > min{m,n} in Problem 1.1, then (A,k) is trivially a yes-instance, so we can assume without loss of generality that k min{m,n}. Now the length of (2.1) is polynomial in the length of (A,k), so (2.1) is indeed a polynomial reduction from PSD RANK to ETR.

The hardest problems in ∃R are called ∃R-complete problems. That is, a problem Π is ∃R-complete if and only if there are polynomial reductions from Π to ETR and from ETR to Π. Our main result states that PSD RANK belongs to this class.

- Theorem 2.3. PSD RANK is ∃R-complete.


The proof of Theorem 2.3 goes as follows. In Section 3, we discuss various problems in ∃R, and we get a suitable restricted version of ETR that is still ∃R-complete. In Section 4, we illustrate the deﬁnition of PSD rank on concrete examples, and we mention several known results that we need in our proof. In Section 5, we introduce the matrix completion problem, which is an essential technique of our proof. In Section 6, we study the connection between this problem and PSD RANK, and we get ready to prove the main result. In Section 7, we ﬁnalize the proof of Theorem 2.3 and discuss a related question arisen from a recent paper by Fawzi, Gouveia, and Robinson.

3. Several ∃R-complete problems

The ETR problem remains ∃R-complete when restricted to formulas consisting of a single polynomial equation, see Proposition 3.2 in the survey [7]. We need a slightly reﬁned version of this statement, so we reproduce the proof as in [7] for the sake of completeness. We deﬁne a monomial as ±xi

is a variable. We say that a polynomial f ∈ Z[x1,...,xn] is in the standard form if it is written as a sum of monomials.

, where each xi

...xi

xi

n

k

2

1

- Theorem 3.1. It is ∃R-complete to decide whether an equation f(x1,...,xn) = 0 has a solution, even if f is written as a sum of monomials.


Proof. Let Φ be a quantiﬁer-free formula. If Φ is a conjunction of polynomial equations Γ = {f1 = 0,...,fk = 0} in which every fi is in standard form, then the equation f12 + ... + fk2 = 0 gives the desired reduction after getting rid of brackets by distributivity.

Before we proceed, we note that the use of negations allows us to assume that every atom in Φ has the form g > 0 for some expression g. We proceed with a construction of the set Γ of polynomials which have a simultaneous solution if and only if Φ is satisﬁable. We start with Γ = ∅. For any atom g > 0, we add to Γ the equation

(gu2g − 1)2 + (wg − 1)2 (g + vg2)2 + wg2 = 0,

where ug,vg,wg are new variables, and wg represents the logical value of the corresponding atom (that is, we have wg = 1 if g > 0 and wg = 0 otherwise). Further, if the variables wa,wb represent the values of Boolean variables a,b, then 1 − wa, wawb, wa + wb − wawb represent ¬a, a ∧ b, a ∨ b, respectively. We can add the corresponding polynomials to Γ, and eventually we get a variable that represents the value of Φ.

Finally, we assume that an equation f = 0 in Γ is such that f = (u ⋆ v) ∗ w with ∗,⋆ ∈ {+,−,·}, and at least one of the expressions u,v,w is not a variable. Then we can add new variables ϕu,ϕv,ϕw and replace f = 0 in Γ by the four equations u − ϕu = 0, v − ϕv = 0, w − ϕw = 0, (ϕu ⋆ ϕv) ∗ ϕw = 0. This way of reasoning eventually allows us to transform all the equations in Γ to the form (yi

= 0, where each yj is either a variable or a constant 0 or 1. All the discussed transformations require time linear in the length of Φ, so the proof is complete.

) ∗ yi

⋆ yi

3

2

1

We need a geometric result by Grigoriev and Vorobjov to proceed with a more restricted version of ETR. The following theorem is a special case of Lemma 9 in [5].

- Theorem 3.2. Let L be the bit length of a polynomial f ∈ Z[x1,...,xn]. Then every connected component of the set {f = 0} has a non-empty intersection with

the ball of the radius 22

CL

centered at the origin, where C is an absolute constant. Now we prove the ∃R-completeness of the problem used in our reduction.

- Theorem 3.3. Theorem 3.1 remains true under an additional restriction that f is forbidden to have a solution outside the cube [−1,1]n.


Proof. Let f be a polynomial as in Theorem 3.1. We will construct a polynomial ϕ without solutions outside [−1,1]n such that the solubility of ϕ = 0 is equivalent to the solubility of f = 0. Our construction requires new variables which we denote by y0,...,ym,z1,...,zn. (Here, m is the number [CL]+1, where L and C are as in Theorem 3.2.) We deﬁne the homogenization of f as h = ymd ·f(x1/ym,...,xn/ym), where d is the degree of f, and we set

m−1

ϕ =

j=0

n

yj+1 − yj2 2 + (2y0 − 1)2 +

i=1

x2i + zi2 − 1 2 + h2.

Getting rid of brackets in ϕ, we get a polynomial that still satisﬁes the requirement of Theorem 3.1. Note that we have constructed ϕ in polynomial time.

If the equality ϕ = 0 is satisﬁed, the ﬁrst two summands of ϕ tell us that yj = 2−2

j

. The third summand shows that xi,zi ∈ [−1,1], so that ϕ satisﬁes the additional requirement of the present theorem. The fourth summand shows that h = 0, which implies that the equality f = 0 is satisﬁable since ym = 0.

Now we check that the satisﬁability of f = 0 implies the satisﬁability of ϕ = 0. If f(ξ1,...,ξn) = 0, then we can assume without loss of generality that |ξi| < 22

m

by Theorem 3.2. We construct a point on {ϕ = 0} as xi = 2−2

![image 2](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile2.png>)

m

j

ξi, yj = 2−2

, zi = 1 − x2i.

Therefore, we have proved that f → ϕ is a polynomial reduction of the problem in Theorem 3.1 to the desired restricted version.

4. Auxiliary results on psd rank

We recall several known results on the PSD ranks of the unit matrix, of the entrywise square A ◦ A of a matrix, of the sum of matrices, and of block matrices. Example 4.1 below appeared as Example 2.11 in [1], and Lemmas 4.2 and 4.3 were a part of Theorem 2.9 in the same paper. Lemma 4.4 was a part of Theorem 2.10 in [1], and Observation 4.5 is an easy consequence of Lemma 4.2. We assume that the matrices appearing in these statements are nonnegative and allow the corresponding matrix operations and constructions of block matrices.

Example 4.1. PSDrank(In) = n.

- Lemma 4.2. PSDrank(A + B) PSDrank(A) + PSDrank(B).
- Lemma 4.3. PSDrank(A ◦ A) rank(A).
- Lemma 4.4. PSDrank


![image 3](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile3.png>)

A B O C

PSDrank(A) + PSDrank(C).

![image 4](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile4.png>)

![image 5](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile5.png>)

- Observation 4.5. PSDrank(A|B) PSDrank(A) + PSDrank(B).
- Observation 4.6. Let M be a nonnegative matrix, assume that (Ai) and (Bj) are families of k × k PSD matrices such that tr(AiBj) = M(i|j) for all i,j. Denote by d the dimension of the linear space spanned by the rows of all matrices in (Aσ). Then PSDrank(M) d.


Proof. The Gram–Schmidt process allows us to construct an orthonormal basis e1,...,ek such that the vectors e1,...,ek−d belong to the intersection of kernels of all of the Aσ’s. We can assume without loss of generality that the tuples (Ai) and (Bj) are written with respect to this basis, and then the ﬁrst k − d rows of Aσ are zero. Therefore, all the non-zero elements of the Aσ’s are located in the bottom-right d × d submatrices. So we get tr(AiBj) = tr(A′iBj′), where A′i, Bj′ are matrices obtained from A, B by cutting oﬀ the ﬁrst k − d rows and columns.

Now we compute the PSD rank of a relevant speciﬁc matrix. Example 4.7. The PSD rank of the matrix

 

 

α 1 1 1 1 0 1 0 1

P(α) =

equals two whenever α ∈ [0,4].

Proof. We get PSDrank(P) 2 by Lemma 4.1. To prove a reversed inequality, we set A2 = B2 = (10 00), A3 = B3 = (00 01), A1 = (a1 a1 ), B1 = 1b 1b , where a,b ∈ [−1,1] are such that 2ab + 2 = α. The Ai’s and Bj’s are PSD, and we can check that tr(AiBj) = P(i|j) for all i,j.

The following is a key result of this section.

- Lemma 4.8. Let S ∈ Rn×n, b ∈ Rn×1, c ∈ R1×n be nonnegative matrices, and let N be a positive integer. Assume that the PSD rank of the matrix


![image 6](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile6.png>)

![image 7](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile7.png>)





0 0 S b . .

![image 8](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile8.png>)

![image 9](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile9.png>)

![image 10](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile10.png>)

![image 11](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile11.png>)

0 0

G =

![image 12](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile12.png>)

![image 13](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile13.png>)

![image 14](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile14.png>)

c N N N 0 ... 0 N N 0 0 ... 0 N 0 N

 

 

![image 15](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile15.png>)

![image 16](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile16.png>)

![image 17](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile17.png>)

![image 18](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile18.png>)

![image 19](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile19.png>)

does not exceed r + 2. Then there is a nonnegative number x such that the matrix A(x) =

![image 20](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile20.png>)

S b c x

has PSD rank at most r.

![image 21](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile21.png>)

![image 22](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile22.png>)

Proof. We label the rows and columns of G by 1,...,n,ν1,ν2 with respect to the order they appear in the deﬁnition of G. There are two tuples, (Aσ) and (Bτ), of PSD matrices of order r + 2 such that tr(AσBτ) = G(σ|τ) for all σ,τ. Using the Cholesky decomposition, we write

- (4.1) Aσ = i

uσiu⊤σi, Bτ =

j

vτjvτj⊤ ,

where i,j enumerate the summands in the decomposition. Here and in the rest of the proof, we assume that they run over {1,...,r + 2}. We get from (4.1) that

- (4.2) tr(AσBτ) = i,j


u⊤σivτj 2 .

Let us denote by U the linear space spanned by the vectors in the decompositions of Aν

2i}. Similarly, we denote by V the linear space spanned by the vectors in the decompositions of Bν

, that is, by the set ∪i{uν

1i,uν

and Aν

2

- 1


. Example 4.1 and Observation 4.6 show that dimU 2, dimV 2, the equality (4.2) shows that the vectors uσi belong to the orthogonal complement V ⊥ if σ ∈ {1,...,n − 1}.

and Bν

2

1

- Step 1. Since dimU + dim U⊥ = r + 2, one has dimU⊥ r. Similarly, we have

dimV ⊥ r.

- Step 2. If dimV ⊥ r−1, then the matrix obtained from A by removing the last


row has PSD rank at most r−1 by Observation 4.6, and we get from Observation 4.5 that PSDrankA(x) r for all x. This would complete the proof of the lemma, so we can assume that dimV ⊥ r, or, taking into account Step 1, that dimV ⊥ = r. Similarly, we get dim U⊥ = r. Using Step 1 again, we get dimU = dimV = 2.

Step 3. Now assume that dim(U + V ⊥) < r + 2. In this case, Observation 4.6 shows that the matrix obtained from G by removing the nth row has PSD rank at most r + 1, so we get from Lemma 4.4 that the matrix obtained from A by removing the last row has PSD rank at most r − 1. As in Step 2, we conclude that PSDrankA(x) r for all x, which would complete the proof of the lemma. So we can assume that dim(U + V ⊥) r + 2, which implies that Rr+2 is a direct sum

of U and V ⊥ after taking into account the result of Step 2. Similarly, we get that Rr+2 is a direct sum of V and U⊥.

Step 4. By the result of Step 3, we have uni = αi + βi with αi ∈ U, βi ∈ V ⊥, and vni = α′i + βi′ with α′i ∈ V and βi′ ∈ U⊥. We deﬁne A′n = i βniβni⊤, Bn′ = and we denote the newly obtained tuples by (A′σ), (Bτ′ ).

- i βniβni′⊤, we replace the matrices An, Bn by A′n, Bn′ in the tuples (Aσ), (Bτ),


We note that, for all p,q ∈ {1,...,n}, one has tr(A′pBq′) = tr(ApBq) unless p = q = n. This means that the tuples (A′p), (Bq′) provide a valid factorization for the matrix A(y) with some value of y. Since for all p ∈ {1,...,n} the rows of the matrices A′p belong to V ⊥, we apply Observation 4.6 and get PSDrank(A(y)) dimV ⊥. So we get PSDrank(A(y)) r by the result of Step 2.

5. A matrix completion problem

Let us consider the set R ∪ {⊛}, where the element ⊛ can be thought of as a ‘real number that is not yet speciﬁed’. A matrix S with entries in R∪{⊛} is called incomplete, and any real matrix C for which C(i|j) = S(i|j) whenever S(i|j) ∈ R is called a completion of S. It will be important for us to consider the following technical condition imposed on incomplete matrices.

- Deﬁnition 5.1. Consider the following property of an incomplete matrix S: For any column index k, there are row indexes i1,i2 and column indexes j1,j2


such that the submatrix S(i1,i2|k,j1,j2) equals (00 10 01). If this holds for both S and S⊤, we say that S satisﬁes the sqrt condition.

This condition is named after the matrix invariant known as sqrt rank, see [1] for details. A reader familiar with this notion can give an equivalent formulation of the lemma below: For any completion C of a matrix satisfying sqrt condition, PSDrank(C) 3 implies sqrtrank(C) 3.

- Lemma 5.2. Let S be an incomplete matrix satisfying the sqrt property. If a completion C of S satisﬁes PSDrank(C) 3, then there is a real matrix Q such that Q ◦ Q = C and rank(Q) 3.


Proof. Let A1,...,An,B1,...,Bm be 3 × 3 PSD matrices satisfying tr(AiBj) = C(i|j) for all i,j. If rank(Ai) 1 and rank(Bj) 1, then we can write Ai = aia⊤i and Bj = bjb⊤j ; in this case, the matrix Q deﬁned as Q(i|j) = a⊤i bj satisﬁes the assumptions of the lemma.

So we can assume that either rank(Ai) > 1 for some i or rank(Bk) > 1 for some k. Since the sqrt condition is invariant under transposition, we assume that rank(Bk) > 1 holds. We get Bk = u1u⊤1 + u2u⊤2 + u3u⊤3 with non-collinear u1,u2 (and possibly zero u3). Let v be a non-zero vector orthogonal to u1,u2; we get At = αtvv⊤ for all t such that Ctk = 0. In other words, any two rows of C having zeros at kth positions are collinear, which contradicts the sqrt condition.

Now we need to introduce the matrix which is the key of our redution from ETR to PSD RANK. This is done in the separate deﬁnition for the ease of subsequent references.

- Deﬁnition 5.3. Let K be a positive integer and S an n×n incomplete matrix. We are going to assign an instance of Problem 1.1 to every pair (S,K) as follows. We denote by E(S) = {e1 = (i1j1),...,ek = (ikjk)} the set of all pairs (i,j) such that


S(i|j) = ⊛. The matrix M = M(S,K) will have 2k +n rows and columns indexed with E1 ∪ E2 ∪ n, where E1,E2 are copies of the set E(S) and n = {1,...,n}. We deﬁne M(i|j) = S(i|j) if (i,j) ∈/ E; if e = (i,j) ∈ E, then we deﬁne the submatrix M(i,e1,e2|j,e1,e2) as KP(1), where P(α) is as in Example 4.7. The entries of M that are not yet deﬁned are set to equal 0.

![image 23](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile23.png>)

![image 24](<2016-shitov-complexity-positive-semidefinite-matrix_images/imageFile24.png>)

- Lemma 5.4. If S admits a completion C such that PSDrank(C) 3 and maxi,j |C(i|j)| K, then PSDrank(M(S,K)) 2k + 3.


Proof. By the deﬁnition of M, the nonzero entries of M − C belong to k disjoint submatrices of the form KP(α) with α ∈ [0,1]. The PSD ranks of these submatrices equal 2 by Example 4.7, so the result follows from Lemma 4.2.

- Lemma 5.5. Let S be an incomplete matrix. If PSDrank(M(S,K)) 2k + 3, then S admits a completion C such that PSDrank(C) 3.


Proof. There is nothing to prove if E is empty, so we assume e = (i,j) ∈ E and proceed by the induction on k (that is, on the cardinality of E). By Lemma 4.8, there is a positive number xij such that, if we remove from M the rows and columns with indexes e1,e2 and replace the (i,j) entry with xij, we will get the matrix M′ with PSD rank at most 2k+1. Note that we have M′ = M(S′,K), where S′ is the matrix obtained from S by replacing the (i,j) entry with xij. Since the number of ⊛-entries of S′ is less than that in S, the result follows by induction.

6. Matrix completion problems and ETR

Now we will work with the ∃R-complete problem discussed in Theorem 3.3. A polynomial f(x1,...,xn) as in this theorem can be written as a sum of monomials. If p = ±xi

is such a monomial, then we deﬁne the set σ(p) as {±1,±xi

...xi

xi

k

2

1

,...,±p}. If f = p1 + ... + ps, then we deﬁne σ(f) = σ(p1) ∪ ... ∪ σ(ps) ∪ {0,±p1,±(p1 + p2),...,±P}.

xi

,±xi

2

1

1

Clearly, the construction of the set σ = σ(f) can be done in time polynomial in the length of f.

We denote by H = H(f) the set of those vectors in σ3 that have one of the coordinates equal to 1. We proceed with the deﬁnition of the three matrices, A =

- A(f), B = B(f), C = C(f), which have their rows and columns indexed with the elements of H.


- Deﬁnition 6.1. Deﬁne A1 as the matrix whose rows are vectors in H, and let A2 be the matrix whose columns are vectors in H. We deﬁne the matrix A over Z[x1,...,xn] as A1A2, that is, we set A(u|v) = (u·v)2, where u·v is the dot product of u and v as vectors in σ3. (In terms of conventional matrix multiplication, u · v stands for u⊤v.)


- Deﬁnition 6.2. B is the matrix with entries in Z ∪ {⊛}, and we set B(u|v) = b if


- A(u|v) is identically equal to b, we also set B(u|v) = 0 in the case when A(u|v) is a multiple of f. In the remaining cases, we set B(u|v) = ⊛. Deﬁnition 6.3. C is the matrix with entries in {0,∗,⊛}. We set C(u|v) = 0 if
- B(u|v) = 0, we set C(u|v) = ⊛ if B(u|v) = ⊛, and also C(u|v) = ∗ if B(u|v) is a nonzero number.


As in the above discussion, the symbol ⊛ can be thought of as a number that is not yet deﬁned. In particular, B belongs to the class of incomplete matrices discussed above. The new symbol, ∗, has a similar meaning as ⊛ but denotes a number required to be non-zero. One can check that these matrices can be constructed in polynomial time.

- Observation 6.4. B satisﬁes the sqrt condition as in Deﬁnition 5.1.


Proof. Let j ∈ σ3 be a column index; by the deﬁnition, one of the coordinates of

- j equals 1. We will consider the case when the ﬁrst coordinate of j equals one, and all the other cases can be considered symmetrically. So we have j = (1,f,g); we deﬁne i1 = (−f,1,0), i2 = (−g,0,1), j1 = (0,1,0), j2 = (0,0,1), and we get


- B(i1,i2|j,j1,j2) = (00 10 01). Since B = B⊤, the result follows.

Lemma 6.5. If f(ξ1,...,ξn) = 0 for some ξi ∈ R, then there is a completion B′ of B such that PSDrank(B′) 3 and |B′(u|v)| 9 (lengthf)4.

Proof. We deﬁne B′ as the entrywise square of the matrix A′ = A(ξ1,...,ξn) obtained from A by substituting the variables xi with numbers ξi. By the deﬁnition, the matrix A′ is a product of the |H|×3 matrix A1(ξ1,...,ξn) and the 3×|H| matrix A2(ξ1,...,ξn). We get rank(A′) 3, and Lemma 4.3 implies PSDrank(B′) 3.

Recall that f satisﬁes the assumption of Theorem 3.3, so that ξi ∈ [−1,1]. In particular, the value of no monomial in the ξi’s can exceed one. We see that the absolute values of the entries of A1(ξ1,...,ξn) and A2(ξ1,...,ξn) cannot exceed (lengthf), which implies the desired bound on the entries of B′.

Now we are going to prove Observation 6.5 in the converse direction. That is, we want to show that existence of a completion of B with PSD rank three implies that f = 0 is satisﬁable. As we will see later, the following is a stronger statement. We say that a matrix D is a completion of the matrix C as in Deﬁnition 6.3 if

- C(u|v) = 0 implies D(u|v) = 0 and C(u|v) = ∗ implies D(u|v) = 0.


- Lemma 6.6. If the matrix C(f) admits a completion D such that rank(D) 3, then the formula f = 0 is satisﬁable.


Proof. Step 1. The completion D satisfying rank(D) 3 can be written as the product of an |H| × 3 matrix and a 3 × |H| matrix. In other words, there are families (pu), (lv) of vectors in R3 such that

(6.1) pu · lv = 0 if C(u|v) = ∗ and pu · lv = 0 if C(u|v) = 0. (The indexes u,v run over the set H.) Let us make the two easy observations, denoted Step 2 and Step 3 for the ease of reference.

- Step 2. The properties (6.1) will not be invalidated under the transformation

(pu,lv) → (B⊤pu,B−1lv), where B is a non-singular 3 × 3 matrix.

- Step 3. The properties (6.1) will not be invalidated under the transformation

(pu,lv) → (λupu,µvlv), where λu,µv are scalars.

- Step 4. Using Step 2, we can assume without loss of generality that p(1,0,0) =


(1,0,0), p(0,1,0) = (0,1,0), p(0,0,1) = (0,0,1), and then the conditions p(1,0,0) · l(1,0,0) = 0, p(0,1,0) · l(1,0,0) = 0, p(0,0,1) · l(1,0,0) = 0 imply that l(1,0,0) = (λ1,0,0) with λ1 = 0. Similarly, we get l(0,1,0) = (0,λ2,0), l(0,0,1) = (0,0,λ3) with non-zero λ2,λ3.

- Step 5. Further, we get from the conditions p(1,1,1)·l(1,0,0) = 0, p(1,1,1)·l(0,1,0) = 0, p(1,1,1) · l(0,0,1) = 0 that p(1,1,1) = (a,b,c) with 0 ∈/ {a,b,c}. Applying Step 2 again, we can assume that p(1,1,1) = (1,1,1).
- Step 6. Applying the transformations as in Steps 2 and 3 to vectors in Steps 4 and 5, we can assume without loss of generality that p(1,0,0) = l(1,0,0) = (1,0,0), p(0,1,0) = l(0,1,0) = (0,1,0), p(0,0,1) = l(0,0,1) = (0,0,1), p(1,1,1) = (1,1,1).
- Step 7. The conditions p(1,0,0) · l(1,0,x


i) = 0 show that l(1,0,x

i) = 0 and p(0,1,0) · l(1,0,x

i) = (1,0,yi) for any variable xi. In what follows, yi denotes the third coordinate of the vector l(1,0,x

i) = (a,0,d) with non-zero a. Using Step 3, we can assume that l(1,0,x

i), and we write x = (x1,...,xn), y = (y1,...,yn).

Step 8. The strategy of the rest of the proof is to check that f(y) = 0. The use of Step 3 allows us to think of the vectors pu, lv as those deﬁned up to a scalar multiplication. We say that the label u = (a(x),b(x),c(x)) is row-good (or column-good) if the vector pu (or lu, respectively) is collinear to (a(y),b(y),c(y)).

- Step 9. The considerations of Steps 6, 7 show that the vectors (1,0,0), (0,1,0),

- (0,0,1), (1,1,1) are row-good, and the vectors (1,0,0), (0,1,0), (0,0,1), (1,0,xi)

are column-good. Similarly, l(0,−1,1) is orthogonal to the row-good vectors (1,0,0) and (1,1,1), so that (0,−1,1) is column-good.

- Step 10. Now assume that a vector (g,0,h) is column-good. The vector p(−h,g,g) is then orthogonal to column-good vectors (g,0,h) and (0,−1,1), so that (−h,g,g) is a row-good vector. Now the vector (g,h,0) is column-good because l(g,h,0) is orthogonal to row-good vectors (0,0,1) and (−h,g,g).
- Step 11. If (g,0,h) is column-good, the vector (−h,0,g) is row-good because it is orthogonal to column-good vectors (g,0,h) and (0,1,0). The symmetry and Step 10 imply that, in the case when (g,0,h) is column-good, any permutation of (g,h,0) is column-good and any permutation of (−h,0,g) is row-good.
- Step 12. Let us now assume that (1,0,α), (1,0,β) are column-good. Step 12.1. Assume α + β ∈ σ. We see that (−1,1,α) is column-good because it is orthogonal to vectors (1,1,0) and (0,−α,1), which are row-good by Steps 9 and 11. Now we see that (−β,−α − β,1) is row-good because it is orthogonal to the column-good vectors (−1,1,α) and (1,0,β). Finally, the vector (0,1,α + β) is column-good because it is orthogonal to the row-good vectors (−β,−α − β,1) and


- (1,0,0). The vector (1,0,α + β) is column-good by Step 11. Step 12.2. Assume α − β ∈ σ. We see that (−1,−1,α) is row-good because it is




orthogonal to the vectors (1,−1,0) and (0,α,1), which are column-good by Steps 9 and 11. Now we see that (β,α − β,1) is column-good because it is orthogonal to the row-good vectors (−1,−1,α) and (1,0,−β). The vector (0,1,β − α) is rowgood because it is orthogonal to the column-good vectors (β,α − β,1) and (1,0,0). Finally, we see that (0,α − β,1) is a column-good vector since it is orthogonal to the row-good vectors (1,0,β − α) and (0,1,0). Step 11 shows that (1,0,α − β) is column-good as well.

Step 12.3. Assume αβ ∈ σ. The vector (αβ,1,α) is column-good because it is orthogonal to the vectors (0,−α,1) and (1,0,−β), which are row-good by Step 10. The vector (1,−αβ,0) is row-good because it is orthogonal to the column-good vectors (0,0,1) and (αβ,1,α). Finally, we see that (αβ,1,0) is a column-good vector because it is orthogonal to row-good vectors (1,−αβ,0) and (0,0,1). Step 10 implies that (1,0,αβ) is column-good as well.

Step 13. The results of Step 12 show that the vector (1,0,s) is column-good for

all s ∈ σ. We get that p(0,0,1) · l(1,0,f) = 0 because C((0,0,1)|(1,0,f)) = 0, which means that (0,0,1) · (1,0,f(y)) = 0 or f(y) = 0. The proof is complete.

We conclude the section with the desired proof of the statement converse to

- Observation 6.5.


- Lemma 6.7. If the matrix B(f) admits a completion B′ such that PSDrank(B′) 3, then the formula f = 0 is satisﬁable.


Proof. Observation 6.4 shows that B possesses the sqrt property, so Lemma 5.2 is applicable. Since B admits a completion B′ with PSDrank(B′) 3, we see that there is a matrix C′ with rank at most three such that B′ = C′ ◦ C′. We see that C′ is a rank-three completion of C, so the formula f = 0 is satisﬁable by

- Lemma 6.6.


7. The main result

Let us ﬁnalize the proof of the main result. Theorem 2.3 follows directly from Remark 2.2 and the theorem below. Theorem 7.1. There is a polynomial-time reduction from ETR to PSD rank.

Proof. The problem in Theorem 3.3 is ∃R-complete, so we can construct a reduction from it. For an instance f of this problem, we construct the matrix B = B(f) as in Deﬁnition 6.2, we denote by k the number of ⊛-entries of B, and we set K = 9 (lengthf)4. We construct the matrix M = M(B,K) as in Section 6, and we claim that ρ : f → (M,2k + 3) is a desired reduction. As we noted in the above discussion, the matrix B can be constructed in time polynomial in the length of f; the matrix M can be constructed in time polynomial in the length of (B,K), so the function ρ can be computed in polynomial time.

Now let f be a yes-instance. By Lemma 6.5, there is a completion B′ of B such that PSDrank(B′) 3 and |B′(u|v)| K. Lemma 5.4 implies PSDrank(M)

- 2k + 3, that is, ρ(f) is a yes-instance of PSD RANK. Finally, let f be a no-instance. By Lemma 6.7, B admits no completion B′ such


that PSDrank(B′) 3. Lemma 5.5 implies PSDrank(M) > 2k + 3, so that ρ(f) is a no-instance of PSD RANK.

The technique developed in this paper allows us to prove another interesting result. For any subﬁeld F ⊂ R, we can deﬁne a similar PSD rank function but with a requirement that the entries of matrices in the factorization belong to F. We consider a polynomial f ∈ Z[x] that is irreducible over Q but has a root r in R. In the notation of the proof of Theorem 7.1, the matrix M(B(f),K) has PSD rank 2k+3 with respect to Q(r). However, the argument as in Lemmas 6.6 and 6.7 shows that every rational completion of B(f) has PSD rank at least four. We can argue as in Lemmas 4.8 and 5.5 and prove that the rational PSD rank of M is greater than 2k + 3. In other words, the PSD ranks deﬁned with respect to Q and Q(r) represent diﬀerent functions of rational matrices, for any irrational number r ∈ R. This is a generalization of the result proved in [2] by Fawzi, Gouveia, and Robinson.

References

- [1] H. Fawzi, J. Gouveia, P. A. Parrilo, R. Z. Robinson, R. R. Thomas, Positive semideﬁnite rank, Mathematical Programming 153 (2015) 133–177.
- [2] H. Fawzi, J. Gouveia, R. Z. Robinson, Rational and real positive semideﬁnite rank can be diﬀerent, Operations Research Letters 44 (2016) 59–60.
- [3] S. Fiorini, S. Massar, S. Pokutta, H.R. Tiwary, R. de Wolf, Linear vs. semideﬁnite extended formulations: Exponential separation and strong lower bounds, Proceedings of the Forty-fourth Annual Symposium on Theory of Computing (2012) 95–106.
- [4] J. Gouveia, R. Z. Robinson, R. R. Thomas, Worst-case results for positive semideﬁnite rank, Mathematical Programming 153 (2015) 201–212.
- [5] D. V. Grigoriev, N. N. Vorobjov, Solving systems of polynomial inequalities in subexponential time, Journal of Symbolic Computation, 5 (1988) 37–64.
- [6] J. R. Lee, P. Raghavendra, D. Steurer, Lower bounds on the size of semideﬁnite programming relaxations, Proceedings of the Forty-Seventh Annual ACM on Symposium on Theory of Computing (2015) 567–576.
- [7] J. Matousˇek, Intersection graphs of segments and ∃R, preprint (2014) arXiv:1406.2326.
- [8] Y. Shitov, A short proof that NMF is NP-hard, preprint (2016) arXiv:1605.04000.
- [9] S. Vavasis, On the complexity of nonnegative matrix factorization, SIAM J. Optimization 20

(2009) 1364–1377.

- [10] M. Yannakakis, Expressing combinatorial optimization problems by linear programs, Comput. System Sci. 43 (1991) 441–466.


National Research University Higher School of Economics, 20 Myasnitskaya Ulitsa, Moscow 101000, Russia

E-mail address: yaroslav-shitov@yandex.ru

