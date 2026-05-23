---
type: source
kind: paper
title: The large $N$ factorization does not hold for arbitrary multi-trace observables in random tensors
authors: Razvan Gurau, Felix Joos, Benjamin Sudakov
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2506.15362v1
source_local: ../raw/2025-gurau-large-factorization-does-not.pdf
topic: general-knowledge
cites:
---

arXiv:2506.15362v1[math-ph]18Jun2025

# The large N factorization does not hold for arbitrary multi-trace observables in random tensors

Razvan Gurau1, Felix Joos2, and Benjamin Sudakov3 1Heidelberg University, Institut fu¨r Theoretische Physik, Philosophenweg 19, 69120 Heidelberg, Germany. email: gurau@thphys.uni-heidelberg.de 2Heidelberg University, Institut fu¨r Informatik, INF 205, 69120 Heidelberg, Germany. email: joos@uni-heidelberg.de 3Department of Mathematics, ETH, Zu¨rich, Switzerland. email: benjamin.sudakov@math.ethz.ch

Abstract

We consider real tensors of order D, that is D-dimensional arrays of real numbers Ta1a2...aD, where each index ac can take N values. The tensor entries Ta1a2...aD have no symmetry properties under permutations of the indices. The invariant polynomials built out of the tensor entries are called trace invariants.

We prove that for a Gaussian random tensor with D ≥ 3 indices (that is such that the entries Ta1a2...aD are independent identically distributed Gaussian random variables) the cumulant, or connected expectation, of a product of trace invariants is not always suppressed in scaling in N with respect to the product of the expectations of the individual invariants. Said otherwise, not all the multi-trace expectations factor at large N in terms of the single-trace ones and the Gaussian scaling is not subadditive on the connected components. This is in stark contrast to the D = 2 case of random matrices in which the multi-trace expectations always factor at large N. The best one can do for D ≥ 3 is to identify restricted families of invariants for which the large N factorization holds and we check that this indeed happens when restricting to the family of melonic observables, the dominant family in the large N limit.

## 1 Introduction

Initially introduced as generating functions for random discrete geometries [1,2], random tensors [3] have been increasingly studied as an interesting generalization of random matrices. Like random matrices, random tensors exhibit a large N limit [3], but, contrary to random matrices, this limit is dominated by melonic [3–9], rather than planar diagrams. A second set of applications of such models in physics stems from the realization that quantum mechanical models built from random tensors are similar to the Sachdev-Ye-Kitaev model [10–12] but do not require quenching the disorder [13–16].

Higher dimensional tensor field theories constitute a new class of large N field theories [17–23] and led to new families of conformal field theories [24–26].

From a mathematical point of view, tensors are quite different from matrices. For instance, while tensor eigenvalues exist and one can study their limit large N distribution [27–32], one needs to account for the fact that a tensor typically has exponentially many eigenvalues and eigenvectors [33,34] and that the eigenvector corresponding to an eigenvalue is unique (the eigenvalue equation is an inhomogenous polynomial equation in the eigenvector components). For random tensors, this leads to a novel eigenvector landscape [35].

More recently, there has been an increased effort to find an appropriate generalization of free probability theory [36,37] to random tensors [38–43] and in particular generalizations of free cumulants, and asymptotic moments – free cumulants relations for tensors have been proposed [40,41].

Large N factorization for random matrices. One main feature of random N × N matrices is that, for a large class of matrix probability measures, in the large N limit the moments (that is, the expectations of products of matrix invariants) factorize into products of expectations of the individual invariants. For instance, for a Hermitian random matrix H one has

⟨Tr(Hn

#### )...Tr(Hn

#### )⟩ ∼N→∞ ⟨Tr(Hn

#### )⟩...⟨Tr(Hn

)⟩ .

1

q

1

q

In turn, the expectations of the individual invariants are equal to the connected expectations, also known as classical cumulants in the mathematics literature1

⟨Tr(Hn

#### )⟩ = ⟨Tr(Hn

)⟩con. .

1

1

When approaching the free probability theory starting from matrices of increasing size, this factorization allows one to completely forget about the moments and focus instead on the classical cumulants. One promotes the classical cumulants to asymptotic moments and subsequently identifies further a new class of cumulants, the free cumulants. The two are related in the strict large N limit by novel moments cumulant relations in the lattice of non crossing partitions [44].

The large N factorization is also crucial for understanding large N conformal field theories, which play a fundamental role in the AdS/CFT correspondence [45]. The factorization ensures that in the strict large N limit the theory becomes classical (free in the physics sense, that is the quantum fluctuations are suppressed) and the operator product expansion significantly simplifies [46].

The main contribution of this paper. Seen how crucial the large N factorization is for random matrices, one can wonder if a similar factorization property holds for random tensors. In fact, a conjecture was formulated in [41] stating that this should indeed be the case for the simplest case of a Gaussian random tensor.

The result of this paper is that this conjecture is wrong: even in the case of Gaussian random tensors, factorization does not hold in general. It is not true that an arbitrary expectation of a product of invariants will factorize as a product of individual expectations. So where does this leave us? The main lesson and message of this paper is that in random tensors one needs to be careful. When discussing the asymptotic behavior of the expectations of observables at large N, the factorization will only hold for subfamilies of observables. We identify a first such family in this paper, namely the melonic family, and we expect that many more useful families can be found. However, in the full theory, the large N factorization fails and the structure of the large N limit is more intricate.

- 1In the free probability literature in particular it is common to denote this cumulant as φn1(H). We decide here


to stick to the physics notation ⟨. . .⟩con. for the connected moments.

## 2 Notation and main theorem

Tensors and trace invariants. We use the notation of [3] and we discuss the case of real tensors (the complex case is similar). A real tensor Ta1a2...aD living in the external tensor product of D fundamental representations of the orthogonal group O(N) changes under a change of basis as

Ta′1a2...aD =

b

Oa11b1Oa22b2 ...Oa3DbD Tb1b2...bD , O1,O2,...,OD ∈ O(N) . (2.1)

We emphasize that each tensor index transforms with its own orthogonal transformation and that the tensor has no symmetry properties under permutations of its indices.

An edge D-colored graph is a graph with 2n vertices labelled 1,2,...,2n and an edge set that is partitioned into D perfect matchings2 M1,M2 ...,MD between the vertices. We define the multi-set M = {M1,M2,...,MD}, and we denote the corresponding graph, somewhat abusively, also by M. A class of invariant polynomials in the tensor entries, called trace invariants, is associated to such edge D-colored graphs3. The polynomial TrM(T) associated with the graph M is built as follows [3]:

- • to every vertex i = 1,...,2n of M one associates a tensor Ta1

ia2i...,aDi ;

- • for every color c = 1,2,...,D and every edge {k,l} ∈ Mc, one associates a Kronecker delta

symbol δac

kacl with {k,l} identifying the indices in the position c of the tensors corresponding to the end vertices k and l;

- • one sums over all the available indices


  ,

 

2n

D

TrM(T) =

Ta1

δac

kacl

i a2i ...aDi

a

c=1

i=1

{k,l}∈Mc

and obtains a polynomial which is invariant under a change of basis as in (2.1). For D = 2, the trace invariants are just traces of powers of the product of T and its transposed Tr[(TTt)n

]...Tr[(TTt)n

] .

1

q

For any D, the trace invariants (also known as tensor networks in other corners of the literature [47]) form an over complete system at finite N, and a basis in the N → ∞ limit [48,49], in the space of invariants. We observe that if a graph M consists of two connected components4 M = M1 ⊔ M2 then the associated invariant splits accordingly

TrM

1⊔M2(T) = TrM

(T) TrM

(T) .

1

2

Gaussian random tensors. We are interested in the Gaussian expectations of trace invariants, which we denote by

Nν

2 a(Ta1a2...aD)2 TrM(T) .

dTa1a2...aD) e−

⟨TrM(T)⟩ = (

a1,...,aD

The tensor entries are independent normally distributed random variables with mean 0 and standard deviation N−ν, hence with covariance matrix

1 Nν

⟨Ta1a2...aDTb1b2...bD⟩ =

δa1b1δa2b2 ...δaDbD .

2A perfect matching is a partition of the vertex set into two element subsets. 3In the complex case the graphs are bipartite. Mutatis mutandis, our results carry over to that case. 4We denote M = M1 ⊔ M2 as the graph M that consists of the disjoint union of two connected components M1

and M2. Note that some relabeling of the vertices might be needed when taking such disjoint unions.

The factor Nν in the Gaussian measure is purely conventional, and we will see below that a common choice is ν = D − 1. We stress that our results are independent of this factor.

The Gaussian expectation of a product of 2n tensor entries is computed using the Wick theorem [50] as a sum over all the possible pairings (perfect matchings, or Gaussian contractions in the physics literature) between the tensor entries of a product of one covariance for each pair in the matching

2n

1 Nνn

k aDl ,

ka2l ...δaD

ka1l δa2

ia2i...aDi =

δa1

Ta1

i=1

M0∈Mn {k,l}∈M0

where M0 runs over the set Mn of all possible perfect matchings on 2n elements. Using √2πn nne−n < n! < √2πn nne−ne121n, it is straightforward to see that |Mn| = (22nnn)!! < √2e2

n

en nn. For the Gaussian expectation of an invariant one obtains

 

 

D

1 Nνn

⟨TrM(T)⟩ =

δa1

ka1l δa2

ka2l ...δaD

k aDl .

δac

kacl

M0∈Mn a

c=1 {k,l}∈Mc

{k,l}∈M0

We note that the matchings M1,...,MD and M0 play distinct roles: while the Mc matchings identify only one index pair between the end tensors, the matching M0 identifies all the indices between the two end tensors. By referring to Fn(M0,Mi) as the number of cycles with edges alternating between M0 and Mi (and the index n signals that there are 2n vertices in total), we conclude

1 Nνn

n(M0,M1)+Fn(M0,M2)+...+Fn(M0,MD) . (2.2)

NF

⟨TrM(T)⟩ =

M0∈Mn

For convenience, we define Fn(M0,M) = Fn(M0,M1) + Fn(M0,M2) + ... + Fn(M0,MD). Let G(M0,M) be the graph with the same vertex set as M and edge set M ∪ M0. Then G(M0,M) is an edge (D + 1)-colored graph (on 2n vertices).

The Gaussian scaling of the expectation of an observable is the maximal possible scaling with N

of a term in (2.2); that is, maxM0∈Mn Fn(M0,M). As we need to take the maximum over all potential choices for M0, the Gaussian scaling is not easy to compute in general.

Melonic graphs. The family of graphs that maximize the Gaussian scaling is well understood [3,4,51].

Definition 1 (Melonic graphs [3,4,51]). Melonic graphs are edge D-colored graphs whose connected components are connected melonic graphs. Connected melonic graphs with D colors are the family of graphs obtained by recursive insertions of two vertices connected by D−1 edges arbitrarily on any edge respecting the coloring, starting from the unique edge D-colored graph with two vertices and D edges. This is depicted in Fig. 1 below.

There is the following upper bound on the Gaussian scaling of an observable.

- Proposition 1 (Gaussian scaling bound [3,50]). Let D ≥ 2. Let M be an edge D-colored graph on


- 2n vertices. If M is connected, then for any M0, we have Fn(M0,M) = 1 + (D − 1)n − ω(M0,M) , ω(M0,M) ≥ 0 ,


and

- • for D = 2 and any M, there exist exactly n+11 2nn matchings M0 such that ω(M0,M) = 0;


Figure 1: Some melonic graphs with three colors. Left: the unique graph with two vertices and three edges. Center: the melonic graph obtained by inserting two vertices connected by two edges on the red edge of the graph on the left. Right: a melonic graph obtained after two insertions.

- • for D ≥ 3, we have ω(M0,M) = 0 if and only if G(M0,M) is a melonic graph with D + 1 colors and in this case M is a (connected) melonic graph with D colors and there exists exactly one M0 such that ω(M0,M) = 0.


If M has q > 1 connected components and G(M0,M) is connected, then

Fn(M0,M) = D − (D − 1)q + (D − 1)n − ω(M0,M) , ω(M0,M) ≥ 0 , and

- • for D = 2 and any M, there exist several M0 such that ω(M0,M) = 0;
- • for D ≥ 3, we have ω(M0,M) = 0 if and only if G(M0,M) is a melonic graph with D + 1 colors and in this case M is a (disconnected) melonic graph and there exist several M0 such that G(M0,M) is connected and melonic.


This proposition explains in particular why one usually takes the scaling ν = D − 1 for the Gaussian. With this scaling, for every connected M, we have

1 N

0,M) ;

N−ω(M

TrM(T) =

M0∈Mn

that is, the rescaled expectation of any connected trace invariant is a series in 1/N. Furthermore, the observables with maximal possible scaling (leading observables) are the melonic ones.

Classical cumulants. The classical cumulants, also called connected moments of the Gaussian measure, are defined starting from the expectations. In the following, we refer to π as a set partition of the set {1,...,q}, that is, π is a set of disjoint subsets of {1,...,q} whose union is {1,...,q}. Furthermore, we denote by ≤ the refinement order among partitions and by 1q the one set partition. If M1,...,Mq are connected graphs, the connected moments ⟨...⟩con., or classical cumulants φ... ... in the free probability literature, are defined implicitly by the relation

TrM

#### (T)...TrM

#### (T) =

TrM

#### (T)

1

q

i

π≤1q B∈π i∈B

which is inverted using the M¨bius inversion to

TrM

#### (T)...TrM

(T) con. =

1

q

π≤1q

λπ

TrM

B∈π i∈B

, (2.3)

con.

#### (T) ,

i

where λπ = (−1)|π|−1(|π| − 1)! is the M¨bius function in the lattice of partitions. For a connected component M1 only the one set partition contributes in (2.3). Hence the connected expectation (classical cumulant) equals the expectation

(T)⟩con. . For two connected graphs M1 and M2, the two partitions {{1},{2}} and {{1,2}} contribute ⟨TrM

⟨TrM

#### (T)⟩ = ⟨TrM

1

1

#### (T)⟩ = ⟨TrM

#### (T)⟩con. ⟨TrM

#### (T)⟩con. + ⟨TrM

(T)⟩con. .

#### (T)TrM

#### (T) TrM

1

2

1

2

1

2

Classical cumulants are defined for any probability measure. For the Gaussian measure, it is straightforward to show that any classical cumulant is computed as a sum over matchings M0 such that the graph G(M0,M) is connected

⟨TrM(T)⟩con. =

1 Nνn

M0∈Mn G(M0,M) connected

n(M0,M) . (2.4)

NF

If M is connected to begin with, then the connectivity restriction on G(M0,M) is automatically fulfilled and one finds that, as already highlighted, the moment and classical cumulant for a connect M coincide. But this restriction does play a role if M has several connected components M = M1 ⊔ ... ⊔ Mq. The Gaussian scaling of a classical cumulant (connected moment) is the maximal scaling

Fn(M0,M1 ⊔ ... ⊔ Mq) ,

max

M0∈Mn G(M0,M1⊔...⊔Mq) connected

of a term in the expansion (2.4).

Large N factorization. The large N factorization of the expectations occurs when in (2.3) the only leading contribution at large N is given by the partition of the set {1,...q} into one element sets π = {{1},{2},...{q}} and all the other terms are strictly suppressed in 1/N, that is,

q

q

(T) con. 1 + O(N−1) =

(T) 1 + O(N−1) .

TrM

#### (T)...TrM

(T) =

TrM

TrM

1

q

ρ

ρ

ρ=1

ρ=1

In order for this to hold, the Gaussian scaling of the cumulants needs to be strictly subadditive; that is, for any connect M1,...Mq with 2n1,2n2,...2nq vertices, respectively, we must have

q

1+...+nq(M0,M1 ⊔ ... ⊔ Mq) <

(Mρ0,Mρ) (2.5)

max

Fn

max

Fn

1

Mρ0∈Mnρ

M0∈Mn1+...+nq G(M0,M1⊔...⊔Mq) connected

ρ=1

where Mρ0 are perfect matchings on the 2nρ vertices of Mρ, and on the right hand side all the G(Mρ0,Mρ) are connected as each Mρ is connected.

The large N factorization holds for D = 2 and for the melonic family in any D. The large N factorization always holds when restricting to the melonic family. Indeed, for connected melonic observables Mρ with 2nρ vertices the Gaussian scaling of the cumulants can be read off from Proposition 1 and

q

D − (D − 1)q + (D − 1)(n1 + ... + nq) <

(1 + (D − 1)nρ) , q ≥ 2 .

ρ=1

Moreover, as the bounds in Proposition 1 are saturated by all the observables in D = 2, one recovers the known results that for D = 2 all the multi-trace expectations factor at large N into products of expectations of the single trace observables.

The general case. For D ≥ 3 one is naturally led to ask the question whether the large N factorization holds for arbitrary choices of observables. The answer to this question is negative and proving this fact is our main result.

Theorem 1 (Main Theorem). The Gaussian scaling for random tensors with D ≥ 3 indices is not strictly subadditive. In particular, there exist choices of connected graphs M1,M2,...,Mq such that

max

M0∈Mn1+...+nq G(M0,M1⊔...⊔Mq) connected

q

1+...+nq(M0,M1 ⊔ ... ⊔ Mq) >

Fn

ρ=1

(M10,Mρ) ,

max

Fn

ρ

Mρ0∈Mnρ

that is, the joint cumulant (connected expectation) of a multi-trace observable is larger in scaling than the product of the single trace expectations.

√2e/ϵ)

ln(e/2) and (D−22)n >

More precisely, for every ϵ > 0 and for n large enough such that n > ln(

(D ln7 − ln2) lnnn + D hold, a fraction of at least 1 − ϵ of all the edge D-colored graphs M on 2n vertices have at least a connected component Mρ with 2nρ vertices such that

max

F2n

M0∈M2nρ G(M0,Mρ⊔Mρ) connected

(M0,Mρ ⊔ Mρ) ≥ Dnρ > 2 max

Fn

ρ

M0∈Mnρ

(M0,Mρ) .

ρ

Therefore, the connected expectation TrM

(T) con. is strictly larger in scaling in N than the product of expectations TrM

(T)TrM

ρ

ρ

(T) TrM

(T) .

ρ

ρ

This theorem does not apply for D = 2, because in that case the inequality (D−22)n > (D ln7 −

ln2) lnnn + D false for all large enough n. For D ≥ 3, the inequality is always satisfied for large enough n; for D = 3 for example, starting at an n of order ∼ 76.

## 3 Proof of the main theorem

In this section, we prove our main theorem. Our strategy is to show that if we select D perfect matchings at random, then with probability very close to 1, they form a collection that verifies the statement of Theorem 1.

The boundary graph. In the following, we will introduce boundary graphs [3,50]. These graphs arise from edge D-colored graphs M when we consider a not necessarily perfect matching M¯ 0 and encode in this graph all information that is already given by M¯ 0 in view of M¯ 0 being completed to a perfect matching M0 at some later stage.

To this end, let M = {M1,...,MD} be an edge D-colored graph on 2n vertices, and consider a matching M¯ 0 with at most n edges on the vertex set of M. Observe that Mc ∪M¯ 0 is a graph whose vertices are incident to at most two edges; that is, its compenents consists of paths and even cycles. In addition, the paths and cycles have edges alternating between Mc and M¯ 0. Crucially, for these paths the first and the last edge are always in Mc (the first and the last edge may be the same). Let us call these paths the alternating paths of M with respect to M¯ 0 and we say a path has color c if the path has a nonempty intersection with Mc. The boundary graph ∂M¯0M of M with respect to M¯ 0 arises from M by adding for all colors c and for all alternating paths with color c an edge of color c between the two end points of the paths; afterwards we delete all the original edges and vertices not incident to the new edges, that is, exactly all vertices of M¯ 0. Note that the boundary graph is again an edge D-colored graph on 2n − 2|M¯ 0| vertices.

Some examples are displayed in Figure 2. We note that it is possible for the graph M to be connected and have a disconnected boundary graph ∂M¯0M for some M¯ 0.

Figure 2: The first and the third graph display the same edge 3-colored graph with two different choices for M¯ 0, where the dash edges indicate the edges of M¯ 0. The second and the fourth graph show the boundary graph with respect to the particular choice of M¯ 0.

A necessary and sufficient condition for factorization. We proceed with some observations regarding a potential factorization. Imagine all multi-trace observables factorize then, for any connected M on 2n vertices, the expectation

⟨TrM(T)TrM(T)⟩ = ⟨TrM(T)⟩con. ⟨TrM(T)⟩con. + ⟨TrM(T)TrM(T)⟩con. ,

should also factorize; that is, the disconnected (first) term on the right-hand side in the above equation must be strictly larger in scaling than the connected (second) term. Among the Gaussian pairings M0 admissible for the connected term, one consists in connecting every vertex in one M to its copy in the second M. This pairing always satisfies F2n(M0,M ⊔ M) = Dn. It follows that the multi-trace observables factorize, or equivalently the Gaussian scaling of cumulants is strictly subadditive, only if for every connected M, we have

Fn(M0,M) >

max

M0∈Mn

Dn 2

. (3.1)

In fact, the converse is also true as the following lemma shows.

We remark that (3.1) holds for all connected edge D-colored graphs M if and only if (3.1) holds for all edge D-colored graphs M. Indeed, if it holds for all edge D-colored graphs, then clearly it holds for all connected edge D-colored graphs. If it holds for all connected graphs, then simply take a matching in each component that attains the maximum and then the union of these matchings shows that (3.1) holds for all graphs.

Lemma 1. The Gaussian scaling is strictly subadditive if and only if for any connected edge Dcolored graph M on 2n vertices, we have

Dn 2

Fn(M0,M) >

max

.

M0∈Mn

Proof. As we argued above, if the Gaussian scaling is strictly subadditive, then (3.1) holds. Hence, it remains that the reversed implication is also true.

To this end, consider connected edge D-colored graphs M1,...,Mq; say, Mρ has 2nρ vertices and ρ nρ = n and M = M1⊔···⊔Mq as well as M = {M1,...,MD}. We need to check that (2.5) holds. Let M0 be any perfect matching on the vertex set of M such that G(M0,M) is connected. In order to finish the proof it suffices to construct perfect matchings Mρ on the vertex set of Mρ such that Fn(M0,M) < ρ Fn

(Mρ,Mρ) holds.

ρ

Let us turn to the details. For each ρ, we denote by Mρ0 the set of edges of M0 with both endpoints in Mρ. Let S0 = M0 \(M10 ∪...∪Mq0); that is, S0 is the subset of M0 consisting of edges that join two different Mρ. Note that S0 ̸= ∅.

Mρ encode all important information we need for the edges in M0 that join two different Mρ. Observe that S0 is a perfect matching on ρ ∂M0

Next, we exploit that the boundary graphs ∂M0

ρ

### Mρ

ρ

and let s = |S|. Crucially, no edge of S0 belongs to a cycle of with only two edges. Thus the number of cycles that alternate between edges in S0 and edges in some Mc is at most Ds2 . By our assumption, for each ρ, there exists a perfect matching M0ρ in ∂M0

Mρ such that M0 =

ρ

ρ M0ρ yields more than Ds2 cycles that alternate between edges in M0 and edges in some Mc. Therefore, Fn(M0,M) < ρ Fn

(Mρ0 ∪ M0ρ,Mρ), which completes the proof.

| |
|---|


ρ

In order to prove Theorem 1, it is therefore enough to exhibit a graph that violates the bound in Lemma 1. It turns out that finding an explicit counterexample is not immediate, but one can use a statistical argument and prove that among large enough graphs, essentially all instances are counterexamples.

Additional families of graphs for which the bound in Lemma 1 holds. Of course, the bound in Lemma 1 holds for melonic graphs. It holds, however, also for larger classes of graphs.

Consider the case where D = 3 and the graph M = {M1,M2,M3} is planar when embedded respecting the colors, that is, such that the faces, or 2-cells, of the embedded graph are the bi-colored cycles. We emphasize that this is the notion of planarity of ribbon graphs [52] (and combinatorial maps), and it is slightly different from the usual notion of planarity in graph theory. For ribbon graphs one requires that the two dimensional cellular complex with 0-cells (the vertices), 1-cells (the edges) and 2-cells (the prescribed faces) is homeomorphic to the 2-dimensional sphere. In the usual sense in graph theory a graph is called planar if the 1-complex with 0-cells (the vertices) and 1-cells (the edges) can be completed to some 2-complex homeomorphic to the 2-dimensional sphere by adding in some way 2-cells formed by cycles of edges.

Suppose M has 2n vertices and hence 3n edges. We denote by Fn(Mi,Mj) the number of bicolored cycles formed by alternating edges in Mi and Mj. Then the Euler relation5 for such a planar graph implies

Fn(M1,M2) + Fn(M1,M3) + Fn(M2,M3) = n + 2q , where q is the number of connected components. In this case there exist two pairs of colors, say 12 and 13 so that Fn(M1,M2) + Fn(M1,M3) > n2 + q. Taking M0 = M1 yields

n 2

Fn(M0,M) = Fn(M1,M1) + Fn(M1,M2) + Fn(M1,M3) > n +

+ q .

Note, however, that one can not conclude from here that, when restricted to planar observables, the large N factorization holds. Contrary to the melonic family, for which we have checked directly that the factorization holds, for the planar family we have only checked that the Gaussian scaling respects the bound in Lemma 1. As we shall see in the following, there exist (non-planar) graphs that violate the bound in Lemma 1. Hence, the large N factorization does not hold in general, and there is no guarantee a priori that factorization holds for planar graphs: in the proof of Lemma 1 we need to assume the bound holds for all the graphs in order to obtain the factorization.

Pairs of random matchings. Later we consider random graphs that are the union of D randomly chosen matchings. To this end, we first investigate the cycle structure of two random matchings (see Proposition 2). For the proof we need the following inequality. Suppose that we are given

- 0 ≤ p1 ≤ p2 ··· ≤ pn with ni=1 pi = 1 and A1 ≥ A2 ··· ≥ An. Then for any i and j, we have (pj − pi)(Ai − Aj) ≥ 0. Consequently, we can compute


n

n

n

n

n

n

pj − pi n

pjAi − piAi n

- 1

- 2


1 n

0 ≤

(Ai − Aj) =

Ai −

=

piAi.

i=1

j=1

i=1

j=1

i=1

i=1

5The Euler relation for a general embedded graph is χ = V − E + F = 2q − k, where χ is the Euler characteristic, V the number of vertices (0-cells), E the number of edges (1-cells), F the number of faces (2-cells), q the number of connected components and k the non-orientable genus of the embedded graph.

#### Rearranging yields

n

1 n

piAi ≤

i=1

n

Ai . (3.2)

i=1

In the following, we refer to P as the probability and to E as the expectation. Observe that the union of two perfect matchings is a union of cycles of even length. In addition, there is a bijection between the union of two perfect matchings on 2n vertices and permutations on 2n elements with only even cycles. The following could also be deduced from existing results in the literature [53, see the proof of Proposition 8.2], but for completeness we give the short proof here.

- Proposition 2. Fix some perfect matching M0 on 2n vertices and add a perfect matching M uniformly at random on the same vertex set. Then for any t > 0, we have


7n (2n)t

P Fn(M0,M) ≥ t ≤

.

Proof. The proof is split into three parts. We first make a general remark on random perfect matchings afterwards we calculate the probability that a particular edge of M0 is contained in a cycle in G(M0,M) of length 2k for any k. As a third step, we prove an upper bound on E[mF

n(M0,M)] for any integer m ≥ 2n. This is turn yields the desired bound by utilizing Markov’s inequality.

Let us turn to the details. Recall that M is a perfect matching chosen uniformly at random among all the perfect matchings on {1,...,2n}. We make two simply observations.

- (i) By symmetry, the vertex i is joined by M to some vertex j and j is a uniformly chosen element of {1,...,2n} \ {i}.
- (ii) Let v1,...,v2ℓ ∈ {1,...,2n} be distinct. The distribution of M conditioned on {v2i−1,v2i} ∈ M for all i = 1,...,ℓ equals that of a uniformly chosen perfect matching on {1,...,2n} \ {v1,...,v2ℓ}.


Recall that M ∪ M0 is the union of cycles of even length. Let {a1,a2} ∈ M0 be arbitrary but fixed. For any k, we denote by pk the probability that {a1,a2} belongs to a cycle of length 2k. Thus, pk = 0 for all k > n.

By (i), we conclude that the probability that a2 is matched to a1 in M equals 1/(2n − 1) = p1. Suppose now k ≥ 2. In the following we tacitly assume that ai ̸= aj for i ̸= j if not stated otherwise. The probability that a2 is not matched to a1 in M equals 1 − 1/(2n − 1) = (2n − 2)/(2n − 1), again by (i). So suppose {a2,a3} ∈ M for some a3. In turn {a3,a4} ∈ M0 for some a4. The probability that a4 is matched to a1 in M (conditioned on {a2,a3} ∈ M) is 1/(2n − 3), by (i) and (ii). Hence p2 = 22nn−−12 2n1−3.

This easily reveals the general pattern. Suppose {a1,a2},...,{a2i−1,a2i} ∈ M0 and we condition on {a2,a3},...,{a2i−2,a2i−1} ∈ M, then the probability that a2i is matched to a1 in M is 1/(2n−2i+

- 1) and the probability that a2i is matched to a2i+1 in M is 1−1/(2n−2i+1) = (2n−2i)/(2n−2i+1), again by (i) and (ii). Consequently, this yields


2n − 4 2n − 3

2n − 2k + 2 2n − 2k + 3

2n − 2 2n − 1

1 2n − 2k + 1

...

.

pk =

Observe that

2n − 2k 2n − 2k − 1

1 2n − 2k − 1

= pk 1 +

pk+1 = pk

,

for all k < n and so p1 < ... < pn as well as ni=1 pi = 1.

Next, we prove by induction on n that for any integer m ≥ 2n

m + n − 1 m − 1

n(M0,M)] ≤

E[mF

1(M0,M)] = m = m m−1 . Let Ek denote the event that e belongs to a cycle of length k in M ∪ M0. For n ≥ 2, we compute

holds. Indeed, fix an edge e in M0 and for n = 1 we evaluate E[mF

n

n

n(M0,M)] =

n(M0,M)| Ek ] =

n−k(Mn0−k,Mn−k)] ,

E[mF

pk E[mF

pkm E[mF

k=1

k=1

where Mn0−k is a matching on 2n − 2k vertices and Mn−k is a uniformly chosen perfect matching on the same vertex set; for the last equality we used again (ii). In addition, we set E[mF

0(M00,M0)] = 1. Recall that rs = rs+1+1 − s+1 r folds for all integers r,s ≥ 0 and hence

s

s

r + i − 1 r

r − 1 r

r + i − 1 r − 1

r + i r −

r + s r −

r + s r

=

=

=

.

i=0

i=0

n−1(Mn0−1,Mn−1)] ≥ E[mF

n(Mn0,Mn)] ≥ p1mE[mF

As m ≥ 2n implies that p1m ≥ 1, we observe that E[mF

n(Mn0−k,Mn−k)] is decreasing in k. This allows us to utilize (3.2) and the induction hypothesis to conclude that

n−1(Mn0−1,Mn−1)]. Hence E[mF

- m

- n


n(M0,M)] ≤

E[mF

- m

- n


≤

n

n−k(Mn0−k,Mn−k)]

E[mF

k=1

n−1

m + k − 1 m − 1

m + n − 1 m

- m

- n


=

k=0

=

m + n − 1 m − 1

.

For any real random variable X ≥ 0 and any real number t > 0, we observe that E[X]/t ≥ E[1X≥t] = P[X ≥ t]. This is known as Markov’s inequality. Therefore, we obtain

3n−1 n

n(M0,M)] (2n)t ≤

E[(2n)F

7n (2n)t

n(M0,M) ≥ (2n)t ≤

P Fn(M0,M) ≥ t = P (2n)F

(2n)t ≤

,

which completes the proof.6

| |
|---|


Random graphs. We are finally in the position to prove that among large enough graphs we always find some which violate the inequality in Lemma 1.

- Proposition 3. There exists an edge D-colored graph M on 2n vertices such that


n lnn

Fn(M0,M) < n + (D ln7 − ln2)

+ D = (1 + o(1))n ,

√2e/ϵ)

for every perfect matching M0. In fact, for every ϵ > 0 and n > ln(

ln(e/2) , a fraction of at least 1−ϵ of all the edge D-colored graphs with 2n vertices satisfies this bound for every M0.

6Using a straightforward induction argument yields 3nn−1 ≤ 2323nn , marginally better than the 7n bound we used.

Proof. We fix a perfect matching M0 on the 2n vertices. We add uniformly at random the D perfect matchings M1,...,MD. We claim that

n lnn

+ D < n−n .

P Fn(M0,M) ≥ n + (D ln7 − ln2)

Indeed, this can be seen as follows. Let us denote A = n + (D ln7 − ln2) lnnn + D. We compute using Proposition 2 in the last line

P Fn(M0,M) ≥ A ≤

P Fn(M0,M1) ≥ t1,Fn(M0,M2) ≥ t2,...,Fn(M0,MD) ≥ tD

t1,t2,...,tD≤n t1+t2+···+tD=A

≤ nD max

P Fn(M0,M1) ≥ t1,Fn(M0,M2) ≥ t2,...,Fn(M0,MD) ≥ tD

t1,t2,...,tD t1+t2+···+tD=A

D

7n (2n)tc < nD 7Dn 2−n n−A = n−n .

≤ nD max

P Fn(M0,Mc) ≥ tc ≤ nD

t1,t2,...,tD t1+t2+···+tD=A

c=1

t1+t2+···+tD=A

Observe that our random selection of M corresponds to the uniform distribution on all edge Dcolored graphs (on 2n labelled vertices). It follows that a fraction larger than 1 − n−n of all the graphs M satisfies Fn(M0,M) < A. Using the union bound and taking into account that there are in total |Mn| = (22nnn)!! < √2e2

n

en nn possible matchings M0, we conclude that there is a fraction of the graphs M larger than 1 − |Mn|n−n > 1 −

√2e2

n

en such that Fn(M0,M) < A holds for all the matchings M0.

| |
|---|


A multi-trace expectation that does not factorize. An explicit example of a multi-trace observable that does not factorize at large N is obtained by taking n large enough such that n+(D ln7− ln2) lnnn + D < D2 n. If the graph M in Proposition 3 is connected, then ⟨TrM(T)TrM(T)⟩con. is strictly larger in scaling in N than ⟨TrM(T)⟩⟨TrM(T)⟩. If M is disconnected, then for at least one of its connected components Mρ, we have maxM0

(Mρ0,Mρ) < Dn2 ρ and TrM

Fn

(T) con. is strictly larger in scaling in N than TrM

(T)TrM

ρ∈Mnρ

ρ

ρ

ρ

(T) . Indeed, if for all the connected components of M we had maxM0

(T) TrM

ρ

ρ

(Mρ0,Mρ) ≥ Dn2 ρ, then there would exist some matching M0 such that Fn(M0,M) ≥ Dn2 , which contradicts the fact that for any M0 we have Fn(M0,M) < n + (D ln7 − ln2) lnnn + D < Dn2 .

Fn

ρ∈Mnρ

ρ

Combining this remark with Proposition 3 proves our main result, Theorem 1.

## Acknowledgments

This work is supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under Germany’s Excellence Strategy EXC 2181/1 - 390900948 (the Heidelberg STRUCTURES Excellence Cluster). Research of the third author was supported in part by SNSF grant 200021228014.

## References

- [1] J. Ambjorn, B. Durhuus, and T. Jonsson, “Three-dimensional simplicial quantum gravity and generalized matrix models,” Mod. Phys. Lett., vol. A6, pp. 1133–1146, 1991.


- [2] N. Sasakura, “Tensor model for gravity and orientability of manifold,” Mod. Phys. Lett., vol. A6, pp. 2613–2624, 1991.
- [3] R. Gurau, Random Tensors. Oxford: Oxford University Press, 2016.
- [4] V. Bonzom, R. Gurau, A. Riello, and V. Rivasseau, “Critical behavior of colored tensor models in the large N limit,” Nucl. Phys., vol. B853, pp. 174–195, 2011.
- [5] D. Benedetti, S. Carrozza, R. Gurau, and M. Kolanowski, “The 1/N expansion of the symmetric traceless and the antisymmetric tensor models in rank three,” Commun. Math. Phys., vol. 371, no. 1, pp. 55–97, 2019.
- [6] I. R. Klebanov and G. Tarnopolsky, “Uncolored Random Tensors, Melon Diagrams, and the SYK Models,” Phys. Rev., vol. D95, no. 4, p. 046004, 2017.
- [7] S. Carrozza, “Large N limit of irreducible tensor models: O(N) rank-3 tensors with mixed permutation symmetry,” JHEP, vol. 06, p. 039, 2018.
- [8] S. Carrozza and S. Harribey, “Melonic Large N Limit of 5-Index Irreducible Random Tensors,” Commun. Math. Phys., vol. 390, no. 3, pp. 1219–1270, 2022.
- [9] S. Prakash and R. Sinha, “Melonic Dominance in Subchromatic Sextic Tensor Models,” Phys. Rev. D, vol. 101, no. 12, p. 126001, 2020.
- [10] S. Sachdev and J. Ye, “Gapless spin fluid ground state in a random, quantum Heisenberg magnet,” Phys. Rev. Lett., vol. 70, p. 3339, 1993.
- [11] A. Kitaev, “A simple model of quantum holography,” KITP strings seminar and Entanglement 2015, Feb. 12, April 7, and May 27, 2015.
- [12] J. Maldacena and D. Stanford, “Remarks on the Sachdev-Ye-Kitaev model,” Phys. Rev., vol. D94, no. 10, p. 106002, 2016.
- [13] E. Witten, “An SYK-Like Model Without Disorder,” J. Phys. A, vol. 52, no. 47, p. 474002, 2019.
- [14] F. Ferrari and F. I. Schaposnik Massolo, “Phases Of Melonic Quantum Mechanics,” Phys. Rev. D, vol. 100, no. 2, p. 026007, 2019.
- [15] K. Pakrouski, I. R. Klebanov, F. Popov, and G. Tarnopolsky, “Spectrum of Majorana Quantum Mechanics with O(4)3 Symmetry,” Phys. Rev. Lett., vol. 122, no. 1, p. 011601, 2019.
- [16] I. R. Klebanov, A. Milekhin, F. Popov, and G. Tarnopolsky, “Spectra of eigenstates in fermionic tensor quantum mechanics,” Phys. Rev., vol. D97, no. 10, p. 106023, 2018.
- [17] S. Giombi, I. R. Klebanov, and G. Tarnopolsky, “Bosonic tensor models at large N and small ϵ,” Phys. Rev., vol. D96, no. 10, p. 106014, 2017.
- [18] S. Giombi, I. R. Klebanov, F. Popov, S. Prakash, and G. Tarnopolsky, “Prismatic Large N Models for Bosonic Tensors,” Phys. Rev., vol. D98, no. 10, p. 105005, 2018.
- [19] J. Kim, I. R. Klebanov, G. Tarnopolsky, and W. Zhao, “Symmetry Breaking in Coupled SYK or Tensor Models,” Phys. Rev. X, vol. 9, no. 2, p. 021043, 2019.
- [20] S. Choudhury, A. Dey, I. Halder, L. Janagal, S. Minwalla, and R. Poojary, “Notes on melonic O(N)q−1 tensor models,” JHEP, vol. 06, p. 094, 2018.


- [21] D. Benedetti and N. Delporte, “Phase diagram and fixed points of tensorial Gross-Neveu models in three dimensions,” JHEP, vol. 01, p. 218, 2019.
- [22] D. Benedetti and N. Delporte, “Remarks on a melonic field theory with cubic interaction,” JHEP, vol. 04, p. 197, 2021.
- [23] D. Benedetti, R. Gurau, and S. Harribey, “Line of fixed points in a bosonic tensor model,” JHEP, vol. 06, p. 053, 2019.
- [24] R. G. Gurau, “Notes on tensor models and tensor field theories,” Ann. Inst. H. Poincare D Comb. Phys. Interact., vol. 9, no. 1, pp. 159–218, 2022.
- [25] I. R. Klebanov, F. Popov, and G. Tarnopolsky, “TASI Lectures on Large N Tensor Models,” PoS, vol. TASI2017, p. 004, 2018.
- [26] D. Benedetti, “Melonic CFTs,” PoS, vol. CORFU2019, p. 168, 2020.
- [27] R. Gurau, “On the generalization of the Wigner semicircle law to real symmetric tensors,” 4

2020. arXiv: 2004.02660.

- [28] O. Evnin, “Melonic dominance and the largest eigenvalue of a large random tensor,” Lett. Math. Phys., vol. 111, no. 3, p. 66, 2021.
- [29] S. Majumder and N. Sasakura, “Three Cases of Complex Eigenvalue/Vector Distributions of Symmetric Order-Three Random Tensors,” PTEP, vol. 2024, no. 9, p. 093A01, 2024.
- [30] N. Delporte and N. Sasakura, “The edge of random tensor eigenvalues with deviation,” JHEP, vol. 01, p. 071, 2025.
- [31] M. R. Kloos and N. Sasakura, “Usefulness of signed eigenvalue/vector distributions of random tensors,” Lett. Math. Phys., vol. 114, no. 3, p. 80, 2024.
- [32] R. Bonnin, “Universality of the Wigner-Gurau limit for random tensors,” 4 2024. arxiv: 2404.14144.
- [33] D. Cartwright and B. Sturmfels, “The number of eigenvalues of a tensor,” Linear algebra and its applications, vol. 438, no. 2, pp. 942–952, 2013.
- [34] P. Breiding, “How many eigenvalues of a random symmetric tensor are real?,” Transactions of the American Mathematical Society, vol. 372, no. 11, pp. 7857–7887, 2019.
- [35] G. B. Arous, S. Mei, A. Montanari, and M. Nica, “The landscape of the spiked tensor model,” Communications on Pure and Applied Mathematics, vol. 72, no. 11, pp. 2282–2330, 2019.
- [36] D. Voiculescu, “Limit laws for random matrices and free products,” Invent. Math., vol. 104, p. 201, 1991.
- [37] D. Voiculescu, K. Dykema, and A. Nica, Free random variables. AMS: CRM Monograph Series, 1992.
- [38] B. Collins, R. Gurau, and L. Lionni, “The tensor Harish-Chandra–Itzykson–Zuber integral I: Weingarten calculus and a generalization of monotone Hurwitz numbers,” J. Eur. Math. Soc., vol. 26, no. 5, pp. 1851–1897, 2024.
- [39] B. Collins, R. Gurau, and L. Lionni, “The Tensor Harish-Chandra–Itzykson–Zuber Integral II: Detecting Entanglement in Large Quantum Systems,” Commun. Math. Phys., vol. 401, no. 1, pp. 669–716, 2023.


- [40] R. Bonnin and C. Bordenave, “Freeness for tensors,” 7 2024. arXiv :2407.18881.
- [41] B. Collins, R. Gurau, and L. Lionni, “Free cumulants and freeness for unitarily invariant random tensors,” 10 2024. arXiv: 2410.00908.
- [42] R. Bonnin, “Tensorial free convolution, semicircular, free Poisson and R-transform in high order,” 12 2024. arxiv: 2412.02572.
- [43] B. Au and J. Garza-Vargas, “Spectral asymptotics for contracted tensor ensembles,” Electronic Journal of Probability, vol. 28, 01 2023.
- [44] A. Nica and R. Speicher, Lectures on the combinatorics of free probability (London Mathematical Society Lecture Note Series). Cambridge: Cambridge University Press, 2006.
- [45] J. M. Maldacena, “The Large N limit of superconformal field theories and supergravity,” Adv. Theor. Math. Phys., vol. 2, pp. 231–252, 1998.
- [46] I. Heemskerk, J. Penedones, J. Polchinski, and J. Sully, “Holography from Conformal Field Theory,” JHEP, vol. 10, p. 079, 2009.
- [47] R. Or´us, “Tensor networks for complex quantum systems,” APS Physics, vol. 1, pp. 538–550, 2019.
- [48] J. Ben Geloun and S. Ramgoolam, “Counting tensor model observables and branched covers of the 2-sphere,” Ann. Inst. H. Poincare D Comb. Phys. Interact., vol. 1, no. 1, pp. 77–138, 2014.
- [49] J. Ben Geloun and S. Ramgoolam, “Tensor Models, Kronecker coefficients and Permutation Centralizer Algebras,” JHEP, vol. 11, p. 092, 2017.
- [50] R. Gurau, “Universality for Random Tensors,” Ann. Inst. H. Poincar´e Proba. Stat., vol. 50, no. 4, pp. 1474–1525, 2014.
- [51] R. Gurau and G. Schaeffer, “Regular colored graphs of positive degree,” Ann. Inst. Henri Poincar´e Comb. Phys. Interact., vol. 3, pp. 257–320, 2016.
- [52] J. A. Ellis-Monaghan and I. Moffatt, Graphs on surfaces: dualities, polynomials, and knots, vol. 84. Springer, 2013.
- [53] M. Lugo, “Profiles of Permutations,” Electron. J. Combin., vol. 16, p. R99, 2009.


