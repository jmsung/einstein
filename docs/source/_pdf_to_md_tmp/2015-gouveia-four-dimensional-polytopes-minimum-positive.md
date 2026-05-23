# arXiv:1506.00187v3[math.CO]25Jul2016

## FOUR-DIMENSIONAL POLYTOPES OF MINIMUM POSITIVE SEMIDEFINITE RANK

JOAO˜ GOUVEIA, KANSTANSTIN PASHKOVICH, RICHARD Z. ROBINSON, AND REKHA R. THOMAS

Abstract. The positive semideﬁnite (psd) rank of a polytope is the size of the smallest psd cone that admits an aﬃne slice that projects linearly onto the polytope. The psd rank of a d-polytope is at least d + 1, and when equality holds we say that the polytope is psd-minimal. In this paper we develop new tools for the study of psd-minimality and use them to give a complete classiﬁcation of psd-minimal 4-polytopes. The main tools introduced are trinomial obstructions, a new algebraic obstruction for psd-minimality, and the slack ideal of a polytope, which encodes the space of realizations of a polytope up to projective equivalence.

Our central result is that there are 31 combinatorial classes of psd-minimal 4-polytopes. We provide combinatorial information and an explicit psd-minimal realization in each class. For 11 of these classes, every polytope in them is psd-minimal, and these are precisely the combinatorial classes of the known projectively unique 4-polytopes. We give a complete characterization of psdminimality in the remaining classes, encountering in the process counterexamples to some open conjectures.

1. Introduction

The positive semideﬁnite (psd) rank of a convex set was introduced in [GPT13], and it can be seen as a measure of geometric complexity of that set. Let Sk denote the vector space of all real symmetric k ×k matrices with the inner product

A,B := trace(AB), and let S+k be the cone of positive semideﬁnite matrices in Sk. A polytope P ⊂ Rd is said to have a psd lift of size k if there is an aﬃne space L ⊂ Sk and a linear map π : Sk → Rd such that P = π(S+k ∩L). The psd rank of P, rankpsd(P), is the smallest k such that P has a psd lift of size k. Linear optimization over a polytope can be achieved via semideﬁnite programming over its psd lift. Thus a lift of small size (alternatively, small psd rank of the polytope) implies, in principle, the possibility of eﬃciently solving a linear optimization problem over this polytope. These features have attracted much research on the psd rank of polytopes in recent years, with several exciting new results coming from optimization and computer

Date: November 15, 2021. Key words and phrases. polytopes; positive semideﬁnite rank; psd-minimal; slack matrix; slack

ideal.

Gouveia was partially supported by the Centre for Mathematics of the University of Coimbra – UID/MAT/00324/2013, funded by the Portuguese Government through FCT/MEC and cofunded by the European Regional Development Fund through the Partnership Agreement PT2020, Pashkovich by F.R.S.-FNRS research project T.0100.13, Semaphore 14620017, Robinson by the U.S. National Science Foundation Graduate Research Fellowship under Grant No. DGE-0718124, and Thomas by the U.S. National Science Foundation grant DMS-1418728.

1

science [BDP13], [LRS14], [LWdW14], [LW14], [FP13], [FSP]. For a survey on psd rank of nonnegative matrices, see [FGP+15].

Since polytopes of small psd rank can admit eﬃcient algorithms for linear optimization, there is much incentive to understand them. If P is a d-polytope, then rankpsd(P) ≥ d + 1, and if equality holds, we say that P is psd-minimal. These polytopes are a natural place to start the study of small psd rank, a task that was initiated in [GRT13]. A well-known example of a psd-minimal polytope is the stable set polytope of a perfect graph [Lov79]. In this case, psd-minimality implies that the size of a largest stable set in a perfect graph can be found in polynomial time, while computing the size of a largest stable set in a graph is NP-hard in general. The existence of a small psd lift for the stable set polytopes of perfect graphs is the only known proof of the polynomial time solvability of the stable set problem in this class of graphs.

The stable set polytope of a perfect graph is also an example of a 2-level polytope [GPT10]. These are polytopes with the property that for each facet of the polytope there is a unique parallel translate of its aﬃne hull containing all vertices of the polytope that are not on the facet. All 2-level polytopes are psd-minimal and aﬃnely equivalent to 0/1-polytopes with additional special properties, yet they are far from well-understood and oﬀer many challenges. Several groups of researchers have been studying them recently [GSa], [BFF+b], [BFF+a]. The study of psdminimal polytopes is an even more ambitious task than that of 2-level polytopes, yet it is an important step in understanding the phenomenon of small psd rank, and oﬀer a rich set of examples for honing psd rank techniques.

The only psd-minimal 2-polytopes are triangles and quadrilaterals. This already helps in the classiﬁcation of higher dimensional psd-minimal polytopes, due to the following useful lemma.

- Lemma 1.1. [GRT13, Proposition 3.8] Any face of a psd-minimal polytope is psdminimal.


Therefore psd-minimal 3-polytopes can only have triangular or quadrilateral facets but still turn out to be interesting. Call an octahedron in R3, biplanar, if there are two distinct planes each containing four vertices of the octahedron. A complete classiﬁcation of psd-minimal 3-polytopes is known.

- Theorem 1.2. [GRT13, Theorem 4.11] The psd-minimal 3-polytopes are precisely simplices, quadrilateral pyramids, bisimplices, biplanar octahedra and their polars.


Recall that if P is a d-polytope containing the origin in its interior, then its polar is P◦ := {y ∈ Rd : x,y ≤ 1 ∀ x ∈ P}. A polytope P has a psd lift of size k if and only if P◦ has a psd lift of size k, and in particular, rankpsd(P) = rankpsd(P◦). The polar of a combinatorial octahedron is a combinatorial cube. The above theorem shows that psd rank is not a combinatorial property; not all polytopes that are combinatorially equivalent to octahedra and cubes are psd-minimal, the embedding matters. Since psd-minimality is closed under polarity and the combinatorial type of the polar depends only on the combinatorial type of the original polytope, we frequently refer to dual pairs of combinatorial types, namely, a pair of combinatorial classes such that the polytopes in one are the polars of those in the other.

If P ⊂ Rd is a polytope with vertices v1,...,vn, and facet inequalities a j x ≤ βj for j = 1,...,m, then the slack matrix of P is the nonnegative matrix SP ∈ Rn×m such that (SP)ij := βj − a j vi, the slack of the vertex vi in the facet inequality

a j x ≤ βj. If P is a d-polytope with d ≥ 1, then rank(SP) = d + 1, and note that the zero pattern in SP records the vertex-facet incidence structure of P, or equivalently, the combinatorics of P.

An S+k-factorization of SP is an assignment of psd matrices A1,...,An ∈ S+k and B1,...,Bm ∈ S+k to the rows and columns, respectively, of SP such that (SP)ij = βj −a j vi = Ai,Bj . The psd rank of SP, denoted as rankpsd(SP), is the minimum k for which SP admits a factorization through S+k. The connection to psd lifts of the polytope P comes via the result from [GPT13] that P has a psd lift of size k if and only if SP has an S+k-factorization, and hence rankpsd(P) = rankpsd(SP).

There is another notion of rank that plays a key role in the study of psdminimality. A Hadamard square root of SP is a matrix obtained by replacing every positive entry in SP with one of its two square roots. The positive Hadamard square root

√SP is the Hadamard square root obtained by replacing every positive entry by its positive square root. The square root rank of SP, denoted as rank√ (SP), is the minimum rank of a Hadamard square root of SP.

+

- Theorem 1.3. [GRT13] A d-polytope P ⊂ Rd with d ≥ 1 is psd-minimal if and only if


rank√ (SP) = d + 1.

- 1.1. Contribution. In this paper, we classify psd-minimal 4-polytopes. The techniques used in the classiﬁcation of psd-minimal 3-polytopes do not have a natural generalization to 4-polytopes, so new tools and approaches had to be developed. These are of interest beyond the scope of this classiﬁcation, and oﬀer insight on psd-minimality in general. As a by-product, we obtain simpler proofs of the classiﬁcation results for 2- and 3-dimensional polytopes.


In terms of techniques, this paper has two main contributions. The ﬁrst is the notion of trinomial obstruction, that provides a simple certiﬁcate that a polytope is not psd-minimal. This obstruction is powerful enough to completely classify the combinatorial types of psd-minimal 4-polytopes. The second main technical contribution is the notion of the slack ideal of a polytope. We show that the positive real zeros of this ideal are essentially in bijection with the diﬀerent projective equivalence classes in the combinatorial class of the polytope. Using slack ideals we develop a general computational algebra procedure for characterizing the psd-minimal polytopes in a combinatorial class. This is used to complete the classiﬁcation.

At a high level, our results are as follows. We prove that there are 31 combinatorial classes of psd-minimal 4-polytopes, and they are described in Table 1. Combinatorial information about each class such as its f-vector and types of facets is listed. We also exhibit an explicit psd-minimal polytope in each of the 31 combinatorial classes. We then proceed to characterize the psd-minimal polytopes in each of these classes. In 11 of them, every polytope is psd-minimal. Coincidentally these classes are also precisely the classes of the 11 known projectively unique 4-polytopes. For the remaining 20 classes, we derive precise conditions for psdminimality. In most cases, the conditions can be seen as aﬃne constraints on the entries of the slack matrices. However we get two interesting new behaviors. For two pairs of primal-dual classes, including the 4-cube and its dual, there are two essentially diﬀerent types of psd-minimal realizations. For two other pairs of primaldual classes, psd-minimality is characterized by non-linear algebraic conditions, and

they settle negatively some open conjectures ([BKLT13, Problem 2] and generalizations). In particular they give us the ﬁrst examples of psd-minimal polytopes whose minimality cannot be certiﬁed by the positive Hadamard square root of the slack matrix.

- 1.2. Organization. The results in this paper naturally split into two parts, which guides the organization of the sections. In the ﬁrst part, we consider combinatorial properties of, and obstructions to, psd-minimality. In Section 2 we develop a lower bounding method for the square root rank of a matrix and illustrate it by deriving a short proof of the psd-minimality results for 2- and 3-polytopes up to combinatorial equivalence. In Section 3 we specify the obstructions to psd-minimality on the slack matrices of 4-polytopes and derive four combinatorial results that constrain the types of facet intersections that are possible for psd-minimal 4-polytopes. These results allow us in Section 4 to precisely identify the 31 combinatorial classes of psdminimal 4-polytopes concluding the ﬁrst part of the paper. An explicit psd-minimal polytope in every combinatorial class, as well as various combinatorial properties of each class can be found in Table 1. We refer to each class by its number in Table 1.

In the second half of the paper, we identify the conditions for psd-minimality in each of the 31 combinatorial classes. This requires new algebraic and geometric tools. In Section 5 we introduce the slack ideal of a polytope, and prove that if this ideal is binomial, then all polytopes that are combinatorially equivalent to this polytope are psd-minimal. Next we prove that if a d-polytope has d + 2 vertices, its slack ideal is binomial, and ﬁnally we show that the slack ideals of classes 1-11 are binomial. In Section 6 we consider the combinatorial classes 1215 from Table 1 which come in two dual pairs. The slack ideal is used to derive a parametrization of the slack matrices of the psd-minimal polytopes in each of these classes. As mentioned above, these examples are particularly interesting since they provide counterexamples to several conjectures about psd-minimality that one might entertain based on the results in [GRT13]. We discuss these features in detail. We conclude in Section 7 with the precise conditions under which the remaining classes in Table 1 are psd-minimal. As an illustration of our new methods, we use them to reprove that biplanarity is a necessary and suﬃcient condition for the psdminimality of octahedra, ﬁnishing a new proof of Theorem 1.2. The codes for the main calculations in this paper can be found at: http://kanstantsinpashkovich. bitbucket.org/computations/psd_minimal_four_polytopes.html in the form of Sage [S+15] worksheets that rely on Macaulay2 [GSb].

- 1.3. Slack matrices of projectively equivalent polytopes. We conclude the introduction with a simple result that relates the slack matrices of projectively equivalent polytopes which is used extensively in the later parts of this paper.


Recall that two polytopes P and Q in Rd are projectively equivalent if and only if there exists a projective transformation sending P to Q, i.e. Q = φ(P) where

Bx + b c x + γ

φ : Rd → Rd, φ(x) :=

- (1)

for some B ∈ Rd×d,b ∈ Rd,c ∈ Rd and γ ∈ R such that det

B b c γ

- (2) = 0.


A convenient way to think of projective equivalence is in terms of homogenizations. Recall that given a polytope P ⊆ Rd with vertices v1,...,vn, its homogenization is the convex cone homog(P) ⊆ Rd+1 spanned by (v1,1),...,(vn,1) ∈ Rd+1.

- Lemma 1.4. Two polytopes P,Q ⊂ Rd are projectively equivalent if and only if the cones homog(P) and homog(Q) in Rd+1 are linearly isomorphic.


Proof. The cones homog(P) and homog(Q) are linearly isomorphic if and only if there exists a linear map from Rd+1 → Rd+1 with invertible representing matrix

B b c γ

that sends homog(P) to homog(Q). By equating Q to the dehomogenization of the image of homog(P), one sees that this happens if and only if for ϕ(x) := cBx x++bγ we have Q = ϕ(P), i.e., if and only if P and Q are projectively equivalent.

Corollary 1.5. Two polytopes are projectively equivalent if and only if they have the same slack matrix up to permutations and positive scalings of rows and columns.

Proof. Slack matrices of cones are deﬁned analogously to slack matrices of polytopes: each entry of the slack matrix is indexed by an extreme ray and a facet of the cone, and contains the corresponding slack value. By deﬁnition, scaling the rows and columns of a slack matrix of a cone by positive real numbers produces another slack matrix of the same cone.

Moreover, a slack matrix of a polytope P is a slack matrix of the cone homog(P) and therefore, by Lemma 1.4, it suﬃces to prove that two pointed cones are linearly isomorphic if and only if they have a common slack matrix. It is easy to see that two linearly isomorphic cones have the same slack matrices. On the other hand, the reasoning in [GGK+13, Theorem 14] shows that every pointed cone is linearly isomorphic to the cone spanned by the rows of its slack matrix. Thus if two pointed cones have the same slack matrix, they are linearly isomorphic to the same cone, and hence to each other.

Acknowledgments. We thank Arnau Padrol and Serkan Hos¸ten for useful inputs to this paper. We also thank the referees for their valuable comments.

2. Trinomial obstructions to psd-minimality

Recall that two polytopes P and Q are combinatorially equivalent if they have the same vertex-facet incidence structure. In this section we describe a simple algebraic obstruction to psd-minimality based on the combinatorics of a given polytope, therefore providing an obstruction for all polytopes in the given combinatorial class. Our main tool is a symbolic version of the slack matrix of a polytope deﬁned as follows.

- Deﬁnition 2.1. The symbolic slack matrix of a d-polytope P is the matrix, SP(x), obtained by replacing all positive entries in the slack matrix SP of P with distinct variables x1,...,xt.


Note that two d-polytopes P and Q are in the same combinatorial class if and only if SP(x) = SQ(x) up to permutations of rows and columns, and names of variables. In this paper we say that a polynomial f ∈ R[x1,...,xt] is a monomial if it is of the form f = ±xa where xa = xa

### 1 ···xa

### t and a = (a1,...,at) ∈ Nt. We

1

t

refer to a sum of two distinct monomials as a binomial and to the sum of three distinct monomials as a trinomial. This diﬀers from the usual terminology where nontrivial coeﬃcients are allowed.

- Lemma 2.2 (Trinomial Obstruction Lemma). Suppose the symbolic slack matrix


SP(x) of a d-polytope P has a (d + 2)-minor that is a trinomial. Then no polytope in the combinatorial class of P can be psd-minimal.

Proof. Suppose Q is psd-minimal and combinatorially equivalent to P. Hence, we can assume that SP(x) equals SQ(x). By Theorem 1.3 there is some u = (u1,...,ut) ∈ Rt, with no coordinate equal to zero, such that SQ = SP(u21,...,u2t) and rankSP(u) = d + 1. Since SQ is the slack matrix of a d-polytope, we have

rankSP(u21,...,u2t) = d + 1 = rankSP(u1,...,ut).

Now suppose D(x) is a trinomial (d + 2)-minor of SP(x). Up to sign, D(x) has the form xa + xb + xc or xa − xb + xc for some a,b,c ∈ Nt. In either case, it is not possible for D(u21,...,u2t) = D(u1,...,ut) = 0.

An interesting property of this obstruction is that it reﬂects the fact that faces of psd-minimal polytopes are psd-minimal (see Lemma 1.1): if a face of a polytope is not psd-minimal due to a trinomial obstruction, then the non psd-minimality of the polytope can also be veriﬁed by a trinomial obstruction.

- Proposition 2.3. Let P be a d-polytope with a facet F such that some (d+1)-minor of SF(x) is a trinomial. Then SP(x) has a trinomial (d + 2)-minor.

Proof. Let vertices v1,...,vd+1 of F and facets F 1,...,F d+1 of F index a (d+1)× (d + 1) submatrix of SF(x) with a trinomial determinant. Let Fi be the unique facet of P that shares F i with the facet F of P. Pick a vertex vd+2 of P not lying on F. Then the determinant of the submatrix of SP(x) indexed by v1,...,vd+2 and F1,...,Fd+1,F is a trinomial.

- 2.1. Psd-minimal 2-polytopes. Lemma 2.2 yields simple proofs of the combinatorial part of the classiﬁcation results for psd-minimal 2- and 3-polytopes that were obtained in [GRT13].


- Proposition 2.4. [GRT13, Theorem 4.7] The psd-minimal 2-polytopes are precisely all triangles and quadrilaterals.


Proof. Let P be an n-gon where n > 4. Then SP(x) has a submatrix of the form

  

  ,

0 x1 x2 x3 0 0 x4 x5

x6 0 0 x7 x8 x9 0 0

whose determinant is x1x4x7x8 −x2x5x6x9 +x3x4x6x9 up to sign. By Lemma 2.2, no n-gon with n > 4 can be psd-minimal.

Since all triangles are projectively equivalent, by verifying the psd-minimality of one, they are all seen to be psd-minimal. Similarly, for quadrilaterals.

- 2.2. Combinatorial classes of psd-minimal 3-polytopes. Lemma 2.2 can also be used to derive [GRT13, Proposition 4.10], which gives the psd-minimal classiﬁcation of 3-polytopes up to combinatorial equivalence.


Using Proposition 2.4, together with Lemma 1.1 and the invariance of psd rank under polarity, we get that that any 3-polytope P with a vertex of degree larger than four, or a facet that is an n-gon where n > 4, cannot be psd-minimal. This is enough to prove a stronger version of [GRT13, Lemma 4.9].

- Lemma 2.5. If P is a 3-polytope with a vertex of degree four and a quadrilateral facet incident to this vertex, then SP(x) contains a trinomial 5-minor.


Proof. Let v be the vertex of degree four incident to facets F1,F2,F3,F4 such that [v1,v] = F1 ∩ F2, [v2,v] = F2 ∩ F3, [v3,v] = F3 ∩ F4 and F4 ∩ F1 are edges of P, where v1, v2 and v3 are vertices of P.

Suppose F4 is quadrilateral. Then F4 has a vertex v4 that is diﬀerent from, and non-adjacent to, v. Therefore, v4 does not lie on F1, F2 or F3. Consider the F1,F2,F3,F4,F where F is a facet not containing v. This matrix has the form

- 5 × 5 submatrix of SP(x) with rows indexed by v,v1,v2,v3,v4 and columns by






0 0 0 0 x1 0 0 x2 x3 ∗ x4 0 0 x5 ∗ x6 x7 0 0 ∗ x8 x9 x10 0 ∗

,

 

 

and its determinant is a trinomial.

- Proposition 2.6. The psd-minimal 3-polytopes are combinatorially equivalent to simplices, quadrilateral pyramids, bisimplices, octahedra or their duals.


Proof. Suppose P is a psd-minimal 3-polytope. If P contains only vertices of degree three and triangular facets, then P is a simplex.

For all remaining cases, P must have a vertex of degree four or a quadrilateral facet. Since psd rank is preserved under polarity, we may assume that P has a vertex u of degree four. By Lemma 2.5, the neighborhood of u looks as follows.

- v1
- v2 v3


v4

|u|
|---|


Suppose P has ﬁve vertices. If all edges of P are in the picture, i.e. the picture is a Schlegel diagram of P, then P is a quadrilateral pyramid. Otherwise P has one more edge, and this edge is [v1,v3] or [v2,v4], yielding a bisimplex in either case.

- If P has more than ﬁve vertices, then we may assume that P has a vertex v that


is a neighbor of v1 diﬀerent from u, v2, v4. Then v1 is a degree four vertex and thus, by Lemma 2.5, all facets of P containing v1 are triangles. This implies that v is a neighbor of v2 and v4. Applying the same logic to either v2 or v4, we get that v is also a neighbor of v3. Since all these vertices now have degree four, there could be no further vertices in P, and so P is an octahedron. Hence P is combinatorially equal to, or dual to, one of the polytopes seen so far.

Proposition 2.6 proves the combinatorial part of Theorem 1.2. The rest of the proof can be seen in Section 7.

3. Facet intersection obstructions for psd-minimal 4-polytopes

We now use the trinomial obstruction lemma to show that facets of psd-minimal 4-polytopes can only intersect in a limited number of ways. In this section and beyond, when we refer to a concrete polytope we refer to its combinatorial type; for example, “cube” is used as a shortcut for “a polytope of the same combinatorial type as a cube”. Similarly, we refer to any quadrilateral as a “square”.

## 3.1. Combinatorial obstruction lemmas.

- Deﬁnition 3.1. An edge of a 3-polytope P is called a wedge if all the vertices of P are contained in the two facets of P that intersect at this edge.


- Lemma 3.2. If two facets of a psd-minimal 4-polytope P intersect at an edge, then this edge must be a wedge of both facets. Proof. Suppose the contrary: there is a facet F1 of P which intersects another facet


- F2 of P at an edge [u,v] that is not a wedge of F1. Let v1 be a vertex of P not contained in F1. Let F3 (F4 respectively) be a facet


of P which contains u but not v (contains v but not u respectively). Let F5 and

- F6 be two facets of P, which contain u and v and induce two diﬀerent facets of F1. Let v2 be a vertex of both F6 and F1, but not of F5; let v3 be a vertex of both F5 and F1, but not of F6. Moreover, since [u,v] is not a wedge of F1 there is a vertex v4 of F1, which does not lie in F5 or F6.


Consider the 6 × 6 submatrix of SP(x) with rows indexed by v1,v,u,v2,v3,v4 and columns by F1,F3,F4,F5,F6,F2. This matrix has the form





x1 ∗ ∗ ∗ ∗ ∗ 0 x2 0 0 0 0 0 0 x3 0 0 0 0 ∗ ∗ x4 0 x5 0 ∗ ∗ 0 x6 x7 0 ∗ ∗ x8 x9 x10

,

 

 

and its determinant is a trinomial, contradicting Lemma 2.2.

- Lemma 3.3. If two facets of a psd-minimal 4-polytope P intersect at a vertex, none of their facets containing that vertex is a square.


Proof. Let F1 be a facet of P which intersects another facet F2 of P at a vertex v. Suppose v is contained in a square facet F of F1.

Let F3 be a facet of P that does not contain v. Pick v1 as a vertex of P not contained in F1. Let F4 be the facet of P which intersects F1 at F . Take v2 as a vertex of F1 not contained in F . Let v3 and v4 be the neighbors of v in the square F , and let F5 and F6 be facets of P which intersect F at the edge [v4,v] and [v3,v], respectively. Denote by v5 the vertex of F diﬀerent from v, v3 and v4.

Consider the 6 × 6 submatrix of SP(x) with rows indexed by v,v1,v2,v3,v4,v5 and columns by F3,F1,F4,F5,F6,F2. This matrix has the form





x1 0 0 0 0 0 ∗ x2 ∗ ∗ ∗ ∗ ∗ 0 x3 ∗ ∗ ∗ ∗ 0 0 x4 0 x5 ∗ 0 0 0 x6 x7 ∗ 0 0 x8 x9 x10

,

 

 

and its determinant is a trinomial, contradicting Lemma 2.2.

While the above two lemmas are general, the next one deals speciﬁcally with octahedral facets. Recall that a combinatorial octahedron is psd-minimal if and only if it is biplanar (see Theorem 1.2).

- Lemma 3.4. An octahedral facet of a psd-minimal 4-polytope cannot intersect another facet of the polytope at a vertex. Proof. Suppose there are facets F and G of a psd-minimal 4-polytope P, such that


- F is octahedral and F ∩ G = {v1}, where v1 is a vertex of P. Consider the submatrix M of SP with rows indexed by the vertices v1,...,v6


of the octahedral facet and columns indexed by the facets F1,...,F8 and G of P, such that F1 ∩ F, ..., F8 ∩ F are diﬀerent facets of F. The symbolic form of M is





x1 x2 x3 x4 0 0 0 0 0

0 0 0 0 x5 x6 x7 x8 z1 x9 x10 0 0 x11 x12 0 0 z2

M(x) =

.

0 0 x13 x14 0 0 x15 x16 z3 x17 0 x18 0 x19 0 x20 0 z4 0 x21 0 x22 0 x23 0 x24 z5

 

 

Observe that rank√ M = 4, since otherwise M extended by F and a vertex of P, which is not contained in F, has square root rank bigger than ﬁve, contradicting the psd-minimality of the 4-polytope P. On the other hand, rankM = 4 because the rows of M are indexed by the vertices of the 3-polytope F.

Let M be the matrix obtained from M by dropping the column indexed by G. Since the octahedron F is psd-minimal, without loss of generality we may assume that the ﬁrst four rows are linearly dependent in both M and each of its Hadamard square roots of rank four. For a justiﬁcation of this assumption, we refer the reader to Remark 7.2. 1 Thus both M and each of its square roots of rank four lie in the variety of the ideal generated by the 4-minors of the upper left 4 × 8 submatrix of M(x), and the 5-minors of M(x). Using a computer algebra system one can verify that this ideal contains trinomials, such as

x11x16x17z5 − x1x11x16x18z5 − x3x9x16x19z5.

As in Lemma 2.2, since both M and its square root must satisfy this trinomial, no polytope combinatorially equivalent to P can be psd-minimal.

1This fact can be proved independently but follows easily from the algebraic machinery developed in the second half of the paper.

- 3.2. Possible facet intersections of a psd-minimal 4-polytope. Based on the three lemmas above we can now provide a short list of allowed intersections among the facets of a psd-minimal 4-polytope. This is the key tool in ﬁnding the combinatorial classes of psd-minimal 4-polytopes.


- Proposition 3.5. Let P be a psd-minimal 4-polytope and F and G be facets of P intersecting at a vertex or an edge. Then, either F is a simplex or one of the following conditions (illustrated in Figure 1) hold:


- (1) F is a bisimplex and F ∩ G is a vertex;
- (2) F is a triangular prism and F ∩ G is one of the edges linking the two triangular faces;
- (3) F is a square pyramid and F ∩ G is the apex or an edge of the base.


Proof. This follows from the previous lemmas as all the other possible edge intersections are not wedges and hence are not intersections by Lemma 3.2. Similarly, all the other possible vertex intersections lie in a square face and hence are not intersections by Lemma 3.3, except for the vertices of the octahedron, which are not intersections directly from Lemma 3.4.

Figure 1. All possible vertex or edge intersections among facets of a psd-minimal 4-polytope (excluding the simplex).

We state one more result about the combinatorics of a psd-minimal 4-polytope.

Lemma 3.6. An edge of a psd-minimal 4-polytope is contained in at most four facets.

Proof. This follows dually from the fact that faces of dimension two of a psdminimal 4-polytope are themselves psd-minimal and hence have at most four vertices.

4. Classification of combinatorial types In this section, we prove our main theorem.

- Theorem 4.1. There are exactly 31 combinatorial classes of psd-minimal 4-polytopes. In Table 1 we list all these classes with the following information in each column:


| |Fig<br><br>|Construction<br><br>|Vertices of a psd-minimal embedding<br><br>|Facet Types|Dual|f-vector<br><br>|Condition|
|---|---|---|---|---|---|---|---|
|1<br><br>| |∆4<br><br>|{−e1234, e1, e2, e3, e4}|5S<br><br>|Self<br><br>|(5, 10, 10, 5)|Cor. 5.12|
|2| |(∆1 × ∆1) ∗ ∆1<br><br>|{±e1, ±e2, e3, e4}|4S,2Py<br><br>|Self|(6, 13, 13, 6)<br><br>|Cor. 5.12|
|3|17B| |{0, 2e1, 2e2, 2e3, e12 − e3, e4, e34}|3S,2Py,2B|Self<br><br>|(7, 17, 17, 7)|Cor. 5.12|
|4<br><br>|6C<br><br>|∆3 × ∆1<br><br>|{−e123, e1, e2, e3} + {±e4}<br><br>|2S,4Pr|5|(8, 16, 14, 6)|Cor. 5.12|
|5| |∆3 ⊕ ∆1|{−e123, e1, e2, e3, ±e4}<br><br>|8S<br><br>|4|(6, 14, 16, 8)|Cor. 5.12|
|6|6A<br><br>|∆2 × ∆2<br><br>|{−e12, e1, e2} + {−e34, e3, e4}|6Pr|7|(9, 18, 15, 6)<br><br>|Cor. 5.12|
|7| |∆2 ⊕ ∆2<br><br>|{−e12, e1, e2, −e34, e3, e4}<br><br>|9S|6<br><br>|(6, 15, 18, 9)<br><br>|Cor. 5.12|
|8<br><br>|7A<br><br>|(∆2 × ∆1) ∗ ∆0|{e4} ∪ ({−e12, e1, e2} + {±e3})<br><br>|2S,1Pr,3Py<br><br>|9|(7, 15, 14, 6)|Cor. 5.12|
|9| |(∆2 ⊕ ∆1) ∗ ∆0<br><br>|{−e12, e1, e2, ±e3, e4}<br><br>|6S,1B<br><br>|8|(6, 14, 15, 7)<br><br>|Cor. 5.12|
|10|6B| |{0, e1, e2, e3, e13, e23, e4, e14}<br><br>|1S,2Pr,4Py|11|(8, 18, 17, 7)|Cor. 5.12|
|11| | |{e1, e2, e3, e4, −2e1 − e24, −e13 − 2e2, −2e12}|4S,4Py<br><br>|10|(7, 17, 18, 8)<br><br>|Cor. 5.12|
|12|6F| |{0, e1, e2/2, e3, e4, e14, e12/2, e13, e2 + 4e34}|3Pr,3Py,2B|13<br><br>|(9, 22, 21, 8)|Prop. 6.2|
|13<br><br>|17C| |{e1, e2, 9/4e3, e4, e124/2, e13, e2 + e3/4, e34}|2S,6Py,1B<br><br>|12|(8, 21, 22, 9)<br><br>|Prop. 6.2|
|14|6D<br><br>|(∆2 ⊕ ∆1) × ∆1<br><br>|{0, e1, e2, e3, e4, e12, e23, e24, 2e13 + e4, 2e13 + e24}|6Pr,2B|15<br><br>|(10, 23, 21, 8)<br><br>|Prop. 6.4|
|15| |(∆2 × ∆1) ⊕ ∆1<br><br>|{e1, 2e2, e3, 2e4, e2 + 2e3, e2 + 4e4, 2e1 + e2, e134}<br><br>|4S,6Py|14|(8, 21, 23, 10)<br><br>|Prop. 6.4|
|16|3D<br><br>|(∆1 × ∆1 × ∆1) ∗ ∆0<br><br>|({±e1} + {±e2} + {±e3}) ∪ {e4}<br><br>|1C,6Py|17<br><br>|(9, 20, 18, 7)|Prop. 7.3|
|17| |(∆1 ⊕ ∆1 ⊕ ∆1) ∗ ∆0|{±e1, ±e2, ±e3, e4}<br><br>|1O,8S|16<br><br>|(7, 18, 20, 9)|Prop. 7.3|
|18|6H<br><br>| |{0, e1, e2/2e4, e234, e23, e24/2, e134, e13}<br><br>|2Pr,4Py,2B<br><br>|19|(9, 22, 21, 8)<br><br>|Prop. 7.3|
|19|13B| |{0, e1, e3, e4, e14, e23, e24, e234}<br><br>|1O,4S,4Py|18|(8, 21, 22, 9)<br><br>|Prop. 7.3|
|20|3C|((∆1 × ∆1) ∗ ∆0) × ∆1|{±e1, ±e2, e3} + {±e4}|1C,4Pr,2Py<br><br>|21|(10, 21, 18, 7)<br><br>|Prop. 7.3|
|21| |((∆1 × ∆1) ∗ ∆0) ⊕ ∆1|{±e1, ±e2, e3, e3/2 ± e4}<br><br>|8S,2Py<br><br>|20<br><br>|(7, 18, 21, 10)|Prop. 7.3|
|22| | |{0, 2e1, 2e3, 2e4, e12, e123, e1234, 2e24, 2e34}<br><br>|6Py,3B<br><br>|23|(9, 24, 24, 9)<br><br>|Prop. 7.3|
|23|7C<br><br>| |{0, e1, e3, e4, e12, e123, e23, e24, e234}|2O,3S,1Pr,3Py<br><br>|22|(9, 24, 24, 9)<br><br>|Prop. 7.3|
|24| | |{0, 2e1, 2e2, 2e3, 2e4, e123, e124, e134, e1234, e234}|10B<br><br>|25|(10, 30, 30, 10)<br><br>|Prop. 7.3|
|25<br><br>|13A| |{e1, e2, e3, e4, e12, e13, e14, e23, e24, e34}<br><br>|5O,5S<br><br>|24|(10, 30, 30, 10)|Prop. 7.3|
|26| |(∆1 × ∆1 × ∆1) ⊕ ∆1<br><br>|({±e1} + {±e2} + {±e3}) ∪ {±e4}<br><br>|12Py<br><br>|27|(10, 28, 30, 12)|Prop. 7.3|
|27|6E|(∆1 ⊕ ∆1 ⊕ ∆1) × ∆1<br><br>|{±e1, ±e2, ±e3} + {±e4}<br><br>|2O,8Pr<br><br>|26|(12, 30, 28, 10)<br><br>|Prop. 7.3|
|28<br><br>|3B|∆1 × ∆1 × ∆2<br><br>|{±e1} + {±e2} + {−e34, e3, e4}<br><br>|3C,4Pr<br><br>|29|(12, 24, 19, 7)<br><br>|Prop. 7.4|
|29| |∆1 ⊕ ∆1 ⊕ ∆2|{±e1, ±e2, −e34, e3, e4}<br><br>|12S<br><br>|28|(7, 19, 24, 12)<br><br>|Prop. 7.4|
|30<br><br>|3A|∆1 × ∆1 × ∆1 × ∆1<br><br>|{±e1} + {±e2} + {±e3} + {±e4}<br><br>|8C|31<br><br>|(16, 32, 24, 8)|Prop. 7.6|
|31| |∆1 ⊕ ∆1 ⊕ ∆1 ⊕ ∆1<br><br>|{±e1, ±e2, ±e3 ± e4}|16S<br><br>|30<br><br>|(8, 24, 32, 16)|Prop. 7.6|


Table 1. Combinatorial classes of psd-minimal 4-polytopes

PSD-MINIMAL4-POLYTOPES11

- (1) The number which we use to refer to the class.
- (2) The reference to its Schlegel diagram, when present in the paper.
- (3) A construction (if one is known) of a polytope in the class using standard

operations on simplices. In the table, ∆d denotes a simplex with d + 1 vertices, and ×, ⊕ and ∗ denote the product, free sum and join operations.

- (4) The vertices of a psd-minimal polytope in the combinatorial class, where psd-minimality of the polytope can be veriﬁed by constructing a slack ma-

trix and checking its square root rank. For S ⊆ {1,2,3,4}, eS denotes the zero-one vector with a one in position i if and only if i ∈ S.

- (5) Information about the combinatorial types of facets, i.e. how many facets of a polytope in this class are cubes (C), triangular prisms (Pr), octahedra (O), bisimplices (B), square pyramids (Py) and simplices (S).
- (6) The number of the dual of the combinatorial class, or Self if it is self dual. Recall that psd-minimality is closed under polarity, and we list dual pairs of combinatorial classes consecutively.
- (7) The f-vector of the polytopes in the the combinatorial class.
- (8) The reference to the result characterizing psd-minimality in the combinatorial class.


Since we provide a psd-minimal polytope in each of the 31 classes of Table 1, to prove Theorem 4.1, it suﬃces to argue that there are no further combinatorial classes of psd-minimal 4-polytopes. To enumerate the possible combinatorial classes of psd-minimal 4-polytopes we systematically study the combinatorics of their facets. For example, we start by listing all combinatorial classes of psd-minimal 4-polytopes with a cubical facet. We assume that a psd-minimal 4-polytope P has a facet combinatorially equivalent to a cube, and then using combinatorial arguments we leverage the facet intersection results of Proposition 3.5 to dramatically restrict the possible combinatorial classes of P. After all classes of psd-minimal 4-polytopes with a cubical facet are obtained, we add them and their dual classes to our list of possibilities, and move on to study polytopes with a diﬀerent combinatorial type of facet, until we cover all cases. Naturally, when studying a new type of facet, we can assume that neither the polytope P nor its dual has facets of the combinatorial types previously studied. Otherwise, we would be double counting. The combinatorial types of facets to consider are those of the psd-minimal 3-polytopes, i.e., cubes, triangular prisms, octahedra, bisimplices, square pyramids and simplices in this order. We treat each case in a separate subsection.

- 4.1. Cube. Let P be a psd-minimal 4-polytope with a cubical facet F. We provide a detailed discussion of this case, skipping similar arguments in later subsections. By Proposition 3.5, any other facet of P either has an empty intersection with F or intersects F in one of its facets. This fact is crucial for the analysis below. Figure 2


shows the graph of F, along with some marked facets, F 1, F 2, F 3 and F 4 of F.

Let F1 and F2 be the facets of P such that F ∩ F1 = F 1 and F ∩ F2 = F 2. The facets F1 and F2 are cubes, triangular prisms or square pyramids since they must have the square facets F 1 and F 2, respectively. By Proposition 3.5, the edge

- F 1 ∩ F 2 is not the intersection of F and some other facet of P. Hence F1 ∩ F2 is a two dimensional face of P, i.e. F1 ∩ F2 is a facet of both F1 and F2.


If there is a cube attached to F, we may assume that it is F2. Then F1 must be either a cube or a triangular prism attached to F2 by a square face. If there are no cubes attached to F, but there are triangular prisms, then again we may

|F 1<br><br>|F 2|
|---|
<br><br>F 3 F 4|
|---|


Figure 2

assume that F2 is a triangular prism and then all square faces of F2 other than F 2 must be attached to triangular prisms. Finally, if there are no cubes or triangular prisms attached to F, then all facets attached to F are square pyramids. These possibilities are represented by the diagrams in the upper row of Figure 3 where we have drawn the Schlegel diagrams of F1 and F2 inside their faces F 1 and F 2.

(A) (B) (C) (D)

Figure 3

The analysis of the four cases depicted in the upper row of Figure 3 leads us to unique ways of completing them to potentially psd-minimal polytopes. The corresponding Schlegel diagrams are shown in the lower row of Figure 3. We elaborate on Figure 3A, when both F1 and F2 are cubes.

Observe that the cube is the only psd-minimal 3-polytope with a vertex contained in three square facets. This observation applied to the vertices of F1∩F2∩F, shows that F3 and F4 are cubes, where F3 and F4 are the facets of P such that F 3 = F3∩F and F 4 = F4 ∩F (see Figure 2). Repeating this argument, we deduce that all facets of P having a nonempty intersection with F are cubes.

Consider the vertex v of P such that v ∈ (F1 ∩F2 ∩F3) F. There exists a facet

- G of P diﬀerent from F1, F2 and F3 such that v ∈ G, because every vertex lies in at least four facets of P. Since F1, F2 and F3 are cubes and they intersect G, by Proposition 3.5, each of the intersections G ∩ Fi, i = 1,...,3 must be a square face of G containing v. Therefore, G must be a cube as it is the only psd-minimal


- 3-polytope with three square facets meeting at a vertex. This implies that the four


vertices of Fi,i = 1,...,3 that are not in F are in G. Applying the same argument to diﬀerent triples of facets of P intersecting F we conclude that they all meet G in

a square face, giving rise to the Schlegel diagram in 3A. The other cases of Figure 3 are obtained by a similar and simpler application of Proposition 3.5.

We conclude that there are four distinct combinatorial classes of psd-minimal polytopes with cubical facets, namely classes 16, 20, 28 and 30. Since none of them are self dual, we obtain eight classes in Table 1.

- 4.2. Triangular Prism. Suppose P has a facet F that is a triangular prism. We may assume that P has no cubical facets since otherwise we would be in the previous


case. Consider the facets F1, F2 and F3 of P such that F 1 = F1 ∩ F, F 2 = F2 ∩ F and F 3 = F3 ∩ F are the square faces of F(see Figure 4).

F 2 F 3

F 1

Figure 4

The facet F1 is a triangular prism or a square pyramid, since its facet F 1 is a square. Thus, we have three possibilities for F1, shown in Figure 5: two ways in which F1 can be a triangular prism and one way in which F1 can be a square pyramid.

Figure 5

We start by considering all the possibilities when F1 is a triangular prism. To do this we have to list all possible combinatorial types and positions of F1, F2 and F3, and draw the corresponding diagrams as in the case of the cube. By Lemma 3.6 we know that every edge of F is in at most four facets of P, while by Proposition 3.5 we know that certain edges of prisms and pyramids can only appear in three facets of P. Therefore, besides combinatorial types, we also consider all the possibilities for edges of F to be contained in exactly three facets of P (in which case we draw the edge thick) or in exactly four facets of P (in which case we draw the edge dashed). The diagrams obtained are shown in Figure 6.

The rules to obtain these diagrams are simply that if Fi and Fj share a thick edge, their facets that contain this edge, and are not facets of F, must be combinatorially the same, as they are identiﬁed. If these face identiﬁcations force distinct vertices

from the same facet to be identiﬁed, we discard the underlying diagram, as it does not correspond to a polytope. The diagrams in the upper rows in Figure 6 are all the cases that result from this process. We explain in detail how we obtain the diagrams in Figure 6 that come from the ﬁrst diagram in Figure 5.

Since F2 and F3 must share a triangular face with F1, there are three cases to consider. Both F2 and F3 can be triangular prisms sharing a triangular face which gives immediately the case in Figure 6A. The second possibility is that both F2

- and F3 are square pyramids. In this case, either they intersect in a triangular face or an edge. If they intersected in a triangular face, then two vertices of F1 would be identiﬁed with each other which cannot happen. Therefore, we can obtain only the case in Figure 6B. Lastly, suppose F2 is a triangular prism and F3 is a square pyramid. Then Proposition 3.5 implies that each pair of F1,F2,F3 intersect in a triangular face which would force the identiﬁcation of two vertices of F1 and F2 not belonging to their already common triangular face which is a contradiction. The remaining seven cases in Figure 6 arise similarly from the second case in Figure 5.


As in the case of cubical facets, it is easy to show that for each diagram there is a unique way to complete it to a potentially psd-minimal combinatorial polytope. Below each case in the upper rows of Figure 6 we present the corresponding Schlegel diagram. Next we assume that none of the facets F1, F2 and F3 are triangular prisms. All possible diagrams and the corresponding Schlegel diagrams are shown in Figure 7.

Further analysis allows us to rule out some of these diagrams. In Figures 6G and 6I two octahedra intersect in a vertex and in an edge respectively, contradicting Proposition 3.5. We can exclude the case in Figure 7B as well because there two bisimplices intersect in an edge. What remains are 9 distinct combinatorial classes, namely classes 4, 6, 8, 10, 12, 14, 18, 23 and 27 in Table 1. Along with their duals we get 18 new classes.

- 4.3. Octahedron. We may now assume that no facet of P or its dual is a cube


or a triangular prism. Let F be an octahedral facet of P and let F 1 be one of its facets (see Figure 8). Take F1 to be the facet of P such that F 1 = F1 ∩ F.

Every vertex of F 1 is contained in three or four facets of F1, because F1 is a psd-minimal 3-polytope. We use this fact for the classiﬁcation and introduce a new type of diagram: the pair consisting of F 1 and its vertex v is marked by a blue angle when v is contained in three facets of F1 and by a red cut angle if v is contained in four facets of F1 (see Figure 9 for all possible markings of F 1). Moreover, given the labeling of F 1, we can now uniquely determine the combinatorial type of F1, since the triangular faces of the four remaining psd-minimal 3-polytopes available to use as facets all have diﬀerent vertex degree distributions.

To enumerate all possible labelings of the facets of F we use the three labeling rules in Figure 10. Rule 10A comes from the fact that by Proposition 3.5 no facet of P intersects F in a vertex or an edge. To elaborate, let (v,F 1) be the pair marked with a red cut angle and F 2,F 3,F 4 be the facets of F that touch v numbered clockwise from F 1 (see Figure 11A). As usual, Fi denotes the facet of P that intersects F in F i. Let G be the facet of F1 that intersects F in only v and

- G be the facet of P that intersects F1 in G . Since the intersection of G and F is nonempty, G intersects F in one of its facets. Hence G intersects F in F 2, F 3 or F 4, i.e. G equals F2, F3 or F4. Note that G cannot be either F2 or F4 as they already contain facets of F1 distinct from G . Thus, G equals F3 and v has degree four in


(A) (B) (C)

(D) (E) (F)

(G) (H) (I)

### Figure 6

(A) (B) (C)

- Figure 7

F 1

- Figure 8

(A) Simplex (B) Square pyramid (C) Bisimplex (D) Octahedron

- Figure 9


- F3, showing that (v,F 3) is marked by a red cut angle. It is now easy to see that v must have degree three in F2 as its intersections with F3 and F1 share an edge of


- G . Similarly for F4 and we get that (v,F 2) and (v,F 4) must be blue angles. Let us prove that rule 10B is valid. Indeed, let v,F1,F2,F3,F4 be as in Fig-


ure 11B with F1 being the bisimplicial facet. By Rule 10A we know that (v,F 3)

(A) (B) (C)

Figure 10

F 1

v

F 4

F 2 F 3

(A)

F 1

v

F 4

F 2 F 3

(B)

Figure 11

must be a blue angle and (v,F 2) and (v,F 4) are either both blue angles or both red cut angles. If all are blue, then F1,...,F4 all share a common edge. In particular, the bisimplicial facet F1 and facet F3 intersect in an edge, contradicting Proposition 3.5.

For Rule 10C we use the fact that only square pyramids among facets of P can have a square face. Thus, if F1 is a square pyramid, the triangular facet of F not containing the apex of F1 but containing an edge of F 1 must also be a facet of a square pyramid.

We now use these rules to produce all valid diagrams. If we start by assuming F1 is an octahedron we get a unique valid diagram, shown in Figure 12A. If we assume F1 to be a square pyramid we only obtain the diagram in Figure 12B. The assumption that F1 is a bisimplex does not lead to any valid diagram. As before, there is a unique way to produce a polytope that complies with each diagram and respects the facet intersection properties of psd-minimal 4-polytopes. The Schlegel diagrams of polytopes in these classes are presented in Figure 13. It turns out that the class shown in Figure 13A is dual to class 18, so it is already accounted for.

(A) (B)

### Figure 12

(A) (B)

- Figure 13

F 1 F 2

F 3 F 4

v

- Figure 14


The other option left to explore is if F1 is not an octahedron, square pyramid or a bisimplex. Without loss of generality we may then assume that all facets of

- P that intersect F in a facet are simplices, otherwise we would consider a non-


simplex facet as the new F1 and be in one of the previous cases. However, this case immediately gives a pyramid over an octahedron, a case that is already accounted for, as it is the dual of the pyramid over the cube, namely class 16. Therefore we only get one new class of psd-minimal polytopes which is class 25, and its dual.

- 4.4. Bisimplex. Suppose now that P has a bisimplicial facet F. We can assume that neither P nor its dual has a cube, triangular prism or octahedron as a facet. In particular, every vertex of P is contained in at most ﬁve facets.


Consider the graph of F with a marked vertex of degree four (with respect to the graph of F) and four marked facets of F as shown in Figure 14. Let F1, F2, F3

- and F4 be the facets of P such that F 1 = F1 ∩ F, F 2 = F2 ∩ F, F 3 = F3 ∩ F and F 4 = F4 ∩ F. Clearly, the vertex v is contained in at least ﬁve facets of P, namely in F1, F2, F3, F4 and F. Hence, there is no other facet of P containing v, otherwise v is contained in at least six facets of P. Additionally note that every edge of F contains a vertex of degree four. By these observations, we can conclude that no facet of P intersects F in an edge or in a vertex of degree four.


This strengthened version of Proposition 3.5 allows us to apply all the labeling rules in Figure 10 to the bisimplicial case as well. Note that the graph of F contains also vertices of degree three.

For these vertices we introduce the two additional rules in Figure 15 which are saying that we cannot mix blue angles and red cut angles around a degree three vertex of F. Suppose we have a red cut angle (v,F 1) and two blue angles. Then

(A) (B)

Figure 15

the two edges of F1 that contain v and are not contained in F have to be the same which is a contradiction. If there were two red cut angles (v,F 1) and (v,F 2) they share an edge that contains v and is not contained in F and the remaining such edge of each would both get identiﬁed with the only such edge of the blue angle face, again a contradiction.

We obtain four valid diagrams up to symmetry, by considering all the diﬀerent possibilities for the bottom triangle. The ﬁrst is gotten by making all other facets simplices, which gives us the pyramid over a bisimplex. This is however dual to the pyramid over a prism, which is already accounted for in class 8. The remaining three possible diagrams for the graph of F are shown in Figure 16.

(A) (B) (C)

Figure 16

The labeling in Figure 16A does not correspond to any 4-polytope. To see this just note that the straightforward identiﬁcation of nodes implied by the facet intersection rules leads to Figure 17A, where nodes of the same shape represent the same vertex. This identiﬁcation implies the existence of two facets of P whose intersection is not a face of P, for instance the outer facet and the middle left facet in the diagram intersect at two vertices not sharing an edge, which would be impossible if P was actually a polytope.

The diagram in Figure 16B leads to a unique psd-minimal 4-polytope, whose Schlegel diagram is in Figure 17B. It is also straightforward to obtain the Schlegel diagram in Figure 17C of the polytope corresponding to the diagram in Figure 16C. However, we can see in that Schlegel digram that the vertices of the central triangle are contained in six facets of P, which means that this must be dual to a previously discovered polytope, and in fact, it is dual to class 12. So again we only get one new class of polytopes, class 3, which turns out to be self dual.

- 4.5. Square Pyramid. Now we assume that the facets of P are simplices and square pyramids. By duality we can additionally assume that every vertex of P is


(A)

(B) (C)

Figure 17

contained in at most ﬁve facets of P, and that every vertex of P is adjacent to at most ﬁve other vertices of P.

Take a facet F of P, where F is a square pyramid. Let one of the triangular faces of F belong to another facet of P, which is a square pyramid. Figure 18 is the only possibility under this assumption. Indeed, note that if two square pyramids would have the same apex then this apex would be adjacent to six other vertices. Furthermore, by Proposition 3.5 no facet of P can intersect F in an edge containing the apex of F. Now it is easy to see that if u is not identiﬁed with the triangle-nodes or circle-nodes then the vertex v4 is adjacent to at least six other vertices of P. If u is a circle-node then v3 is contained in at least six facets and if u is triangle-node then v1 is contained in at least six facets of P. All these cases have been accounted for already.

v4 v3

| |
|---|


u

v1 v2

Figure 18

Thus we can now assume that triangular facets of F are not contained in any other square pyramid facet. In this case a similar identiﬁcation of vertices shows that P is a pyramid over F, giving us the self dual polytope class 2.

- 4.6. Simplex. Finally, we can assume that all facets of P are simplices, and by duality, that every vertex of P is contained in exactly four facets. Then P is a simplex, and we obtain the last class of psd-minimal polytopes, class 1.


5. Slack ideals and the binomial condition (Classes 1–11)

- 5.1. Slack ideals of polytopes. We now deﬁne the slack ideal of a d-polytope which we use to understand psd-minimality in the rest of this paper.


Deﬁnition 5.1. The slack ideal IP of a d-polytope P is the ideal of all (d+2)-minors of SP(x) saturated with respect to all the variables in SP(x). In mathematical notation, if the variables in SP(x) are x1,...,xt, then

IP = (d + 2)-minors of SP(x) : (Πti=1xi)∞.

Recall that the saturation of an ideal I with all its variables is the ideal generated by all polynomials f for which a monomial multiple of f lies in I. Recall also that in this paper, a binomial is a polynomial of the form ±xa ± xb. We say that an ideal is binomial if it is generated by binomials. Since the variety of IP contains positive points, namely the vector of positive elements in the slack matrix SP, any binomial in IP is of the form xa − xb.

## Example 5.2. For a square,

  

  

0 x1 x2 0 0 0 x3 x4

SP(x) =

x5 0 0 x6 x7 x8 0 0

and IP = x2x4x5x8 − x1x3x6x7 is a binomial ideal.

We now compute the slack ideal of a polytope in class 3. One can compute the slack matrix of the speciﬁc polytope in class 3 given in the table and check that the following is the symbolic slack matrix of a polytope in this class:





0 x1 0 0 0 x2 0 x3 0 0 0 0 x4 0 x5 0 x6 0 0 0 x7 0 x8 x9 0 0 0 x10 0 0 0 0 x11 0 x12 0 0 0 x13 x14 x15 0 0 0 x16 x17 0 0 0

SP(x) =

.

 

 

The ideal of all 6-minors of SP(x) is generated by 49 polynomials all of which are binomials except the following four:

- (3)


x4x5x10x11x13x16 − x4x5x9x12x14x17 + x3x7x9x11x15x17 − x3x6x10x11x15x17, x2x7x8x11x13x16 − x2x6x8x12x14x17 − x1x7x9x11x15x17 + x1x6x10x11x15x17, x2x3x7x8x13x16 − x1x4x5x10x13x16 − x1x3x7x9x15x17 + x1x3x6x10x15x17, x2x3x6x8x12x14 − x1x4x5x9x12x14 + x1x3x7x9x11x15 − x1x3x6x10x11x15.

Saturating the ideal of minors with the product of all variables we obtain the binomial ideal: IP = x7x9 − x6x10,x10x11x13x16 − x9x12x14x17,x7x11x13x16 − x6x12x14x17, x2x8x13x16 − x1x9x15x17,x4x5x13x16 − x3x6x15x17,x2x8x12x14 − x1x10x11x15,

x4x5x12x14 − x3x7x11x15,x2x3x7x8 − x1x4x5x10,x2x3x6x8 − x1x4x5x9 .

Notice that saturation changed the ideal of minors into a binomial ideal. For example, the ﬁrst generator in (3), which is the 6-minor of SP(x) obtained by dropping the ﬁrst row and second column, can be written as

x4x5(x10x11x13x16 − x9x12x14x17) + x3x11x15x17(x7x9 − x6x10). Saturation puts x7x9 − x6x10 and x10x11x13x16 − x9x12x14x17 in the slack ideal and hence prevents this four-term polynomial from being a minimal generator of IP. Similarly, all the other four-term polynomials are also unnecessary to generate IP. This example highlights the fact that the slack ideal may be diﬀerent from the ideal of (d + 2)-minors of SP(x) and, in particular, that IP can be binomial even if the ideal generated by the (d + 2)-minors is not.

Matrices with a ﬁxed zero pattern and all non-zero entries being variables are known in the literature as sparse generic matrices. Furthermore, sparse determinantal ideals are the ideals of ﬁxed size minors of a sparse generic matrix, and have been studied in diﬀerent situations [GM82], [Boo12]. The slack ideal of a polytope is not exactly a sparse determinantal ideal, but is the saturation of one, i.e., the saturation of the ideal of all (d + 2)-minors of the sparse generic matrix SP(x). In this paper, we deﬁne and use slack ideals for psd-minimality computations, but they could be of independent interest to both algebraists and combinatorialists.

Let V(IP) denote the real zeros of the slack ideal IP. It is convenient to identify s ∈ V(IP) with the matrix SP(s). Then, by construction, rank(SP(s)) ≤ d + 1.

- If Q is a polytope that is combinatorially equivalent to P, then a slack matrix of


- Q is a positive element of V(IP). Conversely, by [GGK+13, Theorem 24], every positive element of V(IP) is, up to row scaling, the slack matrix of a polytope in the combinatorial class of P. In fact, Corollary 1.5, gives a more precise description of V(IP).


- Theorem 5.3. Given a polytope P there is a one to one correspondence between


the positive elements of V(IP), modulo row and column scalings, and the classes of projectively equivalent polytopes of the same combinatorial type as P.

## 5.2. Binomial slack ideals.

Deﬁnition 5.4. We say that a d-polytope P is combinatorially psd-minimal if all d-polytopes that are combinatorially equivalent to P are psd-minimal.

A d-simplex is combinatorially psd-minimal. By Proposition 2.4, a square is also combinatorially psd-minimal.

- Lemma 5.5. If the slack ideal IP of a polytope P is binomial then P is combinatorially psd-minimal.


Proof. If IP is a binomial ideal then for every positive s ∈ V(IP) and generator xa − xb of IP, we have that sa = sb, which implies (

√s is the entry-wise positive square root of s. Thus

√s)b where

√s)a = (

+

+

+

√s annihilates every generator of IP, so rank(

+

SP(s)) ≤ d + 1.

+

It was shown in Theorem 4.3 in [GRT13] that every d-polytope with d+2 vertices is combinatorially psd-minimal. In view of Lemma 5.5, this fact is a corollary of the following result.

- Theorem 5.6. If a d-polytope P has d + 2 vertices or facets then IP is binomial.


By polarity it suﬃces to prove the result for the case when P has d + 2 vertices. We recall the structure of such polytopes from [Gr¨u03, Section 6.1]. Any d-polytope with d + 2 vertices is combinatorially equivalent to a repeated pyramid over a free sum of two simplices, pyrr(∆k ⊕ ∆l), with k,l ≥ 1, r ≥ 0 and r + k + l = d. Since taking pyramids preserves the slack ideal, it is enough to study the slack ideals of free sums of simplices or, dually, products of simplices. This class of polytopes has a very simple slack matrix structure.

Lemma 5.7. If P = ∆k ⊕ ∆l, then SP(x) has the zero pattern of the vertex-edge incidence matrix of the complete bipartite graph Kk+1,l+1.

- Example 5.8. A polytope in class 5 in Table 1 is of the type ∆1 ⊕ ∆3 hence its slack matrix is the vertex-edge incidence matrix of K2,4. Therefore,






x1 x2 x3 x4 0 0 0 0 0 0 0 0 x5 x6 x7 x8

x9 0 0 0 x10 0 0 0 0 x11 0 0 0 x12 0 0 0 0 x13 0 0 0 x14 0 0 0 0 x15 0 0 0 x16

SP(x) =

.

 

 

Let K be the complete bipartite graph associated to P as above and consider a simple cycle C in K with c edges and hence c distinct vertices. Let MC(x) be the c × c symbolic matrix whose support is the vertex-edge incidence matrix of C





x1 0 0 ... 0 x2 x3 x4 0 ... 0 0 0 x5 x6 ... 0 0 . . . 0 0 0 ... x2c−2 0 0 0 0 ... x2c−1 x2c

.

 

 

Note that det(MC(x)) is a binomial.

- Proposition 5.9. If P = ∆k ⊕ ∆l then IP is generated by the binomials det(MC) as C varies over the simple cycles of Kk+1,l+1.


Proof. Let J denote the ideal generated by the binomials det(MC) as C varies over the simple cycles in Kk+1,l+1. The ideal J is the toric ideal of the Lawrence lifting of the vector conﬁguration consisting of the column vectors of the vertexedge incidence matrix of Kk+1,l+1 [Stu96, Corollary 14.12]. Further, toric ideals are saturated [Stu96, Chapter 12] and hence, J : ( xi)∞ = J.

Since d = dim(P) = k +l, by Lemma 5.7, a (d+2)-minor of SP(x) is a maximal minor of the vertex-edge incidence matrix of Kk+1,l+1. Let M be a (d+2)×(d+2) submatrix of SP(x). Suppose that a row of M has zero or one non-zero entries. In the former case, det(M) = 0 and in the latter case, det(M) is a variable times a (d + 1)-minor of SP(x). Repeating this argument for rows and columns, we see that det(M) is a product of variables times the minor of a submatrix of SP(x) with at least two non-zero entries per row and column, and hence, exactly two nonzero entries per row and column. This submatrix is thus the vertex-edge incidence matrix of a disjoint union of simple cycles in Kk+1,l+1, hence block diagonal (after

permuting rows and columns) with each block indexed by one such cycle. Therefore, det(M) lies in J and IP ⊆ J : ( xi)∞ = J. Note that det(M) is not a product of variables, as this would imply that the corresponding minor in SP is not zero and hence rank(SP) = d + 2 which is a contradiction.

For the reverse inclusion notice that the incidence matrix of a cycle C can be extended to a (d + 2) × (d + 2) submatrix of the incidence matrix of Kk+1,l+1 by picking a vertex on each side of Kk+1,l+1 contained in C and connecting each of these vertices to all vertices on the other side not already in C. As before, the resulting (d + 2)-minor is a product of variables times the minor corresponding to C. This shows that J ⊆ IP, and we conclude that J = IP.

This ﬁnishes the proof of Theorem 5.6.

- Example 5.10. As we saw in Example 5.8, the symbolic slack matrix of a polytope P in combinatorial class 5 has support equal to the vertex-edge incidence matrix


of K2,4. The graph K2,4 has six simple cycles all of length four and the minors of the submatrices they index are

x3x8x14x15 − x4x7x13x16, x2x8x12x15 − x4x6x11x16, x1x8x10x15 − x4x5x9x16,

x2x7x12x13 − x3x6x11x14, x1x7x10x13 − x3x5x9x14, x1x6x10x11 − x2x5x9x12. By Proposition 5.9, the slack ideal IP is generated by these binomials. Theorem 5.11. The slack ideals of classes 2,...,11 in Table 1 are binomial.

Proof. The 4-polytopes in classes 2,4,5,6,7,8,9 have 6 = 4+2 vertices or facets and hence the result follows in these cases from Theorem 5.6. We saw in Example 5.2 that the slack ideal of a polytope in class 3 is binomial. Since classes 10 and 11 are dual, we only need to show that the slack ideal of a polytope in class 10 is binomial.

The symbolic slack matrix of a polytope in class 10 is the following:





0 0 x1 x2 0 0 x3 0 x4 0 x5 0 0 0 0 0 0 x6 0 x7 x8

x9 0 x10 0 0 0 0 x11 0 0 0 0 x12 0

SP(x) =

.

0 0 x13 0 x14 0 x15 0 x16 0 0 x17 0 0 0 0 0 0 x18 x19 x20

 

 

Using Macaulay 2 one can compute that IP is binomial. More precisely, IP = x8x19 − x7x20, x15x18 − x14x20, x3x13 − x1x15, x3x6 − x2x8, x10x11x15x19−x9x12x13x20, x3x10x11x19−x1x9x12x20, x5x8x16x18−x4x6x17x20, x5x7x16x18 − x4x6x17x19, x3x5x16x18 − x2x4x17x20, x9x12x13x18 − x10x11x14x19, x2x7x13x18 − x1x6x14x19, x5x8x14x16 − x4x6x15x17, x3x5x14x16 − x2x4x15x17, x1x5x14x16 − x2x4x13x17, x8x9x12x13 − x7x10x11x15, x3x7x10x11 − x1x8x9x12, x2x7x10x11 − x1x6x9x12, x1x5x9x12x16x18 − x2x4x10x11x17x19, x5x7x10x11x14x16 − x4x6x9x12x13x17 .

We will see at the end of the paper that no other combinatorial class in Table 1 has a binomial ideal. Since the table lists all possible combinatorial types of psdminimal 4-polytopes, using Lemma 5.5 we can conclude that we have identiﬁed all

- 4-polytopes with a binomial polytope ideal.


Corollary 5.12. Any 4-polytope in classes 1-11 is combinatorially psd-minimal.

Remark 5.13. In [McM76], McMullen exhibited 11 combinatorial classes of 4polytopes that are projectively unique and this list is conjectured to be complete. These are precisely the classes 1,...,11 in Table 1. This connection yields an alternate short proof of Corollary 5.12. Since psd rank is invariant under projective transformations, and there is only one polytope in each of these classes up to projective equivalence, Corollary 5.12 follows from the psd-minimality of these representative polytopes.

6. Four interesting classes of 4-polytopes (classes 12–15)

For the remaining classes from Table 1 we want to establish conditions for psdminimality. Since the table lists a psd-minimal instance in each class, every class contains psd-minimal polytopes. In this section, we consider the dual pairs 1213 and 14-15. In theory, a method to derive conditions for the psd-minimality of polytopes of a ﬁxed combinatorial type is as follows.

- (1) Compute the slack ideal IP ⊂ R[x1,...,xt] of a polytope P in the class and let JP be a copy of IP in the variables y1,...,yt.
- (2) Consider the ideal

KP = IP + JP + yi2 − xi i = 1,...,t ⊂ R[x1,...,xt,y1,...,yt].

By construction, for any (x,y) ∈ V(KP) the matrix SP(y) is a Hadamard square root of SP(x). Thus, the polytope P is psd-minimal if and only if there are s, r ∈ Rt such that (s,r) ∈ V(KP) and SP = SP(s).

- (3) Eliminating y1,...,yt from KP we obtain the ideal KP ∩ R[x1,...,xt]. A minimal generating set of this elimination ideal gives the conditions for a polytope in the class of P to be psd-minimal.


In practice, the computation of the slack ideal as deﬁned in Deﬁnition 5.1 is often prohibitive due to the large number of variables in SP(x). Therefore, in this section and the next, we rely on various simpliﬁcations. We ﬁrst illustrate these ideas on the combinatorial class 12.

- Example 6.1 (Class 12). By scaling the rows and columns of a slack matrix of P, an operation that leaves both psd rank and square root rank unchanged, we may


assume that several of the variables xi in SP(x) have been set to one. This allows us to start with the following partially symbolic slack matrix of a polytope in class 12 in only 13 variables





1 0 0 0 0 1 1 1

- x1 0 0 0 1 1 0 0 0 1 0 0 0 1 x12 x13 0 x4 0 0 x11 1 0 0
- x2 0 1 0 0 0 1 0 0 x5 x7 0 0 0 1 0
- x3 0 0 1 0 0 0 1 0 x6 0 x9 0 0 0 1 0 0 x8 x10 1 0 0 0


- (4) .


 

 

### To attain as many ones as we have above, we need to scale rows and columns in a carefully chosen order. For instance, in the above matrix, we can start by scaling columns 1,6,7,8 to get ones in the ﬁrst row, and then rows 2,...,8 to get

the remaining ones in the last three columns. Next we scale columns 2,...,5 to set the ﬁrst non-zero entry in each of those columns to one, and ﬁnally, we scale the last row to get the remaining one in the matrix. Note that if we are only interested in preserving the usual rank then we may also scale with negative scalars. This allows us to put any matrix with the same zero pattern as the above one into the same form without changing its rank. In all remaining examples, we ﬁx variables to one using a similar procedure.

Our goal is to obtain a parametrization of the slack matrices of class 12 with the scalings we have ﬁxed above. Saturating the ideal of all 6-minors of the above matrix we get the ideal

I = x13 − 1,x12 − 1,x11 − 1,x10 − 1,x9 − 1,x8 − 1,x7 − 1,

x3 − x6,x2 − x5,x4 + x5 + x6 − 1,x1 + x5 + x6 − 1 . All slack matrices of class 12 of the form (4) must satisfy the equations given by the generators of I. This ﬁxes all variables except x1,x2,x3 yielding





1 0 0 0 0 1 1 1

- x1 0 0 0 1 1 0 0 0 1 0 0 0 1 1 1 0 x1 0 0 1 1 0 0
- x2 0 1 0 0 0 1 0 0 x2 1 0 0 0 1 0
- x3 0 0 1 0 0 0 1 0 x3 0 1 0 0 0 1 0 0 1 1 1 0 0 0


.

 

 

Running the ideal calculation again yields the principal ideal with generator

x1 + x2 + x3 − 1. Thus we can conclude that the matrices of rank 5 with the same zero-pattern as a slack matrix of class 12 can be parametrized (up to scalings) as





1 0 0 0 0 1 1 1

- x1 0 0 0 1 1 0 0 0 1 0 0 0 1 1 1 0 x1 0 0 1 1 0 0
- x2 0 1 0 0 0 1 0 0 x2 1 0 0 0 1 0


- (5) .

In particular, for every polytope P in class 12 we can choose a slack matrix SP of the above form. If P is psd-minimal then there is a Hadamard square root of SP of rank at most ﬁve. As remarked earlier, we can scale rows and columns of the Hadamard square root to bring it into the form (4). Due to the rank condition, the Hadamard square root has the same symbolic form as (5).

Let us denote the parameters of SP by x1 and x2 and the ones of its square root by y1 and y2. Therefore, for psd-minimality we must have

- (6) y12 = x1, y22 = x2, (1 − y1 − y2)2 = 1 − x1 − x2. Eliminating y1,y2 from these equations we obtain the following condition on x1,x2:
- (7) x41 + 2x31x2 + 3x21x22 + 2x1x32 + x42 − 2x31 − 2x32 + x21 − 2x1x2 + x22 = 0.


1 − x1 − x2 0 0 1 0 0 0 1 0 1 − x1 − x2 0 1 0 0 0 1 0 0 1 1 1 0 0 0

 

 

![image 1](<2015-gouveia-four-dimensional-polytopes-minimum-positive_images/imageFile1.png>)

Figure 19. Set of parameters for which psd-minimality is veriﬁed on combinatorial type 12.

Thus the psd-minimal polytopes in the combinatorial class 12 are those whose slack matrices can be parametrized (up to scalings) as in (5) with x1,x2 satisfying

- (7). The algebraic variety of (7) is shown in Figure 19.


The above calculation proves the following statement for classes 12 and 13.

- Proposition 6.2. A polytope in the combinatorial class 12 (respectively, 13) is psdminimal if and only if, the entries of its slack matrix in the form (5) (respectively, transpose of (5)) satisfy the quartic equation (7).


This example breaks some conjectures on the behavior of square root rank and psd-minimality which we now discuss.

- (1) Up to now, in all known psd-minimal polytopes, the positive square root

+

√SP of the slack matrix SP had rank d + 1. It was asked in Problem 2 [BKLT13] whether this was always the case for psd-minimal polytopes. If we set x1 = 1/9 and x2 = 4/9 in the parametrization (5), condition (7) is veriﬁed and the resulting matrix is a slack matrix of a psd-minimal polytope in class 12. However it is easy to see that the positive square root of this slack matrix is not of rank ﬁve, in fact, we must take the square root parametrized by y1 = −1/3 and y2 = 2/3 to obtain one of rank ﬁve.

- (2) The support matrix of a matrix M is the 0,1 matrix with the same zero pattern as M. A weaker version of the previous conjecture that is also broken by this example is that the support matrix of a psd-minimal d-polytope is always of rank d + 1. This was true in all previously known examples, but here it is trivial to check that the support matrix has rank larger than


5. This, in some sense, provides evidence that the class of psd-minimal polytopes is fundamentally larger than the class of 2-level polytopes.

- Example 6.3 (Class 14). We employ the same general ideas that we used for class


12. Scaling the rows and columns of the symbolic slack matrix of a polytope in

class 14 to set as many entries to 1 as possible, we obtain the symbolic matrix 



1 1 1 1 0 0 0 0 1 x3 0 0 x7 0 0 0 0 x4 1 x5 0 x10 0 0

- 0 1 0 0 x8 x11 0 0 x1 0 0 1 0 0 1 0

- 0 0 0 x6 0 1 1 0 x2 0 1 0 0 0 0 1
- 0 0 1 0 0 x12 0 x16


- 1 0 0 0 1 0 x14 x17 0 0 0 0 x9 x14 x15 1


- (8) .

We then saturate the ideal of the 6-minors of the above matrix, and use all the linear generators to eliminate variables as we did in the previous example. In addition, we also use some of the quadratic generators to eliminate more variables. For instance, the polynomial x8x17 − 1 is a generator of the ideal and can be used to replace x17 by 1/x8. Since scalings are allowed, we then multiply the row by x8 to get rid of denominators. Continuing this way, we arrive at a parametrization of the slack matrices of class 14 in the form



 

- x10 1 1 1 0 0 0 0
- x11 1 0 0 1 0 0 0 0 1 1 1 0 x10 0 0

- 0 1 0 0 1 x11 0 0
- 1 0 0 1 0 0 1 0


- 0 0 0 1 0 1 1 0

x12 0 1 0 0 0 0 1

- 0 0 1 0 0 x12 0 1




1 + x12 + x11 − x10 0 0 0 1 0 1 1 0 0 0 0 1 1 + x12 + x11 − x10 1 1



 

- (9) .

As before, we let y1,y2 and y3 be the parameters of a symbolic square root of the above slack matrix. Then psd-minimality imposes the conditions

- (10) y12 = x10, y22 = x11, y32 = x12, (1 − y1 + y2 + y3)2 = 1 − x10 + x11 + x12. Eliminating the y variables, results in the following degree eight algebraic equation:

x810 − 4x11x710 − 4x12x710 − 4x710 + 6x211x610 + 6x212x610 + 16x11x610 + 16x11x12x610 + 16x12x610 + 6x610− 4x311x510 − 4x312x510 − 24x211x510 − 24x11x212x510 − 24x212x510 − 24x11x510 − 24x211x12x510 − 60x11x12x510− 24x12x510 − 4x510 + x411x410 + x412x410 + 16x311x410 + 16x11x312x410 + 16x312x410 + 36x211x410+ 36x211x212x410 + 76x11x212x410 + 36x212x410 + 16x11x410 + 16x311x12x410 + 76x211x12x410 + 76x11x12x410+ 16x12x410 + x410 − 4x411x310 − 4x11x412x310 − 4x412x310 − 24x311x310 − 24x211x312x310 − 36x11x312x310− 24x312x310 − 24x211x310 − 24x311x212x310 − 76x211x212x310 − 76x11x212x310 − 24x212x310 − 4x11x310 −4x411x12x310 − 36x311x12x310 − 76x211x12x310 − 36x11x12x310 − 4x12x310 + 6x411x210 + 6x211x412x210+ 4x11x412x210 + 6x412x210 + 16x311x210 + 16x311x312x210 + 20x211x312x210 + 20x11x312x210 + 16x312x210+ 6x211x210 + 6x411x212x210 + 20x311x212x210 + 82x211x212x210 + 20x11x212x210 + 6x212x210 + 4x411x12x210+ 20x311x12x210 + 20x211x12x210 + 4x11x12x210 − 4x411x10 − 4x311x412x10 + 4x211x412x10 + 4x11x412x10− 4x412x10 − 4x311x10 − 4x411x312x10 + 4x311x312x10 − 32x211x312x10 + 4x11x312x10 − 4x312x10+ 4x411x212x10 − 32x311x212x10 − 32x211x212x10 + 4x11x212x10 + 4x411x12x10 + 4x311x12x10 + 4x211x12x10+ x411 + x411x412 − 4x311x412 + 6x211x412 − 4x11x412 + x412 − 4x411x312 + 4x311x312 + 4x211x312 − 4x11x312+ 6x411x212 + 4x311x212 + 6x211x212 − 4x411x12 − 4x311x12 = 0.

- (11)


 

 

![image 2](<2015-gouveia-four-dimensional-polytopes-minimum-positive_images/imageFile2.png>)

Figure 20. Set of parameters for which psd-minimality is veriﬁed on combinatorial type 14.

Thus the psd-minimal polytopes in the combinatorial class 14 are those whose slack matrices can be parametrized (up to scalings) as in (9) with x10,x11,x12 satisfying (11). This algebraic variety is shown in Figure 20.

- Proposition 6.4. A polytope in the combinatorial class 14 (respectively, 15) is psdminimal if and only if, the entries of its slack matrix in the form (9) (respectively, transpose of (9)) satisfy the degree eight equation (11).


7. The remaining cases: classes 16–31

In this section we brieﬂy describe the methods to characterize psd-minimality in the remaining combinatorial classes from Table 1.

- 7.1. The 3-cube. To illustrate the techniques, and because we use this in the forthcoming arguments, we reprove the conditions under which a cube (or dually, an octahedron) is psd-minimal.


As before, we scale the rows and columns of the symbolic slack matrix of a cube to ﬁx 15 entries to be one, obtaining the following matrix:





1 0 1 0 1 0 1 0 x1 0 0 1 1 0 0 1 x6 0 1 0 0 x3 0 x9 0 1 1 0 x7 0 0 1 x2 0 0 x10 0 1 0 x4 x8 0 0 1 0 x5 0 x11

- (12) .


 

 

Computing the saturation of the ideal of 5-minors of this matrix, we obtain algebraic conditions that allow us to eliminate variables and get the matrix





1 0 1 0 1 0 1 0 x1 0 0 1 1 0 0 1 x6 0 1 0 0 x1x9 − x9 + 1 0 x9 0 1 1 0 x7 0 0 1 x1x7 − x7 + 1 0 0 x7 0 1 0 1 x6 + x7 − 1 0 0 1 0 x1x11 − x11 + 1 0 x11

- (13) .

Instead of eliminating more variables, we now impose psd-minimality requirements on this matrix. If matrix (12) and one of its square roots have rank four, both have the parametrization (13). Let y1 and y11 denote the square roots of x1 and x11 respectively. Entry (8,4) then implies that

y12y112 − y112 + 1 = x1x11 − x11 + 1 = (y1y11 − y11 + 1)2.

Simplifying, we obtain y1(1 − y1)(1 − y11) = 0 which implies either y1 or y11 is 1. Similarly, looking at the other entries of (13) we get that y1 or y7 must be 1, y1 or y9 must be 1, and y6 or y7 must be 1.

Therefore, if y1 is not 1 then y9,y7 and y11 must be 1. Making this substitution and recomputing the ideal we see that y6 must be 1. If y1 is 1, further computations force us to decide if y6 or y7 is 1. In the end we get three possibilities for a Hadamard square root of rank four:



 

1 0 1 0 1 0 1 0 y1 0 0 1 1 0 0 1 1 0 1 0 0 y1 0 1 0 1 1 0 1 0 0 1 y1 0 0 1 0 1 0 1 1 0 0 1 0 y1 0 1



 

or



 

1 0 1 0 1 0 1 0 1 0 0 1 1 0 0 1 y6 0 1 0 0 1 0 y6 0 1 1 0 1 0 0 1 1 0 0 1 0 1 0 1 y6 0 0 1 0 1 0 y6



 

or



 

1 0 1 0 1 0 1 0 1 0 0 1 1 0 0 1 1 0 1 0 0 1 0 1 0 1 1 0 y7 0 0 1 1 0 0 y7 0 1 0 1 y7 0 0 1 0 1 0 y7



 

- (14) .

The three possibilities above are the same up to permuting rows and columns, which yields the following result.

- Proposition 7.1. A 3-cube is psd-minimal if and only if its slack matrix, up to scalings and permutations of rows and columns is of the form


- (15)


 

 





1 0 1 0 1 0 1 0 1 0 0 1 1 0 0 1 x 0 1 0 0 1 0 x 0 1 1 0 1 0 0 1 1 0 0 1 0 1 0 1 x 0 0 1 0 1 0 x

.

 

 

Remark 7.2. From the proof of Proposition 7.1 it follows that a psd-minimal 3-cube has a slack matrix of the same support as (12) such that both the slack matrix, and each of its Hadamard square roots of rank four, have the property that their ﬁrst, second, third and fourth columns are linearly dependent, and also the third, fourth, ﬁfth and sixth columns are dependent.

Furthermore, the matrix in (15) is the slack matrix of the Cartesian product of the unit segment and the trapezoid with vertices {(0,0),(1,0),(0,1),(x,1)}, hence by Corollary 1.5, a 3-cube is psd-minimal if and only if it is projectively equivalent to the product of a segment and a trapezoid. Note that Proposition 7.1, together with Proposition 2.6 and Theorem 5.6 ﬁnishes an alternate proof of the complete characterization of psd-minimality in R3, as stated in Theorem 1.2.

In what follows we make extensive use of the above idea of imposing psdminimality requirements during the process of parametrizing the slack matrix to make some entries constant at the price of branching the computation. This makes the computations possible and easier to track. We can also explicitly use the parametrization (15) whenever a 4-polytope or its dual has a cubical or octahedral facet, since facets of psd-minimal polytopes must be psd-minimal. This allows us to set many variables to 1 at the start, leading to big computational savings. These tricks are enough to complete the characterization of psd-minimality in the remaining classes from Table 1.

- 7.2. Classes 16–31. We ﬁrst provide the full result for classes 19 through 27 leaving the remaining classes to be explored in more detail after that. The computations follow the exact same ideas as in the previous sections, and hence are not included in the paper.


- Proposition 7.3. A polytope of combinatorial type 16, 18, 20, 22, 24 or 26 (respectively 17, 19, 21, 23, 25 or 27) is psd-minimal if and only if, after scaling and permuting rows and columns, its slack matrix (respectively, its transpose) is of the following form:






1 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 1 0 0 1 0 0 1 0 1 0 0 1 1 0 x 0 0 0 1 1 0 0 x 0 0 1 0 1 x 0 0 0 1 0 1 0 x 0 0 0 0 0 0 0 1

,

 

 





1 1 0 0 0 0 0 0

- 0 0 1 0 1 0 1 0

- 0 0 1 0 1 0 0 1
- 0 1 1 0 0 1 1 0


- 0 1 1 0 0 1 0 1 1 0 0 1 1 0 x 0 1 0 0 1 1 0 0 x 0 0 0 1 0 1 x 0 0 0 0 1 0 1 0 x


,

 

 





1 0 0 0 0 1 0 1 0 0 0 0 0 1 0 1 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 1 0 0 1 0 0 1 0 1 0 0 1 1 0 x 0 0 0 1 1 0 0 x 0 0 1 0 1 x 0 0 0 1 0 1 0 x

 

 





1 1 1 0 0 0 0 0 0 1 1 0 1 0 1 0 1 0 1 0 0 1 0 1 0 0 1

- 0 0 0 1 0 0 1 1 0
- 1 0 1 1 0 0 1 0 1


,

,

- 0 x 0 0 1 1 0 x 0

- 0 0 0 0 1 1 0 0 x

0 x 1 0 1 0 1 x 0

- 0 0 1 0 1 0 1 0 x




 

 









1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 1 0 1 0 0 1 1 0 0 1 1 0 1 0 0 1 1 0 1 0 0 1 0 1 1 0 0 1 0 1 0 1 1 0 x 0 0 1 1 0 x 0 0 1 1 0 0 x 0 1 1 0 0 x 0 1 0 1 x 0 0 1 0 1 x 0 0 1 0 1 0 x 0 1 0 1 0 x 0 0 0 0 0 0 y 1 1 y y x y 1 1 y y x 0 0 0 0 0 0

1 0 1 0 1 0 1 0 0 0 1 0 1 0 0 1 1 1 1 0 1 0 0 1 1 0 1 x 0 1 1 0 0 1 0 1 0 x 0 0 0 1 1 0 x 0 x 0 x x 0 1 1 0 0 x 0 0 x 0 0 1 0 1 x 0 0 0 0 1 0 1 0 1 0 x 0 x x 1

.

,

 

 

 

 

- 0 0 0 0 0 0 1 1 1 1
- 1 1 1 1 1 x 0 0 0 0


A point to note is that in all these cases, the positive square root and the support of the slack matrix are of rank ﬁve. Thus these classes fail to provide counterexamples to the conjectures that were disproved by the polytopes in classes 12-15 as discussed before. Furthermore, unlike in classes 12-15 where the spaces of slack matrices of psd-minimal polytopes were higher degree algebraic varieties, in the above cases, these are just aﬃne spaces.

We now come to the last two dual pairs of combinatorial classes from Table 1.

- Proposition 7.4. A polytope of combinatorial type 28 (respectively 29) is psdminimal if and only if, after scaling and permuting rows and columns, its slack matrix (respectively, its transpose) is of one of the following forms:










0 1 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 1 0 0 1 0 0 1 0 1

0 1 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 x 0 0 1 0 0 1 0 x

- 0 0 1 1 0 y 0

- 0 0 1 1 0 0 y

- 0 0 1 0 1 y 0

- 0 0 1 0 1 0 y
- 1 0 0 1 0 x 0


- 1 0 0 1 0 0 x


- 1 0 0 0 1 x 0


- 1 0 0 0 1 0 x


- 0 0 1 1 0 1 0

- 0 0 1 1 0 0 1

- 0 0 1 0 1 x 0

- 0 0 1 0 1 0 x
- 1 0 0 1 0 1 0


- 1 0 0 1 0 0 1


- 1 0 0 0 1 x 0


- 1 0 0 0 1 0 x


,

 

 

 

 

While it is still true that the positive square root and the support of these slack matrices have rank ﬁve, it diﬀers from the previous instances since the space of slack matrices is a union of two components, each an aﬃne space. One can check that the ﬁrst case corresponds to polytopes projectively equivalent to the product of a triangle and a trapezoid, while the second corresponds to those projectively equivalent to a prism over a wedge.

The computation involved in Proposition 7.4 is similar to those in Proposition 7.3. The only diﬀerence is that while in classes 16-27 all the slack matrices obtained by the disjunctive process collapse to the same one, in classes 28 and 29 two distinct slack matrices remain at the end.

We now consider the 4-cube and its dual. Once again we will see that the space of slack matrices is the union of two components, however the techniques used are more involved than in the previous cases.

- Example 7.5 (Class 30: the 4-cube). We start by reordering rows and columns of the slack matrix so that the upper left 8 × 6 submatrix corresponds to the slack


### matrix of a facet of the 4-cube. If the 4-cube is psd-minimal, this facet is as well, and hence, we can assume that this submatrix is as in Proposition 7.1:





1 0 1 0 1 0 x25 0 1 0 1 0 0 1 x26 0 1 0 0 1 x 0 x27 0 1 0 0 1 0 x x28 0 0 1 1 0 0 0 x29 0 0 1 1 0 0 0 x30 0 0 1 0 1 x 0 x31 0 0 1 0 1 0 x x32 0 x1 0 x9 0 x17 0 0 x33 x2 0 x10 0 0 x21 0 x34 x3 0 0 x13 x18 0 0 x35 x4 0 0 x14 0 x22 0 x36

.

0 x5 x11 0 x19 0 0 x37 0 x6 x12 0 0 x23 0 x38 0 x7 0 x15 x20 0 0 x39 0 x8 0 x16 0 x24 0 x40

 

 

There are still too many variables for computations, but we can repeat the idea on the lower left submatrix, which also corresponds to the slack matrix of a 3-cube. Recall that we already used scalings and permutations of the ﬁrst six columns to put the top left 8 × 6 submatrix into the present form. Therefore we can only assume that the bottom left 8 × 6 submatrix is of one of the forms in (14) up to column scalings. Since we want to keep the top left submatrix intact, we cannot freely permute to reduce the three possible matrices in (14) to just one as we did in Proposition 7.1. However, there is enough freedom to reduce it to one of the last two types in (14). In addition, scaling the last two columns of the full slack matrix, we get two possibilities:





1 0 1 0 1 0 1 0 1 0 1 0 0 1 x9 0 1 0 0 1 1 0 x10 0 1 0 0 1 0 1 x11 0 0 1 1 0 x1 0 x12 0 0 1 1 0 0 x1 x13 0 0 1 0 1 x1 0 x14 0 0 1 0 1 0 x1 x15 0

x2 0 x4 0 x6 0 0 1 x2 0 x4 0 0 x8 0 x16 x2 0 0 x5 x6x7 0 0 x17 x2 0 0 x5 0 x8x7 0 x18

0 x3 x4 0 x6 0 0 x19 0 x3 x4 0 0 x8 0 x20 0 x3 0 x5 x6x7 0 0 x21 0 x3 0 x5 0 x8x7 0 x22

 

 





1 0 1 0 1 0 1 0 1 0 1 0 0 1 x9 0 1 0 0 1 1 0 x10 0 1 0 0 1 0 1 x11 0 0 1 1 0 x1 0 x12 0 0 1 1 0 0 x1 x13 0 0 1 0 1 x1 0 x14 0 0 1 0 1 0 x1 x15 0

.

x2 0 x4 0 x6 0 0 1 x2 0 x4 0 0 x8 0 x16 x2 0 0 x5 x6 0 0 x17 x2 0 0 x5 0 x8 0 x18

0 x3 x4 0 x6x7 0 0 x19 0 x3 x4 0 0 x8x7 0 x20 0 x3 0 x5 x6x7 0 0 x21 0 x3 0 x5 0 x8x7 0 x22

 

 

We then apply our techniques to each of them, with the added idea that we not always take the full ideal of the 6-minors, opting instead to work with minors of submatrices to reduce the size of computations while still eliminating variables. There are several branching points but in the end we obtain just two distinct possibilities, as described in the proposition below.

Proposition 7.6. A combinatorial 4-cube (respectively a combinatorial 4-cross polytope) is psd-minimal if and only if, after scaling and permuting rows and columns

its slack matrix (respectively its transpose) has one of the following forms: 







1 0 1 0 1 0 1 0 1 0 1 0 0 1 1 0 1 0 0 1 1 0 1 0 1 0 0 1 0 1 1 0

1 0 1 0 1 0 1 0 1 0 1 0 0 1 1 0 1 0 0 1 1 0 y 0 1 0 0 1 0 1 y 0

- 0 1 1 0 x 0 y 0

- 0 1 1 0 0 x y 0

- 0 1 0 1 x 0 y 0

- 0 1 0 1 0 x y 0
- 1 0 1 0 1 0 0 1


- 1 0 1 0 0 1 0 1


- 1 0 0 1 1 0 0 1


- 1 0 0 1 0 1 0 1 0 1 1 0 x 0 0 y 0 1 1 0 0 x 0 y 0 1 0 1 x 0 0 y 0 1 0 1 0 x 0 y


- 0 1 1 0 x 0 1 0

- 0 1 1 0 0 x 1 0

- 0 1 0 1 x 0 y 0 0 1 0 1 0 x y 0 1 0 1 0 1 0 0 1
- 1 0 1 0 0 1 0 1


- 1 0 0 1 1 0 0 y


- 1 0 0 1 0 1 0 y 0 1 1 0 x 0 0 1 0 1 1 0 0 x 0 1 0 1 0 1 x 0 0 y 0 1 0 1 0 x 0 y


.

or

 

 

 

 

One can check that the ﬁrst slack matrix is the slack matrix of the product of two trapezoids, namely the ones with vertices {(0,0),(1,0),(0,1),(1,x)} and {(0,0),(1,0),(0,1),(1,y)}, while the second one is the slack matrix of the polytope with vertices ({0} × {0,1}3) ∪ ({1} × {0,1} × {0,x} × {0,y}), a cubical prismoid.

8. Open questions

In this paper we classiﬁed all psd-minimal 4-polytopes. Such a classiﬁcation in higher dimensions seems unwieldy with the current techniques, although it might be possible to tackle 5-polytopes using similar ideas to those in this paper. For any ﬁxed d there is only a ﬁnite number of combinatorial classes of psd-minimal d-polytopes. An answer to the following question, besides being of independent interest, would also be useful for eﬃciently enumerating these classes.

- Problem 8.1. What is the maximum number of facets in a psd-minimal d-polytope?

By the invariance of psd rank under polarity, this is equivalent to asking how many vertices a psd-minimal d-polytope can have. For 2-level polytopes in Rd, it was shown in [GPT10] that the number of vertices and facets cannot exceed 2d and that this bound is tight. Since 2-level polytopes are all psd-minimal, 2d is a lower bound for the maximum number of facets in a psd-minimal d-polytope, and we suspect that it is in fact also an upper bound.

It might be easier to classify psd-minimal polytopes of a ﬁxed combinatorial type. For instance, [0,1]d is 2-level and thus a psd-minimal d-polytope.

- Problem 8.2. What are the precise conditions for psd-minimality of a d-cube (crosspolytope)?

The cube [0,1]d is a product of psd-minimal polytopes, and it is natural to ask about the connection between psd-minimality and standard polytope operations.

- Problem 8.3. How does psd-minimality behave under the polytope operations of free sum, product and join?


- We saw that, unlike a d-cube, some polytopes are combinatorially psd-minimal, in particular, those with a binomial slack ideal. All known combinatorially psdminimal polytopes have a binomial slack ideal (see Section 5).
- Problem 8.4. Is the slack ideal of a combinatorially psd-minimal polytope always binomial?

All d-polytopes with at most d + 2 vertices have a binomial slack ideal. We also saw in Section 5 that there are psd-minimal d-polytopes with more than d + 2 vertices that have binomial slack ideals.

- Problem 8.5. What can be said about the combinatorics of a polytope with a binomial slack ideal?

Toric ideals [Stu96] form a rich class of binomial ideals and we saw in Section 5 that the slack ideal of a d-polytope with d + 2 vertices is, in fact, toric.

- Problem 8.6. When a slack ideal is binomial, is it also toric?

We saw that the stable set polytope of a perfect graph is 2-level, and thus psdminimal. Further, this polytope admits a simple semideﬁnite representation that allows the stable set problem to be solved in polynomial time in a perfect graph.

- Problem 8.7. Are there other interesting examples of polytopes from combinatorial optimization that are psd-minimal (and not necessarily 2-level)? Do these polytopes admit semideﬁnite representations that lead to eﬃcient algorithms for linear optimization over them?


References

[BDP13] J. Brie¨t, D. Dadush, and S. Pokutta. On the existence of 0/1 polytopes with high semideﬁnite extension complexity. In Algorithms, ESA 2013, volume 8125 of Lecture Notes in Computer Science, pages 217–228. Springer Berlin Heidelberg, 2013.

- [BFF+a] A. Bohn, Y. Faenza, S. Fiorini, V. Fisikopoulos, M. Macchia, and K. Pashkovich. Enumeration of 2-level polytopes. preprint.
- [BFF+b] A. Bohn, Y. Faenza, S. Fiorini, V. Fisikopoulos, M. Macchia, and K. Pashkovich. Survey on 2-level polytopes. in preparation.


[BKLT13] L.B. Beasley, H. Klauck, T. Lee, and D.O. Theis. Communication complexity, linear optimization, and lower bounds for the nonnegative rank of matrices (Dagstuhl Seminar 13082). Dagstuhl Reports, 3(2):127–143, 2013.

[Boo12] A. Boocher. Free resolutions and sparse determinantal ideals. Math. Res. Lett., 19(4):805–821, 2012. [FGP+15] H. Fawzi, J. Gouveia, P.A. Parrilo, R.Z. Robinson, and R.R. Thomas. Positive semideﬁnite rank. Math. Program., 153(1, Ser. B):133–177, 2015. [FP13] H. Fawzi and P.A. Parrilo. Exponential lower bounds on ﬁxed-size psd rank and semideﬁnite extension complexity. CoRR, abs/1311.2571, 2013. [FSP] H. Fawzi, J. Saunderson, and P.A. Parrilo. Equivariant semideﬁnite lifts of regular polygons. Mathematics of Operations Research. to appear.

[GGK+13] J. Gouveia, R. Grappe, V. Kaibel, K. Pashkovich, R.Z. Robinson, and R.R. Thomas. Which nonnegative matrices are slack matrices? Linear Algebra and its Applications, 439(10):2921 – 2933, 2013.

[GM82] M. Giusti and M. Merle. Singularite´s isole´es et sections planes de varie´t´es de´terminantielles. II. Sections de varie´t´es de´terminantielles par les plans de coordonn´ees. In Algebraic geometry (La Ra´bida, 1981), volume 961 of Lecture Notes in Math., pages 103–118. Springer, Berlin, 1982.

[GPT10] J. Gouveia, P.A. Parrilo, and R.R. Thomas. Theta bodies for polynomial ideals. SIAM J. Optim., 20(4):2097–2118, 2010.

[GPT13] J. Gouveia, P.A. Parrilo, and R.R. Thomas. Lifts of convex sets and cone factorizations. Mathematics of Operations Research, 38(2):248–264, 2013.

[GRT13] J. Gouveia, R. Z. Robinson, and R. R. Thomas. Polytopes of minimum positive semideﬁnite rank. Discrete & Computational Geometry, 50(3):679–699, 2013. [Gru¨03] B. Gru¨nbaum. Convex Polytopes, volume 221 of Graduate Texts in Mathematics.

Springer, New York, 2003.

- [GSa] F. Grande and R. Sanyal. Theta rank, levelness, and matroid minors. arXiv:1408.1262.
- [GSb] D.R. Grayson and M.E. Stillman. Macaulay2, a software system for research in algebraic geometry. Available at http://www.math.uiuc.edu/Macaulay2/.


[Lov79] L. Lov´asz. On the Shannon capacity of a graph. IEEE Trans. Inform. Theory, 25(1):1– 7, 1979. [LRS14] J.R. Lee, P. Raghavendra, and D. Steurer. Lower bounds on the size of semideﬁnite programming relaxations. CoRR, abs/1411.6317, 2014. [LW14] T. Lee and Z. Wei. The square root rank of the correlation polytope is exponential. CoRR, abs/1411.6712, 2014. [LWdW14] T. Lee, Z. Wei, and R. de Wolf. Some upper and lower bounds on psd-rank. CoRR, abs/1407.4308, 2014. [McM76] P. McMullen. Constructions for projectively unique polytopes. Discrete Mathematics, 14(4):347 – 358, 1976. [S+15] W. A. Stein et al. Sage Mathematics Software (Version 5.11). The Sage Development Team, 2015. http://www.sagemath.org. [Stu96] B. Sturmfels. Gro¨bner Bases and Convex Polytopes, volume 8 of University Lecture Series. American Mathematical Society, Providence, RI, 1996.

CMUC, Department of Mathematics, University of Coimbra, 3001-454 Coimbra, Por-

tugal E-mail address: jgouveia@mat.uc.pt Department of Combinatorics and Optimization, University of Waterloo, 200 Uni-

versity Ave. W Waterloo, Ontario, Canada, N2L 3G1 E-mail address: kanstantsin.pashkovich@gmail.com Department of Mathematics, University of Washington, Box 354350, Seattle, WA

98195, USA E-mail address: rzr@uw.edu Department of Mathematics, University of Washington, Box 354350, Seattle, WA

98195, USA E-mail address: rrthomas@uw.edu

