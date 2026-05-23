arXiv:1204.0449v2[math.FA]30May2012

FINITE GRAPHS AND AMENABILITY

GABOR´ ELEK

Abstract. Hyperﬁniteness or amenability of measurable equivalence relations and group actions has been studied for almost ﬁfty years. Recently, unexpected applications of hyperﬁniteness were found in computer science in the context of testability of graph properties. In this paper we propose a uniﬁed approach to hyperﬁniteness. We establish some new results and give new proofs of theorems of Schramm, Lova´sz, Newman-Sohler and Ornstein-Weiss.

Contents

- 1. Introduction 1

- 1.1. Local statistics for graphs and graphings 1
- 1.2. Hyperﬁniteness 3
- 1.3. Equivalences of graphings 3
- 1.4. The Equipartition Theorem and its consequences 4


- 2. Kaimanovich’s Theorem revisited 4
- 3. Canonical limits 7


- 3.1. The Benjamini-Schramm limit measure 7
- 3.2. B-graphs 8
- 3.3. Edge-colored graphs and B-graphs 8
- 4. The Oracle Method 8
- 5. The proof of Theorem 1 and Theorem 2 11
- 6. Equipartitions 11

- 6.1. The Transfer Theorem 11
- 6.2. The Uniformicity Theorem 13
- 6.3. The proof of the Equipartition Theorem 15
- 6.4. The proof of Theorem 5 15


- 7. Local-global convergence 15
- 8. Strong equivalence 17


- 8.1. The proof of Theorem 3 17
- 8.2. Rokhlin Lemma for non-free actions 17 References 18


1. Introduction

- 1.1. Local statistics for graphs and graphings. First let us recall some basic notions.


Let Gd denote the set of ﬁnite simple graphs of vertex degree bound d (up to isomorphism). A rooted graph H of radius at most r is

![image 1](<2012-elek-finite-graphs-amenability_images/imageFile1.png>)

Work supported in part by a Marie Curie grant and TAMOP 4.2.1/B-09/1/KMR-2010-003. AMS SUBJECT CLASSIFICATION: 43A07, 05C99

1

- • a graph with vertex degree bound d and a distinguished vertex x (the root)
- • such that dG(x,y) ≤ r for any y ∈ V (G), where dG is the usual shortest path metric.


Let us denote by Udr the set of all rooted graphs of radius at most r up to rooted isomorphisms. If G ∈ Gd and α ∈ Udr then T(G,α) is deﬁned as

T(G,α) := {v ∈ V (G) | Br(v) ∼ α}.

Set p(G,α) := |T|V(G,α(G)|)| . That is p(G,α) is the probability that the r-ball around a random vertex of G is rooted-isomorphic to α. Let us enumerate the elements of the set ∪∞r=1Udr. Then we get a map L : Gd → [0,1]N. We equip [0,1]N with a metric dπ that generates the usual product topology.

![image 2](<2012-elek-finite-graphs-amenability_images/imageFile2.png>)

L(G) = {p(G,α1),p(G,α2),... } The map is “almost” injective: if L(G) = L(H) then there exists a graph K such that both

- G and H are disjoint union of K-copies. We say that a sequence of graphs {Gn} ⊂ Gd is convergent (in the sense of Benjamini and Schramm) if limn→∞ p(Gn,α) exists for any r ≥ 1


and α ∈ Udr. That is {Gn}∞n=1 is convergent if and only if {L(Gn)}∞n=1 is convergent pointwise. Now we recall the notion of a graphing [15]. Let X be a standard Borel set. A Borel set

- E ⊂ X × X is a Borel graph if


- • (x,y) ∈ E implies that (y,x) ∈ E
- • (x,x) ∈/ E if x ∈ X.


Note that the degree of a vertex x is well-deﬁned. A Borel graph of vertex degree bound d is such a graph that all of its components are countable graphs with vertex degree bound d. A measurable graph (or a graphing) is a Borel graph on a standard Borel probability measure space (X,µ) satisfying the following property.

• If T : X → X is a Borel bijection such that either T(x) = x or (x,T(x)) ∈ E, then T preserves the measure µ.

The most important examples of such graphings are given by group actions. Let Γ be a ﬁnitely generated group with a symmetric generating system S. Consider a measure preserving Borel action of Γ on (X,µ). Now let (x,y) ∈ E if x = y and sx = y for some s ∈ S. Then G(X,E,µ) is a graphing. For such a graphing G with vertex degree bound d we can deﬁne the probabilities p(G,α) as well. Let α ∈ Udr, then T(G,α) is the Borel set of points x ∈ X such that Br(x) ∼ α. Let p(G,α) := µ(T(G,α)). Thus we can extend L to the isomorphism classes of graphings of vertex degree bound d (from now on, all the graphing in the paper are supposed to have vertex degree bound d). We say that G is a limit of a convergent graph sequence {Gn}∞n=1 ⊂ Gd if for any r ≥ 1 and α ∈ Udr

p(Gn,α) = p(G,α),

lim

n→∞

that is limn L(Gn) = L(G). We deﬁne the pseudo-distance of graphings dstat(G,H) by dπ(L(G),L(H)).

For any convergent graph sequence there exists a limit graphing [7], the converse statement is an open conjecture due to Aldous and Lyons [3]. Let G(X,E,µ) be a graphing and Z ⊂ E be a Borel set of edges. Let

degZ(x) := |{y ∈ X | (x,y) ∈ Z}|. Then

- 1

![image 3](<2012-elek-finite-graphs-amenability_images/imageFile3.png>)

- 2 X


degZ(x).

µE(Z) :=

- 1.2. Hyperﬁniteness. The notion of hyperﬁniteness was introduced in [9]. A set of graphs {Gn} ⊂ Gd is called a hyperﬁnite family if

• for any ǫ > 0 there exists K > 0 such for each n ≥ 1 there exists a set Zn ⊂ V (Gn), |Zn| < ǫ|V (Gn)| such that if we remove the edges incident to Zn the resulting graph G′n consists of components of size at most K.

Note that any planar or subexponentially growing family of graphs is hyperﬁnite [8]. Also, Følner sequences of a ﬁnitely generated amenable group form a hyperﬁnite family. Hyperﬁniteness can be deﬁned for graphings as well [15]. We call a graphing G hyperﬁnite (or amenable) if for any ǫ > 0 there exists K > 0 such that for some Borel set Z ⊂ X

- • µ(Z) < ǫ
- • all the components of E\Z have size at most K.


Note that E\Z denotes the graphing with vertex set X, with edges of G that are not incident to an element of Z. The classical examples of hyperﬁnite graphings are graphings of subexponential growth and the ones associated to probability measure preserving actions of ﬁnitely generated amenable groups. Now we can formulate our ﬁrst result.

- Theorem 1. A convergent graph sequence {Gn}∞n=1 is hyperﬁnite if and only if its limit graphing G is hyperﬁnite.

The original version of this theorem was proved by Oded Schramm [19] using an ingenious probabilistic idea. Notice that he considered unimodular measures as limit objects. He noted that there is a minor technical diﬃculty in some cases (due to symmetries). Our approach is completely deterministic and seems to avoid these diﬃculties. Interestingly, in both proofs one of the directions are much easier to prove than the other, but not the same ones (the reason of this strange phenomenon is hidden in the deﬁnition of hyperﬁniteness for unimodular measures).

1.3. Equivalences of graphings. Following Lov´asz [16], we say that two graphings G and H are weakly equivalent if they have the same local statistics L(G) = L(H). We will prove the following statement (also proved by Lov´asz using Schramm’s probabilistic method).

- Theorem 2. If G and H are weakly equivalent then H is hyperﬁnite if and only if G is hyperﬁnite. That is hyperﬁniteness is a local property.

We say that two graphings G(X,µ) and H(Y,ν) are strongly equivalent if for any ǫ > 0 there exists a measure preserving bijective map ρǫ : X → Y such that

µE(ρ−ǫ 1E(H)△E(G)) < ǫ

If two graphings are strongly equivalent then they are clearly weakly equivalent as well. However for hyperﬁnite graphings, the converse is true.

- Theorem 3. If G and H are weakly equivalent hyperﬁnite graphings, then they are strongly equivalent.




We shall prove a variant of this theorem for group actions as well, generalizing the classical Rokhlin Lemma.

- 1.4. The Equipartition Theorem and its consequences. The following result states that for a hyperﬁnite family statistically similar graphs can be partitioned similarly.


- Theorem 4. Let P ⊂ Gd be a hyperﬁnite family. Then for any ǫ > 0, there exists an integer K > 0 with the following property: For any δ > 0, there exists f(δ) > 0 such that if G ∈ P

and H ∈ Gd with dstat(G,H) ≤ f(δ) then one can remove less that 2ǫ|E(G)| edges of G and less that 2ǫ|E(H)| edges of H such that

- • In the remaining graphs G′ and H′, all components have size at most K.
- • S,|V(S)|≤K |cGS′ − cSH′| < δ,


where CSG′ is the set of points that are in a component of G′ isomorphic to G′, and cGS′ =

|CSG′|

![image 4](<2012-elek-finite-graphs-amenability_images/imageFile4.png>)

|V(G′)|.

Thus, according to the Equipartition Theorem if a graph H is statistically close to a planar graph H, then G can be made planar by removing a small of amount of edges. This means exactly that the planarity property is testable among bounded degree graphs (see [6]). The analogue of Theorem 4 was proved in [8] for graph classes of subexponential growth. Using Theorem 4, we will prove that if a hyperﬁnite graph sequence converges then it converges locally-globally.

The following consequence of the Equipartition Theorem was proved by Newman and Sohler

- [17] (based on the work of Hassidim, Kelner, Nguyen and Onak [11] )) This result can be viewed as the ﬁnitary version of Theorem 3.


- Theorem 5. Let P ⊂ Gd be a hyperﬁnite family. Then for any δ > 0, there exists f(δ) > 0 such that if for a graph G ∈ P and H ∈ Gd, |G| = |H|, dstat(G,H) < f(δ) then G and H are δ-close, that is we have a bijection ρ : V (G) → V (H) such that


|ρ−1E(H)△E(G)| < δn.

It immediately follows from Theorem 5, that graph isomorphism is testable for hyperﬁnite graph families. Consequently, every reasonable property and parameter are testable for hyperﬁnite graph families (see 5 for deﬁnitions of testability). Similar testability results were proved in [8] in case of graph families of subexponential growth.

Acknowledgement: The author thanks the Mittag-Leﬄer Institute, where parts of the paper were written, for their hospitality.

2. Kaimanovich’s Theorem revisited

The goal of this section is to generalize a result of Kaimanovich [13]. First we prove a statement that is missing from [13], but seems to be implicitly accepted in the paper.

- Deﬁnition 2.1. A graphing G has Property A if for every induced Borel subgraphing T ⊆ G, almost every component have zero isoperimetric constant.
- Deﬁnition 2.2. A graphing G has Property B if the following condition is satisﬁed. For any ǫ > 0, every induced subgraphing T contains a subgraphing S that intersects almost every components of T and all the components of S have isoperimetric constant less than ǫ in T .


Note that if F ⊂ T is a ﬁnite subgraph, then its isoperimetric constant is deﬁned as i(F) :=

|∂EF| |F|

,

![image 5](<2012-elek-finite-graphs-amenability_images/imageFile5.png>)

where ∂EF is the set of edges e = (x,y) such that x ∈ F and y ∈/ F. The isoperimetric constant of an inﬁnite graph is the inﬁmum of the isoperimetric constants of its ﬁnite subgraphs. An induced subgraphing T of G is a Borel graphing on a Borel subset Y of X such that if p,q ∈ Y is adjacent in G then they are adjacent in T as well.

- Proposition 2.1. For a graphing G of vertex degree bound d the two properties above are equivalent.

Proof. We only need to prove that Property A implies Property B. Let T ⊆ G be a subgraphing satisfying the condition of Property A. We construct S ⊂ T inductively. Let Sn−1 ⊂ T be the subgraphing constructed after the n−1-th step consisting of ﬁnite components having isoperimetric constants less than ǫ. Now let us consider a Borel coloring

φn : X → Cn = {a1,a2,... ,aqn}

by ﬁnitely many colors such that φn(x) = φn(y) if dG(x,y) ≤ 2n + 2. Such coloring exists by [14]. Let A1 = φ−n1(a1) be the ﬁrst color-class. For x ∈ A1 let Kx1 be the set of ﬁnite subsets F in Bn(x) containing x, having isoperimetric constant less than ǫ and such that F ∩ B2(Sn−1) = ∅. Note that B2(L) is the 2-neighborhood of the set L.

We use the standard ordering trick and suppose that X = [0,1]. Let us order Kx1 the following way.

- • If |A| < |B|, then A < B.
- • If |A| = |B|, then A < B provided that min


a∈A

a < min

b∈B

b.

Let Rx1 be the smallest element of Kx1. Then ∪x∈A1Rx1 is a Borel set. Now let A2 = φ−2 1(a2) be the second color-class. For x ∈ A2 let Kx2 be the set of ﬁnite subsets F in Bn(x) containing x, having isoperimetric constant less than ǫ and such that F ∩ B2(Sn−1 ∪ x∈A

1

Rx1) = ∅. Again, we consider the smallest element in Kx2. Then ∪x∈A2Rx2 is a Borel set. Inductively, we deﬁne the Borel sets ∪x∈AiRxi and ﬁnally we deﬁne

Sn = Sn−1 ∪ (

qn

i=1 x∈Ai

Rxi ).

Then Sn also consists of components having isoperimetric constant less than ǫ. Now we prove that S = ∪∞n=1Sn intersects almost all components of T . Let Z ⊂ T be a component of isoperimetric constant zero and let F ⊂ Z be a ﬁnite subset of isoperimetric constant less than ǫ. Let F ⊂ Bn(x) for some x ∈ F. Then the only reason for not to choose F as some Rxi in the n-th step is that we choose another subset G ⊂ Z with isoperimetric constant less than ǫ. This shows that Property A implies Property B.

Now we are ready to state and prove Kaimanovich’s Theorem.

- Proposition 2.2 (Kaimanovich’s Theorem). For a graphing G of vertex degree bound d the following two statements are equivalent.


- (1) G is hyperﬁnite.
- (2) For any subgraphing T ⊆ G of positive measure almost all the components have isoperimetric constant zero.


Proof. First we show that (2) implies (1). Let us suppose that G satisﬁes the second condition.

- Let G = T0 and S0 be a Borel subset of positive measure consisting of ﬁnite components with isoperimetric constant less than ǫ > 0. Such set exists by Proposition 2.1. Let E0 be the set of edges pointing out of S0. Then µE(E0) ≤ ǫµ(S0). Remove E0 from T0 along with the subgraphing S0. Let us denote the resulting subgraphing by T1. Note that µ(T1) < µ(T0), where µ(T1) denote the measure of the vertex set of T1. Now we proceed by transﬁnite induction. Suppose that Tα is constructed for some countable ordinal and µ(Tα) > 0. Let Sα be a Borel set of positive measure consisting of ﬁnite components with isoperimetric constant less than ǫ > 0 in Tα. Again, let Eα be the set of edges pointing out of Sα. Then µE(Eα) ≤ ǫµ(Sα). Remove Eα from Tα along with the subgraphing Sα. Let us denote the resulting subgraphing by Tα+1. Then µ(Tα+1) < µ(Tα). For a limit cardinal α′, let Tα′ be ∩α<α′Tα. Since µ(Tα) > µ(Tα+1), there exists a countable ordinal β for which µ(Tβ) = 0. Let S = ∪β<αSα and M = ∪β<αEα. Clearly, µE(M) < ǫ. Hence, by removing M and Tα from G we obtain a graphing consisting of ﬁnite components. This implies the hyperﬁniteness of G.


Now let us prove that (1) implies (2). Suppose that G has a subgraphing T of positive measure such that the measure of points p for which the component Zp has positive isoperimetric constant is not zero. Then there exists δ > 0 and a Borel subgraphing Tδ ⊂ T of positive measure such that all the components of Tδ have isoperimetric constants at least δ. Now suppose that G is hyperﬁnite. Let F be a Borel set of edges such that µE(F) < δ|µ10(Tδ)| and S = G\F consists of ﬁnite components. Let K be a component of S. Then by our condition, there exist at least δ|Tδ ∩ K| edges pointing out of K. This gives us an estimate for the edge density of F

![image 6](<2012-elek-finite-graphs-amenability_images/imageFile6.png>)

µE(F) > δ|Tδ|, leading to a contradiction.

Kaimanovich’s Theorem will be applied in our paper using the following corollary. Let G(X,µ) and H(Y,ν) be graphings. A surjective map π : X → Y is a factor map (that is H is a factor

- of G) if


- • π is measure preserving, that is for any Borel set A ⊆ Y , µ(π−1(A)) = ν(A).
- • For almost all x ∈ X, π is a graph isomorphism restricted on the component of x.


- Proposition 2.3. If H is a factor of G, then H is hyperﬁnite if and only if G is hyperﬁnite.


Proof. First suppose that H is hyperﬁnite and W is a Borel set of the edges of H such that νE(W) < ǫ and all the components of E(H)\W have size at most K. Then µE(π−1(W)) < ǫ and all the components of E(G)\π−1(W) have size at most K. Hence G is hyperﬁnite.

For the converse statement, suppose that H is not hyperﬁnite. Then by Kaimanovich’s Theorem, there exists a subgraphing T ⊆ H such that not almost all its components have zero isoperimetric constant. Then π−1(T ) is a subgraphing of G witnessing the non-hyperﬁniteness of G.

Note: Let Γ be a ﬁnitely generated amenable group acting freely on the standard Borel space (X,µ) preserving the probability measure. Then the graphing of the action is hyperﬁnite. The standard proof of this fact is given by the Ornstein-Weiss quasi-tiling construction

- [18]. However, a very short proof can be obtained by Kaimanovich’s Theorem. Without claiming any originality, we provide a proof for completeness.


Proof. Let S be a symmetric generating system and G(X,µ) the graphing of the action. Suppose that G is not hyperﬁnite. Then it contains a subgraphing T , V (τ) > 0, such that the isoperimetric constants of all the components of T are larger than a certain positive constant δ. Indeed, if T is a subgraphing with components of positive isoperimetric constants and Tδ is the subgraphing consisting of components having isoperimetric constant larger than δ, then ∪δTδ = T . Let {Fn}∞n=1 be a Følner sequence in Γ. By the invariance of the measure,

|Fnx ∩ V (T )|dµ = |Fn|µ(V (T )).

X

Hence, we have a sequence of points {xn}∞n=1 ⊂ X such that

|Fnx ∩ V (T )| |Fn|

> µ(V (T )) > 0.

![image 7](<2012-elek-finite-graphs-amenability_images/imageFile7.png>)

Therefore the isoperimetric constants of the induced subgraphs {[Fnx∩V (T )]}∞n=1 tend to 0, leading to a contradiction.

3. Canonical limits This section is of rather technical nature.

- 3.1. The Benjamini-Schramm limit measure. First let us recall the notion of the Benjamini-Schramm limit measure construction. Let Grd be the set of all connected, rooted, countable graphs up to rooted graph isomorphisms. One can introduce a metric on Grd by setting


d(X,Y ) = 2−r , where r is the largest integer such that the r-balls around the roots of X resp. Y are isomorphic. The metric space Grd is compact. Note that for all r ≥ 1 and α ∈ Udr, T(α) ⊆ Grd, that is the set of all graphs such that the r-ball around their roots is isometric to α is a clopen set. Now let Gˆ = {Gn} ⊂ Gd be a convergent graph sequence. Then

µGˆ(T(α)) = lim

p(Gn,α)

n→∞

deﬁnes a Borel probability measure on Grd. This measure is called the Benjamini-Schramm limit measure (a so-called unimodular measure, see [3]) We say that X,Y ∈ Grd are adjacent if there is a neighbouring vertex y of the root of X such that Y is rooted isomorphic to the underlying graph of X with root y. In this way, Grd is equipped with a Borel graph structure. However, the following example shows that (Grd,µGˆ) is not necessarily a graphing.

Example 3.1. Let Gn be the graph obtained from the line graph Ln of length n by adding two leaves for each vertex. Then Gˆ = {Gn}∞n=1 is a convergent graph sequence. The limit measure is concentrated to two points a and b such that µGˆ(a) = 1/3 and µGˆ(b) = 2/3. Hence (Grd,µGˆ) is not a graphing.

- 3.2. B-graphs. It was observed by Aldous and Lyons (Example 9.9 [3]) that for each unimodular measure, one can construct a marked network, which is a graphing. This should be thought as the Bernoulli space of the unimodular measure. So let us recall the notion of B-graphs from [8]. This is an explicite realization of the Aldous-Lyons marked network con-


struction. Let B be the set {0.1}N with the standard product measure. Then GBd is the set of all ﬁnite simple graphs of vertex degree bound d with vertices colored by B (up to colored

isomorphisms). These objects are called B-graphs. Let Udr,B be the set of all rooted r-balls with vertices colored with {0,1}-strings of length r. If G ∈ GBd , β ∈ Udr,B and x ∈ V (G) then x ∈ T(G,β) if the rooted r-ball around x is isomorphic to β, when one restricts the color of the vertices to the ﬁrst r-digits. Set p(G,β) := T|V(G,β(G)|). Again, we can deﬁne the convergence of B-graphs. The sequence of B-graphs {Gn}∞n=1 is convergent if for any r ≥ 1 and β ∈ Udr,B, limn→∞ p(Gn,β) exits.

![image 8](<2012-elek-finite-graphs-amenability_images/imageFile8.png>)

The corresponding limit objects are measures on GrBd , the space of connected, rooted, countable, B-colored graphs. The reason we introduced the notion of B-graphs is that using

- them one can construct canonical limit graphings of standard (colorless) convergent graph


sequences. Let us recall the construction from [8]. Let Gˆ = {Gn}∞n=1 ⊂ Gd be a convergent graph sequence. Let us color the vertices of the graphs in the sequence randomly, independently, by elements of the probability measure space B. Then with probability 1, the resulting

B-colored graph sequence will be convergent to the same measure µBGˆ on GrBd . This measure is the Bernoullization of the Benjamini-Schramm limit measure of the original graph sequence

in the sense of Aldous and Lyons. Then

- • Then G(GrBd ,µBGˆ) is a graphing that we denote by GGˆ.
- • For µBGˆ-almost all x ∈ GrBd the orbit of x in GGˆ is isomorphic to x as rooted B-graphs.


We call GGˆ the canonical limit graphing of Gˆ.

- 3.3. Edge-colored graphs and B-graphs. Finally, we need a little bit more complicated construction of the same genre as the ones above. Let CGd be the set of simple graphs of vertex degree bound d with proper edge-colorings by d+12 colors. Recall that a coloring is proper if incident edges are colored diﬀerently. Similarly, we can consider CGBd the set of


B-graphs of vertex degree bound d with proper edge colorings by d+12 colors. Again, we can deﬁne the convergence of edge-colored graphs resp. edge-colored B-graphs together with

compact metric spaces CGrd resp. CGrBd , the spaces of properly edge-colored rooted graphs resp. properly edge-colored rooted B-graphs (by d+12 colors). Also, the limits of convergent sequences are the appropriate measures on CGrd resp. CGrBd . One should note that there exists a natural Γ-action on graphs properly edge-colored by d+12 colors, where Γ is the

d+1

2 -fold free product of cyclic groups of order 2. Also, Γ acts on CGrd resp. on CGrBd by homeomorphisms. Let Hˆ = {Hn}∞n=1 ⊂ CGd be a convergent graph sequence and µHˆ be the limit measure on CGrd. Then the Borel probability measure µHˆ is invariant under the natural Γ-action. Similarly to the colorless case one can construct the canonical limit measure µBHˆ on CGrBd as well.

4. The Oracle Method

The essence of the oracle method is that it enables us to construct subsets of ﬁnite graphs using one single subset of GrBd . The Oracle Method is strongly related to the notion of

randomized distributed algorithms. Suppose that a subset A ⊆ Udr,B is given. Say, we have a ﬁnite graph G of degree bound d. We color the vertices of G random uniformly with {0,1}-

strings of length r. Then we construct a subset VA ⊆ V (G) the following way. If the r-ball around v ∈ V (G) is colored-isomorphic to an element of A, let v ∈ VA. Otherwise, v ∈/ VA. The only reason we need colorings is that we can use the colors to “break ties” in the case of symmetries. If G is a transitive graph, distributed algorithms without randomization can produce only the empty set and V (G) itself.

Now let x ∈ GrBd and µBGˆ be a limit measure. As it pointed out in Section 3, the measure µBGˆ is concentrated on countable graphs with “broken” symmetries that is on graphs for which all the vertex colors are diﬀerent. In this case, the component of x in the Borel graphing GGˆ is isomorphic to the underlying graph of x. Of course, if the underlying graph of x is transitive and all the vertex colors are identical, then the component of x is just one single vertex. In this case, we lose all the information about the graph structure of x. If the colors on the r-ball around the root of x are diﬀerent, then we know at least that the r-ball around the root of x and the r-ball around x in the graphing are isomorphic.

In order to handle the color issue, we need a simple variation of Udr,B. Let s > r be an integer. Then Udr,s,B is the set of r-balls with vertices colored by {0,1}-strings of length s. Obviously, Udr,r,B = Udr,B. Let Wdr,s,B ⊂ Udr,s,B be the set of balls for which the vertex colors are all diﬀerent. Let Vdr,s,B = Udr,s,B\Wdr,s,B. The following lemma is an easy consequence of the law of large numbers and is left to the reader.

- Lemma 4.1. For any δ > 0 and r ≥ 1 there exists s > r such that

µGˆ ∪α∈V r,s,B

d

µBGˆ(T(α) < δ

for any convergent graph sequence Gˆ. Proposition 4.1. Let Gˆ = {Gn}∞n=1 ⊂ Gd be a convergent graph sequence and let GGˆ be its canonical limit graphing. If GGˆ is hyperﬁnite, then Gˆ is always a hyperﬁnite family.

Proof. Fix a constant δ > 0. Let N ⊂ GrBd be a Borel subset such that µGˆ(N) < δ and if we remove the edges incident to the vertices in N, then all the components of the resulting

subgraphing have size at most K. The goal is to prove that the graphs inherit this property. That is, if n is large enough, then there exists Pn ⊂ V (Gn), |Pn| < δ|(V (Gn)| such that if we remove the edges of Gn incident to the vertices of Pn, the resulting graph G′n has components of size at most K. The following approximation lemma is the key of the proof of Proposition 4.1.

- Lemma 4.2. Let Gˆ and K be as above. Then there exist integers s > r > K and a subset Vdr,s,B ⊂ A ⊂ Udr,s,B with the following property.


- • µGˆ(NA) < δ, where NA = ∪β∈AT(β) .
- • If we remove the edges of GGˆ incident to points in NA, the components of the resulting subgraphing T are of size at most K.


One can interpret the lemma in the following way. The hyperﬁniteness of GGˆ can be witnessed by the removal of edges incident to “nice” subsets. First, let us show that the lemma implies Proposition 4.1. Let t > s, t > 2r be an integer such that

µBGˆ(∪β∈V 2r,t,B

T(β)) < δ − µGˆ(NA).

d

Take a random coloring of the vertices of the graphs {Gn}∞n=1 by B. Let Hn ⊂ V (Gn) be the set of vertices x such that either Br(x) ∈ A or B2r(x) ∈ Vd2r,t,B . Remove the edges incident to Hn. Then in the resulting graph G′n the maximal component size is at most K. Indeed, suppose that there is a component of size greater than K and v ∈ K. Then B2r(v) ∈ Wd2r,t,B, thus the 2r-ball around v in Gn is isomorphic to the 2r-ball round the point z ∈ GrBd , where z ∈ T(α), α ∼ B2r(v). Observe, that by our construction, Br(x) ∩ G′n must be a subgraph of Br(z) ∩ T . Since the later graph does not contain components of size larger than K, neither does Br(x) ∩ G′n. Therefore the maximal component size in G′n is at most K. Now

- Proposition 4.1 follows from the fact that for any α ∈ Udr,s,B, limn→∞ p(Gn,α) = µGˆ(T(α)) with probability one.

Now let us prove Lemma 4.2. Let H ⊂ GrBd be a Borel subset, µGˆ(H) < δ such that if we remove the edges incident to H, the remaining components have size at most K. Since sets in the form NA, where A ⊂ Udl,B for some l > K generate the Borel sets of GrBd we have a sequence {NAl}∞l>K such that

- (1) lim


l→∞

µBGˆ(NAl△H) = 0.

Let Tl be the subgraphing obtained from the Borel graphing GGˆ by removing the edges incident to Nl. Let Xl be the set of points in GrBd that are in a component of Tl larger than K. Observe that liml→∞ µBGˆ(Xl) = 0. Pick s(l) > 2l in such a way that liml→∞ µGˆ(Pl) = 0, where Pl = ∪α∈V 2l,s(l),B

d

T(α). Let Ql = ∪βT(β), where the index β runs through all elements

of Wd2l,s,B such that the root of β is contained in a component of Tl larger than K. Note that it is meaningful, since by looking at the 2l-neighborhood of a vertex we can decide whether

it is contained in a component of Tl larger than K. Since Ql ⊆ Xl, liml→∞ µBGˆ(Ql) = 0. Hence if l is large enough then NA = NAl ∪Pl ∪Ql satisﬁes the conditions of the lemma (with r = 2l).

Now we prove the converse of Proposition 4.1.

- Proposition 4.2. Let Gˆ = {Gn}∞n=1 be a hyperﬁnite convergent graph sequence. Then the canonical limit GGˆ is hyperﬁnite.


Proof. As in the previous sections, let us color the vertices in the graph sequence randomly by B. Now we construct a second B-coloring of the vertices. The k-th digit of the second B-color of x ∈ V (Gn) is given the following way. Let Ck be an integer such that for any n ≥ 1 there exists a subset Hn,k ⊂ V (Gn), with |Hn,k||V (Gn)| < 1/k such that if we remove the edges incident to Hn,k, the components in the remaining graph Gn,k have size at most Ck. Let 0 be the k-th digit of x if x ∈ Hn,k, otherwise let the k-th digit be 1. This way we constructed a coloring of the graphs by B2. Note that for convergent B2 colorings we have limit measures on GrBd 2 completely analogously to B-colorings. We cannot say that the B2-colored graphs constructed above are convergent (as colored graphs). However, we have a convergent subsequence by compactness. Let µBGˆ2 be the associated limit measure on GrdB2. Then, π : GrBd 2 → GrBd is a factor map, where π forgets the second coordinate. Now let us observe that the graphing G(GrBd 2,µBGˆ2) is hyperﬁnite. Indeed, the Borel set of vertices with 0 as the k-th digit of their second B-coordinate has µBGˆ2 measure less than 1/k. Also, if we

remove the edges incident to this set the remaining graphing have components of size at most Ck. By Proposition 2.3, our proposition follows.

5. The proof of Theorem 1 and Theorem 2

We will show slightly more. Let H(X,µ) be an arbitrary graphing with vertex degree bound d, We can consider the associated unimodular measure the following way ([3],[4]). For each point x ∈ X let π(x) ∈ Grd be the component of x in H with x as the root. Then the measure π∗(µ) := µH is unimodular (see also Corollary 6.10 [4]). We can consider the Bernoulli measure [π∗(µ)]B := µBH on GrBd (see Section 3) and the corresponding graphing G(GrBd ,µBH). If G is weakly equivalent to H, then the associated Bernoulli measures and the corresponding graphings are the same. Hence by Proposition 2.3, the following lemma immediately implies Theorem 2.

- Lemma 5.1. There exists a graphing K such that H and G(GrBd ,µBH) are both factors of K.


Proof. First let us note that if the measure µH is concentrated on rooted graphs without rooted automorphisms, then H → G(Grd,µH) is already a factor map. In this case, the proof of Theorem 2. would end here. We use the Bernoullization only to handle the symmetries. This is the point in our paper, where we use the edge-colorings. By a result of Kechris, Solecki and Todorcevic [14] one can color the vertices of a Borel graphing of vertex degree bound d properly with d + 1-colors in a Borel way. This vertex coloring gives us a Borel edge coloring

- of H with d+12 -colors. The color of an edge between a vertex colored by a and a vertex colored by b will be colored by (a,b). As it was mentioned in Section 3, the coloring deﬁnes


a Borel Γ-action on X, where Γ is the free product of d+12 cyclic groups of order 2. Again, we have the natural Γ-equivariant map πC : X → CGrd. We denote (πC)⋆(µ) by µCH. Now let us consider the Bernoullization of µCH on CGrBd , µC,BH . We have two factor maps

- • ρ : G(CGrBd ,µC,BH ) → G(GrBd ,µBH) the map forgetting the edge-colorings.
- • ζ : G(CGrBd ,µC,BH ) → G(CGrd,µCH) the map forgetting the vertex-colorings.


Note that πC and ζ are both Γ-equivariant maps so, we can consider their relative independent joining [10] over CGrd. This gives us a new Γ-action on a space Y , with graphing K. By the joining construction, both H and G(CGrBd ,µC,BH ) are factors of K. On the other hand, G(GrBd ,µBH) is a factor of G(CGrBd ,µC,BH ). Thus both H and G(GrBd ,µBH) are factors of K. Hence the lemma follows.

Now let us observe that Theorem 1 immediately follows from Theorem 2 by Proposition

- 4.1 and Proposition 4.2.


6. Equipartitions

- 6.1. The Transfer Theorem. The Transfer Theorem is one of the basic applications of the Oracle Method.


- Theorem 6 (Transfer Theorem). Let Gˆ = {Gn}∞n=1 ⊂ Gd be a convergent graph sequence.


- Let H ⊆ GGˆ be a subgraphing (note that it means that V (H) = GrBd ). Then there exist subgraphs Hn ⊆ Gn, V (Gn) = V (Hn) such that {Hn}∞n=1 converges to H.


Proof. Recall that GGˆ = G(GrBd ,µGˆ). Also, for µGˆ-almost all elements x of GrBd the vertices of x are B-colored diﬀerently. Let us call such vertex x typical. Thus the orbit of a typical

vertex is isomorphic to the graph represented by x in GrBd . How can we encode the edge set of H ? A symbol σ consists of the following data. A number 0 ≤ k ≤ d, the degree of the symbol,

and a subset {a1 < a2 < ··· < al} of {1,2,... k}, where l ≤ k. For any edge (x,y) ∈ E(G), for which x is typical we have an “edge code” which is s is y is the s-th neighbour of x with respect to the lexicographical ordering of B. If x is a typical vertex, then its position in H can be described by the the symbol σ = (k,a1,a2,... ,al), where k is the degree of x in G and ai is the edge code of the i-th neighbor of x in H in the lexicographical ordering of the B-colors. We denote by Hσ the Borel set of typical vertices x with H-position symbol σ. Let E(Hσ) be the set of edges in G incident to an element of Hσ. Then, E(H) = ∪σE(Hσ). Note that the sets Hσ are disjoint.

As in Lemma 4.2 let Alσ ⊂ Udl,B such that

- • The degree of z ∈ Alσ is the degree of σ.
- • liml→∞ µBGˆ(NAl


△Hσ) = 0.

σ

We also suppose that the sets Alσ are disjoint. Then one can consider the approximating graphings Hl

E(Hl) = ∪σE([Alσ]σ),

where E([Alσ]σ) is the set of edges (z,w) such that z ∈ Alσ and the “edge code” of w belongs to σ. Then liml→∞ L(Hl) = L(H). Therefore it is enough to prove the Transfer Theorem for the subgraphings Hl. We construct the subgraphs {Hn}∞n=1 the following way. First, we B-color the vertices of the graphs Gn randomly to obtain the graph GBn . Then for each vertex v ∈ Gn we check the l-neighborhood of v. If for some σ, Bl(v) ∈ Alσ then using the symbol σ and the B-coloring we choose the appropriate edges of Gn incident to v. In this way we obtain the subgraph Hn. The following lemma ﬁnishes the proof of our theorem.

- Lemma 6.1. {Hn} converges to Hl with probability 1.


Proof. Let r > 0 and β ∈ Udr,B. It is enough to see that

- (2) lim


n→∞

p(Hn,β) = µBGˆ(T(Hl,β))

with probability 1. Let z ∈ GrBd , z ∈ T(γ),γ ∈ Wdr+l,s,B. Then γ determines whether z ∈ T(Hl,β) or not. We denote by Wd,r+1l,s,B the set of γ’s where z ∈ T(Hl,β). So, if v ∈ T(GBn ,γ), γ ∈ Wd,r+1l,s,B then v ∈ T(Hn,β) and if v ∈ T(GBn ,γ′), γ′ ∈ Wdr+l,s,B\Wd,r+1l,s,B,

- then v ∈/ T(Hn,β). Hence we have the following estimates.


p(GBn ,α) ≤ p(Hn,β) ≤

p(GBn ,α) +

p(Gn,α).

α∈Wd,r+1l,s,B

α∈Wd,r+1l,s,B

α′∈Vdr+l,s,B

and

µBGˆ(T(α)) ≤ µBGˆ(T(Hl,β)) ≤

µBGˆ(T(α)) +

µBGˆ(T(α)).

α∈Wd,r+1l,s,B

α∈Wd,r+1l,s,B

α′∈Vdr+l,s,B

Since

µBGˆ(T(α)) = 0

lim

s→∞

α′∈Vdr+l,s,B

the lemma follows from the fact that {Gn}∞n=1 is a convergent sequence.

- 6.2. The Uniformicity Theorem. Let P ⊂ Gd be a hyperﬁnite family. Denote by LP the set of graphings that are limit graphings of sequences in P. By Theorem 1, the elements of LP are hyperﬁnite graphings. The Uniformicity Theorem states that LP is a uniformly hyperﬁnite family of graphings.


- Theorem 7 (The Uniformicity Theorem). Let P ⊂ Gd be a hyperﬁnite family then for any ζ > 0 there exists K > 0 such that for each G ∈ LP there exists a Borel set Z ⊂ E(G) of edge-measure less than ζ such that the components of G\Z are of size at most K.


Let H(X,µ) be a hyperﬁnite graphing such that all of its components have size at most K. For a connected graph S of size at most K let cHS be the µ-measure of points in X that belong to a component isomorphic to S. Let {Hn}∞n=1 be a graph sequence converging to H and CSHn be the set of vertices in V (Hn) that belong to a component isomorphic to S.

- Lemma 6.2. If {Hn}∞n=1 and H are as above then limn→∞ cHSn = cHS .

Proof. Let Ud,Sk+1 be the set of elements of Udk+1 that are isomorphic to S. Note that these rooted balls are already in Udk. However, if the k +1-ball of a vertex is in Ud,Sk+1 then we know that the vertex is in a component isomorphic to S. Clearly,

S α∈Ud,Sk+1

µH(α) = 1,

where S is running through the isomorphic classes of connected graphs of size at most K. By convergence, for any S and any α ∈ Ud,Sk

lim

n→∞

p(Hn,α) = µH(T(α)). Observe that cHS = α∈Uk

d,S

p(Hn,α). Hence the lemma follows.

The proof of the next lemma is basically identical to the previous one.

- Lemma 6.3. Let {Hn}∞n=1 be a sequence of graphings such that limn→∞ L(Hn) = L(H), where H is as above. Then limn→∞ cHS n = cHS , for any S, |V (S)| ≤ K.

Now let Gˆ = {Gn}∞n=1 be a convergent graph sequence and let Z ⊂ E(GGˆ) be a Borel set

of edges with edge-measure less than ǫ > 0, such that the subgraphing H = GGˆ\Z consists of components of size at most K. For the rest of this section we consider this subgraphing

H. We will show that if a hyperﬁnite graphing G′ is statistically close to G then it contains a subgraphing H′ of components of size at most K, such that cHS is close to cHS ′ for any connected graph S, |V (S)| ≤ K. First we formulate this statement for ﬁnite graphs.

- Lemma 6.4. Let G,ˆ H,K be as above. Then for any δ > 0 there exists f(δ) > 0 such that if


for a ﬁnite graph G dstat(G,GGˆ) < f(δ) then G contains a subgraph H ⊂ G with components of size at most K such that

- (3) |cHS − cHS | < δ for all S,|V (S)| ≤ K.


Proof. Suppose that the lemma does not hold. Then we have a δ > 0 and a sequence of ﬁnite graphs Qˆ = {Qn}∞n=1 converging to GGˆ without subgraphs Hn satisfying (3). Observe that GQˆ = GGˆ. Thus, by the Transfer Theorem there exists subgraphs Hn′ ⊂ Qn converging

- to H. By Lemma 6.2, limn→∞ cHn′ = cHS , for any S. So, we have subgraphs Hn ⊂ Hn′


with components of size at most K such that limn→∞ cHSn = cHS for any S, leading to a contradiction.

- Lemma 6.5. Let K(X,µ) be a graphing such that all of its components are of size at most l. Let {Qn}∞n=1 be a sequence of graphs converging to K. Let Hn ⊂ Qn be subgraphs with

components of size at most K such that for all n ≥ 1, |cHSn − cHs | < δ/4, where H is the subgraphing as above. Then there exists a subgraphing H′ ⊂ K with components of size at

most K, such that |cHS − cHS ′| < δ/2 for all connected graph S, |V (S)| ≤ K. Proof. Let L be a connected graph, |V (L)| ≤ l. Let CS,LQn be the set of points in Qn that are in a component C of Qn such that C ∩ L ∼= S. Set cQS,Ln = C

Qn S,L

![image 9](<2012-elek-finite-graphs-amenability_images/imageFile9.png>)

|V (Qn)|. Then S cQS,Ln = cQLn. Pick a subsequence {Qnk}∞n=1 such that for all S, L, limn→∞ cS,LQnk = dS,L exists. Then

S dS,L = CLK. Let CLK be the set of points in X that are in a component of K isomorphic to L. Then µ(CLK) = cKL. Divide CLK into Borel subsets such that

- • µ(CS,LK ) = dS,L.
- • Each component of CS,LK is isomorphic to L.


Let HS,LK be a Borel graph on CS,LK , such that its edges are edges of K and all the components are isomorphic to S. Let H′ be the union of all these graphs. Then

lim

k→∞

cHSnk = cHS ′ for any S, |V (S)| ≤ K. Thus the subgraphing H′ satisﬁes the conditions of our lemma.

Now we prove the analogue of Lemma 6.4 for graphings.

- Lemma 6.6. Let G,ˆ H,K be as above. Then for any δ > 0 there exists g(δ) > 0 such that


if for a hyperﬁnite graphing G′, dstat(G′,GGˆ) < g(δ) then G′ contains a subgraphing H′ ⊂ G′ with components of size at most K such that

- (4) |cHS ′ − cHS | < δ for all S,|V (S)| ≤ K


Proof. Let dstat(G′,GGˆ) < f(δ/2)/2, where f is the function in Lemma 6.4. Since G′ is hyperﬁnite, it has a subgraphing K ⊂ G′ consisting of components of size not greater than

some constant l > 0. Let us choose a graph sequence {Qn}∞n=1 such that

- • {Qn}∞n=1 converges to K.
- • dstat(K,Qn) < f(δ/2 2) for all n ≥ 1.


![image 10](<2012-elek-finite-graphs-amenability_images/imageFile10.png>)

Therefore, dstat(G,Qn) < f(δ/2) holds for all n ≥ 1. Hence by Lemma 6.4, there exist subgraphs Hn ⊂ Qn with components of size at most K such that |cHSn − cHS | < δ/2 for any S, |V (S)| ≤ K. By Lemma 6.5, we have a subgraphing H′ ⊂ K with components of size at most K satisfying (4).

Now we ﬁnish the proof of our theorem. Observe that L(LP) ⊂ [0,1]N is a compact set. Call a hyperﬁnite graphing G an (ǫ,K)-graphing if one can remove an edge set of edge-measure ǫ

to obtain a subgraphing with components of size at most K. By Lemma 6.6, if G ∈ LP is an (ǫ,K)-graphing then if dstat(G,G′) is small enough then G′ is an (2ǫ,K)-graphing. So, the theorem follows from compactness.

Remark: The reader might ask, whether if P is a hyperﬁnite family of (ǫ,K)-graphs, then what is the best constant in the Uniformicity Theorem. As a matter of fact, any constant ǫ′ > ǫ is good. Indeed, if {Qn}∞n=1 ⊂ P is a convergent sequence of (ǫ,K)-graphs, then according to the construction in Proposition 4.2 there exists an (ǫ′,K)-good limit graphing. So, ǫ′ is a good constant for the Uniformicity Theorem by Theorem 3.

- 6.3. The proof of the Equipartition Theorem. By the Uniformicity Theorem, all elements of LP are (ǫ,K)-graphings for some K > 0. Suppose that the theorem does not hold

for some δ > 0. Then we have a sequence of graphs {Gn}∞n=1,{Hn}∞n=1 ⊂ Gd such that limn→∞ dstat(Gn,Hn) = 0, without having pairs {G′n,Hn′ }∞n=1 satisfying the requirement of the theorem. Let us pick a convergent graph sequence Gˆ = {Gnk}∞k=1. Then {Hnk}∞k=1 tends to GGˆ as well. Let H ⊂ GGˆ be a subgraphing with components of size at most K. By the Transfer Theorem, we have subgraphs {G′n

k

⊂ Gnk}∞k=1, {Hn′

k

⊂ Hnk}∞k=1 converging to H. By Lemma 6.4, we can suppose that all the components of G′n

k

and Hn′

k

have size at most K. Then for large enough k,

|E(Gnk)\E(G′n

k

)| ≤ 2ǫ|E(Gnk)| and |E(Hnk)\E(Hn′

k

)| ≤ 2ǫ|E(Hnk)| Also,

S

|cG

′ nk

S − cHS | <

δ 2

![image 11](<2012-elek-finite-graphs-amenability_images/imageFile11.png>)

and

S

|cH

′ nk

S − cHS | <

δ 2

![image 12](<2012-elek-finite-graphs-amenability_images/imageFile12.png>)

leading to a contradiction.

- 6.4. The proof of Theorem 5. Let ǫ > 0, κ > 0 be constants such that (2ǫd + κd) < δ.


Suppose that dstat(G,H) < f(κ), where f is the function in the Equipartition Theorem. So, we have subgraphs G′ ⊂ G, H′ ⊂ H such that

- • S |cGS′ − cHS ′| < κ.
- • |E(G)\E(G′)| < 2ǫ|E(G)| ≤ ǫdn
- • |E(H)\E(H′)| < 2ǫ|E(H)| ≤ ǫdn


Then if cGS′ ≤ cHS ′, we deﬁne ρ : CSG′ → CSH′ to be a component preserving injective map. On the other hand, if cGS′ ≥ cHS ′, then let DSG′ ⊂ CSG′ be a union of some components such that |CSH′| = |DSG′| and deﬁne ρ : DSG′ → CSH′ to be a component preserving bijection. Finally, extend ρ to V (G) arbitrarily. Observe that

|ρ−1(E(H))△E(G)| ≤ (2ǫd + κd)n

7. Local-global convergence

The notion of local-global convergence was introduced by Hatami, Lov´asz and Szegedy [12] (and independently by Bollob´s and Riordan [5] under the name of convergence in the partition metric).

First, let us recall the deﬁnition. For k ≥ 2, let Udr,k be the ﬁnite set of rooted r-balls H with vertex labelings c : V (H) → {1,2,... ,k} = [k]. Let G ∈ Gd be a ﬁnite graph. One can associate to a labeling c a probability distribution Pc on Udr,k, where Pc(γ) = p(G,c,γ),

and p(G,c,γ) is the probability that the r-neighborhood of a random vertex of G is labeledisomorphic to γ. Set

r,k

Ck(G) := ∪c:V(H)→[k] ⊂ [0,1]U

d .

The k-th partition pseudodistance of G and H is dk(G,H) := dhaus(Ck(G),Ck(H)), where dhaus is the Hausdorﬀ-distance. The local-global pseudodistance of G and H is given by dLG(G,H) = ∞k=1 21kdk(G,H). We can extend the local-global pseudodistance to graphings,

![image 13](<2012-elek-finite-graphs-amenability_images/imageFile13.png>)

- as well. Let G(X,µ) be a graphing of vertex degree bound d and c : X → [k] be a Borel function. Then Pc(γ) = µ(T(G,c,γ)), where (T(G,c,γ)) is the set of vertices in X with rneighborhood isomorphic to γ (under the labeling induced by c). Let Ck(G) be the closure of the set ∪cPc ⊂ [0,1]Udr,k and the local-global pseudodistance can be deﬁned as in the case of ﬁnite graphs. A graph sequence {Gn}∞n=1 converges locally-globally to a graphing G if


for any k ≥ 1, {Ck(Gn)}∞n=1 converges to Ck(G) in the Hausdorﬀ distance. Although in general, local-global convergence is much stronger than the Benjamini-Schramm convergence,

for hyperﬁnite sequences the two notions coincide (see also Theorem 9.5 [12]).

- Theorem 8. If {Gn}∞n=1 is a hyperﬁnite graph sequence converging to G then it converges to


- G locally-globally.


Proof. The following lemma is straightforward and left for the reader. It states that a small perturbation of a graph is close to the original graph in the local-global distance.

- Lemma 7.1. For any ǫ > 0, there exists δ > 0 such that


- • If G ∈ Gd, H ⊂ G, V (H) = V (G) and |E|V(G(G\H)|)| < δ then dLG(G,H) < ǫ.

![image 14](<2012-elek-finite-graphs-amenability_images/imageFile14.png>)

- • If G(X,µ) is a graphing, H ⊂ G, V (H) ⊂ V (G) and µE(G\H) < δ then dLG(G,H) < ǫ.


- Lemma 7.2. Let H(X,µ) be a graphing with components of size at most K. Let {Hn}∞n=1 ⊂ Gd be graphs with components of size at most K converging to H. Then limn→∞ dLG(Hn,H) = 0.


Proof. By Lemma 6.3, limn→∞cHSn = cHS for any S, |V (S)| ≤ K. Let M(K,S,k) be the set of all non-isomorphic k-labelings of S. A Borel map c : X → [k] determines a probability

distribution on M(K,S,k), where Pc(β) = µH(T(β)). Clearly, for any ǫ > 0 there exists δ > 0 if |cHSn − cHS | < δ then we can partition CSHn into parts CSHn = ∪β∈M(K,S,k)L(β) such that |VL((Hβ)

n) − Pc(β)| < ǫ. Conversely, for any ǫ > 0 there exists δ > 0 such that if |cHSn − cHS | < δ and cHSn = β∈M(K,S,k) l(β), l(β) ≥ 0, then one can divide CSH into Borel parts CSH = ∪β∈M(K,S,k)R(β) in such a way that each component of R(β) is a component of CSH and |µ(R(β)) − l(β)| < ǫ. Hence the lemma follows, since the ǫ-ball around Ck(H) contains Ck(Hn) and vice versa, the ǫ-ball around Ck(Hn) contains Ck(H).

![image 15](<2012-elek-finite-graphs-amenability_images/imageFile15.png>)

Now we ﬁnish the proof of our theorem. By Lemma 7.1 and Lemma 6.4, we have H ⊂ G and {Hn ⊂ Gn}∞n=1 such that

dLG(G,H) <

ǫ 3

ǫ 3

, dLG(Gn,Hn) <

.

![image 16](<2012-elek-finite-graphs-amenability_images/imageFile16.png>)

![image 17](<2012-elek-finite-graphs-amenability_images/imageFile17.png>)

Hence if n is large, then dLG(G,Gn) < ǫ.

8. Strong equivalence

- 8.1. The proof of Theorem 3. First we deﬁne a new pseudo-distance for graphings. Let


G(X,µ), H(Y,ν) be graphings of vertex degree bound d. Then let dstrong(G,H) be the inﬁmum of ǫ′s such that there exists a measure preserving bijection ρ : X → Y with

µE(ρ−1(E(H))△E(G)) ≤ ǫ. So, G and H is strongly equivalent if dstrong(G,H) = 0.

- Lemma 8.1. Let H1(X,µ), H2(Y,ν) be graphings of degree bound d with components of size


- at most K. Suppose that


|cHS 1 − cHS 2| < κ. Then dstrong(H1,H2) < dκ.

S,|V (S)|≤K

Proof. Let S be a connected graph of size at most K. If cHS 1 ≤ cHS 2, then deﬁne ρ : CSH1 → CSH2 to be an injective map preserving the components such that ν(ρ(A)) = µ(A) if A ⊂ CSH1 is a measurable set. On the other hand, if cHS 1 > cHS 2, then let DSH1 be a Borel set of X such that

- • The components of DSH1 are components of CSH1.
- • µ(DSH1) = cHS 2.


Deﬁne ρ : DSH1 → CSH2 to be a measure-preserving bijection (that also preserves the components). Then, extend ρ to a measure-preserving bijection arbitrarily onto the whole space X.

Then µE(ρ−1(E(H2))△E(H1)) ≤ dκ.

Now let us ﬁnish the proof of Theorem 3. Let Z ⊂ G be a set of edges of edge-measure less than ǫ/4, such that the components of K = G\Z are of size at most K. Then by the deﬁnition of dstat respectively by Lemma 6.6, there exists some δ > 0 such that

- • dstat(G,H) < δ, then |µE(G) − νE(H)| < ǫ/4.
- • dstat(G,H) < δ, then H contains a subgraphing K′ such that S,|V(S)|≤K |cKS − cKS′| <


ǫ 4d.

![image 18](<2012-elek-finite-graphs-amenability_images/imageFile18.png>)

By the previous lemma,

- (5) dstrong(K,K′) < ǫ/4 By (5), |µE(K) − νE(K′)| < ǫ/4. Thus


ǫ 4

ǫ 4

ǫ 2

dstrong(G,H) ≤ dstrong(K,K′) + µE(G\K) + µE(H\K′) ≤

≤ ǫ

+

+

![image 19](<2012-elek-finite-graphs-amenability_images/imageFile19.png>)

![image 20](<2012-elek-finite-graphs-amenability_images/imageFile20.png>)

![image 21](<2012-elek-finite-graphs-amenability_images/imageFile21.png>)

8.2. Rokhlin Lemma for non-free actions. Let Γ be a ﬁnitely generated amenable group with a symmetric generating system. Ornstein and Weiss [18] proved the following version of the classical Rokhlin Lemma. If Γ (X,µ), Γ (Y,ν) are two probability measure preserving essentially free actions, then they are strongly equivalent. That is for any ǫ > 0 there exists a measure preserving bijection ρǫ : X → Y such that

µ({x ∈ X, | ρǫ(sx) = sρǫ(x) for any s ∈ S }) > 1 − ǫ. The goal of this subsection is to show how one can deduce the general (non-free) version of the statement above using Theorem 3. First, let us recall the notion of the type of an action ([2], [20]). Let Fn be the free group on n-generators {s1,s2,... ,sn}. Let α = Fn (X,µ) be a not necessarily free action of Fn. Note that any free action of an n-element generated group

Γ can be viewed as a non-free action of Fn. Let Σn be the space of all rooted Schreier graphs of transitive actions of Fn on countable sets. Note that the elements of Σn are connected rooted graphs with edge labels from {s1,s2,... ,sn,s−1 1,s−2 1,... ,s−n1} where the edge (x,six) is labeled by si. The space Σn is compact and Fn acts on Σn continuously by changing the roots. Following [1], we call the Fn-invariant measures on Σn invariant random subgroups (IRS). Let α : Fn (X,µ) be a p.m.p. Borel action. The type of α is an IRS deﬁned the following way. Let πα : X → Σn be the map that maps x ∈ X to the Schreier graph of its orbit (with root x). The type of α, type(α) is the invariant measure (πα)⋆(µ). Now we state the non-free version of the amenable Rokhlin Lemma. Note that a version (stably weak equivalence of the actions) of the result is proved in [20, Theorem 1.8].

- Theorem 9. If α,β : Fn (X,µ) are hyperﬁnite actions (the underlying graphings are hyperﬁnite) and type(α) = type(β) then α and β are strongly equivalent.


Proof. The idea of the proof is that for each action α we construct an (unlabeled) graphing Gα such that type(α) = type(β) if and only if dstat(Gα,Hα). One should note that if the orbits have no rooted automorphisms, then the graphing of α would ﬁt for this purpose. Again, we only need to handle the symmetries. First, let Gα(X,µ) be the graphing of our action. We will “add” marker graphs to Gα in order to encode the action. The marker graph for si is a path Pi of path-length i (that is of i + 1-vertices). The additional marker graph for a vertex in X is the path Pn+1. The construction of Gα goes as follows.

- Step 1. Stick a graph Pn+1 to each vertex of x ∈ X (the vertices of X will be called “original” vertices). This means that we identify an endpoint of Pn+1 with x. In this way, we obtain

a new graphing G1α(X1,µ1). Here X1 is the union of n + 2-copies of X. We normalize µ1 in order to get a probability measure.

- Step 2. Now we divide each edge (x,six) of the original graphing Gα into three parts by adding two new vertices. In this way, we obtain the graphing G2 from G1. Note that if x = six we do not make any subdivison (we do not consider loops). Also, if six = sjx then the edges (x,six) and (x,sjx) coincide.
- Step 3. In the ﬁnal step we encode the action. For each 1 ≤ i ≤ n we stick a marker graph Pi to the vertex next to x on the path x,six, where x is an original vertex. The resulting graphing is Gα(Xα,µα) (the fact that it is measure-preserving Borel graph follows immediately from the invariance of the action α). By looking at the 3n-ball around a vertex of Xα we can see whether it is an original vertex or not. In fact by looking at the 3nr-ball around such a vertex we can reconstruct the labeled r-ball of the original labeled graphing Gα. It is not hard to see that type(α) = type(β) if and only if dstat(Gα,Gβ) = 0. Hence if type(α) = type(β), by Theorem 3, Gα is strongly equivalent to Gβ. This implies the strong equivalence of the actions α and β. .


References

- [1] M. Ab´ert, Y. Glasner and B. Virag´ , Kesten’s theorem for invariant random subgroups, ( preprint) http://arxiv.org/abs/1201.3399
- [2] M. Ab´ert, G. Elek, The Space of Actions, Partition Metric and Combinatorial Rigidity, (preprint) http://arxiv.org/abs/1108.2147


- [3] D.Aldous and R. Lyons, Processes on unimodular random networks. Electron. J. Probab. 12 no. 54

(2007) 1454-1508.

- [4] I. Artemenko, Graphings and unimodularity, The Waterloo Math. Rev 1 no. 3 (2011) 17–31.
- [5] B. Bollobas´ and O. Riordan, Sparse graphs: metrics and random models. Random Structures and Algorithms 39 no. 1 (2010) 1–38.
- [6] I. Benjamini, O. Schramm and A. Shapira Every minor-closed property of sparse graphs is testable.Adv. Math. 223 (2010) no. 6 2200–2218.
- [7] G. Elek, On limits of ﬁnite graphs. Combinatorica 27 (2007) no. 4 503–507.
- [8] G. Elek, Parameter testing in bounded degree graphs of subexponential growth. Random Structures and Algorithms 37 (2010) no. 2 248–270.
- [9] G. Elek, L2-spectral invariants and convergent sequences of ﬁnite graphs. Journal of Funct. Anal. 254

(2008) no. 10 2667-2689.

- [10] E. Glasner, Ergodic theory via joinings. Mathematical Surveys and Monographs, 101. American Mathematical Society, Providence, RI, (2003).
- [11] A. Hassidim, J. A. Kelner, H.N. Nguyen and K. Onak, Local graph partitions for approximation and testing. FOCS 2009 22–31, IEEE Comp.Soc
- [12] H. Hatami, L. Lovasz´ and B. Szegedy, (preprint) http://arxiv.org/pdf/1205.4356v1.pdf
- [13] V. Kaimanovich, Amenability, hyperﬁniteness, and isoperimetric inequalities. C. R. Acad. Sci. Paris Sr. I Math. 325 (1997), no. 9, 999–1004.
- [14] A. S. Kechris, S. Solecki and S. Todorcevic, Borel chromatic numbers. Adv. Math. 141 (1999), no. 1, 1–44.
- [15] A. S. Kechris and B.D. Miller, Topics in orbit equivalence. Lecture Notes in Mathematics 1852 Springer Verlag (2004)
- [16] (personal communication)
- [17] I. Newman and C. Sohler, Every property of hyperﬁnite graphs is testable. STOC 2011 675–684.
- [18] D. S. Ornstein and B. Weiss, Entropy and isomorphism theorems for actions of amenable groups. J. Analyse Math. 48 (1987), 1–141.
- [19] O. Schramm, Hyperﬁnite graph limits. Electron. Res. Announc. Math. Sci. 15 (2008), 17-23.
- [20] R.D. Tucker-Drob, Weak equivalence and non-classifyability of measure preserving actions. (preprint) http://arxiv.org/abs/1202.3101


Alfred Renyi Institute of the Hungarian Academy of Sciences and Ecole´ Polytechnique Fe´de´rale de Lausanne, EPFL

elek@renyi.hu

