# arXiv:1705.06996v2[math.OC]5Dec2017

## A lower bound on the positive semideﬁnite rank of convex bodies

#### Hamza Fawzi∗ Mohab Safey El Din† November 6, 2021

###### Abstract

The positive semideﬁnite rank of a convex body C is the size of its smallest positive semidef-

√initelogformulation.d where d is Wetheshowsmallestthatdegreethe positiveof a polynomialsemideﬁnitethatrankvanishesof any convexon thebodyboundaryC is atofleastthe polar of C. This improves on the existing bound which relies on results from quantiﬁer elimination. Our proof relies on the B´ezout bound applied to the Karush-Kuhn-Tucker conditions of optimality. We discuss the connection with the algebraic degree of semideﬁnite programming and show that the bound is tight (up to constant factor) for random spectrahedra of suitable dimension.

### 1 Introduction

Semideﬁnite programming is the problem of optimizing a linear function over a convex set described by a linear matrix inequality:

max cTx s.t. x ∈ S where S ⊆ Rn has the form:

S = {x ∈ Rn : A0 + x1A1 + ··· + xnAn 0}. (1)

Here A0,...,An are real symmetric matrices of size m × m and the notation M 0 indicates that M is positive semideﬁnite. A set of the form (1) is called a spectrahedron.

Given a convex set C ⊆ Rk, we say that C has a semideﬁnite lift of size m if it can be expressed as

C = π(S)

where S is a spectrahedron (1) deﬁned using matrices of size m × m and π is any linear map. If C can be expressed in this way, then any linear optimization problem over C can be expressed as a semideﬁnite program of size m. The size of the smallest semideﬁnite lift of C is called the positive semideﬁnite rank of C [GPT13, FGP+15].

The purpose of this paper is to give a general lower bound on the positive semideﬁnite rank of convex bodies. Here, by a convex body we mean a closed convex set such that the origin lies in the interior of C. For the statement of our main theorem, we need the notion of polar of a convex body C, deﬁned as follows:

Co = c ∈ Rk : c,x ≤ 1 ∀x ∈ C .

∗Department of Applied Mathematics and Theoretical Physics, University of Cambridge, UK. †Sorbonne Universite´s, UPMC Univ Paris 06, CNRS, INRIA Paris Center, LIP6, Equipe PolSys, F-75005, Paris,

France.

The polar of a convex body is another full-dimensional closed convex set that is bounded and contains the origin [Roc97, Theorem 14.6]. Throughout the paper, we use log for the logarithm base 2. We can now state the ﬁrst main result of this article.

- Theorem 1. Let C be a convex body and let Co be its polar. Let d be the smallest degree of a

polynomial with real coeﬃcients that vanishes on the boundary of Co. Then rankpsd(C) ≥

√log d. We also show that this bound is tight in general (up to multiplicative factors):

- Theorem 2. There exist convex bodies C where the degree d of the algebraic boundary of Co can

be made arbitrary large and where rankpsd(C) ≤

√20log d.

When C is a polytope, the degree d of the algebraic boundary of Co is nothing but the number of vertices of C. Theorem 1 can thus be compared to the well-known lower bound of Goemans [Goe15] on the size of linear programming lifts. The linear programming extension complexity of a polytope P is the smallest f such that P can be written as the linear projection of a polytope with f facets.

- Theorem 3 (Goemans [Goe15, Theorem 1]). Assume P is a polytope with d vertices. Then the linear programming extension complexity of P is at least log d.


Proof. The proof is elementary so we include it for completeness. Assume P = π(Q) where Q is a polytope with f facets. The pre-image by π of any vertex of P is a face of Q. Since Q has at most 2f faces it follows that f ≥ log d.

| |
|---|


For functions f,g : N → R we say that f(n) ∈ Ω(g(n)) if there exists a constant K > 0 such that f(n) ≥ K · g(n) for all large enough n.

The only previous lower bound on the positive semideﬁnite rank that applies to arbitrary convex bodies that we are aware of is the bound proved in [GPT13, Proposition 6] which says that1 rankpsd(C) ≥ Ω nlog log(logdd/n) where n is the dimension of C. This bound was obtained using results from quantiﬁer elimination theory and one drawback is that it involves constants that are unknown or diﬃcult to estimate. Our lower bound of Theorem 1 improves on this existing bound and also has the advantage of being explicit.

Main ideas. The main idea behind the proof of Theorem 1 is simple. Given a convex body C, we exhibit a system of polynomial equations that vanishes on the boundary of Co. This system of polynomial equations is nothing but the Karush-Kuhn-Tucker (KKT) system, after discarding the inequality constraints to get an algebraic variety. Applying the B´ezout theorem on the KKT system gives us an upper bound on the degree of this variety and yields the stated lower bound. To prove Theorem 2 about tightness of the bound we appeal to existing works [NRS10] where the degree of the KKT system was explicitly computed, under certain genericity assumptions. The convex bodies of Theorem 2 are in fact random spectrahedra (i.e., spectrahedra deﬁned using random matrices A0,...,An) of appropriate dimension, where the formulas for the algebraic degree of semideﬁnite programming [vBR09] allow us to lower bound the degree of the algebraic boundary of their polars. We would like to point out that many of the ideas involved in the proofs of Theorems 1 and 2 appear in some form or another in [RS12, NRS10, SS15]. For example a study of the algebraic boundary of polars of spectrahedra appears in [RS12, Section 5.5]. However it seems that the connection

1In the bound shown in [GPT13, Proposition 6], d is the degree of the algebraic boundary of C. However since rankpsd(C) = rankpsd(Co) it can also be taken to be that of Co in the statement of the lower bound.

with the positive semideﬁnite rank was not made explicit before. The focus in these previous works seemed to be on getting exact values for the degrees, at the price of genericity assumptions. In the present work our aim was on getting bounds (tight up to constant factors) but valid without any genericity assumption.

Notations. The (topological) boundary of a set C ⊆ Rn is denoted ∂C and deﬁned as ∂C = cl(C) \ int(C) where cl and int denote closure and interior respectively. The algebraic boundary of C ⊆ Rn denoted ∂aC is the smallest aﬃne algebraic variety in Cn that contains ∂C. We denote by Sm the space of m × m real symmetric matrices. This is a real vector space of dimension

m + 1 2

.

tm :=

We also denote by Sm(C) the space of m × m symmetric matrices with complex entries.

### 2 Proof of Theorem 1

- In this section we prove Theorem 1. To do so we will exhibit polynomial equations that vanish on the boundary of polars of spectrahedra and their shadows. These equations are nothing but the KKT conditions of optimality. Applying the B´ezout bound will yield Theorem 1.


KKT equations. Let A0,...,An ∈ Sm and deﬁne

A(x) := x1A1 + ··· + xnAn. Consider the linear optimization problem

max cTx s.t. A0 + A(x) 0 (2) and assume that the feasible set

S = {x ∈ Rn : A0 + A(x) 0}

contains 0 in its interior. In this case we know that any optimal point x of (2) must satisfy the following KKT conditions:

∃X,Z ∈ Sm : X = A0 + A(x), A∗(Z) + c = 0, XZ = 0, X 0, Z 0 (3)

where the variable Z plays the role of dual multiplier and A∗(Z) = (Trace(A1 Z),...,Trace(An Z)). Conditions (3) consist of equality conditions as well as inequality conditions. If we disregard the inequality conditions we get a system of polynomial equations in (x,X,Z) ∈ Rn × Sm × Sm which we denote by KKT(c):2

KKT(c) : X = A0 + A(x), A∗(Z) + c = 0, XZ = 0. (4)

This system has n + 2tm unknowns and consists of n + tm + m2 equations. A crucial fact about this system is that it has a ﬁnite number of solutions, assuming the parameters A0,A1,...,An and

2We note here that there are multiple ways of writing the SDP complementarity conditions in general, and these can lead to diﬀerences in the context of algorithms for SDP, see e.g., the discussion in [BTN01, Section 6.5.4]. For our purposes, the main property that we will need of the system KKT(c) is that it has a ﬁnite number of solutions generically (Lemma 1).

c are generic (we come back to the genericity assumption after the statement of the result; some form of genericity is needed for the statement to be true). It is the number of solutions to the KKT system that will give an upper bound on the degree of the algebraic boundary of the polar as we will see later.

- Lemma 1 (Finiteness of KKT solutions). For generic A0,A1,...,An and c, the KKT system of polynomial equations (4) has a ﬁnite number of complex solutions (x,X,Z) ∈ Cn×Sm(C)×Sm(C). Furthermore the number of such solutions is at most 2m2.

Proof. That the KKT system has a ﬁnite number of solutions generically was proved in [NRS10, Theorem 7]. We include a sketch of proof for completeness which is simply a dimension count argument. There are three equations in (4):

- • The equation X = A0 + A(x) is linear and deﬁnes an aﬃne subspace of codimension tm (we assume that A is injective).
- • The equation A∗(Z) + c = 0 is also linear and deﬁnes an aﬃne subspace of codimension n.
- • Finally the equations XZ = 0 can be shown to deﬁne a variety of codimension tm (see e.g., [NRS10, Proof of Theorem 7]).


If A0,A1,...,An and c are generic, a Bertini-Sard type theorem tells us that the intersection of these three varieties will have codimension equal to the sum of the codimensions, i.e., tm+n+tm = 2tm+n which is the dimension of the ambient space. In other words the variety deﬁned by (4) is zerodimensional, i.e., there are a ﬁnite number of solutions.

B´ezout bound tells us that the number of solutions is at most the product of the degrees of the polynomial equations that form the system (4), which in this case is 2m2.

| |
|---|


Remark 1 (Genericity assumption of Lemma 1). An assumption of genericity is necessary in general to guarantee that the system (4) has a ﬁnite number of solutions. This is to rule out situations where the optimization problem (2) has an inﬁnite number of solutions (a positive dimensional face of S) or when there are an inﬁnite number of dual multipliers. In Lemma 1 we assumed all the parameters A0,...,An,c generic to be able to apply a standard Bertini-Sard type theorem. We think however it may be possible to remove some of the genericity assumptions (e.g., just to assume genericity on A0 and c) but we did not pursue this further here as the current statement of the lemma will be suﬃcient for our purposes.

The next lemma shows that the number of solutions to the KKT system is intimately tied to the degree of the algebraic boundary of the polar So.

- Lemma 2. Consider a spectrahedron S = {x ∈ Rn : A0+x1A1+···+xnAn 0} where A0,...,An ∈ Sm and assume that 0 ∈ intS. Let So be its polar deﬁned by


So = {c ∈ Rn : c,x ≤ 1 ∀x ∈ S}.

Then there is a polynomial of degree at most 2m2 with real coeﬃcients that vanishes on the boundary of So.

Proof. The points on the boundary of So are exactly those c such that maxx∈S cTx = 1. Consider the system of polynomial equations obtained by adding the equation cTx = 1 to the KKT system:

KKT :

X = A0 + A(x), A∗(Z) + c = 0, XZ = 0 cTx = 1.

(5)

We think of (5) as a system of equations on the variables (x,X,Z,c). If we eliminate the variables x,X,Z we get an algebraic variety V ⊂ Cn in the variables c:

V = elimc(Sols(KKT)). (6)

By construction this variety contains the boundary of So, i.e., ∂So ⊆ V ∩ Rn. To bound the degree of ∂aSo it thus suﬃces to count the number of intersections of V with a generic line, since ∂aSo ⊆ V and ∂aSo is a hypersurface [Sin15, Corollary 2.8]. We will do this ﬁrst in the case where A0,...,An are generic. Let c0 ∈ Cn generic and consider the line {λc0 : λ ∈ C}. Since V was deﬁned by eliminating variables x,X,Z from (5), we know that λc0 ∈ V if and only if there exist (x,X,Z) in the solution set of KKT(λc0) and λc0Tx = 1. By looking at the equations deﬁning KKT(λc0) this implies that (x,X,(c0Tx)Z) is in the solution set of KKT(c0). Thus the number of intersection points is at most the cardinality of the solution set of KKT(c0), i.e., 2m2. We have thus shown that ∂aSo is a hypersurface of degree at most 2m2.

It thus remains to treat the case where A0,A1,...,An in the deﬁnition of S are not generic. This can be done by using a simple perturbation argument. Let N be the total number of the entries in n+1 symmetric matrices. Hence, the sequence of matrices A0,...,An represents a point A in RN. For any k ∈ N \ {0}, there exists a point Ak in RN in the ball centered at A of radius 1/k which is generic and represents a sequence of symmetric matrices A0,k,...,An,k. Since, by assumption

- 0 ∈ intS, A0 is positive deﬁnite, one can assume w.l.o.g. that A0,k is positive deﬁnite. Hence the spectrahedra Sk deﬁned by A0,k,...,An,k are generic, non-empty and such that 0 ∈ intSk. Hence, one can apply to them the above paragraph.


Now, let (pk) be a sequence of polynomials of degree at most 2m2 that vanish on the boundary of (Sk). We can rescale each pk to be unit-normed and we can thus assume that (pk) has a convergent subsequence that converges to some polynomial p. Clearly the degree of p is at most 2m2. Finally it is easy to verify that p vanishes on the boundary of So.

| |
|---|


We are now in position to prove Theorem 1 on the lower bound for the positive semideﬁnite rank. The main idea is that if C = π(S) where S is a spectrahedron, then by duality Co is the intersection of So with an aﬃne subspace and thus the algebraic boundary of Co has degree at most that of So.

- Proof of Theorem 1. Assume C is a convex body that can be written as C = π(S) where S is a spectrahedron deﬁned using an m×m linear matrix inequality and π a linear map. We can assume that S has nonempty interior, and furthermore that 0 ∈ int(S) since 0 ∈ int(C). We are going to exhibit a polynomial of degree at most 2m2 that vanishes on the boundary of Co. Let p be a polynomial of degree at most 2m2 that vanishes on the boundary of So. Then we claim that the polynomial q = p ◦ π∗ (where π∗ is the adjoint of π), which has degree at most 2m2 vanishes on the boundary of Co. Indeed if y is on the boundary of Co this means that maxx∈C y,x = 1 which means that maxx∈S π∗(y),x = 1 and so π∗(y) is on the boundary of So, hence q(y) = p(π∗(y)) = 0.


If we let d be the degree of the algebraic boundary of Co and m = rankpsd(C) we have thus shown that d ≤ 2m2 which implies rankpsd(C) = m ≥

√log d.

| |
|---|


Application: number of vertices of spectrahedral shadows. In this subsection we discuss an application of Theorem 1 to bound the number of vertices of spectrahedral shadows. If C ⊆ Rn is a convex body and x ∈ C, the normal cone of C at x is deﬁned as

NC(x) := {c ∈ Rn : c,z ≤ c,x ∀z ∈ C}.

A point x ∈ C is called a vertex if NC(x) is full-dimensional. Observe that any vertex of C must be an extreme point, but not all extreme points are vertices, see Figure 1. Vertices play the role of singularities on the boundaries of convex sets; in fact they are also sometimes called 0-singular points. It is known, see e.g., [Sch13, Theorem 2.2.5] that any convex set has at most a countable number of vertices. Vertices of spectrahedra arising from combinatorial optimization problems have been studied in [LP95, dCST15]. The next theorem gives an upper bound on the number of vertices of any spectrahedral shadow. To the best of our knowledge this is the ﬁrst such bound.

- Theorem 4. If C is a convex body having a semideﬁnite representation of size m, then C has at most 2m2 vertices.


Proof. Any vertex of C will contribute a linear factor in the algebraic boundary of Co: indeed if x is a vertex of C then the algebraic boundary of C must contain the hyperplane {c ∈ Rn : cTx = 1} (see e.g., Figure 1(right)). Thus the degree of ∂aCo is greater than or equal the number of vertices of C. The result follows since the degree of ∂aCo is at most 2m2.

| |
|---|


NC(x)

x

C

Co

- Figure 1: Left: A vertex of a convex set C. Right: The polar of C. We see that each vertex contributes a hyperplane in the algebraic boundary ∂aCo.


### 3 Tightness of lower bound, and algebraic degree of semideﬁnite programming

- In this section we prove Theorem 2. We will show that the lower bound of Theorem 1 is tight up


to a constant factor on certain random spectrahedra of appropriate dimension n, namely n ≈ tm/2.

Let S be a spectrahedron deﬁned using matrices A := (A0,...,An). In the previous section we saw that if we project the following KKT equations

KKT :

X = A0 + A(x), A∗(Z) + c = 0, XZ = 0 cTx = 1

(7)

on c ∈ Cn we get an algebraic variety V(A) = elimc(Sols(KKT))

that vanishes on the boundary of So. This variety could coincide exactly with ∂aSo but it can also contain spurious components that do not intersect ∂So and thus are not in its Zariski closure (see Section 4 later for an example).

In order to prove our result we need to understand the irreducible components of the variety V(A). If we can show that there is an irreducible component W of V(A) whose intersection with the boundary of So has dimension the one of W then we know that the degree of the algebraic boundary of So is at least deg W. When A is generic, the irreducible components of V(A) have been studied in [NRS10] where it was shown that they are obtained by imposing rank conditions on the matrices X and Z in the KKT equations, namely by considering the following system for a ﬁxed r:

 

X = A(x) + A0, A∗(Z) + c = 0, XZ = 0 cTx = 1, rank(X) ≤ r, rank(Z) ≤ m − r.

KKTr :

(8)



We think of (8) as a system of equations in (x,X,Z,c). If we eliminate the variables (x,X,Z) from the above equations we get an algebraic variety in Cn that is contained in V(A). We call this variety Vr(A):

Vr(A) = elimc(Sols(KKTr)) ⊆ V(A). (9)

For generic A, it was shown in [NRS10, Theorem 13] that Vr(A) is a hypersurface provided r satisﬁes the Pataki bounds:

n ≥ tm−r and tr ≤ tm − n. (10) Using Bertini theorem one can show that this variety is also irreducible over C provided n > tm−r.

- Lemma 3. For generic A0,...,An the variety Vr(A) is irreducible over C provided n > tm−r.


Before proving this lemma we ﬁrst explain the reason for the condition n > tm−r (which is stronger than the condition imposed by the Pataki bound (10)). The variety Vr(A) is the dual of the determinantal variety {x ∈ Cn : rank(A0 + x1A1 + ··· + xnAn) ≤ r}. The condition n > tm−r rules out the case where this determinantal variety is zero-dimensional, in which case the dual variety Vr(A) is a union of hyperplanes and is thus not irreducible. Note that if we are only interested in irreducibility statements over Q (assuming that A0,...,An are generic with entries in Q) then we do not need to impose such a condition. See [SS15, Remark 2.2] for more on this.

Proof of Lemma 3. The main ingredient of the proof is Bertini’s irreducibility theorem [Deb99, Theorem 4.23]. We will start by showing that the variety

X = A(x) + A0, XZ = 0, rank(X) ≤ r, rank(Z) ≤ m − r (11)

is irreducible for a generic choice of A0,...,An. In [NRS10, Lemma 6] it was shown that {XZ = 0}r := {(X,Z) : XZ = 0,rank(X) ≤ r,rank(Z) ≤ m − r} is irreducible. Consider the projection map u(X,Z) = X. We know that u({XZ = 0}r) is the determinantal variety consisting of symmetric matrices of rank ≤ r and has dimension tm − tm−r. By Bertini theorem [Deb99, Theorem 4.23] we know that for a generic aﬃne subspace L of dimension n the variety u−1(L) is going to be irreducible provided tm − tm−r ≥ 1 + codimL = 1 + tm − n, i.e., provided that n ≥ tm−r + 1. In other words this tells us that (11) is irreducible for a generic choice of A0,...,An.

Consider now the map φ(x,X,Z) = (x,X,−Z/(A∗(Z)Tx),A∗(Z)/(A∗(Z)Tx)) (where the last coordinates stand for c). Observe that the image of the restriction of φ to the solution set of (11) is exactly the variety deﬁned by (8). Since φ is rational at all points, it is regular [Sha77, Thm 4, Sec. 3.2]. Because the solution set of (11) is irreducible, its image by φ is irreducible. Since Vr(A) is the projection of an irreducible variety it is also irreducible.

| |
|---|


The degrees of the irreducible components Vr(A) were computed (for generic A = (A0,...,An)) in [NRS10, vBR09] and are denoted by δ(n,m,r). The resulting formulas involve minors of the matrix of binomial coeﬃcients. An elementary analysis of these formulas allows us to show that in a special regime for n and r, the algebraic degree is at least 2m2/20.

- Lemma 4. Assume m even and large enough and consider n = tm/2 + 1 and r = m/2 + 1. Then for generic A = (A0,...,An) ∈ (Sm(C))n+1 the variety Vr(A) has degree ≥ 2m2/20. Proof. The proof is in Appendix A.

| |
|---|


In order to use Lemma 4 we need to show that there is at least one choice of A = (A0,...,An) with n = tm/2 +1 such that the variety Vr(A) with r = m/2+1 will actually belong to ∂aSo, where S = {x : A0 + x1A1 + ··· + xnAn 0}. We can prove this by appealing to results by Amelunxen and Bu¨rgisser [AB15] where random semideﬁnite programs were analyzed and where it was shown that every value of rank in the Pataki range occurs with “positive probability”.

- Lemma 5. Let m and 1 ≤ n ≤ tm be ﬁxed. Let r in the associated Pataki range (10) with the additional constraint n > tm−r. Let Γ be any Zariski open set in (Sm(C))n+1. Then there exists A = (A0,...,An) ∈ Γ ∩ (Sm(R))n+1 such that the variety Vr(A) is contained in ∂aSo where S = {x ∈ Rn : A0 + x1A1 + ··· + xnAn 0}. Proof. See Appendix B.


| |
|---|


The proof of Theorem 2 is now complete:

- Proof of Theorem 2. Let m be even and large enough and let n = tm/2 + 1. Lemma 5 with r = m/2 + 1 tells us that there is a spectrahedron such that the variety Vr(A) is contained in ∂aSo where S = {x : A0 +x1A1 +···+xnAn 0}. By Lemma 4 we know that the degree of this variety


√20log d as desired.

is at least 2m2/20 and so d = deg(∂aCo) ≥ 2m2/20. But this means that rankpsd(S) ≤ m ≤

| |
|---|


### 4 Example

In this section we consider an example of spectrahedral shadow to illustrate some of the ideas presented in the proofs of Theorem 1 and Theorem 2. Consider the following linear matrix inequality:

  

  .

1 + s t x + s y − t t 1 − s −y − t x − s

A(x,y,s,t) :=

- x + s −y − t 1 + x −y
- y − t x − s −y 1 − x


One can show that the projection of the associated spectrahedron on the variables (x,y) is the regular pentagon in the plane, i.e., if we let S be the spectrahedron associated to A and π(x,y,s,t) = (x,y) then:

2kπ 5

2kπ 5

C := π(S) = conv cos

,sin

,k = 0,...,4 . (12)

It is not diﬃcult to see that the polar of C is another regular pentagon but slightly rotated and scaled:

1 cos(π/5)

Co =

conv cos

2(k + 1/2)π 5

,sin

2(k + 1/2)π 5

,k = 0,...,4 .

From Section 2 we know that the KKT equations allow us to get a polynomial that vanishes on the boundary of Co. The associated variety (denoted by V in (6)) in this case is shown in Figure 2. We see that the variety V contains the algebraic boundary of the polar Co (red lines). However

| | | |
|---|---|---|
| | | |


- Figure 2: Variety V deﬁned in (6) that vanishes on the boundary of Co, where C is the regular


pentagon, see (12). We see that ∂aCo ⊂ V and that V has extra components not in ∂aCo. These are shown in blue.

we also see that it has extra components that are not in ∂aCo: these extra components are shown in blue in Figure 2.

### 5 Discussion

The algebraic argument given in this paper can also be used to lower bound the size of second-order cone lifts, or more generally lifts using products of Sk+. More precisely one can show that if C has a lift using r copies of Sk+ then r ≥ k12 log d where d is the degree of the algebraic boundary of Co. In particular we recover the result of Goemans (Theorem 3) with k = 1.

There are a couple of questions that we believe it would be interesting to pursue further:

- • Polytopes: One important question is to know whether the lower bound rankpsd(C) ≥

√log d can be improved in the case where C is a polytope? In particular can the lower bound be improved to log d in this special case? Recall that if C is a polytope then d = deg ∂aCo is simply its number of vertices.

- • Vertices of spectrahedra: A related question is to know whether the bound of 2m2 on the number of vertices of spectrahedral shadows (Theorem 4) is tight? In words, can we ﬁnd a spectrahedron (or a spectrahedral shadow) that has 2Ω(m2) vertices? We believe that a

natural candidate to try are random spectrahedra of appropriate dimension n ≈ tm/2. Results in [AB15] can be useful for this question.

- • Explicit example: Thirdly, is there an explicit example of a spectrahedron whose polar has an algebraic boundary of degree 2Ω(m2)?


- • Analysis of algebraic degree: Finally we believe it would be useful to have an (asymptotic) analysis of the formulas for the algebraic degrees of semideﬁnite programming δ(n,m,r). For this paper we have used elementary manipulations to show that when n ≈ tm/2 and for certain values of r then δ(n,m,r) is 2Ω(m2), but we believe a more complete and systematic study of these quantities can be undertaken. For example we conjecture that in the regime n ≈ tm/2 the value of δ(n,m,r) for any r in the Pataki range is 2Ω(m2). Proving such a result would allow us to simplify the proof of Theorem 2 by bypassing the need for Lemma 5 (it suﬃces to


take any generic spectrahedron of dimension say n = tm/2+1 and to observe that at least one of the Vr(A) must belong to ∂aSo). An analysis of the values of δ(n,m,r) would also allow us to improve the constants in Theorems 1 and 2. For example, where we used the B´ezout bound in Lemma 1 one can instead use the quantity r δ(n,m,r) (where r ranges over the Pataki range) as an upper bound on the number of solutions of the KKT system.

Acknowledgments. We would like to thank Rainer Sinn for clariﬁcations concerning questions of irreducibility used in Lemma 3, and James Saunderson for comments that helped improve the paper. We would also like to thank anonymous referees for their comments on an earlier version of the paper that was submitted for presentation to the conference MEGA 2017. Finally we would like to thank Xavier Allamigeon and St´ephane Gaubert for organizing the session on Semideﬁnite Optimization at the PGMO 2016 conference where this project was started. The second author is supported by the ANR JCJC GALOP grant.

### A Proof of Lemma 4: analysis of the formula for the algebraic degree of semideﬁnite programming

In this subsection we prove Lemma 4 which we restate below.

- Lemma (Restatement of Lemma 4). Assume m even and large enough and consider n = tm/2 + 1 and r = m/2 + 1. Then for generic A = (A0,...,An) ∈ (Sm(C))n+1 the variety Vr(A) has degree ≥ 2m2/20.


For this we rely on the formula for the algebraic degree of semideﬁnite programming proved in [vBR09].

Let δ(n,m,r) be the degree of the variety Vr(A) where A is a generic pencil (A0,...,An) ∈ (Sm(R))n+1. A formula for δ(n,m,r) was given in [vBR09] which we describe now. Let Ψ be the (inﬁnite) matrix of binomial coeﬃcients, i.e., Ψi,j = j i for i,j ≥ 0. For I ⊆ {1,...,m} deﬁne ψI to be the sum of all the |I| × |I| minors of Ψ[I,·]. For example if I is a singleton we have ψ{i} = 2i−1.

- Theorem 5 ([vBR09], see also [Ran12]). For a generic A = (A0,...,An) the algebraic degree of Vr(A) (see Equation (9)) is given by:


ψIψIc (13)

δ(n,m,r) =

I⊆{1,...,m} |I|=m−r,s(I)=n

where for I ⊆ {1,...,m} we denote by s(I) the sum of the elements of I, and Ic = {1,...,m} \ I.

The main purpose of this Appendix is to prove the following lower bound on δ(n,m,r) in a special regime.

- Lemma 6. For all large enough even m, n = tm/2+1 and r = m/2+1 we have δ(n,m,r) ≥ 2m2/20. The bounds we give in this appendix are very crude and are not meant to be optimal. We

actually conjecture that in the regime n ≈ tm/2, we have δ(tm/2,m,r) ≥ 2Ω(m2) for any r in the Pataki range (10).

In order to prove our result we will ﬁrst analyze the value of ψ on intervals. We will show

- Lemma 7. For any integers p ≤ q we have ψ[p+1,q] ≥ (1 + 2qp−−p1)tp. Before proving Lemma 7, we ﬁrst see how to use it to prove Lemma 6.


Proof of Lemma 6. Consider I = {1,...,m/2 − 2} ∪ {m}. Then |I| = m/2 − 1 = m − r and s(I) = tm/2 + 1 = n. Thus δ(n,m,r) ≥ ψIψIc ≥ ψIc = ψ[m/2−2,m−1]. Using Lemma 7 we get

tm/2−2

m/2 + 1 m − 3

ψ[m/2−2,m−1] ≥ 1 +

.

We now use the fact that 1+ m/m2+1−3 ≥ 1+1/2 = 3/2 and tm/2−2 ≥ m2/9 for large enough m to get ψ[m/2−1,m−2] ≥ 2(log2(3/2)/9)m2 ≥ 2m2/20.

| |
|---|


It thus remains to prove Lemma 7. We can get the value of ψ on intervals by considering the case n = tm−r in (13). Indeed in this case there is only one set I that satisﬁes the constraints of the summation (13) which is I = {1,...,m − r}. Since ψ[1,m−r] = 1 it follows that δ(tm−r,m,r) = ψ[m−r+1,m]. On the other hand a simpler formula for δ(tm−r,m,r) was provided in [NRS10, Corollary 15], based on a result by Harris and Tu [HT84]. This tells us that

δ(tm−r,m,r) = ψ[m−r+1,m] =

m−r−1

m+i m−r−i 2i+1 i

. (14)

i=0

The formula on the right-hand side can be simpliﬁed further using simple manipulations to get ψ[m−r+1,m] =

r + i + j + 1 i + j + 1

. (15)

0≤i≤j≤m−r−1

To see why this holds, ﬁrst use the deﬁnition of binomial coeﬃcient nk = n...(nk−!k+1) to get

r−1

m−r−1

m+i m−r−i 2i+1 i

(m + i)...(r + 2i + 1) (m − r − i)! ·

i! (2i + 1)...(i + 2)

=

ψ[m−r+1,m] =

(16)

i=0

i=0

Separating the terms in (16) we get

 

  ·

m−r−1

i! (m − r − i)!(2i + 1)...(i + 2)

ψ[m−r+1,m] =

(r + i + j + 1)

. (17)

0≤i≤j≤m−r−1

i=0

Noting that mi=0−r−1 i!/(m − r − i)! = (m−1r)! = i m=0−r−1 (i+1)1 we see that the second factor in (17) is equal to

m−r−1

m−r−1

- i
- j=0


1 (2i + 1)...(i + 2)(i + 1)

1 i + j + 1

=

. (18)

i=0

i=0

By doing an appropriate change of variables and plugging this back in (17) we get (15). Now to prove the bound of Lemma 7 note that each term in the product (15) is at least

- 1+ 2(m−rr)−1 and that there are tm−r terms in the product. The statement of Lemma 7 corresponds to p = m − r and q = m. This completes the proof.


### B Proof of Lemma 5: occurrence of each value of rank in the Pataki range

In this Appendix we prove Lemma 5 which we restate here for convenience.

- Lemma (Restatement of Lemma 5). Let m and 1 ≤ n ≤ tm be ﬁxed. Let r in the associated Pataki range (10) with the additional constraint n > tm−r. Let Γ be any Zariski open set in (Sm(C))n+1. Then there exists a pencil A = (A0,...,An) ∈ Γ ∩ (Sm(R))n+1 such that the variety Vr(A) is contained in ∂aSo, where S = {x ∈ Rn : A0 + x1A1 + ··· + xnAn 0}.


Proof. For convenience in this proof we let, for A = (A0,...,An) ∈ (Sm(R))n+1, S(A) ⊂ Rn denote the associated spectrahedron:

S(A) = {x ∈ Rn : A0 + x1A1 + ··· + xnAn 0}.

In the paper [AB15, Remark 4.1] it is shown that for any r satisfying the Pataki bounds (10) we have

cTx = r > 0 (19)

Pr

rank argmax

A0,...,An,c

x∈S(A)

where A0,...,An,c are standard Gaussian with respect to the Euclidean inner product. In other words, each value in the Pataki range occurs with positive probability. Fix r in the Pataki range satisfying n > tm−r and consider

Ωr = (A0,...,An) ∈ (Sm(R))n+1 : Pr

c

cTx = r > 0 .

rank argmax

x∈S(A)

By (19) we know that Ωr has positive probability (otherwise the complement of Ωr has probability 1 which would contradict (19)). Thus this means that Ωr must meet Γ since Γ is Zariski open.

Let A := (A0,...,An) ∈ Ωr ∩ Γ and let S = S(A) = {x ∈ Rn : A0 + x1A1 + ··· + xnAn 0}. To prove our claim we will show that Vr(A) intersects the boundary ∂So along a semialgebraic set of dimension n − 1. This will prove our claim because if we let U be this semialgebraic set we then have on the one hand ∂aSo ⊇ U¯Z (where U¯Z denotes the Zariski closure) and on the other hand U¯Z = Vr(A), the latter following from the fact that Vr(A) is irreducible of dimension n − 1 and that dimC(U¯Z) = n − 1 since U is a semialgebraic set of dimension n − 1, see [BCR13, Proposition 2.8.2].

It remains to show that Vr(A) intersects ∂So along a semialgebraic set of dimension n − 1. To see why this holds let

U = U˜ ∩ ∂So where U˜ = c ∈ Rn : rank argmax

cTx = r .

x∈S

By deﬁnition of Vr(A) (recall that Vr(A) is deﬁned in terms of rank-constrained KKT equations) we have U ⊆ Vr(A) ∩ ∂So. Now observe that U is a semialgebraic set of dimension n − 1: indeed note that U˜ has nonempty interior (since it is a semialgebraic set with positive probability, see Lemma 8) and so U = U˜ ∩ ∂So has dimension n − 1 since for any α ∈ ∂So and neighborhood A of α, dim(A ∩ ∂So) = n − 1 (because ∂So is the boundary of a full-dimensional convex set). This completes the proof.

| |
|---|


- Lemma 8. If W ⊆ RN is semialgebraic and W has positive probability under the standard Gaussian measure, then W has nonempty interior.


Proof. Any semialgebraic set can be decomposed as a disjoint union of semialgebraic sets that are homeomorphic to (0,1)d (see [BCR13, Theorem 2.3.6]). Since Pr[W] > 0, W must have a component that is homeomorphic to (0,1)N and thus W has nonempty interior.

| |
|---|


### References

[AB15] Dennis Amelunxen and Peter Bu¨rgisser. Intrinsic volumes of symmetric cones and applications in convex programming. Mathematical Programming, 149(1-2):105–130, 2015. 8, 9, 12

[BCR13] Jacek Bochnak, Michel Coste, and Marie-Fran¸coise Roy. Real algebraic geometry, volume 36. Springer Science & Business Media, 2013. 12, 13

[BTN01] Aharon Ben-Tal and Arkadi Nemirovski. Lectures on modern convex optimization: analysis, algorithms, and engineering applications. SIAM, 2001. 3

[dCST15] Marcel K. de Carli Silva and Levent Tun¸cel. Vertices of spectrahedra arising from the elliptope, the theta body, and their relatives. SIAM Journal on Optimization, 25(1):295– 316, 2015. 6

[Deb99] Olivier Debarre. Introduction ` la g´eom´etrie alge´brique. 1999. Available online at http://www.math.ens.fr/~debarre/DEA99.pdf. 7

[FGP+15] Hamza Fawzi, Jo˜o Gouveia, Pablo A. Parrilo, Richard Z. Robinson, and Rekha R. Thomas. Positive semideﬁnite rank. Mathematical Programming, 153(1):133–177, 2015. 1

[Goe15] Michel X. Goemans. Smallest compact formulation for the permutahedron. Mathematical Programming, 153(1):5–11, 2015. 2

[GPT13] Jo˜o Gouveia, Pablo A. Parrilo, and Rekha R. Thomas. Lifts of convex sets and cone factorizations. Mathematics of Operations Research, 38(2):248–264, 2013. 1, 2

[HT84] Joe Harris and Loring W. Tu. On symmetric and skew-symmetric determinantal varieties. Topology, 23(1):71–84, 1984. 11

[LP95] Monique Laurent and Svatopluk Poljak. On a positive semideﬁnite relaxation of the cut polytope. Linear Algebra and its Applications, 223:439–461, 1995. 6

[NRS10] Jiawang Nie, Kristian Ranestad, and Bernd Sturmfels. The algebraic degree of semidefinite programming. Mathematical Programming, 122(2):379–405, 2010. 2, 4, 7, 8, 11

[Ran12] Kristian Ranestad. Algebraic degree in semideﬁnite and polynomial optimization. In Handbook on Semideﬁnite, Conic and Polynomial Optimization, pages 61–75. Springer,

2012. 10 [Roc97] R Tyrell Rockafellar. Convex analysis, volume 28. Princeton University Press, 1997. 2

[RS12] Philipp Rostalski and Bernd Sturmfels. Dualities in convex algebraic geometry. In Grigoriy Blekherman, Pablo A. Parrilo, and Rekha R. Thomas, editors, Semideﬁnite Optimization and Convex Algebraic Geometry, chapter 5, pages 203–249. SIAM, 2012. 2

[Sch13] Rolf Schneider. Convex bodies: the Brunn–Minkowski theory. Number 151. Cambridge

University Press, 2013. 6 [Sha77] Igor Shafarevich. Basic Algebraic Geometry 1. Springer Verlag, 1977. 7 [Sin15] Rainer Sinn. Algebraic boundaries of convex semi-algebraic sets. Research in the Math-

ematical Sciences, 2(1):1, 2015. 5 [SS15] Rainer Sinn and Bernd Sturmfels. Generic spectrahedral shadows. SIAM Journal on Optimization, 25(2):1209–1220, 2015. 2, 7

[vBR09] Hans-Christian Graf von Bothmer and Kristian Ranestad. A general formula for the algebraic degree in semideﬁnite programming. Bulletin of the London Mathematical Society, 41(2):193–197, 2009. 2, 8, 10

