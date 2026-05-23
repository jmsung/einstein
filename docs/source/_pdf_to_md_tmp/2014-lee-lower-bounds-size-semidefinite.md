arXiv:1411.6317v1[cs.CC]24Nov2014

# Lower bounds on the size of semideﬁnite programming relaxations

James R. Lee∗ Prasad Raghavendra† David Steurer‡

Abstract

We introduce a method for proving lower bounds on the eﬃcacy of semideﬁnite programming (SDP) relaxations for combinatorial problems. In particular, we show that the cut, TSP, and stable set polytopes on n-vertex graphs are not the linear image of the feasible region of any SDP (i.e., any spectrahedron) of dimension less than 2nδ, for some constant δ > 0. This result yields the ﬁrst super-polynomial lower bounds on the semideﬁnite extension complexity of any explicit family of polytopes.

Our results follow from a general technique for proving lower bounds on the positive semideﬁnite rank of a matrix. To this end, we establish a close connection between arbitrary SDPs and those arising from the sum-of-squares SDP hierarchy. For approximating maximum constraint satisfactionproblems, we provethatSDPsof polynomial-size areequivalentinpower to those arising from degree-O(1) sum-of-squares relaxations. This result implies, for instance, that no family of polynomial-size SDP relaxations can achieve better than a 7/8-approximation for max 3-sat.

Keywords: semideﬁnite programming, sum-of-squares method, lower bounds on positivesemideﬁnite rank, approximation complexity, quantum learning, polynomial optimization.

![image 1](<2014-lee-lower-bounds-size-semidefinite_images/imageFile1.png>)

∗University of Washington. †UC Berkeley. ‡Cornell University.

## Contents

#### 1 Introduction 3

- 1.1 Spectrahedral lifts of polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- 1.2 Semideﬁnite relaxations and constraint satisfaction . . . . . . . . . . . . . . . . . . . 5
- 1.3 Positive semideﬁnite rank and sum-of-squares degree . . . . . . . . . . . . . . . . . . 8


#### 2 Proof overview and setup 11

- 2.1 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
- 2.2 Factorizations, quantum learning, and pseudo-densities . . . . . . . . . . . . . . . . . 12


#### 3 PSD rank and sum-of-squares degree 17

- 3.1 Analysis of the separating functional . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
- 3.2 Degree reduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
- 3.3 Proof of the main theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23


#### 4 Approximations for density operators 24

- 4.1 Approximation against a single test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
- 4.2 Approximation against a family of tests . . . . . . . . . . . . . . . . . . . . . . . . . . 26 4.2.1 Junta approximation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29


#### 5 The correlation polytope 31

- 5.1 Positive semideﬁnite rank . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

6 Optimality of low-degree sum-of-squares for max CSPs 34

- 6.1 The SDP approximation model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34


- 6.2 General SDPs vs. sum-of-squares . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

7 Nonnegative rank 38

- 7.1 Nonnegative rank vs. junta degree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38


- 7.2 The correlation polytope and lopsided disjointness . . . . . . . . . . . . . . . . . . . . 40
- 7.3 Unique games hardness for LPs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42


#### References 43

## 1 Introduction

Convex characterizations and relaxations of combinatorial problems have been a consistent, powerful theme in the theory of algorithms since its inception. Linear and semideﬁnite programming relaxations have been particularly useful for the eﬃcient computation of approximate solutions to NP-hard problems (see, for instance, the books [WS11, Vaz01]). In some sense, semideﬁnite programs (SDPs) can be seen as combining the rich expressiveness of linear programs with the global geometric power of spectral methods. For many fundamental combinatorial problems, this provides a genuinely new structural and computational perspective [GW95, KMS98, ARV09]. Indeed, for an array of optimization problems, the best-known approximation algorithms can only be achieved via SDP relaxations.

It has long been known that integrality gaps for linear programs (LPs) can often lead to gadgets for NP-hardness of approximation reductions (see, e.g., [LY93, CGH+05, HK03]). Furthermore, assuming the Unique Games Conjecture [Kho02], it is known that integrality gaps for SDPs can be translated directly into hardness of approximation results [KKMO04, Aus10, Rag08]. All of this suggests that the computational model underlying LPs and SDPs is remarkably powerful.

Thus it is a natural (albeit ambitious) goal to characterize the computational power of this model. If P NP, we do not expect to ﬁnd polynomial-size families of SDPs that yield arbitrarily good approximations to NP-hard problems. (See [Rot13, BDP13] for a discussion of how this follows formally from the assumption NP P/poly.)

In the setting of linear programs (LPs), the search for a model and characterization began in a remarkable work of Yannakakis [Yan91]. He proved that the TSP and matching polytopes do not admit symmetric linear programming formulations of size 2o(n), where n is the number of vertices in the underlying graph. In the process, he laid the structural framework (in terms of nonnegative factorizations) that would underlie all future work in the subject. It took over 20 years before Fiorini, Massar, Pokutta, Tiwary, and de Wolf [FMP+12] were able to remove the symmetry assumption and obtain a lower bound of 2Ω(

√n) on the size of any LP formulation. Soon afterward, Rothvoß [Rot14] gave a lower bound of 2Ω(n) on the size of any LP formulation for the matching polytope (and also TSP), completing Yannakakis’ vision.

![image 2](<2014-lee-lower-bounds-size-semidefinite_images/imageFile2.png>)

Despite the progress in understanding the power of LP formulations, it remained a mystery whether there were similar strong lower bounds in the setting of SDPs. An analogous positive semideﬁnite factorization framework was provided in [FMP+12, GPT11]. Following the LP methods of [CLRS13], the papers [LRST14, FSP13] proved exponential lower bounds on the size of symmetric SDP formulations for NP-hard constraint satisfaction problems (CSPs).

In the present work, we prove strong lower bounds on the size of general SDP formulations for the cut, TSP, and stable set polytopes. Moreover, we show that polynomial-size SDP relaxations cannotachievearbitrarilygoodapproximationsformanyNP-hardconstraintsatisfactionproblems. For instance, no polynomial-size family of relaxations can achieve better than a 7/8-approximation for max 3-sat. More generally, we show that the low-degree sum-of-squares SDP relaxations yield the best approximation among all polynomial-sized families of relaxations for max-CSPs.

This is achieved by relating arbitrary SDP formulations to those coming from the sum-ofsquares SDP hierarchy1 [Las01, Par00, Sho87], analogous to our previous work with Chan relating LP formulations to the Sherali–Adams hierarchy [CLRS13]. The SDP setting poses a number of signiﬁcant challenges. At a very high level, our approach can be summarized as follows: Given an arbitrary SDP formulation of small size, we use methods from quantum entropy maximization

![image 3](<2014-lee-lower-bounds-size-semidefinite_images/imageFile3.png>)

1This hierarchy is also frequently referred to as the Lasserre SDP hierarchy.

and online convex optimization (often going by the name “matrix multiplicative weights update”) to learn an approximate low-degree sum-of-squares formulation on a subset of the input variables. In the next section, we present a formal overview of our results, and a discussion of the connections to quantum information theory, real algebraic geometry, and proof complexity.

Organization. The results of this work fall along two broad themes, lower bounds on spectrahedral lifts of speciﬁc polytopes and lower bounds on SDP relaxations for constraint satisfaction problems. Both sets of results are consequences of a general method for proving lower bounds on positive semideﬁnite rank. For the convenience of the reader, we have organized the two themes in two self-contained trajectories. Thus, lower bounds on spectrahedral lifts can be accessed via Section 1.1, Section 1.3, Section 2, Section 3 and Section 5. The lower bounds for constraint satisfaction problems can be reached through Section 1.2, Section 1.3, Section 2, Section 3 and Section 6.

We also present general results on approximating density operators against families of linear tests through quantum learning in Section 4. Finally, in Section 7, we exhibit applications of our techniques to non-negative rank; in particular, this is used to give a simple, self-contained proof of a lower bound on the nonnegative rank of the unique disjointness matrix.

### 1.1 Spectrahedral lifts of polytopes

Polytopes are an appealing and useful way to encode many combinatorial optimization problems. Forexample, thetraveling salesman problem onn cities is equivalent tooptimizing linear functions over the traveling salesman polytope, i.e., the convex hull of characteristic vectors 1C ∈ {0,1}(n2) ⊆ R(n2) of n-vertex Hamiltonian cycles C (viewed as edge sets). If a polytope admits polynomial-size LP or SDP formulations, then we can optimize linear functions over the polytope in polynomial time (exactly for LP formulations and up to arbitrary accuracy in the case of SDP formulations). Indeed, a large number of eﬃcient, exact algorithms for combinatorial optimization problems can be explained by small LP or SDP formulations of the underlying polytope. (For approximation algorithms, the characterization in terms of compact formulations of polytopes is not as direct [BFPS12]. In Section 1.2, we will give a direct characterization for approximation algorithms in terms of the original combinatorial problem.)

Positivesemideﬁnitelifts. FixapolytopeP ⊆ Rn (e.g.,thetravelingsalesmanpolytopedescribed above). We are interested in the question of whether there exists a low-dimensional SDP that captures P. Let Sk+ denote the cone of symmetric, k × k positive semideﬁnite matrices embedded naturally in Rk×k. If there exists an aﬃne subspace L ⊆ Rk×k and a linear map π : Rk×k → Rn such that

P = π(Sk+ ∩ L), one says that P admits a positive-semideﬁnite (psd) lift of size k. (This terminology is taken from [FGP+14].) We remark that the intersection of a PSD cone with an aﬃne subspace is often referred to as a spectrahedron.

The point is that in order to optimize a linear function ℓ: Rn → R over the polytope P, it is enough to optimize the linear function ℓ ◦ π: Rk×k → R over the set Sk+ ∩ L instead,

ℓ ◦ π(y).

ℓ(x) = min

min

x∈P

y∈Sk+∩L

Here, the optimization problem on the right is a semideﬁnite programming problem in k-by-k matrices. This idea also goes under the name of a semideﬁnite extended formulation [FMP+12].

The positive-semideﬁnite rank of explicit polytopes. We deﬁne the positive-semideﬁnite (psd) rank of a polytope P, denoted rkpsd(P), to be the smallest number k such that there exists a psd lift of size k. (Our use of the word “rank” will make sense soon—see Section 1.3.) Briët, Dadush, and Pokutta [BDP13] showed (via a counting argument) that there exist 0/1 polytopes in Rn with exponential psd rank. In this work, we prove the ﬁrst super-polynomial lower bounds on the psd rank of explicit polytopes: The correlation polytope corrn ⊆ Rn2 is given by

corrn = conv {xxT : x ∈ {0,1}n} . In Section 5.1, we show the following strong lower bound on its psd rank. Theorem 1.1. For every n 1, we have

rkpsd(corrn) 2Ω(n2/13) .

The importance of the correlation polytope corrn lies in the fact that a number of interesting polytopes from combinatorial optimization contain a face that linearly projects to corrn . We ﬁrst deﬁne a few diﬀerent families of polytopes and then recall their relation to corrn.

For n 1, let Kn = ([n], [n2] ) be the complete graph on n vertices. For a set S ⊆ [n], we use ∂S ⊆ [n2] to denote the set of edges with one endpoint in S and the other in S¯, and we use the notation 1∂S ∈ R(n2) to denote the characteristic vector of S. The cut polytope on n vertices is deﬁned by

cutn = conv({1∂S : S ⊆ [n]}) .

Similarly, if τ is a salesman tour of Kn (i.e., a Hamiltonian cycle), we use 1E(τ) ∈ R(n2) to denote the corresponding indicator of the edges contained in τ. In that case, the TSP polytope is given by

tspn = conv {1E(τ) : τ is a Hamiltonian cycle} .

Finally, consider an arbitrary n-vertex graph G = ([n],E). We recall that a subset of vertices S ⊆ [n] is an independent set (also called a stable set) if there are no edges between vertices in S. The stable set polytope of G is given by

stabn(G) = conv {1S ∈ Rn : S is an independent set in G} .

By results of [DS90] and [FMP+12] (see Proposition 5.2), Theorem 1.1 directly implies the following lower bounds on the psd rank of the cut, TSP, and stable set polytopes.

Corollary 1.2. The following lower bounds hold for every n 1,

rkpsd(cutn) 2Ω(n2/13), rkpsd(tspn) 2Ω(n1/13),

rkpsd(stabn(G)) 2Ω(n1/13).

max

n-vertex G

### 1.2 Semideﬁnite relaxations and constraint satisfaction

We now formalize a computational model of semideﬁnite relaxations for combinatorial optimization problems and prove strong lower bounds for it. Unlike the polytope setting in the previous section, this model also allows us to capture approximation algorithms directly.

Consider the following general optimization problem:2 Given a low-degree function f : {0,1}n → R, represented by its coeﬃcients as a multilinear polynomial,

maximize f(x) subject to x ∈ {0,1}n .

(1.1)

Many basic optimization problems are special cases of this general problem, corresponding to functions f of a particular form: For the problem of ﬁnding the maximum cut in a graph G with n vertices, the function f outputs on input x ∈ {0,1}n the number of edges in G that cross the bipartition represented by x, i.e., f(x) is the number of edges {i, j} ∈ E(G) with xi xj. Similarly, for max 3-sat on a 3CNF formula ϕ with n variables, f(x) is the number of clauses in ϕ satisﬁed by the assignment x. More generally, for any k-ary boolean constraint satisfaction problem, the function f counts the number of satisﬁed constraints. Note that in these examples, the functions have at most degree 2, degree 3, and degree k, respectively.

Algorithms with provable guarantees for these kinds of problems—either implicitly or explicitly—certify upper bounds on the optimal value of instances. (Indeed, for solving the decision version of these optimization problems, it is enough to provide such certiﬁcates.) It turns out that the best-known algorithms for these problems are captured by certiﬁcates of a particularly simple form, namely sums of squares of low-degree polynomials. The following upper bounds on problems of the form (1.1) are equivalent to the relaxations obtained by the sum-of-squares SDP hierarchy [Las01, Par00, Sho87]. For f : {0,1}n → R, we use deg(f) to denote the degree of the unique multilinear real polynomial agreeing with f on {0,1}n; see Section 2.1.

- Deﬁnition 1.3. The degree-d sum-of-squares upper bound for a function f : {0,1}n → R, denoted sosd(f), isthesmallest number c ∈ R suchthatc− f isa sumof squares offunctions ofdegreeat most d/2, i.e., there exists functions g1,..., gt: {0,1}n → R for some t ∈ N with deg(g1),...,deg(gt) d/2 such that the following identity between functions on the discrete cube holds:


![image 4](<2014-lee-lower-bounds-size-semidefinite_images/imageFile4.png>)

c − f = g21 + ··· g2t .

Every function f satisﬁes sosd(f) max(f) since sums of squares of real-valued functions are nonnegative pointwise. For d 1, the problem of computing sosd(f) for a given function f : {0,1}n → R (of degree at most d) is a semideﬁnite program of size at most 1 + nd/2 (see, e.g., Theorem 3.8).3

![image 5](<2014-lee-lower-bounds-size-semidefinite_images/imageFile5.png>)

![image 6](<2014-lee-lower-bounds-size-semidefinite_images/imageFile6.png>)

The sosd upper bound is equivalent to the degree-dsum-of-squares (also knownas the level-d/2 Lasserre) SDP bound, and for small values of d, these upper bounds underlie the best-known approximationalgorithmsforseveraloptimizationproblems. Forexample,theGoemans–Williamson algorithm for max cut is based on the upper bound sos2. If we let αGW ≈ 0.878 be the approximation ratio of this algorithm, then every graph G satisﬁes max(fG) αGW · sos2(fG) where the function fG measures cuts in G, i.e., fG(x) ij∈E(G)(xi − xj)2.

![image 7](<2014-lee-lower-bounds-size-semidefinite_images/imageFile7.png>)

![image 8](<2014-lee-lower-bounds-size-semidefinite_images/imageFile8.png>)

![image 9](<2014-lee-lower-bounds-size-semidefinite_images/imageFile9.png>)

A natural generalization of low-degree sum-of-squares certiﬁcates is obtained by summing squares of functions in a low-dimensional subspace. We can formulate this generalization as a non-uniform model of computation that captures general semideﬁnite programming relaxations. First, we make the following deﬁnition for a subspace of functions.

![image 10](<2014-lee-lower-bounds-size-semidefinite_images/imageFile10.png>)

- 2In this section, we restrict our discussion to optimization problems over the discrete cube. Some of our results also apply to other problems, e.g., the traveling salesman problem (albeit only for exact algorithms).
- 3Moreover, for every d ∈ N, there exists an nO(d)-time algorithm based on the ellipsoid method that, given f, c, and ε > 0, distinguishes between the cases sosd(f) c and sosd(f) c − ε (assuming the binary encoding of f, c, and ε is bounded by nO(d)).


![image 11](<2014-lee-lower-bounds-size-semidefinite_images/imageFile11.png>)

![image 12](<2014-lee-lower-bounds-size-semidefinite_images/imageFile12.png>)

- Deﬁnition 1.4. For a subspace U of real-valued functions on {0,1}n, the subspace-U sum-of-squares upper bound for a function f : {0,1}n → R, denoted sosU(f), is the smallest number c ∈ R such that c − f is a sum of squares of functions from U, i.e., there exist a g1,..., gt ∈ U such that c − f = g21 + ··· + g2t is an identity of functions on {0,1}n.


![image 13](<2014-lee-lower-bounds-size-semidefinite_images/imageFile13.png>)

Here, the subspace U can be thought of as “non-uniform advice” to an algorithm, where its dimension dim(U) is the size of advice. In fact, if we ﬁx this advice U, the problem of computing sosU(f) for a given function f has a semideﬁnite programming formulation of size dim(U).4 Moreover, it turns out that the generalization captures, in a certain precise sense, all possible semideﬁnite programming relaxations for (1.1). The dimension of the subspace corresponds to the size of the SDP. See Section 6.1 for a detailed discussion of the model.

![image 14](<2014-lee-lower-bounds-size-semidefinite_images/imageFile14.png>)

In this work, we exhibit unconditional lower bounds in this powerful non-uniform model of computation. For example, we show that the max 3-sat problem cannot be approximated to a factor better than 7/8 using a polynomial-size family of SDP relaxations. Formally, we show the following lower bound for max 3-sat.

Theorem 1.5. For every s > 7/8, there exists a constant α > 0 such that for every n ∈ N and every linear subspace U of functions f : {0,1}n → R with

log n

dimU nα

log logn ,

![image 15](<2014-lee-lower-bounds-size-semidefinite_images/imageFile15.png>)

there exists a max 3-sat instance ℑ on n variables such that max(ℑ) s but sosU(ℑ) = 1 (i.e., U fails to achieve a factor-s approximation for max 3-sat).

![image 16](<2014-lee-lower-bounds-size-semidefinite_images/imageFile16.png>)

Our main result is a characterization of an optimal semideﬁnite programming relaxation for the class of constraint satisfaction problems among all families of SDP relaxations of similar size. Roughly speaking, we show that the O(1)-degree sum-of-squares relaxations are optimal among all polynomial-sized SDP relaxations for constraint satisfaction problems. Towards stating our main result, we deﬁne the class of constraint satisfaction problems. For the sake of clarity, we restrict ourselves to boolean constraint satisfaction problems although the results hold in greater generality.

Fora ﬁnite collectionPofk-ary predicatesP: {0,1}k → {0,1}, we letmaxP- denotethefollowing optimization problem: An instance ℑ consists of boolean variables X1,...,Xn and a collection ofP-constraints P1(X) = 1,...,PM(X) = 1 over these variables. AP-constraint is a predicate P0: {0,1}n → {0,1}suchthatP0(X) = P(Xi1,...,Xik)forsomeP ∈Panddistinctindicesi1,...,ik ∈ [n]. The objective is to ﬁnd an assignment x ∈ {0,1}n that satisﬁes as many of the constraints as possible, that is, which maximizes

M

1 M

ℑ(x) def=

Pi(x).

![image 17](<2014-lee-lower-bounds-size-semidefinite_images/imageFile17.png>)

i=1

We denote the optimal value of an assignment for ℑ as opt(ℑ) = maxx∈{0,1}n ℑ(x). For example, max cut corresponds to the case wherePconsists of the binary inequality predicate. For max 3-sat,

- P contains all eight 3-literal disjunctions, e.g., X1 ∨ X¯2 ∨ X¯3.


![image 18](<2014-lee-lower-bounds-size-semidefinite_images/imageFile18.png>)

4Under mild conditions on the subspace U, there exists a boolean circuit of size (dimU)O(1) that given a constantdegree function f, and number c ∈ R and ε > 0, distinguishes between the cases sosU(f) c and sosU(f) c − ε (assuming the bit encoding length of f, c, and ε is bounded by (dimU)O(1).). Note that since we will prove lower bounds against this model, the possibility that some subspaces might not correspond to small circuits does not weaken our results.

![image 19](<2014-lee-lower-bounds-size-semidefinite_images/imageFile19.png>)

![image 20](<2014-lee-lower-bounds-size-semidefinite_images/imageFile20.png>)

Next, we discuss how to compare the quality of upper bound certiﬁcates of the form sosU. Let Π be a boolean CSP and let Πn be the restriction of Π to instances with n boolean variables. As discussed before, the problem Πn could for example be max cut on graphs with n vertices or max 3-sat on formulas with n variables. We say that a subspace U ⊆ R{0,1}n achieves a (c,s)-approximation for Πn if every instance ℑ ∈ Πn satisﬁes

![image 21](<2014-lee-lower-bounds-size-semidefinite_images/imageFile21.png>)

max(ℑ) s =⇒ sosU(ℑ) c. (1.2)

![image 22](<2014-lee-lower-bounds-size-semidefinite_images/imageFile22.png>)

In other words, the upper bound sosU allows us to distinguish5 between the cases max(ℑ) s and max(ℑ) > c for all instances ℑ ∈ Πn.

![image 23](<2014-lee-lower-bounds-size-semidefinite_images/imageFile23.png>)

We prove the following theorem, which shows that for every boolean CSP, the approximation guarantees obtained by the degree-d sum-of-squares upper bound (also known as the the level-d/2 Lasserre SDP relaxation) are optimal among all semideﬁnite programming relaxations of size at most ncd for some universal constant c > 0.

Theorem 1.6. Let Π be boolean constraint satisfaction problem and let Πn be the set of instances of Π on n variables. Suppose that for some m,d ∈ N, the subspace of degree-d functions f : {0,1}m → R fails to achieve a (c,s)-approximation for Πm (in the sense of (1.2)). Then there exists a number α = α(Πm,c,s) > 0 such that for all n ∈ N, every subspace U of functions f : {0,1}n → R with dimU α · (n/logn)d/4 fails to achieve a (c,s)-approximation for Πn.

The theorem has several immediate concrete consequences for speciﬁc boolean CSPs. First, we know that O(1)-degree sos upper bounds do not achieve an approximation ratio better than 7/8 for max 3-sat [Gri01b, Sch08], therefore Theorem 1.6 implies that polynomial-size SDP relaxations for max 3-sat cannot achieve an approximation ratio better than 7/8. In fact, a quantitatively stronger version of the above theorem yields Theorem 1.5.

Another concrete consequence of this theorem is that if there exists a polynomial-size family of semideﬁniteprogramming relaxations for maxcut thatachieves an approximation ratio betterthan αGW, then also a O(1)-degree sum-of-squares upper bound achieves such a ratio. This assertion is especially signiﬁcant in light of the notorious Unique Games Conjecture one of whose implications is that it is NP-hard to approximate max cut to a ratio strictly better than αGW.

### 1.3 Positive semideﬁnite rank and sum-of-squares degree

In order to prove our results on spectrahedral lifts and semideﬁnite relaxations, the factorization perspective will be essential. In the LP setting, the characterization of polyhedral lifts and LP relaxations in terms of nonnegative factorizations is a signiﬁcant contribution of Yannakakis [Yan91]. In the SDP setting, the analogous characterization is in terms of positive semideﬁnite factorizations [FMP+12, GPT11].

Deﬁnition 1.7 (PSD rank). Let M ∈ Rp+×q be a matrix with non-negative entries. We say that M admits a rank-r psd factorization if there exist positive semideﬁnite matrices {Ai : i ∈ [p]},{Bj : j ∈ [q]} ⊆ Sr+ such that Mi,j = Tr(AiBj) for all i ∈ [p], j ∈ [q]. We deﬁne rkpsd(M) to be the smallest r such that M admits a rank-r psd factorization. We refer to this value as the psd rank of M.

![image 24](<2014-lee-lower-bounds-size-semidefinite_images/imageFile24.png>)

5In order to distinguish between the cases max(ℑ) s and max(ℑ) > c it is enough to check whether ℑ satisﬁes sosU(ℑ) c. In the case max(ℑ) s, we know that sosU(ℑ) c by (1.2). On the other hand, in the case max(ℑ) > c, we know that sosU(ℑ) > c because sosU(ℑ) is always an upper bound on max(ℑ).

![image 25](<2014-lee-lower-bounds-size-semidefinite_images/imageFile25.png>)

![image 26](<2014-lee-lower-bounds-size-semidefinite_images/imageFile26.png>)

![image 27](<2014-lee-lower-bounds-size-semidefinite_images/imageFile27.png>)

![image 28](<2014-lee-lower-bounds-size-semidefinite_images/imageFile28.png>)

Nonnegative factorizations correspond to the special case that the matrices {Ai} and {Bj} are restricted to be diagonal. A rank-r nonnegative factorization can equivalently be viewed as a sum of r rank-1 nonnegative factorizations (nonnegative rectangles). Indeed, this viewpoint is crucial for all lower bounds on nonnegative factorization. In contrast, rank-r psd factorizations do not seem to admit a good characterization in terms of rank-1 psd factorizations. This diﬀerence captures one of the main diﬃculties of proving psd rank lower bounds.

Main theorem. Consider a nonnegative function f : {0,1}n → R+ on the n-dimensional discrete cube. We say that f has a sum-of-squares (sos) certiﬁcate of degree d if there exist functions

g1,..., gk: {0,1}n → R such that deg(g1),...,deg(gk) d/2, and f(x) = ki=1 gi(x)2 for all x ∈ {0,1}n. (Here, the deg(g) denotes the degree of g as a multilinear polynomial. We refer to Section 2.1 for

the precise deﬁnition.) We then deﬁne the sos degree of f, denoted degsos(f), to be the minimal d such that f has a degree-d sos certiﬁcate.

This notion is closely related6 to (a special case of) the Positivstellensatz proof system of Grigoriev and Vorobjov [GV02]. We refer to the surveys [Lau09, BS14] and the introduction of [OZ12] for a review of such proof systems and their relationship to semideﬁnite programming.

With this notion in place, we can now present a representative theorem that embodies our approach. For a point x ∈ Rn and a subset S ⊆ [n], we denote by xS ∈ R|S| the vector xS = (xi1,xi2,...,xi|S|) where S = {i1,i2,...,i|S|} and i1 < i2 < ··· < i|S|. For a function f : {0,1}m → R+ and a number n m, we deﬁne the following central object: The m n × 2n-dimensional real matrix Mnf is given by

Mnf(S,x) def= f(xS), (1.3) where S ⊆ [n] runs over all subsets of size m and x ∈ {0,1}n.

- Theorem 1.8 (Sum-of-squares degree vs. psd rank). For every m 1 and f : {0,1}m → R+, there exists a constant C > 0 such that the following holds. For n 2m, if d + 2 = degsos(f), then


1 + n1+d/2 rkpsd(Mnf) C

n logn

![image 29](<2014-lee-lower-bounds-size-semidefinite_images/imageFile29.png>)

d/4

.

Remark 1.9. The reader might observe that the matrix in (1.3) looks very similar to the “pattern matrices” deﬁned by Sherstov[She11]. This comparison is not unfounded; some high-level aspects ofourproofare quitesimilar tohis. Randomrestrictionsare a powerfultoolforanalyzing functions over the discrete cube. We refer to [O’D14, Ch. 4] for a discussion of their utility in the context of discrete Fourier analysis. They were also an important tool in the work [CLRS13] on lower bounds for LPs. Accordingly, one hopes that our methods may have additional applications in communication complexity. This would not be surprising, as there is a model of quantum communication that exactly captures psd rank (see [FMP+12]).

Connection to spectrahedral lifts of polytopes. The connection to psd lifts proceeds as follows. Let {x1,x2,...,xv} ⊆ P be such that P = conv(V) is the convex hull of V, and also ﬁx a representation

P = x ∈ Rn : ai,x bi ∀i ∈ [m] . The slack matrix S associated to P (and our chosen representation) is the matrix S ∈ Rm×v

+ given by Si,j = bi− ai,xj . Itisnotdiﬃculttoseethatrkpsd(S)does notdepend onthechoice ofrepresentation. It turns out that the psd rank of S is precisely the minimum size of a psd lift of P.

![image 30](<2014-lee-lower-bounds-size-semidefinite_images/imageFile30.png>)

6For the sake of simplicity, we have only deﬁned this notion for functions on the discrete cube. In more general settings, one has to be a bit more careful; we refer to [GV02].

- Proposition 1.10 ([FMP+12, GPT11]). For every n,k 1, every polytope P ⊆ Rn and every slack matrix S associated to P, it holds that rkpsd(S) k if and only if P admits a psd lift of size k.

Thus our goal in this paper becomes one of proving lower bounds on psd rank. With this notation, we have a precise way to characterize the lack of previous progress: Before this work, there was no reasonable method available to prove lower bounds on the psd rank of explicit matrices. The characterization of Proposition 1.10 explains our abuse of notation in Theorem 1.1, writing rkpsd(P) to denote the psd rank of any slack matrix associated to a polytope P.

Theorem 1.8 is already enoughto show that rkpsd(corrn) must grow faster than any polynomial in n, as we will argue momentarily. In Section 3.1, we present a more reﬁned version (using a more robust version of sos degree) that will allow us to achieve a lower bound of the form rkpsd(corrn) 2Ω(nδ) for some δ > 0.

Given Theorem 1.8, in order to prove a lower bound on rkpsd(corrn), we should ﬁnd, for every

d 1, a number m and a function f : {0,1}m → R+ such that degsos(f) d and such that Mnf is a submatrix of some slack matrix associated to corrn. To this end, it helps to observe the following (we recall the proof in Section 5).

- Proposition 1.11. If f : {0,1}m → R+ is a nonnegative quadratic function over {0,1}m, then for any n m, the matrix Mnf is a submatrix of some slack matrix associated to corrn.


Given the preceding proposition, the following result of Grigoriev on the Knapsack tautologies completes our quest for a lower bound.

- Theorem 1.12 ([Gri01a]). For every odd integer m 1, the function f : {0,1}m → R+ given by


 

 

2

m

m 2 −

1 4

−

f(x) =

xi

![image 31](<2014-lee-lower-bounds-size-semidefinite_images/imageFile31.png>)

![image 32](<2014-lee-lower-bounds-size-semidefinite_images/imageFile32.png>)

i=1

has degsos(f) m + 1.

(1.4)

Note that since m/2 is not an integer, (1.4) is nonnegative for all x ∈ {0,1}m. It turns out that in order to prove stronger lower bounds for corrn, we will require a lower bound on the approximate sos degree of f. Thus the Knapsack tautologies (1.4) will be studied carefully in Section 5.1. In Section 2.2, we discuss the proof of Theorem 1.8 in some detail. Then in Section 3, we present a quantitatively stronger theorem and its proof.

Connection to semideﬁnite relaxations and constraint satisfaction. Fix now numbers k,n 1 and a boolean CSP Π. Fix a pair of constants 0 s c 1. Suppose our goal is to show a lower bound on the size of SDP relaxations that yield a (c,s)-approximation on instances of size n. It turns out that this task reduces to proving a lower bound on the positive semideﬁnite rank of an explicit matrix M indexed by problem instances and problem solutions (points on the discrete cube in our case).

Proposition 1.13. For any boolean CSP Πn and any constants 0 s < c 1, let U be a subspace of minimal dimension that achieves a (c,s)-approximation for Πn. Denote the set of instances

Πn s = {ℑ | max(ℑ) s}. Let M: Πn s × {0,1}n → R denote the matrix

M(ℑ,x) = c − ℑ(x). Then, rkpsd(M)2 dim(U) rkpsd(M).

Before describing the proof of this proposition, observe that together with our main theorem the proposition implies Theorem 1.6 (optimality of degree-d sum-of-squares for approximating boolean CSPs): If ℑ0 is a maxP- instance on m variables with max(ℑ0) s and sosd(ℑ0) > c, then f = c − ℑ0 has sos degree larger than d. Our main theorem gives a lower bound on the psd rank of the matrix Mnf. Since this matrix is a submatrix of the matrix in Proposition 1.13, our psd rank lower bound implies a lower bound on the minimum dimension of a subspace achieving a (c,s)-approximation for maxP- n.

![image 33](<2014-lee-lower-bounds-size-semidefinite_images/imageFile33.png>)

Proof of Proposition 1.13. Set r = dim(U). Fix a basis q1,...,qr : {0,1}n → R for the subspace U. Deﬁne the function Q : {0,1}n → S+r by setting (Q(x))ij := qi(x)qj(x) for all i, j ∈ [r]. Notice that for any q ∈ U, we can write q = ri=1 λiqi and thus q(x)2 = Tr(ΛQ(x)) where Λ ∈ S+r is deﬁned by Λij := λiλj.

Since U achieves a (c,s)-approximation for Πn, for every instance ℑ ∈ Πn s we will have sosU(ℑ) c. By deﬁnition of sosU(ℑ), this implies that c− ℑ = i g2i for gi ∈ U. By expressing each g2i as g2i = Tr(ΛiQ(x)) for some Λi ∈ S+r we get,

![image 34](<2014-lee-lower-bounds-size-semidefinite_images/imageFile34.png>)

![image 35](<2014-lee-lower-bounds-size-semidefinite_images/imageFile35.png>)

M(ℑ,x) = c − ℑ(x) =

i

Tr(ΛiQ(x)) = Tr(ΛℑQ(x)) .

This yields an explicit psd factorization of M certifying that rkpsd(M) dim(U).

Conversely, by deﬁnition of rkpsd(M) there exists positive semideﬁnite matrices {Λℑ : ℑ ∈ Πn s}, {Q(x) : x ∈ {0,1}n} ⊆ S+r such that M(ℑ,x) = Tr(ΛℑQ(x)). Denote by R(x) := Q(x)1/2 the positive semideﬁnite square root, and consider the subspace U˜ := span{(R(x))ij} ⊆ R{0,1}n. Clearly, the dimension of U˜ is at most rkpsd(M)2. Further, for each instance ℑ ∈ Πn s, we can write

![image 36](<2014-lee-lower-bounds-size-semidefinite_images/imageFile36.png>)

c − ℑ = Mℑ,x = Tr(ΛℑQ(x)) = Tr(ΛℑR(x)2) = ΛℑR(x) 2F .

Observe that ΛℑR(x) 2F is a sum of squares of functions from the subspace U˜ 7. Therefore we have sosU˜ (ℑ) c, showing that sosU˜ yields a (c,s)-approximation to Πn. Since U is the minimal subspace yielding a (c,s)-approximation, we have dim(U) dim(U˜ ) rkpsd(M)2.

![image 37](<2014-lee-lower-bounds-size-semidefinite_images/imageFile37.png>)

![image 38](<2014-lee-lower-bounds-size-semidefinite_images/imageFile38.png>)

![image 39](<2014-lee-lower-bounds-size-semidefinite_images/imageFile39.png>)

## 2 Proof overview and setup

### 2.1 Preliminaries

We write [n] def= {1,2,... ,n} for n ∈ N. We will often use the notation Ex to denote a uniform averaging operator where x assumes values over a ﬁnite set. For instance, if x ∈ {−1,1}n, then

Ex f(x) = 2−n x∈{−1,1}n f(x). The domain of the operator should always be readily apparent from context. We also use asymptotic notation: For two expressions A and B, we write A O(B) if there exists a universal constant C such that A C · B. We also sometimes write A B to denote A O(B). The notation A Ω(B) similarly denotes B A, and the notations A = Θ(B) and A ≍ B are both used to denote the conjunction of A B and B A. For a real number x > 0, we use logx to denote the natural logarithm of x.

Inner product spaces and norms. Let H denote a ﬁnite-dimensional vector space over R equipped with an inner product  ·,·  and the induced Euclidean norm | · |. All vector spaces we consider here will be of this kind. We use M(H) to denote the set of self-adjoint linear operators on H, and

![image 40](<2014-lee-lower-bounds-size-semidefinite_images/imageFile40.png>)

7Here,  · F denotes the Frobenius norm.

D(H) ⊆ M(H) for the set of density operators on H, i.e., those positive semideﬁnite operators with trace one. We will use the standard Loewner ordering on M(H).

If H comes equipped with a canonical (ordered) orthonormal basis (as will always be the case throughout), we represent linear operators on H by matrices with rows and columns indexed by the basis elements. In this case, M(H) consists of symmetric matrices and D(H) consists of symmetric, positive semideﬁnite matrices whose diagonal entries summing to one. If A ∈ M(H) is positive semideﬁnite, we use A1/2 to denote the positive semideﬁnite square root of A.

Given a linear operator A : H → H, we deﬁne the operator, trace, and Frobenius norms, respectively:

|Ax| |x| A ∗ = Tr(

A = max

![image 41](<2014-lee-lower-bounds-size-semidefinite_images/imageFile41.png>)

x 0

√

![image 42](<2014-lee-lower-bounds-size-semidefinite_images/imageFile42.png>)

ATA) A F = Tr(ATA).

![image 43](<2014-lee-lower-bounds-size-semidefinite_images/imageFile43.png>)

Recall Tr(ATB) A · B ∗ and the Cauchy-Schwarz inequality Tr(ATB) A F B F. For a matrix M, we use M ∞ to denote the maximum absolute value of an entry in M.

Fourier analysis and degree over the discrete cube. We use L2({−1,1}n) to denotethe Hilbert space of real-valued functions f : {−1,1}n → R. This space is equipped with the natural inner product under the uniform measure: f, g = Ex f(x)g(x). We recall the Fourier basis: For S ⊆ [n], one has χS(x) = i∈S xi. The functions {χS : S ⊆ [n]} form an orthonormal basis for L2({−1,1}n). We can decompose f in the Fourier basis as f = S⊆[n] fˆ(S)χS.

We will use deg(f) to denote the degree of f as a multi-linear polynomial on the discrete cube: deg(f) def= max{|S| : fˆ(S) 0}. Note that by identifying {0,1} and {−1,1}, we can deﬁne deg(f) for functions f : {0,1}n → R as well. (Since the change of domains is given by the linear map x  → 2x − 1, the degree of polynomial representations do not change.)

If we are given a matrix-valued function M : {−1,1}n → Rp×q, we can decompose M as

M = S⊆[n] Mˆ SχS where (Mˆ S)ij = Mij(S), and deg(M) = max{deg(Mij) : i ∈ [p], j ∈ [q]}. We refer to the book [O’D14] for additional background on boolean Fourier analysis.

Quantum information theory. The von-Neumann entropy of a density operator X is denoted S(X) = −Tr(X logX). For two density operators X and Y over the same vector space, the quantum relative entropy of X with respect to Y is the quantity S(X Y) = Tr(X · (logX − logY)). Here, the operator function log is deﬁned on positive operators as logX = − ∞k=0

1

k(Id−X)k. In general, for a function g : I → R analytic on an open interval I ⊆ R and a symmetric operator X ∈ M(H), we deﬁne g(X) via its Taylor series, with the understanding that the spectrum of X should lie in I. Finally, we will often use the notation U = Tr(Id)Id to denote the uniform density matrix (i.e., the maximally mixed state), where the dimension of the identity matrix Id is clear from context. We refer to [Wil13] for a detailed account of quantum information theory.

![image 44](<2014-lee-lower-bounds-size-semidefinite_images/imageFile44.png>)

![image 45](<2014-lee-lower-bounds-size-semidefinite_images/imageFile45.png>)

### 2.2 Factorizations, quantum learning, and pseudo-densities

First, we recall the setup of the main theorem in the paper. Fix m 1, a function f : {0,1}m → R+ and let d + 2 = degsos(f). We deﬁne the matrix Mnf as in (1.3). Our goal is to show a lower bound on the positive semideﬁnite rank of the matrix Mnf.

Suppose we had a psd factorization Mnf(S,x) = Tr(P(S)Q(x)) (2.1)

witnessing rkpsd(M) r. First, we observe that lower bound on degsos(f) already precludes certain low degree psd factorizations. More precisely, if R(x) = Q(x)1/2 then deg(R) is constrained to be at

least d/2. For the sake of contradiction, let us suppose deg(R) < d/2. For any row Mnf(S,·) of the matrix Mnf we will have,

![image 46](<2014-lee-lower-bounds-size-semidefinite_images/imageFile46.png>)

f(xS) = Tr(P(S)R(x)2) = P(S)R(x) 2F .

![image 47](<2014-lee-lower-bounds-size-semidefinite_images/imageFile47.png>)

This contradicts degsos(f) = d+2 since P(S)R(x) 2F is a sum of squares of a polynomials of degree less than d/2.

Pseudo-densities and low degree psd factorizations. By appealing to convex duality, it is possible to construct a certiﬁcate that the matrix Mnf does not admit low degree factorizations. The certiﬁcate consists of a linear functional that separates Mnf from the convex hull of matrices that admit low degree psd factorizations. Formally, if we deﬁne the convex set Cd of non-negative matrices as,

Cd def= N :

n m × {0,1}n → R N(S,x) = Tr(P(S)R(x)2),P(S) 0,deg(R(x)) < d/2

then we will construct a linear functional L on m n × 2n matrices such that

L(Mnf) < 0, but L(N) 0 for all N ∈ Cd . (2.2) The linear functional is precisely the one derived from what we refer to as a pseudo-density.

Adegree-d pseudo-density isa mappingD: {0,1}m → RsuchthatEx D(x) = 1and Ex D(x)g(x)2 0 for all functions g: {0,1}m → R with deg(g) d/2.8 Observe that for any probability distribution over {0,1}n, its density function relative totheuniform distributionon {0,1}n satisﬁestheconditions of a degree-d pseudo-density for every d ∈ N. One has the following characterization:

D(x)f(x) 0 for every degree-d pseudo-density D . (2.3)

degsos(f) = min d 0 : E

x

In other words, the sos degree of a function is larger than d if and only if there exists a degree-d pseudo-density D such that Ex D(x)f(x) < 0. To verify this, note that if degsos(f) > d, then f is not in the closed, convex cone generated by the squares of polynomials of degree at most d/2. Now the required pseudo-density D corresponds exactly to (the normal vector of) a hyperplane separating f from this cone.

Of course, if D is an actual density (with respect to the uniform measure on {0,1}m), then Ex D(x)f(x) is precisely the expectation of f under D. For a pseudo-density D, the corresponding linear functional f  → Ex D(x)f(x) is referred to as a pseudo-expectation in previous papers (see, e.g., [BBH+12, CLRS13]), and the map D is called a pseudo-distribution in [BKS14]. Over ﬁnite domains, these notions are interchangeable. We use the language of densities here in anticipation of future applications to inﬁnite domains and non-uniform background measures (in the context of nonnegative rank, this occurs already in Section 7.2).

Now ﬁx a degree-d pseudo-density D with Ex D(x)f(x) < 0. We deﬁne the following linear functional on matrices N: [mn] × {0,1}n → R:

LD(N) def= E

D(xS) · N(S,x). (2.4)

E

x

|S|=m

![image 48](<2014-lee-lower-bounds-size-semidefinite_images/imageFile48.png>)

8Note that a degree-d pseudo-density does not necessarily have degree d as a function on the discrete cube.

Consider a matrix N ∈ Cd which admits a low degree psd factorization given by N(S,x) = Tr(P(S)R(x)2). Then since D is a degree-d pseudo-density, we would have

![image 49](<2014-lee-lower-bounds-size-semidefinite_images/imageFile49.png>)

D(xS)Tr P(S)R(x)2 = E

D(xS) P(S)R(x) 2F 0. However, since D is negatively correlated with f,

LD(N) = E

E

E

x

x

|S|=m

|S|=m

LD(Mnf) = E

|S|=m

D(xS) · Mnf(S,x) = E

E

x

|S|=m

D(xS) · f(xS) < −ε. (2.5)

E

x

for some ε > 0. The core of our psd rank lower bound is to show that the linear functional LD in fact separates

the matrix Mnf from all low rank psd factorizations, thereby certifying a lower bound on rkpsd(Mnf). Roughly speaking, the idea is to approximate an arbitrary psd factorization using low degree

factorizations with respect to the linear functional LD, and then appeal to the lower bound (2.2) for low degree factorizations.

Formally, for a number r 1, consider the following set Cr of nonnegative matrices,

(mn)×{0,1}n

Cr def= N ∈ R

+ : rkpsd(N) r · N 1, N ∞ 1 .

Here, N 1 is the average of the entries of N and N ∞ is the maximum entry of N. In the rest of the section, we will present an argument that unless r is very large, every matrix N ∈ Cr satisﬁes LD(N) −ε. Since LD(Mnf) < −ε, this implies that the linear functional LD separates Mnf from the convex hull of Cr, thereby certifying a lower bound on rkpsd(Mnf).

Fix a matrix N ∈ Cr. It is instructive to have the situation N 1, N ∞ = Θ(1) in mind for the rest of this outline. By deﬁnition of Cr, the matrix N admits a psd factorization of rank O(r). In light of the above discussion, our goal is to approximate the matrix N by a low degree factorization with respect to the functional LD. A low degree approximation for N is constructed in two steps.

Well-behaved factorizations. The ﬁrst step involves obtaining a nicer factorization of N. Toward this end, we deﬁne the quantity

γr(M) def= sup max

i,j

Ai · Bj ∗ : Nij = Tr(AiBj),Ai,Bj ∈ Sr+ ∀i ∈ [p], j ∈ [q] ,

associated with a matrix M ∈ Rp+×q. The following lemma is proved by Briët, Dadush, and Pokutta [BDP13] (see also the discussion in [FGP+14]).

- Lemma 2.1 (Factorization rescaling). For every nonnegative matrix M with rkpsd(M) r, the following holds:


γr(M) r2 M ∞ .

Applying the above lemma to the matrix N at hand, we get a psd factorization N(S,x) = Tr(P(S)Q(x)) wherein P(S) and Q(x) ∗ are bounded polynomially in r. This analytic control on the factorization will be important for controlling error bounds, but also—in a more subtle way—for the next step.

Learning a low-degree quantum approximation. The next step of the argument exploits the following phenomenon concerning quantum learning. Fix a k 1 and consider a matrix-valued function Q : {0,1}n → Sk+ such that Ex Tr(Q(x)) = 1. We will try to approximate Q by a simpler

mapping with respect to a certain class of test functionals Λ : {0,1}n → Sk+. If Q˜ is the approximator, we would like that

Ex Tr Λ(x)(Q(x) − Q˜(x)) ε (2.6) for some parameter ε > 0. (In this case, Q˜ and Q are indistinguishable to the test Λ up to accuracy ε.) One can set this up as a quantum learning problem in the following way. We deﬁne the density matrix UQ = Ex(exeTx ⊗ Q(x)) and the PSD matrix VΛ = x(exeTx ⊗ Λ(x)).9 Note that Ex Tr(Λ(x)Q(x)) = Tr(VΛUQ).

Now, if T is a family of test functionals, then a canonical way of ﬁnding a “simple” approximation to UQ that satisﬁes all the tests is via the following maximum-entropy (convex) optimization problem:

max S(U˜ ) : Tr(U˜ ) = 1,U˜ 0,|Tr(VΛ(UQ − U˜ ))| ε ∀Λ ∈ T , (2.7)

where we recall that S(·) denotes the quantum entropy functional. Moreover, one can attempt to solve this optimization by some form of projected sub-gradient descent. Interpretations of this algorithm go by many names, notably the “matrix multiplicative weights update method” and “mirror descent” with quantum entropy as the regularizer; see, e.g., [NY83, BT03, TRW05, AK07, WK12] and the recent survey [Bub14].

In our setting, we are not directly concerned with eﬃciency, but instead simplicity of the approximator. A key phenomenon is that when the class of tests T is simple, the approximator inherits this simplicity. Moreover, one can tailor the nature of the approximator by choosing the sub-gradient steps wisely. In Section 4.2 (Theorem 4.5), we prove a generalization of the following approximation theorem. (Recall that U = Id/Tr(Id) is the uniform density matrix.)

- Theorem 2.2 (Approximation by a low-degree square). Let κ 1 and ω > 0 be given. Deﬁne


Tκ,ω = Λ : {0,1}n → Sk+ : deg(Λ) κ, Λ(x) ω ∀x ∈ {0,1}n .

For any Q : {0,1}n → Sk+ with Ex Tr(Q(x)) = 1, there is a matrix-valued function R : {0,1}n → Sk+ with Ex Tr(R(x)2) = 1 satisfying

deg(R) κ

ω ε

1 + S(UQ  U)

, (2.8) and for all tests Λ ∈ Tκ,ω,

![image 50](<2014-lee-lower-bounds-size-semidefinite_images/imageFile50.png>)

![image 51](<2014-lee-lower-bounds-size-semidefinite_images/imageFile51.png>)

Tr Λ(x)(Q(x) − R(x)2) ε.

E

x

In other words, the learning algorithm produces a hypothesis with error at most ε for all the tests in Tκ,ω; moreover, the hypothesis is the square of a polynomial whose degree is not much larger than that of the tests. The value ω corresponds to the ubiquitous “width” parameter and, as in most applications of the multiplicative weights method, bounding ω will be centrally important. The reader should also take note of the appearance of the relative entropy in the degree bound (2.8). It will turn out that low psd rank factorizations will give us functions Q : {0,1}n → Sk+ with high entropy (and thus small relative entropy with respect to the uniform state); this is actually a direct consequence of the factorization rescaling in Lemma 2.1.

Notice that the separating functional LD induces a test of degree at most m. Therefore, if one

takes for granted, as claimed above, that S(UQ Tr(Id) Id ) is small when Q comes from a low psd rank factorization, then Theorem 2.2 suggests that we might think of Q(x) as being a low-degree square.

![image 52](<2014-lee-lower-bounds-size-semidefinite_images/imageFile52.png>)

![image 53](<2014-lee-lower-bounds-size-semidefinite_images/imageFile53.png>)

9In the quantum information literature, these are sometimes called QC states for “quantum/classical.”

Proof sketch for Theorem 1.8. We have all the ingredients to sketch a proof of Theorem 1.8. First, suppose that degsos(f) > d so that by (2.3), there exists a degree-d pseudo-density D with Ex f(x)D(x) < −ε f ∞ for some ε > 0. (We do not specify any quantitative bound on ε at the moment, but we write it this way to indicate how one can get improved bounds under stronger assumptions.)

Then from the deﬁnition of Mnf, we have

LD(Mnf) < −ε Mnf ∞ . (2.9) On the other hand, we will prove the following theorem in Section 3.1.

- Theorem 2.3. For every m,d 1, every ε ∈ (0,1], and every degree-d pseudo-density D : {0,1}m → R,


there exists a number α > 0 such that for every n 2m and every nonnegative matrix N: [mn] ×{0,1}n → R satisfying

N ∞ 1, and 1

N 1rkpsd(N)2 α(n/logn)d/2 , we have LD(N) −ε.

![image 54](<2014-lee-lower-bounds-size-semidefinite_images/imageFile54.png>)

Now if we consider the normalized matrix N = Mnf/ Mnf ∞, we see that it satisﬁes the ﬁrst premise N ∞ 1 but violates the conclusion of the theorem (because of (2.9)). Therefore we know that the second premise is violated, which gives the lower bound

rkpsd(N)2 > α(n/logn)d/2 · N 1 = α(n/logn)d/2 E x

f(x).

Since this achieves our goal, we are left to explain why Theorem 2.3 should be true, at least when we apply it with N = Mnf/ Mnf ∞. If we apply LD to the right-hand side of (2.1)—our presumed factorization for Mnf—we arrive at the expression

LD(Mnf) = E x

Tr E

D(xS)P(S)Q(x) . (2.10)

|S|=m

We can view this as a test on Q in the sense of Theorem 2.2. Since deg(D) m (because D is only a function of m variables), this is a low-degree test. Theorem 2.2 then suggests that we can replace

- Q by a low-degree approximator R2, while losing only ε in the “accuracy” of the test. Since the approximation property implies that Q(x) and R(x)2 should perform similarly under


the test (up to the “accuracy” ε), we would conclude that LD(Mnf) −ε, yielding the conclusion of

- Theorem 2.3.


Random restriction and degree reduction. The one serious issue with the preceding argument is that our supposition is far too strong: One cannot expect to have deg(R) d/2. Indeed, the guarantee of Theorem 2.2 tells us that the approximator R(x) has degree at most K · deg(D) for some (possibly large) number K (which itself depends on many parameters). To overcome this problem, we use another crucial propertyof our functional (2.4): It is an expectation over small sets S ⊆ [n]. If we randomly choose such a subset with |S| = m ≪ n and randomly choose values yS¯ for the variables in S¯, we expect that the resulting (partially evaluated) polynomial R(xS,xS¯)|xS¯=yS¯ will satisfy deg(R(xS,xS¯)|xS¯=yS¯) ≪ deg(R). (Strictly speaking, this will only be true in an approximate sense.)

It is precisely this degree reduction property of random restriction that saves the preceding sketch. In the next sections, we perform a more delicate quantitative analysis capable of achieving much stronger lower bounds. The norm D ∞ of the pseudo-density will play a central role in this study. Thus in Section 5.1, we show that Grigoriev’s proof of Theorem 1.12 can be carefully recast in the language of pseudo-densities such that the resulting pseudo-density has small norm.

## 3 PSD rank and sum-of-squares degree

We now move to proving the main technical theorems of the paper along the lines of the informal overview presented in Section 2.2.

### 3.1 Analysis of the separating functional

Recall that for a pseudo-density D: {0,1}m → R and n 1, we deﬁne a linear functional LD on matrices N: [mn] × {0,1}n → R

LD(N) def= E x

D(xS)N(S,x),

E

S

where the expectation over S is a uniform average over all S ⊆ [n] with |S| = m (as will be the case throughout this section). We will use the notation N ∞ = maxS,x N(S,x) and N 1 = ES,x N(S,x).

We prove the following quantitative version of Theorem 3.1. As discussed in Section 2.2, this

theorem implies a lower bound on the rkpsd(Mnf) in terms of degsos(f). This implication will be proved formally in Section 3.3.

- Theorem 3.1 (Strengthening of Theorem 2.3). For every m,d 1, every ε ∈ (0,1], and every degree-d pseudo-density D: {0,1}m → R, there exists a number α > 0 such that whenever n 2m and a nonnegative matrix N: [mn] × {0,1}n → R satisﬁes


N ∞ 1, 1

N 1rkpsd(N)2 α(n/logn)d/2 , we have LD(N) −ε. Moreover, this holds for

![image 55](<2014-lee-lower-bounds-size-semidefinite_images/imageFile55.png>)

d/2 ε D ∞

3

Cε dm2 D ∞

,

α =

![image 56](<2014-lee-lower-bounds-size-semidefinite_images/imageFile56.png>)

![image 57](<2014-lee-lower-bounds-size-semidefinite_images/imageFile57.png>)

where C > 0 is a universal constant.

The proof of this theorem consists of two parts. First, we observe that if D is a degree-d pseudodensity, then LD(N) is nonnegative for all matrices N that admit a factorization in terms of squares of low-degree polynomials, i.e., a factorization N(S,x) = Tr(A2SB2x) for symmetric matrics {AS} and {Bx} such that the function x  → Bx has degree at most d/2 over {0,1}n.10 Indeed, consider such a factorization. Then,

LD(N) = E x

E

S

D(xS)Tr(A2SB2x) = E S

D(xS) ASBx 2F 0,

E

x

![image 58](<2014-lee-lower-bounds-size-semidefinite_images/imageFile58.png>)

10For the convenience of the reader, we recall that the degree of the matrix-valued function x  → Bx is deﬁned as the maximum degree of the functions x  → (Bx)ij where i, j range over the indices of Bx.

where the inequality used the fact that D is a degree-d pseudo-density (hence Ex D(x)g(x)2 0 whenever deg(g) d/2).

As explained in Section 2.2, this guarantee is not suﬃcient for us. The following theorem (proved in Section 3.2) allows us to analyze LD even when the degree of the map x  → Bx is much larger than d/2. (For m no(1), it will be the case that the linear functional LD is approximately nonnegative on N even when x  → Bx has degree up to no(1)).

- Theorem 3.2 (Degree reduction). Consider postive numbers n 1 and d,k,m n. Let D: {0,1}m → R

be a degree-d pseudo-density. Let N′: [mn] × {0,1}n → R be a matrix that admits a factorization N′(S,x) = TrA2SB2x for symmetric matrices {AS} and {Bx} such that the matrix-valued function x  → Bx has degree at most ℓ. Then,

LD(N′) −

ℓm n − m

![image 59](<2014-lee-lower-bounds-size-semidefinite_images/imageFile59.png>)

d/4

D ∞ · max

S

A2S · E

x

Tr(B2x) · E x

E

S

N′(S,x)

1/2

.

With this theorem in place, our goal is to approximate every matrix N with low psd rank by a matrix N′ that satisﬁes the premise of Theorem 3.2 for a reasonable value of ℓ. Here, our notion of approximation is fairly weak. We only require LD(N) LD(N′)−ε for suﬃciently small ε > 0. As a preliminary step, the following general theorem about psd factorizations allows us to assume that the factorization for N is appropriately scaled. Recall that U = Id/Tr(Id) is the uniform density matrix.

- Theorem 3.3 (psd factorization scaling). For every nonnegative matrix M ∈ Rp×q and every η ∈ (0,1], there exist psd matrices {Pi}i∈[p] and {Qj}j∈[q] with the following properties:


- 1. Mi,j Tr(PiQj) Mi,j + η M ∞,
- 2. 1p pi=1 Pi = Id,

![image 60](<2014-lee-lower-bounds-size-semidefinite_images/imageFile60.png>)

- 3. Pi 2rkpsd(M)2/η for all i ∈ [p],
- 4. Qj M ∞(η + rkpsd(M)2)rkpsd(M)U for all j ∈ [q].


Proof. Let r = rkpsd(M). By Lemma 2.1, we have γ := γr(M) r2 M ∞. Fix a factorization Mi,j = Tr(AiBj) such that maxi,j Ai · Bj ∗ = M ∞ · rkpsd(M)2 and Ai,Bj ∈ Rr×r. By an appropriate normalization, we may assume Ai,Bj 0 and Ai γ, Bj ∗ 1. To construct psd matrices {Pi} and {Qj} with the desired properties, make the following deﬁnitions:

p

1 p

A = η M ∞ Id+

Ai

![image 61](<2014-lee-lower-bounds-size-semidefinite_images/imageFile61.png>)

i=1

Pi = A−1/2(η M ∞ Id+Ai)A−1/2 Qj = A1/2BjA1/2 .

Note that Item 2 holds by construction. Also observe that

Tr(PiQj) = Mi,j + η M ∞ Tr(A−1A1/2BjA1/2) = Mi,j + η M ∞ Tr(Bj), verifying Item 1. Finally, we have the inequalities for all i ∈ [p], j ∈ [q],

γ η M ∞

1 η M ∞

(η M ∞ + Ai ) 1 +

,

Pi

![image 62](<2014-lee-lower-bounds-size-semidefinite_images/imageFile62.png>)

![image 63](<2014-lee-lower-bounds-size-semidefinite_images/imageFile63.png>)

Qj ∗ A · Bj ∗ γ + η M ∞ . The ﬁrst inequality veriﬁes Item 3 since r 1 and η 1. The last inequality implies that

Id Tr(Id)

Id Tr(Id) for all j ∈ [q], verifying Item 4.

r M ∞(η + r2)

Qj (γ + η M ∞)r

![image 64](<2014-lee-lower-bounds-size-semidefinite_images/imageFile64.png>)

![image 65](<2014-lee-lower-bounds-size-semidefinite_images/imageFile65.png>)

Consider a matrix of the form N : [mn] × {0,1}n → R+ with N ∞ 1 and let ε > 0 be given. Apply Theorem 3.3 with a value η ∈ (0,1] to be chosen later to obtain a factorization

N(S,x) = Tr(PSQx) satisfying the conclusions of the theorem.

We can view the matrix-valued function x  → Qx as a density matrix Q = E 1

x(TrQx) Ex(exeTx ⊗ Qx). (The ﬁrst n bits in this density matrix are “classical” and their marginal distribution has density x  → TrQx. If we condition Q on an assignment x ∈ {0,1}n to the ﬁrst n bits, the resulting quantum state is Tr1Q

![image 66](<2014-lee-lower-bounds-size-semidefinite_images/imageFile66.png>)

Qx). Here, the normalization factor τ = Ex TrQx for the density matrix Q satisﬁes

![image 67](<2014-lee-lower-bounds-size-semidefinite_images/imageFile67.png>)

x

  

(Thm 3.3(1)

ES Ex N(S,x) = N 1 ,

TrQx (Thm=3.3(2)) E x

τ = E

TrPSQx

(3.1)

E

(Thm 3.3(1))

x

S

ES Ex N(S,x) + η 1 + η,

where the last inequality has used N ∞ 1. From Theorem 3.3(4), the density matrix Q satisﬁes

(η + rkpsd(N)2)rkpsd(N)

τ U . Therefore,

Q

![image 68](<2014-lee-lower-bounds-size-semidefinite_images/imageFile68.png>)

S(Q U) log(ηrkpsd(N)/τ) log rkpsd(N)/ N 1 . (3.2)

- Theorem 3.3(1) allows us to lower bound LD(N) in terms of the matrix (S,x)  → Tr(PSQx) and value D ∞:


D(xS)N(S,x) E

LD(N) = E x

E

S

D(xS) · Tr(PSQx) − η D ∞ (by Theorem 3.3(1))

E

x

S

= τ · Tr(FQ) − η D ∞ , (3.3) where F is the symmetric matrix

exeTx ⊗ Fx with Fx = E S

D(xS)PS. (3.4)

F =

x∈{0,1}n

Theorem 3.3(2) allows us to upper bound the spectral norm of F by

F max

x

PS (Thm=3.3(2)) D ∞. (3.5)

D(xS)PS D ∞ · E S

E

S

The nexttheorem allows us to lower bound Tr(FQ) by replacing Q with a simpler density matrix that is a low-degree polynomial in F. (See Theorem 4.1, where a slightly more general version is proved.)

- Theorem 3.4 (Density matrix approximation). Let H be some ﬁnite-dimensional real inner-product space. Let F ∈ M(H) be a symmetric matrix and let Q ∈ D(H) be a density matrix. Then, for every ε > 0, there exists a degree-k univariate polynomial p with k (1 + S(Q U)) ·  F /ε such that the density matrix


Q˜ = Trp1(F)2p(F)2 satisﬁes

![image 69](<2014-lee-lower-bounds-size-semidefinite_images/imageFile69.png>)

Tr FQ˜ Tr(FQ) + ε. (3.6)

Apply Theorem 3.4 to the density matrix Q and the symmetric matrix F deﬁned above with the value ε (which is already ﬁxed). Let p be the resulting degree-k polynomial, with k satisfying the bounds of the theorem.

Since the function x  → Fx has deg(F) deg(D) m (since D : {0,1}m → R), the degree of the map x  → Q˜x = E 1

xTr(p(Fx)2)p(Fx)2 is at most deg(p) · m = k · m. Applying Theorem 3.2 to the matrix given by N′(S,x) = Tr(PS · p(Fx)2), we can give a lower bound:

![image 70](<2014-lee-lower-bounds-size-semidefinite_images/imageFile70.png>)

Trp(Fx)2 · Tr F · Q˜ = E S

D(xS)Tr PS · p(Fx)2

E

E

x

x

d/4

km2 n − m

1/2

N′(S,x)

Tr(p(Fx)2) · E x

−

· D ∞ · max

PS · E x

.

E

![image 71](<2014-lee-lower-bounds-size-semidefinite_images/imageFile71.png>)

S

S

Using the fact that Ex ES N′(S,x) = ES Ex TrPS · p(Fx)2 = Ex Trp(Fx)2 from Theorem 3.3(2) and the fact that maxS PS 2rkpsd(N)2/η from Theorem 3.3(3) yields

d/4 D ∞ √η

km2 n − m

Tr F · Q˜ −

rkpsd(N). (3.7)

![image 72](<2014-lee-lower-bounds-size-semidefinite_images/imageFile72.png>)

![image 73](<2014-lee-lower-bounds-size-semidefinite_images/imageFile73.png>)

![image 74](<2014-lee-lower-bounds-size-semidefinite_images/imageFile74.png>)

We have now assembled all components of the proof of Theorem 3.1.

- Proof of Theorem 3.1. We lower bound the linear functional LD(N) by


(3.3)

τ · Tr(FQ) − η D ∞

LD(N)

- (3.6)

τ · Tr(F · Q˜) − ε − η D ∞

- (3.7)


d/4

km2 n − m

D ∞ √η

·

−cτ ·

rkpsd(N) − τ · ε − η D ∞ ,

![image 75](<2014-lee-lower-bounds-size-semidefinite_images/imageFile75.png>)

![image 76](<2014-lee-lower-bounds-size-semidefinite_images/imageFile76.png>)

![image 77](<2014-lee-lower-bounds-size-semidefinite_images/imageFile77.png>)

where c > 0 is a universal constant. Now set η := min(ε/ D ∞,1) and use (3.1) to bound τ 1 + η 2. This yields

LD(N) −2c

km2 n − m

![image 78](<2014-lee-lower-bounds-size-semidefinite_images/imageFile78.png>)

d/4

D 3∞/2 √ε

·

rkpsd(N) − 3ε (3.8)

![image 79](<2014-lee-lower-bounds-size-semidefinite_images/imageFile79.png>)

![image 80](<2014-lee-lower-bounds-size-semidefinite_images/imageFile80.png>)

Now recall that our invocation of Theorem 3.4 gives us a bound on k = deg(p):

(3.5), (3.2)

k (1 + S(Q U)) · F /ε

log rkpsd(N)/ N 1

D ∞ ε

. (3.9)

![image 81](<2014-lee-lower-bounds-size-semidefinite_images/imageFile81.png>)

If rkpsd(N)2/ N 1 satisﬁes the upper bound in the theorem, then the degree bound (3.9) above gives

k ε 1 · d D ∞ · logn.

![image 82](<2014-lee-lower-bounds-size-semidefinite_images/imageFile82.png>)

Plugging this bound into (3.8) yields, for some constant c′ > 0,

d/4

D 3∞/2 √ε

c′d D ∞m2 logn ε(n − m)

·

LD(N) −

rkpsd(N) − 3ε

![image 83](<2014-lee-lower-bounds-size-semidefinite_images/imageFile83.png>)

![image 84](<2014-lee-lower-bounds-size-semidefinite_images/imageFile84.png>)

![image 85](<2014-lee-lower-bounds-size-semidefinite_images/imageFile85.png>)

Since N 1 N ∞ 1, if rkpsd(N) satisﬁes the upper bound in the theorem (for a suﬃciently small constant α), this lower bound is LD(N) −4ε as desired (up to scaling by a factor of 4).

- 3.2 Degree reduction The next theorem is a restatement of Theorem 3.2. One should simply note that for any symmetric matrix A, we have A 2F = Tr(A2).


- Theorem 3.5 (Restatement of Theorem 3.2). Let positive integers n 1 and m,d,ℓ n be given.


Suppose A: m n → Rp×p and B: {0,1}n → Rp×p are two functions taking symmetric matrices as values. Let D: {0,1}m → R be a degree-d pseudo-density and suppose that deg(B) ℓ. Then,

D(xS) A(S)B(x) 2F

E

S,x

d/4

1/2

1/2

1/2

ℓm (n − m)

A(S)2

A(S)B(x) 2F

B(x) 2F

· max

· E

−2 D ∞

,

E

![image 86](<2014-lee-lower-bounds-size-semidefinite_images/imageFile86.png>)

x

S,x

S

Proof. For thesake of this lemma, which usesFourieranalysis, we will think of B and D as functions on {−1,1}n. Since this is a linear transformation on the domain, it does not aﬀect their degrees as multilinear polynomials.

For every S ⊆ [n] with |S| = m, we decompose B into two parts B = BS,low + BS,high such that BS,low is the part of B with degree at most d/2 in the variables S:

Bˆαχα .

BS,low =

α⊆[n] |α∩S| d/2

(Recall Section 2.1 for the Fourier-analytic deﬁnitions.) The proof consists of two steps that are captured by the following two lemmas.

- Lemma 3.6. Let τ = maxS A(S)2 . Then,


D(xS) A(S)B(x) 2F −2√τ D ∞ · E S,x

BS,high(x) 2F

![image 87](<2014-lee-lower-bounds-size-semidefinite_images/imageFile87.png>)

E

S,x

1/2

A(S)B(x) 2F

· E

S,x

1/2

Proof. For ease of notation, we will treat A = A(S) and B = B(x) as matrix-valued random variables that are determined by choosing x ∈ {−1.1}n and S ⊆ [n] with |S| = m uniformly and independently at random. In this notation, we are to lower bound the expectation ED(xS) AB 2F (over the joint distribution of x, S, A, and B).

Let Blow = BS,low(x) and Bhigh = BS,high(x) be matrix-valued random variables in the same probability space. By construction, the Fourier transforms of the functions x  → BS,low(x) and x  → BS,high(x) have disjoint support for every subset S. Therefore, the expectation satisﬁes EBlowBThigh = 0. This fact allows us to control the expectations of ABlow 2F and ABhigh 2F,

E ABlow 2F + E ABhigh 2F = E AB 2F

Here, we have used that the quadratic formula AB 2F = ABlow 2F + ABhigh 2F + 2 ABlow,ABhigh , where  ·,·  is the inner product that induces  · F, i.e., X,Y = Tr(XTY). Hence,

E ABlow,ABhigh | A = Tr(A2 · EBlowBThigh) = 0. Therefore,

E D(xS) AB 2F − E D(xS) ABlow 2F D ∞ · E AB F + ABlow F · AB F − ABlow F D ∞ · E AB F + ABlow F

2 1/2

2

· E AB F − ABlow F

2 D ∞ · E ABhigh 2F 1/2 · E AB 2F 1/2 . The ﬁrst step used the identity |x2 − y2| = |x + y| · |x − y|. In the second step, we applied Cauchy– Schwarz. The third step used the triangle inequality, AB F − ABlow F ABhigh F .

Since x  → A(S)BS,low(x) 2F is a sum of squares of polynomials of degree at most d/2 in the

variables S and D is a degree-d pseudo-density, the expectation ED(xS) ABlow 2F is non-negative. It follows that

E D(xS) AB 2F −2 D ∞ · E ABhigh 2F 1/2 · E AB 2F 1/2 . We also have

A(S)2 · E Bhigh 2F = τE Bhigh 2F . This bound implies the desired lower bound

E ABhigh 2F max

S

E D(xS) AB 2F −2√τ D ∞ · E Bhigh 2F 1/2 · E AB 2F .

![image 88](<2014-lee-lower-bounds-size-semidefinite_images/imageFile88.png>)

#### Lemma 3.7.

ℓd/2md/2 (n − m)d/2 · E

BS,high(x) 2F

B(x) 2F Proof. By construction the Fourier transform of BS,high satisﬁes

E

![image 89](<2014-lee-lower-bounds-size-semidefinite_images/imageFile89.png>)

S,x

S,x

Therefore,

The expectation satisﬁes

Bˆ(α)χα .

BS,high =

α⊆[n] |α∩S|>d/2

B ˆ(α) 2F .

BS,high(x) 2F =

E

x

α⊆[n] |α∩S|>d/2

B ˆ(α) 2F · P |α ∩ S| > d/2 .

BS,high(x) 2F =

E

E

x

S

α⊆[n]

Since B has degree at most ℓ, we can upper bound the probability of the event {|α ∩ S| > d/2},

ℓd/2md/2 (n − m)d/2

ℓ d/2

n m

n m − d/2

P |α ∩ S| > d/2

/

.

![image 90](<2014-lee-lower-bounds-size-semidefinite_images/imageFile90.png>)

Together with α B ˆα 2F = Ex B(x) 2F, the desired bound on the expected norm of BS,high follows: E

ℓd/2md/2 (n − m)d/2 · E

B(x) 2F .

BS,high(x) 2F

E

![image 91](<2014-lee-lower-bounds-size-semidefinite_images/imageFile91.png>)

x

x

S

We combine the previous two lemmas to lower bound the correlation between the pseudodensity D(xS) and the norms A(S)B(x) 2F,

1/2

1/2

D(xS) A(S)B(x) 2F −2√τ D ∞ E S,x

A(S)B(x) 2F

BS,high(x) 2F

![image 92](<2014-lee-lower-bounds-size-semidefinite_images/imageFile92.png>)

E

E

S,x

S,x

- (using Lemma 3.6)

−2√τ D ∞

![image 93](<2014-lee-lower-bounds-size-semidefinite_images/imageFile93.png>)

ℓd/4md/4 (n − m)d/4

![image 94](<2014-lee-lower-bounds-size-semidefinite_images/imageFile94.png>)

E

S,x

A(S)B(x) 2F

1/2

E

x

B(x) 2F

1/2

- (using Lemma 3.7).


- 3.3 Proof of the main theorem For a function f : {0,1}m → [0,1] and an integer n m, let Mnf : m n × {0,1}n → [0,1] be the matrix,


Mnf(S,x) def= f(xS).

- Theorem 3.8. For any m,d 1, the following holds. Let f : {0,1}m → [0,1] be a nonnegative function with d + 2 = degsos(f). Then for n 2m,


d 4

![image 95](<2014-lee-lower-bounds-size-semidefinite_images/imageFile95.png>)

n logn

1 + n1+d/2 rkpsd Mnf Cf

, (3.10)

![image 96](<2014-lee-lower-bounds-size-semidefinite_images/imageFile96.png>)

where Cf > 0 is a constant depending only on f.

Moreover, if there exists an ε ∈ (0,1], and a degree-d pseudo-density D : {0,1}m → R with Ex D(x)f(x) < −ε, then for every n 2m, we have

d/4 ε D ∞

3/2

cεn dm2 D ∞ logn

![image 97](<2014-lee-lower-bounds-size-semidefinite_images/imageFile97.png>)

rkpsd(Mnf)

f(x) , (3.11)

E

![image 98](<2014-lee-lower-bounds-size-semidefinite_images/imageFile98.png>)

![image 99](<2014-lee-lower-bounds-size-semidefinite_images/imageFile99.png>)

x

where c > 0 is a universal constant. Proof. Let d+2 = degsos(f) and consider a degree-d pseudo-density with EDf < −ε for some ε > 0. Recall the linear functional LD deﬁned in Section 3.1. One observes that LD(Mnf) < −ε.

By (the contrapositive of) Theorem 3.1, it follows that rkpsd(Mnf)2 α(n/logn)d/2 · Mnf 1, where α is a constant depending only on the parameters ε,m,d, and the pseudo-density D. Note that

Mnf 1 = E f. This immediately implies (3.10). Likewise, (3.11) follows directly from Theorem 3.1.

Let us now prove that rkpsd(Mnf) 1 + n1+d/2 by exhibiting an explicit factorization of Mnf. Let F def= {A ⊆ [n] : |A| 1 + d/2} and set r = |F |. For x ∈ {0,1}n, we use the notation xA := i∈A xi. Suppose f = tj=1 g2j for some {gj : {0,1}m → R} such that deg(gj) 1 + d/2 for j ∈ [t].

For each function j ∈ [t] and subset S ⊆ [n] with |S| = m, deﬁne the function gS,j : {0,1}n → R by gS,j(x) = gj(xS). We associate the coeﬃcient vector gˆS,j : F → R associated to gS,j by letting gˆS,j(A) be the coeﬃcient of the monomial i∈A xi in gS,j. Finally, for every |S| = m and x ∈ {0,1}m, we deﬁne r × r PSD matrices indexed by F as follows: (Qx)A,B := xAxB and (PS)A,B := tj=1 gˆS,j(A)gˆS,j(B). It is easy to check that

 

 

2

t

t

gS,j(x)2 = f(xS) = Mnf(S,x),

xAgˆS,j(A)

Tr(PSQx) =

=

A∈F

j=1

j=1

which yields an explicit psd factorization of Mnf with matrices {PS},{Qx} of dimension r =

n i 1 + n1+d/2.

i 1+d/2

## 4 Approximations for density operators

We turn now to a central theme of our approach: High-entropy states can be approximated by “simple” states if the approximation is only with respect to “simple” tests. In our setting, “simple” will mean low-degree. In Section 4.1, we present a basic version of this principle with respect to a single test functional. This suﬃces for essentially all our applications to psd rank lower bounds.

We believe that the maximum-entropy approximation framework is a powerful one, so Section 4.2 is devoted to a more general exploration of the principle. In particular, we state and prove approximation theorems for density operators with respect to families of tests. In the rest of this section, we ﬁx a ﬁnite-dimensional real inner product space H.

### 4.1 Approximation against a single test

The following theorem shows that a linear functional over density matrices with high entropy is approximately minimized at a density matrix that is the square of a low-degree polynomial in the linear functional. We recall that U = Tr(Id)Id is the uniform density matrix.

![image 100](<2014-lee-lower-bounds-size-semidefinite_images/imageFile100.png>)

- Theorem 4.1 (Density matrix approximation). Let F ∈ M(H) be a symmetric matrix and let Q ∈ D(H) be a density matrix. Then, for every ε ∈ (0, 21), there exists a degree-k univariate polynomial p with k O( F /ε) · S(Q U) + O loglog 1 log1/ε/ε such that


![image 101](<2014-lee-lower-bounds-size-semidefinite_images/imageFile101.png>)

![image 102](<2014-lee-lower-bounds-size-semidefinite_images/imageFile102.png>)

Tr F · Tr(p1(F)2)p(F)2 Tr(FQ) + ε. Moreover, the polynomial p depends only on ε, the operator norm F , and the relative entropy S(Q U).)

![image 103](<2014-lee-lower-bounds-size-semidefinite_images/imageFile103.png>)

The proof consists of two steps. First, we will show that the theorem holds with Tr(p1(F)2)p(F)2 replaced by e−λF/Tr(e−λF) for λ (1/ε)·S(Q U). Then, we will approximate the matrix exponential by the square of a low-degree polynomial.

![image 104](<2014-lee-lower-bounds-size-semidefinite_images/imageFile104.png>)

- Lemma 4.2. For every symmetric matrix F and every density matrix Q,


Tr F · Tre1−λFe−λF Tr(FQ) + ε, as long as λ 1/ε · S(Q U).

![image 105](<2014-lee-lower-bounds-size-semidefinite_images/imageFile105.png>)

Proof. By the duality formula for quantum entropy (see, e.g., [Car10, Thm. 2.13]), the function f : X  → λTr(FX)+S(X  U) over the the set of density matrices is minimized at X⋆ = e−λF/Tr(e−λF). Therefore, using the fact S(X⋆  U) 0, we get

λTr(FX⋆) f(X⋆) f(Q) = λTr(FQ) + S(Q U), which implies that Tr(FX⋆) Tr(FQ) + S(Q U)/λ Tr(FQ) + ε, as desired.

Next we observe that one can pass from univariate approximations of ex to approximations of eF in the trace norm.

- Lemma 4.3. Let δ ∈ (0,1] and τ > 0 be given. Suppose there exists a univariate polynomial p(x) such that for every x ∈ [−τ/2,τ/2],


ex − p(x) δex . (4.1) Then for every F ∈ M(H) with F τ, we have

p(F/2)2 Tr(p(F/2)2) ∗

eF Tr(eF) −

6δ. (4.2)

![image 106](<2014-lee-lower-bounds-size-semidefinite_images/imageFile106.png>)

![image 107](<2014-lee-lower-bounds-size-semidefinite_images/imageFile107.png>)

Proof. Under the assumptions, for every x ∈ [−τ,τ], one has

ex − p(x/2)2 = ex/2 − p(x/2) · ex/2 + p(x/2) ex/2(2 + δ) ex/2 − p(x/2) δex(2 + δ) 3δex , (4.3)

where the last line follows from δ 1. Note the elementary equality: For all x, y,x′, y′ > 0,

y − y′

- x′

![image 108](<2014-lee-lower-bounds-size-semidefinite_images/imageFile108.png>)

- y′ =


- x − x′

![image 109](<2014-lee-lower-bounds-size-semidefinite_images/imageFile109.png>)

- y


- x

![image 110](<2014-lee-lower-bounds-size-semidefinite_images/imageFile110.png>)

- y −


yy′ x′ . (4.4) Let λ1,λ2,...,λn ∈ [−τ,τ] denote the eigenvalues of F. We conclude that

+

![image 111](<2014-lee-lower-bounds-size-semidefinite_images/imageFile111.png>)

p(λi/2)2 ni=1 eλi − p(λi/2)2

n

n

eλi − p(λi/2)2

p(λi/2)2

eλi

(4.4)

−

+

![image 112](<2014-lee-lower-bounds-size-semidefinite_images/imageFile112.png>)

![image 113](<2014-lee-lower-bounds-size-semidefinite_images/imageFile113.png>)

![image 114](<2014-lee-lower-bounds-size-semidefinite_images/imageFile114.png>)

![image 115](<2014-lee-lower-bounds-size-semidefinite_images/imageFile115.png>)

n i=1 eλi

n i=1 p(λi/2)2

n i=1 eλi

n i=1 eλi n

i=1 p(λi/2)2 (4.3)

i=1

i=1

p(λi/2)2 3δ ni=1 eλi

n

3δ +

![image 116](<2014-lee-lower-bounds-size-semidefinite_images/imageFile116.png>)

n i=1 eλi n

i=1 p(λi/2)2 6δ.

i=1

Since eF and p(F) are simultaneously diagonalizable, the preceding inequality is precisely our goal (4.2).

The following corollary of Lemma 4.3 follows by checking that the Taylor expansion of ex satisﬁes the approximation guarantee (4.1). Corollary 4.4. For every ε ∈ (0, 21) and every symmetric matrix F ∈ M(H), there is a number k 3e F ∞ + log log(1log(1/ε/ε) ) and a univariate degree-k polynomial pk with non-negative coeﬃcients such that

![image 117](<2014-lee-lower-bounds-size-semidefinite_images/imageFile117.png>)

![image 118](<2014-lee-lower-bounds-size-semidefinite_images/imageFile118.png>)

pk(F/2)2 Tr(pk(F/2)2) ∗

eF Tr(eF) −

![image 119](<2014-lee-lower-bounds-size-semidefinite_images/imageFile119.png>)

![image 120](<2014-lee-lower-bounds-size-semidefinite_images/imageFile120.png>)

Proof. Let pk(x) = kt=0 xkk! . By Taylor’s theorem, we have

![image 121](<2014-lee-lower-bounds-size-semidefinite_images/imageFile121.png>)

ε. (4.5)

xk+1 (k + 1)!

ex − pk(x) ex

.

![image 122](<2014-lee-lower-bounds-size-semidefinite_images/imageFile122.png>)

Deﬁne τ = F ∞ and choose k = 3e τ + log log(1log(1/ε/ε) ) so that for x ∈ [−τ/2,τ/2], we have (kx+k+1)!1 ε/6. Finally, apply Lemma 4.3.

![image 123](<2014-lee-lower-bounds-size-semidefinite_images/imageFile123.png>)

![image 124](<2014-lee-lower-bounds-size-semidefinite_images/imageFile124.png>)

The proof of the main theorem in this section follows by combining Lemma 4.2 and Corollary 4.4.

- Proof of Theorem 4.1. Fix ε ∈ (0, 12) and F ∈ M(H), q ∈ D(H). Choose λ = (2/ε) · S(Q U) and


![image 125](<2014-lee-lower-bounds-size-semidefinite_images/imageFile125.png>)

′)

F′ = −λF. Letpk be thepolynomial fromCorollary 4.4 fork = 3e F′ + log(1/ε

log log(1/ε′) and ε′ = ε/(2 F ). Note that k O( F /ε) · S(Q U) + O log log 1 log 1/ε/ε . Moreover,

![image 126](<2014-lee-lower-bounds-size-semidefinite_images/imageFile126.png>)

![image 127](<2014-lee-lower-bounds-size-semidefinite_images/imageFile127.png>)

k(F′/2)2)pk(F′/2)2 Tr F · Tr(1eF′)eF′ + ε′ · F (by Corollary 4.4)

Tr F · Tr(p 1

![image 128](<2014-lee-lower-bounds-size-semidefinite_images/imageFile128.png>)

![image 129](<2014-lee-lower-bounds-size-semidefinite_images/imageFile129.png>)

Tr(FQ) + ε2 + ε′ · F (by Lemma 4.2) Since ε/2 + ε′ · F ε, the polynomial p(x) = pk(−λx/2) satisﬁes the desired bound

![image 130](<2014-lee-lower-bounds-size-semidefinite_images/imageFile130.png>)

Tr F · Tr(p1(F)2)p(F)2 Tr(FQ) + ε.

![image 131](<2014-lee-lower-bounds-size-semidefinite_images/imageFile131.png>)

### 4.2 Approximation against a family of tests

Let T ⊆ M(H) denote a compact set of matrices, and set ∆(T) := supA∈T A . For A ∈ M(H), we deﬁne the associated dual gauge

[A]T def= sup B∈T

Tr(BA).

One should think of T as a set of test functionals; for A,A′ ∈ M(H), the value [A − A′]T measures the extent to which A and A′ are distinguishable using tests from T. It is important to note that if T is not centrally symmetric, then [·]T might also fail to be symmetric. For future reference, we observe that fact that for any A ∈ M(H),

|[A]T | ∆(T) A ∗ (4.6) [A + A′]T [A]T + [A′]T . (4.7)

Our main approximation theorem asserts that, with respect to tests from a convex set T, a highentropy density operator can be well-approximated by the square of a low-degree polynomial in some element of T.

Theorem 4.5 (Approximation by a low-degree square). For every ε ∈ (0, 21), the following holds. Let T ⊆ M(H) be compact and convex, and let Q ∈ D(H) be a density matrix. Then there exists a number

![image 132](<2014-lee-lower-bounds-size-semidefinite_images/imageFile132.png>)

∆(T) ε

k (1 + S(Q U))

,

![image 133](<2014-lee-lower-bounds-size-semidefinite_images/imageFile133.png>)

a univariate degree-k polynomial p, and an element F ∈ T such that Tr(p(F)2) = 1 and

Q − p(F)2 T ε.

Just as for Theorem 4.1, this is proved in two steps: First we ﬁnd an initial approximator of a simple form, and then we construct from that a low-degree approximator. In the next argument, it is helpful to have the following fact: If X(t) is continuously diﬀerentiable matrix-valued function, then for any β ∈ R, we have the Duhamel formula:

β

dX(t) dt

- d dt

![image 134](<2014-lee-lower-bounds-size-semidefinite_images/imageFile134.png>)

- eβX(t) =


e(β−α)X(t) dα. (4.8)

eαX(t)

![image 135](<2014-lee-lower-bounds-size-semidefinite_images/imageFile135.png>)

0

This can be veriﬁed immediately by showing that both sides satisfy the diﬀerential equation

∂F ∂β

dX dt

= eβX

+ X(t)F(β,t)

![image 136](<2014-lee-lower-bounds-size-semidefinite_images/imageFile136.png>)

![image 137](<2014-lee-lower-bounds-size-semidefinite_images/imageFile137.png>)

with F(0,t) = 0 for all t. (This argument is taken from [Wil67].)

We will only require (4.8) for β = 1. For example, (4.8) and cyclicity of the trace yields

Tr

dX(t) dt

d dt

eX(t) = Tr eX(t)

![image 138](<2014-lee-lower-bounds-size-semidefinite_images/imageFile138.png>)

![image 139](<2014-lee-lower-bounds-size-semidefinite_images/imageFile139.png>)

. (4.9)

Denote X′(t) = dXdt(t). If we know that X(t) is symmetric, and its eigenvalues are {λi}, then by diagonalizing in the basis of X(t), we can also derive

![image 140](<2014-lee-lower-bounds-size-semidefinite_images/imageFile140.png>)

d dt

Tr X′(t)

eX(t) =

![image 141](<2014-lee-lower-bounds-size-semidefinite_images/imageFile141.png>)

=

=

1

Tr X′(t)eαX(t)X′(t)e(1−α)X(t) dα

0

1

(X′(t))2ij eλi

eα(λj−λi) dα

0

i,j

1

eλi − eλj λi − λj

(X′(t))2ij

using

![image 142](<2014-lee-lower-bounds-size-semidefinite_images/imageFile142.png>)

0

i,j

(X′(t))2ij emax(λi,λj) ,

i,j

ex − 1 x

eαx dα =

![image 143](<2014-lee-lower-bounds-size-semidefinite_images/imageFile143.png>)

where in the ﬁnal line we have used the fact that if a b, then

ea(1 − eb−a) a − b

ea − eb a − b

ea , since eb−a 1 + (b − a). Thus we have

=

![image 144](<2014-lee-lower-bounds-size-semidefinite_images/imageFile144.png>)

![image 145](<2014-lee-lower-bounds-size-semidefinite_images/imageFile145.png>)

d dt

(X′(t))2ij

Tr X′(t)

eλi

eX(t) 2

![image 146](<2014-lee-lower-bounds-size-semidefinite_images/imageFile146.png>)

i

j

(X′(t))2ij

2Tr(eX(t))max

i

j

= 2Tr(eX(t)) X′(t) 22→∞

2Tr(eX(t)) X′(t) 2 . (4.10) Together these imply

X′(t) Tr(eX(t))

Tr(X′(t)eX(t)) Tr(eX(t))2

eX(t) Tr(eX(t))

deX(t) dt −

deX(t) dt

d dt

Tr X′(t)

= Tr

Tr

![image 147](<2014-lee-lower-bounds-size-semidefinite_images/imageFile147.png>)

![image 148](<2014-lee-lower-bounds-size-semidefinite_images/imageFile148.png>)

![image 149](<2014-lee-lower-bounds-size-semidefinite_images/imageFile149.png>)

![image 150](<2014-lee-lower-bounds-size-semidefinite_images/imageFile150.png>)

![image 151](<2014-lee-lower-bounds-size-semidefinite_images/imageFile151.png>)

![image 152](<2014-lee-lower-bounds-size-semidefinite_images/imageFile152.png>)

Tr(X′(t)eX(t)) Tr(eX(t)) ·

Tr(eX(t)X′(t)) Tr(eX(t))

X′(t) Tr(eX(t))

deX(t) dt −

= Tr

![image 153](<2014-lee-lower-bounds-size-semidefinite_images/imageFile153.png>)

![image 154](<2014-lee-lower-bounds-size-semidefinite_images/imageFile154.png>)

![image 155](<2014-lee-lower-bounds-size-semidefinite_images/imageFile155.png>)

![image 156](<2014-lee-lower-bounds-size-semidefinite_images/imageFile156.png>)

2

Tr(X′(t)eX(t)) Tr(eX(t))

deX(t) dt −

1 Tr(eX(t))

Tr X′(t)

=

![image 157](<2014-lee-lower-bounds-size-semidefinite_images/imageFile157.png>)

![image 158](<2014-lee-lower-bounds-size-semidefinite_images/imageFile158.png>)

![image 159](<2014-lee-lower-bounds-size-semidefinite_images/imageFile159.png>)

(4.10)

2 X′(t) 2 . (4.11) We will use this for the following lemma.

Lemma 4.6 (Sparse approximation by mirror descent). For every ε > 0, the following holds. Let C ⊆ M(H) be a compact set, and let Q,Q0 ∈ D(H) be density matrices. If one deﬁnes h = ⌈ε82S(Q Q0)∆(T)2⌉ then there exist A1,A2,...,Ah ∈ T such that

![image 160](<2014-lee-lower-bounds-size-semidefinite_images/imageFile160.png>)

- h
- i=1 Ai


exp logQ0 − 4∆(εT)2 Tr exp logQ0 − 4∆(εT)2

![image 161](<2014-lee-lower-bounds-size-semidefinite_images/imageFile161.png>)

Q˜ def=

∈ D(H) (4.12)

![image 162](<2014-lee-lower-bounds-size-semidefinite_images/imageFile162.png>)

- h
- i=1 Ai


![image 163](<2014-lee-lower-bounds-size-semidefinite_images/imageFile163.png>)

satisﬁes

Q − Q˜ T ε. (4.13) Proof. Consider for t 0, the density matrix

exp logQ0 − 0 t Λs ds

,

Qt =

![image 164](<2014-lee-lower-bounds-size-semidefinite_images/imageFile164.png>)

Tr exp logQ0 − 0 t Λs ds

where s  → Λs ∈ T is any measurable function. First, one calculates

d dt

d dt

logQt = −Λt − Id

![image 165](<2014-lee-lower-bounds-size-semidefinite_images/imageFile165.png>)

![image 166](<2014-lee-lower-bounds-size-semidefinite_images/imageFile166.png>)

logTr exp logQ0 −

t

Λs ds (4.14)

0

Now, we have

d dt

logTr exp logQ0 −

![image 167](<2014-lee-lower-bounds-size-semidefinite_images/imageFile167.png>)

and thus

d dt Tr exp logQ0 − 0 t Λs ds

t

![image 168](<2014-lee-lower-bounds-size-semidefinite_images/imageFile168.png>)

(4.9=) −Tr(ΛtQt),

Λs ds =

![image 169](<2014-lee-lower-bounds-size-semidefinite_images/imageFile169.png>)

Tr exp logQ0 − 0 t Λs ds

0

d dt

d dt

S(Q Qt) = Tr Q

![image 170](<2014-lee-lower-bounds-size-semidefinite_images/imageFile170.png>)

![image 171](<2014-lee-lower-bounds-size-semidefinite_images/imageFile171.png>)

logQt = −Tr(ΛtQ) + Tr(Q)Tr(ΛtQt) = −Tr(Λt(Q − Qt)), (4.15)

where in the ﬁnal line we have used Tr(Q) = 1. Let T = ε2S(Q Q0). Suppose the map t  → Λt ∈ T is such that

![image 172](<2014-lee-lower-bounds-size-semidefinite_images/imageFile172.png>)

ε 2 ∀t ∈ [0,T]. (4.16)

Tr(Λt(Q − Qt)) >

![image 173](<2014-lee-lower-bounds-size-semidefinite_images/imageFile173.png>)

Then from (4.15) and (4.16), we arrive at

S(Q QT) < S(Q Q0) −

ε 2

T = 0,

![image 174](<2014-lee-lower-bounds-size-semidefinite_images/imageFile174.png>)

which contradicts the fact that S(Q QT) 0.

Finally, we deﬁne the elements A1,...,Ah ∈ T and corresponding approximators Q˜0,Q˜1,...,Q˜h ∈ D(H) inductively. Deﬁne, for i = 0,1,2,... ,h, the times ti = i4∆(εT)2. We will choose the map t  → Λt and put Q˜i = Qti.

![image 175](<2014-lee-lower-bounds-size-semidefinite_images/imageFile175.png>)

We begin by setting Q˜0 = U and Λ0 = 0. Now if Q − Q˜i T ε, then we are done. Otherwise, let Ai+1 ∈ T be such that

Tr(Ai+1Q − Ai+1Q˜i) > ε, (4.17) and deﬁne Λt = Ai+1 for t ∈ (ti,ti+1].

Finally, observe that for t ∈ (ti,ti+1), we have

(4.11)

d dt

d dt

−2 Λt 2 .

Tr(Ai+1Q − Ai+1Qt) =

Tr(ΛtQt)

![image 176](<2014-lee-lower-bounds-size-semidefinite_images/imageFile176.png>)

![image 177](<2014-lee-lower-bounds-size-semidefinite_images/imageFile177.png>)

t

where we have used the fact that Λt = −dtd log elogQ0−

0 Λs ds . We conclude that

![image 178](<2014-lee-lower-bounds-size-semidefinite_images/imageFile178.png>)

Tr(Ai+1Q − Ai+1Qti+1) Tr(Ai+1Q − Ai+1Qti) − 2 Λt 2(ti+1 − ti)

ε 2

Tr(Ai+1Q − Ai+1Qti) −

![image 179](<2014-lee-lower-bounds-size-semidefinite_images/imageFile179.png>)

ε 2

,

>

![image 180](<2014-lee-lower-bounds-size-semidefinite_images/imageFile180.png>)

using (4.17). Thus we either ﬁnd an approximator Q˜i for some i = 0,1,...,h satisfying (4.13) or (4.16) holds. But we have already seen that the latter possibility cannot happen. Observe that the approximators Q˜i are all of the desired form (4.12).

- Proof of Theorem 4.5. First, we apply Lemma 4.6 with Q0 = U to obtain an approximation Q˜ of the form


eλF Tr(eλF) with |λ| 1 + 1δS(Q U) and which satisﬁes

Q˜ =

![image 181](<2014-lee-lower-bounds-size-semidefinite_images/imageFile181.png>)

![image 182](<2014-lee-lower-bounds-size-semidefinite_images/imageFile182.png>)

Q − Q˜ T ε/2. (4.18) Note here that since T is assumed to be convex, we have F ∈ T (see the form of (4.12)). Then we apply Corollary 4.4 to λF to obtain a degree-k polynomial pk such that

pk(λF/2)2 Tr(pk(λF/2)2) ∗

ε 2∆(T)

Q ˜ −

, (4.19)

![image 183](<2014-lee-lower-bounds-size-semidefinite_images/imageFile183.png>)

![image 184](<2014-lee-lower-bounds-size-semidefinite_images/imageFile184.png>)

where

log(∆(T)/ε) loglog(∆(T)/ε)

∆(T) ε

k |λ|∆(T) +

(1 + S(Q U))

. Thus we conclude that

![image 185](<2014-lee-lower-bounds-size-semidefinite_images/imageFile185.png>)

![image 186](<2014-lee-lower-bounds-size-semidefinite_images/imageFile186.png>)

pk(λF/2)2 Tr(pk(λF/2)2) T

Q −

![image 187](<2014-lee-lower-bounds-size-semidefinite_images/imageFile187.png>)

pk(λF/2)2

(4.7)

Q − Q˜ T + Q ˜ −

![image 188](<2014-lee-lower-bounds-size-semidefinite_images/imageFile188.png>)

Tr(pk(λF/2)2) T (4.6)

pk(λF/2)2 Tr(pk(λF/2)2) − Q˜

Q − Q˜ T + ∆(T)

![image 189](<2014-lee-lower-bounds-size-semidefinite_images/imageFile189.png>)

∗ (4.18)∧(4.19)

ε.

#### 4.2.1 Junta approximation

We record here the following application to “classical” functions by restricting Lemma 4.6 to the diagonal case. If X is a ﬁnite set, and T is a collection of real-valued functions on X, we extend the notation ∆(T) = supg∈T g ∞. If µ is a measure on X, and f : X → R+ satisﬁes Eµ f = 1, we abuse notation by writing

D(f µ) = E

[f log f].

µ

for the relative entropy between fµ and µ. We will also allow ourselves to conﬂate µ with the corresponding density by writing µ(x) for µ({x}) and x ∈ X. One should note that an analog of Lemma 4.6 for the special case of probability distributions (instead of density matrices) can be proved exactly along the same lines, but without the use of matrix inequalities.

Corollary 4.7 (Sparse approximation of functions by mirror descent). For every ε > 0, the following holds. Let X be a ﬁnite set equipped with a probability measure µ. Let T ⊆ L2(X,µ) be a compact set of

functions, and let f : X → R+ be such that Eµ f = 1. If one deﬁnes h = ⌈ε82D(f µ)∆(T)2⌉ then there exist functions g1, g2,..., gh ∈ T such that

![image 190](<2014-lee-lower-bounds-size-semidefinite_images/imageFile190.png>)

exp 4∆( εT)2 hi=1 gi x∈X exp 4∆( εT)2 hi=1 gi(x) µ(x)

![image 191](<2014-lee-lower-bounds-size-semidefinite_images/imageFile191.png>)

f˜def=

(4.20)

![image 192](<2014-lee-lower-bounds-size-semidefinite_images/imageFile192.png>)

![image 193](<2014-lee-lower-bounds-size-semidefinite_images/imageFile193.png>)

so that Eµ f˜= 1, and for every g ∈ T,

g(x) f(x) − f˜(x) ε. (4.21)

E

x∼µ

Proof. H the Euclidean space R{0,1}n, and let {ex : x ∈ {0,1}n} be an orthornormal basis of H. We will represent f by the diagonal matrix M(f) ∈ D(H) deﬁned by

f(x)exeTxµ(x).

M(f) =

x∈{0,1}n

We also lift each test g to a matrix M(g) = x∈{0,1}n g(x)exeTx and the set M(T) now denotes a class of matrix tests.

Furthermore, we write

exeTxµ(x)

Q0 =

x∈{0,1}n

so that S(M(f) Q0) = D(f µ). Applying Lemma 4.6 yields an approximation Q˜ to M(f) of the form

Q˜ = Q0 · M,

where M is a diagonal matrix. Furthermore, by construction, the function f˜: {0,1}n → R given by f˜(x) = ex,Mex has the form (4.20). Finally, the approximation guarantee [M(f) − Q˜]M(T) ε is precisely (4.21).

We now apply the preceding corollary to prove an approximation-by-juntas theorem. An essentially equivalent result for Boolean domains is proved in [CLRS13], but it is instructive to see that it falls easily out of the learning framework. Fix n 1 and a ﬁnite set X. We recall that for a subset S ⊆ {1,... ,n}, a function f : Xn → R is called an S-junta if f only depends (at most) on the coordinates in S. In other words, for all x,x′ ∈ Xn, if x|S = x′|S then f(x) = f(x′). We say that f is a k-junta if it is an S-junta for a set with |S| = k.

- Theorem 4.8 (Junta approximation). Let X be an arbitrary ﬁnite set, and let µ denote a probability measure on Xn. Consider a non-negative function f : Xn → R+ with Eµ f = 1, and let T be a collection of k-juntas. Then for every ε > 0, there exists a non-negative k′-junta f˜: Xn → R+ with Eµ f˜= 1, where


k ε2

k′

D(f µ)∆(T)2 ,

![image 194](<2014-lee-lower-bounds-size-semidefinite_images/imageFile194.png>)

and such that for every g ∈ T,

g(x) f(x) − f˜(x) ε. (4.22)

E

x∼µ

Proof. Applying Corollary 4.7 yields an approximation f˜. One simply notes that from (4.20), f˜is an hk-junta where h ε 12D(f µ)∆(T)2

![image 195](<2014-lee-lower-bounds-size-semidefinite_images/imageFile195.png>)

## 5 The correlation polytope

Recall the correlation polytope corrn ⊆ Rn2 given by corrn = conv {xxT : x ∈ {0,1}n} . This polytope is also known as the Boolean quadric polytope [Pad89] for the following reason.

- Proposition 5.1 (Restatement of Proposition 1.11). If f : {0,1}m → R+ is a nonnegative quadratic function over {0,1}m, then for any n m, Mnf is a submatrix of some slack matrix associated to corrn. Proof. Let A,B = Tr(ATB) denote the Frobenius inner product on Rn2. Suppose that f(x) =

i j aijxixj + a0 0 for all x ∈ {0,1}n. We claim that this gives a valid linear inequality for corrn as follows: For all x ∈ {0,1}n,

f(x) = A,xxT + a0 0,

where A is the matrix A = (aij). Since this inequality holds at the vertices, it holds for all of corrn.

We now recall the relationship between the correlation, cut, TSP, and stable set polytopes. The ﬁrst fact is from [DS90], while the second two are taken from [FMP+12].

- Proposition 5.2. For every n 1, the following hold:


- 1. corrn is linearly isomorphic to cutn+1.
- 2. There exists a number an O(n2) such that some face of tspan linearly projects to corrn.
- 3. There exists a graph Hn on bn O(n2) vertices such that some face of stabbn(Hn) linearly projects to corrn.


### 5.1 Positive semideﬁnite rank

We will now prove a lower bound on the psd rank of corrn. Our ﬁrst goal is to construct a suitable family of pseudo-densities. We will employ Grigoriev’s work [Gri01a] on degree lower bounds for Positivstellensatz calculus refutations. The primary diﬃculty will be in expressing Grigoriev’s lower bound using a pseudo-density of small norm.

- Theorem 5.3. Fix an odd integer m 3. There exists a degree-m pseudo-density D : {0,1}m → R such that


 

 

2

m

m 2

xi −

= 0,

D(x)

E

![image 196](<2014-lee-lower-bounds-size-semidefinite_images/imageFile196.png>)

x

i=1

and

D ∞ m3/2 . Proof. Grigoriev constructsa linear functional G onthe space of m-variate real polynomials modulo the ideal I generated by {Xi2 − Xi : i = 1 ∈ [m]}:

G : R[X1,...,Xm]/I → R . His functional satisﬁes

G p(X)2 0 ∀p ∈ R[X1,...,Xm]/I, deg(p) m/2, (5.1)

and



 

 

m

Xi − m2

G



![image 197](<2014-lee-lower-bounds-size-semidefinite_images/imageFile197.png>)

i=1

The functional is uniquely deﬁned by the values

2 

= 0. (5.2)

m/2 |S| m |S|

G(XS) def=

,

![image 198](<2014-lee-lower-bounds-size-semidefinite_images/imageFile198.png>)

for each multilinear monomial XS = i∈S Xi with S ⊆ [m]. Observe that m/2 is not an integer and the (generalized) binomial coeﬃcient mk/2 is deﬁned using the formal expression

r · (r − 1)···(r − k + 1) k · (k − 1)···1

r k

.

=

![image 199](<2014-lee-lower-bounds-size-semidefinite_images/imageFile199.png>)

It is easy to check that G satisﬁes (5.2):

2 



 

 

m

m

m

m2 4

G(Xi2) + 2

Xi − m2

G(XiXj) − m

G(Xi) +

G

=



![image 200](<2014-lee-lower-bounds-size-semidefinite_images/imageFile200.png>)

![image 201](<2014-lee-lower-bounds-size-semidefinite_images/imageFile201.png>)

i=1

i j

i=1

i=1

m2 4

m − 2 4(m − 1) − m

m 2

m 2

+ m(m − 1)

= 0.

=

+

![image 202](<2014-lee-lower-bounds-size-semidefinite_images/imageFile202.png>)

![image 203](<2014-lee-lower-bounds-size-semidefinite_images/imageFile203.png>)

![image 204](<2014-lee-lower-bounds-size-semidefinite_images/imageFile204.png>)

![image 205](<2014-lee-lower-bounds-size-semidefinite_images/imageFile205.png>)

Grigoriev shows that G satisﬁes (5.1) [Gri01a, Lem. 1.4].

We will construct a pseudo-density D : {0,1}m → R such that Ex D(x)p(x) = G(p(X1,...,Xm)) for every multilinear polynomial p. Observe that G is invariant under permutation of variables {X1,...,Xm}. For w = 0,1,...,m, let cw denote the unique degree m polynomial such that,

  

1 if t = w 0 if t ∈ {0,1,...,m} \ {w}

cw(t) =

We claim that for any univariate real polynomial p with deg(p) m,

m

p(w) · cw(t) = p(t). (5.3)

w=0

Both sides of the claimed identity are univariate polynomials in t of degree at most m and agree with each other on the m + 1 points given by t ∈ {0,1,... ,m}. Hence, the two polynomials are identically equal.

For each x ∈ {0,1}m, let |x| denote its hamming weight, and deﬁne

c|x| (m/2) m |x|

D(x) def= 2m ·

.

![image 206](<2014-lee-lower-bounds-size-semidefinite_images/imageFile206.png>)

We claim that D satisﬁes Ex D(x)p(x) = G p(X) for every polynomial multilinear real polynomial p. To see this, consider any monomial xS = i∈S xi with S ⊆ [m]. Put ℓ = |S|. Then we have:





1

D(x)xS = E x

xT

D(x) ·

(symmetry of D)

E





![image 207](<2014-lee-lower-bounds-size-semidefinite_images/imageFile207.png>)

m ℓ

x

T⊆[m],|T|=ℓ

|x| ℓ

1

D(x) ·

= E

![image 208](<2014-lee-lower-bounds-size-semidefinite_images/imageFile208.png>)

m ℓ

x

m w

m

1

D(x) ·

=

E

![image 209](<2014-lee-lower-bounds-size-semidefinite_images/imageFile209.png>)

![image 210](<2014-lee-lower-bounds-size-semidefinite_images/imageFile210.png>)

m ℓ

2m

x

w=0

w ℓ m ℓ

m

cw(m/2)

=

![image 211](<2014-lee-lower-bounds-size-semidefinite_images/imageFile211.png>)

w=0

m/2 ℓ m ℓ

=

![image 212](<2014-lee-lower-bounds-size-semidefinite_images/imageFile212.png>)

|x| ℓ |x| = w

= G XS (using (5.3) with p(t) =

t ℓ

).

Finally, in order to bound D ∞, observe that the polynomials cw(t) are given by the interpolation formula

m a=0,a w(t − a) m a=0,a w(w − a)

. For an x ∈ {0,1}m with |x| = w we have,

cw(t) =

![image 213](<2014-lee-lower-bounds-size-semidefinite_images/imageFile213.png>)

m a=0,a w(m − 2a)

cw(m/2) m w

1

|D(x)| = 2m ·

m a=0,a w(w − a) ·

=

![image 214](<2014-lee-lower-bounds-size-semidefinite_images/imageFile214.png>)

![image 215](<2014-lee-lower-bounds-size-semidefinite_images/imageFile215.png>)

![image 216](<2014-lee-lower-bounds-size-semidefinite_images/imageFile216.png>)

m w

m a=0,a w(m − 2a)

1

(w − 1)!(m − w)! ·

=

![image 217](<2014-lee-lower-bounds-size-semidefinite_images/imageFile217.png>)

![image 218](<2014-lee-lower-bounds-size-semidefinite_images/imageFile218.png>)

m w

- 1

![image 219](<2014-lee-lower-bounds-size-semidefinite_images/imageFile219.png>)

- 2m−1 ·

m − 1 (m−1)/2

·

w |m − 2w| m

![image 220](<2014-lee-lower-bounds-size-semidefinite_images/imageFile220.png>)

![image 221](<2014-lee-lower-bounds-size-semidefinite_images/imageFile221.png>)

![image 222](<2014-lee-lower-bounds-size-semidefinite_images/imageFile222.png>)

- 3 2(m − 1) + 1


= m ·

m + 1 2

![image 223](<2014-lee-lower-bounds-size-semidefinite_images/imageFile223.png>)

![image 224](<2014-lee-lower-bounds-size-semidefinite_images/imageFile224.png>)

m3/2 , where in the last step we have used Sterling’s approximation for the inequality (m m−−1)1/2 2m−1/ 32(m − 1) + 1, valid for m 3.

![image 225](<2014-lee-lower-bounds-size-semidefinite_images/imageFile225.png>)

![image 226](<2014-lee-lower-bounds-size-semidefinite_images/imageFile226.png>)

- Theorem 5.4. There is a constant α > 0 such that for every n 1, rkpsd(corrn) 2αn2/13 .


Proof. For m 1, deﬁne f : {0,1}m → R+ by





 

 

2

m

m 2

1 m2

1 4

−

xi −

, (5.4)

f(x) =





![image 227](<2014-lee-lower-bounds-size-semidefinite_images/imageFile227.png>)

![image 228](<2014-lee-lower-bounds-size-semidefinite_images/imageFile228.png>)

![image 229](<2014-lee-lower-bounds-size-semidefinite_images/imageFile229.png>)

i=1

and let Mnf : m n × {0,1}n → R+ be given by Mnf(S,x) = f(xS) as in (1.3).

By Theorem 5.3, there exists a degree-m pseudo-densityD : {0,1}m → R such that Ex D(x)f(x) = −4m12 and D ∞ m3/2. Fix ε = 1/(4m2) and d = m and apply Theorem 3.8 to conclude that there is

![image 230](<2014-lee-lower-bounds-size-semidefinite_images/imageFile230.png>)

- a constant α′ > 0 such that for n 2m, we have


m/4

α′n m13/2 logn

rkpsd(Mnf)

· m−21/4 · m−1/2

![image 231](<2014-lee-lower-bounds-size-semidefinite_images/imageFile231.png>)

Choosing n α 2′m13/2 logn, an easy calculation shows that rkpsd(Mnf) 2Ω(n2/13) . By Proposition 5.1, we have rkpsd(corrn) rkpsd(Mnf), completing the proof.

![image 232](<2014-lee-lower-bounds-size-semidefinite_images/imageFile232.png>)

## 6 Optimality of low-degree sum-of-squares for max CSPs

Constraint satisfaction problems form a broad class of discrete optimization problems that include, for example, max cut and max 3-sat. For simplicity of presentation, we will focus on constraint satisfaction problems with a boolean alphabet, though similar ideas extend to larger domains (see an analogous generalization in Section 7). We begin our presentation with a formal deﬁnition of semideﬁnite programming relaxations for max-CSPs.

### 6.1 The SDP approximation model

In order to write an SDP relaxation for a max-CSP, one needs to linearize the objective function. For n ∈ N, let max-Πn be the set of max-Π instances on n variables. An SDP-relaxation of size r for max-Πn consists of the following.

Linearization: Let r be a natural number. For every ℑ ∈ max-Πn, we associate a vector ℑ˜ ∈ Rr×r and for every assignment x ∈ {0,1}n, we associate a point x˜ ∈ Rr×r, such that ℑ(x) = ℑ ˜ ,x˜ for all ℑ ∈ max-Πn and all x ∈ {0,1}n.

Feasible region: The feasible region is a closed, convex (possibly unbounded) spectrahedron S ⊆ Rr×r described as the intersection of the cone of r × r PSD matrices with an aﬃne linear subspace:

S = {y ∈ Rr×r|Ay = b, y ∈ S+r }, such that x˜ ∈ S for all assignments x ∈ {0,1}n. Note that the spectrahedron S is independent of the instance ℑ of max-Πn.

Given an instance ℑ ∈ max-Πn, the SDP relaxation S has value S(ℑ) def= max

ℑ ˜ , y .

y∈S

Since x˜ ∈ S for all assignments x ∈ {0,1}n and ℑ ˜ ,x˜ = ℑ(x), we have S(ℑ) opt(ℑ) for all instances ℑ ∈ max-Πn.

Low-degree sum-of-squares relaxations. We will now describe the low-degree sum-of-squares relaxation as it applies to a max-CSP. Let Π be a max-CSP with arity k. Given an instance ℑ of max-Πn, we recall that we think of it as a function ℑ : {0,1}n → R given by ℑ(x) = m1 mi=1 Pi(x) where {Pi}i∈[m] are the constraints in ℑ. Deﬁne the cone Csosd ⊆ R{0,1}n as the cone generated by squares of polynomials of degree at most d/2, i.e.,

![image 233](<2014-lee-lower-bounds-size-semidefinite_images/imageFile233.png>)

Csosd = Cone {g2 | g : {0,1}n → R,deg(g) d/2} . The degree-d sos relaxation for ℑ is given by

sosd(ℑ) def= min c | c − ℑ ∈ Csosd (6.1)

![image 234](<2014-lee-lower-bounds-size-semidefinite_images/imageFile234.png>)

We willnowwritethedualformulationoftheabovesemideﬁniteprogramtoexpose theunderlying spectrahedron and linearization. The dual of (6.1) can be written as,

sosd(ℑ) = max

D,ℑ  (6.2) subject to D,1 = 1,

![image 235](<2014-lee-lower-bounds-size-semidefinite_images/imageFile235.png>)

D:{0,1}n→R

D,h 0 ∀h ∈ Csosd . The function D : {0,1}n → R is referred to as a pseudo-density over {0,1}n, since it satisﬁes that for every degree d/2 function g, Ex D(x)g2(x) 0.

Notice that all the constraints on the pseudodensity D : {0,1}n → R correspond to inner products with functions of degree at most d. Hence, without loss of generality, we may assume deg(D) d. Alternately, the convex program (6.2) can be written succinctly in terms of the lowdegree part of D. We will now carry this out explicitly and thereby identify the feasible region associated with the degree-d sos relaxation.

To this end, set F := {A : A ⊆ [n],|A| d/2} and let r = |F | di=/02 ni . Recall that S+r ⊆ Rr×r is the cone of r ×r PSD matrices. We will index the matrices in S+r using elements of F in the natural way. Deﬁne a matrix Y : F × F → R as follows,

Y(A,B) = D,

xi .

i∈A∪B

By deﬁnition of Y, it is clear that Y(A,B) = Y(B,A) = Y(A ∪ B,∅) for all A,B ∈ F . Moreover, we have Y(∅,∅) = D,1 = 1. Furthermore, the matrix Y is PSD since, for all gˆ : F → R, we have

gˆAgˆBY(A,B)

g ˆ,Ygˆ =

A,B∈F

= D,

gˆAgˆB

xi

i∈A∪B

A,B∈F

 

 

2

using x2i = xi ∀i ∈ [n],x ∈ {0,1}n 0

= D,

gˆA

xi

i∈A

A∈F

where the ﬁnal inequality used the fact that D, g2 0 for all functions g with deg(g) d/2.

From the above discussion, it is clear that the feasible region of the degree d-sos relaxation (6.2) corresponds to the spectrahedron,

S def= {Y ∈ Rr×r | Y ∈ S+r ,Y(∅,∅) = 1 and YA,B = YB,A = YA∪B,∅ ∀A,B ∈ F }

Now we describe the linearization associated with the degree-d sos relaxation. For every assignment x ∈ {0,1}n, associate the matrix x˜ : F × F → R given by

x˜(A,B) def=

xi. (6.3)

i∈A∪B

By deﬁnition, we have x˜(A,B) = x˜(B,A) = x˜(A ∪ B,∅) and x(∅,∅) = 1. Moreover, the matrix x˜ is positive semideﬁnite since it can be written as x˜ = XXT wherein X : F → R is given by X(A) = i∈A xi. Therefore, for each assignment x, we have x˜ ∈ S.

Finally, given an instance ℑ ∈ max-Πn its linearization ℑ˜ is written as follows. Fix d 2⌈k/2⌉, and for every subset S ⊆ [d] with |S| k, deﬁne a disjoint union S = AS ∪ BS where AS contains (up to) the ⌈k/2⌉ smallest elements of S, and BS contains the rest (or is empty).

Each constraint P0 in ℑ is of the form P0(X) = P(Xi1,...,Xik) for a predicate P : {0,1}n → {0,1}

in Π. Therefore the function ℑ : {0,1}n → R given by ℑ(x) = m1 mi=1 Pi(x) can be expressed as a degree-k multilinear polynomial in x,i.e.,

![image 236](<2014-lee-lower-bounds-size-semidefinite_images/imageFile236.png>)

ℑˆ A

ℑ(x) =

xi .

i∈A

A⊆[n],|A| k

The linearization ℑ˜ : F × F → R is given by,

  

ℑˆ S if A = AS,B = BS 0 otherwise

ℑ˜ (A,B) def=

(6.4)

From (6.3) and (6.4), for every instance ℑ ∈ max-Πn and every assignment x ∈ {0,1}n we have ℑ ˜ ,x˜ =

ℑˆ A

xi = ℑ(x).

i∈A

A,|A| d/2

Now the degree-d sos relaxation corresponding to an instance ℑ ∈ max-Πn in (6.1) and (6.2) can be equivalently formulated as

sosd(ℑ) def= max

ℑ ˜ , y .

![image 237](<2014-lee-lower-bounds-size-semidefinite_images/imageFile237.png>)

y∈S

(c,s)-approximations. For 0 s c 1, a sequence of SDP relaxations {Sn}∞n=1 for max-Π is said to achieve a (c,s)-approximation to max-Π if for each n ∈ N and every instance ℑ of max-Πn with opt(ℑ) s, we have Sn(ℑ) c. In order to study (c,s)-approximations for max-Π, we recall (from Proposition 1.13) the set of matrices {Mcn,,sΠ}∞n=1 associated with it, deﬁned as:

Mcn,,sΠ(ℑ,x) = c − ℑ(x),

where the ﬁrst index of Mcn,,sΠ ranges over all instances on n variables satisfying opt(ℑ) s. A simple consequence of Proposition 1.10 is the following.

Proposition 6.1. There exists a sequence of SDP relaxations Sn of size rn achieving a (c,s)-approximation to max-Πn if and only if rkpsd(Mcn,,sΠ) rn.

### 6.2 General SDPs vs. sum-of-squares

Our main theorem is that general SDP relaxations for max-CSPs are no more powerful than lowdegree sum-of-squares relaxations in the polynomial-size regime.

- Theorem 6.2. Fix a positive number d ∈ N, and a k-ary CSP max-Π with d 2⌈k/2⌉. Suppose that the degree-d sos relaxation cannot achieve a (c,s)-approximation for max-Π. Then no sequence of SDP relaxations of size at most o log nn d/4 can achieve a (c,s)-approximation for max-Π.


![image 238](<2014-lee-lower-bounds-size-semidefinite_images/imageFile238.png>)

Proof. Given that the degree-d sos relaxation cannot achieve a (c,s)-approximation, there exists an instance ℑ of max-Πm for some m such that opt(ℑ) s but degsos(c − ℑ) > d.

By Proposition 6.1, it is suﬃcient to lower bound the psd rank of the matrix Mcn,,sΠ. Fix f = c−ℑ and deﬁne the matrix Mnf : m n × {0,1}n → [0,1] as Mnf(S,x) def= f(xS). Since Mnf is a submatrix of Mcn,,sΠ, we have rkpsd(Mcn,,sΠ) rkpsd(Mnf). By Theorem 1.8, for some constant C 1, we have

rkpsd(Mnf)

n Clogn

![image 239](<2014-lee-lower-bounds-size-semidefinite_images/imageFile239.png>)

d/4

.

This implies that no sequence of SDP relaxations of size at most o((lognn)d/4) can achieve a (c,s)approximation for max-Π.

![image 240](<2014-lee-lower-bounds-size-semidefinite_images/imageFile240.png>)

For a stronger quantitative bound, we require the following simple fact.

Fact 6.3. For every positive even integer d, every degree-d pseudo-density D : {0,1}m → R and every subset α ⊆ [m],|α| d, we have

D(x)χα(x)| 1. Proof. Write χα = χAχB for some A,B with |A|,|B| d/2 and observe that E

|E

x

(χA − χB)2 2

D(x) 1 −

D(x) · 1 = 1,

D(x)χα(x) = E x

E

![image 241](<2014-lee-lower-bounds-size-semidefinite_images/imageFile241.png>)

x

x

where we used the fact that Ex D(x)p(x)2 0 whenever deg(p) d/2. Using χα = 21(χA + χB)2 − 1, we get the other direction of the inequality.

![image 242](<2014-lee-lower-bounds-size-semidefinite_images/imageFile242.png>)

- Theorem 6.4. Fix a k-ary CSP max-Π and a monotone increasing function d : N → N such that the


following three conditions are true: d(1) 2⌈k/2⌉, and d(n) n for all n 1, and and limn→∞ d(n) = ∞. Fix ε > 0 and 0 < s < c 1. There is a constant K > 0 such that the following holds.

Suppose that for every n 1, the degree-d(n) sos relaxation cannot achieve a (c+ε,s)-approximation for max-Πn. Then for all n 1, no SDP relaxation of size at most Knd(n)2/8 can achieve a (c,s)-approximation for max-ΠN for every N > n4d(n).

Proof. Without loss of generality, we may assume that d(n) 24 is always an even integer. Given that the degree-d(n) sos relaxation cannot achieve a (c+ε,s)-approximation for max-Πn, there exists an instance ℑ of max-Πn such that opt(ℑ) s, along with a degree-d(n) pseudo-density D(x) such that Ex D(x)(c − ℑ(x)) < −ε. The pseudo-density D(x) can be written as

[D(x)χα(x)] · χα(x),

D(x) =

E

x

α⊆[n],|α| d(n)

where for each α, |Ex[D(x)χα(x)]| 1 by Fact 6.3. Hence,

d(n)

n i

1 + nd(n) .

D ∞

i=0

Fix f = c − ℑ and deﬁne the matrix MNf : Nn × {0,1}n → [0,1] as MNf (S,x) def= f(xS). By Theorem 3.8 (3.11), whenever N > n4d(n), we have we have rkpsd(Mnf) nd(n)2/8. As MNc,s,Π contains MNf as a submatrix, the same lower bound applies to MNc,s,Π. This implies that no SDP relaxation of size at most nd(n)2/4 can achieve a (c,s)-approximation for max-ΠN when N > n4d(n).

Using known lower bounds for low degree sum-of-squares relaxations for max-CSPs [Gri01b, Sch08, Tul09], Theorem 6.4 implies lower bounds against general SDP relaxations for a range of speciﬁc max-CSPs. For instance, the lower bounds of Grigoriev [Gri01b] and Schoenebeck [Sch08] imply a lower bound for max 3-sat (see Theorem 1.5).

- Theorem 6.5 ([Gri01b, Sch08]). For every ε > 0, there exists a constant cε such that the following holds. For every n 1, there is a max-Πn instance ℑn such that opt(ℑn) 7/8 + ε, but soscεn(ℑ) = 1.


![image 243](<2014-lee-lower-bounds-size-semidefinite_images/imageFile243.png>)

Observe that one can obtain the bound of Theorem 1.5 using the preceding result as follows. In

- Theorem 6.4, choose n ≍ logN and d(n) ≍ logloglogNN so that n4d(n) ≍ N. In that case, the lower bound obtained is of the order Nd(n)/32 ≍ NΩ(logN/log logN).


![image 244](<2014-lee-lower-bounds-size-semidefinite_images/imageFile244.png>)

## 7 Nonnegative rank

Theorem 3.8 exhibits a connection between psd rank and sos degree. There is a similar connection between nonnegative rank and junta-degree. The results of Section 7.1 generalize those of [CLRS13], while the method of proof is closely related. As opposed to [CLRS13], we use the learning approach of Section 4 to approximate by juntas. In Section 7.2, we demonstrate an application to the correlation polytope.

### 7.1 Nonnegative rank vs. junta degree

We recall that the nonnegative rank of a matrix M ∈ Rp+×q is the smallest integer r 1 such that there exist v1,...,vp,u1,...,uq ∈ Rr+ satisfying Mij = ui,vj for all i ∈ [p], j ∈ [q]. We denote the minimal value r by rk+(M).

Junta degree and pseudo-densities. Fix a ﬁnite set X. For a nonnegative function f : Xn → R+, we say that f has a nonnegative junta certiﬁcate of degree d if there exist nonnegative d-juntas

g1, g2,..., gk : Xn → R+ such that f = ki=1 gi (as functions on the discrete cube). The junta degree of f, denoted degJ(f), is the minimal d such that f has a nonnegative junta certiﬁcate of degree d.

Consider an arbitrary measure µ on Xn. A function D : Xn → R is called a d-local pseudo-density (with respect to the measure µ) if Eµ D = 1 and furthermore Ex∼µ D(x)g(x) 0 for all nonnegative d-juntas g. If a measure µ is unspeciﬁed, we always refer to the uniform measure by default. The

following characterization is immediate from thefact that thesetof functionssatisfying degJ(f) d is a closed convex cone.

Lemma 7.1. For every f : Xn → R+ and d 0, we have degJ(f) > d if and only if there exists a d-local pseudo-density such that Ex D(x)f(x) < 0.

We also deﬁnea more quantitative notion: Approximate junta degree with respectto an arbitrary measure. Given ε > 0 and a measure µ on Xn, we deﬁne

degεJ(f;µ) def= 1 + max d : ∃ a d-local pseudo-density D wrt µ and E

x∼µ

D(x)f(x) < −ε D ∞ E µ

f ,

where we take the maximum to be equal to −1 if no such pseudo-density exists. (See Section 7.2 for an example where a biased measure µ is used to analyze the nonnegative rank of the lopsided disjointness matrix.) We can now state our main theorem on nonnegative rank.

For any measure µ on X, we use µn to denote the corresponding product measure on Xn. In the following theorem, we write f 1 := Eµm f.

- Theorem 7.2. For any ﬁnite set X, any measure µ on X, and any ε > 0, the following holds. For any f : Xm → R+ and all n 2m,


d

cε2n m2(dlog n + log( f ∞/ f 1))

1 + nd+1 rk+(Mnf)

, (7.1)

![image 245](<2014-lee-lower-bounds-size-semidefinite_images/imageFile245.png>)

where d + 1 = degεJ(f;µm) and c > 0 is a universal constant. Proof. The left-hand-side inequality of (7.1) follows from the fact that the cone of nonnegative d-juntas is spanned by di=+01 ni 1 + nd+1 nonnegative d-juntas. We move on to right-hand inequality.

We will use  ·,·  for the inner product on L2(Xn;µn), i.e. g,h = Eµn[gh]. Consider a rank-r nonnegative factorization

r

Mnf(S,x) =

λi(S)qi(x). (7.2)

i=1

By rescaling, we may assume that Eµn qi = 1 for each i ∈ [r]. Observe that, by taking expectation on both sides with respect to µn, for any ﬁxed S we have

r

λi(S) = E

x∼µn

i=1

Mnf(S,x) = E µm

f = f 1 . (7.3)

Let Λτ = {i : qi ∞ τ}. Note that for i Λτ, we must have

f ∞ τ ∀|S| = m. (7.4)

λi(S)

![image 246](<2014-lee-lower-bounds-size-semidefinite_images/imageFile246.png>)

Let D : Xm → R be a d-local pseudo-density witnessing degεJ(f;µm) > d. For S ⊆ [n] with |S| = m, we deﬁne a function DS : Xn → R by DS(x) = D(xS). Note that each DS is clearly an m-junta.

For some δ > 0 to be chosen later, for each qi with i ∈ Λτ, we apply Theorem 4.8 to obtain a

density q˜i that is a k′-junta for k′ = O( D 2∞δm2 logτ), and such that for every S ⊆ [n] with |S| = m, we have

![image 247](<2014-lee-lower-bounds-size-semidefinite_images/imageFile247.png>)

DS,qi DS,q˜i − δ. (7.5) Let Ji denote the set of coordinates on which qi depends, so that |Ji| k′.

We now take the inner product of both sides of (7.2) with the function E|S|=m DS. On the left-hand side, using our assumption on the pseudo-density D,

DS(x)Mnf(S,x) < −ε D ∞ f 1 . (7.6) We break the right-hand side of (7.2) into two parts. First, using (7.4),

E

E

x∼µn

S

f ∞ τ

DS(x)λi(S)qi(x) −

E

E

![image 248](<2014-lee-lower-bounds-size-semidefinite_images/imageFile248.png>)

x∼µn

S

i Λτ

D ∞r. (7.7)

For the second part, we use (7.5) so that for every i ∈ Λτ and |S| = m, E

DS(x)qi(x) −δ + E

DS(x)q˜i(x)

x∼µn

x∼µn

= −δ + E

[q˜i(x) | xS = y]

DS(y) E

x∼µn

y∈XS y∼µm

−δ − D ∞1{|S∩Ji|>d} ,

where in the ﬁnal line we have used the facts that the function y  → Ex∼µn[q˜i(x) | xS = y] is a nonnegative (S ∩ Ji)-junta, and that DS : Xm → R is a d-local pseudo-density.

This implies that for i ∈ Λτ, E

DS(x)qi(x) −δE S

λi(S) − D ∞ λi ∞ P(|S ∩ Ji| > d)

λi(S) E

x∼µn

S

|Ji| d

n m−d/2

−δE

λi(S) − D ∞ λi ∞

![image 249](<2014-lee-lower-bounds-size-semidefinite_images/imageFile249.png>)

n m

S

λi(S) − D ∞ λi ∞ |Ji|dmd

−δE

![image 250](<2014-lee-lower-bounds-size-semidefinite_images/imageFile250.png>)

(n − m)d −δE

S

(k′)d(2m)d nd

λi(S) − D ∞ f 1

,

![image 251](<2014-lee-lower-bounds-size-semidefinite_images/imageFile251.png>)

S

where in the ﬁnal line we have used λi ∞ f 1 from (7.3) and also |Ji| k′ and n 2m. Combining this with (7.7) and (7.6), we conclude that

r

−ε D ∞ f 1 >

λi(S) E

DS(x)qi(x)

E

x∼µn

S

i=1

(k′)d(2m)d nd − δ

f ∞ τ

D ∞r − |Λτ| · D ∞ f 1

−

λi(S)

E

![image 252](<2014-lee-lower-bounds-size-semidefinite_images/imageFile252.png>)

![image 253](<2014-lee-lower-bounds-size-semidefinite_images/imageFile253.png>)

S

i∈Λτ

(k′)d(2m)d nd − δ f 1 .

f ∞ τ

−r D ∞

+ f 1

![image 254](<2014-lee-lower-bounds-size-semidefinite_images/imageFile254.png>)

![image 255](<2014-lee-lower-bounds-size-semidefinite_images/imageFile255.png>)

Let us now set τ = 3r f f ∞

and δ = ε D ∞/3, yielding

![image 256](<2014-lee-lower-bounds-size-semidefinite_images/imageFile256.png>)

1

r

1 3

![image 257](<2014-lee-lower-bounds-size-semidefinite_images/imageFile257.png>)

n 2k′m

![image 258](<2014-lee-lower-bounds-size-semidefinite_images/imageFile258.png>)

d

ε2n m2 logτ

c

![image 259](<2014-lee-lower-bounds-size-semidefinite_images/imageFile259.png>)

d

for some universal constant c > 0. Now, if r nd, then we are done. Otherwise, (7.8) yields

(7.8)

completing the proof.

r

cε2n m2(dlog n + log( f ∞/ f 1))

![image 260](<2014-lee-lower-bounds-size-semidefinite_images/imageFile260.png>)

d

,

- 7.2 The correlation polytope and lopsided disjointness We now illustrate a particularly simple application of our method to nonnegative rank.


Lemma 7.3. There is a constant ε0 > 0 such that for all m 3, the following holds. Deﬁne f : {0,1}m → R+ by

 1 −

 

2

m

, (7.9)

f(x) =

xi

i=1

and let µ be the measure on {0,1} satisfying µ(0) = 1 − 2/m and µ(1) = 2/m. Then,

m 2

degεJ0(f;µm)

+ 1.

![image 261](<2014-lee-lower-bounds-size-semidefinite_images/imageFile261.png>)

Plugging this result into Theorem 7.2 yields the following.

Theorem 7.4. There is a constant c > 0 such that for every m 3 and n 2m, we have

rk+(Mnf)

cn m3 logn

![image 262](<2014-lee-lower-bounds-size-semidefinite_images/imageFile262.png>)

m/2

.

In particular, by setting m = m(n) appropriately, Proposition 5.1 implies that rk+(corrn) 2Ω(n1/3). One should note that this is somewhat weaker than the lower bound rk+(corrn) 2Ω(n) proved in [FMP+12].

Proof of Lemma 7.3. For x ∈ {0,1}m, let |x| denote the hamming weight of x. Deﬁne the pseudodensity D : {0,1}m → R with respect to µm by

  

−µm1(0) |x| = 0

![image 263](<2014-lee-lower-bounds-size-semidefinite_images/imageFile263.png>)

D(x) def=

2

mµm(x) |x| = 1 0 |x| > 1

![image 264](<2014-lee-lower-bounds-size-semidefinite_images/imageFile264.png>)

We now verify that D is a d-local pseudo-density (with respect to µm) for d = m2 + 1. Observe ﬁrst that

![image 265](<2014-lee-lower-bounds-size-semidefinite_images/imageFile265.png>)

2 m

D(x) = −1 + m ·

= 1.

E

![image 266](<2014-lee-lower-bounds-size-semidefinite_images/imageFile266.png>)

x∼µm

Let β = m2 1 − m2 m−1 denote µm(1,0,...,0). Consider a subset S ⊆ [m] and some ﬁxed string

![image 267](<2014-lee-lower-bounds-size-semidefinite_images/imageFile267.png>)

![image 268](<2014-lee-lower-bounds-size-semidefinite_images/imageFile268.png>)

- b ∈ {0,1}S. Let 1b : {0,1}m → {0,1} denote the indicator of whether xS = b. If b = 0, then


m−1

m

1 − 2|S| − 1

2 m

2 m

= 1 −

D(x)1b(x) = β(m − |S|) − 1 −

E

![image 269](<2014-lee-lower-bounds-size-semidefinite_images/imageFile269.png>)

![image 270](<2014-lee-lower-bounds-size-semidefinite_images/imageFile270.png>)

![image 271](<2014-lee-lower-bounds-size-semidefinite_images/imageFile271.png>)

m The latter quantity is nonnegative as long as |S| m2 + 1.

x∼µm

![image 272](<2014-lee-lower-bounds-size-semidefinite_images/imageFile272.png>)

If |b| > 1, then Ex∼µm D(x)1b(x) = 0, and if |b| = 1, then Ex∼µm D(x)1b(x) 0 since D(x) 0 on the support of 1b. But any nonnegative S-junta is a nonnegative combination of the functions 1b as b ranges over {0,1}S. We conclude that as long as d m2 + 1, D is a d-local pseudo-density.

![image 273](<2014-lee-lower-bounds-size-semidefinite_images/imageFile273.png>)

Moreover we have





m

m

x2i + 2

1 − 2

= −1.

D(x)f(x) = E

D(x)

xi +

xixj

E





x∼µm

x∼µm

i=1

i=1

i j

Also observe that since m 3,

−m

2 m

D ∞ = |D(0)| = 1 −

27.

![image 274](<2014-lee-lower-bounds-size-semidefinite_images/imageFile274.png>)

Lastly, it is easy to see that Eµm f Ω(1). These facts together imply that for some universal constant ε0 > 0, we have degεJ0(f;µm) m/2 + 1, as desired.

An interesting feature of the pseudodensity D is that it is supported only on x ∈ {0,1}m with |x| 1. Therefore, the lower bound on the approximate junta degree established in Lemma 7.3 applies to any function f : {0,1}m → R+ that satisﬁes

  

1 for |x| = 0 0 for |x| = 1.

f(x) =

Moreover, the lower bound on rk+(Mnf) also applies in this general setting. To restate this generalization of Theorem 7.4, let us interpret an element of {0,1}n as a subset of {1,2,...,n}.

Corollary 7.5 (Lopsided unique disjointness). There is a ﬁxed constant c > 0 such that for every m 3 and n 2m, given a matrix M : [mn] × 2[n] → R+ satisfying

  

1 if |S ∩ T| = 1 0 if |S ∩ T| = 0,

M(S,T) =

m/2

we have rk+(M) m3 cnlogn

.

![image 275](<2014-lee-lower-bounds-size-semidefinite_images/imageFile275.png>)

In other words, the lower bound of Theorem 7.4 applies to all matrices that have a subset of entries corresponding to the unique disjointness problem.

### 7.3 Unique games hardness for LPs

As an illustrative application of the relation between nonnegative rank and junta-degree (Theorem 7.2), we present an LP hardness result for the Unique Games problem.11

Fix an integer q 1. An instance ℑ of unique games UGq consists of variables X1,...,Xn taking values in [q] and a collection of predicates P1,...,PM over these variables. Each constraint Pi is over a pair of distinct variables {Xai,Xbi} and is speciﬁed by a bijection πi : [q] → [q] as follows:

Pi(Xai,Xbi) def= 1[πi(Xai) = πi(Xbi)]. The goal is to ﬁnd an assignment that maximizes, over x ∈ [q]n, the number of satisﬁed constraints:

M

1 M

ℑ(x) def=

Pi(x)

![image 276](<2014-lee-lower-bounds-size-semidefinite_images/imageFile276.png>)

i=1

Recall that opt(ℑ) = maxx∈[q]n ℑ(x). Let UGqn denote the family of Unique Games instances on n variables. The authors of [CMM09] exhibit a strong integrality gap for Sherali-Adams linear programming relaxations of UGq

Theorem 7.6 ([CMM09]). Fix a number t 1 and let q = 2t. Then for every δ > 0, there exist γ,ε > 0, an m 1, and an instance ℑ ∈ UGqm such that

1 q

opt(ℑ)

+ δ,

![image 277](<2014-lee-lower-bounds-size-semidefinite_images/imageFile277.png>)

but degεJ(1 − δ − ℑ) mγ.

In fact, the authors of [CMM09] construct a lower bound for the d-round Sherali-Adams LP relaxation (where d ≍ mγ). But there is an equivalence between such lower bounds and the existence of a d-local pseudo-density; we refer to [CLRS13] for a discussion. Applying Theorem 7.2 (with X = [q] and µ as the uniform measure on [q]), we obtain the following corollary.

q

Let Mn,UG

c,s denote the matrix with entries Mn,UG

q

c,s (ℑ,x) = c − ℑ(x), where ℑ runs over all UGqn instances with opt(ℑ) s, and all values x ∈ [q]n.

![image 278](<2014-lee-lower-bounds-size-semidefinite_images/imageFile278.png>)

11We thank Ola Svensson for the suggestion to make this explicit.

Corollary 7.7. For every t 1, δ > 0, and d 1, there exists a constant c > 0 such that for all n 1,

q

rk+ Mn,UG

1−δ,1/q+δ cnd , where q = 2t.

In the language of [CLRS13] (see also Section 6 for related deﬁnitions in the SDP setting), this

shows that polynomial-size families of LP relaxations cannot achieve a (1−δ, 1q +δ)-approximation for the Unique Games problem.

![image 279](<2014-lee-lower-bounds-size-semidefinite_images/imageFile279.png>)

### Acknowledgments

This work was supported, in large part, by NSF grant CCF-1407779. A signiﬁcant fraction of the project was completed during a long-term visit of the authors to the Simons Institute for the Theory of Computing (Berkeley) for the program on Algorithmic Spectral Graph Theory. The authors would also like to thank Paul Beame, Siu-On Chan, Daniel Dadush, Troy Lee, Sebastian Pokutta, Pablo Parrilo, Mohit Singh, Ola Svensson, Thomas Rothvoß, and Rekha Thomas for valuable discussions and comments.

## References

[AK07] SanjeevAroraand SatyenKale. Acombinatorial, primal-dual approachtosemideﬁnite programs. In David S. Johnson and Uriel Feige, editors, STOC, pages 227–236. ACM,

2007. 15 [ARV09] Sanjeev Arora, Satish Rao, and Umesh Vazirani. Expander ﬂows, geometric embeddings and graph partitioning. J. ACM, 56(2):Art. 5, 37, 2009. 3 [Aus10] Per Austrin. Towards sharp inapproximability for any 2-CSP. SIAM J. Comput., 39(6):2430–2463, 2010. 3

[BBH+12] Boaz Barak, Fernando G. S. L. Brandão, Aram Wettroth Harrow, Jonathan A. Kelner, David Steurer, and Yuan Zhou. Hypercontractivity, sum-of-squares proofs, and their applications. In STOC, pages 307–326, 2012. 13

[BDP13] Jop Briët, Daniel Dadush, and Sebastian Pokutta. On the existence of 0/1 polytopes with high semideﬁnite extension complexity. In Algorithms - ESA 2013 - 21st Annual European Symposium, Sophia Antipolis, France, September 2-4, 2013. Proceedings, pages 217–228, 2013. 3, 5, 14

[BFPS12] Gábor Braun, Samuel Fiorini, Sebastian Pokutta, and David Steurer. Approximation limits of linear programs (beyond hierarchies). In FOCS, pages 480–489, 2012. 4

[BKS14] Boaz Barak, Jonathan A. Kelner, and David Steurer. Rounding sum-of-squares relaxations. In Symposium on Theory of Computing, STOC 2014, New York, NY, USA, May 31 June 03, 2014, pages 31–40, 2014. 13

[BS14] Boaz Barak and David Steurer. Sum-of-squares proofs and the quest toward optimal algorithms. CoRR, abs/1404.5236, 2014. 9

[BT03] Amir Beck and Marc Teboulle. Mirror descent and nonlinear projected subgradient methods for convex optimization. Oper. Res. Lett., 31(3):167–175, 2003. 15

[Bub14] S. Bubeck. Theory of convex optimization for machine learning. arXiv:1405.4980, 2014. 15

[Car10] Eric Carlen. Trace inequalities and quantum entropy: an introductory course. In Entropy and the quantum, volume 529 of Contemp. Math., pages 73–140. Amer. Math. Soc., Providence, RI, 2010. 24

[CGH+05] Julia Chuzhoy, Sudipto Guha, Eran Halperin, Sanjeev Khanna, Guy Kortsarz, Robert Krauthgamer, and Joseph Naor. Asymmetric k-center is log∗ n-hard to approximate. J. ACM, 52(4):538–551, 2005. 3

[CLRS13] Siu On Chan, James R. Lee, Prasad Raghavendra, and David Steurer. Approximate constraint satisfaction requires large LP relaxations. In 54th Annual IEEE Symposium on Foundations of Computer Science, FOCS 2013, 26-29 October, 2013, Berkeley, CA, USA, pages 350–359, 2013. 3, 9, 13, 30, 38, 42, 43

[CMM09] M. Charikar, K. Makarychev, and Y. Makarychev. Integrality gaps for Sherali-Adams relaxations. In Proc. STOC, pages 283–292. ACM, 2009. 42

[DS90] Caterina De Simone. The cut polytope and the Boolean quadric polytope. Discrete Math., 79(1):71–75, 1989/90. 5, 31

[FGP+14] Hamza Fawzi, João Gouveia, Pablo A. Parrilo, Richard Z. Robinson, and Rekha R. Thomas. Positive semideﬁnite rank. Arxiv, arXiv:1407.4095, 2014. 4, 14

[FMP+12] Samuel Fiorini, Serge Massar, Sebastian Pokutta, Hans Raj Tiwary, and Ronald deWolf. Linear vs. semideﬁnite extended formulations: exponential separation and strong lower bounds. In STOC, pages 95–106, 2012. 3, 4, 5, 8, 9, 10, 31, 41

[FSP13] H. Fawzi, J. Saunderson, and P. A. Parrilo. Equivariant semideﬁnite lifts and sum-ofsquares hierarchies. arXiv:1312.6662, 2013. 3

[GPT11] J. Gouveia, P. A. Parrilo, and R. Thomas. Lifts of convex sets and cone factorizations. arXiv:1111.3164, 2011. 3, 8, 10

- [Gri01a] Dima Grigoriev. Complexity of positivstellensatz proofs for the knapsack. Computational Complexity, 10(2):139–154, 2001. 10, 31, 32
- [Gri01b] Dima Grigoriev. Linear lower bound on degrees of Positivstellensatz calculus proofs for the parity. Theoret. Comput. Sci., 259(1-2):613–622, 2001. 8, 38


- [GV02] Dima Grigoriev and Nicolai Vorobjov. Complexity of Null- and Positivstellensatz proofs. Ann. Pure Appl. Logic, 113(1-3):153–160, 2002. First St. Petersburg Conference on Days of Logic and Computability (1999). 9
- [GW95] Michel X. Goemans and David P. Williamson. Improved approximation algorithms for maximum cut and satisﬁability problems using semideﬁnite programming. J. Assoc. Comput. Mach., 42(6):1115–1145, 1995. 3


[HK03] Eran Halperin and Robert Krauthgamer. Polylogarithmic inapproximability. In Proceedings of the Thirty-Fifth Annual ACM Symposium on Theory of Computing, pages 585– 594 (electronic). ACM, New York, 2003. 3

[Kho02] Subhash Khot. On the power of unique 2-prover 1-round games. In STOC, pages 767–775, 2002. 3

[KKMO04] Subhash Khot, Guy Kindler, Elchanan Mossel, and Ryan O’Donnell. Optimal inapproximability results for max-cut and other 2-variable csps? In FOCS, pages 146–154,

2004. 3 [KMS98] David Karger, Rajeev Motwani, and Madhu Sudan. Approximate graph coloring by semideﬁnite programming. J. ACM, 45(2):246–265, 1998. 3 [Las01] Jean B. Lasserre. Global optimization with polynomials and the problem of moments. SIAM J. Optim., 11(3):796–817, 2000/01. 3, 6

[Lau09] Monique Laurent. Sums of squares, moment matrices and optimization over polynomials. In Emerging applications of algebraic geometry, volume 149 of IMA Vol. Math. Appl., pages 157–270. Springer, New York, 2009. 9

[LRST14] James R. Lee, Prasad Raghavendra, David Steurer, and Ning Tan. On the power of symmetricLPand SDPrelaxations. InIEEE 29thConferenceonComputationalComplexity, CCC 2014, Vancouver, BC, Canada, June 11-13, 2014, pages 13–21, 2014. 3

[LY93] Carsten Lund and Mihalis Yannakakis. On the hardness of approximating minimization problems. In STOC, pages 286–293, 1993. 3

[NY83] A. S. Nemirovsky and D. B. Yudin. Problem complexity and method eﬃciency in optimization. A Wiley-Interscience Publication. John Wiley & Sons, Inc., New York, 1983. Translated from the Russian and with a preface by E. R. Dawson, Wiley-Interscience Series in Discrete Mathematics. 15

[O’D14] Ryan O’Donnell. Analysis of Boolean Functions. Cambridge University Press, 2014. 9, 12

[OZ12] Ryan O’Donnell and Yuan Zhou. Approximability and proof complexity. CoRR, abs/1211.1958, 2012. 9

[Pad89] Manfred Padberg. The Boolean quadric polytope: some characteristics, facets and relatives. Math. Programming, 45(1, (Ser. B)):139–172, 1989. 31

[Par00] Pablo Parrilo. Structured Semideﬁnite Programs and Semialgebraic Geometry Methods in Robustness and Optimization. PhD thesis, California Institute of Technology, 2000. 3, 6

[Rag08] Prasad Raghavendra. Optimal algorithms and inapproximability results for every CSP? [extended abstract]. In STOC’08, pages 245–254. ACM, New York, 2008. 3

- [Rot13] Thomas Rothvoß. Some 0/1 polytopes need exponential size extended formulations. Math. Program., 142(1-2, Ser. A):255–268, 2013. 3


- [Rot14] Thomas Rothvoß. The matching polytope has exponential extension complexity. In Symposium on Theory of Computing, STOC 2014, New York, NY, USA, May 31 - June 03, 2014, pages 263–272, 2014. 3


[Sch08] G. Schoenebeck. Linear level Lasserre lower bounds for certain k-CSPs. In Proc. FOCS, pages 593–602. IEEE, 2008. 8, 38

[She11] Alexander A. Sherstov. The pattern matrix method. SIAM J. Comput., 40(6):1969–2000,

2011. 9 [Sho87] N. Z. Shor. An approach to obtaining global extremums in polynomial mathematical programming problems. Cybernetics, 23(5):695–700, 1987. 3, 6

[TRW05] Koji Tsuda, Gunnar Rätsch, and Manfred K. Warmuth. Matrix exponentiated gradient updates for on-line learning and Bregman projection. J. Mach. Learn. Res., 6:995–1018,

2005. 15

[Tul09] Madhur Tulsiani. CSP gaps and reductions in the lasserre hierarchy. In Proceedings of the 41st Annual ACM Symposium on Theory of Computing, STOC 2009, Bethesda, MD, USA, May 31 - June 2, 2009, pages 303–312, 2009. 38

[Vaz01] Vijay V. Vazirani. Approximation algorithms. Springer-Verlag, Berlin, 2001. 3 [Wil67] R.M.Wilcox. Exponentialoperatorsand parameterdiﬀerentiationin quantumphysics.

J. Mathematical Phys., 8:962–982, 1967. 26 [Wil13] Mark M. Wilde. Quantum information theory. Cambridge University Press, Cambridge,

2013. 12 [WK12] Manfred K. Warmuth and Dima Kuzmin. Online variance minimization. Mach. Learn., 87(1):1–32, 2012. 15 [WS11] D. P. Williamson and D. B. Shmoys. The design of approximation algorithms. Cambridge University Press, Cambridge, 2011. 3 [Yan91] Mihalis Yannakakis. Expressing combinatorial optimization problems by linear programs. J. Comput. System Sci., 43(3):441–466, 1991. 3, 8

