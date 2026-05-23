## arXiv:1401.7029v2[math.MG]28Jan2015

# Iterative Universal Rigidity

##### Robert Connelly and Steven J. Gortler September 11, 2018

###### Abstract

A bar framework determined by a ﬁnite graph G and conﬁguration p = (p1,...,pn) in Rd is universally rigid if it is rigid in any RD ⊃ Rd. We provide a characterization of universally rigidity for any graph G and any conﬁguration p in terms of a sequence of aﬃne subsets of the space of conﬁgurations. This corresponds to a facial reduction process for closed ﬁnite dimensional convex cones.

Keywords: rigidity, prestress stability, universal rigidity, global rigidity, inﬁnitesimal rigidity, super stability, framework, tensegrity, dimensional rigidity, self stress, equilibrium stress, measurement set, generic, semi-deﬁnite programming, positive semi-deﬁnite (PSD) matrices, point location, form ﬁnding

### 1 Introduction

#### 1.1 Basic Deﬁnitions

Given a conﬁguration p = (p1,...,pn) of n points in Rd, and a ﬁnite graph G, without loops or multiple edges, on those n points one can ask the natural and fundamental question: is there another conﬁguration q = (q1,...,qn) in Rd, where the distance between pi and pj, is the same as the distance between qi and qj when {i,j} is an edge of G? When this happens we say that (G,p) is equivalent to (G,q). (Traditionally G(p) and G(q) is the notation used for (G,p) and (G,q), which are called (bar) frameworks, but we break that tradition here.) Of course, if there is a congruence between p and q, they

are called trivially equivalent or congruent, since all pairs of distances are the same.

The following are a sequence of ever stronger rigidity properties of frameworks, where (G,p) is a framework on n vertices in Rd.

- • If all the frameworks (G,q) in Rd equivalent to (G,p) and suﬃciently close to (G,p) are trivially equivalent to (G,p) we say that (G,p) is locally rigid in Rd (or just rigid in Rd).
- • If all the frameworks (G,q) in Rd equivalent to (G,p) are congruent to (G,p) we say that (G,p) is globally rigid in Rd.
- • If all the frameworks (G,q) in any RD ⊃ Rd equivalent to (G,p) are trivially equivalent to (G,p), we say that (G,p) is universally rigid.


#### 1.2 Main Result

It is well known that the existence of a certain kind of “stress” matrix associated with a speciﬁc framework is suﬃcient to prove its universal rigidity [13]. It is also known that when a “generic” framework is universal rigidity, it is also necessary for it to have this type of associated stress matrix [22]. But there do exist special frameworks that are universally rigid while not possessing such a matrix. In this paper, we propose a new criterion in terms of a certain “sequence of stress matrices” which gives a complete (necessary and suﬃcient) characterization of universal rigidity for any speciﬁc framework in any dimension of any graph.

The validity of this certiﬁcate can be checked eﬃciently and deterministically in the real computational mode of [8]. We need to use a real model, since even if p is described using rational numbers, the stress matrix might have irrational entries. As such, this means that universal rigidity is in the class NP under this real computational model. Note that universal rigidity is clearly in CO-NP under real valued computation since the non universal rigidity of a framework p can always be certiﬁed by a providing an equivalent non-congruent framework q.

The main result will be explained in Section 8 and Theorem 8.1. We will derive our results in a self-contained manner, but note that technically, what we have is really a thinly disguised version of a known technique called “facial reduction” which is used to analyze convex cone programs [9]. The connection is explained explicitly in Section 10.

#### 1.3 Relation to other forms of rigidity

Given (G,p), testing for local or global rigidity is known to be a hard computational problem [1, 38]. Fortunately, this is not the end of the story. For local and global rigidity, the problems become much easier if we assume that p is generic. (We say that a conﬁguration p is generic in Rd if all the coordinates of all the points of p are algebraically independent over the rationals. This means, in particular, there can be no symmetries in the conﬁguration, no three points are collinear for d ≥ 2, etc). Local and global rigidity have eﬃcient randomized algorithms under the assumption that the conﬁguration is generic, (and for d = 1 or d = 2, there are even purely combinatorial polynomial-time algorithms). See [14, 15, 21, 46] for information about all of these concepts. In particular, both local and global rigidity in Rd are generic properties of a graph G. That is, either all generic frameworks are rigid, or none of them are, and so these properties only depend on the graph G and not on the conﬁguration p.

One justiﬁcation for assuming that a conﬁguration is generic is that in any region, the generic conﬁgurations form a set of full measure. In other words, if a conﬁguration is chosen from a continuous distribution, with probability one, it will be generic, and with any physical system, there will always be some indeterminacy with respect to the coordinates. But the problem is that special features of a particular conﬁguration, such as symmetry, collinearity, overlapping vertices, etc, may be of interest and they are necessarily non-generic. In this paper we do not want to restrict ourselves to generic frameworks.

In order to test for local rigidity of a speciﬁc non-generic framework there is a natural suﬃcient condition to use, namely inﬁnitesimal rigidity. This says that in Rd (for n ≥ d) the rank of the rigidity matrix R(p) is nd−d(d+1)/2, where R(p) is an m-by-nd (sparse) matrix with integer linear entries, where m is the number of members (another name for the bars) as deﬁned in Section 6. See also [46], for example. Inﬁnitesimal rigidity of (G,p) can can be computed eﬃciently [46].

Inﬁnitesimal rigidity is simply a linearized form of local rigidity and thus is a very natural suﬃcient condition to use for testing the local rigidity of

- (G,p). In fact, the matrix test for inﬁnitesimal rigidity is central to the determination of generic local rigidity for G just described. In contrast, we do not have such a natural suﬃcient condition to use for global rigidity. Indeed, the particular matrix test used to compute generic global rigidity for


the graph G does not give us information about the global rigidity of any speciﬁc framework (G,p) [15].

Thus, in order to test for global rigidity of a speciﬁc non-generic framework, we often resort to “stronger” conditions; perhaps the most usable such suﬃcient condition is, universal rigidity. In this context, one can choose the ambient dimension D to be, say n−1 with no loss in generality. As such, understanding universal rigidity can be essential to determining global rigidity, and it is the focus of this paper.

- 1.4 Complexity Issues The theoretical complexity of testing universal rigidity for (G,p), (even when


- p is given by integer-valued input) is technically unknown. There are no known hardness results, nor are there any provably correct eﬃcient algorithms. One can pose the problem of universal rigidity in the language of semi-deﬁnite programing (SDP) [49]. Unfortunately, the complexity for for conclusively deciding an SDP feasibility problem is itself unknown [35].


In practice, one can use a numerical (say interior point) SDP solver for these problems. Roughly speaking, this can eﬃciently ﬁnd a framework with an aﬃne span of dimension n − 1 (the highest possible dimension) that is within of being equivalent to the given framework. If this framework appears to “almost” have an aﬃne span of dimension d, and appears to be “very close” to the input p, then we have strong “evidence” for universal rigidity. But it is unclear how to use this to make a determination with provable correctness properties. In eﬀect, this means, in the case with imprecise input, that the problem to determine whether the framework is universally rigid cannot be solved because there is not enough information in the input to be able to solve it.

An exasperating issue is that there can be great sensitivity between errors in achieving desired edge lengths (which are what we get when using an SDP solver) and errors in the resulting conﬁguration. Figure 1.1 shows a framework (with pinned vertices) that is universally rigid in R2. We will see that this can be veriﬁed using methods described in this paper. If the lengths in Figure 1.1 are all increased by less that 0.5%, Figure 1.2 shows the resulting realization in the plane. Note that this slightly perturbed framework is far from universally rigid. Here we see that a very small error in the numerical calculation of the lengths of the members can lead to a very large perturbation of the resulting conﬁguration, and, indeed, the decision as to universal rigidity

m EF = 6.67 cm

Figure 1.1: The large black vertices are pinned to the plane, and the whole framework is universally rigid as in Corollary 8.1.2.

m AB = 3.35 cm

m AC = 6.70 cm

###### A C B

Figure 1.2: This is the same framework as in Figure 1.1 but with the lengths of the bars increased by less than 0.5%.

may be incorrect.

#### 1.5 Certiﬁcates

The lack of conclusive algorithms for universal rigidity brings us, ﬁnally, to the topic of “suﬃcient certiﬁcates” for universal rigidity. In this paper we show that there is a kind of suﬃcient certiﬁcate that must exist for any universally rigid framework. This certiﬁcate is described by a sequence of real-valued matrices and can be veriﬁed eﬃciently using real computation.

Note, that we do not claim that given a universally rigid framework, this certiﬁcate can always be found eﬃciently. But, as we describe below in Section 15, there are many cases where we can systematically ﬁnd the appropriate certiﬁcates for the universal rigidity of (G,p). We also discuss other cases where we have at least a positive probability of ﬁnding the certiﬁcate.

Looking again at the situation of Figure 1.1 and Figure 1.2, we see that universal rigidity itself can be a fragile property, that is destroyed (along with its suﬃcient certiﬁcates) by any errors in the description of p. Given our new characterization of universal rigidity, we suggest that when exploring and designing frameworks that we wish to be universally rigid, it may be best to explicitly maintain the appropriate certiﬁcates as part of the representation and description of (G,p).

### 2 Stress

The central tool we will use to analyze universal rigidity is the concept of a stress.

- Deﬁnition 2.1 A stress associated to a graph G is a scalar ωij = ωji assigned to each edge {i,j} of G. Call the vector ω = (...,ωij,...), the stress vector.

We can suppress the role of G here by simply requiring that ωij = 0 for any non-edge {i,j} of G. (One should also be careful not to confuse the notion of stress here with that used in structure analysis, in physics or in engineering. There, stress is deﬁned as a force per cross-sectional area. In the set-up here, there are no cross-sections; the scalar ωij is better interpreted as a force per unit length.)

Since we will be concerned with conﬁgurations in an arbitrarily high dimension, we will ﬁx a large dimension D, which can eﬀectively be taken to be n if our framework has n vertices. When we are given a particular conﬁguration, we generally will assume it is realized in RD. We can describe a conﬁguration p in RD using coordinates using a single vector in RDn. Of course, for the purposes of deciding universal rigidity and some of the other concepts deﬁned here, there is no reason to restrict the conﬁgurations to lie some particular Euclidean space RD. But it is clear that once the ambient dimension D is greater than n, any conﬁguration in any higher dimension is congruent to one in RD, and it will be convenient to consider conﬁgurations in dimensions larger than n. In order to deﬁne a ﬁnite dimensional space of conﬁgurations appropriate for universal rigidity, though, it is useful to restrict just to those conﬁgurations in RD, and if a construction pops out of RD, we can always rotate it back in to RD.

Given a stress, we can measure the energy of a conﬁguration: Let ω = (...,ωij,...) be a stress for a graph G and let p = (p1,...,pn) be a conﬁguration in RD.

- Deﬁnition 2.2 We deﬁne the stress-energy associated to ω as


Eω(p) :=

ωij(pi − pj)2, (2.1)

i<j

where the product of vectors is the ordinary dot product, and the square of a vector is the square of its Euclidean length.

###### Regarding the stress ω as ﬁxed constants, Eω is a quadratic form deﬁned on vectors in RDn, it is easy to calculate that the conﬁguration p is a critical point for Eω when, for each vertex i of G,

j

ωij(pj − pi) = 0. (2.2)

- Deﬁnition 2.3 When Equation (2.2) holds, we say that the stress ω is an equilibrium stress for the conﬁguration p. We also say that p is in equilibrium with respect to ω.

It is useful to represent a stress in matrix form: The n-by-n stress matrix Ω associated to the stress ω is deﬁned by making the {i,j} entry of Ω be −ωij when i = j, and the diagonal entries of Ω are such that the row and column sums of Ω are zero.

It is easy to see that with respect to the standard basis of RDn, the matrix of Eω is Ω⊗ID, where ID is the D-by-D identity matrix and ⊗ is the matrix Kronecker product. Note that although Eω is deﬁned over the high dimensional space RnD, its being PSD only depends only on Ω, and its rank only depends on the rank of Ω and D.

If p is a conﬁguration in Rd with an equilibrium stress ω, it is easy to check that for any aﬃne map of a : Rd → RD, the conﬁguration a(p) deﬁned by pi → a(pi), for all i, is also an equilibrium conﬁguration with respect to ω.

- Deﬁnition 2.4 We say that a conﬁguration p is universal with respect to the stress ω if p is in equilibrium with respect to ω, and any other conﬁguration q in RD which is, also, in equilibrium with respect to ω, is such that

q is an aﬃne image of p.

- Deﬁnition 2.5 For a conﬁguration p = (p1,...,pn) we regard each pi as a column vector in RD, as we deﬁne the D-by-n conﬁguration matrix of p as


P = p1 p2 ... pn .

Then it is easy to check that the equilibrium condition for a given stress is

P Ω = 0, where Ω is the stress matrix for the stress ω.

The following is easy to check and is in [13]. See also Lemma 7.1 for a general universal construction.

- Proposition 2.1 Given a stress ω, let p be any conﬁguration that is in equilibrium with respect to ω and whose aﬃne span is of maximal dimension over all such conﬁgurations. Let this aﬃne span have dimension d. Then p is universal with respect to ω and the rank of Ω is n − d − 1.

3 The conic at inﬁnity

In a sense, an equilibrium stress can only make distinctions “up to aﬃne motions” as seen in Proposition 2.1. For rigidity questions, we would like to know when the aﬃne motions can be restricted to Euclidean congruences.

- Deﬁnition 3.1 We say that v = {v1,...,vm}, a ﬁnite collection of nonzero vectors in Rd, lie on a conic at inﬁnity if when regarded as points in real projective (d − 1) space RPd−1, they lie on a conic.

This means that there is a non-zero d-by-d symmetric matrix A such that

for all i = 1,...,m, vitAvi = 0, where ()t is the transpose operation. The following shows how aﬃne motions can be non-trivial ﬂexes of a framework.

- Deﬁnition 3.2 A ﬂex of a framework (G,p) is a continuous motion p(s),


- 0 ≤ s ≤ 1,p(0) = p, where p(s) is equivalent to p. It is non-trivial if p(s) is not congruent to p for all s > 0. If p(s) = A(s)p(0), where A(s) is an aﬃne function of Euclidean space, then we say p(s) is an aﬃne ﬂex.


- Proposition 3.1 A framework (G,p) in Rd, with d-dimensional aﬃne span, has a non-trivial aﬃne ﬂex if and only if it has an equivalent non-congruent


aﬃne image in Rd if and only if the member directions {pi −pj}{i,j}∈E(G) lie on a conic at inﬁnity, where E(G) are the edges of G.

See [13, 10] for a simple proof of this property. Note that in the plane, the conic lies in RP1, which consists of two points or one point. So aﬃne motions of a framework can only occur when the edge directions lie in two possible directions.

### 4 The fundamental theorem

The major tool used for proving universal rigidity is the following. (See [13].)

###### Theorem 4.1 Let (G,p) be a framework whose aﬃne span of p is all of Rd, with an equilibrium stress ω and stress matrix Ω. Suppose further

- 1. Ω is positive semi-deﬁnite (PSD).
- 2. The conﬁguration p is universal with respect to the stress ω. (In other words, the rank of Ω is n − d − 1.)
- 3. The member directions of (G,p) do not lie on a conic at inﬁnity. Then (G,p) is universally rigid.


The idea is that Eω(p) only depends on the edge lengths of p, and so any conﬁguration q equivalent to q must have zero energy. Since Eω is PSD, this forces such a q to have coordinates in the kernel of Ω and thus q to be an aﬃne image of p. Thus by Proposition 3.1, their member directions must lie on a conic at inﬁnity. So Condition 3 implies that (G,p) is universally rigid.

- Deﬁnition 4.1 If all three conditions of Theorem 4.1 are met we say that the framework (G,p) is super stable.

There are many instances of such frameworks. For example, the rigid tensegrities of [12] are super stable in R3, where the number of edges of G is

- m = 2n, and n is the number of vertices. Theorem 4.1 is the starting point for most of our results in this paper, where this result will be generalized signiﬁcantly.


Given such a matrix Ω and (G,p) as real valued input, one can eﬃciently verify (under, say a real-model of computation) that Ω is PSD and that it is an equilibrium stress matrix for (G,p).

We note, in passing, the following result in [3] which replaces the conic condition with a more natural one.

- Deﬁnition 4.2 A conﬁguration p = (p1,...,pn) in Rd is in general position if no k points lie in a (k − 1)-dimensional aﬃne space for 1 ≤ k ≤ d.


###### Theorem 4.2 If Conditions 1 and 2 hold in Theorem 4.1 and Condition 3 is replaced by the assumption that the conﬁguration p is in general position, then Condition 3 still holds and (G,p) is super stable.

This natural question is whether the conditions of Theorem 4.1 are necessary for universal rigidity. The answer in the generic case is in the aﬃrmative. The following is from [22]:

- Theorem 4.3 A universally rigid framework (G,p), with p generic in Ed and having n ≥ d+2 vertices, has a PSD equilibrium stress matrix with rank


- n − d − 1.


This result does not hold for non-generic frameworks (even in general position). For example, see the universally rigid framework in Figure 4.1. In this paper, we will describe a (weaker) suﬃcient condition that is also necessary for universal rigidity for all frameworks.

###### A

Figure 4.1: This is a framework, where the vertices are all in general position, there is only a one-dimensional space of equilibrium stresses, and the associated stress matrix does not have maximal rank. The stresses on the members at the vertex A must be all zero. The dotted lines extending the members coming from the vertices of the outside triangle meet at a point and are not part of the framework, as shown. As described in this paper, we will use multiple levels of stresses. In this ﬁgure and later ones, the ﬁrst level stresses and the corresponding members are colored in dark blue, the next level in red and the third level in green.

### 5 Dimensional rigidity

In [4] a notion called dimensional rigidity is introduced. This is closely related to, but distinct from, universal rigidity. Our main result can be best

understood in terms of dimensional rigidity, ﬁrst. Then we can derive the appropriate statements about universal rigidity.

- Deﬁnition 5.1 We say that a framework (G,p) in Rd, with aﬃne span of dimension d, is dimensionally rigid in Rd if every framework (G,q) equivalent to (G,p) has an aﬃne span of dimension no greater than d.


(One might better call this concept dimensionally maximal, since a dimensionally rigid framework may not even be locally rigid, but we refrain from that indulgence.)

In many applications, one often wants to ﬁnd the minimum dimension for a graph (G,e) with given edge lengths e = {...,eij,...}, so the concept of the maximal dimension seems backwards from what is normally desired. For example, ﬁnding the minimal dimension of (G,e) is the point of [6, 29]. Nevertheless, dimensional rigidity is quite relevant for universal rigidity.

It is clear that if a framework (G,p) is universally rigid in Rd, then it is dimensionally rigid in Rd, but we shall see several examples of non-rigid dimensionally rigid frameworks. Such cases always occur due to a conic at inﬁnity, (in which case, the framework is not even locally rigid). For example, two bars, with a single vertex in common, is dimensionally rigid in the plane, but it is ﬂexible, i.e. not rigid, in the plane.

An important connection between dimensional rigidity and universal rigidity is the following. (This is proved in [4], but we provide a more direct proof here.)

- Theorem 5.1 If a framework (G,p) with n vertices in Rd is dimensionally rigid in Rd, and (G,q) is equivalent to (G,p), then q is an aﬃne image of p.


Proof. Suppose that h : p → q is the correspondence between the conﬁgurations. Consider the graph of this correspondence Γ(h) = {(pi,qi)}i=1,...,n ⊂ Rd × RD, where D is suﬃciently large to contain q. It is easy to check (See [7] or the proof of Lemma 7.1 below) that √12Γ(h) is equivalent to p and q. Thus there is a d-dimensional aﬃne hyperplane that contains √12Γ(h). This implies that q is an aﬃne image of p.

A key consequence of Theorem 5.1 shows that universal rigidity can be determined from dimensional rigidity and Property 3.) of Theorem 4.1.

Corollary 5.1.1 A framework (G,p) with n vertices in Rd is universally rigid if and only if it is dimensionally rigid and the edge directions do not lie on a conic at inﬁnity.

One result that follows from the proof of Theorem 4.1 from [13] is the following.

- Theorem 5.2 If a framework (G,p) with n vertices in Rd has an equilibrium stress with a PSD stress matrix of rank n−d−1, then (G,p) is dimensionally rigid in Rd.

See [4] for similar conditions for dimensional rigidity. This just says that the conﬁguration p is universal with respect to the given stress. The only other possible equivalent conﬁgurations of (G,p), in this case, are aﬃne linear images, which do not raise dimension.

Since universal rigidity implies dimensional rigidity, the examples of Figures 11.1 (on the right) and 4.1 also show that the PSD stress matrix of rank n − d − 1 is not necessary for dimensional rigidity.

In order to start to understand what is necessary for dimensional (and universal) rigidity we begin with the following, Theorem 6 in [2]. We also provide a simple proof as a special case of the results is Section 7 here.

- Theorem 5.3 If (G,p) is a dimensionally rigid framework with n vertices whose aﬃne span is d dimensional, d ≤ n − 2, then it has a non-zero equilibrium stress with a PSD stress matrix Ω.


Note that the rank of Ω in Theorem 5.3 could be as low as one. As such, it is weaker than the suﬃcient conditions above. Later, we will describe a new condition, which is stronger than having a non-zero PSD stress matrix, but weaker than having a non-zero PSD stress matrix of rank n−d−1. Our condition instead will be of the form of a sequence of PSD matrices, where the combined rank is n−d−1. Brieﬂy, we will apply Theorem 5.3 repeatedly to a smaller and smaller space of possible conﬁgurations.

### 6 The measurement set

Fix a ﬁnite graph G with n vertices, m edges and ﬁx a Euclidean space RD, where the dimension D is at least as large as n. Let

C := {p | p = (p1,...,pn) is a conﬁguration in RD}

be the set of conﬁgurations in RD. Each conﬁguration can be regarded as a vector in RDn.

- Deﬁnition 6.1 We deﬁne the rigidity map as f : C = RnD → M ⊂ Rm


by f(p) = (...,(pi − pj)2,...), where the {i,j} are the corresponding edges in G, and M = M(G) is the image of f in Rm for the graph G, which we call the measurement set.

In other words, M is the set of squared lengths of edges of a framework that are actually achievable in some Euclidean space. There are some basic properties of C and any aﬃne set A as below.

- 1. M is a closed convex cone in Rm.
- 2. For any e ∈ M, f−1(e) consists of an equivalence class of frameworks p ∈ C.


The convexity of Condition 1 is well-known and even has an explicit formula for the convexity in [7] and follows from Lemma 7.1 in Section 7. Condition 2 follows directly from the deﬁnition.

- Deﬁnition 6.2 The rigidity matrix is deﬁned as R(p) = 12dfp, with respect to the standard basis in Euclidean space, and f(p) = R(p)p, where df is the diﬀerential of f. Then the energy function associated to a stress ω can also be written as

Eω(p) = ωR(p)p, where ω is regarded as a row vector.

7 Aﬃne sets

- Deﬁnition 7.1 A subset A ⊂ C that is the ﬁnite intersection of sets of the form


{p ∈ C |

λij(pi − pj) = 0}, (7.1)

ij

for some set {...,λij,...} of constants, is called an aﬃne set.

Clearly an aﬃne set is a linear subspace of the conﬁguration space C and it is closed under arbitrary aﬃne transformations acting on RD. Moreover, any such set can be deﬁned by equations of the form (7.1).

For example, if there are three collinear points p1,p2,p3, and p2 is the midpoint of p1 and p3, then {p ∈ C | (p1 − p2) − (p3 − p2) = 0} is an aﬃne set. Or {p ∈ C | p1 − p2 + p3 − p4 = 0}, which is a conﬁguration of four points of a parallelogram (possibly degenerate), is another example.

A special case of such an aﬃne set is determined by a stress ω, where the equilibrium condition (2.2) at each vertex supplies the condition (7.1).

In Deﬁnition 2.4 we deﬁned what it means for a conﬁguration p to be universal with respect to a single stress ω. This just means that any other

- conﬁguration q that is in equilibrium with respect to ω is an aﬃne image of p. We generalize this the case to that of any aﬃne set as follows.


- Deﬁnition 7.2 We say that a conﬁguration p in an aﬃne set A is universal with respect to A, if any other conﬁguration q in A is an aﬃne image of p. We denote by A˚ ⊂ A, the set of conﬁgurations that are universal with respect to A.


For any set X in a linear space, X denotes the aﬃne linear span of X.

- Lemma 7.1 A conﬁguration p ∈ C is universal with respect to an aﬃne set A if and only if it has maximal dimensional aﬃne span for conﬁgurations in


- A. Let f : A → Rm be the restriction of the rigidity map to the measurement space for some graph G. Then f(A) is convex and f(A˚) is the relative interior of f(A) ⊂ f(A) .


Proof. Clearly any possible universal conﬁguration must have maximal aﬃne span in order for it to map aﬃne linearly onto any other conﬁguration in A. Conversely, let p be any conﬁguration with maximal dimensional aﬃne span, say d, in A, and let q be any other conﬁguration in A. Deﬁne p˜ to be another conﬁguration where p˜i = (pi,qi) ∈ RD × RD for i = 1,...,n. The conﬁguration p˜ is also in A since all its coordinates satisfy the equations (7.1). Since projection is an aﬃne linear map and the aﬃne span of p is maximal, namely d, the dimension of the aﬃne span of p˜ must also be d, and the projection between their spans must be an isomorphism. So the map

- p → p˜ → q provides the required aﬃne map since projection onto the other coordinates is an aﬃne map as well.


If p,q ∈ A, then, regarding p and q as being in complementary spaces, f((cosθ)p,(sinθ)q) = (cosθ)2f(p) + (sinθ)2f(q), (7.2)

for 0 ≤ θ ≤ π/2 is the segment connecting f(p) to f(q) is in f(A) showing that f(A) and f(A˚) are convex.

The rank of dfp is constant for non-singular aﬃne images of p (see [18], for example), which are in A˚, the universal conﬁgurations. This implies that f is locally a projection into f(A) at p, which implies that f(A˚) is open in f(A) . This, combined with its being dense in f(A), and its convexity makes f(A˚) equal to the relative interior of f(A).

The dimension of an aﬃne set A is dim(A) = D(d + 1), where D is the dimension of the ambient space and d is the dimension of the aﬃne span of a universal conﬁguration p for A.

For any (symmetric) bilinear form B for a vector space V , the radical of

- B is the set {v | B(v,w) = 0 for all w ∈ V }. If V is a ﬁnite dimensional vector space and B is given by a symmetric matrix, then the radical of B is the kernel (or co-kernel) of that matrix. We can interpret the stress-energy


Eω as such a bilinear form. If B acting on V is PSD, then its zero set must be equal to its radical.

- Lemma 7.2 Let q ∈ A ⊂ RnD. Then f(q) is in the boundary of the relative interior of f(A) ⊂ f(A) if and only if there is a non-zero stress ω for


- (G,q) such that when Eω is restricted to A, the resulting form is PSD and has f(q) in its radical.


Note that this does NOT mean that the Eω is necessarily PSD over all of C or that the conﬁguration q is in the radical of the form Eω deﬁned over all of C.

Proof. Suppose that a stress ω = 0 exists for the framework (G,q). The condition that Eω is PSD on A is equivalent to Eω(q) ≥ 0 for all q in A, which is equivalent to the linear inequality ωf(q) ≥ 0 for any f(q) ∈ f(A), and any conﬁguration q in A. When Eω(q) = 0, then f(q) is in the closure of the complement of that inequality in f(A) and thus in the boundary of f(A) ⊂ f(A) .

Conversely, suppose that f(q) is in the boundary of f(A) ⊂ f(A) . Since the set f(A) is convex, f(q) is in a supporting hyperplane

H = {e ∈ f(A) | ωe = 0},

which is deﬁned by a non-zero stress ω. Then

0 ≤

- 1

- 2


ωf(q) = ωR(q)q =

ωij(qi − qj)2 = qtΩ ⊗ IDq = Eω(q).

i<j

Thus the quadratic form deﬁned by Eω restricted to the aﬃne set A, is PSD and has f(q) in its radical.

- Lemma 7.3 Let A be an aﬃne set and Eω be a stress energy which we restrict to A. Then its radical must be an aﬃne set.


Proof. Let q be universal for A. Then a conﬁguration p ∈ A is in the radical when

ωij(pi − pj) · (q˜i − q˜j) = 0,

i<j

for any q˜ that is an aﬃne image of q. Suppose some p is in the radical. Then clearly so is any translation of

- p. Any linear transform applied to the coordinates of p can be deﬁned using the above equation by applying its inverse transpose to q. Thus the radical is invariant for aﬃne transforms, making it an aﬃne set.

8 Iterated aﬃne sets and the main theorem

- Deﬁnition 8.1 If C = A0 ⊃ A1 ⊃ A2 ⊃ ...Ak is a sequence of aﬃne sets, we call it an iterated aﬃne set.
- Deﬁnition 8.2 Suppose an iterated aﬃne set has a corresponding sequence of stress energy functions E1,...,Ek as deﬁned of the form (2.1) such that each Ei is restricted to act only on Ai−1. Suppose that each restricted Ei is PSD (over Ai−1), that Ei(q) = 0 for all q ∈ Ai, and that Ei(q) > 0 for all


- q ∈ Ai−1 − Ai. Then we call E1,...,Ek an (associated) iterated PSD stress for this iterated aﬃne set.


Our main result is the following characterization of dimensional rigidity.

Theorem 8.1 Let (G,p) be a framework in Rd, where p has an aﬃne span of dimension d. Suppose C = A0 ⊃ A1 ⊃ A2 ⊃ ...Ak is an iterated aﬃne

set with p ∈ Ak and with an associated iterated PSD stress. If the dimension of Ak is (d + 1)D. Then (G,p) is dimensionally rigid in Rd.

Conversely, if (G,p) is dimensionally rigid in Rd, then there must be an iterated aﬃne set with p ∈ Ak, Dim(Ak) = (d + 1)D, with an associated iterated PSD stress.

Proof. First we prove the easy direction. Since Ei operates on the squared edge lengths, the energy function forces any equivalent framework (G,q) to be in Ai and ultimately in Ak. Since the dimension of Ak is (d + 1)D, p must be universal for Ak, and so q must be an aﬃne image of p and thus has, at most, a d-dimensional aﬃne span.

For the converse, suppose that (G,p) is dimensionally rigid in Rd. The conﬁguration p is such that p ∈ C = A0. If f(p) is in the boundary of f(A0) we apply Lemma 7.2 to ﬁnd a stress ω1 and a corresponding stress-energy function E1 whose radical includes p, and by Lemma 7.3 is an aﬃne set A1 In order to iterate the process we deﬁne

Ai = {q ∈ Ai−1 | ωiR(q)q = 0}, (8.1)

where ωi = 0 is chosen such that ωiR(q)q = ωif(q) ≥ 0, for all q ∈ Ai−1, ωiR(q)q = ωif(q) > 0 for some q ∈ Ai−1, and ωiR(p)p = ωif(p) = 0. The quadratic form qtΩi ⊗ IDq is PSD when restricted to Ai−1, and from Lemma 7.3, the resulting Ai must also be an aﬃne set. When such an ωi = 0 cannot be found, we stop and that is the end of the sequence of aﬃne sets. This sequence must terminate as each of our subsequent aﬃne sets is of strictly lower dimension.

From Lemma 7.2 we see that we can continue creating stresses ω1,...,ωk and aﬃne sets until f(p) is in the relative interior of f(Ak), and is universal with respect to Ak by Lemma 7.1. If the dimension of Ak is not D(d + 1), then the dimension of Ak is strictly greater than D(d+1) and the dimension of the aﬃne span of p would have been greater than D(d+1), a contradiction.

Figure 8.1, similar to Figure 2 of [22], shows a symbolic version of this process in the measurement set, where the indicated point represents the image of the conﬁguration and its relation to the measurement cone. The arrows represent the stress vectors.

f(A )2 f(A )1

ω2 1

ω

Figure 8.1: The sets f(A1) and f(A2) shown as the point and line segment.

#### 8.1 The basis matrix

An aﬃne set A can always be represented by a universal conﬁguration b = (b1 ...bn) of n points in RD, with an aﬃne span of some dimension, say d. Without loss of generality, we can assume (using a translation if needed) that the linear span of the bi (thought of as vectors) is of dimension d + 1.

- Deﬁnition 8.3 We deﬁne a basis matrix B, for an aﬃne set as a rank d+1 matrix with n columns and D rows given by the coordinates of b.

Since this matrix has rank d + 1, we can then apply row reduction operations so that B has only d + 1 rows. Additionally, (if we want) since the aﬃne span of b is only d dimensional, we can perform these operations so that the ﬁnal row is the all-ones vector.

- Deﬁnition 8.4 Given an iterated aﬃne set, C = A0 ⊃ A1 ⊃ A2 ⊃ ...Ak. We deﬁne di to be the dimension of the aﬃne span of a universal conﬁguration for Ai.
- Deﬁnition 8.5 Given an iterated PSD equilibrium stress for an iterated aﬃne set, a basis matrix Bi−1 for each Ai−1, and the n-by-n stress matrix Ωi corresponding to each Ei, we deﬁne a restricted stress matrix Ω∗i := Bi−1ΩiBit−1. Each Ω∗i is a (di−1 + 1)-by-(di−1 + 1) PSD matrix.


The following is a Corollary of Theorem 8.1.

- Corollary 8.1.1 Let (G,p) be a framework in Rd with an aﬃne span of dimension d. Suppose C = A0 ⊃ A1 ⊃ A2 ⊃ ...Ak is an iterated aﬃne set with p ∈ Ak, and that this iterated aﬃne set has an associated iterated PSD stress, described by restricted stress matrices Ω∗i. Let ri be the rank of Ω∗i. If

k

i=1

ri = n − d − 1. (8.2)

then (G,p) is dimensionally rigid. Conversely, if (G,p) is dimensionally rigid in Rd, then there must be an iterated aﬃne set with p ∈ Ak, with an associated iterated PSD stress such that Equation (8.2) holds.

The two versions of this theorem are related as follows: the zero set of conﬁgurations for the energy function Ei corresponds via the change of basis Bi−1, to the kernel of the matrix Ω∗i. Since the rank of Ω∗i is ri, its kernel has dimension di−1 + 1 − ri = di + 1. Thus dk + 1 = n − ii=1 ri = (d + 1). So Ak, which has dimension (dk +1)D, is the set of all aﬃne images of p in RD.

Figure 15.1, described later, is an example of an application of Theorem 8.1. The set of conﬁgurations of all the points, where for a pole, one is at the midpoint between the other two, is an aﬃne set. The stress is indicated. Each of the restricted stress matrices has rank one. The horizontal members also have a stress that is in equilibrium when restricted to the intersection of the ﬁrst two aﬃne sets. This matrix also has rank one. Thus all the stress matrices can be assumed to be (and are) PSD. But n = 6,d = 2, so d+1+ ii=1 ri = 3+3 = 6 = n, and this (G,p) is dimensionally rigid in R2. This framework has a ﬂex in the plane that is an aﬃne motion, but the point is that it cannot be twisted into a 3-dimensional shape. The calculations are done in Subsection 15.1.

One application of Theorem 8.1 is to universal rigidity.

- Corollary 8.1.2 Suppose C = A0 ⊃ A1 ⊃ A2 ⊃ ...Ak is an iterated aﬃne set for a framework (G,p) with n vertices in Rd. Suppose that the iterated


aﬃne set has an associated iterated PSD stress. If dim(Ak) = D(d + 1) and the member directions do not lie on a conic at inﬁnity, then (G,p) is universally rigid.

Conversely if (G,p) is universally rigid in Rd, then there is such an iterated aﬃne set with an iterated PSD stress, and the member directions do not lie on a conic at inﬁnity.

For example, if another bar is inserted between any of two of the vertices that do not already have a bar in Figure 15.1, the resulting framework will be universally rigid.

### 9 Convexity interpretation

We now point out the connection of the results here from the point of view of basic convexity considerations.

- Deﬁnition 9.1 For any ﬁnite dimensional convex set X and any point x in X, let F(x), called the face of x, be the largest convex subset of X containing x in its relative interior. Equivalently [23], F(x) is the set of points z ∈ X so that there is a z ∈ X with x in the relative interior of the segment [z ,z].


- Deﬁnition 9.2 A subset X0 ⊂ X is called a face of X if X0 = F(x) for some x ∈ X.
- Deﬁnition 9.3 Let X = X0 ⊃ X1 ⊃ X2 ⊃ ...Xk be a sequence of faces of X, which we call a face ﬂag. If each Xi = Hi ∩ Xi−1, where Hi ⊂ Xi−1 is a support hyperplane for Xi−1 ⊂ Xi−1 for i = 1,...,k, then we call the face ﬂag supported. The following is an easy consequence of these deﬁnitions.

- Lemma 9.1 A subset Y of X is a face of X if and only if Y = Xk, for some supported ﬂag face.

We next specialize to the case when the space X = M, the measurement space for the graph G deﬁned in Section 6. The function f is the rigidity map as before.

- Lemma 9.2 A supporting hyperplane H ⊂ Rm for M corresponds to a nonzero PSD stress ω for the graph G. A hyperplane H supports a convex subcone of Xi ⊂ M if and only if there is a quadratic energy form Eω which is PSD on f−1(Xi) and Eω(p) = 0 for some p ∈ f−1(Xi).


- Deﬁnition 9.4 If p ∈ C is a conﬁguration, deﬁne A(p) to be the set of all aﬃne images of p. As before, we call any q of maximal dimensional aﬃne span in A(p) a universal conﬁguration for A(p). Deﬁne A˚(p) to be the set of universal conﬁgurations of A(p).


- Lemma 9.3 Suppose (G,p) is dimensionally rigid. Then f−1(F(f(p))) ⊂ A(p).

Thus additionally, we have

F(f(p)) ⊂ f(A(p)).

Proof. Suppose not. Then there is a conﬁguration q  ∈ A(p)) but such that f(q) ∈ F(f(p)). Since f(p) is in the interior of the face, and f(q) is in the face, then, from the deﬁnition of a face, there must be some third conﬁguration r, such that f(p) is in the relative interior of the segment [f(q), f(r)]. As in the proof of Lemma 7.1, we can use 2 complementary spaces, and ﬁnd appropriate scalars α and β such that p˜ := (αq,βr) is equivalent to p. But since q is not an aﬃne image of p, then neither is p˜. This, together with Theorem 5.1, contradicts our assumption that p was dimensionally rigid.

- Lemma 9.4 Suppose (G,p) is dimensionally rigid. Then F(f(p)) ⊃ f(A(p)).


Thus additionally, we have

f−1(F(f(p))) ⊃ A(p).

Proof. From Lemma 7.1, we know that f(A(p)) is convex with f(p) in its relative interior. Thus from the deﬁnition of a face, we have F(f(p))) ⊃ f(A(p)).

Corollary 9.4.1 If (G,p) is dimensionally rigid and the conﬁguration q is a non-singular aﬃne image of p, then (G,q) is dimensionally rigid as well.

Proof. Since q ∈ A(p), then from the above lemmas, we have f−1(f(q)) ∈ A(p). But q is universal for A(p) and so A(p) = A(q), thus making q dimensionally rigid.

With the above two Lemmas in mind, we make the following deﬁnition:

- Deﬁnition 9.5 We say that the aﬃne set A is a G-aﬃne set if A is equal to the pre-image of some face of the measurement set.


Proposition 9.1 A framework (G,p) is dimensionally rigid if and only if A(p) is a G-aﬃne set.

Proof. Suppose that (G,p) is dimensionally rigid. Then from Lemmas 9.3 and 9.4, we know f−1(F(f(p))) = A(p), which is thus a G-aﬃne set.

For the other direction, let F be any face of M containing f(p). Then F(f(p)) ⊂ F . If (G,p) is not dimensionally rigid, then there is conﬁguration

- q  ∈ A(p) such that such that f(q) = f(p). Thus f−1(F(p)) is not a subset of A(p), and f−1(F ) is not a subset of A(p). So A(p) is not a G-aﬃne set.


In summary this says that the face lattice of the measurement set M exactly corresponds the lattice of G-aﬃne sets. Theorem 8.1 follows directly. The sequence of faces in a face ﬂag of M corresponds to an iterated sequence of G-aﬃne sets Ai cut out by an appropriate stress sequence Ei.

### 10 Relation to Facial Reduction

Facial reduction is a general technique used in the study of duality in cone programming [9, 35, 34], and here we describe the translation between that and our exposition here. In the general setup, one might have a cone programming problem where the feasible set is expressed as points x ∈ RN that are both in some convex cone K ⊂ RN and satisfy an equality constraint, expressed as x ∈ L + b, where L is a linear subpace of RN and b ∈ RN. Let x0 be in the relative interior of the feasible set and let Fmin := F(x0) be its face in K.

In the process of facial reduction, we start with F0 := K and ﬁnd a supporting hyperplane Ω⊥1 whose intersection with F0 is some subface F1 of F0 such that F1 ⊃ Fmin. This can be iterated on any Fi−1 by ﬁnding a hyperplane Ω⊥i that supports Fi−1 and whose intersection with Fi−1 is some subface Fi such that Fi ⊃ Fmin. In each step, we guarantee that we are not excluding any part of Fmin by ensuring that Ωi ∈ (L⊥ ∩ b⊥). This process is iterated until Fi = Fmin.

In the setting of graph embedding, we can think of K as S+n, the cone of n-by-n symmetric PSD matrices. Any conﬁguration p can be mapped to its Gram matrix in K. Each aﬃne set A corresponds to some face of S+n. (Note that not every face F of S+n corresponds to an aﬃne set. The face F must include the all-ones matrix so that its corresponding conﬁguration set is closed under translations in RD).

The linear constraint x ∈ L+b corresponds to a framework being equivalent to (G,p). (The graph G determines the space L and the edge lengths in p gives us a b). The constraint Ωi ∈ L⊥ means that Ωi is a stress matrix for G (zero on non edges, and rows summing to zero). The constraint Ωi ∈ b⊥ means that any p and any equivalent conﬁguration has zero energy under the quadratic form deﬁned by Ωi. The constraint that Ωi supports Fi−1 corresponds to Ωi being PSD over a corresponding aﬃne set Ai.

Under this correspondence, one can see that our process of ﬁnding iterated aﬃne sets Ai using iterated stress matrices Ωi corresponds exactly to an application of facial reduction.

We note, that in our exposition, we do not describe the process using S+n at all. On the one hand, we describe the aﬃne sets Ai as subsets of conﬁguration space (instead of as faces of S+n). On the other hand, instead of picturing of our stresses Ωi as support planes for S+n we work over the measurement set of our graph M(G) := S+n/L, which is a linear projection of S+n. In this projected picture, our support planes are orthogonal to the stress vectors ωi in Rm.

As described in Section 9, facial reduction “upstairs” on the cone K (such

as S+n) for the constraint x ∈ L+b is exactly mirrored by the facial reduction “downstairs” on the cone K/L (such as M) for the constraint x = b/L.

### 11 Tensegrities

It is also possible to use the ideas here to get a similar complete characterization of universal rigidity for tensegrity frameworks, where there are upper and lower bounds (cables and struts) on the member lengths corresponding to the sign of the rigidifying stresses.

- Deﬁnition 11.1 Each edge of a graph G is designated as either a cable, which is constrained to not get longer in length, or a strut, which is constrained not to get shorter in length, or a bar, which, as before, is constrained to stay the same length. So when we have a framework (G,p), where each edge, which we call a member, is so designated, we call it a tensegrity framework, or simply a tensegrity, and we call G a tensegrity graph.


We can then ask whether (G,p) is locally rigid, globally rigid, or universally rigid. For local rigidity and the corresponding concept of inﬁnitesimal rigidity, there is an extensive theory as one can see in [16, 10, 37, 48, 40, 36,

18], for example. For global rigidity and universal rigidity, there is a natural emphasis on stress matrices and related ideas.

- Deﬁnition 11.2 We say that a stress ω = (...,ωij,...) for a tensegrity graph is a proper stress if ωij ≥ 0, when the member {i,j} is cable, and ωij ≤ 0, when the member {i,j} is a strut. There is no condition for a bar.


Theorem 4.1 takes on the following form for tensegrities. See [13].

- Theorem 11.1 Let (G,p) be a tensegrity framework whose aﬃne span of p is all of Rd, with a proper equilibrium stress ω and stress matrix Ω. Suppose further

- 1. Ω is PSD.
- 2. The conﬁguration p is universal with respect to the stress ω. (In other words, the rank of Ω is n − d − 1.)
- 3. The member directions of (G,p) with a non-zero stress, and bars, do not lie on a conic at inﬁnity.


Then (G,p) is universally rigid.

When we draw a tensegrity, cables are designated by dashed line segments, struts by solid line segments, and bars by thicker line segments, as in

- Figure 11.1.


12 Iterated stresses for tensegrities

For the case of tensegrities, the iterated case is similar.

Deﬁnition 12.1 We say that a tensegrity (G,p) in Rd is dimensionally rigid, if any other conﬁguration q in any RD, satisfying the member constraints of G has an aﬃne span of dimension d of less.

- Theorem 12.1 Let (G,p) be a tensegrity in Rd, where p has an aﬃne span of dimension d. Suppose C = A0 ⊃ A1 ⊃ A2 ⊃ ...Ak is an iterated aﬃne set with p ∈ Ak with an associated iterated proper PSD stress. If the dimension of Ak is (d + 1)D, then p is dimensionally rigid in Rd.


Conversely, if (G,p) is dimensionally rigid in Rd, then there must be an iterated aﬃne set with p ∈ Ak, Dim(Ak) = (d + 1)D, with an associated iterated proper PSD stress.

Figure 11.1: These are three examples of super stable tensegrities. The one on the left is trivially universally rigid when all the members are bars. But as a tensegrity it is also super stable, which follows from its rank one equilibrium stress matrix. The tensegrity in the middle is an example of a Cauchy polygon, one of the class of convex polygonal tensegrity polygons as deﬁned in [13]. The one on the right has a degree three vertex attached by bars to another super stable planar tensegrity in R3. The bars must have zero stress, but in order to insure that there is no aﬃne motion, the bar directions must be included in the directions that are to avoid the conic at inﬁnity.

Proof. The proof of this is essentially the same as in Section 8 for Theorem 8.1. For the necessity direction, we just need to be careful to maintain the proper signs for a tensegrity stress. When a tensegrity is dimensionally rigid, this means that not only is f(p) on the boundary of M, but that P, the polyhedral cone of tensegrity constraints of Deﬁnition 11.2 (the squared lengths e2ij ≤ (pi − pj)2, for each cable, and e2ij ≥ (pi − pj)2, for each strut), is disjoint from M, except for f(A(p)). By a standard separation theorem, we can choose a hyperplane that separates the relative interiors of the two convex sets P and M. (See Figure 12.1 in the next section.) This means that the corresponding stress will be a proper stress for the tensegrity. It may be the case, that this hyperplane contains other points of the boundary of P besides just f(p), which means that some of the edges of G will have zero stress components. This argument can be applied at each level of iteration.

Note once an edge has a non-zero stress component at some level, this strictness can be maintained at any subsequent level. In particular, the stress

- ωi is orthogonal to the conﬁgurations in f(Aj), thus we can always replace
- ωj, for j > i, with ωi + ωj. So once a member gets stressed, it can remain stressed from then on.


###### p ω1

Figure 12.1: This shows a section of a cone as in Figure 8.1, but with the rectangular cone given by the cable and strut constraints. The stress vectors ω1 determine the rectangular cone since it is proper.

The major application of this result is the following.

Corollary 12.1.1 Suppose C = A0 ⊃ A1 ⊃ A2 ⊃ ...Ak is an iterated aﬃne set for a tensegrity (G,p) with n vertices in Rd, with an associated iterated

proper PSD stress described by PSD restricted stress matrices Ω∗i. Let ri be the rank of Ω∗i. If (8.2) holds, and the member directions with non-zero stress directions and bars do not lie on a conic at inﬁnity, then (G,p) is universally rigid.

Conversely if (G,p) is universally rigid in Rd, then there is an iterated aﬃne set with an associated iterated PSD stress determined by proper stresses, the dimension of Ak is (d + 1)D, and the members with non-zero stress directions and bars do not lie on a conic at inﬁnity.

Proof. This proof also follows that of the case of a bar framework. The only thing new that we need to establish in the necessity direction is that we will be able to ﬁnd non-zero stress values on the cable and strut edges to certify that they do not lie on a conic at inﬁnity. The iterated stresses that are guaranteed from the above theorem need not be non-zero on any particular set of edges (See the example of Figure 12.2 below).

To establish this we can use, if needed, one extra stress beyond that needed to establish dimensional rigidity. Suppose at the last level of iteration, we have a sequence of stresses that restricts us to frameworks in the aﬃne set Ak, such that p is universal for Ak. In this case, we have that f(p) is in the relative interior of f(Ak). The assumption of universal rigidity means that the polyhedral cone P is disjoint from f(Ak), except for the shared point f(p). Since f(p) is in the relative interior of f(Ak), this means that we can

###### ﬁnd a hyperplane that includes f(Ak) and excludes all of P except for the single point f(p). The corresponding stress must have zero energy for all of Ak and will have non-zero values on all of the edges.

- -1 1
- -1


1 2

2

2

-2

-1 -1

2

2

Figure 12.2: These are two universally rigid tensegrities in the plane. The signs on the members not on the pole can be reversed and it still remains universally rigid.

Figure 12.2 is an example where one extra iteration is needed for universal rigidity after the iteration process shows dimensional rigidity. There is just one pole, in the plane, and just one vertex attached to all three vertices. There are two ways (as shown) to assign cables and struts to the remaining three members so that there will be an equilibrium at that vertex. Both possibilities provide a universally rigid tensegrity. At the ﬁrst level, we can ﬁnd a rank 1 stress on the vertical pole. This is suﬃcient to serve as a certiﬁcate for dimensional rigidity. For a bar framework, universal rigidity follows since the edge directions do not lie at a conic at inﬁnity. But for a tensgrity framework, we are not done, since in that case, the conic test only can use cable and strut edges with non-zero stress coeﬃcients. As shown in

- Figure 12.2, for this we can use a second level stress that has a constant 0 energy over A1.


### 13 Projective invariance

It is well known that a bar framework (G,p) is inﬁnitesimally rigid if and only if (G,q) is inﬁnitesimally rigid, where the conﬁguration q is a non-singular projective image of the conﬁguration p. See [18, 44, 45] for a discussion of this property. Inﬁnitesimal rigidity for tensegrities is also projectively invariant, but a cable that “crosses” the hyperplane at inﬁnity is changed to a strut and vice-versa, because the sign of the stress changes. It is also true

that any equilibrium stress is also altered by the projective transformation. Indeed a stress matrix Ω is replaced by another stress matrix DΩD, where the matrix D is a non-singular diagonal matrix and comes from the nonsingular projective transformation. This transformation preserves the rank and PSD nature of the stress. At any subsequent level, we also can set Ωi := DΩiD using the same D matrix. The basis matrix, which derives from the kernel is transformed as Bi → BiD−1. Thus, the restricted stress matrix, Ω∗i := BiD−1(DΩiD)D−1Bit is not changed at all due the projective transform, thus maintaining its rank and PSD nature. See [19], Proposition 7, for this same idea applied to a bar framework. Thus we get the following result.

- Theorem 13.1 Let f : Rd − X → Rd be non-singular projective transformation, where X is a (d−1)-dimensional aﬃne subspace of Rd, and suppose


that for each i, pi ∈/ X. Then for any tensegrity framework, (G,p) is dimensionally rigid if and only if (G,f(p)) is dimensionally rigid, where the strut/cable designation for {i,j} changes only when the line segment [pi,pj] intersects X and bars go to bars.

It is not always true that the universal rigidity of a bar framework is projectively invariant. For example, the orchard ladder, narrower at the top than at the bottom, as in Figure 13.1, is universally rigid, whereas the straight ladder of Figure 15.1 below, a projective image, is ﬂexible in the plane.

Figure 13.1: This is an example of a universally rigid framework, but the framework of Figure 15.1 below is a projective image that is not universally rigid. The two poles on the sides are collinear triangles.

### 14 Calculation methods

We test for dimensional rigidity of (G,p) by ﬁnding the maximal dimension of any framework (G,q) that is equivalent to p. This is done by building up a maximal iterated aﬃne set with an associated iterated PSD stress as guaranteed by Corollary 8.1.1. To do this calculation, we always maintain a basis matrix Bi, where at the start, B0 = I.

Given Bi−1 we perform the following steps.

Find the next stress: Look for a matrix Ωi such that the restricted stress matrix, Ω∗i := Bi−1ΩiBit−1, is non zero, PSD and such that the “energy” linear constraint pt(Ωi ⊗ ID)p = 0 holds. If there is no such solution we are done with the iteration.

- Deﬁnition 14.1 Given an aﬃne set Ai−1 described by a basis matrix Bi−1. We say that a restricted stress matrix Ω∗i = Bi−1ΩiBit−1, is a restricted equilibrium stress matrix for p if PΩiBit−1 = 0 holds for Ωi.


For any stress matrix Ωi that satisﬁes the energy constraint and such that the restricted stress matrix, Ω∗i, is PSD, we also see that Ω∗i must be a restricted equilibrium matrix for p. Since we want to get the most milage out of our linear constraints, we replace the the energy constraint with this constraint, which we call a restricted energy constraint.

The resulting problem can be posed as an SDP feasibility problem. If possible we would like to avoid using an SDP solver, since that is not only expensive, but, as a numerical algorithm, only approaches, and never exactly hits, a feasible solution. We discuss this issue more below in Section 16.

Sometimes, we can avoid calling an SDP solver by simply looking at the problem and guessing the correct Ωi. For example, if we see, within some two-dimensional framework, a degenerate triangle, (which we will call a pole), it is self evident how to stress that subgraph.

Another easy case arises when the is when the space of solutions for Ω∗i is only one dimensional. In this case, there is no need to search for PSD solutions, one only needs to pick one solution Ω∗i and check its eigenvalues. If it is postive semi-deﬁnite, then we have succeeded. If it is negative semideﬁnite, then we can negate the matrix, and we have succeeded. If it is indeﬁnite, then there is no such solution and we are done with the iteration.

An even easier sub-case of this is when the space of Ω∗i is not only onedimensional, but also that the maximal rank of these matrices is 1. Then we know immediately that Ω∗i is semi-deﬁnite.

Update the basis: Given Bi−1 and a stress Ωi we need to update the basis. We do this by ﬁnding a maximal set of linearly independent row vectors of length n that is in the row span of Bi−1, and such that each of these vectors is in the co-kernel of ΩiBit−1.

These vectors form the rows of our new basis, Bi. We then continue the iteration.

When the iteration is done: We simply count the number of rows of the ﬁnal Bk, which we call dk + 1. If dk equals d, the dimension of the aﬃne span of p, then we have produced a certiﬁcate that p is dimensionally rigid. Otherwise, we have found a higher dimensional aﬃne set that includes frameworks equivalent to p and we have a certiﬁcate that p is not dimensionally rigid.

### 15 Examples

#### 15.1 The ladder

1

2 3

2

2

-2

-1 5 6

-1

2

2

1 4

1

Figure 15.1: This shows a framework with two collinear triangles, each of which provides an aﬃne relation on the space of conﬁgurations of the framework (G,p). The stresses are indicated and the member connecting the external vertices of poles is indicated by a curved arc. This framework is dimensionally rigid in the plane, but it is not universally rigid, since it has an aﬃne ﬂex in the plane, and since there are only two member directions. The vertices are labeled in bold.

We ﬁrst show the process described in Section 8.1 and Section 14 applied to the example in Figure 15.1. The ﬁrst level stress matrix, using just the stresses on the vertical members of the ladder, is the following:





1 1 0 0 −2 0 1 1 0 0 −2 0 0 0 1 1 0 −2 0 0 1 1 0 −2

Ω1 =

.

 

 

−2 −2 0 0 4 0 0 0 −2 −2 0 4

This matrix has rank r1 = 2, a 4-dimensional kernel, and d = 2. The kernel of this matrix deﬁnes the aﬃne set A1. A basis matrix for A1 is

  

  .

1 0 0 0 1/2 0 0 1 0 0 1/2 0 0 0 1 0 0 1/2 0 0 0 1 0 1/2

B1 =

At the second level, we enforce the restricted equilibrium constraint and ﬁnd that the possible candidates for Ω∗2 must be up to scale, equal to

  

  

1 −1 1 −1 −1 1 −1 1

B1Ω2B1t = Ω∗2 =

1 −1 1 −1 −1 1 −1 1

These are rank 1 with positive trace and thus positive semi-deﬁnite. This Ω∗2 has an assocated second level stress Ω2 where ω14 = ω23 = 1 and ω56 = −2 as in Figure 15.1. We have rankΩ1 + rankΩ∗2 = 3 = n − d − 1, making the ladder dimensionally rigid.

#### 15.2 The 4-pole Example

Consider the conﬁguration shown in Figure 15.2 with four vertical parallel line segments, the poles, where each pole is connected to the other three by horizontal members.

The poles are labeled A,B,C,D, and the vertices are simply labeled by their number, 1,...,12. The horizontal spacing between the AB,BC, and CD poles is equal. The vertical spacing of the horizontal members is such

2

1

2 2

4 4

- 5 8

- 2 11

6 9

- 3 12




-1,-1

6

6

-1,-1

-2

-2,4 -2,4

2

2

3

3

A B C D

1

1 4 7 10

1

First Stage Example

Figure 15.2: This is a framework that is dimensionally rigid in the plane. Each set of three (nearly) vertical line segments are considered to be a collinear triangle, while the other horizontal members are connected as shown. This involves at least three levels of iteration as described Section 8, where the levels, in order, are dark blue, red, green.

that the distance between the 2−11 line and the 1−7 line is twice the distance between the 2 − 11 line and the 3 − 5 line. The 5 vertex is the midpoint of the B pole, and the 8 vertex is the midpoint of the C pole. The stresses on this framework are as indicated. These are simply arranged so that the lever arm moments are all 0. The question is whether the appropriate stress matrices are PSD of the right rank.

The stress for each pole is rank one and they can all be combined to one rank 4 stress, which can be considered as a stress at the ﬁrst level. It is simply the certiﬁcate, in any equivalent framework, that each pole remains straight maintaining the ratio of each of the lengths. The stress for each of those members is proportional to the reciprocal of its length in absolute value. The stress for the longest member of each collinear triangle is negative, while the other two are positive.

One can then choose a basis for A1 and search for the restricted equilibrium matrices as in Section 14. It turns out that, as in the ladder example, the space of a possible equilibrium Ω∗2 is only one-dimensional, and these have

rank 4. We check and ﬁnd that these matrices are semi-deﬁnite. An associated Ω2 is shown in red in Figure 15.2. We then choose a basis for A2 and use the methods of Section 14 one ﬁnal time. Again, we ﬁnd a one-dimensional space of equilibrium matrices Ω∗3, and these have rank 1. An associated Ω3 can be constructed with ω1,3 = ω10,12 = 4 and ω4,6 = ω7,9 = −1.

The sum of the ranks is 4 + 4 + 1 = 9 = 12 − (2 + 1) = n − (d + 1), so this framework is dimensionally rigid in the plane. It is not universally rigid since the original framework has only two member directions.

One interesting feature of this example is that the stress Ω2 involves all of the vertices of the graph G from the second level, and yet it still needs another level for the complete analysis of its dimensional rigidity.

The ﬁrst stage in this example involves only the four collinear triangles, which imply the corresponding aﬃne constraints on the the conﬁguration. Suppose one initially starts with those four aﬃne constraints and then proceeds with the analysis, where the distance constraints on the poles is dropped? It turns out that the conﬁguration is not dimensionally rigid in the plane, since at the third level the member constraints in the poles are needed again. The maximal dimensional realization, in that case, is R3.

#### 15.3 The 4-pole Extended Example

- Deﬁnition 15.1 A spider web is a tensegrity, where some subset of the vertices are ﬁxed, and all the members are cables.


For a spider web, it was shown in [13] that it is locally rigid if and only if it is universally rigid, and that when it is universally rigid the iterated construction simpliﬁes to a sequence of proper subgraphs, where the number of vertices decreases at each stage as in Figure 1.1. Another example of the iteration process is shown in Figure 4.1, where the vertex A is added at the second stage. In each of those examples, there is a proper subgraph that is universally rigid on its own without using the presence of the other vertices.

Figure 15.3 shows that, in general, when the framework is universally rigid in more than one step of the iteration, there may be no proper subframework that is universally rigid on its own. The stresses at each level are shown.

This is a perturbed version of Figure 15.2, and it turns out to be universally rigid by the process described here, but using only two stages instead of three as in Subsection 15.2. Since the stressed members have more than

2

4

4

8 8

-2, -1

-2, -1

8

8

-3/2

-8/3, 4 4

4

-8/3, 4

4

4

1

1

Figure 15.3: This is an example of a universally rigid tensegrity framework in the plane that has only one stress that is PSD of rank 8, one less than the maximal possible n − d − 1 = 12 − 2 − 1 = 9. There is a stress at the second stage which is PSD of rank one in the aﬃne set deﬁned by the stress at the ﬁrst stage. The vertices of this conﬁguration are the same as those in Figure 15.2, except the interior point of each pole has been moved half the distance (left or right as indicated) between adjacent poles.

two directions in the plane, and since it is dimensionally rigid in the plane as with Figure 15.2, it is universally rigid.

In both of these cases, we were able to ﬁnd the certifying sequence of stresses without calling a PSD solver. This was because, at each step, there was only a one-dimensional space of restricted equilibrium matrices Ω∗ as candidates. Since they were rank 1, we automatically knew that they were semi-deﬁnite, and for the second step, for the 4 poles, we just checked that it was of rank 4.

More generally, if we end up with a higher dimensional space of equilibrium Ω∗ as candidates, we might have a harder time determining if that space includes a positive semi-deﬁnite one. We discuss this more below in Section 16.

#### 15.4 A hidden stress

One of the problems with SDP is ﬁnding even one PSD equilibrium stress (or more generally restricted equilibrium stresses at later stages). The following example is a framework, where the dimension of PSD equilibrium stresses is a low dimensional subcone of the space of all equilibrium stresses.

Figure 15.4: This is an example of a universally rigid bar framework in the plane that has a three-dimensional space of equilibrium stresses but only a one-dimensional space that is PSD.

The two triangles and the members joining corresponding vertices constitute a super stable PSD subframework as in Figure 4.1. Since the whole (bar) framework is inﬁnitesimally rigid in the plane, and that there are 18 members and 9 vertices, the dimension of the stress space is 18−2·9+3 = 3. Equilibrium at each blue vertex implies that the three stresses at a blue vertex must all have the the same sign. But any equilibrium stress, non-zero on any of the members adjacent to the blue vertices, cannot be all have the same sign for all the members adjacent to all the blue vertices. This is because the twisting inﬁnitesimal motion of the inner triangle relative to the outer triangle either decreases all the members adjacent to the blue vertices or increases them all. So one of the set of three members adjacent to a blue vertex has to have all negative stresses. This stress cannot be PSD since by moving that single blue vertex the stress energy must decrease.

### 16 Computational matters

An important property of universal rigidity is that often it can be calculated eﬃciently using various SDP algorithms. For example, see [5, 47, 34, 41, 28, 9, 35] for information on this vast subject including facial reduction. In particular, if one is given the edge lengths e for a graph G, one can use SDP to ﬁnd a conﬁguration p whose edge lengths approximate e. More precisely, an -approximate conﬁguration p can be found, in some unconstrained dimension D if it exists, in time polynomial in log(1/ ), where n is the number of vertices of G, and m is the number of members of G, as described in [47]. So this can be used to attempt to see if the existence problem is feasible and to attempt to ﬁnd a satisfying conﬁguration when it is feasible.

But, as mentioned in Section 1, one problem is that even though the member lengths of the approximation are close to the given lengths, the conﬁguration may be quite a distance from one implied by the actual constraints. Small errors in the edge lengths can imply large errors in the proposed conﬁguration as in the framework in Figure 1.1, but see [26]. In principle, one could use the calculation as evidence that a given conﬁguration is universally rigid in R2, but Figure 1.2 shows that it may appear that (G,p) has equivalent conﬁgurations in R3 or higher, even with > 0 is very small.

In contrast to this “primal appoach”, we have shown in this paper that when a framework is dimensionally or universally rigid, there must exist a certiﬁcate, in the form of an iterated PSD stress, that conclusively proves the dimensional or universal rigidity of the framework.

Although ﬁnding these stresses also involves solving an SDP problem, in many cases, though we can hope to exactly solve this “dual” SDP. At any level of the analysis here, there is a linear space of restricted equilibrium stress matrices Ω∗i as described in Section 14. If there is such a PSD matrix of maximal rank among all such Ω∗i, then the PSD restricted equilibrium stresses includes an open subset of the space of all restricted equilibrium stresses. In this case, it reasonable to expect that we can exactly ﬁnd such a solution. Thus, even if the numerical solution from an SDP solver is, say, PSD but not quite in restricted equilibrium, a suﬃciently close restricted equilibrium stress will still be PSD and of maximum rank.

In fact this “maximal rank case” must always occur in the last step of our iterated process so, for example, if the framework (G,p) is super stable (in other words, there is only one step in the iterated process described here), then the PSD solutions are full dimensional within the linear space of

equilibrium stress matrices. This is the situation if p is generic in Rd, and the framework (G,p) is universally rigid, since this must be super stable by Theorem 4.3. The two examples on the left in Figure 11.1 have that property.

In other cases, though we may not be able to exactly solve this “dual” SDP, the example of Figure 15.4 shows a case where the PSD equilibrium stresses are all of lower rank than the indeﬁnite equilibrium stresses, and thus do NOT form an open subset of the space of equilibrium stresses. If the dimension of PSD matrices is lower than the dimension of all the equilibrium matrices, then we may have to resort to using the SDP to “suggest” what an actual PSD matrix is (since it will only converge to a PSD matrix in the limit).

More generally, when the conﬁguration is not generic, you have to ask: how is the conﬁguration even deﬁned? It is possible to create conﬁgurations precisely so that they become universally rigid. For example, the symmetric tensegrities of many artists are created in such a way that they become super stable, but not at all generic, not even inﬁnitesimally rigid, even though they are super stable. Indeed, they often have certain symmetries that can be used to simplify the calculations and create tensegrities that are super stable. The representation theory of some small ﬁnite groups can be exploited to create these conﬁgurations. A brief explanation is in [11]. This is called form ﬁnding in the Engineering literature, as in [30, 39].

Stresses and iterated stresses might also be useful during the process of calculating a realization p from an input graph G and input set of edge lengths e. Note though, when we are just given input lengths and are searching for an appropriate Ω, we do not have enough information to express the (restricted) equilibrium linear constraint and can only use the “energy linear constraint”: 0 = i<j e2ijωij. Therefore, we do not expect to be in a “maximal rank” setting. Once we have computed the iterated stresses, then we just need to look for p within the ﬁnal aﬃne set. As described in the appendix in [20], when p is universally rigid, this calculation of p within its aﬃne set can be done easily by solving a certain small linear system. (In the case that p is not universally rigid but is only dimensionally rigid, then that linear system will be singular. Still, since we have restricted ourselves to the correct aﬃne set, we only need to solve small SDP problem, which must be applied over the space of (d + 1)-by-(d + 1) matrices).

In addition to the example in [11], a graph coloring problem can be solved using this idea as in [33].

### 17 Extensions

In general, we propose the following procedure for determining/creating universally rigid frameworks and tensegrities. First a (tensegrity) graph G, and a corresponding conﬁguration p, is deﬁned. A priori, a sequence of aﬃne sets in conﬁguration space can be given as well, as in Section 8. These sets may or may not be a consequence of the geometry of the conﬁguration p. Then at each stage, one either calculates a PSD stress for the given conﬁguration or one assumes that there is a corresponding aﬃne constraint. If the constraints are consistent, then one has a proof that the conﬁguration is dimensionally rigid or universally rigid, depending on the stressed member directions. For example, if there appears to be a (proper) PSD stress for a given aﬃne set, one can assume that it exists and proceed, getting further aﬃne sets. It would depend on the circumstance as to whether the particular aﬃne constraint is reasonable or not. For example, in Figure 1.1, one might suspect that the eight subdivided vertical members are straight, but initially not the others. Only then might one suspect that the four smaller horizontal members are straight, etc. After this is ﬁnished one can conclude that the whole framework is universally rigid.

The idea of assigning nested aﬃne constraints is a generalization of the idea of a body-and-bar framework as deﬁned by Tay and Whiteley in [43, 42]. The concept of nested aﬃne sets, introduced here, is closely related to the concepts of hypergraphs of points and aﬃne rigidity introduced in [20]. Also, a recent result in [17] shows that body-and-bar frameworks are generically globally rigid in Rd if they are generically redundantly rigid in Rd.

Deﬁnition 17.1 Redundant rigidity means that the framework is locally rigid, and remains so after the removal of any member.

It is also true [17] that such body-and-bar graphs always have a generic conﬁguration that is universally rigid in Rd as well.

### 18 Possible future directions and questions

It is also possible to use stresses to estimate the possible perturbations of a given tensegrity or framework. The sign of a PSD stress associated to each member corresponds to an inequality constraint. If all of those constraints are such that at least one of the constraints is violated, we know that the

edge length perturbed conﬁguration cannot be achieved. This imposes somewhat weak, but useful, conditions on which sets of members can increase or decrease in length. If there are more PSD stresses on the members, there will be more of these sign constraints that can be calculated even if the tensegrity framework is not rigid.

One could use universal rigidity properties to understand ﬂexible structures by adding members providing parameters for controlling the motion of a ﬂexible framework. For a ﬁxed length of such additional members, the conﬁguration could be determined. As that length varies the whole conﬁguration could ﬂex in a controlled way.

For the case of generic global rigidity, the notion of globally linked pairs of vertices is discussed in [25, 24]. This means that although the whole framework may not be globally rigid, some pairs of vertices would be forced to have a ﬁxed length for all equivalent conﬁgurations in the same dimension. A similar question in the universally rigid category involving conﬁgurations in higher dimensions that satisfy the tensegrity inequality constraints would be interesting to explore.

Even to determine whether a framework is universally rigid on the line is interesting. In [27] it is determined when a rigid one-dimensional complete bipartite bar-and-joint framework in the line is universally rigid, as well as several open questions in this direction. We have a forthcoming paper that extends this result, and determines when any complete bipartite framework in any dimension is universally rigid.

The weavings of [44, 45, 32, 31] concern lines in the plane that may or may not arise from projections of conﬁgurations of lines in a higher dimension. Particularly, there is a relation to stresses of dual conﬁgurations in [44, 45]. Can there be a connection to the poles in universal rigidity?

### 19 Acknowledgement

We would like to thank Dylan Thurston for countless helpful conversations on convexity.

### References

- [1] Timothy Good Abbott. Generalizations of Kempe’s universality theorem. Masters dissertation, Massachusetts Institute of Technology, 2008.
- [2] A. Y. Alfakih. On bar frameworks, stress matrices and semideﬁnite programming. Math. Program., 129(1, Ser. B):113–128, 2011.
- [3] A. Y. Alfakih and Yinyu Ye. On aﬃne motions and bar frameworks in general position. Linear Algebra Appl., 438(1):31–36, 2013.
- [4] Abdo Y. Alfakih. On dimensional rigidity of bar-and-joint frameworks. Discrete Appl. Math., 155(10):1244–1253, 2007.
- [5] Abdo Y. Alfakih, Miguel F. Anjos, Veronica Piccialli, and Henry Wolkowicz. Euclidean distance matrices, semideﬁnite programming and sensor network localization. Port. Math., 68(1):53–102, 2011.
- [6] Maria Belk and Robert Connelly. Realizability of graphs. Discrete Comput. Geom., 37(2):125–137, 2007.
- [7] Ka´roly Bezdek and Robert Connelly. Two-distance preserving functions from Euclidean space. Period. Math. Hungar., 39(1-3):185–200, 1999. Discrete geometry and rigidity (Budapest, 1999).
- [8] L. Blum, M. Shub, and S. Smale. On a theory of computation over the real numbers: NP completeness, recursive functions and universal machines [Bull. Amer. Math. Soc. (N.S.) 21 (1989), no. 1, 1–46; MR0974426 (90a:68022)]. In Workshop on Dynamical Systems (Trieste, 1988), volume 221 of Pitman Res. Notes Math. Ser., pages 23–52. Longman Sci. Tech., Harlow, 1990.
- [9] Jon M. Borwein and Henry Wolkowicz. Facial reduction for a coneconvex programming problem. J. Austral. Math. Soc. Ser. A, 30(3):369– 380, 1980/81.
- [10] R. Connelly. Tensegrities and global rigidity. in Shaping Space, M. Senechal ed., pages 267–278, 2013.
- [11] R. Connelly and A. Back. Mathematics and tensegrity. AMERICAN SCIENTIST, 86(2):142–151, 1998.


- [12] R. Connelly and M. Terrell. Tense´grit´es sym´etriques globalement rigides. Structural Topology, (21):59–78, 1995. Dual French-English text.
- [13] Robert Connelly. Rigidity and energy. Invent. Math., 66(1):11–33, 1982.
- [14] Robert Connelly. Rigidity. In Handbook of convex geometry, Vol. A, B, pages 223–271. North-Holland, Amsterdam, 1993.
- [15] Robert Connelly. Generic global rigidity. Discrete Comput. Geom., 33(4):549–563, 2005.
- [16] Robert Connelly. What is ... a tensegrity? Notices Amer. Math. Soc., 60(1):78–80, 2013.
- [17] Robert Connelly, Tibor Jord´an, and Walter Whiteley. Generic global rigidity of body-bar frameworks. Journal of Combinatorial Theory, Series B (to appear), pages 1–28, 2013.
- [18] Robert Connelly and Walter Whiteley. Second-order rigidity and prestress stability for tensegrity frameworks. SIAM J. Discrete Math., 9(3):453–491, 1996.
- [19] Robert Connelly and Walter Whiteley. Global rigidity: The eﬀect of coning. Discrete Comput. Geom., 43:717–735, 2010.
- [20] Steven J. Gortler, Craig Gotsman, Liu Ligang, and Dylan P. Thurston. On aﬃne rigidity. arXiv:1011.5553v3, pages 1–20, 13 Aug 2013.
- [21] Steven J. Gortler, Alexander D. Healy, and Dylan P. Thurston. Characterizing generic global rigidity. American Journal of Mathematics, 132(132):897–939, August 2010.
- [22] Steven J. Gortler and Dylan P. Thurston. Characterizing the universal rigidity of generic frameworks. Discrete Comput. Geom., 51(4):1017– 1036, 2014.
- [23] Branko Gr¨unbaum. Convex polytopes, volume 221 of Graduate Texts in Mathematics. Springer-Verlag, New York, second edition, 2003. Prepared and with a preface by Volker Kaibel, Victor Klee and Gu¨nter M. Ziegler.


- [24] Bill Jackson and Tibor Jorda´n. Connected rigidity matroids and unique realizations of graphs. J. Combin. Theory Ser. B, 94(1):1–29, 2005.
- [25] Bill Jackson, Tibor Jord´an, and Zolta´n Szabadka. Globally linked pairs of vertices in equivalent realizations of graphs. Discrete Comput. Geom., 35(3):493–512, 2006.
- [26] Adel Javanmard and Andrea Montanari. Localization from incomplete noisy distance measurements. Found. Comput. Math., 13(3):297–345, 2013.
- [27] Tibor Jorda´n and Viet-Hang Nguyen. On universally rigid frameworks on the line. Technical Report TR-2012-10, Egerv´ry Research Group on Combinatorial Optimization, Budapest Hungary, pages 1–13, July 14, 2012.
- [28] Nathan Krislock and Henry Wolkowicz. Explicit sensor network localization using semideﬁnite representations and facial reductions. SIAM J. Optim., 20(5):2679–2708, 2010.
- [29] Monique Laurent and Antonios Varvitsiotis. The gram dimension of a graph. arXiv:1112.5960, pages 1–12, 3Apr 2012.
- [30] Milenko Masic, Robert E. Skelton, and Philip E. Gill. Algebraic tensegrity form-ﬁnding. Internat. J. Solids Structures, 42(16-17):4833–4858, 2005.
- [31] J. Pach, R. Pollack, and E. Welzl. Weaving patterns of lines and line segments in space. In Algorithms (Tokyo, 1990), volume 450 of Lecture Notes in Comput. Sci., pages 439–446. Springer, Berlin, 1990.
- [32] Ja´nos Pach, Richard Pollack, and Emo Welzl. Weaving patterns of lines and line segments in space. Algorithmica, 9(6):561–571, 1993. Selections from SIGAL International Symposium on Algorithms (Tokyo, 1990).
- [33] Igor Pak and Dan Vilenchik. Constructing Uniquely Realizable Graphs. Discrete Comput. Geom., 50(4):1051–1071, 2013.
- [34] Ga´bor Pataki. Strong duality in conic linear programming: facial reduction and extended duals. arXiv:1301.7717v3, 2009.


- [35] Motakuri V. Ramana. An exact duality theory for semideﬁnite programming and its complexity implications. Math. Programming, 77(2, Ser. B):129–162, 1997. Semideﬁnite programming.
- [36] Andr´as Recski. Combinatorial conditions for the rigidity of tensegrity frameworks. In Horizons of combinatorics, volume 17 of Bolyai Soc. Math. Stud., pages 163–177. Springer, Berlin, 2008.
- [37] B. Roth and W. Whiteley. Tensegrity frameworks. Trans. Amer. Math. Soc., 265(2):419–446, 1981.
- [38] J. B. Saxe. Embeddability of weighted graphs in k-space is strongly nphard. In Proc. 17th Allerton Conference in Communications, Control and Computing, pages 480–489, 1979.
- [39] H.-J. Schek. The force density method for form ﬁnding and computation of general networks. Comput. Methods Appl. Mech. Engrg., 3(1):115– 134, 1974.
- [40] Robert E. Skelton and Maurı´cio C. de Oliveira. Optimal tensegrity structures in bending: the discrete Michell truss. J. Franklin Inst., 347(1):257–283, 2010.
- [41] Anthony Man-Cho So and Yinyu Ye. A semideﬁnite programming approach to tensegrity theory and realizability of graphs. In Proceedings of the Seventeenth Annual ACM-SIAM Symposium on Discrete Algorithms, pages 766–775, New York, 2006. ACM.
- [42] Tiong-Seng Tay. Rigidity of multigraphs. I. Linking rigid bodies in nspace. J. Combin. Theory Ser. B, 36(1):95–112, 1984.
- [43] Tiong-Seng Tay and Walter Whiteley. Recent advances in the generic rigidity of structures. Structural Topology, (9):31–38, 1984. Dual FrenchEnglish text.
- [44] Walter Whiteley. Rigidity and polarity. I. Statics of sheet structures. Geom. Dedicata, 22(3):329–362, 1987.
- [45] Walter Whiteley. Rigidity and polarity. II. Weaving lines and tensegrity frameworks. Geom. Dedicata, 30(3):255–279, 1989.


- [46] Walter Whiteley. Rigidity and scene analysis. In Handbook of discrete and computational geometry, CRC Press Ser. Discrete Math. Appl., pages 893–916. CRC, Boca Raton, FL, 1997.
- [47] Yinyu Ye. Semideﬁnite programming and universal rigidity. Fields Institute Lecture, pages 1–92, 2011.
- [48] Li-Yuan Zhang, Yue Li, Yan-Ping Cao, Xi-Qiao Feng, and Huajian Gao. Self-equilibrium and super-stability of truncated regular polyhedral tensegrity structures: a uniﬁed analytical solution. Proc. R. Soc. Lond. Ser. A Math. Phys. Eng. Sci., 468(2147):3323–3347, 2012.
- [49] Zhisu Zhu, Anthony Man-Cho So, and Yinyu Ye. Universal rigidity and edge sparsiﬁcation for sensor network localization. SIAM J. Optim., 20(6):3059–3081, 2010.


