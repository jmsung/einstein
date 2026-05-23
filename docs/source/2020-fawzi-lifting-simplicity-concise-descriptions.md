---
type: source
kind: paper
title: "Lifting for Simplicity: Concise Descriptions of Convex Sets"
authors: Hamza Fawzi, João Gouveia, Pablo A. Parrilo, James Saunderson, Rekha R. Thomas
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2002.09788v2
source_local: ../raw/2020-fawzi-lifting-simplicity-concise-descriptions.pdf
topic: general-knowledge
cites:
---

# arXiv:2002.09788v2[math.OC]19Nov2021

## LIFTING FOR SIMPLICITY: CONCISE DESCRIPTIONS OF CONVEX SETS

HAMZA FAWZI, JOAO˜ GOUVEIA, PABLO A. PARRILO, JAMES SAUNDERSON, AND REKHA R. THOMAS

Abstract. This paper presents a selected tour through the theory and applications of lifts of convex sets. A lift of a convex set is a higher-dimensional convex set that projects onto the original set. Many convex sets have lifts that are dramatically simpler to describe than the original set. Finding such simple lifts has signiﬁcant algorithmic implications, particularly for optimization problems. We consider both the classical case of polyhedral lifts, described by linear inequalities, as well as spectrahedral lifts, deﬁned by linear matrix inequalities, with a focus on recent developments related to spectrahedral lifts.

Given a convex set, ideally we would either like to ﬁnd a (low-complexity) polyhedral or spectrahedral lift, or ﬁnd an obstruction proving that no such lift is possible. To this end, we explain the connection between the existence of lifts of a convex set and certain structured factorizations of its associated slack operator. Based on this characterization, we describe a uniform approach, via sums of squares, to the construction of spectrahedral lifts of convex sets and illustrate the method on several families of examples. Finally, we discuss two ﬂavors of obstruction to the existence of lifts: one related to facial structure, and the other related to algebraic properties of the set in question.

Rather than being exhaustive, our aim is to illustrate the richness of the area. We touch on a range of diﬀerent topics related to the existence of lifts, and present many examples of lifts from diﬀerent areas of mathematics and its applications.

Contents

- 1. Introduction 2

- 1.1. Why lifts? Two simple examples 2
- 1.2. Lifting to nonpolyhedral sets 4
- 1.3. The conic point of view 6
- 1.4. Lifts in mathematics 7
- 1.5. Organization 8


- 2. Four Examples 9

- 2.1. Lifting 0/1 polytopes to ﬂow polytopes via binary decision diagrams 9
- 2.2. The chain polytope of a poset and the Lov´sz theta body of a graph 11
- 2.3. Convex polynomials and their epigraphs 14
- 2.4. The honeycomb lift of the Horn cone 17


- 3. Slack Operators 19

- 3.1. Slack matrices 19
- 3.2. Nonnegative factorizations and Yannakakis’ theorem 20
- 3.3. The slack operator 23
- 3.4. Cone factorizations of slack operators 24
- 3.5. Bregman divergence as a slack operator 26


- 4. Constructions of Lifts 27 4.1. Spectrahedral lifts and sums of squares 27


Joa˜o Gouveia was partially supported by the Centre for Mathematics of the University of Coimbra UIDB/00324/2020, funded by the Portuguese Government through FCT/MCTES. Pablo Parrilo was partially supported by the National Science Foundation through NSF Grant #CCF-1565235. James Saunderson was partially supported by an Australian Research Council Discovery Early Career Researcher Award (project number DE210101056). Rekha Thomas was partially suported by the National Science Foundation through NSF Grant #DMS-1719538.

1

- 4.2. Hierarchies 30
- 4.3. Symmetric convex bodies 31
- 4.4. Linear programming lifts 32

- 5. Obstructions and lower bounds 32

5.1. Obstructions based on facial structure 33 5.2. Algebraic obstructions 37

- 6. Discussion 41 References 43




1. Introduction

The representation of a convex set in Rn is a crucial aspect of algorithmic primitives for convex sets, such as testing membership, computing volume, or optimization. The study of representations of convex sets is of particular importance in the context of optimization, although it is also of interest well beyond this setting. An established idea for representing a convex set, which has received much attention recently, is to express it as the linear projection of another, “simpler” convex set.

simpler set (“lift”)

linear projection

This idea is very powerful — there are by now many examples of convex sets that require highly complicated descriptions in their ambient space, but for which one can ﬁnd a convex set in a higher-dimensional space, with a concise description, that projects to it. The cartoon in Figure 1 illustrates the idea.

complicated set (given)

Such concise “lifts” can lead to considerable algorithmic eﬃciencies for applications such as linear optimization over the original set. They eﬀectively exploit the non-uniqueness of possible preimages of a projection, to ﬁnd a more computationally convenient description. This article will take the reader on a selective tour of key ideas, examples, and applications related to representations of convex sets as projections.

Figure 1. A complicated convex set might admit a concise “lift”, which is a higher-dimensional convex set with a simpler description that projects to it.

- 1.1. Why lifts? Two simple examples. To motivate our topic, consider linear programming which is the problem of optimizing a linear function over a polytope. The number of linear inequalities needed to represent the polytope can be thought of as a measure of its complexity, as it directly aﬀects the eﬃciency of certain algorithms for linear programming over the polytope. The obvious linear inequality description of a polytope P ⊂ Rn requires one inequality for every facet of P (a codimension-one face). However, the number of facets of P may be very large. In such situations, one might ask if there is a more compact representation of P. One possible way out is to move to a higher dimension and write P as the linear projection of a polytope Q ⊂ R where > n. Such a Q is called a lift of P. If in addition, both and the number of facets of Q are small in size, say polynomial in n, then Q is referred to as a small/compact lift of P. Such a small lift can be very useful in optimization, since any linear optimization problem over P can be solved via linear optimization over Q. Indeed if P = π(Q) where π is a linear map, then for any cost vector c we have:


max

c,x = max

c,π(y) .

x∈P

y∈Q

The right-hand side is a linear optimization problem over Q, which can potentially be much easier to solve.

![image 1](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile1.png>)

Figure 2. Cross-polytope C3

- Example 1.1. Consider the 1-norm ball in Rn which is the n-dimensional cross-polytope deﬁned as the convex hull of the 2n vectors ±ei, i = 1,...,n where ei is the ith standard basis vector in

Rn. This polytope has 2n facets, and its inequality description is Cn = {x ∈ Rn : ni=1 ±xi ≤ 1}. The three-dimensional cross-polytope C3 is shown in Figure 2.

Let πx denote the projection from R2n to Rn sending (x,y)  → x. Then Cn = πx(Qn) where Qn = {(x,y) ∈ R2n : ni=1 yi = 1, −yi ≤ xi ≤ yi ∀i = 1,...,n}. Note that Qn has only 2n facets, in contrast to the exponentially many of Cn.

Even though the cross-polytope has 2n facets, it has only 2n vertices. So it is perhaps not too surprising that it has a small lift. Next we consider an example of a polytope that has both exponentially many facets and vertices.

- Example 1.2. The permutahedron Πn ⊂ Rn is the convex hull of the n! vectors obtained by permuting the coordinates of (1,2,...,n). This is an (n − 1)-dimensional polytope with 2n − 2 facets, one corresponding to each proper subset of [n]. Figure 3 shows Π3 and Π4.


123

213 132

312 231

321

2341

2431

1342

1432

3241

3421

1243

1423

4231

4321

3142

3412

2143

2413

1234

1324

4132

4312

2314

2134

4123

4213

3124

3214

Figure 3. On the left is the permutahedron Π3 shown in the ambient space x1 + x2 + x3 = 6. On the right is the permutahedron Π4 shown in the ambient space x1 + x2 + x3 + x4 = 10.

The Birkhoﬀ polytope Bn which is the convex hull of all permutation matrices in Rn×n is a lift of the permutahedron Πn. The linear map X ∈ Rn×n  → (1,2,...,n)X ∈ Rn surjects Bn onto Πn. The Birkhoﬀ-von Neumann theorem [Bir46, VN53] states that Bn coincides with the set of doubly stochastic matrices, i.e.,

n j=1 Xij = 1, ∀ i ∈ [n], ni=1 Xij = 1, ∀ j ∈ [n],

Bn = X ∈ Rn×n :

.

Xij ≥ 0 ∀ 1 ≤ i,j ≤ n

One can see from this description that Bn has n2 facets given by the nonnegativity conditions Xij ≥ 0, and lives in R where = n2. Hence Bn is a small lift of Πn.

In general, lifts are far from being unique. For instance, in Figure 4 we show two diﬀerent polyhedral lifts of a regular octagon. These are non-isomorphic, since the combinatorial structure of the polytopes is diﬀerent, although both lifts have the minimum possible number of facets (six, in this case).

![image 2](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile2.png>)

![image 3](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile3.png>)

Figure 4. Two non-isomorphic polyhedral lifts of a regular octagon, of six facets each.

- 1.2. Lifting to nonpolyhedral sets. The two examples of lifts we saw above were polytopes. From the computational point of view polytopes are feasible sets of linear programs. A signiﬁcant portion of this survey will be devoted to linear programming’s relative, semideﬁnite programming. Semideﬁnite programs [VB96] are linear optimization problems where one optimizes a linear function cixi subject to constraints described by a linear matrix inequality (LMI) of the form


- (1) x1A1 + ··· + xnAn B,


where A1,...,An,B are symmetric matrices. The notation A B means that B − A is positive semideﬁnite (psd). The relation A B (equivalently, B A), is a partial order on the set of symmetric matrices of the same size. Linear matrix inequalities of the form (1) describe convex sets that are, in general, nonpolyhedral. Such sets are called spectrahedra. We say that a convex set C has a spectrahedral lift if it can be expressed as the projection of a spectrahedron. The motivation is clear: if C has a spectrahedral lift then the maximum of a linear function on C can be computed using semideﬁnite programming.

- Example 1.3. Consider the spectrahedron


 

 

 

  0

1 x y

(x,y,z) ∈ R3 :

E3 =

- x 1 z
- y z 1


.





This spectrahedron is known as the elliptope and arises in the famous semideﬁnite relaxation for the maximum cut problem [GW95]. The three-dimensional elliptope is shown in Figure 5 along with various projections.

Why focus on convex sets? The sets we have considered so far are all convex, and this survey will be dedicated to lifts of convex sets. On a ﬁrst encounter, focusing exclusively on lifts of convex sets may seem quite restrictive. However, essentially any linearly parameterized family of optimization problems can be rewritten as linear optimization over a convex set. We illustrate this idea through a simple example. Suppose we have the family of optimization problems:

max{α sint + β cost : t ∈ [0,2π]}

where α,β ∈ R parameterize a choice of objective function. Then we can set x := sint and y := cost and rewrite the family of problems as max{αx + βy : x2 + y2 = 1}. Since the objective function is

![image 4](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile4.png>)

![image 5](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile5.png>)

Figure 5. Two diﬀerent linear images of a spectrahedron. (Note that the linear image on the left is a polytope!)

now linear, this problem is equivalent to maximizing the linear function αx + βy over the convex hull of the circle, i.e., the unit disc in R2. This last reformulation results in a convex program, since the objective function is linear and the feasible region is convex. Figure 6 shows the reformulations for two diﬀerent objective functions.

cos(t) + sin(t)

x + y = √2

x + y = √2

√2 1

t

−y = 1 −y = 1

−sin(t)

Figure 6. Reformulating the problem of maximizing α cos(t) + β sin(t) over t ∈ [0,2π] as a convex optimization problem for (α,β) = (1,1) (solid) and (α,β) = (0,−1) (dashed).

The above idea makes sense in much more generality. Suppose we want to reformulate a family

of problems of the form max{ ki=1 αibi(x) : x ∈ S} where the bi(x) are ﬁxed continuous functions from Rn → R, S ⊂ Rn is a compact set, and the αi parameterize the problem instance. This can be rephrased as

max

k

αizi : z ∈ b(S) where b(S) := {(b1(x),...,bk(x)) : x ∈ S}.

i=1

Since the objective function is linear we can now optimize over the convex hull of b(S) and obtain the equivalent convex problem max{ αizi : z ∈ conv(b(S))}. The approach is most interesting when a subspace of objective functions is reformulated simultaneously. In the special case where we consider only a single objective function b, this reduces to the (rather tautological) convex optimization problem of ﬁnding the largest point in the interval conv(b(S)).

As an example of this general convexiﬁcation approach, consider applying it to a family of polynomial optimization problems. For a vector a ∈ Nn, let |a| denote its 1-norm and let xa denote the monomial xa11xa22 ···xann. Suppose we wish to maximize any degree d polynomial p(x) =

|a|≤d paxa over all x ∈ S ⊂ Rn. This is equivalent to the convex optimization problem

 

 

paya : y ∈ conv{(xa)|a|≤d : x ∈ S}

.

max





|a|≤d

Note that the convex sets that arise from these reformulations are, in general, not polyhedra, and so it is not at all obvious how to computationally represent these sets.

In combinatorial optimization we are constantly faced with linear optimization problems over ﬁnite sets in Rn, mostly subsets of vectors in {0,1}n. Any such problem is equivalent to a linear program over the polytope that is the convex hull of the ﬁnitely many feasible solutions. We will see examples of lifts of such polytopes in later sections.

- 1.3. The conic point of view. The formal setting we consider in this paper is that of conic lifts which permits an elegant treatment of both polyhedral and spectrahedral lifts in a uniﬁed way. This treatment is also motivated from optimization theory, where linear and semideﬁnite programming are seen as special cases of conic programming [NN94, BTN01a]. To motivate the deﬁnition which follows, note that a polyhedron P = {x ∈ Rn : Ax ≤ b} where A ∈ Rm×n can be equivalently seen


(via a linear bijection) as the intersection Rm+ ∩ L, where Rm+ is the nonnegative orthant in Rm and L = b + colspan(A) is an aﬃne space. Similarly the spectrahedron deﬁned by (1) is linearly

isomorphic to S+m ∩ L, where S+m is the convex cone of m × m symmetric positive semideﬁnite matrices, and L = B + span(A1,...,An). With these examples in mind, we can state the formal deﬁnition of a conic lift that we adopt in this paper:

- Deﬁnition 1.4. Let C ⊂ Rn be a convex set and K ⊂ R be a closed convex cone. We say that C has a K-lift if C = π(K ∩ L) where L is an aﬃne space in R and π : R → Rn is a linear map. The convex set K ∩ L is called a K-lift of C.


If C = π(Rm+ ∩ L) (respectively, C = π(S+m ∩ L)) we say that C has a polyhedral (respectively, spectrahedral) lift of size m. Going back to Example 1.2, the Birkhoﬀ polytope Bn has O(n2) inequalities none of which are redundant, and thus is a polyhedral lift of Πn of size O(n2). The smallest m for which C = π(Rm+ ∩L) is called the linear extension complexity of C, and the smallest m for which C = π(S+m ∩ L) is called the semideﬁnite extension complexity of C. It was shown by Goemans [Goe15] that the linear extension complexity of Πn is O(nlog n). The proof involves constructing an explicit lift of Πn of that size by using sorting networks.

Another convex cone of special interest in conic programming is the second-order cone deﬁned as

L3+ = {(x0,x) ∈ R × R2 : x 2 ≤ x0}. If a convex set has a (L3+)m-lift (for some integer m) then we say it has a second-order cone lift. Examples of convex sets with second-order cone lifts include ellipsoids and p-norm balls for rational p ≥ 1, which arise in many practical situations. (See, e.g., [BTN01a] for these, and many more, interesting examples.) Figure 7 summarizes the inclusion relationship between diﬀerent types of Klifts, when K is one of Rm+,(L3+)m,S+m. A discussion and proof of these relationships, in particular the strict inclusions, will be given in Section 5.

Remark 1.5 (Terminology). We remark that there is diﬀering terminology in the papers that study lifts of convex sets. Polyhedral lifts are sometimes called extended formulations, linear lifts or LPlifts. Spectrahedral lifts are sometimes called semideﬁnite lifts or psd-lifts. A convex set that admits a spectrahedral lift is a projected spectrahedron or spectrahedral shadow, and the set is said to have a linear matrix inequality (LMI) representation or semideﬁnite representation. Linear extension complexity is also known as nonnegative rank and semideﬁnite extension complexity as psd rank. In this paper we will use the terminology we have introduced in the previous paragraphs.

Convex sets having a polyhedral lift = polyhedra

Convex sets having a second-order cone lift

Convex sets having a spectrahedral lift

All convex semialgebraic sets

Figure 7. Inclusion relationship between diﬀerent types of lifts. The fact that the inclusions are strict will be discussed in more detail in Section 5. (The deﬁnition of a semialgebraic set is given in Section 5.2.1.)

- 1.4. Lifts in mathematics. The idea of going to a higher-dimensional space to seek a “nicer” representation of an object is a common theme in many areas of mathematics. A familiar example is resolution of singularities of algebraic varieties, one of the oldest and best known problems in algebraic geometry. Given a singular algebraic variety, the goal is to write it as a proper birational image of a smooth variety. In 1964 Hironaka [Hir64a, Hir64b] proved that such resolutions always exist for varieties over ﬁelds of characteristic zero such as C or R. In simpliﬁed terms, Hironaka’s result says that the set of solutions in kn, where k is a ﬁeld of characteristic zero, to a system of polynomial equations can always be rationally parametrized by a smooth manifold. (See, e.g., [Hau03] for a tutorial-style exposition.) Besides the theoretical importance of resolutions, they are also of practical relevance. For instance, they allow us to use our arsenal of techniques for optimization over smooth functions to indirectly optimize over a non-smooth variety, by passing to the lifted smooth variety.


- Example 1.6. Consider the deltoid curve (see Figure 8), which is the set of solutions in R2 of (x2 + y2)2 − 8(x3 − 3xy2) + 18(x2 + y2) − 27 = 0.


As is evident from Figure 8, this curve has three singularities.

![image 6](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile6.png>)

![image 7](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile7.png>)

Figure 8. On the left is the deltoid curve which has 3 singularities. On the right we see the deltoid as the projection of a smooth curve.

The deltoid is polynomially parametrized by a circle, since it can be written as {(1 + 2cos(t) − 2sin(t)2,2sin(t) − 2sin(t)cos(t)) : t ∈ [0,2π]}.

This is already very useful, but one can actually write it as a linear projection of a smooth curve, by simply adding a sin(3t) term to the parametrization. Consider the curve

Y = {(1 + 2cos(t) − 2sin(t)2,2sin(t) − 2sin(t)cos(t),sin(3t)) : t ∈ [0,2π]} ⊆ R3. The curve Y is smooth, and we can see it projecting onto the deltoid.

Here is another instance of the usefulness of “lifting”. Given a probability distribution πX deﬁned on some space X, a fundamental problem in probability and statistics is to generate a sample from the distribution. One way to do this is to construct an ergodic Markov chain with stationary distribution given by πX, and then generate sample paths for the Markov chain. A key measure of

the performance of such a sampling method is the mixing time of the Markov chain, a measure of how fast the distribution of the samples converges to the stationary distribution.

A lifting of a Markov chain is a new Markov chain on a larger state space X × Y so that the marginal on the X space is the original Markov chain. In certain situations, carefully designed liftings of a Markov chain mix faster than the original chain, leading to faster sampling methods [CLP99]. More generally, many methods for sampling involve introducing auxiliary variables and a probability distribution πX×Y on a larger state space, running a Markov chain Monte-Carlo (MCMC) method to (approximately) sample from that distribution, and then taking the marginal on the X variables. Such strategies often tend to mix faster in practice than an MCMC method working directly in the space of the original distribution. These are often called auxiliary variable samplers, and include approaches such as Hamiltonian Monte-Carlo (HMC) [Nea11] and slice sampling [Nea03].

On a philosophical note, recall that in quantiﬁer elimination, one is interested in ﬁnding a set that has been speciﬁed in terms of quantiﬁers and extra variables. This is a projection operation that is, in general, hard to do. For example, projecting out variables from a system of linear inequalities can be done by Fourier-Motzkin elimination [Zie00, Chapter 1] which can take an exponential number of steps. The concept of a lift is inverse to the idea of projection. We start with a highly complicated (convex) set and ask if it can be written as the projection of a (if possible, simple) convex set in some higher dimension.

- 1.5. Organization. There are a number of applications, coming from a wide range of areas of mathematics, that illustrate the usefulness of lifted representations of convex sets. In Section 2 we give four very diﬀerent examples, to bring home this point.


Given a convex set C ⊂ Rn and a closed convex cone K ⊂ R , the ﬁrst question one can ask is whether C admits a K-lift at all. In Section 3 we build the theory that allows us to answer this foundational question. The key ingredient is the slack operator of a convex set which is described in Section 3.3. This is a generalization of the slack matrix of a polytope which was introduced by Yannakakis [Yan91] to study polyhedral lifts of polytopes. The slack matrix of a polytope is deﬁned in Section 3.1 and Yannakakis’ theorem that decides the existence of a Rm+-lift of a polytope P ⊂ Rn is described in Section 3.2. The main result of Section 3 says that a convex set C ⊂ Rn has a K-lift for some closed convex cone K ⊂ R if and only if the slack operator of C factorizes through K and its polar cone K∗. This result is stated and discussed in Section 3.4 and we illustrate it on several examples. The slack operator of a convex set can also be seen as a generalization of the notion of Bregman divergence of a convex function. This analogy is discussed in Section 3.5.

There are many creative constructions of lifts of convex sets in the literature, and in Section 4 we focus on construction methods for spectrahedral lifts of convex sets. We emphasize in particular the connection with sum-of-squares certiﬁcates of nonnegativity, and semideﬁnite hierarchies. This viewpoint is illustrated on several examples. We brieﬂy discuss the analogous viewpoint for polyhedral lifts and establish the connection with well-known methods such as the Sherali-Adams hierarchy [SA90].

Having addressed the existence question and seen some construction methods, a next natural step is to understand obstructions to the existence of a K-lift of C. In Section 5 we discuss two ﬂavors of obstructions. The ﬁrst is combinatorial in nature and depends on the facial structure of both C and K. Such obstructions are already powerful enough to show interesting results such as the psd cone S+3 does not admit a lift into a product of second order cones [Faw19]. Next we consider algebraic obstructions to the existence of lifts. We prove lower bounds on the semideﬁnite extension complexity of C based on the degree of its algebraic boundary as well as dim(C). Finally we discuss the recent result of Scheiderer [Sch18] that not all convex semialgebraic sets admit a spectrahedral lift and provide concrete examples of such sets (see Figure 7).

x1 x2 x2

- x3 x3

- x4 x4


|0|
|---|


|1|
|---|


x1 x2 x2

- x3 x3

- x4 x4


|1|
|---|


Figure 9. On the left is an (ordered) BDD corresponding to the Boolean function fxor that computes the sum of the inputs modulo 2. Solid lines represent arcs labeled by 1, and dashed lines represent arcs labeled by 0. The path corresponding to the assignment (1,1,0,0) to the variables is highlighted in bold. On the right is a zero-suppressed BDD representing the set {x ∈ {0,1}4 : fxor(x) = 1}.

The study of lifts of convex sets has many results and theories beyond what we have chosen to present in this paper. We conclude with a brief discussion of related directions and results, as well as pointers to surveys and expository articles on these topics.

2. Four Examples

In the rest of this paper we will study lifts of convex sets as in Deﬁnition 1.4. We begin with four examples of lifts, each from a diﬀerent area of mathematics, to illustrate the ubiquity and usefulness of the idea even beyond the context of optimization. This section can be read independently of the rest of the paper and can be skipped if the reader wishes to get to the mathematical theory behind lifts, which begins in Section 3.

- 2.1. Lifting 0/1 polytopes to ﬂow polytopes via binary decision diagrams. A binary decision diagram (BDD) or branching program is a data structure that represents a Boolean function. It is a directed acyclic graph in which exactly one node has in-degree zero (the source node), exactly two nodes have out-degree zero (the sink nodes), and every non-sink node (known as a decision node) has out-degree two (see Figure 9). The sink nodes are labeled 0 and 1. Every decision node


is labeled with a variable x1,x2,...,xn and has one outgoing arc labeled 0 and one outgoing arc labeled 1 (which are usually depicted as dashed and solid arcs respectively). Any assignment of Boolean values to the variables, i.e., xi = ai ∈ {0,1} for all i, speciﬁes a path from the source to one of the sinks. The path is deﬁned by taking, for each decision node labeled xi, the outgoing edge labeled ai (see Figure 9). Whether the path associated with a ∈ {0,1}n ends at the 0-sink or the 1-sink deﬁnes a Boolean function f : {0,1}n → {0,1}. The diagram on the left of Figure 9 shows a BDD representing the function

fxor(x1,x2,x3,x4) = x1 + x2 + x3 + x4 (mod 2). It has the additional property that the variables are totally ordered and, along every source-sink path, every variable appears at most once in a way that respects the order. Such a BDD is called an ordered BDD (OBDD) or oblivious read-once branching program [Bry86]. If a Boolean function has an OBDD representation with a small number of nodes then this automatically leads to eﬃcient

algorithms for counting the number of satisfying assignments, sampling from the uniform distribution on satisfying assignments, and solving the integer linear program maxx∈{0,1}n:f(x)=1 i aixi. Moreover, natural operations on Boolean functions lead to corresponding operations on OBDDs.

Associated with a Boolean function f : {0,1}n → {0,1} is the 0/1 polytope Pf = conv{x ∈ {0,1}n : f(x) = 1}. It turns out that we can construct a polyhedral lift of Pf from an OBDD representation of f. Let A denote the set of arcs of the OBDD. For any subset S of arcs let

χS ∈ {0,1}A denote its characteristic vector deﬁned as (χS)i = 1 if i ∈ S and (χS)i = 0 otherwise. Given an OBDD Bf representing f, consider the ﬂow polytope

F(Bf) = conv χS ∈ {0,1}A : S ⊆ A is a directed path from the source to the 1-sink in Bf . For i = 1,2,...,n, let Ai denote the set of arcs leaving nodes of the OBDD labeled with variable i. Proposition 2.1. The polytope F(Bf) is a polyhedral lift of the 0/1 polytope Pf. The linear map deﬁning the lift is π : RA → Rn deﬁned by [π(y)]i = a∈A

ya for i = 1,2,...,n.

i

Proof. There is a one-one correspondence between paths from the source to the 1-sink in the OBDD and vertices of Pf. Moreover, every such path contains at most one arc from each Ai. As such, the vertices of F(Bf) are mapped to those of Pf by π.

Since F(Bf) is an example of a network ﬂow polytope, it can be described using one linear inequality for each arc in the network. Indeed, it is a fundamental result (see, e.g., [Sch03]) that

F(Bf) = {y ∈ RA : y ≥ 0, By = b} where b ∈ RV and B : RA → RV are deﬁned by

 

1 if v is the 1-sink −1 if v is the source 0 otherwise,

ya −

ya for all v ∈ V ,

and [By]v =

bv =



a∈vin

a∈vout

and where vin ⊆ A and vout ⊆ A denote the set of incoming arcs and outgoing arcs from vertex v ∈ V . To summarize, any OBDD representation of a Boolean function leads to a polyhedral lift of the corresponding 0/1 polytope of the same size as the OBDD.

Corollary 2.2. If f : {0,1}n → {0,1} is a Boolean function with an OBDD representation having |A| arcs, then the polytope Pf = {x ∈ {0,1}n : f(x) = 1} has a polyhedral lift of size |A|.

- Example 2.3 (Odd parity polytope). The odd parity polytope is the convex hull of binary vectors


with an odd number of ones. From Figure 9 it is clear that the Boolean function fxor has an OBDD with 4(n−1)+2 = 4n−2 arcs. It follows that the odd parity polytope has a polyhedral lift of size 4n − 2.

There is a nontrivial upper bound on the size of an OBDD of a general Boolean function f. This gives a corresponding upper bound on the size of a polyhedral lift of an arbitrary 0/1 polytope. Theorem 2.4. Any 0/1 polytope in Rn has a polyhedral lift of size at most 6.n25 · 2n. Proof. Any n-variable Boolean function has an OBDD with at most 3.125n ·2n nodes [LL92, Theorem 1], and hence at most 6.n25 · 2n arcs. The result then follows from Corollary 2.2.

There are many variations and generalizations of OBDDs, a number of which naturally give rise to ﬂow-polytope lifts of 0/1 polytopes. A similar approach can be used to construct polyhedral lifts based on free BDDs (in which every variable appears at most once on every source-sink path, but not necessarily in the same order [Mas76, Weg00]). The lifted representations of 0/1 polytopes described in this section can be simpliﬁed by using zero-supressed OBDDs (ZBDDs) [Min93]. These are OBDDs where any arcs leading only to the 0-sink are removed, and the corresponding diagram

is reduced by removing any redundancy. A ZBDD is shown on the right in Figure 9. Clearly these arcs do not change any path from the source to the 1-sink, so the polyhedral lifts described above can (possibly) be reduced in size by using a ZBDD representation instead.

## 2.2. The chain polytope of a poset and the Lova´sz theta body of a graph.

- 2.2.1. Chain polytopes. Let P be a ﬁnite partially ordered set (poset), where the partial order is denoted by ≺1, and let RP denote the Euclidean space whose coordinates are indexed by the elements of P. We start by quickly recalling a series of basic concepts from posets, that will be used throughout the example. The characteristic vector of an element a ∈ P is the vector in RP with 1 in the coordinate indexed by a and 0 everywhere else. An antichain in P is a collection of elements of P such that no two in the collection are comparable in the partial order. A chain in P on the other hand is a collection of elements that are totally ordered. The characteristic vector of a collection of elements in P, for instance of a chain or antichain, is the sum of the characteristic vectors of all elements in that collection. A closely related concept to antichain is that of a ﬁlter,


i.e. a set I such that a1 ∈ I and a2 a1 implies a2 ∈ I. There is a natural bijection between ﬁlters I and antichains A, given by

I = {y ∈ P : y x for some x ∈ A} ↔ A = {minimal elements of I}.

Finally, we say that a2 covers a1 if a1 ≺ a2 and there is no x ∈ P with a1 ≺ x ≺ a2. We call this a cover relation.

- Example 2.5. Consider P to be the poset of the faces of the triangular prism illustrated in Figure 10 ordered by inclusion. We will usually represent such a poset by its Hasse diagram. This is simply a graph where the nodes are the elements of the poset, drawn in such a way that if a1 a2 then a1 is below a2, and the edges represent the cover relations. In Figure 10 we can also see the Hasse diagram of the poset of faces of the triangular prism.


![image 8](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile8.png>)

ABCDEF

ABC ABDE BCEF ACDF DEF

AB BC AC AD BE CF DE EF DF

A B C D E F

∅

Figure 10. Triangular prism and the Hasse diagram of its face poset

This poset has a single maximal element, the entire prism, and minimal element, the empty face. An example of a chain is (∅,A,AB,ABDE,ABCDEF) which, in this case, is maximal. An example of a maximal antichain is {ABC,AD,BE,CF,DEF}. The ﬁlter mapping to that antichain is the collection of all the elements that are greater than or equal to any of the elements, namely

{ABC,AD,BE,CF,DEF,ADBE,ACDF,BCEF,ABCDEF}.

1We also use this notation for the speciﬁc partial order on symmetric matrices induced by the positive semideﬁnite cone. Occasionally both will be used in close proximity, but the meaning should be clear from the context.

The chain polytope chain(P) of P, introduced in [Sta86], is the convex hull in RP of the characteristic vectors of all antichains of P. The name comes from its inequality description:

- (2) chain(P) = x ∈ RP+ : 0 ≤ xa1 + xa2 + ··· + xak ≤ 1, ∀ chains a1 ≺ a2 ≺ ··· ≺ ak in P . The correctness of this inequality description will become clear at the end of this section. The facets of chain(P) are given by the nonnegativity constraints 0 ≤ xa for all a ∈ P and the inequalities xa1 + xa2 + ··· + xak ≤ 1 for all maximal chains a1 ≺ a2 ≺ ··· ≺ ak in P.

- Example 2.6. There are ﬁve non isomorphic posets with three elements. Those will have three dimensional chain polytopes. We can see all of them in Figure 11. Note that two have the same chain polytope up to coordinate labeling.

![image 9](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile9.png>)

![image 10](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile10.png>)

![image 11](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile11.png>)

![image 12](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile12.png>)

Figure 11. All the three-element posets and their corresponding chain polytopes

The number of vertices and facets of chain(P) can be superpolynomial in |P| as the following example shows.

- Example 2.7. Let B(n) denote the Boolean lattice of the subsets of [n]. The number of antichains


in B(n) is the n-th Dedekind number which grows at least as fast as 2

√ N

log(N), where N = 2n is the number of elements in B(n). As antichains correspond to vertices of the chain polytope chain(B(n)), there are a superpolynomial number of them. On the other hand, since all maximal chains deﬁne facets of chain(B(n)), and there are n! maximal chains in B(n), the number of facets of chain(B(n)) is of the order Nlog(log(N)) which is also superpolynomial in n.

The order polytope of the poset P was also introduced in [Sta86]. It is given by

- (3) order(P) = {x ∈ RP : 0 ≤ xa1 ≤ xa2 ≤ 1, ∀ a2 a1 in P}. It is in fact enough to consider the inequalities corresponding to cover relations, together with


xa ≥ 0 for all minimal elements a ∈ P and xa ≤ 1 for all maximal elements a ∈ P. The vertices of order(P) are the characteristic vectors of ﬁlters, which we have seen to have a natural bijection to antichains, which leads to the following result.

Proposition 2.8 (Theorem 3.2 [Sta86]). The map f : RP → RP deﬁned by

xai if ai is a minimal element of P min{xai − xaj | ai covers aj} otherwise

f(x)ai =

is piecewise linear and maps order(P) bijectively to chain(P) preserving the bijection between vertices.

This is not really a lift of the chain polytope, as the map involved is not linear. However, as is current practice in linear optimization, one can introduce slack variables to linearize the minimum function and we get the following result.

Corollary 2.9. The chain polytope chain(P) of a poset P is the projection onto the z coordinates of (z,x) ∈ RP × RP such that x ∈ order(P), 0 ≤ zai ≤ xai − xaj for all cover relations ai aj and zai = xai for all minimal elements ai.

Corollary 2.9 gives an explicit polyhedral lift of chain(P) with O(|P|2) facets, showing that one can use linear programming to eﬃciently optimize over the chain polytope. Since posets can be thought of as acyclic digraphs, this allows us to eﬃciently optimize over sets of mutually unreachable vertices in an acyclic digraph. Further discussions on the algorithmic implications of the chain polytope can be found on Section 14.5 of [Sch03].

- 2.2.2. A spectrahedral lift of the chain polytope. Next we will see that chain(P) has a spectrahedral lift of size O(|P|). This lift is a special case of a general construction of spectrahedral lifts of stable set polytopes of perfect graphs. We describe the general construction below.


The comparability graph of the poset P is the graph whose vertices are the elements of P and whose edges are (a1,a2) for all a1 ≺ a2 (not just cover relations). A stable set S of a graph G = (V (G),E(G)) is a subset of V (G) such that no pair in S lies in E(G). The characteristic vector of a stable set S in G is the vector in {0,1}V (G) with coordinate 1 in positions indexed by v ∈ S and 0 everywhere else. The stable set polytope of G, denoted as stab(G), is the convex hull of the characteristic vectors of all stable sets in G. Note that the antichains in a poset P are precisely the stable sets in its comparability graph. Hence chain(P) is the stable set polytope of the comparability graph of P.

![image 13](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile13.png>)

Figure 12. Icosahedral graph with an optimal 4-coloring. Each maximal monochromatic set of nodes is actually a maximal stable set.

Recall that a perfect graph is a graph for which the chromatic number equals the clique number for every induced subgraph. In Figure 12 we can see that the icosahedral graph is not perfect,

- as its chromatic number is 4 while its maximal clique is a triangle and hence its clique number is 3. In general, optimizing a linear function over the stable set polytope of a graph is NP-hard. However if the graph G is perfect then stab(G) admits a small spectrahedral lift of size n + 1 where n = |V (G)|. In particular, we get that the largest stable set in a perfect graph can be found in polynomial time via semideﬁnite programming [GLS84, GLS86]. This construction marks the beginning of the use of semideﬁnite programming in discrete optimization. Comparability graphs of posets are perfect graphs (see for instance [Gol04, Section 5.7]), and hence the chain polytope chain(P) has a spectrahedral lift of size |P| + 1. We now describe the general construction from which this lift arises.


Let G = (V (G),E(G)) be a graph where V (G) = [n]. For a stable set S ⊂ [n], let χS denote its characteristic vector in {0,1}n. Setting x := χS, notice that

1 x

X :=

1 x

is a matrix in S+n+1 with the following properties: X00 = 1, X0i = Xi0 = xi ∀i ∈ [n], Xii = xi ∀i ∈ [n], Xij = 0 ∀ij ∈ E(G), rank(X) = 1. Consider the spectrahedron deﬁned by all the above conditions except for the rank condition:

 

 

X00 = 1, X0i = Xi0 = xi ∀i ∈ [n], Xii = xi ∀i ∈ [n], Xij = 0 ∀ij ∈ E(G)

X ∈ S+n+1 :

L(G) :=

.





Now consider the linear map π that maps X ∈ Sn+1 to (X01,X02,...,X0n) ∈ Rn.

- Deﬁnition 2.10. The projection th(G) := π(L(G)) ⊂ Rn is called the theta body of the graph G.


Theta bodies were introduced in [GLS86]. For the formulation shown above, see [GLS93, Chapter 9]. Since every vertex of stab(G) is a χS and the matrix X obtained by lifting χS as above lies in L(G), it follows from convexity that stab(G) ⊆ th(G).

Theorem 2.11. [GLS86, Corollary 3.11] stab(G) = th(G) if and only if G is perfect.

Since the comparability graph of a poset P is perfect, and chain(P) is its stable set polytope, we get the following corollary. Corollary 2.12. The chain polytope chain(P) admits a spectrahedral lift of size |P| + 1. More precisely,

- (4) chain(P) = x ∈ RP : ∃ Y ∈ RP×P s.t.

1 xT x Y

0, diag(Y ) = x, yab = 0 if a b or a ≺ b .

Other examples of perfect graphs are chordal graphs and bipartite graphs. In all of these cases, stab(G) admits a spectrahedral lift of size |V (G)| + 1.

If G = ([n],E) is perfect, then stab(G) also has an explicit (although large) polyhedral description, namely,

stab(G) = x ∈ Rn : x ≥ 0,

i∈K

xi ≤ 1 ∀ cliques K in G .

This is why the facets of the chain polytope chain(P) are given by the maximal chain inequalities in the comparability graph of P and nonnegativities of variables.

We have seen that the chain polytope admits the polyhedral lift order(P) of size O(|P|2) and the spectrahedral lift L(G) of size |P| + 1. We will see later that no spectrahedral lift of chain(P) can have size smaller than |P| + 1. More generally, any spectrahedral lift of a polytope P has size

- at least dim(P) + 1.


- 2.3. Convex polynomials and their epigraphs. In the area of nonlinear programming, it is traditional to express optimization problems in the form


- (5) min


f(x) subject to gi(x) ≤ 0 for i = 1,2,...,m

x

for functions f : Rn → R and g1,...,gm : Rn → R. If these are all convex functions, then such an optimization problem is called a convex optimization problem. Since the advent of interior point methods in the 1990s, it has become common to reformulate such convex optimization problems as

min

t subject to

x,t

(x,t) ∈ epi(f) (x,0) ∈ epi(gi) for i = 1,2,...,m

![image 14](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile14.png>)

LIFTING FOR SIMPLICITY: CONCISE DESCRIPTIONS OF CONVEX SETS 15

Figure 13. The intersection of the zero-sublevel sets of the (sos-)convex polynomials g1(x,y,z) = x4 + y4 + z4 − 3 and g2(x,y,z) = (x − 2)2 + 2y2 + 3z2 − 5.

where epi(f) = {(x,t) ∈ Rn × R : f(x) ≤ t} is the epigraph of f. Here we have introduced an additional variable and expressed the problem as the minimization of a linear functional over a convex set. This motivates the study of lifted representations of the epigraphs of convex functions.

If we restrict to diﬀerentiable convex functions, one approach to constructing lifted representations of their epigraphs is to make use of the ﬁrst-order characterization of convexity, i.e.,

- (6) f(x) − [f(y) +  ∇f(y),x − y ] ≥ 0 for all (x,y) ∈ Rn × Rn.


This inequality just tells us that the graph of f is above the graph of its linear approximation at y, for any y. The expression on the left hand side of (6) is the Bregman divergence associated with f.

- 2.3.1. Convex and sos-convex polynomials. We now restrict, further, to convex polynomials of degree at most 2d. (With minor modiﬁcations, the discussion extends to convex rational functions f(x)/g(x) with g(x) > 0 for all x.) The Bregman divergence of a convex polynomial f of degree at most 2d in n variables, is a non-negative polynomial of degree 2d in the 2n variables (x,y). Since the Bregman divergence is linear in f, the ﬁrst order characterization of convexity (6) tells us that


the set of convex polynomials of degree at most 2d in n variables is a slice of Pol2+n,2d, the cone of nonnegative polynomials of degree at most 2d in 2n variables. Denote by Poll,2d, the set of all polynomials in l variables of degree at most 2d.

Whenever n = 1 or 2d = 2 or (n,2d) = (2,4), it can be shown [AP13] that the Bregman divergence of a convex polynomial of degree at most 2d in n variables can be written as a sum of squares, i.e., there exist f1,f2,... ∈ Pol2n,d such that

fk(x,y)2 for all (x,y) ∈ Rn × Rn.

f(x) − [f(y) +  ∇f(y),x − y ] =

k

Otherwise, the polynomials for which the Bregman divergence is a sum of squares (called sos-convex polynomials [HN10]) are a strict subset of all convex polynomials with a given degree and number of variables.

Let Σ ,+2d denote the cone of polynomials of degree at most 2d in variables that are sums of squares. This cone has a spectrahedral lift given by

Σ ,+2d = {f ∈ Pol ,2d : ∃Q 0, such that f(x) = vd(x) Qvd(x) ∀x ∈ R }.

Here vd(x) is the length +dd vector consisting of all monomials of degree at most d in variables. Using this, we obtain a spectrahedral lift of the cone of sos-convex polynomials.

- Proposition 2.13. The cone of sos-convex polynomials has the following spectrahedral lift

(7) f ∈ Poln,2d : ∃Q 0 s.t. f(x) − [f(y) +  ∇f(y),x − y ] = vd(x,y) Qvd(x,y) ∀(x,y) ∈ Rn × Rn .

In the cases n = 1, 2d = 2, and (n,2d) = (2,4), for which all convex polynomials are sos-convex, Proposition 2.13, in fact, gives a spectrahedral lift of the cone of convex polynomials.

- 2.3.2. Epigraphs of convex and sos-convex polynomials. We can also use the characterization (6)


to express the epigraph of any ﬁxed convex polynomial as an aﬃne slice of Poln,+2d, and give a spectrahedral lift of the epigraph of any sos-convex polynomial.

- Proposition 2.14. If f is a convex polynomial, then


- (8) epi(f) = {(x,t) ∈ Rn × R : t − [f(y) +  ∇f(y),x − y ] ∈ Poln,+2d}. If f is a sos-convex polynomial, then
- (9) epi(f) = {(x,t) ∈ Rn × R : ∃Q 0 s.t. t − [f(y) +  ∇f(y),x − y ] = vd(y) Qvd(y) ∀y ∈ Rn .


Proof. If f is convex (respectively, sos-convex) and (x,t) ∈ epi(f), then f(x) ≤ t and so t − [f(y) +  ∇f(y),x − y ] = (t − f(x)) + f(x) − [f(y) +  ∇f(y),x − y ]

is nonnegative (respectively, a sum of squares). On the other hand, if t−[f(y)+ ∇f(y),x−y ] ≥ 0 for all y ∈ Rn, then putting y = x we have that t ≥ f(x), and so (x,t) ∈ epi(f).

Since the epigraphs of sos-convex polynomials have spectrahedral lifts, we can reformulate convex optimization problems of the form (5), in which the objective function and the constraints are sosconvex polynomials, as semideﬁnite programming problems. Figure 13 shows the feasible region of such a problem for two sos-convex polynomials.

- Example 2.15 (Epigraph of a convex quadratic and convex quadratic programming). If f(x) = x Ax+2b x+c and A is positive semideﬁnite, then f is a convex quadratic. Optimization problems


of the form (5) in which f and the gi are all convex quadratics are known as (convex) quadratic programs. Since any convex quadratic is sos-convex,

epi(f) = {(x,t) ∈ Rn × R : ∃Q 0 s.t. y Ay − 2(Ax) y + (t − c − 2b x) = 1 y Q

1 y ∀y ∈ Rn

t − c − 2b x −(Ax) −Ax A

= (x,t) ∈ Rn × R :

0 .

If f(x) = x x and we consider the t = 1 slice of epi(f), we obtain a well-known spectrahedral representation of the sphere:

1 −x −x I

1 x x I

{x ∈ Rn : x x ≤ 1} = x ∈ Rn :

0 = x ∈ Rn :

0

where the last description is obtained via a congruence by 10 −0I , which preserves positive semidefiniteness.

- 2.4. The honeycomb lift of the Horn cone. Given the eigenvalues of two n × n Hermitian matrices A and B, a classical question from linear algebra is to characterize the eigenvalues of A + B. Equivalently, the problem is to characterize the triplets (λ,µ,ν) ∈ (Rn)3 where λ is the vector of eigenvalues of an n × n Hermitian matrix A in weakly-decreasing order, µ that of B, and ν that of C, such that A + B + C = 0. Call such a triplet (λ,µ,ν) ∈ (Rn)3 valid. The question of characterizing valid triplets was posed by Hermann Weyl in 1912. He gave a number of necessary


conditions, starting with the obvious trace condition that λi + µi + νi = 0.

In 1962 Horn conjectured that the set of valid triplets forms a convex polyhedral cone and proposed a complete set of linear inequalities that describes it via a recursive recipe [Hor62]. Let hornn ⊂ R3n be the set of valid triplets (λ,µ,ν). The inequalities conjectured by Horn have the form

λi1 + ... + λir + µj1 + ... + µjr + νk1 + ... + νkr ≥ 0

where 1 ≤ r < n and all triplets of indices 1 ≤ i1 < ... < ir ≤ n,1 ≤ j1 < ... < jr ≤ n,1 ≤ k1 < ... < kr ≤ n are in a set Tn,r. Horn’s conjecture described the set Tn,r recursively in terms of sets Tr,s for 1 ≤ s < r. This recipe leads to an exponential number of inequalities for hornn.

The Horn conjecture was proved by a combination of the works of Klyachko [Kly98] and KnutsonTao [KT99, KT01]. Remarkably the work of Knutson-Tao also shows that the convex set hornn admits a small polyhedral lift of size O(n2).

- Theorem 2.16. The Horn cone for n×n Hermitian matrices admits a polyhedral lift called honeyn with O(n2) facets.


In this short section we describe the lift of Knutson-Tao but we do not attempt to explain the proof, which uses sophisticated arguments from algebraic geometry and representation theory (we refer the interested reader to [KT01] for more details).

Consider a honeycomb structure as shown in Figure 14. The honeycomb is formed of internal hexagons, and has 3n outgoing edges, each labeled by λi, µi or νi in the way shown in the Figure.

- λ1

- λ2

- λ3

- λ4

- λ5 µ1


- µ2

- µ3

- µ4

- µ5


ν5 ν4 ν3 ν2 ν1

Figure 14. The honeycomb structure used to describe the lift of hornn for the case n = 5

Let En be the set of edges in the n-honeycomb. It is not hard to see that |En| = O(n2). Let Γn ⊂ En × En be the pairs of edges (a,b) ∈ En × En that are in one of the conﬁgurations shown in Figure 15. An example of such a conﬁguration is highlighted in Figure 14.

We are now ready to describe the lift. Consider the polyhedral cone honeyn in REn deﬁned by:

- (10) honeyn = e ∈ REn : ea − eb ≥ 0 ∀(a,b) ∈ Γn ea + eb + ec = 0 ∀edges a,b,c meeting at a common vertex}.


b

a

b

a

a

b

Figure 15. Conﬁgurations of pairs of edges (a,b) in a honeycomb that appear in the lift of hornn. Note that these three patterns are 120◦ rotations of each other.

Consider the map ∂ that projects a vector e ∈ REn onto the 3n outgoing edges of the honeycomb. The result of Knutson and Tao shows that

- (11) hornn = (λ,µ,ν) ∈ R3n : λ1 ≥ ··· ≥ λn, µ1 ≥ ··· ≥ µn, ν1 ≥ ··· ≥ νn and ∃e ∈ honeyn s.t. (λ,µ,ν) = ∂(e)}.

ν3 ν2 ν1

1

0

−1 2

1

0 −1 − ν3 e5 e6

e3 e4

e1 e2

−1

−ν1

1 Figure 16. A 3-honeycomb.

- Example 2.17. Take n = 3 and suppose λ = (1,0,−1), µ = (2,1,0) and ν = (ν1,ν2,ν3) are the vectors of eigenvalues of A,B,C such that C = −A − B and all matrices are 3 × 3 and Hermitian. We would like to use honeycombs to decide the possible values of ν.


A 3-honeycomb with boundary values λ,µ,ν is shown in Figure 16. There are 9 internal edges in this honeycomb, of which three are determined by the boundary values. The remaining edges are labeled e1,...,e6 as shown. Writing the second condition in (10) for all vertices of the honeycomb, yields the following system of equations:

- (12)


- e1 + e2 = 1 ⇒ e2 = 1 − e1,
- e1 + e3 = 0 ⇒ e3 = −e1,


- e3 + e5 = 1 + ν3 ⇒ e5 = 1 + ν3 + e1, e5 + e6 = −ν2 ⇒ e6 = −1 − ν2 − ν3 − e1,
- e4 + e6 = ν1 ⇒ e4 = 1 + (ν1 + ν2 + ν3) + e1, e2 + e4 = −1 ⇒ e2 = −2 − (ν1 + ν2 + ν3) − e1.


The ﬁrst and last equations imply the trace equation ν1 + ν2 + ν3 = −3. We have eliminated all the e variables except e1.

Now we impose the nonnegativity constraints coming from the ﬁrst condition in (10). For example we can identify a conﬁguration of the leftmost type in Figure 15 that yields −1 − e3 ≥ 0. Using the fact that e3 = −e1 derived in (12) gives e1 ≥ 1. Proceeding like this will all conﬁgurations of edges shown in Figure 15 we arrive at the following inequalities:

1 ≤ e1 ≤ 2, e1 ≥ 2 + ν1 + ν2, e1 ≥ 1 + ν1, e1 ≥ −ν2, e1 ≥ 2 + ν2, e1 ≤ 3 + ν1 + ν2, e1 ≤ 2 + ν1.

In addition, we also have the chamber inequalities: ν1 ≥ ν2 ≥ −3 − ν1 − ν2. The possible values of ν are those that allow a value of e1 to exist given the above inequalities.

For a concrete example consider the following triple of symmetric matrices

 

 , B =

 

  and C = −A − B =

 

 

−2 0 0 0 −1 −1 0 −1 0

- 0 0 0
- 0 0 1 0 1 0


2 0 0 0 1 0 0 0 0

A =

√5

√5

which have eigenvalues λ = (1,0,−1), µ = (2,1,0) and ν = (−1+

2 , −1−

2 ,−2) respectively. Plugging in ν1 = −1+

√5

√5

2 and ν2 = −1−

2 into the inequalities we should arrive at a feasible value for e1 and indeed, we get 1+

√5 2 ≤ e1 ≤ 2 which is satisﬁable.

In this example, honey3 can be thought of as a cone in R6+9 with variables indexed by e1,...,e6 and the 9 variables in λ,µ,ν. It could be in R9+9 but recall that the variables associated to three of the bounded edges can be eliminated right away and expressed in terms of λ,µ,ν. The Horn cone is in R9. When we ﬁx λ and µ as we have done in this example, we are looking at a slice of honey3. The method above derives the inequality description of this slice.

3. Slack Operators

A fundamental question concerning lifts is to characterize when they exist. More formally, given a convex set C and a convex cone K, how can we decide whether C has a K-lift? In this section we focus on answering this basic existence question. In order to do this, we introduce a central tool for studying lifts of convex sets, namely the slack operator of the set. We will see that the existence of a K-lift of a convex set C is equivalent to the existence of a factorization of the slack operator of C through the cone K, and its dual cone K∗. This connection provides us with a useful algebraic handle on the geometric picture of cone lifts of convex sets.

- 3.1. Slack matrices. In the case of polyhedral lifts of polytopes, their existence was characterized in [Yan91]. A key component turns out to be the slack matrix of a polytope, which we introduce in this section.


There are two traditional ways of representing a polytope P. We can represent P as a V-polytope, i.e., as the convex hull of a minimal ﬁnite set of points, its vertices. We can also represent P as a H-polytope, i.e., as a bounded intersection of a ﬁnite number of closed half-spaces. It is a fundamental property of polytopes that these two representations are equivalent. Thus we would commonly either list all the vertices of P, or list a minimal set of aﬃne inequalities that cut out P, more precisely, one inequality per facet of P.

- Example 3.1. Consider the polytope P in R3, shown on the left in Figure 17, with the seven vertices (±1,±1,−1/2), (±1,−1,1/2) and (0,−1,3/2). This polytope can also be described by the seven aﬃne inequalities that cut it out:


1 − x ≥ 0, 1 + x ≥ 0, 1 + 2z ≥ 0, 1 + y ≥ 0, 1 − 2y − 2z ≥ 0, 1 − x −

- 1

- 2


- 1

- 2


y − z ≥ 0, 1 + x −

y − z ≥ 0.

![image 15](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile15.png>)

![image 16](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile16.png>)

Figure 17. Polytope P with seven vertices and seven facets, and its polar P◦.

The slack matrix of P combines the V and H descriptions of P into a single, less parsimonious, description. To do this we compute the slack, β − h v, of each vertex v in each facet deﬁning inequality h x ≤ β, obtaining a nonnegative matrix, with rows indexed by the facets and columns indexed by the vertices of the given polytope P. For instance, the slack matrix of the polytope P from Example 3.1 is the following 7 × 7 matrix:





- 2 2 2 0 0 0 1 0 0 0 2 2 2 1 0 0 2 0 0 2 4

- 0 2 0 0 2 0 0 4 0 2 4 0 2 0

3 2 2 1 0 0 0

- 1 0 0 3 2 2 0




SP =

.

 

 

The rows of SP are indexed by the facets of P in the order they are listed above. The columns of SP are indexed by the vertices of P in the following order:

- 1

- 2


- 1

- 2


- 1

- 2


- 1

- 2


- 1

- 2


3 2

- 1

- 2


),(−1,1,−

),(−1,−1,

),(1,−1,−

),(1,1,−

),(1,−1,

),(0,−1,

(−1,−1,−

).

Since the inequality deﬁning a facet of P is only deﬁned up to scaling by a positive number, the slack matrix SP is only deﬁned up to positive scaling of rows.

There is another interesting interpretation of the slack matrix, that brings the duality theory of polytopes to the forefront. Recall that given a polytope P ⊂ Rn with the origin in its interior, one can deﬁne its polar as the set

P◦ = {y ∈ Rn : x,y ≤ 1, for all x ∈ P} which is again a polytope. A fundamental result in the duality of polytopes is that there is a one-to-one correspondence between the vertices of P◦ and the facets of P, that sends vertex y of P◦ to the facet of P cut out by the inequality 1 − x,y ≥ 0. In our example, this means that P◦ is the polytope with vertices (±1,0,0), (0,0,−2), (0,−1,0), (0,2,2), (1,1/2,1) and (−1,1/2,1), shown on the right in Figure 17. Note that if the facet inequalities of P are scaled so that they are of the form 1 −  x,ai ≥ 0 (which is possible since the origin lies in the interior of P), then the transposed matrix S P is a slack matrix of P◦. With the language of duality, we can think of the

- slack matrix SP as the map 1 − x,y evaluated at the vertices of P◦ × P.


- 3.2. Nonnegative factorizations and Yannakakis’ theorem. In order to characterize the existence of polyhedral lifts for a polytope, we need to introduce the notion of nonnegative rank of a matrix. A nonnegative factorization of a nonnegative matrix M ∈ R+n×k is a pair of nonnegative matrices A ∈ Rm+×n and B ∈ Rm+×k such that M = A B. We say m, the inner dimension of the


product, is the size of the factorization, and deﬁne the nonnegative rank of M to be the smallest m for which a nonnegative factorization of M exists. Computing nonnegative ranks of matrices is a hard problem. Nonnegative factorizations and nonnegative rank have many interpretations and applications in diverse ﬁelds. An early survey can be found in [CR93], but there is a growing body of literature on this topic. Somewhat surprisingly, it turns out that this hard algebraic problem encodes the geometric problem of interest—the existence of polyhedral lifts.

- Theorem 3.2 (Yannakakis [Yan91]). The linear extension complexity of a polytope equals the nonnegative rank of its slack matrix.


Proof. Suppose a polytope P is cut out by the facet inequalities h i x ≤ βi for i = 1,...,f, and that SP = A B is a nonnegative factorization of its slack matrix, with inner dimension m. If we let ai, for i = 1,2,...,f, denote the columns of A, then we will show that

- (13) P = x ∈ Rn : ∃y ∈ Rm+ s.t. a i y = βi − h i x, for all i = 1,...,f .


This equality rewrites P as the projection of a polytope with m facets, or, equivalently, as the projection of a slice of Rm+. Hence P has a size m polyhedral lift.

To see why (13) holds, ﬁrst note that if p is in the right hand side we must have h i p = βi − a i y for some nonnegative y. Then, since a i y is nonnegative, it follows that h i p ≤ βi for all i, and so p ∈ P. On the other hand, if vj is a vertex of P, let y = bj be the corresponding column of B

which is nonnegative. Then a i y = a i bj = [SP]ij = βi − h i vj. Consequently vj, and indeed all vertices of P, are in the right hand side set. Since the right hand side set is convex, all of P must

be contained in it, and we have equality between the two sets. Suppose now that P can be written as the projection of a polytope Q with m facets. Take the

- slack matrix SQ and keep only columns that correspond to vertices that project to vertices of P,


and call this reduced m × v matrix SQ. Now any facet inequality on P can be pulled back by the projection to a valid inequality on Q, so by a version of Farkas Lemma, it can be written as a nonnegative combination of facet inequalities of Q. Record the coeﬃcients as column vectors, and

form a matrix A ∈ Rm+×f with those columns. Then SP = A SQ is a nonnegative factorization of SP with inner dimension m.

- Example 3.3. Revisiting Example 3.1, one can now ask for the linear extension complexity of the polytope P. We will prove that it is at least 6 in Example 5.2, using basic considerations about how lifts interact with facial structure that will be introduced in Section 5. To show that there is a lift with 6 facets, Theorem 3.2 tells us that it is enough to ﬁnd a nonnegative factorization of the

slack matrix SP, of size 6. One such factorization is 

 

- 2 2 2 0 0 0 1 0 0 0 2 2 2 1 0 0 2 0 0 2 4

- 0 2 0 0 2 0 0 4 0 2 4 0 2 0

3 2 2 1 0 0 0

- 1 0 0 3 2 2 0






 

=



 

- 2 0 0 0 0 1 0 0 0 0 2 1 0 0 0 2 0 4

- 0 0 2 0 0 0 0 4 0 2 0 0

2 1 0 0 0 0

- 0 1 0 0 2 0






 



 

1 1 1 0 0 0 0 1 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0 0 0 1



 

.

It is not hard to recover the lift Q from the factorization. We just start with an inequality description of P and use the factorization to write the lift as explicitly described in (13). We then simply use the equality constraints to eliminate some the variables y.

- Example 3.4. Recall that in Corollary 2.9 we have shown that the chain polytope chain(P) of a poset P has a small polyhedral lift. By Yannakakis’ Theorem, the slack matrix of chain(P) must have small nonnegative factorization, and we will now show that this is indeed the case.


The vertices of chain(P) are indexed by antichains of P. The facets, apart from the nonnegativities of the variables, are indexed by maximal chains in P. The facet inequality corresponding to a maximal chain C is of the form a∈C xa ≤ 1. As such, given an antichain A and a maximal chain C, the (C,A)-entry of the slack matrix is 0 if C and A intersect, and 1 otherwise.

In Corollary 2.9 we saw that chain(P) has a lift of the form (z,x) ∈ RP×P given by the inequalities

 

0 ≤ za, for all a ∈ P, 0 ≤ xai − xaj − zai, for all cover relations ai aj, 0 ≤ 1 − xa, for all a ∈ Pmax,



together with the equalities za = xa for a ∈ Pmin. Here we denote by Pmin and Pmax the set of minimal, respectively maximal, elements of P. We will also use E to be the set of all cover relations. The proof of Theorem 3.2 then gives us a way of extracting a factorization.

For every antichain A, we will assign a vector that is simply the preimage of its indicator vector χA through the lift, evaluated at each of the facet inequalities. The preimage of χA is (χA,χF) where F is the ﬁlter over A, i.e., the set of all elements greater than or equal to some element of the antichain. Evaluating this at each of the deﬁning inequalities above gives a vector (χA,y,w) ∈ {0,1}P×Pmin×E×Pmax with ya b = 1 if and only if a is in F \ A and b ∈/ F, and wa = 1 if and only if a ∈ Pmax \ F.

5 6 7 8

5 6 7 8

5 6 7 8

4

4

4

1 2 3

1 2 3

1 2 3

Figure 18. Example of an antichain (left), the corresponding ﬁlter (center), and the vector y of the factorization (right).

For example, in Figure 18 we can see an antichain A and its corresponding ﬁlter F in red and blue respectively. We would, in this case, have χA = (0,1,0,0,0,0,0,1), since the antichain contains only the nodes 4 and 8, while χF = (0,1,0,1,0,1,1,1). Setting z = χA and x = χF and looking at the inequalities above, the only interesting ones are those coming from the cover relations that will give us the vector y indicated in the ﬁgure. It is the set of edges in the Hasse diagram that go from a node not in the ﬁlter to a node that is in the ﬁlter but not in the antichain.

As for the facets, the nonnegativities of the variables in chain(P) lift to nonnegativities of the variables za in the lift, so we get the vector (ea,0,0) ∈ {0,1}P×E×Pmax where ea is 1 only in coordinate a. The inequality for a maximal chain C of the form a0 ≺ a1 ≺ ··· ≺ aN, lifts to 1 − Ni=0 zai ≥ 0, which is the sum of the inequalities corresponding to the maximal element in C and also all the cover relations. So we get a vector (0,χC,eaN) ∈ {0,1}P×E×Pmax, where χC is simply the indicator vector of which cover relations are in the chain.

Since we are following the proof of Theorem 3.2, these must necessarily form a factorization. It is not hard to see this independently. For the nonnegativity inequalities this is trivial, so we just have to see that given an antichain A and a chain C the inner product (χA,y,z),(0,χC,eaN) =

y,χC + zaN is 0 if the chain intersects the antichain and 1 otherwise. But y,χC is 1 if and only if the chain enters the ﬁlter outside of an antichain element, while zaN is 1 if and only if the chain never enters the ﬁlter at all, so they can never be 1 at the same time. If they are both 0 it means that the chain did enter the ﬁlter at an element of the antichain, and so we have indeed a factorization. This is a slightly diﬀerent factorization from the classical one originally given by Yannakakis [Yan91], but of roughly the same size.

- 3.3. The slack operator. Since we are interested in lifts of convex sets in general and not just polytopes, we will next need to generalize the notion of slack matrix to a more continuous object, the slack operator of a convex set. To simplify the exposition we will always consider compact convex sets with the origin in the interior, and will refer to these as convex bodies. Given a convex body C, its polar is


C◦ = {y ∈ Rn : x,y ≤ 1, for all x ∈ C}, which is again a convex body. Recall that an extreme point of a convex set C is a point in C that cannot be written as a convex combination of two distinct points of C, i.e., it is not in the relative interior of any line segment contained in C. We will denote the set of all extreme points of C as ext(C). Generalizing the notion of extreme point, a face of a convex set C is a convex subset F ⊆ C such that if any point in F is in the relative interior of a line segment contained in C, then the entire line segment is contained in F.

Consider again the function 1 − y,x but now with domain C◦ × C. In this domain, it is a nonnegative function, and imduces a one-to-one correspondence between points y˜ ∈ C◦ and linear inequalities valid over C, simply given by 1 − y,x ˜ ≥ 0. Since 1 − y,x is aﬃne in x and y (separately), and C and C◦ are compact, its value at any point is completely determined by its value on ext(C◦) × ext(C). We call the resulting map the slack operator of C.

Deﬁnition 3.5. Given a convex body C, its slack operator is the map sC : ext(C◦)×ext(C) deﬁned as sC(y,x) = 1 − x,y .

When C is a polytope, both C and C◦ have a ﬁnite number of extreme points, and we recover the slack matrix.

- Example 3.6. Let C = {(x,y) ∈ R2 : (1 + x)2(x − 1) + y2 ≤ 0, x ≥ −1}. This is a convex set bounded by a cubic curve. Its boundary is parametrized by


1 − v2,2v − v3 with v ∈ [−

√2,√2], and every boundary point is extreme. The polar of C is the convex hull of the cardioid deﬁned by 4x4 + 32y4 + 13x2y2 + 18xy2 − 4x3 − 27y2 = 0, as seen in Figure 19. Not every

![image 17](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile17.png>)

![image 18](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile18.png>)

Figure 19. Convex set C (left) and its polar C◦ (right) with extreme points highlighted.

boundary point of C◦ is extreme. The extreme boundary points are parameterized by 2 − 3u2 2 − u2 + u4

2u 2 − u2 + u4 with u ∈ [−

,

√2,√2 2 → R+ where sC(u,v) = 1 −

√2,√2]. The slack operator can be parametrized as sC : −

(2 − 3u2)(1 − v2) + 2u(2v − v3) 2 − u2 + u4

(2 − v2)(v − u)2 + (u2 − v2)2 u4 + (2 − u2)

. It is obvious from the last expression that sC is nonnegative on its domain.

=

- 3.4. Cone factorizations of slack operators. We deﬁne these general slack operators in the hope that there might be a geometric interpretation to their factorizations. However, to go from polyhedral lifts to more general conic lifts, we still need to generalize the idea of nonnegative factorizations. Before that, we need to quickly recall the deﬁnition of the dual of a cone. Given a cone K ⊆ R we deﬁne its dual to be K∗ = {y ∈ R : x,y ≥ 0 for all x ∈ K}. Here we may think of any inner product but we will always consider the usual Euclidean one. When working with cones of symmetric matrices this amounts to X,Y = tr(XY ), where tr is the usual matrix trace, also called the trace inner product.


Deﬁnition 3.7. Let K be a closed convex cone and K∗ its dual. Furthermore, let C be a convex body and sC its slack operator. A factorization of sC through K, or K-factorization of C, is a pair of maps A : ext(C) → K and B : ext(C◦) → K∗ such that sC(y,x) = A(x),B(y) for all x ∈ ext(C) and y ∈ ext(C◦).

This allows us to factorize the slack operator of a non-polyhedral sets C through a cone K.

- Example 3.8. Recall from Example 3.6 that the slack operator of the set C = {(x,y) ∈ R2 : (1 + x)2(x − 1) + y2 ≤ 0, x ≥ −1}


√2,√2]2 and equaling 1 −

is given by the function sC(u,v) with domain [−

(2 − 3u2)(1 − v2) + 2u(2v − v3) 2 − u2 + u4

2u2 + u4 − 4uv + 2v2 − 3u2v2 + 2uv3 2 − u2 + u4

. Here we are identifying the extreme points of both C and C◦ by the interval [−

=

√2,√2] since we have an explicit parametrization that we can think of as a labeling of the points. We claim that we can factor this operator through the cone S+3 . To see this, deﬁne

 

  =

 

 

 

  + (2 − v2)

 

 

 

 

1 0 1 − v2

1

1

- 0
- 1 v


- 0
- 1 v


- 0 2 − v2 v(2 − v2)
- 1 − v2 v(2 − v2) 1


- 0
- 1 − v2


- 0
- 1 − v2


A(v) =

and

 

  =

 

 

 

  .

u2 − 1 2 −u u2 − 1 u2 − 1 −u u2 − 1 u2 −u

u2 − 1 −u 1

u2 − 1 −u 1

1 2 − u2 + u4

1 2 − u2 + u4

B(u) =

u2 − 1 −u 1

√2,√2], and sC(u,v) = A(v),B(u) , we have the claimed factorization.

Since these matrices are positive semideﬁnite for u,v ∈ [−

As in the Yannakakis setting of polytopes, we can show that the existence of lifts and the existence of factorizations are equivalent even in this generalized setting of arbitrary convex bodies and closed convex cones. Recall that a convex set C has a K-lift, into a closed convex cone K, if we can write it as C = π(K ∩ L), where π is a linear map and L an aﬃne subspace. We will additionally say that C has a proper K-lift if L intersects the relative interior of K. Note that if C has a K-lift it always has a proper lift to some face of K, so the assumption of properness is not a very strong one.

- Theorem 3.9. [GPT13] If a convex body C has a proper K-lift then its slack operator, sC, has a K-factorization. Reciprocally, if sC has a K-factorization then C has a K-lift. Proof. The proof is just a reworking of the proof of Theorem 3.2.


Let A and B form a K-factorization of the slack operator sC. Then one can check that C = {x ∈ Rn : ∃X ∈ K s.t. X,B(y) = sC(y,x), for all y ∈ ext(C◦)},

since the equalities force sC(y,x) ≥ 0 for all y ∈ ext(C◦) guaranteeing that the right hand side is contained in C, while plugging in X = A(x) shows that ext(C), hence C, is contained in the right

hand side. Although there are potentially inﬁnitely many linear equalities, they necessarily cut out a ﬁnite dimensional space, and we can use them to eliminate the variable x and explicitly get C as a projection of a slice of K.

Suppose now C has a K-lift, i.e., C = π(K ∩ L), for some linear map π and aﬃne space L. For x in ext(C), deﬁne A(x) to be any element in the preimage π−1(x) ∩ (K ∩ L). For y ∈ ext(C◦), one can pull back the inequality 1 − x,y by π to a valid inequality on K ∩ L. The hypothesis that L intersects the interior of K (Slater’s condition) can be shown to guarantee that any valid inequality on K ∩ L, when restricted to L equals Y,−  for some Y ∈ K∗. Pick such a Y as B(y). Then one can check that A(x),B(y) = sC(y,x) as intended.

The cones K that we will mostly be interested in are nonnegative orthants and positive semidefinite cones. In those cases, their special structure allows us to omit the properness condition from the statement of Theorem 3.9 (see [GPT13, Corollary 1]).

- Example 3.10. Let us consider again the convex set C given in Example 3.8. Since the slack operator is factorizable through S+3 , Theorem 3.9 implies that C must have a S+3 -lift. In fact

C =

 



(x,y) :

 

1 0 x 0 1 + x y x y 1

  0

 



.

Indeed, check that the nonnegativity of the principal minors of the above matrix gives the polynomial inequalities deﬁning C. Moreover, the symmetry of the existence of factorizations and the self-duality of the psd cone implies that the polar C◦ must also have a S+3 -lift. One can show that

C◦ =

 



(z,w) : ∃z1,z2,z3 ∈ R s.t.

 

1 − z3 − z1 z2 −(z + z3)/2

z2 z3 −w/2 −(z + z3)/2 −w/2 z1

  0

 



.

An important basic property of slack operators is that for any convex body C we have sC(y,x) = sC◦(x,y), in other words the slack operator of C◦ is the transpose of the slack operator of C. This follows directly from the deﬁnition, since (C◦)◦ = C for convex bodies. Furthermore it also follows directly from the deﬁnition that sC has a K-factorization if and only if its transpose has a K∗factorization. An immediate consequence of Theorem 3.9 is that C has a K-lift if and only if C◦ has a K∗-lift.

Moreover, note that if a convex body C can be written as a linear image of some convex set Q, i.e., C = π(Q), then C◦ ∼= Q◦ ∩ ker(π)⊥, which means that we can write C◦ as a linear slice of the polar of its lift. In the case of polytopes, this has a nice interpretation. We saw that if P has a Rm+-lift then P◦ also has a Rm+-lift. This means that if P is the image of a polytope with m facets, then P◦ is a slice of a polytope with m vertices.

- Example 3.11. We have seen in, Figure 4, that the regular octagon is the projection of a polytope with 6 facets. Since the regular octagon is self polar, we then get that it must also be a section of a polytope with 6 vertices. Figure 20 shows the regular octagon as a slice of an octahedron.


One should also point out that there is a simple extension of Theorem 3.9 so that it covers approximations of sets, instead of only exact representations. To state it we need to introduce the generalized slack operator. Given two convex bodies C ⊆ D we deﬁne the generalized slack operator of the pair (C,D) to be sC,D : ext(D◦) × ext(C) → R+ given by sC,D(y,x) = 1 − x,y . A look at the proof of Theorem 3.9 shows that it immediately generalizes to the following result.

- Proposition 3.12. Let C and D be a pair of convex bodies with C ⊆ D. If there is a convex set B such that B has a proper K-lift and C ⊆ B ⊆ D then sC,D has a K-factorization. Reciprocally, if sC,D has a K-factorization then there exists a convex set B such that B has a K-lift and C ⊆ B ⊆ D.


![image 19](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile19.png>)

Figure 20. The regular octagon as a minimal linear slice of an octahedron.

By setting D = (1 + ε)C we obtain a powerful tool to study approximability of a given set by sets with small lifts.

- 3.5. Bregman divergence as a slack operator. An important notion that is closely related to that of slack operator is the Bregman divergence of a convex function, which was brieﬂy mentioned in Section 2.3 and is widely used in applications. The Bregman divergence can, under some mild assumptions, be seen as the slack operator of the epigraph of the corresponding convex function, while slack operators can be seen as special cases of a nonsmooth version of the Bregman divergence, tying the two notions together.


Following [BB97], let f : Rn → R be a closed convex proper function whose domain has nonempty interior. If f is diﬀerentiable in the interior of its domain we deﬁne its Bregman divergence as the function Df : Rn × int(dom(f)) → [0,+∞) given by

Df(x,y) = f(x) − f(y) −  ∇f(y),x − y .

In other words, Df(x,y) is the diﬀerence between f(x) and the value at x of the linear approximation to f around y. The convexity of f implies that Df(x,y) ≥ 0.

- Example 3.13. If we take f(x) = x Qx to be a convex quadratic function, then Df(x,y) = x Qx − y Qy − 2y Q(x − y) = (x − y) Q(x − y)

since Q is a symmetric matrix. In particular, if f(x) = x 2 we have Df(x,y) = x − y 2.

It turns out that the Bregman divergence is a slack operator of sorts for convex functions, where Fenchel duality replaces polarity of convex sets. Recall that the Fenchel conjugate of f is the function f∗ : Rn → R deﬁned by

f∗(y∗) = sup{ x,y∗ − f(x) | x ∈ Rn}. The function f∗ is closed and convex and Fenchel’s inequality says that f(x)+f∗(y∗) ≥ x,y∗ . We will refer to F(x,y∗) := f(x) + f∗(y∗) −  x,y∗ as the slack in the Fenchel inequality. Using simple properties of Fenchel conjugation one gets that Df(x,y) = F(x,∇f(y)). As such, the Bregman divergence is essentially a slack, but of duality of convex functions rather than convex sets.

In fact, if f is well-behaved, namely if f is a convex function of Legendre type, (smooth and strictly convex in its domain, and the limits of  ∇f(x) as x approaches the boundary of the domain through its interior is +∞), then the map y → y∗ := ∇f(y) is an isomorphism from the interior of the domain of f to the interior of the domain of f∗. In that case, the Bregman divergence and the slack of the Fenchel inequality are just reparametrizations of each other. For more details, see [Roc70, Section 26].

- Example 3.14. The function f(x) = ex is a strictly convex smooth function with domain R. Its conjugate f∗ has domain in the nonnegative reals, and is given by f∗(0) = 0 and f∗(z) = z ln(z)−z


for z > 0. The Fenchel inequality becomes F(x,z) = ex + z ln(z) − z − xz ≥ 0. The Bregman divergence is

Df(x,y) = F(x,f (y)) = F(x,ey) = ex − ey + (y − x)ey.

As above, we can think of the function F as the map x0 + y0 − x,y with domain the product of the graph of f and the graph of f∗. When extended to the epigraphs, this operator creates a one-to-one correspondence between points in the epigraph of a function and aﬃne under-estimators of the other function, as illustrated in Figure 21.

![image 20](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile20.png>)

![image 21](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile21.png>)

Figure 21. The epigraphs of f(x) = ex and f∗(z) = z ln(z)−z, with some linear underestimators of f and corresponding points in the epigraph of f∗ marked.

For instance, the point (2,0) in epi(f∗) gives rise to the inequality x0 − 2x ≥ 0, while the point (1,−1), that is an extreme point of epi(f∗) gives rise to the inequality x0−1−x ≥ 0, and so on.

This illustrates that for a smooth convex function of Legendre type, its Bregman divergence is, in a very strong sense, the same as the slack operator of its epigraph. The only diﬀerence is that epi(f) and epi(f∗) are not actually polar to each other, having instead a diﬀerent duality relation.

Interestingly, not only can we think of the Bregman divergence as a slack operator, we can conversely think of slack operators as straightforward generalizations of the Bregman divergence. For any closed convex set C, consider its indicator function ιC(x) given by ιC(x) = 0 if x ∈ C and +∞ otherwise. This is a proper closed convex function, and its Fenchel conjugate is the support function of C, given by hC(y) = supx∈C x,y . Since ιC(x) is not a smooth convex function, its usual Bregman divergence is not deﬁned. However, there are many generalizations of the Bregman divergence to the nonsmooth case. A simple way of doing this is to think of Bregman divergence as the aﬃne operator x0 + y0 −  x,y applied to epi(ιC) × epi(hC). We still have a correspondence between points in the epigraph of hC and valid inequalities on the epigraph of ιC. Restricting to the extreme points of epi(ιC), which correspond to the extreme points of C, and a representative of every extreme ray of the cone epi(hC), recovers the slack operator of C (up to scaling). An advantage of this viewpoint is that we can remove the technical condition of requiring 0 to be in the interior of C.

4. Constructions of Lifts

Is there a systematic way to construct lifts for convex bodies? In this section we will try to answer this question, informed by the factorization theorem from the previous section.

- 4.1. Spectrahedral lifts and sums of squares. We start by restating the factorization theorem (Theorem 3.9) in the special case of spectrahedral lifts, which will be our main focus in this section.


- Theorem 4.1. Let C = conv(X) be a convex body. Then C has a spectrahedral lift of size m if,


and only if, there exists a map A : X → S+m such that the following holds: for any ∈ C◦, there exists a B ∈ S+m such that

- (14) 1 − (x) = tr(A(x)B) ∀x ∈ X.

Remark 4.2. Throughout this section we use the notation for elements of C◦, to emphasize that these are linear forms deﬁned on the ambient space where C lives. We also write (x) (as opposed to the bracket notation  ,x ) for the evaluation of at some element x.

Recall that the slack operator of C is indexed precisely by pairs ( ,x) ∈ ext(C◦) × ext(C) and

the associated entry in the matrix is 1 − (x) ≥ 0. Equation (14) is nothing but a S+m factorization of this slack operator.

It is useful to think of Equation (14) as a certiﬁcate of nonnegativity of the aﬃne function 1− (x) on the set X. Indeed the right-hand side of (14) is “obviously” nonnegative as it is the inner product of two positive semideﬁnite matrices. That (14) is a certiﬁcate of nonnegativity becomes clearer if we factorize A(x) as A(x) = F(x)F(x) and B = DD . (Such a factorization is possible since A(x),B 0.) Then we have, for any x ∈ X

- (15) 1 − (x) = tr(A(x)B) = tr (F(x) D) F(x) D = 1≤i,j≤m

Mij(x)2

where M(x) = F(x) D. Equation (15) shows that 1 − (x) is a sum of squares of the entries of M(x). In turn, the entries of M(x) are linear combinations of the entries of F(x). We have thus shown the following: if C = conv(X) has a spectrahedral lift of size m, then there is a subspace V of functions on X with dim(V ) ≤ m2 such that the following is true:

(*-SDP)

For any valid linear inequality (x) ≤ 1 on X, there exist functions hk ∈ V s.t. 1 − (x) = k hk(x)2 for all x ∈ X.

The subspace V here is precisely V = span{Fij : 1 ≤ i,j ≤ m}, where we think of each Fij as a function on X. (We will look at the nature of these functions later in this section.)

One can also prove a converse of the previous statement. This is the object of the next proposition, showing how to construct a lift from a subspace satisfying (*-SDP). Note that the statement below is not an exact converse, as it gives a spectrahedral lift of size dim(V ) instead of dim(V ). The reason has to do with the rank of the map A(x) which is rank-one in the construction (16) below, whereas it can be of higher rank in Theorem 4.1.

- Proposition 4.3. Let C = conv(X) be a convex body. Assume there exists a subspace V of functions on X such that (*-SDP) is true. Then C has a spectrahedral lift of size dim(V ).


Proof. We construct a positive semideﬁnite factorization of the slack operator of C. Let m = dim(V ), f1,...,fm be a basis of V , and F(x) = [f1(x),...,fm(x)] . Deﬁne

- (16) A(x) = F(x)F(x) ∈ S+m.


Let ∈ C◦ so that 1 − (x) ≥ 0 for all x ∈ X. We want to show that there exists B ∈ S+m such that 1 − (x) = tr(A(x)B) for all x ∈ X. We know by (*-SDP) that there exist functions hk ∈ V such that 1 − (x) = k hk(x)2 for x ∈ X. Since f1,...,fm form a basis of V , we know there exist vectors bk ∈ Rm such that hk(x) = b k F(x). Then

hk(x)2 =

(b k F(x))2 = tr F(x)F(x) B

1 − (x) =

k

k

where B = k bkb k ∈ S+m. This completes the proof.

- Proposition 4.3 reduces the problem of constructing a spectrahedral lift of C to that of ﬁnding a


subspace V of functions such that (*-SDP) holds. We now list some examples of lifts constructed in this way.

- Example 4.4 (Elliptope). Consider the convex body C = [−1,1]2 with extreme points X = {−1,+1}2. Deﬁne the subspace V = span(1,x,y) of aﬃne functions, and consider the valid linear inequality x ≤ 1 on C. Note that we can write


- 1

- 2


(1 − x)2 ∀(x,y) ∈ X

1 − x =

where we used the fact that x2 = 1. Similarly one can check that the other facet inequalities of C (namely 1 + x ≥ 0 and 1 ± y ≥ 0) are sums of squares from functions in V . It thus follows that C has a spectrahedral lift of size dim(V ) = 3. Indeed one can verify that

 

 

 

  0

1 x y

(x,y) ∈ R2 : ∃z ∈ R,

- x 1 z
- y z 1


### (17) C =

.





This is precisely the example of the three-dimensional elliptope seen in the introduction (see Figure 5(left)) which projects onto the two-dimensional square.

- Example 4.5 (Convex hull of rational curves). Consider a plane curve X ⊂ R2 having a rational parametrization, X = {(x(t),y(t)) : t ∈ R} where x(t),y(t) are rational functions, i.e., x(t) = a(t)/q(t), y(t) = b(t)/q(t) where we assume that q(t) > 0 for all t ∈ R and max(deg a,deg b) ≤ deg q. We can show that clconv(X) (where cl denotes the closure) has a spectrahedral lift of size at most deg(q)/2 + 1 [Par06, Hen11]; we will show this by exhibiting a subspace of functions V such that property (*-SDP) holds for X.


We ﬁrst deﬁne a function t : X → R that gives the “time” coordinate of any point in X in the parametrization (x(t),y(t)); namely for any (x0,y0) ∈ X let t(x0,y0) = t0 ∈ R be such that (x(t0),y(t0)) = (x0,y0) (if multiple such t0 exist, an arbitrary choice is made so that t is singlevalued). Consider now the subspace V of bivariate functions of the form

deg(q)/2

t(x,y)i q(t(x,y))

### (18) h(x,y) =

ci

i=0

where the ci are arbitrary coeﬃcients. Note that dim(V ) = 1 + deg(q)/2.

We claim that any valid linear inequality on clconv(X) is a sum of squares from V . Indeed, assume we have a linear form such that 1 − (x) is nonnegative on X, i.e., 1 − (x(t),y(t)) ≥ 0 for all t ∈ R. Using the fact that x(t) = a(t)/q(t) and y(t) = b(t)/q(t) this gives:

q(t) − (a(t),b(t)) ≥ 0 ∀t ∈ R. Note that q(t) − (a(t),b(t)) is a (univariate) polynomial of degree at most deg q. It is a well known simple fact that univariate polynomials are nonnegative in the real line if and only if they are sums of squares (see Chapter 3 of [BPT13] for an overview on sums of squares), therefore q(t) − (a(t),b(t)) must be a sum of squares of some polynomials hk(t) ∈ R[t] of degree at most (deg q)/2, i.e.,

hk(t)2. Evaluating at t = t(x,y) and dividing by q we get

q(t) − (a(t),b(t)) =

k

2

hk(t(x,y)) q(t(x,y))

1 − (x,y) =

∀(x,y) ∈ X.

k

Since the functions (x,y)  → hk(x,y)/ q(t(x,y)) belong to V we have shown what we wanted.

| |
|---|


0.4

0.2

0.0

- -0.4
- -0.2


-0.2 0.0 0.2 0.4 0.6 0.8 1.0 1.2

Figure 22. The Piriform curve deﬁned by y2−x3+x4 = 0. This is a rational curve and so the convex hull of this curve has a spectrahedral lift. However property (*-SDP) is not true for any subspace V consisting of polynomials. (Note that functions of the form (18) are not polynomials.) This example was considered in [GN11, Example 4.4].

- 4.2. Hierarchies. Consider the case where C is the convex hull of a set deﬁned using polynomial equations. A natural choice of subspace V in this setting is the space V = Vk of polynomials of degree at most k, where k is a certain ﬁxed integer. If property (*-SDP) holds with such Vk then we get a spectrahedral lift of conv(X) of size dim(Vk). This spectrahedral lift is precisely the lift produced by the Lasserre/theta-body method, see [Las09, GPT10].


We note that it is possible for a convex body C to have a spectrahedral lift, and yet not verify property (*-SDP) for any subspace of polynomials V (of arbitrary degree). For example, consider the curve deﬁned by the equation y2 − x3 + x4 = 0 and shown in Figure 22; this curve is known as the Piriform curve. Because of the singularity at the origin, one can show that the Lasserre/theta body hierarchy for this curve is not exact at any ﬁnite level k, see [GT12, Theorem 9]. However the convex hull of this curve has a SDP representation since the curve has a rational parametrization, namely it can be shown that it is parametrized by

- x(θ) = 1+sin(2 θ)

- y(θ) = cos(θ)(1+sin(4 θ)),


which can be turned into a rational parametrization using cos(θ) = 11+−tt22 and sin(θ) = 1+2tt2.

- Example 4.6 (k-level polytopes). A polytope P is called k-level if every facet-deﬁning linear function of P takes at most k diﬀerent values on the vertices of the polytope. Said diﬀerently, for every aﬃne hyperplane H deﬁning a facet of P, all the vertices of P lie in at most k diﬀerent translates of H. See Figure 23 for examples of 2 and 3-level polytopes in R3. One important example of 2-level polytope is the stable set polytope of perfect graphs (see Section 2.2, Theorem


- 2.11).


![image 22](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile22.png>)

![image 23](<2020-fawzi-lifting-simplicity-concise-descriptions_images/imageFile23.png>)

Figure 23. Left: examples of 2-level polytopes. Right: a polytope that is 3-level but not 2-level. Figure from [GT12].

One can prove that if P is a k-level polytope, then P admits a spectrahedral lift of size at most

n+k−1

k−1 = dim(Vk−1) where Vk−1 is the space of polynomials of degree at most k −1 in n variables. To do this we will prove that (*-SDP) holds with V = Vk−1.

Indeed, let X be the set of vertices of the polytope, and assume that 1 − (x) ≥ 0 for all x ∈ X.

We need to show that there exist hi ∈ V such that 1 − (x) = i hi(x)2 for all x ∈ X. Note that by Farkas’ Lemma, 1 − (x) is a nonnegative combination of facet deﬁning inequalities, so it

is enough to show that any facet inequality can be written as a sum of squares. We can therefore assume that 1− (x) ≥ 0 deﬁnes a facet which, since P is k-level, implies that {1 − (x) : x ∈ X} = {a1,a2,...,ak} for some nonnegative numbers ai ∈ R. Consider a univariate polynomial r ∈ R[t] of degree k − 1 such that r(ai) = √ai (e.g., constructed using the Lagrange interpolation formula), and let h(x) = r(1− (x)) be the evaluation of r at 1− (x). Since deg r ≤ k −1 we have h ∈ Vk−1. Note that for any x ∈ X we have 1 − (x) = r(1 − (x))2 = h(x)2 where we used the fact that

- 1 − (x) ∈ {a1,...,ak} and that r(ai)2 = ai for all i = 1,...,k. We have thus shown that this choice of subspace works. An illustration of this construction is shown in Figure 24 in the case of the regular hexagon.


x = cos(π/6)

1.0

0.5

0.5 1.0 1.5 2.0

Figure 24. Left: The convex hull of the regular hexagon is a 3-level polytope. The levels of the facet inequality cos(π/6) − x ≥ 0 are {0,a1,a2} = {0,cos(π/6),2cos(π/6)}. Right: the polynomial r(t) of degree 2 such that r(0) = 0, r(a1) = √a1, r(a2) = √a2. Any facet inequality of the regular hexagon is a sum of squares of quadratic polynomials. One can show that this gives a spectrahedral lift of the regular hexagon of size 5.

- 4.3. Symmetric convex bodies. In many cases, the convex body C ⊂ Rn we are interested in has some symmetries. This means that there are certain linear invertible transformations of Rn that leave C invariant. The symmetry group (or automorphism group) of C, is precisely the set of such transformations:


Aut(C) = {T ∈ GL(Rn) : T(C) = C}. For example the automorphism group of the regular n-gon in the plane is the dihedral group and consists of 2n elements. When constructing a lift of the convex body C, one may require that the lift “respects” the symmetry of C. Such lifts are called symmetric or equivariant lifts and have been considered since the work of Yannakakis [Yan91]. Having an equivariant spectrahedral lift of a convex body C has a very natural interpretation in terms of the subspace V of functions in (*-SDP). Finding an equivariant lift of C = conv(X) amounts to ﬁnding a subspace V of functions on X that is invariant under the action of Aut(C). Here the action of Aut(C) on functions X → R is the natural one deﬁned by (g·f)(x) = f(g−1x) for g ∈ Aut(C) and x ∈ X. A question the reader may ask is whether there is beneﬁt in breaking symmetry when constructing lifts of convex bodies. More precisely, given a symmetric convex body, can non-equivariant lifts be much smaller than their equivariant counterparts? It turns out that the answer is yes, and the gap can be very large. Kaibel et al. [KPT12] showed the existence of polytopes (Pn) that have a nonequivariant polyhedral lift

of polynomial size in n, and yet any equivariant lift has size at least nΩ(logn). Also it was shown in [FSP15] that the even parity polytope has no polynomial-size equivariant spectrahedral lift, despite having a linear size non-equivariant one (cf. Section 2.1).

- 4.4. Linear programming lifts. We have so far only discussed the case of spectrahedral lifts. In this concluding paragraph, we brieﬂy discuss polyhedral lifts. It can be shown via the slack matrix factorization theorem, that, for a ﬁnite set X, a polytope P = conv(X) has a polyhedral lift of size


m if, and only if, there are m nonnegative functions a1,...,am : X → R+ such that the following

is true: (*-LP)

For any valid linear inequality (x) ≤ 1 on X, there exist b1,...,bm ≥ 0 s.t. 1 − (x) = mi=1 biai(x) for all x ∈ X. As such, whereas the task of constructing a spectrahedral lift corresponds to ﬁnding a subspace V

such that (*-SDP) holds, constructing an LP lift requires ﬁnding a ﬁnite set of functions a1,...,am : X → R+ such that (*-LP) is true. There are some settings where a natural set of functions can be considered. Assume that X ⊂ {0,1}n is a subset of the Boolean hypercube and is described using polynomial inequalities, i.e.,

- (19) X = {x ∈ {0,1}n : g1(x) ≥ 0,...,gk(x) ≥ 0},

where g1,...,gk are polynomials in x. Such a setting covers many combinatorial optimization problems. In this case one can consider the following family of functions

- (20) aT,I,γ(x) = i∈T


k

gi(x)γi,

(1 − xi)

xi

i=1

i∈I\T

where T ⊆ I ⊂ {1,...,n} and (γ1,...,γk) ∈ Nk. The functions (20) are clearly nonnegative on X. Many of the early lift-and-project methods in combinatorial optimization (Sherali-Adams [SA90] or Lov´sz-Schrijver [LS91]) can be understood in this framework and correspond to choosing functions ai of the form (20).

5. Obstructions and lower bounds

Given a convex body C and a closed convex cone K, how can we show that C does not have a K-lift? In other words, what properties of C are obstructions to C having a K-lift? When K comes from a cone family, such as Rm+ or S+m, we typically phrase things in more quantatitive language, aiming to ﬁnd lower bounds on the size of the corresponding lift.

For polytopes, the study of lower bounds on the size of polyhedral and spectrahedral lifts has received considerable attention in recent years. (See Section 6 for more information and references.) In this section, we focus on cases where C is not a polytope. In this more general setting, even deciding whether C has a K-lift for some K in a given cone family (such as positive semideﬁnite cones of any ﬁnite size) can be very challenging.

The characterization of the existence of lifts in terms of factorizations of the slack operator, discussed in Section 3, is a key tool to ﬁnding obstructions. This connection allows us to conclude the non-existence of K-lifts by showing that it is impossible to ﬁnd a K-factorization of the slack operator. Crucially, we can often ﬁnd such obstructions by considering only very coarse features of the slack operator. For instance, we may consider only the pattern of zeros and non-zeros of the slack operator, capturing only which extreme points lie on which supporting hyperplanes.

As a concrete example, consider the following result of Goemans about the size of polyhedral lifts of polytopes. We use this as a starting point when discussing obstructions to lifts of convex bodies that are not polytopes throughout this section.

- Proposition 5.1 ([Goe15]). Assume C is a polytope with v extreme points. Then any polyhedral lift of C has size at least log2 v .


The bound of Goemans can be tight (up to a constant multiplicative factor). One family of examples showing this are the regular N-gons in the plane. These have N extreme points and are know to have polyhedral lifts of size either 2 log2 N or 2 log2 N − 1 depending on the value of N [VGG17]. These polyhedral lifts are improved versions of a lift of the regular 2n-gon of size

- 2n + 4 due to Ben-Tal and Nemirovski [BTN01b]. Another family of examples showing that Goemans’ bound is tight, comes from the permuta-


hedra Πn. Recall from Example 1.2, that for each n, Πn is the convex hull of all permutations of (1,2,...,n). As such Πn has n! extreme points. Goemans’ lower bound therefore tells us that any polyhedral lift of Πn has size at least nlog2(n/e). By comparison, the Birkhoﬀ polytope lift of the permutahedron from Example 1.2 has size O(n2). Goemans constructed a polyhedral lift of the permutahedron of size O(nlog(n)), and used Proposition 5.1 to show that this lift cannot be substantially reduced in size [Goe15].

Goemans’ lower bound also implies the intuitively obvious fact that a convex body with inﬁnitely many extreme points cannot have a polyhedral lift. In other words, having inﬁnitely many extreme points is an obstruction to the existence of a polyhedral lift. To see why, we can consider the contrapositive of Proposition 5.1. This tells us that if a convex body has a polyhedral lift with at most m facets, then it has at most 2m extreme points.

In the rest of this section, we consider generalizations of Proposition 5.1 in two directions. In Section 5.1, we view Goemans’ bound as being about obstructions to lifts arising from the complexity of the facial structure (in this case, the number of vertices) of C. In particular, we discuss other obstructions based on facial structure that are applicable even when C is not a polytope. In terms of the slack operator, focusing on facial structure essentially corresponds to considering only its pattern of zeros and non-zeros. In Section 5.2, we view Goemans’ bound as being about obstructions to lifts arising from the algebraic complexity of the boundary of C◦. In the case of Goemans’ bound the number of vertices of C is the number of facets of C◦, which is also the smallest degree of a polynomial vanishing on the boundary of C◦. In particular, in Section 5.2 we discuss other obstructions of an algebraic nature.

- 5.1. Obstructions based on facial structure. The faces (see Section 3 for the deﬁnition) of a


convex set are partially ordered by inclusion. Throughout this section we let FC denote the poset of faces of C. If C = π(Q) is the projection of a convex set Q, then the preimage under π of any face of C is a face of Q. This observation can be used to ﬁnd lower bounds on the size of lifts.

- Example 5.2. Consider again the regular octagon for which we see two polyhedral lifts with six facets in Figure 4. In each case, the preimage (under the projection) of each vertex of the octagon is a face of the lift. Moreover, a vertex of the lift can belong to at most one such preimage face. This implies that any polyhedral lift of an octagon must have at least 8 vertices. Since any polytope with 5 or fewer facets has at most six vertices, it follows that any polyhedral lift of an octagon has size at least 6.


In general, if Q is a lift of C then there is an order embedding φ : FC → FQ, i.e., a map that satisﬁes F ⊆ F if and only if φ(F) ⊆ φ(F ) for any F,F ∈ FC. Furthermore, if Q = K∩L for some closed convex cone K and aﬃne space L, then there is a natural order embedding ψ : FQ → FK which sends a face F of Q to the minimal face of K containing F. Overall, then, the composition ψ ◦ φ : FC → FK gives an order embedding from the face poset of C to the face poset of K. For the lift on the right of Figure 4, the embeddings φ and ψ, and their composition, are all illustrated in Figure 25.

Since lifts induce embeddings of face posets, we can ﬁnd obstructions to the existence of K-lifts by ﬁnding obstructions to embedding the face poset of C in the face poset of K.

- 5.1.1. Obstructions from counting faces. If the face poset of the cone K is ﬁnite, then we can use the order embedding together with a counting argument to obtain obstructions to the existence of


Figure 25. Poset embeddings implied by the lift P = π(Q) = π(R6+ ∩ L) of the regular octagon P shown on the right in Figure 4. Left: Hasse diagram of FP. Center: Hasse diagram of FQ with the white nodes showing the embedding of FP. Right: Hasse diagram of FR6

with grey nodes showing the embedding of FQ and white nodes showing the embedding of FP.

+

K-lifts. This approach makes sense in the case of polyhedral lifts, where K = Rm+. The face lattice

- of Rm+ is the Boolean lattice of order m. A counting argument gives a slight generalization of the bound of Goemans.


- Lemma 5.3. If C has an Rm+-lift, then m ≥ log2(|FC|) .

Proof. If C has a Rm+-lift then |FC| = |(ψ ◦φ)(FC)| ≤ 2m since ψ ◦φ is injective and the cardinality of the Boolean lattice of order m is 2m. 5.1.2. Obstructions from chains of faces. Any order embedding maps a chain of a certain length to a chain of the same length, giving the following basic obstruction to the existence of lifts.

- Lemma 5.4. If C is a convex body (of dimension at least one) and C has a K-lift for a closed convex cone K, then the longest chain of faces in C is strictly smaller than the longest chain of faces in K.


Proof. Since C is a convex body, it is compact. Since C has dimension at least one and is compact, it is not a cone. As such, if C = π(K ∩L) then 0 ∈/ L. Therefore, any chain of faces in C is mapped, by the order embedding φ, to a chain of faces of the same length in K that does not include the face {0}. In particular a longest chain of faces in C is mapped to a chain of faces in K that is not of maximum length.

Since the empty set is always a face of a convex set, we focus the discussion on chains of nonempty faces. Example 5.5 (Convex hull of a cardiod). Consider the convex body

C = conv{(x,y) ∈ R2 : 4x4 + 32y4 + 13x2y2 + 18xy2 − 4x3 − 27y2 = 0}, the convex hull of the cardiod shown on the right in Figure 19. In Example 3.10 we saw that this convex body has a S+3 -lift.

The convex hull of a cardiod has a length three chain of non-empty faces given by

{(−1, √12)} ⊆ [(−1,−√12),(−1, √12)] ⊆ C. From Lemma 5.4, we know that if the convex hull of a cardiod is to have a K-lift, then K must have a chain of non-empty faces of length at least four. Since S+2 does not have a chain of non-empty

faces of length four, we can conclude that the convex hull of a cardiod does not have an S+2 -lift. In fact, for any smooth convex cone, the longest chain of non-empty faces has length three (since the only faces are {0}, the extreme rays, and the cone itself). As such, we can conclude that the convex hull of the cardiod does not have a K-lift where K is a smooth convex cone.

Obstructions based on the length of chains of faces can be used to give simple lower bounds on the size of spectrahedral lifts of polytopes. Corollary 5.6 ([GPT13]). Any spectrahedral lift of a polytope C has size at least dim(C) + 1.

Proof. For a polytope C, the dimension strictly increases along chains of faces, and any maximal chain of non-empty faces has length 1+dim(C). On the other hand, the longest chain of non-empty faces in S+m has length at most m + 1. This is because the rank (which is constant on the relative interior of faces of S+m) strictly increases along chains of faces, and the rank is zero on the face {0}.

The polytopes C that have spectrahedral lifts of size dim(C) + 1 are known as psd-minimial polytopes [GRT13]. These are the polytopes for which the lower bound of Corollary 5.6 is tight. Any 2-level polytope (see Section 4.6) is psd-minimal. In particular, the stable set polytopes of perfect graphs from Section 2, are examples of psd-minimal polytopes. There is a complete classiﬁcation of psd-minimal polytopes in dimensions up to four [GPRT17], obtained by a careful study of certain algebraic properties of their slack matrices.

- 5.1.3. Obstructions based on neighborliness. We now consider more elaborate features of the facial structure of convex bodies that, if present, can rule out much larger classes of lifts. These features build on the idea of neighborly polytopes.


- Deﬁnition 5.7. A convex polytope C is k-neighborly if, for every subset of k extreme points of C, the convex hull of that set forms a face of C.

Perhaps the most celebrated examples of neighborly polytopes are the cyclic polytopes [Gal63]. These are obtained by taking the convex hull of v points on the moment curve (t,t2,...,tn). Neighborly polytopes are extremal in the sense that among all n-dimensional polytopes with v vertices, the neighborly polytopes have the largest number of faces in each dimension. This property makes

- them central objects in polyhedral combinatorics. They also provide a geometric interpretation of key results in other contexts, such as compressive sensing [DT05].


Any face of a polytope is exposed by a linear functional. As such, a convex polytope C is kneighborly if, and only if, for every I ⊆ ext(C) with |I| = k, there is a linear functional I ∈ C◦ that exposes exactly the extreme points in I (i.e., I(x) = 1 for x ∈ I and I(x) < 1 for x ∈ ext(C) \ I). We can generalize this deﬁnition to non-polyhedral convex bodies, and to strict subsets of the extreme points. This property turns out to provide an obstruction to certain lifts of non-polyhedral convex bodies.

- Deﬁnition 5.8. A convex body C is k-neighborly with respect to V ⊆ ext(C) if, for every I ⊂ V with |I| = k there exists I ∈ C◦ such that I(x) = 1 for x ∈ I and I(x) < 1 for all x ∈ V \ I.


One can check that a k-neighborly polytope is k-neighborly with respect to its entire set of extreme points. However, this deﬁnition is most interesting beyond the polyhedral setting. Example 5.9. The set of 3×3 positive semideﬁnite matrices with trace one, sometimes called the

- 3 × 3 spectraplex, is 2-neighborly with respect to the (countably inﬁnite) set of extreme points


 

 .

1 p

1 1 + p2 + p4

V = vpv p : p is an integer where vp =

p2

To see this we choose any pair {i,j} of integers and deﬁne the linear functional {i,j} in the polar of the spectraplex by

 

 .

ij −(i + j) 1

{i,j}(X) = tr(X) − w ijXwij where wij =

Since w ijvp = (p − i)(p − j)/ 1 + p2 + p4, it follows that {i,j}(vpv p ) = 1 − 1+p12+p4(p − i)2(p − j)2 which clearly satisﬁes Deﬁnition 5.8. By a similar argument, the (k + 1) × (k + 1) spectraplex is k-neighborly with respect to an inﬁnite set of extreme points.

Convex bodies with neighborliness properties arise very naturally when considering convex reformulations of polynomial optimization problems from the point of view taken in Section 1. If S ⊆ Rn is compact and full-dimensional, we have seen that optimization of polynomials of degree 2d over S can be rephrased as linear optimization over the convex body

C = clconv{(xα)|α|≤2d : x ∈ S}.

The extreme points all have the form (xα)|α|≤2d for x ∈ S. The polar, C◦, is exactly the set of coefﬁcients of polynomials of degree 2d that take value at most one on S. Averkov [Ave19], in a consid-

erable generalization of Example 5.9, showed that for any positive integer M ≥ n+nd − 1 , there is a subset VM of extreme points of C with |VM| = M, and such that C is n+nd − 1 -neighborly with respect to VM. In other words, C is n+nd − 1 -neighborly with respect to arbitrarily large ﬁnite subsets of extreme points.

Being k-neighborly with respect to arbitrarily large ﬁnite sets of extreme points turns out to be an obstruction to K-lifts where K is a Cartesian product of ‘low-complexity’ convex cones. The ﬁrst results in this direction considered the expressive power of second-order cone lifts [Faw19]. Recall that these are K-lifts in which K is a ﬁnite Cartesian product of second-order cones, i.e., cones of the form

L+ +1 = {(x0,x) ∈ R × R : x ≤ x0}.

- Theorem 5.10 ([Faw19]). Let C be a convex body that is 2-neighborly with respect to arbitrarily large ﬁnite sets of extreme points. Then C does not have a second-order cone lift.


Since the 3 × 3 spectraplex is 2-neighborly with respect to an inﬁnite set of extreme points, it

does not have a second-order cone lift. It follows (by a homogenization argument) that S+3 does not have a second-order cone lift.

The second order cone L+ +1 has a (S+2 ) -lift. As such, Theorem 5.10 can also be thought of as giving an obstruction to K-lifts where K is a ﬁnite Cartesian product of 2×2 positive semideﬁnite cones. Averkov [Ave19] extended Theorem 5.10 to show that if m is a positive integer and C is k-neighborly with respect to arbitrarily large ﬁnite sets of extreme points then C does not have a (S+k )m-lift. This allowed him to show that many convex bodies associated with convex approaches to polynomial optimization do not have lifts using small positive semideﬁnite blocks.

The property that C is k-neighborly with respect to arbitrarily large ﬁnite sets of extreme points is really a property of the face lattice of C. As such, we might expect that such a k-neighborliness property is an obstruction to having a K-lift for a class of cones K deﬁned purely by properties of its faces.

- Theorem 5.11 ([Sau20]). Let m be a positive integer and let K1,...,Km be proper convex cones such that, for i = 1,2,...,m, the length of the longest chain of non-empty faces of Ki is at most k+1. If C is a convex body that is k-neighborly with respect to arbitrarily large ﬁnite sets of extreme points, then C does not have a K1 × K2 × ··· × Km-lift.


The length of the longest chain of non-empty faces of the k×k positive semideﬁnite cone is k+1. As such, Theorem 5.10, and Averkov’s extension, are special cases of Theorem 5.11 where we take K1 = K2 = ··· = Km = S+k . Other specializations of Theorem 5.11 tell us, for instance, that

- • the 3 × 3 positive semideﬁnite cone has no K-lift where K is a ﬁnite Cartesian product of smooth convex cones, because any smooth cone only has chains of non-empty faces of length at most three; and
- • the 4 × 4 positive semideﬁnite cone has no lifted representation using a ﬁnite Cartesian product of exponential cones, Kexp = cl{(x,y,t) : y > 0, y exp(x/y) ≤ t}, since the longest chain of non-empty faces in any three-dimensional cone is four.


This last example is of interest due to recent developments in tractable relaxations of polynomial optimization problems based on geometric programming [CS16, DIDW17]. The connection arises because geometric programs can, themselves, be reformulated as conic optimization problems over Cartesian products of exponential cones.

- 5.2. Algebraic obstructions. We have so far discussed obstructions to the existence of lifts based on combinatorial properties of the face lattice of C. In this subsection we discuss algebraic obstructions to the existence of lifts.


- 5.2.1. Preliminaries. A semialgebraic subset of Rn is a set described using Boolean combinations (ﬁnite unions, intersections and complementations) of sets of the form


- (21) {x ∈ Rn : fi(x) = 0,gj(x) ≥ 0,∀i ∈ I,j ∈ J} where fi,gj are polynomials with real coeﬃcients, and I and J are ﬁnite index sets. Most subsets


- of Rn we have seen in this article are semialgebraic subsets. For example any spectrahedron S =


{x ∈ Rn : A0 + x1A1 + ··· + xnAn 0} is semialgebraic, since the constraint that a matrix is positive semideﬁnite can be expressed using polynomial inequalities in the entries of the matrix. A celebrated result of Tarski shows that the projection of any semialgebraic set is semialgebraic.

- Theorem 5.12 (Tarski). Let S ⊂ R be a semialgebraic set and π : R → Rn be a linear map. Then π(S) is semialgebraic.


A consequence of Tarski’s theorem is that if C ⊂ Rn has a spectrahedral lift, then C must be semialgebraic. This already gives us one obstruction to the existence of spectrahedral lift. For example it tells us that a set like {(x,y) ∈ R2 : y ≥ exp(x)} (which is not semialgebraic) cannot have a spectrahedral lift of ﬁnite size.

- 5.2.2. Degree bounds. Let C be a convex semialgebraic set. Deﬁne the (topological) boundary of C as ∂C = (clC) \ (intC). Assuming that our convex set C is full-dimensional in Rn, it can be shown that the boundary is a semialgebraic set of dimension n−1 [Sin15], i.e., it is a hypersurface.


This means that there exists a nonzero polynomial p ∈ R[x1,...,xn] such that ∂C ⊂ Z(p) where Z(p) = {x ∈ Rn : p(x) = 0} is the zero set of p. The set Z(p) is known as the Zariski closure of ∂C. The degree of ∂C is the smallest degree of a polynomial p such that ∂C ⊂ Z(p); and the algebraic boundary of C is deﬁned as Z(p). Below we give several examples of convex sets for which we describe the algebraic boundary and the corresponding degree.

- Example 5.13 (Disk). Consider the convex set C = {(x,y) ∈ R2 : x2 + y2 ≤ 1} which has the 2 × 2 spectrahedral representation


1 − x y y 1 + x

C = (x,y) ∈ R2 :

0 .

The topological boundary of this convex set is the circle {(x,y) ∈ R2 : x2 + y2 = 1} which is described by a polynomial of degree two. Thus the degree of ∂C is equal to two.

- Example 5.14 (Oval). Consider the two-dimensional convex set deﬁned by

(22) C =

 



(x,y) ∈ R2 :

 

- x 0 y 0 1 −x
- y −x 1


  0

 



which corresponds to the blue oval depicted in Figure 26. The smallest degree of a polynomial that vanishes on the boundary of C is 3; an example of such a polynomial is p(x,y) = x − x3 − y2 = 0. The zero set of p(x,y) is shown with a black thick line in Figure 26. We see that it has two components. In this example the topological boundary and algebraic boundary are distinct.

| |
|---|


-2.0 -1.5 -1.0 -0.5 0.0 0.5 1.0 1.5

- -1.5
- -1.0
- -0.5


0.0

0.5

1.0

1.5

Figure 26. In blue is the convex set of Equation (22). The black solid line represents the algebraic boundary of C. It has two components. The degree of the algebraic boundary of C is 3.

- Example 5.15 (k-ellipse). Given points p1,...,pk ∈ R2 in general position, consider the convex set


- (23) C = {x ∈ R2 : x − p1 2 + ··· + x − pk 2 ≤ 1}.

For k = 2, the set C is an ellipse with focal points p1 and p2 and the degree of the boundary of C is equal to 2. For higher k, the degree of the boundary of C was computed in [NPS08], and was

shown to be 2k if k is odd, and 2k − k/ k2 if k is even. Figure 27 shows an example where k = 3.

We saw in Theorem 5.12 that the projection of any semialgebraic set is semialgebraic. More explicit formulations of Tarski’s result give bounds on the degrees of the polynomials that deﬁne the semialgebraic set π(S), in terms of the polynomials that deﬁne S, see, e.g., [Ren92]. These results can be used to show for example that if S is a spectrahedron deﬁned using matrices of size m×m, then the degree of the boundary of π(S) is at most mO(m2n) [GPT13] where n = dim(π(S)). It follows immediately that if C is a convex body of dimension n having a spectrahedral lift of size m

- then necessarily mO(m2n) ≥ d, where d is the degree of the boundary of C. Inverting this inequality allows us to get a lower bound on m in terms of d and n which reads


- (24) m ≥ Ω

log d nlog log(d/n) where Ω hides a constant.

The previous lower bound on m used very little about the structure of the spectrahedron S living in higher dimensions and that projects onto C. A more reﬁned analysis allows us to get the better lower bound [FSED18]:

- (25) m ≥ log d.


5

0

-5

-5 0 5

Figure 27. A 3-ellipse (see Equation (23)) with the focal points shown in red. The smallest degree of a polynomial that vanishes on the boundary of C is 8. The ﬁgure shows the zero set of this degree-8 polynomial.

This bounds relies on the speciﬁc structure of the lift and uses Karush-Kuhn-Tucker system of optimality conditions from convex optimization, combined with the B´ezout bound to count zeroes of systems of polynomial equations.

Observe that the bound (25) only depends on the degree d of the boundary of C and does not depend, say, on the dimension of C. One can easily show that no convex body can have a spectrahedral lift of size smaller than dim(C). Indeed if C = π(S) and S is deﬁned using a linear matrix inequality of size m × m then we must have

m + 1

- (26) dim(C) ≤ dim(S) ≤ dimSm =


2 ≤ m2, which gives m ≥ dim(C).

We note that the two bounds presented above, based on degree and dimension, are not in general comparable:

- • Consider the regular N-gon in the plane. The degree of the boundary is N and so the lower

bound (25) gives m ≥

√log N. On the other hand the bound (26) gives m ≥

√2.

- • Now consider the unit Euclidean ball in Rn. The degree of the boundary is equal to two,


since the boundary is given by the degree-two polynomial equation x21 + ··· + x2n − 1 = 0. Thus the lower bound (25) gives m ≥

√2. On the other hand the dimension lower bound gives m ≥

√n. One interesting open question is to ﬁnd a bound combining both degree d and dimension dim(C) which improves on (24).

- 5.2.3. Scheiderer’s result. In the previous section we saw, using Tarski’s theorem, that in order for a convex set C to have a spectrahedral lift, it must be semialgebraic. Is this condition suﬃcient, i.e., does every convex semialgebraic set have a spectrahedral lift? Nemirovski raised this question in his ICM survey [Nem07] in 2006. In [HN09, HN10] Helton and Nie proved a series of results showing that every convex semialgebraic set whose boundary satisﬁes certain smoothness conditions admits a spectrahedral lift. They also conjectured that any convex semialgebraic set has a spectrahedral lift. In a breakthrough result, Scheiderer [Sch18] disproved this conjecture, and showed the existence of convex semialgebraic sets with no spectrahedral lift.


In this section we give a simple proof of Scheiderer’s result based on the arguments in [Faw21]. For concreteness we will focus on the following convex set:

Cn,2d = clconv (xα)|α|≤2d : x ∈ Rn

where n and d are two integers. Note that Cn,2d is a convex semialgebraic set since it is the convex hull of a semialgebraic set. We will show:

- Theorem 5.16. Assume n and d are two integers such that there is a homogeneous polynomial of degree 2d in n variables that is not a sum of squares. Then Cn,2d has no spectrahedral lift.

The theorem above shows in particular that C3,6 and C4,4 have no spectrahedral lift since it is known by a result of Hilbert that in the cases (n,2d) = (3,6) and (n,2d) = (4,4) there exist nonnegative polynomials that cannot be written as a sum of squares, see, e.g., [BPT13, Chapter 4].

We remark that the assumption in the theorem above can be used to prove that Cn−1,2d has no spectrahedral lift (which readily implies that Cn,2d has no spectrahedral lift, since Cn−1,2d is a projection of Cn,2d), but the argument is more technical and uses additional properties about semialgebraic functions; we refer to [Faw21] for more details.

Sketch of proof of Theorem 5.16. Let n and d as in the statement of the theorem, and assume for contradiction that Cn,2d has a spectrahedral lift. We know from Section 4 (see Equation (*-SDP)) that there is a ﬁnite-dimensional subspace of functions that can be used to certify all valid linear inequalities on Cn,2d using sums of squares. Linear inequalities valid on Cn,2d are nothing but nonnegative polynomials of degree 2d in n variables. Thus the existence of a spectrahedral lift for Cn,2d means that there is a ﬁnite number of functions f1,...,fm : Rn → R such that any nonnegative polynomial in R[x1,...,xn]≤2d is a sum of squares from span(f1,...,fm).

A key observation here is that the functions fi can be taken to be semialgebraic. A semialgebraic function is one whose graph {(x,f(x)) : x ∈ Rn} ⊂ Rn+1 is a semialgebraic set. The observation about the fi can be shown by going back to the proof of the factorization theorem (Theorem 3.9) and using some standard results from semialgebraic geometry, e.g., the cylindrical algebraic decomposition of semialgebraic sets, see [Faw21] for details. Semialgebraic functions are tame and possess nice qualitative properties. The following fact will be crucial for our argument (see, e.g., [HP16, Theorem 1.7] for a proof).

- Theorem 5.17. A semialgebraic function f : Rn → R is smooth (C∞) almost everywhere.


We now have all the ingredients to prove our result. Since the fi (i = 1,...,m) are smooth almost everywhere there is at least one point a ∈ Rn such that all the fi are smooth at the point a.

Let p be a homogeneous polynomial in n variables of degree 2d that is nonnegative but not a sum of squares. Consider the shifted polynomial p(x+a). Since p(x+a) is in R[x1,...,xn]≤2d and nonnegative it must be a sum of squares from span(f1,...,fm). Shifting back to the origin, this means that p(x) is a sum of squares from span(f˜1,...,f˜m) where f˜i(x) = fi(x − a). Note that all the functions in span(f˜1,...,f˜m) are C∞ at the origin. We now use the following proposition:

Proposition 5.18. Let p be a homogeneous polynomial of degree 2d in n variables, and assume that p = j h2j where the hj are arbitrary functions that are smooth (C∞) at the origin. Then p is a sum of squares of polynomials.

Proof. We can write a Taylor expansion of each hj of order d: hj(x) = qj(x) + o( x d) where deg qj = d. Let αj = mindeg qj ≤ d (where mindeg qj is the smallest degree of a monomial in qj) and note that hj(x)2 = qj(x)2 + o( x d+αj). Then we get

p(x) =

j

qj(x)2 + o( x d+αj).

Note that since p is homogeneous we must have αj = d for all j, since otherwise there is a term of degree 2αj in qj(x)2 that cannot be canceled by the other terms. This means that the qj are homogeneous of degree d. But then this means that we must have exact equality p(x) = j qj(x)2 and the remainder term o( x 2d) is identically zero. This shows that p(x) is a sum of squares of polynomials.

End of proof of Theorem 5.16: The proposition above implies that p is a sum of squares of polynomials, which is a contradiction. We have thus shown that Cn,2d has no spectrahedral lift.

6. Discussion

In this article we have focussed on understanding exact lifts of convex sets. We saw several scenarios in which lifted representations greatly simplify the description of a convex set with applications to optimization and other ﬁelds. We also discussed in detail the key tool of slack matrices and operators that both determine the existence of lifts into speciﬁc cones and provide a method to construct them. Various construction methods for lifts, as well as obstructions to their existence, were also discussed. The main focus in these last two sections was on spectrahedral lifts. The purpose of this article was to show the broad connections of lifts to mathematics at large with a focus on spectrahedral lifts in the second half. A short and focussed exposition on just spectrahedral lifts can be found in [Tho18].

There is much more that one can say and study in and around the theory of lifts, and in this ﬁnal section we collect together several of these directions with pointers to the literature. We highlight the surveys and expository articles in each area. These aspects have not been discussed in this article but knit together a more complete view of this rich subject. They also showcase the wide ranging connections between the theory of lifts and other disciplines.

Integer programming/Combinatorial optimization. In this article we have emphasized recent developments in spectrahedral lifts of convex semialgebraic sets, at the expense of more classical topics like polyhedral lifts of polytopes, usually called extended formulations. The study of such extended formulations has a long history, motivated by their importance in combinatorial optimization. A broad exposition of extended formulations of polytopes that arise in combinatorial optimization can be found in [CCZ13]. For a survey of mixed integer linear programming reformulations, see [Vie15].

Lower bounds for polyhedral lifts. The main result of the seminal paper of Yannakakis [Yan91] that was mentioned in Section 3, was that the perfect matching polytope of a complete graph does not admit a small symmetric polyhedral lift. Symmetric lifts were discussed in Section 4. As was mentioned there already, Yannakakis asked whether symmetry imposes restrictions on the linear extension complexity of a polytope. In [KPT12] Kaibel, Pashkovich and Theis showed that, indeed symmetry can force the size of a lift to be higher than necessary. Their examples are certain slices of the perfect matching polytope of a complete graph. A friendly introduction to polyhedral lifts including the symmetry questions can be found in [Kai11]. A second breakthrough result on polyhedral lifts came in [FMP+15] where the authors showed that cut polytopes and traveling salesman polytopes do not admit small polyhedral lifts. The proof relied on showing that a submatrix of the slack matrix had exponentially high nonnegative rank. The underlying combinatorial problems in these examples, the max cut problem and the traveling salesman problem, are NP-hard, and so these results were expected although not known to be true explicitly. On the other hand, there is a polynomial time algorithm to ﬁnd the maximum size matching in a graph which makes it plausible that the matching polytope has a small polyhedral lift. Rothvoss showed in [Rot17] that the matching polytope does not in fact have a small extended formulation. Several results on combinatorial lower bounds on the extension complexity of polytopes and the techniques for establishing such bounds can be found in [FKPT13].

Lower bounds for spectrahedral lifts. Lower bounds on the semideﬁnite extension complexity of polytopes have also received attention. In [LRS15] the authors show that the cut and traveling salesman polytopes of graphs have super polynomial lower bounds on their semideﬁnite extension complexity. As before, such a result is expected but was not known explicitly. It remains open whether matching polytopes also have high semideﬁnite extension complexity. Also no family of polytopes is known with a signiﬁcant gap between linear extension complexity and semideﬁnite extension complexity; see [FSP16] for an explicit example with a nontrivial gap, based on special cyclic polytopes. Semideﬁnite extension complexity can be studied for convex semialgebraic sets beyond polytopes. Not much is known in this direction beyond the results we have presented in Section 5 of this paper.

Other cones. Lifts of convex sets into cone families beyond nonnegative orthants, second order cones and psd cones have also been studied. For instance, a striking result in this direction is that every polytope obtained as the convex hull of a collection of 0/1 vectors in Rn admits a lift into the completely positive cone of size n + 1 [Bur09]. A symmetric matrix M is copositive if x Mx ≥ 0 for all x ≥ 0 and the copositive cone of size k is the set of all k × k copositive matrices. Its dual cone is the completely positive cone and consists of all symmetric matrices of the form BB where B is a nonnegative matrix. While the lifts mentioned above are small in terms of the size of matrices involved, linear programming over copositive and completely positive cones do not admit eﬃcient algorithms unless P = NP [DG14, MK87]. There are other families of convex cones for which the associated conic program enjoys eﬃcient algorithms. Examples include hyperbolic programming [Gu¨l97], geometric programming [BKVH07], and relative entropy programming [CS17]. Studying lifted representations of convex sets using hyperbolicity cones or relative entropy cones gives a systematic approach to understanding the expressive power of these families of optimization problems.

Approximate lifts and hierarchies. Since ﬁnding an exact lift of a convex set might be hard, it is useful to look for an approximate lift in the sense of a set in higher dimension whose projection contains the original convex set. There is a vast body of literature on such approximate lifts, as well as construction methods for producing a hierarchy of lifts in increasing dimensions whose projections create a nested sequence of convex approximations of the original set. The hierarchies most closely related to the discussion in Section 4 of this paper are those of Lasserre [Las01] based on moments of probability measures, and its dual due to Parrilo [Par03] based on sums of squares of polynomials. These methods are connected to deep results in real algebraic geometry, the theory of moments, and optimization, which give tools to address questions of convergence, construction, geometry and more. See [Lau09] for a survey on the Lasserre and Parrilo hierarchies. For a discussion of some of the central hierarchies for convex approximations of a set and their relationships, see [Lau03]. See [BPT13] for broad connections to convex algebraic geometry and related topics. The chapter [GT12] in the Handbook of Semideﬁnite, Conic and Polynomial Optimization is about theta bodies of algebraic varieties which is a speciﬁc hierarchy of spectrahedral lifts that successively approximate the convex hull of an algebraic variety. Theta bodies are also the subject of the chapter titled Convex Hulls of Algebraic Sets in [BPT13]. The tight connection between conic lifts of convex semialgebraic sets and cone factorizations was inspired by the work on theta bodies and the paper of Yannakakis [Yan91] that connects polyhedral lifts to nonnegative factorizations.

Approximation algorithms. Hierarchies of convex relaxations have been studied extensively in theoretical computer science from the point of view of approximation algorithms. The most celebrated result in this context is perhaps the rounding algorithm for the max cut problem due

- to Goemans and Williamson, that yields an α-approximation with α ≈ 0.878 [GW95]. This is based on a simple spectrahedral relaxation of the cut polytope. Recently, hierarchies have been used to produce lower bounds on the approximation power of arbitrary polynomial-size linear (semideﬁnite) programming relaxations of hard combinatorial problems; see e.g. [CLRS16, LRS15] and the references therein.


Computational complexity. A natural question is to ask: what is the complexity of deciding whether a convex set C admits a K-lift?2 To make the question precise, one needs to specify how the input convex set C is provided, e.g., as a set of extreme points, a set of valid inequalities, membership/separation oracle, etc., and similarly for the cone K. Existing results on the hardness of computing the nonnegative and positive semideﬁnite rank of matrices [Vav10, Shi17] can be used to show some NP-hardness results on the existence of lifts. For example, one can show that if P ⊂ Q are two polytopes where P is given by its set of vertices, and Q by its set of facets, the question of deciding whether there is a polytope S with an Rr+-lift such that P ⊂ S ⊂ Q is NP-hard (here r ∈ N is part of the input). The same problem is also NP-hard if we replace Rr+ by S+r lift, and is a consequence of the NP-hardness of computing the positive semideﬁnite rank of matrices [Shi17]. These hardness results follow from the fact that any nonnegative matrix M can be interpreted as the generalized slack matrix/operator (see Prop. 3.12) of two such polytopes P,Q by a simple rank factorization of M, see, e.g., [GG12]. As far as we know the same question where P = Q is given by a V or H-representation is open, as not every nonnegative matrix is the slack matrix of a polytope [GGK+13].

Other applications of factorizations. Factorizations of nonnegative matrices have many uses beyond the theory of lifts. Nonnegative factorizations of matrices is an essential tool for dimensionality reduction. In this case one is often interested in approximate factorizations, rather than exact ones, see the chapter [Gil15] for applications of nonnegative factorizations to data analysis. Nonnegative factorizations also have interpretations in probabilistic modeling, information theory and communication complexity, see [CR93] and [FMP+15]. Positive semideﬁnite factorizations of nonnegative matrices in turn have applications in quantum information theory and quantum communication complexity; these are explained in [FGP+15] and [FMP+15]. The survey [FGP+15] is about psd factorizations and psd ranks of general nonnegative matrices. It does not focus on slack matrices which are the nonnegative matrices needed for lifts.

Symmetric factorizations also have applications. Recall that a matrix M is completely positive

if there exists vectors {bi} ⊂ Rk+ such that Mij = bi,bj . The completely positive rank of M is the smallest k for which such symmetric factorization is possible. Analogously, a square matrix

M ∈ Rp+×p is said to be psd-completely-positive if there exist psd matrices A1,...,Ap (of arbitrary size) such that Mij = tr(AiAj) for all i,j = 1,...,p. These factorizations have found many applications in quantum information, in the context of nonlocal games, see, e.g., [GdLL18]. Tools have recently been developed to bound both the completely positive and psd-completely-positiverank of matrices [GdLL17, GdLL19].

References

[AP13] A. A. Ahmadi and P. A. Parrilo. A complete characterization of the gap between convexity and SOSconvexity. SIAM J. Optim., 23(2):811–833, 2013. 15 [Ave19] G. Averkov. Optimal size of linear matrix inequalities in semideﬁnite approaches to polynomial optimization. SIAM J. Appl. Algebra Geometry, 3(1):128–151, 2019. 36 [BB97] H. H. Bauschke and J. M. Borwein. Legendre functions and the method of random Bregman projections. J. Convex Anal., 4(1):27–67, 1997. 26 [Bir46] G. Birkhoﬀ. Tres observaciones sobre el algebra lineal. Univ. Nac. Tucuma´n, Rev. Ser. A, 5:147–151,

1946. 3 [BKVH07] S. Boyd, S.-J. Kim, L. Vandenberghe, and A. Hassibi. A tutorial on geometric programming. Optim. Eng., 8(1):67–127, 2007. 42

[BPT13] G. Blekherman, P. A. Parrilo, and R. R. Thomas, editors. Semideﬁnite Optimization and Convex Algebraic Geometry, volume 13 of MOS-SIAM Series on Optimization. Society for Industrial and Applied Mathematics (SIAM), Philadelphia; Mathematical Optimization Society, Philadelphia, 2013. 29, 40, 42

[Bry86] R. E. Bryant. Graph-based algorithms for Boolean function manipulation. IEEE Trans. Comput., 100(8):677–691, 1986. 9

2We thank one of the reviewers for raising this question.

- [BTN01a] A. Ben-Tal and A. Nemirovski. Lectures on modern convex optimization: analysis, algorithms, and engineering applications, volume 2. Society for Industrial and Applied Mathematics, 2001. 6
- [BTN01b] A. Ben-Tal and A. Nemirovski. On polyhedral approximations of the second-order cone. Math. Oper. Res., 26(2):193–205, 2001. 33


[Bur09] S. Burer. On the copositive representation of binary and continuous nonconvex quadratic programs. Math. Program., 120(2, Ser. A):479–495, 2009. 42 [CCZ13] M. Conforti, G. Cornu´ejols, and G. Zambelli. Extended formulations in combinatorial optimization. Ann. Oper. Res., 204:97–143, 2013. 41 [CLP99] F. Chen, L. Lova´sz, and I. Pak. Lifting Markov chains to speed up mixing. In Proceedings of the 31st ACM Symposium on Theory of Computing, Atlanta, GA, pages 275–281. ACM, 1999. 8 [CLRS16] S. O. Chan, J. R. Lee, P. Raghavendra, and D. Steurer. Approximate constraint satisfaction requires large LP relaxations. J. ACM, 63(4):Art. 34, 22, 2016. 42 [CR93] J. E. Cohen and U. G. Rothblum. Nonnegative ranks, decompositions, and factorizations of nonnegative matrices. Linear Algebra Appl., 190:149–168, 1993. 21, 43

- [CS16] V. Chandrasekaran and P. Shah. Relative entropy relaxations for signomial optimization. SIAM J. Optim., 26(2):1147–1173, 2016. 37
- [CS17] V. Chandrasekaran and P. Shah. Relative entropy optimization and its applications. Math. Program., 161(1-2, Ser. A):1–32, 2017. 42


[DG14] P. J. C. Dickinson and L. Gijben. On the computational complexity of membership problems for the completely positive cone and its dual. Comput. Optim. Appl., 57(2):403–415, 2014. 42 [DIDW17] M. Dressler, S. Iliman, and T. De Wolﬀ. A Positivstellensatz for sums of nonnegative circuit polynomials. SIAM J. Appl. Algebra Geometry, 1(1):536–555, 2017. 37 [DT05] D. L. Donoho and J. Tanner. Sparse nonnegative solution of underdetermined linear equations by linear programming. Proc. Nat. Acad. Sci. USA, 102(27):9446–9451, 2005. 35 [Faw19] H. Fawzi. On representing the positive semideﬁnite cone using the second-order cone. Math. Program., 175(1-2):109–118, 2019. 8, 36 [Faw21] H. Fawzi. The set of separable states has no ﬁnite semideﬁnite representation except in dimension 3 × 2. Comm. Math. Phys., 386(3):1319–1335, 2021. 40 [FGP+15] H. Fawzi, J. Gouveia, P. A. Parrilo, R. Z. Robinson, and R. R. Thomas. Positive semideﬁnite rank. Math. Program., 153(1, Ser. B):133–177, 2015. 43 [FKPT13] S. Fiorini, V. Kaibel, K. Pashkovich, and D. O. Theis. Combinatorial bounds on nonnegative rank and extended formulations. Discrete Math., 313(1):67–83, 2013. 41 [FMP+15] S. Fiorini, S. Massar, S. Pokutta, H. R. Tiwary, and R. de Wolf. Exponential lower bounds for polytopes in combinatorial optimization. J. ACM, 62(2):Art. 17, 23, 2015. 41, 43 [FSED18] H. Fawzi and M. Safey El Din. A lower bound on the positive semideﬁnite rank of convex bodies. SIAM J. Appl. Algebra Geometry, 2(1):126–139, 2018. 38

- [FSP15] H. Fawzi, J. Saunderson, and P. A. Parrilo. Equivariant semideﬁnite lifts and sum-of-squares hierarchies. SIAM J. Optim., 25(4):2212–2243, 2015. 32
- [FSP16] H. Fawzi, J. Saunderson, and P. A. Parrilo. Sparse sums of squares on ﬁnite abelian groups and improved semideﬁnite lifts. Math. Prog., 160(1-2):149–191, 2016. 42


[Gal63] D. Gale. Neighborly and cyclic polytopes. In Proc. Sympos. Pure Math, volume 7, pages 225–232, 1963. 35

- [GdLL17] S. Gribling, D. de Laat, and M. Laurent. Matrices with high completely positive semideﬁnite rank. Linear Algebra Appl., 513:122–148, 2017. 43
- [GdLL18] S. Gribling, D. de Laat, and M. Laurent. Bounds on entanglement dimensions and quantum graph parameters via noncommutative polynomial optimization. Math. Program., 170(1):5–42, 2018. 43
- [GdLL19] S. Gribling, D. de Laat, and M. Laurent. Lower bounds on matrix factorization ranks via noncommutative polynomial optimization. Found. Comput. Math., 19(5):1013–1070, 2019. 43


[GG12] N. Gillis and F. Glineur. On the geometric interpretation of the nonnegative rank. Linear Algebra Appl., 437(11):2685–2712, 2012. 43 [GGK+13] J. Gouveia, R. Grappe, V. Kaibel, K. Pashkovich, R. Z. Robinson, and R. R. Thomas. Which nonnegative matrices are slack matrices? Linear Algebra Appl., 439(10):2921–2933, 2013. 43

[Gil15] N. Gillis. The why and how of nonnegative matrix factorization. In Regularization, optimization, kernels, and support vector machines, Chapman & Hall/CRC Mach. Learn. Pattern Recogn. Ser., pages 257–291. CRC Press, Boca Raton, FL, 2015. 43

[GLS84] M. Gro¨tschel, L. Lov´asz, and A. Schrijver. Polynomial algorithms for perfect graphs. In Topics on Perfect Graphs, volume 88 of North-Holland Math. Stud., pages 325–356. North-Holland, Amsterdam, 1984. 13 [GLS86] M. Gro¨tschel, L. Lova´sz, and A. Schrijver. Relaxations of vertex packing. J. Combin. Theory Ser. B, 40(3):330–343, 1986. 13, 14

[GLS93] M. Gro¨tschel, L. Lova´sz, and A. Schrijver. Geometric Algorithms and Combinatorial Optimization, volume 2 of Algorithms and Combinatorics. Springer-Verlag, Berlin, second edition, 1993. 14 [GN11] J. Gouveia and T. Netzer. Positive polynomials and projections of spectrahedra. SIAM J. Optim., 21(3):960–976, 2011. 30 [Goe15] M. X. Goemans. Smallest compact formulation for the permutahedron. Math. Program., 153(1):5–11,

2015. 6, 32, 33 [Gol04] M. C. Golumbic. Algorithmic Graph Theory and Perfect Graphs (Annals of Discrete Mathematics, Vol 57). North-Holland Publishing Co., NLD, 2004. 13 [GPRT17] J. Gouveia, K. Pashkovich, R. Z. Robinson, and R. R. Thomas. Four-dimensional polytopes of minimum positive semideﬁnite rank. J. Combin. Theory Ser. A, 145:184–226, 2017. 35 [GPT10] J. Gouveia, P. A. Parrilo, and R. R. Thomas. Theta bodies for polynomial ideals. SIAM J. Optim., 20(4):2097–2118, 2010. 30 [GPT13] J. Gouveia, P. A. Parrilo, and R. R. Thomas. Lifts of convex sets and cone factorizations. Math. Oper. Res., 38(2):248–264, 2013. 24, 25, 35, 38 [GRT13] J. Gouveia, R. Z. Robinson, and R. R. Thomas. Polytopes of minimum positive semideﬁnite rank. Discrete Comput. Geom., 50(3):679–699, 2013. 35 [GT12] J. Gouveia and R. R. Thomas. Convex hulls of algebraic sets. In Handbook on Semideﬁnite, Conic and Polynomial Optimization, pages 113–138. Springer, 2012. 30, 42 [Gu¨l97] O. G¨uler. Hyperbolic polynomials and interior point methods for convex programming. Math. Oper. Res., 22(2):350–377, 1997. 42 [GW95] M. X. Goemans and D. P. Williamson. Improved approximation algorithms for maximum cut and satisﬁability problems using semideﬁnite programming. J. ACM, 42(6):1115–1145, 1995. 4, 42 [Hau03] H. Hauser. The Hironaka theorem on resolution of singularities (or: A proof we always wanted to understand). Bull. Amer. Math. Soc., 40(3):323–403, 2003. 7 [Hen11] D. Henrion. Semideﬁnite representation of convex hulls of rational varieties. Acta Appl. Math., 115(3):319,

2011. 29 [Hir64a] H. Hironaka. Resolution of singularities of an algebraic variety over a ﬁeld of characteristic zero: I. Ann.

- Math., 79(1):109–203, 1964. 7

[Hir64b] H. Hironaka. Resolution of singularities of an algebraic variety over a ﬁeld of characteristic zero: II. Ann.

- Math., 79(2):205–326, 1964. 7


[HN09] J. W. Helton and J. Nie. Suﬃcient and necessary conditions for semideﬁnite representability of convex hulls and sets. SIAM J. Optim., 20(2):759–791, 2009. 39 [HN10] J. W. Helton and J. Nie. Semideﬁnite representation of convex sets. Math. Program., 122(1):21–64, 2010.

15, 39 [Hor62] A. Horn. Eigenvalues of sums of Hermitian matrices. Paciﬁc J. Math., 12:225–241, 1962. 17 [HP16] H.-V. Ha` and T.-S. Pham. Genericity in Polynomial Optimization, volume 3. World Scientiﬁc, 2016. 40 [Kai11] V. Kaibel. Extended formulations in combinatorial optimization. Optima 85, 2011. 14 pages. 41 [Kly98] A. A. Klyachko. Stable bundles, representation theory and Hermitian operators. Selecta Math. (N.S.),

4(3):419–445, 1998. 17 [KPT12] V. Kaibel, K. Pashkovich, and D. O. Theis. Symmetry matters for sizes of extended formulations. SIAM J. Discrete Math., 26(3):1361–1382, 2012. 31, 41 [KT99] A. Knutson and T. Tao. The honeycomb model of GLn(C) tensor products. I. Proof of the saturation conjecture. J. Amer. Math. Soc., 12(4):1055–1090, 1999. 17 [KT01] A. Knutson and T. Tao. Honeycombs and sums of Hermitian matrices. Notices Amer. Math. Soc., 48(2):175–186, 2001. 17 [Las01] J. B. Lasserre. Global optimization with polynomials and the problem of moments. SIAM J. Optim.,

11(3):796–817, 2001. 42 [Las09] J. B. Lasserre. Convex sets with semideﬁnite representation. Math. Program., 120(2):457–477, 2009. 30 [Lau03] M. Laurent. A comparison of the Sherali-Adams, Lova´sz-Schrijver, and Lasserre relaxations for 0-1 pro-

gramming. Math. Oper. Res., 28(3):470–496, 2003. 42

[Lau09] M. Laurent. Sums of squares, moment matrices and optimization over polynomials. In Emerging applications of algebraic geometry, volume 149 of IMA Vol. Math. Appl., pages 157–270. Springer, New York,

2009. 42 [LL92] H.-T. Liaw and C.-S. Lin. On the OBDD-representation of general Boolean functions. IEEE Trans. Comput., 41(6):661–664, 1992. 10

[LRS15] J. R. Lee, P. Raghavendra, and D. Steurer. Lower bounds on the size of semideﬁnite programming relaxations. In Proceedings of the 47th 2015 ACM Symposium on Theory of Computing, Portland, OR, pages 567–576. ACM, New York, 2015. 42

[LS91] L. Lova´sz and A. Schrijver. Cones of matrices and set-functions and 0–1 optimization. SIAM J. Optim., 1(2):166–190, 1991. 32 [Mas76] W. J. Masek. A fast algorithm for the string editing problem and decision graph complexity. Master’s thesis, Massachusetts Institute of Technology, 1976. 10 [Min93] S. Minato. Zero-suppressed BDDs for set manipulation in combinatorial problems. In Proceedings of the 30th ACM/IEEE Design Automation Conference, pages 272–277. IEEE, 1993. 10 [MK87] K. G. Murty and S. N. Kabadi. Some NP-complete problems in quadratic and nonlinear programming.

Math. Program., 39(2):117–129, 1987. 42 [Nea03] R. M. Neal. Slice sampling. Ann. Statist., 31(3):705–767, 2003. 8 [Nea11] R. M. Neal. MCMC using Hamiltonian dynamics. In Handbook of Markov Chain Monte Carlo, pages

139–188. Chapman and Hall/CRC, 2011. 8 [Nem07] A. Nemirovski. Advances in convex optimization: conic programming. In Proceedings of the International Congress of Mathematicians, volume 1, pages 413–444, 2007. 39 [NN94] Yu. Nesterov and A. Nemirovskii. Interior-point Polynomial Algorithms in Convex Programming. SIAM,

1994. 6 [NPS08] J. Nie, P. A. Parrilo, and B. Sturmfels. Semideﬁnite representation of the k-ellipse. In Algorithms in algebraic geometry, pages 117–132. Springer, 2008. 38 [Par03] P. A. Parrilo. Semideﬁnite programming relaxations for semialgebraic problems. Math. Program., 96(2, Ser. B):293–320, 2003. 42 [Par06] P. A. Parrilo. Exact semideﬁnite representation for genus zero curves. In Talk at the Banﬀ workshop “Positive Polynomials and Optimization”, Banﬀ, Canada, pages 8–12, 2006. 29

[Ren92] J. Renegar. On the computational complexity and geometry of the ﬁrst-order theory of the reals. I. Introduction. Preliminaries. The geometry of semi-algebraic sets. The decision problem for the existential theory of the reals. J. Symbolic Comput., 13(3):255–299, 1992. 38

[Roc70] R. T. Rockafellar. Convex Analysis. Princeton University Press, 1970. 26 [Rot17] T. Rothvoss. The matching polytope has exponential extension complexity. J. ACM, 64(6):Art. 41, 19,

2017. 41 [SA90] H. D. Sherali and W. P. Adams. A hierarchy of relaxations between the continuous and convex hull representations for zero-one programming problems. SIAM J. Discrete Math., 3(3):411–430, 1990. 8, 32 [Sau20] J. Saunderson. Limitations on the expressive power of convex cones without long chains of faces. SIAM J. Optim., 30(1):1033–1047, 2020. 36 [Sch03] A. Schrijver. Combinatorial Optimization: Polyhedra and Eﬃciency, volume 24. Springer Science & Busi-

ness Media, 2003. 10, 13 [Sch18] C. Scheiderer. Spectrahedral shadows. SIAM J. Appl. Algebra Geom., 2(1):26–44, 2018. 8, 39 [Shi17] Y. Shitov. The complexity of positive semideﬁnite matrix factorization. SIAM J. Optim., 27(3):1898–1909,

2017. 43 [Sin15] R. Sinn. Algebraic boundaries of convex semi-algebraic sets. Res. Math. Sci., 2(1):3, 2015. 37 [Sta86] R. P. Stanley. Two poset polytopes. Discrete Comput. Geom., 1(1):9–23, 1986. 12 [Tho18] R. R. Thomas. Spectrahedral lifts of convex sets. In Proceedings of the International Congress of

Mathematicians—Rio de Janeiro 2018. Vol. IV. Invited lectures, pages 3819–3842. World Sci. Publ., Hackensack, NJ, 2018. 41

[Vav10] S. A. Vavasis. On the complexity of nonnegative matrix factorization. SIAM J. Optim., 20(3):1364–1377,

2010. 43 [VB96] L. Vandenberghe and S. Boyd. Semideﬁnite programming. SIAM Rev., 38(1):49–95, March 1996. 4 [VGG17] A. Vandaele, N. Gillis, and F. Glineur. On the linear extension complexity of regular n-gons. Linear

Algebra Appl., 521:217–239, 2017. 33

[Vie15] J. P. Vielma. Mixed integer linear programming formulation techniques. SIAM Rev., 57(1):3–57, 2015. 41 [VN53] J. Von Neumann. A certain zero-sum two-person game equivalent to the optimal assignment problem. In

H. W. Kuhn and A. W. Tucker, editors, Contributions to the Theory of Games, volume 2, pages 5–12. Princeton University Press, 1953. 3

[Weg00] I. Wegener. Branching Programs and Binary Decision Diagrams: Theory and Applications, volume 4. SIAM, 2000. 10 [Yan91] M. Yannakakis. Expressing combinatorial optimization problems by linear programs. J. Comput. System Sci., 43(3):441–466, 1991. 8, 19, 21, 22, 31, 41, 42 [Zie00] G. M. Ziegler. Lectures on 0/1-polytopes. In Polytopes–Combinatorics and Computation, pages 1–41. Springer, 2000. 8

Department of Applied Mathematics and Theoretical Physics, University of Cambridge, CB3 0WA,

United Kingdom Email address: h.fawzi@damtp.cam.ac.uk CMUC, Department of Mathematics, University of Coimbra, 3001-454 Coimbra, Portugal Email address: jgouveia@mat.uc.pt Laboratory for Information and Decision Systems (LIDS), Massachusetts Institute of Technology,

Cambridge, MA 02139, USA Email address: parrilo@mit.edu Department of Electrical and Computer Systems Engineering, Monash University, VIC 3800, Aus-

tralia Email address: james.saunderson@monash.edu Department of Mathematics, University of Washington, Box 354350, Seattle, WA 98195, USA Email address: rrthomas@uw.edu

