# arXiv:1303.2865v1[math.CO]12Mar2013

## A Model Theory Approach to Structural Limits∗

J. Nesˇetˇril

Computer Science Institute of Charles University (IUUK and ITI) Malostranske´ na´m.25, 11800 Praha 1, Czech Republic nesetril@kam.ms.mff.cuni.cz

P. Ossona de Mendez

Centre d’Analyse et de Math´ematiques Sociales (CNRS, UMR 8557) 190-198 avenue de France, 75013 Paris, France pom@ehess.fr

(appeared in Comment. Math. Univ. Carolin. 53,4 (2012) 581–603)

##### Abstract

The goal of this paper is to unify two lines in a particular area of graph limits. First, we generalize and provide uniﬁed treatment of various graph limit concepts by means of a combination of model theory and analysis. Then, as an example, we generalize limits of bounded degree graphs from subgraph testing to ﬁnite model testing.

### 1 Introduction

Recently, graph sequences and graph limits are intensively studied, from diverse point of views: probability theory and statistics, property testing in computer science, ﬂag algebras, logic, graphs homomorphisms, etc. Four standard notions of graph limits have inspired this work:

- • the notion of dense graph limit [4, 15];
- • the notion of bounded degree graph limit [3, 2];
- • the notion of elementary limit e.g. [12, 13]
- • the notion of left limit developed by the authors [20, 21].


Let us brieﬂy introduce these notions. Our combinatorial terminology is standard and we refer to the standard books (such as [12, 17, 21, 23]) or original papers for more information.

∗This work, which appeared in Comment. Math. Univ. Carolin. 53,4 (2012) 581–603, is supported by grant ERCCZ LL-1201 of the Czech Ministry of Education and CE-ITI of GACRˇ

The ﬁrst approach consists in randomly picking a mapping from a test graph and to check whether this is a homomorphism. A sequence (Gn) of graphs will be said to be L-convergent if

hom(F,Gn) |Gn||F| converges for every ﬁxed (connected) graph F.

t(F,Gn) =

The second one is used to deﬁne the convergence of a sequence of graphs with bounded degrees. A sequence (Gn) of graphs with bounded maximum degrees will be said to be BS-convergent if, for every integer r, the probability that the ball of radius r centered at a random vertex of Gn is isomorphic to a ﬁxed rooted graph F converges for every F.

The third one is a general notion of convergence based on the ﬁrst-order properties satisﬁed by the elements of the sequence. A sequence (Gi)i∈N is elementarily convergent if, for every sentence φ there exists an integer nφ such that either all the Gi with i > nφ satisfy φ or none of them do.

The fourth notion of convergence is based in testing existence of homomorphisms from ﬁxed graphs: a sequence (Gn) is said to be left-convergent if, for every graph F, either all but a ﬁnite number of the graphs Gn contain a homomorphic image of F or only a ﬁnite number of Gn does. In other words, left-convergence is a weak notion of elementary convergence where we consider primitive positive sentences only.

These four notions proceed in diﬀerent directions and, particularly, relate to either dense or sparse graphs. The sparse–dense dichotomy seems to be a key question in the area.

In this paper we provide a unifying approach to these limits. Our approach is a combination of a functional analytic and model theoretic approach and thus applies to applies to more general structures (rather than graphs). Thus we use term structural limits.

The paper is organized as follows: In Section 2 we brieﬂy introduce a general machinery based on the Boolean algebras and dualities, see [10] for standard background material. In section 3 we apply this to Lindenbaum-Tarski algebras to get a representation of limits as measures (Theorem 1). In section 4 we mention an alternative approach by means of ultraproducts (i.e. a non-standard approach) which yields another representation (of course ineﬀective) of limits (Proposition 4). In section 5 we relate this to examples given in this section and particularly state results for bounded degree graphs, thus extending BenjaminiSchramm convergence [3] to the general setting of FO-convergence (Theorem 5). In the last section, we discuss the type of limit objects we would like to construct, and introduce some applications to the study of particular cases of ﬁrst-order convergence which are going to appear elsewhere.

### 2 Boolean Algebras, Stone Representation, and Measures

Recall that a Boolean algebra B is an algebra with two binary operations ∨ and ∧, a unary operation ¬ and two elements 0 and 1, such that (B,∨,∧) is a distributive lattice with minimum 0 and maximum 1 which is complemented (in the sense that the complementation ¬ satisﬁes a ∨ ¬a = 1 and a ∧ ¬a = 0).

The smallest Boolean algebra, denoted 2, has elements 0 and 1. In this Boolean algebra it holds 0 ∧ a = 0,1 ∧ a = a,0 ∨ a = a,1 ∨ a = 1,¬0 = 1, and ¬1 = 0. Another example is the powerset 2X of a set X has a natural structure of Boolean algebra, with 0 = ∅,1 = X, A ∨ B = A ∪ B, A ∧ B = A ∩ B and ¬A = X \ A.

Key examples for us are the following:

- Logical Example 1. The class of all ﬁrst-order formulas on a language L, considered up to logical equivalence, form a Boolean algebra with conjunction ∨, disjunction ∧ and negation ¬ and constants “false” (0) and “true” (1). This Boolean algebra will be denoted FO(L).

Also, we denote by FO0(L) the Boolean algebra of all ﬁrst-order sentences (i.e. formulas without free variables) on a language L, considered up to logical equivalence. Note FO0(L) is a Boolean sub-algebra of FO(L).

- Logical Example 2. Consider a logical theory T (with negation). The Lindenbaum-


Tarski algebra LT of T consists of the equivalence classes of sentences of T (here two sentences φ and ψ are equivalent if they are provably equivalent in T). The set of all the ﬁrst-order formulas that are provably false from T forms an ideal IT of the Boolean algebra FO0(L) and LT is nothing but the quotient algebra FO0(L)/IT.

With respect to a ﬁxed Boolean algebra B, a Boolean function is a function obtained by a ﬁnite combination of the operations ∨, ∧, and ¬.

Recall that a function f : B → B is a homomorphism of Boolean algebras if f(a ∨ b) = f(a) ∨ f(b), f(a ∧ b) = f(a) ∧ f(b), f(0) = 0 and f(1) = 1. A ﬁlter of a Boolean algebra B is an upper set X (meaning that x ∈ X and y ≥ x imply y ∈ X) that is a proper subset of B and that is closed under ∧ operation (∀x,y ∈ X it holds x ∧ y ∈ X). It is characteristic for Boolean algebras that the maximal ﬁlters coincide with the prime ﬁlters, that is, the (proper) ﬁlters X such that a ∨ b ∈ X implies that either a ∈ X or b ∈ X. One speaks of the maximal (i.e. prime ﬁlters) as of ultraﬁlters (they are also characterized by the fact that for each a either a ∈ X or ¬a ∈ X). It is easily checked that the mapping f  → f−1(1) is a bijection between the homomorphisms B → 2 and the ultraﬁlters on B.

A Stone space is a compact Hausdorﬀ with a basis of clopen subsets. With a Boolean algebra B associate a topological space

S(B) = ({x, x is a ultraﬁlter in B},τ),

where τ is the topology generated by all the KB(b) = {x, b ∈ x} (the subscript B will be omitted if obvious). Then S(B) is a Stone space. By the well-known Stone Duality Theorem [24], the mappings B  → S(B) and X  → Ω(X), where Ω(X) is the Boolean algebra of all clopen subsets of a Stone space X, constitute

- a one-one correspondence between the classes of all Boolean algebras and all Stone spaces.


In the language of category theory, Stone’s representation theorem means that there is a duality between the category of Boolean algebras (with homomorphisms) and the category of Stone spaces (with continuous functions). The two contravariant functors deﬁning this duality are denoted by S and Ω and deﬁned as follows:

For every homomorphism h : A → B between two Boolean algebra, we deﬁne the map S(h) : S(B) → S(A) by S(h)(g) = g ◦ h (where points of S(B) are identiﬁed with homomorphisms g : B → 2). Then for every homomorphism

- h : A → B, the map S(h) : S(B) → S(A) is a continuous function. Conversely, for every continuous function f : X → Y between two Stone spaces, deﬁne the map Ω(f) : Ω(Y ) → Ω(X) by Ω(f)(U) = f−1(U) (where elements of Ω(X) are identiﬁed with clopen sets of X). Then for every continuous function f : X → Y , the map Ω(f) : Ω(Y ) → Ω(X) is a homomorphism of Boolean algebras.


We denote by K = Ω ◦ S one of the two natural isomorphisms deﬁned by the duality. Hence, for a Boolean algebra B, K(B) is the set algebra {KB(b) :

- b ∈ B}, and this algebra is isomorphic to B. Thus we have a natural notion for convergent sequence of elements of S(B)


(from Stone representation follows that this may be seen as the pointwise converegence).

- Logical Example 3. Let B = FO0(L) denote the Boolean Lindenbaum-Tarski algebra of all ﬁrst-order sentences on a language L up to logical equivalence. Then the ﬁlters of B are the consistent theories of FO0(L) and the ultraﬁlters of B are the complete theories of FO0(L) (that is maximal consistent sets of sentences). It follows that the closed sets of S(B) correspond to ﬁnite sets of consistent theories. According to G¨del’s completeness theorem, every consistent theory has a model. It follows that the completeness theorem for ﬁrst-order logic — which states that that a set of ﬁrst-order sentences has a model if and only if every ﬁnite subset of it has a model — amounts to say that S(B) is compact. The points of S(B) can also be identiﬁed with elementary equivalence classes of models. The notion of convergence of models induced by the topology of S(B), called elementary convergence, has been extensively studied.


An ultraﬁlter on a Boolean algebra B can be considered as a ﬁnitely additive measure, for which every subset has either measure 0 or 1. Because of the equivalence of the notions of Boolean algebra and of set algebra, we deﬁne the ba space ba(B) of B has the space of all bounded additive functions f : B → R. Recall that a function f : B → R is additive if for all x,y ∈ B it holds

x ∧ y = 0 =⇒ f(x ∨ y) = f(x) + f(y). The space ba(B) is a Banach space for the norm

f(x) − inf

f = sup

f(x).

x∈B

x∈B

(Recall that the ba space of an algebra of sets Σ is the Banach space consisting of all bounded and ﬁnitely additive measures on Σ with the total variation norm.)

Let h be a homomorphism B → 2 and let ι : 2 → R be deﬁned by ι(0) = 0 and ι(1) = 1. Then ι ◦ h ∈ ba(B). Conversely, if f ∈ ba(B) is such that f(B) = {0,1} then ι−1 ◦ f is a homomorphism B → 2. This shows that S(B) can be identiﬁed with a subset of ba(B).

One can also identify ba(B) with the space ba(K(B)) of ﬁnitely additive measure deﬁned on the set algebra K(B). As vector spaces ba(B) is isomorphic to ba(K(B)) and thus ba(B) is then clearly the (algebraic) dual of the normed vector space V (B) (of so-called simple functions) generated by the indicator functions of the clopen sets (equipped with supremum norm). Indicator

functions of clopen sets are denoted by 1K(b) (for some b ∈ B) and deﬁned by

1K(b)(x) =

1 if x ∈ K(b) 0 otherwise.

The pairing of a function f ∈ ba(B) and a vector X = ni=1 ai1K(b

i) is deﬁned by

n

[f,X] =

aif(bi).

i=1

That [f,X] does not depend on a particular choice of a decomposition of X follows from the additivity of f. We include a short proof for completeness: Assume i αi1K(b

i). As for every b,b ∈ B it holds f(b) = f(b ∧ b ) + f(b ∧ ¬b ) and 1K(b) = 1K(b∧b ) + 1K(b∧¬b ) we can express the two sums as j α j1K(b

i) = i βi1K(b

j) (where b i ∧ b j = 0 for every i = j), with i αif(bi) = j α jf(b j) and i βif(bi) = j β jf(b j). As b i ∧b j = 0 for every i αif(bi) = i βif(bi).

j) = j β j1K(b

- i = j, for x ∈ K(b j) it holds α j = X(x) = β j. Hence α j = β j for every j. Thus


Note that X  → [f,X] is indeed continuous. Thus ba(B) can also be identiﬁed with the continuous dual of V (B). We now show that the vector space V (B) is dense in the space C(S(B)) of continuous functions from S(B) to R, hence that ba(B) can also be identiﬁed with the continuous dual of C(S(B)):

- Lemma 1. The vector space V (B) is dense in C(S(B)) (with the uniform norm).


Proof. Let f ∈ C(S(B)) and let > 0. For z ∈ f(S(B)) let Uz be the preimage by f of the open ball B /2(z) of R centered in z. As f is continuous, Uz is a open set of S(B). As {K(b) : b ∈ B} is a basis of the topology of S(B), Uz can be expressed as a union b∈F(U

z) K(b). It follows that z∈f(S(B)) b∈F(U

z) K(b) is a covering of S(B) by open sets. As S(B) is compact, there exists a ﬁnite subset F of z∈f(S(B)) F(Uz) that covers S(B). Moreover, as for every b,b ∈ B it holds K(b) ∩ K(b ) = K(b ∧ b ) and K(b) \ K(b ) = K(b ∧ ¬b ) it follows that we can assume that there exists a ﬁnite family F such that S(B) is covered by open sets K(b) (for b ∈ F ) and such that for every b ∈ F there exists b ∈ F such that K(b) ⊆ K(b ). In particular, it follows that for every b ∈ F , f(K(b)) is included in an open ball of radius  /2 of R. For each b ∈ F choose a point xb ∈ S(B) such that b ∈ xb. Now deﬁne

fˆ=

f(xb)1K(b)

b∈F

Let x ∈ S(B). Then there exists b ∈ F such that x ∈ K(b). Thus

|f(x) − fˆ(x)| = |f(x) − f(xb)| <  . Hence f − fˆ ∞ < .

It is diﬃcult to exhibit a basis of C(S(B)) or V (B). However, every meet sub-semilattice of a Boolean algebra B generating B contains (via indicator functions) a basis of V (B):

- Lemma 2. Let X ⊆ B be closed by ∧ and such that X generates B (meaning that every element of B can be obtained as a Boolean function of ﬁnitely many elements from X).


Then {1b : b ∈ X} ∪ {1} (where 1 is the constant function with value 1) includes a basis of the vector space V (B).

Proof. Let b ∈ B. As X generates B there exist b1,...,bk ∈ X and a Boolean function F such that b = F(b1,...,bk). As 1x∧y = 1x 1y and 1¬x = 1 − 1x there exists a polynomial PF such that 1b = PF(1b

#### ). For I ⊆ [k], the monomial i∈I 1b

#### ,...,1b

1

k

where bI = i∈I bi. It follows that 1b is a linear combination of the functions 1b

rewrites as 1b

i

I

(I ⊆ [k]) which belong to X if I = ∅ (as X is closed under ∧ operation) and equal 1, otherwise.

I

We are coming to the ﬁnal transformation of our route: One can see that bounded additive real-value functions on a Boolean algebra B naturally deﬁne continuous linear forms on the vector space V (B) hence, by density, on the Banach space C(S(B)) (of all continunous functions on S(B) equipped with supremum norm). It follows (see e.g. [23]) from Riesz representation theorem that the topological dual of C(S(B)) is the space rca(S(B)) of all regular countably additive measures on S(B). Thus the equivalence of ba(B) and rca(S(B)) follows. We summarize all of this as the following:

- Proposition 1. Let B be a Boolean algebra, let ba(B) be the Banach space of


bounded additive real-valued functions equipped with the norm f = supb∈B f(b)−

infb∈B f(b), let S(B) be the Stone space associated to B by Stone representation theorem, and let rca(S(B)) be the Banach space of the regular countably additive measure on S(B) equipped with the total variation norm.

Then the mapping CK : rca(S(B)) → ba(B) deﬁned by CK(µ) = µ◦K is an isometric isomorphism. In other words, CK is deﬁned by

CK(µ)(b) = µ({x ∈ S(B) : b ∈ x}) (considering that the points of S(B) are the ultraﬁlters on B).

Note also that, similarly, the restriction of CK to the space Pr(S(B)) of all (regular) probability measures on S(B) is an isometric isomorphism of Pr(S(B)) and the subset ba1(B) of ba(B) of all positive additive functions f on B such that f(1) = 1.

A standard notion of convergence in rca(S(B)) (as the continuous dual of C(S(B))) is the weak ∗-convergence: a sequence (µn)n∈N of measures is convergent if, for every f ∈ C(S(B)) the sequence f(x)dµn(x) is convergent. Thanks to the density of V (B) this convergence translates as pointwise convergence in ba(B) as follows: a sequence (gn)n∈N of functions in ba(B) is convergent if, for every b ∈ B the sequence (gn(b))n∈N is convergent. As rca(S(B)) is complete, so is rca(B). Moreover, it is easily checked that ba1(B) is closed in ba(B).

In a more concise way, we can write, for a sequence (fn)n∈N of functions in ba(B) and for the corresponding sequence (µf

)n∈N of regular measures on lim n→∞

n

- S(B):


n ⇒ µf. The whole situation is summarized on Fig. 1.

fn pointwise ⇐⇒ µf

Stone duality

|B ≈ K(B)|
|---|


|S(B)|
|---|


(injection)

ba(B) ≈ ba(K(B)) rca(S(B))

Continuous dual

Continuous dual

C(S(B))

dense subspace

V (B)

Figure 1: Several spaces deﬁned from a Boolean algebra, and their interrelations.

The above theory was not developed for its own sake but in order to demonstrate a natural approach to structural limits. The next example is a continuation of our main interpretation, which we started in Logical examples 2 and 3.

- Logical Example 4. Let B = FO0(L) denote the Boolean algebra of all ﬁrstorder sentences on a language L up to logical equivalence. We already noted


that the points of S(B) are complete theories of FO0(L), and that each complete theory has at least one model. Assume L is a ﬁnite language. Then for every n ∈ N there exists a sentence φn such that for every complete theory T ∈ FO0(L) it holds φn ∈ T if and only if T has a unique model and this model has at most n elements. Let U = n≥1 K(φn). Then U is open but not closed. The indicator function 1U is thus measurable but not continuous. This function has the nice property that for every complete theory T ∈ S(B) it holds

1U(T) =

1, if T has a ﬁnite model; 0, otherwise.

### 3 Limits via Fragments and Measures

We provide a unifying approach based on the previous section. We consider the special case of Boolean algebras induced by a fragment of the class FO(L) of the ﬁrst-order formulas over a ﬁnite relational language L. In this context, the language L will be described by its signature, that is the set of non-logical symbols (constant symbols, and relation symbols, along with the arities of the

relation symbols). An FO(L)-structure is then a set together with an interpretation of all relational and function symbols. Thus for example the signature of the language LG of graphs is the symbol ∼ interpreted as the adjacency relation: x ∼ y if {x,y} is an edge of the graph.

We now introduce our notion of convergence. Our approach is a combination of model theoretic and analytic approach.

Recall that a formula is obtained from atomic formulas by the use of the negation (¬), logical connectives (∨ and ∧), and quantiﬁcation (∃ and ∀). A sentence (or closed formula) is a formula without free variables.

The quantiﬁer rank qrank(φ) of a formula φ is the maximum depth of a quantiﬁer in φ. For instance, the quantiﬁer rank of the formula

∃x ((∃y (x ∼ y)) ∨ (∀y ∀z ¬(x ∼ y) ∧ ¬(y ∼ z))) has quantiﬁer rank 3.

The key to our approach is the following deﬁnition.

- Deﬁnition 1. Let φ(x1,...,xp) be a ﬁrst-order formula with p free variables (in the language L) and let G be an L-structure. We denote


φ,G = |{(v1,...,vp) ∈ Gp : G |= φ(v1,...,vp)}| |G|p

. (1)

In other words, φ,G is the probability that φ is satisﬁed in G when the p free variables correspond to a random p-tuple of vertices of G. The value φ,G is called the density of φ in G. Note that this deﬁnition is consistent in the sense that although any formula φ with p free variables can be considered as a formula with q ≥ p free variables with q − p unused variables, we have

|{(v1,...,vq) : G |= φ(v1,...,vp)}| |G|q

= |{(v1,...,vp) : G |= φ(v1,...,vp)}| |G|p

.

It is immediate that for every formula φ it holds  ¬φ,G = 1 − φ,G . Moreover, if φ1,...,φn are formulas, then by de Moivre’s formula, it holds

k

n

n

(−1)k+1

φi

,G .

φi,G =

j

1≤i1<···<ik≤n

j=1

i=1

k=1

In particular, if φ1,...,φk are mutually exclusive (meaning that φi and φj cannot hold simultaneously for i = j) then it holds

k

k

φi,G =

φi,G .

i=1

i=1

In particular, for every ﬁxed graph G, the mapping φ  → φ,G is additive (i.e.  ·,G ∈ ba(FO(L))):

φ1 ∧ φ2 = 0 =⇒ φ1 ∨ φ2,G = φ1,G + φ2,G .

Thus we may apply the above theory to additive functions  ·,G and to structural limits we shall deﬁne now.

Advancing this note that in the case of a sentence φ (that is a formula with no free variables, i.e. p = 0), the deﬁnition reduces to

φ,G =

1, if G |= φ; 0, otherwise.

.

Thus the deﬁnition of φ,G will suit to the elementary convergence. Elementary convergence and all above graph limits are captured by the following deﬁnition:

- Deﬁnition 2. Let X be a fragment of FO(L). A sequence (Gn)n∈N of L-structures is X-convergent if for every φ ∈ X, the


sequence ( φ,Gn )n∈N converges.

For a Boolean sub-algebra X of FO(L), we deﬁne T(X) has the space of all ultraﬁlters on X, which we call complete X-theories. The space T(X) is endowed with the topology deﬁned from its clopen sets, which are deﬁned as the sets K(φ) = {T ∈ T(X) : T φ} for some φ ∈ X. In the sake for simplicity, we denote by 1φ (for φ ∈ X) the indicator function of the clopen set K(φ) deﬁned by φ. Hence, 1φ(T) = 1 if φ ∈ T, and 1φ(T) = 0 otherwise.

It should be now clear that the above general approach yields the following:

- Theorem 1. Let X be a Boolean sub-algebra of FO(L) and let G be the class of all ﬁnite L-structures.


There exists an injective mapping G  → µG from G to the space of probability measures on T(X) such that for every φ ∈ X it holds

φ,G = 1φ(T)dµG(T).

A sequence (Gn)n∈N of ﬁnite L-structures is X-convergent if and only if the sequence (µG

n ⇒ µ then for every φ ∈ X it holds

)n∈N is weakly convergent. Moreover, if µG

n

φ,Gn = 1φ(T)dµ(T). In this paper, we shall be interested in speciﬁc fragments of FO(L):

lim

n→∞

- • FO(L) itself;
- • FOp(L) (where p ∈ N), which is the fragment consisting of all formulas with at most p free variables (in particular, FO0(L) is the fragment of all ﬁrst-order sentences);
- • QF(L), which is the fragment of quantiﬁer-free formulas (that is: propositional logic);
- • FOlocal(L), which is the fragment of local formulas, deﬁned as follows.


Let r ∈ N. A formula φ(x1,...,xp) is r-local if, for every L-structure G and every v1,...,vp ∈ Gp it holds

G |= φ(v1,...,vp) ⇐⇒ G[Nr(v1,...,vp)] |= φ(v1,...,vp),

where Nr(v1,...,vp) is the closed r-neighborhood of x1,...,xp in the L-structure G (that is the set of elements at distance at most r from at least one of x1,...,xp in the Gaifman graph of G), and where G[A] denotes the sub-L-structure of G induced by A. A formula φ is local if it is r-local for some r ∈ N; the fragment FOlocal(L) is the set of all local formulas (over the language L). This fragment form an important fragment, particularly because of the following structure theorem.

- Theorem 2 (Gaifman locality theorem [9]). For every ﬁrst-order formula φ(x1,...,xn) there exist integers t and r such that φ is equivalent to a Boolean combination


of t-local formulas ξj(xi

#### ,...,xi

) and sentences of the form

1

s

∃y1 ...∃ym

dist(yi,yj) > 2r ∧

ψ(yi) (2)

1≤i<j≤m

1≤i≤m

where ψ is r-local. Furthermore, if φ is a sentence, only sentences (2) occur in the Boolean combination.

From this theorem follows a general statement:

- Proposition 2. Let (Gn) be a sequence of graphs. Then (Gn) is FO-convergent if and only if it is both FOlocal-convergent and elementarily-convergent.


Proof. Assume (Gn)n∈N is both FOlocal-convergent and elementarily-convergent and let φ ∈ FO be a ﬁrst order formula with n free variables. According to

- Theorem 2, there exist integers t and r such that φ is equivalent to a Boolean


combination of t-local formula ξ(xi

#### ,...,xi

) and of sentences. It follows that

1

s

φ,G can be expressed as a function of values of the form ξ,G where ξ is either a local formula or a sentence. Thus (Gn)n∈N is FO-convergent.

Notice that if φ1 and φ2 are local formulas, so are φ1 ∧ φ2, φ1 ∨ φ2 and ¬φ1. It follows that FOlocal is a Boolean sub-algebra of FO. It is also clear that all the other fragments described above correspond to sub-algebras of FO. This means that there exist canonical injective Boolean-algebra homomorphisms from these fragments X to FO, that will correspond to surjective continuous functions (projections) from S(FO) to S(X) and it is not hard to see that they also correspond to surjective maps from ba(FO) to ba(X) and to surjective pushforwards from rca(S(FO) to rca(S(X)).

Recall that a theory T is a set of sentences. (Here we shall only consider ﬁrst-order theories, so a theory is a set of ﬁrst-order sentences.) The theory T is consistent if one cannot deduce from T both a sentence φ and its negation. The theory T is satisﬁable if it has a model. It follows from G¨del’s completeness theorem that, in the context of ﬁrst-order logic, a theory is consistent if and only if it is satisﬁable. Also, according to the compactness theorem, a theory has a model if and only if every ﬁnite subset of it has a model. Moreover, according to the downward L¨wenheim-Skolem theorem, there exists a countable model.

- A theory T is a complete theory if it is consistent and if, for every sentence


φ ∈ FO0(L), either φ or ¬φ belongs to T. Hence every complete theory has a countable model. However, a complete theory which has an inﬁnite model has inﬁnitely many non-isomorphic models.

It is natural to ask whether one can consider fragments that are not Boolean sub-algebras of FO(L) and still have a description of the limit of a converging

sequence as a probability measure on a nice measurable space. There is obviously a case where this is possible: when the convergence of φ,Gn for every φ in a fragment X implies the convergence of ψ,Gn for every ψ in the minimum Boolean algebra containing X. We prove now that this is an instance of a more general phaenomenon:

- Proposition 3. Let X be a fragment of FO(L) closed under (ﬁnite) conjunction


— that is: a meet semilattice of FO(L) — and let BA(X) be the Boolean algebra generated by X (that is the closure of X by ∨,∧ and ¬). Then X-convergence is equivalent to BA(X)-convergence.

Proof. Let Ψ ∈ BA(X). According to Lemma 2, there exist φ1,...,φk ∈ X and α0,α1,...,αk ∈ R such that

k

1Ψ = α01 +

αi1φ

.

i

i=1

Let G be a graph, let Ω = S(BA(X)) and let µG ∈ rca(Ω) be the associated measure. Then

Ψ,G =

1Ψ dµG =

Ω

Ω

k

α01 +

αi1φ

i

i=1

k

dµG = α0 +

αi φi,G .

i=1

Thus if (Gn)n∈N is an X-convergent sequence, the sequence ( ψ,Gn )n∈N converges for every ψ ∈ BA(X), that is (Gn)n∈N is BA(X)-convergent.

Continuing to develop the general mechanism for the structural limits we consider fragments of FO quantiﬁed by the number of free variables.

We shall allow formulas with p free variables to be considered as a formula with q > p variables, q − p variables being unused. As the order of the free variables in the deﬁnition of the formula is primordial, it will be easier for us to consider sentences with p constants instead of formulas with p free variables. Formally, denote by Lp the language obtained from L by adding p (ordered) symbols of constants c1,...,cp. There is a natural isomorphism of Boolean algebras νp : FOp(L) → FO0(Lp), which replaces the occurrences of the p free variables x1,...,xp in a formula φ ∈ FOp by the corresponding symbols of constants c1,...,cp, so that it holds, for every graph G, for every φ ∈ FOp and every v1,...,vp ∈ G:

G |= φ(v1,...,vp) ⇐⇒ (G,v1,...,vp) |= νp(φ). The Stone space associated to the Boolean algebra FO0(Lp) is the space

- T(Lp) of all complete theories in the language Lp. Also, we denote by Tω the Stone space representing the Boolean algebra T(FO0(Lω)) ≈ FO. One of the speciﬁc properties of the spaces T(Lp) is that they are endowed with an ultrametric derived from the quantiﬁer-rank:


dist(T1,T2) =

0 if T1 = T2 2−min{qrank(θ): θ∈T

1\T2} otherwise.

This ultrametric deﬁnes the same topology as the Stone representation theorem. As a compact metric space, T(Lp) is (with the Borel sets deﬁned by the metric topology) a standard Borel space.

For each p ≥ 0, there is a natural projection πp : Tp+1 → Tp, which maps a complete theory T ∈ Tp+1 to the subset of T containing the sentences where only the p ﬁrst constant symbols c1,...,cp are used. Of course we have to check that πp(T) is a complete theory in the language Lp but this is indeed so.

According to the ultrametrics deﬁned above, the projections πp are contractions (hence are continuous). Also, there is a natural isometric embedding ηp : Tp → Tp+1 deﬁned as follows: for T ∈ Tp, the theory ηp(T) is the deductive closure of T ∪ {cp = cp+1}. Notice that ηp(T) is indeed complete: for every sentence φ ∈ FO(Lp+1), let φ be the sentence obtained from φ by replacing each symbol cp+1 by cp. It is clear that cp = cp+1 φ ↔ φ. As either φ or ¬ φ belongs to T, either φ or ¬φ belongs to ηp(T). Moreover, we deduce easily from the fact that φ and φ have the same quantiﬁer rank that ηp is an isometry. Finally, let us note that πp ◦ ηp is the identity of Tp.

For these fragments we shall show a particular nice construction, well nonstandard construction, of limiting measure.

### 4 A Non-standard Approach

The natural question that arises from the result of the previous section is whether one can always ﬁnd a representation of the FO-limit of an FO-converging sequence by a “nice” measurable L-structure.

It appears that a general notion of limit object for FO-convergence can be obtained by a non-standard approach. In this we follow closely Elek and Szegedy [7].

We ﬁrst recall the ultraproduct construction. Let (Gn)n∈N be a ﬁnite sequence of ﬁnite L-structures and let U be a non-principal ultraﬁlter. Let G = i∈N Gi and let ∼ be the equivalence relation on V deﬁned by (xn) ∼ (yn) if {n : xn = yn} ∈ U. Then the ultraproduct of the L-structures Gn is the quotient of G by ∼, and it is denoted U Gi. For each relational symbol R with arity p, the interpretation R G of R in the ultraproduct is deﬁned by

([v1],...,[vp]) ∈ R G ⇐⇒ {n : (vn1,...,vnp) ∈ RG

} ∈ U.

n

The fundamental theorem of ultraproducts proved by  Lo´s makes ultraproducts particularly useful in model theory. We express it now in the particular case of L-structures indexed by N but its general statement concerns structures indexed by a set I and the ultraproduct constructed by considering an ultraﬁlter U over I.

- Theorem 3 ([14]). For each formula φ(x1,...,xp) and each v1,...,vp ∈ i Gi we have


U

Gi |= φ([v1],...,[vp]) iﬀ {i : Gi |= φ(vi1,...,vip)} ∈ U.

Note that if (Gi) is elementary-convergent, then U Gi is an elementary limit of the sequence: for every sentence φ, according to Theorem 3, we have

U

Gi |= φ ⇐⇒ {i : Gi |= φ} ∈ U.

A measure ν extending the normalised counting measures νi of Gi is then obtained via the Loeb measure construction. We denote by P(Gi) the Boolean algebra of the subsets of vertices of Gi, with the normalized measure νi(A) =

|A| |Gi|. We deﬁne P = i P(Gi)/I, where I is the ideal of the elements {Ai}i∈N such that {i : Ai = ∅} ∈ U. We have

[x] ∈ [A] iﬀ {i : xi ∈ Ai} ∈ U.

These sets form a Boolean algebra over U Gi. Recall that the ultralimit limU an deﬁned for every (an)n∈N ∈ ∞(N) is such that for every > 0 we have

an + ]} ∈ U. Deﬁne

{i : ai ∈ [lim

an − ; lim

U

U

ν([A]) = lim

νi(Ai).

U

Then ν : P → R is a ﬁnitely additive measure. Remark that, according to Hahn-Kolmogorov theorem, proving that ν extends to a countably additive measure amounts to prove that for every sequence ([An]) of disjoint elements of P such that n[An] ∈ P it holds ν( n[An]) = n ν([An]).

A subset N ⊆ U Gi is a nullset if for every > 0 there exists [A ] ∈ P such that N ⊆ [A ] and ν([A ]) < . The set of nullsets is denoted by N. A set

- B ⊆ U Gi is measurable if there exists B ∈ P such that B∆ B ∈ N. The following theorem is proved in [7]:


- Theorem 4. The measurable sets form a σ-algebra BU and ν(B) = ν( B) deﬁnes a probability measure on BU.


Notice that this construction extends to the case where to each Gi is associated a probability measure νi. Then the limit measure ν is non-atomic if and only if the following technical condition holds: for every > 0 and for every (An) ∈ Gn, if for U-almost all n it holds νn(An) ≥ then there exists δ > 0 and (Bn) ∈ Gn such that for U-almost all n it holds Bn ⊆ An and min(νn(Bn),νn(An \ Bn)) ≥ δ. This obviously holds if νn is a normalized counting measure and limU |Gn| = ∞.

Let fi : Gi → [−d;d] be real functions, where d > 0. One can deﬁne f : U Gi → [−d;d] by

f([x]) = lim

fi(xi).

U

We say that f is the ultralimit of the functions {fi}i∈N and that f is an ultralimit function.

Let φ(x) be a ﬁrst order formula with a single free variable, and let fiφ : Gi → {0,1} be deﬁned by

fiφ(x) =

1 if Gi |= φ(x); 0 otherwise.

- and let fφ : U Gi → {0,1} be deﬁned similarly on the L-structure U Gi.


Then fφ is the ultralimit of the functions {fiφ} according to Theorem 3. The following lemma is proved in [7].

#### Lemma 3. The ultralimit functions are measurable on U Gi and

x∈Gi fi(x) |Gi|

f dν = lim

.

U

U Gi

In particular, for every formula φ(x) with a single free variable, we have: ν [x] :

Gi |= φ([x]) = lim

φ,Gi .

U

U

Let ψ(x,y) be a formula with two free variables. Deﬁne fi : Gi → [0;1] by

fi(x) = |{y ∈ Gi : Gi |= ψ(x,y)}| |Gi|

.

and let

Gi |= ψ([x],[y] .

f([x]) = µ [y] :

U

Let us check that f([x]) is indeed the ultralimit of fi(xi). Fix [x]. Let gi : Gi → {0,1} be deﬁned by

1 if Gi |= ψ(xi,y) 0 otherwise.

gi(y) =

- and let g : U Gi → {0,1} be deﬁned similarly by


g([y]) =

1 if U Gi |= ψ([x],[y]) 0 otherwise.

According to Theorem 3 we have

U

Gi |= ψ([x],[y]) ⇐⇒ {i : Gi |= ψ(xi,yi)} ∈ U.

It follows that g is the ultralimit of the functions {gi}i∈N. Thus, according to

- Lemma 3 we have


ν [y] :

U

|{y ∈ Gi : Gi |= ψ(xi,yi)}| |Gi|

GI |= ψ([x],[y]) = lim

,

U

that is:

f([x]) = lim

fi(xi).

U

Hence f is the ultralimit of the functions {fi}i∈N and, according to Lemma 3, we have

1ψ([x],[y]) dν([x]) dν([y]) = lim

ψ,Gi .

U

This property extends to any number of free variables. We formulate this as a summary of the results of this section.

- Proposition 4. Let (Gn)n∈N be a sequence of ﬁnite L-structures and let U be a non-principal ultraﬁlter on N. Then there exists a measure ν on the ultraproduct


G = U Gn such that for every ﬁrst-order formula φ with p free variables it holds:

···

Gp

1φ([x1],...,[xp]) dν([x1]) ... dν([xp]) = lim

ψ,Gi .

U

Moreover, the above integral is invariant by any permutation on the order of the integrations: for every permutation σ of [p] it holds

ψ,Gi = ···

lim

U

Gp

1φ([x1],...,[xp]) dν([xσ(1)]) ... dν([xσ(p)]).

However, the above constructed measure algebra is non-separable (see [7, 5] for discussion).

### 5 A Particular Case

Instead of restricting convergence to a fragment of FO(L), it is also interesting to consider restricted classes of structures. For instance, the class of graphs with maximum degree at most D (for some integer D) received much attention. Speciﬁcally, the notion of local weak convergence of bounded degree graphs was introduced in [3]:

A rooted graph is a pair (G,o), where o ∈ V (G). An isomorphism of rooted graph φ : (G,o) → (G ,o ) is an isomorphism of the underlying graphs which satisﬁes φ(o) = o . Let D ∈ N. Let GD denote the collection of all isomorphism classes of connected rooted graphs with maximal degree at most D. For simplicity’s sake, we denote elements of GD simply as graphs. For (G,o) ∈ GD and r ≥ 0 let BG(o,r) denote the subgraph of G spanned by the vertices at distance at most r from o. If (G,o),(G ,o ) ∈ GD and r is the largest integer such that (BG(o,r),o) is rooted-graph isomorphic to (BG (o ,r),o ), then set ρ((G,o),(G ,o )) = 1/r, say. Also take ρ((G,o),(G,o)) = 0. Then ρ is metric on GD. Let MD denote the space of all probability measures on GD that are measurable with respect to the Borel σ-ﬁeld of ρ. Then MD is endowed with the topology of weak convergence, and is compact in this topology.

A sequence (Gn)n∈N of ﬁnite connected graphs with maximum degree at most D is BS-convergent if, for every integer r and every rooted connected graph (F,o) with maximum degree at most D the following limit exists:

(v,r) ∼= (F,o)}| |Gn|

|{v : BG

n

.

lim

n→∞

This notion of limits leads to the deﬁnition of a limit object as a probability measure on GD [3].

However, as we shall see below, a nice representation of the limit structure can be given. To relate BS-convergence to X-convergence, we shall consider the fragment FOlocal1 of those formulas with at most 1 free variable that are local. Formally, let FOlocal1 = FOlocal ∩ FO1.

- Proposition 5. Let (Gn) be a sequence of ﬁnite graphs with maximum degree d, with limn→∞ |Gn| = ∞.


Then the following properties are equivalent:

- 1. the sequence (Gn)n∈N is BS-convergent;
- 2. the sequence (Gn)n∈N is FOlocal1 -convergent;
- 3. the sequence (Gn)n∈N is FOlocal-convergent.


Proof. If (Gn)n∈N is FOlocal-convergent, it is FOlocal1 -convergent;

If (Gn)n∈N is FOlocal1 -convergent then it is BS-convergent as for any ﬁnite rooted graph (F,o), testing whether the the ball of radius r centered at a vertex x is isomorphic to (F,o) can be formulated by a local ﬁrst order formula.

Assume (Gn)n∈N is BS-convergent. As we consider graphs with maximum degree d, there are only ﬁnitely many isomorphism types for the balls of radius r centered at a vertex. It follows that any local formula ξ(x) with a single variable can be expressed as the conjunction of a ﬁnite number of (mutually exclusive) formulas ξ(F,o)(x), which in turn correspond to subgraph testing. It follows that BS-convergence implies FOlocal1 -convergence.

Assume (Gn)n∈N is FOlocal1 -convergent and let φ(x1,...,xp) be an r-local formula. Let Fφ be the set of all p-tuples ((F1,f1),...,(Fp,fp)) of rooted connected graphs with maximum degree at most d and radius (from the root) at

most r such that i Fi |= φ(f1,...,fp). Then, for every graph G the sets

{(v1,...,vp) : G |= φ(v1,...,vp)} and

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

According to this proposition, the BS-limit of a sequence of graphs with max-

imum degree at most D corresponds to a probability measure on S(FOlocal1 (L)) (where L is the language of graphs) whose support is included in the clopen

set K(ζD), where ζD is the sentence expressing that the maximum degree is at most D. As above, the Boolean algebra FOlocal1 (L) is isomorphic to the Boolean algebra deﬁned by the fragment X ⊂ FO0(L1) of sentences in the language of rooted graphs that are local with respect to the root. According to this locality, any two countable rooted graphs (G1,r1) and (G2,r2), the trace of the complete theories of (G1,r1) and (G2,r2) on X are the same if and only if the

(rooted) connected component (G 1,r1) of (G1,r1) containing the root r1 is elementary equivalent to the (rooted) connected component (G 2,r2) of (G2,r2) containing the root r2. As isomorphism and elementary equivalence are equivalent for countable connected graphs with bounded degrees it is easily checked that KX(ζD) is homeomorphic to GD. Hence our setting leads essentially to the same limit object as [3] for BS-convergent sequences.

We now consider how full FO-convergence diﬀers to BS-convergence for sequence of graphs with maximum degree at most D. This shows a remarkable stability of BS-convergence.

Corollary 1. A sequence (Gn) of ﬁnite graphs with maximum degree at most d such that limn→∞ |Gn| = ∞ is FO-convergent if and only if it is both BSconvergent and elementarily convergent.

Proof. This is a direct consequence of Propositions 2 and 5.

Explicit limit objects are known for sequence of bounded degree graphs, both for BS-convergence (graphing) and for elementary convergence (countable graphs). It is natural to ask whether a nice limit object could exist for full FO-convergence. We shall now answer this question by the positive.

Let V be a standard Borel space with a measure µ. Suppose that T1,T2,...,Tk are measure preserving Borel involutions of X. Then the system

G = (V,T1,T2,...,Tk,µ)

is called a measurable graphing [1]. Here x is adjacent to y, if x = y and Tj(x) = y for some 1 ≤ j ≤ k. Now if If V is a compact metric space with a Borel measure µ and T1,T2,...,Tk are continuous measure preserving involutions of V , then G = (V,T1,T2,...,Tk,µ) is a topological graphing. It is a consequence of [3] and [8] that every local weak limit of ﬁnite connected graphs with maximum degree at most D can be represented as a measurable graphing. Elek [6] further proved the representation can be required to be a topological graphing.

For an integer r, a graphing G = (V,T1,...,Tk,µ) and a ﬁnite rooted graph (F,o) we deﬁne the set

Dr(G,(F,o)) = {x ∈ G,Br(G,x) (F,o)}.

We shall make use of the following lemma which reduces a graphing to its essential support.

- Lemma 4 (Cleaning Lemma). Let G = (V,T1,...,Td,µ) be a graphing. Then there exists a subset X ⊂ V with 0 measure such that X is globally


invariant by each of the Ti and G = (V − X,T1,...,Td,µ) is a graphing such that for every ﬁnite rooted graph (F,o) and integer r it holds

µ(Dr(G ,(F,o))) = µ(Dr(G,(F,o))) (which means that G is equivalent to G) and

Dr(G ,(F,o)) = ∅ ⇐⇒ µ(Dr(G ,(F,o))) > 0.

Proof. For a ﬁxed r, deﬁne Fr has the set of all (isomorphism types of) ﬁnite rooted graphs (F,o) with radius at most r such that µ(Dr(G,(F,o))) = 0. Deﬁne

X =

Dr(G,(F,o)).

r∈N (F,o)∈Fr

Then µ(X) = 0, as it is a countable union of 0-measure sets.

We shall now prove that X is a union of connected components of G, that is that X is globally invariant by each of the Ti. Namely, if x ∈ X and y is adjacent to x, then y ∈ X. Indeed: if x ∈ X then there exists an integer r such that µ(D(G,Br(G,x))) = 0. But it is easily checked that

µ(D(G,Br+1(G,y))) ≤ d · µ(D(G,Br(G,x))).

Hence y ∈ X. It follows that for every 1 ≤ i ≤ d we have Ti(X) = X. So we can deﬁne the graphing G = (V − X,T1,...,Td,µ).

Let (F,o) be a rooted ﬁnite graph. Assume there exists x ∈ G such that Br(G ,r) (F,o). As X is a union of connected components, we also have Br(G,r) (F,o) and x ∈/ X.

It follows that µ(D(G,(F,o))) > 0 hence µ(Dr(G ,(F,o))) > 0. The cleaning lemma allows us a clean description of FO-limits in the bounded

degree case:

Theorem 5. Let (Gn)n∈N be a FO-convergent sequence of ﬁnite graphs with maximum degree d, with limn→∞ |Gn| = ∞. Then there exists a graphing G and a countable graph Gˆ such that

- • G is a BS-limit of the sequence,
- • Gˆ is an elementary limit of the sequence,
- • G ∪ Gˆ is an FO-limit of the sequence.


Proof. Let G be a BS-limit, which has been “cleaned” using the previous lemma, and let Gˆ be an elementary limit of G. It is clear that G ∪ Gˆ is also a BS-limit of the sequence, so the lemma amounts in proving that G ∪ Gˆ is elementarily equivalent to Gˆ.

According to Hanf’s theorem [11], it is suﬃcient to prove that for every integers r,t and for every rooted ﬁnite graph (F,o) (with maximum degree d) the following equality holds:

min(t,|Dr(G ∪ G,ˆ (F,o))|) = min(t,|Dr(G,ˆ (F,o))|).

Assume for contradiction that this is not the case. Then |Dr(G,ˆ (F,o))| < t and Dr(G,(F,o)) is not empty. However, as G is clean, this implies µ(Dr(G,(F,o))) = α > 0. It follows that for every suﬃciently large n it holds |Dr(Gn,(F,o))| > α/2|Gn| > t. Hence |Dr(G,ˆ (F,o))| > t, contradicting our hypothesis.

Note that the reduction of the satisfaction problem of a general ﬁrst-order formula φ with p free variables to a case analysis based on the isomorphism type of a bounded neighborhood of the free variables shows that every ﬁrstorder deﬁnable subset of (G ∪ Gˆ)p is indeed measurable (we extend µ to G ∪ Gˆ in the obvious way, considering Gˆ as zero measure).

The cleaning lemma sometimes applies in a non-trivial way:

Example 1. Consider the graph Gn obtained from a De Bruijn sequence (see e.g. [17]) of length 2n as shown Fig 2.

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

Figure 2: The graph Gn is constructed from a De Bruijn sequence of length 2n.

It is easy to deﬁne a graphing G, which is the limit of the sequence (Gn)n∈N: as vertex set, we consider the rectangle [0;1) × [0;3). We deﬁne a measure preserving function f and two measure preserving involutions T1,T2 as follows:

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
- (x,y + 2) if 1/2 ≤ x and y < 1




- (x,y − 1) if x < 1/2 and 2 ≤ y
- (x,y − 2) if 1/2 ≤ x and 2 ≤ y (x,y) otherwise




Then the edges of G are the pairs {(x,y),(x ,y )} such that (x,y) = (x ,y ) and either (x ,y ) = f(x,y), or (x,y) = f(x ,y ), or (x ,y ) = T1(x,y), or (x ,y ) = T2(x,y).

If one considers a random root (x,y) in G, then the connected component of (x,y) will almost surely be a rooted line with some decoration, as expected from what is seen from a random root in a suﬃciently large Gn. However, special behaviour may happen when x and y are rational. Namely, it is possible that the connected component of (x,y) becomes ﬁnite. For instance, if x = 1/(2n − 1)

and y = 2n−1x then the orbit of (x,y) under the action of f has length n thus the connected component of (x,y) in G has order 3n. Of course, such ﬁnite connected components do not appear in Gn. Hence, in order to clean G, inﬁnitely many components have to be removed.

### 6 Conclusion and Further Works

In a forthcoming paper [22], we apply the theory developed here to the context of classes of graphs with bounded diameter connected components, and in particular to classes with bounded tree-depth [19]. Speciﬁcally, we prove that if a uniform bound is ﬁxed on the diameter of the connected components, FOconvergence may be considered component-wise (up to some residue for which FO1-convergence is suﬃcient).

The prototype of convenient limit objects for sequences of ﬁnite graphs is a quadruple G = (V,E,Σ,µ), where (V,E) is a graph, (V,Σ,µ) is a standard probability space, and E is a measurable subset of V 2. In such a context, modulo the axiom of projective determinacy (which would follow from the existence of inﬁnitely many Woodin cardinals [16]), every ﬁrst-order deﬁnable subset of V p is measurable in (V p,Σ⊗p) [18]. Then, for every ﬁrst-order formula φ with p free variables, it is natural to deﬁne

ψ,G =

1φ dµ⊗p.

V p

In this setting, G = (V,E,Σ,µ) is a limit — we don’t pretend to have uniqueness — of an FO-convergent sequence (Gn)n∈N of ﬁnite graphs if for every ﬁrst-order formula ψ it holds

ψ,G = lim

ψ,Gn .

n→∞

We obtain in [22] an explicit construction of such limits for FO-convergent sequences of ﬁnite graphs bound to a class of graphs with bounded tree-depth. It is also there where we develop in a greater detail the general theory explained in the Sections 2 and 3. Notice that in some special cases, one does not need a standard probability space and a Borel measurable space is suﬃcient. This is for instance the case when we consider limits of ﬁnite connected graphs with bounded degrees (as we can use a quantiﬁer elimination scheme to prove that deﬁnable sets are measurable) or quantiﬁer-free convergence of graphs (deﬁnable sets form indeed a sub-algebra of the σ-algebra).

### Acknowledgments

The authors would like to thanks the referee for his most valuable comments.

### References

- [1] Adams, S.: Trees and amenable equivalence relations. Ergodic Theory Dynam. Systems 10, 1–14 (1990)
- [2] Aldous, D., Lyons, R.: Processes on unimodular random networks. arXiv:math/0603062 (2006)


- [3] Benjamini, I., Schramm, O.: Recurrence of distibutional limits of ﬁnite planar graphs. Electron. J. Probab. 6(23), 13pp (2001)
- [4] Borgs, C., Chayes, J., Lov´sz, L., S´s, V., Szegedy, B., Vesztergombi, K.: Graph limits and parameter testing. In: Proc. 38th Annual ACM Symp. Principles of Dist. Comp., pp. 51–59 (2005)
- [5] Conley, C., Kechris, A., Tucker-Drob, R.: Ultraproducts of measure preserving actions and graph combinatorics. Ergodic Theory and Dynamical Systems (2012). DOI 10.1017/S0143385711001143
- [6] Elek, G.: Note on limits of ﬁnite graphs. Combinatorica 27, 503–507

(2007). DOI 10.1007/s00493-007-2214-8

- [7] Elek, G., Szegedy, B.: Limits of hypergraphs, removal and regularity lemmas. A non-standard approach. arXiv:0705.2179v1 [math.CO] (2007)
- [8] Gaboriau, D.: Invariant percolation and harmonic Dirichlet functions. Geometric And Functional Analysis 15, 1004–1051 (2005). DOI 10.1007/ s00039-005-0539-2
- [9] Gaifman, H.: On local and non-local properties. In: Proceedings of the Herbrand Symposium, Logic Colloquium ’81 (1982)
- [10] Halmos, P., Givant, S.: Logic as Algebra, Dolciani Mathematical Expositions, vol. 21. The Mathematical Association of America (1998)
- [11] Hanf, W.: Model-theoretic methods in the study of elementary logic. In: J.A. et al. (ed.) The theory of models, pp. 132–145. North-Holland (1965)
- [12] Hodges, W.: A Shorter Model Theory. Cambridge University Press (1997)
- [13] Lascar, D.: La th´eorie des mod`eles en peu de maux. Cassini (2009)
- [14]  Lo´s, J.: Quelques remarques, th´eor`emes et proble`mes sur les classes d´eﬁnissables d’alg`ebres. In: Mathematical interpretation of formal systems, Studies in logic and the foundations of mathematics. North-Holland

(1955)

- [15] Lov´sz, L., Szegedy, B.: Limits of dense graph sequences. J. Combin. Theory Ser. B 96, 933–957 (2006)
- [16] Martin, D., Steel, J.: A proof of projective determinacy. Journal of the American Mathematical Society 2(1), 71–125 (1989)
- [17] Matouˇsek, J., Neˇsetrˇil, J.: Invitation to discrete mathematics. Oxford University Press (1998 (second printing 2008))
- [18] Mycielski, J., Swierczkowski,´ S.: On the Lebesgue measurability and the axiom of determinateness. Fund. Math. 54, 67–71 (1964)
- [19] Neˇsetrˇil, J., Ossona de Mendez, P.: Tree depth, subgraph coloring and homomorphism bounds. European Journal of Combinatorics 27(6), 1022– 1041 (2006). DOI 10.1016/j.ejc.2005.01.010


- [20] Neˇsetrˇil, J., Ossona de Mendez, P.: From sparse graphs to nowhere dense structures: Decompositions, independence, dualities and limits. In: European Congress of Mathematics, pp. 135–165. European Mathematical Society (2010). DOI 10.4171/077-1/7
- [21] Neˇsetrˇil, J., Ossona de Mendez, P.: Sparsity (Graphs, Structures, and Algorithms), Algorithms and Combinatorics, vol. 28. Springer (2012). 465 pages
- [22] Neˇsetrˇil, J., Ossona de Mendez, P.: Graph limits: a uniﬁed approach with application to the study of limits of graphs with bounded diameter components. (2012). Manuscript
- [23] Rudin, W.: Functional Analysis. Mc-Graw Hill (1973)
- [24] Stone, M.: The theory of representations of Boolean algebras. Transactions of the American Mathematical Society 40, 37–111 (1936)


