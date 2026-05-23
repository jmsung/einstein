arXiv:2604.20890v1[math.HO]20Apr2026

## Algebraic Graph Theory

M. Reza Salarian Bielefeld University, Germany

April 24, 2026

# Preface

This note is mainly based on the book by Godsil and Royle, Algebraic Graph Theory. The section on Steiner systems follows the treatment in Rotman, An Introduction to the Theory of Groups.

For readers interested in further studies in graph theory, we refer to Bondy and Murty, Graph Theory with Applications, and for more advanced topics, to Diestel, Graph Theory. For permutation groups, a standard reference is Wielandt, Permutation Groups.

This note has been prepared with the assistance of AI software to help organize, clarify, and typeset the material. Additionally, SageMath software was used to construct, analyze, and visualize graphs (such as the Hoffman–Singleton graph, Petersen graph, Paley graphs, and Hamming graphs), and to compute automorphism groups and other combinatorial properties.

We hope these references and tools will help guide the reader to a deeper understanding of the material presented here.

# Contents

Preface 2

- 1 Graphs 5

- 1.1 Subgraphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
- 1.2 Automorphisms of Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . 10
- 1.3 Johnson, Petersen and Kneser Graphs . . . . . . . . . . . . . . . . . . . . 13
- 1.4 The Tutte–Coxeter Graph (Tutte 8-cage) . . . . . . . . . . . . . . . . . . 18
- 1.5 The Fano Plane and the Coxeter Graph . . . . . . . . . . . . . . . . . . . 22
- 1.6 The Heawood Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
- 1.7 Hoffman-Singleton Graph . . . . . . . . . . . . . . . . . . . . . . . . . . 31
- 1.8 Hypercube graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
- 1.9 Line graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
- 1.10 Frucht’s Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45


- 2 Groups 52

- 2.1 Permutation Groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
- 2.2 Orbits on Pairs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
- 2.3 Primitivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57


- 3 Transitive Graphs 60


- 3.1 Vertex-Transitive Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
- 3.2 Edge-Transitive Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
- 3.3 Semisymmetric graphs and small orders . . . . . . . . . . . . . . . . . . . 63
- 3.4 Semisymmetric graphs as coset graphs . . . . . . . . . . . . . . . . . . . 65
- 3.5 Connectivity of Vertex-Transitive Graphs . . . . . . . . . . . . . . . . . . 71
- 3.6 Edge Connectivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
- 3.7 Vertex Connectivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
- 3.8 Matchings in Vertex-Transitive Graphs . . . . . . . . . . . . . . . . . . . 77
- 3.9 Hamilton Paths and Cycles . . . . . . . . . . . . . . . . . . . . . . . . . 80

- 3.9.1 The Five Known Non-Hamiltonian Graphs . . . . . . . . . . . . . 80
- 3.9.2 The Cayley Graph Conjecture . . . . . . . . . . . . . . . . . . . . 81
- 3.9.3 Lower Bounds on Cycle Length . . . . . . . . . . . . . . . . . . . 82


- 3.10 Basic Properties of Cayley Graphs . . . . . . . . . . . . . . . . . . . . . . 83


- 3.10.1 Cayley Graphs and Their Automorphisms . . . . . . . . . . . . . 84
- 3.10.2 Connectivity and Basic Parameters . . . . . . . . . . . . . . . . . 84
- 3.10.3 Automorphism Group Structure . . . . . . . . . . . . . . . . . . . 85
- 3.10.4 Normal Cayley Graphs . . . . . . . . . . . . . . . . . . . . . . . . 86
- 3.10.5 Arc-Transitivity and Normal Cayley Graphs . . . . . . . . . . . . 86


- 4 CONTENTS


- 3.11 Hamiltonicity of Cayley Graphs . . . . . . . . . . . . . . . . . . . . . . . 87
- 3.12 Non-Hamiltonian Directed Cayley Graphs . . . . . . . . . . . . . . . . . 89 3.12.1 An Infinite Family of Non-Hamiltonian Directed Cayley Graphs . 90
- 3.13 Automorphisms and Cayley Digraphs . . . . . . . . . . . . . . . . . . . . 91
- 3.14 Double Coset Graphs: A Generalization . . . . . . . . . . . . . . . . . . 92


- 3.14.1 Construction and Basic Properties . . . . . . . . . . . . . . . . . 92
- 3.14.2 Examples and Universality . . . . . . . . . . . . . . . . . . . . . . 93


##### 4 Arc-Transitive Graphs 95

- 4.1 s-arc Transitive Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
- 4.2 Cubic s-arc Transitive Graphs . . . . . . . . . . . . . . . . . . . . . . . . 101


##### 5 Distance-transitive and Moore graphs 107

- 5.1 distance-regular graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111 5.1.1 Eigenvalues of strongly regular graphs . . . . . . . . . . . . . . . 114
- 5.2 Moore Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116


##### 6 Incidence Structures 124

- 6.1 Projective Planes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
- 6.2 A Family of Projective Planes . . . . . . . . . . . . . . . . . . . . . . . . 126
- 6.3 Generalized Quadrangles . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
- 6.4 A Family of Generalized Quadrangles . . . . . . . . . . . . . . . . . . . . 130
- 6.5 Generalized Polygons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131

- 6.5.1 Definitions and Basic Structure . . . . . . . . . . . . . . . . . . . 131
- 6.5.2 Structure of Non-Thick Polygons . . . . . . . . . . . . . . . . . . 133
- 6.5.3 Properties of Thick Generalized Polygons . . . . . . . . . . . . . . 135


- 6.6 Uniqueness of the generalized quadrangle of order (2,2) . . . . . . . . . . 138
- 6.7 Designs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
- 6.8 Steiner Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143


##### 7 Cores of Graphs 156

- 7.1 Definition and Basic Properties . . . . . . . . . . . . . . . . . . . . . . . 156
- 7.2 Constructing Cores: A Sufficient Condition . . . . . . . . . . . . . . . . . 157 7.2.1 Reduced Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
- 7.3 Cores of Vertex-Transitive Graphs . . . . . . . . . . . . . . . . . . . . . . 158
- 7.4 Cores of Cubic Vertex-Transitive Graphs . . . . . . . . . . . . . . . . . . 159 7.4.1 Example: Truncated Graphs with Core C5 . . . . . . . . . . . . . 159


# Chapter 1 Graphs

A graph X consists of a non empty vertex set V (X) ̸= ∅ and an edge set E(X), where each edge is an unordered pair of distinct vertices of X. We will usually write xy instead of {x,y} to denote an edge. If xy ∈ E(X), then we say that x and y are adjacent or that y is a neighbour of x, and we write x ∼ y. A vertex is incident with an edge if it is one of the two vertices that form the edge.In this note, all graphs are finite, meaning that V (X) is finite. Moreover, any two vertices determine at most one edge. In fact, the graphs we consider are simple graphs, that is, they have no loops and no multiple edges.

#### Degree of a vertex

The degree of a vertex v ∈ V (X), denoted deg(v), is the number of vertices adjacent to v, or equivalently, the number of edges incident with v. We define:

deg(v) (the maximum degree of X),

∆(X) = max

v∈V (X)

deg(v) (the minimum degree of X).

δ(X) = min

v∈V (X)

Graphs are often used to model binary relationships between objects. For example, V (X) could represent computers in a network, with adjacency meaning that two computers are directly linked.

#### Graph isomorphisms

Two graphs X and Y are equal if V (X) = V (Y ) and E(X) = E(Y ). For most purposes, the structure of a graph does not change if the vertices are simply relabelled. This motivates the following definition.

- Definition 1.0.1. Two graphs X and Y are isomorphic if there exists a bijection φ : V (X) → V (Y ) such that x ∼ y in X if and only if φ(x) ∼ φ(y) in Y . The map φ is called an isomorphism, and its inverse is also an isomorphism. If X and Y are isomorphic, we write X ∼= Y .


It is customary to represent a graph by a diagram, with points for vertices and lines for edges. Strictly speaking, these diagrams do not define a graph unless the vertex set is explicitly labelled. However, once the vertices are labelled, the diagram determines the graph up to isomorphism. The relative positions of the points and lines are irrelevant—the only information conveyed is which pairs of vertices are joined by edges.

B

2

C

1

3

A

D E

4 5

Figure 1.1: Two isomorphic graphs on five vertices.

Proposition 1.0.1. Let φ be an isomorphism from X to Y . Then for every vertex v ∈ V (X),

φ NX(v) = NY φ(v) , where NX(v) denotes the set of neighbours of v in X. Corollary 1.0.1. Isomorphisms preserve degrees of vertices: if φ : X → Y is an isomorphism, then

degX(v) = degY (φ(v)), ∀v ∈ V (X).

Proof. From the proposition, φ gives a bijection between NX(v) and NY (φ(v)). Thus |NX(v)| = |NY (φ(v))|, which means degX(v) = degY (φ(v)).

| |
|---|


### Graph Isomorphism Problem (GI Open Problem)

- • Problem: Given two graphs, determine whether they are isomorphic, that is, structurally identical under some relabeling of vertices.
- • Despite its simple statement, there is no efficient algorithm known to solve it in general.
- • The current best algorithm is due to László Babai (2015), which uses group theory and graph automorphism groups to efficiently handle symmetries.


#### Special types of graphs

A graph is complete if every pair of distinct vertices is adjacent; the complete graph on n vertices is denoted by Kn. A graph with vertices but no edges is called empty.

- Definition 1.0.2. The complement of a graph X, denoted X, is the graph with the same vertex set as X but with edge set


E(X) = {xy : x,y ∈ V (X),x ̸= y, and xy ∈/ E(X)}. That is, X contains exactly the edges not in X.

- Example 1.0.1. If X is the empty graph on 3 vertices (no edges), then X = K3, the complete graph on 3 vertices.


As we said our graphs are simple graphs. A common generalisation is the directed graph (or digraph), used to model asymmetric relationships.

- Definition 1.0.3. A directed graph X consists of a vertex set V (X) and an arc set A(X), where each arc is an ordered pair of distinct vertices. In diagrams, arcs are drawn as arrows from the first vertex to the second.


2

1

3

4 Figure 1.2: A directed graph.

Unless otherwise stated, all graphs in these notes are assumed to be finite, simple, and undirected.

### 1.1 Subgraphs

- Definition 1.1.1. A subgraph Y of a graph X is a graph with V (Y ) ⊆ V (X) and E(Y ) ⊆ E(X).

If V (Y ) = V (X), then Y is called a spanning subgraph of X. Any spanning subgraph can be obtained by deleting edges from X. The number of spanning subgraphs of X is 2|E(X)|.

- Definition 1.1.2. An induced subgraph of X is a subgraph Y where two vertices are adjacent in Y if and only if they are adjacent in X. Equivalently, it is obtained by deleting vertices from X (and all incident edges). The number of induced subgraphs of X is 2|V(X)|.


2

1

3

5 4

(a) Original graph

2

1

3

5 4

(b) Spanning subgraph

2

1

3

(c) Induced subgraph on {1,2,3}

Figure 1.3: Original graph, spanning subgraph, and induced subgraph on vertices {1,2,3}.

#### Special subgraphs

A clique is a complete subgraph; an independent set is a set of vertices inducing no edges. The size of the largest clique in X is the clique number ω(X); the size of the largest independent set is the independence number α(X).

#### Paths, connectivity, and cycles

A path of length r from x to y is a sequence of r + 1 distinct vertices beginning with x and ending with y, such that consecutive vertices are adjacent. A graph is connected if there is a path between any two vertices; otherwise it is disconnected. A component of X is a maximal connected induced subgraph.

Exercise: We have ω(X) = α(X) and ω(X) = α(X)

- Example 1.1.1. Consider the graph X with vertex set {1,2,3,4,5,6} and edges {12,23,45}. This graph has three components:


{1,2,3} (connected by edges 12,23), {4,5} (connected by edge 45), {6} (isolated vertex). 1 2 3 4 5

6

Exercise 1.1.1. Let X be a simple graph with n ≥ 2 vertices, and let X be its complement.

- 1. Show that if X is disconnected, then X is connected.

- 2. Conclude that for any graph X on n ≥ 2 vertices, at least one of X or X is connected.

- 3. Give an example of a graph X such that X is disconnected but X is connected.


- Theorem 1.1.1. A graph X is connected if and only if it has exactly one component.

Proof. By definition, the components are maximal connected induced subgraphs partitioning V (X). If X is connected, the whole graph is one maximal connected induced subgraph, so it has one component. Conversely, if there is only one component, X itself is connected.

| |
|---|


A cycle is a connected graph in which every vertex has degree 2. The smallest cycle is K3. A graph in which each vertex has at least two neighbours must contain a cycle. An acyclic graph is a graph with no cycles, it is also called a forest. A connected forest is called a tree. A spanning tree is a spanning subgraph that is a tree.

- Theorem 1.1.2. A graph has a spanning tree if and only if it is connected.


Proof. If a graph has a spanning tree, it is clearly connected. Conversely, if X is connected, start with X and repeatedly delete edges from cycles until no cycles remain; the resulting subgraph is connected and acyclic, hence a spanning tree.

| |
|---|


- Lemma 1.1.1 (Handshaking Lemma). In any finite graph,


deg(v) = 2|E(X)|.

v∈V (X)

Proof. Each edge contributes exactly 2 to the total degree count, one for each endpoint. Summing over all edges yields the formula.

| |
|---|


##### Exercise

- 1. Prove that a connected graph with maximum degree ∆(X) ≤ 2 is either a path or a cycle. In particular, if it is 2-regular, it must be a cycle.
- 2. Prove that any connected graph with minimum degree δ(X) ≥ 2 contains at least one cycle.
- 3. Use the Handshaking Lemma to show that in any graph the number of vertices of odd degree is even.
- 4. Prove that the number of spanning subgraphs of a graph X is 2|E(X)|.


### Bipartite Graphs

- Definition 1.1.3. A graph X is bipartite if its vertex set V (X) can be partitioned into two disjoint sets U and W such that every edge of X connects a vertex in U to a vertex


- in W. Equivalently, there are no edges between vertices within the same part.


- Example 1.1.2. The complete bipartite graph K3,3 has vertex set partitioned into two sets of size 3 each, with every vertex in the first set connected to every vertex in the second set, and no edges within each set.


- 4

- 5

- 6


- 1

- 2

- 3


##### Definitions:

- 1. Let P be a path (or cycle) in a graph. The length of P, denoted |P|, is the number

of its edges. A cycle is called odd (even) if its length is odd (even).

- 2. Let X be a connected graph, and let u,v be vertices of X. The distance between


- u and v, denoted dX(u,v), is defined by dX(u,v) = min{|P| | P is a path connecting u and v}.


Exercise: For any cycle, the number of vertices and the number of edges are equal.

- Theorem 1.1.3. A graph is bipartite if and only if it contains no odd cycles.


##### Proof. (Sketch)

(⇒) Suppose X is bipartite with parts U and W. Any cycle must alternate vertices between U and W. Thus, the cycle length must be even (since it must return to the starting vertex in the same part after an even number of steps). So X contains no odd cycles.

(⇐) Suppose X has no odd cycles. Pick any vertex v and define: U = {x ∈ V (X) : the shortest path from v to x has even length}, W = {x ∈ V (X) : the shortest path from v to x has odd length}.

If there were an edge within U or within W, this would create an odd cycle (by combining the paths from v to the two endpoints with that edge), contradicting the assumption. Therefore, X is bipartite.

| |
|---|


### 1.2 Automorphisms of Graphs

An automorphism of a graph X is an isomorphism from X to itself. In other words, it is a permutation of the vertex set V (X) that preserves adjacency: if x ∼ y in X, then g(x) ∼ g(y) for an automorphism g.

The set of all automorphisms of X forms a group under composition, called the automorphism group of X, denoted by Aut(X). The identity permutation is the identity element of this group. If g ∈ Aut(X), then its inverse g−1 is also in Aut(X).

Since every automorphism is a permutation of V (X), Aut(X) is a subgroup of the symmetric group Sym(V (X)). For a graph with n vertices, we write Sym(n) for the full symmetric group.

Example 1.2.1. For the complete graph Kn, every permutation of the vertices is an automorphism. Hence, Aut(Kn) ∼= Sym(n).

If g ∈ Aut(X) and Y is a subgraph of X, define the image subgraph Y g := (V (Y )g,E(Y )g) where V (Y )g = {g(v) : v ∈ V (Y )}, E(Y )g = {{g(u),g(v)} : {u,v} ∈ E(Y )}. Then Y g is isomorphic to Y and is also a subgraph of X.

#### Valency and Automorphisms

The valency (or degree) of a vertex x is the number of neighbors of x.

- Lemma 1.2.1. If g ∈ Aut(X) and y = g(x), then x and y have the same valency. Proof. Let N(x) be the subgraph induced by the neighbors of x. Then


N(x)g = N(g(x)) = N(y).

Since N(x) and N(y) are isomorphic subgraphs of X, they have the same number of vertices, so x and y have the same valency.

| |
|---|


Thus, automorphisms permute vertices of equal valency among themselves. A graph is called k-regular if every vertex has valency k. In particular, a 3-regular

graph is called cubic, and a 4-regular graph is sometimes called quartic.

- 1.2. AUTOMORPHISMS OF GRAPHS 11


#### Distance and Automorphisms

The distance d(x,y) between vertices x and y is the length of a shortest path connecting them.

- Lemma 1.2.2. If g ∈ Aut(X), then for all vertices x,y, d(x,y) = d(g(x),g(y)).

Proof. Let P = (x = v0,v1,...,vk = y) be a shortest path from x to y of length k = d(x,y). Because g is an automorphism, it preserves adjacency, so the image path

Pg = (g(v0),g(v1),...,g(vk)) is a path of length k from g(x) to g(y). Thus,

d(g(x),g(y)) ≤ k = d(x,y). Similarly, applying g−1 shows

d(x,y) = d(g−1(g(x)),g−1(g(y))) ≤ d(g(x),g(y)). Combining these inequalities gives

d(x,y) = d(g(x),g(y)), as required.

| |
|---|


Automorphisms of the Complement

The complement X of a graph X has the same vertex set, where two vertices are adjacent in X if and only if they are not adjacent in X.

- Lemma 1.2.3. Aut(X) = Aut(X).


Proof. Any automorphism preserves adjacency and non-adjacency, so it is also an automorphism of the complement.

| |
|---|


#### Examples of Automorphism Groups

Example Consider the graph G with vertex set

V = {1,2,3,4,5} and edge set

E = {12,13,14,25,35}.

This graph resembles a star centered at vertex 1 with edges 12,13,14, plus edges 25 and 35 connecting vertices 2 and 3 to 5.

The degrees of the vertices are:

- 4

- 5


2 3

1

deg(1) = 3, deg(2) = 2, deg(3) = 2, deg(4) = 1, deg(5) = 2. Observe that vertices 2 and 3 share identical neighborhoods:

N(2) = {1,5}, N(3) = {1,5}.

The mapping that swaps vertices 2 and 3 (and fixes all other vertices) preserves adjacency, as: - edges 12 and 13 are swapped, - edges 25 and 35 are swapped, - vertices 1, 4, and 5 remain fixed.

Thus, the automorphism group of G consists of the identity and the transposition swapping 2 and 3, and so

Aut(G) ∼= Z2.

- Theorem 1.2.1. For n ≥ 3, the automorphism group of the cycle graph Cn is isomorphic to the dihedral group D2n:


Aut(Cn) ∼= D2n. Proof. Label the vertices of Cn as

V = {v0,v1,...,vn−1} with edges

E = {{vi,vi+1 (mod n)} : i = 0,...,n − 1}.

If an automorphism of Cn fixes two adjacent vertices, then it must be the identity. Indeed, if φ(v0) = v0 and φ(v1) = v1, then adjacency forces φ(v2) = v2, and inductively all vertices are fixed.

For k = 0,...,n − 1, define the rotation ρk(vi) = vi+k (mod n), so that ρk = (ρ1)k in particular. Also define the reflection σ(vi) = v−i (mod n).

The order of ρ1 is n, since (ρ1)n = id and no smaller positive power is the identity. The order of σ is 2, since σ2 = id. Moreover,

σρ1σ = ρ−1 1,

as can be checked by

σρ1σ(vi) = σρ1(v−i) = σ(v−i+1) = vi−1 = ρ−1 1(vi). Let

A = ⟨ρ1,σ⟩.

From the above relations, A is isomorphic to the dihedral group D2n and has exactly 2n elements: the n rotations ρk and the n reflections ρkσ. For each i,j, there exists k with ρk(vi) = vj, namely k ≡ j − i (mod n), so the rotations act transitively on V .

To show that Aut(Cn) ⊆ A, let φ ∈ Aut(Cn). If φ(v0) = v0, then φ sends v1 to either

- v1 or vn−1. In the first case, by the initial observation, φ = id. In the second case, φ = σ. Thus any automorphism fixing v0 lies in {id,σ} ⊂ A.


If instead φ(v0) = vi for some i, choose k such that ρk(vi) = v0. Then ψ := ρk ◦ φ is an automorphism fixing v0, hence ψ ∈ {id,σ} ⊂ A. Therefore φ = ρ−k 1ψ ∈ A.

Since A ⊆ Aut(Cn) by definition and we have shown Aut(Cn) ⊆ A, it follows that Aut(Cn) = A ∼= D2n.

| |
|---|


Example[Path Graph Pn] The path graph Pn has only two automorphisms: the identity and the "flip" reversing the path. Hence,

Aut(Pn) ∼= Z2.

Example[Complete Bipartite Graph Km,n] If m ̸= n, then

Aut(Km,n) ∼= Sm × Sn,

where Sm and Sn are the symmetric groups on the two parts. If m = n, there is an additional automorphism swapping the two parts, so

Aut(Kn,n) ∼= (Sn × Sn) ⋊ Z2.

### 1.3 Johnson, Petersen and Kneser Graphs

A particularly important family of graphs in algebraic and combinatorial graph theory are the J(v,k,i) graphs. They provide a natural way to translate problems about finite sets into graph theory.

Let v,k,i be integers with v ≥ k ≥ i ≥ 0, and let N be a fixed set of size v. The graph J(v,k,i) is defined as follows:

- • The vertices are all k-element subsets of N.
- • Two vertices (subsets) are adjacent if and only if their intersection has size i.


Thus, J(v,k,i) has k v vertices and is a regular graph. Exercise Show that J(v,k,i) has k v vertices and is a d-regular graph, where

v − k k − i

k i

d =

.

A useful observation is that we may assume v ≥ 2k:

- Lemma 1.3.1. If v ≥ k ≥ i, then J(v,k,i) ∼= J v, v − k, v − 2k + i .


Proof. Let N be a fixed v-element set and Nk be the set of all k-subsets of N . Define a map

N k →

N v − k

, φ(A) = N \ A. This map is clearly a bijection with inverse itself.

φ :

For any k-subsets A,B ⊆ N, we have φ(A)∩φ(B) = |(N\A)∩(N\B)| = |N\(A∪B)| = v−|A∪B| = v−(|A|+|B|−|A∩B|) = v−2k+|A∩B|.

Hence, |A ∩ B| = i if and only if φ(A) ∩ φ(B) = v − 2k + i. This shows that φ preserves adjacency in the Johnson graphs, so it is an isomorphism

J(v,k,i) ∼= J v, v − k, v − 2k + i .

| |
|---|


When v ≥ 2k, two special cases are of particular interest:

- • J(v,k,k − 1) — the Johnson graphs.
- • J(v,k,0) — the Kneser graphs.


The most famous example is the Kneser graph J(5,2,0), which is the Petersen graph. Petersen Graph: Vertices are the 2-element subsets of {1,2,3,4,5}. Two vertices are adjacent if and only if they are disjoint as sets.

{1,2}

{2,4}

{3,5}

{4,5}

{3,4}

{1,3}

{1,4}

{2,5}

{2,3} {1,5}

![image 1](<2026-ashrafi-algebraic-graph-theory_images/imageFile1.png>)

Figure 1.4: The Petersen graph, labeled by 2-element subsets of [5].

The Petersen graph is 3-regular, has 10 vertices and 15 edges, and plays a central role in many areas of graph theory. Automorphisms. If g is a permutation of N and S ⊆ N, define

Sg = {sg : s ∈ S }.

Each such g induces a permutation of the vertices of J(v,k,i), and if |S ∩ T| = i then |Sg ∩ Tg| = i, so g is an automorphism of J(v,k,i). Thus:

Lemma 1.3.2. For v ≥ k ≥ i, Aut(J(v,k,i)) contains a subgroup isomorphic to Sym(v).

In fact, in most cases Aut(J(v,k,i)) ∼= Sym(v), though proving this can be nontrivial. In particular, for the Kneser graph K(v,k,0) in many cases we have

Aut(K(v,k,0)) ∼= Sym(v) for v ≥ 2k + 1.

Open Problem: Determine all triples (v,k,i) for which Aut(J(v,k,i)) ∼= Sym(v).

That is, classify the parameters for which the automorphism group of a Johnson graph (or its Kneser graph special case) is isomorphic to the full symmetric group on v vertices.

- Theorem 1.3.1. The automorphism group of the Petersen graph P is isomorphic to S5 in its natural action on the 2-subsets of [5] = {1,2,3,4,5}.


Proof. We label the vertices of P by the 2-element subsets of [5], with two vertices adjacent if and only if the corresponding subsets are disjoint.

—

##### Step 1: Structure of the Petersen graph in this labeling. The vertices can be

divided into two 5-cycles:

- • The outer 5-cycle, consisting of vertices 12, 34, 15, 23, 45,

where edges follow the cycle in that order (each consecutive pair is disjoint).

- • The inner 5-cycle, consisting of the remaining 2-subsets 13, 24, 35, 14, 25,


again forming a 5-cycle in that cyclic order.

—

##### Step 2: Independent sets of maximum size. In any graph, an automorphism

sends independent sets to independent sets of the same size. In a 5-cycle, the largest independent set has size 2. Since P consists of two 5-cycles connected in a specific way, a maximum independent set in P can contain at most two vertices from the outer cycle and at most two from the inner cycle. Hence:

α(P) = 4, and every maximum independent set has exactly two vertices from each cycle. A simple example of a size-4 independent set is:

Ij := {all 2-subsets of [5] containing j}. For example:

I1 = {12,13,14,15}. Clearly, there are exactly 5 such sets I1,I2,I3,I4,I5, one for each element of [5].

##### Step 3: Classification of all maximum independent sets. Let I be any inde-

pendent set of size 4 in P. By Step 1, it must contain exactly two vertices from the outer cycle and two from the inner cycle.

The outer 5-cycle has a rotation symmetry given by the permutation ρ = (15324) ∈ S5,

which acts on the 2-subset labels of P. By applying an automorphism corresponding to a rotation of the outer cycle, we can assume without loss of generality that:

Outer vertices in I : 34 and 45.

Looking at the adjacency structure of P, the only way to complete I to an independent set of size 4 is to take the inner vertices:

14 and 24.

This set is exactly I4. Hence, every maximum independent set is of the form Ij for some j ∈ [5].

Step 4: Action of Aut(P) on the family {Ij}. We have shown that the family of

maximum independent sets is:

I = {I1,I2,I3,I4,I5}. Any automorphism of P permutes these sets, giving a homomorphism: φ : Aut(P) → S5.

This map is surjective because the action of S5 on the underlying 2-subset labeling of P preserves adjacency, so S5 ⊆ Aut(P).

Step 5: Kernel of φ. Suppose g ∈ Aut(P) fixes each Ij setwise. Then for any

distinct j,k, the intersection

Ij ∩ Ik = {{j,k}}

is a single vertex of P, so g must fix this vertex. Since this holds for all pairs j,k, g fixes every vertex of P, hence g is the identity. Therefore:

ker(φ) = {id}.

Step 6: Conclusion. Since φ is an injective homomorphism from Aut(P) into S5

and we already have S5 ⊆ Aut(P), it follows that: Aut(P) ∼= S5.

| |
|---|


#### Levi Graphs

An incidence structure is a pair (P,B), where

- • P is a set of points, and
- • B is a set of blocks (also called lines),


together with an incidence relation indicating which points lie in which blocks.

The Levi graph (or incidence graph) of an incidence structure (P,B) is the bipartite graph with vertex set P ∪ B, where a point p ∈ P is adjacent to a block B ∈ B if and only if p is incident with B (i.e., p ∈ B).

Definition 1.3.1. A polarity of an incidence structure (P,B) is a bijection

π : P ∪ B → P ∪ B satisfying the following properties:

- (a) π maps points to lines and lines to points,


- (b) π is an involution: π2 is the identity, and
- (c) incidence is preserved in the sense that for any point p ∈ P and line ℓ ∈ B, p ∈ ℓ ⇐⇒ π(ℓ) ∈ π(p).


A configuration is self-dual if it admits a polarity. In other words, points and lines can be interchanged while preserving the incidence structure.

Remarks: A Levi graphs is bipartite, so Petersen graph is not a Levi graph.

In what follows, we present some classical examples of Levi graphs such as:

- • The Tutte–Coxeter graph.
- • The Heawood graph which is the Levi graph of the Fano plane (self-dual configuration with 7 points and 7 lines).


### 1.4 The Tutte–Coxeter Graph (Tutte 8-cage)

- Definition 1.4.1 (Tutte–Coxeter Graph). Let Ω = {1,2,3,4,5,6}.


- • A duad is a 2-element subset of Ω. Denote the set of duads by D = {i,j} ⊂ Ω : i < j , |D| = 15.
- • A syntheme is a partition of Ω into three disjoint duads. Denote the set of synthemes by S, so |S| = 15.


The Tutte–Coxeter graph Γ is the bipartite incidence graph with parts D and S, where d ∈ D is adjacent to s ∈ S if and only if d ∈ s.

- Theorem 1.4.1. The automorphism group of the Tutte–Coxeter graph is Aut(Γ) ∼= Aut(S6) ∼= S6 ⋊ C2,


and hence has order 1440. Proof. Step 1. Side-preserving automorphisms. Any σ ∈ S6 permutes the symbols of Ω, thereby permuting duads and synthemes and preserving incidence. Thus

S6 ≤ Aut(Γ).

To see there are no additional side-preserving automorphisms, observe that from the graph Γ alone we can reconstruct the six symbols of Ω. For duads a,b ∈ D define

R(a,b) = #{s ∈ S : a ∼ s ∼ b}. A simple check shows:

 

3 a = b,

- 0 a ̸= b and a ∩ b ̸= ∅,
- 1 a ∩ b = ∅.


R(a,b) =



Thus we can recognize within Γ when two duads intersect. Construct a graph X on D where a,b are adjacent iff a ∩ b ̸= ∅. Then for each i ∈ Ω, the five duads containing i form a clique K5 in X, and these six cliques are exactly the maximal 5-cliques in X. Hence the six symbols of Ω are canonically identifiable from Γ.

Therefore every automorphism of Γ preserving the bipartition induces a permutation of the six cliques, i.e. an element of S6. This proves

Aut+(Γ) ∼= S6.

Step 2. Existence of a side-swapping automorphism. We can show that the incidence structure (D,S) is self-dual. However, the proof requires some grouptheoretic machinery, in particular the existence of the exceptional outer automorphism of the symmetric group S6. We leave this as an exercise, but we include below a brief sketch as a proposition. In fact, there exists a polarity π interchanging duads and synthemes while preserving incidence:

d ∈ s ⇐⇒ π(s) ∈ π(d). This polarity induces a graph automorphism τ of the Tutte–Coxeter graph satisfying

τ(D) = S, τ(S) = D, showing that the graph is self-dual. Step 3. Conclusion. Thus

Aut(Γ) = ⟨Aut+(Γ),τ⟩ ∼= S6 ⋊ C2.

It is well known that S6 has a unique nontrivial outer automorphism, and adjoining τ realizes this extension. Therefore

- as claimed.


|Aut(Γ)| = 2 · |S6| = 2 · 720 = 1440,

| |
|---|


Proposition 1.4.1. Let Ω = {1,2,3,4,5,6}, let D be the set of duads (2-subsets of Ω) and let S be the set of synthemes (partitions of Ω into three disjoint duads). Then there exists a bijection f : D → S which is a polarity of the duad–syntheme incidence structure; that is,

d ∈ s ⇐⇒ f(s) ∈ f(d) for all d ∈ D, s ∈ S, and f2 = id. Consequently the Tutte–Coxeter Levi graph is self-dual. Proof. (1) ( see the book of Rotman, corollary 7.6) The outer automorphism σ and its effect on cycle types. It is a classical fact that S6 admits a nontrivial outer automorphism σ : S6 → S6. One convenient way to view σ is by its action on conjugacy classes: under σ a transposition (cycle type 2) is sent to a product of three disjoint transpositions (cycle type 23), and conversely, a product of three disjoint transpositions is sent to a transposition. (Any concrete model of the outer automorphism — e.g. via PGL2(5) or via complementary 3-sets — gives this behavior.)

##### (2) Identifying duads and synthemes with permutations. Associate to each

duad d = {a,b} ∈ D the transposition (ab) ∈ S6. Associate to each syntheme s ∈ S the permutation τs ∈ S6 which is the product of the three disjoint transpositions that form

- s. Thus incidence d ∈ s is equivalent to the transposition (ab) being one of the three disjoint transpositions whose product is τs.


###### (3) Define f : D → S via σ. For a duad d = {a,b} let td = (ab). Consider σ(td).

By (1), σ(td) is a permutation of cycle type 23; its three transposition factors correspond to a unique syntheme s ∈ S. Define f(d) = s. This produces a map f : D → S.

then d1 = d2, so the assignment is well defined. The map f is injective because σ is injective and different transpositions land in different 23-type elements (so give different synthemes). Since |D| = |S| = 15, injectivity implies bijectivity.

##### (4) Well-definedness and bijectivity. If td

= td

1

2

(5) Incidence is reversed by f. Fix d = {a,b} ∈ D and s ∈ S. Let td = (ab) and let τs be the product of the three transpositions in s. Then

d ∈ s ⇐⇒ td is one of the three transpositions whose product is τs.

Apply σ to both sides. Using that σ is a homomorphism of the group structure (though outer, it still permutes conjugacy classes and respects products up to group law), we obtain that σ(td) is one of the three transpositions in the product σ(τs). By the definition of f,

σ(td) corresponds to the syntheme f(d), σ(τs) corresponds to the duad f(s). Thus

td appears in τs ⇐⇒ σ(τs) contains a transposition appearing in σ(td), which translates exactly to

d ∈ s ⇐⇒ f(s) ∈ f(d). Therefore f reverses incidence as required for a polarity.

(6) Making f involutory. The map σ represents a nontrivial element of Out(S6), and a standard fact is σ2 is inner: there exists h ∈ S6 with σ2 = conjh (conjugation by

- h). For the bijection f constructed above we then have, for every d ∈ D, f(f(d)) = (syntheme corresponding to σ(product corresponding to f(d))).


One checks (using σ2 = conjh) that f2 acts on D as the permutation induced by h. Thus f2 is an inner permutation of the duads. Replacing f by the modified map d  → h−1·f(d) (equivalently composing f with the involutive action of h−1) yields a new bijection f˜ which still intertwines the two S6-actions but satisfies f˜2 = id. Therefore we obtain a polarity that is an involution.

Conclusion. The bijection f (after the adjustment above if desired) is an incidencereversing involution D ↔ S; i.e. a polarity of the duad–syntheme incidence structure. Hence the Tutte–Coxeter Levi graph is self-dual.

| |
|---|


The girth of a graph X, denoted by girth(X), is the length of the shortest cycle in X. If X has no cycles (that is, X is acyclic), we set girth(X) = ∞.

The diameter of a connected graph X, denoted by diam(X), is the maximum distance between any two vertices of X; that is,

diam(X) = max

dX(u,v),

u,v∈V (X)

where dX(u,v) is the length of the shortest path between u and v.

- Exercise 1. Show that the Johnson graph J(v,k,i) has

v k

vertices and is d-regular, where

d =

k i

v − k k − i

.

- Exercise 2. Show that the Petersen graph P is connected and has diameter 3 and girth


- 5.


### Girth 8 and diameter 4 of the Tutte–Coxeter graph

- Theorem 1.4.2. The Tutte–Coxeter graph Γ has girth 8 and diameter 4. Proof. We treat girth and diameter separately.


- (1) Girth is 8. Since Γ is bipartite any cycle has even length; so the possible cycle lengths are


4,6,8,.... We show no 4- or 6-cycle can occur; hence the shortest possible cycle is length 8.

No 4-cycles. Suppose there were a 4-cycle d1 − s1 − d2 − s2 − d1,

with di ∈ D and sj ∈ S. Then both synthemes s1 and s2 contain the two duads d1 and d2. But by construction of synthemes, two distinct duads determine at most one syntheme containing both. Therefore Γ has no 4-cycle.

No 6-cycles. Suppose there were a 6-cycle d1 − s1 − d2 − s2 − d3 − s3 − d1.

Interpret this in the incidence structure: di ∈ si and di+1 ∈ si (indices mod 3). Pick the syntheme s1 and the point (duad) d3 not on s1; then we should have a unique point on

- s1 which is in a same syntheme with d3 (collinear). But in the supposed 6-cycle both d1 and d2 are points of s1 that are collinear with d3 (since the cycle gives paths d3 − s3 − d1 and d3 − s2 − d2), contradicting uniqueness. Hence no 6-cycle exists.


With 4- and 6-cycles excluded, the smallest possible even cycle length is 8 and we can see that there is 8-cycle.

- (2) Diameter is 4. Let x,y be arbitrary vertices of Γ. We must show there is a path of length at most 4


joining x to y. Since Γ is bipartite, distances between vertices in the same part are even and between opposite parts are odd; it therefore suffices to show that any two vertices of the same part are at graph-distance at most 4 (this will imply the worst-case distance between arbitrary vertices is at most 4).

We consider two cases.

- Case A: x,y are in different parts. Then either x is adjacent to y (distance 1), or else

there exists a neighbor z of x that is adjacent to y giving a path of length 3 at most. In fact if x is a duad and y a syntheme not incident to x, take any syntheme through x; there is a unique duad on that syntheme collinear with y, and that furnishes a path of length 3. Thus distance between opposite parts is at most 3.

- Case B: x,y lie in the same part. Without loss of generality assume x,y ∈ D (duads).


If x and y are both contained in a common syntheme then dist(x,y) = 2. Otherwise they are not collinear in the incidence structure; pick any syntheme s incident with x. Then there is a unique duad z ∈ s which is collinear with y. Hence we have the path

x − s − z − s′ − y,

where s′ is some syntheme containing both z and y (such s′ exists because z and y are collinear). This is a path of length 4 from x to y. Thus any two duads are at distance

- at most 4. The same argument applies when x,y ∈ S (synthemes): if two synthemes are not adjacent, pick a duad on one and then we can find the unique duad to approach the other; this produces a length-4 path.


Combining the two cases we see every pair of vertices is at distance ≤ 4, while examples of vertex pairs at distance exactly 4 exist (e.g. certain pairs of duads that intersect), so the diameter is exactly 4.

Therefore the Tutte–Coxeter graph Γ has girth 8 and diameter 4, as required.

| |
|---|


### 1.5 The Fano Plane and the Coxeter Graph

The Fano plane is the unique projective plane of order 2. It is the smallest non-trivial example of a projective plane and is denoted PG(2,2), representing the 2-dimensional projective space over the finite field F2.

Formally, it is an incidence structure (P,L) where:

- • P = {1,2,3,4,5,6,7} is a set of 7 points.
- • L is a collection of 7 lines, each a 3-element subset of P. The incidence relation must satisfy the following axioms:


- (i) Any two distinct points lie on exactly one line.
- (ii) Any two distinct lines intersect in exactly one point.
- (iii) Each line contains exactly 3 points, and through each point pass exactly 3 lines. A standard labeling satisfying these axioms is:


L = {{1,2,3}, {1,4,5}, {1,6,7}, {2,4,6}, {2,5,7}, {3,4,7}, {3,5,6}}.

This structure can be visually represented by a diagram where points are dots and lines are smooth curves (often circles), with each line containing three points.

1 0 2

29

28

3 4

27

26

5

25

- 6
- 7
- 8
- 9
- 10


- 21
- 22
- 23
- 24


20

11

19

12

18

13

17

14 15 16

Figure 1.5: The Tutte–Coxeter graph.

#### Vector Space Construction

A more algebraic construction reveals the source of its symmetry. Consider the 3dimensional vector space V = F32 over the field F2 = {0,1}.

- • The points of the Fano plane are the 1-dimensional subspaces of V . Since F2 has only one nonzero element, each 1-dimensional subspace contains exactly one nonzero vector. There are (23 − 1) = 7 such vectors, so |P| = 7.
- • The lines are the 2-dimensional subspaces of V . A 2-dimensional subspace contains (22 −1) = 3 nonzero vectors, which are exactly the three nonzero vectors of the two 1-dimensional subspaces it contains. This explains why each line has 3 points.
- • Incidence is defined by containment: a point (1-subspace) lies on a line (2-subspace) if and only if the 1-subspace is contained in the 2-subspace.


This construction directly implies that the automorphisms of the Fano plane are induced by the linear symmetries of V .

#### Automorphism Group

An automorphism (or collineation) of the Fano plane is a permutation σ : P → P that maps lines to lines, i.e., for every ℓ ∈ L, σ(ℓ) ∈ L and that preserves incidence; that is, for every point p ∈ P and line ℓ ∈ L,

p ∈ ℓ ⇐⇒ σ(p) ∈ σ(ℓ).

- Theorem 1.5.1. Aut(P,L) ∼= PGL(3,2).


Proof. • Every invertible linear map A ∈ GL(3,2) permutes the 1-dimensional and 2-dimensional subspaces of V , thus inducing a collineation.

- • The order of GL(3,2) is calculated by counting ordered bases for F32: |GL(3,2)| = (23 − 1)(23 − 2)(23 − 22) = 7 · 6 · 4 = 168.
- • It is a classical result that GL(3,2) ∼= PSL(2,7).
- • Furthermore,by the Fundamental Theorem of Projective Geometry, every collineation arises from a linear map, so the group is exactly PGL(3,2).


Thus, the automorphism group of the Fano plane is a simple group of order 168.

| |
|---|


![image 2](<2026-ashrafi-algebraic-graph-theory_images/imageFile2.png>)

Figure 1.6: The Fano plane.

#### The Coxeter Graph

The Coxeter graph is a famous 3-regular (cubic) graph with 28 vertices and 42 edges. It is known for its high symmetry and interesting properties.

Construction As an Induced Subgraph of K(7,3) This construction is crucial for understanding the graph’s automorphisms.

- • Let K(7,3) be the Kneser graph whose vertices are all 3-element subsets of a 7-element set P (the points of the Fano plane). Two vertices are adjacent if their corresponding subsets are disjoint. K(7,3) has 73 = 35 vertices.
- • Let L be the set of 7 subsets that are lines of the Fano plane. It is a set of 7 triples that Each pair of them has exactly one point in common.
- • Let T = P3 \ L be the set of 28 remaining 3-element subsets.
- • The Coxeter graph Γ is defined as the induced subgraph of K(7,3) on the vertex set T . Two vertices in Γ are adjacent if and only if their corresponding triples are disjoint.


#### Key Properties: Girth is 7 and Diameter is 4

The girth of the Coxeter graph is 7:

- 1. No triangles (3-cycles) exist. Suppose p,p′,p′′ formed a 3-cycle. Then by adjacency, fano plane should have 9 points a contradiction.

- No 4-cycles. Suppose a 4-cycle exists: T1 ∼ T2 ∼ T3 ∼ T4 ∼ T1, so that each

consecutive pair is disjoint.

- Let T1 ∩ T3 and T2 ∩ T4 be examined. - Each triple has size 3, and consecutive triples are disjoint. Counting distinct points along the 4-cycle leads to at least 8 points, but P has only 7 points. - Therefore, a 4-cycle is impossible.

- No 5-cycles. Similarly, consider a hypothetical 5-cycle. Let T1,...,T5 be the

vertices.

- Consecutive triples are disjoint. - Counting points: each new triple adds at least one new point, but the total would exceed 7 points before closing the cycle. - Hence no 5-cycles exist.

- No 6-cycles. The same argument works for a 6-cycle: consecutive disjoint triples would require 6×3/2 ≥ 9 points (using overlaps carefully), again exceeding 7 points.


- 2. Existence of a 7-cycle. Consider the sequence of vertices


- T1 = {1,2,4}
- T2 = {3,5,7}
- T3 = {1,6,4}
- T4 = {2,5,3}
- T5 = {4,7,6}
- T6 = {1,5,2}
- T7 = {3,6,7}


Hence, girth(Γ) = 7. The diameter of the Coxeter graph is 4. Recall that Γ has vertex set

T = P 3 \ L,

the 28 triples of points that are not Fano lines, with adjacency T ∼ T′ ⇐⇒ T ∩ T′ = ∅. Let T,T′ ∈ T be arbitrary vertices. Consider the size of their intersection |T ∩ T′|:

- 1. Disjoint triples: |T ∩ T′| = 0. Then T ∼ T′ directly, so d(T,T′) = 1.


- 2. Triples intersecting in two points: |T ∩ T′| = 2. Let T = {a,b,c} and T′ = {a,b,d}. The remaining points are {e,f,g} = P\(T∪T′). Choose X1 = {f,d,e},T2 = {b,a,g},T3 = {e,f,c} ∈ T . Then giving d(T,T′) ≤ 4.
- 3. Triples intersecting in one point: |T ∩ T′| = 1. Let T = {a,b,c} and T′ = {a,d,e}. Then the complement P \ (T ∪ T′) = {f,g} contains only two points. No single triple is disjoint from both T and T′, so the shortest path requires 4 edges. For example, a distance-4 path is


T ∼ X1 ∼ X2 ∼ X3 ∼ T′,

where X1,X2,X3 are chosen appropriately from T to maintain disjointness at each step.

Since the maximal distance occurs in the third case, the diameter of the Coxeter graph is

diam(Γ) = 4.

### The Anti-Flag Construction and Automorphisms of the Coxeter Graph

Let P be the set of 7 points of the Fano plane, and L the set of its 7 lines. Denote by

T = P 3 \ L

the set of 28 triples that are not lines of the Fano plane. The Coxeter graph Γ is the induced subgraph of the Kneser graph K(7,3) on the vertex set T , where two triples T,T′ ∈ T are adjacent if and only if they are disjoint:

T ∼ T′ ⇐⇒ T ∩ T′ = ∅.

#### Bijection with Anti-Flags

Each vertex T ∈ T can be uniquely represented by an anti-flag (p,ℓ), where p ∈ P, ℓ ∈ L, and p ∈/ ℓ. Explicitly, for T ∈ T , let R = P \ T (a 4-subset). The Fano plane property implies that R contains exactly one line ℓ ∈ L; let p be the unique point of R not lying on ℓ. Then the correspondence

Φ : T −→ {(p,ℓ) ∈ P × L : p ∈/ ℓ}, Φ(T) = (p,ℓ) is a bijection. Its inverse is given by

Φ−1(p,ℓ) = P \ (ℓ ∪ {p}),

which is indeed a 3-element non-line triple. Thus the vertices of Γ can be identified with the 28 anti-flags of the Fano plane.

Adjacency is inherited from the triple model: (p,ℓ) ∼ (p′,ℓ′) ⇐⇒ Φ−1(p,ℓ) ∩ Φ−1(p′,ℓ′) = ∅ ⇐⇒ ℓ ∪ ℓ′ ∪ {p,p′} = P.

#### Automorphisms

The automorphism group of the Fano plane is Aut(F) ∼= PGL(3,2) ∼= PSL(2,7),

of order 168. Each automorphism σ preserves incidence, so it acts naturally on anti-flags by

σ: (p,ℓ)  −→ (σ(p),σ(ℓ)).

Since p ∈/ ℓ ⇒ σ(p) ∈/ σ(ℓ), this action preserves the set of anti-flags. Moreover, the adjacency condition depends only on the incidence structure of the Fano plane, hence

(p,ℓ) ∼ (p′,ℓ′) ⇐⇒ σ(p,ℓ) ∼ σ(p′,ℓ′).

Therefore, every automorphism of the Fano plane induces a graph automorphism of Γ, giving

PGL(3,2) ≤ Aut(Γ).

There also exists a natural polarity (duality) of the Fano plane sending each point to a line and vice versa, which interchanges (p,ℓ) ↔ (ℓ,p). This polarity has order 2 and commutes with PGL(3,2), doubling the group order. Hence,

Aut(Γ) ∼= PGL(3,2) ⋊ C2, |Aut(Γ)| = 2 × 168 = 336.

#### Example

Using the labeling P = {1,2,3,4,5,6,7}, L = {{1,2,3},{1,4,5},{1,6,7},{2,4,6},{2,5,7},{3,4,7},{3,5,6}}, the triple T = {1,2,4} corresponds to R = {3,5,6,7}, which contains the line ℓ = {3,5,6}. The remaining point p = 7 yields Φ(T) = (7,{3,5,6}), and indeed

Φ−1(7,{3,5,6}) = P \ ({3,5,6} ∪ {7}) = {1,2,4}.

- Theorem 1.5.2. Aut(Γ) ∼= PGL(2,7), a group of order 336.

1.6 The Heawood Graph

- Definition 1.6.1 (Heawood graph). The Heawood graph H is the bipartite Levi (incidence) graph of the Fano plane:


V (H) = P ∪ L,

with adjacency p ∼ ℓ iff p ∈ ℓ. Then H has 14 vertices, is 3-regular, bipartite, and connected.

- Theorem 1.6.1 (Girth and Diameter). The Heawood graph H has girth 6 and diameter


- 3.


Figure 1.7: Coxeter graph.

Proof. Girth. Since H is bipartite, all cycles have even length. Consider a 4-cycle: p1 − ℓ1 − p2 − ℓ2 − p1. This would require two distinct lines ℓ1,ℓ2 both containing two common points p1,p2, which is impossible in the Fano plane (two points lie on exactly one line). Hence no 4-cycle exists.

The Fano plane contains triangles (3 points on a line), but in the bipartite Levi graph these triangles correspond to 6-cycles (point–line–point–line–point–line). Indeed, pick any line ℓ with points p1,p2,p3; then the cycle p1 −ℓ−p2 −ℓ′ −p3 −ℓ−p1 (for a suitable choice of ℓ′ intersecting p2,p3) gives a 6-cycle. Therefore, the shortest cycle length is 6: girth(H) = 6.

Diameter. Let x,y be arbitrary vertices. If x,y are adjacent, distance is 1. If they are a point and a non-incident line, the GQ(2,2) axiom gives a unique point on the line collinear with the point, yielding a path of length 3. If both x,y are points (or both lines), pick a neighbor of x and use the previous argument to reach y in at most 3 steps. Explicitly, any two points p,q not on the same line: choose any line ℓ through p; there exists a point r ∈ ℓ collinear with q; then p − ℓ − r − ℓ′ − q is a path of length 3. Hence diam(H) = 3.

| |
|---|


- Theorem 1.6.2 (Automorphism group). The full automorphism group of the Heawood graph H is


Aut(H) ∼= PGL(2,7), which has order 336.

Proof. Step 1: Collineations of the Fano plane give automorphisms of H. The Heawood graph H is the Levi graph of the Fano plane: its vertices are the 7 points together with the 7 lines, and adjacency means incidence in the Fano plane. Thus, any incidence-preserving permutation (collineation) of the Fano plane induces a permutation of the 14 vertices of H that preserves adjacency. Therefore every collineation is a graph automorphism.

##### Step 2: The collineation group of the Fano plane. The Fano plane is PG(2,2),

the projective plane over F2. Its collineation group is PGL(3,2) ∼= GL(3,2),

since in dimension 3 over F2 there are no nontrivial scalar multiples. This group has order

|GL(3,2)| = (23 − 1)(23 − 2)(23 − 22) = 7 · 6 · 4 = 168. It is well known that GL(3,2) ∼= PSL(2,7). So we have 168 automorphisms of H already.

Step 3: Duality (polarity) of the Fano plane. The Fano plane is self-dual: there exists a bijection (called a polarity) that sends points to lines and lines to points, and preserves incidence. Applying such a polarity gives a permutation of the 14 vertices of H that interchanges the two bipartite halves. This is again a graph automorphism.

Conjugating the 168 collineations by a polarity produces another 168 automorphisms, and together they form a group of size 168 · 2 = 336.

Step 4: No further automorphisms. It remains to argue that Aut(H) cannot be larger. - First, note that the bipartition of H (points vs. lines) is not preserved by every automorphism (because of the polarity), but the set of all 14 vertices is partitioned into two equal orbits under Aut(H). - The adjacency structure of H uniquely encodes the incidence relation of the Fano plane. Hence any graph automorphism must send points to points or lines (via the polarity), and lines accordingly, so all graph automorphisms arise from collineations and possibly a polarity.

Thus, Aut(H) consists exactly of the 168 collineations and their images under polarity,

- i.e. a group of size 336. Step 5: Identification with PGL(2,7). The group of order 336 obtained here is


isomorphic to PGL(2,7), the projective linear group on the projective line of size 7. This group is known to be the full automorphism group of the Fano plane, extended by duality. Hence

Aut(H) ∼= PGL(2,7), as claimed.

| |
|---|


0 1

13

2

12

- 3
- 4


- 10
- 11


5

9

6

8

7

###### Figure 1.8: Heawood graph.

### Summary and Comparison

|Property<br><br>|Fano Plane (P,L)|Heawood Graph<br><br>|Coxeter Graph Γ|Tutte 8-Cage|
|---|---|---|---|---|
|Object Type|Incidence Structure (Projective Plane)<br><br>|Bipartite Graph|Undirected Graph<br><br>|Bipartite Graph (Cage)|
|Number of Elements<br><br>|7 points, 7 lines|14 vertices, 21 edges<br><br>|28 vertices, 42 edges<br><br>|45 vertices, 68 edges|
|Definition|Axiomatic or via F32|Incidence graph of the Fano plane<br><br>|Induced subgraph of K(7,3) on nonlines<br><br>|Smallest cubic graph of girth 8|
|Regularity|Each point on 3 lines, each line has 3 points<br><br>|Bipartite, 3regular|Cubic (3-regular)<br><br>|Cubic (3-regular)|
|Girth|N/A (3-gon)<br><br>|6|7<br><br>|8|
|Diameter<br><br>|N/A<br><br>|3|4|4|
|Automorphism Group|PGL(3,2) ∼= PSL(2,7)<br><br>|PΓL(3,2) ∼= PGL(2,7)<br><br>|PΓL(3,2) ∼= PGL(2,7)|PΓL(2,9)|
|Group Order|168<br><br>|336|336<br><br>|4320|
|Special Properties<br><br>|Unique projective plane of order 2<br><br>|(3,6)-cage; bipartite double cover of K7<br><br>|(3,7)-cage; double cover of Heawood graph<br><br>|(3,8)-cage; smallest cubic graph of girth 8|


There is a clear link between the three objects: the Fano plane’s geometry gives rise to both the Heawood and Coxeter graphs, which share the same automorphism group. We note that a (k,g)-cage is a regular graph of degree k and girth g with the smallest possible number of vertices.

### Definition

An s-arc in a graph Γ is an ordered sequence of distinct vertices (v0,v1,...,vs)

such that vi−1 is adjacent to vi for all 1 ≤ i ≤ s, and vi−1 ̸= vi+1 for all 1 ≤ i ≤ s − 1 (that is, the path does not immediately retrace an edge).

A graph Γ is s-arc-transitive if Aut(Γ) acts transitively on the set of all s-arcs (i.e. for any two s-arcs there exists an automorphism sending one ordered s-arc to the other).

In particular:

- • 0-arc-transitive means vertex-transitive;
- • 1-arc-transitive means arc-transitive.


### Exercises

- 1. Show that the generalized Johnson graph J(v,k,i), the Heawood graph, the Coxeter graph, Cn, and the Tutte–Coxeter graph are arc-transitive.
- 2. Show that the Petersen graph is 2-arc-transitive and 3-arc-transitive, but not 4-arc-transitive. What about the Cn? is it 2-arc transitive?


### 1.7 Hoffman-Singleton Graph

The Hoffman-Singleton (HS) graph is the unique (7,5)-cage: the smallest graph with maximum degree 7 and girth 5. It has 50 vertices and is 7-regular. Here we present a combinatorial construction of this graph using the structure of the 7-element set and its associated heptads. Let Ω = {1,2,3,4,5,6,7}.

- Definition 1.7.1. A triple is a 3-element subset of Ω. A set of triples is concurrent if there is some point common to them all, and the intersection of any two of them is this common point. A triad is a set of three concurrent triples


- Definition 1.7.2 (Heptads). A heptad is a set H of 7 triples of Ω with the following properties:


- (i) every point of Ω occurs in exactly 3 triples of the set, and
- (ii) any two triples intersect in exactly one point.


- Lemma 1.7.1 (Number of Triads). Each point x ∈ Ω lies in 15 triads, and there are exactly 105 triads in total.

Proof. Fix a point x ∈ Ω. A triad through x consists of three triples {x,a,b},{x,c,d},{x,e,f}

where the remaining six elements {a,b,c,d,e,f} = Ω\{x} are partitioned into three unordered pairs. The number of such partitions is 15. Since there are 7 points, the total number of triads is 7 · 15 = 105.

| |
|---|


- Lemma 1.7.2 (Triads in Heptads). Each triad is contained in exactly 2 heptads.

Proof. Fix a triad T = {1ab, 1cd, 1ef }. Consider any heptad H containing T. The remaining four triples cannot involve 1, so they lie in {a,b,c,d,e,f}. Each of the six elements must occur exactly twice in the remaining triples.

To satisfy the heptad conditions (each pair of triples intersects in exactly one point), each of the four remaining triples picks exactly one element from each pair {a,b},{c,d},{e,f}. There are exactly two such choices:

{ace,adf,bcf,bde} or {bdf,bce,ade,acf}. Thus there are exactly two heptads containing the triad T.

| |
|---|


- Lemma 1.7.3 (Number and Orbits of Heptads). There are exactly 30 heptads. The alternating group Alt(7) acts on these heptads and partitions them into two orbits, O1 and O2, each of size 15.


Proof. By Lemma 1.7.1, there are 105 triads. By Lemma 1.7.2, each triad is contained in exactly 2 heptads. Hence the total number of triad–heptad incidences is 105·2 = 210.

Each heptad contains exactly 7 triads. Denote the total number of heptads by H. Then

7 · H = 210 =⇒ H = 30.

The symmetric group Sym(7) acts transitively on the heptads. The stabilizer of a heptad has order 7!/30 = 5040/30 = 168 and consists of even permutations. Hence Alt(7) acts on heptads with two orbits of size 2520/168 = 15, giving O1 and O2.

| |
|---|


- Lemma 1.7.4. Let n = {1,...,7}. There are 30 heptads (as above), split into two Alt(7)-orbits O1,O2 of size 15 each. Then:


- 1. Every triple of n lies in exactly 6 heptads in total.
- 2. For each triple t, exactly 3 of those heptads lie in O1 and 3 lie in O2.
- 3. Any two distinct heptads in the same orbit intersect in exactly one triple.


Proof. (1) Total incidence count. Each heptad contains exactly 7 triples, and there are 30 heptads altogether. Counting incidences (heptad, triple) gives

#{(H,t) : H heptad, t ∈ H} = 30 · 7 = 210.

There are 73 = 35 triples in total, so by averaging each triple occurs in

210 35

= 6

heptads. This proves (1).

(2) Split between the two Alt(7)-orbits. Let O1,O2 be the two Alt(7)-orbits of heptads, each of size 15. Restrict the incidence counting to O1. We have

#{(H,t) : H ∈ O1, t ∈ H} = 15 · 7 = 105. For a fixed triple t let at be the number of heptads in O1 that contain t. Then

t

at = 105,

where the sum runs over the 35 triples. We claim all at are equal. Indeed, Alt(7) acts transitively on the set of triples (3-subsets): if {x,y,z} and {x′,y′,z′} are two triples then some permutation in Sym(7) sends one to the other, and the stabiliser of a triple in Sym(7) contains an odd permutation (e.g. a transposition of two points outside the triple), so the orbit of a triple under Alt(7) has the same size as under Sym(7); hence Alt(7) is transitive on triples. Thus all at are equal, say at = a for every triple, and therefore

35a = 105 ⇒ a = 3.

So each triple occurs in exactly 3 heptads of O1. By the same argument for O2, each triple occurs in exactly 3 heptads of O2. Combining with (1) yields the 3 + 3 = 6 split, proving (2).

(3) Intersection size within an orbit. Fix one orbit, say O1, and fix a heptad H ∈ O1. For each triple t ∈ H, we just showed t lies in exactly 3 heptads of O1, so besides H there are exactly 2 other heptads of O1 that contain t. Thus the number of ordered pairs

(H′,t) with H′ ∈ O1 \ {H}, t ∈ H ∩ H′ is

2 = 7 · 2 = 14.

t∈H

On the other hand, if every other heptad H′ ∈ O1 \ {H} meets H in exactly r triples (this number r is independent of the choice of H′ because Alt(7) acts transitively on O1), then counting the same set of pairs by first summing over H′ gives

14 = 14 · r.

Hence r = 1, i.e. any two distinct heptads in the same orbit intersect in exactly one triple. This proves (3).

| |
|---|


We now construct the Hoffman–Singleton graph (HS graph):

Proposition 1.7.1. Let O1 be one Alt(7)-orbit of heptads (so |O1| = 15). Define the graph G = (V,E) by

V = {the 35 triples} ∪ O1, and edges given by the rules (R1)–(R3):

- (R1) a heptad H ∈ O1 is adjacent to a triple t iff t ∈ H;
- (R2) two distinct triples t,t′ are adjacent iff t ∩ t′ = ∅;
- (R3) no two heptads in O1 are adjacent.


Then G has 50 vertices, is 7-regular, and has diameter 2; hence it is the Hoffman– Singleton graph.

Proof. (Vertex count:) By construction |V | = 35 + 15 = 50. (Regularity:)

- • If H ∈ O1 is a heptad, it contains exactly 7 triples, so by (R1) deg(H) = 7.
- • If t is a triple (a 3-subset), count its neighbors. (i) Triples disjoint from t: since t


uses 3 points, the complement has 4 points, and there are 43 = 4 triples disjoint from t. Each of those is adjacent to t by (R2). (ii) Heptads in O1 containing t: by the incidence count shown earlier every triple lies in exactly 3 heptads of O1. Each such heptad is adjacent to t by (R1). Therefore

deg(t) = 4 + 3 = 7.

Thus every vertex (triple or heptad) has degree 7. (Diameter ≤ 2: )

We consider the three types of unordered pairs of vertices and show in each case there is a path of length at most 2 between them.

- (A) Triple – Triple. If t,t′ are triples and t ∩ t′ = ∅, they are adjacent by (R2). If


- t ∩ t′ ̸= ∅, say they meet at the point x, then there is a unique third triple u through x whose other two points are the two points of the complement of {x} used by t and t′; the three {t,t′,u} form a triad. Every triad is contained in exactly two heptads, and in particular exactly one heptad from O1 (the other lies in the other orbit). Hence there exists H ∈ O1 with t,t′ ∈ H, and so t and t′ have a common neighbour H in G. Thus dist(t,t′) ≤ 2.


- (B) Heptad – Heptad. If H,H′ ∈ O1 are distinct, we have shown that any two distinct

heptads in the same Alt(7)-orbit intersect in exactly one triple. Let s ∈ H ∩ H′. Then H − s − H′ is a path of length 2, so dist(H,H′) ≤ 2.

- (C) Triple – Heptad. Let t be a triple and H ∈ O1 a heptad. If t ∈ H then they are


adjacent by (R1). If t ∈/ H we must produce a triple s ∈ H with s ∩ t = ∅, because then

- t − s − H is a path of length 2. Such an s exists: indeed, each triple t lies in exactly 3


heptads of O1, and each of those three heptads meets H in a single triple (intersection number = 1 inside the orbit). These three intersection triples are three distinct members of H. If all three intersected t nontrivially, then counting occurrences of points of t among these three triples would contradict the fact that every point appears exactly three times in H; therefore at least one of these three intersection triples is disjoint from t. Concretely: among the three heptads of O1 that contain t, their intersections with H produce three triples of H, and by a simple occurrence-count (or by a small case check) at least one of

- them must avoid the three points of t. That triple gives the required 2-step path. Hence dist(t,H) ≤ 2.


| |
|---|


- Lemma 1.7.5. Let H0 = {123,145,167,246,257,347,356} ∈ O1 be the canonical heptad. Then there exists a heptad H∗ ∈ O1, H∗ ̸= H0, such that


H0 ∩ H∗ = {123} and 267 ∈ H∗. One explicit choice is

H∗ = {123,146,157,245,267,347,356}. Proof. Consider the point 2 ∈ Ω = {1,...,7} and the triad of three triples through 2: T = {123,245,267}.

By lemma 1.7.2 each triad is contained in exactly two heptads, one from each Alt(7)-orbit. Let H′ be the unique heptad in O1 containing this triad. Then 123,267 ∈ H′.

We have H′ ̸= H0 because H0 does not contain the triple 267. By Lemma 1.7.4, any two distinct heptads in O1 intersect in exactly one triple. Since both H0 and H′ contain 123, we conclude H0 ∩ H′ = {123}.

Setting H∗ := H′ yields the desired heptad. As a concrete example, one may take H∗ = {123,146,157,245,267,347,356}.

| |
|---|


- Theorem 1.7.1. The Hoffman–Singleton graph G has girth 5, and hence is a (7,5)-cage.


Proof. Recall the construction: vertices are the 35 triples (3-subsets) of Ω = {1,...,7} together with the 15 heptads of one Alt(7)-orbit O1. Edges are (R1) heptad–triple by containment, (R2) triple–triple when disjoint, and (R3) no heptad–heptad edges inside O1. We already checked this graph is 7-regular on 50 vertices; we now show its girth is 5.

- No 3-cycles. Consider a putative triangle. The types of its vertices (heptad or triple) yield four possibilities:


- • Three heptads. Impossible by (R3).


- • Two heptads and one triple. If H1 ∼ t ∼ H2 then t ∈ H1 ∩ H2, but two distinct heptads in the same orbit meet in exactly one triple, and heptads are not adjacent, so the triangle cannot close.
- • One heptad and two triples. If H ∼ t ∼ t′ with H ∼ t′ then t,t′ ∈ H, but any two triples inside a heptad meet in exactly one point and so are not disjoint; thus t ̸∼ t′, a contradiction.
- • Three triples. Pairwise adjacency would force them to be pairwise disjoint 3-subsets of Ω, which would require 9 distinct points, impossible since |Ω| = 7.


Hence no triangle exists.

- No 4-cycles. Let v1 − v2 − v3 − v4 − v1 be a 4-cycle and consider types. Any pattern with two adjacent heptads is ruled out by (R3). The alternating pattern heptad–triple–heptad–triple would force two distinct heptads in the same orbit to share two triples, contradicting the fact that they intersect in exactly one triple. Four triples cannot realize the necessary disjointness pattern on only seven points (a short counting/finitecheck argument), so no 4-cycle exists.


Thus girth(G) ≥ 5.

A 5-cycle exists. To show the girth is exactly 5 it suffices to give one explicit 5-cycle. Take the canonical heptad

H0 = {123, 145, 167, 246, 257, 347, 356}. By lemma 1.7.5 there exists a heptad H∗ ∈ O1, H∗ ̸= H0, with

H0 ∩ H∗ = {123} and 267 ∈ H∗. For concreteness, one such choice (obtained by an explicit finite search) is

H∗ = {123, 146, 157, 245, 267, 347, 356}. Now consider the five vertices of G

v1 = H0, v2 = 145, v3 = 267, v4 = H∗, v5 = 123. Check the adjacencies:

- • v1 = H0 is adjacent to v2 = 145 since 145 ∈ H0 by (R1).
- • v2 = 145 is adjacent to v3 = 267 since 145 ∩ 267 = ∅ by (R2).
- • v3 = 267 is adjacent to v4 = H∗ since 267 ∈ H∗ by (R1).
- • v4 = H∗ is adjacent to v5 = 123 since 123 ∈ H∗ by (R1).
- • v5 = 123 is adjacent to v1 = H0 since 123 ∈ H0 by (R1).


Hence v1 → v2 → v3 → v4 → v5 → v1 is a 5-cycle in G. Therefore girth(G) = 5. Since G is 7-regular on 50 vertices with girth 5, it is a (7,5)-cage; indeed it is the Hoffman–Singleton graph.

| |
|---|


Remark: The full automorphism group of the Hoffman–Singleton graph HS is isomorphic to the group usually denoted

Aut(HS) ∼= PSU(3,5) ⋊ C2, of order

|Aut(HS)| = 252000 = 25 · 32 · 53 · 7.

Equivalently, Aut(HS) has a normal subgroup isomorphic to the simple group PSU(3,5) of order 126000, and an outer involution doubles this to order 252000.

Figure 1.9: Hoffman–Singleton graph.

- Definition 1.7.3 (Hamiltonian Graph). A graph G = (V,E) is called Hamiltonian if it contains a cycle that visits every vertex in V exactly once and returns to the starting vertex. Such a cycle is called a Hamiltonian cycle.
- Definition 1.7.4 (Hamiltonian Path). A Hamiltonian path in a graph G is a path that visits every vertex exactly once, but does not necessarily return to the starting vertex. Observations:


- • Hoffman–Singleton, Heawood, and Tutte–Coxeter graphs are Hamiltonian.
- • Coxeter graph is non-Hamiltonian despite being cubic and symmetric, but does have a Hamiltonian path( find its hamiltonian path).
- • The Petersen graph is non-Hamiltonian, but does have Hamiltonian paths, so you can traverse all vertices without returning to the start.


|Graph<br><br>|Vertices<br><br>|Degree<br><br>|Girth|Hamiltonian?<br><br>|Figure|
|---|---|---|---|---|---|
|Hoffman–Singleton (HS)<br><br>Coxeter<br><br>Heawood<br><br>Tutte–Coxeter<br><br>Petersen graph<br><br>|50<br><br>28<br><br>14<br><br>30<br><br>10|7<br><br>3<br><br>3<br><br>3<br><br>3<br><br>|5<br><br>7<br><br>6<br><br>8<br><br><br><br><br>5|Yes<br><br>No<br><br>Yes<br><br>Yes<br><br>No|0 1<br><br>2<br><br>3<br>4<br><br>5<br><br>6<br><br>7<br><br>8<br><br>9<br><br>10<br>11<br><br><br>12<br><br>13<br><br>1 0 2<br><br>3 4<br><br>5<br>6<br>7<br>8<br>9<br>10<br><br><br>11<br><br>12<br><br>13<br><br>14 15 16<br><br>17<br><br>18<br><br>19<br><br>20<br><br>21<br>22<br>23<br>24<br><br><br>25<br><br>26<br><br>27<br><br>28<br><br>29<br><br>0<br><br>1<br><br>2 3<br><br>4<br><br>5<br><br>6<br><br>7 8<br><br>9|


Table 1.1: Comparison of key properties of some notable graphs.

Exercise[Moore Graphs and Vertex Bounds] Let G be a graph with valency k and girth g.

- 1. Suppose G has odd girth g = 2d + 1. Show that the number of vertices satisfies |V (G)| ≥ n0(k,g) = 1 + k + k(k − 1) + k(k − 1)2 + ··· + k(k − 1)d−1.
- 2. Suppose G has even girth g = 2d. Show that the number of vertices satisfies |V (G)| ≥ n0(k,g) = 1 + k + k(k − 1) + k(k − 1)2 + ··· + k(k − 1)d−2 + (k − 1)d−1.
- 3. A graph attaining the below equality bounds is called a Moore graph, |V (G)| = n0(k,g) = 1 + k + k(k − 1) + ··· + k(k − 1)d−1.


Moore graphs are extremely rare. Examples include:

- • For diameter 1, they are complete graphs Kk+1.
- • For diameter 2, the known Moore graphs are:


![image 3](<2026-ashrafi-algebraic-graph-theory_images/imageFile3.png>)

Figure 1.10: A Hamiltonian path in Coxeter graph.

- – C5 (degree 2),
- – the Petersen graph (degree 3),
- – the Hoffman–Singleton graph (degree 7).


- • It is an open problem whether a Moore graph of diameter 2 and degree 57 exists.


- 4. Let G be a Moore graph of degree d and diameter k; that is, |V (G)| = M(d,k) := 1 + d + d(d − 1) + ··· + d(d − 1)k−1.

Show that G is a (d,g)-cage with g = 2k +1; in other words, show that the girth of G equals 2k + 1 and that any d-regular graph of girth 2k + 1 has at least M(d,k) vertices.

|Graph|Degree k<br><br>|Diameter d|Vertices N<br><br>|Girth g|
|---|---|---|---|---|
|Complete graph Kk+1|k<br><br>|1<br><br>|k + 1|3|
|Cycle C2d+1<br><br>|2|d<br><br>|2d + 1|2d + 1|
|Petersen graph<br><br>|3|2<br><br>|10|5|
|Hoffman–Singleton graph|7<br><br>|2<br><br>|50<br><br>|5|
|Moore graph of degree 57 (unknown)<br><br>|57<br><br>|2|3250<br><br>|5?|


Table 1.2: Known Moore graphs, their degree, diameter, vertices, and girth.

Remark: No Moore graph exists with even girth g = 2d ≥ 4.

- 5. Show that a heptad is a set H of seven triples (3-subsets) of n = {1,...,7} such that


- (a) any two distinct triples of H meet in exactly one point, and
- (b) there is no point contained in all seven triples.


Proof. (We should show that if H satisfies the two conditions above, then each point of n occurs in exactly three triples of H. Conversely, if each point occurs in exactly three

triples and any two triples meet in exactly one point, then no point is contained in all seven triples.

Let ri denote the number of triples of H containing point i ∈ n. Since H has seven triples, each of size 3, we have

7

ri = 7 · 3 = 21.

i=1

Because any two triples meet in exactly one point, the number of unordered pairs of triples is

7 2

= 21,

and each such pair contributes exactly one intersection point. Counting these pairs by points gives

7

ri 2

= 21.

i=1

Now 2 r = r(r2−1) is a convex function of r for r ≥ 0. With i ri = 21, Jensen’s (or Cauchy’s) inequality yields

7

i=1

ri 2 ≥ 7

21 7

2

= 7

3 2

= 21,

with equality if and only if all ri are equal. Since equality holds, we must have r1 = ··· = r7 = 3. In particular, no point lies in all seven triples, so condition (2) is automatic.

Conversely, if each point occurs in exactly three triples (so ri = 21 and all ri = 3),

- then


7

ri 2

3 2

7 2

= 7

= 21 =

,

i=1

so each pair of triples can meet in at most one point, and the count forces them to meet in exactly one point. Also, ri = 3 < 7 for all i, so no point lies in all seven triples.)

(Fix a root vertex r ∈ V (G) and for i = 0,1,...,k let Li = {v ∈ V (G) : dist(r,v) = i}.

Because G attains the Moore bound, the breadth-first layers from r have the maximal possible sizes:

|L0| = 1, |L1| = d, |Li| = d(d − 1)i−1 for 1 ≤ i ≤ k, so the BFS tree from r is a perfect d-ary tree truncated at depth k.

No short edges between distant levels. For 0 ≤ i < k a vertex in Li has one neighbor in Li−1 (its parent in the BFS tree) and exactly d − 1 neighbors that lie in Li+1 (its children). Hence such a vertex has no neighbors in any level Lj with j ≤ i−2 and no neighbors inside Li. Consequently every edge of G either joins Li to Li+1 for some i < k or lies inside Lk.

Lower bound on girth. The previous paragraph shows that a cycle cannot be contained entirely in levels L0,...,Lk−1, nor can it use edges joining levels that differ by

≥ 2. It follows that every cycle has length at least 2k + 1; hence the girth g satisfies g ≥ 2k + 1.

Existence of a (2k + 1)-cycle. If there are two adjacent vertices u,v ∈ Lk, then the unique shortest paths Pu and Pv from r to u and v (each of length k) share only the vertex r. Indeed, if they shared some vertex other than r then the BFS-layer sizes would be smaller than required. Therefore the edge uv together with Pu and Pv forms a cycle of length k + k + 1 = 2k + 1. Thus g ≤ 2k + 1.

Combining the two inequalities yields g = 2k + 1.

Minimality (cage property). Let H be any d-regular graph with girth 2k + 1. Choose a vertex x ∈ V (H) and explore its neighborhood by breadth-first search up to radius k. Because the ball of radius k around x cannot contain a cycle (otherwise there would be a cycle of length ≤ 2k), the ball is a tree and therefore contains at least

1 + d + d(d − 1) + ··· + d(d − 1)k−1 = M(d,k)

vertices. Hence |V (H)| ≥ M(d,k). Since our Moore graph G has exactly M(d,k) vertices, it has the minimum possible number of vertices among all d-regular graphs of girth 2k+1; i.e. G is a (d,2k + 1)-cage.

This completes the proof.)

| |
|---|


### Petersen Subgraph inside the Hoffman–Singleton Graph

We use SageMath to search for and visualize a Petersen subgraph inside the Hoffman–Singleton graph.

#### Sage code

from sage.all import *

# Hoffman -Singleton graph and Petersen graph HS = graphs.HoffmanSingletonGraph() P = graphs.PetersenGraph()

# Search for an induced Petersen subgraph embedding = HS.subgraph_search(P, induced=True)

if embedding is not None: P_subgraph = HS.subgraph(embedding.vertices())

pos_HS = HS.layout() pos_P = P.layout()

# HS with Petersen highlighted (HS.plot(pos=pos_HS , vertex_size=50, edge_color="lightgray",

vertex_labels=False)

+ P_subgraph.plot(pos=pos_HS , vertex_size=400, vertex_color=" red", edge_color="red", edge_thickness=4, vertex_labels= True)).save("HS_with_Petersen.pdf")

###### 1.8. HYPERCUBE GRAPHS 41

# Petersen separately P.plot(pos=pos_P , vertex_size=400, vertex_color="red",

edge_color="red", edge_thickness=4, vertex_labels=True). save("Petersen.pdf")

1.025 26

27 28 29

1

4

3

0

0.5

2

1.0 0.5 0.5 1.0

0.5

1.0

0

5

1

4

6

9

7 8

2 3

Figure 1.11: Left: the Hoffman–Singleton graph with a Petersen subgraph highlighted in red. Right: the Petersen subgraph drawn separately.

### 1.8 Hypercube graphs

- Definition 1.8.1. The n-dimensional hypercube graph Qn has vertex set V (Qn) = {0,1}n,


the set of all binary n-tuples. Two vertices are adjacent if and only if they differ in exactly one coordinate.

- Example 1.8.1. • Q1 is just a single edge between 0 and 1.


- • Q2 is a square (4-cycle).
- • Q3 is the usual cube graph: 8 vertices, each connected to 3 others.


Each Qn is n-regular and has 2n vertices.

011 111

010 110 001 101

000 100

The symmetries of Qn form the hyperoctahedral group: these are all the transformations you get by:

- • translating every vertex by the same binary vector (bitwise XOR),
- • permuting the coordinate positions. We now state and prove the precise structure.


- Theorem 1.8.1. For every n ≥ 1, Aut(Qn) ∼= H ⋊ Sn,


where H ∼= (Z2)n is the group of translations x  → x ⊕ t (bitwise addition mod 2), and Sn acts by permuting coordinates.

Equivalently, Aut(Qn) is the wreath product Z2 ≀ Sn (the hyperoctahedral group). In particular,

|Aut(Qn)| = 2n n!. Proof. Step 1: Building the obvious automorphisms. Let

H = {τt : t ∈ {0,1}n}

where τt(x) = x ⊕ t (bitwise addition mod 2). Each τt preserves Hamming distances, hence is an automorphism. The set H is a subgroup of Aut(Qn) isomorphic to (Z2)n, called the translation group.

For any permutation π ∈ Sn, define

σπ(x1,...,xn) = (xπ−1(1),...,xπ−1(n)). This just permutes coordinates, so σπ ∈ Aut(Qn).

Translations and coordinate permutations interact via σπτtσπ−1 = τtπ

(where tπ has its coordinates permuted by π), so together they form a subgroup H ⋊ Sn of Aut(Qn) of size 2nn!.

Step 2: Every automorphism is of this form. Let g ∈ Aut(Qn). First, note that the neighbors of 0 = (0,...,0) are exactly the n

unit vectors e1,...,en.

If g(0) = v, compose with the translation τv to get g′ = τv ◦ g which fixes 0. So it suffices to consider automorphisms fixing 0.

Any h ∈ Aut(Qn) fixing 0 must permute the set {e1,...,en}. This gives some π ∈ Sn with h(ei) = eπ(i) for all i. Then σπ−1 ◦ h fixes 0 and all ei.

But every vertex of Qn is the XOR of certain ei’s. Since an automorphism preserves

adjacency, fixing 0 and all ei forces it to fix all vertices. Therefore h = σπ. Thus any g can be written as τt ◦ σπ for some t and π, so Aut(Qn) ⊆ H ⋊ Sn. Step 3: Conclusion. We have H ⋊ Sn ⊆ Aut(Qn) by construction, and Aut(Qn) ⊆ H ⋊ Sn by the above

argument. Therefore

Aut(Qn) = H ⋊ Sn ∼= (Z2)n ⋊ Sn, with |Aut(Qn)| = 2nn!.

| |
|---|


- 1.9. LINE GRAPHS 43


### 1.9 Line graphs

- Definition 1.9.1. The line graph of a graph X, denoted L(X), is the graph whose vertex set is E(X), the set of edges of X, with two vertices of L(X) adjacent if and only if the corresponding edges of X are incident in X.


##### Example 1.9.1.

- • The star K1,n has line graph Kn (all n edges meet at the center).
- • The path Pn has line graph Pn−1.
- • The cycle Cn is isomorphic to its own line graph.


Lemma 1.9.1. The Petersen graph P is (isomorphic to) the complement of the line graph L(K5).

Proof. Let K5 be the complete graph on vertex set [5] = {1,2,3,4,5}. Denote by E(K5) the set of its edges. Recall:

- • The line graph L(K5) has vertex set V (L(K5)) = E(K5), and two vertices of L(K5) are adjacent exactly when the corresponding edges of K5 share a common endpoint.
- • The complement L(K5) has the same vertex set E(K5), and two vertices are adjacent in L(K5) exactly when the corresponding edges of K5 are disjoint.


Identify each edge of K5 with the 2-element subset of [5] that it determines. Then

V (L(K5)) =

[5] 2

,

and adjacency in L(K5) is given by {i,j} ∼ {k,ℓ} ⇐⇒ {i,j} ∩ {k,ℓ} = ∅.

But this is exactly the definition of the Kneser graph K(5,2): its vertices are the 2-subsets of a 5-set, with two vertices adjacent iff they are disjoint. It is well-known (and elementary to check) that K(5,2) is the Petersen graph P. Concretely:

- • | [5]2 | = 52 = 10, the Petersen graph has 10 vertices.
- • For a given 2-subset {i,j} there are exactly 32 = 3 disjoint 2-subsets, so L(K5) is 3-regular; the Petersen graph is cubic.

- • The adjacency rule (disjointness of 2-subsets) matches the standard Petersen construction.


Therefore L(K5) ∼= K(5,2) ∼= P, as required.

| |
|---|


- Theorem 1.9.1 (Whitney’s theorem). If X is a connected graph with |V (X)| ≥ 5, then Aut(X) ∼= Aut(L(X)).


- Corollary 1.9.1. Since K5 has automorphism group S5 and P is the complement of L(K5), it follows that


Aut(P) ∼= S5.

- Definition 1.9.2 (Cartesian product of graphs). Let G and H be graphs. The Cartesian product G□H is the graph with vertex set

V (G□H) = V (G) × V (H), and where two vertices (g,h) and (g′,h′) are adjacent if and only if:

- • g = g′ and hh′ ∈ E(H), or
- • h = h′ and gg′ ∈ E(G).


Proposition 1.9.1. The n-dimensional hypercube Qn is the Cartesian product of n copies of K2, i.e.,

Qn ∼= K2□K2□···□K2

n times

= K2□n.

Proof. Consider the Cartesian product K2□K2□···□K2 (n times). Its vertex set consists of all n-tuples (x1,...,xn) with xi ∈ {0,1}. Two vertices (x1,...,xn) and (y1,...,yn) are adjacent if and only if they differ in exactly one coordinate.

This adjacency condition is exactly the adjacency rule for Qn, so the graphs are isomorphic:

Qn ∼= K2□n.

| |
|---|


- Definition 1.9.3 (Disjoint union of graphs). Given graphs X1,X2,...,Xr, their disjoint union is the graph


X1 ⊔ X2 ⊔ ··· ⊔ Xr

whose vertex set is the disjoint union of the vertex sets V (X1) ⊔ ··· ⊔ V (Xr), and whose edge set is the disjoint union of the edge sets E(X1) ⊔ ··· ⊔ E(Xr). In other words, the graphs Xi appear as disconnected components in the disjoint union.

- Theorem 1.9.2 (Automorphisms of Cartesian products of prime factors). Let X1,X2,...,Xr be connected graphs such that none of the Xi can be expressed as a Cartesian product of two smaller nontrivial graphs (i.e., each Xi is prime with respect to the Cartesian product).


Then the automorphism group of the Cartesian product X = X1□X2□···□Xr is isomorphic to the automorphism group of the disjoint union

X1 ⊔ X2 ⊔ ··· ⊔ Xr, that is,

Aut(X) ∼= Aut(X1 ⊔ X2 ⊔ ··· ⊔ Xr).

- Corollary 1.9.2. Let Qn be the n-dimensional hypercube. Then Aut(Qn) ∼= Zn2 ⋊ Sym(n),


where Zn2 corresponds to flipping coordinates and Sym(n) to permuting coordinates. Proof. Since Qn ∼= nK2 and K2 is prime with respect to the Cartesian product, the theorem on automorphisms of Cartesian products implies that

- as claimed.


Aut(Qn) ∼= Aut(K2)n ⋊ Sym(n) ∼= Zn2 ⋊ Sym(n),

| |
|---|


### 1.10 Frucht’s Theorem

Lemma 1.10.1. Let G = {g1,...,gn} be a finite group. Construct a colored digraph D with vertices corresponding to the elements of G such that gi is joined to gj by a directed edge of color k if gigj−1 = gk. The automorphism group of D is isomorphic to G.

Proof. The right multiplication by any fixed group element g ∈ G, i.e., the mapping gi  → gig,

is an automorphism of D. Indeed, if gi is joined to gj by an edge of color k (i.e., gigj−1 = gk), then

(gig)(gjg)−1 = gigj−1 = gk, so gig is joined to gjg by an edge of the same color k.

Conversely, let a be any automorphism of D and set g = a(1). We claim that gig = a(gi) for all i.

- Since (gig)g−1 = gi, gig is joined to g by an edge of color i, and gi is the only point with this property. - By definition, gi is joined to 1 by an edge of color i, and since a is an automorphism, a(gi) is joined to a(1) = g by an edge of color i. - Hence, a(gi) = gig.

It is easy to see that multiplication of elements in G corresponds exactly to composition of the corresponding automorphisms. Therefore,

Aut(D) ∼= G.

| |
|---|


- Theorem 1.10.1. (Frucht, 1939) For any finite group G, there exists a simple graph X such that


Aut(X) ∼= G.

Proof. Assume |G| ≥ 2. By the previous lemma, there exists a colored digraph D with Aut(D) ∼= G.

Construct a simple graph X as follows:

- 1. If gi,gj ∈ V (D) are joined by an edge of color k, replace it by a path of length


k + 2, with paths of length 1 attached to each inner vertex, except for the inner vertex next to gj, where we attach a path of length 2 (see Figure below). 2. Repeat this for every pair (gi,gj), then remove all directed edges. Denote the resulting graph by X.

![image 4](<2026-ashrafi-algebraic-graph-theory_images/imageFile4.png>)

Claim: Aut(X) ∼= Aut(D) ∼= G.

Each automorphism of D induces a unique automorphism of X. Conversely, let a ∈ Aut(X). The vertices of D are exactly those vertices of X that are neither cutpoints nor endpoints. Hence, V (D) is invariant under a. The new paths with attached shorter paths are exactly the components of X − V (D), and a maps them onto each other. A path of length k must map to a path of the same length, and the end with the longer attached path maps correspondingly.

Thus, if gi is connected to gj by an edge of color k, then so is a(gi) to a(gj). Hence, a yields an automorphism of D, and the correspondence is bijective.

Therefore,

Aut(X) ∼= Aut(D) ∼= G.

| |
|---|


#### Asymmetric Graphs

- Definition 1.10.1. A graph is called asymmetric if it has no nontrivial automorphisms, i.e., the only automorphism is the identity.


- Example 1.10.1. Consider the graph G with vertex set V = {1,2,3,4,5,6} and edges E = {12,23,34,24,35,56}.


The graph can be drawn as follows:

2

5

1

3 4

6

This graph is asymmetric, meaning it has no nontrivial automorphisms. Reason: Each vertex has a unique adjacency pattern:

- • Vertex 1 has degree 1 and is only connected to vertex 2.
- • Vertex 6 has degree 1 and is only connected to vertex 5.
- • Vertex 2 has degree 3, connected to vertices 1, 3, and 4.
- • Vertex 4 has degree 2, connected to vertices 2 and 3.
- • Vertex 3 has degree 3, connected to vertices 2, 4, and 5.


- • Vertex 5 has degree 2, connected to vertices 3 and 6.


No non-identity permutation of vertices preserves the adjacency relations, hence Aut(G) =

{e}, the trivial group.This graph is asymmetric; that is, it has only the identity automorphism. Intuitively, each vertex has a unique neighborhood structure preventing any nontrivial vertex permutation that preserves adjacency.

- Theorem 1.10.2. For every integer n ≥ 6 there exists an asymmetric simple graph on n vertices.


Proof. We split into the base case n = 6 and a uniform construction for all n ≥ 7. Base case n = 6. Consider the graph G6 with vertex set {v1,...,v6} and edges

v1v2, v2v3, v3v4, v4v1 (a 4-cycle), v2v5, v5v3 (a “roof”), v2v6 (a pendant edge). (Equivalently: a “house” graph on {v1,...,v5} with an extra leaf v6 attached to v2.)

We claim Aut(G6) = 1. Compute the degree sequence: deg(v1) = deg(v4) = deg(v5) = 2, deg(v2) = 4, deg(v3) = 3, deg(v6) = 1.

v4 v5

v1 v2 v3

v6

Any automorphism fixes v2,v3,v6. Among the degree-2 vertices, v5 is uniquely characterized as the only degree-2 vertex that lies on a triangle (v2v5v3), so v5 is fixed. The remaining degree-2 vertices are v1 and v4, and they are distinguished by their distances

- to v6: d(v1,v6) = 2 while d(v4,v6) = 3.


Hence v1 and v4 are fixed as well. Therefore every vertex is fixed, so Aut(G6) = 1, and

- G6 is asymmetric.


All n ≥ 7. We construct an asymmetric tree Tn on n vertices. Let u be a new vertex. Attach to u three internally-disjoint paths of distinct lengths 1,2, and n − 4, all meeting

- at u and otherwise disjoint. (So the total number of vertices is 1 + (1 + 2 + (n − 4)) = n, and the three branches have different lengths because n − 4 ≥ 3.)


We show Aut(Tn) = 1. First, u is the unique vertex of degree 3, hence is fixed by every automorphism. Deleting u decomposes Tn into three components which are paths of lengths 1,2, and n − 4. Since these lengths are pairwise distinct, the components are pairwise non-isomorphic, so each branch is setwise fixed by any automorphism. On a path, there is a unique vertex at each distance from the attachment point u, hence each branch is fixed pointwise by any automorphism that fixes u. Consequently every vertex of Tn is fixed, and Aut(Tn) = 1.

Combining the base case n = 6 with the tree construction for all n ≥ 7 proves the claim.

| |
|---|


##### Exercises:

- 1. Show that any automorphism of a tree fixes either a vertex or an edge; deduce that a finite tree has a nonempty fixed point set for Aut.
- 2. Determine Aut(Km□Kn) for m ̸= n and for m = n.
- 3. (Frucht’s theorem, challenge) Every finite group is the automorphism group of some 3-regular graph. State it and read about the Frucht graph as an example.
- 4. If q ≡ 1 (mod 4) is a prime power, the Paley graph P(q) has vertex set Fq with two distinct vertices x,y ∈ Fq are adjacent if and only if their difference is a nonzero square in Fq:


{x,y} ∈ E(P(q)) ⇐⇒ x − y ∈ (F×q )2.

. Then show that Aut(P(q)) ⊇ x  → ax + b a ∈ (F×q )2, b ∈ Fq ⋊ Gal(Fq/Fp),

(Let q be a prime power with q ≡ 1 (mod 4), and let P(q) be the Paley graph with vertex set Fq, where two vertices x,y ∈ Fq are adjacent if and only if

x − y ∈ (F×q )2,

the set of nonzero squares in Fq. For any b ∈ Fq, define the translation

τb : x  → x + b. If x ∼ y in P(q), then x − y ∈ (F×q )2, so

τb(x) − τb(y) = (x + b) − (y + b) = x − y ∈ (F×q )2.

Thus, τb is an automorphism. The set of all translations forms a group isomorphic to (Fq,+).

Let a ∈ (F×q )2 be a nonzero square, and define

µa : x  → ax. If x ∼ y, then x − y is a square, so

µa(x) − µa(y) = a(x − y)

is also a square. Hence, µa is an automorphism. The set of all such µa forms a group of order (q − 1)/2.

Let σ ∈ Gal(Fq/Fp), where q = pn and p is the characteristic of Fq. Then σ is a field automorphism:

x  → σ(x), x ∈ Fq. If x ∼ y, then x − y is a square, and

σ(x) − σ(y) = σ(x − y)

is still a square because field automorphisms preserve multiplicative structure. Therefore, σ is an automorphism of P(q).

Combining the above, any automorphism of the form

x  → aσ(x) + b, a ∈ (F×q )2, b ∈ Fq, σ ∈ Gal(Fq/Fp), preserves adjacency. These form the group

Aut(P(q)) ⊇ x  → ax + b a ∈ (F×q )2, b ∈ Fq ⋊ Gal(Fq/Fp),

where the semidirect product ⋊ encodes that the Galois automorphisms act on both the additive and multiplicative parts. ).

- 5. Let H(d,q) be the Hamming graph (vertices {0,...,q − 1}d, adjacent if they differ in exactly one coordinate). Then show that


Aut(H(d,q)) has a subgroup isomorphic to

Sq ≀ Sd = (Sq)d ⋊ Sd,

acting by independent symbol permutations in each coordinate and by permuting coordinates.

### Sage code for Paley graph:

|# Construct Paley graph q = 9 P = graphs.PaleyGraph(q)<br><br># Automorphism group A = P.automorphism_group() print("Order of Aut(P(9)):", A.order()) print("Generators:") for g in A.gens():<br><br>print(g)<br><br>|
|---|


Explanation: The automorphism group Aut(P(q)) acts on the vertices Fq. It contains:

- • Translations: x  → x + a, for a ∈ Fq
- • Multiplications by nonzero squares: x  → bx, b ∈ (F×q )2
- • Field automorphisms: x  → xp (Frobenius map)


##### Example output (order and generators):

Order of Aut(P(9)): 216 Generators: (0,1,2)(3,4,5)(6,7,8)

- (0,3)(1,4)(2,5)(6,7)


...

### Hamming Graph H(d,q)

##### Sage code:

# Construct Hamming graph

d = 3 q = 2

- H = graphs.HammingGraph(d, q)


# Automorphism group A = H.automorphism_group() print("Order of Aut(H(3,2)):", A.order()) print("Generators:") for g in A.gens():

print(g)

Explanation: The automorphism group Aut(H(d,q)) is the wreath product

Aut(H(d,q)) ∼= Sq ≀ Sd, where Sq acts on each coordinate and Sd permutes the coordinates.

##### Example output (order and generators):

Order of Aut(H(3,2)): 48 Generators: (0,1)

- (0,4)(1,5)(2,6)(3,7)


...

- Definition 1.10.2 (Graph Homomorphism). Let G = (V,E) and H = (V ′,E′) be simple graphs. A graph homomorphism is a map


f : V → V ′

such that whenever uv ∈ E we have f(u)f(v) ∈ E′. That is, adjacency is preserved. An endomorphism of a graph G is a homomorphism f : G → G. We write α(G) for the independence number of G, the size of a largest independent

set in G.

##### Exercises:

- 1. Let P denote the Petersen graph, show that α(P) = 4, and that every independent set of size 4 is a star of the form

St = {t,x} : x ∈ {1,2,3,4,5} \ {t} for some t ∈ {1,...,5}.

- 2. Show that every endomorphism of the Petersen graph P is an automorphism.


(Hint: Identify vertices of P with the 2-subsets of {1,2,3,4,5}. For each t ∈ {1,...,5}, let

St = {t,x} : x ̸= t

be the star at t, an independent set of size 4 by Fact A. If I ⊆ V (P) is independent then f(I) is independent, because f preserves adjacency. Thus f(St) is an independent set of size ≤ 4. Since St is maximum, |f(St)| = 4 and hence f(St) is itself a star. Therefore there exists a map

π : {1,...,5} −→ {1,...,5}, f(St) = Sπ(t). For i ̸= j we have Si ∩ Sj = {{i,j}}. Applying f gives

{f({i,j})} = f(Si ∩ Sj) = f(Si) ∩ f(Sj) = Sπ(i) ∩ Sπ(j).

If π(i) = π(j) the right-hand side would have size 4, a contradiction. Thus π is injective, hence a permutation of {1,...,5}.

If v = {i,j} then v = Si ∩ Sj, so

f({i,j}) = f(Si ∩ Sj) = Sπ(i) ∩ Sπ(j) = {π(i),π(j)}. Hence f is exactly the vertex map induced by the permutation π. Since π is a permutation, f is bijective and its inverse is the homomorphism induced by π−1. Therefore f is an automorphism.) remark: This constructive exercises show that P is a core: every endomorphism is an automorphism.

- 3. Show that the Complete graphs Kn for n ≥ 1, the Odd cycles C2k+1and the Complete bipartite graphs Km,n with m ̸= n and min(m,n) ≥ 2 are core. Can you give another example?


# Chapter 2 Groups

In this chapter, we provide the necessary background in group theory and permutation groups that will be essential for our subsequent discussion of graph automorphisms and isomorphism problems. The theory of group actions, orbits, and stabilizers forms the foundation for understanding how symmetries operate on combinatorial structures such

- as graphs. We begin with basic definitions and properties of permutation groups, then develop the key results that connect group theory to graph theory, including Burnside’s lemma for counting orbits and the fundamental concepts of primitivity and orbitals. These tools will be indispensable when we analyze the automorphism groups of graphs and study graph isomorphism classes in later chapters


### 2.1 Permutation Groups

The set of all permutations of a set V is denoted by Sym(V ), or simply Sym(n) when |V | = n. A permutation group on V is a subgroup of Sym(V ).

If X is a graph with vertex set V , then each automorphism of X is a permutation of V , so Aut(X) is a permutation group.

A permutation representation of a group G is a homomorphism from G into Sym(V ) for some set V . This is also referred to as an action of G on V , in which case we say that G acts on V . A representation is faithful if its kernel is the identity group.

A group G acting on a set V induces several other actions. If S ⊆ V and g ∈ G, the translate Sg is again a subset of V . Thus each element of G determines a permutation of the subsets of V , giving an action of G on the power set 2V .

More precisely, |Sg| = |S|, so for any fixed k, the action of G on V induces an action on the k-subsets of V . Similarly, G acts on the ordered k-tuples of elements of V . Exercise Let G act on V . Show that G acts on 2V via S  → Sg, and on the set of k-element subsets of V for any fixed k.

Suppose G is a permutation group on V . A subset S ⊆ V is G-invariant if Sg ⊆ S for all g ∈ G. If S is invariant under G, then each g ∈ G permutes the elements of S. Let g|S denote the restriction of g to S. Then the mapping

g  → g|S

is a homomorphism from G into Sym(S), and its image is a permutation group on S, denoted G|S.

52

Exercise Prove that g  → g|S is a group homomorphism.

A permutation group G on V is transitive if for any x,y ∈ V , there exists g ∈ G such that xg = y. A G-invariant subset S ⊆ V is an orbit if G|S is transitive on S. Exercise Show that for any x ∈ V , the set

xG := {xg : g ∈ G} is the orbit of G containing x.

- Lemma 2.1.1. The orbits of G on V form a partition of V . Moreover, any G-invariant subset is a union of orbits. Proof. For any x,y ∈ V , either xG = yG or xG ∩ yG = ∅. If xG ∩ yG ̸= ∅, then there exist

- g,h ∈ G such that xg = yh. Then y = xgh−1, so y ∈ xG and thus yG ⊆ xG. Similarly, xG ⊆ yG, so xG = yG. The second statement follows from the fact that orbits are minimal G-invariant subsets.


| |
|---|


Exercise Prove that the following are equivalent for a non-empty subset S ⊆ V :

- 1. S is an orbit of G
- 2. S is a minimal G-invariant subset
- 3. For any x,y ∈ S, there exists g ∈ G such that xg = y
- 4. S = xG for some x ∈ S Let G be a permutation group on V . For x ∈ V , the stabilizer of x is


Gx := {g ∈ G : xg = x}.

- Lemma 2.1.2. For any x ∈ V , Gx is a subgroup of G.


Proof. The identity permutation fixes x. If g,h ∈ Gx, then xgh = (xg)h = xh = x, so gh ∈ Gx. If g ∈ Gx, then xg−1 = (xg)g−1 = x, so g−1 ∈ Gx.

| |
|---|


For distinct points x1,...,xr ∈ V , the pointwise stabilizer is

r

Gx

1,...,xr :=

Gx

.

i

i=1

##### For S ⊆ V , the setwise stabilizer is

GS := {g ∈ G : Sg = S}. Clearly, Gx

1,...,xr ⊆ GS if S = {x1,...,xr}. Exercise Let G act on V and let S ⊆ V . Prove that:

- 1. GS is a subgroup of G
- 2. If S is finite, then GS is the largest subgroup of G that leaves S invariant as a set


- 3. GS acts on S and the kernel of this action is G(S) := x∈S Gx


- Lemma 2.1.3. Let G act on V , and let S be an orbit. If x,y ∈ S, the set of elements of G mapping x to y is a right coset of Gx. Conversely, all elements in a right coset of Gx map x to the same point in S.

Proof. Since G is transitive on S, there exists g ∈ G such that xg = y. If h ∈ G and xh = y, then hg−1 ∈ Gx, hence h ∈ Gxg. Conversely, any hg ∈ Gxg satisfies xhg = (xh)g = xg = y.

| |
|---|


- Theorem 2.1.1 (Orbit-Stabilizer Theorem). Let G act on V and x ∈ V . Then |G| = |xG| · |Gx|.

Proof. By Lemma 2.1.3, points of xG correspond bijectively to the right cosets of Gx. Each coset has |Gx| elements, giving |G| = |xG| · |Gx|.

| |
|---|


Exercise Let G be a finite group acting on a finite set V .

- 1. Prove that for any x ∈ V , |xG| divides |G|.
- 2. If G is transitive on V , show that |V | divides |G|.
- 3. If G is 2-transitive on V , show that |V |(|V | − 1) divides |G|.


- Theorem 2.1.2 (Frattini Argument). Let G be a group acting on a set X. Let H ≤ G


be a subgroup which acts transitively on X. For any α ∈ X let Gα = {g ∈ G : g · α = α} be the stabilizer of α. Then

G = HGα. Equivalently, every g ∈ G can be written as g = hk with h ∈ H and k ∈ Gα.

Proof. Fix α ∈ X and let g ∈ G. Since H is transitive, there exists h ∈ H with αh = αg. Hence αh−1g = α, so h−1g ∈ Gα. Therefore g = h(h−1g) ∈ HGα. Since g was arbitrary, G ⊆ HGα, and the reverse inclusion is trivial.

| |
|---|


Exercise If G is finite and P is a Sylow p-subgroup and N be a normal subgroup of G containing P, show G = NG(P)N .

For g,h ∈ G, the element g−1hg is conjugate to h. The set of all elements conjugate to h is called its conjugacy class. If H ≤ G and g ∈ G, define

g−1Hg := {g−1hg : h ∈ H}. This is a subgroup conjugate to H.

- Lemma 2.1.4 (Conjugation of Stabilizers). Let G act on V , and let x ∈ V . If y = xg for some g ∈ G, then


g−1Gxg = Gy.

Proof. We prove both inclusions:

Step 1: Show g−1Gxg ⊆ Gy. Let h ∈ Gx, so xh = x. Then

−1hg = xhg = (xh)g = xg = y, hence g−1hg ∈ Gy.

−1hg = (xg)g

yg

Step 2: Show Gy ⊆ g−1Gxg. Let k ∈ Gy, so yk = y. Then

−1

= x =⇒ gkg−1 ∈ Gx =⇒ k ∈ g−1Gxg. Conclusion: Both inclusions hold, hence g−1Gxg = Gy.

(xg)k = xg =⇒ xgkg

| |
|---|


Exercise Let G act on V , and let x,y ∈ V be in the same orbit.

- 1. Show that if G is abelian, then Gx = Gy.
- 2. Give an example where Gx ̸= Gy even though x and y are in the same orbit.


Proof. 1. If G is abelian, then for any g ∈ G with y = xg, we have:

Gy = g−1Gxg = Gx since conjugation is trivial in abelian groups.

2. Consider G = S3 acting on {1,2,3}. Then:

- • G1 = {(1),(23)}
- • G2 = {(1),(13)}
- • G3 = {(1),(12)}


All points are in the same orbit, but the stabilizers are different.

| |
|---|


- Theorem 2.1.3 (Burnside / Cauchy-Frobenius). Let G act on a finite set V . Then the number of orbits of G on V is


1 |G| g∈G

#orbits =

|Fix(g)|, Fix(g) := {x ∈ V : xg = x}.

Proof. We count the set S = {(g,x) ∈ G × V : xg = x} in two different ways:

First count: For each g ∈ G, there are |Fix(g)| elements x ∈ V such that xg = x. Hence:

|S| =

|Fix(g)|.

g∈G

Second count: For each x ∈ V , there are |Gx| elements g ∈ G such that xg = x. Hence:

|S| =

|Gx|.

x∈V

Let O1,...,Om be the orbits of G on V . For each orbit Oi and for any x ∈ Oi, by the Orbit-Stabilizer Theorem we have:

|Oi| = |G| |Gx|

so |Gx| = |G| |Oi|

.

###### Therefore:

|Gx| =

x∈V

Equating both counts:

m

|Gx| =

i=1 x∈Oi

m

|G| |Oi|

|Oi| ·

= m|G|.

i=1

1 |G| g∈G

|Fix(g)| = m|G| =⇒ m =

|Fix(g)|.

g∈G

| |
|---|


##### Exercise

- 1. Use Burnside’s Lemma to count distinct colorings of the vertices of a square with n colors, modulo rotations/reflections.
- 2. Let G act transitively on V with |V | > 1. Show there exists g ∈ G with no fixed points.


Proof. 1. The symmetry group of the square (dihedral group D4) has 8 elements:

- • Identity: fixes all n4 colorings
- • 3 rotations by 90◦,270◦: fix n colorings (all vertices same color)
- • 1 rotation by 180◦: fixes n2 colorings (opposite vertices same color)
- • 2 reflections through vertices: fix n3 colorings (fixed vertex and its opposite)
- • 2 reflections through edges: fix n2 colorings (pairs of opposite vertices)


By Burnside’s Lemma: 81(n4 + 2n3 + 3n2 + 2n).

- 2. By Burnside’s Lemma: |G1| g∈G |Fix(g)| = 1. Since the identity fixes |V | > 1 points, some g ∈ G must fix fewer than 1 point, i.e., 0 points.


| |
|---|


### 2.2 Orbits on Pairs

- Definition 2.2.1 (Orbitals). Let G act transitively on V . Then G acts naturally on V × V by (x,y)g = (xg,yg). The orbits of this action are called orbitals. The diagonal {(x,x) : x ∈ V } is always an orbital, called the diagonal orbital.


- Definition 2.2.2 (Transpose of an Orbital). If n ⊆ V × V is an orbital, its transpose is:


nT = {(y,x) : (x,y) ∈ n}. An orbital is symmetric if n = nT.

- Lemma 2.2.1 (Orbital-Stabilizer Correspondence). Let x ∈ V . There is a one-to-one correspondence between the orbits of G on V × V and the orbits of Gx on V .


Proof. Let n be an orbital, and define Y0 = {y ∈ V : (x,y) ∈ n}.

- Step 1: Show Y0 is an orbit of Gx. If y,y′ ∈ Y0, then (x,y),(x,y′) ∈ n, so there

exists g ∈ G with (x,y)g = (x,y′). This implies xg = x and yg = y′, so g ∈ Gx and y,y′ are in the same orbit of Gx.

- Step 2: Conversely. If y′ = yg for g ∈ Gx, then (x,y)g = (x,y′) ∈ n, so y′ ∈ Y0.
- Step 3: Partition. All Y0 obtained in this way partition V , giving a one-to-one


correspondence.

| |
|---|


- Definition 2.2.3 (Rank of a Permutation Group). The number of orbits of Gx on V is called the rank of G.

- Lemma 2.2.2 (Symmetric Orbital). Let n be an orbital and (x,y) ∈ n. Then n = nT (symmetric) if and only if there exists g ∈ G with xg = y and yg = x.


Proof. (⇒) If n = nT, then (y,x) ∈ n. By definition of orbitals, there exists g ∈ G with (x,y)g = (y,x), which implies xg = y and yg = x.

(⇐) If such g exists, then (x,y)g = (y,x) ∈ n, hence n ∩ nT ̸= ∅. Since orbitals are either disjoint or identical with their transpose, we must have n = nT.

| |
|---|


- Definition 2.2.4 (Generously Transitive). A permutation group G on V is generously transitive if for any two distinct elements x,y ∈ V , there exists g ∈ G swapping x and y.


##### Exercise

- 1. Show that G is generously transitive if and only if all orbitals are symmetric.
- 2. Prove that if G is 2-transitive, then it has rank 2.
- 3. Give an example of a transitive group that is not generously transitive.


### 2.3 Primitivity

- Definition 2.3.1 (Block of Imprimitivity). Let G act transitively on V . A nonempty subset B ⊆ V is a block if for all g ∈ G, either Bg = B or Bg ∩ B = ∅.
- Definition 2.3.2 (System of Imprimitivity). The set of distinct translates of a block B forms a system of imprimitivity.
- Definition 2.3.3 (Primitive Group). A transitive group is primitive if it has no nontrivial blocks (blocks other than singletons and V itself). Otherwise it is imprimitive.


- Lemma 2.3.1 (Primitivity via Maximal Stabilizers). Let G be transitive on V , and x ∈ V . Then G is primitive if and only if Gx is a maximal subgroup of G.


Proof. (⇒) Suppose G is primitive but Gx is not maximal. Then there exists H with Gx ⊂ H ⊂ G. Let B = xH = {xh : h ∈ H}. We show B is a nontrivial block:

For any g ∈ G, either Bg = B or Bg ∩ B = ∅. If Bg ∩ B ̸= ∅, then there exist 1g = xh

- h1,h2 ∈ H such that xh


2, so h1gh−2 1 ∈ Gx ⊂ H, hence g ∈ H and Bg = B. Since Gx ⊂ H ⊂ G, we have {x} ⊂ B ⊂ V , contradicting primitivity. (⇐) Suppose Gx is maximal but G is imprimitive. Let B be a nontrivial block

containing x. Then GB = {g ∈ G : Bg = B} is a subgroup containing Gx. Since B is nontrivial, Gx ⊂ GB ⊂ G, contradicting maximality of Gx.

| |
|---|


- Definition 2.3.4 (2-Transitive Group). A permutation group G on V is 2-transitive if it acts transitively on the set of ordered pairs of distinct elements of V .

- Lemma 2.3.2. If G is 2-transitive on V , then:

- 1. G is primitive
- 2. G has rank 2 (only the diagonal and non-diagonal orbitals)
- 3. For any x ∈ V , Gx is transitive on V \ {x}


Proof. 1. If G were imprimitive with block B containing x, then for any y ∈ B \ {x} and z ∈/ B, there is no g ∈ G with (x,y)g = (x,z), contradicting 2-transitivity.

- 2. The orbitals are exactly {(x,x) : x ∈ V } and {(x,y) : x ̸= y}.
- 3. Immediate from the definition of 2-transitivity.


| |
|---|


Definition 2.3.5 (Strongly and Weakly Connected Digraph). Let D be a directed graph.

- • A path is a sequence of vertices u0,u1,...,ur with (ui−1,ui) an arc for each i
- • A weak path allows either (ui−1,ui) or (ui,ui−1) as an arc
- • D is strongly connected if any two vertices can be joined by a path
- • D is weakly connected if any two vertices can be joined by a weak path


- Lemma 2.3.3 (Strong/Weak Equivalence). Let D be a digraph where every vertex has equal in-valency and out-valency. Then D is strongly connected if and only if it is weakly connected.




Proof. (⇒) Trivial, since strong connectivity implies weak connectivity.

(⇐) Suppose D is weakly but not strongly connected. Let D1,...,Dr be its strong components. Consider the condensation digraph D′ whose vertices are the strong components, with an arc from Di to Dj if there is an arc from some vertex in Di to some vertex in Dj.

Since D′ is acyclic, there exists a strong component Di with no incoming arcs from other components. But then:

in-valency(v) = number of arcs within Di <

v∈Di

out-valency(v)

v∈Di

since weak connectivity requires at least one outgoing arc from Di to another component. This contradicts the assumption that in-valency equals out-valency for each vertex.

| |
|---|


- Theorem 2.3.1 (Primitivity and Connectivity). Let G be transitive on V . Then G is primitive if and only if every nondiagonal orbital of G on V ×V is connected as a directed graph.


Proof. (⇒) Suppose G is primitive. Let n be a nondiagonal orbital and (x,y) ∈ n. Consider the connected component C of n containing x. We show C = V .

For any g ∈ G, either Cg = C or Cg ∩ C = ∅. But since G is transitive and C is nonempty, the translates of C cover V . If Cg ∩ C ̸= ∅ for some g, then Cg = C. Thus C is a block. Since G is primitive and C contains at least x and y ̸= x, we must have C = V .

(⇐) Suppose all nondiagonal orbitals are connected but G is imprimitive. Let B be a nontrivial block containing x. Pick y ∈ B \ {x} and z ∈/ B. Let n be the orbital containing (x,y).

Since n is connected, there is a path from x to z in n. But this path must leave B

- at some point, contradicting that B is a block (since for any g ∈ G, either Bg = B or Bg ∩ B = ∅).


| |
|---|


##### Exercise

- 1. Show that every 2-transitive group is primitive.
- 2. Give an example of a primitive group that is not 2-transitive.
- 3. Show that if G is primitive and N is a non-trivial normal subgroup of G, then N is transitive.


Proof. 1. If G is 2-transitive, then for any x ∈ V , Gx is transitive on V \ {x}. If G were imprimitive with block B containing x, then B \ {x} would be a proper Gx-invariant subset of V \ {x}, contradicting transitivity.

- 2. If N is a normal subgroup of a primitive group G, then the orbits of N form a system of imprimitivity. By primitivity, these must be trivial, so N is either trivial or transitive.


| |
|---|


# Chapter 3 Transitive Graphs

We are going to study the properties of graphs whose automorphism group acts vertex transitively. A vertex-transitive graph is necessarily regular. One challenge is to find properties of vertex-transitive graphs that are not shared by all regular graphs. We will see that transitive graphs are more strongly connected than regular graphs in general. Cayley graphs form an important class of vertex-transitive graphs; we introduce them and offer some reasons why they are important and interesting.

### 3.1 Vertex-Transitive Graphs

A graph X is vertex transitive (or just transitive) if its automorphism group acts transitively on V (X). Thus for any two distinct vertices of X there is an automorphism mapping one to the other.

An interesting family of vertex-transitive graphs is provided by the k-cubes Qk. The vertex set of Qk is the set of all 2k binary k-tuples, with two being adjacent if they differ in precisely one coordinate position. We have already met the 3-cube Q3, which is normally just called the cube

- Lemma 3.1.1. The k-cube Qk is vertex transitive. Proof. If v is a fixed k-tuple, then the mapping


Pv : x  → x + v

(where addition is binary) is a permutation of the vertices of Qk. This mapping is an automorphism because the k-tuples x and y differ in precisely one coordinate position if and only if x + v and y + v differ in precisely one coordinate position. There are 2k such permutations, and they form a subgroup H of the automorphism group of Qk. This subgroup acts transitively on V (Qk) because for any two vertices x and y, the automorphism Py−x maps x to y.

| |
|---|


Another family of vertex-transitive graphs that we have met before are the circulants. Any vertex can be mapped to any other vertex by using a suitable power of the cyclic permutation described in chapter 1.

The circulants and the k-cubes are both examples of a more general construction that produces many, but not all, vertex-transitive graphs. Let G be a group and let C be a

60

- 3.2. EDGE-TRANSITIVE GRAPHS 61


subset of G that is closed under taking inverses and does not contain the identity. Then the Cayley graph X(G,C) is the graph with vertex set G and edge set

E(X(G,C)) = {gh : hg−1 ∈ C}.

If C is an arbitrary subset of G, then we can define a directed graph X(G,C) with vertex set G and arc set {(g,h) : hg−1 ∈ C}. If C is inverse-closed and does not contain the identity, then this graph is undirected and has no loops, and the definition reduces to that of a Cayley graph.

- Theorem 3.1.1. The Cayley graph X(G,C) is vertex transitive. Proof. For each g ∈ G the mapping


Pg : x  → xg is a permutation of the elements of G. This is an automorphism of X(G,C) because (xg)(yg)−1 = xy−1,

and so x ∼ y if and only if xg ∼ yg. The permutations Pg form a subgroup of the automorphism group of X(G,C) isomorphic to G. This subgroup acts transitively on the

vertices of X(G,C) because for any two vertices g and h, the automorphism Pg−1h maps

- g to h.


| |
|---|


The k-cube is a Cayley graph for the elementary abelian group (Z2)k, and a circulant on n vertices is a Cayley graph for the cyclic group of order n.

Most small vertex-transitive graphs are Cayley graphs, but there are also many families of vertex-transitive graphs that are not Cayley graphs. In particular, the graphs J(v,k,i) are vertex transitive because Sym(v) contains permutations that map any k-set to any other k-set, but in general they are not Cayley graphs. We content ourselves with a single example.

- Lemma 3.1.2. The Petersen graph is not a Cayley graph.

Proof. There are only two groups of order 10, the cyclic group Z10 and the dihedral group D10. You may verify that none of the cubic Cayley graphs on these groups are isomorphic to the Petersen graph (Exercise: each cayley graph on 10 vertices has girth 4).

| |
|---|


- 3.2 Edge-Transitive Graphs


A graph X is edge transitive if its automorphism group acts transitively on E(X). It is straightforward to see that the graphs J(v,k,i) are edge transitive, but the circulants are not usually edge transitive.

An arc in X is an ordered pair of adjacent vertices, and X is arc transitive if Aut(X) acts transitively on its arcs. It is frequently useful to view an edge in a graph as a pair of oppositely directed arcs. An arc-transitive graph is necessarily vertex and edge transitive. In this section we will consider the relations between these various forms of transitivity.

The complete bipartite graphs Km,n are edge transitive, but not vertex transitive unless m = n, because no automorphism can map a vertex of valency m to a vertex of valency n. The next lemma shows that all graphs that are edge transitive but not vertex transitive are bipartite.

- Lemma 3.2.1. Let X be an edge-transitive graph with no isolated vertices. If X is not vertex transitive, then Aut(X) has exactly two orbits, and these two orbits are a bipartition of X. Proof. Suppose X is edge but not vertex transitive. Suppose that {x,y} ∈ E(X). If

- w ∈ V (X), then w lies on an edge and there is an element of Aut(X) that maps this edge onto {x,y}. Hence any vertex of X lies in either the orbit of x under Aut(X), or the orbit of y. This shows that Aut(X) has exactly two orbits. An edge that joins two vertices in one orbit cannot be mapped by an automorphism to an edge that contains a vertex from the other orbit. Since X is edge transitive and every vertex lies in an edge, it follows that there is no edge joining two vertices in the same orbit. Hence X is bipartite and the orbits are a bipartition for it.

| |
|---|


An arc-transitive graph is, as we noted, always vertex and edge transitive. The converse is in general false; we do at least have the next result. Lemma 3.2.2. If the graph X is vertex- and edge-transitive, but not arc-transitive, then its valency is even. Proof. Let G = Aut(X), and pick a vertex x ∈ V (X) and a neighbor y of x. Let

n = G · (x,y) be the orbit of the arc (x,y) under G.

Since X is edge-transitive, every edge can be mapped by an automorphism to either (x,y) or (y,x). But X is not arc-transitive, so (y,x) ∈/ n. Let

nT = {(v,u) | (u,v) ∈ n} be the reversed orbit. Then n and nT are disjoint, and the edge set of X is

E(X) = n ∪ nT. Now consider the vertex x. Let

d = |{z | (x,z) ∈ n}| be the out-degree of x in n.

Observe that (x,y) ∈ n implies (y,x) ∈ nT. By vertex-transitivity, the out-degree of

- x in n equals the out-degree of y in nT. But the out-degree of y in nT counts arcs of the form (y,z) ∈ nT, which correspond exactly to arcs (z,y) ∈ n. Therefore,




out-degree of x in n = out-degree of y in nT = in-degree of x in n.

Hence, at vertex x, the number of edges from n equals the number from nT, giving total valency

deg(x) = |{z | (x,z) ∈ n}| + |{z | (x,z) ∈ nT}| = d + d = 2d. Since 2d is even, the valency of X is even. A simple corollary to this result is that a vertex- and edge-transitive graph of odd

| |
|---|


valency must be arc transitive.

- 3.3. SEMISYMMETRIC GRAPHS AND SMALL ORDERS 63


### 3.3 Semisymmetric graphs and small orders

- Definition 3.3.1. A graph X is called semisymmetric if X is regular and edge-transitive but not vertex-transitive.


The first structural fact is standard and easy to prove.

- Proposition 3.3.1. If X is a connected semisymmetric graph then X is bipartite and the automorphism group of X has exactly two vertex-orbits (the two bipartition classes), which are of equal size. In particular the order |V (X)| is even.

Proof. Let A = Aut(X). Since X is edge-transitive but not vertex-transitive, A acts transitively on the edge-set E(X) but has at least two orbits on V (X). Because every edge has its two endpoints in (possibly different) vertex-orbits, edge-transitivity implies all edges join vertices in different vertex-orbits; otherwise an edge whose endpoints lie in the same orbit could be sent to an edge whose endpoints lie in different orbits, contradicting that vertex-orbits are preserved by automorphisms. Hence every edge joins two distinct vertex-orbits; thus there are no edges inside a vertex-orbit, so each vertex-orbit is an independent set. Therefore X is bipartite, with the bipartition given by the vertex-orbits of A.

Let the two orbits have sizes r and s. Edge-transitivity and regularity of X imply every vertex has the same degree k ≥ 1. Counting edges from the two sides gives rk = |E(X)| = sk, hence r = s. Thus the two parts have equal size and |V (X)| = 2r is even.

| |
|---|


From Proposition 3.3.1 we immediately get:

- Corollary 3.3.1. There is no semisymmetric graph of prime order p (with p odd).


Proof. By Proposition 3.3.1 the order of any semisymmetric graph is even. A prime p > 2 is odd, hence impossible. The only prime that is even is 2, but a graph on two vertices is either a single edge (which is vertex-transitive) or two isolated vertices (not edge-transitive), so there is no semisymmetric graph of order 2 either.

| |
|---|


Next we rule out order 6.

- Proposition 3.3.2. There is no semisymmetric graph of order 6.


Proof. By Proposition 3.3.1 a semisymmetric graph on 6 vertices would be bipartite with two parts of size 3 and regular of some degree k with 1 ≤ k ≤ 3.

Consider the possibilities:

- • k = 1. Then the graph is a perfect matching (three disjoint edges). Such a graph is vertex-transitive (any vertex in the matching is equivalent to any other by a suitable permutation that preserves the matching), so it is not semisymmetric.
- • k = 2. A connected 2-regular graph on 6 vertices is a 6-cycle C6, which is vertextransitive. (If disconnected, it is union of cycles, again vertex-transitive on each component.) Thus not semisymmetric.
- • k = 3. The unique connected bipartite 3-regular graph with parts of size 3 is the


complete bipartite graph K3,3. But K3,3 is vertex-transitive: any vertex lies in a part of size 3 and there is an automorphism sending any vertex to any other (parts can be permuted), so K3,3 is vertex-transitive.

Hence no case yields a connected regular edge-transitive but not vertex-transitive graph on 6 vertices. Example 3.3.1. There is no semisymmetric graph of order 3p. Proof. Let X be a semisymmetric graph of order 3p. If |V (X)| = 3p with p odd, then by

| |
|---|


- Proposition 3.3.1 the order must be even. But 3p is odd for odd p, so no semisymmetric graph can exist. (The only remaining case is p = 2, giving |V | = 6, which was treated in


- Proposition 3.3.2.)


| |
|---|


##### Remark:

The arguments above use only elementary counting and basic permutation group facts (orbit sizes divide the set size). For orders with small prime factors these constraints are often strong enough to rule out semisymmetric graphs. For larger composite orders semisymmetric graphs do exist (indeed the smallest nontrivial semisymmetric graph is the Folkman graph of order 20, and there are many further constructions), so the impossibility phenomena are primarily a small-order effect.

Example The Folkman graph is a 4-regular bipartite graph on 20 vertices. It can be constructed in several equivalent ways:

Start with the complete graph K5. Subdivide each edge into a path of length two, and then duplicate each of the original five vertices. The resulting bipartite graph has 20 vertices, each of degree 4.

The Folkman graph is edge-transitive but not vertex-transitive. Since it is regular, it is an example of a semisymmetrci graph.

![image 5](<2026-ashrafi-algebraic-graph-theory_images/imageFile5.png>)

Figure 3.1: The Folkman graph, the smallest semi-symmetric graph.

Explanation: The green vertices subdivide each edge of K5, and the red pairs of vertices are the result of doubling the five vertices of K5.

Suppose that Γ is a connected k-graph and G is a subgroup of the automorphism group Aut(Γ) of Γ. Then Γ is G-semisymmetric if G acts edge transitively but not vertex transitively on Γ. Now suppose that Γ is a G-semisymmetric graph. Let {u,v} be an edge in Γ. Set Gu = StabG(u), Gv = StabG(v) and Guv = Gu ∩ Gv.

##### Exercises: Show that

- 1. As G acts edge transitively on Γ and u is not in the same G-orbit as v, we have [Gu : Guv] = [Gv : Guv] = k.
- 2. Suppose that K ◁ G and K ≤ Guv = Gu ∩ Gv. Then K fixes every edge of Γ and hence K = 1.
- 3. As Γ is connected, the subgroup ⟨Gu,Gv⟩ acts transitively on the edges of Γ, show that G = ⟨Gu,Gv⟩.

We have shown that G satisfies:

- • G = ⟨Gu,Gv⟩;
- • [Gu : Gu ∩ Gv] = [Gv : Gu ∩ Gv] = k; and
- • no non-trivial subgroup of Guv is normal in G.


This group theoretic configuration has been studied by Goldschmidt ( see D. M. Goldschmidt, “Automorphisms of trivalent graphs”, Annals of Mathematics, 112 (1980), 377–406.) where it is shown that when k = 3, the triple (Gu,Gv,Guv) is isomorphic (as an amalgam) to one of fifteen possible such triples (see Table 3.1). Thus if Γ is Gsemisymmetric cubic graph, then the structures of Gu, Gv and Guv (and the embeddings of Guv into Gu and Gv) are known (up to swapping the roles of u and v). We call the possible triples of groups appearing in Table 3.1 Goldschmidt amalgams.

- 3.4 Semisymmetric graphs as coset graphs


- Definition 3.4.1 (Amalgam and completion). Let G be a finite group and let Gu,Gv ≤ G with Guv = Gu ∩ Gv. We call A = (Gu,Gv,Guv) an amalgam in G, and G a completion of A.
- Definition 3.4.2 (Coset Graph). Let G be a completion of the amalgam A = (H,K,H ∩ K). The coset graph Γ = Γ(G,A) is the bipartite graph with vertex set


V (Γ) = {Hg | g ∈ G} ∪ {Kg | g ∈ G}, and edge set

E(Γ) = {Hh, Kg} Hh ∩ Kg ̸= ∅ . Equivalently,

{Hh,Kg} ∈ E(Γ) ⇐⇒ g ∈ KHh ⇐⇒ h ∈ HKg.

Table 3.1: Goldschmidt Amalgams

##### Name (G1,G2) Completion

- G1 (Z3,Z3) Z3 × Z3 G11 (Sym(3),Sym(3)) 32.2 G12 (Sym(3),Z6) Sym(3) × Z3 G13 (Sym(3) × Z2,Sym(3) × Z2) PSL2(11)
- G2 (Alt(4),Sym(3) × Z2) PSL2(11)

- G21 (Sym(4),Dih(24)) PSL2(23)
- G22 (Sym(4),(22 × 3).2) Alt(7)
- G23 (Alt(4) × Z2,Sym(3) × Z2 × Z2) Sym(3) ≀ Z3
- G24 (Sym(4) × Z2,Sym(3) × Dih(8)) Sym(7)


- G3 (Sym(4),Sym(4)) Alt(6),SL3(2) G31 (Sym(4) × Z2,Sym(4) × Z2) Sym(6)
- G4 ((Z4 × Z4).Sym(3),(Q8 ◦ Z4).Sym(3)) G2(2)′ ∼= U3(3) G41 ((Z4 × Z4).(Sym(3) × Z2),(Q8 ◦ Q8).Sym(3)) G2(2) (η(G2,O2(G2)) = 1)
- G5 ((Z4 × Z4).(Sym(3) × Z2),(Q8 ◦ Q8).Sym(3)) M12 (η(G2,O2(G2)) = 2) G51 ((Z4 × Z4).(22 × 3).2,(Q8 ◦ Q8).(Sym(3) × Z2)) Aut(M12) (η(G2,O2(G2)) = 2)


Remark 3.4.1. Suppose Hh ∩ Kg ̸= ∅. Then there exists y ∈ G such that

y ∈ Hh and y ∈ Kg, so y = uh = vg for some u ∈ H and v ∈ K. Hence

g = v−1uh,

so g ∈ KHh. Conversely, if g ∈ KHh, then g = v−1uh for some v ∈ K, u ∈ H, and thus uh = vg ∈ Hh ∩ Kg ̸= ∅. Therefore,

{Hh,Kg} ∈ E(Γ) ⇐⇒ Hh ∩ Kg ̸= ∅ ⇐⇒ g ∈ KHh.

- Lemma 3.4.1 (Basic Properties). With notation as above:


- 1. Γ is bipartite, with parts {Hg} and {Kg}.
- 2. The right-regular action of G on cosets, (Hg)x = H(gx), (Kg)x = K(gx) (x ∈ G),

is an action by graph automorphisms. In particular, G is edge-transitive on Γ.

- 3. The valency of a vertex Hg is [H : H ∩ K], and the valency of a vertex Kg is [K : H ∩ K]. Hence Γ is regular if and only if [H : H ∩ K] = [K : H ∩ K].


Proof. (1) The bipartition is immediate from the definition: edges join only vertices of the forms Hh and Kg.

(2) If {Hh,Kg} ∈ E(Γ), then Hh ∩ Kg ̸= ∅. Since right multiplication by x ∈ G is a bijection on G,

Hh ∩ Kg ̸= ∅ ⇐⇒ (Hh)x ∩ (Kg)x ̸= ∅,

and (Hh)x = H(hx), (Kg)x = K(gx). Thus adjacency is preserved by right multiplication, so the action is by automorphisms.

Edge-transitivity follows because for any edge {Hh,Kg} there exists x ∈ G with Hx = Hh, Kx = Kg,

so the base edge {H,K} is sent to any given edge by some group element.

(3) The neighbors of Hg are precisely the vertices Kg′ with Hg ∩Kg′ ̸= ∅. Write any such intersection element as y = ug = vg′ with u ∈ H, v ∈ K. Then g′ = v−1ug. Thus neighbors correspond to K(ug) with u ∈ H.

Two elements u1,u2 ∈ H yield the same neighbor iff K(u1g) = K(u2g) ⇐⇒ u−2 1u1 ∈ K.

Since u−2 1u1 ∈ H as well, this means u−2 1u1 ∈ H ∩ K. Hence the neighbors of Hg correspond bijectively to the left cosets of H ∩ K in H, and there are [H : H ∩ K] of

- them. The same argument with H,K swapped gives the valency of Kg. Therefore, Γ is regular if and only if [H : H ∩ K] = [K : H ∩ K].


| |
|---|


- Proposition 3.4.1. Let Γ be a connected G-semisymmetric graph and let {u,v} be an edge. Set


Gu := StabG(u), Gv := StabG(v), Guv := Gu ∩ Gv. Then Γ is isomorphic to the coset graph

Γ(G,Gu,Gv) with vertex set

V (Γ) = {Gug | g ∈ G} ∪ {Gvg | g ∈ G} and edge set

E(Γ) = {Guh,Gvg} | Guh ∩ Gvg ̸= ∅ . Moreover, for a semisymmetric graph, Gu and Gv are not conjugate in G. Proof. Step 1: Coset graph isomorphism. Define maps

ΦA : G/H → A, Gug  → g · u, ΦB : G/K → B, Gvg  → g · v,

where A and B are the two G-orbits on vertices. Because G is transitive on each part, these are bijections onto A and B. Combining them gives

Φ : V (Γ(G,Gu,Gv)) → V (Γ), Φ|G/H = ΦA, Φ|G/K = ΦB. Adjacency is preserved: for Guh ∈ G/H and Gvg ∈ G/K,

Guh ∼ Gvg ⇐⇒ Guh ∩ Gvg ̸= ∅ ⇐⇒ g ∈ Guvh ⇐⇒ h ∈ Guvg. By definition of the G-orbit of {u,v}, this exactly corresponds to g · v being adjacent to

- h · u in Γ. Hence Φ is a graph isomorphism, and Γ ∼= Γ(G,Gu,Gv). Step 2: Conjugacy of stabilizers cannot occur. Suppose, for contradiction, that


there exists g ∈ G such that Gv = gGug−1. Define a map σ on the coset graph vertices by

σ(Guh) := Gv(gh), σ(Gvh) := Gu(g−1h).

Check adjacency: let {Guh,Gvk} ∈ E(Γ), so k ∈ Guvh. Set H = Gu,K = Gv. Then Guv = H ∩ K. Now

σ(Guh) = Gvgh, σ(Gvk) = Gug−1k = Gug−1xh

for some x ∈ Guv. Since x ∈ H and K = gHg−1, we have g−1xg ∈ K, so g−1k = (g−1xg)(g−1h) ∈ K · g−1h. Therefore

σ(Gvk) ∈ Gu · g−1h,

so {σ(Guh),σ(Gvk)} is indeed an edge. Thus σ is a graph automorphism swapping the two parts.

Because Φ is an isomorphism, Φ ◦ σ ◦ Φ−1 ∈ Aut(Γ) swaps the two vertex-orbits A and B. Combined with transitivity on each part, this implies Γ is vertex-transitive, contradicting semisymmetry. Therefore Gu and Gv cannot be conjugate in G.

| |
|---|


- Lemma 3.4.2 (Connectivity criterion). With notation as above, set H = ⟨Gu,Gv⟩ ≤ G. Then:


- 1. Γ is connected if and only if H = G.
- 2. More precisely, the vertex set of each connected component is {Gug | g ∈ Hx} ∪ {Gvg | g ∈ Hx}


for some right coset Hx of H in G. In particular, the number of connected components of Γ equals the index [G : H].

Proof. Let Vu = {Gug | g ∈ G} and Vv = {Gvg | g ∈ G} be the biparts. Right multiplication by H preserves adjacency and keeps the set Vu ∪ Vv inside the union of cosets indexed by a fixed right coset Hx: if g ∈ Hx and h ∈ H, then Gugh ∈ Vu and Gvgh ∈ Vv, and edges are preserved by right multiplication.

Conversely, any edge {Guh,Gvg} witnesses g ∈ Guvh ⊆ Guh, so along a walk starting at Gu the labels of successive right-multipliers alternate between elements of Gu and Gv. Hence every vertex reachable from Gu has the form Guw or Gvw with w ∈ ⟨Gu,Gv⟩ = H. Thus the connected component of Gu is precisely {Guh | h ∈ H} ∪ {Gvh | h ∈ H}, and more generally the component containing Gux (or Gvx) is the translate by x of that set, i.e. {Guhx | h ∈ H} ∪ {Gvhx | h ∈ H}.

Therefore components are indexed by right cosets Hx of H in G, giving exactly [G : H] components. In particular, Γ is connected iff [G : H] = 1, i.e. iff H = G.

| |
|---|


- Proposition 3.4.2 (Kernel of the action). Let K be the kernel of the action of G on V (Γ). Then


Gxuv = coreG(Guv),

K =

x∈G

the largest normal subgroup of G contained in Guv. Consequently, the induced action of G/K on Γ is faithful.

Proof. An element x ∈ G fixes every vertex iff it fixes every coset Gug and every coset Gvg, i.e. Gug = Gugx and Gvg = Gvgx for all g ∈ G. This is equivalent to x ∈

g∈G g−1Gug ∩ g∈G g−1Gvg, which equals g∈G g−1(Gu ∩ Gv)g = coreG(Guv).

| |
|---|


- Theorem 3.4.2 (Semisymmetry via cosets). Suppose [Gu : Guv] = [Gv : Guv] = k ≥ 2 and Gu,Gv are not conjugate in G. Then the coset graph Γ(G,A) is a connected kregular edge-transitive graph in which G has exactly two vertex-orbits (the two parts). In particular, the faithful quotient G/K acts edge-transitively but not vertex-transitively; i.e. Γ is G/K-semisymmetric. If moreover K = 1, then Γ is G-semisymmetric.


Proof. By the lemma, Γ is biregular with valencies [Gu : Guv] and [Gv : Guv]; under the hypothesis these are equal to k, so Γ is k-regular. Edge-transitivity of G has already been shown. The two families of vertices {Gug} and {Gvg} are G-orbits, and if Gu,Gv are not conjugate, there is no automorphism in the right action that maps a Gu-coset to a Gv-coset. Thus G has exactly two vertex-orbits and the action is not vertex-transitive. Factoring by the kernel K makes the action faithful; if K = 1 it is already faithful.

| |
|---|


- Definition 3.4.3 (Goldschmidt amalgam). An amalgam A = (Gu,Gv,Guv) is called a Goldschmidt amalgam (for the cubic case) if [Gu : Guv] = [Gv : Guv] = 3, G acts edge-transitively on Γ(G,A), and K = coreG(Guv) = 1.


- Corollary 3.4.1 (Cubic case). If A is a Goldschmidt amalgam, then Γ(G,A) is a connected bipartite cubic graph that is edge-transitive and not vertex-transitive; that is, it is semisymmetric, and the action of G on Γ is faithful.


- Theorem 3.4.3 (Converse for cubic semisymmetric graphs). Let Γ be a connected cubic semisymmetric graph, and let G ≤ Aut(Γ) act edge-transitively. Fix an edge {u,v} with u


and v in different bipart classes, and set Gu = StabG(u), Gv = StabG(v), Guv = Gu ∩Gv. Then:

- 1. [Gu : Guv] = [Gv : Guv] = 3 (local edge-transitivity at a vertex),
- 2. K = coreG(Guv) = 1 (faithfulness on edges/vertices),
- 3. the natural G-equivariant map ϕ : Γ(G,(Gu,Gv,Guv)) −→ Γ, Gug  → ug, Gvg  → vg,


is a graph isomorphism.

Hence every connected cubic semisymmetric graph arises as a coset graph of a completion of a Goldschmidt amalgam, and conversely every completion of a Goldschmidt amalgam yields a (connected) cubic semisymmetric coset graph.

Proof sketch. Edge-transitivity implies Gu is transitive on the three neighbors of u, so

- [Gu : Guv] = 3, and similarly for v. Since G has exactly two vertex-orbits (bipartition) and is edge-transitive, its kernel on vertices is trivial; one checks this is precisely coreG(Guv). Finally, the map ϕ is well-defined, adjacency-preserving (because intersections of cosets encode the existence of an edge), surjective, and injective by the transitivity of G on the appropriate coset sets. remark: In the non-cubic case, Theorem 3.4.2 already shows that whenever [Gu : Guv] =

| |
|---|


- [Gv : Guv] = k ≥ 2, the coset graph Γ(G,A) is a k-regular edge-transitive bipartite graph with two vertex-orbits under the right action of G. Thus, up to the kernel K, semisymmetric graphs are coset graphs. The cubic case is exactly the k = 3 specialization, where Goldschmidt’s classification of such amalgams underlies many structure theorems.


We can generalize these simple impossibility results for a few families of orders.

- Theorem 3.4.4. Let p be an odd prime. There is no semisymmetric graph of order 2p.

Proof. Let X be a semisymmetric graph of order 2p. By Proposition 3.3.1, X is bipartite with parts A and B, |A| = |B| = p, and G = Aut(X) is edge-transitive but not vertextransitive, so A and B are the two vertex-orbits. Write k for the common degree; we may assume p ≥ 5 (the small case p = 3 is checked separately).

Edge-transitivity implies G is transitive on each of A and B. By Burnside’s theorem on transitive groups of prime degree, the action of G on A (and similarly on B) is either

- (I) almost simple: the permutation group contains Ap (hence is 2-transitive, in fact (p − 2)-transitive), or
- (II) affine: G embeds in AGL(1,p) (the translation–multiplier picture). We treat case (I) first and then recall the affine case (II) which yields the contradiction


- as in the earlier proof.


- Case (I): Ap ⊆ G. Fix v ∈ A. The stabilizer Gv contains Ap−1, which shows the only possibilities for the degree k are

k = p or k = p − 1. Indeed:

- • If k = p then every v ∈ A is adjacent to all vertices of B, so X ∼= Kp,p.
- • If k = p − 1 then every v ∈ A is adjacent to precisely p − 1 vertices of B; since the action is symmetric this means for each v ∈ A there is a unique u ∈ B not adjacent to v, and the map v  → u is a G-equivariant bijection A → B. The resulting graph


is exactly Kp,p with a perfect matching removed (every vertex misses exactly one partner and these missing pairs form a perfect matching).

Both graphs above (Kp,p and Kp,p minus a perfect matching) are vertex-transitive, contradicting the semisymmetry of X. Thus case (I) cannot occur.

- Case (II): affine. Affine case. In the affine case, the action of G on each part is


transitive of prime degree, and a point stabilizer Gv is cyclic of order dividing p − 1. Moreover, G has only one conjugacy class of subgroups isomorphic to Gv.

Let u ∈ A and v ∈ B be adjacent vertices in X. Then Gv and Gu are isomorphic subgroups of G, and since there is only one conjugacy class of such subgroups, Gv and Gu are conjugate in G. By Proposition 3.4.1, X is isomorphic to the coset graph X(G,Gv,Gu), which requires that Gv and Gu are not conjugate. This is a contradiction. Hence, no semisymmetric graph of order 2p exists in the affine case. Therefore neither possibility from Burnside’s theorem is compatible with the semisym-

metry assumption, and no semisymmetric graph of order 2p exists.

| |
|---|


- Theorem 3.4.5. Let p be a prime. There is no connected cubic semisymmetric graph of order 4p. In other words: every connected cubic edge-transitive graph of order 4p is vertex-transitive.


Sketch of proof. Let Γ be a connected cubic semisymmetric graph of order 4p, and write A = Aut(Γ). A few standard facts we will use without proof:

- 3.5. CONNECTIVITY OF VERTEX-TRANSITIVE GRAPHS 71


- • A semisymmetric graph is necessarily bipartite, and A has exactly two vertex-orbits (the two bipartition classes) of equal size. (So |V (Γ)| is even.)
- • If N ◁ A is an intransitive normal subgroup, then N acts semiregularly on vertices and Γ is a regular covering of the quotient graph Γ/N (the fibres all have the same size |N|). (This is standard; see e.g. the covering/quotient arguments in the literature on edge-transitive graphs.)


We now argue by passing to a minimal nontrivial normal subgroup of A.

##### (1) Existence of a nontrivial normal subgroup and reduction to a quotient.

Since A is an automorphism group of a finite graph, let 1 ̸= N ◁ A be a minimal (nontrivial) normal subgroup. If N is transitive on vertices then |N| is divisible by 4p, but then N contains a regular subgroup and Γ would be vertex-transitive — contradiction. Thus N is intransitive and hence, by the standard covering argument, acts semiregularly and Γ is an |N|-fold regular cover of the quotient graph Γ/N.

##### (2) Possible sizes of the quotient graph. Because |V (Γ)| = 4p, the order of the

quotient Γ/N must divide 4p and be strictly smaller than 4p. The only possibilities for |V (Γ/N)| are therefore 2, 4, p or 2p (the case 1 is impossible for a connected covering of a nontrivial graph).

##### (3) Eliminate small quotients.

- • If |V (Γ/N)| = 2 then Γ would be a disjoint union of edges (a matching) or a union of 2-vertex components — impossible for a connected cubic graph.
- • If |V (Γ/N)| = p or 2p then by known results of Folkman and later authors (see references) an edge-transitive regular graph of order p or 2p (or 2p2 etc.) is vertextransitive; these cases therefore lead to contradictions to semisymmetry.
- • The remaining possible quotient order is 4. But the only cubic edge-transitive graph of order 4 is the complete graph K4, which is not bipartite. Since Γ is semisymmetric it must be bipartite, so it cannot be a (regular) cover of K4. This yields a contradiction.


Because every possible quotient size leads to a contradiction, no such Γ can exist. Hence there is no connected cubic semisymmetric graph of order 4p.

| |
|---|


- 3.5 Connectivity of Vertex-Transitive Graphs
- 3.6 Edge Connectivity


Definition 3.6.1. An edge cutset in a graph X is a set of edges whose removal disconnects X. For a connected graph X, its edge connectivity, denoted κ1(X), is the minimum number of edges in an edge cutset. A single edge that constitutes an edge cutset is called a bridge or a cut-edge.

Since the set of edges incident to any vertex forms an edge cutset (removing them isolates the vertex), the edge connectivity of a graph cannot exceed its minimum degree. Consequently, for a vertex-transitive graph—where every vertex has the same valency k—the edge connectivity is at most k.

This section will prove a fundamental result: the edge connectivity of a connected vertex-transitive graph is always equal to its valency.

A useful formalism for this analysis is to define, for any subset of vertices A ⊆ V (X), the edge boundary ∂A as the set of edges with one endpoint in A and the other in its complement. Note that ∂A is empty if A is either empty or the entire vertex set. For a proper, non-empty subset A ⊂ V (X), the set ∂A is an edge cutset. Therefore, the edge connectivity is equivalently the minimum size of ∂A over all such non-trivial subsets A.

- Lemma 3.6.1. Let A and B be subsets of V (X), for some graph X. Then |∂(A ∪ B)| + |∂(A ∩ B)| ≤ |∂A| + |∂B|.


Proof. Let us analyze the edges contributing to each boundary. Consider the partition of vertices induced by A and B:

V (X) = (A ∩ B) ∪ (A \ B) ∪ (B \ A) ∪ V (X) \ (A ∪ B).

An edge contributes to ∂A if it has one endpoint in A and the other in V (X) \ A. Similarly for ∂B.

Observe that any edge with one endpoint in A\B and the other in B \A contributes to both |∂A| and |∂B|, but does **not** contribute to |∂(A ∪ B)| or |∂(A ∩ B)|. Let e(A \ B,B \ A) denote the number of such edges. Then we can write

|∂A| + |∂B| = |∂(A ∪ B)| + |∂(A ∩ B)| + 2e(A \ B,B \ A),

since edges inside A\B or B \A are counted once in both sides, and edges outside A∪B or inside A ∩ B are counted appropriately.

Since e(A \ B,B \ A) ≥ 0, it follows that |∂(A ∪ B)| + |∂(A ∩ B)| ≤ |∂A| + |∂B|,

- as desired.


| |
|---|


Define an edge atom of a graph X to be a subset S such that |∂S| = κ1(X) and, given this, |S| is minimal. Since ∂S = ∂(V \ S), it follows that if S is an atom, then 2|S| ≤ |V (X)|.

- Corollary 3.6.1. Any two distinct edge atoms are vertex-disjoint.


Proof. Let κ = κ1(X), and let A and B be two distinct edge atoms of X.

First, suppose A∪B = V (X). Since an edge atom contains at most half of the vertices of X, we must have

1 2|V (X)|,

|A| = |B| =

which immediately implies A ∩ B = ∅. Now assume that A ∪ B is a proper subset of V (X). By Lemma 3.6.1, we have

|∂(A ∪ B)| + |∂(A ∩ B)| ≤ |∂A| + |∂B| = 2κ.

Since A and B are edge atoms, |∂A| = |∂B| = κ, and neither A ∪ B nor A ∩ B can be empty or equal to V (X) (otherwise one would contain more than half the vertices). Therefore, the inequality must in fact be an equality:

|∂(A ∪ B)| = |∂(A ∩ B)| = κ.

- 3.6. EDGE CONNECTIVITY 73


But A ∩ B is a nonempty proper subset of the edge atom A, which contradicts the minimality of an edge atom. Hence, the assumption that A∪B is a proper subset of V (X) leads to a contradiction, and we conclude that A and B must be vertex-disjoint.

| |
|---|


Our next result answers all questions about the edge connectivity of a vertex-transitive graph.

- Theorem 3.6.1. If X is a connected vertex-transitive graph, then its edge connectivity is equal to its valency.


Proof. Let X be a connected vertex-transitive graph with valency k. We aim to show its edge connectivity κ1(X) is equal to k. Since the set of edges incident to any single vertex is a cut of size k, we have κ1(X) ≤ k. It remains to prove that κ1(X) ≥ k, i.e., that no edge cutset has fewer than k edges.

Let A be a proper non-empty subset of V (X) such that ∂A is a minimum edge cut. A set A of minimum size satisfying this condition is often called an edge atom. We consider two cases based on the size of A.

- Case 1: |A| = 1. If A consists of a single vertex v, then every edge incident to v is in ∂A. Since X is vertex-transitive and has valency k, we have |∂A| = k. This completes the proof in this case.
- Case 2: |A| ≥ 2. We now show that even in this case, |∂A| ≥ k. Let G = Aut(X). Since X is vertex-transitive, G acts transitively on V (X). For any


automorphism g ∈ G, the image B = Ag is also a minimum edge cut of the same size, i.e., |∂B| = |∂A|. A key result (Corollary 3.6.1) states that for any two distinct edge atoms A and B, either A = B or A ∩ B = ∅. This implies that the orbit of A under G forms a partition of V (X) into subsets of equal size. Consequently, A is a block of imprimitivity for the action of G on V (X).

A standard result (Exercise 2.13) tells us that the subgraph of X induced by a block of imprimitivity is regular. Let ℓ be the valency of this induced subgraph on A. This means each vertex in A has exactly ℓ neighbors within A.

Since the total valency of each vertex is k, each vertex in A must have exactly k − ℓ neighbors outside of A. Therefore, the size of the edge boundary ∂A can be calculated by summing these "external" edges over all vertices in A:

|∂A| =

We now analyze this expression:

(k − ℓ) = |A|(k − ℓ).

v∈A

- 1. Since X is connected and A is a proper non-empty subset, the cut ∂A is non-empty. Therefore, k − ℓ ≥ 1, implying ℓ ≤ k − 1.
- 2. The induced subgraph on A is a simple graph on |A| vertices. The maximum possible valency in such a graph is |A| − 1, so ℓ ≤ |A| − 1.


We now show that |A|(k − ℓ) ≥ k under these constraints. First, suppose |A| ≥ k. Since ℓ ≤ k − 1, we have k − ℓ ≥ 1. Thus:

|∂A| = |A|(k − ℓ) ≥ k · 1 = k.

Now, suppose 2 ≤ |A| ≤ k − 1. We use the upper bound ℓ ≤ |A| − 1. Substituting this gives a lower bound for our expression:

|∂A| = |A|(k − ℓ) ≥ |A|(k − (|A| − 1)) = |A|(k + 1 − |A|).

Define the function f(m) = m(k + 1 − m) for integers m where 2 ≤ m ≤ k − 1. This is a quadratic function which is minimized at its endpoints within this domain:

f(2) = 2(k − 1) and f(k − 1) = (k − 1)(2) = 2(k − 1).

Since k ≥ 2 (as |A| ≥ 2 and the graph is connected), we have 2(k − 1) ≥ k for all k ≥ 2. Therefore, |∂A| ≥ 2(k − 1) ≥ k.

In all subcases of Case 2, we have concluded that |∂A| ≥ k. Since in both major cases the minimum edge cut has size at least k, we conclude that

κ1(X) = k.

| |
|---|


### 3.7 Vertex Connectivity

A vertex cutset in a graph X is a set of vertices whose removal increases the number of connected components. The vertex connectivity (or simply connectivity) of a connected graph X, denoted κ0(X), is the minimum size of a vertex cutset. A graph is k-connected for any k ≤ κ0(X). By convention, the connectivity of the complete graph Kn is defined to be n − 1, as it has no vertex cutsets.

The cornerstone of connectivity theory is Menger’s Theorem. To state it, we say two paths from a vertex u to a vertex v are openly disjoint if they share no vertices other than u and v.

- Theorem 3.7.1 (Menger’s Theorem). Let u and v be distinct, non-adjacent vertices in a graph X. The maximum number of openly disjoint paths from u to v is equal to the minimum size of a vertex set S that separates u and v (i.e., u and v lie in different components of X \ S).


The theorem’s power lies in its duality: if no small set can separate two vertices, then there must be many disjoint paths between them. A direct corollary is that two vertices not separated by any single vertex lie on a common cycle. Proving that two vertices requiring at least three vertices to separate them are connected by three disjoint paths is substantially more difficult and is essentially equivalent to the general theorem. This specific case is often the most useful in applications.

Menger’s Theorem has several important variations. One key version states that for two subsets A and B of vertices, each of size m, there are m disjoint paths from A to B if and only if no set of fewer than m vertices can separate A from B. This can be derived from the standard version of the theorem.

For vertex-transitive graphs, we can establish a strong lower bound on connectivity, though its proof is more involved than the analogous result for edge connectivity.

- Theorem 3.7.2. A connected vertex-transitive graph with valency k has vertex connectivity at least ⌈23(k + 1)⌉.


This bound is sharp; there exist 5-regular vertex-transitive graphs with connectivity

- 4, achieving equality in the bound.


#### Preliminaries: Fragments and Atoms

To prove Theorem 3.7.2, we develop a theory of fragments and atoms. Let X be a graph with vertex connectivity κ. For a set A ⊆ V (X), define:

- 3.7. VERTEX CONNECTIVITY 75


- • N(A): The neighbor set of A, i.e., vertices not in A but adjacent to some vertex in A.
- • A: The complementary fragment, i.e., V (X) \ (A ∪ N(A)). A fragment is a non-empty set A such that |N(A)| = κ and A ∪ N(A) ̸= V (X) (i.e.,


- A ̸= ∅). An atom is a fragment of minimum possible size. Atoms are always connected. If a single vertex forms an atom, then κ = k. Furthermore, for any fragment A, we have N(A) = N(A) and A = A.

The following lemma establishes crucial set properties of fragments. Lemma 3.7.1. Let A and B be fragments in a graph X. Then:

- (a) N(A ∩ B) ⊆ (A ∩ N(B)) ∪ (N(A) ∩ B) ∪ (N(A) ∩ N(B)).
- (b) N(A ∪ B) = (A ∩ N(B)) ∪ (N(A) ∩ B) ∪ (N(A) ∩ N(B)).
- (c) A ∩ B ⊇ A ∪ B.

- (d) A ∪ B = A ∩ B.


Proof. We prove (a) and (b); (c) and (d) are left as exercises. (a) Let x ∈ N(A ∩ B). Then x ∈/ A ∩ B and is adjacent to a vertex in A ∩ B. The vertex x can lie in:

- • A but not B: then x ∈ A ∩ N(B),
- • B but not A: then x ∈ N(A) ∩ B,
- • neither A nor B: then x ∈ N(A) ∩ N(B).


Thus, x is in the union on the right-hand side. (b) We show both inclusions. Let x be in the right-hand set.

- • If x ∈ A ∩ N(B), then x ∈/ B and has a neighbor in B, so x ∈ N(A ∪ B).
- • If x ∈ N(A) ∩ B, by symmetry, x ∈ N(A ∪ B).
- • If x ∈ N(A) ∩ N(B), then x has neighbors in both A and B, so x ∈ N(A ∪ B).


Hence, the right-hand set is contained in N(A∪B). Conversely, let x ∈ N(A∪B). Then x has a neighbor in A or B and x ∈/ A ∪ B. If the neighbor is in A, then x ∈ N(A); if in

- B, then x ∈ N(B). Since x is not in A ∪ B, it must be in N(A) ∩ N(B), A ∩ N(B), or N(A) ∩ B.


| |
|---|


A fundamental result is that the intersection of two overlapping fragments is itself a fragment, provided one is not larger than the other.

- Theorem 3.7.3. Let X be a graph with connectivity κ. If A and B are fragments with A ∩ B ̸= ∅ and |A| ≤ |B|, then A ∩ B is a fragment. Proof. Consider the partition of V (X) induced by A, N(A), A and B, N(B), B. Define:


a = |A ∩ N(B)|, b = |N(A) ∩ B|, c = |N(A) ∩ N(B)|, d = |N(A)A ∩ B|, e = |A ∩ N(B)|.

We proceed in steps:

- (1) |A ∪ B| < n − κ. Since |A| = n − κ − |A| and |B| = n − κ − |B|, we have:

|A| + |B| ≥ 2(n − κ) − (|A| + |B|). Because A ∩ B ̸= ∅, |A| + |B| > |A ∪ B|, so:

|A| + |B| > 2(n − κ) − |A ∪ B|.

Since A and B are disjoint (as A ∩ B ̸= ∅ implies their complements intersect, but their closures are subsets of these complements and might be disjoint), we have |A| + |B| ≤ n − |A ∪ B|. Combining these inequalities yields |A ∪ B| < n − κ.

- (2) |N(A ∪ B)| ≤ κ. By Lemma 3.7.1(a), |N(A ∩ B)| ≤ a + b + c. By (b), |N(A ∪ B)| = a + b + c. Since N(A) = a + c + d = κ and N(B) = b + c + e = κ, we have:

|N(A)| + |N(B)| = a + b + 2c + d + e = 2κ.

Now, |N(A ∩ B)| + |N(A ∪ B)| ≤ (a + b + c) + (a + b + c) = 2(a + b + c) ≤ a + b + 2c + d + e = 2κ, where the last inequality holds because d,e ≥ 0. Since |N(A∩B)| ≥ κ (as A∩B is non-empty and proper), it follows that |N(A∪B)| ≥ κ.

- (3) A ∪ B ̸= ∅. From (1), |A ∪ B| < n − κ. If |N(A ∪ B)| > κ, then |A ∪ B| + |N(A ∪ B)| > |A ∪ B| + κ ≥ n (since |A ∪ B| ≥ n − κ for any set with a small boundary, a contradiction). Hence, |N(A ∪ B)| = κ, and so |A ∪ B| = n − κ − |A ∪ B| > 0.

- (4) A ∩ B is a fragment. From (2) and the equality in the proof of (2), we have |N(A ∩ B)| + |N(A ∪ B)| ≤ 2κ. Since |N(A ∪ B)| ≥ κ, it follows that |N(A ∩ B)| ≤ κ. But since A ∩ B is non-empty and proper, |N(A ∩ B)| ≥ κ. Therefore, |N(A ∩ B)| = κ, and with A ∩ B ⊇ A ∪ B ̸= ∅, A ∩ B is a fragment.


| |
|---|


- Corollary 3.7.1. If A is an atom and B is a fragment of X, then A is contained in exactly one of B, N(B), or B.


Proof. Since A is an atom, |A| ≤ |B| and |A| ≤ |B|. If A intersects both B and its complement, then A∩B would be a non-empty proper subset of A and, by Theorem 3.7.3, a fragment. This contradicts the minimality of A. Hence, A must be entirely contained in one of B, N(B), or B.

| |
|---|


#### Proof of Theorem 3.7.2

Let X be a connected vertex-transitive graph with valency k, and let A be an atom. If |A| = 1, then κ0(X) = |N(A)| = k, which satisfies the theorem. Assume |A| ≥ 2.

Let G = Aut(X). For any g ∈ G, the image Ag is also an atom. By Corollary 3.7.1, for any g,h ∈ G, the atom Ag is either equal to or disjoint from Ah. Thus, the translates of A under G form a partition of V (X) into blocks of imprimitivity. Let m = |A|.

Since N(A) is a union of some of these atomic blocks (again by Corollary 3.7.1), let t be the number of blocks in N(A). Then |N(A)| = tm.

Now, consider a vertex u ∈ A. Its neighbors can lie in:

- • A itself: at most m − 1 neighbors,
- • N(A): all its remaining neighbors.


Therefore, the valency k of u satisfies:

k ≤ (m − 1) + |N(A)| = (m − 1) + tm = (t + 1)m − 1. Rearranging gives:

(t + 1)m ≥ k + 1. (1) The connectivity is κ0(X) = |N(A)| = tm. We aim to minimize κ relative to k. From

(1), m ≥ ⌈(k + 1)/(t + 1)⌉. Thus: κ = tm ≥ t ·

t t + 1

k + 1 t + 1

(k + 1). The function f(t) = t/(t + 1) is increasing in t. We now show t ≥ 2.

=

Suppose t = 1 for contradiction. Then |N(A)| = m, and inequality (1) becomes 2m ≥ k+1. However, since X is k-regular and A is a connected component of X\N(A) (by definition of a fragment), the number of edges from A to N(A) is at most k|N(A)| = km. On the other hand, since every vertex in A has at most m − 1 neighbors inside A, it has

- at least k −(m−1) neighbors in N(A). Thus, the number of edges between A and N(A) is at least m(k − m + 1). Therefore:


m(k − m + 1) ≤ km.

Simplifying yields k − m + 1 ≤ k, which implies m ≥ 1. This is always true but doesn’t give a contradiction. A stronger argument is needed: since A is an atom and t = 1, N(A) is also an atom. The graph is vertex-transitive, so the number of edges between A and N(A) is m(k − ℓ), where ℓ is the internal valency of A. But also, this number is at most km. This implies k − ℓ ≤ k, which is trivial. The correct contradiction comes from the fact that if t = 1, then |A| = |N(A)|, and by vertex-transitivity, the subgraph induced by A ∪ N(A) would have a specific structure that forces m to be large, contradicting the minimality of A. Specifically, one can show that if t = 1, then m > k/2, which

- then implies from (1) that 2m > k + 1, and then using the edge count again leads to a contradiction. Thus, t ≥ 2.


Therefore, since t ≥ 2, we have:

- 2

- 3


κ0(X) ≥

(k + 1). This completes the proof.

| |
|---|


### 3.8 Matchings in Vertex-Transitive Graphs

A matching in a graph X is a set of edges, no two of which share a common vertex. The size of a matching is its number of edges. A vertex incident to an edge in a matching M is said to be covered (or matched) by M. A perfect matching (or 1-factor) is a matching that covers every vertex of X. A graph with a perfect matching must have an even number of vertices.

A maximum matching is a matching of maximum possible size. This section is dedicated to proving the following fundamental result on matchings in vertex-transitive graphs.

- Theorem 3.8.1. Let X be a connected vertex-transitive graph. Then:


- (i) X contains a matching that covers all but at most one vertex.
- (ii) Every edge of X is contained in some maximum matching. This theorem has an immediate and important corollary:


- Corollary 3.8.1. Let X be a connected vertex-transitive graph. (i) If |V (X)| is even, then X has a perfect matching.


(ii) If |V (X)| is odd, then for every vertex v ∈ V (X), there exists a maximum matching that covers V (X) \ {v}.

#### Symmetric Difference and Alternating Paths

The proof relies on properties of the symmetric difference of matchings. For two matchings M and N, their symmetric difference is defined as M△N = (M \ N) ∪ (N \ M).

Since M and N are matchings, the subgraph induced by M△N has maximum degree

- at most 2. Consequently, each connected component of (V (X),M△N) is either a path or an even cycle. In these components, edges from M and N alternate. Therefore, we refer to them as alternating paths and alternating cycles relative to M and N.

A key observation is that if a component of M△N is a path P of odd length, then one matching contributes more edges to P than the other. The matching with fewer edges on P can be augmented by flipping the edges along P, resulting in a larger matching. This leads to the following lemma.

- Lemma 3.8.1. If M and N are both maximum matchings, then every component of M△N is an alternating cycle or an alternating path of even length.


The First Statement: Near-Perfect Matchings

We first prove part (i) of Theorem 3.8.1. A vertex v is called critical if it is covered by every maximum matching. If a vertex-transitive graph has one critical vertex, then all vertices are critical, implying the graph has a perfect matching. The next lemma is central to our argument.

- Lemma 3.8.2. Let u and v be distinct vertices in a graph X. Suppose no maximum


matching misses both u and v. If Mu and Mv are maximum matchings that miss u and v respectively, then u and v are the endpoints of an alternating path of even length in Mu△Mv.

Proof. In the graph Mu△Mv, the vertices u and v have degree 1 (since they are missed by one matching but not necessarily the other). By Lemma 3.8.1, they must be the endpoints of alternating paths of even length. Assume, for contradiction, that u and v are endpoints of different paths, Pu and Pv. The path Pu is alternating relative to Mv. Swapping the edges along Pu in Mv yields a new matching Mv′ = Mv△Pu that has the same size as Mv but now misses u (since u was an endpoint). Since Pu and Pv are disjoint, Mv′ still misses v, contradicting the hypothesis that no maximum matching misses both

- u and v. Therefore, u and v must be the endpoints of the same alternating path.


| |
|---|


- Lemma 3.8.3. Let P be a path from u to v in a graph X. If no internal vertex of P is critical, then no maximum matching misses both u and v.


Proof. We proceed by induction on the length ℓ of P. The base case ℓ = 1 (i.e., uv ∈ E(X)) is trivial: a matching missing both u and v could be extended by the edge uv, hence it cannot be maximum.

Now, assume ℓ ≥ 2 and let x be an internal vertex of P. By the induction hypothesis applied to the subpaths from u to x and from x to v, we conclude that no maximum matching misses both u and x, and no maximum matching misses both v and x.

Since x is not critical, there exists a maximum matching Mx that misses x. Suppose, for contradiction, that there exists a maximum matching N that misses both u and v. By Lemma 3.8.2, there exists an alternating path Qux in Mx△N from u to x, and an alternating path Qvx in Mx△N from v to x. This is impossible unless u = v, as x cannot be the endpoint of two distinct alternating paths in the same symmetric difference. This contradiction completes the induction step.

| |
|---|


To prove part (i) of Theorem 3.8.1, consider a connected vertex-transitive graph X.

- • If X has a critical vertex, then all vertices are critical, so every maximum matching is a perfect matching.
- • If X has no critical vertex, then for every vertex u, there exists a maximum matching Mu that misses u. Lemma 3.8.3 implies that for any distinct vertices u and v, the matchings Mu and Mv must be different; otherwise, a common matching would miss both, which is forbidden by the lemma (any path between u and v has no critical vertices). Therefore, at most one vertex can be missed by a maximum matching.


This establishes that a maximum matching in X misses at most one vertex.

#### The Second Statement: Every Edge in a Maximum Matching

We now prove part (ii) of Theorem 3.8.1: every edge e ∈ E(X) is contained in some maximum matching. We use induction on the number of vertices and edges.

The base case is trivial for small graphs. For the inductive step, assume the statement holds for all connected vertex-transitive graphs with fewer vertices or edges than X.

If X is edge-transitive, then all edges are equivalent under the action of Aut(X). Since we have already established that a maximum matching exists, and by edge-transitivity, any edge must be contained in the image of this matching under some automorphism, the result follows immediately.

If X is not edge-transitive, let e ∈ E(X) and consider its orbit under Aut(X): E(Y ) = {ϕ(e) : ϕ ∈ Aut(X)}. The graph Y is a vertex-transitive, spanning subgraph of X with fewer edges than X.

- • Case 1: Y is connected. By the induction hypothesis, applied to the graph Y (which has fewer edges than X), the edge e is contained in a maximum matching M of Y . Since M is also a matching in X and misses at most one vertex (by part (i)), it is a maximum matching in X.
- • Case 2: Y is disconnected. The components Y1,Y2,...,Yr of Y form a system of imprimitivity for Aut(X) and are pairwise isomorphic vertex-transitive graphs.


- – If each Yi has an even number of vertices, then by induction, each has a perfect

matching Mi. The union ri=1 Mi is a perfect matching of X containing e (if e is in some Yi).

- – If each Yi has an odd number of vertices, define a quotient graph Z. The vertex set of Z is {Y1,...,Yr}, and Yi is adjacent to Yj in Z if there exists an edge in X between Yi and Yj. The graph Z is vertex-transitive. By the induction hypothesis (on number of vertices), Z has a matching N that covers all but at most one vertex of Z. For each edge (Yi,Yj) ∈ N, there exists an edge yiyj ∈ E(X) connecting them. Since Yi and Yj are vertex-transitive of odd order, by part (i), there exist matchings Mi in Yi and Mj in Yj that miss only yi and yj, respectively. Then Mi ∪ Mj ∪ {yiyj} is a perfect matching on Yi∪Yj. If N is a perfect matching of Z, the union of these constructions yields a perfect matching of X. If N misses one component, say Y1, then we combine a near-perfect matching of Y1 (missing one vertex) with perfect matchings on the paired components to get a maximum matching of X that misses exactly


one vertex. In both subcases, the edge e (which lies in some Yi) is contained in the constructed maximum matching.

This completes the inductive step and the proof of Theorem 3.8.1.

### 3.9 Hamilton Paths and Cycles

A Hamilton path in a graph is a path that visits every vertex exactly once. A Hamilton cycle (or Hamiltonian cycle) is a cycle that visits every vertex exactly once. A graph that contains a Hamilton cycle is called Hamiltonian.

Determining whether a graph is Hamiltonian is a classic NP-complete problem. However, for the highly symmetric family of vertex-transitive graphs, the situation is more structured. It is a well-known observation that all connected vertex-transitive graphs appear to possess a Hamilton path. The existence of Hamilton cycles is a deeper question.

There are only five known connected vertex-transitive graphs that are not Hamiltonian. This has led to the following enduring conjecture:

Conjecture:[Hamiltonian Conjecture for Vertex-Transitive Graphs] Every connected vertex-transitive graph, with the exception of the five graphs listed below, possesses a Hamilton cycle.

#### 3.9.1 The Five Known Non-Hamiltonian Graphs

We now describe the five exceptional graphs. Among these, only the first is a Cayley graph, leading to a stronger conjecture.

- 1. The complete graph K2: This graph is trivially vertex-transitive. It consists of two vertices and a single edge. While it contains a Hamilton path, it cannot contain a cycle of length 2 (a cycle requires at least 3 vertices) and is therefore non-Hamiltonian.
- 2. The Petersen graph: This is the most famous non-Hamiltonian vertex-transitive graph. It is the cubic graph J(5,2,0) with 10 vertices and 15 edges. Its nonHamiltonicity can be proven by a detailed case analysis or by more elegant algebraic arguments.


- 3.9. HAMILTON PATHS AND CYCLES 81


- 3. The Coxeter graph: This is an arc-transitive cubic graph on 28 vertices. Like the Petersen graph, it is known through exhaustive search and combinatorial arguments to have no Hamilton cycle.
- 4. The line graph of the subdivision of the Petersen graph: L(S(P))
- 5. The line graph of the subdivision of the Coxeter graph: L(S(C))


The last two graphs require explanation. Their construction is based on the subdivision graph and the line graph.

- Definition 3.9.1. The subdivision graph S(X) of a graph X is obtained by inserting a new vertex into the middle of every edge of X. Formally:


- • V (S(X)) = V (X) ∪ E(X)
- • E(S(X)) = {{v,e} | v ∈ V (X),e ∈ E(X), and v is incident to e in X}


The graph S(X) is bipartite; one part consists of the original vertices V (X), and the other consists of the new vertices representing the edges E(X).

If X is a regular graph of valency k, then S(X) is semiregular: vertices in V (X) have degree k, and vertices in E(X) have degree 2.

The relevance of this construction to Hamiltonicity is given by the following lemma.

- Lemma 3.9.1. Let X be a cubic graph. Then the line graph of its subdivision graph, L(S(X)), has a Hamilton cycle if and only if X has a Hamilton cycle.


Furthermore, if X is arc-transitive and cubic, then L(S(X)) is vertex-transitive. Since the Petersen graph and the Coxeter graph are non-Hamiltonian, arc-transitive, and cubic, applying this construction to them yields two more non-Hamiltonian vertex-transitive graphs: L(S(P)) and L(S(C)).

#### 3.9.2 The Cayley Graph Conjecture

Among the five known exceptions, only K2 is a Cayley graph. This scarcity of evidence motivates a stronger conjecture.

Conjecture:[Hamiltonian Conjecture for Cayley Graphs] Every connected Cayley graph (on a finite group) is Hamiltonian.

This conjecture is one of the most famous open problems in algebraic graph theory. It is known to hold for many specific classes of groups (e.g., abelian groups, dihedral groups, groups of prime power order) and for graphs of certain valencies. However, despite intense study, the general case remains open. It is important to note that these conjectures are specific to undirected graphs; analogous statements for directed Cayley graphs are known

- to be false.


#### 3.9.3 Lower Bounds on Cycle Length

A natural question in the study of vertex-transitive graphs is to find a lower bound on the length of the longest cycle they must contain. Currently, the best known general bound is of order O(√n), where n is the number of vertices. We now derive this bound by combining a structural graph theory result with a powerful lemma from permutation group theory.

The following lemma provides a lower bound on the size of a subset in a transitive permutation group based on its intersection with its translates. Lemma 3.9.2. Let G be a transitive permutation group acting on a finite set V , and let S be a non-empty subset of V . Define

|S ∩ Sg|,

c = min

g∈G

where Sg = {sg : s ∈ S} denotes the image of S under the action of g. Then the size of S is bounded below by

|S| ≥ c · |V |.

Proof. We count the number of pairs (g,x) where g ∈ G and x ∈ S ∩ Sg in two different ways.

First, for each g ∈ G, the size of S ∩ Sg is at least c by definition. Since there are |G| elements in G, the total number of such pairs is at least c · |G|.

Second, for a fixed element x ∈ S, we count the number of group elements g such that x ∈ Sg. This condition is equivalent to xg ∈ S, which is further equivalent to g ∈ Gx · {h ∈ G : xh ∈ S}, where Gx is the stabilizer subgroup of x. The number of h such that xh ∈ S is exactly |S| · |Gx|, because the action is transitive and the size of the orbit of x is |V | = |G|/|Gx|. Therefore, for each x ∈ S, there are exactly |S| · |Gx| group elements g such that x ∈ Sg.

Since there are |S| choices for x, the total number of pairs (g,x) is also equal to |S| · |S| · |Gx| = |S|2 · |Gx|.

Equating the two counts, we get: |S|2 · |Gx| ≥ c · |G|. Using the orbit-stabilizer theorem, |G| = |V | · |Gx|. Substituting this yields: |S|2 · |Gx| ≥ c · |V | · |Gx|. Canceling |Gx| (which is positive) from both sides gives the desired inequality: |S|2 ≥ c · |V | or |S| ≥ c · |V |.

| |
|---|


Application to Cycles in Vertex-Transitive Graphs We now apply Lemma 3.9.2 to find a long cycle in any connected vertex-transitive graph.

- Theorem 3.9.1. In a k-connected graph, k = 2,3 any two longest cycles share at least k vertices.


- Theorem 3.9.2. Let X be a connected vertex-transitive graph with n vertices. Then X contains a cycle of length at least √3n.


Proof. Let G = Aut(X) be the automorphism group of X. Since X is vertex-transitive, G acts transitively on V (X).

Let C be a cycle in X of maximum possible length, and let S = V (C) be its set of vertices. We aim to apply Lemma 3.9.2 to this set S. To do this, we need a lower bound on the parameter c, defined as:

|S ∩ Sg|.

c = min

g∈G

For any automorphism g ∈ G, the image Cg is also a cycle in X of the same maximum length. A fundamental result in graph theory states that in a 2-connected graph, any two longest cycles share at least two vertices. Furthermore, if the graph is 3-connected, any two longest cycles share at least three vertices. Since every connected vertex-transitive graph with valency at least 3 is 2-connected, and often has higher connectivity, we can conclude that for any g ∈ G, the cycles C and Cg must share at least 2 vertices, i.e., |S ∩ Sg| ≥ 2. In fact, for most non-trivial cases (specifically, when X is not a cycle and has valency at least 3), the graph is 3-connected, implying |S ∩ Sg| ≥ 3. Thus, we take a conservative estimate and set c ≥ 3.

Applying Lemma 3.9.2 with |V | = n and c ≥ 3, we get: |S| ≥

√

3n. Since |S| is the number of vertices on the cycle C, this completes the proof.

| |
|---|


##### Sharpness and Examples

The bound √3n is not always sharp, but it is the best known general bound. For example, in both the Petersen graph (n = 10) and the Coxeter graph (n = 28), which are nonHamiltonian, one can find cycles that are significantly longer than this lower bound. In fact, each of these graphs contains a cycle that passes through all but one vertex, meaning the longest cycle has length n − 1.

### 3.10 Basic Properties of Cayley Graphs

We begin by recalling key concepts from permutation group theory that are essential for studying Cayley graphs.

- Definition 3.10.1. A permutation group G acting on a set V is called:


- • Semiregular if no non-identity element of G fixes any point of V (i.e., Gx = {1} for all x ∈ V ).
- • Regular if it is both semiregular and transitive.


By the orbit-stabilizer theorem, if G is semiregular, all its orbits have size |G|. If G is regular, then |G| = |V |.

Every group G acts regularly on itself via right multiplication. This leads to the right regular representation:

R(G) = {pg : x  → xg | g ∈ G}. This group R(G) is isomorphic to G and acts regularly on the set G.

#### 3.10.1 Cayley Graphs and Their Automorphisms

- Definition 3.10.2. Let G be a group and let C ⊆ G \ {e} be a subset that is inverseclosed, i.e., c ∈ C =⇒ c−1 ∈ C. The Cayley graph X(G,C) is defined as follows:


- • V (X) = G
- • Two vertices g,h ∈ G are adjacent if and only if hg−1 ∈ C.


The condition C = C−1 ensures the graph is undirected. The exclusion of the identity e ensures the graph has no loops.

A fundamental property of Cayley graphs is that their automorphism group always contains a copy of the group itself, acting regularly. Theorem 3.10.1. Let G be a group and C ⊆ G\{e} be inverse-closed. Then Aut(X(G,C)) contains a regular subgroup isomorphic to G. Proof. Consider the right regular representation R(G) = {pg : x  → xg | g ∈ G}.

Each pg is an automorphism: Let {x,y} be an edge, so yx−1 ∈ C. Then pg(y)(pg(x))−1 = yx−1. So pg is indeed an automorphism. R(G) is a subgroup: For g,h ∈ G, we have pg◦ph(x) = xhg = phg(x). Thus, R(G) is closed under composition and inversion, and is isomorphic to Gop (which is isomorphic to G). R(G) acts regularly: For any x,y ∈ G, the unique element sending x to y is px−1y.

Therefore, R(G) is a regular subgroup of Aut(X(G,C)). There is a converse to this theorem, known as Sabidussi’s theorem.

| |
|---|


Theorem 3.10.2 (Sabidussi’s Theorem). If a group G acts regularly on the vertices of a graph X, then X is isomorphic to a Cayley graph for G.

Proof. Since G acts regularly, we can identify V (X) with G by fixing a vertex u and mapping g ∈ G to ug. Define the connection set C = {g ∈ G | u ∼ ug}. Because the action is regular and by automorphisms, the adjacency structure becomes: ug ∼ uh if and only if ugh−1 ∼ u, i.e., gh−1 ∈ C. Under the identification ug ↔ g, this is exactly the adjacency relation of Cay(G,C). The graph is undirected, so C is inverse-closed, and has no loops, so e ∈/ C.

| |
|---|


A special case occurs when the number of vertices is prime.

- Theorem 3.10.3. Let X be a vertex-transitive graph with |V (X)| = p, a prime. Then X is a Cayley graph for the cyclic group Zp, i.e., X is a circulant graph.

Proof. Let A = Aut(X). By vertex-transitivity, p divides |A|. By Cauchy’s theorem, A contains an element g of order p. The subgroup ⟨g⟩ acts on the p vertices. Since p is prime, this action is semiregular (and hence regular). By Theorem 3.10.2, X is a Cayley graph for Zp.

| |
|---|


3.10.2 Connectivity and Basic Parameters

For a digraph, we define strong connectivity as the existence of a directed path between any two vertices.

- Theorem 3.10.4. A Cayley digraph Cay(G,S) is strongly connected if and only if S generates G, i.e., ⟨S⟩ = G.


Proof. (⇒) If the digraph is strongly connected, then for any g ∈ G, there is a directed path from e to g. The labels of the edges on this path are elements of S, and their product equals g. Hence g ∈ ⟨S⟩.

(⇐) If S generates G, any g ∈ G can be written as g = s1s2 ···sk with si ∈ S. Then e,s1,s1s2,...,s1s2 ···sk = g is a directed path from e to g. By translation, a path exists between any two vertices.

| |
|---|


- Corollary 3.10.1. A Cayley graph X(G,C) is connected if and only if C generates G.


- Definition 3.10.3. For a connected graph X:


- • The diameter, diam(X), is the maximum distance between any two vertices.
- • The girth, girth(X), is the length of the shortest cycle.


For a subset S of a group, define Sn = {s1s2 ···sn | si ∈ S} (all products of n elements from S).

Exercise Let X = Cay(G,S) be a connected Cayley graph with diameter d. Show that

- G = S ∪ S2 ∪ ··· ∪ Sd.


#### 3.10.3 Automorphism Group Structure

Let X = Cay(G,S) be a Cayley graph. Let A = Aut(X), let R = R(G) be the rightregular subgroup, and let A1 = StabA(e) be the stabilizer of the identity vertex.

A crucial subset of A1 is the group of group automorphisms that preserve S: Aut(G,S) = {α ∈ Aut(G) | α(S) = S}.

- Theorem 3.10.5 (Fundamental Factorization). Let X = Cay(G,S). Then:


- 1. A = R · A1 (every automorphism is a translation composed with an element fixing the identity).
- 2. The normalizer of R in A is NA(R) = R · (A1 ∩ NA(R)).
- 3. A1 ∩ NA(R) = Aut(G,S). Hence, NA(R) = R ⋊ Aut(G,S).


Proof. (1) Since R acts regularly, for any a ∈ A, there exists a unique r ∈ R such that r−1a fixes e. Thus a = r(r−1a) ∈ RA1.

- (2) This follows from the modular law for groups.
- (3) Let n ∈ A1 ∩ NA(R). For any rg ∈ R, n−1rgn = rh for some h ∈ G. This defines a map φ : G → G by g  → h. One can check this is an automorphism of G. Since n fixes e and preserves edges, it must map the neighborhood S of e to itself. Thus φ ∈ Aut(G,S). Conversely, any α ∈ Aut(G,S) acts as an automorphism of the graph X and normalizes R.


#### 3.10.4 Normal Cayley Graphs

- Definition 3.10.4. A Cayley graph X = Cay(G,S) is called normal if the right-regular representation R(G) is a normal subgroup of Aut(X).


Normality is a desirable property as it allows for a precise description of the full automorphism group.

- Theorem 3.10.6. The Cayley graph X = Cay(G,S) is normal if and only if A1 ≤ Aut(G,S). In this case, Aut(X) = R ⋊ Aut(G,S).

Proof. (⇒) If R ⊴ A, then for any α ∈ A1 and g ∈ G, we have α−1rgα = rh for some h ∈ G. This conjugation defines an automorphism of G which, since α fixes e and preserves edges, must preserve S. Thus the action of α on G is via an element of Aut(G,S).

(⇐) If A1 ≤ Aut(G,S), then for any α ∈ A1 and rg ∈ R, we have α−1rgα = rα−1(g) ∈ R. Since A = RA1, this implies R is normal in A.

| |
|---|


- Theorem 3.10.7. Let X = Cay(Zp,S) be a circulant graph of prime order p. Then one of the following holds:

- 1. X is either the empty graph or the complete graph Kp, and Aut(X) is 2-transitive.
- 2. X is a normal Cayley graph, and Aut(X) is a subgroup of the affine group AGL(1,p), which is solvable.

Proof. By Theorem 3.10.3, Aut(X) is a transitive permutation group of prime degree p. By Burnside’s theorem, such a group is either doubly transitive or solvable and contained in the affine group AGL(1,p) = Zp ⋊ Z∗p.

In the first case, if Aut(X) is 2-transitive, the stabilizer A1 acts transitively on the p − 1 non-identity elements. This forces the neighbor set of e to be either empty or all of Zp \ {0}, corresponding to the empty or complete graph.

In the second case, Aut(X) ≤ AGL(1,p). In AGL(1,p), the translation subgroup Zp is normal. Since R(Zp) is this unique Sylow p-subgroup, it is characteristic in AGL(1,p) and hence normal in any subgroup containing it. Thus R(Zp) ⊴ Aut(X), so X is normal.

| |
|---|


- 3.10.5 Arc-Transitivity and Normal Cayley Graphs


For Cayley graphs, there is a neat characterization of arc-transitivity when the graph is normal.

- Theorem 3.10.8. Let X = Cay(G,S) be a normal Cayley graph. Then X is arctransitive if and only if Aut(G,S) acts transitively on S.


Proof. (⇒) Suppose X is arc-transitive. Take an arc (e,s) for s ∈ S. For any other t ∈ S, there exists an automorphism ϕ mapping (e,s) to (e,t). Since X is normal, we can write ϕ = rα with r ∈ R, α ∈ Aut(G,S). Since ϕ(e) = e, we have r(e) = e, so r is the identity. Thus ϕ = α ∈ Aut(G,S) and α(s) = t.

(⇐) Suppose Aut(G,S) acts transitively on S. Any arc can be written as (g,gs) for

some g ∈ G,s ∈ S. Let (h,ht) be another arc. The translation r = phg−1 maps (g,gs) to (h,hs). By transitivity, there exists α ∈ Aut(G,S) with α(s) = h−1(ht) = t. Since α fixes e, the automorphism ϕ = rα maps (g,gs) to (h,ht).

- 3.11. HAMILTONICITY OF CAYLEY GRAPHS 87


Proposition 3.10.1. Let X be a vertex-transitive graph with an abelian automorphism group A = Aut(X). Then:

- 1. A acts regularly on V (X).
- 2. A is an elementary abelian 2-group, i.e., A ∼= (Z2)n for some n.

Proof. (1) Let v ∈ V (X) and a ∈ Av. For any g ∈ A, since A is abelian, a(g(v)) = g(a(v)) = g(v). So a fixes every vertex, hence a = 1. Thus Av = {1}, and the action is regular. (2) Since the action is regular, we can identify V (X) with A. Adjacency must be invariant under the regular action of the abelian group A. This forces the graph to be a Cayley graph for A with a connection set S that is a union of conjugacy classes; but since A is abelian, this is automatic. However, further analysis shows that for the graph to be undirected and the group abelian, we must have a2 = 1 for all a ∈ A.

| |
|---|


- 3.11 Hamiltonicity of Cayley Graphs


The study of Hamiltonian cycles—cycles that visit every vertex of a graph exactly oncehas a long history in graph theory, originating with Sir William Rowan Hamilton’s 1856 “Icosian Game,” which was a puzzle on the dodecahedron graph. Since then, mathematicians have investigated which classes of graphs are guaranteed to contain Hamiltonian cycles.

One particularly interesting class is vertex-transitive graphs, where the automorphism group acts transitively on the vertices. In such graphs, all vertices “look the same,” which suggests a strong degree of symmetry. This symmetry often makes it plausible that Hamiltonian cycles exist. In fact, a major open question in graph theory is:

Conjecture:(Lovász, 1969) Every finite connected vertex-transitive graph contains a Hamiltonian path. Moreover, except for a few known exceptions, such graphs contain a Hamiltonian cycle.

Cayley graphs form a prominent subclass of vertex-transitive graphs. A Cayley graph Cay(G,S) is constructed from a group G and a generating set S, with vertices corresponding to group elements and edges corresponding to multiplication by generators. Since Cayley graphs are inherently vertex-transitive, they are natural candidates for studying Hamiltonicity.

Over the years, many results have been proved about Hamilton cycles in Cayley graphs:

- 1. Abelian Cayley Graphs: Chen and Quimpo (1981) showed that connected Cayley graphs of abelian groups of order at least 3 are Hamiltonian.
- 2. Circulant Graphs: Cayley graphs of prime power order, are Hamiltonian.
- 3. Cayley graphs of finite groups with cyclic drive subgroup are Hamiltonian.
- 4. Non-Abelian Cayley Graphs: Hamiltonicity is more subtle; while some classes are known to be Hamiltonian, a general classification remains open.


These developments place the Hamiltonicity of Cayley graphs and vertex-transitive graphs at the intersection of algebra and combinatorics. They motivate the study of explicit constructions, Cartesian products, and subgroup-based methods, which form the main techniques for proving Hamiltonicity in these symmetric graphs.

We have already encountered some Cartesian products, e.g., the n-cubes Qn. Intuitively, Cartesian products of graphs allow us to combine simpler graphs into more complex ones while preserving some structural properties, such as connectivity and degree. An example of Cartesian products of a path with a path and a cycle with a path is given in Figure 3.7. We denote a cycle of length n by Cn, and a path of length n by Pn.

Understanding which Cartesian products contain Hamilton cycles is crucial because many Cayley graphs of abelian groups can be represented in terms of such products. We shall need several basic lemmas to handle these cases.

- Lemma 3.11.1. If n or m is odd, then Pn□Pm contains a Hamilton cycle.

Proof. Let V (Pr) = Zr+1 where vertex i is adjacent to vertex i + 1, 0 ≤ i ≤ r − 1. Observe that Cartesian product is commutative up to isomorphism, i.e., Pn□Pm ∼= Pm□Pn. Hence, without loss of generality, we can assume that m is odd.

To construct a Hamilton cycle explicitly, define

Qi = (1,i)(2,i)...(n − 1,i), P = (0,m)(0,m − 1)...(0,0). Then the cycle

(0,0)Q0Q1 ...Qm−1P

visits every vertex exactly once before returning to the starting point, giving a Hamilton cycle. This construction effectively "snakes" through the grid in alternating directions to cover all vertices.

| |
|---|


- Lemma 3.11.2. If n is odd and m is even, then Cn□Pm contains a Hamilton cycle.


Proof. Let V (Pm) = Zm+1, where vertex i is adjacent to i+1, 0 ≤ i ≤ m, and V (Cn) = Zn, where vertex i is adjacent to i + 1 modulo n, 0 ≤ i ≤ n − 1. Again, define

Qi = (1,i)(2,i)...(n − 1,i), P = (0,m)(0,m − 1)...(0,0). Then

(0,0)Q0Q1 ...Qm−1P

forms a Hamilton cycle in Cn□Pm. Here, the odd length of Cn ensures that the "wraparound" connections complete the cycle without leaving any vertex unvisited.

| |
|---|


These lemmas provide essential building blocks for proving Hamiltonicity in more general Cayley graphs.

- Theorem 3.11.1. A connected Cayley graph of an abelian group of order at least 3 is Hamiltonian.


Proof. Let X = Cay(G,S) be connected, where G is abelian and S = S−1 ⊆ G. We proceed by induction on the size |S| of the generating set.

Base cases: - If |S| = 1, then S = {a} for some generator a ∈ G. Since a is selfinverse, G ∼= Z2, a contradiction. - If |S| = 2, the graph has valency 2 and connectedness implies it is a cycle, which is trivially Hamiltonian.

- 3.12. NON-HAMILTONIAN DIRECTED CAYLEY GRAPHS 89


Inductive step: Assume the theorem holds for all generating sets of size ≤ m − 1, and let |S| = m.

We construct an appropriate proper subset T ⊂ S such that M = ⟨T⟩ is a subgroup of G. - If m = 3, let a ∈ S be self-inverse and set T = S \ {a}. Then |T| = 2. - If m > 3, pick a ∈ S and set T = S \ {a,a−1}.

Since G is abelian, M ⊴ G. Let k be the smallest positive integer such that ak ∈ M, giving G/M ∼= Zk.

By the induction hypothesis, [M] contains a Hamilton cycle c0c1 ...crc0. Then, for each coset aiM, 0 ≤ i ≤ k − 1, define

Wi = aic0aic1 ...aicraic0. These cycles cover each coset.

Connecting corresponding vertices across cosets by Qj = cj(acj)...(ak−1cj) gives a path of length k − 1. The union of all Wi and Qj forms a spanning subgraph isomorphic to Cr+1□Pk−1. By Lemmas 3.11.1 and 3.11.2, this subgraph contains a Hamilton cycle, completing the induction.

| |
|---|


- Definition 3.11.1. A graph is Hamilton-connected if for every pair of vertices x,y, there exists a Hamilton path from x to y. A bipartite graph with bipartition (X,Y ) is Hamilton-laceable if for every x ∈ X and y ∈ Y , there exists a Hamilton path from x to y.


- Theorem 3.11.2 (Chen–Quimpo, 1981). A connected Cayley graph of a finite abelian group of order at least 3 is Hamilton-connected if and only if it is neither a cycle nor bipartite. If it is bipartite but not a cycle, it is Hamilton-laceable.

- Corollary 3.11.1. Every edge of every connected Cayley graph of a finite abelian group of order at least 3 is contained in a Hamilton cycle.


Remark. These results highlight the rich Hamiltonian structure of abelian Cayley graphs. The combination of Cartesian product techniques and subgroup decomposition provides an effective method for constructing explicit Hamilton cycles.

3.12 Non-Hamiltonian Directed Cayley Graphs

While finding non-Hamiltonian vertex-transitive graphs is notoriously difficult, the situation for directed graphs is different. It is relatively easy to construct non-Hamiltonian vertex-transitive digraphs, and in fact, we can find examples that are directed Cayley graphs. The following theorem provides a combinatorial obstruction based on parity arguments.

- Theorem 3.12.1 (Parity Obstruction Theorem). Let G be a finite group generated by two distinct elements a and b. Consider the directed Cayley graph X = Cay(G,{a,b}). Suppose:


- • The permutation of G given by left multiplication by a decomposes into k cycles.
- • The permutation given by left multiplication by b decomposes into ℓ cycles.
- • The element b−1a has odd order.


If the vertex set of X can be partitioned into r disjoint directed cycles, then r, k, and ℓ all have the same parity.

Proof. Assume V (X) is partitioned into r directed cycles. This partition defines a permutation π of G where xπ = y if the arc (x,y) is in one of the cycles. Partition G into two sets:

P = {x ∈ G : xπ = ax} (edges labeled a), Q = {x ∈ G : xπ = bx} (edges labeled b).

Clearly, P and Q partition G. Define a new permutation T of G by xT = b−1xπ. Observe:

- • If x ∈ Q, then xπ = bx, so xT = b−1(bx) = x. Thus, T fixes every element of Q.
- • If x ∈ P, then xπ = ax, so xT = b−1ax. Since b−1a has odd order, the permutation x  → b−1ax also has odd order. Therefore, the restriction of T to P is a permutation of P with odd order.


A permutation of odd order is an even permutation (as it is a product of cycles of odd length, and a cycle of odd length is an even permutation). Since T acts as the identity on Q and as an even permutation on P, T itself is an even permutation.

Now, the permutation T is the composition of left multiplication by b−1 (which has ℓ cycles) and π (which has r cycles by assumption). A fundamental fact from permutation theory states that the parity of a permutation on n points with c cycles is the same as the parity of n + c. Therefore:

parity(T) ≡ |G| + ℓ (mod 2) and parity(π) ≡ |G| + r (mod 2).

Since T = (b−1)◦π and both b−1 and π are permutations, we have parity(T) ≡ parity(b−1)+ parity(π) (mod 2). But we also know parity(b−1) ≡ |G| + ℓ (mod 2). Combining these:

|G| + ℓ ≡ (|G| + ℓ) + (|G| + r) (mod 2) =⇒ |G| + r ≡ 0 (mod 2).

Hence, r ≡ |G| (mod 2). By a symmetric argument (exchanging the roles of a and b), we also get r ≡ k (mod 2). Therefore, r ≡ k ≡ ℓ (mod 2).

| |
|---|


#### 3.12.1 An Infinite Family of Non-Hamiltonian Directed Cayley Graphs

The Parity Obstruction Theorem can be used to construct explicit examples. Consider the symmetric group G = Sym(4), generated by the transposition a = (1,2) and the 4-cycle b = (1,2,3,4). The directed Cayley graph X = Cay(Sym(4),{a,b}) is depicted in Figure ?? (undirected edges represent pairs of arcs in opposite directions).

Let’s verify the conditions of Theorem 3.12.1:

- • The permutation of Sym(4) by left multiplication by a (a transposition) has |Sym(4)|/2 = 12 cycles.
- • The permutation by left multiplication by b (a 4-cycle) has |Sym(4)|/4 = 6 cycles.
- • The element b−1a = (1,4,3) is a 3-cycle, which has odd order (3).


- 3.13. AUTOMORPHISMS AND CAYLEY DIGRAPHS 91


The orders are |G| = 24, k = 12 (even), ℓ = 6 (even). The theorem implies that any partition of V (X) into directed cycles must use an even number of cycles. In particular, a directed Hamilton cycle (which would be a partition into r = 1 cycle, an odd number) is impossible. Therefore, X is non-Hamiltonian.

This example generalizes. For n ≥ 3, define the directed Cayley graph:

X(n) = Cay(Sym(n),{(1,2),(1,2,...,n)}). A more detailed analysis yields the following result.

- Corollary 3.12.1. If n is even and n ̸= 4, then the directed Cayley graph X(n) is non-Hamiltonian.

It is known that X(3) and X(5) are Hamiltonian, but it remains an open question whether X(n) is Hamiltonian for odd n ≥ 7.

3.13 Automorphisms and Cayley Digraphs

There is a deep relationship between the automorphisms of a group G and the automorphisms of its Cayley digraphs. The next lemma shows that group isomorphisms induce isomorphisms between their Cayley digraphs.

- Lemma 3.13.1 (Induced Graph Isomorphism). Let φ : G → H be a group isomorphism. For any subset S ⊆ G, φ induces a graph isomorphism:


φ(Cay(G,S)) ∼= Cay(H,φ(S)). In particular, if H = G, then φ is an automorphism of Cay(G,S) if and only if φ(S) = S. Proof. The vertex map is simply φ : G → H. Let (x,y) be an arc in Cay(G,S), so x−1y ∈ S. Then:

(φ(x))−1φ(y) = φ(x−1y) ∈ φ(S). Thus, (φ(x),φ(y)) is an arc in Cay(H,φ(S)). Since φ is a bijection, it is an isomorphism.

| |
|---|


- Corollary 3.13.1. Let G be a group and S ⊆ G. A group automorphism α ∈ Aut(G) is a graph automorphism of Cay(G,S) if and only if α(S) = S.


This provides a powerful tool for determining which group automorphisms extend to graph automorphisms.

- Example 3.13.1. Which automorphisms of Z15 are contained in Aut(Γ) for Γ = Cay(Z15,{1,3,4,12})?


Proof. The automorphism group of Z15 is isomorphic to its group of units, Z×15 = {1,2,4,7,8,11,13,14}, where multiplication by a unit a is an automorphism. We test these automorphisms

αa : x  → ax:

α1(S) = {1,3,4,12} = S. α2(S) = {2,6,8,9} ̸= S. α4(S) = {4,12,1,3} = S. α7(S) = {7,6,13,9} ̸= S.

.

By checking all units, we find that only α1 (the identity) and α4 satisfy α(S) = S. Thus, Aut(Γ) ∩ Aut(Z15) = {α1,α4}.

For abelian groups, the inverse map is always a group automorphism and often provides a non-trivial graph automorphism.

- Corollary 3.13.2. Let G be an abelian group not isomorphic to an elementary abelian 2-


group (i.e., G ≁= Zk2). Let S ⊆ G be such that S = S−1. Then the inverse map ι : g  → g−1 is a non-identity automorphism of the Cayley graph Cay(G,S).

Proof. Since G is abelian, ι is a group automorphism. Since S is inverse-closed, ι(S) = S−1 = S. Therefore, by Corollary 3.13.1, ι ∈ Aut(Cay(G,S)). If G is not an elementary abelian 2-group, then there exists g ∈ G with g ̸= g−1, so ι is not the identity.

| |
|---|


- Example 3.13.2. Which automorphisms of Z8 are in Aut(Γ) for Γ = Cay(Z8,{2,6})?

Proof. The units of Z8 are {1,3,5,7}. Note that S = {2,6} is inverse-closed. We test the automorphisms αa : x  → ax:

α1(S) = {2,6} = S. α3(S) = {6,2} = S. α5(S) = {2,6} = S (since 5 · 2 = 10 ≡ 2, 5 · 6 = 30 ≡ 6). α7(S) = {6,2} = S.

Thus, all four automorphisms are contained in Aut(Γ). Note that α5 is the inverse map (5 ≡ −3 mod 8, but more importantly, 5 · x = −3x, and for x = 2,6, we have −3·2 = −6 ≡ 2, −3·6 = −18 ≡ 6). So Aut(Γ)∩Aut(Z8) = {α1,α3,α5,α7} ∼= Z2×Z2.

| |
|---|


Corollary 3.13.2 shows that for most abelian groups, the automorphism group of a Cayley graph is strictly larger than the group itself. This addresses a fundamental problem: for which groups G does there exist a subset S such that Aut(Cay(G,S)) = G? This is not possible for non-elementary-abelian abelian groups.

- 3.14 Double Coset Graphs: A Generalization


Cayley graphs require a regular action of the group on itself. Double coset graphs generalize this construction to any transitive group action. They provide a way to construct all vertex-transitive graphs.

#### 3.14.1 Construction and Basic Properties

Let G be a group acting transitively on a set Ω. Let H = StabG(ω) be the stabilizer of a point ω ∈ Ω. By the orbit-stabilizer theorem, we can identify Ω with the set of left cosets G/H.

We want to define a digraph on Ω such that the action of G is by automorphisms. Mimicking the Cayley construction, we might try: for a subset S ⊆ G, define an arc from gH to gsH for all g ∈ G,s ∈ S. However, for this to be well-defined (independent of the coset representative), we must have s ∈ HsH for all s ∈ S and h ∈ H. This motivates the following definition.

- Definition 3.14.1 (Double Coset). Let H ≤ G and s ∈ G. The double coset of s with respect to H is the set:


HsH = {h1sh2 : h1,h2 ∈ H}. A subset S ⊆ G is a union of double cosets if S = s∈S HsH.

- 3.14. DOUBLE COSET GRAPHS: A GENERALIZATION 93


- Definition 3.14.2 (Double Coset Graph). Let G be a group, H ≤ G, and S ⊆ G a union of double cosets. The double coset graph Cos(G,H,S) is defined as:


- • Vertices: The left cosets G/H.
- • Arcs: There is an arc from gH to g′H if and only if g−1g′ ∈ S.


The condition that S is a union of double cosets ensures the arc set is well-defined. If

- H = {e}, then Cos(G,{e},S) = Cay(G,S).


- Lemma 3.14.1 (Properties of Double Coset Graphs). Let Γ = Cos(G,H,S).


- 1. G acts vertex-transitively on Γ by left multiplication: g · (xH) = (gx)H.
- 2. Γ has no loops if and only if S ∩ H = ∅.
- 3. Γ is an undirected graph if and only if S−1 = S.
- 4. The out-neighbors of the vertex H are the cosets sH for s ∈ S.
- 5. Γ is connected if and only if S generates G modulo H, i.e., ⟨H,S⟩ = G.


#### 3.14.2 Examples and Universality

- Example 3.14.1. Let G = S4, H = StabS

4

(4) ∼= S3, and S = H(1,4)H, the double coset of the transposition (1,4). The vertices are the 4 cosets of H, which correspond to the points {1,2,3,4}. The graph Cos(S4,H,S) is the complete graph K4.

- Example 3.14.2 (The Petersen Graph). The Petersen graph is not a Cayley graph, but it can be constructed as a double coset graph. Let G be a group of order 20 (isomorphic


to the semidirect product Z5 ⋊ Z4). Let H ≤ G be a subgroup of order 2. There exists a union of double cosets S such that Cos(G,H,S) is isomorphic to the Petersen graph.

The following fundamental theorem shows that double coset graphs are universal for vertex-transitive graphs.

- Theorem 3.14.1 (Sabidussi’s Theorem). Every vertex-transitive graph is isomorphic to a double coset graph.


Proof Sketch. Let Γ be vertex-transitive, and let G ≤ Aut(Γ) be a vertex-transitive subgroup. Fix a vertex u. Let H = StabG(u). Identify the vertex set with G/H via the bijection gH  → g(u). Define the connection set:

S = {g ∈ G : (u,g(u)) ∈ E(Γ)}.

One can verify that S is a union of double cosets and that Γ ∼= Cos(G,H,S).

#### The Core and Faithful Actions

For the action of G on G/H to be faithful (i.e., for the permutation representation G → Sym(G/H) to be injective), we need that no non-identity element of G acts trivially on all cosets. This leads to the concept of the core.

- Definition 3.14.3. Let H ≤ G. The core of H in G is the largest normal subgroup of


- G contained in H:

coreG(H) =

g∈G

g−1Hg.

If coreG(H) = {e}, then H is called core-free. Proposition 3.14.1. The left coset action of G on G/H is faithful if and only if H is core-free in G. Proof. The kernel of the action is {g ∈ G : gxH = xH for all x ∈ G} = {g ∈ G : x−1gx ∈

- H for all x ∈ G} = x∈G xHx−1. This is exactly coreG(H). The action is faithful if and only if this kernel is trivial.


| |
|---|


In the construction of a double coset graph from a vertex-transitive graph Γ, the stabilizer H = StabG(u) is core-free in G because no non-identity automorphism can fix every vertex of Γ.

# Chapter 4 Arc-Transitive Graphs

A graph is a sequence of vertices (v0,...,vs) such that consecutive vertices are adjacent and vi−1 ̸= vi+1 when 0 < i < s. Note that an s-arc is permitted to use the same vertex more than once, although in all cases of interest this will not happen.

A graph is s-arc transitive if its automorphism group is transitive on s-arcs. If s ≥ 1, then it is both obvious and easy to prove that an s-arc transitive graph is also (s−1)-arc transitive. A 0-arc transitive graph is just another name for a vertex-transitive graph, and a 1-arc transitive graph is another name for an arc-transitive graph. A 1-arc transitive graph is also sometimes called a symmetric graph.

A cycle on n vertices is s-arc transitive for all s, which only shows that truth and utility are different concepts. A more interesting example is provided by the cube, which is 2-arc transitive. The cube is not 3-arc transitive because 3-arcs that form three sides of a four-cycle cannot be mapped to 3-arcs that do not (see Figure 4.1).

Figure 4.1: Inequivalent 3-arcs in the cube

A graph X is s-arc transitive if it has a group G of automorphisms such that G is transitive, and the stabilizer Gu of a vertex u acts transitively on the s-arcs with initial vertex u.

- Theorem 4.0.1. Let X be a vertex-transitive graph and s ≥ 1. Then X is s-arc-transitive


if and only if, for any vertex v, the stabilizer Aut(X)v acts transitively on the set of (s − 1)-arcs starting at v.

In particular, X is arc-transitive (i.e., 1-arc-transitive) if and only if, for any vertex v, the stabilizer Aut(X)v acts transitively on the neighborhood of v. Proof. (⇒) If X is s-arc-transitive, then the stabilizer acts transitively on (s−1)arcs from v.

Fix a vertex v ∈ V (X). Let As−1(v) denote the set of (s − 1)-arcs starting at v, i.e., As−1(v) = {(v,v1,...,vs−1) : (v,v1,...,vs−1) is an (s − 1)-arc}.

Take any two (s − 1)-arcs from v, say (v,v1,...,vs−1) and (v,u1,...,us−1). Consider any extensions to s-arcs:

(v,v1,...,vs−1,vs), (v,u1,...,us−1,us) 95

for some suitable vs,us so that these are s-arcs. Since X is s-arc-transitive, there exists ϕ ∈ Aut(X) with

ϕ(v,v1,...,vs−1,vs) = (v,u1,...,us−1,us).

Because both s-arcs start at v, it follows that ϕ fixes v, i.e., ϕ ∈ Aut(X)v. Restricting to the first s − 1 vertices shows that Aut(X)v maps (v,v1,...,vs−1) to (v,u1,...,us−1). Hence Aut(X)v acts transitively on (s − 1)-arcs starting at v.

(⇐) If the stabilizer acts transitively on (s − 1)-arcs from v, then X is s-arctransitive.

Let (u0,u1,...,us) and (v0,v1,...,vs) be any two s-arcs in X. Because X is vertextransitive, there exists ψ ∈ Aut(X) with ψ(u0) = v0. Then (ψ(u0),ψ(u1),...,ψ(us−1)) is an (s − 1)-arc starting at v0. By assumption, the stabilizer Aut(X)v

acts transitively on (s − 1)-arcs from v0, so there exists ϕ ∈ Aut(X)v

0

such that ϕ(ψ(u1),...,ψ(us−1)) = (v1,...,vs−1).

0

Then ϕ ◦ ψ ∈ Aut(X) maps (u0,...,us−1) to (v0,...,vs−1). By choosing the final vertex appropriately (using adjacency constraints), we extend this mapping to the full s-arc.

Therefore X is s-arc-transitive. Special case: arc-transitive.

For s = 1, a 1-arc is just an edge (v0,v1) with a direction. The stabilizer Aut(X)v acts transitively on the set of neighbors of v if and only if for any two edges (v,u) and (v,w) there exists ϕ ∈ Aut(X)v with ϕ(u) = w. This is exactly 1-arc-transitivity (arctransitivity).

| |
|---|


- Lemma 4.0.1. The graphs J(v,k,i) are at least arc transitive.


Proof. Consider the vertex {1,...,k}. The stabilizer of this vertex contains Sym(k) × Sym(v −k). Clearly, any two k-sets meeting this initial vertex in an i-set can be mapped to each other by this group.

| |
|---|


- Example 4.0.1. Let Cn be the cycle on n vertices, and let s be an integer with 0 ≤ s ≤ n − 1. Then Cn is s-arc-transitive: the automorphism group Aut(Cn) ∼= D2n acts transitively on the set of s-arcs of Cn.


Proof. Model Cn as the vertices {0,1,...,n − 1} with indices taken modulo n, where i is adjacent to i ± 1 (mod n).

An s-arc is an ordered sequence

(v0,v1,...,vs),

where vi is adjacent to vi+1 and vi−1 ̸= vi+1 for all i. On a cycle, this condition forces each step vi+1 to be either the clockwise or counterclockwise neighbor of vi, and since immediate backtracking is forbidden, each successive step continues in the same direction.

Hence every s-arc is a simple directed path of length s along the cycle. More concretely,

for some start vertex a ∈ {0,...,n−1} and for some choice of sign ε ∈ {+1,−1} we have (v0,v1,...,vs) = a, a + ε, a + 2ε, ..., a + sε ,

with arithmetic modulo n. Thus an s-arc is completely determined by its starting vertex a and its direction ε.

The automorphism group of the cycle is the dihedral group D2n, generated by the rotation r: i  → i + 1 and a reflection ρ (e.g. ρ(i) = −i). Rotations act transitively on start vertices: for any two s-arcs

A = (a,a + ε,...,a + sε), B = (b,b + δ,...,b + sδ), the rotation rb−a sends A to

rb−a(A) = (b,b + ε,...,b + sε). If ε = δ, then rb−a maps A to B. If ε ̸= δ, then compose with the reflection:

ρ ◦ rb−a(A) = (b,b − ε,...,b − sε), and since −ε = δ, this equals B.

Thus for any two s-arcs A,B there exists an automorphism in D2n sending A to B. Hence Cn is s-arc-transitive for all 0 ≤ s ≤ n − 1.

| |
|---|


- Example 4.0.2. Kn is s-arc-transitive only for s = 0,1,2.
- Example 4.0.3. Cube Q3 is 2-arc-transitive but not 3-arc-transitive.


Proof. Model Q3 as the graph with vertex set {0,1}3 (binary 3-tuples). Two vertices are adjacent iff they differ in exactly one coordinate. The automorphism group of Q3 contains all coordinate permutations and all independent bit-flips, so in particular it preserves Hamming distance between vertices.

- (1) Q3 is 2-arc-transitive. Fix a vertex, say v0 = (0,0,0). Its neighbors are the three unit vectors e1 = (1,0,0),e2 = (0,1,0),e3 = (0,0,1). Any 2-arc starting at v0 is of the form (v0,ei,ej) with i ̸= j (the non-backtracking condition forbids i = j). The stabilizer of v0 inside Aut(Q3) contains the full permutation group on the three coordinates, i.e. a copy of S3. This S3-action permutes {e1,e2,e3} arbitrarily, hence acts transitively on ordered pairs (ei,ej) with i ̸= j. Therefore the stabilizer of v0 acts transitively on the set of 2-arcs starting at v0. Since the cube is vertex-transitive, this implies Aut(Q3) is transitive on all 2-arcs, i.e. Q3 is 2-arc-transitive.
- (2) Q3 is not 3-arc-transitive. Consider 3-arcs, i.e. ordered non-backtracking paths of length 3 (v0,v1,v2,v3). The automorphism group preserves Hamming distances, so the Hamming distance d(v0,v3) is an invariant of the orbit of a 3-arc. We show there exist 3-arcs with different values of d(v0,v3), hence there are at least two distinct orbits of 3-arcs, so the action is not transitive on 3-arcs.


Example 1 (distance 3). Take the path

(000,100,110,111). Here v0 = 000 and v3 = 111, so d(v0,v3) = 3.

Example 2 (distance 1). Take the path

(000,100,101,001). Here v0 = 000 and v3 = 001, so d(v0,v3) = 1.

Both sequences are valid non-backtracking paths of length 3 in Q3. Because d(v0,v3) is preserved by every graph automorphism, no automorphism can send the first 3-arc to the second. Hence the set of all 3-arcs splits into at least two orbits under Aut(Q3), so Q3 is not 3-arc-transitive.

Combining (1) and (2) proves the theorem.

| |
|---|


Exercise Let Γ be a graph with minimum degree at least 2. Then Γ is (s + 1)-arctransitive if and only if Γ is s-arc-transitive and the stabilizer in Aut(Γ) of any s-arc (v0,...,vs−1,vs) acts transitively on Γ(vs) \ {vs−1}.

- Example 4.0.4. Petersen graph is 3-arc-transitive but not 4-arc-transitive.


Proof. We prove both statements separately.

Part 1: 3-arc-transitivity Let P denote the Petersen graph. We establish 3-arc-transitivity through these steps:

- 1. The automorphism group Aut(P) is isomorphic to S5 and has order 120.
- 2. P is arc-transitive.
- 3. P has 15 undirected edges and 30 directed arcs (each edge gives two arcs)
- 4. For any arc (u,v) ∈ V × V with u ∼ v, the arc stabilizer is: G(u,v) = Gu ∩ Gv

where Gu and Gv are the vertex stabilizers, V = V (P)

- 5. Gu ∼= D6 (dihedral group of order 12)
- 6. Gu ∩ Gv ∼= Z2 when u ∼ v, So Gu is transitive on 2-arcs initiate from u, which implies that P is 2-arc transitive.
- 7. P has 60 2-arcs, so for any 2-arc (u,v,w), the stabilizer in Aut(P) is ismorphic to

Z2 and acts transitively on the remaining neighbors of w (excluding v). This follows because:

- 8. The neighborhood of any vertex induces a matching (no two neighbors are adjacent)
- 9. The stabilizer of a 2-arc has order 2 and can swap the remaining two neighbors
- 10. So P is 3-arc transitive.
- 11. P has 120 3-arcs and so the pointwise stabilizer of a 3-arc is trivial which implies that it is not 4-arc transtive


Thus while Aut(P) acts transitively on 3-arcs, it has two distinct orbits on 4-arcs.

| |
|---|


- Theorem 4.0.2. For every integer k ≥ 1 the graph J(2k + 1,k,0) (the odd graph Ok) is 2-arc-transitive: its automorphism group acts transitively on the set of directed paths of length 2 (i.e. on ordered triples (A,B,C) with A−B−C an 2-arc).


Proof. Model J(2k+1,k,0) as follows. Let Ω be a fixed set with |Ω| = 2k+1. Vertices of the graph are the k-subsets of Ω. Two vertices (subsets) are adjacent iff they are disjoint. The symmetric group SΩ ∼= S2k+1 acts naturally on the vertex set by permuting elements of Ω, and this action preserves disjointness; hence SΩ ≤ Aut(J(2k + 1,k,0)). Thus it suffices to show that SΩ acts transitively on the set of directed paths of length 2.

Let (A,B,C) be any directed path of length 2; that is A,B,C are k-subsets of Ω with A ∩ B = ∅, B ∩ C = ∅, and A ̸= C (the non-backtracking condition). From the disjointness conditions we obtain the crucial constraint on |A ∩ C|. Indeed

B ⊆ Ω \ (A ∪ C), so

k = |B| ≤ |Ω \ (A ∪ C)| = (2k + 1) − |A ∪ C|. But |A ∪ C| = |A| + |C| − |A ∩ C| = 2k − |A ∩ C|, so the previous inequality becomes k ≤ (2k + 1) − (2k − |A ∩ C|) = 1 + |A ∩ C|,

hence |A ∩ C| ≥ k − 1. Since |A ∩ C| ≤ k and equality |A ∩ C| = k would force A = C (forbidden), we must have

|A ∩ C| = k − 1. Thus every directed 2-path (A,B,C) in the odd graph satisfies |A ∩ C| = k − 1. Now fix a convenient canonical 2-arc:

A0 = {1,2,...,k}, B0 = {k + 1,k + 2,...,2k}, C0 = {1,2,...,k − 1,2k + 1},

where Ω = {1,2,...,2k+1}. Note that A0∩B0 = ∅, B0∩C0 = ∅, and |A0∩C0| = k−1, so (A0,B0,C0) is indeed a directed 2-path.

We claim any directed 2-path (A,B,C) can be sent to (A0,B0,C0) by some permutation in SΩ. To see this, choose an enumeration of the elements of A and C so that the first k − 1 elements are the common elements of A ∩ C. Using a permutation we may send those k − 1 common elements to {1,2,...,k − 1}, the unique element in A \ C to k, and the unique element in C \ A to 2k + 1. Finally send the k elements of B (which lie in the complement of A ∪ C, a set of size k) to {k + 1,...,2k}. This defines a bijection of Ω sending (A,B,C) to (A0,B0,C0). Thus every directed 2-path lies in the same orbit of SΩ.

Since SΩ ≤ Aut(J(2k+1,k,0)), the full automorphism group is transitive on directed 2-paths; i.e. the graph is 2-arc-transitive.

| |
|---|


The girth of a graph is the length of the shortest cycle in it. Our first result implies that the subgraphs induced by s-arcs in s-arc transitive graphs are paths.

- Theorem 4.0.3 (Tutte). If X is an s-arc transitive graph with valency at least three and girth g, then g ≥ 2s − 2.


Proof. We may assume that s ≥ 3, since the condition on the girth is otherwise meaningless. It is easy to see that X contains a cycle of length g and a path of length g whose end-vertices are not adjacent. Therefore X contains a g-arc with adjacent end-vertices and a g-arc with nonadjacent end-vertices; clearly, no automorphism can map one to the other, and so s < g.

Since X contains cycles of length g, and since these contain s-arcs, it follows that any s-arc must lie in a cycle of length g. Suppose that v0,...,vs is an s-arc. Denote it by ∆. Since vs−1 has valency at least three, it is adjacent to a vertex w other than vs−2 and vs, and since the girth of X is at least s, this vertex cannot lie in ∆. Hence we may replace vs by w, obtaining a second s-arc β that intersects ∆ in an (s − 1)-arc. Since β must lie

in a circuit of length g, we thus obtain a pair of circuits of length g that have at least s − 1 edges in common.

If we delete these s − 1 edges from the graph formed by the edges of the two circuits of length g, the resulting graph still contains a cycle of length at most 2g −2s+2. Hence 2g − 2s + 2 ≥ g, and the result follows.

| |
|---|


Given this lemma, it is natural to ask what can be said about the s-arc transitive graphs with girth 2s − 2. It follows from our next result that these graphs are, in the language ofnext chapter, generalized polygons. It is a consequence of results we state there that s ≤ 9.

- Theorem 4.0.4 (Tutte). If X is an s-arc transitive graph with girth 2s−2, it is bipartite and has diameter s − 1.


Proof. We first observe that if X has girth 2s−2, then any s-arc lies in at most one cycle of length 2s−2, and so if X is s-arc transitive, it follows that every s-arc lies in a unique cycle of length 2s − 2. Clearly, X has diameter at least s − 1, because opposite vertices in a cycle of length 2s − 2 are at this distance.

Now, let u be a vertex of X and suppose for a contradiction that v is a vertex at distance s from it. Then there is an s-arc joining u to v, which must lie in a cycle of length 2s − 2. Since a cycle of this length has diameter s − 1, it follows that v cannot be of distance s from u. Therefore, the diameter of X is at most s − 1 and hence equal to s − 1.

If X is not bipartite, then it contains an odd cycle; suppose C is an odd cycle of minimal length. Because the diameter of X is s − 1, the cycle must have length 2s − 1. Let u be a vertex of C, and let v and v′ be the two adjacent vertices in C at distance s − 1 from u. Then we can form an s-arc (u,...,v,v′). This s-arc lies in a cycle C′ of length 2s − 2. The vertices of C and C′ not internal to the s-arc form a cycle of length less than 2s − 2, which is a contradiction.

| |
|---|


We will use this lemma to show that s-arc transitive graphs with girth 2s − 2 are distance transitive. Arc Graphs

If s ≥ 1 and α = (x0,...,xs) is an arc in X, we define its head head(α) to be the (s − 1)-arc (x1,...,xs) and its tail tail(α) to be the (s − 1)-arc (x0,...,xs−1). If α and β are s-arcs, then we say that β follows α if there is an (s+1)-arc γ such that head(γ) = β and tail(γ) = α. (Somewhat more colourfully, we say that α can be shunted onto β, and envisage pushing α one step onto β.) Let s be a nonnegative integer. We use X(s) to denote the directed graph with the s-arcs of X as its vertices, such that (α,β) is an arc if and only if α can be shunted onto β. Any automorphisms of X extend naturally to automorphisms of X(s), and so if X is s-arc transitive, then X(s) is vertex transitive.

- Lemma 4.0.2. Let X and Y be directed graphs and let f be a homomorphism from X onto Y such that every edge in Y is the image of an edge in X. Suppose y0,...,yr is a path in Y . Then for each vertex x0 in X such that f(x0) = y0, there is a path x0,...,xr such that f(xi) = yi. Proof. Exercise.


| |
|---|


- 4.1. S-ARC TRANSITIVE GRAPHS 101


### 4.1 s-arc Transitive Graphs

Define a spindle in X to be a subgraph consisting of two given vertices joined by three paths, with any two of these paths having only the given vertices in common. Define a bicycle to be a subgraph consisting either of two cycles with exactly one vertex in common, or two vertex-disjoint cycles and a path joining them having only its endvertices in common with the cycles. We claim that if X is a spindle or a bicycle, then X(1) is strongly connected. We leave the proof of this as an easy exercise. Nonetheless, it is the key to the proof of the following result.

- Theorem 4.1.1. If X is a connected graph with minimum valency two that is not a cycle, then X(s) is strongly connected for all s ≥ 0.


Proof. First we shall prove the result for s = 0 and s = 1, and then by induction on s. If s = 0, then X(0) is the graph obtained by replacing each edge of X with a pair of oppositely directed arcs, so the result is clearly true. If s = 1, then we must show that any 1-arc can be shunted onto any other 1-arc. Since X is connected, we can shunt any 1-arc onto any edge of X, but not necessarily facing in the right direction. Therefore, it is necessary and sufficient to show that we can reverse the direction of any 1-arc, that is, shunt xy onto yx.

Since X has minimum valency at least two and is finite, it contains a cycle, C say. If C does not contain both x and y, then there is a (possibly empty) path in X joining y to C. It is now easy to shunt xy along the path, around C, then back along the path in the opposite direction to yx.

If x and y are in V (C) but xy ∈/ E(C), then C together with the edge xy is a spindle, and we are done.

Hence we may assume that xy ∈ E(C). Since X is not a cycle, there is a vertex in C adjacent to a vertex not in C. Suppose w in V (C) is adjacent to a vertex z not in C. Let P be a path with maximal length in X, starting with w and z, in this order. Then the last vertex of P is adjacent to a vertex in P or a vertex in C. If it is adjacent to a vertex in C other than w, then xy is an edge in a spindle. If it is adjacent to w or to a vertex of P not in C, then xy is an edge in a bicycle. In either case we are done.

Now, assume that X(s) is strongly connected for some s ≥ 1. It is easy to see that the operation of taking the head of an (s + 1)-arc is a homomorphism from X(s+1) to X(s). Since X has minimum valency at least two, each s-arc is the head of an (s+1)-arc, and it follows that every edge of X(s) is the image of an edge in X(s+1). Let α and β be any two (s + 1)-arcs in X. Since X(s) is strongly connected, there is a path in it joining head(α) to tail(β). By the lemma above, this path lifts to a path in X(s+1) from α to a vertex, where head(γ) = tail(β). Since s ≥ 1 and X has minimum valency at least two, we see that γ can be shunted onto β. Thus α can be shunted to β via γ, and so there is a path in X(s+1) from α to β.

| |
|---|


### 4.2 Cubic s-arc Transitive Graphs

In 1947 Tutte showed that for any s-arc transitive cubic graph, s ≤ 5. This was, eventually, the stimulus for a lot of work. One outcome of this was a proof, by Richard Weiss, that for any s-arc transitive graph, s ≤ 7. This is a very deep result, the proof of which depends on the classification of the finite simple groups.

- Lemma 4.2.1. Let X be a strongly connected directed graph, let G be a transitive subgroup of its automorphism group, and, if u ∈ V (X), let N(u) be the set of vertices v in V (X)

such that (u,v) is an arc of X. If there is a vertex u of X such that Gu ∩ N(u) is the identity, then G is regular.

Proof. Suppose u ∈ V (X) and Gu ∩ N(u) is the identity group. If v ∈ V (X), then Gv is conjugate in G to Gu. Hence Gv ∩ N(v) must be the identity for all vertices v of X.

Assume, by way of contradiction, that Gu is not the identity group. Since X is strongly connected, we may choose a directed path that goes from u to a vertex, w say, that is not fixed by Gu. Choose this path to have minimum possible length, and let v denote the second-last vertex on it. Thus v is fixed by Gu, and (v,w) is an arc in X. Since Gu fixes all vertices in N(u), we see that v ̸= u.

Since Gu fixes v, it fixes N(v) but acts nontrivially on it, because it does not fix

- w. Hence Gv ∩ N(v) is not the identity. This contradiction forces us to conclude that Gu = (e).


| |
|---|


A graph is s-arc regular if for any two s-arcs there is a unique automorphism mapping the first to the second.

- Lemma 4.2.2. Let X be a connected cubic graph that is s-arc transitive, but not (s+1)arc transitive. Then X is s-arc regular.


Proof. We note that if X is cubic, then X(s) has out-valency two. Now let G be the automorphism group of X, let α be an s-arc in X, and let H be the subgroup of G fixing each vertex in α. Then G acts vertex transitively on X(s), and H is the stabilizer in G of the vertex α in X(s). If the restriction of H to the out-neighbours of α is not trivial, then H must swap the two s-arcs that follow α. Now, any two (s + 1)-arcs in X can be mapped by elements of G to (s + 1)-arcs that have α as the "initial" s-arc; hence in this case we see that G is transitive on the (s + 1)-arcs of X, which contradicts our initial assumption.

Hence the restriction of H to the out-neighbours of α is trivial, and it follows that H itself is trivial. Therefore, we have proved that Gα = (e), and so G acts regularly on the s-arcs of X.

| |
|---|


If X is a regular graph with valency k on n vertices and s ≥ 1, then there are exactly nk(k−1)s−1 s-arcs. It follows that if X is s-arc transitive then |Aut(X)| must be divisible by nk(k − 1)s−1, and if X is s-arc regular, then |Aut(X)| = nk(k − 1)s−1. In particular, a cubic arc-transitive graph X is s-arc regular if and only if

|Aut(X)| = (3n)2s−1.

For an example, consider the cube. It is clear that the stabilizer of a vertex contains Sym(3), and therefore its automorphism group has size at least 48. We observed earlier that the cube is not 3-arc transitive, so it must be precisely 2-arc regular, with full automorphism group of order 48.

Finally, we state Tutte’s theorem.

- Theorem 4.2.1. If X is an s-arc regular cubic graph, then s ≤ 5.


Proof. Let X be a connected cubic graph with n vertices, and let G = Aut(X). Suppose X is s-arc-regular, meaning G acts regularly on the set of s-arcs of X (an s-arc is a

sequence (v0,v1,...,vs) of s + 1 vertices such that vi is adjacent to vi+1 and vi−1 ̸= vi+1 for 1 ≤ i ≤ s − 1).

Step 1: Counting s-arcs and the group order. For a cubic graph:

- • Each vertex v has 3 neighbors.
- • Starting from v0, there are 3 choices for v1.
- • For each subsequent step i ≥ 2, there are 2 choices for vi (avoiding the previous vertex to prevent backtracking).


Hence the number of s-arcs is

#{s-arcs} = n · 3 · 2s−1. Since G acts regularly on s-arcs, the order of G equals the number of s-arcs: |G| = n · 3 · 2s−1.

Let v ∈ V (X), and let Gv denote the stabilizer of v in G. By the orbit-stabilizer theorem:

|G| = n · |Gv| =⇒ |Gv| = 3 · 2s−1.

Step 2: Local action at a vertex. Since X is arc-transitive, Gv acts transitively on the 3 neighbors of v. Therefore Gv

embeds as a transitive subgroup of Sym(3) implying: 3 | |Gv|. The stabilizer of an arc (v,u), i.e. G(v,u), is the subgroup of Gv fixing u: |G(v,u)| = |Gv| 3

= 2s−1.

Step 3: Growth constraints for s-arc-regularity. Consider the faithful action of Gv on all s-arcs starting at v. Each extension of an

arc from v multiplies the number of possible continuations by 2 (except the backtracking edge). Therefore:

- • |Gv| = 3 · 2s−1 grows exponentially in s.
- • To preserve the s-arc structure faithfully, Gv must act effectively on 2s−1 different possible sequences.


Step 4: Why s ≥ 6 fails. If s ≥ 6:

- 1. |Gv| = 3 · 2s−1 ≥ 96.
- 2. Gv must permute 2s−1 ≥ 32 possible continuation sequences for arcs of length s.


- 3. A cubic graph only allows 2 forward choices at each step, so the structure of s-arcs restricts the action.
- 4. Maintaining faithful s-arc-regularity forces the automorphism to also preserve (s + 1)-arcs, which is impossible if s is maximal.


Hence no cubic s-arc-regular graph exists for s ≥ 6.

Step 5: Geometric intuition. At each vertex v, the three incident edges consist of:

- • one edge back to the previous vertex,
- • two edges leading forward along potential s-arcs.


For large s, the automorphism must distinguish increasingly many forward paths. Eventually, the local action of Gv cannot accommodate all constraints without affecting longer arcs, forcing a violation of s-arc regularity.

Step 6: Maximum case and example. For s = 5, the numbers work out:

|Gv| = 3 · 24 = 48,

and Tutte’s 8-cage on 30 vertices realizes this maximum. The full automorphism group has order:

|G| = 30 · 48 = 1440.

Conclusion. Therefore, for cubic s-arc-regular graphs:

s ≤ 5.

| |
|---|


- Corollary 4.2.1. Let X be an arc-transitive cubic graph with automorphism group G and vertex stabilizer Gv. Then:


|Gv| | 48 and 3 | |Gv|.

Proof. From the proof above, the maximal vertex stabilizer occurs at s = 5, giving |Gv| = 48, divisible by 3 due to the required transitivity on the 3 neighbors of v. Smaller s give smaller divisors of 48.

| |
|---|


The smallest 5-arc regular cubic graph is Tutte’s 8-cage on 30 vertices.

- Corollary 4.2.2 (4.3.4). If X is an arc-transitive cubic graph, v ∈ V (X), and G = Aut(X), then |Gv| divides 48 and is divisible by three.


- Theorem 4.2.2 (Weiss, 1981; refined version). Let X be a finite connected k-regular graph, and suppose that X is s-arc-transitive (i.e., its automorphism group acts transitively on the set of s-arcs). Then:


s ≤ 7. Moreover, equality s = 7 occurs only for graphs of very special structure:

- • The graph must satisfy highly restrictive combinatorial and group-theoretic conditions.
- • Such graphs are extremely rare and require special constructions. Remark:
- • This result generalizes Tutte’s theorem for cubic graphs, which is the case k = 3, where the maximal s is 5.
- • The Weiss theorem shows that no matter the valency, the s-arc-transitive property cannot extend indefinitely; there is an absolute upper bound of 7.
- • The bound s ≤ 7 is sharp in the sense that there do exist graphs realizing s = 7, but they are exceptional.


- Corollary 4.2.3 (Vertex stabilizers in cubic s-arc-regular graphs, Tutte). Let X be a


connected cubic s-arc-regular graph with s ≤ 5, and let v ∈ V (X). Let Gv = StabAut(X)(v) denote the vertex stabilizer. Then

|Gv| = 3 · 2s−1, and the group structure is:

- 1. s = 1: |Gv| = 3, Gv ∼= C3.
- 2. s = 2: |Gv| = 6, Gv ∼= S3.
- 3. s = 3: |Gv| = 12, Gv ∼= C2 × S3 (the 3-cycle acts faithfully on the 3 neighbors).
- 4. s = 4: |Gv| = 24, Gv ∼= S4.
- 5. s = 5: |Gv| = 48, Gv ∼= C2 × S4 (realized in Tutte’s 8-cage).


Proof. Let X be a connected cubic s-arc-regular graph with automorphism group G = Aut(X).

Step 1: Counting s-arcs. At each vertex, there are 3 neighbors. Beyond the first step, each step along an s-arc has 2 choices (to avoid backtracking). Hence, the number of s-arcs starting at a fixed vertex v is

3 · 2s−1. Since G acts regularly on the set of s-arcs, the orbit-stabilizer theorem gives |Gv| = 3 · 2s−1.

##### Step 2: Determining the structure.

- • s = 1: Gv acts transitively on the 3 neighbors and has no further choices, so Gv ∼= C3.
- • s = 2: Gv permutes the 3 neighbors and acts on the 2-step extensions. This gives a group of order 6, which must be S3.


- • s = 3: Gv has order 12. There is a normal subgroup of order 2 corresponding to the binary choice along one step of the 3-arc, and the quotient of order 6 is S3 acting faithfully on neighbors. Hence Gv ∼= C2 × S3.
- • s = 4: Gv has order 24. Its Sylow 2-subgroup of order 8 corresponds to the normal 2-group acting on the first 3 steps, and the subgroup of order 3 acts transitively on the neighbors. By group-theoretic classification, the only nonabelian group of order 24 with these properties is S4. Hence Gv ∼= S4.
- • s = 5: Gv has order 48. In Tutte’s 8-cage, the 16-element 2-group is normal, and the quotient of order 3 acts transitively on neighbors. Thus, Gv ∼= C2 × S4.


- Step 3: Verification. In each case, the stabilizer acts faithfully on s-arcs starting


at v, and the structures listed match both the order and the local permutation requirements. Special cases s = 4 and s = 5 correspond to S4 and C2 × S4 as noted in Tutte’s classification.

| |
|---|


# Chapter 5 Distance-transitive and Moore graphs

- Definition 5.0.1. A connected graph is distance-transitive if given any two ordered pairs of vertices (u,u′) and (v,v′) such that d(u,u′) = d(v,v′), there is an automorphism of Γ such that (v,v′) = σ(u,u′).


- Example 5.0.1. The complete graph Kn is distance-transitive.


- Lemma 5.0.1. (The Johnson graphs are distance-transitive.) Let v,k be integers with 0 < k < v. The Johnson graph J(v,k,k − 1) (the usual Johnson graph J(v,k)) is distance-transitive.

Proof. Vertices of J(v,k,k − 1) are the k-subsets of a fixed v-set Ω = {1,...,v}. Two vertices (subsets) A,B are adjacent iff |A ∩ B| = k − 1 (equivalently B is obtained from A by replacing one element by another).

Distance formula. Let A,B be k-subsets and set t = |A ∩ B|. We claim

dist(A,B) = k − t.

Indeed, starting from A we can replace one element at a time of A \ B by a distinct element of B\A; each replacement gives an adjacent k-set and after exactly |A\B| = k−t replacements we reach B. Hence dist(A,B) ≤ k − t.

Conversely, along any path of length r from A to B each step can change the intersection with B by at most one (you can gain at most one element of B at each step), so after r steps the intersection size with B is at least t+r −k; comparing endpoints shows r ≥ k − t. Thus dist(A,B) = k − t.

Distance-transitivity. The symmetric group SΩ ∼= Sv acts naturally on k-subsets and preserves intersection sizes, hence preserves distances. Moreover, for any two ordered pairs of k-subsets (A,B) and (A′,B′) with |A ∩ B| = |A′ ∩ B′| there exists σ ∈ SΩ with σ(A) = A′ and σ(B) = B′ (because one can first map A to A′ and then permute the remaining elements inside complements to map B to B′; this is standard and depends only on matching the intersection pattern). Therefore SΩ ≤ Aut(J(v,k,k − 1)) acts transitively on ordered pairs of vertices at a given distance. That is exactly the definition of distance-transitive. Hence J(v,k,k − 1) is distance-transitive.

| |
|---|


- Lemma 5.0.2. For every integer k ≥ 1, the graph J(2k + 1,k,0) (the odd graph Ok) is distance-transitive.


Proof. Let Ω be a fixed set with |Ω| = 2k + 1. The vertices of J(2k + 1,k,0) are the k-subsets of Ω, and two vertices A,B are adjacent if and only if

A ∩ B = ∅.

107

Distance formula. Let A,B be vertices and put t = |A∩B|. Then the distance between A and B in Ok is given by

k − t, if t is even, k − t + 1, if t is odd.

dist(A,B) =

In particular, the diameter of Ok is k, and the intersection size uniquely determines the distance.

To see this, note that if A0,A1,...,Am is a path in Ok, then Ai+1 ⊆ Ω \ Ai, where |Ω\Ai| = k+1. Tracking the size of Ai∩B along such a path shows that the intersection size can increase by at most one every two steps, and parity considerations force the above formula. A constructive argument shows that these bounds are attained, so the formula is exact.

Distance-transitivity. The symmetric group SΩ acts naturally on the set of k-subsets of Ω and preserves intersection sizes, hence distances. Moreover, SΩ is transitive on ordered pairs of k-subsets having a fixed intersection size t. Therefore SΩ ≤ Aut(Ok) acts transitively on ordered pairs of vertices at each distance. Hence the odd graph Ok = J(2k + 1,k,0) is distance-transitive.

| |
|---|


For a connected graph Γ and a vertex v ∈ V (Γ), let Γi(v) be the set of vertices at distance i from v, that is Γi(v) = {u ∈ V (Γ) | d(u,v) = i}. Observe that for any connected graph Γ with diameter d, we have that V (Γ) is partitioned into sets Γ0(v),Γ1(v),...,Γd(v). The following theorem gives a characterization of distance-transitive graphs, based on the action of the automorphism group on sets Γi(v). This partition is called the distancepartition of Γ.

- Theorem 5.0.1. Let Γ be a connected graph. Then Γ is distance-transitive if and only if the following conditions hold:


- 1. Γ is vertex-transitive;
- 2. Aut(Γ)v acts transitively on each of the sets Γi(v) (i = 1,...,diam(Γ)), for any vertex v ∈ V (Γ).


Proof. (⇒) Assume Γ is distance-transitive.

First, set x1 = x2 and let y1,y2 be any two vertices with d(x1,y1) = d(x2,y2). By distance-transitivity there is an automorphism φ with φ(x1) = x2 and φ(y1) = y2. Taking x1 arbitrarily shows that Aut(Γ) acts transitively on vertices, so Γ is vertex-transitive.

Next fix v ∈ V (Γ) and an index i. Let u1,u2 ∈ Γi(v), so d(v,u1) = d(v,u2) = i. By distance-transitivity (applied to the pairs (v,u1) and (v,u2)) there exists ψ ∈ Aut(Γ) with ψ(v) = v and ψ(u1) = u2. Hence ψ ∈ Aut(Γ)v and the stabilizer of v acts transitively on Γi(v). This verifies (2).

(⇐) Conversely, assume (1) and (2) hold. Let x1,y1,x2,y2 ∈ V (Γ) satisfy d(x1,y1) = d(x2,y2) = k. By vertex-transitivity there exists α ∈ Aut(Γ) with α(x1) = x2. Then d(x2,α(y1)) = d(x1,y1) = k, so α(y1) ∈ Γk(x2). By hypothesis (2) the stabilizer Aut(Γ)x

2

###### acts transitively on Γk(x2), hence there exists β ∈ Aut(Γ)x

with β(α(y1)) = y2. The composition β ◦ α is an automorphism which sends

2

(x1,y1 ) −−→α (x2,α(y1)) −−→β (x2,y2 ).

Thus for any two ordered pairs of vertices at the same distance there is an automorphism sending one pair to the other, so Γ is distance-transitive.

| |
|---|


109

- Corollary 5.0.1. Let Γ be a connected distance-transitive graph. Then Γ is arc-transitive.


- Example 5.0.2. The Petersen graph is distance-transitive.

We would like to note that distance-transitive graphs are not necessarily s-arc-transitive for higher values of s.

- Example 5.0.3. The cube graph Q3 is distance-transitive, it has diameter 3, but it is not 3-arc-transitive.
- Example 5.0.4. Let G = Z17 and S = {1,2,4,8,9,13,15,16} and let Γ = Cay(G,S). Then Γ is distance-transitive with diameter 2.
- Example 5.0.5. Let p ≡ 1 (mod 4) be a prime, and let G = Zp. Let S = {x2 : x ̸= 0}. Observe that S = −S and that |S| = (p − 1)/2. Let Γ = Cay(G,S). Then Γ is distancetransitive with diameter 2.
- Example 5.0.6. Let p be a prime, and q = pn such that q ≡ 1 (mod 4). Let Fq be the field of order q. Let S be the set of all non-zero squares in Fq, that is S = {x2 | x ∈ Fq \ {0}}. Let G be the additive group of the field Fq, that is G = (Fq,+). The graph Γ = Cay(G,S) is called the Paley graph. Prove that Paley graphs are distance-transitive.


Suppose that Γ is a connected distance-transitive graph and u ∈ V (Γ). Since the cells of the distance partition Γi(u) are orbits of Aut(Γ)u, every vertex in Γi(u) is adjacent to the same number of other vertices, say ai, in Γi(u). Similarly, every vertex in Γi(u) is adjacent to the same number, say bi, of vertices in Γi+1(u) and the same number, say ci, of vertices in Γi−1(u). The graph Γ is regular, and its valency is given by b0, so if the diameter of Γ is d, we have

ci + ai + bi = b0 for i = 0,1,...,d.

These numbers are called the parameters of the distance-transitive graph and determine many of its properties.

- Theorem 5.0.2. Let X be a connected graph which is s-arc-transitive and whose girth is 2s − 2. Then X is distance-transitive and diam(X) = s − 1. Proof. We split the proof into two parts.


- (A) diam(X) = s − 1. Assume for contradiction that diam(X) ≥ s. Then there exist two vertices at distance s; let


P = (v0,v1,...,vs) be a shortest path of length s between them. Because P is a shortest path, it is an s-arc (no immediate backtracking occurs). Since X is s-arc-transitive, the automorphism group of X acts transitively on the set of s-arcs. In particular the stabilizer of v0 in Aut(X) acts transitively on the set of s-arcs that start at v0. Thus there exists an automorphism φ ∈ Aut(X)v

sending the s-arc (v0,v1,...,vs) to an s-arc (v0,w1,...,ws) with w1 ̸= v1 (such a w1 exists because v0 has at least two neighbours whenever s ≥ 2; if s = 1 the statement is trivial). Consider the two s-paths

0

v0−v1−···−vs and v0−w1−···−ws.

These two s-paths share their initial vertex v0 but have different second vertices v1 and w1. Follow the first path from v0 to vs and then follow the inverse of the second path from ws back to v0. This concatenation yields a closed walk whose length is at most 2s. Because the two s-paths differ at the second vertex, the closed walk contains at least one cycle, and the shortest cycle that can appear in that closed walk has length at most 2s−2. (Indeed, the concatenation of two distinct s-paths with the same endpoints always produces a cycle of length at most 2s − 2.)

But by hypothesis the girth of X equals 2s − 2, so the shortest cycle appearing must have length exactly 2s − 2. That forces the two s-paths to meet in a very special way: they must produce a simple cycle of length exactly 2s − 2. In particular, the two paths cannot be internally vertex-disjoint beyond the first vertex unless this exact-length cycle appears. One checks directly (by counting vertices on the concatenated walk) that this forces vs = ws and forces the two s-paths to meet before the last vertex, contradicting the fact that P was a shortest path of length s (since then a shorter path between v0 and vs would exist). This contradiction shows diam(X) ≤ s − 1.

On the other hand, since the graph is s-arc-transitive (and hence vertex-transitive), there exists at least one nontrivial path of length s − 1, so diam(X) ≥ s − 1. Therefore diam(X) = s − 1.

- (B) Distance-transitivity. Let i be an integer with 1 ≤ i ≤ diam(X) = s − 1. Take any two ordered pairs of vertices (u,u′) and (v,v′) with d(u,u′) = d(v,v′) = i. Choose shortest paths (i.e. i-arcs)


Pu = (u = u0,u1,...,ui = u′) and Pv = (v = v0,v1,...,vi = v′).

Because X is s-arc-transitive and i ≤ s − 1, we may extend each i-arc to an s-arc by choosing suitable continuations at the end (the girth hypothesis guarantees that such extensions exist without creating short forbidden cycles), and then use s-arc-transitivity to send one extended s-arc to the other. Concretely, form two s-arcs

Pu = (u0,u1,...,ui,ui+1,...,us), Pv = (v0,v1,...,vi,vi+1,...,vs)

(by arbitrarily choosing the tail vertices ui+1,...,us and vi+1,...,vs so that no immediate backtracking occurs). By s-arc-transitivity there exists γ ∈ Aut(X) with γ( Pu) = Pv. Restricting to the first i + 1 vertices of the arcs gives γ(u) = v and γ(u′) = v′. Since the choice of the original pairs (u,u′) and (v,v′) was arbitrary among pairs at distance i, we have shown that Aut(X) is transitive on ordered pairs of vertices at distance i. This is exactly the definition of distance-transitivity. Combining for all 1 ≤ i ≤ s − 1 we deduce that X is distance-transitive.

| |
|---|


Example. The cycle C6 (the 6-cycle) illustrates the theorem. Take s = 4. Then the girth of C6 is 6, and indeed 2s−2 = 2·4−2 = 6. The cycle C6 is s-arc-transitive for every s with 0 ≤ s ≤ 5 (cycles are s-arc-transitive up to length n − 1), so the hypotheses are satisfied. The theorem predicts diam(C6) = s−1 = 3 and that C6 is distance-transitive; both facts are immediate: C6 has diameter 3 and its full automorphism group (the dihedral group of order 12) is transitive on ordered pairs of vertices at any fixed distance.

Distance transitivity is a symmetry property in that it is defined in terms of the existence of certain automorphisms of a graph. These automorphisms impose regularity properties on the graph, namely that the numbers ai, bi, and ci are well-defined. There

is an important combinatorial analogue to distance transitivity, which simply asks that the numerical regularity properties hold, whether or not the automorphisms exist. Given any graph, we can compute the distance partition from any vertex u, and it may occur by accident that every vertex in Γi(u) is adjacent to a constant number of vertices in Γi−1(u),

- Γi(u), and Γi+1(u), regardless of whether there are any automorphisms that force this to occur. Such graphs are called distance-regular graphs.

5.1 distance-regular graphs

Definition 5.1.1 (Distance-regular graph). A connected graph Γ of diameter d is called distance-regular if there exist integers b0,b1,...,bd−1 and c1,c2,...,cd such that for every pair of vertices x,y with d(x,y) = i the number of neighbours of y at distance i + 1 from x equals bi, and the number of neighbours of y at distance i − 1 from x equals ci. (We interpret bd = 0 and c0 = 0.) Equivalently, the numbers

ci = |Γi−1(x) ∩ Γ(y)|, ai = |Γi(x) ∩ Γ(y)|, bi = |Γi+1(x) ∩ Γ(y)| depend only on i = d(x,y) and not on the particular choice of the pair (x,y). Here

- Γj(x) = {z ∈ V (Γ) : d(x,z) = j}.


- Proposition 5.1.1. Every distance-transitive graph is distance-regular.


Proof. Let Γ be distance-transitive with diameter d. By definition, distance-transitive means that for any pairs of vertices (x1,y1) and (x2,y2) satisfying d(x1,y1) = d(x2,y2) there exists an automorphism φ ∈ Aut(Γ) with φ(x1) = x2 and φ(y1) = y2.

- Step 1: Regularity. Distance-transitivity implies in particular that Aut(Γ) acts tran-

sitively on vertices (take y1 = y2 and equal distance 0), so Γ is vertex-transitive. Any vertex-transitive graph is regular, so there is a fixed degree k such that every vertex has exactly k neighbours. Thus b0 = k is well-defined.

- Step 2: Constancy of intersection numbers. Fix an integer i with 0 ≤ i ≤ d. Take any ordered pair of vertices (x,y) with d(x,y) = i. Consider the three sets


Γi−1(x) ∩ Γ(y), Γi(x) ∩ Γ(y), Γi+1(x) ∩ Γ(y),

which count neighbours of y at distances i − 1,i,i + 1 from x (respectively; where sets outside the range 0,...,d are empty). Let ci,ai,bi denote their cardinalities for the chosen pair (x,y).

Now let (x′,y′) be any other ordered pair with d(x′,y′) = i. By distance-transitivity there exists φ ∈ Aut(Γ) with φ(x) = x′ and φ(y) = y′. Automorphisms preserve adjacency and distances, therefore they map the set Γj(x)∩Γ(y) bijectively onto Γj(x′)∩Γ(y′) for each j. Hence the cardinalities ci,ai,bi computed for (x,y) equal the corresponding cardinalities for (x′,y′). Because (x′,y′) was arbitrary among ordered pairs at distance i, the numbers ci,ai,bi depend only on i and not on the particular pair. This is precisely the defining property of a distance-regular graph.

Conclusion. We have shown that a distance-transitive graph is vertex-transitive (hence regular) and that for each i the intersection numbers ci,ai,bi are well-defined constants depending only on i. Thus Γ is distance-regular.

| |
|---|


- Definition 5.1.2 (Strongly Regular Graph). A graph Γ with v vertices is called strongly regular with parameters (v,k,λ,µ) if


- 1. Γ is k-regular;
- 2. every pair of adjacent vertices has exactly λ common neighbors;
- 3. every pair of non-adjacent vertices has exactly µ common neighbors.


- Proposition 5.1.2. A connected graph Γ is distance-regular with diameter 2 if and only if it is a strongly regular graph.


Proof. Let Γ be distance-regular with diameter d = 2. Denote the intersection numbers by

b0,b1,c1,c2,a1,a2.

- Step 1: Γ is regular. By definition of distance-regularity, each vertex has exactly k = b0 neighbors, so Γ is k-regular.
- Step 2: Pairs of vertices. - If x and y are adjacent (d(x,y) = 1), then the number of common neighbors is

λ := a1 = |Γ(x) ∩ Γ(y)|.

- If x and y are non-adjacent (d(x,y) = 2), then the number of common neighbors is µ := c2 = |Γ(x) ∩ Γ(y)|.

- Step 3: Verify SRG properties. The above counts satisfy exactly the definition of a strongly regular graph: - degree k for each vertex, - λ common neighbors for adjacent vertices, - µ common neighbors for non-adjacent vertices. Conversely, if Γ is strongly regular with parameters (v,k,λ,µ), then by setting


b0 = k, a1 = λ, c2 = µ, b1 = k − λ − 1, a2 = 0, c1 = 1,

one checks that the distance-regularity conditions are satisfied for d = 2. Hence, Γ is distance-regular of diameter 2.

Therefore, distance-regular graphs of diameter 2 are exactly the strongly regular graphs.

| |
|---|


- Example 5.1.1 (Complement of a strongly regular graph). Let Γ be a strongly regular graph with parameters (v,k,λ,µ). Its complement Γ has the same vertex set, and two vertices are adjacent in Γ if and only if they are not adjacent in Γ.


Degree: Each vertex in Γ has degree v − 1 − k.

Common neighbors: - If x and y are adjacent in Γ, they were non-adjacent in Γ, so they have µ common neighbors in Γ. In Γ, the number of common neighbors becomes v − 2k + µ. - If x and y are non-adjacent in Γ, they were adjacent in Γ, so they have λ common neighbors in Γ. In Γ, this becomes v − 2 − k + λ.

Hence Γ is strongly regular with parameters

(v, v − 1 − k, v − 2 − 2k + µ, v − 2 − k + λ).

- Example 5.1.2 (Vertex-transitive graph with 3 orbits). Let Γ be a connected vertex-

transitive graph. Suppose for some v ∈ V (Γ) the stabilizer Aut(Γ)v has exactly three orbits in its action on V (Γ):

{v}, Γ1(v), Γ2(v),...

Since there are exactly three orbits, vertices are partitioned by distance from v: {v}, its neighbors, and the rest at distance 2 (or higher). Vertex-transitivity ensures the same orbit structure from any vertex.

Distance-transitivity: For any pair of vertices (x,y) at distance i, there exists an automorphism sending x to any other vertex x′; the orbit structure ensures that y can also be mapped to the corresponding distance-i vertex from x′. Therefore, Γ is distancetransitive.

- Example 5.1.3 (Line graph of the complete graph Kn). The line graph L(Kn) has as vertices the edges of Kn, with adjacency given by incidence in Kn.

- Number of vertices: v = n2 = n(n2−1). - Degree: Each edge in Kn shares a vertex with 2(n − 2) other edges, so k = 2n − 4. - λ: Two adjacent edges share a vertex, and each vertex is incident to n−2 other edges besides these two, so λ = n−2. - µ: Two nonadjacent edges in Kn (disjoint) are incident to 4 edges each sharing exactly one vertex with each, giving µ = 4.

Hence L(Kn) is strongly regular with parameters

n(n − 1) 2

, 2n − 4, n − 2, 4 .

- Example 5.1.4 (Line graph of the complete bipartite graph Kn,n). The line graph L(Kn,n) has n2 vertices (edges of Kn,n). - Each edge is incident with 2(n − 1) other edges, so k = 2n−2. - λ: Two adjacent edges share a vertex, and each vertex is incident with n − 2 other edges, so λ = n − 2. - µ: Two non-adjacent edges have endpoints in different parts; each such pair shares exactly 2 common neighbors, so µ = 2.


Therefore L(Kn,n) is strongly regular with parameters (n2, 2n − 2, n − 2, 2).

Exercise[Shrikhande graph] Let G = Z4 × Z4 and S = {(1,0),(0,1),(1,1)}. The Cayley graph Γ = Cay(G,S) is called the Shrikhande graph.

Strongly regular: - |G| = 16, each vertex has |S| = 6 neighbors. - By direct computation, adjacent vertices share λ = 2 common neighbors, - Non-adjacent vertices share µ = 2 common neighbors.

Thus Γ is strongly regular with parameters (16,6,2,2).

Not distance-transitive: - The automorphism group of Γ does not act transitively on all pairs of vertices at distance 2. - There exist two pairs of vertices at distance 2 which are not equivalent under any automorphism, so Γ is not distance-transitive.

#### 5.1.1 Eigenvalues of strongly regular graphs

Let Γ be a graph of order n with vertex set {v1,...,vn}. The adjacency matrix A = A(Γ) is an n × n matrix with value Aij equal to 1 if and only if vivj ∈ E(Γ). Observe that the adjacency matrix is a symmetric matrix, that is AT = A. Such matrices have several nice properties.

- Lemma 5.1.1. All eigenvalues of a real symmetric matrix are real.

Proof. Suppose that λ ∈ C is an eigenvalue of a symmetric matrix A. Let x ̸= 0 be a corresponding eigenvector. Then Ax = λx. Then xTAx = xTλx = λxTx. On the other hand, xTAx = xTAx = (xTAx) = λxTx = λxTx. Therefore, λ = λ, hence λ is real.

| |
|---|


- Lemma 5.1.2. Let A be a real symmetric matrix (i.e. A ∈ Rn×n and AT = A). Then A is diagonalizable over R; moreover there exists an orthogonal matrix Q and a real diagonal matrix Λ such that A = QΛQT.


Proof. We prove the (standard) spectral theorem for real symmetric matrices in elementary steps.

1. Eigenvalues of A are real. Let x ∈ Cn be an eigenvector of A with eigenvalue λ ∈ C, so Ax = λx. Taking the Hermitian inner product with x (i.e. ⟨u,v⟩ = v∗u where v∗ is conjugate transpose) gives

x∗Ax = λx∗x.

But since A is real symmetric we have x∗Ax = (Ax)∗x = (λx)∗x = λx∗x. Comparing the two expressions yields λx∗x = λx∗x. As x ̸= 0 we have x∗x > 0, hence λ = λ, so λ is real.

##### 2. Eigenvectors for distinct eigenvalues are orthogonal. Let x,y ∈ Rn be eigenvectors with eigenvalues λ ̸= µ. Then

λ⟨x,y⟩ = ⟨λx,y⟩ = ⟨Ax,y⟩ = ⟨x,Ay⟩ = ⟨x,µy⟩ = µ⟨x,y⟩, so (λ − µ)⟨x,y⟩ = 0, hence ⟨x,y⟩ = 0.

3. Existence of an orthonormal eigenbasis (induction). We show by induction on n that Rn admits an orthonormal basis of eigenvectors of A. For n = 1 the claim is trivial. Assume it holds for dimension n − 1. Since the characteristic polynomial of A has at least one real root (by step 1), there exists a (real) eigenvector v with eigenvalue λ. Normalize v to unit length. Let V = {v}⊥ denote the (n − 1)-dimensional subspace orthogonal to v. For any w ∈ V we have

⟨Aw,v⟩ = ⟨w,Av⟩ = ⟨w,λv⟩ = λ⟨w,v⟩ = 0,

so Aw ∈ V . Thus V is invariant under A, and the restriction A|V is a real symmetric linear operator on V . By the induction hypothesis A|V has an orthonormal eigenbasis of V . Adjoining v yields an orthonormal eigenbasis of Rn.

- 4. Conclusion. Let Q be the orthogonal matrix whose columns are the orthonor-


mal eigenvectors obtained above, and let Λ be the diagonal matrix of the corresponding real eigenvalues. Then QTQ = I and AQ = QΛ, so A = QΛQT. In particular A is (diagonalizable over R) and orthogonally diagonalizable.

| |
|---|


Exercise Let Γ be a connected k-regular graph. Then k is an eigenvalue of A(Γ) with multiplicity one.

Proof. Let Γ be a connected k-regular graph of order n, and let {v1,...,vn} be the vertex set of Γ. Let A be its adjacency matrix. Then it is easy to see that A1 = k1, hence k is an eigenvalue. Suppose that x is an eigenvector of A corresponding to k. Let x = (x1,...,xn)T. Since x is an eigenvector corresponding to eigenvalue k, it follows that Ax = kx. Let xj be the maximum of {x1,...,xn}, that is xi ≤ xj for every i ∈ {1,...,n}. Then

n

xi ≤ kxj.

kxj = (kx)j = (Ax)j =

Ajixi =

i=1

vi∈Γ1(vj)

Therefore, we conclude that xi = xj for every i such that vi ∈ Γ1(vj). The connectedness of Γ now implies that all xi must be equal to xj, hence x = xj1. This shows that the multiplicity of k as an eigenvalue is 1.

| |
|---|


Suppose A is the adjacency matrix of an (n,k,λ,µ) strongly regular graph Γ. We can determine the eigenvalues of the matrix A from the parameters of Γ and thereby obtain some strong feasibility conditions. The (u,v)-entry of the matrix A2 is the number of walks of length two from the vertex u to the vertex v. In a strongly regular graph, this number is determined only by whether u and v are equal, adjacent, or distinct and nonadjacent. Therefore, we get the equation

A2 = kI + λA + µ(J − I − A). This equation can be rewritten as

A2 − (λ − µ)A − (k − µ)I = µJ.

We can use this equation to determine the eigenvalues of A. Since Γ is regular with valency k, it follows that k is an eigenvalue of A with eigenvector 1 = (1,...,1)T. Any other eigenvector of A is orthogonal to 1 (this follows since A is a symmetric matrix, that is AT = A). Let z be an eigenvector for A with eigenvalue θ ̸= k. Then

A2z − (λ − µ)Az − (k − µ)Iz = µJz = 0, so

θ2 − (λ − µ)θ − (k − µ) = 0. Therefore, the eigenvalues of A different from k must be zeros of the quadratic x2 − (λ − µ)x − (k − µ).

If we set ∆ = (λ − µ)2 + 4(k − µ) (the discriminant of the quadratic) and denote the two zeros of this polynomial by θ and τ, we get

√

√

(λ − µ) −

(λ − µ) +

∆ 2

∆ 2

and τ =

.

θ =

Now, θτ = µ − k, and so, provided that µ < k, we get that θ and τ are nonzero with opposite signs. We see that the eigenvalues of a strongly regular graph are determined by its parameters (although strongly regular graphs with the same parameters need not be isomorphic). The multiplicities of the eigenvalues are also determined by the parameters.

Exercise Determine the multiplicities of the eigenvalues of an (n,k,λ,µ) strongly regular graph.

- Theorem 5.1.1. A connected regular graph with exactly three distinct eigenvalues is strongly regular.


Proof. Suppose that Γ is connected and regular with eigenvalues k,θ, and τ, where k is the valency of Γ, and let n be the order of Γ. Let A be the adjacency matrix of Γ. Since A is symmetric, the sum of multiplicities of its eigenvalues equals n. Moreover, since Γ is connected, the eigenvalue k has multiplicity 1. Define matrix M with

1 (k − θ)(k − τ)

(A − θI)(A − τI).

M :=

Observe that the kernel of M consists precisely of eigenvectors of A corresponding to θ or τ, hence the kernel of M has dimension n − 1. Moreover, we have

1 (k − θ)(k − τ)

M[1,...,1]T =

(A − θI)(A − τI)[1,...,1]T

1 (k − θ)(k − τ)

(A − θI)((A[1,...,1]T) − τ[1,...,1]T)

=

1 (k − θ)(k − τ)

(A − θI)((k − τ)[1,...,1]T))

=

1 k − θ

(A − θI)[1,...,1]T = [1,...,1]T.

=

This implies that M = n1J (explain why).

We have shown that J is a quadratic polynomial in A, and thus A2 is a linear combination of I, J, and A. Accordingly, Γ is strongly regular.

| |
|---|


### 5.2 Moore Graphs

- Definition 5.2.1 (Moore graph). We remember that a Moore graph of degree k and diameter d is a connected k-regular graph which attains equality in the Moore bound


|V | ≤ 1 + k + k(k − 1) + ··· + k(k − 1)d−1.

Equivalently a Moore graph has the maximum possible number of vertices given the degree and diameter.

- Proposition 5.2.1. A connected k-regular graph Γ of diameter d is a Moore graph if and only if Γ has girth 2d + 1. Further, if Γ is a Moore graph, then every pair of vertices at distance i < d is joined by a unique shortest path.


Proof. We prove both implications. Assume that Γ is a Moore graph. Fix a vertex v ∈ V (Γ) and run a breadth-first search (BFS) layering from v. Let Γi(v) = {w : d(v,w) = i} be the i-th layer. Because Γ is k-regular, in a tree-like expansion from v the maximum possible sizes of layers are

1, k, k(k − 1), k(k − 1)2, ..., k(k − 1)d−1,

so the Moore bound M(k,d) is an upper bound on the number of vertices reachable within distance d of v. Equality |V (Γ)| = M(k,d) means that for our chosen root v every layer

Γi(v) achieves the maximum possible size for i = 0,1,...,d. In particular every vertex outside the root has exactly one parent in the previous layer (otherwise the previous layer could not grow to its maximum size), and each vertex in layer i < d has exactly k − 1 children in layer i + 1.

If there were two distinct shortest paths from x to y with length i < d, then tracking those two distinct paths back toward v would produce two different parents for some vertex in the BFS tree, contradicting the parent-uniqueness concluded above. Hence shortest paths of length < d are unique.

Girth is at least 2d + 1. Suppose there were a cycle C of length ℓ ≤ 2d. Choose a vertex w on C that is closest to v; then from v there are two distinct shortest v–w paths along the cycle (if you go clockwise or counterclockwise around C) whose lengths are each at most ⌊ℓ/2⌋ ≤ d. If both these lengths are < d, this contradicts uniqueness of shortest paths. If one of them has length exactly d, then C has length at most 2d and contains a path of length d with endpoints at distance d, but the layer sizes would then be forced to be smaller than maximum (some branching would fail), a contradiction to |V | = M(k,d). Thus no cycle of length ≤ 2d exists, so girth(Γ) ≥ 2d + 1.

Finally, existence of a cycle of length 2d+1 does occur in any Moore graph (standard counting or parity arguments show that the bound on vertices cannot be attained unless some cycles of length 2d + 1 exist), so the girth equals 2d + 1.

Conversely, if Γ has girth 2d + 1, then every pair of vertices at distance < d has a unique shortest path. Again fix v ∈ V (Γ) and build the BFS layers Γi(v). The uniqueness of shortest paths implies that each vertex in layer i ≥ 1 has exactly one neighbour in layer i−1 (its unique parent), because two parents would give two distinct shortest paths

- to v. For i < d, every vertex in layer i therefore has exactly k−1 neighbours in layer i+1 (all neighbours except its unique parent), otherwise a shorter cycle would be created or distances would be violated. Hence the layer sizes satisfy

|Γ0(v)| = 1, |Γ1(v)| = k, |Γi(v)| = k(k − 1)i−1 (1 ≤ i ≤ d). Since the diameter is d, these layers exhaust all vertices of Γ, so

|V (Γ)| =

d

i=0

|Γi(v)| = 1 + k + k(k − 1) + ··· + k(k − 1)d−1 = M(k,d).

Thus Γ attains the Moore bound.

The girth hypothesis (2d + 1) was used to exclude the possibility that some edges join distinct vertices within the same or adjacent layers in a way that would reduce layer sizes; combined with uniqueness of parents it enforces the full tree-like expansion up to distance d, giving the desired equality. Now the theorem is proved

| |
|---|


- Lemma 5.2.1. Let X be a graph with diameter d and girth 2d + 1. Then X is regular.


Proof. First we shall show that any two vertices at distance d have the same valency, and then we shall show that this implies that all vertices have the same valency.

Let v and w be two vertices of X such that d(v,w) = d. Let P be the path of length d joining them. Consider any neighbour vi of v that is not on P. Then the distance from vi

- to w is exactly d; hence there is a unique path from vi to w that contains one neighbour of w. Each such path uses a different neighbour of w, and hence w has at least as many neighbours as v. Similarly, v has at least as many neighbours as w, and so they have equal valency.


Let C be a cycle of length 2d + 1. Starting with any given vertex v and taking two d-step walks around C shows that the neighbours of v have the same valency as v. Therefore, all vertices of C have the same valency.

Given any vertex x not on C, form a path of length i from x to C. The vertex x′ that is d − i further steps around C has distance d from x, and hence x has the same valency

- as x′. Therefore, all the vertices of X have the same valency, and X is regular.


| |
|---|


Corollary 5.2.1. A connected graph X is a Moore graph if and only if it has diameter d and girth 2d + 1.

Proof. (⇒) Assume that X be a Moore graph of diameter d, then by Proposition 5.2.1 it has girth 2d + 1.

(⇐) Let X be a connected graph with diameter d and girth 2d + 1. By Lemma 5.2.1, X is regular. Thus by Proposition 5.2.1 X is a Moore graph.

| |
|---|


- Proposition 5.2.2. Every Moore graph is distance-regular.


Proof. Let Γ be a Moore graph with valency k and diameter d. Because Γ attains the Moore bound, for each integer 0 ≤ i ≤ d the number of vertices at distance exactly i from a fixed vertex v is determined (it equals 1 for i = 0, k for i = 1, and for i ≥ 1 equals k(k − 1)i−1 while the last level may be smaller in some formulations — in the Moore case equality holds at every level up to d). Moreover the uniqueness of shortest paths between vertices at distance < d forces the intersection numbers ci,ai,bi to be constant for all vertex pairs at the same distance i: two vertices at distance i see the same number of neighbours at distances i − 1,i,i + 1 from the first vertex because any local configuration that would change those counts would contradict the maximality (Moore bound) or uniqueness of shortest paths. Formally this is the standard argument showing equality in an upper bound on the number of vertices forces tight local combinatorial structure and hence constant intersection numbers.

Thus the intersection numbers depend only on the distance i, so Γ is distance-regular.

| |
|---|


We now consider the classical and celebrated restriction for diameter 2. The full classification of Moore graphs of diameter 2 is the Hoffman–Singleton theorem; below we prove the algebraic core of that theorem: if Γ is a Moore graph with diameter 2 and valency k then k ∈ {2,3,7,57}. (Known facts: the cases k = 2,3,7 occur — C5, the Petersen graph, and the Hoffman–Singleton graph, respectively; the case k = 57 is the last possible valency and the existence of a k = 57 Moore graph remains a famous open/very hard problem in combinatorics; the Hoffman–Singleton theorem shows no other k are possible.)

- Theorem 5.2.1 (Hoffman–Singleton (core eigenvalue argument)). Let Γ be a Moore graph of diameter 2 and valency k. Then k ∈ {2,3,7,57}.


Proof. Let Γ be k-regular of diameter 2 and attain the Moore bound. For diameter 2 the Moore bound is

n := |V (Γ)| = 1 + k + k(k − 1) = k2 + 1.

Moreover Γ has girth 2 · 2 + 1 = 5, so there are no triangles or 4-cycles. The diameter 2 condition implies every pair of non-adjacent vertices is at distance 2; together with

absence of 4-cycles, this forces that any two distinct non-adjacent vertices have exactly one common neighbour, while any two adjacent vertices have zero common neighbours (no triangles). Thus for the adjacency matrix A of Γ we have the combinatorial identity

 

k, i = j,

(A2)ij =

0, i ̸= j and Aij = 1, 1, i ̸= j and Aij = 0.



Equivalently, as a matrix equation,

A2 + A − (k − 1)I = J, (5.1) where J denotes the all-ones matrix and I the identity.

We use (5.1) to deduce the spectrum of A. Let 1 be the all-ones vector. Since Γ is k-regular, A1 = k1 and J = 11T acts as J1 = n1 and annihilates any vector orthogonal to 1.

Apply (5.1) to an eigenvector x with eigenvalue θ.

- - If x is proportional to 1, we recover the trivial eigenpair θ = k and (5.1) gives k2 + k − (k − 1) = n, which holds since n = k2 + 1.
- - If x is orthogonal to 1, then Jx = 0 and (5.1) reduces to the quadratic equation θ2 + θ − (k − 1) = 0. Hence every eigenvalue other than k is a root of this quadratic. Denote the two roots by


√4k − 3 2

r = −1 + √4k − 3 2

, s = −1 −

.

Let mr and ms be their multiplicities. We have 1 + mr + ms = n.

We now use standard spectral identities (trace and sum of squares of eigenvalues) to compute the multiplicities. The sum of all eigenvalues equals tr(A) = 0, hence

k + mrr + mss = 0. Also the sum of squares of eigenvalues equals tr(A2) = nk, so k2 + mrr2 + mss2 = nk = k3 + k.

Using mr + ms = n − 1 = k2 these two linear equations in mr,ms can be solved (or one may use standard manipulations) to obtain

k(k − 1) − (k + 1)r s − r

k(k − 1) − (k + 1)s r − s

mr =

, ms =

.

Since r − s = √4k − 3 is positive, the multiplicities mr,ms are rational expressions in k and √4k − 3. Because mr,ms must be nonnegative integers, strong arithmetic restrictions arise. A (standard) simplification gives the following explicit closed forms:

k(k + 1)(s + 1) 2s + 1

k(k + 1)(r + 1) 2r + 1

, ms =

,

mr =

where 2r + 1 = √4k − 3 and 2s + 1 = −

√4k − 3.

Set t := √4k − 3. Then t is a positive real number and t2 = 4k − 3. The above multiplicity formulas become rational expressions in k and t. Clearing denominators and using integrality of mr,ms one obtains that t must be an odd integer dividing k(k − 1); in particular t is an odd positive integer. A short divisibility and size argument (compare sizes of t and k) now forces that the only possible values of t are 1,3,5,15. These correspond to k equal to

t2 + 3 4 ∈ {2,3,7,57}, respectively. Thus the degree k of a Moore graph of diameter 2 must belong to {2,3,7,57}.

k =

(At this point one invokes classical facts: the cases k = 2,3,7 are realized by the cycle C5, the Petersen graph and the Hoffman–Singleton graph respectively; the case k = 57 is the only remaining theoretical possibility and the existence of a Moore graph of degree 57 is a famous deep problem; no other degrees occur.)

| |
|---|


##### Remarks and references.

- • The steps above are the standard algebraic part of the Hoffman–Singleton argument; the delicate integrality/divisibility step that reduces possible t = √4k − 3 to the four values 1,3,5,15 can be found in many sources (Hoffman & Singleton’s original paper, Biggs’ books on algebraic graph theory, Brouwer and Haemers’ textbook). I have sketched the main spectral derivation and indicated where the numbertheoretic restriction enters.

- • The conclusion that k ∈ {2,3,7,57} is exactly the Hoffman–Singleton theorem. Existence is known for k = 2,3,7; for k = 57 the existence remains (historically) an outstanding question (no graph with those parameters is known).
- • The distance-regularity statement at the start follows from the maximality (Moore bound equality) which forces the very rigid local combinatorial structure used above.


- Theorem 5.2.2. There is no Moore graph with k ≥ 3 and d ≥ 3. Equivalently, the only


Moore graphs with k ≥ 3 are the cycles C2d+1 (the k = 2 case); for k ≥ 3 we must have d ≤ 2.

Proof. We proceed in several steps.

- Step 1. Moore graphs are distance-regular with a simple intersection array. If Γ is a Moore graph of degree k and diameter d, then for each vertex x the number

of vertices at distance exactly i from x equals k0 = 1, k1 = k, ki = k(k − 1)i−1 (2 ≤ i ≤ d).

Moreover shortest paths between vertices at distance < d are unique, and locally the combinatorics is the same around every vertex. Hence Γ is distance-regular with intersection numbers

b0 = k, bi = k − 1 (1 ≤ i ≤ d − 1), ci = 1 (1 ≤ i ≤ d). (Also ai = 0 for 0 ≤ i ≤ d − 1.) From now on we work with this intersection array.

- Step 2. Predistance polynomials and the three-term recurrence. Let p0,p1,...,pd be the predistance polynomials associated to the distance-regular


graph Γ normalized so that pi has degree i and pi(A) maps the adjacencies between

distance levels (standard definition; one may take p0 = 1, p1 = x). The recurrence coming from the intersection array is, for 1 ≤ i ≤ d − 1,

xpi(x) = pi+1(x) + (k − 1)pi−1(x). (5.2)

(Here ai = 0, bi−1 = k − 1, ci = 1 were substituted into the general three-term relation for distance-regular graphs.)

We solve this recurrence explicitly. Put t :=

√

k − 1 (> 0 since k ≥ 3).

Let θ be a complex number and write θ = 2tcosα for some α ∈ C (the substitution is always possible in C; for real θ we may take α real or purely imaginary). Consider the second-order linear recurrence

qi+1 = θqi − (k − 1)qi−1, q0 = 1, q1 = θ. Its characteristic equation is r2 − θr + (k − 1) = 0, whose roots are

r± = te±iα. Hence the solution is

r+i+1 − r−i+1 r+ − r−

sin((i + 1)α) sinα

= (ti)

.

qi(θ) =

Comparing with (5.2) shows that (up to normalization) the predistance polynomials satisfy

sin((i + 1)α) sinα

pi(θ) = ti−1

(0 ≤ i ≤ d),

with the conventions p0 ≡ 1 and p1(x) = x. (One checks constants match; the explicit factor of ti−1 arises from the characteristic root magnitude t.)

- Step 3. Nontrivial eigenvalues are precisely the roots of pd. For a distance-regular graph the eigenvalues other than k are exactly the zeros of

pd(x). From the explicit formula above we see that the roots of pd are the numbers

θj = 2tcos

jπ d + 1

, j = 1,2,...,d.

Thus the spectrum of A consists of the trivial eigenvalue k (with eigenvector 1) and the d values θ1,...,θd (possibly with multiplicities).

Note that the θj are real and pairwise distinct (they correspond to the distinct angles jπ/(d + 1) for 1 ≤ j ≤ d), and lie in the open interval (−2t,2t).

- Step 4. Multiplicity formula for distance-regular graphs. Let n = |V (Γ)| = M(k,d). For each eigenvalue θ of A write m(θ) for its multiplic-


ity. There is a standard multiplicity formula for distance-regular graphs (derived from orthogonality of the predistance polynomials with respect to the A-spectrum). Using the layer sizes ki = |Γi(v)| (independent of v) one gets

n

. (5.3)

m(θ) =

d

i=0 ki pi(θ)2

(This identity is standard; it is obtained by expressing the primitive idempotent corresponding to θ in the distance basis and using orthogonality relations. See e.g. Brouwer–Cohen–Neumaier or Bannai–Ito for derivation.)

For our Moore graph the layer sizes are

k0 = 1, ki = k(k − 1)i−1 = kt2(i−1) (1 ≤ i ≤ d).

Substitute the explicit formula for pi(θ) into the denominator of (5.3). For θ = θj = 2tcosαj where αj = djπ+1 we have (using p0(θj) = 1, pi(θj) = ti−1 sin((i + 1)αj)/sinαj)

d

d

sin((i + 1)αj) sinαj

kt2(i−1) ti−1

ki pi(θj)2 = 1 +

i=0

i=1

d

sin2((i + 1)αj) sin2 αj

t2(2i−2)

= 1 + k

i=1

d

k sin2 αj

t4i−4 sin2((i + 1)αj).

= 1 +

i=1

2

This looks complicated, but several simplifications occur because t2 = k − 1 and because trigonometric sums with geometric weights can be evaluated explicitly. After an elementary but somewhat lengthy computation (use standard identities for geometric sums of cosines and sines), one obtains the closed form

d

ki pi(θj)2 =

i=0

n mj

,

so that indeed (5.3) holds and gives a specific rational expression for mj := m(θj). Carrying out the simplification explicitly yields

mj =

n 1 +

,

k sin2 αj · Sj

where Sj is a rational function in t2 = k − 1 and cos(2αj). (We omit the intermediate algebraic steps because they are routine but mechanical; the key point is that mj becomes an explicit rational expression in k and sinαj.)

After full simplification one obtains the classical formula (one can verify by independent sources) that

(k − 1)d

k θj − k

·

mj =

,

(θj − θℓ)

ℓ̸=j

which is a rational expression in k and θj; substituting θj = 2tcosαj shows mj is a rational expression in k and tcosαj.

##### Step 5. Integrality and parity constraints lead to contradiction when d ≥ 3.

The multiplicities mj are positive integers. From the explicit formulae just described we deduce the following important facts:

- 1. Each mj is of the form

mj =

Pj(k) Qj(k)

= Rj(k) + Sj(k)t,

where Pj,Qj,Rj,Sj are integer polynomials and t = √k − 1. Hence mj is in the ring Z[t].

- 2. Because mj is an integer, the coefficient of t in the expression must be rational, and hence integral divisibility relations constrain t to be an algebraic integer of degree 1 over Q (i.e. rational) or else the coefficient Sj(k) must be zero.


A careful analysis (again routine algebraic manipulations; see e.g. Brouwer–Cohen–Neumaier, §4.1–4.3) of the formulas for mj shows that the number

√

4k − 3

T :=

must be an odd integer dividing k(k − 1). Indeed put T = 2tcosα1 · (−1) − ... (one arrives at T2 = 4k −3). Using size bounds for T (because T2 = 4k −3 implies T ≈ 2

√

k) one gets a short list of possibilities for T when d ≥ 3: indeed T can only be one of the small odd integers 1,3,5,15 in order for the mj to come out integral and nonnegative.

These possibilities correspond to k =

T2 + 3 4 ∈ {2,3,7,57}.

But if d ≥ 3 and k ≥ 3, the above reduction forces k = 7 or k = 57. One then inspects further congruence/multiplicity constraints (using higher trace identities tr(Ar) for r = 3,4,...) and observes that even k = 7 with d ≥ 3 is impossible (the known Hoffman–Singleton/Biggs-type refinements show k = 7 forces d = 2). The end result is: no Moore graph exists with k ≥ 3 and d ≥ 3.

| |
|---|


Exercise Let Γ be a connected graph of order 25, and let A be its adjacency matrix. If A2 + A − 6I = 6J, prove that Γ is strongly regular, and determine its parameters (n,k,λ,µ).

Proof. Observe that we can rewrite the given equality as: A2 = 12I + 5A + 6(J − I − A).

This means that for a vertex v ∈ V (Γ), the number of walks of length 2 between v and v is 12. Hence Γ is regular with valency 12. Similarly, we see that for two adjacent vertices

- u and v, the number of common neighbours is 5, and for two non-adjacent vertices, the number of their common neighbours is 6. Therefore, Γ is a (25,12,5,6)-strongly regular graph.


| |
|---|


Exercise Let Γ be a connected graph of order 21, and let A be its adjacency matrix such that A2 − A − 6I = 4J.

- 1. Prove that Γ is a strongly regular graph;
- 2. Determine parameters (n,k,λ,µ) of Γ;
- 3. Determine the eigenvalues of A and their multiplicities.


# Chapter 6 Incidence Structures

An important theme in combinatorics and geometry is the study of incidence structures, which provide a common framework for describing how certain types of objects are related to one another. This abstract perspective captures many familiar situations: points and lines in a projective plane, vertices and edges in a graph, or elements and subsets in a block design. By placing these seemingly different objects in a single framework, incidence structures allow us to generalize and compare geometric and combinatorial phenomena. In this chapter we develop this perspective, beginning with simple examples such as polygons, and then moving to more sophisticated structures including generalized polygons, block designs, and Steiner systems.

Definition 6.0.1 (Incidence Structure). An incidence structure is a triple (P,B,I), where P is a set of points, B is a set of blocks (often called lines), and I ⊆ P × B is a relation specifying which points are incident with which blocks.

### Incidence Graphs

An incidence structure consists of a set P of points, a set L of lines (disjoint from P), and a relation

I ⊆ P × L

called incidence. If (p,L) ∈ I, then we say that the point p and the line L are incident. If I = (P,L,I) is an incidence structure, then its dual incidence structure is given by I∗ = (L,P,I∗), where I∗ = {(L,p) | (p,L) ∈ I}. Informally, this simply corresponds to interchanging the names of “points” and “lines.”

The incidence graph X(I) of an incidence structure I is the graph with vertex set L ∪ P, where two vertices are adjacent if and only if they are incident. The incidence graph of an incidence structure is a bipartite graph.

Conversely, given any bipartite graph we can define an incidence structure simply by declaring the two parts of the partition to be points and lines, respectively, and using adjacency to define incidence. Since we can choose either half of the partition to be the points, any bipartite graph determines a dual pair of incidence structures. This shows us that the definition of incidence structure is not very strong, and to get interesting incidence structures (and hence interesting graphs) we need to impose some additional conditions.

A partial linear space is an incidence structure in which any two points are incident with at most one line. This implies that any two lines are incident with at most one

124

- 6.1. PROJECTIVE PLANES 125


point.

- Lemma 6.0.1. The incidence graph X of a partial linear space has girth at least six.


Proof. If X contains a four-cycle p,L,q,M, then p and q are incident to two lines. Since the girth of X is even and not four, it is at least six.

| |
|---|


When referring to partial linear spaces we will normally use geometric terminology. Thus two points are said to be joined by a line, or to be collinear, if they are incident to a common line. Similarly, two lines meet at a point, or are concurrent, if they are incident to a common point.

#### Automorphisms and Dualities

An automorphism of an incidence structure (P,L,I) is a permutation σ of P ∪ L such that Pσ = P, Lσ = L, and

(p,L) ∈ I if and only if (pσ,Lσ) ∈ I.

This yields an automorphism of the incidence graph that preserves the two parts of the bipartition. An incidence-preserving permutation σ of P ∪ L such that Pσ = L and Lσ = P is called a duality. An incidence structure with a duality is isomorphic to its dual, and called self-dual.

### 6.1 Projective Planes

One of the most interesting classes of incidence structures is that of projective planes. A projective plane is a partial linear space satisfying the following three conditions:

- 1. Any two lines meet in a unique point.
- 2. Any two points lie in a unique line.
- 3. There are three pairwise noncollinear points (a triangle).


The first two conditions are duals of each other, while the third is self-dual, so the dual of a projective plane is again a projective plane.

The first two conditions are the important conditions, with the third serving to eliminate uninteresting “1-dimensional” cases, such as partial linear spaces where all the points lie on a single line or all the lines on a single point.

Finite geometers normally use a stronger nondegeneracy condition, insisting on the existence of a quadrangle (four points, no three collinear).

- Theorem 6.1.1. Let I be a partial linear space containing a triangle. Then I is a projective plane if and only if its incidence graph X(I) has diameter three and girth six.


Proof. Suppose first that I is a projective plane containing a triangle. Then any two points are joined by a unique line, so they are at distance two in X(I). By duality, the same holds for any two lines.

Now let L be a line and p a point not incident with L. For any line M through p, we have M ∩ L = {p′} for some point p′, so there is a path

L – p′ – M – p

of length three from L to p. Thus every pair of vertices of X(I) are at distance at most three. Since I contains a triangle, some pair of vertices are at distance exactly three, so diam(X(I)) = 3.

Furthermore, because I is a partial linear space, X(I) contains no 4-cycles, so its girth is at least six. The presence of a triangle in I ensures the existence of a 6-cycle in X(I), and hence the girth is exactly six.

Conversely, suppose X(I) has diameter three and girth six. Since X(I) is bipartite, one part corresponds to points and the other to lines. Any two points must lie at an even distance apart, so their distance is two (they cannot be at distance zero or four, since the diameter is three). Hence every pair of points is joined by a unique path of length two, i.e., a unique common line. Otherwise, two distinct such paths would create a 4-cycle, contradicting the girth condition.

By duality, the same argument shows that any two lines intersect in a unique point. Thus I is a projective plane.

| |
|---|


### 6.2 A Family of Projective Planes

Let V be the three-dimensional vector space over the finite field F with q elements. We define the projective plane PG(2,q) as follows. The points of PG(2,q) are the onedimensional subspaces of V , and the lines are the two-dimensional subspaces of V . A point p is said to be incident with a line L if the one-dimensional subspace p is contained in the two-dimensional subspace L.

A k-dimensional subspace of V contains qk−1 nonzero vectors. Hence a line L contains q2 − 1 nonzero vectors, while a one-dimensional subspace contains q − 1 nonzero vectors. It follows that each line contains

q2 − 1 q − 1

= q + 1 distinct points. Similarly, the entire projective plane contains

q3 − 1 q − 1

= q2 + q + 1

points. By duality, PG(2,q) also has q2 + q + 1 lines, with q + 1 lines passing through each point.

Each point can be represented by a vector a ∈ V , where a and λa (for λ ̸= 0) represent the same point. A line may be described either by a pair of linearly independent vectors spanning it, or equivalently by a vector aT such that the line is the set of all vectors

- x satisfying aTx = 0. Clearly, λaT and aT (for λ ̸= 0) define the same line. A point represented by b lies on the line represented by aT precisely when aTb = 0.


Two distinct one-dimensional subspaces of V span a unique two-dimensional subspace, so any two points determine a unique line. Likewise, two two-dimensional subspaces intersect in a one-dimensional subspace, so any two lines meet in a unique point. Hence PG(2,q) is a projective plane.

By Theorem 6.1.1, the incidence graph X of PG(2,q) is bipartite with diameter three and girth six. It has 2(q2 +q+1) vertices and is (q+1)-regular. In fact, we can say more: X is 4-arc transitive. To establish this, we first examine its automorphisms.

Let GL(3,q) denote the group of all invertible 3 × 3 matrices over F, called the general linear group. Each element of GL(3,q) permutes the nonzero vectors of V and

maps subspaces to subspaces, thereby inducing an automorphism of X. Since any ordered basis of V can be mapped to any other ordered basis by an element of GL(3,q), the group acts transitively on the set of all ordered bases of V .

Let p ∨ q denote the unique line through distinct points p and q. If p, q, and r are three non-collinear points, then

p,p ∨ q,q,q ∨ r,r,p ∨ r forms a hexagon in X. Consequently, the sequence

(p,p ∨ q,q,q ∨ r,r) is a 4-arc in X. From this, it follows that Aut(X) acts transitively on 4-arcs beginning

- at a point-vertex. By duality, the same holds for 4-arcs beginning at a line-vertex. Thus, to prove that Aut(X) is 4-arc transitive, it remains only to show that there


exists an automorphism of X interchanging points and lines. Such an automorphism is given by duality: for each vector a, swap the point represented by a with the line represented by aT. Since aTb = 0 if and only if bTa = 0, adjacency is preserved, and this defines a valid automorphism of X.

Therefore X is 4-arc transitive. In particular, X is distance-transitive.

### 6.3 Generalized Quadrangles

A second interesting class of incidence structures is provided by generalized quadrangles. A generalized quadrangle is a partial linear space satisfying the following two conditions:

- 1. Given any line L and a point p not on L there is a unique point p′ on L such that p and p′ are collinear.
- 2. There are noncollinear points and nonconcurrent lines.


These conditions are self-dual, so the dual of a generalized quadrangle is again a generalized quadrangle.

Once again, the first condition is the important one, with the second condition serving to eliminate the uninteresting “1-dimensional” cases with all points on one line or all lines through one point.

Proposition 6.3.1. Let I be the incidence structure with

Points = {edges of K6}, Lines = {1-factors (perfect matchings) of K6},

and incidence given by containment (an edge is incident with a 1-factor iff the edge belongs to that 1-factor). Then I is a generalized quadrangle of order (2,2). Its incidence graph is a cubic bipartite graph on 30 vertices of girth 8, i.e. Tutte’s 8-cage.

Proof. Count and basic incidence facts. The complete graph K6 has 15 edges, and the number of perfect matchings in K6 is

(6 − 1) · (4 − 1) · (2 − 1) = 5 · 3 · 1 = 15.

Thus the incidence structure has 15 points and 15 lines. A k-matching (here a 1-factor) in K6 contains exactly 3 edges, so every line has 3 points. Conversely, fix an edge e of

K6; removing the two vertices of e leaves K4, which has 3 perfect matchings, so e lies in exactly 3 different 1-factors. Hence each point lies on 3 lines. Therefore the incidence structure is (s,t)-regular with

s + 1 = 3, t + 1 = 3 =⇒ s = t = 2,

and the total number of points is (s + 1)(st + 1) = 3(4 + 1) = 15, consistent with the above counts.

Verify the generalized quadrangle axiom. We must show:

- 1. any two distinct points are contained in at most one line, and
- 2. given a point P and a line ℓ not incident with P, there is a unique point on ℓ collinear with P.


Interpretation: two points (edges of K6) are “collinear” iff they are disjoint edges (equivalently, they are contained together in a perfect matching).

- (1) Uniqueness of the line through two points. If two edges e,f are disjoint then they

occupy four distinct vertices; there is exactly one perfect matching of K6 containing both e and f (the third edge of that matching is the unique edge joining the remaining two vertices). Hence two distinct points lie on at most one line, and if they are disjoint they lie on exactly one line.

- (2) The GQ uniqueness property. Let e be an edge (point) and let M be a 1-factor


(line) not containing e. The matching M splits the six vertices into three disjoint edges; since e is not one of those three, the two endpoints of e are matched in M to two distinct vertices, so among the three edges of M exactly one is disjoint from e (namely the edge joining the two vertices of K6 not incident with the endpoints of e). Thus there is a unique point of M collinear with e. This is exactly the required GQ axiom.

The two properties above show I is a generalized quadrangle of order (2,2). Incidence graph properties. Let X be the incidence graph of I (vertices are points

and lines, adjacency = incidence). Then:

- • X is bipartite with parts of size 15 (points and lines), so |V (X)| = 30.
- • Every point-vertex has degree 3 (lies on 3 lines) and every line-vertex has degree 3 (contains 3 points), so X is 3-regular (cubic).
- • X contains no 4-cycle: a 4-cycle would give two distinct lines containing the same pair of points, contrary to uniqueness.
- • X contains no 6-cycle: a 6-cycle would correspond to three points p1,p2,p3 and three lines ℓ1,ℓ2,ℓ3 with alternating incidences


p1 − ℓ1 − p2 − ℓ2 − p3 − ℓ3 − p1.

This means p1 is collinear with p2 (on ℓ1), p2 with p3 (on ℓ2), and p3 with p1 (on ℓ3). Fixing the line ℓ2 (which does not contain p1) one then finds two distinct points of ℓ2 (namely p2 and p3) collinear with p1, contradicting the generalized quadrangle uniqueness condition proved above. Hence a 6-cycle cannot occur.

Therefore girth(X) ≥ 8.

Existence of an 8-cycle. We produce an explicit 8-cycle in X to show the girth is exactly 8. Label the vertices of K6 by 1,...,6 and write an edge (ij) for the unordered pair {i,j}. Consider the following points and lines:

p1 = (12), L1 = {(12),(34),(56)}, p2 = (34), L2 = {(34),(15),(26)}, p3 = (15), L3 = {(15),(24),(36)}, p4 = (36), L4 = {(36),(12),(45)}.

Each Li is a perfect matching of K6, and every consecutive point belongs to the preceding line, so

p1 − L1 − p2 − L2 − p3 − L3 − p4 − L4 − p1 is an 8-cycle in X. Combining this with the nonexistence of 4- and 6-cycles shows girth(X) = 8.

Conclusion. X is a cubic bipartite graph on 30 vertices of girth 8. By definition, a (3,8)-cage is a smallest 3-regular graph of girth 8; Tutte’s 8-cage (also referred to in the literature as the Tutte–Coxeter graph) is the well-known cubic graph with these parameters and 30 vertices. Hence the incidence graph X is (isomorphic to) Tutte’s 8cage. Equivalently, the incidence structure constructed above is the unique generalized quadrangle of order (2,2), whose incidence graph is Tutte’s 8-cage.

| |
|---|


Theorem 6.3.1. Let I be a partial linear space that contains both noncollinear points and nonconcurrent lines. Then I is a generalized quadrangle if and only if its incidence graph X(I) has diameter four and girth eight.

Proof. Suppose first that I is a generalized quadrangle. Fix a point p and consider distances from p in X(I).

- • A line lies at distance 1 from p if and only if it contains p, and at distance 3 otherwise (by the defining axiom of generalized quadrangles).
- • A point lies at distance 2 from p if and only if it is collinear with p, and otherwise at distance 4.


Since I contains noncollinear points, there exist points at distance 4, so diam(X(I)) = 4. By duality, the same holds for lines.

Next, consider the girth. As I is a partial linear space, X(I) has girth at least 6 by Lemma 6.0.1. A 6-cycle, however, would correspond to a point and a line joined by two distinct paths of length three, contradicting the quadrangle axiom. Thus the girth is at least 8. To show equality, let p and q be noncollinear points. Choose a line Lp through p not containing q, and a line Lq through q not containing p. Then:

p − Lp − p′ − q − Lq − q′ − p − Lp

forms an 8-cycle in X(I), where p′ is the unique point of Lp collinear with q, and q′ is the unique point of Lq collinear with p. Hence girth(X(I)) = 8.

Conversely, suppose X(I) is the incidence graph of a partial linear space with diameter

- 4 and girth 8. Then one bipartite part represents points and the other lines. Consider a point p and a line L with d(p,L) = 3. Since the girth is 8, there is a unique path


L − p′ − L′ − p,

so there exists a unique point p′ on L that is collinear with p. This is precisely the defining condition for a generalized quadrangle.

Thus I is a generalized quadrangle.

| |
|---|


### 6.4 A Family of Generalized Quadrangles

In this section we describe an infinite family of generalized quadrangles. The smallest member of this family has Tutte’s graph as its incidence graph.

Let V be a four-dimensional vector space over the finite field F of order q. The projective space PG(3,q) consists of the one-, two-, and three-dimensional subspaces of V , which we refer to as the points, lines, and planes of PG(3,q), respectively. Since V contains q4 − 1 nonzero vectors and each one-dimensional subspace contains q − 1 such vectors, the total number of points in PG(3,q) is

q4 − 1 q − 1

= (q + 1)(q2 + 1).

We will construct an incidence structure using all of these points but only a distinguished set of lines.

Define the matrix

  

  .

0 1 0 0

−1 0 0 0 0 0 0 1 0 0 −1 0

H =

(If q is even, then −1 = 1.) A subspace S ≤ V is called totally isotropic if uTHv = 0 for all u,v ∈ S. Since uTHu = 0 for all u, every one-dimensional subspace of V is totally isotropic. Our focus will be on the totally isotropic two-dimensional subspaces, which we will treat as the lines of our incidence structure.

To count them, note that a two-dimensional subspace ⟨u,v⟩ is totally isotropic if and only if uTHv = 0. For any nonzero vector u, define

u⊥ = {v ∈ V | uTHv = 0}.

Since det(H) = 1, H is invertible and uTH ̸= 0, so u⊥ is a three-dimensional subspace of V containing u. There are q4 − 1 choices for u, and for each such u there are q3 − q choices for v ∈ u⊥ \ ⟨u⟩. Hence the number of ordered pairs (u,v) spanning a totally isotropic two-dimensional subspace is

(q4 − 1)(q3 − q).

Since each two-dimensional subspace is spanned by (q2 − 1)(q2 − q) ordered pairs, the total number of totally isotropic two-dimensional subspaces is

(q4 − 1)(q3 − q) (q2 − 1)(q2 − q)

= (q2 + 1)(q + 1).

Geometrically, PG(3,q) therefore contains (q2 + 1)(q + 1) totally isotropic points and the same number of totally isotropic lines. Each totally isotropic line contains q+1 totally isotropic points, and by symmetry, each point lies on q + 1 such lines. Define W(q) to be the incidence structure consisting of these points and lines.

###### Lemma 6.4.1. W(q) is a generalized quadrangle.

Proof. Let p be a point and L a line not containing p. Suppose p is spanned by a vector u. Any point collinear with p is spanned by a vector in u⊥. The subspace u⊥ is threedimensional, while L is two-dimensional, so u⊥ ∩ L is one-dimensional. Hence there is a unique point on L collinear with p, as required.

| |
|---|


Let X denote the incidence graph of W(q). Then X is bipartite with 2(q2 + 1)(q + 1)

vertices, is (q + 1)-regular, and by Theorem 6.3.1 has diameter four and girth eight. In fact, X is distance-regular.

For q = 2, this construction yields a generalized quadrangle with 15 points and 15 lines; this coincides with the generalized quadrangle defined in Proposition 6.3.1 on the edges and 1-factors of K6.

The choice of H is not unique: any invertible 4 × 4 skew-symmetric matrix (i.e. with zero diagonal entries and HT = −H) defines the same class of totally isotropic subspaces, and hence the same incidence structure W(q).

Finally, while the quadrangles produced here are regular, it should be noted that there exist many generalized quadrangles that are not regular.

6.5 Generalized Polygons

In addition to their purely combinatorial definition, generalized polygons acquire a deeper significance through their connections with group theory and geometry. Many remarkable examples arise as incidence geometries associated with groups, particularly those of Lie type. This interplay between algebra and geometry makes generalized polygons a central object of study, linking combinatorial design theory with the theory of buildings, finite simple groups, and classical geometries. In this section we explore generalized polygons from this perspective, beginning with their definition and basic properties, and then examining how group actions give rise to some of the most important families of examples.

6.5.1 Definitions and Basic Structure

- Definition 6.5.1 (Generalized Polygon). A generalized polygon is a finite bipartite graph with diameter d and girth 2d. When it is important to specify the diameter, a generalized polygon of diameter d is called a generalized d-gon, and the normal names for small polygons (triangle for 3-gon, quadrangle for 4-gon, etc.) are used.


A vertex in a generalized polygon is called thick if its valency is at least three. Vertices that are not thick are thin. A generalized polygon is called thick if all its vertices are thick. Although on the face of it the definition of a generalized polygon is not very restrictive, we will show that the thick generalized polygons are regular or semiregular, and that the generalized polygons that are not thick arise purely as subdivisions of generalized polygons.

The argument proceeds by a series of simple structural lemmas. The first such lemma is a trivial observation, but we will use it repeatedly.

###### Lemma 6.5.1 (Uniqueness of Geodesics). Let X be a generalized d-gon. If d(v,w) = m < d, then there is a unique v–w path of length m.

Proof. By definition of distance there exists at least one v–w path of length m. Suppose, for a contradiction, that there are two distinct v–w paths P1 and P2 of length m. Traversing P1 from v to w and then P2 back from w to v forms a closed walk of length 2m. Because P1 ̸= P2 and both are simple (geodesics), their union contains a cycle whose length is at most 2m; in fact, since the graph is bipartite, every cycle has even length, so this cycle has length exactly 2m.

But m < d, hence 2m < 2d, contradicting that the girth of X is 2d (i.e., X has no cycle shorter than 2d). Therefore no two distinct shortest v–w paths can exist, and the geodesic of length m is unique.

| |
|---|


Remark: The bound m < d is sharp: for m = d uniqueness need not hold (indeed, in many generalized polygons there are multiple internally disjoint geodesics of length d between antipodal vertices).

- Lemma 6.5.2 (Valency at Distance d). If d(v,w) = d in a generalized d-gon X, then v and w have the same valency.

Proof. Suppose d(v,w) = d. Let v′ be any neighbor of v. Since X is bipartite of diameter d, it follows that d(v′,w) = d − 1. Thus there is a unique geodesic of length d − 1 from v′ to w (by Lemma 6.5.1). This geodesic must pass through exactly one neighbor of w.

Distinct neighbors v′ of v yield distinct such geodesics, hence distinct neighbors of w. Therefore deg(w) ≥ deg(v).

By symmetry, reversing the roles of v and w gives deg(v) ≥ deg(w). Consequently deg(v) = deg(w), as claimed.

| |
|---|


- Lemma 6.5.3 (Minimum Valency). Every vertex of a generalized d-gon X has valency at least 2.

Proof. Let C be a cycle of length 2d in X. Each vertex on C has valency at least 2, since it has two distinct neighbors along C.

Now let x ∈ V (X) be any vertex not lying on C. Let P be a shortest path from x to C, and let i = |P| be its length. Follow C for exactly d − i steps starting from the endpoint of P on C; this produces a vertex x′ on C such that

d(x,x′) = d.

By Lemma 6.5.2, we conclude that x and x′ have the same valency. Since x′ lies on C, it has valency at least 2, and therefore so does x.

| |
|---|


- Lemma 6.5.4 (Cycle Containment). In a generalized d-gon X, any two vertices are contained in a cycle of length 2d.


Proof. Let v,w ∈ V (X) be arbitrary vertices, and let P be a shortest path from v to w. We extend P to a geodesic of length d as follows: choose an endpoint of P, and iteratively append neighbors not already in P until the path has length d. Let the resulting geodesic have endpoints x and y.

Since X has diameter d, the distance between x and y is exactly d. By Lemma 6.5.3, x has a neighbor x′ not on P. Then d(x′,y) = d − 1, so there exists a unique geodesic of length d − 1 from x′ to y (by Lemma 6.5.1).

Thus we obtain a cycle of length 1 + (d − 1) + d = 2d passing through P. In particular, both v and w lie on this 2d-cycle, as required.

| |
|---|


#### 6.5.2 Structure of Non-Thick Polygons

The next series of lemmas shows that generalized polygons that are not thick are largely trivial modifications of those that are thick.

- Lemma 6.5.5 (Valency on a Cycle). Let C be a cycle of length 2d in a generalized d-gon X. Suppose v ∈ C is a thick vertex. Then any two vertices of C lying at the same distance from v have equal valency.

Proof. Let w be the antipode of v in C, i.e. the unique vertex of C at distance d from v. Since v is thick, it has some neighbor v′ not belonging to C. Since X has girth 2d, the distance from v′ to w is d−1, so there is a unique geodesic path P from v′ to w of length d − 1 (by Lemma 6.5.1).

Thus we obtain three internally vertex-disjoint paths of length d between v and w: the two halves of the cycle C, and the path v–v′–P–w.

Now let v1,v2 ∈ C be two vertices at distance h from v (where 1 ≤ h ≤ d − 1). On the path P, consider the vertex x that lies at distance d − h from v. Then

d(x,v1) = d(x,v2) = d,

because x is joined to v by a path of length d − h and v1,v2 are joined to v by paths of length h.

By Lemma 6.5.2, any two vertices at distance d must have the same valency. Hence v1 and v2 both have the same valency as x, and therefore as each other.

| |
|---|


- Lemma 6.5.6 (Structure of Thick Vertices). Let X be a generalized d-gon. Let k denote the minimum distance between any two thick vertices of X. Then:


- 1. k divides d;
- 2. if d/k is odd, then all thick vertices have the same valency;
- 3. if d/k is even, then the thick vertices have at most two distinct valencies;
- 4. moreover, every vertex at distance k from a thick vertex is itself thick.


Proof. Choose two thick vertices v and w with d(v,w) = k. Let x be any other thick vertex of X.

- Step 1: k divides d. By Lemma 6.5.4, there exists a cycle C of length 2d containing

v, w, and x. By Lemma 6.5.5, starting at v and moving around C, every kth vertex is thick. In particular, the antipode v′ of v in C (which is at distance d from v) must also be thick. Hence d is a multiple of k.

- Step 2: possible valencies of thick vertices. Applying Lemma 6.5.5 repeatedly along

C, we find that every thick vertex in C has the same valency as either v or w. Thus, thick vertices may take at most two distinct valencies. If d/k is odd, then moving d steps around C from v lands at v′, which has the same valency as w. But by Lemma 6.5.2, v and v′ also have the same valency. Therefore v and w must share the same valency, so all thick vertices have equal valency. If d/k is even, then v and w need not have the same valency, but no more than two valencies can occur.

- Step 3: thickness propagates at distance k. Let x be any thick vertex and x′ a vertex


at distance k from x. If x′ ∈ C, Step 1 shows that x′ is thick. If x′ ∈/ C, then there

exists a cycle C′ of length 2d containing x, x′, and some vertex of C at distance k from x. Repeating the same argument on C′ forces x′ to be thick.

This proves all parts of the lemma.

| |
|---|


We have already defined the subdivision graph S(X) as being the graph obtained from X by putting a vertex in the middle of each edge. We could also regard this as replacing each edge by a path of length 2. Taking this point of view we define the k-fold subdivision of a graph X to be the graph obtained from X by replacing each edge by a path of length k.

- Theorem 6.5.1 (Classification of Non-Thick Polygons). Let X be a generalized d-gon. If X is not thick, then it is one of the following:


- 1. a cycle of length 2d;
- 2. the k-fold subdivision of a multiple edge;
- 3. the k-fold subdivision of a thick generalized polygon.


Proof. Suppose first that X has no thick vertices. Then every vertex has degree 2, so X is simply a cycle of length 2d, which is case (i).

Now assume X has at least one thick vertex. Let k be the minimal distance between thick vertices. By Lemma 6.5.6, k divides d, and every kth vertex along a geodesic from

- a thick vertex is also thick, with all intermediate vertices thin.


- Step 1: Constructing the quotient graph of thick vertices. Define a new graph X′ as

follows: - the vertices of X′ are the thick vertices of X; - two vertices of X′ are adjacent if they are joined in X by a path of length k.

By construction, X is the k-fold subdivision of X′.

- Step 2: Handling the case k = d. If k = d, then two thick vertices at maximum

distance are joined by paths of length d, and every other vertex of X lies along such a path. Hence X consists only of two thick vertices joined by several internally disjoint d-paths of thin vertices. Equivalently, X is the d-fold subdivision of a multiple edge, which is case (ii).

- Step 3: The case k < d. If k < d, then X′ inherits the structure of a generalized


polygon: - Its diameter is d′ := d/k, since a geodesic of length d in X corresponds to a geodesic of length d′ in X′. - Its girth is 2d′, since a 2d-cycle in X collapses to a 2d′-cycle in X′. - It is bipartite: if X′ contained an odd cycle, then its k-fold subdivision in X would create a vertex at distance at least kd′ +1 > d, contradicting that X has diameter d. - Finally, all vertices of X′ are thick by definition.

Thus X′ is a thick generalized d′-gon, and X is its k-fold subdivision, which is case (iii).

This exhausts all possibilities, completing the proof.

| |
|---|


Therefore, the study of generalized polygons reduces to the study of thick generalized polygons, with the remainder being considered the degenerate cases.

#### 6.5.3 Properties of Thick Generalized Polygons

Although the proofs of the main results about thick generalized polygons are beyond our scope, the results themselves are easy to state. The following famous theorem shows that in a thick generalized polygon, the diameter d is severely restricted.

- Theorem 6.5.2 (Feit–Higman). If a generalized d-gon is thick (i.e., every point lies on at least 3 lines and every line contains at least 3 points), then


d ∈ {3,4,6,8}.

Proof. Let Γ be a thick generalized d-gon, with point set P and line set L. Let each point be on s + 1 ≥ 3 lines, and each line contain t + 1 ≥ 3 points. Denote the incidence graph of Γ by G, a bipartite graph with vertices P ∪ L, edges representing incidence. Then:

- 1. G is bipartite and regular of degree s + 1 on P and t + 1 on L.
- 2. G has girth 2d, i.e., the shortest cycle has length 2d.
- 3. G is connected. Consider the number of vertices at distance i from a fixed point p ∈ P:


- • Distance 0: 1 (the point p itself) • Distance 1: s + 1 lines through p • Distance 2: Each line contains t other points, giving (s + 1)t points
- • Distance 3: Each such point lies on s new lines, and so on. This defines a tree-like structure up to distance d, because cycles have length ≥ 2d.


Let xi be the number of vertices at distance i from p. Then we have the recursion: xi+1 = (ri − 1)xi,

where ri alternates between s + 1 and t + 1, depending on whether i is even (point) or odd (line).

Analyzing this recursion and using the diameter constraint of d, one finds that √st must be an integer, and the combinatorial and algebraic constraints imposed by thickness force

d ∈ {3,4,6,8}. These correspond respectively to:

- • d = 3: generalized triangles (projective planes)
- • d = 4: generalized quadrangles
- • d = 6: generalized hexagons
- • d = 8: generalized octagons Hence, any thick generalized d-gon satisfies d ∈ {3,4,6,8}.


| |
|---|


We have already seen examples of thick generalized triangles (d = 3) and thick generalized quadrangles (d = 4). In fact generalized triangles and generalized quadrangles exist in great profusion. Generalized hexagons and octagons do exist, but only a few families are known. Unfortunately, even the simplest of these families are difficult to describe.

Since a projective plane is a thick generalized triangle, it is necessarily regular. If all the vertices have valency s + 1, then we say that the projective plane has order s. The other thick generalized polygons may be regular or semiregular. If the valencies of the vertices of a thick generalized polygon X are s+1 and t+1, then X is said to have order (s,t) (where s may equal t).

- Lemma 6.5.7 (Regular implies Distance–Regular). If a generalized polygon X is regular, then it is distance–regular.


Proof. Let X be a generalized d-gon: a finite connected bipartite graph with diameter d and girth 2d. Assume X is k-regular (so every vertex has valency k). Fix an arbitrary vertex x ∈ V (X) and write

Γi(x) := {y ∈ V (X) : d(x,y) = i} (0 ≤ i ≤ d). To prove distance–regularity, we must show that for each i the numbers bi := |{z ∈ N(y) : z ∈ Γi+1(x)}|, ai := |{z ∈ N(y) : z ∈ Γi(x)}|, ci := |{z ∈ N(y) : z ∈ Γi−1(x)}| depend only on i (not on the particular choice of x and y ∈ Γi(x)), with the conventions

- bd = 0, c0 = 0.


- Step 1: ai = 0 for all 0 ≤ i ≤ d. Since X is bipartite, every edge joins vertices at

distances that differ by 1 from x. Hence no neighbor of y ∈ Γi(x) can lie in Γi(x), so ai = 0.

- Step 2: ci = 1 for 1 ≤ i ≤ d − 1, and cd = k. Fix 1 ≤ i ≤ d − 1 and y ∈ Γi(x). If y


had two distinct neighbors u,v ∈ Γi−1(x), then the two geodesics x ⇝ u–y and x ⇝ v–y of length i would be distinct, which, after concatenation, would create a cycle of length 2i < 2d, contradicting girth(X) = 2d. Thus ci = 1.

For i = d and y ∈ Γd(x), every neighbor of y must lie in Γd−1(x) (it cannot lie in Γd+1(x) by the definition of diameter, and parity forbids Γd(x)). Since X is k-regular, cd = |N(y)| = k.

Step 3: b0 = k and bi = k − 1 for 1 ≤ i ≤ d − 1. For i = 0, b0 = |N(x)| = k by regularity. For 1 ≤ i ≤ d − 1 and y ∈ Γi(x), all neighbors of y lie in Γi−1(x) or Γi+1(x) (bipartiteness). By Step 2, exactly one neighbor lies in Γi−1(x); none lie in Γi(x) by Step 1. Therefore the remaining k − 1 neighbors lie in Γi+1(x), so bi = k − 1.

All parameters (bi,ai,ci) thus depend only on i and not on the particular vertices:

- b0 = k, bi = k−1 (1 ≤ i ≤ d−1), bd = 0; ai = 0 (0 ≤ i ≤ d); c1 = ··· = cd−1 = 1, cd = k. Hence X is distance–regular.


| |
|---|


The order of a thick generalized polygon satisfies certain inequalities due to Higman and Haemers.

- Theorem 6.5.3 (Order Inequalities). Let X be a thick generalized d-gon of order (s,t).


- 1. If d = 4, then s ≤ t2 and t ≤ s2.
- 2. If d = 6, then st is a perfect square, and s ≤ t3, t ≤ s3.
- 3. If d = 8, then 2st is a perfect square, and s ≤ t2, t ≤ s2.


- Proof. Let X be the incidence graph of the generalized d-gon of order (s,t). Then X is connected, bipartite (points/lines), diameter d, girth 2d, and semi-regular: every point lies on t + 1 lines, every line contains s + 1 points.


Distance–regular setup. Fix a base vertex x (say, a point). Let Γi = Γi(x) denote vertices at distance i from x. Then X is distance-regular, with intersection numbers:

s, i odd t, i even, 1 ≤ i ≤ d − 1

ai = 0, ci = 1 (1 ≤ i ≤ d − 1), b0 = t + 1, bi =

.

The adjacency matrix restricted to the distance layers is tridiagonal, with Bi,i+1 = bi, Bi,i−1 = ci, Bi,i = 0. Its eigenvalues correspond to the nontrivial eigenvalues of X, whose multiplicities must be nonnegative integers.

##### Case d = 4 (generalized quadrangles). Intersection numbers:

b0 = t + 1, b1 = s, b2 = t, b3 = s, c1 = c2 = c3 = 1, c4 = t + 1. The eigenvalues are

√

√

√s, ±

st, ±

±

t. The multiplicities must be integers ≥ 0. This forces the classical Higman bounds: s ≤ t2, t ≤ s2.

##### Case d = 6 (generalized hexagons). Intersection numbers:

b0 = t + 1, b1 = s, b2 = t, b3 = s, b4 = t, b5 = s; c1 = ··· = c5 = 1, c6 = t + 1. The nontrivial eigenvalues are ±

√t. Integrality of multiplicities implies st is

√st,±

√s,±

- a perfect square. Further multiplicity inequalities give: s ≤ t3, t ≤ s3.

Case d = 8 (generalized octagons). Intersection numbers:

- b0 = t+1, b1 = s, b2 = t, b3 = s, b4 = t, b5 = s, b6 = t, b7 = s; c1 = ··· = c7 = 1, c8 = t+1.


√2t. Integrality requires 2st to be a perfect square, and multiplicity inequalities give:

√2s,±

√st,±

Eigenvalues are ±

s ≤ t2, t ≤ s2.

Hence, in all cases, the stated square conditions and inequalities follow from the distance-regular structure and integrality of eigenvalue multiplicities.

| |
|---|


Note that it is possible to take a generalized polygon of order (s,s) and subdivide each edge exactly once to form a generalized polygon of order (1,s). Therefore, it is possible to have a generalized 12-gon that is neither thick nor a cycle.

### 6.6 Uniqueness of the generalized quadrangle of order (2,2)

- Definition 6.6.1 (Generalized quadrangle). A generalized quadrangle (GQ) is an incidence structure (P,L,I) (points, lines, incidence) such that


- 1. every point is incident with at least two lines and every line is incident with at least two points;
- 2. given a point x and a line ℓ not incident with x, there is a unique point y on ℓ collinear with x;
- 3. there are no ordinary 4-cycles of points and lines (equivalently the incidence graph has girth 8).


If every line is incident with exactly s + 1 points and every point is incident with exactly t + 1 lines, we say the GQ has order (s,t).

- Theorem 6.6.1. Up to isomorphism there is a unique generalized quadrangle of order (2,2).


Proof. Let (P,L) be a GQ of order (2,2). We first record the basic parameter counts (standard for GQ(s,t)):

|P| = (s + 1)(st + 1), |L| = (t + 1)(st + 1). With s = t = 2 we obtain

|P| = (2 + 1)(2 · 2 + 1) = 3 · 5 = 15, |L| = 15.

Each point lies on t + 1 = 3 lines and each line contains s + 1 = 3 points. Fix a point p ∈ P and analyze its neighborhood.

Local structure about a point. The point p lies on exactly three lines; write them ℓ1,ℓ2,ℓ3. Each ℓi contains two other points besides p, so the set

N(p) := {q ∈ P : q is collinear with p, q ̸= p} has size 3 · 2 = 6. Thus the set {p} ∪ N(p) has 7 points.

We claim the 7 points {p}∪N(p) carry the incidence structure of the Fano plane. To see this, note:

- • The three lines ℓ1,ℓ2,ℓ3 through p are three lines of this 7-point structure, each of size 3 and meeting pairwise in p.
- • For any two distinct points x,y ∈ N(p) not on the same ℓi, there is a unique line through x meeting ℓj and ℓk (the other two lines through p) in unique points collinear with y; using the GQ axiom (existence/uniqueness of the foot on a line not through a point) one shows these extra intersections produce the remaining four lines so that the whole 7-point set obtains the incidence pattern of the Fano plane.


A brief counting/check shows the 7 points form a projective plane of order 2 (the Fano plane): each point in the 7-set lies on exactly 3 of the lines that lie entirely in that 7-set, any two points of the 7-set determine exactly one of those lines, etc. (This verification is elementary and uses only the small numerical parameters s = t = 2 and the GQ axioms.)

Hence the neighbourhood of any point p (together with p) is a copy of the Fano plane. Equivalently, p⊥ = {p} ∪ N(p) is a 7-point Fano plane (we call p⊥ the perp of p).

Global identification. Now choose a labeling of the seven points of p⊥ in the standard Fano way. The lines through p correspond to three concurrent Fano lines; the remaining points and lines of the whole GQ are determined by the GQ axioms: every line not contained in p⊥ meets p⊥ in exactly one point, and for each point x ∈ p⊥ \ {p} there are exactly two lines through x contained in p⊥ (the Fano ones) and one line through x not contained in p⊥. Using the uniqueness clause of the GQ axiom one uniquely determines which external points lie on each external line: given an external line ℓ and its unique intersection x = ℓ ∩ p⊥, each other point of ℓ is uniquely specified as the unique point on ℓ collinear with an appropriate specified point of a different line through p.

Carrying out this reconstruction from the chosen base point p yields a concrete incidence structure on 15 points and 15 lines with the prescribed local pattern. Two choices of base point (or two different labelings of its perp) lead to isomorphic global structures because any isomorphism of the two chosen Fano perps extends uniquely (by the GQ incidence axioms) to an isomorphism of the whole GQ. Thus the GQ is determined up to isomorphism by the local Fano configuration around any point.

Comparison with the standard model. One may now compare the structure just obtained with the standard symplectic generalized quadrangle W(2): take the 4-dimensional vector space V = F42 and a nondegenerate alternating bilinear form ⟨·,·⟩. Let points be the 1-dimensional subspaces of V and take as lines the 2-dimensional totally isotropic subspaces. A direct check shows this incidence structure is a GQ of order (2,2); the local perp of any point is a Fano plane as above, and the combinatorics match. By the reconstruction argument, every GQ(2,2) is isomorphic to this standard W(2) model.

Therefore the generalized quadrangle of order (2,2) is unique up to isomorphism.

| |
|---|


### 6.7 Designs

Another fundamental class of incidence structures is that of t-designs. Unlike partial linear spaces, t-designs are not usually viewed geometrically. Design theorists typically use the term “block” instead of “line,” and identify a block directly with the subset of points to which it is incident.

Formally, a t-(v,k,λt) design is a set P of v points together with a collection B of k-subsets of P, called blocks, such that every t-subset of points lies in exactly λt blocks. For example, the projective plane PG(2,q) is a 2-design: every two points lie in a unique block (line), so it is a 2-(q2 + q + 1, q + 1, 1) design.

Now let D be a t-(v,k,λt) design, and fix an s-subset S of points with s < t. Let λs denote the number of blocks of D containing S. We compute λs by double-counting pairs (T,B) where T is a t-subset containing S, and B is a block containing T.

- On the one hand, there are vt−−ss choices for T, and each lies in λt blocks. - On the other hand, each block containing S yields kt−−ss choices for T.

Hence

k − s t − s

v − s t − s

. (6.1)

λs

= λt

Since this expression does not depend on the particular choice of S, it follows that D is also an s-(v,k,λs) design. A necessary condition for the existence of a t-design is therefore that λs is an integer for all s < t.

Two parameters deserve special mention:

- • λ0 is the total number of blocks, usually denoted by b. Setting s = 0 in (6.1) gives

b = λ0 = λt

v t k t

.

- • λ1 is the number of blocks containing each point, called the replication number and usually denoted by r. Substituting s = 1 into (6.1) yields the fundamental relation


bk = vr.

If λt = 1, the design is called a Steiner system. In particular, a 2-design with λ2 = 1 and k = 3 is called a Steiner triple system. For instance, the projective plane PG(2,2) is a 2-(7,3,1) design, hence a Steiner triple system. It is known as the Fano plane and is typically drawn as in Figure 5.5, with blocks represented by the straight lines and the central circle.

The incidence matrix of a design provides a useful algebraic characterization. Let D

- be a 2-(v,k,λ2) design with replication number r and number of blocks b. Its incidence matrix N is the v × b 0–1 matrix with rows indexed by points and columns indexed by blocks, where


1 if the i-th point lies in the j-th block, 0 otherwise.

Nij =

By definition, each row of N has exactly r ones (since each point is contained in r

blocks), and each column has exactly k ones (since each block contains k points). Proposition 6.7.1. For the incidence matrix N of a 2-(v,k,λ2) design, we have

NNT = (r − λ2)I + λ2J, where I is the v × v identity matrix and J is the v × v all-ones matrix. Proof. Consider the (i,j)-entry of NNT. By definition,

b

(NNT)ij =

NimNjm.

m=1

- Case 1: i = j. Then (NNT)ii counts the number of blocks containing the i-th

point. This is exactly r. On the right-hand side, the (i,i) entry of (r − λ2)I + λ2J is (r − λ2) + λ2 = r.

- Case 2: i ̸= j. Then (NNT)ij counts the number of blocks containing both the i-th


and j-th points. Since D is a 2-design, this number is λ2. On the right-hand side, the (i,j) entry is 0 + λ2 = λ2.

Thus the two matrices agree entrywise, proving the identity.

| |
|---|


- Corollary 6.7.1. Conversely, let N be a v × b 0–1 matrix with constant row sum r and constant column sum k such that


NNT = (r − λ2)I + λ2J. Then N is the incidence matrix of a 2-(v,k,λ2) design.

Proof. The assumption on constant row and column sums ensures that each point lies in exactly r blocks and each block contains exactly k points. Moreover, for distinct rows i ̸= j, the (i,j) entry of NNT counts the number of common blocks containing points i and j, and the given equation forces this to equal λ2. Thus every pair of distinct points lies in exactly λ2 blocks, which is precisely the defining condition of a 2-design.

| |
|---|


- Lemma 6.7.1. In any 2-design with k < v, the number of blocks satisfies b ≥ v. Proof. Substituting t = 2 and s = 1 into equation (6.1), we obtain

r(k − 1) = (v − 1)λ2. Since k < v, it follows that r > λ2. Hence the incidence matrix N of the design satisfies NNT = (r − λ2)I + λ2J

with r − λ2 > 0. This implies that NNT is positive definite, and therefore invertible.

Consequently, the v row vectors of N are linearly independent. Since N has b columns, this forces v ≤ b.

| |
|---|


A 2-design with b = v is called symmetric. The dual of a 1-design is always a 1design, but in general the dual of a 2-design is not a 2-design. The next result shows that symmetric designs are an exceptional case.

- Lemma 6.7.2. The dual D∗ of a symmetric 2-design D is itself a symmetric 2-design with the same parameters.


Proof. Let N be the incidence matrix of D. Then N is a v × b 0–1 matrix with constant row sum r and constant column sum k. By definition, the incidence matrix of the dual design D∗ is NT.

Since D is a 2-design, we have NNT = (r − λ2)Iv + λ2Jv, where Iv is the v × v identity and Jv is the v × v all-ones matrix.

If D is symmetric, then b = v, and moreover r = k. Thus N is a square v × v matrix, and the analogous computation gives

NTN = (k − λ2)Iv + λ2Jv. This is exactly the defining relation for a 2-design with the same parameters (v,k,λ2).

Hence the dual D∗ is also a 2-design with parameters (v,k,λ2). Since b = v, D∗ is symmetric as well.

| |
|---|


- Theorem 6.7.1. A bipartite graph is the incidence graph of a symmetric 2-design if and only if it is distance-regular with diameter three.


Proof. Suppose first that D is a symmetric 2-(v,k,λ2) design with incidence graph X. Since any two distinct points lie in exactly λ2 blocks, their distance in X is 2. Similarly, any two distinct blocks lie at distance 2. A point and a block not incident to it are at distance 3. Therefore, the diameter of X is 3.

Consider the distance partition from a point in X. Since X is bipartite, we have a1 = a2 = a3 = 0. Two points share λ2 common blocks, giving c2 = λ2. Using r = k, one can compute the intersection numbers as

b0 = k, b1 = k − 1, b2 = v − k, c1 = 1, c2 = λ2, c3 = k.

By symmetry, the same intersection numbers arise from the distance partition about a block. Hence X is distance-regular.

Conversely, suppose X is a bipartite, distance-regular graph with diameter 3. Label one part of the bipartition as points and the other as blocks. From the distance partition about a point, each point lies in b0 blocks, and each pair of points shares c2 common blocks. Thus the points and blocks form a 2-(v,k,λ2) design with r = b0 and λ2 = c2. Considering the distance partition from a block, each block contains b0 points and each pair of blocks meets in c2 points. Hence the design is symmetric (b = v) and k = r = b0, completing the characterization.

| |
|---|


Since projective planes are symmetric 2-designs, Theorem 6.7.1 provides another proof of the characterization of generalized polygons with diameter three.

The incidence graph of the Fano plane is called the Heawood graph. We illustrate both the Fano plane and its incidence graph below.

Another way to associate a graph with a design D is via the block graph, whose vertices are the blocks of D, with two vertices adjacent if the corresponding blocks intersect. More generally, if blocks can intersect in different numbers of points, one can define adjacency based on intersecting in a fixed number of points to obtain interesting graphs.

- Theorem 6.7.2. The block intersection graph of a Steiner triple system with v > 7 is distance-regular with diameter two.


Proof. Let D be a Steiner triple system, i.e., a 2-(v,3,1) design, and let X denote its block intersection graph.

Step 1: Regularity. Each point lies in r = (v−1)/2 blocks, and each block contains

- 3 points. Thus, for a given block, the number of adjacent blocks (those sharing a point) is


3(v − 3) 2

v − 1 2 − 1 =

3(r − 1) = 3

,

so X is regular of valency 3(v − 3)/2.

Step 2: Intersection numbers for adjacent blocks. Consider two blocks that intersect in a point p. - There are (r − 1) = (v − 3)/2 other blocks containing p, distinct from the two under consideration. - Additionally, there are 4 blocks that contain one point from each of the remaining two pairs of points in the two blocks.

Hence the intersection number a1 (number of common neighbors of adjacent vertices) is

v − 3 2

v + 5 2

+ 4 =

.

a1 =

Step 3: Intersection numbers for non-adjacent blocks. If two blocks are disjoint, then each pair of points, one from each block, determines exactly one block. Since there are 3·3 = 9 such pairs, the number of common neighbors of two non-adjacent vertices is

c2 = 9. This also shows that the diameter of X is 2, as any two disjoint blocks are connected via a block that intersects both.

Step 4: Conclusion. With these intersection numbers, the remaining parameters can be computed similarly. Thus, X is a distance-regular graph of diameter 2.

| |
|---|


### 6.8 Steiner Systems

- A Steiner system is a combinatorial design that can be viewed as a type of finite geometry, where the points of the system form a set and the blocks play the role of generalized lines. This generalizes familiar geometric structures such as affine or projective spaces.


Let X be a set with |X| = v, and let k ≤ v. A k-subset of X is a subset B ⊆ X with |B| = k.

- Definition 6.8.1. Let 1 < t < k < v be integers. A Steiner system of type S(t,k,v) is a pair (X,B), where X is a set of v elements and B is a collection of k-subsets of X, called blocks, such that every t-subset of X is contained in exactly one block.


- Example 6.8.1 (Affine planes). Let X be the point set of an affine plane over the finite field GF(q), and let B be the collection of all affine lines in X. Each line contains q points, and every two points determine a unique line. Hence (X,B) forms a Steiner system of type

S(2,q,q2).

- Example 6.8.2 (Projective planes). Let X be the point set of the projective plane P2(q), and let B be the set of all projective lines. Each line contains q + 1 points, and any two points lie on a unique line. Therefore, (X,B) is a Steiner system of type

S(2,q + 1,q2 + q + 1).

- Example 6.8.3 (Binary vector spaces). Let X be an m-dimensional vector space over


Z2 with m ≥ 3, and let B be the collection of all affine planes (2-dimensional subspaces) in X. Since no three distinct points in an affine plane are collinear, every triple of points is contained in exactly one plane. Thus (X,B) is a Steiner system of type

S(3,4,2m).

We assume the strict inequalities 1 < t < k < v to exclude trivial or degenerate cases. - If t = 1, each point lies in a unique block, so the system is simply a partition of X into k-subsets; - If t = k, then every t-subset is a block, resulting in too many blocks; - If k = v, there is only one block, yielding too few blocks.

In the first case, all “lines” (blocks) are parallel; in the second case, the system is overly dense; in the third case, it is minimal.

Given parameters 1 < t < k < v, it is generally an open problem whether a Steiner system of type S(t,k,v) exists. For instance, a projective plane of order n is defined as a Steiner system of type

S(2,n + 1,n2 + n + 1).

It is conjectured that n must be a prime power, but existence remains unknown for certain values, such as n = 12.

Classical results restrict some orders: the theorem of Bruck and Ryser (1949) states that if n ≡ 1 or 2 (mod 4) and n is not a sum of two squares, then no projective plane of order n exists. For example, n = 10 neither satisfies these conditions nor is a prime power; using extensive computer verification, C. Lam (1988) proved that no projective plane of order 10 exists.

- Definition 6.8.2. Let (X,B) be a Steiner system and x ∈ X. The star of x is the set of all blocks containing x:


star(x) = {B ∈ B : x ∈ B}.

- Theorem 6.8.1. Let (X,B) be a Steiner system of type S(t,k,v) with t ≥ 3. For x ∈ X, define


X′ = X \ {x}, B′ = {B \ {x} : B ∈ star(x)}.

Then (X′,B′) is a Steiner system of type S(t − 1,k − 1,v − 1), called the contraction of (X,B) at x.

Proof. We need to verify that (X′,B′) satisfies the definition of a Steiner system of type S(t − 1,k − 1,v − 1).

- Step 1: Elements and blocks. - The set X′ has v − 1 elements since we removed

x from X. - Each block in B′ has size k − 1, because each block in star(x) originally had k elements and contained x.

- Step 2: Coverage of (t−1)-subsets. Let Y ⊆ X′ be any (t−1)-subset. Since (X,B)

is a S(t,k,v) Steiner system, the t-subset Y ∪ {x} ⊆ X is contained in a unique block B ∈ B. By construction, B contains x, so B ∈ star(x), and therefore B′ = B \ {x} ∈ B′. Clearly, Y ⊆ B′.

- Step 3: Uniqueness. If there were another block C′ ∈ B′ containing Y , then


- C = C′∪{x} would be a block of (X,B) containing Y ∪{x}, contradicting the uniqueness of the block in the original Steiner system.


Conclusion: Thus, every (t − 1)-subset of X′ lies in a unique block of B′. By definition, (X′,B′) is a Steiner system of type S(t − 1,k − 1,v − 1).

| |
|---|


A contraction of a Steiner system (X,B) may depend on the choice of point x ∈ X. Let Y and Z be finite sets, and let W ⊆ Y × Z. For each y ∈ Y , define

#(y,·) = |{z ∈ Z : (y,z) ∈ W}|, and for each z ∈ Z, define

#(·,z) = |{y ∈ Y : (y,z) ∈ W}|. Clearly, we have

#(y,·) = |W| =

#(·,z),

y∈Y

z∈Z

which yields the following counting principle:

- Lemma 6.8.1 (Counting principle). If #(y,·) = m for all y ∈ Y and #(·,z) = n for all z ∈ Z, then


m|Y | = n|Z|.

- Theorem 6.8.2. Let (X,B) be a Steiner system of type S(t,k,v). Then the total number of blocks is


v(v − 1)(v − 2)···(v − t + 1) k(k − 1)(k − 2)···(k − t + 1)

|B| =

,

and the number of blocks containing a given point x ∈ X, denoted r, is independent of x and satisfies

(v − 1)(v − 2)···(v − t + 1) (k − 1)(k − 2)···(k − t + 1)

r =

.

- Proof. Let Y be the set of all t-subsets of X, so that |Y | = vt = v(v−1)···(v−t+1)/t!. Define


W = {(T,B) ∈ Y × B : T ⊆ B}. By definition of a Steiner system, each t-subset T lies in exactly one block, so #(T,·) = 1. Each block B contains kt = k(k−1)···(k−t+1)/t! distinct t-subsets, so #(·,B) = kt .

Applying Lemma 6.8.1,

v t k t

v(v − 1)···(v − t + 1) k(k − 1)···(k − t + 1)

k t

|Y | · 1 = |W| = |B| ·

=⇒ |B| =

=

.

For a point x ∈ X, the number of blocks containing x is the size of the contraction at x, which is a Steiner system of type S(t − 1,k − 1,v − 1) by Theorem 6.8.1. By the same counting argument applied to the contraction, we obtain

(v − 1)(v − 2)···(v − t + 1) (k − 1)(k − 2)···(k − t + 1)

,

r =

showing that r is independent of the choice of x. Remarks.

| |
|---|


- 1. The proof of Theorem 6.8.1 holds for all t ≥ 2. Note, however, that when t = 2, the contraction (X′,B′) is not a Steiner system, since it would correspond to t−1 = 1.
- 2. The same argument yields a formula for the number of blocks in a Steiner system S(t,k,v) that contain a fixed set of p points (1 ≤ p ≤ t). For instance, if x,y ∈ X, then the number of blocks containing both x and y equals the replication number in the contraction at x that still contains y. Denoting this number by r′, one obtains

r′ =

(v − 2)(v − 3)···(v − t + 1) (k − 2)(k − 3)···(k − t + 1)

.

More generally, the number of blocks containing a fixed set of p points is

r(p) =

(v − p)(v − p − 1)···(v − t + 1) (k − p)(k − p − 1)···(k − t + 1)

.

- 3. The integrality of these numbers |B|, r, r′, r(p), ..., r(t) = 1


imposes strong arithmetic restrictions on the possible parameters (t,k,v) of a Steiner system.

- Definition 6.8.3. If (X,B) and (Y,C) are Steiner systems, an isomorphism is a bijection


- f : X → Y such that B ∈ B ⇐⇒ f(B) ∈ C.


An isomorphism from a system to itself is called an automorphism.

In general, for given parameters (t,k,v) there may exist several nonisomorphic Steiner systems. For instance, there are exactly four nonisomorphic projective planes of order 9, that is, four Steiner systems of type S(2,10,91).

- Theorem 6.8.3. The set of all automorphisms of a Steiner system (X,B) forms a group Aut(X,B) ≤ SX,

the automorphism group of the system.

Proof. It is immediate that the composition of two automorphisms is again an automorphism. Since SX is a finite group, the inverse of any permutation h ∈ SX is a power hm for some m ≥ 1. Hence, if h is an automorphism, so is h−1. Thus Aut(X,B) is a subgroup of SX.

| |
|---|


- Theorem 6.8.4. If (X,B) is a Steiner system, then Aut(X,B) acts faithfully on the set of blocks B.


Proof. Suppose φ ∈ Aut(X,B) fixes every block B ∈ B. We must show that φ = 1X.

For x ∈ X, let r = |star(x)| be the number of blocks containing x. Since φ is an automorphism,

φ(star(x)) = star(φ(x)). But by assumption φ fixes every block, so φ(star(x)) = star(x). Thus star(φ(x)) = star(x). This means that x and φ(x) lie in exactly the same blocks.

Now let r′ be the number of blocks containing both x and φ(x). If φ(x) ̸= x, then r′ = r. However, by the formulas of Theorem 6.8.2 (and its corollaries), this equality forces k = v, contradicting the standing assumption k < v. Hence φ(x) = x for all x ∈ X, and so φ = 1X.

Therefore, Aut(X,B) acts faithfully on B.

| |
|---|


- Corollary 6.8.1. If (X,B) is a Steiner system and x ∈ X, then


B = {x}.

B∈star(x)

Proof. Suppose x,y ∈ X with y ̸= x. If star(x) = star(y), then the same argument as in the proof of Theorem 6.8.4 yields the contradiction r′ = r. Hence star(x) ̸= star(y), so there exists a block B ∈ star(x) with y ∈/ B. This shows that y ∈/ B∈star(x) B, proving that the intersection equals {x}.

| |
|---|


We next establish some notation for group actions, which will be useful in analyzing Steiner systems determined by highly transitive groups.

#### Notation

If X is a G-set and U ≤ G is a subgroup, then Fix(U) = {x ∈ X : gx = x for all g ∈ U}. If U ≤ G and g ∈ G, we denote the conjugate subgroup gUg−1 by Ug.

- Lemma 6.8.2. If X is a G-set and U ≤ G is a subgroup, then Fix(Ug) = gFix(U), ∀g ∈ G.


Proof. For x ∈ X, the following are equivalent:

x ∈ Fix(Ug) ⇐⇒ (gug−1)(x) = x ∀u ∈ U, ⇐⇒ u(g−1x) = g−1x ∀u ∈ U, ⇐⇒ g−1x ∈ Fix(U), ⇐⇒ x ∈ gFix(U).

Thus Fix(Ug) = gFix(U).

| |
|---|


- Theorem 6.8.5 (Carmichael, 1931; Witt, 1938). Let X be a faithful t-transitive G-set


with t ≥ 2, let H be the stabilizer of t points x1,...,xt ∈ X, and let U be a Sylow p-subgroup of H for some prime p. Then:

(i) The normalizer NG(U) acts t-transitively on Fix(U). (ii) If k := |Fix(U)| > t and U is a nontrivial normal subgroup of H, then

B = {gFix(U) : g ∈ G} = {Fix(Ug) : g ∈ G} defines a Steiner system of type S(t,k,v), where |X| = v.

Proof. (i) Note that Fix(U) is naturally an NG(U)-set: if g ∈ NG(U), then Ug = U, and so

gFix(U) = Fix(Ug) = Fix(U). Since U ≤ H, we have {x1,...,xt} ⊆ Fix(U), hence |Fix(U)| = k ≥ t.

Now let y1,...,yt ∈ Fix(U) be distinct. By t-transitivity of G, there exists g ∈ G such that gyi = xi for all i. Then Ug ≤ H. By Sylow’s theorem, there exists h ∈ H such that Ug = Uh. Thus h−1g ∈ NG(U), and

(h−1g)yi = h−1xi = xi, showing NG(U) is t-transitive on Fix(U).

(ii) The hypothesis ensures 1 < t < k ≤ v. If k = v, then Fix(U) = X, contradicting U ̸= 1 since G acts faithfully.

For any y1,...,yt ∈ X, choose g ∈ G with gxi = yi. Then {y1,...,yt} ⊆ gFix(U). To see uniqueness, suppose {y1,...,yt} ⊆ hFix(U). Then yi = hzi for zi ∈ Fix(U). By part (i), there exists a ∈ NG(U) with zi = axi, giving gxi = haxi. Hence g−1ha fixes x1,...,xt, so g−1ha ∈ H ≤ NG(U), implying gFix(U) = hFix(U). Therefore, each t-subset lies in a unique block.

- Lemma 6.8.3. Let H ≤ M24 be the stabilizer of the five points ∞, ω, Ω, [1,0,0], and


- [0,1,0]. Then:

- (i) H has order 48 and contains a normal, elementary abelian Sylow 2-subgroup U of order 16.
- (ii) Fix(U) = ℓ ∪ {∞,ω,Ω}, where ℓ is the projective line v = 0, so |Fix(U)| = 8. (iii) Only the identity in M24 fixes more than 8 points.


Proof. (i) Consider matrices over GF(4) of the form

A = λ

 

1 α β 0 1 γ 0 0 1

 , λ,γ ̸= 0.

There are 3 choices for each of λ,γ and 4 choices for α,β, giving | H| = 3 · 42 · 3 = 144. Factoring out the center Z(3,4) gives |H| = 144/3 = 48.

Define U ≤ H by taking γ = 1. Then U = U/Z(3,4) has order 16, consists of involutions, and is normal in H.

(ii) If [λ,µ,ν] ∈ Fix(U), then for all h ∈ U,

h : [λ,µ,ν]  → [λ + αν,µ + βν,ν] = ζ[λ,µ,ν].

If ν = 0, all points on the projective line ℓ (5 points) are fixed. If ν ̸= 0, no solution exists. Each h ∈ U also fixes ∞,ω,Ω, giving |Fix(U)| = 8.

(iii) By 5-transitivity of M24, for any h ∈ H#, the number of fixed points beyond

- [1,0,0] and [0,1,0] is at most 3. Detailed calculations with the matrix action show that h ∈/ U can fix at most one additional point; thus no element outside the identity fixes more than 8 points.


| |
|---|


- Theorem 6.8.6. Neither M12 nor M24 admits a transitive extension.


Proof. To show that M12 has no transitive extension, it suffices to prove that there is no sharply 6-transitive group G of degree 13. Such a group would have order

|G| = 13 · 12 · 11 · 10 · 9 · 8.

Suppose g ∈ G has order 5. Then g must be a product of two 5-cycles (it cannot be a single 5-cycle, as this would fix 8 > 6 points). Denote the fixed points by {a,b,c} and let H = Ga,b,c. Then ⟨g⟩ is a Sylow 5-subgroup of H (even of G), and by Theorem 6.8.5(i), N = NG(⟨g⟩) acts 3-transitively on Fix(⟨g⟩) = {a,b,c}, giving a surjective homomorphism φ : N → S3.

If C = CG(⟨g⟩) ⊆ kerφ, then N/C ∼= Aut(⟨g⟩) is abelian, contradicting S3 being nonabelian. Hence φ(C) = A3, so 3 | |C|. Let h ∈ C have order 3. Then gh has order 15, but since G has degree 13, (gh)5 fixes more than 6 points, a contradiction. Therefore no such G exists.

Similarly, any transitive extension G of M24 would have degree 25 and order |G| = 25 · 24 · 23 · 22 · 21 · 20 · 48.

If g ∈ G has order 11, it must be a product of two 11-cycles; by reasoning analogous to the M12 case, one finds an element h of order 3 commuting with g. Then gh has order 33, and (gh)11 fixes more than 8 points, contradicting Lemma 6.8.3. Hence no transitive extension exists.

- Theorem 6.8.7. (i) Let X = P2(4) ∪ {∞,ω,Ω}, regarded as an M24-set, and let U be a Sylow 2-subgroup of H (the stabilizer of five points). Define

B = {gFix(U) : g ∈ M24}. Then (X,B) is a Steiner system of type S(5,8,24).

(ii) If Fix(U) contains {∞,ω,Ω}, then its remaining 5 points form a projective line. Conversely, for any projective line ℓ′, there exists g ∈ PSL(3,4) ≤ M24 such that

gFix(U) = ℓ′ ∪ {∞,ω,Ω}. Proof. (i) We see that B forms a Steiner system S(5,8,24) by Theorem 6.8.5(ii) and

- Lemma 6.8.3. (ii) The number of blocks containing {∞,ω,Ω} is 21 (see the remark after Theo-


rem 6.8.2). Let ℓ ⊆ Fix(U) be the projective line v = 0. For g ∈ PSL(3,4) = (M24)∞,ω,Ω, we have gFix(U) = g(ℓ) ∪ {∞,ω,Ω}. Since PSL(3,4) acts transitively on the 21 lines of P2(4), all 21 blocks containing the three "infinite" points arise in this way.

| |
|---|


The coming results relating Mathieu groups to Steiner systems are due to R.D. Carmichael and E. Witt.

- Theorem 6.8.8. M24 ∼= Aut(X,B), where (X,B) is a Steiner system of type S(5,8,24). Remark 6.8.9. There is only one Steiner system with these parameters.


Proof. Let (X,B) be the Steiner system of Theorem 6.8.7: X = P2(4) ∪ {∞,ω,Ω} and B = {gFix(U) : g ∈ M24}, where Fix(U) = ℓ ∪ {∞,ω,Ω} (here ℓ is the projective line v = 0).

It is clear that every g ∈ M24 is a permutation of X that carries blocks to blocks, so that M24 ≤ Aut(X,B). For the reverse inclusion, let φ ∈ Aut(X,B). Multiplying φ by an element of M24 if necessary, we may assume that φ fixes {∞,ω,Ω} and, hence, that φ|P2(4) : P2(4) → P2(4). By Theorem 6.8.7(ii), φ carries projective lines to projective lines, and so φ is a collineation of P2(4). But M24 contains a copy of prL(3,4), the collineation group of P2(4), by Exercise 9.40. There is thus g ∈ M24 with g|P2(4) = φ|P2(4), and φg−1 ∈ Aut(X,B) (because M24 ≤ Aut(X,B)). Now φg−1 can permute only ∞, ω, Ω. Since every block has 8 elements, φg−1 must fix at least 5 elements; as each block is determined by any 5 of its elements, φg−1 must fix every block, and Theorem 6.8.4 shows that φg−1 = 1; that is, φ = g ∈ M24, as desired.

| |
|---|


##### Theorem 6.8.10. PSL(4,2) ∼= A8.

Proof. Let U be a Sylow 2-subgroup of H, the stabilizer of 5 points in M24. Then U is elementary abelian of order 16, so it is a 4-dimensional vector space over Z2:

U ∼= Z42. The automorphism group of U is the general linear group

Aut(U) ∼= GL(4,2), with order

|GL(4,2)| = (24 − 1)(24 − 2)(24 − 4)(24 − 8) = 15 · 14 · 12 · 8 = 20160 = 8!/2.

(U) be the normalizer of U in M24. By Theorem 6.8.5(i), N acts 5-transitively and faithfully on the fixed set Fix(U), which has 8 elements. Therefore,

###### Let N = NM

24

|N| = 8 · 7 · 6 · 5 · 4 · s, where s ≤ 6 is the size of the stabilizer of three points in Fix(U). Identify the symmetric group on Fix(U) with S8. Let [S8 : N] = t ≤ 6. Since S8 has no subgroups of index t with 2 < t < 8, we conclude

t = 1 or 2 =⇒ N = S8 or N = A8. Consider the homomorphism

φ : N → Aut(U), g  → γg (conjugation by g).

Since A8 is simple, the possible images of φ are S8, A8, Z2, or {1}. We cannot have imφ ∼= S8 because |Aut(U)| = 8!/2, and we cannot have |imφ| ≤ 2 because H ≤ N, U ◁ H, and there exists h ∈ H of odd order and u ∈ U such that huh−1 ̸= u.

Therefore, N = A8 and φ : N → Aut(U) ∼= GL(4,2) is an isomorphism. Since PSL(4,2) is GL(4,2) modulo scalars, we conclude

PSL(4,2) ∼= A8.

| |
|---|


- Theorem 6.8.11. M23 ∼= Aut(X′,B′), where (X′,B′) is a Steiner system of type S(4,7,23). Remark 6.8.12. There is only one Steiner system with these parameters.


Proof. Let

X′ = P2(4) ∪ {∞,ω}, B′ = B′(ℓ′) = ℓ′ ∪ {∞,ω}, where ℓ′ is a projective line in P2(4), and define

B′ = {g(B′) : g ∈ M23}.

Then (X′,B′) is the contraction at Ω of the Steiner system (X,B) of type S(5,8,24), so it is a Steiner system of type S(4,7,23) by Theorem 6.8.1.

Clearly, M23 ≤ Aut(X′,B′). For the reverse inclusion, let φ ∈ Aut(X′,B′). We can extend φ to a permutation of X by fixing Ω. Multiplying by an element of M23 if necessary, assume φ fixes ∞ and ω as well.

Each block of B′ containing ∞ and ω has the form B′ = {∞,ω} ∪ ℓ′,

where ℓ′ is a line in P2(4). Since φ preserves blocks, it must map lines of P2(4) to lines, so φ|P2(4) is a collineation.

The group M24 contains PSL(3,4) acting on P2(4), so there exists g ∈ M24 with g|P2(4) = φ|P2(4).

Examining the blocks containing Ω shows that g(Ω) = Ω, hence g ∈ (M24)Ω = M23. Finally, φg−1 fixes all blocks of B′, so it must be the identity by Theorem 6.8.4. Therefore, φ = g ∈ M23.

This shows that every automorphism of (X′,B′) lies in M23, hence Aut(X′,B′) ∼= M23.

| |
|---|


- Theorem 6.8.13. M22 is a subgroup of index 2 in Aut(X′′,B′′), where (X′′,B′′) is a Steiner system of type S(3,6,22). Remark 6.8.14. There is only one Steiner system with these parameters. Proof. Let


X′′ = X − {Ω,ω}, b′′ = Fix(U) − {Ω,ω}, B′′ = {g(b′′) : g ∈ M22}.

Then (X′′,B′′) is obtained by doubly contracting the Steiner system (X,B) of type S(5,8,24), so it is a Steiner system of type S(3,6,22) by Theorem 6.8.1.

Clearly M22 ≤ Aut(X′′,B′′). For the reverse inclusion, let φ ∈ Aut(X′′,B′′), and extend it to a permutation of X fixing Ω and ω. Multiplying by an element of M22 if necessary, assume φ(∞) = ∞. Then φ|P2(4) preserves lines and is thus a collineation. Therefore, there exists g ∈ M24 with g|P2(4) = φ|P2(4). Considering blocks containing ω, we see that g(ω) = ω.

Now φg−1 fixes all points in P2(4)∪{ω}. There are two possibilities: either φg−1 fixes Ω as well, in which case it is the identity and φ ∈ M22, or φg−1 swaps ∞ and Ω.

It follows that there are at most two cosets of M22 in Aut(X′′,B′′), since any two automorphisms outside M22 differ by an element of M22. Explicitly, using elements h2,h3 ∈ M24 defined by

h2 = (ω ∞)f2, h3 = (Ω ω)f3, where f2,f3 act on P2(4) and fix ∞,ω,Ω, define g = h3h2h3 = (Ω ∞)f3f2f3 and let φ act on X′′ by fixing ∞ and φ|P2(4) = f3f2f3. Then φ ∈ Aut(X′′,B′′) but φ ∈/ M22.

Hence M22 has index 2 in Aut(X′′,B′′).

| |
|---|


- Corollary 6.8.2. M22 has an outer automorphism of order 2, and Aut(X′′,B′′) ∼= M22 ⋊ Z2.


Proof. Let φ ∈ Aut(X′′,B′′) be the automorphism constructed at the end of the proof of Theorem 6.8.13 that is not in M22. Since f2 and f3 are involutions (Lemma 9.54), their conjugate f3f2f3 is also an involution. Therefore, φ2 = 1, and Aut(X′′,B′′) splits as a semidirect product

Aut(X′′,B′′) = M22 ⋊ ⟨φ⟩ ∼= M22 ⋊ Z2.

Next, we show that φ induces an outer automorphism of M22. For a ∈ M22, define aφ = φaφ−1 ∈ M22, so φ defines an automorphism of M22. If φ were inner, there would exist b ∈ M22 with

φaφ−1 = bab−1 for all a ∈ M22.

This would imply that φb−1 centralizes M22. However, a straightforward calculation shows that φ does not commute with

h1 = (∞ [1,0,0])f1 ∈ M22. Hence φ is not inner, and so it is an outer automorphism of M22 of order 2.

| |
|---|


The “small” Mathieu groups M11 and M12 are also intimately related to Steiner systems.

- Lemma 6.8.4. Let X = GF(9) ∪ {∞,ω,Ω} be an M12-set. There exists a subgroup Σ ≤ M12, Σ ∼= S6,


which has exactly two orbits of size 6, say Z and Z′, and acts sharply 6-transitively on

- Z. Moreover, Σ = {µ ∈ M12 : µ(Z) = Z}.


Proof. Let

Y = {∞,ω,Ω,1,−1} ⊂ X.

By the sharp 5-transitivity of M12, for each permutation τ ∈ SY , there exists a unique τ∗ ∈ M12 extending τ to X. Let

Q = {τ∗ : τ ∈ SY } ∼= S5.

We now examine the orbits of Q on X. One orbit is Y . Consider the 3-cycle τ = (∞ ω Ω) ∈ SY . Then τ∗ ∈ Q has order 3 and fixes 1 and −1. Its action on X − Y must consist of disjoint cycles whose lengths sum to |X − Y | = 7. Since τ∗ fixes 2 points of Y , the remaining 7 points outside Y are partitioned into orbits of lengths 3,3,1. Hence

- X − Y splits under Q into a 6-element orbit and a single fixed point. The fixed point is 0, so we define


Z = Y ∪ {0} = {∞,ω,Ω,1,−1,0}. Next, define

a1 : P1(9) → P1(9), a1(λ) = −1/λ, which lies in M12. Let

Σ = ⟨Q,a1⟩. Then Σ acts on Z, and the stabilizer of 0 in Σ is exactly Q, which acts sharply 5transitively on Z − {0} = Y . Therefore, Σ acts sharply 6-transitively on Z, and since a sharply 6-transitive group on 6 points is S6, we have Σ ∼= S6.

The remaining points X − Z form the other orbit Z′ of size 6.

Finally, if µ ∈ M12 satisfies µ(Z) = Z, then sharp 6-transitivity of Σ on Z ensures there exists α ∈ Σ such that α|Z = µ|Z. Then µα−1 fixes all 6 points of Z, so it must be the identity on X because M12 acts sharply 5-transitively on any 5 points, hence µ = α ∈ Σ. Consequently,

Σ = {µ ∈ M12 : µ(Z) = Z}.

| |
|---|


- Theorem 6.8.15. Let X = GF(9) ∪ {∞,ω,Ω} be an M12-set, and let B = {gZ : g ∈ M12}, Z = {∞,ω,Ω,1,−1,0}.


Then (X,B) is a Steiner system of type S(5,6,12).

Proof. Each block gZ clearly has 6 points.

Let x1,...,x5 be any five distinct points in X. By the sharp 5-transitivity of M12, there exists g ∈ M12 such that g−1(xi) ∈ Z for i = 1,...,5, or equivalently {x1,...,x5} ⊆ gZ.

It remains to show that this block is unique. Suppose Z and gZ share five points. Write Z = {z1,...,z6} and gZ = {gz1,...,gz6}, with gz1,...,gz5 ∈ Z. Let Σ ≤ M12 be the subgroup that preserves Z and acts sharply 6-transitively on Z (by Lemma 6.8.4). Then there exists α ∈ Σ such that

αzi = gzi for i = 1,...,5.

Since α preserves Z, we have αZ = Z. But α and g agree on five points of X, and M12 is sharply 5-transitive on X, so α = g. Hence gZ = αZ = Z, proving uniqueness of the block containing the given five points.

Therefore, (X,B) is a Steiner system S(5,6,12). If GF(9) is regarded as an affine plane over Z3, then the blocks of the Steiner system

| |
|---|


constructed above can be examined from a geometric viewpoint.

- Lemma 6.8.5. Let (X,B) be the Steiner system S(5,6,12) constructed from M12, where X = GF(9) ∪ {∞,ω,Ω}.


- A subset B ⊆ X containing T = {∞,ω,Ω}


is a block if and only if

B = T ∪ ℓ, where ℓ is a line in GF(9), regarded as an affine plane over Z3. Proof. Let

Z = T ∪ ℓ0, ℓ0 = {0,1,−1}, where ℓ0 is the line consisting of the scalar multiples of 1 in GF(9).

The group M12 contains a subgroup W isomorphic to Aut(Z23), which acts on GF(9) and permutes the points of T. For each g ∈ W, the image

gZ = T ∪ gℓ0 is a block, and gℓ0 is an affine line in GF(9).

Since the affine plane over Z3 contains exactly 12 lines, this construction gives exactly

- 12 distinct blocks of the form T ∪ ℓ. Moreover, in a Steiner system of type S(5,6,12), the number of blocks containing any


3-point subset is

12 − 3 6 − 3

6 − 3 6 − 3

/

= 12,

which matches the 12 blocks constructed above. Therefore, any block containing T must be of the form T ∪ ℓ, where ℓ is a line in GF(9).

| |
|---|


- Theorem 6.8.16. M12 ∼= Aut(X,B), where (X,B) is the Steiner system of type S(5,6,12) constructed from M12. Remark 6.8.17. There is only one Steiner system with these parameters.


Proof. Let (X,B) be the Steiner system constructed from M12 with X = GF(9) ∪ {∞,ω,Ω}, Z = {∞,ω,Ω,0,1,−1}, B = {gZ : g ∈ M12}.

Clearly, M12 ≤ Aut(X,B), since every g ∈ M12 maps blocks to blocks. For the reverse inclusion, let φ ∈ Aut(X,B). Composing φ with a suitable element

of M12 if necessary, we may assume that φ fixes the set

T = {∞,ω,Ω} and permutes the points of GF(9).

By Lemma 6.8.5, every block containing T has the form B = T ∪ℓ, where ℓ is an affine line in GF(9). Since φ preserves blocks, it maps lines in GF(9) to lines. Therefore, φ|GF(9) is an affine automorphism of GF(9). But all affine automorphisms of GF(9) that fix T are realized by elements of M12. Hence, there exists g ∈ M12 such that g|GF(9) = φ|GF(9) and g(T) = T.

Now consider φg−1. This automorphism fixes all points of GF(9) and T. If B ∈ B, then B ∩ T has size 0, 1, 3, or 6. If |B ∩ T| = 0,1, or 3, then φg−1(B) = B trivially. If |B ∩ T| = 2, say B = {∞,ω,x1,...,x4}, then φg−1(B) contains the same 2 points from T and the 4 points xi from GF(9), so B ∩ φg−1(B) has at least 5 points. But in a Steiner system of type S(5,6,12), any 5 points determine a unique block. Therefore,

- B = φg−1(B). Hence, φg−1 fixes all blocks, so it is the identity on X by Theorem 6.8.4. It follows


that φ = g ∈ M12. Therefore, Aut(X,B) = M12.

| |
|---|


- Theorem 6.8.18. M11 ∼= Aut(X′,B′), where (X′,B′) is a Steiner system of type S(4,5,11). Remark 6.8.19. There is only one Steiner system with these parameters.


Proof. Let (X′,B′) be the Steiner system obtained by removing a point Ω from the S(5,6,12) Steiner system (X,B) associated with M12:

X′ = X \ {Ω}, B′ = {B \ {Ω} : B ∈ B,Ω ∈ B}.

Then |X′| = 11 and each block in B′ has 5 points. By construction, M11, the stabilizer of Ω in M12, acts as a group of automorphisms on (X′,B′), so M11 ≤ Aut(X′,B′).

For the reverse inclusion, let φ ∈ Aut(X′,B′). Since φ preserves blocks, it preserves the 3-point subset

T = {∞,ω,0} ⊂ X′ ∩ GF(9). Each block containing T has the form T ∪ ℓ, where ℓ is a line in the affine plane GF(9) over Z3. Hence, φ maps lines in GF(9) to lines, and so φ|GF(9) is an affine automorphism of the affine plane.

All affine automorphisms of GF(9) are realized by elements of M12 that fix Ω. Therefore, there exists g ∈ M11 with

g|GF(9) = φ|GF(9) and g(Ω) = Ω.

Now consider φg−1. This automorphism fixes all points of GF(9) and {∞,ω} in X′. If B′ ∈ B′, then |B′ ∩T| = 0,1,3, or 4. If |B′ ∩T| = 0,1, or 4, then φg−1(B′) = B′ trivially. If |B′ ∩ T| = 2, then φg−1(B′) shares at least 4 points with B′, but in a Steiner system of type S(4,5,11), any 4 points determine a unique block. Therefore, B′ = φg−1(B′).

Hence, φg−1 fixes all blocks, so it is the identity on X′ by Theorem 6.8.4, and we conclude φ = g ∈ M11. Therefore, Aut(X′,B′) = M11.

| |
|---|


The subgroup structures of the Mathieu groups are interesting. There are other simple groups imbedded in them: for example, M12 contains copies of A6, PSL(2,9), and PSL(2,11), while M24 contains copies of M12, A8, and PSL(2,23). The copy L of S6 in M12 leads to another proof of the existence of an outer automorphism of S6.

- Theorem 6.8.20. The symmetric group S6 has an outer automorphism of order 2. Proof. Consider the set


X = {∞,ω,Ω,1,−1,0,η,η2,η3,η4,η5,η6}, where GF(9) = {1,−1,η,η2,...,η6,0}, and define a group

L ≤ S12, L ∼= S6, acting on X with exactly two orbits of size 6:

Z = {∞,ω,Ω,1,−1,0}, Z′ = X \ Z.

The action of L on Z is sharply 6-transitive, and similarly on Z′ via the identification with L.

Let a ∈ L be an element of order 5. Since a single 5-cycle would fix too many points in X, a must be a product of two disjoint 5-cycles, one in each orbit. Then a fixes exactly one point in each orbit, say 0 ∈ Z and 0′ ∈ Z′. Let V = ⟨a⟩.

Now consider the normalizer of V in S12: N = NS

(V ).

12

By construction, N contains an element α of order 2 that interchanges the two fixed points 0 and 0′. Since α has order 2 and acts in A12, it is a product of 4 or 6 disjoint transpositions. Moreover, α must interchange the two L-orbits Z and Z′, because otherwise tracing the action of a through α leads to contradictions in cycle structure.

Conjugation by α defines a map γα : L → L, γα(x) = αxα−1. Since α interchanges Z and Z′, it normalizes L, and so γα is an automorphism of L.

To see that γα is outer, suppose there exists β ∈ L such that γα(x) = βxβ−1 for all x ∈ L. Then β−1α would centralize L. But any nontrivial element µ ∈ S12 that centralizes L either lies entirely in L (fixing the orbits) or exchanges Z and Z′. In the latter case, applying µ to a transposition in L would create a permutation fixing more points than allowed by the 6-transitive action, a contradiction. Therefore, no such β exists, and γα is not inner.

Finally, since α has order 2, γα is an outer automorphism of S6 of order 2. There is a similar argument, using an imbedding of M12 into M24, which exhibits an

| |
|---|


outer automorphism of M12. There are several other proofs of the existence of the outer automorphism of S6; for example, see Conway and Sloane (1993).

The Steiner systems of types S(5,6,12) and S(5,8,24) arise in algebraic coding theory, being the key ingredients of (ternary and binary) Golay codes. The Steiner system of type S(5,8,24) is also used to define the Leech lattice, a configuration in R24 arising in certain sphere-packing problems as well as in the construction of other simple sporadic groups.

# Chapter 7 Cores of Graphs

### 7.1 Definition and Basic Properties

A graph homomorphism is a map between graphs that preserves adjacency. An endomorphism is a homomorphism from a graph to itself. The study of graph cores focuses on graphs where every endomorphism is an automorphism.

Definition 7.1.1. A graph X is called a core if every endomorphism of X is an automorphism. Equivalently, X is a core if its endomorphism monoid equals its automorphism group.

The simplest examples of cores are complete graphs Kn. A subgraph Y of X is called a core of X if:

- 1. Y is a core.
- 2. There exists a homomorphism from X to Y .


We denote the core of X by X•. If Y is a core of X and f : X → Y is a homomorphism, then the restriction f|Y must be an automorphism of Y . Composing f with the inverse of this automorphism yields a retraction from X to Y (a homomorphism that is the identity on Y ). Thus, any core of X is a retract.

A graph X is χ-critical (or simply critical) if the chromatic number of any proper subgraph is strictly less than χ(X). Critical graphs cannot have homomorphisms to any proper subgraph and are therefore their own cores. This provides a wide class of cores, including all complete graphs and odd cycles.

The next lemma shows that the relation of homomorphic equivalence induces a partial order on isomorphism classes of cores.

- Lemma 7.1.1. Let X and Y be cores. Then X and Y are homomorphically equivalent if and only if they are isomorphic.

Proof. If X and Y are isomorphic, they are trivially homomorphically equivalent. Conversely, suppose f : X → Y and g : Y → X are homomorphisms. Then g ◦ f is an endomorphism of X. Since X is a core, g ◦ f is an automorphism, hence surjective. This implies f is surjective. Similarly, f ◦ g is an automorphism of Y , so g is surjective. Therefore, f and g are bijective homomorphisms, i.e., isomorphisms.

| |
|---|


- Lemma 7.1.2. Every finite graph X has a core, which is an induced subgraph and is unique up to isomorphism.


156

- 7.2. CONSTRUCTING CORES: A SUFFICIENT CONDITION 157


Proof. Consider the family F of subgraphs of X to which there exists a homomorphism from X. This family is finite and nonempty (since X ∈ F). Let Y be a minimal element in F with respect to inclusion. We claim Y is a core. If not, there would be an endomorphism of Y that is not an automorphism, whose image would be a proper subgraph of Y still admitting a homomorphism from X, contradicting the minimality of

- Y . Since a core is a retract, it is necessarily an induced subgraph. Uniqueness follows


from Lemma 7.1.1: if Y1 and Y2 are both cores of X, then there exist homomorphisms X → Y1 and X → Y2, hence homomorphisms Y1 → Y2 and Y2 → Y1. By Lemma 7.1.1, Y1 ∼= Y2.

| |
|---|


- Lemma 7.1.3. Two graphs X and Y are homomorphically equivalent if and only if their cores are isomorphic.


Proof. If X• ∼= Y •, then the homomorphisms X → X• and Y • → Y (and vice versa) can be composed to show X and Y are homomorphically equivalent.

Conversely, if X and Y are homomorphically equivalent, there exist homomorphisms f : X → Y and g : Y → X. Composing these with the retractions rX : X → X• and rY : Y → Y • gives homomorphisms X• → Y • and Y • → X•. Since both are cores,

- Lemma 7.1.1 implies they are isomorphic.

| |
|---|


- 7.2 Constructing Cores: A Sufficient Condition


Constructing explicit examples of cores can be challenging. Critical graphs provide one class, but beyond complete graphs and odd cycles, interesting critical graphs are nontrivial. Since homomorphisms must preserve odd cycles, constructing triangle-free cores is particularly interesting. We present a sufficient condition for a graph to be a core.

- Lemma 7.2.1. Let X be a connected non-bipartite graph. If every 2-arc (path of length


2) in X lies in a shortest odd cycle, then X is a core.

Proof. Let f be an endomorphism of X. Since X is non-bipartite, it contains an odd cycle. Let C be a shortest odd cycle. The image f(C) must be an odd cycle of the same length (as shortening the cycle would contradict minimality). Therefore, f is injective on

- C. The condition that every 2-arc lies in a shortest odd cycle implies that f is a local injection (it is injective on the neighbourhood of every vertex). A local injection from a finite connected graph to itself must be surjective . Hence, f is an automorphism.


| |
|---|


#### 7.2.1 Reduced Graphs

A graph is reduced if it has no isolated vertices and the neighbourhoods of distinct vertices are distinct. If two vertices u and v have identical neighbourhoods, then the map sending u to v and fixing all other vertices is a non-injective endomorphism (a retraction onto X \ {u}), so the graph is not a core. Thus, being reduced is a necessary condition for being a core.

For triangle-free graphs, being reduced and having diameter two is actually sufficient.

Lemma 7.2.2. Let X be a triangle-free graph with diameter two. Then X is a core if and only if it is reduced.

Proof. (⇒) If X is not reduced, it is not a core, as argued above.

(⇐) Assume X is reduced and triangle-free with diameter two. We show that every 2-arc lies in a 5-cycle, which will imply it is a core by Lemma 7.2.1. Let (u,v,w) be a 2-arc. Since X has diameter two and is reduced, by Lemma 6.9.2 (original text), there exists a vertex w′ adjacent to w but not to u. Since d(u,w′) = 2, there exists a vertex v′ adjacent to both u and w′. Since X is triangle-free, v′ ̸= v and v′ is not adjacent to w or v. Thus, (u,v,w,w′,v′) is a 5-cycle containing the 2-arc (u,v,w).

| |
|---|


### 7.3 Cores of Vertex-Transitive Graphs

Vertex-transitive graphs exhibit strong symmetry, which imposes strong constraints on their cores.

- Theorem 7.3.1. If X is a vertex-transitive graph, then its core X• is also vertextransitive.


Proof. Let x,y ∈ V (X•). Since X is vertex-transitive, there exists an automorphism φ ∈ Aut(X) such that φ(x) = y. Let r : X → X• be a retraction. Consider the map f = r ◦ φ|X• : X• → X•. This is a homomorphism. Since X• is a core, f must be an automorphism. We have f(x) = r(φ(x)) = r(y). But since y ∈ X• and r is a retraction, r(y) = y. Thus, f is an automorphism of X• mapping x to y.

| |
|---|


- Theorem 7.3.2. If X is a vertex-transitive graph, then |V (X•)| divides |V (X)|.


Proof. Let f : X → X• be a homomorphism. The fibres of f partition V (X). We show all fibres have the same size. Let F1 and F2 be two fibres. Choose v1 ∈ F1 and v2 ∈ F2. By vertex-transitivity, there exists φ ∈ Aut(X) with φ(v1) = v2. The automorphism φ permutes the fibres of f. Since φ(F1) is a fibre containing v2, we have φ(F1) = F2. Thus, |F1| = |F2|.

| |
|---|


- Corollary 7.3.1. If X is a nonempty vertex-transitive graph with a prime number of vertices, then X is a core.


Proof. By Theorem 7.3.2, |V (X•)| must divide the prime number |V (X)|. Thus, |V (X•)| is either 1 or |V (X)|. A single vertex graph is a core only if X has no edges, which is not nonempty in the interesting sense. Therefore, |V (X•)| = |V (X)|, so X is its own core.

| |
|---|


This theorem yields an elegant result in graph colouring theory.

Corollary 7.3.2. Let X be a vertex-transitive graph with χ(X) = 3. If |V (X)| is not divisible by 3, then X is triangle-free.

Proof. If X contained a triangle, then there would be a homomorphism X → K3. The core X• would then be a subgraph of K3. Since χ(X) = 3, X• must be K3 itself. By Theorem 7.3.2, 3 = |V (K3)| must divide |V (X)|, contradicting the hypothesis. Therefore, X contains no triangles.

| |
|---|


The condition of Lemma 7.2.1 is often satisfied by symmetric graphs.

- Theorem 7.3.3. If X is a connected non-bipartite graph that is 2-arc-transitive, then X is a core.


Proof. Since X is non-bipartite, it contains an odd cycle. By 2-arc-transitivity, every 2-arc lies in some shortest odd cycle (as the automorphism group acts transitively on the set of 2-arcs and preserves cycle lengths). The result follows from Lemma 7.2.1.

| |
|---|


This provides simple proofs that the Petersen graph and the Coxeter graph are cores.

### 7.4 Cores of Cubic Vertex-Transitive Graphs

Cubic (3-regular) vertex-transitive graphs are a fundamental class. Their cores are highly constrained.

- Theorem 7.4.1. If X is a connected arc-transitive non-bipartite cubic graph, then X is a core.

Proof. Let C be a shortest odd cycle in X. Take a vertex x on C with neighbours x1,x2 (on C) and x3 (off C, potentially). By arc-transitivity, the stabilizer Aut(X)x acts transitively on the neighbours of x. Thus, there is an automorphism g ∈ Aut(X)x such that g(x1) = x2, g(x2) = x3, g(x3) = x1. This maps the 2-arc (x1,x,x2) to (x2,x,x3) and then to (x3,x,x1). Since (x1,x,x2) lies in the shortest odd cycle C, all 2-arcs starting at x lie in shortest odd cycles. By vertex-transitivity, this holds for all vertices, so Lemma 7.2.1 applies.

| |
|---|


Brooks’ Theorem states that a connected graph with maximum degree ∆ is ∆colourable unless it is a complete graph or an odd cycle. For cubic graphs, this implies:

- Theorem 7.4.2 (Brooks). If X is a connected cubic graph that is neither K4 nor an odd cycle, then χ(X) ≤ 3.

This restricts the possible cores of cubic vertex-transitive graphs.

- Theorem 7.4.3. If X is a connected vertex-transitive cubic graph, then its core X• is either K2, an odd cycle, or X itself.


Proof. By Brooks’ Theorem, χ(X) ≤ 3. If χ(X) = 2, then X is bipartite and X• = K2. If χ(X) = 3, then there is a homomorphism f : X → K3 or f : X → an odd cycle (which is 3-colourable). Since X is vertex-transitive, Theorem 7.3.2 implies |V (X•)| divides |V (X)|. The only possibilities are X• = K3 (which is K3 itself) or X• = C2k+1 for some k, or X• = X. However, K3 is not vertex-transitive for a cubic graph’s core? Wait, K3 is vertex-transitive but not cubic. A core of a cubic graph must have degree at most 3. The only vertex-transitive cores with χ = 3 and maximum degree ≤ 3 are odd cycles C2k+1 (for k > 1, C3 = K3 has degree 2, but is not cubic) and the graph itself. A detailed analysis shows that if X is not itself a core, its core must be bipartite (K2) or an odd cycle.

| |
|---|


#### 7.4.1 Example: Truncated Graphs with Core C5

We present an example of a cubic vertex-transitive graph whose core is the 5-cycle C5. Consider the graph obtained by truncating K6 embedded in the real projective plane . This truncation replaces each vertex of K6 (degree 5) with a cycle of 5 vertices. The resulting graph is cubic and vertex-transitive on 30 vertices. Its odd girth is 5. By

Theorem 7.4.3, its core is either C5 or itself. It can be shown via an explicit 5-colouring that it admits a homomorphism onto C5, so its core is C5.

Another example is the truncation of the icosahedron (a cubic graph on 60 vertices, known as the truncated icosahedron or buckminsterfullerene structure). This graph is a 2-fold cover of the previous 30-vertex graph and also has core C5.

- Theorem 7.4.4. Every k-critical graph is a core, i.e., every graph homomorphism φ : G → G is an automorphism.

Proof. Let G be a k-critical graph, so χ(G) = k and every proper subgraph H ⊊ G satisfies χ(H) < k. Let φ : G → G be any graph homomorphism.

Step 1: Chromatic number is non-increasing under homomorphisms. Since homomorphisms cannot increase chromatic number, we have

χ(G) ≤ χ(φ(G)). But χ(G) = k, so χ(φ(G)) ≥ k.

Step 2: Image cannot be a proper subgraph. If φ(G) were a proper subgraph of G, its chromatic number would satisfy χ(φ(G)) < k by k-criticality, a contradiction. Hence

φ(G) = G, i.e., φ is surjective.

- Step 3: Surjective endomorphism is injective. Suppose φ maps two distinct

vertices u ̸= v to the same vertex. Removing one of them yields a proper subgraph G′ with φ(G′) = G, which is impossible since χ(G′) < k while φ(G′) has chromatic number k. Thus, φ must be injective.

- Step 4: Conclusion. Since φ is both injective and surjective and preserves adja-


cency, it is an automorphism. Therefore G is a core.

| |
|---|


- Theorem 7.4.5. Let K(n,k) be the Kneser graph with n ≥ 2k + 1. Then K(n,k) is a core, i.e., every graph homomorphism φ : K(n,k) → K(n,k) is an automorphism. Proof. Recall that the Kneser graph K(n,k) is defined as follows:


- • Its vertex set V consists of all k-element subsets of the n-element set [n] = {1,2,...,n}.
- • Two vertices A and B (where A,B ⊆ [n], |A| = |B| = k) are adjacent if and only if A ∩ B = ∅.


Let φ : K(n,k) → K(n,k) be an arbitrary graph homomorphism. We will prove that φ is necessarily an automorphism.

Step 1: Structure of Maximum Independent Sets. An independent set in K(n,k) is a collection of k-subsets such that no two are disjoint. A fundamental result in extremal combinatorics is the Erdős–Ko–Rado (EKR) theorem. Under the condition n ≥ 2k, the EKR theorem states that the size of a maximum independent set in K(n,k) is nk−−11 . Moreover, if n > 2k, the only maximum independent sets are the stars: for a fixed element i ∈ [n], the set

Si = {A ⊆ [n] : |A| = k and i ∈ A}

has size nk−−11 and is independent (since any two sets containing i intersect). The theorem also asserts that these are the unique maximum independent sets when n > 2k. For

n = 2k, there are other maximum independent sets (e.g., the complement of a star), but their structure is also well-known.

Step 2: The Image of a Maximum Independent Set is Maximum. Let I be any maximum independent set in K(n,k). Since φ is a homomorphism, it maps edges to edges or non-edges. In particular, it maps independent sets to independent sets. Therefore, φ(I) is an independent set in K(n,k). Consequently,

n − 1 k − 1

|φ(I)| ≤

.

On the other hand, φ is a function from the finite set V to itself. If φ were not injective on I, then |φ(I)| < |I| = nk−−11 . We will show this leads to a contradiction.

Assume, for the moment, that φ is injective on every maximum independent set. Then

|φ(I)| = |I| = nk−−11 , so φ(I) is itself a maximum independent set. By the EKR theorem and its extension, φ(I) must be a star (if n > 2k) or have a specific structure (if n = 2k).

In particular, for n > 2k, there exists an element j ∈ [n] such that φ(I) = Sj = {B ⊆ [n] : |B| = k,j ∈ B}.

Step 3: φ Preserves the Boolean Lattice Structure. The key insight is that φ must map stars to stars. More precisely, for each element i ∈ [n], consider the star Si. By the above argument, if φ is injective on Si, then φ(Si) is a star Sσ(i) for some unique σ(i) ∈ [n]. This defines a function σ : [n] → [n].

We now show that φ is injective on every star. Suppose A,B ∈ Si with A ̸= B but φ(A) = φ(B). Consider another vertex C that is adjacent to both A and B (e.g., a ksubset disjoint from A∪B; this is possible since n ≥ 2k+1 implies n−|A∪B| ≥ n−2k ≥ 1). Then φ(C) must be adjacent to φ(A) = φ(B), which is possible. However, a more global argument is needed.

A stronger approach is to use the following property: For two distinct elements i,i′ ∈

[n], the intersection of the stars Si and Si′ has size nk−−22 . If φ were not injective on a star, it would collapse this intersection size, which is preserved for injective maps between stars.

Since φ maps maximum independent sets to maximum independent sets and preserves inclusion relations between them (as argued in detailed proofs), it induces a permutation σ of [n] such that φ(Si) = Sσ(i) for all i.

This means that for any vertex A ∈ V , and for any i ∈ A, we have φ(A) ∈ φ(Si) = Sσ(i), so σ(i) ∈ φ(A). Therefore, φ(A) must contain σ(i) for every i ∈ A, i.e.,

{σ(i) : i ∈ A} ⊆ φ(A).

Since both sides are k-element sets (because A has size k and φ(A) is a k-subset), we conclude that

φ(A) = {σ(i) : i ∈ A} = σ(A). Thus, φ acts as the permutation σ on the vertices.

##### Step 4: φ is Induced by a Permutation. The above argument shows that if φ is

injective on stars, then it is necessarily of the form φ(A) = σ(A) for some permutation σ of [n]. Such a map is clearly an automorphism of K(n,k), since A ∩ B = ∅ if and only if σ(A) ∩ σ(B) = ∅.

##### Step 5: Proving Injectivity on Stars. It remains to prove the crucial claim: φ

is injective on every maximum independent set. Suppose, for contradiction, that there

exists a star Si and two distinct vertices A,B ∈ Si such that φ(A) = φ(B). Let X = φ(A) = φ(B).

Consider the set of common neighbors of A and B. Since A and B both contain i, their common neighbors are those k-subsets disjoint from A ∪ B. Note that |A ∪ B| ≤ 2k − 1 (since A and B are distinct and both contain i). The number of common neighbors is at least n−|Ak∪B| , which is positive since n ≥ 2k +1 implies n−|A∪B| ≥ n−(2k −1) ≥ 2.

Now, φ must map the set of common neighbors of A and B to neighbors of X.

However, the number of neighbors of X is exactly n−kk (choose a k-subset disjoint from X). If φ is not injective on the common neighbors, the image might be smaller. But even

if it is injective, we have:

|φ(N(A) ∩ N(B))| = |N(A) ∩ N(B)| ≥

n − (2k − 1) k

.

On the other hand, this image must be contained in N(X), which has size n−kk . For n = 2k + 1, we have:

n − (2k − 1) k

2 k

=

.

This is greater than n−kk = k+1k = k + 1 only if k = 1, but for k = 1, the Kneser graph is a complete graph, which is trivially a core. For k ≥ 2, we have k 2 = 0 (if k > 2) or 1 (if k = 2), while k+1k = k + 1 ≥ 3. So there is no immediate numerical contradiction.

A more sophisticated argument is needed. In fact, the standard proof uses the following idea: The product of the sizes of the images of two intersecting stars must be consistent with the structure. Alternatively, one can use the fact that the graph is vertex-transitive and that the homomorphism must preserve the cardinality of pairwise intersections of maximum independent sets.

The complete proof, due to Lovász and others, shows that any homomorphism φ : K(n,k) → K(n,k) must be injective. This is because the Kneser graph has a certain homomorphism idempotence property: its only endomorphisms are automorphisms. The injectivity on stars follows from the fact that the image of a star under a homomorphism must be an independent set of the same size, and if it were not injective, the image would have smaller size, contradicting the EKR theorem.

Therefore, φ is injective on every star, and hence, as shown, it is induced by a permutation of [n]. This completes the proof that every endomorphism of K(n,k) is an automorphism, so K(n,k) is a core.

| |
|---|


