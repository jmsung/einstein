# arXiv:1207.0638v3[math.CO]19May2013

## Isoperimetric Inequalities in Simplicial Complexes

Ori Parzanchevski, Ron Rosenthal and Ran J. Tessler November 27, 2024

Abstract

In graph theory there are intimate connections between the expansion properties of a graph and the spectrum of its Laplacian. In this paper we deﬁne a notion of combinatorial expansion for simplicial complexes of general dimension, and prove that similar connections exist between the combinatorial expansion of a complex, and the spectrum of the high dimensional Laplacian deﬁned by Eckmann. In particular, we present a Cheeger-type inequality, and a high-dimensional Expander Mixing Lemma. As a corollary, using the work of Pach, we obtain a connection between spectral properties of complexes and Gromov’s notion of geometric overlap. Using the work of Gunder and Wagner, we give an estimate for the combinatorial expansion and geometric overlap of random Linial-Meshulam complexes.

### 1 Introduction

It is a cornerstone of graph theory that the expansion properties of a graph are intimately linked to the spectrum of its Laplacian. In particular, the discrete Cheeger inequalities [Tan84, Dod84, AM85, Alo86] relate the spectral gap of a graph to its Cheeger constant, and the Expander Mixing Lemma [FP87, AC88, BMS93] relates the extremal values of the spectrum to discrepancy in the graph (see (1.4)) and to its mixing properties.

In this paper we deﬁne a notion of expansion for simplicial complexes, which generalizes the Cheeger constant and the discrepancy in graphs. We then study its relations to the spectrum of the high dimensional Laplacian deﬁned by Eckmann [Eck44], and present a high dimensional Cheeger inequality and a high dimensional Expander Mixing Lemma.

This study is closely related to the notion of high dimensional expanders. A family of graphs {Gi} with uniformly bounded degrees is said to be a family of expanders if their Cheeger constants h(Gi) are uniformly bounded away from zero. By the discrete Cheeger inequalities (1.3), this is equivalent to having their spectral gaps λ(Gi) uniformly bounded away from zero. Thus, combinatorial expanders and spectral expanders are equivalent notions. We refer to [HLW06, Lub12] for the general background on expanders and their applications.

It is desirable to have a similar situation in higher dimensions, but at least as of now, it is not clear what is the “right” notion of “high dimensional expander”. One generalization of the Cheeger constant to higher dimensions is the notion of coboundary expansion, originating in [LM06, Gro10], and studied under various names in [MW09, DK10, MW11, GW12, SKM12, NR12]. While in dimension one it coincides with the Cheeger constant, its combinatorial meaning is somewhat vague in higher dimensions. Furthermore, it is shown in [GW12] that there exist, in any dimension greater than one, complexes with spectral gaps bounded away from zero† and arbitrarily small coboundary

† The spectral gap of a complex is deﬁned in Section 2.1.

expansion; In [SKM12] the other direction is settled: there exist coboundary expanding complexes with arbitrarily small spectral gaps.

Another notion of expansion is Gromov’s geometric overlap property, originating in [Gro10] and studied in [FGL+11, MW11]. This notion was shown in [Gro10, MW11] to be related to coboundary expansion. However, even in dimension one it is not equivalent to that of expander graphs.

Our deﬁnition of expansion suggests a natural notion of “combinatorial expanders”, and we show that spectral expanders with complete skeletons are combinatorial expanders. A theorem of Pach [Pac98] shows that this notion of combinatorial expansion is also connected to the geometric overlap property. As an application of our main theorems we analyze the Linial-Meshulam model of random complexes, and show that for suitable parameters they form combinatorial and geometric expanders.

- 1.1 Combinatorial expansion and the spectral gap The Cheeger constant of a ﬁnite graph G = (V, E) on n vertices is usually taken to be


ϕ(G) = min

A⊆V 0<|A|≤ n

2

|E (A,V\A)| |A|

where E (A, B) is the set of edges with one vertex in A and the other in B. In this paper, however, we work with the following version:

n|E (A,V\A)| |A||V\A|

h(G) = min

. (1.1)

0<|A|<n

Since ϕ(G) ≤ h(G) ≤ 2ϕ(G), deﬁning expanders by ϕ or by h is equivalent.

The spectral gap of G, denoted λ(G), is the second smallest eigenvalue of the Laplacian ∆+ : RV → RV, which is deﬁned by

∆+ f (v) = deg(v) f (v) −

f (w). (1.2)

w∼v

The discrete Cheeger inequalities [Tan84, Dod84, AM85, Alo86] relate the Cheeger constant and the spectral gap:

h2 (G)

8k ≤ λ(G) ≤ h(G), (1.3) where k is the maximal degree of a vertex in G.† In particular, the bound λ ≤ h shows that spectral expanders are combinatorial expanders. This proved to be of immense importance since the spectral gap is approachable by many mathematical tools (coming from linear algebra, spectral methods, representation theory and even number theory - see e.g. [Lub10, Lub12] and the references within). In contrast, the Cheeger constant is usually hard to analyze directly, and even to compute it for a given graph is NP-hard [BKV+81, MS90].

Moving on to higher dimension, let X be an (abstract) simplicial complex with vertex set V. This means that X is a collection of subsets of V, called cells (and also simplexes, faces, or hyperedges), which is closed under taking subsets, i.e., if σ ∈ X and τ ⊆ σ, then τ ∈ X. The dimension of a cell σ is dimσ = |σ| − 1, and Xj denotes the set of cells of dimension j. The dimension of X is the maximal dimension of a cell in it. The degree of a j-cell (a cell of dimension j) is the number of (j + 1)-cells which contain it. Throughout this paper we denote by d the dimension of the complex at hand, and

† For ϕ they are given by ϕ22(kG) ≤ λ(G) ≤ 2ϕ(G).

by n the number of vertices in it. We shall occasionally add the assumption that the complex has a complete skeleton, by which we mean that every possible j-cell with j < d belongs to X.

We deﬁne the following generalization of the Cheeger constant: Deﬁnition 1.1. For a ﬁnite d-complex X with n vertices V,

n · |F (A0, A1,..., Ad)| |A0| · |A1| · ... · |Ad|

h(X) = min

,

V= di=0 Ai

where the minimum is taken over all partitions of V into nonempty sets A0,..., Ad, and F (A0,..., Ad) denotes the set of d-dimensional cells with one vertex in each Ai.

For d = 1, this coincides with the Cheeger constant of a graph (1.1). To formulate an analogue of the Cheeger inequalities, we need a high-dimensional analogue of the spectral gap. Such an analogue is provided by the work of Eckmann on discrete Hodge theory [Eck44]. In order to give the deﬁnition we shall need more terminology, and we defer this to Section 2.1†. The basic idea, however, is the same as for graphs, namely, the spectral gap λ(X) is the smallest nontrivial eigenvalue of a suitable Laplace operator. The following theorem, whose proof appears in Section 4.1, generalizes the upper Cheeger inequality to higher dimensions:

Theorem 1.2 (Cheeger Inequality). For a ﬁnite complex X with a complete skeleton, λ(X) ≤ h(X). Remarks.

- (1) If the skeleton of X is not complete, then h(X) = 0, since there exist some {v0,...,vd−1} Xd−1, and then F ({v0},{v1},...,{vd−1},V\{v0,...,vd−1}) = 0. This suggests that a diﬀerent deﬁnition of h is called for, and we propose one in Section 5.
- (2) For a discussion of a possible lower Cheeger inequality, see Section 4.2.


In [LM06] Linial and Meshulam introduced the following model for random simplicial complexes: for a given p = p(n) ∈ (0,1), X (d,n, p) is a d-dimensional simplicial complex on n vertices, with a complete skeleton, and with every d-cell being included independently with probability p. Using the analysis of the spectrum of X (d,n, p) in [GW12], we show the following:

Corollary 1.3. The Linial-Meshulam complexes satisfy the following:

- (1) For large enough C, a.a.s. h X d,n, Clogn n ≥ C − O √C logn.

- (2) For C < 1, a.a.s. h X d,n, Clogn n = 0. The proof appears in Section 4.5, as part of Corollary 4.6.


#### 1.2 Mixing and discrepancy

The Cheeger inequalities (1.1) bound the expansion along the partitions of a graph, in terms of its spectral gap. However, the spectral gap alone does not suﬃce to determine the expansion between arbitrary sets of vertices. For example, the bipartite Ramanujan graphs constructed in [LPS88] are regular graphs with very large spectral gaps, which are bipartite. This means that they contain disjoint sets A, B ⊆ V of size n4, with E (A, B) = ∅. It turns out that control of the expansion between any two

† The spectral gap appears in Deﬁnition 2.1, and is given alternative characterizations in Propositions 2.2 and 3.3.

sets of vertices is possible by observing not only the smallest nontrivial eigenvalue of the Laplacian, but also the largest one†. In particular, the so-called Expander Mixing Lemma ([FP87, AC88, BMS93], see also [HLW06]) states that for a k-regular graph G = (V, E), and A, B ⊆ V,

k |A||B|

|E (A, B)| −

n ≤ ρ · |A||B|, (1.4) where ρ is the maximal absolute value of a nontrivial eigenvalue of kI − ∆+.

The deviation of |E (A, B)| from its expected value p|A||B|, where p = nk ≈ |E|/(n2) is the edge density, is called the discrepancy of A and B. This is a measure of quasi-randomness in a graph, a notion closely related to expansion (see e.g. [Chu97]). In a similar fashion, if k is the average degree of a (d − 1)-cell in X, we call the deviation

Xd n d+1

k |A0| · ... · |Ad| n

· |A0| · ... · |Ad| ≈ |F (A0,..., Ad)| −

|F (A0,..., Ad)| −

the discrepancy of A0,..., Ad (the question of using |Xd|

(d+n1) or nk is addressed in Remark 4.3). The following theorem generalizes the Expander Mixing Lemma to higher dimensions: Theorem 1.4 (Mixing Lemma). If X is a d-dimensional complex with a complete skeleton, then for any disjoint sets of vertices A0,..., Ad one has

k · |A0| · ... · |Ad| n ≤ ρ · (|A0| · ... · |Ad|)d+d1 ,

|F (A0,..., Ad)| −

where k is the average degree of a (d − 1)-cell in X, and ρ is the maximal absolute value of a nontrivial eigenvalue of kI − ∆+.

Here ∆+ is the Laplacian of X, which is deﬁned in Section 2. The proof, and a formal deﬁnition of ρ, appear in Section 4.3.

A related measure of expansion in graphs is given by the convergence rate of the random walk on it. As for the discrepancy, it is not enough to bound the spectral gap but also the higher end of the Laplace spectrum in order to understand this expansion. For example, on the bipartite graphs mentioned earlier the random walk does not converge at all. In [PR12] we suggest a generalization of the notion of random walk to general simplicial complexes, and study its connection to the spectral properties of the complex.

#### 1.3 Geometric overlap

If a graph G = (V, E) has a large Cheeger constant, then given a mapping ϕ : V → R, there exists a point x ∈ R which is covered by many edges in the linear extension of ϕ to E (namely, x = median({ϕ(v)|v ∈ V}). This observation led Gromov to deﬁne the geometric overlap of a complex [Gro10]:

- Deﬁnition 1.5. Let X be a d-dimensional simplicial complex. The overlap of X is deﬁned by


# σ ∈ Xd x ∈ conv{ϕ(v)|v ∈ σ} Xd

overlap(X) = min

max

.

ϕ:V→Rd

x∈Rd

† Graphs having both of them bounded are referred to as “two-sided expanders” in [Tao11].

In other words, X has overlap ≥ ε if for every simplicial mapping of X into Rd (a mapping induced linearly by the images of the vertices), some point in Rd is covered by at least an ε-fraction of the d-cells of X.

A theorem of Pach [Pac98], together with Theorem 1.4 yield a connection between the spectrum of the Laplacian and the overlap property.

- Corollary 1.6. Let X be a d-complex with a complete skeleton, and denote the average degree of a (d − 1)-cell in X by k. If the nontrivial spectrum of the Laplacian of X is contained in [k − ε,k + ε], then

overlap(X) ≥

cdd ed+1

cd −

ε(d + 1) k

,

where cd is Pach’s constant from [Pac98].

The proof appears in Section 4.4. As an application of this corollary, we show that LinialMeshulam complexes have geometric overlap for suitable parameters:

- Corollary 1.7. There exist ϑ > 0 such that for large enough C a.a.s. overlap X d,n, C·logn n > ϑ. Again, this is a part of Corollary 4.6, which is proved in Section 4.5.


The structure of the paper is as follows: in Section 2 we present the basic deﬁnitions relating to simplicial complexes and their spectral theory. Section 3 is devoted to proving basic properties of the high dimensional Laplacians. In Section 4 we prove the theorems and corollaries stated in the introduction, and discuss the possibility of a lower Cheeger inequality. Finally, Section 5 lists some open questions.

Acknowledgement. The authors would like to thank Alex Lubotzky for initiating our study of spectral expansion of complexes. We would also like to express our gratitude for the suggestions made to us by Noam Berger, Konstantin Golubev, Gil Kalai, Nati Linial, Doron Puder, Doron Shafrir, Uli Wagner, and Andrzej Zuk.˙ We are thankful for the support of the ERC.

### 2 Notations and deﬁnitions

Recall that X denotes a ﬁnite d-dimensional simplicial complex with vertex set V of size n, and that Xj denotes the set of j-cells of X, where −1 ≤ j ≤ d. In particular, we have X−1 = {∅}. For j ≥ 1, every j-cell σ = σ0,...,σj has two possible orientations, corresponding to the possible orderings of its vertices, up to an even permutation (1-cells and the empty cell have only one orientation). We denote an oriented cell by square brackets, and a ﬂip of orientation by an overbar. For example, one orientation of σ = {x,y,z} is x,y,z , which is the same as y,z, x and z, x,y . The other orientation of σ is x,y,z = y, x,z = x,z,y = z,y, x . We denote by X±j the set of oriented j-cells (so that

X±j = 2 Xj for j ≥ 1 and X±j = Xj for j = −1,0).

We now describe the discrete Hodge theory due to Eckmann [Eck44]. This is a discrete analogue of Hodge theory in Riemannian geometry, but in contrast, the proofs of the statements are all exercises in ﬁnite-dimensional linear algebra. Furthermore, it applies to any complex, and not only to manifolds.

The space of j-forms on X, denoted Ωj (X), is the vector space of skew-symmetric functions on oriented j-cells:

Ωj = Ωj (X) = f : X±j → R f (σ) = −f (σ) ∀σ ∈ X±j .

In particular, Ω0 is the space of functions on V, and Ω−1 = R{∅} can be identiﬁed in a natural way with R. We endow each Ωi with the inner product

f (σ)g(σ) (2.1)

##### f,g =

σ∈Xi

(note that f (σ)g(σ) is well deﬁned even without choosing an orientation for σ).

For a cell σ (either oriented or non-oriented) and a vertex v, we write v ∼ σ if v σ and {v} ∪ σ is a cell in X (here we ignore the orientation of σ). If σ = σ0,...,σj is oriented and v ∼ σ, then vσ denotes the oriented (j + 1)-cell v,σ0,...,σj . An oriented (j + 1)-cell σ0,...,σj induces orientations on the j-cells which form its boundary, as follows: the face σ0,...,σi−1,σi+1,...,σj is oriented as (−1)i [σ1,...,σi−1,σi+1,...,σk], where (−1)τ = τ.

The jth boundary operator ∂j : Ωj → Ωj−1 is

##### ∂j f (σ) =

f (vσ).

v∼σ

The sequence Ωj,∂j is a chain complex, i.e., ∂j−1∂j = 0 for all j, and one denotes

Zj = ker∂j j−cycles Bj = im∂j+1 j−boundaries Hj = Zj/Bj the jth homology of X (over R).

The adjoint of ∂j w.r.t. the inner product (2.1) is the co-boundary operator ∂∗j : Ωj−1 → Ωj given by

##### ∂∗j f (σ) =

f (τ) =

τisinthe boundaryof σ

j

##### (−1)i f (σ\σi),

i=0

where σ\σi = σ0,σ1,...,σi−1,σi+1,...σj . Here the standard terms are

Zj = ker∂∗j+1 = B⊥j closed j−forms Bj = im∂∗j = Z⊥j exact j−forms Hj = Zj/Bj the jth cohomology of X (over R).

The upper, lower, and full Laplacians ∆+,∆−,∆ : Ωd−1 → Ωd−1 are deﬁned by

##### ∆+ = ∂d∂∗d, ∆− = ∂∗d−1∂d−1, and ∆ = ∆+ + ∆−,

respectively†. All the Laplacians decompose (as a direct sum of linear operators) with respect to the orthogonal decompositions Ωd−1 = Bd−1 ⊕ Zd−1 = Bd−1 ⊕ Zd−1. In addition, ker∆+ = Zd−1 and ker∆− = Zd−1.

The space of harmonic (d − 1)-forms on X is Hd−1 = ker∆. If f ∈ Hd−1 then 0 = ∆f, f = ∂d−1 f,∂d−1 f + ∂∗d f,∂∗d f

† More generally, one can deﬁne the jth lower Laplacian ∆−j : Ωj → Ωj by ∆−j = ∂∗j∂j, and similarly for ∆+j and ∆j. For our purposes, ∆−d−1, ∆+d−1 and ∆d−1 are the relevant ones.

which shows that Hd−1 = Zd−1 ∩ Zd−1. This gives the so-called discrete Hodge decomposition

Ωd−1 = Bd−1 ⊕ Hd−1 ⊕ Bd−1. In particular, it follows that the space of harmonic forms can be identiﬁed with the cohomology of X:

B⊥

Bd−1 ⊕ Hd−1

Zd−1 Bd−1

d−1 Bd−1

Hd−1 =

Bd−1 Hd−1. The same holds for the homology of X, giving

=

=

Hd−1 Hd−1 Hd−1. (2.2)

For comparison, the original Hodge decomposition states that for a Riemannian manifold M and 0 ≤ j ≤ dim M, there is an orthogonal decomposition

Ωj (M) = d Ωj−1 (M) ⊕ H j (M) ⊕ δ Ωj+1 (M)

where Ωj are the smooth j-forms on M, d is the exterior derivative, δ its Hodge dual, and H j the smooth harmonic j-forms on M. As in the discrete case, this gives an isomorphism between the jth de-Rham cohomology of M and the space of harmonic j-forms on it.

Example. For j = 0, Z0 consists of the locally constant functions (functions constant on connected components); B0 consists of the constant functions; Z0 of the functions whose sum vanishes, and B0 of the functions whose sum on each connected component vanishes.

For j = 1, Z1 are the forms whose sum along the boundary of every triangle in the complex vanishes; in B1 lie the forms whose sum along every closed path vanishes; Z1 are the Kirchhoﬀ forms, also known as ﬂows, those for which the sum over all edges incident to a vertex, oriented inward, is zero; and B1 are the forms spanned (over R) by oriented boundaries of triangles in the complex. The chain of simplicial forms in dimensions −1 to 2 is depicted in Figure 1.

H0 H0 H0 H1 H1 H1 H2

###### Z1

Z2

Z0

###### Z0

Z1 Kirchhoﬀ

sumzeroalong triangleboundaries

locally constant

sum zero

###### ∂0 Ω0

###### ∂1 Ω1

###### ∂2 Ω2

###### R Ω−1

∂∗0

∂∗1

∂∗2

=

B−1 B0

###### B1

B2

B0

B1

sumzero alongcycles

constant

sumzero oncomponents

spanof triangleboundaries

Figure 1: The lowermost part of the chain complex of simplicial forms.

#### 2.1 Deﬁnition of the spectral gap

Every graph has a “trivial zero” in the spectrum of its upper Laplacian, corresponding to the constant functions. There can be more zeros in the spectrum, and these encode information about the graph (its connectedness), while the ﬁrst one does not. Similarly, for a d-dimensional complex, the space Bd−1

is always in the kernel of the upper Laplacian, and considered to be its “trivial zeros”. The existence of more zeros indicates a nontrivial (d − 1)-cohomology, since it means that Bd−1 ker∆+ = Zd−1. As Bd−1 ⊥ = Zd−1, this leads to the following deﬁnition:

- Deﬁnition 2.1. The spectral gap of a d-dimensional complex X, denoted λ(X), is the minimal eigenvalue of the upper or the full Laplacian on (d − 1)-cycles:


λ(X) = minSpec ∆ Z

= minSpec ∆+ Z

d−1

d−1

.)

(the equality follows from ∆ Z

##### ≡ ∆+ Z

d−1

d−1

The following proposition gives two more characterizations of the spectral gap. For complexes with a complete skeleton we shall obtain even more explicit characterizations in Proposition 3.3.

##### Proposition 2.2. Let Spec∆+ = λ0 ≤ λ1 ≤ ... ≤ λ|Xd−1|−1 .

- (1) If βj = dim Hj is the jth (reduced) Betti number of X, then λ(X) = λr where r = Xd−1 − βd−1 − Xd − βd .
- (2) λ(X) is the minimal nonzero eigenvalue of ∆+, unless X has a nontrivial (d − 1)th-homology, in which case λ(X) = 0.


Remark. For a graph G = (V, E), Deﬁnition 2.1 states that λ(G) is the minimal eigenvalue of the Laplacian on a function which sums to zero. By Proposition 2.2 (1) we have λ(G) = λr, where r = n − |E| − β0 + β1. Since β0 + 1 is the number of connected components in G, and β1 is the number of cycles in G, by Euler’s formula

##### r = n − |E| − β0 + β1 = χ(G) − (χ(G) − 1) = 1

and therefore λ(G) = λ1. From (2) in Proposition 2.2 we obtain that λ(G) is the minimal nonzero eigenvalue of G’s Laplacian if G is connected, and zero otherwise.

Proof. Since ∆+ decomposes w.r.t. Ωd−1 = Bd−1 ⊕ Zd−1, and ∆+ Bd−1 ≡ 0, the spectrum of ∆+ consists of r = dim Bd−1 zeros, followed by the spectral gap. By (2.2),

Hd−1 Hd−1 = Zd−1 ∩ Zd−1 = ker∆+ Z

d−1

so that λ(X) = 0 if and only if Hd−1 0, i.e. X has a nontrivial (d − 1)th-homology. This also shows that if Hd−1 = 0, then λ(X) is the smallest nonzero eigenvalue of ∆+. Finally, to compute r = dim Bd−1, we observe that

dim Bj−1 = dimZj−1 − dim Hj−1 = null∂∗j − βj−1

= dimΩj−1 − rank ∂∗j − βj−1 = Xj−1 − dim Bj − βj−1 and therefore

r = dim Bd−1 = Xd−1 − dim Bd − βd−1 = Xd−1 − Xd − dim Bd+1 − βd − βd−1

##### = Xd−1 − βd−1 − Xd − βd .

### 3 Properties of the Laplacians

In this section we begin the study of the Laplacians and their spectra. We start by writing the Laplacians in a more explicit form.

For the upper Laplacian, if f ∈ Ωd−1 and σ ∈ Xd−1, then

d

(−1)i f (vσ\(vσ)i)

∂∗d−1 f (vσ) =

∆+ f (σ) =

v∼σ

v∼σ

i=0

d−1

(−1)i f (vσ\σi)

f (σ) −

=

v∼σ

i=0

d−1

(−1)i f (vσ\σi), (3.1)

= deg(σ) f (σ) −

v∼σ

i=0

where we recall that deg(σ) is the number of d-cells containing σ. Let us introduce the following notation: for σ,σ ∈ Xd−1

± we denote σ ∼ σ if there exists an oriented d-cell τ such that both σ and σ are in the boundary of τ (as oriented cells). Using this notation we can express ∆+ more elegantly as

∆+ f (σ) = deg(σ) f (σ) −

f σ . (3.2)

σ ∼σ

For the lower Laplacian we have

d−1

d−1

(−1)i (∂d−1 f)(σ\σi) =

(−1)i

∆− f (σ) =

f (vσ\σi). (3.3)

i=0

i=0

v∼σ\σi

The following straightforward claim bounds the spectrum of the upper Laplacian:

Claim 3.1. The spectrum of ∆+ is contained in the interval [0,(d + 1)k], where k is the maximal degree in X.

#### 3.1 Complexes with a complete skeleton

Complexes with a complete skeleton appear to be particularly well behaved, in comparison with the general case. The following proposition lists some observations regarding their Laplacians. These will be used in the proofs of the main theorems, and also to obtain simpler characterizations of the spectral gap in this case.

- Proposition 3.2. If X has a complete skeleton, then


- (1) If X is the complement complex of X, i.e., Xd−1 = Xd−1 = Vd † and Xd = d V+1 \Xd, then ∆+X = n · I − ∆X. (3.4)

- (2) The spectrum of ∆ lies in the interval [0,n].
- (3) The lower Laplacian of X satisﬁes ∆− = n · PBd−1 (3.5)


where PBd−1 is the orthogonal projection onto Bd−1.

† V

j denotes the set of subsets of V of size j.

Proof. By the completeness of the skeleton, the lower Laplacian (see (3.3)) can be written as

d−1

d−1

(−1)i

(−1)i

∆− f (σ) =

f (vσ\σi) =

i=0

i=0

v∼σ\σi

d−1

(−1)i f (vσ\σi).

= d · f (σ) +

v σ

i=0

f (vσ\σi)

v σ\σi

To show (1) we observe that v ∼ σ in X iﬀ v σ and v σ (in X), so that

∆X f + ∆+X f (σ) = ∆−X f (σ) + ∆+X f (σ) + ∆+X f (σ)

d−1

(−1)i f (vσ\σi)

=d · f (σ) +

v σ

i=0

d−1

(−1)i f (vσ\σi)

+ deg(σ) f (σ) −

v∼σ

i=0

d−1

(−1)i f (vσ\σi) = nf (σ).

+ n − d − deg(σ) f (σ) −

i=0

v σ v σ

From (1) we conclude that Spec∆+X = n − γ γ ∈ Spec∆X , and since ∆X and ∆+X are positive semidefinite, (2) follows. To establish (3), recall that Bd−1 ⊥ = Zd−1 = ker∆−, and it is left to show that ∆− f = nf for f ∈ Bd−1. Note that Bd−1 ⊆ Zd−1 = ker∆+X, and in addition, that since Bd−1 only depends on X’s (d − 1)-skeleton,

Bd−1 (X) = Bd−1 X ⊆ Zd−1 X = ker∆+X. Now from (1) it follows that for f ∈ Bd−1

∆−X f = ∆−X f + ∆+X f = ∆X f = nf − ∆+X f = nf as desired.

The next proposition oﬀers alternative characterizations of the spectral gap:

- Proposition 3.3. If X has a complete skeleton, then


- (1) The spectral gap of X is obtained by λ(X) = minSpec ∆. (3.6)
- (2) Furthermore, it is the d n−−11 + 1 smallest eigenvalue of ∆+.


Remarks.

- (1) For graphs (3.6) gives λ(G) = minSpec ∆+ + J , where J = ∆− = 


#####  .

1 1 1 1 1 ··· 1

... .



. .

1 1 ··· 1

- (2) In general (3.6) does not hold: for example, for the triangle complex , λ = minSpec ∆ Z


= 3 but minSpec ∆ = 1.

d−1

Proof.

- (1) First, since ∆ decomposes w.r.t. Ωd−1 = Bd−1 ⊕ Zd−1 we have

Spec ∆ = Spec∆ Bd−1 ∪ Spec∆ Z

d−1

= Spec∆− Bd−1 ∪ Spec∆+ Z

d−1

.

By Proposition 3.2, Spec∆− Bd−1 = {n} and Spec ∆ ⊆ [0,n], which implies that

λ = minSpec ∆+ Z

d−1

= minSpec ∆.

- (2) The Euler characteristic satisﬁes di=−1 (−1)i Xi = χ(X) = di=−1 (−1)i βi. Therefore, by Proposition 2.2 we have λ = λr, with


r = Xd−1 − βd−1 − Xd − βd

d

= Xd−1 − βd−1 − Xd − βd + (−1)d

(−1)i Xi − βi

i=−1

d−2

(−1)d+i Xi − βi .

=

i=−1

Since the (d − 1)-skeleton is complete, Xi = i+ n1 and βi = 0 for 0 ≤ i ≤ d − 2, and so

d−2

n − 1 d − 1

n i + 1

(−1)d+i

r =

##### .

=

i=−1

We ﬁnish with a note on the density of d-cells in X:

- Proposition 3.4. Let δ denote the d-cell density of X, δ = |Xd| (d+n1), let k denote the average degree of a


(d − 1)-cell, and let λavg denote the average over the spectrum of ∆+ Z

. Then

d−1

k n − d

λavg n

. Proof. On the one hand

δ =

=

n d

k d+1 n d+1

Xd−1 k

Xd n d+1

k n − d

d+1 n d+1

δ =

##### .

=

=

=

On the other,

n d

k = Xd−1 k =

and by Proposition 3.3

degσ = trace∆+ =

λ =

λ∈Spec∆+

σ∈Xd−1

1

λavg =

λ =

n d − d n−−11 λ∈Spec∆+|Zd−1

1

n−1 d λ∈Spec∆+|Zd−1

##### λ

λ∈Spec∆+|Zd−1

n n − d · k.

λ =

### 4 Proofs of the main theorems

#### 4.1 A Cheeger-type inequality

This section is devoted to the proof of Theorem 1.2: For a complex with a complete skeleton, the Cheeger constant is bounded from below by the spectral gap.

Proof of Theorem 1.2. Recall that we seek to show

n · |F (A0, A1,..., Ad)| |A0| · |A1| · ... · |Ad|

= λ(X) ≤ h(X) = min

minSpec ∆+ Z

.

d−1

V= di=0 Ai

Let A0,..., Ad be a partition of V which realizes the minimum in h. We deﬁne f ∈ Ωd−1 by

f ([σ0 σ1 ... σd−1]) =   

sgn(π) Aπ(d) ∃π ∈ Sym{0...d} with σi ∈ Aπ(i) for 0 ≤ i ≤ d − 1 0 else, i.e. ∃k,i j with σi,σj ∈ Ak.

(4.1)

Note that f (π σ) = sgn(π ) f (σ) for any π ∈ Sym{0...d−1} and σ ∈ Xd−1. Therefore, f is a welldeﬁned skew-symmetric function on oriented (d − 1)-cells, i.e., f ∈ Ωd−1. Figure 2 illustrates f for d = 1,2.

A2

0

|A1| |A0|

0 0

0

0

A0 A1

|A2|

Figure 2: The form f ∈ Ωd−1 deﬁned in (4.1), for complexes of dimensions one and two.

We proceed to show that f ∈ Zd−1. Let σ = [σ0,σ1,...,σd−2] ∈ Xd−2

± . As we assumed that Xd−1 is complete,

(∂d−1 f)(σ) =

f ([v,σ0,σ1,...,σd−2]) =

f ([v,σ0,σ1,...,σd−2]).

v∼σ

v σ

If for some k and i j we have σi,σj ∈ Ak, this sum vanishes. On the other hand, if there exists π ∈ Sym{0...d} such that σi ∈ Aπ(i) for 0 ≤ i ≤ d − 2 then

f ([v,σ0,σ1,...,σd−2])

##### f ([v,σ0,σ1,...,σd−2]) +

(∂d−1 f)(σ) =

v∈Aπ(d)

v∈Aπ(d−1)

(−1)d sgnπ Aπ(d−1)

(−1)d−1 sgnπ Aπ(d) +

=

v∈Ad

v∈Aπ(d−1)

= (−1)d−1 sgnπ Aπ(d−1) Aπ(d) − Aπ(d) Aπ(d−1) = 0 and in both cases f ∈ Zd−1. Thus, by Rayleigh’s principle

∂∗d f,∂∗d f f, f

∆+ f, f f, f

λ(X) = minSpec ∆+ Z

. (4.2)

≤

=

d−1

The denominator is

f (σ)2 ,

f, f =

σ∈Xd−1

and a (d − 1)-cell σ contributes to this sum only if its vertices are in diﬀerent blocks of the partition, i.e., there are no k and i j with σi,σj ∈ Ak. In this case, there exists a unique block, Ai, which does not contain a vertex of σ, and σ contributes |Ai|2 to the sum. Since Xd−1 is complete, there are |A0| · ... · |Ai−1| · |Ai+1| · ... · |Ad| non-oriented (d − 1)-cells whose vertices are in distinct blocks and which do not intersect Ai, hence

#####  

Aj 

d

d

|Ai|2 = n

f, f =

|Ai|.

j i

i=0

i=0

To evaluate the numerator in (4.2), we ﬁrst show that for σ ∈ Xd

∂∗d f (σ) =   

n σ ∈ F (A0,..., Ad) 0 σ F (A0,..., Ad)

. (4.3)

First, let σ F (A0,..., Ad). If σ has three vertices from the same Ai, or two pairs of vertices from the same blocks (i.e. σi,σj ∈ Ak and σi ,σj ∈ Ak ), then for every summand in

d

##### (−1)i f (σ\σi),

∂∗d f (σ) =

i=0

the cell σ\σi has two vertices from the same block, and therefore ∂∗d f (σ) = 0. Next, assume that σj and σk (with j < k) is the only pair of vertices in σ which belong to the same block. The only

non-vanishing terms in ∂∗d f (σ) = di=0 (−1)i f (σ\σi) are i = j and i = k, i.e.,

##### ∂∗d f (σ) = (−1)j f σ\σj + (−1)k f (σ\σk).

Since the value of f on a simplex depends only on the blocks to which its vertices belong, f σ\σj = f σ0 σ1 ... σj−1 σj+1 ...σk−1 σk σk+1 ... σd

= f σ0 σ1 ... σj−1 σj+1 ...σk−1 σj σk+1 ... σd

= f (−1)k−j+1 σ0 σ1 ... σj−1 σj σj+1 ... σk−1 σk+1 ... σd

= (−1)k−j+1 f (σ\σk), so that

##### ∂∗d f (σ) = (−1)j (−1)k−j+1 f (σ\σk) + (−1)k f (σ\σk) = 0.

The remaining case is σ ∈ F (A0,..., Ad). Here, there exists π ∈ Sym{0...d} with σi ∈ Aπ(i) for 0 ≤ i ≤ d. Observe that

f (σ\σi) = sgn(π · (d d−1 d−2 ... i)) Aπ(i) = (−1)d−i sgnπ Aπ(i) and therefore

∂∗d f (σ) =

d

d

(−1)i f (σ\σi) = (−1)d sgnπ

i=0

i=0

Aπ(i) = (−1)d sgnπn.

Therefore, ∂∗d f (σ) = n. This establishes (4.3), which implies that

and in total

∂∗d f,∂∗d f =

σ∈Xd

2

∂∗d f (σ)

= n2 |F (A0,..., Ad)|

∂∗d f,∂∗d f f, f

λ(X) ≤

n|F (A0,..., Ad)|

= h(X).

=

d i=0 |Ai|

#### 4.2 Towards a lower Cheeger inequality

The ﬁrst observation to be made regarding a lower Cheeger inequality, is that no bound of the form C · h(X)m ≤ λ(X) can be found. Had such a bound existed, one would have that λ(X) = 0 implies h(X) = 0, but a counterexample to this is provided by the minimal triangulation of the Möbius strip (Figure 3).

1 3 0

0 2 4 1

Figure 3: A triangulation of the Möbius strip for which h(X) = 114 but λ(X) = 0.

Nevertheless, numerical experiments hint that a bound of the form C · h(X)2 − c ≤ λ(X) should hold, where C and c depend on the dimension and the maximal degree of a (d − 1)-cell in X.

An attempt towards an upper bound for the Cheeger constant can be made by connecting it to “local Cheeger constants”, as follows. For every τ ∈ Xd−2 we consider the link of τ (see Figure 4),

lk τ = {σ ∈ X |σ ∩ τ = ∅ and σ ∪ τ ∈ X}.

Figure 4: Two examples for the link of a vertex in a triangle complex.

Since dimτ = d − 2, lk τ is a graph, and there is a 1 − 1 correspondence between vertices (edges) of lk τ and (d − 1)-cells (d-cells) of X which contain τ. We have the following bound for the Cheeger constant of X:

Proposition 4.1. The bound h(X) ≤ 1h−(lkd−τ1)

holds for any d-complex X and τ ∈ Xd−2.

n

Proof. Write τ = [τ0,τ1,...,τd−2] and denote Ai = {τi} for 0 ≤ i ≤ d − 2. Due to the correspondence between (lk τ)j and cells in Xd−1+j containing τ,

|Elkτ (B,C)| · (lk τ)0 |B| · |C|

|F (A0,..., Ad−2, B,C)| · (lk τ)0 |B| · |C|

h(lk τ) def= min

= min

##### .

B C=(lk τ)0

B C=(lk τ)0

Assume that the minimum is attained by B = B0 and C = C0. We deﬁne

 

Ai

d−1

Ad−1 = B0, Ad = V\

##### .

i=0

Now A0,..., Ad is a partition of V, and

F (A0,..., Ad−2, B0,C0) = F (A0,..., Ad−2, Ad−1, Ad) since no d-cell containing τ has a vertex in Ad\C0. In addition,

(lk τ)0 |Ad| − |Ad−1|(|Ad| − |C0|) n|C0|

(lk τ)0 |Ad| n|C0|

≥

[n − (d − 1) − (|Ad| − |C0|)]|Ad| − |Ad−1|(|Ad| − |C0|) n|C0|

=

(n − (d − 1))|Ad| − (|Ad−1| + |Ad|)(|Ad| − |C0|) n|C0|

=

(n − (d − 1))[|Ad| − (|Ad| − |C0|)] n|C0|

d − 1 n

= 1 −

##### ,

=

which implies

F (A0,..., Ad−2, Ad−1, Ad) (lk τ)0 |B0| · |C0|

h(lk τ) =

(lk τ)0 |Ad| n|C0| ≥ h(X) ·

F (A0,..., Ad−2, Ad−1, Ad)n |A0| · ... · |Ad|

·

=

(lk τ)0 |Ad| n|C0|

d − 1 n

h(X).

≥ 1 −

Since lk τ is a graph, its Cheeger constant can be bounded using the lower inequality in (1.1). We also note that the degree of a vertex in lk τ corresponds to the degree of a (d − 1)-cell in X, and therefore

1 − d−n1 2 8k

h(lk τ)2 8k ≤

h(lk τ)2

h2 (X) ≤

8kτ ≤ λ(lk τ) (4.4) where k is the maximal degree of a (d − 1)-cell in X, and kτ of a vertex in lk τ.

We now see that a bound of the spectral gap of links by that of the complex would yield a lower Cheeger inequality. Such a bound was indeed discovered by Garland in [Gar73], and was studied further by several authors [Zuk96, ABM05, GW12]. The following lemma appears in [GW12], for a normalized version of the Laplacian. We give here, without proof, its form for the Laplacian we use.

Lemma 4.2 ([Gar73, GW12]). Let X be a d-dimensional simplicial complex. Given f ∈ Ωd−1,σ ∈ Xd−1,τ ∈ Xd−2 deﬁne a function fτ : (lk τ)0 → R by fτ (v) = f (vτ), and an operator ∆+τ : Ωd−1 (X) → Ωd−1 (X) by

  

f (σ ) τ ⊂ σ 0 τ σ

degτ (σ) f (σ) −

∆+τ f (σ) =

σ ∼σ τ⊆σ

where degτ (σ) = #{σ ∼ σ|τ ⊆ σ } = deglkτ (σ\τ). The following then hold:

- (1) ∆+ = τ∈Xd−2 ∆+τ − (d − 1) D, where (Df)(σ) = deg(σ) f (σ).
- (2) ∆+τ f, f = ∆+lkτ fτ, fτ .
- (3) If f ∈ Zd−1 then fτ ∈ Z0 (lk τ).
- (4) τ∈Xd−2 fτ, fτ = d f, f .


Assume now that f ∈ Zd−1 is a normalized eigenfunction for λ(X), i.e. f, f = 1 and ∆+ f = λ(X) f. Using the lemma we ﬁnd that

∆+τ f, f − (d − 1) Df, f (=2)

λ(X) = ∆+ f, f (=1)

∆+lkτ fτ, fτ − (d − 1) Df, f

τ∈Xd−2

τ∈Xd−2

(3)

λ(lk τ) fτ, fτ − (d − 1)k (=4) d min

∆+lkτ fτ, fτ − (d − 1)k

λ(lk τ) − (d − 1)k.

##### ≥

##### ≥

τ∈Xd−2

τ∈Xd−2

τ∈Xd−2

By (4.4) we obtain the bound

d 1 − d−n1 2 8k

h2 (X) − (d − 1)k ≤ λ(X).

Sadly, this bound is trivial, as it is not hard to show that the l.h.s. is non-positive for every complex X. A possible line of research would be to ﬁnd a stronger relation between the spectral gap of the complex and that of its links, for the case of complexes with a complete skeleton (Garland’s work applies to general ones).

- 4.3 The Mixing Lemma Here we prove Theorem 1.4. We begin by formulating it precisely.


Theorem (1.4). Let X be a d-dimensional complex with a complete skeleton. Fix α ∈ R, and write Spec αI − ∆+ = {µ0 ≥ µ1 ≥ ... ≥ µm} (where m = d n −1). For any disjoint sets of vertices A0,..., Ad (not necessarily a partition), one has

##### α · |A0| · ... · |Ad|

n ≤ ρα · (|A0| · ... · |Ad|)d+d1 where

|F (A0,..., Ad)| −

ρα = max µ(n−1

##### d−1) ,|µm| = αI − ∆+ Z

##### .

d−1

- Remark 4.3. Which α should one take in practice? In the introduction we state the theorem for α = k, the average degree of a (d − 1)-cell, so that it generalize the familiar form of the Expander Mixing Lemma for k-regular graphs. However, the expectation of |F (A0,..., Ad)| in a random settings is


actually δ|A0| · ... · |Ad|, where δ is the d-cell density |Xd|

(dn) . Therefore, α = nδ = nnk−d is actually a more accurate choice. This becomes even clearer upon observing that we seek to minimize ρα =

is centered around λavg =

, since Proposition 3.4 shows that the spectrum of ∆+ Z

##### αI − ∆+ Z

d−1

d−1

nδ = nnk−d. While for a ﬁxed d the choice between k and nnk−d is negligible, this should be taken into account when d depends on n.

Proof. For any disjoint sets of vertices A0,..., Ad−1, deﬁne δA0,...,Ad−1 ∈ Ωd−1 by

δA0,...,Ad−1 (σ) =   

sgn(π) ∃π ∈ Sym{0...d−1} with σi ∈ Aπ(i) for 0 ≤ i ≤ d − 1 0 else

##### .

Since the skeleton of X is complete,

δ2A

0,...,Ad−1 (σ) = |A0| · ... · |Ad−1|. (4.5)

δA0,...,Ad−1 =

σ∈Xd−1

Now, let A0,..., Ad be disjoint subsets of V (not necessarily a partition), and denote

ϕ = δA0,A1,A2,...,Ad−1 ψ = δAd,A1,A2,...,Ad−1.

Let σ be an oriented (d − 1)-cell with one vertex in each of A0, A1,..., Ad−1. We shall denote this by σ ∈ F (A0,..., Ad−1), ignoring the orientation of σ. There is a correspondence between d-cells in

- F (A0,..., Ad) containing σ, and neighbors of σ which lie in F (Ad, A1,..., Ad−1). Furthermore, for such a neighbor σ we have ϕ(σ) = ψ(σ ), since σ and σ must share the vertices which belong to A1,..., Ad−1. Therefore, if (Df)(σ) = deg(σ) f (σ) then by (3.2)


ϕ(σ) D − ∆+ ψ (σ) =

ϕ(σ)ψ σ

ϕ, D − ∆+ ψ =

σ∈Xd−1 σ ∼σ

σ∈Xd−1

# σ ∈ F (Ad, A1,..., Ad−1) σ ∼ σ

##### ϕ(σ)ψ σ =

=

σ∈F(A0...Ad−1)

σ∈F(A0...Ad−1) σ ∼σ

#{τ ∈ F (A0, A1,..., Ad)|σ ⊆ τ} = |F (A0, A1,..., Ad)|. (4.6)

=

σ∈F(A0...Ad−1)

Notice that since the Ai are disjoint, ϕ and ψ are supported on diﬀerent (d − 1)-cells, so that for any α ∈ R

##### ϕ, D − ∆+ ψ = ϕ,−∆+ψ = ϕ, αI − ∆+ ψ . (4.7)

As ∆+ decomposes w.r.t. the orthogonal decomposition Ωd−1 = Bd−1 ⊕ Zd−1, and since Bd−1 ⊆ Zd−1 = ker∆+,

|F (A0, A1,..., Ad)| = ϕ, αI − ∆+ ψ

= ϕ, αI − ∆+ PBd−1ψ + PZd−1ψ

= ϕ,αPBd−1ψ + αI − ∆+ PZd−1ψ

= α ϕ,PBd−1ψ + ϕ, αI − ∆+ PZd−1ψ . (4.8)

We proceed to evaluate each of these terms separately. Using (3.5) and (3.4) we ﬁnd that

α n

α n

ϕ,∆−ψ =

ϕ, nI − ∆+X − ∆+X ψ and by (4.6) and (4.7) this implies

α ϕ,PBd−1ψ =

α n

α n

ϕ, nI − ∆+X ψ +

ϕ,−∆+Xψ

α ϕ,PBd−1ψ =

α n

α n |FX (A0, A1,..., Ad)| +

FX (A0, A1,..., Ad)

=

α · |A0| · ... · |Ad| n

. (4.9)

=

We turn to the second term in (4.8). First, we recall from Proposition 3.3 that dim Bd−1 = d n−−11 . Since Bd−1 ⊆ ker∆+, we can assume that in Spec αI − ∆+ = {µ0 ≥ µ1 ≥ ... ≥ µm} the ﬁrst d n−−11 values correspond to Bd−1, and the rest to Bd−1 ⊥ = Zd−1. Thus,

ρα = max µ(n−1

##### d−1) ,|µm| = max |µ| µ ∈ Spec αI − ∆+ Z

d−1

and therefore

##### = αI − ∆+ Z

d−1

, (4.10)

##### ϕ, αI − ∆+ PZd−1ψ ≤ ϕ · αI − ∆+ PZd−1ψ ≤ ϕ · αI − ∆+ Z

##### · PZd−1ψ

d−1

≤ ρα · ϕ · ψ = ρα |A0||Ad||A1||A2|...|Ad−1|, (4.11) where the last step is by (4.5). Together (4.8), (4.9) and (4.11) give

##### α · |A0| · ... · |Ad|

|F (A0, A1,..., Ad)| −

n ≤ ρα |A0||Ad||A1||A2|...|Ad−1|. Since A0,..., Ad play the same role, one can also obtain the bound

ρα Aπ(0) Aπ(d) Aπ(1) Aπ(2) ... Aπ(d−1) , for any π ∈ Sym{0..d}. Taking the geometric mean over all such π gives

##### α · |A0| · ... · |Ad|

n ≤ ρα · (|A0||A1|...|Ad|)d+d1 .

|F (A0, A1,..., Ad)| −

Remark. The estimate (4.11) is somewhat wasteful. As is done in graphs, a slightly better one is

ϕ, αI − ∆+ PZd−1ψ = PZd−1ϕ, αI − ∆+ PZd−1ψ ≤ ρα · PZd−1ϕ · PZd−1ψ , and we leave it to the curious reader to verify that this gives

 1 −

 |Ad|

#####  |A1|...|Ad−1|.

 1 −

d−1 i=0 |Ai|

d i=1 |Ai|

ϕ, αI − ∆+ PZd−1ψ ≤ ρα |A0|

n

n

#### 4.4 Gromov’s geometric overlap

Here we prove Corollary 1.6, which gives a bound on the geometric overlap of a complex in terms of the width of its spectrum.

Proof of Corollary 1.6. Given ϕ : V → Rd+1, choose arbitrarily some partition of V into equally sized parts P0,..., Pd. By Pach’s theorem [Pac98], there exist cd > 0 and Qi ⊆ Pi of sizes |Qi| = cd |Pi| such that for some x ∈ Rd+1 we have x ∈ conv{ϕ(v)|v ∈ σ} for any σ ∈ F (Q0,..., Qd). By the Mixing Lemma (Theorem 1.4),

d kcd

k · |Q0| · ... · |Qd| n − ε · (|Q0| · ... · |Qd|)d+d1 =

cdn d + 1

|F (Q0,..., Qd)| ≥

d + 1 − ε . On the other hand,

d k d + 1

k d + 1

n d

k d + 1 ≤

en d

Xd = Xd−1

. As this holds for every ϕ,

=

overlap(X) ≥

cdd e(d + 1)

d

cdd ed+1

ε(d + 1)

cd −

k ≥

ε(d + 1) k

cd −

.

⊆ λavg − ε ,λavg + ε then using the Mixing Lemma with α = λavg = nnk−d one has

- Remark 4.4. Following Remark 4.3, if Spec∆+ Z


d−1

d nkcd

k · |Q0| · ... · |Qd| n − d − ε · (|Q0| · ... · |Qd|)d+d1

cdn d + 1

|F (Q0,..., Qd)| ≥

≥

(n − d)(d + 1) − ε so that

cddn ed+1 (n − d)

ε (d + 1) λavg

overlap(X) ≥

cd −

.

#### 4.5 Expansion in random complexes

In this section we prove Corollaries 1.3 and 1.7, regarding the expansion of random Linial-Meshulam complexes. The main idea is the following lemma, which is a variation on the analysis in [GW12] of the spectrum of D − ∆+ for X = X (d,n, p).

Lemma 4.5. Let c > 0. There exists γ = O √C such that X = X d,n, C·logn n satisﬁes

⊆ (C − γ)logn,(C + γ)logn

Spec ∆+ Z

d−1

with probability at least 1 − n−c. Proof. We denote p = C·logn n. For C large enough we shall ﬁnd γ = O √C such that

≤ γ logn (4.12) holds with probability at least 1 − n−c. This implies the Lemma, as

##### ∆+ − pn · I Z

d−1

⊆ pn − γ logn, pn + γ logn = (C − γ)logn,(C + γ)logn .

Spec ∆+ Z

d−1

To show (4.12) we use

= ∆+ − p(n − d) I − pdI + D − D Z

##### ∆+ − pn · I Z

d−1

d−1

≤ (D − p(n − d) I) Z

(4.13) and we will treat each term separately. For the ﬁrst, we have

##### + D − ∆+ + pdI Z

d−1

d−1

degσ − (n − d) p .

≤ D − (n − d) pI = max

(D − (n − d) pI) Z

d−1

σ∈Xd−1

Since degσ ∼ B(n − d, p), a Chernoﬀ type bound (e.g. [Jan02, Theorem 1]) gives that for every t > 0

− t2

2(n−d)p+ 2t

Prob degσ − (n − d) p > t ≤ 2e

3 . By a union bound on the degrees of the (d − 1)-cells we get

− t2

n

2(n−d)p+ 2t

degσ − (n − d) p > t ≤ 2

3 , (4.14)

Prob max

- d
- e


σ∈Xd−1

and a straightforward calculation shows that there exists α = α(c,d) > 0 such that for t = α nplogn, the r.h.s. in (4.14) is bounded by 21nc for large enough C and n. In total this implies

Prob (D − (n − d) pI) Z

d−1

≤ α

√

C logn ≥ 1 −

- 1

- 2nc


. (4.15)

In order to understand the last term in (4.13) we follow [GW12], which shows that DX − ∆+X Z

d−1

n Zd−1, where Knd is the complete d-complex on n vertices. Note that DKd

is close to p times DKd

− ∆+Kd

n

n Zd−1 = n · I, and that Zd−1 (X) = Zd−1 Knd as both have the same (d − 1)skeleton. In the proof of Theorem 7 in [GW12] (which uses an idea from [Oli10]), it is shown that

= (n − d) · I and ∆+Kd

n

Prob DX − ∆+X + pdI Z

d−1

≥ t = Prob DX − ∆+X Z

d−1

− p DKd

n

n

t2

- d
- e−


n Zd−1 ≥ t ≤ 2

− ∆+Kd

8pnd+4t.

Again, there exists β = β(c,d) > 0 such that for t = β nplogn, the r.h.s. is bounded by 21nc for large enough C and n. Consequently,

Prob D − ∆+ + pdI Z

d−1

≤ β

√

- 1

- 2nc


C logn ≥ 1 −

##### ,

so that

√

C logn ≥ 1 − n−c, and γ = (α + β) √C gives the required result.

≤ (α + β)

Prob ∆+ − pnI Z

d−1

We obtain the following corollary, which implies in particular Corollaries 1.3 and 1.7. Corollary 4.6. Observe X = X d,n, C·logn n .

- (1) Given c > 0, there exist a constant H = C − O √C such that for large enough n Prob h(X) ≥ H · logn ≥ 1 − n−c, (4.16)

and for any ϑ < ced d+1 (where cd is Pach’s constant [Pac98]), for C and n large enough

Prob overlap(X) > ϑ ≥ 1 − n−c.

- (2) If C < 1 then Prob(h(X) = 0) −→n→∞ 1.


Proof. (1) Since λ(X) ≤ h(X) (Theorem 1.2), (4.16) follows from Lemma 4.5 with H = C − γ (recall that γ = O √C ). We turn to the geometric overlap. From Lemma 4.5 it follows that

⊆ (C − γ)logn,(C + γ)logn . Therefore, Spec ∆+ Z

for C large enough a.a.s. Spec∆+ Z

⊆ λavg − ε ,λavg + ε with ε = 2γ logn. By Remark 4.4,

d−1

d−1

cddn ed+1 (n − d)

cdd ed+1

d+1

2γ logn(d + 1)

2γ (d + 1) C − γ

cd e

−→ C→∞

overlap(X) ≥

cd −

cd −

λavg ≥

##### .

(2) Choose some τ ∈ Xd−2. It was observed in [GW12] that lk τ ∼ G n − d + 1, C·logn n (where

- G (n, p) = X (1,n, p) is the Erd˝os–Rényi model), and G n, C·logn n has isolated vertices a.a.s. for C < 1 [ER59, ER61]. These correspond to isolated (d − 1)-cells in X (cells of degree zero), whose existence implies h(X) = 0 (and thus also λ(X) = 0).


### 5 Open questions

Non-complete skeleton. The proof of the generalized mixing lemma assumes that the skeleton is complete. This raises the following question:

Question: Can the discrepancy in X be bounded for general simplicial complexes?

As remarked after the statement of Theorem 1.2, one always has h(X) = 0 for X with a non-complete skeleton. This calls for a reﬁned deﬁnition, and a natural candidate is the following:

n · |F (A0, A1,..., Ad)| F∂ (A0, A1,..., Ad)

h(X) = min

,

V= di=0 Ai

where F∂ (A0, A1,..., Ad) denotes the set of (d − 1)-spheres (i.e. copies of the (d − 1)-skeleton of the d-simplex) having one vertex in each Ai. For a complex X with a complete skeleton, h(X) = h(X) as F∂ (A0,..., Ad) = A0 × ... × Ad. It is not hard to see that a lower Cheeger inequality does not hold here: consider any non-minimal triangulation of the (d − 1)-shpere, and attach a single d-simplex to one of the (d − 1)-cells on it. The obtained complex has λ = 0, and h = n. However, we conjecture that the upper bound still holds:

Question: Does the inequality λ(X) ≤ h(X) holds for every d-complex?

Inverse Mixing Lemma In [BL06] Bilu and Linial prove an Inverse Mixing Lemma for graphs: Theorem ([BL06]). Let G be a k-regular graph on n vertices. Suppose that for any disjoint A, B ⊆ V

k |A||B| n ≤ ρ |A||B|.

E (A, B) −

Then the nontrivial eigenvalues of kI − ∆G+ are bounded, in absolute value, by O ρ 1 + log ρ k . Question: Can one prove a generalized Inverse Mixing Lemma for simplicial complexes?

Random simplicial complexes In the random graph model G = G (n, p) = X (1,n, p), taking p = nk with a ﬁxed k gives disconnected G a.a.s. However, random k-regular graphs are a.a.s. connected,

and in fact are excellent expanders (see e.g. [Fri03, Pud12]). In higher dimension, X = X d,n, nk has a.a.s. a nontrivial (d − 1)-homology, and also h(X) = 0 (by Corollary 4.6 (2)). It is thus natural to ask

about the expansion quality of k-regular d-complexes, but since it is not clear whether such complexes even exist, we say that a k-semiregular complex is a complex with k −

√k ≤ degσ ≤ k +

√k for all

σ ∈ XdimX−1, and ask: Question: Are λ(X), h(X) and overlap(X) bounded away from zero with high probability, for X a

random k-semiregular d−complex with a complete skeleton?

A Riemannian analogue In Riemannian geometry, the Cheeger constant of a Riemannian manifold M is concerned with its partitions into two submanifolds along a common boundary of codimension one. The original Cheeger inequalities, due to Cheeger [Che70] and Buser [Bus82], relate the Cheeger constant to the smallest eigenvalue of the Laplace-Beltrami operator on C∞ (M) = Ω0 (M).

Question: Can one deﬁne an isoperimetric quantity which concerns partitioning of M into d+1 parts, and relate it to the spectrum of the Laplace-Beltrami operator on Ωd−1 (M), the space of smooth (d − 1)-forms?

Ramanujan complexes Ramanujan Graphs are expanders which are spectrally optimal in the sense of the Alon-Boppana theorem [Nil91], and therefore excellent combinatorial expanders. Such graphs were constructed in [LPS88] as quotients of the Bruhat-Tits tree associated with PSL2 Qp by certain arithmetic lattices. Analogue quotients of the Bruhat-Tits buildings associated with PSLd Fq ((t)) are constructed in [LSV05], and termed Ramanujan Complexes. It is natural to ask whether these complexes are also optimal expanders in the spectral and combinatorial senses.

### References

[ABM05] R. Aharoni, E. Berger, and R. Meshulam, Eigenvalues and homology of ﬂag complexes and vector representations of graphs, Geometric and functional analysis 15 (2005), no. 3, 555–566.

[AC88] N. Alon and F.R.K. Chung, Explicit construction of linear sized tolerant networks, Dis-

crete Mathematics 72 (1988), no. 1-3, 15–19. [Alo86] N. Alon, Eigenvalues and expanders, Combinatorica 6 (1986), no. 2, 83–96. [AM85] N. Alon and V.D. Milman, λ1, isoperimetric inequalities for graphs, and superconcentra-

tors, Journal of Combinatorial Theory, Series B 38 (1985), no. 1, 73–88.

[BKV+81] Manuel Blum, Richard M. Karp, O Vorneberger, Christos H. Papadimitriou, and Mihalis Yannakakis, Complexity of testing whether a graph is a superconcentrator, INFO. PROC. LETT. 13 (1981), no. 4, 164–167.

[BL06] Y. Bilu and N. Linial, Lifts, discrepancy and nearly optimal spectral gap, Combinatorica

26 (2006), no. 5, 495–519.

[BMS93] R. Beigel, G. Margulis, and D.A. Spielman, Fault diagnosis in a small constant number of parallel testing rounds, Proceedings of the ﬁfth annual ACM symposium on Parallel algorithms and architectures, ACM, 1993, pp. 21–29.

[Bus82] P. Buser, A note on the isoperimetric constant, Ann. Sci. École Norm. Sup.(4) 15 (1982), no. 2, 213–230.

[Che70] J. Cheeger, A lower bound for the smallest eigenvalue of the Laplacian, Problems in anal-

ysis 195 (1970), 199. [Chu97] F.R.K. Chung, Spectral graph theory, CBMS, no. 92, Amer Mathematical Society, 1997. [DK10] D. Dotterrer and M. Kahle, Coboundary expanders, arXiv preprint arXiv:1012.5316

(2010). [Dod84] J. Dodziuk, Diﬀerence equations, isoperimetric inequality and transience of certain random walks, Trans. Amer. Math. Soc 284 (1984). [Eck44] B. Eckmann, Harmonische funktionen und randwertaufgaben in einem komplex, Commentarii Mathematici Helvetici 17 (1944), no. 1, 240–255. [ER59] Paul Erd˝os and Alfréd Rényi, On random graphs, Publicationes Mathematicae Debrecen

6 (1959), 290–297.

[ER61] Paul Erdos and Alfréd Rényi, On the evolution of random graphs, Bull. Inst. Internat. Statist 38 (1961), no. 4, 343–347.

[FGL+11] J. Fox, M. Gromov, V. Laﬀorgue, A. Naor, and J. Pach, Overlap properties of geometric expanders, Proceedings of the Twenty-Second Annual ACM-SIAM Symposium on Discrete Algorithms, SIAM, 2011, pp. 1188–1197.

[FP87] J. Friedman and N. Pippenger, Expanding graphs contain all small trees, Combinatorica

7 (1987), no. 1, 71–76.

[Fri03] Joel Friedman, A proof of Alon’s second eigenvalue conjecture, Proceedings of the thirtyﬁfth annual ACM symposium on Theory of computing, ACM, 2003, pp. 720–724.

[Gar73] H. Garland, p-adic curvature and the cohomology of discrete subgroups of p-adic groups, The Annals of Mathematics 97 (1973), no. 3, 375–423.

[Gro10] M. Gromov, Singularities, expanders and topology of maps. part 2: From combinatorics to topology via algebraic isoperimetry, Geometric And Functional Analysis 20 (2010), no. 2, 416–526.

[GW12] A. Gundert and U. Wagner, On Laplacians of random complexes, Proceedings of the 2012 symposuim on Computational Geometry, ACM, 2012, pp. 151–160.

[HLW06] S. Hoory, N. Linial, and A. Wigderson, Expander graphs and their applications, Bulletin of the American Mathematical Society 43 (2006), no. 4, 439–562.

[Jan02] S. Janson, On concentration of probability, Contemporary combinatorics 10 (2002), no. 3, 1–9.

[LM06] N. Linial and R. Meshulam, Homological connectivity of random 2-complexes, Combinatorica 26 (2006), no. 4, 475–487.

[LPS88] A. Lubotzky, R. Phillips, and P. Sarnak, Ramanujan graphs, Combinatorica 8 (1988), no. 3, 261–277.

[LSV05] A. Lubotzky, B. Samuels, and U. Vishne, Ramanujan complexes of type A˜d, Israel Journal of Mathematics 149 (2005), no. 1, 267–299.

[Lub10] A. Lubotzky, Discrete groups, expanding graphs and invariant measures, vol. 125, Birkhauser, 2010.

[Lub12] , Expander graphs in pure and applied mathematics, Bull. Amer. Math. Soc 49

(2012), 113–162. [MS90] David W Matula and Farhad Shahrokhi, Sparsest cuts and bottlenecks in graphs, Discrete Applied Mathematics 27 (1990), no. 1, 113–123. [MW09] R. Meshulam and N. Wallach, Homological connectivity of random k-dimensional complexes, Random Structures & Algorithms 34 (2009), no. 3, 408–417. [MW11] J. Matoušek and U. Wagner, On Gromov’s method of selecting heavily covered points, Arxiv preprint arXiv:1102.3515 (2011). [Nil91] A. Nilli, On the second eigenvalue of a graph, Discrete Mathematics 91 (1991), no. 2, 207–210.

[NR12] Ilan Newman and Yuri Rabinovich, On multiplicative λ-approximations and some geometric applications, Proceedings of the Twenty-Third Annual ACM-SIAM Symposium on Discrete Algorithms, SODA ’12, SIAM, 2012, pp. 51–67.

[Oli10] R.I. Oliveira, Concentration of the adjacency matrix and of the Laplacian in random graphs with independent edges, Arxiv preprint ArXiv:0911.0600v2 (2010).

[Pac98] J. Pach, A Tverberg-type result on multicolored simplices, Computational Geometry 10

(1998), no. 2, 71–76. [PR12] Ori Parzanchevski and Ron Rosenthal, Simplicial complexes: spectrum, homology and random walks, arXiv preprint arXiv:1211.6775 (2012). [Pud12] Doron Puder, Expansion of random graphs: New proofs, new results, arXiv preprint arXiv:1212.5216 (2012). [SKM12] J. Steenbergen, C. Klivans, and S. Mukherjee, A Cheeger-type inequality on simplicial complexes, arXiv preprint arXiv:1209.5091 (2012). [Tan84] R.M. Tanner, Explicit concentrators from generalized n-gons, SIAM Journal on Algebraic and Discrete Methods 5 (1984), 287. [Tao11] T. Tao, Basic theory of expander graphs, http://terrytao.wordpress.com/2011/

##### 12/02/245b-notes-1-basic-theory-of-expander-graphs/, 2011.

[Zuk96] A. Zuk, La propriété (T) de Kazhdan pour les groupes agissant sur les polyedres, Comptes rendus de l’Académie des sciences. Série 1, Mathématique 323 (1996), no. 5, 453–458.

