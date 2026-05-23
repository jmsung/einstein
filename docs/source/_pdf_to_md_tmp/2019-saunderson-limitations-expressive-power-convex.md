arXiv:1902.06401v2[math.OC]5Aug2019

Limitations on the expressive power of convex cones without long chains of faces

James Saunderson∗ August 6, 2019

Abstract

A convex optimization problem in conic form involves minimizing a linear functional over the intersection of a convex cone and an aﬃne subspace. In some cases, it is possible to replace a conic formulation using a certain cone, with a ‘lifted’ conic formulation using another cone that is higher-dimensional, but simpler, in some sense. One situation in which this can be computationally advantageous is when the higher-dimensional cone is a Cartesian product of many ‘low-complexity’ cones, such as second-order cones, or small positive semideﬁnite cones.

This paper studies obstructions to a convex cone having a lifted representation with such a product structure. The main result says that whenever a convex cone has a certain neighborliness property, then it does not have a lifted representation using a ﬁnite product of cones, each of which has only short chains of faces. This is a generalization of recent work of Averkov (‘Optimal size of linear matrix inequalities in semideﬁnite approaches to polynomial optimization’, SIAM J. Appl. Alg. Geom., Vol. 3, No. 1, 128–151, 2019) which considers only lifted representations using products of positive semideﬁnite cones of bounded size. Among the consequences of the main result is that various cones related to nonnegative polynomials do not have lifted representations using products of ‘low-complexity’ cones, such as smooth cones, the exponential cone, and cones deﬁned by hyperbolic polynomials of low degree.

- 1 Introduction A conic optimization problem has the form


minimizex c,x subject to A(x) = b, x ∈ K (1)

where K ⊆ Rn is a closed convex cone, A : Rn → Rm is a linear map, and c ∈ Rn and b ∈ Rm. Diﬀerent choices of convex cones in Eq. (1) lead to diﬀerent classes of convex optimization problems. For instance, if K = Rn+ is a nonnegative orthant, we obtain a linear program; if K is a ﬁnite Cartesian product of second-order cones Q = {(x,y,z) ∈ R3 : x2 + y2 ≤ z}, we obtain a secondorder cone program; if K = S+k is the cone of k × k positive semideﬁnite matrices, we obtain a semideﬁnite program. Computationally, conic optimization problems are often easier to solve if K = K1 ×··· ×Km where each of the Ki are convex cones of ‘low-complexity’. One reason for this is that basic algorithmic primitives related to the cone, such as computing the Euclidean projection of a point onto the cone, are separable across the factors and so are easily parallelizable.

![image 1](<2019-saunderson-limitations-expressive-power-convex_images/imageFile1.png>)

It is natural, then, to try to understand which families of convex optimization problems can be expressed in conic form with respect to a ﬁnite Cartesian product of ‘low-complexity’ cones.

![image 2](<2019-saunderson-limitations-expressive-power-convex_images/imageFile2.png>)

∗Department of Electrical and Computer Systems Engineering, Monash University, VIC 3800, Australia. Email: james.saunderson@monash.edu

The question can be phrased in geometric terms by using the notion of a lifted representation of a convex cone.

- Deﬁnition 1.1 ([GPT13]). If C ⊆ Rn and K ⊆ Rd are closed convex cones then C has a K-lift if C = π(K ∩ L) where π : Rd → Rn is a linear map and L ⊆ Rd is a linear subspace.


If C has a K-lift, then any conic optimization problem using the cone C can be reformulated as a conic optimization problem using K. As such we are interested in understanding when a convex cone C has a K-lift where K is a Cartesian product of ‘low-complexity’ cones. There are many examples where such reformulations are possible.

- • If C is the set of symmetric positive semideﬁnite matrices that are sparse with respect to a

chordal graph, then C has a S+k1×···×S+kℓ-lift where the ki are the sizes of the maximal cliques in the graph [AHMR88, GJSW84]. This observation can be exploited to yield signiﬁcant computational savings for semideﬁnite programs with sparse data (see, e.g., [VA15]).

- • The cone of scaled diagonally dominant matrices [AM19], and the cone of sums of nonnegative

circuit polynomials [IDW16], both have second-order cone lifts, or equivalently, (S+2 )m-lifts for some m.1 These have been used to give more tractable certiﬁcates of nonnegativity for multivariate polynomials than those given by general sums of squares.

- • Ben-Tal and Nemirovski’s book [BTN01] has many nontrivial examples of convex sets that have second-order cone lifts.
- • Cones of sums of arithmetic-mean geometric-mean functions (SAGE functions) [CS16], used to certify nonnegativity of signomial functions, have lifted representations using a product of three-dimensional relative entropy cones (or, equivalently, exponential cones).


This paper, on the other hand, explores limitations on the expressive power of lifts using ﬁnite products of ‘low-complexity’ cones. Until recently, the only result in this direction was the fact that a convex cone has an Rm+-lift for some ﬁnite m if and only if it is a polyhedral cone.

In a breakthrough paper, Fawzi [Faw18] studied the expressive power of second-order cone programming. Among his results is that S+3 has no second-order cone lift. Fawzi identiﬁed the importance of certain neighborliness properties of the positive semideﬁnite cone as an obstruction to constructing second-order cone lifts. He also introduced a combinatorial approach to establish results of this type, via Tura´n’s theorem.

Averkov [Ave19] subsequently signiﬁcantly extended Fawzi’s approach. He introduced the semideﬁnite extension degree of a convex cone—the smallest k such that C has an (S+k)m-lift for some positive integer m. Averkov established that convex cones with a certain k-neighborliness property (made precise in Deﬁnition 1.2) have semideﬁnite extension degree at least k + 1. To prove this result, Averkov used Ramsey’s theorem for uniform hypergraphs to provide the key combinatorial obstruction.

The present work moves beyond studying lifts using products of positive semideﬁnite cones of bounded size. Instead, we consider a notion of ‘low-complexity’ that just depends on the face lattice of a cone. In particular, we consider the expressive power of K-lifts where K is a ﬁnite product of cones, each of which has only short chains of faces. The main result (Theorem 1.4) gives an explicit obstruction to a cone having a lifted representation of this type. The obstruction is the same as that considered by Averkov, and is based on the existence of arbitrarily large ﬁnite collections of extreme rays of the cone that satisfy a certain neighborliness property (see Deﬁnition 1.2).

![image 3](<2019-saunderson-limitations-expressive-power-convex_images/imageFile3.png>)

1The fact that sums of nonnegative circuit polynomials have (S+2 )m-lifts was established by Averkov [Ave19].

## 1.1 Chains of faces, neighborliness, and our main result

- 1.1.1 Chains of faces

If K is a closed convex cone, then a subset F ⊆ K is a face if x,y ∈ K and αx + (1 − α)y ∈ F for some α ∈ (0,1) implies that x,y ∈ F. Note that the empty set is always a face. A collection of faces F1,F2,... ,Fℓ ⊆ K is a chain of length ℓ if F1 F2 ··· Fℓ. For a convex cone K, deﬁne

ℓ(K) = maximum length of a chain of nonempty faces of K.

This is well-deﬁned because ℓ(K) ≤ dim(K) + 1 where dim(K) is the dimension of the span of K (see Section 2.2). Crucially, ℓ(·) is monotone, in the sense that if F is a face of K and F K then ℓ(F) < ℓ(K).

This quantity appears naturally in the study of facial reduction algorithms for conic optimization problems (see, e.g., [Pat13, WM13]), and has been used to give an upper bound on the Carathe´odory number of a closed, pointed convex cone [IL17]. In this paper we will think of cones without any long chains of faces as being of low complexity. Indeed ℓ(K) = 1 if and only if K is a linear subspace, and ℓ(K) = 2 if and only if K is a closed halfspace.

- 1.1.2 Neighborliness properties


In Deﬁnition 1.2, to follow, we describe the cones for which we can show the non-existence of lifts. This is the same class of convex cones that is considered by Averkov [Ave19]. In the following deﬁnition, and throughout, we ﬁx an inner product  ·,·  on Rn and denote the associated norm by · . If C ⊆ Rn is a set, then C∗ = {f : f,x ≥ 0 for all x ∈ C} is the corresponding dual cone. A closed convex cone C ⊆ Rn is pointed if C ∩ (−C) = {0} and full-dimensional if span(C) = Rn. A convex cone is proper if it is closed, pointed, and full-dimensional. For a convex cone C ⊆ Rn, we denote the set of extreme rays of C by Ext(C) and the set of normalized extreme rays by ext(C) := {v ∈ Rn : v = 1, R+v ∈ Ext(C)}.

- Deﬁnition 1.2. Let C be a proper convex cone. If V ⊆ ext(C) is a subset of normalized extreme rays of C, then C is k-neighborly with respect to V if for every k-element subset W ⊂ V , there is some linear functional fW ∈ C∗ such that fW,v > 0 if v ∈ V \ W and fW,v = 0 if v ∈ W.


In this paper we will be particularly interested in the case where C is k-neighborly with respect to arbitrarily large ﬁnite subsets of normalized extreme rays of C. Example 1.3 (Positive semideﬁnite cone). The cone of (k + 1) × (k + 1) positive semideﬁnite symmetric matrices is k-neighborly with respect to

V = {viviT/ vi 2 : i ∈ N} where vi := (1,i,i2,... ,ik).

To see why this is true, for each set W of k natural numbers, deﬁne the non-negative polynomial pW and the vector c(W) ∈ Rk+1 such that

2

= 

c(W)jtj

2

k

= tr(c(W)c(W)T vtvtT).

(t − i)

pW(t) =





i∈W

j=0

Observe that pW(t) vanishes if and only if t ∈ W. Consequently c(W)c(W)T ∈ (S+k+1)∗ = S+k+1 vanishes on viviT if and only if i ∈ W.

We are now in a position to state our main result.

Theorem 1.4. Let C be a proper convex cone, let m be a positive integer, and let K1,... ,Km be closed convex cones with ℓ(Ki) ≤ k +1 for each i = 1,2,... ,m. Suppose that, for each N ∈ N there exists a subset VN ⊆ ext(C) such that C is k-neighborly with respect to VN and |VN| ≥ N. Then C does not have a K1 × ··· × Km-lift.

We remark that if a proper convex cone C is k-neighborly with respect to an inﬁnite set V ⊆ ext(C), then C is k-neighborly with respect to any ﬁnite subset of V , and so the neighborliness hypothesis of Theorem 1.4 holds.

Section 2.1 gives examples of convex cones that are k-neighborly with respect to arbitrarily large ﬁnite sets of normalized extreme rays. Section 2.2 gives examples of convex cones with only short chains of faces. Combining these allows us to specialize Theorem 1.4 to produce a range of irrepresentability results. The following statements about the non-existence of lifts of certain positive semideﬁnite cones are examples of the kind of results that follow from Theorem 1.4:

- • S+3 has no K-lift where K is a ﬁnite Cartesian product of smooth convex cones (such as second-order cones);
- • S+4 has no K-lift where K is a ﬁnite Cartesian product of three-dimensional convex cones (such as cones over the epigraphs of univariate convex functions);
- • S+k+1 has no (S+k)m-lift where m is a positive integer, a result from [Ave19];
- • S+k+1 has no K-lift where K is a hyperbolicity cone corresponding to a hyperbolic polynomial with all its irreducible factors having degree at most k.


Our proof of Theorem 1.4 follows Averkov’s approach to lower-bounding the semideﬁnite extension degree. In fact, the underlying combinatorial part of the argument is exactly the same. The main new contribution is that all of the algebraic structure of the positive semideﬁnite cone used by Averkov can be done away with, and replaced with basic properties of face lattice of convex cones.

## 1.2 Notation

For a convex cone C, let relint(C) denote the relative interior of C. If S ⊆ Rn let cone(S) be the cone generated by S, i.e., the collection of all non-negative combinations of elements of S. If n is a positive integer let [n] := {1,2,... ,n}. If S is a ﬁnite set let Sn be the collection of n-element subsets of S. Other notation, needed only for the proofs, will be introduced in Section 3.

## 1.3 Outline

The rest of the paper is structured as follows. In Section 2 we discuss the consequences of Theorem 1.4. We state a number of examples (many from Averkov’s work) of cones that are k-neighborly with respect to an inﬁnite set. We then give bounds on the length of chains of faces for a number of families of convex cones. From the discussion one can extract many irrepresentability results. For the sake of brevity we will not exhaustively state such results. In Section 3 we brieﬂy introduce some of the technical tools used in the proof of the main result. In Section 4 we generalize the key technical results of [Ave19] to our setting, prove these results, and consequently complete the proof of Theorem 1.4.

# 2 Consequences of the main result

To appreciate the consequences of our main result, this section is devoted to giving examples of convex cones to which Theorem 1.4 can be applied. In Section 2.1 we give examples of convex cones that are k-neighborly (for some k) with respect to arbitrarily large ﬁnite sets of normalized extreme rays. These are the convex cones that can be used as C in Theorem 1.4. In Section 2.2 we give upper bounds on ℓ(·), for many convex cones. These are the cones that can be used as the Ki in Theorem 1.4.

## 2.1 Cones k-neighborly with respect to arbitrarily large ﬁnite sets

- 2.1.1 Non-polyhedral cones

If C is a proper, non-polyhedral cone then it has inﬁnitely many extreme rays. Moreover, it has inﬁnitely many exposed extreme rays (extreme rays that can be obtained as the intersection of C with a hyperplane), because exposed extreme rays are dense in the set of all extreme rays by Straszewicz’s theorem [Roc15, Theorem 18.6]. It follows that C is 1-neighborly with respect to the (inﬁnite) set of normalized exposed extreme rays.

- 2.1.2 Cones related to nonnegative polynomials and sums of squares


A number of interesting examples are special cases of the following result, which is essentially [Ave19, Corollary 3].

- Proposition 2.1. Let X ⊆ Rn have nonempty interior. Deﬁne


Pn,2d(X) := {polynomials p of degree ≤ 2d such that p(x) ≥ 0 for all x ∈ X} Σn,2d := {polynomials of degree ≤ 2d in n variables that are sums of squares}.

Let C be a closed convex cone that satisﬁes Pn,2d(X)∗ ⊆ C ⊆ Σ∗n,2d. Then for each N ∈ N there is a set V ⊆ ext(C) with |V | ≥ N such that C is n+dd − 1 -neighborly with respect V .

From Proposition 2.1 we can construct many examples. Perhaps the simplest, which are also discussed in Averkov’s paper, are the following:

- • The (self-dual) cone of k×k positive semideﬁnite matrices S+k is linearly isomorphic to Σk−1,2, since a quadratic polynomial in k − 1 variables is nonnegative if and only if it has the form

q(x) = 1 xT Q

1 x

where Q is positive semideﬁnite. It then follows from Proposition 2.1 that S+k is (k − 1)neighborly with respect to arbitrarily large ﬁnite subsets of normalized extreme rays. We

gave a direct argument that S+k is (k − 1)-neighborly with respect to an inﬁnite subset of extreme rays in Example 1.3.

- • The dual of the cone of univariate nonnegative polynomials of degree at most 2d, i.e., P1,2d(R)∗ is d-neighborly with respect to arbitrarily large ﬁnite subsets of normalized extreme rays.


- 2.1.3 Cones over k-neighborly manifolds

If M ⊆ Rm is a smooth embedded manifold, Kalai and Widgerson [KW08] say that M is kneighborly if, for every subset X ⊆ M of cardinality k, there exists a linear functional f, and a real number b, such that f,x = b for all x ∈ X and f,x > b for all x ∈ M\X. If M is a k-neighborly manifold of positive dimension, then cone(M × {1}) ⊆ Rm+1 is k-neighborly with respect to the inﬁnite set {v/ v : v ∈ M × {1}} of normalized extreme rays.

- 2.1.4 Cones with neighborly faces and derivative relaxations of S+k


Suppose that C is a convex cone and F is an exposed face of C. One can show that if F is kneighborly with respect to V ⊆ ext(F) ⊆ ext(C) then C is also k-neighborly with respect to V . This simple observation gives some interesting additional examples beyond cones related to nonnegative polynomials. We describe just one example here, which is an example of a hyperbolicity cone (a class of convex cones we discuss more at the end of Section 2.2).

The cone of k × k positive semideﬁnite matrices can be described as

S+k = {X ∈ Sk : E1,k(X) ≥ 0, E2,k(X) ≥ 0, ... , Ek,k(X) ≥ 0}

where Eℓ,k(X) is the sum of the ℓ × ℓ principal minors of the k × k symmetric matrix X (see, e.g., [Ren06]). For 0 ≤ ℓ ≤ k − 1 one can deﬁne a cone (which turns out to be convex) by keeping only the ﬁrst k − ℓ of these inequalities:

S+k,(ℓ) = {X ∈ Sk : E1,k(X) ≥ 0, ... , Ek−ℓ,k(X) ≥ 0}.

These are often called the derivative relaxations or Renegar derivatives of the positive semideﬁnite cone. For the connection to derivatives, and the fact that these are convex cones, see [Ren06].

Consider the intersection of S+k,(ℓ) with the subspace L of symmetric matrices of the form Y0 00 where only the top (k − ℓ) × (k − ℓ) block is nonzero. Restricted to this subspace we have that

Ep,k

Y 0 0 0

=

Ep,k−ℓ(Y ) if p ≤ k − ℓ 0 otherwise.

As such S+k,(ℓ) ∩ L is a face of S+k,(ℓ) that is linearly isomorphic to S+k−ℓ. Since S+k−ℓ is (k − ℓ − 1)neighborly with respect to an inﬁnite set of normalized extreme rays, it follows that S+k,(ℓ) has the same property.

## 2.2 Cones with only short chains of faces

The innovation of Theorem 1.4 is that it rules out K-lifts where K is a ﬁnite Cartesian product of cones, each of which has only short chains of faces. In this section we now give a number of examples of cones K that have only short chains of faces.

- 2.2.1 Rays


The ray R+ has two nonempty faces: {0} and R+ itself. It follows that ℓ(R+) = 2. From Theorem 1.4 we recover the fact that any cone that is 1-neighborly with respect to an inﬁnite set of normalized extreme rays (i.e., a cone with inﬁnitely many exposed extreme rays) cannot have a Rm+-lift.

- 2.2.2 Smooth cones

Following [LP18], for instance, we call a pointed closed convex cone K smooth if its only non-empty faces are {0} or K or its extreme rays. As such, any smooth cone has ℓ(K) ≤ 3. For example, the second-order cone

Qn+1 = {(x0,... ,xn) ∈ Rn+1 : x21 + ··· + x2n ≤ x0}

![image 4](<2019-saunderson-limitations-expressive-power-convex_images/imageFile4.png>)

is a smooth cone. From Theorem 1.4 we can conclude that any cone 2-neighborly with respect to arbitrarily large ﬁnite sets of normalized extreme rays does not have a lift using a ﬁnite product of smooth cones.

- 2.2.3 Low-dimensional cones

Since the dimension strictly increases along chains of faces [Roc15, Corollary 18.1.3], we always have that

ℓ(K) ≤ dim(K) + 1.

For example, the exponential cone K = cl{(x,t,y) ∈ R2 × R++ : yex/y ≤ t} satisﬁes ℓ(K) ≤ 3 + 1. More generally, if K = cl{(x,t,y) ∈ R2 × R++ : y g(x/y) ≤ t} is the closure of the cone over the epigraph of any univariate convex function g, then ℓ(K) ≤ 3+1. From Theorem 1.4 we can conclude that any cone k-neighborly with respect to arbitrarily large ﬁnite sets of normalized extreme rays does not have a lift using a ﬁnite product of k-dimensional cones.

- 2.2.4 The positive semideﬁnite cone

The rank of a symmetric matrix is constant on the relative interior of faces of the positive semidefinite cone. Moreover, the rank function strictly increases on chains of faces. As such,

ℓ(S+k) ≤ k + 1.

On the other hand, it is easy to construct a chain of non-empty faces of length k + 1, so we have that ℓ(S+k ) = k+1. Theorem 1.4, in this context, recovers Averkov’s result that if C is k-neighborly with respect to arbitrarily large ﬁnite sets of normalized extreme rays then C has no (S+k )m-lift.

- 2.2.5 Hyperbolicity cones


A class of convex cones that generalizes the positive semideﬁnite cone are hyperbolicity cones. A homogeneous polynomial p of degree d in n variables with real coeﬃcients is called hyperbolic with respect to e ∈ Rn if p(e) > 0 and, for all x ∈ Rn, the univariate polynomial t  → p(te − x) has only real roots. We call these real roots the hyperbolic eigenvalues of x. There is an associated closed cone

Λ+(p,e) = {x ∈ Rn : all hyperbolic eigenvalues of x are nonnegative}

which is convex, a result of Ga˚rding [Ga˚r59]. As an example, the determinant restricted to symmetric matrices is hyperbolic with respect to the identity matrix, and the associated hyperbolicity cone is the positive semideﬁnite cone.

With a hyperbolic polynomial, one can associate a rank function by deﬁning rankp,e(x) = # non-zero hyperbolic eigenvalues of x.

Renegar [Ren06, Theorem 26] has showed that if F is a face of a hyperbolicity cone Λ+(p,e) then every point in the relative interior of F has the same hyperbolic rank, and every point in the boundary of F has strictly smaller rank. Consequently, there is a well deﬁned notion of the hyperbolic rank of a face, and the hyperbolic rank function is strictly increasing along chains of faces. Since any point in the relative interior of the hyperbolicity cone has rank d = degree(p), we have the bound

ℓ(Λ+(p,e)) ≤ d + 1. The following gives a natural suﬃcient condition under which this bound is tight.

- Proposition 2.2. Suppose that p is homogeneous of degree d, hyperbolic with respect to e, and the associated hyperbolicity cone Λ+(p,e) is pointed. If all of the extreme rays of Λ+(p,e) have hyperbolic rank one then ℓ(Λ+(p,e)) = d + 1.


Proof. Let x1,x2,... ,xκ be a collection of generators of extreme rays such that x1 +x2 +···+xκ is in the relative interior of Λ+(p,e). Since the Carathe´odory number of Λ+(p,e) is bounded above by ℓ(Λ+(p,e)) − 1 [IL17], it follows that we can choose κ ≤ ℓ(Λ+(p,e)) − 1. Since the hyperbolic rank function is a nonnegative submodular function on the face lattice of the hyperbolicity cone [AB18], the hyperbolic rank is subadditive. Then

ℓ(Λ+(p,e)) − 1 ≤ d = rankp,e

κ

xi ≤

i=1

κ

rankp,e(xi) = κ ≤ ℓ(Λ+(p,e)) − 1.

i=1

![image 5](<2019-saunderson-limitations-expressive-power-convex_images/imageFile5.png>)

![image 6](<2019-saunderson-limitations-expressive-power-convex_images/imageFile6.png>)

![image 7](<2019-saunderson-limitations-expressive-power-convex_images/imageFile7.png>)

![image 8](<2019-saunderson-limitations-expressive-power-convex_images/imageFile8.png>)

Symmetric cones2 are examples of hyperbolicity cones with p being the determinant associated with the appropriate Euclidean Jordan algebra. For these cones, all of the extreme rays have hyperbolic rank one. As such Proposition 2.2 generalizes [IL17, Theorem 14]. It also applies to spectrahedra with all rank one extreme rays which, in the real symmetric case, have been classiﬁed by Blekherman, Sinn, and Velasco [BSV17].

We can obtain a more reﬁned bound in cases where all the extreme rays have rank at least r, and so all nonzero faces have rank at least r. Then

ℓ(Λ+(p,e)) ≤ d − r + 2

since, in that case, there are no faces of rank 1,2,... ,r−1. For hyperbolicity cones corresponding to strictly hyperbolic polynomials [Nui69] (which give rise to smooth hyperbolicity cones), all extreme rays have rank d − 1 so this bound becomes ℓ(Λ+(p,e)) ≤ 3.

A hyperbolic polynomial is irreducible if it cannot be factored as a product of polynomials of lower degree. If p is hyperbolic with respect to e and is reducible, we can write p = pm1 1 ··· pmn n where the pi are the irreducible factors of p and the mi are positive integers. It is straightforward to see that the pi are also hyperbolic with respect to e. The hyperbolicity cone corresponding to p is the intersection of the cones corresponding to the pi. As such,

Λ+(p,e) = {x : (x,x,... ,x) ∈ Λ+(p1,e) × ··· × Λ+(pn,e)} gives a Λ+(p1,e) × ··· × Λ+(pn,e)-lift of Λ+(p,e).

The following corollary of Theorem 1.4 summarizes some of the discussion above, and highlights one of very few known obstructions to the existence of lifts using hyperbolicity cones.

![image 9](<2019-saunderson-limitations-expressive-power-convex_images/imageFile9.png>)

2Self-dual conex cones for which the automorphism group acts transitively on the interior.

Corollary 2.3. Suppose C is a proper convex cone such that for any N ∈ N there is a subset VN ⊆ ext(C) such that |VN| ≥ N and C is k-neighborly with respect to VN. If p is hyperbolic with respect to e and all the irreducible components of p have degree at most k, then C does not have a Λ+(p,e)-lift.

# 3 Technical preliminaries

In this section we brieﬂy introduce the additional deﬁnitions, and basic technical results, needed for our proof of Theorem 1.4.

## 3.1 Convex cones and their faces

The lineality space Lin(C) of a closed convex cone is Lin(C) := C∩(−C), and is the largest subspace contained in C. A closed convex cone C is pointed if and only if Lin(C) = {0}. A closed convex cone can always be expressed as C = C′ + Lin(C) where C′ is pointed and the sum is direct (for instance we can take C′ = C ∩ Lin(C)⊥).

If C ⊆ Rn is a closed convex cone and X ⊆ C, we denote by FC(X) the smallest (inclusionwise) face of C containing X. If x ∈ C, we write FC(x) instead of FC({x}) for the smallest (inclusion-wise) face of C containing x. If C is clear from the context, we omit it from the notation.

The collection of faces of a proper convex cone C, partially ordered by inclusion, form a lattice [Bar73]. The lattice operations are

F1 ∧ F2 = F1 ∩ F2 and F1 ∨ F2 = FC(F1 ∪ F2). We summarize some useful properties of this operation for future reference.

- Lemma 3.1. Let C be a proper convex cone.


- 1. If F is a face of C and F C then dim(F) < dim(C).
- 2. If x ∈ C and F is a face of C then FC(x) = F if and only if x ∈ relint(F).
- 3. If λ > 0 and x ∈ C then FC(λx) = FC(x).
- 4. If x,y ∈ C then FC(x + y) = FC(x) ∨ FC(y).
- 5. If x1,... ,xn ∈ C and λ1,... ,λn > 0 then


FC

n

n

FC(λixi) =

λixi =

i=1

i=1

n

FC(xi) = FC

i=1

n

xi .

i=1

Proof. The ﬁrst statement is [Roc15, Corollary 18.1.3]. For the second statement, suppose that x ∈ relint(F). Then F is a face of C that contains x, so FC(x) ⊆ F. Moreover, x ∈ FC(x)∩relint(F) so, by [Roc15, Corollary 18.1.2], F ⊆ FC(x). Now assume that FC(x) = F. Then, by [Bar73,

- Lemma 2.9], x ∈ relint(FC(x)) = relint(F). The third statement follows from the fact that if F is a face of C then x ∈ F if and only if λx ∈ F. The fourth statement is a special case of [BC75, Corollary 1]. The ﬁfth statement follows from statements 3 and 4.


![image 10](<2019-saunderson-limitations-expressive-power-convex_images/imageFile10.png>)

![image 11](<2019-saunderson-limitations-expressive-power-convex_images/imageFile11.png>)

![image 12](<2019-saunderson-limitations-expressive-power-convex_images/imageFile12.png>)

![image 13](<2019-saunderson-limitations-expressive-power-convex_images/imageFile13.png>)

- 3.2 Cone lifts and the factorization theorem We begin with the notion of a proper3 lift, a slight reﬁnement of Deﬁnition 1.1.


Deﬁnition 3.2. If C ⊆ Rn and K ⊆ Rd are closed convex cones then C has a proper K-lift if C = π(K ∩ L) where π : Rd → Rn is a linear map and L ⊆ Rd is a linear subspace that meets the relative interior of K.

The factorization theorem [GPT13, Theorem 1] of Gouveia, Parrilo, and Thomas, allows us to reformulate geometric questions about the existence of cone lifts as algebraic questions about the existence of factorizations of certain non-negative operators. Here we state and prove (for completeness) only the direction of the result of Gouveia, Parrilo, and Thomas that we need, and express it in a modiﬁed form that is most convenient for our subsequent use.

Theorem 3.3 (Factorization theorem [GPT13, Theorem 1]). If a proper convex cone C has a proper K1 × ··· × Km-lift then, for i = 1,2,... ,m, there are maps ai : C∗ → Ki∗ and bi : C → Ki such that x,y = mi=1 bi(x),ai(y) for all (x,y) ∈ C × C∗.

Proof. Since C has a proper K := K1 × ··· × Km-lift there is a subspace L that meets the relative interior of K such that C = π(K ∩ L). For each x ∈ C deﬁne b(x) to be an arbitrary choice of element of K ∩ L such that π(b(x)) = x.

Since C = π(K ∩ L) and L meets the relative interior of K, it follows from [Roc15, Corollary 16.4.2] that π∗(C∗) ⊆ (K ∩ L)∗ = K∗ + L⊥. So, for each y ∈ C∗, there exists a(y) ∈ K∗ and w(y) ∈ L⊥ such that π∗(y) = a(y) + w(y). Then

x,y = π(b(x)),y = b(x),π∗(y) = b(x),a(y) + w(y) = b(x),a(y)

since b(x) ∈ L and w(y) ∈ L⊥. If we let the ai and bi be the associated coordinate functions of a and b, the result follows.

![image 14](<2019-saunderson-limitations-expressive-power-convex_images/imageFile14.png>)

![image 15](<2019-saunderson-limitations-expressive-power-convex_images/imageFile15.png>)

![image 16](<2019-saunderson-limitations-expressive-power-convex_images/imageFile16.png>)

![image 17](<2019-saunderson-limitations-expressive-power-convex_images/imageFile17.png>)

The following result means we can replace general lifts with proper lifts when we prove Theorem 1.4, allowing us to use the factorization theorem.

- Lemma 3.4. Suppose that C is a proper convex cone and there exist a positive integer m and closed convex cones K˜1,K˜2,... ,K˜m such that C has a K˜1 × ··· × K˜m-lift and ℓ(K˜i) ≤ k +1 for all i ∈ [m]. Then there exist a positive integer m and closed convex cones K1,K2,... ,Km such that C has a proper K1 × ··· × Km-lift and ℓ(Ki) ≤ k + 1 for all i ∈ [m].


Proof. By our assumption on C, there is a linear map π and a subspace L such that C = π(L ∩ (K˜1 × ··· × K˜m)). If L meets the relative interior of K˜1 × ··· × K˜m we simply take Ki = K˜i for all i ∈ [m]. If L does not intersect the relative interior of K˜1 × ··· × K˜m then let F denote the minimal face of K˜1 × ··· × K˜m containing (K˜1 × ··· × K˜m) ∩ L. Since F is a face of K˜1 × ··· × K˜m it has the form F1 ×···×Fm where Fi is a face of K˜i for all i ∈ [m] [Bar78, Theorem 2]. Moreover, we have that ℓ(Fi) ≤ ℓ(K˜i) for all i ∈ [m]. As such, C has a proper F1 × F2 × ··· × Fm-lift and ℓ(Fi) ≤ k + 1 for all i ∈ [m]. Taking Ki = Fi for all i ∈ [m] completes the proof.

![image 18](<2019-saunderson-limitations-expressive-power-convex_images/imageFile18.png>)

![image 19](<2019-saunderson-limitations-expressive-power-convex_images/imageFile19.png>)

![image 20](<2019-saunderson-limitations-expressive-power-convex_images/imageFile20.png>)

![image 21](<2019-saunderson-limitations-expressive-power-convex_images/imageFile21.png>)

![image 22](<2019-saunderson-limitations-expressive-power-convex_images/imageFile22.png>)

3The notion of a proper lift of a closed convex cone (from Deﬁnition 3.2) is quite distinct from the notion of a proper (i.e., closed, pointed, full-dimensional) convex cone. The distinction between these (standard) uses should be clear from the context.

## 3.3 Ramsey numbers

The key combinatorial result we use is Ramsey’s theorem for hypergraphs. We formally state it in language more suited to our application.

Theorem 3.5 ([Ram30, Theorem B]). Let k, m, and n be positive integers. There exists a positive integer Rk(m;n) such that whenever V is a set with |V | ≥ Rk(m;n) and f : Vk → [n] then there exists W ⊆ V such that |W| = m and f(S) = f(T) for all S,T ∈ Wk .

In the hypergraph setting we think of f as a coloring of the k-uniform hypergraph on vertex set V with n colors, and W as a subset of m vertices of the hypergraph for which all induced hyperedges have the same color. Except in a few very special cases, the numbers Rk(m;n) are not known, although explicit upper bounds are available. For our purposes, we only need the fact that Rk(m;n) is ﬁnite for positive integers n,k, and m.

# 4 Generalizing Averkov’s lemmas and the proof of Theorem 1.4

In this section we establish Theorem 1.4 by generalizing the key technical arguments of [Ave19]. Crucial to Averkov’s approach is the following simple result about positive semideﬁnite matrices. In the statement, if X is a positive semideﬁnite matrix, let col(X) denote its column space, and interpret the empty sum as zero, i.e., i∈∅ Xi = 0.

- Lemma 4.1. Suppose X1,X2,... ,Xℓ 0 and rank( i∈[n] Xi) = k. Then there exists a subset I ⊆ [n] with |I| ≤ k such that col i∈I Xi = col i∈[n] Xi .


We note that Averkov states the conclusion in an equivalent form as i∈I col(Xi) = i∈[n] col(Xi). The statement given here suggests, more clearly, the generalization we require.

Lemma 4.1 can be generalized to the setting in which the rank is replaced with the largest length of a chain of nonempty faces (minus one), and the column space is replaced with the minimal face containing a point of the convex cone. In the statement and proof of Lemma 4.2 we interpret the empty sum as zero, i.e., i∈∅ xi = 0.

- Lemma 4.2. Let K be a closed convex cone and suppose that x1,x2,... ,xn ∈ K are such that n i=1 xi ∈ relint(K). Then there exists I ⊆ [n] with |I| ≤ ℓ(K) − 1 such that F( i∈I xi) =


F( i∈[n] xi) = K.

Proof. First, we will prove the result under the assumption that K is pointed. We argue by induction on ℓ(K). For the base case, consider a closed pointed convex cone with ℓ(K) = 1. The only possibility is K = {0}. In this case if x1,... ,xn ∈ K we can choose I = ∅ so that |I| = 0 = ℓ({0}) − 1 and F( i∈I xi) = F(0) = {0} = K.

Assume the statement holds for all closed pointed convex cones K with ℓ(K) ≤ k, for some positive integer k. Consider a closed pointed convex cone C with ℓ(C) = k + 1. Let x1,... ,xn ∈ C be such that F(x1 + ··· + xn) = C. Let I ⊆ [n] be an inclusion-wise minimal subset of [n] such that F( i∈I xi) = C. Choose some j ∈ I and observe that xj ∈/ F( i∈I\{j} xi) (by minimality of I) and so F( i∈I\{j} xi) is strictly contained in C. Hence,

ℓ(F( i∈I\{j} xi)) ≤ ℓ(C) − 1 = k.

Since F( i∈I\{j} xi) is closed, convex, and pointed, by the induction hypothesis, there is some I′ ⊆ I \ {j} such that |I′| ≤ k − 1 and

F( i∈I′ xi) = F( i∈I\{j} xi).

Then, by Lemma 3.1, F(xj + i∈I′ xi) = F(xj) ∨ F( i∈I′ xi)

= F(xj) ∨ F( i∈I\{j} xi) = F( i∈I xi) = C.

Since I is minimal with this property and I′ ∪ {j} ⊆ I we must have that I′ ∪ {j} = I. It then follows that |I| = |I′| + 1 ≤ k, as required.

If K is not pointed, then K = K′ + Lin(K) where K′ is pointed and the sum is direct. Furthermore, F′ is a face of K′ if and only if F′ + Lin(K) is a face of K. If x = x′ + z with x′ ∈ K′ and z ∈ Lin(K) then x ∈ relint(K) if and only if x′ ∈ relint(K′).

Now, let xi = x′i+zi be decompositions of each of the xi so that x′i ∈ K′ and zi ∈ Lin(K) for all i. By assumption, ni=1 xi ∈ relint(K) and so ni=1 x′i ∈ relint(K′). Since the lemma holds for the pointed case, there exists I ⊆ [n] with |I| ≤ ℓ(K′) − 1 = ℓ(K) − 1 such that i∈I x′i ∈ relint(K′). Then i∈I xi ∈ relint(K) as required.

![image 23](<2019-saunderson-limitations-expressive-power-convex_images/imageFile23.png>)

![image 24](<2019-saunderson-limitations-expressive-power-convex_images/imageFile24.png>)

![image 25](<2019-saunderson-limitations-expressive-power-convex_images/imageFile25.png>)

![image 26](<2019-saunderson-limitations-expressive-power-convex_images/imageFile26.png>)

Averkov’s main lemma is the following result, which relies crucially on Lemma 4.1 for its proof.

- Lemma 4.3. Let m be a positive integer and let S denote a ﬁnite set with cardinality at least k. Suppose that, for each i ∈ [m], there are maps ai : Sk → S+k and bi : S → S+k such that

m

i=1

ai(T),bi(s) = 0 ⇐⇒ s ∈ T.

Then |S| < Rk(k + 1;(k + 1)m).

We can use essentially the same argument as Averkov to establish the following analogue of Lemma 4.3, once we replace column spaces by minimal faces and rank with the largest length of a chain of nonempty faces (minus one). We recover Averkov’s lemma as a special case by noting that the cone S+k is self-dual and satisﬁes ℓ(S+k) = k + 1.

- Lemma 4.4. Let m be a positive integer and let K1,K2,... ,Km be closed convex cones. Let S denote a ﬁnite set with cardinality at least k. Suppose that, for each i ∈ [m], there are maps ai : Sk → Ki∗ and bi : S → Ki such that


m

i=1

ai(T),bi(s) = 0 ⇐⇒ s ∈ T.

If ℓ(Ki) ≤ k + 1 for i = 1,2,... ,m then |S| < Rk(k + 1;(k + 1)m). Proof. For each T ⊆ S and each i ∈ [m] deﬁne

bT,i :=

t∈T

bi(t) ∈ Ki and dT,i := ℓ(F(bT,i)).

For each T ∈ Sk , we assign ‘color’ (dT,1,... ,dT,m) to the set T. Since ℓ(Ki) ≤ k + 1, then the same is true for any nonempty face of Ki, and so dT,i ∈ {0,1,... ,k} for each T and i. As such, we are coloring with at most (k + 1)m colors.

Seeking a contradiction, let us assume that |S| ≥ Rk(k + 1;(k + 1)m). Then, by the deﬁnition of the Ramsey number, there exists W ⊆ S with |W| = k + 1 such that all k-element subsets of W have the same color (d1,d2,... ,dm). More explicitly, for all T ⊂ W with |T| = k we have (dT,1,... ,dT,m) = (d1,... ,dm).

Claim For each i ∈ [m] and each T ⊂ W such that |T| = k, we have that F(bT,i) = F(bW,i). If this were not the case, then there exists such an i ∈ [m] and T ⊂ W with |T| = k such that F(bW,i) strictly contains F(bT,i). By Lemma 4.2, there is a subset T′ ⊆ W with |T′| ≤ ℓ(F(bW,i)) − 1 ≤ k such that F( t′∈T′ bi(t′)) = F(bW,i). By adding elements of W (if necessary) we can form a set T′′ such that T′ ⊆ T′′ ⊂ W and |T′′| = k such that

F

bi(t′′) ⊇ F

t′′∈T′′

bi(t′) = F(bW,i).

t′∈T′

One the one hand, since all k-element subsets of W have the same ‘color’, di = dT′′,i ≥ ℓ(F(bW,i)). On the other hand, since F(bW,i) strictly contains F(bT,i) we have that ℓ(F(bW,i)) > ℓ(F(bT,i)) = di. This contradiction establishes the claim.

With the claim established, we write W = T ∪ {s} where |T| = k and s ∈/ T. By assumption on ai and bi, we have that

m

ai(T),bi(t) = 0 for all t ∈ T.

i=1

Since ai(T) ∈ Ki∗ and bi(t) ∈ Ki we can conclude that

ai(T),bi(t) = 0 for all t ∈ T and all i ∈ [m]. But then

ai(T),

bi(t) = 0.

t∈T

In particular, for each i ∈ [m] the linear functional deﬁned by ai(T) vanishes on the face F( t∈T bi(t)) = F(bT,i) = F(bW,i) where the last equality is the claim. But then, even though s ∈/ T, we have that

0 = ai(T),

w∈W

bi(w) = ai(T),bi(s) +

t∈T

bi(t) = ai(T),bi(s)

for all i ∈ [m]. This contradicts the fact that a and b satisfy 0 = mi=1 ai(T),bi(s) if and only if s ∈ T. It then follows that |S| < Rk(k + 1;(k + 1)m).

![image 27](<2019-saunderson-limitations-expressive-power-convex_images/imageFile27.png>)

![image 28](<2019-saunderson-limitations-expressive-power-convex_images/imageFile28.png>)

![image 29](<2019-saunderson-limitations-expressive-power-convex_images/imageFile29.png>)

![image 30](<2019-saunderson-limitations-expressive-power-convex_images/imageFile30.png>)

Following Averkov, we combine Lemma 4.3 with the factorization theorem of Gouveia, Parrilo, and Thomas (Theorem 3.3) to turn the statement about the structure of maps ai and bi into a statement about lifts of convex cones. We brieﬂy repeat the argument here, in our setting, to make the paper more self-contained.

Proposition 4.5. Suppose that a proper convex cone C ⊆ Rn has a proper K1 × ··· × Km-lift where ℓ(Ki) ≤ k + 1 for i ∈ [m]. If C is k-neighborly with respect to some ﬁnite set V ⊆ ext(C) then |V | < Rk(k + 1;(k + 1)m).

Proof. Since C is k-neighborly with respect to V , for each k-element subset W ∈ Vk there is fW ∈ C∗ such that fW,w vanishes if w ∈ W and is positive if w ∈ V \ W. Since C has a proper K1 × ··· × Km lift, by the factorization theorem (Theorem 3.3) we know that for i = 1,2,... ,m

there exist maps a˜i : C∗ → Ki∗ and ˜bi : C → Ki such that f,x = mi=1 a ˜i(f),˜bi(x) for all f ∈ C∗ and all x ∈ C. Deﬁne ai : Vk → Ki∗ by ai(W) = a˜i(fW) and bi : V → Ki by bi(w) = ˜bi(w). Then

fW,w = mi=1 ai(W),bi(w) which vanishes when w ∈ W and is positive when w ∈ V \ W. It follows from Lemma 4.4 that |V | < Rk(k + 1;(k + 1)m).

![image 31](<2019-saunderson-limitations-expressive-power-convex_images/imageFile31.png>)

![image 32](<2019-saunderson-limitations-expressive-power-convex_images/imageFile32.png>)

![image 33](<2019-saunderson-limitations-expressive-power-convex_images/imageFile33.png>)

![image 34](<2019-saunderson-limitations-expressive-power-convex_images/imageFile34.png>)

Theorem 1.4 is a straightforward consequence of Proposition 4.5.

Proof of Theorem 1.4. By assumption, there exists some ﬁnite V ⊂ ext(C) such that |V | ≥ Rk(k + 1;(k+1)m) and C is k-neighborly with respect to V . Then by the contrapositive of Proposition 4.5 it follows that C does not have a proper K1 × ··· × Km lift with ℓ(Ki) ≤ k + 1 for all i ∈ [m]. It follows from Lemma 3.4 that C does not have a (possibly improper) K˜1 × ··· × K˜m-lift with ℓ(K˜i) ≤ k + 1 for all i ∈ [m], completing the proof.

![image 35](<2019-saunderson-limitations-expressive-power-convex_images/imageFile35.png>)

![image 36](<2019-saunderson-limitations-expressive-power-convex_images/imageFile36.png>)

![image 37](<2019-saunderson-limitations-expressive-power-convex_images/imageFile37.png>)

![image 38](<2019-saunderson-limitations-expressive-power-convex_images/imageFile38.png>)

# 5 Discussion

In this paper we have shown that for a convex cone C, having a certain neighborliness property is an obstruction to having a K-lift where K is a Cartesian product of cones all of which only have short chains of faces. Our argument is a fairly direct generalization of an argument of Averkov showing that the same neighborliness property is an obstruction to having an (S+k )m-lift.

Although we only stated qualitative results about the non-existence of lifts, the approach taken in this paper could be made quantitative in the following sense. If C is k-neighborly with respect to a ﬁnite set V and ℓ(Ki) ≤ k +1 for all i, then Theorem 1.4 does not rule out the possibility that C has a K1 × ··· × Km-lift. However one could, in principle, extract a lower bound on the number of factors m required in any such lift in terms of k and |V |. Unfortunately, this gives very weak lower bounds, since the Ramsey numbers Rk(k + 1;(k + 1)m) grow extremely fast (and so the implied lower bounds on m grows extremely slowly). For convex cones that do have K1 × ··· × Km-lifts where ℓ(Ki) ≤ k +1 for all i, it would be very interesting to develop general techniques to establish stronger lower bounds on m, the number of factors. In the case k = 1 this reduces to the study of lower bounds on the linear programming extension complexity of a polyhedral cone.

This paper gives some of the ﬁrst results about non-existence of K-lifts where K is a hyperbolicity cone. Currently the only other such result is a lower bound on the size of PSD lifts of convex semialgebraic sets, based on quantiﬁer elimination [GPT13], that can be generalized directly to the setting of hyperbolicity cones. Fawzi and Safey El Din [FSED18] strengthen the quantiﬁer elimination-based bounds in the case of PSD lifts by exploiting connections with the algebraic degree of semideﬁnite programming [NRS10]. It would be interesting to develop a similar approach to devise lower bounds on natural notions of complexity for lifts using hyperbolicity cones.

Acknowledgments I would like to thank Hamza Fawzi for encouraging and insightful comments related to this work, Venkat Chandrasekaran for introducing me to the notion of the length of the longest chain of nonempty faces of a convex cone, and the anonymous referees for their careful reading and very helpful comments.

# References

[AB18] N. Amini and P. Br¨nde´n. Non-representable hyperbolic matroids. Advances in Mathematics, 334:417–449, 2018.

[AHMR88] J. Agler, W. Helton, S. McCullough, and L. Rodman. Positive semideﬁnite matrices with a given sparsity pattern. Linear algebra and its applications, 107:101–149, 1988.

[AM19] A. A. Ahmadi and A. Majumdar. DSOS and SDSOS optimization: more tractable alternatives to sum of squares and semideﬁnite optimization. SIAM Journal on Applied Algebra and Geometry, 3(2):193–230, 2019.

[Ave19] G. Averkov. Optimal size of linear matrix inequalities in semideﬁnite approaches to polynomial optimization. SIAM Journal on Applied Algebra and Geometry, 3(1):128– 151, 2019.

[Bar73] G. P. Barker. The lattice of faces of a ﬁnite dimensional cone. Linear Algebra and its

Applications, 7(1):71–82, 1973. [Bar78] G. P. Barker. Perfect cones. Linear Algebra and its Applications, 22:211–221, 1978. [BC75] G. P. Barker and D. Carlson. Cones of diagonally dominant matrices. Paciﬁc Journal

of Mathematics, 57(1):15–32, 1975. [BSV17] G. Blekherman, R. Sinn, and M. Velasco. Do sums of squares dream of free resolutions? SIAM Journal on Applied Algebra and Geometry, 1(1):175–199, 2017. [BTN01] A. Ben-Tal and A. Nemirovski. Lectures on modern convex optimization: analysis, algorithms, and engineering applications, volume 2. SIAM, 2001. [CS16] V. Chandrasekaran and P. Shah. Relative entropy relaxations for signomial optimization. SIAM Journal on Optimization, 26(2):1147–1173, 2016. [Faw18] H. Fawzi. On representing the positive semideﬁnite cone using the second-order cone. Mathematical Programming, pages 1–10, 2018. [FSED18] H. Fawzi and M. Safey El Din. A lower bound on the positive semideﬁnite rank of convex bodies. SIAM Journal on Applied Algebra and Geometry, 2(1):126–139, 2018. [Ga˚r59] L. Ga˚rding. An inequality for hyperbolic polynomials. Journal of Mathematics and Mechanics, pages 957–965, 1959. [GJSW84] R. Grone, C. R. Johnson, E. M. Sa´, and H. Wolkowicz. Positive deﬁnite completions of partial Hermitian matrices. Linear algebra and its applications, 58:109–124, 1984. [GPT13] J. Gouveia, P. A. Parrilo, and R. R. Thomas. Lifts of convex sets and cone factorizations. Mathematics of Operations Research, 38(2):248–264, 2013. [IDW16] S. Iliman and T. De Wolﬀ. Amoebas, nonnegative polynomials and sums of squares supported on circuits. Research in the Mathematical Sciences, 3(1):9, 2016. [IL17] M. Ito and B. F. Louren¸o. A bound on the Carathe´odory number. Linear Algebra and its Applications, 532:347–363, 2017. [KW08] G. Kalai and A. Wigderson. Neighborly embedded manifolds. Discrete & Computational Geometry, 40(3):319–324, 2008.

[LP18] M. Liu and G. Pataki. Exact duals and short certiﬁcates of infeasibility and weak infeasibility in conic linear programming. Mathematical Programming, 167(2):435–480, 2018.

[NRS10] J. Nie, K. Ranestad, and B. Sturmfels. The algebraic degree of semideﬁnite programming. Mathematical Programming, 122(2):379–405, 2010.

[Nui69] W. Nuij. A note on hyperbolic polynomials. Mathematica Scandinavica, 23(1):69–72, 1969.

[Pat13] G. Pataki. Strong duality in conic linear programming: facial reduction and extended duals. In Computational and analytical mathematics, pages 613–634. Springer, 2013.

[Ram30] F. P. Ramsey. On a problem of formal logic. Proceedings of the London Mathematical Society, 2(1):264–286, 1930.

[Ren06] J. Renegar. Hyperbolic programs, and their derivative relaxations. Foundations of

Computational Mathematics, 6(1):59–79, 2006. [Roc15] R. T. Rockafellar. Convex analysis. Princeton University Press, 2015. [VA15] L. Vandenberghe and M. S. Andersen. Chordal graphs and semideﬁnite optimization.

Foundations and Trends R in Optimization, 1(4):241–433, 2015. [WM13] H. Waki and M. Muramatsu. Facial reduction algorithms for conic optimization problems. Journal of Optimization Theory and Applications, 158(1):188–215, 2013.

