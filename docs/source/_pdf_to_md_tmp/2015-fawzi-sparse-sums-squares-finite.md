# arXiv:1503.01207v1[math.OC]4Mar2015

## Sparse sum-of-squares certiﬁcates on ﬁnite abelian groups

Hamza Fawzi James Saunderson Pablo A. Parrilo March 3, 2015

Abstract

Let G be a ﬁnite abelian group. This paper is concerned with nonnegative functions on G that are sparse with respect to the Fourier basis. We establish combinatorial conditions on subsets S and T of Fourier basis elements under which nonnegative functions with Fourier support S are sums of squares of functions with Fourier support T . Our combinatorial condition involves constructing a chordal cover of a graph related to G and S (the Cayley graph Cay( G, S)) with maximal cliques related to T . Our result relies on two main ingredients: the decomposition of sparse positive semideﬁnite matrices with a chordal sparsity pattern, as well as a simple but key observation exploiting the structure of the Fourier basis elements of G (the characters of G).

We apply our general result to two examples. First, in the case where G = Zn2, by constructing a particular chordal cover of the half-cube graph, we prove that any nonnegative quadratic form in n binary variables is a sum of squares of functions of degree at most n/2 , establishing a conjecture of Laurent. Second, we consider nonnegative functions of degree d on ZN (when d divides N). By constructing a particular chordal cover of the dth power of the N-cycle, we prove that any such function is a sum of squares of functions with at most 3d log(N/d) nonzero Fourier coeﬃcients. Dually this shows that a certain cyclic polytope in R2d with N vertices can be expressed as a projection of a section of the cone of positive semideﬁnite matrices of size 3d log(N/d). Putting N = d2 gives a family of polytopes in R2d with linear programming extension complexity Ω(d2) and semideﬁnite programming extension complexity O(d log(d)). To the best of our knowledge, this is the ﬁrst explicit family of polytopes (Pd) in increasing dimensions where xcPSD(Pd) = o(xcLP(Pd)) (where xcPSD and xcLP are respectively the SDP and LP extension complexity).

The authors are with the Laboratory for Information and Decision Systems, Department of Electrical Engineering and Computer Science, Massachusetts Institute of Technology, Cambridge, MA 02139. Email: {hfawzi,jamess,parrilo}@mit.edu.

### Contents

- 1 Introduction 2
- 2 Preliminaries 6

- 2.1 Fourier analysis on ﬁnite groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 2.2 Chordal graphs and matrix completion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
- 2.3 Lifts of polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


- 3 Main result for general ﬁnite abelian groups 9

- 3.1 Nonnegative functions and sum-of-squares certiﬁcates . . . . . . . . . . . . . . . . . . . . . . 10
- 3.2 Dual point of view: moment matrices and matrix completion . . . . . . . . . . . . . . . . . . 13

- 3.2.1 Moment polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
- 3.2.2 Moment polytopes and matrix completion . . . . . . . . . . . . . . . . . . . . . . . . . 15


- 3.3 Real sums-of-squares and moment polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16


- 4 Application 1: The case G = Zn2 and binary quadratic optimization 18

- 4.1 Quadratic forms on {−1,1}n and the cut polytope . . . . . . . . . . . . . . . . . . . . . . . . 18
- 4.2 The associated Cayley graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
- 4.3 Applying Theorem 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20


- 5 Application 2: The case G = ZN and cyclic polytopes 21

- 5.1 The case S = {−1,0,1}: the cycle graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
- 5.2 Degree d functions: powers of cycle graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21


- 5.2.1 Triangulating the Cayley graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
- 5.2.2 Cyclic polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24


- 6 Conclusion 26 A Additional proofs 26


- A.1 Proofs from Section 3.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
- A.2 Proof of Lemma 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
- A.3 Proof of Proposition 6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
- A.4 Proof of Theorem 9: triangulation of the cycle graph . . . . . . . . . . . . . . . . . . . . . . . 29


### 1 Introduction

Let G be a ﬁnite abelian group. It is well-known that any function f : G → C admits a Fourier decomposition where the Fourier basis consists of the characters of G. Such a decomposition takes the form

f(χ)χ(x) ∀x ∈ G

f(x) =

χ∈ G

where G is the set of characters of G (known as the dual group of G) and f(χ) are the Fourier coeﬃcients of f. The function f : G → C is called sparse if only a few of its Fourier coeﬃcients are nonzero. More precisely we say that f is supported on S ⊆ G if f(χ) = 0 whenever χ ∈/ S.

This paper is concerned with functions f : G → C that are sparse and nonnegative, i.e., f(x) ∈ R+ for all x ∈ G. If f is a nonnegative function on G, a sum-of-squares certiﬁcate for the nonnegativity of f has the form:

J

|fj(x)|2 ∀x ∈ G (1)

f(x) =

j=1

where fj : G → C. Sum-of-squares certiﬁcates of nonnegative functions play an important role in optimization and particularly in semideﬁnite programming [BPT13]. When the function f is sparse, it is natural

to ask whether f admits a sum-of-squares certiﬁcate that is also sparse, i.e., where all the functions fj are supported on a common “small” set T ⊆ G. This is the main question of interest in this paper:

Given S ⊆ G, ﬁnd a subset T ⊆ G such that any nonnegative function G → R+ supported on S admits a sum-of-squares certiﬁcate supported on T .

(Q)

Our main result is to give a suﬃcient condition for a set T to satisfy the requirement above for a given S. The condition is expressed in terms of chordal covers of the Cayley graph Cay( G,S). Recall that the Cayley graph Cay( G,S) is the graph where nodes correspond to elements of G and where χ,χ are connected by an edge if χ−1χ ∈ S. Our main result can be stated as follows:

Theorem 1. Let S ⊆ G. Let T be a subset of G obtained as follows: Let Γ be a chordal cover of Cay( G,S), and for each maximal clique C of Γ, let χC be an element of G; deﬁne

T (Γ,{χC}) =

χCC (2)

C

where the union is over all the maximal cliques of Γ and where χCC := {χCχ : χ ∈ C} is the translation of C by χC. Then any nonnegative function supported on S admits a sum-of-squares certiﬁcate supported on T (Γ,{χC}).

Theorem 1 gives a way to construct a set T that satisﬁes the condition in (Q) for a given S ⊆ G. Such a construction proceeds in two steps: ﬁrst choose a chordal cover Γ of the graph Cay( G,S), and then choose elements χC ∈ G for each maximal clique C of G. Diﬀerent choices of Γ and {χC} will in general lead to diﬀerent sets T (Γ,{χC}). When using Theorem 1, one wants to ﬁnd a good choice of Γ and {χC} such that the resulting set T (Γ,{χC}) is as small as possible (or has other desirable properties).

One of the main strengths of Theorem 1 is in the ability to choose the elements {χC}. In fact the conclusion of Theorem 1 is almost trivial if χC = 1 G for all C, since in this case it simply says that any nonnegative function has a sum-of-squares certiﬁcate supported on G, which is easy to see since G is ﬁnite. As we will see in the applications, it is the ability to translate the cliques C of Γ via the choice of χC that is key in Theorem 1 and allows us to obtain interesting results. Equation (2) gives us the intuition behind a good choice of {χC}: in order to minimize the cardinality of T (Γ,{χC}) one would like to ﬁnd the translations χC that maximize the total overlap of the cliques (i.e., minimize the cardinality of their union).

Before describing the main idea behind Theorem 1 and its proof, we illustrate how one can use Theorem

- 1 in two important special cases, namely G = Zn2 (the boolean hypercube) and G = ZN.


- • Boolean hypercube: Consider the case G = {−1,1}n ∼= Zn2. The Fourier expansion of functions on {−1,1}n take the form


f(x) =

f(S)

xi. (3)

i∈S

S⊆[n]

A function f is said to have degree d if f(S) = 0 for all S such that |S| > d. Many combinatorial optimization problems correspond to optimizing a certain function f over {−1,1}n. For example the maximum cut problem in graph theory consists in optimizing a quadratic function over {−1,1}n. In [Lau03] Laurent conjectured that any nonnegative quadratic function on the hypercube is a sum of squares of functions of degree at most n/2 . Using our notations, this corresponds to asking whether for S = {S ⊆ [n] : |S| = 0 or 2} one can ﬁnd T ⊆ {S ⊆ [n] : |S| ≤ n/2 } such that the conclusion of Theorem 1 holds. By studying chordal covers of the Cayley graph Cay( G,S) we are able to answer this question positively:

Theorem 2. Any nonnegative quadratic function on {−1,1}n is a sum-of-squares of polynomials of degree at most n/2 .

Note that Blekherman et al. [BGP14] previously showed a weaker version of the conjecture that allows for multipliers: They showed that for any nonnegative quadratic function f on the hypercube, there exists h sum-of-squares such that h(x)f(x) is a sum-of-squares of polynomials of degree at most n/2 .

- • Trigonometric polynomials: Another important application that we consider in this paper is the case where G = ZN, the (additive) group of integers modulo N. The Fourier decomposition of a function f : ZN → C is the usual discrete Fourier transform and takes the form:


f(k)e2iπkx/N (4)

f(x) =

k∈ZN

where f(k) are the Fourier coeﬃcients of f. A function f is said to have degree d if suppf ⊆ {−d,−(d − 1),...,d − 1,d}. Nonnegative trigonometric polynomials play an important role in many areas such as in signal processing [Dum07], but also in convex geometry [Zie95, Bar02], in their relation to (trigonometric) cyclic polytopes. We are interested in nonnegative functions on G of degree at most d, i.e., functions supported on S = {−d,−(d−1),...,d−1,d}. By studying chordal covers of Cay( G,S) (which is nothing but the d’th power of the cycle graph) and using Theorem 1 we are able to show the following:

Theorem 3. Let N and d be two integers and assume that d divides N. Then there exists T ⊆ ZN with |T | ≤ 3dlog(N/d) such that any nonnegative function on ZN of degree at most d has a sum-of-squares certiﬁcate supported on T .

Remark. Note that if one is interested in functions of degree at most d on ZN and d does not divide N, then one can still apply Theorem 3 with d instead of d, where d is the smallest divisor of N that is greater than d.

Dual point of view and moment polytopes Theorem 1 can be interpreted from the dual point of view as giving a semideﬁnite programming description of certain moment polytopes. If S ⊆ G, deﬁne the moment polytope M(G,S) to be the set of S-moments of probability distributions on G, i.e.,

M(G,S) = Ex∼µ χ(x) χ∈S ∈ CS : µ a probability measure supported on G . Note that M(G,S) is a polytope since it can be equivalently expressed as:

M(G,S) = conv (χ(x))χ∈S ∈ CS : x ∈ G .

Note that from a geometric point of view, nonnegative functions f : G → R+ supported on S correspond to valid linear inequalities for the polytope M(G,S). By giving a sum-of-squares characterization for all valid inequalities of M(G,S) Theorem 1 allows us to obtain a semideﬁnite programming description of M(G,S). The following statement can be obtained from Theorem 1 by duality (we call this result “Theorem 1D” to reﬂect that it is a dual version of “Theorem 1”–we adopt this numbering convention throughout the paper):

Theorem 1D. Let S ⊆ G and let T = T (Γ,{χC}) be as deﬁned in Theorem 1. Then we have the following semideﬁnite programming description of the moment polytope M(G,S):

M(G,S) = ( χ)χ∈S : ∃(yχ)χ∈T −1T such that yχ = χ for all χ ∈ S , and y1

(5)

= 1, and yχχ χ,χ ∈T 0 .

G

In terms of positive semideﬁnite lifts, Equation (5) shows that M(G,S) has a Hermitian positive semidefinite lift of size |T |. We now illustrate this dual point of view for the two applications mentioned above, G = {−1,1}n and G = ZN:

- • For the case of the boolean hypercube G = {−1,1}n, if S = {S ⊆ [n] : |S| = 0 or 2}, the moment polytope M({−1,1}n,S \ {∅}) is nothing but the cut polytope for the complete graph on n vertices which we denote by CUTn:


CUTn = conv (xixj)i<j ∈ R(n

) : x ∈ {−1,1}n .

2

From the dual point of view, Theorem 2 shows that the n/2 level of the Lasserre hierarchy for the cut polytope is exact. This bound is tight since Laurent showed in [Lau03] that at least n/2 levels are needed.

Theorem 2D. The n/2 level of the Lasserre hierarchy for the cut polytope CUTn (as considered in [Lau03]) is exact.

- • Consider now the case G = ZN and S = {−d,−(d − 1),...,d − 1,d}. Here the moment polytope M(G,S) is the trigonometric cyclic polytope of degree d which we denote by TC(N,2d):


TC(N,2d) = conv M(2πx/N) : x = 0,1,...,N − 1 ⊂ R2d, (6) where M(θ) is the degree d trigonometric moment curve:

M(θ) = cos(θ),sin(θ),cos(2θ),sin(2θ),...,cos(dθ),sin(dθ) .

When interpreted from the dual point of view, Theorem 3 shows that TC(N,2d) has a Hermitian positive semideﬁnite lift of size at most 3dlog(N/d).

Theorem 3D. Let N and d be two integers and assume that d divides N. The trigonometric cyclic polytope TC(N,2d) deﬁned in (6) has a Hermitian positive semideﬁnite lift of size at most 3dlog(N/d).

Note that in the case d = 1 the polytope TC(N,2d) is nothing but the regular N-gon in the plane. Theorem 3D thus recovers, and extends to the case where N is not a power of two, a result from [FSP14] giving a semideﬁnite lift of the regular N-gon of size O(log N).

For d > 1 our result is, as far as we are aware, the ﬁrst nontrivial semideﬁnite programming lift of a cyclic polytope. Furthermore, in the regime where N = d2 our lift is provably smaller than any linear programming lift: Indeed, since TC(d2,2d) is d-neighborly [Gal63], a lower bound from [FKPT13] concerning neighborly polytopes shows that any linear programming lift of TC(d2,2d) must have size at least Ω(d2), whereas our semideﬁnite programming lift in this case has size O(dlog d) = o(d2). To the best of our knowledge this gives the ﬁrst example of a family of polytopes (Pd)d∈N in increasing dimensions where xcPSD(Pd) = o(xcLP(Pd)) where xcPSD and xcLP are respectively the SDP and LP extension complexity (see Section 2.3 for the deﬁnitions). More precisely, we have:

Corollary 1. There exists a family (Pd)d∈N of polytopes where Pd ⊂ R2d such that

log d d

xcPSD(Pd) xcLP(Pd)

= O

.

The only nontrivial linear programming lift for cyclic polytopes that we are aware of is a construction by Bogomolov et al. [BFMP14] for the polytope conv{(i,i2,...,id) : i = 1,...,N} which has size (log N) d/2 .

Main ideas We now brieﬂy describe the main ideas behind Theorem 1, which can be summarized in three steps:

- 1. A sum-of-squares certiﬁcate with a sparse Gram matrix: Given a nonnegative function f : G → R+ it is easy to see, since G is ﬁnite, that f can be written as a sum-of-squares. When the function f is supported on S, one can show that f admits a speciﬁc sum-of-squares representation where the Gram matrix Q, in the basis of characters, is sparse according to the graph Cay( G,S).
- 2. Chordal completion: Let Γ be a chordal cover of the graph Cay( G,S). Using well-known results concerning positive semideﬁnite matrices that are sparse according to a chordal graph [GT84, GJSW84] (see Section 2.2 for more details) one can decompose the Gram matrix Q into a sum of positivesemideﬁnite matrices, where each matrix is supported on a maximal clique of Γ. In terms of sum-ofsquares representation, this means that the function f can be written as:


f =

j

|fj|2 (7)

where each fj is supported on a maximal clique Cj of Γ.

- 3. Translation of cliques: The problem with the decomposition (7) is that even though each maximal clique Cj might be small, the union of the Cj’s might be large, and thus the total support of (7) might


be large (in fact the union of the Cj is the whole G). In order to reduce the total support of the sum-of-squares certiﬁcate (7), we use the following simple but crucial observation: if h is a function supported on C and if χ ∈ G then χh is supported on χC and we have |χh|2 = |h|2. Thus if for each maximal clique Cj of Γ we choose a certain χj ∈ G then, by translating each term in (7) by χj we obtain a sum-of-squares representation of f of the form f = j | hj|2 where hj is supported in χjCj. Having chosen the χj such that χjCj ⊆ T for all maximal cliques Cj (cf. Theorem 1), we get a representation of f as a sum-of-squares of functions supported on T .

Organization The paper is organized as follows. Section 2 starts by giving a brief review of Fourier analysis of ﬁnite abelian groups, as well as a review of chordal graphs, chordal covers and the main results concerning decomposition/matrix completion with chordal sparsity structure [GT84, GJSW84]. In Section 3 we prove our main result, Theorem 1. We present the proof using the two dual viewpoints of sum-ofsquares certiﬁcates and in terms of moment polytopes. In Section 4 we look at the case of the hypercube G = {−1,1}n mentioned earlier, and we look in particular at quadratic functions on the hypercube. We give an explicit chordal cover for the corresponding Cayley graph and we show how it leads to a proof of Laurent’s conjecture. In Section 5 we look at the special case G = ZN and functions of degree d. We give an explicit chordal cover for the corresponding graphs, and we discuss the consequences concerning positive semideﬁnite lifts of the trigonometric cylic polytope.

Notations We collect some of the notations used in the paper. If z ∈ C we denote by z the complex conjugate of z. Given a square matrix X ∈ Cn×n the Hermitian conjugate of X is denoted X∗, and X is called Hermitian if X∗ = X. The space of n × n Hermitian matrices is denoted Hn and the cone of Hermitian positive semideﬁnite matrices is denoted by Hn+. Similarly we denote by Sn the space of n × n real symmetric matrices and by Sn+ the cone of n × n real symmetric positive semideﬁnite matrices. If V is an arbitrary set, we will denote by CV the space of complex vectors indexed by elements of V , and by HV the space of Hermitian matrices where rows and columns are indexed by elements of V (and similarly for HV+ and SV ,SV+).

### 2 Preliminaries

In this section we present some background material needed for the paper: we ﬁrst recall some of the basic results and terminology concerning Fourier analysis on ﬁnite abelian groups [Rud90, Ter99], then we review the deﬁnition of chordal graph and the main results concerning sparse positive semideﬁnite matrices and matrix completion. We also review some of the terminology concerning lifts of polytopes/extended formulations.

#### 2.1 Fourier analysis on ﬁnite groups

Let G be a ﬁnite abelian group which we denote multiplicatively, and let F(G,C) be the vector space of complex-valued functions on G. A character χ of G is a group homomorphism χ : G → (C∗,×), i.e., it is an element of F(G,C) which satisﬁes:

χ(xy) = χ(x)χ(y) ∀x,y ∈ G.

Since G is abelian, one can easily show that the (pointwise) product of two characters is a character and that the (pointwise) inverse of a character is again a character. Thus if we denote by G the set of characters of G, then G forms an abelian group, where the group operation corresponds to pointwise multiplication. The group G is known as the dual group of G. Observe that since G is ﬁnite, if χ is a character then for any x ∈ G we have χ(x)|G| = χ(x|G|) = χ(1G) = 1, which implies that |χ(x)| = 1. It follows that the inverse of a character χ is simply its (pointwise) complex conjugate χ.

Consider the standard inner product on F(G,C): f,g =

1 |G| x∈G

f(x)g(x) ∀f,g ∈ F(G,C). (8)

A crucial property of the set of characters G is that they form an orthonormal basis of F(G,C), which is called the Fourier basis of G. Note that this implies in particular that | G| = |G|. We summarize this in the following theorem:

- Theorem 4. Let G be a ﬁnite abelian group and let G be the set of characters of G. Then G is an abelian group with pointwise multiplication. Furthermore | G| = |G| and G forms an orthonormal basis of F(G,C) for the standard inner product (8).


We now illustrate the previous theorem in the two examples G = {−1,1}n (the hypercube) and G = ZN presented in the introduction.

- Example 1 (Fourier analysis on the hypercube). Let G = {−1,1}n be the hypercube in dimension n which

forms a group of size 2n under componentwise multiplication, isomorphic to Zn2. Observe that if S is a subset of [n] then the function χS deﬁned by:

χS : {−1,1}n → C∗, χS(x) =

i∈S

xi

satisﬁes χS(xy) = χS(x)χS(y), and thus is a character of G. For example χ∅ is the constant function equal to 1, and χ[n] is the function χ[n](x) = x1 ...xn. One can show that these are all the characters of G, i.e., G = {χS,S ⊆ [n]}. Thus the decomposition of a function f : {−1,1}n → C in the basis of characters takes the form:

f(x) =

S⊆[n]

f(S)

i∈S

xi,

where f(S) are the Fourier coeﬃcients of f. ♦

- Example 2 (Fourier analysis on ZN). Let N be an integer and consider the (additive) group G = ZN of integers modulo N. For k ∈ ZN, deﬁne χk by


χk : ZN → C∗, χk(x) = e2iπkx/N.

Note that χk satisﬁes χk(x + y) = χk(x)χk(y) and thus χk is a character of ZN. It is not hard to show that any character χ of ZN actually must have the form χ = χk for some k ∈ ZN. Thus the dual group ZN of ZN is ZN = {χk,k ∈ ZN}. Note that χkχk = χk+k and (χk)−1 = χk = χ−k, and thus ZN is isomorphic to ZN. According to Theorem 4, any function f : ZN → C can be decomposed in the basis of characters:

f(k)e2iπkx/N ∀x ∈ ZN.

f(x) =

k∈ZN

This decomposition is nothing but the well-known Fourier decomposition of discrete signals of length N. ♦

For a general ﬁnite abelian group G, the Fourier decomposition of a function f : G → C, in the orthonormal basis of characters takes the form:

f(x) =

f(χ)χ(x).

χ∈ G

The coeﬃcients f(χ) are the Fourier coeﬃcients of f. By orthonormality of the basis of characters, we have for any χ ∈ G:

1 |G| x∈G

f(χ) = χ,f =

χ(x)f(x).

The support of a function f, denoted suppf is the set of characters χ for which f(χ) = 0: suppf = {χ ∈ G : f(χ) = 0}.

#### 2.2 Chordal graphs and matrix completion

In this section we recall some of the main results concerning sparse matrix decomposition and matrix completion with a chordal sparsity structure. For more details, we refer the reader to [GJSW84, GT84] and [AHMR88].

Chordal graphs Let G = (V,E) be a graph. The graph G is called chordal if any cycle of length at least four has a chord. A chordal cover (also called triangulation) of G is a graph G = (V,E ) where E ⊂ E and where G is chordal. Figure 1 shows a non-chordal graph G on four vertices and a chordal cover G of G.

1

1

2

2

| |
|---|


| |
|---|


4 3 G

4 3 G

Figure 1. A non-chordal graph G and a chordal cover G of G.

A subset C ⊆ V is a clique in G if {i,j} ∈ E for all i,j ∈ C, i = j. The clique C is called maximal if it is not a strict subset of another clique C of G. For example the maximal cliques of the graph G shown in Figure 1 are {1,2,4} and {2,3,4}.

Sparse matrices Let Q ∈ HV be a Hermitian positive semideﬁnite matrix where rows and columns are indexed by some set V . Assume furthermore that Q is sparse according to some graph G = (V,E), i.e.,

Qij = 0,i = j ⇒ {i,j} ∈ E.

One of the main tools used in this paper is a result from [GT84, GJSW84] which allows to decompose sparse positive semideﬁnite matrices as a sum of positive semideﬁnite matrices supported on a small subset of rows/columns. We say that a Hermitian matrix A is supported on C ⊆ V if Aij = 0 whenever i ∈/ C or j ∈/ C. The result can be stated as follows:

- Theorem 5. ([GT84, GJSW84]) Let Q be a Hermitian positive semideﬁnite matrix, and assume that Q is sparse according to some graph G. Assume furthermore that G is chordal. Then for every maximal clique C of G there exists a Hermitian positive semideﬁnite matrix QC supported on C such that:


Q =

QC. (9)

C

Remark. If the sparsity pattern G of Q is not chordal, one can still apply the previous theorem by considering a chordal cover G of G. Indeed if Q is sparse according to G then it also clearly sparse according to G , since G ⊆ G . In this case the summation (9) is over the maximal cliques of G .

- Example 3. We can illustrate the previous theorem with a simple 4×4 matrix. Let Q be the 4×4 Hermitian positive semideﬁnite matrix given by:


  

  .

2 1 − i 0 1 + i 1 + i 2 1 − i 0

Q =

- 0 1 + i 2 1 − i
- 1 − i 0 1 + i 2


Note that Q is sparse according to the “square graph” G shown in Figure 1(left). Since G is not chordal we cannot directly apply Theorem 5 with G, but we can apply it with G shown in Figure1(right) which is a chordal cover of G. In this case Theorem 5 asserts that one can decompose Q as a sum of two positive

semideﬁnite matrices supported respectively on the maximal cliques, {1,2,4} and {2,3,4}. For this example, it is not hard to ﬁnd an explicit decomposition, for example we can verify that:

  

  

  

  

2 1 − i 0 1 + i 1 + i 1 0 i

- 0 0 0 0
- 0 1 1 − i −i 0 1 + i 2 1 − i 0 i 1 + i 1


+

.

Q =

- 0 0 0 0
- 1 − i −i 0 1


0

0

♦

Matrix completion One can also state Theorem 5 in its dual form, in terms of the matrix completion problem. Given a graph G = (V,E), a G-partial matrix X is a matrix where only the diagonal entries, as well as the entries Xij for {i,j} ∈ E are speciﬁed. Given a G-partial matrix X, the positive semideﬁnite matrix completion problem asks whether X can be completed into a full |V | × |V | Hermitian matrix that is positive semideﬁnite. Clearly a necessary condition for such a completion to exist is that X[C,C] 0 for all cliques C of G (note that if C is a clique of G, then all the entries of X[C,C] are speciﬁed). When G is chordal, it turns out that this condition is also suﬃcient. The following theorem can actually be obtained from Theorem 5 via duality:

- Theorem 6. ([GJSW84]) Let G = (V,E) be a graph and let X be a G-partial matrix. Assume that G is chordal. Then X can be completed into a full |V | × |V | Hermitian positive semideﬁnite matrix if, and only if, X[C,C] 0 for all maximal cliques C of G.


#### 2.3 Lifts of polytopes

In this section we recall some of the deﬁnitions and terminology concerning lifts (or extended formulations) of polytopes. The concepts deﬁned here are not used in the proofs of our theorems, but simply make some of the results more convenient to state. We refer the reader to [Yan91, GPT13] for more details.

Let P ⊂ Rd be a polytope. We say that P has a LP lift of size k if P can be expressed as the linear

projection of an aﬃne section of the cone Rk+, i.e., if there exist π : Rk → Rd linear and an aﬃne subspace L ⊂ Rk such that:

P = π(Rk+ ∩ L). (10) Note that this deﬁnition is equivalent to say that P is the projection of a polytope Q with k facets. The smallest k such that P has a LP lift of size k is called the LP extension complexity of P and is denoted xcLP(P).

The deﬁnition of LP lift can be extended to PSD lifts, where instead we are looking to describe P using linear matrix inequalities. Formally, we say that P has a Hermitian PSD lift of size k if P can be expressed as the linear projection of an aﬃne section of the Hermitian positive semideﬁnite cone Hk+, i.e., if there exist π : Hk → Rd linear, and an aﬃne subspace L ⊂ Hk such that:

P = π(Hk+ ∩ L). (11)

The smallest k for which P has a PSD lift of size k is called the PSD extension complexity of P and denoted xcPSD(P). Note that one can also deﬁne PSD lifts with the cone of real symmetric positive semideﬁnite matrices Sk+ (instead of Hk+) and in this case we call the lift a real PSD lift.

### 3 Main result for general ﬁnite abelian groups

In this section we state and prove our main result in the general setting of ﬁnite abelian groups G. We ﬁrst describe the primal point of view concerning sparse sum-of-squares certiﬁcates of nonnegative functions, and then we present the dual point of view related to moment polytopes.

#### 3.1 Nonnegative functions and sum-of-squares certiﬁcates

Let G be a ﬁnite abelian group and let F(G,C) be the space of complex-valued functions on G. Given a nonnegative function f : G → R+, a sum-of-squares certiﬁcate for f takes the form:

K

|fk(x)|2 ∀x ∈ G. (12)

f(x) =

k=1

where f1,...,fK ∈ F(G,C).

It is well-known in the literature on polynomial optimization (see e.g., [Par00, Nes00, Las01]) that the existence of sum-of-squares certiﬁcates can be expressed in terms of the existence of a certain positive semideﬁnite matrix called a Gram matrix for f. This connection between sum-of-squares certiﬁcates and positive semideﬁnite matrices will be important in this paper, and so we recall this connection more formally in the next proposition:

- Proposition 1. Let n = |G| and let b1,...,bn be a basis for F(G,C). Let f : G → R be a real-valued function on G. Then f has a sum-of-squares representation (12), if, and only if, there exists a n × n Hermitian positive semideﬁnite matrix Q such that

f(x) = [b(x)]∗Q[b(x)] =

1≤i,j≤n

Qijbi(x)bj(x) ∀x ∈ G (13)

where [b(x)] := [bi(x)]i=1,...,n ∈ Cn. If (13) holds where Q is Hermitian positive semideﬁnite, we say that Q is a Gram matrix for f in the basis b1,...,bn.

Proof. Assume ﬁrst that f is a sum of squares, i.e., f(x) = Kk=1 |fk(x)|2. Since (b1,...,bn) forms a basis of F(G,C) we can write fk(x) = ni=1 akibi(x) for some coeﬃcients aki ∈ C. Note that |fk(x)|2 =

1≤i,j≤n akiakjbi(x)bj(x) and thus f(x) = k |fk(x)|2 = 1≤i,j≤n Qi,jbi(x)bj(x) where Q is the Hermitian matrix deﬁned by: Qi,j = k akiakj. Note that Q is positive semideﬁnite since it has the form Q = k aka∗k where ak is the vector (ak)i = aki.

We now show the converse. Assume f can be written as (13). Since Q is positive semideﬁnite, we can ﬁnd vectors ak such that Q = Kk=1 aka∗k. If we deﬁne fk to be the function fk(x) = ni=1 akibi(x) then we can verify that f = Kk=1 |fk|2.

| |
|---|


Given y ∈ G deﬁne the Dirac function δy at y by:

δy(x) =

1 if x = y 0 else.

Then it is easy to see that we have:

- Proposition 2. Any nonnegative function f on G has a sum-of-squares certiﬁcate as:


| f(y)δy(x)|2 ∀x ∈ G. (14)

f(x) =

y∈G

Said diﬀerently, a nonnegative function f is a sum-of-squares because if we pick b1,...,bn to be the basis of Dirac functions, then f satisﬁes Equation (13) where Q is the diagonal matrix consisting of the values taken by f on G.

Since we are working with functions on a ﬁnite abelian group G, it is more natural (and more beneﬁcial, as we see later) to look at sum-of-squares representation in the basis of characters. One reason for this is that typically the functions f we are interested in have a small support in the basis of characters and in this case one can hope to ﬁnd a sum-of-squares decomposition which also only involves a small number of characters. The next theorem is simply a change-of-basis in the formula (14).

- Proposition 3. Let f : G → R and assume that f is nonnegative, i.e., f(x) ≥ 0 for all x ∈ G. Deﬁne the Hermitian matrix Q ∈ R|G|×|G| indexed by characters χ ∈ G by:


Qχ,χ = f(χχ ). (15) Then Q is positive semideﬁnite and we have for any x ∈ G: f(x) =

1 |G|

1 |G|

[χ(x)]∗Q[χ(x)] =

Qχ,χ χ(x)χ (x). (16)

χ,χ ∈ G

Proof. Consider the matrix X = [χ(x)]x∈G,χ∈ G where rows are indexed by elements x ∈ G and columns are indexed by characters χ ∈ G. Since the characters form an orthonormal basis of F(G,C) for the inner product (8), this means that the matrix √1

X is a unitary matrix. Note that we can rewrite the deﬁnition

|G|

(15) of Q in matrix terms as follows:

1 |G|

X∗ diag([f(x)]x∈G)X,

Q =

where diag([f(x)]x∈G) is the diagonal matrix with the values f(x) on the diagonal. This shows that the eigenvalues of Q are the values {f(x),x ∈ G}, and thus Q is positive semideﬁnite. Since √1

X is unitary we also get that:

|G|

1 |G|

XQX∗. which, when evaluated at the diagonal entries is exactly Equation (16).

diag([f(x)]x∈G) =

| |
|---|


- Example 4. We now include a simple example to illustrate the previous theorem. Let G = Z6 and consider the function


- 1

- 2


(χ1(x) + χ−1(x)) = 1 − cos(2πx/6) ∀x ∈ Z6. (17)

f(x) = 1 −

Clearly f(x) ≥ 0 for all x ∈ Z6. Also note that f(0) = 1, f(1) = f(−1) = −1/2 and f(k) = 0 for all k ∈/ {−1,0,1}. The matrix Q deﬁned in (15) associated to this function f takes the form:





1 −1/2 0 0 0 −1/2

−1/2 1 −1/2 0 0 0 0 −1/2 1 −1/2 0 0 0 0 −1/2 1 −1/2 0 0 0 0 −1/2 1 −1/2

(18)

Q =

 

 

−1/2 0 0 0 −1/2 1

♦

We are now interested in nonnegative functions f : G → R that are supported on a subset S ⊆ G, i.e., f(χ) = 0 for all χ ∈/ S. For such functions we are interested in ﬁnding sparse sum-of-squares certiﬁcates for f, i.e., we are interested in ﬁnding a set T ⊆ G such that any nonnegative function f supported on S has a sum-of-squares certiﬁcate of the form:

K

|fk|2 where suppfk ⊆ T ∀k = 1,...,K. (19)

f =

k=1

The main idea to obtain such a “sparse” sum-of-squares certiﬁcate of f is to exploit the sparsity of the Gram matrix Q from Proposition 3. Indeed, note that if suppf = S, then the Gram matrix Q of Proposition 3 has a speciﬁc sparsity structure:

Qχ,χ = 0 ⇔ χχ ∈ S.

In other words, the sparsity structure of Q is given by the Cayley graph Cay( G,S). Recall the deﬁnition of a Cayley graph:

- Deﬁnition 1. Let H be a group and let S ⊂ H be a subset of H that is symmetric, i.e., x ∈ S ⇒ x−1 ∈ S. The Cayley graph Cay(H,S) is the graph where vertices are the elements of the group H, and where two distinct vertices x,y ∈ H are connected by an edge if x−1y ∈ S (or y−1x ∈ S, which is the same since S is symmetric).

Remark. We do not require the set S to be a generator for the group H and hence the graph Cay(H,S) may be disconnected. Also observe that the set S = suppf in our case is symmetric since f is real-valued; indeed when f is real-valued we have f(χ) = f(χ) for all χ ∈ G and thus χ ∈ suppf ⇒ χ ∈ suppf.

To obtain a set T ⊆ G such that (19) holds for all functions f supported on S we will study chordal covers of the graph Cay( G,S). We now introduce the key deﬁnition of Fourier support for a graph with vertices G.

- Deﬁnition 2. Let Γ be a graph with vertices G. We say that Γ has Fourier support (or frequencies) T ⊆ G


if for any maximal clique C of Γ there exists χC ∈ G such that χCC ⊆ T (where χCC := {χCχ : χ ∈ C} is the translation of C by χC).

Note that one can also state the deﬁnition of Fourier support of Γ in terms of equivalence classes of cliques: Given a subset C ⊆ G deﬁne the equivalence class of C to be all the subsets of G that can be obtained from C by translation, i.e., it is the set [C] := {χC : χ ∈ G}. Using this terminology, the graph Γ has Fourier support T if for any maximal clique C of Γ there is at least one representative from [C] that is contained in T .

We are now ready to state and prove our main theorem (the theorem below was stated as Theorem 1 in the introduction and we reuse the same numbering here since it is just a restatement).

Theorem 1. Let S be a symmetric subset of G and assume that Cay( G,S) has a chordal cover with Fourier support T ⊆ G. Then any nonnegative function supported on S admits a sum-of-squares certiﬁcate supported on T .

Proof. Let f : G → R be a nonnegative function supported on S. Let Q be the Gram matrix (15) associated to the sum-of-squares representation of f in the basis of characters. We saw that Q is sparse according to the Cayley graph Cay( G,S). Since Γ is a cover of Cay( G,S), Q is also sparse according to Γ. Thus, since Γ is chordal, using Theorem 5 we can ﬁnd a decomposition of Q as follows:

Q =

QC (20)

C

where the sum is over the maximal cliques C of Γ and where each QC is a positive semideﬁnite matrix supported on C. Note that Equation (20) implies that for all x ∈ G:

[χ(x)]∗Q[χ(x)] =

[χ(x)]∗QC[χ(x)],

C

where [χ(x)] := [χ(x)]χ∈ G. Since f(x) = [χ(x)]∗Q[χ(x)]/|G| the above equation says that: f(x) =

fC(x)

C

where we let fC(x) := [χ(x)]∗QC[χ(x)]/|G|. Since QC is positive semideﬁnite and supported on C, this means that each fC(x) is a sum-of-squares of functions supported on C ⊆ G, i.e.,

|fC,k|2

fC =

k

where suppfC,k ⊆ C.

According to Deﬁnition 2, we know that there exist χC ∈ G for each maximal clique C of Γ such that χCC ⊆ T . Now, observe that:

|fC,k|2 (=i)

|χCfC,k|2 (=ii)

| fC,k|2

f =

fC =

C

C k

C k

C k

where in (i) we used the fact that |χC|2 = 1 and in (ii) we let fC,k = χCfC,k which is supported on χCC ⊆ T . Thus we have shown that f is a sum-of-squares of functions supported on T .

| |
|---|


- Example 5. Let G = Z6 and let S = {−1,0,1} ⊂ Z6. We will use the previous theorem to show that any nonnegative function on Z6 supported on S = {−1,0,1} is a sum-of-squares of functions supported on


T = {−1,0,1,3} ⊆ Z6. The Cayley graph Cay( Z6,{−1,0,1}) is the cycle graph on 6 nodes shown in Figure 2(left). Clearly the graph is not chordal since the cycle 0,1,...,5 has no chord. Figure 2(right) shows a

chordal cover Γ of Cay( Z6,{−1,0,1}) where the maximal cliques are: C1 = {0,1,3}, C2 = {1,2,3}, C3 = {3,4,5}, C4 = {0,3,5}.

2 1

2 1

3

0

3

0

4 5 Cay( Z6,{−1,0,1}) Γ

4 5

Figure 2. Left: The Cayley graph Cay( Z6, {−1, 0, 1}) is the cycle graph on 6 nodes. Right: A chordal cover of the cycle graph, Γ.

Observe that if we translate the clique C2 = {1,2,3} by −2 we get {−1,0,1} and similarly if we translate the clique {3,4,5} by −4 we also get {−1,0,1}. Thus by choosing

= −2, χC

= −4, χC

χC

= 0, χC

= 0

1

2

3

4

we get that χC + C ⊆ {−1,0,1,3} for all maximal cliques C of Γ (we used the fact that 5 = −1 in Z6). In other words we have shown that Γ is a chordal cover of Cay( Z6,{−1,0,1}) with frequencies {−1,0,1,3}. Thus by Theorem 1, this means that any nonnegative function on Z6 supported on {−1,0,1} can be written as a sum-of-squares of functions supported on {−1,0,1,3}. ♦

#### 3.2 Dual point of view: moment matrices and matrix completion

Section 3.1 shows that nonnegative functions f : G → R that have Fourier support S can be written as sums of Hermitian squares of functions h : G → C with Fourier support T , where T satisﬁes a combinatorial property related to the Cayley graph Cay( G,S). In this section we describe the same results from the dual point of view, arriving at a dual statement (Theorem 1D) of the main result of Section 3.1 (Theorem 1). The dual result describes a certain moment polytope M(G,S) (see Deﬁnition 3 to follow) as the projection of a section of the cone of positive semideﬁnite matrices indexed by T . We could obtain this dual result by applying a conic duality argument directly to the statement of Theorem 1. The purpose of this section, however, is to re-explain the results of Section 3.1 from an alternative viewpoint.

##### 3.2.1 Moment polytopes

We begin by describing the moment polytope M(G,S) where S ⊆ G is a collection of characters. Concretely M(G,S) is the convex hull of a collection of complex vectors indexed by S:

M(G,S) = conv{(χ(x))χ∈S ∈ CS : x ∈ G}. The following deﬁnition is equivalent, somewhat easier to work with, and more readily generalizable.

- Deﬁnition 3. The moment polytope M(G,S) with respect to the characters S ⊆ G, is the convex polytope M(G,S) = {(Eµ[χ])χ∈S ∈ CS : µ a probability measure supported on G}.

For example, in the case where G = Z6 and S = {−1,1}, the moment polytope is M(Z6,{−1,1}) = conv{(e

−2πki

6 ,e

2πki

6 ) : k ∈ Z6}.

Nonnegative functions on ﬁnite abelian groups are sums of squares. Furthermore, we can express sums of squares concretely in terms of a Gram matrix. There is a similarly concrete way to describe the constraints that must be satisﬁed by a collection of complex numbers ∈ C G if they are a valid collection of moments of a probability measure supported on G. This description is given naturally in terms of a matrix constructed from ( χ)χ∈ G.

- Deﬁnition 4. If ∈ C G, the associated moment matrix is the square matrix with rows and columns indexed by G of the form


[M( )]χ,χ = χχ for all χ,χ ∈ G. If T ⊆ G and ∈ CT

−1T , the associated truncated moment matrix is the square matrix with rows and columns indexed by T of the form

[MT ( )]χ,χ = χχ for all χ,χ ∈ T .

We now describe the dual version of the fact that any nonnegative function on G is a sum of squares. Writing this in coordinates gives a concrete description in terms of moment matrices. That probability measures are real-valued and nonnegative, and have total mass one corresponds to the conditions that for any valid moment vector , the moment matrix M( ) is Hermitian and positive semideﬁnite, and has unit diagonal.

- Proposition 4. The moment polytope can be expressed as


M(G, G) = {( (χ))χ∈ G : (1 G) = 1, (|f|2) ≥ 0 for all f ∈ F(G,C)}. Equivalently, deﬁning coordinates χ := (χ) with respect to the character basis for F(G,C) we have M(G, G) = { ∈ C G : 1

= 1, M( ) 0}.

G

- Proof. See Appendix A.1


| |
|---|


Some readers may recognize this as essentially a statement of Bochner’s theorem for ﬁnite abelian groups [Rud90]. If we regard as a function : G → C, the condition that M( ) 0 is exactly saying that is a positive deﬁnite function on G. While we could use the language of positive deﬁnite functions throughout this section, we instead use the more concrete language of moment matrices. We do this both so that our descriptions are compatible with the literature on polynomial optimization, and so that they are easy to implement in code.

The polytope M(G,S) is just the projection of M(G, G) onto the coordinates cooresponding to S. Alternatively we can think of M(G,S) as those points in CS that can be completed to valid moment sequences. This suggests describing M(G,S) in terms of a structured positive semideﬁnite matrix completion problem. In this problem the diagonal is given, the entries corresponding to the edges of Cay( G,S) are given, and the goal is to complete the matrix to a positive semideﬁnite moment matrix.

- Corollary 2. The moment polytope with respect to S can be expressed as


M(G,S) = { ∈ CS : ∃y ∈ C G s.t. χ = yχ for all χ ∈ S, y1

G

= 1, M(y) 0}. (21)

In the example of M(Z6,{−1,1}) we index characters by {0,1,2,3,4,5} (so that −1 = 5). Then Corollary 2 tells us that M(Z6,{−1,1}) is the set of ( 5, 1) such that





1 1 y2 y3 y4 5

5 1 1 y2 y3 y4 y4 5 1 1 y2 y3 y3 y4 5 1 1 y2 y2 y3 y4 5 1 1

∃y2,y3,y4 ∈ C s.t.

0.

 

 

1 y2 y3 y4 5 1

Note that we adopt the convention, throughout, that writing M(y) 0 implies that M(y) is Hermitian. This may, in turn, imply certain linear equalities on y. For instance, in the above example the notation implies that 1 = 5 = −1 and y2 = y4 = y−2 and y3 = y3.

##### 3.2.2 Moment polytopes and matrix completion

In Proposition 3 we saw that any nonnegative (and hence sum of squares) function with Fourier support S has a Gram matrix that is sparse with respect to the graph Cay( G,S). The dual statement is that the moment polytope M(G,S) can be described in terms of an unstructured positive semideﬁnite matrix completion problem. In this case we are given the diagonal and the entries correponding to the edges of Cay( G,S) and just need to complete the matrix to be positive semideﬁnite, without requiring it to be a moment matrix.

- Proposition 5. The moment polytope with respect to S can be expressed as


M(G,S) = { ∈ CS : ∃Y ∈ H G+ s.t. Yχ,χ = χχ whenever χχ ∈ S and Yχ,χ = 1 for all χ ∈ G}. Idea of proof. We describe the main idea of the proof, giving the details in Appendix A.1. The key issue is to show that if ∈ CS has a completion to a positive semideﬁnite matrix Y ∈ H G+ then also has a completion to a positive semideﬁnite moment matrix M(y) (for some y ∈ C G). This can be established by observing that the group G acts on the rows and columns of Hermitian matrices H G by permutations. This action ﬁxes, pointwise, positive semideﬁnite moment matrices. Averaging the orbit of Y under this group action gives a moment matrix with the desired properties.

| |
|---|


Recall that Theorem 1 gave a combinatorial condition under which any nonnegative function with Fourier

- support S is not just a sum of squares, but a sum of squares of functions with Fourier support T . The dual version says that under the same combinatorial condition, to check that ∈ M(G,S) we are not required to complete it to a full positive semideﬁnite moment matrix. Instead it is enough to complete it to a truncated

moment matrix MT (y) for some y ∈ CT

−1T .

- Theorem 1D. Let S be a symmetric subset of G. If Cay( G,S) has a chordal cover with Fourier support T ⊆ G then


M(G,S) = { ∈ CS : ∃y ∈ CT

−1T s.t. yχ = χ for all χ ∈ S, y1

G

= 1, and MT (y) 0}. (22)

Idea of proof. Again we summarize the key idea, deferring a detailed proof to Appendix A.1. The main issue is to show that being able to complete to a truncated moment matrix MT (y) for some y ∈ CT

−1T implies

we can complete it to a positive semideﬁnite matrix Y ∈ H G+. Proposition 5 then implies we can complete it to a positive semideﬁnite moment matrix.

The key observation, analogous to the translation of frequencies idea in the proof of Theorem 1, is that given y ∈ CT

−1T , the partial moment matrices MχT (y) for any χ ∈ G are all the same. Hence imposing that MT (y) 0, implies that MχT (y) 0 for all χ ∈ G. Since Cay( G,S) has a chordal cover Γ with Fourier

- support T , we construct from y a partial matrix supported on the maximal cliques of Γ. The conditions


that MχT (y) 0 for all χ ∈ G are enough to show that all the principal submatrices supported on maximal cliques of Γ are positive semideﬁnite. The chordal matrix completion result (Theorem 6) completes the proof.

| |
|---|


Example (Example 5 cont.). Recall that the Cayley graph Cay( Z6,{−1,1}) is the 6-cycle. We label the elements of Z6 by {0,1,2,3,4,5}. The Cayley graph has a chordal cover (see Figure 2) with Fourier support T = {−1,0,1,3} = {5,0,1,3} (in Z6). Observe that T −1T = Z6. Applying Theorem 1D we see that

 

 

  

   0

1 1 y3 5

5 1 y2 y4 y3 y4 1 y2

M(Z6,{−1,1}) =

( 5, 1) : ∃y2,y3,y4 ∈ C s.t.

.





1 y2 y4 1

#### 3.3 Real sums-of-squares and moment polytopes

The main results of Sections 3.1 and 3.2 work with sums of Hermitian squares of complex-valued functions and complex Hermitian moment matrices respectively. While this is convenient mathematically, computationally it is desirable to work with real-valued functions and real symmetric moment matrices. In this section we give real versions of Theorem 1 and Theorem 1D. These are the forms most suited to implementation and the forms we use when discussing the examples in Sections 4 and 5 to follow.

Basic observations The main additional observation we make is that the dual group G consists of two types of characters: those that are real-valued, and those that are not. It is helpful to think of this decomposition in terms of the involution χ  → χ−1 = χ on G. Real-valued characters are those that are ﬁxed by inversion (complex conjuation). The remaining characters come in inverse (complex conjugate) pairs.

To ﬁx notation let G0 denote the real-valued characters and G−1∪ G1 be a ﬁxed partiton of the remaining

characters into conjugate pairs. In particular G−1 = G−1 1. If S ⊆ G is symmetric (i.e. S−1 = S) then inversion restricts to an involution on S and so we have the decomposition S = S0 ∪ S−1 ∪ S1 where Si = Gi ∩ S for i = −1,0,1.

Sums-of-squares Suppose f is a sum of Hermitian squares of functions fj : G → C, each supported on T ⊆ G. Then f can be expressed as a sum-of-squares of real-valued functions Re[fj] and Im[fj] as

f =

j

|fj|2 =

j

Re[fj]2 + Im[fj]2 .

Clearly Re[fj] and Im[fj] are supported on the symmetric subset T ∪ T −1 of characters. As such, the real analogue of Theorem 1 is the following, the only modiﬁcation being that we insist that T is symmetric.

- Theorem 7. Let S ⊆ G be symmetric and let f : G → R be a non-negative function supported on S. If T ⊆ G is symmetric and Cay( G,S) has a chordal cover with Fourier support T then f is a sum of squares of real-valued functions supported on T .


Real moment matrices and moment polytopes We now develop the real analogue of moment polytopes and moment matrices. The discussion is more explicit (and more involved) than was required for the sum-of-squares viewpoint. We begin by deﬁning real moment polytopes. These are just linear transformations of the moment polytopes of Section 3.2. Throughout this section for any symmetric S ⊆ G partitioned as S0 ∪ S−1 ∪ S1 ﬁx a linear map RS : CS → R|S| deﬁned by

RS( ) = (( χ)χ∈S

). Observe that RS depends on the partitioning of S.

,(Re[ χ],Im[ χ])χ∈S

0

1

- Deﬁnition 5. If S ⊆ G is symmetric and partitioned as S0 ∪ S−1 ∪ S1, the real moment polytope with respect to S is the image of M(G,S) under RS, i.e.


MR(G,S) = RS(M(G,S)).

This is a polytope in R|S| that is aﬃnely isomorphic to M(G,S). For example, in the case where G = Z6 and S = {−1,1} is decomposed as S−1 = {−1} and S1 = {1}, the real moment polytope is

MR(Z6,{−1,1}) = conv{(cos(2πk6 ),sin(2πk6 )) : k ∈ Z6}, the regular hexagon in the plane.

We have a description of M(G,S), and hence of MR(G,S) in terms of Hermitian positive semideﬁnite matrices. Using this it is straightforward to give a description in terms of real symmetric positive semideﬁnite matrices of twice the size (via (31) in Appendix A.2). Our aim is to describe the real moment polytope MR(G,S) in terms of real symmetric positive semideﬁnite matrices without increasing the size of the description. It turns out that we can do this whenever T has a property that is related to, but less restrictive than, being symmetric.

- Deﬁnition 6. A subset T ⊆ G has an equalizing involution if there is an involution σ : T → T such that σ(χ)χ = σ(χ )χ for all χ,χ ∈ G.


Observe that if T is symmetric, then the map that sends every element of T to its inverse satisﬁes χ−1χ = (χ )−1χ = 1 G for all χ,χ ∈ T . Hence any symmetric subset of G has an equalizing involution. An example of a set that has an equalizing involution but is not symmetric is T = {0,1,2,3} ⊆ Z5. Then T

is not symmetric and, furthermore, there is no k ∈ Z5 such that k + T is symmetric. Nevertheless, T does have an equalizing involution given by σ(0) = 3, σ(3) = 0, σ(1) = 2 and σ(2) = 1 since σ(k) + k = 3 for all k ∈ T .

Our main result in this section is the following.

- Theorem 8. Let S ⊆ G be symmetric and let T ⊆ G have an equalizing involution σ. If Cay( G,S) has a chordal cover with Fourier support T then


MR(G,S) = { RS( ) ∈ R|S| :∃y ∈ CT

−1T s.t. yχ = yχ for all χ ∈ T −1T , yχ = χ for all χ ∈ S, y1

= 1, and [Re[yχχ ] − Im[yσ(χ)χ ]]χ,χ ∈T 0 .

G

Note that the main change between Theorem 8 and Theorem 1D is that we have replaced the condition that the (Hermitian) truncated moment matrix MT (y) be positive semideﬁnite with the condition that a real symmetric matrix indexed by T be positive semideﬁnite. We also explicitly add the conjugate symmetry constraint that yχ = yχ, which was implied by MT (y) being Hermitian in Theorem 1D.

- Example 6. Before giving a proof, we apply Theorem 8 to the case of MR(Z6,{−1,1}), the regular hexagon in the plane. Recall that in this case we can take T = {0,1,3,5} which is symmetric. Hence T has σ(χ) = χ−1 as an equalizing involution. Decomposing G as G0 = {0,3} and, for instance G1 = {1,2} and G−1 = {4,5} we have that S0 = {0} and S1 = {1}. Note also that T −1T = G in this case, giving (T −1T )i = Gi for i = −1,0,1. Ordering the elements of T as (0,1,3,5) and writing uj = Re[ j], vj = Im[ j], wj = Re[yj] and xj = Im[yj]. we see that


  

  .

- w0 − x0 w1 − x1 w3 − x3 w5 − x5 w5 − x1 w0 − x2 w2 − x4 w4 − x0 w3 − x3 w4 − x4 w0 − x0 w2 − x2
- w1 − x5 w2 − x0 w4 − x2 w0 − x4


[Re[yχχ ] − Im[yσ(χ)χ ]]χ,χ ∈T = [wχχ − xχχ ]χ,χ ∈T =

The conjugate symmetry constraint on y implies that x0 = x3 = 0, w1 = w5, x1 = −x5, w2 = w4, and x2 = −x4. Applying these and the constraints that u1 = w1, v1 = x1 and w0 = 1, we obtain a description of the regular hexagon in the plane as

 

 

  

   0

1 u1 − v1 w3 u1 + v1 u1 − v1 1 − x2 w2 + x2 w2

MR(Z6,{−1,1}) =

(u1,v1) : ∃w2,w3,x2 ∈ R s.t.

.

w3 w2 + x2 1 w2 − x2 u1 + v1 w2 w2 − x2 1 + x2





♦

Proof of Theorem 8. We use a novel result that allows us to write certain complex Hermitian linear matrix inequalities as real symmetric linear matrix inequalities of the same size. The key requirement is that restricted to the subspace of Hermitian matrices of interest, entry-wise complex conjugation can be expressed

- as congruence by an orthogonal symmetric matrix.

Lemma 1. Let L be a subspace (over the reals) of Hd. Suppose there is some orthogonal J ∈ O(d) such that J2 = I and

JLJT = L for all L ∈ L, i.e. congruence by J restricted to L is entry-wise complex conjugation. Then

{L ∈ L : L ∈ Hd+} = {L ∈ L : Re[L] − J Im[L] ∈ Sd+}. Proof. See Appendix A.2.

| |
|---|


Let L be the subspace (over the reals) of HT given by L = {M(y) : y ∈ CT

−1T , yχ = yχ, for all χ ∈ T −1T }.

Let J be the |T | × |T | permutation matrix representing the equalizing involution σ : T → T . Since σ is an involution, J satisﬁes J2 = I. The deﬁnition of equalizing involution comes from our desire that σ satisfy the relation σ(χ)σ(χ ) = χχ , equivalent to the deﬁning relation in Deﬁnition 6, for all χ,χ ∈ T . Then for any conjugate symmetric y,

JM(y)J = [yχχ ]σ(χ),σ(χ )∈T = [yσ(χ)σ(χ )]χ,χ ∈T

= [yσ(χ)σ(χ )]χ,χ ∈T by conjugate symmetry of y

= [yχχ ]χ,χ ∈T since σ is an equalizing involution.

Hence congruence by J corresponds to entry-wise complex conjugation restricted to L. Applying Lemma 1 we can conclude that for all y ∈ CT

−1T ,

M(y) 0 ⇐⇒ yχ = yχ ∀χ ∈ T −1T and [Re[yχχ ] − Im[yσ(χ)χ ]]χ,χ ∈T 0. This completes the proof of Theorem 8.

| |
|---|


4 Application 1: The case G = Zn2 and binary quadratic optimization

In this section we apply the results of Section 3.1 to the case of nonnegative quadratic forms on the vertices of the hypercube in n dimensions. Dually, the moment polytope of interest in this section is the nth cut polytope CUTn. Our main aim is to establish Laurent’s conjecture [Lau03, Conjecture 4] that any nonnegative quadratic form on the vertices of the hypercube in n dimension is a sum of squares of polynomials of degree

- at most n/2 .


#### 4.1 Quadratic forms on {−1,1}n and the cut polytope

Let G = {−1,1}n be the vertices of the hypercube in dimension n. View G as a group (isomorphic to Zn2) under componentwise multiplication. Recall that the characters of G are indexed by subsets S ∈ 2[n] and are the square-free monomials

xi for all x ∈ G.

χS(x) =

i∈S

We focus on characterizing nonnegative quadratic funcions on G. These are of particular interest because the problem of maximizing a quadratic form over G i.e.

max

Aijxixj (23)

x∈G

1≤i<j≤n

{1}

∅

- {1,3} {1,4}

{3,4}

- {2,3} {2,4}


{3} {4}

{1,2}

{2}

{1,3,4} {1,2,3} {1,2,4}

{1,2,3,4}

{2,3,4}

Figure 3. The Cayley graph Cay( G, S) for G = {−1, 1}4 and S = {S : |S| = 0 or |S| = 2}. The two connected components are Teven (left) and Todd (right). The vertices of Todd are arranged to correspond to their images in Teven under the graph automorphism φ(S) = {1} S. We can obtain a chordal cover of Cay( G, S) by forming maximal cliques on the vertices of Teven marked with ﬁlled circles, the vertices of Teven marked with open circles, and the images in Todd of these two cliques under the map φ.

includes, for example, the max-cut problem, which arises when the symmetric matrix Aij is the Laplacian of a (weighted) graph on n vertices. We can solve (23) by ﬁnding the smallest upper bound on the objective:

γ s.t. γ −

min

γ

Aijxixj ≥ 0 for all x ∈ G. (24)

1≤i<j≤n

If we have a characerization of nonnegative functions on G with Fourier support S = {S ∈ 2[n] : |S| = 0 of |S| = 2} as sums of squares of functions supported on T ⊆ G then we can solve (24) by solving a semideﬁnite optimization problem of size |T |.

The dual picture to (24) is to consider optimization over the moment polytope M({−1,1}n,S \ {∅}), known as the cut polytope

CUTn := M({−1,1}n,S \ {∅}) = conv {(xixj)1≤i<j≤n : (x1,x2,...,xn) ∈ {−1,1}n}.

We can solve the binary quadratic optimization problem (23) by optimizing the linear function deﬁned by A over CUTn, i.e. by solving the linear program

max

( ij)1≤i<j≤n

i<j

ijAij s.t. ( ij)1≤i<j≤n ∈ CUTn.

If we have a PSD lift of the cut polytope CUTn of size |T | then we can solve this optimization problem by solving a semideﬁnite optimization problem of size |T |.

#### 4.2 The associated Cayley graph

To apply the results of Section 3.1 we need to understand the graph Cay( G,S). In the case n = 4 this graph is shown in Figure 3. Throughout this section we identify the character χS ∈ G with the subset S ⊆ [n] that indexes it and work exclusively in the language of subsets. As such, the vertex set of Cay( G,S) is 2[n], the collection of all subsets S ⊆ [n]. There is an edge between two subsets S,T if and only if |S T| = 2. This graph is often called the half-cube graph.

The group operation on characters is multiplication of functions, which corresponds to taking the symmetric diﬀerence of the subsets that index the characters. In other words, if S,T ⊆ [n] then

χS(x)χT(x) = χS T(x)

- where S T = (S\T)∪(T \S). As such, there is an action of G on the vertices of Cay( G,S) by S·T = S T. Furthermore if T ⊆ 2[n] is a subset of the vertices of Cay( G,S) we write S T := {S T : T ∈ T }.

We now record some simple observations that follow directly from the adjacency relation in Cay( G,S). For convenience of notation, for k = 0,1,...,n let

Tk = {S ⊆ [n] : |S| = k}.

Any edge of Cay( G,S) either has both endpoints in Tk for some k or one endpoint in Tk and the other in Tk+2 for some k. Consequently, Cay( G,S) has two connected components

Teven = T0 ∪ T2 ∪ ··· ∪ T2 n/2 and Todd = T1 ∪ T3 ∪ ··· ∪ T2 n/2 −1.

Deﬁne a map φ : 2[n] → 2[n] by φ(S) = {1} S. Since |φ(S) φ(T)| = |S T| for all S,T ∈ 2[n] it follows that φ extends to an automorphism of Cay( G,S) that exchanges Teven and Todd.

4.3 Applying Theorem 1

To apply Theorem 1 from Section 3.1 we need to ﬁnd a subset T ⊆ 2[n] of vertices such that Cay( G,S) has a chordal cover with Fourier support T . The following result explicitly describes such a collection of vertices.

Proposition 6. The graph Cay( G,S) has a chordal cover with Fourier support

T = T0 ∪ T2 ∪ ··· ∪ T n/2 if n/2 even T1 ∪ T3 ∪ ··· ∪ T n/2 if n/2 odd.

(25)

Proof. We give a detailed proof in Appendix A.3.

| |
|---|


Example 7. To give the ﬂavor of the proof, we discuss the case n = 4. In this case Cay( G,S) is shown in Figure 3. Deﬁne Γ to be the graph with vertex set 2[4] and with edges between S,T ∈ Teven if and only if ||S| − |T|| ≤ 2, and edges between S,T ∈ Todd if and only if ||φ(S)| − |φ(T)|| ≤ 2. The graph Γ is chordal, with maximal cliques given by C0 = T0 ∪T2, C2 = T2 ∪T4, φ(C0), and φ(C2). The vertices in cliques C0 and C2 are indicated by open and ﬁlled circles respectively in Figure 3. (The vertices in cliques φ(C0) and φ(C2) are similarly marked.) If T = T0∪T2 then we can see that Γ is a chordal cover of Cay( G,S) with Fourier support T by observing that ∅ C0 ⊆ T , {1,2,3,4} C2 ⊆ T , φ(∅) φ(C0) ⊆ T and φ({1,2,3,4}) φ(C2) ⊆ T . ♦

Laurent’s conjecture follows directly from Proposition 6 and Theorem 1.

Theorem 2. Suppose f(x) = A∅ + 1≤i<j≤n Aijxixj is nonnegative on G. Then there is a collection (hk)|Tk=1| of functions hk : G → R each supported on T (deﬁned in (25)) such that

f(x) =

|T |

k=1

hk(x)2.

Consequently, any nonnegative quadratic form on G is a sum of squares of functions of degree at most n/2 . Proof. The ﬁrst assertion follows directly from Proposition 6 and Theorem 1. The second assertion holds simply because every function supported on T has degree at most n/2 .

| |
|---|


The dual version of this result gives a PSD lift of the cut polytope of size |T |. It follows directly from

- Proposition 6 and Theorem 1D, and the observation that in this case all the characters are real-valued.


Corollary 3. The cut polytope CUTn has a real PSD lift of size |T | given by

CUTn = ∈ RS\∅ : ∃y ∈ RT  T s.t. y∅ = 1, y{i,j} = {i,j} for 1 ≤ i < j ≤ n, and [yS T]S,T∈T 0

- where T is deﬁned in (25).


In the language used, for example, in [Lau03] when discussing the Lasserre hierarchy for binary quadratic optimization, Corollary 3 could be expressed simply as Q n/2 = CUTn for all n.

### 5 Application 2: The case G = ZN and cyclic polytopes

In this section we apply the results of Section 3 to the case where G = ZN is the (additive) group of integers modulo N. As we will see, this will allow us to obtain a positive semideﬁnite lift of size O(dlog(N/d)) for the regular trigonometric cyclic polytope with N vertices of degree d, when d divides N.

Recall from Section 2, that the characters of ZN are indexed by k ∈ ZN and are given by: χk(x) = e2iπkx/N ∀x ∈ ZN. Thus the Fourier decomposition of a function f : ZN → C is given by: f(x) =

f(k)e2iπkx.

k∈ZN

Furthermore, we say that a function f has degree d if it is supported on {−d,−(d − 1),...,d − 1,d}.

#### 5.1 The case S = {−1,0,1}: the cycle graph

In this section we are interested in obtaining sparse sum-of-squares certiﬁcates for functions of degree 1 on ZN, i.e., functions supported on S = {−1,0,1}. Note that the real moment polytope MR(ZN,{−1,1}) in this case is just the regular N-gon in the plane:

MR(ZN,{−1,1}) = conv (cos(2πx/N),sin(2πx/N)) : x ∈ ZN .

To obtain sparse sum-of-squares for nonnegative functions of degree 1 we are going to study the Cayley graph Cay( ZN,{−1,0,1}). Note that this is simply the cycle graph on N vertices, which we will denote by CN for simplicity. The object of this section is to show that this graph admits a chordal cover with a small number of frequencies. We show:

- Theorem 9. Let N be a positive integer greater than 2. Then CN has a chordal cover with frequencies T ⊆ ZN where |T | ≤ 3log2 N. More precisely the set T can be described explicitly as follows: Let k1 < k2 <


··· < kl be the positions of the nonzero digits in the binary expansion of N so that N = lj=1 2k

. Let k be

j

the largest integer such that 2k < N (i.e., k = k1 − 1 if N is a power of two and k = kl otherwise). Then the set T is given by

 

 

- i
- j=1


T = {0} ∪ {−2i,2i,i = 0,...,k − 1} ∪

2k

,i = 1,...,l − 2

. (26)

j





Proof. The chordal cover is constructed by induction on N, see Appendix A.4 for the details. Figure 4 shows the chordal cover for N = 8 and N = 16.

| |
|---|


If we combine the previous theorem with Theorem 1, we get that any nonnegative degree-1 function on ZN has a sum-of-squares certiﬁcate supported on T where |T | ≤ 3log N. Note that this corresponds to

- Theorem 3 from the introduction for the case d = 1. Dually, this allows us to obtain a Hermitian positive semideﬁnite lift of the regular N-gon of size |T | ≤ 3log N.


In a previous paper [FSP14] we showed that the N = 2n-gon admits a positive semideﬁnite lift of size 2n − 1. In fact we showed that any linear function on ZN that is nonnegative can be written as a sum-ofsquares of functions supported on {0} ∪ {±2i,i = 0,...,n − 2}. Note that this is the same set of frequencies that we get if we plug N = 2n in (26). Thus Theorem 9 generalizes the result of [FSP14] for arbitrary N.

#### 5.2 Degree d functions: powers of cycle graph

In this section we are interested in functions of degree d on ZN where d divides N. We show how to construct a chordal cover of the associated Cayley graph Cay( ZN,S) using the chordal cover of the cycle graph constructed in the previous section. This allows us to show that any nonnegative function on ZN of degree d has a sum-of-squares certiﬁcate supported on at most 3dlog(N/d) frequencies.

4 5

3

2 3

6

2

1

- 7

- 8

- 9

- 10


- 0

- 1


4

0

15

5

7

14

6

11

13

12

Figure 4. Triangulation of the 8-cycle with frequencies T = {−2, −1, 0, 1, 2} and of the 16-cycle with frequencies T = {−4, −2, −1, 0, 1, 2, 4}.

##### 5.2.1 Triangulating the Cayley graph

Observe that the Cayley graph Cay( ZN,S) when S = {−d,...,d} is the d’th power of the cycle graph CN. Recall the deﬁnition of power of a graph:

- Deﬁnition 7. Let G = (V,E) be a graph. Given d ∈ N, the d’th power of G is the graph Gd = (V,Ed) where two vertices u,v ∈ V are connected if there is a path of length ≤ d connecting u and v in G.

Following this observation, we will use the symbol CNd to denote the Cayley graph Cay( ZN,{−d,...,d}). Figure 5(left) shows the graph CNd for N = 8 and d = 2.

C82 C4 K2

0

1

2 3

4

5

6

7

0

1

2 3

4

5

6

7

Figure 5. Left: The second power of the cycle graph on 8 nodes: two nodes are connected by an edge if their distance in the cycle graph is at most 2. Right: The graph C4 K2. Note that C82 ⊂ C4 K2. The edges in C4 K2 that are not in C82 are indicated with a heavier line.

To construct a triangulation of CNd we will actually use the triangulation of the cycle graph CN constructed in the previous section. For this, we need the following deﬁnition of strong product of graphs:

- Deﬁnition 8. Given graphs G = (V,E) and G = (V ,E ) deﬁne the strong product of G and G , denoted G G to be the graph with vertex set V × V and where two vertices (u,u ) ∈ V × V and (v,v ) ∈ V × V are connected if:


(u = v and {u ,v } ∈ E ) or ({u,v} ∈ E and u = v ) or ({u,v} ∈ E and {u ,v } ∈ E ).

Remark. An important special case is when one of the graphs, say G , is a complete graph G = Km. In this case two distinct vertices (u,u ) and (v,v ) in G Km are connected if either u = v or {u,v} ∈ E(G).

Given two graphs G = (V,E) and G = (V,E ) with the same vertex set V we say that G covers G and we write G ⊆ G if E ⊆ E . Our main observation to construct a chordal cover of CNd is the following:

- Proposition 7. Let N and d be two integers and assume that d divides N. Let CNd be the d’th power of the cycle graph CN and let CN/d be the cycle graph on N/d nodes. Then

CNd ⊆ CN/d Kd. (27)

Proof. To show the inclusion (27) we ﬁrst need to identify the vertices of CNd with those of CN/d Kd. Note that the vertex set of CNd can be identiﬁed with ZN and the vertex set of CN/d can be identiﬁed with ZN/d. We also identify the vertices of Kd with {0,...,d − 1}. By deﬁnition of , the vertices of CN/d Kd are ZN/d × {0,...,d − 1}. Consider the map:

φ : ZN/d × {0,...,d − 1} → ZN, φ(q,r) = qd + r. (28)

This map is well-deﬁned and gives a bijection between ZN/d × {0,...,d − 1} and ZN. The map φ thus identiﬁes vertices of CNd with those of CN/d Kd.

We now show that, with this identiﬁcation, inclusion (27) holds. We need to show that if i,i ∈ ZN are

connected in CNd (i.e., i − i ∈ {−d,...,d}) then necessarily (q,r) and (q ,r ) are connected in CN/d Kd (i.e., q − q ∈ {−1,0,1}), where (q,r) and (q ,r ) are such that i = φ(q,r) and i = φ(q ,r ). Consider for

q ∈ ZN/d the set of vertices of CNd given by Vq = {φ(q,r) : r = 0,...,d − 1} ⊂ ZN. Note that (Vq)q∈Z

N/d

forms a partition of the vertex set of CNd and that |Vq| = d for all q (for example if N = 8 and d = 2 (Figure of CNd , then i and i must be in the same group (i.e., i,i ∈ Vq) or in adjacent group (i.e., i ∈ Vq and i ∈ Vq+1 or vice-versa). In other words this means that q − q ∈ {−1,0,1} which means that (q,r) and (q ,r ) are connected in CN/d Kd.

- 5) V0 = {0,1},V1 = {2,3},V2 = {4,5},V4 = {6,7}). It is easy to see that if i and i are two adjacent vertices


| |
|---|


The previous proposition gives a natural way to construct a chordal cover of CNd from that of CN/d. Indeed if Γ is a chordal cover of CN/d then one can show that Γ Kd is a chordal cover of CNd and one can also characterize the maximal cliques of Γ Kd in terms of those of Γ. This is the object of the next proposition.

- Proposition 8. Let G = (V,E) be a graph and d be any integer.

- 1. If G is such that G ⊆ G then G Kd ⊆ G Kd.
- 2. If G is chordal then G Kd is chordal.
- 3. All the maximal cliques of G Kd have the form C × Kd where C is a maximal clique of G.


Proof. 1. The ﬁrst point is clear from the deﬁnition of .

- 2. Let (u1,v1)...(ul,vl) be a cycle in G Kd of length l ≥ 4 where (ul,vl) = (u1,v1). If there exists i ∈ {1,...,l − 1} such that ui = ui+1 then the edge {(ui,vi),(ui+2,vi+2)} is a chord of the cycle. Otherwise note that u1 ...ul is a cycle in G of length ≥ 4. Since G is chordal there is 1 ≤ i,j ≤ l − 1 with j − i ≥ 2 such that {ui,uj} ∈ E. In this case the edge {(ui,vi),(uj,vj)} is a chord of the cycle.
- 3. The third property easily follows from the fact that if C = {(ui,vi),i = 1,...,k} is a clique in G Kd then {ui,i = 1,...,k} ⊆ V is a clique in G.


| |
|---|


We can now use the triangulation of the cycle graph constructed in the previous section to obtain a triangulation of CNd .

- Proposition 9. Let N and d be two integers and assume that d divides N. If CN/d has a triangulation with frequencies T ⊆ ZN/d, then CNd has a triangulation with frequencies


T = {dk + r : k ∈ T ,r ∈ {0,...,d − 1}}. (29) Note that |T | ≤ d · |T |.

Proof. Let Γ be a triangulation CN/d with frequencies T . By deﬁnition, this means that for any maximal clique C of CN/d, there is kC ∈ ZN/d such that kC + C ⊆ T .

By Proposition 8, we know that Γ Kd is a chordal cover of CNd . Let C be a maximal clique of Γ Kd. By Proposition 8, we know that there exists C maximal clique of Γ such that C = C × Kd = {dq + r : q ∈ C,r ∈ {0,...,d − 1}}. Deﬁne kC = dkC ∈ ZN and note that:

kC + C = {dkC + dq + r : q ∈ C,r ∈ {0,...,d − 1}}

= {(kC + q)d + r : q ∈ C,r ∈ {0,...,d − 1}} ⊆ T ,

where the last inclusion follows from the fact that kC + q ∈ T whenever q ∈ C. We have thus shown that for any maximal clique C of Γ Kd, there is kC ∈ ZN such that kC + C ⊆ T . Thus this shows that Γ Kd is a chordal cover of CNd with frequencies T .

| |
|---|


Combining Proposition 9 and the triangulation of the cycle graph from Theorem 9 we get the following corollary:

- Corollary 4. Let N and d be two integers and assume that d divides N. Then the graph CNd has a triangulation with frequencies T ⊂ ZN where |T | ≤ 3dlog(N/d).

Using Theorem 1, this proves Theorem 3 from the introduction concerning nonnegative functions on ZN of degree d.

Theorem 3. Let N and d be two integers and assume that d divides N. Then there exists T ⊆ ZN with |T | ≤ 3dlog(N/d) such that any nonnegative function on ZN of degree at most d has a sum-of-squares certiﬁcate supported on T .

Figure 6 shows the triangulation of C162 obtained by triangulating C8 using Theorem 9 and applying the strong graph product with K2.

- 0

- 1


2

3

5 4 6

7

- 8

- 9

- 10 11


12 13

14

15

Figure 6. Triangulation of the graph C162 obtained as the strong graph product of Γ and K2, where Γ is the triangulation of C8 obtained from Theorem 9 and illustrated in Figure 4(left).

- 5.2.2 Cyclic polytopes Observe that the real moment polytope for G = ZN and S = {−d,...,d} is given by:


MR(ZN,{−d,...,d}) = conv (cos(2πx/N),sin(2πx/N),...,cos(2πdx/N),sin(2πdx/N)),x ∈ ZN ⊂ R2d. This is just the regular trigonometric cyclic polytope which we abbreviate by TC(N,2d):

TC(N,2d) = conv M(2πx/N) : x = 0,1,...,N − 1 ⊂ R2d, (30)

where M(θ) is the degree d trigonometric moment curve:

M(θ) = cos(θ),sin(θ),cos(2θ),sin(2θ),...,cos(dθ),sin(dθ) .

Cyclic polytopes play an important role in polyhedral combinatorics [Zie95] and satisfy many interesting properties. For example the celebrated Upper Bound Theorem, states that for any 2d dimensional polytope P with N vertices, fi(P) ≤ fi(TC(N,2d)) for any i = 0,...,2d, where fi(P) is the number of i-dimensional faces of a polytope P [Zie95]. Another important property of cyclic polytopes is that they are neighborly [Gal63] (recall that a 2d-dimensional polytope P is called neighborly if any collection of d vertices of P span a face of P).

The results from this section allow us to obtain a positive semideﬁnite lift of TC(N,2d) of size O(dlog(N/d))

when d divides N. More precisely, if we combine Corollary 4 and Theorem 1D we get that TC(N,2d) has a Hermitian positive semideﬁnite lift of size at most 3dlog(N/d), proving Theorem 3D from the introduction:

Theorem 3D. Let N and d be two integers and assume that d divides N. Then the trigonometric cyclic polytope TC(N,2d) has a Hermitian positive semideﬁnite lift of size at most 3dlog(N/d).

Real positive semideﬁnite lifts Using the results of Section 3.3 one can convert the Hermitian positive semideﬁnite lift of TC(N,2d) into a real positive semideﬁnite lift of size at most 4dlog(N/d). Indeed, ﬁrst note that in the case d = 1, if T is the set of frequencies (26) for the cycle graph CN then T ∪ (−T ) has cardinality at most 4log(N) and the set T ∪(−T ) clearly has an equalizing involution since it is symmetric. Thus this shows that in the case d = 1, the moment polytope MR(ZN,{−1,1}) has a real positive semideﬁnite lift of size at most 4log(N). For the case where d > 1 and d divides N it is not diﬃcult to show that if T has an equalizing involution σ then T deﬁned in (29) also has an equalizing involution. Indeed given k ∈ T and r ∈ {0,...,d − 1}, deﬁne σ : T → T by σ (dk + r) = dσ(k) + d − r − 1 (such a map is well-deﬁned). Then σ (dk + r) + dk + r = d(σ(k) + k) + d which is a constant independent of k and r, and thus σ is an equalizing involution for T . Thus using the symmetric set of frequencies for the cycle graph CN/d (of size 4log(N/d)) we get that T has size at most 4dlog(N/d) and has an equalizing involution. Thus this shows that MR(ZN,{−d,...,d}) has a real positive semideﬁnite lift of size at most 4dlog(N/d).

Comparison with LP lifts One can show that in the regime N = Θ(d2) our positive semideﬁnite lift for TC(N,2d) is provably smaller than any linear programming lift of TC(N,2d). Indeed, the following lower bound on the LP extension complexity of k-neighborly polytopes was proved in [FKPT13]:

- Proposition 10. ([FKPT13, Proposition 5.16]) If P be a k-neighborly polytope with N vertices then xcLP(P) ≥ min(N,(k + 1)(k + 2)/2).


Since TC(N,2d) is d-neighborly, if we choose for example N = d2 then the previous proposition asserts that xcLP(TC(d2,2d)) ≥ Ω(d2) whereas in this case our positive semideﬁnite has size O(dlog d). This allows us to prove the following result giving a gap between SDP extension complexity and LP extension complexity.

Corollary 1. There exists a family (Pd)d∈N of polytopes where Pd ⊂ R2d such that

log d d

xcPSD(Pd) xcLP(Pd)

= O

.

The only nontrivial LP lift for cyclic polytopes that we are aware of is a recent construction by Bogomolov et al. [BFMP14] for the cylic polytope

C(N,d) = conv (i,i2,...,id) : i = 1,...,N

of size (log N) d/2 . Note that this lift has smaller size than the “trivial” vertex lift of C(N,d) only when d < O((log N)/(log log N)). Their construction for d = 2 is based on the reﬂection relations framework of Kaibel and Pashkovich [KP11] and the case of general d is then obtained via tensor products.

### 6 Conclusion

In this paper we studied nonnegative functions f deﬁned on a ﬁnite abelian group G. We looked at functions f that have a sparse Fourier support S and we identiﬁed a certain combinatorial condition involving chordal covers of the Cayley graph Cay( G,S), that guarantees the existence of a sparse sum-of-squares certiﬁcate for any nonnegative function supported on S. We applied our general framework to two special cases. First we looked at quadratic functions deﬁned on the hypercube G = {−1,1}n and we showed that any nonnegative quadratic function on G has a sum-of-squares certiﬁcate of degree at most n/2 . This proves a conjecture by Laurent from 2003 [Lau03] and shows that the Lasserre hierarchy for the cut polytope converges after

n/2 steps. Second, we looked at nonnegative functions deﬁned on G = ZN, the group of integers modulo N. We showed that when d divides N, any degree d nonnegative function on ZN has a sum-of-squares certiﬁcate with functions supported on some T where |T | ≤ O(dlog(N/d)). From the geometric point of view, this establishes that the regular trigonometric cyclic polytope of degree d in N vertices has a positive semideﬁnite lift of size O(dlog(N/d)). For the regime N = Θ(d2) this gives us a family of polytopes in increasing dimensions, where the ratio of the PSD extension complexity to the LP extension complexity is O((log d)/d).

Equivariance of lifts Observe that the moment polytopes M(G,S) ⊂ CS considered in this paper are invariant under the natural action of G on CS given by ρ(x) = diag([χ(x)]χ∈S). One can show that the Hermitian PSD lifts for M(G,S) considered in this paper respect this symmetry of M(G,S), in a certain formal sense known as equivariant lifts deﬁned in [FSP13].

Open problems We conclude by brieﬂy discussing two concrete problems about regular trigonometric cyclic polytopes arising from this work. In previous work we showed that any ZN-equivariant PSD lift of the regular N-gon must have size at least ln(N/2) [FSP14, Theorem 9]. Since all the Hermitian PSD lifts in this paper are equivariant, this shows that it is not possible to construct substantially better equivariant PSD lifts of the regular N-gons than the construction given in Theorem 3D with d = 1. It would be interesting to establish corresponding lower bounds for general d.

- Problem 1. Find lower bounds on the size of (ZN-equivariant) PSD lifts of the regular trigonometric cyclic polytope of degree d in N vertices.

Problem 9.9 of [FGP+14] asks for a “family of polytopes that exhibits a large (e.g. exponential) gap between its nonnegative and psd ranks”. We have found that the regular trigonometric cyclic polytope of degree d in N = d2 vertices gives an explicit family of polytopes for which we can prove a signiﬁcant (but far from exponential) gap between PSD and LP extension complexity. It may be possible to prove a better lower bound (parameterized by N and d) on the LP extension complexity for this family of polytopes since the bound we use only uses the fact that the polytope is neighborly. Such a lower bound may allow us to establish a larger gap between the LP and PSD extension complexity of these polytopes.

- Problem 2. Find N(d) to make the gap between the LP and PSD extension complexity of regular trigonometric cyclic polytopes of degree d in N(d) vertices as large as possible.


### A Additional proofs

- A.1 Proofs from Section 3.2 In this section we provide detailed proofs of the main results in Section 3.2.


Proof of Lemma 4. Suppose µ is a probability measure supported on G. Then because µ is a probability measure, (Eµ[χ])χ∈S certainly satisﬁes Eµ[1 G] = 1 and Eµ[|f|2] ≥ 0 whenever f ∈ F(G,C). Conversely, suppose is a linear functional on F(G,C) such that (1 G) = 1 and (|f|2) ≥ 0 for all f ∈ F(G,C). We show that (·) coincides with Eµ[·] for some probability measure µ supported on G. For any x ∈ G deﬁne

###### µ({x}) = (δx). Since δx = |δx|2 we have that µ({x}) = (|δx|2) ≥ 0 for all x ∈ G. Since is linear

µ({x}) =

δx = (1 G) = 1.

x∈G

x∈G

Hence µ deﬁnes a probability measure supported on G and (·) is exactly the corresponding expectation Eµ[·]. The second description of M(G, G) in the lemma follows by rewriting the condition (|f|2) for all f ∈ F(G,C) in coordinates with respect to the character basis as

f(χ)χ 2) =

(χχ ) f(χ) f(χ ) for all ( f(χ))χ∈ G ∈ C G.

(

χ,χ ∈ G

χ∈ G

This is exactly the deﬁnition of the matrix M( ) = [ χχ ]χ,χ ∈ G being Hermitian positive semideﬁnite.

| |
|---|


- Proof of Proposition 5. If ( χ)χ∈S ∈ M(G,S) then from Corollary 2 there is (yχ)χ∈ G such that yχ = χ for


all χ ∈ S, y1

= 1, and M(y) 0. Hence we can take Yχ,χ = yχχ to show that ( χ)χ∈S is an element of the right hand side of (21).

G

Conversely, suppose there exists Y ∈ H G+ with Yχ,χ = χχ whenever χχ ∈ S and Yχ,χ = 1 for all χ ∈ G. Our task is to construct, from Y some (yχ)χ∈ G such that yχ = χ for all χ ∈ S, y1

= 1, and M(y) 0. Observe that G acts on Hermitian matrices H G indexed by elements of G by simultaneously permuting the rows and columns, i.e. by [λ·Y ]χ,χ = Yλχ,λχ . We construct a new matrix Z by averaging Y over this group action:

G

1 | G| λ∈ G

1 | G| λ∈ G

[λ · Y ]χ,χ =

Zχ,χ :=

Yλχ,λχ .

Since the action of λ is by simultaneously permuting rows and columns each λ·Y , and hence Z itself, is positive semideﬁnite with ones on the diagonal. Since we have constructed Z by averaging over a group action, Z is ﬁxed by the action and so satisﬁes Zλχ,λχ = Zχ,χ for all χ,χ ∈ G. Consequently there is some (yχ)χ∈ G such that Zχ,χ = yχχ for all χ,χ ∈ G. It remains to show that if χχ ∈ S then yχχ := Zχ,χ = Yχ,χ := χχ . This holds because if χχ ∈ S then

1 | G| λ∈ G χχ

1 | G| λ∈ G

Zχ,χ =

Yλχ,λχ =

= χχ .

Hence y has all the desired properties, completing the proof. Proof of Theorem 1D. First we show that M(G,S) is a subset of the right-hand-side of (22). To see this observe that the right-hand-side of (21) is certainly contained in the right-hand-size of (22).

| |
|---|


We now establish the reverse inclusion. Suppose ( χ)χ∈S is such that there exists (yχ)χ∈T −1T with yχ = χ for all χ ∈ S, y1

= 1 and MT (y) 0. Let Γ be a chordal cover of Cay( G,S) with Fourier support T . Speciﬁcally Γ has the property that for every maximal clique C of Γ there is χC ∈ G such that χCC ⊆ T .

G

Deﬁne the Γ-partial matrix Yη,η = yηη whenever (η,η ) form an edge of Γ and Yχ,χ = 1 for all χ ∈ G. This is well deﬁned because if (η,η ) is an edge of Γ, then ηη ∈ T −1T . To see this observe that any edge of Γ is contained in a maximal clique C, and so there is some χC ∈ G such that χCη ∈ T and χCη ∈ T . Consequently ηη = χCηχCη ∈ T −1T .

We show that Y [C,C] 0 for all maximal cliques C of the chordal graph Γ. This holds because Y [C,C] = [yηη ]η,η ∈C = [yχ

CηχCη ]η,η ∈C = [yχχ ]χ,χ ∈χ

CC

which, since χCC ⊆ T , is a principal submatrix of the positive semideﬁnite (by assumption) matrix MT (y) = [yχχ ]χ,χ ∈T . By the chordal completion theorem (Theorem 6) we can complete Y to a positive semideﬁnite matrix Y ∈ S G+. The completed matrix has unit diagonal and, whenever χχ ∈ S,

Yχ,χ = yχχ = χχ

where the ﬁrst equality is because the edge set of Γ contains the edge set of Cay( G,S) and the second is from the deﬁnition of y. Hence, by Proposition 5, ( χ)χ∈S ∈ M(G,S), as we require.

| |
|---|


- A.2 Proof of Lemma 1 Proof of Lemma 1. First note that L ∈ Hd+ if and only if L ∈ Hd+ which holds if and only if the block diagonal matrix L0 L0 ∈ H2+d. Conjugating by a unitary matrix we obtain

√ 12I √12I √i2I −√i2I

L 0 0 L

√ 12I √12I √i2I −√i2I

∗

=

Re[L] Im[L] −Im[L] Re[L]

. (31)

We have simply recovered the familiar realization of Hd+ as a section of S2+d, and have not yet used any special properties of L. To complete the proof it remains to carefully choose a 2d × 2d orthogonal matrix Q (depending on J) such that

Q

Re[L] Im[L] −Im[L] Re[L]

QT =

Re[L] − J Im[L] 0 0 Re[L] − J Im[L]

for all L ∈ L.

Observe that J2 = I and JTJ = I imply that J = JT. Since JLJT = L we have that for all L ∈ L,

Re[L] =

L + JLJ 2

and Im[L] =

L − JLJ 2i

. (32)

It follows that for all L ∈ L, Re[L] and Im[L] commute and anti-commute respectively with J, i.e., J Re[L] = Re[L]J and J Im[L] = −Im[L]J. (33) Choosing Q to be the orthogonal matrix Q = √12 − IJ JI we obtain

√ 12I √12J −√12J √12I

Re[L] Im[L] −Im[L] Re[L]

√ 12I √12J −√12J √12I

T

=

Re[L] − J Im[L] 0 0 Re[L] − J Im[L]

.

Clearly this last matrix is positive semideﬁnite if and only if the real symmetric matrix Re[L] − J Im[L] is positive semideﬁnite, completing the proof.

| |
|---|


- A.3 Proof of Proposition 6


- Proof of Proposition 6. The proof proceeds as follows. First we deﬁne a graph Γ and prove that it is a chordal cover of Cay( G,S). We then characterize the maximal cliques of Γ. Finally we show that for any maximal clique C of Γ there is some S ∈ 2[n] such that S C ⊆ T , establishing the stated result. We consider the two cases n/2 even and n/2 odd separately. We describe the argument in detail in the case where


n/2 is even, and just sketch the required modiﬁcations in the case where n/2 is odd.

Assume that n/2 is even. Let Γ be the graph with vertex set 2[n] such that two vertices S,T are adjacent in Γ if and only if either

- • |S| and |T| are both even and ||S| − |T|| ≤ 2 or
- • |S| and |T| are both odd and ||φ(S)| − |φ(T)|| ≤ 2.


Note that just like Cay( G,S), the graph Γ also has two connected components with vertex sets Teven and Todd. Furthermore, φ (deﬁned in Section 4.2) is also an automorphism of Γ that exchanges these two connected components. Observe that if |S T| = 2 (i.e. S and T are adjacent in Cay( G,S)) then both ||S| − |T|| ≤ 2 and ||φ(S)| − |φ(T)|| ≤ 2 hold. Hence if S and T are adjacent in Cay( G,S) they are also adjacent in Γ.

We now show that Γ is a chordal graph. Let the vertices S1,S2,S3,...,Sk form a k-cycle (with k ≥ 4) in Γ such that each of the Si ∈ Teven. Without loss of generality assume that |S1| ≤ |Si| for 1 ≤ i ≤ k. We show that the cycle S1,S2,S3,...,Sk has a chord. If |S2| = |S1| then ||S1|−|S3|| = ||S2|−|S3|| ≤ 2 (since S2 and S3 are adjacent) and so there is a chord between S1 and S3. Otherwise suppose |S2| = |S1|+2. Because

- S1 and Sk are adjacent we see that either |Sk| = |S1| = |S2| − 2 or |Sk| = |S1| + 2 = |S2| and so there is a chord between S2 and Sk. Now suppose S1,S2,S3,...,Sk form a k-cycle (with k ≥ 4) in Γ such that each


of the Si ∈ Todd. Then the image of the cycle under φ is a k-cycle in Γ with vertices in Teven and so it has a chord. Since φ is an automorphism of Γ it follows that S1,S2,S3,...,Sk also has a chord. So Γ is a chordal cover of Cay( G,S).

The subgraphs of Γ induced by the vertex sets Ck := Tk ∪ Tk+2 (for k = 0,2,...,2 n/2 − 2) and the vertex sets φ(Ck) (for k = 0,2,...,2 n/2 − 2) are cliques in Γ. In fact, these are maximal cliques in Γ. To show that each Ck is a maximal clique, suppose S is a vertex that is not in Ck. Then either |S| is odd (in which case S is not adjacent to any element of Ck) or |S| ≤ k − 2 (in which case S is not adjacent to any

- T ∈ Tk+2) or |S| ≥ k + 4 (in which case S is not adjacent to any T ∈ Tk). Hence there is no inclusion-wise larger clique of Γ containing Ck. Since φ is an automorphism of Γ it follows that the φ(Ck) are also maximal cliques of Γ. Finally, there are no other maximal cliques in Γ because every edge of Γ is contained either in Ck or φ(Ck) for some k = 0,2,...,2 n/2 − 2.


It remains to show that for any maximal clique Ck (for k = 0,2,...,2 n/2 − 2) of Γ there is Sk ∈ 2[n] such that Sk Ck ⊆ T . This is suﬃcient to establish that Cay( G,S) has a chordal cover with Fourier support T because for the cliques φ(Ck) we have that φ(Sk) φ(Ck) = Sk Ck ⊆ T . The following gives valid choices of Sk (for k = 0,2,...,2 n/2 − 2).

- • If k ≤ n/2 − 2 then Ck ⊆ T so we can take Sk = ∅.
- • If k ≥ n/2 and n is even then n = 2 n/2 and so n−k−2 ≤ n/2 −2. Hence [n] Ck = Cn−k−2 ⊆ T so we can take Sk = [n].
- • If k ≥ n/2 and n is odd then n = 2 n/2 − 1 and so n − k + 1 ≤ n/2 . Hence φ([n]) Ck = [n] φ(Ck) ⊆ [n] (Tk−1 ∪ Tk+1 ∪ Tk+3) ⊆ Tn−k−3 ∪ Tn−k−1 ∪ Tn−k+1 ⊆ T


so we can take Sk = φ([n]). This completes the argument in the case where n/2 is even.

In the case where n/2 is odd we exchange the roles of the odd and even components in the deﬁnition of Γ and throughout the argument. More precisely, two vertices S,T are adjacent in Γ if and only if either

- • |S| and |T| are both odd and ||S| − |T|| ≤ 2 or
- • |S| and |T| are both even and ||φ(S)| − |φ(T)|| ≤ 2.


It is still the case that Γ is a chordal cover of Cay( G,S). Its maximal cliques are now Ck := Tk ∪ Tk+2 for k = 1,3,...,2 n/2 − 3 together with the φ(Ck). Note that the cliques are now indexed by odd integers. As before, we can choose the Sk (for k = 1,3,...,2 n/2 − 3) to be Sk = ∅ if k ≤ n/2 − 2, Sk = [n] if k ≥ n/2 and n is even, and Sk = φ([n]) if k ≥ n/2 and n is odd. This completes the argument in the case where n/2 is odd.

| |
|---|


#### A.4 Proof of Theorem 9: triangulation of the cycle graph

In this appendix we prove Theorem 9 concerning the triangulation of the cycle graph CN. Theorem 10 below shows how to construct a triangulation of the cycle graph CN+1 on N + 1 nodes, by induction. The triangulation of CN used to obtain Theorem 9 will then be obtained simply by contracting a certain edge of the triangulation of CN+1 (more details below). We thus start by describing a triangulation of the N + 1-cycle.

- Theorem 10 (Triangulation of the cycle graph on N +1 vertices). Let N be an integer greater than or equal


2. Let k1 < ··· < kl be the position of the nonzero digits in the binary expansion of N, i.e., N = li=1 2k

.

i

Let k be the largest integer such that 2k < N (i.e., k = k1 − 1 if N is a power of two and k = kl otherwise). Then there exists a triangulation of the cycle graph on N + 1 nodes CN+1 with frequencies:

 

 

- i
- j=1


T = {0} ∪ {±2i,i = 0,...,k} ∪

2k

,i = 1,...,l − 1

. (34)

j





Proof. The proof of the theorem is by induction on N. Consider the cycle graph on N +1 nodes where nodes are labeled 0,1,...,N. To triangulate the graph, we ﬁrst put an edge between nodes 0 and 2k and another edge between nodes 2k and N, where 2k is the largest power of two that is strictly smaller than N. This is depicted in Figure 7.

0 N

{−2k,0,N − 2k}

(a) (b)

2k

Figure 7. Recursive triangulation of the cycle 0 . . . N on N + 1 vertices

Note that the frequencies used by the triangle {0,2k,N} are equivalent, by translation, to {−2k,0,N−2k}. We now use induction to triangulate the two remaining parts of the cycle (denoted (a) and (b) in Figure 7):

- • For part (a), which is a cycle graph labeled 0...N with N = 2k, the induction hypothesis gives us a

triangulation with frequencies

Ta = {0} ∪ {±2i,i = 0,...,k − 1}. (35)

- • For part (b) of the graph, we use induction on the cycle 2k ...N which is, by translation, equivalent to


the cycle with labels 0...N where N = N − 2k. We distinguish two cases:

- – If N = 2k+1, then we have N = 2k and induction gives a triangulation of (b) with the same frequencies as for part (a). Thus in this case we get a triangulation of the full (N + 1)-cycle with frequencies:

Ta ∪ {−2k,0,2k} = {0} ∪ {±2i,i = 0,...,k} which is what we want.

- – Now assume that N < 2k+1, which means that the most signiﬁcant bit of N is at position k = kl. Thus the binary expansion of N = N − 2k is the same as that of N except that the bit at position


k = kl is replaced with a 0. Let k be the largest integer such that 2k < N . Using induction we get a triangulation of the cycle 0...N using frequencies where

 

 

- i
- j=1


Tb = {0} ∪ {±2i,i = 0,...,k } ∪

2k

,j = 1,...,l − 2

. (36)

j





Combining the triangulation of parts (a) and part (b) we get a triangulation of the (N + 1)-cycle with frequencies

{−2k,0,N − 2k}

∪Ta ∪ Tb.

triangle {0, 2k, N}

Given the expressions (35) and (36) for Ka and Kb, and noting that k ≤ k − 1 and that N − 2k = l−1 j=1 2k

, one can check that the triangulation has frequencies in

j

 

 

- i
- j=1


T = {0} ∪ {±2i,i = 0,...,k} ∪

2k

,i = 1,...,l − 1

.

j





which is exactly what we want.

To complete the proof, it remains to show the base case of the induction. We will show the base cases N = 2 and N = 3. For N = 2, note that the (N + 1)-cycle is simply a triangle which is already triangulated

and the frequencies are simply {−1,0,1}. If we evaluate expression (34) for N = 2 (note that here k = 0) we get T = {−1,0,1}, as needed.

For N = 3 (the 4-cycle), we have k = 1 and l = 2 with k1 = 0 and k2 = 1. Thus expression (34) evaluates to T = {0} ∪ {±1,±2} ∪ {1} = {−2,−1,0,1,2}. It is easy to construct a triangulation of the 4-cycle with such frequencies (one can even construct one where T = K ∪ (−K) = {−1,0,1}).

| |
|---|


Example 8. Figure 8 shows the recursive construction for the case N = 8. We have indicated in each triangle (3-clique) the associated set of frequencies. ♦

2 3

−1,0,1

1

−1,0,1

−2, 0, 2

- 4
- 5


0

−4, 0, 4

−1,

- 0,
- 1


−2, 0, 2

8

−1,0,1

6

7

Figure 8. Illustration of the recursive triangulation of the (N + 1)-cycle for N = 8.

Proof of Theorem 9. To prove Theorem 9 for the N-cycle, we use the triangulation of the (N + 1)-cycle of Theorem 10 except that we regard nodes 0 and N as the same nodes (they collapse into a single one). Thus this means that the triangle in Figure 7 with frequencies {−2k,0,N −2k} also collapses and we only have to look at the frequencies for parts (a) and (b). It is not hard to show that the frequencies we get are the same as those given in Equation (34) except that in the middle term the iterate i goes from 0 to k − 1 (instead of from 0 to k), and in the last term the iterate i goes from 1 to l − 2 (instead of from 1 to l − 1) which gives exactly the set of frequencies of Equation (26).

| |
|---|


Note that there are actually many diﬀerent ways of constructing triangulations for the cycle graph, and diﬀerent constructions will lead to a diﬀerent set of “frequencies”. We can mention that for the cycle graph CN one can actually construct a triangulation where the number of frequencies is related to the logarithm of N base 3. When N is a power of three the frequencies are precisely the powers of 3 that are smaller than N. We omit the precise description of this construction, but Figure 9 shows the triangulation for the 9-cycle and 27-cycle.

8 7 6 9

5

4

10

- 0

- 1

- 2

- 3


- 11

- 12

- 13

- 14

- 15

- 16


2 3

- 0

- 1


- 4

- 5


- 24

- 25

- 26


8

6

7

17

23

18

22

19 20 21

Figure 9. Triangulation of the 9-cycle with frequencies T = {0, ±1, ±3} and of the 27-cycle with frequencies T = {0, ±1, ±3, ±9}.

### References

[AHMR88] Jim Agler, William Helton, Scott McCullough, and Leiba Rodman. Positive semideﬁnite matrices with a given sparsity pattern. Linear algebra and its applications, 107:101–149, 1988. 8

[Bar02] Alexander Barvinok. A course in convexity, volume 54. American Mathematical Society, 2002. 4

[BFMP14] Yuri Bogomolov, Samuel Fiorini, Aleksandr Maksimenko, and Kanstantsin Pashkovich. Small extended formulations for cyclic polytopes. arXiv preprint arXiv:1401.8138, 2014. 5, 25

[BGP14] Grigoriy Blekherman, Joa˜o Gouveia, and James Pfeiﬀer. Sums of squares on the hypercube. arXiv preprint arXiv:1402.4199, 2014. 3

[BPT13] Grigoriy Blekherman, Pablo A. Parrilo, and Rekha R. Thomas. Semideﬁnite optimization and convex algebraic geometry. SIAM, 2013. 2

[Dum07] Bogdan Dumitrescu. Positive trigonometric polynomials and signal processing applications. Springer, 2007. 4

[FGP+14] Hamza Fawzi, Jo˜o Gouveia, Pablo A. Parrilo, Richard Z. Robinson, and Rekha R. Thomas. Positive semideﬁnite rank. arXiv preprint arXiv:1407.4095, 2014. 26

[FKPT13] Samuel Fiorini, Volker Kaibel, Kanstantsin Pashkovich, and Dirk Oliver Theis. Combinatorial bounds on nonnegative rank and extended formulations. Discrete Mathematics, 313(1):67 – 83,

2013. 5, 25

- [FSP13] Hamza Fawzi, James Saunderson, and Pablo A. Parrilo. Equivariant semideﬁnite lifts and sumof-squares hierarchies. arXiv preprint arXiv:1312.6662, 2013. 26
- [FSP14] Hamza Fawzi, James Saunderson, and Pablo A. Parrilo. Equivariant semideﬁnite lifts of regular polygons. arXiv preprint arXiv:1409.4379, 2014. 5, 21, 26


[Gal63] David Gale. Neighborly and cyclic polytopes. In Proceedings of the Seventh Symposium in Pure Mathematics of the American Mathematical Society, volume 7, pages 225–232, 1963. 5, 25

[GJSW84] Robert Grone, Charles R. Johnson, Eduardo M. S´, and Henry Wolkowicz. Positive deﬁnite completions of partial hermitian matrices. Linear algebra and its applications, 58:109–124, 1984. 5, 6, 8, 9

[GPT13] Jo˜o Gouveia, Pablo A. Parrilo, and Rekha R. Thomas. Lifts of convex sets and cone factorizations. Mathematics of Operations Research, 38(2):248–264, 2013. 9

[GT84] Andreas Griewank and Philippe L. Toint. On the existence of convex decompositions of partially separable functions. Mathematical Programming, 28(1):25–49, 1984. 5, 6, 8

[KP11] Volker Kaibel and Kanstantsin Pashkovich. Constructing extended formulations from reﬂection relations. In Integer Programming and Combinatorial Optimization, pages 287–300. Springer,

2011. 25 [Las01] Jean B. Lasserre. Global optimization with polynomials and the problem of moments. SIAM Journal on Optimization, 11(3):796–817, 2001. 10 [Lau03] Monique Laurent. Lower bound for the number of iterations in semideﬁnite hierarchies for the cut polytope. Mathematics of Operations Research, 28(4):871–883, 2003. 3, 4, 5, 18, 20, 26 [Nes00] Yurii Nesterov. Squared functional systems and optimization problems. In High performance optimization, pages 405–440. Springer, 2000. 10 [Par00] Pablo A. Parrilo. Structured Semideﬁnite Programs and Semialgebraic Geometry Methods in Robustness and Optimization. PhD thesis, California Institute of Technology, 2000. 10

[Rud90] Walter Rudin. Fourier Analysis on Groups. John Wiley & Sons, Inc., 1990. 6, 14 [Ter99] Audrey Terras. Fourier analysis on ﬁnite groups and applications. Cambridge University Press,

1999. 6 [Yan91] Mihalis Yannakakis. Expressing combinatorial optimization problems by linear programs. Journal of Computer and System Sciences, 43(3):441–466, 1991. 9 [Zie95] Gu¨nter M. Ziegler. Lectures on polytopes, volume 152. Springer, 1995. 4, 25

