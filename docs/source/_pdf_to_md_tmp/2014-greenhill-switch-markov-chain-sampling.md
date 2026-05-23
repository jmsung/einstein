## The switch Markov chain for sampling irregular graphs

(Extended Abstract) Catherine Greenhill∗

# arXiv:1412.5249v1[cs.DS]17Dec2014

Abstract

The problem of eﬃciently sampling from a set of (undirected) graphs with a given degree sequence has many applications. One approach to this problem uses a simple Markov chain, which we call the switch chain, to perform the sampling. The switch chain is known to be rapidly mixing for regular degree sequences. We prove that the switch chain is rapidly mixing for any degree sequence with minimum degree at least 1 and with maximum degree dmax which satisﬁes 3 ≤ dmax ≤ 41

√

M, where M is the sum of the degrees. The mixing time bound obtained is only an order of n larger than that established in the regular case, where n is the number of vertices.

### 1 Introduction

The switch chain is a natural Markov chain for sampling from a set of graphs with a given degree sequence. Each move of the chain selects two distinct, non-incident edges edges uniformly at random and attempts to replace these edges by a perfect matching of the four endvertices, chosen uniformly at random. The proposed move is rejected if a multiple edge would be formed.

We call each such move a switch. Ryser [21] used switches to study the structure of 0-1 matrices. Markov chains based on switches have been introduced by Besag and Cliﬀord [3] for 0-1 matrices (bipartite graphs), Diaconis and Sturmfels [7] for contingency tables and Rao, Jana and Bandyopadhyay [20] for directed graphs.

The switch chain is aperiodic and its transition matrix is symmetric. It is well-known that the switch chain is irreducible for any (undirected) degree sequence: see [19, 24].

In order for the switch chain to be useful for sampling, it must converge quickly to its stationary distribution. (For Markov chain deﬁnitions not given here, see [10].)

Cooper, Dyer and Greenhill [5, 6] showed that the switch chain is rapidly mixing for regular undirected

∗c.greenhill@unsw.edu.au, School of Mathematics and Statistics, UNSW Australia, Sydney 2052, Australia. Research supported by Australian Research Council Discovery Project DP140101519.

graphs. Here the degree d = d(n) may depend on n, the number of vertices. The mixing time bound is given as a polynomial in d and n. Earlier, Kannan, Tetali and Vempala [13] investigated the mixing time of the switch chain for regular bipartite graphs. Greenhill [9] proved that the switch chain for regular directed graphs (that is, d-in, d-out directed graphs) is rapidly mixing, again for any d = d(n). Mikl´s, Erd˝s and Soukup [18] proved that the switch chain is rapidly mixing on half-regular bipartite graphs; that is, bipartite degree sequences which are regular for vertices on one side of the bipartition, but need not be regular for the other.

The proofs of all these mixing results used a multicommodity ﬂow argument [22]. In each case, regularity (or half-regularity) was only required for one lemma, which we will call the critical lemma. This is a counting lemma which is used to bound the maximum load of the ﬂow (see [5, Lemma 4], [9, Lemma 5.6] and [18, Lemma 6.15]).

In Section 3 we give an alternative proof of the critical lemma which does not require regularity. This establishes the following theorem, extending the rapid mixing result from [5] to irregular degree sequences which are not too dense.

Given a degree sequence d = (d1,...,dn), write Ω(d) for the set of all (simple) graphs with vertex set [n] = {1,2,...,n} and degree sequence d. Recall that d is called graphical when Ω(d) is nonempty. We restrict our attention to graphical sequences. Write dmin and dmax for the minimum and maximum degree in d, respectively, and let M = nj=1 dj be the sum of the degrees.

Theorem 1.1. Let d = (d1,...,dn) be a graphical degree sequence such that dmin ≥ 1 and

√

1 4

3 ≤ dmax ≤

M.

The mixing time τ(ε) of the switch Markov chain with state space Ω(d) satisﬁes

τ(ε) ≤ 101 d14max M9 M log(M) + log(ε−1) .

This result covers many diﬀerent degree sequences, for example:

- • sparse graphs with constant average degree and maximum√n, degree a suﬃciently small constant times

- • dense graphs with linear average degree and maximum degree a suﬃciently small constant times n.


The mixing time bound given above is at most a factor of n larger than that obtained in [5, 6] in the regular case. (To see this, substitute M = dmaxn, which holds when d is regular: note that M ≤ dmaxn always holds,

- as M is the sum of the degrees.) We expect that our approach also applies to di-


rected graphs, which should allow the rapid mixing proof from [9] to be extended to irregular directed degree sequences, under conditions analogous to those in Theorem 1.1.

- 1.1 Related work There are several approaches to the problem of sampling graphs with a given degree sequence, though none is known to be eﬃcient for all degree sequences. The conﬁguration model of Bollob´s [4] gives expected polynomial time uniform sampling if


dmax = O(√log n). McKay and Wormald [16] adapted the conﬁguration model to give an algorithm which performs uniform sampling from Ω(d) in expected polynomial time when dmax = O(M1/4).

Jerrum and Sinclair [11] used a construction of Tutte’s to reduce the problem of sampling from Ω(d) to the problem of sampling perfect matchings from an auxilliary graph. The resulting Markov chain algorithm is rapidly mixing if the degree sequence d is stable: see [12]. Stable sequences are those in which small local changes to the degree sequences do not greatly aﬀect the size of |Ω(d)|. Many degree sequences which satisfy the conditions of Theorem 1.1 are stable; however, not all stable sequences satisfy the conditions of Theorem 1.1. (For example, if dmin = n/9 and dmax = 4n/9 then d is stable [12] but then

√

M ≤ 2n/3, which is not large enough for Theorem 1.1.)

Steger and Wormald [23] gave an easilyimplementable algorithm for sampling regular graphs, and proved that their algorithm performs asymptotically uniform sampling in polynomial time when d = o(n1/28) (where d denotes the degree). Kim and Vu [14] gave a sharper analysis and established that d = o(n1/3) suﬃces for eﬃcient asymptotically uniform sampling. Bayati, Kim and Saberi [2] extended Steger and Wormald’s algorithm to irregular degree sequences, giving polynomial-time asymptotically uniform sampling when dmax = o(M1/4). From this they constructed a sequential importance sampling

algorithm for Ω(d). Recently, Zhao [25] described and analysed a similar approach to that of [16], in a general combinatorial setting. Zhao shows that for sampling from Ω(d), when dmax = o(M1/4), his algorithm performs asymptotically uniform sampling in time O(M).

Finally we note that Barvinok and Hartigan [1] showed that the adjacency matrix of a random element of Ω(d) is “close” to a certain “maximum entropy matrix”, when the degree sequence is tame. The deﬁnition of tame depends on the maximum entropy matrix, but a suﬃcient condition is that dmin ≥ α(n−1) and dmax ≤ β(n−1) for some constants α,β > 0. Some degree sequences satisfying this latter condition are stable sequences, and many of these degree sequences also satisfy the condition of Theorem 1.1. It would be interesting to explore further the connections between stable degree sequences, tame degree sequences and the mixing rate of the switch Markov chain.

It is not known whether the corresponding counting problem (exact evaluation of |Ω(d)|) is #P-complete. There are several results giving asymptotic enumeration formulae for |Ω(d)| under various conditions on d: see for example [1, 15, 17] and references therein.

### 2 The switch chain and multicommodity ﬂow

A transition of the switch chain on Ω(d) is performed as follows: from the current state G ∈ Ω(d), choose an unordered pair of two distinct non-adjacent edges uniformly at random, say F = {{x,y},{z,w}}, and choose a perfect matching F from the set of three perfect matchings of (the complete graph on) {x,y,z,w}, chosen uniformly at random. If F ∩ (E(G) \ F) = ∅ then the next state is the graph G with edge set (E(G) \ F) ∪ F , otherwise the next state is G = G.

Deﬁne M2 = nj=1 dj(dj − 1). If P(G,G ) = 0 and G = G then P(G,G ) = 3a1(d), where

(2.1) a(d) =

M/2 2 − 21 M2

is the number of unordered pairs of distinct nonadjacent edges in G. This shows that the Markov chain is symmetric. The chain is aperiodic since by deﬁnition P(G,G) ≥ 1/3 for all G ∈ Ω(d).

2.1 Multicommodity ﬂow To bound the mixing time of the switch chain, we apply a multicommodity ﬂow argument. Suppose that G is the graph underlying a Markov chain M, so that xy is an edge of G if and only if P(x,y) > 0. A ﬂow in G is a function f : P → [0,∞)

#### such that

f(p) = π(x)π(y) for all x,y ∈ Ω, x = y.

p∈Pxy

Here Pxy is the set of all simple directed paths from x to y in G and P = ∪x =yPxy. Extend f to a function on oriented edges by setting f(e) = p e f(p), so that f(e) is the total ﬂow routed through e. Write Q(e) = π(x)P(x,y) for the edge e = xy. Let (f) be the length of the longest path with f(p) > 0, and let ρ(e) = f(e)/Q(e) be the load of the edge e. The maximum load of the ﬂow is ρ(f) = maxe ρ(e). Using Sinclair [22, Proposition 1 and Corollary 6’], the mixing time of M can be bounded above by

- (2.2) τ(ε) ≤ ρ(f) (f) log(1/π∗) + log(ε−1 where π∗ = min{π(x) | x ∈ Ω}.


- 2.2 Deﬁning the ﬂow The deﬁnition of the multicommodity ﬂow given in [5, Section 2.1] carries across to irregular degree sequences without change. This is because the ﬂow from G to G depends only on the symmetric diﬀerence G G of G and G , treated as a


- 2-edge-coloured graph (with edges from G\G coloured blue and edges from G \G coloured red, say). The blue degree at a given vertex equals the red degree at that vertex, but in general the blue degree sequence will not be regular. Hence the multicommodity ﬂow deﬁnition given in [5] is already general enough to handle irregular degree sequences.


The multicommodity ﬂow is deﬁned using a process which we now sketch. Given G,G ∈ Ω(d):

- • Deﬁne a bijection from the set of blue edges incident at v to the set of red edges incident at v, for each vertex v ∈ [n]. The vector of these bijections is called a pairing ψ, and the set of all possible pairings is denoted Ψ(G,G ).
- • The pairing gives a canonical way to decompose the symmetric diﬀerence G G into a sequence of circuits, where each circuit is a blue/red-alternating closed walk.
- • Each circuit is decomposed in a canonical way into a sequence of simpler circuits of two types: 1circuits and 2-circuits. A 1-circuit is an alternating cycle in G G , while a 2-circuit is an alternating walk with one vertex of degree 4, the rest of degree 2, consisting of two odd cycles which share a common vertex. Each 1-circuit or 2-circuit has a designated start vertex. (The start vertex of a 2-circuit is the unique vertex of degree 4.) An important fact is that the 1-circuits and 2-circuits are pairwise edge-disjoint.


• Each 1-circuit or 2-circuit is processed in a canonical way to give a segment of the canonical path γψ(G,G ).

For full details see [5, Section 2.1]. 3 Analysing the ﬂow

Now we show how to bound the load of the ﬂow by adapting the analysis from [5]. Note that some proofs in [5] used the assumption d = d(n) ≤ n/2, since (for regular sequences) the general result follows by complementation. This trick does not work for irregular degree sequences, so we cannot make a similar assumption here.

Given matrices G, G , Z ∈ Ω(d), deﬁne the encoding L of Z (with respect to G,G ) by

L + Z = G + G

by identifying each of Z, G and G with their symmetric 0-1 adjacency matrices. Then L is a symmetric n × n matrix with entries in {−1,0,1,2} and with zero diagonal. Entries which equal −1 or 2 are called defect entries. Treating L as an edge-labelled graph with edges labelled −1,1,2 (and omitting edges corresponding to zero entries), a defect edge is an edge labelled −1 or 2. (In [5] these were called “bad edges”.) Speciﬁcally, we will refer to (−1)-defect edges and to 2-defect edges. A 2-defect edge is present in both G and G but is absent in Z, while a (−1)-defect edge is absent in both G and G but is present in Z.

We say that the degree of vertex v in L is the sum of the labels of the edges incident with v (equivalently, the sum of the entries in the row of L corresponding to v). By deﬁnition, the degree sequence of L equals d.

Some proofs from [5, 6] also apply in the irregular case without any substantial change (after replacing d by dmax). These proofs refer only to the symmetric diﬀerence and the process used to construct the multicommodity ﬂow (and none of them use the assumption d ≤ n/2). We state two of these results now.

Lemma 3.1. Suppose that G,G ,Z,Z ∈ Ω(d) are such that (Z,Z ) is a transition of the switch chain which lies on the canonical path γψ(G,G ) for some ψ ∈ Ψ(G,G ). Let L be the encoding of Z with respect to (G,G ). Then the following statements hold:

- (i) ([5, Lemma 1]) From (Z,Z ), L and ψ it is possible to uniquely recover G and G .
- (ii) ([5, Lemma 2]) There are at most four defect edges in L. The labelled graph consisting of the defect edges in L must form a subgraph of one of the ﬁve labelled graphs shown in Figure 1, where “?” represents a label which may be either −1 or 2.


x a

x a

z

x

x

z

x a

x

a

x x

x z

x z

a

z

Figure 1: The ﬁve possible conﬁgurations of four defect edges

The next result collects together some further useful results about encodings. Lemma 3.2. Suppose that the conditions of Lemma 3.1 hold. Let x,y,z ∈ [n] be distinct vertices.

- (i) If L(x,y) = 2 then dx ≥ 2, dy ≥ 2.
- (ii) If L(x,y) = 2 and L(y,z) = 2 then dy ≥ 4.
- (iii) If L(x,y) = 2 and L(y,z) = −1 then dy ≥ 3.


Proof. It follows from the deﬁnition of the multicommodity ﬂow given in [5] that a 2-defect edge {x,y} (with L(x,y) = 2) can only arise in two cases:

- (a) {x,y} is a shortcut edge which is present in G,G but which is absent in Z. (See [5, Figure 4].) In this case, x and y are vertices on some 2-circuit, which is an alternating blue/red walk in the symmetric diﬀerence G G . Hence both x and y have degree at least two in G.
- (b) {x,y} is an odd chord which is present in G,G but which is absent in Z. (See the section “Processing a 1-circult” in [5].) In this case, x and y are vertices on some 1-circuit, which is an alternating blue/red walk in the symmetric diﬀerence G G . Again, this shows that both x and y have degree at least two in G.


This proves (i).

Next, if y is incident with two edges of defect 2 then it must be that one is an odd chord for a 1-circuit C1 and one is a shortcut edge for a 2-circuit C2. Then y is incident in G with an edge of C1, an edge of C2 and the two edges {x,y}, {y,z} which are 2-defect edges in L. Since C1 and C2 are edge-disjoint and no defect edge belongs to G G , it follows that dy ≥ 4, proving (ii).

We may adapt this argument to prove (iii), noting that a (−1)-defect may only arise from a shortcut edge or an odd chord which is absent in G and G and present in Z.

| |
|---|


Now we extend the term “encoding” to refer to any symmetric n×n matrix with entries in {−1,0,1,2} which has zero diagonal and row sums given by d. We say that an encoding L is consistent with Z if L+Z only takes entries in {0,1,2}. Say that an encoding is valid if it satisﬁes the conclusions of Lemma 3.1(ii), and that a valid encoding is good if it also satisﬁes the conclusion of Lemma 3.2. Let L(Z) be the set of valid encodings which are consistent with Z, and let L∗(Z) be the set of good encodings which are consistent with Z. In [5] the set L(Z) was studied, but we require a bit more information about our encodings, so we will focus on the smaller set L∗(Z).

Lemma 3.3. ([5, Lemma 5] and [6, Lemma 1]) The load f(e) on the transition e = (Z,Z ) satisﬁes

f(e) ≤ d14max |L∗(Z)|

.

|Ω(d)|

Proof. In [5, Lemma 5] and [6, Lemma 1] it was shown that f(e) ≤ d14 |L(Z)|/|Ω(d)|2 when d = (d,d,...,d) is a regular degree sequence. (The assumption d ≤ n/2 is not used in this proof.) The proof relied on the fact that L(Z) contains all encodings which may arise along a canonical path. But the same is true for L∗(Z), by Lemma 3.1(ii) and Lemma 3.2, so the proof goes through without change in the irregular setting (after replacing d by dmax).

| |
|---|


The switch operation can be extended to encodings in the natural way: each switch reduces two edge labels by one and increases two edge labels by one, without changing the degrees. It was shown in [5, Lemma 3] that from any valid encoding, one could obtain a graph (with no defect edges) by applying a sequence of at most three switches. In [5, Lemma 4] we used this fact to bound the ratio |L(Z)|/|Ω(d)| for regular degree sequences. This provided an upper bound for the ﬂow f(e) through a transition e = (Z,Z ) (as in Lemma 3.3, above).

The proof of [5, Lemma 3] uses regularity to prove the existence of certain edges which are needed in order

to ﬁnd switches to remove the defect edges. This argument fails for irregular degree sequences. Instead, we consider a slightly more complicated operation than a switch, which we call a 3-switch. (This operation is called a “circular C6-swap” in [8]).

A 3-switch is described by a 6-tuple (a1,b1,a2,b2,a3,b3) of distinct vertices such that a1b1, a2b2, a3b3 are all edges and a2b1, a3b2, a1b3 are all non-edges. The 3-switch deletes the three edges a1b1, a2b2, a3b3 from the edge set and replaces them with a2b1, a3b2, a1b3, as shown in Figure 2.

b1 a2

b1 a2

b2

a1

a1

b2

b3 a3

b3 a3

Figure 2: A 3-switch

Let C(p,q) be the set of encodings in L∗(Z) with precisely p defect edges labelled 2 and precisely q defect edges labelled −1, for p ∈ {0,1,2} and q ∈ {0,1,2,3}. Then Ω(d) = C(0,0) and

L∗(Z) = ∪2p=0 ∪3q=0 C(p,q),

where this union is disjoint. (Note that C(2,3) = ∅, by Lemma 3.1(ii).)

For v ∈ [n], given an encoding L, write NL(v) to denote the set of w ∈ [n] \ {v} such that L(v,w) = 1. This is the set of neighbours of v in L, where neighbours along defect edges are not included. If L ∈ C(p,q) then there are precisely M/2 − 2p + q non-defect edges in L. (To see this, note that the sum of all entries in the matrix L must equal M, and L has zero diagonal.)

Lemma 3.4. Suppose that d satisﬁes dmin ≥ 1 and 3 ≤ dmax ≤ 14

√

M. Let Z ∈ Ω(d). Then

|L∗(Z)| ≤ 51 M6 |Ω(d)|.

Proof. We prove that any L ∈ L∗(Z) can be transformed into an element of Ω(d) (with no defect edges) using a sequence of at most three 3-switches. The strategy is as follows: in Phase 1 we aim to remove two defects per 3-switch (one 2-defect and one (−1)-defect), then in Phase 2 we remove one 2-defect per 3-switch, and ﬁnally in Phase 3 we remove one (−1)-defect per

- 3-switch. There is at most one step in Phase 1, though


the other phases may have more than one step: any phase may be empty. Each 3-switch we perform gives rise to an upper bound on certain ratios of the sizes of the sets C(p,q), by double counting. The proof is completed by combining these bounds. (Such an argument is often called a “switching argument” in the asymptotic enumeration literature: see [17] for example.)

Phase 1. If p + q ≤ 3 then Phase 1 is empty: proceed to Phase 2. Otherwise, suppose that L ∈ C(p,q) where p + q = 4. Then (p,q) ∈ {(2,2), (1,3)}, and it follows from Figure 1 that there must be a vertex b1 which is incident with a 2-defect L(a1,b1) = 2 and a (−1)defect L(a2,b1) = −1. We count the number of 3switches (a1,b1,a2,b2,a3,b3) which may be applied to L to produce an encoding L ∈ Cp−1,q−1. This operation is shown in Figure 3, where defect edges are shown using thicker lines: a thick solid line is a 2-defect edge while a thick dashed line is a (−1)-defect edge.

b1 a2

b1 a2

b2

a1

a1

b2

b3 a3

b3 a3

Figure 3: A 3-switch with L(a1,b1) = 2, L(a2,b1) = −1.

Given (a1,b1,a2), there is at least one vertex b2 ∈ NL(a2) \ {a1}. To see this, ﬁrst suppose that a2 is not incident with a 2-defect. Then NL(a2) has at least da

+ 1 ≥ 2 elements, leaving at least one which is distinct from a1. Otherwise, if a2 is incident with a 2defect then it can be incident with at most one 2-defect, since p ≤ 2. Then there are at least da

2

2 − 2 choices for b2 in NL(a2) \ {a1}, and this number is positive by Lemma 3.2(iii).

Next, we choose (a3,b3) such that all six vertices are distinct, L(a3,b3) = 1 and L(a3,b2) = L(a1,b3) = 0. There are M − 4p + 2q possibilities for (a3,b3) with L(a3,b3) = 1, but we must reject those which are incident with the four vertices already chosen, or which are incident to a neighbour of a1 or b2. We need to be careful with (−1)-defect edges. Hence, for all x ∈ [n], let ηx be the number of (−1)-defect edges other than {a2,b1} which are incident with x in L. Then

x∈[n] ηx ≤ 4 since there are at most two more (−1)defect edges in L. Furthermore, ηa

2 ≤ 3. The

+ ηb

1

number of bad choices for (a3,b3) is at most

 |NL(b1)| +

 .

|NL(x)| +

|NL(y)|

2

x∈NL(a1)

y∈NL(b2)

To see this, note that a2 ∈ NL(b2) so all edges incident with a2 are counted in the ﬁnal sum (with y = a2). Furthermore, for each x ∈ NL(a1), the edge from a1 to x is among those counted by |NL(x)|, so the ﬁrst sum covers all edges incident with a1 or a neighbour of a1 (and similarly for the second sum). Hence the number of bad choices for (a3,b3) is at most

1 − 1 + ηb

- 2 db


1

#### +

(dx + ηx)

x∈NL(a1)

+

(dy + ηy)

y∈NL(b2)

≤ 2 dmax − 1 + ηa

#### + ηb

2

1

2 − 2 + ηa

#### + dmax (da

+ db

#### + ηb

)

1

1

2

+

2ηx

x ∈{a1,b1,a2,b2}

≤ 2 2d2max + 2dmax + 1 . The ﬁnal inequality follows from setting ηa

#### + ηb

#### = 3, the maximum possible, and letting ηx = 1 for some x  ∈ {a1,b1,a2,b2} (as well as bounding da

1

2

by dmax).

#### and db

1

2

Hence, the number of possible 3-switches (a1,b1,a2,b2,a3,b3) such that L(a1,b1) = 2 and L(a1,b3) = −1 is at least

- (3.3) M − 4p + 2q − 2 2d2max + 2dmax + 1 ≥ M − 2 2d2max + 2dmax + 3


≥ M − 6d2max ≥ M/2

√

since 3 ≤ dmax ≤ 14

M. Each such 3-switch produces an encoding L ∈ C(p − 1,q − 1).

Now we consider the reverse of this operation, which is given by reversing the arrow in Figure 3. Given L ∈ C(p − 1,q − 1), we need an upper bound on the number of 6-tuples (a1,b1,a2,b2,a3,b3) such that L (a1,b1) = L (a1,b3) = L (a3,b2) = 1 and L (a2,b1) = L (a2,b2) = L (a3,b3) = 0. Since the encoding L ∈ C(p,q) produced by this reverse operation must be consistent with Z, it follows that {a2,b1} must be an edge of Z. Hence there are precisely M choices for (a2,b1). There are

ways to choose a1 ∈ NL(b1) and at most da

- at most db


#### + ηb

1

1

1 − 1 + ηa

ways to choose b3 ∈ NL(a1) \ {b1}.

1

From Figure 1, if ηa

= 1 then ηa

#### = 2 then ηb

#### = 0, and if ηb

1

1

1

1 ≤ 1. (Otherwise, the reverse switching would produce an encoding which is not valid.) Therefore,

1 ≤ 1. Furthermore, ηb

1 − 1 + ηa

) ≤ dmax (dmax + 1) ≤ 34 d2max.

(db

#### + ηb

)(da

1

1

1

Finally we must choose (a3,b2) such that L(a3,b2) = 1, the vertices a3,b2 are distinct from the four vertices chosen so far and L (a2,b2) = L (a3,b3) = 0. When (p,q) = (2,2) we ignore all conditions except L(a3,b2) = 1, and take

M − 4(p − 1) + 2(q − 1) = M − 2 ≤ M

as an upper bound for the number of good choices of (a3,b2). When (p,q) = (1,3) there are no 2-defects in L , as L ∈ C(0,2), so there are at most

M − 4(p − 1) + 2(q − 1) − (da

#### + db

#### + da

#### + db

) ≤ M − 4p + 2q − 2

1

1

2

3

= M

good choices for (a3,b2). (The existence of any additional (−1)-defect edges incident with a1, b1, a2 or b3 can only help here.) Hence the number of ways to apply the reverse operation to L ∈ C(p − 1,q − 1) to produce a consistent encoding L ∈ C(p,q) is at most 43 d2maxM2.

Combining this with (3.3) shows that whenever p + q = 4, by double counting,

(3.4) |C(p,q)| |C(p − 1,q − 1)|

≤ 38 d2maxM.

Phase 2. Once Phase 1 is complete, we have reached an encoding L ∈ C(p,q) with p+q ≤ 3. If p = 0 then Phase 2 is empty: proceed to Phase 3. Otherwise, we have (p,q) ∈ {(2,1), (2,0), (1,2), (1,1), (1,0)}. We count the number of ways to perform a 3-switch to reduce the number of 2-defect edges by one, as shown in Figure 4.

b1 a2

b1 a2

b2

a1

b2

a1

b3 a3

b3 a3

Figure 4: A 3-switch with L(a1,b1) = 2.

Choose an ordered pair (a1,b1) such that L(a1,b1) = 2, in 2p ways. The number of ways to

choose the ordered pair (a2,b2) such that a1,b1,a2,b2 are all distinct, L(a2,b2) = 1 and L(a2,b1) = 0, is at least

M − 4p + 2q − 2 |NL(a1)| +

|NL(x)|

x∈NL(b1)

≥ M − 4p + 2q − 2 da

1 − 2 + ηa

#### +

(dx + ηx)

2

x∈NL(b1)

≥ M − 2 dmax + 2 + dmax(db

1 − 2 + ηb

ηx

) +

1

x =b1

≥ M − 2 d2max + dmax + 4 ≥ M − 4d2max.

This uses the fact that L may contain up to two (−1)defect edges, so the worst case is when ηb

= 2 and x =b1 ηx = 2.

1

Next, choose an ordered pair (a3,b3) such that all six vertices are distinct, L(a3,b3) = 1 and L(a1,b3) = L(a3,b2) = 0. This can be done in at least M − 4p + 2q

− 2 |NL(b1)| +

|NL(x)| +

|NL(y)|

x∈NL(a1)

y∈NL(b2)

≥ M − 4p + 2q − 2 db

1 − 2 + ηb

1

#### +

(dx + ηx)

x∈NL(a1)

+

(dy + ηy)

y∈NL(b2)

≥ M − 2 dmax + 2 + ηa

#### + ηb

2

1

2 − 2 + ηa

#### + dmax (da

+ db

#### + ηb

)

1

1

2

+

2ηx

x ∈{a1,b1,a2,b2}

- ≥ M − 2 2d2max + 2dmax + 4 ≥ M − 8d2max


ways, arguing as above. (Again, the worst case is when ηa

= 3 and ηx = 1 for some x  ∈ {a1,b1,a2,b2}.) Hence there are at least (3.5) 2 M − 4d2max M − 8d2max ≥ 21M2 such choices for (a1,b1,a2,b2,a3,b3), using the stated upper bound on dmax.

#### + ηb

1

2

For the reverse operation, let L ∈ C(p − 1,q) where (p,q) ∈ {(2,1), (2,0), (1,2), (1,1), (1,0)}. We need an upper bound on the number of 6-tuples

(a1,b1,a2,b2,a3,b3) with L(a1,b1) = L(a1,b3) =

- L(a2,b1) = L(a3,b2) = 1 and L(a2,b2) = L(a3,b3) = 0. There are at most M − 4p + 2q ≤ M choices for (a1,b1) with L(a1,b1) = 1, and then there are at most

(da

1 − 1 + ηa

1

)(db

1 − 1 + ηb

1

) ≤ d2max

choices for (a2,b3). This uses the fact that there are at most two defect edges in L , and hence ηa

1

+ ηb

1 ≤ 2, by choice of (a1,b1). Finally there are at most M − 4p + 2q ≤ M choices for (a3,b2), so the number of 6-tuples where the reverse operation can be performed is at most d2maxM2.

Combining this with (3.5), it follows that

(3.6) |C(p,q)| |C(p − 1,q)|

≤ 2d2max

holds for (p,q) ∈ {(2,1), (2,0), (1,2), (1,1), (1,0)}.

Phase 3. After Phase 2, we may suppose that p = 0. Let L ∈ C(0,q) where q ∈ {1,2,3}. We count the number of 6-tuples (a1,b1,a2,b2,a3,b3) where a 3-switch can be performed with L(a2,b1) = −1. Performing this 3switch will produce L ∈ C(0,q − 1), as illustrated in Figure 5.

a1

b1 a2

b2

b3 a3

a1

b1 a2

b2

b3 a3

Figure 5: A 3-switch with L(a2,b1) = −1.

There are 2q ways to choose (b1,a2), and at least db

1

+ 1 ways to choose a1 ∈ NL(b1). Then there are at least da

2

ways to choose b2 ∈ NL(a2)\{a1}. (Note that the presence of other (−1)-defect edges incident with b1 or a2 only helps here.) Finally, we must choose (a3,b3) with L(a3,b3) = 1 such that all vertices are distinct,

- L(a3,b2) = 0 and L(a1,b3) = 0. The number of choices


for (a3,b3) is at least M + 2q − 2

|NL(x)| +

|NL(y)|

x∈NL(a1)

y∈NL(b2)

≥ M + 2q − 2

(dx + ηx) +

(dy + ηy)

x∈NL(a1)

y∈NL(b2)

≥ M − 2 dmax (2dmax + ηa

) − 1 +

+ ηb

2ηx

1

2

x ∈{a1,b2}

- ≥ M − 2 2d2max + 3dmax + 1 ≥ M − 8d2max.


The penultimate line follows by substituting ηa

+ηb

=

1

2

- 3 and letting ηx = 1 for some x  ∈ {a1,b1,a2,b2}. Hence the number of 3-switches which can be performed in L to reduce the number of 2-defects by exactly one is at least


(M − 8d2max) ≥ 4q(M − 8d2max)

2q(db

+ 1)da

1

2

- (3.7) ≥ 2M,

using the given bounds on dmax.

For the reverse operation, let L ∈ C(0,q − 1), where q ∈ {1,2,3}. We need an upper bound on the number of 6-tuples such that L(a1,b3) = L(a3,b2) = 1, L(a1,b1) = L(b1,a2) = L(a2,b2) = L(a3,b3) = 0 and {a2,b1} is an edge of Z. There are at most M choices for (a2,b1) satisfying the latter condition, then at most M + 2(q − 1) − 2(da

2

+ db

1

) ≤ M ways to choose (a3,b2) with L(a3,b2) = 1 and a1,a3,b2,b3 all distinct. Similarly, there at most M ways to choose (a1,b3). Hence the number of reverse operations is at most M3.

Combining this with (3.7) shows that

- (3.8) |C(0,q)|


≤ 12M2 holds for q ∈ {1,2,3}, by double counting. Consolidation. Deﬁne

|C(0,q − 1)|

B(2,−1) = 83d2maxM, B(2) = 2d2max, B(−1) = 12M2. It follows from (3.4)–(3.8) that

|L∗(Z)| |Ω(d)|

2

3

|C(p,q)| |C(0,0)|

=

p=0

q=0

≤ 1 + B(2) + B(2)2 + B(−1) + B(−1)B(2) + B(−1)B(2)2 B(−1)B(2)B(2,−1) + B(2−1) + B(2−1)B(2)

+ B(2−1) B(2,−1) + B(3−1) ≤ 15M6,

using the upper bound on dmax and the fact that M ≥

144. This completes the proof of Lemma 3.4.

| |
|---|


Since M ≤ dmaxn, the bound 15M6 is at most a factor n/10 bigger than the analogous bound 2d6n5 given in [5, Lemma 4] in the regular case.

Finally we can prove Theorem 1.1.

Proof. (Proof of Theorem 1.1) We wish to apply (2.2). It follows from the conﬁguration model (see [17, Equation (1)]) that the set Ω(d) has size (3.9)

M! 2M/2 (M/2)! nj=1 dj! ≤ exp 12 M log(M) .

|Ω(d)| ≤

Hence the smallest stationary probability π∗ satisﬁes log(1/π∗) = log(|Ω(d)|) ≤ M log(M). Next, (f) ≤ M/2 since each transition along a canonical path replaces an edge of G by an edge of G .

Finally, if e = (Z,Z ) is a transition of the switch chain then 1/Q(e) = 6a(d) ≤ M2, using (2.1). Combining this with Lemmas 3.3 and 3.4 gives ρ(f) ≤ 1 5d14max M8. Substituting these expressions into (2.2) gives the claimed bound on the mixing time.

| |
|---|


### References

- [1] A. Barvinok and J.A. Hartigan, The number of graphs and a random graph with a given degree sequence, Random Structures and Algorithms 42 (2013), 301– 348.
- [2] M. Bayati, J.H. Kim and A. Saberi, A sequential algorithm for generating random graphs, Algorithmica 58 (2010), 860–910.
- [3] J. Besag and P. Cliﬀord, Generalized Monte Carlo signiﬁcance tests, Biometrika 76 (1989), 633–642.
- [4] B. Bolloba´s, A probabilistic proof of an asymptotic formula for the number of labelled regular graphs, European Journal of Combinatorics 1 (1980), 311–316.
- [5] C. Cooper, M.E. Dyer and C. Greenhill, Sampling regular graphs and a peer-to-peer network, Combinatorics, Probability and Computing 16 (2007), 557–593.
- [6] C. Cooper, M.E. Dyer and C. Greenhill, Corrigendum: Sampling regular graphs and a peer-to-peer network. arXiv:1203.6111v1 [math.CO]
- [7] P. Diaconis and B. Sturmfels, Algebraic algorithms for sampling from conditional distributions, The Annals of Statistics 26 (1998), 363–397.
- [8] P.L. Erdo˝s, S.Z. Kiss, I. Miklo´s and L. Soukup, Constructing, sampling and counting graphical realizations of restricted degree sequences, Preprint 2013. arXiv:1301.7523
- [9] C. Greenhill, A polynomial bound on the mixing time of a Markov chain for sampling regular directed graphs, Electronic Journal of Combinatorics 18 (2011), #P234.


- [10] M. Jerrum, Counting, sampling and integrating: algorithms and complexity, Lectures in Mathematics – ETH Zu¨rich, Birkha¨user, Basel, 2003.
- [11] M. Jerrum and A. Sinclair, Fast uniform generation of regular graphs, Theoretical Computer Science 73

(1990), 91–100.

- [12] M. Jerrum, A. Sinclair and B. McKay, When is a graphical sequence stable?, in Random Graphs, Vol. 2 (Pozna´n, 1989), Wiley, New York, 1992, pp. 101–115.
- [13] R. Kannan, P. Tetali and S. Vempala, Simple Markovchain algorithms for generating bipartite graphs and tournaments, Random Structures and Algorithms 14

(1999), 293–308.

- [14] J.H. Kim and V. Vu, Generating random regular graphs, Combinatorica 26 (2006), 683–708.
- [15] B.D. McKay, Subgraphs of dense random graphs with speciﬁed degrees, Combinatorics, Probability and Computing 20 (2011), 413–433.
- [16] B.D. McKay and N.C. Wormald, Uniform generation of random regular graphs of moderate degree, Journal of Algorithms 11 (1990), 52–67.
- [17] B.D. McKay and N.C. Wormald, Asymptotic enumeration by degree sequence of graphs with degrees o(n1/2), Combinatorica 11 (1991), 369–382.
- [18] I. Miklo´s, P.L. Erdo˝s and L. Soukup, Towards random uniform sampling of bipartite graphs with given degree sequence, Electronic Journal of Combinatorics 20(1), 2013, #P16.
- [19] J. Petersen, Die Theorie der regula¨ren graphs, Acta Mathematica 15 (1891), 193–220.
- [20] A.R. Rao, R. Jana and S. Bandyopadhyay, A Markov chain Monte Carlo method for generating random (0,1)-matrices with given marginals, Sankhya¯: The Indian Journal of Statistics 58 (1996), 225–242.
- [21] H.J. Ryser, Combinatorial properties of matrices of zeros and ones, Canadian Journal of Mathematics 9

(1957), 371–377.

- [22] A. Sinclair, Improved bounds for mixing rates of Markov chains and multicommodity ﬂow, Combinatorics, Probability and Computing 1 (1992), 351–370.
- [23] A. Steger and N. Wormald, Generating random regular graphs quickly, Combinatorics, Probability and Computing 8 (1999), 377–396.
- [24] R. Taylor, Constrained switching in graphs, in Combinatorial Mathematics VIII, Springer Lecture Notes in Mathematics vol. 884, 1981, pp.314–336.
- [25] J.Y. Zhao, Expand and Contract: Sampling graphs with given degrees and other combinatorial families, Preprint, 2013. arXiv:1308.6627 [cs.DS]


