arXiv:1202.5337v2[math.CO]29Sep2012

Nondeterministic graph property testing

La´szlo´ Lova´sz Katalin Vesztergombi Institute of Mathematics, Eo¨tv¨os Lor´and University Budapest, Hungary

October 31, 2018

Abstract

A property of ﬁnite graphs is called nondeterministically testable if it has a “certiﬁcate” such that once the certiﬁcate is speciﬁed, its correctness can be veriﬁed by random local testing. In this paper we study certiﬁcates that consist of one or more unary and/or binary relations on the nodes, in the case of dense graphs. Using the theory of graph limits, we prove that nondeterministically testable properties are also deterministically testable.

# 1 Introduction

Let P be a property of ﬁnite simple graphs (i.e., a class of ﬁnite simple graphs closed under isomorphism). We say that P is testable, if there exists another property T (called a test property) satisfying the following conditions:

- • if a graph G has property P, then for all 1 ≤ r ≤ |V (G)|, a random induced subgraph on r nodes (chosen uniformly among all such induced subgraphs) has property T with probability at least 2/3, and
- • for every ε > 0 there is an rε ≥ 1 such that if G is a graph whose edit distance from P is at least ε|V (G)|2, then for all rε ≤ r ≤ |V (G)|, a random induced subgraph on r nodes has property T with probability at most 1/3.


This notion of testability is often called oblivious testing, which refers to the fact that no information about the size of G is assumed. It is easy to see that if P is a testable property such that arbitrarily large graphs can have the property, then there must exist a graph with property P with any suﬃciently large number of nodes. The deﬁnition extends trivially to graphs whose edges are oriented, and whose nodes and/or edges are colored with a ﬁxed ﬁnite number k of colors.

Testability of graph properties was introduced by Rubinfeld and Sudan [16] and Goldreich, Goldwasser and Ron [11]. There are many graph properties that are known to be testable [11, 1]; (see e.g. [8] for a survey and [10] for a collection of more recent surveys). One surprisingly general suﬃcient condition was found by Alon and Shapira [3]: Every hereditary graph property is testable. (A graph property is called hereditary, if it is inherited by induced subgraphs.)

Various characterizations of testable properties are known [2, 14], but they are not simple to state. The goal of this paper is to prove a characterization, which is useful as a suﬃcient condition in a number of cases.

Let L be a directed graph whose nodes and edges are colored. Let us make some simplifying assumptions that don’t change the results. We assume that every pair of nodes is connected by two, oppositely directed edges. If some edges are missing, we can add them colored with an additional color. If some edges have larger (but bounded) multiplicity, we can use colors to indicate this. Furthermore, we may get rid of the node colors by coloring every edge e with the triple (a,b,c), where a is the original color of the edge, b is the color of its head, and c is the color of its tail. Edge-colorings obtained this way have a special property (each edge incident with a node v should carry the same information about the color of V ), but this consistency is a testable property. We call a complete digraph whose edges are colored with 1,...,k brieﬂy a k-colored digraph.

Given a k-colored digraph L and a positive integer m ≤ k, we can get an ordinary graph from L by keeping only the edges with colors 1,...,m, and then forgetting the coloring and the orientation. We call this graph L′ the “shadow” of L. If Q is a property of colored directed graphs, then we deﬁne Q′ = {L′ : L ∈ Q}.

A graph property P is nondeterministically testable, if there exist two integers k ≥ m ≥ 1 and a property Q of k-colored digraphs such that Q is testable and Q′ = P. In other words, G has property P if and only if we can orient its edges (in one or both directions), color them with m colors, add all the missing oriented edges, and color them with further k − m colors, so that the resulting k-colored digraph has property Q. We call such an orientation and coloring a certiﬁcate for P.

Instead of a k-coloring, we could specify k binary relations on V (G) as a certiﬁcate (this would be more in the spirit of mathematical logic). The fact that in a coloring they are disjoint and partition V (G) and V (2G) , respectively, can be easily tested. Conversely, such a system of relations deﬁnes a 2k-coloring. As long as we are not concerned with eﬃciency, these two ways of looking at certiﬁcates are equivalent.

Clearly every testable property is nondeterministically testable (choosing k = 2, m = 1). Our main result asserts the converse. Theorem 1.1 A graph property is nondeterministically testable if and only if it is testable.

One could say that this theorem shows that “P=NP” for property testing in dense graphs. The proof uses the theory of graph limits as developed in [5, 12], and its connection with property testing [14].

# 2 Preliminaries

- 2.1 Convergence and limits


Convergence of a sequence of dense ﬁnite graphs was deﬁned by Borgs, Chayes, Lov´asz, So´s and Vesztergombi [4, 5]. Graphons were introduced by Lov´asz an Szegedy in [12] as limits of convergent sequences of ﬁnite graphs. We have to extend these notions to colored digraphs; this was essentially done in [15], but we use here a little diﬀerent (simpler) terminology.

For a graph G and integer r ≤ |V (G)|, let us select an ordered r-tuple of nodes of G randomly and uniformly (without repetition). Let G(r,G) denote the subgraph induced by these nodes. If G is colored and directed, then G(r,G) is also a colored digraph in the obvious way.

We say that a sequence of k-colored digraphs Ln is convergent, if |V (Gn)| → ∞, and for every r ≥ 1, the distribution of G(r,Ln) tends to a limit as n → ∞. Note that this distribution is over a ﬁnite set, so it does not matter in which norm we want it to converge.

The limit object of a convergent sequence of simple graphs can be described as a symmetric measurable function W : [0,1]2 → [0,1], called a graphon. We will need the more general notion of a kernel, a bounded symmetric measurable function W : [0,1]2 → R. Dropping the condition of symmetry, we get digraphons and dikernels.

For a sequence of k-colored digraphs, the limit object is a bit more complicated:

it consists of k digraphons (W1,...,Wk) such that h Wh = 1. We call the k-tuple W = (W1,...,Wk) a k-digraphon. We deﬁne a k-dikernel analogously.

Let L be a k-colored digraph with V (L) = [n]. Let Sn denote the partition of [0,1] into n intervals S1,...,Sn of equal length. We can associate with L a k-digraphon WL = (WL1,...,WLk), where

WLh(x,y) =

1, if x ∈ Si, y ∈ Sj, and the color of ij is h, 0, otherwise.

More generally, we can consider a fractionally k-colored digraph H in which we have k nonnegative weights β1(i,j),...,βk(i,j) for every ordered pair (i,j) of nodes, with

h βh(i,j) = 1. We consider every k-colored digraph as a special case, where βh is the indicator function of edge color h. For a fractionally k-colored digraph H, we deﬁne the k-digraphon WH in the obvious way.

We can sample a k-colored digraph G(r,W) on node set [r] from a k-digraphon W as follows: we choose r independent random points X1,...,Xr ∈ [0,1] uniformly, and we color a pair (i,j) with color h with probability Wh(Xi,Xj) (independently for diﬀerent pairs of nodes).

The following fact is proved in [15].

- Proposition 2.1 Let Ln be a convergent sequence of k-colored digraphs. Then there is a k-digraphon W such that G(r,Ln) → G(r,W) in distribution. We write Ln → W if this holds.

Let W be a dikernel, and let J = {S1,...,Sm} be a partition of [0,1] into measurable sets with positive measure. We denote by WJ the dikernel obtained by averaging W in every rectangle Si × Sj. More precisely, for x ∈ Si and y ∈ Sj we deﬁne

WJ (x,y) =

1 λ(Si)λ(Sj)

![image 1](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile1.png>)

Si×Sj

W(u,z)du dz.

We quote a well-known fact:

- Proposition 2.2 For every dikernel W, we have WS


n → W (n → ∞) almost everywhere.

- 2.2 Many distances


Cut norm and cut distance. Convergence to a k-digraphon can be described in more explicit forms. Let us start with recalling the cut-norm-distance of two graphs G and G′ on the same node set V (introduced by Frieze and Kannan [9]):

|eG(S,T) − eG′(S,T)| |V |2

d (G,G′) = max S,T⊆V

,

![image 2](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile2.png>)

where eG(S,T) denotes the number of edges with one endpoint in S and the other in T. A related notion for dikernels is the cut norm

W = sup

S,T⊆[0,1]

S×T

W(x,y)dxdy .

The cut norm deﬁnes a distance function between two dikernels in the usual way by d (U,W) = U − W .

The cut norm has many nice properties (see [5]), of which we need the following (Lemma 2.2 in [14]):

- Proposition 2.3 Let Wn (n = 1,2,...) be a sequence of uniformly bounded dikernels such that Wn → 0. Then for every bounded measurable function Z : [0,1]2 → R, we have WnZ → 0.


Proof. If Z is the indicator function of a rectangle, the conclusion follows from the deﬁnition of the . norm. Hence the conclusion follows for stepfunctions, since they are linear combinations of a ﬁnite number of indicator functions of rectangles. Then it follows for all integrable functions, since they are approximable in L1([0,1]2) by stepfunctions.

From the point of view of graph limits, however, a kernel is only relevant up to a measure preserving transformation of [0,1]. Hence it is often more natural to consider the following distance notion, which we call the cut distance:

δ (U,W) = inf

φ,ψ

Uφ − Wψ ,

where φ,ψ : [0,1] → [0,1] are measure preserving maps, and Uφ(x,y) = U(φ(x),φ(y)). This deﬁnes a pseudometric on the set of kernels (it is only a pseudometric, since diﬀerent kernels may have distance 0). An important fact is that endowing the space of all graphons with this pseudometric makes it compact [13].

For two graphs G and G′ (not necessarily with the same number of nodes) we deﬁne δ (G,G′) = δ (WG,WG′).

(There is a ﬁnite description of this in terms of the optimum of a quadratic program, but it is quite complicated, and for us this less explicit deﬁnition will be suﬃcient.) It is easy to see that if V (G) = V (G′), then

δ (G,G′) ≤ d (G,G′).

These distance notions can be extended to colored graphs and kernels. For two fractionally k-colored digraphs H and H′ on the same node set V , with edgeweights βHh (i,j) and βHh ′(i,j) (h = 1,...,k), let

k

1 |V |2

d (H,H′) =

max

![image 3](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile3.png>)

S,T⊆V

h=1

(βHh (i,j) − βHh ′(i,j)) .

- i∈S
- j∈T


We generalize the cut-norm-distance to two k-digraphons U = (U1,...,Uk) and W = (W1,...,Wk):

k

Uh − Wh . (1)

d (U,W) =

h=1

Similarly as above, we need the “unlabeled” cut distance δ (U,W) = inf

d (Uφ,Wψ) (2)

φ,ψ

(where Uψ is obtained from U by substituting φ(x) for x in each of the 2k functions constituting U).

For two fractionally k-colored digraphs H and H′ (not necessarily with the same number of nodes) we deﬁne

δ (H,H′) = δ (WH,WH′). The following result is proved (in a more general form) in [15].

- Proposition 2.4 Let Ln be a sequence of k-colored digraphs, and let W be a k-

digraphon. Then Ln → W if and only if δ (WL

n

,W) → 0. We cannot claim convergence in the d distance, since WL

n

depends on the labeling of the nodes of Ln, while the convergence Ln → W does not. However, at least in the case of simple graphs, the following stronger version is true ([5], Theorem 4.16):

- Proposition 2.5 Let Gn be a sequence of graphs, and let U be a graphon such that


n − U → 0.

Gn → U. Then the graphs Gn can be labeled so that WG

Edit distance. From the point of view of property testing, the “edit distance” is very important (in fact, from the point of view of analysis, property testing is about the interplay between the edit distance and the cut distance). For two graphs G and G′ on the same set of nodes V = V (G) = V (G′), their edit distance is deﬁned by

d1(G,G′) = |E(G)△E(G′)| |V |2

.

![image 4](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile4.png>)

We generalize this for two k-colored digraphs L and L′ on the same node set:

D2 |V |2

d1(L,L′) =

,

![image 5](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile5.png>)

where D2 is the number of edges colored diﬀerently, in L and L′.

For two kernels, their edit distance is just their L1-distance as functions. For two k-digraphons, their edit distance is deﬁned by a formula very similar to (1):

k

d1(U,W) =

h=1

Uh − Wh 1.

Similarly to (2), we could deﬁne the unlabeled version of the edit distance, but we don’t need it in this paper.

The following (easy) characterization of testability of graph properties was formulated in [14], Theorem 3.20.

- Proposition 2.6 A graph property P is testable if and only if for any sequence (Gn) of graphs with |V (Gn)| → ∞, the condition δ (Gn,P) → 0 implies that d1(Gn,P) → 0.


We note that the condition says that Gn is close to some graph in P (not necessarily with the same number of nodes) in the δ distance, while the conclusion is that it must be close to a graph in P on the same node set in the edit distance.

# 3 Main proof

We start with a randomized construction to obtain a k-colored digraph from a fractionally k-colored digraph H: we color every edge ij ∈ [n2] with color h with probability βh(i,j). For diﬀerent pairs i,j we make an independent decision. We denote this random k-colored digraph by L(H).

- Lemma 3.1 Let H be a fractionally k-colored digraph on n nodes. Then

d (H,L(H)) ≤

10k √n

![image 6](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile6.png>)

![image 7](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile7.png>)

with probability at least 1 − ke−n. Proof. For two colors, this is just Lemma 4.3 in [5]. For general k, it follows by applying this fact to each color separately.

The main step in the proof of Theorem 1.1 is the following lemma.

- Lemma 3.2 Let W = (W1,...,Wk) be a k-digraphon, and suppose that U = m h=1 Wh is symmetric (where 1 ≤ m ≤ k). Let Fn be a sequence of simple graphs


such that Fn → U. Then there exist k-colored digraphs Jn on V (Fn) such that Jn′ = Fn and Jn → W.

Proof. First, we construct a fractionally k-colored digraph Hn on V (Fn). To keep the notation simple, assume that V (Fn) = [n]. By Proposition 2.5, we can choose the labeling of the nodes of each Fn so that WF

n − U → 0. For every pair i,j ∈ [n], we deﬁne

WSh

(x,y) US

 

if 1 ≤ h ≤ m,

n

(An)ij

![image 8](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile8.png>)

(x,y)

βh(i,j) =

n

WSh

(x,y) 1 − US

if m + 1 ≤ h ≤ k,

(1 − (An)ij)

n



![image 9](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile9.png>)

(x,y)

n

where An denotes the adjacency matrix of Gn and x ∈ Si and y ∈ Sj (these numbers are independent of the choice of x and y). It is easy to check that h βh(i,j) = 1 for all i = j. We show that for the fractionally k-colored digraph Hn constructed this way, we have

,W) → 0 (n → ∞). (3) Here we have

d (WH

n

k

n − Wh ,

WHh

,W) =

d (WH

n

h=0

and so it suﬃces to prove that WHh

− Wh → 0 for every ﬁxed h. We describe the proof for h ≤ m; the other case is analogous. Since 0 ≤ Wh ≤ U, we can write Wh = UZ, where 0 ≤ Z ≤ 1, and Z = 0 if U = 0. Then we have

n

n − Wh = sup

WHh

S,T⊆[0,1]

S×T

n − Wh .

WHh

Substituting from the deﬁnition,

(WHh

n

S×T

− Wh) =

S×T

WSh

(x,y) US

(x,y) − Wh(x,y) dxdy.

(x,y)

WF

n

![image 10](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile10.png>)

n

n

We split this integral as follows:

S×T U=0

WF

n

(UZ)S

n

![image 11](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile11.png>)

US

n

+

S×T U =0

WF

n

(UZ)S

n

− Z +

![image 12](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile12.png>)

US

n

S×T

n − U)Z. (4)

(WF

The ﬁrst term, which is nonnegative, can be estimated as follows:

S×T U=0

WF

n

(UZ)S

n

![image 13](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile13.png>)

US

n

≤

S×T

WF

n U=0 =

S×T

n − U) U=0 ≤ (WF

n − U) U=0 .

(WF

Here the right hand side tends to 0 by Proposition 2.3. The second term can be estimated like this. By Proposition 2.2, we have (UZ)S

n → U almost everywhere. Hence (UZ)S

n → UZ and US

n → Z in almost every point where U = 0. Since the integrand is bounded, this implies that

/US

n

WF

n

S×T U =0

(UZ)S

n

− Z ≤

WF

![image 14](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile14.png>)

n

US

n

U =0

(UZ)S

n

− Z → 0.

![image 15](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile15.png>)

US

n

Finally for the third term in (4), we have

n − U)Z ,

n − U)Z ≤ (WF

(WF

S×T

and here the right hand side tends to 0, again by Proposition 2.3. This proves (3).

To complete the proof of the lemma, we consider the k-colored digraphs Jn = L(Hn). By Lemma 3.1, we have

10k √n

d (Jn,Hn) ≤

![image 16](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile16.png>)

![image 17](<2012-lovsz-non-deterministic-graph-property-testing_images/imageFile17.png>)

(5)

with probability at least 1 − ke−n. Since n e−n is convergent, the Borel–Cantelli Lemma implies that almost surely (5) holds for all but a ﬁnite number of indices n.

) → 0, and hence d (WJ

,WH

Choosing the Jn so that this occurs, we have d (Jn,Hn) = d (WJ

n

n

,W) → 0.

n

Proof of Theorem 1.1. Let P be a nondeterministically testable property; we show that it is testable. By Proposition 2.6 it suﬃces to prove that if (Fn) is a sequence of graphs such that d (Fn,P) → 0, then d1(Fn,P) → 0.

Since P is nondeterministically testable, there are integers 1 ≤ m ≤ k and a testable property Q of k-colored digraphs such that P = Q′. Let Gn ∈ P such that d (Fn,Gn) → 0. Since Gn ∈ P, there are k-colored digraphs Ln ∈ Q such that Gn = L′n.

We may assume that the union of colors 1,...,m contains every edge of Gn in both directions; else, we reﬁne the coloring so that no edge in G and in its complement gets the same color in any direction (this doubles the number of colors at most). By selecting a subsequence, we may assume that the sequence (Ln) is convergent. Let W be a k-digraphon representing its limit, and let U = mh=1 Wh. Then Gn → U. From δ (Gn,Fn) → 0 we see that Fn → U.

Now we invoke Lemma 3.2, and construct k-colored digraphs Jn such that Jn′ = Fn and Jn → W. Hence d (Jn,Q) → 0. Since Q is testable, this implies that d1(Jn,Q) → 0, and so we can change the color of o(n2) edges in Jn so that the resulting k-colored digraph Mn belongs to Q. But then Mn′ ∈ P, and Mn′ diﬀers from Fn in o(n2) edges only, so d1(Fn,P) ≤ d1(Fn,Mn′ ) → 0.

# 4 Applications

There are many graph properties that can be certiﬁed by a node-coloring: k-colorable graphs, split graphs, etc. Many of these properties are hereditary, and so their testability follows also by the Alon–Shapira Theorem mentioned in the introduction. Here we formulate some consequences for non-hereditary graph properties.

One of the ﬁrst nontrivial results about property testing concerned the maximum cut. Let us derive one version. The property of a 2-node-colored graph G that “at least c|V (G)|2 edges connect nodes with diﬀerent colors” is trivially testable, and hence:

- Corollary 4.1 Let 0 < c < 1. The property of a graph G that its maximum cut contains at least c|V (G)|2 edges is testable. Similarly for maximum bisection.


In their paper [11], Theorem 9.1, Goldreich, Goldwasser and Ron prove the testability of more general properties, namely the existence of multiway cuts with upper and lower bounds on the sizes of partition classes as well as on edge densities between parts. The existence of such a cut can be certiﬁed by a node-coloring, and so this

property is trivially nondeterministically testable. So their general result (without explicit bounds on the sample size) follows from Theorem 1.1.

Alon, Fischer, Krivelevich and Szegedy [1] prove that a graph property is testable, provided it is expressible in the form ∃x1 ...∃xa∀y1 ...∀ybΦ(x1,...,xa,y1,...,yb), where the xi and yj are variables ranging over nodes, and Φ is a (quantiﬁer-free) Boolean expression involving equality and adjacency of the variables xi and yj. They also give an example showing that graph properties deﬁned by more general ﬁrst order sentences (with more quantiﬁer alternations) are not necessarily testable.

To relate this result to ours, let us start with noticing that properties expressible by universal ﬁrst-order formulas ∀y1 ...∀ybΦ(y1,...,yb) are exactly those expressible by a ﬁnite number of excluded induced subgraphs. (Such properties are hereditary, and this shows that the Alon–Shapira Theorem described in the Introduction is a generalization of this special case in another direction.) In the general case, roughly speaking, they eliminate the existential quantiﬁers by encoding them into a node-coloring: the color of a node expresses to which of the nodes xi it is connected, along with the subgraph induced by the nodes xi. Hence such a property is nondeterministically testable: the certiﬁcate is this coloring.

Our result implies a more general testability condition in terms of logical formulas:

- Corollary 4.2 Let P be a graph property expressible by a second-order formula of the form ∃S1 ...∃Sc∃x1 ...∃xa∀y1 ...∀ybΦ(S1,...,Sc,x1,...,xa,y1,...,yb), where the Si are variables ranging over unary or binary relations, xi and yj are variables ranging over nodes, and Φ is a (quantiﬁer-free) Boolean expression involving equality, adjacency, and the relations Si of the variables xi and yj. Then P is testable.

In [14], the upward closure of a graph property P was deﬁned as the graph property P↑ consisting of those graphs that have a spanning subgraph in P. Suppose that P is testable, then the property of 3-edge-colored graphs that “edges with color 1 form a graph with property P” is testable, and hence:

- Corollary 4.3 The upward closure of a testable graph property is testable.

Suppose again that P is testable, then the property of 4-edge-colored graphs that “edges with colors 1 and 2 form a graph with property P, and edges with colors 2 and 3 are fewer than |V (G)|2/100” is testable, and hence:

- Corollary 4.4 If P is a testable property, then the property that “we can change at most |V (G)|2/100” edges to get a graph with property P” is also testable.
- 5 Parameter estimation


Let f be a bounded graph parameter (i.e., a function deﬁned on simple graphs, invariant under isomorphism). We say that f is estimable, if for every ε,δ > 0 there is a positive integer k such that if G is a graph with at least k nodes and we select a random k-set X ⊆ V (G), then

P(|f(G) − f(G[X])| > ε) < δ. (6)

We deﬁne an estimable parameter of edge-colored digraphs similarly. If g is such a parameter, then we can deﬁne

g′(G) = max{g(L) : L′ = G}. An argument very similar to the proof of Theorem 1.1 above gives:

Theorem 5.1 If g is an estimable parameter of k-colored digraphs, then g′ is estimable as well.

We could of course replace the maximum in the deﬁnition of g′ by minimum. As an example, let us consider graphs L whose nodes are 2-colored red and blue, and let g(L) denote the number of 2-colored edges, divided by |V (G)|2. Then g is trivially estimable. The simple graph parameter g′ is the maximum cut (normalized), so this is estimable.

# 6 Concluding remarks

There are several possible analogues and extensions of our results. One could consider certiﬁcates in the form of t-ary relations for any t. One could then allow hypergraphs instead of the original graphs. A limit theory for hypergraphs is available (Elek and Szegedy [7], and we expect our main result to generalize to hypergraphs; however, several of the auxiliary results we have made use of have not been extended, and a full proof will take further research.

A generalization in a diﬀerent direction would be to consider, instead of coloring, node and edge decorations from a compact topological space. For example, the property of being a threshold graph can be certiﬁed by a decoration of the nodes by numbers from [0,1]. The limit theory for graphs has been extended to compact decorations [15]; perhaps our main result extends too, but this takes further research.

We should point out that our results are non-eﬀective, they don’t provide any explicit bound on how large a sample size must be chosen for a given error bound. In this sense, what we have given is a pure existence proof of an algorithm. From a practical point of view, this does not make much diﬀerence from related results based on the Regularity Lemma, but from a theoretical point of view, it would be interesting to determine whether Theorem 1.1 can be proved with an eﬀective bound.

Finally, let us mention that the situation is quite diﬀerent in the case of graphs with bounded degree (for which a limit theory analogous to the dense case is available, and property testing has been extensively studied). Here the sampling method is to select r random nodes (uniformly), and explore their neighborhoods of depth r. The property of a graph G that “G is the disjoint union of two graphs on at least |V (G)|/3 nodes” can be certiﬁed by coloring the nodes in these two graphs with diﬀerent colors, so this property is nondeterministically testable. On the other hand, sampling will not distinguish between an expander graph and the disjoint union of two copies of it, so this property is not testable.

Acknowledgements. Research was supported by the European Research Council Grant No. 227701 and by the National Science Foundation under agreement No. DMS0835373. Hospitality of the Institute for Advanced Study is gratefully acknowledged. Any opinions and conclusions expressed in this material are those of the authors and do not necessarily reﬂect the views of the NSF or of the ERC.

# References

- [1] N. Alon, E. Fischer, M. Krivelevich and M. Szegedy: Eﬃcient testing of large graphs, Combinatorica 20 (2000) 451–476.
- [2] N. Alon, E. Fischer, I. Newman and A. Shapira: A Combinatorial Characterization of the Testable Graph Properties: It’s All About Regularity, Proc. of the 38-th ACM Symp. Theor. of Comp. (STOC) (2006), 251–260.
- [3] N. Alon and A. Shapira: A Characterization of the (natural) Graph Properties Testable with One-Sided Error, SIAM J. Computing 37 (2008), 1703–1727.
- [4] C. Borgs, J. Chayes, L. Lov´asz, V.T. So´s, K. Vesztergombi: Counting graph homomorphisms, in: Topics in Discrete Mathematics (ed. M. Klazar, J. Kratochvil, M. Loebl, J. Matouˇsek, R. Thomas, P. Valtr), Springer (2006), 315–371.
- [5] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s, and K. Vesztergombi: Convergent Graph Sequences I: Subgraph frequencies, metric properties, and testing, Advances in Math. 219 (2008), 1801–1851.
- [6] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s, and K. Vesztergombi: Convergent Graph Sequences II: Multiway Cuts and Statistical Physics, Annals of Math. http://www.cs.elte.hu/~lovasz/ConvRight.pdf
- [7] G. Elek, B. Szegedy: Limits of hypergraphs, removal and regularity lemmas. A non-standard approach. http://arxiv.org/0705.2179
- [8] E. Fischer: The art of uninformed decisions: A primer to property testing, The Computational Complexity Column of the Bulletin of the European Association for Theoretical Computer Science 75 (2001), 97-126.
- [9] A. Frieze and R. Kannan: Quick approximation to matrices and applications, Combinatorica 19 (1999), 175–220.
- [10] O. Goldreich (ed): Property Testing: Current Research and Suerveys, LNCS 6390, Springer, 2010.
- [11] O. Goldreich, S. Goldwasser and D. Ron: Property testing and its connection to learning and approximation, J. ACM 45 (1998), 653–750.
- [12] L. Lov´asz, B. Szegedy: Limits of dense graph sequences, J. Comb. Theory B 96

(2006), 933–957.

- [13] L. Lov´asz, B. Szegedy: Szemer´edi’s Lemma for the analyst, Geom. Func. Anal. 17 (2007), 252–270.
- [14] L. Lov´asz, B. Szegedy: Testing properties of graphs and functions, Israel J. Math. 178 (2010), 113–156.
- [15] L. Lov´asz, B. Szegedy: Limits of compact decorated graphs http://arxiv.org/abs/1010.5155
- [16] R. Rubinfeld and M. Sudan: Robust characterization of polynomials with applications to program testing, SIAM J. on Computing 25 (1996), 252–271.


