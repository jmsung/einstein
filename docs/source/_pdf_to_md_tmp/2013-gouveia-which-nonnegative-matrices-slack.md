arXiv:1303.5670v1[math.OC]22Mar2013

WHICH NONNEGATIVE MATRICES ARE SLACK MATRICES?

JOAO˜ GOUVEIA, ROLAND GRAPPE, VOLKER KAIBEL, KANSTANTSIN PASHKOVICH, RICHARD Z. ROBINSON, AND REKHA R. THOMAS

Abstract. In this paper we characterize the slack matrices of cones and polytopes among all nonnegative matrices. This leads to an algorithm for deciding whether a given matrix is a slack matrix. The underlying decision problem is equivalent to the polyhedral veriﬁcation problem whose complexity is unknown.

1. Introduction

This paper is concerned with a class of nonnegative matrices with real entries, called slack matrices, that arise naturally from polyhedral cones and polytopes. Given a polytope P ⊂ Rn with vertices v1,...,vp and facet inequalities aTj x ≤ βj for j = 1,...,q, a slack matrix of P is the p × q nonnegative matrix whose (i,j)entry is βj −aTj vi, the slack (distance from equality), of the ith vertex vi in the jth facet inequality aTj x ≤ βj of P. A similar deﬁnition holds for polyhedral cones.

Slack matrices form an interesting class of nonnegative matrices with many special properties. Most obviously, if M is a slack matrix of a polytope P, then the zeros in M record the face lattice of P and hence the combinatorial structure of P. In its entirety, M speciﬁes an embedding of P up to aﬃne transformation. However, slack matrices carry much more surprising information about P. In [15], Yannakakis proved that the nonnegative rank of a slack matrix of P is the minimum k such that P is the linear image of an aﬃne slice of the positive orthant Rk+. We use R+ to denote the set of nonnegative real numbers. The nonnegative rank of a matrix M ∈ Rp+×q is the smallest k such there there exists vectors a1,...,ap ∈ Rk+ and b1,...,bq ∈ Rk+ such that Mij = aTi bj. Aﬃne slices of positive orthants that project onto P are called polyhedral lifts or polyhedral extended formulations of P and the smallest k such that Rk+ admits a lift of P is called the (polyhedral) extension complexity or nonnegative rank of P. If the extension complexity of P is small (polynomial in the dimension of P), then usually it is possible to optimize a linear function over P in polynomial time by optimizing an appropriate function on the lift. This is a powerful technique in optimization that yields polynomial time algorithms for linear optimization over complicated polytopes. There are many instances of n-dimensional polytopes with exponentially many (in n) facets that allow small polyhedral lifts.

![image 1](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile1.png>)

Gouveia was supported by by the Centre for Mathematics at the University of Coimbra and Fundac˜ao para a Ciˆencia e a Tecnologia, through the European program COMPETE/FEDER, Kaibel by the Deutsche Forschungsgemeinschaft (KA 1616/4-1), Pashkovich by the Progetto di Eccellenza 2008-2009 of the Fondazione Cassa Risparmio di Padova e Rovigo, Robinson by the U.S. National Science Foundation Graduate Research Fellowship (DGE-1256082), and Thomas by the U.S. National Science Foundation grant DMS-1115293.

1

Yannakakis’ result was generalized in [5] to lifts of convex sets by aﬃne slices of convex cones via cone factorizations of slack operators. Even in the larger context of cone lifts of convex sets, the case of polytopes is the simplest and the theory relies on slack matrices of polytopes and their factorizations through cones. Thus, understanding the structure of these matrices is fundamental for this theory. There are several phenomena that occur in the class of nonnegative matrices that have not yet been observed for slack matrices. For instance, an important open question is whether there exists a family of slack matrices of polytopes that exhibit an exponential gap between nonnegative rank and positive semideﬁnite rank. (If S+k denotes the cone of k × k real symmetric positive semideﬁnite matrices, then the positive semideﬁnite rank of a matrix M ∈ Rp+×q is the smallest k such that there exists matrices Ai ∈ S+k , i = 1,...,p and Bj ∈ S+k , j = 1,...,q such that Mij =

Ai,Bj .) While there are simple families of matrices that exhibit even arbitrarily large gaps between nonnegative and positive semideﬁnite ranks [5, Example 5], no family of slack matrices with this property is known. Such a family would be a clear witness for the power of semideﬁnite programming over linear programming in lifts of polytopes.

This paper was motivated by the many open questions about slack matrices which rely on understanding the structure of these matrices. We establish two main characterizations of slack matrices of polyhedral cones and polytopes. In Section 2 we establish linear algebraic characterizations: Theorem 1 for cones and Theorem 6 for polytopes. In Section 4 we give combinatorial characterizations: Theorem 22 for polytopes and Theorem 24 for polyhedral cones. In Section 3 we use our characterization from Section 2 to give an algorithm for recognizing slack matrices. The computational complexity of this problem is unknown and is equivalent to the polyhedral veriﬁcation problem. There are several further geometric and complexity results about slack matrices throughout the paper.

Notation: For a set of vectors A = {a1,...,ap}, cone(A) := { λiai : λi ≥ 0} is the cone spanned by A; conv(A) := { λiai : λi ≥ 0, λi = 1} is the convex hull of A; lin(A) := { λiai : λi ∈ R} is the linear span of A, and aﬀ(A) := { λiai : λi = 1} is the aﬃne span of A. The above sets can also be deﬁned for an inﬁnite subset A ⊂ Rn by taking unions over all ﬁnite subsets of A. For a n × q matrix M, we let rows(M) and cols(M) denote the sets of all rows and columns, respectively, of M. We let A · M be the set of vectors {xTM : x ∈ A}. For a set K ⊂ Rn, lineal(K) is the largest subspace contained in K, known as the lineality space of K. The dimension of a polytope P, dim(P) is the dimension of aﬀ(P), the aﬃne hull of P, and the dimension of a cone K is the dimension of lin(K).

2. Geometric Characterizations of Slack Matrices

- 2.1. Slack Matrices of Polyhedral Cones. Consider the polyhedral cone


K = {x ∈ Rn : xTB ≥ O} = Rp+ · A in Rn constrained by the columns of the matrix B ∈ Rn×q and generated by the rows of the matrix A ∈ Rp×n. We call (the set of rows of) A a V-representation and (the set of columns of) B an H-representation of K. The slack matrix of K with respect to the representation (A,B) is S = AB ∈ Rp+×q. Its (i,j)-entry records the “slack” of the ith generator of K with respect to the jth inequality of K in the given description of K.

Let SK denote the set of all slack matrices of K. For S ∈ SK, any matrix obtained by scaling the rows and columns of S by positive reals is again in SK since scaling the vectors in a V and/or H-representation of K does not change K. Also, SK can have matrices of diﬀerent sizes as adding redundant inequalities and/or generators to the representations of K does not change K. From

(Rn · B) ∩ Rq+ = K · B = (Rp+ · A) · B = Rp+ · S ⊆ (Rp · S) ∩ Rq+ = (Rp · AB) ∩ Rq+ ⊆ (Rn · B) ∩ Rq+

we ﬁnd that Rp+ · S = Rp · S ∩ Rq+ which says that the cone generated by the rows of S coincides with the nonnegative part of the row span of S. In fact, this relation characterizes slack matrices of cones:

Theorem 1. A nonnegative matrix M ∈ Rp+×q is a slack matrix of a polyhedral cone if and only if

- (1) Rp+ · M = Rp · M ∩ Rq+, or in other words, the cone spanned by the rows of M coincides with the nonnegative part of the row span of M.

Proof. It remains to show that every matrix M ∈ Rp+×q with Rp+ ·M = Rp ·M ∩Rq+ is a slack matrix of some cone. Let n = rank(M) and choose a bijective linear map

ϕ : Rp · M → Rn

that preserves the (standard) scalar product (an isometry). Let Mi denote the ith row of M and let A ∈ Rp×n be the matrix whose rows are ϕ(Mi). Let π : Rq → Rp ·M be an orthogonal projection and let B ∈ Rn×q be the matrix whose columns are ϕ(π( 1)),...ϕ(π( q)) where i is the ith standard unit vector in Rq. Then M = AB and using (1),

K = {x ∈ Rn : xTB ≥ O} = {ϕ(y) : y ∈ Rp · M, ϕ(y)TB ≥ O}

= ϕ(Rp · M ∩ Rq+) = ϕ(Rp+ · M) = Rp+ · A, which shows that M is a slack matrix of the cone K.

Recall that the dual cone of K is the cone

K⋆ = {y ∈ Rn : xTy ≥ 0 for all x ∈ K} = {y ∈ Rn : Ay ≥ 0} = B · Rq+. Hence, ST is a slack matrix of K⋆ and we get the following result. Proposition 2. A nonnegative real matrix is a slack matrix of a polyhedral cone if and only if its transpose is also the slack matrix of a polyhedral cone. In particular, we obtain the following consequence of Theorem 1.

- Corollary 3. A nonnegative matrix M ∈ Rp+×q is a slack matrix of a polyhedral cone if and only if


- (2) M · Rq+ = M · Rq ∩ Rp+, or in other words, the cone spanned by the columns of M coincides with the nonnegative part of the column span of M.


We say that a matrix M satisﬁes the row cone generating condition (RCGC) if (1) holds and the column cone generating condition (CCGC) if (2) holds.

- Corollary 4. For a nonnegative matrix M ∈ Rp+×q the following statements are pairwise equivalent:


- • M is a slack matrix of a polyhedral cone.
- • M satisﬁes the RCGC.
- • M satisﬁes the CCGC.


The equivalence of RCGC and CCGC for a general nonnegative matrix is not obvious. However, its proof becomes transparent via the theory of slack matrices of polyhedral cones and cone duality.

For a nonnegative M with RCGC/CCGC, the proof of Theorem 1 showed how to produce a cone K such that M ∈ SK. We now give another way to produce such a cone K that will be useful later. For any matrix M ∈ Rp×q of rank k, we will call a factorization of the form M = AB with A ∈ Rp×k, rank(A) = k and B ∈ Rk×q, rank(B) = k a rank factorization of M.

Lemma 5. Let M ∈ Rp+×q be the slack matrix of a polyhedral cone and let M = AB be a rank factorization of M. Then if K is the cone generated by the rows of A,

the columns of B form an H-representation of K. In particular, M ∈ SK.

Proof. Let K = cone({a1,...,ap}) and K = {x ∈ Rk : xTbj ≥ 0, j = 1,...,q} where ai is the ith row of A and bj is the jth column of B. We need to show that

- K = K. Since M is a nonnegative matrix, K ⊆ K. To prove the reverse inclusion we will argue that every linear function that is nonnegative on K is also nonnegative on K. Let k = rank(M). Since M has the CCGC and A · Rk = M · Rq (since


rank(A) = k), we have that M·Rq+ = A·Rk∩Rp+. Suppose L(x) = ℓ1x1+...+ℓkxk ≥ 0 for all x ∈ K. Then the evaluation vector (L(a1),...,L(ap))T = Aℓ lies in M · Rq+. Since the columns of M are Abj for j = 1,...,q, there exists λj ≥ 0 such that Aℓ = qj=1 λj(Abj) = A qj=1 λjbj. This implies that ℓ = qj=1 λjbj since the columns of A are linearly independent. Therefore, ℓ is a nonnegative linear combination of the bj’s and L(x) ≥ 0 is valid on K.

- 2.2. Slack Matrices of Polytopes. We now investigate the slack matrices of polytopes. Let V ∈ Rp×n and P = conv(rows(V )) be the polytope in Rn that is the convex hull of the rows of V . Suppose also that P = {x ∈ Rn : Wx ≤ w} with W ∈ Rq×n and w ∈ Rq. To avoid unnecessary inconveniences, we assume that dim(P) ≥ 1. We call (the set of rows of) V a V-representation and (the set of columns of) [w,−W]T an H-representation of P. The slack matrix of P with respect to the representation (V,W,w) is then


- (3) S = [ ,V ] · [w,−W]T ∈ Rp+×q .

We denote the set of all slack matrices of P by SP. Clearly, scaling the columns of a slack matrix of P by positive scalars yields another slack matrix of P, because scaling the vectors in an H-representation of P yields another H-representation of P. However, we cannot scale the rows of a matrix S ∈ SP and still stay in SP.

The matrix S is also the slack matrix of the homogenization cone of P:

- (4) Ph = Rp+ · [ ,V ] = {(x0,x) ∈ R × Rn : Wx ≤ x0w}


T

with respect to the representation ([ ,V ], w

−WT ). Since dim(P) ≥ 1, there is some c ∈ Rn with

max{cTx : x ∈ P} − min{cTx : x ∈ P} = 1 ,

and hence, due to LP-duality, we get

- (5) (1,OT) ∈ Rq · (w,W) and so also, (1,OT) ∈ Rq · (w,−W).

From (3) and (5) we get that ∈ S · Rq, the column span of S. These properties characterize the slack matrices of polytopes of dimension at least one:

Theorem 6. A matrix M ∈ Rp+×q with rank(M) ≥ 2 is a slack matrix of a polytope if and only if M is a slack matrix of a polyhedral cone and ∈ M · Rq.

Proof. It suﬃces to show that a matrix M ∈ Rp+×q with ∈ M ·Rq that is the slack matrix of some cone K ⊆ Rn with respect to a representation (A,B) is also the slack matrix of some polytope. To construct such a polytope, choose any µ ∈ Rq such that = Mµ and deﬁne c = Bµ. Then Ac = since M = AB. Deﬁne P = conv(rows(A)). Then we have:

P = {yTA : yT = 1,y ∈ Rp+} = {yTA : yTAc = 1,y ∈ Rp+}

= {x ∈ K : xTc = 1} = {x ∈ Rn : xTB ≥ O,xTc = 1} .

Mapping the hyperplane in Rn deﬁned by xTc = 1 isometrically to Rn−1 (as in the proof of Theorem 1), we ﬁnd that M is a slack matrix of the resulting image of P.

- Corollary 7. A matrix M ∈ Rp+×q with rank(M) ≥ 2 is a slack matrix of some polytope if and only if it satisﬁes the RCGC (or, equivalently, the CCGC) and

∈ M · Rq holds.

Theorem 1 geometrically characterizes the slack matrices of cones as those matrices M ∈ Rp+×q that satisfy

(6) cone(rows(M)) = lin(rows(M)) ∩ Rq+ . There is an analogous geometric characterization of slack matrices of polytopes.

- Corollary 8. A matrix M ∈ Rp+×q with rank(M) ≥ 2 is a slack matrix of some polytope if and only if


- (7) conv(rows(M)) = aﬀ(rows(M)) ∩ Rq+ .


Proof. First, suppose that M is a slack matrix of some polytope. Then by Corollary 7, we have that M satisﬁes (6) and ∈ M ·Rq. Hence, there exists some c ∈ Rq such that Mc = and the aﬃne hyperplane L = {x ∈ Rq : xTc = 1} contains the rows of M. Intersecting L with both sides of (6), we obtain (7).

For the reverse implication, let M ∈ Rp+×q be a nonnegative matrix satisfying (7). Using any isometry ϕ between the d-dimensional aﬃne subspace aﬀ(rows(M)) and Rd, we ﬁnd that M is a slack matrix of the ϕ-image of the polytope deﬁned in (7).

We have seen above that every slack matrix of a polytope P has the all-ones vector in its column span and is also a slack matrix of the homogenization cone Ph of P. The next example shows that not all slack matrices of Ph are slack matrices of P, in fact, this does not even hold for the slack matrices of Ph that have the all-ones vector in their column span.

Example 9. Let P be the square [−1,1]2. The matrix

  

  

   =

  

 

 

4 3 0 43 0 2 0 0 2

- 2

![image 7](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile7.png>)

- 3


- 2

![image 8](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile8.png>)

- 3


- 2

![image 9](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile9.png>)

- 3 1 1 −1


![image 10](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile10.png>)

![image 11](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile11.png>)

1 1 1 1 1 −1 0 0 0 0 1 −1

M =

- 1 −1 1
- 2 −2 −2


0 2 2 0 0 4 0 4

is in SPh and is in the column span of M. It is clear, however, that M is not in SP since each facet of [−1,1]2 is equidistant from the two vertices not on the facet. On the other hand, since M has the RCGC/CCGC and is in its column span, it is the slack matrix of some other polytope Q. To obtain it, write a new rank factorization of M (note that rank(M) = 3) so that the ﬁrst factor contains the all ones vector as its ﬁrst column as follows:

  

  UU−1

 

 , U =

 

 

- 2

![image 12](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile12.png>)

- 3


- 2

![image 13](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile13.png>)

- 3


- 2

![image 14](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile14.png>)

- 3 1 1 −1


1 1 1 1 1 −1 0 0 0 0 1 −1

1 0 0 1/4 1 0 1/4 0 1

M =

- 1 −1 1
- 2 −2 −2


to get

   =

  

  

  

 

  .

1 32 23 1 1 −1

4 3 0 43 0 2 0 0 2

![image 15](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile15.png>)

![image 16](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile16.png>)

![image 17](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile17.png>)

![image 18](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile18.png>)

1 1 1 1

3/4 −5/4 −1/4 −1/4 −1/4 −1/4 3/4 −5/4

M =

0 2 2 0 0 4 0 4

- 1 −1 1
- 1 −2 −2


By Lemma 5, M is the slack matrix of the cone with V-representation the rows of the ﬁrst factor and H-representation the columns of the second factor. Assuming the coordinates of this three-dimensional cone are x0,x1,x2, and slicing the cone with the hyperplane {((x0,x1,x2) : x0 = 1} gives a polytope Q with vertices (2/3,2/3),(1,−1),(−1,1),(−2,−2) and H-representation given by the columns of the second factor. Then M ∈ SQ.

- 2.3. Further Results on Slack Matrices of Cones and Polytopes. In this section we derive some more insight into the geometric relations between cones, polytopes, and their slack matrices that will be useful in later parts of the paper. We return to the setup used earlier: K is assumed to be a cone and S the slack matrix of K with respect to its representation (A,B) where A ∈ Rp×n and B ∈ Rn×q.


First, we will show that every slack matrix of a cone is the slack matrix of some pointed cone. Recall that we use lin(K) to denote the linear hull of K and lineal(K) to denote the lineality space of K. Then we have lin(K) = Rp · A and lineal(K) = leftkernel(B). A cone K is pointed if lineal(K) = {O}. Deﬁne

L := lin(K) ∩ lineal(K)⊥ = (Rp · A) ∩ (B · Rq). Then we have

lin(K) = L + lineal(K) (where the summands are orthogonal to each other) and

K = (K ∩ L) + lineal(K), where K∩L ⊆ L is a pointed (i.e., having trivial lineality space) cone with dim(K∩

- L) = dim(L). Denoting by A′ ∈ Rp×n the matrix obtained from A by orthogonal projections of all rows to L, we have


K ∩ L = Rp+ · A′ and S = A′B .

By mapping L isometrically to Rdim(L), we thus ﬁnd that S is a slack matrix of the pointed cone that is the image of K ∩ L under that map and we get the following:

- Lemma 10. A matrix is a slack matrix of a polyhedral cone if and only if it is a slack matrix of some pointed polyhedral cone.

If the cone K is pointed, then for every zero-row of S = AB the corresponding row of A is a zero-row as well. Hence, removing any zero-row from S results in another slack matrix of K. A similar statement clearly holds for adding zero-rows.

- Lemma 11. If a matrix S is a slack matrix of a pointed polyhedral cone K then every matrix obtained from S by adding or removing zero-rows is a slack matrix of K as well.

Lemmas 10 and 11 together also imply this statement:

- Lemma 12. If a matrix is a slack matrix of some polyhedral cone then every matrix obtained from it by adding or removing zero-rows is a slack matrix of some polyhedral cone as well.

Let us further investigate the linear map x  → xTB. It induces the isomorphism

(8) L −−−−−−−−→·B

isomorphism

Rp · S between the linear space L and the row span of S because of the relations:

L ⊆ lineal(K)⊥ = leftkernel(B)⊥ and

L · B = (L + lineal(K)) · B = lin(K) · B = (Rp · A) · B = Rp · S . It also induces the isomorphism

K ∩ L −−−−−−−−→·B

isomorphism

Rp+ · S

between the cone K ∩L and the cone spanned by the rows of S since (K ∩L)·B = ((K ∩ L) + lineal(K)) · B = K · B = (Rp+ · A) · B = Rp+ · S. In particular, we have shown the following result:

- Lemma 13. A polyhedral cone K is pointed if and only if dim(K) = rank(S) for any slack matrix S of K.


Recall that if P is a polytope with representation (V,W,w) and slack matrix S = [ ,V ] · B where

wT −WT

B =

,

then the homogenization Ph of P is a pointed cone that also has S as a slack matrix. Since Ph is pointed, L contains the entire cone and we can restrict the isomorphism in (8) to the set {1} × P = conv(rows([ ,V ])). Thus we have that {1} × P is isomorphic to conv(rows([ ,V ])) · B = conv(rows(S)). This establishes the ﬁrst part of the following:

Theorem 14. If S is a slack matrix of the polytope P, then P is isomorphic to conv(rows(S)). In addition, we have dim(P) = rank(S) − 1.

Proof. To prove the second statement, note that dim(Ph) = dim(P) + 1. By Lemma 13, we have that dim(Ph) = rank(S).

In the conic case, we had that M ∈ SK if and only if MT ∈ SK∗. This correspondence breaks down for polytopes as we see in the example below. The reason behind this is that we cannot scale V-representations of polytopes by positive scalars.

Example 15. The matrix





1 1 0 0 0 1 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 1 0 0 0 1 1

M =

 

 

is a slack matrix for the triangular prism in R3. Thus, by Corollary 7, M satisﬁes both the RCGC and the CCGC, and the all ones-vector is in the column span of M. However, the all-ones vector is not in the row span of M, so MT is not the slack matrix of any polytope.

Despite this complication, we can still derive some results for transposes of slack matrices of polytopes. Recall that the polar of a polytope P ⊂ Rn is

P◦ = {y ∈ Rn : xTy ≤ 1 for all x ∈ P} .

Then P◦ is a polytope whenever 0 ∈ int(P), the interior of P. Since translating P does not change its slack matrices, we may assume that 0 ∈ int(P). Therefore, P has an H-representation of the form P = {x ∈ Rn : Wx ≤ } and P◦ = conv(rows(W)). Similarly, if P = conv(rows(V )), then P◦ = {x ∈ Rn : V x ≤ }. This implies that the slack matrix of P with respect to the representation (V,W, ) is the transpose of the slack matrix of P◦ with respect to the representation (W,V, ) and we get the following result that is analogous to Proposition 2 for cones.

Proposition 16. For any polytope P, there exists a slack matrix M ∈ SP such that MT is also a slack matrix of a polytope.

In the light of Theorem 6, this says that slack matrices of polytopes (which already have in their column span) allow positive scalings of their columns that puts into their row span as well. This is false for general nonnegative matrices.

Example 17. Continuing Example 15, we see that the following matrix M′ obtained by scaling the columns of M is also a slack matrix of the same prism and does have in its row span:





2 2 0 0 0 2 0 4 0 0 2 0 0 4 0 0 2 0 0 2 0 0 4 0 2 0 0 0 4 2

M′ =

.

 

 

The prism has vertices:

(0,1,−1),(2,−1,−1),(−2,−1,−1),(0,1,1),(2,−1,1),(−2,−1,1) and M′ comes from the facet description:

z ≤ 1,−y ≤ 1,−x + y ≤ 1,x + y ≤ 1,−z ≤ 1.

Therefore, P◦ has vertices (0,0,1),(0,−1,0),(−1,1,0),(1,1,0),(0,0,−1) and is a bisimplex with slack matrix M′T.

We can also show a converse to Proposition 16.

Proposition 18. Suppose M ∈ Rp+×q such that M and MT are both slack matrices of polytopes. Then there exists a polytope P, with 0 ∈ int(P), such that M ∈ SP and MT ∈ SP◦.

Proof. Since MT is a slack matrix of a polytope, we have that ∈ Rp+·M. Without loss of generality, we can scale M by a positive scalar so that ∈ conv(rows(M)).

Let M be a slack matrix of a polytope R with dim(R) = d. By Theorem 14, rank(M) = d + 1. Since the convex hull of the rows of M is isomorphic to R, we have that the aﬃne hull of the rows of M has dimension d. Let J denote the all-ones matrix of dimension p × q. Since is contained in the aﬃne hull of the rows of M, we have that the aﬃne hull of the rows of M − J passes through the origin and has dimension d. Hence, rank(M − J) = d. This implies that we can write M − J = AB with A ∈ Rp×d and B ∈ Rd×q.

Let A′ = ( ,A) and let B′ = ,BT T. Then M = A′B′ is a rank factorization of M. Let P := conv(rows(A)) and Q := {x ∈ Rd : + xTB ≥ O}. Then the rows of A′ form a V-representation of Ph and the columns of B′ form a H-representation for Qh = {(x0,x) ∈ Rd+1 : x0 + xTB ≥ O}. By Lemma 5, Ph = Qh which implies that P = Q. Therefore, M is a slack matrix of P and MT is a slack matrix of P◦.

3. An Algorithm to Recognize Slack Matrices

In this section, we discuss the algorithmic problem of deciding whether a given nonnegative matrix has the RCGC (or, equivalently, the CCGC). According to Corollaries 4 and 7 this is the crucial step to be performed in order to decide whether a given matrix is a slack matrix of a cone or a polytope.

We start with a promising result:

- Theorem 19. The problem to decide whether a nonnegative matrix satisﬁes the RCGC (or the CCGC) is in coNP. In particular, the same holds for checking the property of being a slack matrix (of a cone or of a polytope).


Proof. If the given matrix M ∈ Rp+×q does not satisfy the RCGC, then there is some point x ∈ Rp · M ∩ Rq+ \ Rp+ · M (which can be chosen to have coordinates whose encoding lengths are bounded polynomially in the encoding length of M). The fact that x  ∈ Rp+ · M can be certiﬁed by the help of some separating hyperplane whose normal vector can be chosen to have coordinates with encoding length bounded polynomially in the encoding length of M as well.

Next, we are going to describe an algorithm to check the CCGC (equivalently, the RCGC) for a nonnegative matrix. By Corollary 4, this algorithm will then provide a method to check if a given nonnegative matrix is a slack matrix of a cone. To check if the matrix is the slack matrix of a polytope (see Corollary 7), we can add the additional step of checking if the all-ones vector is in the column span of the matrix which is doable in polynomial time. A SAGE worksheet implementing this code can be found at http://www.math.washington.edu/∼rzr.

Algorithm to check if a nonnegative matrix has the CCGC

Input: A matrix M ∈ Rp+×q. Output: True if M has the CCGC and False otherwise.

- (1) Compute a basis L for the left kernel of M. For each vector ℓ in L, generate the equation ℓTx = 0.
- (2) Generate an H-representation of the cone K with the equations from the previous step and the inequalities x1 ≥ 0,...,xp ≥ 0.
- (3) Compute a minimal V-representation of K.
- (4) Normalize the vectors in the V-representation and the columns of M.
- (5) Check that each normalized vector in the V-representation is a normalized column of M. If so, return True. If not, return False.


Proof. We have K = M ·Rq ∩Rp+ and M ·Rq+ ⊆ K due to the nonnegativity of M. Thus, M satisﬁes the CCGC if and only if K ⊆ M · Rq+ holds, which is what the algorithm checks in the last three steps (note that all cones involved are pointed because they are contained in Rp+).

The only computationally challenging part of the algorithm is converting from the H-representation of K to a V-representation. There are several algorithms to do this, and we refer to [6], [9], and [11] for information on the diﬀerent techniques. No polynomial time algorithm for this conversion exists, since the V-representation may have size exponential in that of the H-representation. If the dimension of the cone is ﬁxed, however, then there do exist polynomial time algorithms for the conversion [3]. Thus, we obtain the following complexity results.

- Theorem 20. For ﬁxed r, checking whether a rank r matrix satisﬁes the RCGC (CCGC) can be done in polynomial time. In particular, checking whether matrices of ﬁxed rank are slack matrices of cones or polytopes can be done in polynomial time.

Given an H-polyhedron P and a V-polytope Q contained in P, the problem of deciding whether P = Q is known as the polyhedral veriﬁcation problem. The complexity of this problem is unknown [13]. However, a polynomial time algorithm for the polyhedral veriﬁcation problem would yield an output sensitive algorithm for the problem of computing the facets of a polytope given in V-representation, and thus solve a decades old open problem in computational geometry (see [7]).

Clearly, given a V-polytope it is easy to check whether it is contained in an H-polyhedron. The reverse problem of checking whether an H-polyhedron is contained in a V-polytope is known to be coNP-complete [4]. Note that the polyhedral veriﬁcation problem is the restriction of the latter problem to those instances in which the V-polytope is contained in the H-polyhedron (see also

http://www.inf.ethz.ch/personal/fukudak/polyfaq/node21.html, [8] and [12]).

- Theorem 21. The following problems can be reduced in polynomial time to each other:


- (1) The polyhedral veriﬁcation problem
- (2) Is a given matrix a slack matrix of a polytope?
- (3) Is a given matrix a slack matrix of a cone?
- (4) Does a given matrix satisfy the RCGC/CCGC?


Proof. Corollary 7 shows that (2) can be reduced (in polynomial time) to (4) (since checking whether is contained in the column space can be done in polynomial time) and Corollary 4 shows that (4) can be reduced to (3).

We can also reduce (3) to (2): Suppose we need to check whether a given matrix M is a slack matrix of a cone. By Lemma 11, we can assume that M has no zero rows. We can also scale the rows of M by positive scalars without eﬀect on M being a slack matrix of a cone. Using these two facts, we can assume that is in the column span of M. Then, being a slack matrix of a cone is equivalent to being a slack matrix of a polytope due to Theorem 6.

Since Corollary 8 shows how to reduce (2) to (1), it thus remains to establish a reduction of (1) to (2). Let Q = conv(rows(V )) with V ∈ Rp×n and P = {x ∈ Rn : Wx ≤ w} with W ∈ Rq×n and w ∈ Rq with Q ⊆ P. Suppose we need to decide whether P = Q. First, we check whether P is pointed (i.e., W has a trivial right kernel) and dim(P) = dim(Q) (both checks can be done in polynomial time, the second one using linear programming). If either check fails, then P = Q.

So let us assume dim(P) = dim(Q) and that P is pointed. The latter fact implies that the aﬃne map ϕ : Rn → Rq deﬁned via ϕ(x) = w − Wx is injective. Let M be the matrix arising from V by applying ϕ to each row. Then, due to Q ⊆ P, we have that M is nonnegative. According to Corollary 8, the matrix M is a slack matrix of a polytope if and only if

- (9) conv(rows(M)) = aﬀ(rows(M)) ∩ Rq+. Since we have


conv(rows(M)) = ϕ(conv(rows(V ))) = ϕ(Q) and

aﬀ(rows(M)) ∩ Rq+ = ϕ(aﬀ(rows(V ))) ∩ Rq+ = ϕ(aﬀ(Q)) ∩ Rq+

= ϕ({x ∈ aﬀ(Q) : ϕ(x) ≥ O}) = ϕ(P ∩ aﬀ(Q)) = ϕ(P)

(here we used that dim(P) = dim(Q)), condition (9) is equivalent to ϕ(P) = ϕ(Q). In turn, this is equivalent to P = Q since ϕ is injective. Thus, P = Q is equivalent to M being the slack matrix of a polytope.

4. A Combinatorial Characterization of Slack Matrices

Our second characterization of slack matrices of cones and polytopes relies on incidence structures. For a (nonnegative) matrix M, we denote by Minc the 0/1matrix with (Minc)ij = 1 if and only if Mij = 0. The matrices Minc arising from slack matrices M of a polyhedral cone K or of a polytope P are called the incidence matrices of K or P, respectively.

We start by characterizing the slack matrices of polytopes, since the corresponding statement for cones can easily be deduced from the one for polytopes. The characterization is restricted to nonnegative matrices of rank at least two. It is easy to see that no matrix of rank one is a slack matrix of a nontrivial polytope. One may (or may not) want to consider a rank-zero matrix as a slack matrix of the polytope consisting of the zero-vector in R0.

- Theorem 22. A nonnegative matrix M with rank(M) ≥ 2 is a slack matrix of


some polytope if and only if Minc is an incidence matrix of some (rank(M) − 1)dimensional polytope and is contained in the column span of M.

Proof. If M is a slack matrix of a polytope P, then is contained in the column span of M (Theorem 6), and by Theorem 14, dim(P) = rank(M) − 1.

In order to establish the non-trivial implication of the claim, let M ∈ Rp+×q be a nonnegative matrix with rank(M) = d + 1 ≥ 2, ∈ M · Rq and Minc an incidence matrix of some d-dimensional polytope R. Denote by V ⊆ Rq+ the set of rows of M and deﬁne the polytope P := conv(V ) and the polyhedron Q := aﬀ(V ) ∩ Rq+. Clearly, P ⊆ Q, and since ∈ M · Rq, dim(Q) = dim(P) = d. By Corollary 8, in order to show that M is a slack matrix of a polytope, it suﬃces to prove P = Q.

In order to establish Q ⊆ P, let us deﬁne

Vi = {v ∈ V : vi = 0} and Fi = conv(Vi) for 1 ≤ i ≤ q . The set

q

Fi

F =

i=1

is contained in the relative boundary ∂Q of Q. Note that as an incidence matrix of some polytope of dimension at least one, Minc does not have an all-ones column. Since Q = conv(∂Q) (note that Q is a pointed polyhedron of dimension d ≥ 2, which is important here in case of Q being unbounded), if we show that F = ∂Q, then we will have that Q = conv(F) ⊆ P.

Thus, our goal is to establish F = ∂Q. As mentioned above, we have F ⊆ ∂Q. It suﬃces to show that F is homotopy-equivalent to a (d − 1)-dimensional sphere1, because then F cannot be properly contained in the (d − 1)-dimensional connected (recall dim(Q) ≥ 2) manifold ∂Q. This follows, e.g., from [2, Cor. 8.5] together with the fact that the (d − 1)-st cohomology group of a (d − 1)-dimensional sphere is non-trivial.

To show that F is homotopy-equivalent to a (d− 1)-dimensional sphere, observe that for every subset I ⊆ {1,...,q}, we have ∩i∈IFi = ∅ if and only if the submatrix of Minc formed by the columns indexed by I has an all-ones row. Now let R be a polytope of which Minc is an incidence matrix. Let G1,...,Gq be the faces of R that correspond to the columns of Minc. Then ∩i∈IGi = ∅ holds if and only if the submatrix of Minc formed by the columns indexed by I has an all-ones row.

Therefore, the abstract simplicial complexes {I ⊆ {1,...,q} :

Fi = ∅}, and {I ⊆ {1,...,q} :

Gi = ∅}

i∈I

i∈I

(known as the nerves of the polyhedral complexes induced by F1,...,Fq and by G1,...,Gq, respectively) are identical. Since all intersections i∈I Fi and i∈I Gi are contractible (in fact, they are even convex), this simplicial complex is homotopy equivalent to both F and to the (d − 1)-dimensional (polyhedral) sphere ∂R (see, e.g., [1, Thm. 10.6]).

Since polygons have a very simple combinatorial structure, Theorem 22 readily yields a simple characterization of their slack-matrices. Here, a vertex-facet slack matrix of a polytope P is a slack matrix of P whose rows and columns are in one-to-one correspondence with the vertices and facets of P, respectively.

Corollary 23. A matrix M ∈ R+n×n (n ≥ 3) is a vertex-facet slack matrix of an n-gon if and only if its rows span an aﬃne space of dimension exactly two and its rows and columns can be permuted such that the non-zero entries appear exactly at the positions (i,i) (for 1 ≤ i ≤ n), and (i,i − 1) (for 2 ≤ i ≤ n), and (1,n).

![image 25](<2013-gouveia-which-nonnegative-matrices-slack_images/imageFile25.png>)

1Our proof of this is inspired by [7].

Steinitz’ theorem [14] says that a graph G is the 1-skeleton of a three-dimensional polytope if and only if G is planar and three-connected. Using this, one can check in polynomial time whether a given 0/1-matrix is an incidence matrix of a threedimensional polytope. For every ﬁxed d ≥ 4, however, it is NP-hard to decide whether a given 0/1-matrix is an incidence matrix of a d-dimensional polytope [10].

In the following combinatorial characterization of slack matrices of cones we restrict our attention to matrices of rank at least two as for polytopes. Clearly, every nonnegative matrix of rank one is a slack matrix of the ray R1+, and, we may consider a matrix of rank zero as a slack matrix of the trivial cone {0} in R0.

Theorem 24. A nonnegative matrix M with rank(M) ≥ 2 is a slack matrix of a polyhedral cone if and only if Minc is an incidence matrix of some rank(M)dimensional pointed polyhedral cone.

Proof. If M is a slack matrix of some polyhedral cone then, by Lemma 10, M is a slack matrix (and hence Minc is an incidence matrix) of a pointed polyhedral cone K. By Lemma 13 this cone has dimension rank(M).

In order to prove the reverse implication, we can assume by the results in Section 2.3 that M does not have any zero-row. Since M is also nonnegative, there exists a positive diagonal matrix D such that DM contains in its column span.

Given a pointed cone K, we can slice K by an aﬃne hyperplane L such that the slice is a polytope of dimension dim(K) − 1 and the incidence structures of K and K ∩ L are identical. Thus, (DM)inc is an incidence matrix of some (rank(M) − 1)-dimensional polytope. By Theorem 22, we have that DM is a slack matrix of a polytope. Hence, M is a slack matrix of the homogenization cone of this polytope.

Note that dropping pointed from the formulation of Theorem 24 makes the statement false. Indeed,

   with Minc =

  

  

  

- 1 2
- 2 1 0 0 0 0


- 0 0

- 0 0
- 1 1


- 1 1


M =

and rank(M) = 2 is not a slack matrix (since M does not satisfy the RCGC), but Minc is the incidence matrix of the non-pointed cone {(x1,x2) : x2 ≥ 0} with V-representation (0,1), (0,1), (1,0), (−1,0) and H-representation (0,1), (0,1).

References

- [1] A. Bjo¨rner. Topological methods. In: Handbook of combinatorics, Elsevier, pp. 1819–1872, 1995.
- [2] G.E. Bredon. Topology and geometry. Graduate Texts in Mathematics 139, Springer, 1993.
- [3] M.E. Dyer. The complexity of vertex enumeration methods. Mathematics of Op. Res., 8(3):381–402, 1983.
- [4] R. Freund and J. Orlin. On the complexity of four polyhedral set containment problems. Math. Programming, 33:133-145, 1985.
- [5] J. Gouveia, P.A. Parrilo, and R.R. Thomas. Lifts of convex sets and cone factorizations. Mathematics of OR, to appear, doi:10.1287/moor.1120.0575
- [6] M. Joswig. Chapter 64: Software. In Jacob E. Goodman and Joseph ORourke, eds.., Handbook of Discrete and Computational Geometry, 2nd edition, 14151433. CRC Press, 2004.
- [7] M. Joswig and G.M. Ziegler. Convex hulls, oracles, and homology. J. Symbolic Comput., 38(4):1247–1259, 2004.


- [8] V. Kaibel and M.E. Pfetsch. Some algorithmic problems in polytope theory. In Algebra, geometry, and software systems, pp. 23–47, Springer, Berlin, 2003.
- [9] T.H. Matheiss and D. Rubin. A Survey and Comparison of Methods for Finding All Vertices of Convex Polyhedral Sets. Mathematics of Op. Res., 5(2):167–185, 1980.
- [10] J. Richter-Gebert. Realization Spaces of Polytopes. Lecture Notes in Mathematics 1643, Springer, 1996.
- [11] R. Seidel. Chapter 22: Convex Hull Computations. In Jacob E. Goodman and Joseph ORourke, eds.., Handbook of Discrete and Computational Geometry, 2nd edition, 495512. CRC Press, 2004.
- [12] P.D. Seymour. A Note on Hyperplane Generation. Journal of Comb. Theory, Series B, 61(1):88–91, 1994.
- [13] V. Kaibel and M.E. Pfetsch. Some algorithmic problems in polytope theory. In: Algebra, geometry, and software systems, Springer, 2004, 23–47.
- [14] E. Steinitz and H. Rademacher. Vorlesungen ber die Theorie der Polyeder. Springer, 1934 (reprint 1976).
- [15] M. Yannakakis. Expressing combinatorial optimization problems by linear programs. J. Comput. System Sci., 43(3):441–466, 1991.


CMUC, Department of Mathematics, University of Coimbra, 3001-454 Coimbra, Por-

tugal E-mail address: jgouveia@mat.uc.pt Universit´e Paris 13, Sorbonne Paris Cit´e, LIPN, CNRS, (UMR 7030), F-93430, Vil-

letaneuse, France E-mail address: Roland.Grappe@lipn.univ-paris13.fr Otto-von-Guericke Universitat¨ Magdeburg, Fakutat¨ fur¨ Mathematik, 39106 Magde-

burg, Germany E-mail address: kaibel@ovgu.de Dipartimento di Matematica, Universita` degli Studi di Padova, Via Trieste 63, 35121

Padova, Italy E-mail address: pashkovich@math.unipd.it Department of Mathematics, University of Washington, Box 354350, Seattle, WA

98195, USA E-mail address: rzr@uw.edu Department of Mathematics, University of Washington, Box 354350, Seattle, WA

98195, USA E-mail address: rrthomas@uw.edu

