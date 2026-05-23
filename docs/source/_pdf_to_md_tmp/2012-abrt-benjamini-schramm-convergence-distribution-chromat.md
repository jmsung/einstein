# arXiv:1201.3861v3[math.CO]16May2013

## Benjamini-Schramm convergence and the distribution of chromatic roots for sparse graphs

Miklo´s Abe´rt and Tama´s Hubai November 27, 2024

Abstract

We deﬁne the chromatic measure of a ﬁnite simple graph as the uniform distribution on its chromatic roots. We show that for a BenjaminiSchramm convergent sequence of ﬁnite graphs, the chromatic measures converge in holomorphic moments.

As a corollary, for a convergent sequence of ﬁnite graphs, we prove that the normalized log of the chromatic polynomial converges to an analytic function outside a bounded disc. This generalizes a recent result of Borgs, Chayes, Kahn and Lova´sz, who proved convergence at large enough positive integers and answers a question of Borgs.

Our methods also lead to explicit estimates on the number of proper colorings of graphs with large girth.

### 1 Introduction

Let G be a ﬁnite undirected graph without multiple edges and loops. A map f : V (G) → {1,...,q} is a proper coloring if for all edges (x,y) ∈ E(G) we have f(x) = f(y). For a positive integer q let chG(q) denote the number of proper colorings of G with q colors. Then chG is a polynomial in q, called the chromatic polynomial of G. The complex roots of chG are called the chromatic roots of G.

The study of chromatic polynomials and its roots has been initiated by Birkhoﬀ. Since then, the subject has gotten considerable interest, partially because of its connection to statistical mechanics. In particular, the chromatic roots control the behaviour of the antiferromagnetic Potts model at zero temperature. For a survey on the subject see [13].

For a ﬁnite graph G, a ﬁnite rooted graph α and a positive integer R, let P(G,α,R) denote the probability that the R-ball centered at a uniform random vertex of G is isomorphic to α. We say that a graph sequence (Gn) of bounded degree is Benjamini-Schramm convergent if for all ﬁnite rooted graphs α and R > 0, the probabilities P(Gn,α,R) converge (see [3]). This means that one can not statistically distinguish Gn and Gn for large n and n by sampling them from a random vertex with a ﬁxed radius of sight. An example (that is regularly used in statistical physics) is to approximate the inﬁnite lattice Zd by

bricks with all the side lengths tending to inﬁnity. More generally, amenable vertex transitive graphs can be obtained as the Benjamini-Schramm limits of their Følner sequences.

For a simple graph G let µG, the chromatic measure of G denote the uniform distribution on its chromatic roots. By a theorem of Sokal [12], µG is supported on the open disc of radius Cd around 0, denoted by

D = B(0,Cd) where d is the maximal degree of G and C < 8 is an absolute constant.

- Theorem 1.1 Let (Gn) be a Benjamini-Schramm convergent graph sequence of absolute degree bound d, and D an open neighborhood of the closed disc D. Then for every holomorphic function f : D → C, the sequence

D

f(z)dµG

n

(z)

converges.

Let ln denote the principal branch of the complex logarithm function. For a simple graph G and z ∈ C let

tG(z) =

lnchG(z) |V (G)|

where this is well-deﬁned. In statistical mechanics, tG(z) is called the entropy per vertex or the free energy at z. In their recent paper [4], Borgs, Chayes, Kahn and Lov´sz proved that if (Gn) is a Benjamini-Schramm convergent graph sequence of absolute degree bound d, then tG

n

(q) converges for every positive integer q > 2d. Theorem 1.1 yields the following.

- Theorem 1.2 Let (Gn) be a Benjamini-Schramm convergent graph sequence of


absolute degree bound d with |V (Gn)| → ∞. Then tG

(z) converges to a real analytic function on C \ D.

n

(z) converges for all z ∈ C \ D. Theorem 1.2 answers a question of Borgs [2, Problem 2] who asked under which circumstances the entropy per vertex has a limit and whether this limit is analytic in 1/z. Note that for an amenable quasi-transitive graph and its Følner sequences, this was shown to hold in [9].

In particular, tG

n

To prove Theorem 1.1 we show that for a ﬁnite graph G and for every k, the number

zkdµG(z)

pk(G) = |V (G)|

D

can be expressed as a ﬁxed linear combination of hom(H,G) where the H are connected ﬁnite graphs and hom(H,G) denotes the number of graph homomorphisms from H to G. Since a sequence of graphs Gn of bounded degree is Benjamini-Schramm convergent if and only if

hom(H,Gn) |V (Gn)| converges for all connected graphs H. This gives convergence of all the holomorphic moments of µG

, and this is equivalent to Theorem 1.1. For instance, for the fourth moment we get p4(G) = −13 hom( ,G)+43 hom( ,G)−21 hom ,G +13 hom ,G + hom ,G − 12 hom ,G + hom ,G − 13 hom ,G −

n

- 1

3 hom ,G + 13 hom ,G + 52 hom ,G − 2hom ,G +

- 2hom ,G − hom ,G + hom ,G − 21 hom ,G +

- 1


- 3 hom ,G − 301 hom ,G .

One could speculate that assuming Benjamini-Schramm convergence of Gn, maybe the complex measures µG

n

themselves will weakly converge. That is, Theorem 1.1 would hold for any continuous real function on D or, equivalently, convergence would hold in all the moments

D

zkzjdµG

n

(z).

However, this is not true in general, as the following easy counterexample shows. Let Pn denote the path of length n and let Cn denote the cycle of length n. Then Pn and Cn converge to the same object, the inﬁnite rooted path, while we have

chP

n

(z) = z(z − 1)n−1 and chC

n

(z) = (z − 1)n + (−1)n(z − 1). Thus, the weak limit of µP

n

is the Dirac measure on 1 and the weak limit of µC

n

is the normalized Lebesgue measure on the unit circle centered at 1. Still, using Theorem 1.1, we are able to prove the weak convergence of µG

n

for some natural sequences of graphs. For example, let Tn = C4×Pn denote the

- 4 × n tube, i.e. the cartesian product of the 4-cycle with a path on n vertices.


- Tn is a 4-regular graph except at the ends of the tube.


Proposition 1.3 The chromatic measures µT

n

weakly converge.

The proof is as follows: as Salas and Sokal [11] showed, the pointwise limit X of supports of µT

##### is part of a particular algebraic curve, so any subsequential weak limit is supported on X. The complement of X is connected, so by

n

Mergelyan’s theorem [8], every continuous function on X can be uniformly approximated by polynomials. Using Theorem 1.1 this yields weak convergence of µT

. See Section 4 for details. In this case one can use the so-called transfer matrix method to control the support of the chromatic measures (see [11] for various models related to the square lattice). In general, even for models of the square lattice, the complement of the limiting set may not be connected, and hence one can not invoke Mergelyan’s theorem. It is expected, however, that for any model where the transfer matrix method can be used, the chromatic measures do converge weakly.

n

Another naturally interesting case is when the girth of G (the minimal size of a cycle) is large. One can show that

zkdµ(z) = |E(G)| |V (G)|

D

(1 ≤ k ≤ girth(G) − 2)

that is, the moments are all the same until the girth is reached (see Lemma 5.2). This implies that for a sequence of d-regular graphs Gn with girth tending to inﬁnity, the limit of the free entropy

lim

tG

n→∞

(z) = lnq +

n

1 q

d 2

ln(1 −

)

for q > Cd. This is one of the main results in [1]. Note that their proof works for q > d + 1, while our approach only works for q > Cd. The advantage of our approach is that it gives an explicit estimate on the number of proper colorings of large girth graphs.

Theorem 1.4 Let G be a ﬁnite graph of girth g and maximal degree d. Then for all q > Cd we have

(Cd/q)g−1 1 − Cd/q

− lnq + |E(G)| |V (G)|

lnchG(q) |V (G)|

1 q

) ≤ 2

ln(1 −

.

When G is d-regular with asymptotically maximal girth, i.e. g = cln|V (G)|, this yields

d 2

1 q

lnchG(q) |V (G)|

) ≤ O(|V (G)|−c )

− lnq +

ln(1 −

for some explicit constant c > 0. Counting the number of proper colorings of random d-regular graphs have been considered in [1]. These graphs do not have logarithmic girth, but they have few shorter cycles, so one can obtain a similar result for them.

Here we wish to raise attention to an interesting phenomenon, of which we only have some computational evidence. We have computed the chromatic measures of several 3-regular large girth graphs and surprisingly, it looks like one may also get weak convergence of chromatic measures.

x

- 0

- 1

- 2


x

-1 0 1 2 3

- -2

- -1


Figure 1: Chromatic roots of the 30368 cubic graphs of size 32 and girth 7

Problem 1.5 Let Gn be a sequence of d-regular graphs with girth tending to inﬁnity. Does µG

weakly converge?

n

This would be interesting because one could consider the limit as the ‘chromatic measure of the d-regular inﬁnite tree’. Observe that any subsequential weak limit µ of µG

satisﬁes

n

d 2

zkdµ(z) =

D

(k ≥ 1)

that is, the holomorphic moments of µ are independent of k. While Figure 1 looks very promising, one misleading aspect of it may be that 3-regular graphs having 32 vertices and (maximal possible) girth 7 may exhibit structural restrictions that are much stronger than just large girth.

It would be interesting to generalize the results of this paper to the Tutte polynomial TG(x,y). This two-variable polynomial encodes a lot of interesting

invariants of G. For instance, TG(z,0) = chG(z), TG(2,1) counts the number of forests, TG(1,1) is the number of spanning trees and TG(1,2) is the number of connected spanning subgraphs. By a result of Lyons [7], we know that

log TG

(1,1) |V (Gn)|

n

converges for a Benjamini-Schramm convergent sequence of graphs Gn of bounded degree. Also, in [4] it is shown that the same holds at the places (q,y) where 0 ≤ y < 1 and q is large enough in terms of the maximal degree. It would be interesting to see whether this also holds at other places. The places (2,1) and (1,2) would be good test points as they have a natural combinatorial meaning. Also, it is not clear whether Theorem 1.1 holds for pG(z) = TG(z,y0) for all ﬁxed y0. Note that even for the chromatic polynomial, in general, the above log convergence will not hold, for instance at (2,0), because cycles of even and odd length converge to the same limit, but even cycles have a proper 2-coloring, while odd cycles do not. This may not be so surprising, since TG(2,0) ≤ 2c(G) where c(G) is the number of components of G. So for a nontrivial graph sequence Gn, TG

(2,0) is subexponential in |V (Gn)|, which points to the proximity of roots of TG

n

. To apply Theorem 1.1 in its present form, one needs that some small neighbourhood of the place is sparse in terms of roots.

n

Remark. Note that recently Csikv´ri and Frenkel [5] generalized Theorem 1.2 to a large class of graph polynomials, including the Tutte polynomial. In particular, they show that convergence holds for the normalized log of T(x,y) where x,y have large enough absolute value.

Acknowledgements. The authors thank L´szl´ Lov´sz who introduced them to [4], G´bor Hal´sz who raised their attention to the relevance of Mergelyan’s theorem and Lewis Bowen who pointed out some inconsistencies of notation in a previous version of this paper. This work was partially supported by the MTA R´enyi “Lend¨ulet” Groups and Graphs Research Group.

### 2 Preliminaries

For a simple graph H on n vertices let the number of legal colorings of H with q colors be denoted by chH(q). Then for any edge e of H the following recursion holds:

chH(q) = chH\e(q) − chH/e(q) where H \ e is obtained from H by deleting e and H/e is obtained by gluing the endpoints of e and erasing multiple edges and loops. This implies that chH is a polynomial of degree n in q with integer coeﬃcients, called the chromatic polynomial of G and that the above recursion holds for the polynomials themselves. It also follows that the constant coeﬃcient of chH is zero and its main

coeﬃcient is 1. So, we can write chH(z) = zn − e1(H)zn−1 + ... + (−1)kek(H)zn−k + ... + (−1)n−1en−1(H)z =

n

(z − λi(H)).

=

i=1

The ek(H) are called the chromatic coeﬃcients of H and λi(H) are its chromatic roots. For k ≥ 0 let

n

λki (H).

pk(H) =

i=1

The Newton identities establish connections between the roots and coeﬃcients of a polynomial. In this paper we will use the following version:

pk = (−1)k−1kek +

k−1

(−1)k−i−1piek−i.

i=1

Let H,G be simple graphs. A map f : V (H) → V (G) is a homomorphism if for all edges (x,y) ∈ E(H) we have (f(x),f(y)) ∈ E(G). We denote the number of homomorphisms from H to G by hom(H,G). The quantity hom(H,G) is nice to work with, mainly because of the following property.

- Lemma 2.1 Let H be the disjoint union of H1 and H2. Then hom(H,G) = hom(H1,G)hom(H2,G)


for all simple graphs G. We leave the proof to the reader.

For a random rooted graph G, a ﬁnite rooted graph α and a positive integer R, let P(G,α,R) denote the probability that the R-ball centered at the root of G is isomorphic to α. Analogously, for an unrooted ﬁnite graph G, let P(G,α,R) denote the probability that the R-ball centered at a uniform random vertex of G is isomorphic to α. A graph sequence Gn has bounded degree if there is an absolute upper bound on the degrees of vertices of Gn.

A graph sequence (Gn) of bounded degree is Benjamini-Schramm convergent if for all ﬁnite rooted graphs α and R > 0 the probabilities P(Gn,α,R) converge.

The limit of a Benjamini-Schramm convergent sequence of graphs is the random rooted graph G satisfying

P(G,α,R) = lim

P(Gn,α,R)

n→∞

for all R > 0 and α. It is easy to see that G is well deﬁned. In the most transparent case, G is just one graph, which then has to be vertex transitive. For instance, the d dimensional lattice

(Z/nZ)d = lim

Zd = lim

Bnd

n→∞

n→∞

where (Z/nZ)d is the d dimensional torus and Bnd is the box of side length n in Zd. The same way, one can obtain any connected vertex transitive amenable graph as a limit. Let G be a connected vertex transitive graph of bounded degree. A sequence of connected subgraphs Fn of G is a Følner sequence, if

|∂Fn| |V (Fn)|

lim

= 0

n→∞

where ∂Fn denotes the external vertex boundary of Fn. Note that G is amenable if and only if it has a Følner sequence. It is easy to show that any connected vertex transitive amenable graph is the Benjamini-Schramm limit of its Følner sequences.

Let us consider now the d-regular tree Td, which is in many senses the farthest possible from being amenable. One can obtain Td as the limit of ﬁnite graphs, but it is worth to point out that Td can not be obtained as a limit of ﬁnite trees. Indeed, the expected degrees of ﬁnite trees are approximately 2 and this passes on to their limits. It is a good exercise to understand what the limit of the balls in Td is (it is a ﬁxed tree where the root is random). The right way to approximate Td in Benjamini-Schramm convergence is to take ﬁnite d-regular graphs Gn with girth tending to inﬁnity.

Benjamini-Schramm convergence can also be expressed in terms of graph homomorphisms using the following lemma (see [6], Proposition 5.6).

- Lemma 2.2 Let Gn be a graph sequence of bounded degree. Then Gn is BenjaminiSchramm convergent if and only if for every ﬁnite connected graph H, the limit

lim

n→∞

hom(H,Gn) |V (Gn)| exists.

Note that one needs connectedness in Lemma 2.2, as hom(H,G) may be the order of |V (G)|c where c is the number of components in H.

- 3 Expressing moments from homomorphisms


In this section we give an explicit formula for the holomorpic moments of the chromatic measure in terms of graphs homomorphisms.

For a ﬁnite, simple graph G let P(G) be deﬁned as the set of partitions of V (G) where no edge of G connects two vertices in the same class. A partition P ∈ P(G) can be considered as a surjective homomorphism from G to the simple graph G/P obtained by contracting each class of P and erasing multiple edges. For simple graphs G and T let

P(G,T) = {P ∈ P(G) | G/P ∼= T}

be the collection of partitions of G with quotient isomorphic to T. For P ∈ P(G) let

(|p| − 1)!

P =

p∈P

where p ∈ P runs through the P-classes.

Let Aut(G) denote the automorphism group of G. Let G(k) denote the set of graphs without isolated vertices, where the number of vertices minus the number of components equals k and let

G(≤ k) = ∪j≤kG(j). Note that G(≤ k) is a ﬁnite set.

Base parameters. Now we introduce a sequence of parameters that will connect moments with chromatic coeﬃcients. For a simple graph T and k > 0 let

(−1)|E(G)|+|V (G)|+|V (T)|+k |Aut(G)|

P .

ck(T) =

P∈P(G,T)

G∈G(k)

It turns out that these parameters allow us to express ek(H) in a nice way.

- Lemma 3.1 Let H be a simple graph. Then we have


ek(H) =

ck(T)hom(T,H).

T∈G(≤k)

Proof. We derive the lemma from two easy claims. Let inj(G,H) denote the number of injective homomorphisms from G to H.

#### Claim 1. We have

(−1)|E(G)|+k |Aut(G)|

ek(H) =

inj(G,H).

G∈G(k)

- To see this, we use the following identity, that is sometimes used as a deﬁnition.


(−1)|E(G)|zc(G)

chH(z) =

G⊆H spanning

where c(G) is the number of connected components in the spanning subgraph

- G. It is enough to prove this for positive integer values of z. In this case, there are exactly zc(G) colorings that violate the legal coloring constraint for all edges of G, and the equation follows from the inclusion-exclusion principle.

The value of ek(H) is (−1)k times the coeﬃcient of zn−k, which contains the terms where c(G) = n−k, or equivalently, where the graph G, when erasing its isolated vertices, is in Gk. A graph G is counted as many times as it appears in

- H as a spanning subgraph, which equals inj(G,H)/|Aut(G)|. Claim 1 is proved.


- Claim 2. Let G ∈ G(k) and let H be a simple graph. Then we have


 (−1)|V (G)|+|V (T)|

 hom(T,H).

inj(G,H) =

P

T∈G(≤k)

P∈P(G,T)

To see this, let us consider the partially ordered set P(G) with respect to reﬁnement. For P,P ∈ P(G) with P ≤ P (i.e. P reﬁnes P), let p1,...,pr be a list of the P-classes and let ai be the number of P -classes contained in pi

r

(1 ≤ i ≤ r). Let s =

ai be the number of classes in P . Then the Mobius function is

i=1

r

µ(P ,P) = (−1)r+s

(ai − 1)!

i=1

(see e.g. [10]). In particular, for the discrete partition P0 we get

µ(P0,P) = (−1)|V (G)|+|V (G/P)| P . On the other hand, we have

hom(G/P ,H) =

inj(G/P,H).

P ≤P∈P(G)

Now the Mobius inversion formula yields inj(G,H) =

(−1)|V (G)|+|V (G/P)| P hom(G/P,H)

P∈P(G)

which, when collecting terms by T = G/P ∈ G(≤ k) gives the formula in Claim 2.

The lemma follows from substituting the formula in Claim 2 into the formula in Claim 1 and collecting terms.

Now we show that the base parameters of a disconnected graph can be expressed as a convolution of the base parameters of its connected components, normalized by a constant computed from the multiplicities:

- Lemma 3.2 Let T be the disjoint union of the connected graphs T1,T2,...,Tl. Let S = {j | i < j : Ti ∼= Tj} contain the indices of nonisomorphic Tj’s and


mj = |{i | Ti ∼= Tj}| denote the multiplicity of Tj. Deﬁne σ =

mj!. Then for all k > 0 we have

j∈S

ck(T) =

l

1 σ

j=1

(x1,...,xl) x1+···+xl=k

cx

##### (Tj).

j

Proof. Recall that

(−1)|E(G)|+|V (G)|+|V (T)|+k |Aut(G)|

ck(T) =

P .

G∈G(k)

P∈P(G,T)

For a ﬁxed G and P, the connected components of G/P can be identiﬁed with T1,T2,...,Tl in σ possible ways. Each of these matchings gives a subdivision G = G1 ∪G2 ∪...∪Gl by applying the inverse image of the quotient map to the

- Ti’s. The restrictions Pi = P|Gi


of the partition P satisfy Pi ∈ P(Gi,Ti) and l

Pj = P .

j=1

Therefore

l

(−1)|E(G)|+|V (G)|+|V (T)|+k |Aut(G)| G=G

1 σ

Pj .

ck(T) =

1∪...∪Gl Pj∈P(Gj,Tj) 1≤j≤l

j=1

G∈G(k)

If we already know the isomorphism classes of G1,G2,...,Gl, there are still |Aut(G)|

l

|Aut(Gj)|

j=1

possibilities to arrange them as a subdivision of G. It follows that ck(T) equals

|Aut(G)|

l

Gj∈G(xj) 1≤j≤l

(x1,...,xl) x1+...+xl=k

|Aut(Gj)|

j=1

l

(−1)|E(G)|+|V (G)|+|V (T)|+k |Aut(G)|

1 σ

·

j=1

Pj∈P(Gj,Tj) 1≤j≤l

Pj .

By using

|E(G)| + |V (G)| + |V (T)| + k =

l

(|E(Gj)| + |V (Gj)| + |V (Tj)| + xj)

j=1

and rearranging we get

ck(T) =

l

##### (−1)|E(G

j)|+|V (Gj)|+|V (Tj)|+xj

1 σ

|Aut(Gj)|

j=1 Gj∈G(xj)

Pj∈P(Gj,Tj)

(x1,...,xl) x1+...+xl=k

l

1 σ

=

cx

(Tj).

j

j=1

(x1,...,xl) x1+...+xl=k

Pj =

We can use the following variant of Lemma 3.2 when we would like to detach one connected component of T at a time:

- Lemma 3.3 Let T be the disjoint union of the connected graphs T1,T2,...,Tl where l ≥ 2. Let S = {j | i < j : Ti ∼= Tj} contain the indices of nonisomorphic


- Tj’s. Then we have


k−1

kck(T) −

ici(Tj)ck−i(T \ Tj) = 0.

i=1 j∈S

Proof. Let mj denote the multiplicity of Tj and σ =

mj! as in Lemma 3.2. Since isomorphic Tj’s have identical ci(Tj) and ck−i(T \ Tj), it follows that

j∈S

l

i mt

ci(Tt)ck−i(T \ Tt).

ici(Tj)ck−i(T \ Tj) =

t=1

j∈S

By using Lemma 3.2 for T and σ and also for T \ Tt and mσ

we obtain:

t

k−1

k−1

l

i mt

kck(T) −

ici(Tj)ck−i(T \ Tj) = kck(T) −

ci(Tt)ck−i(T \ Tt) =

t=1

i=1 j∈S

i=1

k−1

l

l

l

k σ

mt σ

i mt ·

(Tj) −

=

cx

cx

(Tj) =

j

j

t=1

j=1

j=1

i=1

(x1,...,xl) x1+...+xl=k

(x1,...,xl) x1+...+xl=k xt=i

l

l

1 σ

k −

xt

cx

=

(Tj) = 0.

j

t=1

j=1

(x1,...,xl) x1+...+xl=k

l

The last equation follows from k −

xt = 0.

t=1

Now we show that pk(H) can be expressed using the number of homomorphisms from connected graphs. Theorem 3.4 Let H be a simple graph on n vertices and let k > 0 be an integer. Then

(−1)k−1kck(T)hom(T,H).

pk(H) =

T∈G(≤k) T is connected

Proof. The Newton identites tell us that

pk(H) = (−1)k−1kek(H) +

k−1

(−1)k−i−1pi(H)ek−i(H)

i=1

for all k > 0. Using induction on k, we can assume that the result holds for all j < k. Lemma 3.1 gives us a formula for ek(H) in the parameters ck(T),

namely we have

ek(H) =

ck(T)hom(T,H).

T∈G(≤k)

Using that hom is multiplicative (stated as Lemma 2.1) we get pk(H) as a ﬁxed linear combination of the hom(T,H)’s. Let qk(T) denote the formal coeﬃcient of hom(T,H) in this sum. So, we have

pk(H) =

qk(T)hom(T,H).

T∈G(≤k)

This leads to the following equality for all T:

qk(T) = (−1)k−1kck(T) +

k−1

(−1)k−i−1

qi(U1)ck−i(U2)

i=1

- U1∈G(≤i)
- U2∈G(≤k−i) U1∪U2=T


where T is isomorphic to the disjoint union of U1 and U2. Let T ∈ G(≤ k). We claim that

qk(T) = (−1)k−1kck(T)

if T is connected and 0 otherwise. If T is connected then it is impossible to choose U1 and U2 in the second sum above, so the claim holds. If T is disconnected then as in Lemma 3.3, let T be the disjoint union of the connected graphs T1,T2,...,Tl and let S contain the indices of nonisomorphic Tj’s. Using induction on k we can assume that qi(U1) = 0 unless U1 is isomorphic to one of the Tj’s. This gives

qk(T) = (−1)k−1kck(T) +

k−1

(−1)k−i−1

i=1

qi(Tj)ck−i(T \ Tj).

j∈S

We know from the induction hypothesis that qi(Tj) = (−1)i−1ici(Tj) and therefore we get

 kck(T) −

 

k−1

qk(T) = (−1)k−1

ici(Tj)ck−i(T \ Tj)

i=1 j∈S

which is 0 according to Lemma 3.3.

### 4 Convergence of chromatic measures

In this section we prove Theorem 1.1, Theorem 1.2 and Proposition 1.3. For the convenience of the reader, we state the theorems again.

- Theorem 1.1 Let (Gn) be a Benjamini-Schramm convergent graph sequence of absolute degree bound d, and D an open neighborhood of the closed disc D. Then for every holomorphic function f : D → C, the sequence


converges. Proof. We have

f(z)dµG

n

(z)

D

D

|V (G)|

pk(G) |V (G)|

1 |V (G)|

λki (G) =

zkdµG(z) =

i=1

for k ≥ 0. Since f is holomorphic, it equals its Taylor series

∞

anzn

f(z) =

n=0

on an open neighborhood of D. Let

k

anzn

fk(z) =

n=0

denote the partial sums. The fk’s converge uniformly on D, so we also know that

Fk(G) =

D

k

fk(z)dµG(z) =

n=0

k

zndµG(z) =

an

an

n=0

D

pn(G) |V (G)|

converges to

F(G) =

f(z)dµG(z)

D

uniformly on the set of graphs G with µG supported on D. By Theorem 3.4 we have

(−1)n−1ncn(T)hom(T,G).

pn(G) =

T∈G(≤n) T is connected

By rearranging, this gives

Fk(G) =

T

hom(T,G) |V (G)|

bk,T

where T runs through connected graphs on at most k + 1 vertices. Now let Gn be a Benjamini-Schramm convergent sequence of graphs. By Lemma 2.2, the sequences

hom(T,Gn) |V (Gn)|

converge for every connected T. (Note that for non-connected T this is in general false). This implies that Fk(Gn) is convergent for every k. Since we already know that Fk(Gn) uniformly converges to F(Gn) for every n, we obtain that F(Gn) is also convergent. It also follows that

F(Gn,u) =

D

f(z + u)dµG

n

(z)

uniformly converges to a holomorphic function in a neighborhood of 0. We are ready to prove Theorem 1.2.

- Theorem 1.2 Let (Gn) be a Benjamini-Schramm convergent graph sequence of


absolute degree bound d with |V (Gn)| → ∞. Then tG

(z) converges to a real

n

analytic function on C \ D. Proof. The principal branch of the complex logarithm function only takes values with an imaginary part in (−π,π]. Therefore tG

(z) is always in the interval |V −(Gπ

n

n)|, |V (πG

##### (z) → 0. To prove convergence for the real part tG

n)| and |V (Gn)| → ∞ implies tG

n

(z), consider a ﬁxed z0 ∈ C \ D. Since the disc B(z0,Cd) is bounded away from 0, there exists a branch ln∗ of the complex logarithm function whose branch cut is a half-line emanating from

n

- 0 that is disjoint from the disc. It follows that f(z) = ln∗(z0 −z) is holomorphic on an open neighborhood of D. According to Theorem 1.1,


D

ln∗(z0 − z)dµG

n

(z)

converges uniformly in a neighborhood of z0, which implies that

ln(z0 − λ) |V (Gn)|

lnchG

(z0) |V (Gn)|

= λ root

n

tG

(z0) =

=

n

D

ln(z0 − z)dµG

n

(z) =

=

D

ln∗(z0 − z)dµG

n

(z) =

D

ln∗(z0 − z)dµG

n

##### (z)

##### is locally uniformly convergent as a function of z0. Since ln(z0 − λ) is a harmonic function for all chromatic roots λ, so is tG

##### (z0), and the harmonicity of limtG

n

(z0) follows from local uniform convergence. The observation that all harmonic functions are real analytic concludes the proof.

##### (z0) = lim tG

n

n

Now we prove Proposition 1.3. Note that already Salas and Sokal [11] showed that the pointwise limit of supports of µT

is part of a particular algebraic curve. For convenience, we include some details on that, also adding a picture on the supporting set, but we do not introduce the transfer matrix method here. See [11] for a description of the transfer matrix method.

n

Proposition 1.3 The chromatic measures µT

n

weakly converge.

Proof. We deﬁned Tn as the cartesian product of C4 and Pn. By the transfer matrix method we obtain

(z) = v1Mn−11T with

chT

n

v1 = z4−6z3+11z2−6z 2z3−6z2+4z z2−z

 

 

z4−10z3+41z2−84z+73 2z3−14z2+38z−40 z2−5z+8 z4−10z3+40z2−77z+60 2z3−13z2+32z−29 z2−4z+5 z4−10z3+39z2−70z+48 2z3−12z2+26z−20 z2−3z+3

M =

 



1 1 1

.

1T =

Using the eigenvectors of M as our new basis we can diagonalize M and rewrite the above expression as

(z) = u1Dn−1u2 where

chT

n

  

  

T

z7−10z6+44z5−105z4+143z3−109z2+36z+z3r−2z2r+zr 2z3−12z2+28z−24 z7−10z6+44z5−105z4+143z3−109z2+36z−z3r+2z2r−zr 2z3−12z2+28z−24

u1 =

0

 

 

z4−8z3+29z2−55z+46+r 2 0 0 0 z

4−8z3+29z2−55z+46−r

D =

2 0 0 0 1

 

 

z4−8z3+27z2−47z+36+r 2r −z4+8z3−27z2+47z−36+r 2r

u2 =

0

and

r = z8−16z7+118z6−526z5+1569z4−3250z3+4617z2−4136z+1776.

The matrix Dn−1 is straightforward to calculate, so we get the following closed formula for the chromatic polynomial:

(z) = a1λn1−1 + a2λ2n−1 where

chT

n

z(z−1)(z4−8z3+27z2−47z+36+ri)(z5−9z4+35z3−70z2+73z−36+zri−ri) 4ri(z−2)(z2−4z+6) and

ai =

z4−8z3+29z2−55z+46+ri 2 with r1,2 = ±r.

λi =

We are interested in the complex roots of this expression if n is very large. We don’t need to specify them exactly, but we’ll prove a necessary condition. If the eigenvalues λi diﬀer in their absolute value for some z, there will be an arbitrarily large multiplicative gap between a1λn1−1 and a2λn2−1 for any values of ai unless both a1λ1 = 0 and a2λ2 = 0 holds.

It follows that all roots must have |λ1| = |λ2| with the possible exception of a ﬁnite set consisting of the roots and singularities of a1, a2, λ1 and λ2, or equivalently, the roots of

z(z−1)(z−2)(2z−5)(z2−3z+1)(z2−4z+6)· ·(z6−12z5+61z4−169z3+269z2−231z+85)· ·(z8−16z7+118z6−526z5+1569z4−3250z3+4617z2−4136z+1776).

Let’s ignore this set S of special roots for now and concentrate on the general case of |λ1| = |λ2|:

λ1λ1 = λ2λ2 z4−8z3+29z2−55z+46+r

z4−8z3+29z2−55z+46+r 2

2 ·

=

z4−8z3+29z2−55z+46−r 2

z4−8z3+29z2−55z+46−r 2 ·

=

(z4−8z3+29z2−55z+46)r + (z4−8z3+29z2−55z+46)r = 0

Our last expression means that (z4−8z3+29z2−55z+46)r is purely imaginary, which is equivalent to its square being a nonpositive real. When calculated, this gives a degree 14 algebraic curve clipped by a degree 16 algebraic curve, shown as the set C on the Figure 2.

It follows that the curve C is compact, has an empty interior and its complement is connected. Hence the same holds for C = C ∪ S.

x

- 0

- 1

- 2

- 3

- 4


C

x

-4 -3 -2 -1 0 1 2 3 4

- -4

- -3

- -2

- -1


Figure 2: Possible limit points of chromatic roots of Tn = C4 × Pn as n → ∞

Now Mergelyan’s theorem [8] says that every continuous function on C can be uniformly approximated by polynomials. This implies that if two probability measures µ1 and µ2 are supported on C and the holomorphic moments satisfy

then

C

zkdµ1(z) =

C

zkdµ2(z) (k ≥ 1)

f(z)dµ1(z) =

f(z)dµ2(z)

C

C

for all continuous functions f : C → R. Hence, we have µ1 = µ2. Since any subsequential weak limit of µT

##### is supported on C , we get that µT

is weakly convergent.

n

n

Remark. As we saw in the introduction, weak convergence does not hold in general. The phenomenon where an associated measure blows up by a small

change of the graph but keeps its holomorphic moments unchanged also occurs in the spectral theory of directed graphs. Namely, the weak limit of the eigenvalue distributions of the directed path of length n is the Dirac measure at 0, while for the directed n-cycle the limit is the uniform measure on the unit circle centered at 0. In both the chromatic and the spectral case, the reason is that the change only aﬀects the coeﬃcients of small index in the corresponding polynomial, and the k-th moment only depends on the k highest index coeﬃcients. It would be interesting to study this blow-up phenomenon using just abstract polynomials.

### 5 Graphs of large girth

In this section we study graphs with large girth and prove Theorem 1.4.

- Lemma 5.1 Suppose that the ﬁnite graphs G and H both have girth at least g and |E(G)| = |E(H)|. Then ei(G) = ei(H) holds for i = 0,1,...,g − 2.

Proof. We use induction on |E(G)| = |E(H)|. If the number of edges is zero, the claim is trivial, as is when g ≤ 3. Otherwise pick e ∈ E(G) and f ∈ E(H) arbitrarily and use the deletion-contraction argument:

ei(G) = ei(G \ e) + ei−1(G/e) ei(H) = ei(H \ f) + ei−1(H/f)

The claim follows from the observation that G \ e and H \ f have girth ≥ g while G/e and H/f have girth ≥ g − 1.

- Lemma 5.2 Let G be a ﬁnite graph with girth ≥ g. Then pi(G) = |E(G)| for i = 1,2,...,g − 2.


Proof. Let H be an arbitrary tree on |E(G)| + 1 vertices and use the previous lemma. Since the chromatic polynomial of H is q(q −1)|E(G)|, we have ei(H) =

i for i ≤ |E(G)|, which translates into ei(G) = |E(iG)| for i ≤ g − 2. Substituting the ei’s into Newton’s identities completes the proof.

|E(G)|

Theorem 1.4 Let G be a ﬁnite graph of girth g and maximal degree d. Then for all q > Cd we have

(Cd/q)g−1 1 − Cd/q

− lnq + |E(G)| |V (G)|

1 q

lnchG(q) |V (G)|

ln(1 −

) ≤ 2

.

Proof. The normalized log of the chromatic polynomial can be expanded as

lnchG(q) |V (G)|

=

D

z q

ln(q − z)dµG(z) = lnq +

ln 1 −

D

∞

1 nqn

zndµG(z)

= lnq −

n=1

D

dµG(z) =

where the Sokal bound |z| ≤ Cd gives the constraint

D

zndµG(z) ≤ (Cd)n

for the holomorphic moments, and our last lemma implies

D

= |E(G)| |V (G)|

pn(G) |V (G)|

zndµG(z) =

for n ≤ g − 2. We also know that any real number x ∈ [0,1) satisﬁes

x

x

∞

∞

tg−2 1 − t

xg−2 1 − x

xg−1 1 − x

xn n

tndt =

dt ≤ x ·

=

=

.

n=g−1

n=g−2

0

0

Now we have

≤

− lnq + |E(G)| |V (G)|

lnchG(q) |V (G)|

1 q

ln(1 −

) =

 lnq −

  − lnq −

∞

∞

|E(G)| |V (G)|

1 nqn

1 nqn ·

zndµG(Z)

≤

=

n=1

n=1

D

 

  ≤

 

  ≤

∞

∞

|E(G)| |V (G)|

zndµG(z) + |E(G)| |V (G)|

1 nqn

1 nqn

zndµG(z) −

n=g−1

n=g−1

D

D

∞

∞

(Cd/q)g−1 1 − Cd/q

(Cd)n + |E(G)|/|V (G)| nqn ≤

2(Cd)n nqn ≤ 2

≤

.

n=g−1

n=g−1

The theorem holds.

### 6 Appendix

In the appendix we publish some data that may be useful for further analysis. For abbreviation, we use the following terminology:

hom

n

αiGi,H =

i=1

n

αi hom(Gi,H)

i=1

where the Gi and H are ﬁnite graphs.

One can express the ﬁrst 4 chromatic coeﬃcients as a linear combination of homomorphisms as follows:

- e0(G) = hom( ,G)

- e1(G) = hom 12 ,G

- e2(G) = hom − 14 − 16 + 18 ,G

- e3(G) = hom 24 1 + 14 + 121 − 18 − 18 + 14 − 241 −


1 12 + 481 ,G

e4(G) = hom 12 1 − 13 + 18 + 965 − 121 − 14 + 18 −

- 4 + 121 + 18 + 121 − 321 + 121 − 121 − 101 +


- 1


- 1

- 2 − 12 + 14 − 14 + 18 − 121 + 1201 − 161 + 18 −

- 1 48 + 721 − 481 + 3841 ,G


Also, one can express the ﬁrst 5 chromatic moments as a linear combination of homomorphisms as follows.

- p0(G) = hom( ,G)

- p1(G) = hom 12 ,G

- p2(G) = hom 12 + 13 ,G

- p3(G) = hom 18 + 34 + 41 − 38 + 34 − 81 ,G

- p4(G) = hom − 13 + 43 − 12 + 31 + − 12 + − 31 −


- 1


- 3 +13 +25 −2 +2 − + −12 +13 −301 ,G


##### p5(G) = hom − 1972 − 165 − 1516 + 12572 + 58 + 2524 +

35 48 − 2435 − 14425 + 485 + 58 − 54 + 54 − 2524 +

25

- 24 + 165 + 34 − 154 + 154 + 54 − 125 − 258 +

- 25 8 − 2516 + 2524 − 485 − 485 + 485 + 45 − 25 − 54 +


- 5


##### 2 + 58 − 58 − 125 + 54 + 52 −5 − 52 +

5

##### 2 − 58 + 52 + 54 − 52 + 5 + 56 − 25 +

- 4 + 725 − 125 − 54 + 125 − 365 − 54 + 52 +

- 5


5

- 2 +54 −52 −165 +165 −52 −54 +52 −12 +


5 12 − 52 − 52 + 52 − 45 − 52 − 58 + 52 − 125 +

5 12 + 54 + 125 + 58 − 45 − 485 + 165 − 485 + 1441 ,G

### References

- [1] A. Bandyopadhyay and D. Gamarnik, Counting without sampling. Asymptotics of the logpartition function for certain statistical physics models, Random Structures & Algorithms 33 (2008)
- [2] C. Borgs, Absence of Zeros for the Chromatic Polynomial on Bounded Degree Graphs, Combinatorics, Probability and Computing 15 (2006), 63– 74.
- [3] I. Benjamini and O. Schramm, Recurrence of distributional limits of ﬁnite planar graphs, Electron. J. Probab. 6 (2001), no. 23, 13 pp.
- [4] C. Borgs, J. Chayes, J. Kahn and L. Lov´sz, Left and right convergence of graphs with bounded degree, Random Structures & Algorithms 42 (2013)
- [5] P. Csikv´ri and P. E. Frenkel, Benjamini–Schramm continuity of root moments of graph polynomials, http://arxiv.org/abs/1204.0463
- [6] L. Lov´sz, Large Networks and Graph Limits. Colloquium Publications, vol. 60. American Mathematical Society (2012)
- [7] R. Lyons, Asymptotic enumeration of spanning trees, Combinatorics, Probability and Computing 14 (2005), 491–522.
- [8] S. N. Mergelyan, Uniform approximations to functions of a complex variable, Uspehi Mat. Nauk (N.S.) 7 (48) (1952), 31–122.
- [9] A. Procacci, B. Scoppola and V. Gerasimov: Potts model on inﬁnite graphs and the limit of chromatic polynomials. Commun. Math. Phys. 235 (2003), 215–231.
- [10] G. C. Rota, On the foundations of combinatorial theory I. Theory of M¨bius functions, Probability theory and related ﬁelds 2 (4) (1964), 340–368.
- [11] J. Salas and A.D. Sokal, Transfer Matrices and Partition-Function Zeros for Antiferromagnetic Potts Models V. Further Results for the Square-Lattice Chromatic Polynomial, J Stat Phys 135 (2009), 279–373.
- [12] A. D. Sokal: Bounds on the complex zeros of (di)chromatic polynomials and Potts-model partition functions, Combinatorics, Probability and Computing 10 (2001), 41–77.
- [13] A. D. Sokal, The multivariate Tutte polynomial (alias Potts model) for graphs and matroids, In: Webb, BS, (ed.) Surveys in Combinatorics, 2005, 173–226. Cambridge University Press


