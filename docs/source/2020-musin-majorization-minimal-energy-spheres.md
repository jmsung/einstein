---
type: source
kind: paper
title: Majorization and minimal energy on spheres
authors: Oleg R. Musin
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2001.04067v4
source_local: ../raw/2020-musin-majorization-minimal-energy-spheres.pdf
topic: general-knowledge
cites:
---

# Majorization and minimal energy on spheres

arXiv:2001.04067v4[math.MG]24Mar2021

Oleg R. Musin

Abstract

In the present paper, we consider the majorization theorem (also known as Karamata’s inequality) and the respective minima of the majorization (the so-called M-sets) for fenergy potentials of m-point conﬁgurations on the unit sphere. In particular, we show the optimality of regular simplexes, describe some M-sets of small cardinality, deﬁne and discuss spherical f-designs.

Keywords: Majorization inequality, optimal spherical conﬁgurations, spherical designs

## 1 Introduction

Let A = (a1, . . ., an) be an arbitrary sequence of real numbers. Let A↑ = (a(1), . . ., a(n)) denote the sequence obtained from A by arranging its elements in the non-decreasing order: a(1) ≤ a(2) ≤ . . . ≤ a(n).

Given two sequences A = (a1, . . ., an) and B = (b1, . . ., bn), we say that A majorizes B, and write A ⊲ B if the following conditions are fulﬁlled:

a(1) + . . . + a(k) ≥ b(1) + . . . + b(k), k = 1, . . ., n. Remark. Note that in [17] and [22] this condition is called a weak majorization.

The main theorem in the theory of majorization is the majorization (or Karamata) inequality (see details in [17, 22]). Here, we shall consider its “weak” version. Theorem (The majorization theorem). Let f(x) be a convex decreasing function, and let A = (a1, . . ., an), B = (b1, . . ., bn) be two sequences. Then if A ⊲ B, we have

- f(a1) + . . . + f(an) ≤ f(b1) + . . . + f(bn). (1.1)

Moreover, A ⊲ B if and only if for all convex decreasing functions g we have

- g(a1) + . . . + g(an) ≤ g(b1) + . . . + g(bn).


Provided f(x) is strictly convex, the inequality (1.1) turns into equality if and only if we have A↑ = B↑.

Let P be a set of sequences of length n. We say that A ∈ P is an M-set if for any B ∈ P either A ⊲ B or A and B are incomparable. Let M(P) denote the set of all M-sets in P.

Suppose that f(x) be a strictly convex decreasing function, and deﬁne Ef(A) := f(a1) + . . . + f(an), A = (a1, . . ., an).

Then the majorization theorem readily implies that if Ef achieves its minimum at some A ∈ P, then A ∈ M(P).

Let S be a set and ρ : S × S → R be a symmetric function. Let X be a subset of S of cardinality m (or, shortly, an m-subset). Denote by Rρ(X) the set of values of ρ(a, b) over all unordered pairs (a, b) of elements in X. Then we have the following generalization of the majorization theorem (Theorem 2.1):

Theorem. Let X and Y be two m-subsets of S. Suppose Rρ(X) ⊲ Rρ(Y ). Then for every convex decreasing function f we have Ef(X) ≤ Ef(Y ).

Now, let us put P = {Rρ(X)}, where X ⊂ S is an m-subset. Then we deﬁne M(S, ρ, m) = M(P) and discuss its properties further in Section 2. Our main interest is the case when S is the standard unit sphere Sn−1 in Rn. In particular, we prove that on the unit circle

- S1 with angular distance ρ = ϕ, the M-sets are vertex sets of regular polygons (Theorem 3.2). We also show that M(Sn−1, ρ, n+1) consists of vertices of regular simplices, for ρ being the standard Euclidean distance squared (Theorem 4.1), and describe some small M-sets, and some are left as open problems, depending on the “distance fucntional” ρ. In Section 6 we deﬁne spherical f-design and study their properties. Then we discuss possible relations between the notions of f-designs and M-sets (Theorem 6.2), τ-designs, and two-distance sets.


## 2 M-sets and minimums of potential energy

- Let S be an arbitrary set, and ρ : S × S → D ⊂ R be any symmetric function. Then for a given convex decreasing function f : D → R and for every ﬁnite subset X = {x1, . . .xm} ⊂ S we deﬁne the potential energy Ef(X) of X with respect to f as


f(ρ(xi, xj)).

Ef(X) :=

1≤i<j≤m

In this paper we consider the following minimum energy problem. Generalized Thomson’s Problem. For S, ρ, f and m given, ﬁnd all X ∈ Sm = S ×...×S such that Ef(X) is the minimum of Ef over the set of all m-subsets of S.

Let Rρ(X) denote the set of all ρ(xi, xj), where 1 ≤ i < j ≤ m, i.e.

Rρ(X) := {ρ(x1, x2) . . ., ρ(x1, xm), . . ., ρ(xm−1, xm)}. Then the majorization theorem implies

- Theorem 2.1. Let X and Y be two m-subsets of S. Suppose Rρ(X) ⊲ Rρ(Y ). Then for every decreasing and convex function f we have Ef(X) ≤ Ef(Y ).

Note that ⊲ deﬁnes a partial order on Sm. Let X and Y be two m-subsets of S, such that Rρ(X) = Rρ(Y ). Then we have one of three following cases: either Rρ(X) ⊲ Rρ(Y ), or Rρ(Y ) ⊲ Rρ(X), or Rρ(X) and Rρ(Y ) are incomparable. Now we deﬁne the maximal subsets of the poset (Sm, ⊲).

- Deﬁnition 2.1. We say that X ∈ Sm is an M-set in S with respect to ρ if for any Y ∈ Sm

we have that either Rρ(X) ⊲ Rρ(Y ), or Rρ(X) and Rρ(Y ) are incomparable. Let M(S, ρ, m) denote the set of all M–sets in S of cardinality m.

- Deﬁnition 2.2. Let f : D → R be a convex decreasing function. Let Vf = infY∈Sm Ef(Y ). Let Mf(S, ρ, m) denote the set of all X ∈ Sm such that Ef(X) = Vf.


- Theorem 2.2. Let S be a compact topological space and ρ : S × S → D ⊂ R be a symmetric continuous function. Let f : D → R be a strictly convex decreasing function. Then Mf(S, ρ, m) is non-empty and Mf(S, ρ, m) ⊆ M(S, ρ, m).

Proof. Since S is compact, there is X ∈ Sm such that Ef(X) = Vf, i.e. Mf(S, ρ, m) = ∅. The majorization theorem yields that for all Y ∈ Sm we have either Rρ(X) ⊲ Rρ(Y ) or Rρ(X) and Rρ(Y ) are incomparable. Indeed, if X, Y ∈ Mf(S, ρ, m) while Rρ(X) and Rρ(Y ) are comparable, then Rρ(X) = Rρ(Y ). This means that X is an M–set.

![image 1](<2020-musin-majorization-minimal-energy-spheres_images/imageFile1.png>)

![image 2](<2020-musin-majorization-minimal-energy-spheres_images/imageFile2.png>)

![image 3](<2020-musin-majorization-minimal-energy-spheres_images/imageFile3.png>)

![image 4](<2020-musin-majorization-minimal-energy-spheres_images/imageFile4.png>)

Remark. I am very grateful to one of the reviewers who pointed out an inaccuracy in the previous version of the manuscript. Namely, if we do not require f be strictly convex, then the following counterexample shows that Theorem 2.2 cannot hold.

Let S = S1, ρ = ϕ, where ϕ is the angular (geodesic) distance, and f(t) = −t. Clearly, f is convex and decreasing, though not strictly convex. It is easy to see that Mf(S1, ϕ, m), for m even, contains all centrally symmetric sets X in S1. However, M(S1, ϕ, m) consists of the vertices of regular m–gons inscribed in S1, see Theorem 3.2. Obviously, Mf(S1, ϕ, m)

M(S1, ϕ, m).

- Theorem 2.3. Let ρ : S ×S → D ⊂ R be a symmetric function and h : D → R be a convex increasing function. Then M(S, ρ, m) ⊆ M(S, h(ρ), m).


Proof. Assume the contrary. Then there exist X ∈ M(S, ρ, m) and Y ⊂ S, |Y | = m, such that

Rh(ρ)(Y ) ⊲ Rh(ρ)(X).

Note that f = −h−1 is a convex decreasing function, and the majorization theorem yields Rρ(Y ) ⊲ Rρ(X). The latter contradicts our assumption that X ∈ M(S, ρ, m).

![image 5](<2020-musin-majorization-minimal-energy-spheres_images/imageFile5.png>)

![image 6](<2020-musin-majorization-minimal-energy-spheres_images/imageFile6.png>)

![image 7](<2020-musin-majorization-minimal-energy-spheres_images/imageFile7.png>)

![image 8](<2020-musin-majorization-minimal-energy-spheres_images/imageFile8.png>)

In this paper we consider the case when S is the standard unit sphere Sn−1 in Rn. There are two natural distances on Sn−1: the Euclidean distance r and the angular distance ϕ. Here r(x, y) denotes the Euclidian distance ||x−y|| between two points x, y ∈ Sn−1, while ϕ(x, y) denotes the angular distance in Sn−1, i.e. ϕ(x, y) = 2 arcsin(||x − y||/2).

- Deﬁnition 2.3. For s ∈ R deﬁne the function


 

rs(x, y), if s > 0; log r(x, y), if s = 0; −rs(x, y), if s < 0.

rs(x, y) :=



- Corollary 2.1. The following inclusions hold:

- (i) M(Sn−1, rs, m) ⊆ M(Sn−1, rt, m), for all t ≥ s;
- (ii) M(Sn−1, rs, m) ⊆ M(Sn−1, ϕ, m), for all s ∈ (−∞, 1].


Proof. Let h(x) = xt/s, x > 0. Then h(x) is a convex increasing function for all t > s > 0. Since rt = h(rs), Theorem 2.3 implies (i) for s > 0. The functions h(x) = esx, s > 0, x > 0, and h(x) = log(−x)/s, s < 0, x < 0, prove the inclusions

M(Sn−1, r0, m) ⊆ M(Sn−1, rs, m), s > 0, and M(Sn−1, rs, m) ⊆ M(Sn−1, r0, m), s < 0.

The remaining case s < t < 0 in (i) follows from the fact that h(x) = (−x)s/t, x < 0, is a convex increasing function in x. It is clear that h(x) = arcsin(x/2), x ∈ [0, 2], is a convex increasing function in x. Then Theorem 2.3 also yields (ii).

![image 9](<2020-musin-majorization-minimal-energy-spheres_images/imageFile9.png>)

![image 10](<2020-musin-majorization-minimal-energy-spheres_images/imageFile10.png>)

![image 11](<2020-musin-majorization-minimal-energy-spheres_images/imageFile11.png>)

![image 12](<2020-musin-majorization-minimal-energy-spheres_images/imageFile12.png>)

Let X = {p1, . . ., pm} be an m–subset of Sn−1 that consists of distinct points. Then the Riesz t-energy of X is given by

Et(X) :=

i<j

1 ||pi − pj||t

![image 13](<2020-musin-majorization-minimal-energy-spheres_images/imageFile13.png>)

, for t > 0, and E0(X) :=

i<j

log

1 ||pi − pj||

![image 14](<2020-musin-majorization-minimal-energy-spheres_images/imageFile14.png>)

. (2.1)

Note that for t = 0 minimizing Et is equivalent to maximizing

i =j

||pi − pj||), which is

Smale’s 7th problem [29]. For t = 1 we obtain the Thomson problem, and for t → ∞ the minimum Riesz energy problem transforms into the Tammes problem.

Theorem 2.2 and Corollary 2.1 yield:

- Corollary 2.2. Let t ≥ 0. If X ⊂ Sn−1 gives the minimum of Et in the set of all m-subsets of Sn−1, then X ∈ M(Sn−1, rs, m) for all s > −t.


## 3 Minima of majorizations

Let f be a convex function on R. Let x1, . . ., xn be a sequence of real numbers and x¯ :=

- (x1 + . . . + xn)/n. The Jensen inequality states that

f(¯x) ≤

f(x1) + ... + f(xn) n

![image 15](<2020-musin-majorization-minimal-energy-spheres_images/imageFile15.png>)

. If y ≥ x¯, then it is easy to see that we have

(y, . . ., y) ⊲ (x1, . . ., xn). (3.1) Then the majorization theorem yields Jensen’s inequality for a convex decreasing f:

f(y) ≤

f(x1) + ... + f(xn) n

![image 16](<2020-musin-majorization-minimal-energy-spheres_images/imageFile16.png>)

.

In this section we extend the above inequality. First, we deﬁne a sequence Y (T) :=

- (y1, . . ., ym) for any sequence of m real numbers T, as follows. Deﬁnition 3.1. Let T = (T1, . . ., Tm), with T1 ≤ . . . ≤ Tm. Let


- y1(T) := min

k=1,...,m

Tk k

![image 17](<2020-musin-majorization-minimal-energy-spheres_images/imageFile17.png>)

,

- y2(T) := min


Tk − y1(T) k − 1

,

![image 18](<2020-musin-majorization-minimal-energy-spheres_images/imageFile18.png>)

k≥2

. . . ym(T) := Tm − y1(T) − . . . − ym−1(T),

Y (T) := (y1(T), . . ., ym(T)). Let a sequence A = (a1, . . ., am) be such that

a(1) + . . . + a(i) ≤ Ti, for all i = 1, . . ., m, and P(T1, . . ., Tm) denote the set of all such sequences. Lemma 3.1. If T1 ≤ . . . ≤ Tm and A ∈ P(T1, . . ., Tm), then Y (T1, . . ., Tm) ⊲ A, i.e. Y (T1, . . ., Tm) is the only maximum element in P(T1, . . ., Tm). Proof. Let A ∈ P(T1, . . ., Tn). A proof immediately follows from the following inequalities:

Tk k

a(1) ≤

for all k = 1, . . ., m and

![image 19](<2020-musin-majorization-minimal-energy-spheres_images/imageFile19.png>)

Tk − a(1) − . . . − a(i−1) k − i + 1

a(i) ≤

for all k ≥ i > 1.

![image 20](<2020-musin-majorization-minimal-energy-spheres_images/imageFile20.png>)

![image 21](<2020-musin-majorization-minimal-energy-spheres_images/imageFile21.png>)

![image 22](<2020-musin-majorization-minimal-energy-spheres_images/imageFile22.png>)

![image 23](<2020-musin-majorization-minimal-energy-spheres_images/imageFile23.png>)

![image 24](<2020-musin-majorization-minimal-energy-spheres_images/imageFile24.png>)

Notation. Given S, ρ, n, and X ⊂ S with |X| = n, let m := n(n − 1)/2, and

Qρ(X) := (Rρ(X))↑, (q1, . . ., qm) := Qρ(X), Skρ(X) := q1 + . . . + qk, k = 1, . . ., m. Note that Lemma 3.1, Theorem 2.1 and (3.1) combined yield the following theorem.

- Theorem 3.1. Let S be a set and ρ : S × S → D ⊂ R be a symmetric function. Let

T = (T1, . . ., Tm), where m = n(n − 1)/2, be a sequence of real numbers with T1 ≤ . . . ≤ Tm such that all yi(T) ∈ D. Suppose that X ⊂ S with |X| = n satisﬁes

Skρ(X) ≤ Tk, k = 1, . . ., m. Then Y (T) ⊲ Rρ(X), and for every convex decreasing function f : D → R we have Ef(X) ≥ f(y1(T)) + . . . + f(ym(T)).

In particular, if there is y ∈ D such that Tk = ky, for all k = 1, ..., m, then yk(T) = y, for all k = 1, ..., m, and we have Ef(X) ≥ mf(y). Remark. In the latter case, the inequality Ef(X) ≥ mf(y) is just Jensen’s inequality.

Now let us consider the case of the unit circle S = S1 with angular distance ρ = ϕ.

- Theorem 3.2. Up to isometry, there exists a unique M-set of cardinality n in the unit circle S1 with ρ = ϕ: the vertices of a regular n-gon inscribed in S1. In other words, M(S1, ϕ, n) consists of the vertices of regular polygons.


Proof. Let X = {p1, . . ., pn} ⊂ S1 and pn+i := pi for all integer i > 0. We obviously have

n

ϕ(pi, pi+1) ≤ 2π,

i=1

where the equality holds only if |∠piOpi+1| = ϕ(pi, pi+1) for all i. Moreover, we have

n

ϕ(pi, pi+k) ≤ 2πk, k = 1, 2, .., ⌊n/2⌋.

i=1

Then (3.1) yields

πn,k := (2πk/n, . . ., 2πk/n) ⊲ Rk := (ϕ(p1, pk+1), . . ., ϕ(pn, pk)). It is not hard to see that these inequalities yield

Rϕ(Πn) = πn,1 ∪ . . . ∪ πn,ℓ ⊲ R1 ∪ . . . ∪ Rℓ = Rϕ(X), where ℓ = ⌊n/2⌋ and Πn is the set of vertices of a regular n-gon in S1.

![image 25](<2020-musin-majorization-minimal-energy-spheres_images/imageFile25.png>)

![image 26](<2020-musin-majorization-minimal-energy-spheres_images/imageFile26.png>)

![image 27](<2020-musin-majorization-minimal-energy-spheres_images/imageFile27.png>)

![image 28](<2020-musin-majorization-minimal-energy-spheres_images/imageFile28.png>)

This theorem implies that M(S1, r1, n) consists of the vertices of regular polygons. However, the set M(S1, r2, n), n ≥ 4, is much larger. In fact (see Section 5), M(S1, r2, 4) consists of the vertices of quadrilaterals with side lengths 2π − 3α, α, α, α (in the angular measure), where π/2 ≤ α ≤ 2π/3.

## 4 Optimal simplices and constrained (n + k)-sets

First we show that Jensen’s inequality for (n + 1)-sets on Sn−1 yields optimality of regular simplices.

- Theorem 4.1. Let s ≤ 2. Then M(Sn−1, rs, n + 1) consists of regular simplices. Proof. Let X = {p1, . . ., pm} ⊂ Sn−1 and ti,j := pi · pj. Then


2

m

≥ 0. (4.1)

pi

ti,j =

i=1

i,j

Since ti,i = pi · pi = 1, we have

ti,j ≥ −m.

i =j

It is easy to see that r2(x, y) = ||x − y||2 = 2 − 2x · y, x, y ∈ Sn−1. Then

r2(pi, pj) =

i<j

(2 − 2ti,j) ≤ m2.

i<j

Therefore, by (3.1) we have

2m m − 1

.

(am, . . ., am) ⊲ Rr

(X), for am :=

![image 29](<2020-musin-majorization-minimal-energy-spheres_images/imageFile29.png>)

2

Note that for m = n + 1, the side lengths of a regular n-simplex are equal to √am. This completes the proof.

![image 30](<2020-musin-majorization-minimal-energy-spheres_images/imageFile30.png>)

![image 31](<2020-musin-majorization-minimal-energy-spheres_images/imageFile31.png>)

![image 32](<2020-musin-majorization-minimal-energy-spheres_images/imageFile32.png>)

![image 33](<2020-musin-majorization-minimal-energy-spheres_images/imageFile33.png>)

![image 34](<2020-musin-majorization-minimal-energy-spheres_images/imageFile34.png>)

An open problem. The set MnS := M(Sn−1, ϕ, n + 1), n ≥ 3, is not as simple to describe as in the case ρ = r2. For example, consider the case n = 3. Let us deﬁne a two-parametric family of tetrahedra ABCD in S2. Let the opposite edges AC and BD of ABCD be of equal length and the angle between them be θ. Let X be the midpoint of AC and Y be the midpoint of BD. Suppose that X, Y and O, which is the center of S2, are collinear. Then ABCD is uniquely (up to isometry) deﬁned by the parameters a = |OX| = |OY | and θ. Let ∆a,θ denote such a tetrahedron ABCD. Note that ∆0,π/2 is a square inscribed into the unit circle, while ∆1/√3,π/2 is a regular tetrahedron.

![image 35](<2020-musin-majorization-minimal-energy-spheres_images/imageFile35.png>)

We conjecture that M3S consists of the vertices of all tetrahedra ∆a,θ, for a ∈ [0, 1/√3] and 0 < θ ≤ π/2.

![image 36](<2020-musin-majorization-minimal-energy-spheres_images/imageFile36.png>)

More generally, it is an interesting problem to ﬁnd MnS for all n.

Now let us apply Theorem 4.1 to P ⊂ Sn−1, with n+2 ≤ |P| ≤ 2n. Davenport and Hajo´s [10], and, independently, Rankin [26] proved that if P is a subset of Sn−1 with |P| ≥ n + 2, then the minimum distance between the points in P is at most √2. For the case |P| = 2n,

![image 37](<2020-musin-majorization-minimal-energy-spheres_images/imageFile37.png>)

Rankin proved that P is a regular cross-polytope. Later on, Wlodzimierz Kuperberg [19] extended this theorem.

Kuperberg’s theorem. Let P be a (n+k)-point subset of the unit n-ball Bn with 2 ≤ k ≤ n such that the minimum distance between points in P is at least √2. Then:

![image 38](<2020-musin-majorization-minimal-energy-spheres_images/imageFile38.png>)

- (1) every point of P lies on the boundary of Bn; and
- (2) Rn splits into the orthogonal product ki=1 Li of nondegenerate linear subspaces Li such that for Si := P ∩ Li we have |Si| = di + 1 and rank(Si) = di (i = 1, 2, ..., k), where di := dim Li.


With this above fact in mind, let us extend Deﬁnition 2.1. Let S ⊂ Rn and ρ : S ×S → R be a symmetric function. Then, let Ω = Ω(S, ρ, q0, m) denote the set of all X ⊂ S of cardinality m, such that for all distinct points x, y ∈ X we have ||x − y|| ≥ q0. Finally, let M(S, ρ, q0, m) denote the set of all X in Ω such that for any Y ∈ Ω either Rρ(X) ⊲ Rρ(Y ), or X and Y are incomparable.

- Theorem 4.2. Let 2 ≤ k ≤ n and s ≤ 2. Then M(Bn, rs, √2, n+k) = M(Sn−1, rs, √2, n+k) and this set consists of k mutuallu orthogonal regular di-simplices Si, such that all di ≥ 1 and d1 + ... + dk = n.


![image 39](<2020-musin-majorization-minimal-energy-spheres_images/imageFile39.png>)

![image 40](<2020-musin-majorization-minimal-energy-spheres_images/imageFile40.png>)

Proof. By Kuperberg’s theorem, we obtain that if P ∈ M(Bn, rs, √2, n + k), then (1) P ⊂ Sn−1 and (2) P consists of mutually orthogonal di-simplices Si. By Theorem 4.1, all Si have to be regular.

![image 41](<2020-musin-majorization-minimal-energy-spheres_images/imageFile41.png>)

![image 42](<2020-musin-majorization-minimal-energy-spheres_images/imageFile42.png>)

![image 43](<2020-musin-majorization-minimal-energy-spheres_images/imageFile43.png>)

![image 44](<2020-musin-majorization-minimal-energy-spheres_images/imageFile44.png>)

![image 45](<2020-musin-majorization-minimal-energy-spheres_images/imageFile45.png>)

Remarks.

- 1. From Rankin’s theorem [26] it follows that Ω(Sn−1, rs, √2, 2n) contains only regular cross-polytopes. However, if 2 ≤ k < n−1 then Ω(Sn−1, rs, √2, n+k) contains inﬁnitely many non-isometric point sets P of several combinatorial types. For instance, if k = 2

![image 46](<2020-musin-majorization-minimal-energy-spheres_images/imageFile46.png>)

![image 47](<2020-musin-majorization-minimal-energy-spheres_images/imageFile47.png>)

and n = 4 then the respective dimensions (d1, d2), as deﬁned in the statement of Kuperberg’s theorem, can be (1, 3) or (2, 2).

- 2. An interesting open problem is to ﬁnd M(Sn−1, rs, n + k). Even for the case k = 2, n = 3 this seems a rather complicated task, see the discussion in Section 5.3.
- 3. Recently, in our joint paper with Peter Dragnev [15], we enumerated and classiﬁed all stationary logarithmic conﬁgurations of n + 2 points in Sn−1. In particular, we showed that the logarithmic energy attains its relative minima at conﬁgurations that consist of two mutually orthogonal regular simplices. Actually, these conﬁgurations are the same as in Theorem 4.2 for k = 2.


Now, let k ∈ [2, n]. Then, our conjecture is that the logarithmic energy of n+k points in Sn−1 attains its relative minima at conﬁgurations that consist of k mutually orthogonal regular simplices. So far this conjecture remains open for k = 3, ..., n − 1.

## 5 Spherical M-sets of small cardinality

In this section we consider spherical M-sets of cardinality m ≤ 5. Clearly, for any S and ρ the case m = 2 is trivial: M(S, ρ, 2) consists of pairs (x, y) such that ρ(x, y) attains its maximum on S × S. However, the structure of M-sets for m > 2 is not so simple.

### 5.1 Spherical three-point M-sets

Theorems 3.2 and 4.1 yield that M(S1, ϕ, 3) and M(S1, r2, 3) contain only the vertices of regular triangles. Let us now investigate M(S1, rs, 3) for all s.

Consider the equation

(1 − t)z + 2z−1(1 − t2)z =

3 2

![image 48](<2020-musin-majorization-minimal-energy-spheres_images/imageFile48.png>)

z+1

, z =

s 2

. (5.1)

![image 49](<2020-musin-majorization-minimal-energy-spheres_images/imageFile49.png>)

For all s, this equation has a solution t = −1/2. It can be shown that if

4 > s ≥ s0 := log4/3 (9/4) ≈ 2.8188, then (5.1) has one more solution ts ∈ (−1, −1/2). Note that

= −1, t4 = −1/2, and ts is increasing on the interval [s0, 4] as a function of s.

ts

0

- Theorem 5.1. The following cases hold for M := M(S1, rs, 3):


- 1. if s ≤ log4/3 (9/4), then M contains only vertices of regular triangles;
- 2. if log4/3 (9/4) < s < 4, then M consists of the vertices of regular triangles and triangles with angular side lengths α, α, 2π − 2α, where α ∈ (arccos(ts), π];
- 3. if s ≥ 4, then M consists of the vertices of regular triangles and triangles with angular side lengths α, α, 2π − 2α, α ∈ [2π/3, π].


Proof. Suppose that we have a triangle T inscribed in the unit circle S1 with angles u1, u2, u3 and (Euclidean) side lengths x1, x2, x3, where u1 + u2 + u3 = π. Moreover, we assume that u1 ≥ u2 ≥ u3.

First, let us show that if T is an M-set with ρ = rs, then u1 = u2. Indeed, ﬁx u3 so that x3 = √2 − 2 cos2u3 is also ﬁxed. Then we have to maximize the function

![image 50](<2020-musin-majorization-minimal-energy-spheres_images/imageFile50.png>)

F(u1, u2) := xs1 + xs2 subject to u1 + u2 = π − u3.

If u3 = 0, then we obviously have u1 = u2 = π/2. Assume that u3 > 0. By the law of sines we get

x3 sinu3

x1 = c sinu1, x2 = c sinu2, c :=

. Then

![image 51](<2020-musin-majorization-minimal-energy-spheres_images/imageFile51.png>)

F(u1, u2) = cs(sins u1 + sins u2).

The method of Lagrange multipliers gives the equality sin u1 = sinu2 that under our constraints yields u1 = u2.

Now, for T, we have that u1 = u2 = u and u3 = π − 2u. Therefore, fs(t) := (xs1 + xs2 + xs3)/2z+1 = (1 − t)z + 2z−1(1 − t2)z, t := cos2u.

Note that (5.1) is the equation fs(t) = fs(−1/2). Since u ∈ [π/3, π/2], we have t ∈ [−1, −1/2]. It not hard to see that fs(t) ≤ fs(−1/2) for 0 < s ≤ log4/3 (9/4) and all t; if log4/3 (9/4) < s < 4, then fs(t) ≤ fs(−1/2) for t ∈ [ts, −1/2]; and if s ≥ 4 and t ∈ [−1, −1/2), then fs(t) > fs(−1/2). These observations complete the proof.

![image 52](<2020-musin-majorization-minimal-energy-spheres_images/imageFile52.png>)

![image 53](<2020-musin-majorization-minimal-energy-spheres_images/imageFile53.png>)

![image 54](<2020-musin-majorization-minimal-energy-spheres_images/imageFile54.png>)

![image 55](<2020-musin-majorization-minimal-energy-spheres_images/imageFile55.png>)

### 5.2 Spherical four-point M-sets

- Theorem 3.2 yields that M(S1, ϕ, 4) contains only vertices of squares. This fact together with Corollary 2.1(ii) imply that M(S1, rs, 4) for s ≤ 1 also contains only vertices of squares.


An interesting open problem is to describe M(S1, rs, 4) for all s. Let us mention that it can be proven that M(S1, r2, 4) consists of the vertices of quadrilaterals inscribed into the unit circle with angular side lengths α, α, α, 2π − 3α, where π/2 ≤ α ≤ 2π/3.

Theorem 4.1 yields that M(S2, rs, 4), with s ≤ 2, contains only vertices of regular tetrahedra. Another interesting problem is to describe what we have for the case s > 2.

### 5.3 Spherical ﬁve-point M-sets

From Theorem 3.2 we obtain that the sets M(S1, ϕ, 5) and M(S1, rs, 5) for s ≤ 1 contain only vertices of regular pentagons.

The triangular bi-pyramid (or TBP, for short) is the conﬁguration of 5 points in S2 placed as follows: one point at the North pole, another one at the South pole, while the remaining three are arranged in an equilateral triangle on the equator. Theorem 4.2 yields that M(S2, rs, √2, 5), s ≤ 2, contains only the TBP. Moreover, the same result holds for M(S2, ϕ, √2, 5). Indeed, from Kuperberg’s theorem it follows that P consists of a 1dimensional simplex S1 that is a pair of antipodal points in S2, say the North and South poles, and a triangle S2 on the equator. By Theorem 3.2 this triangle has to be regular, i.e. P is the TBP.

![image 56](<2020-musin-majorization-minimal-energy-spheres_images/imageFile56.png>)

![image 57](<2020-musin-majorization-minimal-energy-spheres_images/imageFile57.png>)

The last known case is M(S3, rs, 5) with s ≤ 2 that contains only vertices of regular 4-simplices. This follows from Theorem 4.1.

It is an interesting open problem to ﬁnd M(S2, rs, 5). By Corollary 2.2 the global minimizer of the Riesz potential Et of 5 points lies in M(S2, rs, 5) for all s > −t. Then a solution to this problem for some s can help to ﬁnd minimizers of Et for all t > −s. It is proved that the TBP is the minimizer of Et for t = 0 [14], for t = 1, 2 [27], and for t < 15.048 [28]. Note that the TBP is not the global minimizer for Et when t > 15.04081 [23].

## 6 Spherical f-designs

In this section we deﬁne and study spherical f-designs. In particular, we discuss possible relations between f-designs and M-sets, τ-designs, and two-distance sets. Moreover, we extend

- Theorem 4.1 about the optimality of simplices, proving Theorem 6.2 below. Since f-designs are extremal spherical conﬁgurations, we believe that there are more connections between


- them and M-sets.


### 6.1 Deﬁnition of f-design

Since a long time Delsarte’s method (also known in coding theory as the Linear Programming Bound) has been widely used for ﬁnding cardinality bounds for codes (see [9, Chap. 9,13] and [11, 18, 21]). This approach for energy bounds was ﬁrst applied by Yudin [30], then by Cohn and Kumar [8], and recently in [6].

In our case, this method relies on the positive semideﬁnite property of Gegenabauer polynomials Gk(n)(t) that can be deﬁned via the following recurrence formula:

(2k + n − 4) tG(kn−)1 − (k − 1) G(kn−)2 k + n − 3.

G(0n) = 1, G1(n) = t, . . ., G(kn) =

.

![image 58](<2020-musin-majorization-minimal-energy-spheres_images/imageFile58.png>)

Alternatively, {Gk(n)}k can be deﬁned as a family of orthogonal polynomials on the interval [−1, 1], with respect to the weight function ρ(t) = (1 − t2)(n−3)/2.

Let P = {p1, . . ., pm} be a ﬁnite subset of Sn−1, in other words, P is a ﬁnite set of unit vectors. We deﬁne the k-th moment of P as

Mk(P) :=

m

i=1

m

Gk(n)(ti,j), where ti,j := pi · pj = cos(ϕ(pi, pj)).

j=1

It is well–known that Gegenabauer polynomials are positive deﬁnite. A real function f on [−1, 1] is called positive deﬁnite (p.d.) in Sn−1 if for every ﬁnite subset P = {p1, . . ., pm} in Sn−1 the matrix f(ti,j) mi,j=1 is positive semideﬁnite.

The p.d. property of Gegenabauer polynomials yields that

Mk(P) ≥ 0 for all k = 1, 2, ... (6.1) Since G(1n)(t) = t, then the inequality (6.1) for k = 1 gives (4.1).

Let f be a function on [−1, 1] such that its Gegenbauer series ∞k=0 fkG(kn) is well–deﬁned. Throughout this section we assume that this series converges uniformly to f on the whole interval [−1, 1]. Then we can write

∞

fkG(kn)(t) for all t ∈ [−1, 1].

f(t) =

k=0

Note that f is p.d. if and only if all its Gegenbauer coeﬃcients are non–negative: fk ≥ 0. It is easy to see that for any P = {p1, . . ., pm} in Sn−1 we have

m

m

∞

Sf(P) :=

f(ti,j) =

fkMk(P). (6.2)

i=1

j=1

k=0

Deﬁnition 6.1. Let P = {p1, . . ., pm} be a ﬁnite subset of the unit sphere Sn−1. Let D(P) denote the set of all inner products that occur between distinct pi’s in P.

For a given function f(t) = k fk G(kn)(t), we say that P is an f-design if it satisﬁes the following properties:

- 1. for all k > 0 with fk = 0, we have that Mk(P) = 0;
- 2. D(P) ⊂ Zf, where Zf denotes the set of all t ∈ [−1, 1) such that f(t) = 0. For a given f we say that an f-design is of degree d if f is a polynomial of degree d.


Remark. Property (1) in the above deﬁnition is related to linear programming slackness conditions and the concept of harmonic indices [1, 3, 5, 11, 13, 31]. Let K be a subset of N. A subset P ⊂ Sn−1 is called a spherical design of harmonic index K if for all k ∈ K we have Mk(P) = 0.

Property (2) in the above deﬁnition is related to the concept of annihilating polynomial from [21]. Below we show that (2) yields a tight property of harmonic indices.

Note that for some P several degrees are possible. For instance, the cross–polytope is the second degree design with f(t) = t(t + 1). However, it is an f–design of degree 3 with all f(t) = (at + b)t(t + 1)), where ab = 0, see Proposition 6.1.

### 6.2 Delsarte’s bound and f-designs

- Let T be a subset of the interval [−1, 1). A set of points P in Sn−1 of cardinality m is called a T-spherical code if for every pair (x, y) of distinct points in P the inner product x · y ∈ T. We wish to maximize the cardinality m over all T-spherical codes of ﬁxed dimension n. The Delsarte (or linear programing) bound relates this maximization problem to a minimization problem for certain real function f as follows (see [11, 18, 21]):


Let T ⊂ [−1, 1). Let f be a function on [−1, 1] with all fk ≥ 0 such that f(t) ≤ 0 for all t ∈ T. Then for every T-spherical code of cardinality m we have that

mf0 ≤ f(1) (6.3)

There are several known examples of P and T when the inequality (6.3) turns into equality, see [9, 11, 18, 21]. Now we consider f–designs that imply the equality mf0 = f(1). Lemma 6.1. Let f(t) = k fk Gk(n)(t) be a function on [−1, 1].

- 1. If P ⊂ Sn−1 is such that D(P) ⊂ Zf, then Sf(P) = |P| f(1).
- 2. If there is an f-design in Sn−1 of cardinality m, then f(1) = mf0.


Proof. 1. Let P = {p1, . . ., pm} ⊂ Sn−1 with D(P) ⊂ Zf. Then f(ti,j) = 0 for all i = j and we have

Sf(P) = mf(1). (6.4)

2. Let P be an f-design. Since fkMk(P) = 0 for all k > 0 we have Sf(P) =

fkMk(P) = f0M0(P) = f0m2.

k

Thus,

f(1) = mf0. (6.5)

![image 59](<2020-musin-majorization-minimal-energy-spheres_images/imageFile59.png>)

![image 60](<2020-musin-majorization-minimal-energy-spheres_images/imageFile60.png>)

![image 61](<2020-musin-majorization-minimal-energy-spheres_images/imageFile61.png>)

![image 62](<2020-musin-majorization-minimal-energy-spheres_images/imageFile62.png>)

Now we derive some conditions for P to be an f-design.

- Theorem 6.1. Let f(t) = k fk Gk(n)(t) be a function with all fk ≥ 0. Let P ⊂ Sn−1 with |P| = m be such that D(P) ⊂ Zf. Then P is an f-design if and only if f(1) = mf0.

Proof. If P = {p1, . . ., pm} is an f-design then by Lemma 6.1 we have f(1) = mf0.

Suppose f(1) = mf0. Since D(P) ⊂ Zf, by (6.4) we have Sf(P) = mf(1). Moreover, by assumption, fk ≥ 0 for all k. Then Delsarte’s bound (6.3) yields:

mf(1) = Sf(P) =

k

fkMk(P) ≥ m2f0.

From (6.1) it follows that fkMk(P) ≥ 0, for all k. Then the equality f(1) = mf0 holds only if fkMk(P) = 0, for all k > 0. This is exactly Property (1) in Deﬁnition 6.1.

![image 63](<2020-musin-majorization-minimal-energy-spheres_images/imageFile63.png>)

![image 64](<2020-musin-majorization-minimal-energy-spheres_images/imageFile64.png>)

![image 65](<2020-musin-majorization-minimal-energy-spheres_images/imageFile65.png>)

![image 66](<2020-musin-majorization-minimal-energy-spheres_images/imageFile66.png>)

- 6.3 Spherical f-designs and M-sets Now we show that there is a simple connection between f-designs and M-sets.


- Theorem 6.2. Let f(t) = k fk Gk(n)(t) be a function on [−1, 1] with all fk ≥ 0. Then any f-design in Sn−1 is an M-set with ρ(x, y) = −f(x · y).


Proof. Let ρ(x, y) := −f(x · y), where x, y ∈ Sn−1. For Y = {y1, . . ., ym} ⊂ Sn−1 deﬁne Gf(Y ) :=

ρ(yi, yj).

i<j

If P = {p1, . . ., pm} is an f-design then the following equalities hold: f(1) = mf0, ρ(pi, pj) = 0, ∀ i = j, Gf(P) = 0. It is easy to see that for an arbitrary Y ⊂ Sn−1, |Y | = m, (6.1) implies Sf(Y ) =

fkMk(Y ) ≥ f0m2.

k

Thus

f0m2 − Sf(Y )

mf(1) − Sf(Y ) 2

2 ≤ 0. Finally, by (3.1) we have

Gf(Y ) =

=

![image 67](<2020-musin-majorization-minimal-energy-spheres_images/imageFile67.png>)

![image 68](<2020-musin-majorization-minimal-energy-spheres_images/imageFile68.png>)

Rρ(P) = (0, . . ..0) ⊲ Rρ(Y ). This completes the proof.

![image 69](<2020-musin-majorization-minimal-energy-spheres_images/imageFile69.png>)

![image 70](<2020-musin-majorization-minimal-energy-spheres_images/imageFile70.png>)

![image 71](<2020-musin-majorization-minimal-energy-spheres_images/imageFile71.png>)

![image 72](<2020-musin-majorization-minimal-energy-spheres_images/imageFile72.png>)

Open problem. Consider f as in Theorem 6.2 with all fk ≥ 0 and f(1) = mf0. Then Theorems 6.1 and 6.2 yield that if D(P) ⊂ Zf, then P is an f-design and P ∈ M(Sn−1, −f, m). It is easy to prove that if Y ∈ M(Sn−1, −f, m), then D(Y ) ⊂ Zf. Is it true that Y is always isomorphic to P? There are several cases when the answer is positive (see [2]).

- 6.4 Spherical τ- and f-designs A spherical τ-design P is a set of points in Sn−1 such that


1 µ(Sn−1) Sn−1

1 m x∈P

F(x), with m = |P|,

F(x)dµ(x) =

![image 73](<2020-musin-majorization-minimal-energy-spheres_images/imageFile73.png>)

![image 74](<2020-musin-majorization-minimal-energy-spheres_images/imageFile74.png>)

(µ(x) is the surface area measure) holds for all polynomials F(x) of total degree at most τ. Equivalently, P is a τ-design if and only if Mk(P) = 0 for all k = 1, 2, . . ., τ (see [11, 21]).

The following proposition directly follows from the deﬁnition of f- and τ-designs.

- Proposition 6.1. If P ⊂ Sn−1 is a τ-design and |D(P)| ≤ τ, then P is an f-design of degree τ with


(t − x), deg g ≤ τ − |D(P)|.

f(t) = g(t)

x∈D(P)

There are many examples of spherical f-designs. Let C be the set of vertices of a regular cross-polytope. Then D(C) = {0, −1} and C is a spherical 3-design. If f(t) := (at+b) t(t+1), a, b ∈ R, then Proposition 6.1 yields that C is an f-design of degree 3.

This example can be extended for universally optimal conﬁgurations. Note that all known universally optimal spherical conﬁgurations P are τ-designs with τ > |D(P)| [8]. Therefore, if f is the same as in Proposition 6.1, then P is an f-design.

However, the set of f-designs is much larger than the set of universally optimal conﬁgurations. Let P be the set of vertices of a regular 24-cell P in S3. It is known that P is not universally optimal [7]. In this case P is a 5-design and D(P) = {±1/2, 0, −1}. Thus, if

f(t) := (at + b) (t2 − 1/4)(t2 + t),

- then P is an f-design for all real a and b.


### 6.5 Spherical two-distance sets and f-designs

A ﬁnite collection P of unit vectors in Rn is called a spherical two-distance set if there are two real numbers a and b such that the inner product of each pair of distinct vectors from P takes value either a or b. In particular, if the inner products in P satisfy the condition a = −b, then P is a set of equiangular lines. In this subsection we discuss f-designs that are two-distance sets.

Let P be an f-design of degree 2. Then |D(P)| ≤ |Zf| ≤ 2, i.e. P is a two-distance set.

- Proposition 6.2. Let f(t) = (t − a)(t − b), where a, b ∈ [−1, 1) and a + b = 0. Then P in Sn−1 is an f-design if and only if P is a two-distance 2-design. Proof. We have


f(t) = t2 − (a + b)t + ab =

n − 1 n

G2(n) − (a + b) G(1n) + ab + 1/n = f2G(2n) + f1G(1n) + f0.

![image 75](<2020-musin-majorization-minimal-energy-spheres_images/imageFile75.png>)

Let P be an f-design. Since f1 = 0 and f2 = 0, P is a 2-design. If P is a two-distance 2-design with inner products a and b then, by Proposition 6.1, P is an f-design.

![image 76](<2020-musin-majorization-minimal-energy-spheres_images/imageFile76.png>)

![image 77](<2020-musin-majorization-minimal-energy-spheres_images/imageFile77.png>)

![image 78](<2020-musin-majorization-minimal-energy-spheres_images/imageFile78.png>)

![image 79](<2020-musin-majorization-minimal-energy-spheres_images/imageFile79.png>)

Actually, all two-distance 2-designs can be obtained from strongly regular graphs as shown in [4, Theorem 1.2]. This gives a characterization of f-designs of degree 2 with a + b = 0.

The case a = −b when f–designs become sets of equiangular lines is also very interesting. Note that the connection between these sets and strongly regular graphs is well–known [11].

If a = −b, we get f(t) = t2 − a2 and then f0 = 1/n − a2, f1 = 0, f2 = 1 − 1/n. In this case Delsarte’s bound (6.3) becomes

f(1) f0

m ≤

![image 80](<2020-musin-majorization-minimal-energy-spheres_images/imageFile80.png>)

n(1 − a2) 1 − na2

=

.

![image 81](<2020-musin-majorization-minimal-energy-spheres_images/imageFile81.png>)

For sets of equiangular lines this inequality is known as the relative bound as opposed to the absolute (or Gerzon) bound (see [20] and a recent improvement in [16]):

n(n + 1) 2

m ≤

. (6.5)

![image 82](<2020-musin-majorization-minimal-energy-spheres_images/imageFile82.png>)

We have that a set P in Sn−1 with |P| = m is an f-design, where f(t) = t2 − a2, if and only if D(P) = {a, −a} and m(1 − na2) = n(1 − a2). There are several known particular cases. However, the problem of classiﬁcation of these designs is yet unsolved.

Now let f(t) := g(t)(t − a)(t − b). We would like to ﬁnd all P in Sn−1 with |P| = m and D(P) = {a, b} that are f-designs.

Consider the case a + b ≥ 0. (For the case a + b < 0, see [24, 16].) In [24] we proved that if a+b ≥ 0, then the absolute bound (6.5) holds. Moreover, this bound is tight: for all n ≥ 7 there are maximal, i.e. with m = n(n + 1)/2, two-distance sets.

Let the unit vectors e1, . . ., en+1 form an orthogonal basis of Rn+1. Let Vn be the set of points ei + ej, 1 ≤ i < j ≤ n + 1. Since Vn lies in the hyperplane nk=1+1 xk = 2, we see that it represents a spherical two-distance set in Rn. The cardinality of Vn is n(n + 1)/2.

Let us rescale Vn such that its points lie on the unit sphere Sn−1. Let Λn denote the resulting set. It is not hard to determine the respective distances a and b:

n − 3 2(n − 1)

, b = −2 n − 1

n − 7 2(n − 1)

a =

, a + b =

.

![image 83](<2020-musin-majorization-minimal-energy-spheres_images/imageFile83.png>)

![image 84](<2020-musin-majorization-minimal-energy-spheres_images/imageFile84.png>)

![image 85](<2020-musin-majorization-minimal-energy-spheres_images/imageFile85.png>)

We see that for n > 7, |Λn| attains the upper bound for two-distance sets with a + b > 0.

In fact, Λn is a maximal f-design of degree 2. The following questions seems interesting: Are there other maximal f-designs with a + b > 0 of degree d ≥ 2?

As noted above, there is a correspondence between f-designs of degree 2 and strongly regular graphs. Actually, every graph G can be embedded as a spherical two-distance set (see [25]). This raises the following question: Which graphs are embeddable as f-designs?

Acknowledgments. I wish to thank Eiichi Bannai, Alexander Barg, Peter Boyvalenkov and Alexander Kolpakov for helpful discussions and useful comments.

## References

- [1] N. N. Andreev and V. A. Yudin, Problems of approximation theory in discrete geometry, Math. Research, (Advances in Multivariate Approximation), 107 (1999), 19-32
- [2] E. Bannai and N. J. A. Sloane, Uniqueness of certain spherical codes, Canadian J. Math., 33 (1981), 437-449.
- [3] E. Bannai, T. Okuda and M. Tagami, Spherical designs of harmonic index t. J. Approximation Theory, 195 (2015), 1-18.


- [4] A. Barg, A. Glazyrin, K. A. Okoudjou and W-H. Yu, Finite two-distance tight frames. Linear Algebra and its Application, 474 (2015), 163-175
- [5] P. Boyvalenkov, D. Danev, P. Kazakov, Indexes of spherical codes, in “Codes and Association Schemes (Proc. DIMACS Workshop, November 1999”, A Barg and S. Litsyn, Eds.), American Mathematical Society 2001, pp. 47-57.
- [6] P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saﬀ, M. Stoyanova, Universal lower bounds for potential energy of spherical codes, Constr. Approx., 44 (2016), 385–415.
- [7] H. Cohn, J. H. Conway, N. Elkies and A. Kumar. The D4 root system is not universally optimal. Experiment. Math., 16(3):313-320, 2007.
- [8] H. Cohn and A. Kumar, Universally optimal distribution of points on spheres, J. Amer. Math. Soc., 20 (2007), 99-148.
- [9] J.H. Conway and N.J.A. Sloane, Sphere Packings, Lattices, and Groups, New York, Springer-Verlag, 1999 (Third Edition).
- [10] H. Davenport and G. Haj´s, Problem 35. Mat. Lapok, 2 (1951), 68 (in Hungarian).
- [11] P. Delsarte, J. M. Goethals, and J. J. Seidel. Spherical codes and designs. Geometriae Dedicata, 6(3):363-388, 1977.
- [12] P. Delsarte and V. I. Levenshtein, Association schemes and coding theory, IEEE Trans. Inform. Theory, 44 (1998), 2477-2504.
- [13] P. Delsarte and J. J. Seidel, Fisher type inequalities for Euclidean t–designs, Linear Algebra Appl., 114/115 (1989), 213–230.
- [14] P. D. Dragnev, D. A. Legg, and D. W. Townsend, Discrete logarithmic energy on the sphere, Paciﬁc J. Math. 207 (2002), 345-357.
- [15] P. D. Dragnev and O. R. Musin. Log-optimal (d + 2)-conﬁgurations in d-dimensions, preprint, arXiv:1909.09909.
- [16] A. Glazyrin and W.-H. Yu, Upper bounds for s–distance sets and equiangular lines, Advances in Math., 330: 810–833, 2018.
- [17] G. H. Hardy, J. E. Littlewood and G. Po´lya, Inequalities, 2nd edition, 1952, Cambridge University Press, London.
- [18] G. A. Kabatiansky and V. I. Levenshtein, Bounds for packings on a sphere and in space, Problems of Information Transmission, 14:1 (1978), 1-17.
- [19] W. Kuperberg. Optimal arrangements in packing congruent balls in a spherical container. Discrete Comput. Geom., 37(2): 205-212, 2007.


- [20] P. W. H. Lemmens and J. J. Seidel, Equiangular lines, J. Algebra, 24 (1973), 494-512.
- [21] V. I. Levenshtein. Universal bounds for codes and designs. In Handbook of Coding Theory, Vol. I, 499-648. North-Holland, Amsterdam, 1998.
- [22] A. W. Marshall and I. Olkin, Inequalities: Theory of Majorization and Its Application, Academic Press, 1979.
- [23] T. W. Melnik, O. Knop, and W. R. Smith, Extremal arrangements of points and unit charges on a sphere: equilibrium conﬁgurations revised, Can. J. Chem., 55 (1977), 17451761.
- [24] O. R. Musin. Spherical two-distance sets. J. Combin. Theory Ser. A, 116 (2009), 988-995.
- [25] O. R. Musin. Graphs and spherical two-distance sets. European J. Combin., 80 (2019), 311-325.
- [26] R.A. Rankin, The closest packing of spherical caps in n dimensions. Proc. Glasgow Math. Assoc., 2: 139–144, 1955.
- [27] R. Schwartz, The ﬁve-electron case of Thomson’s problem, Exp. Math., 22 (2013), 157– 186.
- [28] R. Schwartz, Five point energy minimization: a synopsis,, Constr. Approx., 51 (2020), 537–564.
- [29] S. Smale, Mathematical problems for the next century, in Arnold, V. I.; Atiyah, M.; Lax, P.; Mazur, B. Mathematics: Frontiers and Perspectives, AMS (1999), 271–294
- [30] V. A. Yudin, Minimum potential energy of a point system of charges, Discrete Math. Appl., 3 (1993), 75-81.
- [31] Y. Zhu, E. Bannai, Et. Bannai, K.-T. Kim, W.-H. Yu: On Spherical Designs of Some Harmonic Indices. Electr. J. Comb., 24 (2017), 2-14.


O. R. Musin University of Texas Rio Grande Valley, School of Mathematical and Statistical Sciences Moscow Institute of Physics and Technology The Institute for Information Transmission Problems of RAS

Mailing address: One West University Boulevard, Brownsville, TX, 78520, USA. E-mail address: oleg.musin@utrgv.edu

