# arXiv:1803.08079v1[math.OC]21Mar2018

## SPECTRAHEDRAL LIFTS OF CONVEX SETS

REKHA R. THOMAS

Abstract. Eﬃcient representations of convex sets are of crucial importance for many algorithms that work with them. It is well-known that sometimes, a complicated convex set can be expressed as the projection of a much simpler set in higher dimensions called a lift of the original set. This is a brief survey of recent developments in the topic of lifts of convex sets. Our focus will be on lifts that arise from aﬃne slices of real positive semideﬁnite cones known as psd or spectrahedral lifts. The main result is that projection representations of a convex set are controlled by factorizations, through closed convex cones, of an operator that comes from the convex set. This leads to several research directions and results that lie at the intersection of convex geometry, combinatorics, real algebraic geometry, optimization, computer science and more.

1. Introduction

Eﬃcient representations of convex sets are of fundamental importance in many areas of mathematics. An old idea from optimization for creating a compact representation of a convex set is to express it as the projection of a higher-dimensional set that might potentially be simpler, see for example [CCZ10], [BTN01]. In many cases, this technique oﬀers surprisingly compact representations of the original convex set. We present the basic questions that arise in the context of projection representations, provide some answers, pose more questions, and examine the current limitations and challenges.

As a motivating example, consider a full-dimensional convex polytope P ⊂ Rn. Recall that P can be expressed either as the convex hull of a ﬁnite collection of points in Rn or as the intersection of a ﬁnite set of linear halfspaces. The minimal set of points needed in the convex hull representation are the vertices of P, and the irredundant inequalities needed are in bijection with the facets (codimension-one faces) of P. Therefore, if the number of facets of P is exponential in n, then the linear inequality representation of P is of size exponential in n. The complexity of optimizing a linear function over P depends on the size of its inequality representation and hence it is worthwhile to ask if eﬃcient inequality representations can be obtained through some indirect means such as projections. We illustrate the idea on two examples.

Example 1.1. The n-dimensional crosspolytope Cn is the convex hull of the standard unit vectors ei ∈ Rn and their negatives [Zie95, Example 0.4]. For example, C2

Date: March 23, 2018.

The author was partially supported by the U.S. National Science Foundation grant DMS1719538. This paper was written while the author was in residence at the Mathematical Sciences Research Institute in Berkeley, California, during the Fall 2017 semester, and based on work supported by the National Science Foundation under Grant No. 1440140.

1

![image 1](<2018-thomas-spectrahedral-lifts-convex-sets_images/imageFile1.png>)

![image 2](<2018-thomas-spectrahedral-lifts-convex-sets_images/imageFile2.png>)

Figure 1. The permutahedron Π4 and the crosspolytope C3.

is a square and C3 is an octahedron, see Figure 1. Written in terms of inequalities, Cn = {x ∈ Rn : ±x1 ± x2 ± ··· ± xn ≤ 1}

and all 2n inequalities listed are needed as they deﬁne facets of Cn. However, Cn is also the projection onto x-coordinates of the polytope

n

Qn = (x,y) ∈ R2n :

yi = 1, −yi ≤ xi ≤ yi ∀i = 1,...,n which involves only 2n inequalities and one equation.

i=1

- Example 1.2. The permutahedron Πn is the (n − 1)-dimensional polytope that is the convex hull of all vectors obtained by permuting the coordinates of the ndimensional vector (1,2,3,...,n). It has 2n − 2 facets, each indexed by a proper subset of [n] := {1,2,...,n} [Zie95, Example 0.10]. In [Goe15], Goemans used


sorting networks to show that Πn is the linear image of a polytope Qn that has Θ(n log n) variables and facets, and also argued that one cannot do better.

The key takeaway from the above examples is that one can sometimes ﬁnd eﬃcient linear representations of polytopes if extra variables are allowed; a complicated polytope P ⊂ Rn might be the linear projection of a polytope Q ⊂ Rn+k with many fewer facets. To be considered eﬃcient, both k and the number of facets of Q must be polynomial functions of n. Such a polytope Q is called a lift or extended formulation of P. Since optimizing a linear function over P is equivalent to optimizing the same function over a lift of it, these projection representations oﬀer the possibility of eﬃcient algorithms for linear programming over P.

Polytopes are special cases of closed convex sets and one can study closed convex lifts in this more general context. All convex sets are slices of closed convex cones by aﬃne planes and hence we will look at lifts of convex sets that have this form. Formally, given a closed convex cone K ⊂ Rm, an aﬃne plane L ⊂ Rm, and a convex set C ⊂ Rn, we say that K ∩ L is a K-lift of C if C = π(K ∩ L) for some linear map π : Rm → Rn. Recall that every polytope is an aﬃne slice of a nonnegative orthant Rk+ and hence polyhedral lifts of polytopes, as we saw in Examples 1.1 and 1.2, are special cases of cone lifts. A polytope can also have non-polyhedral lifts.

The main source of non-polyhedral lifts in this paper will come from the positive semideﬁnite cone S+k of k × k real symmetric positive semideﬁnite (psd) matrices.

![image 3](<2018-thomas-spectrahedral-lifts-convex-sets_images/imageFile3.png>)

Figure 2. A spectrahedral lift of a square.

If a matrix X is psd, we write X 0. An aﬃne slice of S+k is called a spectrahedron of size k. If a spectrahedron (of size k) is a lift of a convex set C, we say that C admits a spectrahedral or psd lift (of size k). It is also common to say that C is sdp representable or a projected spectrahedron or a spectrahedral shadow. Note that a spectrahedron in S+k can also be written in the form

t

x ∈ Rt : A0 +

Aixi 0

i=1

where A0,A1,...,At are real symmetric matrices of size k.

- Example 1.3. The square P ⊂ R2 with vertices (±1,±1) can be expressed as the projection of a spectrahedron as follows:

P =

 



(x,y) ∈ R2 : ∃z ∈ R s.t.

 

1 x y

- x 1 z
- y z 1


  0

 



.

The spectrahedral lift in this example is known as the elliptope and is shown in Figure 2. It consists of all X ∈ S+3 such that Xii = 1 for i = 1,2,3.

- Example 1.4. Given a graph G = ([n],E) with vertex set [n] and edge set E, a collection S ⊆ [n] is called a stable set if for each i,j ∈ S, the pair {i,j}  ∈ E. Each stable set S is uniquely identiﬁed by its incidence vector χS ∈ {0,1}n deﬁned as (χS)i = 1 if i ∈ S and 0 otherwise. The stable set polytope of G is


STAB(G) := conv{χS : S stable set in G} where conv denotes convex hull. For x = χS, consider the rank one matrix in S+n+1

1 x x xx

1 x

1 x x U

1 x =

=

.

Since χS ∈ {0,1}n, Uii = xi for all i ∈ [n], and since S is stable, Uij = 0 for all {i,j} ∈ E. Therefore, the convex set

 

 

1 x x U

∃U ∈ S+n s.t.

0,

x ∈ Rn :

TH(G) :=

Uii = xi ∀i ∈ [n], Uij = 0 ∀{i,j} ∈ E





known as the theta body of G, contains all the vertices of STAB(G), and hence by convexity, all of STAB(G). In general, this containment is strict. The theta body TH(G) is the projection onto x-coordinates of the set of all matrices in S+n+1 whose entries satisfy a set of linear constraints. The latter is a spectrahedron.

Theta bodies of graphs were deﬁned by Lov´sz in [Lov79]. He proved that STAB(G) = TH(G) if and only if G is a perfect graph. Even for perfect graphs, STAB(G) can have exponentially many facets, but by Lov´sz’s result, it admits a spectrahedral lift of size n + 1.

We close the introduction with a psd lift of a non-polytopal convex set. Since polyhedra can only project to polyhedra, any lift of a non-polyhedral convex set is necessarily non-polyhedral.

- Example 1.5. Let X be the n×n symbolic matrix with entries x1,...,xn2 written consecutively along its n rows. and let In denote the n×n identity matrix. Consider


the spectrahedron of size 2n deﬁned by the conditions

 

  0, trace(Y ) = 1.

Y X

X In

The psd condition is equivalent to Y − XX 0 via Schur complement. Taking the trace on both sides we get 1 = trace(Y ) ≥ trace(XX ) = n

2

i=1 x2i. Thus, the projection of the above spectrahedron onto x = (x1,...,xn2) is contained in the unit ball

Bn2 := {(x1,...,xn2) : x2i ≤ 1}. On the other hand, for any x on the boundary of Bn2, the matrix

 

 

XX X

X In

lies in the above spectrahedron and projects onto x. We conclude that Bn2 has a spectrahedral lift of size O(n).

In many of the above cases, projections oﬀer a more compact representation of the convex set in question compared to the natural representation the set came with. Two fundamental questions we can ask now are the following.

- Question 1.6. Given a convex set C ⊂ Rn and a closed convex cone K ⊂ Rm, does C admit a K-lift?
- Question 1.7. If K comes from a family of cones {Kt ⊂ Rt} such as the set of all positive orthants or the set of all psd cones, what is the smallest t for which C admits a Kt-lift? The smallest such t is a measure of complexity of C.


We will address both these questions and discuss several further related directions and results. In Section 2 we prove that the existence of a K-lift for a convex set C is controlled by the existence of a K-factorization of an operator associated to C. This result specializes nicely to polytopes as we will see in Section 3. These factorization theorems generalize a celebrated result of Yannakakis [Yan91] about polyhedral lifts of polytopes. The rest of the sections are focussed on spectrahedral lifts of convex sets. In Section 4 we deﬁne the notion of positive semideﬁnite rank (psd rank) of a convex set and explain the known bounds on this invariant. We also mention recent

results about psd ranks of certain families of convex sets. The psd rank of an ndimensional polytope is known to be at least n+1. In Section 5, we explore the class of polytopes that have this minimum possible psd rank. We conclude in Section 6 with the basic connections between sum of squares polynomials and spectrahedral lifts. We also describe the recent breakthrough by Scheiderer that provides the ﬁrst examples of convex semialgebraic sets that do not admit spectrahedral lifts.

2. The Factorization Theorem for Convex Sets

A convex set is called a convex body if it is compact and contains the origin in its interior. For simplicity, we will always assume that all our convex sets are convex bodies. Recall that the polar of a convex set C ⊂ Rn is the set

C◦ = {y ∈ Rn : x,y ≤ 1, ∀x ∈ C}. Let ext(C) denote the set of extreme points of C, namely, all points p ∈ C such that if p = (p1 + p2)/2, with p1,p2 ∈ C, then p = p1 = p2. Both C and C◦ are convex hulls of their respective extreme points. Consider the operator S : Rn × Rn → R deﬁned by S(x,y) = 1 − x,y . The slack operator SC, of a convex set C ⊂ Rn, is the restriction of the operator S to ext(C) × ext(C◦). Note that the range of SC is contained in R+, the set of nonnegative real numbers.

- Deﬁnition 2.1. Let K ⊂ Rm be a full-dimensional closed convex cone and C ⊂ Rn a full-dimensional convex body. A K-lift of C is a set Q = K ∩ L, where L ⊂ Rm is an aﬃne subspace, and π : Rm → Rn is a linear map such that C = π(Q). If L intersects the interior of K we say that Q is a proper K-lift of C.

We will see that the existence of a K-lift of C is intimately related to properties of the slack operator SC. Recall that the dual of a closed convex cone K ⊂ Rm is K∗ = {y ∈ Rm : x,y ≥ 0, ∀x ∈ K}.

- A cone K is self-dual if K∗ = K. The cones Rn+ and S+k are self-dual.


- Deﬁnition 2.2. Let C and K be as in Deﬁnition 2.1. We say that the slack operator SC is K-factorizable if there exist maps (not necessarily linear)


A : ext(C) → K and B : ext(C◦) → K∗ such that SC(x,y) = A(x),B(y) for all (x,y) ∈ ext(C) × ext(C◦).

We can now characterize the existence of a K-lift of C in terms of the operator SC, answering Problem 1.6. The proof relies on the theory of convex cone programming which is the problem of optimizing a linear function over an aﬃne slice of a closed convex cone, see [BTN01], or [BPT13, §2.1.4] for a quick introduction.

- Theorem 2.3. [GPT13, Theorem 1] If C has a proper K-lift then SC is Kfactorizable. Conversely, if SC is K-factorizable then C has a K-lift.


Proof. Suppose C has a proper K-lift. Then there exists an aﬃne space L = w0+L0 in Rm (L0 is a linear subspace) and a linear map π : Rm → Rn such that C = π(K ∩ L) and w0 ∈ int(K). Equivalently,

C = {x ∈ Rn : x = π(w), w ∈ K ∩ (w0 + L0)}. We need to construct the maps A : ext(C) → K and B : ext(C◦) → K∗ that factorize the slack operator SC, from the K-lift of C. For xi ∈ ext(C), deﬁne A(xi) := wi, where wi is any point in the non-empty convex set π−1(xi) ∩ K ∩ L.

Let c be an extreme point of C◦. Then max{ c,x : x ∈ C } = 1 since c,x ≤ 1 for all x ∈ C, and if the maximum was smaller than one, then c would not be an extreme point of C◦. Let M be a full row rank matrix such that kerM = L0. Then the following hold:

= max π∗(c),w

1 = max c,x x ∈ C

= max c,π(w) w ∈ K ∩ (w0 + L0)

Mw = Mw0 w ∈ K

Since w0 lies in the interior of K, by Slater’s condition we have strong duality for the above cone program, and we get

1 = min Mw0,y : MTy − π∗(c) ∈ K∗ with the minimum being attained. Further, setting z = MTy we have that

1 = min w0,z : z − π∗(c) ∈ K∗, z ∈ L⊥0 with the minimum being attained. Now deﬁne B : ext(C◦) → K∗ as the map that sends yi ∈ ext(C◦) to B(yi) := z − π∗(yi), where z is any point in the nonempty convex set L⊥0 ∩ (K∗ + π∗(yi)) that satisﬁes w0,z = 1. Note that for such a z,

wi,z = 1 for all wi ∈ L. Then B(yi) ∈ K∗, and for an xi ∈ ext(C), xi,yi = π(wi),yi = wi,π∗(yi) = wi,z − B(yi)

= 1 − wi,B(yi) = 1 − A(xi),B(yi) .

Therefore, SC(xi,yi) = 1 − xi,yi = A(xi),B(yi) for all xi ∈ ext(C) and yi ∈ ext(C◦).

Suppose now SC is K-factorizable, i.e., there exist maps A : ext(C) → K and B : ext(C◦) → K∗ such that SC(x,y) = A(x),B(y) for all (x,y) ∈ ext(C) × ext(C◦). Consider the aﬃne space

L = {(x,z) ∈ Rn × Rm : 1 − x,y = z,B(y) , ∀ y ∈ ext(C◦)},

and let LK be its coordinate projection into Rm. Note that 0  ∈ LK since otherwise, there exists x ∈ Rn such that 1− x,y = 0 for all y ∈ ext(C◦) which implies that C◦ lies in the aﬃne hyperplane x,y = 1. This is a contradiction since C◦ contains the origin. Also, K ∩LK = ∅ since for each x ∈ ext(C), A(x) ∈ K ∩LK by assumption.

Let x be some point in Rn such that there exists some z ∈ K for which (x,z) is in L. Then, for all extreme points y of C◦ we will have that 1 −  x,y is nonnegative. This implies, using convexity, that 1 − x,y is nonnegative for all y in C◦, hence x ∈ (C◦)◦ = C.

We now argue that this implies that for each z ∈ K ∩ LK there exists a unique xz ∈ Rn such that (xz,z) ∈ L. That there is one, comes immediately from the deﬁnition of LK. Suppose now that there is another such point x z. Then (txz + (1 − t)x z,z) ∈ L for all reals t which would imply that the line through xz and x z would be contained in C, contradicting our assumption that C is compact.

The map that sends z to xz is therefore well-deﬁned in K ∩ LK, and can be easily checked to be aﬃne. Since the origin is not in LK, we can extend it to a linear map π : Rm → Rn. To ﬁnish the proof it is enough to show C = π(K ∩ LK). We have already seen that π(K ∩ LK) ⊆ C so we just have to show the reverse inclusion. For all extreme points x of C, A(x) belongs to K ∩ LK, and therefore, x = π(A(x)) ∈ π(K ∩ LK). Since C = conv(ext(C)) and π(K ∩ LK) is convex, C ⊆ π(K ∩ LK).

The asymmetry in the two directions of Theorem 2.3 disappears for many nice

cones including Rk+ and S+k. For more on this, see [GPT13, Corollary 1]. In these nice cases, C has a K-lift if and only if SC has a K-factorization. Theorem 2.3 generalizes the original factorization theorem of Yannakakis for polyhedral lifts of polytopes [Yan91, Theorem 3, §4] to arbitrary cone lifts of convex sets.

Recall that in the psd cone S+k, the inner product A,B = trace(AB).

- Example 2.4. The unit disk C ⊂ R2 is a spectrahedron in S+2 as follows

C = (x,y) ∈ R2 :

1 + x y y 1 − x

0 ,

and hence trivially has a S+2 -lift. This means that the slack operator SC must have a S+2 factorization. Since C◦ = C, ext(C) = ext(C◦) = ∂C, and so we have to ﬁnd maps A,B : ext(C) → S+2 such that for all (x1,y1),(x2,y2) ∈ ext(C),

A(x1,y1),B(x2,y2) = 1 − x1x2 − y1y2. This is accomplished by the maps

A(x1,y1) =

1 + x1 y1

y1 1 − x1 and

B(x2,y2) =

- 1

- 2


1 − x2 −y2 −y2 1 + x2 which factorize SC and are positive semideﬁnite in their domains.

- Example 2.5. Consider the spectrahedral lift of the unit ball Bn2 from Example 1.5. Again, we have that ext(Bn2) = ext(Bn◦2) = ∂Bn2. The maps


- 1

- 2


In −Y −Y Y Y

XX X X In

A(x) =

, B(y) =

where X is deﬁned as in Example 1.5 and Y is deﬁned the same way, oﬀer a S+2nfactorization of the slack operator of Bn2.

The existence of cone lifts of convex bodies is preserved under many geometric operations [GPT13, Propositions 1 and 2]. For instance, if C has a K-lift, then so does any compact image of C under a projective transformation. An elegant feature of this theory is that the existence of lifts is invariant under polarity/duality; C has a K-lift if and only if C◦ has a K∗-lift. In particular, if C has a spectrahedral lift of size k, then so does C◦.

3. The Factorization Theorem for Polytopes

When the convex body C is a polytope, Theorem 2.3 becomes rather simple. This specialization also appeared in [FMP+12].

- Deﬁnition 3.1. Let P be a full-dimensional polytope in Rn with vertex set VP = {p1,...,pv} and an irredundant inequality representation


P = {x ∈ Rn : h1(x) ≥ 0,...,hf(x) ≥ 0}.

Since P is a convex body, we may assume that the constant in each hj(x) is 1. The slack matrix of P is the nonnegative v × f matrix whose (i,j)-entry is hj(pi), the slack of vertex pi in the facet inequality hj(x) ≥ 0.

When P is a polytope, ext(P) is just VP, and ext(P◦) is in bijection with FP, the set of facets of P. The facet Fj is deﬁned by hj(x) ≥ 0 and f := |FP|. Then the slack operator SP is the map from VP × FP to R+ that sends the vertex facet pair (pi,Fj) to hj(pi). Hence, we may identify the slack operator of P with the slack matrix of P and use SP to also denote this matrix. Since the facet inequalities of P are only unique up to multiplication by positive scalars, the matrix SP is also only unique up to multiplication of its columns by positive scalars. Regardless, we will call SP, derived from the given presentation of P, the slack matrix of P.

- Deﬁnition 3.2. Let M = (Mij) ∈ Rp+×q be a nonnegative matrix and K a closed convex cone. Then a K-factorization of M is a pair of ordered sets {a1,...,ap} ⊂ K and {b1,...,bq} ⊂ K∗ such that ai,bj = Mij.


Note that M ∈ Rp+×q has a Rk+-factorization if and only if there exist a p × k nonnegative matrix A and a k × q nonnegative matrix B such that M = AB, called a nonnegative factorization of M. Deﬁnition 3.2 generalizes nonnegative factorizations of nonnegative matrices to cone factorizations.

- Theorem 3.3. If a full-dimensional polytope P has a proper K-lift then every slack matrix of P admits a K-factorization. Conversely, if some slack matrix of P has a K-factorization then P has a K-lift.


Theorem 3.3 is a direct translation of Theorem 2.3 using the identiﬁcation between the slack operator of P and the slack matrix of P. The original theorem of Yannakakis [Yan91, Theorem 3, §4] proved this result in the case where K = Rk+.

- Example 3.4. Consider the regular hexagon with inequality description


1 √3/3 0 2√3/3













1 1 1 1 1 1





−1 √3/3 −1 −

x1 x2 ≤

√3/3 0 −2√3/3 1 −

(x1,x2) ∈ R2 :

.

H =

 

 

 

 





√3/3

We will denote the coeﬃcient matrix by F and the right hand side vector by d. It is easy to check that H cannot be the projection of an aﬃne slice of Rk+ for k < 5. Therefore, we ask whether it can be the linear image of an aﬃne slice of R5+. Using

- Theorem 3.3 this is equivalent to asking if the slack matrix of the hexagon,




SH :=

 



- 0 0 1 2 2 1
- 1 0 0 1 2 2
- 2 1 0 0 1 2 2 2 1 0 0 1 1 2 2 1 0 0 0 1 2 2 1 0


,

 

![image 4](<2018-thomas-spectrahedral-lifts-convex-sets_images/imageFile4.png>)

Figure 3. A R5+-lift of the regular hexagon.

has a R5+-factorization. Check that





1 0 1 0 0 1 0 0 0 1





- 0 0 0 1 2 1
- 1 2 1 0 0 0


- 0 0 0 1 2
- 0 1 0 0 1 0 1 1 0 0 0 0 2 1 0


- 0 0 1 1 0 0
- 0 1 0 0 1 0 1 0 0 0 0 1


,

SH =

 

 

 

 

where we call the ﬁrst matrix A and the second matrix B. We may take the rows of A as elements of R5+, and the columns of B as elements of R5+ = (R5+)∗, and they provide us a R5+-factorization of the slack matrix SH, proving that this hexagon has a R5+-lift while the trivial polyhedral lift would have been to R6+.

We can construct the lift using the proof of the Theorem 2.3. Note that H = {(x1,x2) ∈ R2 : ∃ y ∈ R5+ s.t. Fx + BTy = d}. Hence, the exact slice of R5+ that is mapped to the hexagon is simply

{y ∈ R5+ : ∃ x ∈ R2 s.t. BTy = d − Fx}. By eliminating the x variables in the system we get

{y ∈ R5+ : y1 + y2 + y3 + y5 = 2,y3 + y4 + y5 = 1},

and so we have a three dimensional slice of R5+ projecting down to H. This projection is visualized in Figure 3.

The hexagon is a good example to see that the existence of lifts depends on more than the combinatorics of the polytope. If instead of a regular hexagon we take the hexagon with vertices (0,−1), (1,−1), (2,0), (1,3), (0,2) and (−1,0), a valid slack matrix would be





- 0 0 1 4 3 1
- 1 0 0 4 4 3 7 4 0 0 4 9


S :=

.

- 3 4 4 0 0 1
- 3 5 6 1 0 0 0 1 3 5 3 0


 

 

One can check that if a 6 × 6 matrix with the zero pattern of a slack matrix of a hexagon has a R5+-factorization, then it has a factorization with either the same zero pattern as the matrices A and B obtained before, or the patterns given by applying a cyclic permutation to the rows of A and the columns of B. A simple algebraic computation then shows that the slack matrix S above has no such decomposition hence this irregular hexagon has no R5+-lift.

- Example 3.5. In Example 1.3 we saw a S+3 -lift of a square P. Up to scaling of columns by positive numbers, the slack matrix of P is


  

  

- 0 0 1 1
- 0 1 1 0 1 1 0 0 1 0 0 1


SP =

where the rows are associated to the vertices (1,1), (1,−1), (−1,−1), (−1,1) in that order, and the columns to the facets deﬁned by the inequalities

1 − x1 ≥ 0, 1 − x2 ≥ 0, 1 + x1 ≥ 0, 1 + x2 ≥ 0.

The matrix SP admits the following S+3 -factorization where the ﬁrst four matrices are associated to the rows of SP and the next four matrices are associated to the columns of SP:

 ,

 

 ,

 

 ,

 

 

 

1 1 −1 1 1 −1

1 −1 −1

1 −1 1 −1 1 −1 1 −1 1

1 1 1 1 1 1 1 1 1

−1 1 1 −1 1 1

−1 −1 1

 

 ,

 

 ,

 

 ,

 

 .

1 −1 0 −1 1 0 0 0 0

1 0 −1 0 0 0

1 1 0 1 1 0 0 0 0

1 0 1

1 4

1 4

1 4

1 4

- 0 0 0
- 1 0 1


−1 0 1

4. Positive Semidefinite Rank

From now on we focus on the special case of spectrahedral lifts of convex sets. Since the family of psd cones {S+k : k ∈ N} is closed in the sense that any face of a member S+i in the family is isomorphic to S+j for some j ≤ i, we can look at the smallest index k for which a convex set C admits a S+k-lift.

- Deﬁnition 4.1. The psd rank of a convex set C ⊂ Rn, denoted as rankpsd(C) is


the smallest positive integer k such that C = π(S+k ∩L) for some aﬃne space L and linear map π. If C does not admit a psd lift, then deﬁne rankpsd(C) = ∞.

The following lemma is immediate from the previous sections and oﬀers an explicit tool for establishing psd ranks.

- Lemma 4.2. The psd rank of a convex set C is the smallest k for which the slack operator SC admits a S+k-factorization. If P is a polytope, then rankpsd(P) is the smallest integer k for which the slack matrix SP admits a S+k-factorization.


Following Deﬁnition 3.2, for any nonnegative matrix M ∈ Rp+×q, one can deﬁne rankpsd(M) to be the smallest integer k such that M admits a S+k-factorization. The relationship between rankpsd(M) and rank(M) is as follows:

- 1

- 2


- (1) 1 + 8rank(M) − 1 ≤ rankpsd(M) ≤ min{p,q}.


For a proof, as well as a comprehensive comparison between psd rank and several other notions of rank of a nonnegative matrix, see [FGP+15].

The goal of this section is to describe the known bounds on psd ranks of convex sets. As might be expected, the best results we have are for polytopes.

- 4.1. Polytopes. In the case of polytopes, there is a simple lower bound on psd rank. The proof relies on the following technique to increase the psd rank of a matrix by one.


- Lemma 4.3. [GRT13, Proposition 2.6] Suppose M ∈ Rp+×q and rankpsd(M) = k.


M 0 w α

where w ∈ Rq+, α > 0 and 0 is a column of zeros, then rankpsd(M ) = k + 1. Further, the factor associated to the last column of M in any S+k+1-factorization of M has rank one.

If M is extended to M =

- Theorem 4.4. [GRT13, Proposition 3.2] If P ⊂ Rn is a full-dimensional polytope,


then the psd rank of P is at least n + 1. If rankpsd(P) = n + 1, then every S+n+1factorization of the slack matrix of P only uses rank one matrices as factors.

Proof. The proof is by induction on n. If n = 1, then P is a line segment and we may assume that its vertices are p1,p2 and facets are F1,F2 with p1 = F2 and p2 = F1. Hence its slack matrix is a 2 × 2 diagonal matrix with positive diagonal entries. It is not hard to see that rankpsd(SP) = 2 and any S+2 -factorization of it uses only matrices of rank one.

Assume the ﬁrst statement in the theorem holds up to dimension n − 1 and consider a polytope P ⊂ Rn of dimension n. Let F be a facet of P with vertices p1,...,ps, facets f1,...,ft and slack matrix SF. Suppose fi corresponds to facet Fi of P for i = 1,...,t. By induction hypothesis, rankpsd(F) = rankpsd(SF) ≥ n. Let p be a vertex of P not in F and assume that the top left (s+1)×(t+1) submatrix of SP is indexed by p1,...,ps,p in the rows and F1,...,Ft,F in the columns. Then this submatrix of SP, which we will call S F, has the form

SF 0 ∗ α

S F =

with α > 0. By Lemma 4.3, the psd rank of S F is at least n + 1 since the psd rank of SF is at least n. Hence, rankpsd(P) = rankpsd(SP) ≥ n + 1.

Suppose there is now a S+n+1-factorization of SP and therefore of S F. By

- Lemma 4.3 the factor corresponding to the facet F has rank one. Repeating the


procedure for all facets F and all submatrices S F we get that all factors corresponding to the facets of P in this S+n+1-factorization of SP must have rank one. To prove that all factors indexed by the vertices of P also have rank one, we use the fact that the transpose of a slack matrix of P is (up to row scaling) a slack matrix of the polar polytope P◦, concluding the proof.

For an n-dimensional polytope P ⊂ Rn, it is well-known that rank(SP) = n+1, see for instance [GRT13, Lemma 3.1]. Therefore, Theorem 4.4 implies that for a slack matrix SP of a polytope P we have a simple relationship between rank and psd rank, namely rank(SP) ≤ rankpsd(P), as compared to (1). From (1) we also

have that for a polytope P with v vertices and f facets, rankpsd(P) ≤ min{v,f}. In general, it is not possible to bound the psd rank of nonnegative matrices, even slack matrices, by a function in the rank of the matrix. For instance, all slack matrices of polygons have rank three. However, we will see as a consequence of the results in the next subsection that the psd rank of an n-gon grows with n.

In the next section we will see that the lower bound in Theorem 4.4 can be tight for several interesting classes of polytopes. Such polytopes include some 0/1polytopes. However, Bri¨et, Dadush and Pokutta showed that not all 0/1-polytopes can have small psd rank.

- Theorem 4.5. [BDP15] For any n ∈ Z+, there exists U ⊂ {0,1}n such that

rankpsd(conv(U)) = Ω

2n4 (nlog n)14

.

Despite the above result, it is not easy to ﬁnd explicit polytopes with high psd rank. The most striking results we have so far are the following by Lee, Raghavendra and Steurer, which provide super polynomial lower bounds on the psd rank of speciﬁc families of 0/1-polytopes.

- Theorem 4.6. [LRS15] The cut, TSP, and stable set polytopes of n-vertex graphs

have psd rank at least 2n

δ

, for some constant δ > 0.

We saw the stable set polytope of an n-vertex graph before. The cut and TSP polytopes are other examples of polytopes that come from graph optimization problems. The TSP (traveling salesman problem) is the problem of ﬁnding a tour through all vertices of the n-vertex complete graph that minimizes a linear objective function. Each tour can be represented as a 0/1-vector in {0,1}(n

2

) and the TSP polytope is the convex hull of all these tour vectors.

- 4.2. General convex sets. We now examine lower bounds on the psd rank of an arbitrary convex set C ⊂ Rn. The following elegant lower bound was established by Fawzi and Safey El Din.


- Theorem 4.7. [FSED] Suppose C ⊂ Rn is a convex set and d is the minimum degree of a polynomial with real coeﬃcients that vanishes on the boundary of C◦.


√log d.

Then rankpsd(C) ≥

The algebraic degree of a convex set C is the smallest degree of a polynomial with real coeﬃcients that vanishes on the boundary of C. Suppose P is a polytope with v vertices and the origin in its interior. Then P◦ has v facets each corresponding to a linear polynomial li that vanishes on the facet. The polynomial p := πiv=1li vanishes on the boundary of P◦ and has degree v. In fact, the algebraic degree of

√log v. This result is analogous to an observation of Goemans [Goe15] that any polyhedral lift Q of P has at least log v facets. The reason is that every vertex in P is the projection of a face of Q which in turn is the intersection of some set of facets of Q. Therefore,

- P◦ is v. Hence by Theorem 4.7, rankpsd(P) ≥


v ≤ # faces of Q ≤ 2# facets of Q.

Even for polytopes there are likely further factors from combinatorics and topology that can provide stronger lower bounds on psd rank.

The lower bound in Theorem 4.7 is very explicit and simple, but it does not involve n. We now exhibit a simple lower bound that does.

### Proposition 4.8. Let C ⊂ Rn be an n-dimensional convex body. Then rankpsd(C) = Ω(√n).

Proof. Suppose rankpsd(C) = k. Then there exists maps A : ext(C) → S+k and B : ext(C◦) → S+k such that for all (x,y) ∈ ext(C) × ext(C◦),

1 −y

SC((x,y)) = 1 − x,y = (1,x ) ·

(2) = trace(A(x)B(y)).

Deﬁne rank(SC) to be the minimum l such that SC((x,y)) = a x by for ax,by ∈ Rl. Equality of the ﬁrst and third expressions in (2) implies that rank(SC) ≤ n+1. Now consider n+1 aﬃnely independent extreme points x1,...,xn+1 of C and n+1 aﬃnely independent extreme points y1,...,yn+1 of C◦. Then the values of SC restricted to (x,y) as x and y vary in these chosen sets are the entries of the matrix

  

  

1 x 1

1 ··· 1 −y1 ··· −yn+1

. 1 x n+1

which has rank n + 1. Therefore, rank(SC) = n + 1. Equality of the ﬁrst and last expressions in (2) implies that the ﬁrst inequality in (1) holds with M replaced by SC via the same proof, see [GPT13, Proposition 4]. In other words,

- 1

- 2 1 + 8(n + 1) − 1 ≤ rankpsd(SC) = rankpsd(C), and we get the result.


Example 4.9. The spectrahedral lift of Bn2 in Example 1.5 is optimal, and rankpsd(Bn2) = Θ(n).

The lower bounds in Theorem 4.7 and Proposition 4.8 depend solely on the algebraic degree of C◦ and n respectively. A question of interest is how the bound might jointly depend on both these parameters?

While the lower bounds in Theorems 4.4, 4.7 and Proposition 4.8 can be tight, we do not have much understanding of the psd ranks of speciﬁc polytopes or convex sets except in a few cases. For example, Theorem 4.7 implies that the psd rank of polygons must grow to inﬁnity as the number of vertices grows to inﬁnity. However, we do not know if the psd rank of polygons is monotone in the number of vertices.

5. Psd-Minimal Polytopes

Recall from Theorem 4.4 that the psd rank of an n-dimensional polytope is at least n+1. In this section we study those polytopes whose psd rank is exactly this lower bound. Such polytopes are said to be psd-minimal. The key to understanding psd-minimality is another notion of rank of a nonnegative matrix.

Deﬁnition 5.1. A Hadamard square root of a nonnegative real matrix M, denoted as

√

M, is any matrix whose (i,j)-entry is a square root (positive or negative) of the (i,j)-entry of M.

√

M)} be the minimum rank of a Hadamard square root of a nonnegative matrix M. We recall the basic connection between the psd rank of a nonnegative matrix M and rank√ (M) shown in [GRT13, Proposition 2.2].

Let rank√ (M) := min{rank(

### Proposition 5.2. If M is a nonnegative matrix, then rankpsd(M) ≤ rank√ (M). In particular, the psd rank of a 0/1 matrix is at most the rank of the matrix.

√

M be a Hadamard square root of M ∈ Rp+×q of rank r. Then there exist vectors a1,...,ap,b1,...,bq ∈ Rr such that (

Proof. Let

√

M)ij = ai,bj . Therefore, Mij = ai,bj 2 = aiaTi ,bjbTj where the second inner product is the trace inner product for symmetric matrices deﬁned earlier. Hence, rankpsd(M) ≤ r.

Even though rank√ (M) is only an upper bound on rankpsd(M), we cannot ﬁnd S+k-factorizations of M with only rank one factors if k < rank√ (M).

- Lemma 5.3. [GRT13, Lemma 2.4] The smallest k for which a nonnegative real


matrix M admits a S+k-factorization in which all factors are matrices of rank one is k = rank√ (M).

Proof. If k = rank√ (M), then there is a Hadamard square root of M ∈ Rp+×q of rank k and the proof of Proposition 5.2 gives a S+k-factorization of M in which all factors have rank one. On the other hand, if there exist a1aT1 ,...,apaTp ,b1bT1 ,...,bqbTq ∈

S+k such that Mij = aiaTi ,bjbTj = ai,bj 2, then the matrix with (i,j)-entry ai,bj is a Hadamard square root of M of rank at most k.

This brings us to a characterization of psd-minimal polytopes.

- Theorem 5.4. If P ⊂ Rn is a full-dimensional polytope, then rankpsd(P) = n + 1 if and only if rank√ (SP) = n + 1.


Proof. By Proposition 5.2, rankpsd(P) ≤ rank√ (SP). Therefore, if rank√ (SP) = n + 1, then by Theorem 4.4, the psd rank of P is exactly n + 1.

Conversely, suppose rankpsd(P) = n + 1. Then there exists a S+n+1-factorization of SP which, by Theorem 4.4, has all factors of rank one. Thus, by Lemma 5.3, we have rank√ (SP) ≤ n+1. Since rank√ is bounded below by rankpsd, we must have rank√ (SP) = n + 1.

Our next goal is to ﬁnd psd-minimal polytopes. Recall that two polytopes P and

- Q are combinatorially equivalent if they have the same vertex-facet incidence structure. In this section we describe a simple algebraic obstruction to psd-minimality based on the combinatorics of a given polytope, therefore providing an obstruction for all polytopes in the given combinatorial class. Our main tool is a symbolic version of the slack matrix of a polytope.


Deﬁnition 5.5. The symbolic slack matrix of a d-polytope P is the matrix, SP(x), obtained by replacing all positive entries in the slack matrix SP of P with distinct variables x1,...,xt.

Note that two d-polytopes P and Q are in the same combinatorial class if and only if SP(x) = SQ(x) up to permutations of rows and columns, and names of variables. Call a polynomial f ∈ R[x1,...,xt] a monomial if it is of the form f = ±xa where xa = xa

### 1 ···xa

t and a = (a1,...,at) ∈ Nt. We refer to a sum of two distinct monomials as a binomial and to the sum of three distinct monomials as a trinomial. This diﬀers from the usual terminology that allows nontrivial coeﬃcients.

1

t

Lemma 5.6 (Trinomial Obstruction Lemma). Suppose the symbolic slack matrix SP(x) of an n-polytope P has a (n+2)-minor that is a trinomial. Then no polytope in the combinatorial class of P can be psd-minimal.

Proof. Suppose Q is psd-minimal and combinatorially equivalent to P. Hence, we can assume that SP(x) equals SQ(x). By Theorem 5.4 there is some u = (u1,...,ut) ∈ Rt, with no coordinate equal to zero, such that SQ = SP(u21,...,u2t) and rank(SP(u)) = n + 1. Since SQ is the slack matrix of an n-polytope, we have

rank(SP(u21,...,u2t)) = n + 1 = rank(SP(u1,...,ut)).

Now suppose D(x) is a trinomial (n + 2)-minor of SP(x). Up to sign, D(x) has the form xa + xb + xc or xa − xb + xc for some a,b,c ∈ Nt. In either case, it is not possible for D(u21,...,u2t) = D(u1,...,ut) = 0.

## 5.1. Psd-minimal polytopes of dimension up to four.

Proposition 5.7. [GRT13, Theorem 4.7] The psd-minimal polygons are precisely all triangles and quadrilaterals. Proof. Let P be an n-gon where n > 4. Then SP(x) has a submatrix of the form

  

  ,

0 x1 x2 x3 0 0 x4 x5

x6 0 0 x7 x8 x9 0 0

whose determinant is x1x4x7x8 −x2x5x6x9 +x3x4x6x9 up to sign. By Lemma 5.6, no n-gon with n > 4 can be psd-minimal.

Since all triangles are projectively equivalent, by verifying the psd-minimality of one, they are all seen to be psd-minimal. Similarly, for quadrilaterals.

Lemma 5.6 can also be used to classify up to combinatorial equivalence all 3polytopes that are psd-minimal. Using Proposition 5.7, together with the fact that

- faces of psd-minimal polytopes are also psd-minimal, and the invariance of psd rank under polarity, we get that that any 3-polytope P with a vertex of degree larger than four, or a facet that is an n-gon where n > 4, cannot be psd-minimal. Lemma 5.8. If P is a 3-polytope with a vertex of degree four and a quadrilateral
- facet incident to this vertex, then SP(x) contains a trinomial 5-minor.


Proof. Let v be the vertex of degree four incident to facets F1,F2,F3,F4 such that [v1,v] = F1 ∩ F2, [v2,v] = F2 ∩ F3, [v3,v] = F3 ∩ F4 and F4 ∩ F1 are edges of P, where v1, v2 and v3 are vertices of P.

Suppose F4 is quadrilateral. Then F4 has a vertex v4 that is diﬀerent from, and non-adjacent to, v. Therefore, v4 does not lie on F1, F2 or F3. Consider the 5 × 5 submatrix of SP(x) with rows indexed by v,v1,v2,v3,v4 and columns by F1,F2,F3,F4,F where F is a facet not containing v. This matrix has the form





0 0 0 0 x1 0 0 x2 x3 ∗ x4 0 0 x5 ∗ x6 x7 0 0 ∗ x8 x9 x10 0 ∗

,

 

 

and its determinant is a trinomial. Proposition 5.9. The psd-minimal 3-polytopes are combinatorially equivalent to simplices, quadrilateral pyramids, bisimplices, octahedra or their duals.

Proof. Suppose P is a psd-minimal 3-polytope. If P contains only vertices of degree three and triangular facets, then P is a simplex.

For all remaining cases, P must have a vertex of degree four or a quadrilateral facet. Since psd rank is preserved under polarity, we may assume that P has a vertex u of degree four. By Lemma 5.8, the neighborhood of u looks as follows.

- v1
- v2 v3


v4

|u|
|---|


Suppose P has ﬁve vertices. If all edges of P are in the picture, i.e. the picture is a Schlegel diagram of P, then P is a quadrilateral pyramid. Otherwise P has one more edge, and this edge is [v1,v3] or [v2,v4], yielding a bisimplex in either case.

If P has more than ﬁve vertices, then we may assume that P has a vertex v that is a neighbor of v1 diﬀerent from u, v2, v4. Then v1 is a degree four vertex and thus, by Lemma 5.8, all facets of P containing v1 are triangles. This implies that v is a neighbor of v2 and v4. Applying the same logic to either v2 or v4, we get that v is also a neighbor of v3. Since all these vertices now have degree four, there could be no further vertices in P, and so P is an octahedron. Hence P is combinatorially equal to, or dual to, one of the polytopes seen so far.

Call an octahedron in R3, biplanar, if there are two distinct planes each containing four vertices of the octahedron. The complete classiﬁcation of psd-minimal 3-polytopes is as follows.

- Theorem 5.10. [GRT13, Theorem 4.11] The psd-minimal 3-polytopes are precisely simplices, quadrilateral pyramids, bisimplices, biplanar octahedra and their polars.


In dimension four, the classiﬁcation of psd-minimal polytopes becomes quite complicated. The full list consists of 31 combinatorial classes of polytopes including the 11 known projectively unique polytopes in R4. These 11 are combinatorially psd-minimal, meaning that all polytopes in each of their combinatorial classes are psd-minimal. For the remaining 20 classes, there are non-trivial conditions on psdminimality. We refer the reader to [GPRT17] for the result in R4.

Beyond R4, a classiﬁcation of all psd-minimal polytopes looks to be cumbersome. On the other hand, there are families of polytopes of increasing dimension that are all psd-minimal. A polytope P ⊂ Rn is 2-level if for every facet of P, all vertices of P are either on this facet or on a single other parallel translate of the aﬃne span of this facet. Examples of 2-level polytopes include simplices, regular hypercubes, regular cross-polytopes, and hypersimplices. All 2-level polytopes are psd-minimal, but not conversely. For example, the regular bisimplex in R3 is psd-minimal but not 2-level. Recall from Example 1.4 that the stable set polytopes of perfect graphs are psdminimal. In fact, they are also 2-level and it was shown in [GPT10, Corollary 4.11] that all down-closed 0/1-polytopes that are 2-level are in fact stable set polytopes of perfect graphs. On the other hand, [GPT13, Theorem 9] shows that STAB(G) is not psd-minimal if G is not perfect.

![image 5](<2018-thomas-spectrahedral-lifts-convex-sets_images/imageFile5.png>)

![image 6](<2018-thomas-spectrahedral-lifts-convex-sets_images/imageFile6.png>)

![image 7](<2018-thomas-spectrahedral-lifts-convex-sets_images/imageFile7.png>)

Figure 4. The theta bodies of I = (x + 1)x(x − 1)2 and their spectrahedral lifts. The ﬁrst theta body is the entire real line, the second is slightly larger than [−1,1] and the third is exactly [−1,1].

6. Spectrahedral lifts and sum of squares polynomials

We now look at a systematic technique that creates a sequence of nested outer approximations of the convex hull of an algebraic set. These approximations come from projections of spectrahedra and are called theta bodies. In many cases, the theta body at the kth step will equal the closure of the convex hull of the algebraic set and hence the spectrahedron that it was a projection of, is a lift of this convex set. We examine how this type of lift ﬁts into our general picture.

Let I = p1,...,ps ⊂ R[x] := R[x1,...,xn] be a polynomial ideal and let VR(I) ⊂ Rn be the real points in its variety. Then the closure of the convex hull of VR(I), C := conv(VR(I)), is a closed convex semialgebraic set. Since we are only interested in the convex hull of VR(I), and the convex hull is deﬁned by its extreme points, we may assume without loss of generality that I is the largest ideal that vanishes on the extreme points of C.

Recall that C is the intersection of all half spaces containing VR(I). Each half space is expressed as l(x) ≥ 0 for some linear polynomial l ∈ R[x] that is nonnegative on VR(I). A linear polynomial l is nonnegative on VR(I) if there exists polynomials hi ∈ R[x] such that l − h2i ∈ I. In this case we say that l is a sum of squares (sos) mod I, and if the degree of each hi is at most k, then we say that l is k-sos mod I. Deﬁne the kth theta body of I to be the set

THk(I) := {x ∈ Rn : l(x) ≥ 0 ∀ l linear and k-sos mod I}.

Note that all theta bodies are closed convex semialgebraic sets and they form a series of nested outer approximations of C since

THi(I) ⊇ THi+1(I) ⊇ C for all i ≥ 1.

We say that I is THk-exact if THk(I) = C. The terminology is inspired by Lov´sz’s theta body TH(G) from Example 1.4 which is precisely TH1(IG) of the ideal

IG = x2i − xi, ∀i = 1,...,n + xixj, ∀{i,j} ∈ E(G) . In our terminology, IG is TH1-exact when G is a perfect graph.

Theta bodies of a general polynomial ideal I ⊂ R[x] were deﬁned in [GPT10], and it was shown there that I is THk-exact if and only if C admits a speciﬁc type of spectrahedral lift. This lift has size equal to the number of monomials in R[x] of

degree at most k. Let [x]k denote the vector of all monomials of degree at most k in R[x]. When THk(I) = C, Theorem 2.3 promises two maps A and B that factorize the slack operator of C. These operators are very special.

- Theorem 6.1. [GPT13, Theorem 11] The slack operator of C = conv(VR(I)) has


a factorization in which A(x) = [x]k[x] k if and only if C = THk(I). Further, the map B sends each linear functional l(x) corresponding to an extreme point of the

polar of C to a psd matrix Ql such that l(x) − x Qlx ∈ I certifying that l(x) is nonnegative on VR(I).

In fact, each theta body is the projection of a spectrahedron. Figure 4 shows the theta bodies and their spectrahedral lifts of the ideal I = (x + 1)x(x − 1)2 . In this case, C = [−1,1] ⊂ R.

While theta bodies oﬀer a systematic method to sometimes construct a spectrahedral lift of C, they may not oﬀer the most eﬃcient lift of this set. So an immediate question is whether there might be radically diﬀerent types of spectrahedral lifts for

- C. Since the projection of a spectrahedron is necessarily convex and semialgebraic, a set C can have a spectrahedral lift only if it is convex and semialgebraic. So a second question is whether every convex semialgebraic set has a spectrahedral lift. This question gained prominence from [Nem07], and Helton and Nie showed that indeed a compact convex semialgebraic set has a spectrahedral lift if its boundary is suﬃciently smooth and has positive curvature. They then conjectured that every convex semialgebraic set has a spectrahedral lift, see [HN09] and [HN10]. This conjecture was very recently disproved by Scheiderer who exhibited many explicit counter-examples [Sch18b]. All these sets therefore have inﬁnite psd rank.


Recall that a morphism φ : X → Y between two aﬃne real varieties creates a ring homomorphism φ∗ : R[Y ] → R[X] between their coordinate rings. By a real variety we mean a variety deﬁned by polynomials with real coeﬃcients. Let XR denote the R-points of X.

- Theorem 6.2. [Sch18b, Theorem 3.14] Let S ⊂ Rn be a semialgebraic set and let C be the closure of its convex hull. Then C has a spectrahedral lift if and only if there is a morphism φ : X → An of aﬃne real varieties and a ﬁnite-dimensional R-linear subspace U in the coordinate ring R[X] such that


- (1) S ⊂ φ(XR),
- (2) for every linear polynomial l ∈ R[x] that is nonnegative on S, the element φ∗(l) of R[X] is a sum of squares of elements in U.


This theorem oﬀers a set of necessary and suﬃcient conditions for the existence of a spectrahedral lift of the convex hull of a semialgebraic set by working through an intermediate variety X. The setting is more general than that in Theorem 6.1 where we only considered convex hulls of algebraic sets. Regardless, the spirit of condition (2) is that the theta body method (or more generally, Lasserre’s method [Las01]) is essentially universal with the subspace U ⊆ R[X] playing the role of degree bounds on the sos nonnegativity certiﬁcates that were required for THkexactness. Theorem 6.2 provides counterexamples to the Helton-Nie conjecture.

Theorem 6.3. [Sch18b, Theorem 4.23] Let S ⊂ Rn be any semialgebraic set with dim(S) ≥ 2. Then for some positive integer k, there exists a polynomial map φ : S → Rk such that the closed convex hull of φ(S) ⊂ Rk is not the linear image of a spectrahedron.

These results show, among other examples, that there are high enough Veronese embeddings of semialgebraic sets that cannot be the projections of spectrahedra.

Corollary 6.4. [Sch18b, Corollary 4.24] Let n,d be positive integers with n ≥ 3,d ≥ 4 or n = 2 and d ≥ 6. Let m1,...,mN be the non-constant monomials in R[x] of degree at most d. Then for any semialgebraic set S ⊆ Rn with non-empty interior, the closed convex hull of

m(S) := {(m1(s),...,mN(s)) : s ∈ S} ⊂ RN is not the linear image of a spectrahedron.

In contrast, Scheiderer had previously shown that all convex semialgebraic sets in R2 have spectrahedral lifts [Sch18a], thus proving the Helton-Nie conjecture in the plane. The current smallest counterexamples to the Helton-Nie conjecture are in R11. Is it possible that there is a counterexample in R3?

7. Notes

There are many further results on spectrahedral lifts of convex sets beyond those mentioned here. An important topic that has been left out is that of symmetric spectrahedral lifts which are lifts that respect the symmetries of the convex set. Due to the symmetry requirement, such lifts are necessarily of size at least as large as the psd rank of the convex set. On the other hand, the symmetry restriction provides more tools to study such lifts and there are many beautiful results in this area, see [FSP17], [FSP15], [FSP16].

Many speciﬁc examples of spectrahedral lifts of convex sets exist, and several of them have signiﬁcance in applications. An easy general source is the book [BPT13]. In particular, Chapter 6 is dedicated to sdp representability of convex sets. This book includes a number of further topics in the area of Convex Algebraic Geometry.

Acknowledgments. I am indebted to all my collaborators on the projects that contributed to this paper. I thank Pablo Parrilo for the construction in Example 1.5 and for several useful conversations. I also thank Hamza Fawzi and Jo˜o Gouveia for comments on this paper, and Hamza for pointing out the bound in Proposition 4.8. Claus Scheiderer and Daniel Plaumann were very helpful with the content of Section 6.

References

[BDP15] J. Brie¨t, D. Dadush, and S. Pokutta. On the existence of 0/1 polytopes with high semideﬁnite extension complexity. Math. Program., 153(1, Ser. B):179–199, 2015.

[BPT13] G Blekherman, P. A. Parrilo, and R.R. Thomas. Semideﬁnite optimization. In Semideﬁnite optimization and convex algebraic geometry, volume 13 of MOS-SIAM Ser. Optim., pages 3–46. SIAM, Philadelphia, PA, 2013.

[BTN01] A. Ben-Tal and A. Nemirovski. Lectures on modern convex optimization. MPS/SIAM Series on Optimization. Society for Industrial and Applied Mathematics (SIAM), Philadelphia, PA; Mathematical Programming Society (MPS), Philadelphia, PA, 2001. Analysis, algorithms, and engineering applications.

[CCZ10] M. Conforti, G. Cornue´jols, and G. Zambelli. Extended formulations in combinatorial optimization. 4OR, 8(1):1–48, 2010. [FGP+15] H. Fawzi, J. Gouveia, P. A. Parrilo, R. Z. Robinson, and R. R. Thomas. Positive semideﬁnite rank. Math. Program., 153(1, Ser. B):133–177, 2015.

[FMP+12] S. Fiorini, S. Massar, S. Pokutta, H. R. Tiwary, and R. de Wolf. Linear vs. semideﬁnite extended formulations: exponential separation and strong lower bounds. In STOC’12—Proceedings of the 2012 ACM Symposium on Theory of Computing, pages 95–106. ACM, New York, 2012.

[FSED] H. Fawzi and M. Safey El Din. A lower bound on the positive semideﬁnite rank of convex bodies. arXiv:1705.06996.

- [FSP15] H. Fawzi, J. Saunderson, and P. A. Parrilo. Equivariant semideﬁnite lifts and sum-ofsquares hierarchies. SIAM J. Optim., 25(4):2212–2243, 2015.
- [FSP16] H. Fawzi, J. Saunderson, and P. A. Parrilo. Sparse sums of squares on ﬁnite abelian groups and improved semideﬁnite lifts. Math. Program., 160(1-2, Ser. A):149–191, 2016.
- [FSP17] H. Fawzi, J. Saunderson, and P. A. Parrilo. Equivariant semideﬁnite lifts of regular polygons. Math. Oper. Res., 42(2):472–494, 2017.


[Goe15] M. X. Goemans. Smallest compact formulation for the permutahedron. Math. Program., 153(1, Ser. B):5–11, 2015.

[GPRT17] J. Gouveia, K. Pashkovich, R. Z. Robinson, and R. R. Thomas. Four-dimensional polytopes of minimum positive semideﬁnite rank. J. Combin. Theory Ser. A, 145:184– 226, 2017.

[GPT10] J. Gouveia, P. A. Parrilo, and R. R. Thomas. Theta bodies for polynomial ideals. SIAM J. Optim., 20(4):2097–2118, 2010. [GPT13] J. Gouveia, P. A. Parrilo, and R. R. Thomas. Lifts of convex sets and cone factorizations. Math. Oper. Res., 38(2):248–264, 2013. [GRT13] J. Gouveia, R. Z. Robinson, and R. R. Thomas. Polytopes of minimum positive semideﬁnite rank. Discrete Comput. Geom., 50(3):679–699, 2013.

- [HN09] J. W. Helton and J. Nie. Suﬃcient and necessary conditions for semideﬁnite representability of convex hulls and sets. SIAM J. Optim., 20(2):759–791, 2009.
- [HN10] J. W. Helton and J. Nie. Semideﬁnite representation of convex sets. Math. Program., 122(1, Ser. A):21–64, 2010.


[Las01] J. B. Lasserre. Global optimization with polynomials and the problem of moments. SIAM J. Optim., 11(3):796–817, 2000/01. [Lov79] L. Lova´sz. On the Shannon capacity of a graph. IEEE Trans. Inform. Theory, 25(1):1– 7, 1979.

[LRS15] J. R. Lee, P. Raghavendra, and D. Steurer. Lower bounds on the size of semideﬁnite programming relaxations. In STOC’15—Proceedings of the 2015 ACM Symposium on Theory of Computing, pages 567–576. ACM, New York, 2015.

[Nem07] A. Nemirovski. Advances in convex optimization: conic programming. In International Congress of Mathematicians. Vol. I, pages 413–444. Eur. Math. Soc., Zu¨rich, 2007.

- [Sch18a] C. Scheiderer. Semideﬁnite Representation for Convex Hulls of Real Algebraic Curves. SIAM J. Appl. Algebra Geom., 2(1):1–25, 2018.
- [Sch18b] C. Scheiderer. Spectrahedral Shadows. SIAM J. Appl. Algebra Geom., 2(1):26–44, 2018.


[Yan91] M. Yannakakis. Expressing combinatorial optimization problems by linear programs. J. Comput. System Sci., 43(3):441–466, 1991. [Zie95] G.M. Ziegler. Lectures on Polytopes, volume 152 of Graduate Texts in Mathematics. Springer-Verlag, New York, 1995.

Department of Mathematics, University of Washington, Box 354350, Seattle, WA 98195, USA

E-mail address: rrthomas@uw.edu

