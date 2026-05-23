---
type: source
kind: paper
title: Semidefinite programming, multivariate orthogonal polynomials, and codes in spherical caps
authors: Christine Bachoc, Frank Vallentin
year: 2006
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/math/0610856v2
source_local: ../raw/2006-bachoc-semidefinite-programming-multivariate-orthogonal.pdf
topic: general-knowledge
cites:
---

arXiv:math/0610856v2[math.MG]18Oct2007

# SEMIDEFINITE PROGRAMMING, MULTIVARIATE ORTHOGONAL POLYNOMIALS, AND CODES IN SPHERICAL CAPS

CHRISTINE BACHOC AND FRANK VALLENTIN

ABSTRACT. In this paper we apply the semideﬁnite programming approach developed in [2] to obtain new upper bounds for codes in spherical caps. We compute new upper bounds for the one-sided kissing number in several dimensions where we in particular get a new tight bound in dimension 8. Furthermore we show how to use the SDP framework to get analytic bounds.

Dedicated to Eiichi Bannai in occasion of his 60th birthday

1. INTRODUCTION

Let Sn−1 denote the unit sphere of the Euclidean space Rn. The spherical cap with center e ∈ Sn−1 and angular radius φ is the set

Cap(e,φ) = {x ∈ Sn−1 : e · x ≥ cos φ}.

We consider the problem of ﬁnding upper bounds of the size of a code C contained in Cap(e,φ) with minimal angular distance θ. Following notations of [3], the maximal size of such a code is denoted by A(n,θ,φ). Many reasons to consider this problem are exposed in [3], e.g. upper bounds for spherical codes can be derived from upper bounds for spherical cap codes through the following inequality:

A(n,θ,φ) vol(Cap(e,φ))

A(n,θ) vol(Sn−1)

≤

![image 1](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile1.png>)

![image 2](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile2.png>)

where A(n,θ) stands as usual for the maximal size of a spherical code with minimal angular distance θ.

Moreover, it is a challenging problem, because the so-called linear programming method does not apply to this situation. In coding theory many of the best upper bounds are consequences of the so-called linear programming method due to P. Delsarte. This method gives upper bounds for codes from the solution of a certain linear program. It can be applied to symmetric spaces and has been successfully used to deal with two-point homogeneous spaces like the unit sphere Sn−1 ([8], [9], [11] and the survey [7, Chapter 9]), or with symmetric spaces which are

![image 3](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile3.png>)

Date: October 16, 2007. 1991 Mathematics Subject Classiﬁcation. 52C17, 90C22. Key words and phrases. spherical codes, spherical caps, one-sided kissing number, semideﬁnite

programming, orthogonal polynomials.

The second author was supported by the Netherlands Organization for Scientiﬁc Research under grant NWO 639.032.203 and by the Deutsche Forschungsgemeinschaft (DFG) under grant SCHU 1503/4.

1

not two-point homogeneous like Grassmannian spaces ([1]). However the method is not applicable to spaces which are not symmetric spaces like spherical caps.

In this paper, we show that the approach developed in [2] based on semideﬁnite programming can be applied to the above problem. It turns out that it gives good numerical results. In particular we obtain improvements in the determination of the so-called one-sided kissing number, corresponding to φ = π/2 and θ = π/3, and denoted by B(n) after [14].

Let us describe brieﬂy the idea underlying our approach. The isometry group of Cap(e,φ) is the group H := Stab(O(Rn),e) stabilizing the point e in O(Rn). This group acts on the space Pol≤d(Sn−1) of polynomial functions on the unit sphere of degree at most d. In the decomposition of this space into irreducible subspaces some irreducible subspaces occur with multiplicities. To each irreducible subspace with multiplicity m we can associate an m × m matrix Y whose coefﬁcients are real polynomials in three variables (u,v,t) and have an explicit expression in terms of Gegenbauer polynomials. Each matrix Y satisﬁes the positivity property:

For all ﬁnite C ⊂ Sn−1,

Y (e · c,e · c′,c · c′) 0,

(c,c′)∈C2

where “ 0” stands for “is positive semideﬁnite”.

We want to point out that one can consider other metric spaces X with isometry group in this framework. Only the expression of the matrices Y will depend on the speciﬁc situation. For a symmetric space X the multiplicities in the irreducible decomposition are equal to 1. Hence the matrices Y have size 1×1. So we recover the classical positivity property of zonal polynomials which underlies the linear programming method.

The paper is organized as follows: Section 2 recalls the needed notations and results of [2]. Section 3 states the semideﬁnite program (SDP for short) which obtains an upper bound for A(n,θ,φ) and presents numerical results. Section 4 translates the dual SDP into a statement on three variable polynomials, and contains more material on orthogonality relations, positivity property and other classical material which might be of independent interest.

2. REVIEW ON THE SEMIDEFINITE ZONAL MATRICES

We start with some notations. The standard inner product of the Euclidean space Rn is denoted by x · y. The orthogonal group O(Rn) acts homogeneously on the unit sphere

Sn−1 := {x ∈ Rn : x · x = 1}. The space of real polynomial functions on Sn−1 of degree at most d is denoted by Pol≤d(Sn−1). It is endowed with the induced action of O(Rn), and equipped with the standard O(Rn)-invariant inner product

1 ωn Sn−1

- (1) (f,g) =


f(x)g(x)dωn(x),

![image 4](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile4.png>)

where ωn is the surface area of Sn−1 for the standard measure dωn. It is a classical result that under the action of O(Rn)

- (2) Pol≤d(Sn−1) = H0n ⊥ H1n ⊥ ... ⊥ Hdn,

where Hkn is isomorphic to the O(Rn)-irreducible space of homogeneous, harmonic polynomials of degree k in n variables, denoted by Harmnk. For the dimension of these spaces we write hnk := dim(Harmnk).

For the restricted action of the subgroup H := Stab(e,O(Rn)), introduced above, we have the following decomposition into isotypic components:

- (3) Pol≤d(Sn−1) = I0 ⊥ I1 ⊥ ... ⊥ Id, where

Ik ≃ (d − k + 1)Harmkn−1, k = 0,... ,d. More precisely, Ik decomposes as

- (4) Ik = Hk,kn−1 ⊥ ... ⊥ Hk,dn−1,

where, for i ≥ k, Hk,in−1 is the unique subspace of Hin isomorphic to Harmkn−1. The following construction associates to each Ik a matrix-valued function

- (5) Zkn : Sn−1 × Sn−1 → R(d−k+1)×(d−k+1)

which is uniquely deﬁned up to congruence. Let (eks,1,eks,2,... ,eks,hn−1

k

) be an orthonormal basis of Hk,kn−+1s. We assume that the basis (eks,i)1≤i≤hn−1

k

is the image of (ek0,i)1≤i≤hn−1

k

by some H-isomorphism φs : Hk,kn−1 → Hk,kn−+1s. Then, deﬁne

Ekn(x) :=

1 hkn−1

![image 5](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile5.png>)

![image 6](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile6.png>)

  

ek0,1(x) ... ek0,hn−1

k

(x)

. . ekd−k,1(x) ... ekd−k,hn−1

k

(x)

  ,

and

- (6) Zkn(x,y) := Ekn(x)Ekn(y)t ∈ R(d−k+1)×(d−k+1).

One can prove that, for all g ∈ H, Zkn(g(x),g(y)) = Zkn(x,y). As a consequence, the coefﬁcients of Zkn can be expressed as polynomials in the three variables u = e · x, v = e · y, t = x · y. More precisely, let Ykn(u,v,t) be the (d − k + 1) × (d − k + 1) matrix such that

- (7) Zkn(x,y) = Ykn(e · x,e · y,x · y).


We denote the zonal polynomials of the unit sphere Sn−1 by Pkn. In other words, if n ≥ 3, then Pkn(t) is the Gegenbauer polynomial of degree k with parameter n/2 − 1, normalized by the condition Pkn(1) = 1. If n = 2, then Pkn(t) is the Chebyshev polynomial of the ﬁrst kind with degree k. We give in [2, Theorem 3.2] the following explicit expressions for the coefﬁcients of the matrices Ykn:

- Theorem 2.1. We have, for all 0 ≤ i,j ≤ d − k,

(8) Ykn i,j(u,v,t) = λi,jPin+2k(u)Pjn+2k(v)Qkn−1(u,v,t), where

Qkn−1(u,v,t) := (1 − u2)(1 − v2) k/2Pkn−1

t − uv (1 − u2)(1 − v2)

![image 7](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile7.png>)

![image 8](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile8.png>)

,

and

λi,j =

ωn ωn−1

![image 9](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile9.png>)

ωn+2k−1 ωn+2k

![image 10](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile10.png>)

(hin+2khjn+2k)1/2.

We recall the matrix-type positivity property of the matrices Ykn which underlies the semideﬁnite programming method:

- Theorem 2.2. For any ﬁnite code C ⊂ Sn−1,


- (9)


Ykn(e · c,e · c′,c · c′) 0.

(c,c′)∈C2

Proof. We recall the straightforward argument:

Zkn(c,c′) =

(c,c′)∈C2

Ekn(c)

c∈C

Ekn(c)

c∈C

t

0.

- 3. SEMIDEFINITE PROGRAMMING BOUND FOR CODES IN SPHERICAL CAPS


Let C ⊂ Cap(e,φ) be a code of minimal angular distance θ. Deﬁne the domains ∆ and ∆0 by

∆ := {(u,v,t) : cos φ ≤ u ≤ v ≤ 1, −1 ≤ t ≤ cos θ, 1 + 2uvt − u2 − v2 − t2 ≥ 0},

and

∆0 := {(u,u,1) : cos φ ≤ u ≤ 1}. The two-point distance distribution of C is the map y : ∆ ∪ ∆0 → R given by

m(u,v) card(C)

card{(c,c′) ∈ C2 : e · c = u,e · c′ = v,c · c′ = t}, where

y(u,v,t) =

![image 11](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile11.png>)

2 if u = v, 1 if u = v.

m(u,v) =

We introduce the symmetric matrices Y nk(u,v,t) deﬁned by Y nk(u,v,t) :=

![image 12](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile12.png>)

- 1

![image 13](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile13.png>)

- 2


Ykn(u,v,t) + Ykn(v,u,t) .

![image 14](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile14.png>)

Then, (9) is equivalent to the semideﬁnite condition

y(u,v,t)Y nk(u,v,t) 0.

![image 15](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile15.png>)

(u,v,t)∈∆∪∆0

For any d ≥ 0, the y(u,v,t)’s satisfy the following obvious properties: y(u,v,t) ≥ 0 for all (u,v,t) ∈ ∆ ∪ ∆0, y(u,v,t) = 0 for all but ﬁnitely many (u,v,t) ∈ ∆ ∪ ∆0,

- (u,u,1)∈∆0

- y(u,u,1) = 1,

(u,v,t)∈∆∪∆0

- y(u,v,t) = card(C),




y(u,v,t)Y nk(u,v,t) 0 for k = 0,... d.

![image 16](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile16.png>)

(u,v,t)∈∆∪∆0

Hence a solution to the following semideﬁnite program is an upper bound for A(n,θ,φ).

max 1 +

y(u,v,t) :

(u,v,t)∈∆

y(u,v,t) ≥ 0 for all (u,v,t) ∈ ∆ ∪ ∆0, y(u,v,t) = 0 for all but ﬁnitely many (u,v,t) ∈ ∆ ∪ ∆0,

- (u,u,1)∈∆0

- y(u,u,1) = 1,

(u,v,t)∈∆∪∆0

- y(u,v,t)Y nk(u,v,t) 0 for all k = 0,... ,d .




![image 17](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile17.png>)

As usual, the dual problem is easier to handle. The duality theorem says that any feasible solution of the dual problem provides an upper bound for A(n,θ,φ). For expressing the dual problem we use the standard notation A,B = Trace(ABt).

- Theorem 3.1. Any feasible solution to the following semideﬁnite problem provides an upper bound on A(n,θ,φ).


- (10)


min 1 + M : Fk 0 for all k = 0,... ,d,

d

Fk,Y nk(u,u,1) ≤ M for all (u,u,1) ∈ ∆0, d

![image 18](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile18.png>)

k=0

Fk,Y nk(u,v,t) ≤ −1 for all (u,v,t) ∈ ∆

![image 19](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile19.png>)

k=0

In order to make use of this theorem in computations we follow the same line as in [2, Section 5]. A theorem of M. Putinar ([17]) shows that the two last conditions

best lower best upper bound SDP n bound known previously known method

![image 20](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile20.png>)

![image 21](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile21.png>)

![image 22](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile22.png>)

![image 23](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile23.png>)

![image 24](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile24.png>)

![image 25](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile25.png>)

- 3 9 9 [10] 9

![image 26](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile26.png>)

![image 27](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile27.png>)

![image 28](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile28.png>)

- 4 18 18 [14] 18

![image 29](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile29.png>)

![image 30](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile30.png>)

![image 31](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile31.png>)

- 5 32 35 [15] 33

![image 32](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile32.png>)

![image 33](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile33.png>)

![image 34](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile34.png>)

- 6 51 64 [15] 61

![image 35](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile35.png>)

![image 36](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile36.png>)

![image 37](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile37.png>)

- 7 93 110 [15] 105

![image 38](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile38.png>)

![image 39](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile39.png>)

![image 40](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile40.png>)

- 8 183 186 [15] 183

![image 41](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile41.png>)

![image 42](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile42.png>)

![image 43](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile43.png>)

- 9 309 [15] 297

![image 44](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile44.png>)

![image 45](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile45.png>)

![image 46](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile46.png>)

- 10 472 Table 1. Bounds on B(n).


![image 47](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile47.png>)

![image 48](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile48.png>)

![image 49](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile49.png>)

![image 50](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile50.png>)

can be replaced by:

d

Fk,Y nk(u,u,1) = M − q0(u) − p(u)q1(u) d

![image 51](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile51.png>)

k=0

4

Fk,Y nk(u,v,t) = −1 − r0(u,v,t) −

![image 52](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile52.png>)

pi(u,v,t)ri(u,v,t)

i=1

k=0

where p(u) = −(u−cos φ)(u−1), p1 = p(u), p2 = p(v), p3 = −(t+1)(t−cos θ), p4 = −(u2 + v2 + t2) + 2uvt + 1, and the polynomials qi(u), 0 ≤ i ≤ 1 and ri(u,v,t), 0 ≤ i ≤ 4 are sums of squares of polynomials. If we set the degree of those polynomials to be less than a given value N, and ﬁx the parameter d, we relax (10) to a ﬁnite semideﬁnite program.

In the most interesting case cos φ = 0 and cos θ = 1/2, corresponding to the socalled one-sided kissing number B(n), we obtain the computational results given in Table 1. For our computations we chose the parameter d = N = 10.

In this table, the values in the column of the best lower bounds known correspond to the number of points in an hemisphere from the best known kissing conﬁgurations, given by the root systems D3, D4, D5, E6, E7, E8.

Our method gives a tight upper bound in three cases. In dimension 3 we get with parameters d = N = 4 the bound B(3) ≤ 9.6685 and hence we recover the exact values B(3) = 9 ﬁrst proved by G. Fejes To´th ([10]). In dimension 4 we get with parameters d = N = 6 the bound B(4) ≤ 18.5085 and hence we recover the exact value B(4) = 18 ﬁrst proved by O.R. Musin ([14]). In dimension 8 we ﬁnd a new tight upper bound. The famous conﬁguration of 240 points of S7 given by the root system E8 is well known to be an optimal spherical code of minimal angular distance π/3, which is moreover unique up to isometry. Optimality is due to A.M. Odlyzko and N.J.A. Sloane ([16]), and independently to V.I. Levenshtein ([13]), uniqueness is due to E. Bannai and N.J.A. Sloane ([6]). From these 240 points we get a code of the hemisphere as follows: Take e among these points, then the subset of those points lying in the hemisphere with center e consists in 183 points. We obtain a bound of 183.012 with d = N = 8 in our computation. Hence, it proves

that it is a maximal code of the hemisphere, in other words that B(8) = 183.

It is reasonable to believe that the conﬁguration of 183 points of E8 is unique up to isometry. Unfortunately we were not able to prove it.

4. POLYNOMIALS

- 4.1. Polynomial restatement of the SDP bound for codes in spherical caps. We want to give an equivalent expression of the bound provided by Theorem 3.1 in terms of polynomials. Such an expression will be useful to prove analytic bounds without the use of software for solving semideﬁnite programs, just like in the case of the linear programming (LP) bound (see e.g. [16]). Moreover, we aim at setting bounds in the form of explicit functions of cosθ and cos φ. We start with a lemma which shows that any polynomial in the variables u,v,t can be expressed in terms


of the matrix coefﬁcients of the Ykn(u,v,t). In our situation it sufﬁces to restrict to polynomials which are symmetric in u,v. We introduce the following notation:

Rd := {F ∈ R[u,v,t] : F(u,v,t) = F(v,u,t),deg(u,t)(F) ≤ d,degt(F) ≤ d}, where deg(u,t) stands for the total degree in the variables u,t.

Lemma 4.1. Let F(u,v,t) ∈ Rd. There exists a unique sequence of d + 1 real symmetric matrices (F0,F1,... ,Fd) such that Fk is a (d − k + 1) × (d − k + 1) matrix and

d

Fk,Y nk(u,v,t) . We shall say that (F0,... ,Fd) are the matrix coefﬁcients of F. Proof. The polynomials Qkn−1(u,v,t) have degree k in the variable t. Hence, F(u,v,t) has a unique expression of the form

- (11) F(u,v,t) =


![image 53](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile53.png>)

k=0

d

qk(u,v)Qkn−1(u,v,t),

F(u,v,t) =

k=0

where qk(u,v) is symmetric in u,v and has degree in u at most d − k. Since Pin+2k(u) has degree i, qk has a unique expression as a linear combination of the products λi,jPin+2k(u)Pjn+2k(v) for 0 ≤ i,j ≤ d − k. Thus, there is a symmetric (d − k + 1) × (d − k + 1) matrix Fk so that

(Fk)i,jλi,jPin+2k(u)Pjn+2k(v).

qk(u,v) =

0≤i,j≤d−k

Since one can write Yk(u,v,t) as Qkn−1(u,v,t)(λi,jPin+2k(u)Pjn+2k(v)) we obtain decomposition (11).

- Remark 4.2. The matrix coefﬁcients of a polynomial F do only trivially depend on the choice of d. The matrix coefﬁcients associated to d′ ≥ d will simply be the ones associated to d, enlarged by sufﬁciently many rows and columns of zeros.


- Remark 4.3. From [2, Proposition 3.5], the polynomials Pkn(t) are linear combi-


nations of diagonal elements of the matrices Y nk with non negative coefﬁcients. As a consequence, the matrix coefﬁcients of any polynomial P(t) ∈ R[t], are diagonal

![image 54](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile54.png>)

matrices. If P(t) = fkPkn(t), with all fk ≥ 0, then the matrix coefﬁcients Fk of P are also non negative, and, moreover, the top left corner of F0 equals f0.

The following reformulation of Theorem 3.1 is an analogue of the classical expression of the linear programming bound (see e.g. [7, Chapter 9, Theorem 4]).

Theorem 4.4. Let E0 be the matrix whose only non zero entry is the top left corner which contains 1. For a polynomial F(u,v,t) ∈ Rd let (F0,... ,Fd) be symmetric matrices such that

d

Fk,Y nk(u,v,t) . Suppose the following conditions hold:

![image 55](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile55.png>)

F(u,v,t) =

k=0

- (a) Fk 0 for all 0 ≤ k ≤ d.
- (b) F0 − f0E0 0 for some f0 > 0.
- (c) F(u,v,t) ≤ 0 for all (u,v,t) ∈ ∆.
- (d) F(u,u,1) ≤ B for all u ∈ [cos φ,1].


Then, for any code C in Cap(e,φ) with minimal angular distance at least θ, card(C) ≤

B f0

.

![image 56](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile56.png>)

Proof. The statement follows immediately from Theorem 3.1 because the matrices G0 = F0/f0 − E0 and Gk = Fk/f0 for 1 ≤ k ≤ d are a feasible solution to the SDP (10) with M = B/f0 − 1.

We also give a direct proof, which has the additional feature to give information about the case when the obtained bound coincides with the size of a certain code. Let

F(e · c,e · c′,c · c′).

S :=

(c,c′)∈C2

We expand F in the Y nk’s:

![image 57](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile57.png>)

d

Y nk(e · c,e · c′,c · c′) .

![image 58](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile58.png>)

S =

Fk,

k=0

(c,c′)∈C2

On one hand, from the positivity property (9) together with the fact that A,B ≥ 0 for any two positive semideﬁnite matrices A,B we obtain

- (12)


Y n0(e · c,e · c′,c · c′)

![image 59](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile59.png>)

S ≥ f0E0,

(c,c′)∈C2

Y n0 0,0(e · c,e · c′,c · c′) = f0 card(C)2.

![image 60](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile60.png>)

= f0

(c,c′)∈C2

On the other hand, if we split the sum S into diagonal terms belonging to pairs (c,c) and into cross terms belonging to pairs (c,c′) with c = c′, we obtain from condition (c) and (d)

- (13)


F(e · c,e · c,1) + (c,c′)∈C2,c =c′ F(e · c,e · c′,c · c′) ≤ B card(C) + 0,

S =

c∈C

because (e · c,e · c,1) ∈ ∆0 and (e · c,e · c′,c · c′) ∈ ∆ if c = c′. Now (12) and

- (13) together give the inequality card(C) ≤ B/f0.


- Remark 4.5. Like in the LP method, the above proof gives additional information on the case of equality. Namely, if for a given code C and a given polynomial F, we

have card(C) = B/f0, the inequality (13) must be an equality. So, F(u,v,t) = 0 for all (u,v,t) running through the set of triples (e · c,e · c′,c · c′) with c = c′ and (c,c′) ∈ C2, and F(u,u,1) = B for all u = e · c with c ∈ C.

- Remark 4.6. In view of explicit computations, it is more convenient to remove the


factor λi,j from the coefﬁcients of Ykn, so that polynomials with rational coefﬁcients have rational matrix coefﬁcients. It changes the above deﬁned Fk to congruence, hence does not affect the property to be positive semideﬁnite. These are the matrix coefﬁcients we discuss about in the next two examples.

- Example 1. (d = 1) We consider the polynomial F = t − cos θ − uv + cos2 φ. The matrices of the


decomposition (11) are: F0 = ( a0 00) with a = cos2φ − cos θ and F1 = ( 1). Condition (a) of Theorem 4.4 is fulﬁlled if a ≥ 0. Condition (b) holds for f0 = a. Obviously (c) holds if cos φ ≥ 0 and B = 1 − cos θ because F(u,u,1) = 1 − cosθ − u2 + cos2 φ. We obtain:

1 − cos θ cos2 φ − cosθ

If cosφ ≥ 0 and cos θ < cos2 φ, then A(n,θ,φ) ≤

. It is worth to point out that the polynomial G = (t − cos θ) − cos φ(u + v −

![image 61](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile61.png>)

2cos φ) leads to exactly the same bound. This time F0 = c−+ca −1c with c = cos φ, f0 = a, B = 1 − cosθ.

The above bound is already proved in [3, Theorem 5.2]. Indeed with the notations of [3], let w(θ,φ) be deﬁned by cos w(θ,φ) = (cos θ − cos2 φ)/(sin2 φ); we have just proved that the Rankin bound for A(n − 1,w(θ,φ)) is also a bound for A(n,θ,φ). More generally, LP bounds for A(n − 1,w(θ,φ)) are also bounds for A(n,θ,φ): Let f(x) be a polynomial of degree d that realizes an LP bound on Sn−2 for the angle w(θ,φ). We can take polynomial approximations of the function

t − uv (1 − u2)(1 − v2) 1/2

F(u,v,t) = (1 − u2)(1 − v2) d/2f

![image 62](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile62.png>)

obtained by the truncated developments of the powers (1−u2)(1−v2) k/2 around u = cos φ, v = cos φ.

- Example 2. (d = 2) We consider the polynomial F = (t+1)(t−cosθ)+a (u−cosφ)(u−1)+(v − cosφ)(v − 1) . The parameter a > 0 will be chosen later to optimize the bound. Condition (c) is obviously fulﬁlled and condition (d) holds with B = 2(1 −cos θ). The polynomial (t + 1)(t − cos θ) has non negative coefﬁcients if we expand it in terms of the basis Pkn(t) whenever cos θ ≤ 1/n. More precisely its constant


coefﬁcient equals n 1 − cos θ while the two others are positive. So we only need to make sure that F0 is positive semideﬁnite. We ﬁnd that:

![image 63](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile63.png>)

2a(n1 + cos φ) + n1 − cos θ −a(1 + cosφ) a(1 − n1) −a(1 + cos φ) (1 − cos θ) 0

F0 = 

 .

![image 64](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile64.png>)

![image 65](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile65.png>)

![image 66](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile66.png>)



a(1 − n1) 0 (1 − n1)

![image 67](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile67.png>)

![image 68](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile68.png>)

Let

(1 + cos φ)2 1 − cos θ

1 n

1 n

1 n

f0(a) := −a2

+ (1 −

) + 2a

+ cos φ +

− cos θ.

![image 69](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile69.png>)

![image 70](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile70.png>)

![image 71](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile71.png>)

![image 72](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile72.png>)

Then, an easy calculation shows that F0 0 iff f0(a) ≥ 0, and that F0−f0E0 0 iff f0 ≤ f0(a). The best bound is obtained when f0 = f0(a) attains the maximal value

1 n + cos φ 2

1 n

![image 73](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile73.png>)

.

(f0)max =

− cos θ +

![image 74](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile74.png>)

![image 75](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile75.png>)

(1+cos φ)2

1−cosθ + 1 − n1

![image 76](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile76.png>)

![image 77](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile77.png>)

The ﬁnal bound equals

2(1 − cos θ) (f0)max

.

![image 78](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile78.png>)

and is valid as long as (f0)max > 0 and n 1 + cos φ > 0 (this last condition holds because (f0)max must be attained at a positive a).

![image 79](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile79.png>)

It is worth noticing that the resulting bound is smaller than the LP bound for the entire sphere A(n,θ), obtained from the polynomial (t + 1)(t − cos θ), which is 2(1 − cos θ)

.

![image 80](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile80.png>)

1 n − cos θ

![image 81](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile81.png>)

For example, when cos φ = cos θ = 0, we recover the exact bound of 2n − 1 (see also [12]).

- Remark 4.7. We can interpret the two examples treated above as follows: in both cases, we have perturbed the optimal polynomial for the LP method, respectively t−cos θ and (t+1)(t−cos θ), by a polynomial in the variables u,v, which affects


the ﬁrst matrix coefﬁcient F0 and increases the value of the constant coefﬁcient f0. However it seems difﬁcult to generalize this approach.

- 4.2. Orthogonality relations. In this subsection, we calculate the scalar product induced on R[u,v,t] by the natural scalar product on Pol(Sn−1) deﬁned by (1).


Proposition 4.8. Let P ∈ R[u,v,t] be a polynomial. We have

1 ωn2 (Sn−1)2

P(u,v,t)k(u,v,t)dudvdt

P(e · x,e · y,x · y)dωn(x)dωn(y) =

![image 82](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile82.png>)

Ω

where

ωn−1ωn−2 ωn2

(1 − u2 − v2 − t2 + 2uvt)n−24 and

k(u,v,t) =

![image 83](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile83.png>)

![image 84](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile84.png>)

Ω = {(u,v,t) : −1 ≤ u,v,t ≤ 1, 1 + 2uvt − u2 − v2 − t2 ≥ 0}.

Proof. If u = e · x and ζ ∈ Sn−2 is deﬁned by x = ue + (1 − u2)12ζ, we have

![image 85](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile85.png>)

dωn(x) = (1 − u2)n−23dudωn−1(ζ). With y = ve + (1 − v2)12ξ, we have

![image 86](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile86.png>)

![image 87](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile87.png>)

P(e · x,e · y,x · y)dωn(x)

Sn−1

1

- 1

![image 88](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile88.png>)

- 2ζ · ξ)(1 − u2)n−23dudωn−1(ζ)


P(u,v,uv + (1 − u2)(1 − v2)

=

![image 89](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile89.png>)

Sn−2

−1

1

1

P(u,v,t)(1 − α2)n−24(1 − u2)n−23dαdu,

= ωn−2

![image 90](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile90.png>)

![image 91](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile91.png>)

−1

−1

- 1

![image 92](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile92.png>)

- 2α. With this change of variables having


where t := uv + (1 − u2)(1 − v2) Jacobian (1 − u2)(1 − v2)

- 1

![image 93](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile93.png>)

- 2 we obtain


P(e · x,e · y,x · y)dωn(x)

Sn−1

P(u,v,t)(1 − u2 − v2 − t2 + 2uvt)n−24 (1 − v2)−n−23dudt, where

= ωn−2

![image 94](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile94.png>)

![image 95](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile95.png>)

Ω(v)

Ω(v) = {(u,t) : −1 ≤ u,t ≤ 1,

1 + 2uvt − u2 − v2 − t2 ≥ 0}. Hence

P(e · x,e · y,x · y)dωn(x)dωn(y)

(Sn−1)2

= ωn−1ωn−2

P(u,v,t)(1 − u2 − v2 − t2 + 2uvt)n−24 dudvdt

![image 96](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile96.png>)

Ω

Deﬁnition 4.9. With the notations of Proposition 4.8, the following expression deﬁnes a scalar product on R[u,v,t]:

- (14) [F,G] = Ω


F(u,v,t)G(u,v,t)k(u,v,t)dudvdt.

From Proposition 4.8, it is the scalar product induced by the standard scalar product (1) on Pol(Sn−1).

The subspaces Hk,in−1 are pairwise orthogonal. Consequently the matrix coefﬁ-

cients of Ykn(u,v,t) are pairwise orthogonal for [·,·]. Their norm is also easy to compute, and we obtain the following useful formulas:

# Proposition 4.10.

- (a) For all k,k′ and all i,j, i′,j′ we have

(15) [ Ykn i,j, Ykn′ i′,j′] =

δ(i,j,k),(i′,j′,k′) hkn−1

![image 97](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile97.png>)

.

- (b) For all symmetric matrices A,B and all k,k′ we have


- (16) [ A,Y nk , B,Y nk′ ] =

![image 98](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile98.png>)

![image 99](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile99.png>)

δk,k′ A,B hkn−1

![image 100](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile100.png>)

.

Proof. Obvious.

4.3. Characterization of the positive deﬁnite polynomials. In view of Theorem 4.4, we are concerned with the construction of polynomials satisfying condition (a). We prove in this subsection that this property is stable under multiplication. We start with a characterization of the set of polynomials satisfying (a) of Theorem 4.4.

Deﬁnition 4.11. We say that the polynomial F(u,v,t) ∈ R[u,v,t] is positive definite if, for all ﬁnite C ⊂ Sn−1, for all functions α : C → R,

- (17) (c,c′)∈C2


α(c)α(c′)F(e · c,e · c′,c · c′) ≥ 0.

The polynomials F(u,v,t) of the form

d

Fk,Y nk(u,v,t)

![image 101](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile101.png>)

F(u,v,t) =

k=0

with Fk 0 for all 0 ≤ k ≤ d are positive deﬁnite in the above sense. Note that

- (17) is slightly stronger than the positivity property of the matrices Ykn proved in Theorem 2.2; the argument is essentially the same, as it follows from the equality


α(c)α(c′)Zkn(c,c′) =

(c,c′)∈C2

α(c)Ekn(c)

c∈C

α(c)Ekn(c)

c∈C

t

0.

We prove with next proposition that all positive deﬁnite polynomials in Rd arise in this way.

Proposition 4.12. Let F(u,v,t) ∈ Rd. Let (F0,... ,Fd) be symmetric matrices such that

d

Fk,Y nk(u,v,t) . If F is positive deﬁnite, then Fk 0 for all 0 ≤ k ≤ d.

![image 102](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile102.png>)

F(u,v,t) =

k=0

Proof. Let F˜(x,y) = F(e · x,e · y,x · y). By compactness, F is positive deﬁnite if and only if for all f ∈ Pol(Sn−1),

2 f(x)f(y)F˜(x,y)dωn(x)dωn(y) ≥ 0. As a consequence, if Q(x) is any matrix,

Sn−1

Sn−1

2 Q(x),Q(y) F ˜(x,y)dωn(x)dωn(y) ≥ 0.

Let us ﬁx k ∈ {0,... ,d} and let A be a (d−k+1)×(d−k+1) symmetric, positive semideﬁnite matrix. Because of expression (6) of Zkn, we can write A,Zkn(x,y)t in the form Q(x),Q(y) . Hence,

2 A,Zkn(x,y)t F ˜(x,y)dωn(x)dωn(y) ≥ 0. In terms of the scalar product [·,·] this is equivalent to

Sn−1

[ A,Y nk ,F] ≥ 0.

![image 103](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile103.png>)

Since from (16) [ A,Y nk ,F] = hkn−1 −1 A,Fk , we have proved that A,Fk ≥ 0 for all A 0, and so Fk 0.

![image 104](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile104.png>)

Remark 4.13. This characterization of positive deﬁnite functions is in fact already proved in [4, Section III] in a more general context: for compact spaces which are homogeneous under the action of their automorphism group, but not necessarily two-point homogeneous. The assumption that the group acts transitively is however not needed in the proof.

Corollary 4.14. Let F,G ∈ Rd. If F and G are positive deﬁnite, then the product FG is also positive deﬁnite.

Proof. From Proposition 4.12 it sufﬁces to consider the case F = A,Y nk , G = B,Y nl , where A and B are positive semideﬁnite matrices. Again, we write A,Zkn(x,y)t = Q(x),Q(y) and B,Zln(x,y)t = T(x),T(y) . With the

![image 105](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile105.png>)

![image 106](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile106.png>)

formula

Q(x),Q(y) T(x),T(y) = Q(x) ⊗ T(x),Q(y) ⊗ T(y) we have

α(c)α(c′)F˜(c,c′)G˜(c,c′)

(c,c′)∈C2

α(c)α(c′) Q(c),Q(c′) T(c),T(c′)

=

(c,c′)∈C2

α(c)Q(c) ⊗ T(c),α(c′)Q(c′) ⊗ T(c′))

=

(c,c′)∈C2

= UC,UC ≥ 0

with

UC =

α(c)Q(c) ⊗ T(c).

c∈C

4.4. Reproducing kernels. We deﬁne the kernel Kd : R3 × R3 → R by

- (18) Kd((u,v,t),(u′,v′,t′)) :=

n

k=0

hkn−1 Y nk(u,v,t),Y nk(u′,v′,t′) .

![image 107](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile107.png>)

![image 108](<2006-bachoc-semidefinite-programming-multivariate-orthogonal_images/imageFile108.png>)

Proposition 4.15. The kernel Kd is the reproducing kernel of the space Rd, i.e., for all F ∈ Rd and all (u′,v′,t′) ∈ R3 we have

- (19) [Kd(·,(u′,v′,t′)),F] = F(u′,v′,t′). Proof. It is straightforward from (16).


REFERENCES

- [1] C. Bachoc, Linear programming bounds for codes in Grassmannian spaces, IEEE Trans. Inf. Th. 52-5 (2006), 2111–2125.
- [2] C. Bachoc, F. Vallentin, New upper bounds for kissing numbers from semideﬁnite programming, to appear in J. Amer. Math. Soc.
- [3] A. Barg, O.R. Musin, Codes in spherical caps, Adv. Math. Comm. 1 (2007), 131–149.
- [4] S. Bochner, Hilbert distances and positive deﬁnite functions, Ann. of Math. 42 (1941) 647– 656.
- [5] B. Borchers, CSDP, A C library for semideﬁnite programming, Optimization Methods and Software 11 (1999) 613–623.
- [6] E. Bannai, N.J.A. Sloane, Uniqueness of certain spherical codes, Canad J. Math. 33 (1981), 437–449.
- [7] J.H. Conway, N.J.A. Sloane, Sphere Packings, Lattices and Groups, Springer-Verlag, 1988.
- [8] P. Delsarte, An algebraic approach to the association schemes of coding theory, Philips Res. Rep. Suppl. (1973), vi+97.
- [9] P. Delsarte, J.M. Goethals, J.J. Seidel, Spherical codes and designs, Geom. Dedicata 6 (1977), 363–388.
- [10] G. Fejes T´oth, Ten-neighbor packing of equal balls, Periodica Math. Hungar. 12, (1981) 125– 127.
- [11] G.A. Kabatiansky, V.I. Levenshtein, Bounds for packings on a sphere and in space, Problems of Information Transmission 14 (1978), 1–17.
- [12] W. Kuperberg, Optimal arrangements in packing congruent balls in a spherical container, Discrete Comput. Geom. 37 (2007), 205–212.
- [13] V.I. Levenshtein, On bounds for packing in n-dimensional Euclidean space, Soviet Math. Dokl. 20 (1979), 417–421.
- [14] O.R. Musin, The one-sided kissing number in four dimensions, Periodica Math. Hungar. 53,

(2006) 209–225.

- [15] O.R. Musin, Bounds for codes by semideﬁnite programming, preprint, September 2006, arXiv:math.MG/0609155.
- [16] A.M. Odlyzko, N.J.A. Sloane, New bounds on the number of unit spheres that can touch a unit sphere in n dimensions, J. Combin. Theory Ser. A 26 (1979), 210–214.
- [17] M. Putinar, Positive polynomials on compact semi-algebraic sets, Ind. Univ. Math. J. 42


(1993), 969–984.

C. BACHOC, LABORATOIRE A2X, UNIVERSITE´ BORDEAUX I, 351, COURS DE LA LIBE´-

RATION, 33405 TALENCE, FRANCE E-mail address: bachoc@math.u-bordeaux1.fr F. VALLENTIN, CENTRUM VOOR WISKUNDE EN INFORMATICA (CWI), KRUISLAAN 413,

1098 SJ AMSTERDAM, THE NETHERLANDS E-mail address: f.vallentin@cwi.nl

