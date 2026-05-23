# arXiv:1503.07228v1[math.MG]24Mar2015

## UNIVERSAL LOWER BOUNDS FOR POTENTIAL ENERGY OF SPHERICAL CODES

P. G. BOYVALENKOV †, P. D. DRAGNEV ††, D. P. HARDIN∗, E. B. SAFF∗, AND M. M. STOYANOVA∗∗

Abstract. We derive and investigate lower bounds for the potential energy of ﬁnite spherical point sets (spherical codes). Our bounds are optimal in the following sense – they cannot be improved by employing polynomials of the same or lower degrees in the Delsarte-Yudin method. However, improvements are sometimes possible and we provide a necessary and suﬃcient condition for the existence of such better bounds. All our bounds can be obtained in a uniﬁed manner that does not depend on the potential function, provided the potential is given by an absolutely monotone function of the inner product between pairs of points, and this is the reason for us to call them universal. We also establish a criterion for a given code of dimension n and cardinality N not to be LP-universally optimal, e.g. we show that two codes conjectured by Ballinger et al to be universally optimal are not LP-universally optimal.

1. Introduction

Minimal energy conﬁgurations, maximal codes, and spherical designs have wide ranging applications in various ﬁelds of science, such as crystallography, nanotechnology, material science, information theory, wireless communications, etc. In this article we shall derive lower bounds on the potential energy of such conﬁgurations via a uniﬁed method working for a large class of potential interaction functions. A fundamental connection between our lower bounds and the classical Delsarte-Goethals-Seidel bounds on spherical designs and Levenshtein’s bounds on maximal codes is presented. For a ﬁxed dimension and code cardinality the Delsarte-Goethals-Seidel bounds serve to localize the analysis

Date: July 6, 2021. 2010 Mathematics Subject Classiﬁcation. 74G65, 94B65 (52A40, 05B30). Key words and phrases. minimal energy problems, spherical potentials, spherical codes and designs,

Levenshtein bounds, Delsarte-Goethals-Seidel bounds, linear programming.

† The research of this author was supported, in part, by a Bulgarian NSF contract I01/0003. †† The research of this author was supported, in part, by a Simons Foundation grant no. 282207. ∗ The research of these authors was supported, in part, by the U. S. National Science Foundation under grants DMS-1109266 and DMS-1412428. ∗∗ The research of this author was supported, in part, by the Science Foundation of Soﬁa University under contract 015/2014.

The authors express their gratitude to Erwin Schro¨dinger International Institute for providing conducive research atmosphere during their stay when part of this manuscript was written.

1

and then, as illustrated in Figure 2, the zeros of the Levenshtein optimal polynomials for maximal codes determine the optimal polynomials for a large class of potentials.

Following Levenshtein’s terminology (see [27]) we call the lower bounds that we obtain universal. This choice of terms is also consistent with its use by Cohn and Kumar in their study [14] of universally optimal energy conﬁgurations, since our bounds likewise work for all absolutely monotone potential functions of the inner product. Furthermore, our lower bounds are attained for all sharp conﬁgurations as deﬁned in [14].

Let Sn−1 denote the unit sphere in Rn. We refer to a ﬁnite set C ⊂ Sn−1 as a spherical code and, for a given (extended real-valued) function h(t) : [−1,1] → [0,+∞], we deﬁne the h-energy of a spherical code C by

E(C;h) :=

h( x,y ),

x,y∈C,x =y

where x,y denotes the inner product of x and y. Note that for x,y ∈ Sn−1 we have |x − y|2 = 2 − 2 x,y .

A commonly arising problem is to minimize the potential energy provided the cardinality |C| of C is ﬁxed; that is, to determine

E(n,N;h) := inf{E(C;h) : |C| = N, C ⊂ Sn−1} the minimum possible h-energy of a spherical code of cardinality N (see [20, 31]). Although the theorems in Section 2 hold for general potentials h we will be especially concerned with functions h(t) that are absolutely monotone (absolutely strictly monotone), that is h(i)(t) ≥ 0, i = 0,1,... (h(i)(t) > 0, i = 0,1,...). Some examples of absolutely monotone potentials include the Riesz α-potential h(t) = [2(1 − t)]−α/2, α > 0, and in particular the Newton potential (when α = n − 2); the Gauss potential h(t) = e2t−2; the Korevaar potential h(t) = (1 + r2 − 2rt)−(n−2)/2, 0 < r < 1. Although the logarithmic potential h(t) = −(1/2)ln(1 − t) is not positive on [−1,0], all its derivatives are positive and the results in this article apply to this potential as well. The situation is similar for the Fejes-T´th potential h(t) = −[2(1 − t)]α/2, 0 < α < 2, which includes the important particular case in discrete geometry of α = 1, namely of ﬁnding conﬁgurations that maximize the sum of all mutual distances.

A general technique (referred to here as the Delsarte-Yudin method) for obtaining lower bounds for the h-energy of arbitrary spherical codes was developed by Yudin [35] using Delsarte’s linear programming method [17, 18, 21] and was further applied by Kolushov and Yudin [22], Andreev [1], and Cohn and Kumar [14]. These bounds depend on the choice of polynomials satisfying certain constraints. Here we provide explicit solutions to Delsarte’s linear program based upon Levenshtein’s work on maximal codes [26] and [27], which allows us to establish universal lower bounds on potential energy for a large class of potential functions h.

In Section 2 we describe in a uniﬁed manner results from Delsarte, Goethals and Seidel [18] and Levenshtein [25, 26, 27] that are instrumental in deﬁning our bounds. Theorems

- 2.3 and 2.6 explain the importance of special type quadrature rules in determining lower


bounds on energy and investigation of their optimality. Theorem 3.1 is one of the main results in this paper. It gives lower bounds which are optimal in the following sense – they cannot be improved by polynomials of the same or lower degree that satisfy the standard linear programming constraints speciﬁed in Theorem 2.2. On the other hand, the bounds of Theorem 3.1 can be further improved in some cases and Theorem 4.1 gives necessary and suﬃcient conditions for existence of such improvements via the so-called test functions, which were ﬁrst introduced and investigated for analysis of the Levenshtein bounds for maximal codes in 1996 by Boyvalenkov, Danev and Bumova [11]. We derive a quantitative version of [11, Theorem 5.2] in Theorem 4.10, which provides a criterion for disproving that certain codes are LP-universally optimal. As an application we prove that the two codes conjectured to be universally optimal in [2], are not LP-universally optimal, namely their universal optimality may not be established by an ad-hoc approach similar to the 600-cell approach given in [14, 15].

2. Linear programming framework and 1/N-quadrature rules

- 2.1. Gegenbauer polynomials and the Delsarte-Yudin linear programming framework. For ﬁxed dimension n, the Gegenbauer polynomials [33] are deﬁned by P0(n) = 1, P1(n) = t and the three-term recurrence relation


(i + n − 2)Pi(+1n)(t) = (2i + n − 2)tPi(n)(t) − iPi(−n1)(t) for i ≥ 1.

We note that {Pi(n)(t)} are orthogonal in [−1,1] with respect to the weight (1−t2)(n−3)/2 and that Pi(n)(1) = 1. In standard Jacobi polynomial notation (see [33, Chapter 4]), we have that

Pi((n−3)/2,(n−3)/2)(t) Pi((n−3)/2,(n−3)/2)(1)

- (1) Pi(n)(t) =


.

Denote the space of real polynomials of degree at most k by Pk. Any f ∈ Pk can

be uniquely expanded in terms of the Gegenbauer polynomials as f(t) = ki=0 fiPi(n)(t). The coeﬃcients fi given by

1 −1 f(t)Pi(n)(t)(1 − t2)(n−3)/2 dt

fi =

, i = 0,1,...,k,

2

1 −1 Pi(n)(t)

(1 − t2)(n−3)/2 dt

play an important role in linear programming theorems.

Let {Yk (x) : = 1,2,...,rk} be an orthonormal basis of the space Harm(k) of homogeneous harmonic polynomials in n variables of degree k restricted to Sn−1, where

n + k − 1 n − 1 −

n + k − 3 n − 1

n + k − 3 n − 2

2k + n − 2 k

=

rk := dim Harm(k) =

and orthonormality is with respect to integration over the sphere utilizing σn, the normalized (n − 1)-dimensional Hausdorﬀ measure restricted to Sn−1. The functions {Yk ,

= 1,2,...,rk}, are known as spherical harmonics of degree k. The Gegenbauer polynomials and spherical harmonics are related through the well-known Addition Formula (see [23]):

- (2)

1 rk

rk

=1

Yk (x)Yk (y) = Pk(n)( x,y ), x,y ∈ Sn−1;

that is, the Gegenbauer polynomial Pk(n)(t) is, up to a normalization, the kernel for the orthogonal projection onto Harm(k).

If f is a function integrable on [−1,1] with respect to the weight function (1−t2)(n−3)/2 and y is any ﬁxed point on Sn−1, then the following relation (a partial case of the FunkHecke formula, see [29, Theorem 6]) holds:

Sn−1

f( x,y )dσn(x) = γn

1

−1

f(t)(1 − t2)(n−3)/2dt,

where

γn :=

Γ n2 √πΓ n−21

.

If C = {x1,...,xN} is a spherical code of N points on Sn−1, then it follows from (2) that:

- (3)

N

i,j=1

Pk(n)( xi,xj ) =

1 rk

rk

=1

N

i,j=1

Yk (xi)Yk (xj) =

1 rk

rk

=1

N

i=1

Yk (xi)

2

≥ 0.

We deﬁne the k-th moment of C by

Mk(C) :=

N

i,j=1

Pk(n)( xi,xj ).

From (3), we have Mk(C) = 0 if and only if Ni=1 Y (xi) = 0 for all spherical harmonics Y ∈ Harm(k). If Mk(C) = 0 for 1 ≤ k ≤ τ, then C is called a spherical τ-design. Equivalently, C is a spherical τ-design if and only if

Sn−1

p(x)dσn(x) =

1 |C| x∈C

p(x)

(σn is the normalized (n − 1)-dimensional Hausdorﬀ measure) holds for all polynomials p(x) = p(x1,x2,...,xn) of degree at most τ. The set

- (4) I(C) := {k ∈ N: Mk(C) = 0},


is called the index set of C. Hence, C is a spherical τ-design if and only if {1,2,...,τ} ⊂ I(C).

Suppose f : [−1,1] → R is of the form

- (5) f(t) =

∞

k=0

fkPk(n)(t), fk ≥ 0 for all k ≥ 1,

where we remark that f(1) = ∞k=0 fk < ∞. Since |Pk(n)(t)| ≤ 1, it follows that the right-hand side of (5) converges uniformly on [−1,1]. We then obtain the following

relations which form the basis for many packing and energy bounds for spherical codes C = {xi}Ni=1 of cardinality N (see [6, 14, 21, 35]):

E(C;f) =

N

i,j=1

f( xi,xj ) − f(1)N

=

∞

k=0

fk

N

i,j=1

Pk(n)( xi,xj ) − f(1)N

=

∞

k=0

fkMk(C) − f(1)N

≥ f0N2 − f(1)N.

- (6)

Since Mk(C) = 0 for k = 1,...,τ when C is a τ-design, the following result immediately follows from (6).

- Theorem 2.1 (Delsarte, Goethals, Seidel [18]). Suppose C is a spherical τ-design on Sn−1 and f(t) is a polynomial of degree at most τ such that f(t) ≥ 0 on [−1,1] and f0 = γn − 11 f(t)(1 − t2)(n−3)/2 dt > 0. Then


- (7) |C| ≥

f(1) f0

.

Maximizing the right hand side of (7) over polynomials satisfying the above hypotheses, Delsarte, Goethals, and Seidel [18] obtain a lower bound on

B(n,τ) := min{|C| : C ⊂ Sn−1 is a spherical τ-design} Speciﬁcally, they show

- (8) B(n,τ) ≥ D(n,τ) :=


 

n + k − 2 n − 1

, if τ = 2k − 1,

2

n + k − 1 n − 1

n + k − 2 n − 1



, if τ = 2k. We refer to D(n,τ) as the Delsarte-Goethals-Seidel bound for spherical τ-designs. Another application of (6) is Yudin’s lower bound on energy.

+

- Theorem 2.2 (Yudin [35]). Suppose f : [−1,1] → R is of the form (5) with fk ≥ 0 for all k ≥ 1. Then, for N ≥ 2


E(n,N;f) ≥ f0N2 − f(1)N. Consequently, if h : [−1,1] → [0,∞] satisﬁes h(t) ≥ f(t), t ∈ [−1,1], we have

- (9) E(n,N;h) ≥ f0N2 − f(1)N.

Furthermore, C is an optimal (energy minimizing) code for h and equality holds in (9) if and only if both of the following conditions hold:

- (a) f(t) = h(t) for all t ∈ { x,y : x = y, x,y ∈ C};
- (b) for all k ≥ 1, either fk = 0 or Mk(C) = 0.


For a given h : [−1,1] → [0,∞], we denote by An,h the set of functions f ≤ h satisfying the conditions (5). Recall that for such f, the coeﬃcient sequence (f0,f1,...) ∈ 1. The problem of maximizing the lower bound f0N2 − f(1)N arising in Theorem 2.2 can then be expressed in terms of an inﬁnite linear program:

maximize F(f0,f1,...) := N f0(N − 1) −

∞

k=1

fk ,

subject to

∞

k=0

fkPk(n)(t) ≤ h(t),t ∈ [−1,1] and fk ≥ 0, for all k ≥ 1.

- (10)

In the following we shall consider the above linear program restricted to a subspace Λ (usually ﬁnite-dimensional) of the linear space C([−1,1]) of real-valued functions continuous on [−1,1]. For such a Λ, we deﬁne

- (11) W(n,N,Λ;h) := sup f∈Λ∩An,h

N2(f0 − f(1)/N).

In general, it can be a diﬃcult problem to ﬁnd the value of W(n,N,Λ;h). We consider suﬃcient conditions that allow us to solve for W(n,N,Λ;h). In particular, we explicitly ﬁnd the solutions of the truncated linear program (10) and thus ﬁnd (11) when Λ = Pk, for all k ≤ τ(n,N), for some τ(n,N) (as deﬁned in equation (18) below). In the particular case when m = τ(n,N) we derive the universal lower bound (ULB) for potential energy of spherical codes.

2.2. 1/N-Quadrature rules and lower bounds for energy. We refer to a ﬁnite sequence of ordered pairs {(αi,ρi)}ki=1 as a 1/N-quadrature rule if −1 ≤ α1 < α2 < ··· < αk < 1, and ρi > 0 for i = 1,2,...,k, and say that {(αi,ρi)}ki=1 is exact for a subspace Λ ⊂ C([−1,1]) if

- (12) f0 := γn


k

1

f(1) N

f(t)(1 − t2)(n−3)/2dt =

+

ρif(αi),

−1

i=1

for all f ∈ Λ.

- Theorem 2.3. Let {(αi,ρi)}ki=1 be a 1/N-quadrature rule that is exact for a subspace Λ ⊂ C([−1,1]).


- (a) If f ∈ Λ ∩ An,h, then

E(n,N;h) ≥ N2

k

i=1

ρif(αi).

- (b) We have


- (13) W(n,N,Λ;h) ≤ N2

k

i=1

ρih(αi).

If there is some f ∈ Λ∩An,h such that f(αi) = h(αi) for i = 1,...,k, then equality holds in (13) which yields the universal lower bound

- (14) E(n,N;h) ≥ N2


k

i=1

ρih(αi).

Proof. If f ∈ Λ, then (12) holds and so, from Theorem 2.2, we obtain

k

E(n,N;h) ≥ N2(f0 − f(1)/N) = N2

ρif(αi),

i=1

showing that (a) holds. For (b), using (12), we obtain W(n,N,Λ;h) = sup

N2(f0 − f(1)/N)

f∈Λ∩An,h

k

k

N2

ρif(αi) ≤ N2

= sup

ρih(αi).

f∈Λ∩An,h

i=1

i=1

Clearly equality holds if there is some f ∈ Λ ∩ An,h such that f(αi) = h(αi) for i =

- 1,...,k.


- As we next describe, a spherical code C = {x1,...,xN} ⊂ Sn−1 provides a quadrature


rule that is exact on the subspace

 

 

flPl(n)(t):

|fl| < ∞

ΛC :=

f(t) = f0 +

,





l∈I(C)

l∈I(C)

with I(C) as deﬁned in (4). Let { xi,xj : xi = xj ∈ C} =: {−1 ≤ α1 < α2 < ··· < αk < 1},

and let {ql} denote the inner product distribution; i.e., ql := {(i,j): xi,xj = αl} N2

, l = 1,...,k.

If f ∈ ΛC, then fl = 0 for all l  ∈ I(C) (unless l = 0) and equality holds in (6). Hence, for such f, we obtain

- k
- l=1


1 N2

f(1) N

- (15) f0 =


E(C;f) + Nf(1) =

+

qlf(αl),

that is, {(αl,ql)}kl=1 is a 1/N-quadrature rule exact for ΛC.

- Example 2.4. As an example we consider the 600-cell C consisting of 120 points in S3. Each x ∈ C has 12 nearest neighbors forming an icosahedron (the Voronoi cells are dodecahedra) and there are 8 inner products −1 = α1 < α2 < ··· < α8 < 1 between distinct points in C. If f(t) ≤ h(t) on [−1,1] and f(αk) = h(αk) and for all αk > −1, then we must also have f (αk) = h (αk), resulting in 2 · 7 + 1 = 15 interpolation conditions. If C were a 14-design, then this would suggest we search for f ∈ A4,h ∩Λ with Λ = P14. However, C is only an 11-design (i.e., M12(C) = 0), although M13(C) = ··· = M19(C) = 0, so C is almost a 19-design. This suggests we choose

Λ to be a 15-dimensional subspace of P19 ∩ {P12(4)}⊥. In fact, Cohn and Kumar [14, Section 7] show that for any absolutely monotone potential h on [−1,1], there is a unique

f ∈ An,h ∩ Λ for Λ := {f ∈ P17: f11 = f12 = f13 = 0} that proves the optimality of C.

- Example 2.5. Another example is provided by the so-called sharp conﬁgurations [14], namely conﬁgurations with k distinct inner products that are spherical designs of strength


2k−1. In this case Λ = P2k−1 and the existence of the 1/N-quadrature is provided by the conﬁguration quadrature (15) and the design property. We shall return to this example in the Remark 3.3 following Theorem 3.1.

The two examples above cover all currently known universally optimal conﬁgurations. The next theorem provides suﬃcient conditions for optimality of (14) even in a larger subspace.

Theorem 2.6. Let {(αi,ρi)}ki=1 be a 1/N-quadrature rule that is exact for a subspace Λ ⊂ C([−1,1]) and such that equality holds in (13). Suppose Λ = Λ span {Pj(n): j ∈ I} for some index set I ⊂ N. If Q(jn) := N1 + ki=1 ρiPj(n)(αi) ≥ 0 for j ∈ I, then

k

W(n,N,Λ ;h) = W(n,N,Λ;h) = N2

ρih(αi).

i=1

Proof. Suppose f(t) ∈ An,h ∩ Λ . Then we may write the decomposition of f as f(t) = g(t) +

fjPj(n)(t),

j∈I

for some g ∈ Λ and fj ≥ 0, for j ∈ I. Note that f0 = g0, since 0  ∈ I. Furthermore, since the quadrature rule {(αi,ρi)}ki=1 is exact for g ∈ Λ, we have

 g(1) +

 N−1

k

g(1) N

f0 − f(1)N−1 = g0 − f(1)N−1 =

ρig(αi) −

+

fj

j∈I

i=1

 f(αi) −

  −

 

 N−1

k

fjPj(n)(αi)

=

ρi

fj

j∈I

j∈I

i=1

k

k

1 N

ρiPj(n)(αi)

ρif(αi) −

=

+

fj

j∈I

i=1

i=1

k

k

1 N2W(n,N,Λ;h),

fjQ(jn) ≤

ρif(αi) −

=

ρih(αi) =

j∈I

i=1

i=1

where, for the last inequality, we used f(t) ∈ An,h and Q(jn) ≥ 0.

- 2.3. Levenshtein bounds for spherical codes. Let A(n,s) := max{|C|: C ⊂ Sn−1, x,y ≤ s, x = y ∈ C}


denote the maximal possible cardinality of a spherical code on Sn−1 of prescribed maximal inner product s.

For a,b ∈ {0,1} and i ≥ 1, let ta,bi denote the greatest zero of the adjacent Jacobi polynomial P(a+

n−3

2 ,b+n−2 3)

i (t) and also deﬁne t10,1 = −1. For τ ∈ N, let Iτ denote the interval

 

t1k,−11,tk1,0 , if τ = 2k − 1,

Iτ :=



t1k,0,t1k,1 , if τ = 2k,

The collection of intervals is well deﬁned from the interlacing properties tk1,−11 < tk1,0 < t1k,1, see [27, Lemmas 5.29, 5.30]. Note also that it partitions I = [−1,1) into countably many subintervals with non-overlapping interiors.

For every s ∈ Iτ, using linear programming bounds for special polynomials fτ(n,s)(t) of degree τ (see [27, Equations (5.81) and (5.82)]), Levenshtein proved that (see [27, Equation (6.12)])

 

(n) k−1(s)−Pk(n)(s)

L2k−1(n,s) = k+k−n−13 2kn+−n1−3 − P

, if s ∈ I2k−1

(1−s)Pk(n)(s)

- (16) A(n,s) ≤


(n) k (s)−Pk(n+1) (s))

L2k(n,s) = k+nk−2 2kn+−n1−1 − (1+s)(P



, if s ∈ I2k.

(1−s)(Pk(n)(s)+Pk(n+1) (s))

For every ﬁxed dimension n each bound Lτ(n,s) is smooth with respect to s. The function

 

L2k−1(n,s), if s ∈ I2k−1, L2k(n,s), if s ∈ I2k

L(n,s) =



is continuous in s. The connection between the Delsarte-Goethals-Seidel bound (8) and the Levenshtein bounds (16) is given by the equalities

L2k−2(n,tk1,−11) = L2k−1(n,t1k,−11) = D(n,2k − 1), L2k−1(n,t1k,0) = L2k(n,t1k,0) = D(n,2k).

- (17)

and the ends of the intervals Iτ.

![image 1](<2015-boyvalenkov-universal-lower-bounds-potential_images/imageFile1.png>)

Figure 1. The Levenshtein function L(4,s) on Ik, 1 ≤ k ≤ 6.

2.4. Levenshtein’s 1/N-quadrature rule. Levenshtein’s method for obtaining his bounds on cardinality of maximal spherical codes utilizes orthogonal polynomials theory and Gauss-type quadrature rules that we now brieﬂy review. The location of the cardinality N relative to the Delsarte-Goethals-Seidel numbers D(n,τ) is an important step in determining our universal lower bounds. From the properties of the bounds D(n,τ) and Lτ(n,s) (see (8), (17)) we derive that for every ﬁxed dimension n and cardinality N there is unique

- (18) τ := τ(n,N) such that N ∈ (D(n,τ),D(n,τ + 1)]. For the so found τ deﬁne k := τ+12 and let αk = s be the unique solution of

- (19) N = Lτ(n,s), s ∈ Iτ.


- Then as described by Levenshtein in [27, Section 5] (see also [26, 9]) there exist uniquely determined quadrature nodes and nonnegative weights
- (20) − 1 ≤ α1 < ··· < αk < 1, ρ1,...,ρk ∈ R+, i = 1,...,k such that the Radau/Lobato 1/N-quadrature (see [16], [5]) holds
- (21) f0 =

f(1) N

+

k

i=1

ρif(αi), for all f ∈ Pτ.

When τ = 2k − 2 is even, then α1 = −1 and (21) is Lobato quadrature. The numbers αi, i = 2,...,k, are the roots of the equation

- (22) Pk−1(t)Pk−2(αk) − Pk−1(αk)Pk−2(t) = 0,

where Pi(t) = P(

n−1

2 ,n−2 1)

i (t). When τ = 2k − 1 is odd, then α1 > −1 and (21) becomes Radau quadrature. The numbers αi, i = 1...,k, are the roots of the equation

- (23) Pk(t)Pk−1(αk) − Pk(αk)Pk−1(t) = 0,


2 ,n−2 3)

n−1

where Pi(t) = P(

i (t). In fact, {αi} are roots of the Levenshtein’s polynomials fτ(n,αk)(t) (see [27, Equations (5.81) and (5.82)]).

The dynamical behavior of the quadrature nodes {αi} is the following. When N ∈ (D(n,2k−2),D(n,2k−1)) then α1 = −1 and the quadrature (21) is Lobato. The solution αk of (19) belongs to the interval (tk1,−01,t1k,−11) and all {αi}ki=2 strictly increase with N. We have that

1 = |α1| > |α2| > |αk| > |α3| > |αk−1| > ··· .

- At the transition point N = D(n,2k − 1), α1 = −1 and αk = t1k,−11. The equation (22) becomes Pk(−n+21 (t) = 0, which implies that


1 = |α1| > |α2| = |αk| > |α3| = |αk−1| > ··· .

As N increases from D(n,2k−1) to D(n,2k), αk strictly increases from t1k,−11 to t1k,0, as do the rest of the nodes {αi}ki=1−1. In particular, α1 > −1 and (21) deﬁnes Radau quadrature and

1 > |α1| > |αk| > |α2| = |αk−1| > ··· .

More details on the nodes {αi} can be found in [12, Appendix], [10, Corollary 3.9], and [7, Section 2.6].

3. Universal lower bounds

- 3.1. Optimal polynomials for lower bounds. The optimal polynomials of degrees one and two to be applied in Theorem 2.2 can be found by direct computations and manipulations with the corresponding derivatives. These polynomials suggest a general form of polynomials which are optimal in the following sense – they give lower bounds


which cannot be improved by utilizing other polynomials of the same or lower degree in

- Theorem 2.2.

Our choice of polynomials for Theorem 2.2 can be viewed as extension of the ideas of Levenshtein [26, 27] who uses suitable quadrature formulas (Subsection 2.4) to explain the bounds (16) and their optimality in the same sense as above. This similarity should not seem unusual – the maximal code problem is inﬁnite version of the Riesz energy problem. In fact, Cohn and Kumar [14] use similar idea to deal with the universally optimal conﬁgurations. Thus, our paper can be viewed as natural extension of the works [26, 27, 14]. Recall that given a ﬁxed dimension n and a code cardinality N we can associate τ = τ(n,N) and s ∈ Iτ such that Lτ(n,s) = N (see (18) and (19)). Depending on the parity of τ we distinguish two cases:

- Case (i): τ = 2k −2 and αk = s ∈ tk1,−01,tk1,−11 . Then f(t) := fτh(n,N)(t) is the Hermite

interpolation polynomial of degree 2k − 2 deﬁned by (recall that α1 = −1 in this case)

(24) f(−1) = h(−1), f(αi) = h(αi), f (αi) = h (αi), i = 2,...,k.

- Case (ii): τ = 2k − 1 and αk = s ∈ t1k,−11,tk1,0 . Then f(t) := fτh(n,N)(t) is the Hermite


interpolation polynomial of degree 2k − 1 deﬁned by

- (25) f(αi) = h(αi), f (αi) = h (αi), i = 1,2,...,k; In the notation of Cohn-Kumar’s paper [14, p. 110], our polynomials are
- (26) fτh(n,N)(t) = H(h;(t − s)fτ(n,s)(t)).


3.2. Main theorem. The equations (24) and (25) deﬁne a Hermite’s interpolation problem for f(t) to intersect and touch the graph of the potential function h(t) (see [22, Theorems 2 and 3], [14, Section 5]). This implies as in [14, Sections 3 and 5] that f ∈ An,h and we could use f(t) for bounding E(n,N;h) from below. Observe that the nodes (20) are independent of the potential function h, hence we call our bound on E(n,N;h) a universal lower bound (ULB).

Next, we state our main theorem. We note that here is the ﬁrst time when we impose the condition that the potential function h(t) is absolutely monotone and that none of the preceding results have required this property.

- Theorem 3.1. Let n, N be ﬁxed and h(t) be an absolute monotone potential. Suppose


that τ = τ(n,N) is as in (18), and choose k = τ+12 . Associate the quadrature nodes and weights αi and ρi, i = 1,...,k, as in (21). Then

- (27) E(n,N;h) ≥ Rτ(n,N;h) := N2

k

i=1

ρih(αi).

Moreover, the polynomials deﬁned by (i), respectively by (ii), provide the unique optimal solution of the linear program (11) for the subspace Λ = Pτ and consequently,

- (28) W(n,N,Pτ;h) = Rτ(n,N;h).


- Remark 3.2. The optimality of the Hermite interpolants (26) is analogous to the op-

timality of the Levenshtein polynomials fτ(n,s)(t) (proved ﬁrst by Sidelnikov [32]), and emphasizes the universality of our bound.

- Remark 3.3. As noted in Example 2.5, the sharp conﬁgurations (see [14]) deﬁne 1/N-


quadrature. Moreover, the k inner products coincide with {αi}. Consequently, the bounds (27) are attained by all sharp conﬁgurations.

Proof of Theorem 3.1. We ﬁrst consider the odd case (ii), that is τ = 2k − 1. The conditions in (ii) deﬁne Hermite interpolation at the points αi, i = 1,2,...,k, and give a unique polynomial f of degree 2k − 1 with positive leading coeﬃcient. The absolute monotonicity of h(t) implies that f(t) ≤ h(t).

Next we derive that f satisﬁes the condition (5) as well. From (23) we have that the quadrature nodes {α1,...,αk} are zeros of the polynomial Pk(t) + cPk−1(t), where {Pi} are the Jacobi orthogonal polynomials {P(

n−1

2 ,n−2 3)

i }. From the interlacing properties of the orthogonal polynomials we obtain that the constant c = −Pk(s)/Pk−1(s) is non-negative. Indeed, the largest roots of the Jacobi polynomials tk1,−01 of Pk−1 satisfy t1k,−01 < t1k,−11 (see [26]). Since the last but largest root of Pk is smaller than tk1,−01 (by the interlacing property), we obtain that the ratio Pk(t)/Pk−1(t) doesn’t change sign in [t1k,−11,t1k,0). Moreover, from [7, Lemma 3.1.3 (a)] (see also [8, Lemma 1.5.8])

Pk(t1k,−11) Pk−1(t1k,−11)

n + 2k − 3 n + 2k − 1

−

> 0,

=

hence c ≥ 0. Utilizing the approach of [14, Sections 3 and 5] we conclude that the Hermite interpolant f has non-negative Gegenbauer expansion. Therefore, f ∈ An,h.

We now use (21) to derive the universal bound of f. We have

k

f(1) N

ρif(αi) ⇐⇒ N(f0N − f(1)) = N2

f0 =

+

i=1

k

k

ρif(αi) = N2

ρih(αi),

i=1

i=1

which means that E(n,N;h) ≥ N2 ki=1 ρih(αi) = R2k−1(n,N;h).

Furthermore, for any polynomial u = 2i=0k−1 uiPi(n)(t) ∈ An,h of degree at most 2k −1 we have

- (29) N(f0N − f(1)) = N2


k

ρih(αi) ≥ N2

i=1

k

ρiu(αi) = N(u0N − u(1)),

i=1

i.e. N(u0N − u(1)) ≤ R2k−1(n,N;h) and u(t) does not improve (27).

Should equality hold in (29) for some u ∈ An,h ∩P2k−1, we observe that u(αi) = h(αi) for i = 1,2,...,k. Additionally, the condition u(t) ≤ h(t) implies that u (αi) = h (αi) for all αi ∈ (−1,1). Hence, u satisﬁes the Hermite interpolation data (25), and by the

uniqueness of the Hermite interpolant, u ≡ f. Therefore, f is the unique optimal solution to the linear programming problem (10) in the class An,h ∩ P2k−1 and (28) holds.

In the even case (i) we proceed analogously, where we only modify the proof of the non-negativity of the Gegenbauer expansion. In this case we utilize [15, Lemma 10].

![image 2](<2015-boyvalenkov-universal-lower-bounds-potential_images/imageFile2.png>)

Figure 2. The optimal polynomials (Hermite interpolants), that provide the ULB for Gauss, Korevaar, and Newton potentials (in ascending order), along with the corresponding Levenshtein polynomial for n = 4, N = 24

- 3.3. Discussion and examples. The bounds (27) are easy for computation and investigation. Moreover, the approach by which they were derived doesn’t depend on the potential function and in this sense they are universal. This universality is illustrated in Figure 2, where we consider n = 4, N = 24 and plot the Gauss, Korevaar, and Newton potential functions, together with the corresponding optimal Hermite interpolants of degree τ = 5, that solve the linear program (10) in the class P5. We also overlay the


Levenshtein polynomial f5(4,s)(t), whose zeros are the solutions of (23), where s satisﬁes L5(4,s) = 24. These zeros of the Levenshtein polynomial also serve as quadrature nodes for the universal lower bound (27) and as Hermite interpolation nodes for the optimal LP polynomials.

In [2] the authors have done an extensive experimental investigation of energy-minimizing

point conﬁgurations, in particular they provide the computational minimizers for the Newton potential energy (h(t) = [2(1 − t)]−(n−2)/2) when n = 1,2,...,32 and N = 1,2,...,64. Table 1 compares the Newton energy from [2] and our universal lower bound (ULB) when n = 4 and N = 5,6,...,64.

![image 3](<2015-boyvalenkov-universal-lower-bounds-potential_images/imageFile3.png>)

Table 1. Newtonian (harmonic) energy comparison (see [2]) with ULB for n = 4, N = 5,...,64.

Utilizing the same Newton energy-minimizing conﬁgurations provided in [2] in Table 2 we compare our universal lower bound (ULB) with the Gauss potential (h(t) = e2t−2) energies of these conﬁgurations, which in general provide upper bounds on the minimal Gauss energy for the same choice of n = 4 and N = 5,6,...,64. We note that the error dramatically improves, which is to be expected, as the Hermite interpolants of analytic

potential functions are excellent approximants. Observe that for N = 5 and N = 8 the bounds are exact. Both cases are universally optimal.

![image 4](<2015-boyvalenkov-universal-lower-bounds-potential_images/imageFile4.png>)

Table 2. Gauss energy of the harmonic optimal conﬁgurations (as provided in [2]) compared with ULB for n = 4, N = 5,...,64.

As a consequence of the proof of Theorem 3.1 we describe the explicit LP solutions for m ≤ τ(n,N) in the next corollary.

- Corollary 3.4. The linear program (LP) can be solved for any m ≤ τ(n,N) and the solution in the class Pm ∩ An,h is given by the Hermite interpolants at the Levenshtein nodes determined by N = Lm(n,s).


Example 3.5. Here we present the suboptimal LP solutions for n = 4 and N = 24. In this case τ(n,N) = 5. For m = 1,...,5 we ﬁnd the intersection of N = 24 with L1(4,s),...,L5(4,s). The corresponding suboptimal solutions as Gegenbauer expansions

(up to three digits) are:

- f1(t) = .499P0(t) + .229P1(t)
- f2(t) = .581P0(t) + .305P1(t) + 0.093P2(t)
- f3(t) = .658P0(t) + .395P1(t) + .183P2(t) + 0.069P3(t)
- f4(t) = .69P0(t) + .43P1(t) + .23P2(t) + .10P3(t) + 0.027P4(t)
- f5(t) = .71P0(t) + .46P1(t) + .26P2(t) + .13P3(t) + 0.05P4(t) + 0.01P5(t).


![image 5](<2015-boyvalenkov-universal-lower-bounds-potential_images/imageFile5.png>)

Figure 3. Suboptimal LP solutions for n = 4 and N = 24.

A natural question is whether linear programming bounds can be improved if we consider polynomials of higher than τ(n,N) degree. The next section investigates this topic. As one would expect from our results thus far presented, the analogy with the situation for maximal spherical codes is quite close.

4. Necessary and sufficient conditions for optimality of the universal lower bounds

- 4.1. Test functions. Let n and N be ﬁxed, τ = τ(n,N) and Lτ(n,s) = N be as in


(18) and (19), and j be a positive integer. We introduce the following functions in n and s = αk:

k

1 N

ρiPj(n)(αi) for s ∈ Iτ.

+

- (30) Qj(n,s) :=


i=1

It follows that Qj(n,s) = 0 for 1 ≤ j ≤ τ and s ∈ Iτ (since this is the coeﬃcient f0 = 0 in the Gegenbauer expansion of Pj(n)(t)). Thus the functions Qj(n,s) are not interesting for these cases and so we assume below that j ≥ τ + 1 when s ∈ Iτ.

The next theorem shows that the functions Qj(n,s) give necessary and suﬃcient conditions for existence of improving polynomials of higher degrees.

- Theorem 4.1. The bounds (27) can be improved by a polynomial from An,h of degree at least τ + 1 if and only if Qj(n,s) < 0 for some j ≥ τ + 1. Furthermore, if h is strictly absolutely monotone and Qj(n,s) < 0 for some j ≥ τ + 1, then (27) can be improved by a polynomial from An,h of degree exactly j.


Proof. We give a proof for τ = 2k − 1. (Necessity) The necessity follows from Theorem 2.6 for I = {2k,2k + 1,...}. (Suﬃciency) Conversely, assume that h is strictly absolutely monotone and suppose

that Qj(n,s) < 0 for some j ≥ 2k. We shall improve the bound (27) by using the polynomial

f(t) =  Pj(n)(t) + g(t),

where > 0 and g(t) ∈ P2k−1 will be properly chosen. Denote h˜(t) := h(t) −  Pj(n)(t) and select such that h˜(t)(i)(t) ≥ 0 on [−1,1] for all i = 0,1,...,j. Observe, that for this choice of the function h˜(t) is absolutely monotone. The polynomial g(t) is chosen as the Hermite interpolant of h˜ at the nodes {αi}, i.e.

g(αi) = h˜(αi), g (αi) = h˜ (αi), i = 1,2,...,k.

Since h˜(t) is an absolutely monotone function, we infer as in Theorem 3.1 that g ∈ An,h˜, implying that f ∈ An,h.

Let g(t) = 2 =0k−1 g P(n) (t). Note that f0 = g0 and f(1) = g(1) + . We next prove that the bound given by f(t) is better that R2k−1(n,N;h). To this end, we multiply by ρi and sum up the ﬁrst interpolation equalities: k

k

k

ρiPj(n)(αi). Since

ρih(αi) −

ρig(αi) =

i=1

i=1

i=1

k

g(1) N by (21) and

ρig(αi) = g0 −

i=1

k

1 N

ρiPj(n)(αi) = Qj(n,s) −

i=1

by the deﬁnition of the test functions (30), we obtain g0 −

g(1) N

R2k−1(n,N;h) N2

N −  Qj(n,s) which is equivalent to

+

=

N(Ng0 − (g(1) + )) = R2k−1(n,N;h) −  N2Qj(n,s).

Therefore N(Nf0 − f(1)) = R2k−1(n,N;h) −  N2Qj(n,s) > R2k−1(n,N;h), i.e. the polynomial f(t) gives better bound indeed. We also obtained a new bound

- (31) W(n,N;h) ≥ R2k−1(n,N;h) −  N2Qj(n,s).

Theorem 4.1 provides a suﬃcient condition for solving the inﬁnite linear program (10).

- Corollary 4.2. If Qj(n,s) ≥ 0 for all j > τ(n,N), then fτh(n,N)(t) solves the linear program (10).


- 4.2. Investigation of the test functions. The test functions (30) coincide with the functions with the same name which were introduced and investigated in 1996 by Boyvalenkov, Danev and Bumova [11]. More details and all proofs are given in the dissertations [7] and [8]. We cite some results from [11, 7, 8] with only reformulations for energy bounds.


- Theorem 4.3 ([7], [8], [11]). The bounds Rτ(n,N;h) cannot be improved by using polynomials of degrees τ + 1 and τ + 2.


Set k1(n) := √n − 2 and let k2(n) ≥ 9 be such that

4n ≤ k2(n)2 − 4k2(n) + 5 + k2(n)4 − 8k2(n)3 − 6k2(n)2 + 24k2(n) + 25. Then we have the following theorems.

- Theorem 4.4. a) [7, Theorem 3.5.15], [8, Theorem 3.4.12] If n ≥ 3 and k ≥ k1(n), then all bounds R2k(n,N;h) corresponding to s in the open interval I2k can be improved by polynomials of degree 2k + 3.

b) [7, Theorem 3.5.9], [8, Theorem 3.4.14] If n ≥ 3 and k ≥ k2(n), then all bounds R2k−1(n,N;h) corresponding to s in the open interval I2k−1 can be improved by polynomials of degree 2k + 3.

- Theorem 4.5. a) If n ≥ 3 and k ≥ k1(n), then


- (32) E(n,N;h) ≥ R2k−1(n,N;h) −  N2Q2k+3(n,s). for every N ∈ (D(n,2k − 1),D(n,2k)) where is chosen as in Theorem 4.1.

b) If n ≥ 3 and k ≥ k2(n), then

- (33) E(n,N;h) ≥ R2k(n,N;h) −  N2Q2k+3(n,s). for every N ∈ (D(n,2k),D(n,2k + 1)) where is chosen as in Theorem 4.1.


Proof. This follows from (31) and the fact that Theorem 4.4 is based on the inequality Q2k+3(n,s) < 0 which holds true for the mentioned values of n and τ.

Another application of Theorem 4.4 concerns the sharp conﬁgurations. Recall that a sharp conﬁguration is a maximal spherical (n,L2k−1(n,s),s) =(dimension, cardinality, maximal cosine) code; i.e. a code that attains the odd Levenshtein bound L2k−1(n,s) (cf. [26]). In fact, the next corollary is implicit in [12] and follows from the main result of [28] as well.

Corollary 4.6. For any ﬁxed dimension n ≥ 3 only ﬁnitely many sharp conﬁgurations are possible.

Proof. Theorem 4.4 implies that in every ﬁxed dimension n ≥ 3 every Levenshtein

bound L2k−1(n,s) can be improved in the whole open interval t1k,0,t1k,1 provided k is large enough. The remaining end points correspond to tight spherical designs, which means (among many other things) that k ≤ 6 [3, 4]. This leaves only ﬁnitely many possible intervals I2k−1 where the Levenshtein bound L2k−1(n,s) can be attained. Every such interval contains ﬁnitely many s, corresponding to cardinalities N, which completes the proof.

We complete the subsection with the following conjecture, based on the above results and numerous investigations of the test functions as related to maximal spherical codes. Conjecture 4.7. If Qj(n,s) ≥ 0 for j = τ(n,N) + 3 and τ(n,N) + 4, then Qj(n,s) ≥ 0 for all j > τ(n,N).

- 4.3. Test functions and LP universality. We now apply the test functions to the study of universal conﬁgurations.


Deﬁnition 4.8. A spherical code C ⊂ Sn−1 of cardinality |C| = N is called LPuniversally optimal if

E(C;h) = W(n,N,P;h), for all absolutely monotone h, where P is the subspace of polynomials.

Remark 4.9. Observe that from (9) and (11) one infers that LP-universally optimal codes are in fact universally optimal. If the conjecture in Ballinger et al [2] is true, then Theorem 4.11 implies that the converse does not hold.

We derive a criterion for positivity of test functions of large enough j that can be used for proving that certain spherical codes of given dimension n and cardinality N are not LP-universally optimal. We utilize (n,N) to denote1 codes C ⊂ Rn with cardinality |C| = N. As examples, the cases (n,N) = (10,40), (14,64) and (15,128) are analyzed.

1We note that [2] uses (N, n) notation instead.

Sharp estimations for Gegenbauer polynomials can be derived from [19] (see also [24]). In [19, Theorem 1] the following inequality is given

- (34) max t∈[−1,1]

1 − t2w(t)p2j(t) ≤

2e(2 + α2 + β2) π

,

where {pj(t)} are the orthonormal Jacobi polynomials with weight w(t) = (1−t)α(1+t)β. Utilizing α = β = n−23 to get Gegenbauer polynomials and the normalization Pj(n)(1) = 1, we rewrite (34) as

- (35) |Pj(n)(t)| ≤

Γ n−21 (1 − t2)(n−2)/4

2n−2e(4 + (n − 3)√2)j! π(2j + n − 2)(j + n − 3)!

,

where Γ(x) is the Gamma function [34]. Note that for every ﬁxed n ≥ 3 and t ∈ (−1,1) the right-hand side of (35) is strictly monotone decreasing in j.

Let k, α1, α2 and ρ1 be as in Theorem 3.1. Denote by j0(n,N) the smallest degree j > τ(n,N) such that the right hand side of (35) is less than N1−1 when

- (36) t =

- α1 if α1 > −1,
- α2 if α1 = −1 and ρ1 < N1 ,


or less than N2−2 when t = α2 if α1 = −1 and ρ1 = 1/N. Theorem 4.10. Let n ≥ 3, N ≥ 2, and let k, α1, α2 and ρ1 be as in Theorem 3.1. Then Qj(n,αk) ≥ 0 for all j ≥ j0(n,N).

Proof. As the comments on the dynamical behavior of the quadrature nodes {αi} at the end of Section 2 indicate, we have |α1| ≥ |αi| for i = 2,...,k and in the case α1 = −1, we further have |α2| ≥ |αi| for i = 3,...,k.

We ﬁrst consider the case |α1| < 1; i.e., α1 > −1. If j ≥ j0(n,N) then we have

- (37) Qj(n,s) ≥


k

1 N −

1 N − 1 −

1 N ·

1 N − 1

ρi|Pj(n)(αi)| ≥

= 0

i=1

(we used N ki=1 ρi = N − 1 following from (12) for f(t) = 1). The case α1 = −1 and ρ1 < 1/N is handled similarly using (35) as suggested by the second line of (36).

For the ﬁnal special case α1 = −1 and ρ1 = 1/N it is clear (cf. [12]) that Qj(n,s) = 0

for odd j. The case of even j follows similarly as above using the facts that Pj(n)(−1) = 1 and that |αi| ≤ |α2| for i = 3,...,k.

- Theorem 4.10 gives a useful tool for disproving LP-universal optimality. For given n


and N and numerics suggesting that Corollary 4.2 may hold one ﬁnds explicit j0(n,N) and calculates the remaining test functions Qj(n,s) for every j ∈ {τ(n,N)+3,τ(n,N)+

- 4,...,j0(n,N) − 1}. This will be applied in the next subsection for some codes from [2].


4.4. Examples. Table 3 lists the ﬁrst twenty test functions for some interesting conﬁgurations. We utilize (n,N) to denote codes C ⊂ Rn with cardinality |C| = N.

![image 6](<2015-boyvalenkov-universal-lower-bounds-potential_images/imageFile6.png>)

Table 3. Test functions for some special (n,N) spherical codes.

Judging by the behavior of the test functions the linear programming method will provide improvements on our ULB for (4,24) and (7,182) but it is unlikely to give a solution similar to the case with the 600-cell (4,120), where a polynomial in P17 served as an exact lower bound. Indeed, that the test functions Q14,Q15 and Q17 are negative provides additional insight on the unique property of the 600-cell as the only universally optimal code known that is not a sharp conﬁguration.

The ﬁrst conﬁguration (4,24) is the D4 root system, or the so-called kissing number conﬁguration in R4 (see [30]), which was shown by Cohn, Conway, Elkies, and Kumar (see [13]) not to be universal. The negative test functions Q8(4,s) and Q9(4,s), s = α2 ≈ 0.4749504897, suggest searching for a polynomial f(t) = 9i=0 fiPi(4)(t) with f6 = f7 = 0 and four touching points of the graphs of f(t) and the potential h(t). We have developed a numerical algorithm for handling such situations. For example, if h(t) = 2(11−t) is the

Newton potential, our numerical calculations led to the polynomial f(t) = 0.4987 + 0.4852t + 0.4535t2 + 0.5546t3 + 0.9401t4 + 0.8425t5 −0.3305t6 − 0.7479t7 + 0.1889t8 + 0.37394t9

= 0.0073P9(4)(t) + 0.0066P8(4)(t) + 0.0659P5(4)(t) + 0.2384P4(4)(t) + 0.5116P3(4)(t)

+0.7915P2(4)(t) + 0.9236P1(4)(t) + 0.7142P0(4)(t).

The Hermite interpolation points are approximately −0.860297, −0.489872, −0.195724 and 0.47850. The bound obtained from f(t) is 333.1575, while the universal lower bound (27) gives R5(4,24;1/(2(1 − t)) = 333 and the energy of the D4 root system is 334. Theoretical and computational aspects of the aforementioned algorithm for improvements (when possible) of our ULB and their nature will be discussed elsewhere.

- Theorem 4.11. The spherical codes (n,N) = (10,40), (14,64) and (15,128) are not LP-universally optimal.


Proof. The codes (10,40) and (14,64) were conjectured by Ballinger, Blekherman, Cohn, Giansiracusa, Kelly, and Schu¨rmann in [2] to be universally optimal. It follows from Theorem 4.10 and numerical calculations as explained in the end of the last subsection that these codes are not LP-universally optimal. Indeed, we have τ(10,40) = 3 (so α1 > −1), j0(10,40) = 10 and the second column in Table 3 shows that this code is not LP-universally optimal. Similarly, τ(14,64) = 3, j0(14,64) = 8, and the inspection of the third column of Table 3 suﬃces. The code (15,128) was not conjectured to be universally optimal (but not eliminated) in [2] and we see that it is not LP-universally optimal because of τ(15,128) = 3, j0(14,64) = 9, and the fourth column in Table 3.

References

- [1] N. N. Andreev, Location of points on a sphere with minimal energy, Tr. Math. Inst. Steklova 219, 27–31, (1997) (in Russian); English translation: Proc. Inst. Math Steklov 219, 20–24, (1997).
- [2] B. Ballinger, G. Blekherman, H. Cohn, N. Giansiracusa, E. Kelly, A. Shu˝rmann, Experimental Study of Energy-minimizing Point Conﬁgurations on Spheres, Experiment. Math. 18, 257–283, (2009).
- [3] E. Bannai, R. M. Damerell, Tight spherical designs I, J. Math. Soc. Japan 31, 199-207 (1979).
- [4] E. Bannai, R. M. Damerell, Tight spherical designs II, J. London Math. Soc. 21, 1980, 13-30.
- [5] B. Beckermann, J. Bustamante, R. Martinez-Cruz, J. Quesada, Gaussian, Lobatto and Radau positive quadrature rules with a prescribed abscissa, Calcolo 51, 319–328, (2014).
- [6] S. Borodachov, D. Hardin, E. Saﬀ, Minimal Discrete Energy on the Sphere and other Manifolds, Springer, 2015 (to appear).
- [7] S. P. Boumova, Applications of polynomials to spherical codes and designs, PhD Dissert., TU Eindhoven, 2001.
- [8] P. G. Boyvalenkov, Linear programming bounds for spherical codes and designs, Dr.Sci. Dissert., Inst. Math. Inf. BAS, Soﬁa, 2004 (in Bulgarian).
- [9] P. Boyvalenkov, S. Bumova, D. Danev, Necessary conditions for existence of some designs in polynomial metric spaces, Europ. J. Combin. 20 213–225, (1999).
- [10] P. G. Boyvalenkov, D. P. Danev, On maximal codes in polynomial metric spaces, Lecture Notes in Computer Science 1255, 29-38, (1997).


- [11] P. G. Boyvalenkov, D. P. Danev, S. P. Bumova, Upper bounds on the minimum distance of spherical codes, IEEE Trans. Inform. Theory 41, 1576–1581, (1996).
- [12] P. Boyvalenkov, D. Danev, I. Landjev, On maximal spherical codes II, J. Combin. Des. 7, 1999, 316-326.
- [13] H. Cohn, J. Conway, N. Elkies, A. Kumar, The D4 root system is not universally optimal, Experiment. Math. 16, 313–320, (2007).
- [14] H. Cohn, A. Kumar, Universally optimal distribution of points on spheres, J. of Amer. Math. Soc. 20, 99–148, (2006).
- [15] H. Cohn, J. Woo, Three point bounds for energy minimization, J. of Amer. Math. Soc. 25, 929–958,

(2012).

- [16] P. J. Davis, Interpolation and Approximation, Blaisdell Publishing Company, New York, 1963.
- [17] P. Delsarte, An Algebraic Approach to the Association Schemes in Coding Theory, Philips Res. Rep. Suppl. 10, (1973).
- [18] P. Delsarte, J.-M. Goethals, J. J. Seidel, Spherical codes and designs, Geom. Dedicata 6, 363–388,

(1977).

- [19] T. Erde´lyi, A. Magnus, P. Nevai, Generalized Jacobi weights, Christoﬀel functions, and Jacobi polynomials, SIAM J. Math. Anal. 25, 602–614, (1994).
- [20] D. P. Hardin, E. B. Saﬀ, Discretizing manifolds via minimum energy points, Notices Amer. Math. Soc. 51, 1186–1194, (2004).
- [21] G. A. Kabatiansky, V. I. Levenshtein, Bounds for packings on a sphere and in space (Russian), Problemy Peredachi Informacii 14, 3–25, (1978); English translation in Problems of Information Transmission 14, 1–17, (1978).
- [22] A. V. Kolushov, V. A. Yudin, Extremal dispositions of points on the sphere, Anal. Math. 23, 25–34,

(1997).

- [23] T. H. Koorwinder, The addition formula for Jacobi polynomials and spherical harmonics, SIAM J. Appl. Math. 25, 236–246, (1973).
- [24] I. Krasikov, An upper bound on Jacobi polynomials, J. Approx. Theory 149, 116–130, (2007).
- [25] V. I. Levenshtein, Bounds for packings in metric spaces and certain applications, Probl. Kibernetiki 40, 44–110, (1983) (in Russian).
- [26] V. I. Levenshtein, Designs as maximum codes in polynomial metric spaces, Acta Appl. Math. 25, 1–82, (1992).
- [27] V. I. Levenshtein, Universal bounds for codes and designs, Handbook of Coding Theory, V. S. Pless and W. C. Huﬀman, Eds., Elsevier, Amsterdam, Ch. 6, 499–648, (1998).
- [28] W. J. Matrin, J. S Williford, There are ﬁnitely many Q-polynomial association schemes with given ﬁrst multiplicity at least three, Europ. J. Combin. 30, 698–704 (2009).
- [29] C. Mu¨ller. Spherical harmonics, Lecture Notes in Mathematics 17, Springer-Verlag, Berlin, 1966.
- [30] O. Musin, The kissing number in four dimensions. Ann. of Math., 168, 1–32, (2008).
- [31] E. B. Saﬀ, A. B. J. Kuijlaars, Distributing many points on a sphere, Math. Intelligencer 19, 5–11,

(1997).

- [32] V. M. Sidelnikov, On extremal polynomials used to estimate the size of codes, Problems of Information Transmission 16, 174–186, (1980).
- [33] G. Szego¨, Orthogonal polynomials, AMS Col. Publ., 23, Providence, RI, 1939.
- [34] G. N. Watson, A Treatise of the Theory of Bessel Functions, Cambridge Univ. Press 1995.
- [35] V. A. Yudin, Minimal potential energy of a point system of charges, Discret. Mat. 4, 115–121, (1992) (in Russian); English translation: Discr. Math. Appl. 3, 75–81, (1993).


Institute of Mathematics and Informatics, Bulgarian Academy of Sciences, 8 G Bonchev Str., 1113 Sofia, Bulgaria, and Faculty of Mathematics and Natural Sciences, SouthWestern University, Blagoevgrad, Bulgaria.

E-mail address: peter@math.bas.bg Department of Mathematical Sciences, Indiana-Purdue University Fort Wayne, IN 46805,

USA E-mail address: dragnevp@ipfw.edu Center for Constructive Approximation, Department of Mathematics, Vanderbilt Uni-

versity, Nashville, TN 37240, USA E-mail address: doug.hardin@vanderbilt.edu E-mail address: edward.b.saff@vanderbilt.edu Faculty of Mathematics and Informatics, Sofia University, 5 James Bourchier Blvd.,

1164 Sofia, Bulgaria E-mail address: stoyanova@fmi.uni-sofia.bg

