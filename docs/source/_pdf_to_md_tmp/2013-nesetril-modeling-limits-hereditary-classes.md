# arXiv:1312.0441v1[math.CO]2Dec2013

## MODELING LIMITS IN HEREDITARY CLASSES: REDUCTION AND APPLICATION TO TREES

JAROSLAV NESETˇ RILˇ AND PATRICE OSSONA DE MENDEZ

Abstract. Limits of graphs were initiated recently in the two extreme contexts of dense and bounded degree graphs. This led to elegant limiting structures called graphons and graphings. These approach have been uniﬁed and generalized by authors in a more general setting using a combination of analytic tools and model theory to FO-limits (and X-limits) and to the notion of modeling. The existence of modeling limits was established for sequences in a bounded degree class and, in addition, to the case of classes of trees with bounded height and of graphs with bounded tree depth. These seemingly very special classes is in fact a key step in the development of limits for more general situations. The natural obstacle for the existence of modeling limit for a monotone class of graphs is the nowhere dense property and it has been conjectured that this is a suﬃcient condition. Extending earlier results we derive several general results which present a realistic approach to this conjecture. As an example we then prove that the class of all ﬁnite trees admits modeling limits.

1. Introduction

The study of limiting properties of large graphs have recently received a great attention, mainly in two directions: limits of graphs with bounded degrees [1] and limit of dense graphs [11]. These developments are nicely documented in the recent monograph of Lov´sz [10]. Motivated by a possible unifying scheme for the study of structural limits, we introduced the notion of Stone pairing and FO-convergence [16, 18]. Precisely, we proposed an approach based on the Stone pairing φ,G of a ﬁrst-order formula φ (with set of free variables Fv(φ)) and a graph G, which is deﬁned by following expression

φ,G = |{(v1,...,v|Fv(φ)|) ∈ G|Fv(φ)| : G |= φ(v1,...,v|Fv(φ)|)}| |G||Fv(φ)|

.

Date: October 23, 2021. 2010 Mathematics Subject Classiﬁcation. Primary 03C13 (Finite structures), 03C98 (Appli-

cations of model theory), 05C99 (Graph theory), 06E15 (Stone spaces and related structures), Secondary 28C05 (Integration theory via linear functionals).

Key words and phrases. Graph and Relational structure and Graph limits and Structural limits and Radon measures and Stone space and Model theory and First-order logic and Measurable graph.

Supported by grant ERCCZ LL-1201 and CE-ITI P202/12/G061, and by the European Associated Laboratory “Structures in Combinatorics” (LEA STRUCO).

Supported by grant ERCCZ LL-1201 and by the European Associated Laboratory “Structures in Combinatorics” (LEA STRUCO).

1

In other words, φ,G is the probability that φ is satisﬁed in G by a random assignment of vertices (chosen independently and uniformly in the vertex set of G) to the free variables of G.

Stone pairing induces a notion of convergence: a sequence of graphs (Gn)n∈N is FO-convergent if, for every ﬁrst order formula φ (in the language of graphs), the values φ,Gn converge as n → ∞. In other words, (Gn)n∈N is FO-convergent if the probability that a formula φ is satisﬁed by the graph Gn with a random assignment of vertices of Gn to the free variables of φ converges as n grows to inﬁnity.

It is sometimes interesting to consider weaker notions of convergence, by restricting the set of considered formulas to a fragment X of FO. In this case, we speak about X-convergence instead of FO-convergence. Of special importance are the following fragments:

|Fragment|Type of formulas|Type of convergence|
|---|---|---|


|QF|quantiﬁer free formulas<br><br>|left convergence [11]|
|---|---|---|
|FO0|sentences (no free variables)<br><br>|elementary convergence|
|FOp<br><br>|formulas with free variables in {x1,...,xp}| |
|FOlocal<br><br>|local formulas (depending on a ﬁxed distance neighborhood of the free variables)| |
|FOlocal1<br><br>|local formulas with single free variable<br><br>|local convergence (if bounded degree) [1]|


Table 1. Fragments of speciﬁc importance.

Note that the above notions clearly extend to relational structures. Precisely, if we consider relational structures with signature λ, the symbols of the relations and constants in λ deﬁne the non-logical symbols of the vocabulary of the ﬁrst-order language FO(λ) associated to λ-structures. Notice that if λ is at most countable then FO(λ) is countable. We have shown in [16, 18] that every ﬁnite relational structure A with (at most countable) signature λ deﬁnes (injectively) a probability measure µA on the standard Borel space S(B(FO(λ))), which is the Stone space of the Lindenbaum-Tarski algebra of ﬁrst-order formulas (modulo logical equivalence) in the language of λ-relational structures. In this setting, a sequence (An)n∈N of λ-structures is FO-convergent if and only if the sequence (µA

)n∈N of measures converge (in the sense of a weak-* convergence), and that the uniquely determined limit probability measure µ is such that for every ﬁrst-order formula φ it holds

n

lim

φ,An =

1K(φ)(T)dµ(T),

n→∞

S(B(FO(λ)))

where 1K(φ) stands for the indicator function of the set K(φ) of the T ∈ S(B(FO(λ))) such that φ ∈ T. Note that the space of probability measures on the Stone space of a countable Boolean algebra, equipped with the weak topology, is compact.

It is natural to search for a limit object that would more look like a relational structure. Thus we introduced in [18] — as candidate for a possible limit object of

sparse structures — the notion of modeling, which extends the notion of graphing introduced for bounded degree graphs. Here is an outline of its deﬁnition. A relational sample space is a relational structure A (with signature λ) with additional structure: The domain A of A of a relation sample space is a standard Borel space (with Borel σ-algebra ΣA) with the property that every subset of Ap that is ﬁrst-order deﬁnable in FO(λ) is measurable (in Ap with respect to the product σ-algebra). A modeling is a relational sample space equiped with a probability measure (denoted νA). For brevity we shall use the same letter A for structure, relational sample space, and modeling. The deﬁnition of modelings allows us to extend Stone pairing naturally to modelings: the Stone pairing φ,A of a ﬁrstorder formula φ (with free variables in {x1,...,xp}) and a modeling A, is deﬁned by

φ,A = ··· 1Ω

φ(A)(x1,...,xp)dνA(x1)...dνA(xp), where 1Ω

φ(A) is the indicator function of the solution set Ωφ(A) of φ in A, that is: Ωφ(A) = {(v1,...,vp) ∈ Ap : A |= φ(v1,...,vp).

Note that every ﬁnite structure canonically deﬁnes a modeling (with same universe, discrete σ-algebra, and uniform probability measure) and that in the deﬁnition above matches the deﬁnition of Stone pairing of a formula and a ﬁnite structure introduced earlier.

In the following, we assume that free variables of formulas are of the form xi with i ∈ N. Note that the free variables need not to be indexed by consecutive integers. For a formula φ, denote by φ the formula obtained by packing the free variables of φ: if the free variables of φ are xi

### with i1 < i2 < ··· < ip then φ is obtained from φ by renaming xi

### ,...,xi

1

p

to x1,...,xp. Although Ωφ(A) and Ωφ (A) diﬀer in general, it is clear that they have same measure (as Ωφ(A) can be obtained from Ωφ (A) by taking the Cartesian product by some power of A, and then permuting the coordinates). Hence for every formula φ it holds

### ,...,xi

1

p

φ, ·  = φ , · , that is: the Stone pairing is invariant by renaming of the free variables.

The expressive power of the Stone pairing goes slightly beyond satisfaction statistics of ﬁrst-order formulas. In particular, we prove (see Corollary 1) that the Stone pairing  ·,A can be extended in a unique way to the inﬁnitary language Lω1ω, which is an extension of FO allowing countable conjunctions and disjunctions [20, 21]. Note that this language is still complete, as proved by Karp [5]. Although the compactness theorem does not hold for Lω1,ω, the interpolation theorem for Lω1,ω was proved by Lopez-Escobar [9] and Scott’s isomorphism theorem for Lω1,ω by Scott [19]. For a modeling A and an integer p, the Lω1,ω-deﬁnable subsets of Ap correspond to the smallest σ-algebra that contains all the ﬁrst-order deﬁnable subsets of Ap (see Lemma 7). According to the deﬁnition of a modeling, this means that all Lω1,ω-deﬁnable sets of a modeling are Borel measurable.

We say that a class C of structures admits modeling limits if for every FOconvergent sequence of structures An ∈ C there is a modeling L such that for every φ ∈ FO it holds

φ,L = lim

φ,An ,

n→∞

what we denote by An −−→FO L. More generally, for a fragment X of FO, we say that a class C of structures admits modeling X-limits if for every X-convergent sequence of structures An ∈ C there is a modeling L such that for every φ ∈ X it holds

φ,L = limn→∞ φ,An , and we denote this by An −→X L. The following results have been proved in [18]:

- • every class of graphs with bounded degree admits modeling limits;
- • every class of graphs of colored rooted trees bounded height admits modeling limits;
- • every class of graphs with bounded tree-depth admits modeling limits.


On the other hand, only sparse monotone classes of graphs can admits modeling limits. Precisely, if a monotone class of graphs admits modeling limits, then it is nowhere dense [18], and we conjectured that a monotone class of graphs actually admits modeling limits if and only if it is nowhere dense.

Recall that a monotone class of graphs C is nowhere dense if, for every integer p there exists a graph whose p-subdivision is not in C (for more on nowhere dense graphs, see [13, 12, 14, 15, 17]). The importance of nowhere dense classes and the strong relationship of this notion with ﬁrst-order logic is exampliﬁed by the recent result of Grohe, Kreutzer, and Siebertz [4], which states that (under a reasonable complexity theoretic assumption) deciding ﬁrst-order properties of graphs in a monotone class C is ﬁxed-parameter tractable if and only if C is nowhere dense.

In this paper, we initiate a systematic study of hereditary classes that admit modeling limits. We prove that the problem of the existence of a modeling limit can be reduced to the study of FOlocal-convergence, and then to two “typical” particular cases:

- • Residual sequences, that is sequences such that (intuitively) the limit has only zero-measure connected components,
- • Non-dispersive sequences, that is sequences such that (intuitively) the limit is (almost) connected.


A modeling A with universe A satisﬁes the Finitary Mass Transport Principle if, for every φ,ψ ∈ FO1(λ) and every integers a,b such that

φ (∃≥ay)(x1 ∼ y) ∧ ψ(y) ψ (∃≤by)(x1 ∼ y) ∧ φ(y)

it holds

a φ,A ≤ b ψ,A .

It is clear that every ﬁnite structure satisﬁes the Finitary Mass Transport Principle, hence every modeling FO-limit of ﬁnite structures satisﬁes the Finitary Mass Transport Principle, too.

A stronger version of this principle, which is also satisﬁed by every ﬁnite structure, does not automatically hold in the limit. A modeling A with universe A satisﬁes the Strong Finitary Mass Transport Principle if, for every measurable subsets X,Y of A, and every integers a,b, the following property holds:

If every x ∈ X has at least a neighbors in Y and every y ∈ Y has at most b neighbors in X then aνA(X) ≤ bνA(Y ).

In this context, we prove the following theorem, which is the principal result of this paper.

- Theorem 1. Let C be a hereditary class of structures.

Assume that for every An ∈ C and every ρn ∈ An (n ∈ N) the following properties hold:

- (1) if (An)n∈N is FOlocal1 -convergent and residual, then it has a modeling FOlocal1 limit;
- (2) if (An,ρn)n∈N is FOlocal-convergent (resp. FOlocalp -convergent) and ρ-nondispersive then it has a modeling FOlocal-limit (resp. a FOlocalp -limit).


Then C admits modeling limits (resp. modeling FOp-limits). Moreover, if in cases (1) and (2) the modeling limits satisfy the Strong Finitary

Mass Transport Principle, then C admits modeling limits (resp. modeling FOplimits) that satisfy the Strong Finitary Mass Transport Principle.

Then we apply this theorem in Section 8 to give a simple proof of the fact that the class of forests admit modeling limits.

- Theorem 2. The class of ﬁnite forests admits modeling limits, that is: every FOconvergent sequence of ﬁnite forests as a modeling FO-limit that satisﬁes the Strong Finitary Mass Transport Principle.

Note that a result similar to Theorem 2 was recently claimed by Kr´l’, Kupec, and Tu˚ma [7].

2. Preliminaries

Let A be a relational structure with signature λ and universe A, and let X ⊆ A. The substructure A[X] induced by X has domain X and the same relations as A (restricted to X). A class C of λ-structures is hereditary if every induced substructure of a structure in C belongs to C: (∀A ∈ C,∀X ⊂ A) A[X] ∈ C.

The distance between two vertices u,v ∈ A is the smallest number of relations inducing a connected substructure of A and containing both u and v, that is the graph distance between u and v in the Gaifman graph of A. For r ∈ N and v ∈ A, we denote by Br(A,v) the ball of radius r centered at v, that is the substructure of A induced by the vertices at distance at most r from v in A. More generally, for v1,...,vk ∈ A, we denote by Br(A,v1,...,vk) the substructure of A induced by the vertices at distance at most r from at least one of the vi (1 ≤ i ≤ k) in A.

A formula φ ∈ FOlocalp is r-local if its satisfaction only depends on the rneighborhood of the free variables, that is: for every λ-structure A and every v1,...,vp ∈ Ap it holds

A |= φ(v1,...,vp) ⇐⇒ Br(A,v1,...,vp) |= φ(v1,...,vp).

Recall the particular case of Gaifman locality theorem for sentences, which we will be usefull in the following. A local sentence is a sentence of the form

∃x1 ...∃xk

1≤i<j≤k

dist(xi,xj) > 2r ∧

1≤i≤k

ψi(xi) ,

where r,k ≥ 1 and ψi is r-local.

- Theorem 3 (Gaifman [3]). Every ﬁrst-order sentence is equivalent to a Boolean combination of local sentences.


We end this section with two very simple but usefull lemmas.

- Lemma 4. Let φ,ψ be formulas. Then it holds | φ, ·  − φ ∧ ψ, · | ≤ 1 − ψ, · .

Proof.

ψ ∧ φ, ·  ≤ φ, ·  =  ¬ψ ∧ φ, ·  + ψ ∧ φ, ·  ≤  ¬ψ, ·  + ψ ∧ φ, · , Thus

| φ, ·  − φ ∧ ψ, · | ≤  ¬ψ, ·  = 1 − ψ, · .

- Lemma 5. Let ψ1,...,ψp be formulas without common free variables. Then it

holds

p

i=1

ψi, ·  =

p

i=1

ψi, · .

Proof. Let k = max{i : xi ∈ pj=1 Fv(ψj)}− pj=1 |Fv(ψj)|. For every modeling A, the solution set Ω p

i=1 ψi(xi)(A) can be obtained from Ωψ

1

(A)×···×Ωψ

p

(A)×Ak by permuting the coordinates, hence both sets have the same measure, that is:

p

i=1

ψi, ·  =

p

i=1

ψ i , ·  =

p

i=1

ψi, · .

3. What does Stone pairing measure?

By deﬁnition, the Stone pairing φ,A measures the probability that a given ﬁrst-order formula φ is satisﬁed in A by a random assignment of vertices of A to the free variables. For this deﬁnition to make sense, we have to assume that every subset of a power of A that is ﬁrst-order deﬁnable without parameters is measurable. Hence we have to consider, for each p ∈ N, a σ-algebra on Ap that contains all subsets of Ap that are ﬁrst-order deﬁnable without parameters.

The aim of this section is to prove that the minimal σ-algebra including all subsets of Ap that are ﬁrst-order deﬁnable without parameters is exactly the family of all subsets of Ap that are Lω1ω-deﬁnable without parameters.

We take time out for two lemmas.

- Lemma 6. Let Ω be a set. For p ∈ N, let Ap be a ﬁeld of sets on Ωp, and let σ(Ap) be the minimal σ-algebra that contains Ap. For p ∈ N, let fp : Ωp+1 → Ωp and let Fp : P(Ωp+1) → P(Ωp) be deﬁned by Fp(X) = {fp(x) : x ∈ X}.


Assume that for each p ∈ N, Fp maps Ap+1 to Ap. Then Fp maps σ(Ap+1) to σ(Ap).

Proof. The proof follows the standard construction of a σ-algebra by transﬁnite induction. For p ∈ N, we let

- • Sp,0 be the collection of sets obtained as countable unions of increasing sets

in Ap, that is: sets of the form i∈N Xi where Xi ∈ Ap and X1 ⊆ X2 ⊆ ··· ⊆ Xn ⊆ ...;

- • Pp,0 be the collection of sets obtained as countable intersections of de-


creasing sets in Ap, that is: sets of the form i∈N Xi where Xi ∈ Ap and X1 ⊇ X2 ⊇ ··· ⊇ Xn ⊇ ...;

- • (for i ≥ 1 not a limit ordinal) Sp,i be the collection of sets obtained as countable unions of increasing sets in Pp,i−1;
- • (for i ≥ 1 not a limit ordinal) Pp,i be the collection of sets obtained as countable intersections of decreasing sets in Sp,i−1;
- • (for i limit ordinal) Sp,i = j<i Sp,j and Pp,i = j<i Pp,j.


Then it is easily checked that by induction that for every i up to ω1 it holds:

- • for all X ∈ Ωp, (X ∈ Sp,i) ⇐⇒ (Ωp \ X ∈ Pp,i);
- • for every limit ordinal i, Sp,i = Pp,i;
- • if X,Y ∈ Sp,i then X ∪ Y ∈ Sp,i and X ∩ Y ∈ Sp,i;
- • if X,Y ∈ Pp,i then X ∪ Y ∈ Pp,i and X ∩ Y ∈ Pp,i;
- • Fp maps Sp+1,i to Sp,i and Pp+1,i to Pp,i;


According to the monotone class theorem, σ(Ap) = Sp,ω1

= Pp,ω1

.

- Lemma 7. We consider a relational structure A with countable signature.


Let Ap (resp. A+p ) be the ﬁeld of sets of all the subsets of Ap that are ﬁrst-order deﬁnable without (resp. with) parameters. Then the smallest σ-algebra σ(Ap) ⊇ Ap (resp. σ(A+p ) ⊇ A+p ) is the algebra of all the subsets of Ap that are deﬁnable in Lω1ω without (resp. with) parameters.

Proof. Let Ω = L and fp : Ap+1 → Ap be the projection map. According to Lemma 6, the projection map send sets in σ(Ap+1) to sets in σ(Ap) (and sets in σ(A+p+1) to sets in σ(A+p )). It follows easily that subsets of Ap that are Lω1ωdeﬁnable without (resp. with) parameters are exactly those in σ(Ap) (resp. σ(A+p )).

Note that when A is a modeling, the collection of the subsets of Ap deﬁnable in Lω1ω without parameters is the σ-algebra generated by the projection pTp

: Ap → S(B(FOp)), mapping a p-tuple of vertices of A to its p-type: a subset X of Ap is deﬁnable in Lω1ω without parameters if and only if it is the preimage by pTp

A

of a Borel subset of S(B(FOp)) (see [18] for detailed deﬁnition and analysis of pTp

A

).

A

- Corollary 1. For every modeling A the Stone pairing  ·,A can be extended in a unique way to Lω1ω. Remark 8. Let Ξ(λ) be the set of all probability measures on the Stone space S(B(FO(λ))), and let B be the σ-algebra generated by evaluation maps µ  → µ(A) for A measurable set of S(B(FO(λ))). It is well known that (Ξ(λ),B) is a standard Borel space ([6], Sect. 17.E). (Hence the space of all ﬁnite λ-structures and their FO-limits is also a compact standard Borel space, as it can be identiﬁed to a closed


subspace of Ξ(λ).) The mapping A  → νA embeds the space M of modelings into Ξ(λ). The initial topology on M with respect to this mapping is the same as the topology induced by Stone pairing. Hence the mapping φ, ·  : M → [0,1], which maps A to φ,A , is continuous for φ ∈ FO(λ), and measurable for φ ∈ Lω1ω(λ).

Also remark that the topology of Ξ(λ) can be deﬁned by means of Le´vy–Prokhorov metric (by choosing some metric on the Stone space). For instance, for ﬁnite signature λ, the topology of M can be generated by the pseudometric:

−n}.

dist(A,B) = 2−sup{n| ∀φ∈FO(λ),qrank(φ)+|Fv(φ)|≤n⇒| φ,A − φ,B |<2

Theorem 9. Let A be a relational sample space. Then every subset of Ap that is Lω1ω-deﬁnable (with parameters) is measurable (with respect to product Borel σ-algebra Σ⊗Ap).

3.1. Interpretation Schemes. Interpretation Schemes (introduced in this setting in [18]) generalize to other logics than FO.

- Deﬁnition 10. Let L be a logic (for us, FO or Lω1ω). For p ∈ N and a signature λ, Lp(λ) denotes the set of the formulas in the language of λ in logic L, with free variables in {x1,...,xp}.

Let κ,λ be signatures, where λ has q relational symbols R1,...,Rq with respective arities r1,...,rq.

An L-interpretation scheme I of λ-structures in κ-structures is deﬁned by an integer k — the exponent of the L-interpretation scheme — a formula E ∈ L2k(κ), a formula θ0 ∈ Lk(κ), and a formula θi ∈ FOr

ik(κ) for each symbol Ri ∈ λ, such that:

- • the formula E deﬁnes an equivalence relation of k-tuples;
- • each formula θi is compatible with E, in the sense that for every 0 ≤ i ≤ q it holds


1≤j≤ri

E(xj,yj) θi(x1,...,xr

i

) ↔ θi(y1,...,yr

i

),

where r0 = 1, boldface xj and yj represent k-tuples of free variables, and where θi(x1,...,xr

i

) stands for θi(x1,1,...,x1,k,...,xr

i,1,...,xr

i,k). For a κ-structure A, we denote by I(A) the λ-structure B deﬁned as follows:

- • the domain B of B is the subset of the E-equivalence classes [x] ⊆ Ak of the tuples x = (x1,...,xk) such that A |= θ0(x);
- • for each 1 ≤ i ≤ q and every v1,...,vs


i ∈ Akr

i

such that A |= θ0(vj) (for every 1 ≤ j ≤ ri) it holds

B |= Ri([v1],...,[vr

i

]) ⇐⇒ A |= θi(v1,...,vr

i

).

From the standard properties of model theoretical interpretations (see, for instance [8] p. 180), we state the following: if I is an L-interpretation of λ-structures in κ-structures, then there exists a mapping ˜I : L(λ) → L(κ) (deﬁned by means of the formulas E,θ0,...,θq above) such that for every φ ∈ Lp(λ), and every κstructure A, the following property holds (while letting B = I(A) and identifying elements of B with the corresponding equivalence classes of Ak):

For every [v1],...,[vp] ∈ Bp (where vi = (vi,1,...,vi,k) ∈ Ak) it holds

B |= φ([v1],...,[vp]) ⇐⇒ A |=˜I(φ)(v1,...,vp). It directly follows from the existence of the mapping ˜I that

- • an FO-interpretation scheme I of λ-structures in κ-structures deﬁnes a continuous mapping from S(B(FO(κ))) to S(B(FO(λ)));
- • an Lω1ω-interpretation scheme I of λ-structures in κ-structures deﬁnes a measurable mapping from S(B(FO(κ))) to S(B(FO(λ))).


- Deﬁnition 11. Let κ,λ be signatures. A basic L-interpretation scheme I of λ-


structures in κ-structures with exponent k is deﬁned by a formula θi ∈ Lkri

(κ) for each symbol Ri ∈ λ with arity ri.

For a κ-structure A, we denote by I(A) the structure with domain Ak such that, for every Ri ∈ λ with arity ri and every v1,...,vr

i ∈ Ak it holds I(A) |= Ri(v1,...,vr

### ) ⇐⇒ A |= θi(v1,...,vr

### ).

i

i

It is immediate that every basic L-interpretation scheme I deﬁnes a mapping ˜I : L(λ) → L(κ) such that for every κ-structure A, every φ ∈ Lp(λ), and every v1,...,vp ∈ Ak it holds

I(A) |= φ(v1,...,vp) ⇐⇒ A |=˜I(φ)(v1,...,vp) We deduce the following general properties:

- Lemma 12 ([18]). Let I be an FO-interpretation scheme of λ-structures in κstructures.

Then, if a sequence (An)n∈N of ﬁnite κ-structures is FO-convergent then the sequence (I(An))n∈N of (ﬁnite) λ-structures is FO-convergent.

- Lemma 13. Let I be an Lω1ω-interpretation scheme of λ-structures in κ-structures. If I is injective and A is a relational sample space, then I(A) is a relational

sample space.

Furthermore, if I is a basic Lω1ω-interpretation scheme and A is a modeling, then I(A) is a modeling and for every φ ∈ Lp(λ), it holds

φ,I(A) = ˜I(φ),A .

Proof. Assume I is an injective Lω1ω-interpretation scheme and A is a relational sample space.

We ﬁrst mark all the (ﬁnitely many) parameters and reduce to the case where the interpretation has no parameters (as in the case of FO-interpretation, see [18]. Let D be the domain of f. As B is L-deﬁnable in B, D is L-deﬁnable in A hence D ∈ ΣkA. Then D is a Borel sub-space of Ak. As f is a bijection from D to B, we deduce that (B,ΣB) is a standard Borel space. Moreover, as the inverse image of every L-deﬁnable set of B is L-deﬁnable in A, we deduce that (B,ΣB) is a λ-relational sample space.

Assume I is a basic Lω1ω-interpretation scheme and A is a modeling. The pushforward of νA by I deﬁnes a probability measure on I(A) such that for every φ ∈ Lp(λ), it holds

φ,I(A) = I∗(νA)(Ωφ(I(A))) = νA(Ω˜I(φ)(A)) = ˜I(φ),A .

4. Residual Sequences

Every modeling can be decomposed into countably many connected components with non-zero measure and an union of connected components with (individual) zero measure. A residual modeling is a modeling, all components of which have zero measure.

- Lemma 14. A modeling A is residual if it holds


∀r ∈ N, sup

νL(Br(A,v)) = 0.

v∈A

Proof. Assume that for every r ∈ N it holds supv∈L νL(Br(A,v)) = 0. For u ∈ A, the connected component Cu of u is Cu = r∈N Br(A,u). As all these balls are ﬁrst-order deﬁnable (hence measurable) we deduce

νA(Cu) = lim

νA(Br(A,u)) = 0.

r→∞

It follows that every connected component of L has zero-measure, hence A is residual.

Conversely, assume that there exists u ∈ A and r ∈ N such that νA(Br(A,u)) >

- 0. Then the connected component of u does not have zero measure, hence A is not residual.


This equivalence justiﬁes the following notion of residual sequence.

Deﬁnition 15 (Residual sequence). A sequence (An)n∈N of modelings is residual if

∀r ∈ N, limsup

## νA

(Br(An,v)) = 0.

sup

n

n→∞

v∈An

- Lemma 16. Let φ ∈ FOlocalp be r-local, and deﬁne the formula


θr(x1,...,xp) :

dist(xi,xj) > r.

1≤i<j≤p

Then there exist r-local formulas ψ1,...,ψp ∈ FOlocal1 such that it holds | φ, ·  −

p

ψi, · | ≤ 2(1 − θr, · ). Proof. According to Lemma 4 it holds

i=1

| φ, ·  − φ ∧ θr, · | ≤ 1 − θr, · .

According to the r-locality of φ there exist r-local formulas ψ1,...,ψp ∈ FOlocal1 such that φ ∧ θr is logically equivalent to pi=1 ψi(xi) ∧ θr (where ψi(xi) denotes the formula ψi with free variable x1 renamed xi). Thus, according to Lemma 4, it holds

p

ψi(xi), ·  − φ ∧ θr, · | ≤ 1 − θr, · . As the formulas ψi(xi) use no common free variables, it holds (according to Lemma 5):

| 

i=1

p

p

ψi, · . Hence the result.

ψi(xi), ·  =

i=1

i=1

- Corollary 2. Let φ ∈ FOlocalp be r-local.


Then there exist r-local formulas ψ1,...,ψp ∈ FOlocal1 such that for every modeling A it holds

p

ψi,A | < p2 sup v∈A

| φ,A −

νA(Br(A,v)).

i=1

Proof. Let θr be deﬁned as in Lemma 16. By union bound, we get  ¬θr,A =

dist(xi,xj) ≤ r,A

1≤i<j≤p

p 2

≤

dist(x1,x2) ≤ r,A

p 2

=

sup

νA(Bd(A,v)),

v∈A

and the result follows from Lemma 16.

- Lemma 17. For a residual sequence, FOlocal-convergence is equivalent to FO1localconvergence.


Proof. Let (An)n∈N be a residual sequence. If (An)n∈N is FOlocal-convergent, it is FOlocal1 -convergent; Assume (An)n∈N is FOlocal1 -convergent, let φ ∈ FOlocalp be an r-local formula,

and let θr be the formula 1≤i<j≤p dist(xi,xj) > r. As C is residual, it holds

lim

θr,An = 1.

n→∞

According to Lemma 16, there exist r-local formulas ψ1,...,ψp ∈ FOlocal1 such that for every n ∈ N it holds

p

ψi,An | ≤ 2(1 − θr,An ). Hence

| φ,An −

i=1

p

p

ψi,An =

lim

ψi,An .

lim

φ,An = lim

n→∞

n→∞

n→∞

i=1

i=1

Hence for residual sequences, FOlocal1 -convergence implies FOlocal-convergence.

To every formula φ ∈ FOlocalp and integer r ∈ N we associate the formula Λr(φ) ∈ FOlocalp deﬁned as

p

(∃y1,...,yp)

(dist(xi,yi) ≤ r) ∧ φ(y1,...,yp).

i=1

Deﬁnition 18. A modeling A is clean if for every formula φ ∈ FOlocal1 it holds A |= (∃x) φ(x) ⇐⇒ lim

Λr(φ),L > 0. (Note that the right-hand side condition is equivalent to existence of d such that Λr(φ),A > 0.)

r→∞

- Lemma 19. Let A be a residual clean modeling and let φ ∈ FOlocal1 . If Ωφ(L) is not empty, then it is uncountable.


Proof. Assume Ωφ(A) is not empty. As A is clean, there exists r ∈ N such that Λr(φ),A > 0, that is: νA(ΩΛ

φ(A) Br(A,v). Assume for contradiction that Ωφ(A) is countable. Then

r(φ)(A)) > 0. Clearly ΩΛ

r(φ)(A) = v∈Ω

νA(ΩΛ

r(φ)(A)) =

νA(Br(A,v)).

v∈Ωφ(A)

As A is residual, for every v ∈ A it holds νA(Br(A,v)) = 0, what contradicts the assumption νA(ΩΛ

r(φ)(A)) > 0.

Let X be a fragment of FO. Two modeling A and A are X-equivalent if, for every φ ∈ X it holds φ,A = φ,A . We shall now show how any modeling can be transformed into a residual clean modeling, which is FOlocal1 -equivalent.

- Lemma 20. Let A be a modeling. Then there exists a residual modeling A that is FOlocal1 -equivalent to A.

Proof. Consider the modeling A with universe A = A×[0,1], measure νA = νA⊗λ (where λ is standard Borel measure of [0,1]) and relations deﬁned as follows: for every relation Ri of arity ri it holds

A |= Ri((v1,α1),...,(vr

i

,αr

i

)) ⇐⇒ A |= Ri(v1,...,vr

i

) and α1 = ··· = αr

i

. Then A is residual and for every φ ∈ FOlocal1 it holds

φ,A = νA (Ωφ(A )) = νA (Ωφ(A) × [0,1]) = νA(Ωφ(A)) = φ,A .

- Lemma 21. Let A be a residual modeling. Then there exists a residual clean modeling A obtained from A by removing a union of connected components with global νA-measure zero.

Proof. Let φ ∈ FOlocal1 be such that A |= (∃x)φ(x) and limr→∞ Λr(φ),A = 0. For v ∈ A, denote by Av the connected component of A that contains v, that is: Av = r∈N Br(A,v). Note that if A |= φ(v) and if u ∈ Av then A |= Λr(φ)(u) but

Λr(Λr(φ)),A = Λr(φ),A = 0.

Note that the assumption on φ rewrites as “Ωφ(A) = ∅ while for every v ∈ Ωφ(A) it holds νA(Av) = 0”.

Then νA

v∈Ωφ(A)

Av = νA

v∈Ωφ(A) r∈N

Br(A,v) = νA

r∈N v∈Ωφ(A)

Br(A,v)

= νA

r∈N

ΩΛ

r(φ)(A) =

r∈N

Λr(φ),A = 0.

Denote by F the set of all φ ∈ FOlocal1 such that

A |= (∃x)φ(x) and lim

r→∞

Λr(φ),A = 0, and let A be obtained by removing φ∈F v∈Ω

φ(A) Av from A. As for every φ ∈ F it holds νA v∈Ω

φ(A) Av = 0 and as F is countable, the modeling A diﬀers from A by a set of connected components of global measure 0. Moreover, it is clear that A is clean.

Recall that FO-convergence can be decomposed into elementary convergence and FOlocal-convergence:

- Lemma 22 ([16, 18]). A sequence (An)n∈N is FO-convergent if and only if it is both elementary convergent and FOlocal-convergent.

Consequently, a modeling L is a modeling FO-limit of a sequence (An)n∈N if and only if it is both an elementary limit and a modeling FOlocal-limit of it.

The interest of residual clean modelings stands in the following.

- Lemma 23. Let (Gn)n∈N be a residual FO-convergent sequence.


If L is a residual clean modeling FOlocal1 -limit of (Gn)n∈N and M is a countable elementary limit of (Gn)n∈N then L ∪ M is a modeling FO-limit of (Gn)n∈N.

Proof. According to Theorem 3, it is suﬃcient to check that if ψ1,...,ψn are r-local formulas with a single free variable and if we let

φ(x1,...,xn) :

then it holds

dist(xi,xj) > 2r ∧

1≤i<j≤n

n

ψi(xi)

i=1

L ∪ M |= (∃x1,...xn)φ(x1,...,xn) ⇐⇒ M |= (∃x1,...xn)φ(x1,...,xn). But (according to the locality assumptions) it is equivalent to check that for every r-local ψ1,...,ψn and associated φ it holds

L |= (∃x1,...xn)φ(x1,...,xn) ⇒ M |= (∃x1,...xn)φ(x1,...,xn).

But if L |= (∃x1,...xn)φ(x1,...,xn), then forall 1 ≤ i ≤ n it holds L |= (∃x)ψi(x) hence, as L is clean, it that there exists r0 ∈ N such that Λr

(ψi),L > 0 for every

0

- 1 ≤ i ≤ n. As L is residual, this implies Λr


(φ),L > 0. Thus there exits n0 such that for every n ≥ n0 it holds Λr

0

(φ),Gn > 0. In particular the elementary limit M of Gn satisﬁes (∃x1,...,xn)φ(x1,...,xn).

0

- Corollary 3. A residual FO-convergent sequence (Gn)n∈N admits a modeling FOlimit if and only if it admits a modeling FOlocal1 -limit.


In this context, the following conjecture is interesting. Conjecture 1. Every FO-convergent residual sequence admits a modeling FO-limit.

Note that, according to Lemmas 20, 21 and 23, Conjecture 1 is equivalent to the (seemingly weaker) conjecture that every FOlocal1 -convergent residual sequence admits a modeling FOlocal1 -limit.

5. Non-dispersive Sequences

The notion of residual sequences derives from the notion of residual modelings, that is: modelings without connected components with non-zero measure). Similarly the notion of non-dispersive sequences derives from the notion of connected modelings (modulo a zero-measure set).

Deﬁnition 24. A sequence (An)n∈N of modelings is non-dispersive if

∀ > 0∃d ∈ N, liminf

(Bd(An,v)) > 1 −  .

sup

## νA

n

n→∞

v∈An

In the case of rooted structures, we usually want a stronger statement that the structures remain concentrated around their roots: a sequence (An,ρn)n∈N of rooted modelings is ρ-non-dispersive if

∀ > 0∃d ∈ N, liminf

(Bd(An,ρn)) > 1 −  . Note that every ρ-non-dispersive sequence is obviously non-dispersive.

## νA

n

n→∞

Remark 25. Let (An)n∈N be a non-dispersive FOlocal-convergent sequence. If (An)n∈N has a modeling FOlocal-limit L, then L has a full measure connected component, which is also a modeling FOlocal-limit of (An)n∈N.

- Lemma 26. Let (An,ρn)n∈N be a ρ-non-dispersive FO1-convergent sequence, with

modeling FOlocal1 -limit (L,ρ) and a countable elementary limit (M, ).

Let M• and L• be the connected component of the root in M and L, respectively. Then M• and L• are elementarily equivalent.

Proof. As (An,ρn)n∈N is ρ-non-dispersive, L• has full measure. According to Theorem 3, it is suﬃcient to check that if ψ1,...,ψn are r-local formulas with a single free variable and if we let

φ(x1,...,xn) :

1≤i<j≤n

dist(xi,xj) > 2r ∧

n

i=1

ψi(xi)

then it holds M• |= ∃x1 ...∃xn φ(x1,...,xn) ⇐⇒ L• |= ∃x1 ...∃xn φ(x1,...,xn).

Assume L• |= ∃x1 ...∃xn φ(x1,...,xn). Let v1,...,vn ∈ L• be such that L• |= φ(v1,...,vn). As L• is a full measure connected component of L, there exists d ≥ max1≤i≤n dist(vi,ρ) such that νL(Bd(L,ρ)) ≥ 1/2. Let ζ ∈ FOlocal1 be the 2d-local formula

∃y1 ...∃yn

n

i=1

dist(x1,yi) ≤ 2d ∧ φ(y1,...,yn) .

Then obviously Ωζ(L) ⊇ Bd(L,ρ) hence ζ,L ≥ 1/2. As L is a modeling FOlocal1 limit of (An,ρn)n∈N, there exists n0 such that for every n ≥ n0 it holds ζ,An ≥ 1/4. In particular, for every n ≥ n0 it holds An |= ∃x1 ...∃xn φ(x1,...,xn) hence

- M• |= ∃x1 ...∃xn φ(x1,...,xn). Conversely, assume that M• |= ∃x1 ...∃xn φ(x1,...,xn). Let v1,...,vn ∈ M•


be such that M• |= φ(v1,...,vn), and let d = max1≤i≤n dist(vi, ). As (M•,ρn) is an elementary limit of (An,ρn)n∈N, there exists n0 such that for every n ≥ n0 it holds

An |= ∃x1 ...∃xn

n

i=1

dist(xi,ρn) ≤ d ∧ ψ(x1,...,xn) . As (An,ρn)n∈N is ρ-non-dispersive, there exists D ≥ d and n1 ≥ n0 such that for

- every n ≥ n0, it holds |BD(An,ρn)| ≥ |An|/2. Let ζ ∈ FOlocal1 be the 2D-local formula


∃y1 ...∃yn

n

i=1

dist(x1,yi) ≤ 2D ∧ φ(y1,...,yn) .

Then obviously Ωζ(An) ⊇ BD(An,ρn) hence ζ,An ≥ 1/2. As L is a modeling FOlocal1 -limit of (An,ρn)n∈N, it holds ζ,L ≥ 1/2 hence, as L• is full dimensional, all of Ωζ(L) but a subset with νL-measure zero is included in Ln•. Hence L• |= ∃x1 ...∃xn φ(x1,...,xn).

- Lemma 27. Let p ≥ 1 and let (An,ρn)n∈N be a ρ-non-dispersive FOp-convergent


sequence, with modeling FOlocalp -limit (L,ρ) and countable elementary limit (M, ).

Let M• and L• be the connected components of the root in M and L, respectively. Then L• ∪ (M \ M•) is a modeling FOp-limit of (An,ρn)n∈N.

Proof. According to Lemma 26, L• and M• are elementarily equivalent, so L• ∪ (M \M•) and M are elementarily equivalent. It follows that L• ∪(M \M•) is both an elementary limit of (An,ρn)n∈N and a modeling FOlocalp -limit of (An,ρn)n∈N (as

it diﬀers from L by a set of connected components with global measure zero) hence a modeling FOp-limit of (An,ρn)n∈N.

Problem 1. Let (An)n∈N be a non-dispersive FOlocal1 -convergent sequence with modeling FOlocal1 -limit L. Does there exist ρn ∈ An and ρ ∈ L such that (An,ρn)n∈N is a ρ-non-dispersive FOlocal1 -convergent sequence with modeling FOlocal1 -limit (L,ρ)?

Sometimes, ρ-non-dispersive sequences may be still quite diﬃcult to handle, and sequences with bounded diameter may be more tractable. It is thus natural to consider to what extent it could be possible to further reduce to the bounded diameter case. We give here a partial answer.

- Lemma 28. Let (An,ρn) be a ρ-non-dispersive FOlocalp -convergent sequence, and let (L,ρ) be a connected modeling.


Assume that for each d ∈ N, it holds that (Bd(L,ρ),ρ) is a modeling FOlocalp -limit of (Bd(An,ρn),ρn). Then (L,ρ) is a modeling FOlocalp -limit of (An,ρn).

Proof. Let φ ∈ FOlocalp be r-local and let > 0. As (An,ρn)n∈N is ρ-non-dispersive and as L is connected, there exist d,n0 ∈ N such that νL(Bd(L,ρ)) > 1 − and such that for every n ≥ n0 it holds |Bd(An,ρn)| > (1− )|An|. Let θ be the formula dist(x1,ρ) ≤ d − r, and let θ(p) be the formula pi=1 θd(xi). Note that

θ,Bd(An,ρn) = |Bd−r(An,ρn)| |Bd(An,ρn)|

|Bd−r(An,ρn)| |An|

≥

= θ,An .

According to Lemma 4 it holds

| φ,An − φ ∧ θ(p),An | ≤ 1 − θ,An p < p . and also

| φ,Bd(An,ρn) − φ ∧ θ(p),Bd(An,ρn) | ≤ 1 − θ,Bd(An,ρn) p < p .

According to the r-locality of φ, it holds φ ∧ θ(p),An = φ ∧ θ(p),Bd(An,ρn) , hence

| φ,An − φ,Bd(An,ρn) | < 2p . Similarly, it holds

| φ,L − φ,Bd(L,ρ) | < 2p .

By assumption, Bd(L,ρ) is a modeling FOlocalp -limit of (Bd(An,ρn))n∈N. Thus there exists n1 ≥ n0 such that | φ,Bd(L,ρ) − φ,Bd(An,ρn) | < p , hence for

- every n ≥ n1 it holds | φ,L − φ,An | < 5p .


Considering → 0, we deduce

φ,L = lim

φ,An .

n→∞

6. Breaking

The aim of this section is to prove that the study of FO-convergent sequences of structures in a hereditary class naturally reduces to the study of residual sequences and ρ-non-dispersive sequences in that class.

Advancing the main result of this section, Theorem 33, we state four technical lemmas.

- Lemma 29. Let 0 < ≤ 1 and let r ∈ N. Then, for every graph G there exists a subset A of vertices such that

- (1) for every a ∈ A, it holds |B2r(G,a)| ≥ |G|;
- (2) for every v ∈/ a∈A B2r(G,a), it holds |Br(G,v)| < |G|;
- (3) |A| ≤ 1/ .


Proof. Let A be a maximal subset of vertices of G such that

- • for every a ∈ A, it holds |Br(G,a)| ≥ |G| (Hence (1) holds);
- • for every distinct x,y ∈ A, it holds Br(G,x) ∩ Br(G,y) = ∅. Obviously, |A| ≤ 1/ , hence (3) holds. Moreover, by maximality of X, if v is any vertex such that |Br(G,v)| ≥ |G| then there exists a ∈ A such that Br


0

(G,a) ∩ Br

- 0


(G,v) = ∅, thus v ∈ B2r(G,a). Hence (2) holds.

- Lemma 30. Let > 0, let r ∈ N and let (Gn)n∈N be an FOlocal-convergent sequence. Then there exists integer q ≤ 1/ , integer D, and increasing function


- N : N → N and an FOlocal-convergent sequence (G+n)n∈N of q-rooted graphs, such that G+n is a q-rooting of GN(n) (with roots cn1,...,cnq ) and


- • limn→∞ distG+

n

(cni ,cnj ) = ∞ for every 1 ≤ i < j ≤ q;

- • BD(G+n,cni ) ∩ BD(G+n,cnj ) = ∅ for every 1 ≤ i < j ≤ q and every n ∈ N;
- • |BD(G+n,cni )| ≥ |G+n| for every 1 ≤ i ≤ q and every n ∈ N;
- • |Br(G+n,v)| < |G+n| for every v ∈/ qi=1 BD(G+n,cni ) and every n ∈ N.


Proof. Consider the signature obtained by adding K = 1/  unary symbols R1,...,RK. According to Lemma 29, there exists, for each Gn, vertices z1n,...,zkn

such that

n

- • for every 1 ≤ i ≤ kn, it holds |B2r(Gn,zin)| ≥ |Gn|;
- • for every v ∈/ ki=1n B2r(Gn,zin), it holds |Br(Gn,v)| < |Gn|;
- • kn ≤ K.


We mark vertex z1n,...,zkn

thus obtaining a structure An. By compactness, the sequence (An)n∈N has an FO-converging subsequence (AN

### by R1,...,Rk

n

n

1(n))n∈N. Moreover, as the number of roots of An converges (by elementary convergence), we can assume without loss of generality that the subsequence is such that all the structures AN

1(n) use exactly the marks R1,...,Rp (with p ≤ K). According to the elementary convergence of (AN

(ziN1(n),zjN1(n))

1(n))n∈N, the limit di,j = limn→∞ distA

N1(n)

exists for every 1 ≤ i < i ≤ p and this limit can be either an integer or ∞. Let I be a maximal subset of {1,...,p} such that di,j = ∞ for every distinct i,j ∈ I, and let q = |I|. Without loss of generality, we assume that I = {1,...,q}. Deﬁne

D = 2r + max{di,j|1 ≤ i < j ≤ p and di,j < ∞}. Then each ball B2r(AN

1(n),ziN1(n)) with q < i ≤ p is included in one of the balls BD(AN

1(n),zjN1(n)) with 1 ≤ j ≤ q. As di,j = ∞ for every 1 ≤ i < j ≤ q, there

(ziN1(n),zjN1(n)) > 2D. We let N(n) = N1(n + n0), cni = ziN(n), and G+n = AN(n).

### exists n0 such that for every n ≥ n0 it holds distA

N1(n)

Let 0 < ≤ 1, let r,D ∈ N, and let (G+n)n∈N be an FO-convergent sequence of q-rooted graphs (with roots cni ) such that

- • limn→∞ distG+

n

(cni ,cnj ) = ∞ for every 1 ≤ i < j ≤ q;

- • BD(G+n,cni ) ∩ BD(G+n,cnj ) = ∅ for every 1 ≤ i < j ≤ q and every n ∈ N;
- • |BD(G+n,cni )| ≥ |G+n| for every 1 ≤ i ≤ q and every n ∈ N;
- • |Br(G+n,v)| < |G+n| for every v ∈/ qi=1 BD(G+n,cni ) and every n ∈ N.


For 1 ≤ i ≤ q, we deﬁne the function fi : N → R+ by fi(d) = lim

|Bd(G+n,cni )| |G+n|

.

n→∞

and we let λi = limd→∞ fi(d). For 1 ≤ i ≤ q, we also deﬁne gi : N × (0,1) → N by

gi(d,x) = min n0 : (∀n ≥ n0) |Bd(G+n,cni )| |G+n|

− fi(d) < x . We further deﬁne the function h : N → N by

h(x) = min{d : fi(d) ≥ λi − x}, and the function w : N → N by

(cni ,cnj ) > 2d}.

w(d) = min{n0 : (∀n ≥ n0) (∀1 ≤ i < j ≤ q) distG+

n

- Lemma 31. For every > 0 and r ∈ N there exist d0,n0 ∈ N such that for every n ≥ n0 it holds

- • fi(d0 − r ) ≥ λi − ,
- • |Bd

0−r (G+n,cni ) − fi(d0 − r )| < |G+n|,

- • |Bd

0

(G+n,cni ) − fi(d0)| < |G+n|,

- • |Bd

0+r (G+n,cni ) − fi(d0 + r )| < |G+n|,

- • |Bd

0+r (G+n,cni ) \ Bd

0−r (G+n,cni )| < |G+n|,

- • the cni ’s are pairwise at distance strictly greater than 2d0 + 4r .


Proof. Choose d0 ≥ D + 2r and ≥ r + maxi hi( /3), n0 ≥ maxi max(gi(d0 − r,  /3),gi(d0,  /3),gi(d0 + r,  /3)) and n0 ≥ w(d0 − r). Note that the third condition then follows from

|Bd

0+r(G+n,cni ) \ Bd

0−r(G+n,cni )| |G+n|

≤

|Bd

0+r(G+n,cni ) |G+n|

− fi(d0 + r)

+ |Bd

0−r(G+n,cni ) |G+n|

− fi(d0 − r)

+ fi(d0 + r) − fi(d0 − r) and the obvious inequality fi(d0 + r) − fi(d0 − r) ≤ λi − fi(d0 − r).

- Lemma 32. For every > 0 and r ∈ N there exist d0,n0 ∈ N with the following


(G+n,cni ),cni ) and unrooted graph Rn = G+n \ i Hi,n, let G∗n = Rn ∪ i Hi,n, and let G n = Unmark(G∗n). Then for every n ≥ n0:

properties: Deﬁne rooted graphs Hi,n = (Bd

0

- • |Hi,n − λi|G+n|| < |G+n|,


- • |Bd

0

(Hi,n,cni )| > (1 − / )λi|G+n|,

- • for every vertex v ∈ Rn it holds λ0|Br(Rn,v)| < |G+n|,
- • for every r -local φ ∈ FOlocalp it holds | φ,Gn − φ,G n | < p  / .


Proof. Obviously, φ,Gn = φ,G+n and φ,G n = φ,G∗n . Let θ be the formula deﬁned as

dist(x1,ci) ≤ d0 − r ∨

dist(x1,ci) > d0 + r ,

i

i

and let θ(p) be the formula pi=1 θ(xi).

For every n ≥ n0, it holds θ(p),G+n = θ,G+n p > (1 − / )p hence 1 − θ(p),G+n < p  / . Thus

| φ,G+n − φ ∧ θ(p),G+n | ≤ 1 − θ(p),G+n < p  / . Also, θ(p),G∗n = θ,G∗n p > (1 − / )p hence 1 − θ(p),G∗n < p  / . Thus | φ,G∗n − φ ∧ θ(p),G∗n | ≤ 1 − θ(p),G∗n < p  / 

According to the r -locality of φ it holds φ ∧ θ(p),G+n = φ ∧ θ(p),G∗n . Hence | φ,Gn − φ,G n | < 2p  / .

Now for a ∈ N we let =  /a,r = a, Hˆi,a = Hi,n

0(a), Rˆa = Rn

0(a) and Gˆa = G n

0(a). Then it holds for every n ∈ N:

- • (Hˆi,n)n∈N is ρ-non-dispersive,
- • limn→∞ |Hˆi,n|/|Gˆn| = λi,
- • for every vertex v ∈ Rn it holds λ0|Br(Rˆn,v)| < |Gn|,
- • for every r-local φ ∈ FOlocalp and every n ≥ r it holds | φ,Gn  −  φ,Gˆn | < p/n thus (Gn)n∈N and (Gˆn)n∈N have the same FOlocal-limit.


Theorem 33. Let (Gn)n∈N be an FOlocalp -convergent sequence. Then there exist a ρ-non-dispersive FOlocalp -convergent sequences (Hˆi,n)n∈N of rooted graphs (i ∈ N), a residual FOlocalp -convergent sequence (Rˆn)n∈N, positive real numbers λi > 0, and an increasing function ϕ : N → N such that:

- (1) The sequences (Gn)n∈N and (Gˆn)n∈N have the same FOlocal-limit, where Gˆn = Rn ∪ i∈N Unmark(Hˆi,n).
- (2) If (Hˆi,n)n∈N has FOlocalp -modeling limit Li, (Rˆn)n∈N has FOlocal1 -modeling limit L0, λ0 = 1 − i∈N λi, and L = i≥0(Li,λi), then Unmark(L) is an FOlocalp -modeling limit of (Gn)n∈N.
- (3) Furthermore, if (Gn)n∈N is FOp-convergent, then it has a modeling FOplimit, which can be obtained by ﬁrst cleaning L0, computing L, taking the disjoint union with some countable graph, and then forgetting marks.


Our main result immediately follows from Theorem 33

- Theorem 1. Let C be a hereditary class of structures.


Assume that for every An ∈ C and every ρn ∈ An (n ∈ N) the following properties hold:

- (1) if (An)n∈N is FOlocal1 -convergent and residual, then it has a modeling FOlocal1 limit;


- (2) if (An,ρn)n∈N is FOlocal-convergent (resp. FOlocalp -convergent) and ρ-nondispersive then it has a modeling FOlocal-limit (resp. a FOlocalp -limit).


Then C admits modeling limits (resp. modeling FOp-limits). Moreover, if in cases (1) and (2) the modeling limits satisfy the Strong Finitary

Mass Transport Principle, then C admits modeling limits (resp. modeling FOplimits) that satisfy the Strong Finitary Mass Transport Principle.

7. Extended Comb Lemma

- Deﬁnition 34. A component relation system for a class C of modelings is a sequence d of equivalence relations such that for every d ∈ N and for every A ∈ C there is a

partition of the d-equivalence classes of A into two parts E0( d,A) and E+( d,A) such that:

- • every class in E0( d,A) is a singleton;
- • νA( E0( d,A)) < (d) + η(|A|) (where limd→∞ (d) = limn→∞ η(n) = 0);
- • two vertices x,y in E+( d,A) belong to a same connected component of A if and only if A |= d(x,y) (i.e. iﬀ x and y belong to a same class).


- Deﬁnition 35 ([18]). A family of sequence (Ai,n)n∈N (i ∈ I) of λ-structures is uniformly elementarily convergent if, for every formula φ ∈ FO1(λ) there is an integer N such that it holds


∀i ∈ I, ∀n ≥ n ≥ N, (Ai,n |= (∃x)φ(x)) =⇒ (Ai,n |= (∃x)φ(x)).

(Note that if a family (Ai,n)n∈N (i ∈ I) of sequences is uniformly elementarily convergent, then each sequence (Ai,n)n∈N is elementarily convergent.)

The proof of the next theorem essentially follows the lines of Section 3.3 of [18]. We do not provide the updated version of the proof here, as the proof is quite long and technical, but does not present particular additional diﬃculties when compared to the original version.

- Theorem 36 (Extended comb structure). Let (An)n∈N be an FOlocal-convergent sequence of ﬁnite λ-structures with component relation system d.

Then there exist I ⊆ N ∪ {0} and, for each i ∈ I, a real αi and a sequence

(Bi,n)n∈N of λ-structures, such that An = i∈I Bi,n (for all n ∈ N), i∈I αi = 1, and for each i ∈ I it holds

- • αi = limn→∞ ||BAi,n|

n| , and αi > 0 if i = 0;

- • if i = 0 and α0 > 0 then (Bi,n)n∈N is FOlocal-convergent and residual;
- • if i > 0 then (Bi,n)n∈N is FOlocal-convergent and non-dispersive.


Moreover, if (An)n∈N is FO-convergent we can require the family {(Bi,n)n∈N : i ∈ I} to be uniformly elementarily-convergent.

The following theorem is proved in [18]:

- Theorem 37. Assume J is a countable set, αi (i ∈ I) are reals, and (Bi,n)n∈N


(i ∈ I) are sequences of λ-structures such that αi = limn→∞ | |Bi,n|

j∈I Bj,n| (∀i ∈ I),

i∈I αi = 1, and for each i ∈ I, (Bi,n)n∈N is FOlocal-convergent. Then An = i∈I Bi,n is FOlocal-convergent. Also, if there exist λ-modelings Li (i ∈ I) such

local

local

that for each i ∈ I, Bi,n FO

−−−−→ Li, then An FO

### −−−−→ i∈I(Li,αi).

Moreover, if the family {(Bi,n)n∈N : i ∈ I} is uniformly elementarily-convergent, then (An)n∈N is FO-convergent. Also, if there exist λ-modelings Li (i ∈ I) such that for each i ∈ I it holds Bi,n −−→FO Li (for i > 0 and i = 0 if α0 > 0) and B0,n −−−→FO0 L0 (if α0 = 0) then An −−→FO i∈I(Li,αi).

8. Limit of Forests

## 8.1. Limit of Residual Sequences of Forests. In this section we shall prove

that every FOlocal1 -convergent residual sequence of trees has a modeling FOlocal1 limit that satisﬁes the Strong Finitary Mass Transport Principle.

In this section, we consider rooted forests with edges oriented from the roots. Roots are marked by unary relation M and arcs by binary relation R. Rooted forests are deﬁned by the following countable set of axioms:

- (1) for each r ∈ N, a formula stating that two distinct roots are at distance at least r (for each r ∈ N);
- (2) a formula stating that every vertex has indegree exactly one if it is not a root, and zero if it is a root;
- (3) for each r ∈ N, a formula stating that there is no circuit of length r.


In other words, a rooted forest is an directed acyclic graph such that all the vertices but the roots (which are sources) have indegree 1, and such that each connected component contains at most one root. Note that a rooted forest has two types of connected components: connected components that contain a root, and (inﬁnite) connected components that do not contain a root.

We ﬁrst state a lemma relating ﬁrst-order properties of p-tuples in a rooted forest to ﬁrst-order properties of individual vertices.

- Lemma 38. Fix rooted forests Y,Y . Let u1,...,up be p vertices of Y, let

u 1,...,u p be p vertices of Y , and let r,n ∈ N. We denote by Father both the ﬁrst-order deﬁned mapping that maps a non-root vertex to its unique in-neighbor and leaves roots ﬁxed.

Assume that for every 1 ≤ i ≤ p and every pr-local formula φ ∈ FOlocal1 with quantiﬁer rank at most n + r it holds

Y |= φ(ui) ⇐⇒ Y |= φ(u i)

and that for every 1 ≤ i,j ≤ p and every 0 ≤ k,l ≤ r, it holds

Y |= Fatherk(ui) = Fatherl(uj) ⇐⇒ Y |= Fatherk(u i) = Fatherl(u j).

Then, for every r-local formula ψ ∈ FOlocalp with quantiﬁer rank at most n it holds

Y |= ψ(u1,...,up) ⇐⇒ Y |= ψ(u 1,...,u p). Proof. The proof is similar to the proof of Lemma 4.13 in [18].

- Lemma 39. Every FOlocal1 -convergent residual sequence of forests (Yn)n∈N has a modeling FOlocal1 -limit that satisﬁes the Strong Finitary Mass Transport Principle.


Proof. Let (Yn)n∈N be an FOlocal1 -convergent residual sequence of forests. We mark a root (by unary relation M) in each connected component of Yn and orient the edges of Yn from the root (we denote by R(x,y) the binary relation expressing the existence of an arc from x to y). By extracting a subsequence, we assume that (the rooted oriented) (Yn)n∈N is FOlocal1 -convergent.

Connected components of the limit may or not contain a root. For instance, if Yn is the union of √n copies of stars of order √n, then every connected component in the limit contains a root; however, if Yn is a path of length n, only one connected component (with zero measure) in the limit contains a root.

Local formulas form a Boolean algebra. Let S(B(FOlocal1 )) be the associated Stone space, and let S1 be the closed subspace of S(B(FOlocal1 )) formed by all the T ∈ S(B(FOlocal1 )) that contain all the axioms of rooted forests (see the beginning of this section).

As (Yn)n∈N is FOlocal1 -convergent, there exists (see [16, 18]) a limit measure µ on S1 such that for every φ ∈ FOlocal1 it holds

1K(φ)(T)dµ(T), where K(φ) = {T ∈ S1 : φ ∈ T}.

lim

φ,Yn =

n→∞

S1

We partition S1 into countably many measurable parts as follows:

- • for each non-negative integer r, S1(r) denotes the clopen subset of S1 deﬁned by

S1(r) = {T : ((∃z) M(z) ∧ dist(z,x1) = r) ∈ T};

- • S1◦ is the closed subset of S1 deﬁned by


S1(r).

S1◦ = S1 \

r≥0

We further deﬁne a measurable mapping ζ : [0,1) → [0,1) as follows: Let x ∈ [0,1), x = i≥0 xi2−i (with {i : xi = 1} not coﬁnite). We deﬁne

x2i2−i) mod 1.

ζ(x) = (

i∈N

We deﬁne F : S1 → S1 by

T if M(x1) ∈ T {φ : ((∃z)R(z,x1) ∧ φ(z)) ∈ T} otherwise

F(T) =

(Note that F(T) is indeed an ultraﬁlter of B(FOlocal1 ) as there exists exactly one z such that R(z,x1).)

Deﬁne w : S1 \S1(0) → {0,1,...,∞} as the supremum of the integers k such that there exists a tree A with universe A and a ∈ A such that there are at least k sons b1,...,bk of a such that for all φ ∈ FOlocal1 it holds A |= φ(bi) if and only if φ ∈ T.

Finally, we deﬁne the mapping ξ : (S1 \ S1(0)) × [0,1) → [0,1) by

w(T)α mod 1 if w(T) < ∞ ζ(α) otherwise

ξ(T,α) =

Note that for every (T,α) ∈ (S1 \ S1(0)) × [0,1), the set {α ∈ [0,1) : ξ(T,α ) = ξ(T,α)} has cardinality w(T) (if w(T) < ∞) and is inﬁnite (if w(T) = ∞).

Using these special functions, we can construct limit modelings of residual sequences of forests with the following simple form:

Let Z = r≥0 S1(r) × [0,1) ∪ S1◦ × [0,1) × S1 , where S1 is the unit circle (identiﬁed here with reals mod 2π). It is clear that Z is the standard Borel space. We ﬁx a real θ0 such that θ0 and π are incommensurable, and we deﬁne a rooted directed forest Z on Z has follows:

- • for z ∈ Z, it holds M(z) if and only if z ∈ S1(0) × [0,1);
- • for positive integer r and z ∈ S1(r) × [0,1), z = (T,α), the vertex z has exactly one incoming edge from the vertex (F(T),ξ(T,α)) ∈ S1(r−1) ×[0,1);
- • for z ∈ S1◦ × [0,1) × S1, z = (T,α,θ) the vertex z has exactly one incoming edge from the vertex (F(T),ξ(T,α),θ + θ0).


It is easily checked that for z ∈ Z (z = (T,α) or z = (T,α,θ)), the set of formulas φ ∈ FOlocal1 such that Z |= φ(z) is exactly T.

We now prove that Z is a relational sample space. It suﬃces to prove that for every p ∈ N and every ϕ ∈ FOlocalp the set

Ωϕ(Z) = {(v1,...,vp) ∈ Vhp : Z |= ϕ(v1,...,vp)} is measurable.

Let ϕ ∈ FOlocalp and let n = qrank(ϕ). We partition Vh into equivalence classes modulo ≡n+r, which we denote C1,...,CN. Let i1,...,ip ∈ [N] and, for 1 ≤ j ≤ p, let vj and v j belong to Ci

. According to Lemma 38, if for every 1 ≤ i < j ≤ p and

j

- 1 ≤ k,l ≤ r it holds


Fatherk(ui) = Fatherl(u,j) ⇐⇒ Fatherk(u i) = Fatherl(u,j ) then it holds

(v1,...,vp) ∈ Ωϕ(Z) ⇐⇒ (v 1,...,v p) ∈ Ωϕ(Z). According to the encoding of the vertices of Z, the conditions on the common ancestors rewrite as equalities and inequalities of iterated measurable functions [0,1] → [0,1). It follows that Ωϕ(Z) is measurable. Thus Z is a relational sample space.

We deﬁne a probability measure νZ on Z to turn Z into a modeling as follows:

- • on r≥0 S1(r) ×[0,1), νZ is the product of the restriction of µ and the Borel measure on [0,1);
- • on S1◦ × [0,1) × S1, νZ is the product of the restriction of µ, the Borel measure on [0,1), and the Haar (rotation invariant) probability measure of S1.


It is easily checked from the above deﬁnition of Z (and of course ζ,F,ξ,w)

that the modeling Z is a modeling FOlocal1 -limit of (Yn)n∈N, and that if µ satisﬁes the Finitary Mass Transport Principle then Z satisﬁes the Strong Finitary Mass Transport Principle.

The construction of a modeling FOlocal1 -limit for the root-free part resembles spinning wheel of a limit forest (cf [2]) and it is schematically illustrated on Fig 1.

- 8.2. Limit of ρ-non-dispersive Sequences of Trees. Let λ be the signature of graphs, λ• the signature of graphs with additional unary relation R, λ+ the signature of graphs with additional unary relations R and P, λω the signature of


graphs with countably many additional unary relations Mi and Ni (i ∈ N). We consider two basic interpretation schemes, which we made use of already in [18]:

x

θ0

θ0

√n

√n √n √n √n √n √n √n

Figure√n. Vertex1. Modelingx is adjacentFOlocal1to 2-limitℵ of a √n-path of stars of order

vertices on a segment and to two vertices obtained by rotation of ±θ0, where θ0 is irrational to π.

0

- (1) IY →F is a basic interpretation scheme of λ+-structures in λ•-structures deﬁned as follows: for every λ-structure A, the domain of IY →F(A) is the same as the domain of A, and it holds (for every x,y ∈ A):

IY →F(A) |= x ∼ y ⇐⇒ A |= (x ∼ y) ∧ ¬R(x) ∧ ¬R(y) IY →F(A) |= R(x) ⇐⇒ A |= (∃z) R(z) ∧ (z ∼ x) IY →F(A) |= P(x) ⇐⇒ A |= R(x)

In particular, if Y is a λ•-tree, with a single vertex marked by R (the root), IY →F maps Y into a λ+-forest IY →F(Y ), formed by the subtrees rooted at the sons of the former root (roots marked by R) and a single vertex rooted principal component (the former root, marked P);

- (2) IF→Y is a basic interpretation scheme of λ•-structures in λ+-structures deﬁned as follows: for every λ+-structure A, the domain of IF→Y (A) is the


same as the domain of A, and it holds (for every x,y ∈ A): IF→A(A) |= x ∼ y ⇐⇒ A |= (x ∼ y) ∨ R(x) ∧ P(y) ∨ R(y) ∧ P(x) IF→A(A) |= R(x) ⇐⇒ A |= P(x)

In particular, IF→Y maps a λ+-forest F with all connected components rooted by R, except exactly one rooted by P into a λ•-tree IF→Y (F) by making each non principal root a son of the principal root;

- Lemma 40. Every FO-convergent ρ-non-dispersive sequence of rooted trees (Yn)n∈N has a modeling FO-limit.


Proof. Let (Yn)n∈N be an FO-convergent ρ-non-dispersive sequence of rooted trees. Then IY →F(Yn)n∈N is an FO-convergent sequence of rooted forests. According to Theorem 36, there exist I ⊆ N, reals αi, sequences (Bi,n)n∈N for i ∈ I ∪ {0}, such that:

- • α0 ≥ 0, αi > 0 (for i ∈ I), and i∈I∪{0} αi = 1;
- • Yn is the union of the Bi,n (i ∈ I ∪ {0});
- • limn→∞ |Bi,n|/|Yn| = αi (for i ∈ I ∪ {0});
- • (B0,n)n∈N is an FOlocal-convergent residual sequence if α0 > 0;
- • (Bi,n)n∈N is an FOlocal-convergent non-dispersive sequence;
- • the family {(Bi,n,ρi,n)n∈N : i ∈ I} is uniformly elementarily convergent.


In this situation we apply Theorem 37: We denote by Li and L0 the modeling limits, so that

- • (Bi,n) −−→FO Li (for i ∈ N);
- • (B0,n) −−→FO L0 (if α0 > 0), and (B0,n) −−−→FO0 L0 (otherwise).


Then we have (by Theorem 37): Yn −−→FO IF→Y

(Li,αi) .

i∈I∪{0}

It is easily checked that each sequence (Bi,n)n∈N is ρ-non-dispersive (for Bi,n rooted at its marked vertex), as a direct consequence of the fact that (Yn)n∈N (rooted at marked vertex) is ρ-non-dispersive.

If we repeat the same process on each ρ-non-dispersive sequence (Bi,n)n∈N (for i ∈ I \ {0}), we inductively construct a countable rooted tree S and, associated to each node v of the tree, a residual sequence of forests (Fv,n)n∈N and a weight λv. If we have started with a ρ-non-dispersive sequence, then for every > 0 there is integer d such that the sum of the measures of the residues attached to the nodes at height at most d is at least 1 − .

According to Lemma 39, for each residual FO-convergent sequence (Fv,n)n∈N of forests there is a rooted tree modeling L0v that is the FOlocal1 -limit of (IF→Y (Fv,n))n∈N. Hence, according to Lemmas 20, 21, and 23, there is a rooted tree modeling Lv, which is the FO-limit of (IF→Y (Fv,n))n∈N.

The grafting of the modelings Lv on the rooted tree S (with weights λv) form a ﬁnal modeling L.

We prove that L is a relational sample space: each ﬁrst-order deﬁnable subset

of Lp is a Lω1ω-deﬁnable subsets of the countable union of all the Lv in which the roots of all the roots have been marked by distinct unary relations Mv. As the

used language in countable, it follows from Lemma 7 that Lω1ω-deﬁnable subsets are Borel measurable.

Let d ∈ N, and let Yn(d) be the subtree of Yn induced by vertices at distance at most d from the root. As the trees Yn(d) are obtained by an obvious interpretation, we get that (Yn(d))n∈N is FO-convergent. Now consider L(d), obtained from L by restricting to the set Xd of the vertices at distance at most d from the root. As the set Xd is ﬁrst-order deﬁned, it is measurable. It follows that Xd (with induced σ-algebra) is a standard Borel space, and that L(d) is a relational sample space. We deﬁne a probability measure on L(d) by νL(d) = νL/νL(Xd), thus deﬁning the modeling L(d). By applying iteratively (at depth d) Theorem 37 and the interpretation IF→Y we easily deduce that L(d) is a modeling FO-limit of (Yn(d))n∈N. Thus, according to Lemma 28, we deduce that L is a modeling FOlocal-limit of the sequence (Yn)n∈N. By Lemma 27, we deduce that (Yn)n∈N has a modeling FO-limit, which is the union of L and a countable graph.

- Theorem 2. Every FO-convergent sequence of ﬁnite forests has a modeling FOlimit that satisﬁes the Strong Finitary Mass Transport Principle.


Proof. The theorem is an immediate consequence of Theorem 1 and Lemmas 39 and 40.

9. Conclusion

Compared to the results obtained in [18] for rooted trees with bounded height, we do not have inverse theorem for tree-modeling. Our conjecture is that a treemodeling that satisfy the Strong Finitary Mass Transport Principle and whose complete theory has the ﬁnite model property is the modeling limit of a sequence of ﬁnite trees.

We believe that our approach can be used to obtain modeling limits of further classes of graphs. In particular, we believe that the structure “residual limits grafted on a countable skeleton” might well be universal for sequences of nowhere dense graphs.

References

- [1] I. Benjamini and O. Schramm, Recurrence of distibutional limits of ﬁnite planar graphs, Electron. J. Probab. 6 (2001), no. 23, 13pp.
- [2] D. Clayton-Thomas, Spinning wheel, song by Blood, Sweat & Tears, 1969.
- [3] H. Gaifman, On local and non-local properties, Proceedings of the Herbrand Symposium, Logic Colloquium ’81, 1982.
- [4] M. Grohe, S. Kreutzer, and S. Siebertz, Deciding ﬁrst-order properties of nowhere dense graphs, arXiv:1311.3899 [cs.LO], November 2013.
- [5] C. R. Karp, Languages with expressions of inﬁnite length, vol. 33, NorthHolland Pub. Co., 1964.
- [6] A. Kechris, Classical descriptive set theory, Springer-Verlag, 1995.
- [7] D. Kr´l’, M. Kupec, and V. Tu˚ma, FO limits of trees, oral presentation at Utrecht Graphs Workshop 2013, November 2013.
- [8] D. Lascar, La th´eorie des mod`eles en peu de maux, Cassini, 2009.
- [9] E.G.K. Lopez-Escobar, An interpolation theorem for inﬁnitely long sentences, Fundamenta Mathematicae 57 (1965), 253–272.


- [10] L Lov´sz, Large networks and graph limits, Colloquium Publications, vol. 60, American Mathematical Society, 2012.
- [11] L. Lov´sz and B. Szegedy, Limits of dense graph sequences, J. Combin. Theory Ser. B 96 (2006), 933–957.
- [12] J. Nesˇetrˇil and P. Ossona de Mendez, First order properties on nowhere dense structures, The Journal of Symbolic Logic 75 (2010), no. 3, 868–887.
- [13] , From sparse graphs to nowhere dense structures: Decompositions, independence, dualities and limits, European Congress of Mathematics, European Mathematical Society, 2010, pp. 135–165.

- [14] , Sparse combinatorial structures: Classiﬁcation and applications, Proceedings of the International Congress of Mathematicians 2010 (ICM 2010) (Hyderabad, India) (R. Bhatia and A. Pal, eds.), vol. IV, World Scientiﬁc, 2010, pp. 2502–2529.

- [15] , On nowhere dense graphs, European Journal of Combinatorics 32

(2011), no. 4, 600–617.

- [16] , A model theory approach to structural limits, Commentationes Mathematicæ Universitatis Carolinæ 53 (2012), no. 4, 581–603.

- [17] , Sparsity (graphs, structures, and algorithms), Algorithms and Combinatorics, vol. 28, Springer, 2012, 465 pages.

- [18] , A uniﬁed approach to structural limits (with application to the study of limits of graphs with bounded tree-depth), arXiv:1303.6471v2 [math.CO], October 2013.

- [19] D. Scott, Logic with denumerably long formulas and ﬁnite strings of quantiﬁers, The theory of models 1104 (1965), 329–341.
- [20] D. Scott and A. Tarski, The sentential calculus with inﬁnitely long expressions, Colloquium Mathematicae, vol. 6, Institute of Mathematics Polish Academy of Sciences, 1958, pp. 165–170.
- [21] A. Tarski, Remarks on predicate logic with inﬁnitely long expressions, Colloquium Mathematicum 16 (1958), 171–176.


Jaroslav Neˇsetril,ˇ Computer Science Institute of Charles University (IUUK and ITI), Malostranske´ nam.25,´ 11800 Praha 1, Czech Republic

E-mail address: nesetril@iuuk.mff.cuni.cz

Patrice Ossona de Mendez, Centre d’Analyse et de Mathematiques´ Sociales (CNRS, UMR 8557), 190-198 avenue de France, 75013 Paris, France — and — Computer Science Institute of Charles University (IUUK), Malostranske´ nam.25,´ 11800 Praha 1, Czech Republic

E-mail address: pom@ehess.fr

