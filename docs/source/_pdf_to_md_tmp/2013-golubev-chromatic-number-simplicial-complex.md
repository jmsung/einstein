arXiv:1306.4818v2[math.CO]17Nov2015

# On the chromatic number of a simplicial complex1

Konstantin Golubev 2

Department of Mathematics, The Hebrew University of Jerusalem Givat Ram, Jerusalem 91904, Israel.

### March 4, 2018

Abstract

In [Ho] A.J. Hoﬀman proved a lower bound on the chromatic number of a graph in the terms of the largest and the smallest eigenvalues of its adjacency matrix. In this paper, we prove a higher dimensional version of this result and give a lower bound on the chromatic number of a pure d-dimensional simplicial complex in the terms of the spectra of the higher Laplacian operators.

## 1 Introduction

The chromatic number of a graph is the minimal number of colors needed to color its vertices in such a way that no edge is monochromatic. It has been studied extensively by diﬀerent methods. One of them is the spectral method, i.e. bounding the chromatic number by means of the spectra of various operators deﬁned on the graph. For example, an upper bound was given by H.S. Wilf, [Wi], and a lower bound by A.J. Hoﬀman, [Ho]. See also [WE] by P. Wocjan and C. Elphick, which contains a generalization of the latter bound as well as an exposition of the known results in the area. An advantage of the spectral method is that the spectrum of an operator

![image 1](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile1.png>)

- 1This work is a part of the Ph.D. thesis being written at the Hebrew University of Jerusalem, Israel.
- 2E-mail: kost.golubev@mail.huji.ac.il


on a ﬁnite graph can be calculated in polynomial time, while the problem of ﬁnding the chromatic number of a graph is NP-complete.

One operator is the Laplacian of a graph. Given a graph G the Laplacian ∆ of G is an operator on the space C0 of the real-valued functions on the vertex set V of G. On a function f ∈ C0 it acts as

∆f(v) = deg v · f(v) −

f(u) =

u∼v

(f(v) − f(u)),

u∼v

where v ∈ V , deg v is the number of edges adjacent to v, and u ∼ v stands for the vertices u and v being connected by an edge in G.

The chromatic number χ(G) of the graph G is connected to its independence number α(G). The independence number α(G) of the graph G is the cardinality of the largest subset of vertices, such that no two vertices of this subset are connected by an edge. Then α(G)χ(G) ≥ n, where n is the cardinality of the vertex set of G.

In 1970, A.J. Hoﬀman gave a lower bound on the chromatic number in the terms of the eigenvalues of the adjacency matrix of the graph. Here we give a version of it in the terms of the Laplacian.

- Theorem 1.1. (A.J. Hoﬀman, 1970, [Ho]) For a nonempty graph G on n vertices,


µ − k µ · n, and hence, χ(G) ≥

µ µ − k

α(G) ≤

,

![image 2](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile2.png>)

![image 3](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile3.png>)

where α(G) is the independence number of G, χ(G) is the chromatic number of G, k is the minimal degree of a vertex of G and µ is the largest eigenvalue of the Laplacian ∆ on G.

Proof. Let A ⊂ V be the largest independent subset of V , and B = V \ A be its complement. Note that both A and B are nonempty, since the graph G is nonempty. Consider the following function f ∈ C0 on the vertex set V

f(v) = −|B|, if v ∈ A;

|A|, if v ∈ B. Then

|A| · k · (|A| + |B|)2 |A| · |B|2 + |B| · |A|2

∆f, f f, f ≥

k · n n − |A|

µ ≥

=

, and hence

![image 4](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile4.png>)

![image 5](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile5.png>)

![image 6](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile6.png>)

µ − k

µ · n. Since χ(G)α(G) ≥ n, the second bound follows.

|A| = α(G) ≤

![image 7](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile7.png>)

![image 8](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile8.png>)

![image 9](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile9.png>)

![image 10](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile10.png>)

![image 11](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile11.png>)

An important application of the Hoﬀman bound is given in [LPS], where non-bi-partite Ramanujan graphs are constructed. These graphs are regular, i.e. all vertices have the same degree, and are shown there to have chromatic number of order √k, where k is the degree of regularity, and girth greater or equal to 34 logk−1 n, where n is the number of vertices. Thus, an explicit construction of graphs of arbitrarily large girth and arbitrarily large chromatic number was given.

![image 12](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile12.png>)

![image 13](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile13.png>)

Hoﬀman’s theorem also serves as a powerful tool in extremal combinatorics. For example, in [Lo] L. Lova´sz reproved the Erd˝os-Ko-Rado theorem on the maximum size of a uniform family of intersecting sets by showing that the Hoﬀman bound is sharp for the corresponding Kneser graph. Another example is a diﬀerent proof of the Deza-Frankl theorem on the number of intersecting permutations of n elements. In [DF], by purely combinatorial considerations M. Deza and P. Frankl proved that the largest set of intersecting permutations is of size (n − 1)!. The work [Re] of P. Renteln, where the largest eigenvalue of the Laplacian of the derangement graph was computed, implies via the Hoﬀman theorem a sharp bound on its independence number, thus reproving the Deza-Frankl theorem.

In this paper we present a generalization of the Hoﬀman result to higher dimensions. As a generalization of the notion of a ﬁnite graph we take a ﬁnite pure d-dimensional abstract simplicial complex. That is a family X of subsets a ﬁnite vertex set V closed under taking subsets, such that every maximal subset in the family is of size d + 1. The elements of X are called faces. The dimension of a face is its cardinality minus one. By the degree of a j-face we mean the number of (j + 1)-faces containing it.

The chromatic number χ(X) of a simplicial complex X is the least number of colors needed to color its vertices in such a way that no maximal face is monochromatic. This is also known as the weak chromatic number of a complex. The independence number α(X) of a simplicial complex X is the size of the largest subset of vertices such that no maximal face of the complex has all its vetices in this subset. As in the case of graphs, α(X)χ(X) ≥ |V |, where V is the vertex set of the complex.

The Laplacian operators for simplicial complexes were introduced by B. Eckmann in [Ec] generalizing the above deﬁnition for graphs. The reader is referred to Section 2 for precise deﬁnitions.

The main result of this paper is the following theorem.

- Theorem 1.2. Let X be a nonempty pure d-dimensional simplicial complex on a ﬁnite vertex set V of size n. Then


µ0 . . .µd−1 − (k0 + 1)(k1 + 2) . . .(kd−2 + d − 1)kd−1 µ0 . . .µd−1 · n,

α(X) ≤

![image 14](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile14.png>)

and hence, χ(X) ≥

µ0 . . .µd−1 µ0 . . .µd−1 − (k0 + 1)(k1 + 2) . . .(kd−2 + d − 1)kd−1

,

![image 15](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile15.png>)

where χ(X) is the chromatic number of X, and for 0 ≤ j ≤ d − 1, kj is the minimal degree of a j-face of X, and µj is the largest eigenvalue of the j-th upper Laplacian operator ∆+j of X.

We note that in the one-dimensional case, when a simplicial complex is

just a graph, the upper Laplacian operator ∆+0 coincides with the Laplacian operator ∆ of a graph deﬁned earlier, and that Theorem 1.1 is a special case of Theorem 1.2.

In Section 3, we prove the main result. In Section 4, we formulate a version of Theorem 1.2 for the case of a pure d-dimensional simplicial complex with a complete (d − 1)-skeleton and give a diﬀerent, shorter, proof.

## 2 Notations and deﬁnitions

An abstract simplicial complex X on a ﬁnite vertex set V is a collection of subsets of V closed under taking subsets. Elements of X are called faces of the complex.

The dimension of a face τ ∈ X is its cardinality minus one, dim(τ) = |τ| − 1. A face of dimension j is called a j-face. The set of all j-faces of X is denoted Xj, in particular, X0 = V . The dimension of a complex, dim(X), is the largest dimension of its face. A d-dimensional complex is called pure, if all the maximal faces are of dimension d.

By X(j) we denote the set of all faces of dimension at most j. It is a j-dimensional simplicial complex by itself and it is called the j-skeleton of X.

The degree of a j-face τ ∈ Xj is the number of (j + 1)-faces containing it, i.e. deg(τ) = |{σ ∈ Xj+1 | τ ⊂ σ}|.

For a subset A ⊆ V , we denote the set of j-faces with all its vertices in

- A by Xj(A) = {v0, . . ., vj} ∈ Xj | vl ∈ A, for all l = 0, . . ., j .


For a j-face τ ∈ Xj and disjoint subsets A1, . . ., Am ⊆ V denote the set of all (j + m)-faces containing τ and having exactly one vertex in each of A1, . . ., Am by

Xj+m(τ, A1, . . ., Am) = τ ∪ {v1, . . ., vm} ∈ Xj+m | ∀1 ≤ i ≤ m : vi ∈ Ai .

Chromatic and independence numbers A subset A ⊆ V of vertices of a simplicial complex X is called independent, if there is no maximal face of X with all vertices in A. The independence number α(X) of a complex X is the size of the largest independent set of vertices.

The chromatic number χ(X) of a complex X is the least integer χ such that vertices of X can be partitioned into χ disjoint independent sets. Note that |V | ≤ α(X) · χ(X).

In other words, the chromatic number of a simplicial complex X is the least number of colors needed to color the vertices of X is such a way that no maximal face of X is monochoromatic, i.e. no maximal face has all its vertices colored in one color. It is also known as the weak chromatic number of X, while the chromatic number of the underlying graph X(1) of X, denoted χ(X(1)), is known as the strong chromatic number of X. Clearly, χ(X) ≤ χ(X(1)). In fact, a stronger inequality holds.

Proposition 2.1. For a d-dimensional complex X

χ(X) ≤

χ(X(1)) d

![image 16](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile16.png>)

,

where ⌈·⌉ denotes the ceiling function.

1(X)

Proof. Let χ1 = χ(X(1)), m = χ

d , and χd = χ(X). Let V = A1 ⊔ · · · ⊔ Aχ

![image 17](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile17.png>)

be a proper 1-coloring of X in χ1 colors, i.e. there is no edge with both endpoints in Aj for all 1 ≤ j ≤ χ1.

1

Let B1 = A1 ⊔ · · · ⊔ Ad, B2 = Ad+1 ⊔ · · · ⊔ A2d, . . ., Bm = A(m−1)·d+1 ⊔ · · · ⊔ Aχ

.

1

Since for 1 ≤ j ≤ χ1, Aj contains no 1-face of X, Bi contains no d-face of X for all 1 ≤ i ≤ m, and therefore, χd ≤ m.

![image 18](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile18.png>)

![image 19](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile19.png>)

![image 20](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile20.png>)

![image 21](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile21.png>)

Laplacian operators A j-face A ∈ Xj with an ordering of its vertices is called oriented and denoted [A]. For 0 ≤ j ≤ d, denote by Cj = Cj(X, R) the vector space of all real-valued antisymmetric functions on oriented j-faces of the complex X. That is, for a function f ∈ Cj, a j-face F = {v0, . . ., vj} ∈ Xj and a permutation π ∈ Sj+1 the following equality holds

f([vπ(0), . . ., vπ(j)]) = sgn(π)f([v0, . . ., vj]). An inner product on Cj is deﬁned as

f, g =

f([A])g([A]).

A∈Xj

Note that the sum runs over the non-oriented j-faces of X, but the functions are evaluated on oriented ones. Since the functions f and g are antisymmetric, an orientation of each face may be chosen arbitrarily, and f, g is well-deﬁned.

For 0 ≤ j ≤ d − 1, the j-th coboundary map δj : Cj → Cj+1 is deﬁned as

j+1

(−1)if([v0, . . ., vi, . . ., vj+1]).

(δjf)([v0, . . ., vj+1]) =

i=0

Note that this deﬁnes a cochain complex, i.e. δj+1 ◦ δj = 0. For 0 ≤ j ≤ d − 1, the j-th boundary map ∂j : Cj+1 → Cj is deﬁned as

f([u, v0, . . ., vj]).

(∂jf)([v0, . . ., vj]) =

u∈V : {u,v0,...,vj}∈Xj+1

The j-th boundary map is the adjoint of the j-th coboundary map.

The following operator on Cj is called the upper j-th Laplacian of the complex:

∆+j = ∂j ◦ δj.

Remark 2.2. One can also consider the lower j-th Laplacian deﬁned as ∆−j = δj−1 ◦ ∂j−1, and the j-th Laplacian deﬁned as the sum of the upper and the lower ones. Both lower and upper Laplacians are postitve semideﬁnite. The spectrum of (j + 1)-th lower Laplacian coincides with the spectrum of j-th upper Laplacian up to the multiplicity of the zero eigenvalue.

Note that in the case of graphs, the upper Laplacian operator on C0 of a graph coincides with the Laplacian operator deﬁned earlier in the introduction

For an exposition of theory of Laplacian operators of an abstract simplicial complex, we address the reader to [HJ] and the references therein.

In this paper we deal with the largest eigenvalue of the upper Laplacian

operators. For 0 ≤ j ≤ d − 1, we denote the largest eigenvalue of ∆+j (X) by µj = µj(X). In [HJ, Theorem 3.4], a lower bound for the largest eigenvalue of the Laplacian of a complex is provided.

Theorem 2.3. (D. Horak, J. Jost, 2011, [HJ], Theorem 3.4) Let X be a pure d-dimensional simplicial complex. Then for each 0 ≤ j ≤ d − 1,

Kj + (j + 1) ≤ µj,

where Kj is the maximal degree of a j-face and µj is the largest eigenvalue of the j-th upper Laplacian operator ∆+j of X.

## 3 Proof of the Main Theorem

In this section we prove Theorem 1.2. Let X be a nonempty pure d-dimensional simplicial complex on a ﬁnite vertex set V . Then

µ0 . . .µd−1 − (k0 + 1) . . .(kd−2 + d − 1)kd−1

α(X) ≤

µ0 . . .µd−1 · n, and hence,

![image 22](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile22.png>)

µ0 . . .µd−1 µ0 . . .µd−1 − (k0 + 1) . . .(kd−2 + d − 1)kd−1

χ(X) ≥

,

![image 23](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile23.png>)

where for 0 ≤ j ≤ d − 1, kj is the minimal degree of a j-face of X, and µj is the largest eigenvalue of the j-th upper Laplacian operator ∆+j of X.

The proof of this theorem is mainly based on the following lemma.

Lemma 3.1. Let X be a nonempty pure d-dimensional simplicial complex on a ﬁnite vertex set V . For 0 ≤ i ≤ d − 1, denote by ki the minimal degree of an i-face of X. Let 0 ≤ j ≤ d−2, A ⊆ V a subset of vertices, B = V \A, and 0 < β ≤ kj+1 be a constant such that for each (j + 1)-cell τ which has all its vertices in A, i.e. τ ∈ Xj+1(A), the following inequality holds

|Xj+2(τ, B)| ≥ β. Then for each j-cell σ ∈ Xj(A),

kj + j + 1 µj+1

|Xj+1(σ, B)| ≥ β ·

,

![image 24](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile24.png>)

where µj+1 is the largest eigenvalue of the (j +1)-st upper Laplacian operator ∆+j+1 of X.

Proof. Let σ = {v0, v1, . . ., vj} ∈ Xj(A) be a j-face of X with all vertices in A. Denote by aσ the number of (j + 1)-cells containing σ and having the remaining vertex in A, and by bσ the number of (j + 1)-cells containing σ and having the remaining vertex in the complement B = V \ A, i.e.

aσ = |Xj+1(σ, A)|, and bσ = |Xj+1(σ, B)|. Then

aσ + bσ ≥ kj.

Note that bσ > 0, since σ is contained in some (j + 1)-face and β > 0. Assume aσ = 0. Note that kd−1 < kd−2 < · · · < k0, since X is d-dimensional and pure, hence β < kj. Also, β ≤ Kj+1, where Kj+1 is the maximal degree of a (j + 1)-face of X. Then, by Theorem 2.3,

β kj

µj+1 ≥ Kj+1 + (j + 2) ≥ β + (j + 1)

![image 25](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile25.png>)

and hence,

kj + j + 1 µj+1

bσ ≥ kj ≥ β

.

![image 26](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile26.png>)

Now assume that both aσ = 0 and bσ = 0. Denote the vertices in A which form a (j + 1)-cell with σ by u1, . . ., ua

, and those in B which form a (j + 1)-cell with σ by w1, . . ., wb

σ

. Deﬁne a function f ∈ Cj+1(X) in the following way:

σ

- – For 1 ≤ i ≤ aσ, f[v0, . . ., vj, ui] = (−1)j+2 · bσ.
- – For 1 ≤ i ≤ bσ, f[v0, . . ., vj, wi] = (−1)j+1 · aσ.
- – For 1 ≤ i1 ≤ aσ, 1 ≤ i2 ≤ bσ and 0 ≤ r ≤ j,

f[v0, . . ., vr, . . ., vj, ui

1

, wi

2

] = (−1)r.

- – For all other (j + 1)-cells τ ∈ Xj+1, f[τ] = 0.


Then for every (j + 2)-cell of the form {v0, . . ., vj, ui

2} the following equalities hold

, wi

1

(δj+1f)[v0, . . ., vj, ui

]

, wi

1

2

j

(−1)rf[v0, . . ., vr, . . ., vj, ui

=

, wi

1

r=0

] + (−1)j+1f[v0, . . ., vj, wi

]

2

1

+(−1)j+2f[v0, . . ., vj, ui

]

1

j

(−1)2r + (−1)2(j+1)aσ + (−1)2(j+2)bσ = j + 1 + aσ + bσ.

=

r=0

There are aσ (j + 1)-cells in A containing σ, hence there are at least aσβ (j + 2)-cells of the form {v0, . . ., vj, ui

2}, i.e., |Xj+2(σ, A, B)| ≥ aσβ.

, wi

1

Therefore,

∆j+1f, f = δj+1f, δj+1f ≥ aσβ(j + 1 + aσ + bσ)2.

There are exactly aσ faces of the form {v0, . . ., vj, ui}, and exactly bσ faces of the form {v0, . . ., vj, wi}, and for each 0 ≤ r ≤ j there are not more than aσbσ faces of the form {v0, . . ., vr−1, vr, . . ., vj, ui

2}. Hence

, wi

1

f, f ≤ aσb2σ + bσa2σ + (j + 1)aσbσ = aσbσ(j + 1 + aσ + bσ) Since µj+1 is the largest eigenvalue of ∆j+1, we get that

aσβ(j + 1 + aσ + bσ)2 aσbσ(j + 1 + aσ + bσ)

∆j+1f, f f, f ≥

β(j + 1 + aσ + bσ) bσ ≥

µj+1 ≥

=

![image 27](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile27.png>)

![image 28](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile28.png>)

![image 29](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile29.png>)

β(j + 1 + kj) bσ

, and hence

![image 30](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile30.png>)

kj + j + 1 µj+1

bσ = |Xj+1(σ, B)| ≥ β

.

![image 31](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile31.png>)

![image 32](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile32.png>)

![image 33](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile33.png>)

![image 34](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile34.png>)

![image 35](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile35.png>)

Now we turn to the proof of the Theorem 1.2.

Proof. Let A ⊆ V be the largest independent set of vertices of X, in particular, there is no d-face with all vertices in A. Denote the complement

- B = V \ A and a = |A|, b = |B|. Note that both a and b are positive. The desired inequality on the independence number is obtained by bounding from above and below the number |X1(A, B)| of 1-faces, i.e. edges, with exactly one vertex in A.


Upper bound: Consider the function f0 ∈ C0 on the vertices of X:

f0(v) = −b, if v ∈ A; a, if v ∈ B.

Since µ0 is largest eigenvalue of the 0-th Laplacian ∆0, µ0 ≥

∆0f0, f0 f0, f0

δ0f0, δ0f0 f0, f0

=

![image 36](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile36.png>)

![image 37](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile37.png>)

= |X1(A, B)| · (a + b)2 a · b2 + b · a2

= |X1(A, B)| · n (n − a)a

, and hence

![image 38](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile38.png>)

![image 39](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile39.png>)

(n − a) · a n ≥ |X1(A, B)|. (1)

µ0 ·

![image 40](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile40.png>)

Lower bound: Since A is independent, for each (d − 1)-face in A, τ ∈ Xd−1(A) the following inequality holds

|Xd(τ, B)| ≥ kd−1.

By a consecutive application of Lemma 3.1, we have that for each 0-face, i.e. a vertex v ∈ A,

kd−2 + d − 1 µd−1

k0 + 1 µ1

|X1(v, B)| ≥ kd−1 ·

. Hence,

. . .

![image 41](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile41.png>)

![image 42](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile42.png>)

|X1(A, B)| =

(k0 + 1) . . .(kd−2 + d − 1)kd−1 µ1 . . . µd−1 · a. (2)

|X1(v, B)| ≥

![image 43](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile43.png>)

v∈A

Conclusion: By combining the bounds (1) and (2), we have

(n − a) · a n ≥ |X1(A, B)| ≥

(k0 + 1) . . .(kd−2 + d − 1)kd−1

µ0 ·

µ1 . . .µd−1 · a which implies,

![image 44](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile44.png>)

![image 45](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile45.png>)

µ0 . . .µd−1 − (k0 + 1) . . .(kd−2 + d − 1)kd−1 µ0 . . .µd−1 · n. And since χ(X)α(X) ≥ n, the second bound of the theorem follows.

a = α(X) ≤

![image 46](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile46.png>)

![image 47](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile47.png>)

![image 48](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile48.png>)

![image 49](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile49.png>)

![image 50](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile50.png>)

## 4 Complexes with complete (d − 1)-skeleton

Denote Knd the complete d-dimensional complex on n vertices, i.e. every subset of size (d+1) forms a face in Knd. A d-dimensional simplicial complex X on a vertex set V , with |V | = n, is said to have a complete (d−1)-skeleton, if X(d − 1) = Knd−1.

Theorem 4.1. Let X be a nonempty pure d-dimensional simplicial complex with complete (d − 1)-skeleton on a ﬁnite vertex set V of size n, then

µ − kd−1

α(X) ≤

µ · n, and

![image 51](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile51.png>)

µ µ − kd−1

χ(X) ≥

,

![image 52](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile52.png>)

where kd−1 is the minimal degree of a (d − 1)-face, µ = µd−1 is the largest eigenvalue of the (d − 1)-th upper Laplacian operator ∆+d−1 of X.

Since for each j = 0, . . ., d−2 all j-faces are of the same degree n−(j+1), and the largest eigenvalue of ∆+j is

µj = n, 0 ≤ j ≤ d − 2,

the proposition follows directly from the main theorem. Nevertheless, this special case can be proved directly and diﬀerently as follows.

Proof. As before, let A ⊆ V be the largest independent set of vertices of X, let B = V \ A be its complement, and a = |A|, b = |B| = n − a. Note that, a ≥ d. Partition A into a disjoint union of d non-empty subsets A = A0 ⊔ · · · ⊔ Ad−1, and denote |Aj| = aj, j = 0, . . ., d − 1. Consider the following function f ∈ Cd−1(X, R)

- – For vi ∈ Ai, 0 ≤ i ≤ d − 1, f[v0, . . ., vd−1] = b.
- – For vi ∈ Ai, 0 ≤ i ≤ d − 1, u ∈ B and 0 ≤ l ≤ d − 1, f[v0, . . ., vl−1, vl+1, . . ., vd−1, u] = (−1)l · al.
- – For all other (d − 1)-cells τ ∈ Xj+1, f[τ] = 0.


Then

f, f = a0 · · ·ad−1 · b · (b + a0 + . . .ad−1) = a0 · · ·ad−1 · (n − a) · n and, since A is independent and X has complete skeleton,

∆d−1f, f ≥ a0 · · ·ad−1 · kd−1 · (b + a0 + . . .ad−1)2 = a0 · · ·ad−1 · kd−1 · n2 And since

∆d−1f, f f, f

kd−1 · n n − a the bound follows.

µd−1 ≥

=

![image 53](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile53.png>)

![image 54](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile54.png>)

![image 55](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile55.png>)

![image 56](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile56.png>)

![image 57](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile57.png>)

![image 58](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile58.png>)

This proof was inspired by the work [PRT] of O. Parzanchevski, R. Rosenthal and R. Tessler on a generalization of the Cheeger inequality. Remark 4.2. The bound presented in Theorem 4.1 is sharp for the independence number of the full d-dimensional complex Knd on n vertices.

The complex Knd has a full (d − 1)-skeleton and every (d − 1)-face is contained in kd−1 = n−d d-faces. The largest eigenvalue of ∆+d−1 is µd−1 = n. The independence number of Knd is equal to d, and it is equal to the bound given by Theorem 1.2

µd−1 − kd−1 µd−1 · n.

αd(Knd) = d =

![image 59](<2013-golubev-chromatic-number-simplicial-complex_images/imageFile59.png>)

Acknowledgements. The author is grateful to his advisor A. Lubotzky as well as to Oren Becker, Shai Evra, Ori Parzanchevski, Ron Rosenthal and Benny Sudakov for fruitful discussions on the topic, and to ERC for the support.

The author is grateful to two anonymous referees, whose valuable remarks helped shortening the proofs and enriching the content of the paper.

The ﬁnal draft of the paper was prepared during a short visit of the author to ITC-ETHZ.

## References

[DF] M. Deza, P. Frankl, On the maximum number of permutations with given maximal or minimal distance, Journal of Combinatorial Theory, Series A, 22(3), (1977), pp. 352–360.

[Ec] B. Eckmann, Harmonische Funktionen und Randwertaufgaben in einem

Komplex, Commentarii Mathematici Helvetici, 17(1), (1944), pp. 240–255. [Ho] A.J. Hoﬀman, On Eigenvalues and Colorings of Graphs, Graph Theory

and its Applications, (ed: B. Harris), Academic Press, (1970) pp. 79–91.

[HJ] D. Horak, J. Jost, Spectra of combinatorial Laplace operators on simplicial complexes, Advances in Mathematics, 244, (2013), pp. 303–336.

[Lo] L. Lova´sz, On the Shannon capacity of a graph, IEEE Transactions of Information Theory, IT-25(1), (1979), pp. 1–7.

[LPS] A. Lubotzky, R. Phillips, P. Sarnak, Ramanujan Graphs, Combinatorica, 8(3), (1988), pp. 261–277.

[PRT] O. Parzanchevski, R. Rosenthal, R.J. Tessler, Isoperimetric Inequalities in Simplicial Complexes, Combinatorica, (2015), pp. 1–33.

[Re] P. Renteln, On the Spectrum of the Derangement Graph, Electronic Journal of Combinatorics, 14(1), (2007), R82.

[Wi] H.S. Wilf, The Eigenvalues of a Graph and Its Chromatic Number, Journal of the London Mathematical Society s1-42 (1967), pp. 330–332.

[WE] P. Wocjan, C. Elphick, New Spectral Bounds on the Chromatic Number Encompassing all Eigenvalues of the Adjacency Matrix. Electronic Journal of Combinatorics, 20(3), (2013), P39.

