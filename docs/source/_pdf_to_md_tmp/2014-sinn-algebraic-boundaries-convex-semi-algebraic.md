# arXiv:1405.7822v2[math.AG]3Nov2014

## ALGEBRAIC BOUNDARIES OF CONVEX SEMI-ALGEBRAIC SETS

RAINER SINN

Abstract. We study the algebraic boundary of a convex semi-algebraic set via duality in convex and algebraic geometry. We generalize the correspondence of facets of a polytope with the vertices of the dual polytope to general semi-algebraic convex sets. In this case, exceptional families of extreme points might exist and we characterize them semi-algebraically. We also give an algorithm to compute a complete list of exceptional families, given the algebraic boundary of the dual convex set.

1. Introduction

The algebraic boundary of a semi-algebraic set is the smallest algebraic variety containing its boundary in the euclidean topology. For a full-dimensional polytope Rn, it is the hyperplane arrangement associated to its facets which has been studied extensively in discrete geometry and complexity theory in linear programming [4]. The algebraic boundary of a convex set which is not a polytope has recently been considered in other special cases, most notably the convex hull of a variety by Ranestad and Sturmfels, cf. [11] and [12]. This class includes prominent families such as the moment matrices of probability distributions and the highly symmetric orbitopes. It does not include examples such as hyperbolicity cones and spectrahedra, which have received attention from applications of semi-deﬁnite programming in polynomial optimisation, see [2] and [18], and statistics of Gaussian graphical models, see [16].

First steps towards using the algebraic boundary of a spectrahedron for a complexity analysis of semi-deﬁnite programming have been taken by Nie, Ranestad, and Sturmfels [9]. For semi-deﬁnite liftings of convex semi-algebraic sets via Lasserre relaxations or theta body construction, the singularities of the algebraic boundary on the convex set give obstructions, cf. [8], [6].

So algebraic boundaries are central objects in applications of algebraic geometry to convex optimisation and statistics. In this paper, we want to consider the class of all sets for which the algebraic boundary is an algebraic hypersurface: convex semi-algebraic sets with non-empty interior. Our goal in this paper is to extend the study of the algebraic boundary of the convex hull of a variety started by Ranestad and Sturmfels in [11] and [12] to general convex semi-algebraic sets. The most natural point of view in the general setting is via convex duality and its algebraic counterpart in projective algebraic geometry.

2010 Mathematics Subject Classiﬁcation. Primary: 52A99, 14N05, 14P10; Secondary: 51N35, 14Q15.

Key words and phrases. algebraic boundary, convex semi-algebraic set, projective dual variety.

1

The ﬁrst main theorem generalizes and implies the correspondence between facets of a polytope with vertices of its dual polytope.

Theorem (Corollary 3.4). Let C ⊂ Rn be a compact convex semi-algebraic set with 0 ∈ int(C). Let Z be an irreducible component of the Zariski closure of the set of extreme points of its dual convex body. Then the variety dual to Z is an irreducible component of the algebraic boundary of C.

For polytopes, this theorem is the whole story. In the general semi-algebraic case, not every irreducible component of the algebraic boundary of C arises in this way, as we will see below. We study the exceptional cases and give a complete semi-algebraic description of the exceptional families of extreme points in terms of convex duality (normal cones) and a computational way of getting a list of potentially exceptional strata from the algebraic boundary of the dual. This proves an assertion made by Sturmfels and Uhler in [16, Proposition 2.4].

The main techniques come from the duality theories in convex and projective algebraic geometry. For an introduction to convex duality, we refer to Barvinok’s textbook [1]. The duality theory for projective algebraic varieties is developed in several places, e.g. Harris [7], Tevelev [17], or Gelfand-KapranovZelevinsky [5].

This article is organized as follows: In Section 2, we introduce the algebraic boundary of a semi-algebraic set and discuss some special features of convex semi-algebraic sets coming from their algebraic boundary. The section sets the technical foundation for Section 3, where we prove the main results of this work.

2. The Algebraic Boundary and Convexity

This section is supposed to be introductory. We will ﬁx notation and observe some basic features of convex semi-algebraic sets, their algebraic boundary, and some special features relying on this algebraic structure. The main results will be proven in the following section.

Deﬁnition 2.1. Let S ⊂ Rn be a semi-algebraic set. The algebraic boundary of S, denoted as ∂aS, is the Zariski closure in An of the euclidean boundary of S.

Remark 2.2. In this paper, we ﬁx a subﬁeld k of the complex numbers. The most important choices to have in mind are the reals, the complex numbers or the rationals. When we say Zariski closure, we mean with respect to the k-Zariski topology, i.e. the topology on Cn (resp. P(Cn+1)) whose closed sets are the algebraic sets deﬁned by polynomials (resp. homogeneous polynomials) with coeﬃcients in k. The set Cn (resp. P(Cn+1)) equipped with the k-Zariski topology is usually denoted Ank (resp. Pnk). We drop the ﬁeld k in our notation. The statements in this paper are true over any subﬁeld k of the complex numbers given that the semi-algebraic set in consideration can be deﬁned by polynomial inequalities with coeﬃcients in k ∩ R.

If we are interested in symbolic computation, we tend to consider semialgebraic sets deﬁned by polynomial inequalities with coeﬃcients in Q and take Zariski closures in the Q-Zariski topology.

We ﬁrst want to establish that the algebraic boundary of a convex body is a hypersurface. Deﬁnition 2.3. A subset of Rn is called regular if it is contained in the closure (in the euclidean topology) of its interior.

- Remark 2.4. Every convex semi-algebraic set with non-empty interior is regular and the complement of a convex semi-algebraic set is also regular.


Lemma 2.5. Let ∅ = S ⊂ Rn be a regular semi-algebraic set and suppose that its complement Rn \ S is also regular and non-empty. Each irreducible component of the algebraic boundary of S has codimension 1 in An, i.e. ∂aS is a hypersurface.

Proof. By Bochnak-Coste-Roy [3, Proposition 2.8.13], dim(∂S) ≤ n − 1. Conversely, we prove that the boundary ∂S of S has local dimension n − 1 at each point x ∈ ∂S: Let x ∈ ∂S be a point and take > 0. Then int(S)∩B(x, ) and int(Rn\S)∩B(x, ) are non-empty, because both S and Rn\S are regular. Applying [3, Lemma 4.5.2], yields that

dim(∂S ∩ B(x, )) = dim(B(x, ) \ (int(S) ∪ (Rn \ S))) ≥ n − 1

Therefore, all irreducible components of ∂aS = clZar(∂S) have dimension n − 1.

- Example 2.6. The assumption of S being regular cannot be dropped in the above lemma. Write h := x2+y2+z2−1 ∈ R[x,y,z]. Let S be the union of the unit ball with the ﬁrst coordinate axis, i.e. S = {(x,y,z) ∈ R3: y2h(x,y,z) ≤ 0,z2h(x,y,z) ≤ 0}. The algebraic boundary of S is the union of the sphere V(h) and the line V(y,z), which is a variety of codimension 1 with a lower dimensional irreducible component.


- Remark 2.7. In the above proof of Lemma 2.5, we argue over the ﬁeld of real numbers. The algebraic boundary of S, where the Zariski closure is taken with respect to the k-Zariski topology for a diﬀerent ﬁeld k, is also a hypersurface. It is deﬁned by the reduced product of the Galois conjugates of the polynomial deﬁning ∂aS over R, whose coeﬃcients are algebraic numbers over k.


- Corollary 2.8. Let C ⊂ Rn be a compact semi-algebraic convex set with nonempty interior. Its algebraic boundary is a hypersurface.


This property characterises the semi-algebraic compact convex sets.

Proposition 2.9. A compact convex set with non-empty interior is semialgebraic if and only if its algebraic boundary is a hypersurface.

Proof. The converse follows from results in semi-algebraic geometry. Namely if the algebraic boundary ∂aC is an algebraic hypersurface, its complement Rn\(∂aC)(R) is a semi-algebraic set and the closed convex set C is the closure of

the union of ﬁnitely many of its connected components. This is semi-algebraic by Bochnak-Coste-Roy [3, Proposition 2.2.2 and Theorem 2.4.5].

By the construction of homogenisation in convexity, the algebraic boundary of a pointed and closed convex cone relates to the algebraic boundary of a compact base via the notion of aﬃne cones in algebraic geometry.

- Remark 2.10. Let C ⊂ Rn be a compact semi-algebraic convex set and let co(C) ⊂ R×Rn be the convex cone over C embedded at height 1, i.e. co(C) = {(λ,λx): λ ≥ 0,x ∈ C}. Since a point (1,x) lies in the boundary of co(C) if and only if x is a boundary point of C, the aﬃne cone {(λ,λx): λ ∈ C,x ∈ ∂aC} over the algebraic boundary of C is a constructible subset of the algebraic boundary of co(C). More precisely, we mean that ∂a co(C) = X, where X is the projective closure of ∂aC with respect to the embedding An  → Pn, (x1,...,xn)  → (1 : x1 : ... : xn).


Recall that a closed convex cone C ⊂ Rn is called pointed if C∩(−C) = {0}, i.e. it does not contain a line.

- Corollary 2.11. Let C ⊂ Rn+1 be a pointed closed semi-algebraic convex cone. Its algebraic boundary is a hypersurface in An+1 and an algebraic cone. In particular, it is the aﬃne cone over its projectivisation in Pn, i.e.


P∂aC = ∂aC.

We will now take a look at convex duality for semi-algebraic sets. Given a compact convex set C ⊂ Rn, we write Co = { ∈ (Rn)∗: (x) ≥ −1 for all x ∈ C} for the dual convex set. We use the notation Xreg for the set of all regular (or smooth) points of an algebraic variety X.

- Proposition 2.12. Let C ⊂ Rn be a compact semi-algebraic convex set with


0 ∈ int(C) and set S := ∂Co ∩ (∂aCo)reg. For every ∈ S, the face supported by is a point. The set S is an open and dense (in the euclidean topology) semi-algebraic subset of the set ∂Co of all supporting hyperplanes to C.

Proof. If evx is a supporting hyperplane to Co at , then (x) = −1 and Co lies in one halfspace deﬁned by evx. Therefore, (∂aCo)(R) lies locally around

in one halfspace deﬁned by evx and so evx deﬁnes the unique tangent hyperplane to ∂aCo at . Now we show that x is an extreme point of C, exposed by

. Suppose x = 21(y +z) with y,z ∈ C, then (y) = −1 and (z) = −1. Since y and z are, by the same argument as above, also normal vectors to the tangent hyperplane T ∂aCo, we conclude x = y = z.

The same statement is true for convex cones: We denote the dual convex cone to C ⊂ Rn+1 as C∨ = { ∈ (Rn+1)∗: (x) ≥ 0 for all x ∈ C}.

- Corollary 2.13. Let C ⊂ Rn+1 be a pointed closed semi-algebraic convex cone


with non-empty interior and set S := ∂C∨ ∩ (∂aC∨)reg. For every ∈ S, the face supported by is an extreme ray of C. The set S is open and dense (in the euclidean topology) semi-algebraic subset of ∂C∨.

- Example 2.14. (a) In the case that C is a polytope, the set S of regular points of the algebraic boundary is exactly the set of linear functionals exposing extreme points. Indeed, in this case the algebraic boundary of C is a union of aﬃne hyperplanes, namely the aﬃne span of its facets. A point in ∂C is a


regular point of the algebraic boundary ∂aC if and only if it lies in the relative interior of a facet, cf. Barvinok [1, Theorem VI.1.3]. These points expose the vertices of Co. (b) In general, a linear functional ∈ ∂Co exposing an extreme point of C does not need to be a regular point of the algebraic boundary of Co as the following example shows: Let C be the convex set in the plane deﬁned by the inequalities y ≥ (x + 1)2 − 3/2, y ≥ (x − 1)2 − 3/2 and y ≤ 1. Consider the extreme point x = (0,−1/2) of C. The dual face is the line segment between the vectors (−2,1) and (2,1), the normal vectors to the tangent lines to the curves deﬁned by y − (x + 1)2 + 3/2 and y − (x − 1)2 + 3/2, which meet transversally in x. Indeed, the linear functionals (−2,1) and (2,1) both expose extreme points; but they are each intersection points of a line and a quadric in the algebraic boundary of Co and so they are singular points of ∂aCo.

The extreme points (resp. rays) of a convex set play an important role for duality. They will also be essential in a description of the algebraic boundary using the algebraic duality theory. So we ﬁx the following notation:

Deﬁnition 2.15. (a) Let C ⊂ Rn be a convex semi-algebraic set. We denote by Exa(C) the Zariski closure of the union of all extreme points of C in An. (b) Let C ⊂ Rn+1 be a semi-algebraic convex cone. We write Exra(C) for the Zariski closure of the union of all extreme rays of C in An+1.

- Remark 2.16. (a) Note that the union of all extreme points of a convex semi-algebraic set is a semi-algebraic set by quantiﬁer elimination because the deﬁnition is expressible as a ﬁrst order formula in the language of ordered rings, cf. Bochnak-Coste-Roy [3, Proposition 2.2.4]. Therefore, its Zariski closure is an algebraic variety whose dimension is equal to the dimension of Ex(C) as a semi-algebraic set, cf. Bochnak-Coste-Roy [3, Proposition 2.8.2]. Of course, the same is true for convex cones and the Zariski closure of the union of all extreme rays. (b) Note that Exra(C) is an algebraic cone. In particular, we have


Exra(C) = PExra(C).

Lemma 2.17. Let C ⊂ Rn be a compact semi-algebraic convex set with 0 ∈ int(C). For a general extreme point x ∈ Exa(C) there is a supporting hyperplane 0 ∈ ∂Co exposing the face x and a semi-algebraic neighbourhood U of 0 in ∂Co such that every ∈ U supports C in an extreme point x and all x lie on the same irreducible component of Exa(C) as x.

By general we mean in this context that the statement is true for all points in a dense (in the Zariski topology) semi-algebraic subset of Exa(C).

Proof. By Straszewicz’s Theorem (see Rockafellar [14, Theorem 18.6]) and the Curve Selection Lemma from semi-algebraic geometry (see Bochnak-CosteRoy [3, Theorem 2.5.5]), a general extreme point is exposed. Let y ∈ Ex(C) be an exposed extreme point contained in a unique irreducible component Z of Exa(C) and denote by y an exposing linear functional. Let Z1,...,Zr be the irreducible components of Exa(C) labelled such that Z = Z1. Since the sets Zi ∩ ∂C ⊂ C are closed, they are compact. Now y is strictly greater than −1 on Zi ∩ ∂C for i > 1 and therefore, there is a neighbourhood U in ∂Co of y such that every ∈ U is still strictly greater than −1 on Zi ∩ ∂C. The intersection of this neighbourhood with the semi-algebraic set S of linear functionals exposing extreme points, which is open and dense in the euclidean topology by Proposition 2.12, is non-empty and open in ∂Co. Pick

0 from this open set, then the extreme point x exposed by 0 has the claimed properties.

- Example 2.18. (a) Again, the above lemma has a simple geometric meaning in the case of polytopes: Every extreme point of the polytope is exposed exactly by the relative interior points of the facet of the dual polytope dual to it, again by Barvinok [1, Theorem VI.1.3]. (b) In Example 2.14(b), the boundary of the convex set C consists of extreme points and a single 1-dimensional face. So the only linear functional not exposing an extreme point of C is the dual face to the edge of C, which is (0,−1) ∈ Ex(Co).


By homogenisation, we can prove the analogous version of the above lemma for closed and pointed convex cones.

- Corollary 2.19. Let C ⊂ Rn+1 be a pointed closed semi-algebraic convex cone with non-empty interior. Let F0 ⊂ C be an extreme ray of C such that the line [F0] is a general point of PExra(C). Let Z be the irreducible component of PExra(C) with [F0] ∈ Z. Then there is a supporting hyperplane 0 ∈ ∂C∨ exposing F0 and a semi-algebraic neighbourhood U of 0 in ∂C∨ such that every


∈ U supports C in an extreme ray F of C contained in the regular locus of Z, i.e. [F ] ∈ Zreg.

The above notion of general now translates into the projective notion, i.e. the statement is true for points in a dense semi-algebraic subset of the semialgebraic set of extreme rays as a subset of PExra(C) ⊂ Pn.

3. The Algebraic Boundary of Convex Semi-algebraic Sets

In this section, we consider a full-dimensional closed semi-algebraic convex cone C ⊂ Rn+1 which is pointed, i.e. it does not contain a line. The algebraic boundary of C is an algebraic cone. In particular, it is the aﬃne cone over its projectivisation, i.e. ∂aC = P∂aC. The dual convex cone is the set

C∨ = { ∈ (Rn+1)∗: ∀ x ∈ C (x) ≥ 0},

i.e. the set of all half spaces containing C. We write Exra(C) for the Zariski closure of the union of all extreme rays of C in An+1. Again, this is an algebraic

cone. This is the technically more convenient language for the algebraic duality theory. We will deduce the statements for convex bodies by homogenisation.

We now consider projective dual varieties: Given an algebraic variety X ⊂ Pn, the dual variety X∗ ⊂ (Pn)∗ is the Zariski closure of the set of all hyperplanes [H] ∈ (Pn)∗ such that H contains the tangent space to X at some regular point x ∈ Xreg. For computational aspects of projective duality, we refer to Ranestad-Sturmfels [11] and Rostalski-Sturmfels [15].

- Proposition 3.1. The dual variety to the algebraic boundary of C is contained in the Zariski closure of the extreme rays of the dual convex cone, i.e.


(P∂aC)∗ ⊂ PExra(C∨)

- Proof. Let Y ⊂ P∂aC be an irreducible component of the algebraic boundary of C. Let x ∈ Y ∩ ∂C be a general point and H ⊂ Rn+1 be a supporting hyperplane to C at x. We argue similarly to the proof of Proposition 2.12: Since C lies in one half-space deﬁned by H, so does Y locally around x. Therefore,


H is the tangent hyperplane Tx Y . Now the tangent hyperplane to Y at x is unique, because Y has codimension 1. So the set of all supporting hyperplanes to C at x is an extreme ray of the dual convex cone. Since Y ∩ C is Zariski dense in Y , the hyperplanes tangent to Y at points x ∈ Y ∩ C are dense in the dual variety to Y .

- Remark 3.2. Let Z ⊂ Exra(C) be an irreducible component. Then the dual variety to PZ ⊂ Pn is a hypersurface in (Pn)∗, which follows from the biduality theorem in projective algebraic geometry Tevelev [17, Theorem 1.12], because PZ cannot contain a dense subset of projective linear spaces of dimension ≥ 1. Suppose PZ contained a dense subset of projective linear spaces of dimension ≥ 1, then the set Z ∩ Exr(C), which is dense in Z, would contain a Zariski dense subset of an aﬃne linear space of dimension at least 2. This contradicts the fact that the set of extreme rays Exr(C) does not contain any line segments other than those lying on the rays themselves.


In the language of cones, our ﬁrst main theorem is the following.

Theorem 3.3. Let C ⊂ Rn+1 be a pointed closed semi-algebraic convex cone with non-empty interior. The dual variety to the locus of extreme rays of C is contained in the algebraic boundary of the dual convex cone C∨, i.e.

(PExra(C))∗ ⊂ P∂aC∨.

More precisely, the dual variety to every irreducible component of PExra(C) is an irreducible component of P∂aC.

Proof. Let PZ ⊂ PExra(C) be an irreducible component of the locus of extreme rays of C. By Corollary 2.19, a general extreme ray [F0] ∈ PZ ∩ (PExr(C)) is exposed by 0 ∈ ∂C∨ and there is a semi-algebraic neighbourhood U of 0 in ∂C∨ such that every ∈ U exposes an extreme ray F of C such that [F ] ∈ (PZ)reg. The hyperplane Pker( ) is tangent to PZ at [F ] because PZ is locally contained in C; so PU is a semi-algebraic subset of PZ∗ of full dimension and the claim follows.

In the Introduction, we gave an aﬃne version of the preceding theorem that follows from it via homogenisation.

- Corollary 3.4. Let C ⊂ Rn be a compact convex semi-algebraic set with 0 ∈ int(C). Let Z be an irreducible component of the Zariski closure of the set of extreme points of its dual convex body. Then the variety dual to Z is an irreducible component of the algebraic boundary of C. More precisely, the dual variety to the projective closure Z of Z with respect to the embedding An → (Pn)∗, x  → (1 : x) is an irreducible component of the projective closure of ∂aC with respect to An → Pn, x  → (1 : x).


Proof. We homogenise the convex body and its dual convex body by embedding both at height 1 to get convex cones co(C) = {(λ,λx): λ ≥ 0,x ∈ C} ⊂ R×Rn and co(Co) = (co(C))∨ ⊂ R×(Rn)∗. The projective closure Z of the irreducible component Z ⊂ Exa(Co) with respect to the embedding An → (Pn)∗,

- x  → (1 : x) is an irreducible component of PExra(co(C)∨). By the above Theorem 3.3, the dual variety to Z is an irreducible component of P(∂a co(C)), which is the projective closure of an irreducible component of the algebraic boundary of C with respect to the embedding An → Pn, x  → (1 : x).

Corollary 3.5. Let C ⊂ Rn+1 be a pointed closed semi-algebraic convex cone with non-empty interior. We have (P∂aC)∗ = PExra(C∨).

Remark 3.6. It does not follow from the biduality theorems in both theories that (PExra(C∨))∗ = P∂aC simply because the biduality theorem in the algebraic context does not in general apply to this situation, since the varieties in question tend to be reducible. In fact, the mentioned equality does not hold in general, as the following example shows: Let C ⊂ R2 be the convex set deﬁned by the inequalities x2 +y2 −1 ≥ 0 and x ≤ 3/5, see Figure 1. The dual convex body is the convex hull of the set {(x,y) ∈ R2: x2+y2−1 ≥ 0,x ≥ −3/5} and the point (−5/3,0) (it cannot be deﬁned by simultaneous polynomial inequalities, i.e. it is not a basic closed semi-algebraic set). Its algebraic boundary has three components, namely the circle and the two lines y = 3/4x+5/4 and

- y = −3/4x−5/4. The set of extreme points of C is {(x,y): x2+y2−1 = 0,x ≤ 3/5}. So Exa(C) = V(x2+y2−1) and V(x2+y2−1)∗ = V(x2+y2−1) ∂aCo.


| | | |
|---|---|---|
| | | |


Figure 1. A circle cut by a halfspace and its dual convex body.

The following statement gives a complete semi-algebraic characterisation of the irreducible subvarieties Y ⊂ Exra(C) with the property that Y ∗ is an irreducible component of the algebraic boundary of C∨.

Theorem 3.7. Let C ⊂ Rn+1 be a pointed closed semi-algebraic convex cone. Let Z be an irreducible algebraic cone contained in Exra(C) and suppose Z ∩ Exr(C) is Zariski dense in Z. Then the dual variety to PZ is an irreducible component of P∂aC∨ if and only if the dimension of the normal cone to a general point x ∈ Z ∩ Exr(C) is equal to the codimension of Z, i.e.

dim(Z) + dim(NC(R+x)) = n + 1.

Conversely, if Y is an irreducible component of the algebraic boundary of C∨, then the dual variety to PY is an irreducible subvariety of PExra(C), the set (PY )∗∩Exr(C) is Zariski dense in (PY )∗ and the above condition on the normal cone is satisﬁed at a general extreme ray for the aﬃne cone over (PY )∗.

To be clear, the normal cone is NC(R+x) = { ∈ (Rn+1)∗: ∀ y ∈ C \ R+x (y) ≥ (x) = 0}. Proof. Consider the semi-algebraic set Σ ⊂ ∂C × ∂C∨ ⊂ Rn+1 × (Rn+1)∗ deﬁned as

Σ = {(x, ) ∈ Rn+1 × (Rn+1)∗: x ∈ Zreg ∩ Exr(C),  ∈ C∨, (x) = 0}

This is the set of all tuples (x, ), where x spans an extreme ray of C and is a regular point of Z and is a supporting hyperplane to C at x, i.e. the ﬁbre of the projection π1 onto the ﬁrst factor over a point x is the normal cone NC(R+x). Since a supporting hyperplane to C at x is tangent to Z at x, this bihomogeneous semi-algebraic incidence correspondence is naturally contained in the conormal variety CN(PZ) ⊂ Pn × (Pn)∗ of the projectivisation of Z. Now the image π2(Σ) is Zariski dense in PZ∗ if and only if PZ∗ is an irreducible component of the projectivisation of the algebraic boundary of C∨. Indeed, π2(Σ) ⊂ PZ∗ ∩ P∂C∨ and so if it is dense in PZ∗, we immediately get that PZ∗ ⊂ P∂aC∨ is an irreducible component, because PZ∗ is a hypersurface (cf. Remark 3.2(b)). Conversely, we have seen in the proof of the above proposition that if PZ∗ ⊂ P∂aC∨ is an irreducible component, the unique tangent hyperplane to a general point of PZ∗ ∩P∂C∨ spans an extreme ray of C, i.e. a general point of PZ∗ ∩ P∂C∨ is contained in π2(Σ).

This says, that Σ is dense in CN(PZ), i.e. dim(Σ) = dim(CN(PZ))+2 = n+1 if and only if PZ∗ is an irreducible component of P∂aC∨.

On the other hand, counting dimensions of Σ as the sum of the dimensions of Z and the dimension of the ﬁbre over a general point in Zreg ∩ Exr(C), we see that dim(Σ) = n + 1 if and only if the claimed equality of dimensions

dim(Z) + dim(NC(R+x)) = n + 1

holds. The second part of the statement follows from the ﬁrst by Proposition 3.1.

- Remark 3.8. We want to compare this theorem to the result of Ranestad and Sturmfels in [11]: They consider the convex hull of a smooth algebraic variety X ⊂ Pn and make the technical assumption that only ﬁnitely many hyperplanes are tangent to the variety X in inﬁnitely many points, which is needed for a dimension count in the proof. We get rid of this technical assumption in the above theorem. The assumption that the extreme rays are Zariski dense in the variety Z in question, compares best to the RanestadSturmfels assumption. It is semi-algebraic in nature.


The corresponding aﬃne statement to Theorem 3.7 is the following. We take projective closures with respect to the same embeddings as in the aﬃne version Corollary 3.4 of Theorem 3.3 above.

- Corollary 3.9. Let C ⊂ Rn be a compact convex semi-algebraic set with 0 ∈ int(C). Let Z be an irreducible subvariety of Exa(C) and suppose Z ∩ Ex(C) is dense in Z. Then the dual variety to Z is an irreducible component of ∂aCo if and only if


dim(Z) + dim(NC({x})) = n

for a general extreme point x ∈ Z ∩ Ex(C). Conversely, if Y is an irreducible component of ∂aCo, then the dual variety to Y is an irreducible subvariety of Exa(C), the set Y ∗ ∩ Ex(C) is dense in Y ∗ and the condition on the normal cone is satisﬁed at a general extreme point.

Proof. Again, the proof is simply by homogenising as above. Note that the dimension of the normal cone does not change when homogenising.

In the following aﬃne examples we will drop the technical precision of taking projective closures and talk about the dual variety to an aﬃne variety to make

- them more readable.


- Example 3.10. Let C = {x ∈ Rn: g1(x) ≥ 0,...,gr(x) ≥ 0} ⊂ Rn be a basic closed semi-algebraic convex set with non-empty interior deﬁned by g1,...,gr ∈ R[x1,...,xn]. Then the algebraic boundary ∂aC is contained in the variety V(g1) ∪ ... ∪ V(gr) = V(p1) ∪ ...V(ps), where p1,...,ps are the irreducible factors of the polynomials g1,...,gr. The irreducible hypersurface V(pi) is an irreducible component of ∂aC if and only if V(pi) ∩ ∂C is a semialgebraic set of codimension 1. By the above Corollary 3.9, we can equivalently check the following conditions on the dual varieties Xi to the projective closure V(pi):


- ◦ The extreme points of the dual convex set are dense in Xi via Rn → (Pn)∗, x  → (1 : x).
- ◦ A general extreme point of the dual convex set in Xi exposes a face of C of dimension codim(Xi) − 1.


We consider the convex set shown in Figure 2, whose algebraic boundary is the cubic curve X = V(y2 − (x + 1)(x − 1)2), with diﬀerent descriptions as a basic closed semi-algebraic set. The dual convex body is the convex hull of a quartic curve. Its algebraic boundary is

V(4x4 + 32y4 + 13x2y2 − 4x3 + 18xy2 − 27y2) ∪ V(x + 1).

![image 1](<2014-sinn-algebraic-boundaries-convex-semi-algebraic_images/imageFile1.png>)

Figure 2. A basic closed semi-algebraic set in the plane on the left and its dual convex set on the right.

Here, the line V(x + 1) is a bitangent to the quartic and the dual variety of the node (1,0) of the cubic and the quartic is the dual curve to the cubic. We deﬁne C using the cubic inequality and additionally either one linear inequality or the two tangents to the branches of X in (1,0)

C = {(x,y) ∈ R2: y2 − (x + 1)(x − 1)2 ≤ 0,x ≤ 1} = {(x,y) ∈ R2: y2 − (x + 1)(x − 1)2 ≤ 0,y ≥

√

√

2(x − 1),y ≤ −

2(x − 1)},

and we see both conditions in action. First, the dual variety to the aﬃne line x = 1 is (−1,0), which is not an extreme point of Co. The ﬁrst condition mentioned above shows, that the line V(x − 1) corresponding to the second inequality in the ﬁrst description is not an irreducible component of ∂aC. In the second description, the dual variety to the aﬃne line y = √2(x−1) is the point P = (−1, √12), which is an extreme point of Co. The normal cone NCo({P}) is 1-dimensional, because the supporting hyperplane is uniquely determined it is the bitangent V(x + 1) to the quartic. So by the second condition above, the line V(y −

√2(x − 1)) is not an irreducible component of ∂aC.

- Corollary 3.11. [to Corollary 3.9] Let C ⊂ Rn be a compact semi-algebraic set with 0 ∈ int(C). Let Y ⊂ ∂aCo be an irreducible component such that Y ∗ ⊂ Exa(C) is not an irreducible component. If Y ∗ is contained in a bigger irreducible subvariety Z ⊂ Exa(C) such that Z ∩ Ex(C) is dense in Z, then


- ◦ Y ∗ ⊂ Zsing or

- ◦ Y ∗ is contained in the algebraic boundary of the semi-algebraic subset Ex(C) ∩ Z of Z.


- Proof. Let Z ⊂ Exa(C) be an irreducible subvariety. If ∈ (Rn)∗ deﬁnes a supporting hyperplane to an extreme point x ∈ Ex(C) that is an interior point of the semi-algebraic set Ex(C) ∩ Z as a subset of Z and (1 : x) ∈ Zreg,


- then the variety Z lies locally in one of the half spaces deﬁned by (1 : ) and therefore (1 : ) is tangent to Z at (1 : x). In particular, the dimension of the normal cone NC({x}) is bounded by the local codimension of Z at (1 : x).


Now if Y ∗ is strictly contained in Z, it cannot contain (1 : x) by Corollary 3.9 because dim(Y ∗) < dim(Z).

The set Z ∩ Ex(C) in the above corollary does not need to be a regular semi-algebraic set. So the second condition can also occur in the following way.

- Example 3.12. Consider the convex hull C of the half ball {(x,y,z) ∈ R3: x2+y2+z2 ≤ 1,x ≥ 0} and the circle X = {(x,y,z) ∈ R3: x2+y2 ≤ 1,z = 0}. The Zariski closure of the extreme points of C is the sphere S2. Every point of the circle X is a regular point of S2 and X is contained in the algebraic boundary of Ex(C)∩S2 ⊂ S2, because the semi-algebraic set Ex(C)∩S2 does not have local dimension 2 at the extreme points (x,y,0) ∈ X ∩ Ex(C) where x < 0. The algebraic boundary of the dual convex set has three irreducible components, namely the sphere S2 and the dual varieties to the two irreducible components X and V(y2 + z2 − 1,x) of ∂a(Ex(C) ∩ S2) ⊂ S2.


The following examples show how the statement of the corollary can be used

- to determine the algebraic boundary in concrete cases.


- Example 3.13. Consider the spectrahedron P = {(x,y,z) ∈ R3: Q(x,y,z) ≥ 0} where Q is the symmetric matrix


  

  ,

1 x 0 x x 1 y 0 0 y 1 z x 0 z 1

Q =

studied by Rostalski and Sturmfels in [15, Section 1.1] and called pillow. The Zariski closure of the set of extreme points of P is deﬁned by the equation det(Q) = 0, where

det(Q) = x2(y − z)2 − 2x2 − y2 − z2 + 1. The algebraic boundary of the dual convex body Po is the hypersurface ∂aPo = V(b2 + 2bc + c2 − a2b2 − a2c2 − b4 − 2b2c2 − 2bc3 − c4 − 2b3c) ∪

V(2 − a2 + 2ab − b2 + 2bc − c2 − 2ac) ∪ V(2 − a2 − 2ab − b2 + 2bc − c2 + 2ac),

computed in Rostalski-Sturmfels [15, Section 1.1, Equations 1.7 and 1.8]. The ﬁrst quartic is the dual variety to the quartic V(det(Q)). The two quadric hypersurfaces are products of linear forms over R and they are the dual va-

rieties to the four corners of the pillow, namely √12(1,1,−1), √12(−1,−1,1), √12(1,−1,1) and √12(−1,1,−1). These four points are extreme points of P and singular points of V(det(Q)).

Another interesting consequence of Corollary 3.9 concerns the semi-algebraic set Ex(C).

Corollary 3.14. Let C ⊂ Rn be a compact semi-algebraic convex set with 0 ∈ int(C). Every extreme point x of C is a central point of the dual variety of at least one irreducible component of ∂aCo via An → Pn, x  → (1 : x).

A point x on a real algebraic variety X ⊂ Pn is called central if X(R) has full local dimension around x. Equivalently, x ∈ X is central if it is the limit of a sequence regular real points of X, cf. Bochnak-Coste-Roy [3, Section 7.6 and Proposition 10.2.4].

Proof. By Straszewicz’s Theorem [14, Theorem 18.6], it suﬃces to prove, that the statement holds for exposed extreme points because every extreme point is the limit of an exposed one. So let x be an exposed extreme point of C and let Fx = { ∈ Co: (x) = −1} be the dual face. Because x is exposed, the normal cone NCo(Fx) = R+x is 1-dimensional. Fix a relative interior point ∈ Fx. Let Y be an irreducible component of ∂aCo on which is a central point and let ( j)j∈N ⊂ Yreg(R) be a sequence of regular real points converging to in the euclidean topology. There is a unique (up to scaling) linear functional minimising in j over Co, namely yj ∈ ∂C with j(yj) = −1 and αj(yj) = −1 for all α ∈ T

Y . Since (yj) is a sequence in a compact set, there exists a converging subsequence; without loss of generality, we assume that (yj)j∈N converges and we call the limit y. Note that y represents a central point of Y ∗. We know y ∈ ∂C and

j

yk) = −1,

(y) = lim

j(y) = lim

j( lim

j→∞

j→∞

k→∞

so y exposes the face Fx of Co and is therefore equal to x by NCo(Fx) = R+x.

We take a short look at implications of this corollary to hyperbolicity cones.

Example 3.15. A homogeneous polynomial p ∈ R[x0,...,xn] of degree d is called hyperbolic with respect to e ∈ Rn+1 if p(e) = 0 and the univariate polynomial p(te−x) ∈ R[t] has only real roots for every x ∈ Rn+1. We consider the set

Cp(e) = {x ∈ Rn+1: all roots of p(te − x) are non-negative},

which is called the hyperbolicity cone of p (with respect to e). It turns out to be a convex cone, cf. [13]. Assume that all non-zero points in the boundary of Cp(e) are regular points of V(p). Then by Corollary 3.11 the algebraic boundary of the dual convex cone is the dual variety to V(q) where q is the unique irreducible factor of p which vanishes on ∂Cp.

The assumption on the hyperbolicity cone being smooth is essential: Consider the hyperbolicity cone of p = y2z−(x+z)(x−z)2 ∈ R[x,y,z] with respect to (0,0,1). The cubic V(p) ⊂ R3 is singular along the line R(1,0,1) and the algebraic boundary of the dual convex cone has an additional irreducible component, namely the hyperplane dual to this line because the normal cone has dimension 2 at this extreme ray, see Figure 2.

Let now Cp(e) be any hyperbolicity cone and decompose ∂aCp(e) = X1 ∪ ... ∪ Xr into its irreducible components X1,...,Xr. The dual convex cone

Cp(e)∨ is the conic hull of the regular real points of the dual varieties of the irreducible components Xi up to closure, i.e.

Cp(e)∨ = cl(co((X1∗)reg(R) ∪ ... ∪ (Xr∗)reg(R))).

Indeed, the right hand side contains every central point of every variety Xi∗ and by Corollary 3.14, this gives one inclusion. Conversely, let be a general

real point of Xi∗ for any i. Then is tangent to Xi in a regular real point of ∂aCp(e) and by hyperbolicity of p, the linear functional has constant sign on the hyperbolicity cone Cp(e) because every line through the hyperbolicity cone intersects every regular real point of ∂aCp(e) with multiplicity 1, cf. PlaumannVinzant [10, Lemma 2.4].

How can we compute these exceptional varieties of extreme points? Given the algebraic boundary of the dual convex set, the following theorem gives an answer. In its statement, we use an iterated singular locus: The k-th iterated singular locus of a variety X, denoted by Xk,sing, is the singular locus of the (k − 1) iterated singular locus. The 1-st iterated singular locus is the usual singular locus of X.

Theorem 3.16. Let C ⊂ Rn be a compact semi-algebraic convex set with 0 ∈ int(C) and suppose that every point ∈ ∂Co is a regular point on every irreducible component of ∂aC0 containing it. Let Z ⊂ Exa(Co) be an irreducible subvariety such that Z∗ is an irreducible component of ∂aC. If codim(Z) = 1, then Z is an irreducible component of ∂aCo. If codim(Z) = c > 1, then Z is an irreducible component of an iterated singular locus, namely it is an irreducible component of one of the varieties (∂aCo)sing,(∂aCo)2,sing,...,(∂aCo)c−1,sing.

Proof. Assume codim(Z) = c > 1 and let ∈ Z ∩ Ex(Co) be a general point. Since Whitney’s condition a is satisﬁed for (Xreg,Z) at for every irreducible component X ⊂ ∂aCo with Z ⊂ X by Bochnak-Coste-Roy [3, Theorem 9.7.5], every extreme ray R+x of NCo({ }) is tangent to Z at by Corollary 3.14. Since the extreme rays of the normal cone NCo({ }) span the smallest linear space containing it, the dimension of Z is bounded from above by codim(NCo({ })). The assumption that Z∗ is an irreducible component of ∂aC implies dim(Z) = codim(NCo({ })) by Corollary 3.9. It follows that the tangent space T Z is the lineality space of the convex cone NCo({ })∨. To show that Z is an irreducible component of (∂aCo)j,sing, suppose Y ⊂ (∂aCo)k,sing is an irreducible component with Z Y and Yreg ∩Z = ∅ and let ∈ Z ∩Ex(Co) be a general point with ∈ Yreg. Then T Z T Y and there is an extreme ray R+x of NCo( ) with x ∈ Ex(C) and x|T Y = 0. By Corollary 3.14, there is an irreducible component X ⊂ ∂aCo such that x is a central point of X∗. So by assumption, ∈ Xreg and x ∈ (T X)⊥. Since x|T Y = 0, the varieties Y and X intersect transverally at . So Z ⊂ Y ∩X Y and Y ∩X ⊂ (∂aCo)j,sing is an irreducible component for some j > k because the multiplicity of a point in Y ∩ X in ∂aCo is higher than the multiplicity of a general point on Y . Induction on the codimension of Z proofs the theorem.

- Remark 3.17. (a) This theorem gives a computational way to get a list of candidates for the dual varieties to irreducible components of the algebraic boundary of C, given the algebraic boundary of Co. Certain of these candidates may fail to contribute an irreducible component due to semi-algebraic constraints. For illustration, we will apply it to two examples.


(b) The assumption that all irreducible components of ∂aCo are smooth along the boundary of Co is used to show that the stratiﬁcation into iterated singular loci is suﬃcient in this case. In general, it may be necessary to reﬁne this stratiﬁcation such that Whitney’s condition a is satisﬁed for all adjacent strata, see Example 3.20.

- Example 3.18 (cf. Remark 3.6). We consider the convex set C ⊂ R2 in the plane deﬁned by the two inequalities x2+y2 ≤ 1 and x ≤ 3/5, see Figure 1. Its algebraic boundary is the plane curve V((x2+y2−1)(x−3/5)). The dual convex body is the convex hull of the set {(X,Y ) ∈ R2: X2 + Y 2 ≤ 1,X ≥ −3/5}

and the point (−5/3,0). Its algebraic boundary is the curve ∂aCo = V((X2 + Y 2 − 1)(4Y − 3X − 5)(4Y + 3X + 5)). Its three irreducible components are smooth and its singular locus consists of three points, namely (−5/3,0) and (−3/5,±4/5). By the above theorem, a complete list of candidates for the algebraic boundary of C are the dual varieties to the circle V(X2 + Y 2 − 1) and the irreducible components of the ﬁrst iterated singular locus, i.e. the lines dual to the points (−5/3,0) and (−3/5,±4/5). In fact, the last two points do not contribute an irreducible component to ∂aC, because the normal cone to Co at these points is 1-dimensional, cf. Corollary 3.9.

We can also look at it dually and compute the algebraic boundary ∂aCo from the singularities of the algebraic boundary of C: The curve ∂aC is reducible, all components are smooth, and its singular locus consists of two points, namely (3/5,±4/5). Both of these points dualize to irreducible components of ∂aCo.

- Example 3.19. As an example in 3-space, consider the convex set C deﬁned as the intersection of two aﬃnely smooth cylinders given by the inequalities x2 + y2 ≤ 1 and 3y2 + 4z2 − 4y ≤ 4. The algebraic boundary of C is the (reducible) surface V((x2 +y2 −1)(3y2 +4z2 −4y −4)), whose singular locus is a smooth curve of degree 4, namely the intersection of the two cylinders. Since the dual varieties to the cylinders are curves and the iterated singular loci of


∂aC are this smooth curve of degree 4 or empty, the algebraic boundary of the dual convex body is, by Theorem 3.16, the dual variety of this curve, which is

### a surface of degree 8 deﬁned by the polynomial

- −240X8 − 608X6Y 2 − 240X4Y 4 + 384X2Y 6 + 256Y 8 + 840X6Z2

+696X4Y 2Z2 − 192X2Y 4Z2 + 384Y 6Z2 − 1215X4Z4 + 696X2Y 2Z4

- −240Y 4Z4 + 840X2Z6 − 608Y 2Z6 − 240Z8 − 896X6Y − 2304X4Y 3 −1920X2Y 5 − 512Y 7 + 1152X4Y Z2 + 192X2Y 3Z2 + 768Y 5Z2 − 1848X2Y Z4


+2784Y 3Z4 + 1504Y Z6 + 832X6 + 1312X4Y 2 − 160X2Y 4 − 640Y 6 − 984X4Z2 −4144X2Y 2Z2 − 3520Y 4Z2 − 234X2Z4 − 2504Y 2Z4 + 232Z6

+2176X4Y + 3584X2Y 3 + 1408Y 5 + 2048X2Y Z2 + 576Y 3Z2 − 1640Y Z4 −800X4 − 288X2Y 2 + 656Y 4 − 424X2Z2 + 2808Y 2Z2 + 313Z4 − 1664X2Y −1280Y 3 − 128Y Z2 + 64X2 − 416Y 2 − 456Z2 + 384Y + 144.

### Viewed dually, this example is more complicated. The algebraic boundary of Co is the surface of degree 8 deﬁned by the above polynomial, which has singularities along the boundary of Co. So the above theorem is not applicable in this case but the conclusion is still true and we compute the iterated singular loci for demonstration. The singular locus of the surface has 4 irreducible components: the dual varieties to the cylinders, which are circles, namely V(Z,X2 + Y 2 − 1) and V(X,4Y 2 + 4Z2 − 4Y − 3), a complex conjugate pair of quadrics V(2Y 2 − Y + 2,4X2 − 3Z2 − 2Y Z2 + 8Y − 4), and a curve of degree 12, which we denote by X12. The second iterated singular locus, which is the singular locus of the union of these 4 irreducible curves, consists of 24 points. 16 of them are the singular points of X12 and the other 8 points are intersection points of X12 with the complex conjugate pair of quadrics V(2Y 2 − Y + 2,4X2 − 3Z2 − 2Y Z2 + 8Y − 4). The two circles dual to the cylinders intersect the curve X12 only in singular points of the latter. There are no other intersection points of the irreducible components of (∂aCo)sing. Of these 24 points in (∂aCo)2,sing only 4 are real. They are (± 5/9,2/3,0) and (0,−1/6,± 5/9). Now the diﬃcult job is to exclude those varieties that do not contribute irreducible components to the algebraic boundary of C. The dual variety to ∂aCo is only a curve, so it cannot be an irreducible component of ∂aC. Next, we discuss the irreducible components of (∂aCo)sing: The dual varieties to the complex conjugate pair of quadrics cannot be an irreducible component of ∂aC either, because the real points will not be dense in this hypersurface. Why the dual variety to the curve X12 is not an irreducible component of ∂aC is not obvious. Of the irreducible components of (∂aCo)2,sing, the 4 real points must be considered as potential candidates for dual varieties to irreducible components of ∂aC.

### To close, we want to consider an example of a convex set whose algebraic boundary is not smooth along its euclidean boundary and for which the conclusion of the Theorem 3.16 is false. As remarked above, the stratiﬁcation into iterated singular loci must be reﬁned to a stratiﬁcation that is Whitney a-regular.

- Example 3.20. Consider the surface in A3 deﬁned by


- f = (z2 + y2 − (x + 1)(x − 1)2)(y − 5(x − 1))(y + 5(x − 1)),

which is the union of an irreducible cubic and two hyperplanes meeting along the line V(x − 1,y). The cubic surface is a rotation of the nodal curve shown in Figure 2 on the left along the x-axis, so the convex set C bounded by the cubic looks like a teardrop. We consider the extreme point p = (1,0,0) of C: The normal cone is two-dimensional and so the dual hyperplane p⊥ is an irreducible component of the algebraic boundary of Co. Indeed, the point p is a singular point of the cubic that lies on the line V(x − 1,y), which is an irreducible component of the singular locus of the reducible surface V(f), so p cannot be found by computing the iterated singular loci of V(f). We make this discussion relevant by perturbing the above polynomial f in such a way that it becomes irreducible and shows the same behaviour: Consider the polynomial

- g = f +


1 10

(x − 1)yz2,

which is irreducible over Q. The surface V(g) ⊂ A3 is the algebraic boundary of a convex set C , a perturbation of the teardrop C. Convexity of C can be checked by writing z as a function of x and y and checking its convexity resp. concavity using its Hessian matrix (note that z only occurs to the power of 2 in g). The point p is also an extreme point of C and the normal cone at

- p relative to C is still 2-dimensional. Yet the algebraic boundary of C is only singular along the line V(x − 1,y), which is a smooth curve. So we don’t ﬁnd


{p} as an irreducible component of an iterated singular locus of ∂aC = V(g).

Note that Whitney’s condition a for (V(g),V(x − 1,y)) is not satisﬁed at p because a hyperplane that is in limiting position for supporting hyperplanes to the teardrop C do not contain the line V(x − 1,y). Reﬁning the stratiﬁcation of iterated singular loci into a Whitney a-regular stratiﬁcation would detect this special extreme point.

Acknowledgements. This work is part of my PhD thesis. I would like to thank my advisor Claus Scheiderer for his encouragement and support, the Studienstiftung des deutschen Volkes for their ﬁnancial and ideal support of my PhD project, and the National Institute of Mathematical Sciences in Korea, which hosted me when I ﬁnished this paper.

References

- [1] Alexander Barvinok. A course in convexity, volume 54 of Graduate Studies in Mathematics. American Mathematical Society, Providence, RI, 2002.
- [2] Grigoriy Blekherman, Pablo A. Parrilon, and Rekha R. Thomas, editors. Semideﬁnite Optimization and Convex Algebraic Geometry, volume 13 of MOS-SIAM Series on Optimization. 2013.
- [3] Jacek Bochnak, Michel Coste, and Marie-Fran¸coise Roy. Real algebraic geometry, volume 36 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)]. Springer-Verlag, Berlin, 1998. Translated from the 1987 French original, Revised by the authors.
- [4] Jesu´s A. De Loera, Bernd Sturmfels, and Cynthia Vinzant. The central curve in linear programming. Found. Comput. Math., 12(4):509–540, 2012.


- [5] I. M. Gelfand, M. M. Kapranov, and A. V. Zelevinsky. Discriminants, resultants and multidimensional determinants. Modern Birkh¨user Classics. Birkh¨user Boston Inc., Boston, MA, 2008. Reprint of the 1994 edition.
- [6] Jo˜o Gouveia and Tim Netzer. Positive polynomials and projections of spectrahedra. SIAM J. Optim., 21(3):960–976, 2011.
- [7] Joe Harris. Algebraic geometry, volume 133 of Graduate Texts in Mathematics. SpringerVerlag, New York, 1992. A ﬁrst course.
- [8] Tim Netzer, Daniel Plaumann, and Markus Schweighofer. Exposed faces of semideﬁnitely representable sets. SIAM J. Optim., 20(4):1944–1955, 2010.
- [9] Jiawang Nie, Kristian Ranestad, and Bernd Sturmfels. The algebraic degree of semideﬁnite programming. Math. Program., 122(2, Ser. A):379–405, 2010.
- [10] Daniel Plaumann and Cynthia Vinzant. Determinantal representations of hyperbolic plane curves: an elementary approach. J. Symbolic Comput., 57:48–60, 2013.
- [11] Kristian Ranestad and Bernd Sturmfels. The convex hull of a variety. In Petter Branden, Mikael Passare, and Mihai Putinar, editors, Notions of Positivity and the Geometry of Polynomials, Trends in Mathematics, pages 331–344. Springer, Basel, 2011.
- [12] Kristian Ranestad and Bernd Sturmfels. On the convex hull of a space curve. Adv. Geom., 12(1):157–178, 2012.
- [13] James Renegar. Hyperbolic programs, and their derivative relaxations. Found. Comput. Math., 6(1):59–79, 2006.
- [14] R. Tyrrell Rockafellar. Convex analysis. Princeton Mathematical Series, No. 28. Princeton University Press, Princeton, N.J., 1970.
- [15] Philipp Rostalski and Bernd Sturmfels. Dualities in convex algebraic geometry. Rend. Mat. Appl. (7), 30(3-4):285–327, 2010.
- [16] Bernd Sturmfels and Caroline Uhler. Multivariate Gaussian, semideﬁnite matrix completion, and convex algebraic geometry. Ann. Inst. Statist. Math., 62(4):603–638, 2010.
- [17] E. A. Tevelev. Projective duality and homogeneous spaces, volume 133 of Encyclopaedia of Mathematical Sciences. Springer-Verlag, Berlin, 2005. Invariant Theory and Algebraic Transformation Groups, IV.
- [18] Victor Vinnikov. LMI representations of convex semialgebraic sets and determinantal representations of algebraic hypersurfaces: past, present, and future. In Mathematical methods in systems, optimization, and control, volume 222 of Oper. Theory Adv. Appl., pages 325–349. Birkh¨user/Springer Basel AG, Basel, 2012.


Georgia Institute of Technology, Atlanta, USA E-mail address: sinn@math.gatech.edu

