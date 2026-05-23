## 23 RANDOM SIMPLICIAL COMPLEXES

Matthew Kahle

# arXiv:1607.07069v1[math.CO]24Jul2016

#### INTRODUCTION

Random shapes arise naturally in many contexts. The topological and geometric structure of such objects is interesting for its own sake, and also for applications. In physics, for example, such objects arise naturally in quantum gravity, in material science, and in other settings. Stochastic topology may also be considered as a null hypothesis for topological data analysis.

In this chapter we overview combinatorial aspects of stochastic topology. We focus on the topological and geometric properties of random simplicial complexes. We introduce a few of the fundamental models in Section 23.1. We review highdimensional expander-like properties of random complexes in Section 23.2. We discuss threshold behavior and phase transitions in Section 23.3, and Betti numbers and persistent homology in Section 23.4.

### 23.1 MODELS

We brieﬂy introduce a few of the most commonly studied models.

#### 23.1.1 ERDOS–R˝ ENYI-INSPIRED´ MODELS

A few of the models that have been studied are high-dimensional analogues of the Erd˝s–R´enyi random graph.

#### The Erd˝s–R´enyi random graph

The Erd˝s–Re´nyi random graph G(n,p) is the probability distribution on all graphs on vertex set [n] = {1,2,...,n}, where every edge is included with probability p jointly independently. Standard references include [Bol01] and [J LR00].

One often thinks of p as a function of n and studies the asymptotic properties of G(n,p) as n → ∞. We say that an event happens with high probability (w.h.p.) if the probability approaches 1 as n → ∞.

Erd˝s–R´enyi showed that p¯ = log n/n is a sharp threshold for connectivity. In other words,: for every ﬁxed > 0, if p ≥ (1+ )¯p then w.h.p. G(n,p) is connected, and if p ≤ (1 − )¯p then w.h.p. it is disconnected. A slightly sharper statement is given in the following section. Several thresholds for topological properties of G(n,p) are summarized in Table 23.1.1.

TABLE 23.1.1 Topological thresholds for G = G(n,p). The column SHARP indicates whether the threshold is sharp, coarse, or one-sided sharp. The column TIGHT indicates whether there is any room for improvement on the present bound.

|PROPERTY<br><br>|THRESHOLD|SHARP<br><br>|TIGHT<br><br>|SOURCE|
|---|---|---|---|---|
|G is not 0-collapsible H1(G) = 0 G is not planar G contains arbitrary minors G is pure 1-dimensional G is connected<br><br>|1/n 1/n 1/n 1/n log n/n log n/n|one-sided one-sided<br><br>sharp sharp sharp sharp<br><br>|yes yes yes yes yes yes|[Pit88] [Pit88] [ LPW94] [AKS79] [ER59] [ER59]<br><br>|


#### GLOSSARY

Threshold function: Let P be a graph property. We say that f is a threshold function for property P in the random graph G = G(n,p) if whenever p = ω(f), G has property P w.h.p. and whenever p = o(f), G does not have property P.

Sharp threshold: We say that f is a sharp threshold for graph property P if there exists a function g = o(f) such that for p < f −g, G ∈/ P w.h.p. and if p > f +g, G ∈ P w.h.p.

Simplicial complex: A simplicial complex ∆ is a collection of subsets of a set S, such that (1) if U ⊂ V is nonempty and V ∈ ∆ then U ∈ ∆, and (2) {v} ∈ ∆ for every v ∈ S. An element of ∆ is called a face. Such a set system can be naturally associated a topological space by considering every set of size k in ∆ to represent a k − 1-dimensional simplex, homeomorphic to a closed Euclidean ball. This topological space is sometimes called the geometric realization of ∆, but we will slightly abuse notation and identify a simplicial complex with its geometric realization.

Link: Given a simplicial complex ∆ and a face σ ∈ ∆, the link of σ in ∆ is deﬁned

by

lk∆(σ) = {τ ∈ ∆ | τ ∩ σ = ∅ and τ ∪ σ ∈ ∆}. The link is itself a simplicial complex.

Homology: Associated with any simplicial complex X, abelian group G, and integer i ≥ 0, Hi(X,G) denotes the ith homology group of X with coeﬃcients in G. If k is a ﬁeld, then Hi(X,k) is a vector space over k. Homology is deﬁned as “cycles modulo boundaries”. Homology is invariant under homotopy deformations.

Betti numbers: If one considers homology with coeﬃcients in R, then Hi(X,R) is a real vector space. The Betti numbers βi are deﬁned by βi = dimHi (X,R). The 0th Betti number β0 counts the number of connected components of X, and in general the ith Betti number is said to count the number of i-dimensional holes in X.

#### The random 2-complex

Random hypergraphs have been well studied, but if we wish to study such objects topologically then random simplicial complexes is probably a more natural point of view.

Linial and Meshulam introduced the topological study of the random 2-complex Y (n,p) in [LM06]. This model of random simplicial complex has n vertices, n2

edges, and each of the n3 possible 2-dimensional faces is included independently with probability p.

The random 2-complex is perhaps the most natural 2-dimensional analogue of G(n,p). For example, the link of every vertex in Y (n,p) has the same distribution as G(n − 1,p).

Several topological thresholds for Y (n,p) discussed in the next section are described in Table 23.1.2.

TABLE 23.1.2 Topological thresholds for the random 2-complex Y = Y (n,p). c.f. in the TIGHT column means that the bound is best possible up to a constant factor.

|PROPERTY<br><br>|THRESHOLD|SHARP<br><br>|TIGHT<br><br>|SOURCE|
|---|---|---|---|---|
|Y is not 1-collapsible H2(Y, R) = 0 cdim π1(Y ) = 2 Y is not embeddable in R4 Y is pure 2-dimensional H1(Y, Z/ Z) = 0 H1(Y, R) = 0 π1(Y ) has property (T) H1(Y, Z) = 0 cdim π1(Y ) = ∞ Y contains arbitrary subdivisions π1(Y ) = 0<br><br>|2.455/n 2.753/n Θ(1/n) Θ(1/n) 2 log n/n 2 log n/n 2 log n/n 2 log n/n O(log n/n) 1/n3/5 θ 1/√n O(1/√n)<br><br>|one-sided one-sided<br><br>? ?<br><br>sharp sharp sharp sharp sharp coarse<br><br>? ?<br><br>|yes yes c.f. c.f. yes yes yes yes c.f. yes c.f. no<br><br>|[CCFK12, AL LM13, AL16] [Koz10, LP14, AL15] [CF15a, New16] [Wag11] [LM06] [LM06, MW09] [LM06, HKP12]<br><br>[HKP12]<br>[HKP13] [CF13]<br><br><br>[GW16] [BHK11, GW16, KPS16]|


TABLE 23.1.3 Topological thresholds for Yd(n,p), d > 2. Deﬁnitions for the constants cd and c∗d are given in Section 2.3.2.

|PROPERTY<br><br>|THRESHOLD|SHARP<br><br>|TIGHT<br><br>|SOURCE|
|---|---|---|---|---|
|Y is not (d − 1)-collapsible Hd(Y, R) = 0 Y is not embeddable in R2d Y is pure d-dimensional Hd−1(Y, Z/ Z) = 0 Hd−1(Y, R) = 0 Hd−1(Y, Z) = 0 πd−1(Y ) = 0|cd/n c∗d/n Θ(1/n)<br><br>d log n/n d log n/n d log n/n<br><br>O(log n/n) O(log n/n)<br><br>|one-sided one-sided ? sharp sharp sharp sharp sharp|yes yes c.f. yes yes yes c.f. c.f.<br><br>|[AL LM13, AL16] [Koz10, LP14, AL15] [Wag11] [MW09] [MW09, HKP12]<br><br>[HKP12]<br>[HKP13] [HKP13]<br>|


#### The random d-complex

The natural generalization to d-dimensional model was introduced by Meshulam and Wallach in [MW09]. For the random d-complex Yd(n,p), contains the complete (d − 1)-skeleton of a simplex on n vertices, and every d-dimensional face appears independently with probability p. Some of the topological subtlety of the random 2-dimensional model collapses in higher dimensions: for d ≥ 3, the complexes are d − 2-connected, and in particular simply connected. By the Hurewicz theorem, πd−1(Y ) is isomorphic to Hd−1(Y,Z), so these groups have the same vanishing threshold.

#### The random clique complex

Another analogue of G(n,p) in higher dimensions was introduced in [Kah09]. The random clique complex X(n,p) is the clique complex of G(n,p). It is the maximal simplicial complex compatible with a given graph. In other words, the faces of the clique complex X(H) correspond to complete subgraphs of the graph H.

The random clique complex asymptotically puts a measure over a wide range of topologies. Indeed, every simplicial complex is homeomorphic to a clique complex, e.g. by barycentric subdivision.

There are several comparisons of this model to the random d-complex, but some important contrasts as well. One contrast to Yd(n,p) is that for every k ≥ 1, X(n,p) has not one but two phase transitions for kth homology, one where homology appears and one where it vanishes. In particular, higher homology is not monotone with respect to p. However, there are still comparisons to Yd(n,p)the appearance of homology Hk(X) is analogous to the birth of top homology Hd(Y ). Similarly, the vanishing threshold for Hk(X(n,p)) is analogous to vanishing of Hd−1(Y ).

TABLE 23.1.4 Topological thresholds for X(n,p)

|PROPERTY<br><br>|THRESHOLD|SHARP|TIGHT<br><br>|SOURCE|
|---|---|---|---|---|
|π1(X) = 0<br><br>Hk(X, R) = 0 Xk is pure k-dimensional<br><br>Hk(Y, R) = 0<br><br><br>|p = 1/n1/3 p = c/n1/k<br><br>p = (k/2+1)n log n<br><br>1/(k+1)<br><br>p = (k/2+1)n log n<br><br>1/(k+1)|?<br><br>one-sided<br><br>yes yes<br><br>|no c.f.<br><br>yes yes<br><br>|[Kah09, Bab12, CFH15] [Kah09] [Kah09] [Kah14a]<br><br>|


#### The multi-parameter model

There is a natural multi-parameter model which generalizes all of the models discussed so far. For every every i = 1,2,... let pi : N → [0,1]. Then deﬁne the multiparameter random complex X(n;p1,p2,...) as follows. Start with n vertices. Insert every edge with probability p1. Conditioned on the presence of all three boundary edges, insert a 2-face with probability p2, etc.

The random d-complex Yd(n,p) with complete (d − 1)-skeleton is equivalent to the case p1 = p2 = ··· = pd−1 = 1, p = pd, and pd+1 = pd+2 = ··· = 0. The random clique complex X(n,p) corresponds to p2 = p3 = ··· = 1, and p = p1. This multi-parameter model is ﬁrst studied by Costa and Farber in [CF14].

#### 23.1.2 RANDOM GEOMETRIC MODELS

The random geometric graph G(n,r) is a ﬂexible model, deﬁned as follows. Consider a probability distribution on Rd with a bounded, measurable, density function f : Rd → R. Then one chooses n points independently and identically distributed (i.i.d.) according to this distribution. The n points are the vertices of the graph, and two vertices are adjacent if they are within distance r. Usually r = r(n) and n → ∞. The standard reference for random geometric graphs is Penrose’s monograph [Pen03].

There are at least two commonly studied ways to build a simplicial complex on a geometric graph. The ﬁrst is the Vietoris–Rips complex, which is the same construction as the clique complex above—one ﬁlls in all possible faces, i.e. the faces of the Vietoris–Rips complex correspond to the cliques of the graph. The second is the Cechˇ complex, where one considers the higher intersections of the balls of radius r/2. This leads to two natural models for random geometric complexes V R(n,r) and C(n,r).

- TABLE 23.1.5 Topological thresholds for C(n,r)

|PROPERTY|THRESHOLD<br><br>|SHARP<br><br>|TIGHT|SOURCE|
|---|---|---|---|---|
|Hk(X) = 0<br><br>Hk(Y ) = 0<br><br><br>|nrd = n−(k+2)/(k+1) nrd = log n + θ(log log n)<br><br>|coarse sharp|yes essentially<br><br>|[Kah11] [BW15]|


- TABLE 23.1.6 Topological thresholds for V R(n,r)


|PROPERTY<br><br>|THRESHOLD|SHARP<br><br>|TIGHT<br><br>|SOURCE|
|---|---|---|---|---|
|Hk(X) = 0<br><br>Hk(Y ) = 0<br><br><br>|nrd = n−(2k+2)/(2k+1) nrd = θ(log n)|coarse<br><br>sharp<br><br>|yes c.f.|[Kah11] [Kah11]<br><br>|


### 23.2 HIGH DIMENSIONAL EXPANDERS

#### GLOSSARY

Cheeger number: The normalized Cheeger number of a graph h(G) with vertex

set V is deﬁned by

#E(A,A¯) min{volA,volA¯}

,

h(G) = min

∅ A V

where

volA =

deg(v)

v∈A

and A¯ is the complement of A in V .

Laplacian: For a connected graph H, the normalized graph Laplacian L = L[H]

is deﬁned by

L = I − D−1/2AD−1/2.

Here A is the adjacency matrix, and D is the diagonal matrix with vertex degrees along the diagonal.

Spectral gap: The eigenvalues of the normalized graph Laplacian of a connected

graph satisfy

0 = λ1 < λ2 ≤ ··· ≤ λn ≤ 2.

The smallest positive eigenvalue λ2[H] is of particular importance, and is sometimes called the spectral gap of H.

Expander family: Let {Gi} be an inﬁnite sequence of graphs where the number

of vertices tends to inﬁnity. We say that {Gi} is an expander family if liminf λ2[Gi] > 0.

Expander graphs are of fundamental importance for their applications in computer science and mathematics [HLW06]. It is natural to seek their various higherdimensional generalizations. See [Lub14] for a survey of recent progress on higherdimensional expanders, particularly Ramanujan complexes which generalize Ramanujan graphs.

Gromov suggested that one property that higher-dimensional expanders should have is geometric or topological overlap. A sequence of d-dimensional simplicial complexes ∆1, ∆2, ..., is said to have the geometric overlap property if for every geometric map (aﬃne-linear on each face) f : ∆i → Rd, there exists a point p ∈ Rd such that f−1(p) intersects the interior of a constant fraction of the d-dimensional faces. The sequence is said to have the stronger topological overlap property if this holds even for continuous maps.

One way to deﬁne higher-dimensional expander is via coboundary expansion, which generalizes the Cheeger number of a graph. Following Linial and Meshulam’s coisoperimetric ideas, Dotterrer and Kahle [DK12] pointed out that d-dimensional random simplicial complexes are coboundary expanders. By a theorem of Gromov [Gro09, Gro10] (see the note [DKW15] for a self contained proof of Gromov’s theorem), this implies that random complexes have the topological overlap property.

Lubotzky and Meshulam introduced a new model of random 2-complex, based on random Latin squares, in [LM15]. The main result is the existence of coboundary expanders with bounded edge-degree, answering a question asked implicitly in [Gro10] and explicitly in [DK12].

Another way to deﬁne higher-dimensional expanders is via spectral gap of various Laplacian operators. Hoﬀman, Kahle, and Paquette studied spectral gap of random graphs [HKP12], and applied Garland’s method to prove homology-vanishing theorems. Gundert and Wagner extened this to study higher-order spectral gaps of these complexes [GW15]. Parzanchevski, Rosenthal, and Tessler showed that this implies the geometric overlap property [PRT15].

### 23.3 PHASE TRANSITIONS

There has been a lot of interest in identifying thresholds for various topological properties, such as vanishing of homology. As some parameter varies, the topology passes a phase transition where some property suddenly emerges. In this section we review a few of the most well-studied topological phase transitions.

#### 23.3.1 HOMOLOGY-VANISHING THEOREMS

The following theorem describing the connectivity threshold for the random graph G(n,p) is the archetypal homology-vanishing theorem.

THEOREM 23.3.1 Erd˝os–R´enyi theorem [ER59] If

log n + ω(1) n

p ≥

- then w.h.p. G(n,p) is connected, and if

p ≤

log n − ω(1) n

- then w.h.p. G(n,p) is disconnected. Here ω(1) is any function so that ω(1) → ∞ as n → ∞.

We say that it is a homology-vanishing theorem because path connectivity of a topological space X is equivalent to H0(X,G) = 0 with any coeﬃcient group G.

It is also a cohomology-vanishing theorem, since H0(X,G) = 0 is also equivalent to path-connectivity. In many ways it is better to think of it as a cohomology theorem, since the standard proof, for example in Chapter 10 of [Bol01], is really a cohomological one. This perspective helps when understanding the proof of the Linial–Meshulam theorem.

The following cohomological analogue of the Erd˝s–Re´nyi theorem was the ﬁrst nontrivial result for the topology of random simplicial complexes.

THEOREM 23.3.2 Linial–Meshulam theorem [LM06] Let Y = Y (n,p). If

p ≥

2log n + ω(1) n

- then w.h.p. H1(Y,Z/2Z) = 0, and if


p ≤

2log n − ω(1) n

- then w.h.p. H1(Y,Z/2Z) = 0.


One of the main tools introduced in [LM06] is a new co-isoperimetric inequality for the simplex, which was discovered independently by Gromov. These coisoperimetric inequalities were combined by Linial and Meshulam with intricate cocycle-counting combinatorics to get a sharp threshold.

See [DKW15] for a comparison of various deﬁnitions co-isoperimetry, and a clean statement and self-contained proof of Gromov’s theorem.

Theorem 23.3.2 was generalized further by Meshulam and Wallach. THEOREM 23.3.3 [MW09]

Fix d ≥ 1, and let Y = Yd(n,p). Let G be any ﬁnite abelian group. If

dlog n + ω(1) n then w.h.p. Hd−1(Y,G) = 0, and if

p ≥

dlog n − ω(1) n then w.h.p. Hd−1(Y,G) = 0.

p ≤

Theorem 23.3.3 generalizes Theorem 23.3.2 in two ways: by letting the dimension d ≥ 2 be arbitrary, and also by letting coeﬃcients be in an arbitrary ﬁnite abelian group G.

#### Spectral gaps and Garland’s method

There is another approach to homology-vanishing theorems for simplicial complexes, via Garland’s method [Gar73]. The following reﬁnement of Garland’s theorem is due to Ballman and Swiatkowski.´

#### THEOREM 23.3.4 [Gar73, BS97]´

If ∆ is a ﬁnite, pure d-dimensional, simplicial complex, such that

1 d

λ2[lk∆(σ)] > 1 −

for every (d − 2)-dimensional face σ ∈ ∆, then Hd−1(∆,R) = 0.

This leads to a new proof of Theorem 23.3.3, at least over a ﬁeld of characteristic zero.

#### THEOREM 23.3.5 [HKP12]

- Fix d ≥ 1, and let Y = Yd(n,p). If


dlog n + ω(1) n then w.h.p. Hd−1(Y,R) = 0, and if

p ≥

dlog n − ω(1) n

p ≤

then w.h.p. Hd−1(Y,R) = 0. Here ω(1) is any function that tends to inﬁnity as n → ∞.

This is slightly weaker than the Meshulam–Wallach theorem topologically speak-

ing, since Hi(Y,G) = 0 for any ﬁnite group G implies that Hi(Y,R) = 0 by the universal coeﬃcient theorem, but generally the converse is false. However, the

proof via Garland’s method avoids some of the combinatorial complications of cocycle counting.

Garland’s method also provides proofs of theorems which have so far eluded other methods. For example, we have the following homology-vanishing threshold in the random clique complex model. Note that k = 0 again corresponds to the Erd˝s–R´enyi theorem.

THEOREM 23.3.6 [Kah14a] Fix k ≥ 1 and let X = X(n,p). Let ω(1) denote a function that tends to ∞ arbitrarily slowly. If

p ≥

k 2 + 1 log n + k2 log log n + ω(1)

n

1/(k+1)

then w.h.p. Hk(X,R) = 0, and if 1 nk ≤ p ≤

k 2 + 1 log n + k2 log log n − ω(1)

n

1/(k+1)

then w.h.p. Hk(X,R) = 0.

It may be that this theorem holds with R coeﬃcients replaced by a ﬁnite group G or even with Z, but for the most part this remains an open problem. The only other case that seems to be known is the case k = 1 and G = Z/2 by DeMarco, Hamm, and Kahn [DHK13], where a similarly sharp threshold is obtained.

The applications of Garland’s method depends on new results on the spectral gap of random graphs.

#### THEOREM 23.3.7 [HKP12]

Fix k ≥ 0. Let λ1,λ2,... denote the eigenvalues of the normalized graph Laplacian of the random graph G(n,p). If

(k + 1)log n + ω(1) n then

p ≥

C np ≤ λ2 ≤ ··· ≤ λn ≤ 1 +

1 −

C np

with probability at least 1 − o n−k . Here C > 0 is a universal constant.

Theorem 23.3.6, combined with some earlier results [Kah09], has the following corollary.

THEOREM 23.3.8 [Kah14a] Let k ≥ 3 and > 0 be ﬁxed. If

(Ck + )log n n

1/k

1 n1/(k+1)+

≤ p ≤

,

where C3 = 3 and Ck = k/2 + 1 for k > 3, then w.h.p. X is rationally homotopy equivalent to a bouquet of k-dimensional spheres.

The main remaining conjecture for the topology of random clique complexes is that these rational homotopy equivalences are actually homotopy equivalences.

CONJECTURE 23.3.9 The bouquet-of-spheres conjecture.

Let k ≥ 3 and > 0 be ﬁxed. If

n− n1/(k+1)

n n1/k ≤ p ≤

then w.h.p. X is homotopy equivalent to a bouquet of k-spheres.

Given earlier results, this is equivalent to showing that Hk(X,Z) is torsion free. So far, integer homology for X(n,p) is not very well understood. Some progress has been made for Yd(n,p), described in the following.

#### Integer homology

Unfortunately, neither method discussed above (the cocycle-counting methods pioneered by Linial and Meshulam or the spectral methods of Garland), seems to handle integral homology. There is a slight subtlety here—if one knows for some simplicial complex Σ that Hi(Σ,G) = 0 for every ﬁnite abelian group G then Hi(Σ,Z) = 0 by the universal coeﬃcient theorem. See, for example, Chapter 2 of Hatcher [Hat02].

So it might seem that the Theorem 23.3.3 will also handle Z coeﬃcients, but the proof uses cocycle counting methods which require G to be ﬁxed, or at least for the order of the coeﬃcient group |G| to be growing suﬃciently slowly. Cocycle counting does not seem to work, for example, when |G| is growing exponentially fast. The following gives an upper bound on the vanishing threshold for integer homology.

#### THEOREM 23.3.10 [HKP12]

- Fix d ≥ 2, and let Y = Yd(n,p). If


p ≥

80dlog n n

,

then w.h.p. Hd−1(Y,Z) = 0.

The author suspects that the true threshold for homology with Z coeﬃcients is the same as for ﬁeld coeﬃcients: dlog n/n.

CONJECTURE 23.3.11 A sharp threshold for Z homology. If

dlog n + ω(1) n then w.h.p. Hd−1(Y,Z) = 0, and if

p ≥

dlog n − ω(1) n then w.h.p. Hd−1(Y,Z) = 0.

p ≤

#### 23.3.2 THE BIRTH OF CYCLES AND COLLAPSIBILITY

G(n,p) in the p = 1/n regime

There is a remarkable phase transition in structure of the random graph G(n,p) at the threshold p = 1/n. A “giant” component, on a constant fraction of the vertices, suddenly emerges. This is considered an analogue of percolation on an inﬁnite lattice, where an inﬁnite component appears with probability 1.

#### THEOREM 23.3.12 [ER59]

Let p = c/n for some c > 0 ﬁxed, and G = G(n,p).

- • If c < 1 then w.h.p. all components are of order O(log n).
- • If c > 1 then w.h.p. there is a unique giant component, of order Ω(n).


An overview of this remarkable phase transition can be found in Chapter 11 of Alon and Spencer [AS08].

In random graphs, the appearance of cycles with high probability has the same threshold 1/n.

#### THEOREM 23.3.13 [Pit88]

Suppose p = c/n where c > 0 is constant.

- • If c ≥ 1 then w.h.p. G contains at least one cycle, i.e. P[H1(G) = 0] → 1.
- • If c < 1 then


√1 − c exp(c/2 + c2/4). The analogy in higher dimensions is only just beginning to be understood.

P[H1(G) = 0] →

#### The birth of cycles

Kozlov ﬁrst studied the vanishing threshold for top homology in [Koz10].

#### THEOREM 23.3.14 [Koz10]

Let Y = Yd(n,p), and G be any abelian group.

- (1) If p = o(1/n) then w.h.p. Hd(Y,G) = 0.
- (2) If p = ω(1/n) then w.h.p. Hd(Y,G) = 0.


Part (1) of this theorem cannot be improved. Indeed, let S be the number of subcomplexes isomorphic to the boundary of a (d + 1)-dimensional simplex. If p = c/n for some constant c > 0, then

E[S] → cd+2/(d + 2)!,

as n → ∞. Moreover, S converges in law to a Poisson distribution with this mean in the limit, so

P[Hd(Y,G) = 0] ≥ P[S = 0] → 1 − exp(−cd+2/(d + 2)!).

In particular, for p = c/n and c > 0, P[Hd(Y,G) = 0] is bounded away from zero.

On the other hand, part (2) can be improved. Indeed straightforward computation shows that if p ≥ c/n and c > d+1 then w.h.p. the number of d-dimensional faces is greater than the number of (d−1)-dimensional faces. Simply by dimensional considerations, we conclude that Hd(Y,G) = 0.

This can improved more though. Aronshtam and Linial found the best possible constant factor c∗d, deﬁned for d ≥ 2 as follows.

Let x ∈ (0,1) be the unique root to the equation

(d + 1)(1 − x) + (1 + dx)log x = 0, and then set

c∗d = −log x

.

(1 − x)d

#### THEOREM 23.3.15 [AL15]

Let Y = Yd(n,p). If p ≥ c/n where c > c∗d, then w.h.p. Hd(Y,G) = 0.

In the other direction, Linial and Peled showed that this result is tight, at least in the case of R coeﬃcients.

#### THEOREM 23.3.16 [LP14]

If p ≤ c/n where c < c∗d then w.h.p. Hd(Y,G) is generated by simplex boundaries. So

P[Hd(Y,R) = 0] → exp(−cd+2/(d + 2)!).

Linial and Peled also showed the birth of a giant (homological) shadow at the same point. This is introduced and deﬁned in [LP14], and it is discussed there as a higher-dimensional analogue of the birth of the giant component in G(n,p).

The threshold for d-collapsibility In a d-dimensional simplicial complex, an elementary collapse is an operation that deletes a pair of faces (σ,τ) such that

- • τ is a d-dimensional face,
- • σ is a d − 1-dimensional face contained in τ, and
- • σ is not contained in any other d-dimensional faces. An elementary collapse results in a homotopy equivalent simplicial complex.


If a simplicial complex can be reduced to a d − 1-dimensional complex by a series of elementary collapses, we say that it is d-collapsible.

For a graph, 1-collapsible is equivalent to being a forest. In other words, a graph G is 1-collapsible if and only if H1(G) = 0. This homological criterion does not hold in higher dimensions. In fact, somewhat surprisingly, d-collapsibility and Hd = 0 have distinct thresholds for random complexes.

Let d ≥ 2 and set gd(x) = (d + 1)(x + 1)e−x + x(1 − e−x)d+1.

Deﬁne cd to be the unique solution x > 0 of gd(x) = d + 1.

THEOREM 23.3.17 [AL LM13, AL16] Let Y = Yd(n,p).

- • If p ≥ c/n where c > cd then w.h.p. Y is not d-collapsible, and
- • if p ≤ c/n where c < cd then Y is d-collapsible with probability bounded away from zero.


So again, this is a one-sided sharp threshold. Regarding collapsibility in the random clique complex model, Malen showed in his PhD thesis that if p n−1/(k+1), then w.h.p. X(n,p) is k-collapsible.

#### Embeddability

Every d-dimensional simplicial complex is embeddable in R2d+1, but not necessarily in R2d. Wagner studied the threshold for non-embeddability of random d-complexes in R2d, and showed the following for Y = Yd(n,p).

#### THEOREM 23.3.18 [Wag11]

There exists constants c1,c2 > 0 depending only on the dimension d such that:

- • if p < c1/n then w.h.p. Y is embeddable in R2d, and
- • if p > c2/n then w.h.p. Y is not embeddable in R2d.


There is a folklore conjecture that a d-dimensional simplicial complex on n vertices embeddable in R2d can have at most O(nd) faces [Dey93, Kal91]. See, for example, the discussion in the expository book chapter [Wag13] or Chapter 24 of this handbook. The d = 1 case is equivalent to showing that a planar graph may only have linearly many edges, which follows immediately from the Euler formula, but the conjecture is open for every d ≥ 2. Theorem 23.3.18 shows that it holds generically.

#### 23.3.3 PHASE TRANSITIONS FOR HOMOLOGY IN RANDOM GEOMETRIC COMPLEXES

Penrose described sharp thresholds for connectivity of random geometric graphs, analogous to the Erd˝s–R´enyi theorem. In the case of a uniform distribution on the unit cube [0,1]d or a standard multivariate distribution, these results are tight [Pen03].

Thresholds for homology in random geometric complexes was ﬁrst studied in [Kah11]. A homology vanishing threshold for random geometric complexes is obtained in [Kah11], which is tight up to a constant factor, but recently a much sharper result was obtained by Bobrowski and Weinberger.

THEOREM 23.3.19 [BW15] Fix 1 ≥ k ≥ d − 1. If

nrd ≥ log n + k log log n + ω(1),

then w.h.p. βk = 0, and if

nrd ≤ log n + (k − 2)log log n − ω(log log log n), then w.h.p. βk → ∞.

- 23.3.4 RANDOM FUNDAMENTAL GROUPS


GLOSSARY

Fundamental group: In a path-connected topological space X, choose an arbitrary base point p. Then the homotopy classes of loops in X based at p, i.e. continuous functions f : [0,1] → X with f(0) = f(1) = p may be endowed with the structure of a group, where the group operation is concatenation of two loops at double speed. This is called the fundamental group π1(X), and up to isomorphism it does not depend on the choice of base point p. If π1(X) = 0 then X is said to be simply connected. The ﬁrst homology group H1(X,Z) is isomorphic to the abelianization of π1(X).

A chain of implications: The following implications hold for an arbitrary sim-

plicial complex X. π1(X) = 0 =⇒ H1(X,Z) = 0 =⇒ H1(X,Z/qZ) = 0 =⇒ H1(X,R) = 0.

Here q is any prime. This is a standard application of the universal coeﬃcient theorem for homology [Hat02].

A partial converse to one of the implications is the following. If H1(X,Z/qZ) = 0 for every prime q, then H1(X,Z) = 0.

Hyperbolic group: A ﬁnitely presented group is said to be word hyperbolic if it can be equipped with a word metric satisfying certain characteristics of hyperbolic geometry [Gro87].

Kazhdan’s property (T): A group G is said to have property (T) if the trivial representation is an isolated point in the unitary dual equipped with the Fell topology. Equivalently, if a representation has almost invariant vectors then it has invariant vectors.

Group cohomology: Associated with a ﬁnitely-presented group G is a contractible CW complex EG on which G acts freely. The quotient BG is the classifying space for principle G bundles. The group cohomology of G is equivalent to the cohomology of BG.

Cohomological dimension: The cohomological dimension of a group G, denoted cdim G, is the largest dimension k such that Hk(G,R) = 0 for some coeﬃcient ring R.

The random fundamental group π1(Y (n,p)) may fruitfully be compared to other models of random group studied earlier, such as Gromov’s density model [Oll05]. The techniques and ﬂavor of the subject owes as much to geometric group theory as to combinatorics.

#### The vanishing threshold and hyperbolicity

Babson, Hoﬀman, and Kahle showed that the vanishing threshold for simple connectivity is much larger than the homology-vanishing threshold.

#### THEOREM 23.3.20 [BHK11]

Let > 0 be ﬁxed and Y = Y (n,p). If

n √n then w.h.p. π1(Y ) = 0, and if

p ≥

n− √n

p ≤

then w.h.p. π1(Y ) is a nontrivial hyperbolic group.

Most of the work in proving Theorem 23.3.20 is showing that, on the sparse side of the threshold, π1 is hyperbolic. This in turn depends on a local-to-global principle for hyperbolicity due to Gromov [Gro87].

Gundert and Wagner showed that it suﬃces to assume that

C √n

p ≥

for some constant C > 0 to show that w.h.p. π1(Y ) = 0 [GW16]. Kor´ndi, Peled, and Sudakov showed that it suﬃces to take C = 1/2 [KPS16].

The author suspects that there is a sharp threshold for simple connectivity at C/√n for some C > 0.

CONJECTURE 23.3.21 A sharp vanishing threshold for π1(Y ). There exists some constant C > 0 such that if

C + √n

p ≥

,

with high probability, π1(Y ) = 0; and if

C − √n

p ≤

,

with high probability, π1(Y ) = 0.

#### Kazhdan’s property (T)

One of the most important properties studied in geometric group theory is property (T). Loosely speaking, a group is (T) if it does not have many unitary representations. Property (T) is also closely related to the study of expander graphs. For a comprehensive overview of the subject, see the monograph [BHV08].

Inspired by Garland’s method, Zuk˙ gave a spectral condition suﬃcient to imply (T). Hoﬀman, Kahle, and Paquette applied Zuk’s˙ condition, together with Theorem 23.3.7 to show that the threshold for π1(Y ) to be (T) coincides with the Linial– Meshulam homology-vanishing threshold.

THEOREM 23.3.22 [HKP12] Let Y = Y (n,p).

- • If

p ≥

2log n + ω(1) n then w.h.p. π1(Y ) is (T), and

- • if


2log n − ω(1) n then w.h.p. π1(Y ) is not (T).

p ≤

#### Cohomological dimension

Costa and Farber [CCFK12] studied the cohomological dimension of the random fundamental group in [CF13]. Their main ﬁndings are that there are regimes when the cohomological dimension is 1, 2, and ∞, before the collapse of the group at p = 1/√n.

THEOREM 23.3.23 [HKP12] Let Y = Y (n,p).

- • If

p

1 n

- then w.h.p. cdim π1(Y ) = 1 [CCFK12].

• If

3 n ≤ p n−3/5

- then w.h.p. cdim π1(Y ) = 2 [CF15a] .


- • if n−3/5 p ≤ n−1/2−


then w.h.p. cdim π1(Y ) = ∞ [CF13]. Here we use f g to mean f = o(g), i.e. lim

f/g = 0.

n→∞

Newman recently reﬁned part of this picture [New16], showing that if p < 2.455/n w.h.p. cdim π1(Y ) = 1, and if p > 2.754/n then w.h.p. cdim π1(Y ) = 2. The precise constants are c2 and c∗2, deﬁned in Section 23.3.2.

#### The fundamental group of the clique complex

Babson showed that p = n−1/3 is the vanishing threshold for π1(X(n,p)) in [Bab12]. An independent and self-contained proof, including more reﬁned results regarding torsion and cohomological dimension, was given by Costa, Farber, and Horak in [CFH15].

#### Finite quotients

Meshulam studied ﬁnite quotients of the random fundamental group, and showed that if they exist then the index must be large—the index must tend to inﬁnity with n. His technique is a version of the cocycle-counting arguments in [LM06] and [MW09], for non-abelian cohomology.

#### THEOREM 23.3.24 Meshulam, [Mes13]

Let c > 0 be ﬁxed. If p ≥ (6+7cn) logn then w.h.p. π1(Y ) has no ﬁnite quotients with index less than nc. Moreover, if H is any ﬁxed ﬁnite group and p ≥ (2+cn) logn then w.h.p. there are no nontrivial maps to H.

#### 23.3.5 PHASE TRANSITIONS IN THE MULTI-PARAMETER MODEL

Applying Garland’s method, Fowler described the homology-vanishing phase transition in the multi-parameter model in [Fow15].

THEOREM 23.3.25 Fowler [Fow15] Let X = X(n,p1,p2,...) with pi = n−α

and αi ≥ 0 for all i. If k

i

k i

αi

< 1,

i=1

then w.h.p. Hk−1(X,Q) = 0. If

and

then w.h.p. Hk−1(X,Q) = 0.

k

αi

i=1

k i ≥ 1

k−1

αi

i=1

k − 1 i

< 1

### 23.4 BETTI NUMBERS AND PERSISTENT HOMOLOGY

- 23.4.1 BETTI NUMBERS


The random clique complex

In the random clique complex X(n,p), it was noted in [Kah09] that if

1/n1/k p 1/n1/(k+1), then

n k + 1

p(k+1

).

E[βk] = (1 − o(1))

2

![image 1](<2016-kahle-random-simplicial-complexes_images/imageFile1.png>)

FIGURE 23.4.1 |E[χ]| plotted in blue, against the Betti numbers of the random ﬂag complex X(n, p). Here

- n = 25 and p varies from 0 to 1. The horizontal axis is the number of edges. Computation and image courtesy of Vidit Nanda.


A more reﬁned estimate may be obtained along the following lines. We have the Euler relation

χ = f0 − f1 + f2 − ··· = β0 − β1 + β2 − ...,

where fi denotes the number of i-dimensional faces. The expected number of idimensional faces is easy to compute—by linearity of expectation we have

E[fi] =

n i + 1

p(i+1

).

2

If we make the simplifying assumption that only one Betti number βi is nonzero, then we have

|χ| = |f0 − f1 + f2 − ...| = βi. So we obtain a plot of all of the Betti numbers by plotting the single function

|χ| = |f0 − f1 + f2 − ...|

n 1 −

n 2

n 3

p1 +

=

p2 −

n 4

p6 + ...

This seems to work well in practice. See for example Figure 23.4.1. It is interesting that even through all of the theorems we have discussed are asymptotic as n → ∞, the above heuristic gives a reasonable prediction of the shape of the Betti number curves, even for n = 25 and p ≤ 0.6.

#### Homological domination in the multi-parameter model

In [CF15b, CF15c], Costa and Farber show that for many choices of parameter (an open, dense subset of the set of allowable vectors of exponents) in the multiparameter model, the homology is dominated in one degree.

#### Random geometric complexes

Betti numbers of random geometric complexes were ﬁrst studied by Robins in [Rob06].

Betti numbers of random geometric complexes are also studied in [Kah11]. Estimates are obtained for the Betti numbers in the subcritical regime nrd → 0. In this regime the Vietoris–Rips complex and Cechˇ complex have small connected components (bounded in size), so all the topology is local.

For the following theorems, we assume that n points are chosen i.i.d. according to a probability measure on Rd with a bounded measurable density function f. So the assumptions on the underlying probability distribution are farily mild.

The following describes the expectation of the Betti numbers of the Vietoris– Rips complex in the subcritical regime. In this regime the homology of V R(n,r) is dominated by subcomplexes combinatorially isomorphic to the boundary of the cross-polytope.

#### THEOREM 23.4.1 [Kah11]

Fix d ≥ 2 and k ≥ 1. If nrd → 0 then E[βk[V R(n,r)]]/ n2k+2rd(2k+1) → Ck, as n → ∞ where Dk is a constant which depends on k,d, and the function f.

The analogous story for the Cechˇ complex is the following. Here the homology is dominated by simplex boundaries.

#### THEOREM 23.4.2 [Kah11]

Fix d ≥ 2 and 1 ≤ k ≤ d − 1. If nrd → 0 then E[βk[C(n,r)]]/ nk+2rd(k+1) → Ck, as n → ∞ where Dk is a constant which depends on k,d, and the function f.

#### In the thermodynamic limit

The thermodynamic limit, or critical regime, is when nrd → C for some constant C > 0. In [Kah11], it is shown that for every 1 ≤ k ≤ d − 1, we have βk = Θ(n). Yogeshwaran, Subag, and Adler obtained the strongest results so far for Betti numbers in the thermodynamic limit, including strong laws of large numbers [YSA15], in particular that βk/n → Ck.

#### Limit theorems

Kahle and Meckes computed variance of the Betti numbers, and proved Poisson and normal limiting distributions for Betti numbers in the subcritical regime r =

- o n−1/d in [KM13].


#### More general point processes

Yogeshwaran and Adler obtained similar results for Betti numbers in a much more general setting of stationary point processes [YA15].

#### 23.4.2 PERSISTENT HOMOLOGY

Bubenik and Kim studied persistent homology for i.i.d. random points on the circle, in the context of a larger discussion about foundations for topological statistics [BK07].

Bobrowski, Kahle, and Skraba studied maximally persistent cycles in V R(n,r) and C(n,r). They deﬁned the persistence of a cycle as p(σ) = d(σ)/b(σ), and found a law of the iterated logarithm for maximal persistence.

THEOREM 23.4.3 [BKS15] Fix d ≥ 2, and 1 ≤ i ≤ d − 1. Choose n points i.i.d. uniformly randomly in the cube [0,1]d. With high probability, the maximally persistent cycle has persistence

max

p(σ) = Θ

σ

log n log log n

1/i

.

##### CONJECTURE 23.4.4 A law of large numbers for persistent homology.

1/i

log n log log n

→ C,

max

p(σ)/

σ

for some constant C = Cd,i.

#### OTHER RESOURCES

For an earlier survey of Erd˝s–R´enyi based models with a focus on the cohomologyvanishing phase transition, see also [Kah14b]. For a more comprehensive overview of random geometric complexes, see [BK14].

Several other models of random topological space have been studied. Ollivier’s survey [Oll05] provides a comprehensive introduction to random groups, especially to Gromov’s density random groups and the triangular model. Dunﬁeld and Thurston introduced a new model of random 3-manifold [DT06] which has been well studied since then.

#### RELATED CHAPTERS

Chapter 22: Topological methods Chapter 24: Embedding and geometric realization

- Chapter 26: Persistent homology
- Chapter 27: High-dimensional topological data analysis


#### REFERENCES

[AKS79] M. Ajtai, J. Koml´os, and E. Szemere´di. Topological complete subgraphs in random graphs. Studia Sci. Math. Hungar., 14:293–297, 1979. [AL16] L. Aronshtam and N. Linial. The threshold for collapsibility in random complexes. Random Structures Algorithms, 48:260–269, 2016

[AL15] L. Aronshtam and N. Linial. When does the top homology of a random simplicial complex vanish? Random Structures Algorithms, 46:26–35, 2015.

[AL LM13] L. Aronshtam, N. Linial, T.  Luczak, and R. Meshulam. Collapsibility and vanishing of top homology in random simplicial complexes. Discrete Comput. Geom., 49:317–334, 2013.

[AS08] N. Alon and J.H. Spencer. The probabilistic method. Wiley-Interscience Series in Discrete Mathematics and Optimization, Wiley, Hoboken, 3rd edition, 2008. [Bab12] E. Babson. Fundamental groups of random clique complexes. Preprint, arXiv:1207. 5028, 2012. [BHV08] B. Bekka, P. de la Harpe, and A. Valette. Kazhdan’s property (T), vol. 11 of New Mathematical Monographs. Cambridge University Press, Cambridge, 2008. [BHK11] E. Babson, C. Hoﬀman, and M. Kahle. The fundamental group of random 2-complexes. J. Amer. Math. Soc., 24:1–28, 2011. [BK07] P. Bubenik and P.T. Kim. A statistical approach to persistent homology. Homology, Homotopy Appl., 9:337–362, 2007.

[BK14] O. Bobrowski and M. Kahle. Topology of random geometric complexes: a survey. In Topology in Statistical Inference, Proc. Symposia in Applied Math., AMS, Providence, to appear. Preprint, arXiv:1409.4734, 2014.

[BKS15] O. Bobrowski, M. Kahle, and P. Skraba. Maximally persistent cycles in random geometric complexes. Preprint, arXiv:1509.04347, 2015. [Bol01] B. Bolloba´s. Random graphs, vol. 73 of Cambridge Studies in Advanced Mathematics.

Cambridge University Press, Cambridge, 2nd edition, 2001. [BS97]´ W. Ballmann and J. Swi´

atkowski. On L2-cohomology and property (T) for automorphism groups of polyhedral cell complexes. Geom. Funct. Anal., 7:615–645, 1997.

‘

[BW15] O. Bobrowski and S. Weinberger. On the vanishing of homology in random Cechˇ complexes. Preprint, arXiv:1507.06945, 2015. [CCFK12] D. Cohen, A. Costa, M. Farber, and T. Kappeler. Topology of random 2-complexes. Discrete Comput. Geom., 47:117–149, 2012.

- [CF13] A. Costa and M. Farber. Geometry and topology of random 2-complexes. Israel J. Math., 209:883–927, 2015.
- [CF14] A. Costa and M. Farber. Random simplicial complexes. Preprint, arXiv:1412.5805, 2014.
- [CF15a] A. Costa and M. Farber. The asphericity of random 2-dimensional complexes. Random Structures Algorithms, 46:261–273, 2015.


- [CF15b] A. Costa and M. Farber. Homological domination in large random simplicial complexes. Preprint, arXiv:1503.03253, 2015.
- [CF15c] A. Costa and M. Farber. Large random simplicial complexes, III; the critical dimension. Preprint, arXiv:1512.08714, 2015.


[CFH15] A. Costa, M. Farber, and D. Horak. Fundamental groups of clique complexes of random graphs. Trans. London Math. Soc., 2:1–32, 2015. [Dey93] T.K. Dey. On counting triangulations in d dimensions. Comput. Geom., 3:315–325, 1993. [DHK13] B. DeMarco, A. Hamm, and J. Kahn. On the triangle space of a random graph. J. Comb., 4:229–249, 2013. [DK12] D. Dotterrer and M. Kahle. Coboundary expanders. J. Topol. Anal., 4:499–514, 2012.

[DKW15] D. Dotterrer, T. Kaufman, and U. Wagner. On expansion and topological overlap. In Proc. 32nd Sympos. Comp. Geom., vol. 51 of LIPIcs, pages 35:1–35:10, Dagstuhl, 2016.

[DT06] N.M. Dunﬁeld and W.P. Thurston. Finite covers of random 3-manifolds. Invent. Math., 166:457–521, 2006.

[ER59] P. Erdo˝s and A. Re´nyi. On random graphs. I. Publ. Math. Debrecen, 6:290–297, 1959. [Fow15] C. Fowler. Generalized random simplicial complexes. Preprint, arXiv:1503.01831,

2015. [Gar73] H. Garland. p-adic curvature and the cohomology of discrete subgroups of p-adic groups. Ann. of Math. (2), 97:375–423, 1973. [Gro87] M. Gromov. Hyperbolic groups. In Essays in group theory, vol. 8 of Math. Sci. Res. Inst. Publ., pages 75–263, Springer, New York, 1987.

- [Gro09] M. Gromov. Singularities, expanders and topology of maps. I. Homology versus volume in the spaces of cycles. Geom. Funct. Anal., 19:743–841, 2009.
- [Gro10] M. Gromov. Singularities, expanders and topology of maps. Part 2: From combinatorics to topology via algebraic isoperimetry. Geom. Funct. Anal., 2:416–526, 2010.


[GW16] A. Gundert and U. Wagner. On topological minors in random simplicial complexes. Proc. Amer. Math. Soc., 144:1815–1828, 2016. [GW15] A. Gundert and U. Wagner. On eigenvalues of random complexes. Israel J. Math, to appear. Preprint, arXiv:1411.4906, 2015. [Hat02] A. Hatcher. Algebraic topology. Cambridge University Press, Cambridge, 2002.

- [HKP12] C. Hoﬀman, M. Kahle, and E. Paquette. Spectral gaps of random graphs and applications to random topology. Preprint, arXiv:1201.0425, 2012.
- [HKP13] C. Hoﬀman, M. Kahle, and E. Paquette. The threshold for integer homology in random d-complexes. Preprint, arXiv:1308.6232, 2013.


[HLW06] S. Hoory, N. Linial, and A. Wigderson. Expander graphs and their applications. Bull. Amer. Math. Soc. (N.S.), 43:439–561, 2006. [J LR00] S. Janson, T  Luczak, and A. Rucinski. Random graphs. Wiley-Interscience Series in Discrete Mathematics and Optimization. Wiley, New York, 2000.

[Kah09] M. Kahle. Topology of random clique complexes. Discrete Math., 309:1658–1671, 2009. [Kah11] M. Kahle. Random geometric complexes. Discrete Comput. Geom., 45:553–573, 2011.

- [Kah14a] M. Kahle. Sharp vanishing thresholds for cohomology of random ﬂag complexes. Ann. of Math. (2), 179:1085–1107, 2014.
- [Kah14b] M. Kahle. Topology of random simplicial complexes: a survey. In Algebraic topology: applications and new directions, vol. 620 of Contemp. Math., pages 201–221, AMS, Providence, 2014.


[Kal91] G. Kalai. The diameter of graphs of convex polytopes and f-vector theory. In Applied geometry and discrete mathematics, vol. 4 of DIMACS Ser. Discrete Math. Theoret. Comput. Sci., pages 387–411, AMS, Providence, 1991.

[KM13] M. Kahle and E. Meckes. Limit theorems for Betti numbers of random simplicial complexes. Homology Homotopy Appl., 15:343–374, 2013. [Koz10] D.N. Kozlov. The threshold function for vanishing of the top homology group of random d-complexes. Proc. Amer. Math. Soc., 138:4517–4527, 2010. [KPS16] D. Kora´ndi, Y. Peled, and B. Sudakov. A random triadic process. SIAM J. Discrete Math., 30:1–19, 2016.

[LM06] N. Linial and R. Meshulam. Homological connectivity of random 2-complexes. Combinatorica, 26:475–487, 2006. [LM15] A. Lubotzky and R.‘Meshulam. Random Latin squares and 2-dimensional expanders. Adv. Math., 272:743–760, 2015. [LP14] N. Linial and Y. Peled. On the phase transition in random simplicial complexes. Ann. of Math., to appear, Preprint, arXiv:1410.1281, 2014. [ LPW94] T.  Luczak, B. Pittel, and J.C. Wierman. The structure of a random graph at the point of the phase transition. Trans. Amer. Math. Soc., 341:721–748, 1994. [Lub14] A. Lubotzky. Ramanujan complexes and high dimensional expanders. Jpn. J. Math., 9:137–169, 2014. [Mes13] R. Meshulam. Bounded quotients of the fundamental group of a random 2-complex. Preprint, arXiv:1308.3769, 2013. [MW09] R. Meshulam and N. Wallach. Homological connectivity of random k-dimensional complexes. Random Structures Algorithms, 34:408–417, 2009. [New16] A. Newman. On freeness of the random fundamental group. Preprint, arXiv:1601. 07520, 2016.

[Oll05] Y. Ollivier. A January 2005 invitation to random groups, vol. 10 of Ensaios Matema´ticos [Mathematical Surveys]. Sociedade Brasileira de Matema´tica, Rio de Janeiro, 2005.

[Pen03] M. Penrose. Random geometric graphs, vol. 5 of Oxford Studies in Probability. Oxford University Press, Oxford, 2003. [Pit88] B. Pittel. A random graph with a subcritical number of edges. Trans. Amer. Math. Soc., 309:51–75, 1988. [PRT15] O. Parzanchevski, R. Rosenthal, and R.J. Tessler. Isoperimetric inequalities in simplicial complexes. Combinatorica, 35:1–33, 2015. [Rob06] V. Robins. Betti number signatures of homogeneous poisson point processes. Physical Review E, 74:061107, 2006. [Wag11] U. Wagner. Minors in random and expanding hypergraphs. In Proc. 27th Sympos. Comput. Geom., pages 351–360, ACM Press, 2011.

[Wag13] U. Wagner. Minors, embeddability, and extremal problems for hypergraphs. In J. Pach, editor, Thirty Essays on Geometric Graph Theory, pages 569–607, Springer, New York, 2013.

[YA15] D. Yogeshwaran and R.J. Adler. On the topology of random complexes built over stationary point processes. Ann. Appl. Probab., 25:3338–3380, 2015. [YSA15] D. Yogeshwaran, E. Subag, and R.J. Adler. Random geometric complexes in the thermodynamic regime. Probab. Theory Related Fields, 1–36, 2015.

