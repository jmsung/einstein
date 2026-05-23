---
type: source
kind: paper
title: Limits of local-global convergent graph sequences
authors: Hamed Hatami, László Lovász, Balázs Szegedy
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1205.4356v2
source_local: ../raw/2012-hatami-limits-local-global-convergent-graph.pdf
topic: general-knowledge
cites:
---

arXiv:1205.4356v2[math.CO]22Aug2013

Limits of locally-globally convergent graph sequences

Hamed Hatami School of Computer Science, McGill University Montreal, Quebec, Canada H3A 0G4∗

La´szlo´ Lova´sz Institute of Mathematics, Eo¨tv¨os Lor´and University Budapest, Hungary H-1117

Bal´zs Szegedy Department of Mathematics, University of Toronto Toronto, Ontario, Canada M5S2E4

December 2012

Abstract

The colored neighborhood metric for sparse graphs was introduced by Bollob´s and Riordan [8]. The corresponding convergence notion reﬁnes a convergence notion introduced by Benjamini and Schramm [6]. We prove that even in this reﬁned sense, the limit of a convergent graph sequence (with uniformly bounded degree) can be represented by a graphing. We study various topics related to this convergence notion such as: Bernoulli graphings, factor of i.i.d. processes and hyperﬁniteness.

![image 1](<2012-hatami-limits-local-global-convergent-graph_images/imageFile1.png>)

∗Research of H.H. was supported by an NSERC and an FQRNT grant. Research of L.L. was supported by ERC Grant No. 227701 and OTKA grant No. CNK 77780. Research of B.Sz. was supported by an NSERC grant.

# Contents

- 1 Introduction 2
- 2 Local-Global convergence of bounded degree graphs 4
- 3 Involution-invariant measures and graphings 5
- 4 Local limits of decorated graphs 7
- 5 A regularization lemma 8
- 6 Proof of the main theorem 9
- 7 Bernoulli graphings and Bernoulli graph sequences 11
- 8 Joins and maximal graphings 15
- 9 Non-standard graphings 17
- 10 Hyperﬁnite graphs and graphings 18
- 11 Graphings as operators and expander graphings 20
- 12 Graphings and local algorithms 21
- 13 Concluding remarks 23


# 1 Introduction

The theory of graph convergence is a recently emerging ﬁeld. It creates a link between combinatorics and analysis similarly as F¨urstenberg’s correspondence principle connects ﬁnite integer sequences with measure preserving systems. Interestingly (or rather unfortunately) there is no uniﬁed theory of graph convergence. Instead there are various convergence notions that work well in diﬀerent situations. For example the theory of dense graph limits [25, 26, 11] works well if the number of edges is quadratic in the number of vertices but it trivializes for sparser graphs. On the other hand the Benjamini–Schramm limit [6] is only deﬁned for graphs which have a linear number of edges in terms of the vertices. In the regime between linear and quadratic the situation is more complicated.

In this paper we focus on the very sparse case were graphs have degrees bounded by some ﬁxed number d (which we consider as ﬁxed throughout). According to Benjamini and Schramm, a graph sequence (Gn)∞n=1 is convergent if the distribution of the isomorphism types of neighborhoods of radius r (when a vertex is chosen uniformly at random in Gn) converges for every ﬁxed r. This notion of convergence is called local convergence, weak convergence or Benjamini–Schramm convergence.

The following example illustrates why a diﬀerent, stronger notion of convergence is needed in some cases. For odd n, let Gn be a d-regular expander graph on n nodes. For even n, let Gn be

the disjoint union of two d-regular expander graphs on n/2 nodes. Assume that the girth of Gn tends to inﬁnity. Then the sequence Gn is locally convergent, but clearly even and odd members of the sequence are quite diﬀerent, and it would be desirable to reﬁne our notion of convergence to distinguish them.

Bollob´s and Riordan [8] introduced such a ﬁner convergence notion (i.e., fewer sequences are convergent). A graph sequence (Gn)∞n=1 is convergent in this sense if for every r,k ∈ N and ε > 0 there is an index l such that if n,m > l, then for every coloring of the vertices of Gn with k colors, there is a coloring of the vertices of Gm with k colors such that the distance between the distributions of colored neighborhoods of radius r in Gn and Gm is at most ε. This is equivalent to saying that Gn and Gm are close in the colored neighborhood metric introduced in [8]. This ﬁner notion of convergence is sensitive to both local and global properties of the graphs whereas the Benjamini–Schramm convergence is only sensitive to local properties. For this reason we call this notion local-global convergence.

Benjamini and Schramm described a limit object for locally convergent sequences in the form of an involution-invariant distribution on rooted countable graphs with bounded degree. One can also describe this limit object as a graphing (Aldous and Lyons [1], Elek [14]), which is a bounded degree graph on a Borel probability space such that the edge set is Borel measurable and it satisﬁes a certain measure preservation property. (We will give a precise deﬁnition below.) Neighborhood statistics in graphings can be deﬁned by using the probability space structure on the vertex set. Every involution-invariant distribution can be represented by a graphing. We note that graphings are common generalizations of bounded degree graphs and measure preserving systems and so they are also interesting from an ergodic theoretic point of view.

However, the graphing representing the limit object of a locally convergent graph sequence is not unique: diﬀerent graphings can describe the same involution-invariant distribution. In other words, a graphing contains more information than just the limiting neighborhood distribution. This suggests that graphings can be used to represent limit objects for more reﬁned convergence notions. Indeed, in the present paper we show that the limit of a local-global convergent sequence can also be represented by a graphing in the sense that the graphs in the sequence converge to the graphing in the colored neighborhood metric. This means that for every local-global convergent sequence we produce a graphing which contains both local and global information about the graphs.

We highlight the importance of a special family of graphings called Bernoulli graphings. We show that with given local statistics, the Bernoulli graphings contain the least global information. This means that the global properties of a Bernoulli graphing can be modeled with an arbitrary precision on any other graphing with the same local statistics. For a graph G, being close to a Bernoulli graphing in the local-global sense means that the local statistics of any coloring on G can be modeled by a randomized process called local algorithm or factor of i.i.d. process.

Roughly speaking, a hyperﬁnite graph sequence is a bounded degree sequence whose members can be cut into small connected components removing a small set of vertices (or equivalently edges). We prove that a locally convergent hyperﬁnite sequence is locally-globally convergent, and its limit is a Bernoulli graphing. (This was proved independently by Elek [16]). It is an interesting question how to construct a non-hyperﬁnite sequence converging to a Bernoulli graphing.

# 2 Local-Global convergence of bounded degree graphs

A rooted graph is a pair (G,o) where o is a vertex of a graph G. The radius of a rooted graph is the distance of the farthest vertex in G to o. We denote by Ur the set of all rooted graphs with radius at most r (and all degrees bounded by d). For an integer r ≥ 0, and a vertex v in a graph G, let NG,r(v) denote the subgraph of G rooted at v and induced by the vertices that are at a distance at most r from v. Two rooted graphs (G,o) and (G′,o′) are said to be isomorphic if there is an isomorphism from G to G′ that maps o to o′.

Given a ﬁnite graph G and a radius r ≥ 0, we can choose a node v ∈ V (G) uniformly and randomly, and consider the distribution of NG,r(v). Let PG,r denote this probability measure on Ur. We say that a sequence (Gn) of ﬁnite graphs is locally convergent (or Benjamini–Schramm convergent) if PG

n,r converges to a limit distribution as n → ∞, for every ﬁxed r ≥ 0. Denote the set of probability measures on a Borel space X by M(X). Note that since Ur is ﬁnite, all the usual distances on M(Ur) are topologically equivalent. We shall usually work with the total variation distance dvar, deﬁned (in general, for a space X) by

|µ(A) − ν(A)|

dvar(µ,ν) = sup A⊆X

where A runs through the Borel measurable sets.

To deﬁne our reﬁnement of local convergence, we consider vertex colorings. For a ﬁnite graph G, let K(k,G) denote the set of all vertex colorings with k colors. Fix integers k and r, and let Ur,k be the set of all triples (H,o,c) where (H,o) is a rooted graph of radius at most r and c is an arbitrary k-coloring of V (H). Consider a ﬁnite graph G together with a c ∈ K(k,G). Pick a random vertex v from G. Then the restriction of the k-coloring to NG,r(v) is an element in Ur,k, and thus for the graph G, every c ∈ K(k,G) introduces a probability distribution on Ur,k which we denote by PG,r[c]. Sometimes we refer to the probability distributions PG,r[c] (for r ≥ 0) as local statistics of the coloring c. Let

QG,r,k := PG,r[c] : c ∈ K(k,G) ⊆ M(Ur,k). These sets are similar to “quotient sets” introduced in [12] for dense graphs, except that there only edges with the given coloring were counted, while here we consider the colors on larger neighborhoods. Notice that the sets QG,r,k are ﬁnite, and they are subsets of the ﬁnite dimensional space RU

r,k

that is independent of the graph G.

- Deﬁnition 2.1 A sequence of ﬁnite graphs (Gn)∞n=1 with all degrees at most d is called locally-


n,r,k)∞n=1 converges in the Hausdorﬀ distance inside the compact metric space (M(Ur,k),dvar).

globally convergent if for every r,k ≥ 1, the sequence (QG

In other words, if i and j are large enough, then for every k-coloring ci of V (Gi) there is a k-coloring cj of V (Gj) so that the distributions of colored r-neighborhoods of (Gi,ci) and (Gj,cj) are almost the same.

Since compact subsets of a compact metric space form a compact space with respect to the Hausdorﬀ metric, it follows that every inﬁnite sequence of ﬁnite graphs contains a locally-globally convergent subsequence.

Fixing k = 1 in Deﬁnition 2.1, we recover a metric deﬁnition of Benjamini–Schramm convergence. It is easy to construct examples of graph sequences which are convergent in Benjamini–Schramm sense, but not locally-globally. However we do not know whether k = 2 would give a convergence notion equivalent to local-global convergence.

It is natural to ask if we obtain a diﬀerent convergence notion if we replace vertex colorings by edge colorings or other locally deﬁned extra structures. It turns out that all local structures can be encoded by vertex colorings, and thus they do not lead to diﬀerent convergence notions. As an example, we show how to encode edge colorings by vertex colorings.

Let G be a graph with all degrees at most d and let c : E(G) → [k] be an edge coloring of G. It is easy to see that there exists an edge coloring c1 : E(G) → [30d3k] such that c1(e) ≡ c(e) modulo k for every e ∈ E(G), and if c1(e1) = c1(e2) holds, then the edges e1 and e2 are of distance at least

- 3 in the edge graph of G. It is clear that c1 encodes the coloring c in the sense that local statistics of c1 modulo k give the local statistics of c. Let S denote the set of subsets of [30d3k] of size at most d. We deﬁne the vertex coloring c2 : V (G) → S by setting c2(v) to be the set of c1-colors of the edges incident to v. Now it is easy to see that c2 encodes the coloring c1 in the following way. If e = (v,w) is an edge in G, then {c1(e)} is the intersection of the sets c2(v) and c2(w).


# 3 Involution-invariant measures and graphings

Benjamini and Schramm [6] associated a limit object with every locally convergent graph sequence as follows. Let G denote the set of (isomorphism classes of) rooted, connected (possibly inﬁnite) graphs with all degrees at most d. For a rooted graph (B,o) with radius r, we denote by G(B,o) the set of all rooted graphs (G,o) such that NG,r(o) ∼= (B,o). For a rooted graph (G,o), we deﬁne a neighborhood basis at (G,o) as G(NG,r(o)). These neighborhoods deﬁne a topology on G. It is easy to see that this is a compact separable space.

The Benjamini–Schramm limit of the locally convergent graph sequence (Gn)∞n=1 is a probability measure ν on the Borel sets of G, such that

n,r(B,o) = ν(G(B,o)) for every r ≥ 1 and every rooted graph (B,o) of radius r.

lim

PG

n→∞

Not every probability measure on G arises as the limit of a convergent graph sequence. One property that all limits have is called involution invariance or unimodularity. To deﬁne this, let G˜ denote the space of graphs in G with a distinguished edge incident to the root. Let α : G˜ → G˜ denote the continuous transformation that moves the root to the other endpoint of the distinguished edge. For every probability measure µ on G, deﬁne µ∗ to be the unique probability measure on G such that dµ∗/dµ(G) is proportional to the degree of the root in G. Deﬁne the probability measure µ˜ on G˜ by ﬁrst picking a µ∗-random graph, and then distinguishing a random edge incident to the root. The measure µ is called involution-invariant if µ˜ is invariant under α. Involution-invariant measures on G form a closed set in the weak topology.

Let G be a ﬁnite graph, and let the probability measure ν on the Borel sets of G be deﬁned as ν(G(B,o)) = PG,r(B,o) for every r ≥ 1 and every rooted graph (B,o) of radius r. It is easy to see

that ν is involution-invariant. It follows that every measure on G that is the limit of ﬁnite graphs is involution-invariant. Aldous and Lyons [1] conjectured that all involution-invariant measures arise as graph limits. The Aldous-Lyons conjecture is considered to be one of the most important open problems in this area.

In the dense setting, the set of the symmetric measurable maps w : [0,1]2 → [0,1] were used to generalize the concept of graphs and describe graph limits [25]. For local-global convergence (Deﬁnition 2.1), graphings serve this purpose.

- Deﬁnition 3.1 Let X be a Polish topological space and let ν be a probability measure on the Borel sets in X. A graphing is a graph G on V (G) = X with Borel measurable edge set E(G) ⊂ X × X in which all degrees are at most d and


e(x,B)dν(x) =

A

e(x,A)dν(x) (1)

B

for all measurable sets A,B ⊆ X, where e(x,S) is the number of edges from x ∈ X to S ⊆ X.

Note that every ﬁnite graph G is a graphing where X = V (G) and νG is the uniform distribution on V (G).

If (1) holds, then η∗(A×B) = A e(x,B)dν(x) deﬁnes a measure on the Borel sets of X×X. This measure is concentrated on E(G), symmetric in the two coordinates, and its marginal ν∗ satisﬁes (dν∗/dν)(x) = deg(x). Normalizing by d0 = X deg(x)dx, we get a probability distribution η on the set of edges. We can generate a random edge from η by selecting a random point v from ν∗ and selecting uniformly a random edge incident with v. Conversely, if G is a Borel graph and we have a measure η∗ on X × X that is concentrated on E(G), so that η∗(A × B) = A e(x,B)dν(x), then (1) follows by Fubini’s theorem, and so G is a graphing.

Let G be a graphing (of degree at most d) on the probability space (X,ν). Then it induces a measure µG on G: pick a random element x ∈ X and take its connected component Gx rooted at x. It is easy to see that µG is an involution-invariant measure. (In fact, (1) just expresses this property.)

Let G be a graphing as in Deﬁnition 3.1. A vertex coloring of G with k colors is a measurable function c : X → [k]. The set of all such colorings will be denoted by K(k,G). We deﬁne PG,r[c] and QG,r,k in a similar way as in a ﬁnite graph. (Notice that it makes sense to talk about a random vertex in G.) The set QG,r,k is a subset of the ﬁnite dimensional space RU

r,k

, but in general it might be inﬁnite and not necessarily closed; we will often use its closure QG,r,k (see Question 9.1).

![image 2](<2012-hatami-limits-local-global-convergent-graph_images/imageFile2.png>)

Now we are ready to state our main theorem.

Theorem 3.2 Let (Gi)∞i=1 be a local-global convergent sequence of ﬁnite graphs with all degrees at most d. Then there exists a graphing G such that QG

n,r,k → QG,r,k (n → ∞) in Hausdorﬀ distance for every r and k.

To what degree is the limit object determined? This question leads to diﬀerent notions of “isomorphism” between graphings.

- Deﬁnition 3.3 Let (G1,X1,ν1) and (G2,X2,ν2) be graphings.


- • They are called locally equivalent if for every r ∈ N, the distribution of NG

1,r(x1) is the same as the distribution of NG

2,r(x2) for random x1 ∈ X1 and x2 ∈ X2.

- • They are called locally-globally equivalent if QG


![image 3](<2012-hatami-limits-local-global-convergent-graph_images/imageFile3.png>)

![image 4](<2012-hatami-limits-local-global-convergent-graph_images/imageFile4.png>)

2,r,k for every r,k ∈ N.

1,r,k = QG

Local equivalence of two graphings means that they induce the same involution-invariant measure on G. Local-global equivalence implies local equivalence by setting k = 1.

- Deﬁnition 3.4 (Local-global partial order) Assume that G1 and G2 are two graphings of max-


![image 5](<2012-hatami-limits-local-global-convergent-graph_images/imageFile5.png>)

![image 6](<2012-hatami-limits-local-global-convergent-graph_images/imageFile6.png>)

imal degree at most d. We say that G1 ≺ G2 if QG

2,r,k for every r,k ≥ 1. In particular, G1 and G2 are locally-globally equivalent if and only if both G1 ≺ G2 and G2 ≺ G1 hold.

1,r,k ⊆ QG

In the setting of group actions, this partial order means the same as “weak containment” of the corresponding group actions, and local-global equivalence corresponds to “weak equivalence” (Kechris [21]).

Recall that a measurable map φ : (X,µ) → (Y,ν) is called measure-preserving if µ(φ−1(A)) = ν(A) for every measurable set A ⊆ Y . An easy way to prove a relation G1 ≺ G2 between two graphings is the following. We call a measure preserving map φ : V (G1) → V (G2) a local isomorphism if restricted to any connected component of G1, we get an isomorphism with a connected component of G2. Clearly local isomorphisms can be combined. However, a local isomorphism may not be invertible! It is easy to see that the existence of a local isomorphism G1 → G2 implies that G1 and G2 are locally equivalent, and G2 ≺ G1.

Example 3.5 Let G be a ﬁnite connected graph, and G ∪ G denote the disjoint union of G with itself. The function φ : V (G ∪ G) → V (G) that maps both copies of G in G ∪ G isomorphically to G is a (non-invertible) local isomorphism. Consequently G ∪ G and G are locally equivalent, and G ≺ G ∪ G. However, G and G ∪ G are not locally-globally equivalent.

We shall study the local-global equivalence and the local-global partial order in Sections 7 and

8. In particular, we will show that among all graphings in a local equivalence class, there is always a smallest one and a largest one in this partial order.

# 4 Local limits of decorated graphs

In this section we extend the formalism behind the Benjamini–Schramm limits for the case when vertices are decorated by elements from a compact space. Let C be a second countable compact Hausdorﬀ space. Let G(C) denote the space of (isomorphism classes of) rooted, connected (countable) graphs with all degrees at most d such that the vertices are decorated by elements from C. So the points of G(C) are triples (G,o,c), where G is a connected countable graph, o ∈ V (G), and c : V (G) → C. If C is the trivial (one point) compact space, then G(C) can be identiﬁed with the space G deﬁned earlier. Two important special cases for us will be when C = [0,1] (assigning [0,1]weights to vertices), and C = [k] (coloring vertices by k colors). With a slight abuse of notation, these will be denoted by G[0,1] and G[k].

We put a compact topology on G(C) by specifying a basis of it. Let r be an arbitrary natural number and (H,o) be a ﬁnite rooted graph of radius r. Assume furthermore that every vertex v of (H,o) is decorated by an open set Uv in C. Let S be the collection of all (G,o,c) ∈ G(C) where the neighborhood NG,r(o) is isomorphic to (H,o), and furthermore there is an isomorphism α : NG,r(o) → (H,o) such that c(v) ∈ Uα(v) for every v ∈ NG,r(o). It is easy to see that G(C) with this topology is a compact, second countable, Hausdorﬀ space. As a consequence, probability measures on G(C) form a compact space in the weak topology.

Let G be a ﬁnite graph with all degrees at most d in which the vertices are C-labeled. We can construct a probability measure µG on G(C) by putting a root o on a randomly chosen vertex v ∈ V (G) and keeping only the connected component of the root. A sequence (Gn)∞n=1 of C-labeled graphs is called locally convergent if the corresponding measures {µG

}∞n=1 converge in the weak topology to some measure µ. The measure µ is the limit object of the sequence.

n

We deﬁne involution-invariance completely analogously to the undecorated case, simply replacing G by G(C) everywhere. Involution-invariant measures on G(C) form a closed set in the weak topology. It follows that if µ is a measure on G(C) that is the limit of ﬁnite C-decorated graphs, then it is involution-invariant.

A C-decorated graphing is a graphing G together with a Borel function c : V (G) → C. Similarly

- as in the undecorated case, every C-decorated graphing deﬁnes an involution-invariant distribution. The measure µG,c on G(C) is created by picking a random element x ∈ V (G), and taking its connected component Gx rooted at x together with the vertex labels given by the restriction of c to V (Gx). It is easy to see that µG,c is an involution-invariant measure.


Remark 4.1 We can deﬁne a Borel graph on G(C). The edge set E(C) of this graph consists of pairs ((G,o1,c),(G,o2,c)) ∈ G(C) × G(C) such that (o1,o2) is an edge in G. Note that loop edges can arise in this graph. For example if there is an automorphism of (G,c) which takes o1 to its neighbor o2, then (G,o1,c) is identiﬁed with (G,o2,c) in G(C). In general it is not true that every involution-invariant measure ν on G(C) turns this graph into a graphing. This is due to the problem with automorphisms which also lead to loops. However it is not hard to show that if for an involution-invariant measure ν, with probability one, a ν-random connected component has no automorphisms, then we get a graphing (G(C),ν,E(C)). One important role of appropriate decorations is to break symmetries, and make this graph a graphing.

# 5 A regularization lemma

The following lemma is the main ingredient in proving Theorem 3.2. It serves as a “regularity lemma” in our framework for bounded degree graphs.

- Lemma 5.1 (Regularization) For positive integers r,k and real number ε > 0, there exists an integer tr,k,ε such that the following holds. For every graph G with all degrees at most d, there exists a tr,k,ε-vertex coloring q of G which satisﬁes the following conditions.


- • If q(v) = q(w), then either v = w or the distance of v and w in G is at least r + 1;


- • For every g ∈ K(k,G), there exists α : [tr,k,ε] → [k] such that dvar(PG,r[g],PG,r[α ◦ q]) ≤ ε.


Proof. The space M(Ur,k) is a bounded dimensional compact set with the topology generated by dvar. Let N be an ε/2-net in M(Ur,k) in dvar. Let NG be the subset of points in N that are at most ε/2 far from a point of the form PG,r[g] for some g ∈ K(k,G). For each a ∈ NG, we choose a representative xa = PG,r[ga] such that dvar(a,xa) ≤ ε/2. It is clear that for every g ∈ K(k,G), there is a point xa such that dvar(PG,r[g],xa) ≤ ε. Let f be the common reﬁnement of all the partitions {ga}a∈N

. Clearly f has a bounded number of partition sets in terms of r,k,ε and d and it satisﬁes the second condition.

G

Now we further reﬁne f to satisfy the ﬁrst condition. Let f′ be a proper coloring of the graph G with (d + 1)r colors in which every two vertices in distance at most r receive diﬀerent colors. The common reﬁnement q of f and f′ satisﬁes both conditions.

![image 7](<2012-hatami-limits-local-global-convergent-graph_images/imageFile7.png>)

# 6 Proof of the main theorem

Now we introduce the space X which will serve as a universal Borel space for the limit graphings of sequences of ﬁnite graphs with all degrees at most d. Consider the compact space C = k,r,n[tr,k,1/n] with the product topology where tr,k,1/n are deﬁned according to Lemma 5.1. We denote by X the compact space G(C) and by E ⊂ X × X the set of edges ((G,o1,c),(G,o2,c)) such that (o1,o2) is an edge in G (See Remark 4.1). Let q : X → C be the function deﬁned as q : (G,o,c)  → c(o). Furthermore for r,k,n ∈ N, deﬁne the coloring qr,k,n : X → [tr,k,1/n] as the composition of q with the projection to the coordinate (r,k,n) in C.

Let (Gi)∞i=1 be a local-global convergent sequence of graphs with all degrees at most d. For each Gi and triple (r,k,n) ∈ N3, we choose a coloring qr,k,ni : V (Gi) → [tr,k,1/n] guaranteed by

- Lemma 5.1. Let qi : V (Gi) → C be deﬁned as r,k,n{qr,k,ni (v)} ∈ C. As described in Section 4, each graph Gi together with the coloring qi deﬁnes a probability measure µi on X by putting the root on a random vertex of Gi and keeping only the connected component of the root.

By choosing a subsequence from (Gi)∞i=1 we can assume that the sequence {µi}∞i=1 weakly converges to a probability distribution µ on X. Our goal is to show that the Borel graph (X,E) with the measure µ is a graphing which represents the local-global limit of (Gi)∞i=1.

Let us ﬁrst observe that for a µ-random element (G,o,c) in (X,µ), with probability one, the

vertex labels {c(v) : v ∈ V (G)} are all diﬀerent. This follows from the fact that the colorings qr,k,ni separate points in Gi that are closer than r + 1, and that this property is preserved in the limit. This means that if v,w ∈ V (G) are of distance r, then with probability one their colors projected to the coordinate (r,k,n) (where k,n are arbitrary) are diﬀerent.

- Lemma 6.1 The measurable graph (X,E,µ) is a graphing.


Proof. Let us introduce the measures {ηi∗}∞i=1, similarly as in Section 3, by

ηi∗(A × B) =

e(x,B)dµi(x),

A

where A,B ⊆ X are measurable, and e(x,B) is the number of edges (x,y) ∈ E with y ∈ B. We deﬁne η∗ analogously as η∗(A × B) = A e(x,B)dµ(x).

Assume that A,B ⊂ X are open-closed sets. The weak convergence of {µi}∞i=1 implies that limi→∞ ηi∗(A × B) = η∗(A × B) and limi→∞ ηi∗(B × A) = η∗(B × A). Note that ηi∗(A × B) = ηi∗(B × A), since both are equal (up to normalization by |V (Gi)|) to the number of edges between the sets {v|(Gi,v,qi) ∈ A} and {v|(Gi,v,qi) ∈ B}. Here we used the fact that the vertex labels qi(·) are all diﬀerent and thus automorphisms of Gi cannot cause any problems. We obtain that η∗(B × A) = η∗(A × B), and since such product sets generate the whole σ-algebra on X × X, the proof is complete.

![image 8](<2012-hatami-limits-local-global-convergent-graph_images/imageFile8.png>)

i,r[qr,k,ni ] converge to PG,r[qr,k,n] as i → ∞ for every ﬁxed triple r,k,n ∈ N.

- Lemma 6.2 The probability distributions PG


Proof. Pick a µ-random point x = (G,o,c) ∈ X. Let the rooted graph Gx be the connected component of x in the graphing G rooted at x. There is a natural vertex coloring on Gx which is the restriction of the function q to the vertices of Gx. So Gx can be regarded as an element in X. We claim that with probability one x = (G,o,c) is isomorphic (in a root and label preserving way) to (Gx,q|G

). Indeed with probability one all the vertex labels of G are diﬀerent, and in this case the map given by v  → (G,v,c) deﬁnes a decoration-preserving isomorphism between (G,o,c) and Gx. (The fact that the vertex labels in G are all diﬀerent guarantees that the map is one to one.)

x

We conclude that the probability distribution PG,r[qr,k,n] is the same as the distribution of (NG,r(o),cr,k,n) where (G,o,c) is a µ-random element in X, and cr,k,n is the projection of c to the coordinate (r,k,n). The lemma now follows from the weak convergence of {µi}∞i=1 to µ.

![image 9](<2012-hatami-limits-local-global-convergent-graph_images/imageFile9.png>)

- Lemma 6.3 For every r,k ∈ N and ε > 0 there is an index i0 such that for every i ≥ i0 and


c ∈ K(k,Gi), there is a k-coloring c′ of X such that dvar(PG

i,r[c],PG,r[c′]) ≤ ε. Proof. Let n ≥ 2/ε. By Lemma 6.2 there is an index i0 such that dvar(PG

ε 2

i,r[qr,k,ni ],PG,r[qr,k,n]) ≤

(2)

![image 10](<2012-hatami-limits-local-global-convergent-graph_images/imageFile10.png>)

for every index i ≥ i0. Let i ≥ i0 be arbitrary, and let c ∈ K(k,Gi) be a k-coloring of Gi. Then by

- Lemma 5.1 there is a map α : [tr,k,ε/2] → [k] such that

dvar(PG

i,r[c],PG

i,r[α ◦ qr,k,ni ]) ≤

1 n

![image 11](<2012-hatami-limits-local-global-convergent-graph_images/imageFile11.png>)

≤

ε 2

![image 12](<2012-hatami-limits-local-global-convergent-graph_images/imageFile12.png>)

.

The deﬁnition of the total variation distance and (2) imply that

dvar(PG

i,r[α ◦ qr,k,ni ],PG,r[α ◦ qr,k,n]) ≤

ε 2

![image 13](<2012-hatami-limits-local-global-convergent-graph_images/imageFile13.png>)

.

Hence c′ = α ◦ qr,k,n satisﬁes the required condition.

![image 14](<2012-hatami-limits-local-global-convergent-graph_images/imageFile14.png>)

- Lemma 6.4 For every coloring c ∈ K(k,G), r ∈ N and ε > 0 there is an index i0 such that for


every i ≥ i0, there is a coloring c′ ∈ K(k,Gi) with dvar(PG

i,r[c′],PG,r[c]) ≤ ε.

Proof. Let c : X → [k] be a Borel coloring. Then for every δ > 0, there is a continuous coloring

cδ : X → [k] such that |µ(c−1(a)△c−δ 1(a))| ≤ δ for all 1 ≤ a ≤ k. Taking δ to be suﬃciently small, we have

ε 2

dvar(PG,r[cδ],PG,r[c]) ≤

. (3)

![image 15](<2012-hatami-limits-local-global-convergent-graph_images/imageFile15.png>)

Let the graphing Gi be the same as the graphing G with the only diﬀerence that the measure µ is replaced by µi. Since {µi}∞i=1 converges weakly to µ and cδ is continuous, there is an index i0 such that if i ≥ i0, then

ε 2

i,r[cδ],PG,r[cδ]) ≤

dvar(PG

. (4)

![image 16](<2012-hatami-limits-local-global-convergent-graph_images/imageFile16.png>)

The coloring cδ induces a coloring fδi on Gi which assigns to every vertex v ∈ V (Gi) the cδ color of the rooted graph (Gi,v,qi) ∈ X. Then we have PG

i,r[fδi] ≡ PG

i,r[cδ]. Together with (3) and (4), this completes the proof.

![image 17](<2012-hatami-limits-local-global-convergent-graph_images/imageFile17.png>)

# 7 Bernoulli graphings and Bernoulli graph sequences

Probably the most fundamental graphing construction is the Bernoulli graphing corresponding to an involution-invariant measure. These graphings are closely related to factor of i.i.d. processes and local algorithms. In this chapter we explain their role in local-global convergence.

Deﬁnition 7.1 (Bernoulli graphings) Let µ be an involution-invariant measure on G. Let ν be the probability measure on G[0,1] produced by putting independent random weights from [0,1] on the nodes of a µ-random graph. (Note that diﬀerent choices of the weights can lead to the same point of G[0,1], if they can be transformed into each other by an automorphism of the µ-random rooted graph.) The triple (G[0,1],ν,E[0,1]) as deﬁned in Remark 4.1 will be called the Bernoulli graphing corresponding to µ, and denoted by Bµ.

It is not hard to see that Bµ is a graphing and it represents the involution-invariant distribution µ (Elek [14]).

Remark 7.2 Perhaps it would be more natural to decorate the nodes of the µ-random graph by independent bits, or more generally, by colors from [k] for some ﬁxed k ≥ 2. This would yield an involution-invariant distribution on G[k], but the graph (G[k],E[k]) together with this distribution would not necessarily form a graphing.

We deﬁne the Bernoulli graphing BG corresponding to an arbitrary graphing G as the Bernoulli graphing deﬁned by the involution-invariant distribution induced by G on G. Clearly G and BG are locally equivalent.

Example 7.3 A simple example for a Bernoulli graphing is provided by the involution-invariant measure which is concentrated on a single d-regular rooted tree. Let T denote the rooted d-regular tree, and let (X,ν) be the probability space in which we put independent random weights from [0,1] on the vertices of T. Two points of X are connected in G if they can be obtained from each other by moving the root to a neighboring vertex. It seems to be an interesting problem to decide whether the sets QG,r,k are all closed (see also Question 9.1).

The following is a related construction. For every graphing G on the probability space (X,ν), we deﬁne its Bernoulli lift G+ as follows. The underlying set X+ of G+ will be pairs (x,ξ), where

- x ∈ X and ξ : V (Gx) → [0,1] assigns weights from [0,1] to the vertices of the connected component Gx rooted at x. We connect (x,ξ) to (y,υ) if y is a neighbor of x and ξ = υ. (Note that if y is a neighbor of x, then Gx = Gy.) The measure on X+ is deﬁned as follows. To generate a random element of X+, one picks a ν-random point x ∈ X, and then assigns independent random weights ξ(u) to the nodes u of Gx.


We deﬁne two maps φ : V (G+) → V (G) and ψ : V (G+) → V (BG) by φ(x,ξ) = x and ψ(x,ξ) = Gx,ξ . It is easy to check that the maps φ and ψ are local isomorphisms. This implies that graphing G is locally equivalent to its Bernoulli lift G+ as well as its Bernoulli graphing BG.

Our main goal in this section is to describe the relationship between G, BG and G+ from the point of view of local-global equivalence. Deﬁnition 7.4 A graphing is called atom-free if its underlying probability space contains no mass points.

Remark 7.5 Note that no ﬁnite graph corresponds to an atom-free graphing. Using the graphing property (1), it is easy to see that if a graphing contains an atom, then this belongs to a ﬁnite component. If G is the local limit of a sequence of connected graphs (Gn)∞n=1 with V (Gn)| → ∞, then all its components are inﬁnite, and hence it is atom-free. On the other hand, if the union of ﬁnite components of a graphing has positive weight, then merging isomorphic ﬁnite components we get atoms. Furthermore, if G is the local-global limit of graphs (Gn)∞n=1 (not necessarily connected) with |V (Gn)| → ∞, then G is atom-free. This follows from the observation that a graphing is atom-free if and only if its points have a Borel k-coloring with equal color classes for every k.

The following is our main result in this section.

- Theorem 7.6 Every atom-free graphing is local-global equivalent to its Bernoulli lift.


The map ψ : V (G+) → V (BG) deﬁned above is a local isomorphism from G+ to BG. Thus we have the relation BG ≺ G+, which implies by Theorem 7.6: Corollary 7.7 (Minimality of Bernoulli graphings) For every atom-free graphing G, we have BG ≺ G.

In other words, Bernoulli graphings are minimal elements in the set of atom-free graphings in their local equivalence class. A group theoretical analogue of this fact was obtained by Ab´ert and Weiss in [2].

In an algorithmic setting, a Borel coloring of G+ can be considered as a coloring that depends not only on the graph, but also on a random real number at each point. To be able to imitate this in G, we have to construct “random-like” colorings on G. For technical reasons, we have to deal with graphings that already have a Borel coloring.

Deﬁnition 7.8 (Quasirandom colorings) Let G be a graphing on the space (X,ν), and let h : X → [l] be a Borel coloring. Let µr,h,k be the probability distribution on Ur,kl obtained

from ν by considering the r-neighborhood of a random element x ∈ X and decorating its vertices by random independent elements from [k] (in addition to the given l-coloring h). We say that a measurable coloring c : X → [k] is (r,ε)-quasirandom if dvar(PG,r[c × h],µr,h,k) ≤ ε where c × h denotes the kl-coloring with pairs of colors (c(x),h(x)).

- Lemma 7.9 (Existence of quasirandom colorings) Let G be a atom-free graphing on the space


- (X,ν). Then for every k,r,l ∈ N, ε > 0 and Borel l-coloring h, there is an (r,ε)-quasirandom coloring c : X → [k] of (G,h).


Proof. Let C = {0,1}N be the Cantor set with the uniform measure. Since (X,ν) has no mass points, there is a measurable equivalence between C and X, without loss of generality, we can identify the two spaces, assume that X = C. Let πi : C → {0,1}i be the projection onto the ﬁrst i coordinates. The map πi is measure preserving if we consider the uniform measure on {0,1}i. Fix k,r ∈ N, and let gi : {0,1}i → [k] be a uniform random coloring of {0,1}i with k colors. Our goal is to show that if i is suﬃciently large, then with a large probability gi ◦ πi is (r,ε)-quasirandom.

- Claim 1 For every ε1 > 0 and n ∈ N, there is an index j such that if x1,...,xn ∈ X are independent ν-random points, then with probability 1 − ε1, the map πj separates all the points in ∪ni=1NG,r(xi).


It is easy to see that π = (π1,π2,...) separates the points of ∪ni=1NG,r(xi) with probability 1 on Xn. Let Yj denote the set of points (x1,x2,...,xn) in Xn for which πj separates the points in ∪ni=1NG,r(xi). Then Yj is an increasing chain of measurable sets such that ν(∪∞i=1Yi) = 1. This shows that for some index j, we have ν(Yj) > 1 − ε1 and completes the proof of Claim 1.

Let x = (x1,...,xn) ∈ Xn and let g be a k-coloring ∪ni=1NG,r(xi). Let us say that x is representative if the distribution of the l-colored neighborhood NG,h,r(xt) for a random t ∈ [n] is ε/6-close to the distribution µr,h := PG,r[h]. Let us say that (x,g) is representative if the distribution of the kl-colored neighborhood (NG,h,r(xt),g) is ε/3-close to the distribution µr,h,k.

Let x = (x1,...,xn) ∈ Xn be chosen randomly and independently from the distribution ν. We note that with probability 1, the neighborhoods NG,r(xi) are disjoint. If n is large enough, then (just by the Law of Large Numbers)

ε 6

Prx(x representative) ≥ 1 −

.

![image 18](<2012-hatami-limits-local-global-convergent-graph_images/imageFile18.png>)

Hence if g is a uniform random k-coloring of ∪ni=1NG,r(xi), and n is large enough, then (by the Law of Large Numbers again), we have

ε 3

Prx,g((x,g) representative) ≥ 1 −

. Let us ﬁx n so that this holds.

![image 19](<2012-hatami-limits-local-global-convergent-graph_images/imageFile19.png>)

Next, using Claim 1, we ﬁx j so that (for a random x) πj separates all the points in ∪ni=1NG,r(xi) with probability at least 1 − ε/3. Whenever this happens, the restriction of gj ◦ πj to ∪ni=1NG,r(xi) is a uniform random k-coloring. In other words, we can generate a uniform random k-coloring of

∪ni=1NG,r(xi) by restricting gj ◦ πj to it if πj separates it, and randomly k-coloring it otherwise. Thus

- 2ε

![image 20](<2012-hatami-limits-local-global-convergent-graph_images/imageFile20.png>)

- 3


ε 3

≥ 1 −

((x,gj ◦ πj) representative) ≥ Prx,g((x,g) representative) −

.

Prx,g

![image 21](<2012-hatami-limits-local-global-convergent-graph_images/imageFile21.png>)

j

It follows that there is at least one k-coloring gj for which

- 2ε

![image 22](<2012-hatami-limits-local-global-convergent-graph_images/imageFile22.png>)

- 3


Prx((x,gj ◦ πj) representative) ≥ 1 −

.

Let us ﬁx such a gj. Then c = gj◦πj is an (r,ε)-quasirandom k-coloring of X. In fact, we can generate

- a random point of x by ﬁrst generating n independent random points x1,...,xn and choosing one of


- them, xt, uniformly at random. Then with probability at least 1−2ε/3, (x,gj ◦πj) is representative, and whenever this happens, the distribution of the kl-colored neighborhood (NG,h,r(xt),gj ◦ πj) is ε/3-close to the distribution µr,h,k. It follows that the total variation distance of (NG,h,r(xt),gj ◦πj) from µr,h,k, when xt is also randomly chosen, is at most ε.


![image 23](<2012-hatami-limits-local-global-convergent-graph_images/imageFile23.png>)

Our next lemma shows that we can approximate any measurable k-coloring of G+ by a k-coloring that is “locally computable” in the sense that the color of a node depends only on a colored neighborhood of the node, and it depends only on a discrete approximation of the nodeweights. To be precise, we deﬁne the (m,s)-discretization (m,s ∈ N) as the map ξm,s : X+ → Us,m, where ξm,s(x) is obtained by considering the neighborhood NG+,s(x), and replacing every nodeweight ξ(v) by ⌈mξ(v)⌉. Recall that the local isomorphism φ : V (G+) → V (G) is deﬁned by φ : (x,ξ)  → x.

- Lemma 7.10 For every r ≥ 1 and ε > 0, and every measurable k-coloring c of G+, there are positive integers s,m and l, a measurable l-coloring h of G, and a map f : Us,m × [l] → [k] such that the k-coloring c′(x) = f ξs,m(x),h(φ(x)) of G+ satisﬁes


dvar PG+,r[c],PG+,r[c′] ≤ ε. Proof. Let (X+,ν+) be the underlying space of G+. Let K denote the set of all subsets of X+ of the form ξm,s−1 (y)∩φ−1(B), where y ∈ Us,m, and B is a Borel set of X. These sets generate the Borel sets of X+, hence by the Monotone Class Theorem, the closure under pointwise convergence of the vector space generated by their indicator functions contains every bounded Borel function on X+.

i,mi, Borel sets Bi ⊆ X and real coeﬃcients ai (i = 1,...,N) such that

In particular, there are pairs of integers (mi,si), colored balls yi ∈ Us

ν+ x ∈ X+ : c(x) −

N

- 1

![image 24](<2012-hatami-limits-local-global-convergent-graph_images/imageFile24.png>)

- 2


i,si(x) = yi,φ(x) ∈ Bi) ≥

ai (ξm

i=1

ε dr+1

<

.

![image 25](<2012-hatami-limits-local-global-convergent-graph_images/imageFile25.png>)

Let s = maxi si, m = i mi, l = 2N, and let h be a Borel l-coloring of X in which every Bi is a union of color classes. Then the sum in the above expression can be written as g ξs,m(x),h(φ(x)) for some g : Us,m×[l] → R. Rounding the values of g to the closest integer in [k], we get a k-coloring c′ for which

ε dr+1

ν x ∈ X+ : c(x) = c′(x) <

.

![image 26](<2012-hatami-limits-local-global-convergent-graph_images/imageFile26.png>)

For a random point x ∈ X+, the probability that the colorings c and c′ diﬀer on any node in its r-neighborhood is less than ε. This implies the lemma.

![image 27](<2012-hatami-limits-local-global-convergent-graph_images/imageFile27.png>)

Now we are able to prove the main theorem in this section.

Proof of Theorem 7.6. Our goal is to approximate every element in QG+,r,k by an element in QG,r,k with arbitrary precision ε > 0. In other words, we want to construct, for every measurable

k-coloring c of G+, a measurable k-coloring c0 of G that deﬁnes a similar distribution of colored neighborhoods.

By Lemma 7.10 we may assume that c is of the form f ξs,m(x),h(φ(x)) where h is an l-coloring of

- G and f : Us,m → [k]. Let q be an (s,ε)-quasirandom m-coloring of (G,h) guaranteed by Lemma 7.9, and let G′ = (G,h × q). Consider the k-coloring of G deﬁned by c0(z) = f(NG′,s(z),h(z)). We claim that c0 has similar statistics as c:


dvar(PG+,r[c],PG,r[c0]) ≤ ε.

This follows if we prove that the distributions of (ξs,m(y),h(φ(y)) (where y is a random point of G+) and (NG′,s(x),h(x)) (where x is a random point of G) are close. But the distribution of (ξs,m(y),h(φ(y)) is just µs,h,m, and the distribution of (NG′,s(x),h(x)) is ε-close to this by the quasirandomness of q. This completes the proof.

![image 28](<2012-hatami-limits-local-global-convergent-graph_images/imageFile28.png>)

The following fact shows another connection between a graphing and its associated Bernoulli graphing. We say that two graphings are bi-locally isomorphic if there exists a third graphing that has local isomorphisms into both. The construction of the Bernoulli lift implies that every graphing is bi-locally isomorphic to its Bernoulli graphing. Since by the deﬁnition of the Bernoulli graphing, two graphings are locally equivalent if and only if they have the same Bernoulli graphing, we get the following more explicit characterization:

Proposition 7.11 Two graphings are locally equivalent if and only if they are bi-locally isomorphic.

To prove this proposition, it suﬃces to show that bi-local isomorphism is a transitive relation. This takes some work which we do not discuss here; for the details, we refer the reader to [24].

Let us turn to graph sequences. Every locally convergent graph sequence determines a unique involution-invariant distribution and through this, a Bernoulli graphing. One expects that among sequences with the same local limit, a sequence with the least possible global structure would converge to the Bernoulli graphing in the local-global sense. As a special case, the following conjecture was popularized by us in the past few years: Let Gn be a random d-regular graph on n vertices (if d is odd, then we only consider even values of n). Then (Gn)∞n=1 is a Bernoulli sequence with probability one. In other words, the limit object is the Bernoulli graphing produced from the d-regular tree. A very recent paper of Gamarnik and Sudan [18] disproves this conjecture.

The following weaker conjecture remains unsolved:

Conjecture 7.12 A growing sequence of random d-regular graphs is local-global convergent with probability one.

We don’t know whether for d ≥ 3, the Bernoulli graphing corresponding to the d-regular tree is the local-global limit of any graph sequence.

# 8 Joins and maximal graphings

We show that every weak equivalence class of graphings contains a maximal member. For this, we introduce a direct product-like construction.

- Lemma 8.1 Let G,G1,G2,... be graphings and let φi : V (Gi) → V (G) be local isomorphisms. Then there exists a graphing H and local isomorphisms ψi : V (H) → V (Gi) and ξ : V (H) → V (G) such that φi ◦ ψi = ξ.


We call H a join of the graphings Gi relative to the common “factor” G.

Proof. Let (X,ν) be the underlying space of G, and let (Xi,νi) be the underlying space of Gi. First, consider the cartesian product space U = i Xi. Let ψi : U → Xi be the coordinate maps, and consider the “diagonal” ∆ = {x ∈ U : ψi(φi(x)) = ψj(φj(x))for all i,j ∈ N}. By this deﬁnition, the map ξ = ψi ◦ φi|U is independent of i.

We note that ∆ is nonempty; in fact, ξ(∆) has measure 1 in G. Indeed, the facts that φi is measure preserving and the space Xi is standard imply that φi(Xi) is a measurable subset of X of measure 1. Hence so is the set W = ∩iφi(Xi). For any x ∈ W and any choice yi ∈ φ−i 1(x), we have

- y = (yi,y2,...) ∈ U and ξ(y) = x. The cartesian product graph H′ = i Gi, deﬁned by


V (H′) =

i

V (Gi) E(H′) = {(x,y) : (ψi(x),ψi(y)) ∈ E(Gi) for all i = 1,2,...},

is not locally ﬁnite in general, but the induced subgraph H = H′[∆] is:

- Claim 2 When restricted to any connected component of H, every coordinate map ψi gives an isomorphism between this connected component of H and a connected component of Gi. Consequently, all degrees of H are bounded by d.

Let x ∈ ∆, and consider the connected component L of H containing x, the connected component J of G containing ξ(x), and the connected component Ji of Gi containing ψi(x). The map φi is a local isomorphism, and hence it gives an isomorphism between Ji and J. Let ζi : V (J) → V (Ji) be the inverse of this map, and deﬁne ζ(y) = (ζ1(y),ζ2(y),...) for y ∈ V (J). It is straightforward to check that ζ is an embedding of J into H, and that there are no further edges of H incident with the nodes of ζ(V (J)). Hence ζ(J) = L. This proves the Claim.

We deﬁne a Polish space Y on ∆ by restricting the product space i Xi to ∆. It is not hard to check that H is a Borel graph on Y .

Next, we deﬁne a measure on Y . Let Ai ⊆ Xi be Borel sets so that only a ﬁnite number of them are proper subsets. Let σi(B) = νi(Ai ∩ φ−i 1(B)) for every Borel subset B ⊆ X, and consider the Radon-Nikodym derivative fi = dσi/dν. Deﬁne

µ(A1 × A2 × ···) =

X

f1f2 ... dν. (5)

It is not hard to check that µ extends from these boxes to a probability measure on all Borel sets in ∆ (in ergodic theory, this construction is called the relatively independent joining of the measures νi over the common factor ν; see e.g. [9], Lemma 6.2 for a detailed description of this construction for two factors). It is easy to see that every coordinate map ψi is measure preserving as a map from (Y,µ) → (X,ν).

- Claim 3 The measure µ, as a measure on the Borel graph H, is involution invariant.


To prove this, it suﬃces to construct a measure σ∗ on Y × Y that is concentrated on E(H) and

σ∗(A × B) =

eH(x,B)dµ(x). (6)

A

Since the Gi are graphings, we know that there are measures ηi∗ on the Borels sets of Xi × Xi, and η∗ on the Borels sets of X × X, related similarly to the measures νi and ν. The space Y × Y

is the cartesian product of the spaces Xi × Xi, and the maps φi deﬁne measure preserving maps φi ×φi : (Xi ×Xi,ηi∗) → (X,η∗). We deﬁne a measure σ∗ similarly to (5) above. It is easy to check that σ∗ satisﬁes (6) and it is concentrated on E(H).

Thus we know that H is a graphing, and the maps ψi : V (H) → V (Gi) and ξ are local automorphisms.

![image 29](<2012-hatami-limits-local-global-convergent-graph_images/imageFile29.png>)

- Theorem 8.2 In every local equivalence class C of graphings there is a largest one in the local-global partial order.


Proof. Let Qr,k denote the union of the sets QG,r,k, where G ∈ C. There is a countable set of graphings F = {G1,G2,...} in the equivalence class such that ∪iQG

i,r,k is dense in Qr,k for every r and k. It is enough to ﬁnd a graphing that is larger than every Bernoulli lift Gi+ in the local-global partial order.

Let B be the Bernoulli graphing in C. As shown in Section 7, there are local isomorphisms φi : V (Gi+) → V (B). By Lemma 8.1, there is a graphing H and there are local isomorphisms

- H → Gi+. This implies that H is above any of the Gi+ in the local-global partial order.


![image 30](<2012-hatami-limits-local-global-convergent-graph_images/imageFile30.png>)

# 9 Non-standard graphings

An alternative proof of Theorem 3.2 can be based on the ultraproduct method of Elek and Szegedy [17]. Let (Gi)∞i=1 be an arbitrary graph sequence of maximum degree at most d. Let ω be a nonprincipal ultraﬁlter on N. Let G denote the ultraproduct of the graph sequence. The vertex set V of G is the ultraproduct of the vertex sets Vi of Gi and the edge set E ⊂ V × V is the ultraproduct of the edge sets Ei ⊂ Vi ×Vi of Gi. The graph G has maximum degree at most d, since this property is expressible by a ﬁrst order formula. We can also construct a σ-algebra A on V and a probability measure µ on V which is the ultralimit of the uniform distributions on the sets Vi. It is not hard to check that G satisﬁes the graphing axiom (1).

If (Gi)∞i=1 is a locally convergent graph sequence, then G has neighborhood frequencies that are the limits of the neighborhood frequencies of the graphs Gi. If (Gi)∞i=1 is locally-globally convergent,

- then QG,r,k is the Hausdorﬀ limit of the sets QG


i,r,k. However, this does not directly prove Theorem 3.2, since (V,µ) is not a separable probability space. One can complete the proof by choosing an appropriate separable sub-sigma-algebra of G which preserves the graphing structure. We omit the details here.

An attractive feature of ultralimit graphings is that the sets QG,r,k are all closed. It is not clear if there is a standard graphing representation of the limit of a convergent sequence with this stronger property.

Question 9.1 Let (Gn)∞n=1 be a local-global convergent sequence of graphs. Is there a graphing G that represents the limit with the property that QG,r,k are all closed?

# 10 Hyperﬁnite graphs and graphings

For a graph G, we deﬁne τq(G) as the smallest t such that deleting t appropriate nodes, every connected component of the remaining graph has at most q nodes. We say that a sequence (Gn)∞n=1 of ﬁnite graphs is (q,ε)-hyperﬁnite if liminfn τq(Gn)/|V (Gn)| ≤ ε. We say that (Gn)∞n=1 is hyperﬁnite if for every ε > 0, there is a q such that (Gn)∞n=1 is (q,ε)-hyperﬁnite. We can deﬁne hyperﬁniteness of a graphing G on underlying space X similarly: let τq(G) denote the inﬁmum of numbers δ ≥ 0 such that we can delete a Borel set S ⊆ X with measure δ so that every connected component of the remaining graphing has at most q nodes. We say that a graphing G is (q,ε)-hyperﬁnite if τq(G) ≤ ε, and we say that G is hyperﬁnite if for every ε > 0, there is a q such that G is (q,ε)-hyperﬁnite. Since we are talking about graphs with bounded degree, we could replace deleting nodes by deleting edges in the deﬁnitions of hyperﬁniteness.

Hyperﬁniteness in diﬀerent settings was introduced by diﬀerent people (see Kechris and Miller [22], Elek [15], Schramm [28]). Schramm proved that a locally convergent sequence of graphs is hyperﬁnite if and only if its limit is hyperﬁnite. This does not hold for (q,ε)-hyperﬁniteness for a ﬁxed pair

- q and ε. As an easy example, a sequence of random d-regular graphs tend to a limiting involutioninvariant distribution (concentrated on the inﬁnite d-regular tree) that is (1,1/2)-hyperﬁnite, while the sequence is not. On the other hand, a local-global convergent sequence of graphs behaves nicer:


- Proposition 10.1 Let a sequence (Gn)∞n=1 of ﬁnite graphs converge to a graphing G in the localglobal sense. Then (Gn)∞n=1 is (q,ε)-hyperﬁnite if and only if G is (q,ε)-hyperﬁnite.

Proof. A ﬁnite graph G satisﬁes τq(G) ≤ ε|V (G)| if and only if it has a 2-coloring c such that PG,k,r[c](c(root) = 1) ≤ ε and PG,k,r[c](B) = 0 for every colored r-ball B that contains a connected all-blue subgraph with k+1 nodes. A graphing G satisﬁes τq(G) ≤ ε if and only if for every ε′ > ε, it has a 2-coloring c such that PG,k,r[c](c(root) = 1) ≤ ε′ and PG,k,r[c](B) = 0 for every colored r-ball B that contains a connected all-blue subgraph with k + 1 nodes. The proposition follows by the deﬁnition of local-global convergence to a graphing.

![image 31](<2012-hatami-limits-local-global-convergent-graph_images/imageFile31.png>)

The following important property of hyperﬁniteness is closely related to the results of Schramm [28] and Benjamini, Schramm and Shapira [7]. It can be derived using the graph partitioning algorithm of Hassidim, Kelner, Nguyen and Onak [20]; a direct proof is given in [24].

- Proposition 10.2 Hyperﬁniteness is invariant under local equivalence.


Together with Proposition 10.1, this implies the above mentioned result of Schramm that a locally convergent sequence of graphs is hyperﬁnite if and only if its limit is hyperﬁnite. We note that (q,ε)-hyperﬁniteness for a ﬁxed q and ε is not invariant under local equivalence, which is shown, for example, by the local-global limits of random d-regular graphs and of random d-regular bipartite graphs. Our main result about hyperﬁnite graphings is a strengthening of Corollary 7.7.

Theorem 10.3 Every atom-free hyperﬁnite graphing G is locally-globally equivalent to its Bernoulli graphing.

Proof. By Corollary 7.7, BG ≺ G. It remains to show that G ≺ BG. In other words, for every coloring of G, we have to ﬁnd a coloring of BG with almost the same local statistics.

Let (X,ν) be the underlying space of G, let c : X → [k] be a measurable coloring, and let us ﬁx a radius r ∈ N and an ε > 0. Let νB denote the measure of BG, and set ε1 = ε/(8(d + 1)r). By Proposition 10.2, the Bernoulli graphing BG of a hyperﬁnite graphing G is also hyperﬁnite. Let S ⊂ G[0,1] be a subset such that νB(S) ≤ ε1 and every connected component of G[0,1]\S has at most n nodes. Let m ∈ N, and deﬁne the coloring b : G[0,1] → [m] × {0,1} by b(x) = (⌈w(o)m⌉, S(x)) where x = (G,o,w). Choosing m large enough, we may assume that the set S′ of points x for which NB

G,r(x) contains two points with the same color has measure at most ε1. Note that νB(S∪S′) ≤ 2ε1 and all points of BG \ (S ∪ S′) are contained in connected components that have at most n vertices, and whose nodes are colored diﬀerently by b.

On the other hand, by Corollary 7.7 we have BG ≺ G which implies that there is a coloring

- b∗ : X → [m] × {0,1} such that


dvar(PG,n[b∗],PB

G,n[b]) ≤ ε1.

It follows that there are subsets T ⊆ G[0,1] and T′ ⊆ X with νB(T) = ν(T′) ≤ 4ε1 such that the following conditions hold:

- (a) All points of BG \ T are contained in connected components that have at most n vertices and whose nodes are colored diﬀerently by b, and the same holds for the connected components of G \ T′ with coloring b∗;
- (b) Furthermore, for every ([m] × {0,1})-colored connected graph H with at most n vertices, the measure of points in components isomorphic to H (as colored graphs) is the same in BG \ T and G \ T′. Let VH(BG \ T) and VH(G \ T′) be these two sets.


Let C be a connected component of G \ T′. Since the vertices of C are colored diﬀerently by b∗, there is a (unique) function fC : [m] × {0,1} → [k] such that c = fC ◦ b∗ on the nodes of C. This splits every set VH(G \T′) into at most k2m measurable sets VH,f(G \T′) (indexed by functions f : [m] × {0,1} → [k]) that are unions of components of G \ T′.

Split VH(BG \ T) into sets VH,f(BG \ T) so that each VH,f(BG \ T) is a union of components of BG \ T, and moreover νB(VH,f(BG \ T)) = ν(VH,f(G \ T′)). This is possible since there is no probability mass on any component of BG.

Let c′ be the measurable k-coloring of BG deﬁned in the following way. Every v ∈ VH,f(BG \ T) is colored by f ◦ b(v), and the points in T are all colored with one arbitrary color in [k]. Note that the (conditional) local statistics of c′ obtained by picking a random v ∈ BG conditioned on NB

G,r(v) ∩ T = ∅ is the same as the (conditional) local statistics of c obtained by picking a random v ∈ G conditioned on NG,r(v)∩T′ = ∅. The ν-measure of the vertices v ∈ G with NG,r(v)∩T′ = ∅ is

- at most ν(T′)(d + 1)r ≤ 4ε1(d + 1)r. The same bound also holds for the νB-measure of the vertices


v ∈ BG with NB

G,r(v) ∩ T = ∅. Thus we have dvar(PG,r[c],PB

G,r[c′]) ≤ 8(d + 1)rε1 ≤ ε which proves the theorem.

![image 32](<2012-hatami-limits-local-global-convergent-graph_images/imageFile32.png>)

Remark 10.4 As the proof of Theorem 10.3 shows, G ≺ BG holds for every hyperﬁnite graphing G (not necessarily atom-free).

Now we are ready to state and prove our main theorem about convergence of hyperﬁnite graph sequences. This theorem was proved independently by Elek [16]. Theorem 10.5 Every locally convergent hyperﬁnite graph sequence (Gn)∞n=1 with |V (Gn)| → ∞ is a local-global convergent Bernoulli sequence.

Proof. Let (Gi)∞i=1 be a locally convergent hyperﬁnite sequence, and let µ be the involutioninvariant measure on G that is the local limit of the sequence. Since the Bernoulli graphing Bµ is locally equivalent to the local limit of (Gi)∞i=1, Proposition 10.2 implies that it is hyperﬁnite.

To prove the theorem, assume by contradiction that (Gi)∞i=1 does not converge in the localglobal sense to Bµ. Then it has a local-global convergent subsequence whose limit graphing G is not local-global equivalent to BG = Bµ. By Remark 7.5 the condition |V (Gn)| → ∞ implies that G is atom-free. This however contradicts Theorem 10.3.

![image 33](<2012-hatami-limits-local-global-convergent-graph_images/imageFile33.png>)

Corollary 10.6 Local-global convergence is equivalent to local convergence when restricted to growing hyperﬁnite graph sequences.

# 11 Graphings as operators and expander graphings

Let G be a Borel graph on the probability space (X,µ) with all degrees at most d. If f : X → C is a measurable function, then we deﬁne Gf : X → C by

Gf(x) =

f(v).

(x,v)∈E(G)

It takes a short calculation to show that if G is a graphing, then it acts on the Hilbert space L2(X,ν)

- as a bounded self-adjoint operator. Let f : X → C be an arbitrary function in L2(X,ν). Then


|Gf(x)|2 dν ≤

x

|f(v)|2 dν = d |f(x)|2deg(x) dν ≤ d2 f 22.

d

x

(x,v)∈E(G)

The equality in the above calculation uses the fact that G satisﬁes (1). It is easy to see that (1) is equivalent to the statement that the action of G is self-adjoint in the sense that  Gf,g = f,Gg holds for every pair f,g of bounded measurable functions. This implies that the action of G is also self-adjoint on L2(X,ν). The Laplace operator corresponding to a graphing is deﬁned as L = D −G where Df(x) = f(x)deg(x). It is easy to check that

Lf,f =

(f(v) − f(w))2 dη∗ (7)

(v,w)∈E(G)

holds in L2(X,ν) where η∗ is deﬁned in Section 3. Thus L is positive semideﬁnite .

The theory of graphings is closely related to the theory of measure preserving systems (in a sense, it generalizes ergodic theory). In particular, one can deﬁne the notion of ergodicity. A graphing G is ergodic if there is no measurable partition of the vertex set X into positive measure sets X1,X2 such that there is no edge between X1 and X2, or equivalently such that X1 is a union of connected components of G. Note that graphings, when deﬁned on an uncountable set, are never connected as graphs and so the notion of ergodicity is a good replacement for the notion of connectivity. Equation (7) implies the following analogue of a well known theorem from ergodic theory about the Koopman representation (see [19]).

- Proposition 11.1 Let L be the Laplace operator corresponding to the graphing G. The multiplicity of the eigenvalue 0 of L as an operator on L2(X,ν) is 1 if and only if G is ergodic.

Graphings oﬀer new phenomena. Ergodicity is equivalent to saying that ν(N1(S)) > ν(S) for every set S with 0 < ν(S) ≤ 1/2 (Here N1(S) = ∪x∈SNG,1(x)). Positive expansion is a natural strengthening of this condition. We say that a graphing G is a c-expander if for every Borel set S ⊆ X with 0 < ν(S) ≤ 1/2, we have ν(N1(S)) ≥ (1 + c)ν(S). We say that a graphing G is an expander if it is a c-expander for some c > 0.

Let us restrict our attention to d-regular graphs and graphings. Let (Gn)∞n=1 be a sequence of d-regular graphs that are expanders with expansion c > 0. Let us select a local-global convergent subsequence. It is easy to see that its limit is a d-regular graphing that is also a c-expander.

We can generalize spectral conditions for expanders to graphings. Let us deﬁne spectral gap of a d-regular graphing by

gap(G) = inf{ Lf,f : f,f = 1, f,1 = 0} (note that it does not matter whether we take the inﬁmum over f ∈ L2(X) or f ∈ L∞(X)). The following analogue of the theorems of Alon and Milman [4] and Alon [3] on expanders can be proved along the same lines:

- Proposition 11.2 Suppose that a d-regular graphing G is a c-expander. Then c2/(2d) ≤ gap(G) ≤ 2c. In particular, a graphing is an expander if and only if its spectral gap is positive.


An easy calculation shows that if G1 and G2 are local-global equivalent, then gap(G1) = gap(G2). In other words gap(G) is a local-global invariant quantity. This follows from the classical fact that measurable functions can be arbitrarily well approximated by step functions. It is also easy to see that gap(G) is not invariant under local equivalence.

One must be careful though: the spectral gap gap(G) is a lower bound on the eigenvalues of G belonging to non-constant eigenfunctions of G, but it may not be the inﬁmum of such eigenvalues. For example, the Bernoulli graphing of a 2-way inﬁnite path is ergodic but not an expander, and its Laplacian has no non-constant eigenfunction.

# 12 Graphings and local algorithms

Local algorithms and factor of i.i.d. processes. Elek and Lippner [13] formulate a correspon-

dence principle between graphings and local algorithms. We can make this more precise using the notion of Bernoulli graphings:

Measurable graph theoretic statements for Bernoulli graphings correspond to randomized local algorithms for ﬁnite graphs.

Let us consider an example. Let T be the d-regular tree with a distinguished root and let Ω be the compact space [0,1]V(T). Let f : Ω → [k] be any measurable function which depends only on the isomorphism class of the labeled rooted tree. In other words f is invariant under the action of the root preserving automorphism group of T. Using the function f, we create a random model of k colorings of T in the following way. First we produce a random element ω ∈ Ω by putting independent random weights from [0,1] on the vertices of T, and then for every v ∈ V (T), we deﬁne the color c(v) as the value of f on the labeled rooted tree obtained from T by assigning labels ω and placing the root on v. We say that f is the rule of the coloring process c. Such processes on the tree are called factor of i.i.d. processes. We say that the rule f has radius r if it depends only on the labels on vertices of T that are of distance at most r from the root.

The following rule (of radius 1) is a classical method to construct an independent set of nodes in a graph (see Alon and Spencer [5]). Let f : Ω → {0,1} be the function which returns 1 if and only if the label on the root is smaller than the labels on all the neighboring vertices. It is clear that with probability one the corresponding random coloring c is the characteristic function of some independent set on T. We can view c as a randomized algorithm which produces an independent set of points of density 1/(d + 1). Since the rule f has radius 1, it can also be applied to a ﬁnite d-regular graph G. Let us put random labels from [0,1] on the vertices of G, and then evaluate the rule f at each vertex using only the neighborhood of radius 1. We get a random {0,1} coloring of V (G) such that 1’s form an independent set. Such algorithms (corresponding to a rule of bounded radius) are called local algorithms. On the other hand, we can view f as the characteristic function of a single (non-random) independent set in the Bernoulli graphing G corresponding to the tree T (that is, G := Bµ where µ is the Dirac probability measure on the point T ∈ G). The vertex set of G is G[0,1], but in G almost every vertex is represented by an element in [0,1]V(T), and so we can evaluate the function f for almost every point. It is clear now that f−1(1) is an independent measurable set in G.

A general deﬁnition of factor of i.i.d. processes can be obtained through Bernoulli graphings. Let µ be an involution-invariant measure on G, and let Bµ be the corresponding Bernoulli graphing on G[0,1]. Let f : G[0,1] → [k] be a Borel function. Then the involution-invariant measure µB,f on G[k] has the property that it projects to µ when the labels on the vertices are forgotten. In other words µB,f puts a k-coloring process on the graphs generated by µ. The measure µB,f is called a factor of i.i.d. process on µ. The rule of the process is the function f. We say that the rule f has radius r if f(G1) = f(G2) whenever the balls of radius r in G1 and G2 are isomorphic as rooted labeled graphs.

We can approximate the rule f with an arbitrary precision ε with another rule f′ of ﬁnite radius

- r (which depends on ε) in the sense that ν(x|f(x) = f′(x)) ≤ ε. An advantage of the ﬁnite radius approximation is that it can be used for local algorithms on ﬁnite graphs. Let G be a ﬁnite graph


of maximal degree at most d, and let us put random labels from [0,1] on the vertices in G. Then f′ deﬁnes a new coloring of G such that the color of a vertex v is computed using f′ for the labeled neighborhood of radius r of v.

Nondeterministic property testing. The connection between the two convergence notions can be illuminated by the following algorithmic considerations. Given a (very large) graph G with bounded degree, we use the following sampling method to gain information: we select randomly and uniformly a node of G, and explore its neighborhood of radius r. We can repeat this t times. There are a number of algorithmic tasks (parameter estimation, property testing) that can be studied in this framework; we only sketch a simple version of property testing, and its connection to local-global convergence.

It will be convenient to introduce the edit distance for graphs with bounded degree. For two graphs on the same node set V (G) = V (G′), we deﬁne

1 |V (G)|

d1(G,G′) =

|E(G)△E(G′)|.

![image 34](<2012-hatami-limits-local-global-convergent-graph_images/imageFile34.png>)

For a graph property P, let P−ε = {G ∈ G : d1(G,P) > ε}.

We say that the graph property P is testable if for every ε > 0, there are integers r,t ≥ 1 such that given any graph G that is large enough, taking t samples of radius r as described above, we can guess whether the graph has property P: if G ∈ P, then our guess should be “YES” with probability

- at least 2/3; if G ∈ P−ε, then the answer should be “NO” with probability at least 2/3. If P is testable, then a locally convergent graph sequence cannot contain inﬁnitely many graphs from both


P and P−ε.

Now let us say that P is nondeterministically testable if there is an integer k ≥ 1, and a testable property Q of k-colored graphs with bounded degree, such that G ∈ P if and only if there is a k-coloring c such that (G,c) ∈ Q. This k-coloring is a “witness” for our conclusion. As an example, the property “G is the disjoint union of two graphs with at least |V (G)|/1000 nodes” is not testable, but it is nondeterministically testable (a witness is a 2-coloring with no edge between the 2 colors); so these two notions are diﬀerent (in contrast to the case of dense graphs [27]). If P is nondeterministically testable, then a local-global convergent graph sequence cannot contain inﬁnitely many graphs from both P and P−ε.

# 13 Concluding remarks

Local-global equivalence and limit representation. We have seen a characterization of local equivalence of two graphings (Proposition 7.11). Is there a similar characterization of local-global equivalence?

Does every graphing represent the limit of a local-global convergent graph sequence? This is stronger than the Aldous–Lyons conjecture, but perhaps there is a counterexample. We can mention two possible counterexamples suggested by our results.

Can a d-regular graphing be a better expander than any ﬁnite d-regular graph? Such a graphing would certainly be a counterexample. It is not easy, however, to compute the expansion rate of even very simple graphings, like the Bernoulli tree.

Is every graphing (d+1)-edge-colorable in a Borel way? If a graphing is the local-global limit of a sequence of ﬁnite simple graphs, then these graphs can be (d+1)-edge-colored by Vizing’s Theorem, and it is not hard to see that such an edge-coloring can be transferred to the limit graphing.

Even ﬁner limit notions. Limit graphings can represent even ﬁner information than local-global convergence. Consider the following examples. Let 0 < a < 1 be an irrational number, and consider the following three graphings: (a) Ca is obtained by connecting every point x ∈ [0,1] to the two points x ± a (mod 1); (b) Ca′ consists of two disjoint copies of Ca (both with measure 1/2); (c) Ca′′ is obtained by taking two copies of [0,1] (call them upper and lower), each with mass 1/2, and connecting every lower point x ∈ [0,1] to the two upper points x ± a (mod 1).

These three graphings are locally isomorphic, and either one of them represents the local-global limit of the sequence of cycles. But they are “diﬀerent”: there is no measure preserving isomorphism between them, and this has combinatorial reasons. The graphing Ca′ is “disconnected” (non-ergodic), while Ca′′ is “bipartite”: it has a partition into two sets with positive measure such that every edge connects the two classes. The graphing Ca does not have any partition with either one of these properties (even if we allow an exceptional subset of measure 0). This follows from basic ergodic theory.

It seems that the graphing Ca should represent the limit of odd cycles, Ca′ should represent the limit of graphs consisting of a pair of odd cycles, while Ca′′ should represent the limit of even cycles. This would correspond to a ﬁner ordering of graphings, where we say that say that a graphon G2 is “ﬁner” that a graphing G2 if QG

2,r,k for every r,k ≥ 1. A theory of convergence that would explain these examples has not been worked out, however.

1,r,k ⊆ QG

We know [10] that local convergence is equivalent to right-convergence where the target graph is in a small neighborhood of the looped complete graph with all edge-weights 1. Can local-global convergence be characterized by, or at least related to, some stronger form of right convergence?

# References

- [1] D. Aldous, R. Lyons: Processes on Unimodular Random Networks, Electron. J. Probab. 12, Paper 54 (2007), 1454–1508.
- [2] M. Abert, B. Weiss: Bernoulli actions are weakly contained in any free action, Ergodic theory and dynamical systems, to appear.
- [3] N. Alon: Eigenvalues and expanders, Combinatorica 6 (1986), 83–96.
- [4] N. Alon and V. D. Milman: λ1, isoperimetric inequalities for graphs and superconcentrators, J. Combinatorial Theory B 38 (1985), 73–88.
- [5] N. Alon, J. Spencer: The Probabilistic Method, Wiley–Interscience, 2000.
- [6] I. Benjamini and O. Schramm: Recurrence of distributional limits of ﬁnite planar graphs, Electronic J. Probab. 6 (2001), paper no. 23, 1–13.


- [7] I. Benjamini, O. Schramm, A. Shapira: Every Minor-Closed Property of Sparse Graphs is Testable, Advances in Math. 223 (2010), 2200–2218.
- [8] B. Bollobas, O. Riordan: Sparse graphs: Metrics and random models, Rand. Struc. Alg. 39, 1–38.
- [9] C. Borgs, J. Chayes and L. Lov´asz: Moments of Two-Variable Functions and the Uniqueness of Graph Limits, Geom. Func. Anal. 19 (2010), 1597–1619.
- [10] C. Borgs, J.T. Chayes, J. Kahn and L. Lov´asz: Left and right convergence of graphs with bounded degree, Random Struc. Alg. 42 (2013), 1–28.
- [11] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s, and K. Vesztergombi: Convergent graph sequences I: Subgraph frequencies, metric properties, and testing, Advances in Math. 219 (2008), 1801– 1851.
- [12] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s, and K. Vesztergombi: Convergent graph sequences II: Multiway Cuts and Statistical Physics, Annals of Math. 176 (1912), 151–219.
- [13] G. Elek and G. Lippner: Borel oracles. An analytical approach to constant-time algorithms, Proc. Amer. Math. Soc. 138 (2010), 2939–2947.
- [14] G. Elek: On limits of ﬁnite graphs, Combinatorica 27 (2007), 503–507.
- [15] G. Elek: The combinatorial cost, Enseign. Math. 53 (2007), 225–235.
- [16] G. Elek: Finite graphs and amenability, J. of Func. Anal. 263 (2012), 2593–2614.
- [17] G. Elek, B. Szegedy: A measure-theoretic approach to the theory of dense hypergraphs, Adv. in Math. 231 (2012), 1731–1772.
- [18] D. Gamarnik and M. Sudan: Limits of local algorithms over sparse random graphs, http: //arxiv.org/abs/1304.1831
- [19] Eli Glasner: Ergodic Theory via Joinings, Amer. Math. Soc. (2003).)
- [20] A. Hassidim, J.A. Kelner, H.N. Nguyen, K. Onak: Local Graph Partitions for Approximation and Testing, in: FOCS ’09, 50th Ann. IEEE Symp. on Found. Comp. Science (2009), 22–31.
- [21] A.S. Kechris: Global aspects of ergodic group actions, Math. Surveys and Monographs 160, Amer. Math. Soc., Providence, R.I. (2010).
- [22] A. Kechris and B.D. Miller: Topics in orbit equivalence theory, Lecture Notes in Mathematics

1852. Springer-Verlag, Berlin, 2004.

- [23] A. Kechris, S. Solecki and S. Todorcevic: Borel chromatic numbers, Advances in Mathematics 141 (1999) 1–44.
- [24] L. Lov´asz: Large networks and graph limits, Amer. Math. Soc., Providence, R.I. (2012).


- [25] L. Lov´asz, B. Szegedy: Limits of dense graph sequences, J. Comb. Theory B 96 (2006), 933–957.
- [26] L. Lov´asz, B. Szegedy: Szemer´edi’s Lemma for the analyst, Geom. Func. Anal. 17 (2007), 252–270.
- [27] L. Lov´asz, K. Vesztergombi: Nondeterministic graph property testing, Comb. Prob. and Comput.
- [28] O. Schramm: Hyperﬁnite graph limits, Elect. Res. Announce. Math. Sci. 15 (2008), 17–23.


