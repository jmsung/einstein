arXiv:1605.00988v3[math.OC]26Oct2016

MATRICES WITH HIGH COMPLETELY POSITIVE SEMIDEFINITE RANK

SANDER GRIBLING1,3, DAVID DE LAAT1,3, AND MONIQUE LAURENT1,2

Abstract. A real symmetric matrix M is completely positive semideﬁnite if it admits a Gram representation by (Hermitian) positive semideﬁnite matrices of any size d. The smallest such d is called the (complex) completely positive semideﬁnite rank of M, and it is an open question whether there exists an upper bound on this number as a function of the matrix size. We construct completely positive semideﬁnite matrices of size 4k2+2k+2 with complex completely positive semideﬁnite rank 2k for any positive integer k. This shows that if such an upper bound exists, it has to be at least exponential in the matrix size. For this we exploit connections to quantum information theory and we construct extremal bipartite correlation matrices of large rank. We also exhibit a class of completely positive matrices with quadratic (in terms of the matrix size) completely positive rank, but with linear completely positive semideﬁnite rank, and we make a connection to the existence of Hadamard matrices.

1. Introduction

A matrix is said to be completely positive semideﬁnite if it admits a Gram representation by (Hermitian) positive semideﬁnite matrices of any size. The n × n completely positive semideﬁnite matrices form a convex cone, called the completely positive semideﬁnite cone, which is denoted by CS+n.

The motivation for the study of the completely positive semideﬁnite cone is twofold. Firstly, the completely positive semideﬁnite cone CS+n is a natural analog of the completely positive cone CPn, which consists of the matrices admitting a factorization by nonnegative vectors. The cone CPn is well studied (see, for example, the monograph [1]), and, in particular, it can be used to model classical graph parameters. For instance, [17] shows how to model the stability number of a graph

- as a conic optimization problem over the completely positive cone. A second moti-


vation lies in the connection to quantum information theory. Indeed, the cone CS+n was introduced in [18] to model quantum graph parameters (including quantum stability numbers) as conic optimization problems, an approach extended in [24] for quantum graph homomorphisms and in [26] for quantum correlations.

In this paper we are interested in the size of the factors needed in Gram representations of matrices. This type of question is of interest for factorizations by nonnegative vectors as well as by (Hermitian) positive semideﬁnite matrices.

Throughout we use the following notation. For X,Y ∈ Cd×d, X∗ is the conjugate transpose and X,Y = Tr(X∗Y ) is the trace inner product. For vectors u,v ∈ Rd,

- u,v = uTv denotes their Euclidean inner product.


![image 1](<2016-gribling-matrices-high-completely-positive_images/imageFile1.png>)

1CWI, Amsterdam, The Netherlands

- 2Tilburg University, Tilburg, The Netherlands
- 3The work was supported by the Netherlands Organization for Scientiﬁc Research, grant num-


ber 617.001.351. Date: October 17, 2016. 1991 Mathematics Subject Classiﬁcation. 15B48, 15A23, 90C22. Key words and phrases. completely positive semideﬁnite cone, matrix factorization, quantum

correlations, Cliﬀord algebras, Hadamard matrices.

1

A matrix M is said to be completely positive if there exist nonnegative vectors

- v1,...,vn ∈ Rd+ such that Mi,j = vi,vj for all i,j ∈ [n]. We call such a set of vectors a Gram representation or factorization of M by nonnegative vectors. The smallest d for which these vectors exist is denoted by cp-rank(M) and is called the completely positive rank of M.


Similarly, a matrix M is called completely positive semideﬁnite if there exist (real symmetric or complex Hermitian) positive semideﬁnite d × d matrices X1,...,Xn such that Mi,j = Xi,Xj for all i,j ∈ [n]. We call such a set of matrices a Gram representation or factorization of M by (Hermitian) positive semideﬁnite matrices. The smallest d for which there exists a Gram representation of M by Hermitian positive semideﬁnite d×d matrices is denoted by cpsd-rankC(M), and the smallest d for which these matrices can be taken to be real is denoted by cpsd-rankR(M). We call this the real/complex completely positive semideﬁnite rank of M. If a matrix has a factorization by Hermitian positive semideﬁnite matrices, then it also has a factorization by real positive semideﬁnite matrices. In fact, for every M ∈ CS+n, we have

cpsd-rankC(M) ≤ cpsd-rankR(M) ≤ 2 cpsd-rankC(M) (see Section 2).

By construction, we have the inclusions CPn ⊆ CS+n ⊆ S+n ∩ Rn×n

+ ,

where S+n is the cone of (real) positive semideﬁnite n×n matrices. The three cones coincide for n ≤ 4 (since doubly nonnegative matrices of size n ≤ 4 are completely positive), but both inclusions are strict for n ≥ 5 (see [18] for details).

By Carath´eodory’s theorem, the completely positive rank of a matrix in CPn is

- at most n+12 + 1. In [25] the following stronger bound is given: n + 1


2 − 4 for M ∈ CPn and n ≥ 5,

- (1) cp-rank(M) ≤


which is also not known to be tight. No upper bound (as a function of n) is known for the completely positive semideﬁnite rank of matrices in CS+n. It is not even known whether such a bound exists. A positive answer would have strong implications. It would imply that the cone CS+n is closed. This, in turn, would imply that the set of quantum correlations is closed, since it can be seen as a projection of an aﬃne slice of the completely positive semideﬁnite cone (see [21, 26]). Whether the set of quantum correlations is closed is an open question in quantum information theory. In contrast, as an application of the upper bound (1), the completely positive cone CPn is easily seen to be closed. A description of the closure of the completely positive semideﬁnite cone in terms of factorizations by positive elements in von Neumann algebras can be found in [5]. Such factorizations were used to show a separation between the closure of CS+n and the doubly nonnegative cone S+n ∩ Rn×n

+ (see [12, 18]). In this paper we show that if an upper bound exists for the completely positive

semideﬁnite rank of matrices in CS+n, then it needs to grow at least exponentially in the matrix size n. Our main result is the following:

Theorem 1.1. For each positive integer k, there exists a completely positive semideﬁnite matrix M of size 4k2 + 2k + 2 with cpsd-rankC(M) = 2k.

The proof of this result relies on a connection with quantum information theory and geometric properties of (bipartite) correlation matrices. We refer to the main text for the deﬁnitions of quantum and bipartite correlations. A ﬁrst basic ingredient is the fact from [26] that a quantum correlation p can be realized in local

dimension d if and only if there exists a certain completely positive semideﬁnite matrix M with cpsd-rankC(M) at most d. Then, the key idea is to construct a class of quantum correlations p that need large local dimension.

The papers [30, 27, 15] each use diﬀerent techniques to show the existence of diﬀerent quantum correlations that require large local dimension. Our main contribution is to provide a uniﬁed, explicit construction of the quantum correlations from [30] and [27], which uses the seminal work of Tsirelson [28, 29] combined with convex geometry and recent insights from rigidity theory. In addition, we also give an explicit proof of Tsirelson’s bound (see Corollary 3.10) and we show examples where the bound is tight.

More speciﬁcally, we construct such quantum correlations from bipartite correlation matrices. For this we use the classical results of Tsirelson [28, 29], which characterize bipartite correlation matrices in terms of operator representations and, using Cliﬀord algebras, we relate the rank of extremal bipartite correlations to the local dimension of their operator representations. In this way we reduce the problem to ﬁnding bipartite correlation matrices that are extreme points of the set of bipartite correlations and have large rank.

For the completely positive rank we have the quadratic upper bound (1), and completely positive matrices have been constructed whose completely positive rank grows quadratically in the size of the matrix. This is the case, for instance, for the matrices

Ik k1Jk

1 kJk Ik ∈ CP2k,

![image 2](<2016-gribling-matrices-high-completely-positive_images/imageFile2.png>)

Mk =

![image 3](<2016-gribling-matrices-high-completely-positive_images/imageFile3.png>)

where cp-rank(Mk) = k2. Here Ik ∈ Sk is the identity matrix and Jk ∈ Sk is the all-ones matrix. This leads to the natural question of how fast cpsd-rankR(Mk) and cpsd-rankC(Mk) grow. As a second result we show that the completely positive semideﬁnite rank grows linearly for the matrices Mk, and we exhibit a link to the question of existence of Hadamard matrices. More precisely, we show that cpsd-rankC(Mk) = k for all k, and cpsd-rankR(Mk) = k if and only if there exists a real Hadamard matrix of order k. In particular, this shows that the real and complex completely positive semideﬁnite ranks can be diﬀerent.

The completely positive and completely positive semideﬁnite ranks are symmetric analogs of the nonnegative and positive semideﬁnite ranks. Here the nonnegative rank, denoted rank+(M), of a matrix M ∈ Rm×n

+ , is the smallest integer d for which there exist nonnegative vectors {ui} and {vj} in Rd+ such that Mi,j = ui,vj for all i and j, and the positive semideﬁnite rank, denoted rankpsd(M), is the smallest d for which there exist positive semideﬁnite matrices {Xi} and {Yj} in S+d such that Mi,j = Xi,Yj for all i and j. These notions have many applications, in particular to communication complexity and for the study of eﬃcient linear or semideﬁnite extensions of convex polyhedra (see [32, 13]). Unlike in the symmetric setting, in the asymmetric setting the following bounds, which show a linear regime, can easily be checked:

rankpsd(M) ≤ rank+(M) ≤ min(m,n). We refer to [11] and the references therein for a recent overview of results about the positive semideﬁnite rank.

Organization of the paper. In Section 2 we ﬁrst present some simple properties of the (real/complex) completely positive semideﬁnite rank, and then investigate its value for the matrices Mk, where we also show a link to the existence of Hadamard matrices. We also give a simple heuristic for ﬁnding approximate positive semideﬁnite factorizations. The proof of our main result in Theorem 1 boils down to several key ingredients which we treat in the subsequent sections.

- In Section 3 we group old and new results about the set of bipartite correlation

matrices. In particular, we give a geometric characterization of the extreme points, we revisit some conditions due to Tsirelson and links to rigidity theory, and we construct a class of extreme bipartite correlations with optimal parameters.

- In Section 4 we recall some characterizations, due to Tsirelson, of bipartite corre-


lations in terms of operator representations. We also recall connections to Cliﬀord algebras, and for bipartite correlations that are extreme points we relate their rank to the dimension of their operator representations.

Finally in Section 5 we introduce quantum correlations and recall their link to completely positive semideﬁnite matrices. We show how to construct quantum correlations from bipartite correlation matrices, and we prove the main theorem.

Note. Upon completion of this paper we learned of the recent independent work [22], where a class of matrices with exponential cpsd-rank is also constructed. The key idea of using extremal bipartite correlation matrices having large rank is the same. Our construction uses bipartite correlation matrices with optimized parameters meeting Tsirelson’s upper bound (8) (see Corollary 3.10). As a consequence, our completely positive semideﬁnite matrices have the best ratio between cpsd-rank and size that can be obtained using this technique.

2. Some properties of the completely positive semidefinite rank

In this section we consider the (complex) completely positive semideﬁnite rank of matrices in the completely positive cone. In particular, for a class of matrices, we show a quadratic separation in terms of the matrix size between the completely positive and completely positive semideﬁnite ranks. We also mention a simple heuristic for building completely positive semideﬁnite factorizations, which we have used to test several explicit examples.

We start by collecting some simple properties of the (complex) completely positive semideﬁnite rank. A ﬁrst observation is that if a matrix M admits a Gram representation by Hermitian positive semideﬁnite matrices of size d, then it also admits a Gram representation by real symmetric positive semideﬁnite matrices of size 2d, and thus M is completely positive semideﬁnite with cpsd-rankR(M) ≤ 2d. This is based on the well-known fact that mapping a Hermitian d × d matrix X to

1 √2

Re(X) Im(X) Im(X)T Re(X) ∈ S2d

![image 4](<2016-gribling-matrices-high-completely-positive_images/imageFile4.png>)

![image 5](<2016-gribling-matrices-high-completely-positive_images/imageFile5.png>)

is an isometry that preserves positive semideﬁniteness. The (complex) completely positive semideﬁnite rank is subadditive; that is, for A,B ∈ CS+n and K = R or K = C, we have

cpsd-rankK(A + B) ≤ cpsd-rankK(A) + cpsd-rankK(B), which can be seen as follows: If A is the Gram matrix of X1,...,Xn ∈ Kk×k and

- B is the Gram matrix of Y1,...,Yn ∈ Kr×r, then A + B is the Gram matrix of the matrices X1 ⊕ Y1,...,Xn ⊕ Yn ∈ K(k+r)×(k+r).


For M ∈ CS+n we have the inequalities cpsd-rankR(M) + 1 2 ≥ rank(M) and cpsd-rankC(M)2 ≥ rank(M),

since a factorization of M by real symmetric (resp., complex Hermitian) positive semideﬁnite r × r matrices yields another factorization of M by real vectors of size

r+1

2 (resp., by real vectors of size r2).

Finally, the next lemma shows that if the (complex) completely positive semideﬁnite rank of a matrix is high, then each factorization by (Hermitian) positive semideﬁnite matrices must contain at least one matrix with high rank.

- Lemma 2.1. Let M ∈ CS+n. For each Gram representation of M by (Hermitian) positive semideﬁnite matrices X1,...,Xn ∈ Kd×d, with K ∈ {R,C}, we have


cpsd-rankK(M) ≤ rank(X1 + ... + Xn). Proof. Let v1,...,vd−k be an orthonormal basis of ker(X1) ∩...∩ ker(Xn), and let

- u1,...,uk be an orthonormal basis of (ker(X1)∩...∩ker(Xn))⊥. Let U be the d×k matrix with columns u1,...,uk, and let V be the d × (d − k) matrix with columns
- v1,...,vd−k, so that P = U V is an orthogonal matrix. Set Yi = U∗XiU ∈ Kk×k for i ∈ [n]. Then Yi is (Hermitian) positive semideﬁnite. Since XiV = 0 by construction, we have


Yi,Yj = U∗XiU,U∗XjU = P∗XiP,P∗XjP = Xi,Xj for all i,j ∈ [n], which shows M = Gram(Y1,...,Yn). We have

cpsd-rankK(M) ≤ k = n − dim(ker(X1) ∩ ... ∩ ker(Xn)),

and because the matrices X1,...,Xn are positive semideﬁnite, the right hand side is equal to

n − dim(ker(X1 + ... + Xn)) = rank(X1 + ... + Xn).

- 2.1. A connection to the existence of Hadamard matrices. Consider the 2k × 2k matrix


Ik k1Jk

![image 6](<2016-gribling-matrices-high-completely-positive_images/imageFile6.png>)

,

Mk =

1 kJk Ik

![image 7](<2016-gribling-matrices-high-completely-positive_images/imageFile7.png>)

where Ik is the k × k identity matrix and Jk the k × k all-ones matrix. The completely positive rank of Mk equals k2, which is well known and easy to check (see Proposition 2.2 below). This means the completely positive rank of these matrices is within a constant factor of the upper bound (1). The signiﬁcance of the matrices Mk stems from the recently disproved (see [3, 4]) Drew-Johnson-Loewy conjecture [8]. This conjecture states that ⌊n2/4⌋ is an upper bound on the completely positive rank of n × n matrices, which means the matrices Mk are sharp for this bound.

It is therefore natural to ask whether the matrices Mk also have large (quadratic in k) completely positive semideﬁnite rank. As we see below this is not the case. We show that the complex completely positive semideﬁnite rank is k, and we show that the real completely positive semideﬁnite rank is equal to k if and only if a real Hadamard matrix of order k exists, which suggests that determining the completely positive semideﬁnite rank is a diﬃcult problem in general.

A real (complex) Hadamard matrix of order k is a k × k matrix with pairwise orthogonal columns and whose entries are ±1-valued (complex valued with unit modulus). A complex Hadamard matrix exists for any order; take for example

- (2) (Hk)i,j = e2πi(i−1)(j−1)/k for i,j ∈ [k].


On the other hand, it is still an open conjecture whether a real Hadamard matrix exists for each order k that is a multiple of 4.

For completeness we ﬁrst give a proof that the completely positive rank is k2. Here, the support of a vector u ∈ Rd is the set of indices i ∈ [d] for which ui = 0.

- Proposition 2.2. The completely positive rank of Mk is equal to k2.


√

√

![image 8](<2016-gribling-matrices-high-completely-positive_images/imageFile8.png>)

![image 9](<2016-gribling-matrices-high-completely-positive_images/imageFile9.png>)

Proof. For i ∈ [k] consider the vectors vi = 1/

k 1 ⊗ ei, where ei is the ith basis vector in Rk and 1 is the all-ones vector in Rk. The

k ei ⊗ 1 and ui = 1/

vectors v1,...,vk,u1,...,uk are nonnegative and form a Gram representation of Mk, which shows cp-rank(Mk) ≤ k2.

Suppose Mk = Gram(v1,v2,...,vk,u1,u2,...,uk) with vi,ui ∈ Rd+. In the remainder of the proof we show d ≥ k2. We have (Mk)i,j = δij for 1 ≤ i,j ≤ k. Since the vectors vi are nonnegative, they must have disjoint supports. The same holds for the vectors u1,...,uk. Since (Mk)i,j = 1/k > 0 for 1 ≤ i ≤ k and k+1 ≤ j ≤ 2k, the support of vi overlaps with the support of uj for each i and j. This means that for each i ∈ [k], the size of the support of the vector vi is at least k. This is only possible if d ≥ k2.

- Proposition 2.3. For each k we have cpsd-rankC(Mk) = k. Moreover, we have cpsd-rankR(Mk) = k if and only if there exists a real Hadamard matrix of order k.


Proof. The lower bound cpsd-rankC(Mk) ≥ k follows because Ik is a principal submatrix of Mk and cpsd-rankC(Ik) = k. To show cpsd-rankC(Mk) ≤ k, we give a factorization by Hermitian positive semideﬁnite k × k matrices. For this consider the complex Hadamard matrix Hk in (2) and deﬁne the factors

uiu∗i k

Xi = eieTi and Yi =

for i ∈ [k],

![image 10](<2016-gribling-matrices-high-completely-positive_images/imageFile10.png>)

where ei is the ith standard basis vector of Rk and ui is the ith column of Hk. By direct computation it follows that Mk = Gram(X1,...,Xk,Y1,...,Yk).

We now show that cpsd-rankR(Mk) = k if and only if there exists a real Hadamard matrix of order k. One direction follows directly from the above proof: If a real Hadamard matrix of size k exists, then we can replace Hk by this real matrix and this yields a factorization by real positive semideﬁnite k × k matrices.

Now assume cpsd-rankR(Mk) = k and let X1,...,Xk,Y1,...,Yk ∈ S+k be a Gram representation of M. We ﬁrst show there exist two orthonormal bases u1,...,uk and v1,...,vk of Rk such that Xi = uiuTi and Yi = viviT. For this we observe that I = Gram(X1,...,Xk), which implies Xi = 0 and XiXj = 0 for all i = j. Hence, for all i = j, the range of Xj is contained in the kernel of Xi. Therefore the range of Xi is orthogonal to the range of Xj. We now have ki=1dim(range(Xi)) ≤ k and dim(range(Xi)) ≥ 1 for all i. From this it follows that rank(Xi) = 1 for all i ∈ [k]. This means there exist u1,...,uk ∈ Rk such that Xi = uiuTi for all i. From I = Gram(X1,...,Xk) it follows that the vectors u1,...,uk form an orthonormal basis of Rk. The same argument can be made for the matrices Yi, thus Yi = viviT and the vectors v1,...,vk form an orthonormal basis of Rk. Up to an orthogonal transformation we may assume that the ﬁrst basis is the standard basis; that is, ui = ei for i ∈ [k]. We then obtain

1 k

= (Mk)i,j+k = ei,vj 2 = (vj)i 2 for i,j ∈ [k], hence (vj)i = ±1/

![image 11](<2016-gribling-matrices-high-completely-positive_images/imageFile11.png>)

√

√

![image 12](<2016-gribling-matrices-high-completely-positive_images/imageFile12.png>)

![image 13](<2016-gribling-matrices-high-completely-positive_images/imageFile13.png>)

k vk is a real Hadamard matrix.

k. Therefore, the k × k matrix whose kth column is

The above proposition leaves open the exact determination of cpsd-rankR(Mk) for the cases where a real Hadamard matrix of order k does not exist. Extensive experimentation using the heuristic from Section 2.2 suggests that for k = 3,5,6,7 the real completely positive semideﬁnite rank of Mk equals 2k, which leads to the following question:

- Question 2.4. Is the real completely positive semideﬁnite rank of Mk equal to 2k if a real Hadamard matrix of size k × k does not exist?


We also used the heuristic from Section 2.2 to check numerically that the aforementioned matrices from [3], which have completely positive rank greater than

⌊n2/4⌋, have small (smaller than n) real completely positive semideﬁnite rank. In fact, in our numerical experiments we never found a completely positive n × n matrix for which we could not ﬁnd a factorization in dimension n, which leads to the following question:

- Question 2.5. Is the real (or complex) completely positive semideﬁnite rank of a completely positive n × n matrix upper bounded by n?


- 2.2. A heuristic for ﬁnding Gram representations. In this section we give an adaptation to the symmetric setting of the seesaw method from [31], which is used

to ﬁnd good quantum strategies for nonlocal games. Given a matrix M ∈ CS+n with cpsd-rankR(M) ≤ d, we give a heuristic to ﬁnd a Gram representation of M by positive semideﬁnite d × d matrices. Although this heuristic is not guaranteed to converge to a factorization of M, for small n and d (say, n,d ≤ 10) it works well in practice by restarting the algorithm several times. The following algorithm seeks to minimize the function

E(X1,...,Xn) = max

i,j∈[n]

| Xi,Xj − Mi,j|.

Algorithm 2.6. Initialize the algorithm by setting k = 1 and generating random matrices X10,...,Xn0 ∈ S+d that satisfy Xi0,Xi0 = Mi,i for all i ∈ [n]. Iterate the following steps:

- (1) Let (δ,Y1,...,Yn) be a (near) optimal solution of the semideﬁnite program min δ : δ ∈ R+, Y1,...,Yn ∈ S+d , Xik−1,Yj − Mi,j ≤ δ for i,j ∈ [n] .
- (2) Perform a line search to ﬁnd the scalar r ∈ [0,1] minimizing E (1 − r)X1k−1 + rY1,...,(1 − r)Xnk−1 + rYn ,

and set Xik = (1 − r)Xik−1 + rYi for each i ∈ [n].

- (3) If E(X1k,...,Xnk) is not small enough, increase k by one and go to step (1). Otherwise, return the matrices X1k, ..., Xnk.


3. The set of bipartite correlations

In this section we deﬁne the set Cor(m,n) of bipartite correlations and we discuss properties of the extreme points of Cor(m,n), which will play a crucial role in the construction of CS+-matrices with large complex completely positive semideﬁnite rank. In particular we give a characterization of the extreme points of Cor(m,n) in terms of extreme points of the related set Em+n of correlation matrices. We use it to give a simple construction of a class of extreme points of Cor(m,n) with rank r, when m = n = r+12 . We also revisit conditions for extreme points introduced by Tsirelson [28] and point out links with universal rigidity. Based on these we can construct extreme points of Cor(m,n) with rank r when m = r and n = r2 + 1, which are used to prove our main result (Theorem 1).

- 3.1. Bipartite correlations and correlation matrices. A matrix C ∈ Rm×n is called a bipartite correlation matrix if there exist real unit vectors x1,...,xm,


- y1,...,yn ∈ Rd (for some d ≥ 1) such that Cs,t = xs,yt for all s ∈ [m] and t ∈ [n]. Following Tsirelson [28], any such system of real unit vectors is called a C-system. We let Cor(m,n) denote the set of all m × n bipartite correlation matrices.


The elliptope En is deﬁned as En = E ∈ S+n : Eii = 1 for i = 1,...,n ,

its elements are the correlation matrices, which can alternatively be deﬁned as all matrices of the form ( zi,zj )ni,j=1 for some real unit vectors z1,...,zn ∈ Rd (d ≥ 1). We have the surjective projection

- (3) π: Em+n → Cor(m,n),


Q C CT R  → C.

Hence, Cor(m,n) is a projection of the elliptope Em+n and therefore a convex set. Given C ∈ Cor(m,n), any matrix E ∈ Em+n such that π(E) = C is called an extension of C to the elliptope and we let ﬁb(C) denote the ﬁber (the set of extensions) of C.

Theorem 3.3 below characterizes extreme points of Cor(m,n) in terms of extreme points of Em+n. It is based on two intermediary results. The ﬁrst result (whose proof is easy) relates extreme points C ∈ Cor(m,n) to properties of their set of extensions ﬁb(C). It is shown in [9] in a more general setting.

- Lemma 3.1 ([9, Lemma 2.4]). Let C ∈ Cor(m,n). Then C is an extreme point


of Cor(m,n) if and only if the set ﬁb(C) is a face of Em+n. Moreover, if C is an extreme point of Cor(m,n), then every extreme point of ﬁb(C) is an extreme point of Em+n.

The second result (from Tsirelson [28]) shows that every extreme point C of Cor(m,n) has a unique extension E in Em+n, we give a proof for completeness. Lemma 3.2 ([28]). Assume C is an extreme point of Cor(m,n).

- (i) If x1,...,xm,y1,...,yn is a C-system, then Span{x1,...,xm} = Span{y1,...,yn}.
- (ii) The matrix C has a unique extension to a matrix E ∈ Em+n, and there exists a C-system x1,...,xm,y1,...,yn ∈ Rr, with r = rank(C), such that


E = Gram(x1,...,xm,y1,...,yn).

Proof. We will use the following observation: Each matrix C = ( as,bt )s∈[m],t∈[n], where as,bt are vectors with as , bt ≤ 1, belongs to Cor(m,n) since it satisﬁes

 

  for all (s,t) ∈ [m] × [n].

  ,

 

as 1 − as 2 0

bt 0

![image 14](<2016-gribling-matrices-high-completely-positive_images/imageFile14.png>)

Cs,t =

![image 15](<2016-gribling-matrices-high-completely-positive_images/imageFile15.png>)

1 − bt 2

(i) Set V = Span{x1,...,xm} and assume yk  ∈ V for some k ∈ [n]. Let w denote the orthogonal projection of yk onto V . Then w < 1 and one can choose a nonzero vector u ∈ V such that w+−u ≤ 1. Deﬁne the matrices C+− ∈ Rm×n by

xs,w +− u if t = k, xs,yt if t = k.

Cs,t+− =

Then, C+− ∈ Cor(m,n) (by the above observation) and C = (C+ + C−)/2. As

- C is an extreme point of Cor(m,n) one must have C = C+ = C−. Hence u is orthogonal to each xs and thus u = 0, a contradiction. This shows the inclusion Span{y1,...,ym} ⊆ Span{x1,...,xm} and the reverse one follows in the same way.


(ii) Assume {x′s,yt′} and {x′′s,yt′′} are two C-systems. We show x′r,x′s = x′′r,x′′s for all r,s ∈ S and yt′,yu′ = yt′′,yu′′ for all t,u ∈ T. For this deﬁne the vectors

x′s ⊕ x′′s √2

yt′ ⊕ yt′′ √2

xs =

and yt =

,

![image 16](<2016-gribling-matrices-high-completely-positive_images/imageFile16.png>)

![image 17](<2016-gribling-matrices-high-completely-positive_images/imageFile17.png>)

![image 18](<2016-gribling-matrices-high-completely-positive_images/imageFile18.png>)

![image 19](<2016-gribling-matrices-high-completely-positive_images/imageFile19.png>)

which again form a C-system. Using (i), for any s ∈ S, there exist scalars λst such that xs = t∈T λstyt and thus x′s = t∈T λstyt′ and x′′s = t∈T λstyt′′. This shows

x′r,x′s =

λrt yt′,x′s =

λrtCs,t =

λrt yt′′,x′′s = x′′r,x′′s

t∈T

t∈T

t∈T

for all r,s ∈ S. The analogous argument shows yt′,yu′ = yt′′,yu′′ for all t,u ∈ T. This shows C has a unique extension to a matrix E ∈ Em+n.

Finally, we show that rank(E) = rank(C). Say E is the Gram matrix of x1,...,xm,y1,...,yn. In view of (i), rank(E) = rank{x1,...,xm} and thus it suﬃces to show that rank{x1,...,xm} ≤ rank(C). For this note that if {xs : s ∈ I} (for some I ⊆ S) is linearly independent then the corresponding rows of C are linearly independent, since s∈I λs xs,yt = 0 (for all t ∈ T) implies s∈I λsxs = 0 (using (i)) and thus λs = 0 for all s.

Theorem 3.3. A matrix C is an extreme point of Cor(m,n) if and only if C has a unique extension to a matrix E ∈ Em+n and E is an extreme point of Em+n. Proof. Direct application of Lemma 3.1 and Lemma 3.2 (ii).

We can use the following lemma to construct explicit examples of extreme points of Cor(m,n) for the case m = n.

- Lemma 3.4. Each extreme point of En is an extreme point of Cor(n,n). Proof. Let C be an extreme point of En. Deﬁne the matrix


C C C C

E =

.

Then E ∈ E2n is an extension of C. In view of Theorem 3.3 it suﬃces to show that E is the unique extension of C and that E is an extreme point of E2n. With e1,...,en denoting the standard unit vectors in Rn, observe that the vectors ei⊕−ei (i ∈ [n]) lie in the kernel of any matrix E′ ∈ ﬁb(C). Indeed, since E′ and C have an all-ones diagonal we have

(ei ⊕ −ei)TE′(ei ⊕ −ei) = 0, and since E′ is positive semideﬁnite this implies that ei ⊕ −ei ∈ ker(E′). This implies that ﬁb(C) = {E}. We now show that E is an extreme point of E2n. For this let E1,E2 ∈ E2n and 0 < λ < 1 such that E = λE1 + (1 − λ)E2. As E1,E2 are positive semideﬁnite, the kernel of E is the intersection of the kernels of E1 and E2. Hence the vectors ei ⊕ −ei belong to the kernels of E1 and E2 and thus

C2 C2 C2 C2

C1 C1 C1 C1

and E2 =

E1 =

for some C1,C2 ∈ En. Hence, C = λC1 + (1 − λ)C2, which implies C = C1 = C2, since C is an extreme point of En. Thus E = E1 = E2, which completes the proof.

The above lemma shows how to construct extreme points of Cor(n,n) from extreme points of the elliptope En. Li and Tam [20] give the following characterization of the extreme points of En.

Theorem 3.5 ([20]). Consider a matrix E ∈ En with rank r and unit vectors

- z1,...,zn ∈ Rr such that E = Gram(z1,...,zn). Then E is an extreme point of En if and only if


r + 1 2

= dim(Span{z1z1T,...,znznT}).

- (4)


In particular, if E is an extreme point of En, then r+12 ≤ n.

Example 3.6 ([20]). For each integer r ≥ 1 there exists an extreme point of En of rank r, where n = r+12 . For example, let e1,...,er be the standard basis vectors of Rr and deﬁne

e1 + e2 √2

E = Gram e1,...,er,

,

![image 20](<2016-gribling-matrices-high-completely-positive_images/imageFile20.png>)

![image 21](<2016-gribling-matrices-high-completely-positive_images/imageFile21.png>)

e1 + e3 √2

,...,

![image 22](<2016-gribling-matrices-high-completely-positive_images/imageFile22.png>)

![image 23](<2016-gribling-matrices-high-completely-positive_images/imageFile23.png>)

er−1 + er √2

![image 24](<2016-gribling-matrices-high-completely-positive_images/imageFile24.png>)

![image 25](<2016-gribling-matrices-high-completely-positive_images/imageFile25.png>)

.

Then E is an extreme point of En of rank r. Note that the above example is optimal in the sense that a rank r extreme

point of En can exist only if n ≥ r+12 (by Theorem 3.5). By combining this with Lemma 3.4, this gives a class of extreme points of Cor(m,n) with rank r and

m = n = r+12 .

- 3.2. Tsirelson’s bound. If C is an extreme point of Cor(m,n) with rank r, then by Theorems 3.3 and 3.5 we have r+12 ≤ m+n. Tsirelson [29] claimed the stronger


bound r+12 ≤ m + n − 1 (see Corollary 3.10 below). In the rest of this section we show how to derive this stronger bound of Tsirelson (which is given in [29] without

proof). In the next section, we construct two classes of extreme bipartite correlation matrices, of which one meets Tsirelson’s bound. To show Tsirelson’s bound we need to investigate in more detail the unique extension property for extreme points of Cor(m,n).

Let C ∈ Cor(m,n) with rank r, let {xs}, {yt} be a C-system in Rr, and let

E = Gram(x1,...,xm,y1,...,yn) ∈ Em+n. In view of Theorem 3.3, if C is an extreme point of Cor(m,n), then E is the unique extension of C in Em+n. This uniqueness property can be rephrased as the requirement that an associated semideﬁnite program has a unique solution. Namely, consider the following dual pair of semideﬁnite programs:

- (5) max 0 : X ∈ S+S∪T, Xk,k = 1 for k ∈ S ∪ T, Xs,t = Cs,t for s ∈ S,t ∈ T ,
- (6) min s∈S


Diag(λ) W WT Diag(µ) ∈ S+S∪T .

λs+

µt+2

Ws,tCs,t : Ω =

t∈T

s∈S,t∈T

The feasible region of problem (5) consists of all possible extensions of C in Em+n, and the feasible region of (6) consists of the positive semideﬁnite matrices Ω whose support (consisting of all oﬀ-diagonal pairs (i,j) with Ωi,j = 0) is contained in the complete bipartite graph with bipartition S ∪ T. Moreover, the optimal values of both problems are equal to 0. Finally, for any primal feasible (optimal) X and dual optimal Ω, equality ΩX = 0 holds, which implies that rank(X)+rank(Ω) ≤ m+n.

Theorem 3.7 below (shown in [19] in the more general context of universal rigidity) shows that if equality rank(X) + rank(Ω) = m + n holds (also known as strict complementarity), then X is in fact the unique feasible solution of program (5), and thus C has a unique extension in Em+n.

Theorem 3.7. Let C ∈ Cor(m,n) and let {xs}, {yt} be a C-system spanning Rr. Assume E = Gram(x1,...,xm,y1,...,yn) is an extreme point of Em+n. If there exists an optimal solution Ω of program (6) with rank(Ω) = m + n − r, then E is the only extension of C in Em+n.

Proof. Apply [19, Theorem 3.2] to the bar framework G(p), where G is the complete bipartite graph Km,n with bipartition S ∪ T and p = {xs(s ∈ S),yt(t ∈ T)}. Note that the conditions (v), (vi) in [19, Theorem 3.2] follow from ΩE = 0 and the fact that {xs},{yt} ⊂ Rr are C-systems spanning Rr.

In addition one can relate uniqueness of an extension of C in the elliptope to the existence of a quadric separating the two point sets {xs} and {yt} (Theorem 3.9 below). Roughly speaking, such a quadric allows us to construct a suitable optimal dual solution Ω and to apply Theorem 3.7. This property was stated by Tsirelson

- [29], however without proof. Interestingly, an analogous result was shown recently by Connelly and Gortler [7] in the setting of universal rigidity. We will give a sketch of a proof for Theorem 3.9. For this we use Theorem 3.7, arguments in [7], and the following basic property of semideﬁnite programs (which can be seen as an analog of Farkas’ lemma for linear programs).


Lemma 3.8. Given A1,...,Am ∈ Sn and b ∈ Rm, and assume that there exists a matrix X ∈ Sn such that Aj,X = bj for all j ∈ [m]. Then exactly one of the following two alternatives holds:

- (i) There exists a matrix X ≻ 0 such that Aj,X = bj for all j ∈ [m].
- (ii) There exists y ∈ Rm such that Ω = mj=1 yjAj 0, Ω = 0, and ΩX = 0.


- Theorem 3.9 ([29, Theorems 2.21-2.22]). Let C ∈ Cor(m,n), let {xs}, {yt} be a C-system spanning Rr, and let E = Gram(x1,...,xm,y1,...,yn) ∈ Em+n.


(i) If C is an extreme point of Cor(m,n), then there exist nonnegative scalars λ1,...,λm, µ1,...,µn, not all equal to zero, such that

- (7)


m

n

λsxsxTs =

µtytytT.

s=1

t=1

(ii) If E is an extreme point of Em+n and there exist strictly positive scalars λ1,...,λm,µ1,...,µn for which relation (7) holds, then C is an extreme point of Cor(m,n).

Proof. (i) By assumption, C is an extreme point of Cor(m,n), so by Lemma 3.2 (ii) E is the only feasible solution of the program (5). As E has rank r < m + n, it follows that the program (5) does not have a positive deﬁnite feasible solution. Applying Lemma 3.8 it follows that there exists a nonzero matrix Ω that is feasible for the dual program (6) and satisﬁes ΩE = 0. This gives:

λsxs +

Ws,tyt = 0 (s ∈ S), µtyt +

Ws,txs = 0 (t ∈ T).

t∈T

s∈S

Since Ω 0, the scalars λs,µt are nonnegative. We claim that they satisfy (7). We multiply the left relation by xTs and the right one by ytT to obtain

λsxsxTs +

Ws,tytxTs = 0 (s ∈ S), µtytytT +

Ws,txsytT = 0 (t ∈ T).

t∈T

s∈S

Summing the left relation over s ∈ S, and summing the right relation over t ∈ T and taking the transpose, we get:

λsxsxTs = −

Ws,tytxTs =

µtytytT,

s∈S

s∈S t∈T

t∈T

and thus (7) holds.

(ii) Assume that E is an extreme point of Em+n and that there exist strictly positive scalars λ1,...,λm,µ1,...,µn for which (7) holds. The key idea is to construct a matrix Ω that is optimal for the program (6) and has rank m + n − r, since then we can apply Theorem 3.7 and conclude that E is the only extension of C in Em+n. The construction of such a matrix Ω is analogous to the construction given in [7] for frameworks (see Theorem 4.3 and its proof), so we omit the details.

- Corollary 3.10 ([29]). If C is an extreme point of Cor(m,n), then


- (8)


rank(C) + 1 2 ≤ n + m − 1.

Proof. Let x1,...,xm,y1,...,yn ∈ Rr, with r = rank(C), be a C-system spanning Rr and let E be their Gram matrix. As E is an extreme point of Em+n, it follows from relation (4) that Sr is spanned by the m+n matrices xixTi ,yjyjT (i ∈ S,j ∈ T). Combining this with the identity (7) this implies that Sr is spanned by a set of

- m + n − 1 matrices and thus its dimension r+12 is at most m + n − 1. Our ﬁrst construction in the next section provides instances where the bound

- (8) is tight.


3.3. Constructions of extreme bipartite correlation matrices. We construct two families of extreme points of Cor(m,n), which we will use in Section 5 to construct completely positive semideﬁnite matrices with exponentially large completely positive semideﬁnite rank. The ﬁrst construction meets Tsirelson’s bound and is used to prove Theorem 1. The second construction will be used to recover one of the results of [27].

We begin with constructing a family of extreme points C1 of Cor(m,n) with

rank(C1) = r, m = r, and n = r2 + 1, which thus shows that inequality (8) is tight. Such a family of bipartite correlation matrices can also be inferred from

[30], where the correlation matrices are obtained through analytical methods as optimal solutions of linear optimization problems over Cor(m,n). Instead, we use the suﬃcient conditions for extremality of bipartite correlations given above.

For this we will construct matrices E1,Ω1 ∈ Sr+n that satisfy the conditions of

- Theorem 3.7; that is, E1 is an extreme point of Er+n, Ω1 is positive semideﬁnite with support contained in the complete bipartite graph Kr,n, rank(E1) = r, rank(Ω1) =


- n, and Ω1E1 = 0. Our construction of Ω1 is inspired by [14], which studies the maximum possible rank of extremal positive semideﬁnite matrices with a complete bipartite support.


Consider the matrix B ∈ Rr×(r

), whose columns are indexed by the pairs (i,j)

2

with 1 ≤ i < j ≤ r, with entries Bi,(i,j) = 1, Bj,(i,j) = −1 for 1 ≤ i < j ≤ r, and all other entries 0. We also consider the matrix B ∈ Rr×n obtained by adjoining

to B a last column equal to the all-ones vector e. Note that BBT = rIr and

- B BT = rIr − Jr. Then deﬁne the following matrices:


√n

√ nInBr T √rInBn ∈ Sr+n, E′ =

![image 26](<2016-gribling-matrices-high-completely-positive_images/imageFile26.png>)

![image 27](<2016-gribling-matrices-high-completely-positive_images/imageFile27.png>)

r B −

Ir −

r BT rn2BTB ∈ Sr+n. Since

Ω′ =

![image 28](<2016-gribling-matrices-high-completely-positive_images/imageFile28.png>)

√n

![image 29](<2016-gribling-matrices-high-completely-positive_images/imageFile29.png>)

![image 30](<2016-gribling-matrices-high-completely-positive_images/imageFile30.png>)

![image 31](<2016-gribling-matrices-high-completely-positive_images/imageFile31.png>)

![image 32](<2016-gribling-matrices-high-completely-positive_images/imageFile32.png>)

T

T

n √rIr Bn

n √rIr Bn

Ir −

Ir −

![image 33](<2016-gribling-matrices-high-completely-positive_images/imageFile33.png>)

![image 34](<2016-gribling-matrices-high-completely-positive_images/imageFile34.png>)

and E′ =

Ω′ =

![image 35](<2016-gribling-matrices-high-completely-positive_images/imageFile35.png>)

![image 36](<2016-gribling-matrices-high-completely-positive_images/imageFile36.png>)

√n

√n

,

![image 37](<2016-gribling-matrices-high-completely-positive_images/imageFile37.png>)

![image 38](<2016-gribling-matrices-high-completely-positive_images/imageFile38.png>)

![image 39](<2016-gribling-matrices-high-completely-positive_images/imageFile39.png>)

![image 40](<2016-gribling-matrices-high-completely-positive_images/imageFile40.png>)

r BT

r BT

![image 41](<2016-gribling-matrices-high-completely-positive_images/imageFile41.png>)

![image 42](<2016-gribling-matrices-high-completely-positive_images/imageFile42.png>)

it follows that Ω′ and E′ are positive semideﬁnite, Ω′E′ = 0, rank(Ω′) = n, and rank(E′) = r. It suﬃces now to modify the matrix E′ in order to get a matrix E1 with an all-ones diagonal. For this, consider the diagonal matrix

![image 43](<2016-gribling-matrices-high-completely-positive_images/imageFile43.png>)

r n

r √2n

In−1 ⊕

D = Ir ⊕

I1

![image 44](<2016-gribling-matrices-high-completely-positive_images/imageFile44.png>)

![image 45](<2016-gribling-matrices-high-completely-positive_images/imageFile45.png>)

![image 46](<2016-gribling-matrices-high-completely-positive_images/imageFile46.png>)

and set E1 = DE′D and Ω1 = D−1Ω′D−1. Then E1 has an all-ones diagonal, it is in fact the Gram matrix of the vectors e1,...,er, (ei−ej)/√2 (for 1 ≤ i < j ≤ r), and (e1 + ... + er)/√r, and thus E1 is an extreme point of Er+n. Moreover, Ω1E1 = 0, rankE1 = r, and rankΩ1 = n. Therefore the conditions of Theorem 3.7 are fulﬁlled

![image 47](<2016-gribling-matrices-high-completely-positive_images/imageFile47.png>)

![image 48](<2016-gribling-matrices-high-completely-positive_images/imageFile48.png>)

and we can conclude that the matrix C1 = π(E1) is an extreme point of Cor(r,n). So we have shown part (i) in Theorem 3.11 below.

Our second construction is inspired by the XOR-game considered by Slofstra in [27, Section 7.2]. We construct a family of extreme points C2 of Cor(m,n) with rank(C2) = r − 1, m = r and n = r2 . Deﬁne the (r + n) × (r + n) matrices

√nIr B BT √rnIn

1 r−1 B BT −2√rn B −2√rn BT 12 BT B

![image 49](<2016-gribling-matrices-high-completely-positive_images/imageFile49.png>)

![image 50](<2016-gribling-matrices-high-completely-positive_images/imageFile50.png>)

![image 51](<2016-gribling-matrices-high-completely-positive_images/imageFile51.png>)

![image 52](<2016-gribling-matrices-high-completely-positive_images/imageFile52.png>)

Ω2 =

.

, E2 =

![image 53](<2016-gribling-matrices-high-completely-positive_images/imageFile53.png>)

![image 54](<2016-gribling-matrices-high-completely-positive_images/imageFile54.png>)

![image 55](<2016-gribling-matrices-high-completely-positive_images/imageFile55.png>)

![image 56](<2016-gribling-matrices-high-completely-positive_images/imageFile56.png>)

![image 57](<2016-gribling-matrices-high-completely-positive_images/imageFile57.png>)

Note that

T

T

√ −21n B BT √12 BT

√ −21n B BT √12 BT

√ 1r B √1re r nIn 0

√ 1r B √1re r nIn 0

Ω2 = √n

![image 58](<2016-gribling-matrices-high-completely-positive_images/imageFile58.png>)

![image 59](<2016-gribling-matrices-high-completely-positive_images/imageFile59.png>)

![image 60](<2016-gribling-matrices-high-completely-positive_images/imageFile60.png>)

![image 61](<2016-gribling-matrices-high-completely-positive_images/imageFile61.png>)

![image 62](<2016-gribling-matrices-high-completely-positive_images/imageFile62.png>)

![image 63](<2016-gribling-matrices-high-completely-positive_images/imageFile63.png>)

![image 64](<2016-gribling-matrices-high-completely-positive_images/imageFile64.png>)

![image 65](<2016-gribling-matrices-high-completely-positive_images/imageFile65.png>)

![image 66](<2016-gribling-matrices-high-completely-positive_images/imageFile66.png>)

![image 67](<2016-gribling-matrices-high-completely-positive_images/imageFile67.png>)

![image 68](<2016-gribling-matrices-high-completely-positive_images/imageFile68.png>)

![image 69](<2016-gribling-matrices-high-completely-positive_images/imageFile69.png>)

![image 70](<2016-gribling-matrices-high-completely-positive_images/imageFile70.png>)

,

, E2 =

![image 71](<2016-gribling-matrices-high-completely-positive_images/imageFile71.png>)

![image 72](<2016-gribling-matrices-high-completely-positive_images/imageFile72.png>)

![image 73](<2016-gribling-matrices-high-completely-positive_images/imageFile73.png>)

![image 74](<2016-gribling-matrices-high-completely-positive_images/imageFile74.png>)

![image 75](<2016-gribling-matrices-high-completely-positive_images/imageFile75.png>)

![image 76](<2016-gribling-matrices-high-completely-positive_images/imageFile76.png>)

![image 77](<2016-gribling-matrices-high-completely-positive_images/imageFile77.png>)

![image 78](<2016-gribling-matrices-high-completely-positive_images/imageFile78.png>)

where we use that B BT B = (rIr − Jr) B = r B. It follows that Ω2 and E2 are positive semideﬁnite, rank(Ω2) = n + 1 and rank(E2) = r − 1. Moreover, one can check that Ω2E2 = 0. In order to be able to apply Theorem 3.7 it remains to verify that E2 is an extreme point of Er+n.

The above factorization of E2 shows that it is the Gram matrix of the system of vectors in Rr:

1 √2n

1 √2

uk =

(e − rek) : k ∈ [r] ∪ vij =

(ei − ej) : 1 ≤ i < j ≤ r .

![image 79](<2016-gribling-matrices-high-completely-positive_images/imageFile79.png>)

![image 80](<2016-gribling-matrices-high-completely-positive_images/imageFile80.png>)

![image 81](<2016-gribling-matrices-high-completely-positive_images/imageFile81.png>)

![image 82](<2016-gribling-matrices-high-completely-positive_images/imageFile82.png>)

As the vectors uk,vij lie in Rr while E2 has rank r − 1 we need to consider another Gram representation of E2 by vectors in Rr−1. For this, let Q be an r × r orthogonal matrix with columns p1,...,pr and pr = 1/√re. Then the vectors {QTuk} ∪ {QTvij} form again a Gram representation of E2. Furthermore, as all uk,vij are orthogonal to the vector pr it follows that the vectors QTuk and QTvij are all orthogonal to QTpr = er. Hence QTuk = (xk,0) and QTvij = (yij,0) for some vectors xk,yij ∈ Rr−1 which now provide a Gram representation of E2 in Rr−1.

![image 83](<2016-gribling-matrices-high-completely-positive_images/imageFile83.png>)

In order to conclude that E2 is an extreme point of Er+n it suﬃces, by Theorem 3.5, to verify that the set {xkxTk} ∪ {yijyijT} spans the whole space Sr−1. Equivalently, we must show that the set {QTukuTkQ}∪{QTvijvijTQ} spans the subspace {R ⊕ 0 : R ∈ Sr−1} of Sr, or, in other words, that the set {ukuTk} ∪ {vijvijT} spans the subspace

M := {Q(R ⊕ 0)QT : R ∈ Sr−1} ⊆ Sr.

Observe that dim(M) = 2 r . We also have that span{vijvijT : 1 ≤ i < j ≤ r} is contained in

span({ukuTk : k ∈ [r]} ∪ {vijvijT : 1 ≤ i < j ≤ r}) ⊆ M, and that

span{vijvijT : 1 ≤ i < j ≤ r} = span{(ei − ej)(ei − ej)T : 1 ≤ i < j ≤ r} has dimension r2 . Therefore, equality holds throughout:

span({ukuTk : k ∈ [r]} ∪ {vijvijT : 1 ≤ i < j ≤ r}) = M, and thus E2 is an extreme point of Er+n.

This shows that the conditions of Theorem 3.7 are satisﬁed and we can conclude that the matrix C2 = π(E2) is an extreme point of Cor(r,n). So we have shown part (ii) in Theorem 3.11 below.

- Theorem 3.11. Consider an integer r ≥ 1 and let e1,...,er denote the standard unit vectors in Rr.


- (i) There exists a matrix C1 which is an extreme point of C(r, r2 + 1) and has rank r. We can take C1 to be the matrix with columns (ei − ej)/√2 (for 1 ≤ i < j ≤ r) and (e1 + ... + er)/√r.

![image 84](<2016-gribling-matrices-high-completely-positive_images/imageFile84.png>)

![image 85](<2016-gribling-matrices-high-completely-positive_images/imageFile85.png>)

- (ii) There exists a matrix C2 which is an extreme point of Cor(r, r2 ) and has rank r − 1. We can take C2 to be the matrix whose columns are − r/(2(r − 1))(ei − ej) for 1 ≤ i < j ≤ r.


![image 86](<2016-gribling-matrices-high-completely-positive_images/imageFile86.png>)

We conclude this section with explaining how our second construction permits to recover a lower bound of Slofstra [27] for the amount of entanglement needed by any optimal quantum strategy for the XOR-game he considers in [27, Section 7.2].

The goal of an XOR-game is to ﬁnd a quantum strategy with maximal winning probability, or, equivalently, a strategy that maximizes the bias of the game. For an introduction to XOR-games we refer to, e.g., [2, 6]. An XOR-game is given by a game matrix, and the game presented in [27, Section 7.2] has game matrix B as deﬁned above. An optimal quantum strategy corresponds to an optimal solution of the following optimization problem:

- (9) max{  B,C : C ∈ Cor(m,n)}.

Slofstra [27] showed (using the notion of ‘solution algebra’ of the game) that any tensor operator representation of any optimal solution C of (9) has local dimension at least 2⌊(r−1)/2⌋ (see Section 4 for the deﬁnition of a tensor operator representation). As we now point out this can also be derived from Tsirelson’s results using our treatment.

For this note ﬁrst that problem (9) is equivalent to

- (10) min{  B,C : C ∈ Cor(m,n)}

(since C ∈ Cor(m,n) if and only if −C ∈ Cor(m,n)). Problem (10) is in turn equivalent to the following optimization problem over the elliptope:

- (11) min{ Ω2,E : E ∈ Em+n},


with Ω2 being deﬁned as above (since E ∈ Em+n is optimal for (11) if and only if C = π(E) ∈ Cor(m,n) is optimal for (10)). As Ω2 is positive semideﬁnite and

Ω2,E2 = 0, it follows that E2 is optimal for (11) and thus C2 = π(E2) is optimal for (10). Moreover, as rank(E2) = m + n − rank(Ω2) is the largest possible rank of an optimal solution of (11), it follows from a geometric property of semideﬁnite programming that E2 must lie in the relative interior of the set of optimal solutions of (11). This, combined with the fact that E2 is an extreme point of Em+n, implies that E2 is the unique optimal solution of (11) and thus C2 is the unique optimal solution of (10). Finally, as C2 is an extreme point of Cor(m,n) with rank r − 1, we can conclude using Corollary 4.5 below that any tensor operator representation of C2 uses local dimension at least 2⌊(r−1)/2⌋, and the same holds for the unique optimal solution −C2 of (9).

4. Lower bounding the size of operator representations

We start with recalling, in Theorem 4.1, some equivalent characterizations for bipartite correlations in terms of operator representations, due to Tsirelson. For this consider a matrix C ∈ Rm×n. We say that C admits a tensor operator representation if there exist an integer d (the local dimension), a unit vector ψ ∈ Cd⊗Cd, and Hermitian d × d matrices {Xs}ms=1 and {Yt}nt=1 with spectra contained in [−1,1], such that Cs,t = ψ∗(Xs ⊗ Yt)ψ for all s and t.

Moreover we say that C admits a (ﬁnite dimensional) commuting operator representation if there exist an integer d, a Hermitian positive semideﬁnite d × d matrix W with trace(W) = 1, and Hermitian d × d matrices {Xs} and {Yt} with spectra

contained in [−1,1], such that XsYt = YtXs and Cs,t = Tr(XsYtW) for all s and t. A commuting operator representation is said to be pure if rank(W) = 1.

Existence of these various operator representations relies on using Cliﬀord algebras. For an integer r ≥ 1 the Cliﬀord algebra C(r) of order r can be deﬁned as the universal C∗-algebra with Hermitian generators a1,...,ar and relations

- (12) a2i = 1 and aiaj + ajai = 0 for i = j.

We call these relations the Cliﬀord relations. To represent the elements of C(r) by matrices we can use the following map, which is a ∗-isomorphism onto its image:

- (13) ϕr : C(r) → C2


⊗ X ⊗ I⊗⌈r2⌉−i+12 for i odd, Z⊗

i−1 2

Z⊗

![image 87](<2016-gribling-matrices-high-completely-positive_images/imageFile87.png>)

![image 88](<2016-gribling-matrices-high-completely-positive_images/imageFile88.png>)

![image 89](<2016-gribling-matrices-high-completely-positive_images/imageFile89.png>)

⌈r/2⌉×2⌈r/2⌉, ϕr(ai) =

i−2 2

2⌉−2i for i even. Here we use the Pauli matrices

r

⊗ Y ⊗ I⊗⌈

![image 90](<2016-gribling-matrices-high-completely-positive_images/imageFile90.png>)

![image 91](<2016-gribling-matrices-high-completely-positive_images/imageFile91.png>)

![image 92](<2016-gribling-matrices-high-completely-positive_images/imageFile92.png>)

- 0 1
- 1 0


0 −i i 0

1 0 0 −1

X =

, Y =

, Z =

.

For even r the representation ϕr is irreducible and thus C(r) is isomorphic to the full matrix algebra with matrix size 2r/2. For odd r the representation ϕr decomposes as a direct sum of two irreducible representations, each of dimension 2⌊r/2⌋. Therefore, if X1,...,Xr is a set of Hermitian matrices satisfying the relations Xi2 = I and XiXj + XjXi = 0 for i = j, then they must have size at least 2⌊r/2⌋. We refer to [23, Section 5.4] for details about (representations of) Cliﬀord algebras.

- Theorem 4.1 ([28]). Let C ∈ Rm×n. The following statements are equivalent:


- (1) C is a bipartite correlation.
- (2) C admits a tensor operator representation.
- (3) C admits a pure commuting operator representation.
- (4) C admits a commuting operator representation.


Proof. (1) ⇒ (2) Let C ∈ Cor(m,n). That means there exist unit vectors {xs} and {yt} in Rr, where r = rank(C), such that Cs,t = xs,yt for all s and t. Set d = 2⌊r/2⌋ and deﬁne

r

r

(yt)iπ(ai)T,

(xs)iπ(ai), Yt =

Xs =

i=1

i=1

where π is an irreducible representation of C(r) by matrices of size d (note that for r even we could use the explicit representation ϕr). With ψ = √1d di=1 ei ⊗ ei one can use the Cliﬀord relations to derive the following identity (see for example [2]): Cs,t = xs,yt = Tr(XsYtT)/d = ψ∗(Xs ⊗ Yt)ψ for all s ∈ S,t ∈ T.

![image 93](<2016-gribling-matrices-high-completely-positive_images/imageFile93.png>)

![image 94](<2016-gribling-matrices-high-completely-positive_images/imageFile94.png>)

The eigenvalues of the matrices π(a1),...,π(ar) lie in {−1,1}, and the Cliﬀord relations (12) can be used to derive that the eigenvalues of Xs and Yt also lie in {−1,1}. Thus, ({Xs},{Yt},ψ) is a tensor operator representation of C.

(2) ⇒ (3) If ({Xs},{Yt},ψ) is a tensor operator representation of C, then the operators Xs ⊗ I and I ⊗ Yt commute, and by using the identity

ψ∗(Xs ⊗ Yt)ψ = Tr((Xs ⊗ I)(I ⊗ Yt)ψψ∗) we see that ({Xs ⊗I},{I ⊗Yy},ψψ∗) is a pure commuting operator representation.

- (3) ⇒ (4) This is immediate.
- (4) ⇒ (1) Suppose ({Xs},{Yt},W) is a commuting operator representation of


- C. Since W is positive semideﬁnite and has trace 1, there exist nonnegative scalars


λi and orthonormal unit vectors ψi ∈ Cd ⊗ Cd such that W = i λiψiψi∗ and i λi = 1. Then,

λi Tr(XsYtψiψi∗) =

λiψi∗XsYtψi. So, with

Cs,t = Tr(XsYtW) =

i

i

xs =

i

![image 95](<2016-gribling-matrices-high-completely-positive_images/imageFile95.png>)

λi

Re(Xsψi) Im(Xsψi)

and yt =

i

![image 96](<2016-gribling-matrices-high-completely-positive_images/imageFile96.png>)

λi

Re(Ytψi) Im(Ytψi)

we have Cs,t = xs,yt and xs , ys ≤ 1, and by using the observation in the proof of Lemma 3.2 we can extend the vectors xs and yt to unit vectors.

- Corollary 4.2. If C is a bipartite correlation matrix of rank r, then it admits a tensor operator representation in local dimension 2⌊r/2⌋. If C is a bipartite correlation matrix that admits a tensor operator representation in local dimension d, then it has a commuting operator representation by matrices of size d2.


The remainder of this section is devoted to showing that there are bipartite correlation matrices for which every operator representation requires a large dimension.

For this we need two more deﬁnitions. A commuting operator representation ({Xs},{Yt},W) is nondegenerate if there does not exist a projection matrix P = I such that PWP = W, XsP = PXs, and YtP = PYt for all s and t. It is said to be Cliﬀord if there exist matrices Q ∈ Rm×m and R ∈ Rn×n with all-ones diagonals, such that

XsXs′ + Xs′Xs = 2Qs,s′I for all s,s′ ∈ S, YtYt′ + Yt′Yt = 2Rt,t′I for all t,t′ ∈ T. We will use the following theorem from Tsirelson as crucial ingredient.

- Theorem 4.3 ([28, Theorem 3.1]). If C is an extreme point of Cor(m,n), then any nondegenerate commuting operator representation of C is Cliﬀord.


We can now state and prove the main result of this section.

- Theorem 4.4. Let C be an extreme point of Cor(m,n) and let r = rank(C). Every commuting operator representation of C uses matrices of size at least (2⌊r/2⌋)2.


Proof. Let ({Xs},{Yt},W) be a commuting operator representation of C where Xs,Yt and W are matrices of size d. We will show d ≥ (2⌊r/2⌋)2. If this representation is degenerate, then there exists a projection matrix P = I such that PWP = W, XsP = PXs, and YtP = PYt for all s and t. Let P = ki=1 vivi∗ be its spectral decomposition, where the vectors v1,...,vk are orthonormal, and set U = (v1,...,vk). Then one can verify that ({U∗XsU},{U∗YsU},U∗WU) is a commuting operator representation of C of smaller dimension. So, since we are proving a lower bound on the dimension, we may assume ({Xs},{Yt},W) to be a nondegenerate commuting operator representation.

By extremality of C we may assume the operator representation is pure. Hence, there is a unit vector ψ such that W = ψψ∗. This gives

Cs,t = Tr(XsYtW) = ψ∗XsYtψ = xs,yt , where

Re(Xsψ) Im(Xsψ)

Re(Ytψ) Im(Ytψ)

xs =

and yt =

.

These vectors xs and yt are unit vectors because C is extreme (see the proof of Lemma 3.2), and therefore, they form a C-system.

By Theorem 4.3 the commuting operator representation ({Xs},{Yt},W) is Clifford. So, there exist matrices Q ∈ Rm×m and R ∈ Rn×n with all-one diagonals such that

XsXs′ + Xs′Xs = 2Qs,s′I for all s,s′ ∈ S,

YtYt′ + Yt′Yt = 2Rt,t′I for all t,t′ ∈ T. We show that E is an extension to the elliptope of C, where

Q C CT R

E =

. For this, we have to show Qs,s′ = xs,xs′ and Rt,t′ = yt,yt′ . Indeed, xs,xs′ + xs′,xs = Re ψ∗XsXs′ψ + ψ∗Xs′Xsψ

= Re ψ∗(XsXs′ + Xs′Xs)ψ

= Re ψ∗(2Qs,s′I)ψ = 2Qs,s′, and in the same way yt,yt′ + yt′,yt = 2Rt,t′.

By Theorem 3.3 the matrix E is the unique extension of C to the elliptope. Furthermore, Lemma 3.2 tells us that rank(Q) = rank(R) = rank(C) = r.

Consider the spectral decomposition Q = ri=1 αivivi∗, where the vectors v1,...,vr are orthonormal, and consider the algebra C A1,...,Ar , where

m

1 √αi

Ai =

(vi)sXs for i ∈ [r]. We have

![image 97](<2016-gribling-matrices-high-completely-positive_images/imageFile97.png>)

![image 98](<2016-gribling-matrices-high-completely-positive_images/imageFile98.png>)

s=1

m

1 √αiαj

((vi)s(vj)s′XsXs′ + (vj)s(vi)s′XsXs′)

AiAj + AjAi =

![image 99](<2016-gribling-matrices-high-completely-positive_images/imageFile99.png>)

![image 100](<2016-gribling-matrices-high-completely-positive_images/imageFile100.png>)

s,s′=1

m

1 √αiαj

(vi)s(vj)s′ (XsXs′ + Xs′Xs)

=

![image 101](<2016-gribling-matrices-high-completely-positive_images/imageFile101.png>)

![image 102](<2016-gribling-matrices-high-completely-positive_images/imageFile102.png>)

s,s′=1

m

1 √αiαj

2 √αiαj

vi∗QvjI = 2δi,jI,

=

(vi)s(vj)s′2Qs,s′I =

![image 103](<2016-gribling-matrices-high-completely-positive_images/imageFile103.png>)

![image 104](<2016-gribling-matrices-high-completely-positive_images/imageFile104.png>)

![image 105](<2016-gribling-matrices-high-completely-positive_images/imageFile105.png>)

![image 106](<2016-gribling-matrices-high-completely-positive_images/imageFile106.png>)

s,s′=1

which means that we have the representation πA: C(r) → C A1,...,Ar deﬁned by πA(ai) = Ai, where the ai are the generators of C(r). In the same way we can deﬁne matrices B1,...,Br by taking linear combinations of the matrices Yt so that we obtain the representation πB : C(r) → C B1,...,Br deﬁned by πB(ai) = Bi.

By assumption, the algebras C X1,...,Xm and C Y1,...,Yn commute. This implies that the algebras C A1,...,Ar and C B1,...,Br also commute and that C A1,...,Ar C B1,...,Br is an algebra. Moreover, we have

[πA(a),πB(b)] = πA(a)πB(b) − πA(a)πB(b) = 0 for all a,b ∈ C(r). By the universal property of the tensor product of algebras (see, e.g., [16, Proposition II.4.1]), there exists a (unique) algebra homomorphism

π : C(r) ⊗ C(r) → C A1,...,Ar C B1,...,Br

such that π(a ⊗ 1) = πA(a) and π(1 ⊗ a) = πB(a) for all a ∈ C(r). Moreover, each ﬁnite dimensional, irreducible representation of a tensor product of algebras is the tensor product of two irreducible representations of those algebras (see, e.g., [10, Remark 2.27]). This means that each irreducible representation of C(r) ⊗ C(r) is the tensor product of two irreducible representations of C(r). Since irreducible representations of C(r) have size at least 2⌊r/2⌋, it follows that irreducible representations of the tensor product C(r) ⊗ C(r) must have size at least (2⌊r/2⌋)2. Since

π is a representation of C(r) ⊗ C(r), this means that the matrices Ai and Bj must have size at least (2⌊r/2⌋)2, which shows d ≥ (2⌊r/2⌋)2.

- Corollary 4.5. Let C be an extreme point of Cor(m,n) and let r = rank(C). The minimum local dimension of a tensor operator representation of C is 2⌊r/2⌋. Proof. The proof follows directly from Corollary 4.2 and Theorem 4.4.


5. Matrices with high completely positive semidefinite rank

In this section we prove our main result and construct completely positive semideﬁnite matrices with exponentially large cpsd-rank. In order to do so we are going to use an additional link between bipartite correlations and quantum correlations, combined with the fact that quantum correlations arise as projections of completely positive semideﬁnite matrices. We start with recalling the facts that we need about quantum correlations.

Let A, B, S, and T be ﬁnite sets. A function p: A × B × S × T → [0,1] is called a quantum correlation, realizable in local dimension d, if there exist a unit vector ψ ∈ Cd ⊗ Cd and Hermitian positive semideﬁnite d × d matrices Xsa (s ∈ S, a ∈ A) and Ytb (t ∈ T, b ∈ B) satisfying the following two conditions:

- (14)

a∈A

Xsa =

b∈B

Ytb = I for all s ∈ S,t ∈ T,

- (15) p(a,b|s,t) = ψ∗(Xsa ⊗ Ytb)ψ for all a ∈ A,b ∈ B,s ∈ S,t ∈ T.

The next theorem shows a link between quantum correlations and CS+-matrices. This result can be found in [26, Theorem 3.2] (see also [21]). This link allows us to construct CS+-matrices with large complex completely positive semideﬁnite rank by ﬁnding quantum correlations that cannot be realized in a small local dimension.

Theorem 5.1. A function p: A × B × S × T → [0,1] is a quantum correlation that can be realized in local dimension d if and only if there exists a completely positive semideﬁnite matrix M, with rows and columns indexed by the disjoint union (A × S) ⊔ (B × T), satisfying the following conditions:

- (16) cpsd-rankC(M) ≤ d,
- (17) M(a,s),(b,t) = p(a,b|s,t) for all a ∈ A,b ∈ B,s ∈ S,t ∈ T, and
- (18) a∈A,b∈B

M(a,s),(b,t) =

a,a′∈A

M(a,s),(a′,s′) =

b,b′∈B

M(b,t),(b′,t′) = 1

for all s,s′ ∈ S and t,t′ ∈ T.

Next we show how to construct from a bipartite correlation C ∈ Cor(m,n) a quantum correlation p, with |A| = |B| = 2 and S = [m], T = [n], having the property that the smallest local dimension in which p can be realized is lower bounded by the smallest local dimension of a tensor representation of C.

Lemma 5.2. Let C ∈ Cor(m,n) and assume C admits a tensor operator representation in local dimension d, but does not admit a tensor operator representation in smaller dimension. Then there exists a quantum correlation p deﬁned on {0,1} × {0,1} × [m] × [n], satisfying the relations

- (19) C(s,t) = p(0,0|s,t)+ p(1,1|s,t)− p(0,1|s,t)− p(1,0|s,t) for s ∈ [m],t ∈ [n], that can be realized in local dimension d, but cannot be realized in smaller dimension.


- Proof. We ﬁrst show the existence of a quantum correlation that satisﬁes (19). Let C ∈ Cor(m,n). By assumption there exists a unit vector ψ ∈ Cd ⊗ Cd, and Hermitian d × d matrices X1,...,Xm,Y1,...,Yn, whose spectra are contained in [−1,1], such that Cs,t = ψ∗(Xs ⊗ Yt)ψ for all s and t. We deﬁne the Hermitian positive semideﬁnite matrices
- (20) Xsa =


I + (−1)aXs 2

I + (−1)bYt 2

, Ytb =

for a,b ∈ {0,1}.

![image 107](<2016-gribling-matrices-high-completely-positive_images/imageFile107.png>)

![image 108](<2016-gribling-matrices-high-completely-positive_images/imageFile108.png>)

Using the fact that Xs0 + Xs1 = Yt0 + Yt1 = I, Xs = Xs0 − Xs1, and Yt = Yt0 − Yt1, it follows that the function p(a,b|s,t) = ψ∗(Xsa ⊗ Ytb)ψ is a quantum correlation that can be realized in local dimension d and satisﬁes (19).

Assume that p can be realized in dimension k, we show that k ≥ d. As p is realizable in dimension k there exist a unit vector ψ˜ ∈ Ck ⊗ Ck and Hermitian positive semideﬁnite k × k matrices {X˜sa} and {Y˜tb} such that

Y˜tb = I for all s ∈ S,t ∈ T,

X˜sa =

b∈{0,1}

a∈{0,1}

for which we have p(a,b|s,t) = ψ˜∗(X˜sa ⊗ Y˜tb)ψ˜. Observe that the spectrum of the operators X˜sa and Y˜tb is contained in [0,1]. We deﬁne X˜s = X˜s0−X˜s1,Y˜t = Y˜t0−Y˜t1. Then, using (19), we can conclude

Cs,t = ψ˜∗(X˜s ⊗ Y˜t)ψ.˜ This means that C has a tensor operator representation in local dimension k and thus, by the assumption of the lemma, k ≥ d.

We can now prove our main theorem: Theorem 1.1. For each positive integer k, there exists a completely positive semideﬁnite matrix M of size 4k2 + 2k + 2 with cpsd-rankC(M) = 2k.

Proof. Let k be a positive integer, let r = 2k, and set n = r2 + 1. By Theorem 3.11(i) there exists an extreme point C of Cor(r,n) with rank(C) = r. Corol-

lary 4.5 tells us there exists a tensor operator representation of C using local dimension d = 2⌊r/2⌋ = 2k, and that there does not exist a smaller tensor operator representation. Then, by Lemma 5.2, there exists a quantum correlation p: {0,1} × {0,1} × [r] × [n] → [0,1] that can be realized in local dimension d and not in smaller dimension. Let M be a completely positive semideﬁnite matrix constructed from p as indicated in Theorem 5.1, so that cpsd-rankC(M) = d and the size of M is 2r + 2n = r2 + r + 2 = 4k2 + 2k + 2.

We note that by using Theorem 3.11(ii) we would get a matrix with the same completely positive semideﬁnite rank 2k, but with larger size 4k2+6k+2. Likewise, the result of [15] combined with Theorem 5.1 also leads to a matrix with the same completely positive semideﬁnite rank, but with larger size (148k2 − 58k). It is an open problem to ﬁnd a family of completely positive semideﬁnite matrices where the ratio of the completely positive semideﬁnite rank to the matrix size is larger than in the above theorem. It is not possible to obtain such an improved family by the above method. Indeed, if M is a completely positive semideﬁnite matrix with cpsd-rankC(M) = 2k, constructed from an extreme bipartite correlation matrix C ∈ Cor(m,n) as in the above theorem, then the size 2m + 2n of M is at least 4k2 +2k+2. To see this, note that, by Corollary 4.5 and the results in this section, C has to have rank 2k. Then, by Tsirelson’s bound, m + n − 1 ≥ 2k2+1 and therefore 2m + 2n ≥ 4k2 + 2k + 2.

Acknowledgements. We are grateful to an anonymous referee for his/her careful reading and helpful comments, and for bringing the works [15, 27] to our attention.

References

- [1] A. Berman and N. Shaked-Monderer. Completely Positive Matrices. World Scientiﬁc Publishing, 2003.
- [2] J. Bri¨et. Grothendieck Inequalities, Nonlocal Games and Optimization. PhD Thesis, 2011.
- [3] I.M. Bomze, W. Schachinger, and R. Ullrich. From seven to eleven: completely positive matrices with high cp-rank. Linear Algebra and its Applications, 459:208–221, 2014.
- [4] I.M. Bomze, W. Schachinger, and R. Ullrich. New lower bounds and asymptotics for the cp-rank. SIAM Journal on Matrix Analysis and Applications, 36(1):20–37, 2015.
- [5] S. Burgdorf, M. Laurent, and T. Piovesan. On the closure of the completely positive semidefinite cone and linear approximations to quantum colorings. In S. Beigi and R. Koenig (Eds.), Proceedings of the 10th Conference on the Theory of Quantum Computation, Communication and Cryptography (TQC 2015) (pp. 127–146). Leibniz: Schloss Dagstuhl-Leibniz-Zentrum fuer Informatik. (Leibniz International Proceedings in Informatics, 44), 2015.
- [6] R. Cleve, P. Hoyer, B. Toner, and J. Watrous. Consequences and limits of nonlocal strategies. Proceedings of the 19th Annual IEEE Conference on Computational Complexity (CCC 2004), 236–249.
- [7] R. Connelly and S.J. Gortler. Universal rigidity of complete bipartite graphs. Preprint, arXiv:1502.02278, 2015.
- [8] J.H. Drew, C.R. Johnson, and R. Loewy. Completely positive matrices associated with Mmatrices. Linear and Multilinear Algebra, 37:303–31, 1994.
- [9] M. E.-Nagy, M. Laurent, and A. Varvitsiotis. Forbidden minor characterizations for lowrank optimal solutions to semideﬁnite programs over the elliptope. Journal of Combinatorial Theory B, 108:40–80, 2014.
- [10] P. Etingof, O. Golberg, S. Hensel, T. Liu, A. Schwendner, D. Vaintrob, and E. Yudovina. Introduction to representation theory. Lecture notes, 2011.
- [11] H. Fawzi, J. Gouveia, P.A. Parrilo, R.Z. Robinson, and R.R. Thomas. Positive semideﬁnite rank. Math. Program. Ser. B, 153(1):133–177, 2015.
- [12] P.E. Frenkel and M. Weiner. On vector conﬁgurations that can be realized in the cone of positive semideﬁnite matrices. Linear Algebra and its Applications, 459:465–474, 2014.
- [13] J. Gouveia, R.R. Thomas, and P. Parrilo. Lifts of convex sets and cone factorizations. Mathematics of Operations Research, 38:248–264, 2013.
- [14] R. Grone and S. Pierce. Extremal bipartite matrices. Linear Algebra and its Applications, 131:39–50, 1990.
- [15] Z. Ji. Binary constraint system games and locally commutative reductions. Preprint, arXiv:1310:3794, 2013.
- [16] C. Kassel. Quantum Groups. Graduate texts in mathematics, Springer-Verlag, 1995.
- [17] E. de Klerk and D.V. Pasechnik. Approximation of the stability number of a graph via copositive programming. SIAM Journal on Optimization, 12:875–892, 2002.
- [18] M. Laurent and T. Piovesan. Conic approach to quantum graph parameters using linear optimization over the completely positive semideﬁnite cone. SIAM Journal on Optimization, 25(4):2461–2493, 2015.
- [19] M. Laurent and A. Varvitsiotis. Positive semideﬁnite matrix completion, universal rigidity and the Strong Arnold Property. Linear Algebra and its Applications, 452(1):292–317, 2014.
- [20] C.-K. Li and B.S. Tam. A Note on Extreme Correlation Matrices. SIAM Journal on Matrix Analysis and Applications, 15(3):903–908, 1995.
- [21] L. Manˇcinska and D.E. Roberson. Note on the correspondence between quantum correlations and the completely positive semideﬁnite cone, 2014.
- [22] A. Prakash, J. Sikora, A. Varvitsiotis, and Z. Wei. Completely positive semideﬁnite rank. arXiv:1604.07199, 2016.
- [23] C. Procesi. Lie groups - An approach through Invariants and Representations. Springer, 2007.
- [24] D.E. Roberson. Conic formulations of graph homomorphisms. Journal of Algebraic Combinatorics, 43(4):877–913, 2016.
- [25] N. Shaked-Monderer, A. Berman, I.M. Bomze, F. Jarre, and W. Schachinger. New results on the cp-rank and related properties of co(mpletely) positive matrices. Linear and Multilinear Algebra, 63(2):384–396, 2015.
- [26] J. Sikora and A. Varvitsiotis, Linear conic formulations for two-party correlations and values of nonlocal games. Math. Program. (2016).
- [27] W. Slofstra. Lower bounds on the entanglement needed to play XOR non-local games. Journal of Mathematical Physics, 52, 102202, 2011.
- [28] B.S. Tsirel’son. Quantum analogues of the Bell inequalities. The case of two spatially separated domains. Journal of Soviet Mathematics, 36(4):557–570, 1987.


- [29] B.S. Tsirel’son. Some results and problems on quantum Bell-type inequalities. Hadronic Journal Supplement, 8(4):329–345, 1993.
- [30] T. V´ertesi and K.F. P´al. Bounding the dimension of bipartite quantum systems. Physical Review A, 79, 2009.
- [31] R.F. Werner and M.M. Wolf. Bell inequalities and entanglement. Quantum Information & Computation, 1(3):1–25, 2001.
- [32] M. Yannakakis. Expressing combinatorial optimization problems by linear programs. Journal of Computer and System Sciences, 43(3):441–466, 1991.


