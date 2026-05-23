arXiv:1407.7700v2[math.CO]30Jul2014

Mixing properties and the chromatic number of Ramanujan complexes

Shai Evra∗, Konstantin Golubev†, Alexander Lubotzky‡ Institute of Mathematics Hebrew University Jerusalem 91904 ISRAEL

August 27, 2018

Dedicated to Nati Linial on his 60th birthday.

Abstract

Ramanujan complexes are high dimensional simplical complexes generalizing Ramanujan graphs. A result of Oh on quantitative property (T) for Lie groups over local ﬁelds is used to deduce a Mixing Lemma for such complexes. As an application we prove that non-partite Ramanujan complexes have ’high girth’ and high chromatic number, generalizing a well known result about Ramanujan graphs.

# 1 Introduction

In 1959, Erdo˝s [E] used random methods to show that there are graphs with arbitrary large girth and arbitrary large chromatic number. In a way this is a surprising fact, since large girth means that such a graph looks locally like a tree, and so locally its chromatic number is two, while globally it requires a large number of colors. A constructive proof was given by Lov´asz [Lo] in 1968, and explicit examples (with quantitative estimates) in 1988 by Lubotzky, Phillips, Sarnak [LPS] using Ramanujan graphs. This is still by no mean an easy result even by nowadays standards.

The goal of this paper is to extend the above from Ramanujan graphs to high-dimensional Ramanujan complexes, as deﬁned and constructed in [LSV1] and [LSV2]. One is facing the immediate question what we mean by ”girth” and ”chromatic number” for simplicial complexes?

The girth g(X) of a graph X is equal to twice its injectivity radius r(X)

(more precisely r(X) = ⌊g(X2)−1⌋). The injectivity radius of X is the maximal r ∈ N such that if π : X˜ → X is the universal cover map, then for every y ∈ X˜, π is one-to-one on the ball of radius r around y. This deﬁnition is easily extended

![image 1](<2014-evra-mixing-properties-chromatic-number_images/imageFile1.png>)

![image 2](<2014-evra-mixing-properties-chromatic-number_images/imageFile2.png>)

∗E-mail address: shai.evra@mail.huji.ac.il †E-mail address: kost.golubev@mail.huji.ac.il ‡E-mail address: alex.lubotzky@mail.huji.ac.il

to ﬁnite simplicial complexes and, in particular, to the Ramanujan complexes, whose universal covers are the Bruhat-Tits buildings. The injectivity radius is deﬁned similarly with respect to the graph metric on the 1-skeletons of X˜ and X. This notion has been studied in [LuMe] where it was shown that there exist Ramanujan complexes of ”large girth” in this sense. See Proposition 3.3 there and Corollary 5.2 below.

Before moving to the chromatic number, let us make the following warning: Every simplicial complex X can be considered as a hypergraph H, when we take the maximal simplices (facets) of X to be the edges of H. Moreover if X is pure, i.e. all its facets are of the same dimension, say d − 1, then H is a d-uniform hypergraph, i.e. all of its edges are of size d. The commonly used notion of girth in the theory of hypergraphs is diﬀerent then the one we are using here; it refers to the length of a minimal sequence of the form x1,E1,x2,E2,...,xg,Eg,xg+1 where all x1,...,xg are diﬀerent vertices, xg+1 = x1, E1,...,Eg are edges and for any i = 1,...,g, {xi,xi+1} ⊂ Ei. This notion is not suitable for the Ramanujan complexes or any clique complex: any two facets with a common 1-codimension wall give girth 2 in this deﬁnition (so, even the building has girth

- 2). Anyway, the theory of hypergraphs of high girth and high chromatic number has been developed quite intensively. See [N] for a nice survey. The reader is referred also to ([LuMe], [G1] and [G2]) for related notions of girth for simplicial complexes, based on local acyclicity.


The notion of chromatic number for simplicial complexes we will use is the same as the one commonly used for hypergraphs. Let X be a (d−1)-dimensional simplicial complex with a set of vertices V .

Deﬁnition 1.1. The chromatic number of X, denoted χ(X), is the minimal number of colors needed to color the vertices of X, so that no facet (i.e. maximal face) is monochromatic.

Clearly χ(X) is bounded above by the chromatic number of the graph X(1)(= the 1-skeleton of X).

Let us now recall what are Ramanujan complexes and how they are constructed: Let F be the local non-archimedean ﬁeld Fq((t)), i.e. the ﬁeld of Laurent power series over Fq, where Fq is the ﬁnite ﬁeld of order q. Let B = Bd(F) be the Bruhat-Tits building associated with PGLd(F). It is an inﬁnite (d − 1)dimensional countable simplicial complex, whose vertices come naturally with types in Z/dZ, denoted τ : B(0) → Z/dZ (see [LSV1] and the references therein) in such a way that in every (d − 1)-face all vertices are of diﬀerent types. In particular, its chromatic number is at most d. (Even its 1-skeleton has chromatic number d.) In fact, its chromatic number is 2, since we can divide the set of d types Z/dZ into two non-empty disjoint sets and then using only two colors, we get that no (d − 1)-cell is monochromatic. If Γ is a cocompact lattice in G = PGLd(F), with dist(Γ) := min1 =γ∈Γ,x∈B dist(γ.x,x) ≥ 2, then Γ\B is a ﬁnite simplicial complex. If Γ preserves the types of the vertices of B, Γ\B is also d-colorable (and even 2-colorable). The injectivity radius of Γ\B is ⌊dist(Γ)2 −1⌋.

![image 3](<2014-evra-mixing-properties-chromatic-number_images/imageFile3.png>)

We will use the remarkable lattice Λ constructed by Cartwright and Steger [CS], which acts transitively on the vertices of B, and, in particular, does not preserve the types of the vertices of B. In this Λ we will choose suitable congruence subgroups Λ(f) for some f ∈ Fq[1t ], and show:

![image 4](<2014-evra-mixing-properties-chromatic-number_images/imageFile4.png>)

- Theorem 1.2. For every integer d ≥ 3 and odd prime power q, there exists a sequence of ﬁnite (d−1)-dimensional simplicial complexes (Xn)n∈N with |Xn| → ∞, covered by Bd(Fq((t))), with injectivity radius

r(Xn) ≥

logq |Xn| 2(d − 1)(d2 − 1) −

![image 5](<2014-evra-mixing-properties-chromatic-number_images/imageFile5.png>)

- 1

![image 6](<2014-evra-mixing-properties-chromatic-number_images/imageFile6.png>)

- 2


(so, the chromatic number of every ball of radius 2(dlog−1)(q |Xd2n−|1) − 21 is two), while

![image 7](<2014-evra-mixing-properties-chromatic-number_images/imageFile7.png>)

![image 8](<2014-evra-mixing-properties-chromatic-number_images/imageFile8.png>)

χ(Xn) ≥

- 1

![image 9](<2014-evra-mixing-properties-chromatic-number_images/imageFile9.png>)

- 2 · q


- 1

![image 10](<2014-evra-mixing-properties-chromatic-number_images/imageFile10.png>)

- 2d


and so, χ(Xn) → ∞ when q → ∞. In particular, by letting q → ∞, this gives for every d ≥ 3, (d − 1)-dimensional simplicial complexes of arbitrary large ”girth” (twice the injectivity radius) and arbitrary large chromatic number.

Note, that in order to have arbitrarily large chromatic number, q must go to inﬁnity, otherwise the chromatic number of Xn, even as graphs, would be bounded since the degree would be bounded.

Moreover, for our complexes

diam(Xn) ≤

4 logq |Xn| d2 ≤ 8d · r(Xn),

![image 11](<2014-evra-mixing-properties-chromatic-number_images/imageFile11.png>)

for q ≫ d (see Remark 6.2). In particular, up to radius diam(X

n)

![image 12](<2014-evra-mixing-properties-chromatic-number_images/imageFile12.png>)

8d , the chromatic number of a ball in Xn is 2, and only for bigger balls it grows, eventually to inﬁnity.

As mentioned before, the fact that the quotients by congruence subgroups give large injectivity radius (and no small non-trivial homology cycles) was shown by Lubotzky and Meshulam in [LuMe] (see [GuLu, Section 4.1] for a ”general principle” of this kind). So the main novelty of the current paper is giving a lower bound on the chromatic number for some carefully chosen congruence subgroups (see §5.3 below). To this end we will prove the following result which is of independent interest:

- Theorem 1.3 (Colorful Mixing Lemma). Let F be a non-archimedean local ﬁeld with ﬁnite residue ﬁeld Fq, q odd, d ≥ 3, and B = Bd(F), the Bruhat-Tits building associated with PGLd(F). Let Γ ≤ PGLd(F) be a cocompact lattice preserving the type (coloring) function of B(0) with injectivity radius ≥ 2, so X = Γ\B is a simplicial complex with a type function τ : X(0) → Z/dZ. For each type i ∈ Z/dZ = {1,2,...,d}, let Vi ⊂ X(0) be the set of vertices of type i, i.e. Vi = τ−1(i).


Then for any choice of subsets Wi ⊆ Vi we have:

d

|Wi| |Vi|

|E(W1,...,Wd)| |X(d − 1)|

2d q12

−

≤

![image 13](<2014-evra-mixing-properties-chromatic-number_images/imageFile13.png>)

![image 14](<2014-evra-mixing-properties-chromatic-number_images/imageFile14.png>)

![image 15](<2014-evra-mixing-properties-chromatic-number_images/imageFile15.png>)

![image 16](<2014-evra-mixing-properties-chromatic-number_images/imageFile16.png>)

i=1

where E(W1,...,Wd) is the set of all (d − 1)-dimensional cells with exactly one vertex in each Wi,i = 1,...,d.

So, the lemma ensures that when q ≫ 0, the number |E(W1,...,Wd)| of facets with one vertex from each Wi is approximately what one should expect by random considerations.

This mixing lemma will be deduced from a more general one (see Corollary

- 3.7 below) using a result of Hee Oh [Oh] which gives a quantitative estimate for


Kazhdan property (T) of PGLd(F). In this argument we follow a related use of Oh’s work in [FGLNP].

It is interesting to observe that the above mixing lemma is for quotients of B = Bd(F) on which the d-coloring by the d types is preserved, but eventually our main theorem is about Xf = Λ(f)\B which are not d-colorable (in fact, our main goal is to show that they need many more colors!) We will acquire this by applying the colorful mixing lemma to the natural d-colorable d-sheeted cover of Xf (see Section 5 for details).

The paper is organized as follows. After a few preliminaries in Section 2, we show in Section 3 how the discrepancy of a colorful simplicial complex can be estimated using the eigenvalues of some naturally associated bipartite graphs. In Section 4, we will use Oh’s theorem and apply it to the colorable quotients of the Bruhat-Tits building of PGLd(F), to estimate these eigenvalues. In Section 5, we will follow carefully [LSV2] to choose the suitable congruence subgroups Λ(f) of Λ — the Cartwright-Steger lattice. We will use the congruence subgroups Λ(f) for which Λ(f)\B is a non-partite complex, see there. In Section 6, we collect all the information together and prove Theorem 1.2.

This paper is dedicated to Nati Linial who has pioneered the study of high dimensional expanders and many other things.

Acknowledgement. The authors are grateful to the ERC, ISF and NSF for partial support. This work is part of the Ph.D. theses of the ﬁrst two authors at the Hebrew University of Jerusalem, Israel. The authors are grateful to Nati Linial for valuable discussions.

# 2 Notations and conventions

Throughout this paper H is a ﬁnite d-uniform hypergraph, i.e. H = (V,E) and

- E ⊂ Vd . We say that H has a d-type function τ : V = V (H) → Z/dZ if each edge contains vertices of all d types, i.e. τ is one-to-one when restricted to each edge e ∈ E. We call such hypergraph d-partite and we also write it as H = (V0,...,Vd−1,E), where Vi = τ−1(i),i ∈ Z/dZ, and so E can be

considered as a subset of di=0−1 Vi. A 2-partite hypergraph is what is usually called a bipartite graph. Sometimes it is more convenient to think of Z/dZ as

{1,...,d}.

Recall that a simplicial complex X = (V,E) is a family E of ﬁnite subsets (called faces or simplicies) of the set of vertices V closed under inclusion, i.e. if

- F1 ∈ E and F2 ⊆ F1 then F2 ∈ E. For F ∈ E, denote dim(F) = |F| − 1 and X(i) the set of simplices of


dimension i. We say that dim(X) = d if X(d) = ∅ while X(d + 1) = ∅. It is called a pure complex of dimension d, if every maximal face in E is of dimension d. Given X = (V,E), we denote by X(i) the i-skeleton of X, this is the subcomplex of X of all the faces F in E with dim(F) ≤ i.

Given a pure simplicial complex X = (V,E) of dimension (d − 1), one can associate with it the d-uniform hypergraph H = H(X) = (V,X(d − 1)). Conversely if H = (V,E) is a d-uniform hypergraph then by taking E˜ = {F ⊆ V | ∃e ∈ E with F ⊆ e} we get a pure simplicial complex X = X(H) = (V,E˜) of dimension d−1. Clearly, X( H(X)) = X and H( X(H)) = H. Moreover if τ is a

type function on H, it deﬁnes a type function on X such that when restricted to every maximal face (facet) it is one-to-one. Such complexes are called balanced.

The theories of pure simplicial complexes and uniform hypergraphs are therefore completely equivalent. In this paper, we will use these languages alternately.

# 3 Discrepancy

For a d-partite hypergraph H = (V1,...,Vd,E), and a collection of subsets Wi ⊆ Vi,i = 1,...,d, denote E(W1,...,Wd) = E ∩ di=1 Wi, the edges in E with vertices in W1,...,Wd. We deﬁne the discrepancy of W1,...,Wd in H to be

d

discH(W1,...,Wd) = |E(W1,...,Wd)| |E|

|Wi| |Vi|

−

(3.1)

![image 17](<2014-evra-mixing-properties-chromatic-number_images/imageFile17.png>)

![image 18](<2014-evra-mixing-properties-chromatic-number_images/imageFile18.png>)

i=1

In other words, the discrepancy measures the diﬀerence between the actual portion of edges between W1,...,Wd and the expected portion if the hyperedges would have been chosen randomly uniformly.

For a biregular bipartite graph, the expander mixing lemma provides an upper bound on the discrepancy in the terms of the the second largest eigenvalue of the graph. In this section our aim is to give a similar bound for d-partite hypergraphs.

3.1 Discrepancy of bipartite graphs

- Let G = (V1,V2,E) be a ﬁnite connected bipartite (k1,k2)-biregular graph on n vertices, i.e. each vertex in V1 has exactly k1 neighbors, all of them in V2, and each vertex in V2 has k2 neighbors, all of them in V1, |V1| + |V2| = n, and so k1|V1| = k2|V2| = |E|.


Recall that the adjacency operator A = A(G) of the graph G is the following operator on the space of complex valued functions on the vertices

(Af)(v) =

f(u), (3.2)

u∼v

where u ∼ v stands for (u,v) ∈ E.

The following lemmas are probably known, but for lack of a reference we give short proofs.

- Lemma 3.1. Let λn ≤ ... ≤ λ2 ≤ λ1 be the eigenvalues of the adjacency operator A of G. Then


- 1. The spectrum is symmetric, i.e. λn−i+1 = −λi for all i.
- 2. The largest (resp. smallest) eigenvalue is λ1 = √k1k2 (resp., λn =


![image 19](<2014-evra-mixing-properties-chromatic-number_images/imageFile19.png>)

+ √k21V

√k1k2), whose corresponding eigenfunction is √k11V

![image 20](<2014-evra-mixing-properties-chromatic-number_images/imageFile20.png>)

![image 21](<2014-evra-mixing-properties-chromatic-number_images/imageFile21.png>)

![image 22](<2014-evra-mixing-properties-chromatic-number_images/imageFile22.png>)

−

√k11V (resp.

√k21V

1

2

![image 23](<2014-evra-mixing-properties-chromatic-number_images/imageFile23.png>)

![image 24](<2014-evra-mixing-properties-chromatic-number_images/imageFile24.png>)

1 −

).

2

Proof. Let f be an eigenfunction of A with an eigenvalue λ, i.e. Af = λ · f. Then it is easy to see that the following function

g(v) =

f(v), if v ∈ V1 −f(v), if v ∈ V2

(3.3)

satisﬁes Ag = (−λ) · g, which proves (1).

If λ is an eigenvalue of A, then λ2 is an eigenvalue of A2. The operator A2 expresses the 2-step walk on G, i.e. the (v,u)-entry in the matrix of A2 equals the number of paths of length 2 in G connecting the vertices v and u. By the (k1,k2)-regularity condition, the sum of any row of the matrix A2 is k1k2. Thus, A2 is the adjacency matrix of a k1k2-regular multigraph, i.e. a graph with loops and multiple edges, and hence its largest eigenvalue is k1k2. Thus the largest eigenvalue of A is √k1k2, and by (1), the smallest is −

√k1k2. By the biregularity condition,

![image 25](<2014-evra-mixing-properties-chromatic-number_images/imageFile25.png>)

![image 26](<2014-evra-mixing-properties-chromatic-number_images/imageFile26.png>)

. (3.4) Hence

) = k11V

and A(1V

) = k21V

A(1V

1

2

2

1

![image 27](<2014-evra-mixing-properties-chromatic-number_images/imageFile27.png>)

![image 28](<2014-evra-mixing-properties-chromatic-number_images/imageFile28.png>)

![image 29](<2014-evra-mixing-properties-chromatic-number_images/imageFile29.png>)

![image 30](<2014-evra-mixing-properties-chromatic-number_images/imageFile30.png>)

![image 31](<2014-evra-mixing-properties-chromatic-number_images/imageFile31.png>)

1 ± k21V

1 ± k21V

) = ± k1k2( k11V

A( k11V

). (3.5)

2

2

![image 32](<2014-evra-mixing-properties-chromatic-number_images/imageFile32.png>)

![image 33](<2014-evra-mixing-properties-chromatic-number_images/imageFile33.png>)

![image 34](<2014-evra-mixing-properties-chromatic-number_images/imageFile34.png>)

![image 35](<2014-evra-mixing-properties-chromatic-number_images/imageFile35.png>)

- Lemma 3.2. [Expander mixing lemma for bipartite graphs.] Let G = (V1,V2,E) be a bipartite (k1,k2)-biregular ﬁnite connected graph. Let λ = λ(G) be the second largest eigenvalue of the adjacency operator of G. Then for any S ⊆ V1 and T ⊆ V2,


√k1k2|S||T| |V1||V2|

![image 36](<2014-evra-mixing-properties-chromatic-number_images/imageFile36.png>)

![image 37](<2014-evra-mixing-properties-chromatic-number_images/imageFile37.png>)

|E(S,T)| −

≤ λ(G) |S||T| (3.6)

![image 38](<2014-evra-mixing-properties-chromatic-number_images/imageFile38.png>)

![image 39](<2014-evra-mixing-properties-chromatic-number_images/imageFile39.png>)

Proof. As before, denote by A the adjacency matrix of G, and its spectrum by λn ≤ ... ≤ λ2 ≤ λ1. Note that

![image 40](<2014-evra-mixing-properties-chromatic-number_images/imageFile40.png>)

|λ1| = |λn| = k1k2 and |λi| ≤ λ(G) for i = 2,...,n − 1. (3.7)

Let f1,...,fn be an orthonormal basis of eigenfunctions of A, i.e. Afi = λifi and fi,fj = δi,j, where the inner product is deﬁned as

![image 41](<2014-evra-mixing-properties-chromatic-number_images/imageFile41.png>)

f(v)g(v). (3.8)

f,g =

v∈V1⊔V2

Let 1S and 1T be the characteristic functions of S and T, respectively. Then |E(S,T)| = A1S,1T . Expressing them as linear combinations of orthonormal eigenvectors of A

n

n

tifi, (3.9) we get

sifi and 1T =

1S =

i=1

i=1

|E(S,T)| = A1S,1T =

n

![image 42](<2014-evra-mixing-properties-chromatic-number_images/imageFile42.png>)

![image 43](<2014-evra-mixing-properties-chromatic-number_images/imageFile43.png>)

![image 44](<2014-evra-mixing-properties-chromatic-number_images/imageFile44.png>)

sitiλi = s1t1λ1 + sntnλn +

i=1

n−1

![image 45](<2014-evra-mixing-properties-chromatic-number_images/imageFile45.png>)

sitiλi. (3.10)

i=2

By Lemma 3.1, we can assume that

and

1 k1|V1| + k2|V2|

f1 =

![image 46](<2014-evra-mixing-properties-chromatic-number_images/imageFile46.png>)

![image 47](<2014-evra-mixing-properties-chromatic-number_images/imageFile47.png>)

1 k1|V1| + k2|V2|

fn =

![image 48](<2014-evra-mixing-properties-chromatic-number_images/imageFile48.png>)

![image 49](<2014-evra-mixing-properties-chromatic-number_images/imageFile49.png>)

![image 50](<2014-evra-mixing-properties-chromatic-number_images/imageFile50.png>)

( k11V

1

![image 51](<2014-evra-mixing-properties-chromatic-number_images/imageFile51.png>)

+ k21V

) (3.11)

2

![image 52](<2014-evra-mixing-properties-chromatic-number_images/imageFile52.png>)

![image 53](<2014-evra-mixing-properties-chromatic-number_images/imageFile53.png>)

1 − k21V

), (3.12)

( k11V

2

Hence, as k1|V1| = k2|V2|, we get

s1 = f1,1S = |S| 2|V1|

= sn and t1 = f1,1T = |T| 2|V2|

![image 54](<2014-evra-mixing-properties-chromatic-number_images/imageFile54.png>)

![image 55](<2014-evra-mixing-properties-chromatic-number_images/imageFile55.png>)

= −tn. (3.13)

![image 56](<2014-evra-mixing-properties-chromatic-number_images/imageFile56.png>)

![image 57](<2014-evra-mixing-properties-chromatic-number_images/imageFile57.png>)

![image 58](<2014-evra-mixing-properties-chromatic-number_images/imageFile58.png>)

![image 59](<2014-evra-mixing-properties-chromatic-number_images/imageFile59.png>)

Therefore, since λ1 = √k1k2 = −λn,

![image 60](<2014-evra-mixing-properties-chromatic-number_images/imageFile60.png>)

√k1k2|S||T| 2 |V1||V2|

![image 61](<2014-evra-mixing-properties-chromatic-number_images/imageFile61.png>)

![image 62](<2014-evra-mixing-properties-chromatic-number_images/imageFile62.png>)

![image 63](<2014-evra-mixing-properties-chromatic-number_images/imageFile63.png>)

s1t1λ1 = sntnλn =

. (3.14)

![image 64](<2014-evra-mixing-properties-chromatic-number_images/imageFile64.png>)

![image 65](<2014-evra-mixing-properties-chromatic-number_images/imageFile65.png>)

And so,

√k1k2|S||T| |V1||V2|

n−1

n−1

![image 66](<2014-evra-mixing-properties-chromatic-number_images/imageFile66.png>)

![image 67](<2014-evra-mixing-properties-chromatic-number_images/imageFile67.png>)

![image 68](<2014-evra-mixing-properties-chromatic-number_images/imageFile68.png>)

siti ≤

sitiλi ≤ λ(G)

|E(S,T)| −

=

![image 69](<2014-evra-mixing-properties-chromatic-number_images/imageFile69.png>)

![image 70](<2014-evra-mixing-properties-chromatic-number_images/imageFile70.png>)

i=2

i=2

![image 71](<2014-evra-mixing-properties-chromatic-number_images/imageFile71.png>)

n−1

n−1

![image 72](<2014-evra-mixing-properties-chromatic-number_images/imageFile72.png>)

![image 73](<2014-evra-mixing-properties-chromatic-number_images/imageFile73.png>)

|ti|2) ≤ λ(G) 1S 2 1T 2 ≤ λ(G) |S||T|.

|si|2)(

≤ λ(G) (

i=2

i=2

(3.15)

![image 74](<2014-evra-mixing-properties-chromatic-number_images/imageFile74.png>)

![image 75](<2014-evra-mixing-properties-chromatic-number_images/imageFile75.png>)

![image 76](<2014-evra-mixing-properties-chromatic-number_images/imageFile76.png>)

![image 77](<2014-evra-mixing-properties-chromatic-number_images/imageFile77.png>)

We learned recently that Lemma 3.2 appears also in [BAV]. Recall that the normalized adjacency operator A = A(G) of a graph G is

the following operator on the space of complex valued functions on the vertices

1 deg v u∼v

( Af)(v) =

f(u), (3.16)

![image 78](<2014-evra-mixing-properties-chromatic-number_images/imageFile78.png>)

where u ∼ v stands for (u,v) ∈ E.

For a biregular bipartite graph G if f is an eigenfunction of the adjacency operator A(G) with an eigenvalue λ, than √deg1 vf(v) is an eigenfunction of the normalized adjacency operator A(G) with an eigenvalue √kλ

![image 79](<2014-evra-mixing-properties-chromatic-number_images/imageFile79.png>)

![image 80](<2014-evra-mixing-properties-chromatic-number_images/imageFile80.png>)

1k2 .

![image 81](<2014-evra-mixing-properties-chromatic-number_images/imageFile81.png>)

![image 82](<2014-evra-mixing-properties-chromatic-number_images/imageFile82.png>)

In particular, the largest and smallest eigenvalues of the normalized adjacency operator are 1 and (−1), respectively. The second largest eigenvalue λ˜ of A˜ is equal to

λ(G) √k1k2

λ(G) =

. (3.17)

![image 83](<2014-evra-mixing-properties-chromatic-number_images/imageFile83.png>)

![image 84](<2014-evra-mixing-properties-chromatic-number_images/imageFile84.png>)

Deﬁnition 3.3. Let G = (V1,V2,E) be a bipartite graph, S ⊆ V1 and T ⊆ V2. Then the discrepancy of these subsets is deﬁned to be

|T| |V2|

|S| |V1|

discG(S,T) = |E(S,T)| |E|

−

. (3.18)

![image 85](<2014-evra-mixing-properties-chromatic-number_images/imageFile85.png>)

![image 86](<2014-evra-mixing-properties-chromatic-number_images/imageFile86.png>)

![image 87](<2014-evra-mixing-properties-chromatic-number_images/imageFile87.png>)

In these terms, the following statement is a corollary of the Expander Mixing Lemma (Lemma 3.2). Corollary 3.4. Let G = (V1,V2,E) be a bipartite (k1,k2)-biregular ﬁnite graph. Then for any S ⊆ V1,T ⊆ V2

![image 88](<2014-evra-mixing-properties-chromatic-number_images/imageFile88.png>)

|T| |V2|

|S| |V1|

discG(S,T) ≤ λ˜(G) ·

(3.19)

![image 89](<2014-evra-mixing-properties-chromatic-number_images/imageFile89.png>)

![image 90](<2014-evra-mixing-properties-chromatic-number_images/imageFile90.png>)

Proof. By the (k1,k2)-biregularity of G |E| = k1|V1| = k2|V2| = k1k2|V1||V2|, (3.20)

![image 91](<2014-evra-mixing-properties-chromatic-number_images/imageFile91.png>)

hence √k1k2|S||T| |V1||V2|

![image 92](<2014-evra-mixing-properties-chromatic-number_images/imageFile92.png>)

|S||T| |V1||V2|

= |E| ·

. (3.21)

![image 93](<2014-evra-mixing-properties-chromatic-number_images/imageFile93.png>)

![image 94](<2014-evra-mixing-properties-chromatic-number_images/imageFile94.png>)

![image 95](<2014-evra-mixing-properties-chromatic-number_images/imageFile95.png>)

And therefore, by Lemma 3.2, we get

|E(S,T)| |E|

−

![image 96](<2014-evra-mixing-properties-chromatic-number_images/imageFile96.png>)

|T| |V1|

|S| |V2|

![image 97](<2014-evra-mixing-properties-chromatic-number_images/imageFile97.png>)

![image 98](<2014-evra-mixing-properties-chromatic-number_images/imageFile98.png>)

λ(G) √k1k2

≤

![image 99](<2014-evra-mixing-properties-chromatic-number_images/imageFile99.png>)

![image 100](<2014-evra-mixing-properties-chromatic-number_images/imageFile100.png>)

![image 101](<2014-evra-mixing-properties-chromatic-number_images/imageFile101.png>)

|S||T| |V1||V2|

. (3.22)

![image 102](<2014-evra-mixing-properties-chromatic-number_images/imageFile102.png>)

![image 103](<2014-evra-mixing-properties-chromatic-number_images/imageFile103.png>)

![image 104](<2014-evra-mixing-properties-chromatic-number_images/imageFile104.png>)

![image 105](<2014-evra-mixing-properties-chromatic-number_images/imageFile105.png>)

![image 106](<2014-evra-mixing-properties-chromatic-number_images/imageFile106.png>)

- 3.2 Discrepancy of hypergraphs


- Let H = (V1,...,Vd,E) be a d-partite hypergraph. Our aim is to give estimates and bounds on its discrepancy. We will do it by deﬁning various associated bipartite graphs and then we will bound the discrepancies of H by their discrepancies.


For i = 1,...,d, denote Ei = {F \{vi} | F ∈ E,vi ∈ Vi}, i.e. the set Ei is the set of of all edges of H with the vertex of type i being removed. A set Y ∈ Ei is called a wall of cotype i. Denote by Hi = (V1,...,Vi−1,Vi+1,...,Vd,Ei) the (d − 1)-partite hypergraph induced from H by removing the vertices of type i.

Denote by Bi the bipartite graph with Vi as one set of vertices and Ei as the second. A vertex vi ∈ Vi and a wall Y ∈ Ei are connected by an edge of Bi if their union forms an edge of H, i.e.{vi} ∪ Y ∈ E. We will write Bi = (Vi,Ei,EB

). An edge of Bi is a pair (vi,F \ {vi}), where F ∈ E is an edge of H. Following the terminology of simplicial complexes, this is the ”vertices versus walls” graph. Note that since every edge of H has exactly one vertex in Vi, there is a natural bijection between the edges of Bi and the edges of H.

i

As before, for a collection of subsets Wj ⊆ Vj for j = 1,...,d, we denote by E(W1,...,Wd) the set of all edges of H with vertices in the sets W1,...,Wd. Analogously, for Hi we will denote by Ei(W1,...,Wd) the subset of all edges with vertices in W1,...,Wi−1,Wi+1,...,Wd. For the graph Bi we will denote by EB

(Wi,Ei(W1,...,Wd)) the set of all edges of Bi with one vertex in Wi and the other in Ei(W1,...,Wd). Note that the above mentioned bijection between the edges of H and Bi restricts to a bijection between E(W1,...,Wd) and EB

i

(Wi,Ei(W1,...,Wd)).

i

The following lemma reduces the question of bounding the discrepancy of a d-partite hypergraph to its induced hypergraphs and bipartite graphs.

- Lemma 3.5. Let Wj ⊆ Vj for j = 1,...,d. Then for i = 1,...,d, discH(W1,...,Wd) ≤


(Wi,Ei(W1,...,Wd)) + |Wi| |Vi|

(W1,...,Wi−1,Wi+1,...,Wd) (3.23)

discH

discB

![image 107](<2014-evra-mixing-properties-chromatic-number_images/imageFile107.png>)

i

i

Proof. By the deﬁnition of the bipartite graph Bi

and hence:

(Wi,Ei(W1,...,Wd))| |EB

= |EB

|E(W1,...,Wd))| |E|

i

![image 108](<2014-evra-mixing-properties-chromatic-number_images/imageFile108.png>)

![image 109](<2014-evra-mixing-properties-chromatic-number_images/imageFile109.png>)

i|

(3.24)

d

discH(W1,...,Wd) = |E(W1,...,Wd)| |E|

|Wj| |Vj|

−

=

![image 110](<2014-evra-mixing-properties-chromatic-number_images/imageFile110.png>)

![image 111](<2014-evra-mixing-properties-chromatic-number_images/imageFile111.png>)

j=1

|Wi| |Vi|

|Ei(W1,...,Wd)| |Ei|

= |E(W1,...,Wd)| |E|

−

·

+

![image 112](<2014-evra-mixing-properties-chromatic-number_images/imageFile112.png>)

![image 113](<2014-evra-mixing-properties-chromatic-number_images/imageFile113.png>)

![image 114](<2014-evra-mixing-properties-chromatic-number_images/imageFile114.png>)

  ≤

 |Ei(W1,...,Wd)|

d

+ |Wi| |Vi|

|Wj| |Vj|

·

−

![image 115](<2014-evra-mixing-properties-chromatic-number_images/imageFile115.png>)

![image 116](<2014-evra-mixing-properties-chromatic-number_images/imageFile116.png>)

![image 117](<2014-evra-mixing-properties-chromatic-number_images/imageFile117.png>)

|Ei|

j=1,j =i

|Wi| |Vi|

|Ei(W1,...,Wd)| |Ei|

(W1,...,Wd)| |EB

|EB

i

−

·

≤

+

![image 118](<2014-evra-mixing-properties-chromatic-number_images/imageFile118.png>)

![image 119](<2014-evra-mixing-properties-chromatic-number_images/imageFile119.png>)

![image 120](<2014-evra-mixing-properties-chromatic-number_images/imageFile120.png>)

i|

d

+ |Wi| |Vi|

|Ei(W1,...,Wd)| |Ei|

|Wj| |Vj|

·

−

=

![image 121](<2014-evra-mixing-properties-chromatic-number_images/imageFile121.png>)

![image 122](<2014-evra-mixing-properties-chromatic-number_images/imageFile122.png>)

![image 123](<2014-evra-mixing-properties-chromatic-number_images/imageFile123.png>)

j=1,j =i

(Wi,Ei(W1,...,Wd)) + |Wi| |Vi|

· discH

= discB

(W1,...,Wi−1,Wi+1,...,Wd)

![image 124](<2014-evra-mixing-properties-chromatic-number_images/imageFile124.png>)

i

i

![image 125](<2014-evra-mixing-properties-chromatic-number_images/imageFile125.png>)

![image 126](<2014-evra-mixing-properties-chromatic-number_images/imageFile126.png>)

![image 127](<2014-evra-mixing-properties-chromatic-number_images/imageFile127.png>)

![image 128](<2014-evra-mixing-properties-chromatic-number_images/imageFile128.png>)

Deﬁnition 3.6. A d-partite hypergraph H is called type-regular if for any type i, 1 ≤ i ≤ d, there exist ki,li ∈ N, such that each i-type vertex is contained in exactly ki hyperedges in H and each cotype i wall is contained in exactly li hyperedges in H. Note that if H is type-regular, then each induced bipartite graph Bi, deﬁned above, is (ki,li)-biregular.

Recall that for a graph G we denote by λ˜(G) the normalized second largest eigenvalue. We can now generalize Corollary 3.4 from graphs to hypergraphs.

),

- Corollary 3.7. Let H be a d-partite type-regular hypergraph. Let Bi = (Vi,Ei,EB


i

i = 1 ...,d, be the induced bipartite graphs of H, as deﬁned above. Then for any W1 ⊆ V1,...,Wd ⊆ Vd,

![image 129](<2014-evra-mixing-properties-chromatic-number_images/imageFile129.png>)

d−1

|Wi| |Vi|

λ ˜(Bi) ·

discH(W1,...,Wd) ≤

. (3.25)

![image 130](<2014-evra-mixing-properties-chromatic-number_images/imageFile130.png>)

i=1

In particular

λ˜(Bi). (3.26)

discH(W1,...,Wd) ≤ (d − 1) · max

max

Wi⊆Vi

1≤i≤d−1

Proof. Since H is type-regular, for any type i ∈ Z/dZ, there exists a number li ∈ N, such that any wall of cotype i is contained in exactly li facets. Hence,

li|Ei(W1,...,Wd)| = |E(W1,...,Wi−1,Vi,Wi+1,...,Wd)| and li|Ei| = |E|, (3.27)

and so,

(W1,...,Wd) = |Ei(W1,...,Wd)| |Ei|

discH

![image 131](<2014-evra-mixing-properties-chromatic-number_images/imageFile131.png>)

i

d

|Wj| |Vj|

−

![image 132](<2014-evra-mixing-properties-chromatic-number_images/imageFile132.png>)

j=1,j =i

=

d

|Vi| |Vi|

|Wj| |Vj|

= |E(W1,...,Wi−1,Vi,Wi+1,...,Wd)| |E|

−

=

![image 133](<2014-evra-mixing-properties-chromatic-number_images/imageFile133.png>)

![image 134](<2014-evra-mixing-properties-chromatic-number_images/imageFile134.png>)

![image 135](<2014-evra-mixing-properties-chromatic-number_images/imageFile135.png>)

j=1,j =i

= discH(W1,...,Wi−1,Vi,Wi+1,...,Wd).

- Corollary 3.4 gives that for any i = 1,...,d,


(Wi,Ei(V1,...,Vi−1,Wi+1,...,Wd)) ≤ λ˜(Bi) ·

discB

i

So, by iterating on Lemma 3.5 and equation (3.28), we get

![image 136](<2014-evra-mixing-properties-chromatic-number_images/imageFile136.png>)

|Wi| |Vi|

![image 137](<2014-evra-mixing-properties-chromatic-number_images/imageFile137.png>)

(3.28)

(3.29)

![image 138](<2014-evra-mixing-properties-chromatic-number_images/imageFile138.png>)

|W1| |V1|

discH(W1,...,Wd) ≤ λ˜(B1) ·

+ discH(V1,W2,...,Wd) ≤

![image 139](<2014-evra-mixing-properties-chromatic-number_images/imageFile139.png>)

![image 140](<2014-evra-mixing-properties-chromatic-number_images/imageFile140.png>)

![image 141](<2014-evra-mixing-properties-chromatic-number_images/imageFile141.png>)

|W1| |V1|

|W2| |V2|

+ λ˜(B2) ·

≤ λ˜(B1) ·

+ discH(V1,V2,W3,...,Wd) ≤

![image 142](<2014-evra-mixing-properties-chromatic-number_images/imageFile142.png>)

![image 143](<2014-evra-mixing-properties-chromatic-number_images/imageFile143.png>)

(3.30)

![image 144](<2014-evra-mixing-properties-chromatic-number_images/imageFile144.png>)

d−1

|Wi| |Vi|

λ˜(Bi) ·

... ≤

+ discH(V1,V2,...,Vd−1,Wd) =

![image 145](<2014-evra-mixing-properties-chromatic-number_images/imageFile145.png>)

i=1

![image 146](<2014-evra-mixing-properties-chromatic-number_images/imageFile146.png>)

d−1

|Wi| |Vi|

λ˜(Bi) ·

=

![image 147](<2014-evra-mixing-properties-chromatic-number_images/imageFile147.png>)

i=1

The last equality follows from the fact that discH(V1,V2,...,Vd−1,Wd) = 0, since any vertex w of Wd is contained in kd edges and for elements w = w′ of Wd these edges are diﬀerent.

![image 148](<2014-evra-mixing-properties-chromatic-number_images/imageFile148.png>)

![image 149](<2014-evra-mixing-properties-chromatic-number_images/imageFile149.png>)

![image 150](<2014-evra-mixing-properties-chromatic-number_images/imageFile150.png>)

![image 151](<2014-evra-mixing-properties-chromatic-number_images/imageFile151.png>)

# 4 Colorful Mixing Lemma for Ramanujan Complexes

The goal of this section is to prove the Colorful Mixing Lemma (Theorem 1.3).

Let F be a local non-archimedean ﬁeld whose residue ﬁeld is of order q, and let B = Bd(F), d ≥ 3, be the Bruhat-Tits building of type A˜d−1 associated with PGLd(F). The building is equipped with a natural d-type function which gives it a structure of an inﬁnite d-partite hypergraph. For any cocompact lattice Γ ≤ PGLd(F) preserving the type function, the quotient BΓ = Γ\Bd(F) is a ﬁnite d-partite hypergraph. Recall the notation dist(Γ) = minx∈B,1 =γ∈Γ dist(γ.x,x), and that the injectivity radius r(Γ) of BΓ is equal to ⌊dist(Γ)2 −1⌋, since the building B is its universal cover. The Colorful Mixing Lemma reads as follows. Assuming that the injectivity radius of BΓ is at least 2, for any choice of subsets Wi of vertices of BΓ of type i:

![image 152](<2014-evra-mixing-properties-chromatic-number_images/imageFile152.png>)

2d q1/2

(W1,...,Wd) ≤

discB

. (4.1)

![image 153](<2014-evra-mixing-properties-chromatic-number_images/imageFile153.png>)

Γ

- 4.1 The building of type A˜d−1


In this subsection we review the structure and basic properties of the building Bd(F). Rather than using the general language of buildings, we will present it and prove its properties from basic principles.

Let F be a local non-archimedean ﬁeld with a discrete valuation ν : F∗ → Z, let O be the ring of integers of F, π a uniformizer and q < ∞ the cardinality of the residue ﬁeld F¯ = O/πO. For example, F = Fq((t)) the Laurent series, ν = deg, O = Fq[[t]] the Taylor series and π = t.

The building B = Bd(F) associated to a local ﬁeld F is an inﬁnite (d − 1)dimensional pure simplicial complex constructed as follows.

Vertices. A lattice is a free O-submodule of V = Fd of rank d, i.e. it is of the form < v1,...,vd >= Ov1 + ... + Ovd where {v1,...,vd} is a basis for V . Two lattices L1,L2 are said to be equivalent if there exists λ ∈ F∗ such that L1 = λL2. The equivalence class of a lattice L is denoted by [L]. The set of equivalence classes of lattices forms the set of vertices of the building B.

Faces. Two vertices [L1],[L2] are connected by an edge in the building, if there exist representatives L′1 ∈ [L1],L′2 ∈ [L2] such that πL′1 ⊂ L′2 ⊂ L′1. Note that L′1/πL′1 is a d-dimensional vector space over the ﬁnite ﬁeld F¯ = O/πO. Fixing a representative L′1 of a vertex [L1] gives rise to a one-to-one correspondence between the neighbors of [L1] and the proper subspaces of L′1/πL′1.

A set of vertices {[L1],...,[Lk]} forms a (k − 1)-face in the building if there exist representatives L′i ∈ [Li] such that (maybe, after renumbering) πL′1 ⊂ L′k ⊂ ... ⊂ L′2 ⊂ L′1. Note that a (k − 1)-simplex in the building gives rise to a k-ﬂag of subspaces in L′1/πL′1, hence the dimension of the building is (d − 1).

The link of every vertex of B is isomorphic to the ﬂag complex of F¯d = Fdq.

Action of GLd(F). The group GLd(F) acts transitively on the lattices in Fd, and its center preserves the equivalence classes, hence this action induces an action of G = PGLd(F) on the vertices of the building. The stabilizer of the vertex [Od], which is called the standard lattice, is K = PGLd(O), hence the set G/K may be identiﬁed with the set of vertices of the building.

Type function. For each vertex [L] there exists an element g ∈ G such that [L] = g[Od]. Deﬁne the type of [L] to be τ([L]) = ν(det(g)) mod d. It is well deﬁned since for k ∈ K the determinant det(k) ∈ O∗ and hence ν(det(k)) = 0. This deﬁnes a type function from the vertices of the building to Z/dZ. Note that a maximal simplex contains vertices of all d types.

For i ∈ Z/dZ, denote Gi = (ν ◦ det)−1(i). Then G0 is the subgroup of G of type-preserving elements, and Gi are its cosets. We saw before that the vertices of the building may be identiﬁed with G/K. Under this identiﬁcation, Gi/K is the set of vertices of type i.

The group G0 of type-preserving elements is equal to PSLd(F) · K. It is a normal subgroup of G = PGLd(F) of index d, since G0 = {g ∈ G | ν(det(g)) = 0 mod d}.

Let now Γ be a cocompact discrete subgroup of G which is contained in G0 and BΓ = Γ\B. This is a ﬁnite simplicial complex and τ is well deﬁned on

BΓ. The vertices V of BΓ may be identiﬁed with Γ\G/K, and in this case the i-typed vertices Vi of BΓ are identiﬁed with Γ\Gi/K.

![image 154](<2014-evra-mixing-properties-chromatic-number_images/imageFile154.png>)

Relative position. Deﬁne the set A+ = {a = (a1,...,ad) ∈ Zd/(1,...,1)Z | a1 ≤ ... ≤ ad}, and let Λ+ be the set of diagonal matrices in PGLd(F) of the form πa = π(a

![image 155](<2014-evra-mixing-properties-chromatic-number_images/imageFile155.png>)

![image 156](<2014-evra-mixing-properties-chromatic-number_images/imageFile156.png>)

,...,πa

) for (a1,...,ad) ∈ A+. Denote A0 = {(a1,...,ad) ∈ A | ai ≡ 0 mod d}. The Cartan decomposition G = KΛ+K, means that each element g ∈ G may be written uniquely as g = k1πak2 for k1,k2 ∈ K and a ∈ A+. By identifying the vertices of the building with G/K, for any two vertices x = gK and y = hK we deﬁne the relative position of y

1,...,ad) = diag(πa

d

1

![image 157](<2014-evra-mixing-properties-chromatic-number_images/imageFile157.png>)

- w.r.t. x, to be the unique element a ∈ A+ such that Kg−1hK = KπaK. We get a function B(0) × B(0) → A+, where B(0) is the set of vertices of B.

In other words, for two vertices x,y consider a basis {v1,...,vd} of Fd, such that x = [Ov1 + ... + Ovd] and y = [πa

1

Ov1 + ... + πa

d

Ovd] (one can always ﬁnd such a basis). Let g ∈ G = PGLd(F) be the element which sends the standard basis to {v1,...,vd}, and let a = (a1,...,ad) ∈ A+. Then x = g.[Od] and y = (gπa).[Od], hence ”x−1y” = πa, and the relative position of y w.r.t. x is a. We also see that in this case τ(x) − τ(y) ≡ ai mod d, and the relative position of x w.r.t. y is (0,ad − ad−1,...,ad − a1). In addition, if y is in relative position (a1,...,ad) w.r.t. x, then the distance between them, i.e. the number of edges in the shortest path connecting them, is equal to dist(x,y) = ad − a1. The action of G on B preserves the relative position of pairs of vertices.

![image 158](<2014-evra-mixing-properties-chromatic-number_images/imageFile158.png>)

![image 159](<2014-evra-mixing-properties-chromatic-number_images/imageFile159.png>)

![image 160](<2014-evra-mixing-properties-chromatic-number_images/imageFile160.png>)

We note that by the Cartan decomposition, for any a ∈ A+, K acts transitively on the vertices of a ﬁxed relative position a w.r.t. the standard lattice x0 = [Od]. By the transitivity of the action of G, for any vertex x, Kx = StabG(x) acts transitively on the vertices of relative position a w.r.t.

- x. Various combinatorial aspects of the building can be expressed by the relative


position:

- Lemma 4.1. Let y be a vertex in the building with relative position a = (a1,...,ad) w.r.t. x. Then:


![image 161](<2014-evra-mixing-properties-chromatic-number_images/imageFile161.png>)

- 1. x and y are neighbors if and only if ad = a1+1, i.e. a = (0,...,0,1 ...,1).

![image 162](<2014-evra-mixing-properties-chromatic-number_images/imageFile162.png>)

- 2. x and y are of the same type if and only if ai = 0 modulo d, i.e. a ∈ A0.
- 3. x and y are separated by a common wall of codimension 1 (i.e., there exists a (d−2)-face σ such that σ∪{x} and σ∪{y} are both (d−1)-faces) if and only if either a = (0,...,0), i.e. they coincide, or a = (−1,0,...,0,1) = (0,1,...,1,2).


![image 163](<2014-evra-mixing-properties-chromatic-number_images/imageFile163.png>)

![image 164](<2014-evra-mixing-properties-chromatic-number_images/imageFile164.png>)

![image 165](<2014-evra-mixing-properties-chromatic-number_images/imageFile165.png>)

Proof. Statements (1) and (2) follow immediately from the deﬁnition of the relative position and the discussion above.

![image 166](<2014-evra-mixing-properties-chromatic-number_images/imageFile166.png>)

To prove (3), assume ﬁrst that y is in relative position (0,1,...,1,2) w.r.t. x. This implies that x has a representative L with an O-basis {v1,...,vd} such that L′ =< v1,πv2,...,πvd−1,π2vd > represents y. For i = 1,...,d − 1, denote Li =< v1,...,vi,πvi+1,...,πvd >. Then the set σ = {zi = [Li] | 1 ≤ i ≤ d − 1} forms a (d − 2)-cell, and both σ ∪ {x} and σ ∪ {y} are facets of B, since

πL ⊂ L1 ⊂ ...Ld−1 ⊂ L and πLd−1 ⊂ L′ ⊂ L1 ⊂ ··· ⊂ Ld−1. (4.2)

To see the opposite direction, assume that there exists a (d − 2)-cell σ with both σ ∪ {x} and σ ∪ {y} being facets of B. As the link of every vertex of B is the ﬂag complex of Fdq, one can decuce that σ is contained in (q + 1) facets. The fact that σ ∪ {x} is a facet, implies that there exists a representative L of x with an O-basis {v1,...,vd} such that σ = {zi = [Li] | 1 ≤ i ≤ d − 1}, where Li =< v1,...,vi,πvi+1,...,πvd >.

Here is a list of representatives of (q +1) vertices {yε = [L′ε] | ε ∈ Fq ∪ {∞}} such that σ ∪ {yε} is a facet of B:

L′∞ =< πv1,...,πvd > (note that y∞ = [L′∞] = x) (4.3) and for ε ∈ Fq

L′ε =< v1 + ε · πvd,πv2,...,πvd−1,π2vd > . (4.4)

One can easily check that all the yε’s are not equivalent and σ∪{yε} is a facet, so these are all the facets containing σ. For every ε ∈ Fq, yε is in relative position (0,1,...,1,2) w.r.t. x. This can be seen by taking {v1 + ε · πvd,v2,...,vd} as a basis for L.

![image 167](<2014-evra-mixing-properties-chromatic-number_images/imageFile167.png>)

![image 168](<2014-evra-mixing-properties-chromatic-number_images/imageFile168.png>)

![image 169](<2014-evra-mixing-properties-chromatic-number_images/imageFile169.png>)

![image 170](<2014-evra-mixing-properties-chromatic-number_images/imageFile170.png>)

![image 171](<2014-evra-mixing-properties-chromatic-number_images/imageFile171.png>)

- 4.2 Hecke operators


![image 172](<2014-evra-mixing-properties-chromatic-number_images/imageFile172.png>)

For any a = (a1,...,ad) ∈ A+, deﬁne the following Hecke operator on the vertices of the building Ha : L2(B(0)) → L2(B(0)),

1 µ(KπaK) yK∈xKπ

f(yK),

Haf(xK) =

![image 173](<2014-evra-mixing-properties-chromatic-number_images/imageFile173.png>)

aK

where µ is the Haar measure on G, normalized such that µ(K) = 1, (i.e. µ(KπaK) = |KπaK/K|). This is the normalized ﬁnite sum over the vertices yK of relative position a w.r.t. xK. Note that µ(KπaK) is equal to the number of vertices which are of relative position a w.r.t. x.

If Γ is a lattice in G with dist(Γ) > ad − a1, then the action of Γ commutes with Ha. Hence, we can consider Ha also as a map Ha : L2(V ) → L2(V ) where V is the set of vertices of Γ\B, so

1 µ(KπaK) ΓyK∈ΓxKπ

Haf(ΓxK) =

f(ΓyK).

![image 174](<2014-evra-mixing-properties-chromatic-number_images/imageFile174.png>)

aK

Moreover if a ∈ A0, then the type of each yK ∈ xKπaK is the same as that of xK, so we may consider Ha as a map Ha : L2(Vi) → L2(Vi), where Vi is the set of vertices of type i.

Finally, note that if we consider f ∈ L2(Γ\G/K), as a K-invariant function in L2(Γ\G), and dk is the Haar measure on K, normalized such that dk(K) = 1, we may write Ha as an integral over K, instead of a sum,

Haf(x) =

f(xkπa)dk. (4.5)

K

Let (ρ,L2(Γ\G)) be the unitary G-representation, given by right translations ρ(g)f(x) = f(xg). The following lemma will allow us to give bounds on the spectra of the Hecke operators, assuming we have bounds on the matrix coeﬃcients of the representation L2(Γ\G). Bounds on the matrix coeﬃcients will be given at the end of this section, using a theorem by Oh.

- Lemma 4.2. Let a ∈ A+. For any K-invariant vectors f1,f2 in L2(Γ\G), Haf1,f2 = ρ(πa)f1,f2 (4.6)

Proof.

Haf1,f2 =

Γ\G

Ha (f1(x)) f2(x)dx =

![image 175](<2014-evra-mixing-properties-chromatic-number_images/imageFile175.png>)

=

Γ\G K

f1(xkπa)dk f2(x)dx =

![image 176](<2014-evra-mixing-properties-chromatic-number_images/imageFile176.png>)

=

K Γ\G

f1(xkπa)f2(x)dx dk,

![image 177](<2014-evra-mixing-properties-chromatic-number_images/imageFile177.png>)

(4.7)

where the last equality follows from Fubini’s theorem. Since the measure dx is right invariant we can replace x by xk, and by the K-invariance of f2 we get

Haf1,f2 =

K Γ\G

f1(xπa)f2(x)dx dk =

![image 178](<2014-evra-mixing-properties-chromatic-number_images/imageFile178.png>)

=

Γ\G

f1(xπa)f2(x)dx = ρ(πa)f1,f2 .

![image 179](<2014-evra-mixing-properties-chromatic-number_images/imageFile179.png>)

![image 180](<2014-evra-mixing-properties-chromatic-number_images/imageFile180.png>)

![image 181](<2014-evra-mixing-properties-chromatic-number_images/imageFile181.png>)

![image 182](<2014-evra-mixing-properties-chromatic-number_images/imageFile182.png>)

![image 183](<2014-evra-mixing-properties-chromatic-number_images/imageFile183.png>)

- Lemma 4.3. Let i ∈ Z/dZ be a type and f ∈ L20(Vi), where L20(Vi) = {g ∈


= 0}. Extend f to a function in L20(V ) by setting it to be zero outside Vi. Recall that V = Γ\G/K, where K = PGLd(O), and consider f as a K-invariant vector in L2(Γ\G). Then f is orthogonal to any G+-invariant vector, where G+ = PSLd(F).

L2(Vi) | g,1V

i

Proof. Let h ∈ L2(Γ\G) be a G+-invariant function. Deﬁne h˜(x) = K h(xk)dk. Recall that the type-preserving subgroup G0 is equal to G+K. So, h˜ is G+invariant and K-invariant, and hence G0-invariant. Since each Gi is a G0-coset, h˜ is constant on each Γ\Gi and hence on Vi = Γ\Gi/K. Now, since f ∈ L20(Vi) we get that

f,h˜ = 0. On the other hand,

f,h =

![image 184](<2014-evra-mixing-properties-chromatic-number_images/imageFile184.png>)

f(x)h(x)dx =

Γ\G

![image 185](<2014-evra-mixing-properties-chromatic-number_images/imageFile185.png>)

f(x)h(x)dx dk =

K Γ\G

=

f(xk−1)h(x)dx dk =

![image 186](<2014-evra-mixing-properties-chromatic-number_images/imageFile186.png>)

![image 187](<2014-evra-mixing-properties-chromatic-number_images/imageFile187.png>)

f(y)h(yk)dy dk =

K Γ\G

K Γ\G

![image 188](<2014-evra-mixing-properties-chromatic-number_images/imageFile188.png>)

![image 189](<2014-evra-mixing-properties-chromatic-number_images/imageFile189.png>)

f(y)h˜(y)dy = f,h˜ ,

h(yk)dk dy =

=

f(y)

K

Γ\G

Γ\G

where again we used: K dk = 1, the K-invariance of f, the Haar measure dx being right invariant and Fubini’s Theorem, respectively. So f is orthogonal to

- h, which proves the claim.


![image 190](<2014-evra-mixing-properties-chromatic-number_images/imageFile190.png>)

![image 191](<2014-evra-mixing-properties-chromatic-number_images/imageFile191.png>)

![image 192](<2014-evra-mixing-properties-chromatic-number_images/imageFile192.png>)

![image 193](<2014-evra-mixing-properties-chromatic-number_images/imageFile193.png>)

![image 194](<2014-evra-mixing-properties-chromatic-number_images/imageFile194.png>)

Recall that A0 = {(a1,...,ad) ∈ A| ai ≡ 0(mod d)}, is the set of typepreserving translations (see Lemma 4.1). So, for any a ∈ A0 the Hecke operator Ha is a well deﬁned operator from L2(Vi) to itself, for any type i.

Combining Lemmas 4.2 and 4.3 we get the following bound on the norm of the Hecke operator in terms of the matrix coeﬃcients.

- Corollary 4.4. For any type i ∈ Z/dZ and any a ∈ A0,


ρ(πa)f1,f2 (4.8)

0(Vi) ≤ sup f1,f2

Ha L2

where f1,f2 run over all the K-invariant normalized vectors in L2(Γ\Gi) orthogonal to any G+-invariant vector (when considered as functions in L2(Γ\G) as in Lemma 4.3.)

Proof. Let f1,f2 ∈ L20(Vi) of norm 1 be such that Ha L2

0(Vi) = Haf1,f2 . By Ha L2

- Lemma 4.2,


0(Vi) = ρ(πa)f1,f2

and by Lemma 4.3, f1,f2 are orthogonal to any G+-invariant vector in L2(Γ\G), which proves the claim.

![image 195](<2014-evra-mixing-properties-chromatic-number_images/imageFile195.png>)

![image 196](<2014-evra-mixing-properties-chromatic-number_images/imageFile196.png>)

![image 197](<2014-evra-mixing-properties-chromatic-number_images/imageFile197.png>)

![image 198](<2014-evra-mixing-properties-chromatic-number_images/imageFile198.png>)

- 4.3 Adjacency operators


Again let Γ be a cocompact lattice in G with Γ ⊆ G0, i.e. Γ preserves the type function. So BΓ = Γ\B is a d-partite hypergraph.

Recall that for each type i ∈ Z/dZ, the induced bipartite graph Bi of the d-partite hypergraph BΓ, has the i-type vertices Vi on one side, and the walls Ei, i.e. the simplicies of dimension (d − 2) of cotype i, on the other side. A vertex and a wall are connected if their union forms a maximal simplex in BΓ.

Let A = A(Bi) be the normalized adjacency operator of Bi, i.e. Af(x) :=

1 deg(x) y∼x

f(y),

![image 199](<2014-evra-mixing-properties-chromatic-number_images/imageFile199.png>)

where the summation is over all the neighbors of x in Bi. In the natural basis the matrix of A is a block matrix of the form

A =

0 N Nt 0

,

where N is a matrix of size |Vi| × |Ei|.

Deﬁne Di to be the multigraph on Vi, where two vertices are connected by as many edges as there are paths of length 2 in the graph Bi connecting them. Then the matrix NNt is the matrix of the normalized adjacency operator of the multigraph Di. Note that the number of loops on each vertex in Di is equal to the vertex degree in Bi.

The non-zero eigenvalues of the matrices NNt and NtN coincide, and λ = 0 is an eigenvalue of NNt if and only if

√

![image 200](<2014-evra-mixing-properties-chromatic-number_images/imageFile200.png>)

λ is an eigenvalue of A. So, in order to bound the eigenvalues of A, it is enough to bound the eigenvalues of NNt.

- Lemma 4.5. The operator NNt, as an operator from L2(Vi) to itself, is a convex sum of two Hecke operators I = H(0,...,0) and H(−1,0,...,0,1), in fact,


1 q + 1

q q + 1

NNt =

I +

H(−1,0,...,0,1).

![image 201](<2014-evra-mixing-properties-chromatic-number_images/imageFile201.png>)

![image 202](<2014-evra-mixing-properties-chromatic-number_images/imageFile202.png>)

Proof. By Lemma 4.1, two vertices of type i of the building share a common wall if and only if their relative position is either (0,...,0) or (−1,0,...,0,1), i.e. a vertex xK of type i shares a common wall with vertices which are either the right K-cosets in xKπ(−1,0,...,0,1)K or xK itself.

![image 203](<2014-evra-mixing-properties-chromatic-number_images/imageFile203.png>)

![image 204](<2014-evra-mixing-properties-chromatic-number_images/imageFile204.png>)

In the quotient BΓ, the vertex ΓxK of type i can be lifted to the vertex xK in the building. The i-type vertices in the building which share a common wall with xK are mapped surjectively to the vertices in the quotient which share a common wall with ΓxK in the quotient. Since Γ has injectivity radius ≥ 2, this map is also injective.

Hence, after the normalization, by the deﬁnition of the Hecke operators we get, that

NNt = c(0,...,0)H(0,...,0) + c(−1,0,...,0,1)H(−1,0,...,0,1), where ca is the number of edges in Di connecting a vertex xK to vertices of relative position a with respect to it, divided by the degree of the vertex xK in the graph Di. Clearly c(0,...,0) + c(−1,0,...,0,1) = 1.

Each wall of the building Bd(F) is contained in exactly q + 1 chambers, and each i-type vertex is contained in exactly r chambers (= facets), where the number r depends on d and q, but not on the vertex. In the quotient BΓ, since the injectivity radius ≥ 2, each wall is also contained in exactly q + 1 chambers and each i-type vertex is contained in r chambers. Hence Bi is a bipartite (r,q + 1)-biregular graph. Therefore Di is a r(q + 1) regular multigraph, where each vertex has exactly r loops, so c(0,...,0) = q+11 , which completes the proof.

![image 205](<2014-evra-mixing-properties-chromatic-number_images/imageFile205.png>)

![image 206](<2014-evra-mixing-properties-chromatic-number_images/imageFile206.png>)

![image 207](<2014-evra-mixing-properties-chromatic-number_images/imageFile207.png>)

![image 208](<2014-evra-mixing-properties-chromatic-number_images/imageFile208.png>)

![image 209](<2014-evra-mixing-properties-chromatic-number_images/imageFile209.png>)

We can now get the following bound on the normalized second largest eigenvalue of Bi, in terms of matrix coeﬃcients of a certain unitary representation.

- Corollary 4.6. Let (ρ,L2(Γ\G)) be the unitary G-representation given by right translation ρ(g)f(x) = f(xg). Let W ≤ L2(Γ\G) be the subspace of K-invariant vectors which are orthogonal to all G+-invariant vectors. For any g ∈ G, deﬁne


ρW(g) to be the maximal absolute value of a matrix coeﬃcient of normalized vectors from W on the element g, i.e.

| ρ(g)f1,f2 |.

ρW(g) = sup

f1,f2∈W, f1 = f2 =1

Then the normalized second largest eigenvalue of Bi, λ˜i = λ˜(Bi), satisﬁes

![image 210](<2014-evra-mixing-properties-chromatic-number_images/imageFile210.png>)

1 q + 1

q q + 1

![image 211](<2014-evra-mixing-properties-chromatic-number_images/imageFile211.png>)

λ˜i ≤

ρW(π(−1,0,...,0,1)) ≤ q−1 + ρW(π(−1,0,...,0,1)). (4.9) Proof. By Lemma 4.5 and the discussion before it,

+

![image 212](<2014-evra-mixing-properties-chromatic-number_images/imageFile212.png>)

![image 213](<2014-evra-mixing-properties-chromatic-number_images/imageFile213.png>)

![image 214](<2014-evra-mixing-properties-chromatic-number_images/imageFile214.png>)

λ˜i = NNt L2

0(Vi) ≤

![image 215](<2014-evra-mixing-properties-chromatic-number_images/imageFile215.png>)

q q + 1

1 q + 1

+

H(−1,0,...,0,1) L2

0(Vi),

![image 216](<2014-evra-mixing-properties-chromatic-number_images/imageFile216.png>)

![image 217](<2014-evra-mixing-properties-chromatic-number_images/imageFile217.png>)

0(Vi) ≤ ρW(π(−1,0,...,0,1)).

and, by Corollary 4.4, H(−1,0,...,0,1) L2

![image 218](<2014-evra-mixing-properties-chromatic-number_images/imageFile218.png>)

![image 219](<2014-evra-mixing-properties-chromatic-number_images/imageFile219.png>)

![image 220](<2014-evra-mixing-properties-chromatic-number_images/imageFile220.png>)

![image 221](<2014-evra-mixing-properties-chromatic-number_images/imageFile221.png>)

- 4.4 Proof of the mixing Lemma


The following result by Oh, gives a uniﬁed bound on the matrix coeﬃcients of a unitary representation of a reductive group over a local ﬁeld.

Theorem 4.7. [Oh, Theorem 1.1] Let F be a local non-archimedean ﬁeld with char(F) = 2. Let G be the group of the F-rational points of an F-split connected reductive group of rank ≥ 2 and G/Z(G) almost F-simple. Let G+ be the the subgroup of G generated by the unipotent elements of G.

Let Φ be a root system of G with regard to some maximal torus T, and Φ+ the set of positive roots in Φ. Let S ⊂ Φ= be a strongly orthogonal system of roots, which, by deﬁnition, means ∀α,β ∈ S ⇒ α ± β  ∈ S.

Let K be a good maximal compact subgroup of G, which means that K is a stabilizer of a special vertex in the building of G. Any good maximal compact subgroup gives rise to a Cartan decomposition G = KΛ+K, where Λ+ is a positive Weyl chamber.

Then for any unitary representation ρ of G without a non-zero G+-invariant vectors, and for any K-ﬁnite unit vectors v and u,

- 1

![image 222](<2014-evra-mixing-properties-chromatic-number_images/imageFile222.png>)

- 2ξS(λ) (4.10)


| ρ(g)v,u | ≤ (dim(Kv)dim(Ku))

α(λ) 0 0 1

where g = k1λk2 ∈ KΛ+K = G, ξS(λ) = α∈S ΞPGL

and ΞPGL

2(F)

2(F) is the Harish-chandra Ξ-function of PGL2(F).

In our case, G = PGLd(F) satisﬁes the assumptions of Theorem 4.7 and G+ is equal to PSLd(F). The subgroup K is the stabilizer of the fundamental lattice, hence K is a good maximal compact subgroup. As a maximal torus T, we take the subgroup of diagonal matrices, and as strongly orthogonal system we take the singelton S = {α := ad − a1}, α(diag(πa

d−a1, where b1,...,bd ∈ O∗.

b1,...,πa

bd)) := πa

d

1

Using the following formula (see [Oh, Section 3.8]), for n ∈ N,

π±n 0 0 1

n(q − 1) + q + 1

q + 1 ≤ (n + 1)q−n/2 (4.11) We get the following application of Oh’s theorem, when this time G =

= q−n/2

ΞPGL

2(F)

![image 223](<2014-evra-mixing-properties-chromatic-number_images/imageFile223.png>)

PGLd(F):

- Corollary 4.8. Deﬁne (ρ,L2(Γ\G)) to be the G-representation given by right translation ρ(g)f(x) = f(xg). Let f,f′ ∈ L2(Γ\G) be K-invariant unit vectors


which are orthogonal to all G+-invariant vectors. Then for g = π(a

1,...,ad),

ad−a1

| ρ(g)f,f′ | ≤ (ad − a1 + 1)q−

2 . (4.12)

![image 224](<2014-evra-mixing-properties-chromatic-number_images/imageFile224.png>)

Combining all these estimates together with Corollary 3.7, we can prove the colorful mixing lemma. Proof of the colorful mixing lemma. Let λ˜i = λ˜(Bi) be the normalized second largest eigenvalue of the bipartite graph Bi. By Corollary 4.6

![image 225](<2014-evra-mixing-properties-chromatic-number_images/imageFile225.png>)

λ˜i ≤ q−1 + ρW(π(−1,0,...,0,1)) By Corollary 4.8 in the notation of Corollary 4.6 we have ρW(π(−1,0,...,0,1)) ≤ 3q−1

Combining these together, we get that for any type i,

2 q1/2

λ˜(Bi) ≤

.

![image 226](<2014-evra-mixing-properties-chromatic-number_images/imageFile226.png>)

Finally, by Corollary 3.7, for any choice of sets Wi ⊂ Vi,i = 1,...,d,

2d q1/2

λ˜(Bi) ≤

discΓ\B(W1,...,Wd) ≤ d · max

,

![image 227](<2014-evra-mixing-properties-chromatic-number_images/imageFile227.png>)

i

which proves the claim.

![image 228](<2014-evra-mixing-properties-chromatic-number_images/imageFile228.png>)

![image 229](<2014-evra-mixing-properties-chromatic-number_images/imageFile229.png>)

![image 230](<2014-evra-mixing-properties-chromatic-number_images/imageFile230.png>)

![image 231](<2014-evra-mixing-properties-chromatic-number_images/imageFile231.png>)

# 5 Explicit construction of Ramanujan complexes

Ramanujan complexes were introduced in [Li], [LSV1] and [Sar] as a generalization of the Ramanujan graphs constructed in [LPS], and were explicitly constructed in [LSV2]. These complexes are certain quotients of the Bruhat-Tits buildings.

The heart of the construction in [LSV2] is the Cartwright-Steger lattice (CSlattice) Λ [CS], which allows us to view some of the quotients of the building as Cayley complexes of ﬁnite groups with explicit sets of generators.

The reader is referred to [LSV1, LSV2] for more details, and to [Lu2] for a reader friendly survey.

- 5.1 The Cartwright-Steger lattice


Here we present the CS-lattice, and express explicitly its set of generators.

Let Fq be the ﬁnite ﬁeld of size q, and Fqd the ﬁeld extension of Fq of degree d. Let φ be a generator of the Galois group Gal(Fqd/Fq) ∼= Z/dZ, and ﬁx a basis ξ0,...,ξd−1 of Fqd over Fq with ξi = φi(ξ0). Denote RT = Fq[y, 1+1y]. For a given RT-algebra S (i.e. S is given with a ring homomorphism RT → S), we deﬁne a S-algebra A(S) = di,j−=01 Sξizj with the relations zd = 1 + y and zξi = φ(ξi)z. One can see that the center of A(S) is S, and A(S)∗/S∗ is a group scheme for RT-algebras.

![image 232](<2014-evra-mixing-properties-chromatic-number_images/imageFile232.png>)

Let k = Fq(y). Then A(k) is a k-central simple algebra. For almost all completions kν of k, A(kν) splits, i.e. A(kν) ∼= Md(kν). In fact, this happens for all completions except for ν1

,

and ν1+y. In particular, for F = Fq((y)) = kν

y

![image 233](<2014-evra-mixing-properties-chromatic-number_images/imageFile233.png>)

y

the algebra splits and A(F)∗/F∗ ∼= PGLd(F) (see [LSV2, Proposition 3.1]). On the other hand, for ν = ν1

or ν1+y, A(kν) is a division algebra and A(kν)∗/kν∗ is compact. Thus Fq[y1,y, 1+1y] ֒→ kν

![image 234](<2014-evra-mixing-properties-chromatic-number_images/imageFile234.png>)

y

×kν

y ×kν

is discrete and by substituting

![image 235](<2014-evra-mixing-properties-chromatic-number_images/imageFile235.png>)

![image 236](<2014-evra-mixing-properties-chromatic-number_images/imageFile236.png>)

1+y

1 y

![image 237](<2014-evra-mixing-properties-chromatic-number_images/imageFile237.png>)

these rings in A(−)∗/(−)∗ and projecting to the ﬁrst coordinate A(F)∗/F∗ ∼= PGLd(F) we get a discrete subgroup, which is an arithmetic lattice.

Denote R = Fq[y, y1, 1+1y]. As 1 + y is invertible in RT, z is invertible in A(RT), since it divides zd = 1 + y. Denote b = 1 − z−1 ∈ A(RT). Since y is invertible in R, so is 1+yy, and hence b is invertible in A(R), since it divides 1 − z−d = 1+yy. For an element u ∈ F∗qd ⊂ A(R), denote bu = ubu−1 and note that as Fq ⊂ R is in the center of A(R), bu depends only on the coset u ∈ F∗qd/F∗q. Deﬁne Σ1 = {¯bu |u ∈ F∗

![image 238](<2014-evra-mixing-properties-chromatic-number_images/imageFile238.png>)

![image 239](<2014-evra-mixing-properties-chromatic-number_images/imageFile239.png>)

![image 240](<2014-evra-mixing-properties-chromatic-number_images/imageFile240.png>)

![image 241](<2014-evra-mixing-properties-chromatic-number_images/imageFile241.png>)

q} ⊂ A(R)∗/R∗ ⊂ A(F)∗/F∗ ∼= PGLd(F) where

qd/F∗

- F = Fq((y)). The Cartwright-Steger lattice is Λ = Σ1 . This is the promised


CS-lattice which acts simply transitively on the vertices of the building B = Bd(Fq((y))) (see [CS] and [LSV2, Proposition 4.8]).

More explicitly, let x0 = [Od] be the vertex of the building corresponding to the standard lattice, and let τ : B → Z/dZ be the type function on the building. Then for each neighboring vertex x of x0 with τ(x) = 1, there exists a unique bu ∈ Σ1 such that bu · x0 = x. Now, for i = 2,...,d − 1 denote Ni = {x ∈ V (B)| x ∼ x0 and τ(x) = i}. For every x ∈ Ni, there is a unique γx ∈ Λ with γx.x0 = x. Let Σi = {γx|x ∈ Ni}, so Σi.x0 = Ni. Let Σ = ∪di=1−1Σi. Then Σ.x0 is the set of all the neighbors of x0, and we can identify the 1-skeleton of the building with the Cayley graph Cay(Λ,Σ). Note that as Λ acts simply transitively, |Σi| = di q and hence |Σ| = di=1−1 di q, where di q is the number of i-dimensional subspaces of a d-dimensional vector space over Fq.

Recall that a clique in a graph is a set of vertices such that each pair of them is connected by an edge, and the clique complex of a graph is deﬁned to be the collection of the cliques in the graph. The clique complex of a Cayley graph is called a Cayley complex. The building B and its quotients with injectivity radius ≥ 2 are clique complexes, hence completely determined by their 1-skeleton.

We can conclude that if Γ ⊳ Λ, the complex Γ\B is the Cayley complex Cay(Λ/Γ,Σ) of the quotient group Λ/Γ w.r.t. the set of generators Σ. In the next subsection we will apply this in the case where Γ is a normal congruence subgroup of Λ.

- 5.2 Congruence subgroups


Ramanujan complexes are obtained in [LSV2] by dividing the building modulo the action of congruence subgroups of some arithmetic cocompact lattices, such as Λ above. Here we deﬁne the congruence subgroups of Λ and display their quotients as Cayley complexes of some ﬁnite groups.

For an ideal 0 = I ⊳ R, deﬁne the congruence subgroup of Λ to be Λ(I) = Λ ∩ ker(A(R)∗/R∗ → A(R/I)∗/(R/I)∗). This congruence subgroup is a ﬁnite index normal subgroup of Λ. Hence the quotient Λ(I)\B is a ﬁnite simplicial complex, which we will identify with the Cayley complex of the group Λ/Λ(I) (w.r.t. Σ as the set of generators). By [LSV2, Theorem 6.2] for any 0 = I ⊳ R, Λ/Λ(I) is a Ramanujan complex (though, in this paper, we are not really using this deep fact).

By [LSV2, Theorem 6.6], the group Λ/Λ(I) can be identiﬁed as a subgroup of PGLd(R/I) which contains PSLd(R/I). As R = Fq[y, y1, 1+1y], we consider I = (f) where f ∈ Fq[y] is an irreducible polynomial of degree e ≥ 2. Then R/I ∼= Fqe and hence PSLd(Fqe) ≤ Λ/Λ(f) ≤ PGLd(Fqe). Moreover, by [LSV2, Theorem 7.1], (assuming qe > 4d2 + 1), for any subgroup PSLd(Fqe) ≤

![image 242](<2014-evra-mixing-properties-chromatic-number_images/imageFile242.png>)

![image 243](<2014-evra-mixing-properties-chromatic-number_images/imageFile243.png>)

- G ≤ PGLd(Fqe), we may ﬁnd f such that G = Λ/Λ(f). In particular, G has


a set of di=1−1 di q generators such that the corresponding Cayley complex is a Ramanujan complex.

For such quotients of B by congruence subgroups, a bound on the injectivity radius was presented in [LuMe]:

Proposition 5.1. [LuMe, Proposition 3.3] Let f ∈ Fq[y] be an irreducible polynomial, Γ = Λ(f), and X = Γ\B. Denote by |X| the number of vertices of X.

Then

logq |X| (d − 1)(d2 − 1) As a consequence of this proposition, we get

deg(f) d ≥

dist(γ.x,x) ≥

dist(Γ) := min

![image 244](<2014-evra-mixing-properties-chromatic-number_images/imageFile244.png>)

![image 245](<2014-evra-mixing-properties-chromatic-number_images/imageFile245.png>)

1 =γ∈Γ,x∈B

- Corollary 5.2 (injectivity radius). Let X = Γ\B be a quotient of the building, where Γ as above. Then the injectivity radius r(X) of X satisﬁes


logq |X| 2(d − 1)(d2 − 1) −

dist(Γ) − 1 2 ⌋ ≥

- 1

![image 246](<2014-evra-mixing-properties-chromatic-number_images/imageFile246.png>)

- 2


r(X) ≥ ⌊

.

![image 247](<2014-evra-mixing-properties-chromatic-number_images/imageFile247.png>)

![image 248](<2014-evra-mixing-properties-chromatic-number_images/imageFile248.png>)

- 5.3 Partite Ramanujan complexes


Before continuing, let us examine the special case of d = 2, i.e. the Ramanujan graphs (compare with [LPS] and [Lu1]). In this case Λ/Λ(I) is a subgroup of PGL2(Fqe) containing PSL2(Fqe), and since PSL2(Fqe) is of index 2 inside PGL2(Fqe), Λ/Λ(I) is either PGL2(Fqe) or PSL2(Fqe). In this case all the elements of Σ = Σ1 either lie outside of PSL2(Fqe) or all are inside of it (which is the case iﬀ the image of b is in it, in which case all the bu, which are conjugates of b, are also there). The Cayley graph Cay(Λ/Λ(I),Σ) is bipartite in the ﬁrst case and has large chromatic number in the second. In other words, the quotient Λ/Λ(I) inherits the type function of the building (τ : B → Z/2Z) if and only if the index of PSL2(Fqe) inside Λ/Λ(I) is 2, i.e. Λ/Λ(I) = PGL2(Fqe).

In the high-dimensional case the situation is in analogy with the 1-dimensional

case (see [LSV2, Proposition 6.7, Corollary 6.8]). Assume I = (f) as before with R/I = Fqe. Then PGLd(Fqe)/PSLd(Fqe) ∼= Z/dZ. If r is the index of PSLd(R/I) in Λ/Λ(I) then r|d, and the image of Λ in Z/dZ under the map τ is drZ/dZ ∼= Z/rZ. The quotient then inherits an r-partition from the building, i.e. τ : Λ/Λ(I) → Z/rZ. In the construction above, the index r = [Λ/Λ(I) : PSLd(R/I)] is equal to the order of 1+yy inside (R/I)∗/(R/I)∗d (see [LSV2, Proposition 6.7]).

![image 249](<2014-evra-mixing-properties-chromatic-number_images/imageFile249.png>)

![image 250](<2014-evra-mixing-properties-chromatic-number_images/imageFile250.png>)

- Lemma 5.3. Let 0 = I ⊳ R and Γ = Λ(I) as above, r = [Λ/Γ : PSLd(R/I)], and consider the simplicial complex Γ\B.


- (a) Denote Γ0 = Γ ∩ G0 = {g ∈ Γ | νF(det(g)) ≡ 0 mod d} the subgroup of type-preserving elements of Γ. Then [Γ : Γ0] = dr.

![image 251](<2014-evra-mixing-properties-chromatic-number_images/imageFile251.png>)

- (b) If r = 1, then Γ0\B → Γ\B is a d-cover. Moreover, for each vertex in Γ\B, its preimage is a set of d vertices, one of each type in Z/dZ.


Proof. Let us look at the type function as a surjective homomorphism of groups τ = νF ◦ det : Λ ∼= B(0) → Z/dZ

If Λ/Γ is an extension of the simple group PSLd(qe) by a cyclic group of order r, it follows that by restricting the homomorphism, we get a surjective

homomorphism, τΓ : Γ → Z/rdZ ∼= rZ/dZ. Now, since G0 is the subgroup of type-preserving elements in G, then ker(τ|X) = X ∩ G0. So by the First Isomorphism Theorem we have

![image 252](<2014-evra-mixing-properties-chromatic-number_images/imageFile252.png>)

d r

Γ/Γ0 = Γ/ ker(τΓ) ∼= τ(Γ) ∼= Z/

Z.

![image 253](<2014-evra-mixing-properties-chromatic-number_images/imageFile253.png>)

This proves (a). To prove (b) we argue as follows:

Since r = 1 then by (a) we have that [Γ : Γ0] = d. Let γ1,...,γd be representatives of Γ0-cosets. Since Γ0 = ker(νF ◦ det|Γ) all the d types are obtained, then after renumbering, for each i ∈ Z/dZ, νF ◦ det(γi) = i. Also, for any Γx ∈ Γ\B, its preimages are Γ0γ1x,...,Γ0γdx, and their types are 1 + τ(x),... ,d + τ(x), which give all d types in Z/dZ.

![image 254](<2014-evra-mixing-properties-chromatic-number_images/imageFile254.png>)

![image 255](<2014-evra-mixing-properties-chromatic-number_images/imageFile255.png>)

![image 256](<2014-evra-mixing-properties-chromatic-number_images/imageFile256.png>)

![image 257](<2014-evra-mixing-properties-chromatic-number_images/imageFile257.png>)

When r = 1, we say that Γ\B is non-partite. In order to ﬁnd such Ramanujan complexes we proceed as follows. Choose some β ∈ F∗qe such that βd = 1 and that α = β

d

1−βd generates the ﬁeld Fqe. By Lemma 7.2 and the proof of Proposition 7.3 in [LSV2], if qe ≥ 4d2 + 1 there exists such β. Now, let f ∈ Fq[y] be the minimal polynomial of α. Then f is of degree e, and under the identiﬁcation R/(f) ∼= Fqe, y ←→ α = β

![image 258](<2014-evra-mixing-properties-chromatic-number_images/imageFile258.png>)

d

1−βd and 1+yy ←→ βd. Therefore

![image 259](<2014-evra-mixing-properties-chromatic-number_images/imageFile259.png>)

![image 260](<2014-evra-mixing-properties-chromatic-number_images/imageFile260.png>)

y 1+y ∈ (R/I)∗d, and by the discussion above Λ/Γ = PSLd(Fqe) and the Cayley complex of Λ/Γ is non-partite.

![image 261](<2014-evra-mixing-properties-chromatic-number_images/imageFile261.png>)

The above may be summarized by the following proposition, which is a special case of [LSV2, Theorem 7.1] together with Lemma 5.3.

Proposition 5.4. Let q be a prime power, d ≥ 2, e ≥ 2 such that qe ≥ 4d2 +1. Let Λ be the Cartwright-Steger lattice in PGLd(Fq((y))). For an irreducible polynomial f ∈ Fq[y], let Γ = Λ(f) ⊳ Λ be its congruence subgroup, and let Γ0 = Γ ∩ G0 be the ﬁnite index subgroup of type-preserving elements in Γ.

Then there exists an irreducible polynomial f ∈ Fq[y] of degree e, such that:

- 1. The Cayley complex X = Cay(Λ/Γ,Σ) is a non-partite Ramanujan complex.
- 2. The Cayley complex X˜ = Cay(Λ/Γ0,Σ) is a d-partite Ramanujan complex.
- 3. The complex X˜ is a d-cover of X, and the preimage in X˜ of each vertex in X is a set of d vertices of all d types.


- Remark 5.5. A polynomial f(y) of degree e can be also considered as a poly-


nomial of degree e in y1, by multiplying it by y1e, which is an invertible element in R.

![image 262](<2014-evra-mixing-properties-chromatic-number_images/imageFile262.png>)

![image 263](<2014-evra-mixing-properties-chromatic-number_images/imageFile263.png>)

# 6 Proof of the main theorem

We are now ready to prove the following theorem which implies Theorem 1.2.

Theorem 6.1. Let d ≥ 3 and q an odd prime power, and let X be a nonpartite Ramanujan complex as constructed in Proposition 5.4. Let χ(X) and r(X) be the chromatic number and injectivity radius of X (as deﬁned in the introduction). Then

logq |X| 2(d − 1)(d2 − 1) −

- 1

![image 264](<2014-evra-mixing-properties-chromatic-number_images/imageFile264.png>)

- 2


r(X) ≥

(6.1) and, assuming r(X) ≥ 2,

![image 265](<2014-evra-mixing-properties-chromatic-number_images/imageFile265.png>)

- 1

![image 266](<2014-evra-mixing-properties-chromatic-number_images/imageFile266.png>)

- 2 · q1/2d (6.2)


χ(X) ≥

Proof. The claim about the injectivity radius is Corollary 5.2. For the chromatic number: Consider a coloring of X with χ(X) colors, and let W be the set of

vertices of X of the most common color, so |W| ≥ |Vχ((XX))|. Let X be the d-cover of X with the type-function inherited from building, as in Proposition 5.4. For

![image 267](<2014-evra-mixing-properties-chromatic-number_images/imageFile267.png>)

each i ∈ Z/dZ, let Wi be the preimage of W of vertices of type i in X, so |Wi| = |W|.

Note that the image of each j-dimensional simplex e˜ in X is again an jdimensional simplex e in X. Indeed, as the injectivity radius is ≥ 2 and each simplex is a clique, so any two vertices in e˜ are of distance 1, hence are not mapped to the same vertex in X.

In particular, each d-dimensional simplex in X, with one vertex in each Wi, is mapped to a d-dimensional simplex in X, with all the vertices in W. But by the deﬁnition of the chromatic number there are no such simplices in X with all vertices in W, and therefore E(W1,...,Wd) = ∅.

Denote by Vi the set of vertices of type i in X, then |Vi| = |V (X)| for all

|Vi| = |V|W(X|)| ≥ χ(1X). Since E(W1,...,Wd) = ∅, we get

- i = 1,...,d. Therefore |W


i|

![image 268](<2014-evra-mixing-properties-chromatic-number_images/imageFile268.png>)

![image 269](<2014-evra-mixing-properties-chromatic-number_images/imageFile269.png>)

![image 270](<2014-evra-mixing-properties-chromatic-number_images/imageFile270.png>)

d

disc X(W1,...,Wd) =

i=1

|Wi| |Vi|

1 χ(X)d

≥

.

![image 271](<2014-evra-mixing-properties-chromatic-number_images/imageFile271.png>)

![image 272](<2014-evra-mixing-properties-chromatic-number_images/imageFile272.png>)

On the other hand, by the Colorful Mixing Lemma, we have

2d q1/2

disc X(W1,...,Wd) ≤

.

![image 273](<2014-evra-mixing-properties-chromatic-number_images/imageFile273.png>)

Combining these together we get

1 d

χ(X) ≥ (2d)−

![image 274](<2014-evra-mixing-properties-chromatic-number_images/imageFile274.png>)

· q

- 1

![image 275](<2014-evra-mixing-properties-chromatic-number_images/imageFile275.png>)

- 2 · q


- 1

![image 276](<2014-evra-mixing-properties-chromatic-number_images/imageFile276.png>)

- 2d


- 1

![image 277](<2014-evra-mixing-properties-chromatic-number_images/imageFile277.png>)

- 2d .


≥

![image 278](<2014-evra-mixing-properties-chromatic-number_images/imageFile278.png>)

![image 279](<2014-evra-mixing-properties-chromatic-number_images/imageFile279.png>)

![image 280](<2014-evra-mixing-properties-chromatic-number_images/imageFile280.png>)

![image 281](<2014-evra-mixing-properties-chromatic-number_images/imageFile281.png>)

- Remark 6.2. The complexes in Theorem 6.1 are non-partite. It follows therefore that for their 1-skeletons, the largest eigenvalue of their adjacency matrices


2/8 (see [Lu2, remark 2.1.5]). It follows from [C, Theorem 1] that diam(X) ≤ log(logλ|X|

2/4 where the second one λ2 is at most ddqd

is k ≈ qd

1/λ2), so

![image 282](<2014-evra-mixing-properties-chromatic-number_images/imageFile282.png>)

4 logq |Xn| d2 ≤ 8d · r(Xn)

logq |Xn| logq(d k

logq |Xn| d2/4 − dlogq d ≈

diam(Xn) ≤

dqd2/8) ≈

![image 283](<2014-evra-mixing-properties-chromatic-number_images/imageFile283.png>)

![image 284](<2014-evra-mixing-properties-chromatic-number_images/imageFile284.png>)

![image 285](<2014-evra-mixing-properties-chromatic-number_images/imageFile285.png>)

![image 286](<2014-evra-mixing-properties-chromatic-number_images/imageFile286.png>)

for q ≫ d. So, up to a constant fraction of their diameters, these complexes are two colorable around every vertex.

Remark 6.3. Theorems 6.1 and 1.2 are true also if q is even or if d = 2. In this case one should use the full power of the Ramanujan bounds. For the cases we treated here, Oh’s theorem suﬃces.

# References

[BAV] R. Ben Ari, U. Vishne, Homology of 2-dimensional complexes and internal partitions, preprint.

[CS] D. Cartwright, T. Steger, A Family of An-groups, Israel Journal of Mathematics, 103 (1988) 125-140.

[C] F.R.K. Chung, Diameters and eigenvalues, Journal of the American Mathematical Society, 2(2) (1989) 187-196 .

[E] P. Erdo˝s, Graph theory and probability, Canadian Journal of Mathematics, 11 (1959) 34-38.

[EH] P. Erdo˝s, A. Hajnal, On chromatic number of graphs and set-systems, Acta Math. Acad. Sci. Hungar. 17 (1966), 61-99.

[FGLNP] J. Fox, M. Gromov, V. Laﬀorgue, A. Naor and J. Pach, Overlap properties of geometric expanders, Journal fur die reine und angewandte Mathematik (Crelle’s Journal), 671 (2012) 49-83.

- [G1] M. Goﬀ, Higher dimensional Moore bounds, Graphs and Combinatorics, 27 (2011) 505-530.
- [G2] M. Goﬀ, Simplicial girth and pure resolutions, Graphs and Combinatorics, 29 (2011) 225-240.


[GuLu] L. Guth, A. Lubotzky, Quantum error-correcting codes and 4dimensional arithmetic hyperbolic manifolds, J. of Mathematical physics, to appear. arXiv:1310.5555 (2013).

[Li] W.C.W. Li, Ramanujan hypergraphs, Geometric and Functional Analysis, 14(2) (2004) 380-399.

[Lo] L. Lov´asz, On chromatic number of ﬁnite set-systems, Acta Mathematica Hungarica, 19 (1968) 59-67.

[Lu1] A. Lubotzky, Discrete Groups, Expanding Graphs and Invariant Mea-

sures, Progress in Mathematics, Birkhuser Verlag, Basel, 125 (1994). [Lu2] A. Lubotzky, Ramanujan complexes and high dimensional expanders,

Japanese Journal of Mathematics, to appear. arXiv:1301.1028,

(2013). [LuMe] A. Lubotzky, R. Meshulam, A Moore bound for simplicial complexes, Bulletin of the London Mathematical Society, 39 (2007) 353-358. [LPS] A. Lubotzky, R. Philips, P. Sarnak, Ramanujan graphs, Combinatorica, 8(3) (1988) 261-277. [LSV1] A. Lubotzky, B. Samuels, U. Vishne, Ramanujan complexses of type Ad, Israel Journal of Mathematics, 149 (2005) 267-300. [LSV2] A. Lubotzky, B. Samuels, U. Vishne, Explicit construction of Ra-

manujan complexes of type Ad, European Journal of Combinatorics, 26(6) (2005) 965-993.

[N] J. Nesetril, A combinatorial classic - sparse graphs with high chromatic number, Erdo˝s Centennial Bolyai Society Mathematical Studies 25, (2013) 383-407.

[Oh] H. Oh, Uniform pointwise bounds for matrix coeﬃcients of unitary representations and applications to Kazhdan constants, Duke Mathematical Journal, 113(1) (2002) 133-192.

## [Sar] A. Sarveniazi, Ramunajan (n1,n2,...,nd−1)-regular hypergraphs based on Bruhat-Tits buildings of type A˜d, Duke Mathematical Journal, 139(1) (2007) 141-171.

