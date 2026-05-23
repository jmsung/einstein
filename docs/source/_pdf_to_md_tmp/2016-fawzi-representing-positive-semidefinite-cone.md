arXiv:1610.04901v1[math.OC]16Oct2016

On representing the positive semideﬁnite cone using the second-order cone

Hamza Fawzi∗ October 18, 2016

Abstract

The second-order cone plays an important role in convex optimization and has strong expressive abilities despite its apparent simplicity. Second-order cone formulations can also be solved more eﬃciently than semideﬁnite programming in general. We consider the following question, posed by Lewis and Glineur, Parrilo, Saunderson: is it possible to express the general positive semideﬁnite cone using second-order cones? We provide a negative answer to this question and show that the 3 × 3 positive semideﬁnite cone does not admit any second-order cone representation. Our proof relies on exhibiting a sequence of submatrices of the slack matrix of the 3 × 3 positive semideﬁnite cone whose “second-order cone rank” grows to inﬁnity. We also discuss the possibility of representing certain slices of the 3 × 3 positive semideﬁnite cone using the second-order cone.

# 1 Introduction

Let Q ⊂ R3 denote the three-dimensional second-order cone (also known as the “ice-cream” cone or the Lorentz cone):

Q = {(x,t) ∈ R2 × R : x ≤ t}.

It is known that Q is linearly isomorphic to the cone of 2 × 2 real symmetric positive semideﬁnite matrices. Indeed we have:

(x1,x2,t) ∈ Q ⇐⇒

t − x1 x2 x2 t + x1

0. (1)

Despite its apparent simplicity the second-order cone Q has strong expressive abilities and allows us to represent various convex constraints that go beyond “simple quadratic constraints”. For example it can be used to express geometric means (x  → ni=1 xpii where pi ≥ 0 and ni=1 pi = 1), ℓp-norm constraints, multifocal ellipses, robust counterparts of linear programming, etc. We refer the reader to [BTN01a] for more details.

Given this strong expressive ability one may wonder whether the general positive semideﬁnite cone can be represented using Q. This question was posed in particular by Adrian Lewis (personal communication) and Glineur, Parrilo and Saunderson [GPS13]. In this paper we show that this is not possible, even for the 3 × 3 positive semideﬁnite cone. To make things precise we use the language of lifts (or extended formulations), see [GPT13]. We say that a convex cone K ⊂ Rm

![image 1](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile1.png>)

∗Department of Applied Mathematics and Theoretical Physics, University of Cambridge. Email: h.fawzi@damtp.cam.ac.uk.

has a second-order cone lift of size k (or simply Qk-lift) if it can be written as the projection of an aﬃne slice of the Cartesian product of k copies of Q, i.e.:

K = π Qk ∩ L (2)

where π : R3k → Rm is a linear map and L is a linear subspace of R3k, and Qk is the Cartesian product of k copies of Q:

Qk = Q × ··· × Q (k copies). In this paper we prove:

- Theorem 1. The cone S3+ does not admit any Qk-lift for any ﬁnite k. Note that higher-dimensional second order cones of the form


{(x,t) ∈ Rn × t : x ≤ t}

where n ≥ 3 can be represented using the three-dimensional cone Q, see e.g., [BTN01b, Section 2]. Thus Theorem 1 also rules out any representation of S3+ using the higher-dimensional second-order cones. Moreover since S3+ appears as a slice of higher-order positive semideﬁnite cones Theorem 1 also shows that one cannot represent Sn+, for n ≥ 3 using second-order cones.

# 2 Preliminaries

The paper [GPT13] introduced a general methodology to prove existence or nonexistence of lifts in terms of the slack matrix of a cone. In this section we review some of the deﬁnitions and results from this paper, and we introduce the notion of second-order cone factorization and second-order cone rank.

Recall that the dual of a cone K living in Euclidean space E is deﬁned as: K∗ = {x ∈ E : x,y ≥ 0 ∀y ∈ K}.

We also denote by ext(K) the extreme rays of a cone K. The notion of slack matrix plays a fundamental role in the study of lifts.

- Deﬁnition 1 (Slack matrix). The slack matrix of a cone K, denoted SK, is a (potentially inﬁnite) matrix where columns are indexed by extreme rays of K, and rows are indexed by extreme rays of K∗ (the dual of K) and where the (x,y) entry is given by:

SK[x,y] = x,y ∀(x,y) ∈ ext(K∗) × ext(K). (3)

Note that, by deﬁnition of dual cone, all the entries of SK are nonnegative. Also note that an element x ∈ ext(K∗) (and similarly y ∈ ext(K)) is only deﬁned up to a positive multiple. Any choice of scaling gives a valid slack matrix of K and the properties of SK that we are interested in will be independent of the scaling chosen.

The existence/nonexistence of a second-order cone lift for a convex cone K will depend on whether SK admits a certain second-order cone factorization which we now deﬁne.

- Deﬁnition 2 (Qk-factorization and second-order cone rank). Let S ∈ RI×J be a matrix with nonnegative entries. We say that S has a Qk-factorization if there exist vectors ai ∈ Qk for i ∈ I and bj ∈ Qk for j ∈ J such that S[i,j] = ai,bj for all i ∈ I and j ∈ J. The smallest k for which such a factorization exists will be denoted ranksoc(S).


- Remark 1. It is important to note that the second-order cone rank of any matrix S can be equivalently expressed as the smallest k such that S admits a decomposition


S = M1 + ··· + Mk (4)

where ranksoc(Ml) = 1 for each l = 1,... ,k (i.e., each Ml has a factorization Ml[i,j] = ai,bj where ai,bj ∈ Q). This simply follows from the fact that Qk is the Cartesian product of k copies of Q.

We now state the main theorem from [GPT13] that we will need. Recall that a cone K is called proper if it is closed, convex, full-dimensional and such that K∗ is also full-dimensional.

- Theorem 2 (Existence of a lift, special case of [GPT13]). A proper cone K has a Qk-lift if and only if its slack matrix SK has a Qk-factorization.

The cone S3+ In this paper we are interested in the cone K = S3+ of real symmetric 3×3 positive semideﬁnite matrices. Note that the extreme rays of S3+ are rank-one matrices of the form xxT where x ∈ R3. Also note that S3+ is self-dual, i.e., (S3+)∗ = S3+. The slack matrix of S3+ thus has its rows and columns indexed by three-dimensional vectors and

SS3

+

[x,y] = xxT,yyT = xTy 2 ∀(x,y) ∈ R3 × R3. (5)

In order to prove that S3+ does not admit a second-order representation, we will show that its slack matrix does not admit any Qk-factorization for any ﬁnite k. In fact we will exhibit a sequence (An) of submatrices of SS3

+

where ranksoc(An) grows to +∞ as n → +∞.

Before introducing this sequence of matrices we record the following simple fact concerning orthogonal vectors in the cone Q which will be useful later.

- Fact 1. Assume a,b1,b2 ∈ Q are all nonzero and a,b1 = a,b2 = 0. Then necessarily b1 and b2 are collinear.


Proof. This is easy to see geometrically by visualizing the “ice cream” cone. We include a proof for completeness: let a = (a′,t) ∈ R2 × R and bi = (b′i,si) ∈ R2 × R where a′ ≤ t and b′i ≤ si. Note that for i = 1,2 we have 0 = a,bi = a′,b′i + tsi ≥ − a′ b′i + tsi ≥ 0 where in the ﬁrst inequality we used Cauchy-Schwarz and in the second inequality we used the deﬁnition of the second-order cone. It thus follows that all the inequalities must be equalities: by the equality case in Cauchy-Schwarz we must have that b′i = αia′ for some constant αi and we must also have t = a′ and si = b′i (note that αi < 0). Thus we get that bi = (αia′,|αi| a′ ) = |αi|(−a′, a′ ). This shows that b1 and b2 are both collinear to the same vector (−a′, a′ ) and thus completes the proof.

![image 2](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile2.png>)

![image 3](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile3.png>)

![image 4](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile4.png>)

![image 5](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile5.png>)

- 3 Proof


A sequence of matrices We now deﬁne our sequence An of submatrices of the slack matrix of S3+. For any integer i deﬁne the vector

vi = (1,i,i2) ∈ R3. (6) Note that this sequence of vectors satisﬁes the following:

For all distinct integers i1,i2,i3 det(vi1,vi2,vi3) = 0. (7)

Our matrix An has size n2 × n and is deﬁned as follows (rows are indexed by 2-subsets of [n] and columns are indexed by [n]):

An[{i1,i2},j] := (vi1 × vi2)Tvj 2 = det(vi1,vi2,vj)2 ∀{i1,i2} ∈

[n] 2

, ∀j ∈ [n] (8)

where × denotes the cross-product of three-dimensional vectors. It is clear from the deﬁnition of An that it is a submatrix of the slack matrix of S3+. Note that the sparsity pattern of An satisﬁes the following:

An[e,j] = 0 if j ∈ e An[e,j] > 0 otherwise

[n] 2

e ∈

, j ∈ [n]. (9)

Also note that An satisﬁes the following important recursive property: for any subset C of [n] of size n0 the submatrix An[ C2 ,C] has the same sparsity pattern as An0. In our main theorem we will show that the second-order cone rank of An grows to inﬁnity with n.

- Remark 2. The speciﬁc choice of vi in (6) is not important, as long as it satisﬁes (7), since the only property that we will use about An is its sparsity pattern. For example another choice for vi that we could use is


vi = (1,cos(θi),sin(θi)) ∈ R3 (10) where θ1,θ2,... is any increasing sequence in [0,2π). In fact using this choice of vi we will argue later (Section 4) that a certain slice of S3+ does not admit a second-order cone lift.

Covering numbers Our analysis of the matrix An will only rely on its sparsity pattern. Given two matrices A and B of the same size we write A supp= B if A and B have the same support (i.e., Aij = 0 if and only if Bij = 0 for all i,j). We now deﬁne a combinatorial analogue of the second-order cone rank:

- Deﬁnition 3. Given a nonnegative matrix A, we deﬁne the soc-covering number of A, denoted


covsoc(A) to be the smallest number k of matrices M1,... ,Mk with ranksoc(Ml) = 1 for l = 1,... ,k that are needed to cover the nonzero entries of A, i.e., such that

A supp= M1 + ··· + Mk. (11)

- Fact 2. For any nonnegative matrix A ∈ RI+×J we have ranksoc(A) ≥ covsoc(A). Proof. This follows immediately from Remark 1 concerning ranksoc and the deﬁnition of covsoc.


![image 6](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile6.png>)

![image 7](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile7.png>)

![image 8](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile8.png>)

![image 9](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile9.png>)

A simple but crucial fact concerning soc-coverings that we will use is the following: in any soc-covering of A of the form (11), each matrix Ml must satisfy Ml[i,j] = 0 whenever A[i,j] = 0. This is because the matrices M1,... ,Mk are all entrywise nonnegative.

We are now ready to state our main result.

- Theorem 3. Consider a sequence (An) of matrices of sparsity pattern given in (9). Then for


any n0 ≥ 2 we have covsoc(A3n2

) ≥ covsoc(An0) + 1. As a consequence covsoc(An) → +∞ when n → +∞.

0

The proof of our theorem rests on a key lemma concerning the sparsity pattern of any term in a soc-covering of An.

- Lemma 1 (Main). Let n such that n ≥ 3n20 for some n0 ≥ 2. Assume M ∈ R(n2)×n satisﬁes ranksoc(M) = 1 and M[e,j] = 0 for all e ∈ n2 and j ∈ [n] such that j ∈ e. Then there is a subset C of [n] of size at least n0 such that the submatrix M[ C2 ,C] is identically zero.


Before proving this lemma, we show how this lemma can be used to easily prove Theorem 3.

Proof of Theorem 3. Let n = 3n20 and consider a soc-covering of An supp= M1 + ··· + Mr of size r = covsoc(An) (note that we have of course r ≥ 1 since An is not identically zero). By Lemma 1 there is a subset C of [n] of size n0 such that M1[ C2 ,C] = 0. It thus follows that we have An[ C2 ,C] supp= M2[ C2 ,C] + ··· + Mr[ C2 ,C]. Also note that An[ C2 ,C] supp= An0. It thus follows that An0 has a soc-covering of size r − 1 and thus covsoc(An0) ≤ covsoc(A3n2

) − 1. This completes the proof.

0

![image 10](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile10.png>)

![image 11](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile11.png>)

![image 12](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile12.png>)

![image 13](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile13.png>)

For completeness we show how Theorem 1 follows directly from Theorem 3. Proof of Theorem 1. Since for any n ≥ 1, An is a submatrix of the slack matrix of S3+, Theorem

- 3 shows that the slack matrix of S3+ does not admit any Qk-factorization for ﬁnite k. This shows, via Theorem 2, that S3+ does not have a Qk-lift for any ﬁnite k.


![image 14](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile14.png>)

![image 15](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile15.png>)

![image 16](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile16.png>)

![image 17](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile17.png>)

The rest of the paper is devoted to prove Lemma 1.

Proof of Lemma 1. Let M ∈ R(n2)×n and assume that M has a factorization Me,j = ae,bj where ae,bj ∈ Q for all e ∈ [n2] and j ∈ [n], and that Me,j = 0 whenever j ∈ e.

Let E0 := {e ∈ [n2] : ae = 0} be the set of rows of M that are identically zero and let E1 = [n2] \ E0. Similarly for the columns we let S0 := {j ∈ [n] : bj = 0} and S1 = [n] \ S0.

In the next lemma we use the sparsity pattern of An together with Fact 1 to infer additional properties on the sparsity pattern of M.

- Lemma 2. Let C be a connected component of the graph with vertex set S1 and edge set E1(S1) (where E1(S1) consists of elements in E1 that connect only elements of S1). Then necessarily M[ C2 ,C] = 0.


Proof. We ﬁrst show using Fact 1 that all the vectors {bj}j∈C are necessarily collinear. Let j1,j2 ∈ S1 such that e = {j1,j2} ∈ E1. Note that since Me,j1 = Me,j2 = 0 then we have, by Fact 1 that bj1 and bj2 are collinear. It is easy to see thus now that if j1 and j2 are connected by a path in the graph (S1,E1(S1)) then bj1 and bj2 must be collinear.

We thus get that all the columns of M indexed by C must be proportional to each other, and so they must have the same sparsity pattern. Now let e ∈ C2 . If ae = 0 then M[e,C] = 0 since the entire row e is zero. Otherwise if ae = 0 let e = {j1,j2} with j1,j2 ∈ C. Since Me,j1 = 0 it follows that for any j ∈ C we must have Me,j = 0, i.e., M[e,C] = 0. This is true for any e ∈ C2 thus we get that M[ C2 ,C] = 0.

![image 18](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile18.png>)

![image 19](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile19.png>)

![image 20](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile20.png>)

![image 21](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile21.png>)

To complete the proof of Lemma 1 assume that n ≥ 3n20 for some n0 ≥ 2. We need to show that there is a subset C of [n] of size at least n0 such that M[ C2 ,C] = 0.

First note that if the graph (S1,E1(S1)) has a connected component of size at least n0 then we are done by Lemma 2. Also note that if S0 has size at least n0 we are also done because all the columns indexed by S0 are identically zero by deﬁnition.

In the rest of the proof we will thus assume that |S0| < n0 and that the connected components of (S1,E1(S1)) all have size < n0. We will show in this case that E0 necessarily contains a clique of size at least n0 (i.e., a subset of the form C2 where |C| ≥ n0) and this will prove our claim since all the rows in E0 are identically zero by deﬁnition. The intuition is as follows: the assumption that |S0| < n0 and that the connected components of (S1,E1(S1)) have size < n0 mean that the graph (S1,E1(S1)) is very sparse. In particular this means that E1 has to be small which means that E0 = E1c must be large and thus it must contain a large clique.

More precisely, to show that E1 is small note that it consists of those edges that are either in E1(S1) or, otherwise, they must have at least one node in S1c = S0. Thus we get that

|E1| ≤ |E1(S1)| + |S0|(n − 1) ≤ |E1(S1)| + (n0 − 1)(n − 1).

where in the second inequality we used the fact that |S0| < n0. Also since the connected components of (S1,E1(S1)) all have size < n0 it is not diﬃcult to show that |E1(S1)| < n0n/2 (indeed if we let x1,... ,xk be the size of each connected component we have |E1(S1)| ≤ 12 ki=1 x2i < 12 ki=1 n0xi ≤

![image 22](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile22.png>)

![image 23](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile23.png>)

- 1

![image 24](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile24.png>)

- 2n0n). Thus we get that


n0n 2

|E1| ≤

+ (n0 − 1)(n − 1) ≤

![image 25](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile25.png>)

3 2

n0 − 1 n

![image 26](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile26.png>)

Thus this means, since E0 = n2 \ E1:

|E0| ≥

n 2

−

n2 2

3 2

n0 − 1 n >

![image 27](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile27.png>)

![image 28](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile28.png>)

3 2

−

n0n

![image 29](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile29.png>)

We now invoke a result of Tura´n to show that E0 must contain a clique of size at least n0:

- Theorem 4 (Tura´n, see e.g., [Aig95]). Any graph on n vertices with more than 1 − k1 n22 edges contains a clique of size k + 1.


![image 30](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile30.png>)

![image 31](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile31.png>)

By taking k = n0 − 1 we see that E0 contains a clique of size n0 if

n2 2 This simpliﬁes into

n2 2

3 2

1 n0 − 1

−

n0n ≥ 1 −

![image 32](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile32.png>)

![image 33](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile33.png>)

![image 34](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile34.png>)

![image 35](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile35.png>)

n ≥ 3n0(n0 − 1) which is true for n ≥ 3n20.

![image 36](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile36.png>)

![image 37](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile37.png>)

![image 38](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile38.png>)

![image 39](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile39.png>)

# 4 Slices of the 3 × 3 positive semideﬁnite cone

Certain slices of S3+ are known to admit a second-order cone representation. For example the following second-order cone representation of the slice {X ∈ S3+ : X11 = X22} appears in [GPS13]:

 

  0 ⇐⇒ ∃u,v ∈ R s.t.

t a b

t + a b + c b + c u

t − a b − c b − c v

- a t c
- b c s


0,

0, u + v = 2s.

(12) (The 2 × 2 positive semideﬁnite constraints can be converted to second-order cone constraints using (1)). To see why (12) holds note that by applying a congruence transformation by √12 11 −11 00

![image 40](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile40.png>)

![image 41](<2016-fawzi-representing-positive-semidefinite-cone_images/imageFile41.png>)

0 0 2

on the 3 × 3 matrix on the left-hand side of (12) we get that

 

 

  0 ⇐⇒

  0.

t a b

t + a 0 b + c

- a t c
- b c s


0 t − a b − c b + c b − c 2s

The latter matrix has an arrow structure and thus using results on the decomposition of matrices with chordal sparsity pattern [GT84, GJSW84, AHMR88] we get the decomposition (12).

On the other hand, the proof presented in the previous section can be used to show that certain other slices do not admit second-order cone representations. Consider the following slice which we denote by C:

C = {X ∈ S3+ : X11 = X22 + X33}. We will argue that there is no second-order cone representable set that is contained between C and S3+ (in particular C does not have a second-order cone lift). To do so we ﬁrst need to introduce the notion of generalized slack matrix for a pair of convex cones K1 ⊆ K2: such matrix has its rows indexed by ext(K2∗) (the valid linear inequalities of K2) and its columns indexed by ext(K1) and is deﬁned by

SK1,K2[x,y] = x,y x ∈ ext(K2∗),y ∈ ext(K1).

One can show that SK1,K2 has a second-order cone factorization if and only if there exists a secondorder cone representable set between K1 and K2 (this can be proved using exactly the same arguments as in, e.g., Theorem 4 of [FGP+15]).

We now claim that matrices An of the form given by (9) appear as submatrices of the generalized slack matrix of C and S3+. Indeed note that the vectors vi = (1,cos(θi),sin(θi)) given in (10) satisfy viviT ∈ C. Furthermore for any i,j it is clear that (vi × vj)(vi × vj)T,X ≥ 0 is a valid inequality for S3+. It thus follows that the matrix

An[{i1,i2},j] = (vi1 × vi2)(vi1 × vi2)T,vjvjT = (vi1 × vi2),vj 2

is a submatrix of the generalized slack matrix of C and S3+. The arguments from the previous section show that ranksoc(An) goes to +∞ with n. Thus this shows that there cannot be any second-order cone representable set that lies between C and S3+.

# Acknowledgments

I would like to thank Franc¸ois Glineur, Pablo Parrilo and James Saunderson for comments on a draft of this manuscript that helped improve the exposition.

# References

[AHMR88] Jim Agler, William Helton, Scott McCullough, and Leiba Rodman. Positive semideﬁnite matrices with a given sparsity pattern. Linear algebra and its applications, 107:101– 149, 1988.

[Aig95] Martin Aigner. Tura´n’s graph theorem. The American Mathematical Monthly, 102(9):808–816, 1995.

- [BTN01a] Aharon Ben-Tal and Arkadi Nemirovski. Lectures on modern convex optimization: analysis, algorithms, and engineering applications. SIAM, 2001.
- [BTN01b] Aharon Ben-Tal and Arkadi Nemirovski. On polyhedral approximations of the secondorder cone. Mathematics of Operations Research, 26(2):193–205, 2001.


[FGP+15] Hamza Fawzi, Joa˜o Gouveia, Pablo A. Parrilo, Richard Z. Robinson, and Rekha R. Thomas. Positive semideﬁnite rank. Mathematical Programming, 153(1):133–177, 2015.

[GJSW84] Robert Grone, Charles R. Johnson, Eduardo M. Sa´, and Henry Wolkowicz. Positive deﬁnite completions of partial Hermitian matrices. Linear algebra and its applications, 58:109–124, 1984.

- [GPS13] Franc¸ois Glineur, Pablo Parrilo, and James Saunderson. Second-order cone representations of positive semideﬁnite cones. Talk at the Fourth SDP days. Link to slides (retrieved online October 5, 2016), 2013.
- [GPT13] Joa˜o Gouveia, Pablo A. Parrilo, and Rekha R. Thomas. Lifts of convex sets and cone factorizations. Mathematics of Operations Research, 38(2):248–264, 2013.


[GT84] Andreas Griewank and Philippe L. Toint. On the existence of convex decompositions of partially separable functions. Mathematical Programming, 28(1):25–49, 1984.

