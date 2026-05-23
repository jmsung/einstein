# Graphs and spherical two–distance sets

##### Oleg R. Musin∗

## arXiv:1608.03392v5[math.MG]14Jul2018

###### Abstract

Every graph G can be embedded in a Euclidean space as a two–distance set. The Euclidean representation number of G is the smallest dimension in which G is representable by such an embedding. We consider spherical and J–spherical representation numbers of G and give exact formulas for these numbers using multiplicities of polynomials that are deﬁned by the Caley–Menger determinant. One of the main results of the paper are explicit formulas for the representation numbers of the join of graphs which are obtained from W. Kuperberg’s type theorem for two–distance sets.

Throughout this paper we will consider only simple graphs, Rd will denote the d– dimensional Euclidean space, Sn will denote the n–dimensional unit sphere in Rn+1, and dist(x,y) := ||x − y|| will denote the Euclidean distance in Rd. For a set X ⊂ Rd we shall denote the aﬃne hull (or aﬃne span) by aﬀ(X), rank(X) := dimaﬀ(X) and conv(X) will denote the convex hull of X. We will denote the cardinality of a ﬁnite set X by |X| .

### 1 Introduction

Representations (embeddings) of a graph G into a metric space, in particular into Rd, is a classical discrete geometry problem (see [10, Ch. 6,19] and [11, Ch. 15,19]). The dimension of G is the smallest d for which it can be embedded in Rd as a unit–distance graph [7]. In this paper we consider the smallest d for which G can be embedded as a two–distance set.

Let G be a graph on n vertices. Consider a Euclidean representation of G in Rd as a two–distance set. In other words, there are two positive real numbers a and b with b ≥ a > 0 and an embedding f of the vertex set of G into Rd such that

dist(f(u),f(v)) :=

- a if uv is an edge of G
- b otherwise


After Roy [24], the smallest d such that G is representable in Rd we will call the Euclidean representation number of G and denote it dimE2(G).

∗This research is partially supported by the NSF grant DMS–1400876.

Einhorn and Schoenberg [12] showed that dimE2(G) can be found explicitly in terms of the multiplicity µ(G) of the root τ1 of the discriminating polynomial (see Section 2).

- Theorem 2.1 Let G be a graph with n vertices. Then dimE2(G) = n − µ(G) − 1.

In Section 3 we consider representations of G as spherical two–distance sets. Let f be a Euclidean representation of G in Rd with the minimum distance a = 1. We say that f is spherical if the image f(G) lies on a (d−1)–sphere in Rd. We denote by dimS2(G) the smallest d such that G is spherically representable in Rd.

If d ≤ n − 2, then f is uniquely deﬁned up to isometry (see Section 2). Therefore, if f is spherical, then the circumradius of f(G) is also uniquely deﬁned. We denote it by R(G). If f is not spherical or µ(G) = 0, then we put R(G) = ∞ (Deﬁnition 3.2).

- Theorem 3.1. Let G be a graph with n vertices. Then

dimS2(G) =

dimE2(G), R(G) < ∞; n − 1, R(G) = ∞.

Nozaki and Shinohara [22] also give necessary and suﬃcient conditions of a Euclidean representation of G to be spherical. However, their conditions are more bulky. Namely, they used Roy’s theorem (see [22, Theorem 2.4]) and they showed that among ﬁve types of conditions only three of them yields sphericity [22, Theorem 3.7].

Nozaki and Shinohara also considered strongly regular graphs. For instance, they proved the following interesting fact: a graph G with n vertices is strongly regular if and only if dimS2(G) + dimS2(G¯) + 1 = n [22, Theorem 4.5].

Theorem 4.1 states that R(G) ≥ 1/√2. In Section 4 we consider the extreme case R(G) = 1/√2. Let f be a spherical representation of a graph G in Rd as a two–distance set. We say that f is a J–spherical representation of G if the image f(G) lies in a sphere Sd−1 of radius 1/√2 and the ﬁrst (minimum) distance a = 1.

To prove the existence of J–spherical representations is not very easy. Corollary 4.1 states that for any graph G = Kn there is a unique (up to isometry) J–spherical representation. Then for a J–spherical representation f : G → Rd the dimension d and second distance b are uniquely deﬁned, we denote these d and b by dimJ2(G) and β∗(G) respectevely.

- Theorem 4.3. Let G = Kn be a graph on n vertices. Then


dimE2(G), R(G) = 1/√2; n − 1, R(G) > 1/√2.

dimJ2(G) =

In Section 5 we consider W. Kuperberg’s theorem on sets S in Sn−1 with n+2 ≤ |S| ≤ 2n and the minimum distance between points of S at least √2 [15]. Theorem 5.4 shows that S is the join of its subsets Si. If S is a two–distance set, then S is a J–spherical representation.

Using results of Section 5, in Section 6 we give explicit formulas for representation numbers in the case when G is the graph join: G = G1 + ... + Gm. In particular, these formulas can be applied for the complete multipartite graph Kn

1...nm.

Theorem 6.2. Let G1,...,Gm be a ﬁnite collection of graphs with n1,...,nm vertices respectively, let G := G1 + ... + Gm and n := n1 + ... + nm. Suppose

β∗(G1) = ... = β∗(Gk) < β∗(Gk+1) ≤ ... ≤ β∗(Gm). Then

dimJ2(G) = dimJ2(G1) + ... + dimJ2(Gk) + nk+1 + ... + nm, dimS2(G) = dimJ2(G), dimE2(G) = min(dimJ2(G),n − 2).

Corollary 6.1. Let G be the complete multipartite graph Kn

1...nm. Suppose n1 = ... = nk > nk+1 ≥ ... ≥ nm

and let n := n1 + ... + nm. Then

- 1. dimE2(G) = min(n − k,n − 2);
- 2. dimS2(G) = dimJ2(G) = n − k. Note that Statement 1 in Corollary 6.1 was ﬁrst proved by Roy [24, Theorem 1]. In Section 7 we consider seven open problems on representations of graphs.


### 2 Euclidean representations of graphs

In this section we consider Euclidean representations of graphs as two–distance sets.

A complete graph Kn represents the vertices of a regular (n − 1)–simplex. In fact, this is a representation of Kn as a one–distance set. Then dimE2(Kn) = n − 1 and

dimE2(G) ≤ n − 1 for any graph G with n vertices.

Thus we have a correspondence between graphs and two-distance sets. Let S be a two– distance set in Rd with distances a and b ≥ a. Denote by Γ(S) a graph with S as the set vertices and edges [pq], p,q ∈ S, such that dist(p,q) = a. Then S is a Euclidean representation of G = Γ(S).

Let S be a two–distance set of cardinality n in Rd. Then, see [3, 8], we have

(d + 1)(d + 2) 2

n ≤

. (2.1)

(Lisoneˇk [16] shows that the upper bound (2.1) is tight for d = 8.) This bound implies the following lower bound

√8n + 1 − 3 2

dimE2(G) ≥

.

Let G be a graph with n vertices. Einhorn and Schoenberg [12] considered Euclidean representations of graphs. They proved that

dimE2(G) = n − 1 if and only if G is a disjoint union of cliques. Moreover, they have shown that

If dimE2(G) ≤ n − 2, then a Euclidean representation of G in Rd, where d := dimE2(G), is uniquely deﬁned up to isometry.

Let S = {p1,...,pn} be a two-distance set with distances a = 1 and b > 1. Let dij := dist(pi,pj). Consider the Cayley–Menger determinant

CS :=

- 0 1 1 ... 1
- 1 0 d212 ... d21n


1 d221 0 ... d22n .................... .................... 1 d2n1 d2n2 ... 0

(2.2)

Since for i = j, dij = 1 or b, CS is a polynomial in t = b2. Denote this polynomial by CG(t).

Actually, in [12] instead of CG the discriminating polynomial D(t) is considered. This polynomial can be deﬁned through the Gram determinant. Since, see [6, Lemma 9.7.3.3],

CG(t) = (−1)nD(t) these two polynomials are the same up to the sign and therefore have the same roots.

- Deﬁnition 2.1. Let G be a graph with n vertices. Let τ1 = τ1(G) be the smallest root of CG(t), i.e. CG(τ1) = 0, such that τ1 > 1. By µ(G) we denote the multiplicity of the root τ1(G) of CG. If all roots t∗ ≤ 1, then we put τ1(G) = ∞ and µ(G) = 0.


Einhorn and Schoenberg proved that if S is embedded exactly in Rd, then τ1 is a root of CG(t) of exact multiplicity n − d − 1 [12, Lemma 6]. Equivalently, we have the following theorem:

- Theorem 2.1. Let G be a graph with n vertices. Then dimE2(G) = n − µ(G) − 1.


Roy [24] found that dimE2(G) depends on certain eigenvalues of graphs. Actually, these dimensions are closely related with the multiplicity of the smallest (or second smallest) eigenvalue of the adjacency matrix A(G).

In [12, 22, 24] two Euclidean representation numbers dimE2(G) and dimE2(G¯) are considered , where G¯ is the graph complement of G. These numbers can be diﬀerent. For instance, let G be the disjoint union of m edges. Then dimE2(G) = 2m − 1. On the other hand, G¯ is the complete multipartie graph K2,...,2. It follows from [12, Theorem 2] or [24, Theorem 1] (see also [2]) that

dimE2(K2,...,2) = m. Indeed, G = K2,...,2, then n = 2m and

CG(t) = 2mtm(2 − t)m−1. Therefore τ1(G) = 2 and µ(G) = m − 1. Thus dimE2(K2,...,2) = m.

Note that a minimal Euclidean representation of this graph is a regular m–dimensional cross–polytope. In Section 6 we consider a geometric method for complete multipartite graphs.

There is an obvious relation between polynomials CG(t) and CG¯(t). Namely, CG¯(t) is the reciprocal polynomial of CG(t). If G or G¯ is not the complete multipartite graph, then τ0(G) := 1/τ1(G¯) is a root of CG(t) and there are no more roots in the interval I := [τ0(G),τ1(G)]. Moreover, a two–distance set S with distances 1 and √t is well–deﬁned only if t ∈ I [12].

In fact, if dimE2(G) ≤ n − 2, then a minimal Euclidean representation is unique up to isometry. Indeed, in this case a = 1 and b = √τ1, then all distances between vertices in the representation are known.

Using this approach Einhorn and Schoenberg [12] enumerated all two-distance sets in dimensions two and three. In other words, they enumerated all graphs G with dimE2(G) = 2 and dimE2(G) = 3. In [19] we state the same problem in four dimensions. Recently, Szo¨llo¨si [25] using a computer enumeration of graphs solved this problem.

### 3 Spherical representations of graphs

Let f be a Euclidean representation of a graph G with n vertices in Rd as a two–distance set. We say that f is a spherical representation of G if the image f(G) lies on a (d − 1)–sphere in Rd. We will call the smallest d such that G is spherically representable in Rd the spherical representation number of G and denote it dimS2(G).

Representation numbers dimS2(G) and dimE2(G) can be diﬀerent. In Section 6 we show that if G is a bipartite graph Km,n with m = n, then

dimE2(Km,n) = n + m − 2 < dimS2(Km,n) = n + m − 1. For a graph G on n vertices we obviously have

dimE2(G) ≤ dimS2(G) ≤ n − 1 (3.1)

Actually, for spherical representation numbers lower bound (2.1) can be a little bit improved. Delsarte, Goethals, and Seidel [9] proved that the largest cardinality of spherical two-distance sets in Rd is bounded by d(d + 3)/2. (This upper bound is known to be tight for d = 2,6,22.) That yields

√8n + 9 − 3 2

dimS2(G) ≥

. This bound has been improved for some dimensions. Namely, in [18] we proved that n ≤

d(d + 1) 2

(3.2)

for 6 < d < 22 and 23 < d < 40. This inequality was extended for almost all d ≤ 93 by Barg & Yu [5] and for d ≤ 417 by Yu [26]. Recently, Glazyrin & Yu [13] proved (3.2) for all d ≥ 7 with possible exceptions for some d = (2k + 1)2 − 3, k ∈ N.

Let S = {p1,...,pn} be a set in Rn−1. As above, dij := dist(pi,pj). Let

0 d212 ... d21n d221 0 ... d22n ................. ................. d2n1 d2n2 ... 0

(3.3)

MS :=

It is well known [6, Proposition 9.7.3.7], that if the points in S form a simplex of dimension (n − 1), then the radius R of the sphere circumscribed around this simplex is given by

- 1

- 2


MS CS

R2 = −

. (3.4)

(Here CS is deﬁned by (2.2).)

- Deﬁnition 3.1. Let G be a graph with vertices v1,...,vn. Put dij := 1 if [vivj] is an edge of G, otherwise put dij := b. We denote by CG(t) and MG(t) the polynomials in t = b2 that are deﬁned by (2.2) and (3.3), respectively. Let


- 1

- 2


FG(t) := −

MG(t) CG(t)

.

- Lemma 3.1. Let S be a spherical representation of a graph G with distances a and b, b ≥ a. Then S lies on a sphere of radius R = a2FG(b2/a2).


Proof. If X = {x1,...,xn} is a set of points in Rn−1 in general position, then rank(X) = n−1, conv(X) is a simplex and (3.4) determines the circumradius R(X) of conv(X). Clearly, R(X) is a continues function in {xi}.

We have that rank(S) ≤ n−1. If rank(S) = n−1, then (3.4) implies the lemma, otherwise consider a sequence of sets {Xk}, k ∈ N, in Rn−1 in general position such that S is a limit set of this sequence. Thus, R(S) is the limit of {R(Xk)}, k ∈ N.

As we noted above, if rank(S) < n − 1 and a = 1, then a spherical (and Euclidean) representation of G is uniquely deﬁned up to isometry. However, if rank(S) = n − 1, then there are inﬁnitely many non–isometric spherical representations. This is easy to see, let S be the set of vertices of a simplex in which one of edges has length b ≥ 1 and all other edges are of lengths a = 1. It can be proved (see the next section) that the range of R(S) is [1/√2,∞). This fact and Lemma 3.1 explain our deﬁnition of the circumradius of G.

- Deﬁnition 3.2. If G is a graph with τ1(G) < ∞ and FG(τ1) < ∞, then denote R(G) := FG(τ1).


Otherwise, put R(G) := ∞.

- Theorem 3.1. Let G be a graph on n vertices. Then

dimS2(G) =

dimE2(G) if R(G) < ∞; n − 1 if R(G) = ∞.

Proof. Denote by Iε a small interval [τ1 − ε,τ1 + ε] that does not contain any other roots of CG and MG. Then for every t in Iε, t = τ1, the Cayley–Menger determinant (2.2) is non–zero. Therefore, it deﬁnes a Euclidean (spherical) representation ft of G in Rn−1. Let St := {ft(vi)}, where vi are the vertices of G. Lemma 3.1 implies that FG(t) = R2(t), where R(t) is the radius of the sphere circumscribed about St.

From (3.1) it follows that dimE2(G) = n − 1 yields dimS2(G) = n − 1. If dimE2(G) ≤ n − 2, then µ(G) ≥ 1. Therefore, for t = τ1, Theorem 2.1 implies that St is embedded into Rn−µ−1.

Suppose dimS2(G) ≤ n−2. Then (3.1) implies that dimE2(G) ≤ n−2. In this case a minimal spherical representation of G is uniquely deﬁned by τ1 and Sτ

1

is a spherical set that lies on a sphere of radius ρ > 0. Then R(t) and FG(t) are continuous functions in t that are well deﬁned for all t in Iε and FG(τ1) = ρ2. It is easy to see that the inequlality FG(τ1) > 0 yields that the multiplicities of τ1 in CG and MG are equal. Thus, we have dimS2(G) = dimE2(G).

| |
|---|


4 J–spherical representation of graphs

In this section we prove that R(G) ≥ 1/√2 and then we consider the boundary case R(G) = 1/√2.

For a proof of the next theorem we need Rankin’s theorem. Rankin [23] proved that If S is a set of d + k, k ≥ 2, points in the unit sphere Sd−1 in Rd, then two of the points in S are at a distance of at most √2 from each other.

- Theorem 4.1. R(G) ≥ 1/√2.


Proof. Let G be a graph on n vertices. By the deﬁnition if dimS2(G) = n−1, then R(G) = ∞.

Let S be a minimal spherical representation of G. If dimS2(G) ≤ n − 2, then S lies in a sphere Ω in Rn−2 of radius R. By Rankin’s theorem if d+2 points lie in a sphere of radius R in Rd, then a ratio a/R ≤

√2, where a is the minimum distance between these points. Since

- a = 1, we have R(G) = R ≥ 1/√2.


Hence we have a two–distance set X with distances a = 1 and b > a such that the circumradius of X is 1/√2. Actually, we will consider a set S that is similar to X with the scale factor √2. Therefore, S is a two-distance set with the ﬁrst distance a = √2 that can be inscribed in the unit sphere.

- Deﬁnition 4.1. Let f be a spherical representation of a graph G in Rd as a two distance set. We say that f is a J–spherical representation of G if the image f(G) lies in the unit sphere Sd−1 and the ﬁrst (minimum) distance a = √2.


The existence of Euclidean and spherical representations for any graph G is obvious. However, to prove it for J–spherical representations is not very easy. Clearly, if G is a complete graph Kn, then this representation does not exist. We show that this is just one exceptional case, and for every other G there is a J–spherical representation.

Notation. Let G be a graph on n vertices. IG := √2, 2τ1(G) . SG(x) : a two–distance set S in Rn−1 with distances a = √2 and b = x such that Γ(S) = G. (Here, as above, Γ(S) is the graph with edges of length a.)

∆G(x) := conv SG(x). ΦG(x) : the radius of the minimum enclosing ball of SG(x) in Rn−1.

- Lemma 4.1. If x ∈ IG, then rankSG(x) = n − 1.


Proof. Since the Cayley–Menger determinant and the volume of a simplex are equal up to a constant and CG(x2/2) = 0 for x ∈ IG, we have that ∆G(x) is a simplex in Rn−1 of dimension n − 1. Thus, rankSG(x) = dim∆G(x) = n − 1.

| |
|---|


- Lemma 4.2. The function ΦG(x) is increasing on IG. Proof. The proof relies on the Kirszbraun theorem (see [14, 1])1:


Let X be a subset of Rd and f : X → Rm be a Lipschitz function. Then f can be extended to the whole Rd keeping the Lipschitz constant of the original function.

Let √2 ≤ y1 < y2 < 2τ1(G). Then by Lemma 4.1 SG(yi) = {vi1,...,vin} is the set of vertices of an (n−1)–simplex ∆G(yi) that lies in the minimum enclosing ball B(yi) of radius ΦG(yi).

Let

h(v2k) := v1k, k = 1,...,n.

Then we have h : SG(y2) → Rn−1. It is clear that the Lipschitz constant of h is equal to 1. By the Kirszbraun theorem h can be extended to H : Rn−1 → Rn−1 with the same Lipschitz constant.

1The author thanks Arseniy Akopyan for the idea of this proof.

Let c2 be the center of B(y2). For all k = 1,...,n we have dist(H(c2),H(v2k)) = dist(H(c2),v1k) ≤ dist(c2,v2k) ≤ ΦG(y2).

Therefore, H(c2) is a point in ∆G(y1) such that all distances from H(c2) to vertices SG(y1) does not exceed ΦG(y2). Then ΦG(y1) ≤ ΦG(y2).

| |
|---|


- Lemma 4.3. Let S be a set in Rn−1 of cardinality |S| ≥ n. Suppose the minimum distance between points of S is at least √2. If S lies in a sphere of radius R ≤ 1, then sphere’s center O ∈ conv(S).


Proof. Assume the converse. Then S lies in an open hemisphere of radius R. It can be proved (see [17, Theorem 3] or [4, Theorem 5]) that the assumptions yield |S| < n, a contradiction.

| |
|---|


- Theorem 4.2. Let G be a graph with n vertices. Let R : (n − 1)/n < R ≤ 1. Suppose G = Kn, then there is a unique x ∈ IG such that SG(x) lies on a sphere of radius R.


Proof. Let b1 := 2τ1(G). First we prove that there is a solution of the equation ΦG(x) = R. Namely, we are going to prove that

√

2) = (n − 1)/n ≤ R ≤ 1 ≤ ΦG(b1).

ΦG(

Indeed, it is clear that ΦG(√2) is the circumradius of a regular (n − 1)–simplex, of side length √2. Then

√

n − 1 n

. Now we show that ΦG(b1) ≥ 1. In the case b1 = ∞, it is clear that ΦG(x) approaches ∞

ΦG(

2) =

- as x approaches ∞. Let b1 < ∞. Then the Cayley–Menger determinant vanishes and SG(b1) embeds in Rd,


where d ≤ n − 2. By Theorem 4.1, √2R(G) ≥ 1. Therefore, if ΦG(x) < 1, then x < b1. (Equivalently, we have n ≥ d+2 points with the minimum distance √2 in a ball of radius

ΦG(b1). By Rankin’s theorem [23] it is possible only if the radius ΦG(b1) ≥ 1.) Therefore ΦG(b) = R for some b ∈ [√2,b1]. Now we show that for x ∈ [√2,b1] a solution of the equation ΦG(x) = R is unique. By

- Lemma 4.2 ΦG(x) is increasing whenever x is increasing. However, we did not prove that ΦG(x) is a strictly increasing function. Suppose P(y1) = R and P(y2) = R, where y1 < y2. Then ΦG(x) is a constant on the interval [y1,y2]. Lemma 4.3 yields that for x ∈ [y1,y2] the circumcenter of a simplex ∆G(x) lies in this simplex.


It is well known that if the circumcenter of a simplex ∆ is an internal point of ∆, then the minimum enclosing sphere is the circumsphere of ∆. Therefore, for this case we have

x2 2

ΦG(x) = 2FG(t), t =

.

Then Φ2G(x) is a rational function in x2. It implies that ΦG(x) cannot be a constant in [y1,y2]. Note that the case of an empty graph, i.e. G = K¯1,...,1, is well–deﬁned. If R = 1, then

√

2n n − 1

b∗ =

>

2

and SG(b(1)) is the set of vertices of a regular (n − 1)–simplex of side length b. (In this case there are no edges of length a = √2.) If for R < 1 we take b = Rb∗, then it will be a unique solution of the equation ΦG(x) = R.

| |
|---|


This theorem for R = 1 yields the following

- Corollary 4.1. For every graph G = Kn there is a unique (up to isometry) J–spherical representation.

The uniqueness of a J–spherical representation shows that the following deﬁnition is correct.

Deﬁnition 4.2. Let f : G → Rd be a J–spherical representation of G. We denote the image f(G) by WG and the dimension d by dimJ2(G). Denote the second distance of WG by β∗(G).

Representation numbers dimJ2(G) and dimS2(G) can be diﬀerent. For instance, if G is the pentagon, then

dimS2(G) = 2 < dimJ2(G) = 4.

Note that dimJ2(G) < n − 1 only if β∗(G) = 2τ1(G). Moreover, since the circumradius of WG is 1, we have to have R(G) = 1/√2. That yields the following theorem. Theorem 4.3. Let G = Kn be a graph on n vertices. Then

dimJ2(G) =

dimE2(G), R(G) = 1/√2; n − 1, R(G) > 1/√2.

Rankin’s theorem and Theorem 4.3 yield

- Corollary 4.2. Let G be a graph on n vertices and G = Kn. Then n 2 ≤ dimJ2(G) ≤ n − 1.


If dimJ2(G) = n/2, then G = K2,...,2 and a J–spherical representation of G is a regular cross–polytope.

### 5 The join of sets and Kuperberg’s theorem

- 5.1 W. Kuperberg’s theorem.


As we noted above, Rankin’s theorem states that if S is a subset of Sd−1 with |S| ≥ d + 2, then the minimum distance between points in S is at most √2. Wlodzimierz Kuperberg [15] extended Rankin’s theorem and proved that:

- Theorem 5.1. Let d and k be integers such that 2 ≤ k ≤ d. If S is a (d + k)–point subset of the unit d–ball such that the minimum distance between points is at least √2, then: (1)


every point of S lies on the boundary of the ball, and (2) Rd splits into the orthogonal product

k

i=1 Li of nondegenerate linear subspaces Li such that for Si := S ∩Li we have |Si| = di +1 and rank(Si) = di (i = 1,2,...,k), where di := dimLi.

In fact, this theorem states that S is join–decomposable.

- Deﬁnition 5.1. The join X ∗Y of two sets X ⊂ Rm and Y ⊂ Rn is formed in the following manner. Embed X in the m–dimensional linear subspace of Rm+n as


{(x1,...,xm,0,...,0) : x = (x1,...,xm) ∈ X} and embed Y as

{(0,...,0,y1,...,yn) : y ∈ Y }.

Geometrically the join corresponds to putting the two sets X and Y in orthogonal linear subspaces of Rm+n. Hence Kuperberg’s theorem implies that S = S1 ∗ ... ∗ Sk.

Actually, Kuperberg’s proof of Theorem 5.1 yields that conv(Si) contains the center O of the unit d–ball. This statement also follows from Lemma 4.3

Let conv(S) be a d–dimensional simplex, i.e. rank(S) = d. We have two cases: (i) O lies in the interior of conv(S); (ii) O lies on the boundary of conv(S).

It is clear, that in Case (i) S is join–indecomposable. Consider Case (ii). Let S1 be a minimal subset of S among such subsets whose convex hull contains O. Then [15, Proposition

###### 6] yields that S2 := S \ S1 lies in the orthogonal complement of aﬀ(S1), i.e. S = S1 ∗ S2.

- Lemma 5.1. Let S be a subset of Sd−1 with |S| ≥ d + 1 such that the minimum distance between points of S is at least √2. Suppose O lies on the boundary of conv(S). Then S is join–decomposable.


This lemma shows that there are two types of join–indecomposable spherical sets.

- Type I: S ⊂ Sd−1, |S| = d + 1, rank(S) = d and the center O of Sd−1 lies in the interior of conv(S).
- Type II: S ⊂ Sd−1, |S| = d, rank(S) = d − 1 and O ∈/ aﬀ(S).


Consider an example, let S consists of three vertices of an isosceles right triangle in the unit circle, for instance, S = {p1.p2,p3}, p1 = (1,0), p2 = (−1,0) and p3 = (0,1). Then S = S ∗ S , where S := {p1,p2} and S := {p3}. Here S is of Type 1 and S is of Type 2.

Lemma 5.1 says that if O lies in the boundary of Si then Si = S i ∗ S i . It yields the following version of Kuperberg’s theorem.

- Theorem 5.2. Let S be a subset of the unit d–ball in Rd with the minimum distance between points at least √2. Suppose |S| = d + k with 2 ≤ k ≤ d. Then S = S1 ∗ ... ∗ Sm, where Si, i = 1,...,k are of Type I and all other Si are of Type II.


#### 5.2 The join of spherical two–distance sets

- Deﬁnition 5.2. We say that a two–distance set S in Rd is a J–spherical two–distance set (JSTD) if S lies in the unit sphere centered at the origin 0 and a = √2. For this S the second distance b will be denoted b(S).


The next two lemmas immediately follow from deﬁnitions.

- Lemma 5.2. Let S1 and S2 be spherical two-distance sets with the same distances a and

b ≥ a. Let Ri denote the circumradius of Si. Then (1) the join S1∗S2 is spherical if R1 = R2 and (2) the join is a two–distance set only if R12 + R22 = a2 or R12 + R22 = b2.

- Lemma 5.3. Let S1 and S2 be JSTD sets with b(S1) = b(S2). Then the join S1 ∗ S2 is a JSTD set.
- Lemma 5.4. Suppose for sets X1 and X2 in Rd there is positive ρ such that dist(p1,p2) = ρ for all points p1 ∈ X1, p2 ∈ X2. Then both Xi are spherical sets and the aﬃne hulls aﬀ(Xi) in Rd are orthogonal each other. If additionally rank(X1∪0)+rank(X2∪0) = rank(X1∪X2∪0), then X1 ∪ X2 = X1 ∗ X2, where 0 denote the origin of Rd.

Proof. 1. If p ∈ X1, then by assumption X2 lies on a sphere Sρ(p) of radius ρ and centered at p. Therefore, X2 belongs to a sphere that is the intersection of all Sρ(p), where p ∈ X1.

- 2. Let p1,p2 ∈ X1 and q1,q2 ∈ X2. Since in the tetrahedron p1p2q1q2 four sides piqj have the same length ρ, the edges p1p2 and q1q2 are orthogonal. That implies the orthogonality of the aﬃne spans aﬀ(X1) and aﬀ(X2) in Rd.
- 3. Let Li := aﬀ(Xi ∪ 0). Then dimLi = rank(Xi ∪ 0). By assumption L1 ∩ L2 = 0. Thus, the orthogonality of aﬀ(Xi) yields X1 ∪ X2 = X1 ∗ X2.


| |
|---|


- Theorem 5.3. Let S1 and S2 be JSTD sets in Rd. Then S := S1 ∪ S2 is a JSTD set and S = S1 ∗ S2 if and only if (1) dist(p1,p2) are the same for all points p1 ∈ S1, p2 ∈ S2; (2) rank(S ∪ 0) = rank(S1 ∪ 0) + rank(S2 ∪ 0) and (3) b(S1) = b(S2).


Proof. By Lemma 5.4, (1) and (2) imply that S = S1 ∗ S2. Since R1 = R2 = 1, from Lemma

- 5.2 we have dist(p1,p2) = √2. Finally, Lemma 5.3 yields that S is JSDT.


| |
|---|


#### 5.3 Kuperberg type theorem for two–distance sets

- Deﬁnition 5.3. Let S be a two-distance set. We say that S is J–prime if S is indecomposable with respect to the join.


It is easy to see that J–prime sets can be deﬁned in another way.

Proposition 5.1. Let S be a two–distance set. Let G = Γ(S). Then S is J–prime if and only if the graph complement G¯ is connected.

From Theorem 5.2 we know that any J–prime set is of Type I or Type II. If S is of Type I in Rd, then S is a JSTD of rank d and cardinality d+1. Therefore if we take G = Γ(S), then we obtain S = WG. Note that the inequality β∗(G) < τ1(G) implies that dimJ2(G) = d, where G is a graph on d + 1 vertices. We proved the following:

- Lemma 5.5. Let S be a J–prime JSTD set of Type I. Then b(S) = β∗(G) < τ1(G), where G := Γ(S).

If S is of Type II in Rd, then S is a JSDT set of cardinality d. For instance, if S = {p,q} is a two–points set in the unit circle with √2 < b = dist(p,q) < 2, then S is J– prime of Type II. Hence in this case the second distance b is not ﬁxed and lies in some open interval.

Let S be a JSDT set in Rd of cardinality d+k, where 2 ≤ k ≤ d. For this S Theorem 5.2 states that there are exactly k subsets Si of Type I. Now if we take S1 of Type I and S2 of Type II then S1 ∗ S2 is a JSDT set. From Lemma 5.3 follows that b(S1) = b(S2). Moreover, for S2 we have an extra constraint: this set lies in a (d − 2)–sphere of radius R < 1.

- Lemma 5.6. A JSTD set S in Rd, d = |S| − 2, is a J–prime set of Type II only if b(S) <


- β∗(G) < τ1(G), where G := Γ(S).


Proof. The assumption b(S) < β∗(G) is equivalent to R < 1, where R is the circumradius of S. By Theorem 4.2, there is a unique b such that a two–distance set S with a = √2 lies in a sphere of radius R.

| |
|---|


Theorem 5.2 implies the following theorem.

- Theorem 5.4. Let S, |S| = d+k, k ≥ 1, be a two–distance set in the unit sphere in Rd with


the minimum distance a = √2. Then S = S1 ∗ ... ∗ Sm such that all subsets Si are J–prime and exactly k of them are of Type I.

### 6 Representation numbers of the join of graphs

Recall that the join G = G1+G2 of graphs G1 and G2 with disjoint point sets V1 and V2 and edge sets E1 and E2 is the graph union G1 ∪ G2 together with the edges joining each point of V1 to each point of V2. In this section we apply results of Section 5 for the join of graphs.

The following theorem is a version of Theorem 5.4.

- Theorem 6.1. Let G be a graph with n vertices. Let dimJ2(G) = n − k ≤ n − 2. Then G = G1 + ... + Gm, where all Gi are indecomposable with respect to the join and


β∗(G) = β∗(G1) = ... = β∗(Gk) < β∗(Gk+1) ≤ ... ≤ β∗(Gm). Proof. Let S be a J–spherical representation of G. Then S satisﬁes the assumptions of

- Theorem 5.4. Therefore S = S1 ∗ ... ∗ Sm. Let S1,...,Sk be sets of Type I. Thus subgraphs Gi := Γ(Si) are as required.

| |
|---|


- Theorem 6.2. Let G1,...,Gq be a ﬁnite collection of graphs with n1,...,nq vertices, respectively. Let G := G1 + ... + Gq and n := n1 + ... + nq. Suppose


β∗(G1) = ... = β∗(Gp) < β∗(Gp+1) ≤ ... ≤ β∗(Gq). Then

dimJ2(G) = dimJ2(G1) + ... + dimJ2(Gp) + np+1 + ... + nq, dimS2(G) = dimJ2(G), dimE2(G) = min(dimJ2(G),n − 2).

Proof. By Theorem 6.1 there are graphs F1,...,Fm indecomposable with respect to the join and such that G := F1 + ... + Fm, k := k1 + ... + kp, where ki := ni − dimJ2(Gi), and

β∗(F1) = ... = β∗(Fk) < β∗(Fk+1) ≤ ... ≤ β∗(Fm). Let Si := WF

, i = 1,...k. For i > k, denote by Si a sets of Type II with Γ(Si) = Fi and b(Si) = β∗(F1). Then let S = S1 ∗ ... ∗ Sm be a J–spherical representation of G. It is clear that rank(S) = n − k.

i

If k ≥ 2, then dimJ2(G) ≤ rank(S) ≤ n − 2. In this case Lemma 5.2, Theorem 3.1 and Theorem 4.3 yield

dimE2(G) = dimS2(G) = dimJ2(G) = n − k = dimJ2(G1) + ... + dimJ2(Gp) + np+1 + ... + nq.

Now consider the case dimJ2(G) = n − 1 or, equivalently, k = 1. Let H := F2 + ... + Fm. Note that β∗(F1) < β∗(H) = β∗(F2).

Since G is not a disjoint union of cliques, dimE2(G) ≤ n − 2. Therefore, a Euclidean representation f : G = F1 + H → Rn−2 is unique. Let X1 := f(F1) and X2 := f(H). From Lemma 5.4 it follows that X1 and X2 are spherical orthogonal sets. Moreover, by Lemma

- 5.2 we have R12 + R22 = a2, where Ri denotes the circumradius of Xi. First note that R1 = R2, otherwise X and Y would be JSTD sets with dimE2(G) =


dimJ2(G) = n − 1. Hence f would not a spherical representation and dimS2(G) = n − 1. Note that R1 > R2. Indeed, it follows from the fact that b(X1) = b(X2), but β∗(F1) <

- β∗(H). Since b(X2) < β∗(H), we have rank(X2) = vH − 1, where vH denotes the number of vertices of H. Thus dimE2(G) = rank(X1 ∪ X2) = v1 − 1 + vH − 1 = n − 2.


| |
|---|


1...nm and n := n1 + ... + nm. Suppose

Corollary 6.1. Let G be the complete multipartite graph Kn

n1 = ... = nk > nk+1 ≥ ... ≥ nm. Then

dimS2(G) = dimJ2(G) = n − k, dimE2(G) = min(n − k,n − 2) Proof. Note that

1...nm = K¯n

+ ... + K¯n

. Since

Kn

m

1

2n n − 1

β∗(K¯n) =

, our assumption is equivalent to

β∗(K¯n

) = ... = β∗(K¯n

) < β∗(K¯n

) ≤ ... ≤ β∗(K¯n

).

m

1

k

k+1

Thus, this corollary follows from Theorem 6.2 and the obvious fact that the empty graph K¯ is indecomposable with respect to the join, i.e. dimJ2(K¯ ) = − 1.

| |
|---|


### 7 Concluding remarks and open problems

First we consider open problems that are directly related to this paper.

#### 7.1 Range of the circumradius R(G)

Let R(G) < ∞. What is the range of R(G)? Since for a ﬁxed n there are ﬁnitely many graphs G this range is a countable subset of the interval [1/√2,∞).

What is the maximum value of R(G)? Can R(G) be greater than 1?

#### 7.2 Monotonicity and convexity of the function FG(t)

Lemma 4.2 states that the function ΦG(x) is increasing on IG. If the circumcenter of a simplex ∆G(x) lies in this simplex, then its circumradius and the radius of the minimum enclosing sphere are the same, i.e. FG(t) = Φ2G(x), x = √2t. Therefore, under this constraint FG(t) is monotonic. Our conjecture is:

FG(t) is a monotonic increasing function for all t ∈ (1,τ1(G)). Moreover, we think that

FG(t) is convex on the interval (1,τ1(G)).

- 7.3 The second distance β∗(G) There are two interesting questions about β∗(G):


- (1) What is the range of β∗(G)?
- (2) Can β∗(G1) = β∗(G2) for distinct G1 and G2? For the second question the answer is positive. Let σ be a collection of positive integers


n1,...,nm with m > 1. We denote

|σ| := n1 + ... + nm. Let K¯σ := K¯n

1,...,nm, where K¯n

1,...,nm is the graph complement of the complete m–partite graph Kn

1,...,nm. In other words, K¯σ is the disjoint union of cliques of sizes n1,...,nm. Einhorn and Schoenberg [12] proved that

dimE2(K¯σ) = |σ| − 1. Moreover, the converse statement is also true. If for a graph G on n vertices we have dimE2(G) = n − 1, then G is K¯σ for some σ with |σ| = n.

Let σ1 = (1,1,1), σ2 = (2,2) and σ3 = (1,4). Then β∗(σi) = √3 for i = 1,2,3. Another example,

σ = (1,1,1,1,1), (2,2,2), (4,4), (2,8), (1,16). For all these collections β∗(σ) = 5/2.

It is an interesting problem to describe sets of collections σ with the same β∗(σ).

#### 7.4 Sets of Type II

In Section 4 we consider join–indecomposable spherical sets of Type I and II. Note that if we remove a point from a J–prime set of Type I, then we obtain a set of Type II. It is not clear can we use this method to obtain all sets of Type II? In other words,

Is it true that any J–prime set of Type II is a subset of a set of Type I? Now we consider generalizations of graph representations.

#### 7.5 Spherical representations with R(G) ≤ R0

Let f be a spherical representation of a graph G on n vertices in Rd as a two–distance set with a = 1 and b > a. Let R0 be a positive real number. We say that f is a minimal spherical representations with R(G) ≤ R0 if the image f(G) lies in a sphere of radius R ≤ R0 with the smallest d. If G = Kn, then Theorem 4.2 yields the existence of such representations with d ≤ n − 1. We denote the minimum dimension d by dimS2(G,R0).

Note that dimS2(G,1/√2) = dimJ2(G). It is easy to see that for R0 ≥ 1/√2 we have dimJ2(G) ≥ dimS2(G,R0) ≥ dimS2(G).

The following theorem can be proved by the same arguments as in the proof of Theorem

- 4.3. Theorem 7.1. Let G = Kn be a graph on n vertices. Let R0 ≥ 1/√2. If R(G) ≤ R0, then


dimS2(G,R0) = n − µ(G) − 1, otherwise dimS2(G,R0) = n − 1.

Since in Theorem 4.3 we have dimJ2(G) = dimS2(G) this theorem also holds for dimS2(G,R0). Consider interesting problem: Find families of graphs G with dimS2(G,R0) = dimS2(G).

Another interesting question is to ﬁnd the minimum R0 such that dimS2(G,R0) = dimS2(G) for all G. In particular, is it true that this equality holds for R0 = 1? (See Subsection 7.1.)

#### 7.6 Representations of colored E(Kn) as s–distance sets

First consider an equivalent deﬁnition of graph representations. Let G = (V (G),E(G)) be a graph on n vertices. We have E(Kn) = E(G) ∪ E(G¯). Then it is can be considered as a coloring of E(Kn) in two colors. Hence

E(Kn) = E1 ∪ E2, where E1 ∩ E2 = ∅. Clearly, G is uniquely deﬁned by the equation E(G) = E1.

Let L(e) := i if e ∈ Ei. Then L : E(Kn) → {1,2} is a coloring of E(Kn). A representation L as a two–distance set is an embedding f of V (Kn) into Rd such that dist(f(u),f(v))) = ai for [uv] ∈ Ei. Here a2 ≥ a1 > 0.

This deﬁnition can be extended to any number of colors. Let L : E(Kn) → {1,...,s} be a coloring of the set of edges of a complete graph Kn. Then

E(Kn) = E1 ∪ ... ∪ Es, Ei := {e ∈ E(Kn) : L(e) = i}.

We say that an embedding f of the vertex set of Kn into Rd is a Euclidean representation of a coloring L in Rd as an s–distance set if there are s positive real numbers a1 ≤ ... ≤ as such that dist(f(u),f(v))) = ai if and only if [uv] ∈ Ei.

It is easy to extend the deﬁnitions of polynomials CG(t) and MG(t) for s–distance sets. In this case we have multivariate polynomials CL(t2,...,ts) and ML(t2,...,ts), where a1 = 1 and ti = a2i for i = 2,...,s. It is clear that a Euclidean representation of L is spherical only if FL(t2,...,ts) is well deﬁned, where

1 2

FL(t2,...,ts) := −

ML(t2,...,ts) CL(t2,...,ts)

.

We think that the Einhorn–Schoenberg theorem and several results from this paper can be generalized for representations of colorings L as s–distance sets.

#### 7.7 Contact graph representations of G

The famous circle packing theorem (also known as the Koebe–Andreev–Thurston theorem) states that for every connected simple planar graph G there is a circle packing in the plane whose contact graph is isomorphic to G. Now consider representations of a graph G as the contact graph of a packing of congruent spheres in Rd. Equivalently, the contact graph can be deﬁned in the following way.

Let X be a ﬁnite subset of Rd. Denote ψ(X) := min

{dist(x,y)}, where x = y.

x,y∈X

The contact graph CG(X) is a graph with vertices in X and edges (x,y), x,y ∈ X, such that dist(x,y) = ψ(X). In other words, CG(X) is the contact graph of a s packing of spheres of diameter ψ(X) with centers in X.

Let a graph G = (V,E) on n vertices have at least one edge. Let f be a Euclidean representation of vertices of G in Rd. We say that f with minimum d is a minimal Euclidean contact graph representation if G is isomorphic to CG(X), where X = f(V ). If X lies on a sphere then we call f a minimal spherical contact graph representation.

There are several combinatorial properties of contact graphs, see the survey paper [7]. For instance, the degree of any vertex of CG(X), X ⊂ Rd, is not exceed the kissing number kd. For spherical contact graph representations in S2 this degree is not greater than ﬁve. Using this and other properties of CG(X) we enumerated spherical irreducible contact graphs for n ≤ 11 [20, 21].

It is an interesting problem to ﬁnd minimal dimensions of Euclidean and spherical contact graph representations of graphs G. Acknowledgment. I am very grateful to the reviewers of this paper for their great help in improving the text and helpful comments.

### References

- [1] A. V. Akopyan and A. S. Tarasov. A constructive proof of Kirszbraun’s theorem. Math. Notes, 84:5, 725–728, 2008.
- [2] V. Alexandrov. An analogue of a theorem of van der Waerden, and its application to two–distance preserving mappings. Periodica Math. Hungarica, 72(2):252–257, 2016.
- [3] E. Bannai, E. Bannai, and D. Stanton. An upper bound for the cardinality of an s-distance subset in real euclidean space, ii. Combinatorica, 3(2):147–152, 1983.
- [4] A. Barg and O. R. Musin, Codes in spherical caps. Advances in Math. of Communication, 1(1): 131–149, 2007.


- [5] A. Barg and W. H. Yu. New bounds for spherical two–distance sets. Experimental Math., 22(2):187–194, 2013.
- [6] M. Berger. Geometry I. Universitext. Springer-Verlag, Berlin, 1987.
- [7] K. Bezdek and S. Reid. Contact graphs of unit sphere packings revisited. J. Geom., 104(1): 57–83, 2013.
- [8] A. Blokhuis. Few–Distance Sets, volume 7 of CWI Tracts. CWI, 1984.
- [9] P. Delsarte, J. M. Goethals, and J. J. Seidel. Spherical codes and designs. Geometriae Dedicata, 6(3):363–388, 1977.
- [10] M.M. Deza and M. Laurent. Geometry of Cuts and Metrics, Springer, Berlin, 1997.
- [11] M.M. Deza and E. Deza. Encyclopedia of Distances, Springer, Berlin, 2009.
- [12] S. J. Einhorn and I. J. Schoenberg. On Euclidean sets having only two distances between points. I, II. Nederl. Akad. Wetensch. Proc. Ser. A 69=Indag. Math., 28:479–488, 489– 504, 1966.
- [13] A. Glazyrin and W.–H. Yu, Upper bounds for s–distance sets and equiangular lines, preprint available at arXiv:1611.09479
- [14] M. D. Kirszbraun. Uber¨ die zusammenziehende und Lipschitzsche Transformationen. Fund. Math., 22:77–108, 1934.
- [15] W. Kuperberg. Optimal arrangements in packing congruent balls in a spherical container. Discrete Comput. Geom., 37(2): 205–212, 2007.
- [16] P. Lisonˇek. New maximal two–distance sets. J. Comb. Theory, Ser. A, 77(2):318–338, 1997.
- [17] O. R. Musin. The kissing number in four dimensions. Ann. of Math., 168 (1): 1–32,

- 2008.

[18] O. R. Musin. Spherical two–distance sets. J. Comb. Theory, Ser. A, 116(4): 988–995,

- 2009.


- [19] O. R. Musin. Towards a proof of the 24-cell conjecture, Acta Math. Hungar., 155 (1): 184–199, 2018.
- [20] O. R. Musin and A. S. Tarasov, Enumeration of irreducible contact graphs on the sphere. J. Math. Sci., 203(6): 837–850, 2014.
- [21] O. R. Musin and A. S. Tarasov, Extreme problems of circle packings on a sphere and irreducible contact graphs. Proc. Steklov Inst. Math., 288: 117–131, 2015.


- [22] H. Nozaki and M. Shinohara. A geometrical characterization of strongly regular graphs. Linear Algebra and Appl., 437(3): 2587–2600, 2012.
- [23] R.A. Rankin, The closest packing of spherical caps in n dimensions. Proc. Glasgow Math. Assoc., 2: 139–144, 1955.
- [24] A. Roy. Minimal Euclidean representation of graphs. Discrete Math., 310(4): 727–733, 2010.
- [25] F. Szo¨ll¨osi. The two–distance sets in dimension four, arXiv:1806.07861
- [26] W.–H. Yu, New bounds for equiangular lines and spherical two–distance sets, preprint available at arXiv:1609.01036.


O. R. Musin, School of Mathematical and Statistical Sciences, University of Texas Rio Grande Valley, One West University Boulevard, Brownsville, TX, 78520.

E-mail address: oleg.musin@utrgv.edu

