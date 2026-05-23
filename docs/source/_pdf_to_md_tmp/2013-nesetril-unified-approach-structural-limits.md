# arXiv:1303.6471v3[math.CO]22Apr2021

## A Uniﬁed Approach to Structural Limits and Limits of Graphs with Bounded Tree-depth

### Jaroslav Neˇsetˇril Patrice Ossona de Mendez

Author address: Jaroslav Neˇsetril,ˇ Computer Science Institute of Charles Univer-

sity (IUUK and ITI), Malostranske´ nam.25,´ 11800 Praha 1, Czech Republic

Email address: nesetril@iuuk.mff.cuni.cz Patrice Ossona de Mendez, Centre d’Analyse et de Mathematiques´

Sociales (CNRS, UMR 8557), 190-198 avenue de France, 75013 Paris, France

Email address: pom@ehess.fr

## Contents

- Chapter 1. Introduction 1

- 1.1. Main Deﬁnitions and Results 5

Chapter 2. General Theory 11

- 2.1. Limits as Measures on Stone Spaces 11


- Chapter 3. Modelings for Sparse Structures 41

- 3.1. Relational Samples Spaces 41
- 3.2. Modelings 43
- 3.3. Decomposing Sequences: the Comb Structure 65

Chapter 4. Limits of Graphs with Bounded Tree-depth 79

- 4.1. FO1-limits of Colored Rooted Trees with Bounded Height 79


- Chapter 5. Concluding Remarks 105


- 2.2. Convergence, Old and New 20
- 2.3. Combining Fragments 27
- 2.4. Interpretation Schemes 38


- 4.2. FO-limits of Colored Rooted Trees with Bounded Height 95
- 4.3. Limits of Graphs with Bounded Tree-depth 102


- 5.1. Selected Problems 105
- 5.2. Addendum 107 Acknowledgements 108


Bibliography 109

iii

## Abstract

In this paper we introduce a general framework for the study of limits of relational structures and graphs in particular, which is based on a combination of model theory and (functional) analysis. We show how the various approaches to graph limits ﬁt to this framework and that they naturally appear as “tractable cases” of a general theory. As an outcome of this, we provide extensions of known results. We believe that this puts these into a broader context. The second part of the paper is devoted to the study of sparse structures. First, we consider limits of structures with bounded diameter connected components and we prove that in this case the convergence can be “almost” studied component-wise. We also propose the structure of limit objects for convergent sequences of sparse structures. Eventually, we consider the speciﬁc case of limits of colored rooted trees with bounded height and of graphs with bounded tree-depth, motivated by their role as “elementary bricks” these graphs play in decompositions of sparse graphs, and give an explicit construction of a limit object in this case. This limit object is a graph built on a standard probability space with the property that every ﬁrst-order deﬁnable set of tuples is measurable. This is an example of the general concept of modeling we introduce here. Our example is also the ﬁrst “intermediate class” with explicitly deﬁned limit structures where the inverse problem has been solved.

Received by the editor October 20th, 2013. 2010 Mathematics Subject Classiﬁcation. Primary 03C13 (Finite structures), 03C98 (Appli-

cations of model theory), 05C99 (Graph theory), 06E15 (Stone spaces and related structures), Secondary 28C05 (Integration theory via linear functionals).

Key words and phrases. Graph and Relational structure and Graph limits and Structural limits and Radon measures and Stone space and Model theory and First-order logic and Measurable graph.

This paper is part of a project that has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 810115 – Dynasnet).

![image 1](<2013-nesetril-unified-approach-structural-limits_images/imageFile1.png>)

.

iv

CHAPTER 1

## Introduction

To facilitate the study of the asymptotic properties of ﬁnite graphs (and more generally of ﬁnite structures) in a sequence G1,G2,...,Gn,..., it is natural to introduce notions of structural convergence. By structural convergence, we mean that we are interested in the characteristics of a typical vertex (or group of vertices) in the graph Gn, as n grows to inﬁnity. This convergence can be concisely expressed by various means. We note two main directions:

- • the convergence of the sampling distributions;
- • the convergence with respect to a metric in the space of structures (such as the cut metric).


Also, sampling from a limit structure may also be used to deﬁne a sequence convergent to the limit structure.

All these directions lead to a rich theory which originated in a probabilistic context by Aldous [3] and Hoover [48] (see also the monograph of Kallenberg [53] and the survey of Austin [8]) and, independently, in the study of random graph processes, and in analysis of properties of random (and quasirandom) graphs (in turn motivated among others by statistical physics [16, 17, 63]). This development is nicely documented in the recent monograph of Lov´sz [62].

The asymptotic properties of large graphs are studied also in the context of decision problems as exempliﬁed e.g. by structural graphs theory, [26, 80]. However it seems that the existential approach typical for decision problems, structural graph theory and model theory on the one side and the counting approach typical for statistics and probabilistic approach on the other side have little in common and lead to diﬀerent directions: on the one side to study, say, deﬁnability of various classes and the properties of the homomorphism order and on the other side, say, properties of partition functions. It has been repeatedly stated that these two extremes are somehow incompatible and lead to diﬀerent areas of study (see e.g. [15, 46]). In this paper we take a radically diﬀerent approach which uniﬁes these both extremes.

We propose here a model which is a mixture of the analytic, model theoretic and algebraic approach. It is also a mixture of existential and probabilistic approach. Precisely, our approach is based on the Stone pairing φ,G of a ﬁrst-order formula φ (with set of free variables Fv(φ)) and a graph G, which is deﬁned by the following expression

φ,G = |{(v1,...,v|Fv(φ)|) ∈ G|Fv(φ)| : G |= φ(v1,...,v|Fv(φ)|)}| |G||Fv(φ)|

.

Stone pairing induces a notion of convergence: a sequence of graphs (Gn)n∈N is FO-convergent if, for every ﬁrst order formula φ (in the language of graphs), the values φ,Gn converge as n → ∞. In other words, (Gn)n∈N is FO-convergent if the 1

probability that a formula φ is satisﬁed by the graph Gn with a random assignment of vertices of Gn to the free variables of φ converges as n grows to inﬁnity. We also consider analogously deﬁned X-convergence, where X is a fragment of FO.

Our main result is that this model of FO-convergence is a suitable model for the analysis of limits of sparse graphs (and particularly of graphs with bounded tree depth). This ﬁts to a broad context of recent research.

For graphs, and more generally for ﬁnite structures, there is a class dichotomy: nowhere dense and somewhere dense [78, 74]. Each class of graphs falls in one of these two categories. Somewhere dense class C may be characterised by saying that there exists a (primitive positive) FO interpretation of all graphs into them. Such class C is inherently a class of dense graphs. In the theory of nowhere dense structures [80] there are two extreme conditions related to sparsity: bounded degree and bounded diameter. Limits of bounded degree graphs have been studied thoroughly [10], and this setting has been partially extended to sparse graphs with far away large degree vertices [65]. The class of graphs with bounded diameter is considered in Section 3.3 (and leads to a diﬃcult analysis of componentwise convergence). This analysis provides a ﬁrst-step for the study of limits of graphs with bounded treedepth. Classes of graphs with bounded tree-depth can be deﬁned by logical terms as well as combinatorially in various ways; the most concise deﬁnition is perhaps

- that a class of graphs has bounded tree depth if and only if the maximal length of a path in every G in the class is bounded by a constant. Graphs with bounded tree-depth play also the role of building blocks of graphs in a nowhere dense class (by means of low tree-depth decompositions [68, 69, 80]). So the solution of limits for graphs with bounded tree depth presents a step (and perhaps provides a road map) in solving the limit problem for sparse graphs.


We propose here a new type of measurable structure, called modeling, which extends the notion of graphing, and which we believe is a good candidate for limit objects of sequence of graphs in a nowhere dense class. The convergence of graphs with bounded tree depth is analysed in detail and this leads to a construction of a modeling limits for those sequences of graphs where all members of the sequence have uniformly bounded tree depth (see Theorem 4.36). Moreover, we characterize modelings which are limits of graphs with bounded tree-depth.

There is more to this than meets the eye: We prove that if C is a monotone class of graphs such that every FO-convergent sequence has a modeling limit then the class C is nowhere dense (see Theorem 1.8). This shows the natural limitations to modeling FO-limits. To create a proper model for bounded height trees we have to introduce the model in a greater generality and it appeared that our approach relates and in most cases generalizes, by properly choosing a fragment X of FO, all existing models of graph limits. For instance, for the fragment X of all existential ﬁrst-order formulas, X-convergence means that the probability that a structure has a particular extension property converges. Our approach is encouraged by the deep connections to the four notions of convergence which have been proposed to study graph limits in diﬀerent contexts.

The ultimate goal of the study of structural limits is to provide (as eﬀectively as possible) limit objects themselves: we would like to ﬁnd an object which will induce the limit distribution and encode the convergence.

For dense graphs Lov´sz and Szegedy managed to unveil the essential notion of a graphon, which exactly ﬁts their notion of convergence: In this representation

1. INTRODUCTION 3

the limit [63, 16] is a symmetric Lebesgue measurable function W : [0,1]2 → [0,1] called a graphon and every graphon is the limit of a sequence of graphs. Such a representation is of course not unique, in the sense that diﬀerent graphons may deﬁne the same graph limit, but equivalence of graphons is well understood [13, 25]. A connection between graph limits and de Finetti’s theorem for exchangeable arrays (and the early works of Aldous [3], Hoover [48] and Kallenberg [53]) has been established, see e.g. Diaconis and Janson [25]. Note that representation of graph limits by graphons extend (in a non-trivial way) to regular hypergraphs [32, 91] and, more generally, to relational structures [6, 7].

A representation of the limit for our second example of bounded degree graphs is a measurable graphing (notion introduced by Adams [1] in the context of Ergodic theory), that is a standard Borel space with a measure µ and d measure preserving Borel involutions. The existence of such a representation has been made explicit by Elek [31], and relies on the works of Benjamini [10] and Gaboriau [38]. Graphing representation is not unique, but the equivalence of graphings (called local equivalence) can be characterized by means of bi-local isomorphism [62]. However, it is a diﬃcult open problem, known as Aldous–Lyons conjecture, whether every graphing is the limit of some sequence of ﬁnite graphs (see Conjecture 1.2).

Both of these models of convergence are particular cases of our general approach. One of the main issue of our general approach is to determine a representation of FO-limits as measurable graphs. A natural limit object is a standard probability space (V,Σ,µ) together with a graph with vertex set V and edge set

- E, with the property that every ﬁrst-order deﬁnable subset of a power of V is measurable. This leads to the notion of relational sample space and to the notion of modeling. This notion seems to be particularly suitable for sparse graphs (and in the full generality only for sparse graphs, see Theorem 1.8). We shall see that modelings inherit most of the nice properties of graphings and that open problems on graphings can be generalized to open problems on modelings (in particular the Aldous–Lyons conjecture mentioned above). It is open which type of limit object could be considered for the general (sparse and dense) case, which would generalize graphons and graphings.


In this paper, we shed a new light on all these constructions by an approach inspired by functional analysis. The preliminary material and our framework are introduced in Sections 1.1 and 2.1. The general approach presented in the ﬁrst sections of this paper leads to several new results. Let us mention a sample of such results.

Central to the theory of graph limits stand random graphs (in the Erd˝s-R´enyi model, where each edge is present with a given probability p, independently of the other edges [33]): a sequence of random graphs with increasingly many vertices and ﬁxed edge probability 0 < p < 1 is almost surely convergent to the constant graphon p [63]. On the other hand, it follows from the work of Erd˝s and R´enyi [34] and the work of Glebskii, Kogan, Liagonkii and Talanov [42], Fagin [35] that such a sequence is almost surely elementarily convergent to an ultra-homogeneous graph, called the Rado graph. We prove that these two facts — elementary convergence to the Rado graph and convergence to a constant graphon — together with the quantiﬁer elimination property of ultra-homogeneous graphs, imply that a sequence of random graphs with increasing order and ﬁxed edge probability 0 < p < 1 is

almost surely FO-convergent, see Section 2.3.4. (However, we know that this limit cannot be either a random-free graphon or a modeling, see Theorem 1.8)

We shall prove that a sequence of bounded degree graphs (Gn)n∈N with |Gn| → ∞ is FO-convergent if and only if it is both convergent in the sense of BenjaminiSchramm and in the sense of elementary convergence. The limit can still be represented by a graphing, see Sections 2.2.2 and 3.2.6.

For the general case we prove that the limit of an FO-convergent sequence of graphs is a probability measure on the Stone space of the Boolean algebra of ﬁrstorder formulas, which is invariant under the action of the symmetric group Sω on this space, see Section 2.1. This representation theorem holds generally and it is the basis of our approach. Fine interplay of these notions is depicted on Table 1.

Boolean algebra B(X) Stone Space S(B(X))

|Formula φ|Continuous function fφ<br><br>|
|---|---|
|Vertex v|“Type” of vertices T|
|Graph G<br><br>|statistics of types =probability measure µG|
|φ,G<br><br>|fφ(T) dµG(T)|
|X-convergent (Gn)<br><br>|weakly convergent µG<br><br>n|
|Γ = Aut(B(X))<br><br>|Γ-invariant measure|


Table 1. Some correspondences

Graph limits (in the sense of Lov´sz et al.) — and more generally hypergraph limits — have been studied by Elek and Szegedy [32] through the introduction of a measure on the ultraproduct of the graphs in the sequence (via Loeb measure construction, see [59]). The fundamental theorem of ultraproducts proved by  Lo´s [60] implies that the ultralimit of a sequence of graphs is (as a measurable graph) an FO-limit. Thus in this non-standard setting we get FO-limits (almost) for free see [79]. However this very general construction has several major drawbacks in an analytical context: it involves countably many measures (which are not simply product measures) and non-separable sigma algebras, while major tools from analysis rely on Borel product measures on standard Borel spaces (like for graphings).

We believe that the approach taken in this paper is natural and that it enriches the existing notions of limits by several natural notions of X-convergence (such as elementary, quantiﬁer-free, and local convergences), and gives the whole area a new perspective, which we explain in the next section. In a sense we proceed dually to homomorphism counting (see e.g. [15, 62]). We do not view φ,G as a “φ test” for G but rather as a “G test” for φ: A graph deﬁnes an operator on the Boolean algebra of all FO-formulas (or on the sub-algebra induced by a fragment X ⊂ FO).

It also presents a promising approach to more general intermediate classes (see the ﬁnal comments).

###### 1.1. Main Deﬁnitions and Results

If we consider relational structures with signature λ, the symbols of the relations and constants in λ deﬁne the non-logical symbols of the vocabulary of the ﬁrstorder language FO(λ) associated to λ-structures. Notice that if λ is countable then FO(λ) is countable. The symbols of variables will be assumed to be taken from a countable set {x1,...,xn,...} indexed by N. Let u1,...,uk be terms. The set of used free variables of a formula φ will be denoted by Fv(φ) (by saying that a variable xi is “used” in φ we mean that φ is not logically equivalent to a formula in which xi does not appear). The formula φx

i1,...,xik(u1,...,uk) denotes the formula obtained by substituting simultaneously the term uj to the free occurrences of xi

j

for j = 1,...,k. In the sake of simplicity, we will denote by φ(u1,...,uk) the substitution φx

1,...,xk(u1,...,uk).

A relational structure A with signature λ is deﬁned by its domain (or universe) A and relations with names and arities as deﬁned in λ. In the following we will denote relational structures by bold face letters A,B,... and their domains by the corresponding light face letters A,B,...

The key to our approach are the following two deﬁnitions.

Definition 1.1 (Stone pairing). Let λ be a signature, let φ ∈ FO(λ) be a ﬁrst-order formula with free variables x1,...,xp and let A be a ﬁnite λ-structure.

Put

Ωφ(A) = {(v1,...,vp) ∈ Ap : A |= φ(v1,...,vp)}. We deﬁne the Stone pairing of φ and A by

- (1.1) φ,A = |Ωφ(A)| |A|p


.

In other words, φ,A is the probability that φ is satisﬁed in A when we interpret the p free variables of φ by p vertices of G chosen randomly, uniformly and independently. Also, Ωφ(A) is interpreted as the solution set of φ in A.

Note that in the case of a sentence φ (that is a formula with no free variables, thus p = 0), the deﬁnition of the Stone pairing reduces to

φ,A =

1, if A |= φ; 0, otherwise.

Definition 1.2 (FO-convergence). A sequence (An)n∈N of ﬁnite λ-structures is FO-convergent if, for every formula φ ∈ FO(λ) the sequence ( φ,An )n∈N is (Cauchy) convergent.

In other words, a sequence (An)n∈N is FO-convergent if the sequence of mappings  ·,An : FO(λ) → [0,1] is pointwise-convergent.

The interpretation of the Stone pairing as a probability suggests to extend this view to more general λ-structures which will be our candidates for limit objects.

Definition 1.3 (Relational sample space). A relational sample space is a relational structure A (with signature λ) with extra structure: The domain A of A of a sample model is a standard Borel space (with Borel σ-algebra ΣA) with the property that every subset of Ap that is ﬁrst-order deﬁnable in FO(λ) is measurable (in Ap with respect to the product σ-algebra). For brevity we shall use the same letter A for structure and relational sample space.

In other words, if A is a relational sample space then for every integer p and every φ ∈ FO(λ) with p free variables it holds that Ωφ(A) ∈ ΣpA.

Definition 1.4 (Modeling). A modeling A is a relational sample space A equipped with a probability measure (denoted νA). By the abuse of symbols the modeling will be denoted by A (with σ-algebra ΣA and corresponding measure νA). A modeling with signature λ is a λ-modeling.

Remark 1.5. We take time for some comments on the above deﬁnitions:

- • According to Kuratowski’s isomorphism theorem, the domains of relational sample spaces are Borel-isomorphic to either R, Z, or a ﬁnite space.
- • Borel graphs (in the sense of Kechris et al. [55]) are generally not modelings (in our sense) as Borel graphs are only required to have a measurable adjacency relation.
- • By equipping its domain with the discrete σ-algebra, every ﬁnite λ-structure deﬁnes a relational sample space. Considering the uniform probability measure on this space then canonically deﬁnes a uniform modeling.
- • It follows immediately from Deﬁnition 1.3 that any k-rooting of a relational sample space is a relational sample space.


We can extend the deﬁnition of Stone pairing from ﬁnite structures to modelings as follows.

Definition 1.6 (Stone pairing for modeling). Let λ be a signature, let φ ∈ FO(λ) be a ﬁrst-order formula with free variables x1,...,xp and let A be a λmodeling.

We can deﬁne the Stone pairing of φ and A by

φ(A)(x)dνAp (x).

- (1.2) φ,A =


1Ω

x∈Ap

Note that the deﬁnition of a modeling is simply tailored to make the expression (1.2) meaningful. Based on this deﬁnition, modelings can sometimes be used as a representation of the limit of an FO-convergent sequence of ﬁnite λ-structures.

Definition 1.7. A modeling L is a modeling FO-limit of an FO-convergent sequence (An)n∈N of ﬁnite λ-structures if φ,An converges pointwise to φ,L for every ﬁrst order formula φ.

As we shall see in Lemma 3.8, a modeling FO-limit of an FO-convergent sequence (An)n∈N of ﬁnite λ-structures is necessarily weakly uniform (meaning that

all the singletons of the limit have the same measure). It follows that if a modeling L is a modeling FO-limit then L is either ﬁnite or uncountable.

We shall see that not every FO-convergent sequence of ﬁnite relational structures admits a modeling FO-limit. In particular we prove (see Theorem 3.39):

Theorem 1.8. Let C be a monotone class of ﬁnite graphs, such that every FOconvergent sequence of graphs in C has a modeling FO-limit. Then the class C is nowhere dense.

Recall that a class of graphs is monotone if it is closed under the operation of taking a subgraph, and that a monotone class of graphs C is nowhere dense if, for every integer p, there exists an integer N(p) such that the p-th subdivision of the complete graph KN(p) on N(p) vertices does not belong to C (see [74, 78, 80]).

However, we conjecture that the theorem above expresses exactly when modeling FO-limits exist:

Conjecture 1.1. If (Gn)n∈N is an FO-convergent sequence of graphs and if {Gn : n ∈ N} is a nowhere dense class, then the sequence (Gn)n∈N has a modeling FO-limit.

As a ﬁrst step, we prove that modeling FO-limits exist in two particular cases, which form in a certain sense the building blocks of nowhere dense classes.

Theorem 1.9. Let C be a integer.

- (1) Every FO-convergent sequence of graphs with maximum degree at most C has a modeling FO-limit;
- (2) Every FO-convergent sequence of rooted trees with height at most C has a modeling FO-limit.


The ﬁrst item will be derived from the graphing representation of limits of Benjamini-Schramm convergent sequences of graphs with bounded maximum degree with no major diﬃculties. Recall that a graphing [1] is a Borel graph G such that the following Intrinsic Mass Transport Principle (IMTP) holds:

∀A,B

degB(x)dx =

degA(y)dy,

A

B

where the quantiﬁcation is on all measurable subsets of vertices, and where degB(x) (resp. degA(y)) denotes the degree in B (resp. in A) of the vertex x (resp. of the vertex y). In other words, the Mass Transport Principle states that if we count the edges between sets A and B by summing up the degrees in B of vertices in A or by summing up the degrees in A of vertices in B, we should get the same result.

Theorem 1.10 (Elek [31]). The Benjamini-Schramm limit of a bounded degree graph sequence can be represented by a graphing.

A full characterization of the limit objects in this case is not known, and is related to the following conjecture.

Conjecture 1.2 (Aldous, Lyons [5]). Every graphing is the BenjaminiSchramm limit of a bounded degree graph sequence.

Equivalently, every unimodular distribution on rooted countable graphs with bounded degree is the Benjamini-Schramm limit of a bounded degree graph sequence.

We conjecture that a similar condition could characterize modeling FO-limits of sequences of graphs with bounded degree. In this more general setting, we have to add a new condition, namely to have the ﬁnite model property. Recall that an inﬁnite structure L has the ﬁnite model property if every sentence satisﬁed by L has a ﬁnite model.

Conjecture 1.3. A modeling is the Benjamini-Schramm limit of a bounded degree graph sequence if and only if it is a graph with bounded degree, is weakly uniform, it satisﬁes both the Intrinsic Mass Transport Principle, and it has the ﬁnite model property.

When handling inﬁnite degrees, we do not expect to be able to keep the Intrinsic Mass Transport Principle as is. If a sequence of ﬁnite graphs is FO-convergent to some modeling L then we require the following condition to hold, which we call Finitary Mass Transport Principle (FMTP):

For every measurable subsets of vertices A and B, if it holds that degB(x) ≥ a for every x ∈ A and degA(y) ≤ b for every y ∈ B then aνL(A) ≤ bνL(B).

Note that in the case of modelings with bounded degrees, the Finitary Mass Transport Principle is equivalent to the Intrinsic Mass Transport Principle. Also note that the above equation holds necessarily when A and B are ﬁrst-order deﬁnable, according to the convergence of the Stone pairings and the fact that the Finitary Mass Transport Principle obviously holds for ﬁnite graphs.

The second item of Theorem 1.9 will be quite diﬃcult to establish and is the main result of this paper. We formulate it together with the inverse theorem as follows:

Theorem 1.11. Every sequence of ﬁnite rooted colored trees with height at most C has a modeling FO-limit that is a rooted colored tree with height at most C, is weakly uniform, and satisﬁes the Finitary Mass Transport Principle.

Conversely, every rooted colored tree modeling with height at most C that satisﬁes the Finitary Mass Transport Principle is the FO-limit of a sequence of ﬁnite rooted colored trees.

By Theorem 1.8, modeling FO-limits do not exist in general. However, we have

- a general representation of the limit of an FO-convergent sequence of λ-structures


by means of a probability distribution on a compact Polish space Sλ deﬁned from FO(λ) using Stone duality:

Theorem 1.12. Let λ be a ﬁxed (possibly ﬁnite) countable signature. Then there exist two mappings A  → µA and φ  → K(φ) such that

- • A  → µA is an injective mapping from the class of ﬁnite λ-structures to the space of regular probability measures on Sλ,
- • φ  → K(φ) is a mapping from FO(λ) to the set of the clopen subsets of Sλ,


such that for every ﬁnite λ-structure A and every ﬁrst-order formula φ ∈ FO(λ) the following equation holds:

φ,A =

1K(φ) dµA.

Sλ

(To prevent risks of notational ambiguity, we shall use µ as root symbol for measures on Stone spaces and keep ν for measures on modelings.)

Consider an FO-convergent sequence (An)n∈N. Then the pointwise convergence of  ·,An translates as a weak ∗-convergence of the measures µA

and we get:

n

Theorem 1.13. A sequence (An)n∈N of ﬁnite λ-structures is FO-convergent if and only if the sequence (µA

)n∈N is weakly ∗-convergent. Moreover, if µA

n

n ⇒ µ then for every ﬁrst-order formula φ ∈ FO(λ) the following equation holds:

1K(φ) dµ = lim

φ,An .

n→∞

Sλ

These last two Theorems are established in the next section as a warm up for our general theory.

CHAPTER 2

## General Theory

###### 2.1. Limits as Measures on Stone Spaces

In order to prove the representation theorems Theorem 1.12 and Theorem 1.13, we ﬁrst need to prove a general representation for additive functions on Boolean algebras.

2.1.1. Representation of Additive Functions. Recall that a Boolean algebra B = (B,∧,∨,¬,0,1) is an algebra with two binary operations ∨ and ∧, a unary operation ¬ and two elements 0 and 1, such that (B,∨,∧) is a complemented distributive lattice with minimum 0 and maximum 1. The two-elements Boolean algebra is denoted 2.

To a Boolean algebra B is associated a topological space, denoted S(B), whose points are the ultraﬁlters on B (or equivalently the homomorphisms B → 2). The topology on S(B) is generated by a sub-basis consisting of all sets

KB(b) = {x ∈ S(B) : b ∈ x}, where b ∈ B. When the considered Boolean algebra will be clear from context we shall omit the subscript and write K(b) instead of KB(b).

A topological space is a Stone space if it is Hausdorﬀ, compact, and has a basis of clopen subsets. Boolean algebras and Stone spaces are equivalent as formalized by Stone representation theorem [89], which states (in the language of category theory) that there is a duality between the category of Boolean algebras (with homomorphisms) and the category of Stone spaces (with continuous functions). This justiﬁes calling S(B) the Stone space of the Boolean algebra B. The two contravariant functors deﬁning this duality are denoted by S and Ω and deﬁned as follows:

For every homomorphism h : A → B between two Boolean algebra, we deﬁne the map S(h) : S(B) → S(A) by S(h)(g) = g◦h (where points of S(B) are identiﬁed with homomorphisms g : B → 2). Then for every homomorphism h : A → B, the map S(h) : S(B) → S(A) is a continuous function.

Conversely, for every continuous function f : X → Y between two Stone spaces, deﬁne the map Ω(f) : Ω(Y ) → Ω(X) by Ω(f)(U) = f−1(U) (where elements of Ω(X) are identiﬁed with clopen sets of X). Then for every continuous function f : X → Y , the map Ω(f) : Ω(Y ) → Ω(X) is a homomorphism of Boolean algebras.

We denote by K = Ω ◦ S one of the two natural isomorphisms deﬁned by the duality. Hence, for a Boolean algebra B, K(B) is the set algebra {KB(b) : b ∈ B}, and this algebra is isomorphic to B.

An ultraﬁlter of a Boolean algebra B can be considered as a ﬁnitely additive measure, for which every subset has either measure 0 or 1. Because of the equivalence of the notions of Boolean algebra and of set algebra, we deﬁne the space

11

ba(B) as the space of all bounded additive functions f : B → R. Recall that a function f : B → R is additive if for all x,y ∈ B the following implication holds

x ∧ y = 0 =⇒ f(x ∨ y) = f(x) + f(y). The space ba(B) is a Banach space for the norm

f(x) − inf

f ba(B) = sup x∈B

f(x).

x∈B

(Recall that the ba space of an algebra of sets Σ is the Banach space consisting of all bounded and ﬁnitely additive measures on Σ with the total variation norm.)

Let V (B) be the normed vector space (of so-called simple functions) generated by the indicator functions of the clopen sets (equipped with supremum norm). The indicator function of the clopen set K(b) (for some b ∈ B) is denoted by 1K(b).

Lemma 2.1. The space ba(B) is the topological dual of V (B). Proof. One can identify ba(B) with the space ba(K(B)) of ﬁnitely additive

measures deﬁned on the set algebra K(B). As a vector space, ba(B) ≈ ba(K(B)) is then clearly the (algebraic) dual of the normed vector space V (B).

The pairing of a function f ∈ ba(B) and a vector X = ni=1 ai1K(b

i) is deﬁned by

n

[f,X] =

aif(bi).

i=1

That [f,X] does not depend on a particular choice of a decomposition of X follows from the additivity of f. We include a short proof for completeness: Assume

i). As for every b,b ∈ B it holds that f(b) = f(b ∧ j α j1K(b

i αi1K(b

i) = i βi1K(b

- b ) + f(b ∧ ¬b ) and 1K(b) = 1K(b∧b ) + 1K(b∧¬b ) we can express the two sums as


j) (where b i ∧ b j = 0 for every i = j), with i αif(bi) = j α jf(b j) and i βif(bi) = j β jf(b j). As b i ∧ b j = 0 for every i = j, for

j) = j β j1K(b

- x ∈ K(b j) it holds that α j = X(x) = β j. Hence α j = β j for every j. Thus


i αif(bi) = i βif(bi).

Note that X  → [f,X] is indeed continuous. Thus ba(B) is the topological dual of V (B).

Lemma 2.2. The vector space V (B) is dense in C(S(B)) (with the uniform norm).

Proof. Let f ∈ C(S(B)) and let > 0. For z ∈ f(S(B)) let Uz be the preimage by f of the open ball B /2(z) of R centered in z. As f is continuous, Uz is a open set of S(B). As {K(b) : b ∈ B} is a basis of the topology of S(B), Uz can be expressed as a union b∈F(U

z) K(b) is a covering of S(B) by open sets. As S(B) is compact, there exists a ﬁnite subset

z) K(b). It follows that z∈f(S(B)) b∈F(U

- F of z∈f(S(B)) F(Uz) that covers S(B). Moreover, as for every b,b ∈ B it holds that K(b) ∩ K(b ) = K(b ∧ b ) and K(b) \ K(b ) = K(b ∧ ¬b ) it follows that we can assume that there exists a ﬁnite family F such that S(B) is covered by open sets K(b) (for b ∈ F ) and such that for every b ∈ F there exists b ∈ F such that K(b) ⊆ K(b ). In particular, it follows that for every b ∈ F , f(K(b)) is included in an open ball of radius  /2 of R. For each b ∈ F choose a point xb ∈ S(B) such


- that b ∈ xb. Now deﬁne fˆ=


f(xb)1K(b)

b∈F

Let x ∈ S(B). Then there exists b ∈ F such that x ∈ K(b). Thus

|f(x) − fˆ(x)| = |f(x) − f(xb)| <  . Hence f − fˆ ∞ < .

Lemma 2.3. Let B be a Boolean algebra, let ba(B) be the Banach space of

bounded additive real-valued functions equipped with the norm f = supb∈B f(b)− infb∈B f(b), let S(B) be the Stone space associated to B by the Stone representation theorem, and let rca(S(B)) be the Banach space of the regular countably additive measure on S(B) equipped with the total variation norm.

Then the mapping CK : rca(S(B)) → ba(B) deﬁned by CK(µ) = µ ◦ K is an isometric isomorphism. In other words, CK is deﬁned by

CK(µ)(b) = µ({x ∈ S(B) : b ∈ x}) (considering that the points of S(B) are the ultraﬁlters on B).

Proof. According to Lemma 2.1, the Banach space ba(B) is the topological dual of V (B) and as V (B) is dense in C(S(B)) (according to Lemma 2.2) we deduce that ba(B) can be identiﬁed with the continuous dual of C(S(B)). By Riesz representation theorem, the topological dual of C(S(B)) is the space rca(S(B)) of regular countably additive measures on S(B). From these observations follows the equivalence of ba(B) and rca(S(B)).

This equivalence is easily made explicit, leading to the conclusion that the mapping CK : rca(S(B)) → ba(B) deﬁned by CK(µ) = µ ◦ K is an isometric isomorphism.

Note also that, similarly, the restriction of CK to the space Pr(S(B)) of all (regular) probability measures on S(B) is an isometric isomorphism of Pr(S(B)) and the subset ba1(B) of ba(B) of all non-negative additive functions f on B such that f(1) = 1.

Recall that given a measurable function f : X → Y (where X and Y are measurable spaces), the pushforward f∗(µ) of a measure µ on X is the measure on Y deﬁned by f∗(µ)(A) = µ(f−1(A)) (for every measurable set A of Y ). Note that if f is a continuous function and if µ is a regular measure on X, then the pushforward measure f∗(µ) is a regular measure on Y . By similarity with the deﬁnition of Ω(f) : Ω(Y ) → Ω(X) (see above deﬁnition) we denote by Ω∗(f) the mapping from rca(X) to rca(Y ) deﬁned by (Ω∗(f))(µ) = f∗(µ).

All the functors deﬁned above are consistent in the sense that if h : A → B is a homomorphism and f ∈ ba(B) then

Ω∗(S(h))(µf) ◦ KA = f ◦ h.

A standard notion of convergence in rca(S(B)) (as the continuous dual of C(S(B))) is the weak ∗-convergence: a sequence (µn)n∈N of measures is convergent if, for every f ∈ C(S(B)) the sequence f(x)dµn(x) is convergent. Thanks to the density of V (B) this convergence translates as pointwise convergence in ba(B) as follows: a sequence (gn)n∈N of functions in ba(B) is convergent if, for every b ∈ B the sequence (gn(b))n∈N is convergent. As rca(S(B)) is complete, so is rca(B). Moreover, it is easily checked that ba1(B) is closed in ba(B).

###### In a more concise way, we can write, for a sequence (fn)n∈N of functions in ba(B) and for the corresponding sequence (µf

)n∈N of regular measures on S(B): fn → f pointwise ⇐⇒ µf

n

n ⇒ µf. We now apply this classical machinery to structures and models.

2.1.2. Basics of Model Theory and Lindenbaum–Tarski Algebras. We denote by B(FO(λ)) the equivalence classes of FO(λ) deﬁned by logical equivalence. The (class of) unsatisﬁable formulas (resp. of tautologies) will be designated by 0 (resp. 1). Then, B(FO(λ)) gets a natural structure of Boolean algebra (with minimum 0, maximum 1, inﬁmum ∧, supremum ∨, and complement ¬). This algebra is called the Lindenbaum–Tarski algebra of FO(λ). Notice that all the Boolean algebras FO(λ) for countable λ are isomorphic, as there exists only one countable atomless Boolean algebra up to isomorphism (see [47]).

For an integer p ≥ 1, the fragment FOp(λ) of FO(λ) contains ﬁrst-order formulas φ such that Fv(φ) ⊆ {x1,...,xp}. The fragment FO0(λ) of FO(λ) contains ﬁrst-order formulas without free variables (that is sentences).

We check that the permutation group Sp on [p] acts on FOp(λ) by σ · φ = φ(xσ(1),...,xσ(p)) and that each permutation indeed deﬁne an automorphism of B(FOp(λ)). Similarly, the group Sω of permutations on N acts on FO(λ) and B(FO(λ)). Note that FO0(λ) ⊆ ··· ⊆ FOp(λ) ⊆ FOp+1(λ) ⊆ ··· ⊆ FO(λ). Conversely, let rank(φ) = max{i : xi ∈ Fv(φ)}. Then we have a natural projection πp : FO(λ) → FOp(λ) deﬁned by

φ if rank(φ) ≤ p ∃xp+1 ∃xp+2 ... ∃xrank(φ) φ otherwise

πp(φ) =

An elementary class (or axiomatizable class) C of λ-structures is a class consisting of all λ-structures satisfying a ﬁxed consistent ﬁrst-order theory TC. Denoting by IT

the ideal of all ﬁrst-order formulas in L that are provably false from axioms in TC, The Lindenbaum–Tarski algebra B(FO(λ),TC) associated to the theory TC of C is the quotient Boolean algebra B(FO(λ),TC) = B(FO(λ))/IT

C

. As a set, B(FO(λ),TC) is simply the quotient of FO(λ) by logical equivalence modulo TC.

C

As we consider countable languages, TC is at most countable and it is easily checked that S(B(FO(λ),TC)) is homeomorphic to the compact subspace of S(B(FO(λ))) deﬁned as {T ∈ S(B(FO(λ))) : T ⊇ TC}. Note that, for instance, S(B(FO0(λ),TC)) is a clopen set of S(B(FO0(λ))) if and only if C is ﬁnitely axiomatizable (or a basic elementary class), that is if TC can be chosen to be a single sentence. These explicit correspondences are particularly useful to our setting.

2.1.3. Stone Pairing Again. We add a few comments to Deﬁnition 1.6. Note ﬁrst that this deﬁnition is consistent in the sense that for every modeling A and for every formula φ ∈ FO(λ) with p free variables can be considered as a formula with q ≥ p free variables with q − p unused variables, we have

φ(A)(x)dνAq (x) =

φ(A)(x)dνAp (x).

1Ω

1Ω

Aq

Ap

It is immediate that for every formula φ it holds that  ¬φ,A = 1 − φ,A . Moreover, if φ1,...,φn are formulas, then by de Moivre’s formula, the following equation holds:

n

n

k

(−1)k+1

φi,A =

φi

###### ,A .

j

1≤i1<···<ik≤n

i=1

j=1

k=1

In particular, if φ1,...,φk are mutually exclusive (meaning that φi ∧ φj = 0) then the following equation holds:

k

k

φi,A =

φi,A .

i=1

i=1

It follows that for every ﬁxed modeling A, the mapping φ  → φ,A is additive (i.e.  ·,A ∈ ba(B(FO(λ)))):

φ1 ∧ φ2 = 0 =⇒ φ1 ∨ φ2,A = φ1,A + φ2,A . The Stone pairing is antimonotone: Let φ,ψ ∈ FO(λ). For every modeling A the following implication holds:

φ ψ =⇒ φ,G ≥ ψ,G .

However, even if φ and ψ are sentences and φ, ·  ≥ ψ, ·  on ﬁnite λ-structures, this does not imply in general that φ ψ: let θ be a sentence with only inﬁnite models and let φ be a sentence with only ﬁnite models. On ﬁnite λ-structures it holds that φ ∨ θ, ·  = φ, ·  although φ ∨ θ φ (as witnessed by an inﬁnite model of θ).

Nevertheless, inequalities between Stone pairing that are valid for ﬁnite λstructures will of course still hold at the limit. For instance, for φ1,φ2 ∈ FO1(λ), for ζ ∈ FO2(λ), and for a,b ∈ N deﬁne the ﬁrst-order sentence B(a,b,φ1,φ2,ζ) expressing that for every vertex x such that φ1(x) holds there exist at least a vertices y such that φ2(y) ∧ ζ(x,y) holds and that for every vertex y such that φ2(x) holds there exist at most b vertices x such that φ1(x)∧ζ(x,y) holds. Then it is easily checked that for every ﬁnite λ-structure A the following implication holds:

A |= B(a,b,φ1,φ2,ζ) =⇒ a φ1,A ≤ b φ2,A . For example, if a ﬁnite directed graph is such that every arc connects a vertex with out-degree 2 to a vertex with in-degree 1, it is clear that the probability that a random vertex has out-degree 2 is half the probability that a random vertex has in-degree 1.

Now we come to important twist and the basic of our approach. The Stone pairing  ·, ·  can be considered from both sides: On the right side the functions of type φ, ·  are a generalization of the homomorphism density functions [15]:

t(F,G) = |hom(F,G)| |G||F|

(these functions correspond to φ,G for Boolean conjunctive queries φ and a graph G). Also the density function used in [10] to measure the probability that the ball of radius r rooted at a random vertex as a given isomorphism type may be expressed as a function φ, · . Note again that we follow here, in a sense, a dual approach: we consider for ﬁxed A the function  ·,A , which is an additive function on B(FO(λ)) with the following properties:

- •  ·,A ≥ 0 and 1,A = 1;


- • σ · φ,A = φ,A for every σ ∈ Sω;
- • if Fv(φ) ∩ Fv(ψ) = ∅, then φ ∧ ψ,A = φ,A ψ,A .


Thus  ·,A is, for a given A, an operator on the class of ﬁrst-order formulas. We now can apply Lemma 2.3 to derive a representation by means of a regular

measure on a Stone space. The ﬁne structure and interplay of additive functions, Boolean functions, and dual spaces can be used eﬀectively if we consider ﬁnite λstructures as probability spaces as we did when we considered ﬁnite λ-structures as a particular case of Borel models.

The following two theorems generalize Theorems 1.12 and 1.13 mentioned in Section 1.1.

Theorem 2.4. Let λ be a signature, let B(FO(λ)) be the Lindenbaum– Tarski algebra of FO(λ), let S(B(FO(λ))) be the associated Stone space, and let rca(S(B(FO(λ)))) be the Banach space of the regular countably additive measures on S(B(FO(λ))). Then:

- (1) There is a mapping from the class of λ-modeling to rca(S(B(FO(λ)))),

which maps a modeling A to the unique regular measure µA such that for every φ ∈ FO(λ) the following equation holds:

φ,A =

S(B(FO(λ)))

1K(φ) dµA,

where 1K(φ) is the indicator function of K(φ) in S(B(FO(λ))). Moreover, this mapping is injective of ﬁnite λ-structures.

- (2) A sequence (An)n∈N of ﬁnite λ-structures is FO-convergent if and only if

the sequence (µA

n

)n∈N is weakly converging in rca(S(B(FO(λ))));

- (3) If (An)n∈N is an FO-convergent sequence of ﬁnite λ-structures then the


)n∈N is such that for every φ ∈ FO(λ) the following equation holds:

weak limit µ of (µA

n

lim

φ,An =

1K(φ) dµ.

n→∞

S(B(FO(λ)))

Proof. The proof follows from Lemma 2.3, considering the additive functions  ·,A .

Let A be a ﬁnite λ-structure. As µA allows one to recover the complete theory of A and as A is ﬁnite, the mapping A  → µA is injective.

It is important to consider fragments of FO(λ) to deﬁne a weaker notion of convergence. This allows us to capture limits of dense graphs too.

Definition 2.5 (X-convergence). Let X be a fragment of FO(λ). A sequence (An)n∈N of ﬁnite λ-structures is X-convergent if φ,An is convergent for every φ ∈ X.

In the particular case that X is a Boolean sub-algebra of B(FO(λ)) we can apply all above methods and in this context we can extend Theorem 2.4.

Theorem 2.6. Let λ be a signature, and let X be a fragment of FO(λ) deﬁning a Boolean algebra B(X) ⊆ B(FO(λ)). Let S(B(X)) be the associated Stone space, and let rca(S(B(X))) be the Banach space of the regular countably additive measure on S(B(X)). Then:

- (1) The canonical injection ιX : B(X) → B(FO(λ)) deﬁnes by duality a con-

tinuous projection pX : S(B(FO(λ))) → S(B(X)); The pushforward pX∗ µA of the measure µA associated to a modeling A (see Theorem 2.4) is the unique regular measure on S(B(X)) such that:

φ,A =

S(B(X))

1K(φ) dpX∗ µA,

where 1K(φ) is the indicator function of K(φ) in S(B(X)).

- (2) A sequence (An)n∈N of ﬁnite λ-structures is X-convergent if and only if

the sequence (pX∗ µA

n

)n∈N is weakly converging in rca(S(B(X)));

- (3) If (An)n∈N is an X-convergent sequence of ﬁnite λ-structures then the


weak limit µ of (pX∗ µA

)n∈N is such that for every φ ∈ X the following equation holds:

n

lim

φ,An =

1K(φ) dµ.

n→∞

S(B(X))

Proof. If X is closed under conjunction, disjunction and negation, thus deﬁning a Boolean algebra B(X), then the inclusion of X in FO(λ) translates as a canonical injection ι from B(X) to B(FO(λ)). By Stone duality, the injection ι corresponds to a continuous projection p : S(B(FO(λ))) → S(B(X)). As every measurable function, this continuous projection also transports measures by pushforward: the projection p transfers the measure µ on S(B(FO(λ))) to S(B(X)) as the pushforward measure p∗µ deﬁned by the identity p∗µ(Y ) = µ(p−1(Y )), which holds for every measurable subset Y of S(B(X)).

The proof follows from Lemma 2.3, considering the additive functions  ·,A .

We can also consider a notion of convergence restricted to λ-structures satisfying a ﬁxed axiom.

Theorem 2.7. Let λ be a signature, and let X be a fragment of FO(λ) deﬁning a Boolean algebra B(X) ⊆ B(FO(λ)). Let S(B(X)) be the associated Stone space, and let rca(S(B(X))) be the Banach space of the regular countably additive measure on S(B(X)).

Let C be a basic elementary class deﬁned by a single axiom Ψ ∈ X ∩ FO0, and let IΨ be the principal ideal of B(X) generated by ¬Ψ.

Then:

- (1) The Boolean algebra obtained by taking the quotient of X equivalence


modulo Ψ is the quotient Boolean algebra B(X,Ψ) = B(X)/IΨ. Then S(B(X,Ψ)) is homeomorphic to the clopen subspace K(Ψ) of S(B(X)).

If A ∈ C is a ﬁnite λ-structure then the support of the measure pX∗ µA associated to A (see Theorem 2.6) is included in K(Ψ) and for every φ ∈ X the following equation holds:

1K(φ) dpX∗ µA.

φ,A =

K(Ψ)

- (2) A sequence (An)n∈N of ﬁnite λ-structures of C is X-convergent if and only

if the sequence (pX∗ µA

n

)n∈N is weakly converging in rca(S(B(X,Ψ)));

- (3) If (An)n∈N is an X-convergent sequence of ﬁnite λ-structures in C then


the weak limit µ of (pX∗ µA

)n∈N is such that for every φ ∈ X the following equation holds:

n

lim

φ,An =

1K(φ) dµ.

n→∞

K(Ψ)

Proof. The quotient algebra B(X,Ψ) = B(X)/IΨ is isomorphic to the subBoolean algebra B of B of all (equivalence classes of) formulas φ ∧ Ψ for φ ∈ X. To this isomorphism corresponds by duality the identiﬁcation of S(B(X,Ψ)) with the clopen subspace K(Ψ) of S(B(X)).

The situation expressed by these theorems is summarized in the following diagram.

B(FO(λ)) canonical injection B(X) inclusion B isomorphism B(X,Ψ)

X

S(B(X)) inclusion K(Ψ) homeomorphism S(B(X,Ψ))

S(B(FO(λ))) projection p

µ pushforward pX∗ µ restriction pX∗ µ The essence of our approach is that we follow a dual path: we view a graph G as an operator on ﬁrst-order formulas through Stone pairing  ·,G .

2.1.4. Limit of Measures Associated to Finite Structures. We consider a signature λ and fragment FOp of FO(λ). Let (An)n∈N be an X-convergent sequence of λ-structures, let µA

###### be the measure on S(B(X)) associated to An, and let µ be the weak limit of µA

n

.

n

Fact 2.8. As we consider countable languages only, S(B(FOp)) is a Radon space and thus for every (Borel) probability measure µ on S(B(FOp)), any measurable set outside the support of µ has zero µ-measure.

Definition 2.9. Let π be the natural projection S(B(FOp)) → S(B(FO0)). A measure µ on S(B(FOp)) is pure if |π(Supp(µ))| = 1. The unique element T

of π(Supp(µ)) is then called the complete theory of µ.

Remark 2.10. Consider FOp or FO convergence. Every measure µ that is the weak limit of some sequence of measures associated to ﬁnite structures is pure and its complete theory has the ﬁnite model property.

###### Indeed, if a sequence (An)n∈N of ﬁnite structures is FOp or FO-convergent it is in particular FO0-convergent. It follows that if µA

weakly converges to µ then π(µ) is concentrated on the complete theory T of the elementary limit of (An)n∈N (thus µ is pure) and as T is the complete theory of the elementary limit of ﬁnite structures it has the ﬁnite model property.

n

Definition 2.11. For T ∈ S(B(FOp),ψ,φ ∈ FOp, and β ∈ FO2p deﬁne

 

k if T (∃=k(y1,...,yp)β(x1,...,xp,y1,...,yp) ∧ ψ(y1,...,yp)) ∞ otherwise.

degβψ+(T) =



k if T (∃=k(x1,...,xp)φ(x1,...,xp) ∧ β(x1,...,xp,y1,...,yp)) ∞ otherwise.

degβφ−(T) =

Denote by ξk the formula ∃=k(y)β(x,y) ∧ ψ(y) (where x = (x1,...,xp) and

- y = (y1,...,yp)) then for every ﬁnite structure A it holds that A |= (∀x) ¬ξk(x,y)


p

+

ψ = |A|

if k > |A|p. Thus degβ

k=1 1K(ξ

k) and

+

degβ

ψ (T)dµA(T) =

K(φ)

|A|p

=

k=1

=

and, similarly we get

=

|A|p

1K(ξ

k) dµA(T)

K(φ)

k=1

ξk ∧ φ,A

1 |A|p

{w ∈ ψ(A) : A |= β(v,w)}

v∈φ(A)

1 |A|p

{((v,w) ∈ φ(A) × ψ(A) : A |= β(v,w)}

1 |A|p

−

degβ

φ (T)dµA(T) =

K(ψ)

1 |A|p

=

{v ∈ φ(A) : A |= β(v,w)}

w∈ψ(A)

{((v,w) ∈ φ(A) × ψ(A) : A |= β(v,w)} .

Thus if µ is a measure associated to a ﬁnite structure then for every φ,ψ ∈ FOp the following equation holds:

+

degβ

ψ (T)dµ(T) =

K(φ)

degβφ−(T)dµ(T).

K(ψ)

Hence for every measure µ that is the weak limit of some sequence of measures associated to ﬁnite structures the following property holds:

###### General Finitary Mass Transport Principle (GFMTP)

For every φ,ψ ∈ FOp, every β ∈ FO2p, and all integers a,b that are such that ∀T ∈ K(φ) degβ

+

ψ (T) ≥ a ∀T ∈ K(ψ) degβφ−(T) ≤ b

the following inequality holds:

aµ(K(φ)) ≤ bµ(K(ψ)).

Of course, similar statement holds as well for the projection of µ on S(B(FOq)) for q < p. In the case of digraphs, when p = 1 and β(x1,x2) is existence of an arc from x1 to x2, we shall write deg+ψ and deg−φ instead of degβψ+ and degβφ−. (In the case of graphs, we have deg+ψ = deg−ψ = degψ.) Thus the following property holds.

Finitary Mass Transport Principle (FMTP) For every φ,ψ ∈ FO1, and all integers a,b that are such that

∀T ∈ K(φ) deg+ψ(T) ≥ a ∀T ∈ K(ψ) deg−φ (T) ≤ b

the following inequality holds:

aµ(K(φ)) ≤ bµ(K(ψ)).

GFMTP and FMTP will play a key role in the analysis of modeling limits.

###### 2.2. Convergence, Old and New

As we have seen above, there are many possible notions of convergence for a sequence (An)n∈N of ﬁnite λ-structures. As we considered λ-structures deﬁned with a countable signature λ, the Boolean algebra B(FO(λ)) is countable. It follows that the Stone space S(B(FO(λ))) is a Polish space, and thus (with the Borel σalgebra) it is a standard Borel space. Hence every probability distribution turns S(B(FO(λ))) into a standard probability space. However, the ﬁne structure of S(B(FO(λ))) is complex and we have no simple description of this space.

FO-convergence is of course the most restrictive notion of convergence and it seems (at least at the ﬁrst glance) that this is perhaps too much to ask, as we may encounter many particular diﬃculties and speciﬁc cases. But we shall exhibit later classes for which FO-convergence is captured — for special basic elementary classes of structures — by X-convergence for a small fragment X of FO.

At this time it is natural to ask whether one can consider fragments whose corresponding Boolean algebras are not sub-Boolean algebras of B(FO(λ)) and still have a description of the limit of a converging sequence as a probability measure on a nice measurable space. There is obviously a case where this is possible: when the convergence of φ,An for every φ in a fragment X implies the convergence of

ψ,An for every ψ in the minimum Boolean algebra containing X. We prove now that this is for instance the case when X is a fragment closed under conjunction.

For a Boolean algebra B and a subset X of B we denote by B[X] the Boolean sub-algebra of B generated by X, that is the sub-algebra of B whose elements can

be expressed as a ﬁnite combination of elements of X, using the Boolean operations (in B). We shall need the following preliminary lemma:

Lemma 2.12. Let B be a Boolean algebra and let X ⊆ B be closed under ∧ and such that X generates B (i.e. such that B[X] = B).

Then {1b : b ∈ X} ∪ {1} (where 1 is the constant function with value 1) includes a basis of the vector space V (B) generated by the whole set {1b : b ∈ B}.

Proof. Let b ∈ B. As X generates B there exist b1,...,bk ∈ X and a Boolean function F such that b = F(b1,...,bk). As 1x∧y = 1x 1y and 1¬x = 1 − 1x there exists a polynomial PF such that 1b = PF(1b

###### ). For I ⊆ [k], the monomial i∈I 1b

###### ,...,1b

1

k

where bI = i∈I bi. It follows that 1b is a linear combination of the functions 1b

rewrites as 1b

i

I

(I ⊆ [k]) which belong to X if I = ∅ (as X is closed under ∧ operation) and equals 1, otherwise.

I

Proposition 2.13. Let X be a fragment of FO(λ) closed under (ﬁnite) conjunction — thus deﬁning a meet semilattice of B(FO(λ)) — and let B(X) be the sub-Boolean algebra of B(FO(λ)) generated by X. Let X be the fragment of FO(λ) consisting of all formulas with equivalence class in B(X).

Then X-convergence is equivalent to X-convergence. Proof. Let Ψ ∈ X. According to Lemma 2.12, there exist φ1,...,φk ∈ X and

α0,α1,...,αk ∈ R such that

k

1Ψ = α01 +

αi1φ

.

i

i=1

Let A be a λ-structure, let Ω = S(B(X)) and let µA ∈ rca(Ω) be the associated measure. Then

Ψ,A =

1Ψ dµA =

Ω

Ω

k

αi1φ

α01 +

i

i=1

k

αi φi,A .

dµG = α0 +

i=1

It follows that if (An)n∈N is an X-convergent sequence, the sequence ( ψ,An )n∈N converges for every ψ ∈ X, that is (An)n∈N is X-convergent.

Now we demonstrate the expressive power of X-convergence by relating it to the main types of convergence of graphs studied previously:

- (1) the notion of dense graph limit [14, 63];
- (2) the notion of bounded degree graph limit [10, 5];
- (3) the notion of elementary limit derived from two important results in ﬁrstorder logic, namely G¨del’s completeness theorem and the compactness theorem.


These standard notions of graph limits, which have inspired this work, correspond to special fragments of FO(γ), where γ is the signature of graphs. In the remainder of this section, we shall only consider undirected graphs, thus we shall omit making mention of their signature in the notations as well as the axioms deﬁning the basic elementary class of undirected graphs.

2.2.1. L-convergence and QF-convergence. Recall that a sequence (Gn)n∈N of graphs is L-convergent if

hom(F,Gn) |Gn||F|

t(F,Gn) =

converges for every ﬁxed (connected) graph F, where hom(F,G) denotes the number of homomorphisms of F to G [63, 16, 17].

It is a classical observation that homomorphisms between ﬁnite structures can be expressed by Boolean conjunctive queries [19]. We denote by HOM the fragment of FO consisting of formulas formed by conjunction of atoms. For instance, the formula

(x1 ∼ x2) ∧ (x2 ∼ x3) ∧ (x3 ∼ x4) ∧ (x4 ∼ x5) ∧ (x5 ∼ x1)

belongs to HOM and it expresses that (x1,x2,x3,x4,x5) form a homomorphic image of C5. Generally, to a ﬁnite graph F we associate the canonical formula φF ∈ HOM deﬁned by

(xi ∼ xj).

φF :=

ij∈E(F)

Then, for every graph G the following equation holds:

hom(F,G) |G||F|

φF,G =

= t(F,G).

Thus L-convergence is equivalent to HOM-convergence. According to Proposition 2.13, HOM-convergence is equivalent to HOM-convergence. It is easy to see that HOM is the fragment QF− of quantiﬁer free formulas that do not use equality. We prove now that HOM-convergence is actually equivalent to QF-convergence, where QF is the fragment of all quantiﬁer free formulas. Note that QF is a proper fragment of the fragment FOlocal of local formulas (that is of formulas whose satisfaction only depends on a ﬁxed neighborhood of the free variables, see Section 2.2.2 for a formal deﬁnition).

Theorem 2.14. Let (Gn) be a sequence of ﬁnite graphs such that limn→∞ |Gn| = ∞.

Then the following conditions are equivalent:

- (1) the sequence (Gn) is L-convergent;
- (2) the sequence (Gn) is QF−-convergent;
- (3) the sequence (Gn) is QF-convergent;


Proof. As L-convergence is equivalent to HOM-convergence and as HOM ⊂ QF− ⊂ QF, it is suﬃcient to prove that L-convergence implies QF-convergence.

Assume (Gn) is L-convergent. The inclusion/exclusion principle implies that for every ﬁnite graph F the density of induced subgraphs isomorphic to F converges too. Deﬁne

(#F ⊆i Gn) |Gn||F|

dens(F,Gn) =

. Then dens(F,Gn) is a converging sequence for each F.

Let θ be a quantiﬁer free formula with Fv(θ) ⊆ [p]. We ﬁrst consider all possible cases of equalities between the free variables. For a partition P = (I1,...,Ik) of [p], we deﬁne |P| = k and sP(i) = minIi (for 1 ≤ i ≤ |P|). Consider the formula

|P|

|P|

P(i)) ∧

(xj = xs

(xs

P(j) = xs

P(i)) .

ζP :=

i=1 j∈Ii

j=i+1

Then θ is logically equivalent to (

(xi = xj) ∧ θ) ∨

ζP ∧ θP(xs

P(1),...,xs

P(|P|)).

i =j

P:|P|<p

Note that all the formulas in the disjunction are mutually exclusive. Also i =j(xi = xj) ∧ θ may be expressed as a disjunction of mutually exclusive terms:

(xi = xj) ∧ θ =

θ F,

F∈F

i =j

where F is a ﬁnite family of ﬁnite graphs F and where G |= θ F(v1,...,vp) if and only if the mapping i  → vi is an isomorphism from F to G[v1,...,vp].

It follows that for every graph G it holds that θ,G =

ζP ∧ θP(xs

θ F,G +

P(1),...,xs

P(|P|)),G

F∈F

P:|P|<p

|G||P|−p θP,G

=

θ F,G +

F∈F

P:|P|<p

|{(v1,...,vp) : G |= θ F(vσ(1),...,vσ(p))}| |G|p

1 p! σ∈S

+ O(|G|−1)

=

F∈F

p

Aut(F) p!

dens(F,G) + O(|G|−1).

=

F∈F

Thus θ,Gn converge for every quantiﬁer free formula θ. Hence (Gn) is QFconvergent.

Notice that the condition that limn→∞ |Gn| is necessary as witnessed by the sequence (Gn) where Gn is K1 if n is odd and 2K1 if n is even. The sequence is obviously L-convergent, but not QF convergent as witnessed by the formula φ(x,y) : x = y, which has density 0 in K1 and 1/2 in 2K1.

Remark 2.15. The Stone space of the fragment QF− has a simple description. Indeed, a homomorphism h : B(QF−) → 2 is determined by its values on the formulas xi ∼ xj and any mapping from this subset of formulas to 2 extends (in a unique way) to a homomorphism of B(QF−) to 2. Thus the points of S(B(QF−)) can be identiﬁed with the mappings from N2 to {0,1} that is to the graphs on N. Hence the considered measures µ are probability measures of graphs on N that have the property that they are invariant under the natural action of Sω on N. Such random graphs on N are called inﬁnite exchangeable random graphs. For more on inﬁnite exchangeable random graphs and graph limits, see e.g. [8, 25].

2.2.2. BS-convergence and FOlocal-convergence. The class of graphs with maximum degree at most D (for some integer D) has received much attention. Speciﬁcally, the notion of local weak convergence of bounded degree graphs was introduced in [10], which is called here BS-convergence:

A rooted graph is a pair (G,o), where o ∈ V (G). An isomorphism of rooted graph φ : (G,o) → (G ,o ) is an isomorphism of the underlying graphs which satisﬁes φ(o) = o . Let D ∈ N. Let GD denote the collection of all isomorphism classes of connected rooted graphs with maximal degree at most D. For the sake of simplicity, we denote elements of GD simply as graphs. For (G,o) ∈ GD and r ≥ 0 let BG(o,r) denote the subgraph of G spanned by the vertices at distance at most r from o. If (G,o),(G ,o ) ∈ GD and r is the largest integer such that (BG(o,r),o) is rooted-graph isomorphic to (BG (o ,r),o ), then set ρ((G,o),(G ,o )) = 1/r, say. Also take ρ((G,o),(G,o)) = 0. Then ρ is metric on GD. Let MD denote the space of all probability measures on GD that are measurable with respect to the Borel σ-ﬁeld of ρ. Then MD is endowed with the topology of weak convergence, and is compact in this topology.

A sequence (Gn)n∈N of ﬁnite connected graphs with maximum degree at most D is BS-convergent if, for every integer r and every rooted connected graph (F,o) with maximum degree at most D the following limit exists:

(v,r) ∼= (F,o)}| |Gn|

|{v : BG

n

.

lim

n→∞

This notion of limits leads to the deﬁnition of a limit object as a probability measure on GD [10].

To relate BS-convergence to X-convergence, we shall consider the fragment of local formulas:

Let r ∈ N. A formula φ ∈ FOp is r-local if, for every graph G and every v1,...,vp ∈ Gp the following equivalence holds:

G |= φ(v1,...,vp) ⇐⇒ G[Nr(v1,...,vp)] |= φ(v1,...,vp),

where G[Nr(v1,...,vp)] denotes the subgraph of G induced by all the vertices at (graph) distance at most r from one of v1,...,vp in G.

A formula φ is local if it is r-local for some r ∈ N; the fragment FOlocal is the set of all local formulas in FO. Notice that if φ1 and φ2 are local formulas, so are φ1 ∧ φ2, φ1 ∨ φ2 and ¬φ1. It follows that the quotient of FOlocal by the relation of logical equivalence deﬁnes a sub-Boolean algebra B(FOlocal) of B(FO). For p ∈ N we further deﬁne FOlocalp = FOlocal ∩ FOp.

Theorem 2.16. Let (Gn) be a sequence of ﬁnite graphs with maximum degree d, with limn→∞ |Gn| = ∞.

Then the following properties are equivalent:

- (1) the sequence (Gn)n∈N is BS-convergent;
- (2) the sequence (Gn)n∈N is FOlocal1 -convergent;
- (3) the sequence (Gn)n∈N is FOlocal-convergent.


Proof. If (Gn)n∈N is FOlocal-convergent, it is FOlocal1 -convergent;

If (Gn)n∈N is FOlocal1 -convergent then it is BS-convergent as for any ﬁnite rooted graph (F,o), testing whether the the ball of radius r centered at a vertex x is isomorphic to (F,o) can be formulated by a local ﬁrst order formula.

Assume (Gn)n∈N is BS-convergent. As we consider graphs with maximum degree d, there are only ﬁnitely many isomorphism types for the balls of radius r centered at a vertex. It follows that any local formula ξ(x) with a single variable can be expressed as the conjunction of a ﬁnite number of (mutually exclusive) formulas ξ(F,o)(x), which in turn correspond to subgraph testing. It follows that BS-convergence implies FOlocal1 -convergence.

Assume (Gn)n∈N is FOlocal1 -convergent and let φ ∈ FOlocalp be an r-local formula. Let Fφ be the set of all p-tuples ((F1,f1),...,(Fp,fp)) of rooted connected graphs with maximum degree at most d and radius (from the root) at most r such

that i Fi |= φ(f1,...,fp). Then, for every graph G the sets

Ωφ(G) = {(v1,...,vp) : G |= φ(v1,...,vp)} and

p

{v : G |= θ(F

i,fi)(v)}

i=1

((F1,f1),...,(Fp,fp))∈Fφ

diﬀer by at most O(|G|p−1) elements. Indeed, according to the deﬁnition of an r-local formula, the p-tuples (x1,...,xp) belonging to exactly one of these sets are such that there exists 1 ≤ i < j ≤ p such that dist(xi,xj) ≤ 2r.

It follows that

φ,G =

p

i=1

((Fi,fi))1≤i≤p∈Fφ

i,fi),G + O(|G|−1).

θ(F

It follows that FOlocal1 -convergence (hence BS-convergence) implies full FOlocalconvergence.

Remark 2.17. According to this proposition and Theorem 2.7, the BS-limit of a sequence of graphs with maximum degree at most D corresponds to a probability measure on S(B(FOlocal1 )) whose support is include in the clopen set K(ζD), where ζD is the sentence expressing that the maximum degree is at most D. The Boolean algebra B(FOlocal1 ) is isomorphic to the Boolean algebra deﬁned by the fragment X ⊂ FO0(λ1) of sentences for rooted graphs that are local with respect to the root (here, λ1 denotes the signature of graphs augmented by one symbol of constant). According to this locality, any two countable rooted graphs (G1,r1) and (G2,r2), the trace of the complete theories of (G1,r1) and (G2,r2) on X are the same if and only if the (rooted) connected component (G 1,r1) of (G1,r1) containing the root r1 is elementary equivalent to the (rooted) connected component (G 2,r2) of (G2,r2) containing the root r2. As isomorphism and elementary equivalence are equivalent for countable connected graphs with bounded degrees (see Lemma 2.20) it is easily checked that KX(ζD) is homeomorphic to GD. Hence our setting (based on a very diﬀerent and dual approach) leads essentially to the same limit object as [10] for BS-convergent sequences.

2.2.3. Elementary-convergence and FO0-convergence. We already mentioned that FO0-convergence is nothing but elementary convergence. Elementary convergence is implicitly part of the classical model theory. Although we only consider graphs here, the deﬁnition and results indeed generalize to general λ-structures We now reword the notion of elementary convergence:

A sequence (Gn)n∈N is elementarily convergent if, for every sentence φ ∈ FO0, there exists a integer N such that either all the graphs Gn (n ≥ N) satisfy φ or none of them do.

Of course, the limit object (as a graph) is not unique in general and formally, the limit of an elementarily convergent sequence of graphs is an elementary class deﬁned by a complete theory.

Elementary convergence is also the backbone of all the X-convergences we consider in this paper. The FO0-convergence is induced by an easy ultrametric deﬁned on equivalence classes of elementarily equivalent graphs. Precisely, two (ﬁnite or inﬁnite) graphs G1,G2 are elementarily equivalent (denoted G1 ≡ G2) if, for every sentence φ the following equivalence holds:

G1 |= φ ⇐⇒ G2 |= φ.

In other words, two graphs are elementarily equivalent if they satisfy the same sentences.

A weaker (parametrized) notion of equivalence will be crucial: two graphs G1,G2 are k-elementarily equivalent (denoted G1 ≡k G2) if, for every sentence φ with quantiﬁer rank at most k it holds that G1 |= φ ⇐⇒ G2 |= φ.

It is easily checked that for every two graphs G1,G2 the following equivalence holds:

G1 ≡ G2 ⇐⇒ (∀k ∈ N) G1 ≡k G2.

For every ﬁxed k ∈ N, checking whether two graphs G1 and G2 are k-elementarily equivalent can be done using the so-called Ehrenfeucht-Fraı¨ss´e game.

From the notion of k-elementary equivalence naturally derives a pseudometric dist0(G1,G2):

0 if G1 ≡ G2 min{2−qrank(φ) : (G1 |= φ) ∧ (G2 |= ¬φ)} otherwise

dist0(G1,G2) =

Proposition 2.18. The metric space of countable graphs (up to elementary equivalence) with ultrametric dist0 is compact.

Proof. This is a direct consequence of the compactness theorem for ﬁrst-order logic (a theory has a model if and only if every ﬁnite subset of it has a model) and of the downward L¨wenheim-Skolem theorem (if a theory has a model and the language is countable then the theory has a countable model).

Note that not every countable graph is (up to elementary equivalence) the limit of a sequence of ﬁnite graphs. A graph G that is a limit of a sequence ﬁnite graphs is said to have the ﬁnite model property, as such a graph is characterized by the property that every ﬁnite set of sentences satisﬁed by G has a ﬁnite model (which does not imply that G is elementarily equivalent to a ﬁnite graph). As proved by Trakhtenbrot [90] the set of ﬁnitely satisﬁable sentences is not decidable and deciding wether a given theory has a ﬁnite model is usually an extremely diﬃcult problem (see for instance Example 2.36).

Example 2.19. A ray is not an elementary limit of ﬁnite graphs as it contains exactly one vertex of degree 1 and all the other vertices have degree 2, what can be expressed in ﬁrst-order logic but is satisﬁed by no ﬁnite graph. However, the union of two rays is an elementary limit from the sequence (Pn)n∈N of paths of order n.

Although two ﬁnite graphs are elementary equivalent if and only if they are isomorphic, this property does not holds in general for countable graphs. For instance, the union of a ray and a line is elementarily equivalent to a ray. However we shall make use of the equivalence of isomorphisms and elementary equivalences for rooted connected countable locally ﬁnite graphs, which we prove now for completeness.

Lemma 2.20. Let (G,r) and (G ,r ) be two rooted connected countable graphs. If G is locally ﬁnite then (G,r) ≡ (G ,r ) if and only if (G,r) and (G ,r ) are

isomorphic.

Proof. If two rooted graphs are isomorphic they are obviously elementarily equivalent. Assume that (G,r) and (G ,r ) are elementarily equivalent. Enumerate the vertices of G in a way that distance to the root is not decreasing. Using n-backand-forth equivalence (for all n ∈ N), one builds a tree of partial isomorphisms of the subgraphs induced by the n ﬁrst vertices, where ancestor relation is restriction. This tree is inﬁnite and has only ﬁnite degrees. Hence, by K˝nig’s lemma, it contains an inﬁnite path. It is easily checked that it deﬁnes an isomorphism from (G,r) to (G ,r ) as these graphs are connected.

Fragments of FO0 allow to deﬁne convergence notions, which are weaker than elementary convergence. The hierarchy of the convergence schemes deﬁned by subalgebras of B(FO0) is as strict as one could expect. Precisely, if X ⊂ Y are two sub-algebras of B(FO0) then Y -convergence is strictly stronger than X-convergence — meaning that there exists graph sequences that are X-convergent but not Y convergent — if and only if there exists a sentence φ ∈ Y such that for every sentence ψ ∈ X, there exists a (ﬁnite) graph G disproving φ ↔ ψ.

We shall see that the special case of elementary convergent sequences is of particular importance. Indeed, every limit measure is a Dirac measure concentrated on a single point of S(B(FO0)). This point is the complete theory of the elementary limit of the considered sequence. This limit can be represented by a ﬁnite or countable graph. As FO-convergence (and any FOp-convergence) implies FO0convergence, the support of a limit measure µ corresponding to an FOp-convergent sequence (or to an FO-convergent sequence) is such that Supp(µ) projects to a single point of S(B(FO0)).

Finally, let us remark that all the results of this section can be readily formulated and proved for λ-structures.

###### 2.3. Combining Fragments

2.3.1. The FOp Hierarchy. When we consider FOp-convergence of ﬁnite λ-structures for ﬁnite a signature λ, the space S(B(FOp(λ))) can be given the following ultrametric distp (compatible with the topology of S(B(FOp(λ)))): Let T1,T2 ∈ S(B(FOp(λ))) (where the points of S(B(FOp(λ))) are identiﬁed with ultraﬁlters on B(FOp(λ))). Then

0 if T1 = T2 2−min{qrank(φ): φ∈T

distp(T1,T2) =

1\T2} otherwise

This ultrametric has several other nice properties:

- • actions of Sp on S(B(FOp(λ))) are isometries: ∀σ ∈ Sp ∀T1,T2 ∈ S(B(FOp(λ))) distp(σ · T1,σ · T2) = distp(T1,T2);
- • projections πp are contractions: ∀q ≥ p ∀T1,T2 ∈ S(B(FOq(λ))) distp(πp(T1),πp(T2)) ≤ distq(T1,T2).


We prove that there is a natural isometric embedding ηp : S(B(FOp(λ))) → S(B(FO(λ))). This may be seen as follows: for an ultraﬁlter X ∈ S(B(FOp(λ))), consider the ﬁlter X+ on B(FO(λ)) generated by X and all the formulas xi = xi+1 (for i ≥ p). This ﬁlter is an ultraﬁlter: for every sentence φ ∈ FO(λ), let φ be the sentence obtained from φ by replacing each free occurrence of a variable xq with q > p by xp. It is clear that φ and φ are equivalent modulo the theory Tp = {(xi = xi+1) : i ≥ p}. As either φ or ¬ φ belongs to X, either φ or ¬φ belongs to ηp(X). Moreover, we deduce easily from the fact that φ and φ have the same quantiﬁer rank that if q ≥ p then πq ◦ ηp is an isometry. Finally, let us note that πp ◦ ηp is the identity of S(B(FOp(λ))).

Let λp be the signature λ augmented by p symbols of constants c1,...,cp. There is a natural isomorphism of Boolean algebras νp : FOp(λ) → FO0(λp), which replaces the free occurrences of the variables x1,...,xp in a formula φ ∈ FOp by the corresponding symbols of constants c1,...,cp, so that the following equation holds, for every modeling A, for every φ ∈ FOp and every v1,...,vp ∈ A:

A |= φ(v1,...,vp) ⇐⇒ (A,v1,...,vp) |= νp(φ).

This mapping induces an isometric isomorphism of the metric spaces (S(B(FOp(λ))),distp) and (S(B(FO0(λp))),dist0). Note that the Stone space S(B(FO0(λp))) associated to the Boolean algebra B(FO0(λp)) is the space of all complete theories of λp-structures. In particular, points of S(B(FOp(λ)) can be represented (up to elementary equivalence) by countable λ-structures with p special points. All these transformations may seem routine but they need to be carefully formulated and checked.

We can test whether the distance distp of two theories T and T is smaller than 2−n by means of an Ehrenfeucht-Fra¨ıss´e game: Let νp(T) = {νp(φ) : φ ∈ T} and, similarly, let νp(T ) = {νp(φ) : φ ∈ T }. Let (A,v1,...,vp) be a model of T and let (A ,v 1,...,v p) be a model of T . Then the following equivalence holds:

distp(T,T ) < 2−n ⇐⇒ (A,v1,...,vp) ≡n (A ,v 1,...,v p). Recall that the n-rounds Ehrenfeucht-Fraı¨ss´e game on two λ-structures A and A , denoted EF(A,A ,n) is the perfect information game with two players — the Spoiler and the Duplicator — deﬁned as follows: The game has n rounds and each round has two parts. At each round, the Spoiler ﬁrst chooses one of A and A and accordingly selects either a vertex x ∈ A or a vertex y ∈ A . Then, the Duplicator selects a vertex in the other λ-structure. At the end of the n rounds, n vertices have been selected from each structure: x1,...,xn in A and y1,...,yn in A (xi and yi corresponding to vertices x and y selected during the ith round). The Duplicator wins if the substructure induced by the selected vertices are order-isomorphic (i.e. xi  → yi is an isomorphism of A[{x1,...,xn}] and A [{y1,...,yn}]). As there are no hidden moves and no draws, one of the two players has a winning strategy, and

we say that that player wins EF(A,A ,n). The main property of this game is the following equivalence, due to Fraı¨sse´ [36, 37] and Ehrenfeucht [29]: The duplicator wins EF(A,A ,n) if and only if A ≡n A . In our context this translates to the following equivalence:

distp(T,T ) < 2−n ⇐⇒ Duplicator wins EF((A,v1,...,vp),(A ,v 1,...,v p),n).

As FO0 ⊂ FO1 ⊂ ··· ⊂ FOp ⊂ FOp+1 ⊂ ··· ⊂ FO = i FOi, the fragments FO form a hierarchy of more and more restrictive notions of convergence. In particular,

FOp+1-convergence implies FOp-convergence and FO-convergence is equivalent to FOp for all p. If a sequence (An)n∈N is FOp-convergent then for every q ≤ p the FOq-limit of (An)n∈N is a measure µq ∈ rca(S(B(FOq))), which is the pushforward of µp by the projection πq (more precisely, by the restriction of πq to S(B(FOp))):

µq = (πq)∗(µp).

2.3.2. FOlocal and Locality. FO-convergence can be reduced to the conjunction of elementary convergence and FOlocal-convergence, which we call local convergence. This is a consequence of a result, which we recall now:

Theorem 2.21 (Gaifman locality theorem [39]). For every ﬁrst-order formula φ(x1,...,xn) there exist integers t and r such that φ is equivalent to a Boolean combination of t-local formulas ξs(xi

###### ,...,xi

) and sentences of the form

1

s

(2.1) ∃y1 ...∃ym

dist(yi,yj) > 2r ∧

ψ(yi)

1≤i<j≤m

1≤i≤m

where ψ is r-local. Furthermore, we can choose r ≤ 7qrank(φ)−1, t ≤ (7qrank(φ)−1 − 1)/2, m ≤ n + qrank(φ),

and, if φ is a sentence, only sentences (2.1) occur in the Boolean combination. Moreover, these sentences can be chosen with quantiﬁer rank at most q(qrank(φ)), for some ﬁxed function q.

From this theorem and the following folklore technical result will follow the claimed decomposition of FO-convergence into elementary and local convergence.

Lemma 2.22. Let B be a Boolean algebra, let A1 and A2 be sub-Boolean algebras of B, and let b ∈ B[A1 ∪ A2] be a Boolean combination of elements from A1 and A2. Then b can be written as

xi ∧ yi,

b =

i∈I

where I is ﬁnite, xi ∈ A1, yi ∈ A2, and for every i = j in I it holds that (xi ∧ yi) ∧ (xj ∧ yj) = 0.

Proof. Let b = F(u1,...,ua,v1,...,vb) with ui ∈ A1 (1 ≤ i ≤ a) and vj ∈ A2 (1 ≤ j ≤ b) where F is a Boolean combination. By using iteratively Shannon’s expansion, we can write F as

ui ∧

¬ui ∧

vj ∧

¬vj),

F(u1,...,ua,v1,...,vb) =

(

i∈X1

i∈X2

j∈Y1

j∈Y2

(X1,X2,Y1,Y2)∈F

where F is a subset of the quadruples (X1,X2,Y1,Y2) such that (X1,X2) is a partition of [a] and (Y1,Y2) is a partition of [b]. For a quadruple Q = (X1,X2,Y1,Y2),

vj ∧ j∈Y2 ¬vj. Then for every Q ∈ F it holds that xQ ∈ A1,yQ ∈ A2, for every Q = Q ∈ F it holds that xQ ∧ yQ ∧ xQ ∧ yQ = 0, and we have b = Q∈F xQ ∧ yQ.

###### ui ∧ i∈X2 ¬ui and yQ = j∈Y

###### deﬁne xQ = i∈X

1

1

Theorem 2.23. Let (An) be a sequence of ﬁnite λ-structures. Then (An) is FO-convergent if and only if it is both FOlocal-convergent and FO0-convergent. Precisely, (An) is FOp-convergent if and only if it is both FOlocalp -convergent and FO0-convergent.

Proof. Assume (An)n∈N is both FOlocalp -convergent and FO0-convergent and let φ ∈ FOp. According to Theorem 2.21, there exist integers t and r such that φ is equivalent to a Boolean combination of t-local formula ξ(xi

) and of sentences. As both FOlocal and FO0 deﬁne a sub-Boolean algebra of B(FO), according to Lemma 2.22, φ can be written as i∈I ψi ∧ θi, where I is ﬁnite, ψi ∈ FOlocal, θi ∈ FO0, and ψi ∧ θi ∧ ψj ∧ θj = 0 if i = j. Thus for every ﬁnite λ-structure A the following equation holds:

###### ,...,xi

1

s

ψi ∧ θi,A .

φ,A =

i∈I

As  ·,A is additive and θi,A ∈ {0,1} we have ψi ∧ θi,A = ψi,A θi,A . Hence

φ,A =

ψi,A θi,A .

i∈I

Thus if (An)n∈N is both FOlocalp -convergent and FO0-convergent then (An)n∈N is FOp-convergent.

Similarly points of S(B(FOp(λ)) can be represented (up to elementary equivalence) by countable λ-structures with p special points, and points of S(B(FOlocalp (λ)) can be represented by countable λ-structures with p special points such that every connected component contains at least one special point. In particular, points of S(B(FOlocal1 (λ)) can be represented by rooted connected countable λ-structures.

Also, the structure of an FOlocal2 -limit of graphs can be outlined by considering that points of S(B(FOlocal2 )) as countable graphs with two special vertices c1 and c2, such that every connected component contains at least one of c1 and c2. Let µ2 be the limit probability measure on S(B(FOlocal2 )) for an FOlocal2 -convergent sequence (Gn)n∈N, let π1 be the standard projection of S(B(FOlocal2 )) into S(B(FOlocal1 )), and let µ1 be the pushforward of µ2 by π1. We construct a measurable graph Gˆ as follows: the vertex set of Gˆ is the support Supp(µ1) of µ1. Two vertices x and y of Gˆ are adjacent if there exists x ∈ π1−1(x) and y ∈ π1−1(y) such that (considered as ultraﬁlters of B(FOlocal2 )) it holds that:

- • x1 ∼ x2 belongs to both x and y ,
- • the transposition τ1,2 exchanges x and y (i.e. y = τ1,2 · x ).


The vertex set of Gˆ is of course endowed with a structure of a probability space (as a measurable subspace of S(B(FOlocal1 )) equipped with the probability measure µ1). In the case of bounded degree graphs, the obtained graph Gˆ is the graph of

###### graphs introduced in [61]. Notice that this graph may have loops. An example of such a graph is shown Fig. 1.

S(B(FOlocal1 ))

- 2−1
- 2−2
- 2−3
- 2−4
- 2−5


...

Figure 1. An outline of the local limit of a sequence of trees

2.3.3. Component-Local Formulas. It is sometimes possible to reduce FOlocal to a smaller fragment. This is in particular the case when connected components of the considered structures can be identiﬁed by some ﬁrst-order formula. Precisely:

Definition 2.24. Let λ be a signature and let T be a theory of λ-structures.

- A binary relation ∈ λ is a component relation in T if T entails that is an equivalence relation such that for every k-ary relation R ∈ λ with k ≥ 2 the following property holds:


T |= (∀x1,...,xk) R(x1,...,xk) →

(xi,xj) .

1≤i<j≤k

A local formula φ with p free variables is -local if φ is equivalent (modulo T) to φ ∧ xi,xj∈Fv(φ) (xi,xj).

In presence of a component relation, it is possible to reduce from FOlocal to the fragment of -local formulas, thanks to the following result.

###### Lemma 2.25. Let be a component relation in a theory T. For every local formula φ with quantiﬁer rank r there exist -local formulas ξi,j ∈ FOlocalq

(1 ≤ i ≤ n, j ∈ Ii) with quantiﬁer rank at most r and permutations σi of [p] (1 ≤ i ≤ n) such that for each 1 ≤ i ≤ n, j∈I

i,j

qi,j = p and, for every model A of T the following equation holds:

i

n

Ωφ(A) =

Fσ

Ωξ

(A) ,

i

i,j

j∈Ii

i=1

where Fσ

(X) performs a permutation of the coordinates according to σi.

i

Proof. First note that if two -local formulas φ1 and φ2 share a free variable then φ1 ∧ φ2 is -local. For this obvious fact, we deduce that if ψ1,...,ψn are

-local formulas in FOp, then there is a partition τ and a permutation σ of [p] such that for every λ-structure A the following equation holds:

i∈P ψi(A) , where each i∈P ψi is -local, and Fσ : Ap → Ap is deﬁned by Fσ(X) = {(vσ(1),...,vσ(p)) : (v1,...,vp) ∈ X}.

Ω n

i=1 ψi(A) = Fσ

Ω

P∈τ

For a partition τ of [p] we denote by ζτ the conjunction of (xi,xj) for every i,j belonging to a same part and of ¬ (xi,xj) for every i,j belonging to diﬀerent parts. Then, for any two distinct partitions τ and τ , the formula ζτ ∧ ζ τ is never satisﬁed; moreover τ ζτ is always satisﬁed. Thus for every local formula φ the following equation holds:

(ζτ ∧ φ) =

(ζτ ∧ φ)

φ =

τ

τ

(where only the partitions τ for which ζτ ∧ φ = 0 have to be considered).

We denote by Λτ the formula P∈τ i,j∈P (xi,xj). Obviously the following equation holds:

Λτ =

ζτ,

τ ≥τ

where ⊕ stands for the exclusive disjunction (a ⊕ b = (a ∧ ¬n) ∨ (¬a ∧ b)) and τ ≥ τ means that τ is a partition of [p], which is coarser than τ. Then there exists (by Mo¨bius inversion or immediate induction) a function M from the set of the partitions of [p] to the powerset of the set of partitions of [p] such that for every partition τ of [p] the following equation holds:

ζτ =

Λτ .

τ ∈M(τ)

Hence

Λτ ∧ φ.

φ =

τ τ ∈M(τ)

It follows that φ is a Boolean combination of formulas Λτ ∧ φ, for partitions τ such that ζτ ∧ φ = 0 (as ζτ ∧ φ = 0 and τ ≥ τ imply ζτ ∧ φ = 0). Each formula Λτ ∧φ is itself a Boolean combination of -local formulas. Putting this in standard form (exclusive disjunction of conjunctions) and gathering in the conjunctions the

-local formulas whose set of free variables intersect, we get that there exist families

- Fτ of -local formulas ϕP (P ∈ τ) with free variables Fv(ϕP) = {xj : j ∈ P} such that


φ =

ϕP,

τ ϕ∈Fτ P∈τ

where the disjunction is exclusive.

Hence, considering adequate permutations στ of [p] the following equation holds:

Fσ

Ωφ(A) =

Ωϕ˜

(A) ,

τ

P

τ ϕ∈Fτ

P∈τ

which is the requested form. Note that the fact that qrank(ξi,j) ≤ qrank(φ) is obvious as we did not intro-

duce any quantiﬁer in our transformations. As a consequence, we get the the desired: Corollary 2.26. Let be a component relation in a theory T and let (An)n∈N

be a sequence of models of T. Then the sequence (An)n∈N is FOlocal-convergent if and only if it is FO -local-convergent.

2.3.4. Sequences with Homogeneous Elementary Limit. Elementary convergence is an important aspect of FO-convergence and we shall see that in several contexts, FO-convergence can be reduced to the conjunction of elementary convergence and X-convergence (for some suitable fragment X).

In some special cases, the limit (as a countable structure) will be unique. This means that some particular complete theories have exactly one countable model (up to isomorphism). Such complete theories are called ω-categorical. Several properties are known to be equivalent to ω-categoricity. For instance, for a complete theory T the following statements are equivalent:

- • T is ω-categorical;
- • for every p ∈ N, the Stone space S(B(FOp(λ),T)) is ﬁnite (see Fig. 2);
- • every countable model A of T has an oligomorphic automorphism group, what means that for every n ∈ N, An has ﬁnitely many orbits under the action of Aut(A).


A theory T is said to have quantiﬁer elimination if, for every p and every formula φ ∈ FOp(λ) there exists φ ∈ QFp(λ) such that T |= φ ↔ φ. If a theory (in the language of relational structures with given ﬁnite signature, like the language of graphs) has quantiﬁer elimination then it is ω-categorical. Indeed, for every p, there exists only ﬁnitely many quantiﬁer free formulas with p free variables hence (up to equivalence modulo T) only ﬁnitely many formulas with p free variables. The unique countable model of a complete theory T (in the language of relational structures with given ﬁnite signature) with quantiﬁer elimination is ultra-homogeneous, what means that every partial isomorphism of ﬁnite induced substructures extends

- as a full automorphism. In the context of relational structures with given ﬁnite signature, the property of having a countable ultra-homogeneous model is equivalent to the property of having quantiﬁer elimination. We provide a proof of this folklore result in the context of graphs in order to illustrate these notions.


S(B(FO))

- π2

π1

π0

| | |
|---|---|
| | |


- π3


- S(B(FO0)) T

- S(B(FO1))
- S(B(FO2))
- S(B(FO3))


| | |
|---|---|
| | |
| | |
| | |


Figure 2. Ultraﬁlters projecting to an ω-categorical theory

Lemma 2.27. Let T be a complete theory of graphs with no ﬁnite model. Then T has quantiﬁer elimination if and only if some (equivalently, every)

countable model of T is ultra-homogeneous. Proof. Assume that T has an ultra-homogeneous countable model G. Let

- (a1,...,ap), (b1,...,bp) be p-tuples of vertices of G. Assume that ai  → bi is an isomorphism between G[a1,...,ap] and G[b1,...,bp]. Then, as G is ultrahomogeneous, there exists an automorphism f of G such that f(ai) = bi for every 1 ≤ i ≤ p. As the satisfaction of a ﬁrst-order formula is invariant under the action


of the automorphism group, for every formula φ ∈ FOp the following equivalence holds:

G |= φ(a1,...,ap) ⇐⇒ G |= φ(b1,...,bp). Consider a maximal set F of p-tuples (v1,...,vp) of G such that G |= φ(v1,...,vp) and no two p-tuples induce isomorphic (ordered) induced subgraphs. Obviously |F| = 2O(p

2) is ﬁnite. Moreover, each p-tuple  v = (v1,...,vp) deﬁnes a quantiﬁer free formula η v with p free variables such that G |= η v(x1,...,xp) if and only if xi  → vi is an isomorphism between G[x1,...,xp] and G[v1,...,vp]. Hence the following property holds:

G |= φ ↔

η v.

 v∈F

In other words, φ is equivalent (modulo T) to the quantiﬁer free formula φ =  v∈F η v, that is: T has quantiﬁer elimination.

Conversely, assume that T has quantiﬁer elimination. As notice above, T is ωcategorical thus has a unique countable model. Assume (a1,...,ap) and (b1,...,bp) are p-tuples of vertices such that f : ai  → bi is a partial isomorphism. Assume that f does not extend into an automorphism of G. Let (a1,...,aq) be a tuple of vertices of G of maximal length such that there exists bp+1,...,bq such that

###### ai  → bi is a partial isomorphism. Let aq+1 be a vertex distinct from a1,...,aq. Let φ(x1,...,xq) be the formula

(xi ∼ xj) ∧

¬(xi ∼ xj) ∧

ai∼aj

¬(ai∼aj)

¬(xi = xj)

1≤i≤q

∧ (∃y)

(xi ∼ y) ∧

¬(xi ∼ y) ∧

ai∼aq+1

¬(ai∼aq+1)

¬(xi = y)

1≤i≤q

As T has quantiﬁer elimination, there exists a quantiﬁer free formula φ such that T |= φ ↔ φ. As G |= φ(a1,...,aq) (witnessed by aq+1) it holds that G |= φ(a1,...,aq) hence G |= φ(b1,...,bq) (as ai  → bi,1 ≤ i ≤ q is a partial isomorphism) thus G |= φ(b1,...,bq). It follows that there exists bq+1 such that ai  → bi,1 ≤ i ≤ q + 1 is a partial isomorphism, contradicting the maximality of

- (a1,...,aq).


When a sequence of graphs is elementarily convergent to an ultra-homogeneous graph (i.e. to a complete theory with quantiﬁer elimination), we shall prove that FO-convergence reduces to QF-convergence. This later mode of convergence is of particular interest as it is equivalent to L-convergence.

Lemma 2.28. Let (Gn)n∈N be sequence of graphs that converges elementarily to some ultra-homogeneous graph Gˆ. Then the following properties are equivalent:

- • the sequence (Gn)n∈N is FO-convergent;
- • the sequence (Gn)n∈N is QF-convergent;
- • the sequence (Gn)n∈N is L-convergent.


Proof. As FO-convergence implies QF-convergence we only have to prove the opposite direction. Assume that the sequence (Gn)n∈N is QF-convergent. According to Lemma 2.27, for every formula φ ∈ FOp there exists a quantiﬁer free formula φ ∈ QFp such that Gˆ |= φ ↔ φ (i.e. Th(Gˆ) has quantiﬁer elimination). As Gˆ is an elementary limit of the sequence (Gn)n∈N there exists some N such that for every n ≥ N it holds that Gn |= φ ↔ φ. It follows that for every n ≥ N it holds that φ,Gn = φ,Gn hence limn→∞ φ,Gn exists. Thus the sequence (Gn)n∈N is FO-convergent.

There are not so many countable ultra-homogeneous graphs. Theorem 2.29 (Lachlan and Woodrow [56]). Every inﬁnite countable ultraho-

mogeneous undirected graph is isomorphic to one of the following:

- • the disjoint union of m complete graphs of size n, where m,n ≤ ω and at least one of m or n is ω, (or the complement of it);
- • the generic graph for the class of all countable graphs not containing Kn for a given n ≥ 3 (or the complement of it);
- • the Rado graph R (the generic graph for the class of all countable graphs).


Among them, the Rado graph R (also called “the random graph”) is characterized by the extension property: for every ﬁnite disjoint subsets of vertices A and

- B of R there exists a vertex z of R − A − B such that z is adjacent to every vertex


in A and to no vertex in B. We deduce for instance the following application of Lemma 2.28.

Example 2.30. It is known [11, 12] that for every ﬁxed k, Paley graphs of suﬃciently large order satisfy the k-extension property hence the sequence of Paley graphs converge elementarily to the Rado graph. Moreover, Paley graphs is a standard example of quasi-random graphs [23], and the sequence of Paley graphs is L-convergent to the 1/2-graphon. Thus, according to Lemma 2.28, the sequence of Paley graphs is FO-convergent.

We now relate more precisely the extension property with quantiﬁer elimination.

Definition 2.31. Let k ∈ N. A graph G has the k-extension property if, for every disjoint subsets of vertices A,B of G with size k there exists a vertex z not in A ∪ B that is adjacent to every vertex in A and to no vertex in B. In other words,

- G has the k-extension property if G satisﬁes the sentence Υk below:


(∀x1,...,x2k)

¬(xi = xj)

1≤i<j≤2k

2k

¬(xi = z) ∧

→ (∃z)

i=1

k

(xi ∼ z) ∧

i=1

2k

¬(xi ∼ z) .

i=k+1

Lemma 2.32. Let G be a graph and let p,r be integers. If G has the (p+r)-extension property then every formula φ with p free variables

and quantiﬁer rank r is equivalent, in G, with a quantiﬁer free formula.

Proof. Let φ be a formula with p free variables and quantiﬁer rank r. Let (a1,...,ap) and (b1,...,bp) be two p-tuples of vertices of G such that ai  → bi is a partial isomorphism. The (p+r)-extension properties allows to easily play a r-turns back-and-forth game between (G,a1,...,ap) and (G,b1,...,bp), thus proving that (G,a1,...,ap) and (G,b1,...,bp) are r-equivalent. It follows that G |= φ(a1,...,ap) if and only if G |= φ(b1,...,bp). Following the lines of Lemma 2.27, we deduce that there exists a quantiﬁer free formula φ such that G |= φ ↔ φ.

We now prove that random graphs converge elementarily to the countable random graphs.

Lemma 2.33. Let 1/2 > δ > 0. Assume that for every positive integer n ≥ 2 and every 1 ≤ i < j ≤ n, pn,i,j ∈ [δ,1 − δ]. Assume that for each n ∈ N, Gn is a random graph on [f(n)] where f(n) ≥ n, and where i and j are adjacent with probability pn,i,j (all these events being independent). Then the sequence (Gn)n∈N almost surely converges elementarily to the Rado graph.

Proof. Let p ∈ N and let α = δ(1 − δ). The probability that Gn |= Υp is at least 1 − (1 − αp)f(n). It follows that for N ∈ N the probability that all the graphs Gn (n ≥ N) satisfy Υp is at least 1−α−p(1−αp)f(N). According to Borel-Cantelli lemma, the probability that Gn does not satisfy Υp inﬁnitely many is zero. As this holds for every integer p, it follows that, with high probability, every elementarily converging subsequence of (Gn)n∈N converges to the Rado graph hence, with high probability, (Gn)n∈N converges elementarily to the Rado graph.

Thus we get:

Theorem 2.34. Let 0 < p < 1 and let Gn ∈ G(n,p) be independent random graphs with edge probability p. Then (Gn)n∈N is almost surely FO-convergent.

Proof. This is an immediate consequence of Lemma 2.28, Lemma 2.33 and the easy fact that (Gn)n∈N is almost surely QF-convergent.

Theorem 2.35. For every φ ∈ FOp there exists a polynomial Pφ ∈ Z[X1,...,X(p

)] such that for every sequence (Gn)n∈N of ﬁnite graphs that converges elementarily to the Rado graph the following holds:

2

If (Gn)n∈N is L-convergent to some graphon W then lim

φ,Gn = ··· Pφ((Wi,j(xi,xj))1≤i<j≤p)dx1 ...dxp.

n→∞

Proof. Assume the sequence (Gn)n∈N is elementarily convergent to the Rado graph and that it is L-convergent to some graphon W.

According to Lemma 2.27, there exists a quantiﬁer free formula φ such that

G |= (∀x1 ...xp) φ(x1,...,xp) ↔ φ(x1,...,xp)

(hence Ωφ(G) = Ω φ(G)) holds when G is the Rado graph. As (Gn)n∈N is elementarily convergent to the Rado graph, this sentence holds for all but ﬁnitely many

graphs Gn. Thus for all but ﬁnitely many Gn it holds that φ,Gn = φ,Gn . Moreover, according to Lemma 2.28, the sequence (Gn)n∈N is FO-convergent and thus the following equation holds:

lim

φ,Gn = lim

φ,Gn .

n→∞

n→∞

By using an inclusion/exclusion argument and the general form of the density of homomorphisms of ﬁxed target graphs to a graphon we deduce that there exists a polynomial Pφ ∈ Z[X1,...,X(p

)] (which depends only on φ) such that lim

2

φ,Gn = ··· Pφ((Wi,j(xi,xj))1≤i<j≤p)dx1 ...dxp. The theorem follows.

n→∞

Although elementary convergence to Rado graph seems quite a natural assumption for graphs which are neither too sparse nor too dense, elementary convergence to other ultra-homogeneous graphs may be problematic.

Example 2.36. Cherlin [21] posed the problem whether there is a ﬁnite ksaturated triangle-free graph, for each k ∈ N, where a triangle free graph is called k-saturated if for every set S of at most k vertices, and for every independent subset T of S, there exists a vertex adjacent to each vertex of T and to no vertex of S − T. In other words, Cherlin asks whether the generic countable trianglefree graph has the ﬁnite model property, that is if it is an elementary limit of a sequence of ﬁnite graphs. See [50] for more ultra-homogeneous structures deﬁned by forbidden substructures.

It is possible to extend Lemma 2.28 to sequences of graph having a non ultrahomogeneous elementary limit if we restrict FO to a smaller fragment. An example is the following:

Example 2.37. A graph G is IH-Homogeneous [18] if every partial ﬁnite isomorphism extends into an endomorphism. Let PP be the fragment of FO that consists into primitive positive formulas, that is formulas formed using adjacency, equality, conjunctions and existential quantiﬁcation only, and let BA(PP) be the minimum sub-Boolean algebra of FO containing PP.

Following the lines of Lemma 2.28 and using Theorem 2.14 and Proposition 2.13, one proves that if a sequence of graphs (Gn)n∈N converges elementarily to some IHhomogeneous inﬁnite countable graph then (Gn)n∈N is BA(PP)-convergent if and only if it is QF-convergent.

2.3.5. FO-convergence of Graphs with Bounded Maximum Degree. We now consider how full FO-convergence diﬀers to BS-convergence for sequence of graphs with maximum degree at most D. As a corollary of Theorems 2.23 and 2.16 we have:

Corollary 2.38. A sequence (Gn) of ﬁnite graphs with maximum degree at most d such that limn→∞ |Gn| = ∞ is FO-convergent if and only if it is both BSconvergent and elementarily convergent.

###### 2.4. Interpretation Schemes

In the process of this research we discovered the increasing role played by interpretations. They are described in this section.

2.4.1. Continuous Functions and Interpretations. Let X and Y be fragments of FO(κ) and FO(λ), respectively. Let f : S(B(X)) → S(B(Y )). A function f : S(B(X)) → S(B(Y )) is continuous if and only if the inverse image of an open subset of S(B(Y )) is an open subset of S(B(X)). In the case of Stone spaces (where clopen subsets generates the topology), we can further restrict our attention to clopen subsets: f will be continuous if the inverse image of a clopen subset is a clopen subset. In other words, f is continuous if there exists f∗ : B(Y ) → B(X), such that for every φ ∈ Y , the following equation holds:

f−1(K(φ)) = K(f∗(φ)).

It follows that if f is continuous then for every X-convergent sequence (An)n∈N, the sequence (f(An))n∈N is Y -convergent. Note that f∗ will be a homomorphism from B(Y ) to B(X), and that the duality between f and f∗ is nothing more the duality between Stone spaces and Boolean algebras.

The above property can be sometimes restated in terms of deﬁnable sets in structures. For a fragment X of FO and a relational structure A, a subset F ⊆ Ap is X-deﬁnable if there exists a formula φ ∈ X with free variables x1,...,xp such that

F = Ωφ(A) = {(v1,...,vp) ∈ Ap : A |= φ(v1,...,vp)}.

Let A be a κ-structure, let B be a λ-structure, and let g : Ak → B be surjective. Assume that there exists a function g∗ : Y → X such that for every φ ∈ Y with

2.4. INTERPRETATION SCHEMES 39

free variables x1,...,xp (p ≥ 0), and every vi,j ∈ A (1 ≤ i ≤ p, 1 ≤ j ≤ k) the following holds:

B |= φ(g(v1,1,...,v1,k),...,g(vp,1,...,vp,k)) ⇐⇒ A |= g∗(φ)(v1,1,...,v1,k,...,vp,1,...,vp,k)

then g∗ is a homomorphism, and thus it deﬁnes a continuous function from S(B(X)) to S(B(Y )). Note that the above formula can be restated as

Ωg∗(φ)(A) = gˆ−1(Ωφ(B)), where

gˆ((v1,1,...,vp,k)) = (g(v1,1,...,v1,k),...,g(vp,1,...,vp,k)). In other words, the inverse image of a Y -deﬁnable set of B is an X-deﬁnable set of A.

When X = FO(κ) and Y = FO(λ), the property that the inverse image of a ﬁrst-order deﬁnable set of B is a ﬁrst-order deﬁnable set of A leads to the model theoretical notion of interpretation (without parameters) of B in A. We recall now the formal deﬁnition of an interpretation.

Definition 2.39 (Interpretation). An interpretation of B in A with parameters (or without parameters, respectively) with exponent k is a surjective map from a subset of Ak onto B such that the inverse image of every set X deﬁnable in B by a ﬁrst-order formula without parameters is deﬁnable in A by a ﬁrst-order formula with parameters (or without parameters, respectively).

2.4.2. Interpretation Schemes. The main drawback of interpretations is that they only concerns two speciﬁc structures A and B. However, it is frequent that interpretations naturally generalize to a family of interpretations of λ-structures in κ-structures with the same associated homomorphism of Boolean algebras. Moreover, this homomorphism is uniquely deﬁned by the way it transforms each relation in λ (including equality) into a formula in κ and by the formula which deﬁnes the domain of the κ-structures. This can be formalized as follows.

Definition 2.40 (Interpretation Scheme). Let κ,λ be signatures, where λ has q relational symbols R1,...,Rq with respective arities r1,...,rq.

An interpretation scheme I of λ-structures in κ-structures is deﬁned by an integer k — the exponent of the interpretation scheme — a formula E ∈ FO2k(κ), a formula θ0 ∈ FOk(κ), and a formula θi ∈ FOr

ik(κ) for each symbol Ri ∈ λ, such that:

- • the formula E deﬁnes an equivalence relation of k-tuples;
- • each formula θi is compatible with E, in the sense that for every 0 ≤ i ≤ q the following property holds:


###### ) ↔ θi(y1,...,yr

E(xj,yj) θi(x1,...,xr

),

i

i

1≤j≤ri

where r0 = 1, boldface xj and yj represent k-tuples of free variables, and where θi(x1,...,xr

i,k). For a κ-structure A, we denote by I(A) the λ-structure B deﬁned as follows:

) stands for θi(x1,1,...,x1,k,...,xr

i,1,...,xr

i

- • the domain B of B is the subset of the E-equivalence classes [x] ⊆ Ak of the tuples x = (x1,...,xk) such that A |= θ0(x);
- • for each 1 ≤ i ≤ q and every v1,...,vs


i ∈ Akr

such that A |= θ0(vj) (for every 1 ≤ j ≤ ri) the following equivalence holds:

i

B |= Ri([v1],...,[vr

###### ]) ⇐⇒ A |= θi(v1,...,vr

).

i

i

From the standard properties of model theoretical interpretations (see, for instance [57] p. 180), we state the following: if I is an interpretation of λ-structures in κ-structures, then there exists a mapping ˜I : FO(λ) → FO(κ) (deﬁned by means of the formulas E,θ0,...,θq above) such that for every φ ∈ FOp(λ), and every κ-structure A, the following property holds (while letting B = I(A) and identifying elements of B with the corresponding equivalence classes of Ak):

For every [v1],...,[vp] ∈ Bp (where vi = (vi,1,...,vi,k) ∈ Ak) the following equivalence holds:

B |= φ([v1],...,[vp]) ⇐⇒ A |=˜I(φ)(v1,...,vp).

It directly follows from the existence of the mapping˜I that an interpretation scheme I of λ-structures in κ-structures deﬁnes a continuous mapping from S(B(FO(κ))) to S(B(FO(λ))). Thus, interpretation schemes have the following general property:

Proposition 2.41. Let I be an interpretation scheme of λ-structures in κstructures.

Then, if a sequence (An)n∈N of ﬁnite κ-structures is FO-convergent then the sequence (I(An))n∈N of (ﬁnite) λ-structures is FO-convergent.

We shall be mostly interested in very speciﬁc and simple types of interpretation schemes.

Definition 2.42. Let κ,λ be signatures. A basic interpretation scheme I of λ-structures in κ-structures with exponent k is deﬁned by a formula θi ∈ FOkr

(κ) for each symbol Ri ∈ λ with arity ri.

i

For a κ-structure A, we denote by I(A) the structure with domain Ak such that, for every Ri ∈ λ with arity ri and every v1,...,vr

i ∈ Ak the following equivalence holds:

I(A) |= Ri(v1,...,vr

###### ) ⇐⇒ A |= θi(v1,...,vr

).

i

i

It is immediate that every basic interpretation scheme I deﬁnes a mapping ˜I : FO(λ) → FO(κ) such that for every κ-structure A, every φ ∈ FOp(λ), and every v1,...,vp ∈ Ak the following equivalence holds:

I(A) |= φ(v1,...,vp) ⇐⇒ A |=˜I(φ)(v1,...,vp) and

qrank(˜I(φ)) ≤ k(qrank(φ) + max

qrank(θi)).

i

It follows that for every κ-structure A, every φ ∈ FOp(λ), the following equation holds:

Ωφ(I(A)) = Ω˜I(φ)(A). In particular, if A is a ﬁnite structure, the following equation holds:

φ,I(A) = ˜I(φ),A .

CHAPTER 3

## Modelings for Sparse Structures

###### 3.1. Relational Samples Spaces

The notion of relational sample space is a strenghtening of the one of relational structure, where it is required that the domain shall be endowed with a suitable structure of a (nice) measurable space.

###### 3.1.1. Deﬁnition and Basic Properties.

Definition 3.1. Let λ be a signature. A λ-relational sample space is a λstructure A, whose domain A is a standard Borel space with the property that every ﬁrst-order deﬁnable subset of Ap is measurable. Precisely, for every integer p, and every φ ∈ FOp(λ), denoting

Ωφ(A) = {(v1,...,vp) ∈ Ap : A |= φ(v1,...,vp)}, it holds that Ωφ(A) ∈ ΣpA, where ΣA is the Borel σ-algebra of A.

Note, that in the case of graphs, every relational sample space is a Borel graph (that is a graph whose vertex set is a standard Borel space and whose edge set is Borel), but the converse is not true.

Lemma 3.2. Let λ be a signature, let A be a λ-structure, whose domain A is a standard Borel space with σ-algebra ΣA.

Then the following conditions are equivalent:

- (a) A is a λ-relational sample space;
- (b) for every integer p ≥ 0 and every φ ∈ FOp(λ), it holds that Ωφ(A) ∈ ΣpA;
- (c) for every integer p ≥ 1 and every φ ∈ FOlocalp (λ), it holds that Ωφ(A) ∈ ΣpA;
- (d) for all integers p,q ≥ 0, every φ ∈ FOp+q(λ), and every a1,...,aq ∈ Aq the set {(v1,...,vp) ∈ Ap : A |= φ(a1,...,aq,v1,...,vp)}


belongs to ΣpA.

Proof. Items (a) and (b) are equivalent by deﬁnition. Also we obviously have the implications (d) ⇒ (b) ⇒ (c). That (c) ⇒ (b) is a direct consequence of Gaifman locality theorem, and the implication (b) ⇒ (d) is a direct consequence of Fubini-Tonelli theorem.

Lemma 3.3. Let A be a relational sample space, let a ∈ A, and let Aa be the connected component of A containing a.

Then Aa has a measurable domain and, equipped with the σ-algebra of the Borel sets of A included in Aa, it is a relational sample space.

41

Proof. Let φ ∈ FOlocalp and let

X = {(v1,...,vp) ∈ Apa : Aa |= φ(v1,...,vp)}. As φ is local, there is an integer D such that the satisfaction of φ only depends on the D-neighborhoods of the free variables.

For every integer n ∈ N, denote by B(A,a,n) the substructure of A induced by all vertices at distance at most n from a. By the locality of φ, for every v1,...,vp

- at distance at most n from a the following equivalence holds: Aa |= φ(v1,...,vp) ⇐⇒ B(A,a,n + D) |= φ(v1,...,vp).


However, it is easily checked that there is a local ﬁrst-order formula ϕn ∈ FOlocalp+1 such that for every v1,...,vp the following equivalence holds:

p

B(A,a,n+D) |= φ(v1,...,vp)∧

i=1

dist(a,vi) ≤ n ⇐⇒ A |= ϕn(a,v1,...,vp).

By Lemma 3.2, it follows that the set Xn = {(v1,...,vn) ∈ A : A |= ϕn(a,v1,...,vp)} is measurable. As X = n∈N Xn, we deduce that X is measurable (with respect to ΣpA). In particular, Aa is a Borel subset of A hence Aa, equipped with the σ-algebra ΣA

###### of the Borel sets of A included in Aa, is a standard Borel set. Moreover, it is immediate that a subset of Apa belongs to ΣpA

a

if and

a

only if it belongs to ΣpA. Hence, every subset of Apa deﬁned by a local formula is measurable with respect to ΣpA

. By Lemma 3.2, it follows that Aa is a relational sample space.

a

3.1.2. Interpretations of Relational Sample Spaces. An elementary interpretation with parameter amounts to distinguishing a single element, the parameter, by adding a new unary symbol to the signature (e.g. representing a root).

Lemma 3.4. Let A be a λ-relational sample space, let λ+ be the signature obtained from λ by adding a new unary symbol M and let A+ be obtained from A by marking a single a ∈ A (i.e. a is the only element x of A+ = A such that A+ |= M(x)).

Then A+ is a relational sample space. Proof. Let φ ∈ FOp(λ+). There exists φ ∈ FOp+1(λ) such that for every

x1,...,xp ∈ A the following equivalence holds:

A+ |= φ(x1,...,xp) ⇐⇒ A |= φ(a,x1,...,xp).

According to Lemma 3.2, the set of all (x1,...,xp) such that A |= φ(a,x1,...,xp) is measurable. It follows that A+ is a relational sample space.

Lemma 3.5. Every injective ﬁrst-order interpretation (with or without parameters) of a relational sample space is a relational sample space.

Precisely, if f is an injective ﬁrst-order interpretation of a λ-structure B in a κ-relational sample space A and if we deﬁne

ΣB = {X ⊆ B : f−1(X) ∈ ΣkA}, then (B,ΣB) is a relational sample space.

Proof. According to Lemma 3.4, we can ﬁrst mark all the parameters and reduce to the case where the interpretation has no parameters.

Let D be the domain of f. As B is ﬁrst-order deﬁnable in B, D is ﬁrst-order

deﬁnable in A hence D ∈ ΣkA. Then D is a Borel sub-space of Ak. As f is a bijection from D to B, we deduce that (B,ΣB) is a standard Borel space.

Moreover, as the inverse image of every ﬁrst-order deﬁnable set of B is ﬁrstorder deﬁnable in A, we deduce that (B,ΣB) is a λ-relational sample space.

3.1.3. Disjoint union. Let Hi be λ-relational sample spaces for i ∈ I ⊆ N. We deﬁne the disjoint union

###### H =

###### Hi

i∈I

of the Hi’s as the relational structure, which is the disjoint union of the Hi’s endowed with the σ-algebra ΣH = { i Xi : Xi ∈ ΣH

i}.

Lemma 3.6. Let Hi be λ-relational sample spaces for i ∈ I ⊆ N. Then H = i∈I Hi is a λ-relational sample space, in which every Hi is measurable.

Proof. We consider the signature λ+ obtained from λ by adding a new binary relation , and the basic interpretation scheme I1 of λ+-structures in λ-structures corresponding to the addition of the new relation by the formula θ = 1. This means that for every λ-structure A it holds that I1(A) |= (∀x,y) (x,y). Let H+i = I1(Hi).

Let H+ = i∈I H+i . Clearly, ΣH+ = ΣH and (H,ΣH) is a standard Borel space. Moreover, by construction, each Hi is measurable.

Let φ ∈ FOp(λ). First notice that for every (v1,...,vp) ∈ Hp+q (which is also (H+)p+q) it holds that Ωφ(H) = Ωφ(H+), that is:

H |= φ(v1,...,vp) ⇐⇒ H+ |= φ(v1,...,vp).

It follows from Lemma 2.25 that the set Ωφ(H+) may be obtained by Boolean operations, products, and coordinate permutations from sets deﬁned by -local formulas (which we introduced in Section 2.3.3). As all these operations preserve measurability, we can assume that φ is -local. Then Ωφ(H+) is the union of the sets Ωφ(Hi). All these sets are measurable (as Hi is a modeling) thus their union is measurable (by construction of ΣH). It follows that H+ is a relational sample space, and so is H (every ﬁrst-order deﬁnable set of H is ﬁrst-order deﬁnable in H+).

###### 3.2. Modelings

We introduced a notion of limit objects — called modelings — for sequences of sparse graphs and structures, which is a natural generalization of graphings. These limit objects are deﬁned by considering a probability measure on a relational sample space. In this section, we show that the most we can expect is that modelings are limit objects for sequence of sparse structures, and we conjecture that an unavoidable qualitative jump occurs for notions of limit structures, which coincides with the nowhere dense/somewhere dense frontier (see Conjecture 1.1).

3.2.1. Deﬁnition and Basic Properties. Recall Deﬁnitions 1.4 and 1.6: a λ-modeling A is a λ-relational sample space equipped with a probability measure (denoted νA), and the Stone pairing of φ ∈ FO(λ) and a λ-modeling A is φ,A = νAp (Ωφ(A)). Notice that it follows (by Fubini’s theorem) that it holds that

φ(A)(x)dνAp (x)

φ,A =

1Ω

x∈Ap

= ··· 1Ω

φ(A)(x1,...,xp) dνA(x1) ... dνA(xp).

Then, generalizing Deﬁnition 1.7, we extend the notion of X-convergence to modelings:

Definition 3.7 (modeling X-limit). Let X be a fragment of FO(λ). If an X-convergent sequence (An)n∈N of λ-modelings satisﬁes

(∀φ ∈ X) φ,L = lim

φ,An for some λ-modeling L, then we say that L is a modeling X-limit of (An)n∈N.

n→∞

A λ-modeling A is weakly uniform if all the singletons of A have the same measure. Clearly, every ﬁnite λ-structure A can be identiﬁed with the weakly uniform modeling obtained by considering the discrete topology on A. This identiﬁcation is clearly consistent with our deﬁnition of the Stone pairing of a formula and a modeling.

In the case where a modeling A has an inﬁnite domain, the condition for A to be weakly uniform is equivalent to the condition for νA to be atomless. This property is usually fulﬁlled by modeling X-limits of sequences of ﬁnite structures.

Lemma 3.8. Let X be a fragment of FO that includes FO0 and the formula (x1 = x2). Then every modeling X-limit of weakly uniform modelings is weakly uniform.

Proof. Let φ be the formula (x1 = x2). Notice that for every ﬁnite λ-structure A it holds that φ,A = 1/|A| and that for every inﬁnite weakly uniform λ-structure it holds that φ,A = 0.

Let L be a modeling X-limit of a sequence (An)n∈N. Assume limn→∞ |An| = ∞. Assume for contradiction that νL has an atom {v} (i.e. νL({v}) > 0). Then

φ,L ≥ νL({v})2 > 0, contradicting limn→∞ φ,An = 0. Hence νL is atomless.

Otherwise, |L| = limn→∞ |An| < ∞ (as L is an elementary limit of (An)n∈N). Let N = |L|. Label v1,...,vN the elements of L and let pi = νL({vi}). Then

N

N

2

1 N

1 N

φ,L N −

1 N2

p2i −

pi

=

i=1

i=1

1 N2

limn→∞ φ,An N −

=

= 0 Thus pi = 1/N for every i = 1,...,N.

Corollary 3.9. Every modeling FOlocal2 -limit of ﬁnite structures is weakly uniform.

Lemma 3.10. Let X be a fragment that includes all quantiﬁer free formulas. Assume L is a modeling X-limit of a sequence (Gn)n∈N of graphs with |Gn| →

∞. Let νL be the completion of the measure νL.

Then there is at least one mod 0 isomorphism f : [0,1] → (L,νL), and for every such f the graphon W deﬁned by

(x1∼x2)(L)(f(x),f(y)) (for x,y in the domain of f, and W(x,y) = 0 elsewhere) is a random-free graphon L-limit of (Gn)n∈N.

W(x,y) = 1Ω

Proof. Considering the formula x1 = x2, we infer that νL is atomless. This measure is also atomless and turns L into a standard probability space. According to the isomorphism theorem, all atomless standard probability spaces are mutually mod 0 isomorphic hence there is at least one mod 0 isomorphism f : [0,1] → (L,νL) ([0,1] is considered with Lebesgue measure).

Fix such a mod 0 isomorphism f, deﬁned on [0,1] \ N1, with value on L \ N2

- (where N1 and N2 are nullsets). For every Borel measurable function g : Ln → [0,1], deﬁne gf by gf(x1,...,xn) = g(f(x1),...,f(xn)) if xi ∈/ N1 for every 1 ≤ i ≤ n and gf(x1,...,xn) = 0 otherwise. Then it holds that


gf(x1,...,xn)dx1 ...dxn =

[0,1]n

g(v1,...,vn)dνL(v1)...dνL(vn)

Ln

=

g(v1,...,vn)dνL(v1)...dνL(vn).

Ln

It follows that for every ﬁnite graph F with vertex set {1,...,n}, denoting by φF the formula ij∈E(F)(xi ∼ xj), it holds that

t(F,W) =

W(xi,xj)dx1 ...dxn

[0,1]n ij∈E(F)

=

Ln ij∈E(F)

###### 1Ω

(x1∼x2)(L)(vi,vj)dνL(v1)...dνL(vn)

=

###### 1Ω

φF (L)(v1,...,vn)dνL(v1)...dνL(vn)

Ln

= φF,L

= lim

φF,Gn

n→∞

= lim

t(F,Gn).

n→∞

Hence W is a graphon L-limit of (Gn)n∈N. As W is {0,1}-valued, it is (by deﬁnition) random-free.

We deduce the following limitation of modelings as limit objects. Corollary 3.11. Let X be a fragment that includes all quantiﬁer free formu-

las.

Assume (Gn)n∈N is an X-convergent sequence of graphs with unbounded order, which is L-convergent to some non random-free graphon W. Then (Gn)n∈N has no modeling X-limit.

Let us now give some example stressing that the nullsets of the mod 0 isomorphism f can be quite large, making L and W look quite diﬀerent. We now give an example in the more general setting of directed graphs and non-symmetric graphons.

Example 3.12. Let Tn be the transitive tournament of order n, that is the directed graph on {1,...,n} deﬁned from the natural linear order <n on {1,...,n} by i → j if i < j. This sequence is obviously FO-convergent.

It is not diﬃcult to construct a modeling FO-limit of ( Tn)n∈N: Let

L = ({0} × Z+) ∪ (]0,1[×Z) ∪ ({1} × Z−), with the Borel σ-algebra Σ generated by the product topology of Z (with discrete topology) and R (with usual topology). On L we deﬁne a linear order <L by (α,i) <L (β,j) if α < β or (α = β) and (i < j). That (L,Σ) is a relational sample space follows from the o-minimality of ([0,1],<). The measure νL can be deﬁned as the product of Lebesgue measure on [0,1] by any probability measure on Z. For instance, for every B ∈ Σ we let νL(B) = λ(B ∩ ([0,1] × {0})), where λ is Lebesgue measure. It is not diﬃcult to check that L is indeed a modeling FO-limit of ({1,...,n},<n) Tn.

In this case, a mod 0 isomorphism f deﬁned on [0,1] with values in L \ N2

- (where N2 is a nullset) can be deﬁned by f(x) = (x,0). The null set N2, although very large, is clearly a νL-nullset, and the obtained (non symmetric) random-free graphon W : [0,1] × [0,1] → [0,1] is simply deﬁned by


1 if x < y 0 otherwise.

W(x,y) =

Note that W corresponds to [0,1] with its natural order <. This order is clearly an L-limit of <n (but not an elementary limit, as it is dense although no ﬁnite order is).

In the spirit of Lemma 3.2, we propose the following problems:

- Problem 3.1. Let L be a modeling FO-limit of a sequence (An)n∈N of λ-

structures, and let v ∈ L. Does there exist a sequence (vn)n∈N such that vn ∈ An and such that the rooted modeling (L,v) is a modeling FO-limit of the rooted structures (An,vn)?

- Problem 3.2. Let L be a modeling FO-limit of a sequence (An)n∈N of λ-

structures. Does there exist f : L → i∈N An such that for every v1,...,vk ∈ L, the k-rooted modeling (L,v1,...,vk) is a modeling FO-limit of the k-rooted structures (An,f(v1)n,...,f(vk)n)?

- 3.2.2. Interpretation Schemes applied to Modelings. Basic interpreta-


tion schemes will be an eﬃcient tool to handle modelings. Let I be an interpretation scheme I of λ-structures in κ-structures. We have seen that I can be extended to a mapping from κ-relational sample space to λ-relational sample space. In the case where I is a basic interpretation scheme, we further extend I to a mapping from κ-modeling to λ-modeling: For a κ-modeling A, the λ-modeling B = I(A) is the modeling on the image relational sample space of A with the probability measure νB = νA. This is formalized as follows:

Lemma 3.13. Let I be a basic interpretation scheme I of λ-structures in κstructures with exponent k. Extend the deﬁnition of I to a mapping of κ-modeling to λ-modeling by setting νI(A) = νAk . Then for every κ-modeling A and every φ ∈ FO(λ) the following equation holds:

φ,I(A) = ˜I(φ),A .

Proof. Let A be a κ-modeling. For every φ ∈ FOp(λ) the following equation holds:

Ωφ(I(A)) = Ω˜I(φ)(A) thus φ,I(A) = νIp(A)(Ωφ(I(A))) = νAkp(Ω˜I(φ)(A)) = ˜I(φ),A .

Remark 3.14. If the basic interpretation scheme I is deﬁned by quantiﬁer free formulas only, then it is possible to deﬁne I in such a way that for every φ ∈ FO(λ) it holds that qrank( I(φ)) ≤ qrank(φ).

The following strengthening of Proposition 2.41 in the case where we consider a basic interpretation scheme is a clear consequence of Lemma 3.13.

Proposition 3.15. Let I be a basic interpretation scheme of λ-structures in κ-structures.

If L is a modeling FO-limit of a sequence (An)n∈N of κ-modelings then I(L) is a modeling FO-limit of the sequence (I(An))n∈N.

Remark 3.16. Let us mention that interpretations can be used to generalize graphings to bounded degree k-regular hypergraphs, and even to bounded degree relational structures: Deﬁne the degree of an element of a λ-structure as the number of relations it belongs to. Following the lines of Proposition 3.15 and considering a natural interpretation of λ-structures with maximum degree D in colored (multi)graphs with maximum degree max(D,r) (where r is the maximum arity of a relation in λ) we deduce from Corollary 2.38 that classes of relational structures with bounded maximum degree have modeling FO-limits.

Lemma 3.17. Let p ∈ N be a positive integer, let L be a modeling, and let pTp

: Lp → S(B(FOp(λ))) be the function mapping (v1,...,vp) ∈ Lp to the complete theory of (L,v1,...,vp) (that is the set of the formulas ϕ ∈ FOp(λ) such that L |= ϕ(v1,...,vp)).

L

Then pTp

is a measurable map from (Lp,ΣpL) to S(B(FOp(λ))) (with its Borel

L

σ-algebra). Let (An)n∈N be an FOp(λ)-convergent sequence of ﬁnite λ-structures, and let µp be the associated limit measure (as in Theorem 2.6).

Then L is an FOp(λ)-limit modeling of (An)n∈N if and only if µp is the pushforward of the product measure νLp by the measurable map pTp

, that is: pTp

L

L ∗(νLp) = µp.

Proof. Recall that the clopen sets of S(B(FOp(λ))) are of the form K(φ) for φ ∈ FOp(λ) and that they generate the topology of S(B(FOp(λ))) hence also its Borel σ-algebra.

That pTp

is measurable follows from the fact that for every φ ∈ FOp the preimage of K(φ), that is pTp

L

−1(K(φ)) = Ωφ(L), is measurable.

L

Assume that L is an FOp(λ)-limit modeling of (An)n∈N. In order to prove that pTp

L ∗(νLp) = µp, it is suﬃcient to check it on sets K(φ):

φ,An = φ,L = νLp(pTp

−1(K(φ))). Conversely, if pTp

µp(K(φ)) = lim

L

n→∞

L ∗(νLp) = µp then for every φ ∈ FOp(λ) the following equation holds:

φ,L = νLp(pTp

−1(K(φ))) = µp(K(φ)) = limn→∞ φ,An , hence L is an FOp(λ)-limit modeling of (An)n∈N.

L

If (X,Σ) is a Borel space with a probability measure ν, it is standard to deﬁne the product σ-algebra Σω on the inﬁnite product space XN, which is generated by cylinder sets of the form

R = {f ∈ XN : f(i1) ∈ Ai

,...,f(ik) ∈ Ai

k} for some k ∈ N and Ai

1

k ∈ Σ. The measure νω of the cylinder R deﬁned above is then

,...,Ai

1

k

νω(R) =

ν(Ai

).

j

j=1

By Kolmogorov’s Extension Theorem, this extends to a unique probability measure on Σω (which we still denote by νω). We summarize this as the following (see also Fig. 1).

: LN → S(B(FO(λ))) be the function which assigns to f ∈ LN the point of S(B(FO(λ))) corresponding to the set {φ : L |= φ(f(1),...,f(p)), where Fv(φ) ⊆ {1,...,p}}.

Theorem 3.18. let L be a modeling, and let ωTp

L

Then ωTp

is a measurable map. Let (An)n∈N be an FO(λ)-convergent sequence of ﬁnite λ-structures, and let µ be the associated limit measure (see Theorem 2.4).

L

Then L is an FO(λ)-limit modeling of (An)n∈N if and only if ωTp

L ∗(νLω) = µ.

Fig. 1 visualizes Lemma 3.17 and Theorem 3.18.

Remark 3.19. We could have considered free variables to be indexed by Z instead of N. In such a context, natural shift operations S and T act respectively on the Stone space S of the Lindenbaum–Tarski algebra of FO(λ), and on the space LZ of the mappings from Z to a λ-modeling L. If (An)n∈N is an FO-convergent sequence with limit measure µ on S, then (S,µ,S) is a measure-preserving dynamical system. Also, if νZ is the product measure on A, (AZ,ν,T) is a Bernoulli scheme. Then, the condition of Theorem 3.18 can be restated as follows: the modeling L is a modeling FO-limit of the sequence (An)n∈N if and only if (S,µ,S) is a factor of (AZ,νZ,T). This setting leads to yet another interpretation of our result, which we hope will be treated elsewhere.

S(B(FO0)) with δT

S2

L2 with νL2

L with νL

L1Tp

L2Tp

S2

S(B(FO1)) with µ1

S(B(FO2)) with µ2

S2

S(B(FO1))2 with µ21

Sp

Sω

###### LN with νLω

Lp with νLp

. . .

LpTp

ωLTp

Sp

Sω

S(B(FOp)) with µp

S(B(FO)) with µ

. . .

Sp

Sω

S(B(FO1))N with µω1

S(B(FO1))p with µp1

. . .

Figure 1. Pushforward of measures

3.2.3. Component-Local Formulas. The basic observation is that for local formulas, we can reduce the Stone pairing to components.

Lemma 3.20. Let A be a λ-modeling and component relation . Let ψ ∈ FOp(λ) be a -local formula of A.

Assume A has countably many connected components {Bi}i∈Γ. Let Γ+ be the set of indexes i such that νA(Bi) > 0. For i ∈ Γ+ we equip Bi with the σ-algebra ΣB

###### is restriction of ΣA to Bi and, for X ∈ ΣB

###### and the probability measure νB

###### , where ΣB

i

i

i

###### , νB

(X) = νA(X)/νA(Bi). Then ψ,A =

i

i

νA(Bi)p ψ,Bi .

i∈Γ

Proof. First note that each connected component of A is measurable: let Bi be a connected component of A and let a ∈ Bi. Then Bi = {x ∈ A : A |= (x,a)} hence Bi is measurable as A is a relational sample space. Let Y = {(v1,...,vp) ∈ Ap : A |= ψ(v1,...,vp)}. Then ψ,A = νAp (Y ). As ψ is -local, it also holds that Y = i∈Γ Yi, where Yi = {(v1,...,vp) : Bi |= ψ(v1,...,vp)} = Y ∩ Bip. As Bi ∈ ΣA and Y ∈ ΣpA, it follows that Yi ∈ ΣpA and (by countable additivity) it holds that

ψ,A = νAp (Y ) =

νAp (Yi) =

νA(Bi)pνBp

νA(Bi)p ψ,Bi .

(Yi) =

i

i∈Γ

i∈Γ+

i∈Γ

Corollary 3.21. Let A be a ﬁnite λ-structure with component relation . Let ψ ∈ FOp(λ) be a -local formula of A.

Let B1,...,Bn be the connected components of A. Then ψ,A =

n

p

|Bi| |A|

ψ,Bi .

i=1

We are now ready to reduce Stone pairing of local formulas to Stone pairings with -local formulas on connected components.

###### Theorem 3.22. Let p ∈ N and φ ∈ FOlocalp (λ). Then there exist -local formulas ξi,j ∈ FOlocalq

###### (1 ≤ i ≤ n, j ∈ Ii) with qrank(ξi,j) ≤ qrank(φ) such that for each i, j∈I

i,j

qi,j = p and, for every modeling A with component relation and countable set of connected components {Bk}k∈Γ, the following equation holds:

i

n

νA(Bk)q

φ,A =

ξi,j,Bk .

i,j

i=1 j∈Ii k∈Γ

Proof. This is a direct consequence of Lemmas 2.25 and 3.20. The case of sentences can be handled easily by limited counting. For a set X

and an integer m, deﬁne

Bigm(X) =

1 if |X| ≥ m 0 otherwise.

Lemma 3.23. Let θ ∈ FO0(λ).

Then there exist formulas ψ1,...,ψs ∈ FOlocal1 with quantiﬁer rank at most q(qrank(θ)), integers m1,...,ms ≤ qrank(θ), and a Boolean function F such that for every λ-structure A with component relation and connected components Bi (i ∈ I), the property A |= θ is equivalent to

({i,Bi |= (∃x)ψs(x)})) = 1.

###### ({i,Bi |= (∃x)ψ1(x)}),...,Bigm

F(Bigm

s

1

Proof. Indeed, it follows from the Gaifman locality theorem (Theorem 2.21) that — in the presence of a component relation — every sentence θ with quantiﬁer rank r can be written as a Boolean combination of sentences θk of the form

∃y1 ...∃ym

¬ (yi,yj) ∧

ψk(yi)

k

1≤i<j≤mk

1≤i≤mk

where ψk is -local, mk ≤ qrank(θ), and qrank(ψk) ≤ q(qrank(θ)), for some ﬁxed function q. As A |= θk if and only if Bigm

({i,Bi |= (∃x)ψk(x)}) = 1, the lemma follows.

k

3.2.4. Convex Combinations of Modelings. In several contexts, it is clear when the disjoint union of converging sequences forms a converging sequence. If two graph sequences (Gn)n∈N and (Hn)n∈N are L-convergent or BS-convergent, it is clear that the sequence (Gn ∪ Hn)n∈N is also convergent, provided that the limit

|Gn|/(|Gn| + |Hn|)

lim

n→∞

exists. The same applies if we merge a countable set of L-convergent (resp. BSconvergent) sequences (Hn,i)n∈N (where i ∈ N), with the obvious restriction that for each i ∈ N all but ﬁnitely many Hn,i are empty graphs.

###### We shall see that the possibility of merging a countable set of converging sequences to FOlocal-convergence will need a further assumption, namely the following equality:

|Gn,i| | j Gn,j|

lim

= 1. The importance of this assumption is illustrated by the next example. Example 3.24. Let Nn = 22

n→∞

i

n

(so that N(n) is divisible by 2i for every 1 ≤ i ≤ 2n). Consider sequences (Hn,i)n∈N of edgeless black and white colored graphs where Hn,i is

- • empty if i > 2n,
- • the edgeless graph with (2−i + 2−n)Nn white vertices and 2−iNn black vertices if n is odd,
- • the edgeless graph with (2−i + 2−n)Nn black vertices and 2−iNn white vertices if n is even.


For each i ∈ N, the sequence (Hn,i)n∈N is obviously L-convergent (and even FOconvergent) as the proportion of white vertices in Hn,i tends to 1/2 as n → ∞. The order of Gn = i∈N Hn,i is 3Nn and |Hn,i|/|Gn| tends to 32 ·2−i as n goes to inﬁnity. However the sequence (Gn)n∈N is not L-convergent (hence not FOlocal-convergent). Indeed, the proportion of white vertices in Gn is 2/3 if n is odd and 1/3 is n is even.

Hence, we are led to the following deﬁnition. Definition 3.25 (Convex combination of Modelings). Let Hi be λ-modelings

for i ∈ I ⊆ N and let (αi)i∈I be positive real numbers such that i∈I αi = 1.

Let H = i∈I Hi be the relational sample space obtained as the disjoint union of the Hi. We endow H with the probability measure νH(X) = i αiνH

(X ∩Hi).

i

Then H is the convex combination of modelings Hi with weights αi and we denote it by i∈I(Hi,αi).

Lemma 3.26. Let Hi be λ-modelings for i ∈ I ⊆ N and let (αi)i∈I be positive real numbers such that i∈I αi = 1. Let H = i∈I(Hi,αi) Then

- (1) H is a modeling, each Hi is measurable and νH(Hi) = αi holds for every i ∈ I;
- (2) if all the Hi are weakly uniform and either all the Hi are inﬁnite or all


the Hi are ﬁnite, I is ﬁnite, and αi = |Hi|/ i∈I |Hi|, then H is weakly uniform.

Proof. According to Lemma 3.2, H is a relational sample space, in which each Hi is measurable. That νH(Hi) = αi immediately follows from the deﬁnition of νH.

Assume that all the Hi are weakly uniform. If all the Hi are ﬁnite, I is ﬁnite, and αi = |Hi|/ i∈I |Hi|, then H is the modeling associated to the union of the Hi hence it is weakly uniform. Otherwise all the Hi are inﬁnite, hence all the νH

i

are atomless, νH is atomless, and H is weakly uniform.

Lemma 3.27. Let p ∈ N and φ ∈ FOlocalp (λ). Then there exist local formulas ξi,j ∈ FOlocalq

###### (1 ≤ i ≤ n, j ∈ Ii) with qrank(ξi,j) ≤ qrank(φ) such that for each i, j∈I

i,j

###### qi,j = p and, for every countable

i

set of modelings Ak and weights αk (k ∈ Γ ⊆ N and k αk = 1) the following equation holds, denoting A = i∈Γ(Ai,αi):

n

αkqi,j ξi,j,Ak .

φ,A =

i=1 j∈Ii k∈Γ

Proof. Considering, as above, the combination A+ = i∈Γ(A+i ,αi), where

A+i is obtained by the basic interpretation scheme adding a full binary relation , the result is an immediate consequence of Theorem 3.22.

For λ-modelings A and B, and p,r ∈ N deﬁne

A − B localp,r = sup{| φ,A − φ,B | : φ ∈ FOlocalp (λ),qrank(φ) ≤ r}.

The following lemma relates precisely how close Stone pairings on two combinations of modelings are, when the modelings and weights involved in the combinations deﬁne close Stone pairings.

Lemma 3.28. Let p,r ∈ N, and let Γ ⊆ N. For k ∈ Γ, let Ak,Bk be λmodelings, and let αk,βk be non-negative weights with k αk = k βk = 1.

Let A = i∈Γ(Ai,αi) and B = i∈Γ(Bi,βi). Then there exists a constant cr,p (which depends only on λ,r, and p) such that it holds that

A − B localp,r ≤ cr,p α − β 1 +

αk Ak − Bk localp,r

k∈Γ

Ai − Bi localp,r .

≤ cr,p α − β 1 + sup i∈Γ

Proof. Let φ ∈ FOlocalp (λ) with qrank(φ) ≤ r. According to Lemma 3.27 there exist local formulas ξi,j ∈ FOlocalq

###### (λ) (1 ≤ i ≤ n, j ∈ Ii) with qrank(xii,j) ≤ r such that for each i, j∈I

i,j

qi,j = p and, for every countable set of modelings Ck and weights γk (k ∈ Γ and k γk = 1) the following equation holds, denoting C = i∈Γ(Ci,γi):

i

n

φ,C =

ξi,j,C , with ξi,j,C =

i=1 j∈Ii

γkqi,j ξi,j,Ck .

k∈Γ

As there are only ﬁnitely many non-equivalent formulas in FOlocalp (λ) with quantiﬁer rank at most r, there is a constant Nr,p such that n ≤ Nr,p.

We have

n

| φ,A − φ,B | ≤

ξi,j,A −

i=1 j∈Ii

j∈Ii

ξi,j,B .

Note that if ai,bi ∈ [0,1] then we get easily

k

k

k

k

k

bi = (a1 − b1)

ai −

ai −

ai + b1

bi

i=1

i=1

i=2

i=2

i=2

k

k

ai −

≤ |a1 − b1| +

bi

i=2

i=2

k

≤

|ai − bi|.

i=1

Hence, as for every 1 ≤ i ≤ n and every j ∈ I it holds that 0 ≤ ξi,j,A ≤ 1 and 0 ≤ ξi,j,B ≤ 1, we have

n

ξi,j,A − ξi,j,B

| φ,A − φ,B | ≤

i=1 j∈Ii

n

βkqi,j ξi,j,Bk

αkqi,j ξi,j,Ak −

≤

i=1 j∈Ii k∈Γ

k∈Γ

n

αkqi,j ξi,j,Ak − βkqi,j ξi,j,Bk .

≤

i=1 j∈Ii k∈Γ

Thus, as qi,j ≥ 1 and as Stone pairings  ·, ·  have value in [0,1], the following inequality holds (denoting cr,p = pNr,p):

A − B localp,r ≤ cr,p

|αk − βk| +

k∈Γ

αk Ak − Bk localp,r .

k∈Γ

Lemma 3.29. Let p,r ∈ N, let A,B be λ-modeling, with connected components Ak,k ∈ ΓA and Bk,k ∈ ΓB (where ΓA and ΓB can be inﬁnite non-countable).

Then the following inequality holds

A − B localp,r < cr,p sup

νB(Bk) + A − B local1,r .

νA(Ak) + sup

k∈ΓA

k∈ΓB

Proof. Let φ ∈ FOlocalp (λ) with qrank(φ) ≤ r. The following equation holds

n

φ,A =

ξi,j,A .

i=1 j∈Ii

It is clear that if ζi,j is component-local and qi,j > 1 then ξi,j,A < sup

νA(Ak).

k∈ΓA

Let X be the set of the integers 1 ≤ i ≤ n such that there is j ∈ Ii such that qi,j > 1, and let Y be the complement of X in {1,...,n}. Then

φ,A −

ξi,j,A < cr,p sup

νA(Ak).

k∈ΓA

i∈Y j∈Ii

Similarly, it holds that φ,B −

ξi,j,B < cr,p sup

νB(Bk).

k∈ΓB

i∈Y j∈Ii

Thus the statement follows from

ξi,j,A −

###### ξi,j,B ≤

ξi,j,A −

ξi,j,B

j∈Ii

i∈Y j∈Ii

i∈Y j∈Ii

i∈Y j∈Ii

ξi,j,A − ξi,j,B

≤

i∈Y j∈Ii

≤ cr,p A − B local1,r .

Theorem 3.30. Let p ∈ N, let I ⊆ N and, for each i ∈ I let (Ai,n)n∈N be an FOlocalp (λ)-convergent sequence of λ-modelings and let (ai,n)n∈N be a convergent sequence of non-negative real numbers, such that i∈I ai,n = 1 holds for every n ∈ N, and such that i∈I limn→∞ ai,n = 1.

Then the sequence of convex combinations i∈I(Ai,n,ai,n) is FOlocalp (λ)convergent.

Proof. If I is ﬁnite, then the result follows from Lemma 3.27. Hence we can assume I = N.

Let φ ∈ FOlocalp , let q ∈ N, and let > 0 be a positive real. Assume that for each i ∈ N the sequence (Ai,n)n∈N is FOlocalp -convergent and that (ai,n)n∈N is a convergent sequence of non-negative real numbers, such that i ai,n = 1 holds for every n ∈ N. Let αi = limn→∞ ai,n, let di = limn→∞ φ,Ai,n , and let C be such that Ci=1 αi > 1 −  /4. There exists N such that for every n ≥ N and every i ≤ C it holds that |an,i − αi| <  /4C and |aqi,n φ,Ai,n − αiqdi| <  /2C. Thus

C i=1 aqi,n φ,Ai,n − Ci=1 αiqdi <  /2 and i>C+1 ai,n <  /2. It follows that for

any n ≥ N the following inequality holds

###### aqi,n φ,Ai,n −

αiqdi ≤ max

i>C+1

i>C+1

aqi,n,

αiqdi <  /2

i>C+1

i>C+1

hence | i aqi,n φ,Ai,n − i αiqdi| < .

For every ψ ∈ FOlocalp , the expression appearing in Lemma 3.27 for the expansion of φ, i(Ai,n,ai,n) is a ﬁnite combination of terms of the form i aqi,ni,n φ,Ai,n , where qi,n ∈ N and φ ∈ FOlocalp . It follows that the value

φ, i(Ai,n,ai,n) converges as n grows to inﬁnity. Hence ( i(Ai,n,ai,n))n∈N is FOlocalp -convergent.

Corollary 3.31. Let p ≥ 1 and let (An)n∈N be a sequence of ﬁnite λstructures.

Assume An be the disjoint union of Bn,i (i ∈ N) where all but a ﬁnite number of Bn,i are empty. Let an,i = |Bn,i|/|An|. Assume further that:

- • for each i ∈ N, the limit αi = limn→∞ an,i exists,
- • for each i ∈ N such that αi = 0, the sequence (Bn,i)n∈N is FOlocalp convergent,
- • the following equation holds:


αi = 1.

i≥1

Then, the sequence (An)n∈N is FOlocalp -convergent. Moreover, if Li is a modeling FOlocalp -limit of (Bn,i)n∈N when αi = 0 then

i(Li,αi) is a modeling FOlocalp -limit of (An)n∈N.

Proof. This follows from Theorem 3.30, as An = i(Bn,i,an,i). Definition 3.32. A family of sequence (Ai,n)n∈N (i ∈ I) of λ-structures is

uniformly elementarily convergent if, for every formula φ ∈ FO1(λ) there is an integer N such that the following implication holds

∀i ∈ I, ∀n ≥ n ≥ N, (Ai,n |= (∃x)φ(x)) =⇒ (Ai,n |= (∃x)φ(x)).

First notice that if a family (Ai,n)n∈N (i ∈ I) of sequences is uniformly elementarily convergent, then each sequence (Ai,n)n∈N is elementarily convergent.

Lemma 3.33. Let I ⊆ N, and let (Ai,n)n∈N (i ∈ I) be sequences forming a

uniformly elementarily convergent family. Then ( i∈I Ai,n)n∈N is elementarily convergent. Moreover, if (Ai,n)n∈N is elementarily convergent to Ai then ( i∈I Ai,n)n∈N

is elementarily convergent to i∈I Ai.

Proof. Let λ+ be the signature λ augmented by a binary relational symbol . Let I1 be the basic interpretation scheme of λ+-structures in λ-structures deﬁning

(x,y) for every x,y. Let A+i,n = I1(Ai,n). According to Lemma 3.23, for every sentence θ ∈ FO0(λ) there exist formulas ψ1,...,ψs ∈ FOlocal1 , an integer m, and a Boolean function F such that the property i∈I A+i,n |= θ is equivalent to

({i,Ai,n |= (∃x)ψs(x)})) = 1. According to the deﬁnition of a uniformly elementarily convergent family there is an integer N such that, for every 1 ≤ j ≤ s, the value Bigm

###### ({i,Ai,n |= (∃x)ψ1(x)}),...,Bigm

F(Bigm

1

s

({i,Ai,n |= (∃x)ψj(x)}) is a function of n, which is non-decreasing for n ≥ N. It follows that this function admits a limit for every 1 ≤ j ≤ s hence the exists an integer N such that either i∈I A+i,n |= θ holds for every n ≥ N or it holds for no n ≥ N . It follows that ( i∈I A+i,n)n∈N is elementarily convergent. Thus (by means of the basic interpretation scheme deleting ) ( i∈I Ai,n)n∈N is elementarily convergent

j

If I is ﬁnite, it is easily checked that if (Ai,n)n∈N is elementarily convergent to Ai then ( i∈I Ai,n)n∈N is elementarily convergent to i∈I Ai.

Otherwise, we can assume I = N. Following the same lines, it is easily checked that ( ni=1 Ai)n∈N converges elementarily to ( i∈N Ai)n∈N. For i,n ∈ N, let Bi,2n = Ai,n and Bi,2n+1 = Ai. As, for each i ∈ N, Ai is an elementary limit of

(Ai,n)n∈N it is easily checked that the family of the sequences (Bi,n)n∈N is uniformly elementarily convergent. It follows that ( i∈N Bi,n)n∈N is elementarily convergent thus the elementary limit of ( i∈I Ai,n)n∈N and ( ni=1 Ai)n∈N are the same, that is i∈I Ai.

From Corollary 3.31 and Lemma 3.33 then follows the next general result.

Corollary 3.34. Let (An)n∈N be a sequence of ﬁnite λ-structures. Assume An be the disjoint union of Bn,i (i ∈ N) where all but a ﬁnite number

of Bn,i are empty. Let an,i = |Bn,i|/|An|. Assume that:

- • for each i ∈ N, the limit αi = limn→∞ an,i exists and the following equation holds:

i≥1

αi = 1,

- • for each i ∈ N such that αi = 0, the sequence (Bn,i)n∈N is FOlocalconvergent,
- • the family {(Bn,i)n∈N (i ∈ N)} is uniformly elementarily convergent.


Then, the sequence (An)n∈N is FO-convergent. Moreover, if Li is a modeling FO-limit of (Bn,i)n∈N when αi = 0 and an

elementary limit of (Bn,i)n∈N when αi = 0 then i(Li,αi) is a modeling FO-limit of (An)n∈N.

3.2.5. Random-free graphons and Modelings. A graphon is random-free if it is {0,1}-valued almost everywhere. Moreover, if two graphons represent the same L-limit of ﬁnite graphs, then either they are both random-free or none of them are (see for instance [51]). Several properties of random-free graph limits have been studied.

For example, a graph limit Γ is random-free if and only if the random graph G(n,Γ) of order n sampled from Γ has entropy o(n2) [4, 51] (see also [45]).

A sequence of graphs (Gn)n∈N is L-convergent to a random-free graphon if and only if the sequence (Gn)n∈N is convergent for the stronger metric δ1 [88], where the distance δ1(G,H) of graphs G and H with respective vertex sets {x1,...,xm} and {y1,...,ym} is the minimum over all non-negative m × n matrices A = (αi,j) with row sums 1/m and column sums 1/n of (i,j,g,h)∈∆ αi,gαj,h, where ∆ is the set of quadruples (i,j,g,h) such that either {xi,xj} ∈ E(G) or {yg,yh} ∈ E(H) (but not both).

Lov´sz and Szegedy [64] deﬁned a graph property (or equivalently a class of graphs) C to be random-free if every L-limit of graphs in C is random-free. They prove the following:

Theorem 3.35 (Lov´sz and Szegedy [64]). A hereditary class C is random-free if and only if there exists a bipartite graph F with bipartition (V1,V2) such that no graph obtained from F by adding edges within V1 and V2 is in C.

From this result, one deduce for instance that the class of m-partite cographs is random-free (see [20] for a related study of quantiﬁer-free limits of tree-semilattices), generalizing the particular cases of threshold graphs [24] and (more general) cographs [52].

Recall that the Vapnik–Chervonenkis dimension (or simply VC-dimension) VC(G) of a graph G is the maximum integer k such that there exists in G disjoint vertices ui (1 ≤ i ≤ k) and vI (∅ ⊆ I ⊆ {1,...,k}) such that ui is adjacent to vI exactly if i ∈ I. We now rephrase Lov´sz and Szegedy Theorem 3.35 in terms of VC-dimension.

Theorem 3.36. A hereditary class C is random-free if and only if VC(C) < ∞, where

VC(C) = sup

VC(G).

G∈C

Proof. Let Bk be the bipartite graph with vertices ui (1 ≤ i ≤ k) and vI (∅ ⊆ I ⊆ {1,...,k}) such that ui is adjacent to vI exactly if i ∈ I.

If VC(C) < k then no graph obtained from Bk by adding edges within the ui’s and the vI’s is in C hence, according to Theorem 3.35, the class C is random-free.

Conversely, if the class C is random-free there exists, according to Theorem 3.35, a bipartite graph F with bipartition (V1,V2) (with |V1| ≤ |V2|) such that no graph obtained from F by adding edges within V1 and V2 is in C. It is easily checked that

- F is an induced subgraph of B|V

1|+log2 |V2| so VC(C) < |F2| + log2 |F|.

The VC-dimension of classes of graphs can also be related to the nowhere dense/somewhere dense dichotomy. Recall that a class C is somewhere dense if there exists an integer p such that for every integer n the p-subdivision of Kn is a subgraph of a graph in C, and that the class C is nowhere dense, otherwise [74, 78, 80]. This dichotomy can also be characterized in quite a number of diﬀerent ways, see [80]. Based on Laskowski [58], another characterization has been proved, which relates this dichotomy to VC-dimension:

- Theorem 3.37 (Adler and Adler [2]). For a monotone class of graphs C, the

following are equivalent:

- (1) For every interpretation scheme I of graphs in graphs, the class I(C) has bounded VC-dimension;
- (2) For every basic interpretation scheme I of graphs in graphs with exponent 1, the class I(C) has bounded VC-dimension;
- (3) The class C is nowhere-dense.


From Theorem 3.35 and 3.37 we deduce the following:

- Theorem 3.38. Let C be a monotone class of graphs. Then the following are


equivalent:

- (1) For every interpretation scheme I of graphs in graphs, the class I(C) is random-free;
- (2) For every basic interpretation scheme I of graphs in graphs with exponent 1 and built using local formulas, the class I(C) is random-free;
- (3) The class C is nowhere-dense.


Proof. Obviously, condition (1) implies condition (2). Assume that (2) and assume for contradiction that (3) does not hold. Then, as C is monotone and somewhere dense, there is an integer p ≥ 1 such that for every graph n, the psubdivision Subp(Kn) of the complete graph Kn is in C. To every ﬁnite graph G we associate a graph G by considering an arbitrary orientation of G and then building

- G as shown on the ﬁgure bellow.


x y

###### G

| | | |
|---|---|---|
| | | |


p p p

p

x y

###### G

p

p

(2p + 1)(|G| − dG(x)) − 1 (2p + 1)(|G| − dG(y)) − 1

p

Note that G ∈ C as it is obviously a subgraph of the p-subdivision of the complete graph of order (2p + 1)|G|2. It is easily checked that there is a basic interpretation scheme Ip of graphs in graphs with exponent 1 (which deﬁnitions only depends on p) deﬁned using local formulas only, such that Ip(G ) = G[(2p + 1)|G|], where G[(2p+1)|G|] denotes the graph obtained from G by blowing each vertex to an independent set of size (2p + 1)|G|.

Let (Gi)i∈N be a sequence of graph that is L-convergent to a non random-free graphon W. As t(F,G) = hom(|G|F,G)

is invariant by uniform blow-up of the vertices of G, for every ﬁnite graph F the following equation holds:

|F |

t(F,Ip(G i)) = t(F,Gi[(2p + 1)|Gi|]) = t(F,Gi).

Hence (Ip(G i))i∈N is L-convergent to W. Then the condition (2) contradicts the hypothesis that W is not random-free. It follows (by contradiction) that (2) implies (3).

Assume condition (3) holds, and let I be an interpretation scheme of graphs in graphs. Then according to Theorem 3.37 the class I(C) has bounded VC-dimension, hence the hereditary closure of I(C) has bounded VC-dimension thus is random-free, whence I(C) is random-free.

We derive the following corollary concerning existence of modeling FOlocallimits, which completes Corollary 3.11 and implies Theorem 1.8.

Theorem 3.39. Let C be a monotone class of graphs. If every FOlocal-convergent sequence of graphs in C has a modeling FOlocal-limit

then C is nowhere dense.

Proof. Let I be a basic interpretation scheme of graphs in graphs built using local formulas, and let (Gi)i∈N be a sequence of graphs in C such that |Gi| is unbounded, and the sequence (I(Gi))i∈N is L-convergent.

###### )i∈N that is FOlocal-convergent. Hence, by hypothesis, (Gn

By compactness, the sequence (Gi)i∈N has a subsequence (Gn

i

###### )i∈N has a modeling FOlocal-limit L. According to Proposition 3.15, the sequence (I(Gn

i

###### ))i∈N has modeling FOlocal-limit I(L). By Lemma 3.10, L deﬁnes a random-free graphon W that is the L-limit of

i

))i∈N. Of course, the L-limit of an L-convergent sequence (Gi)i∈N with |Gi| bounded is also random-free. Hence the class I(C) is random-free. As this conclusion holds for every basic interpretation scheme I built using local formulas we deduce from Theorem 3.38 that C is nowhere dense.

###### (I(Gn

i

3.2.6. Modelings FO-limits for Graphs of Bounded Degrees. Nice limit objects are known for sequence of bounded degree connected graphs, both for BSconvergence (graphing) and for FO0-convergence (countable graphs). It is natural to ask whether a nice limit object could exist for full FO-convergence. We shall now give a positive answer to this question. First we take time to comment on the connectivity assumption. A ﬁrst impression is that FO-convergence of disconnected graphs could be considered component-wise. This is far from being true in general. The contrast between the behaviour of graphs with a ﬁrst-order deﬁnable component relation (like graphs with bounded diameter components) and of graphs with bounded degree is exempliﬁed by the following example.

- Example 3.40. Consider a BS-convergent sequence (Gn)n∈N of planar graphs

with bounded degrees such that the limit distribution has an inﬁnite support. Note that limn→∞ |Gn| = ∞. Then, as planar graphs with bounded degrees form a hyperﬁnite class of graphs there exists, for every graph Gn and every > 0 a subgraph S(Gn, ) of Gn obtained by deleting at most |Gn| of edges, such that the connected components of S(Gn, ) have order at most f( ). By considering a subsequence Gs(n) we can assume limn→∞ |Gs(n)|/f(1/n) = ∞. Then note that the sequences (Gs(n))n∈N and (S(Gs(n),1/n))n∈N have the same BS-limit. By merging these sequences, we conclude that there exists an FOlocal convergent sequence of graphs with bounded degrees (Hn) such that Hn is connected if n is even and such that the number of connected components of Hn for n odd tends to inﬁnity.

- Example 3.41. Using Fig. 2, consider four sequences (An)n∈N, (Bn)n∈N, (Cn)n∈N,(Dn)n∈N


of FO-converging sequences where |An| = |Bn| = |Cn| = |Dn| grows to inﬁnity, and where these sequences have distinct limits.

Consider a sequence (Gn)n∈N deﬁned as follows: for each n, Gn has two connected components denoted by Hn,1 and Hn,2 obtained by joining An,Cn and Bn,Dn by a path of length n (for n odd), and by joining An,Dn and Bn,Cn by a path of length n (for n even). Then (Gn)n∈N is FO-convergent. However, there is no choice of a mapping f : N → {1,2} such that (Hn,f(n)) is FO-convergent (or even BS-convergent).

This situation is indeed related to the fact that the diameter of the graph Gn in the sequence tend to inﬁnity as n grows and that the belonging to the same connected component cannot be deﬁned by a ﬁrst-order formula. This situation is standard when one consider BS-limits of connected graphs with bounded degrees: it is easily checked that, as a limit of connected graphs, a graphing may have uncountably many connected components.

Remark 3.42. In the spirit of the construction shown Fig. 2, we can prove that the set of measure µ which are BS-limits of connected graphs with maximum degree d ≥ 2 and order going to inﬁnity is convex: Assume (Gn)n∈N and (Hn)n∈N are convergent sequences with limits µ1 and µ2, and let 0 < α < 1. We construct graph Mn as follows: let cn = min(|Gn|,|Hn|). We consider α|Hn| copies of Gn and

An Bn

Cn Dn

An Bn

Cn Dn

Figure 2. An FO-converging sequence with no component selection

(1 − α)|Gn| copies of Hn linked by paths of length log cn (see Fig. 3). It is easily checked that the statistics of the neighborhoods of Mn tend to αµ1 + (1 − α)µ2.

Gn Gn Gn Gn Gn

Hn Hn Hn Hn

Figure 3. Construction of the graph Mn

Let V be a standard Borel space with a measure µ. Suppose that T1,T2,...,Tk are measure preserving Borel involutions of X. Then the system

G = (V,T1,T2,...,Tk,µ) is called a measurable graphing (or simply a graphing) [1]. A graphing G determines an equivalence relation on the points of V . Simply, x ∼G y if there exists a sequence of points (x1,x2,...,xm) of X such that

- • x1 = x,xm = y
- • xi+1 = Tj(xi) for some 1 ≤ j ≤ k.


Thus there exist a natural simple graph structure on the equivalence classes, the leafgraph. Here x is adjacent to y, if x = y and Tj(x) = y for some 1 ≤ j ≤ k. Now if If V is a compact metric space with a Borel measure µ and T1,T2,...,Tk are continuous measure preserving involutions of V , then G = (V,T1,T2,...,Tk,µ) is a topological graphing. It is a consequence of [10] and [38] that every local weak limit

of ﬁnite connected graphs with maximum degree at most D can be represented as a measurable graphing. Elek [31] further proved the representation can be required to be a topological graphing.

A graphing deﬁnes an edge coloration, where {x,y} is colored by the set of the indexes i such that y = Ti(x). For an integer r, a graphing G = (V,T1,...,Tk,µ) and a ﬁnite rooted edge colored graph (F,o) we deﬁne the set

Dr(G,(F,o)) = {x ∈ G,Br(G,x) (F,o)}. It is easily checked that Dr(G,(F,o)) is measurable. Considering a k-edge colored graphing allows us to describe a vertex x in a distance-r neighborhood of a given vertex v by the sequence of the colors of the edges of a path linking v to x. Taking, among the minimal length sequences, the one which is lexicographically minimum, it is immediate that for every vertex v and every integer r there is a injection ιv,r from Br(G,v) to the set of the sequences of length at most r with values in [k]. Moreover, if Br(G,v) and Br(G,v ) are isomorphic as edge-colored rooted graphs, then there exists a unique isomorphism f : Br(G,v) → Br(G,v ) and this isomorphism as the property that for every

- x ∈ Br(G,v) it holds that ιv,r (f(x)) = ιv,r(x). Lemma 3.43. Every graphing is a modeling.


Proof. Let G = (V,T1,...,Td,µ) be a graphing. We color the edges of G according to the the involutions involved.

For r ∈ N, we denote by Fr the ﬁnite set of all the colored rooted graphs that arise as Br(G,v) for some v ∈ V . To every vertex v ∈ V and integer r ∈ N we associate tr(v), which is the isomorphism type of the edge colored ball Br(G,v).

According to Gaifman’s locality theorem, in order to prove that G is a modeling, it is suﬃcient to prove that for each φ ∈ FOlocalp , the set

X = {(v1,...,vp) ∈ V q : G |= φ(v1,...,vp)} is measurable (with respect to the product σ-algebra of V p).

Let L ∈ N be such that φ is L-local. For every v = (v1,...,vp) ∈ X we deﬁne the graph Γ(v) with vertex set {v1,...,vp} such that two vertices of Γ(v) are adjacent if their distance in G is at most L. We deﬁne a partition P(v) of [p] as follows: i and j are in a same part if vi and vj belong to a same connected component of Γ(v). To each part P ∈ P(v), we associate the tuple formed by TP = t(|P|−1)L(vminP) and, for each i ∈ P − {minP}, a composition FP,i = Ti

1 ◦ ··· ◦ Ti

j

with 1 ≤ j ≤ (|P|−1)L, such that vi = FP,i(vminP). We also deﬁne FP,minP as the identity mapping. According to the locality of φ, if v = (v 1,...,v p) ∈ V p deﬁnes the same partition, types, and compositions, then v ∈ X. For ﬁxed partition P, types (TP)P∈P, and compositions (FP,i)i∈P∈P, the corresponding subset X of X is included in a (reshuﬄed) product Y of sets of tuples of the form (FP,i(xminP)) for vminP ∈ WP, and is the set of all v ∈ G such that B(|P|−1)L(G,v) = TP. Hence WP is measurable and (as each FP,i is measurable) Y is a measurable subset of G|P|. Of course, this product may contain tuples v deﬁning another partition. A simple induction and inclusion/exclusion argument shows that X is measurable. As X is the union of a ﬁnite number of such sets, X is measurable.

We now relate graphings to FO-limits of bounded degree graphs. We shall make use of the following lemma which reduces a graphing to its essential support.

Lemma 3.44 (Cleaning Lemma). Let G = (V,T1,...,Td,µ) be a graphing.

Then there exists a subset X ⊂ V with 0 measure such that X is globally invariant by each of the Ti and G = (V − X,T1,...,Td,µ) is a graphing such that for every ﬁnite rooted colored graph (F,o) and integer r the following equation holds:

µ(Dr(G ,(F,o))) = µ(Dr(G,(F,o))) (which means that G is equivalent to G) and

Dr(G ,(F,o)) = ∅ ⇐⇒ µ(Dr(G ,(F,o))) > 0.

Proof. For a ﬁxed r, deﬁne Fr has the set of all (isomorphism types of) ﬁnite rooted k-edge colored graphs (F,o) with radius at most r such that µ(Dr(G,(F,o))) = 0. Deﬁne

X =

Dr(G,(F,o)).

r∈N (F,o)∈Fr

Then µ(X) = 0, as it is a countable union of 0-measure sets.

We shall now prove that X is a union of connected components of G, and thus X is globally invariant by each of the Ti. Namely, if x ∈ X and y is adjacent to x, then y ∈ X. Indeed: if x ∈ X then there exists an integer r such that µ(D(G,Br(G,x))) = 0. But it is easily checked that

µ(D(G,Br+1(G,y))) ≤ d · µ(D(G,Br(G,x))). Hence y ∈ X. It follows that for every 1 ≤ i ≤ d we have Ti(X) = X. So we can deﬁne the graphing G = (V − X,T1,...,Td,µ).

Let (F,o) be a rooted ﬁnite colored graph. Assume there exists x ∈ G such that Br(G ,r) (F,o). As X is a union of connected components, we also have Br(G,r) (F,o) and x ∈/ X. It follows that µ(D(G,(F,o))) > 0 hence it holds that µ(Dr(G ,(F,o))) > 0.

The cleaning lemma allows us a clean description of FO-limits in the bounded degree case:

Theorem 3.45. Let (Gn)n∈N be a FO-convergent sequence of ﬁnite graphs with maximum degree d, with limn→∞ |Gn| = ∞. Then there exists a graphing G, which is the disjoint union of a graphing G0 and a countable graph Gˆ such that

- • The graphing G is a modeling FO-limit of the sequence (Gn)n∈N.
- • The graphing G0 is a BS-limit of the sequence (Gn)n∈N such that Dr(G0,(F,o)) = ∅ ⇐⇒ µ(Dr(G0,(F,o))) > 0.
- • The countable graph Gˆ is an elementary limit of the sequence (Gn)n∈N.


Proof. Let G0 be a BS-limit, which has been “cleaned” using the previous lemma, and let Gˆ be an elementary limit of G. It is clear that G = G0 ∪Gˆ is also a BS-limit of the sequence, so the lemma amounts in proving that G is elementarily equivalent to Gˆ.

According to Hanf’s theorem [44], it is suﬃcient to prove that for all integers r,t and for every rooted ﬁnite graph (F,o) (with maximum degree d) the following equality holds:

min(t,|Dr(G,(F,o))|) = min(t,|Dr(G,ˆ (F,o))|).

Assume for contradiction that this is not the case. Then |Dr(G,ˆ (F,o))| < t and Dr(G0,(F,o)) is not empty. However, as G0 is clean, this implies µ(Dr(G0,(F,o))) = α > 0. It follows that for every suﬃciently large n it holds that |Dr(Gn,(F,o))| > α/2|Gn| > t. Hence |Dr(G,ˆ (F,o))| > t, contradicting our hypothesis.

That G is a modeling then follows from Lemma 3.43.

Remark 3.46. Not every graphing with maximum degree 2 is an FO-limit modeling of a sequence of ﬁnite graphs (as it needs not be an elementary limit of ﬁnite graphs). Indeed: let G be a graphing that is an FO-limit modeling of the sequence of cycles. The disjoint union of G and a ray is a graphing G , which has the property that all its vertices but one have degree 2, the exceptional vertex having degree 1. As this property is not satisﬁed by any ﬁnite graph, G is not the FO-limit of a sequence of ﬁnite graphs.

Let us ﬁnish this section by giving an interesting example, which shows that the cleaning lemma sometimes applies in a non-trivial way:

Example 3.47. Consider the graph Gn obtained from a de Bruijn sequence of length 2n as shown Fig 4.

0

0

1

- 0

- 0
- 1


1

- 1


0

1

0

0

1

1 1

0

Figure 4. The graph Gn is constructed from a de Bruijn sequence of length 2n.

It is easy to deﬁne a graphing G, which is the limit of the sequence (Gn)n∈N: as vertex set, we consider the rectangle [0;1) × [0;3). We deﬁne a measure preserving

function f and two measure preserving involutions T1,T2 as follows:

 

(2x,y/2) if x < 1/2 and y < 1 (2x − 1,(y + 1)/2) if 1/2 ≤ x and y < 1 (x,y) otherwise

f(x,y) =



- T1(x,y) =

 



(x,y + 1) if y < 1 (x,y − 1) if 1 ≤ y < 2 (x,y) otherwise

- T2(x,y) =




- (x,y + 1) if x < 1/2 and 1 ≤ y < 2
- (x,y + 2) if 1/2 ≤ x and y < 1 (x,y − 1) if x < 1/2 and 2 ≤ y (x,y − 2) if 1/2 ≤ x and 2 ≤ y (x,y) otherwise






Then the edges of G are the pairs {(x,y),(x ,y )} such that (x,y) = (x ,y ) and either (x ,y ) = f(x,y), or (x,y) = f(x ,y ), or (x ,y ) = T1(x,y), or (x ,y ) = T2(x,y).

If one considers a random root (x,y) in G, then the connected component of (x,y) will almost surely be a rooted line with some decoration, as expected from what is seen from a random root in a suﬃciently large Gn. However, special behaviour may happen when x and y are rational. Namely, it is possible that the connected component of (x,y) becomes ﬁnite. For instance, if x = 1/(2n − 1) and

- y = 2n−1x then the orbit of (x,y) under the action of f has length n; thus the connected component of (x,y) in G has order 3n. Of course, such ﬁnite connected


components do not appear in Gn. Hence, in order to clean G, inﬁnitely many components have to be removed.

Let us give a simple example exemplifying the distinction between BS and FO-convergence for graphs with bounded degree.

Example 3.48. Let Gn denote the n × n grid. The BS-limit object is a probability distribution concentrated on the inﬁnite grid with a speciﬁed root. A limit graphing can be described as the Lebesgue measure on [0,1]2, where (x,y) is adjacent to (x ± α mod 1,y ± α mod 1) for some irrational number α.

This graphing, however, is not an FO-limit of the sequence (Gn)n∈N as every FO-limit has to contain four vertices of degree 2. An FO-limit graphing can be described as the above graphing restricted to [0,1)2 (obtained by deleting all vertices with x = 1 or y = 1). One checks for instance that this graphing contains four vertices of degree 2 (the vertices (α,α), (1 − α,α), (α,1 − α), and (1 − α,1 − α)) and inﬁnitely many vertices of degree 3.

We want to stress that our general and unifying approach to structural limits was not developed for its own sake and that it provided a proper setting (and, yes, encouragement) for the study of classes of sparse graphs. So far classes of graphs with bounded degree are the only classes of sparse graphs where the structural

limits were constructed eﬃciently. (Another example of limits of sparse graphs is provided by scaling limits of transitive graphs [9] which proceeds in diﬀerent direction and is not considered here.)

###### 3.3. Decomposing Sequences: the Comb Structure

The combinatorics of limits of equivalence relations (such as components) is complicated. We start this analysis by considering the combinatorics of “large” equivalence classes. This leads to the notion of spectrum, which will be analyzed in this section.

###### 3.3.1. Spectrum of a First-order Equivalence Relation.

Definition 3.49 ( -spectrum). Let A be a λ-modeling (with measure νA), and let ∈ FO2(λ) be a formula expressing a component relation on A (see Deﬁnition 2.24). Let {Ci : i ∈ Γ} be the set of all the -equivalence classes of A, and let Γ+ be the (countable) subset of Γ of the indexes i such that νA(Ci) > 0.

The -spectrum Sp (A) of A is the (countable) sequence of the values νA(Ci) (for i ∈ Γ+) ordered in non-increasing order.

Lemma 3.50. For k ∈ N, let (k) be the formula ki=1 (xi,xi+1). Then the following equation holds:

νA(Ci)k+1 = (k),A .

i∈Γ+

Proof. Let k ∈ N. Deﬁne

Dk+1 = {(x1,...,xk+1) ∈ Ak+1 : A |= k(x1,...,xk+1)}. According to Lemma 3.3, each Ci is measurable, thus i∈Γ

Ci is measurable and so is R = A \ i∈Γ+ Ci.

+

k+1∩Rk+1 of Dk+1 ∩ Rk+1 and applying Fubini’s theorem, we get

Considering the indicator function 1D

k+1∩Rk+1 dνAk+1 = ··· 1R(x1,...,xk+1) dνA(x1,...,dνA(xk+1) = 0. as for every ﬁxed a1,...,ak (with a1 ∈ Cα, for some α ∈ Γ \ Γ+) we have

1D

Ak+1

0 ≤ 1R(a1,...,ak,xk+1)dνA(xk+1) ≤ νA(Cα) = 0. It follows (by countable additivity) that

(k),A = νAk+1(Dk+1) = νAk+1(

i∈Γ+

Cik+1) =

νA(Ci)k+1.

i∈Γ+

It follows from Lemma 3.50 that the spectrum Sp (A) is computable from the sequence of (non-increasing) values ( (k),A )k∈N.

We assume that every ﬁnite sequence x = (x1,...,xn) of positive reals is implicitly embedded in an inﬁnite sequence by deﬁning xi = 0 for i > n. Recall the usual k norms:

1/k

|xi|k

.

x k =

i

Hence above equations rewrite as (3.1) Sp (A) k+1 = (k),A 1/(k+1).

We shall prove that the spectrum is, in a certain sense, deﬁned by a continuous function. We need the following technical lemma.

Lemma 3.51. For each n ∈ N, let an = (an,i)i∈N be a non-increasing sequence

of positive real numbers with bounded sum (i.e an 1 < ∞ for every n ∈ N). Assume that for every integer k ≥ 1 the limit sk = limn→∞ an k exists. Then (an)n∈N converges in the space c0 of all sequences converging to zero (with

norm · ∞).

Proof. We ﬁrst prove that the sequences converge pointwise, that is that there exists a sequence x = (xi)i∈N such that for every i ∈ N the following equation holds:

xi = lim

an,i.

n→∞

For every > 0, if sk < then an,1 < 2 for all suﬃciently large values of n. Thus if sk = 0 for some k, the limit limn→ an,i exists for every i and is null. Thus, we can assume that sk is strictly positive for every k ∈ N.

Fix k ∈ N. There exists N ∈ N such that for every n ≥ N it holds that

|skk − an kk| < skk/k. As (an,i)i∈N is a non-increasing sequence of positive real numbers, for every n = N the following inequality holds

akn,1 ≤ an kk < skk(1 + 1/k) and

akn,−11 ≥ an kk > skk(1 − 1/k). Hence

log(1 − 1/k) k

1 k − 1

log(1 + 1/k) k ≥ log an,1 ≥ 1 +

log sk +

.

log sk +

Thus x1 = limn→∞ an,1 exists and x1 = limk→∞ sk. Inductively, we get that for each i ∈ N, the limit xi = limn→∞ an,i exists and that

(skk −

xkj)1/k.

xi = lim

k→∞

j<i

We now prove that the converge is uniform, that is that for every > 0 there exists N such that for every n ≥ N the following inequality holds:

x − an ∞ <  .

As an ∈ 1 and an 1 converges there exists M such that an 1 ≤ M for every n ∈ N. Let > 0. Let A = min{i : xi ≤  /3}. (Note that A ≤ 3M/ .) There exists N such that for every n ≥ N it holds that supi≤A |xi − an,i| <  /3. Moreover, for every i > A the following inequality holds:

0 ≤ an,i ≤ an,A < xA +  /3 < 2 /3. As 0 ≤ xi ≤  /3 for every i > A the following inequality holds: |xi − an,i| <

for every i > A (hence for every i). Thus (an)n∈N converges in ∞. As obviously each an has 0 limit, (an)n∈N converges in c0.

Lemma 3.52. Let λ be a signature. The mapping A  → Sp (A) is a continuous mapping from the space of λ-modelings with a component relation (with the topology of FOlocal(λ)-convergence) to the space c0 of all sequences converging to zero (with · ∞ norm).

Proof. Assume An is an FOlocal(λ)-convergent sequence of λ-modelings. Let (spn,1,..., spn,i,...) be the -spectrum of An (extended by zero values if

ﬁnite), and let an = (an,i)i∈N be the sequence deﬁned by an,i = sp2n,i. Then for every integer k ≥ 1 it holds that

an k = Sp (An) 22k = (2k−1),An 1/k.

Hence sk = limn→∞ an k exists. According to Lemma 3.51, (an)n∈N converges in c0, thus so does (Sp (An))n∈N.

Definition 3.53. Let (An)n∈N be a sequence of ﬁnite λ-structures. Let be a component relation, and for simplicity assume ∈ λ. In the following, we assume that -spectra are extended to inﬁnite sequences by adding zeros if necessary.

- • The sequence (An)n∈N is -nice if Sp (An) converges pointwise;
- • The limit -spectrum of a -nice sequence (An)n∈N is the pointwise limit of Sp (An);
- • the -support is the set I of the indexes i for which the limit -spectrum is non-zero;
- • the sequence has full -spectrum if, for every index i not in the -support,


there is some N such that the ith value of Sp (An) is zero for every n > N.

As proved in Lemma 3.52, every FOlocal-convergent sequence is -nice. Lemma 3.54. Let (An) be a -nice sequence of λ-structures with empty -

support. Then the following conditions are equivalent:

- (1) the sequence (An) is FOlocal-convergent;
- (2) the sequence (An) is FOlocal1 -convergent.


Moreover, for every -local formula φ with p > 1 free variables it holds that lim

φ,An = 0.

n→∞

Proof. FOlocal-convergence obviously implies FOlocal1 -convergence. So, assume that (An)n∈N is FOlocal1 -convergent, and let φ be a -local ﬁrst-order formula with p > 1 free variables. For n ∈ N, let Bn,i (i ∈ Γn) denote the connected components of An. As (An) is -nice and has empty -support, there exists for every > 0 an integer N such that for n > N and every i ∈ Γn it holds that |Bn,i| < |An|. Then, according to Corollary 3.21, for n > N

p

|Bn,i| |An|

φ,An =

φ,Bn,i

i∈Γn

p

|Bn,i| |An|

≤

i∈Γn

|Bn,i| |An|

p−1 = p−1.

<

i∈Γn

Hence φ,An converges (to 0) as n grows to inﬁnity. It follows that (An)n∈N is FOlocal-convergent, according to Theorem 3.22.

Lemma 3.55. Let (An)n∈N be an FOlocal-convergent sequence of ﬁnite λ-structures, with component relation ∈ λ and limit -spectrum (spi)i∈I. For n ∈ N, let Bn,i be the connected components of An order in non-decreasing order (with Bn,i empty if i is greater than the number of connected components of An). Let a ≤ b be the ﬁrst and last occurrence of spa = spb in the -spectrum and let A n be the union of all the Bn,i for a ≤ i ≤ b.

Then (A n)n∈N is FO-convergent if spa > 0 and FOlocal-convergent if spa = 0. Assume moreover that (An)n∈N has a modeling FOlocal-limit L. Let L be the

union of the connected components Li of L with νL(Li) = spa. Equip L with the σ-algebra ΣL which is the restriction of ΣL to L and the probability measure νL deﬁned by νL (X) = νL(X)/νL(L ) (for X ∈ ΣL ).

Then L is a modeling FO-limit of (A n)n∈N if spa > 0 and a modeling FOlocallimit of (A n)n∈N if spa = 0.

Proof. Extend the sequence sp to the null index by deﬁning sp0 = 2. Let r = min(spa−1/spa, spb/spb+1) (if spb+1 = 0 simply deﬁne r = spa−1/spa). Notice that r > 1. Let φ be a -local formula with p free variables. According to Corollary 3.21 the following equation holds:

p

|Bn,i| |An|

φ,An =

φ,Bn,i . In particular, it holds that

i

p

|Bn,i| |An|

(p),An =

.

i

Let α > 1/(1 − rp). Deﬁne wn,i = |Bn,i| |An|

p

(α + φ,Bn,i ).

From the deﬁnition of r it follows that for each n ∈ N, wn,i > wn,j if i < a and j ≥ a or i ≤ b and j > b. Let σ ∈ Sω be a permutation of N, such that an,i = wn,σ(i) is non-increasing. It holds that

wn,i = α (p),An + φ,An . Hence

###### an,i =

i

i

apn,i

lim

n→∞ i

exists. According to Lemma 3.51 it follows that for every i ∈ N the limit limn→∞ an,i exists. Moreover, as σ globally preserves the set {a,...,b} it follows that the limit

b

p

|Bn,i| |An|

d = lim

(α + φ,Bn,i )

n→∞

i=a

exists. As for every i ∈ {a,...,b} it holds that limn→∞ |Bn,i|/|An| = spa and as φ,A n = bi=a(|Bn,i|/|An|)p φ,Bn,i we deduce lim

φ,A n = d − (b − a + 1)α.

n→∞

Hence limn→∞ φ,A n exists for every -local formula and, according to Theorem 3.22, the sequence (A n)n∈N is FOlocal-convergent.

Assume spa > 0. Let N = b−a+1. To each sentence θ we associate the formula θ ∈ FOlocalN that asserts that the substructure induced by the closed neighborhood of x1,...,xN satisﬁes θ and that x1,...,xN are pairwise distinct and non-adjacent. For suﬃciently large n, the structure A n has exactly N connected components. It is easily checked that if A n does not satisfy θ then θ,A n = 0, although if A n does satisfy θ then

mina≤i≤b |Bn,i| b i=a |Bn,i|

N

θ,A n ≥

,

hence θ,A n > (2N)−N for all suﬃciently large n. As θ,A n converges for every sentence θ, we deduce that the sequence (A n)n∈N is elementarily convergent.

- According to Theorem 2.23, the sequence (A n)n∈N is thus FO-convergent. Now assume that (An)n∈N has a modeling FOlocal-limit L. First note that

Li being an equivalence class of it holds that Li ∈ ΣL, hence L ∈ ΣL and νL(L ) is well deﬁned. For every -local formula φ ∈ FOp(λ) it holds, according to Lemma 3.20, that

φ,L =

b

i=a

νL (Li)p φ,Li

=

1 νL(L )p

b

i=a

νL(Li)p φ,Li .

We deduce that

φ,L = lim

n→∞

φ,A n .

- According to Theorem 3.22, it follows that the same equality holds for every φ ∈ FOlocal(λ) hence L is a modeling FOlocal-limit of the sequence (A n)n∈N.


As above, for spa > 0, if L is a modeling FOlocal-limit of (A n)n∈N then it is a modeling FO-limit.

Lemma 3.56. Let (An)n∈N be an FO-convergent sequence of ﬁnite λ-structures, with component relation (expressing usual notion of connected components). Assume all the An have at most k connected components. Denote by Bn,1,...,Bn,k these components (adding empty λ-structures if necessary).

Assume that for each 1 ≤ i ≤ k it holds that limn→∞ |Bn,i|/|An| = 1/k.

Then there exists a sequence (σn)n∈N of permutations of [k] such that for each 1 ≤ i ≤ k the sequence (Bn,σ

n(i))n∈N is FO-convergent.

Proof. To a formula φ ∈ FOp(λ) we associate the -local formula φ ∈

FOlocalp (λ) asserting that all the free variables are -adjacent and that their closed neighborhood (that is their connected component) satisﬁes φ. Then essentially

the same proof as above allows to reﬁne An into sequences such that φ,A n,i is constant on the connected components of each of the A n. Considering formulas allowing to split at least one of the sequences, we repeat this process (at most k−1 times) until each A n,i contains equivalent connected components. Then, A n,i can be split into connected components in an arbitrary order, thus obtaining the sequences Bn,i.

So we have proved that a FO-convergent can be decomposed by isolines of the -spectrum (that is by groups of connected components with same asymptotic measure). In the next sections, we shall investigate how to reﬁne this further.

3.3.2. Sequences with Finite Spectrum. For every -nice sequence (An)n∈N with ﬁnite support I, we deﬁne the residue Rn of An as the union of the connected components Bn,i of An such that i ∈/ I.

When one considers an FOlocal-convergent sequence (An) with a ﬁnite support then the sequence of the residues forms a sequence which is either FOlocal-convergent or “negligible” in the sense that limn→∞ |Rn|/|An| = 0. This is formulated as follows:

Lemma 3.57. Let (An)n∈N be a sequence of λ-structures with component relation . For each n ∈ N and i ∈ N, let Bn,i be the i-th largest connected component of An.

Assume that (An)n∈N is FOlocal-convergent and has ﬁnite spectrum (spi)i∈I. Let Rn be the residue of An.

Then sp = limn→∞ |Rn|/|An| exists and either sp = 0 or (Rn)n∈N is FOlocalconvergent.

Proof. Clearly, sp = 1 − i spi. Assume sp > 0. First notice that for every > 0 there exists N such that for every i > N, the λ-structure Rn has no connected component of size at least  /2sp |An| and Rn has order at least sp /2|An|. Hence, for every i > N, the λ-structure Rn has no connected component of size at least |Rn|. According to Lemma 3.54, proving that (Rn)n∈N is FOlocal-convergent reduces to proving that (Rn)n∈N is FOlocal1 -convergent.

Let φ ∈ FOlocal1 . We group the λ-structures Bn,i (for i ∈ I) by values of spi as A n,1,...,A n,q. Denote by cj the common value of spi for the connected components Bn,i in A n,j. According to Corollary 3.21 it holds (as φ is clearly

-local) that

φ,An =

i

=

i∈I

q

=

j=1

|Bn,i| |An|

φ,Bn,i

|Bn,i| |An|

|Bn,i| |An|

φ,Bn,i +

φ,Bn,i

i/∈I

|A n,j| |An|

φ,A n,j + |Rn| |An|

φ,Rn .

According to Lemma 3.55, each sequence (A n,j)n∈N is FO-convergent. Hence the limit limn→∞ φ,Rn exists and we have

q

1 sp

φ,An −

lim

cj lim

φ,A n,j .

lim

φ,Rn =

n→∞

n→∞

n→∞

j=1

It follows that the sequence (Rn)n∈N is FOlocal-convergent.

The following result ﬁnally determines the structure of converging sequences of (disconnected) λ-structures with ﬁnite support. This structure is called comb structure, see Fig 5.

Theorem 3.58 (Comb structure for λ-structure sequences with ﬁnite spectrum). Let (An)n∈N be an FOlocal-convergent sequence of ﬁnite λ-structures with component relation and ﬁnite spectrum (spi)i∈I. Let Rn be the residue of An.

Then there exists, for each n ∈ N, a permutation fn : I → I such that the following holds

- • limn→∞ maxi/∈I |Bn,i|/|An| = 0;
- • limn→∞ |Rn|/|An| exists;
- • for every i ∈ I, the sequence (Bn,f

n(i))n∈N is FO-convergent and limn→∞ |Bn,f

n(i)|/|An| = spi;

- • either limn→∞ |Rn|/|An| = 0, or the sequence (Rn)n∈N is FOlocalconvergent.


Moreover, if (An)n∈N is FO-convergent then (Rn)n∈N is elementary-convergent.

Proof. This lemma is a direct consequence of Lemmas 3.55, 3.56 and 3.57, except that we still have to prove FO-convergence of (Rn)n∈N in the case where (An)n∈N is FO-convergent. As I is ﬁnite, the elementary convergence of (Rn)n∈N easily follows from the one of (An) and the one of the (Bn,f

n(i)) for i ∈ I.

3.3.3. Sequences with Inﬁnite Spectrum. Let (An)n∈N be a -nice sequence with inﬁnite spectrum (and support I = N). In such a case, the notion of a residue becomes more tricky and will need some technical deﬁnitions. Before this, let us take the time to give an example illustrating the diﬃculty of the determination of the residue Rn in the comb structure of sequences with inﬁnite spectrum.

- G1
- G2
- G3


Gn

Hn,1 Hn,k Rn

λ1 λk λ = 1 − i∈I λi

Figure 5. Illustration of the Comb structure for sequences with ﬁnite support

Example 3.59. Consider the sequence (Gn)n∈N where Gn is the union of 2n stars Hn,1,...,Hn,2n, where the i-th star Hn,i has order 22

n

(2−i + 2−n)/2. Then it holds that

|Hn,i|/|Gn| = 2−(i+1)

spi = lim

n→∞

hence i spi = 1/2 thus the residue asymptotically should contain half of the vertices of Gn! An FO-limit of this sequence is shown Fig. 6.

This example is not isolated. In fact it is quite frequent in many of its variants. To decompose such examples we need a convenient separation. This is provided by the notion of clip.

Definition 3.60. • A clip of a -nice sequence (An)n∈N with support N is a non-decreasing function C : N → N such that limn→∞ C(n) = ∞ and

∀n ≥ n

C(n)

|Bn ,i| |An |

− spi ≤

spi

i=1

i>C(n)

• The residue Rn of An with respect to a clip C(n) is the disjoint union of the Bn,i for i > C(n).

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


Figure 6. An FOlocal-limit. On the left side, each rectangle correspond to a star with the upper left point as its center; on the right side, each vertical line is a star with the upper point as its center.

Proposition 3.61. Every -nice sequence (An)n∈N with inﬁnite support has a clip C0, which is deﬁned by

M

|Bn ,i| |An |

− spi ≤

C0(n) = sup M, (∀n ≥ n)

spi .

i=1

i>M

Moreover, limn→ C0(n) = ∞ and a non decreasing function C is a clip of (An)n∈N if and only if C ≤ C0 and limn→ C(n) = ∞.

Proof. Indeed, for each n ∈ N, the value zl(M) = supn ≥n Mi=1 |B|An ,i|

n | − spi

is non-decreasing function of C with zl(0) = 0, and zr(M) = i>M spi is a decreasing function of C with zr(0) = i spi > 0 hence C0 is well deﬁned. Moreover, for every integer M, let α = i>M spi > 0. Then, as limn→∞ |Bn ,i|/|An | = spi there exists N such that for every n ≥ N and every 1 ≤ i ≤ M it holds that ||Bn ,i|/|An | − spi| ≤ α/M thus for every n ≥ N it holds that

M

|Bn ,i| |An |

− spi ≤ α =

spi.

i=1

i>M

It follows that C0(N) ≥ M. Hence limn→∞ C0(n) = ∞.

That a non decreasing function C is a clip of (An)n∈N if and only if C ≤ C0 and limn→ C(n) = ∞ follows directly from the deﬁnition.

Lemma 3.62. Let (An)n∈N be a -nice sequence with support N, and let C be a clip of (An)n∈N.

Then the limit sp = limn→∞ |R

n|

###### |An| exists and sp = 1 − i spi. Proof. As C is a clip, the following inequality holds for every n ∈ N

i

C(n)

|Bn,i| |An|

spi − 2

spi ≤

≤

i=1

i>C(n)

i

spi.

Also, for every > 0 there exists n such that | i C=1(n) spi − i spi| < , that is: i>C(n) spi <  . It follows that

C(n)

|Bn,i| |An|

lim

=

n→∞

i=1

i

spi.

Hence the limit sp = limn→∞ |R

n|

|An| exists and sp = 1 − i spi.

Lemma 3.63. Let (An)n∈N be a sequence of λ-structures with component relation . For each n ∈ N and i ∈ N, let Bn,i be the i-th largest connected component of An (if i is at most equal to the number of connected components of An, the empty λ-structure otherwise).

Assume that (An)n∈N is FO-convergent. Let C : N → N be a clip of (An)n∈N, and let Rn be the residue of An with

respect to C.

Let sp = limn→∞ |Rn|/|An|. Then either sp = 0 or (Rn)n∈N is FOlocalconvergent.

Proof. According to Lemma 3.62, limn→∞ |Rn|/|An| exists and sp = 1 −

i spi. Assume sp > 0. First notice that for every > 0 there exists N such that for every i > N, the λ-structure Rn has no connected component of size at least  /2sp |An| and Rn has order at least sp /2|An|. Hence, for every i > N, the λ-structure Rn has no connected component of size at least |Rn|. According to Lemma 3.54, proving that (Rn)n∈N is FOlocal-convergent reduces to proving that (Rn)n∈N is FOlocal1 -convergent.

Let φ ∈ FOlocal1 (thus φ is -local). Let > 0. There exists k ∈ N such that

i≤k spi > 1 − sp −  /3 and such that spk+1 < spk. We group the λ-structures Bn,i (for 1 ≤ i ≤ k) by values of spi as A n,1,...,A n,q. Denote by cj the common value of spi for the connected components Bn,i in A n,j. According to Lemma 3.55, each sequence (A n,i)n∈N is FO-convergent. Deﬁne

µi = lim

φ,A n,i .

n→∞

There exists N such that for every n > N the following inequality holds

q

| φ,A n,i − µi| <  /3.

i=1

According to Corollary 3.21 it holds, for every n > N, that φ,An =

|Bn,i| |An|

φ,Bn,i

i

C(n)

k

|An,i| |An|

|Bn,i| |An|

|Bn,i| |An|

=

φ,Bn,i +

φ,Bn,i +

φ,Bn,i

i=1

i=k+1

i>C(n)

C(n)

q

|Bn,i| |An|

φ,Bn,i + |Rn| |An|

=

ci φ,A n,i +

φ,Rn .

i=1

i=k+1

Thus we have

C(n)

q

q

sp φ,Rn − φ,An −

ciµi ≤

| φ,A n,i − µi| +

|Bn,i|/|An|

i=1

i=1

i=k+1

+ |Rn|/|An| − sp ≤  .

It follows that limn→∞ φ,Rn exists. By sorting the C(n) ﬁrst connected

components of each An according to both spi and Lemma 3.56 we obtain the following expression for the limit:

1 sp

φ,An −

spi lim

( lim

φ,Bn,i ).

lim

φ,Rn =

n→∞

n→∞

n→∞

i< C

Finally, we obtain the main results of this section.

Theorem 3.64 (Comb structure for λ-structure sequences with inﬁnite spectrum (local convergence)). Let (An)n∈N be an FOlocal-convergent sequence of ﬁnite λ-structures with component relation , support N, and spectrum (spi)i∈N. Let C : N → N be a clip of (An)n∈N, and let Rn be the residue of An with respect to C.

Then there exists, for each n ∈ N, a permutation fn : [C(n)] → [C(n)] such that, extending fn to N by putting f(i) to be the identity for i > C(n), the following holds:

- • limn→∞ maxi>C(n) |Bn,i|/|An| = 0;
- • sp = limn→∞ |Rn|/|An| exists;
- • for every i ∈ N, (Bn,f

n(i))n∈N is FO-convergent;

- • either sp = 0 or the sequence (Rn)n∈N is FOlocal-convergent.


Proof. This lemma is a direct consequence of the previous lemmas. We shall now extend the Comb structure theorem to full FO-convergence. In

contrast with the case of a ﬁnite -spectrum, the elementary convergence aspects will be non trivial and will require a careful choice of a clip for the sequence.

Lemma 3.65. Let (An)n∈N be an FOlocal-convergent sequence of ﬁnite λ-structures with component relation , such that limn→∞ |An| = ∞. Let Bn,i be the connected components of An. Assume that the connected components with same spi

G1 G2 G3

Gn

Hn,1 Hn,i Hn,C(n) Rn

λ1 λ2 λi 1 − i λi

Figure 7. Illustration of the Comb structure theorem

have been reshuﬄed according to Lemma 3.56, so that (Bn,i)i∈N is FO-convergent for each i ∈ N.

For i ∈ N, let Bi be an elementary limit of (Bn,i)n∈N. Then there exists a clip C such that the sequence (Rn)n∈N of the residues is elementarily convergent. Moreover, if R is an elementary limit of (Rn)n∈N, then i Bi∪ R is an elementary limit of (An)n∈N.

Let B n,i be either Bn,i if C(n) ≥ i or the empty λ-structure if C(n) < i. Then the family consisting in the sequences (B n,i)i∈N (i ∈ N) and of the sequence (Rn)n∈N is uniformly elementarily convergent.

Proof. Let A be an elementary limit of (An)n∈N. For θ ∈ FOlocal1 and m ∈ N we denote by θ(m) the sentence

m

θ(m) : (∃x1 ...∃xm)

¬ (xi,xj) ∧

θ(xi) .

1≤i<j≤m

i=1

According to Theorem 2.21, elementary convergence of a sequence of λ-structures with component relation can be checked by considering sentences of the form θ(k) for θ ∈ FOlocal1 and k ∈ N.

Note that for every k < k and every λ-structure A, if it holds that A |= θ(k ) then it holds that A |= θ(k). Deﬁne

M(θ) = sup{k ∈ N : A |= θ(k)}

Ω(θ) = {i ∈ N : Bi |= (∃x)θ(x)}. Note that obviously |Ω(θ)| ≤ M(θ). For r ∈ N, let θ1,...,θF(r) be an enumeration of the local ﬁrst-order formulas

with a single free variable with quantiﬁer rank at most r (up to logical equivalence). Deﬁne

maxΩ(θa)). Let

A(r) = max(r, max

a≤F(r)

K

|Bn ,i| |An |

C0(n) = sup K ∈ N : (∀n ≥ n)

− spi ≤

spi

i=1

i>K

be the standard (maximal) clip on (An)n∈N (see Proposition 3.61). Let B(r) be the minimum integer such that

- (1) it holds that C0(B(r)) ≥ A(r) (note that limn→∞ C0(n) = ∞, according to Proposition 3.61);
- (2) for every n ≥ B(r),a ≤ F(r) and every k ≤ r it holds that An |= θa(k) if and only if M(θa) ≥ k (note that this holds for suﬃciently large n as A is an elementary limit of (An)n∈N);
- (3) for every i ≤ A(r) and a ≤ F(r) the following equivalence holds: Bn,i |= (∃x)θa(x) ⇐⇒ Bi |= (∃x)θa(x).


(note that this holds for suﬃciently large n as Bi is an elementary limit of (Bn,i)n∈N and as we consider only ﬁnitely many values of i);

we deﬁne the non-decreasing function C : N → N by C(n) = max{A(r) : B(r) ≤ n}.

As limr→∞ A(r) = ∞ and as C0(B(r)) ≥ A(r) it holds that limr→∞ B(r) = ∞. Moreover, for every r ∈ N it holds that C0(B(r)) ≥ A(r) hence C0(n) ≥ C(n). According to Proposition 3.61, it follows that the function C is a clip on (An)n∈N.

Let (Rn)n∈N be the residue of (An)n∈N with respect to the clip C, and let B n,i be deﬁned as Bn,i if i ≤ C(n) and the empty λ-structure otherwise. Then it is immediate from the deﬁnition of the clip C that the family {(B n,i)n∈N : i ∈ N} is uniformly elementarily convergent. Using Lemma 3.23, it is also easily checked that the residue (Rn)n∈N of (An)n∈N with respect to the clip C is elementarily convergent and thus, that the family {(B n,i)n∈N : i ∈ N}∪{(Rn)n∈N} is uniformly elementarily convergent.

The extension of the Comb structure theorem to FO-convergence now follows directly.

Theorem 3.66 (Comb structure for λ-structure sequences with inﬁnite spectrum). Let (An)n∈N be an FO-convergent sequence of ﬁnite λ-structures with component relation and inﬁnite spectrum (spi)i∈N.

Then there exists a clip C : N → N with residue Rn and, for each n ∈ N, a permutation fn : [C(n)] → [C(n)] such that, extending fn to N by putting f(i) to be the identity for i > C(n), and letting B n,i be either Bn,f

n(i) if C(n) ≥ i or the empty λ-structure if C(n) < i, the following holds:

- • An = Rn ∪ i∈N B n,i;
- • limn→∞ maxi>C(n) |B n,i|/|An| = 0;
- • limn→∞ |Rn|/|An| exists;
- • for every i ∈ N, (B n,i)n∈N is FO-convergent;
- • either limn→∞ |Rn|/|An| = 0 and (Rn)n∈N is elementarily convergent, or the sequence (Rn)n∈N is FO-convergent;
- • the family {(B n,i)n∈N : i ∈ N} ∪ {(Rn)n∈N} is uniformly elementarily convergent.


This ends the (admittedly very technical and complicated) analysis of the component structure of limits. This was not developed for its own sake, but it will be all needed in the Part 3 of this paper, to construct modeling FO-limits for convergent sequences of trees with bounded height and, by means of a ﬁtting basic interpretation scheme, to graphs with bounded tree-depth (deﬁned in [68]), or graphs with bounded SC-depth (deﬁned in [41]).

In a broader sense, this detailed analysis was a cradle of much of the further research (see Addendum Section 5.2).

CHAPTER 4

## Limits of Graphs with Bounded Tree-depth

In this part, we mainly consider the signature λ, which consists in a binary relation ∼ (symmetric adjacency relation), a unary relation R (property of being a root), and c unary relations Ci (the coloring). Colored rooted trees with height at most h are particular λ-structures, and the class of (ﬁnite or inﬁnite) colored rooted trees with height at most h will be denoted by Y(h). (Here we shall be only concerned with trees that are either ﬁnite, countable, or of size continuum.)

###### 4.1. FO1-limits of Colored Rooted Trees with Bounded Height

In this section, we explicitly deﬁne modeling FO1-limits for FO1-convergent sequences of colored rooted trees with bounded height and characterize modelings which are FO1-limits for FO1-convergent sequences of (ﬁnite) colored rooted trees with bounded height.

4.1.1. Preliminary Observations. We take some time for some preliminary observations on the logical structure of rooted colored trees with bounded height. These observations will use arguments based on Ehrenfeucht-Fraı¨sse´ games and strategy stealing. (For deﬁnitions of ≡n and Ehrenfeucht-Fraı¨sse´ games, see Section 2.3.1.)

For a rooted colored tree Y ∈ Y(h) and a vertex x ∈ Y , we denote by Y(x) the subtree of Y rooted at x — that is the subtree of Y with root x induced by x and all its descendants — and (for a non-root x) by Y \ Y(x) the rooted tree obtained from Y by removing all the vertices in Y(x).

The following two lemmas show that, like for isomorphism, equivalence between two colored rooted trees can be reduced to equivalence of branches.

Lemma 4.1. Let Y,Y ∈ Y(h), let s,s be sons of the roots of Y and Y ,

respectively. Let n ∈ N. If Y(s) ≡n Y (s ) and Y \ Y(s) ≡n Y \ Y (s ), then Y ≡n Y . Proof. Assume Y(s) ≡n Y (s ) and Y \ Y(s) ≡n Y \ Y (s ). In order to

prove Y ≡n Y we play an n-step Ehrenfeucht-Fraı¨sse´-game EF0 on Y and Y as Duplicator. Our strategy will be based on two auxiliary n-step EhrenfeuchtFraı¨ss´e-games, EF1 and EF2, on Y(s) and Y (s ) and on Y \Y(s) and Y \Y (s ), respectively, against Duplicators following a winning strategy. Each time Spoiler selects a vertex in game EF0, we play the same vertex in the game EF1 or EF2 (depending on the tree the vertex belongs to), then we mimic the selection of the Duplicator of this game. It is easily checked that this strategy is a winning strategy.

Lemma 4.2. Let Y,Y ∈ Y(h), let s,s be sons of the roots of Y and Y , respectively.

79

Let n ∈ N. If Y ≡n+h Y and Y(s) ≡n Y (s ), then Y \ Y(s) ≡n Y \ Y (s ). Proof. Assume Y ≡n+h Y and Y(s) ≡n Y (s ).

We ﬁrst play (as Spoiler) s in Y then s in Y . Let t and t be the corresponding plays of Duplicator. Then the further n steps of the game have to map vertices in Y(s), Y(t), Y\(Y(s)∪Y(t)) to Y (t ), Y (s ), Y \(Y (t )∪Y (s )) (and converse), for otherwise h − 2 steps would allow Spoiler to win the game. Also, by restricting our play to one of these pairs of trees, we deduce Y(s) ≡n Y (t ), Y(t) ≡n Y (s ), and Y \ (Y(s) ∪ Y(t)) ≡n Y \ (Y (s ) ∪ Y (t )). As Y (s ) ≡n Y(s) it follows

Y(t) ≡n Y (s ) ≡n Y(s) ≡n Y (t ).

Hence, according to Lemma 4.1, as Y \ (Y(s) ∪ Y(t)) = (Y \ Y(s)) \ Y(t) and Y \(Y (s )∪Y (t )) = (Y \Y (s ))\Y (t ), we deduce Y\Y(s) ≡n Y \Y (s ).

Let λ• denote the signature obtained from λ by adding a new unary relation S

(marking a special vertex, which is not necessarily the root). Let θ• be the sentence (∃x)(S(x) ∧ (∀y S(y) → (y = x))),

which states that a λ• contains a unique special vertex. We denote by Y•(h) the class obtained by marking as special a single vertex of a colored rooted tree with height at most h. Let Unmark be the interpretation of λ-structures in λ•-structures consisting in forgetting S (so that Unmark projects Y•(h) onto Y(h)).

Lemma 4.3. Let Y,Y ∈ Y•(h) be such that Y (resp. Y ) has special vertex m (resp. m ). Assume that both m and m have height t > 1 (in Y and Y , respectively). Let v (resp. v ) be son of the root of Y (resp. Y ) that is an ancestor of m (resp. m ).

Then for every n ∈ N, if Unmark(Y) ≡n+h Unmark(Y ) and Y(v) ≡n Y (v ), then Y ≡n Y .

Proof. Assume Unmark(Y) ≡n+h Unmark(Y ) and Y(v) ≡n Y (v ). Then it holds that Unmark(Y(v)) ≡n Unmark(Y (v )) thus, according to Lemma 4.2,

Y \ Y(v) = Unmark(Y) \ Unmark(Y(v))

≡n Unmark(Y ) \ Unmark(Y (v )) = Y \ Y (v ).

Hence, according to Lemma 4.1, it holds that Y ≡n Y (as the marking could be considered as a coloring).

The next lemma states that the properties of a colored rooted trees with a distinguished vertex v (which is not necessarily the root) can be retrieved from the properties of the subtree rooted at v, the subtree rooted at the father of v, etc. (see Fig. 1).

Lemma 4.4. Let Y,Y ∈ Y(h), vt ∈ Y and v t ∈ Y be vertices with height t. For 1 ≤ i < t, let vi (resp. v i) be the ancestor of vt (resp. of v t) at height i.

Then for every integer n it holds that (∀1 ≤ i ≤ t) Y(vi) ≡n+h+1−i Y (v i) =⇒ (Y,vt) ≡n (Y ,v t) (Y,vt) ≡n+(t−1)h (Y ,v t) =⇒ (∀1 ≤ i ≤ t) Y(vi) ≡n+(t−i)h Y (v i)

vt = v

(Y,v)

vt vt−1

(Y1,Y2,...,Yt)

v1

Figure 1. Transformation of a rooted tree with a distinguished vertex (Y,vt) into a tuple of rooted trees (Y1,...,Yt).

Proof. We proceed by induction over t. If t = 1, then the statement obviously holds. So, assume t > 1 and that the statement holds for t − 1.

Let Y•,Y • ∈ Y•(h) be the marked rooted colored trees obtained from Y and Y by marking vt (resp. v t) as a special vertex.

Assume (∀1 ≤ i ≤ t) Y(vi) ≡n+h+1−i Y (v i). By induction, (∀2 ≤ i ≤ t) Y(vi) ≡n+(h−1)+1−(i−1) Y (v i) implies (Y(v2),vt) ≡n (Y (v 2),v t), that is Y•(v2) ≡n Y •(v 2). As Y ≡n+h Y , it follows from Lemma 4.3 that Y• ≡n Y •, that is: (Y,vt) ≡n (Y ,v t).

Conversely, if (Y,vt) ≡n+(t−1)h (Y ,v t) (i.e. Y• ≡n+(t−1)h Y •) an repeated application of Lemma 4.2 gives Y•(vi) ≡n+(t−i)h Y •(vi) hence (by forgetting the marking) Y(vi) ≡n+(t−i)h Y (vi) .

This lemma allows to encode the complete theory of a colored rooted tree Y of height at most h with special vertex v as a tuple of complete theories of colored rooted trees with height at most h.

In fact what follows could be described as a ﬁne analysis of the Stone dual of the Boolean algebra of all the formulas having a model in Y(h). As the height h is bounded, the classes Y(h) can be axiomatized by ﬁnitely many axioms (hence by some single axiom ηY(h)), it is a basic elementary class. For an integer p ≥ 0, we introduce a short notation for the Stone space associated to the Lindenbaum–Tarski algebra of formulas on Y(h) with p free variables:

Y(ph) = S(B(FOp(λ),ηY(h))).

We shall now move from models to theories, speciﬁcally from Y•(h) (colored rooted trees with height at most h and a special vertex) to the Stone space Y1(h) and from Y(h) (colored rooted trees with height at most h) to the Stone space Y(0h).

In that direction, we ﬁrst show how the notion of “property of the subtree Y(v) of Y rooted at the vertex v” translates into a relativization homomorphism

: B(FO0(λ)) → B(FO1(λ)).

We consider the simple interpretation I• of λ-structures in λ•-structures, which maps a λ•-structure Y• to the λ-structure deﬁned as follows: let x y be deﬁned as (x ∼ y) ∨ (x = y). Then

• the domain of I•(Y•) is deﬁned by the formula

- h−1
- i=1


S(x1) ∨ (∀y1,...,yh) R(y1) ∧

¬S(yi) ∧ (yi yi+1) → (yh = x1) ;

- • the adjacency relation ∼ is deﬁned as in Y• (i.e. by the formula (x1 ∼ x2));
- • the relation R of I•(Y•) is deﬁned by the formula S(x1).


Although I• maps general λ•-structures to λ-structures, we shall be only concerned by the speciﬁc property that I• maps a rooted tree Y• ∈ Y•(h) with special vertex v to the rooted tree Unmark(Y•)(v).

In a sake for simplicity, for Y ∈ Y(h) we denote by (Y,v) (where Y is a λstructure) the λ•-structure obtained by adding the new relation S with v being the unique special vertex.

Lemma 4.5. There is a Boolean algebra homomorphism : B(FO0(λ),ηY(h)) → B(FO1(λ),ηY(h))

(called relativization), such that for every sentence φ ∈ FO0(λ), every Y ∈ Y(h), and every v ∈ Y the following equivalence holds

Y(u) |= φ ⇐⇒ Y |= (φ)(u). Proof. The lemma follows from the property

Y(u) |= φ ⇐⇒ I•(Y,u) |= φ ⇐⇒ (Y,u) |=˜I•(φ).

The formula ρ(φ) is obtained from the sentence ˜I•(φ) by replacing each occurrence of S(y) by y = x1.

Using relativization and Lemma 4.4, we can translate the transformation shown on Figure 1 to a encoding of elements of Y(1h) into tuples of elements Y0(h). Intuitively, a element T ∈ Y(1h) deﬁnes the properties of a colored rooted tree Y with special vertex x1, and the relativization ρ allows us to extract from T the tuple of the complete theories of the subtrees of Y rooted at x1, the father of x1, etc. Moreover, the meaning of Lemma 4.4 is that what we obtain only depends on the complete theory of (Y,x1), that is only on T.

Definition 4.6. For 1 ≤ i ≤ h, let ηi ∈ FO1(λ) be the formula stating that

the height of x1 is i. We deﬁne the mapping Encode : Y(1h) → hk=1(Y(0h))k as follows: For T ∈ Y(1h), let k be the (unique) integer such that ηk ∈ T. Then Encode(T)

is the k-tuple (T0,...,Tk−1), where

- • Tk−1 is the set of sentences θ ∈ FO0(λ) such that ρ(θ) ∈ T (intuitively, the complete theory of the subtree rooted at x1);
- • Tk−2 is the set of sentences θ ∈ FO0(λ) such that (∃y1)(ηk−1(y1) ∧ y1 ∼ x1 ∧ ρ(θ)(y)) ∈ T

(intuitively, the complete theory of the subtree rooted at the father of x1);

- • Tk−1−i is the set of sentences θ ∈ FO0(λ) such that

(∃y1 ...yi)(

i

j=1

ηk−j(yj) ∧

- i−1
- j=1


(yj ∼ yj+1 ∧ y1 ∼ x1 ∧ ρ(θ)(yi) ∈ T

(intuitively, the complete theory of the subtree rooted at the ancestor of x1 which has height k − i);

- • T0 = T∩ ∈ FO0(λ) (intuitively, the complete theory of the whole rooted tree).


Lemma 4.7. Encode is a homeomorphism of Y(1h) and Encode(Y1(h)), which is a closed subspace of hk=1(Y(0h))k.

Proof. This lemma is a direct consequence of Lemma 4.4.

4.1.2. The Universal Relational Sample Space Yh. The aim of this section is to construct a rooted colored forest on a standard Borel space Yh that is FO1-universal, in the sense that every FO1-convergent sequence of colored rooted trees will have a modeling FO1-limit obtained by assigning an adapted probability measure to one of the connected components of Yh.

Definition 4.8. For theories T,T ∈ Y(0h), we deﬁne w(T,T ) ≥ k if and only if there exists a model Y of T, such that the root of Y has k (distinct) sons v1,...,vk with Th(Y(vi)) = T .

Lemma 4.9. For k ∈ N and φ ∈ FO0, let ζk(φ) be the sentence (∃≥ky) ρ(φ)(y). Then w(T,T ) ≥ k if and only if ζk(φ) ∈ T holds for every φ ∈ T .

Proof. If w(T,T ) ≥ k, then ζk(φ) ∈ T holds for every φ ∈ T , hence we only have to prove the opposite direction. Assume that ζk(φ) ∈ T holds for every φ ∈ T , but that there is φ0 ∈ T such that ζk+1(φ0) ∈/ T. Let Y be a model of T, and let v1,...,vk be the sons of the root of Y such that Y (vi) |= φ0. For every r ∈ N, r ≥ qrank(φ0), let ψr be the conjunction of the sentences in T with quantiﬁer rank r. Obviously, ψr ∈ T . Moreover, as ζk(ψr) ∈ T, it holds that Y |= ζk(ψr). As ψr φ0, it follows that for every 1 ≤ i ≤ k it holds that Y (vi) |= ψr (only possible choices). As this holds for every r, we infer that for every 1 ≤ i ≤ k, Y (vi) is a model of T hence w(T,T ) ≥ k. Now assume that for every k ∈ N and every φ ∈ T it holds that ζk(φ) ∈ T. Let Y be a model of T, let Y be a model of T , and let Y˜ be obtained from Y by adding (at the root of Y ) a son u with subtree Y˜(u) isomorphic to Y . By an easy application of an Ehrenfeucht-Fraı¨ss´e game, we get that Y˜ is elementarily equivalent to Y , hence a model of T. Thus w(T,T ) ≥ k.

Let N be the one point compactiﬁcation of N, that is N = N ∪ {∞} with open sets generated by complements of ﬁnite sets.

Lemma 4.10. The function w : Y(0h) ×Y0(h) → N is upper semicontinuous (with respect to product topology of Stone space Y(0h)).

Proof. For r ∈ N deﬁne the function wr : Y0(h) × Y(0h) → N by:

wr(T,T ) = sup{k ∈ N : ∀ψ ∈ T (qrank(ψ) ≤ r) ⇒ ζk(ψ) ∈ T}. It follows from Lemma 4.9 that the following equation holds

w(T,T ) = inf

wr(T,T ).

r∈N

Hence, in order to prove that the function w is upper semicontinuous, it is suﬃcient to prove that the functions wr are continuous. Let (T0,T 0) ∈ Y0(h) × Y(0h). We distinguish two cases:

– Firstly, assume wr(T0,T 0) = k. If dist(T ,T 0) < 2−r and dist(T,T0) < 2−max{qrank(ζ

k+1(ψ)): qrank(ψ)≤r}, then it holds that wr(T,T ) = wr(T0,T 0);

– Secondly, assume wr(T0,T 0) = ∞, and let k ∈ N. If dist(T ,T 0) < 2−r and dist(T,T0) < 2−max{qrank(ζ

k+1(ψ)): qrank(ψ)≤r}, then it holds that wr(T,T ) > k.

For z = (z1,...,za) ∈ Na deﬁne the subset Fz of (Y0(h))a+1 by

Fz = {(T0,...,Ta) : w(Ti−1,Ti) = zi}. For t ∈ N, deﬁne

Xt = {1,...,t}, if t ∈ N,

[0,1], if t = ∞. For z = (z1,...,za) ∈ Na, deﬁne Xz = ai=1 Xz

. Let

i

h−1

Vh = Y(0h)

(Fz × Xz).

a=1 z∈Na

Definition 4.11. The universal forest Yh has vertex set Vh. The roots of Yh are the elements in Y(0h). The edges of Yh are the pairs of the form

{((T0,T1,...,Ta),(α1,...,αa)),((T0,T1,...,Ta+1),(α1,...,αa+1))} where Ti ∈ Y(0h), αi ∈ [0,1] and a ∈ {0,...,h − 1}.

Moreover, the vertex set Vh inherits the topological structure of hi=1(Y(0h))i × [0,1]i−1, which deﬁnes a σ-algebra Σh on Vh (as the trace on Vh of the Borel σalgebra of hi=1(Y(0h))i × [0,1]i−1).

Remark 4.12. Let T0 be the complete complete theory of a colored rooted tree with height at most h. Then, by construction, T0 is the complete theory of the connected component of Yh rooted at T0. In particular, no two connected components of Yh are elementarily equivalent.

The remaining of this section will be devoted to the proof of Theorem 4.14, which states that Yh is a relational sample space. In order to prove this result, we shall need a preliminary lemma, which expresses that the property of a tuple of vertices in a colored rooted tree with bounded height is completely determined by the individual properties of the vertices in the tuple and the heights of the lowest common ancestors of every pair of vertices in the tuples.

Lemma 4.13. Fix rooted trees Y,Y ∈ Y(h). Let u1,...,up be p vertices of Y, let u 1,...,u p be p vertices of Y , and let n ∈ N.

Assume that for every 1 ≤ i ≤ p it holds that (Y,ui) ≡n+h (Y ,u i) and that for every 1 ≤ i,j ≤ p the height of ui ∧ uj in Y is the same as the height of u i ∧ u j in Y (where u ∧ v denotes the lowest common ancestor of u and v).

Then (Y,ui,...,up) ≡n (Y ,u 1,...,u p). Proof. In the proof we consider p+1 simultaneous Ehrenfeucht-Fraı¨ss´e games

(see Fig. 2).

D1

D

D2

D S

S

S D

S M

S S D

Dt−1

D

Dt

Figure 2. Schematic representation of how a winning strategy for EF((Y,u1,...,up),(Y ,u 1,...,u p),n) is built using p auxiliary games EF((Y,ui),(Y ,u i),n + h).

Consider an n-step Ehrenfeucht-Fraı¨ss´e EF((Y,u1,...,up),(Y ,u 1,...,u p),n) on (Y,u1,...,up) and (Y ,u 1,...,u p). We build a strategy for Duplicator by considering p auxiliary Ehrenfeucht-Fraı¨ss´e games EF((Y,ui),(Y ,u i),n + h) on (Y,ui) and (Y ,u i) (for 1 ≤ i ≤ p) where we play the role of Spoiler against Duplicators having a winning strategy for (n + h)-step games.

For every vertex v ∈ Y (resp. v ∈ Y ) let p(v) (resp. p (v)) be the maximum ancestor of v (in the sense of the furthest from the root) such that p(v) ≤ ui (resp. p (v) ≤ u i) for some 1 ≤ i ≤ p. We partition Y and Y as follows: for every vertex

- v ∈ Y (resp. v ∈ Y ) we put v ∈ Vi (resp. v ∈ V i ) if i is the minimum integer such that p(v) ≤ ui (resp. such that p (v) ≤ u i), see Fig 3.


Note that each Vi (resp. V i induces a connected subgraph of Y (resp. of Y ). Assume that at round j ≤ n, Spoiler plays a vertex v ∈ (Y,u1,...,up) (resp.

a vertex v ∈ (Y ,u 1,...,u p)).

If v ∈ Vi (resp. v ∈ V i ) for some 1 ≤ i ≤ p then we play v (resp. v ) on (Y,ui) (resp. (Y ,u i)). We play Duplicator on (Y ,u 1,...,u p) (resp. on (Y,u1,...,up)) with the same move as our Duplicator opponent did on (Y ,ui) (resp. on (Y,ui)). If such a move is not legal (i.e. does not deﬁne a local isomorphism) then it is

V2

V4

u2 u1 u3 u4

V1

V3

Figure 3. The partition (V1,V2,V3,V4) of Y induced by (u1,u2,u3,u4).

easily checked that h additional moves (at most) are suﬃcient for at least one of the Spoilers to win one of the p games, contradicting the hypothesis of p winning strategies for Duplicators. It follows that (Y,ui,...,up) ≡n (Y ,u 1,...,u p).

Theorem 4.14. The rooted colored forest Yh (equipped with the σ-algebra Σh) is a relational sample space.

Proof. It suﬃces to prove that for every p ∈ N and every ϕ ∈ FOp the set Ωϕ(Yh) = {(v1,...,vp) ∈ Vhp : Yh |= ϕ(v1,...,vp)}

is measurable. Let ϕ ∈ FOp and let n = qrank(ϕ). We partition Vh into equivalence classes modulo ≡n+h, which we denote

C1,...,CN. Let i1,...,ip ∈ [N] and, for 1 ≤ j ≤ p, let vj and v j belong to Ci

.

j

According to Lemma 4.13, if the heights of the lowest common ancestors of the pairs in (v1,...,vp) coincide with the heights of the lowest common ancestors of the pairs in (v 1,...,v p) then it holds that

(Yh,v1,...,vp) ≡n (Yh,v 1,...,v p) thus (v1,...,vp) ∈ Ωϕ(Yh) if and only if (v 1,...,v p) ∈ Ωϕ(Yh).

It follows from Lemma 4.7 (and the deﬁnition of Vh and Σh) that each Cj is measurable. According to Lemma 4.7 and the encoding of the vertices of Vh, the conditions on the heights of lowest common ancestors rewrite as equalities and inequalities of coordinates. It follows that Ωϕ(Yh) is measurable.

4.1.3. Modeling FO1-limits of Colored Rooted Trees with Bounded Height. Let (Yn)n∈N be an FO1-convergent of colored rooted trees with height at most h, and let Y be the connected component of Yh that is an elementary limit

of (Yn)n∈N. According to Lemma 3.3, Y is a relational sample space. We have to transfer the measure µ we obtained in Theorem 2.7 on S(B(FO1)) to Y.

Definition 4.15. Let µ be a measure on Y1(h). We deﬁne ν on Yh as follows: let µ = Encode∗(µ) be the pushforward of µ by Encode (see page 13). For t ∈ N we equip Xt with uniform discrete probability measure if t < ∞ and the Haar probability measure if t = ∞. For z ∈ Na, Xz is equipped with the corresponding product measure, which we denote by λz (not to be confused with signature λ).

We deﬁne the measure ν as follows: let A be a measurable subset of Vh, let A0 = A ∩ Y(0h), and let Az = A ∩ (Fz × Xz). Then

h−1

( µ ⊗ λz)(Az).

ν(A) = µ(A0) +

a=1 z∈Na

(Notice that the sets Az are measurable as Fz × Xz is measurable for every z.)

Lemma 4.16. The measure µ is the push-forward of ν by the projection P : Yh → Y(1h) deﬁned by

P((T0,T1,α1,...,Ta,αa)) = Encode−1(T0,...,Ta), that is: µ = P∗(ν).

Proof. First notice that P is continuous, as Encode is a homeomorphism

(by Lemma 4.7). Let B be a measurable set of Y(1h). Let A = P−1(B). Then A ∩ (Fz × Xz) = (Encode(B) ∩ Fz) × Xz hence

( µ ⊗ λz)(A ∩ (Fz × Xz)) = ν(Encode(B) ∩ Fz)λz(Xz) = µ(Encode(B) ∩ Fz). It follows that

P∗(ν)(B) = ν(A)

h−1

= µ(A ∩ Y(0h)) +

( µ ⊗ λz)(A ∩ (Fz × Xz))

a=1 z∈Na

h−1

= µ(Encode(B) ∩ Y(0h)) +

µ(Encode(B) ∩ Fz)

a=1 z∈Na

h−1

= µ Encode(B) ∩ (Y(0h)

Fz)

a=1 z∈Na

= µ ◦ Encode(B)

= µ(B).

(as z ranges over a countable set and as all the Fz are measurable). Hence µ = P∗(ν).

Lemma 4.17. Let µ be a pure measure on Y(1h) and let T0 be the complete theory of µ (see Deﬁnition 2.9). Let ν be the measure deﬁned from µ by Deﬁnition 4.15. Let Y be the connected component of Yh containing the support of ν. Let ν Y be the restriction of ν to Y.

Then Y, equipped with the probability measure ν Y is a modeling such that for every ϕ ∈ FO1 the following equality holds

ϕ, Y = µ(K(ϕ)).

Let X ⊂ Y(1h) be the set of all T ∈ Y1(h) such that x1 is not the root (i.e. X = {T ∈ Y(1h) : R(x1) ∈/ T}). Let f : X → Y(0h) be the second projection of Encode (if Encode(T) = (T0,...,Ti) then f(T) = T1). Let κ = f∗(µ) be the pushforward of µ by f. Intuitively, for T ∈ Y(0h), κ({T}) is the global measure of all the subtrees with complete theory T that are rooted at a son of the root.

Let r Y be the root of Y. Then it holds that sup

κ({T}) w(T0,T)

.

ν Y( Y(v)) = sup T∈X

v∼r Y

Proof. As µ is pure, the complete theory of µ is the theory T0 to which every point of the support of µ projects. Hence the support of µ deﬁnes a unique connected component Y of Yh. That for every ϕ ∈ FO1 it holds that

ϕ, Y = µ(K(ϕ))

is a direct consequence of Lemma 4.16. The second equation is a direct consequence of the construction of ν Y. Theorem 4.18. Let Yn be an FO1-convergent sequence of colored rooted trees

on Y(1h). Let ν be the measure deﬁned from µ by Deﬁnition 4.15. Let Y be the connected component of Yh containing the support of ν. Let ν Y be the restriction of ν to Y.

with height at most h, and let µ be the limit measure of µY

n

Then Y, equipped with the probability measure ν Y, is a modeling FO1-limit of (Yn)n∈N.

Moreover, it holds that sup

|Yn(v)| |Yn|

ν Y( Y(v)) ≤ liminf

.

max

n→∞

v∼rYn

v∼r Y

Proof. As (Yn)n∈N is elementarily convergent, the complete theory of the elementary limit of this sequence is the theory T0 to which every point of the support of µ projects, hence µ is pure. According to Lemma 4.17, Y is an FO1modeling limit of (Yn)n∈N.

ν Y( Y(v)) = 0 hence the inequation holds.

Let κ be deﬁned as in Lemma 4.17. If κ is atomless, then supv∼r

Y

Let T be such that κ({T}) > 0. For every > 0 there exists θ ∈ T such that

κ({T}) ≤ κ({T : T θ }) ≤ κ({T}) +  . Moreover, it follows from Lemma 4.9 that

{w(T0,T ) : T θ }.

w(T0,T) = lim →0

Then, as (Yn)n∈N is elementarily convergent to a rooted tree with theory T0 it holds that

w(T0,T) = lim →0

= lim

→0

lim

lim

|{v ∈ Yn : v ∼ rY

and Yn(v) |= θ }|

n

n→∞

|{v ∈ Yn : Yn |= (v ∼ rY

) ∧ ρ(θ )(v)}|.

n

n→∞

As limn→∞ |{v ∈ Yn : Yn |= (v ∼ rY

) ∧ ρ(θ )(v)}| is non-increasing when → 0, and is a non-negative integer or ∞, there exists 0 such that for every 0 < < 0 it holds that

n

|{v ∈ Yn : Yn |= (v ∼ rY

w(T0,T) = lim

n

n→∞

) ∧ ρ(θ )(v)}|.

For > 0, let φ be the formula stating that the subtree rooted at a son of the root that contains x1 satisﬁes θ . Then it holds that

κ({T : T θ }) = µ(K(φ ))

= lim

φ ,Yn

n→∞

|Yn(v)| : Yn |= (v ∼ rY

) ∧ ρ(θ )(v) |Yn|

n

= lim

n→∞

Hence, for every 0 < < 0 it holds that

+ |Y

n(v)|

|Yn| : Yn |= (v ∼ rY

) ∧ ρ(θ )(v) |{v ∈ Yn : Yn |= (v ∼ rY

n

κ({T}) w(T0,T) ≤ lim

) ∧ ρ(θ )(v)}| ≤ + liminf

n→∞

n

max |Yn(v)| |Yn|

: Yn |= (v ∼ rY

) ∧ ρ(θ )(v)

n

n→∞

|Yn(v)| |Yn|

≤ + liminf

max

.

n→∞

v∼rYn

Hence

κ({T}) w(T0,T) ≤ liminf

|Yn(v)| |Yn|

max

.

n→∞

v∼rYn

###### 4.1.4. Inverse Theorems for FO1-limits of Colored Rooted Trees with Bounded Height. We characterize here the measures µ on S(B(FO1)), which are weak limits of measures µY

for some FO1-convergent sequence (Yn)n∈N of colored rooted trees with height at most h.

n

Fact 4.19. If (Yn)n∈N is an FO1-convergent sequence of colored rooted trees with height at most h, then µ is pure and its complete theory is the limit in S(B(FO0)) of the complete theories of the rooted trees Yn.

We now deﬁne a Finitary Mass Transport Principle for probability measures on a the Stone dual of B(FOp(λ)), in a similar way that a Finitary Mass Transport Principle was introduced for modelings in Section 2.1.4.

Definition 4.20. A probability measure µ on S(B(FOp(λ))) (p ≥ 1) or S(B(FO(λ))) satisﬁes the Finitary Mass Transport Principle (FMTP) if for every φ,ψ ∈ FO1(λ) and all integers a,b such that

φ (∃≥ay)(x1 ∼ y) ∧ ψ(y) ψ (∃≤by)(x1 ∼ y) ∧ ψ(y)

it holds that

aµ(K(φ)) ≤ bµ(K(ψ)).

Similarly, a modeling L satisﬁes the FMTP if, for every φ,ψ,a,b as above the following holds (see Fig. 4):

a φ,L ≤ b ψ,L .

#### L

B = Ωψ(L)

##### ≤ b =⇒ aνL(A) ≤ bνL(B)

≥ a

A = Ωφ(L)

Figure 4. A modeling L satisﬁes the FMTP if, for every ﬁrstorder deﬁnable subsets A,B of L and all integers a,b with the property that every element in A has at least b neighbors in B and every element in B has at most b neighbors in A, it holds that aνL(A) ≤ bνL(B) .

Fact 4.21. Every ﬁnite structure A satisﬁes the FMTP and, consequently, the measures µA associated to A on S(B(FOp)) (p ≥ 1) and S(B(FO)) satisfy the FMTP.

Let r ∈ N. We denote by FO(1r) the fragment of FO1 with formulas having quantiﬁer-rank at most r. Note that B(FO(1r)) is a ﬁnite Boolean algebra, hence S(B(FO(1r))) is a ﬁnite space.

The following approximation lemma lies in the center of our inverse argument. Lemma 4.22. Let µ be a pure measure on S(B(FO1(λ))) with support in Y1(h)

that satisﬁes the FMTP. Then, for every integer r ≥ 1 there exist integer C = C(λ,r) such that for every N ∈ N there is a colored rooted tree YN with the following properties:

- (1) N ≤ |YN| ≤ N + C;


- (2) for every ϕ ∈ FO1 with quantiﬁer rank at most r it holds that ϕ,YN − µ(K(ϕ)) ≤ C/N.
- (3) the trees YN (with root rN) are balanced in the following sense: for every modeling L (with root rL) such that φ,L = µ(K(φ)) holds for every φ ∈ FO1, we have


|YN(v)| |YN|

1 r + h

≤ max

max

, sup

νL(L(v)) + C/N.

v∼rN

v∼rL

Proof. Note that it is suﬃcient to prove that there exists C such that for every N ≥ C the statement holds (as the initial statement obviously holds with constant 2C instead of C).

For integers k,r and a sentence φ ∈ FO0(λ), let ζk(φ) be the sentence

(∃≥ky) (φ)(y), and let

c(s,k) = k + 1 + max{qrank(ζk(φ)) : φ ∈ FO0(λ) and qrank(φ) ≤ s}. For formulas φ,ψ we deﬁne

 

0 if φ y (ψ)(y) k if 0 < k < r + h, φ ζk(ψ), and φ ζk+1(ψ) r + h otherwise.

w (φ,ψ) =



Let T,T ∈ Y(0h) be complete theories of rooted trees, let a,b are integers such that a ≥ c(b,r + h), let φ = (T ∩ FO(0a)), and let ψ = (T ∩ FO0(b)). Then either w (φ,ψ) < r + h or φ ζr+h(ψ). This means that for any model Y of T, either w (φ,ψ) < r + h and the root of Y has exactly w (φ,ψ) sons v such that Th(Y(v)) ∩ FO(0b) = T ∩ FO(0b), or w (φ,ψ) = r + h and the root of Y has at least r + h sons v such that Th(Y(v)) ∩ FO0(b) = T ∩ FO(0b).

Let µ = Encode∗(µ) (see Lemma 4.7) be the pushforward of µ on hi=1(Y(0h))i. For a given integer r, we deﬁne integers ar,0,ar,1,...,ar,h−1 by

ar,h−1 = r + h, ar,h−2 = c(ar,h−1,r + h),..., ar,0 = c(ar,1,r + h). Let F be the mapping deﬁned on hi=1(Y(0h))i by

F(T0,...,Ti) = (T0 ∩ FO(0ar,0),...,Ti ∩ FO(0ar,i)).

We note that X = F hi=1(Y(0h))i is a ﬁnite space, and we endow X with the discrete topology. (Note that F is continuous.) We deﬁne the probability measure

µ(r) = F∗( µ) on X as the pushforward of µ by F. We will construct disjoint sets VTˆ

0,...,Tˆi indexed by the elements (Tˆ0,...,Tˆi) of X. To construct these sets, it will be suﬃcient to deﬁne their cardinalities and the unary relations that apply to their elements. We proceed inductively on the length of the index tuple. As µ is pure, X contains a unique 1-tuple (Tˆ0), and we let the set VTˆ

will be the root of the approximation tree YN. Hence we let R(v) and for every color relation Ci we let Ci(r) if (∀x)R(x) → Ci(x) belongs to Tˆ0. Assume sets VTˆ

###### to be a singleton. The unique element r of VTˆ

0

0

0,...,Tˆj have been

constructed for every 0 ≤ j ≤ i and every (Tˆ0,...,Tˆj) ∈ X. Let (Tˆ0,...,Tˆi+1) ∈ X. Then of course (Tˆ0,...,Tˆi) ∈ X.

- • If µ(r)({(Tˆ0,...,Tˆi)}) = 0 and µ(r)({(Tˆ0,...,Tˆi+1)}) = 0 then

|VTˆ

0,...,Tˆi+1| = w ( T ˆi, T ˆi+1)|VTˆ

0,...,Tˆi|;

- • If µ(r)({(Tˆ0,...,Tˆi)}) > 0 and µ(r)({(Tˆ0,...,Tˆi+1)}) = 0 then (according

to FMTP) w ( T ˆi, T ˆi+1) = 0 and we let VTˆ

0,...,Tˆi = ∅;

- • If µ(r)({(Tˆ0,...,Tˆi)}) = 0 and µ(r)({(Tˆ0,...,Tˆi+1)}) > 0 then (according to FMTP) w ( T ˆi, T ˆi+1) = r + h and we let

|VTˆ

0,...,Tˆi+1| = max((r + h)|VTˆ

0,...,Tˆi|, µ(r)({(Tˆ0,...,Tˆi+1)})N ).

- • Otherwise µ(r)({(Tˆ0,...,Tˆi)}) > 0 and µ(r)({(Tˆ0,...,Tˆi+1)}) > 0. In this case, according to FMTP, it holds that


µ(r)({(Tˆ0,...,Tˆi+1)}) µ(r)({(Tˆ0,...,Tˆi)})

w ( T ˆi, T ˆi+1) = min r + h,

,

Then, if w ( T ˆi, T ˆi+1) < r + h we let |VTˆ

0,...,Tˆi+1| = w ( T ˆi, T ˆi+1)|VTˆ

0,...,Tˆi|

and otherwise we let |VTˆ

0,...,Tˆi|, µ(r)({(Tˆ0,...,Tˆi+1)})N ). The colors of the elements of VTˆ

0,...,Tˆi+1| = max((r + h)|VTˆ

1,...,Tˆi are easily deﬁned: for v ∈ VTˆ

1,...,Tˆi and color relation Ci we let Ci(v) if (∀x)R(x) → Ci(x) belongs to Tˆi.

0,...,Tˆi+1 is partitioned as equally as possible into |VTˆ

The tree YN has vertex set VTˆ

1,...,Tˆi. Each set VTˆ

0,...,Tˆi| parts, each part being adjacent to a single vertex in VTˆ

0,...,Tˆi lies between  |VTˆ

0,...,Tˆi. It follows that the degree in VTˆ

0,...,Tˆi+1 of a vertex in VTˆ

0,...,Tˆi| , and that (by construction and thanks to FMTP) this coincides with w ( T ˆi, T ˆi+1) (when < r +h) or is at least

0,...,Tˆi+1|/|VTˆ

0,...,Tˆi|  and  |VTˆ

0,...,Tˆi+1|/|VTˆ

- w ( T ˆi, T ˆi+1) (when = r + h). For (Tˆ0,...,Tˆi) ∈ X, it is easily checked that


0,...,Tˆi| − µ({(Tˆ0,...,Tˆi)})N ≤ (r + h)i.

|VTˆ

For φ ∈ FO1(λ), let Fφ = {F ◦ Encode(T) : T ∈ K(φ) ∩ Y(1h)}. Let C = (r + h)h|X|. Then, by summing up the above inequality, we get

0 ≤

|VTˆ

0,...,Tˆi| − µ(K(ϕ))N ≤ C.

(Tˆ0,...,Tˆi)∈Fϕ

In particular, if φ is the true statement, we get N ≤ |YN| ≤ N + C. Also, we deduce that for every (Tˆ0,Tˆ1) ∈ X and every v1,v2 ∈ VTˆ

0,Tˆ1 the following inequality holds

|YN(v1)| − |YN(v2)| ≤ C.

Let Z = {T ∈ Y(1h) : T ∩FO0(λ) = T0}, let T ∈ Z, let (T0,...,Ti) = Encode(T), and let (Tˆ0,...,Tˆi) = F(T0,...,Ti). We now prove that if v ∈ VTˆ

0,...,Tˆi and

(T 0,...,T i) = Encode(Th(YN,v)) then it holds that Tj ∩ FO0(r+h) = T j ∩ FO0(r+h) for every 1 ≤ j ≤ i (see Fig 4.1.4).

T T = Th(YN,v) Y(1h)

| | |
|---|---|
| | |
| | |


Encode

Encode

v (T0,...,Ti)

(T 0,...,T i) i=1(Y(0h))i

h

VTˆ

0,...,Tˆi

YN

F

(Tˆ0,...,Tˆi) X

- h
- i=1(S(B(FO(0r+h)))i


( T0,..., Ti)

Figure 5. Comparing T with its approximation in YN

First note that it is suﬃcient to prove Ti∩FO0(r+h) = T i ∩FO0(r+h), as the other equalities follow by considering the ancestors of v. If Ti (hence T i) is the complete theory of a single vertex tree, then by construction of VTˆ

0,...,Tˆi, it holds that Ti = T i. Assume now that i is such that for every (T0,...,Ti+1) ∈ Encode(T) with T ∈ Z, it holds that Ti+1 ∩ FO(0r+h) = T i+1 ∩ FO0(r+h). Let A be a model of Ti and let B be a model of T i. It follows from the induction that the roots of A and B have the same number of sons (up to r + h) with subtrees, which are (r + h)-equivalent to a ﬁxed rooted tree. By an easy argument based on an Ehrenfeucht-Fraı¨ss´e game, it follows that A and B are (r + h)-equivalent hence Ti ∩ FO0(r+h) = T i ∩ FO0(r+h).

According to Lemma 4.4, we deduce that for T ∈ Z and the corresponding vertex v ∈ VTˆ

0,...,Tˆi it holds that Th(YN,v) ∩ FO(1r) = T ∩ FO(1r). It follows that for every ϕ ∈ FO(1r) the following equation holds:

|VTˆ

0,...,Tˆi| |YN|

ϕ,YN =

.

(Tˆ0,...,Tˆi)∈Fϕ

Hence

ϕ,YN − µ(K(ϕ)) ≤ C/N. Let rN be the root of YN. Deﬁne

|YN(v)| |YN|

. Assume L is a modeling with FO1 statistics µ and root rL. Let (Tˆ0,Tˆ1) ∈ X (vertices in VTˆ

αN = max v∼rN

0,Tˆ1 are sons of the root of YN). By construction, all the subtrees rooted at a vertex in VTˆ

0,Tˆ1 have almost the same number of vertices

(the diﬀerence being at most C). If w (Tˆ0,Tˆ1) = r +h, it follows that for every v ∈ VTˆ

0,Tˆ1 it holds that |YN(v)| ≤ C+|YN|/(r+h), i.e. |YN(v)|/|YN| ≤ 1/(r+h)+C/N. Otherwise, w (Tˆ0,Tˆ1) = k < r+h hence if ψ is the formula stating that the ancestor of x1 which is a son of the root satisﬁes T ˆ1, then

νL(L(v)) ≤ k sup v∼rL

µ(K(ψ)) = ψ,L =

νL(L(v)).

v∼rL,L|=ψ(v)

Also

0,...,Tˆi| |YN|

|VTˆ

C N ≥ ψ,YN =

µ(K(ψ)) +

(Tˆ0,...,Tˆi)∈Fψ

|YN(v)| |YN|

###### =

v∼rN,Yn|=ψ(v)

|YN(v)|

hence µ(K(ψ)) + NC ≥ maxv∼r

|YN| if k = 1, and otherwise µ(K(ψ)) +

N,Yn|=ψ(v)

|YN(v)| − C |YN| ≥ k max

C N ≥ k max

v∼rN,Yn|=ψ(v)

|YN(v)| |YN|

− C/N. Hence, considering the case k = 1 and the case k ≥ 2 (where 2C/k ≤ C) we get max

v∼rN,Yn|=ψ(v)

|YN(v)| |YN|

≤ sup

νL(L(v)) + C/N. And we deduce

v∼rN,Yn|=ψ(v)

v∼rL

1 r + h

αN ≤ max

, sup

νL(L(v)) + C/N.

v∼rL

Summarizing, we get the following two inverse results:

Theorem 4.23. A measure µ on S(B(FO1)) is the weak limit of a sequence of measures µY

associated to an FO1-convergent sequence (Yn)n∈N of ﬁnite colored rooted trees with height at most h (i.e. of ﬁnite Yn ∈ Y(h)) if and only if

n

- • µ is pure and its complete theory belongs to Y0(h),
- • µ satisﬁes the FMTP.


Proof. Assume that (Yn)n∈N is an FO1-convergent sequence of ﬁnite Yn ∈ Y(h), and that µY

N ⇒ µ. According to Remark 2.10, µ is pure. As (Yn)n∈N is elementarily convergent, the complete theory of µ is the complete theory of the elementary limit of (Yn)n∈N. Also, µ satisﬁes the FMTP (see Section 2.1.4).

Conversely, assume µ is pure, that its complete theory belongs to Y(0h), and that it satisﬁes the FMTP. According to Lemma 4.22 we can construct a sequence (Yn)n∈N of ﬁnite Yn ∈ Y(h) (considering for instance r = n and N = 10C where C is the constant deﬁned from r,h,c) such that for every formula φ ∈ FO1(λ) it holds that φ,Yn − µ(K(φ)) → 0 as n → ∞, i.e. µY

n ⇒ µ.

From this we deduce

Theorem 4.24. A modeling L is the FO1-limit of an FO1-convergent sequence (Yn)n∈N of ﬁnite colored rooted trees with height at most h (i.e. of ﬁnite Yn ∈ Y(h)) if and only if

- • L is a colored rooted tree with height at most h (i.e. L ∈ Y(h)),
- • L satisﬁes the FMTP.


Proof. That an FO1-convergent sequence of ﬁnite rooted colored trees Yn ∈ Y(h) has a modeling FO1-limit is a direct consequence of Theorem 4.18. That L satisﬁes the FMTP is immediate (as the associated measure µ = 1Tp

L ∗(νL) does).

Conversely, that a colored rooted tree modeling L ∈ Y(h) that satisﬁes the FMTP is the FO1-limit of a sequence of ﬁnite rooted colored trees Yn ∈ Y(h) is a direct consequence of Theorem 4.23.

###### 4.2. FO-limits of Colored Rooted Trees with Bounded Height

In this section we explicitly deﬁne modeling FO-limits for FO-convergent se-

quences of colored rooted trees with bounded height. We ﬁrst sketch our method. We consider the signature λ+, which is the signature λ augmented by a new unary relation P. Particular λ+-structures are colored rooted forests with a principal connected component, whose root will be marked by relation P instead of R (no other vertex gets P). The class of colored rooted forests with a principal connected component and height at most h will be denoted by F(h).

We consider three basic interpretation schemes:

- (1) IY →F is a basic interpretation scheme of λ+-structures in λ-structures deﬁned as follows: for every λ-structure A, the domain of IY →F(A) is the same as the domain of A, and the following holds (for every x,y ∈ A):

IY →F(A) |= x ∼ y ⇐⇒ A |= (x ∼ y) ∧ ¬R(x) ∧ ¬R(y) IY →F(A) |= R(x) ⇐⇒ A |= (∃z) R(z) ∧ (z ∼ x) IY →F(A) |= P(x) ⇐⇒ A |= R(x)

In particular, IY →F maps a colored rooted tree Y ∈ Y(h) into a colored rooted forest IY →F(A)(Y ) ∈ F(h−1), formed by the subtrees rooted at the sons of the former root and a single vertex rooted principal component (the former root);

- (2) IF→Y is a basic interpretation scheme of λ-structures in λ+-structures deﬁned as follows: for every λ+-structure A, the domain of IF→Y (A) is the same as the domain of A, and the following holds (for every x,y ∈ A):


IF→A(A) |= x ∼ y ⇐⇒ A |= (x ∼ y) ∨ R(x) ∧ P(y) ∨ R(y) ∧ P(x) IF→A(A) |= R(x) ⇐⇒ A |= P(x)

In particular, IF→Y maps a colored rooted forest F ∈ F(h) into a colored rooted tree IF→Y (F) ∈ Y(h+1) by making each non-principal root a son of the principal root;

- (3) IR→P is a basic interpretation scheme of λ+-structures in λ-structures deﬁned as follows: for every λ+-structure A, the domain of IR→P(A) is the same as the domain of A, adjacencies are the same in A and IR→P(A), no element of IR→P(A) is in R, and for every x ∈ A the following equivalence holds:


IR→P(A) |= P(x) ⇐⇒ A |= R(x).

(Roughly speaking, the relation R becomes the relation P.) In particular, IR→P maps a colored rooted tree Y ∈ Y(h) into a colored rooted forest IR→P(Y ) ∈ F(h) having a single (principal) component.

We now outline our proof strategy. Let (Yn)n∈N be an FO-convergent sequence of ﬁnite rooted colored trees (Yn ∈ Y(h)) such that limn→∞ |Yn| = ∞.

For each n, IY →F(Yn) is a forest Fn, and (Yn)n∈N is an FO-convergent sequence. According to the Comb Structure Theorem, there exists a countable set (Yn,i)n∈N of FO-convergent sequences of colored rooted trees Yn,i ∈ Y(h) and a FO-convergent sequence (Rn)n∈N of residues Rn ∈ F(h), which are special colored rooted forests (as the isolated principal root obviously belongs to Rn), so that

- • the sequences (Yn,i)n∈N and the sequence (Rn)n∈N form a uniformly convergent family of sequences;
- • for each n ∈ N it holds that IY →F(Yn) = Rn ∪ i∈I Yn,i.


If the limit spectrum of (IY →F(Yn))n∈N is empty (i.e. I = ∅), the sequence (Yn)n∈N of colored rooted trees is called residual, and in this case we deduce directly that a residual sequence of colored rooted trees admit a modeling FO-limit from our results on FO1-convergent sequences.

Otherwise, we proceed by induction over the height bound h. Denote by (spi)i∈I the limit spectrum of (IY →F(Yn))n∈N, let sp0 = 1 − i∈I spi, and let Yn,0 = IR→P ◦ IF→Y (Rn). As (IF→Y (Rn))n∈N is residual, (Yn,0)n∈N has a modeling FO-limit Y0. By induction, each (Yn,i)n∈N has a modeling FO-limit Yi. As Yn = IF→Y ( i∈I∪{0} Yn,i), we deduce (using uniform elementary convergence) that (Yn)n∈N has modeling FO-limit IF→Y ( i∈I∪{0}( Yi, spi)).

This ﬁnishes the outline of our construction. Now we provide details. 4.2.1. The Modeling FO-limit of Residual Sequences. We start by a

formal deﬁnition of residual sequences of colored rooted trees.

- Definition 4.25. Let (Yn)n∈N be a sequence of ﬁnite colored rooted trees, let

Nn be the set of all sons of the root of Yn, and let Yn(v) denote (for v ∈ Yn) the subtree of Yn rooted at v.

The sequence (Yn)n∈N is residual if limsup

n→∞

max

v∈Nn

|Yn(v)| |Yn|

= 0.

We extend this deﬁnition to single inﬁnite modelings.

- Definition 4.26. A modeling colored rooted tree Y with height at most h is


residual if, denoting by N the neighbor set of the root, it holds that sup

ν Y( Y(v)) = 0.

v∈N

Note that the above deﬁnition makes sense as belonging to some Y(v) (for some v ∈ N) is ﬁrst-order deﬁnable hence, as Y is a relational sample space, each Y(v) is Σ Y-measurable.

We ﬁrst prove that for a modeling colored rooted tree to be a modeling FOlimit of a residual sequence (Yn)n∈N of rooted colored trees with bounded height, it is suﬃcient that it is a modeling FO1-limit of the sequence.

Lemma 4.27. Assume (Yn)n∈N is a residual FO1-convergent sequence of ﬁnite rooted colored trees with bounded height with residual modeling FO1-limit Y.

Then (Yn)n∈N is FO-convergent and has modeling FO-limit Y.

Proof. Let h be a bound on the height of the rooted trees Yn. Let Fn = IY →F(Yn). Let be the formula asserting dist(x1,x2) ≤ 2h. Then Fn |= (u,v) holds if and only if u and v belong to a same connected component of Fn. According to Lemma 3.54, we get that (Fn)n∈N is FOlocal-convergent. As it is also FO0convergent, it is FO-convergent (according to Theorem 2.23). As Yn = IF→Y (Fn), we deduce that (Yn)n∈N is FO-convergent.

That Y is a modeling FO-limit of (Yn)n∈N then follows from Theorem 3.22. Lemma 4.28. Let Yn be a residual FO1-convergent sequence of colored rooted

on T(1h), and let Y be the connected component of Yh containing the support of ν. Then Y, equipped with the probability measure ν Y = ν, is a modeling FO-limit of (Yn)n∈N.

trees with height at most h, let µ be the limit measure of µY

n

Proof. That Y is a residual FO1-modeling limit of (Yn)n∈N is a consequence of Theorem 4.18. That it is then an FO-modeling limit of (Yn)n∈N follows from Lemma 4.27

4.2.2. The Modeling FO-Limit of a Sequence of Rooted Trees. For an intuition of how the structure of a modeling FO-limit of a sequence of colored rooted trees with height at most h could look like, consider a modeling rooted colored tree Y. Obviously, the Y contains two kind of vertices: the heavy vertices v such that the subtree Y(v) of Y rooted at v has positive νY-measure and the light vertices for which Y(v) has zero νY-measure. It is then immediate that heavy vertices of Y induce a countable rooted subtree with same root as Y.

This suggest the following deﬁnitions.

- Definition 4.29. A rooted skeleton is a countable rooted tree S together with

a mass function m : S → (0,1] such that m(r) = 1 (r is the root of S) and for every non-leaf vertex v ∈ S it holds that

m(v) ≥

u son of v

m(u).

- Definition 4.30. Let (S,m) be a rooted skeleton, let S0 be the subset of S


with vertices v such that m(v) = u son of v m(u), let (Rv)v∈S\S

###### be a countable sequence of non-empty residual λ-modeling indexed by S \ S0, and let (Rv)v∈S

0

0

###### be a countable sequence of non empty countable colored rooted trees indexed by S0. The grafting of (Rv)v∈S\S

###### and (Rv)v∈S

on (S,m) is the modeling Y deﬁned

0

0

- as follows: As a graph, Y is obtained by taking the disjoint union of S with the colored rooted trees Rv and then identifying v ∈ S with the root of Rv (see Fig. 6). The sigma algebra ΣY is deﬁned as


M v : Mv ∈ ΣR

,M v ⊆ Rv

Mv ∪

###### ΣY =

v

v∈S0

v∈S\S0

and the measure νY(M) of M ∈ Σ is deﬁned by νY(M) =

m(v) −

m(u) νR

(Mv),

v

u son of v

v∈S\S0

Mv ∪ v∈S M v with Mv ∈ ΣR

and M v ⊆ Rv.

where M = v∈S\S

v

0

Rv

v

S Y

Figure 6. Grafting of trees on a skeleton

Lemma 4.31. Let Y be obtained by grafting a countable sequence of non-empty modeling colored rooted trees Rv on a rooted skeleton (S,m). Then Y is a modeling.

Proof. We prove the statement by induction over the height of the rooted skeleton. The statement obviously holds if S is a single vertex rooted tree (that is if height(S) = 1). Assume that the statement holds for rooted skeletons with height

- at most h, and let (S,m) be a rooted skeleton with height h + 1. Let s0 be the root of S and let {si : i ∈ I ⊆ N} be the set of the sons of s0 in


S. For i ∈ I, Yi = Y(si) be the subtree of Y rooted at si, let spi = x∈Y

m(x), and let mi be the mass function on Si deﬁned by mi(v) = m(v)/spi. Also, let sp0 = 1 − i∈I spi.

i

For each i ∈ I ∪ {0}, if spi = 0 (in which case Rs

is only assumed to be a relational sample space) we turn Rs

i

into a modeling by deﬁning a probability measure on Rs

i

concentrated on si.

i

For i ∈ I, let Yi be obtained by grafting the Rv on (Si,mi) (for v ∈ Si), and let Y0 be the λ+-modeling consisting in a rooted colored forest with single (principal) component Rs

(that is: Y0 = IR→P(Rs

)). According to Lemma 3.13, Y0 is a modeling, and by induction hypothesis each Yi (i ∈ I) is a modeling. According to Lemma 3.26, it follows that F = i∈I∪{0}(Yi, spi) is a modeling. Hence, according to Lemma 3.13, Y = IF→Y (F) is a modeling.

0

0

Our main theorem is the following.

Theorem 4.32. Let (Yn)n∈N be an FO-convergent sequence of ﬁnite colored rooted trees with height at most h.

Then there exists a skeleton (S,m) and a family (Rv)v∈S — where Rv is (isomorphic to) a connected component of Yh, ΣR

is the induced σ-algebra on Rv with the property that the grafting Y of the Rv on (S,m) is a modeling FO-limit of the sequence (Yn)n∈N.

v

Proof. First notice that the statement obviously holds if limn→∞ |Yn| < ∞

- as then the sequence is eventually constant to a ﬁnite colored rooted tree Y: we can let S be Y (without the colors), m be the uniform weight (m(v) = 1/|Y |), and Rv be single vertex rooted tree whose root’s color is the color of v in Y. So, we can assume that limn→∞ |Yn| = ∞.


We prove the statement by induction over the height bound h. For h = 1, each Yn is a single vertex colored rooted tree, and the statement obviously holds.

Assume that the statements holds for h = h0 − 1 ≥ 1 and let ﬁnite colored rooted trees with height at most h0. Let Fn = IY →F(Yn). Then (Fn)n∈N is FOconvergent (according to Lemma 3.13). According to the Comb Structure Theorem, there exists countably many convergent sequences (Yn,i)n∈N of colored rooted trees (for i ∈ I) and an FO-convergent sequence (Rn)n∈N of special rooted forests forming a uniformly convergent family of sequences, such that IY →F(Yn) = Rn∪ i∈I Yn,i.

If the limit spectrum of (IY →F(Yn))n∈N is empty (i.e. I = ∅), the sequence (Yn)n∈N of colored rooted trees is residual, and the result follows from Lemma 4.28. Otherwise, let (spi)i∈I the limit spectrum of (IY →F(Yn))n∈N, let sp0 = 1 −

i∈I spi, and let Yn,0 = IR→P ◦ IF→Y (Rn). If sp = 0 then there is a connected component Y0 of Yh that is an elementary limit of (Yn,0)n∈N; otherwise, as (IF→Y (Rn))n∈N is residual, (Yn,0)n∈N has, according to Lemma 4.28, a modeling FO-limit Y0. By induction, each (Yn,i)n∈N has a modeling FO-limit Yi. As Yn = IF→Y ( i∈I∪{0} Yn,i), we deduce, by Corollary 3.31, Lemma 3.33, Theorem 2.23, and Lemma 3.13, that (Yn)n∈N has modeling FO-limit IF→Y ( i∈I∪{0}( Yi, spi)).

So, in the case of colored rooted trees with bounded height, we have constructed an explicit relational sample space that allows one to pullback the limit measure µ deﬁned on the Stone space S(B(FO)).

4.2.3. Inverse theorem for FO-limits of Colored Rooted Trees with Bounded Height. Recall that for λ-modelings A and B, and p,r ∈ N we deﬁned

A − B localp,r = sup{| φ,A − φ,B | : φ ∈ FOlocalp (λ),qrank(φ) ≤ r}.

Lemma 4.33. Let L ∈ Y(h) (with root rL) be a colored rooted tree modeling that satisﬁes the FMTP, let p,r ∈ N, and let > 0. Then there exist C0 = C0(λ,p,r, ),N0 = N0(λ,p,r, ) such that for every N ≥ N0 there exists a ﬁnite colored rooted tree Y ∈ Y(h) such that it holds that N ≤ |Y | ≤ N + C0, Y ≡r L, and

Y − L localp,r < max( ,2 sup v∼rL

νL(L(v))).

Proof. Without loss of generality we can assume ≥ 2supv∼r

νL(L(v)). Let r = max(r,4cr,p/ ), where cr,p is the constant introduced in Lemma 3.28..

L

According to Lemma 4.22, there is C0 = C(λ,r ) (hence C0 depends on λ,p,r, and ) such that for every N ∈ N there exists Y ∈ Y(h) with the following properties:

- (1) N ≤ |Y | ≤ N + C0;
- (2) for every ϕ ∈ FO1 with quantiﬁer rank at most r the following inequality holds

ϕ,Y − ϕ,L ≤ C0/N. (In particular Y ≡r L as N > C0.)

- (3) we have


|Y (v)| |Y |

1 r + h

≤ max

νL(L(v)) + C0/N. Let N0 = 4cr,pC(λ,r )/  and assume N ≥ N0.

max

, sup

v∼rN

v∼rL

Let F = IY →F(Y ) and A = IY →F(L). Let Fi,i ∈ ΓF and Ai,i ∈ ΓA be the connected components of F and A. Then

|Fi| |F|

1 r + h

≤ max

max

, sup

νA(Ai) + C0/N <

.

2cr,p

i∈ΓF

i∈ΓL

As IY →F is a quantiﬁer free interpretation, for every ϕ ∈ FO1 with quantiﬁer rank

- at most r the following inequality holds

ϕ,F − ϕ,A ≤ C0/N ≤ 4cr,p

.

In particular we have F −A local1,r ≤ 4c

r,p

. According to Lemma 3.29, it holds that

F − A localp,r < cr,p max i∈ΓF

|Fi| |F|

+ sup

i∈ΓL

νA(Ai) + F − A local1,r <  .

and it follows that Y − L localp,r < .

Lemma 4.34. Let L ∈ Y(h) be an inﬁnite colored rooted tree modeling that satisﬁes the FMTP, let p,r ∈ N and let > 0. Then there exist constants Ch,Nh (depending on λ,p,r, ) such that for every N ≥ Nh there is a ﬁnite colored rooted tree Y ∈ Y(h) such that N ≤ |Y | ≤ N + Ch, Y ≡r L, and L − Y localp,r < .

Proof. Let α = 2/(2(3cr,p)h), where cr,p is the constant which appears in Lemma 3.28. A vertex v ∈ L is α-heavy if either v is the root rL of L, or the father

- u of v in L is α-heavy and νL(L(v)) > ανL(L(u)). The α-heavy vertices of L form a ﬁnite subtree S rooted at rL (each node v of S has at most 1/α sons).


We prove by induction on the height t of S that — assuming α ≤  /2 — there exist constants Ct−1,Nt−1 (depending on λ,p,r, ) such that for every N ≥ Nt−1 there is a ﬁnite colored rooted tree Y ∈ Y(h) such that N ≤ |Y | ≤ N + Ct−1, Y ≡r L, and L − Y localp,r < .

If t = 1 (i.e. rL is the only α-heavy vertex) then sup

νL(L(v)) < α.

v∼rL

Hence, according to Lemma 4.33, there exists N0,C0 (depending on λ,r,p, and ) such that for every N ≥ N0 there is a ﬁnite colored rooted tree Y ∈ Y(h) such that N ≤ |Y | ≤ N + C0, Y ≡r L, and

Y − L localp,r < max( ,2 sup v∼rL

νL(L(v))) =  .

Now assume that the statement we want to prove by induction holds when S has height at most t ≥ 1, and let L be such that the associated subtree S of

α-heavy vertices has height t + 1. Let v1,...,vk (where k is at most 1/α) be the α-heavy sons of the root rL of L, let Li be the relational sample space deﬁned by Li = L(vi) for 1 ≤ i ≤ k, and let L0 be the colored rooted tree relational sample space obtained by removing all the subtrees Li from L. Each Li is measurable in L. Let ai = νL(Li), and let

=

3cr,p Ct(λ,p,r, ) = max

Ct−1(λ,p,r,  ) α

,C0(λ,p,r,  /3cr,p)

Ct−1(λ,p,r,  ) α 

Nt−1(λ,p,r,  )

,N0(λ,p,r,  /3cr,p) . (Note that we do not change α.)

,

Nt(λ,p,r, ) = max

Assume a0 ≥ . Let Lˆi be the modeling with relational sample space Li and probability measure νLˆ

which is a−i 1νL|Li, where νL|Li stands for the restriction of νL to Li. Let Si be the rooted subtree of α-heavy vertices of Lˆi. Clearly, if 1 ≤ i ≤ k, then Si = S(vi) (as we did not change α) thus Si has height at most t. Let F ∈ F(h) be the forest deﬁned from F = ki=0(Lˆi,ai) by making the component Lˆ0 special. It is clear that L = IF→Y (F). For every N ≥ Nt(λ,p,r, ) ≥ Nt−1(λ,p,r,  )/  there exist, by induction, Y1,...,Yk such that aiN ≤ Yi ≤ aiN + Ct−1(λ,p,r,  ), Yi ≡r Lˆi, and Yi − Lˆi localp,r < . As the induction step is carried on at most h times, it will always hold that α ≤ 2/2 hence

i

1

α

(Lˆ0(v))) ≤

νL(L0(v))) ≤

≤ /2.

sup

νLˆ

sup

0

v∼rLˆ0

v∼rL0

Also, according to Lemma 4.33, for every N ≥ Nt−1(λ,p,r,  ) ≥ N0(λ,p,r,  ) there is a ﬁnite colored rooted tree Y0 ∈ Y(h) such that N ≤ |Y0| ≤ N + C0(λ,p,r,  ) ≤ N + Ct−1(λ,p,r,  ), Y ≡r Lˆ0, and

(Lˆ0(v))) = . Then

Y0 − Lˆ0 localp,r < max( ,2 sup

νLˆ

0

v∼rLˆ0

|Yi|

ai N + Ct−1(λ,p,r,  )/α ≤

ai + Ct−1(λ,p,r,  ) N

≤

.

k i=0 |Yi|

Thus

|Yi|

Ct−1(λ,p,r,  ) αN ≤ .

ai −

<

k i=0 |Yi|

Let G be the disjoint union of the Yi. Hence the following inequality holds, according to Lemma 3.28

F − G localp,r ≤ 2cr,p <  .

Moreover, N ≤ |G| ≤ N + Ct−1(λ,p,r,  )/α ≤ N + Ct(λ,p,r, ).

If a0 < we consider Y1,...,Yk as above, but Y0 is chosen with the only conditions that |Y0| ≤ C0(λ,p,r,  ) ≤ Ct−1(λ,p,r,  ) and Y0 ≡r L0. (Actually, Y0 can be chosen so that |Y0| is bounded by a function of λ,p, and r only.) Let G be the disjoint union of the Yi. Let Lˆ0 be the modeling with relational sample space L0 and probability measure νLˆ

= a−0 1νL|L0 if a0 > 0, and any probability measure if a0 = 0 (for instance the discrete probability measure concentrated on rLˆ

0

). Let

0

- F ∈ F(h) be the forest deﬁned from F = ki=0(Lˆi,ai) by making the component Lˆ0 special. It is clear that L = IF→Y (F). Then, according to Lemma 3.28

F − G localp,r ≤ cr,p +

k

i=1

ai L ˆi − Yi localp,r + a0

< cr,p 2 + sup

1≤i≤k

L ˆi − Yi localp,r ≤ 3cr,p =  .

and, as above, N ≤ |G| ≤ N + Ct(λ,p,r, ). Now, let Y = IF→Y (G). As IF→Y is basic and quantiﬁer free, and as IF→(Y) = L it holds that L − Y localp,r < and N ≤ |Y | ≤ N + Ct(λ,p,r, ).

Theorem 4.35. A modeling L is the FO-limit of an FO-convergent sequence (Yn)n∈N of ﬁnite colored rooted trees with height at most h if and only if

- • L is a colored rooted tree with height at most h,
- • L satisﬁes the FMTP.


4.3. Limits of Graphs with Bounded Tree-depth

Let Y be a rooted forest. The vertex x is an ancestor of y in Y if x belongs to the path linking y and the root of the tree of Y to which y belongs to. The closure Clos(Y) of a rooted forest Y is the graph with vertex set V (Y ) and edge set {{x,y} : x is an ancestor of y in Y,x = y}. The height of a rooted forest is the maximum number of vertices in a path having a root as an extremity. The tree-depth td(G) of a graph G is the minimum height of a rooted forest Y such that G ⊆ Clos(Y). This notion is deﬁned in [68] and studied in detail in [80]. In particular, graphs with bounded tree-depth serve as building blocks for low treedepth decompositions, see [69, 70, 71]. It is easily checked that for each integer t the property td(G) ≤ t is ﬁrst-order deﬁnable. It follows that for each integer t there exists a ﬁrst-order formula ξ with a single free variable such that for every graph

- G and every vertex v ∈ G the following equivalence holds: G |= ξ(v) ⇐⇒ td(G) ≤ t and td(G − v) < td(G).


Let t ∈ N. We deﬁne the basic interpretation scheme It, which interprets the class of connected graphs with tree-depth at most t in the class of 2t−1-colored rooted trees: given a 2t−1-colored rooted tree Y (where colors are coded by t − 1 unary relations C1,...,Ct−1), the vertices u,v ∈ Y are adjacent in It(Y) if the there is an integer i in 1,...,t − 1 such that Y |= Ci(v) and u is the ancestor of v at height i or Y |= Ci(u) and v is the ancestor of u at height i.

Continuing this with all above results we arrive to the closing statement of this paper.

Theorem 4.36. Let (Gn)n∈N be an FO-convergent sequence of ﬁnite colored graphs with tree-depth at most h. Then there exists a colored rooted tree modeling L ∈ Y(h) satisfying the FMTP, such that the modeling G = Ih(L) has tree-depth at most h and is a modeling FO-limit of the sequence (Gn)n∈N.

4.3. LIMITS OF GRAPHS WITH BOUNDED TREE-DEPTH 103

Conversely, if there is colored rooted tree modeling L ∈ Y(h) satisfying the FMTP and if G = Ih(L), then there is an FO-convergent sequence (Gn)n∈N of ﬁnite colored graphs with tree-depth at most h, such that G is a modeling FO-limit of (Gn)n∈N.

Proof. For each Gn, there is a colored rooted tree Yn ∈ Y(h) such that Gn = Ih(Yn). By compactness, the sequence (Yn)n∈N has a converging subsequence (Yi

)n∈N, which admits a modeling FO-limit Y (according to Theorem 4.35), and it follows from Lemma 3.13 that Ih(Y) is a modeling FO-limit (with tree-depth at most h) of the sequence (Gi

n

)n∈N, hence a modeling FO-limit of the sequence (Gn)n∈N.

n

Conversely, if there is colored rooted tree modeling L ∈ Y(h) satisfying the FMTP and if G = Ih(L) then, according to Theorem 4.35 there is an FO-convergent sequence (Yn)n∈N of ﬁnite colored rooted trees with FO-limit L. It follows from Lemma 3.13 that Ih(Y) is a modeling FO-limit of the sequence (Gn)n∈N, where Gn = Ih(Yn) is a ﬁnite graph with tree-depth at most h.

CHAPTER 5

## Concluding Remarks

###### 5.1. Selected Problems

We hope that the theory developed here will encourage further researches. Here we list and summarize a sample of related problems (some of which we discussed in Section 1).

5.1.1. Modeling Limits for Nowhere Dense Classes. The ﬁrst problem concern existence of modeling FO-limits. Recall that a class C is nowhere dense [74, 75, 76, 78] if, for every integer d there is an integer N such that the d-subdivision of KN is not a subgraph of a graph in C. We have proven, see Theorem 3.39, that if a monotone class C is such that every FO-convergent sequence of graphs in C has a modeling FO-limit, then C is nowhere dense. It is thus natural to ask whether the converse statement holds.

Problem 5.1. Let C be a nowhere dense class of graphs. Is it true that every FO-convergent sequence (Gn)n∈N of ﬁnite graphs in C admit a modeling FO-limit?

5.1.2. Inverse Problems. The Aldous–Lyons conjecture [5] states that every unimodular distribution on rooted countable graphs with bounded degree is the limit of a bounded degree graph sequence. One of the reformulations of this conjecture is that every graphing is an FOlocal limit of a sequence of ﬁnite graphs. The importance of this conjecture appears, for instance, in the fact that it would imply that all groups are soﬁc, which would prove a number of famous conjectures which are proved for soﬁc groups but still open for all groups.

If Aldous–Lyons conjecture holds, then it follows that every graphing is localequivalent to a graphing with the ﬁnite model property. Indeed, if (Gn)n∈N is BSconvergent to a graphing G, then (by compactness) some subsequence of (Gn)n∈N is FO-convergent and (by Corollary 2.38) has a graphing FO-limit G , which is local-equivalent to G. Hence the following problem can be seen as a natural ﬁrst step towards the resolution of Aldous–Lyon conjecture:

Problem 5.2. Is every graphing local-equivalent to a graphing with the ﬁnite model property?

If the previous problem would have a positive answer then the next problem would be a possible strengthening of Aldous–Lyons conjecture.

Problem 5.3. Is every graphing G with the ﬁnite model property an FO-limit of a sequence of ﬁnite graphs?

Although the existence of a modeling FO-limit for FO-convergent sequences of graphs with bounded tree-depth follows easily from our study of FO-convergent sequence of rooted colored trees, the inverse theorem is more diﬃcult. Indeed, if

105

we would like to extend the inverse theorem for rooted colored trees to bounded tree-depth modelings (thus removing the condition G = Ih(L) in Theorem 4.36), we naturally have to address the following question:

Problem 5.4. Is it true that there is a function f : N → N such that for every graph modeling L with tree-depth at most t there exists a rooted colored tree modeling Y with height at most f(t) such that L = If(t)(Y), where the Ih (for h ∈ N) are the basic interpretation schemes introduced in Section 4.3?

5.1.3. Classes with Bounded SC-depth. We can generalize our main construction of limits to other tree-like classes. For example, in a similar way that we obtained a modeling FO-limit for FO-convergent sequences of graphs with bounded tree-depth, it is possible to get a modeling FO-limit for FO-convergent sequences of graphs with bounded SC-depth, where SC-depth is deﬁned as follows [41]:

Let G be a graph and let X ⊆ V (G). We denote by GX the graph G with vertex set V (G) where x = y are adjacent in G if (i) either {x,y} ∈ E(G) and {x,y}  ⊆ X, or (ii) {x,y}  ∈ E(G) and {x,y} ⊆ X. In other words, GX is the graph obtained from G by complementing the edges on X.

Definition 5.1 (SC-depth). We deﬁne inductively the class SC(n) as follows:

- • We let SC(0) = {K1};
- • if G1,...,Gp ∈ SC(n) and H = G1∪˙ ...∪˙ Gp denotes the disjoint union of


the Gi, then for every subset X of vertices of H we have H X ∈ SC(n+1). The SC-depth of G is the minimum integer n such that G ∈ SC(n).

Note that classes with bounded SC-depth can be seen as the ﬁrst step towards moving from the study of monotone classes to the study of hereditary classes (that is classes closed under induced subgraphs). For instance, classes of graphs with bounded tree-depth are exactly those monotone classes of graphs where ﬁrst-order logic and monadic second-order logic have the same expressive power, while classes with bounded SC-depth are exactly those hereditary classes where ﬁrst-order logic and monadic second-order logic have the same expressive power [30].

5.1.4. Classes with Bounded Expansion. A graph H is a shallow topological minor of a graph G at depth t if some ≤ 2t-subdivision of H is a subgraph of G. For a class C of graphs we denote by C t the class of all shallow topological minors at depth t of graphs in C. The class C has bounded expansion if, for each t ≥ 0, the average degrees of the graphs in the class C t is bounded, that is (denoting by d(G) the average degree of a graph G):

(∀t ≥ 0) sup

d(G) < ∞.

G∈C t

The notion of classes with bounded expansion were introduced by the authors in [66, 67, 69], and their properties further studied in [70, 71, 27, 28, 72, 73, 75, 76, 80, 87] and in the monograph [77]. Particularly, classes with bounded expansion include classes excluding a topological minor, like classes with bounded maximum degree, planar graphs, proper minor closed classes, etc.

Classes with bounded expansion have the characteristic property that they admit special decompositions — the so-called low tree-depth decompositions — related to tree-depth:

5.2. ADDENDUM 107

Theorem 5.2 ([67, 69]). Let C be a class of graphs. Then C has bounded expansion if and only if for every integer p ∈ N there exists N(p) ∈ N such that the vertex set of every graph G ∈ C can be partitioned into at most N(p) parts in such a way that the subgraph of G induced by any i ≤ p parts has tree-depth at most i.

By an inductive argument, following [43], we can prove that for every integer p,r and every class C of λ-structure with bounded expansion, there is a signature λ+ ⊇ λ, such that every λ-structure A ∈ C can be lifted into a λ+-structure A+ with same Gaifman graph, in such a way that for every ﬁrst-order formula φ ∈ FOp(λ) with quantiﬁer rank at most r there is an existential formula φ ∈ FOp(λ+) such that for every v1,...,vp ∈ A the following equivalence holds:

A |= φ(v1,...,vp) ⇐⇒ A+ |= φ(v1,...,vp). Moreover, by considering a slightly stronger notion of lift if necessary, we can assume that φ is a local formula. We deduce that there is an integer q = q(C,p,r) such that checking φ(v1,...,vp) can be done by considering satisfaction of ψ(v1,...,vp) in subgraphs induced by q color classes of a bounded coloration. Using a low-tree depth decomposition (and putting the corresponding colors in the signature λ+), we get that there exists ﬁnitely many induced substructures A+I (I ∈ [Nq ] ) with tree-depth at most q and the property that for every ﬁrst-order formula φ ∈ FOp(λ) with quantiﬁer rank at most r there is an existential formula φ ∈ FOp(λ+) such that for every v1,...,vp ∈ A with set of colors I0 ⊆ I the following equivalence holds:

[N] q − p

: A+I∪I

A |= φ(v1,...,vp) ⇐⇒ ∃I ∈

|= φ(v1,...,vp).

0

Moreover, the Stone pairing φ,A can be computed by inclusion/exclusion from Stone pairings φ,A+I for I ∈ [≤Nq] .

Thus, if we consider an FO-convergent sequence (An)n∈N, the tuple of limits of the λ+-structures (An)+I behaves as a kind of approximation of the limit of the λ-structures An.

###### 5.2. Addendum

5.2.1. Modeling Limits for Nowhere Dense Classes. Since the submission of this paper a great progress has been made on Problem 5.1. Based on the results of this paper, classes of graphs for which there exist explicit modeling FOlimits (satisfying the Finitary Mass Transport Principle) now include the class of forests [83] and, more generally, classes of graphs with bounded pathwidth [40].

For the general case, it has ﬁrst been proved [84] that for every FO-convergent sequence of graphs (Gn)n∈N there exists a modeling L such that for every ﬁrst-order formula φ the following equation holds

φ,L = 0 ⇐⇒ lim

φ,Gn = 0.

n→∞

This result has been extended to prove that every FO-convergent sequence of nowhere dense graphs has a modeling limit [81]. (Note that this result heavily relies on this paper.) But it is still open whether this modeling limit could be required to satisfy the Finitary Mass Transport Principle.

- 5.2.2. Asymptotic Connectivity. Some further applications include the study

of the connectivity structure of FOlocal-convergent sequences we started in Section 3.3 has been further reﬁned in [83] to study modeling limits of forests (with unbounded height). In [85] we deal with the important notion of clustering of a convergent sequence, and show that connectivity properties — although not ﬁrstorder deﬁnable — can be established in FOlocal-convergent sequences by means of Fourier analysis.

- 5.2.3. Inverse Problems. The study of existence of modeling limits for sim-

ple algebraic structures has led us to prove that FO-convergent sequences of mappings admit a modeling limit [86], and we have been able to prove inverse theorems in this case [49]: every atomless modeling mapping that satisﬁes the Finitary Mass Transport Principle is the FOlocal-limit of an FOlocal-convergent sequence of ﬁnite mappings, and if moreover its complete theory has the Finite Model Property then if it is the FO-limit of an FO-convergent sequence of ﬁnite mappings.

- 5.2.4. Rooting of Modelings. Problems 3.1 and 3.2 have been solved nega-

tively in [22], where it is nevertheless proved that Problem 3.1 holds for almost all rootings of the modeling limit.

- 5.2.5. Others. The analytic framework of X-convergence has also been pre-


sented in [82]. One of the main reasons for interest in our notion of convergence is that it allows to consider structures with arbitrary (countable) signature, and interpretations of these. For instance, it led to the study of limits of mappings [86] (mentioned above), limits of matroids [54], and quantiﬁer-free convergence of tree-semilattices [20].

###### Acknowledgements

The authors would like to thank Pierre Charbit for suggesting to use a proof by induction for Lemma 4.4 and Cameron Freer for his help in proving that the FO-limit of a sequence of random graphs cannot be a modeling.

The authors would like to express their gratitude to the anonymous referee for his careful reading of this manuscript.

## Bibliography

- [1] S. Adams, Trees and amenable equivalence relations, Ergodic Theory and Dynamical Systems 10 (1990), 1–14.
- [2] H. Adler and I. Adler, Interpreting nowhere dense graph classes as a classical notion of model theory, European Journal of Combinatorics 36 (2014), 322– 330.
- [3] D. Aldous, Representations for partially exchangeable arrays of random variables, Journal of Multivariate Analysis 11 (1981), 581–598.
- [4] , Exchangeability and related topics, Ecole´ d’´et´e de probabilit´es de SaintFlour, XIII — 1983, Lecture Notes in Mathematics, vol. 1117, Springer, 1985, pp. 1–198.

- [5] D. Aldous and R. Lyons, Processes on unimodular random networks, Electronic Journal of Probability 12 (2007), 1454–1508.
- [6] A. Aroskar, Limits, regularity and removal for relational and weighted structures, Ph.D. thesis, 2012.
- [7] A. Aroskar and J. Cummings, Limits, regularity and removal for ﬁnite structures, arXiv:1412.8084, 2014, to appear in The Journal of Symbolic Logic.
- [8] T. Austin, On exchangeable random variables and the statistics of large graphs and hypergraphs, Probability Surveys 5 (2008), 80–145.
- [9] I. Benjamini, H. Finucane, and R. Tessera, On the scaling limit of ﬁnite vertex transitive graphs with large diameter, Combinatorica (2016), 1–42.
- [10] I. Benjamini and O. Schramm, Recurrence of distributional limits of ﬁnite planar graphs, Electronic Journal of Probability 6 (2001), no. 23, 13pp.
- [11] A. Blass, G. Exoo, and F. Harary, Paley graphs satisfy all ﬁrst-order adjacency axioms, Journal of Graph Theory 5 (1981), 435–439.
- [12] B. Bollob´s and A. Thomason, Graphs which contain all small graphs, European Journal of Combinatorics 2 (1981), 13–15.
- [13] C. Borgs, J.T. Chayes, and L Lov´sz, Moments of two-variable functions and the uniqueness of graph limits, Geometric And Functional Analysis 19 (2012), no. 6, 1597–1619.
- [14] C. Borgs, J.T. Chayes, L. Lov´sz, V.T. S´s, B. Szegedy, and K. Vesztergombi, Graph limits and parameter testing, STOC’06. Proceedings of the 38th Annual ACM Symposium on Theory of Computing, 2006, pp. 261–270.
- [15] C. Borgs, J.T. Chayes, L. Lov´sz, V.T. S´s, and K. Vesztergombi, Counting graph homomorphisms, Topics in Discrete Mathematics (M. Klazar, J. Kratochvı´l, M. Loebl, J. Matouˇsek, R. Thomas, and P. Valtr, eds.), Algorithms and Combinatorics, vol. 26, Springer Verlag, 2006, pp. 315–371.
- [16] , Convergent sequences of dense graphs I: Subgraph frequencies, metric properties and testing, Advances in Mathematics 219 (2008), no. 6, 1801–1851.


109

- [17] , Convergent sequences of dense graphs II: Multiway cuts and statistical physics, Annals of Mathematics 176 (2012), 151–219.

- [18] P.J. Cameron and J. Nesˇetrˇil, Homomorphism-homogeneous relational structures, Combinatorics, Probability and Computing 15 (2006), 91–103.
- [19] A.K. Chandra and P.M. Merlin, Optimal implementation of conjunctive queries in relational databases, Proceedings of the 9th annual ACM symposium on Theory of Computing, 1977, pp. 77–90.
- [20] P. Charbit, L. Hosseini, and P. Ossona de Mendez, Limits of structures and the example of tree-semilattices, arXiv:1505.03037 [math.CO], 2015.
- [21] G. Cherlin, Two problems on homogeneous structures, revisited, Model Theoretic Methods in Finite Combinatorics (M. Grohe and J.A. Makowsky, eds.), vol. 558, American Mathematical Society, 2011, pp. 319–415.
- [22] D. Christoﬁdes and D. Kr´l’, First-order convergence and roots, Combinatorics, Probability and Computing 25 (2016), no. 2, 213–221.
- [23] F. R. K. Chung, R. L. Graham, and R. M. Wilson, Quasi-random graphs, Combinatorica 9 (1989), no. 4, 345–362.
- [24] P. Diaconis, S. Holmes, and S. Janson, Threshold graph limits and random threshold graphs, Internet Mathematics 5 (2009), no. 3, 267–318.
- [25] P. Diaconis and S. Janson, Graph limits and exchangeable random graphs., Rendiconti di Matematica e delle sue Applicazioni. Serie VII 28 (2008), no. 1, 33–61 (English).
- [26] R. Diestel, Graph theory, Springer Verlag, 1997.
- [27] Z. Dvorˇ´k, Asymptotical structure of combinatorial objects, Ph.D. thesis, Charles University, Faculty of Mathematics and Physics, 2007.
- [28] , On forbidden subdivision characterizations of graph classes, European Journal of Combinatorics 29 (2008), no. 5, 1321–1332.

- [29] A. Ehrenfeucht, An application of games to the completeness problem for formalized theories, Fundamenta Mathematicae 49 (1961), 129–141.
- [30] M. Elberfeld, M. Grohe, and T. Tantau, Where ﬁrst-order and monadic secondorder logic coincide, 27th Annual IEEE Symposium on Logic in Computer Science, 2012, pp. 265–274.
- [31] G. Elek, Note on limits of ﬁnite graphs, Combinatorica 27 (2007), 503–507.
- [32] G. Elek and B. Szegedy, Limits of hypergraphs, removal and regularity lemmas. A non-standard approach, arXiv:0705.2179v1 [math.CO], 2007.
- [33] P. Erd˝s and A. R´enyi, The evolution of random graphs, Publications of the Mathematical Institute of the Hungarian Academy of Sciences 5 (1960), 17–61.
- [34] , Asymmetric graphs, Acta Mathematica Hungarica 14 (1963), 295– 315.

- [35] R. Fagin, Probabilities on ﬁnite models, The Journal of Symbolic Logic 41

(1976), 50–58.

- [36] R. Fraı¨ss´e, Sur une nouvelle classiﬁcation des syst`emes de relations, Comptes rendus hebdomadaires des s´eances de l’Acad´emie des Sciences 230 (1950), 1022–1024.
- [37] , Sur quelques classiﬁcations des syst`emes de relations, Ph.D. thesis, University of Paris, 1953, published in Publications Scientiﬁques de l’Universit´e d’Alger, series A 1 (1954), 35–182., pp. 1022–1024.

- [38] D. Gaboriau, Invariant percolation and harmonic Dirichlet functions, Geometric And Functional Analysis 15 (2005), 1004–1051.


- [39] H. Gaifman, On local and non-local properties, Proceedings of the Herbrand Symposium, Logic Colloquium ’81, 1982.
- [40] J. Gajarsk´y, P. Hlinˇeny´, T. Kaiser, D. Kr´l’, M. Kupec, J Obdrˇz´lek, S. Ordyniak, and V. Tu˚ma, First order limits of sparse graphs: plane trees and path-width, Random Structures and Algorithms (2016).
- [41] R. Ganian, P. Hlinˇeny´, J. Neˇsetrˇil, J. Obdrˇz´lek, P. Ossona de Mendez, and

R. Ramadurai, When trees grow low: Shrubs and fast MSO1, MFCS 2012, Lecture Notes in Computer Science, vol. 7464, Springer-Verlag, 2012, pp. 419– 430.

- [42] Y.V. Glebskii, D.I. Kogan, M.I. Liagonkii, and V.A. Talanov, Range and degree of realizability of formulas the restricted predicate calculus, Cybernetics 5

(1969), no. 2, 142–154, (Russian: Kibernetica 5:2, 17-27).

- [43] M. Grohe and S. Kreutzer, Methods for algorithmic meta theorems, Model Theoretic Methods in Finite Combinatorics, Contemporary mathematics, 2011, pp. 181–206.
- [44] W. Hanf, Model-theoretic methods in the study of elementary logic, The theory of models (J.W. Addison et al., ed.), North-Holland, 1965, pp. 132–145.
- [45] H. Hatami and S. Norine, The entropy of random-free graphons and properties, Combinatorics, Probability and Computing 22 (2013), no. 4, 517–526.
- [46] P. Hell and J. Nesˇetrˇil, Graphs and homomorphisms, Oxford Lecture Series in Mathematics and its Applications, vol. 28, Oxford University Press, 2004.
- [47] W. Hodges, Model theory, Cambridge University Press, 1993.
- [48] D. Hoover, Relations on probability spaces and arrays of random variables, Tech. report, Institute for Advanced Study, Princeton, NJ, 1979.
- [49] L. Hosseini, J. Neˇsetrˇil, and P. Ossona de Mendez, Approximation of mappings, 2017+, in preparation.
- [50] J. Hubiˇcka and J. Neˇsetrˇil, Universal structures with forbidden homomorphisms, Ontos Mathematical Logic (˚A. Hirvonen, J. Kontinen, R. Kossak, and A. Villaveces, eds.), vol. 5, de Gruyter, 2015, pp. 241–264.
- [51] S. Janson, Graphons, cut norm and distance, couplings and rearrangements, New York Journal of Mathematics Monographs, vol. 4, 2013.
- [52] , Graph limits and hereditary properties, European Journal of Combinatorics 52 (2016), 321–337.

- [53] O. Kallenberg, Probabilistic symmetries and invariance principles, Probability and Its Applications, Springer, 2005.
- [54] F. Kardoˇs, D. Kr´l’, A. Liebenau, and L. Mach, First order convergence of matroids, arXiv:1501.06518v1 [math.CO], 2015.
- [55] A.S. Kechris, S. Solecki, and S. Todorcevic, Borel chromatic numbers, Advances in Mathematics 141 (1999), 1–44.
- [56] A.H. Lachlan and R.E. Woodrow, Countable ultrahomogeneous undirected graphs, Transactions of the American Mathematical Society 262 (1980), 51–94.
- [57] D. Lascar, La th´eorie des mod`eles en peu de maux, Cassini, 2009.
- [58] M.C. Laskowski, Vapnik-Chervonenkis classes of deﬁnable sets, The Journal of the London Mathematical Society 45 (1992), no. 2, 377–384.
- [59] P. Loeb, Conversion from nonstandard to standard measure spaces and applications in probability theory, Transactions of the American Mathematical Society 211 (1975), 113–122.


- [60] J.  Lo´s, Quelques remarques, the´or`emes et probl`emes sur les classes de´ﬁnissables d’alg`ebres, Mathematical interpretation of formal systems, Studies in logic and the foundations of mathematics, North-Holland, 1955.
- [61] L Lov´sz, Very large graphs, Current Developments in Mathematics 2008

(2009), 67–128.

- [62] , Large networks and graph limits, Colloquium Publications, vol. 60, American Mathematical Society, 2012.

- [63] L. Lov´sz and B. Szegedy, Limits of dense graph sequences, Journal of Combinatorial Theory, Series B 96 (2006), 933–957.
- [64] , Regularity partitions and the topology of graphons, An irregular mind (Szemer´edi is 70) (I. B´r´ny and J. Solymosi, eds.), Bolyai Society Mathematical Studies, vol. 21, Springer, 2010, pp. 415–446.

- [65] R. Lyons, Asymptotic enumeration of spanning trees, Combinatorics, Probability and Computing 14 (2005), 491–522.
- [66] J. Neˇsetrˇil and P. Ossona de Mendez, The grad of a graph and classes with bounded expansion, 7th International Colloquium on Graph Theory (A. Raspaud and O. Delmas, eds.), Electronic Notes in Discrete Mathematics, vol. 22, Elsevier, 2005, pp. 101–106.
- [67] , Linear time low tree-width partitions and algorithmic consequences, STOC’06. Proceedings of the 38th Annual ACM Symposium on Theory of Computing, ACM Press, 2006, pp. 391–400.

- [68] , Tree depth, subgraph coloring and homomorphism bounds, European Journal of Combinatorics 27 (2006), no. 6, 1022–1041.

- [69] , Grad and classes with bounded expansion I. Decompositions, European Journal of Combinatorics 29 (2008), no. 3, 760–776.

- [70] , Grad and classes with bounded expansion II. Algorithmic aspects, European Journal of Combinatorics 29 (2008), no. 3, 777–791.

- [71] , Grad and classes with bounded expansion III. Restricted graph homomorphism dualities, European Journal of Combinatorics 29 (2008), no. 4, 1012–1024.

- [72] , Fraternal augmentations, arrangeability and linearly bounded Ramsey numbers, European Journal of Combinatorics 30 (2009), no. 7, 1696–1703.

- [73] , Extremal problems for sparse graphs, An irregular mind (Szemer´edi is

70) (I. B´r´ny and J. Solymosi, eds.), Bolyai Society Mathematical Studies, vol. 21, Springer, 2010, pp. 447–490.

- [74] , First order properties on nowhere dense structures, The Journal of Symbolic Logic 75 (2010), no. 3, 868–887.

- [75] , From sparse graphs to nowhere dense structures: Decompositions, independence, dualities and limits, European Congress of Mathematics, European Mathematical Society, 2010, pp. 135–165.

- [76] , Sparse combinatorial structures: Classiﬁcation and applications, Proceedings of the International Congress of Mathematicians 2010 (ICM 2010) (Hyderabad, India) (R. Bhatia and A. Pal, eds.), vol. IV, World Scientiﬁc, 2010, pp. 2502–2529.

- [77] , How many F’s are there in G?, European Journal of Combinatorics 32 (2011), no. 7, 1126–1141.

- [78] , On nowhere dense graphs, European Journal of Combinatorics 32


(2011), no. 4, 600–617.

- [79] , A model theory approach to structural limits, Commentationes Mathematicæ Universitatis Carolinæ 53 (2012), no. 4, 581–603.

- [80] , Sparsity (graphs, structures, and algorithms), Algorithms and Combinatorics, vol. 28, Springer, 2012, 465 pages.

- [81] , Existence of modeling limits for sequences of sparse structures, arXiv:1608.00146 [math.CO], 2016.

- [82] , First-order limits, an analytical perspective, European Journal of Combinatorics 52 Part B (2016), 368–388.

- [83] , Modeling limits in hereditary classes: Reduction and application to trees, Electronic Journal of Combinatorics 23 (2016), no. 2, #P2.52.

- [84] , Structural sparsity, Uspekhi Matematicheskikh Nauk 71 (2016), no. 1, 85–116, (Russian Math. Surveys 71:1 79-107).

- [85] , Cluster analysis of local convergent sequences of structures, Random Structures & Algorithms (2017), accepted.

- [86] , Limits of mappings, European Journal of Combinatorics (2017), accepted.

- [87] J. Neˇsetrˇil, P. Ossona de Mendez, and D.R. Wood, Characterizations and examples of graph classes with bounded expansion, European Journal of Combinatorics 33 (2012), no. 3, 350–373.
- [88] O. Pikhurko, An analytic approach to stability, Discrete Mathematics 310

(2010), 2951–2964.

- [89] M.H. Stone, The theory of representations of Boolean algebras, Transactions of the American Mathematical Society 40 (1936), 37–111.
- [90] B.A. Trakhtenbrot, The impossibility of an algorithm for the decision problem for ﬁnite domains, Doklady Akademii Nauk SSSR 70 (1950), 569–572.
- [91] Y. Zhao, Hypergraph limits: a regularity approach, arXiv:1302.1634v3 [math.CO], March 2014.


