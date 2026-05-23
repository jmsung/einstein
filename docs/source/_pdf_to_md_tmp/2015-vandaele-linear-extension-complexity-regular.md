arXiv:1505.08031v2[math.OC]4May2016

On the Linear Extension Complexity of Regular n-gons

Arnaud Vandaele∗ Nicolas Gillis∗ Franc¸ois Glineur†

Abstract

In this paper, we propose new lower and upper bounds on the linear extension complexity of regular n-gons. Our bounds are based on the equivalence between the computation of (i) an extended formulation of size r of a polytope P, and (ii) a rank-r nonnegative factorization of a slack matrix of the polytope P. The lower bound is based on an improved bound for the rectangle covering number (also known as the boolean rank) of the slack matrix of the n-gons. The upper bound is a slight improvement of the result of Fiorini, Rothvoss and Tiwary [Extended Formulations for Polygons, Discrete Comput. Geom. 48(3), pp. 658-668, 2012]. The diﬀerence with their result is twofold: (i) our proof uses a purely algebraic argument while Fiorini et al. used a geometric argument, and (ii) we improve the base case allowing us to reduce their upper bound 2 ⌈log2(n)⌉ by one when 2k−1 < n ≤ 2k−1 + 2k−2 for some integer k. We conjecture that this new upper bound is tight, which is suggested by numerical experiments for small n. Moreover, this improved upper bound allows us to close the gap with the best known lower bound for certain regular n-gons (namely, 9 ≤ n ≤ 13 and 21 ≤ n ≤ 24) hence allowing for the ﬁrst time to determine their extension complexity.

Keywords. nonnegative rank, extension complexity, regular n-gons, nonnegative factorization, boolean rank.

# 1 Introduction

An extended formulation (or extension) for a polytope P is a higher dimensional polyhedron Q such that there exists a linear map π with π(Q) = P. The size of such an extended formulation is deﬁned as the number of facets of the polyhedron Q. The size of the smallest possible extension of P is called the (linear) extension complexity of P and is denoted xc(P). The quantity xc(P) is of great importance since it characterizes the minimum information necessary to represent P. In particular, in combinatorial optimization, it characterizes the minimum size necessary to represent a problem as a linear programming problem (taking P as the convex hull of the set of feasible solutions). Hence although P might have exponentially many facets, Q might have only a few, providing a way to solve linear programs over P much more eﬀectively. An example of such a polytope is the permutahedron, that is, the convex hull of all permutations of the set {1,2,... ,n} with n! vertices and 2n − 2 facetdeﬁning inequalities, that can be represented as the projection of a polyhedron with O(nlog(n)) facets [12].

![image 1](<2015-vandaele-linear-extension-complexity-regular_images/imageFile1.png>)

∗Department of Mathematics and Operational Research, Faculte´ Polytechnique, Universite´ de Mons, Rue de Houdain 9, 7000 Mons, Belgium. Emails: {arnaud.vandaele, nicolas.gillis}@umons.ac.be.

†Universite´ catholique de Louvain, CORE and ICTEAM Institute, B-1348 Louvain-la-Neuve, Belgium; francois.glineur@uclouvain.be.

The characterization of the extension complexity has attracted much interest recently; in particular lower bounds since they provide provable limits of linear programming to solve combinatorial optimization problems; see, e.g., [8]. For example, it was recently shown that the extension complexity of the matching polytope is exponential (in the number of vertices of the graph), answering a longstanding open question whether there exists a polynomial-size linear programming formulation for the matching problem [20] which implies that although it is solvable in polynomial time, the standard formulation cannot be written as a linear program with a polynomial number of inequalities.

Interestingly, most lower bounds for the extension complexity of polytopes are based on a wellknown linear algebra concept: the nonnegative rank. The nonnegative rank of a nonnegative m-by-n matrix M, denoted rank+(M), is the minimum r such that there exist a nonnegative m-by-r matrix U and a nonnegative r-by-n matrix V such that M = UV . The pair (U,V ) is a rank-r nonnegative fatorization of M. The link between the nonnegative rank and the extension complexity of a polytope, a seminal result of Yannakakis [24], goes as follows. Let P be a polytope in dimension d with

- • f facets expressed as linear inequalities aTi x ≤ bi 1 ≤ i ≤ f, and
- • v vertices denoted xj ∈ Rd 1 ≤ j ≤ v.


The slack matrix SP ∈ Rf+×v of P is deﬁned as

SP(i,j) = bi − aTi xj ≥ 0, for all 1 ≤ i ≤ f,1 ≤ j ≤ v. Note that the slack matrix of a polytope is not unique since the inequalities can be scaled, and the rows and columns permuted but this does not inﬂuence its nonnegative rank; see [13] for more details. Note also that rank(SP) = d + 1 if P is full dimensional. Then, we have

rank+(SP) = xc(P).

Moreover any nonnegative factorization (U,V ) ≥ 0 of SP = UV provides an explicit extended formulation for P (with some redundant equalities):

P = {x ∈ Rd | Ax ≤ b} = {x ∈ Rd | Ax + Uy = b and y ≥ 0}, where A ∈ Rf×d with A(i,:) = ai for all i, and b ∈ Rf. For example, the matrix





- 0 1 2 2 1 0

- 0 0 1 2 2 1
- 1 0 0 1 2 2
- 2 1 0 0 1 2 2 2 1 0 0 1


- 1 2 2 1 0 0


S6 =

 

 

is a slack matrix of the regular hexagon (hence it has rank three) and has nonnegative rank equal to ﬁve:





- 0 0 0 1 2
- 0 1 0 0 1






1 2 1 0 0 0

- 0 0 0 1 2 1
- 1 0 0 0 0 1 0 1 0 0 1 0 0 0 1 1 0 0


- 0 1 1 0 0

- 0 0 2 1 0
- 1 0 1 0 0


- 1 0 0 0 1


S6 =

.

 

 

 

 

This implies that the regular hexagon can be described as the projection of a higher dimensional polytope with 5 facets; see Figure 1 for an illustration. In this paper, we focus on the extension complexity of regular n-gons, and in particular on a new upper bound.

5 facets

π

6 facets

Figure 1: Minimum-size extension of the regular hexagon.

Extension complexity of regular n-gons In the remainder of this paper, we denote Sn the slack matrix of the regular n-gon (more precisely, any slack matrix; see Section 2 for a construction), hence rank+(Sn) equals the extension complexity of the regular n-gon; see above. In the following, we describe several bounds for the nonnegative rank, focusing on the slack matrices of regular n-gons.

Lower bounds. There exist several approaches to derive lower bounds for the nonnegative rank, which we classify in three classes:

- • Geometric. Using a counting argument and the facts that (i) any face of a polytope is the projection of a face of its extension, and (ii) any face is an intersection of facets, it can be

shown that rank+(Sn) ≥ ⌈log2(2n + 2)⌉ [12]. Based on a reﬁned geometric counting argument, Gillis and Glineur [10] described a stronger lower bound for the slack matrix of polygons1: the

nonnegative rank r+ = rank+(Sn) of Sn must satisfy n ≤ max

3≤d≤r+−1

min

i=0,1

faces(r+,d − 1,d − 3 + i),

where the quantity faces(v,d,k) is the maximal number of k-faces of a polytope with v vertices in dimension d, attained by cyclic polytopes [18]; see also [25, p.257, Corollary 8.28]. We have

faces(v,d,k − 1) =

d 2

![image 2](<2015-vandaele-linear-extension-complexity-regular_images/imageFile2.png>)

i=0

∗ d − i k − i

+

i k − d + i

v − d − 1 + i i

,

where ∗ denotes a sum where only half of the last term is taken for i = d2 if d is even, and the whole last term is taken for i = ⌊d2⌋ = d−21 if d is odd. This bound can be generalized to any nonnegative matrix [10], but it becomes diﬃcult to compute for non-slack matrices as it requires another quantity that is in general NP-hard to compute (namely, the restricted nonnegative rank, which is always equal to n for the slack matrix of a polytope with n vertices).

![image 3](<2015-vandaele-linear-extension-complexity-regular_images/imageFile3.png>)

![image 4](<2015-vandaele-linear-extension-complexity-regular_images/imageFile4.png>)

![image 5](<2015-vandaele-linear-extension-complexity-regular_images/imageFile5.png>)

- • Combinatorial. These bounds are based on the sparsity pattern of the input matrix. The most well-known one is the rectangle covering bound (RCB) that counts the minimum number of rectangles necessary to cover all positive entries of the matrix, a rectangle being a subset of rows and columns for which the corresponding submatrix contains only positive entries; see [7] and the references therein. Note that the RCB is equal to the boolean rank; see, e.g., [4]. A closely


![image 6](<2015-vandaele-linear-extension-complexity-regular_images/imageFile6.png>)

- 1They actually derived this bound for linear Euclidean distance matrices, but it also applies to the slack matrix of


polygons.

related bound is the reﬁned rectangle covering bound (RRCB) by Oelze, Vandaele, Weltge [19]: in addition to covering every positive entry by a rectangle, the RRCB requires that every 2-by-2 nonsingular submatrix is touched by at least two rectangles (note that the same rectangle can be used twice). For example, the RCB for the matrix

 

 

1 2 0 3 4 5 6 0 7 8 9 0

S9 =

is equal to two while the RRCB is equal to three. In fact, there are only three maximal rectangles (that is, rectangles not contained in any larger rectangle):

 

 

 ,

 

 , and

 ,

1 1 0 0 1 1 0 0 1 1 0 0

1 1 0 1 0 0 0 0 0 0 0 0

- 0 0 0 0
- 1 1 1 0 1 1 1 0


and only two of them are required to cover all positive entries (the last two, which is the unique solution) while three are necessary to touching twice all rank-two positive submatrices (which

4 5 7 8

is tight since this is a 3-by-4 matrix), e.g., the block

touched only once with the RCB solution.

Although these bounds can be rather strong in some cases, they are computationally very expensive, and only work well for matrices with ‘well located’ zero entries. For the slack matrices of the regular n-gons, we could compute them up to n = 13 (for larger n, it would take several weeks of computation with our current formulation).

• Convex Relaxations. Fawzi and Parrilo developed two lower bounds for the nonnegative rank based on a sum-of-squares approximation of the copositive cone [5, 6]. These bounds are very general as they can be computed for any nonnegative matrix; however they are typically weaker than the aforementioned lower bounds, in particular for slack matrices.

These bounds are compared for the regular n-gons on Figure 2. We observe that the best lower bounds are the geometric bound from [10] and the rectangle covering bounds [7, 19] that coincide except for n = 9,13 for which only the RRCB is tight (as it matches the best upper bound; see below).

Upper bounds. Ben-Tal and Nemirovski [3] gave an extension of the regular n-gons when n is a

power of two (n = 2k for some k) with 2log2(n) + 4 facets. They used this construction to approximate the circle with regular n-gons which allowed them to approximate second-order cone programs

with linear programs. This construction was slightly reduced to size 2log2(n) in [11] (again, only for n = 2k). Kaibel and Pashkovich [15, 16] proposed a general construction for arbitrary n of size

2⌈log2(n)⌉ + 2. Fiorini, Rothvoss and Tiwary [9] improved the bound to 2⌈log2(n)⌉, which is, to the best of our knowledge, the best known upper bound for regular n-gons. These last bounds are based on a geometric argument using successive reﬂections to construct the regular n-gon. Note that Shitov [21] proved an upper bound of 67n for the nonnegative rank of any n-by-n rank-three nonnegative matrix, hence is applicable to the slack matrix of polygons.

![image 7](<2015-vandaele-linear-extension-complexity-regular_images/imageFile7.png>)

As shown on Figure 2, prior to our new upper bound, the exact value of rank+(Sn) is not known for most values of n larger than 9 as the best lower and upper bounds do not coincide. Therefore, the exact value of the extension complexity of many regular n-gons is still unknown.

- 3

- 4

- 5

- 6

- 7

- 8

- 9

- 10

- 11

- 12


Shitov [15]

this paper

reflections [6]

Goemans [9]

τ+SOS [3]

ν0+ [2]

geometric [7]

RCB [4]

RRCB [13]

4 8 16 32 64

n

- Figure 2: Comparison of lower and upper bounds for the nonnegative rank of the slack matrices of


regular n-gons, that is, rank+(Sn). (Note that some bounds cannot be computed for all n because of their high computational cost.)

Table 1 also gives the best upper and lower bounds for n up to 20.

![image 8](<2015-vandaele-linear-extension-complexity-regular_images/imageFile8.png>)

![image 9](<2015-vandaele-linear-extension-complexity-regular_images/imageFile9.png>)

![image 10](<2015-vandaele-linear-extension-complexity-regular_images/imageFile10.png>)

![image 11](<2015-vandaele-linear-extension-complexity-regular_images/imageFile11.png>)

n 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 RRCB [19] 5 6 6 7 7 7 7 8 ? ? ? ? ? ? ? ?

![image 12](<2015-vandaele-linear-extension-complexity-regular_images/imageFile12.png>)

![image 13](<2015-vandaele-linear-extension-complexity-regular_images/imageFile13.png>)

![image 14](<2015-vandaele-linear-extension-complexity-regular_images/imageFile14.png>)

![image 15](<2015-vandaele-linear-extension-complexity-regular_images/imageFile15.png>)

![image 16](<2015-vandaele-linear-extension-complexity-regular_images/imageFile16.png>)

![image 17](<2015-vandaele-linear-extension-complexity-regular_images/imageFile17.png>)

![image 18](<2015-vandaele-linear-extension-complexity-regular_images/imageFile18.png>)

![image 19](<2015-vandaele-linear-extension-complexity-regular_images/imageFile19.png>)

geometric [10] 5 6 6 6 7 7 7 7 7 8 8 8 8 8 8 9 Equation (1) 5 6 6 7 7 7 7 8 8 8 8 9 9 9 9 9

![image 20](<2015-vandaele-linear-extension-complexity-regular_images/imageFile20.png>)

![image 21](<2015-vandaele-linear-extension-complexity-regular_images/imageFile21.png>)

![image 22](<2015-vandaele-linear-extension-complexity-regular_images/imageFile22.png>)

![image 23](<2015-vandaele-linear-extension-complexity-regular_images/imageFile23.png>)

![image 24](<2015-vandaele-linear-extension-complexity-regular_images/imageFile24.png>)

Table 1: Comparison of two lower bounds (ﬁrst two rows) and the upper bound from Equation (1) for the nonnegative rank of regular n-gons. Bold indicates the tight bounds, that is, bounds that coincide with the nonnegative rank.

Contribution of the Paper In this paper, our contribution is mainly towfold. First, in Section 3, we derive an improved lower bound for the rectangle covering number r of the slack matrix of regular n-gons. We show that the following relation holds

r − ⌊r/2⌋ r − 1

n ≤

![image 25](<2015-vandaele-linear-extension-complexity-regular_images/imageFile25.png>)

r ⌊r/2⌋

,

which improves over the best known previous relation given by n ≤ ⌊r/ r2⌋ [4]. Although this new lower bound does not improve the best known lower bounds for the nonnegative rank of the slack

matrices of regular n-gons (namely, the RRCB and the geometric bound; see previous paragraph), it is applicable to a broader class of matrices, namely those which have the same sparsity pattern as the slack matrices of n-gons. Moreover, it turns out to be a tight bound for the rectangle covering number, a.k.a. the boolean rank, for some n (comparing it with the upper bound from [1]).

Second, we slightly improve the upper bound of Fiorini, Rothvoss and Tiwary [9]. Although our approach is equivalent to that of Fiorini et al., both being recursive, our proof is rather diﬀerent, being purely algebraic as opposed to their geometric approach. Moreover, we are able to reduce the upper bound by one when 2k−1 < n ≤ 2k−1 + 2k−2 for some k: this is possible by stopping the recursion earlier at a better base case (note that it would be possible to modify the proof of Fiorini et al. to achieve the same bound). We show that for all n ≥ 2,

rank+(Sn) ≤

2⌈log2(n)⌉ − 1 = 2k − 1 for 2k−1 < n ≤ 2k−1 + 2k−2, 2⌈log2(n)⌉ = 2k for 2k−1 + 2k−2 < n ≤ 2k.

(1)

Although the improvement is relatively minor, our numerical experiments strongly suggest that this bound is tight; see the discussion at the end of Section 4. Moreover, our bound allows us to close the gap for several n-gons as it matches the best known lower bound, for 9 ≤ n ≤ 12 our bound implies that rank+(Sn) = 7 and, for 21 ≤ n ≤ 24, that rank+(Sn) = 9; see Figure 2. (Note that, for n = 13, the RRCB was, to the best of our knowledge, never computed prior to this work hence it is also the ﬁrst time rank+(Sn) = 8 is claimed for n = 13.)

The paper is organized as follows. In Section 2, we brieﬂy describe the construction of the slack matrices of regular n-gons. In Section 3, we describe our new improved lower bound for the rectangle covering of these matrices, and, in Section 4, we describe our construction that proves the aforementioned upper bound. Then we discuss some directions for further research and conclude in Section 5.

# 2 The Slack Matrices of Regular n-gons

Let us construct the slack matrices of regular n-gons. Without loss of generality (w.l.o.g.), we use regular n-gons centered at the origin with their vertices located on the unit circle of radius equal to one; see Figure 3 for an illustration with the pentagon. The length s of the facets of the regular n-gon

![image 26](<2015-vandaele-linear-extension-complexity-regular_images/imageFile26.png>)

- Figure 3: Illustration for the construction of the slack matrices of regular n-gons. In this paper, we assume w.l.o.g. that r = 1.


is given by s = 2sin πn . The slack between a facet and the kth vertex (the 0th and (n-1)th being on the considered facet, and counting along the circle in any direction) is equal to:

![image 27](<2015-vandaele-linear-extension-complexity-regular_images/imageFile27.png>)

π n

π n

− cos (2k + 1)

. (2)

ck = cos

![image 28](<2015-vandaele-linear-extension-complexity-regular_images/imageFile28.png>)

![image 29](<2015-vandaele-linear-extension-complexity-regular_images/imageFile29.png>)

By symmetry, (i) our slack matrices of regular n-gons are circulant matrices for which the vector c is translated one element to the right on each row, and (ii) the vector c satisﬁes ck = cn−1−k for all k. For example, for n = 9, we have





0 c1 c2 c3 c4 c3 c2 c1 0 0 0 c1 c2 c3 c4 c3 c2 c1 c1 0 0 c1 c2 c3 c4 c3 c2 c2 c1 0 0 c1 c2 c3 c4 c3 c3 c2 c1 0 0 c1 c2 c3 c4 c4 c3 c2 c1 0 0 c1 c2 c3 c3 c4 c3 c2 c1 0 0 c1 c2 c2 c3 c4 c3 c2 c1 0 0 c1 c1 c2 c3 c4 c3 c2 c1 0 0

. (3)

S9 =

 

 

Note that, to the best of our knowledge, the best known lower (resp. upper) bound for rank+(S9) is 7 (resp. 8). In this paper, we will improve the upper bound to 7 hence proving that rank+(S9) = 7; see Figure 2.

# 3 Lower bound for the boolean rank of Sn

In this section, we improve the lower bound on the boolean rank (or, equivalently, the rectangle covering number) for regular n-gons. On the way, we derive several new interesting results that could be used to derive other bounds.

Let U,V ≥ 0 be an exact nonnegative factorization of M = UV of size r. In this section, we will use the following notation. Let us deﬁne the following subsets of {1,2,... r}, representing the supports of the rows of U and columns of V :

si = {k | Uik = 0} 1 ≤ i ≤ m and tj = {k | Vkj = 0} 1 ≤ j ≤ n. Since Mij = U(i,:)V (:,j), U ≥ 0 and V ≥ 0, we have

Mij = 0 ⇐⇒ sj ∩ tj = ∅. (4)

If si ⊆ sl for some i,l, (4) implies that the sparsity pattern of the ith row of M is contained in the sparsity pattern of the lth row of M (and similarly for the columns). Therefore, if M contains p rows whose sparsity patterns are not contained in one another, there are p subsets from si (1 ≤ i ≤ n) that form a Sperner family of size p, also know as an antichain of size p, which is a family of p sets that are not contained in one another [22]. By symmetry, the same holds for the columns.

## 3.1 Sperner theorem and rectangle covering

Sperner theorems bounds the size of an antichain over r elements. Let us recall this result and a proof that will be useful later.

- Theorem 1. Let S = {s1,s2,... ,sn} be a set of n subsets of {1,2,... ,r}. Let also S be an antichain, that is, no subset in S is contained in another subset in S. Then,


r ⌊r/2⌋

n ≤

, (5) and the bound is tight (take all subsets of size ⌊r/2⌋).

Proof. ([17]) This proof is based on a counting argument using the fact that there are r! permutations of {1,2,... ,r}. Given si ∈ S with k elements, there are k!(r − k)! permutations of {1,2,... ,r} whose ﬁrst k elements are in si. Because the si’s are not contained in one another, the permutations generated for two diﬀerent subsets si and sj cannot coincide (otherwise this would imply that si ⊂ sj or sj ⊂ si). Let us also denote ak the number of sets with k elements contained in S, that is, ak = |{s ∈ S | |s| = k}|, hence n = rk=0 ak. We have

r

akk!(r − k)! ≤ r! .

k=0

Therefore,

n

![image 30](<2015-vandaele-linear-extension-complexity-regular_images/imageFile30.png>)

r ⌊r/2⌋

r

ak r ⌊r/2⌋

=

![image 31](<2015-vandaele-linear-extension-complexity-regular_images/imageFile31.png>)

k=0

≤

r

ak r k

![image 32](<2015-vandaele-linear-extension-complexity-regular_images/imageFile32.png>)

k=0

r

k!(r − k)! r!

ak

=

![image 33](<2015-vandaele-linear-extension-complexity-regular_images/imageFile33.png>)

k=0

≤ 1.

since ⌊r/ r2⌋ ≥ k r for all k. This completes the proof. The above result was used to prove that the rectangle covering of the n-by-n Euclidean distance

![image 34](<2015-vandaele-linear-extension-complexity-regular_images/imageFile34.png>)

![image 35](<2015-vandaele-linear-extension-complexity-regular_images/imageFile35.png>)

![image 36](<2015-vandaele-linear-extension-complexity-regular_images/imageFile36.png>)

![image 37](<2015-vandaele-linear-extension-complexity-regular_images/imageFile37.png>)

matrices (with zeros only the diagonal) is the minimum r such that n ≤ ⌊r/ r2⌋ ; see [2] and the references therein. This result can actually be generalized for any nonnegative matrix.

- Corollary 1 ([4]). Let M be a matrix having p rows or p columns whose sparsity patterns are not contained in one another. Then,

rc(M) ≥ min r

r ⌊r/2⌋

≥ p .

Proof. Let M have p rows with diﬀerent sparsity patterns. As explained in the introduction of this section, this implies that there are p subsets of {1,2,... ,r} corresponding to the sparsity patterns of p rows of U that are not contained in one another. Theorem 1 allows to conclude.

![image 38](<2015-vandaele-linear-extension-complexity-regular_images/imageFile38.png>)

![image 39](<2015-vandaele-linear-extension-complexity-regular_images/imageFile39.png>)

![image 40](<2015-vandaele-linear-extension-complexity-regular_images/imageFile40.png>)

![image 41](<2015-vandaele-linear-extension-complexity-regular_images/imageFile41.png>)

In particular, this result can be applied to the slack matrix of any polytope. In fact, the slack of two diﬀerent vertices cannot be contained in one another, otherwise it would mean that a vertex is the intersection of a subset of the facets intersecting at another vertex. The same holds for two diﬀerent facets by polar duality or a similar argument.

- Corollary 2. Let M be the slack matrix of a polytope with f facets and v vertices. Then,


rc(M) ≥ min r

r ⌊r/2⌋

≥ max(f,v) .

Note that, the results from Corollaries 1 and 2 were already known prior to this work; see, e.g., [14, Cor. 4.13] for a more general result.

In the next section, we apply the same ideas to improve the lower bound for the rectangle covering number of the slack matrices of n-gons.

## 3.2 Improvement for n-gons

Let M be the slack matrix of a n-gons such that Mij = 0 if and only if i = j or i = (j + 1)modn for 1 ≤ i,j ≤ n; see Section 2. To simplify the heavy notation modn, we will assume throughout this section that i = 1 ≡ n + 1 when i represents an index. As before, let UV = M be a nonnegative factorization of size r of M, let si denote the support of the ith row of U (1 ≤ i ≤ n) and tj the support of the jth column of V (1 ≤ j ≤ n). We have Mij = 0 if and only if i = j or i = j + 1, and

Mij = 0 ⇐⇒ si ∩ tj = ∅.

Let us try to characterize the size of the sets S = {s1,s2,... ,sn} and T = {t¯1,t¯2,... ,t¯n} that satisfy the above property, where t¯j denotes the complement of tj.

First, we can assume without loss of generality that ti = si ∪ si+1. In fact, ti = si ∪ si+1 is the largest possible set that does not intersect si ∪ si+1 while having the most intersections with all other sets in S (which is the best possible situation since Mij > 0 for i = j,j + 1).

![image 42](<2015-vandaele-linear-extension-complexity-regular_images/imageFile42.png>)

![image 43](<2015-vandaele-linear-extension-complexity-regular_images/imageFile43.png>)

For the same reason as in Corollary 1, since the rows and columns of M have diﬀerent sparsity patterns, we have that (C1) S = {s1,s2,... ,sn} is an antichain. (C2) T = {s1 ∪ s2,s2 ∪ s3,... ,sn−1 ∪ sn,sn ∪ s1} is an antichain, since taking the complement of all

the sets in an antichain gives another antichain of the same size. (C3) Every set si ⊆ {1,2,... ,r} contains at least one element not in the sets t¯j = sj ∪ sj+1 for j,j + 1 = i, since Mij > 0 for i = j,j + 1.

- Theorem 2. Let S and T satisfy (C1-C3) and r ≥ 2. Then


r − ⌊r/2⌋ r − 1

n ≤

![image 44](<2015-vandaele-linear-extension-complexity-regular_images/imageFile44.png>)

r ⌊r/2⌋

.

Proof. Let us denote ki the number of elements in si, zi the number of additional elements in t¯i compared to si (that is, |t¯i| = ki + zi) and zi′ the number of additional elements in t¯i−1 compared to si (that is, |t¯i−1| = ki + zi′). Following the same argument as in Theorem 1, we have that the number of permutations with the elements of si in the ﬁrst positions is given by ki!(r − ki)!, of t¯i by (ki + zi)!(r − ki − zi)!, and of t¯i−1 by (ki + zi′)!(r − ki − zi′)!. However, between si and t¯i, there are ki!zi!(r − ki − zi)! common permutations (and similarly between si and t¯i−1). Note that these are the only possible repetitions because of (C3). Note also that |t¯i| = ki+zi = ki+1+zi′+1 hence the number of permutations corresponding to t¯i are also equal to 1/2(ki!zi!(r−ki−zi)!+(ki+1!zi+1!(r−ki+1−zi+1)). Counting all permutations corresponding to si and t¯i for 1 ≤ i ≤ n and accounting for the repetitions, we get

n

ki!(r−ki)!+

i=1

- 1

![image 45](<2015-vandaele-linear-extension-complexity-regular_images/imageFile45.png>)

- 2


(ki+zi)!(r−ki−zi)!+

- 1

![image 46](<2015-vandaele-linear-extension-complexity-regular_images/imageFile46.png>)

- 2


(ki+zi′)!(r−ki−zi′)!−ki!zi!(r−ki−zi)!−ki!zi′!(r−ki−zi′)! ≤ r!.

Let us lower bound the left hand side of the above inequality. To do so, we minimize over each term of the sum independently. Noting that zi and zi′ have exactly the same role, we can assume without loss of generality that zi = zi′ at a minimum. Removing the index i for simplicity, we therefore have to evaluate

k!(r − k)! + (k + z)!(r − k − z)! − 2k!z!(r − k − z)!.

min

k≥1,z≥1,k+z≤r

In Appendix A, we show that k∗ = ⌊r/2⌋ and z∗ = 1 is an optimal solution. Therefore, dividing the inequality above by r! and using our lower bound for each term (replacing the ki’s with ⌊r/2⌋ and the zi’s with 1), we obtain



n

 

r ⌊r/2⌋

−1

+

−1⌊r/2⌋ + 1

r ⌊r/2⌋

![image 47](<2015-vandaele-linear-extension-complexity-regular_images/imageFile47.png>)

r − ⌊r/2⌋ (⌊r/2r⌋+1)−1

![image 48](<2015-vandaele-linear-extension-complexity-regular_images/imageFile48.png>)

![image 49](<2015-vandaele-linear-extension-complexity-regular_images/imageFile49.png>)

1 ⌊r/2⌋ + 1

1 − 2

![image 50](<2015-vandaele-linear-extension-complexity-regular_images/imageFile50.png>)



≤ 1.

 

from which we get, after simpliﬁcations, n ≤ r−⌊r−r/12⌋ ⌊r/ r2⌋ . Corollary 3. Let r be the rectangle covering number of the slack matrix of any n-gon for n ≥ 2, then

![image 51](<2015-vandaele-linear-extension-complexity-regular_images/imageFile51.png>)

![image 52](<2015-vandaele-linear-extension-complexity-regular_images/imageFile52.png>)

![image 53](<2015-vandaele-linear-extension-complexity-regular_images/imageFile53.png>)

![image 54](<2015-vandaele-linear-extension-complexity-regular_images/imageFile54.png>)

![image 55](<2015-vandaele-linear-extension-complexity-regular_images/imageFile55.png>)

n ≤

r − ⌊r/2⌋ r − 1

![image 56](<2015-vandaele-linear-extension-complexity-regular_images/imageFile56.png>)

r ⌊r/2⌋

.

Note that the term r−⌊r−r/12⌋ goes to 1/2 when r grows, and we cannot hope to obtain a better bound using our counting argument. In fact, this is the case when there would be no repetitions between the permutations generated from the sets in S and T ; see the proof of Theorem 2.

![image 57](<2015-vandaele-linear-extension-complexity-regular_images/imageFile57.png>)

The bound from the corollary above also applies to the so-called boolean rank, which is the same as the rectangle coreving number. Comparing our bound with the upper bounds computed in [1, p.145] for small n, our bound is tight for n = 2 − 6,8 − 9,13 − 21,24 − 32 (a − b means from a to b, that is, a,a + 1,... ,b), which was not the case of the previous bound (5) which is tight only for n = 2 − 4.

# 4 Explicit nonnegative factorization of slack matrices Sn of regular n-gons

In this section, we construct a nonnegative factorization of Sn in a recursive way. The idea is the following. At the ﬁrst step, a rank-two modiﬁcation of Sn is performed so that the pattern of zero entries of the constructed matrix therefore looks like a cross (see below for an example on S9). This subdivides the matrix into four blocks with a lot of symmetry that implies that the nonnegative rank of one block equals the nonnegative rank of the full matrix. Then, the same scheme is applied to that subblock until the number of columns of the obtained block B is smaller than four, which we factorize with a trivial decomposition B = BI (I being the identity matrix of appropriate dimension).

Before we rigorously prove that our construction works for any n-gon, let us illustrate the idea on the slack matrix of the regular 9-gon form (3). Observe that the entries of the slack matrix on the main diagonal and the diagonal below it are equal to zero. The ﬁrst step of our construction will make a rank-two correction of the slack matrix so that the same pattern appears: we remove a matrix from the 4-by-4 lower left block of S9

   −

  

c4 c3 c2 c1 c3 c4 c3 c2 c2 c3 c4 c3 c1 c2 c3 c4

![image 58](<2015-vandaele-linear-extension-complexity-regular_images/imageFile58.png>)

![image 59](<2015-vandaele-linear-extension-complexity-regular_images/imageFile59.png>)

![image 60](<2015-vandaele-linear-extension-complexity-regular_images/imageFile60.png>)

![image 61](<2015-vandaele-linear-extension-complexity-regular_images/imageFile61.png>)

![image 62](<2015-vandaele-linear-extension-complexity-regular_images/imageFile62.png>)

![image 63](<2015-vandaele-linear-extension-complexity-regular_images/imageFile63.png>)

![image 64](<2015-vandaele-linear-extension-complexity-regular_images/imageFile64.png>)

   =

  

c4 − c3 c3 − c2 c2 − c1 c1 c3 − c2 c4 − c1 c3 c2 c2 − c1 c3 c4 c3 − c1

![image 65](<2015-vandaele-linear-extension-complexity-regular_images/imageFile65.png>)

![image 66](<2015-vandaele-linear-extension-complexity-regular_images/imageFile66.png>)

![image 67](<2015-vandaele-linear-extension-complexity-regular_images/imageFile67.png>)

![image 68](<2015-vandaele-linear-extension-complexity-regular_images/imageFile68.png>)

![image 69](<2015-vandaele-linear-extension-complexity-regular_images/imageFile69.png>)

c1 c2 c3 − c1 c4 − c2

![image 70](<2015-vandaele-linear-extension-complexity-regular_images/imageFile70.png>)

![image 71](<2015-vandaele-linear-extension-complexity-regular_images/imageFile71.png>)

  ,

  

c3 c2 c1 0 c2 c1 0 0 c1 0 0 c1 0 0 c1 c2

![image 72](<2015-vandaele-linear-extension-complexity-regular_images/imageFile72.png>)

![image 73](<2015-vandaele-linear-extension-complexity-regular_images/imageFile73.png>)

![image 74](<2015-vandaele-linear-extension-complexity-regular_images/imageFile74.png>)

![image 75](<2015-vandaele-linear-extension-complexity-regular_images/imageFile75.png>)

![image 76](<2015-vandaele-linear-extension-complexity-regular_images/imageFile76.png>)

![image 77](<2015-vandaele-linear-extension-complexity-regular_images/imageFile77.png>)

![image 78](<2015-vandaele-linear-extension-complexity-regular_images/imageFile78.png>)

and another matrix from the positive 4-by-4 block of S9 at the upper right (rows 2 to 5, last 4 columns)

  

   −

   =

  .

  

  

c4 − c2 c3 − c1 c2 c1 c3 − c1 c4 c3 c2 − c1 c2 c3 c4 − c1 c3 − c2 c1 c2 − c1 c3 − c2 c4 − c3

c4 c3 c2 c1 c3 c4 c3 c2 c2 c3 c4 c3 c1 c2 c3 c4

c2 c1 0 0 c1 0 0 c1 0 0 c1 c2 0 c1 c2 c3

![image 79](<2015-vandaele-linear-extension-complexity-regular_images/imageFile79.png>)

![image 80](<2015-vandaele-linear-extension-complexity-regular_images/imageFile80.png>)

![image 81](<2015-vandaele-linear-extension-complexity-regular_images/imageFile81.png>)

![image 82](<2015-vandaele-linear-extension-complexity-regular_images/imageFile82.png>)

![image 83](<2015-vandaele-linear-extension-complexity-regular_images/imageFile83.png>)

![image 84](<2015-vandaele-linear-extension-complexity-regular_images/imageFile84.png>)

![image 85](<2015-vandaele-linear-extension-complexity-regular_images/imageFile85.png>)

![image 86](<2015-vandaele-linear-extension-complexity-regular_images/imageFile86.png>)

![image 87](<2015-vandaele-linear-extension-complexity-regular_images/imageFile87.png>)

![image 88](<2015-vandaele-linear-extension-complexity-regular_images/imageFile88.png>)

![image 89](<2015-vandaele-linear-extension-complexity-regular_images/imageFile89.png>)

![image 90](<2015-vandaele-linear-extension-complexity-regular_images/imageFile90.png>)

![image 91](<2015-vandaele-linear-extension-complexity-regular_images/imageFile91.png>)

![image 92](<2015-vandaele-linear-extension-complexity-regular_images/imageFile92.png>)

![image 93](<2015-vandaele-linear-extension-complexity-regular_images/imageFile93.png>)

![image 94](<2015-vandaele-linear-extension-complexity-regular_images/imageFile94.png>)

![image 95](<2015-vandaele-linear-extension-complexity-regular_images/imageFile95.png>)

![image 96](<2015-vandaele-linear-extension-complexity-regular_images/imageFile96.png>)

![image 97](<2015-vandaele-linear-extension-complexity-regular_images/imageFile97.png>)

![image 98](<2015-vandaele-linear-extension-complexity-regular_images/imageFile98.png>)

![image 99](<2015-vandaele-linear-extension-complexity-regular_images/imageFile99.png>)

Clearly, the removed matrices are nonnegative since 0 ≤ ck−1 ≤ ck for all 0 ≤ k ≤ ⌊n2⌋. Moreover, we show in the next lemma that they have rank one.

![image 100](<2015-vandaele-linear-extension-complexity-regular_images/imageFile100.png>)

Lemma 1. The (inﬁnite) matrix

cα−i+j − cβ−i−j

i∈Z,j∈Z has rank one for any ﬁxed α ∈ Z, β ∈ Z and n ∈ N>0.

Proof. We have that ck = cos(πn) − cos((2k + 1)πn) = 2sin(kπn)sin((k + 1)nπ). Choosing any 2 × 2 minor with rows i ∈ {0,x} and columns j ∈ {0,y} (w.l.o.g.), one can check, using algebra with a few

![image 101](<2015-vandaele-linear-extension-complexity-regular_images/imageFile101.png>)

![image 102](<2015-vandaele-linear-extension-complexity-regular_images/imageFile102.png>)

![image 103](<2015-vandaele-linear-extension-complexity-regular_images/imageFile103.png>)

![image 104](<2015-vandaele-linear-extension-complexity-regular_images/imageFile104.png>)

trigonometric identities, that the determinant of

cα − cβ cα+y − cβ−y cα−x − cβ−x cα−x+y − cβ−x−y is equal to zero for any x, y, and any n.

![image 105](<2015-vandaele-linear-extension-complexity-regular_images/imageFile105.png>)

![image 106](<2015-vandaele-linear-extension-complexity-regular_images/imageFile106.png>)

![image 107](<2015-vandaele-linear-extension-complexity-regular_images/imageFile107.png>)

![image 108](<2015-vandaele-linear-extension-complexity-regular_images/imageFile108.png>)

After these two nonnegative rank-one factors are removed, we obtain









T

T

c4−c3 c1 c3−c2 c1 c2−c1 c1













![image 109](<2015-vandaele-linear-extension-complexity-regular_images/imageFile109.png>)

0 0 0 0

0 c1 c2 c3 c4 c3 c2 c1 0 0 0 c1 c2 c3 c2 c1 0 0 c1 0 0 c1 c2 c1 0 0 c1 c2 c1 0 0 c1 0 0 c1 c2 c3 c2 c1 0 0 0 c1 c2 c3 c3 c2 c1 0 0 0 c1 c2 c3 c2 c1 0 0 c1 0 0 c1 c2 c1 0 0 c1 c2 c1 0 0 c1 0 0 c1 c2 c3 c2 c1 0 0

0 0 0 0 0 c1 c2 c3 − c1 c4 − c2

0 c4 − c2 c3 − c1 c2 c1 0 0 0 0

![image 110](<2015-vandaele-linear-extension-complexity-regular_images/imageFile110.png>)

![image 111](<2015-vandaele-linear-extension-complexity-regular_images/imageFile111.png>)

![image 112](<2015-vandaele-linear-extension-complexity-regular_images/imageFile112.png>)

![image 113](<2015-vandaele-linear-extension-complexity-regular_images/imageFile113.png>)

![image 114](<2015-vandaele-linear-extension-complexity-regular_images/imageFile114.png>)

![image 115](<2015-vandaele-linear-extension-complexity-regular_images/imageFile115.png>)

1 0 0 0 0 0

![image 116](<2015-vandaele-linear-extension-complexity-regular_images/imageFile116.png>)

- 0
- 1


S9 −

−

,

=

![image 117](<2015-vandaele-linear-extension-complexity-regular_images/imageFile117.png>)

![image 118](<2015-vandaele-linear-extension-complexity-regular_images/imageFile118.png>)

c2−c1 c1 c3−c2 c1 c4−c3 c1

![image 119](<2015-vandaele-linear-extension-complexity-regular_images/imageFile119.png>)

![image 120](<2015-vandaele-linear-extension-complexity-regular_images/imageFile120.png>)

 

 

 

 

 

 

 

 

 

 

![image 121](<2015-vandaele-linear-extension-complexity-regular_images/imageFile121.png>)

![image 122](<2015-vandaele-linear-extension-complexity-regular_images/imageFile122.png>)

![image 123](<2015-vandaele-linear-extension-complexity-regular_images/imageFile123.png>)

![image 124](<2015-vandaele-linear-extension-complexity-regular_images/imageFile124.png>)

with a pattern of zeros forming a cross. This matrix is highly symmetric and has a lot of redundancy: the last four columns (resp. rows) are copies of the ﬁrst four. Therefore, if we had a nonnegative factorization of the 5-by-5 upper left block then we would have a nonnegative factorization of the entire matrix with the same nonnegative rank.

To construct that factorization, we apply our strategy recursively: use a rank-two correction to the upper left block to make a cross of zeros appear:





0 c1 c2 c3 c4 0 0 c1 c2 c3 c1 0 0 c1 c2 c2 c1 0 0 c1 c3 c2 c1 0 0

 

 

→





![image 125](<2015-vandaele-linear-extension-complexity-regular_images/imageFile125.png>)

0 c1 c2 c1 0 0 0 c1 0 0 c1 0 0 0 c1 c1 0 0 0 c1 0 0 c1 0 0

![image 126](<2015-vandaele-linear-extension-complexity-regular_images/imageFile126.png>)

![image 127](<2015-vandaele-linear-extension-complexity-regular_images/imageFile127.png>)

=

 

 

![image 128](<2015-vandaele-linear-extension-complexity-regular_images/imageFile128.png>)

![image 129](<2015-vandaele-linear-extension-complexity-regular_images/imageFile129.png>)

![image 130](<2015-vandaele-linear-extension-complexity-regular_images/imageFile130.png>)





0 c1 c2 0 0 c1 c1 0 0 c1 0 0 0 0 c1

 

 

 

![image 131](<2015-vandaele-linear-extension-complexity-regular_images/imageFile131.png>)

 .

![image 132](<2015-vandaele-linear-extension-complexity-regular_images/imageFile132.png>)

1 0 0 0 1 0 1 0 1 0 0 0 1 0 0

![image 133](<2015-vandaele-linear-extension-complexity-regular_images/imageFile133.png>)

![image 134](<2015-vandaele-linear-extension-complexity-regular_images/imageFile134.png>)

Now, the upper left block has a trivial nonnegative factorization (since it is a 3-by-3 matrix of rank

3) from which we can derive a nonnegative factorization for the full matrix S9: 



0 c1 c2 0 c3 − c1 0 0 0 0 c1 0 c2 0 c4 − c2 c1 0 0 0 c1 0 c3 − c1 c1 0 0 c1 0 0 c2 0 0 c1 c2 0 0 c1 0 0 c1 c2 0 c1 0 c1 0 0 c1 0 c2 0 c1 0 0 0 c1 c3 − c1 0 0 0 c1 0 c2 c4 − c2 0





1 0 0 0 1 0 0 0 1 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0 1 0 0

c1 1 0 0 0 0 0 1 c2c−c1

c2−c1

.

![image 135](<2015-vandaele-linear-extension-complexity-regular_images/imageFile135.png>)

![image 136](<2015-vandaele-linear-extension-complexity-regular_images/imageFile136.png>)

1

0 0 0 1 c2c−c1

1 0 0 0

![image 137](<2015-vandaele-linear-extension-complexity-regular_images/imageFile137.png>)

1

 

 

c4−c3 c1

c3−c2 c1

c2−c1

c1 1 0 0 0 0 0 0 0 0 0 0 1 c2c−c1

![image 138](<2015-vandaele-linear-extension-complexity-regular_images/imageFile138.png>)

![image 139](<2015-vandaele-linear-extension-complexity-regular_images/imageFile139.png>)

![image 140](<2015-vandaele-linear-extension-complexity-regular_images/imageFile140.png>)

 

 

c3−c2 c1

c4−c3 c1

![image 141](<2015-vandaele-linear-extension-complexity-regular_images/imageFile141.png>)

![image 142](<2015-vandaele-linear-extension-complexity-regular_images/imageFile142.png>)

![image 143](<2015-vandaele-linear-extension-complexity-regular_images/imageFile143.png>)

1

Remark 1. Once the ﬁrst two rank-one factors have been removed from S9, the 5-by-5 block could also directly be trivially factorized, and we would obtain





0 c1 c2 c3 c4 0 0 0 0 c1 c2 c3 0 c4 − c2 c1 0 0 c1 c2 0 c3 − c1 c2 c1 0 0 c1 0 c2 c3 c2 c1 0 0 0 c1 c3 c2 c1 0 0 c1 0 c2 c1 0 0 c1 c2 0 c1 0 0 c1 c2 c3 − c1 0 0 0 c1 c2 c3 c4 − c2 0





1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0

S9 =

.

 

 

c3−c2 c1

c2−c1

c4−c3 c1

c1 1 0 0 0 0 0 0 0 0 0 0 1 c2c−c1

![image 144](<2015-vandaele-linear-extension-complexity-regular_images/imageFile144.png>)

![image 145](<2015-vandaele-linear-extension-complexity-regular_images/imageFile145.png>)

![image 146](<2015-vandaele-linear-extension-complexity-regular_images/imageFile146.png>)

 

 

c3−c2 c1

c4−c3 c1

![image 147](<2015-vandaele-linear-extension-complexity-regular_images/imageFile147.png>)

![image 148](<2015-vandaele-linear-extension-complexity-regular_images/imageFile148.png>)

![image 149](<2015-vandaele-linear-extension-complexity-regular_images/imageFile149.png>)

1

For n even, the construction slightly changes because the symmetry in the residual with the cross pattern of zero is diﬀerent. Let us illustrate it for n = 6. The ﬁrst rank-two correction is the same as for n = 9 and we obtain









0 c1 c2 c2 c1 0 0 0 c1 c2 c2 c1 c1 0 0 c1 c2 c2 c2 c1 0 0 c1 c2 c2 c2 c1 0 0 c1 c1 c2 c2 c1 0 0

0 c1 c2 c2 c1 0 0 0 c1 c1 0 0 c1 0 0 0 0 c1 c2 c1 0 0 c1 c2 c1 0 0 0 0 c1 0 0 c1 c1 0 0

→ R6 =

S6 =

. (6)

 

 

 

 

However, the fourth row of R6 is not a copy of the ﬁrst three. Therefore, we need to keep it: factorizing the following submatrix

  

  

0 c1 c2 0 0 c1 c1 0 0 c2 c1 0

R6′ =

allows to factor R6 (last three columns and last two rows are duplicates). Since it is a 4-by-3 matrix, we can factor it trivially as R6′ = R6′ I3 and obtain a rank-5 nonnegative factorization of S6.

In summary,

- • At the recursion steps, the factorization of the remaining k-by-l block (k = l or l+1) is computed via a nonnegative rank-two correction and the factorization of its ⌈k′⌉-by-⌈2l ⌉ upper left block where k′ = ⌈2l ⌉ + 1 when k = l is even and k′ = ⌈2l ⌉ otherwise.


![image 150](<2015-vandaele-linear-extension-complexity-regular_images/imageFile150.png>)

![image 151](<2015-vandaele-linear-extension-complexity-regular_images/imageFile151.png>)

![image 152](<2015-vandaele-linear-extension-complexity-regular_images/imageFile152.png>)

- • At the last step, when k ≤ 4, a trivial factorization is used. Note that there will be four ‘basic’ cases: 3-by-3 (e.g., for n = 5,9), 4-by-3 (e.g., for n = 6), 4-by-4 (e.g., n = 4,7), and 3-by-2 (e.g., for n = 10).


In the recursion steps described above, from a large matrix with c columns, a submatrix with

⌈2c⌉ columns is extracted, and the nonnegative rank of the larger matrix is smaller than that of the submatrix plus two (because of the two nonnegative rank-one corrections). This leads to the following

![image 153](<2015-vandaele-linear-extension-complexity-regular_images/imageFile153.png>)

result:

- Theorem 3. Let n ≥ 2, then the nonnegative rank of any slack matrix Sn of the regular n-gon is bounded as follows:


rank+(Sn) ≤

2⌈log2(n)⌉ − 1 = 2k − 1 for 2k−1 < n ≤ 2k−1 + 2k−2, 2⌈log2(n)⌉ = 2k for 2k−1 + 2k−2 < n ≤ 2k.

(7)

Proof. Let us ﬁrst assume that the recursion described above is correct, that is, that at each step the number of columns c is decreased to ⌈2c⌉ while the nonnegative rank is increased by at most 2, unless c ≤ 4 in which case we use the trivial factorization of rank c. To verify that (7) holds, we observe that the function ⌈2c⌉ is nondecreasing in c hence it suﬃces to verify that the upper bound holds for the critical values 2k,2k−1 + 1,2k−1 + 2k−2 and 2k−1 + 2k−2 + 1 for any k. For n = 2k, we check that the recursion divides the number of column by two at each step until the number of columns is equal to four which gives rank+(Sn) ≤ 2log2(n). For n = 2k−1 + 1, the number of columns c = 2p + 1 for some p is reduced at each step to ⌈c/2⌉ = 2p−1 + 1. After k − 2 steps, we get a 3-by-3 matrix which gives rank+(Sn) ≤ 2(k − 2) + 3 = 2k − 1. For n = 2k−1 + 2k−2, after k − 2 steps, the number of columns is equal to 3 hence we obtain rank+(Sn) ≤ 3 + 2(k − 2) = 2k − 1; the case n = 2k−1 + 2k−2 + 1 is similar to that above.

![image 154](<2015-vandaele-linear-extension-complexity-regular_images/imageFile154.png>)

![image 155](<2015-vandaele-linear-extension-complexity-regular_images/imageFile155.png>)

Let us now prove the recursion. To understand the proof, we encourage the reader to also look at the (short) Matlab code in Appendix B that constructs the factorizations2.

Let B be the k-by-l upper left block of the slack matrix Sn, where k = l or l + 1 and 1 ≤ k,l ≤ n. Note that, at the ﬁrst step, k = l = n. Basic step. If l ≤ 4, B is trivially factorized, that is, B = BIl where Il is the l-by-l identity matrix. Recursion step. If we show that

rank+(B) ≤ 2 + rank+(B′),

where B′ is the k′-by-⌈l/2⌉ upper left block of B, where k′ = ⌈k/2⌉ except when k = l is even in which case k′ = ⌈k/2⌉ + 1 = l/2 + 1, then the proof will be complete, by recursion (since B′ is also a k′-by-l′ upper left block of the slack matrix Sn where l′ = ⌈l/2⌉ and k′ = l′ or l′ + 1).

Since B is the upper left block of Sn, it is a circulant matrix and has the following form





c0 c1 ... c−1+l

c−1 c0 ... c−2+l . . ... . c−k+1 c−k+2 ... c−k+l

B =

= [c−i+j]1≤i≤k,1≤j≤l ,

 

 

![image 156](<2015-vandaele-linear-extension-complexity-regular_images/imageFile156.png>)

2Note that we have numerically checked the correctness of the construction for all n ≤ 10000.

where the ck’s are given by (2). The recursion works as follows. First, we subdivide the matrix B into four blocks: (i) the upper left ⌈l/2⌉-by-⌊l/2⌋ block, (ii) the upper right ⌈l/2⌉-by-⌈l/2⌉ block, (iii) the lower left (k − ⌈l/2⌉)-by-⌊l/2⌋ block, and (iv) the lower right (k − ⌈l/2⌉)-by-⌈l/2⌉ block. (Note that k −⌈l/2⌉ = ⌊l/2⌋+k −l which will be useful later.) Then, we make a nonnegative rank-one correction to the upper right and lower left blocks so that the oﬀ-diagonal entries of B and the entries below are set to zero, that is, all entries (i,j) of B such that i + j = l + 1 or i + j = l + 2 will be set to zero. (Note that the entries (i,j) of B such that i = j or i = j + 1 are already equal to zero.)

Upper right block. Let p = ⌈l/2⌉ and consider the p-by-p upper right block of B





cl−p cl−p+1 ... cl−1 cl−p−1 cl−p ... cl−2

U =

= [c−i+j]1≤i≤p,l−p+1≤j≤l = [c−i+h+l−p]1≤i≤p,1≤h=j−l+p≤p ,

 

 

. . ... . cl−2p+1 cl−2p+2 ... cl−p

from which we remove the matrix U − [c1+p−i−j]1≤i≤p,1≤j≤p which is equal to 



cl−p − cp−1 cl−p+1 − cp−2 ... cl−1 − c0 cl−p−1 − cp−2 cl−p − cp−3 ... cl−2 − c−1

= [cα−i+j − cβ−i−j]1≤i≤p,1≤j≤p ,

 

 

. . ... . cl−2p+1 − c0 cl−2p+2 − c−1 ... cl−p − c−p+1

where α = l − p and β = 1 + p. By Lemma 1, that matrix has rank-one. Moreover, it is nonnegative because for all 1 ≤ i,j ≤ p

cl−⌈l/2⌉−i+j = c⌊l/2⌋−i+j ≥ c1+⌈l/2⌉−i−j since ⌊l/2⌋ + j ≥ 1 + ⌈l/2⌉ − j for all j. We obtain





- cp−1 cp−2 ... c1 0
- cp−2 cp−3 ... 0 0


[c−i+j+l−p − cα−i+j + cβ−i−j]1≤i≤p,1≤j≤p =

= [cp+1−i−j]1≤i≤p,1≤j≤p .

. . ... . .

 

 

c1 0 ... cp−4 cp−3 0 0 ... cp−3 cp−2

Lower left block. Let p = ⌊l/2⌋ and q = p + k − l = k − ⌈l/2⌉ (= p if k = l, = p + 1 if k = l + 1), and consider the q-by-p lower left block of B





c−k+q c−k+q+1 ... c−k+q+p−1

. . ... . c−k+2 c−k+3 ... c−k+p+1 c−k+1 c−k+2 ... c−k+p

L =

= [c−i+j]k−q+1≤i≤k,1≤j≤q = [c−h−k+q+j]1≤h=i−k+q≤q,1≤j≤p ,

 

 

from which we remove the matrix L − [c1+p−i−j]1≤i≤q,1≤j≤p which is equal to 



c−k+q − cp−1 c−k+q+p − cp−2 ... c−k+q+p−1 − c0 c−k+q−1 − cp−2 c−k+q − cp−3 ... c−k+q+p−2 − c−1 . . ... . c−k+2 − cp−q+1 c−k+3 − cp−q ... c−k+p+1 − c−q+2 c−k+1 − cp−q c−k+2 − cp−q−1 ... c−k+p − c−q+1

= [cα−i+j − cβ−i−j]1≤i≤q,1≤j≤p ,

 

 

where α = −k +q = −⌊l/2⌋ and β = 1+p = ⌊l/2⌋+1, which can be checked to be nonnegative (using the fact that c−k = ck+1, we have cα−i+j = c−α+i−j+1 = c⌊l/2⌋+i−j+1 ≥ c⌊l/2⌋+1−i−j = cβ−i−j), and has rank-one by Lemma 1. We obtain

[c−i−k+q+j − cα−i+j + cβ−i−j]1≤i≤q,1≤j≤p =





- cp−1 cp−2 ... c1 0
- cp−2 cp−3 ... 0 0


.

. . ... . . cp−q+1 cp−q(= 0) ... c−q+3 c−q+2

 

 

cp−q(= 0) cp−q−1 ... c−q+2 c−q+1

Note that, if k = l (that is, p = q) then cp−q−1 = 0 otherwise k = l + 1 and cp−q+1 = 0.

Finally, putting all the blocks together: the untouched upper left and lower right blocks, and the corrected upper right and lower left blocks, we obtain, after a nonnegative rank-two correction of B, the following l-by-l matrix 



0 c1 c2 ... c2 c1 0 0 0 c1 ... c1 0 0 c1 0 0 ... 0 0 c1 . . . . . .

c2 c1 0 ... 0 c1 c2 c1 0 0 ... 0 0 c1 0 0 c1 ... c1 0 0

 

 

to which the following row

0 c1 c2 ... c2 c1 0 has to be added when k = l + 1. That matrix has the following properties

- • every column is repeated twice except the middle one when l is odd –more precisely, the jth and (l − j + 1)th columns are identical for 1 ≤ j ≤ ⌊l/2⌋–, and
- • every row is repeated twice except (i) the ﬁrst one when k = l, (ii) the (l/2 + 1)th when k = l is even, (ii) the middle one when k = l + 1 is odd –more precisely, the (i + s)th and (k − i + 1)th rows are identical for 1 ≤ i ≤ ⌊k/2⌋, and s = 0 for k = l + 1 and s = 1 for k = l.


This concludes the recursion step, hence the proof. A Matlab code that generates the slack matrices of regular n-gons and constructs the nonnegative

![image 157](<2015-vandaele-linear-extension-complexity-regular_images/imageFile157.png>)

![image 158](<2015-vandaele-linear-extension-complexity-regular_images/imageFile158.png>)

![image 159](<2015-vandaele-linear-extension-complexity-regular_images/imageFile159.png>)

![image 160](<2015-vandaele-linear-extension-complexity-regular_images/imageFile160.png>)

factorizations described above for any n is available from https://sites.google.com/site/exactnmf/regularngons.

Tightness of the Bound It has to be pointed out that our inspiration for constructing the nonnegative factorizations used in Theorem 3 came from factorizations computed by our numerical solver [23] available on https://sites.google.com/site/exactnmf/.

Moreover, for n up to 78, the heuristic algorithm developed in [23] always found a factorization for the bound of Theorem 3 but never smaller. This suggests that our upper bound is tight, at least for small n.

# 5 Conclusion

In this paper, we have ﬁrst proposed a new lower bound for the rectangle covering number of the slack matrix of any n-gons, using a generalization of Sperner theorem; see Theorem 2 and Corollary 3. We hope that this idea will lead to new lower bound for other types of nonnegative matrices.

Then, we proposed an algebraic proof for the upper bounds for the extension complexity of regular n-gons based on explicit nonnegative factorizations of the slack matrices of regular n-gons; see Theorem 3. This bound slightly improves upon the previously best known upper bound from [9] (our improvement essentially comes from improving the base case but we provided a new purely algebraic proof), and allows us to close the gap with the best known lower bound for several n-gons (9 ≤ n ≤ 13, 21 ≤ n ≤ 24; see Figure 2). However, for most n-gons (precisely, for n = 14, 17 ≤ n ≤ 20, 25 ≤ n ≤ 30 and n ≥ 33), there is still a gap with the best known lower and upper bounds hence it is a direction for further research to improve these bounds to determine the extension complexity of these regular n-gons. Our numerical results suggest that the way to go would be to improve the lower bounds since our upper bound appears to be tight, at least for small n.

# 6 Acknowledgement

We kinldy acknowledge the participants of the Dagstuhl seminar 15082 on ‘Limitations of convex programming: lower bounds on extended formulations and factorization ranks’ for insightful discussions, and we thank in particular the organizers, Hartmut Klauck, Troy Lee, Dirk Oliver Theis, and Rekha R. Thomas. We also thank the two anonymous reviewers for their insightful comments which helped improve the paper signiﬁcantly. Finally, we thank Joa˜o Gouveia for insightful discussions and for giving us the reference to the upper bounds for the boolean rank [1].

# References

- [1] Barefoot, C., Hefner, K., Jones, K., Lundgren, J.: Biclique covers of the complements of cycles and paths in a digraph. Congressus Numerantium 53, 133–146 (1986)
- [2] Beasley, L., Laﬀey, T.: Real rank versus nonnegative rank. Linear Algebra and its Applications 431(12), 2330–2335 (2009)
- [3] Ben-Tal, A., Nemirovski, A.: On polyhedral approximations of the second-order cone. Mathematics of Operations Research 26(2), 193–205 (2001)
- [4] de Caen, D., Gregory, D., Pullman, N.: The boolean rank of zero-one matrices. In: Proc. 3rd Caribbean Conference on Combinatorics and Computing, pp. 169-173 (1981)
- [5] Fawzi, H., Parrilo, P.: Lower bounds on nonnegative rank via nonnegative nuclear norms. Mathematical Programming 153(1), 41–66 (2015)
- [6] Fawzi, H., Parrilo, P.: Self-scaled bounds for atomic cone ranks: applications to nonnegative rank and cp-rank. Mathematical Programming (2015)
- [7] Fiorini, S., Kaibel, V., Pashkovich, K., Theis, D.: Combinatorial bounds on nonnegative rank and extended formulations. Discrete Mathematics 313(1), 67–83 (2013)
- [8] Fiorini, S., Massar, S., Pokutta, S., Tiwary, H., de Wolf, R.: Linear vs. semideﬁnite extended formulations: exponential separation and strong lower bounds. In: Proceedings of the forty-fourth annual ACM symposium on Theory of computing, pp. 95–106. ACM (2012)


- [9] Fiorini, S., Rothvoss, T., Tiwary, H.: Extended formulations for polygons. Discrete & Computational Geometry 48(3), 658–668 (2012)
- [10] Gillis, N., Glineur, F.: On the geometric interpretation of the nonnegative rank. Linear Algebra and its Applications 437(11), 2685–2712 (2012)
- [11] Glineur, F.: Computational experiments with a linear approximation of second order cone optimization

(2000). Image Technical Report 0001, Service de Math´ematique et de Recherche Op´erationnelle, Facult Polytechnique de Mons

- [12] Goemans, M.: Smallest compact formulation for the permutahedron. Mathematical Programming 153(1), 5–11 (2015). http://math.mit.edu/~goemans/PAPERS/permutahedron.pdf
- [13] Gouveia, J., Grappe, R., Kaibel, V., Pashkovich, K., Robinson, R., Thomas, R.: Which nonnegative matrices are slack matrices? Linear Algebra and its Applications 439(10), 2921–2933 (2013)
- [14] Gouveia, J., Parrilo, P., Thomas, R.: Lifts of convex sets and cone factorizations. Mathematics of Operations Research 38(2), 248–264 (2013)
- [15] Kaibel, V., Pashkovich, K.: Constructing extended formulations from reﬂection relations. In: Integer Programming and Combinatoral Optimization, pp. 287–300. Springer (2011)
- [16] Kaibel, V., Pashkovich, K.: Constructing extended formulations from reﬂection relations. In: M. Jnger, G. Reinelt (eds.) Facets of Combinatorial Optimization, pp. 77–100. Springer Berlin Heidelberg (2013)
- [17] Lubell, D.: A short proof of Sperner’s lemma. Journal of Combinatorial Theory 1(2), 299 (1966)
- [18] McMullen, P.: The maximum numbers of faces of a convex polytope. Mathematika 17(02), 179–184 (1970)
- [19] Oelze, M., Vandaele, A., Weltge, S.: Computing the extension complexities of all 4-dimensional 0/1polytopes (2014). arXiv:1406.4895
- [20] Rothvoss, T.: The matching polytope has exponential extension complexity. In: Proceedings of the 46th ACM symposium on Theory of Computing, STOC ’14, pp. 263–272 (2014)
- [21] Shitov, Y.: An upper bound for nonnegative rank. Journal of Combinatorial Theory, Series A 122, 126–132

(2014)

- [22] Sperner, E.: Ein satz ¨uber untermengen einer endlichen menge. Mathematische Zeitschrift 27(1), 544–548

(1928)

- [23] Vandaele, A., Gillis, N., Glineur, F., Tuyttens, D.: Heuristics for exact nonnegative matrix factorization. Journal of Global Optimization (2015). http://dx.doi.org/10.1007/s10898-015-0350-z
- [24] Yannakakis, M.: Expressing Combinatorial Optimization Problems by Linear Programs. Journal of Computer and System Sciences 43(3), 441–466 (1991)
- [25] Ziegler, G.: Lectures on Polytopes. Springer-Verlag (1995)


# A Proof for Theorem 2

The solution k∗ = ⌊r/2⌋ and z∗ = 1 is optimal for min

k!(r − k)! + (k + z)!(r − k − z)! − 2k!z!(r − k − z)!.

k≥1,z≥1,k+z≤r

Proof. Let us observe the following

- • the ﬁrst (resp. second) term is decreasing when k (resp. k + z) gets closer to r/2.
- • the last term is strictly increasing in z hence being minimized in z = 1.
- • f(k,z) = f(r − k − z,z). (Note that this implies that, for r even, k∗ = r/2 − 1 is also optimal.)


The ﬁrst two observations imply that, at optimality, the case z ≥ 2 and k + z ≥ ⌊r/2⌋ + 1 is not possible, otherwise we would decrease the objective function by decreasing z. In other words, either z∗ = 1 or k + z ≤ ⌊r/2⌋.

- Case 1: z∗ = 1. Since f(k,1) = f(r−k−1,1), we can assume w.l.o.g. that k ≥ ⌊r/2⌋ since either k or r−k−1 is larger than ⌊r/2⌋. Showing that f(k,1) is increasing for ⌊r/2⌋ ≤ k ≤ r − 1, that is, that f(k,1) ≤ f(k + 1,1) for k + 1 ≤ r − 1 will prove the result: k!(r −k)!+(k +1)!(r −k −1)!−2k!(r −k −1)! ≤ (k +1)!(r −k −1)!+(k +2)!(r −k −2)!−2(k +1)!(r −k −2)!

⇐⇒ k!(r − k)! − 2k!(r − k − 1)! ≤ (k + 2)!(r − k − 2)! − 2(k + 1)!(r − k − 2)!. Dividing by k! and (r − k − 2)!,

(r − k)(r − k − 1) − 2(r − k − 1) ≤ (k + 2)(k + 1) − 2(k + 1) which is equivalent to

r2 − 3r + 2 ≤ 2k(r − 1). Since k ≥ ⌊r/2⌋, 2k ≥ r − 1 hence the above inequality would be implied by r2 − 3r + 2 ≤ (r − 1)2 = r2 − 2r + 1 ⇐⇒ r ≥ 1.

- Case 2: k + z ≤ ⌊r/2⌋. We have k′ = r − k − z ≥ ⌊r/2⌋ hence we can reduce this case to the case k ≥ ⌊r/2⌋ without loss of generality, since f(k,z) = f(r − k − z,z). For k ≥ ⌊r/2⌋, it is clear that z∗ = 1 is optimal (since last tow terms increase with z in that case) so that this case reduces to case 1 when z∗ = 1.


![image 161](<2015-vandaele-linear-extension-complexity-regular_images/imageFile161.png>)

![image 162](<2015-vandaele-linear-extension-complexity-regular_images/imageFile162.png>)

![image 163](<2015-vandaele-linear-extension-complexity-regular_images/imageFile163.png>)

![image 164](<2015-vandaele-linear-extension-complexity-regular_images/imageFile164.png>)

# B Code for the Nonnegative Factorization of Slack Matrices of Regular n-gons

% Rank r nonnegative factorization of the slack matrix S n=UV of the regular % n−gon generated by the function slack.m, r being equal to % 2k−1 for 2ˆ{k−1} < n ≤ 2ˆ{k−1}+2ˆ{k−2} , and % 2 k for 2ˆ{k−1}+2ˆ{k−2} < n ≤ 2ˆ{k} . % % See A. Vandaele, N. Gillis and F. Glineur, % "On the Linear Extension Complexity of Regular n−gons", arXiv, 2015. % If you use the code, please cite the paper. % See also https://sites.google.com/site/exactnmf/regularngons % % This version uses the matrix S as an input with 0(nˆ2) operations, % hence is computationally less efficient as factorization.m which % only requires O(n log(n)). % However, it is more intuitive to understand the construction and follows % the proof of the paper above more closely.

![image 165](<2015-vandaele-linear-extension-complexity-regular_images/imageFile165.png>)

function [U,V,R] = NonnegFactoRegnGon(S) [m,n] = size(S); if n ≤ 4 % trivial factorization

- U = S;
- V = eye(n); R = S;


else n > 4 % non−trivial factorizations

- % Step 1: Create the cross pattern of zeros removing a nonnegative % rank−two factor [U,V,R] = offdiag zeros(S);

![image 166](<2015-vandaele-linear-extension-complexity-regular_images/imageFile166.png>)

- % Step 2: Extract the upper left block that has the same nonnegative % rank as the full residual R (because of symmetry/redundancy)

- k1 = ceil(m/2); if k1 == m/2 && m == n % When m is even and m == n

k1 = k1+1; end

- k2 = ceil(n/2);


- % Step 3: Factor the upper left block using recursion [Ur,Vr] = NonnegFactoRegnGon(S(1:k1,1:k2));
- % Step 4: Put everything together using the symmetry r = size(Ur,2); U = [U zeros(m,r)]; V = [V; zeros(r,n)]; % Factor V V(3:end,1:k2) = Vr; for i = n : −1 : k2+1


V(3:end,i) = V(3:end,n−i+1);

end % Factor U U(1:k1,3:end) = Ur; if m == n % Case 1: R(k1,:)==R(k1+1,:), symmetry is 'perfect'

p = 1; elseif m == n+1 % Case 2: R(k1−1,:)==R(k1+1,:), symmetry is shifted by one p = 0;

end

end for i = 1 : m−k1

U(k1+i,3:end) = U(k1−i+p,3:end); end

% Add zeros on off−diagonal entries of matrix S using a rank−two % correction. The first rank−one factor puts zero entries on the lower left % block, the second on the upper right block.

function [U,V,R] = offdiag zeros(S) [m,n] = size(S);

![image 167](<2015-vandaele-linear-extension-complexity-regular_images/imageFile167.png>)

- U = zeros(m,2);
- V = zeros(2,n); k2 = floor(n/2); % Lower left block if m == n % zeros below the diagonal (starting from the lower left)


k1 = ceil(n/2); U(m,1) = S(m,1);

elseif m == n+1 % zeros above the diagonal (starting from the lower left) k1 = floor(m/2); U([m−1 m],1) = S([m−1 m],1);

else

error('The matrix should be n−by−n or n+1−by−n'); end

- V(1,1) = 1; for i = 2 : k2

V(1,i) = S(n−i+2,i) / U(n−i+2,1); U(n−i+1,1) = S(n−i+1,i)/ V(1,i);

end % Upper right block: zeros below the diagonal % (starting from the upper right)

- V(2,n) = 1; U(1,2) = S(1,n); for i = 2 : k1


- U(i,2) = S(i,n−i+2) / V(2,n−i+2);
- V(2,n−i+1)= S(i,n−i+1) / U(i,2);


end % Residual with the pattern of zeros like a cross R = S − U*V;

The code is available from https://sites.google.com/site/exactnmf/regularngons.

