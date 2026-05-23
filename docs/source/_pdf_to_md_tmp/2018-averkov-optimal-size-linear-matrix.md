arXiv:1806.08656v3[math.OC]14Jan2019

# Optimal size of linear matrix inequalities in semideﬁnite approaches to polynomial optimization

Gennadiy Averkov∗ January 15, 2019

Abstract

The abbreviations LMI and SOS stand for ‘linear matrix inequality’ and ‘sum of squares’, respectively. The cone Σn,2d of SOS polynomials in n variables of degree at most 2d is known to have a semideﬁnite extended formulation

with one LMI of size n+nd . In other words, Σn,2d is a linear image of a set described by one LMI of size n+nd . We show that Σn,2d has no semideﬁnite extended formulation with ﬁnitely many LMIs of size less than n+nd . Thus, the standard extended formulation of Σn,2d is optimal in terms of the size of the LMIs. As a direct consequence, it follows that the cone of k × k symmetric positive semideﬁnite matrices has no extended formulation with ﬁnitely many LMIs of size less than k. We also derive analogous results for further cones considered in polynomial optimization such as truncated quadratic modules, the cones of copositive and completely positive matrices and the cone of sums of non-negative circuit polynomials.

## 1 Introduction

- 1.1 Semideﬁnite extended formulations


Consider the vector space Sk of k × k symmetric matrices over R and the cone S+k of positive semideﬁnite matrices in Sk. If A : Rn → Sk is an aﬃne map, say

A(x1,... ,xn) := A0 + x1A1 + ··· + xnAn, with A0,... ,An ∈ Sk, then the condition

A(x1,... ,xn) ∈ S+k

is called a linear matrix inequality (LMI) of size k on real-valued variables x1,... ,xn. Semideﬁnite programming (SDP) is optimization of a linear function subject to ﬁnitely many LMIs [WSV00, AL12]. Equivalently, SDP can also be described as optimization of a linear function over the intersection of an aﬃne subspace H of Sk

![image 1](<2018-averkov-optimal-size-linear-matrix_images/imageFile1.png>)

∗Institute of Mathematical Optimization, Faculty of Mathematics, Otto-von-GuerickeUniversit¨t Magdeburg, email: averkov@ovgu.de

with the cone S+k. Due to the stunning expressive power of LMIs, SDP has numerous applications across a wide range of subject areas [WSV00].

While SDP is known to be eﬃciently solvable – with a desired accuracy – under mild assumptions, the size of the LMIs is deﬁnitely an important limitation on the way to practical solvability [Mit03]. In order to successfully use SDP solvers, it is thus important to keep the size of the respective LMIs under control when modeling an underlying problem. The aim of this article is to address this size issue from the theoretical viewpoint. We are interested in understanding the limitation on the expressive power of the SDP implied by prescribing a size bound on the underlying LMIs. More concretely, we discuss semideﬁnite relaxations of problems in polynomial optimization.

Our aim is to study properties of the so-called semideﬁnite extended formulations of semialgebraic sets. We will use the general conic-programming framework from Gouveia et al. [GPT13] that allows to deal with various types of conic extended formulations in a uniform fashion. If K is a closed convex cone in a ﬁnite-dimensional R-vector space and S = π(K ∩H), where H is an aﬃne space and π is a linear map, then we say that S has a K-lift. For

K = (S+k)m = S+k × ··· × S+k

,

![image 2](<2018-averkov-optimal-size-linear-matrix_images/imageFile2.png>)

![image 3](<2018-averkov-optimal-size-linear-matrix_images/imageFile3.png>)

m

a set S having a K-lift is a linear image of a set that can be described by m LMIs of size k. In this case, we also say that S has a semideﬁnite extended formulation with m LMIs of size k.

Deﬁnition 1 (Semideﬁnite extension complexity and semideﬁnite extension degree). Let S be a subset of an R-vector space. We call the minimal k such that S has a S+klift the semideﬁnite extension complexity of S and denote this value by sxc(S). If S has no S+k-lift independently of the choice of k, we deﬁne sxc(S) := ∞. As a natural complement to sxc(S), we introduce the semideﬁnite extension degree sxdeg(S) of

- S to be the smallest k such that S has an (S+k )m-lift for some ﬁnite m. If S has no semideﬁnite extended formulation, we deﬁne sxdeg(S) := ∞.


Studying lower and upper bounds on sxc(S) is an active research area [GPT13, Sau15, FGP+15, FSP15, SP15, FSP16, SPW15, LRS15, GGS17, FSP17, AKW18, FSED18]. It is clear that sxdeg(S) ≤ sxc(S). We believe that, along with sxc(S), the value sxdeg(S) is an important parameter for quantifying tractability of semideﬁnite approaches to optimization of linear functions over S.

### 1.2 Convex cones in polynomial optimization

We brieﬂy revise some basic concepts and facts from polynomial optimization, see also [Mar08, Lau09, Las15].

In what follows, let m,n and k be positive integers and d a non-negative integer. Let x = (x1,... ,xn) and let R[x] be the ring of n-variate polynomials in variables x1,... ,xn with coeﬃcients in R. The subset

R[x]d := {f ∈ R[x] : deg f ≤ d} .

of R[x] is a vector space of dimension n+nd . A polynomial f ∈ R[x] is called sum of squares (SOS) if f = f12 + ··· + fr2 holds for ﬁnitely many polynomials f1,... ,fr ∈ R[x].

The following are the basic cones from real algebraic geometry and polynomial optimization:

Σn,2d := {f ∈ R[x]2d : f is SOS} , Pn,2d := {f ∈ R[x]2d : f ≥ 0 on Rn},

Pn,2d(X) := {f ∈ R[x]2d : f ≥ 0 on X} (X ⊆ Rn).

It is well-known [Las15, §2.1] that Σn,2d has the semideﬁnite extended formulation

Σn,2d = vn,d⊤ Avn,d : A ∈ S+k for k =

n + d n

, (1)

where vn,d is the vector

vn,d := (xα)|α|≤d (2)

of all monomials of degree at most d in n variables and the notation xα with α = (α1,... ,αn) ∈ Zn+ is used to denote the monomial

xα := xα11 ··· xαnn of degree

|α| := α1 + ··· + αn. Equality (1) implies

sxdeg(Σn,2d) ≤ sxc(Σn,2d) ≤

n + d n

. (3)

The lifted representation (1) of Σn,2d is a basic building block for the reduction of polynomial optimization problems to SDP problems. Due to the obvious inclusion

Σn,2d ⊆ Pn,2d, lower bounds on the unconstrained polynomial optimization problem inf

f(x) (f ∈ R[x]2d), (4)

x∈Rn

can be derived from the SOS relaxation of (4), which is the conic problem – with respect to the cone Σn,2d – formulated as

max{λ ∈ R : f − λ ∈ Σn,2d} . (5)

In view of (1), the condition f − λ ∈ Σn,2d in (5) can be reformulated as the linear constraint λ + vn,⊤2dAvn,d = f on the scalar decision variable λ ∈ R and the matrix decision variable A ∈ S+k of size k = n+dd . Reformulated like this, (5) becomes a semideﬁnite optimization problem.

For a general constrained polynomial optimization problem inf {f(x) : x ∈ Rn,g1(x) ≥ 0,... ,gk(x) ≥ 0} (f,g1,... ,gk ∈ R[x]) (6)

the approach is similar. Feasible solutions of (6) form the set X := {x ∈ Rn : g1(x) ≥ 0,... ,gk(x) ≥ 0} .

Choosing d with 2d ≥ deg f, one can reformulate (6) as the conic problem with respect to the cone Pn,2d(X):

inf {λ ∈ R : f − λ ∈ Pn,2d(X)} .

In constrained polynomial optimization, the principle of the SOS-based approaches is to ﬁnd a cone C contained in Pn,2d(X) that approximates Pn,2d(X) suﬃciently well and has a semideﬁnite extended formulation. Real algebraic geometry suggests various natural choices of C that are built upon Σn,2d. The so-called SOS hierarchies for (6) involve cones of the form

C = Σn,2d0 + g1Σn,2d1 + ··· + gkΣn,2dk (7)

with d0,... ,dk ∈ Z+ [Las15, §2.4.2 and §2.7.1]. We call the cone C given by (7) the truncated quadratic module generated by g1,... ,gs with the truncation degrees 2d0,... ,2dk. The standard approach is to ﬁrst choose the value d0 ∈ Z+ such that 2d0 is an upper bound on the degrees of the of the polynomials f,g1,... ,gk and then to ﬁx the largest possible values d1,... ,dk ∈ Z+ satisfying 2di + deg gi ≤ 2d0. The truncated modules with the above special choice of the truncation degrees generate the so-called SOS hierarchy, while the choice of d0 determines the level of the hierarchy.

- 1.3 Overview of results We address the following basic questions:


- (Q1) How large is sxdeg(C) for closed convex cones C satisfying Σn,2d ⊆ C ⊆ Pn,2d(X)?
- (Q2) How large is sxdeg(C) for C being a truncated quadratic module?


Our main theorem (Theorem 2) suggests an approach to lower-bounding sxdeg(C)

for the above cases. Using this approach, we can answer (Q1) and (Q2) in a variety of cases. Regarding (Q1), it should be mentioned that recent breakthrough results of Scheiderer [Sch18] provide various choices of convex semi-algebraic sets C, for which sxdeg(C) is inﬁnite. For example, sxdeg(Pn,2d) is inﬁnite if n,d ≥ 2 and (n,d) = (2,2) [Sch18, Corollary 4.25]. Our quantitative studies are in a certain sense complementary, because our objective is to determine sxdeg(C) in those cases, for which this value is ﬁnite. A recent contribution of Fawzi [Faw18] can be interpreted as a ﬁrst step in the study of quantitative aspects of (Q1). Arguments of Fawzi allow to determine sxdeg(S+k ) for k ≤ 3 and sxdeg(Σn,2d) for n = 1 and d ≤ 2. Regarding sxdeg(Σn,2d) in the case n = 1 and d ≤ 2, see also the exposition in [AHP+17].

In this paper, we determine sxdeg(S+k) and sxdeg(Σn,2d) for all k, n and d. We also determine the semideﬁnite extension degree of the truncated quadratic modules under a natural assumption.

Apart from SOS-based approaches, there has been a new approach to polynomial optimization based on the so-called SONC cone Cn,2d, considered in the work of Dressler et al. [DIdW19, DIdW17]. It has not been clear if this alternative approach has a semideﬁnite formulation. It turns out that this is indeed the case. Moreover, Cn,2d even has a second-order cone extended formulation. This can be expressed as the equality sxdeg(Cn,2d) = 2 in our notation.

The paper is organized as follows. In Section 2, we formulate and discuss the results. Section 3 provides background information, including the notation and two basic tools that we need for proving our main theorem (Theorem 2). Section 4 contains the proof of the main theorem. Section 5 presents proofs of the consequences of the main theorem. Section 6 deals with the SONC cone.

## 2 Results

### 2.1 Main theorem and its consequences

Lower bounds on the semideﬁnite extension degree of various speciﬁc convex cones that we discuss below will be obtained as a consequence of the following general result.

Theorem 2 (Main theorem). Let X ⊆ Rn be a set with non-empty interior. Let C ⊆ Pn,2d(X) be a closed convex cone such that there exist ﬁnite subsets S of X of arbitrarily large cardinality with the following property:

(∗) For every k-element subset T of S, some polynomial f in the cone C is equal

to zero on T and is strictly positive on S \ T. Then sxdeg(C) > k.

Specializing Theorem 2 to more concrete situations we obtain a number of corollaries. Their detailed proofs are given in Section 5. As mentioned in the introduction, SOS-based approaches to polynomial optimization use conic formulations based on cones C that lie between Σn,2d and Pn,2d(X). In view of Theorem 2, the semideﬁnite extension degree of such cones C is necessarily ‘large’. In the case Σn,2d ⊆ C ⊆ Pn,2d(X), choosing f in (∗) to be appropriate polynomials from Σn,2d, we arrive at

- Corollary 3. Let X ⊆ Rn be a set with non-empty interior and C be a closed convex cone satisfying Σn,2d ⊆ C ⊆ Pn,2d(X). Then

sxdeg(C) ≥

n + d n

.

Since Σn,2d has a semideﬁnite extended formulation with one LMI of size n+dd , the latter corollary allows to determine the exact values of the semideﬁnite extension degree and the semideﬁnite extension complexity for the cone Σn,2d:

- Corollary 4. sxdeg(Σn,2d) = sxc(Σn,2d) = n+nd .


Corollary 4 allows to determine the computational costs of solving the SOSrelaxation (5) of an unconstrained polynomial optimization problem by means of SDP.

Turning to constrained polynomial optimization, we determine the semideﬁnite extension degree of the truncated quadratic modules, which allows us to estimate the costs of solving a given level of the SOS hierarchy. The following corollary deals with the natural case when the set X of feasible solutions of the underlying optimization problem has non-empty interior.

- Corollary 5. Let g1,... ,gk ∈ R[x] \ {0} be such that the set X := {x ∈ Rn : g1(x) ≥ 0,... ,gk(x) ≥ 0}

has non-empty interior. Then, for the truncated quadratic module

C = Σn,2d0 + g1Σn,2d1 + ··· + gkΣn,2dk with d0,... ,dk ∈ Z+, one has

sxdeg(C) =

n + d n

,

where

d := max{d0,... ,dk}. The cone C in Corollary 5 has a straightforward semideﬁnite extended formula-

tion with k +1 LMIs of sizes n+nd0 ,... , n+ndk . The number n+nd is the maximum of these k + 1 sizes. By Corollary 5, the straightforward extended formulation is

optimal in terms of the size of the LMIs when X has non-empty interior. The case d = 1 of Corollary 4 yields the semideﬁnite extension degree of S+k:

- Corollary 6. sxdeg(S+k) = k.


Corollary 6 implies that the expressive power of the semideﬁnite optimization grows strictly with the growth of the size k of the underlying LMIs. In other words, the family of all convex semialgebraic sets that have a semideﬁnite extended formulation (we call such sets semideﬁnitely representable) can be decomposed into the hierarchy of the families

SDR(k) := {S ⊆ Rn : n ∈ N, sxdeg(S) ≤ k}

with each level of the hierarchy being strictly larger than the previous one. The lowest level SDR(1) of the hierarchy is just the family of all polyhedra. The family SDR(1) corresponds to linear optimization. The next level SDR(2) corresponds to the second-order cone programming, which is an important generalization of linear programming. The family SDR(2) can be characterized using the second-order cone

![image 4](<2018-averkov-optimal-size-linear-matrix_images/imageFile4.png>)

Lm := (x1,... ,xm) ∈ Rm : xm ≥ x21 + ··· + x2m−1

(for m = 1, we deﬁne Lm := R+).

Proposition 7 (Folklore; see the discussion in [Faw18]). For S ⊆ Rn, the following conditions are equivalent

- (i) sxdeg(S) ≤ 2.
- (ii) S has an (L3)m-lift for some m ∈ N.
- (iii) S has an Lm-lift for some m ∈ N.


Our results cover the following recent results as a special case. Aiming to demonstrate the discrepancy between the expressive power of second-order cone programming and semideﬁnite programming, Fawzi proved

- Theorem 8 (Fawzi [Faw18]). sxdeg(S+3 ) = 3.

In [Faw18], Fawzi also explains how to determine sxdeg(Σ1,4). Note that the cone Σ1,4 is not discussed in the arxiv version (arXiv:1610.04901) of Fawzi’s paper [Faw18]. Independently, Ahmadi et al. [AHP+17, Theorem 5] refer to the arxiv version of [Faw18] and provide a short argument that allows to determine sxdeg(Σ1,4) by reusing Fawzi’s proof of Theorem 8.

- Theorem 9 (Ahmadi et al. [AHP+17, Thm. 5], Fawzi [Faw18, Sec. 4]). sxdeg(Σ1,4) =


- 3.


The notation in [Faw18] and [AHP+17] is diﬀerent, but results from these sources

have a straightforward interpretation as a derivation of the equalities sxdeg(S+3 ) = 3 and sxdeg(Σ1,4) = 3. Theorems 8 and 9 are special cases of our Corollaries 6 and 4, respectively.

The proof of the lower bound sxdeg(S+3 ) ≥ 3 of Fawzi is based on the idea that a special face-incidence structure of the convex cone S+3 is an obstruction to having an (S+2 )m-lift with a small m. Combinatorial obstructions to having an Rm+lift are thoroughly studied in linear and discrete optimization [FKPT13], but for semideﬁnite optimization, the respective theory is not as developed yet, and Fawzi’s contribution is a ﬁrst step in this new direction. Since S+3 is a non-polyhedral cone, its face lattice is inﬁnite. The relevant face incidences of a given closed convex set S can be extracted from the so-called slack matrix of S. Loosely speaking, the slack matrix provides results f(s) of evaluation of all linear inequalities f ≥ 0 valid for S at all points s of S. Recently, Gouveia et al. [GPT13] developed a criterion for testing if a given convex set has a K-lift for convex cones K under some mild assumptions on K. Arguing by contradiction, Fawzi assumes the existence of (S+2 )m-lift for S+3 . He then applies the slack-matrix criterion from [GPT13] for K = (S+2 )m and gives a purely combinatorial graph-theoretic argument, which yields a lower bound on m. This lower bound on m depends on the number face-incidences of S+3 taken into account and can be made arbitrarily large by choosing suﬃciently many incidences.

Our proof approach to Theorem 2 is inspired by the arguments of Fawzi [Faw18]. Following his ideas, we also rely on the slack-matrix criterion provided in [GPT13]. The combinatorial argument from [Faw18] can be replaced by a direct application of Ramsey’s theorem for graphs. To prove Theorem 2, we use Ramsey’s theorem for k-uniform hypergraphs, with the case k = 2 corresponding to graphs.

Essentially, our proof of Corollary 4 is a generalization of the proof idea from [AHP+17, Section IV-B]. The extension for n = 1 and an arbitrary d from the case

n = 1,d = 2 considered in [AHP+17, Section IV-B] is rather straightforward, but for passing from n = 1 to an arbitrary n, somewhat more work is needed.

In view of Corollary 4, to determine sxdeg(Pn,2d), it suﬃces to combine a classical result of Hilbert with a recent result of Scheiderer.

- Theorem 10 (Hilbert [Hil88]). Σn,2d = Pn,2d ⇐⇒ n,d ≥ 2, (n,d) = (2,2).
- Theorem 11 (Scheiderer [Sch18, Corollary 4.25]). If n ≥ 2,d ≥ 2 and (n,d) = (2,2), then Pn,2d has no semideﬁnite extended formulation.


Directly combining Corollary 4, Theorem 10 and Theorem 11, we get Corollary 12.

sxdeg(Pn,2d) = sxc(Pn,2d) =

∞, if n,d ≥ 2, (n,d) = (2,2).

n+d

n , otherwise.

Results from [GPT13] imply that sxc(C) and sxdeg(C) are invariant under duality of cones: if C ⊆ Rn is a n-dimensional pointed closed convex cone, then

sxc(C) = sxc(C∗), (8) sxdeg(C) = sxdeg(C∗), (9)

where C∗ is the dual cone of C. Via dualization, Corollaries 3 and 4 yield a number of consequences. We introduce the moment cones

Mn,2d := cl(cone({vn,2d(x) : x ∈ Rn})), Mn,2d(X) := cl(cone({vn,2d(x) : x ∈ X}) (X ⊆ Rn),

where cl stands for the Euclidean topological closure and cone for the convex conic hull. Representability of the moment cones via S+k-lifts has been studied by Scheiderer:

Theorem 13 (Scheiderer [Sch18, Corollary 4.24]). Let X ⊆ Rn be a semi-algebraic set with non-empty interior and let n,d ≥ 2 and (n,d) = (2,2). Then Mn,2d(X) has no semideﬁnite extended formulation. In particular, Mn,2d has no semideﬁnite extended formulation, too.

If n = 1 or d = 1 or (n,d) = (2,2), Theorem 13 does not rule out the possibility of sxdeg(Mn,2d(X)) being ﬁnite. In these cases, the following consequence of

- Corollary 3 and (9) can be used to provide lower bounds on sxdeg(Mn,2d(X)):


- Corollary 14. For every X ⊆ Rn with non-empty interior,


sxdeg(Mn,2d(X)) ≥

n + d n

.

As a direct consequence of Corollary 3, (9) and Theorem 13 we also obtain the exact values of Mn,2d for all n and d:

- Corollary 15.

sxdeg(Mn,2d) = sxc(Mn,2d) =

∞, if n,d ≥ 2, (n,d) = (2,2),

n+d

n , otherwise. The cone

CPk := A ∈ Sk : x⊤Ax ≥ 0 for all x ∈ Rk+

is known as the cone of copositive matrices of size k. Its dual cone CP∗k is the closed convex cone generated by rank-one positive semideﬁnite matrices xx⊤ with

- x ∈ Rn+. Elements of CP∗k are called completely positive matrices. Note that various well-known hard combinatorial optimization problems can be modeled as conic op-


timization problems with respect to the cones CPk and CP∗k [Du¨r10]. We provide a lower bound the semideﬁnite extension degree of both cones and determine it exactly for small values of k:

- Corollary 16. One has sxdeg(CPk) = sxdeg(CP∗k) ≥ k, and the equality sxdeg(CPk) = sxdeg(CP∗k) = k holds if k ≤ 4.


The exact values sxdeg(CPk) for k > 4 are left undetermined. In fact, it is not even known if these values are ﬁnite [Sch18, §5.2].

From the above results we draw the conclusion that standard SOS-based approaches to polynomial optimization necessarily lead to semideﬁnite problems with large LMIs, which are usually hard to solve in practice. A solution to this issue could be to use sparsity or symmetry of underlying problems, if applicable; see [Las15, Ch. 8], [Nie15] and [AHP+17]. Alternatively, one can look for new ways of reduction of polynomial optimization problems to convex problems. There are a number of results in this direction [DPZ67, GM10, GM12, CS16, DIdW17, DIdW19, Dre18, CS17].

### 2.2 Results for the SONC cone

An alternative approach to polynomial optimization, suggested by Dressler et al. in [DIdW17, DIdW19, Dre18], is based on the cone Cn,2d of sums of non-negative circuit polynomials (abbreviated as SONC polynomials) in n variables of degree at most

- 2d. As reported in [DIdW19], the optimization approach based on Cn,2d leads to convex problems that frequently can be solved eﬃciently in practice. Furthermore, this alternative approach seems to be not as sensitive to the choice of n and d as the well-known approach based on Σn,2d [SdW18].


We transform the original deﬁnition of Cn,2d, which is given Section 6, to a less

technical deﬁnition more suitable for our purposes. For a ﬁnite set A ⊆ Zn+, we ﬁrst introduce the cone

Pn,A := f =

fαxα : f ≥ 0 on Rn . (10)

α∈A

of non-negative polynomials f with the support {α : fα = 0} of f contained in A. While for an arbitrary A, it is hard to ﬁnd an explicit description of Pn,A in terms of the coeﬃcients fα of the polynomial f, there are special cases of ‘sparse’ sets A, in

which such a description is known. If the convex hull of A is a k-dimensional simplex with vertices α(0),... ,α(k) belonging to (2Z+)n and A consists of the k +1 vertices of this simplex and another point β that lies in the relative interior of the simplex, then Pn,A has a simple inequality description derivable from the weighted arithmeticgeometric mean inequality. We denote by An,2d the family of all A having the special form as above and satisfying the inclusion A ⊆ α ∈ Zn+ : |α| ≤ 2d . The inclusion for A ensures Pn,A ⊆ Pn,2d for every A ∈ An,2d so that one has Cn,2d ⊆ Pn,2d. It turns out that the SONC cone Cn,2d can be represented as the sum

Cn,2d =

Pn,A.

A∈An,2d

The following theorem provides theoretical support to the informal message that Cn,2d is ‘practically tractable’. The smallest possible semideﬁnite extension degree for a non-polyhedral cone is two. The following result shows that the semideﬁnite extension degree of Cn,2d is that small, independently of the choice of n and d. A wellknown result of Ben-Tal and Nemirovski [BTN01, §§2.3.5] shows that the hypograph of a weighted geometric-mean function with rational weights has a second-order cone extended formulation. Directly applying this fact to the explicit inequality description of the cones sxdeg(Pn,A) = 2 occurring in the above description of Cn,2d we obtain

Theorem 17. For all n,d ∈ N, one has sxdeg(Cn,2d) = 2. By Proposition 7 and Theorem 17, the SONC relaxation inf {λ ∈ R : f − λ ∈ Cn,2d} (11)

of the unconstrained polynomial optimization problem (4) can be formulated as a second-order cone problem. While sxdeg(Cn,2d) remains the same for all n and d, the cone Cn,2d does become more complex with the growth of n and d. It would also be interesting to study sxc(Cn,2d) and to determine the number of constraints needed in a second-order cone or semideﬁnite extended formulation of Cn,2d. Such studies would shed light on how to formulate (11) compactly in the paradigms of semideﬁnite and second-order programming.

In [IdW16, Prop. 7.2] it was shown that Cn,2d and Σn,2d are not comparable with respect to inclusion for n,d ≥ 2, (n,d) = (2,2). So, the cone Σn,2d +Cn,2d is strictly larger than both Σn,2d and Cn,2d for these choices of (n,d), which implies that the SOS+SONC relaxation

inf {λ ∈ R : f − λ ∈ Σn,2d + Cn,2d} (12)

of (4) is a stronger relaxation than both the SOS relaxation and the SONC relaxation.

The following corollary addresses the question on the relation between Pn,2d and Σn,2d + Cn,2d, which was formulated in the PhD thesis [Dre18, p. 134] of Mareike Dressler and asked by Raman Sanyal during the defense of her thesis. Above

results imply that the cone Σn,2d+Cn,2d always has a semideﬁnite extended formulation, while in view of Scheiderer’s result, the cone Pn,2d has a semideﬁnite extended formulation only in the cases of equality Σn,2d = Pn,2d, which was characterized by Hilbert. This yields

Corollary 18. For all n,d ∈ N, one has: Σn,2d + Cn,2d = Pn,2d ⇐⇒ n,d ≥ 2, (n,d) = (2,2). Corollary 18 shows that, in general, (12) is not equivalent to the original problem

(4).

## 3 Background material

### 3.1 Basic notation and terminology

Let N := {1,2,3,...} be the set of all positive integers. We use Z+ resp. R+ to denote the set of non-negative integer resp. real values. Let [k] := {1,... ,k} for k ∈ N and [k] := ∅ for k = 0. The cardinality of a set X is denoted by |X|. Given a set X and a non-negative integer k ≥ 0, we denote by Xk the set of all k-element subsets of X. If X1,... ,Xr are ﬁnitely many sets in a vector space, the sum of X1,... ,Xr is introduced as

X1 + ··· + Xr := {u1 + ··· + ur : u1 ∈ X1,... ,ur ∈ Xr} . If g ∈ R and C ⊆ Rn or g ∈ R[x] and C ⊆ R[x], we use the notation

gC := {gp : p ∈ C}.

If A is a matrix, then A⊤ denotes the transpose of A. Vectors are interpreted as columns in matrix expressions. The image of a matrix A ∈ Rm×n is im(A) := {Ax : x ∈ Rn}.

### 3.2 Euclidean spaces and convex sets

We endow the space Rn with the standard scalar product x, y := x⊤y. Two linear subspaces X of Y of Rn are said to be orthogonal if x, y = 0 holds for all x ∈ X and y ∈ Y . In the space Sk of k × k symmetric matrices over R we introduce the scalar product of A = (aij)i,j∈[k] and B = (bij)i,j∈[k] by

A, B :=

aijbij.

i,j∈[k]

The set S+k is the convex closed cone of positive semideﬁnite matrices in Sk. For x,y ∈ Rk the rank-one symmetric matrices xx⊤,yy⊤ ∈ S+k satisfy the relation

xx⊤ , yy⊤ = x, y 2 . (13)

We endow the space (Sk)m of m-tuples of k × k symmetric matrices with the scalar product

m

A, B :=

Ai , Bi

i=1

for A = (A1,... ,Am),B = (B1,... ,Bm) ∈ (Sk)m.

By cone we denote the convex conic hull and by cl the topological closure with respect to the Euclidean topology. For a non-empty set X ⊆ Rn, we deﬁne the conic dual [Roc97] of X by

X∗ := {y : x, y ≥ 0 for all x ∈ X} . It is well-known that

(X∗)∗ = cl(cone(X)) (14) holds for all X with ∅ = X ⊆ Rn. The conic dual is introduced in the same way in an arbitrary Euclidean space, in particular, in (Sk)m. It is known that S+k is self-dual, that is, (S+k)∗ = S+k [BTN01, Thm. A.7.6]. This implies that (S+k)m is self-dual, too.

We call a convex cone C in Rn pointed if there exists u ∈ Rn\{0} with u, x ≥ 0 for all x ∈ C and such that {x ∈ C : u, x = 0} = {0}. If C is pointed, and u a vector as above, then {x ∈ C : u, x = 1} is a bounded aﬃne slice of C. The cones Σn,2d,Pn,2d and Pn,2d(X), with X ⊆ Rn having non-empty interior, are known to be pointed, closed and full-dimensional within the vector space R[x]2d.

### 3.3 Tools

The following result is contained, albeit in somewhat diﬀerent wording, in [GPT13]. Theorem 19 (Gouveia et al. [GPT13]). Let C ⊆ Rn be a closed convex cone and let K = (S+k )m. Then the following conditions are equivalent:

- (i) C has a K-lift.
- (ii) For every x ∈ C there exist Ax ∈ K and for every y ∈ C∗ there exists By ∈ K such that the equality


x, y = Ax , By holds for all x ∈ C and y ∈ C∗.

- Remark 20. One can rephrase the results about K-lifts of n-dimensional compact convex sets from [GPT13] as results about K-lifts of n-dimensional pointed closed convex cones. With this interpretation, it can be seen that Theorem 19 in the case of n-dimensional pointed convex cones is covered by Remark 2.3, Theorem 2.4 and Corollary 2.6 in [GPT13]. Note also that Corollary 2.6 is about K-lifts of so-called


nice cones K. The cone K = (S+k)m in Theorem 19 is nice, because S+k is known to be a nice cone; see the comment following Corollary 2.6 in [GPT13].

We also sketch how to deduce the assertion of Theorem 19 for general convex cones from the case of n-dimensional pointed convex cones. If C is not fulldimensional or not pointed, then passing to appropriate coordinates, we can assume C = C0 × Rs × {0}t, where the cone C0 is (n − s − t)-dimensional and pointed. It is not hard to see that C has a K-lift if and only if C0 has a K-lift. One has C∗ = C0∗ × {0}s × Rt. Thus, each scalar product x, y with x ∈ C and y ∈ C∗, occurring in (ii), can be written as x, y = x0 , y0 where x0 ∈ C0 is a vector of the ﬁrst n − s − t components of x and y0 ∈ C0∗ is a vector of the ﬁrst n − s − t components of y. Conversely, each x0 ∈ C0 and y0 ∈ C0 yield vectors x ∈ C and

- y ∈ C∗ with x0 , y0 = x, y . This shows that condition (ii) holds for the cone C if


and only if it holds for the cone C0. Thus, equivalence (i) ⇐⇒ (ii) for the general cone C is derived from the same equivalence for the cone C0.

- Remark 21. Equalities (8) and (9) from the introduction follow from Theorem 19.


Ramsey’s theory is another powerful tool that we use in our proofs. Quoting T. S. Motzkin, one can describe Ramsey type results as assertions that the “complete disorder is impossible” [GRS90, Ch. 2]. The most well-known version of Ramsey-type theorems is concerned with edge colorings of complete graphs. It can be illustrated by the following example. If we color each edge of the complete graph on six nodes with one of the two given colors, then – no matter how we choose the coloring – our colored graph will always contain a monochromatic triangle. This observation is a special case of the Ramsey theorem for graphs: if, for given c ∈ N and n ∈ N, the edges of the complete graph on N nodes are colored with c colors then the graph will contain a complete monochromatic subgraph on n nodes whenever N is large enough. For the above example, the ‘input’ of the Ramsey theorem is the number c = 2 of colors and the size n = 3 of the ordered substructure that we want to discover in the overall structure, while N = 6 is a possible ‘output’, giving the size of the overall structure suﬃcient for guaranteeing the existence of an ordered substructure of the desired size. In our arguments, we will need the Ramsey theorem for hypergraphs, which is a natural generalization of Ramsey’s theorem for graphs from the case of the complete graph [N2] to the case of the complete k-uniform hyperpgraph [Nk] :

Theorem 22 (Ramsey’s theorem for hypergraphs [GRS90]). Let k,n,c ∈ N. Then there exists N ∈ N with the following property: for every map F : [Nk] → [c] there exists a subset W of [N] of cardinality n such that F is constant on Wk .

Theorem 22 is a generalization of Ramsey’s theorem for graphs from k = 2 to an arbitrary k. We denote the minimal N in Theorem 22 by Rk(n;c). The value Rk(n;c) is the so-called Ramsey number for k-uniform hypergraphs. In the context of Theorem 22, F(T) is usually called the color assigned to T ∈ [Nk] .

- 4 Proof of Theorem 2 We give an outline of the proof of Theorem 2. In what follows, we will use


Remark 23. The vector spaces R[x]d and R(n+nd) can be identiﬁed via the identiﬁcation of f = |α|≤d fαxα with the vector (fα)|α|≤d. This allows us to write the evaluation f(x) of f at x ∈ Rn as the scalar product f(x) = f , vn,d(x) , using the vector vn,d of monomials deﬁned by (2), and to consider dual cones C∗ ⊆ R(n+nd) of closed convex cones C ⊆ R[x]d.

To highlight the relevant combinatorial convex geometry exploited in the proof of Theorem 2, we introduce the following notion. We call a subset S of a n-dimensional closed convex set C ⊆ Rn a k-neighborly conﬁguration in C if, for each k-element subset T of S, there exists a supporting hyperplane H of C satisfying H ∩ S = T. This notion is strongly related to the well-known notion of k-neighborly polytope

from polyhedral combinatorics. We recall that a k-neighborly polytope is a polytope with every set of k or fewer vertices forming a face [Zie95] .

Remark 23 implies that for the cone C ⊆ Pn,2d(X), the vector vn,2d(s) belongs to the dual cone C∗ for every s ∈ X. Consequently, if C had a (S+k )m-lift, then by Theorem 19, one would have f(s) = f , vn,2d(s) = Af , Bt for all f ∈ C and all

- s ∈ X with appropriate choices of Af ∈ (S+k )m,Bs ∈ (S+k )m. Our proof uses the zero-pattern in the decomposition f(s) = Af , Bs . This means that we only make use of the distinction between f(s) = 0 and f(s) > 0. A set S ⊆ X satisfying (∗)


gives rise to polynomials fT ∈ C with T ∈ Sk that satisfy fT(s) = 0 for s ∈ T and fT(s) > 0 for s ∈ S \ T. Interpreting fT(s) as fT , vn,2d(s) , the latter implies that set {vn,2d(s) : s ∈ S} is a k-neighborly point conﬁguration of the cone C∗.

The crucial step of the proof is to show that, if C has a (S+k )m-lift, then C∗ cannot contain a k-neighborly conﬁguration of an arbitrarily large cardinality. The proof does not explicitly use the notion of k-neighborly conﬁguration, but this notation allows to ‘visualize’ what is happening in convex-geometric terms. The derivation of an upper bound on the size of a k-neighborly conﬁguration is carried out in

- Lemma 26 in a somewhat more abstract setting that uses only AT := AfT for


- T ∈ Sk and Bt with t ∈ S and does not explicitly involve the cone C. Note that for deciding whether AT , Bt = 0 is fulﬁlled, one does not need the whole knowledge of AT and Bt. If AT = (AT,1,... ,AT,m) and Bt = (Bt,1,... ,Bt,m), then it is easy to check that condition AT , Bt = 0 holds if and only if im(AT,i) is orthogonal to the image of im(Bt,i) for every i ∈ [m] (see Lemma 25). Thus, the only information we need about AT,i and Bt,i is the knowledge of their images.


The condition fT(s) = 0 implies that im(AT,i) is orthogonal to the space UT,i :=

t∈T im(Bt,i). Thus, UT,i is an obstruction to the choice of im(Af,i). The tuple (UT,1,... ,UT,m) of m vector spaces is a label of the hyperedge T ∈ Sk in the hypergraph Sk . As we do not have any particular information about the labeling T ∈ Sk  → (UT,1,... ,UT,m), it ‘looks’ like a completely unordered structure to us. The lack of the order can be eliminated by applying Ramsey’s theorem and passing to an ordered substructure. Using Ramsey’s theorem for hypergraphs (Theorem 22), we are able to show that, if S is large enough, then within some smaller hyperpgraph

- W k on a set W ⊆ S of k+1 nodes, the hyperedge T has the same label (U1,... ,Um)


for every T ∈ Wk . Once the existence of W as above is established, one can easily derive a contradiction and conclude the proof.

We now proceed with detailed arguments.

- Lemma 24. Let U1,... ,Un be linear subspaces of Rk and let U := ni=1 Ui. Then there exists a subset I ⊆ [n] with |I| ≤ k such that U = i∈I Ui.

Proof. Pick a basis b1,... ,bm of U from the set U1 ∪ ... ∪ Uk and then ﬁx for each i ∈ [m] an index ji ∈ [n] with bi ∈ Uji. It is clear that the assertion holds for I = {j1,... ,jm}.

![image 5](<2018-averkov-optimal-size-linear-matrix_images/imageFile5.png>)

![image 6](<2018-averkov-optimal-size-linear-matrix_images/imageFile6.png>)

![image 7](<2018-averkov-optimal-size-linear-matrix_images/imageFile7.png>)

![image 8](<2018-averkov-optimal-size-linear-matrix_images/imageFile8.png>)

- Lemma 25. Let A,B ∈ S+k. Then A, B = 0 holds if and only if im(A) is orthogonal to im(B).


Proof. Let a1,... ,ak be a basis of Rk consisting of eigenvectors of A corresponding to the eigenvalues λ1 ≥ ... ≥ λr > λr+1 = ... = λk = 0. Analogously, let b1,... ,bk

be a basis of Rk consisting of eigenvectors of B corresponding to the eigenvalues µ1 ≥ ... ≥ µs > µs+1 = ... = µk = 0. Then im(A) is linearly spanned by a1,... ,ar and im(B) is linearly spanned by b1,... ,bs. Furthermore, one has

r

λiaia⊤i and B =

A =

i=1

s

µjbjb⊤j .

j=1

In view of (13), the latter representations imply

A, B =

r

s

λiµj ai , bj 2 .

i=1

j=1

Consequently, A, B = 0 holds if and only if ai , bj = 0 holds for all i ∈ [r] and all j ∈ [s]. This gives the assertion.

![image 9](<2018-averkov-optimal-size-linear-matrix_images/imageFile9.png>)

![image 10](<2018-averkov-optimal-size-linear-matrix_images/imageFile10.png>)

![image 11](<2018-averkov-optimal-size-linear-matrix_images/imageFile11.png>)

![image 12](<2018-averkov-optimal-size-linear-matrix_images/imageFile12.png>)

- Lemma 26 (Key lemma). Let S be a set of cardinality at least k and let AT ∈ (S+k)m,


with T ∈ Sk , and Bs ∈ (S+k)m, with s ∈ S, be such that the condition AT , Bs = 0 holds if and only if s ∈ T. Then

|S| < Rk(k + 1;(k + 1)m). Proof. The proof relies on Theorem 22. Let

S k

AT = (AT,1,... ,AT,m) for T ∈

, Bs = (Bs,1,... ,Bs,m) for s ∈ S.

For T ∈ Sk and i ∈ [m], consider UT,i :=

im(Bt,i) (15)

t∈T

and let

dT,i := dim(UT,i). We view {0,... ,k}m as a set of (k + 1)m colors and assign color (dT,1,... ,dT,m) ∈ {0,... ,k}m to the set T ∈ Sk .

Assuming |S| ≥ Rk(k + 1;(k + 1)m), we will arrive at a contradiction. By the deﬁnition of Rk(k + 1,(k + 1)m), there exists a subset W of S of cardinality k + 1 such that all elements of Wk are colored with the same color. This means, for some color (d1,... ,dk) ∈ {0,... ,k}m, one has dT,i = di for all i ∈ [m] and T ∈ Wk . Thus, when T ∈ Wk , the dimension of the vector space UT,i does not depend on T. We show that for T ∈ Wk , the vector space UT,i itself is independent of T ∈ Wk . This means, we will verify the following

Claim. For some vector spaces U1,... ,Um ⊆ Rk, one has UT,i = Ui for all i ∈ [k] and T ∈ Wk .

If the claim was false, then we had UT1,i = UT2,i for some i ∈ [k] and T1,T2 ∈ Wk . Hence, UT1,i and UT2,i are proper subspaces of UT1,i+UT2,i so that dim(UT1,i+UT2,i) > di holds. By (15),

im(Bt,i). (16)

UT1,i + UT2,i =

t∈T1∪T2

Lemma 24, applied to the right-hand side of (16), yields the existence of T′ ⊆ T1∪T2 with |T′| ≤ k such that

UT1,i + UT2,i =

im(Bi,t).

t∈T′

The set T′ ⊆ T1 ∪ T2 ⊆ W is a subset of some T′′ ∈ Wk . We thus arrive at dT′′,i = dim(UT′′,i) ≥ dim(UT1,i + UT2,i) > di, which contradicts dT′′,i = di. This concludes the proof of the claim.

Since W has cardinality k+1, we can choose an arbitrary decomposition W = T∪ {s}, where T ∈ Wk and s ∈ W \T. The equalities mi=1 AT,i , Bt,i = AT , Bt = 0 for t ∈ T and the inequalities AT,i , Bt,i ≥ 0 for i ∈ [m] yield AT,i , Bt,i = 0 for all t ∈ T and i ∈ [m]. By Lemma 25, im(AT,i) is orthogonal to im(Bt,i). Since

- t ∈ T is arbitrary, we conclude that im(AT,i) is orthogonal to t∈T im(Bt,i) = Ui. By the choice of Ui, the linear space Ui contains all im(Bw,i) with w ∈ W as a subspace. Hence, im(AT,i) is orthogonal to im(Bs,i). By Lemma 25, this means that


AT,i , Bs,i = 0 holds for all i ∈ [m]. Thus, we have shown AT , Bs = 0. Since s  ∈ T, this contradicts the assumptions and yields the desired assertion.

![image 13](<2018-averkov-optimal-size-linear-matrix_images/imageFile13.png>)

![image 14](<2018-averkov-optimal-size-linear-matrix_images/imageFile14.png>)

![image 15](<2018-averkov-optimal-size-linear-matrix_images/imageFile15.png>)

![image 16](<2018-averkov-optimal-size-linear-matrix_images/imageFile16.png>)

Proof of Theorem 2. It is clear that vn,2d(x), for x ∈ X, belongs to C∗. Indeed, the inclusion C ⊆ Pn,2d(X) implies 0 ≤ f(x) = f , vn,d(x) for all f ∈ C. We ﬁx an arbitrary m ∈ N and show that C has no (S+k)m-lift. Let

N = Rk(k + 1,(k + 1)m)

and consider a set S of cardinality N satisfying (∗). For every T ∈ Sk , choose a polynomial fT ∈ C which is equal to 0 on T and is strictly positive on S \ T. If C had a (S+k )m-lift, then by the implication (i) ⇒ (ii) of Theorem 19, there would exist AT ∈ (S+k )m with T ∈ Sk and Bs ∈ (S+k)m with s ∈ S such that

fT(s) = fT , vn,2d(s) = AT , Bs

holds for all T ∈ Sk and s ∈ S. By construction, AT , Bs = 0 holds if and only if s ∈ T. Thus, assumptions of Lemma 26 are fulﬁlled, and Lemma 26 implies

|S| < Rk(k + 1,(k + 1)m) = N, which is a contradiction to |S| = N. This shows that C has no (S+k)m-lift.

![image 17](<2018-averkov-optimal-size-linear-matrix_images/imageFile17.png>)

![image 18](<2018-averkov-optimal-size-linear-matrix_images/imageFile18.png>)

![image 19](<2018-averkov-optimal-size-linear-matrix_images/imageFile19.png>)

![image 20](<2018-averkov-optimal-size-linear-matrix_images/imageFile20.png>)

## 5 Proofs of the consequences of Theorem 2

We outline the proof Corollary 3. The corollary follows from Theorem 2 by verifying the condition (∗) for k = n+nd −1 and appropriately chosen polynomials f. In view of the assumption Σn,2d ⊆ C in Corollary 3 one can choose polynomials f in (∗) to be squares. Thus, we need to ﬁnd arbitrarily large S ⊆ X such that for every k-element subset T of S there exists a polynomial which is equal to zero on T and is not equal to zero on all points of S \ T. Taking f in (∗) to be the square of such polynomial, we are able to verify the assumptions of Theorem 2 and obtain sxdeg(C) > k.

The construction of sets S and the choice of polynomials vanishing on T and not vanishing on S \ T relies on the following Lemmas 27 and 28. We say that a set V of vectors in Rn is in general linear position if every subset of V of cardinality at most n is linearly independent.

- Lemma 27. Let N ∈ N and N ≥ n+nd . Then the following hold:

- (a) The set of all (x1,... ,xN) ∈ (Rn)N such that {vn,d(x1),... ,vn,d(xN)} is a set of N vectors in general linear position, is dense in (Rn)N in the Euclidean topology.
- (b) If {x1,... ,xN} is an N-element subset of Rn such that the set {vn,d(x1),... ,vn,d(xN)} is in general linear position, then every non-zero polynomial f ∈ R[x]d is equal to zero on at most n+nd − 1 points of {x1,... ,xN}.


Proof. (a): Let k := n+nd . For every I = {i1,... ,ik} ∈ [Nk] with 1 ≤ i1 < ... ≤ ik ≤ N, consider

DI(x1,... ,xN) := det(vn,d(xi1),... ,vn,d(xik)).

Clearly, DI(x1,... ,xN) can be viewed as a polynomial in Nn variables. Note that DI(x1,... ,xN) is a non-zero polynomial, as by Leibniz formula, it involves exactly k! distinct monomials. It follows that DI(x1,... ,xN) is non-zero on an open dense subset of (Rn)N. Consequently, all DI(x1,... ,xN) with I ∈ [Nk] are simultaneously not equal to zero on a dense subset of (Rn)N.

(b): Assume that vn,d(x1),... ,vn,d(xN) are in general position. If f ∈ R[x]d vanishes on a k-element set {xi1,... ,xik}, then f(xi1) = ··· = f(xik) = 0. This condition on f, can be viewed as a homogeneous linear system with k equalities in k variables, by interpreting f as an element of Rk. The linearly independent vectors vn,d(xi1),... ,vn,d(xik) form the left hand side of this system. We thus conclude that f = 0.

![image 21](<2018-averkov-optimal-size-linear-matrix_images/imageFile21.png>)

![image 22](<2018-averkov-optimal-size-linear-matrix_images/imageFile22.png>)

![image 23](<2018-averkov-optimal-size-linear-matrix_images/imageFile23.png>)

![image 24](<2018-averkov-optimal-size-linear-matrix_images/imageFile24.png>)

- Lemma 28. For every subset S of Rn of cardinality at most n+nd − 1 there exists a non-zero polynomial f ∈ R[x]d, which is equal to zero on S.


Proof. Since the dimension of R[x]d is k = n+nd the conditions f(s) = 0 for all s ∈ S can be viewed as an under-determined homogeneous linear system in the

coeﬃcients of f. This implies that there exists a non-zero polynomial f as in the assertion.

![image 25](<2018-averkov-optimal-size-linear-matrix_images/imageFile25.png>)

![image 26](<2018-averkov-optimal-size-linear-matrix_images/imageFile26.png>)

![image 27](<2018-averkov-optimal-size-linear-matrix_images/imageFile27.png>)

![image 28](<2018-averkov-optimal-size-linear-matrix_images/imageFile28.png>)

- Proof of Corollary 3. Let N be an arbitrary integer with N ≥ k := n+nd − 1. By

Lemma 27, there exist x1,... ,xN ∈ X such that {vn,d(x1),... ,vn,d(xN)} is an Nelement set in general linear position. Let S = {x1,... ,xN}. By Lemma 28, for

every T ∈ Sk there exists a non-zero polynomial fT ∈ R[x]d equal to zero on T. In view of Lemma 27, fT is not equal to zero on S \T. The square fT2 of fT belongs to Σn,2d and by this also to C. Since N is chosen arbitrarily, assumptions of Theorem 2 are fulﬁlled. We thus conclude that sxdeg(C) > k.

![image 29](<2018-averkov-optimal-size-linear-matrix_images/imageFile29.png>)

![image 30](<2018-averkov-optimal-size-linear-matrix_images/imageFile30.png>)

![image 31](<2018-averkov-optimal-size-linear-matrix_images/imageFile31.png>)

![image 32](<2018-averkov-optimal-size-linear-matrix_images/imageFile32.png>)

- Remark 29. In the case n = 1, in the above proof, one could also choose x1,... ,xN ∈

X to be arbitrary distinct values and ﬁx fT :=

t∈T

(x − t) ∈ R[x]

This was also the choice used for deriving the lower bound sxdeg(Σ1,4) ≥ 3 in [AHP+17, Sect. IV-B].

- Remark 30. In the case d = 1, in the above proof, vn,1(x) ∈ Rn+1 is obtained from x ∈ Rn by appending a component 1. So, one can choose


xi = (x∗ + t1i,... ,x∗ + tni )

using a point x∗ in the interior of X and N distinct values t1,... ,tN ∈ R that are suﬃciently close to zero. With this choice, the set {vn,1(x1),... ,vn,1(xN)} of N vectors is in general linear position. The latter can be seen by observing that det(vn,1(xi1),... ,vn,1(xin+1)) is the Vandermonde determinant.

Applying Corollary 3 in the case C = Σn,2d, we determine sxdeg(Σn,2d) and sxc(Σn,2d):

- Proof of Corollary 4. As mentioned in the introduction, the inequalities


sxdeg(Σn,2d) ≤ sxc(Pn,2d) ≤

n + d n

are known. Applying Corollary 3 for C = Σn,2d, we get sxdeg(Σn,2d) ≥ n+nd .

![image 33](<2018-averkov-optimal-size-linear-matrix_images/imageFile33.png>)

![image 34](<2018-averkov-optimal-size-linear-matrix_images/imageFile34.png>)

![image 35](<2018-averkov-optimal-size-linear-matrix_images/imageFile35.png>)

![image 36](<2018-averkov-optimal-size-linear-matrix_images/imageFile36.png>)

Truncated quadratic modules are sums of ﬁnitely many cones. To determine the semideﬁnite extension degree of the truncated quadratic modules, we ﬁrst make an observation on how the semideﬁnite extension degree behaves with respect to taking sums:

- Lemma 31. Let C1,... ,Ck ⊆ Rn. Then sxdeg(C1 + ··· + Ck) ≤ max{sxdeg(Ci) : i = 1,... ,k} .


Proof. This follows directly from the fact that C1 + ··· + Ck is a linear image of C1 × ··· × Ck under the linear map (u1,... ,uk)  → u1 + ··· + uk acting from (Rn)k to Rn.

![image 37](<2018-averkov-optimal-size-linear-matrix_images/imageFile37.png>)

![image 38](<2018-averkov-optimal-size-linear-matrix_images/imageFile38.png>)

![image 39](<2018-averkov-optimal-size-linear-matrix_images/imageFile39.png>)

![image 40](<2018-averkov-optimal-size-linear-matrix_images/imageFile40.png>)

As we will see in the proof of Corollary 5, for cones occurring in the deﬁnition of the truncated quadratic module and under assumptions of Corollary 5, the inequality in Lemma 31 is in fact an equality. The proof of Corollary 5 reuses the proof approach of Corollary 3.

- Proof of Corollary 5. Let g0 := 1 and Ci := giΣn,2di for i = 0,... ,d. In this notation, one has C = C0+···+Ck. Since the cone Ci is linearly isomorphic to Σn,2di for

each i = 0,... ,k and since the semideﬁnite extension degree of Σn,2di is determined by Corollary 4, taking into account Lemma 31, we obtain the upper bound

sxdeg(C) ≤ max{sxdeg(Ci) : i = 0,... ,k}

= max{sxdeg(Σn,2di) : i = 0,... ,k}

=

n + d n

on sxdeg(C). We can adapt the proof of Corollary 3 to derive the matching lower bound sxdeg(C) ≥ n+nd . Fix i = 0,... ,k with di = d. Since gi is not a zero polynomial, the set {x ∈ X : gi(x) = 0} is n-dimensional. Thus, we can ﬁx arbitrarily many points x1,... ,xN with N ≥ n+nd − 1 as in the proof of Corollary 3 that satisfy the additional assumption gi(xj) = 0 for j ∈ [N]. The polynomials fT with T ⊆ S and |T| = n+nd − 1 from the proof of Corollary 3 give rise to polynomials gifT2 in Ci that vanish on T and are strictly positive on S \T. In view of Theorem 2, we get sxdeg(C) ≥ n+nd .

![image 41](<2018-averkov-optimal-size-linear-matrix_images/imageFile41.png>)

![image 42](<2018-averkov-optimal-size-linear-matrix_images/imageFile42.png>)

![image 43](<2018-averkov-optimal-size-linear-matrix_images/imageFile43.png>)

![image 44](<2018-averkov-optimal-size-linear-matrix_images/imageFile44.png>)

To prove Corollary 6, it suﬃces to observe that S+k is linearly isomorphic to Σk−1,2:

- Proof of Corollary 6. We assume k ≥ 2, as otherwise the assertion is trivial. Consider the maps A  → qA  → fA given by


qA(x) := x⊤Ax, fA(x1,... ,xk−1) := qA(x1,... ,xk−1,1).

It is straightforward to see that A  → fA is a linear bijection acting from Sk to R[x1,... ,xk−1]2 that maps S+k onto Σk−1,2. Thus, the assertion follows by applying

- Corollary 4 for d = 1 and n = k − 1.


![image 45](<2018-averkov-optimal-size-linear-matrix_images/imageFile45.png>)

![image 46](<2018-averkov-optimal-size-linear-matrix_images/imageFile46.png>)

![image 47](<2018-averkov-optimal-size-linear-matrix_images/imageFile47.png>)

![image 48](<2018-averkov-optimal-size-linear-matrix_images/imageFile48.png>)

The cases of equality Pn,2d = Σn,2d are characterized by a classical result of Hilbert, while Scheiderer’s result result shows that, in the case Pn,2d = Σn,2d, the cone Pn,2d has no semideﬁnite extended formulation. In Corollary 12, we use these results and the knowledge of sxdeg(Σn,2d) to determine sxdeg(Pn,2d).

Proof of Corollary 12. If n,d ≥ 2 and n,d = (2,2), Theorem 11 of Scheiderer implies sxdeg(Pn,2d) = sxc(Pn,2d) = ∞. Otherwise, by Theorem 10 of Hilbert, Pn,2d = Σn,2d. Thus, sxdeg(Pn,2d) = sxc(Pn,2d) = n+nd follows using Corollary 4.

![image 49](<2018-averkov-optimal-size-linear-matrix_images/imageFile49.png>)

![image 50](<2018-averkov-optimal-size-linear-matrix_images/imageFile50.png>)

![image 51](<2018-averkov-optimal-size-linear-matrix_images/imageFile51.png>)

![image 52](<2018-averkov-optimal-size-linear-matrix_images/imageFile52.png>)

Corollaries 14 and 15 are obtained through straightforward dualization. Moment cones are known to be dual to cones of non-negative polynomials:

- Lemma 32 (Folklore). Pn,2d(X)∗ = Mn,2d(X) for every X ⊆ Rn. In particular, Pn,∗2d = Mn,2d.


Proof. Writing evaluation of f at x ∈ Rn as the scalar product f(x) = f , vn,2d(x) , we obtain Pn,2d(X) = ({vn,2d(x) : x ∈ X})∗. Dualizing the latter equation and using (14), we get Pn,2d(X)∗ = Mn,2d(X).

![image 53](<2018-averkov-optimal-size-linear-matrix_images/imageFile53.png>)

![image 54](<2018-averkov-optimal-size-linear-matrix_images/imageFile54.png>)

![image 55](<2018-averkov-optimal-size-linear-matrix_images/imageFile55.png>)

![image 56](<2018-averkov-optimal-size-linear-matrix_images/imageFile56.png>)

- Proof of Corollary 14. By Lemma 32, sxdeg(Mn,2d(X)) = sxdeg(Pn,2d(X)∗). By

(9), the semideﬁnite extension degree is preserved under duality, so that one has sxdeg(Pn,2d(X)∗) = sxdeg(Pn,2d(X)). By Corollary 3, sxdeg(Pn,2d(X)) ≥ n+nd . This yields the assertion.

![image 57](<2018-averkov-optimal-size-linear-matrix_images/imageFile57.png>)

![image 58](<2018-averkov-optimal-size-linear-matrix_images/imageFile58.png>)

![image 59](<2018-averkov-optimal-size-linear-matrix_images/imageFile59.png>)

![image 60](<2018-averkov-optimal-size-linear-matrix_images/imageFile60.png>)

- Proof of Corollary 15. We have Mn,2d = Pn,∗2d, by Lemma 32. By (8) and (9) the semideﬁnite extension degree and the semideﬁnite extension complexity are pre-

served under duality, so that one has sxdeg(Pn,∗2d) = sxdeg(Pn,2d) and sxc(Pn,∗2d) = sxc(Pn,2d). We conclude that Mn,2d has the same semideﬁnite extension degree and the semideﬁnite extension complexity as the cone Pn,2d. An application of Corollary 12 concludes the proof.

![image 61](<2018-averkov-optimal-size-linear-matrix_images/imageFile61.png>)

![image 62](<2018-averkov-optimal-size-linear-matrix_images/imageFile62.png>)

![image 63](<2018-averkov-optimal-size-linear-matrix_images/imageFile63.png>)

![image 64](<2018-averkov-optimal-size-linear-matrix_images/imageFile64.png>)

The lower bound on the semideﬁnite extension degree of the copositive cone CPk in Corollary 16 is established by interpreting CPk as Pn,2d(X) with an appropriate choice of n,d and X. The matching upper bound for k ≤ 4 is a direct consequence of the fact that, for k ≤ 4, a symmetric k × k matrix is copositive if and only if it is a sum of a non-negative matrix and a positive semideﬁnite matrix [MM63].

- Proof of Corollary 16. We assume k ≥ 2 to exclude the trivial case k = 1. We can use the linear bijection A  → fA from the proof of Corollary 6. It is easy to see that this bijection sends CPk onto Pk−1,2(R+k−1). Thus, by Theorem 3, we get sxdeg(CPk) = sxdeg(Pk−1,2(R+k−1)) ≥ k.


It is known that CPk = S+k + N+k holds for k ≤ 4, where N+k := Sk ∩ R+k×k is the cone of symmetric k × k matrices with non-negative components (see [MM63] and [Du¨r10, Sect. 3]). Lemma 31 yields sxdeg(CPk) ≤ max{sxdeg(S+k),sxdeg(N+k)} = k.

![image 65](<2018-averkov-optimal-size-linear-matrix_images/imageFile65.png>)

![image 66](<2018-averkov-optimal-size-linear-matrix_images/imageFile66.png>)

![image 67](<2018-averkov-optimal-size-linear-matrix_images/imageFile67.png>)

![image 68](<2018-averkov-optimal-size-linear-matrix_images/imageFile68.png>)

## 6 Proofs of results for the SONC cone

In this section, we ﬁrst convert the existing description of the SONC cone by Iliman and Timo de Wolﬀ to an alternative description, which is more convenient for our purposes. Once the alternative description is obtained, the existence of a secondorder cone extended formulation for the SONC cone, will follow from a well-known result of Ben-Tal and Nemirovski.

The deﬁnition of the SONC cone involves non-negative circuit polynomials: Deﬁnition 33 (Non-negative circuit polynomials and circuit number [IdW16, DIdW17]).

Let An be the set of all A ⊆ Zn+ of the form A = {α(0),... ,α(k),β}, where k ∈ [n], with the following properties:

- 1. α(0),... ,α(k) ∈ (2Z+)n,
- 2. α(0),... ,α(k) are vertices of a k-dimensional simplex,
- 3. β is in the relative interior of the simplex with the vertices α(0),... ,α(k), that is,


k

k

λiα(i) and 1 =

β =

λi

i=0

i=0

holds for some coeﬃcients λ0 > 0,... ,λk > 0 uniquely determined by α(0),... ,α(k) and β.

Elements of the set

P˜n,A := f =

fαxα : f ≥ 0 on Rn, fα(0) > 0,... ,fα(k) > 0 .

α∈A

are called non-negative circuit polynomials with respect to the circuit A ∈ An. If f = α∈A fαxα, is polynomial satisfying fα(i) ≥ 0 for all i ∈ {0,... ,k}, then the value

k

λi

fα(i) λi

Θf :=

. (17)

![image 69](<2018-averkov-optimal-size-linear-matrix_images/imageFile69.png>)

i=0

is called the circuit number of f. Theorem 34 (Iliman and Timo de Wolﬀ [IdW16, Theorem 3.8]). In the notation of Deﬁnition 33, the set P˜n,A is described as

P˜n,A = f =

and

fαxα : fα(0) > 0,... ,fα(k) > 0, fβ ≥ −Θf if β ∈ (2Z+)n

α∈A

P˜n,A = f =

fαxα : fα(0) > 0,... ,fα(k) > 0, Θf ≥ fβ ≥ −Θf if β  ∈ (2Z+)n.

α∈A

While P˜n,A has a nice explicit description, it has a minor technical drawback of being neither open, nor closed nor a convex cone (P˜n,A is missing the zero polynomial for being a convex cone). Essentially, the cone Pn,A of non-negative polynomials whose support is a subset of A, deﬁned by equality (10) in the introduction, is a ‘regular’ version of P˜n,A with a completely analogous description:

Lemma 35. In the notation of Deﬁnition 33, the set Pn,A is described as

Pn,A = f =

and

fαxα : fα(0) ≥ 0,... ,fα(k) ≥ 0, fβ ≥ −Θf if β ∈ (2Z+)n

α∈A

Pn,A = f =

fαxα : fα(0) ≥ 0,... ,fα(k) ≥ 0, Θf ≥ fβ ≥ −Θf if β  ∈ (2Z+)n.

α∈A

Proof. First observe that, if f is in Pn,A then fα(i) ≥ 0 holds for every i = 0,... ,k. Let us show fα(0) ≥ 0. Choose a vector γ = (γ1,... ,γn) ∈ Zn \ {0} such that

γ , α(0) > γ , β > γ , α(1) = ··· = γ , α(k) .

The vector γ is an inner facet normal of the simplex with the vertices α(0),... ,α(k). For t ∈ R+, we obtain

q(t) := f(tγ1,... ,tγn) = fα(0)t α(0), γ + fβt β, γ +

k

fα(i) t α(1), γ .

i=1

If one had fα(0) < 0, then q(t) would be negative for a suﬃciently large t. Hence α(0) ≥ 0, and analogously we obtain fα(i) ≥ 0 for every i = 0,... ,k.

We introduce the ǫ-perturbation of f by

fǫ :=

k

k

(fα(i) + ǫ)xα(i) + fβxβ = f + ǫ

i=0

i=0

xα(i).

Since α(0),... ,α(k) ∈ (2Z+)n, the non-negativity of f implies the non-negativity of fǫ for every ǫ > 0. Thus, if f ∈ Pn,A, then fǫ is non-negative for every ǫ > 0. Since fǫ ∈ P˜n,A, applying a description of P˜n,A from Theorem 34, and letting ǫ > 0 go to 0, we derive the ‘⊆’ parts of the equalities of our assertion.

Conversely, if β ∈ (2Z+)n and the inequalities fα(0) ≥ 0,... ,fα(k) ≥ 0,fβ ≥ −Θf are fulﬁlled, then in the case fα(0) > 0,... ,fα(k) > 0, one has f ∈ P˜n,A ⊆ Pn,A, while in the case fα(i) = 0 for some i = 0,... ,k one has Θf = 0 so that f is a sum of squares of k + 2 monomial terms.

Similarly, if β  ∈ (2Zn+), then carrying out the same case distinction, we conclude that one has f ∈ P˜n,A ⊆ Pn,A or, otherwise, f is a sum of squares of k +1 monomial terms.

![image 70](<2018-averkov-optimal-size-linear-matrix_images/imageFile70.png>)

![image 71](<2018-averkov-optimal-size-linear-matrix_images/imageFile71.png>)

![image 72](<2018-averkov-optimal-size-linear-matrix_images/imageFile72.png>)

![image 73](<2018-averkov-optimal-size-linear-matrix_images/imageFile73.png>)

Comparing Lemma 35 and Theorem 34, we see that every polynomial f in Pn,A is either in P˜n,A or is a non-negative linear combination of squares of monomials. Deﬁnition 36 (SONC polynomials [IdW16, DIdW17]). Let n,d ∈ N. Using the set An from Deﬁnition 33, we deﬁne

An,2d := {A ∈ An : |α| ≤ 2d for all α ∈ A} Let Cn,2d be the set of all polynomials f ∈ R[x]2d that can be written as f = µ1f1 + ··· + µNfN, where N ∈ N, µ1,... ,µN ≥ 0, and, for every i ∈ {1,... ,N}, the polynomial fi is

- 1. either an element of P˜n,A for some A ∈ An,2d
- 2. or a square fi = x2α of some monomial xα with α ∈ Zn+ and |α| ≤ d.


Polynomials from Cn,2d are called sums of non-negative circuit (SONC) polynomials of degree at most 2d in n variables.

- Remark 37. From deﬁnitions given in [IdW16, DIdW17] it is not immediately clear if monomial squares x2α are supposed to be SONC polynomials. According to explanations given by Timo De Wolﬀ [dW18], the authors of [IdW16, DIdW17] did intend to view monomial squares as degenerate SONC polynomials. In Deﬁnition 36, the ‘shape’ of the cone Cn,2d is determined by Condition 1, while adding monomial squares via Condition 2 makes the cone Cn,2d topologically closed.
- Remark 38. In view of Theorem 34 and Lemma 35, every element of Pn,A \ P˜n,A, with A ∈ An, is a conic combination of monomial squares. This shows that, for n,d ∈ N, the SONC cone Cn,2d can be represented as


Pn,A. (18)

Cn,2d =

A∈An,2d

Equality (18) is a non-technical alternative deﬁnition of Cn,2d.

We can easily determine the semideﬁnite extension degree of Cn,2d from (18), as sxdeg(Pn,A) for A ∈ An,2d can be calculated using the following result from [BTN01]. Lemma 39 (Ben-Tal and Nemirovski [BTN01, Example 15 in §§2.3.5]). Let λ1,... ,λm be positive rational numbers satisfying λ1 + ··· + λm ≤ 1. Then, for the set

C := (x1,... ,xm,xm+1) ∈ Rm+ × R : xm+1 ≤ xλ11 ··· xλmm , one has sxdeg(C) ≤ 2. Proof. Constructions in [BTN01, §§2.3.5] yield an explicit second-order cone extended formulation of C, which shows sxdeg(C) ≤ 2.

![image 74](<2018-averkov-optimal-size-linear-matrix_images/imageFile74.png>)

![image 75](<2018-averkov-optimal-size-linear-matrix_images/imageFile75.png>)

![image 76](<2018-averkov-optimal-size-linear-matrix_images/imageFile76.png>)

![image 77](<2018-averkov-optimal-size-linear-matrix_images/imageFile77.png>)

Proof of Theorem 17. Equality (18) describes Cn,2d as a sum of ﬁnitely many closed convex cones. Hence, applying Lemma 31 to the cone Cn,2d represented by (18), we obtain

sxdeg(Cn,2d) ≤ max{Pn,A : A ∈ An,2d} . The description of cones Pn,A given in Lemma 31 is in terms of non-strict linear inequalities fα(0) ≥ 0,... ,fα(k) ≥ 0 and the inequalities which coincide, up to a rescaling of the variables, with the inequalities describing the set C in Lemma 39. Thus, Lemma 39 yields sxdeg(Pn,A) ≤ 2 for every A ∈ An,2d and we obtain sxc(Cn,2d) ≤ 2.

It remains to show sxdeg(Cn,2d) ≥ 2, which means that Cn,2d is not a polyhedron. One way to see this is to use Theorem 2 in the degenerate case k = 1. Take S ⊆ Rn to be an arbitrarily large ﬁnite subset of the x1-axis R × {0}n−1. For each s = (s1,0,... ,0) ∈ S, the quadratic polynomial f = (x1 − s1)2 ∈ R[x] belongs to Cn,2d and is equal to zero on exactly one point of S. So, by Theorem 2, sxdeg(Cn,2d) > 1.

![image 78](<2018-averkov-optimal-size-linear-matrix_images/imageFile78.png>)

![image 79](<2018-averkov-optimal-size-linear-matrix_images/imageFile79.png>)

![image 80](<2018-averkov-optimal-size-linear-matrix_images/imageFile80.png>)

![image 81](<2018-averkov-optimal-size-linear-matrix_images/imageFile81.png>)

Proof of Corollary 18. If n = 1 or d = 1 or (n,d) = (2,2), then Σn,2d = Pn,2d by Theorem 10. Hence Σn,2d + Cn,2d = Pn,2d.

In the case n,d ≥ 2 and (n,d) = (2,2), Theorem 11 of Scheiderer asserts that Pn,2d has no semideﬁnite extended formulation. On the other hand, in view Lemma 31, the cone Σn,2d + Cn,2d does have a semideﬁnite extended formulation since both summands Σn,2d and Cn,2d have a semideﬁnite extended formulation, by Corollary 4 and Theorem 17, respectively. This implies Σn,2d + Cn,2d = Pn,2d.

![image 82](<2018-averkov-optimal-size-linear-matrix_images/imageFile82.png>)

![image 83](<2018-averkov-optimal-size-linear-matrix_images/imageFile83.png>)

![image 84](<2018-averkov-optimal-size-linear-matrix_images/imageFile84.png>)

![image 85](<2018-averkov-optimal-size-linear-matrix_images/imageFile85.png>)

### Acknowledgements

I thank Jonas Frede for pointing to [AHP+17]. Theorem 17 and Corollary 18 were motivated by the discussion with Andreas Bernig, Mareike Dressler, Raman Sanyal and Thorsten Theobald during the defense of Mareike’s PhD thesis [Dre18]. I would like to thank Timo de Wolﬀ for clarifying the deﬁnition of the SONC cone.

### Funding

The project is funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) - 314838170, GRK 2297 MathCoRe.

## References

[AHP+17] Amir Ali Ahmadi, Georgina Hall, Antonis Papachristodoulou, James Saunderson, and Yang Zheng, Improving eﬃciency and scalability of sum of squares optimization: Recent advances and limitations, Decision and Control (CDC), 2017 IEEE 56th Annual Conference on, IEEE, 2017, pp. 453–462.

[AKW18] Gennadiy Averkov, Volker Kaibel, and Stefan Weltge, Maximum semidefinite and linear extension complexity of families of polytopes, Math. Program. 167 (2018), no. 2, Ser. A, 381–394.

[AL12] Miguel F. Anjos and Jean B. Lasserre (eds.), Handbook on semideﬁnite, conic and polynomial optimization, International Series in Operations Research & Management Science, vol. 166, Springer, New York, 2012.

[BTN01] Aharon Ben-Tal and Arkadi Nemirovski, Lectures on modern convex optimization, MPS/SIAM Series on Optimization, Society for Industrial and Applied Mathematics (SIAM), Philadelphia, PA; Mathematical Programming Society (MPS), Philadelphia, PA, 2001, Analysis, algorithms, and engineering applications.

- [CS16] Venkat Chandrasekaran and Parikshit Shah, Relative entropy relaxations for signomial optimization, SIAM J. Optim. 26 (2016), no. 2, 1147–1173. MR 3499559
- [CS17] , Relative entropy optimization and its applications, Math. Program. 161 (2017), no. 1-2, Ser. A, 1–32.


![image 86](<2018-averkov-optimal-size-linear-matrix_images/imageFile86.png>)

[DIdW17] Mareike Dressler, Sadik Iliman, and Timo de Wolﬀ, A Positivstellensatz for sums of nonnegative circuit polynomials, SIAM J. Appl. Algebra Geom. 1 (2017), no. 1, 536–555.

[DIdW19] , An approach to constrained polynomial optimization via nonnegative circuit polynomials and geometric programming, J. Symbolic Comput. 91 (2019), 149–172.

![image 87](<2018-averkov-optimal-size-linear-matrix_images/imageFile87.png>)

[DPZ67] Richard J. Duﬃn, Elmor L. Peterson, and Clarence Zener, Geometric Programming: Theory and Application, John Wiley & Sons, Inc., New York-London-Sydney, 1967.

[Dre18] Mareike Dressler, Sums of nonnegative circuit polynomials, PhD thesis, Goethe-Universita¨t Frankfurt am Main, 2018.

[Du¨r10] Mirjam Du¨r, Copositive programming–a survey, Recent advances in op-

timization and its applications in engineering, Springer, 2010, pp. 3–20. [dW18] Timo de Wolﬀ, Private communication, 2018. [Faw18] Hamza Fawzi, On representing the positive semideﬁnite cone using the

second-order cone, Math. Program. (online ﬁrst) (2018).

[FGP+15] Hamza Fawzi, Joa˜o Gouveia, Pablo A. Parrilo, Richard Z. Robinson, and Rekha R. Thomas, Positive semideﬁnite rank, Math. Program. 153

(2015), no. 1, Ser. B, 133–177.

[FKPT13] Samuel Fiorini, Volker Kaibel, Kanstantsin Pashkovich, and Dirk Oliver Theis, Combinatorial bounds on nonnegative rank and extended formulations, Discrete Math. 313 (2013), no. 1, 67–83.

[FSED18] Hamza Fawzi and Mohab Safey El Din, A lower bound on the positive semideﬁnite rank of convex bodies, SIAM J. Appl. Algebra Geom. 2

(2018), no. 1, 126–139.

- [FSP15] Hamza Fawzi, James Saunderson, and Pablo A. Parrilo, Equivariant semideﬁnite lifts and sum-of-squares hierarchies, SIAM J. Optim. 25

(2015), no. 4, 2212–2243.

- [FSP16] , Sparse sums of squares on ﬁnite abelian groups and improved semideﬁnite lifts, Math. Program. 160 (2016), no. 1-2, Ser. A, 149–191.

![image 88](<2018-averkov-optimal-size-linear-matrix_images/imageFile88.png>)

- [FSP17] , Equivariant semideﬁnite lifts of regular polygons, Math. Oper. Res. 42 (2017), no. 2, 472–494.


![image 89](<2018-averkov-optimal-size-linear-matrix_images/imageFile89.png>)

[GGS17] Ant´nio Pedro Goucha, Joa˜o Gouveia, and Pedro M. Silva, On ranks of regular polygons, SIAM J. Discrete Math. 31 (2017), no. 4, 2612–2625.

[GM10] Mehdi Ghasemi and Murray Marshall, Lower bounds for a polynomial in

terms of its coeﬃcients, Arch. Math. (Basel) 95 (2010), no. 4, 343–353. [GM12] , Lower bounds for polynomials using geometric programming,

![image 90](<2018-averkov-optimal-size-linear-matrix_images/imageFile90.png>)

SIAM J. Optim. 22 (2012), no. 2, 460–473.

[GPT13] Joa˜o Gouveia, Pablo A. Parrilo, and Rekha R. Thomas, Lifts of convex sets and cone factorizations, Math. Oper. Res. 38 (2013), no. 2, 248–264.

[GRS90] Ronald L. Graham, Bruce L. Rothschild, and Joel H. Spencer, Ramsey Theory, second ed., Wiley-Interscience Series in Discrete Mathematics and Optimization, John Wiley & Sons, Inc., New York, 1990, A WileyInterscience Publication.

[Hil88] David Hilbert, Uber¨ die Darstellung deﬁniter Formen als Summe von Formenquadraten, Mathematische Annalen 32 (1888), no. 3, 342–350.

[IdW16] Sadik Iliman and Timo de Wolﬀ, Amoebas, nonnegative polynomials and sums of squares supported on circuits, Res. Math. Sci. 3 (2016), Paper No. 9, 35.

[Las15] Jean Bernard Lasserre, An Introduction to Polynomial and Semialgebraic Optimization, Cambridge Texts in Applied Mathematics, Cambridge University Press, Cambridge, 2015.

[Lau09] Monique Laurent, Sums of squares, moment matrices and optimization over polynomials, Emerging applications of algebraic geometry, IMA Vol. Math. Appl., vol. 149, Springer, New York, 2009, pp. 157–270.

[LRS15] James R. Lee, Prasad Raghavendra, and David Steurer, Lower bounds on the size of semideﬁnite programming relaxations, STOC’15—Proceedings of the 2015 ACM Symposium on Theory of Computing, ACM, New York, 2015, pp. 567–576.

[Mar08] Murray Marshall, Positive Polynomials and Sums of Squares, Mathematical Surveys and Monographs, vol. 146, American Mathematical Society, Providence, RI, 2008.

[Mit03] H. D. Mittelmann, An independent benchmarking of SDP and SOCP solvers, Math. Program. 95 (2003), no. 2, Ser. B, 407–430, Computational semideﬁnite and second order cone programming: the state of the art.

[MM63] John E. Maxﬁeld and Henryk Minc, On the matrix equation X′X = A, Proc. Edinburgh Math. Soc. (2) 13 (1962/1963), 125–129.

[Nie15] Jiawang Nie, Linear optimization with cones of moments and nonnegative polynomials, Math. Program. 153 (2015), no. 1, Ser. B, 247–274.

[Roc97] R. Tyrrell Rockafellar, Convex Analysis, Princeton Landmarks in Mathematics, Princeton University Press, Princeton, NJ, 1997, Reprint of the 1970 original, Princeton Paperbacks.

[Sau15] James Francis Saunderson, Semideﬁnite representations with applications in estimation and inference, ProQuest LLC, Ann Arbor, MI, 2015, Thesis (Ph.D.)–Massachusetts Institute of Technology.

[Sch18] Claus Scheiderer, Spectrahedral shadows, SIAM J. Appl. Algebra Geom. 2 (2018), no. 1, 26–44.

[SdW18] Henning Seidler and Timo de Wolﬀ, An experimental comparison of sonc and sos certiﬁcates for unconstrained optimization, arXiv preprint arXiv:1808.08431 (2018).

[SP15] James Saunderson and Pablo A. Parrilo, Polynomial-sized semideﬁnite representations of derivative relaxations of spectrahedral cones, Math. Program. 153 (2015), no. 2, Ser. A, 309–331.

[SPW15] J. Saunderson, P. A. Parrilo, and A. S. Willsky, Semideﬁnite descriptions of the convex hull of rotation matrices, SIAM J. Optim. 25 (2015), no. 3, 1314–1343.

[WSV00] Henry Wolkowicz, Romesh Saigal, and Lieven Vandenberghe (eds.), Handbook of semideﬁnite programming, International Series in Operations Research & Management Science, vol. 27, Kluwer Academic Publishers, Boston, MA, 2000, Theory, algorithms, and applications.

[Zie95] Gu¨nter M. Ziegler, Lectures on Polytopes, Graduate Texts in Mathematics, vol. 152, Springer-Verlag, New York, 1995.

