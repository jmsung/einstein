arXiv:1611.09479v1[math.MG]29Nov2016

Upper bounds for s-distance sets and equiangular lines

Alexey Glazyrin∗ and Wei-Hsuan Yu† November 30, 2016

Abstract

The set of points in a metric space is called an s-distance set if pairwise distances between these points admit only s distinct values. Two-distance spherical sets with the set of scalar products {α,−α}, α ∈ [0,1), are called equiangular. The problem of determining the maximum size of s-distance sets in various spaces has a long history in mathematics. We suggest a new method of bounding the size of an s-distance set in compact two-point homogeneous spaces via zonal spherical functions. This method allows us to prove that the maximum size of a spherical

two-distance set in Rn, n ≥ 7, is n(n2+1) with possible exceptions for some n = (2k + 1)2 − 3, k ∈ N. We also prove the universal upper bound ∼ 23na2 for equiangular sets with α = a1 and, employing this bound, prove a new upper bound on the size of equiangular sets in all dimensions. Finally, we classify all equiangular sets reaching this new bound.

![image 1](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile1.png>)

![image 2](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile2.png>)

![image 3](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile3.png>)

# 1 Introduction

An s-distance set in a metric space M is a ﬁnite set of points with exactly s distinct pairwise distances. A number of classical problems can be formulated in terms of ﬁnding s-distance sets of maximum size. For example, the Ray-Chaudhuri–Wilson theorem [54] gives an upper bound of ns for s-distance sets in the Johnson space Jn,w (the space of subsets of an n-element set with exactly w elements). A special case of this problem corresponds to the celebrated Erd˝os-Ko-Rado theorem [28, 63]. There is extensive literature devoted to generalizations and improvements of these results [24, 25, 32, 31, 2, 3, 1, 33, 58, 34].

In the Euclidean case Rn, problems of ﬁnding upper bounds on the maximum size of s-distance sets are generally of two types: the number of distinct distances s is very large compared to n, and the number of distinct distances is comparable to n. For the former case, the most well-studied problem is the famous Erd˝os distinct distances problem for the plane [27] which was essentially solved by Guth and Katz [36] who proved that the size of an s-distance set on the plane is O(s ln s). In the latter case, the upper bound n+s s was given in [8]. There is a natural example for each s ≤ n with the same asymptotic order as this bound: the set of n+1s centers of all s-faces of a regular simplex. Distances between the centers are deﬁned only by how many common vertices their faces have. The study of two-distance sets was initiated in [26]. Apart from the natural example described above, very little is known about lower bounds [46].

The above example works in the spherical case as well since all the face centers are equidistant from the center of the circumsphere. The ﬁrst upper bounds for the maximum size of an s-distance

![image 4](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile4.png>)

∗School of Mathematical & Statistical Sciences, The University of Texas Rio Grande Valley, USA. †Mathematics Department, Michigan State University, USA.

set on the unit sphere Sn−1 were found in [23] (the so-called harmonic bounds, see Theorem 7). If an s-distance set attains the harmonic bound, then it forms a so-called tight spherical 2s-design (see the survey paper [6]). Several maximum spherical s-distance sets are known to form beautiful and important conﬁgurations on the unit sphere. For instance, the maximum 3-distance set in R3 is the icosahedron. The maximum 3-distance sets in R8 is coming from the E8 root system. It provides the solution to the kissing number problem in R8 [45, 51] and also, as it has been recently shown, generates an optimal sphere packing in R8 [60]. Maximum spherical s-distance sets also usually oﬀer a solution for energy minimization problems on sphere. The table in [19] of universal optimal codes, minimizers of a large class of energy functions on the sphere, shows that most of them are maximum spherical s-distance sets.

Denote by g(n) the maximum size of a two-distance set in Sn−1. The harmonic bound gives

g(n) ≤ n(n2+3). This bound is attained on the regular pentagon for n = 2. The results of [23] also imply that the harmonic bound can be reached for n ≥ 3 only if n = a2 − 3, where a is an

![image 5](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile5.png>)

odd number. In fact for a = 3 and 5 two-distance sets with 27 and 275 points respectively do exist [43, 20]. It follows from [10, 49] that this is not the case for inﬁnitely many other values of

a: a cannot be equal to 7,9,13,21,45,61,69, 77, etc. In [47] it was shown that g(n) = n(n2+1) for 7 ≤ n ≤ 39 except for n = 22,23. The set of the values of n, where the natural lower bound is in

![image 6](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile6.png>)

fact optimal, was extended to almost all n ≤ 93 in [14] and almost all n ≤ 417 in [65]. As one of the main results of this paper we show that this pattern holds for all n.

- Theorem 1.

g(n) =

n(n + 1) 2

![image 7](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile7.png>)

for all n ≥ 7 with possible exceptions for some n = (2k + 1)2 − 3, k ∈ N.

Finding maximum s-distance sets is sometimes equivalent to constructing tight spherical tdesigns for t = 2s [23]. For s = 2, the only unknown cases in Theorem 1 are exactly the longstanding open problems for the classiﬁcation of tight spherical 4-designs.

A particular case of two-distance spherical sets, namely equiangular sets, attracts a lot of interest as it arises in various areas of mathematics. For instance, there is an extensive literature in frame theory devoted to equiangular tight frames [56, 38, 57].

By an equiangular spherical set we will mean a two-distance spherical set with scalar products α and −α. The natural question is to determine the maximum cardinality M(n) of an equiangular set in Sn−1. This problem was posed in [43] where a few values of M(n) were determined. The general upper bound n+12 is due to Gerzon [44] (see Theorem 8).

It is not hard to show the connection between equiangular sets attaining Gerzon’s bound and two-distance sets reaching the harmonic bound. For each equiangular set with n(n2+1) points it is possible to construct a derived set (see Subsection 2.2 for more details) in Sn−2 with n(n2+1) − 1 = (n−1)(n+2)

![image 8](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile8.png>)

![image 9](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile9.png>)

![image 10](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile10.png>)

2 points that must attain the harmonic bound. It is much more diﬃcult to construct equiangular sets of large size. The ﬁrst O(n2) construction

was found by de Caen in [18] (see also [39, 35] for large equiangular sets). This construction has 2 9(n + 1)2 points in Sn−1, where n = 3 · 22t−1, t ∈ N. There are also O(n3/2) constructions of equiangular sets built on Taylor graphs and projective planes [44].

![image 11](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile11.png>)

We improve Gerzon’s general bound on equiangular sets for almost all natural n.

- Theorem 2. If n ≥ 359, then


(a2 − 2)(a2 − 1) 2

,

M(n) ≤

![image 12](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile12.png>)

where a is the unique positive odd integer such that a2 − 2 ≤ n ≤ (a + 2)2 − 3.

If n = a2 − 2 for some odd integer a the upper bound of Theorem 2 coincides with Gerzon’s bound. For all other n ≥ 359, the bound of Theorem 2 strictly improves Gerzon’s bound.

Denote by Mα(n) the cardinality of the largest equiangular set in Sn−1 with scalar products α,−α. The question of ﬁnding maximum equiangular sets with prescribed scalar products was raised in [44]. In their paper, Lemmens and Seidel found that M1

(n) ≤ 2n − 2 for n ≥ 15. They also proved that if nα2 < 1, then Mα(n) ≤ n(1−α

![image 13](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile13.png>)

3

2)

1−nα2 (the so-called relative bound, see Theorem 5). Generally, it was shown by Neumann (see [44]) that M1

![image 14](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile14.png>)

(n) ≤ 2n unless a is an odd natural number. For a ﬁxed odd natural a the behavior of M1

![image 15](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile15.png>)

a

(n) was not known before the paper of Bukh [17], where he showed that M1

![image 16](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile16.png>)

a

(n) ≤ cn, where c = 2O(a2). Recently this bound was signiﬁcantly improved by Balla, Dr¨xler, Keevash, and Sudakov. In [5] they showed that for suﬃciently large n, M1

![image 17](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile17.png>)

a

(n) ≤ 1.93n. We prove a new universal bound on M1

(n) ≤ 2n − 2. If a = 3, their bound is even better, namely M1

![image 18](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile18.png>)

![image 19](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile19.png>)

a

a

(n) that works for all a ≥ 3 and all n.

![image 20](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile20.png>)

a

- Theorem 3. M1

![image 21](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile21.png>)

a

(n) ≤ n

- 2

![image 22](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile22.png>)

- 3


a2 +

4 7

![image 23](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile23.png>)

+ 2, for all a ≥ 3 and for all n ∈ N.

The main beneﬁt of this bound is its universality. Only for a2 34n, Gerzon’s bound is a better upper bound for M1

![image 24](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile24.png>)

![image 25](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile25.png>)

a

(n). For a ﬁxed a, the bound of Theorem 3 is asymptotically inferior to the bound from [5]. However, the bound from [5] is valid only for suﬃciently large n (depending on a) and our bound works for all pairs (a,n). We also note that the bound of Theorem 3 is usually better than SDP bounds in [15] and [41] when a is relatively small compared to n (see Section 4 for details).

Finally, we classify all extremal cases, where the bound of Theorem 2 is attained.

- Theorem 4. For each odd natural number a ≥ 3, if n ≤ 3a2−16, then the equiangular set X ⊂ Sn−1


2−2)(a2−1)

with scalar products a1,−a1 and exactly (a

2 points must belong to an (a2 − 2)-dimensional subspace.

![image 26](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile26.png>)

![image 27](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile27.png>)

![image 28](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile28.png>)

- Corollary 1. Let n ≥ 359 and let a be the unique positive odd integer such that a2 − 2 ≤ n ≤


2−2)(a2−1)

(a + 2)2 − 3. Suppose that X ⊂ Sn−1 is an equiangular set of size (a

2 . Then X has scalar products a1,−a1 and is contained in an (a2 − 2)-dimensional subspace.

![image 29](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile29.png>)

![image 30](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile30.png>)

![image 31](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile31.png>)

The paper is organized as follows. In Section 2 we overview the main methods applicable to the problem of ﬁnding maximal s-distance sets. Subsection 2.1 gives a brief introduction to zonal spherical functions on compact two-point homogeneous spaces. In Subsection 2.2, we show how Gegenbauer polynomials can be used to prove the relative bound on equiangular sets by Lemmens and Seidel [44] and the bound from [65]. In 2.3 we describe the polynomial method and demonstrate by giving short proofs of the bounds from [23, 44]. Section 3 is devoted to a new method of ﬁnding upper bounds on s-distance sets in two-point homogeneus spaces. In Section 4 we show how this method can be applied to two-distance spherical sets. Subsection 4.1 contains the general spherical bounds and in Subsection 4.2 we derive new bounds on equiangular sets. Proofs of Theorems 1 and 2 are contained in Section 5. In Section 6, we classify all extremal equiangular sets attaining the bound from Theorem 2. Section 7 is devoted to open questions and discussion.

# 2 s-distance sets

In this section we overview two general approaches used for ﬁnding upper bounds on s-distance sets.

## 2.1 Zonal spherical functions in compact two-point homogeneous spaces

The approach using zonal spherical functions for ﬁnding packing bounds was introduced by Delsarte et al [22, 23] and then generalized by Kabatyansky and Levenshtein [40] to all compact two-point homogeneous spaces. Here we brieﬂy deﬁne zonal spherical functions and explain how they can be used in this context.

A metric space M with group G acting on it is called two-point homogeneous if G acts transitively on ordered pairs with the same distance. Inﬁnite two-point homogeneous spaces with the structure of a connected Riemannian manifold are classiﬁed by Wang [62] and include only spheres; real, complex, quaternionic spaces; and the Cayley projective plane.

Suppose G is a connected compact group or a ﬁnite group. Taking H as a stabilizer of some ﬁxed point x0, we can associate each point in M with the corresponding left coset gH. Let µ be the Haar measure for G. This measure induces the unique invariant measure on M which we also denote by µ.

By L2(G) we denote the vector space of complex functions f on G satisfying

with the standard inner product

G

|f(g)|2dµ(g) < ∞

(f1,f2) =

![image 32](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile32.png>)

f1(g)f2(g)dµ(g).

G

By taking only functions of L2(G) constant on left cosets of H, we can deﬁne L2(M) with the analogously deﬁned inner product

(f1,f2) =

![image 33](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile33.png>)

f1(x)f2(x)dµ(x).

M

By the Peter-Weyl theorem [53], L2(G) splits into an orthogonal direct sum of irreducible ﬁnite-dimensional representations of G. With certain conditions on G (see, for instance, [40] or [21, Chapter 9] for details) this decomposition induces a decomposition of L2(M) into mutually orthogonal subspaces {V (k),k = 0,1,...}, hk = dim V (k), where each space deﬁnes an irreducible representation of G. For an orthonormal basis {e(1k),... ,e(hk)

} of V (k), deﬁne for each k

k

hk

![image 34](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile34.png>)

e(ik)(x)e(ik)(y).

Pk(x,y) =

i=1

Since V (k) deﬁnes a unitary representation of G, Pk(gx,gy) = Pk(x,y) and, because of twopoint homogeneity of M, Pk(x,y) depends only on the distance between x and y. The function Pk is called a zonal spherical function associated with V (k).

In practice, it is often convenient to use a modiﬁed distance function τ(x,y) (we call it just a distance function from now on) to express Pk(x,y) as a function of one variable Pk(τ(x,y)). Throughout the paper we will also use the notation τ0 = τ(x,x).

The deﬁnition of Pk implies that, for any ﬁnite set of points {x1,... ,xN} and any set of complex numbers {a1,... ,aN},

N

N

Pk(xi,xj)aiaj ≥ 0

![image 35](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile35.png>)

i=1

j=1

so the following proposition is true. Proposition 1. For any ﬁnite set X = {x1,... ,xN} and any k ≥ 0, the matrix (Pk(τ(xi,xj))) is positive semideﬁnite.

For the spherical case, the standard scalar product (x,y) is used as a distance function τ(x,y) and the zonal spherical functions are given by Gegenbauer polynomials which can be deﬁned recursively as follows:

G(0n)(t) = 1, G(1n)(t) = t,

(n + 2k − 4)tG(kn−)1(t) − (k − 1)G(kn−)2(t) n + k − 3

Gk(n)(t) =

.

![image 36](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile36.png>)

Here for convenience we use the normalized version of Gegenbauer polynomials, i.e. for all of them, G(kn)(1) = 1.

Since it will be used further in the paper, we would like to write down Gegenbauer polynomials of degree 2 and 3 as well:

nt2 − 1 n − 1

(n + 2)t3 − 3t n − 1

G2(n)(t) =

, G(3n)(t) =

.

![image 37](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile37.png>)

![image 38](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile38.png>)

Schoenberg [55] proved the converse version of Proposition 1 for the spherical case by showing that the real function f satisﬁes (f(τ(xi,xj))) 0 for any ﬁnite set X = {x1,... ,xN} only if f is a non-negative combination of Gegenbauer polynomials. Bochner [16] proved the general version of this theorem for zonal spherical functions.

## 2.2 Bounds on equiangular sets via Gegenbauer polynomials

Here we show how to use zonal spherical functions to prove upper bounds on the size of equiangular sets. The following relative bound was proved by Lemmens and Seidel [44].

- Theorem 5 (Relative bound). For an n-dimensional equiangular set X with scalar products {α,−α} with nα2 < 1,


n(1 − α2) 1 − nα2

|X| ≤

![image 39](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile39.png>)

Proof. Let X = {x1,... ,xN}. The matrix G(2n)(xi,xj) is positive semideﬁnite by Proposition 1 so its sum of elements must be non-negative. Note that its diagonal elements are 1 and all the

non-diagonal elements are nαn−2−11 so we get N +N(N −1)nαn−2−11 ≥ 0 and, therefore, N ≤ 1−n−nα12 +1 = n(1−α2)

![image 40](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile40.png>)

![image 41](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile41.png>)

![image 42](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile42.png>)

1−nα2 .

![image 43](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile43.png>)

![image 44](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile44.png>)

![image 45](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile45.png>)

![image 46](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile46.png>)

![image 47](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile47.png>)

As one more example we show how to obtain a short proof of the main theorem from [65]. The proof in [65] relied on a more intricate approach of Bachoc and Vallentin [4].

- Theorem 6.


(a2 − 2)(a2 − 1) 2 for all n and a such that n ≤ 3a2 − 16 and a ≥ 3.

M1

(n) ≤

![image 48](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile48.png>)

![image 49](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile49.png>)

a

Before proving this theorem we describe the construction of derived spherical s-distance sets. For an s-distance set Z ⊂ Sn−1 the set of all points of Z equidistant from some ﬁxed point x ∈ Z form an s-distance set with the same set of distances in a sphere of smaller dimension and smaller radius. By shifting these points and dilating the sphere we can get an s-distance set on a unit sphere. Deﬁning this formally, the set Zx,α derived from Z, with respect to x ∈ Z and scalar

product α, is √ y1−−αxα2|y ∈ Z,(y,x) = α . If the set of scalar products of Z is {α,β,γ,...}, then Zx,α will have scalar products {α1−−αα22, β1−−αα22, γ1−−αα22,...}. Proof of Theorem 6. Unless a is an odd natural number (see [44] and the explanation after Lemma 2.3), M1

![image 50](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile50.png>)

![image 51](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile51.png>)

![image 52](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile52.png>)

![image 53](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile53.png>)

![image 54](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile54.png>)

2−2)(a2−1)

(n) ≤ 2n ≤ 2(3a2 − 16) which is always smaller than (a

2 . Therefore, we are interested only in the case when a is an odd natural. It is suﬃcient to prove the statement of the theorem for n equal to 3a2 − 16 exactly since any set of smaller dimension will be realizable in larger dimensions as well. From this moment on, n = 3a2 − 16.

![image 55](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile55.png>)

![image 56](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile56.png>)

a

Consider an equiangular set X with scalar products {a1,−a1} in Sn−1 and choose an arbitrary point x0 ∈ X. Note that any point in an equiangular set may be changed to its opposite and the set still remains equiangular. Using this procedure we make (y,x0) = a1 hold for all y ∈ X, y = x0. Denote the equiangular set obtained this way by Z. Now we consider the derived set Zx

![image 57](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile57.png>)

![image 58](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile58.png>)

![image 59](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile59.png>)

0,a1 . This is a two-distance set in Sn−2 with scalar products a+11 , a−−11 and |X| − 1 points.

![image 60](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile60.png>)

![image 61](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile61.png>)

![image 62](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile62.png>)

0,a1 there are N1 with scalar product a+11 and N2 with scalar product a−−11. These values should satisfy N(N−1) = N1+N2. By taking the sum of elements from matrices formed by values of Gegenbauer polynomials and

Denote |X|−1 by N and assume that among ordered pairs of points in Zx

![image 63](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile63.png>)

![image 64](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile64.png>)

![image 65](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile65.png>)

applying Proposition 1, we get that G(kn−1)((xi,xj)) ≥ 0, where the sum is taken over all ordered pairs of points in Zx

0,a1 . Taking k = 1,3 we get the following two inequalities

![image 66](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile66.png>)

1 a + 1

N1 + −1 a − 1

N +

N2 ≥ 0 (1) N + −2a − 6

![image 67](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile67.png>)

![image 68](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile68.png>)

N1 + −2a + 6 (a2 − 6)(a − 1)3

N2 ≥ 0 (2)

![image 69](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile69.png>)

![image 70](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile70.png>)

(a2 − 6)(a + 1)3

Taking the ﬁrst inequality with a non-negative coeﬃcient (a2−6)(a+1)16 2(a−1)2 and adding to the second one, we get

![image 71](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile71.png>)

16 (a2 − 6)(a + 1)2(a − 1)2

![image 72](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile72.png>)

N1 + −1 a − 1

1 a + 1

N2 +

N +

![image 73](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile73.png>)

![image 74](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile74.png>)

N1 + −2a + 6 (a2 − 6)(a − 1)3

+ N + −2a − 6 (a2 − 6)(a + 1)3

N2 ≥ 0.

![image 75](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile75.png>)

![image 76](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile76.png>)

+ 1 + (N1 + N2) −2a2 + 10

16 (a2 − 6)(a + 1)2(a − 1)2

N

(a2 − 6)(a + 1)2(a − 1)2 ≥ 0. Since N1 + N2 = N(N − 1) we obtain

![image 77](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile77.png>)

![image 78](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile78.png>)

2a2 − 10 (a2 − 6)(a + 1)2(a − 1)2

16 (a2 − 6)(a + 1)2(a − 1)2

+ 1 ≥ (N − 1)

![image 79](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile79.png>)

![image 80](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile80.png>)

(a2 − 5)(a4 − 3a2 − 2) 2(a2 − 5)

a4 − 3a2 2

16 + (a2 − 6)(a + 1)2(a − 1)2 2a2 − 10

= 1 +

=

.

N ≤ 1 +

![image 81](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile81.png>)

![image 82](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile82.png>)

![image 83](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile83.png>)

2−2)(a2−1)

|X| = N + 1 ≤ a4−23a2 + 1 = (a

2 .

![image 84](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile84.png>)

![image 85](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile85.png>)

![image 86](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile86.png>)

![image 87](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile87.png>)

![image 88](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile88.png>)

![image 89](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile89.png>)

- Remark 1. This proof allows us to get more information on extremal conﬁgurations than the proof in [65]. The upper bound is attained only if both inequalities become equalities and, subsequently, values of N1 and N2 are known exactly and must be the same regardless of the choice of the point x0. We will use this to prove Theorem 4 in Section 6.


## 2.3 Polynomial method

One of the key methods in analyzing sets with few distances is the polynomial method. The main idea is to ﬁnd a set of polynomials nullifying almost all values of the distance function and use the following standard lemma.

- Lemma 2.1. For an arbitrary set X consider a vector space V of functions f : X → F, where F is a ﬁeld. Assume that f1,... ,fm ∈ V , a ﬁnite-dimensional vector subspace of V. Then for any ﬁnite set of elements {x1,... ,xN} ⊆ X, the rank of the matrix (fi(xj)) is at most the dimension of V .


Proof. Any linear dependence of the functions fi is also a linear dependence of the columns of this matrix, so the rank is not greater than the dimension of the space of functions.

![image 90](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile90.png>)

![image 91](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile91.png>)

![image 92](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile92.png>)

![image 93](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile93.png>)

The straightforward application of this method in [23] allows one to prove a general bound on spherical s-distance sets (the so-called absolute bound).

- Theorem 7. The size of an s-distance set in Sn−1 is not greater than n+ss−1 + n+s−s−12

Proof. Suppose X = {x1,... ,xN} is an s-distance set in Sn−1 with the set of scalar products {β1,... ,βs}. Deﬁne polynomials fj(x) = si=1((x,xj) − βi). Matrix (fi(xj)) has non-zero entries on its diagonal and 0 everywhere else. Hence its rank is N. By Lemma 2.1 the rank is no greater than the dimension of the space of spherical polynomials with degree ≤ s which is exactly n+ss−1 +

n+s−2

s−1 . Similarly, we can get the bound on equiangular sets from [44].

![image 94](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile94.png>)

![image 95](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile95.png>)

![image 96](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile96.png>)

![image 97](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile97.png>)

- Theorem 8 (Gerzon’s bound). The size of an equiangular set in Sn−1 is not greater than n(n2+1).


![image 98](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile98.png>)

Proof. Assume X = {x1,... ,xN} is an equiangular set in Sn−1 with scalar products ±α. For each j, deﬁne fj(x) = (x,xj)2 − α2. As in the proof of the previous theorem, the matrix (fi(xj)) has non-zero entries on its diagonal and 0 everywhere else. The rank is N and by Lemma 2.1 it’s not greater than the dimension of the space of polynomials generated by all monomials of degree 2 or 0 which is exactly n+12 .

![image 99](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile99.png>)

![image 100](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile100.png>)

![image 101](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile101.png>)

![image 102](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile102.png>)

Musin [47] showed that the linear span of polynomials ((x,xj)−α)((x,xj)−β) does not contain any monomials of degree 1 if α + β ≥ 0 and, subsequently, generalized Gerzon’s bound to all two-distance sets with scalar products α,β such that α + β ≥ 0.

- Lemma 2.2. The size of a two-distance set in Sn−1 with scalar products α,β such that α + β ≥ 0 is not greater than n(n2+1).

![image 103](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile103.png>)

For the next lemma, suppose X = {x1,... ,xN} is an s-distance set in a metric space M. τ is a distance function and τ(x,x) = τ0 for all x ∈ M. Assume τ admits only real values β1,... ,βs over all ordered pairs of points from X. Let Vs−1 be a linear space of real functions spanned by all fQ,ξ(x) = Q(τ(x,ξ)), where ξ is a ﬁxed point from M and Q is a real polynomial of degree s − 1. Let dim Vs−1 = K.

For each l, 1 ≤ l ≤ s, we can deﬁne the adjacency matrix Φl, where the ij-entry of this matrix is 1 if τ(xi,xj) = βl and 0 otherwise. Denote kl = − i =l

τ0−βi βl−βi.

![image 104](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile104.png>)

The following lemma was essentially proved by Nozaki [50] as the main ingredient in his proof of the generalization of [42].

- Lemma 2.3. If the size of X is at least K, then for each l, 1 ≤ l ≤ s, kl is an eigenvalue of the adjacency matrix Φl with multiplicity at least |X| − K. Proof. Deﬁne functions fjl(x) = i =l τ(x,xβ j)−βi

![image 105](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile105.png>)

l−βi . fjl(xi) may take only three diﬀerent values: if i = j then fil(xi) = i =l τβ0−βi

![image 106](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile106.png>)

l−βi = −kl; if i = j and τ(xi,xj) = βl then fil(xi) = 1; if i = j and τ(xi,xj) = βl then fil(xi) = 0. Hence, for a ﬁxed l, matrix fil(xi) is −klI + Φl. By Lemma 2.1 the rank of this matrix is not greater than K and, therefore, 0 is the eigenvalue of −klI + Φl with multiplicity at least |X| −K. From here we conclude that Φl has eigenvalue kl with multiplicity at least |X| − K.

![image 107](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile107.png>)

![image 108](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile108.png>)

![image 109](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile109.png>)

![image 110](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile110.png>)

Using this lemma, it is not hard to prove that M1

![image 111](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile111.png>)

a

(n) > 2n+2 implies that a is an odd natural number. Dimension K in this scenario is n + 1 and the eigenvalue 1+

1 a

![image 112](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile112.png>)

![image 113](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile113.png>)

1

![image 114](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile114.png>)

a+a1 = a+12 will be a root of multiplicity ≥ |X| − (n + 1) > 21|X| of the characteristic polynomial of the adjacency matrix Φ. This polynomial has degree |X| and integer coeﬃcients. Any algebraic conjugate of a+12 must be a root of this polynomial with the same multiplicity but it would make the total degree greater than |X|. Hence there are no algebraically conjugate numbers and a+12 is integer. Proving the same condition with the assumption M1

![image 115](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile115.png>)

![image 116](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile116.png>)

![image 117](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile117.png>)

![image 118](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile118.png>)

![image 119](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile119.png>)

![image 120](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile120.png>)

a

(n) > 2n as in [44] takes a little more eﬀort. The numbers kl from Lemma 2.3 satisfy the following useful properties (see [48, Theorem 2.6]).

- Lemma 2.4. For any real polynomial P of degree ≤ s − 1, P(τ0) + sl=1 klP(βl) = 0.


Proof. The polynomial P(x) − sl=1 i =l

x−βi βl−βiP(βl) is 0 at all βi. Since P has s roots, it must be

![image 121](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile121.png>)

identically 0 and, in particular, must be 0 at τ0.

![image 122](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile122.png>)

![image 123](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile123.png>)

![image 124](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile124.png>)

![image 125](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile125.png>)

- Lemma 2.5. τ0s + sl=1 klβls = sl=1(τ0 − βl).


Proof. The polynomial xs − sl=1 i =l

x−βi βl−βiβls is 0 at all βi. Since this polynomial has s roots and

![image 126](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile126.png>)

its leading coeﬃcient is 1, it must be the product of all x − βl. Particularly, at τ0 it must be the product of all τ0 − βl.

![image 127](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile127.png>)

![image 128](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile128.png>)

![image 129](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile129.png>)

![image 130](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile130.png>)

# 3 General bound for s-distance sets

In this section we derive a new general method to ﬁnd upper bounds on the size of s-distance sets in compact two-point homogeneous spaces. Our setup is similar to the one for Lemma 2.3. We assume that X = {x1,... ,xN} is an s-distance set in a compact two-point homogeneous metric space M equipped with a distance function τ(x,y), τ(x,x) = τ0, and zonal spherical functions Pk(t) as described in Subsection 2.1. Assume τ admits only values {β1,... ,βs} on pairs of points from X. For each l, Φl is an adjacency matrix for βl.

- Theorem 9. Let X be an s-distance set in M, s ≥ 2, and let the distance function τ admit only values {β1,... ,βs} on pairs of points from X. Let K be the dimension of a linear space of real functions spanned by all fQ,ξ(x) = Q(τ(x,ξ)), where ξ is a ﬁxed point from M and Q is a real


τ0−βi βl−βi. Assume |X| > 1 + K(s − 1) and let P(t)

polynomial of degree s − 1. Denote kl = − i =l

![image 131](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile131.png>)

be any non-negative linear combination of zonal spherical functions Pk(t) of the compact two-point homogeneous space M. Then

0 ≤ (|X| − 1 − K(s − 1))(P(τ0) + P(β1)k1 + ... + P(βs)ks) ≤ |X|P(τ0).

Proof. By Lemma 2.3, kl is an eigenvalue of the adjacency matrix Φl for βl and its multiplicity is at least |X| − K. For each l denote the eigenspace of Φl corresponding to kl by Sl and the eigenspace of J (matrix of all 1’s) corresponding to 0 by S0. We consider the intersection S = S0∩S1 ...∩Ss−1. Its codimension is not greater than the sum of codimensions of S0, ..., Ss−1, hence it’s not greater than 1 +K(s −1). Therefore, its dimension is at least |X| −K(s −1) −1. Any vector from S is an eigenvector of Φi, 1 ≤ i ≤ s − 1, with the eigenvalue ki, an eigenvector of J with eigenvalue 0, and an eigenvector of I with eigenvalue 1. From the condition on matrices I + Φ1 + ... + Φs = J, we get that any vector of S is also an eigenvector of Φs with the eigenvalue −1 − k1 − ... − ks−1. By Lemma 2.4 for degree 0, this eigenvalue is equal to ks. Therefore, any vector from S belongs to Ss

- as well. The Gram matrix of X is G = I + β1Φ1 + ... + βsΦs. For a real polynomial P, denote


P(G) := P(τ0)I + P(β1)Φ1 + ... + P(βs)Φs. Note that if vector v is in S, then

P(G)v = (P(τ0) + P(β1)k1 + ... + P(βs)ks)v.

Hence any vector v ∈ S is an eigenvector of P(G) with the eigenvalue P(τ0) + P(β1)k1 + ... + P(βs)ks. Therefore, the multiplicity m of this eigenvalue of P(G) is at least |X| − 1 − K(s − 1).

If P is any non-negative linear combination of zonal spherical functions, then P(G) 0. Then any eigenvalue of P(G) is a non-negative real number which proves the ﬁrst inequality in the statement of the theorem. The sum of eigenvalues of P(G) equals tr(P(G)) = |X|P(τ0) and, since all eigenvalues are non-negative,

|X|P(τ0) ≥ m(P(τ0) + P(β1)k1 + ... + P(βs)ks) ≥

≥ (|X| − 1 − K(s − 1))(P(τ0) + P(β1)k1 + ... + P(βs)ks) which proves the second inequality of the theorem.

![image 132](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile132.png>)

![image 133](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile133.png>)

![image 134](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile134.png>)

![image 135](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile135.png>)

- Remark 2. By a regular s-distance set we mean an s-distance set such that the distribution of distances from any point of this set is the same. The result of Theorem 1 and all subsequent corollaries may be improved if the set is known to be regular. In this case, S1 ... ∩ Ss−1 already is a subset of S0 and the codimension will be no greater than K(s − 1). Numerators in all bounds of Corollaries 2-4 will be smaller by one with this condition.


For the next statement we assume that Ps(t) is a real polynomial of degree s and use it in Theorem 9. Let the highest degree coeﬃcient of Ps(t) be cs.

- Corollary 2. With the notation used for Theorem 9,


1 + K(s − 1) 1 −

|X| ≤

,

![image 136](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile136.png>)

Ps(τ0) cs sl=1(τ0 − βl)

![image 137](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile137.png>)

if |X| > 1 + K(s − 1) and the right hand side of the inequality is positive. Proof. We can write Ps(t) = csts + Q(t), where Q has degree ≤ s − 1. Then

s

s

klβls) + (Q(τ0) +

(P(τ0) + P(β1)k1 + ... + P(βs)ks) = cs(τ0s +

klQ(βl)).

l=1

l=1

By Lemmas 2.4 and 2.5, this is equal to cs sl=1(τ0 − βl). Due to the ﬁrst inequality from

- Theorem 9 this value is positive. To ﬁnish the proof we transform the second inequality from Theorem 9:


s

1 + K(s − 1) |X|

cs

(τ0 − βl) ≤ P(τ0),

1 −

![image 138](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile138.png>)

l=1

1 + K(s − 1) |X|

P(τ0) cs sl=1(τ0 − βl) ≤

,

1 −

![image 139](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile139.png>)

![image 140](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile140.png>)

1 + K(s − 1) 1 −

.

|X| ≤

![image 141](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile141.png>)

Ps(τ0) cs sl=1(τ0 − βl)

![image 142](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile142.png>)

![image 143](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile143.png>)

![image 144](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile144.png>)

![image 145](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile145.png>)

![image 146](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile146.png>)

# 4 Upper bounds for two-distance sets

## 4.1 General spherical bounds

In this section we show how to obtain new upper bounds for spherical two-distance sets. Firstly, we rewrite Corollary 2 for the speciﬁc case of spherical sets.

Corollary 3. Let X be a spherical s-distance set in Sn−1 with scalar products β1,... ,βs. Then

1 + n+s−s−12 + n+s−s−23 (s − 1) 1 −

|X| ≤

,

![image 147](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile147.png>)

1

![image 148](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile148.png>)

s i=2

s l=1(1 − βl)

n+2i−4 n+i−3

![image 149](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile149.png>)

if the right hand side is positive.

Proof. For the spherical case τ(x,y) = (x,y) so τ0 = 1. The leading coeﬃcient of the normalized Gegenbauer polynomial of degree s is precisely si=2 nn+2+ii−−34. Finally, the space of spherical polynomials of degree ≤ s − 1 has dimension n+s−s−12 + n+s−s−23 . The corollary is then obtained by substituting these values in Corollary 2. In this case the denominator in the inequality is always less than 1 so it works even when |X| ≤ 1 + n+s−s−12 + n+s−s−23 (s − 1).

![image 150](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile150.png>)

![image 151](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile151.png>)

![image 152](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile152.png>)

![image 153](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile153.png>)

![image 154](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile154.png>)

By taking s = 2 we get the result for two-distance sets. Corollary 4. Let X be a spherical two-distance set in Sn−1 with scalar products α,β. Then |X| ≤

n + 2 1 − n(1−nα−)(11 −β)

,

![image 155](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile155.png>)

![image 156](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile156.png>)

if the right hand side is positive.

## 4.2 Bounds for equiangular sets

In this subsecton we assume that X is an equiangular set in Sn−1 with scalar products α = a1,β = −a1. Using Corollary 4 in a straightforward manner will not bring any new bounds for equiangular sets. In fact, we can only get |X| ≤ (n+2)n(1−α

![image 157](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile157.png>)

![image 158](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile158.png>)

2)

1−nα2 , which is worse than the relative bound from Theorem 5. The trick here is to consider derived sets and apply the bound to them.

![image 159](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile159.png>)

- Theorem 10. For any a ≥ 3,


n2a2 + n − 2 n + a2 − 2

< na2.

M1

(n) ≤

![image 160](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile160.png>)

![image 161](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile161.png>)

a

Proof. Just like in the proof of Theorem 6, we choose an arbitrary point x0 ∈ X and change some points of X to their opposites so that (y,x0) = a1 for all y ∈ X, y = x0. We denote the resulting equiangular set by Z and consider the derived set Zx

![image 162](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile162.png>)

0,a1 . This is a two-distance set in Sn−2 with scalar products a+11 and a−−11. By Corollary 4,

![image 163](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile163.png>)

![image 164](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile164.png>)

![image 165](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile165.png>)

(n2 − 1)a2 n + a2 − 2

n + 1 1 − (n−(n2)(−1)a2a−2 1)

n + 1 1 − (n−1)(1−n−1 2

.

=

=

|Zx

0,a1 | ≤

![image 166](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile166.png>)

![image 167](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile167.png>)

![image 168](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile168.png>)

![image 169](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile169.png>)

![image 170](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile170.png>)

a+1)(1+a−11)

![image 171](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile171.png>)

![image 172](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile172.png>)

![image 173](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile173.png>)

(n2 − 1)a2 n + a2 − 2

+ 1 =

0,a1 | + 1 ≤

|X| = |Zx

![image 174](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile174.png>)

![image 175](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile175.png>)

n2a2 + n − 2 n + a2 − 2

<

![image 176](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile176.png>)

n2a2 + na2(a2 − 2) n + a2 − 2

= na2.

![image 177](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile177.png>)

![image 178](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile178.png>)

![image 179](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile179.png>)

![image 180](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile180.png>)

![image 181](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile181.png>)

When n ∼ a2, the bound in this theorem is asymptotically the same as Gerzon’s bound, i.e.

∼ 12n2. The reason why this bound cannot be precise for the cases when Gerzon’s bound is attained lies in the proof of Theorem 9. Conﬁgurations where Gerzon’s bound is attained are known to be

![image 182](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile182.png>)

determined by regular graphs so, as we mentioned in Remark 2, we should use codimension ≤ n+1 instead of n + 2 which eventually ended up in the numerator of Corollary 4. Using this corollary with the additional condition of regularity would lead to the very same Gerzon bound for n = a2−2.

When n ≫ a2, it makes sense to use the upper bound na2. For the size of equiangular sets with prescribed scalar products, the ﬁrst bound linear in n was proved in [17] and it was asymptotically ≤ cn, where c = 2O(a2). The bound from [5] is much better, 1.93n unless a = 3 for which it was already known to be 2n − 2 [44], but this bound holds only for suﬃciently large n. Essentially our

bound ﬁlls the gap between Gerzon’s bounds n(n2+1), when n is really close to a2, and 1.93n, when n is suﬃciently large with respect to a2.

![image 183](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile183.png>)

The na2 bound of Theorem 10 can be improved by a more careful analysis of derived sets.

- Theorem 3.


M1

(n) ≤ n

![image 184](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile184.png>)

a

4 7

- 2

![image 185](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile185.png>)

- 3


a2 +

![image 186](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile186.png>)

+ 2, for all a ≥ 3 and for all n ∈ N.

Proof. We consider the set T := Z1 a,x0 from the proof of Theorem 6. It is a two-distance set in

![image 187](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile187.png>)

Sn−2 with |X| − 1 points and scalar products a+11 and a−−11. Choose an arbitrary vertex x00 in this set. The remaining vertices are split into two sets depending on the scalar product with respect to

![image 188](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile188.png>)

![image 189](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile189.png>)

a−1,x00.

x00. Consider the derived sets T1 = T 1

a+1,x00 and T2 = T −1

![image 190](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile190.png>)

![image 191](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile191.png>)

- T1 is a two-distance set in Sn−3 with scalar products a+21 and −(a−a1)(+3a+2). Applying Corollary

![image 192](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile192.png>)

![image 193](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile193.png>)

4 to T1, we get that

|T1| ≤

n 1 − (n−2)(1− 1 n−3

![image 194](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile194.png>)

![image 195](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile195.png>)

![image 196](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile196.png>)

a+2)(1+(a−a1)(+3a+2))

![image 197](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile197.png>)

=

n 1 − n−3

![image 198](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile198.png>)

![image 199](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile199.png>)

(n−2) 1+(a−31)(a+5a+2)2

![image 200](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile200.png>)

=

=

n(n − 2) 1 + (a−1)(3a+5a+2)2 1 + (n − 2)(a−1)(3a+5a+2)2

![image 201](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile201.png>)

![image 202](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile202.png>)

![image 203](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile203.png>)

=

n 1 + (a−31)(a+5a+2)2

![image 204](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile204.png>)

![image 205](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile205.png>)

1

![image 206](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile206.png>)

n−2 + (a−31)(a+5a+2)2

![image 207](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile207.png>)

, (3)

which is strictly smaller than

n 1 + (a−1)(3a+5a+2)2

![image 208](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile208.png>)

![image 209](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile209.png>)

3a+5 (a−1)(a+2)2

![image 210](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile210.png>)

= n

(a − 1)(a + 2)2 3a + 5

![image 211](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile211.png>)

+ 1 .

- T2 is a two-distance set in Sn−3 with scalar products −a−12 and (a+1)(a−a3−2). By Corollary 4 for


![image 212](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile212.png>)

![image 213](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile213.png>)

T2 and calculations similar to those for T1,

n(n − 2) 1 + (a+1)(3a−a5−2)2 1 + (n − 2)(a+1)(3a−a−5 2)2

![image 214](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile214.png>)

=

|T2| ≤

![image 215](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile215.png>)

![image 216](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile216.png>)

n 1 + (a+1)(3a−a−5 2)2

![image 217](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile217.png>)

, (4)

![image 218](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile218.png>)

1

n−2 + (a+1)(3a−a−5 2)2

![image 219](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile219.png>)

![image 220](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile220.png>)

which is strictly smaller than

(a + 1)(a − 2)2 3a − 5

n

+ 1 . Combining these two inequalities and taking into account points x0 and x00, we get that |X| ≤ n

![image 221](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile221.png>)

(a + 1)(a − 2)2 3a − 5

(a − 1)(a + 2)2 3a + 5

- 2

![image 222](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile222.png>)

- 3


4 7

a2 +

+

+ 2 + 2 ≤ n

+ 2,

![image 223](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile223.png>)

![image 224](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile224.png>)

![image 225](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile225.png>)

2

2

since (a−1)(a+2)

3a+5 + (a+1)(a−2)

3a−5 + 2 − 23a2 is a strictly decreasing function for a ≥ 3 and its value

![image 226](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile226.png>)

![image 227](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile227.png>)

![image 228](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile228.png>)

- at 3 is 74.


![image 229](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile229.png>)

![image 230](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile230.png>)

![image 231](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile231.png>)

![image 232](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile232.png>)

![image 233](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile233.png>)

The bound of Theorem 3 is usually better than SDP bounds in [15] and [41] when a is relatively small compared to n. For instance, using inequalities (3) and (4) from the proof of Theorem 3 we can prove the upper bound of 2224 for M1

(137) which is much better than the SDP bound of 9529 from [15] and the bound of 6743 for M1

![image 234](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile234.png>)

5

(400) which is signiﬁcantly better than 17595 from [41].

![image 235](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile235.png>)

5

The choice of a new vertex and split of the set into two two-distance subsets of smaller dimension may be done any number of times. By iterating this process l times, i.e. choosing l arbitrary points in T and dividing all other vertices into 2l groups depending on their distances to the chosen vertices, we can get asymptotically (n/a → ∞) the upper bound ∼ 2l2+1l na2 which is optimal for l = 1.

![image 236](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile236.png>)

# 5 Proof of Theorems 1 and 2

Theorem 2. If n ≥ 359, then

(a2 − 2)(a2 − 1) 2

, where a is the unique positive odd integer such that a2 − 2 ≤ n ≤ (a + 2)2 − 3. Proof. Since 359 = 192 − 2, a ≥ 19. Assume M(n) = M1

M(n) ≤

![image 237](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile237.png>)

(n). If b is not an odd natural number,

![image 238](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile238.png>)

b

2−2)(a2−1)

- M(n) ≤ 2n ≤ 2((a + 2)2 − 3) < (a


2 for all suitable a. There are three possible cases for b.

![image 239](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile239.png>)

- 1. b2 − 2 ≤ n ≤ 3b2 − 16. In this case b ≤ a because a is the largest odd integer such that a2 − 2 ≤ n. By Theorem 6,

M1

![image 240](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile240.png>)

b

(n) ≤

(b2 − 2)(b2 − 1) 2 ≤

![image 241](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile241.png>)

(a2 − 2)(a2 − 1) 2

![image 242](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile242.png>)

.

- 2. n ≤ b2 − 3. By Theorem 5 (relative bound), M1


2−1)

(n) ≤ n(b

b2−n . In this case, b ≥ a + 2 and among all possible values b = a + 2 maximizes n(b

![image 243](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile243.png>)

![image 244](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile244.png>)

b

2−1)

2−1)

(n) ≤ n((a+2)

(a+2)2−n . With respect to n, this value is maximal when n = (a + 2)2 − 3. Therefore,

b2−n so M1

![image 245](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile245.png>)

![image 246](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile246.png>)

![image 247](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile247.png>)

b

(a2 − 2)(a2 − 1) 2 for all a ≥ 19.

((a + 2)2 − 3)((a + 2)2 − 1) 3

M1

<

(n) ≤

![image 248](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile248.png>)

![image 249](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile249.png>)

![image 250](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile250.png>)

b

- 3. n ≥ 3b2 − 15. By Theorem 3,


M1

(n) ≤ n

![image 251](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile251.png>)

b

4 7

- 2

![image 252](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile252.png>)

- 3


b2 +

![image 253](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile253.png>)

+ 2 ≤ n

n + 15 3

4 7

- 2

![image 254](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile254.png>)

- 3 ·


+

![image 255](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile255.png>)

![image 256](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile256.png>)

14n2 + 246n + 126 63 ≤

+ 2 =

![image 257](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile257.png>)

(a2 − 2)(a2 − 1) 2 for all a ≥ 19.

14((a + 2)2 − 3)2 + 246((a + 2)2 − 3) + 126 63

<

≤

![image 258](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile258.png>)

![image 259](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile259.png>)

![image 260](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile260.png>)

![image 261](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile261.png>)

![image 262](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile262.png>)

![image 263](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile263.png>)

Theorem 1.

n(n + 1) 2

g(n) =

![image 264](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile264.png>)

for all n ≥ 7 with possible exceptions for some n = (2k + 1)2 − 3, k ∈ N.

Proof. We will use the following observation made in [23]. If X = {x1,... ,xN} is a spherical twodistance set in Sn−1 with scalar products α and β such that α+β < 0, then there is an equiangular set of the same size in Sn. For the construction of this set consider a unit vector y orthogonal to all xi. Then for any t ∈ [0,1], the set of points txi + √1 − t2y is a set in Sn with only two scalar products t2α+(1−t2) and t2β +(1−t2). The sum of these scalar products is t2(α+β)+2(1−t2), which is negative at t = 1 and positive at t = 0. Hence there is t, where this sum is 0 and the set is equiangular.

![image 265](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile265.png>)

Therefore, if X is a two-distance set with α + β < 0 in Sn−1, its size cannot be larger than

- M(n + 1). For n ≥ 358, using Theorem 2 we get that, unless n + 1 = a2 − 2 for some odd a,


- M(n + 1) ≤ n(n2+1). The statement of the theorem is true for n < 359 due to computations in [41] and the same observation (see [65] for details).


![image 266](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile266.png>)

Finally, the case when α + β ≥ 0 is covered for all dimensions by Lemma 2.2.

![image 267](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile267.png>)

![image 268](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile268.png>)

![image 269](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile269.png>)

![image 270](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile270.png>)

# 6 Extremal equiangular sets

In this section we analyze what equiangular sets attain the bound of Theorem 2. In order to prove Theorem 4 we will need the deﬁnition of a strongly regular graph and its basic properties.

By a strongly regular graph with parameters (v,k,λ,µ) we mean a regular simple graph with v vertices and degree k such that every two connected vertices have exactly λ common neighbors and every two non-connected vertices have exactly µ common neighbors. If Φ is an incidence matrix of such strongly regular graph, then, from the deﬁnition of a strongly regular graph, Φ2 = kI+λΦ+µ(J−I−Φ). Vector 1 of all 1’s is an eigenvector of Φ with eigenvalue k so from this matrix equality multiplied by 1 we get that parameters are not independent: k2 = k + λk + µ(v − 1 − k). All other eigenvectors of Φ must be orthogonal to 1 so they are annihilated by J and all other eigenvalues must satisfy e2 = k + λe + µ(−1 − e). Unless µ = 0 (the case of a disjoint union of complete graphs with k + 1 vertices each), e cannot be the same as k so the eigenspace for k is one-dimensional. Two other eigenvalues e1 and e2 may be found from the quadratic equation above. Dimensions of their respective eigenspaces must satisfy equation 1+d1+d2 = v for the total dimension and k + d1e1 + d2e2 = 0 for the trace of Φ which can allow one to ﬁnd the dimensions precisely.

- Theorem 4. For each odd natural number a ≥ 3, if n ≤ 3a2−16, then the equiangular set X ⊂ Sn−1


2−2)(a2−1)

with scalar products a1,−a1 and exactly (a

2 points must belong to an (a2 − 2)-dimensional subspace.

![image 271](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile271.png>)

![image 272](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile272.png>)

![image 273](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile273.png>)

Proof. We continue with the same notation as in the proof of Theorem 6. X is an equiangular set in Sn−1 with scalar products {a1,−a1}. An arbitrary point x0 ∈ X was chosen and some points of X were switched to their opposite so that (y,x0) = a1 for all y ∈ X. The set obtained this way was called Z and we considered the derived set Zx

![image 274](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile274.png>)

![image 275](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile275.png>)

![image 276](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile276.png>)

0,a1 . This is a two-distance set in Sn−2 with scalar products a+11 , a−−11 and |X| −1 points. We denoted |X| −1 by N and assumed that among ordered pairs of points in Zx

![image 277](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile277.png>)

![image 278](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile278.png>)

![image 279](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile279.png>)

0,a1 there are N1 with scalar product a+11 and N2 with scalar product a−−11. Consider a graph G on N vertices in Z1

![image 280](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile280.png>)

![image 281](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile281.png>)

![image 282](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile282.png>)

a,x0 such that two vertices x and y form an edge if and only if (x,y) = a+11 . Our goal is to show that this graph is a strongly regular graph.

![image 283](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile283.png>)

![image 284](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile284.png>)

2−3)a2

At the moment from the proof of Theorem 6 we know that N = (a

2 and inequalities used in the proof must become equalities since the bound is attained. Therefore, numbers N1 (twice the number of edges in G) and N2 (twice the number of non-edges in G) may be found precisely: N1 = (a+1)N2a(N−a), N2 = N(N − 1) − N1.

![image 285](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile285.png>)

![image 286](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile286.png>)

The main observation under the proof is that we can choose any vertex of the set X for x0. Depending on a vertex taken we can get diﬀerent graphs. It follows from the proof of Theorem 6 that all these graphs must have the same number of edges.

First, let us analyze how the graph is changed when the initial vertex for switching is changed. Assume we take another point x, associated with vertex u in G, and make a derived set using x instead of x0. Denote by N(u) the set of neighbors of u in G and denote by N′(u) the set of non-neighbors. In the equiangular set Z, the set of points having scalar product a1 with x consists of x0 and points corresponding to N(u) and the set of points having scalar product −a1 with x consists of points corresponding to N′(u). Therefore, we need to switch all points for N′(u) to their opposites. After this operation, x0 has scalar products of a1 with x and points for N(u) and has scalar products of −a1 with points for N′(u). All scalar products between N(u) and N′(u) changed their signs.

![image 287](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile287.png>)

![image 288](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile288.png>)

![image 289](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile289.png>)

![image 290](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile290.png>)

When constructing a new graph G′ we should delete the vertex u, introduce a new vertex u′ corresponding to the point x which is connected to all vertices in N(u) and not connected to any vertex in N′(u), and swap edges and non-edges between N(u) and N′(u). Note that the new vertex

- u′ has the same adjacencies as the old vertex u so essentially G′ is the graph G in which edges and non-edges between N(u) and N′(u) were swapped.


Denote by k the degree of u. Just as G, the graph G′ must have exactly N1/2 edges. The number of edges between N(u) and N′(u) may not change by swapping edges and non-edges so it must be exactly k(N − 1 − k)/2.

a,x0 and, similarly to the proof of Theorem 3, consider two-distance derived sets T1 = T 1

Denote T := Z1

![image 291](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile291.png>)

a−1,x. T1 is a two-distance set with k points and scalar products a+21 and −(a−a1)(+3a+2). Denote by t1 and t2 the numbers of ordered pairs of points in T1 such that their scalar products are a+21 and −(a−a1)(+3a+2) respectively. T2 is a two-distance set with N − k − 1 points and scalar products −a−12 and (a+1)(a−a3−2). Denote by t′

a+1,x and T2 = T −1

![image 292](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile292.png>)

![image 293](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile293.png>)

![image 294](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile294.png>)

![image 295](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile295.png>)

![image 296](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile296.png>)

![image 297](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile297.png>)

1 and t′

2 the numbers of ordered pairs of points in T2 such that their scalar products are (a+1)(a−a3−2) and −a−12 respectively. We know that N1 = 2k +t1 +t′1 +k(N −k −1) (the degree of u is counted twice and the number of pairs between

![image 298](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile298.png>)

![image 299](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile299.png>)

![image 300](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile300.png>)

![image 301](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile301.png>)

- N(u) and N′(u) is exactly k(N − 1 − k) as we showed above).


Both for T1 and T2 we can ﬁnd lower bounds on t1 and t′

1 using positive semideﬁniteness of their Gram matrices. For T1 we have

a + 3 (a − 1)(a + 2)

1 a + 2

t2 ≥ 0. Therefore,

t1 + −

t1 + t2 = k(k − 1) and k +

![image 302](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile302.png>)

![image 303](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile303.png>)

Similarly, for T2 we have

k2(a + 3) − k(a + 1)2 2(a + 1)

.

t1 ≥

![image 304](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile304.png>)

a − 3 (a + 1)(a − 2)

1 a − 2

t′1 + t′2 = (N − k − 1)(N − k − 2) and (N − k − 1) +

t′1 + (−

)t′2 ≥ 0.

![image 305](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile305.png>)

![image 306](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile306.png>)

Therefore,

(a + 1)(N − k − 1)(N − k − a) 2(a − 1)

t′1 ≥

.

![image 307](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile307.png>)

From these two inequalities and equality N1 = (a+1)N2a(N−a) we get that

![image 308](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile308.png>)

k2(a + 3) − k(a + 1)2 2(a + 1)

- (a + 1)N(N − a) 2a ≥ 2k +


+

![image 309](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile309.png>)

![image 310](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile310.png>)

Transforming this inequality, we obtain

(a + 1)(N − k − 1)(N − k − a) 2(a − 1)

+ k(N − k − 1).

![image 311](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile311.png>)

2

2a a2 − 1

(N − a)(a + 1) 2a

0 ≥

.

k −

![image 312](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile312.png>)

![image 313](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile313.png>)

We conclude that k must be (N−a2)(aa+1). The choice of point x was arbitrary which means that all vertices in G must have the same degree k and, moreover, all degrees in G′ after swapping edges and non-edges between N(u) and N′(u) must be still the same. This means that from each vertex of N′(u) there are exactly N(u)/2 = k/2 edges to N(u), i.e. any two disconnected vertices of G have exactly k/2 common neighbors. Similarly, for any vertex of N(u) there are exactly

![image 314](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile314.png>)

- N′(u)/2 = (N −k −1)/2 edges to N′(u) which leaves k −1−(N −k −1)/2 = (3k −N −1)/2 edges to other vertices of N(u). This means that any two connected vertices of G must have (3k−N−1)/2


common neighbors. Therefore, G is a strongly regular graph with parameters (N,k, 3k−2N−1, k2).

![image 315](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile315.png>)

![image 316](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile316.png>)

For the remaining part of the proof we employ the fact that adjacency matrices Φ of graph G and J − I − Φ of its complement have the same spectral structure. One of the eigenspaces is the one-dimensional space generated by 1 and the other two eigenspaces have dimensions we can ﬁnd as described above. Using the notation from the beginning of this section, we ﬁnd that e1 = N2−aa with multiplicity d1 = N(a

![image 317](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile317.png>)

2−1)

N+a2 and e2 = −a+12 with multiplicity d2 = NN2+−aa22.

![image 318](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile318.png>)

![image 319](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile319.png>)

![image 320](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile320.png>)

The Gram matrix of Z is I + a+11 Φ+ a−−11(J −I −Φ) and, as the beneﬁt of the spectral structure of Φ, we can ﬁnd all eigenvalues of this matrix with their multiplicities:

![image 321](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile321.png>)

![image 322](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile322.png>)

1 a + 1

k + −1 a − 1

1 a + 1 −

a + 1 2 −

1 a − 1 −1 −

a + 1 2

1 +

(N − k − 1) = 1 +

![image 323](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile323.png>)

![image 324](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile324.png>)

![image 325](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile325.png>)

![image 326](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile326.png>)

![image 327](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile327.png>)

![image 328](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile328.png>)

so 0 is an eigenvalue with multiplicity d2 + 1;

= 0

N + a2

N − a 2a −

1 a − 1 −1 −

N − a 2a

1 a + 1

=

1 +

![image 329](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile329.png>)

![image 330](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile330.png>)

![image 331](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile331.png>)

![image 332](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile332.png>)

![image 333](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile333.png>)

a2 − 1 so this is an eigenvalue of multiplicity d1 = N(a

2−1)

N+a2 . The rank of the Gram matrix is then

![image 334](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile334.png>)

- N(a2−1) N+a2 = a2 −3 so Z belongs to the (a2 −3)-dimensional space. Therefore, the initial equiangular


![image 335](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile335.png>)

set X is (a2 − 2)-dimensional.

![image 336](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile336.png>)

![image 337](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile337.png>)

![image 338](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile338.png>)

![image 339](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile339.png>)

Generally, Theorem 4 claims that, given n ≤ 3a2 − 16, the Gerzon-type bound of Theorem 2 is attainable if and only if the actual Gerzon bound is attainable and, moreover, the extremal set is precisely the set where the Gerzon bound is attained. This may be used to slightly improve upper bounds for the maximum size of an equiangular set in some dimensions. For example, it is known [10] that there is no equiangular set in R47 with 1128 points. Due to Theorem 4, all equiangular sets with 1128 points in dimensions 48-75 must be embeddable in R47 and, therefore, such sets don’t exist either. This means that M(n) ≤ 1127 for all n from 47 to 75. Similarly, M(n) ≤ 3159 for n ∈ [79,116] and M(n) ≤ 14027 for n ∈ [167,221].

2−3)a2 2

- Remark 3. When proving that G is strongly regular, we didn’t use that N is precisely (a


![image 340](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile340.png>)

so this part essentially gives a new self-contained proof for the classiﬁcation of equiangular tight frames and their connection to strongly regular graphs with parameters (N,k, 3k−2N−1, k2) (see, for instance, [61]). For the classiﬁcation of all spherical two-distance tight frames see [13].

![image 341](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile341.png>)

![image 342](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile342.png>)

Corollary 1. Let n ≥ 359 and let a be the unique positive odd integer such that a2 − 2 ≤ n ≤

2−2)(a2−1)

- (a + 2)2 − 3. Suppose that X ⊂ Sn−1 is an equiangular set of size (a


2 . Then X has scalar products a1,−a1 and is contained in an (a2 − 2)-dimensional subspace.

![image 343](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile343.png>)

![image 344](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile344.png>)

![image 345](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile345.png>)

Proof. As in the proof of Theorem 2, assume that the bound is attained on the set with scalar products 1b and −1b. Of the three cases in the proof, only in the ﬁrst it is possible to reach the bound. Hence b2 − 2 ≤ n ≤ 3b2 − 16. Moreover, since M1

![image 346](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile346.png>)

![image 347](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile347.png>)

2−2)(b2−1)

(n) ≤ (b

2 , the bound is attained

![image 348](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile348.png>)

![image 349](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile349.png>)

b

only if b = a, which means that this set must have scalar products a1 and −a1. The second part of the corollary statement automatically follows from Theorem 4.

![image 350](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile350.png>)

![image 351](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile351.png>)

![image 352](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile352.png>)

![image 353](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile353.png>)

![image 354](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile354.png>)

![image 355](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile355.png>)

# 7 Discussion

In this section we would like to list several open questions and our conjectures as well as some general directions for research in this area.

- 1. We proved that maximum spherical n-dimensional two-distance sets, bar a set of exceptional


dimensions, have n(n2+1) points. However, the proof does not give a characterization of all maximal sets. The methods we employ can give a lot of information about two-distance sets

![image 356](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile356.png>)

with scalar products α+β ≤ 0. Unfortunately, the only result for the case α+β > 0 is Musin’s

lemma (Lemma 2.2) which doesn’t provide any insight into extremal cases. We conjecture that for almost all dimensions (the density of exceptional dimensions from 1 to N converges to 0 when N → ∞) the extremal conﬁgurations are natural conﬁgurations of midpoints of the regular simplex. Moreover, we think that, for a ﬁxed natural c, all two-distance spherical conﬁgurations with at least n(n2+1) − c points are subsets of these natural conﬁgurations for almost all dimensions.

![image 357](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile357.png>)

- 2. We conjecture that in each of the exceptional cases, n = (2k +1)2 −3, if there is no spherical two-distance set with n(n2+3) vertices, then the maximal set has n(n2+1) vertices. In other words, there are no intermediate two-distance sets: the extremal set is either a very special set bearing a lot of structural properties (tight spherical design, strongly regular graph, etc) or is simply the set of midpoints of the regular simplex.

![image 358](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile358.png>)

![image 359](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile359.png>)

- 3. The harmonic bound (Theorem 7) may not be attained for any s ≥ 3. This follows from the non-existence of tight spherical 2s-designes for s ≥ 3 [9]. However, no general bounds asymptotically improving the harmonic bound are known. We conjecture that the natural conﬁguration with n+1s points is the maximal s-distance conﬁguration for almost all n.
- 4. Due to the construction of de Caen [18] and Gerzon’s bound, 2

![image 360](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile360.png>)

9 ≤ limsup

n→∞

M(n) n2 ≤

![image 361](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile361.png>)

- 1

![image 362](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile362.png>)

- 2


.

The exact value of this upper limit is an open question. As one of the outcomes of this paper we know that there are no equiangular sets with scalar product a1 of size ∼ n2 if a2 ≪ n. We can adjust the question of ﬁnding the upper limit to the case of all a and, using [5] and Theorem 3, ﬁnd similar bounds for M1

![image 363](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile363.png>)

![image 364](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile364.png>)

a

(n):

1 3 ≤ limsup

![image 365](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile365.png>)

n→∞

max

a

M1

![image 366](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile366.png>)

a

(n) na2 ≤

![image 367](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile367.png>)

- 2

![image 368](<2016-glazyrin-upper-bounds-distance-sets_images/imageFile368.png>)

- 3


.

The lower bound here is also obtained from de Caen’s construction. It will be interesting to ﬁnd this number exactly or improve existing bounds.

- 5. Theorem 4 and Corollary 1 show that in cases where the Gerzon-type bound is attained it is always given by a set in dimension (2k + 1)2 − 2. For each n, it seems reasonable to analyze equiangular sets of dimensions precisely n (not smaller) and deﬁne M∗(n) as the size of a maximal equiangular set of dimension precisely n (not embeddable in Rn−1). One of the consequences of Theorem 4 is that M∗(n) is not monotonous. For example, M∗(21) < M∗(22) and M∗(23) < M∗(22). It will be very interesting to ﬁnd lower bounds on M∗(n). So far it is not even clear that M∗(n) has a quadratic lower bound.


# 8 Acknowledgments

We thank Alexander Barg for his invaluable comments on the text of the paper. Alexey Glazyrin was supported in part by NSF grant DMS-1400876.

# References

- [1] R. Ahlswede and L. H. Khachatrian, The complete nontrivial-intersection theorem for systems of ﬁnite sets, Journal of Combinatorial Theory, Series A, 76, 121–138, 1996.
- [2] N. Alon, L. Babai, and H. Suzuki, Multilinear polynomials and Frankl–Ray-Chaudhuri–Wilson type intersection theorems, Journal of Combinatorial Theory, Series A, 58(2):165–180, 1991.
- [3] L. Babai, H. Snevily, and R. M. Wilson, A new proof of several inequalities on codes and sets, Journal of Combinatorial Theory, Series A, 71(1):146–153, 1995.
- [4] C. Bachoc and F. Vallentin, New upper bounds for kissing numbers from semideﬁnite programming, J. Amer. Math. Soc. 21 (2008), 909–924.
- [5] I. Balla, F. Dr¨xler, P. Keevash, and B. Sudakov, Equiangular lines and spherical codes in Euclidean space available at arXiv:1606:06620.
- [6] E. Bannai and Et. Bannai, A survey on spherical designs and algebraic combinatorics on spheres, Euro. Journal of Comb. Volume 30, Issue 6, August 2009, Pages 1392–1425.
- [7] E. Bannai, E. Bannai, K.T. Kim, W.-H. Yu, and Y. Zhu, More on spherical designs of harmonic index t, preprint available at arXiv:1507.05373.
- [8] E. Bannai, Et. Bannai, and D. Stanton, An upper bound for the cardinality of an s-distance subset in real Euclidean space, II, Combinatorica 3 (1983) 147–152.
- [9] E. Bannai, R. M. Damerell, Tight spherical designs. I, J. Math. Soc. Japan 31 (1979), no. 1, 199–207.
- [10] E. Bannai, A. Munemasa, and B. Venkov, The nonexistence of certain tight spherical designs, Algebra i Analiz, 16 (2004), 1-23.
- [11] E. Bannai, T. Okuda, and M. Tagami, Spherical designs of harmonic index t, J. Approx. Theory, Volume 195, July 2015, 1–18.
- [12] A. Barg and O. Musin, Bounds on sets with few distances, Journal of Combinatorial Theory, Series A, 118, 1465–1474, 2011.
- [13] A. Barg, A. Glazyrin, K. A. Okoudjou, and W.-H. Yu, Finite two-distance tight frames, Linear Algebra and its Applications 475 (2015): 163–175.
- [14] A. Barg and W.-H. Yu, New bounds for spherical two-distance set, Experimental Mathematics, 22 (2013), 187–194.
- [15] A. Barg and W.-H. Yu, New bounds for equiangular lines, Discrete Geometry and Algebraic Combinatorics, A. Barg and O. Musin, Editors, AMS Series: Contemporary Mathematics, vol. 625, 2014, 111–121.
- [16] S. Bochner, Hilbert distances and positive deﬁnite functions, Ann. of Math. (2), 42:647–656, 1941.


- [17] B. Bukh, Bounds on equiangular lines and on related spherical codes, SIAM J. Discrete Math., 30(1), 549–554.
- [18] D. de Caen, Large equiangular sets of lines in Euclidean space, Electron. J. Combin. 7 (2000), Research Paper 55.
- [19] H. Cohn and A. Kumar, Universal optimal distribution of points on spheres, J. Amer. Math. Soc. 20 (2007), 99–148.
- [20] J. H. Conway, A characterisation of Leechs lattice, Invent. Math. 7 (1969), 137–142.
- [21] J. H. Conway, N. J. A. Sloane, Spherical Packings, Lattices and Groups, Springer-Verlag,

(1988).

- [22] P. Delsarte, An algebraic approach to the association schemes of coding theory, Philips Res. Rep. Suppl. 10 (1973), 1–97.
- [23] P. Delsarte, J. M. Goethals, and J. J. Seidel, Spherical codes and designs, Geometriae Dedicata 6 (1977), 363–388.
- [24] M. Deza, P. Erd˝os, and P. Frankl, Intersection properties of systems of ﬁnite sets, Proceedings of the London Mathematical Society(3), 36(2):369–384, 1978.
- [25] M. Deza and P. Frankl. Erd˝os-Ko-Rado theorem—22 years later. SIAM J. Algebraic Discrete Methods, 4(4):419–431, 1983.
- [26] S. J. Einhorn and I.J. Schoenberg, On Euclidean sets having only two distances between points, I-II, Nederl. Akad. Wetensch. Proc. Ser. A. Math. 28 (1966) 479-504.
- [27] P. Erd˝os, On sets of distances of n points, American Mathematical Monthly, 53: 248250, 1946.
- [28] P. Erd˝os, C. Ko, and R. Rado, Intersection theorems for systems of ﬁnite sets, Quart. J. Math. Oxford Ser. (2), 12:313–320, 1961.
- [29] M. Fickus, J. Jasper, D. G. Mixon, J. D. Peterson, C. E. Watson, Equiangular tight frames with centroidal symmetry, to appear in Appl. Comput. Harmon. Anal.
- [30] M. Fickus, D. G. Mixon, J. Jasper, Equiangular tight frames from hyperovals, to appear in IEEE Trans. Inform. Theory.
- [31] P. Frankl, Orthogonal vectors in the n-dimensional cube and codes with missing distances, Combinatorica, 6(3):279–285, 1986.
- [32] P. Frankl and R. M. Wilson, Intersection theorems with geometric consequences, Combinatorica, 1(4):357–368, 1981.
- [33] T.-S. Fu, Erdo˝s-Ko-Rado-type results over Jq(n,d),Hq(n,d) and their designs, Discrete Mathematics, 196(1-3):137–151, 1999.
- [34] C. Godsil and K. Meagher, Erdo˝s-Ko-Rado Theorems: Algebraic Approaches, Cambridge University Press 2015.


- [35] G. Greaves, J. H. Koolen, A. Munemasa, and F. Szo¨ll˝si, Equiangular lines in Euclidean spaces, J. Combin. Theory Ser. A, 138 (2016) 208-235.
- [36] L. Guth and N. H. Katz, On the Erdo˝s distinct distances problem in the plane, Annals of Mathematics, 181 (1): 155190, 2015.
- [37] J. Haantjes, Equilateral point-sets in elliptic two and three-dimensional spaces, Nieuw Arch. Wisk., 22 (1948) 355-362.
- [38] R. B. Holmes and V. I. Paulsen, Optimal frames for erasures,Linear Algebra and its Applications, 377:31–51, 2004.
- [39] J. Jedwab and A. Wiebe, Large sets of complex and real equiangular lines, J. Combin. Theory Ser. A, 134:98–102, 2015.
- [40] G. Kabatyansky, V.I. Levenshtein, Bounds for packings on the sphere and in the space, Probl. Inf. Transm. 14 (1) (1978), 3–25.
- [41] E. King and X. Tang, Computing upper bounds for equiangular lines in Euclidean spaces, preprint available at arXiv:1606:03259.
- [42] D. G. Larman, C. A. Rogers, and J. J. Seidel, On two-distance sets in Euclidean space, Bulletin of the London Mathematical Society, 9.3 (1977): 261–267.
- [43] J. H. van Lint and J.J. Seidel, Equilateral point sets in elliptic geometry Proc. Nedert. Akad. Wetensh. Series 69 (1966), 335–348.
- [44] P. W. H. Lemmens and J. J. Seidel, Equiangular lines, Journal of Algebra 24 (1973), 494–512.
- [45] V.I. Levenshtein, On bounds for packing in n-dimensional Euclidean space, Sov. Math. Dokl. 20(2), 1979, 417–421.
- [46] P. Lisoneˇk, New maximal two-distance sets, Journal of Combinatorial Theory, Series A, 77 (2), 318–338, 1997.
- [47] O. Musin, Spherical two-distance sets, J. Combin. Theory Ser. A, Volume 116, Issue 4, 2009, 988-995.
- [48] O. Musin and H. Nozaki. Bounds on three-and higher-distance sets, European Journal of Combinatorics, 32 (8), 1182–1190, 2011.
- [49] G. Nebe and B. Venkov, On tight spherical designs, Algebra i Analiz, 24(3):163–171, 2012.
- [50] H. Nozaki, A generalization of Larman-Rogers-Seidel’s theorem, Discrete Mathematics, 311

(10): 792–799, 2011.

- [51] A. M. Odlyzko, N. J. A. Sloane, New bounds on the number of unit spheres that can touch a unit sphere in n dimensions, J. Combin. Theory Ser. A 26 (1979), no. 2, 210–214.
- [52] T. Okuda and W.-H. Yu, A new relative bound for equiangular lines and nonexistence of tight spherical designs of harmonic index 4, European J. of Combin. Volume 53, April 2016, 96–103.


- [53] F. Peter and H. Weyl, Die Vollst¨ndigkeit der primitiven Darstellungen einer geschlossenen kontinuierlichen Gruppe, Math. Ann., 97(1):737–755, 1927.
- [54] D. K. Ray-Chaudhuri and R. M. Wilson, On t-designs, Osaka J. Math., 12(3): 737–744, 1975.
- [55] I. J. Schoenberg, Positive deﬁnite functions on spheres, Duke Mathematical Journal, 9(1): 96–108, 1942.
- [56] T. Strohmer and R. W. Heath, Grassmannian frames with applications to coding and communication, Applied and Computational Harmonic Analysis, 14(3): 257–275, 2003.
- [57] M. A. Sustik, J. A. Tropp, I. S. Dhillon, and R. W. Heath, On the existence of equiangular tight frames, Linear Algebra and its Applications, 426(2):619–635, 2007.
- [58] H. Tanaka, The Erdo˝s-Ko-Rado theorem for twisted Grassmann graphs, Combinatorica, 32(6), 735-740, 2012.
- [59] J. J. Thomson, On the Structure of the Atom: an Investigation of the Stability and Periods of Oscillation of a number of Corpuscles arranged at equal intervals around the Circumference of a Circle; with Application of the Results to the Theory of Atomic Structure, Philosophical Magazine Series 6, Volume 7, Number 39, 1904 March, pp. 237–265.
- [60] M. Viazovska, The sphere packing problem in dimension 8, preprint available at arXiv:1603.04246.
- [61] S. Waldron, On the construction of equiangular frames from graphs, Linear Alg. and its Applications 431, no. 11 (2009), 2228–2242.
- [62] H.C. Wang, Two-point homogeneous spaces, Ann. of Math., 55 (1952), 177–191.
- [63] R. M. Wilson, The exact bound in the Erdo˝s-Ko-Rado theorem., Combinatorica, 4(2-3):247– 257, 1984.
- [64] W.-H. Yu, There are no 76 equiangular lines in R19, preprint available at arXiv:1511:08569.
- [65] W.-H. Yu, New bounds for equiangular lines and spherical two-distance sets, preprint available at arXiv:1609.01036.


