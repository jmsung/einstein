---
type: source
kind: paper
title: Some notes on the equivalence of first-order rigidity in various geometries
authors: Franco V. Saliola, Walter Whiteley
year: 2007
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/0709.3354v1
source_local: ../raw/2007-saliola-some-notes-equivalence-first-order.pdf
ingested_for_concept: basin-rigidity.md
cites:
  - ../wiki/concepts/basin-rigidity.md
  - ../wiki/problems/5-*.md
  - ../wiki/problems/6-*.md
  - ../wiki/problems/10-*.md
  - ../wiki/problems/11-*.md
  - ../wiki/problems/12-*.md
  - ../wiki/problems/13-*.md
  - ../wiki/problems/14-*.md
  - ../wiki/problems/15-*.md
  - ../wiki/problems/16-*.md
  - ../wiki/problems/19-*.md
  - ../wiki/problems/22-*.md
---

arXiv:0709.3354v1[math.MG]21Sep2007

SOME NOTES ON THE EQUIVALENCE OF FIRST-ORDER RIGIDITY IN VARIOUS GEOMETRIES

FRANCO V. SALIOLA† AND WALTER J. WHITELEY‡

Abstract. These pages serve two purposes. First, they are notes to accompany the talk Hyperbolic and projective geometry in constraint programming for CAD by Walter Whiteley at the J´anos Bolyai Conference on Hyperbolic Geometry, 8–12 July 2002, in Budapest, Hungary. Second, they sketch results that will be included in a forthcoming paper that will present the equivalence of the ﬁrst-order rigidity theories of bar-and-joint frameworks in various geometries, including Euclidean, hyperbolic and spherical geometry. The bulk of the theory is outlined here, with remarks and comments alluding to other results that will make the ﬁnal version of the paper.

1. Introduction

In this paper, we explore the connections among the theories of ﬁrst-order rigidity of bar and joint frameworks (and associated structures) in various metric geometries extracted from the underlying projective space of dimension n, or Rn+1. The standard examples include Euclidean space, elliptical (or spherical) space, hyperbolic space, and a metric on the exterior of hyperbolic space.

In his book, Pogorelov explored more general issues of uniqueness, and local uniqueness of realizations in these standard spaces, with some ﬁrst-order correspondences as corollaries [11]. We will take the opposite tack – beginning directly with the ﬁrst-order theory, in this paper. We believe this presents a more transparent and accessible starting point for the correspondences. In a second paper, we will use the additional technique of ‘averaging’ in combination with the ﬁrst-order results to transfer results about pairs of objects with identical distance constraints in one space to corresponding pairs in a second space

Like Pogorelov (and perhaps for related reasons) we will begin with the correspondence between the theory in elliptical or spherical space and the theory in Euclidean space (§4). This correspondence of conﬁgurations is direct – using gnomic projection (or central projection) from the upper half sphere to the corresponding Euclidean space. This correspondence between spherical frameworks and their central projections into the plane is also embedded in previous studies of frameworks in dimension d and their one point cones into dimension d + 1 [18].

With a ﬁrm grounding for the ﬁrst-order rigidity in spherical space, it is simpler to work from the spherical n-space to the other metrics extracted from the underlying Rn+1 (§5). The correspondence works for any metric of the form p, q = ni=1+1 aipiqi, ai = 0, in addition to

![image 1](<2007-saliola-some-notes-equivalence-first-order_images/imageFile1.png>)

†Department of Mathematics, 310 Malott Hall, Cornell University, Ithaca, NY 14853-4201 USA (saliola@math.cornell.edu) Work supported, in part, by an NSERC (Canada) research award held at York University and an NSERC (Canada) PGS A award.

‡Department of Mathematics and Statistics, York University, 4700 Keele Street, North York, Ontario, M3J 1P3 Canada (whiteley@mathstat.yorku.ca). Work supported by a grant from NSERC (Canada).

the special case of Euclidean space (with an+1 = 0). It has a particularly simple form, for selected normalizations of the rays as points in the space, such as p, p = ±1, which is the form we present.

Having examined the theory of ﬁrst-order motions, we pause to present the motions as the solutions to a matrix equation RX(G, p)x = 0 for the metric space X (§6). In this setting, we have the equivalent theory of static rigidity working with the row space and row dependences (the self-stresses) of these matrices, instead of the column dependencies (the motions). The correspondence is immediate, but it takes a particular nice form for the ‘projective’ models in Euclidean space of the standard metrics. In this setting, the rigidity correspondence is a simple matrix multiplication:

RX(G, p)[TXY ] = RY (G, p)

for the same underlying conﬁguration p, where [TXY ] is a block diagonal matrix with a block entry for each vertex, based on how the sense of ‘perpendicular’ is twisted at that location from one metric to the other. As a consequence of this simple correspondence of matrices, we see that row dependencies (the static self-stresses) are completely unchanged by the switch in metric. As a biproduct of this static correspondence, there is a correspondence for the ﬁrst-order rigidity of the structures with inequalities, the tensegrity frameworks, which are well understood as a combination of ﬁrst-order theory and self-stresses of the appropriate signs for the edges with pre-assigned inequality constraints.

As this shared underlying statics hints, there is a shared underlying projective theory of statics (and associated ﬁrst-order kinematics) [4].

We will not present that theory here but we note the projective invariance, in all the metrics, of the ﬁrst-order and static theories (§7). There are various extensions that follow from this underlying projective theory, such as inclusion of ‘vertices at inﬁnity’ in Euclidean space [4], and the possibility that polarity has a role to play (see below).

As an application of these correspondences, we consider a classical theory of rigidity for polyhedra – the theorems of Cauchy, Alexandrov, and the associated theory of Andreev. This theory provides theorems about the ﬁrst-order rigidity of convex polyhedra and convex polytopes with either rigid faces, or 2-faces triangulated with bars and joints in dimensions d ≥ 3, in Euclidean space. Since the basic concepts of convexity transfer among the metrics (if we remove the equator on the sphere, or the corresponding line at inﬁnity in Euclidean space), this ﬁrst-order and static theory immediately transfers to identical theorems in the other metric spaces (§7). There are some ﬁrst-order extensions of Cauchy’s Theorem to versions of local convexity, which will automatically extend to the various metrics and on through to hyperplanes and angles, giving additional generalizations. Moreover, this theory for hyperplanes and angles will be projectively invariant, if we are careful with the transfer of concepts such as ‘convexity’ through the projective transformations.

In hyperbolic space, there is a correspondence between rigidity of ‘bar-and-joint frameworks’ with vertices and distance constraints in the exterior hyperbolic space (or ideal points) and planes and angle constraints in the interior hyperbolic space. We present this correspondence directly, although it can be viewed as a polarity about the absolute. With this correspondence, the ﬁrst-order Cauchy theory in exterior hyperbolic space gives a ﬁrst-order theory for planes and angles in hyperbolic space. This result turns out to be a generalization of the ﬁrst-order version of Andreev’s Theorem. In this setting, the constraint that angles be

less than π/2 disappears and the angles have the full range of angles in a convex polyhedron (< π).

Moreover, as this hints, there is a correspondence, via spherical polarity, which connects the ﬁrst-order Cauchy Theorem in the spherical or elliptic space with an Andreev style ﬁrst-order theorem for planes and angles of a simple convex polytope in elliptical geometry (§none). The eﬀect of polarity in Euclidean space is drastically diﬀerent. It has an interesting, and distinctive interpretations in dimensions d = 2 and d = 3 [22, 23].

The general problem of characterizing which graphs have some (almost all) realizations in d-space as ﬁrst-order rigid frameworks is hard for dimensions d ≥ 3. With these correspondences, we realize that this problem is identical in all the metric spaces and we will not get additional leverage by comparing ﬁrst-order behaviour under the various metrics.

On the other hand, in general geometric constraint programming in ﬁelds such as CAD, there is an interest in more general systems of geometric objects and general constraints. For example, circles of variable radii with angles of intersection as constraints are in interest in CAD. As people familiar with hyperbolic geometry may realize, these are equivalent, both a ﬁrst-order and at all orders, to planes and angles in hyperbolic 3-space. The correspondence presented here provides the ﬁnal step in the correspondence between circles and angles in the plane and points and distances in Euclidean 3-space [13].

The basic ﬁrst-order correspondence among metrics should extend to diﬀerentiable surfaces from these discrete structures. The major diﬀerence here is that static rigidity and ﬁrst-order rigidity are distinct concepts in the this world which corresponds to inﬁnite matrices. Still the correspondence should apply to both theories, and all the metrics.

2. First-Order Rigidity in En

- 2.1. Euclidean n-space. Let En denote the set of vectors in Rn+1 with xn+1 = 1, En = {x ∈ Rn+1 | e · x = 1},

where e = (0, 0, . . ., 1) ∈ Rn+1. An m-plane of En is the intersection of En with an (m + 1)subspace of Rn+1. The distance between x, y ∈ En is dE(x, y) = |x − y| = ni (xi − yi)2.

![image 2](<2007-saliola-some-notes-equivalence-first-order_images/imageFile2.png>)

- 2.2. Frameworks and rigidity in En. A graph G = (V, E) consists of a ﬁnite vertex set V = {1, 2, . . ., v} and an edge set E, where E is a collection of unordered pairs of vertices. A bar-and-joint framework G(p) in En is a graph G together with a map p : V → En. Let

pi denote p(i).

A motion of the framework G(p) is a continuous family of functions p(t) : V → En with p(0) = p such that for {i, j} ∈ E, dE(pi(t), pj(t)) = cij, where cij is a constant, for all t. A framework is rigid if all motions are trivial: for each t, there is a rigid motion At of En, such that At(pi) = pi(t), for all i ∈ V .

- 2.3. Motivation for ﬁrst-order rigidity. Suppose p(t) is a motion of the framework G(p)


in En diﬀerentiable at t = 0. Since dE(pi(t), pj(t)) = cij for each {i, j} ∈ E, the derivative of p(t) must satisfy

(pi − pj) · (p′i(0) − p′j(0)) = 0, where x·y denotes the Euclidean inner product of the vectors x and y. Since the framework lies in En during the motion (pk(t) ∈ En for all k ∈ V ), pk(t) satisﬁes e · pk(t) = 0 for all

k ∈ V . Hence its derivative satisﬁes,

e · p′i(0) = 0 for each i ∈ V . This motivates the following deﬁnition.

- 2.4. First-order rigidity in En. A ﬁrst-order motion of the framework G(p) in En is a map u : V → Rn+1 satisfying, for each {i, j} ∈ E and k ∈ V ,

- (1) (pi − pj) · (ui − uj) = 0 and e · uk = 0, where ui denotes u(i).


![image 3](<2007-saliola-some-notes-equivalence-first-order_images/imageFile3.png>)

Figure 1. u is a ﬁrst-order motion if (pi −pj) · ui = (pi −pj) · uj for all edges {i, j}. That is, the projection of ui onto pi − pj must equal the projection of uj onto pi − pj.

A trivial ﬁrst-order motion of En is a map u : En → Rn+1 satisfying (x − y) · (u(x) − u(y)) = 0 and e · u(z) = 0,

for all x, y and z in En. G(p) is ﬁrst-order rigid in En if all the ﬁrst-order motions of the framework G(p) are restrictions of trivial ﬁrst-order motions of En.

- 2.5. Remark. Any rigid motion of En yeilds a trivial ﬁrst-order motion of a given framework: the isometry restricts to a motion of the framework whose derivative satisﬁes the equations in (1).
- 2.6. Remark. First-order rigidity is a good indicator of rigidity: ﬁrst-order rigidity implies rigidity, but not conversely.


3. First-Order Rigidity in Sn+

- 3.1. Spherical n-Space. Let Sn+ denote the upper hemisphere of the unit sphere in Rn+1, Sn+ = {x ∈ Rn+1 | x · x = 1, e · x > 0},

An m-plane of Sn+ is the intersection of Sn+ with an (m + 1)-subspace of Rn+1. The distance between two points x, y ∈ Sn+ is given by the angle subtended by the vectors x and y, dS

+

(x, y) = arccos(x · y).

- 3.2. Frameworks and rigidity in Sn+. A bar-and-joint framework G(p) in Sn+ is a graph G together with a map p : V → Sn+. A motion of the framework G(p) in Sn+ is a continuous


family of functions p(t) : V → Sn+ with p(0) = p such that for {i, j} ∈ E, dS

(pi(t), pj(t)) = cij, where cij is a constant, for all t. A framework is rigid if all motions are trivial: for each t, there is a rigid motion At of Sn+, such that At(pi) = pi(t), for all i ∈ V .

+

- 3.3. Motivation for ﬁrst-order rigidity in Sn+. To extend the deﬁnitions of ﬁrst-order motion and ﬁrst-order rigidity to frameworks in Sn+, mimic the motivation presented in section 2.3. If p(t) is a motion of a framework G(p) in Sn+, then for all t and {i, j} ∈ E,

dS

+

(pi(t) · pj(t)) = cij, where cij is constant for all {i, j} ∈ E, and for all t and k ∈ V ,

pk(t) · pk(t) = 1. Equivalently, for all t, {i, j} ∈ E and k ∈ V ,

pi(t) · pj(t) = coscij, pk(t) · pk(t) = 1.

If the motion p(t) is diﬀerentiable at t = 0, then p(t) must satisfy, pi · p′j(0) + p′i(0) · pj = 0,

pk · p′k(0) = 0. This leads to the following deﬁnition.

- 3.4. First-Order Rigidity in Sn+. A ﬁrst-order motion of the framework G(p) in Sn+ is a map u : V → Rn+1 satisfying, for each {i, j} ∈ E and for each k ∈ V ,

(2) pi · uj + pj · ui = 0 and pk · uk = 0. A trivial ﬁrst-order motion of Sn+ is a map u : Sn+ → Rn+1 satisfying x · u(y) + y · u(x) = 0 and z · u(z) = 0,

for all x, y and z in En. The framework G(p) is ﬁrst-order rigid in Sn+ if all ﬁrst-order motions of G(p) are restrictions of trivial ﬁrst-order motions.

- 3.5. Remark. Note that the equations in (2) are equivalent to the following conditions,

(pi − pj) · (ui − uj) = 0 and pk · uk = 0, which are similar to the equations deﬁning ﬁrst-order rigidity in En.

- 3.6. Remark. If G(p) is a bar-and-joint framework in Sn+, then the graph obtained from G by adjoining a new vertex with edges incident with all vertices of G, together with the map p : V ∪ {v + 1} → En+1 given by


p(i) if i = v + 1 0 if i = v + 1

p(i) =

,

is ﬁrst-order rigid in En+1 iﬀ G(p) is ﬁrst-order rigid in Sn++1. That is, frameworks in Sn+ can be modeled by the cone on the same framework in En+1.

4. Equivalence of First-Order Rigidity in Sn+ and En.

This section presents two maps, a map carrying a framework G(p) in Sn+ into a framework G(q) in En, and a map carrying the ﬁrst-order motions of G(p) into ﬁrst-order motions of G(q). The latter map carries trivial ﬁrst-order motions of Sn+ to trivial ﬁrst-order motions of En, yielding the result G(p) is ﬁrst-order rigid iﬀ G(q) is ﬁrst-order rigid.

- 4.1. Mapping frameworks and ﬁrst-order motions. If G(p) is a framework in Sn+, then G(ψ ◦ p) is a framework in En, where ψ : Sn → En is given by ψ(x) = x/(e · x). The inverse of ψ is given by ψ−1(x) = x/√x · x.

![image 4](<2007-saliola-some-notes-equivalence-first-order_images/imageFile4.png>)

![image 5](<2007-saliola-some-notes-equivalence-first-order_images/imageFile5.png>)

Figure 2. Mapping ﬁrst-order motions of a framework in Sn+ to ﬁrst-order motions of a framework in En.

If u is a ﬁrst-order motion of the framework G(p) in Sn+, let ϕ denote the map ϕ : ui  →

1 e · pi

![image 6](<2007-saliola-some-notes-equivalence-first-order_images/imageFile6.png>)

(ui − (ui · e)e). If G(q) is a framework in En with ﬁrst-order motion v, then ϕ−1 is given by ϕ−1 : vi  →

1 √qi · qi

![image 7](<2007-saliola-some-notes-equivalence-first-order_images/imageFile7.png>)

![image 8](<2007-saliola-some-notes-equivalence-first-order_images/imageFile8.png>)

(vi − (vi · qi)e) .

Observe that ϕ and ϕ−1 map into the appropriate tangent spaces: ψ−1(qi) · ϕ−1(vi) = 0 and ϕ(ui) · e = 0.

- 4.2. Theorem. u is a ﬁrst-order motion of the framework G(p) in Sn+ iﬀ ϕ ◦ u is a ﬁrstorder motion of the framework G(ψ ◦ p) in En. Moreover, u is a trivial ﬁrst-order motion iﬀ ϕ ◦ u ◦ ψ−1 is a trivial ﬁrst-order motion.


Pf. Note that (ψ(pi) − ψ(pj)) · (ϕ(ui) − ϕ(uj)) =

pi · ui (e · pi)2 −

pi · uj + pj · ui (e · pi)(e · pj)

pj · uj (e · pj)2

- (3) .


+

![image 9](<2007-saliola-some-notes-equivalence-first-order_images/imageFile9.png>)

![image 10](<2007-saliola-some-notes-equivalence-first-order_images/imageFile10.png>)

![image 11](<2007-saliola-some-notes-equivalence-first-order_images/imageFile11.png>)

If u is a ﬁrst-order motion of G(p), then ui · pi = 0 for all i ∈ V , and pi · uj + pj · ui = 0 for all {i, j} ∈ E. By (3), (ψ(pi) − ψ(pj)) · (ϕ(ui) − ϕ(uj)) = 0 for all {i, j} ∈ E. The deﬁnition of ϕ ensures that ϕ(ui) · e = 0. Therefore, ϕ ◦ u is a ﬁrst-order motion of G(ψ ◦ p).

Conversely, suppose ϕ ◦ u is a ﬁrst-order motion of G(ψ ◦ p). Then for all {i, j} ∈ E, (ψ(pi) − ψ(pj)) · (ϕ(ui) − ϕ(uj)) = 0. The observation at the end of the 4.1 gives that pi ·ui = ψ−1(ψ(pi))·ϕ−1(ϕ(ui)) = 0 for all i ∈ V . Equation (3) reduces to pi ·uj +pj ·ui = 0.

- So u is a ﬁrst-order motion of G(p). Suppose u is a trivial ﬁrst-order motion. Then x · u(x) = 0 for all x ∈ Sn+ and x · u(y) +

y · u(x) = 0 for all x, y ∈ Sn+. Let v : En → Rn+1 denote the composition φ ◦ u ◦ ψ−1. If x, y ∈ En with x denoting ψ−1( x) and y denoting ψ−1( y), then (3) gives

( x − y) · (v( x) − v( y)) =

x · u(x) (e · x)2 −

![image 12](<2007-saliola-some-notes-equivalence-first-order_images/imageFile12.png>)

x · u(y) + y · u(x) (e · x)(e · y)

![image 13](<2007-saliola-some-notes-equivalence-first-order_images/imageFile13.png>)

+

y · u(y) (e · y)2

![image 14](<2007-saliola-some-notes-equivalence-first-order_images/imageFile14.png>)

= 0.

- So v is a trivial ﬁrst-order motion. The converse follows similarly. Corollary. G(p) is ﬁrst-order rigid in Sn+ iﬀ G(ψ ◦ p) is ﬁrst-order rigid in En.


- 4.3. Remark. Sn+ versus Sn: Given a discrete framework, there exists a rotation of the nsphere such that no vertex of the framework lies on the equator of the sphere. Therefore, we need not restrict our frameworks to a hemisphere.


5. Equivalence of First-Order Rigidity in Other Geometries.

- 5.1. Geometries. For x, y ∈ Rn+1, let x, y k denote the function x, y k = x1y1 + · · · + xn−k+1yn−k+1 − xn−k+2yn−k+2 − · · · − xn+1yn+1,

and let Xc,kn denote the set,

Xc,kn = {x ∈ Rn+1 | x, x k = c, xn+1 > 0}, for some constant c = 0 and k ∈ N. We write Xn to simplify notation, if c and k are understood. If k = 1 and c = −1, then Xn is hyperbolic space, Hn. If k = 1 and c = 1, then Xn is exterior hyperbolic space, Dn. Spherical space Sn+ is the case k = 0, c = 1. Note that En = Xn for any choice of c and k.

- 5.2. Remark. In more generality we can replace x, y k with x, y = a1x1y1 + · · · + an+1xn+1yn+1,

where ai = 0 for all i, with the exception for Euclidean space: a1 = a2 = · · · = an = 1 and an+1 = 0.

- 5.3. First-order rigidity in Xn. A metric dX can be placed on Xn so that dX(x, y) is a function of x, y k. A suﬃcient condition for the distance dX(x, y) remaining constant is the requirement x, y k remain constant. Therefore, the same analysis motivates the following extensions of the deﬁnitions of ﬁrst-order rigidity to Xn.


A bar-and-joint framework G(p) in Xn is a graph G together with a map p : V → Xn. A ﬁrst-order motion of the framework G(p) in Xn is a map u : V → Rn+1 satisfying for each {i, j} ∈ E,

- (4) pi, uj k + pj, ui k = 0,


and for each i ∈ V ,

- (5) pi, ui k = 0. A trivial ﬁrst-order motion of Xn is a map u : Xn → Rn+1 satisfying


x, u(y) k + y, u(x) k = 0 and z, u(z) k = 0 for all x, y, z ∈ Xn. G(p) is ﬁrst-order rigid in Xn if all ﬁrst-order motions of G(p) are the restrictions of trivial ﬁrst-order motions of Xn.

- 5.4. Xn and En. In section 4 we established the equivalence between ﬁrst-order rigidity in

En and ﬁrst-order rigidity in Sn+. We need only demonstrate the equivalence holds between the ﬁrst-order rigidity theories of Xn and Sn+.

- 5.5. Xn and Sn+. Let ψS

+

: Xn → Sn+ denote the map x  → x/√x · x, and let ϕS

![image 15](<2007-saliola-some-notes-equivalence-first-order_images/imageFile15.png>)

+

denote the map

ϕS

+

: ui  →

Jk(ui) √pi · pi

![image 16](<2007-saliola-some-notes-equivalence-first-order_images/imageFile16.png>)

![image 17](<2007-saliola-some-notes-equivalence-first-order_images/imageFile17.png>)

, where Jk(x) = (x1, · · · , xn−k+1, −xn−k+2, · · · , −xn+1).

Figure 3. Mapping a bar-and-joint framework from the spherical plane S2+ into the hyperbolic plane H2.

- 5.6. Theorem. G(p) is ﬁrst-order rigid in Xn iﬀ G(ψS


+ ◦ p) is ﬁrst-order rigid in Sn+. Pf. Since, x, y k = x · Jk(y) we have

pj, uj k pj · pj

pi, ui k pi · pi −

pi, uj k + pj, ui k √pi · pi√pj · pj

+

ψS

(pi) − ψS

(pj) · ϕS

(ui) − ϕS

(uj) =

.

![image 18](<2007-saliola-some-notes-equivalence-first-order_images/imageFile18.png>)

![image 19](<2007-saliola-some-notes-equivalence-first-order_images/imageFile19.png>)

![image 20](<2007-saliola-some-notes-equivalence-first-order_images/imageFile20.png>)

+

+

+

+

![image 21](<2007-saliola-some-notes-equivalence-first-order_images/imageFile21.png>)

![image 22](<2007-saliola-some-notes-equivalence-first-order_images/imageFile22.png>)

As in the proof of Theorem 4.2, the above equation and the deﬁnitions of ψS

and ϕS

give that ϕS

+

+

+ ◦ p) iﬀ u is a ﬁrst-order motion of G(p).

+ ◦ u is a ﬁrst-order motion of G(ψS

It is clear that trivial motions of Sn+ map to trivial motions of Xn. However, a trivial motion of Xn maps onto a “trivial motion” of a proper subset of Sn+. The following fact ﬁnishes of this proof.

![image 23](<2007-saliola-some-notes-equivalence-first-order_images/imageFile23.png>)

Figure 4. Mapping ﬁrst-order motions of a framework in Sn+ to ﬁrst-order motions of a framework in Hn.

Fact. Given a ﬁrst-order motion u of Kn+1, the complete graph on n + 1 vertices in En, there exists a unique trivial ﬁrst-order motion of En extending u.

(This result and the equivalence of the ﬁrst-order theories of En and Sn+ give the corresponding result for Sn+, which was needed to ﬁnish the proof of the proceeding theorem.)

- 5.7. Remark. There is no obstruction to deﬁning a framework with vertices in Hn and Dn: the equations deﬁning ﬁrst-order motions provide formal constraints between these vertices, although the geometric interpretations of these constraints may not be obvious. In general, the theorem holds for frameworks with vertices on the surface x, x k = ±1, but not with vertices on x, x k = 0.


6. The Rigidity Matrix

- 6.1. Projective models of Xn. The projective model of Xn is the subset of En obtained by projecting from the origin the points of Xn onto En,


1 e · x

x x ∈ Xn ⊂ En.

![image 24](<2007-saliola-some-notes-equivalence-first-order_images/imageFile24.png>)

The projective model of hyperbolic n-space Hn is the interior of the unit n-ball Bn of En and the projective model of exterior hyperbolic n-space Dn is the exterior of Bn. The unit (n − 1)-sphere Sn−1 is the absolute, the points at inﬁnity of hyperbolic geometry. Spherical n-space is model projectively by En.

![image 25](<2007-saliola-some-notes-equivalence-first-order_images/imageFile25.png>)

Figure 5. Mapping ﬁrst-order motions of a framework in Sn+ to ﬁrst-order motions of a framework in En.

Since we are now restricting our attention to points in En, we identify En with Rn and write PXn to denote the projective model of Xn as a subset of Rn. Distance in PXn is calculated by normalizing the points into Xn and applying the deﬁnition of distance in Xn. For example, the distance between points x and y in PSn+ (so x, y ∈ Rn) is

dPS

+

(x, y) = arccos

and for points x and y in PHn,

1 + x · y √1 + x · x√1 + y · y

![image 26](<2007-saliola-some-notes-equivalence-first-order_images/imageFile26.png>)

![image 27](<2007-saliola-some-notes-equivalence-first-order_images/imageFile27.png>)

![image 28](<2007-saliola-some-notes-equivalence-first-order_images/imageFile28.png>)

,

dPH(x, y) = arccosh

1 − x · y √1 − x · x√1 − y · y

![image 29](<2007-saliola-some-notes-equivalence-first-order_images/imageFile29.png>)

![image 30](<2007-saliola-some-notes-equivalence-first-order_images/imageFile30.png>)

![image 31](<2007-saliola-some-notes-equivalence-first-order_images/imageFile31.png>)

.

- 6.2. The rigidity matrix of a framework. A ﬁrst-order motion u : V → Rn of the framework G(p) in Rn, satisﬁes


(pi − pj) · (ui − uj) = 0.

This system of homogeneous linear equations, indexed by the edges of G, induces a linear transformation with matrix RE(G, p), called the rigidity matrix of G(p),

i · · · j . .

  .

  

{i, j} · · · pi − pj · · · pj − pi · · ·

RE(G, p) =

. .

The kernel of RE(G, p) is precisely the space of ﬁrst-order motions of G(p).

A ﬁrst-order motion u : V → Rn of the framework G(p) in PHn, PDn or PSn satisﬁes (kij + kji) · (ui + uj) = 0, where kij is

 

1−pi·pj

1−pi·pi pi − pj, for PHn or PDn

![image 32](<2007-saliola-some-notes-equivalence-first-order_images/imageFile32.png>)

kij =

.

1+pi·pj



1+pi·pi pi − pj, for PSn+

![image 33](<2007-saliola-some-notes-equivalence-first-order_images/imageFile33.png>)

The matrix of the linear transformation induced by this system of linear equations is the rigidity matrix RX(G, p) of G(p),

RX(G, p) =

Note that kij depends on X.

i · · · j . .

  

{i, j} · · · kij · · · kji · · ·

. .

  .

- 6.3. Transforming rigidity matrices. Let TK(G, p) denote the matrix


  ,

  

Tp

0 0 0 0 Tp

1

0 0 0 0

2

TK(G, p) =

... 0 0 0 0 Tp

v

= I + K(pk(i)p(kj)) (I is the n × n identity matrix and (p(ki)p(kj)) is the n × n matrix

where Tp

k

with p(ki)p(kj) as entry (i, j), where p(ki) is the i-th component of pk). For example, for n = 3 and pk = (x1, x2, x3),

 .

 

1 + Kx21 Kx1x2 Kx1x3 Kx1x2 1 + Kx22 Kx2x3 Kx1x3 Kx2x3 1 + Kx23

Tp

=

k

Theorem. Let G(p) be a framework with p ∈ Rn. Then

- (1) TK(G, p) satisﬁes

RPH × T−1(G, p) = RE(G, p) and RPS

+ × T1(G, p) = RE(G, p);

- (2) G(p) is ﬁrst-order rigid in PSn+ iﬀ G(p) is ﬁrst-order rigid in PEn;
- (3) G(p) is ﬁrst-order rigid in PHn∪PDn iﬀ G(p) is ﬁrst-order rigid in PEn and pi·pi = 1 for all i ∈ V (no vertex is on the absolute).


![image 34](<2007-saliola-some-notes-equivalence-first-order_images/imageFile34.png>)

Figure 6. A visual summary of the equivalence of ﬁrst-order rigidity in the projective models of hyperbolic geometry H, spherical geometry S and Euclidean geometry E. Here TSE denotes the linear transformation T1(G, p) deﬁned in the text, TES the inverse of TSE.

multiplies only the columns corresponding to vertex i, we need only verify kij × Tp

Pf. (1) Since Tp

i

= pi − pj. This is a straightforward calculation, kij × (column ℓ of Tp

i

)

i

1 + K(pi · pj) 1 + K(pi · pi)

pi − pj · eℓ + Kp(iℓ)pi

=

![image 35](<2007-saliola-some-notes-equivalence-first-order_images/imageFile35.png>)

1 + K(pi · pj) 1 + K(pi · pi)

pi · eℓ + Kp(iℓ)(pi · pi) − p(jℓ) + Kp(iℓ)(pj · pi)

=

![image 36](<2007-saliola-some-notes-equivalence-first-order_images/imageFile36.png>)

1 + K(pi · pj) 1 + K(pi · pi)

(1 + K(pi · pi))p(iℓ) − p(jℓ) + Kp(iℓ)(pj · pi)

=

![image 37](<2007-saliola-some-notes-equivalence-first-order_images/imageFile37.png>)

= (1 + K(pi · pj)) pi(ℓ) − p(jℓ) + Kp(iℓ)(pj · pi)

= pi(ℓ) + Kpi(ℓ)(pi · pj) − p(jℓ) − Kp(iℓ)(pj · pi)

= pi(ℓ) − pj(ℓ), which is column ℓ of pi − pj.

## (2), (3): Since the determinant of TK(G, p) is the product vi=1 det(Tp

) and det(Tp

i

) = 1 + K(pi · pi),

i

the dimension of the vector space of ﬁrst-order motions of G(p) is the same in each geometry iﬀ 1 + K(pi · pi) = 0 for all i ∈ V .

- 6.4. Remark. It is well-known that the rank of the rigidity matrix, and thus ﬁrst-order rigidity, of a framework in En is invariant under projective transformations of En. Due to the equivalence of ﬁrst-order theories, the same is true of frameworks in Xn. (In fact, there exists an underlying projective theory.) Intuitively at least, this projective invariance suggests the equivalences presented in this paper since all the geometries discusses can be obtained from projective geometry by choosing an appropriate set of transformations.


# Underlying Projective Theory

Signed weighted points, segments, areas, ..., weighted centers of motion

|RP(G,p)|
|---|


P

Euclidean Metric

H

|Hyperbolic Metric|
|---|


Spherical Metric

H

E

S

|RE(G,p)|
|---|


H

S

|RH(G,p)|
|---|


|RS(G,p)|
|---|


Invariance under projective transformations.

Points at infinity in Euclidean metric. Polarity has some interpretations.

Figure 7. A visual summary of the underlying projective theory: hyperbolic space H, Euclidean space E and spherical space S can be realized as subgeometries of projective geometry.

7. The First-Order Uniqueness Theorems of Andreev and Cauchy-Dehn An immediate consequence of the equivalence of these ﬁrst-order rigidity theories is the

ability to transfer results between the theories.

- 7.1. The Cauchy-Dehn Theorem. The Cauchy-Dehn theorem for polytopes in En states that a convex, triangulated polyhedron in En, n ≥ 3, is ﬁrst-order rigid. Before the generalization of this theorem can be stated, convexity in Xn needs to be deﬁned. A set S ⊂ Xn is convex if, for any line L of Xn, L ∩ S is connected. Therefore, S ⊂ Xn is convex iﬀ ψE(S) ⊂ En is convex.


Theorem. (Cauchy-Dehn) A convex, triangulated polytope P in Xn, n ≥ 3, is ﬁrst-order rigid.

- 7.2. A ﬁrst-order version of Andreev’s uniqueness theorem. If p denotes a point of


Dn, then the set of points x in Rn+1 satisfying p, x 1 = 0 (orthogonal in the hyperbolic sense) deﬁnes a unique hyperplane of Rn+1 through the origin. Therefore, to each point of p, there corresponds a unique hyperplane of Hn,

P = {x ∈ Hn | p, x 1 = 0}, and conversely.

If q is another point of Dn with Q the corresponding hyperplane of Hn, the angle of intersection of the hyperplanes P and Q is deﬁned to be arccos( p, q 1). So equations (4) and (5) deﬁning a ﬁrst-order motion u of a framework G(p) in Dn,

pi, uj k + pj, ui k = 0 and pi, ui k = 0,

are precisely the conditions deﬁning a “ﬁrst-order motion” of a collection of planes under angle constraints (a bar-and-joint framework is merely a collection of points under distance constraints). Polyhedra with ﬁxed dihedral angles are examples of such objects.

Under this point-plane correspondence of Dn and Hn, the Cauchy-Dehn theorem for Dn gives a ﬁrst-order version of Andreev’s uniqueness theorem. Indeed, a simple, convex polytope in Hn is a triangulated, convex polytope in Dn. We use stiﬀ to denote the analogous deﬁnition of ﬁrst-order rigid.

Theorem. (Andreev) If M is a simple, convex polytope in Hn, n ≥ 3, then M is stiﬀ.

- 7.3. Remark. The usual hypothesis of Andreev’s theorem requires the polytope M to have dihedral angles not exceeding π/2. This supposition implies M is simple.
- 7.4. Remark. The point-plane correspondence described above is known as polarity. There is a version of this result for the sphere that requires a better discussion of polarity on the sphere.


References

- [1] A. D. Alexandrov, Konvex polyedrer, German transl. Akademie-Verlag, Berlin, 1958.
- [2] E. M. Andreev, Convex polyhedra in Lobacˇevski˘i spaces, Mat. Sb. (N.S.) 81 (123) 1970, 445–478
- [3] A. Cauchy, Deuxieme memoire sur les polygons et les polyedres, J. Ecole POlytechnique XVIe Cahier

(1831), 87-98.

- [4] H. Crapo and W. Whiteley, Statics of frameworks and motions of panel structures: a projective geometric introduction, Structural Topology 6 (1982), 43-82.
- [5] R. Connelly, On generic global rigidity, in “Applied Geometry and Discrete Mathematics”, DIMACS Ser. Discrete Math. Theoret. Comput. Sci. 4 (1990), 147–155.
- [6] H.S.M. Coxeter, An Introduction to Non-Euclidean Geometry, Math. Assoc. of Amer., 6th Edition 1998.
- [7] J. Graver, B. Servatius and H. Servatius, Combinatorial Rigidity, AMS 1994.


- [8] L. Henneberg, (1968). Die graphische Statik der starren Systeme Leipzig 1911, Johnson Reprint.
- [9] G. Kramer, Solving Geometric Constraint Systems (A case study in kinematics), MIT Press 1992
- [10] G. Laman, On graphs and the rigidity of plane skeletal structures, J. Engin. Math. 4 (1970), 331–340.
- [11] A. V. Pogorelov, Extrinsic Geometry of Convex Surfaces, Translation of the 1969 edition, Translations of Mathematical Monographs 35, American Mathematical Society, 1973.
- [12] B. Roth and W. Whiteley, Tensegrity frameworks, Trans. AMS 177 (1981),419-446.
- [13] F. Saliola and W. Whiteley, Constraining plane conﬁgurations in CAD: circles, lines and angles in the plane, submitted.
- [14] J.J. Stoker, Geometric theorems regarding polyhedra in the large, Comm. Pure Appl. Math. 21 (1968), 119–168.
- [15] T-S. Tay and W. Whiteley, Generating all isostatic frameworks, Structural Topology 11 (1985), 21–69.
- [16] T-S. Tay, N. White and W. Whiteley, Skeletal Rigidity of Symplicial Complexes I, II, European Journal of Combinatorics 16 (1995), 381–403, 503–523.
- [17] W. Whiteley, Introduction to Structural Geometry I, II, Notes, 1977 (available at York University)
- [18] W. Whiteley, Cones, inﬁnity and one-story buildings, Structural Topology 8 (1983), 53–70.
- [19] W. Whiteley, Inﬁnitesimal rigidity of a bipartite framework, Paciﬁc J. Math. 110 (1984), 233–255.
- [20] W. Whiteley, Inﬁnitesimally rigid polyhedra I: statics of frameworks, Trans. Amer. Math. Soc. 285

(1984), 431–461.

- [21] W. Whiteley, Inﬁnitesimally rigid polyhedra II: modiﬁed spherical frameworks, Trans. Amer. Math. Soc. 306 (1988), 115–139.
- [22] W. Whiteley, Rigidity and polarity I: statics of sheet structures, Geometriae Dedicata 22 (1987), 329-362
- [23] W. Whiteley, Rigidity and polarity II: weaving lines and tensegrity frameworks , Geometriae Dedicata 23 (1989), 75-79
- [24] W. Whiteley, Matroids for discrete applied geometry, in ‘Matroid Theory’, J. Bonin, J. Oxley and B. Servatius (eds.), Contemporary Mathematics 197, AMS, 1996, 171–311.


