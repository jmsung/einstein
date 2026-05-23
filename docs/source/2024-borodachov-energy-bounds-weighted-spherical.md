---
type: source
kind: paper
title: Energy bounds for weighted spherical codes and designs via linear programming
authors: Sergiy Borodachov, Peter Boyvalenkov, Peter Dragnev, Douglas Hardin, Edward Saff, Maya Stoyanova
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2403.07457v2
source_local: ../raw/2024-borodachov-energy-bounds-weighted-spherical.pdf
topic: general-knowledge
cites:
---

arXiv:2403.07457v2[math.MG]19Dec2024

ENERGY BOUNDS FOR WEIGHTED SPHERICAL CODES AND DESIGNS VIA LINEAR PROGRAMMING

S. V. BORODACHOV, P. G. BOYVALENKOV, P. D. DRAGNEV, D. P. HARDIN, E. B. SAFF, AND M. M. STOYANOVA

ABSTRACT. Universal bounds for the potential energy of weighted spherical codes are obtained by linear programming. The universality is in the sense of Cohn-Kumar – every attaining code is optimal with respect to a large class of potential functions (absolutely monotone), in the sense of Levenshtein – there is a bound for every weighted code, and in the sense of parameters (nodes and weights) – they are independent of the potential function. We derive a necessary condition for optimality (in the linear programming framework) of our lower bounds which is also shown to be sufﬁcient when the potential is strictly absolutely monotone. Bounds are also obtained for the weighted energy of weighted spherical designs. We explore our bounds for several previously studied weighted spherical codes.

1. INTRODUCTION

Let Sn−1 be the unit sphere in Rn. A pair (C,W) consisting of an N-tuple C = (x1,x2,... ,xN) of distinct points on Sn−1 and corresponding weights W = (w1,w2,... ,wN), where wi > 0 corresponds to xi and w1 + w2 + ··· + wN = 1, is called a weighted spherical code. Let s(C) := max{xi · xj : i = j} be the maximal inner product of pairs of distinct points of C (or, for short, the maximal inner product of C). We shall denote by |X| the size of a tuple X.

For a given (extended real-valued) continuous function h : [−1,1] → R ∪ {+∞}, ﬁnite on [−1,1), and a given weighted spherical code, we consider the weighted h-energy of (C,W)

Eh(C,W) :=

wiwjh(xi · xj),

i =j

which arises in the electrostatic problem of distributing N = |W| positive charges (not necessarily equal) on the unit sphere. Let

Eh(W) := inf{Eh(C,W) : C ∈ Sn−1 |W|} (1) be the minimum weighted h-energy among all weighted codes (C,W) with ﬁxed weight W.

Similarly, for ﬁxed s ∈ [−1,1) we consider Uh(s,W) := sup{Eh(C,W) : C ∈ Sn−1 |W| , s(C) = s}, (2)

![image 1](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile1.png>)

Date: December 20, 2024.

1

the maximum1 weighted h-energy among all weighted codes (C,W) with ﬁxed maximal inner product s ∈ [−1,1) and ﬁxed weights W.

Although the general linear programming theorems that will be presented in Sections 2 and 4 (Theorem 2.1 and Theorem 4.1, respectively), hold for general potentials h, we will be especially interested when they are absolutely monotone (strictly absolutely monotone); that is, h(i)(t) ≥ 0, i = 0,1,... (h(i)(t) > 0, i = 0,1,... ) for all t ∈ [−1,1) (all t ∈ (−1,1)). Commonly occuring absolutely monotone potentials include

h(t) = [2(1 − t)]1−n/2, Newton potential, h(t) = [2(1 − t)]−α/2, α > 0, Riesz potential, h(t) = e−α(1−t), Gaussian potential,

h(t) = −log[2(1 − t)], Logarithmic potential. As observed by Cohn and Kumar [14, p. 101], if an absolutely monotone function fails to be strictly absolutely monotone, then it is a polynomial.

As is often the case in the study of spherical codes, the Gegenbauer polynomials Pi(n) of respective degrees i = 0,1,... , play a useful role. They are orthogonal with respect to the measure

dµn(t) := γn(1 − t2)n−23 dt, t ∈ [−1,1],

![image 2](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile2.png>)

where γn := Γ(n2)/√πΓ(n−21) is a normalizing constant that makes µn a probability measure. We normalize these polynomials by Pi(n)(1) = 1. Note that Pi(n)(t) is exactly the Jacobi polynomial Pi(α,β)(t) with parameters α = β = (n − 3)/2 and the corresponding normalization.

![image 3](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile3.png>)

![image 4](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile4.png>)

![image 5](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile5.png>)

Given a weighted code (C,W) we consider its weighted moments

Mℓ(C,W) :=

|W|

wiwjPℓ(n)(xi · xj), ℓ ≥ 1. (3)

i,j=1

It follows from the positive deﬁniteness of the Gegenbauer polynomials (see e.g. [32], [5, Chapter 5]) that Mℓ(C,W) ≥ 0 for every positive integer ℓ. The case of equality for some ℓ is especially interesting.

Deﬁnition 1.1. A weighted spherical code (C,W) is called a weighted spherical design of strength τ (or a weighted spherical τ-design) if its ﬁrst τ weighted moments are zero; i.e.,

Mℓ(C,W) = 0 for 1 ≤ ℓ ≤ τ.

In the equi-weighted case w1 = ··· = wN = 1/N one obtains the classical spherical designs introduced in the seminal paper of Delsarte, Goethals, and Seidel [18] from 1977. The weighted case can be traced back to the 1960’s and 70’s when cubature formulas (or numerical integration schemes with some degree of precision) for approximate calculation of multiple integrals on Sn−1

![image 6](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile6.png>)

1By convention, we deﬁne the sup of the empty set to be −∞. Thus, Uh(s, W) = −∞ when there exist no C ⊂ Sn−1 with |C| = N = |W| and s(C) = s.

were investigated [34, 36, 35, 31, 23]. The related weighted designs in Rn and Euclidean designs on several concentric spheres were ﬁrst considered in [30] (see also the comprehensive survey [1]).

Utilizing linear programming, we shall obtain bounds for the quantities Eh(W) given by (1) and Uh(s,W) given by (2). Our bounds are valid for all absolutely monotone potentials h and are universal in the sense of Levenshtein (there is a bound for every weighted code) and in the sense of deﬁning parameters (nodes and weights) that are independent of the potential function. Also, assuming the existence of a code that attains our bound for some absolutely monotone h, that code will attain our bound for all absolutely monotone h. That is, our bounds are universal in the sense of Cohn-Kumar. We shall also obtain bounds in the special cases when the codes are weighted spherical designs.

The universal lower bounds (ULB, Theorem 2.3) on Eh(W) and universal upper bounds (UUB, Theorem 4.2) on Uh(s,W) are derived as certain solutions of linear programs that arise naturally as generalizations of the equi-weighted frameworks from [9] for the ULB and from [11] for the UUB (see also [10] for such bounds in polynomial metric spaces). We present examples of ULB and UUB for some special weighted codes that have previously attracted attention for their high degree of precision when used in cubature formulas; see Sobolev [34], Goethals and Seidel [23], Waldron [37], and Godsil [22, Theorem 3.2].

The paper is organized as follows. In Section 2 we develop the general linear programming technique for obtaining lower bounds on the energy of weighted codes and formulate a linear program to obtain bounds that are in a sense optimal. Then we solve that program in a certain class of polynomials to derive our universal lower bound for the quantity Eh(W). In the remainder of the section we consider weighted spherical designs and present examples of our lower bounds in two cases where good weighted spherical designs can be easily constructed – a weighted pentakis dodecahedron (weighted union of an icosahedron with a dodecahedron), which is a weighted spherical 9-design, and a weighted union of a cube with a crosspolytope in n dimensions, which is a weighted spherical 5-design. In Section 3 we prove a necessary condition for optimality of our lower bounds, which is also sufﬁcient for strictly absolutely monotone potentials with positive derivatives at −1. Section 4 is devoted to the counterpart technique for obtaining upper bounds for the quantity Uh(s,W). We develop the corresponding linear programming framework and propose a construction of a solution which might be optimal. The same two examples are considered from the upper bounds case point of view. In Section 5 we derive ULB and UUB for weighted spherical designs. The design properites allow us to establish both bounds for broader classes of potentials and to improve the UUB.

2. UNIVERSAL LOWER BOUNDS FOR ENERGY OF WEIGHTED CODES

- 2.1. A general linear programming lower bound for weighted codes. Given a potential function h, we consider the set of polynomials


 

 

deg(f)

Lh(n) :=

fiPi(n)(t) : f(t) ≤ h(t),t ∈ [−1,1),fi ≥ 0,i ≥ 1

f(t) =

,





i=0

∞ i=0

are the Gegenbauer polynomials as deﬁned in the Introduction. The set L(hn) will be the feasible domain for our linear programming lower bounds for Eh(W). Without loss of generality we may assume that f(1) > 0.

where Pi(n)

The following theorem is a useful folklore result of Delsarte-Yudin type [16, 17, 18, 38, 25]. Hereafter we denote the common size of C and W by N.

Theorem 2.1. If f(t) = ℓ deg(=0f) fℓPℓ(n)(t) ∈ L(hn), then for every (C,W) code on Sn−1

N

wi2. (4) Consequently,

Eh(C,W) ≥ Ef(C,W) ≥ f0 − f(1)

i=1

N

wi2 =: ULB(W,h). (5)

Eh(W) ≥ sup

f0 − f(1)

f∈L(hn)

i=1

If equality is attained throughout (4) for some f and (C,W) with C = (x1,x2,... ,xN), then f(xi · xj) = h(xi · xj) for every i = j and fℓMℓ(C,W) = 0 for every ℓ ∈ {1,2,... ,deg(f)}.

Proof. The ﬁrst inequality in (4) follows obviously from f ≤ h in [−1,1); i.e., Eh(C,W) =

wiwjh(xi · xj) ≥

wiwjf(xi · xj) = Ef(C,W).

i =j

i =j

For the second inequality we estimate Ef(C,W) from below as follows:

Ef(C,W) =

i,j

N

wi2

wiwjf(xi · xj) − f(1)

i=1

=

deg(f)

fℓ

ℓ=0

i,j

N

wiwjPℓ(n)(xi · xj) − f(1)

wi2

i=1

deg(f)

N

wi2

= f0 +

fℓMℓ(C,W) − f(1)

i=1

ℓ=1

N

wi2.

≥ f0 − f(1)

i=1

2

Above we used that the coefﬁcient of f0 is Ni,j=1 wiwj = Ni=1 wi

= 1, the inequalities fℓ ≥

0 for ℓ ≥ 1, and i,j wiwjPℓ(n)(xi · xj) = Mℓ(C,W) ≥ 0 because of the positive deﬁniteness of the Gegenbauer polynomials. The conditions for equality follow immediately from the above.

Remark 2.2. We note that equality will hold for the last two quantities of the multi-display formula above if and only if fℓMℓ(C,W) = 0 for all ℓ = 1,... ,deg(f), which is true when the weighted code (C,W) is a spherical weighted design of high enough strength. We shall use this observation

in Section 5 to broaden the class of potentials for which our universal bounds hold when applied to weighted spherical designs.

Of particular importance is the case when the supremum in (5) is taken over the class of polyno-

mials Lh(n) ∩ Pm, where Pm denotes the class of polynomials of degree at most m. This yields the linear program

 

N

wi2

maximize f0 − f(1)

(6)



i=1

subject to f ∈ L(hn) ∩ Pm.

For particular parameters h, W, and m we shall obtain explicit solutions of this linear program. We shall denote the maximized objective function by ULBm(W,h). Note that

N

1 N

wi2 ≥

SW :=

![image 7](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile7.png>)

i=1

(7)

with equality if and only if w1 = w2 = ··· = wN = 1/N (i.e., in the classical case of equiweighted code). Then it follows that

N

f0 − f(1)

i=1

f(1) N

wi2 ≤ f0 −

,

![image 8](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile8.png>)

where the right-hand side coincides exactly with the quantity that appears in the linear programming bound for the equi-weighted codes. This means that the bounds from Theorem 2.1 will be always less than the bounds for the corresponding equi-weighted case. In any case, it is important to note that the quantity

N

1 SW

wi2

NW :=

= 1/

![image 9](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile9.png>)

i=1

has to play an important role since it is going to determine the parameters (nodes and weights) of the universal lower bound in the same way as the cardinality N does in [9]. Clearly, as the weights wi get closer in value to one another, as measured by the variance

var W := (1/N)SW − 1/N2, (8)

the quantity NW approaches |W| = N from below. The inequality (7), written as N ≥ NW, means that NW is always less than or equal to the tuple size N with equality only for equal weights and serves to replace N in the framework from [9]. This discussion further justiﬁes the bounds in this paper as natural generalizations of the ULB from [9] and UUB from [11]. Note that in the UUB setting of Section 4 one additional constant, denoted by Nq, will appear, where Nq > N ≥ NW. Note that while N is a natural number, NW and Nq are in general real.

- 2.2. Delsarte-Goethals-Seidel bound for minimal spherical designs and Levenshtein bound for maximal spherical codes. The parameters of our energy bounds are closely related to two classical universal linear programming bounds, the Delsarte-Goethals-Seidel lower bound for minimal cardinality B(n,m) of spherical designs of given dimension n and strength m and the Levenshtein upper bound for the maximal cardinality A(n,s) of spherical codes of given dimension n and maximal inner product s.


The Delsarte-Goethals-Seidel bound [18] states that B(n,m) ≥ D(n,m) :=

n + k − 2 + ε n − 1

n + k − 2 n − 1

+

(9)

for m = 2k − 1 + ε, where ε ∈ {0,1} just indicates the parity of m. The numbers D(n,m), m = 1,2,3,..., from (9) deﬁne a partition of the positive integers in [2,+∞) into countably many consecutive intervals. Therefore, there exists a unique positive integer m such that NW ∈ (D(n,m),D(n,m + 1)] (we will always assume that NW > 2). In what follows we will always assume that NW and m are related this way.

Following Levenshtein’s notations from [27], for a,b ∈ {0,1} we denote by ta,bk the largest zero

of the Jacobi polynomial Pk(a+(n−3)/2,b+(n−3)/2)(t), k ≥ 1, with t01,1 := −1 by deﬁnition. For m ∈ N, consider the interval

 

tk1,−11,tk1,0 , if m = 2k − 1, tk1,0,tk1,1 , if m = 2k,

Im :=



(or Im := [tk1,−1−1+εε,t1k,ǫ] with the short ε-notation). The interlacing properties tk1,−11 < tk1,0 < tk1,1, k ≥ 1,

- (see [27, Sections 3, 4] or [28, Lemmas 5.29, 5.30]) imply that the collection of intervals {Im}∞m=1 is well deﬁned and constitute a partition of the interval [−1,1) into countably many subintervals with non-overlapping interiors. The Levenshtein bound (obtained in 1979 [26]; see also [27, 28]) states that


A(n,s) ≤ Lm(n,s), s ∈ Im, (10) where

 .

 2k + n − 3 + 2ε

(1 + s)ε Pk(−n)1+ε(s) − Pk(+n)ε(s) (1 − s) εPk(n)(s) + Pk(+n)ε(s)

k + n − 3 + ε n − 2

n − 1 −

Lm(n,s) :=

![image 10](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile10.png>)

![image 11](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile11.png>)

There is a strong relation between the Delsarte-Goethals-Seidel bound and the Levenshtein bound. For every ﬁxed m ∈ N, the function Lm(n,s) is continuous, strictly increasing, and maps the interval Im bijectively onto the interval [D(n,m),D(n,m + 1)]. This relates the two partitions from above and, moreover, implies the four equalities (recall that m = 2k − 1 + ε)

Lm(n,tk1,−1−1+εε) = D(n,m), Lm(n,t1k,ε) = D(n,m + 1), ε ∈ {0,1} (11)

at the ends of the intervals Im. The Levenshtein function L(n,s) : [−1,1) → [2,+∞) is deﬁned to coincide with Lm(n,s) on Im, m ≥ 1. It follows from (11) that it is continuous, strictly increasing, and smooth in the interiors of the intervals Im.

The Levenshtein bound Lm(n,s) is valid (and optimal in a sense; see [33], [27, Section 4], [28, Theorem 5.39]) in the whole interval s ∈ Im. It is deﬁned via corresponding Levenshtein polynomial fm(n,s)(t) and one has Lm(n,s) = fm(n,s)(1)/f0 (see, e.g., [27, Section 4] for detailed description of this correspondence). Note that

k−2+ε

(t − αi)2,

fm(n,s)(t) = (t − αk−1+ε)(t − α0)2−ε

i=1

where the roots of fm(n,s) will play important roles in our considerations (ﬁrst of all, αk−1+ε = s).

- 2.3. Generation of parameters. We are now in a position to generate the necessary parameters for our universal lower bounds.


Given a weighted spherical code (C,W) we ﬁnd the parameter NW > 2 and determine the unique positive integer m = 2k − 1 + ε such that

D(n,m) < NW ≤ D(n,m + 1). (12) Next, we ﬁnd the unique s ∈ Im = [t1k,−1−1+εε,t1k,ǫ] such that

Lm(n,s) = NW (13) and construct the corresponding Levenshtein polynomial fm(n,s)(t). Then the roots of fm(n,s),

α0 < α1 < ··· < αk−1+ε = s

(note that −1 ≤ α0 with equality if and only if ε = 1; i.e. if m = 2k) will serve as nodes for both, quadrature (14) and our Hermite interpolation. Alternatively, one can obtain the nodes (αi)ik=0−1+ε as the roots of (13) considered as an equation in the variable s.

We also need weights (ρi)ik=0−1+ε (ρi corresponds to αi) which are computed by substituting the Lagrange basis polynomials ℓi(t) = j =i(t − αj) for i = 0,1,... ,k − 1 + ε in the quadrature formula (14) below. Explicit formulas for (ρi)ik=0−1+ε in the case ε = 0 (this is for odd m = 2k − 1) can be found in [8, Appendix A4] (see also the expressions in the proof of Theorem 5.39 from [28]). We note also that

1

ℓ2i(t)dµn(t) > 0, i = 0,1,... ,k − 1 + ε,

ρi =

−1

- (see [28, Theorem 5.39]) and the identity i k=0−1+ε ρi = 1−1/NW both hold by setting f(t) = ℓ2i(t) or f(t) ≡ 1, respectively, in the quadrature formula (14) below.


Summarizing, the derivation of the necessary parameters proceeds as follows. Given a weighted code (C,W), we ﬁnd NW and the unique m = 2k−1+ε such that NW ∈ (D(n,m),D(n,m+1)]. Then we solve (13) as an equation in s and derive the parameters (αi)ik=0−1+ε and (ρi)ik=0−1+ε.

- 2.4. Universal lower bound for weighted codes. It is crucial for our approach that the Gauss-type quadrature formula (cf. [28, Theorem 5.39])


f(1) Lm(n,s)

f0 =

![image 12](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile12.png>)

k−1+ε

f(1) NW

ρif(αi) =

+

+

![image 13](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile13.png>)

i=0

k−1+ε

ρif(αi) (14)

i=0

holds true for every polynomial f(t) = f0 + i deg(=1 f) fiPi(n)(t) of degree at most 2k −1+ε (recall that NW is less than but possibly close to N). The formula (14) is called a 1/NW-quadrature rule in the framework from [9]. Note that we do not require the existence of a spherical code with maximum inner product s for such a quadrature to exist.

As in the equi-weighted case we will need two facts from the theory of orthogonal polynomials. Namely, it is well known that the Gegenbauer expansions of the polynomials Pi(n)(t)Pj(n)(t) and (t + 1)Pi(n+2)(t)Pj(n+2)(t) have nonnegative coefﬁcients for every i,j; see [21]. In [28], these properties are called Krein conditions and strengthened Krein conditions, respectively (cf. [28, Sections 3 and 5]).

We are now in a position to solve the linear program (6).

- Theorem 2.3. (ULB for weighted codes) Let W be a weight vector such that NW satisﬁes (12) and let h be absolutely monotone. Then


Eh(W) ≥

k−1+ε

ρih(αi), (15)

i=0

where the parameters (αi,ρi)ik=0−1+ε are deﬁned as above. This bound cannot be improved by any polynomial from Lh(n) ∩ Pm; i.e., the maximized objective function ULBm(W,h) is equal to the right-hand side of (15).

Proof. Let f be the unique Hermite interpolant to h at the nodes (αi)ik=0−1+ε, each counted twice except for the case α0 = −1 (equivalent to m = 2k) which is counted once. Then deg(f) ≤ m, so (14) along with the interpolation conditions f(αi) = h(αi), i = 0,1,... ,k − 1 + ε, yields the equalities

N

wi2 =

f0 − f(1)

i=1

k−1+ε

k−1+ε

ρih(αi) = ULBm(W,h).

ρif(αi) =

i=0

i=0

The error formula for the Hermite interpolation implies that for all t ∈ [−1,1)

k−1+ε

h(2k+ε)(ξ) (2k + ε)!

(t − αi)2, ξ ∈ (−1,1).

(t − α0)2−ε

h(t) − f(t) =

![image 14](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile14.png>)

i=1

As h(2k+ε) ≥ 0 on [−1,1], we conclude that f(t) ≤ h(t) for every t ∈ [−1,1). It remains to prove that f is positive deﬁnite to complete the veriﬁcation that f ∈ L(hn).

We ﬁrst consider the case ε = 0 (i.e., m = 2k − 1). Order the multiset of nodes as (α0,α0,α1,α1,... ,αk−1,αk−1) = (t1,t2,... ,t2k−1,t2k)

(i.e., t2i+1 = t2i+2 = αi for i = 0,1,... ,k − 1). Then the Newton interpolation formula (see, for example, [4])

r

2k−1

(t − tj)

h[t1,... ,tr+1]

f(t) = h(t1) +

r=1

j=1

implies that the polynomial f is a nonnegative linear combination of the constant 1 and the partial products

r

(t − tj), r = 1,2,... ,2k − 1. (16) Since

j=1

B1(t − α0)(t − α1)··· (t − αk−1) = Pk((n−1)/2,(n−3)/2)(t) − β1Pk((−n1−1)/2,(n−3)/2)(t),

- for some positive constants B1 and β1, it follows from [14, Theorem 3.1] that all polynomials (t − α0)(t − α1)··· (t − αi), i = 0,1,... ,k − 2,

expand in the system {Pi((n−1)/2,(n−3)/2)(t)} with nonnegative coefﬁcients. Since every polynomial Pi((n−1)/2,(n−3)/2)(t) is positive deﬁnite (cf. [28, Eq. (5.119)]; this follows directly from the Christoffel-Darboux formula which relates explicitly this polynomial to the Gegenbauer polynomials Pj(n), j = 0,1,... ,i − 1), the Krein condition implies that all partial products (16) with r ≤ 2k − 2 are positive deﬁnite. The only remaining partial product (with r = 2k − 1 in (16)) is exactly the Levenshtein polynomial f2(kn,s−1)(t) which is positive deﬁnite as well (see, for example, [28, Theorem 5.42]). Therefore f is positive deﬁnite and (15) follows in this case.

For ε = 1 (i.e., m = 2k) we need the strengthened Krein condition. Now the interpolation nodes are ordered as

(α0 = −1,α1,α1,... ,αk,αk) = (−1,t1,t2,... ,t2k−1,t2k) and our polynomial f is a nonnegative linear combination of 1 and the partial products

(t + 1)

r

j=1

(t − tj), r = 1,2,... ,2k − 1. (17)

Theorem 3.1 from [14] now implies that all polynomials

(t − α1)(t − α2)··· (t − αi), i = 1,2,... ,k − 1, expand in the system {Pi(n+2)(t)} with nonnegative coefﬁcients because

B2(t − α1)(t − α2)··· (t − αk) = Pk((n−1)/2,(n−1)/2)(t) − β2Pk((−n1−1)/2,(n−1)/2)(t),

- for some positive constants B2 and β2. Then all partial products from (17) with r ≤ 2k − 2


expand with nonnegative coefﬁcients in (t + 1)Pi(n+2)(t)Pj(n+2)(t) and the strengthened Krein condition completes the argument. Finally, in the case r = 2k−1 we obtain exactly the Levenshtein

polynomial f2(kn,s)(t) which is positive deﬁnite and this is exactly what is needed to complete the proof that f ∈ Lh(n) ∩ Pm. Thus, (15) follows in this case as well.

If g(t) = deg(i=0 g) giPi(n)(t) is a polynomial from L(hn) ∩Pm and f is deﬁned as above, then (14) can be applied with g to see that the lower bound provided by g satisﬁes

N

k−1+ε

k−1+ε

N

wi2 = ULBm(W,h), which completes the proof.

wi2 =

ρih(αi) = f0 − f(1)

ρig(αi) ≤

g0 − g(1)

i=1

i=0

i=0

i=1

We next establish the monotonicity of ULBm(W,h) in NW.

- Theorem 2.4. Let V = (v1,... ,v N) and W = (w1,... ,wN) be two weight vectors with positive


components such that |iV=1| vi = |iW=1| wi = 1, and suppose that NV < NW (equivalently, SV > SW). Let m and m be the positive integers associated with V and W, respectively, via (12). Then m ≥ m and

ULBm(W,h) > ULB m(V,h).

If m = m, then the nodes (αi)ik=0−1+ε for NW are strictly greater than the corresponding nodes for NV .

Proof. The inequality NV < NW implies via (12) that m ≥ m. If the equality holds, (13) and the monotonicity of the Levenshtein function L(n,s) imply the monotonicity of the nodes αi; i.e., they are increasing with s = αk−1+ε which is increasing with NW (see [8]).

Let f and g be the (unique) polynomial solutions of (6) associated with W and V , respectively. Then, as g ∈ Lh(n) ∩ P m ⊆ Lh(n) ∩ Pm, the optimality of f over L(hn) ∩ Pm yields

g(1) NW

g(1) NV

f(1) NW ≥ g0 −

= ULB m(V,h). Note that g has positive Gegenbauer coefﬁcients and g(1) = g0 + ··· + g m > 0.

> g0 −

ULBm(W,h) = f0 −

![image 15](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile15.png>)

![image 16](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile16.png>)

![image 17](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile17.png>)

- 2.5. Low degrees bounds. We proceed with derivation of more explicit forms of the ﬁrst degrees ULB. For degree one ULB, we have (see [28, Table 6.1] for the ﬁrst ﬁve bounds Lm(n,s)) L1(n,s) = (s − 1)/s = NW (note that s ∈ [−1,−1/n] is negative). This gives


1 α0NW

NW − 1 NW

1 NW − 1

, ρ0 = −

, where 2 ≤ NW(≤ N) ≤ n + 1. Therefore,

=

α0 = −

![image 18](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile18.png>)

![image 19](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile19.png>)

![image 20](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile20.png>)

NW − 1 NW · h −

1 NW − 1

Eh(W) ≥ ULB1(W,h) = ρ0h(α0) =

, 2 ≤ NW ≤ n + 1.

![image 21](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile21.png>)

![image 22](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile22.png>)

The degree two ULB is computed via L2(n,s) = 2n(1 − s)/(1 − ns) = NW, where s ∈ [−1/n,0] (corresponding to the restrictions n + 1 ≤ NW ≤ 2n), giving the parameters

2n − NW n(NW − 2)

,

α0 = −1, α1 = −

![image 23](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile23.png>)

n(NW − 2)2 NW((n + 1)NW − 4n)

NW − n − 1 (n + 1)NW − 4n

ρ0 =

. This leads to the bound

, ρ1 =

![image 24](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile24.png>)

![image 25](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile25.png>)

Eh(W) ≥ ULB2(W,h) = ρ0h(α0) + ρ1h(α1)

NW(NW − n − 1)h(−1) + n(NW − 2)2h −n2(nN−NW

![image 26](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile26.png>)

W −2) NW((n + 1)NW − 4n)

,

=

![image 27](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile27.png>)

where n + 1 ≤ NW ≤ 2n.

The degree three ULB is already too complicated to be explicitly stated here. However, for particular suitable potentials, like the Fejes To´th potential (see the next paragraph), where the potential and the formulas for the weights (ρi)ik=0−1 via the nodes (αi)ik=0−1 (this is for ε = 0, i.e. m = 2k − 1) from [8, Appendix] are relatively simple and ﬁt well each other, the calculations of ULB3(W,h) are still doable.

![image 28](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile28.png>)

The potential h(t) = − 2(1 − t) ﬁts in the above scheme because 2+h(t) is absolutely monotone. This potential corresponds to the Fejes To´th problem [20] and it has been studied by many authors (see, for example, [3, 2] and references therein). The degrees 1-3 ULB for weighted codes and this particular potential (and their asymptotic consequences) can be extracted from [2] simply by replacing N by NW and dividing by NW2 .

- 2.6. Examples. In contrast to difﬁculties for derivation of more explicit analytic expressions of


ULBm(W,h) for m ≥ 3, the numerical calculations of bounds for given n, h, and W can be easily programmed. In this subsection we present several examples, where the ULB and the actual weighted energy are computed.

In all computations here and below we used two independent programs, one in Maple and one in Mathematica. Both programs produced the same numbers with 50-digits precision. For the sake of short presentation, we truncate or round up (depending on whether the bounds are lower or upper, respectively) the real numbers giving the weighted energy ULB and UUB. The values of the remaining real parameters (NW, nodes, weights) are rounded to the fourth digit.

- Example 2.5. (Union of icosahedron and dodecahedron.) Let C32 ⊂ S2 consist of the 12 vertices of an icosahedron, each of weight wI = 20/(21·32) = 5/168, and the 20 vertices of a dodecahedron, each of weight wD = 36/(35 · 32) = 9/280. The vertices of the icosahedron are the centers of the spherical caps deﬁned by the twelve pentagonal faces of the dodecahedron. In geometry, this is


called a pentakis dodecahedron or a kisdodecahedron. Note that (C32,W) is a weighted spherical 9-design (see [23, Section 5], [24, Example 3.6]).

We proceed with computations of the actual weighted energy of (C32,W) and the corresponding ULB9(W,h) for the potential function h(t) = 1/ 2(1 − t).

![image 29](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile29.png>)

The weighted energy of (C32,W) is computed from the information about its structure from Table 1. There are two types of points, I and D, respectively, according to whether they belong to the icosahedron or the dodecahedron, which deﬁne the two different distance distributions (the last

two rows of Table 1). To shorten the notation we set

1 − 2/√5 √3

![image 30](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile30.png>)

![image 31](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile31.png>)

, b :=

a :=

![image 32](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile32.png>)

![image 33](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile33.png>)

1 + 2/√5 √3

![image 34](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile34.png>)

![image 35](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile35.png>)

.

![image 36](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile36.png>)

![image 37](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile37.png>)

TABLE 1. Structure of (C32,W). Inner products −1 ±1/√5 ±a ±b ±1/3 ±

![image 38](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile38.png>)

![image 39](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile39.png>)

![image 40](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile40.png>)

![image 41](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile41.png>)

![image 42](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile42.png>)

√5/3 Type Number of points

![image 43](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile43.png>)

![image 44](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile44.png>)

![image 45](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile45.png>)

![image 46](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile46.png>)

![image 47](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile47.png>)

![image 48](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile48.png>)

![image 49](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile49.png>)

![image 50](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile50.png>)

![image 51](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile51.png>)

![image 52](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile52.png>)

![image 53](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile53.png>)

![image 54](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile54.png>)

![image 55](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile55.png>)

![image 56](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile56.png>)

![image 57](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile57.png>)

![image 58](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile58.png>)

![image 59](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile59.png>)

![image 60](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile60.png>)

![image 61](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile61.png>)

![image 62](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile62.png>)

![image 63](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile63.png>)

![image 64](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile64.png>)

![image 65](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile65.png>)

![image 66](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile66.png>)

![image 67](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile67.png>)

I 1 5 5 5 0 0 D 1 0 3 3 6 3

![image 68](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile68.png>)

![image 69](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile69.png>)

![image 70](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile70.png>)

![image 71](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile71.png>)

![image 72](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile72.png>)

![image 73](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile73.png>)

![image 74](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile74.png>)

![image 75](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile75.png>)

![image 76](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile76.png>)

![image 77](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile77.png>)

Then, Eh(C32,W) =

wiwjh(xi · xj)

i =j

√

√

= 12wI2 h(−1) + 5h(−1/

![image 78](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile78.png>)

![image 79](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile79.png>)

5) + 5h(1/

5)

+120wIwD (h(a) + h(−a) + h(b) + h(−b))

√

√

+20wD2 h(−1) + 6h(−1/3) + 6h(1/3) + 3h(−

![image 80](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile80.png>)

![image 81](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile81.png>)

5/3) ≈ 0.8050318.

5/3) + 3h(

We have NW = 1/ 32i=1 wi2 = 735/23 ≈ 31.9565217 which is very close to the cardinality 32 of C32. Thus, we expect good bounds. We compute the ULB for n = 3, NW, and the Coulomb potential h(t) = 1/ 2(1 − t). Since NW belongs to the interval (D(3,9),D(3,10)] = (30,36] (note that N = 32 is in the same interval), we solve the equation L9(3,s) = NW to derive the parameters (αi,ρi)4i=0 with approximate values as shown in Table 2.

![image 82](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile82.png>)

TABLE 2. Parameters (αi,ρi)4i=0 for (n,N,NW) = (3,32,735/23). i 0 1 2 3 4

![image 83](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile83.png>)

![image 84](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile84.png>)

![image 85](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile85.png>)

![image 86](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile86.png>)

![image 87](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile87.png>)

![image 88](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile88.png>)

![image 89](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile89.png>)

![image 90](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile90.png>)

![image 91](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile91.png>)

![image 92](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile92.png>)

![image 93](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile93.png>)

![image 94](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile94.png>)

![image 95](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile95.png>)

![image 96](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile96.png>)

![image 97](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile97.png>)

![image 98](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile98.png>)

αi −0.9412 −0.6741 −0.2109 0.3281 0.7793 ρi 0.0771 0.1889 0.2636 0.2612 0.1777

![image 99](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile99.png>)

![image 100](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile100.png>)

![image 101](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile101.png>)

![image 102](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile102.png>)

![image 103](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile103.png>)

![image 104](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile104.png>)

![image 105](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile105.png>)

![image 106](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile106.png>)

![image 107](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile107.png>)

Therefore,

4

Eh(W) ≥ ULB9(W,h) =

ρih(αi) ≈ 0.804786, which is very close (within 0.03%) to the actual h-energy ≈ 0.8050318 of (C32,W).

i=0

It is worth mentioning that in the equi-weighted case, the Coulomb energy of (C32,(1/32)32) is Eh(C32,((1/32)32)) ≈ 0.8052 and the universal lower bound from [9] for (n,N) = (3,32) and the same h is ≈ 0.8049.

- Example 2.6. (Union of cube and cross-polytope.) We consider a weighted code (Cqp,W) comprised of the union of a cube and a cross-polytope on Sn−1 deﬁned by their duality; i.e., each pair of antipodal vertices of the cross-polytope deﬁnes a symmetry axis of two opposite facets of the cube. Each point of the cross-polytope has weight wp := 1/(2n + n2) and each point of the cube has weight wc := n2/2n(2n + n2). We see that the sum of weights of the union is 1. Furthermore, (Cqp,W) is a weighted 5-design on Sn−1 for n ≥ 3, as we now show.


Indeed, since Cqp is antipodal and the weights of points in each antipodal pair are equal, all odd (in particular the ﬁrst, third, and ﬁfth) weighted moments (3) of (Cqp,W) equal zero. To show that the fourth weighted moment is zero, we denote by Q the set of vertices of the cube and by P the set of vertices of the cross-polytope in (Cqp,W) and observe that for every x = (x1,... ,xn) ∈ Sn−1,

(x · y)4

(x · y)4 + wp

U4(x) : = wc

y∈P

y∈Q

n

wc n2

x4i

(σ1x1 + ··· + σnxn)4 + 2wp

=

![image 108](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile108.png>)

i=1

σ1,...,σn∈{−1,1}

   + 2wp

  

n

n

n

n

2nwc n2

x4i

x2ix2j

x4i + 3

=

![image 109](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile109.png>)

(18)

i=1

i=1

i=1

j=1 j =i

  

  

n

n

n

3 2n + n2

x2ix2j

x4i +

=

![image 110](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile110.png>)

i=1

i=1

j=1 j =i

1

3 2n + n2

3 2n + n2

x21 + ··· + x2n 2 =

t4(1 − t2)n−23 dt.

=

= γn

![image 111](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile111.png>)

![image 112](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile112.png>)

![image 113](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile113.png>)

−1

Using a similar argument, we can also show that

U2(x) := wc

(x · y)2 + wp

y∈Q

1 n

(x · y)2 =

y∈P

= γn

![image 114](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile114.png>)

1

t2(1 − t2)n−23 dt, x ∈ Sn−1.

![image 115](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile115.png>)

−1

Consequently,

P2(n)(x · y) + wp

wc

y∈P

y∈Q

P2(n)(x · y) = 0, x ∈ Sn−1. (19)

Finally, expressing P4(n) from the Gegenbauer expansion of t4 and using (18), (19), and the fact that (18) equals the constant term in the Gegenbauer expansion of t4, we obtain that

P4(n)(x · y) + wp

wc

y∈P

y∈Q

P4(n)(x · y) = 0, x ∈ Sn−1,

which together with (19) implies that the second and the fourth weighted moments (3) of (Cqp,W) equal zero. Thus, (Cqp,W) is a weighted 5-design.

For n = 2, (Cqp,W) is a regular 8-gon and the weights are equal; i.e. it is a tight spherical 7-design. Therefore, it is a sharp spherical code and a universally optimal conﬁguration [14].

In three and four dimensions, the codes (Cqp,W) can be described as follows. On S2, each point of the cross-polytope will have weight 1/15 and each point of the cube will have weight 3/40, giving a weighted spherical 5-design of 14 points; on S3, each point of the cross-polytope will have weight 1/24 and each point of the cube will also have weight 1/24 (thus, we obtain a 24-cell, an equi-weighted spherical 5-design; see [13]). Note that there exist no equi-wegthed spherical 5-designs with 13 points [6] and the existence of such designs with 14 points is undecided.

For any h, the actual weighted h-energy of (Cqp,W) is Eh(Cqp,W) = 2nwp2 (h(−1) + (2n − 2)h(0))

1 √n

1 √n

+2n+1nwpwc h

+ h −

![image 116](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile116.png>)

![image 117](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile117.png>)

![image 118](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile118.png>)

![image 119](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile119.png>)

n−1

n k

2k n

+2nwc2

h −1 +

.

![image 120](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile120.png>)

k=0

The ULB for the corresponding parameters (n,|Cqp| = 2n + 2n,NW), where

n(n + 2)22n n3 + 2n+1

1 2nwp2 + 2nwc2

1

=

=

NW =

![image 121](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile121.png>)

![image 122](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile122.png>)

![image 123](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile123.png>)

2n+2n i=1 wi2

(note that NW ∈ (D(n,5),D(n,6)] for 3 ≤ n ≤ 6 only), is computed as follows. We solve

(n + 2)(n + 3)s2 + 4(n + 2)s − n + 1 (1 − s) 2s (3 − (n + 2)s2)

(n + 2)22n n3 + 2n+1

L5(n,s) = NW ⇐⇒

=

![image 124](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile124.png>)

![image 125](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile125.png>)

to obtain the nodes (αi)2i=0. Then the quadrature weights (ρi)2i=0 are computed by setting f equal to the Lagrange basis polynomials in (14) or by the known formulas

(1 − α20)(1 − α22) α1NW(α21 − α20)(α21 − α22)

(1 − α21)(1 − α22) α0NW(α20 − α21)(α20 − α22)

, ρ1 = −

ρ0 = −

![image 126](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile126.png>)

![image 127](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile127.png>)

- from [8] and the relation ρ0 + ρ1 + ρ2 = 1 − 1/NW. The ULB in dimensions 2 ≤ n ≤ 7, calculated for the absolutely monotone potential


1 (2(1 − t))(n−2)/2

h(t) =

,

![image 128](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile128.png>)

are shown in the sixth column of Table 3. It is ULB7(W,h) for n = 2, ULB5(W,h) for 3 ≤ n ≤ 6 and ULB6(W,h) for n = 7. Note that the bound ULB7(W,h) is attaned for n = 2, where it coincides with the ULB for the equi-weighted case [9] (recall that the attaining (Cqp,W) is an equi-weighted regular 8-gon).

We remark that the h-energy in the equi-weighted case and the corresponding ULB from [9] for the 14-point Cqp in three dimensions are ≈ 0.70757 and ≈ 0.70629, respectively.

TABLE 3. Approximate parameters and ULB for (n,N,NW) = (n,2n+2n,NW), 2 ≤ n ≤ 7, h(t) = (2(1 − t))−(n−2)/2.

![image 129](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile129.png>)

![image 130](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile130.png>)

![image 131](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile131.png>)

![image 132](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile132.png>)

![image 133](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile133.png>)

![image 134](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile134.png>)

![image 135](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile135.png>)

![image 136](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile136.png>)

![image 137](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile137.png>)

n NW N (αi) (ρi) ULB Energy of (Cqp,W) −1 1/8

![image 138](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile138.png>)

![image 139](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile139.png>)

![image 140](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile140.png>)

![image 141](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile141.png>)

![image 142](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile142.png>)

![image 143](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile143.png>)

![image 144](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile144.png>)

![image 145](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile145.png>)

![image 146](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile146.png>)

![image 147](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile147.png>)

- 2 8 8 −

![image 148](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile148.png>)

![image 149](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile149.png>)

![image 150](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile150.png>)

√2/2 1/4 0.875 0.875

![image 151](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile151.png>)

![image 152](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile152.png>)

![image 153](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile153.png>)

![image 154](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile154.png>)

![image 155](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile155.png>)

![image 156](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile156.png>)

![image 157](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile157.png>)

![image 158](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile158.png>)

![image 159](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile159.png>)

√20/2 11//44 −0.8580 0.1832

![image 160](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile160.png>)

![image 161](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile161.png>)

![image 162](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile162.png>)

![image 163](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile163.png>)

![image 164](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile164.png>)

![image 165](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile165.png>)

![image 166](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile166.png>)

![image 167](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile167.png>)

![image 168](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile168.png>)

![image 169](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile169.png>)

![image 170](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile170.png>)

![image 171](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile171.png>)

![image 172](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile172.png>)

![image 173](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile173.png>)

![image 174](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile174.png>)

![image 175](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile175.png>)

![image 176](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile176.png>)

![image 177](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile177.png>)

![image 178](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile178.png>)

![image 179](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile179.png>)

![image 180](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile180.png>)

![image 181](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile181.png>)

![image 182](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile182.png>)

- 3 13.95 14 −0.2701 0.3832 0.7058 0.7070 0.5225 0.3618

![image 183](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile183.png>)

![image 184](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile184.png>)

![image 185](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile185.png>)

![image 186](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile186.png>)

![image 187](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile187.png>)

![image 188](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile188.png>)

![image 189](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile189.png>)

![image 190](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile190.png>)

![image 191](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile191.png>)

![image 192](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile192.png>)

![image 193](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile193.png>)

![image 194](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile194.png>)

![image 195](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile195.png>)

![image 196](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile196.png>)

![image 197](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile197.png>)

![image 198](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile198.png>)

![image 199](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile199.png>)

![image 200](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile200.png>)

![image 201](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile201.png>)

![image 202](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile202.png>)

−0.8173 0.1384

![image 203](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile203.png>)

![image 204](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile204.png>)

![image 205](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile205.png>)

![image 206](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile206.png>)

![image 207](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile207.png>)

- 4 24 24 −0.2575 0.4339 0.5781 0.5798 0.4749 0.3858

![image 208](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile208.png>)

![image 209](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile209.png>)

![image 210](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile210.png>)

![image 211](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile211.png>)

![image 212](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile212.png>)

![image 213](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile213.png>)

![image 214](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile214.png>)

![image 215](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile215.png>)

![image 216](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile216.png>)

![image 217](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile217.png>)

![image 218](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile218.png>)

![image 219](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile219.png>)

![image 220](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile220.png>)

![image 221](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile221.png>)

![image 222](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile222.png>)

![image 223](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile223.png>)

![image 224](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile224.png>)

![image 225](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile225.png>)

![image 226](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile226.png>)

![image 227](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile227.png>)

−0.7428 0.1424

![image 228](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile228.png>)

![image 229](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile229.png>)

![image 230](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile230.png>)

![image 231](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile231.png>)

![image 232](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile232.png>)

- 5 41.48 42 −0.1910 0.4680 0.4825 0.4901 0.4684 0.3653

![image 233](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile233.png>)

![image 234](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile234.png>)

![image 235](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile235.png>)

![image 236](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile236.png>)

![image 237](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile237.png>)

![image 238](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile238.png>)

![image 239](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile239.png>)

![image 240](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile240.png>)

![image 241](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile241.png>)

![image 242](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile242.png>)

![image 243](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile243.png>)

![image 244](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile244.png>)

![image 245](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile245.png>)

![image 246](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile246.png>)

![image 247](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile247.png>)

![image 248](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile248.png>)

![image 249](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile249.png>)

![image 250](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile250.png>)

![image 251](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile251.png>)

![image 252](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile252.png>)

−0.6753 0.1540

![image 253](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile253.png>)

![image 254](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile254.png>)

![image 255](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile255.png>)

![image 256](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile256.png>)

![image 257](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile257.png>)

- 6 71.44 76 −0.1327 0.4996 0.4074 0.4314 0.4705 0.3323

![image 258](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile258.png>)

![image 259](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile259.png>)

![image 260](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile260.png>)

![image 261](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile261.png>)

![image 262](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile262.png>)

![image 263](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile263.png>)

![image 264](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile264.png>)

![image 265](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile265.png>)

![image 266](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile266.png>)

![image 267](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile267.png>)

![image 268](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile268.png>)

![image 269](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile269.png>)

![image 270](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile270.png>)

![image 271](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile271.png>)

![image 272](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile272.png>)

![image 273](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile273.png>)

![image 274](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile274.png>)

![image 275](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile275.png>)

![image 276](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile276.png>)

![image 277](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile277.png>)

−1 0.0022

![image 278](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile278.png>)

![image 279](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile279.png>)

![image 280](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile280.png>)

![image 281](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile281.png>)

![image 282](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile282.png>)

- 7 121.16 142 −0.5936 0.1785 0.3462 0.3993 −0.0772 0.5165


![image 283](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile283.png>)

![image 284](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile284.png>)

![image 285](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile285.png>)

![image 286](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile286.png>)

![image 287](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile287.png>)

![image 288](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile288.png>)

![image 289](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile289.png>)

![image 290](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile290.png>)

![image 291](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile291.png>)

![image 292](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile292.png>)

![image 293](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile293.png>)

![image 294](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile294.png>)

![image 295](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile295.png>)

![image 296](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile296.png>)

![image 297](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile297.png>)

![image 298](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile298.png>)

![image 299](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile299.png>)

![image 300](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile300.png>)

![image 301](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile301.png>)

![image 302](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile302.png>)

![image 303](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile303.png>)

![image 304](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile304.png>)

![image 305](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile305.png>)

0.4748 0.2944

![image 306](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile306.png>)

Many other examples from the classical sources [34, 36, 35, 31, 23] can be similarly explored. Also, one can derive upper bounds from the next section and bounds for weighted spherical designs in the last section.

3. ON THE OPTIMALITY OF THE ULB

We showed in Theorem 2.3 that the bound (15) cannot be improved by using polynomials of degree m or less. We shall extend this result by proving a necessary and sufﬁcient condition for the optimality of (15) among polynomials from the whole set L(hn).

With parameters as in Theorem 2.3 we deﬁne the functions

k−1+ε

1 NW

ρiPj(n)(αi), j ≥ 1, (20) and call them test functions. The name will be justiﬁed by Theorem 3.1.

Qj(n,s) :=

+

![image 307](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile307.png>)

i=0

It is easy to see that Qj(n,s) ≡ 0 for j ∈ {1,2,... ,m} (because in this case the right-hand side in (20) is equal, via the quadrature (14), to the coefﬁcient f0 of the Gegenbauer polynomial Pj(n),

which clearly equals 0). The next theorem, which is a weighted analog of Theorems 2.6 and 4.1

- from [9] (see also Theorem 3.1 in [7] and Theorem 5.47 in [28]), shows that the values of the test functions Qj(n,s) for j ≥ m + 1 are as meaningful as their signs are.


- Theorem 3.1. Let h be absolutely monotone. For given n, NW, and parameters m and (αi,ρi)ik=0−1+ε


- as in Theorem 2.3, the following is true.


- (a) If Qj(n,s) ≥ 0 for every positive integer j, then the bound ULBm(W,h) cannot be improved

by any polynomial from Lh(n); i.e.,

ULB(W,h) = ULBm(W,h).

- (b) If h is strictly absolutely monotone, h(i)(−1) > 0 for all i ≥ 0, and Qj(n,s) < 0 for some


positive integer j ≥ m + 1, then there exists a polynomial from L(hn) of degree j that gives a bound on Eh(W) better than ULBm(W,h); i.e.,

ULB(W,h) > ULBm(W,h).

Proof. (a) Let us assume that f ∈ L(hn) has degree d ≥ m + 1 (the case d ≤ m is covered by Theorem 2.3). We decompose f as

d

fjPj(n)(t), (21)

f(t) = g(t) +

j=m+1

where g ∈ Pm. Note that f0 = g0 and fj ≥ 0 for every relevant j. Using the quadrature (14) for h and the representation (21), we consecutively reorganize and ﬁnally estimate from above the bound generated by f as follows:

f(1) NW

f0 −

![image 308](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile308.png>)

= g0 −

=

g(1) NW

![image 309](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile309.png>)

=

=

=

≤

k−1+ε

i=0

k−1+ε

i=0

k−1+ε

i=0

k−1+ε

i=0

f(1) NW

![image 310](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile310.png>)

 g(1) +

 

d

k−1+ε

1 NW ·

fj

ρig(αi) −

+

![image 311](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile311.png>)

j=m+1

i=0

  −

 f(αi) −

d

d

1 NW ·

fjPj(n)(αi)

ρi

fj

![image 312](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile312.png>)

j=m+1

j=m+1

d

k−1+ε

1 NW

ρiPj(n)(αi)

fj

ρif(αi) −

+

![image 313](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile313.png>)

j=m+1

i=0

d

fjQj(n,s)

ρif(αi) −

j=m+1

ρih(αi) = ULBm(W,h),

where, for the last inequality, we used fi ≥ 0 and Qj(n,s) ≥ 0 for j = m + 1,... ,d. (b) We shall ﬁnd an improvement of the bound ULBm(W,h) by using the polynomial

f(t) = g(t) + µPj(n)(t), where the constant µ > 0 and the polynomial g(t) ∈ Pm will be suitably chosen. We ﬁrst deﬁne an auxiliary potential

h(t) := h(t) − µPj(n)(t),

where µ > 0 is chosen in such a way that the derivatives h(i)(t) ≥ 0 on [−1,1) for all i = 0,1,... ,j. Since h(i)(t) = h(i)(t) > 0 for i ≥ j + 1, this choice of µ makes the new potential h(t) absolutely monotone.

Next, we choose the polynomial g(t) as the Hermite interpolant of h at the nodes (αi)ik=0−1+ε in exactly the same way as we constructed f to interpolate h in Theorem 2.3; i.e.,

g(αi) = h(αi), g′(αi) = h′(αi), i = 0,1,... ,k − 1 + ε, where the interpolation is simple if and only if (ε,i) = (1,0). It follows in the same way is in Theorem 2.3 that g ∈ L( hn), implying immediately that f ∈ L(hn).

In what follows in the proof we compute the bound from f and show that it is greater than

ULBm(W,h). Let g(t) = mℓ=0 gℓPℓ(n)(t) be the Gegenbauer expansion of g. Note that f0 = g0 and f(1) = g(1) + µ. We have

k−1+ε

k−1+ε

ρi h(αi)

ρig(αi) =

i=0

i=0

k−1+ε

k−1+ε

ρiPj(n)(αi)

ρih(αi) − µ ·

=

i=0

i=0

k−1+ε

ρiPj(n)(αi). Since

= ULBm(W,h) − µ ·

i=0

k−1+ε

g(1) NW

ρig(αi) = g0 −

![image 314](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile314.png>)

i=0

by the formula (14) for g and

k−1+ε

1 NW by the deﬁnition of the test functions (20), we obtain

ρiPj(n)(αi) = Qj(n,s) −

![image 315](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile315.png>)

i=0

µ NW − µQj(n,s).

g(1) NW

= ULBm(W,h) +

g0 −

![image 316](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile316.png>)

![image 317](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile317.png>)

But the left-hand side is equal to f0 − (f(1) − µ)/NW, and so

f(1) NW

= ULBm(W,h) − µQj(n,s) > ULBm(W,h), showing that the bound from the polynomial f is better than ULBm(W,h).

f0 −

![image 318](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile318.png>)

The better bound deduced from the polynomial f from Theorem 3.1(b) can be computed numerically but it seems to not be the best that can be obtained by higher degree polynomials. A technique, called skip 2-add 2, was developed for obtaining bounds via higher degree polynomials in the equi-weighted case in [12]. It can be applied for weighted codes as well.

The same test functions were deﬁned and investigated in the case of upper bounds2 for the maximal cardinality of spherical codes of given dimension and maximal inner product in [7]. It follows from the investigation from [7] that the ﬁrst two nonzero test functions, Qm+1(n,s) and Qm+2(n,s), are always non-negative. This means that the assumption Qj(n,s) < 0 in Theorem

- 3.1 (b) is possible only for j ≥ m + 3; i.e., the degree of an improving polynomial (if any) will be

at least m + 3.

- 4. UNIVERSAL UPPER BOUNDS FOR ENERGY OF WEIGHTED CODES WITH GIVEN MINIMUM DISTANCE


- 4.1. A general linear programming upper bound for weighted codes. We assume now that (C,W) is a weighted spherical code on Sn−1 with |C| = |W| = N and maximal inner product s(C) ∈ [−1,1) (equivalently, minimum distance d(C) = 2(1 − s(C)). In the sequel, we shall often omit C in the notation of the maximal inner product. Then it is natural to consider upper bounds for the quantity Uh(s,W) deﬁned in (2). As with Theorem 2.1 we ﬁrst derive a general linear program.


![image 319](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile319.png>)

We now deﬁne the admissible set of polynomials for linear programming as

 

 

deg(g)

Uh(n,s) :=

giPi(n)(t) : g(t) ≥ h(t),t ∈ [−1,s],gi ≤ 0,i = 1,... ,deg(g)

g(t) =

.





i=0

Then every polynomial from the set Uh(n,s) provides a upper bound for Uh(s,W) as shown in the next theorem.

- Theorem 4.1. Let s ∈ [−1,1) and g ∈ Uh(n,s). Then for every weighted code (C,W) on Sn−1 with tuple size N and maximal inner product s(C) = s,


N

wi2.

Eh(C,W) ≤ Eg(C,W) ≤ g0 − g(1)

i=1

![image 320](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile320.png>)

2In this case the universal bound is the Levenshtein bound.

Consequently,

Uh(s,W) ≤ inf

g∈Uh(n,s)

g0 − g(1)

N

wi2 . (22)

i=1

Proof. The ﬁrst inequality follows obviously from g ≥ h in [−1,s] since all inner products of C belong to that interval; i.e.,

Eh(C,W) =

wiwjh(xi · xj) ≤

i =j

wiwjg(xi · xj) = Eg(C,W).

i =j

For the second inequality, we estimate Eg(C,W) from above as follows:

Eg(C,W) =

i,j

N

wi2

wiwjg(xi · xj) − g(1)

i=1

=

deg(g)

gℓ

ℓ=0

i,j

≤ g0 − g(1)

N

wiwjPℓ(n)(xi · xj) − g(1)

wi2

i=1

N

wi2.

i=1

2

= 1, gℓ ≤ 0 for ℓ ≥ 1, and i,j wiwjPℓ(n)(xi · xj) = Mℓ(C,W) ≥ 0 for ℓ ≥ 1. Since (C,W) was arbitrary with tuple size |C| = N and maximal inner product s, (22) follows.

We used that Ni=1 wi

By analogy with the ULB case we consider the inﬁmum in (22) over the class of polynomials Uh(n,s) ∩ Pm. Thus, we obtain the linear program

 

N

wi2 subject to g ∈ Uh(n,s) ∩ Pm.

minimize g0 − g(1)

(23)



i=1

- 4.2. A construction of feasible polynomials. We next construct polynomials in Uh(n,s) to be used in the linear program (23). We derive the necessary parameters and then follow the approach from the equi-weighted case [11].


Given a weighted spherical code (C,W) (in particular, a weight vector W) with maximal inner product s(C) = s we can ﬁnd NW and m as before. However, the main role here will be played by another parameter denoted by Nq.

Referring to the partition [−1,1) = ∪∞j=1Ij (see Section 2.2), we ﬁnd the unique positive integer q such that

s ∈ Iq = t1ℓ−,11+−εε,t1ℓ,ε ,

where q = 2ℓ − 1 + ε, ε ∈ {0,1} indicates the parity of q. Then we proceed with introduction of the additional parameter

fq(n,s)(1) f0

,

Nq := Lq(n,s) =

![image 321](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile321.png>)

(recall that fq(n,s)(t) is the Levenshtein polynomial corresponding to s ∈ Iq (i.e., the polynomial, used by Levenshtein for obtaining the bound Lq(n,s). Thus, Nq determines upper bound param-

eters (αi(n,s),ρi(n,s))iℓ=0−1+ε in the same way as NW does for the lower bound parameters (αi,ρi) in Theorem 2.3.

If Nq < N, the Levenshtein bound implies that there exist no C ⊂ Sn−1 with |C| = N and s(C) = s. Therefore, Nq ≥ N (with equality in the latter case following if and only if the equiweighted code C ⊂ Sn−1 with |C| = N = |W| attains the Levenshtein bound; i.e., it is universally optimal) and q ≥ m. We also note that Nq ≥ N means that s cannot be too small in Iq; in fact, it belongs to a subinterval of Iq whose left end is the largest solution of Lq(n,s) = N (see section

- 4.3 for explicit expressions of that left end in the cases q = 1 and 2).


In the next theorem we construct feasible polynomials g ∈ Uh(n,s) ∩ Pq, where q is determined by s as above, and compute the corresponding universal upper bound (UUB).

- Theorem 4.2. (UUB for weighted codes) Let W be a weight vector with NW = 1/ Ni=1 wi2. Let


s ∈ Iq = [tℓ1−,11+−εε,t1ℓ,ε], q = 2ℓ − 1 + ε, ε ∈ {0,1}, be such that Lq(n,s) = Nq ≥ N = |W| and h satisfy h(q) ≥ 0 on [−1,s]. Then

Nq NW

gT(1) NW

Uh(s,W) ≤ −λ∗f0 1 −

, (24)

+ (gT)0 −

![image 322](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile322.png>)

![image 323](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile323.png>)

where T is the set of nodes in [−1,s] speciﬁed below in (26) and (27) and gT is the Hermite interpolating polynomial to h in the nodes T; furthermore, f0 is the zeroth Gegenbauer coefﬁcient of the Levenshtein polynomial fq(n,s) and λ∗ is a constant deﬁned below in (28).

Proof. We consider the polynomials

q

giPi(n)(t), (25) where λ ≥ 0 is a parameter (to be determined later) and

g(t) := −λfq(n,s)(t) + gT(t) =

i=0

q−1

(gT)iPi(n)(t) (26)

gT(t) := Hh,T(t) =

i=0

is the Hermite interpolating polynomial to the function h(t) that agrees with h(t) exactly in the points of a multiset T that will be deﬁned now.

With q in the role of m from the lower bounds case, we denote q = 2ℓ − 1 + ε, ε ∈ {0,1} giverning the parity of q, and by

α0(n,s) < α1(n,s) < ··· < αℓ(n,s−2+) ε < αℓ(n,s−1+) ε = s

the roots of the Levenshtein polynomial fq(n,s)(t). We deﬁne

 

{α0(n,s),α0(n,s),α1(n,s),α1(n,s),... ,αℓ(n,s−2),αℓ(n,s−2),αℓ(n,s−1) = s} if q = 2ℓ − 1 {α0(n,s) = −1,α1(n,s),α1(n,s),... ,αℓ(n,s−1),αℓ(n,s−1),αℓ(n,s) = s} if q = 2ℓ

T :=

(27)



to be the multiset of these roots counted with their multiplicities. Note that deg(gT) = q − 1.

In a sense, we use the polynomial fq(n,s) to “adjust” gT in order to obtain a suitable g ∈ Uh(n,s). Indeed, we have gT(t) ≥ h(t) for t ∈ [−1,s] from the interpolation (as described above) and the error formula in the Hermite interpolation

ℓ−2+ε

h(q)(ξ) q!

(t − αi(n,s))2, ξ ∈ (−1,1),

(t − α0(n,s))2−ε(t − s)

h(t) − gT(t) =

![image 324](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile324.png>)

i=1

(note we interpolate only the value of h at s). Since fq(n,s)(t) ≤ 0 for t ∈ [−1,s] and λ > 0, we conclude that

g(t) = −λfq(n,s)(t) + gT(t) ≥ h(t), t ∈ [−1,s].

Moreover, since fi > 0, i = 1,... ,q, in the Gegenbaeur expansion of the Levenshtein polynomial

q

fiPi(n)(t) (see, e.g., [28, Theorem 5.42]), it is clear that large enough λ > 0 will ensure that

fq(n,s)(t) =

i=0

gi = −λfi + (gT)i ≤ 0, i = 1,2,... ,q − 1, gq = −λfq < 0 showing that g ∈ Uh(n,s) for such λ. Finally, combining the interpolation conditions and the properties of the Levenshtein polynomial (i.e., gT(αi(n,s)) = h(αi(n,s)) and fq(n,s)(αi(n,s)) = 0), we see that g(αi(n,s)) = h(αi(n,s)). Note that g′(αi(n,s)) = h′(αi(n,s)) follows also (except in the cases α0(n,s) = −1 and i = ℓ − 1 + ε) from (25) since fq(n,s)

′

(αi(n,s)) = 0 in all relevant cases.

Assume that we have chosen λ = λ0 such that g(t) = −λ0fq(n,s)(t) + gT(t) belongs to Uh(n,s). Then the bound provided via the so-chosen g(t) in Theorem 4.1 can be calculated as follows:

N

wi2

Uh(s,W) ≤ g0 − g(1)

i=1

N

wi2

= −λ0f0 + (gT)0 − (−λ0fq(n,s)(1) + gT(1))

i=1

N

N

wi2

wi2 + (gT)0 − gT(1)

= −λ0f0 1 − Lq(n,s)

i=1

i=1

Nq NW

gT(1) NW

= −λ∗f0 1 −

+ (gT)0 −

![image 325](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile325.png>)

![image 326](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile326.png>)

(note the presence of the coefﬁcient f0 of the Levenshtein polynomial fq(n,s)). We recall that Nq = Lq(n,s) = fq(n,s)(1)/f0 ≥ N ≥ NW.

The linear dependence on λ0 of the bound means that λ0 must be as small as possible. Summarizing the requirements for the best value of λ0, which we denote by λ∗, we conclude that

λ∗ := max

(gT)i fi

: i ∈ I(gT) , (28)

![image 327](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile327.png>)

where I(gT) := {i ∈ {1,2,... ,q − 1} : (gT)i > 0} is the set of the indices of the positive coefﬁcients in the Gegenbauer expansion of gT (we choose λ∗ = 0 if the set I(gT) is empty). This completes the proof.

We emphasize the difference between the deﬁnitions of the nodes (αi)ik=0−1+ε for the lower bounds (Section 2) and (αi(n,s))iℓ=0−1+ε for the upper bounds (this section). In the case of ULB we ﬁnd the nodes via the equation (13); i.e., they are deﬁned via NW = 1/ Ni=1 wi2, while for UUB we derive them as roots of the polynomial fq(n,s)(t) used for obtaining the Levenshtein bound Lq(n,s) for the given s; i.e., they are deﬁned via the number s.

- Remark 4.3. If h is absolutely monotone, then gT is positive deﬁnite as in Theorem 2.3; i.e. I(gT) = {1,2,... ,q − 1} and

λ∗ := max

(gT)1 f1

![image 328](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile328.png>)

,... ,

(gT)q−1 fq−1

![image 329](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile329.png>)

, q > 1, (29) and λ∗ = 0 for q = 1.

The quadrature rule (14) for gT with Nq gives

(gT)0 −

gT(1) Nq

![image 330](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile330.png>)

=

ℓ−1+ε

i=0

ρi(n,s)gT(αi(n,s)) =

ℓ−1+ε

i=0

ρi(n,s)h(αi(n,s)),

where gT(αi(n,s)) = h(αi(n,s)), i = 0,1,... ,ℓ − 1 + ε, from the interpolation. Using this, we can write the bound (24) as follows:

Uh(s,W) ≤ −λ∗f0 +

gT(1) Nq

![image 331](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile331.png>)

1 −

Nq NW

![image 332](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile332.png>)

+

ℓ−1+ε

i=0

ρi(n,s)h(αi(n,s)). This formula involves the potential h explicitly.

- Remark 4.4. We remark that in [11, Theorem 3.2] the requirement of absolute monotonicity of h can be weakened in the same way as in Theorem 4.2.
- Remark 4.5. Let q′ be a positive integer in [m,q]. As proved in [27, Section 4], the function Lq′(n,s) can be deﬁned in a larger interval whose left end coincides with the left end of Iq′ and whose right end is t0r,ǫ > t1r,ǫ, where q′ = 2r − 1 + ǫ. The image of this extension is the interval [D(n,q′),+∞). Our s can belong to such an extended interval, where we can ﬁnd Nq′ = Lq′(n,s)


and can proceed with upper bounds as in Theorem 4.2. However, such bounds will involve less nodes and weights and will be weaker.

- 4.3. Small degrees UUB. We present explicitly degree one and two UUB. They are valid for Nq ∈ (D(n,q),D(n,q + 1)] and s in a certain interval whose left endpoint is determined from the Levenshtein bound Nq = Lq(n,s) ≥ N.


For s ∈ [−1/(N − 1),−1/n] ⊃ I1 to generate N1 ∈ (N,n + 1] we consider the degree one UUB (24), where the parameters are determined as follows: q = 1, L1(n,s) = (s − 1)/s = N1 as in section 2.5,

g(t) = −λf1(n,s)(t) + gT(t) = −λ(t − s) + gT(t)

is our linear programming polynomial (25), and α0(n,s) = s, ρ0(n,s) = 1/(1−s) are the corresponding Levenshtein’s parameters. Then the polynomial gT(t) has degree q − 1 = 0; i.e., it is a constant which is found from the interpolation equality gT(s) = h(s). Thus λ∗ = 0 and we ﬁnd f(t) = h(s) giving the (trivial) bound

N

1 NW

wi2 h(s) = 1 −

Uh(s,W) ≤ 1 −

h(s).

![image 333](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile333.png>)

i=1

Indeed, this bound is straightforward upon estimating all terms in the energy sum Eh(C,W) from above by the constant h(s) and taking into account that w1 + ··· + wN = 1.

Fors ∈ [(N − 2n)/n(N − 2),0] ⊃ I2 to give N2 ∈ (N,2n] we consider (24) for degree q = 2. Let

N2 = L2(n,s) = 2n(1 − s)/(1 − ns). We construct the UUB polynomial

g(t) = −λf2(n,s)(t) + gT(t) = −λ(t + 1)(t − s) + gT(t) as described in Theorem 4.2. The Levenshtein’s parameters can be computed as in section 2.5 but we need α0(n,s) = −1 and α1(n,s) = s only. The degree one polynomial gT(t) is found from the interpolation set T = {−1,s}; whence gT(−1) = h(−1) and gT(s) = h(s). Thus,

h(s) + sh(−1) 1 + s

h(s) − h(−1) 1 + s · t +

.

gT(t) =

![image 334](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile334.png>)

![image 335](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile335.png>)

The coefﬁcient λ∗ is chosen to make g1 = 0 in the Gegenbauer expansion g(t) = g0 +g1P1(n)(t) + g2P2(n)(t) (there is only one element in the set from (28)). This gives

h(s) − h(−1) 1 − s2 and, therefore,

λ∗ =

![image 336](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile336.png>)

h(s) − s2h(−1) 1 − s2

h(s) − h(−1) 1 − s2 · t2 +

g(t) = −

. We can use now directly Theorem 4.1. Since

![image 337](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile337.png>)

![image 338](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile338.png>)

(n − 1)h(s) + (1 − ns2)h(−1) n(1 − s2)

, g(1) = h(−1),

g0 =

![image 339](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile339.png>)

we obtain

(n − 1)h(s) + (1 − ns2)h(−1) n(1 − s2) −

h(−1) NW

g(1) NW

Uh(s,W) ≤ g0 −

=

.

![image 340](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile340.png>)

![image 341](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile341.png>)

![image 342](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile342.png>)

The degree three UUB is quite complicated to be stated here. However, numerical calculations are feasible as in the case of ULB.

- 4.4. Examples. We compute the UUB from Theorem 4.2 for the cases discussed in Section 2. Thereby, we obtain a strip where the weighted h-energy belongs for given n, h, and W (and s for the upper bounds).


- Example 4.6. We consider the case of the weighted code (C32,W) ⊂ S2 from Example 2.5. Since the maximal inner product of C32 is

s = s(C32) = 1 + 2/

![image 343](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile343.png>)

√

![image 344](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile344.png>)

5/

√

![image 345](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile345.png>)

3 ≈ 0.794654 ∈ I9 = [0.765055... ,0.80293...]

(this is the constant b from Example 2.5), we compute the UUB for Uh(s,W) for the parameters n = 3, the above s implying that q = 9, N9 = L9(3,s) = 34.4268..., and for the Coulomb potential h(t) = 1/ 2(1 − t).

![image 346](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile346.png>)

The interpolation nodes are the roots of the Levenshtein polynomial f9(3,s); i.e., (α(3i ,s))4i=0 ≈ (−0.9247,−0.6213,−0.1493,0.3703,0.7946).

The polynomial gT is positive deﬁnite (i.e., (gT)i ≥ 0 for all i and we use (29); this is, in fact, part of more general property) and

λ∗ =

(gT)1 f1 ≈ 7.47994 via (28). Thus our UUB polynomial g has g1 = 0 and gi < 0 for 2 ≤ i ≤ 9. Finally, the UUB is Uh(s,W) ≤ 0.8234054.

![image 347](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile347.png>)

We recall from Example 2.5 that the actual Coulomb energy of (C32,W) is ≈ 0.8050318 and the ULB is ≈ 0.804786.

- Example 4.7. We compute the UUB for the parameters from the weighted codes from Example 2.6. For convenience and comparison, we recall the actual energy and the ULB from that example. The results are shown in Table 4.


5. ULB AND UUB FOR WEIGHTED SPHERICAL DESIGNS

In the case when a weighted spherical code is also a weighted design, the ULB and UUB may be extended to wider class of potentials, which we now describe.

TABLE 4. Approximate parameters and UUB for (n,N,NW,s,Nq) = (n,2n + 2n,NW,s,Nq), 3 ≤ n ≤ 7, h(t) = (2(1 − t))−(n−2)/2.

![image 348](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile348.png>)

![image 349](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile349.png>)

![image 350](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile350.png>)

![image 351](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile351.png>)

![image 352](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile352.png>)

![image 353](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile353.png>)

![image 354](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile354.png>)

![image 355](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile355.png>)

![image 356](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile356.png>)

![image 357](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile357.png>)

![image 358](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile358.png>)

n NW N s q Nq ULB Energy of (Cqp,W) UUB

- 3 13.95 14 1/√3 5 16.098 0.7058 0.7070 0.7357

![image 359](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile359.png>)

![image 360](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile360.png>)

![image 361](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile361.png>)

![image 362](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile362.png>)

![image 363](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile363.png>)

![image 364](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile364.png>)

![image 365](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile365.png>)

![image 366](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile366.png>)

![image 367](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile367.png>)

![image 368](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile368.png>)

![image 369](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile369.png>)

![image 370](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile370.png>)

- 4 24 24 1/2 5 26 0.5781 0.5798 0.5988

![image 371](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile371.png>)

![image 372](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile372.png>)

![image 373](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile373.png>)

![image 374](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile374.png>)

![image 375](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile375.png>)

![image 376](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile376.png>)

![image 377](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile377.png>)

![image 378](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile378.png>)

![image 379](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile379.png>)

![image 380](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile380.png>)

![image 381](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile381.png>)

- 5 41.48 42 3/5 6 81.351 0.4825 0.4901 0.708

![image 382](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile382.png>)

![image 383](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile383.png>)

![image 384](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile384.png>)

![image 385](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile385.png>)

![image 386](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile386.png>)

![image 387](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile387.png>)

![image 388](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile388.png>)

![image 389](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile389.png>)

![image 390](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile390.png>)

![image 391](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile391.png>)

![image 392](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile392.png>)

- 6 71.44 76 2/3 7 289.561 0.4074 0.4314 1.0421

![image 393](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile393.png>)

![image 394](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile394.png>)

![image 395](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile395.png>)

![image 396](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile396.png>)

![image 397](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile397.png>)

![image 398](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile398.png>)

![image 399](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile399.png>)

![image 400](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile400.png>)

![image 401](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile401.png>)

![image 402](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile402.png>)

![image 403](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile403.png>)

- 7 121.16 142 5/7 8 2228.146 0.3462 0.3993 1.9464


![image 404](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile404.png>)

![image 405](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile405.png>)

![image 406](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile406.png>)

![image 407](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile407.png>)

![image 408](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile408.png>)

![image 409](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile409.png>)

![image 410](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile410.png>)

![image 411](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile411.png>)

![image 412](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile412.png>)

![image 413](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile413.png>)

![image 414](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile414.png>)

![image 415](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile415.png>)

- 5.1. Properties of weighted spherical designs. We shall need the following equivalent deﬁnition of weighted τ-designs. It was used as primary deﬁnition of cubatures in [23].


We denote by Pτ,n the space of polynomials in n variables of degree at most τ and Hnℓ the subspace of homogeneous spherical harmonics of degree ℓ ≤ τ, where Z(n,ℓ) := dim(Hnℓ ) and {Yℓ,k}kZ=1(n,ℓ) is an orthonormal basis of Hnℓ . We recall that a real-valued function on Sn−1 is called a spherical harmonic of degree ℓ if it is the restriction of a homogeneous polynomial Y in n variables of degree ℓ that is harmonic, i.e. for which △Y ≡ 0.

Lemma 5.1. A weighted spherical code (C,W) ⊂ Sn−1, C = (x1,... ,xN), is a weighted spherical τ-design if and only if the following quadrature formula

p(y)dσn(y) =

Sn−1

N

wip(xi), (30)

i=1

holds for all polynomials in n variables of total degree at most τ. Here σn is the Lebesgue surface measure of Sn−1 normalized so that σn(Sn−1) = 1.

Proof. The proof is similar to the proof in the equi-weighted case. Since the restriction Pτ,n|Sn−1 is a direct sum of the orthogonal subspaces Hnℓ , ℓ = 0,1,... ,τ, it sufﬁces to prove the lemma for p ∈ Hnℓ , ℓ ≤ τ.

Since w1 + ··· + wN = 1, the quadrature (30) holds trivially for the constant polynomial; i.e. for ℓ = 0. Let us ﬁx 1 ≤ ℓ ≤ τ. Then the left-hand side of (30) vanishes as p is harmonic and homogeneous of degree at least 1 (the mean-value property holds). From the Addition formula [29, Theorem 2] (see also [5, Formula (5.1.14)]) we have

which implies that

Z(n,ℓ)

Yℓ,k(xi)Yℓ,k(xj) = Z(n,ℓ)Pℓ(n)(xi · xj),

k=1

Z(n,ℓ)

1 Z(n,ℓ)

Mℓ(C,W) =

![image 416](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile416.png>)

k=1

N

wiYℓ,k(xi)

i=1

2

.

Thus, if (C,W) is a weighted τ-design, then Mℓ(C,W) = 0 and the right-hand side of (30) holds true for all {Yℓ,k}kZ=1(n,ℓ) and hence for all p ∈ Hnℓ . On the other hand, if the quadrature (30) holds for all p ∈ Hnℓ , then it holds for all Yℓ,k, which implies Mℓ(C,W) = 0 and completes the proof.

Next, we utilize the identity

f(1) ·

N

wi2 +

i=1

wiwjf(xi · xj) = f0 +

i =j

τ

fℓMℓ(C,W) (31)

ℓ=1

(holding for deg(f) ≤ τ; used in the proof of Theorem 2.3) to see the following characterization of weighted spherical designs.

- Theorem 5.2. A weighted spherical code (C,W) on Sn−1 is a weighted spherical τ-design if and only if

i =j

wiwjf(xi · xj) = f0 − f(1) ·

N

i=1

wi2 (32)

holds for any real polynomial of degree at most τ. Proof. If (C,W) is a weighted spherical τ-design on Sn−1, then Mℓ(C,W) = 0 for 1 ≤ ℓ ≤ τ yields (32) directly from (31).

Conversely, assume that (32) holds for any polynomial f of degree at most τ. Then with the polynomial f(t) = τi=0 Pi(n)(t) in (31) and (32) we obtain that

τ

ℓ=1

Mℓ(C,W) = 0;

whence Mℓ(C,W) = 0 for 1 ≤ ℓ ≤ τ.

The condition (32) can be further specialized as we shall see in the next theorem, where we prove that the left-hand side of (32) decomposes into N equal parts (when x = xi ∈ C).

- Theorem 5.3. A weighted spherical code (C,W) on Sn−1 is a weighted spherical τ-design if and only if for any point x ∈ Sn−1 the equality


N

wjf(x · xj) = f0 (33)

j=1

holds for any real polynomial f of degree at most τ and every i = 1,2,... ,N.

Proof. If (C,W) is a weighted spherical τ-design on Sn−1, then Mℓ(C,W) = 0 for 1 ≤ ℓ ≤ τ. Let f(t) = τk=0 fkPk(n)(t) be the Gegenbauer expansion of f. Then for every i = 1,2,... ,N we have that p(x) := Nj=1 wjf(x · xj) ∈ Pτ,n and from Lemma 5.1 and the Funk-Hecke formula we derive that

N

1

f(t)dµn(t) = f0.

f(x · y)dσn(y) =

wjf(x · xj) =

Sn−1

−1

j=1

Suppose now that the identity (33) holds for all i = 1,2,... ,N. Applying it for xi ∈ C, then multiplying by wi and adding for all i, we utilize f(t) = Pℓ(n)(t) in (33) to derive that Mℓ(C,W) =

- 0 for 1 ≤ ℓ ≤ τ.

- Theorem 5.3 is the weighted analog of the property of designs in the equi-weighted case ex-

pressed by [19, Equation (1.10)]. The identity (33) from Theorem 5.3 could be used with x ∈ C to estimate the frequency and location of inner products of C via the polynomial f. Such approach was used in [6] for obtaining bounds on the extreme (smallest and largest) inner products that imply some nonexistence results for (equi-weighted) spherical designs of odd strengths and odd cardinalities.

Applications of Theorem 5.3 for obtaining bounds for polarization of weighted spherical designs will be considered in a future paper.

5.2. ULB on energy for weighted spherical τ-designs. Assume that (C,W) is a weighted spherical τ-design on Sn−1 such that NW ∈ (D(n,τ),D(n,τ + 1)]. Since all the moments Mi(C,W), 1 ≤ i ≤ τ, are equal to 0, we do not need the conditions fi ≥ 0 for i = 1,2,... ,τ. The good set of polynomials will be

Lh(n,τ) := f(t) =

τ

i=0

fiPi(n)(t) : f(t) ≤ h(t),t ∈ [−1,1) ,

For the same reason, we can relax the conditions of the derivatives of the potential function h to the requirement h(τ+1) ≥ 0 to be used only in the Hermite error formula.

With these observations, we restate Theorem 2.3 as ULB for weighted designs.

- Theorem 5.4. (ULB for weighted designs) Let (C,W) be a weighted spherical τ-design, τ =


- 2k − 1 + ε, ε ∈ {0,1}, and W be such that NW satisﬁes (12) with m = τ. If the potential function h satisﬁes h(τ+1) ≥ 0, then


k−1+ε

ρih(αi), (34)

Eh(C,W) ≥

i=0

where the parameters (αi,ρi)ik=0−1+ε are the same as in Theorem 2.3. This bound cannot be improved by any polynomial f ∈ Lh(n,τ).

Proof. With parameters and interpolation as in Theorem 2.3, we see that f ∈ Lh(n,τ) and

k−1+ε

f(1) NW

ρih(αi).

=

Eh(C,W) ≥ f0 −

![image 417](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile417.png>)

i=0

In the case of absolutely monotone potential h, the bounds (15) and (34) are both valid and coincide.

- 5.3. UUB for weighted spherical τ-designs. As was the case for the ULB for weighted designs, the condition gℓ ≤ 0 for the linear programming polynomials for UUB is no longer necessary for 1 ≤ ℓ ≤ τ since Mℓ(C,W) = 0 in (31) for these ℓ.


We ﬁrst reformulate Theorem 4.1. We consider the set of good polynomials as

 

 

deg(g)

Vh(n,s,τ) :=

giPi(n)(t) : g(t) ≥ h(t), t ∈ [−1,s], deg(g) ≤ τ

g(t) =

.





i=0

- Theorem 5.5. If g ∈ Vh(n,s,τ), then for every weighted spherical τ-design (C,W) on Sn−1 with cardinality (size) N and maximal inner product s = s(C) ∈ [−1,1),

Eh(C,W) ≤ Eg(C,W) = g0 − g(1)

N

i=1

wi2. Consequently,

Eh(C,W) ≤ inf

g∈Vh(n,s,τ)

g0 − g(1)

N

i=1

wi2 . (35)

Proof. Obvious from g ≥ h in [−1,s] and (31).

- Theorem 5.6. Let h be such that h(τ) ≥ 0 and (C,W) be a weighted spherical τ-design on Sn−1 with cardinality (size) N and maximal inner product s = s(C) ∈ [−1,1). Assume that Nq = Lq(n,s) satisﬁes (12) with q = τ = 2ℓ − 1 + ε and Nq instead of NW. Then


ℓ−1+ε

(NW − Nq)gT(1) NWNq

ρi(n,s)h(αi(n,s)), (36)

+

Eh(C,W) ≤

![image 418](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile418.png>)

i=0

where the set T of interpolation nodes and the polynomial gT are as in Theorem 4.2.

Proof. We naturally consider an interpolant g that stays above h in [−1,s] so we utilize the nodes from the multiset T from (27) but with q replaced by τ. This produces the polynomial g = gT, which can be also viewed as the polynomial from (25) with λ = 0 (i.e., without the correction via the Levenshtein polynomial fτ(n,s)). Since deg(g) = deg(gT) = τ − 1, the veriﬁcation of g ≥ h in [−1,s] by the Hermitte interpolation error formula

ℓ−2+ε

h(τ)(ξ) τ!

(t − αi)2, ξ ∈ (−1,1),

(t − α0)2−ε(t − s)

h(t) − g(t) =

![image 419](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile419.png>)

i=1

requires h(τ)(t) ≥ 0 only. Therefore, g ∈ Vh(n,s,τ) and Theorem 5.5 implies

N

wi2,

Eh(C,W) ≤ (gT)0 − gT(1)

i=1

which yields (36) by the quadrature rule (14) applied for the polynomial g with Nq instead of NW and the interpolation equalities g(αi(n,s)) = h(αi(n,s)).

Remark 5.7. The conditions of Theorem 5.6 impose the requirements D(n,m) < N < Nq ≤ D(n,m + 1) which restrict the applicability of the bound (36) to weighted spherical designs with relatively small cardinalities (see the examples below).

We illustrate the UUB (36) with continuations of our two examples.

- Example 5.8. Theorem 5.6 can be applied to Examples 2.5 and 4.6 with n = 3, τ = 9, N = 32, weights W as in (C32,W), and every potential with h(9) ≥ 0 (note that all three numbers NW < N < Nq belong to the ninth Delsarte-Goethals-Seidel interval (D(3,9),D(3,10)] = (30,36]). Using again the Coulomb potential h(t) = 1/ 2(1 − t) for comparison and computing (36), we obtain

![image 420](<2024-borodachov-energy-bounds-weighted-spherical_images/imageFile420.png>)

Eh(C,W) ≤ 0.805816

for such weighted spherical designs. This bound is very close to the actual energy of (C32,W) and the corresponding ULB (recall that Eh(C32,W) ≈ 0.8050318 and Eh(W) ≥ 0.804786). The interpolation nodes and the polynomial gT itself are the same as in Example 4.6.

- Example 5.9. We apply Theorem 5.6 for parameters of weighted 5-designs as in Examples 2.6


and 4.7 and for potentials h with h(5)(t) ≥ 0. The numbers N and Nq belong to the interval (D(n,5),D(n,6)] for 3 ≤ n ≤ 5. We compute the UUB for the Coulomb potential again to obtain:

Eh(C,W) ≤ 0.70893 for every weighted 5-design (with weights as (Cqp,W) ⊂ S2) with 14 points on S2,

Eh(C,W) ≤ 0.58111 for any (equi-weighted) 5-design with 24 points on S3, and

Eh(C,W) ≤ 0.500221

for every weighted 5-design (with weights as (Cqp,W) ⊂ S4) with 42 points on S4. These values are very close to the actual energy and the corresponding ULBs (cf. Table 4).

Acknowledgments. The research of the second author was supported, in part, by Bulgarian NSF grant KP-06-N72/6-2023. The research of the third author is supported, in part, by the Lilly Endowment. The research of the sixth author was supported, in part, by Contract BG-RRP-2.004-0008, Soﬁa University Marking Momentum for Innovation and Technological Transfer (SUMMIT), Work group 3.2.1. Numerical Analysis, Theory of Approximations and Their Applications (NATATA).

The authors thank an anonymous referee for comments that signiﬁcantly improved the exposition.

REFERENCES

- [1] Bannai, Ei, Bannai, Et., A survey on spherical designs and algebraic combinatorics on spheres, Europ. J. Combin. 30, 1392–1425 (2009).
- [2] Barg, A., Boyvalenkov, P., Stoyanova, M., Bounds for the sum of distances in spherical sets of small size, Discr. Math., 346, art. 113346 (2023).
- [3] Bilyk, D., Matzke, R. W., On the Fejes T´oth problem about the sum of angles between lines, Proc. Am. Math. Soc. 147, 51–59 (2019).
- [4] de Boor, C., Divided differences, Surveys in Approximation Theory 1, 46–69 (2005).
- [5] Borodachov, S. V., Hardin, D. P., Saff, E. B., Discrete Energy on Rectiﬁable Sets, Springer Monographs in Mathematics, Springer, 2019.
- [6] Boumova, S., Boyvalenkov, P., Danev, D., Necessary conditions for existence of some designs in polynomial metric spaces, Europ. J. Combin. 20, 213–225 (1999).
- [7] Boyvalenkov, P., Danev, D., Bumova, S., Upper bounds on the minimum distance of spherical codes, IEEE Trans. Inform. Theory 42, 1576–1581 (1996).
- [8] Boyvalenkov, P., Danev, D., Landgev, I., On maximal spherical codes II, J. Combin. Designs 7, 316–326 (1999).
- [9] Boyvalenkov, P., Dragnev, P., Hardin, D., Saff, E., Stoyanova, M., Universal lower bounds for potential energy of spherical codes, Constr. Approx. 44, 385–415 (2016).
- [10] Boyvalenkov, P., Dragnev, P., Hardin, D., Saff, E., Stoyanova, M., Energy bounds for codes in polynomial metric spaces, Anal. Math. Phys. 9, 781–808 (2019).
- [11] Boyvalenkov, P. Dragnev, D. Hardin, Saff, E., Stoyanova, M., Upper bounds for energies of spherical codes with given cardinality and separation, Des. Codes Cryptogr. 88, 1811–1826 (2020).
- [12] Boyvalenkov, P., Dragnev, P., Hardin, D., Saff, E., Stoyanova, M., Bounds for spherical codes: the Levenshtein framework lifted, Math. Comp. 90, 1323–1356 (2021).
- [13] Cohn, H., Conway, J., Elkies, N., Kumar, A., The D4 root system is not universally optimal, Experim. Math. 16, 313–320 (2007).
- [14] Cohn, H., Kumar, A., Universally optimal distribution of points on spheres, J. Amer. Math. Soc. 20, 99–148 (2007).
- [15] Cohn, H., Woo, J., Three-point bounds for energy minimization, J. Amer. Math. Soc. 25, 929–958 (2012).
- [16] Delsarte, P., An Algebraic Approach to the Association Schemes in Coding Theory, Philips Res. Rep. Suppl. 10, 1973.
- [17] Delsarte, P., Bounds for unrestricted codes by linear programming, Philips Res. Rep. 27, 272–289 (1972).
- [18] Delsarte, P., Goethals, J.-M., Seidel, J. J., Spherical codes and designs, Geom. Dedic. 6, 363–388 (1977).
- [19] Fazekas, G., Levenshtein, V. I., On upper bounds for code distance and covering radius of designs in polynomial metric spaces, J. Comb. Theory Ser. A, 70, 267–288 (1995).
- [20] Fejes T´oth, L., On the sum of distances determined by a pointset, Acta Math. Acad. Sci. Hung. 7, 397–401 (1956).
- [21] Gaspar, G., Linearization of the product of Jacobi polynomials - I, Canad. J. Math. 22, 171–175 (1970).
- [22] Godsil, C. D., Polynomial spaces, Discrete Mathematics, 73, 71–88 (1988/89).
- [23] Goethals, J.M., Seidel, J.J., Cubature Formulae, Polytopes, and Spherical Designs. In: Davis, C., Gr¨unbaum, B., Sherk, F.A. (eds) The Geometric Vein, Springer, New York, 1981.
- [24] Hughes, D., Waldron, S., Spherical (t, t)-designs with a small number of vectors, Lin. Alg. Appl. 608, 84–106,

(2021).

- [25] Kolushov, A. V., Yudin, V. A., Extremal dispositions of points on the sphere, Anal. Math. 23, 25–34 (1997).
- [26] Levenshtein, V. I., On bounds for packings in n-dimensional Euclidean space, Soviet Math. Dokl. 20, 417–421

(1979).

- [27] Levenshtein, V. I., Designs as maximum codes in polynomial metric spaces, Acta Applic. Math. 25, 1–82 (1992).
- [28] Levenshtein, V. I., Universal bounds for codes and designs, in Handbook of Coding Theory, V. S. Pless and W. C. Huffman, Eds., Elsevier, Amsterdam, Ch. 6, 499–648 (1998).
- [29] M¨uller, C., Spherical Harmonics, Lecture Notes in Mathematics 17 Springer-Verlag Berlin Heidelberg, 1966.
- [30] Neumaier, A., Seidel, J. J., Discrete measures for spherical designs, eutactic stars and lattices, Indagationes Mathematicae (Proceedings), 91, 321–334 (1988).


- [31] Salihov, G. N., On the theory of cubature formulas for multidimensional spheres. Dissertation, Acad. Sci. USSR, Novosibirsk 1978 (in Russian).
- [32] Schoenberg, I. J., Positive deﬁnite functions on spheres, Duke Math. J. 9, 96–107 (1942).
- [33] Sidel’nikov, V. M., On extremal polynomials used to estimate the size of codes, Probl. Inform. Transm. 16, 174–186

(1980).

- [34] Sobolev, S. L., Cubature formulas on the sphere invariant under ﬁnite groups of rotations, Dokl. Akad. Nauk SSSR 146, 310–313 (1962). (in Russian); English translation Soviet Math. Dokl. 3, 1307–1310 (1962).
- [35] Sobolev, S. L., Introduction to the Theory of Cubature Formulas (Russian). Nauka 1974.
- [36] Stroud, A. H., Approximate Calculation of Multiple Integrals. Prentice-Hall 1971.
- [37] Waldron S., An Introduction to Finite Tight Frames, New York, Applied and Numerical Harmonic Analysis, Birkha¨user/Springer, 2018.
- [38] Yudin, V. A., Minimal potential energy of a point system of charges, Discret. Mat. 4, 115-121 (1982), in Russian; English translation: Discr. Math. Appl. 3, 75–81 (1983).


DEPARTMENT OF MATHEMATICS, TOWSON UNIVERSITY, 7800 YORK RD, TOWSON, MD, 21252, USA Email address: sborodachov@towson.edu

INSTITUTE OF MATHEMATICS AND INFORMATICS, BULGARIAN ACADEMY OF SCIENCES, 8 G BONCHEV STR.,

1113 SOFIA, BULGARIA Email address: peter@math.bas.bg DEPARTMENT OF MATHEMATICAL SCIENCES, PURDUE UNIVERSITY, FORT WAYNE, IN 46805, USA Email address: dragnevp@pfw.edu CENTER FOR CONSTRUCTIVE APPROXIMATION, DEPARTMENT OF MATHEMATICS, VANDERBILT UNIVERSITY,

NASHVILLE, TN 37240, USA Email address: doug.hardin@vanderbilt.edu CENTER FOR CONSTRUCTIVE APPROXIMATION, DEPARTMENT OF MATHEMATICS, VANDERBILT UNIVERSITY,

NASHVILLE, TN 37240, USA Email address: edward.b.saff@vanderbilt.edu FACULTY OF MATHEMATICS AND INFORMATICS, SOFIA UNIVERSITY “ST. KLIMENT OHRIDSKI”, 5 JAMES

BOURCHIER BLVD., 1164 SOFIA, BULGARIA Email address: stoyanova@fmi.uni-sofia.bg

