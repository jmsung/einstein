# arXiv:1204.0235v1[math.OC]1Apr2012

## PACKING ELLIPSOIDS WITH OVERLAP∗ CAROLINE UHLER† AND STEPHEN J. WRIGHT ‡

Abstract. The problem of packing ellipsoids of diﬀerent sizes and shapes into an ellipsoidal container so as to minimize a measure of overlap between ellipsoids is considered. A bilevel optimization formulation is given, together with an algorithm for the general case and a simpler algorithm for the special case in which all ellipsoids are in fact spheres. Convergence results are proved and computational experience is described and illustrated. The motivating application — chromosome organization in the human cell nucleus — is discussed brieﬂy, and some illustrative results are presented.

Key words. ellipsoid packing, trust-region algorithm, semideﬁnite programming, chromosome territories.

AMS subject classiﬁcations. 90C22, 90C26, 90C46, 92B05

1. Introduction. Shape packing problems have been a popular area of study in discrete mathematics over many years. Typically, such problems pose the question of how many uniform objects can be packed without overlap into a larger container, or into a space of inﬁnite extent with maximum density. In ellipsoid packing problems, the smaller shapes are taken to be ellipsoids of known size and shape. In three dimensions, the ellipsoid packing problem has become well known in recent years, due in part to colorful experiments involving the packing of M&Ms [6].

Finding densest ellipsoid packings is a diﬃcult computational problem. Most studies concentrate on the special case of sphere packings, with spheres of identical size. Here, optimal densities have been found for the inﬁnite Euclidean space of dimensions two and three. In two dimensions, the densest circle packing is given by the hexagonal lattice (see [16]), where each circle has six neighbors. The density of this packing (that is, the proportion of the space ﬁlled by the circles) is π/√12. In dimension three, it has been proven recently by Hales [8] that the face-centered cubic (FCC) lattice achieves the densest packing. In this arrangement, every sphere has 12 neighboring spheres and the density is π/√18. For dimensions higher than 3, the problem of ﬁnding the densest sphere packing is still open.

A problem related to sphere packing is sphere covering. Here, the goal is to ﬁnd an arrangement that covers the space with a set of uniform spheres, as economically as possible. Overlap is not only allowed in these arrangements, but inevitable. The density is deﬁned similarly to sphere packing (that is, the total volume of the spheres divided by the volume covered), but now we are interested in ﬁnding an arrangement of minimal density. In two dimensions, as for circle packing, the optimal circle covering is given by the regular hexagonal arrangement. However, the thinnest sphere covering in dimension 3 is given not by the FCC lattice, but by the body-centered cubic (BCC) lattice. In this arrangement, every sphere intersects with fourteen neighboring spheres; see for example [14].

In this paper we study a problem that falls between ellipsoid packing and covering. Given a set of ellipsoids of diverse size and shape, and a ﬁnite enclosing ellipsoid, we

∗Version of November 27, 2024. Research supported by NSF Grants DMS-0914524 and DMS-

0906818, and DOE Grant DE-SC0002283. †IST Austria, Am Campus 1, 3400 Klosterneuburg, Austria. caroline.uhler@ist.ac.at ‡Computer Sciences Department, 1210 W. Dayton Street, University of Wisconsin, Madison, WI

53706, USA. swright@cs.wisc.edu

seek an arrangement that minimizes some measure of total overlap between ellipsoid pairs.

Our formulation is motivated by chromosome organization in human cell nuclei. In biological sciences, the study of chromosome arrangements and their functional implications is an area of great current interest. The territory occupied by each chromosome can be modeled as an ellipsoid, diﬀerent chromosomes giving rise to ellipsoids of diﬀerent size. The enclosing ellipsoid represents a cell nucleus, the size and shape of which diﬀers across cell types. Overlap between chromosome territories has biological signiﬁcance: It allows for interaction and co-regulation of diﬀerent genes. Also of key signiﬁcance are the DNA-free interchromatin channels that allow access by regulatory factors to chromosomes deep inside a cell nucleus. Smaller nuclei tend to have tighter packings, so that fewer channels are available, and the chromosomes packed closest to the center may not be accessible to regulatory factors.

The arrangement of chromosome territories is neither completely random nor deterministic. Certain features of the arrangement are believed to be conserved during evolution [15], but can change during such processes as cell diﬀerentiation and cancer development [11]. In general, smaller and more gene-dense chromosomes are believed to be found closer to the center of the nucleus [1], and heterologous chromosomes tend to be nearer to each other than homologous pairs [9]. For further background on chromosome arrangement properties, see [5, 18].

A major goal of this paper is to determine whether the experimental observations made to date about chromosome organization can be explained in terms of simple geometrical principles, such as minimal overlap. The minimum-overlap principle appears to be consistent with the tendency of chromosome territories to exploit the whole volume of the nucleus, to make the DNA-free channels as extensive as possible. Our formulation also includes features to discourage close proximity of homologous pairs.

The remainder of the paper is organized as follows. In Section 2, we outline the mathematical formulation, deﬁne notation, and state a key technical result concerning algebraic formulations of ellipsoidal containment. In Section 3, we study the special case of ﬁnding a minimal overlap conﬁguration of spheres inside an ellipsoidal container. We describe a simple iterative procedure based on convex linearized approximations that produces convergence to stationary points of the minimal-overlap problem. We show through simulations that our algorithm can be used to recover known optimal circle and sphere packings. In Section 4, we generalize our optimization procedure to ellipsoid packing, introducing trust-region stabilization and proving convergence results. Section 5 describes the application of our algorithms to chromosome arrangement.

Notation. When A and B are two symmetric matrices, the relation A B indicates that B−A is positive semideﬁnite, while A ≺ B denotes positive deﬁniteness of B − A. Similar deﬁnitions apply for and .

Let X be a ﬁnite-dimensional vector space over the reals IR endowed with inner product  ·,· . (The usual Euclidean space IRn with inner product x,y := xTy and the space of symmetric matrices SIRn×n with inner product X,Y := trace(XY ) are two examples of particular interest in this paper.) Given a closed convex subset Ω ⊂ X, the normal cone to Ω at a point x is deﬁned as

NΩ(x) := {v ∈ X | v,y − x ≤ 0 for all y ∈ Ω}. (1.1) We use ∂f to denote the Clarke subdiﬀerential of the function f : X → IR. In deﬁning this quantity, we follow Borwein and Lewis [2, p. 124] by assuming Lipschitz

continuity of f at x, and deﬁning the Clarke directional derivative as follows:

f(y + th) − f(y) t

f◦(x;h) := limsup y→x,t↓0

.

The Clarke subdiﬀerential is then ∂f(x) := {v ∈ X | v,h ≤ f◦(x;h), for all h ∈ X}. (1.2)

When f is convex (in addition to Lipschitz continuous), this deﬁnition coincides with the usual subdiﬀerential from convex analysis, which is

∂f(x) := {v ∈ X | f(y) ≥ f(x) + v,y − x for all y ∈ dom f} (see [4, Proposition 2.2.7]).

2. Problem Description and Preliminaries. An ellipsoid E ⊂ IRn can be speciﬁed in terms of its center c ∈ IRn and a symmetric positive deﬁnite eccentricity matrix S ∈ SIRn×n. We can write

E := {x ∈ IRn | (x − c)TS−2(x − c) ≤ 1} = {c + Su | u 2 ≤ 1}. (2.1)

It is often convenient to work with the quantity Σ := S2 (also symmetric positive deﬁnite), and thus to rewrite the deﬁnition (2.1) as

E := {x ∈ IRn | (x − c)TΣ−1(x − c) ≤ 1}. (2.2)

For the remainder of this section, we assume that n = 3, that is, the ellipsoids are three-dimensional. The eigenvalues of S are the lengths of the principal semi-axes of E; we denote these by r1, r2, and r3, and assume that these three positive quantities are arranged in nonincreasing order. It follows that the eigenvalues of Σ are r12, r22, and r32, and that the matrices S and Σ have the form

 QT,

 QT, Σ = Q

 

 

r12 0 0 0 r22 0 0 0 r32

r1 0 0 0 r2 0 0 0 r3

S = Q

for some orthogonal matrix Q, which determines the orientation of the ellipse.

In this paper, we are given the semi-axis lengths ri1, ri2, and ri3 for a collection of N ellipsoids Ei, i = 1,2,...,N. The goal is to specify centers ci and matrices Si for these ellipsoids, such that

- (a) Ei ⊂ E, for some ﬁxed ellipsoidal container E;
- (b) The eigenvalues of Si are ri1, ri2, and ri3, for i = 1,2,...,N;
- (c) Some measure of volumes of the pairwise overlaps Ei ∩ Ej, i,j = 1,2,...,N, i = j, is minimized.


In the following subsections, we give more speciﬁc formulations of (c), ﬁrst for the case in which all Ei are spheres (that is, ri1 = ri2 = ri3, i = 1,2,...,N) and then for the general case. For now, we note that a crucial element in formulating these problems is ellipsoidal containment, that is, algebraic conditions that ensure that one given ellipsoid is contained in another. This is the subject of the following lemma, which is a simple application of the S-procedure (see [3, Appendix B.2]).

Lemma 2.1. Deﬁne two ellipsoids as follows:

E = {x ∈ IR3 | (x − c)TS−2(x − c) ≤ 1} = {c + Su | u 2 ≤ 1}, E¯ = {x ∈ IR3 | (x − c¯)TS¯−2(x − c¯) ≤ 1} = {c¯+ Su¯ | u 2 ≤ 1}.

The containment condition E¯ ⊂ E can be represented as the following linear matrix inequality (LMI) in parameters c¯, S¯, c, and S2: There exists λ ∈ IR such that

 

  0. (2.3)

−λI 0 S¯ 0 λ − 1 (¯c − c)T S¯ c¯− c −S2

Proof. The condition E¯ ⊂ E can be expressed as

(¯c + Su¯ − c)TS−2(¯c + Su¯ − c) ≤ 1 for all u such that u 2 ≤ 1. By multiplying out this inequality we get

uTSS¯ −2Su¯ + 2uTSS¯ −2(¯c − c) + (¯c − c)TS−2(¯c − c) − 1 ≤ 0

for all u such that uTu − 1 ≤ 0. By applying the S-procedure, we ﬁnd that this is equivalent to the existence of λ > 0 such that

SS ¯ −2S¯ SS¯ −2(¯c − c) (¯c − c)TS−2S¯ (¯c − c)TS−2(¯c − c) − 1

I 0 0 −1

λ

. (2.4)

This expression is not linear in the variables c¯, S¯, c, and S2, but an elementary Schur complement argument shows equivalence to the linear matrix inequality (2.3), completing the proof.

| |
|---|


As one special case, the condition Ei ⊂ E, where Ei is a sphere with center ci and radius ri and E is an ellipsoid centered at 0 with matrix S, can be represented as the LMI:

 

  0. (2.5)

−λiI 0 riI

0 λi − 1 cTi riI ci −S2

The more general case of Ei ⊂ E, where Ei is an ellipsoid with center ci and matrix Si and E is an ellipsoid centered at 0 with matrix S, can be represented as the LMI:

 

  0. (2.6)

−λiI 0 Si

0 λi − 1 cTi Si ci −S2

3. Sphere Packing. We give a problem formulation for the case in which all enclosed shapes are spheres (of arbitrary dimension), and present a successive approximation algorithm that is shown to accumulate or converge to a stationary point of the formulation. Some examples of results obtained with this approach are described at the end of the section.

3.1. Formulation and Algorithm. When the inscribed objects are spheres, the variables in the problem are the centers ci ∈ Rm, i = 1,2,...,N, which we aggregate as follows:

c := (c1,c2,...,cN). (3.1)

The radii ri, i = 1,2,...,N are given. We express the containment condition for each sphere as follows:

Ei ⊂ E ⇔ ci ∈ Ωi, (3.2)

where Ωi is a closed, bounded, convex set with nonempty interior. When E is a sphere of radius R centered at 0, we have Ωi := {ci : ci ≤ R − ri}. Otherwise, we can deﬁne Ωi implicitly by Lemma 2.1; see in particular (2.5).

A simple measure for the overlap between two spheres Ei and Ej is the diameter of the largest sphere inscribed into the intersection, which we denote by an auxiliary variable ξij:

ξij := max(0,(ri + rj) − ci − cj 2), ξ := (ξij)1≤i<j≤N. (3.3) Our minimum-overlap problem can thus be formulated as follows:

min

c,ξ

H(ξ) (3.4a)

subject to (ri + rj) − ci − cj 2 ≤ ξij for 1 ≤ i < j ≤ N (3.4b) 0 ≤ ξ, (3.4c) ci ∈ Ωi, for i = 1,...,N, (3.4d)

where (3.4c) denotes the entrywise condition ξij ≥ 0, 1 ≤ i < j ≤ N. The objective H : IR+n(n−1)/2 → IR+ satisﬁes the following assumption.

Assumption 1. The function H : IRn+(n−1)/2 → IR+ is convex and continuous, with the following additional properties:

- (a) H(0) = 0;
- (b) H(ξ) > 0 whenever ξ = 0;
- (c) 0 ≤ ξ¯≤ ξ ⇒ H(ξ¯) ≤ H(ξ). Assumption 1 is satisﬁed, for example, by the norms H(ξ) = ξ 1, H(ξ) = ξ 2,


and H(ξ) = ξ ∞ = max1≤i<j≤N |ξij|. In the application to be discussed below, we prefer the overlaps in the overlapping ellipsoids to be roughly the same size; for this purpose, the 2 and ∞ norms are the most appropriate.

Although the objective (3.4a) and containment constraints (3.4d) are convex, the problem (3.4) is nonconvex, due to the constraints (3.4b). A point is Clarke-stationary for (3.4) if the following conditions are satisﬁed, for some λij ∈ IR, 1 ≤ i < j ≤ N:

0 ≤ gij − λij ⊥ ξij ≥ 0 for some gij ∈ ∂ξ

H(ξ), 1 ≤ i < j ≤ N, (3.5a)

ij

- i−1
- j=1


N

λjiwji ∈ NΩ

λijwij −

(ci), i = 1,2,...,N, (3.5b)

i

j=i+1

0 ≤ ξij + ci − cj − (ri + rj) ⊥ λij ≥ 0, 1 ≤ i < j ≤ N, (3.5c) where wij 2 ≤ 1, with wij =

ci − cj ci − cj 2

when ci = cj, 1 ≤ i < j ≤ N. (3.5d)

Condition (3.5d) deﬁnes wij to be in the subdiﬀerential of ci − cj 2 with respect to ci. See (1.1) for the deﬁnition of the normal cone in (3.5b).

We now develop an algorithm that seeks a local solution of (3.4), by formulating a sequence of convex approximations in which the key feature is linearization of the nonconvex constraint (3.4b) around the current iterate. Because of the special properties of this problem, we need not apply the usual safeguards for this successive approximation approach, such as trust regions or line searches. Decrease of the objective at each iteration and accumulation of the iteration sequence at ﬁrst-order points of the problem (3.4) can be proved in the absence of these features. However, for purposes of stabilizing the iterates generated by the method, it may be desirable to place

a uniform bound on the length of each step. This can be done without complicating the analysis, and we do so in our implementations.

The linearization of (3.4) around the current iterate c− is deﬁned as follows: P(c−) := min

H(ξ¯) (3.6a)

c,ξ¯

subject to (ri + rj) − zijT (ci − cj) ≤ ξ¯ij, for 1 ≤ i < j ≤ N, (3.6b) 0 ≤ ξ,¯ (3.6c) ci ∈ Ωi, for i = 1,...,N, (3.6d)

(c−i − c−j )T/ c−i − c−j when c−i = c−j 0 otherwise.

where zij :=

(3.6e)

This problem is convex, with aﬃne constraints except for the inclusion (3.6d), which can be satisﬁed strictly when each Ωi is closed, bounded, and convex, with nonempty interior. Hence (see for example [13, Theorem 28.2, Corollary 28.3.1]), its solutions are characterized by the following KKT conditions: There exist λij, 1 ≤ i < j ≤ N such that

0 ≤ gij − λij ⊥ ξ¯ij ≥ 0 for some gij ∈ ∂ξ¯ijH(ξ¯), 1 ≤ i < j ≤ N, (3.7a)

- i−1
- j=1


N

λijzij −

λjizji ∈ NΩ

(ci), i = 1,2,...,N, (3.7b)

i

j=i+1

0 ≤ ξ¯ij + zijT (ci − cj) − (ri + rj) ⊥ λij ≥ 0, 1 ≤ i < j ≤ N. (3.7c)

We can use a compactness argument to verify that solutions to (3.6) are attained. The vector of feasible centers c is restricted to a compact set, by the assumed properties of Ω1,Ω2,...,ΩN. By using (3.6b) we can deﬁne eﬀective upper bounds on the variables ξ¯ij as follows:

ξ¯ ij := max 0, sup

(ri + rj) − zijT (ci − cj) .

ci∈Ωi, cj∈Ωj

(For any feasible c, and given any ξ¯ satisfying (3.6b), we can always replace ξ¯ by an alternative feasible point ξ¯ ∈ [0,ξ¯ ] without increasing the value of H, by property (b) of Assumption 1.) Thus, the problem (3.6) reduces to minimization of a continuous convex function over a compact set, for which existence of a solution is guaranteed.

Algorithm 1 Packing Spheres by Minimizing Overlap Given ri, i = 1,2,...,N and Ωi closed, convex, bounded with nonempty interior; Choose c0 ∈ Ω1 × Ω2 × ··· × ΩN; for k = 0,1,2,... do

Solve P(ck) deﬁned by (3.6) to obtain (ck+1,ξ¯k+1); if H(ξ¯k+1) = H(ξk) then

stop and return ck; end if Set ξijk+1 = max(0,(ri + rj) − cki+1 − ckj+1 ) for 1 ≤ i < j ≤ N;

## end for

Algorithm 1 is the simple algorithm based on the subproblem (3.6). To analyze convergence properties of this method, we start with basic results about stationary points and about the changes in H at each iteration of Algorithm 1.

Lemma 3.1. Suppose that the sets Ωi in (3.4) are closed, bounded, and convex, with a nonempty interior, and that Assumption 1 holds. Then the following claims are true.

- (i) If the point (ck,ξk) satisﬁes the optimality conditions (3.7) for the subproblem P(ck) deﬁned by (3.6), then (ck,ξk) satisﬁes the stationarity conditions (3.5) for the problem (3.4).
- (ii) If the point (ck,ξk) satisﬁes the stationarity conditions (3.5) for the problem

(3.4) and in addition cki = ckj for all 1 ≤ i < j ≤ N, then (ck,ξk) satisﬁes the optimality conditions (3.7) for the subproblem P(ck) deﬁned by (3.6).

- (iii) If (ck,ξk) does not satisfy the stationarity conditions (3.5), then H(ξ¯k+1) < H(ξk).
- (iv) For each k we have H(ξk) ≤ H(ξ¯k). Proof.


- (i) If (ck,ξk) satisﬁes the optimality conditions (3.7) for P(ck), then by setting wij = zij in (3.5), we see that these conditions are also satisﬁed with the same values of gij and λij. (We have made the particular choice wij = 0 when cki = ckj.)
- (ii) If the conditions (3.5) are satisﬁed at (ck,ξk) with cki = ckj for all i, j with

1 ≤ i < j ≤ N, then wij = (cki − ckj)/ cki − ckj for all such i, j. Thus by noting that zij = wij for all such i, j, we can verify using the same values of gij and λij that (ck,ξk) satisﬁes the optimality conditions (3.7), and therefore is a solution of P(ck).

- (iii) Note that the point (ck,ξk) is feasible for the subproblem (3.6) (with c− = ck), so its optimal objective satisﬁes H(ξ¯k+1) ≤ H(ξk). Since (ck,ξk) does not satisfy the stationarity conditions (3.5), however, part (i) implies that it cannot be a solution of (3.6), which implies that in fact H(ξ¯k+1) < H(ξk), as claimed.
- (iv) By using the fact that zijk−1 2 ≤ 1, we have for all k ≥ 1 and all i, j with 1 ≤ i < j ≤ N that


ξijk = max(ri + rj −  cki − ckj 2,0) ≤ max(ri + rj − (zijk−1)T(cki − ckj),0) ≤ ξ¯ijk . The result now follows immediately from Assumption 1(c).

| |
|---|


Note that in the case of coinciding centers, i.e. ci = cj for some i = j, the stationarity conditions for (3.4) and (3.6) are not equivalent. This observation yields the intriguing property — unusual in algorithms based on linear approximations that Algorithm 1 may be able to move away from a stationarity point for (3.4). That is, if (ck,ξk) satisﬁes (3.5) but there is some pair (i,j) with i = j and cki = ckj, then by setting zij = 0, the subproblem (3.7) may yield a solution (ck+1,ξ¯k+1) with H(ξ¯k+1) < H(ξk), and thus (by Lemma 3.1 (iv)) the next iterate will satisfy H(ξk+1) < H(ξk). Note too that the proof of Lemma 3.1 (iv) still holds if zijk is chosen to be any vector with zijk 2 ≤ 1 when cki = ckj. Hence, random choices for zijk in this situation could be used in place of our choice zijk = 0 above, leading to some interesting algorithmic possibilities for avoiding coincident centers and moving away from stationary points. Since coincident centers rarely arise in the cases of interest, however, we do not pursue these possibilities.

- 0.8

- 1


- 0.8

- 1


- 0.8

- 1


0.6

0.6

0.6

2

2

4

2

5

0.4

0.4

0.4

0.2

0.2

0.2

- 3

- 4


0

3

0

0

1

4

1

5

−0.2

−0.2

−0.2

5

−0.4

−0.4

−0.4

3

1

−0.6

−0.6

−0.6

−0.8

−0.8

−0.8

−1

−1

−1

−1 −0.5 0 0.5 1

−1 −0.5 0 0.5 1

−1 −0.5 0 0.5 1

(a) Global Solution: o =

(b) Local Solution: o = .5

(c) Local Solution: o = .5

.4122147478

Fig. 3.1. Solutions obtained by Algorithm 1 for packing circles of radius .5 into a circle of radius 1, showing ﬁnal overlap measures for each.

We now prove the main convergence result for Algorithm 1.

Theorem 3.2. Suppose that the sets Ωi in (3.4) are closed, bounded, and convex, with a nonempty interior, and that Assumption 1 holds. Then Algorithm 1 either terminates at a stationary point for (3.4), or else generates an inﬁnite sequence {ck} for which all accumulation points cˆ are either stationary points for (3.4), or else have cˆi = cˆj for some pair (i,j) with 1 ≤ i < j ≤ N.

Proof. Lemma 3.1 (iii) says that termination can occur only if (ck,ξk) satisﬁes the stationarity conditions (3.5). Hence, we need to consider only the case of an inﬁnite sequence of iterates {ck}. Suppose for contradiction that there is an accumulation point cˆ for this sequence such that cˆi = cˆj for all (i,j) but cˆ is not stationary for

- (3.4). Considering the problem P(ˆc) deﬁned by (3.6), we have by Lemma 3.1 (iii)


that := H(ξˆ) − H(ξ¯) > 0 (strict inequality), where ξˆij = max(0,ri + rj −  cˆi − cˆj ). Moreover, we can identify a neighborhood N of c¯ such that for all ck ∈ N, we have

H(ξk+1) ≤ H(ξ¯k+1) < H(ξk) −  /2, (3.8)

This claim follows from Lemma 3.1 (iv) and the observation that the optimal objective in (3.6) is a continuous function of c−, for c− near cˆ. The face that cˆi = cˆj for all (i,j) ensures that the zij are continuous functions of c−, while H itself is continuous by Assumption 1. Since there is a subsequence S with limk∈S ck = cˆ, we have from (3.8) and monotonicity of the full sequence {H(ξk)} that H(ξk) ↓ −∞. This is impossible, however, since H is bounded below by 0. We conclude therefore that all accumulation points cˆ are either stationary or else have cˆi = cˆj for some pair (i,j), as required.

| |
|---|


As noted above, the case in which accumulation points have coincident centers is exceptional, so Theorem 3.2 shows that the algorithm usually either terminates or accumulates at stationary points.

3.2. Examples. We present several examples showing results obtained with Algorithm 1 on various problems, and compare them with known results. To begin, a simple example to demonstrate the existence of local minima that are not global minima.

Example 3.1 (Five Circles). Consider the problem of packing ﬁve circles of radius .5 into an enclosing circle of radius 1. Results obtained with Algorithm 1, with objective H(ξ) = ξ ∞, from random starting points reveal an apparent global solution (Figure 3.1(a)) and a family of local solutions (Figures 3.1(b) and 3.1(c)).

![image 1](<2012-uhler-packing-ellipsoids-overlap_images/imageFile1.png>)

![image 2](<2012-uhler-packing-ellipsoids-overlap_images/imageFile2.png>)

Fig. 3.2. Circle packing in a circular enclosure. A nearly hexagonal arrangement is seen in the interior.

The local solutions are characterized by one of the packed circles having its center at the center of the enclosing circle; this circle thus has an overlap of .5 with all four of the outer circles. The outer circles in this local solution need only be arranged so that their maximum pairwise overlap is no greater than .5. Algorithm 1 required only a few iterations for each of these examples.

Student Version of MATLAB

As noted in Section 1 optimal sphere packings (conﬁgurations with no overlap) have been obtained in two and three dimensions, for spaces of inﬁnite extent. Our algorithm can only solve problems with ﬁnite enclosing shapes, but we can use large enclosures to investigate how similar the local solutions attained by our algorithm are to the known optimal packings in IR2 (hexagonal lattice with density π/√12) and IR3 (FCC lattice with density π/√18).

Example 3.2 (Uniform Circles in IR2). We ran Algorithm 1 with N = 150 circles, each of area π, and a circular container of size 150√12. This results in a total circle area-to-container area ratio which is equal to the optimal packing density. The resulting circle conﬁguration is shown in Figure 3.2. The hexagonal arrangement of the circles is clearly visible in the interior of the container.

We also ran tests in which 100 circles are packed into a square container. (Rectangular feasible sets Ωi are easily incorporated into the formulation by deﬁning bound constraints on the centers ci.) We generate starting points by arranging the centers in a 10 × 10 square lattice. We may then add a random perturbation to each center. Results are shown in Figure 3.3. (For clarity, we show only the centers in this ﬁgure, omitting the circles.) When no perturbations are added to the starting conﬁguration, the algorithm does not move from the initial square conﬁguration shown in

#### (a) o = .1192514295

#### (b) o = .1188906843

#### (c) o = .1181440939

(d) o = .1179656050

Fig. 3.3. Local minima obtained by Algorithm 1 for packing circles into a square, showing ﬁnal overlap measures for each.

9

Student Version of MATLAB

Student Version of MATLAB

Student Version of MATLAB

Student Version of MATLAB

Figure 3.3(a). When random initial perturbations are applied (large enough that the original square grid structure is not recognizable in the initial point), many diﬀerent local minima are obtained. Three of these are shown in Figures 3.3(b), 3.3(c), and

- 3.3(d). Note that all of these have a maximum overlap less than the square conﬁguration, and that hexagonal structure is recognizable in large parts of the domain, with square structure and disorder in intermediate regions.

Example 3.3 (Uniform spheres in IR3). We performed a similar test to Example 3.2 in three dimensions. We checked to see whether Algorithm 1 converges to a solution like the FCC lattice in a ﬁnite minimum-overlap arrangement with 200 spheres enclosed in a larger sphere. We chose the small spheres to have volume π and the containing sphere to have volume 200√18, giving a density of π/√18, identical to the FCC lattice, which is optimal in inﬁnite space. At the solution obtained by Algorithm 1, we counted the number of spheres that touch or intersect each sphere. This statistic provides an indication of the type of packing attained, since the FCC lattice has 12 neighbors per sphere, while the BCC lattice has only 8 neighbors per sphere. The histogram for the number of neighboring spheres is shown in Figure 3.4(a). A more instructive diagram is obtained by removing from consideration those spheres that touch the enclosing sphere. After doing so, we obtain the histogram in Figure

- 3.4(b). This ﬁgure suggests strongly that the calculated solution is close to the FCC lattice over most of the interior region of the domain.


Finally, we report on solutions obtained by Algorithm 1 on packings of discs in a circle, for which the optimal packing is known in only a few cases. In particular, we analyze packings with equally sized discs, where the number of discs is given by a hexagonal number, that is,

h(k) = 3k(k + 1) + 1, k ≥ 1. (3.9)

Example 3.4. Lubachevsky and Graham [10] introduce curved hexagonal packings, a new family of packings for conﬁgurations with a hexagonal number of discs. This family contains the best packings found so far for h(k) deﬁned by (3.9), for k ≤ 5. We ran Algorithm 1 with the optimal densities found in [10] for k = 3,4,5. The best local optima we found are shown in Figure 3.5; they are identical to the conﬁgurations found in [10]. (We highlight some of the circles to emphasize the “curved” feature of the packing, which distinguishes it from a standard hexagonal arrangement, which has slightly lower density when restricted to a ﬁnite circle.)

##### Histogram of neighbors

##### Histogram of lattice

01020304050

01020304050

Frequency

Frequency

6 8 10 12 14

6 8 10 12 14

Number of neighbors

Number of neighbors

(a) Distribution of neighbor counts.

(b) Distribution of neighbor counts, after spheres at the periphery have been removed.

Fig. 3.4. Neighbor counts for packing of 100 three-dimensional spheres in in a spherical container.

![image 3](<2012-uhler-packing-ellipsoids-overlap_images/imageFile3.png>)

![image 4](<2012-uhler-packing-ellipsoids-overlap_images/imageFile4.png>)

#### (a) 37 discs

![image 5](<2012-uhler-packing-ellipsoids-overlap_images/imageFile5.png>)

![image 6](<2012-uhler-packing-ellipsoids-overlap_images/imageFile6.png>)

#### (b) 61 discs

![image 7](<2012-uhler-packing-ellipsoids-overlap_images/imageFile7.png>)

![image 8](<2012-uhler-packing-ellipsoids-overlap_images/imageFile8.png>)

![image 9](<2012-uhler-packing-ellipsoids-overlap_images/imageFile9.png>)

![image 10](<2012-uhler-packing-ellipsoids-overlap_images/imageFile10.png>)

#### (c) 91 discs

(d) 37 discs, larger radii

Fig. 3.5. Optimal conﬁgurations found using Algorithm 1 for hexagonal numbers of unit discs in an enclosing circle.

Student Version of MATLAB

Student Version of MATLAB

Student Version of MATLAB

Student Version of MATLAB

When we ran Algorithm 1 on the problem of 37 uniform discs in a larger disc, where the radii were too large to allow packing without overlap, the algorithm with H(ξ) = ξ ∞ produced the same arrangement of centers as in Figure 3.5(a) (see Figure 3.5(d)) when initialized at a suﬃciently close initial point. It is a well known property of minimization of the norm · ∞ that many elements of the argument vector tend to achieve the maximum value. In our application, this means that the maximal overlap is attained by many pairs of circles. We can obtain non-overlapping conﬁgurations by simply reducing the radii of all discs uniformly, by an amount equal to half the maximal overlap. This will yield a solution in which each pair of circles that formerly overlapped maximally now just touches.

4. Ellipsoid Packing. Here we discuss a bilevel optimization procedure for packing ellipsoids into an ellipsoidal container in a way that minimizes the maximum overlap of any pair of ellipsoids. It is not as obvious how to measure the overlap between two ellipsoids as between two spheres, since it depends on the orientation of the ellipsoids as well as the location of their centers. We measure the overlap by the sum of principal semi-axes of the largest ellipsoid that can be inscribed in the intersection of the two ellipsoids. This overlap measure can be calculated by solving a small semideﬁnite optimization problem, constructed according to the S-procedure (see Subsection 4.1). These are the lower-level problems in our bilevel optimization formulation. The upper-level problem is to position and orient the ellipsoids so as to minimize the maximum overlap (see Subsection 4.2), while keeping all ellipsoids inside the enclosing shape. We refer to this problem as “min-max-overlap.” Dual information from the lower-level problems provides a measure of sensitivity of the overlaps to the ellipsoid parameters, allowing us to develop a successive approximation approach, with trust regions, whose accumulation points are stationary for the min-max-overlap problem. Technical results regarding the trust-region approach and the proof of convergence are given in Subsection 4.3.

4.1. Measuring Overlap. Boyd and Vandenberghe [3, Section 8.4.2] consider the problem of ﬁnding the ellipsoid of largest volume inscribed in an intersection of ellipsoids. The volume of an ellipsoid E = {c + Su | u 2 ≤ 1} is proportional to det(S). Although this problem is convex, it is not a semideﬁnite program (SDP), because the objective is nonlinear. We thus consider an alternative in which trace(S) is used as the objective. The trace is the sum of lengths of the semi-axes of the ellipsoid, which is a good proxy for the volume in problems of the type we consider. Trace maximization admits an SDP formulation of the lower-level problems, which

facilitates theoretical development and analysis of our min-max-overlap problem. Recalling from (2.1) that we deﬁne the ellipsoid Ei by

Ei := {ci + Siu | u 2 ≤ 1}, (4.1)

we introduce the notation Σi = Si2. Parametrizing the inscribed ellipsoid similarly by Eij := {cij +Siju | u 2 ≤ 1}, and using (2.3) to formulate the fact that the inscribed ellipsoid is contained in both Ei and Ej, we formulate the problem of measuring overlap as follows:

Oˆ(ci,cj,Σi,Σj) := max

trace(Sij)

Sij 0,cij,λij1,λij2

 

  0, (4.2a)

−λij1I 0 Sij

0 λij1 − 1 (cij − ci)T Sij cij − ci −Σi

subject to

 

  0. (4.2b)

−λij2I 0 Sij

0 λij2 − 1 (cij − cj)T Sij cij − cj −Σj

The Lagrangian can be written as L(c,Sij,λij1,λij2,Tij,Mij1,Mij2) := I,Sij + Tij,Sij

- − Mij1,

 

−λij1I 0 Sij

0 λij1 − 1 (cij − ci)T Sij cij − ci −Σi

 

- − Mij2,


with the dual problem being derived from

 

  ,

−λij2I 0 Sij

0 λij2 − 1 (cij − cj)T Sij cij − cj −Σj

min

Mij1 0,Mij2 0,Tij 0

L(cij,Sij,λij1,λij2,Tij,Mij1,Mij2) .

max

Sij 0,cij,λij1,λij2

Introducing the following notation for Mij1 and Mij2:

 

 , Mij2 :=

 

 , (4.3)

Rij1 rij1 Pij1 rijT1 pij1 qijT1 Pij1 qij1 Qij1

Rij2 rij2 Pij2 rijT2 pij2 qijT2 Pij2 qij2 Qij2

Mij1 :=

we can write the dual explicitly as follows: Oˆ(ci,cj,Σi,Σj) := min

pij1 + pij2 + 2qijT1ci + 2qijT2cj + Qij1,Σi + Qij2,Σj

Mij1 0,Mij2 0,Tij 0

subject to 0 = I + Tij − 2Pij1 − 2Pij2 (4.4)

- 0 = trace(Rij1) − pij1
- 0 = trace(Rij2) − pij2 0 = qij1 + qij2.


(We have assumed without loss of generality that Pij1 and Pij2 are in SIRn×n; this follows from Sij ∈ SIRn×n.)

When the ellipsoids Ei and Ej overlap, strong duality holds for this primal-dual pair of semideﬁnite programs since, as we now verify, both problems have a strictly feasible point. For (4.2) we know that there exists an ellipsoid with positive volume that is strictly inscribed in the intersection. By setting cij and Sij to be the parameters of this ellipsoid (with Sij 0), the S-procedure for strict inequalities can be applied to show that (strict) deﬁniteness holds in (4.2a) and (4.2b). This fact establishes strict feasibility of (4.2). For the dual (4.4), we can set Tij = I and deﬁne

 .

 

I 0 21I

- 0 n 0
- 1

- 2I 0 I


Mij1 = Mij2 =

It is easy to verify that these choices satisfy the constraints in (4.4), along with the (strict) interiority conditions Mij1 0, Mij2 0, Tij 0. This observation of strong duality justiﬁes our use of the notation Oˆ(ci,cj,Σi,Σj) to denote the optimal objectives of both primal and dual.

4.2. Choosing Ellipse Positions and Orientations. The main variables in the min-max-overlap problem are the parameters deﬁning the ellipses Ei for i = 1,2,...,N: the centers ci and the orientations deﬁned by Si (and thus Σi = Si2). For n = 3 (which we assume in this section and subsequently), we would like to ﬁx the lengths of the axes of each ellipsoid at the values ri1, ri2, and ri3 (assuming that ri1 ≥ ri2 ≥ ri3). This is equivalent to ﬁxing the eigenvalues of Σi at ri21, ri22, and ri23, or to ﬁxing the eigenvalues of Si to ri1, ri2, and ri3.

Using the notation Oˆ deﬁned in (4.2) and (4.4), we can formulate the min-maxoverlap problem as the following bilevel optimization problem:

min

ξ (4.5a)

ξ,(ci,Si,Σi),i=1,2,...,N

subject to ξ ≥ Oˆ(ci,cj,Σi,Σj), 1 ≤ i < j ≤ N, (4.5b) Ei ⊂ E, i = 1,2,...,N, (4.5c) Σi = Si2, (4.5d) semi-axes of Ei have lengths ri1,ri2,ri3, i = 1,2,...,N. (4.5e)

This problem is nonconvex for three reasons. First, each pairwise overlap objective

- Oˆ(ci,cj,Σi,Σj) is a nonconvex function of its arguments. This issue is intrinsic; as in the sphere-packing problem, we expect there to be many local solutions and we can only expect our algorithm to ﬁnd one of them. As we see below (in (4.10) and Algorithm 4.4), our algorithm iteratively solves subproblems in which each Oˆ is replaced by a linearized approximation that makes use of the optimal dual variables


Mij1 and Mij2 from the formulation (4.4). These subproblems will be convex if we can overcome the other two sources of nonconvexity in the formulation (4.5), which we address now.

The second nonconvexity issue is in the constraint (4.5e) on the eigenvalues of Si, i = 1,2,...,N. We consider instead the following convex relaxation:

Si − ri1I 0, Si − ri3I 0, trace(Si) = ri1 + ri2 + ri3. (4.6)

Note that this is indeed a relaxation: If Ei has the desired dimensions, then the eigenvalues of Si are ri1, ri2, and ri3, and the conditions (4.6) are satisﬁed. Because the

overall goal is to minimize maximal overlap, and because minimum-volume ellipsoids are those that are most eccentric, the relaxation (4.6) is usually “tight” with respect to (4.5) in many interesting cases. Intermediate iterates are often observed to have ellipsoids less eccentric than desired.

The third source of nonconvexity — the constraint (4.5d) — is relatively easy to deal with. We replace it with the following pair of restrictions:

Σi Si Si I

0, Si 0, i = 1,2,...,N. (4.7)

The ﬁrst of these conditions ensures only that Σi Si2. However, the overlap

- Oˆ(ci,cj,Σi,Σj) will grow if Σi is replaced by any matrix Σ˜i Σi. Hence, because of the min-max-overlap objective in (4.5), the matrices Σi will be set to the “smallest possible values” that satisfy the conditions (4.7), that is, Σi = Si2.


Finally, deﬁning the containing ellipse to be E := {x | (x − c)TΣ−1(x − c) ≤ 1}, we can use (2.3) to formulate the condition (4.5c) as follows:

 

  0, (4.8)

−λiI 0 Si

0 λi − 1 (ci − c)T Si ci − c −Σ

Given all these considerations, we deﬁne the relaxed version of (4.5) to be addressed in this section as follows:

min

ξ (4.9a)

ξ,(λi,ci,SiΣi),i=1,2,...,N

subject to ξ ≥ Oˆ(ci,cj,Σi,Σj), 1 ≤ i < j ≤ N, (4.9b)

 

  0, i = 1,2,...,N, (4.9c)

−λiI 0 Si

0 λi − 1 (ci − c)T Si ci − c −Σ

Σi Si Si I

0, i = 1,2,...,N, (4.9d)

Si − ri1I 0, Si − ri3I 0, i = 1,2,...,N, (4.9e) trace(Si) = ri1 + ri2 + ri3, i = 1,2,...,N. (4.9f)

Note that when the ellipse Ei is actually a circle, that is, ri1 = ri2 = ri3, we can ﬁx Si = ri1I and Σi = ri21I in (4.10), and eliminate these variables from that problem. Hence, we can assume without loss of generality that ri1 > ri3.

In the remainder of this subsection, we describe our algorithm for solving the bilevel optimization problem (4.9), and prove convergence properties. Our development and analysis takes place in a general setting that encompasses (4.9) but uses simpler notation. A key step in the algorithm is the solution of a subproblem for (4.9) in which the objective is linearized using the optimal values from the dual overlap formulation (4.4). The other constraints in (4.9) remain the same, and a trust region is added to restrict the amount by which the ellipsoid parameters can change. This

subproblem can be stated as follows:

min

ξ (4.10a)

ξ,(λi,ci,Si,Σi),i=1,2,...,N

subject to ξ ≥ pij1 + pij2 + 2qijT1ci + 2qijT2cj

+ Qij1,Σi + Qij2,Σj , for (i,j) ∈ I, (4.10b)

  0, i = 1,2,...,N, (4.10c)

 

−λiI 0 Si

0 λi − 1 (ci − c)T Si ci − c −Σ

Σi Si Si I

0, i = 1,2,...,N, (4.10d)

Si − ri1I 0, Si − ri3I 0, i = 1,2,...,N, (4.10e) trace(Si) = ri1 + ri2 + ri3, i = 1,2,...,N, (4.10f)

ci − c−i 22 ≤ ∆2c, i = 1,2,...,N, (4.10g) Si − Si− ≤ ∆S, i = 1,2,...,N, (4.10h)

|λi − λ−i | ≤ ∆λ, i = 1,2,...,N. (4.10i)

Here, (λ−i ,c−i ,Si−,Σ−i ) are the values of the variables at the current iteration, and ∆c, ∆S, and ∆λ are trust-region radii. The quantities pij1, pij2, qij1, qij2, Qij1, and Qij2 are extracted from the dual solutions Mij1 and Mij2 of (4.4) according to the structure

- (4.3). The set I represents a subset of all possible pairs (i,j) for 1 ≤ i < j ≤ N, representing some selection of ellipses which currently have a (strict) overlap. Further details on the choice of I are given in Subsection 4.4.


We claim ﬁrst that, if it is possible to ﬁt each ellipsoid Ei strictly inside the enclosing ellipsoid E, the subproblem (4.10) satisﬁes a Slater condition. That is, there exists a point that satisﬁes the linear equality constraints and strictly satisﬁes the inequality constraints in this problem. To justify this claim, we ﬁrst show that it is possible to ﬁnd a point (λ¯i,c¯i,S¯i,Σ¯i) that satisﬁes the following conditions:

 

  ≺ 0, i = 1,2,...,N, (4.11a)

−λ¯iI 0 S¯i

0 λ¯i − 1 (¯ci − c)T S¯i c¯i − c −Σ

Σ ¯i S¯i S¯i I

0, i = 1,2,...,N, (4.11b) S¯i − ri1I ≺ 0, S¯i − ri3I 0, i = 1,2,...,N, (4.11c)

trace(Si) = ri1 + ri2 + ri3, i = 1,2,...,N. (4.11d)

First, choosing c¯i = c in (4.11a), and orienting ellipsoid Ei appropriately, we can ﬁnd λ¯i > 0 such that (4.11a) is satisﬁed. This remains true if we perturb S¯i slightly so that its spectrum lies in the open interval (ri3,ri1) while still satisfying the trace condition (4.11d). This perturbed S¯i thus satisﬁes the conditions (4.11c). Second, we can simply deﬁne Σ¯i = σiI for large enough σi > 0 to ensure that (4.11b) is satisﬁed strictly.

Next, note that from the current iteration, we have a point (λ−i ,c−i ,Si−,Σ−i ) that

satisﬁes the constraints of (4.9), that is,

 

  0, i = 1,2,...,N, (4.12a)

−λ−i I 0 Si−

0 λ−i − 1 (c−i − c)T Si− c−i − c −Σ

Σ−i Si− Si− I

0, i = 1,2,...,N, (4.12b)

Si− − ri1I 0, Si− − ri3I 0, i = 1,2,...,N, (4.12c) trace(Si−) = ri1 + ri2 + ri3, i = 1,2,...,N. (4.12d)

It is now easy to check that for suﬃciently small > 0, the point

(λi( ),ci( ),Si( ),Σi( )) := (1 − )(λ−i ,c−i ,Si−,Σ−i ) + (λ¯i,c¯i,S¯i,Σ¯i)

satisﬁes the inequalities (4.10c), (4.10d), and (4.10e) strictly, satisﬁes the linear constraint (4.10f), and satisﬁes the trust-region constraints (4.10g), (4.10h), and (4.10i) strictly. Since we can choose ξ arbitrarily large to strictly satisfy (4.10b), we conclude that there exists a Slater point for (4.10).

4.3. Technical Results. We prove here some technical results that provide the basis for convergence of the trust-region strategy. To simplify the notation, we note that each dual overlap problem (4.4) has the general form

P(l,C) : t∗l (C) :=min

C,Ml (4.13a) s.t. Al,i,Ml = bl,i, i = 1,2,...,pl, Ml 0. (4.13b)

Ml

Here C captures the parameters that describe all the ellipses, and Ml is the dual variable for the overlap problem. We assume that C lies in a set Ω of the following form:

Ω := Ω¯ ∩ {C : Bk,C = bk, k = 1,2,...,p}, (4.14)

where Ω¯ is closed, convex, bounded, with nonempty interior. We now verify formally that the ellipse parameters satisfying the constraints in (4.9) can be expressed in the form (4.14). We deﬁne C to be a block-diagonal matrix with N blocks of the form:

Σi ci cTi 1

, i = 1,2,...,N, (4.15)

and deﬁne Ω¯ to be the set of all symmetric matrices of this form for which there exist λi and Si such that each tuple (λi,ci,Si,Σi) satisﬁes the conditions (4.9c), (4.9d), and (4.9e). Boundedness of ci is obvious from the containment condition Ei ⊂ E; boundedness of Si follows from (4.9e); while (4.9c) implies that λi ∈ [0,1]. Boundedness of Σi is not guaranteed by the constraints in (4.9). We could, however, add the constraint Σi ri21I without changing the solution of the problem, thus completing the veriﬁcation of boundedness of Ω.¯ (For simplicity, however, we do not put this explicit bound on Σi in our discussion below.) Closedness and convexity are immediate consequence of the form of the constraints (4.9c), (4.9d), and (4.9e). To verify nonemptiness of the interior of Ω,¯ recall the discussion following (4.9), where we noted that variable Si can be eliminated from the formulation if ellipsoid Ei is in

fact a circle. Thus, we can assume without loss of generality that ri1 > ri3 for all i, and hence, from the discussion surrounding (4.11), we conclude that the set of tuples (λi,ci,Si,Σi) allowed by constraints (4.9c), (4.9d), and (4.9e) has nonempty interior. The structural features of C (the diagonal element 1 in (4.15) and the oﬀ-diagonal zeros) can in principle be enforced by aﬃne constraints of the form given in (4.14). The constraints (4.9f) can also be enforced in this way.

Following the notation of (4.11), we denote by C¯ the point that satisﬁes

C¯ ∈ intΩ¯ and Bk,C¯ = bk, k = 1,2,...,p. (4.16) We denote by Ml(C) an optimal value of Ml in (4.13) (not necessarily unique).

The primal form (4.2) of the overlap problem (4.13) has the form

bTl ζl s.t. C −

max

ζl=(ζl,1,ζl,2,...,ζl,pl)

pl

ζl,iAl,i 0. (4.17)

i=1

As discussed in Subsection 4.1, both (4.13) and (4.17) have strictly feasible points when there is positive overlap between two ellipsoids. Therefore, strong duality holds, so the following optimality conditions relating the solutions of (4.13) and (4.17) are satisﬁed:

pl

0 Ml ⊥ C −

ζl,iAl,i 0 (4.18a)

i=1

Al,i,Ml = bl,i, i = 1,2,...,pl. (4.18b)

By convention, we set t∗l (C) = −∞ if (4.13) is infeasible, that is, if there is no overlap between the two ellipses corresponding to index l. By the nature of the

problem, we know that t∗l (C) > 0 if these two ellipses have positive overlap. It is easy to see that t∗l (C) is a concave, extended-valued function of C ∈ Ω, and as a consequence that t∗l (C) is continuous on the relative interior of its domain. Further useful facts about t∗l (C) are given in Lemma A.3. These include Lipschitz continuity in a neighborhood of a point C at which (4.17) has a strictly interior point (which,

- as noted in Subsection 4.1, occurs when the two ellipsoids have positive overlap), and the fact that any solution Ml(C) of (4.13) belongs to the Clarke subdiﬀerential of


t∗l (C).

Using the notation of (4.13) and (4.17) to capture the min-max-overlap problem (4.5), we can state this problem as follows:

min

C∈Ω

t∗(C) := max

t∗l (C). (4.19)

l=1,2,...,m

Here each element in {1,2,...,m} represents the overlap problem for a given pair of ellipsoids. Note that t∗(C) = −∞ if no pair of ellipsoids overlaps or touches.

We now deﬁne the subproblems to be solved at each iteration of the algorithm, which depend on just a subset F ⊂ {1,2,...,m} of the individual overlap problems. The key quantity is deﬁned as follows

t∗F(C) := max

t∗l (C), (4.20) where F is a subset of the strictly overlapping ellipsoid pairs, that is,

l∈F

F ⊂ {l = 1,2,...,m : t∗l (C) > 0}.

(We will be more speciﬁc about the deﬁnition of F later.) In the algorithm, the solutions Ml(C) of (4.13) for l ∈ F are used to construct a linearized subproblem whose solution is a step ∆C in the parameter C, assuming that the current C is feasible. The subproblem is as follows:

L(F,C,MF(C),ρ) : r(F,C,MF(C),ρ) := min r,∆C

r (4.21a) s.t. r ≥ t∗l (C) + ∆C,Ml(C) , l ∈ F, (4.21b) C + ∆C ∈ Ω, ∆C ≤ ρ. (4.21c)

Here ρ > 0 is a trust-region radius, and MF(C) denotes the set of matrices {Ml(C) : l ∈ F}. The problem (4.21) is convex, and its feasible set is bounded, so it has an optimal value which we denote by ∆C(ρ). Further, the KKT conditions are satisﬁed

- at this point. This claim follows from the fact that, given the point C¯ satisfying (4.16), and deﬁning ∆C = (C¯ − C) for some small positive > 0, we have that


C + ∆C = (1 − )C + C ¯ ∈ intΩ,

while the trust-region condition is strictly satisﬁed ( (C¯ −C) < ρ), and the remaining constraints in (4.21) are aﬃne. Hence, the conditions of [13, Theorem 28.2] are satisﬁed, and we can apply [13, Corollary 28.3.1] to deduce that there exist µl, l ∈ F and τ ≥ 0 such that

1 −

µl = 0, (4.22a)

l∈F

0 ≤ µl ⊥ r(F,C,MF(C),ρ) − t∗l (C) − ∆C,Ml(C) ≥ 0, l ∈ F, (4.22b) −

µlMl(C) − τu ∈ NΩ(C + ∆C) for some u ∈ ∂ ∆C , (4.22c)

l∈F

C + ∆C ∈ Ω, (4.22d) 0 ≤ τ ⊥ ρ − ∆C ≥ 0. (4.22e)

Here NΩ(C) denotes the normal cone to the closed convex set Ω at the point C (see (1.1)) and ∂ denotes a subdiﬀerential. (As noted in Section 1, since · is convex and Lipschitz continuous, the Clarke subdiﬀerential coincides with the subdiﬀerential from convex analysis.) Note that the set {τv : τ ≥ 0, v ∈ ∂ ∆C } is a closed convex cone and that it is an outer semicontinuous set-valued function of ∆C.

It is sometimes convenient to rewrite L(F,C,MF(C),ρ) by deﬁning the function GF(∆C;C,MF(C)) := max

C + ∆C,Ml(C) , (4.23)

l∈F

and writing L(F,C,MF(C),ρ) : min

GF(∆C;C,MF(C)) s.t. C + ∆C ∈ Ω, ∆C ≤ ρ.

∆C

(4.24) Note that GF(·;C,MF(C)) is convex, in fact piecewise linear.

Next, we deﬁne the reference problem P(F) that minimizes t∗F(C) deﬁned in (4.20) over C ∈ Ω:

P(F) : t∗F := min C∈Ω

t∗F(C) = min C∈Ω

t∗l (C). (4.25)

max

l∈F

Nonsmooth analysis provides the following result that characterizes solutions of (4.25).

Lemma 4.1. Suppose that for a given set F ⊂ {1,2,...,m}, C¯ is a local solution of (4.25) at which (4.17) has a strictly interior point, for all l ∈ F. Deﬁne F¯(C¯) to be the set of indices achieving the maximum in (4.25), that is, F¯(C¯) = {l ∈ F : t∗l (C¯) = t∗F}. Then there exist M¯l ∈ ∂t∗l (C¯) and scalars µl, for all l ∈ F¯(C¯), such that

µlM¯l ∈ NΩ(C¯),

−

l∈F¯(C¯)

µl = 1, µl ≥ 0, l ∈ F¯(C¯), C¯ ∈ Ω. (4.26)

l∈F¯(C¯)

Proof. We appeal to results about the Clarke subdiﬀerential applied to maxfunctions and sums of functions. First, note that the strict interiority assumption means that we can apply Lemma A.3 (iv) to deduce that each t∗l is Lipschitz continuous in a neighborhood of C¯. Hence, applying [2, Theorem 6.1.5], we have that

∂ t∗F(C) ⊂ conv{∂t∗l (C¯) : l ∈ F¯(C¯)}, (4.27)

where conv(·) denotes the convex hull. The Corollary in [4, p. 52] can be used to show that when C¯ is a solution of (4.25), we have

0 ∈ ∂ t∗F(C¯) + NΩ(C¯). The result follows by combining this expression with (4.27).

| |
|---|


By introducing multipliers for the indices l ∈ F \ F¯(C¯), we can restate the conditions (4.26) as follows:

0 ≤ µl ⊥ t∗F − t∗l (C¯) ≥ 0, for all l ∈ F, (4.28a)

µl = 1, (4.28b)

l∈F

µlM¯l ∈ NΩ(C¯), (4.28c)

−

l∈F

C¯ ∈ Ω. (4.28d) We say that a point C¯ at which these conditions are satisﬁed is Clarke-stationary for

- P(F) deﬁned in (4.25). For purposes of our main technical lemma, we deﬁne the “predicted decrease”


from subproblem L(F,C,MF(C),ρ) as follows:

Λ(F,C,MF(C),ρ) := t∗F(C) − r(F,C,MF(C),ρ). (4.29) Note that since ∆C = 0 is feasible for (4.21), we have Λ(F,C,MF(C),ρ) ≥ 0.

Lemma 4.2. Let F ⊂ {1,2,...,m} be given.

- (i) Suppose that C¯ is such that (4.17) has a strictly feasible point for all l ∈ F.

If Λ(F,C,M¯ F(C¯),ρ) = 0 for some ρ > 0 and some set of solutions Ml(C¯) to (4.13) for l ∈ F, then C¯ is Clarke-stationary for P(F).

- (ii) Λ(F,C,MF(C),ρ) is an increasing function of ρ > 0.
- (iii) Λ(F,C,MF(C),ρ)/ρ is a decreasing function of ρ > 0.
- (iv) For all C in some neighorhood of C¯ deﬁned in (i), we have that t∗F(C + ∆C(ρ)) ≤ r(F,C,MF(C),ρ) for any ρ > 0.


Proof. (i) If r(F,C,M¯ F(C¯),ρ) = t∗F for some ρ > 0, then ∆C = 0 achieves the minimum in (4.21), for C = C¯. Hence, there exist µl, l ∈ F such that the optimality conditions (4.22) are satisﬁed with ∆C = 0 and τ = 0. Thus, conditions (4.28) are satisﬁed with M¯l = M¯l(C¯) and the same values of µl, l ∈ F.

- (ii) Trivial, as the size of the feasible region for L(F,C,MF(C),ρ) increases with ρ.
- (iii) We need to show that for ρ1 and ρ2 with 0 < ρ1 < ρ2, we have Λ(F,C,MF(C),ρ1)

ρ1 ≥

Λ(F,C,MF(C),ρ2) ρ2

.

Using the formulation (4.24) of L(F,C,MF(C),ρ), and in particular the convex function GF(·;C,MF(C)) deﬁned in (4.23), we have that

GF(0;C,MF(C)) = max

l∈F

C,Ml(C) = t∗F(C).

Given the solution ∆C(ρ2) of L(F,C,MF(C),ρ2), note that ρ

1

ρ2 ∆C(ρ2) is feasible for L(F,C,MF(C),ρ1). Since ∆C(ρ1) is optimal for L(F,C,MF(C),ρ1), we have

GF(∆C(ρ1);C,MF(C)) ≤ GF

- ρ1

- ρ2


∆C(ρ2);C,MF(C)

≤ 1 −

- ρ1

- ρ2


GF(0;C,MF(C)) +

- ρ1

- ρ2


GF(∆C(ρ2);C,MF(C)).

The result follows by rearrangement of this expression, since

- Λ(F,C,MF(C),ρ1) = GF(0;C,MF(C)) − GF(∆C(ρ1);C,MF(C)),
- Λ(F,C,MF(C),ρ2) = GF(0;C,MF(C)) − GF(∆C(ρ2);C,MF(C)).


- (iv) The result follows immediately from Lemma A.3 (iv), when we use the deﬁnition (4.20) and the fact that


t∗l (C) + ∆C(ρ),Ml(C) .

r(F,C,MF(C),ρ) = max

l∈F

| |
|---|


We show now that all accumulation points of a sequence {Ck} for which

Λ(F,Ck,MF(Ck),1) → 0 are Clarke-stationary for P(F).

Theorem 4.3. Suppose that for a given set F ⊂ {1,2,...,m}, {Ck} is a sequence of matrices in Ω converging to a limit C¯ such that (4.17) has a strictly feasible point for each l ∈ F. Suppose further that Λ(F,Ck,MF(Ck),1) → 0. Then C¯ is Clarkestationary for P(F).

Proof. We invoke Theorem A.2 to deduce that for all l ∈ F, the solution sets of

- P(l,Ck) in (4.13) are uniformly bounded for all k suﬃciently large. Hence, we can identify subsequences of {Ml(Ck)} for each l ∈ F that approach some limit M¯l, where by Theorem A.2 (ii), M¯l is a solution of P(l,C¯) for each l ∈ F. We can thus write Ml(C¯) = M¯l for each l ∈ F. By deﬁning MF(Ck) and MF(C¯) in obvious ways, and taking a subsequence, we have that MF(Ck) → MF(C¯).


We show next, by contradiction, that Λ(F,C,M¯ F(C¯),1) = 0. If this claim is not true, there exists ∆C such that

∆C ≤ 1, C¯ + ∆C ∈ Ω, GF(∆C ;C,M¯ F(C¯)) ≤ t∗F(C¯) −  , for some > 0. Deﬁning

∆C k := C¯ − Ck + ∆C ,

we have from Ck → C¯, ∆Ck ≤ 1, and Ck + ∆C k = C¯ + ∆C ∈ Ω that ∆C k is feasible for L(F,Ck,MF(Ck),2). Hence, invoking Lemma 4.2 (iii), we have

t∗F(Ck) − Λ(F,Ck,MF(Ck),2) ≥ lim

GF(∆C k;Ck,MF(Ck)) ≥ lim

lim

k

k

t∗F(Ck) − 2Λ(F,Ck,MF(Ck),1)

k

= t∗F(C¯).

The ﬁnal limit above follows from the deﬁnition of t∗F, Lemma A.3 (iv), and the assumption that Λ(F,Ck,MF(Ck),1) → 0. On the other hand, we have from Ck + ∆C k = C¯ + ∆C , the deﬁnition of GF (4.23), and the limit MF(Ck) → MF(C¯) that

lim

GF(∆C k;Ck,MF(Ck)) = lim

max

Ck + ∆C k,Ml(Ck)

l∈F

k

k

C ¯ + ∆C ,Ml(Ck)

= lim

max

l∈F

k

C ¯ + ∆C ,Ml(C¯) ≤ t∗F(C¯) −  ,

= max

l∈F

where > 0 is deﬁned above. This yields the contradiction, so we conclude that Λ(F,C,M¯ F(C,¯ 1) = 0, as claimed. Clarke stationarity of C¯ for P(F) now follows from Lemma 4.2 (i).

| |
|---|


4.4. Algorithm. We now deﬁne the algorithm for solving the problem P deﬁned

by (4.19). Note that in this general setting, t∗l (C) deﬁned by (4.13) is continuous on the set

Ψl := {C : t∗l (C) > −∞},

which is closed and convex. We make additional assumptions about the nature of the solutions to the parametrized primal-dual pair (4.13), (4.17), that do not hold in general, but which are satisﬁed for the application we consider here.

Assumption 2.

- (i) t∗l (C) > −∞ ⇒ t∗l (C) ≥ 0.
- (ii) If t∗l (C) > 0, then the dual (4.17) has a strict feasible point. It is an immediate consequence of Assumption 2 and Lemma A.3 that all points C


on the boundary of Ψl have t∗l (C) = 0. We also have the following uniform continuity result.

Lemma 4.4. Suppose that t∗l (C) is deﬁned by (4.13), that Assumption 2 holds, and that Ω has the form (4.14). Let t¯ > 0 be given. Then for any > 0, there is δ > 0 such that for all C¯ ∈ Ω, all C ∈ Ω with C − C¯ ≤ δ, and all l = 1,2,...,m, the following conditions hold:

- (i) If t∗l (C¯) ≥ t¯, then t∗l (C) ≥ t∗l (C¯) − ;


- (ii) t∗l (C) ≤ max(0,t∗l (C¯)) + . Proof. Note ﬁrst that since Ω is compact, the set Ψl(t¯) := {C ∈ Ω | t∗l (C) ≥ t¯}


is also compact, for any l ∈ {1,2,...,m} and any t¯> 0. Since t∗l (·) is continuous at every point of this set, under the stated assumptions, it is uniformly continuous on

this set. Thus for any > 0, there is a value δ = δl( ) > 0 such that (i) holds. Thus it is suﬃcient for (i) to deﬁne δ to be minl=1,2,...,m δl( ).

For (ii), we suppose for contradiction that for some > 0, there is no δ > 0 with the property claimed. Thus, for any sequence {δr} with δr ↓ 0, we can ﬁnd C¯r ∈ Ω, Cr ∈ Ω with Cr − C¯r ≤ δr, and l ∈ {1,2,...,m} such that

t∗l (Cr) > max(0,t∗l (C¯r)) +  . (4.30) By taking a subsequence if necessary, we can assume that this inequality holds for some ﬁxed l ∈ {1,2,...,m}. Since all Cr belong to the compact set Ω ∩ {C | t∗l (C) ≥ }, we can assume (by taking another subsequence if necessary) that Cr → Cˆ, for some Cˆ with t∗l (Cˆ) ≥ . It follows that C¯r → Cˆ also, so using continuity of t∗l and taking limits in both sides of (4.30), we obtain

max(0,t∗l (C¯r)) + = max(0,t∗l (Cˆ)) + ≥ t∗l (Cˆ) +  , a contradiction.

t∗l (Cˆ) = lim

t∗l (Cr) ≥ lim

r→∞

r→∞

| |
|---|


A key issue in implementing the algorithm is to decide which subset F of the overlapping pairs to use in calculating the step ∆C in (4.21). Clearly, F should include the indices l for which the overlaps between the corresponding ellipsoid pairs are at or near the maximum. It could also include other indices with positive (but smaller) overlap. Clearly, it cannot contain any non-overlapping ellipsoids, as the problem P(l,C) (4.13) has no solution in this case, so Ml(C) is not deﬁned. We settle on the following requirement, which depends on parameters η1,η2 ∈ (0,1) with 0 < η1 < η2 < 1: Given Ck for which t∗(Ck) > 0 (see deﬁnition (4.19)), we choose Fk to satisfy:

{l : t∗l (Ck) ≥ η2t∗(Ck)} ⊂ Fk ⊂ {l : t∗l (Ck) ≥ η1t∗(Ck)}. (4.31)

Algorithm 4.4 describes our method. It follows a standard trust-region framework, though its analysis is a little non-standard. At each iteration, we calculate a candidate step ∆Ck by solving the linearized subproblem (4.21) with trust-region radius ρk, and calculate the predicted reduction Λ(Fk,Ck,MF

(Ck),ρk) (4.29) expected from this step. If the actual objective achieves at least a fraction c1 of this decrease (for c1 ∈ (0,1)), we accept the step. If in fact the improvement is at least a larger fraction c2 of the expected decrease, we may increase the trust-region radius for the next iteration. Otherwise, we do not take the step, but rather shrink the trust-region radius and proceed to the next iteration.

k

We now show that when the values t∗(Ck) are bounded away from zero, there is a positive threshold such that any step ∆Ck with norm smaller than this threshold will be accepted.

Lemma 4.5. Suppose that Assumption 2 holds and let t¯> 0 be given. Let Ck be any iterate with t∗(Ck) ≥ t¯ such that Ck is not Clarke-stationary for the problem P deﬁned in (4.19), and suppose that Fk satisﬁes (4.31). Then there exists a threshold value ρ¯t¯ > 0 (independent of Ck) such that

t∗(Ck + ∆C(ρ)) ≤ t∗(Ck) − Λ(Fk,Ck,MF

### (Ck),ρ) < t∗(Ck) (4.32)

k

Algorithm 2 Packing Ellipsoids by Minimizing Overlap

Given Ω ⊂ SIRn×n compact; η ∈ (0,1); c1 and c2 with 0 < c1 < c2 < 1; φ1 and φ2 with 0 < φ1 < 1 < φ2; and ρmax > 0; Choose C0 ∈ Ω, ρ0 ∈ (0,ρmax]; for k = 0,1,2,... do

Deﬁne Fk as in (4.31); Solve L(Fk,Ck,MF

(Ck),ρk) (4.21) to obtain ∆Ck; Compute predicted decrease Λ(Fk,Ck,MF

k

(Ck),ρk) from (4.29); if ∆Ck = 0 or t∗(Ck + ∆Ck) = 0 then

k

stop; end if if t∗(Ck + ∆Ck) ≤ t∗(Ck) − c1Λ(Fk,Ck,MF

(Ck),ρk) then

k

Ck+1 ← Ck + ∆Ck; if t∗(Ck + ∆Ck) ≤ t∗(Ck) − c2Λ(Fk,Ck,MF

(Ck),ρk) then ρk+1 ← min(φ2ρk,ρmax);

k

## end if

else Ck+1 ← Ck; ρk+1 ← φ1ρk;

end if end for

whenever ∆C(ρ) is a solution of L(Fk,Ck,MF

(Ck),ρ) with ρ ∈ (0,ρ¯t¯].

k

Proof. Note ﬁrst that if Ck were Clarke-stationary for P(Fk), given that Fk contains all the indices l for which t∗l (Ck) attains the maximum t∗(Ck), we would have that Ck is also Clarke-stationary for P, which we have assumed is not the case. From Assumption 2 and Lemma 4.2 (i) we have therefore that Λ(Fk,Ck,MF

(Ck),ρ) > 0 for all ρ > 0 and all solutions Ml(Ck) to (4.13) with C = Ck and l ∈ Fk.

k

Now deﬁne = t¯(1 − η2)/2, and let ρ¯t¯ be the corresponding (positive) value of δ from Lemma 4.4. Consider any ∆C such that ∆C ≤ ρ¯t¯. For indices l such that t∗l (Ck) = t∗(Ck) ≥ t¯, we have from Lemma 4.4 (i) that

t∗l (Ck + ∆C) ≥ t∗(Ck) − t¯(1 − η2)/2 ≥ t∗(Ck)(1 + η2)/2. For indices l ∈/ Fk, we have t∗l (Ck) ≤ η2t∗(Ck), and so from Lemma 4.4 it follows that t∗l (Ck+∆C) ≤ max(0,t∗l (Ck))+t¯(1−η2)/2 ≤ η2t∗(Ck)+t¯(1−η2)/2 ≤ t∗(Ck)(1+η2)/2. Hence, for ∆C ≤ ρ¯t¯, the index l for which t∗(Ck +∆C) = t∗l (Ck +∆C) comes from the set Fk, that is,

(Ck + ∆C) = t∗(Ck + ∆C). So choosing ρ ∈ (0,ρ¯t¯] and setting ∆C(ρ) to be the solution of L(Fk,Ck,MF

t∗F

k

(Ck),ρ), we have from Lemma 4.2 (iv) that

k

t∗(Ck + ∆C(ρ)) = t∗F

(Ck + ∆C(ρ)) ≤ t∗F

k

(Ck) − Λ(Fk,Ck,MF

(Ck),ρ) < t∗F

k

k

(Ck)

k

= t∗(Ck),

- as claimed. The inequality (4.32) satisﬁes the step acceptance conditions in Algorithm 4.4,


| |
|---|


since 0 < c1 < c2 < 1. It follows immediately that for any Ck with t∗(Ck) > 0, the algorithm cannot “get stuck” by performing inﬁnitely many unsuccessful iterations eventually it will decrease ρ to the point where the step acceptance condition holds.

We now prove the main convergence result.

Theorem 4.6. Suppose that Assumption 2 holds. Then either Algorithm 4.4 terminates ﬁnitely, or else it generates an inﬁnite sequence of iterates {Ck} for which accumulation points exist, and all accumulation points are Clarke-stationary points of P. When t∗(Ck) ↓ 0, all accumulation points are in fact global solutions of P.

Proof. The ﬁnite termination cases are obvious, so we focus on the case of an inﬁnite sequence {Ck}. Since all iterates are conﬁned to the compact set Ω, accumulation points of sequence {Ck} exist. Note that the sequence of function values {t∗(Ck)} is decreasing. The ﬁnal statement of the theorem is self-evident, as this case indicates convergence to points at which there are no overlaps between ellipsoids. Hence, we focus on the case in which there exists t¯ > 0 such that t∗(Ck) ≥ t¯ for all k. From Lemma 4.5, we see that at each iteration k, the trust-region radius ρk will generate a successful step ∆Ck whenever it falls below ρ¯t¯. Hence, since the algorithm decreases ρ by a factor of φ1 after each unsuccessful step, we have that

ρk ≥ min(ρ0,φ1ρ¯t¯), for all k. (4.33)

In considering accumulation points of the sequence {Ck} we can remove all repeated entries from the sequence. These repeats arise from unsuccessful steps (for which the acceptance condition was not satisﬁed), and the accumulation points of the sequence are the same whether the repeated entries are present or not. Note that there must be inﬁnitely many successful steps since, as we note in the comment after Lemma 4.5, the algorithm must eventually move away from any non-stationary point Ck with t∗(Ck) > 0. We denote the subsequence of successful iterates by S.

At a successful iteration k ∈ S, we have t∗(Ck+1) = t∗(Ck + ∆Ck)

≤ t∗(Ck) − c1Λ(Fk,Ck,MF

### (Ck),ρk) ≤ t∗(Ck) − c1 min(ρk,1)Λ(Fk,Ck,MF

k

### (Ck),1) ≤ t∗(Ck) − c1 min(ρ0,φ1ρ¯t¯,1)Λ(Fk,Ck,MF

k

(Ck),1),

k

where we used Lemma 4.2 (ii) and (iii) to derive the second inequality, and the last inequality comes from (4.33). Since the sequence {t∗(Ck)} is decreasing and bounded below (by t¯), we have 0 < t∗(Ck)−t∗(Ck+1) ↓ 0, so by rearranging and using the fact that min(ρ0,φ1ρ¯t¯,1) > 0, we have

Λ(Fk,Ck,MF

lim

(Ck),1) = 0. (4.34)

k

k∈S

Now suppose that C¯ ∈ Ω is an accumulation point of the full sequence {Ck}. As noted above, it must also be an accumulation point of the “successful iterate” sequence {Ck}k∈S. So by taking a further subsequence S ⊂ S, we have limk∈S Ck = C¯. Since there is only a ﬁnite number of possibilities for the set Fk, we can take another subsequence S ⊂ S such that, in addition, Fk ≡ F for all k ∈ S . By the deﬁnition (4.31), we have that t∗l (Ck) ≥ η1t∗(Ck) ≥ η1t¯ for all l ∈ Fk and all k ∈ S . Thus, using continuity of t∗l , we have that

t∗l (C¯) ≥ η1t¯> 0, for all l ∈ F,

implying that P(l,C¯) has a strictly feasible point for all l ∈ F. Clarke stationarity of C¯ now follows from (4.34), using the fact that S ⊂ S and applying Theorem 4.3.

| |
|---|


5. Application: Chromosomal Arrangement in Human Cell Nuclei. We return to the application introduced in Section 1, that is, ﬁnding arrangements of chromosome territories in a cell nucleus on the basis of simple geometric principles (namely, low overlap and discouragement of proximity for homologous pairs) and seeing how closely the resulting arrangements match the experimental observations that have been made to date.

During most of the cell cycle the chromosomes of higher eukaryotes are organized into distinct compartments known as chromosome territories (CTs). These domains have a roughly ellipsoidal shape and can overlap each other. This overlap is believed to have an important biological purpose, since it allows for the interaction and coregulation of diﬀerent genes. Additionally, the CTs tend to exploit the space available inside the cell nucleus, to allow for internal DNA-free channels, the interchromatin compartments. These compartments allow CTs deep inside the cell nucleus to be accessible for regulatory factors.

As noted earlier, the arrangement of CTs is known to be non-random. Arrangements are known to be broadly conserved during evolution and are similar among cell types with similar developmental pathways. CT arrangements can also change during processes such as cancer development or cell diﬀerentiation. See [5] for more details and an overview about what is known about CT arrangements.

There is strong evidence that chromosomes have a preferred radial position inside the nucleus. These preferences appear to be diﬀerent for nuclei of diﬀerent shapes, spherical and ellipsoidal. In ellipsoidal nuclei, CT size seems to drive the radial preferences, with the smaller CTs tending to lie nearer to the center. In spherical nuclei the situation is less clear, with the more gene-dense chromosomes seeming to lie nearer to the center of the nucleus.

There is also evidence for neighbor preferences, which may play an important role in causing co-regulated genes in diﬀerent chromosomes to be closer together. In particular, it has been observed recently that CTs tend to favor neighborhoods of heterologous chromosomes. This results in the two chromosomes in a homologous pair tending to be well separated. (In human cells there are 22 homologous pairs, each consisting of one chromosome from the mother and a similar one from the father.)

We model a CT arrangement as a packing of overlapping ellipsoids of various sizes inside an ellipsoidal container, which represents the cell nucleus. Minimizing maximum overlap mimics the fact that the CTs exploit the space available in the nucleus, to allow for the presence of contiguous DNA-free interchromatin channels. These channels extend from the nuclear pores into the interior of the nucleus, making even the deepest CTs accessible from outside and connecting most chromosome territories.

In this section we analyze whether purely geometric considerations, enforcing the simple principles of minimal overlap and well-separatedness of homologous pairs, can explain the observed arrangements of CTs in cell nuclei of diﬀerent sizes and shapes.

5.1. Human Cell Nucleus. The human cell nucleus has a volume of between 500 µm3 and 1600 µm3, depending on the cell size and stage of diﬀerentiation. The shape also diﬀers according to cell type. Human ﬁbroblasts, for example, have ﬂat ellipsoidal nuclei, whereas lymphocytes have spherical cell nuclei. In this study we analyze three diﬀerent nucleus sizes: small (500 µm3), medium (1000 µm3) and large

(1600 µm3). For all three sizes we consider two shapes: spherical nuclei and ﬂat ellipsoidal nuclei (with axis lengths in the ratio 1:2:4).

We estimate the volume of each CT to be proportional to the number of base pairs in the chromosome, with the constant of proportionality determined by the average chromatin packing density. The number of base pairs for human cells ranges from 47 Mbp (chromosome 21) to 247 Mbp (chromosome 1), while the human chromatin packing density in living cells has been estimated to be 0.15 µm3/Mbp ([12]). By multiplying the total number of base pairs by this average density, we arrive at a total volume of about 461 µm3 over all CTs. The individual volumes for each chromosome territory are given in Table 5.1.

Table 5.1 Volume of each chromosome territory based on chromatin packing density of 0.15 µm3/Mbp.

CT 1 2 3 4 5 6 7 8 volume 37.05 36.45 29.85 28.65 27.15 25.65 23.85 21.90 CT 9 10 11 12 13 14 15 16 volume 21.00 20.25 20.10 19.80 17.10 15.90 15.00 13.35 CT 17 18 19 20 21 22 X Y volume 11.85 11.40 9.45 9.30 7.05 7.50 23.25 8.70

5.2. Implementation. The algorithm was implemented in Matlab and CVX [7]. Both, the pairwise-overlap problems and the master problem at each iterate of the algorithm were formulated in CVX. The algorithm is terminated when one of the following conditions holds.

- (i) The ratio of predicted decrease to trust-region radius falls below a speciﬁed tolerance. Using the notation of Algorithm 4.4, we state this condition as

Λ(Fk,Ck,MF

k

(Ck),ρk)/ρk ≤ Tol1, where we set Tol1 = .005 in our experiments.

- (ii) The maximum overlap falls below a small fraction Tol2 of the volume of the enclosing ellipsoid. We used Tol2 = .0001 in our experiments.
- (iii) The algorithm runs for 100 iterations. Many instances of the problem, including problems of diﬀerent sizes and shapes,


with diﬀerent random starting points, were executed on servers running various versions of Linux.

5.3. Radial Preferences. In the ﬁrst set of experiments, we use Algorithm 4.4 to arrange the CTs so as to minimize the maximal pairwise overlap, with overlap measured as in Section 4.1. (We enforce no constraints on homologous pairs in this ﬁrst set.) We set up numerous trials with the data varied as follows.

- (i) CT volumes are obtained by sampling from a normal distribution, with mean taken from Table 5.1 and the standard deviation set to .02 of the mean.
- (ii) The relative axis lengths are varied around the intercepts found in [9] for mouse chromosomes, namely, 1:2.9:4.4. The second and third ratios are sampled from a Gaussian distribution with mean values 2.9 and 4.4, respectively, and standard deviations of .1 times the mean. (The absolute axis lengths are then adjusted to match the volume chosen in (i).)


Table 5.2

Statistics for ﬁnal objective values attained in the six scenarios, showing number of trials, means, and standard deviations, both before and after the screening step.

|shape vol (µm3)|Before Screening trials mean sd|After Screening trials mean sd|
|---|---|---|
|spherical 500|100 3.0889 0.0533|100 3.0889 0.0533|
|ellipsoidal 500|100 3.2769 0.0660|100 3.2769 0.0660|
|spherical 1000|200 1.8927 0.4409|195 1.8233 0.0657|
|ellipsoidal 1000|200 1.9723 0.0714|200 1.9723 0.0714|
|spherical 1600|100 0.6342 1.4325|89 0.1349 0.0362|
|ellipsoidal 1600|100 0.1338 0.0291|100 0.1338 0.0291|


We analyzed the radial preferences for two diﬀerent nucleus shapes — spherical and ﬂat ellipsoidal with axis ratios of 1:2:4 — and for the small, medium, and large nuclei with sizes described above.

For each of these six diﬀerent scenarios we ran 100-200 trials, each with data perturbed as described above and each from a diﬀerent random starting point. We applied a screening step to remove those trials that have a ﬁnal objective value greater than

f∗ + max(0.5,min(0.2 ∗ f∗,2.0)),

where f∗ is the lowest objective value obtained over all trials for this scenario. Table 5.2 shows statistics on the ﬁnal objective value for each of the six scenarios. Only a few trials were removed in the screening step, mostly for the large spherical nucleus in which the no-overlap solution was not quite attained. After screening, the ﬁnal objective values were similar for all trials on a given scenario.

Recall we use Algorithm 4.4 to solve the convex relaxation (4.9) of the original formulation (4.5), in which the prescribed half-axis lengths (ri1,ri2,ri3) are replaced by the constraints (4.6). We found that a number of the ellipsoids were “more rounded”

- at the solution than our prescription would require, but that the deformation typically aﬀected only a subset of the ellipsoids and was not too severe. By taking relative dif-


ference in the 2 norm between the vector of actual half-axis lengths and the prescribed values, we found that on small nuclei, an average of 8 of the 46 CTs experienced a relative change of greater than 10%. For medium spherical nuclei, about 7 out of 46 changed by more than 10% while the corresponding number for large spherical nuclei is 11 out of 46. The statistics for ellipsoidal nuclei are slightly smaller, about 5 for small and large nuclei and 3 for medium nuclei.

We analyzed the solutions generated in the trials remaining after the screening step to ﬁnd the distances of each ellipsoid from the center of the nucleus. Figure 5.1 contains scatter plots that show the mean volume of each CT (on the horizontal axis) plotted against the distance between the center of that CT and the nuclear center (on the vertical axis), for a medium-sized nucleus (volume of 1000 µm3) and for both spherical and ﬂat ellipsoidal shapes. (The scatter plots for the large and small volume nuclei are similar, so we do not show them here.) A least-squares regression line is also shown. In both graphs, a negative trend is detectable, meaning that the larger ellipsoids tend to lie closer to the nuclear center, while the smaller ones prefer peripheral positions. This is the opposite trend to the one observed in nature, suggesting that the minimum-overlap criterion alone is insuﬃcient to explain the experimental results.

(a) Spherical Nucluei

(b) Ellipsoidal Nuclei

Fig. 5.1. Scatter plots and regression lines for distances of ellipsoidal chromosome territories to nucleus center, for medium-sized nuclei. Horizontal axis is CT volume, vertical axis is distance to nucleus center.

In Table 5.3 we report the slopes of the regression line for all six scenarios. Interestingly, the negative trend is consistently weaker for ﬂat ellipsoidal nuclei compared to spherical nuclei. Experimentalists report a preference for larger CTs to be on the periphery for ellipsoidal nuclei, while for spherical nuclei, the radial preferences are believed to be correlated with gene density.

Table 5.3 Slope of regression line for all six scenarios.

| |small medium large|
|---|---|
|spherical ellipsoidal<br><br>|-0.0050562 -0.0029405 -0.0020672<br>-0.0047345 -0.0025045 -0.0018849<br>|


5.4. Radial preferences assuming heterologous CT groupings. Khalil et al. [9] showed that CTs tend to assemble in heterologous neighborhoods, causing the distances between homologous chromosome pairs to be larger in general than heterologous inter-CT distances. They discuss a number of possible explanations for this phenomenon, such as that heterologous neighborhoods act as a buﬀer zone in preventing inter-homologue recombination and protect against the loss of heterozygosity. The authors also analyze whether the radial preferences discussed in the previous subsection could explain the preference for arrangements with larger homologous inter-CT distances. Using simulations, they give a negative answer to this question.

In the following analysis, we invert the question, asking instead whether the preference for heterologous neighborhoods can explain the observed radial preferences. To investigate this question, we add penalties to our model to discourage the CTs in a homologous pair from being too close to each other. We solve the resulting formulation using a combination of Algorithm 1 for sphere packing with Algorithm 4.4 for ellipsoid packing.

We denote the set of index pairs (i,j) corresponding to homologous chromosome pairs by H and we introduce a new variable η to capture the proximity of CTs in a homologous pair. Speciﬁcally, we deﬁne for each ellipsoid i an enclosing sphere that is concentric with the ellipsoid i, with radius λ times the maximum semi-axis length ri of the CT, where λ ≥ 1 is a user-deﬁned parameter. We deﬁne η to be the maximal

overlap of these enclosing spheres, over all homologous pairs, by adding constraints whose form is similar to (3.4b). We then add a penalty term cη to the objective (where c ≥ 0 is some penalty parameter), to obtain the following extension of formulation (4.5).

min

ξ + cη (5.1a)

ξ,η,(ci,Si,Σi),i=1,2,...,N

subject to ξ ≥ Oˆ(ci,cj,Σi,Σj), 1 ≤ i < j ≤ N, (5.1b) λ(ri − rj) − ci − cj 2 ≤ η, (i,j) ∈ H, (5.1c) Ei ⊂ E, i = 1,2,...,N, (5.1d) Σi = Si2, (5.1e) semi-axes of Ei are ri1,ri2,ri3, i = 1,2,...,N. (5.1f)

We can relax this to obtain an extended formulation of (4.9). To solve, we extend Algorithm 4.4 by adding linearizations of the constraints (5.1b) to each subproblem, in the manner of (3.6b).

For our simulations, we choose c = 100 and λ = 1.25. As in Subsection 5.3, we generated about 100-200 trials by perturbing CT volumes and dimensions randomly around given mean values and using diﬀerent random starting points. The screening procedure described in the previous subsection was applied to remove those trials with less competitive ﬁnal objective values. Statistics for the ﬁnal objectives are shown in Table 5.4. The large objective values in the ﬁrst line of the table indicates that for small spherical nuclei, it was not possible to ﬁnd solutions in which the homolog separation was enforced adequately. (The only trial that survived screening was one that violated these conditions signiﬁcantly less than most others.) Among the other scenarios, only the medium spherical nucleus saw signiﬁcant numbers of trials removed by screening. Here, most of the trials attained ﬁnal objectives quite close to 1.90, while the others had signiﬁcantly higher values. In the other four scenarios — small ellipsoidal, medium ellipsoidal, large spherical, and large ellipsoidal — proximity penalties for homologous pairs were not incurred, and ﬁnal objective values were tightly clustered.

The convex relaxation of our problem that encourages separation of homologous CT pairs does less well in preserving the dimensions of the ellipsoids than the formulation considered in Section 5.3. For spherical nuclei 26 out of the 46 CTs for small nuclei experienced a relative change in the half-axes lengths of more than 10%. For the medium spherical nuclei it was in average 11 out of 46 and for the large spherical

Table 5.4

Statistics for ﬁnal objective values attained in the six scenarios in which homolog proximity is penalized, showing number of trials, means, and standard deviations, both before and after the screening step.

|shape vol (µm3)|Before Screening trials mean sd|After Screening trials mean sd|
|---|---|---|
|spherical 500|100 294.0617 46.8185|1 184.0292 0.0000|
|ellipsoidal 500|100 3.6556 0.2691|95 3.5987 0.0879|
|spherical 1000|200 15.0885 20.7260|114 1.8993 0.0833|
|ellipsoidal 1000|200 2.0088 0.5118|192 1.9060 0.0691|
|spherical 1600|100 0.4424 1.2293|94 0.1369 0.0213|
|ellipsoidal 1600|100 0.2752 0.8097|97 0.1343 0.0251|


(a) Spherical Nuclei

(b) Ellipsoidal Nuclei

Fig. 5.2. Scatter plots and regression lines for ellipsoidal chromosome territory distances to nucleus center, where penalties to enforce heterologous groupings are present in the objective. Horizontal axis is CT volume, vertical axis is distance to nucleus center.

nuclei 17 out of 46. The statistics for the ellipsoidal nuclei were somewhat smaller: 12 for the small nuclei, 4 for the medium nuclei, and 9 for the large nuclei. On the small nuclei, the distortions can be explained by the tightness of space, while on large nuclei, the fact that all CTs can be ﬁt without any overlap reduces the need for them to adopt their lowest-volume dimensions (which would achieve the prescribed semi-axis lengths).

Figure 5.2 contains scatter plots showing the mean volume of each CT (on the horizontal axis) plotted against the distance between the center of that CT and the nuclear center (on the vertical axis), for a medium-sized nucleus (volume of 1000 µm3) and for both spherical and ﬂat ellipsoidal shapes. (As in Subsection 5.3, scatter plots for the large and small volume nuclei are similar, so we do not show them here.) Here the regression line shows a signiﬁcant positive trend, meaning that the smaller ellipsoids tend to lie in the interior of the nucleus, while the larger ones prefer peripheral positions. Hence, by adding penalties on nearness of homologous pairs to the formulation, we are able to match the radial preferences observed in nature.

Another interesting observation, more evident in Figure 5.2(a), is that the X and Y chromosomes both lie closer to the nucleus center than their size would suggest. This makes sense, as these are the only two chromosomes not subject to the homologouspair separation penalties.

In Table 5.5 we report the slopes of the regression line for all six size / shape scenarios considered in this section. These results highlight a signiﬁcant diﬀerence between spherical and ﬂat-ellipsoidal nuclei. The radial preference is consistently weaker for spherical nuclei than in ﬂat-ellipsoidal nuclei.

Table 5.5 Slope of regression line for all six scenarios assuming heterologous CT groupings.

| |small medium large|
|---|---|
|spherical ellipsoidal|0.0031803 0.0078299 0.0072028 0.0081768 0.0102088 0.0145001<br><br>|


### 6. Discussion. We have described a bilevel optimization procedure for ﬁnding local solutions of the problem of packing spheres and ellipsoids in ﬁnite volumes, and

used these procedures to model and analyze chromosome arrangement in cell nuclei. Semideﬁnite programming duality is used to obtain the sensitivity information needed to construct the approximation to the upper-level problem that is solved at each iteration of the trust-region procedure. Our convergence analysis takes place in a general setting in which the lower-level problems are semideﬁnite programs parametrized by their objective coeﬃcient matrix; it is not conﬁned to the speciﬁc form of the semidefinite programs arising from the S-procedure for overlapping ellipsoids. Thus it may be adaptable to other design problems involving parametrized systems that can be modeled by semideﬁnite programs.

In the CT packing application discussed in Section 5, we initially found that the arrangements observed experimentally could not be explained by the simple geometric principle of minimizing the maximum overlap. However, when we enhanced the model to capture the recently observed phenomenon of heterologous neighborhoods / homologous pair separation, the radial preferences observed in nature (in which larger CTs tended to lie further from the nuclear center) were recovered in our simulations. The homologous-pair-separation aspects of our model are governed by two positive parameters c and λ; we reported results in Subsection 5.4 only for the values c = 100 and λ = 1.25. From an examination of Tables 5.3 and 5.5, we speculate that it would be possible to choose these parameters in such a way that the slope of the regression line for spherical nuclei would be approximately zero, while the corresponding slope for ellipsoidal nuclei would be positive. Such a result would be consistent with experimental observations that identify no clear radial preference for spherical nuclei, but a pronounced radial preference for ellipsoidal nuclei.

We obtained results on a limited but representative range of nuclei dimensions. In future work, we will explore CT conﬁgurations for a wider range of ellipsoidal shapes and sizes, corresponding to known dimensions of nuclei in diﬀerent cell types. We will also enhance the model as further biological results are obtained, aiming to ﬁnd biologically plausible, elementary principles that explain experimental observations (in the spirit of Occam’s Razor).

Appendix A. Technical Results for Parametrized Semideﬁnite Programs.

In this section we consider the following primal-dual pair of semideﬁnite programs that are parametrized by the primal objective term C:

min

X

C,X s.t. Ai,X = bi, i = 1,2,...,p, X 0, (A.1)

bTζ s.t.

max

ζ,S

p

ζiAi + S = C, S 0. (A.2)

i=1

We denote solutions of these problems by X(C) and (ζ(C),S(C)), respectively. (Our interest is in the application to the SDP pair (4.13), (4.17), but we have simpliﬁed the notation here.)

We show ﬁrst that the solutions to (A.1) are uniformly bounded in a neighborhood of a C for which a strictly feasible point for the dual (A.2) exists. The result is an almost immediate consequence of [17, Theorem 4.1].

Lemma A.1. Consider the primal-dual pair (A.1), (A.2) of semideﬁnite programs: Suppose that (A.1) is feasible (with feasible point Xˆ), and that at some matrix C0 ∈ SIRn×n, there exists a strictly feasible point (ζ,ˆ Sˆ) for (A.2), where the eigenvalues of Sˆ are bounded below by σ > 0. Then there exists a constant δ > 0 such that

for all matrices C ∈ SIRn×n with C − C0 F ≤ δ, (A.1) has a nonempty solution set, and all solutions X(C) are bounded as follows:

2 σ

( X, ˆ Sˆ + δ X ˆ F). Moreover the optimal values of the problems (A.1) and (A.2) are equal.

X(C) F ≤

Proof. We have for any X feasible for the primal (note that the primal feasible region does not depend on C) that

C,X = C0,X + C − C0,X

p

ζˆiAi + S,Xˆ + C − C0,X

=

i=1

= bTζˆ+ S,X ˆ + C − C0,X .

Since bTζˆ is independent of X, we can obtain an equivalent to the primal problem by replacing its objective C,X by S ˆ + C − C0,X . Using the assumed feasible point Xˆ of (A.1) (note that there is no dependence of Xˆ on C), we can formulate (A.1) equivalently as follows:

S ˆ + C − C0,X s.t. Ai,X = bi, i = 1,2,...,p, X 0, (A.3a) S ˆ + C − C0,X ≤ S ˆ + C − C0,Xˆ . (A.3b)

min

X

By choosing δ ∈ (0,σ/2], we have that all eigenvalues of Sˆ + C − C0 are bounded below by σ/2. Hence from “Fact 14” of [17], we have that

2 σ

S ˆ+C−C0,X ≤ S ˆ+C−C0,Xˆ ⇒ X F ≤

S ˆ+C−C0,Xˆ ≤

2 σ

( S, ˆ Xˆ +δ X ˆ F).

Hence, (A.3) involves the minimization of a continuous function over a nonempty compact set, so the solution set exists, and moreover, all solutions are bounded as claimed.

The last claim can be derived exactly as in [17, Theorem 4.1]. The next result examines the solution of a sequence of parametrized SDPs.

| |
|---|


Theorem A.2. Given Ai, i = 1 = 1,2,...,p and b ∈ IRp as in Lemma A.1, such that (A.1) is feasible, let C¯ ∈ SIRn×n be such that there exists a strictly feasible point for (A.2) when C = C¯. Consider a sequence {Ck} with Ck ∈ SIRn×n and Ck → C¯. Then the following is true:

- (i) There is a constant β > 0 and index K such that (A.1) with C = Ck has nonempty solution set for all k ≥ K, and X(Ck) F ≤ β for all such solutions.
- (ii) If {X(Ck)} is a sequence of solutions of (A.1) with C = Ck, then this sequence has at least one accumulation point, and all such accumulation points are solutions of (A.1) with C = C¯.


Proof. The ﬁrst claim (i) is an immediate consequence of Lemma A.1. For (ii), note that boundedness of X(Ck) ensures existence of accumulation points. Suppose that X¯ is such a point and assume WLOG that X(Ck) → X¯. Note ﬁrst that X¯ is feasible for (A.1) regardless of C. If X¯ were not optimal for (A.1) with C = C¯, then there would exist another feasible matrix X˜ with C, ¯ X˜ < C, ¯ X¯ . But since

lim

k

Ck,X˜ = C, ¯ X˜ < C, ¯ X¯ = lim

k

Ck,X(Ck) ,

we have that Ck,X˜ < Ck,X(Ck) for all k suﬃciently large, contradicting optimality of X(Ck). Hence (ii) is true.

| |
|---|


We next prove some elementary and useful facts about the value function of (A.1), which we denote by t(C).

Lemma A.3. Suppose that (A.1) is feasible, and let C¯ ∈ SIRn×n be such that there exists a strictly feasible point for (A.2) when C = C¯. Then there exists a neighborhood N of C¯ within which the following claims are true.

- (i) t(·) is a concave function.
- (ii) For all C ∈ N and all ∆C ∈ SIRn×n, we have t(C + ∆C) ≤ t(C) + X(C),∆C , (A.4)

where X(C) is any solution of (A.1).

- (iii) Any X(C) that solves (A.1) belongs to the Clarke subdiﬀerential of t(·) at C.
- (iv) t(·) is Lipschitz continuous in N. Proof. The proof of (i) is elementary. For (ii), note ﬁrst from Lemma A.1 that we can choose N so as to ensure that a


solution X(C) to (A.1) exists for all C ∈ N. We have (denoting by Ψ the feasible set for (A.1)) that

t(C + ∆C) = min

X∈Ψ

C + ∆C,X ≤ C + ∆C,X(C) = t(C) + ∆C,X(C) ,

as required.

- For (iii), note that (by taking the negative of the inequality (A.4)) −X(C) is a

subgradient of the convex function (−t)(C), and so −X(C) belongs to the Clarke subdiﬀerential of (−t)(C). It follows from [2, p. 128, Exercise 8(c)] (with λ = −1) that X(C) belongs to the Clarke subdiﬀerential of t(C), as claimed.

- For (iv), note from Lemma A.1 that we can choose N such that X(C) is


uniformly bounded for all C ∈ N (by β > 0, say). Denoting by C1 and C2 any two points in N, we have from (A.4) that

t(C2) ≤ t(C1) + X(C1),C2 − C1 , t(C1) ≤ t(C2) + X(C2),C1 − C2 .

Thus

|t(C1) − t(C2)| ≤ max( X(C1) , X(C2) ) C1 − C2 ≤ β C1 − C2 , proving the Lipschitz property.

| |
|---|


## Acknowledgments

We thank Saira Mian for helpful discussions about the application to chromosome arrangement in cell nuclei. We are grateful to the Institute for Mathematics and its Applications at the University of Minnesota for supporting visits by both authors while this research was conducted.

REFERENCES

- [1] A. Bolzer, G. Kreth, I. Solovei, D. Koehler, K. Saracoglu, C. Fauth, S. Mu¨ller, R. Eils, C. Cremer, M. R. Speicher, and T. Cremer. Three-dimensional maps of all chromosomes in human male ﬁbroblast nuclei and prometaphase rosettes. PLoS Biol., 3, 2005.


- [2] J. Borwein and A. S. Lewis. Convex Analysis and Nonlinear Optimization: Theory and Examples. CMS Books in Mathematics. Springer, 2000.
- [3] S. Boyd and L. Vandenberghe. Convex Optimization. Cambridge University Press, 2003.
- [4] F. H. Clarke. Optimization and Nonsmooth Analysis. John Wiley, New York, 1983.
- [5] T. Cremer and M. Cremer. Chromosome territories. Cold Spring Harb. Perspect. Biol., 2010.
- [6] A. Donev, I. Cisse, D. Sachs, E. A. Variano, F. H. Stillinger, R. Connelly, S. Torquato, and P. M. Chaikin. Improving the density of jammed disordered packings using ellipsoids. Science, 303:990–993, February 2004.
- [7] M. Grant and S. Boyd. CVX User’s Guide. Stanford University, version 1.22 edition, February 2012.
- [8] T. A. Hales. A proof of the Kepler conjecture. Annals of Mathematics, Second Series, 162(3):1065–1185, November 2005.
- [9] A. Khalil, J. L. Grant, L. B. Caddle, E. Atzema, K. D. Mills, and A. Arneodo. Chromosome territories have a highly nonspherical morphology and nonrandom positioning. Chromosome Res., 15:899–916, 2007.
- [10] B. D. Lubachevsky and R. L. Graham. Curved hexagonal packings of equal disks in a circle. Discrete and Computational Geometry, 18(2):179–194, June 2007.
- [11] N. V. Marella, S. Bhattacharya, L. Mukherjee, J. Xu, and R. Berezney. Cell type speciﬁc chromosome territory organization in the interphase nucleus of normal and cancer cells. J. Cell. Physiol., 221:130–138, 2009.
- [12] I. Mu¨ller, S. Boyle, R. H. Singer, W. A. Bickmore, and J. R. Chubb. Stable morphology, but dynamic internal reorganisation, of interphase human chromosomes in living cells. PLoS One, 5, 2010.
- [13] R. T. Rockafellar. Convex Analysis. Princeton University Press, Princeton, N.J., 1970.
- [14] C. A. Rogers. Packing and Covering, volume 54 of Cambridge Tracts in Mathematics and Mathematical Physics. Cambridge University Press, 1964.
- [15] H. Tanabe, S. Mu¨ller, M. Neusser, J. von Hase, E. Calcagno, M. Cremer, I. Solovei, C. Cremer, and T. Cremer. Evolutionary conservation of chromosome territory arrangements in cell nuclei from higher primates. Proc. Natl. Acad. Sci., 99:4424–4429, 2002.
- [16] A. Thue. Uber¨ die dichteste Zusammenstellung von kongruenten Kreisen in einer Ebene. Norske Vod. Selsk. Skr., 1:1–9, 1910.
- [17] M. J. Todd. Semideﬁnite optimization. Acta Numerica, 10:515–560, 2001.
- [18] M. J. Zeitz, L. Mukherjee, S. Bhattacharya, J. Xu, and R. Berezney. A probabilistic model for the arrangement of a subset of human chromosome territories in WI38 human ﬁbroblasts. J. Cell. Physiol., 221:120–129, 2009.


