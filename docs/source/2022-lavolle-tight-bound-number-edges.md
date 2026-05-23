---
type: source
kind: paper
title: A tight bound for the number of edges of matchstick graphs
authors: Jérémy Lavollée, Konrad Swanepoel
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2209.09800v2
source_local: ../raw/2022-lavolle-tight-bound-number-edges.pdf
topic: general-knowledge
cites:
---

arXiv:2209.09800v2[math.CO]15Jun2023

A TIGHT BOUND FOR THE NUMBER OF EDGES OF MATCHSTICK GRAPHS

JER´ EMY´ LAVOLLEE´ AND KONRAD SWANEPOEL

Abstract. A matchstick graph is a plane graph with edges drawn as unitdistance line segments. Harborth introduced these graphs in 1981 and conjectured that the maximum number of edges for a matchstick graph on n vertices is ⌊3n −

√12n − 3⌋. In this paper we prove this conjecture for all n ≥ 1. The main geometric ingredient of the proof is an isoperimetric inequality related to L’Huilier’s inequality.

![image 1](<2022-lavolle-tight-bound-number-edges_images/imageFile1.png>)

1. Introduction

A matchstick graph is a graph drawn in the Euclidean plane with each edge a straight unit-length segment, such that two edges only intersect in a common endpoint. These graphs were introduced by Harborth [11,12] in 1981. Most of the literature deals with matchstick graphs which are regular [3,8, 9, 14–16,21,26] or almost regular [18,22–25]. There are also a few papers dealing with more general aspects, such as enumeration [20] and algorithmic recognition [1, 13]. Harborth considered the extremal problem of ﬁnding the minimum number n of vertices in a matchstick graph on e edges, or equivalently, the maximum number of edges for a given number of vertices. He conjectured in [12] that e ≤ 3n −

√12n − 3 (see also [4, p. 225]) and proved this in the special case of penny graphs using a neat induction on the number of vertices [10] (see also [19, Theorem 13.12]). A penny graph is a matchstick graph with the additional property that the circles of radius 1/2 around the vertices are non-overlapping.

![image 2](<2022-lavolle-tight-bound-number-edges_images/imageFile2.png>)

- Theorem 1 (Harborth [10]). Let G be a matchstick graph on n vertices such that the distance between any two vertices is at least 1. Then the number of edges of G

satisﬁes e ≤ 3n −

√12n − 3.

![image 3](<2022-lavolle-tight-bound-number-edges_images/imageFile3.png>)

For each n ≥ 1 there are examples on the triangular lattice with n vertices and the optimal ⌊3n −

√12n − 3⌋ edges [10,19]. Proving Harborth’s conjecture in general turns out to be trickier. Using the isoperimetric inequality (Lemma 1) we showed in [17] that e ≤ 3n − c√12n − 3, where c = 12(1 + π√3/6) = 0.976 ..., which implies Harborth’s conjecture for some small values of n. In this paper we settle the conjecture completely.

![image 4](<2022-lavolle-tight-bound-number-edges_images/imageFile4.png>)

![image 5](<2022-lavolle-tight-bound-number-edges_images/imageFile5.png>)

![image 6](<2022-lavolle-tight-bound-number-edges_images/imageFile6.png>)

![image 7](<2022-lavolle-tight-bound-number-edges_images/imageFile7.png>)

![image 8](<2022-lavolle-tight-bound-number-edges_images/imageFile8.png>)

- Theorem 2. Let G be a matchstick graph with n vertices and e edges. Then √12n − 3.


![image 9](<2022-lavolle-tight-bound-number-edges_images/imageFile9.png>)

- e ≤ 3n −


As in our previous paper [17], as a ﬁrst step we use the Euler formula and the isoperimetric inequality.

- Lemma 1 (Isoperimetric inequality). For any simple polygon of perimeter b and area A we have 4πA < b2.


![image 10](<2022-lavolle-tight-bound-number-edges_images/imageFile10.png>)

2020 Mathematics Subject Classiﬁcation. Primary 52C10. Secondary 05C10. Key words and phrases. matchstick graph, penny graph, plane unit-distance graph.

1

However, we will then exploit a diﬀerent isoperimetric inequality that takes into account that many edges on the outer boundary of G lie on the same triangular lattice. A variant of the isoperimetric inequality in the plane, known as L’Huilier’s inequality, states that among all polygons of a given perimeter for which the sides are constrained to be parallel to a given set of directions, the one of maximum area is circumscribed to a circle [6, pp. 9–10], [7, pp. 12–13]. In particular, among all closed polygons of a given perimeter with each side parallel to one of the sides of a ﬁxed regular hexagon, the regular hexagon is optimal. We prove the following variant of this special case where we allow a certain bounded amount of the perimeter to be unconstrained in direction.

- Lemma 2. Let P be a simple polygon with perimeter b, area A, and with the total


length of the sides not parallel to any side of some ﬁxed regular hexagon at most b∗. Then

√

3A ≤ b + √ 23 − 1 b∗ 2.

![image 11](<2022-lavolle-tight-bound-number-edges_images/imageFile11.png>)

8

![image 12](<2022-lavolle-tight-bound-number-edges_images/imageFile12.png>)

![image 13](<2022-lavolle-tight-bound-number-edges_images/imageFile13.png>)

Our proof of Theorem 2 has an analytical ﬂavour, with many inequalities appearing in it that are rather weak, with constants that could easily be improved. Surprisingly, this turns out to be unnecessary. The inequalities also often need n to be large, which creates the potential problem that this approach will only work for suﬃciently large n. However, the original isoperimetric inequality allows us to dismiss all values of n < 147 early on in the proof. Then the rest of the proof goes through, although there are many inequalities that have to be checked. This can be done by hand or by apps such as Wolfram Alpha or Desmos. We have to balance the asymptotics with constant terms in order to make the inequalities valid for small n. It is rather strange that such an approach manages to make the induction succeed for all values of n.

- 1.1. Proof outline. The proof of Theorem 2 is in Section 2. Here we give a highlevel summary. The proof is by induction with the induction step split up into 12 claims. As the cases 1 ≤ n ≤ 4 of Theorem 2 are easily checked, we assume that n > 4 and that the theorem holds for all smaller values of n, but not for n, and aim for a contradiction.


Starting oﬀ, we show that the graph has minimum degree 3 (Claim 1) and is 2-connected (Claim 2). We then apply the Euler formula and count incident edgeface pairs to give an upper bound for the length of the boundary of G in terms of n and a certain weighted count F of the number of non-triangular inner faces (Claim 3), as well as a lower bound for the number of triangles (Claim 4). If this weighted count F equals 0 or 1, then either all inner faces are triangles, a case where Theorem 1 applies, or there is a quadrilateral as well, a case that can be easily dealt with by splitting up the graph at the quadrilateral and applying induction. Thus we can assume that F ≥ 2 (Claim 5).

We apply the isoperimetric inequality (Lemma 1) to our upper bound of the boundary length of G and the lower bound on its area derived from the lower bound on the number of triangles. This gives an upper bound for F of the form c√12n − 3 (we use c = 1/11, but c can be made as small as 1/20) as well as showing that we may assume that n ≥ 147 otherwise F < 2 (Claim 6).

![image 14](<2022-lavolle-tight-bound-number-edges_images/imageFile14.png>)

We next consider the so-called lattice components of the graph, which we deﬁne to be maximal 2-connected subgraphs that each lie on some triangular lattice. We ﬁnd lower bounds for their boundary lengths (Claim 7) and show that they cover almost all of G without too much overlap (Claim 8). This enables us to show that the largest lattice component, G1, has to be quite large (we show that n(G1) > 3n/4 in Claim 9, but it is possible to go up to 0.97n if n is suﬃciently large).

We split G up into G1 and a slight enlargement of G − G1, and apply induction to obtain a lower bound for F in terms of n and n1 (Claim 10) that will be crucial for the ﬁnal part of the proof. We also bound the number of edges on the boundary of G that are not on the boundary of G1 (Claim 11). Thus, except for a bounded quantity, the boundary edges of G all lie on the same triangular lattice. Our new isoperimetric inequality (Lemma 2) then gives an improved upper bound on the area of G, which can be bounded from below using the bound on the number of triangles from Claim 4. The upshot of this is that we ﬁnd a very good upper bound on F (Claim 12), which, together with the lower bound from Claim 10 gives us our ﬁnal contradiction.

- 1.2. Deﬁnitions. We deﬁne a triangular lattice to be any subset of the plane isometric to {m(1,0)+n(1/2,√3/2) : m,n ∈ Z}, and we say that a ﬁnite set of points lies on a triangular lattice if it is a subset of some triangular lattice. We will use the following simple observation.


![image 15](<2022-lavolle-tight-bound-number-edges_images/imageFile15.png>)

- Lemma 3. If a and b are distinct points on a triangular lattice and c is a point at distance 1 to both a and b, then c lies on the same triangular lattice.

We use standard graph theory terminology as can be found in [5, Sections 1.1–

- 1.4, 4.1, 4.2]. We call the cycle bounding the outer face of a plane graph G the boundary of G, its length the boundary length of G, and its edges the boundary edges of G.

We will occasionally use the function φ(x) = √12x − 3−3 which is non-negative for all x ≥ 1. Since φ is strictly concave, φ(x + a) − φ(x) is strictly decreasing in x for all ﬁxed a > 0. This implies the following inequality that we will use repeatedly.

![image 16](<2022-lavolle-tight-bound-number-edges_images/imageFile16.png>)

Lemma 4. φ(a) + φ(b) < φ(a − c) + φ(b + c) whenever a > b + c, b ≥ 1 and c > 0. 2. Proof

- 2.1. Setting up the induction. Let G be a matchstick graph on n = n(G) vertices in the plane. Denote the number of edges by e = e(G). We prove Theorem 2 by induction. The cases 1 ≤ n ≤ 3 are trivial. The case n = 4 follows since the complete graph on 4 vertices is not a matchstick graph. So we ﬁx n > 4 and assume the theorem is true for all matchstick graphs of less than n vertices. Among all matchstick graphs on n vertices, ﬁx one G with the maximum number e of edges. We assume that




√12n − 3, (1) and will aim for a contradiction. Claims 1–12 below will all have as unstated assumptions the induction hypothesis, n > 4, the inequality (1), and that G has the maximum number of edges among all matchstick graphs with n vertices.

![image 17](<2022-lavolle-tight-bound-number-edges_images/imageFile17.png>)

e > 3n −

- 2.2. Basic properties.


- Claim 1. Each vertex of G has at least 3 neighbours.


Proof. Suppose that there is a vertex v with at most 2 neighbours, and let G′ = G − v. Then by induction and Lemma 4,

![image 18](<2022-lavolle-tight-bound-number-edges_images/imageFile18.png>)

e ≤ e(G′) + 2 ≤ 3(n − 1) − 12(n − 1) − 3 + 2

= 3n − φ(n − 1) − 4 ≤ 3n − φ(n) + φ(5) − φ(4) − 4

√12n − 3, which contradicts (1).

√12n − 3 + φ(5) − φ(4) − 1 < 3n −

![image 19](<2022-lavolle-tight-bound-number-edges_images/imageFile19.png>)

![image 20](<2022-lavolle-tight-bound-number-edges_images/imageFile20.png>)

= 3n −

- Claim 2. G is 2-connected.

Proof. G has to be connected, otherwise we can move a connected component until one of its vertices has distance 1 to some other vertex, contradicting maximality.

If G is not 2-connected, then G has a cut vertex. Thus there exist two subgraphs G1 and G2 that cover G and have only a single vertex in common. Then with n1 = n(G1),n2 = n(G2) ≥ 2, e1 = e(G1), and e2 = e(G2), we have n = n1 + n2 − 1, and

e = e1 + e2 ≤ 3n1 −

√12n1 − 3 + 3n2 −

![image 21](<2022-lavolle-tight-bound-number-edges_images/imageFile21.png>)

√12n2 − 3

![image 22](<2022-lavolle-tight-bound-number-edges_images/imageFile22.png>)

= 3n − φ(n1) − φ(n2) − 3 < 3n − φ(n1 + n2 − 1) − φ(1) − 3 = 3n −

√12n − 3 by induction and Lemma 4, which contradicts (1).

![image 23](<2022-lavolle-tight-bound-number-edges_images/imageFile23.png>)

2.3. The Euler formula and double counting. Since G is 2-connected by Claim 2, all of its faces are polygons. Let b denote the length of the outer face, and for each i ≥ 3, let fi denote the number of inner faces bounded by a cycle of length i. Since G is connected, Euler’s formula gives

n − e +

i≥3

fi = 1, (2)

and since G is 2-connected, by counting incident edge-face pairs in two ways, we obtain

2e = b +

i≥3

ifi. (3)

Let F = i≥4(i − 3)fi. Then (2) and (3) imply

e = 3n − 3 − b − F. (4) From (1) we then obtain

- Claim 3. b < √12n − 3 − 3 − F = φ(n) − F.

![image 24](<2022-lavolle-tight-bound-number-edges_images/imageFile24.png>)

2.4. Using the isoperimetric inequality. We need the following lower bound on the number of triangular faces, so that we can estimate the area of the region bounded by G, then use the isoperimetric inequality to ﬁnd a lower bound for b and from that our ﬁrst upper bound on F. This upper bound will be needed later in our proof of an improved upper bound for F (Claim 12).

- Claim 4. f3 > 2n + 1 −

√12n − 3 − F = φ(n)2/6 − F. Proof. Using the Euler formula (2) and our assumption (1), we obtain f3 = e − n + 1 −

![image 25](<2022-lavolle-tight-bound-number-edges_images/imageFile25.png>)

i≥4

fi > 2n −

√12n − 3 + 1 − F.

![image 26](<2022-lavolle-tight-bound-number-edges_images/imageFile26.png>)

- Claim 5. F ≥ 2.


Proof. If F = 0, then all inner faces are triangular, and since G is 2-connected, it lies on a single triangular lattice. Then G is a penny graph, and Harborth’s Theorem 1 gives e ≤ 3n −

√12n − 3, a contradiction.

![image 27](<2022-lavolle-tight-bound-number-edges_images/imageFile27.png>)

If F = 1, then there is a single quadrilateral inner face with all other inner faces triangular. Each vertex v of this quadrilateral must lie on the boundary of G, otherwise, all other faces incident with v would be equilateral triangles, implying that the angle of the quadrilateral at v is a multiple of 60◦. Then the quadrilateral would have angles 60◦ and 120◦, and we could add an edge between the two opposite vertices at the 120◦ angles, violating the maximality of G.

G2

G1

p

q

Figure 1. Subgraphs G1 and G2 covering G and sharing edge pq of a quadrilateral

We next decompose G. Since n > 5, at least one of the edges of the quadrilateral is not a boundary edge of G. Let p and q be the endpoints of such an edge. Then G − {p,q} is not connected and has exactly two connected components C1 and C2. Let Gi be the subgraph of G induced by the vertices of Ci and p and q for i = 1,2. Then G1 and G2 have only an edge of the quadrilateral in common, and cover G. Denoting ni = n(Gi) and ei = e(Gi), i = 1,2, we have n1 + n2 = n + 2 and e1 + e2 = e + 1. Since pq is not on the boundary of G, it follows that ni ≥ 3 (i = 1,2), and the length b of the boundary of G is at least 5. Then Claim 3 implies that n > 7, and

e = e1 + e2 − 1 ≤ 3n − φ(n1) − φ(n2) − 1 by induction ≤ 3n − φ(n1 + n2 − 3) − φ(3) − 1 by Lemma 4 < 3n − φ(n) + φ(7) − φ(6) − φ(3) − 1 again by Lemma 4 < 3n −

√12n − 3, contradicting assumption 1.

![image 28](<2022-lavolle-tight-bound-number-edges_images/imageFile28.png>)

- Claim 6. n ≥ 147 and F < 111 √12n − 3 − 1. Proof. Denote the area of the boundary polygon of G by A. The area of an


![image 29](<2022-lavolle-tight-bound-number-edges_images/imageFile29.png>)

![image 30](<2022-lavolle-tight-bound-number-edges_images/imageFile30.png>)

equilateral triangle of side length 1 is √3/4, hence A >

√3

![image 31](<2022-lavolle-tight-bound-number-edges_images/imageFile31.png>)

![image 32](<2022-lavolle-tight-bound-number-edges_images/imageFile32.png>)

4 f3. By Claim 4,

![image 33](<2022-lavolle-tight-bound-number-edges_images/imageFile33.png>)

- f3 > φ(n)2/6 − F, and by the isoperimetric inequality (Lemma 1) and Claim 3, 4πA < b2 < (φ(n) − F)2. In the remainder of this proof we write φ = φ(n). We


√3 6 (φ2 − 6F) < (φ − F)2, or when expanded,

![image 34](<2022-lavolle-tight-bound-number-edges_images/imageFile34.png>)

thus obtain the inequality π

![image 35](<2022-lavolle-tight-bound-number-edges_images/imageFile35.png>)

√

√

![image 36](<2022-lavolle-tight-bound-number-edges_images/imageFile36.png>)

![image 37](<2022-lavolle-tight-bound-number-edges_images/imageFile37.png>)

3/6)φ2 > 0. (5)

F2 − (2φ − π

3)F + (1 − π

By Claim 3 and b ≥ 3, we obtain F < φ − π√3/2, so the left-hand side of (5) is decreasing in F. Thus we can substitute F = 2 into (5) to obtain

![image 38](<2022-lavolle-tight-bound-number-edges_images/imageFile38.png>)

√

√

![image 39](<2022-lavolle-tight-bound-number-edges_images/imageFile39.png>)

![image 40](<2022-lavolle-tight-bound-number-edges_images/imageFile40.png>)

3/6)φ2 > 0,

3) + (1 − π

4 − 2(2φ − π

hence φ < 4.114 ... or φ > 38.849 ..., or in terms of n, n < 4.468 ... or n > 146.199 .... Since n ≥ 5 by assumption, we conclude that n ≥ 147, as required. For the second part of the claim, we solve for F in (5) to obtain

F < φ − π

√

- 1

![image 41](<2022-lavolle-tight-bound-number-edges_images/imageFile41.png>)

- 2


![image 42](<2022-lavolle-tight-bound-number-edges_images/imageFile42.png>)

3/2 −

![image 43](<2022-lavolle-tight-bound-number-edges_images/imageFile43.png>)

√

2π √3

![image 44](<2022-lavolle-tight-bound-number-edges_images/imageFile44.png>)

3φ + 3π2.

φ2 − 4π

![image 45](<2022-lavolle-tight-bound-number-edges_images/imageFile45.png>)

![image 46](<2022-lavolle-tight-bound-number-edges_images/imageFile46.png>)

In order to show that F < (φ − 8)/11, it is suﬃcient to show that

![image 47](<2022-lavolle-tight-bound-number-edges_images/imageFile47.png>)

√

√

φ − 8 11

2π √3

- 1

![image 48](<2022-lavolle-tight-bound-number-edges_images/imageFile48.png>)

- 2


![image 49](<2022-lavolle-tight-bound-number-edges_images/imageFile49.png>)

![image 50](<2022-lavolle-tight-bound-number-edges_images/imageFile50.png>)

φ2 − 4π

3φ + 3π2 ≤

3/2 −

φ − π

.

![image 51](<2022-lavolle-tight-bound-number-edges_images/imageFile51.png>)

![image 52](<2022-lavolle-tight-bound-number-edges_images/imageFile52.png>)

![image 53](<2022-lavolle-tight-bound-number-edges_images/imageFile53.png>)

This inequality is equivalent to φ ≤ 2.084 ... or φ ≥ 20.506 .... However, we have already shown that φ > 38.849 .... Thus we conclude that F < (φ − 8)/11, which proves the second part of the claim.

- 2.5. Lattice components. We deﬁne a lattice component of G to be any maximal 2-connected subgraph (on at least 3 vertices) that lies on some triangular lattice. Denote the lattice components of G by G1,...,Gk. Denote the number of vertices by ni = n(Gi), the number of edges by ei = e(Gi), and the boundary length of Gi by bi. Assume that n1 ≥ n2 ≥ ··· ≥ nk. Note that no two lattice components have an edge in common, otherwise their union would be a larger 2-connected graph on the same lattice.


- Claim 7. For each i = 1,...,k, bi ≥

√12ni − 3 − 3.

![image 54](<2022-lavolle-tight-bound-number-edges_images/imageFile54.png>)

Proof. Gi is on a triangular lattice and is 2-connected, so its boundary is a cycle. Construct a new graph G′ from Gi, by ﬁlling up all missing lattice vertices and edges inside the boundary of Gi. By Theorem 1, e(G′) ≤ 3n(G′) − 12n(G′) − 3, since G′ is also on the triangular lattice. (We cannot use induction here, because G′ might have more than n vertices.) By (4) applied to G′ (which is still 2-connected and with F = 0), we obtain bi ≥ 12n(G′) − 3 − 3 ≥

![image 55](<2022-lavolle-tight-bound-number-edges_images/imageFile55.png>)

![image 56](<2022-lavolle-tight-bound-number-edges_images/imageFile56.png>)

√12ni − 3 − 3, since G′ has the same outer boundary as Gi.

![image 57](<2022-lavolle-tight-bound-number-edges_images/imageFile57.png>)

We will later need that the largest lattice component is not too small. We ﬁrst show that the lattice components cover almost all of G and do not overlap too much.

- Claim 8. n − 2F ≤ ki=1 ni ≤ n + 4F.

Proof. For the lower bound, consider a vertex v of G that does not belong to any lattice component. Let s be the number of inner faces of G incident to v. Since v has at least 3 neighbours (Claim 1), s ≥ 2. Assign a charge of 1/s to each inner face incident to v. Since these faces are all non-triangular, the total charge is ≤ 21 i≥4 ifi ≤ 2F. The total charge on all such vertices counts the number of vertices not covered by any lattice component. Thus, at least n − 2F vertices of G are covered by the lattice components, which gives ki=1 ni ≥ n − 2F.

![image 58](<2022-lavolle-tight-bound-number-edges_images/imageFile58.png>)

For the upper bound, consider a vertex v that belongs to t ≥ 2 of the Gi. Now let

- s be the number of non-triangular inner faces of G incident to v. Since two adjacent faces incident to v cannot belong to distinct Gi, there is at least one non-triangular face between any two faces at v belonging to distinct Gi, so v is incident to at least
- t non-triangular faces, of which one could be the outer face. Hence s ≥ t−1. Assign a charge of (t − 1)/s to each non-triangular inner face incident to v. This gives a


total charge of t−1 for each v, which is exactly its contribution to i ni −n. Since (t − 1)/s ≤ 1, we obtain that the total charge is at most i≥4 ifi ≤ 4F. Thus,

i ni ≤ n + 4F. From now on we concentrate on the largest lattice component G1. We ﬁrst show

that it covers a considerable proportion of G.

- Claim 9. n1 > 3n/4.


Proof. Suppose that all ni ≤ 3n/4. We will ﬁnd a contradiction by bounding k i=1 bi from above and below. Since no two Gi have a common boundary edge,

this sum counts the number of edges on the boundaries of all lattice components.

For the upper bound, note that if an edge is on the boundary of some lattice component then it borders a non-triangular face on the outside of the lattice component.

This gives

k

√12n − 3 − 6 (6)

ifi < √12n − 3 − 3 − F + 4F <

14 11

![image 59](<2022-lavolle-tight-bound-number-edges_images/imageFile59.png>)

![image 60](<2022-lavolle-tight-bound-number-edges_images/imageFile60.png>)

bi ≤ b +

![image 61](<2022-lavolle-tight-bound-number-edges_images/imageFile61.png>)

i=1

i≥4

from Claims 3 and 6. For the lower bound we just use Claim 7:

k

bi ≥

i=1

k

(√12ni − 3 − 3) =

![image 62](<2022-lavolle-tight-bound-number-edges_images/imageFile62.png>)

i=1

k

φ(ni). (7)

i=1

We lower bound the right-hand side by relaxing it to a continuous optimisation problem. We have k ≤ N/3, where N = ki=1 ni. For later reference, note that 3n/4 + 3 < N < 6n/4 − 3 since n ≥ 13, by Claims 8 and 6. In particular, k ≥ 2. For each ℓ = 2,...,⌊N/3⌋, deﬁne Φℓ(x1,...,xℓ) = ℓi=1 φ(xi) on the domain

ℓ

Dℓ = (x1,...,xℓ) ∈ Rℓ : 34n ≥ x1 ≥ ··· ≥ xℓ ≥ 3,

xi = N .

![image 63](<2022-lavolle-tight-bound-number-edges_images/imageFile63.png>)

i=1

For each ℓ, the function Φℓ has a minimum value yℓ on Dℓ. Among all of these ℓ, ﬁx one, say m, that minimises yℓ. Fix (x1,...,xm) ∈ Dm such that Φm(x1,...,xm) = ym. By strict concavity of φ (Lemma 4) we cannot have two xi in the open interval (3, 43n). If m ≥ 3, we cannot have some xi = 3 and another xj ≤ 3n/4 − 3, since we can then replace both by a single variable equal to xj + 3, thereby ﬁnding

![image 64](<2022-lavolle-tight-bound-number-edges_images/imageFile64.png>)

ym−1 ≤ ym + φ(3 + xj) − φ(xj) − φ(3) ≤ ym + φ(6) − φ(3) − φ(3) by Lemma 4 < ym.

It follows that we cannot have any xi = 3, since this would imply that all other xj ∈ (3n/4 − 3,3n/4], but 3 + 3n/4 < N and 3 + 2(3n/4 − 3) > N as noted before. We cannot have two xi equal to 34n, since 6n/4 > N. Thus necessarily m = 2,x1 = 34n,x2 = N − 34n. It follows that

![image 65](<2022-lavolle-tight-bound-number-edges_images/imageFile65.png>)

![image 66](<2022-lavolle-tight-bound-number-edges_images/imageFile66.png>)

![image 67](<2022-lavolle-tight-bound-number-edges_images/imageFile67.png>)

k

φ(ni) = Φk(n1,...,nk) ≥ Φ2(x1,x2) ≥ Φ2(x1 + 1/16,x2 − 1/16) by Lemma 4

i=1

![image 68](<2022-lavolle-tight-bound-number-edges_images/imageFile68.png>)

![image 69](<2022-lavolle-tight-bound-number-edges_images/imageFile69.png>)

= (3/4)(12n − 3) − 3 + 12(N − 3n/4) − 15/4 − 3 ≥

√3 2

√12n − 3 + 12(n/4 − 2F) − 15/4 − 6 by Claim 8. (8) Putting (6), (7) and (8) together, we obtain

![image 70](<2022-lavolle-tight-bound-number-edges_images/imageFile70.png>)

![image 71](<2022-lavolle-tight-bound-number-edges_images/imageFile71.png>)

![image 72](<2022-lavolle-tight-bound-number-edges_images/imageFile72.png>)

![image 73](<2022-lavolle-tight-bound-number-edges_images/imageFile73.png>)

√3 2

![image 74](<2022-lavolle-tight-bound-number-edges_images/imageFile74.png>)

- 1


1 4

14 11 −

2

(12n−3) > 12(n/4−2F)−15/4 =

(12n−3)−3−24F. Again using Claim 6 it follows that

(12n−3) >

![image 75](<2022-lavolle-tight-bound-number-edges_images/imageFile75.png>)

![image 76](<2022-lavolle-tight-bound-number-edges_images/imageFile76.png>)

![image 77](<2022-lavolle-tight-bound-number-edges_images/imageFile77.png>)

![image 78](<2022-lavolle-tight-bound-number-edges_images/imageFile78.png>)

- 6


√12n − 3 − 24, which has no solutions in n, a contradiction.

1 12

24 11

![image 79](<2022-lavolle-tight-bound-number-edges_images/imageFile79.png>)

(12n − 3) − 3 < 24F <

![image 80](<2022-lavolle-tight-bound-number-edges_images/imageFile80.png>)

![image 81](<2022-lavolle-tight-bound-number-edges_images/imageFile81.png>)

The next inequality comes from applying the induction hypothesis to G1 and a slight enlargement of the remainder G − G1.

- Claim 10. 12(n − n1) < 6F + √12n − 3 −


√12n1 − 3.

![image 82](<2022-lavolle-tight-bound-number-edges_images/imageFile82.png>)

![image 83](<2022-lavolle-tight-bound-number-edges_images/imageFile83.png>)

![image 84](<2022-lavolle-tight-bound-number-edges_images/imageFile84.png>)

G1 G′

K

Figure 2. Decomposition of G into G1 and G′ with common vertex set K

Proof. Let K be the set of vertices of G1 that are joined to some vertex in G − G1, and let G′ be the subgraph of G induced by V (G − G1) ∪ K. Since G1 is on the lattice, we already know by Harborth’s Theorem 1 that e1 ≤ 3n1 −

√12n1 − 3. If K = ∅, then G1 = G since G and G1 are connected, and then the assumption (1) is contradicted. Thus K = ∅. Let n′ = n(G′) = n − n1 + |K| and e′ = e(G′). Then G′ and G1 cover all the edges of G, hence e ≤ e1 + e′. To bound e′ from above, we will apply induction, but then we need to ensure that K = V (G1). We do this by bounding |K| from above.

![image 85](<2022-lavolle-tight-bound-number-edges_images/imageFile85.png>)

Each vertex v in K belongs to some inner face of G not lying on the lattice of G1, otherwise all inner faces around v lie on the same lattice, so must be part of G1 by maximality. Consider any inner face Γ not lying on the lattice of G1, so with at least one vertex not in K. Denote the length of the cycle bounding Γ by i. Suppose that all but one of the vertices on this cycle lie in K and consider the remaining vertex v with neighbours u and w on Γ. Since u and w are on the lattice of G1, v also lies on the same lattice by Lemma 3, but then Γ lies on the lattice of G1, a contradiction. Hence at most i − 2 vertices of K belong to Γ. Since Γ is a non-triangular face of G, we ﬁnd the upper bound

|K| ≤

(i − 2)fi ≤ 2F.

i≥4

By Claims 6 and 9 it follows that 2F < n1, hence K cannot be all of G1 so G′ is a proper subset of G, and we can apply induction to G′ to obtain

√12n′ − 3. Using assumption (1) and n1 + n′ = n + |K|, we obtain

√12n1 − 3 + 3n′ −

![image 86](<2022-lavolle-tight-bound-number-edges_images/imageFile86.png>)

e ≤ e1 + e′ ≤ 3n1 −

![image 87](<2022-lavolle-tight-bound-number-edges_images/imageFile87.png>)

12(n − n1 + |K|) − 3 < 3|K| + √12n − 3 −

√12n1 − 3. (9) The claim now follows from the bounds 1 ≤ |K| ≤ 2F.

![image 88](<2022-lavolle-tight-bound-number-edges_images/imageFile88.png>)

![image 89](<2022-lavolle-tight-bound-number-edges_images/imageFile89.png>)

![image 90](<2022-lavolle-tight-bound-number-edges_images/imageFile90.png>)

Let b∗ be the number of boundary edges of G not on the boundary of G1. √12n1 − 3.

- Claim 11. b∗ < √12n − 3 −


![image 91](<2022-lavolle-tight-bound-number-edges_images/imageFile91.png>)

![image 92](<2022-lavolle-tight-bound-number-edges_images/imageFile92.png>)

Proof. Each edge on the boundary of G1 borders either the outer face of G or an inner non-triangular face Γ of G. Let i denote the length of the cycle bounding Γ. Not all the edges of Γ are on the boundary of G1. Thus Γ contributes at most i − 1 edges to the boundary of G1. If Γ has i − 1 or i − 2 of its edges on the boundary of G1, then by Lemma 3, Γ has to be a lattice polygon, so has to be part of G1 by maximality. Thus Γ has at most i−3 of its edges on the boundary of G1. Therefore,

b1 ≤ b − b∗ +

(i − 3)fi = b − b∗ + F.

i≥4

r6

Q1

H

- r1
- r2


p6

- Q2
- Q3


- r4
- r5


- p2

q3 p4

q4

p5

q1

p7 = p1 q6

P′

- q2


Q6

q5

Q5

p3

Q4

r3

Figure 3. The polygon P′ and its circumscribed hexagon H

The claim now follows from the inequalities in Claims 3 and 7.

- 2.6. An improved isoperimetric inequality. Our next aim is to ﬁnd a better


upper bound for F in a form similar to the upper bound of b∗ in Claim 11. This bound (Claim 12) will then be combined with Claim 10 to obtain a contradiction.

- Claim 12 will follow from our isoperimetric inequality in Lemma 2, which we now restate and prove.


Lemma 2. Let P be a simple polygon with perimeter b, area A, and with the total length of the sides not parallel to any side of some ﬁxed regular hexagon at most b∗. Then

√

3A ≤ b + √ 23 − 1 b∗ 2.

![image 93](<2022-lavolle-tight-bound-number-edges_images/imageFile93.png>)

8

![image 94](<2022-lavolle-tight-bound-number-edges_images/imageFile94.png>)

![image 95](<2022-lavolle-tight-bound-number-edges_images/imageFile95.png>)

Proof. Let h be a ﬁxed regular hexagon. For any simple polygonal path (open or closed) Q, we denote its length by b(Q) and the total length of its sides not parallel to any side of h by b∗(Q). If Q is closed (a polygon), we denote its area by A(Q).

We ﬁrst modify P into a convex polygon P′ with b(P) = b(P′), b∗(P) = b∗(P′), and A(P) ≤ A(P′). We say that a simple polygon Q is a rearrangement of P if there is a bijection between the edge set of Q and the edge set of P such that corresponding edges are parallel and have the same length. Note that for any rearrangement Q of P we have b(P) = b(Q) and b∗(P) = b∗(Q). Among all rearrangements of P ﬁx one, P′, of maximum area. We claim that P′ is convex. If P′ is not convex, then it has two vertices p and q such that the boundary of P′ between p and q lies in the interior of the convex hull of P′. If we replace this part of the boundary by its rotation by 180◦ around the midpoint of p and q, then we obtain a new simple polygon that is still a rearrangement of P, but with larger area. Let H denote the hexagon with sides parallel to the sides of h circumscribed around P′. Number the sides of H in order from 1 to 6. For each i = 1,...,6, let piqi be the segment of P′ on side i of H, such that the points lie in the order p1,q1,p2,q2,...,p6,q6 around P′. Denote the path of P′ between qi and pi+1 by Qi, i = 1,...,6, where p7 = p1.

Note that in a triangle pqr with ∠r = 120◦, the cosine rule gives |pq|2 = |pr|2 + |qr|2 − 2|pr| · |qr|cos120◦

= |pr|2 + |qr|2 + |pr| · |qr|

= 43(|pr| + |qr|)2 + 14(|pr| − |qr|)2 ≥ 43(|pr| + |qr|)2,

![image 96](<2022-lavolle-tight-bound-number-edges_images/imageFile96.png>)

![image 97](<2022-lavolle-tight-bound-number-edges_images/imageFile97.png>)

![image 98](<2022-lavolle-tight-bound-number-edges_images/imageFile98.png>)

hence |pr| + |qr| ≤ √23|pq|. We now apply this to each triangle pi+1qiri to obtain an upper bound on the perimeter of H in terms of b and b∗:

![image 99](<2022-lavolle-tight-bound-number-edges_images/imageFile99.png>)

![image 100](<2022-lavolle-tight-bound-number-edges_images/imageFile100.png>)

6

6

|piqi| +

b(Qi)

b =

i=1

i=1

6

6

6

|ripi+1| +

|qiri| −

= b(H) −

b(Qi)

i=1

i=1

i=1

6

6

6

|qipi+1| by the triangle inequality

|ripi+1| +

|qiri| −

≥ b(H) −

i=1

i=1

i=1

6

6

≥ b(H) − √23

|qipi+1| since ∠ri = 120◦

|qipi+1| +

![image 101](<2022-lavolle-tight-bound-number-edges_images/imageFile101.png>)

![image 102](<2022-lavolle-tight-bound-number-edges_images/imageFile102.png>)

i=1

i=1

6

= b(H) − (√23 − 1)

|qipi+1|

![image 103](<2022-lavolle-tight-bound-number-edges_images/imageFile103.png>)

![image 104](<2022-lavolle-tight-bound-number-edges_images/imageFile104.png>)

i=1

6

≥ b(H) − (√23 − 1)

b(Qi) again by the triangle inequality

![image 105](<2022-lavolle-tight-bound-number-edges_images/imageFile105.png>)

![image 106](<2022-lavolle-tight-bound-number-edges_images/imageFile106.png>)

i=1

= b(H) − (√23 − 1)b∗.

![image 107](<2022-lavolle-tight-bound-number-edges_images/imageFile107.png>)

![image 108](<2022-lavolle-tight-bound-number-edges_images/imageFile108.png>)

By the isoperimetric inequality for hexagons (or L’Huilier’s inequality for hexagons with sides parallel to those of a ﬁxed hexagon) the hexagon with a ﬁxed perimeter maximising the area is regular. It follows that

A ≤ A(P′) ≤ A(H) ≤

√3 24 b(H)2 by the isoperimetric inequality for hexagons

![image 109](<2022-lavolle-tight-bound-number-edges_images/imageFile109.png>)

![image 110](<2022-lavolle-tight-bound-number-edges_images/imageFile110.png>)

√3 24 (b + (√23 − 1)b∗)2,

![image 111](<2022-lavolle-tight-bound-number-edges_images/imageFile111.png>)

≤

![image 112](<2022-lavolle-tight-bound-number-edges_images/imageFile112.png>)

![image 113](<2022-lavolle-tight-bound-number-edges_images/imageFile113.png>)

![image 114](<2022-lavolle-tight-bound-number-edges_images/imageFile114.png>)

and Lemma 2 follows.

We now obtain an improved upper bound for F from the above isoperimetric estimate, again bounding the area from below by using the lower bound on f3 from Claim 4.

Claim 12. F < 61(√12n − 3 −

√12n1 − 3) + 21. Proof. As before, the area A of the boundary polygon of G is at least

![image 115](<2022-lavolle-tight-bound-number-edges_images/imageFile115.png>)

![image 116](<2022-lavolle-tight-bound-number-edges_images/imageFile116.png>)

![image 117](<2022-lavolle-tight-bound-number-edges_images/imageFile117.png>)

![image 118](<2022-lavolle-tight-bound-number-edges_images/imageFile118.png>)

√3

![image 119](<2022-lavolle-tight-bound-number-edges_images/imageFile119.png>)

4 f3. If we substitute this, as well as the upper bounds for b and b∗ from Claims 3 and 11, respectively, and the lower bound for f3 from Claim 4, into Lemma 2, we obtain

![image 120](<2022-lavolle-tight-bound-number-edges_images/imageFile120.png>)

12n + 6 − 6√12n − 3 − 6F ≤ (b + cD)2 < (√12n − 3 − 3 + cD − F)2, where D = √12n − 3 −

![image 121](<2022-lavolle-tight-bound-number-edges_images/imageFile121.png>)

![image 122](<2022-lavolle-tight-bound-number-edges_images/imageFile122.png>)

√12n1 − 3 and c = 2/√3 − 1. Suppose that cD − F ≤ −1/2. Then

![image 123](<2022-lavolle-tight-bound-number-edges_images/imageFile123.png>)

![image 124](<2022-lavolle-tight-bound-number-edges_images/imageFile124.png>)

![image 125](<2022-lavolle-tight-bound-number-edges_images/imageFile125.png>)

12n + 6 − 6√12n − 3 − 6F < (√12n − 3 − 7/2)2.

![image 126](<2022-lavolle-tight-bound-number-edges_images/imageFile126.png>)

![image 127](<2022-lavolle-tight-bound-number-edges_images/imageFile127.png>)

Multiplying out and simplifying, we obtain F > 16√12n − 3− 2413, which contradicts the previous upper bound on F from Claim 6.

![image 128](<2022-lavolle-tight-bound-number-edges_images/imageFile128.png>)

![image 129](<2022-lavolle-tight-bound-number-edges_images/imageFile129.png>)

![image 130](<2022-lavolle-tight-bound-number-edges_images/imageFile130.png>)

Therefore, cD − F > −1/2, which gives the claim.

2.7. The conclusion. We now combine the new estimate for F from Claim 12 with Claim 10 to obtain a contradiction. Claim 12 together with F ≥ 2 (Claim 5) imply that

D := √12n − 3 −

√12n1 − 3 > 9. (10) Again by Claim 12,

![image 131](<2022-lavolle-tight-bound-number-edges_images/imageFile131.png>)

![image 132](<2022-lavolle-tight-bound-number-edges_images/imageFile132.png>)

4 3

1 3

D by (10). Then Claim 10 gives

D =

6F < D + 3 < D +

![image 133](<2022-lavolle-tight-bound-number-edges_images/imageFile133.png>)

![image 134](<2022-lavolle-tight-bound-number-edges_images/imageFile134.png>)

12(n − n1) √12n − 3 + √12n1 − 3

4 3

7 3

7 3 ·

![image 135](<2022-lavolle-tight-bound-number-edges_images/imageFile135.png>)

12(n − n1) <

. It follows that

D + D =

D =

![image 136](<2022-lavolle-tight-bound-number-edges_images/imageFile136.png>)

![image 137](<2022-lavolle-tight-bound-number-edges_images/imageFile137.png>)

![image 138](<2022-lavolle-tight-bound-number-edges_images/imageFile138.png>)

![image 139](<2022-lavolle-tight-bound-number-edges_images/imageFile139.png>)

![image 140](<2022-lavolle-tight-bound-number-edges_images/imageFile140.png>)

![image 141](<2022-lavolle-tight-bound-number-edges_images/imageFile141.png>)

(√12n − 3 + √12n1 − 3) < 12(n − n1). (11)

3 7

![image 142](<2022-lavolle-tight-bound-number-edges_images/imageFile142.png>)

![image 143](<2022-lavolle-tight-bound-number-edges_images/imageFile143.png>)

![image 144](<2022-lavolle-tight-bound-number-edges_images/imageFile144.png>)

![image 145](<2022-lavolle-tight-bound-number-edges_images/imageFile145.png>)

By Claim 9, and using that n1 and n are integers, we have n1 > 43n + 161 , which implies √12n1 − 3 >

![image 146](<2022-lavolle-tight-bound-number-edges_images/imageFile146.png>)

![image 147](<2022-lavolle-tight-bound-number-edges_images/imageFile147.png>)

√12n − 3 and 12(n − n1) < 12√12n − 3. Together with

√3 2

![image 148](<2022-lavolle-tight-bound-number-edges_images/imageFile148.png>)

![image 149](<2022-lavolle-tight-bound-number-edges_images/imageFile149.png>)

![image 150](<2022-lavolle-tight-bound-number-edges_images/imageFile150.png>)

![image 151](<2022-lavolle-tight-bound-number-edges_images/imageFile151.png>)

![image 152](<2022-lavolle-tight-bound-number-edges_images/imageFile152.png>)

![image 153](<2022-lavolle-tight-bound-number-edges_images/imageFile153.png>)

![image 154](<2022-lavolle-tight-bound-number-edges_images/imageFile154.png>)

√3

![image 155](<2022-lavolle-tight-bound-number-edges_images/imageFile155.png>)

(11) we obtain the contradiction 73(1 +

2 ) < 21. This ﬁnishes the induction step and thereby the proof of Theorem 2.

![image 156](<2022-lavolle-tight-bound-number-edges_images/imageFile156.png>)

![image 157](<2022-lavolle-tight-bound-number-edges_images/imageFile157.png>)

![image 158](<2022-lavolle-tight-bound-number-edges_images/imageFile158.png>)

References

- [1] Abel, Z., Demaine E. D., Demaine M. L., Eisenstat S., Lynch J., Schardl T. B.: Who needs crossings? Hardness of plane graph rigidity. 32nd International Symposium on Computational Geometry, Art. No. 3, 15 pp., LIPIcs. Leibniz Int. Proc. Inform., 51, Schloss Dagstuhl. LeibnizZent. Inform., Wadern. (2016)
- [2] Bl˚asj¨, V.: The Isoperimetric Problem. Amer. Math. Monthly 112, 526–566. (2005)
- [3] Blokhuis, A.: Regular ﬁnite planar maps with equal edges. arXiv preprint arXiv:1401.1799.

(1982)

- [4] Brass, P., Moser W. O. J., and Pach. J.: Research Problems in Discrete Geometry. SpringerVerlag, New York. (2005)
- [5] Diestel, R.: Graph theory. 3rd ed. Springer, Berlin Heidelberg. (2006)
- [6] Fejes To´th, L.: Lagerungen in der Ebene auf der Kugel und im Raum. 2nd ed. Springer-Verlag, Berlin-New York. (1972)
- [7] Fejes To´th, L., Fejes To´th G, and Kuperberg W.: Lagerungen: Arrangements in the Plane, on the Sphere, and in Space. Springer-Verlag, Cham. (2023) (Translation of [6] with additional material.)
- [8] Gerbracht, E. H.-A.: Minimal polynomials for the coordinates of the Harborth graph. arXiv:math/0609360. (2006)
- [9] Gerbracht, E. H.-A.: Symbol-crunching the Harborth graph. Adv. in Appl. Math., 47 276–281.

(2011)

- [10] Harborth, H.: Solution to Problem 664A. Elemente der Mathematik 29, 14–15. (1974)
- [11] Harborth, H.: Point sets with equal numbers of unit-distant neighbors (Abstract), Discrete Geometry, 12–18 July 1981, Oberwolfach, Tagungsbericht 31/1981, Mathematisches Forschungsinstitut Oberwolfach. pp. 11–12. (1981)
- [12] Harborth, H.: Match sticks in the plane. In: The Lighter Side of Mathematics. Proceedings of the Eug`ene Strens Memorial Conference on Recreational Mathematics and its History held at the University of Calgary, Calgary, Alberta, August 1986. edited by R. K. Guy and R. E. Woodrow, 281–288. Mathematical Association of America, Washington, D.C. (1994)
- [13] Kurz, S.: Fast recognition of planar non unit distance graphs. Geombinatorics, 21, 25–33.

(2011)

- [14] Kurz, S.: A lower bound for 4-regular planar unit distance graphs. Geombinatorics, 21, 63–72.

(2011)

- [15] Kurz, S. and Mazzuoccolo G.: 3-regular matchstick graphs with given girth, Geombinatorics, 19, 156–173. (2010)


- [16] Kurz, S. and Pinchasi R.: Regular matchstick graphs. Amer. Math. Monthly 118, 264–267.

(2011)

- [17] Lavoll´ee, J. and Swanepoel K. J.: Bounding the Number of Edges of Matchstick Graphs. SIAM Journal on Discrete Mathematics, 36, 777–785. (2022)
- [18] Lavoll´ee, J. and Swanepoel K. J.: The number of small-degree vertices in matchstick graphs. Australas. J. Combin. 85, 92–99. (2023)
- [19] Pach, J. and Agarwal P. J.: Combinatorial Geometry. Wiley, New York. (1995)
- [20] Salvia, R.: A catalog of matchstick graphs. arXiv:1303.5965. (2013)
- [21] Winkler M.: Ein neuer 4-regul¨arer Streichholzgraph. Mitteilungen der Deutschen Mathematiker-Vereinigung, 24, 74–75. (2016)
- [22] Winkler M.: A catalogue of 4-regular matchstick graphs with 63–70 vertices and (2, 4)-regular matchstick graphs with less than 42 vertices which contain only two vertices of degree 2. arXiv preprint arXiv:1705.04715. (2017)
- [23] Winkler, M., Dinkelacker P., and Vogel. S.: Minimal completely asymmetric (4; n)-regular matchstick graphs. arXiv preprint arXiv:1609.06972. (2016)
- [24] Winkler, M., Dinkelacker P., and Vogel. S.: New minimal (4, n)-regular matchstick graphs. Geombinatorics, 27, 26–44. (2017)
- [25] Winkler, M., P. Dinkelacker, and S. Vogel: On the existence of 4-regular matchstick graphs. arXiv preprint arXiv:1705.00293. (2017)
- [26] Winkler, M., P. Dinkelacker, and S. Vogel: A 3-regular matchstick graph of girth 5 consisting of 54 vertices. Geombinatorics, 29, 116–121. (2020)


