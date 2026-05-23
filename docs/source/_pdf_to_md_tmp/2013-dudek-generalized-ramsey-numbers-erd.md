# arXiv:1309.4521v1[math.CO]18Sep2013

## On generalized Ramsey numbers of Erdo˝s and Rogers

Andrzej Dudek∗

Department of Mathematics Western Michigan University Kalamazoo, MI

andrzej.dudek@wmich.edu

Troy Retter

Department of Mathematics and Computer Science Emory University Atlanta, GA

tretter@emory.edu

Vojteˇch R¨odl†

Department of Mathematics and Computer Science Emory University Atlanta, GA

rodl@mathcs.emory.edu

September 10, 2021

Abstract

Extending the concept of Ramsey numbers, Erd˝s and Rogers introduced the following function. For given integers 2 ≤ s < t let

fs,t(n) = min{max{|W| : W ⊆ V (G) and G[W] contains no Ks}},

where the minimum is taken over all Kt-free graphs G of order n. In this paper, we show that for every s ≥ 3 there exist constants c1 = c1(s) and c2 = c2(s) such that fs,s+1(n) ≤ c1(log n)c

√n. This result is best possible up to a polylogarithmic factor. We also show for all t − 2 ≥ s ≥ 4, there exists a constant c3 such that fs,t(n) ≤ c3√n. In doing so, we partially answer a question of Erd˝s by showing that limn→∞ fsf+1,s+2(n)

2

s,s+2(n) = ∞ for any s ≥ 4.

### 1 Introduction

In a graph G, a set S ⊆ V (G) is independent if G[S] does not contain a copy of K2. More generally for any integer s, a set S ⊆ V (G) can be called s-independent if G[S] does not contain a copy of Ks. With this in mind, deﬁne the s-independence number of G, denoted by αs(G), to be the size of the largest s-independent set in G. The classical Ramsey number R(t,u) can be deﬁned in this language as the smallest integer n such that every graph of

∗Supported in part by Simons Foundation Grant #244712. †Supported in part by NSF grant DMS 0800070.

order n contains either a copy of Kt or a 2-independent set of size u. In other words, R(t,u) is the smallest integer n such that

u ≤ min{α2(G) : G is a Kt-free graph of order n}.

Observe that if the right hand side of the above inequality is understood as a function of n and t, then so is the classical Ramsey number.

A more general problem results by replacing the standard independence number by the s-independence number for some 2 ≤ s < t. Following this approach, in 1962 Erd˝s and Rogers [10] introduced the function

fs,t(n) = min{αs(G) : G is a Kt-free graph of order n}.

The lower bound k ≤ fs,t(n) means that every Kt-free graph of order n contains a subset of k vertices with no copy of Ks. The upper bound fs,t(n) < means that there exists a Kt-free graph of order n such that every subset of vertices contains a copy of Ks.

The case t = s + 1 has received the considerable attention over the last 50 years, in part due to the fact that it creates a general upper bound in the sense that for t > t, we clearly have fs,t (n) ≤ fs,t(n). A ﬁrst nontrivial upper bound for fs,s+1(n) was established by Erd˝s and Rogers [10], which was subsequently addressed by Bollob´s and Hind [4], Krivelevich [12, 13], Alon and Krivelevich [2], Dudek and R¨dl [7], and most recently Wolfovitz [17]. The ﬁrst nontrivial lower bound established by Bollob´s and Hind [4] was later slightly improved by Krivelevich [13]. The most recent general bounds for s ≥ 3 were of the form:

nlog n log log n

= fs,s+1(n) = O n23 . (1)

Ω

The precise lower bound of (1) was ﬁrst explicitly stated by Dudek and Mubayi [6], and was based upon their observation that the result of Krivelevich [13] could be slightly strengthened by incorporating a result of Shearer [14]. This upper bound of (1) appears in [7], where it was also conjectured that for all suﬃciently large s the upper bound could be improved to show that

fs,s+1(n) = n21+o(1). (2) Recently, Wolfovitz [17] showed that (2) holds when s = 3. In this paper, (2) is proved for every s ≥ 3, establishing an upper bound that is tight up to a polylogarithmic factor. Our proof builds upon the ideas in [17], [7], [12], and [13].

- Theorem 1.1 For every s ≥ 3 there is a constant c = c(s) such that


fs,s+1(n) ≤ c(log n)4s2√n.

For the case t = s + 2, it follows from a result of Sudakov [15] (see also [7] for a simpliﬁed formula) that fs,s+2(n) = Ω(na2), where a1

##### = 2 + 3s2−4. On the other hand, clearly fs,s+2(n) ≤ fs,s+1(n). When s ≥ 4, we establish an improved upper bound that omits the logarithmic factor.

2

- Theorem 1.2 For every s ≥ 4 there is a constant c = c(s) such that fs,s+2(n) ≤ c√n.


This establishes the following corollary which provides the best known bounds on fs,t(n) for t < 2s.

Corollary 1.3 For every 6 ≤ s + 2 ≤ t there is a constant c = c(s) such that

fs,t(n) ≤ fs,s+2(n) ≤ c√n.

When t ≥ 2s, the upper bound c(log n)1/(s−1)ns/(t+1) of Krivelevich [12] remains best. For all values of t > s + 1, the best lower bounds follow from a recursive formula deﬁned by Sudakov [15, 16]. We will return to the these results concerning the general case in our concluding remarks. More related results are summarized in the survey [8].

Now that our two main results have been stated, we turn our attention towards an old question of Erd˝s [9], who asked if for ﬁxed integers s + 1 < t,

fs+1,t(n) fs,t(n)

= ∞. (3)

lim

n→∞

This central conjecture in the area is still wide open and asks for a rather precise estimation of fs,t(n). It is known due to Sudakov [16] that (3) holds for

(s,t) ∈ {(2,4),(2,5),(2,6),(2,7),(2,8),(3,6)}.

Observe that Theorem 1.2 together with the lower bound of [13] (and [7]) implies that for s ≥ 4,

Ω log lognlognn O(√n)

fs+1,s+2(n) fs,s+2(n) ≥

log n log log n −−−→

∞.

= Ω

n→∞

That is, (3) holds for all pairs (s,t) ∈ {(4,6),(5,7),(6,8),...}.

In what follows, consider s to be an arbitrary ﬁxed integer and n suﬃciently large, i.e. n ≥ n0(s). We will show that there exists a Ks+1-free graph of order n such that every subset of c(log n)4s2√n vertices contains a copy of Ks and that there exists a Ks+2-free graph of order n such that every subset of c√n vertices contains a copy of Ks. Indeed, this establishes Theorems 1.1 and 1.2 as stated (for all n), since the constant factors can subsequently be inﬂated to accommodate the ﬁnitely many cases where n ≤ n0. For simplicity, we do not round numbers that are supposed to be integers either up or down; this is justiﬁed since these rounding errors are negligible to the asymptomatic calculations we will make.

In Section 2, we begin our construction by considering the random hypergraph H which is essentially the random hypergraph obtained from the aﬃne plane by taking each hyperedge (line) with some uniform probability. We then use H in Section 3 to construct a random graph G by replacing each hyperedge by a complete s-partite graph. In Section 4, the proof of Theorem 1.2 considers an induced subgraph of G whereas the proof of Theorem 1.1 considers yet another random subgraph of G which is analyzed by way of the Local Lemma.

Below we will use the standard notation to denote the neighborhood and degree of v ∈ G by NG(v) and dG(v) respectively.

### 2 The Hypergraph H

The aﬃne plane of order q is an incidence structure on a set of q2 points and a set of q2 +q lines such that: any two points lie on a unique line; every line contains q points; and every point lies on q + 1 lines. It is well known that aﬃne planes exist for all prime power orders. Clearly, an incidence structure can be viewed as a hypergraph with points corresponding to vertices and lines corresponding to hyperedges; we will use this terminology interchangeably.

In the aﬃne plane, call lines L and L parallel if L ∩ L = ∅. In the aﬃne plane there exist q +1 sets of q pairwise parallel lines. (For more details see, e.g., [5].) Let (V,L) be the hypergraph obtained by removing a parallel class of q lines from the aﬃne plane or order q. The following lemma establishes some properties of this graph.

- Lemma 2.1 For q prime, the q-uniform, q-regular hypergraph (V,L) of order q2 satisﬁes:


- (P1) Any two vertices are contained in at most one hyperedge;
- (P2) For every A ∈ Vq , |{L ∈ L : L ∩ A = ∅}| ≥ q22.


Proof. By construction, (V,L) is q-uniform, q-regular, and satisﬁes (P1). Consider A = {v1,v2,...,vq}. Deﬁne d+(vi) = |{L ∈ L : L ∩ {v1,v2,...,vi} = {vi}}|. Hence by property (P1), d+(vi) ≥ q − i + 1. We now compute

q

q2 2

q + 1 2 ≥

|{L ∈ L : L ∩ A = ∅}| ≥

d+(vi) ≥

.

i=1

| |
|---|


The objective of this section is to establish the existence of a certain hypergraph (V,L ) ⊆ (V,L) by considering a random sub-hypergraph of (V,L). Preceding this, we introduce some terminology. Deﬁne

L A = {L ∈ L : L ∩ A = ∅}, and L B,γ = {L ∈ L : |L ∩ B| ≥ γ}.

Call S ⊆ V L -complete if every pair of points in S is contained in some common line in L . Let L(x,y) denote the unique line in L containing x and y, provided such a line exists.

We will now distinguish 3 types of L -dangerous subsets as depicted in Figure 1. The ﬁrst two types have 5 vertices {v1,v2,v3,v4,x} and third type has 6 vertices {v1,v2,v3,v4,y,z}. All 3 types of dangerous sets must be L -complete and have 4 points {v1,v2,v3,v4} in general position. Additionally we specify:

- Type 1 L -dangerous The points {v1,v2,v3,v4,x} are in general position.
- Type 2 L -dangerous The point x is contained in precisely one of the 6 lines L(vi,vj) for 1 ≤ i < j ≤ 4. Up to relabeling, say x ∈ L(v2,v3).


![image 1](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile1.png>)

![image 2](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile2.png>)

![image 3](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile3.png>)

![image 4](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile4.png>)

![image 5](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile5.png>)

![image 6](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile6.png>)

![image 7](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile7.png>)

![image 8](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile8.png>)

![image 9](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile9.png>)

![image 10](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile10.png>)

![image 11](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile11.png>)

![image 12](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile12.png>)

![image 13](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile13.png>)

![image 14](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile14.png>)

![image 15](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile15.png>)

![image 16](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile16.png>)

(a) Type 1 (b) Type 2 (c) Type 3

Figure 1: Types of dangerous sets.

- Type 3 L -dangerous The points y and z are each contained in exactly two of the lines L(vi,vj) for 1 ≤ i < j ≤ 4. Up to relabeling, say y ∈ L(v1,v3) ∩ L(v2,v4) and z ∈ L(v1,v2) ∩ L(v3,v4).


All concepts above were deﬁned relative to the subset L ⊆ L. Obviously we can deﬁne the concepts L-complete, L-dangerous, LA, and LB,γ related to the set L analogously.

We are now ready to state the main result of this section.

- Lemma 2.2 Let q be a suﬃciently large prime and α = (log q)2. Then, there exists a q-uniform hypergraph H = (V,L ) of order q2 such that:


- (H1) Any two vertices are contained in at most one hyperedge;
- (H2) For every v ∈ V , dH(v) ≤ 2α;
- (H3) |D| ≤ 2α8q, where D is the set of L -dangerous subsets;
- (H4) For every A ∈ Vq , |L A| ≥ αq4 ;

- (H5) For every integer 1 ≤ γ ≤ 16q and every B ∈ 16 Vγq , |L B,γ| ≥ αq8 .


Before proving the above lemma, we state a basic form of the Chernoﬀ bound (as appearing in Corollary 2.3 of [11]) and mention what we will refer to as the union bound. Chernoﬀ Bound If X ∼ Bi(n,p) and 0 < ε ≤ 32, then

E(X)ε2 3

Pr |X − E(X)| ≥ ε · E(X) ≤ 2exp −

.

Union Bound If Ei are events, then

Pr

k

Ei ≤ k · max{Pr(Ei) : i ∈ [k]}.

i=1

Proof of Lemma 2.2. Take (V,L) to be a hypergraph established by Lemma 2.1. Let H = (V,L ) be a random sub-hypergraph of (V,L) where every line in L is taken independently with probability

(log q)2 q

α q

=

.

Since H is a subgraph of (V,L) any two vertices are in at most one line, so H always satisﬁes (H1). We will show H fails to satisfy (H2) and (H4) with probability at most o(1) and that H fails to satisfy (H3) with probability at most 12. Together this implies H satisﬁes (H1)-

- (H4) with probability at least 1 − 12 − o(1), establishing the existence of a hypergraph H that satisﬁes (H1)-(H4). Finally, we use a counting argument to show that any such H necessarily satisﬁes (H5).


(H2): We ﬁrst show that the probability that there exists a vertex of degree greater

than 2α is o(1). Observe for ﬁxed v ∈ H, dH(v) ∼ Bi(q, αq ) and E(dH(v)) = α. So by the Chernoﬀ bound with ε = 1,

α 3

Pr dH(v) ≥ 2α ≤ Pr |dH(v) − α| ≥ α ≤ 2exp −

.

Thus by the union bound the probability that there exists some v ∈ V with dH(v) ≥ 2α is at most

(log q)2 3

α 3

q2 · 2exp −

= 2exp 2log q −

= o(1).

(H3): In order to show |D| > 4α8q with probability at most 21, we begin by counting the number of L-dangerous subsets of each type. Clearly the number of Type 1 L-dangerous subsets is at most q52 . To count the number of Type 2 L-dangerous subsets, ﬁrst choose {v1,v2,v3,v4} then x, observing x must lie on one of the 6 lines which each have at most q vertices. Thus there are at most q42 (6q) conﬁgurations of this type. To count the number of Type 3 L-dangerous subsets, observe the lines L(vi,vj) for 1 ≤ i < j ≤ 6 intersect at at most 3 points other than v1,v2,v3,v4. Hence there are at most q42 32 subsets of this type in L.

Since L-dangerous subsets of Type 1, Type 2, and Type 3 have 10, 8, and 7 lines respectively, an L-dangerous subset of each type will be L -dangerous with respective probabilities

10

8

7

α q

, αq

, and αq

. By the linearity of expectation, we now compute

10

8

7

q2 5 ·

q2 4

q2 4

qα8 4

qα7

α q

α q

3 2 ·

α q

≤ α10 +

8 ≤ qα8. Thus, the Markov inequality yields,

E(|D|) ≤

(6q)·

+

+

+

- 1

- 2


Pr |D| ≥ 2α8q ≤ Pr |D| ≥ 2E(|D|) ≤

.

(H4): We will now prove that the probability that there exists A ∈ Vq such that |L A| < αq4 is o(1). Begin by considering any ﬁxed A ∈ Vq . Then by Lemma 2.1, |LA| ≥ q22,

so we may ﬁx X ⊆ LA with |X| = q22. Let X = X ∩ L . Since each line in X appears in X independently with probability αq , |X | ∼ Bi(q22, αq ) and E(|X |) = αq2 . Hence by the Chernoﬀ bound with ε = 12,

αq 2 ≥

αq 4 ≤ Pr |X | <

αq 4 ≤ Pr |X | −

Pr |L A| <

αq 4 ≤ 2exp −

αq 24

.

Consequently by the union bound, the probability that there exits some A ⊆ V , |A| = q, with |L A| < αq4 is at most

q2 q · 2exp −

(log q)2q 24

αq 24 ≤ q2q · 2exp −

q(log q)2 24

= 2exp 2q log q −

= o(1).

(H5): Finally, we will establish the following deterministic property: If H satisﬁes (H2) and (H4), then H also satisﬁes (H5).

Consider arbitrary ﬁxed 0 ≤ γ ≤ 16q and B ∈ 16 Vγq . Let B = B1 ∪ B2 ∪ ··· ∪ B16γ be a partition of B into 16γ sets of size q. Consider the auxiliary bipartite graph Aux with bipartition {B1,B2,...,B16γ} ∪ L . Join Bi to L ∈ L if Bi ∩ L = ∅. By property (H4) dAux(Bi) ≥ αq4 for all i ∈ [16γ], and thus the number of edges in Aux satisﬁes

αq

|e(Aux)| ≥

4 |{B1,B2,...,B16γ}| = 4αqγ. (4) On the other hand, clearly dAux(L) ≤ |{B1,B2,...,B16γ}| = 16γ for all L ∈ L and by deﬁnition dAux(L ) ≤ γ for all L ∈ {L \ L B,γ}. Also keeping in mind that by (H2) |L \ L B,γ| ≤ |L | = v∈V dHq(v) ≤ q22qα = 2αq, we compute

|e(Aux)| ≤ |L B,γ| · 16γ + |{L \ L B,γ}| · γ ≤ |L B,γ| · 16γ + 2αq · γ. (5) Comparing (4) and (5), we obtain

4αqγ ≤ |e(Aux)| ≤ |L B,γ| · 16γ + 2αqγ, which yields |L B,γ| ≥ αq8 .

| |
|---|


### 3 The Graph G

Based upon the hypergraph H established in the previous section, we will construct a graph G with the following properties.

Lemma 3.1 Let q be a suﬃciently large prime, α = (log q)2, β = (log q)4s2, and s ≥ 3. Then, there exists a graph G = (V,E) of order q2 such that:

- (G1) For every C ∈ 16 Vsq , G[C] contains a copy of Ks;


- (G2) For every U ∈ 64 Vsβq , G[U] contains αβ162q edge disjoint copies of Ks;

- (G3) Every edge xy ∈ E is in at most 6sα2s−2 copies of Ks+1;
- (G4) If s ≥ 4, then G can be made Ks+2 free by removing 2α8q vertices.


Proof. Fix a hypergraph H = (V,L ) as established by Lemma 2.2. Construct the random graph G as follows. For every L ∈ L , let χL : L → [s] be a random partition of the vertices of L into s classes, where for every v ∈ L, a class χL(v) ∈ [s] is assigned uniformly and independently at random. Then, let xy ∈ E if {x,y} ⊆ L for some L ∈ L and χL(x) = χL(y). Thus for every L ∈ L , G[L] is a complete s-partite graph with vertex partition L = χ−L1(1) ∪ χ−L1(2) ∪ ··· ∪ χ−L1(s) (where the classes need not have the same size and the unlikely event that a class is empty is permitted). Observe that not only are GH [L] and GH [L ] are edge disjoint for distinct L,L ∈ L , but also that the partitions for L and L were determined independently.

We will show G does not satisfy (G1) and (G2) with probability at most o(1) and that G always satisﬁes (G3) and (G4). Hence the probability that G satisﬁes properties (G1)-(G4) is at least 1 − o(1), implying the existence of a graph G described in the lemma.

(G1): Consider any C ∈ 16 Vsq . We will bound the probability that G[C]  ⊃ Ks. By

- (H5) with γ = s, the set of lines L C,s that intersect C in at least s vertices has cardinality |L C,s| ≥ αq8 . For each L ∈ L C,s, let XL be the event Ks  ⊆ G[L ∩ C]. Since |L ∩ C| ≥ s for all L ∈ L C,s, Pr(XL) ≤ 1 − sss! . By independence,


αq 8

|L C,s|

αq 8

s! ss

s! ss

s! ss

Pr Ks  ∈ G[C] ≤ Pr

XL ≤ 1 −

≤ 1 −

≤ exp −

.

L∈L C,s

So by the union bound, the probability that there exists a subset of 16sq vertices in G that contains no Ks is at most

q2 16sq

s! ss

exp −

αq 8 ≤ q16sq exp −

s! ss

αq 8

s!q(log q)2 8ss

= exp 16sq log q −

= o(1).

(G2): For arbitrary U ∈ 64 Vsβq , we will bound the probability that G[U] does not contain αβ162q edge disjoint copies of Ks. By (H5) with γ = 4sβ, we may ﬁx a subset ZU ⊆ L U,4sβ of exactly αq8 lines with the property that each line has intersection at least 4sβ with U. We will consider the lines in ZU that contain the complete balanced s-partite graph on 2sβ vertices, which we denote by K2β,...,2β. Deﬁne Z U = {L ∈ ZU : K2β,...,2β ⊆ G[L∩U]}. The graph K2β,...,2β certainly contains at least β2 edge disjoint Ks (Since we may choose a prime β ≤ p ≤ 2β and it follows from [1] that we may then decompose Kp,...,p into p2 edge disjoint copies of Ks; this suﬃces for our purposes, but stronger results are know). Thus if we show |Z U| ≥ αq16 it will imply that G[U] contains at least |Z U| · β2 ≥ αβ162q edge disjoint copies of Ks.

For L ∈ ZU, let YL be the event that L  ∈ Z U and ﬁx L4sβ ⊆ L ∩ U,|L4sβ| = 4sβ. Now YL will occur only if |χ−L1(i) ∩ L4sβ| < 2β for some i ∈ [s]. Deﬁning Xi = |χ−L1(i) ∩ L4sβ|, observe Xi ∼ Bi(4sβ, 1s) and E(Xi) = 4β. Chernoﬀ’s inequality reveals

β 3

E(Xi) 2 ≤ 2exp −

4β 12

= 2exp −

Pr Xi < 2β ≤ Pr |Xi − E(Xi)| ≥

.

By the union bound, Pr(YL) ≤ Pr i∈s(Xi ≤ 2β) ≤ s · 2exp −β3 .

By independence, the probability that YL occurs for at least αq16 = |Z2U| of the lines in ZU is at most

|ZU| |ZU| 2

β 3

2sexp −

|ZU|/2

β 3

≤ 4|ZU|/2 2sexp −

|ZU|/2

β 3

= 8sexp −

αq 16

.

αq

That is, we have shown |Z U| < αq16 with probability at most 8sexp −β3

16 for ﬁxed U. Thus by the union bound, the probability that there exits some U ⊆ V with |U| = 64sβq such that |Z U| < αq16 is at most

αq 16

αq 16

q2 64sβq

β 3

β 3

αq

≤ q64sβq(8s)

8sexp −

16 exp −

![image 17](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile17.png>)

αq 16

αβq 48

≤ exp 64sβq log q +

log(8s) −

= o(1).

(G3): For any xy ∈ E, we will show the number of copies of Ks+1 that contain xy is at most 6sα2s−2. Let L ∈ L be the unique line such that {x,y} ⊆ L as depicted in Figure 2.

![image 18](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile18.png>)

![image 19](<2013-dudek-generalized-ramsey-numbers-erd_images/imageFile19.png>)

#### L

Figure 2: Counting Ks+1 in G that contains a ﬁxed edge xy by considering lines in H.

Let N = (NH(x)∩NH(y))\L be the set of all vertices not on L that are collinear with both x and y. Since dH(x),dH(y) ≤ 2α by (H2), we infer that |N| ≤ 4α2. Because Ks+1  ⊆ G[L], if a Ks+1 is to contain x and y it must contain at least one vertex v ∈ N. There are at most |N| ≤ 4α2 choices for this vertex v. Once v has been chosen, each of the remaining s − 2

vertices of the Ks+1 must lie in N or in L ∩ NH(v). Since |N| + |L ∩ NH(v)| ≤ 4α2 + 2α, the number of Ks+1 containing the edge xy is at most 4α2(4α2 + 2α)s−2 ≤ 6sα2s−2.

(G4): We will ﬁnally show that if s ≥ 4, G can be made Ks+2 free be removing at most 2α8q vertices. By (H3), all L -dangerous sets can be destroyed by removing 2α8q vertices, so it suﬃces to shown that every Ks+2 in G contains a L -dangerous subset.

Let K be any copy of Ks+2 in G. By assumption s ≥ 4, so K must have at least 6 vertices, which clearly form a L -complete set.

We ﬁrst show that K contains 4 vertices in general position. Suppose otherwise. Then there is some line L ∈ L that contains 3 vertices {p1,p2,p3} of K. Since Ks+1  ⊆ G[L], there must exist two vertices a and b in K \ L. Observe {a,b} and any 2 vertices in {p1,p2,p3} \ L(a,b) are in general position.

Now ﬁx 4 vertices {v1,v2,v3,v4} of K that are in general position and let u1,u2 be any two other vertices of K. Three cases are now considered. If either u1 or u2 do not lie on any of the 6 lines L(vi,vj) for 1 ≤ i < j ≤ 4, then there is a L -dangerous subset of Type 1. If either u1 or u2 lie on exactly one line in L(vi,vj) for 1 ≤ i < j ≤ 4, then there is a L -dangerous subset of Type 2. In the remaining case where both u1 and u2 each lie on at least 2 lines in L(vi,vj) for 1 ≤ i < j ≤ 4, then there is a L -dangerous subset of Type 3.

| |
|---|


### 4 Proof of Theorem 1.1 and 1.2

Consider any suﬃciently large integer n and s ≥ 3. By Bertrand’s postulate, we can ﬁnd a prime q such that 4n ≤ q2 ≤ 16n. Fix a graph G procured by Lemma 3.1 of order q2 and as before take

α = (log q)2 and β = (log q)4s2.

Theorem 1.1 and Theorem 1.2 are now proved by considering diﬀerent subgraphs of G of order n.

Proof of Theorem 1.2. Consider the case where s ≥ 4. To prove the theorem, we will show there exists a Ks+2-free induced subgraph of G of order n with the property that every subset of order 64s√n contains a copy of Ks.

By (G1), every set of size 16sq in G contains Ks, so certainly every subset of size 64s√n ≥ 16sq in any induced subgraph of G must also contain a copy of Ks. Thus it will suﬃce to show that there is a Ks+2-free subset of G of order n. But by (G4), we know that there is a set R ⊆ V (G) of size |R| = 2α8q ≤ n such that G[V \ R] will be Ks+2-free. Finally since |V \ R| ≥ 4n − n ≥ n, the induced graph of G on any n vertices in V \ R will have the desired properties.

| |
|---|


Proof of Theorem 1.1. For s ≥ 3, we will concentrate on constructing a Ks+1-free graph G on q2 vertices with the property that every subset of size 64sβq vertices contains a copy of Ks. Since log(4n) ≤ 2log n,

64sβq = 64s(log q)4s2q ≤ 64s(log 4n)4s24n ≤ 24s2+8(log n)4s2n,

and so any induced subgraph of G of order n will also be Ks+1-free and have the property that every set of order 24s2+8(log n)4s2n contains a copy of Ks, exactly as desired.

Let G be a random subgraph of G where each edge is taken with probability

1 γ

, where γ = (log q)8.

For a set S ∈ Vs+1(G) that spans a copy of Ks+1 in G, let AS to be the event that all the edges of S are in G . Hence, AS means that Ks+1  ⊆ G . For a set U ∈ 64 V (sβqG) let KU be a (ﬁxed) set of

1 16

αβ2q

m =

edge disjoint copies Ks contained in U, which are known to exist by (G2). Deﬁne BU to be the event that none of the m edge disjoint Ks appear in G . Hence, BU implies that for every U ∈ 64 V (sβqG) one of the disjoint copies of Ks in G[U] appears in G . It will suﬃce to show that the probability that AS ∩ BU occurs is nonzero. In order to show this, we apply the Local Lemma (see, e.g., Lemma 5.1.1 in [3]).

Lova´sz Local Lemma Let E1,E2,...,Ek be events in an arbitrary probability space. A directed graph D on the set of vertices {1,2,...,k} is called a dependency digraph for the

events E1,E2,...,Ek if for each i, 1 ≤ i ≤ k, the event Ei is mutually independent of all the events {Ej : (i,j)  ∈ D}. Suppose that D is a dependency digraph for the above events and suppose there are real numbers z1,...,zk such that 0 ≤ zi < 1 and Pr(Ei) ≤ zi (i,j)∈D(1 − zj) for all 1 ≤ i ≤ k. Then, Pr ki=1 Ei > 0.

Let D be a dependency graph that corresponds to all events AS and BU. Observe that AS depends only on the s+12 edges in S and BU depends only on the m 2 s edges of the Ks in KU. Also, observe that the number of events of the type BU is 64 qsβq2 ≤ q64sβq. Thus by (G3), a ﬁxed event AS depends on at most

dAA =

s + 1 2

6sα2s−2

other events AS and at most

dAB = q64sβq events BU. Similarly, a ﬁxed event BU depends on at most

dBA = m

s 2

6sα2s−2

events AS and at most

dBB = q64sβq other events BU . Let

1 α2s2

1 (log q)4s2q64sβq

x =

and y =

.

To ﬁnish the proof, due to the Local Lemma it suﬃces to show that

(s+12 )

1 γ

≤ x(1 − x)dAA(1 − y)dAB, (6)

(2s) m

1 γ

≤ y(1 − x)dBA(1 − y)dBB. (7)

1 −

First we show that (6) holds. Using the fact that e−2x ≤ 1 − x for x suﬃciently small (observe that x → 0 with q → ∞), a suﬃcient condition for (6) will be

(s+12 )

1 γ

≤ xe−2xdAA e−2ydAB, and equivalently,

s + 1 2

1 x

log (γ) ≥ log

+ 2xdAA + 2ydAB.

The latter immediately follows from the following three inequalities (which can be easily veriﬁed):

2s2 2s2 + 2s

s + 1 2

1 x

log (γ) ≥ log

, s 2s2 + 2s

s + 1 2

log (γ) ≥ 2xdAA, s 2s2 + 2s

s + 1 2

log (γ) ≥ 2ydAB.

e−

Similarly, using the facts that e−2y ≤ 1−y for y suﬃciently small and that 1− γ 1

(2s)

1 γ

, (7) will be satisﬁed if

(2s)

≤

(2s)

1 γ

e−m

≤ y e−2xdBA e−2ydBB, and equivalently,

(2s)

1 γ

1 y

≥ log

m

+ 2xdBA + 2ydBB. As before the latter will follow from the following easy to check inequalities:

1 3

m

1 3

m

1 3

m

1 γ

1 γ

1 γ

(2s)

1 y

≥ log

(2s)

≥ 2xdBA,

(2s)

≥ 2ydBB.

,

This completes the proof of Theorem 1.1.

| |
|---|


### 5 Concluding Remarks

We close this paper by discussing how the asymptotic behavior of fs,t(n) changes for diﬀerent values of 3 ≤ s < t.

If the diﬀerence between s and t is ﬁxed, we make the following observation based upon the lower bound in Sudakov [15] (and Fact 3.5 in [7]) and Corollary 1.3. Observation 5.1 For any ε > 0 and an integer k ≥ 2 there is a constant s0 = s0(k,ε) such that for all s ≥ s0,

Ω n12−ε = fs,s+k(n) = O(√n). In view of this observation and Theorem 1.2 we ask the following. Question 5.2 For any s ≥ 3, is fs,s+2(n) = o(√n)?

Another interesting question results from ﬁxing that ratio between s and t. The following is based upon [15] and [12] respectively. Observation 5.3 For any ε > 0 and λ ≥ 2 there is a constant s0 = s0(λ,ε) such that for all s ≥ s0,

Ω n21λ−ε = fs, λs (n) = O nλ1 . In particular, when λ = 3, we see Ω(n1/6−ε) = fs, λs (n) = O(n1/3).

- Question 5.4 What is the asymptotic behavior of fs, λs (n)? Recall that Erd˝s [9] asked if for ﬁxed s + 2 ≤ t, limn→∞ fsf+1,t(n)

s,t(n) = ∞. We ask a similar question, that if answered in the aﬃrmative would imply an aﬃrmative answer to the question of Erd˝s.

- Question 5.5 For all t > s ≥ 3, is limn→∞ fs+1f ,t+1(n)


s,t(n) = ∞?

### References

- [1] R. Abel, C. Colbourn, and J. Dinitz. Mutually orthogonal Latin squares (MOLS), In C. Colbourn and J. Dinitz, eds., Handbook of Combinatorial Designs, chap. III.3, pp. 160–193. Chapman & Hall, 2nd ed., 2007.
- [2] N. Alon and M. Krivelevich, Constructive bounds for a Ramsey-type problem, Graphs Combin. 13 (1997), 217–225.
- [3] N. Alon and J. Spencer, The Probabilistic Method, third ed., John Wiley & Sons Inc., 2008.


- [4] B. Bollob´as and H. Hind, Graphs without large triangle free subgraphs, Discrete Math. 87 (1991), no. 2, 119–131.
- [5] P. Cameron, Combinatorics: Topics, Techniques, Algorithms, Cambridge University Press, Cambridge, 1994.
- [6] A. Dudek and D. Mubayi, On generalized Ramsey numbers for 3-uniform hypergraphs, submitted.
- [7] A. Dudek and V. R¨dl, On Ks-free subgraphs in Ks+k-free graphs and vertex Folkman numbers, Combinatorica 31 (2011), 39–53.
- [8] A. Dudek and V. R¨dl, On the function of Erd˝os and Rogers, in Ramsey Theory: Yesterday, Today and Tomorrow, edited by A. Soifer, Progress in Mathematics, vol. 285, Springer-Birkh¨user, 2010, pp. 63–76.
- [9] P. Erd˝s, Some of my recent problems in combinatorial number theory, geometry and combinatorics, in: Graph theory, combinatorics, and algorithms, Vol. 1, 2, Wiley, New York, 1995, 335–349.
- [10] P. Erd˝s and C. Rogers, The construction of certain graphs, Canad. J. Math. 14 (1962), 702–707.
- [11] S. Janson, T.  Luczak, and A. Rucin´ski, Random Graphs, Wiley, New York, 2000.
- [12] M. Krivelevich, Bounding Ramsey numbers through large deviation inequalities, Random Structures Algorithms 7 (1995), 145–155.
- [13] M. Krivelevich, Ks-free graphs without large Kr-free subgraphs, Combin. Probab. Comput. 3 (1994), 349–354.
- [14] J. B. Shearer, On the independence number of sparse gaphs, Random Structures Algorithms 7 (1995), 269-271.
- [15] B. Sudakov, Large Kr-free subgraphs in Ks-free graphs and some other Ramsey-type problems, Random Structures Algorithms 26 (2005), 253-265.
- [16] B. Sudakov, A new lower bound for a Ramsey-type problem, Combinatorica 25 (2005), 487–498.
- [17] G. Wolfovitz, K4-free graphs without large induced triangle-free subgraphs, to appear in Combinatorica.


