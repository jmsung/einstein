arXiv:1509.03871v2[math.AT]10Jul2017

2-COMPLEXES WITH LARGE 2-GIRTH

DOMINIC DOTTERRER, LARRY GUTH, AND MATTHEW KAHLE

Abstract. The 2-girth of a 2-dimensional simplicial complex X is the minimum size of a non-zero 2-cycle in H2(X,Z/2). We consider the maximum possible girth of a complex with n vertices and m 2-faces. If m = n2+α for α < 1/2, then we show that the 2-girth is at most 4n2−2α and we prove the existence of complexes with 2-girth at least cα,ǫn2−2α−ǫ. On the other hand, if α > 1/2, the 2-girth is at most Cα. So there is a phase transition as α passes 1/2.

Our results depend on a new upper bound for the number of combinatorial types of triangulated surfaces with v vertices and f faces.

1. Introduction

In this paper, we study a 2-dimensional analogue of the girth of a graph. Recall that the girth of a graph is the shortest length of a nontrivial cycle in the graph. If X is a 2-dimensional simplicial complex, then the 2-girth of X is deﬁned to be the minimum number of 2-faces in a non-zero 2-cycle with coeﬃcients in Z/2. We address the following question: if X has n vertices and m 2-faces, what is the maximum possible size of the 2-girth of X? We prove upper and lower bounds which match pretty closely. They show a phase transition as m passes n2.5.

For context, let us ﬁrst recall the situation for graphs. Let g(n, m) denote the maximum possible girth of a graph with n vertices and m edges. We note that g(n, n) = n, because any graph with n vertices and n edges must contain a cycle, and the number of edges in the cycle is at most the total number of edges in the graph. As we increase the number of edges, g(n, m) decreases rapidly. For instance, g(n, 2n) = O(log n),

![image 1](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile1.png>)

L.G. was supported in part by a Simons Investigator Grant. M.K. gratefully acknowledges support from DARPA #N66001-12-1-4226, NSF

#CCF-1017182 and #DMS-1352386, the Institute for Mathematics and its Applications, and the Alfred P. Sloan Foundation.

All three authors thank the Institute for Advanced Study for hosting them in Spring 2011, when some of this work was completed.

1

and for any α > 0, g(n, n1+α) ≤ Cα. These estimates are special cases of the Moore bounds (cf. [1] ).

Now we turn to 2-dimensional simplicial complexes. Let g2(n, m) denote the maximum possible 2-girth of a 2-dimensional simplicial complex X with n vertices and m 2-faces. A graph with n vertices has

at most n2 edges. If m = n2 − n + 2, then a dimension counting argument implies that H2(X, Z/2) = 0, and so X contains a non-zero 2-cycle. Therefore,

n 2 − n + 2 ≤ n2.

n 2 − n + 2) ≤

g2(n,

As we add 2-faces to a simplicial complex X, its 2-girth can only decrease, and so g2(n, m) is decreasing in m. In analogy with the case of graphs, one might expect g2(n, m) to decrease very sharply

- as m increases. For instance, we initially expected that g2(n, 2n2) = O(logn). But it turns out that this is not the case. Aronshtam, Linial, Luczak, and Meshulam introduced techniques in [2] which show that


g2(n, Kn2) ≥ cKn2 for every constant K > 0 – see Section 6 for more discussion of their work.

We study the behavior of g2(n, m) as m increases further. We prove two upper bounds for g2(n, m).

- Theorem 3.1. If α ≥ 0 and m ≥ n2+α,

then

g2(n, m) ≤ 4n2−2α.

In the case α > 1/2, there is a much better upper bound on g2(n, m). This was studied implicitly by S´os, Erd˝os, and Brown [8], in the context of Tura´n theory for hypergraphs. We include their argument for the sake of completeness, to show the following.

- Theorem 3.2. If m ≥ n2+α, where α > 1/2, then g2(n, m) ≤ Cα,


where Cα is a constant which depends only on α.

Our most diﬃcult result is a lower bound on g2(n, m) that roughly matches the upper bound from Theorem 3.1 in the regime 0 ≤ α < 1/2.

∞

| | | |
|---|---|---|
| | | |
| | | |
| | | |


∞

- n0
- n1
- n2
- n3


| | |
|---|---|
| | |
| | |


g(n, m)2

g(n, m)

- n0
- n1
- n2


n0 n1 n2

n0 n1 n2 n3

m

m

Figure 1. Comparing the large-scale behavior of g(n, m) and g2(n, m), on a log-log scale.

Theorem 4.1. Let 0 < α < 1/2, and ǫ > 0. For suﬃciently large n, there exist simplicial complexes ∆ with n vertices and with at least

- m = n2+α faces, and 2-girth at least n2−2α−ǫ.

Notice that if α is slightly less than 1/2, then g2(n, n2+α) is roughly

- n, while if α is slightly more than 1/2, then g2(n, n2+α) is bounded by a constant. Figure 1 compares the behavior of g(n, m) and g2(n, m).


The proof of Theorem 4.1 is based on random simplicial complexes. Linial and Meshulam [6] introduced the following random model of simplicial complexes, called Y (n, p). Take the complete graph on n

vertices. There are n3 possible 2-simplices that we could add to this graph. Include each independently with probability p. If p = nα−1,

then with high probability the resulting simplicial complex Y has on the order of n2+α 2-faces. We count inclusion-minimal 2-cycles in Y , and we show that with high probability Y contains only a small number of inclusion-minimal 2-cycles of size less than n2−2α−ǫ. By removing a 2-face from each of these cycles, we get a complex with 2-girth at least n2−2α−ǫ and with roughly n2+α 2-faces.

Let ∆(2)n denote the 2-skeleton of the simplex on n vertices. We have Y ⊂ ∆(2)n . If z is an inclusion-minimal 2-cycle in ∆(2)n with f faces, then z will be included in Y ∈ Y (n, p) with probability pf. So to prove our main theorem, we have to count the number of inclusion minimal 2-cycles in ∆(2)n . This turns out to be a complicated counting problem. We organize the inclusion minimal 2-cycles according to combinatorial type, which is deﬁned as follows. Given z an inclusion minimal 2cycle, there is a triangulated surface Σ and a simplicial map Σ →

∆(2)n realizing z. Because z is inclusion-minimal, Σ is connected. The combinatorial type of z is the combinatorial type of the surface Σ. It’s not so hard to count the number of inclusion minimal 2-cycles of a ﬁxed combinatorial type. It turns out to be harder to count and organize the possible combinatorial types. The most diﬃcult step in the argument is an estimate about the set of possible combinatorial types.

Theorem 4.1. Let T(f, w) be the set of connected, triangulated closed surfaces with f 2-faces and w vertices, up to simplicial isomorphism. For every δ > 0, there is a constant Cδ so that

|T(f, w)| ≤ Cδfff/2w−(1−δ)w.

Using this counting argument, we study the sizes of cycles in a random simplicial complex Y chosen from Y (n, p). A similar method gives an estimate about the isoperimetric properties of Y :

Theorem 6.1 Let α ∈ 0, 21 and ǫ > 0. Suppose p = nα−1, so the expected number of faces in Y (n, p) is n2+α. Let A be the ﬁlling area

![image 2](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile2.png>)

of the cycle 123 in Y . Then with high probability

n2−2α−ǫ ≤ A ≤ n2−2α+ǫ. 2. Notation and Concepts

- Deﬁnition 2.1. Let S = {1, 2, . . ., n}. A simplicial complex, ∆, on the underlying set S is a collection of subsets X ⊆ 2S such that if A ⊆ S is an element of ∆ and B ⊂ A, then B is an element of ∆.

We refer to the elements of ∆ of order 1, 2, and 2 as vertices, edges and faces, respectively. We denote the set of vertices, edges and faces

- as ∆(0), ∆(1) and ∆(2) respectively.


- Deﬁnition 2.2. If we set


Ck∆ := {c : ∆(k) → F}, we obtain a chain complex

· · · → Ck+1∆ →∂ Ck∆ →∂ Ck−1∆ → · · · whose chain maps, ∂ = ∂k : Ck∆ → Ck−1∆ are deﬁned by ∂c(σ) :=

c(σ ∩ {x}).

x∈S,σ∪{x}∈∆

We deﬁne Zk∆ := ker ∂k, the subspace of k-cycles, Bk−1∆ := im∂k, the subspace of (k − 1)-boundaries, and Hk(∆; F) := Zk∆/Bk∆, the k-th homology of ∆.

- Deﬁnition 2.3. For F = Z/2Z, we use the Hamming “norm”: for c ∈ Ck∆, deﬁne


c := supp(c) = |{σ ∈ ∆(k) | c(σ) = 1}|.

3. Upper bounds on g2(n, m)

- Theorem 3.1. If m ≥ n2+α,

where 0 < α ≤ 1/2, then

g2(n, m) ≤ 4n2−2α. So Theorem 3.1 bounds the size of the 2-girth for m up to n5/2. For

- m much larger than this, the 2-girth is bounded in size.


- Theorem 3.2. [S´s, Erd˝s, and Brown] Let ∆ be a 2-dimensional simplicial complex with n vertices and m faces. If m ≥ n2+α, where

1/2 < α < 1, then the 2-girth of ∆ is bounded by Cα where Cα is a constant which depends only on α.

- Theorem 3.2 is a result of S´os, Erd˝os, and Brown [8], but we include


a proof here for the sake of completeness.

- 3.1. Proof of Theorem 3.1.


- Lemma 3.3. Let ∆ be a 2-dimensional complex with n vertices and m faces. If m ≥ n2/2, then H2(∆) = 0. Proof. Since ∆ is a simplicial complex, the number of edges of ∆ is


- at most n2 < n2/2. If m ≥ n22, then the boundary map in simplicial homology from 2-chains to 1-chains has a nontrivial cycle, in which case H2(∆) = 0.


![image 3](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile3.png>)

We will restrict our attention to Z/2Z-cycles, and we will restrict ourselves to the ones which are irreducible in the following sense:

Deﬁnition 3.4. A Z/2Z-cycle, z ∈ Z2(∆) is called inclusion-minimal if for any other cycle z′ ∈ Z2(∆), supp(z′) ⊆ supp(z) implies that z′ = z.

- Lemma 3.5. For a 2-dimensional complex on n vertices, every inclusionminimal 2-cycle has fewer than n2/2 faces.


Proof. If there are more than n2/2 faces in a cycle, then delete faces arbitrarily until no more than n2/2 faces remain. By Lemma 3.3, there still remains at least one cycle. So an inclusion-minimal cycle can not have more than n2/2 faces.

- Proof of Theorem 3.1. Let D be a random subcomplex of ∆, chosen as


follows. Let V be a set of exactly k vertices, chosen uniformly over all

n

k such subsets, and let D = D(V ) be the induced subcomplex of ∆ on V .

So D is a simplicial complex with k vertices. What is the expected number of 2-faces E[f2(D)]? For a 2-face T = {x, y, z} in ∆, T is a face in D if and only if x, y, z ∈ V . We have

n−3 k−3 n k

P[x, y, z ∈ V ] =

,

![image 4](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile4.png>)

k3 2n3

,

≥

![image 5](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile5.png>)

- as long as n ≥ k ≥ 6. Now,


k3 2n3

E[f2(D)] ≥

f2(∆) ≥

![image 6](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile6.png>)

k3 2n3

n2+α

![image 7](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile7.png>)

Setting k = 2n1−α,

8n3−3α 2n3

n2+α

E[f2(D)] ≥

![image 8](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile8.png>)

= 4n2−2α

= k2.

Since this is the average, there must exist some subcomplex D′ on k vertices, such that f2(D′) ≥ k2. Applying Lemma 3.3, we have that H2(D′) = 0. Applying Lemma 3.5, D′ contains a non-trivial 2-cycle with at most k2 faces. Since k = 2n1−α, we get the desired bound.

- 3.2. Proof of Theorem 3.2.


- Lemma 3.6. If H is a graph on fewer than n vertices, and with at least n1+β edges, with β > 0 then H contains a cycle of length at most


Cβ = 2

1 β

![image 9](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile9.png>)

+ 1.

Proof of Lemma 3.6. A graph H of average degree d contains a subgraph H′ of minimum degree d′ ≥ d/2. (See for example Proposition 1.2.2 in [4].) Here

d = 2n1+β/n = 2nβ and we restrict our attention to a subgraph H′ ⊆ H, which has minimum degree at least nβ.

Let v ∈ H′ be a vertex, and for k = 0, 1, 2, . . . let Nv(k) denote the number of vertices in H′ at graph distance k from v. By the minimum degree requirement, Nv(1) ≥ nβ. If any of the distance-1 vertices have an edge between them, we have g(H) ≤ g(H′) ≤ 3.

If any two of the distance-1 vertices have a common neighbor, g(H) ≤

- 4. Similarly, if any two of the distance-2 vertices are adjacent, then g(H) ≤ 5, and so on. Now, every vertex at distance d must have at least nbeta −1 neighbors at distance d+1. So up to distance d, we have


- at least 1 + nβ + nβ nβ − 1 + nβ nβ − 1 2 + · · · + nβ nβ − 1 d−1


- Proof of Theorem 3.2. Deﬁne the degree deg(e) of an edge e to be number of 2-dimensional faces containing it. Then


e

deg(e) = 3m

and m ≥ n5/2+α by assumption. Note that the average edge degree is then at least ⌊6n1/2+α⌋.

Let P denote the number of pairs of 2-dimensional faces in ∆ which share an edge. Then

deg(e) 2

. Note that if a + 2 ≤ b, then

P =

e

b 2

a 2

b − 1 2 ≤

a + 1 2

,

+

+

so the sum e deg(2 e) is minimized when the parts are as close together

- as possible. Then even if each edge e had degree ⌊6n1/2+α⌋, we still have


⌊6n1/2+α⌋ 2 ≥ n3+2α

n 2

P ≥

for large enough n.

Now for every pair of vertices a, b, let T(a, b) denote the graph lk(a)∩ lk(b). I.e. the vertices in T(a, b) correspond to the intersection of the neighborhoods of a and b, and the edges xy in T(a, b) correspond to pairs of triangles axy, bxy.

If we sum up the number of edges in T(a, b) over all n2 pairs a, b, this gives P. So by the pigeonhole principle, there must be at least one pair a, b such that T(a, b) has at least n1+2α edges. Then applying

- Lemma 3.6, this graph must contain a cycle C on at most Calpha edges. In the simplicial complex ∆ then, there is a suspension over C with


suspension points a and b. So in particular there exists a 2-cycle with

- at most 2Cα 2-faces.


4. Complexes with large girth

- 4.1. Overview. We prove the existence of simplicial complexes with large girth.


- Theorem 4.1. Let 0 < α < 1/2, and ǫ > 0. For suﬃciently large


- n, there exist simplicial complexes ∆ with n vertices and with at least m = n2+α faces, and 2-girth at least n2−2α−ǫ.


Our strategy is to start with a random 2-dimensional simplicial complex. We recall the Linial-Meshulam model of random simplicial complexes Y (n, p) from [6]. A complex Y in Y (n, p) has n vertices, and

n

- 2 edges, and each 2-face is included independently with probability


- p. We choose p = n−1+α, where 0 < α < 1/2 is as in Theorem 4.1. We say that an event occurs with high probability (w.h.p.) if the


probability approaches one as n → ∞. We will show that with high probability, a complex Y in Y (n, p) contains only a few small 2-cycles. We construct the complex ∆ in Theorem 4.1 by starting with a random 2-dimensional complex Y from Y (n, p), and then removing a small number of 2-faces to destroy all the small 2-dimensional cycles.

Let ∆(2)n denote the 2-skeleton of the simplex on n vertices so that Y ⊂ ∆(2)n . If z is a 2-cycle in ∆(2)n with f 2-faces, then z is included in Y with probability pf. To estimate the number of small 2-cycles in

Y , we have to organize the set of 2-cycles in ∆(2)n . It turns out to be a good idea to study inclusion-minimal 2-cycles. We say that a 2-cycle z is inclusion minimal if there is no 2-cycle supported on a proper subset of the 2-faces in the support of z.

Let Z(f, v) denote the number of inclusion-minimal 2-cycles in ∆(2)n with vertex support [v] = {1, 2, . . ., v}, and with exactly f faces.

- Lemma 4.2. Z(f, v) = 0 unless 2f ≤ v ≤ f/2 + 2.


![image 10](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile10.png>)

Proof. The Euler formula for a ﬁnite 2-dimensional complex is that v − e + f = β0 − β1 + β2. For a minimal 2-cycle, we have that β0 = β2 = 1, so

(∗) v − e + f = 2 − β1. Since e ≤ v2 , this gives that

v2 2

v 2 − v + 2 − β1 ≤

f ≤

, so v ≥

![image 11](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile11.png>)

√2f.

![image 12](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile12.png>)

For the other inequality, we ﬁrst assume without loss of generality that every edge is contained in at least one 2-dimensional face—if not, then the edge can be deleted without aﬀecting either v or f. Since it is a 2-cycle, every edge is then contained in at least two 2-faces, so

2e ≤ 3f. Combining with (*) to eliminate the variable e, we have that f ≥ 2v − 4 + 2β1. Since β1 ≥ 0, the inequality v ≤ f/2 + 2 follows.

We will also require an upper bound on Z(f, v), namely that for any ﬁxed δ > 0, and large enough f and v, we have that

Z(f, v) ≤ Cδfff/2vδf. We establish this bound in Section 4.5.

We will use α and ǫ consistently throughout the section. Since α < 1/2, we may assume without loss of generality that ǫ is small enough that 2α + ǫ < 1.

Now we deﬁne constants δ and M which only depend on α and ǫ, and which we also use throughout the rest of the section.

First we set

1 − 2α 4

ǫ 3(2 − 2α − ǫ)

δ = min

. and

,

![image 13](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile13.png>)

![image 14](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile14.png>)

8 1 − 2α

+ 1.

M =

![image 15](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile15.png>)

First, we consider small cycles, where 4 ≤ v ≤ M. We will show that with high probability the total number of such cycles is small relative to the number of 2-dimensional faces. Then we can delete one face out of every small cycle without signiﬁcantly aﬀecting the number of faces.

Next, we consider intermediate cycles, where 2M − 2 ≤ f ≤ n. By

- Lemma 4.2, if v ≥ M + 1 then f ≥ 2M −2, so there is no gap between small and intermediate cycles. We show that with high probability there are no intermediate cycles.


Finally, we consider large cycles, where n ≤ f ≤ n2−2α−ǫ. Again, we show that with high probability there are no such cycles.

The conclusion is that w.h.p., the modiﬁed random 2-complex only has very-large cycles, i.e. cycles of area greater than n2−2α−ǫ.

- 4.2. Small cycles. For a simplicial complex ∆ and number M, let


C∆(M) denote the number of cycles supported on at most M vertices.

Deﬁne a subcomplex of Y on v vertices as barely-dense if it has exactly 2v − 4 faces. Let T∆(M) denote the number of barely-dense subcomplexes of ∆ with at most M vertices. Note that T∆(M) ≥ C∆(M) for every ∆ and M. Indeed, every cycle has f ≥ 2v − 4 and so contains a barely-dense subcomplex so we one can remove all the cycles by removing one face from every barely-dense subcomplex.

Again, letting ∆ = Y = Y (n, p) and by linearity of expectation,

M

v 3

n v

p2v−4.

E[TY (M)] =

2v − 4

v=4

Since M is a constant which only depends on α, this is a ﬁnite sum and v is bounded. Moreover, the terms in the sum are strictly decreasing as v increases for large enough n, so the ﬁrst term in the sum dominates.

Then

E[TY (M)] ≤ n4p4

= n4n−4+4α

= n4α.

On the other hand, the expected number of 2-faces E[f2(Y )] is

n 3

n2+α 6

p ≈

.

![image 16](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile16.png>)

The number of faces is a binomial random variable, therefore it is tightly concentrated around its mean (by Chernoﬀ bounds, for example).

By Markov’s inequality,

n4α n2+α/2

P TY (M) ≥ n2+α/2 ≤

,

![image 17](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile17.png>)

which tends to zero as n → ∞ since α < 1/2.

Since TY (M) dominates CY (M), with high probability we can remove one face from every small cycle and still be left with almost all of the faces.

- 4.3. Intermediate cycles. The sum


n−4

f/2+2

v=√2f

f=2M−2

![image 18](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile18.png>)

n v

Z(f, v)pf

is a union bound on the probability that there are any intermediate cycles: cycles whose number of faces f satisﬁes 2M − 2 ≤ f ≤ n.

Since f ≤ n and v ≤ f/2 + 2 ≤ n/2, we have that

n v ≤

n f/2 + 2

,

and then we may use the estimate

valid for f ≥ 4.

n f/2 + 2 ≤

en f

![image 19](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile19.png>)

f/2+2

,

- (1)

≤ n2

n

f=2M−2

f/2+2

v=√2f

![image 20](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile20.png>)

en f

![image 21](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile21.png>)

1/2

Cδf1/2vδp

f

- (2)

≤ n2

n

f=2M−2

f/2+2

v=√2f

![image 22](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile22.png>)

(en)1/2 Cδvδn−1+α

f

- (3)

≤ n2

n

f=2M−2

f/2+2

v=√2f

![image 23](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile23.png>)

- (4) Cδ′nδn−1/2+α f ,

≤ n3

n

f=2M−2

- (5) Cδ′nδ−1/2+α f ,


f/2+2

f/2+2

n

n

f/2+2

n v

en f

Cδfff/2vδfpf,

Z(f, v)pf ≤

![image 24](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile24.png>)

v=√2f

v=√2f

f=2M−2

f=2M−2

![image 25](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile25.png>)

![image 26](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile26.png>)

where C′

δ is a constant which only depends on δ.

This sum can be bounded, term by term, by the inﬁnite geometric series

a 1 − r

a + ar + ar2 + · · · =

, where

![image 27](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile27.png>)

a = n3 Cδ′nδ−1/2+α 2M−2 and

r = Cδ′nδ−1/2+α. We have chosen δ such that

1 − 2α 4

, so

δ ≤

![image 28](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile28.png>)

2α − 1 4

- 1

![image 29](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile29.png>)

- 2


< 0. We have chosen M so that

+ α ≤

δ −

![image 30](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile30.png>)

16 1 − 2α

2M − 2 ≥

> 0. So

![image 31](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile31.png>)

(δ − 1/2 + α)(2M − 2) ≤ −4, and

a = O n−1 . Since δ − 1/2 + α < 0, we also have that r = o(1).

Since a → 0 and r → 0 as n → ∞, we also have that a/(1 − r) → 0, and the probability that there are any intermediate cycles tends to zero.

- 4.4. Large cycles. Finally, we show that for any ﬁxed 0 < α < 1/2 and ǫ > 0,


n2−2α−ǫ

f/2+2

f=n

v=√2f

![image 32](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile32.png>)

n v

Z(f, v)pf → 0,

- as n → ∞, so by the union bound, w.h.p. there are no large cycles. We require the estimate |Z(f, v)| ≤ Cδfff/2vδv again.


n2−2α−ǫ

n2−2α−ǫ

f/2+2

f/2+2

n v

n v

Cδfff/2vδfpf

Z(f, v)pf ≤

v=√2f

v=√2f

f=n

f=n

![image 33](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile33.png>)

![image 34](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile34.png>)

n2−2α−ǫ

f/2+2

Cδfff/2pf

≤

v=√2f

f=n

![image 35](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile35.png>)

n2−2α−ǫ

Cδfff/2pf2nfδf,

≤

f=n

n v

vδf,

n2−2α−ǫ

≤

f=n

n2−2α−ǫ

≤

f=n

n2−2α−ǫ

≤

f=n

Cδf1/2+δp f 2n,

Cδ′f1/2+δn−1+α f ,

Cδ′n(2−2α−ǫ)(1/2+δ)n−1+α f .

Since we chose δ > 0 such that δ <

ǫ 2(2 − 2α − ǫ)

,

![image 36](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile36.png>)

we have

(2 − 2α − ǫ)(1/2 + δ) − 1 + α < 0,

in which case we can bound the sum by a geometric series whose ﬁrst term and ratio are tending to zero.

- 4.5. Cycle counts from counting triangulated surfaces. Recall that Z(f, v) is the set of inclusion-minimal 2-cycles on vertex set [v] = {1, 2, . . ., v} with exactly f faces. We bound |Z(f, w)| by bounding |T(f, w)|, the number of combinatorial isomorphism types of connected triangulated surfaces on f faces and w vertices. Theorem 5.1 gives the


following bound on |T(f, w)|: for any δ > 0, there is a constant Cδ so that

- (6) |T(f, w)| ≤ Cδfff/2w−(1−δ)w.

Next we note that |Z(f, v)| is related to |T(f, w)| by the following inequality:

- (7) |Z(f, v)| ≤


|T(f, w)|vw.

w≥v

We can see Inequality 7 as follows. Any 2-cycle can be realized as the image of a simplicial map from a triangulated surface which is injective on 2-dimensional faces. If the 2-cycle is minimal, then the triangulated surface must be connected. For a ﬁxed triangulated surface with w vertices, the number of simplicial maps to the simplex with v vertices is at most vw.

Combining (6) and (7), we have

|T(f, w)|vw

|Z(f, v)| ≤

w≥v

f/2+2

C˜δfff/2w−(1−δ)wvw

≤

w=v

f/2+2

= C˜δfff/2

(v/w1−δ)w

w=v

≤ C˜δfff/2(f/2 + 2)vδ(f/2+2) ≤ Cδfff/2vδf,

for large enough v and f, where Cδ is a constant which only depends on δ > 0.

5. Counting triangulated surfaces

Recall that T(f, w) is the set of connected triangulated surfaces with f faces and w vertices, counted up to simplicial isomorphism. In this section, we prove an upper bound for |T(f, w)|.

- Theorem 5.1. For every δ > 0, there exists a constant Cδ so that for all f, w,


|T(f, w)| ≤ Cδfff/2w−(1−δ)w.

In order to estimate |T(f, w)|, we imagine starting with f simplices and gluing together edges one at a time until we get a closed surface. This point of view was suggested by Brooks and Makover, [3].

We make a formal deﬁnition of this gluing process. Let ∆1, ..., ∆f be copies of the standard 2-simplex. Each of them has three edges, ∆j,a with a = 0, 1, 2. A gluing story for these f simplices is a sequence of 3f/2 gluing maps g1, ..., g3f/2. Each gluing map gk is a simplicial isomorphism from an edge ∆j(k),a(k) to another edge ∆j′(k),a′(k). (A gluing map is allowed to map one edge of a simplex to another edge of the same simplex, but it is not allowed to map an edge to itself.) The maps gk make a gluing story if each edge is involved in exactly one gluing map gk. We abbreviate a gluing story by  g, and we let GS(f) denote the set of all gluing stories for f 2-simplices.

It’s straightforward to count the total number of gluing stories. Proposition 5.2. |GS(f)| = (3f)!23f/2.

Proof. We ﬁrst need to list the sequence of domains of gk and ranges of gk. This amounts to listing the 3f edges of the triangles ∆j in some order, so there are (3f)! choices. After choosing the domain and range of each gk, we have two choices for each map gk, because there are two simplicial isomorphisms from one interval to another.

Given a gluing story  g, we can deﬁne a 2-dimensional surface X( g) by starting with the f simplices ∆1, ..., ∆f and identifying points p and

- q if one of the gluing maps takes p to q. The resulting object is not always a triangulated surface. It is a slightly more general object called a pseudomanifold. For example, X( g) could consist of two triangles, one on top of the other, with corresponding edges glued together. The resulting surface is homeomorphic to S2, but it is not a triangulated surface. (Recall that a triangulated surface is a simplicial complex which is homeomorphic to a 2-dimensional manifold. This last example is not a simplicial complex.) We will discuss pseudomanifolds more below.


Here is an outline of the proof of Theorem 5.1. Each surface X ∈ T(f, w) is simplically isomorphic to X( g) for some g ∈ GS(f). In fact, each surface X ∈ T(f, w) can be realized by many diﬀerent gluing stories, and we have to estimate the size of this overcount.

- Lemma 5.3. There is a constant C > 0 so that the following holds. For every X ∈ T(f, w), there are at least C−ff5f/2 gluing stories  g so that X( g) is simplicially isomorphic to X.


This lemma is similar to results in [3], but we will give a selfcontained proof.

Next we will estimate the number of gluing stories that produce triangulated surfaces with w vertices. This estimate is the new ingredient in the proof of Theorem 5.1.

- Lemma 5.4. For any δ > 0, there is a constant Cδ so that for any f, w, the number of gluing stories  g ∈ GS(f) on f so that X( g) is a connected triangulated surface with w vertices is ≤ Cδff3fw−(1−δ)w.


Combining Lemma 5.3 and Lemma 5.4 gives Theorem 5.1.

If we compare Proposition 5.2 and Lemma 5.4, we see that the fraction of gluing stories  g ∈ GS(f) so that X( g) is a triangulated surface with w vertices is at most roughly w−w. In particular, gluing stories that produce triangulated surfaces with many vertices are quite rare.

Here is the intuition behind our argument. Imagine that we carry out the gluings one map at a time. Before the ﬁrst gluing, we have f disjoint triangles. At each step of the process, we glue together two of the edges in the boundary. After performing k gluings, we have a surface with boundary, called Xk( g). After using all 3f/2 gluing maps, we have X( g). A vertex of Xk( g) is called a boundary vertex if it lies in the boundary of Xk( g), and an internal vertex otherwise. Let Vint(Xk) be the set of internal vertices of Xk( g). Since X( g) has no boundary, every vertex of X( g) is internal. On the other hand, X0( g) has zero internal vertices. The only way that Xk+1( g) can have more internal vertices than Xk( g) is if gk+1 glues together two edges of ∂Xk( g) that share a vertex. This is a rare event. The number of edges in ∂Xk( g) is

- 3f − 2k. Each boundary edge shares a vertex with at most two other


edges. If we randomly pick two edges of ∂Xk( g), the probability that they share a vertex is on the order of (3f − 2k)−1. This suggests that gluing stories that produce many vertices are quite rare.

In our proof, we turn this intuition into a precise estimate. Getting the quantitative result that we need from this approach was technically tricky, and we discuss this more below. For example, it is much easier to prove that |T(f, w)| ≤ Cfff/2w−w/2. However, this weaker estimate

is too weak for our applications in the paper, and we need to do some work to get the best estimate that we can.

In subsection 5.1 we estimate the overcounting and prove Lemma

- 5.3. In subsection 5.2 we prove Lemma 5.4.


- 5.1. Gluing stories for a given triangulated surface. In this section, we prove Lemma 5.3. If X is a connected triangulated surface with f faces, then we have to prove that there are at least C−ff5f/2 diﬀerent gluing stories  g ∈ GS(f) so that X( g) is simplicially isomorphic to X.


The simplicial automorphisms of a triangulated surface X will be involved in the proof. Let Aut(X) be the group of simplicial automorphisms of X. We will need the following well-known estimate.

Lemma 5.5. If X is a connected triangulated surface with f faces, then |Aut(X)| ≤ 6f.

Proof. Let ∆1 be a face in X. There are 6f simplicial isomorphisms from ∆1 to one of the faces of X. We claim that each of these maps extends to at most one simplicial isomorphism from X to itself.

Let φ1, φ2 : X → X be simplicial isomorphisms, and suppose that φ1 and φ2 agree on a 2-face ∆. We say that two faces ∆, ∆′ ⊂ X are adjacent if they have a common edge. We will show that φ1 and φ2 also agree on each simplex adjacent to ∆. Suppose that ∆′ is adjacent to ∆ and that e = ∆∩∆′ is the edge that they both contain. We know that φ1 and φ2 agree on the edge e. Now φ1(e) = φ2(e) is an edge of X, and so it lies in exactly two faces of X. We know that φ1(∆) = φ2(∆) is one of these faces. Since φ1 and φ2 are both simplicial isomorphisms, they must both map ∆ to the other of these faces. Now φ1 and φ2 agree on the edge e, and so they must also agree on the third vertex of ∆′, and so φ1 and φ2 agree on ∆′.

Now suppose φ1, φ2 are simplicial isomorphisms X → X that agree on ∆1. By the result of the last paragraph, they must agree on all the simplices that are adjacent to ∆1. Iterating the argument, they must agree on all the simplices adjacent to these simplices. Since X is connected, by iterating this argument, we see that φ1 and φ2 must agree everywhere.

Now we turn to the proof of Lemma 5.3.

Proof. Let X be a connected triangulated surface with f faces. First we check that there is a gluing story  g ∈ GS(f) so that X is simplicially isomorphic to X( g). Number the faces of X as F1, ..., Ff. For each face Fj, pick an identiﬁcation of the face with a standard simplex ∆j.

Now number the edges of X from 1 to 3f/2. Suppose that ek is the kth edge, and that it lies in faces Fj(k) and Fj′(k). The edge ek corresponds to an edge ∆j(k),a(k) ⊂ ∆j(k) and to an edge ∆j′(k),a′(k) ⊂ ∆j′(k). Since these two edges are identiﬁed in X, we get a simplicial isomorphism gk : ∆j(k),a(k) → ∆j′(k),a′(k). The sequence of gk make a gluing story  g ∈ GS(f) and X( g) is simplically isomorphic to X.

Given a gluing story  g, we now produce many other gluing stories that lead to the same surface X( g). These other gluing stories come from relabelling the characters in the initial gluing story  g. There are two diﬀerent kinds of relabelling that we can do. We can reorder the gluing maps gk. In other words, we can consider a gluing story with the same set of gluing maps in a diﬀerent order. Reordering the gluing maps gk deﬁnes an action of the symmetric group S3f/2 on GS(f). We can also relabel the simplices ∆1, ..., ∆f. This relabelling gives an action of Sf on GS(f). These two actions commute, and so we get an action of S3f/2 × Sf on GS(f). If  g and  g′ are in the same orbit of this action, then X( g) and X( g′) are simplicially isomorphic.

This action is not necessarily free. We note that |S3f/2 × Sf| = (3f/2)!f! ≥ C−ff5f/2. Recall that we found an element  g ∈ GS(f) so that X( g) is simplicially isomorphic to our given X. For every h in the S3f/2 × Sf-orbit of  g, X( h) is also simplicially isomorphic to X. The size of this orbit is |S3f/2 × Sf|/|Stab( g)|. (Here Stab( g) ⊂ S3f/2 × Sf is the stabilizer subgroup: the set of group elements ψ ∈ S3f/2 × Sf so that ψ( g) =  g.)

To ﬁnish the proof, we will check that |Stab( g)| ≤ |Aut(X)|. By

- Lemma 5.5 above, |Aut(X)| ≤ 6f. To see that |Stab( g)| ≤ |Aut(X)|, we will construct a natural injection Stab( g) → Aut(X( g)).


Suppose that (ψ1, ψ2) ∈ Stab( g), where ψ1 ∈ S3f/2 and ψ2 ∈ Sf. We use ψ2 to deﬁne a simplicial map from X( g) to itself. The map sends ∆j to ∆ψ

2(j) by the identity (remember, the ∆j are all copies of the standard 2-simplex). We have to check that this map respects all of the gluings. But if gk glues ∆j(k),a(k) to ∆j′(k),a′(k), then gψ

1(k)

2(j′(k)),a′(k) by the same simplicial isomorphism. Therefore, our map does respect all the gluings, and it gives a simplicial map. Applying the same construction with (ψ1−1, ψ2−1) we get an inverse simplicial map, so (ψ1, ψ2) was mapped to a simpicial isomorphism X → X.

glues ∆ψ

2(j(k)),a(k) to ∆ψ

We now have a group homomorphism Stab( g) → Aut(X(g)). We next show that this homomorphism is injective. Suppose that (ψ1, ψ2) ∈ Stab( g) corresponds to the identity map X → X. By construction, we see that ψ2 is the identity. But just reordering the gluing maps will

produce a diﬀerent gluing story unless ψ1 is the identity also. So the kernel of the homomorphism is the identity.

- 5.2. Gluing stories with many vertices. In this section, we prove Lemma 5.4. Recall that Lemma 5.4 gives a bound on the number of gluing stories  g ∈ GS(f) so that X( g) is a connected triangulated surface with w vertices.


Let  g ∈ GS(f) be a gluing story. For 0 ≤ k ≤ 3f/2, let Xk( g) be the space formed from the simplices ∆1, ..., ∆f by making identiﬁcations using the ﬁrst k gluing maps, g1, ..., gk. The space X0( g) is just a disjoint union of f simplices, and X3f/2( g) = X( g). To help understand the number of vertices in X( g), we will consider the vertices of Xk( g) for every k and keep track of how they change as k increases.

Before turning to the proof, we should talk brieﬂy about what type of object Xk( g) is. We observed above that for a general gluing story  g ∈ GS(f), the space X( g) may not be a triangulated surface. In Lemma 5.4, we can restrict attention to gluing stories so that X( g) is a triangulated surface. But even if X( g) is a triangulated surface, the spaces Xk( g) may not all be triangulated surfaces with boundary. For example, consider the second-to-last space X(3f/2)−1( g). The boundary of this space must consist of two edges, and the last gluing map g3f/2 glues together these two edges. These two edges must form a loop of length 2, which means that they have the same boundary vertices. Therefore, X(3f/2)−1( g) is not a simplicial complex, and so it is certainly not a triangulated surface with boundary.

The spaces Xk( g) are always pseudomanifolds with boundary. In Subsection 5.3, we give an appendix recalling all the deﬁnitions and facts about pseudomanifolds with boundary that we need.

For a general gluing story  g, the boundary of Xk( g) consists of a disjoint union of loops, and each loop consists of at least one edge. These loops are called the connected components of the boundary of Xk( g). For general  g, the boundary of Xk( g) may contain a loop with only one edge. However, if X( g) is a triangulated surface, then each component of the boundary of Xk( g) contains at least two edges. We can see this as follows. Since X( g) is a triangulated surface, in particular a simplicial complex, there is no edge in X( g) from a vertex to itself. But then Xk( g) cannot contain any edge from a vertex to itself either. For more details, see Subsection 5.3.

The pseudomanifold with boundary Xk+1 is formed from Xk by gluing together two of the boundary edges of Xk by the gluing map gk+1. To prove Lemma 5.4, we will pay attention to whether we glue together

“nearby” edges or ”far apart” edges. We say that two edges of ∂Xk are

adjacent if they share a vertex. We say that edges e and e′ in ∂Xk are D-near if there is a string of adjacent edges in ∂Xk, e = e0 adjacent to e1, ej adjacent to ej+1 for 1 ≤ j < D, and eD = e′. We will show that if X( g) is a triangulated surface with many vertices, then many of the gluing maps gk must glue together nearby edges. Here is a lemma that makes this precise.

- Lemma 5.6. For any δ > 0, there is a Dδ so that the following holds. Suppose that  g ∈ GS(f) is a gluing story and that X( g) is a triangulated surface with V (X) vertices and H(X) connected components. Suppose that N of the gluing steps gk glue together edges that are Dδ-near. Then


V (X) ≤ (1 + δ)N + H(X). In particular, if X( g) is a connected triangulated surface, then

V (X) ≤ (1 + δ)N + 1. First we prove that Lemma 5.6 implies Lemma 5.4.

Proof of Lemma 5.4 assuming Lemma 5.6. The point of the proof is that there are not very many ways to glue two nearby edges of ∂Xk. For any Xk, there are at most 12Dδf gluing maps gk+1 between edges that are Dδ near. This is because there are at most 3f edges for the domain of gk+1. Then there are at most 2Dδ edges that are Dδ near to the ﬁrst edge. Then there are at most two gluings from the ﬁrst edge to the second edge. There are at most 2(3f)2 = 18f2 possible gluing maps gk+1. Suppressing the constants, the number of possible gluing maps between nearby edges is ≤ Cδf, and the total number of possible gluing maps is ≤ Cf2.

The number of gluing stories in GS(f) with exactly N Dδ-near moves is at most

3f/2 N

(Cδf)N(Cf2)(3f/2)−N ≤ (3f/2)N(N!)−1(Cδf)N(Cf2)(3f/2)−N

≤ Cδff3f(N!)−1 ≤ Cδff3fN−N.

In other words:

- (8) |{ g ∈ GS(f)| g has exactly NDδ-near moves}| ≤ Cδff3fN−N.


Let GSw(f) ⊂ GS(f) be the set of gluing stories  g ∈ GS(f) so that X( g) is a connected triangulated surface with w vertices. Lemma 5.6 implies that for any  g ∈ GSw(f), the number of Dδ-near gluing maps in  g is at least w1+−δ1. By equation 8, we see that

![image 37](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile37.png>)

w

Cδff3fN−N ≤ Cδff3fw−

|GSw(f)| ≤

1+δ.

![image 38](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile38.png>)

N≥w1+−δ1

![image 39](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile39.png>)

Since δ > 0 is arbitrary, this proves Lemma 5.4.

Remark. We will give below a short proof that V (X) ≤ 2N. This bound is not strong enough to prove Lemma 5.4. Using the bound V (X) ≤ 2N in place of Lemma 5.6 in the argument above leads to the estimate |T(f, w)| ≤ Cfff/2w−w/2. This bound is much weaker than Theorem 5.1 when w is large. In Lemma 5.6, in the bound V (X) ≤ (1 + δ)N + H(X), it is important to get the right constant in front of the N.

Next we discuss why the number of connected components plays a role in Lemma 5.6. Consider gluing together a tetrahedron from four faces, ∆0, ∆1, ∆2, ∆3. For the ﬁrst three moves, we attach ∆1, ∆2, and ∆3 to the three edges of ∆0. These steps are gluings between edges in diﬀerent components. Then we do three more gluings and get a tetrahedron. The last three gluings connect nearby edges. If f is a multiple of 4, we can repeat this procedure f/4 times to get f/4 tetrahedra. The f/4 tetrahedra have V = f vertices. In this story, the number of gluings between nearby edges is N = 3f/4. So in this example V = (4/3)N, which is too large. But this example also has H = f/4 connected components. So we see that V = N + H. This example shows that we need to include the number of connected components in our estimate.

Next we classify gluing moves according to how they aﬀect the number of internal vertices of Xk. Before we do this, it is helpful to remark that if X( g) is a triangulated surface, then every edge of every Xk must have two diﬀerent endpoints.

Suppose that gk+1 is a gluing map from e1 to e2. If e1 and e2 share no vertices, we say that gk+1 is a gluing of type A. In this case, the gluing gk+1 creates no new internal vertices: Vint(Xk+1) = Vint(Xk). If e1 and e2 share exactly one vertex, we say that gk+1 is a gluing of type B. In this case, gk+1 creates one new internal vertex: Vint(Xk+1) =

- Vint(Xk) + 1. It can also happen that e1 and e2 share two vertices! In other words, e1 and e2 are both edges between the same two vertices


- v, v′. In this case, we say that gk+1 is a gluing of type C, and we note that Vint(Xk+1) = Vint(Xk) + 2.


The gluing maps of type C are crucial in our story, so we take a moment to describe an example. Such examples can occur even when

- X( g) is a triangulated surface. Suppose that f = 6 so that the gluing story has 3f/2 = 9 moves. The boundary of X7 has four edges. Suppose that X7 has one boundary component which consists of four edges. (This is not diﬃcult to arrange.) Next suppose that g8 glues together two adjacent edges of this boundary. So g8 is a gluing map


- of type B. Now X8 has one boundary component consisting of two edges. The gluing map g9 must glue together these two edges. So g9 is a gluing map of type C. Notice that the number of vertices of X( g) is Vint(X9) = Vint(X8) + 2.


The number of vertices of X( g) is Vint(X3f/2) = B + 2C, where we write B for the number of type B gluing maps in  g, and similarly for C. Gluing maps of type B or C are 1-near, and so we see that V (X) ≤ 2N. As we discussed above, this estimate is not strong enough to prove

- Theorem 5.1. We need to be more careful in how we deal with gluing maps of type C.


Now we begin the rigorous proof of Lemma 5.6:

Proof of Lemma 5.6. Here is the frame of the proof. We set Dδ = 101/δ. We will deﬁne some function F(Xk) and check the following properties.

- (1) F(X0) = 0.
- (2) F(X3f/2) = V (X) − H(X).
- (3) If gk+1 glues together two Dδ-near edges, then


F(Xk+1) ≤ F(Xk) + 1 + δ. If gk+1 glues together two edges which are not Dδ-near, then

F(Xk+1) ≤ F(Xk).

Given these properties, it is easy to ﬁnish the proof of the lemma. By Property 2, V (X)−H(X) = F(X3f/2). By Property 3, F(X3f/2) ≤ (1+ δ)N +F(X0). By Property 1, this is equal to (1+δ)N. So all together, we have V (X) − H(X) ≤ (1 + δ)N. Hence V (X) ≤ (1 + δ)N + H(X).

The main diﬃculty is to craft a function F that obeys these properties. The function F(Xk) will be the number of internal vertices of Xk plus some other terms. Before writing down the detailed formula, we try to motivate these other terms. A gluing of type C increases the number of internal vertices by 2, and it gets rid of a boundary component of length 2. Since F is only allowed to increase by 1 + δ, we decide that a boundary component of length 2 should contribute approximately 1 − δ to F. Now a gluing of type C only increases F by

- 1 + δ.


- But this patch creates new issues. For instance, if we glue together two edges in a boundary component of length 6, we can get two boundary components of length 2. The two boundary components of length
- 2 contribute approximately 2 − 2δ to F. Since F is only allowed to increase by 1 + δ, we decide that a boundary component of length 6 should contribute approximately 1 − 3δ to F. In general, a boundary component of length l contributes β(l) to F, where β(l) decreases slowly to zero. Note that if we glue together two edges that are Dδ far apart, we can create a new boundary component of length Dδ. When we glue far apart edges, F(Xk) cannot increase at all, so we have to arrange that β(l) = 0 for l ≥ Dδ.


But this scheme leads to another issue. The initial conﬁguration X0 has many boundary components of length 3. We want F(X0) = 0. To ﬁx this problem, we only count some of the boundary components. More precisely, for each component X′

k ⊂ Xk, we don’t include the boundary contribution from the longest boundary component of Xk′. In particular, each component of X0 has only a single boundary component and so the boundary contribution of X0 is zero, as desired.

This modiﬁcation creates yet another small issue. Suppose that we do a gluing move of type C on a boundary component of length 2 which is the only boundary component of some component X′

k ⊂ Xk. The boundary component of length 2 no longer contributes to F(Xk), and we still create two new internal vertices. In this situation, we also create a new closed connected component of Xk+1. (A connected component Xk′ ⊂ Xk is closed if it has no boundary.) We decide that each closed component of Xk contributes −1 to F(Xk). In this situation, the number of internal vertices goes up by two, but the number of closed components goes up by 1, and so F increases by only 1.

With this motivation, we are ready to give the precise deﬁnition of F(Xk) and check all of the properties. The function F(Xk) is a sum of three terms:

F(Xk) = Vint(Xk) − Hcl(Xk) + B(Xk),

The terms are as follows. Vint is the number of interior vertices of Xk. Hcl(Xk) is the number of closed components of Xk: the number of components of Xk which are pseudomanifolds without boundary. And B(Xk) is a boundary term involving the lengths of the boundary components of Xk.

For l ≥ 1, we deﬁne β(l) = max(0, 1 − δ log10 l). We have β(l) ≥ 0, with β(l) = 0 for all l ≥ Dδ = 101/δ. We see that β(1) = 1, and we note that β is decreasing.

For a connected component Y ⊂ ∂Xk, we let l(Y ) denote the length of Y (i.e. the number of edges in Y ). For a connected component Xk′ ⊂ Xk, we deﬁne

lmax(Xk′) := max

l(Y ). For a connected component X′

Y a conn. compon. of Xk′

k ⊂ Xk, we deﬁne B(X′

k) as follows:

β(l(Y ))

B(Xk′) = 

 − β(lmax(Xk′)).



Y a conn. compon. of Xk′

Finally, we deﬁne B(Xk) as a sum of contributions from the connected components:

B(Xk′).

B(Xk) :=

Xk′ a conn. compon. of Xk

This ﬁnishes the deﬁnition of F(Xk), and now we have to check Properties 1-3.

- Property 1. We know that X0 is a disjoint union of f 2-simplices. It has no interior vertices. It has no closed components. Each component of X0 has a single boundary component of length 3, and so B(X0) = 0. Therefore, F(X0) = 0 proving Property 1.
- Property 2. It’s also easy to analyze F(X3f/2). We know that X3f/2 = X( g) has no boundary, so the complicated term B(X3f/2) vanishes. That leaves F(X3f/2) = Vint(X3f/2) − Hcl(X3f/2). Since X3f/2 has no boundary, all its vertices are interior vertices, and all its connected components are closed. Therefore, F(X3f/2) = V (X) − H(X), proving Property 2.
- Property 3. We have to compare F(Xk+1) and F(Xk). We consider separately the cases that gk+1 has type A, B, or C. We begin with type C, because it plays such an important role in the problem.


Suppose that gk+1 has type C. By the deﬁnition of type C, the map gk+1 glues together two edges that share two vertices. A map

- of type C is 1-near, so we have to show that F(Xk+1) ≤ F(Xk) +


- 1 + δ. The map gk+1 creates two new interior vertices: Vint(Xk+1) =


- Vint(Xk) + 2. The two edges that are glued together by gk+1 form a


boundary component Y of length 2 in ∂Xk. Suppose that Y ⊂ ∂X′

k

for a connected component Xk′ ⊂ Xk. Now we consider two cases.

- • Suppose that Y is the whole boundary of X′


k. In this case, the gluing step does not change the boundary term: B(Xk+1) = B(Xk). Also, the number of closed components increases by

1: Hcl(Xk+1) = Hcl(Xk) + 1. Assembling all the terms, we get F(Xk+1) = F(Xk) + 1.

- • Suppose that Xk′ has other boundary components. In this case, the gluing step reduces the boundary term by β(2): B(Xk+1) = B(Xk) − β(2). The number of closed components remains the same. Assembling all the terms, we get F(Xk+1) = F(Xk) + 2 − β(2) = F(Xk) + 1 + δ log10(2).


Next, we suppose that gk+1 has type B. The map glues together two adjacent edges in a boundary component of some length l ≥ 3. A gluing of type B is 1-near, so again we have to prove that F(Xk+1) ≤ F(Xk) + 1 + δ. The gluing creates one new interior vertex. It does not change the number of closed components. The boundary term may increase by at most β(l − 2) − β(l) ≤ δ log10 l−l2 ≤ δ log10 3 ≤ δ. Therefore, F(Xk+1) ≤ F(Xk) + 1 + δ.

![image 40](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile40.png>)

Finally we suppose that gk+1 has type A. In this case, the number of interior vertices and the number of closed components do not change, so we only need to analyze the boundary term. A gluing map of type A may or may not be Dδ-near. The type A case has a number of sub-cases

- as follows.


- (1) The map gk+1 glues together two edges in the same component of ∂Xk.
- (2) The map gk+1 glues together two edges in diﬀerent components of ∂Xk, but in the same component of Xk.
- (3) The map gk+1 glues together two edges in diﬀerent components of Xk.


We ﬁrst consider Case 1: the map gk+1 glues together two edges in the same component of ∂Xk. Suppose that this boundary component has length l ≥ 3. After the gluing, depending on the orientation of the gluing, the boundary component of length l either becomes two boundary components of lengths l1, l2 ≥ 2 where l1+l2+2 = l, or else it becomes one boundary component of length l−2. The most interesting case is when the boundary component splits into two components of lengths l1, l2. We discuss this case ﬁrst. We begin by noting that l ≥ max(l1, l2). We let X′

k be the component of Xk that contains the edges where gk+1 acts. We let Xk′+1 be the corresponding component of Xk+1. Now the change in the boundary term is

- (9) B(Xk+1)−B(Xk) = −β(l)+β(l1)+β(l2)+β(lmax(Xk′))−β(lmax(Xk′+1).


If the gluing gk+1 is Dδ-far, then l1, l2, l are all at least Dδ, and hence lmax(X′

k) and lmax(X′

k+1) are also at least Dδ. Therefore, all the terms on the right-hand side of equation 9 vanish.

If the gluing gk+1 is Dδ-near, then we note that lmax(X′

k+1) ≤ lmax(X′

k). Therefore,

B(Xk+1) − B(Xk) ≤ −β(l) + β(l1) + β(l2). This increase is acceptable by the following lemma:

- Lemma 5.7. Suppose that l1, l2 ≥ 2 and l ≥ 3 are integers with l1 + l2 + 2 = l. Then β(l1) + β(l2) − β(l) ≤ 1 + δ.


Proof. We can assume that l1 ≤ l2. Since l1, l2 ≥ 2, we have l ≥ l1, l2. If β(l2) = 0, then β(l1) + β(l2) − β(l) ≤ β(l1) ≤ 1. So we can assume that β(l1) and β(l2) are positive. Then we get

β(l1) + β(l2) − β(l) ≤ (1 − δ log10(l1)) + (1 − δ log10(l2)) − (1 − δ log10(l))

= 1 + δ (log10(l) − log10(l1) − log10(l2)) .

It suﬃces to prove that the expression in parentheses is ≤ 1. Since

- 2 ≤ l1 ≤ l2, we have l1l2 ≥ l1 + l2 and so


log10(l1) + log10(l2) ≥ log10(l1 + l2)

= log10(l − 2). So we have

log10(l) − log10(l1) − log10(l2) ≤ log10(l) − log10(l − 2)

l l − 2

= log10(

)

![image 41](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile41.png>)

≤ log10 3 ≤ 1.

Now we turn to the simpler possiblity that gk+1 glues together two edges of a boundary component of length l, turning it into a single component of length l − 2. (The orientation of the gluing map determines whether the boundary component of length l splits into two boundary components or remains a single connected component of the boundary of Xk+1.) In this case,

B(Xk+1) − B(Xk) = −β(l) + β(l − 2) + β(lmax(Xk′)) − β(lmax(Xk′+1) ≤ −β(l) + β(l − 2).

If gk+1 is Dδ-far, then all the terms vanish. If gk+1 is Dδ-near, then −β(l) + β(l − 2) ≤ δ log10 l−l2 ≤ δ.

![image 42](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile42.png>)

This ﬁnishes the analysis of Case 1, and now we turn to Case 2: the map gk+1 glues together two edges in diﬀerent components of ∂Xk, but in the same component X′

k ⊂ Xk. Suppose that the two components in ∂Xk′ have lengths l1, l2 and the new component in ∂Xk′+1 has length l3 = l1 + l2 − 2 ≥ max(l1, l2). Note that in Case 2, the gluing map is automatically Dδ far, and so we have to prove that B(Xk+1) ≤ B(Xk). We expand

- (10) B(Xk+1)−B(Xk) = −β(l1)−β(l2)+β(l3)+β(lmax(Xk′))−β(lmax(Xk′+1)).


We note that

lmax(Xk′+1) = max(lmax(Xk′), l3). In the ﬁrst case, the two lmax terms cancel in equation 10, leaving

B(Xk+1) − B(Xk) = −β(l1) − β(l2) + β(l3) ≤ −β(l1) ≤ 0. In the second case, the lmax(X′

k+1) term and the l3 term cancel in

- equation 10 leaving


B(Xk+1) − B(Xk) = −β(l1) − β(l2) + β(lmax(Xk′)) ≤ −β(l1) ≤ 0. This ﬁnishes the analysis of Case 2, and now we turn to Case 3: the

map gk+1 glues together two edges in diﬀerent components of Xk, say X′

k and X′′

k. The map gk+1 glues together an edge from a component of X′

k with length l1 and an edge from a component of X′′

k with length l2. After the gluing, X′

k and X′′

k have merged into one component Xk′′′+1 ⊂ Xk+1, and the boundary components of lengths l1 and l2 have merged into one component of length l3 = l1+l2−2. We note as above that l3 ≥ max(l1, l2). In Case 3, the gluing map gk+1 is automatically Dδ-far, and so we have to prove that B(Xk+1) ≤ B(Xk).

We expand B(Xk+1) − B(Xk) to get

- (11) − β(l1) − β(l2) + β(l3) + β(lmax(Xk′)) + β(lmax(Xk′′)) − β(lmax(Xk′′′+1)).


We note that

lmax(Xk′′′+1) = max(lmax(Xk′), lmax(Xk′′), l3) . The ﬁrst two cases are equivalent. If lmax(X′′′

k+1) = lmax(X′

k), then those two terms cancel from equation 11, leaving B(Xk+1) − B(Xk) =

−β(l1) − β(l2) + β(l3) + β(lmax(Xk′′)) ≤ −β(l1) + β(l3) ≤ 0. On the hand, if lmax(X′′′

k+1) = l3, then those two terms cancel from

- equation 11, leaving B(Xk+1) − B(Xk) =


−β(l1) + β(lmax(Xk′)) − β(l2) + β(lmax(Xk′′)) ≤ 0.

This ﬁnishes the analysis of Case 3. We have now checked Properties 1-3, ﬁnishing the proof of Lemma 5.6.

There are a number of open questions about counting surfaces with various restrictions related to the material in this section. First of all, it would be interesting to ﬁnd upper and lower bounds for |T(f, w)| that are as close together as possible. It would also be interesting to estimate the number of connected pseudomanifolds with f faces and w vertices, up to combinatorial equivalence. Finally, it would be interesting to consider generalizations to higher dimensions. There are several variations in higher dimensions. From the point of view of studying the d-dimensional girths of d-dimensional complexes, it would be helpful to estimate the number of connected d-dimensional simplicial complex pseudomanifolds with f d-faces and w vertices. (A simplicial complex pseudomanifold is a pseudomanifold which is also a simplicial complex.) It would also be interesting to estimate the number of connected d-dimensional pseudomanifolds with f faces and

- w vertices.


- 5.3. Background on pseudomanifolds. In this section, we provide background on pseudomanifolds. We recall the deﬁnition of a pseudomanifold and a pseudomanifold with boundary. We will see that


the spaces Xk( g) are all pseudomanifolds with boundary. We will deﬁne vertices, edges, faces, and connected components of a pseudomanifold. We will see that the boundary of a d-dimensional pseudomanifold with boundary is itself a (d − 1)-dimensional pseudomanifold (without boundary). As a result, we will see that the boundary of Xk( g) consists

of ﬁnitely many components and that each components is a loop with

- at least one edge. Finally, if X( g) is a triangulated surface, then we


will check that each component of the boundary of Xk( g) contains at least two edges.

A d-dimensional pseudomanifold is made by gluing together d-dimensional simplices. Suppose that ∆1, ∆2, ..., ∆f are copies of the standard (closed) d-simplex. (In this paper, we always work with ﬁnite pseudomanifolds, made from ﬁnitely many simplices.)

We glue facets of these ∆j together using simplicial isomorphisms. Each ∆j has d + 1 facets, which we label as ∆j,a with a = 0, ..., d. A gluing is deﬁned by specifying two (diﬀerent) facets, ∆j,a and ∆j′,a′ and giving a simplicial isomorphism from ∆j,a to ∆j′,a′. (Technical remark. Gluing a facet ∆j,a to itself is not allowed. But gluing a facet ∆j,a to another facet of the same simplex, ∆j,a′, is allowed.)

A pseudomanifold is speciﬁed by a set of gluings where each facet of

the ∆j is involved in exactly one gluing. Recalling the deﬁnition of a gluing story, it follows immediately that for any gluing story  g, X( g) is a 2-dimensional pseudomanifold.

A pseudomanifold with boundary is speciﬁed by a set of gluings where each facet of the ∆j is involved in at most one gluing. It follows that for each  g ∈ GS(f) and each k, Xk( g) is a pseudomanifold with boundary.

A pseudomanifold (possibly with boundary) leads to an underlying topological space by identifying any points that have been glued together. The set of points in the pseudomanifold is formally deﬁned as follows. We begin with the union of the simplices ∆1, ∆2, ... If a gluing map takes one point to another point, then those points are equivalent. These equivalences generate equivalence classes. A point of the pseudomanifold is an equivalence class of the original points.

We can deﬁne the k-dimensional faces of a pseudomanifold (possibly with boundary) in a similar way. We begin with the set of kdimensional faces of the simplices ∆j. Two k-dimensional faces are equivalent if one of our gluing maps maps one of them onto the other. These equivalences generate an equivalence relation on the set of kfaces. A k-face of the pseudomanifold is an equivalence class for this relation. In particular, we can deﬁne the vertices of a pseudomanifold

- as the 0-dimensional faces. Two d-dimensional faces can never be glued together, so the d-faces of a d-dimensional pseudomanifold are just the


original d-dimensional simplices ∆1, ∆2,...

For example, a 1-dimensional pseudomanifold without boundary is a ﬁnite collection of circles, where each circle is made from some number of intervals connected end-to-end. A 1-dimensional pseudomanifold

can be made from a single interval with its two boundary points glued together. So each circle can have any number of edges ≥ 1.

Next we deﬁne connected pseudomanifolds. Two simplices ∆j and ∆j′ are adjacent if two of their facets have been glued together. We say ∆j is connected to ∆j′ if there is a sequence of adjacent simplices starting with ∆j and ending with ∆j′. We say that a pseudomanifold is connected if every two simplices are connected. Any pseudomanifold (possibly with boundary) is a ﬁnite union of disjoint connected pseudomanifolds, its connected components.

Now we deﬁne the boundary of a pseudomanifold with boundary. Consider a d-dimensional pseudomanifold with boundary, X, formed from d-simplices ∆1, ∆2, ... by some gluing maps g1, g2, ... A facet ∆dj,a−1 ⊂

∆dj is called a boundary simplex if it is not involved in any of the gluing maps. (We write the exponent d − 1 to recall that the dimension

of ∆dj,a−1 is d − 1.) It turns out that the boundary simplices form a (d − 1)-dimensional pseudomanifold without boundary.

If ∆dj,a−1 is a boundary simplex, and ∆dj,a,b−2 ⊂ ∆dj,a−1 is one of its facets, then we have to prove that the equivalence class of ∆j,a,b lies in exactly one other boundary simplex. We will describe the equivalence class of ∆j,a,b in terms of the gluing maps.

The facets of a boundary simplex are (d − 2)-dimensional. To help study them, we deﬁne some notation to describe the (d−2)-dimensional facets of a d-simplex. Recall that if ∆j is one of our d-simplices, then its facets are ∆j,a with a = 0, ..., d. Any (d − 2)-face of ∆j is contained in exactly two of the facets of ∆j. For any a = b, we write ∆dj,a,b−2 := ∆dj,a−1 ∩ ∆dj,b−1 ⊂ ∆dj.

We are considering a boundary simplex ∆j,a and one of its facets ∆j,a,b. If ∆dj,b−1 is also a boundary simplex, then the equivalence class of ∆j,a,b is just {∆j,a,b}, and it is a facet of ∆j,a and ∆j,b. In this case, we are done.

Now suppose that ∆dj,b−1 is not a boundary simplex, i.e. it is involved in a gluing. Suppose that ∆dj,b−1 is glued to ∆dj−1

1,a1 ⊂ ∆dj

. This gluing identiﬁes ∆dj,a,b−2 with a (d − 2)-face ∆dj−2

1

1,a1,b1 ⊂ ∆dj−1

1,a1. As above, we use the convention that ∆dj−2

1,a1,b1 = ∆dj−1

1,a1 ∩ ∆dj−1

1,b1. If ∆j

1,b1 is a boundary simplex, then the equivalence class of ∆j,a,b is {∆j,a,b, ∆j

- 1,a1,b1}, and it

is a facet of exactly two boundary simplices: ∆j,a and ∆j

- 1,b1.


2,a2. This gluing map identiﬁes ∆j,a,b with some (d − 2)-face ∆dj−2

If ∆j

1,b1 is not a boundary simplex, then it is glued to some ∆j

2,a2,b2 = ∆dj−1

2,a2 ∩ ∆dj−1

. The general picture is as follows. For i = 1, ..., t, ∆j

2,b2 ⊂ ∆j

2

i,bi is glued to ∆j

i+1,ai+1, which identiﬁes ∆j

i,ai,bi with ∆j

i+1,ai+1,bi+1.

t,bt is another boundary simplex. This procedure has to stop with another boundary simplex, ∆j

The face ∆j

t,bt, because the (d − 1)-faces ∆j

i,bi are all distinct. Now the equivalence class of ∆j,a,b is exactly {∆j,a,b, ∆j

i,ai and ∆j

t,at,bt}. It is the facet of exactly two boundary simplices: ∆j,a and ∆j

1,a1,b1, ..., ∆j

t,bt.

This ﬁnishes our explanation of the structure of the boundary of a pseudomanifold with boundary. In particular, we see that ∂Xk( g) is a 1-dimensional pseudomanifold without boundary. By the classiﬁcation we described above, ∂Xk( g) is a ﬁnite union of circles each containing

- at least one edge. Finally, we check that if X( g) is a triangulated surface, then each


component of ∂Xk( g) contains at least two edges. Since X( g) is a triangulated surface, each edge of X( g) has two distinct vertices. This implies that each edge of Xk( g) has two distinct vertices. Therefore, each edge of ∂Xk( g) has two distinct vertices, and so each component of ∂Xk( g) contains at least two edges.

6. Comments

- 6.1. Filling area of cycles in random 2-complexes. Over the past ten years or so, the topology of random 2-complexes has been well studied. This area began with Linial and Meshulam’s paper [6]. The Linial–Meshulam theorem describes the vanishing threshold for homology. Theorem (Linial–Meshulam, 2006). Let Y = Y (n, p).


If

2 log n + ω(1) n

p ≥

![image 43](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile43.png>)

then with high probability H1(Y, Z/2Z) = 0, and if p ≤

2 log n − ω(1) n

,

![image 44](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile44.png>)

then with high probability H1(Y, Z/2Z) = 0. (Here ω(1) denotes any function that tends to inﬁnity as n → ∞.)

A geometric reﬁnement of this picture would be to understand the typical ﬁlling area of cycles, i.e. in the typical number of triangles in the minimal bounding chain for a given cycle. For instance, what is the typical ﬁlling area of the length 3 1-cycle 123 in Y ? The LinialMeshulam theorem gives an upper bound as follows. Consider the sub complex of Y restricted to the ﬁrst s vertices. This sub-complex is

chosen according to Y (s, p). If p > sǫ−1 > 2 logs s, then with high probability the ﬁrst homology of the sub complex vanishes by the theorem

![image 45](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile45.png>)

of Linial-Meshulam. Therefore, the cycle 123 bounds a 2-chain in this sub complex. But the number of 2-faces in the sub-complex is at most Cps3 with high probability. Therefore, with high probability, the ﬁlling area of 123 is at most Cp−2−ǫ. If p = nα−1, then with high probability

- Y has about n2+α 2-faces and the ﬁlling area of 123 is at most n2−2α+ǫ. The techniques of this paper allow one to prove that this upper bound is essentially sharp when 0 ≤ α < 1/2.


- Theorem 6.1. Let α ∈ 0, 21 and ǫ > 0. Suppose p = nα−1, so the expected number of faces in Y (n, p) is n2+α. Let A be the ﬁlling area of the cycle 123 in Y . Then with high probability


![image 46](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile46.png>)

n2−2α−ǫ ≤ A ≤ n2−2α+ǫ.

The new part of Theorem 6.1 is the lower bound. The proof of the lower bound is very similar to the proof of Theorem 4.1. One counts ﬁllings of the 1-cycle 123 instead of counting 2-cycles, but the counts are closely related since adding a triangle to a ﬁlling results in a cycle. The only diﬀerence has to do with small ﬁllings or small cycles. A small ﬁlling of 123 gives rise to a small inclusion-minimal cycle which contains the vertices 123. The number of such cycles in Y goes to zero, although the total number of small inclusion-minimal cycles does not. Here is a more detailed explanation.

With high probability, Y does not contain the face with vertices 123. If c is a 2-chain in Y bounded by the cycle 123 and with a minimal number of 2-faces, then adding the face with vertices 123 to c gives an inclusion-minimal 2-cycle in ∆(2)n .

Recall that an inclusion-minimal 2-cycle was called small if it contains at most M vertices for M = M(α) deﬁned in Section 4.1. Similarly, an inclusion minimal ﬁlling of 123 is called small if it contains at most M vertices. The small cycles in Y were estimated in Section 4.2 using barely-dense subcomplexes. Recall that a barely dense subcomplex of Y is a subcomplex with v vertices and 2v − 4 faces. Each small inclusion-minimal 2-cycle contains a barely dense subcomplex. Similarly, an inclusion-minimal small ﬁlling of the cycle 123 must contain a sub complex of Y with v vertices and 2v −5 faces of Y , and containing the vertices 1, 2, and 3. The expected number of such sub-complexes in Y is

M

v=4

n v − 3

v 3

2v − 4

p2v−5.

This sum is decreasing in v, and so it is dominated by M times the ﬁrst term. Hence the sum is

≤ Cαnp3 = Cαn3α−2.

Since α < 1/2, this is at most Cαn−1/2, and so with high probability, there is no small ﬁlling of Y . The rest of the proof of Theorem 6.1 is the same as the proof of Theorem 4.1.

- 6.2. Comparison with earlier work. Aronshtam, Linial,  Luczak, and Meshulam studied the threshold for collapsibility of random ddimensional simplicial complexes in [2]. In Section 4 they provide an

upper bound on Cd(n, m), the number of minimal core d-complexes with n vertices and m facets. This is in turn gives an upper bound on the number of inclusion-minimal cycles with n vertices and m facets, since every cycle is a minimal core.

So their estimate can be used to count cycles in random complexes. In the case we are interested in, d = 2, their estimate implies the following.

Theorem 6.2.

- (1) For any C > 0, for all n suﬃciently large, there exist simplicial complexes ∆ with n vertices and with at least Cn2 faces, such that every cycle in H2(∆) is supported on at least f(C)n2 faces.
- (2) For α > 0, for all n suﬃciently large, there exist simplicial complexes ∆ with n vertices and with at least n2+α faces, such


that every cycle in H2(∆) is supported on at least Cαn2−16α faces.

Part (1) of Theorem 6.2 is slightly stronger than our Theorem 4.1 in the regime m = θ (n2), and is optimal up to a constant factor by Theorem 3.1. On the other hand, part (2) of this theorem is weaker than Theorem 4.1 for α > 0, since

2 − 16α < 2 − 2α − ǫ for suﬃciently small ǫ.

- 6.3. Volume distortion. By combining Theorem 6.1 with a standard probabilistic technique (see for example the proof of Proposition 4.2 in [5]), another estimate is obtained:


Proposition 6.3. Let Y = Y (n, p) be a random complex with p = nα−1. Let ǫ > 0 be given. For each 1-cycle, τ, of length 3 (e.g. 123 as

above), let FillY (τ) = min{ y  | y ∈ C2(Y ; Z/2Z) and ∂y = τ}. Then for suﬃciently large n (depending on ǫ) with high probability

τ∈(

n 3

(FillY (τ))2 ≥

)

n 3

n2−2α−ǫ 2 .

This leads immediately to an improvement of Theorem 1.2 in [5]:

Theorem 6.4. Let Y (n, p) be as in Proposition 6.3. Let ǫ > 0. Then with high probability, for every map φ : Y → H from Y to a Hilbert space H which is aﬃne on each simplex,

FillH(φτ) FillY (τ) ≥ cn2−2α−ǫ,

FillY (τ) FillH(φτ) · max τ∈(

max τ∈(

![image 47](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile47.png>)

![image 48](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile48.png>)

)

)

n 3

n 3

where FillH(φτ) refers to the area of the convex hull of φ(τ). In particular, by taking α > 0 arbitrarily small, we see that for every δ > 0, and for every large enough n > C = Cδ, there exists a 2dimensional simplicial complex, Y with complete 1-skeleton, such that every map, φ : Y → H, from Y to a Hilbert space H, which is aﬃne on each simplex has that

FillY (τ) FillH(φτ) · max τ∈(

FillH(φτ) FillY (τ) ≥ cn2−δ.

max τ∈(

![image 49](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile49.png>)

![image 50](<2015-dotterrer-2-complexes-large-2-girth_images/imageFile50.png>)

)

)

n 3

n 3

The left hand side of this inequality is referred to in [5] as the ﬁlling distortion of φ and is a natural homological analogue of much studied phenomenon of metric distortion (see [7] for a survey).

The following is one way to think about this theorem. For any complex Y with complete 1-skeleton, we could embed that complex into Euclidean space by sending the n vertices to the standard basis elements of Rn. In that case, the convex hull of any triangle has area O(1) and ﬁlling distortion is bounded from below by maxτ FillY (τ), which is at most |Y (2)|. If we choose α > 0 small and positive, then with high probability |Y (2)| ∼ n2+2α and the distortion is at least around n2−2α, which are very close to each other. For such Y , this naive, “equilateral” embedding achieves essentially the best result.

The analogous statement in the context of graphs is the following: for expander graphs with n vertices, every embedding into Euclidean requires Ω(log n) metric distortion, and since the diameter of such an

expander graph is at most O(log n), an embedding that sends the vertices to the standard basis of Rn achieves essentially the minimal possible distortion.

References

- [1] Noga Alon, Shlomo Hoory, and Nathan Linial. The Moore bound for irregular graphs. Graphs Combin., 18(1):53–57, 2002.
- [2] Lior Aronshtam, Nathan Linial, Tomasz  Luczak, and Roy Meshulam. Collapsibility and vanishing of top homology in random simplicial complexes. Discrete Comput. Geom., 49(2):317–334, 2013.
- [3] Robert Brooks and Eran Makover. Random construction of Riemann surfaces. J. Diﬀerential Geom., 68(1):121–157, 2004.
- [4] Reinhard Diestel. Graph theory, volume 173 of Graduate Texts in Mathematics. Springer, Heidelberg, fourth edition, 2010.
- [5] Dominic Dotterrer. Higher dimensional distortion of random complexes. to appear in Math Research Letters, arXiv:1210.6951, 2012.
- [6] L. Linial and R. Meshulam. Homological connectivity of random 2-complexes. Combinatorica, 26(4):475–487, 2006.
- [7] N. Linial, A. Magen, and A. Naor. Girth and Euclidean distortion. Geom. Funct. Anal., 12(2):380–394, 2002.
- [8] V. T. So´s, P. Erdo˝s, and W. G. Brown. On the existence of triangulated spheres in 3-graphs, and related problems. Period. Math. Hungar., 3(3-4):221–228, 1973.


