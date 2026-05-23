# arXiv:1211.6775v2[math.CO]11Jan2013

## Simplicial complexes: spectrum, homology and random walks

Ori Parzanchevski† and Ron Rosenthal‡ Hebrew University of Jerusalem November 27, 2024

Abstract

Random walks on a graph reﬂect many of its topological and spectral properties, such as connectedness, bipartiteness and spectral gap magnitude. In the ﬁrst part of this paper we deﬁne a stochastic process on simplicial complexes of arbitrary dimension, which reﬂects in an analogue way the existence of higher dimensional homology, and the magnitude of the high-dimensional spectral gap originating in the works of Eckmann and Garland.

The second part of the paper is devoted to inﬁnite complexes. We present a generalization of Kesten’s result on the spectrum of regular trees, and of the connection between return probabilities and spectral radius. We study the analogue of the Alon-Boppana theorem on spectral gaps, and exhibit a counterexample for its high-dimensional counterpart. We show, however, that under some assumptions the theorem does hold - for example, if the codimension-one skeletons of the complexes in question form a family of expanders.

Our study suggests natural generalizations of many concepts from graph theory, such as amenability, recurrence/transience, and bipartiteness. We present some observations regarding these ideas, and several open questions.

### Contents

##### 1 Introduction 2

- 1.1 Example - regular triangle complexes . . . . . . . . . . . . . . . . . . . . . . . . . 3
- 1.2 Summary of results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5


##### 2 Finite complexes 6

- 2.1 The (d − 1)-walk and expectation process . . . . . . . . . . . . . . . . . . . . . . 7
- 2.2 Simplicial complexes and Laplacians . . . . . . . . . . . . . . . . . . . . . . . . . 9
- 2.3 The upper Laplacian spectrum . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
- 2.4 Walk and spectrum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13


†Supported by an Advanced ERC Grant, and the ISF. ‡Supported by ERC StG 239990.

1 INTRODUCTION

- 3 Inﬁnite complexes 16

- 3.1 Inﬁnite graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
- 3.2 Inﬁnite complexes of general dimension . . . . . . . . . . . . . . . . . . . . . . . 17
- 3.3 Example - arboreal complexes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
- 3.4 Continuity of the spectral measure . . . . . . . . . . . . . . . . . . . . . . . . . . 22
- 3.5 Alon-Boppana type theorems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
- 3.6 Analysis of balls in T22 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
- 3.7 Spectral radius and random walk . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
- 3.8 Amenability, transience and recurrence . . . . . . . . . . . . . . . . . . . . . . . . 32


- 4 Open Questions 34


### 1 Introduction

There are well known connections between dynamical, topological and spectral properties of graphs: The random walk on a graph reﬂects both its topological and algebraic connectivity, which are reﬂected by the 0th-homology and the spectral gap, respectively.

In this paper we present a stochastic process which takes place on simplicial complexes of arbitrary dimension and generalizes these connections. In particular, for a ﬁnite d-dimensional complex, the asymptotic behavior of the process reﬂects the existence of a nontrivial (d − 1)homology, and its rate of convergence is dictated by the (d − 1)-dimensional spectral gap†. The study of the process on ﬁnite complexes occupies the ﬁrst half of the paper. In the second half we turn to inﬁnite complexes, studying the high-dimensional analogues of classic properties and theorems regarding inﬁnite graphs. Both in the ﬁnite and the inﬁnite cases, one encounters new phenomena along the familiar ones, which reveal that graphs present only a degenerated case of a broader theory.

In order to give a ﬂavor of the results without plunging into the most general deﬁnitions, we present in §1.1, without proofs, the special case of regular triangle complexes. A summary of the paper and its main results both for ﬁnite and inﬁnite complexes is presented in §1.2.

This manuscript is part of an ongoing research seeking to understand the notion of highdimensional expanders. Namely, the analogue of expander graphs in the realm of simplicial complexes of general dimension. Here we discuss the dynamical aspect of expansion, i.e. asymptotic behavior of random walks, and its relation to spectral expansion and homology. In a previous paper we studied expansion from combinatorial and isoperimetric points of view [PRT12]. The study of high-dimensional expanders is currently a very active one, comprising the notions of geometric and topological expansion in [Gro10, FGL+10, MW11], F2-coboundary expansion in [LM06, MW09, DK10, GW12, SKM12], and Ramanujan complexes in [CSŻ03, Li04, LSV05]. We refer the reader to [Lub13] for a survey of the current state of the ﬁeld.

† The high-dimensional spectral gap originates in the classic works of Eckmann [Eck44] and Garland [Gar73], and appears in Deﬁnition 2.5 here.

#### 1.1 Example - regular triangle complexes

First, let us observe the 12-lazy random walk on a k-regular graph G = (V,E): the walker starts at a vertex v0, and at each step remains in place with probability 21 or moves to each of its k neighbors with probability 21k. Let pv

n0 (v) denote the probability of ﬁnding the walker at the vertex v at time n. The following observations are classic:

- (1) If G is ﬁnite, then pv

∞0 = limn→∞ pv

n0 exists, and it is constant if and only if G is connected.

- (2) Furthermore, the rate of convergence is given by

pv

0

n − const = O 1 −

- 1

- 2


λ(G)

n

,

where λ(G) is the spectral gap of G (the deﬁnition follows below).

- (3) When G is inﬁnite and connected, the spectral gap is related to the return probability of the walk by


- 1

- 2


n pv

λ(G). (1.1)

n0 (v0) = 1 −

lim

n→∞

We recall the basic deﬁnitions: the Laplacian of G, which we denote by ∆+, is the operator which acts on RV by

1 k w∼v

∆+f (v) = f (v) −

f (w)

(where ∼ denotes neighboring vertices). If G is ﬁnite, then its spectral gap λ(G) is deﬁned as the minimal Laplacian eigenvalue on a function whose sum on V vanishes. When G is inﬁnite,

its spectral gap is deﬁned to be λ(G) = minSpec ∆+ L

2(V ) (for more on this see §3.1).

Moving one dimension higher, let X = (V,E,T) be a k-regular triangle complex. This means that E ⊆ V2 (i.e. E consists of subsets of V of size 2, the edges of X), T ⊆ V3 (the triangles), every edge is contained in exactly k triangles in T, and for every triangle {u,v,w} in T, the edges forming its boundary, {u,v}, {u,w} and {v,w}, are in E.

For {v,w} ∈ E we denote the directed edge •v w• by [v,w], and the set of all directed edges by E± (so that |E±| = 2|E|). For e ∈ E±, e denotes the edge with the same vertices and opposite direction, i.e. [v,w] = [w,v].

The following deﬁnition is the basis of the process which we shall study:

- Deﬁnition 1.1. Two directed edges e,e ∈ E± are called neighbors (indicated by e ∼ e ) if they have the same origin or the same terminus, and the triangle they form is in the complex. Namely, if e = [v,w] and e = [v ,w ], then e ∼ e means that either v = v and {v,w,w } ∈ T, or w = w and {v,v ,w } ∈ T.


We study the following lazy random walk on E±: The walk starts at some directed edge e0 ∈ E±. At every step, the walker stays put with probability 21, or else move to a uniformly chosen neighbor. Figure 1.1 illustrates one step of the process, in two cases (the right one is non-regular, but the walk is deﬁned in the same manner).

As in the random walk on a graph, this process induces a sequence of distributions on E±, pn (e) = pe

n (e),

0

Figure 1.1: One step of the edge walk.

describing the probability of ﬁnding the walker at the directed edge e at time n (having started from e0). However, studying the evolution of pn amounts to studying the traditional random walk on the graph with vertices E± and edges deﬁned by ∼. This will not take us very far, and in particular will not reveal the presence or absence of ﬁrst homology in X. Instead, we study the evolution of what we call the “expectation process” on X:

###### n (e) − pe

###### n (e) = pe

En (e) = Ee

n (e),

0

0

0

i.e. the probability of ﬁnding the walker at time n at e, minus the probability of ﬁnding it at the opposite edge e (for the reasons behind the name see Remark 2.4).

n0 as is done in graphs, but a moment of reﬂection will show the reader that Ee

It is tempting to look at Ee

∞0 = limn→∞ Ee

∞0 ≡ 0 for any ﬁnite triangle complex, and any starting point e0. Namely, the probabilities of reaching e and e become arbitrarily close, for every e. While this might cause initial worry, it turns out that the rate of decay of En is always the same: for any ﬁnite triangle complex one has  Ee

n0 = Θ 34 n . It is therefore reasonable to turn our attention to the normalized expectation process,

###### n (e) = 43 n Ee

###### n (e) = 3 4 n pe

Ee

###### n (e) − pe

n (e) , and observe its limit,

0

0

0

0

Ee

Ee

n .

∞ = lim

0

0

n→∞

For a ﬁnite triangle complex this limit always exists, and is nonzero. This is the object which reveals the ﬁrst homology of the complex.

To see how, we need the following deﬁnition: We say that f : E± → R is exact if its sum along every closed path vanishes; namely, if

v0 ∼ v1 ∼ ... ∼ vn = v0 =⇒

n−1

f ([vi,vi+1]) = 0.

i=0

This is the one-dimensional analogue of constant functions (for reasons which will become clear in §2.2), and the following holds:

(1) For a ﬁnite X, Ee

∞0 is exact for every e0 ∈ E± if and only if G has a trivial ﬁrst homology.

- 1.2 Summary of results 1 INTRODUCTION


- (2) Furthermore, the rate of convergence is given by

Ee

0

n − exact = O 1 −

1 3

λ(X)

n

,

where λ(X) is the spectral gap of X (see Deﬁnition 2.5).

- (3) If X is inﬁnite and every vertex in X is of inﬁnite degree, then its spectral gap (which is deﬁned in §3.2) is revealed by the “return expectation”:


n Ee

n0 (e0) = 1 −

sup

lim

n→∞

e0∈E±

1 3

λ(X).

What if one is interested not only in the existence of a ﬁrst homology, but also in its dimension? The answer is manifested in the walk as well. In graphs the number of connected components is given by the dimension of Span{pv

∞0 |v0 ∈ V }, and an analogue statement holds here (see Theorem 2.9).

Remark. If the non-lazy walk on a ﬁnite graph is observed, then apart from disconnectedness there is another obstruction for convergence to the uniform distribution: bipartiteness. We shall see that this is a special case of an obstruction in general dimension, which we call disorientability (see Deﬁnition 2.6). In our example we have avoided this problem by considering the lazy walk, both on graphs and on triangle complexes.

#### 1.2 Summary of results

We give now a brief summary of the paper and its main results. The deﬁnitions of the terms which appear in this section are explained throughout the paper.

- In §2.1 we deﬁne a p-lazy random walk on the oriented (d − 1)-cells of a d-dimensional complex


n0. In §2.4 it is shown that the limit of this process Eσ

X, and associate with this walk the normalized expectation process Eσ

n0 always exists and captures various properties of X, according to the amount of laziness p (this is an abridged version of Theorem 2.9): Theorem. When d−1

∞0 = limn Eσ

∞0 is exact for every starting point σ0 if and only if the

3d−1 < p < 1, Eσ

(d − 1)-homology of X is trivial. If furthermore p ≥ 12 then the rate of convergence is controlled by the spectral gap of X:

1 − p p(d − 1) + 1

dist Eσ

n , Eσ

∞ = O 1 −

λ(X)

0

0

n

.

When p = 3dd−−11, Eσ

∞0 is exact for every starting point σ0 if and only if the (d − 1)-homology of X is trivial, and in addition X has no disorientable (d − 1)-components (see Deﬁnitions 2.2, 2.6).

Next, we move on to discuss inﬁnite complexes, showing that they present new aspects which do not appear in inﬁnite graphs. In §3.3 we deﬁne a family of simplicial complexes (which we call arboreal complexes) generalizing the notion of trees. In Theorem 3.3 we compute their spectra, generalizing Kesten’s classic result on the spectrum of regular trees [Kes59]. The spectra of the regular arboreal complexes of high dimension and low regularity exhibit a surprising new phenomenon - an isolated eigenvalue.

2 FINITE COMPLEXES

Sections 3.4 and 3.5 are devoted to study the behavior of the spectrum with respect to a limit in the space of complexes. In particular we are interested in the high-dimensional analogue of the Alon-Bopanna theorem, which states that if a sequence of graphs Gn convergences to a graph G, then liminfn→∞ λ(Gn) ≤ λ(G). We ﬁrst show that in general this need not hold in higher dimension (Theorem 3.10). This uses the isolated eigenvalue of the 2-regular arboreal complex of dimension two, which is shown in Figure 3.1, as well as a study of the spectrum of balls in this complex (shown in Figure 3.2).

Even though the Alon-Bopanna theorem does not hold in general in high dimension, we show that under a variety of conditions it does hold (Theorem 3.11):

Theorem. If Xn n−→→∞ X, and one of the following holds:

- (1) The spectral gap of X is nonzero,
- (2) zero is a non-isolated point in the spectrum of X, or
- (3) the (d − 1)-skeletons of the complexes Xn form a family of (d − 1)-expanders,


then

λ(Xn) ≤ λ(X).

liminf

n→∞

- In §3.7 we show that the connection between the spectrum of a graph, and the return probability of the random walk on it (see e.g. [Kes59, Lemma 2.2]), generalizes to higher dimensions (Proposition 3.14).


The ﬁnal section on inﬁnite complexes addresses the high-dimensional analogues of the concepts of amenability, recurrence and transience, proving some properties of these (Proposition 3.17), and raising many open questions.

Acknowledgement. We would like to thank Alex Lubotzky and Gil Kalai who prompted this research, and Jonathan Breuer for many helpful discussions. We are also grateful to Noam Berger, Emmanuel Farjoun, Nati Linial, Doron Puder and Andrzej Żuk for their insightful comments.

### 2 Finite complexes

Throughout this section X is a ﬁnite d-dimensional simplicial complex on a ﬁnite vertex set V . This means that X is comprised of subsets of V , called cells, and the subset of every cell is also a cell. A cell of size j +1 (where −1 ≤ j) is said to be of dimension j, and Xj denotes the set of j-cells - cells of dimension j. The dimension of X is the maximal dimension of a cell in it. The degree of a j-cell σ, denoted deg (σ), is the number of (j + 1)-cells containing it. We shall assume that X is uniform, meaning that every cell is contained in some cell of dimension d = dimX.

For j ≥ 1, every j-cell σ = {σ0,...,σj} has two possible orientations, corresponding to the possible orderings of its vertices, up to an even permutation (1-cells and the empty cell have only one orientation). We denote an oriented cell by square brackets, and a ﬂip of orientation by an overbar. For example, one orientation of σ = {x,y,z} is [x,y,z], which is the same as [y,z,x] and [z,x,y]. The other orientation of σ is [x,y,z] = [y,x,z] = [x,z,y] = [z,y,x]. We denote by

X±j the set of oriented j-cells (so that X±j = 2 Xj for j ≥ 1 and X±j = Xj for j = −1,0), and we shall occasionally denote by X+j a choice of orientation for Xj, i.e. a subset of X±j such that X±j is the disjoint union of X+j and σ σ ∈ X+j .

The faces of a j-cell σ = {v0,...,vj} are the (j − 1)-cells σ\v0,σ\v1,...,σ\vj. An oriented j-cell σ = [v0,...,vj] (2 ≤ j ≤ d) induces an orientation on its faces as follows: the face {v0,...,vi−1,vi+1,...,vj} is oriented as (−1)i [v1,...,vi−1,vi+1,...,vk], where (−1)i means taking the opposite orientation when (−1)i is −1.

Finally, we deﬁne the space of j-forms on X: these are functions on X±j which are antisymmetric w.r.t. a ﬂip of orientation:

Ωj = Ωj (X) = f : X±j → R f (σ) = −f (σ) ∀σ ∈ X±d−1 .

For j = −1,0 there are no ﬂips; Ω0 is just the space of functions on the vertices, and Ω−1 = {f : {∅} → R} can be identiﬁed in a natural way with R. With every oriented j-cell σ ∈ Xj we associate the Dirac j-form σ deﬁned by

 

1 σ = σ −1 σ = σ 0 otherwise

σ (σ ) =



(for j = 0 this is the standard Dirac function, and ∅ is the constant 1).

#### 2.1 The (d − 1)-walk and expectation process

Let X be a uniform d-dimensional complex and 0 ≤ p < 1. The following process is the generalization of the edge walk from §1.1:

- Deﬁnition 2.1. The p-lazy (d − 1)-walk on a d-complex X is deﬁned as follows:


- • Two oriented (d − 1)-cells σ,σ ∈ X±d−1 are said to be neighbors (denoted σ ∼ σ ) if there exists an oriented d-cell τ, such that both σ and σ are faces of τ with the orientations induced by it (see Figure 1.1).

- • The walk starts at an initial oriented (d − 1)-cell σ0, and at each step the walker stays in place with probability p, and with probability (1 − p) chooses uniformly one of its neighbors and moves to it.


Put diﬀerently, it is the Markov chain on X±d−1 with transition probabilities

 

p σ = σ

1−p ddeg(σ) σ ∼ σ 0 otherwise

Prob(Xn+1 = σ |Xn = σ) =

,



(note that σ is contained in deg (σ) d-cells, and thus has d · deg σ neighbors!) We remark that neighboring cells can also be described in the following way: if σ,σ ∈ X±j and

- j ≥ 2, then σ ∼ σ iﬀ the unoriented cell σ ∪ σ is in Xd, and the intersection σ ∩ σ inherits the same orientation from both σ and σ . For j = 1, this can be interpreted as follows: two


edges e,e ∈ X±1 are neighbors if they bound a triangle in the complex, and the vertex at which they intersect “inherits the same orientation from both of them”: it is either the origin of both e

- and e , or the terminus of both. Finally, for j = 0 Deﬁnition 2.1 gives the standard neighboring relation and p-lazy random walk on a graph.


- Deﬁnition 2.2. We say that X is (d − 1)-connected if the (d − 1)-walk on it is irreducible, i.e.,

for every pair of oriented (d − 1)-cells σ and σ there exist a chain σ = σ0 ∼ σ1 ∼ ... ∼ σn = σ . Moreover, having such a chain deﬁnes an equivalence relation on the (d − 1)-cells of X, whose classes we call the (d − 1)-components of X.

Remark. Due to the assumption of uniformity, it is enough to observe unoriented cells - X is (d − 1)-connected iﬀ for every σ,σ ∈ Xd−1 there exists a chain of unoriented (d − 1)-cells σ = σ0,σ1,...,σn = σ with σi ∪σi+1 ∈ Xd for all i. This is also equivalent to the assertion that for any τ,τ ∈ Xd there is a chain τ = τ0,τ1,...,τm = τ of d-cells with τi ∩ τi−1 ∈ Xd−1 for all i (this is sometimes referred to as a chamber complex). We note that it follows from uniformity that a (d − 1)-connected complex is connected as a topological space. The other direction does not hold: the complex is not 1-connected, even though it is connected (and uniform).

Observing the (d − 1)-walk on X, we denote by pσ

n0 (σ) the probability that the random walk starting at σ0 reaches σ at time n. We then have:

- Deﬁnition 2.3. For d ≥ 2, the expectation process on X starting at σ0 is the sequence of


n0}∞n=0 deﬁned by

(d − 1)-forms {Eσ

n (σ) − pσ

n (σ) = pσ

Eσ

n (σ). For d = 1 (i.e. graphs) we simply deﬁne Ev

0

0

0

n0.† The normalized expectation process is deﬁned to be

n0 = pv

n

n

d p(d − 1) + 1

d p(d − 1) + 1

Eσ

[pσ

Eσ

n (σ) − pσ

n (σ) =

n (σ)],

n (σ) =

0

0

0

0

n0 for all p. The reason for this particular normalization is that for a lazy enough process (in particular for p ≥ 12) one has  Eσ

where p is the laziness of the walk. In particular, for d = 1 one has Ev

n0 = pv

n0 = Ev

n

n0 = Θ p(d−d1)+1

(see (2.8)). Note that Eσ

0 = Eσ

. Remark 2.4. The name “expectation process” comes from the fact that for any (d − 1)-form f Eσ

0 = σ

0

0

0

Eσ

##### pσ

n (σ)f (σ)

n (σ)f (σ) =

n [f] =

0

0

0

σ∈Xd−1

σ∈X±d−11

where, as implied by the notation, Eσ

n0 (σ)f (σ) does not depend on the orientation of σ. The evolution of the expectation process over time is given by Eσ

n0, where A = A(X,p) is the transition operator acting on Ωd−1 by

n+1 = AEσ

0

(1 − p) d σ ∼σ

f (σ ) deg (σ )

f ∈ Ωd−1,σ ∈ Xd−1 . (2.1)

(Af)(σ) = pf (σ) +

Note that the evolution of pσ

n0 is given by the same A, acting on all functions from X±d to R,

and not only on forms. It is sometimes useful to observe the Markov operator M = M (X,p) associated with this evolution, which is characterized by

Eσ

n+1 [f] = Eσ

n [Mf],

0

0

† The results in the paper hold for graphs as well, using this deﬁnition of Env0, but they are all familiar theorems. In some cases the proofs are slightly diﬀerent, and we will not trouble to handle this special case.

and is given explicitly by (Mf)(σ) = pf (σ) +

1 − p ddeg (σ) σ ∼σ

f (σ ) f ∈ Ωd−1,σ ∈ Xd−1 .

This is the transpose of A, w.r.t. to a natural choice of basis for Ωd−1 (X).

#### 2.2 Simplicial complexes and Laplacians

For a cell σ and a vertex v ∈/ σ, we write v σ if vσ = {v} ∪ σ is a cell in X. If σ is oriented, σ = [σ0,...,σk], and v σ, then vσ denotes the oriented cell [v,σ0,...,σk]. For 0 ≤ k ≤ d, the kth boundary operator ∂k : Ωk → Ωk−1 is deﬁned by

(∂kf)(σ) =

f (vσ).

v σ

In particular ∂0 : Ω0 → Ω−1 is deﬁned by (∂0f)(∅) = v∈X0 f(v). The sequence Ωk,∂k is the simplicial chain complex of X, meaning that ∂k∂k+1 = 0 for all

- k, giving rise to the k-cycles Zk = ker∂k, the k-boundaries Bk = im∂k+1 and the (real) kthhomology Hk = Zk/Bk. Given a weight function w : X → (0,∞), Ωk become inner product spaces (for −1 ≤ k ≤ d) with


w(σ)f(σ)g(σ) ∀f,g ∈ Ωk.

f,g =

σ∈Xk

Note that the sum is over Xk and not X±k - this is well deﬁned since the value of f (σ)g (σ) is independent of the orientation of σ.

Since X is ﬁnite the spaces Ωk are ﬁnite dimensional, and there exist adjoint operators to the boundary operators ∂k. These are the co-boundary operators, which are denoted by δk = ∂k∗ : Ωk−1 → Ωk, and are given by

k

1 w (σ)

(−1)i w (σ\σi)f (σ\σi) 0 ≤ k ≤ d.

(δkf)(σ) = (∂k∗f)(σ) =

i=0

We will stick with the notation ∂k∗ until we get to inﬁnite complexes, where sometimes δk is deﬁned even though ∂k is not. The simplicial cochain complex of X is (Ωk,δk), and Zk = kerδk+1, Bk = imδk, Hk = Zk/Bk are the cocycles, coboundaries and cohomology, respectively. Cocycles are also known as closed forms, and coboundaries as exact forms.

The following weight functions will be used throughout this paper†:

1 degσ σ ∈ Xd−1 1 σ ∈ X\Xd−1

w (σ) =

.

Notice that for σ ∈ Xd−1

1 w (σ)

1 d

σ ∈ Xd−1 σ ∼ σ .

= deg (σ) = τ ∈ Xd σ ⊂ τ = |{v |v σ}| =

† Another natural weight function is the constant one. The obtained Laplacians are more convenient for isoperimetric analysis. For more details see [PRT12].

Due to our choice of weights, the inner product and coboundary operators are given by

 

f (σ)g (σ) f,g ∈ Ωk,k = d − 1

σ∈Xk

f,g =

f(σ)g(σ)

degσ f,g ∈ Ωd−1



σ∈Xd−1



k

(−1)i f (σ\σi) k ≤ d − 2 deg (σ)

i=0



d−1

(−1)i f (σ\σi) k = d − 1

(δkf)(σ) = (∂k∗f)(σ) =

i=0

(−1)i f (σ\σi) deg (σ\σi)

d



k = d.

i=0

Finally, the upper, lower, and full Laplacians ∆+,∆−,∆ : Ωd−1 → Ωd−1 are deﬁned by:

∆+ = ∂dδd = ∂d∂d∗ ∆− = δd−1∂d−1 = ∂d∗−1∂d−1 ∆ = ∆+ + ∆−.

An explicit calculation gives

(2.2)

(2.3)

d

(−1)i f (vσ\(vσ)i) deg (vσ\(vσ)i)

(∂d∗f)(vσ) =

∆+f (σ) =

v σ

v σ

i=0

(2.4)

d−1

(−1)i f (v (σ\σi)) deg (v (σ\σi))

f (σ ) deg (σ )

= f (σ) −

= f (σ) −

v σ

σ ∼σ

i=0

and

d−1

(−1)i

∆−f (σ) = deg σ

f (vσ\σi). (2.5)

i=0

v σ\σi

More generally, one can deﬁne the k-th upper, lower and full Laplacians ∆+k = ∂k+1δk+1, ∆−k = δk∂k and ∆k = ∆+k + ∆−k . Apart from k = d − 1, these will only make a brief appearance in §3.5. The kernel of ∆k is the space of harmonic k-forms, denoted by Hk = Hk (X).

The spaces deﬁned so far are related by

Zk = ker∂k = ker∆−k Bk = Zk ⊥ = im∂k+1 = im∆+k Zk = kerδk+1 = ker∆+k Bk = Zk⊥ = imδk = im∆−k

Hk = ker∆k = Zk ∩ Zk = Bk ⊕ Bk ⊥ ∼= Hk ∼= Hk

The isomorphism between harmonic functions, homology and cohomology, which is sometimes called the discrete Hodge theorem, was ﬁrst observed in [Eck44]. In a similar manner, there is a “discrete Hodge decomposition”

Zk

Ωk =

Bk ⊕ Hk ⊕ Bk

, (2.6)

Zk

and all the Laplacians decompose with respect to it. All of these claims follow by linear algebra, using the fact that Ωk is ﬁnite-dimensional (see [PRT12, §2] for the details). For inﬁnite complexes the situation is more involved, and is addressed in §3.2.

#### 2.3 The upper Laplacian spectrum

In this section we study the spectrum of the upper Laplacian ∆+ of a ﬁnite complex X. First note that as ∆+ = ∂d∂d∗, its spectrum is non-negative. Furthermore, zero is obtained precisely on closed forms, i.e. ker∆+ = Zd−1. The space of closed forms always contains the exact forms, Bd−1 = im∂d∗−1, which are considered the trivial zeros in the spectrum of ∆+. The existence of nontrivial zeros in the spectrum of ∆+, i.e. closed forms which are not exact, indicates the existence of a nontrivial homology. This leads to the following deﬁnition:

- Deﬁnition 2.5. The spectral gap of a ﬁnite d-dimensional complex X, denoted λ(X), is

λ(X) = minSpec ∆+|Zd−1

= minSpec ∆|Zd−1

. The essential gap of X, denoted λ˜(X), is

λ(X) = minSpec ∆+|Bd−1

= minSpec ∆|Bd−1 (the transition from ∆ to ∆+ follows from the fact that ∆− vanishes on Zd−1.)

Since λ vanishes precisely when the (d − 1)-homology of X is nontrivial, it should be thought of as giving a quantitative measure for the “triviality of the homology”. For example, in graphs, having λ(X) far away from zero is a measure of high-connectedness, or “high triviality of the 0th-homology”.

In contrast, λ never vanishes, as Bd−1 = Zd−1 ⊥ = (ker∆+)⊥. If the (d − 1)-homology is nontrivial then λ = λ, so that λ is only of additional interest when the homology vanishes. In a disconnected graph λ controls the mixing rate as λ does for a connected graph, and we will see that the same happens in higher dimension (see (2.10)).

Until now we have studied one extremity of Spec∆+. The other side relates to the following deﬁnition:

- Deﬁnition 2.6. A disorientation of a d-complex X is a choice of orientation X+d of its d-cells,


so that whenever σ,σ ∈ X+d intersect in a (d − 1)-cell they induce the same orientation on it. If X has a disorientation it is said to be disorientable.

Remarks.

- (1) A disorientable 1-complex is precisely a bipartite graph, and thus disorientability should be thought of as a high-dimensional analogue of bipartiteness. Another natural analogue is “(d + 1)-partiteness”: having some partition A0,...,Ad of V so that every d-cell contains one vertex from each Ai. A (d + 1)-partite complex is easily seen to be disorientable, but the opposite does not necessarily hold for d ≥ 2.
- (2) Notice the similarity to the notion of orientability: a d-complex is orientable if there is a choice of orientations of its d-cells, so that cells intersecting in a codimension one cell induce opposite orientations on it. However, orientability implies that (d − 1)-cells have degrees at most two, where as disorientability impose no such restrictions. Note that a complex can certainly be both orientable and disorientable (e.g. Figure 2.1(a)).


- Proposition 2.7. Let X be a ﬁnite complex of dimension d.


- (1) Spec∆+ (X) is the disjoint union of Spec∆+ (Xi) where Xi are the (d − 1)-components of X.


- (2) The spectrum of ∆+ = ∆+ (X) is contained in [0,d + 1].
- (3) Zero is achieved on the closed (d − 1)-forms, Zd−1.
- (4) If X is (d − 1)-connected, then d+1 is in the spectrum iﬀ X is disorientable, and is achieved on the boundaries of disorientations (see (2.7)).


Proof. (1) follows from the observation that ∆+ decomposes w.r.t. the decomposition Ωd−1 (X) = i Ωd−1 (Xi). We have already seen (3), and the fact that the spectrum is nonnegative. Now, assume that ∆+f = λf. Choose σ ∈ Xd−1 which maximize deg(|f(σσ)|). By (2.4),

f (σ ) deg (σ ) and therefore

λf (σ) = ∆+f (σ) = f (σ) −

σ ∼σ

|f (σ )| deg (σ ) ≤ (d + 1)|f (σ)|,

|λf (σ)| ≤ |f (σ)| +

σ ∼σ

(since #{σ |σ ∼ σ} = ddeg σ), hence λ ≤ d + 1 and (2) is obtained. Next, assume that X is (d − 1)-connected and that X+d is a disorientation. Deﬁne

F (τ) =

1 τ ∈ X+d −1 τ ∈ X±d \X+d

, (2.7)

- and f = ∂dF. For any σ ∈ X±d−1, there exists some vertex v with v σ (since X is uniform). Furthermore, by the assumption on X+d, if v   σ and v   σ for vertices v,v then vσ ∈ X+d if and only if v σ ∈ X+d, and thus


f (σ) = (∂dF)(σ) =

F (vσ) = deg (σ)F (τ)

v σ

where τ is any d-cell containing σ. If σ and σ are neighboring (d − 1)-faces in X±d−1, then by deﬁnition, for some τ ∈ X±d , σ is a face of τ and σ is a face of τ, so that

f (σ ) deg σ

f (σ) deg σ

+

= F (τ) + F (τ) = 0,

and consequently for any σ ∈ X±d−1

f (σ ) deg (σ )

∆+f (σ) = f (σ) −

= f (σ) −

σ ∼σ

σ ∼σ

so that f is a ∆+-eigenform with eigenvalue d + 1.

−f(σ) deg (σ)

= (d + 1)f (σ),

In the other direction, assume that X is (d − 1)-connected and that ∆+f = (d + 1)f for some f ∈ Ωd−1 (X)\{0}. Fix some σ ∈ X±d−1 which maximize |degf(σσ)|, normalize f so that |degf( σ σ)| = 1, and deﬁne

∂d∗f d + 1

, X+d = τ ∈ X±d F (τ) > 0 .

F =

∗ df

+f

d+1 = ∂d∂

We have f = ∆

d+1 = ∂dF by assumption, and we proceed to show that X+d is a disorientation with F the corresponding form as in (2.7). By the deﬁnition of ∆+

|f (σ)| deg (σ) ≤

f (σ) deg (σ) ≤

1 d σ∼ σ

1 d σ∼ σ

1 d σ∼ σ

deg σ = |f ( σ)| =

1 = deg σ,

so that |degf(σσ)| = 1 for every σ ∼ σ. Continuing in this manner, (d − 1)-connectedness implies that |degf(σσ)| ≡ 1 on all X±d . Using again the deﬁnition of ∆+, for any σ in X±d

f (σ) deg σ

1 deg σ · d σ ∼σ

f (σ ) deg (σ )

= −

.

Since the r.h.s is an average over terms whose absolute value is that of the l.h.s this gives f(σ ) degσ = −degf(σσ) whenever σ ∼ σ , hence

1 d + 1

F (τ) =

i=0

d

(−1)i f (τ\τi) deg (τ\τi)

f (τ\τ0) deg (τ\τ0)

=

is always of absolute value one. Furthermore, if τ,τ ∈ X±d intersect in a face σ and induce opposite orientations on it, then τ = vσ and τ = v σ for some vertices v,v , hence

f (σ) deg σ

F (τ) = F (vσ) =

which concludes the proof.

= F (v σ) = −F v σ = −F (τ )

| |
|---|


- 2.4 Walk and spectrum The (d − 1)-walk deﬁned in §2.1 is related to the Laplacians from §2.2 as follows:


- Proposition 2.8. Observe the p-lazy (d − 1)-walk on X starting at σ0 ∈ X±d−1. Then


- (1) The transition operator A = A(X,p) is given by

A =

p(d − 1) + 1 d · I −

1 − p

d · ∆+, so that

Eσ

0

n = AnEσ

0

0 =

p(d − 1) + 1 d · I −

1 − p d · ∆+

n

Eσ

0

0 .

- (2) The spectrum of A is contained in 2p − 1, p(d−d1)+1 , with 2p − 1 achieved by disorientations, and p(d−d1)+1 by closed forms (Zd−1).

- (3) The expectation process satisﬁes


n

p(d − 1) + 1 d

p(d − 1) + 1 d

1 Kd−2Kd−1

≤  Eσ

n ≤ max |2p − 1|,

0

where Kj is the maximal degree of a j-cell in X.

n

(2.8)

Proof. (1) follows trivially from (2.1) and (2.4), and Proposition 2.7 then implies (2). The upper bound in (3) follows from (2) by Eσ

n0 = AnEσ

###### 0 and  Eσ

≤ 1. For the lower bound, let v be a vertex in σ0, and σ0,...,σk the (d − 1)-cells containing σ0\v. Deﬁne f = ∂d∗ σ

###### = √deg1 σ

0 = σ

0

0

0

0

0\v = ki=0 deg σi · σi

, so that f ∈ Zd−1 and f 2 = ki=0 deg σi ≤ Kd−2Kd−1. Since

∆+ decomposes w.r.t. the orthogonal sum Ωd−1 = Zd−1⊕Bd−1 so does A = p(d−d1)+1·I−1−dp·∆+, hence by (2)

n

n

) ≥ p(d−d1)+1

0 ≥ p(d−d1)+1

f f , σ

 Eσ

n = An σ

PZd−1 ( σ

0

0

0

n |f (σ0)| f deg σ0 ≥

n

1 Kd−2Kd−1

= p(d−d1)+1

p(d−1)+1 d

.

| |
|---|


This proposition leads to the connection between the asymptotic behavior of the (d − 1)-walk and the homology and spectrum of the complex:

- Theorem 2.9. Let Enσ be the normalized expectation process associated with the p-lazy (d − 1)-


walk on X starting from σ (see Deﬁnitions 2.1, 2.3). Then E∞σ = limn→∞ Enσ exists and satisﬁes the following:

- (1) If d−1

3d−1 < p < 1, then E∞σ is exact for every starting point σ if and only if Hd−1(X) = 0.† If furthermore p ≥ 12 then

dist Enσ,Bd−1 = O 1 −

1 − p p(d − 1) + 1

λ(X)

n

. (2.9)

- (2) More generally, the dimension of Hd−1 (X) equals the dimension of

Span PZ

d−1 E∞σ σ ∈ Xd−1 .

- (3) If p = 3dd−−11 then E∞σ is exact for all σ if and only if X has a trivial (d − 1)-homology and no disorientable (d − 1)-components.

- (4) More generally, if d−1


3d−1 < p < 1 then E∞σ is closed, and likewise for p = 3dd−−11, unless X has a disorientable (d − 1)-component. If p ≥ 12 then

n

1 − p p(d − 1) + 1

dist Enσ,Zd−1 = O 1 −

. (2.10)

λ(X)

Proof.

- Case (i) − 3dd−−11 < p < 1: We have |2p − 1| < p(d−d1)+1, so that A = maxSpecA = p(d−1)+1


d . Thus,

SpecA B

d−1

p(d − 1) + 1 d ⊆ (− A , A ).

⊆ 2p − 1,

† Note that the ﬁrst value of p for which the homology can be studied via the walk in every dimension is p = 13.

###### Since A decomposes w.r.t. Ωd−1 = Bd−1 ⊕ Zd−1, and A Z

, this means that

###### = A · I Z

d−1

d−1

n

n

n

E0σ, which shows that

converges to the orthogonal projection PZd−1. Now Enσ = p(d− d1)+1

A A

Enσ = A A

E∞σ = PZd−1 E0σ = PZd−1 (E0σ) = PZd−1 ( σ). (2.11)

In particular E∞σ is closed, so that if the homology of X is trivial then it is exact. On the other hand, assume that E∞σ is exact for all σ: then

E∞σ = PZd−1 (E0σ) = PZd−1 ( σ) = PBd−1 ( σ) + PHd−1 ( σ)

so that PHd−1 ( σ) = 0 by (2.6). As { σ} span Ωd−1, this shows that Hd−1 ∼= Hd−1 = 0. To further understand the dimension of the homology, observe that

d−1 E∞σ σ ∈ Xd−1 = Hd−1 (X), which follows from

Span PZ

d−1 E∞σ = PZ

PZ

(PZd−1 ( σ)) = PHd−1 ( σ).

d−1

If p ≥ 21 then we know not only that A = maxSpecA but also that A Z

###### = maxSpec A Z

d−1

, which allows us to say more. In this case A is positive semideﬁnite, so that (2.10) follows by

d−1

n

d p(d − 1) + 1

d p(d − 1) + 1

− PZd−1 =

A

A B

n

1 − p p(d − 1) + 1 · ∆+

= I −

which gives (2.9) as well when the homology is trivial.

n

d−1

1 − p p(d − 1) + 1

Bd−1 = 1 −

λ(X)

n

,

- Case (ii) − p = 3dd−−11: Now, |2p − 1| = p(d−d1)+1 = A . If X has no disorientable (d − 1)-


components then again SpecA B

⊆ (− A , A ), which gives (2.11), and everything is as before. On the other hand, let us assume that E∞σ is closed for all σ. Denoting by Ωλd−1 the λ-eigenspace of A, now p(d− d1)+1A

d−1

2n

###### (∆+ is diagonalizable and consequently so is A). Since E∞σ is closed this shows that PΩd−1

converges to PZd−1 + PΩd−1

2p−1

( σ) = 0, and consequently that

2p−1

Ωd2p−−11 = 0, i.e. X has no disorientable (d − 1)-components. Remarks.

| |
|---|


- (1) The study of complexes via (d − 1)-walk gives a conceptual reason to the fact that the highdimensional case is harder than that of graphs: while graphs are studied by the evolution of probabilities, analogue properties of high-dimensional complexes are reﬂected in the expectation process. As this is given by the diﬀerence of two probability vectors, it is much harder to analyze. Several examples of this appear in the open questions in §4.
- (2) In order to study the connectedness of a graph it is enough to observe the walk starting


at one vertex. If pv

∞0 is not exact (i.e. not proportional to the degree function) for even one v0, then the graph is necessarily disconnected. In general dimension, however, this is not enough: there are complexes (even (d − 1)-connected ones!) with nontrivial (d − 1)-

homology, such that E∞σ is exact for a carefully chosen σ.

3 INFINITE COMPLEXES

- (3) If one starts the process with a general initial distribution p0 instead of the Dirac probability σ, then Theorem 2.9 holds for the corresponding expectation process (i.e. E0 (σ) = p0 (σ)−p0 (σ), En+1 = AEn). Furthermore, in these settings a disorientable com-


ponent corresponds to a distribution for which En is 2-periodic for p = 3dd−−11 (see Figure 2.1(a)); a nontrivial homology corresponds to a distribution which induces a stationery

non-exact En for p ≥ 3dd−−11 (see Figure 2.1(b)).

(a) (b) Figure 2.1: Two distributions on the edges of 2-complexes (the orientations drawn have uniform probability, and their inverses probability zero). (a) is a distribution for which En = 3 5 n En is 2-periodic under the 15-lazy walk; (b) is a distribution for which En is stable and non exact (under the p-lazy walk, p > 51).

### 3 Inﬁnite complexes

#### 3.1 Inﬁnite graphs

We move to the case of inﬁnite complexes, starting with inﬁnite graphs. Recall that for a ﬁnite graph G = (V,E), we observed ∆+ = ∆+ (G), and deﬁned

λ(G) = minSpec∆+ (B

0)⊥ = minSpec∆+ Z

.

0

In contrast, when G is an inﬁnite graph (i.e. |V | = ∞) one usually restrict his attention to L2 (V ) and deﬁne

λ(G) = minSpec∆+ L

2(V ). (3.1)

Here there is no restriction to Z0, nor to B0 ⊥. These two spaces, which coincide in the ﬁnite dimensional case, since

Z0 = ker∂0 = (im∂0∗)⊥ = B0 ⊥ , (3.2) fail to do so in the inﬁnite settings. First, Z0 is not even deﬁned, as (∂0f)(∅) = v∈V f (v) has no meaning for general f ∈ L2 (V ). One can observe B0 = imδ0, taking (2.3) as the deﬁnition of δ0 (as ∂0 is not deﬁned). With this deﬁnition, B0 consists of the scalar multiples of the degree function. Since these are never in L2 (V ) (assuming as always that there are no isolated vertices), we have B0 = 0 and B0 ⊥ = L2 (V ), justifying (3.1). Another thing which fails here is the chain complex property ∂0∂1 = 0: there may exist f ∈ Ω1 (G) such that ∂0∂1f is deﬁned and nonzero. For example, take V = Z, E = {{i,i+1}|i ∈ Z}, and f ([i,i+1]) =

- 0 i < 0
- 1 0 ≤ i


. Here

∂1f = 0, and thus (∂0∂1f)(∅) = 1. If G is transient, e.g. the Z3 graph, or a k-regular tree with k ≥ 3, there are even such f in L2 - see §3.8.

- 3.2 Inﬁnite complexes of general dimension 3 INFINITE COMPLEXES


#### 3.2 Inﬁnite complexes of general dimension For a complex X of dimension d, and −1 ≤ k ≤ d, we denote

ΩkL2 = ΩkL2 (X) = f ∈ Ωk (X) f 2 < ∞ ⊆ Ωk (X), where we recall that

f 2 =

k f (σ)2 k = d − 1

w (σ)f (σ)2 = σ∈X

.

f(σ)2 degσ k = d − 1

σ∈Xk

σ∈Xk

Whenever referring to inﬁnite complexes, the domain of all operators (i.e. ∂,δ,∆+,∆−,∆) is assumed to be ΩkL2, unless explicitly stated that we are interested in Ωk.

Let us examine these operators. We shall always assume that the (d − 1)-cells in X have globally bounded degrees, which ensures that the boundary and coboundary operators ∂d : Ωd → Ωd−1, δd : Ωd−1 → Ωd are deﬁned, bounded, and adjoint to one another, so that ∆+ = ∂dδd = ∂d∂d∗ is bounded and self-adjoint. We do not assume that the degrees in other dimensions are bounded, as this would rule out inﬁnite graphs, for example. This means that in general δk does not take ΩkL−2 1 into ΩkL2 but only to Ωk, and ∂k need not even be deﬁned. In particular, one cannot always deﬁne ∆−.

The cochain property δkδk−1 = 0 always holds, whereas in general ∂k−1∂k (f) can be deﬁned and nonzero for some f ∈ ΩkL2. If the degrees of (k − 1)-cells are bounded, then δk and ∂k are bounded and δk = ∂k∗. Thus, if the degrees of (k − 1)-cells and (k − 2)-cells are globally bounded one has ∂k−1∂k = (δkδk−1)∗ = 0∗ = 0 as well.

In contrast with inﬁnite graphs, an inﬁnite d-complex may have (d − 2)-cells of ﬁnite degree, so that the image of δd−1 may contain L2-coboundaries. For example, if v is a vertex of ﬁnite degree in an inﬁnite triangle complex, then the “star” δ1 v is an L2-coboundary. We denote by Bd−1 the L2-coboundaries, i.e. Bd−1 = imδd−1 ∩ ΩLd−21. In order to avoid trivial zeros in the spectrum of ∆+, we deﬁne Zd−1 = Bd−1 ⊥ (the orthogonal complement in ΩLd−21), and

λ(X) = minSpec∆+ Z

.

d−1

We stress out that Zd−1 is not necessarily the kernel of ∂d−1 (which is not even deﬁned in general). If the (d − 2)-degrees are globally bounded then ∂d−1 is deﬁned and dual to δd−1, and this gives inclusion in one direction:

Zd−1 = Bd−1 ⊥ = (imδd−1)⊥ ⊆ ker∂d−1. (3.3) For ﬁnite complexes there is an equality here (as in (3.2)) due to dimension considerations.

2(V ). The following lemma shows that this happens whenever all (d − 2)-cells are of inﬁnite degree: Lemma 3.1. If X is a d-complex whose (d − 2)-cells are all of inﬁnite degree, then Bd−1 = 0 and thus λ(X) = minSpec∆+.

In inﬁnite graphs we had B0 = 0, Z0 = Ω0L2 = L2 (V ) and λ = minSpec∆+ L

Proof. Let f ∈ Ωd−2 be such that δd−1f ∈ ΩLd−21\{0}. Choose τ ∈ X±d−2 for which f (τ) > 0, and let {σi}∞i=1 be a sequence of (d − 1)-cells containing τ. Since ∞i=1 (δd−1f)2 (σi) ≤ δd−1f 2 <

∞, for inﬁnitely many i we have |(δd−1f)(σi)| ≤ f(2τ). Since τ contributes f (τ) to (δd−1f)(σi), one of the other faces of σi must be of absolute value at least 2(fd(−τ)1). Since these faces are all diﬀerent (d − 2)-cells (if σi ∩ σj contains τ and another (d − 2)-cell, then σi = σj), we have

f = ∞.

| |
|---|


#### 3.3 Example - arboreal complexes

Deﬁnition 3.2. We say that a d-complex is arboreal if it is (d − 1)-connected, and has no simple d-loops. That is, there are no non-backtracking closed chains of d-cells, σ0,σ1,...,σn = σ0 s.t. dim(σi ∩ σi+1) = d−1 (σi and σi+1 are adjacent) and σi = σi+2 (the chain is non-backtracking).

For d = 1, these are simply trees. As in trees, there is a unique k-regular arboreal d-complex for every k ∈ N, and we denote it by Tkd. It can be constructed as follows: start with a d-cell, and attach to each of its faces k − 1 new d-cells. Continue by induction, adding to each face of a d-cell in the boundary k − 1 new d-cells at every step. For example, the 2-regular arboreal triangle complex T22 can be thought of as an ideal triangulation of the hyperbolic plane, depicted in Figure 3.1.

Figure 3.1: The 2-regular arboreal triangle complex T22. The following theorem describes the spectrum of regular arboreal complexes:

- Theorem 3.3. The spectrum of the non-lazy transition operator on the k-regular arboreal dcomplex is


 

√

√

kd , 1−d+2

d(k−1)

d(k−1)

1−d−2

kd ∪ d 1 2 ≤ k ≤ d 1−d−2

SpecA Tkd,0 =

(3.4)

√

√

kd , 1−d+2

d(k−1)

d(k−1)



kd d < k.

Remarks.

- (1) For d = 1 this gives the spectrum of the k-regular tree, which is a famous result of Kesten [Kes59]:


2√k − 1 k

2√k − 1 k

SpecA Tk1,0 = −

,

.

- (2) Since for 2 ≤ k ≤ d the value d1 is an isolated value of the spectrum of Tkd, it follows that it is in fact an eigenvalue. This is a major diﬀerence from the case of graphs, where the value 1 d = 1 cannot be an eigenvalue for inﬁnite graphs. This phenomena will play a crucial role in the counterexample for the Alon-Boppana theorem in general dimension (see §3.5-3.6).

- (3) Another phenomena which does not occur in the case of graphs, is that in the region 2 ≤ k ≤ d the spectrum expands as k becomes larger. The spectrum is maximal (as a set) for k = d+1, where SpecA Tdd+1,0 = −d3(dd−+1)1 , d1 , merging with the isolated eigenvalue which appear for smaller k.

- (4) The spectra of the Laplacian ∆+ = ∆+ Tkd , and of the p-lazy transition operator Ap = A Tkd,p , are obtained from (3.4) using ∆+ = I − d · A and Ap = p · I + (1 − p) · A.


In order to prove Theorem 3.3 we will need the following lemma, for the idea of which we are indebted to Jonathan Breuer:

- Lemma 3.4. Let X be any set, and L2(X) the Hilbert space of complex functions of ﬁnite L2norm on X (with respect to the counting measure). Let A be a bounded self adjoint operator on L2(X), and a < b ∈ R, such that the following hold:


- (1) For every x ∈ X and a ≤ λ ≤ b, there exists ψxλ ∈ L2(X) such that (A − λI)ψxλ = x.
- (2) The integral


´ b

a c(λ)2 dλ is ﬁnite, where c(λ) = sup x∈X

ψxλ .

Then (a,b) ∩ Spec(A) = ∅.

Proof. We show that P[a,b], the spectral projection of A on the interval [a,b], is zero, and the conclusion (a,b) ∩ Spec(A) = ∅ follows by the spectral theorem. Stone’s formula states that

ˆ b

- 1

- 2πi


- 1

- 2


(A − λ − iε)−1 − (A − λ + iε)−1 dλ = P(a,b) +

P{a,b}

(s)lim

ε↓0

a

where P(a,b) and P{a,b} the spectral projections of A on (a,b) and {a,b} respectively, and (s)lim denotes a limit in the strong sense. Denoting P = P(a,b) + 21P{a,b}, this gives for every x ∈ X

ˆ b

- 1

- 2πi


(A − λ − iε)−1 − (A − λ + iε)−1 x, x dλ = P x, x Evaluating the right hand side we get

lim

ε↓0

a

- 1

- 2πi


P x, x = lim ε↓0

- 1

- 2πi


= lim

ε↓0

- 1

- 2πi


= lim

ε↓0

ˆ b

ε π

= lim

ε↓0

ˆ b

ε π

≤ lim

ε↓0

ˆ b

a

ˆ b

a

ˆ b

a

(A − λ − iε)−1 − (A − λ + iε)−1 x, x dλ

(A − λ − iε)−1 − (A − λ + iε)−1 (A − λ)ψxλ,(A − λ)ψxλ dλ

(A − λ + iε)−1 [A − λ + iε − A + λ + iε](A − λ − iε)−1 (A − λ)2 ψxλ,ψxλ dλ

a

a

(A − λ)2 + ε2 −1 (A − λ)2 ψxλ,ψxλ dλ

(A − λ)2 + ε2 −1 (A − λ)2 c(λ)2 dλ.

2

Deﬁning fε,λ (t) = (t−λ)

(t−λ)2+ε2, we have |fε,λ (t)| ≤ 1 for every t,λ ∈ R and ε > 0, and thus fε,λ (A) ≤ 1. Therefore, using (2), the last limit above is zero. Consequently, for any x,y ∈ X

- 1

- 2


- 1

- 2


· P y,P y

| P x, y | = | P x,P y | ≤ P x,P x

= 0. It follows that for general f ∈ L2(X)

Pf,f = P

f(v)f(w) P x, y = 0,

f(x) x ,

f(y) y =

x∈X

y∈X

x,y∈X

which implies that P = 0, hence also P(a,b) and P{a,b}, and therefore also P[a,b].

| |
|---|


√

Proof of Theorem 3.3. Let X = Tkd, and Λ± = 1−d±2

d(k−1)

kd . The proof is separated into two

parts. First we prove that every Λ− ≤ λ ≤ Λ+, and also λ = d1 when k ≤ d, is in the spectrum, by exhibiting an appropriate eigenform or an approximate one. In the second part we use Lemma

- 3.4 to prove that there are no other points in the spectrum.


Deﬁne an orientation X+d−1 as follows: choose an arbitrary (d − 1)-cell σ0 ∈ X±d−1 and place it in X+d−1. Then add to X+d−1 all the k · d neighbors of σ0. Next, for every neighbor τ of the recently added k · d cells, add τ to X+d−1, unless τ or τ is already there. Continue expanding in this manner, adding at each stage the neighbors of the last “layer” which are further away from the starting cell σ0. Apart from orientation, this process gives X+d−1 a layer structure: {σ0} is the 0th layer, its neighbors the 1st layer, and so on. We denote by Sn (X,σ0) the nth layer, and also write Bn (X,σ0) = k≤n Sk (X,σ0) for the “nth ball” around σ0. Figure 3.2 demonstrates this for the ﬁrst four layers of T22.

| |
|---|
| |


| |
|---|
| |


B0 T22,σ0 B1 T22,σ0 B2 T22,σ0

B3 T22,σ0 Figure 3.2: The orientation at the zeroth, ﬁrst, second, and third layers of X = T22.

We shall study X+d−1-spherical forms, i.e. forms in Ωd−1 (X) which are constant on each layer of X+d−1. For such a form f we will make some abuse of notation and write f (n) for the value of f on the cells in the nth layer of X+d−1. As in regular trees, if one allows forms which are not in L2, then for every λ ∈ R there is a unique (up to a constant) X+d−1-spherical eigenform f with eigenvalue λ. This form is given explicitly by

α+ − λ

λ − α− α+ − α− · α+n +

α+ − α− · α−n , where

f(n) =

d − 1 + dkλ ± (d − 1 + dkλ)2 − 4d(k − 1) 2d(k − 1)

, (3.5)

α± =

except for the case α+ = α−, which happens when λ ∈ {Λ−,Λ+}. In this case f is given by

n−1

n

(d − 1) + dkλ 2d(k − 1)

(d − 1) + dkλ 2d(k − 1)

f(n) = (1 − n)

+ λn

,

but this will not concern us as the spectrum is closed, and it is therefore enough to show that (Λ−,Λ+) is contained in it to deduce this for [Λ−,Λ+]. The term inside the root in (3.5) is negative for Λ− < λ < Λ+, hence in this case |α+| = |α−| = √ 1

. We claim the following: for any Λ− < λ < Λ+ there exist 0 < c1 < c2 < ∞ (which depend on λ) such that

d(k−1)

- (1) For all n ∈ N,

|f (n)| ≤ c2

1 d(k − 1)

n

. (3.6)

- (2) For inﬁnitely many n ∈ N,


n

1 d(k − 1)

≤ |f (n)|. (3.7)

c1

n

+−λ α+−α−

Indeed, (1) follows from |f (n)| ≤ λ−α

α+−α− + α

(as α+ = α− for Λ− < λ < Λ+). Next, denote γ = λ−α−

√ 1

−

d(k−1)

α+−α− and observe that |f (n)|[d(k − 1)]

n

n 2

n 2

= γα+n + γα−n [d(k − 1)]

= 2 γ α+ d(k − 1)

.

n 2

n−→→∞ 0. Since α+ d(k − 1) = 1, this means that narg α+ n−→→∞ π2 − arg γ (modπ), hence α+ ∈ R, which is false. Even though f is not in ΩdL−21 (X) it induces a natural sequence of approximate eigenforms:

If (2) fails, then |f (n)|[d(k − 1)]

 

f (k) σ ∈ Sk (X,σ0) and k ≤ n −f (k) σ ∈ Sk (X,σ0) and k ≤ n 0 otherwise.

fn (σ) =



To see this, observe that (A0 − λ)f = 0, and that fn coincides with f on Bn (X,σ0) for k ≤ n and vanishes on Tdk d−1 \Bn (X,σ0). It follows that (A0 − λ)fn is supported on Sn (X,σ0) ∪ Sn+1 (X,σ0), and by |Sn (X,σ0)| = dnk (k − 1)n−1, the deﬁnition of A0, and (3.6)

= |Sn (X,σ0)| dk 1 [f (n − 1) − (d − 1)f (n)] − λf(n) 2 + |Sn+1 (X,σ0)| dk 1 f (n) 2 n j=0 |Sj (X,σ0)|f2(j)

(A0 − λ)fn 2 fn 2

dnk (k − 1)n−1 · −k−k1f (n + 1) 2 + dn+1k (k − 1)n dk 1 f (n) 2 f2 (0) + nj=1 djk (k − 1)j−1 f2 (j)

=

dnk−1 (k − 1)n+1f (n + 1)2 + dn−1k−1 (k − 1)nf (n)2 f2 (0) + nj=1 djk (k − 1)j−1 f2 (j) ≤

=

2c22

dk f2 (0) + k−k1 nj=1 [d(k − 1)]j f (j)2

.

0−λ)fn 2

By (3.7), the denominator becomes arbitrarily large as n grows, and therefore (A

fn 2 → 0

and λ ∈ SpecA0. Turning to the isolated eigenvalues in (3.4), one can easily check that f (n) = d1n is an eigenform with eigenvalue d1, and for 2 ≤ k ≤ d it is in L2. This concludes the ﬁrst part of the proof.

Next assume that λ ∈ −1, d1 \[Λ−,Λ+]. We show that in this case Lemma 3.4 can be applied. Let σ0 and X+d−1 be as before, including the layer structure. Deﬁne the following X+d−1-spherical forms:

α+n α+ − λ

α−n α− − λ

ψσλ

, ϕλσ

. (3.8)

(n) =

(n) =

0

0

The functions ψσλ

is deﬁned whenever λ = α+, which holds unless λ = d1 and k ≤ d + 1 (see (3.5)). Similarly, ϕλσ

0

is deﬁned unless λ = −1, or λ = d1 and k ≤ d + 1. It is straightforward to verify that

0

(A0 − λI)ψσλ

= (A0 − λI)ϕλσ

= σ

0

0

0

whenever the functions are deﬁned. For every X+d−1-spherical form f one has

∞

∞

k k − 1

[(k − 1)d]n f2 (n). (3.9)

f 2 =

|Sn (X,σ0)|f2 (n) = f2 (0) +

n=1

n=0

One can verify that 0 < d(k − 1)α+2 < 1 holds for all λ < Λ−, and thus by (3.8) and (3.9) ψσλ

is continuous w.r.t. λ in this region, so that it is bounded on every interval [a,b] ⊆ (−∞,Λ−). Furthermore, for any σ ∈ Xd−1 there is an isometry of Tkd which takes σ0 to σ, and thus ψσλ

is ﬁnite. In fact, ψσλ

0

0

, and which satisﬁes (A0 − λI)ψσλ = σ. We can now invoke Lemma 3.4 for [a,b] ⊆ (−∞,Λ−), using ψσλ

to a form ψσλ with the same L2-norm as ψσλ

0

0

and its translations by isometries, and obtain that (a,b)∩SpecA0 = ∅. Thus, SpecA0 does not intersect (−∞,Λ−).

0

Similarly, 0 < d(k − 1)α−2 < 1 holds for all λ > Λ+, so that the same argumentation for ϕλσ

0

shows that SpecA0 does not intersect (Λ+,∞), provided that d+1 < k. When k ≤ d+1 we know that d1 ∈ SpecA0, and we need to show that SpecA0 does not intersect (Λ+,∞)\ d 1 . This is done in the same manner, observing intervals [a,b] ⊆ Λ+, d1 and [a,b] ⊆ d 1,∞ separately.

| |
|---|


#### 3.4 Continuity of the spectral measure

In this section we generalize parts of Grigorchuk and Żuk’s work on graphs [GŻ99] to general simplicial complexes. We assume throughout the section that all d-complexes referred to are (d − 1)-connected, and that families and sequences of d-complexes we encounter have globally bounded (d − 1)-degrees.

For a uniform d-complex X we deﬁne the distance between two (d − 1)-cells to be the minimal length of a (d − 1)-chain connecting them:

dist(σ,σ ) = min n ∃σ0,σ1,...,σn = σ0 ∈ Xd−1 s.t. σi ∪ σi+1 ∈ Xd ∀i

.

We denote by Bn (X,σ) the ball of radius n around σ in X, which is the maximal subcomplex of X all of whose (d − 1)-cells are of distance at most n from σ†. A marked d-complex (X,σ) is

† this is similar to Bn (X, σ) deﬁned in the proof of theorem 3.3, but there Bn (X, σ) referred only to the (d − 1)cells, and here to the entire subcomplex

a d-complex with a choice of a (d − 1)-cell σ. On the space of marked d-complexes with ﬁnite

- (d − 1)-degrees one can deﬁne a metric by


1 n + 1

: Bn (X1,σ1) is isometric to Bn (X2,σ2) Remarks.

dist((X1,σ1),(X2,σ2)) = inf

- (1) A limit (X,σ) of a sequence (Xn,σn) in this space is unique up to isometry.
- (2) For every K ∈ N, the subspace of d-complexes with (d − 1)-degrees bounded by K is compact. This is due to the fact that there is only a ﬁnite number of possibilities for a ball of radius n, so that every sequence has a converging subsequence by a diagonal argument (see [GŻ99] for details).


Our next goal is to study the relation of this metric to the spectra of complexes. We use some standard spectral theoretical results which we summarize as follows: Let X be a countable set with a weighted counting measure w, i.e.,

X f = x∈X w (x)f (x), and A a self-adjoint operator on L2 (X,w). For every x ∈ X, the spectral measure µx is the unique regular Borel measure on C such that for every polynomial P (t) ∈ C[t]

´

P(A) x, x = ˆ

P(z)dµx(z),

C

where x is the Dirac function of the point x. For x,y ∈ X the spectral measure µx,y is the unique regular Borel measure on C such that for every polynomial P

P(A) x, y = ˆ

P(z)dµx,y(z).

C

The spectrum of A can be inferred from the spectral measures by SpecA =

suppµx. (3.10)

suppµx,y =

x,y∈X

x∈X

+

d on ΩdL−21 (with the inner product as in (2.2)), and this is justiﬁed by observing that for any choice of orientation X+d−1 of Xd−1, we have an isometry ΩLd−21 ∼= L2 X+d−1,w , where w (σ) = deg1 σ. For any σ ∈ Xd−1 we denote by µXσ the spectral measure of A w.r.t. σ. Similarly, µXσ,σ denotes the spectral measure of A w.r.t. σ and σ .

We wish to apply this mechanism to the analysis of the action of A = A(X,0) = I−∆

##### Lemma 3.5. If lim

(Xn,σn) = (X,σ) then µX

σnn converges weakly to µXσ .

n→∞

Proof. For regular ﬁnite Borel measures on R with compact support, weak convergence follows from convergence of the moments of the measures (see e.g. [Fel66, §VIII.1]). For m ≥ 0 the mth

moment of µXσ , denoted µXσ (m), is given by

zmdµXσ (z) = Am σ, σ = AmE0σ, σ =  Emσ , σ = Emσ (σ)

µXσ (m) = ˆ

,

deg σ

C

where Emσ is the 0-lazy expectation process starting at σ, at time m. However,

Emσ (σ) = pσm (σ) − pσm (σ) is determined by the structure of the complex in the ball Bm (X,σ). For large enough n, Bm (X,σ) is isometric to Bm (Xn,σn), which implies that µX

(m) = µXσ (m).

| |
|---|


σnn

#### 3.5 Alon-Boppana type theorems

Deﬁnition 3.6. A sequence of d-complexes Xn, whose (d − 1)-degrees are bounded globally, is said to converge to the complex X (written Xn n−→→∞ X) if (Xn,σn) converges to (X,σ) for some choice of σn ∈ Xnd−1 and σ ∈ Xd−1.

In particular, if X is an inﬁnite d-complex with bounded (d − 1)-degrees, and {Xn} is a sequence of quotients of X whose injectivity radii approach inﬁnity, then Xn n−→→∞ X.

The following is (one form of) the classic Alon-Boppana theorem:

- Theorem 3.7 (Alon-Boppana). Let Gn be a sequence of graphs whose degrees are globally bounded, and G a graph s.t. Gn n−→→∞ G. Then

liminf

n→∞

λ(Gn) ≤ λ(G).

In the literature one encounters many variations on this formulation: some refer only to quotients of G, some only to regular graphs, and some are quantitative (e.g. [Nil91]).

In this section we study the analogue question for complexes of general dimension. We start with the following:

- Theorem 3.8. If Xn n−→→∞ X and λ ∈ SpecA(X,0), there exist λn ∈ SpecA(Xn,0) with


λn = λ. The same holds for the corresponding Laplacians ∆+X and ∆+X

.

lim

n

n→∞

Proof. Let σn,σ be as in Deﬁnition 3.6. Since λ ∈ SpecA(X,0), for every ε > 0 there exists σ ∈ Xd−1 such that µXσ ((λ − ε,λ + ε)) > 0. We denote r = dist(σ,σ ), and restrict our attention to the tail of {(Xn,σn)} in which Br (Xn,σn) is isometric to Br (X,σ). If σ n is the image of σ under such an isometry, and dn = max{k |Bk (Xn,σn) ∼= Bk (X,σ)}, then Bd

n−r (Xn,σ n) ∼= Bd

n−r (X,σ ), and since dn − r → ∞ we have (Xn,σ n) → (X,σ ). By Lemma 3.5, µX

σ n ((λ − ε,λ + ε)) > 0 for large enough n and therefore SpecA(Xn,0) intersects

n

(λ − ε,λ + ε). The result for the Laplacians follows from the fact that ∆+ = I − d · A. In particular this gives: Corollary 3.9. If Xn n−→→∞ X then SpecAX ⊆ n SpecAX

| |
|---|


.

n

This is an analogue of [Li04, Thm. 4.3], which is also regarded sometimes as an Alon-Boppana theorem. In [Li04] the same statement is proved for the Hecke operators acting on X = Bn,F, the Bruhat-Tits building of type An, and on a sequence of quotients of X whose injectivity radii approach inﬁnity.

Returning to the formulation of Alon-Boppana with spectral gaps, Theorem 3.8 yields as an immediate result that if Xn n−→→∞ X then

≤ minSpec∆+X ≤ λ(X). (3.11) In order to obtain the higher dimensional analogue of the Alon-Boppana theorem one would like to verify that this holds also when the spectrum of ∆+X

minSpec∆+X

liminf

n

n→∞

is restricted to Zd−1 = Bd−1 ⊥. But while this holds for graphs, the situation is more involved in general dimension. First of all, it does not hold in general:

n

- Theorem 3.10. Let T22 be the arboreal 2-regular triangle complex (Figure 3.1), and Xr =

Br T22,e0 be the ball of radius r around an edge in it (as in Figure 3.2). Then lim

r→∞

λ(Xr) =

3 2 −

√2, while λ T22 = 0.

The proof follows in the next section. Before we delve into this counterexample, let us exhibit ﬁrst several cases in which the Alon-Boppana analogue does hold:

- Theorem 3.11. If Xn n−→→∞ X, and one of the following holds:


- (1) Zero is not in Spec∆+X Z

d−1

(i.e. λ(X) = 0),

- (2) zero is a non-isolated point in Spec∆+X Z

d−1

, or

- (3) the (d − 1)-skeletons of the complexes Xn form a family of (d − 1)-expanders,


then

λ(Xn) ≤ λ(X).

liminf

n→∞

Proof. By Theorem 3.8 there exist λn ∈ Spec∆+X

with λn → λ(X). If (1) holds, then λn > 0 for large enough n, which implies that λn ∈ Spec∆+X

n

n Zd−1, hence λ(Xn) = minSpec∆+X

n Zd−1 ≤ λn. Thus, liminfn→∞ λ(Xn) ≤ liminfn→∞ λn = λ(X). If (2) holds then there are µn ∈ Spec∆+X\{0} with µn → λ(X). For every µn there is a sequence λn,m ∈ Spec∆+X

m Zd−1 with λn,m m−→→∞ µn, and λn,n → λ(X).

In (3) we mean that the (d − 2)-cells in Xn have globally bounded degrees, and the (d − 2)dimensional spectral gaps

λd−2 (Xn) = minSpec∆+d−2 Z

d−2(Xn)

are bounded away from zero (see Remark (1) after the proof). For example, if Xn are triangle complexes, this means that their underlying graphs form a family of expander graphs in the classical sense. By the previous cases, we can assume that λ(X) = 0, and furthermore that zero

is an isolated point in Spec∆+X Z

. This implies that it is an eigenvalue, so that there exists 0 = f ∈ Zd−1 (X) = Bd−1 (X)⊥ with ∆+Xf = 0. Since Xn n−→→∞ X there exist σn ∈ Xn, σ∞ ∈ X, a sequence r (n) → ∞, and isometries ψn : Br(n) (Xn,σn) −→∼= Br(n) (X,σ∞). Deﬁne fn ∈ ΩdL−21 (Xn) by

d−1

fn (τ) =

f (ψn (τ)) dist(τ,σn) ≤ r (n) 0 r (n) < dist(τ,σn).

We ﬁrst claim that ∆+fn and ∆−fn converge to zero (∆− = ∆− (Xn) are deﬁned since the

- (d − 2)-degrees are bounded). Since fn is zero outside Br(n) (Xn,σn) and coincide with f on it, by ∆+f = 0 we have


∆+fn 2 =

∆+fn (σ) 2 =

∆+fn (σ) 2

σ∈Xnd−1

σ:r(n)≤dist(σ,σn)≤r(n)+1

2

fn (σ ) deg σ

fn (σ) −

###### .

=

σ ∼σ

σ:r(n)≤dist(σ,σn)≤r(n)+1

Using ki=1 ai

2

≤ k ki=1 a2i this gives

∆+fn 2 ≤ (dK + 1)

σ:r(n)≤dist(σ,σn)≤r(n)+1

|fn (σ )|2 ,

|fn (σ)|2 +

σ ∼σ

where K is a bound on the degree of (d − 1)-cells in X and Xn. Since every (d − 1)-cell has at most dK neighbors, we have

∆+fn 2 ≤ dK (dK + 1)

|fn (σ)|2

σ:r(n)−1≤dist(σ,σn)≤r(n)+2

2 n→∞

−→ 0.

≤ dK (dK + 1) f X\B

X(σ,r(n)−2)

The reasoning for ∆−fn → 0 (see (2.5)) is analogous: (3.3) gives ∆−f = 0, and the assumptions that (d − 2)-degrees are globally bounded yields similar bounds as done for ∆+.

For every n write fn = zn + bn, with zn ∈ Zd−1 (Xn) and bn ∈ Bd−1 (Xn). It is enough to show that zn are bounded away from zero, since then ∆

+zn zn = ∆

+fn zn → 0, showing that

d−1(Xn) converge to zero. Assume therefore that there are arbitrarily small zn , and by passing to a subsequence that zn → 0. Then bn → f > 0, giving ∆

λ(Xn) = minSpec ∆+ Z

−fn bn → 0. This implies that λ n =

−bn bn = ∆

d−1(Xn) converge to zero. However,

minSpec ∆− B

λ n = minSpec ∆− B

d−1(Xn) = minSpec ∂d∗−1∂d−1 B

d−1(Xn)

= minSpec ∂d−1∂d∗−1 B

d−2(Xn) = minSpec ∆+d−2 B

d−2(Xn) ≥ minSpec ∆+d−2 Z

d−2(Xn) = λd−2 (Xn)

where is due to the fact that Bd−1 and Bd−1 are the orthogonal complements of ker∂d−1 and ker∂d∗−1 respectively. This is a contradiction, since λd−2 (Xn) are bounded away from zero. Remarks.

| |
|---|


- (1) If X(j) denote the j-skeleton of a complex X, i.e. the subcomplex consisting of all cells

of dimension ≤ j, then one can look at λ Xn(d−1) instead of at λd−2 (Xn). Since we have diﬀerent weight functions in codimension one, these are not equal. However, since we assumed that all (d − 1) and (d − 2) degrees are globally bounded (and nonzero), the norms induced by these choices of weight functions are equivalent, and thus λ Xn(d−1) are bounded away from zero iﬀ λd−2 (Xn) are.

- (2) The Alon-Boppana theorem for graphs follows from condition (2) in this Proposition (as done in [GŻ99]), since zero is never an isolated point in the spectrum of the Laplacian of an inﬁnite connected graph. Otherwise, it would correspond to an eigenfunction, which is some multiple of the degree function, hence not in L2.


#### 3.6 Analysis of balls in T22

In this section we analyze the spectrum of balls in the 2-regular triangle complex T22, proving in particular that they constitute a counterexample for the higher-dimensional analogue of Alon-

Boppana (Theorem 3.10). We denote here Xr = Br T22,e0 the ball of radius r around an edge , X3 =

- e0 in T22: X0 is a single edge, X1 = , X2 =


, and so on. For r ≥ 1 we deﬁne

| |
|---|
| |


| |
|---|
| |


three r × r matrices denoted M++(r),M+(r−),M−−(r) , and for r ≥ 0 a (r + 1) × (r + 1) matrix M−(r+), as follows:

M−(0)+ = 1 , M++(1) = M+(1)− = M−−(1) = 0 M−(1)+ = − 11 −22 , M++(2) = M+(2)− =

- 1

- 2 −1


−1 2 , M−−(2) =

3 2 −1

−1 2

 

  

  

- 1

- 2 −1


− 12 23 −1

M++(r) = M+(r−) =

...

r



− 12 32 −1 −1 2

 

  

  

3 2 −1

− 12 23 −1

M−−(r) =

...

r



− 12 32 −1 −1 2

 

  

  

1 −2 − 21 23 −1

...

M−(r+) =

r + 1



− 12 32 −1 −1 2

- Theorem 3.12. The spectrum of Xr = Br T22 is given (including multiplicities) by


r−1

Spec∆+ (Xr) = SpecM++(r) ∪ SpecM+(r−) ∪ SpecM−−(r) ∪ SpecM−(r+) ∪

j=1

SpecM++(j)

2r−j+1

where [X]i means that X is repeated i times.

To make this clear, this gives

Spec∆+ (Xr) = 4r + 1 +

as ought to be.

r−1

2r−j+1 · j = 2r+2 − 3 = Xr1 = dimΩ1 (Xr),

j=1

Proof. The symmetry group of Xr (for r ≥ 1) is G = {id,τh,τv,σ}, where τh is the horizontal reﬂection, τv is the vertical reﬂection (around the middle edge e0), and σ = τh ◦ τv = τv ◦ τh is a rotation by π. The irreducible representations of G are given in Table 3.1.

We deﬁne four orientations for Xr, denoted Xr±±, demonstrated in Figure 3.3. In all of them e0 is oriented from left to right, and the ﬁrst (top right) quadrant is oriented clockwise. Each of the

other quadrants is then oriented according to the corresponding representation, e.g. Xr+− satisﬁes

| |e<br><br>|τh|τv|σ|
|---|---|---|---|---|


|V++|1<br><br>|1|1<br><br>|1|
|---|---|---|---|---|
|V+−<br><br>|1|1|−1<br><br>|−1|
|V−+|1<br><br>|−1<br><br>|1|−1|
|V−−|1<br><br>|−1<br><br>|−1<br><br>|1|


Table 3.1: The irreducible representations of G = Sym(Xr).

| |
|---|
| |


| |
|---|
| |


| |
|---|
| |


| |
|---|
| |


X3−− Figure 3.3: The four choices of orientations for Xr, depicted for r = 3.

X3+−

X3−+

X3++

the following: for every oriented edge e, if e ∈ Xr+− then τhe ∈ Xr+−, while τve,σe ∈/ Xr+− (so that τve,σe ∈ Xr+−).

The space of 1-forms Ω1 (Xr) is naturally a representation of G = Sym(Xr), by (γf)(e) =

- f γ−1e (where γ ∈ G, f ∈ Ω1 (Xr), e ∈ Xr1). We denote by Ω(±±r) = Ω1±± (Xr) its V±±-isotypic


components. For example, f ∈ Ω(+r−) if and only if it satisﬁes τhf = f and τvf = −f (which implies that σf = τvτhf = −f).

We say that a 1-form on Xr is ++-spherical, denoted f ∈ S++(r) , if it is

- (1) spherical in absolute value (i.e. |f (e)| = |f (e )| whenever dist(e0,e) = dist(e0,e )), and
- (2) V++-isotypic (namely f ∈ Ω(++r) , or equivalently, f is of constant sign on Xr++).


The deﬁnition of S+(r−) ,S−(r+) ,S−−(r) are analogue.

Let e1,...,er be edges in the ﬁrst quadrant of Xr oriented as in Xr±±, and with dist(ei,e0) = i. Let f be an eigenform of ∆+ with eigenvalue λ, which is in one of the S±±(r) . Then for 2 ≤ i ≤ r−1

- 1

- 2


λf (ei) = ∆+f (ei) = f (ei) −

[f (ei−1) − f (ei) + 2f (ei+1)] and

λf (er) = ∆+f (er) = f (er) − [f (er−1) − f (er)]. The behavior of f around e0,e1 depends on the isotypic component. We assume r ≥ 2, and leave it to the reader to verify the cases r = 0,1. Every form in Ω(++r) ,Ω(+r−) ,Ω(−−r) must vanish on the middle edge e0: for the ﬁrst two, since

f (e0) = (τhf)(e0) = f (τhe0) = f (e0) = −f (e0),

and for the last one since f (e0) = (−τvf)(e0) = −f (τve0) = −f (e0). For a spherical (−+)functions we have

- 1

- 2


λf (e0) = ∆+f (e0) = f (e0) −

[4 · f (e1)],

and at e1 we have (using the fact that f (e0) = 0 for f ∈ Ω(++r) ,Ω(+r−) ,Ω(−−r) )

 

f (e1) − 21 [f (e1) + 2f (e2)] f ∈ Ω(++r) ,Ω(+r−) f (e1) − 21 [f (e0) − f (e1) + 2f (e2)] f ∈ Ω(−r+) f (e1) − 21 [−f (e1) + 2f (e2)] f ∈ Ω(−−r) .

λf (e1) = ∆+f (e1) =



The matrices M±±(r) represent these equations, and thus the ++-spherical spectrum of Xr is Spec∆+ S(r)

= SpecM++(r), and likewise for the other S±±(r) .

++

Until now we have only accounted for the spherical part of Ω1 (X), ﬁnding in total 4r + 1 eigenvalues. The other eigenvalues are obtained by using spherical eigenforms of Xi with i < r.

Denote by Xrh the upper half of Xr, including e0, which is a fundamental domain for {id,τv}. Observe that Xr\

◦

X1 (by which we mean Xr after deleting e0 and the two triangles adjacent to it, but not the other four edges), is comprised of four copies of Xrh−1, which intersect only in vertices. Denote these four copies of Xrh−1 by Y1,...,Y4. Let f ∈ S++(r−1) be a (++)-spherical λ-eigenform on Xr−1, and deﬁne g ∈ Ω1 (Xr) by g Y

= 0. We

###### and g Y

###### = g Y

###### = g Y

###### = f Xh

4

3

2

1

r−1

show now that g is a λ-eigenform of Xr. Since f ∈ Ω++(r−1), g (e1) = f (e0) = 0, where e1 is the edge incident to e0 in Y1. Therefore, ∆+g = λg holds everywhere outside Y1. It also holds at e1, since if e2,e 2 are the two edges incident to e1 in Y1, then g (e2) = −g (e 2) since f is symmetric with respect to τh. Obviously, ∆+g = λg holds in Y1\{e1}, and we are done. We could have taken g Y

for any i ∈ {1,2,3,4}, and the resulting eigenforms are independent. We

###### = f Xh

i

r−1

remark that taking f ∈ Ω(+r−−1) would also work, but would give again the same eigenforms, while f ∈ Ω−(r+) ,Ω(−−r) would not deﬁne an eigenform on Xr.

◦

Xj is comprised of 2j+1 copies of Xrh−j, and in a similar way every eigenform of ∆+ S(r−j)

More generally, Xr\

contributes 2j+1 eigenforms to Xr. We recall that for f ∈ S++(r−j) we always have f (e0) = 0, and observe that due to the recursion relations if f = 0 then f (e1) = 0. Therefore, the eigenforms obtained from copies of Xrh−j for various j are all linearly independent, as they are supported outside diﬀerent balls in Xr. Together with the 4r + 1 spherical eigenforms, this accounts for

++

4r + 1 +

r

2j+1 · Spec∆+ S(r−j)

++

j=1

= 4r + 1 +

r−1

2j+1 (r − j) = 2r+2 − 3

j=1

independent eigenforms, and since this is the dimension of Ω1 (Xr) we are done.

√2 < λ.

- Proposition 3.13. For every r ∈ N and λ ∈ SpecM±±(r) , either λ = 0 or 32 −


| |
|---|


Proof. Let p++[r] (λ) = det M++(r) − λI , and similarly for the other ±±. Expanding M−−(r) − λI

by minor gives

7 2

27 4

p[1]−− (λ) = 1 − λ, p[2]−− (λ) = λ2 −

λ + 2, p[3]−− = −λ3 + 5λ2 −

λ + 2

3 2 − λ p[−−r−1] (λ) −

- 1

- 2


p−−[r−2] (λ) (r ≥ 4).

p[−−r] (λ) =

This yields a quadratic recurrence formula in Q[λ] whose solution (for r ≥ 2) is p[−−r] (λ) = α (λ)µ+ (λ)r + β (λ)µ− (λ)r, where

- (2λ − 2)√4λ2 − 12λ + 1 + 4λ2 − 10λ − 2

- (2λ − 3)√4λ2 − 12λ + 1 + 4λ2 − 12λ + 1


α (λ) = 2 − β (λ) =

,

- 3

- 4 −


λ 2 ±

1 4

4λ2 − 12λ + 1.

µ± (λ) =

√2 one can verify that β (λ) < 0 < α(λ) and 0 < µ− (λ) < µ+ (λ), and for r ≥ 2

For 0 < λ < 23 −

r

2

µ− (λ) µ+ (λ)

µ− (λ) µ+ (λ)

p[−−r] (λ) = µ+ (λ)r α (λ) + β (λ)

≥ µ+ (λ)r α (λ) + β (λ)

= µ+ (λ)r−2 α (λ)µ+ (λ)2 + β (λ)µ− (λ)2 = µ+ (λ)r−2 p[2]−− (λ) > 0.

Using the solution for p[−−r] one can write p[+r−] , for r ≥ 4, as

- 1

- 2


- 1

- 2 − λ p[−−r−1] (λ) −


p−−[r−2] (λ)

p[+r−] (λ) =

- 1

- 2 − λ µ+ (λ) −


- 1

- 2


- 1

- 2 − λ µ− (λ) −


- 1

- 2


µ+ (λ)r−2 + β (λ)

µ− (λ)r−2

= α (λ)

√2, and it follows that p+[r−] (λ) does not vanish in this interval. This takes care of p[++r] (λ) as well, since M++[r] = M+[r−] . The considerations for p[−r]+ (λ) are similar, and we leave them to the reader.

Now α (λ) 2 1 − λ µ+ (λ) − 12 < 0 < β (λ) 12 − λ µ− (λ) − 21 for 0 < λ < 23 −

| |
|---|


We can conclude now that {Xr}r∈N constitute a counterexample for high-dimensional AlonBoppana:

Proof of Theorem 3.10. By the results in this section, the spectrum of ∆+X

is contained in {0}∪

r

3

- 2 −

√2,3 . Since Xr is contractible, its ﬁrst homology is trivial and thus the zeros in the spectrum all belong to coboundaries, i.e., Spec∆+X

r Z1 ⊆ 32 −

√2,3 . Therefore, liminf

r→∞

λ(Xr) ≥

- 3


√2 ∈ SpecT22 (by Theorem 3.3), together with Theorem 3.8, which asserts that there exist λr ∈ Spec∆+X

√2. In fact, liminf

√2. This follows from 23 −

λ(Xr) = 32 −

2 −

r→∞

√2. As λr can be assumed to be nonzero, they are in fact in Spec∆+X

such that λr → 32 −

r

r Z1, so that liminf

λ(Xr) ≤ lim r→∞

r→∞

√2. Finally, by Lemma 3.1 and Theorem 3.3 we have λ T22 = 0.

λr = 23 −

| |
|---|


- 3.7 Spectral radius and random walk 3 INFINITE COMPLEXES


#### 3.7 Spectral radius and random walk

The spectral radius of an operator T is ρ(T) = max{|λ||λ ∈ SpecT}. If T is a self-adjoint operator on a Hilbert space then ρ(T) = T . In this section we observe the transition operator A = A(X,p) acting on ΩdL−21, and relate it to the asymptotic behavior of the expectation process on X. Under additional conditions, this can be translated to a result on the spectral gap of the complex.

- Proposition 3.14. Let Enσ be the expectation process associated with the p-lazy (d − 1)-walk on a ﬁnite or countable d-complex X with bounded (d − 1)-degrees.


- (1) For all values of p sup

σ∈X±d−1

limsup

n→∞

n |Enσ (σ)| = A = ρ(A).

- (2) If 21 ≤ p ≤ 1 then

sup

σ∈X±d−1

limsup

n→∞

n Enσ (σ) = A = maxSpecA =

p(d − 1) + 1 d −

1 − p d · minSpec∆+.

- (3) If 12 ≤ p ≤ 1 and all (d − 2)-cells in X are of inﬁnite degree, then


p(d − 1) + 1 d −

1 − p d · λ(X).

n Enσ (σ) =

sup

limsup

n→∞

σ∈X±d−1

Proof. For an oriented (d − 1)-cell σ,

Enσ (σ) = AnE0σ (σ) = deg σ An σ, σ = deg σ ˆ

C

zndµσ (z) = deg σ ˆ

Spec A

where µσ is the spectral measure of A with respect to σ. It follows that

zndµσ (z),

n |Enσ (σ)| = limsup

limsup

n→∞

n→∞

deg σ ˆ

zndµσ (z) = max{|λ||λ ∈ suppµσ},

n

supp µσ

and by Spec(A) =

supp(µσ) (see (3.10))

σ∈X±d−1

n |Enσ (σ)| = sup

max{|λ||λ ∈ suppµσ} = ρ(A),

sup

limsup

n→∞

σ∈X±d−1

σ∈X±d−1

settling (1). Since Spec(A) ⊆ 2p − 1, p(d−d1)+1 , in the case p ≥ 12 the spectrum of A is nonnegative. Therefore,

Enσ (σ) = AnE0σ (σ) = deg σ An σ, σ ≥ 0

so that |Enσ (σ)| = Enσ (σ), and in addition ρ(A) = maxSpecA. This accounts for (2), and combining this with Lemma 3.1 gives (3).

| |
|---|


This proposition is a generalization of the classic connection between return probability and spectral radius in an inﬁnite connected graph. Namely, for any vertex v the non-lazy walk on this graph satisﬁes

n pvn (v) = 1 − λ(G) = maxSpecA = A = ρ(A),

lim

n→∞

where A is the transition operator of the walk. There are slight diﬀerences, though: in general dimension p ≥ 21 is needed for some of these equalities, and in addition one must take the supremum over all possible starting points for the process. For graphs this is not necessary (provided the graph is connected), and we do not know whether the same is true in general dimension. One case in which this is not necessary is when the complex is (d − 1)-transitive, in the sense that its symmetry group acts transitively on Xd−1. This (together with Theorem 3.3) leads to the following corollary:

- Corollary 3.15. For the k-regular arboreal d-complex Tkd, the non-lazy random walk starting at any (d − 1)-cell σ satisﬁes

limsup

n→∞

n |pσn (σ) − pσn (σ)| =

d − 1 + 2 d(k − 1) kd

.

For p ≥ 12, the p-lazy walk satisﬁes

limsup

n→∞

n pσn (σ) − pσn (σ) =

p + 1−dp 2 ≤ k ≤ d + 1 p + (1 − p) 1−d+2

√

d(k−1)

kd d + 1 ≤ k

.

Another corollary of Proposition 3.14 is the following:

- Corollary 3.16. If dimX = d and there exists some τ ∈ Xd−2 of ﬁnite degree (in particular, if X is ﬁnite), then the p ≥ 12 lazy random walk satisﬁes


1 − p d

n pσn (σ) − pσn (σ) = p +

limsup

.

sup

n→∞

σ∈X±d−1

Proof. The form δd−1 τ is in ΩdL−21 and in kerδd, so that 0 ∈ Spec∆+.

| |
|---|


- 3.8 Amenability, transience and recurrence An inﬁnite connected graph with ﬁnite degrees is said to be amenable if its Cheeger constant


|E (A,V \A)| |A|

h(X) = min

A⊆V 0<|A|<∞

is zero. It is called recurrent if with probability one the random walk on it returns to its starting point, and transient otherwise. A nonamenable graph is always transient.

All three notions have many equivalent characterizations. Among these are the following, which relate to the Laplacian of the graph:

- (1) If X has bounded degrees, then it is amenable if and only if λ(X) = minSpec∆+ = 0. This follows from the so-called discrete Cheeger inequalities due to Tanner, Dodziuk, and Alon-Milman [Dod84, Tan84, AM85, Alo86].


- (2) X is transient if and only if Ev number of

visits to v = ∞n=0 pvn (v) < ∞ for some v, or equivalently for all v.

- (3) X is transient if and only if there exists f ∈ Ω1L2 (X) such that ∂f = v for some v, or equivalently for all v [Lyo83].


This suggests observing the following generalizations of these notions for a simplicial complex of dimension d:

(A) λ(X) = 0. (A ) minSpec∆+ = 0. (T) ∞n=0 Enσ (σ) < ∞ for every σ ∈ Xd−1, where E is the normalized expectation process

of laziness p on X, for some 21 ≤ p < 1 (see Proposition 3.17(5)). (T ) For every σ ∈ Xd−1 there exists f ∈ ΩdL2 (X) such that ∂df = σ.

For inﬁnite graphs, (A) and (A ) are the same and are equivalent to amenability, and (T) (for any p) and (T ) are equivalent to transience. These deﬁnitions suggests many questions, some of which are presented in the next section. The next proposition points out some observations regarding them. Let us also deﬁne the property:

(S) All (d − 2)-cells in X have inﬁnite degrees, which holds in any inﬁnite graph. Proposition 3.17. Let X be a complex of dimension d with bounded (d − 1)-degrees. Then

- (1) (A) ⇒ (A ).
- (2) (A ) + (S) ⇒ (A).
- (3) ¬(A ) ⇒ (T ) ⇒ (S).
- (4) ¬(A ) ⇒ (T).
- (5) If (T) holds for some 12 ≤ p < 1, then it holds for every such p.

- (6) If zero is an isolated point in Spec∆+ then ¬(T).


Proof. (1) is trivial and (2) follows from Lemma 3.1.

- (3) If (A ) fails then 0 ∈/ Spec∆+, which means that ∆+ is invertible on ΩLd−21 (X). Thus, for


every σ ∈ Xd−1 there exists ψ ∈ ΩdL−21 s.t. ∆+ψ = σ, and taking f = δdψ gives (T ). If (S) fails, then some τ ∈ Xd−2 has ﬁnite degree. In this case for any f ∈ Ωd one has

(∂d−1∂df)(τ) =

(∂df)(vτ) =

f (wvτ) = 0,

v τ

v τ w vτ

since this sums over every d-cell containing τ exactly twice, with opposite orientations. If σ is any (d − 1)-cell containing τ, then ∂df = σ would give 0 = (∂d−1∂df)(τ) = (∂d−1 σ)(τ) = 1, so that (T ) fails.

4 OPEN QUESTIONS

- (4) If minSpec∆+ > 0 then by Proposition 3.14(2)

sup

σ∈X±d−1

limsup

n→∞

n Enσ (σ) = 1 −

1 − p p(d − 1) + 1 · minSpec∆+ < 1

which gives ∞n=0 Enσ (σ) < ∞ for every σ.

- (5) Let 21 ≤ p, and denote by Enp,σ


∞ n=0

the p-lazy normalized expectation process starting from

σ and Ap = p(d−d1)+1 · Ap. Recall that Enp,σ = Anp E0p,σ = Anp σ, and let µp = µ Aσp be the spectral measure of Ap w.r.t. σ. Then

∞

Enp,σ (σ) =

n=0

∞

∞

Anp σ (σ) = deg σ

n=0

n=0

∞

Anp σ, σ = deg σ

n=0

ˆ

λndµp (λ).

Spec Ap

Since Spec Ap ⊆ p d((2d−p1)+1−1) ,1 ⊆ [0,1], by monotone convergence

∞

∞

dµp (λ) 1 − λ

ˆ

λndµp (λ) = deg σ ˆ

Enp,σ (σ) = deg σ

(3.12)

Spec Ap

Spec Ap

n=0

n=0

which is to be understood as ∞ if µp has an atom at λ = 1. Given p < q < 1 one has Aq = π Ap + (1 − π)I, where π = π (p,q,d) = 11−−pq · pq((dd−−1)+11)+1 ∈ (0,1). The spectral measure of Aq w.r.t. σ is thus given by µq = µ Aσq = µ Aσp ◦ g−1 where g (λ) = πλ + 1 − π, so that

∞

∞

dµq (λ) 1 − λ

dµp (λ) 1 − (πλ + 1 − π)

1 π

Enq,σ (σ) = deg σ ˆ

= deg σ ˆ

Enp,σ (σ)

=

Spec( Aq)

Spec Ap

n=0

n=0

which completes the proof. Finally, (6) follows from (3.12) as an isolated point in the spectrum implies an atom at 1.

| |
|---|


### 4 Open Questions

- (1) In an inﬁnite connected graph, the limit of

n

pvn (v) (which describes the spectral radius of the transition operator, see §3.7) is independent of the starting point v. Is the same true in higher dimension? Namely, is limsupn→∞

n

Enσ (σ) independent of σ for a (d − 1)connected complex?

- (2) If X Y is a covering map of graphs, then λ(X) ≥ λ(Y ) (see e.g. [Kes59, Lemma 3.1], but beware - Kesten uses λ(X) for what we denote by 1 − λ(X)). Does the same holds in higher dimension? If π : X Y is a covering map of d-complexes, then the same argumentation as in graphs shows that for any σ ∈ Xd−1 and σ = π ( σ) ∈ Y d−1 one has p σn ( σ) ≤ pσn (σ) and also p σn σ ≤ pσn (σ). This, however, does not suﬃce to show that


En σ ( σ) ≤ Enσ (σ). Showing that this hold (or even that it holds after taking nth-roots and letting n → ∞) would give the desired result.

- (3) It is not hard to see that a (d + 1)-partite d-complex is disorientable, but for d ≥ 2 one can also construct examples of disorientable complexes which are not (d + 1)-partite. It seems reasonable to conjecture that for simply connected complexes these properties coincide. Is this indeed the case?
- (4) The suggestions for higher-dimensional analogues of amenability and transience raise several questions:

- (a) Can high amenability and transience be characterized in non-spectral terms (i.e. combinatorial expansion, or some 1 − 0 event in the (d − 1)-walk model)?
- (b) Are the transience properties (T) and (T ) equivalent under some conditions?
- (c) Are all d-complexes with degrees bounded by d + 1 d-amenable?

(5) In classical settings, the Brownian motion on a Riemannian manifold constitute a continuous limit of the discrete random walk. Can one deﬁne a continuous process, say, on the

- (d − 1)-sphere bundle of a Riemannian manifold, which relates to its (d − 1)-homology and to the spectrum of the Laplace-Beltrami operator on (d − 1)-forms?


- (6) There are surprising and useful connections between random walks on graphs and electrical networks (see e.g. [DS84, LP05]). Can a parallel theory be devised for the random (d − 1)walk on d-complexes?


### References

[Alo86] N. Alon, Eigenvalues and expanders, Combinatorica 6 (1986), no. 2, 83–96. [AM85] N. Alon and V.D. Milman, λ1, isoperimetric inequalities for graphs, and superconcen-

trators, Journal of Combinatorial Theory, Series B 38 (1985), no. 1, 73–88. [CSŻ03] D.I. Cartwright, P. Solé, and A. Żuk, Ramanujan geometries of type A˜n, Discrete mathematics 269 (2003), no. 1, 35–43. [DK10] D. Dotterrer and M. Kahle, Coboundary expanders, arXiv preprint arXiv:1012.5316

(2010). [Dod84] J. Dodziuk, Diﬀerence equations, isoperimetric inequality and transience of certain random walks, Trans. Amer. Math. Soc 284 (1984). [DS84] P.G. Doyle and J.L. Snell, Random walks and electric networks, no. 22, Mathematical Association of America, 1984. [Eck44] B. Eckmann, Harmonische funktionen und randwertaufgaben in einem komplex, Com-

mentarii Mathematici Helvetici 17 (1944), no. 1, 240–255. [Fel66] W. Feller, An introduction to probability theory, vol. ii, 1966. [FGL+10] J. Fox, M. Gromov, V. Laﬀorgue, A. Naor, and J. Pach, Overlap properties of geo-

metric expanders, arXiv preprint arXiv:1005.1392 (2010). [Gar73] H. Garland, p-adic curvature and the cohomology of discrete subgroups of p-adic groups, The Annals of Mathematics 97 (1973), no. 3, 375–423.

[Gro10] M. Gromov, Singularities, expanders and topology of maps. part 2: From combinatorics to topology via algebraic isoperimetry, Geometric and Functional Analysis 20

(2010), no. 2, 416–526. [GW12] A. Gundert and U. Wagner, On laplacians of random complexes, Proceedings of the 2012 symposuim on Computational Geometry, ACM, 2012, pp. 151–160.

[GŻ99] R.I. Grigorchuk and A. Żuk, On the asymptotic spectrum of random walks on inﬁnite families of graphs, Random walks and discrete potential theory (Cortona, 1997), Sympos. Math 39 (1999), 188–204.

[Kes59] H. Kesten, Symmetric random walks on groups, Trans. Amer. Math. Soc. 92 (1959), 336–354. MR 0109367 (22 #253)

[Li04] W.C.W. Li, Ramanujan hypergraphs, Geometric and Functional Analysis 14 (2004), no. 2, 380–399.

[LM06] N. Linial and R. Meshulam, Homological connectivity of random 2-complexes, Com-

binatorica 26 (2006), no. 4, 475–487. [LP05] R. Lyons and Y. Peres, Probability on trees and networks, 2005. [LSV05] A. Lubotzky, B. Samuels, and U. Vishne, Ramanujan complexes of type A˜d, Israel

Journal of Mathematics 149 (2005), no. 1, 267–299. [Lub13] A. Lubotzky, Ramanujan complexes and high dimensional expanders, arXiv preprint arXiv:1301.1028 (2013). [Lyo83] T. Lyons, A simple criterion for transience of a reversible Markov chain, The Annals of Probability (1983), 393–402. [MW09] R. Meshulam and N. Wallach, Homological connectivity of random k-dimensional complexes, Random Structures & Algorithms 34 (2009), no. 3, 408–417. [MW11] J. Matoušek and U. Wagner, On Gromov’s method of selecting heavily covered points, Arxiv preprint arXiv:1102.3515 (2011). [Nil91] A. Nilli, On the second eigenvalue of a graph, Discrete Mathematics 91 (1991), no. 2, 207–210. [PRT12] O. Parzanchevski, R. Rosenthal, and R.J. Tessler, Isoperimetric inequalities in simplicial complexes, arXiv preprint arXiv:1207.0638 (2012). [SKM12] J. Steenbergen, C. Klivans, and S. Mukherjee, A Cheeger-type inequality on simplicial complexes, arXiv preprint arXiv:1209.5091 (2012). [Tan84] R.M. Tanner, Explicit concentrators from generalized n-gons, SIAM Journal on Algebraic and Discrete Methods 5 (1984), 287.

