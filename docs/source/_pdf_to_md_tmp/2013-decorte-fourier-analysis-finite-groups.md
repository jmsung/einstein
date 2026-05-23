arXiv:1307.5703v1[math.OC]22Jul2013

FOURIER ANALYSIS ON FINITE GROUPS AND THE LOVASZ´ THETA-NUMBER OF CAYLEY GRAPHS

EVAN DECORTE, DAVID DE LAAT, AND FRANK VALLENTIN

Abstract. We apply Fourier analysis on ﬁnite groups to obtain simpliﬁed formulations for the Lova´sz ϑ-number of a Cayley graph. We put these formulations to use by checking a few cases of a conjecture of Ellis, Friedgut, and Pilpel made in a recent article proving a version of the Erd˝s-Ko-Rado theorem for k-intersecting families of permutations. We also introduce a q-analog of the notion of k-intersecting families of permutations, and we verify a few cases of the corresponding Erd˝s-Ko-Rado assertion by computer.

1. Introduction

One approach to some problems in extremal combinatorics involves estimating the independence number of a Cayley graph. A classic example is upper bounding sizes of error-correcting codes in Abelian groups. A recent, exciting example is provided by a version of the Erdo˝s-Ko-Rado theorem for permutations proven by Ellis, Friedgut, and Pilpel [4]: If k is a positive integer, n is suﬃciently large depending on k, and A is a largest set of permutations on n letters such that any two agree on at least k letters, then |A| = (n − k)!. This resolved a conjecture of Frankl and Deza from [6] stated in 1977.

The Lov´asz ϑ-number, introduced in [9], provides an upper bound on the size of an independent set in a general graph. It can be computed by solving a semideﬁnite program involving n × n-matrices, where n is the cardinality of the vertex set. We specialize the ϑ-number to Cayley graphs and show how the semideﬁnite program block-diagonalizes to a simpler one involving smaller matrices associated to the irreducible representations of the group. The resulting semideﬁnite program can be thought of as a “frequency domain” formulation of the ϑ-number. Furthermore, under a suﬃcient condition on the graph, our semideﬁnite program collapses to a linear program which can be formulated using only knowledge of the group characters. This condition applies, in particular, for the two examples given above. In fact, one can interpret the arguments in [4] as constructing feasible solutions to the linear program computing the ϑ-number for a particular Cayley graph on the symmetric group.

In [4], the problem of quantifying the dependence of n on k is left open, but they conjecture that the conclusion of their theorem holds when n ≥ 2k + 1. By explicit computations we verify their conjecture for some small values of n and k, and we identify some values for which the ϑ-number does not give a tight enough bound to verify the conjecture, suggesting that other methods will be required to resolve these cases.

![image 1](<2013-decorte-fourier-analysis-finite-groups_images/imageFile1.png>)

Date: July 21, 2013. 1991 Mathematics Subject Classiﬁcation. 05A05, 20C30, 90C22. Key words and phrases. Lova´sz theta number, Cayley graphs of ﬁnite groups, independent sets,

Erd˝s-Ko-Rado theorems, intersecting families of permutations (and its q-analog), ﬁnite Fourier analysis.

The authors were supported by Vidi grant 639.032.917 from the Netherlands Organization for Scientiﬁc Research (NWO).

1

The outline of the paper is as follows: In Section 2 we ﬁx notation and deﬁnitions, and recall some basic facts from ﬁnite Fourier analysis. In Section 3 we ﬁnd several reformulations of the Lov´asz ϑ-function for Cayley graphs by using the group structure on the vertex set. In Section 4 we apply these results in the context of the Ellis-Friedgut-Pilpel conjecture made in [4], and in Section 5 we introduce a q-analog of their result as a conjecture, and perform the analogous computations. In Section 6, we show how the machinery developed in Section 3 could also be applied to vertex-transitive graphs.

2. Definitions, notation, and background in Fourier analysis

All graphs will be simple and undirected. For any graph G = (V,E), the independence number is the maximum number of pairwise nonadjacent vertices; this maximum will be denoted α(G).

Suppose Γ is a ﬁnite group. A subset X ⊆ Γ will be called a connection set if the unit element e of Γ does not belong to X, and if X is inverse-closed; that is x−1 ∈ X whenever x ∈ X. For any connection set X ⊆ Γ, the Cayley graph Cay(Γ,X) is the graph with vertex set Γ, where two vertices x and y are adjacent if and only if y−1x ∈ X. The deﬁning conditions of a connection set imply that Cay(Γ,X) is an undirected graph without self-loops. Notice that we do not require X to generate Γ; therefore Cay(Γ,X) need not be connected.

In the following we recall some basic facts from representation theory of ﬁnite groups. For a good reference, see for instance Terras [10]. A (ﬁnite-dimensional) unitary representation of Γ is a group homomorphism π: Γ → U(dπ) where U(dπ) is the group of unitary dπ ×dπ matrices. The number dπ is called the degree of π. The character of π is deﬁned as χπ(γ) = Tr(π(γ)), where Tr denotes trace. A subspace M of Cdπ

is π-invariant if π(γ)m ∈ M for all γ ∈ Γ and m ∈ M. The unitary representation π is said to be irreducible if {0} and Cdπ

are the only π-invariant subspaces of Cdπ

. Two unitary representations π and π′ are (unitarily) equivalent if there is a unitary matrix T such that Tπ(γ) = π′(γ)T for all γ ∈ Γ.

Given two inequivalent irreducible unitary representations π and π′, the Schur orthogonality relations give us the following two facts:

- (1) γ∈Γ πij(γ)πlk′ (γ) = 0, where πij(γ) is the ij-entry of the matrix π(γ), and πlk′ (γ) is deﬁned analogously;

![image 2](<2013-decorte-fourier-analysis-finite-groups_images/imageFile2.png>)

- (2) γ∈Γ πij(γ)πlk(γ) = |dΓ|


![image 3](<2013-decorte-fourier-analysis-finite-groups_images/imageFile3.png>)

δilδjk, where δ is the Kronecker delta.

![image 4](<2013-decorte-fourier-analysis-finite-groups_images/imageFile4.png>)

π

These relations are implied by Schur’s lemma, which says that if π and π′ are irreducible unitary representations, and if T is a matrix for which Tπ(γ) = π′(γ)T for all γ ∈ Γ, then T is either invertible or zero; if π = π′, then T is a scalar multiple of the identity matrix.

We ﬁx a set of mutually inequivalent irreducible unitary representations of Γ, so that each unitary equivalence class has a representative; call this set Γ.ˆ This allows us to deﬁne the Fourier transform of a function f : Γ → C:

fˆ(π) =

f(γ)π(γ),

γ∈Γ

where fˆ(π) is a complex dπ × dπ matrix. The Fourier inversion formula says we can recover f from its Fourier transform:

f(γ) =

1 |Γ|

dπ f ˆ(π),π(γ) .

![image 5](<2013-decorte-fourier-analysis-finite-groups_images/imageFile5.png>)

π∈Γˆ

The inner product used here is the trace inner product, deﬁned as A,B = Tr(B∗A) for square complex matrices A and B of the same dimension, where B∗ denotes the conjugate-transpose of B.

The convolution of two functions f : Γ → C and g: Γ → C is deﬁned by f ∗ g(γ) =

f(β)g(β−1γ),

β∈Γ

![image 6](<2013-decorte-fourier-analysis-finite-groups_images/imageFile6.png>)

and the involution of f is deﬁned as f∗(γ) = f(γ−1). It is a fact that f ∗ g(π) = fˆ(π)ˆg(π), and that f∗(π) = fˆ(π)∗.

A function f : Γ → C is of positive type if

g ∗ g∗(γ)f(γ) ≥ 0

γ∈Γ

for all functions g: Γ → C; that is, the sum is a nonnegative real number. We denote by P(Γ) the set of functions on Γ of positive type. Notice that f ∈ P(Γ) if and only if f¯ ∈ P(Γ), where f¯ is the pointwise complex-conjugate of f. One fact that will be needed later is that f(γ−1) = f(γ) for all γ ∈ Γ when f is of positive type. For a proof of this fact and more information on functions of positive type, see Folland [5, Chapter 3.3].

![image 7](<2013-decorte-fourier-analysis-finite-groups_images/imageFile7.png>)

For vectors u,v ∈ Cn, we use u,v to denote the usual inner product of u and v. An n × n matrix A with entries from C will be called positive semideﬁnite if

Av,v is a nonnegative real number for all v ∈ Cn. Using the polarization identity, it is possible to prove that every positive semideﬁnite matrix is Hermitian. For each ﬁnite set V , the set of positive semideﬁnite matrices with rows and columns indexed on V will be denoted SV 0. When V = {1,...,n}, we will use the notation Sn 0 instead. It is a fact that A ∈ Sn 0 if and only if A,B ≥ 0 for all B ∈ Sn 0; this fact is known as the self-duality of Sn 0.

The following theorem is an application of self-duality, as well as Parseval’s identity, which says that

1 |Γ|

![image 8](<2013-decorte-fourier-analysis-finite-groups_images/imageFile8.png>)

f(γ)g(γ) =

![image 9](<2013-decorte-fourier-analysis-finite-groups_images/imageFile9.png>)

γ∈Γ

dπ f ˆ(π),gˆ(π)

π∈Γˆ

for all functions f and g on Γ:

- Theorem 1 (Bochner’s theorem for ﬁnite groups). Suppose Γ is a ﬁnite group and let f : Γ → C. Then f is of positive type if and only if fˆ(π) is positive semideﬁnite for each π ∈ Γˆ. Proof. For any two complex-valued functions f and g on Γ, we have


(1)

1 |Γ|

g ∗ g∗(γ)f(γ) =

![image 10](<2013-decorte-fourier-analysis-finite-groups_images/imageFile10.png>)

![image 11](<2013-decorte-fourier-analysis-finite-groups_images/imageFile11.png>)

γ∈Γ

1 |Γ|

dπ g ∗ g∗(π),fˆ(π) =

![image 12](<2013-decorte-fourier-analysis-finite-groups_images/imageFile12.png>)

π∈Γˆ

dπ g ˆ(π)ˆg(π)∗,fˆ(π) .

π∈Γˆ

The matrices gˆ(π)ˆg(π)∗ are always positive semideﬁnite, so (1) is nonnegative if all the matrices fˆ(π) are positive semideﬁnite. This gives one direction.

For the other direction, suppose f : Γ → C is of positive type, and ﬁx π ∈ Γ.ˆ Now let A ∈ Sd

0 be arbitrary, and let A = BB∗ be the Cholesky decomposition. Deﬁne g: Γ → C by g(γ) = dπ/|Γ| B,π(γ) . By the Schur orthogonality relations (or uniqueness of Fourier coeﬃcients), we have gˆ(π) = B and gˆ(π′) = 0 when π′ and π are inequivalent, whence

π

gˆ(π)ˆg(π)∗ = BB∗ = A and gˆ(π′)ˆg(π′)∗ = 0.

Now (1), which is nonnegative by hypotheses, is equal to dπ/|Γ| A,fˆ(π) . Since π and A were arbitrary, we conclude that A,fˆ(π) ≥ 0 for every π and every A ∈ Sd

0 now implies fˆ(π) ∈ Sd

0 for each π ∈ Γ.ˆ

0. Self-duality of Sd

π

π

π

3. The ϑ-number of a Cayley graph

Let G = (V,E) be a ﬁnite graph. In [9], the Lov´asz ϑ-number ϑ(G) of G is deﬁned and a number of equivalent formulations are given. The formulation of ϑ(G) which will be most important for us is:

- (A) A(u,v) : A ∈ SV 0 real-valued, Tr(A) = 1, A(u,v) = 0 for {u,v} ∈ E .

When G is the Cayley graph Cay(Γ,X), the optimization over matrices in (A) can be replaced with optimization over functions on Γ, as we proceed to show.

Theorem 2. Suppose G = Cay(Γ,X). Then ϑ(G) = max

γ∈Γ

- (B) f(γ) : f ∈ P(Γ) real-valued, f(e) = 1, f(x) = 0 for x ∈ X .


ϑ(G) = max

u,v∈V

Before we prove Theorem 2, we require a lemma:

Lemma 3. Suppose A: Γ × Γ → C is a Hermitian matrix satisfying A(γ,e) = A(γβ,β) for all γ,β ∈ Γ. Deﬁne f : Γ → C by f(γ) = A(γ,e). Then for any function g: Γ → C we have

g ∗ g∗(γ)f(γ) =

g(γ)g(γ′)A(γ,γ′).

![image 13](<2013-decorte-fourier-analysis-finite-groups_images/imageFile13.png>)

γ∈Γ

γ,γ′∈Γ

Proof. This follows from a straightforward computation. Proof of Theorem 2. For one direction, let A be a feasible solution for (A). Deﬁne A¯: Γ × Γ → R entrywise by

1 |Γ| β∈Γ

A¯(γ,γ′) =

A(γβ,γ′β).

![image 14](<2013-decorte-fourier-analysis-finite-groups_images/imageFile14.png>)

Being the average of matrices similar to A (via permutation matrices), the matrix A¯ is positive semideﬁnite, and one now easily checks that A¯ is again a feasible solution for (A) having the same objective value as A. Moreover, we have A¯(γ,e) = A¯(γβ,β) for all γ,β ∈ Γ.

Now deﬁne f : Γ → R by f(γ) = |Γ|A¯(γ,e). Then A¯ and f/|Γ| satisfy the hypotheses of Lemma 3, so

g(γ)g(γ′)A¯(γ,γ′),

g ∗ g∗(γ)f(γ) = |Γ|

![image 15](<2013-decorte-fourier-analysis-finite-groups_images/imageFile15.png>)

γ∈Γ

γ,γ′∈Γ

and since A¯ is positive semideﬁnite, it follows that the function f is of positive type. It is easily checked that the other constraints of (B) are satisﬁed by f, and moreover that the objective values are equal:

A¯(γ,e) =

f(γ) = |Γ|

γ∈Γ

γ∈Γ

A¯(γ,γ′) =

A(γ,γ′).

γ,γ′∈Γ

γ,γ′∈Γ

For the other direction, we begin with a feasible solution f : Γ → R to (B), and we deﬁne A: Γ × Γ → R by A(β,γ) = |Γ1|f(βγ−1). Then A is a feasible solution to

![image 16](<2013-decorte-fourier-analysis-finite-groups_images/imageFile16.png>)

- (A) by Lemma 3, and its objective value is γ∈Γ f(γ).


Using Theorem 1, we can also give a (complex) semideﬁnite programming formulation of (B) using block matrices.

- Theorem 4. Suppose G = Cay(Γ,X). Then

ϑ(G) = max A1 : Aπ ∈ Sd

π

(C) 0 for each π ∈ Γˆ,

π∈Γˆ

dπ Tr(Aπ) = |Γ|,

π∈Γˆ

dπ Aπ,π(x) = 0 for x ∈ X ,

where 1 ∈ Γˆ denotes the trivial representation.

Proof. If f : Γ → R is any feasible solution to (B), set Aπ = fˆ(π) for each π ∈ Γ.ˆ By Theorem 1, the matrices Aπ are positive semideﬁnite. Moreover, one easily checks using the Fourier inversion formula that the other constraints of (C) are satisﬁed

by {Aπ : π ∈ Γˆ}, and that the objective values are equal: A1 = γ∈Γ f(γ).

For the other direction, let {Aπ : π ∈ Γˆ} be a feasible solution for (C) and deﬁne g: Γ → C by

g(γ) =

1 |Γ|

![image 17](<2013-decorte-fourier-analysis-finite-groups_images/imageFile17.png>)

π∈Γˆ

dπ Aπ,π(γ) for all γ ∈ Γ.

Then g is of positive type by Theorem 1. Now deﬁne f(γ) = 21(g(γ) + g(γ−1)) for all γ ∈ Γ. Then f is real-valued, and that f satisﬁes all the other constraints of

![image 18](<2013-decorte-fourier-analysis-finite-groups_images/imageFile18.png>)

(B) is easily checked using the fact that X is inverse-closed. Moreover

γ∈Γ

f(γ) =

1 |Γ| γ∈Γ

![image 19](<2013-decorte-fourier-analysis-finite-groups_images/imageFile19.png>)

π∈Γˆ

dπ Aπ,π(γ) = A1

by the Schur orthogonality relations.

When Γ is an Abelian group, then all its irreducible representation are onedimensional. Therefore, the semideﬁnite program (C) is just a linear program. More generally, (C) is equivalent to a linear program whenever the connection set of the Cayley graph Cay(Γ,X) is closed under conjugation; that is, γxγ−1 ∈ X for all x ∈ X and γ ∈ Γ. This is the content of the next theorem.

- Theorem 5. Let G be the Cayley graph Cay(Γ,X) and suppose that the connection set X is closed under conjugation. Then


- (D) ϑ(G) = max a1 : aπ ≥ 0 for each π ∈ Γˆ,


d2πaπ = |Γ|,

π∈Γˆ

dπaπχπ(x) = 0 for x ∈ X .

π∈Γˆ

Proof. We prove the equivalence of (C) and (D). Let {Aπ : π ∈ Γˆ} be a feasible solution for (C), and for each π let

1 |Γ| γ∈Γ

A¯π =

π(γ)Aππ(γ)∗.

![image 20](<2013-decorte-fourier-analysis-finite-groups_images/imageFile20.png>)

Then {A¯π : π ∈ Γˆ} is again a solution to (C): If x ∈ X, then

1 |Γ|

dπ A ¯π,π(x) =

![image 21](<2013-decorte-fourier-analysis-finite-groups_images/imageFile21.png>)

π∈Γˆ

π∈Γˆ

1 |Γ|

=

![image 22](<2013-decorte-fourier-analysis-finite-groups_images/imageFile22.png>)

π∈Γˆ

π(γ)Aππ(γ)∗,π(x)

dπ

γ∈Γ

dπ

π(γ)Aπ,π(xγ) .

γ∈Γ

Since X is closed under conjugation there is a y ∈ X so that xγ = γy holds. Hence, the sum above equals

1 |Γ|

1 |Γ|

dπ

π(γ)Aπ,π(γy) =

![image 23](<2013-decorte-fourier-analysis-finite-groups_images/imageFile23.png>)

![image 24](<2013-decorte-fourier-analysis-finite-groups_images/imageFile24.png>)

π∈Γˆ

π∈Γˆ

γ∈Γ

dπ

Aπ,π(y) =

γ∈Γ

dπ Aπ,π(y) = 0.

π∈Γˆ

Moreover, since π(γ)Aππ(γ)∗ is similar to Aπ for each γ ∈ Γ, the matrix A¯π is positive semideﬁnite for each π ∈ Γˆ and π∈Γˆ dπ Tr(A¯π) = |Γ|.

We have constructed A¯π so that A¯ππ(γ) = π(γ)A¯π for all γ ∈ Γ. Schur’s lemma then implies that A¯π is equal to aπId

for some scalar aπ and since A¯π is positive semideﬁnite this scalar is nonnegative. We have dπaπ = Tr(A¯π) as well as

π

A ¯π,π(γ) = aπχπ(γ) for all γ ∈ Γ,

so {aπ : π ∈ Γˆ} is a feasible solution to (D) having objective value a1 = A1.

For the other direction, we take a feasible solution {aπ : π ∈ Γˆ} to (D), and for each π ∈ Γ,ˆ we set Aπ = aπId

. This is a feasible solution to (C) with objective value A1 = a1.

π

Denote the constraint π∈Γˆ dπaπχπ(x) = 0 by Cx (x ∈ X). For computational purposes, the following simpliﬁcations can be applied to (D): First, only one of the constraints {Cx,Cx−1} is needed. Second, since the characters χπ are constant on conjugacy classes, it suﬃces to keep only the constraints Cx, with one x per conjugacy class.

4. First application: k-intersecting permutations

In this section we apply Theorem 5 to the problem of k-intersecting permutations as discussed in the introduction.

Let Sn be the symmetric group on n letters. A family A ⊆ Sn is said to be k-intersecting if any two permutations in A agree on at least k elements. That is, a k-intersecting family of Sn is an independent set in the graph Cay(Sn,Xn,k), where

Xn,k = {σ ∈ Sn : σ has strictly less than k ﬁxed points}.

The set Xn,k is closed under conjugation so Theorem 5 applies. One can interpret the method of Ellis, Friedgut, and Pilpel in [4] as constructing an explicit family of feasible solutions to the linear programs which turns out to be optimal for given k and n suﬃciently large.

Conjecture 2 of [4] implies that a largest k-intersecting family in Sn has size max

{σ ∈ Sn: σ has at least k + i ﬁxed points in {1,...,k + 2i}} ,

0≤i≤(n−k)/2

which in particular means that the maximum size is (n − k)! for n ≥ 2k + 1. We solved the linear program (D) for small values of n and k with the help of a computer. In Table 1 the (n,k)-th entry is marked when the ϑ-number gives the conjectured maximum. To evaluate the characters of the symmetric group we used gap [7] and to solve the linear programs we used lrs [1]. Since both software packages only use rational arithmetic our computations are rigorous.

![image 25](<2013-decorte-fourier-analysis-finite-groups_images/imageFile25.png>)

n

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

k

![image 26](<2013-decorte-fourier-analysis-finite-groups_images/imageFile26.png>)

- 1

![image 27](<2013-decorte-fourier-analysis-finite-groups_images/imageFile27.png>)

- 2

![image 28](<2013-decorte-fourier-analysis-finite-groups_images/imageFile28.png>)

- 3

![image 29](<2013-decorte-fourier-analysis-finite-groups_images/imageFile29.png>)

- 4

![image 30](<2013-decorte-fourier-analysis-finite-groups_images/imageFile30.png>)

- 5

![image 31](<2013-decorte-fourier-analysis-finite-groups_images/imageFile31.png>)

- 6

![image 32](<2013-decorte-fourier-analysis-finite-groups_images/imageFile32.png>)

- 7

![image 33](<2013-decorte-fourier-analysis-finite-groups_images/imageFile33.png>)

- 8

![image 34](<2013-decorte-fourier-analysis-finite-groups_images/imageFile34.png>)

- 9

![image 35](<2013-decorte-fourier-analysis-finite-groups_images/imageFile35.png>)

- 10

![image 36](<2013-decorte-fourier-analysis-finite-groups_images/imageFile36.png>)

- 11

![image 37](<2013-decorte-fourier-analysis-finite-groups_images/imageFile37.png>)

- 12

![image 38](<2013-decorte-fourier-analysis-finite-groups_images/imageFile38.png>)

- 13

![image 39](<2013-decorte-fourier-analysis-finite-groups_images/imageFile39.png>)

- 14

![image 40](<2013-decorte-fourier-analysis-finite-groups_images/imageFile40.png>)

- 15 Table 1. Computation of ϑ(Cay(Sn, Xn,k))


![image 41](<2013-decorte-fourier-analysis-finite-groups_images/imageFile41.png>)

5. Second application: k-intersecting invertible matrices

Here we consider a q-analog of the previous application. Let Γ = GL(n,Fq) be the group of invertible n × n-matrices over the ﬁnite ﬁeld with q elements, where q is a prime power. We say that two matrices A and B in GL(n,Fq) k-intersect if there is a k-dimensional subspace H of Fnq such that Ax = Bx for all x ∈ H. Given a natural number k, let

Xq,n,k = {A ∈ GL(n,Fq) : rank(A − I) > n − k}

and consider the Cayley graph Gq,n,k = Cay(Γ,Xq,n,k). Independent sets in this graph correspond to k-intersecting families of invertible matrices.

The independence number of Gq,n,1 was recently calculated by Guo and Wang in [8] (not by computing ϑ(Gq,n,1)).

For any q and n, one clearly obtains a lower bound by choosing a nonzero vector x ∈ Fnq and considering the set A of all matrices A ∈ GL(n,Fq) such that Ax = x. One has |A| = i n=1−1(qn − qi) by the orbit-stabilizer theorem, and for small values of n and q we found numerically that ϑ(Gq,n,1) equals this lower bound. Since Xq,n,k is closed under conjugation, ϑ(Gq,n,k) can be computed by solving the linear program (D).

- Conjecture 1. One has ϑ(Gq,n,1) = α(Gq,n,1) = i n=1−1(qn − qi) for all values of n and q.

For k > 1, we can construct independent sets in a similar way as above: Choose linearly independent vectors x1,...,xk ∈ Fnq and let A be the set of all matrices A ∈ GL(n,Fq) such that Axi = xi for 1 ≤ i ≤ k. Then |A| = i n=−k1(qn − qi). By computing the ϑ-number for small values of n and q (see Table 2) we have evidence that a version of the Erdo˝s-Ko-Rado theorem might also be true in this setting.

- Conjecture 2. We conjecture that for each q,k ∈ N, there exists n0 = n0(q,k) ∈ N such that ϑ(Gq,n,k) = α(Gq,n,k) = i n=−k1(qn − qi) for all n ≥ n0.


The computations in Table 2 have been performed with magma [3] and lpsolve [2]. As the computation of the characters of GL(n,Fq) involve irrational numbers we

cannot solve the linear programs with rational arithmetic only. So these computations cannot be considered as rigorous mathematical proofs. Nevertheless we are certain that we placed checkmarks where the exact computation of ϑ(Gq,n,k) would give an upper bound which is equal to the corresponding lower bound.

![image 42](<2013-decorte-fourier-analysis-finite-groups_images/imageFile42.png>)

q = 2 q = 3 q = 4

![image 43](<2013-decorte-fourier-analysis-finite-groups_images/imageFile43.png>)

![image 44](<2013-decorte-fourier-analysis-finite-groups_images/imageFile44.png>)

![image 45](<2013-decorte-fourier-analysis-finite-groups_images/imageFile45.png>)

n

1 2 3 4 5 6 1 2 3 4 1 2 3

k

![image 46](<2013-decorte-fourier-analysis-finite-groups_images/imageFile46.png>)

- 1

![image 47](<2013-decorte-fourier-analysis-finite-groups_images/imageFile47.png>)

- 2

![image 48](<2013-decorte-fourier-analysis-finite-groups_images/imageFile48.png>)

- 3

![image 49](<2013-decorte-fourier-analysis-finite-groups_images/imageFile49.png>)

- 4

![image 50](<2013-decorte-fourier-analysis-finite-groups_images/imageFile50.png>)

- 5

![image 51](<2013-decorte-fourier-analysis-finite-groups_images/imageFile51.png>)

- 6


![image 52](<2013-decorte-fourier-analysis-finite-groups_images/imageFile52.png>)

Table 2. Computation of ϑ(Cay(Γ, Xq,n,k))

6. Blowing up vertex transitive graphs

The ﬁnal theorem in this note shows that for the purposes of estimating the independence number of a graph, the theory presented in the preceding sections can be applied not just to Cayley graphs, but also to vertex-transitive graphs.

- Theorem 6. Let G = (V,E) be a graph and let Γ be a group of automorphisms of G. Suppose Γ acts transitively on V . Then there exists a connection set X ⊆ Γ such that


α(G) = ||VΓ||α(Cay(Γ,X)). Proof. Pick a vertex x0 ∈ V and deﬁne

![image 53](<2013-decorte-fourier-analysis-finite-groups_images/imageFile53.png>)

X = {γ ∈ Γ : {x0,γ · x0} ∈ E}. Then for β,γ ∈ Γ, one has an edge {β,γ} in the Cayley graph Cay(Γ,X) if and only if

γ−1β ∈ X ⇐⇒ {x0,γ−1β · x0} ∈ E ⇐⇒ {γ · x0,β · x0} ∈ E. Now notice that by the orbit-stabilizer theorem, one has

|Γ| |V |

|{γ ∈ Γ : γ · x = x}| =

for all x ∈ V , and the theorem follows immediately.

![image 54](<2013-decorte-fourier-analysis-finite-groups_images/imageFile54.png>)

Going from G to the Cayley graph Cay(Γ,X) is accomplished using the following procedure: First choose a vertex x0 ∈ V arbitrarily, and let H be the stabilizer subgroup of x0 in Γ. Each vertex x ∈ V is then replaced with an empty graph on the left coset of H in Γ consisting of all those γ ∈ Γ such that γ · x0 = x. In other words, the vertex set V is regarded as a Γ-homogeneous space, and each vertex is “blown up” to an independent set of size |Γ|/|V | by replacing it with its inverse image under the projection map.

References

- [1] D. Avis, A C-implementation of the reverse search vertex enumeration algorithm, School of Computer Science, McGill University, Montreal, Canada 1993. (http://www-cgrl.cs.mcgill.ca/~avis/C/lrs.html)
- [2] M. Berkelaar, K. Eikland, P. Notebaert, lpsolve version 5.5, available from the web site http://lpsolve.sourceforge.net/


- [3] W. Bosma, J. Cannon, C. Playoust, The Magma algebra system. I. The user language, J. Symbolic Comput., 24 (1997), 235–265.
- [4] D. Ellis, E. Friedgut, H. Pilpel, Intersecting families of permutations, J. Amer. Math. Soc. 24 (2011), 649–682. (http://arxiv.org/abs/1011.3342)
- [5] G.B. Folland, A Course in Abstract Harmonic Analysis, CRC Press Inc., 1995.
- [6] P. Frankl, M. Deza, On the maximum number of permutations with given maximal or minimal distance, J. Comb. Theory Ser. A 22 (1977), 352–360.
- [7] The GAP Group, GAP — Groups, Algorithms, and Programming, Version 4.6.4; 2013. (http://www.gap-system.org)
- [8] J. Guo, K. Wang, An Erdo˝s-Ko-Rado theorem in general linear groups, arXiv:1107.3178 [math.CO] (http://arxiv.org/abs/1107.3178)
- [9] L. Lova´sz, On the Shannon capacity of a graph, IEEE Trans. Inf. Th. 25 (1979), 1–7.
- [10] A. Terras, Fourier Analysis on Finite Groups and Applications, Cambridge University Press, 1999.


P.E.B. DeCorte, Delft Institute of Applied Mathematics, Delft University of Tech-

nology, P.O. Box 5031, 2600 GA Delft, The Netherlands E-mail address: p.e.b.decorte@tudelft.nl D. de Laat, Delft Institute of Applied Mathematics, Delft University of Technol-

ogy, P.O. Box 5031, 2600 GA Delft, The Netherlands E-mail address: mail@daviddelaat.nl F. Vallentin, Mathematisches Institut, Universitat¨ zu Koln,¨ Weyertal 86–90, 50931

Koln,¨ Germany E-mail address: frank.vallentin@uni-koeln.de

