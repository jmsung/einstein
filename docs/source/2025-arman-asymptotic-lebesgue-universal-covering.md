---
type: source
kind: paper
title: On asymptotic Lebesgue's universal covering problem
authors: Andrii Arman, Andriy Bondarenko, Andriy Prymak, Danylo Radchenko
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2512.04023v1
source_local: ../raw/2025-arman-asymptotic-lebesgue-universal-covering.pdf
topic: general-knowledge
cites:
---

# arXiv:2512.04023v1[math.MG]3Dec2025

## ON ASYMPTOTIC LEBESGUE’S UNIVERSAL COVERING PROBLEM

A. ARMAN, A. BONDARENKO, A. PRYMAK, AND D. RADCHENKO

Abstract. Universal cover in En is a measurable set that contains a congruent copy of any set of diameter 1. Lebesgue’s universal covering problem, posed in 1914, asks for the convex set of smallest area that serves as a universal cover in the plane (n = 2).

A simple universal cover in En is provided by the classical theorem of Jung, which states that any set of diameter 1 in an n-dimensional Euclidean space is contained in a ball Jn of radius 2nn+2; in other words, Jn is a universal cover in En.

We show that in high dimensions, Jung’s ball Jn is asymptotically optimal with respect to the volume, namely, for any universal cover U ⊂ En,

Vol(U) ≥ (1 − o(1))nVol(Jn).

1. Introduction and main result

1.1. Asymptotic bound on the volume of a universal cover. A measurable set U ⊂ En is called a universal cover if it contains a congruent copy of every set A ⊂ En of diameter 1. Lebesgue’s universal covering problem asks for the convex universal cover of smallest possible area in the plane (n = 2). Originally posed by Lebesgue in a 1914 letter to Pa´l and first published by Pa´l in [31], the problem has since been the focus of much activity, leading to a sequence of improvements both in lower bounds and explicit constructions. Important contributions include those of Sprague [33], Hansen [16], Elekes [13], and Baez–Bagdasaryan–Gibbs [3].

Despite this progress, the problem remains open: the best current lower bound, 0.832, is due to Brass and Sharifi [9], while the smallest known convex universal cover, of area 0.8440935944, is due to Gibbs [14] (pre-print). Although a non-convex cover of smaller area was obtained by Duff [11], it is now surpassed by the most recent convex construction [14]. Universal covers are closely linked to a range of classical extremal problems in convex and discrete geometry, with a notable connection to Borsuk’s question on decomposing a set into parts of strictly smaller diameter.

2020 Mathematics Subject Classification. Primary 52C17; Secondary 52A20, 52A22, 52A38, 52A39, 52A40, 49Q20.

Key words and phrases. Universal cover, volume, Jung’s theorem, Lebesgue’s problem, diameter, Borsuk’s problem.

The first author was supported in part by a postdoctoral fellowship of the Pacific Institute for the Mathe-

matical Sciences. The second author was supported in part by Grant 334466 of the Research Council of Norway. The third author was supported by NSERC of Canada Discovery Grant RGPIN-2020-05357. The fourth author was supported by ERC Starting Grant No. 101078782.

1

The broader question of existence, structure, and optimality of universal covers in various dimensions has also inspired substantial work, especially in the context of polyhedral coverings. Notable contributions include a series of papers by Makeev [25–29], as well as results of Kovalev [22], Kuperberg [23], and Hausel–Makai–Szˆucs [17]. For further perspectives, related problems, and survey material, see [8, Sect. 11.4] and [10, Section D15].

By Bn we denote the unit ball in En, and by Vol(·) the Lebesgue measure in En. A classical

theorem of Jung [18] states that the Euclidean ball Jn = rnBn with radius rn := 2nn+2 is a universal cover. Our main result shows that, in high dimensions, the volume of any universal

cover is at least (1−o(1))nVol(Jn), so Jung’s ball is an asymptotically optimal universal cover, up to a subexponential factor.

Theorem 1. Let U be a universal cover in En. Then

Vol(U) ≥ exp − (5/4 + o(1))nlog n Vol(Jn), where Jn is the ball of radius 2nn+2.

- 1.2. Relation to Borsuk’s question. Let b(n) denote the smallest number b such that any bounded set in En can be partitioned into b subsets of strictly smaller diameter. The example of a regular simplex shows that b(n) ≥ n+1. In 1933, Borsuk [6] asked whether b(n) = n+1 holds in all dimensions. This was verified for n = 2,3, but, unexpectedly, the conjecture fails in high

dimensions: in 1993, Kahn and Kalai [19] proved that b(n) > 1.2

√n for all sufficiently large n. The problem of determining b(n), along with many related questions, remains of significant interest; see, for example, the survey by Kalai [20].

In small dimensions, universal covers can be used to derive good estimates on b(n) by partitioning a universal cover into pieces of diameter < 1. For example, the regular hexagon whose opposite sides are at distance 1 is a universal cover in the plane (see Pa´l [31]), giving b(2) ≤ 3. Similarly, suitably truncated octahedra were used by Eggleston [12] and Grunbaum [15] to obtain b(3) ≤ 4. For general n, Lassak [24] observed that for a unit vector u the set Jn∩(rnu+Bn) is a universal cover and used this to show b(n) ≤ 2n−1+1, which remains the best known upper bound for 4 ≤ n ≤ 17.

For high dimensions, Theorem 1 implies that universal covers must have volume at least

(1−o(1))n(√12)nVol(Bn). Hence, if a universal cover in En could be partitioned into M subsets of diameter 1, then by the isodiametric inequality and simple volume estimates one would

obtain M ≥ (√2 − o(1))n. This is weaker than the currently best known asymptotic bound b(n) ≤ ( 3/2 + o(1))n established by Schramm [32] and by Bourgain and Lindenstrauss [7]. Thus, one cannot hope to improve the estimate on b(n) by partitioning universal covers into subsets of diameter strictly less than 1.

- 1.3. Asymptotic optimality for other geometric measures. A sharp result analogous to Theorem 1, but restricted to translative universal covers, was obtained independently by Bezdek and Connelly [4] and by Makeev [28, Th. 1], who proved that the minimal value of


mean width of a translative universal cover is exactly the mean width of Jung’s ball Jn. For general congruent (not necessarily translative) universal covers, Jn is not an exact minimizer for either volume or mean width, since, for example, for a unit u ∈ En the set Jn ∩ (rnu + Bn) is a universal cover with both smaller volume and smaller mean width than Jn.

As a corollary of Theorem 1, we deduce that Jn has asymptotically minimal mean width among all convex universal covers: by Urysohn’s inequality (see, e.g. [2, Sect. 1.5.5]), any convex universal cover in En must have mean width at least (1−o(1)) times that of Jn. We also remark that, similarly, by using Alexandov inequality (see, e.g. [2, Sect. 1.1.5]), the asymptotic optimality of Jn also holds with respect to any quermassintegral/intrinsic volume, for example, w.r.t. the surface area.

- 1.4. Outline of the proof of Theorem 1. Assume, to the contrary, that U is a minimal universal cover whose volume is too small (smaller than claimed by Theorem 1). For an appro-


priately chosen radius r very close to rn = 2nn+2 , we will construct a discrete set X ⊂ rBn of diameter at most 1 which is not contained in any member of the family U consisting of all

congruent copies of U that intersect rBn. Although the family U is infinite, it admits a discretization in the following sense: there exists a finite family Uε of congruent copies of a small “thickening” U + εBn such that every member of U is contained in some member of Uε; see Theorem 7. So, it remains to construct the desired X which is not contained in any member of Uε. The cardinality of Uε is quite large (bounded above by nn3), but remains sufficiently controlled for our argument.

The set X is then chosen probabilistically: we take a suitable number of random points in rBn, and, if necessary, delete certain points to ensure that the resulting set X has diameter ≤ 1. The probability that such a construction produces a set not covered by a fixed member of Uε can be estimated in terms of Vol(U + εBn), which is very close to Vol(U); see Section 2.2. If Vol(U) is too small, and since the cardinality of Uε is manageable, then such a set X must exist.

In Section 2.3 we develop a general framework for these probabilistic constructions, providing lower bounds on covering numbers by elements of a discrete family in terms of measurable graphs. This framework generalizes the deletion method previously used in [1]. Its application to our geometric setting is carried out in Section 2.4.

2. Proofs

- 2.1. Notations. Let µ be the rotation invariant probability measure on Sn−1, the unit sphere in En, and let


C(x,α) := {y ∈ Sn−1 : x · y ≥ cosα}

be the spherical cap of radius α centred at x ∈ Sn−1. We denote the measure of the spherical cap of radius α by m(α) := µ(C(x,α)). By [5, Cor. 3.2], for α ∈ (0,π/2) we have

- (1)

sinn−1 α √2πn

< m(α) <

sinn−1 α 2π(n − 1)cosα

.

We use | · | to denote the cardinality of a finite set, while ∥ · ∥ denotes the Euclidean norm.

2.2. Lemma about ε-thickening of a minimal universal cover. In each dimension, universal covers of minimal volume exist by [28, Th. 2]. To prove Theorem 1 we need the following property.

- Lemma 2. There is n0 such that for any n > n0, any universal cover U of minimal volume in En and any 0 < ε < 551 we have

(2)

Vol(U + εBn) Vol(U) ≤ 1 + ε · 55 · 5n .

While an estimate of the type (2) is natural to expect, U is not assumed to be convex which causes certain additional difficulties. We also remark that only a rough estimate is needed and the result does not contribute significantly in Theorem 1. We need the following two auxiliary results for the proof of Theorem 2.

- Lemma 3. For any measurable U ⊂ En, direction ρ ∈ Sn−1, and scalars 0 < h1 < h2, the set T(ρ,h1,h2,U) := {x ∈ En : x + tρ ∈ U for all t ∈ [h1,h2]}




satisfies

- h1

- h2 − h1


Vol(T(ρ,h1,h2,U) \ U) ≤

Vol(U).

Proof. It suffices to consider the case n = 1, as for larger n the inequality follows from the onedimensional case by considering restrictions to the lines with the direction ρ. Now assuming n = 1 and ρ = 1, define Q = {x ∈ ∂U : [x,x+h2 −h1] ⊂ U}. If Q is infinite, then Vol(U) = ∞ and the inequality is trivial. Otherwise, observe that

so

(T(1,h1,h2,U) \ U) ⊂

[x − h1,x],

x∈Q

- h1

- h2 − h1


- h1

- h2 − h1


Vol(U). □

[x,x + h2 − h1] ≤

Vol(T(ρ,h1,h2,U) \ U) ≤ h1|Q| =

Vol

x∈Q

Let K(a,ξ,α,l) be the cone with apex a ∈ En, axis direction ξ ∈ Sn−1, height ℓ > 0, and angle α ∈ (0,π/2):

K(a,ξ,α,ℓ) := {x ∈ En : ∥x − a∥cosα ≤ (x − a) · ξ ≤ l}.

- Lemma 4. Suppose α ∈ (0,π/2) and ℓ > 0. For constants ε0 = 3ℓ tan α2 cosα, c1 = sin1α/2, c2 =


3, for any a ∈ En, ξ ∈ Sn−1, ρ ∈ C(ξ,α/2), 0 < ε < ε0, we have a + εBn ⊂ T(ρ,c1ε,c1ε + c2,K(a,ξ,α,ℓ)).

ℓ

Proof. For any 0 < ε < ε0, let Kε := K(a,ξ, α2, 23ℓ) \ K(a,ξ, α2,εcot α2) be the corresponding “truncated cone” having half the angle of that of K(a,ξ,α,ℓ), the same axis and direction. It

is elementary to check that dist(Kε,∂K(a,ξ,α,ℓ)) = ε. The required inclusion follows provided a + tρ ∈ Kε whenever ρ ∈ C(ξ,α/2) and c1ε ≤ t ≤ c1ε + c2. Projecting on the direction of ξ, we observe that for ρ ∈ C(ξ,α/2) we have a + tρ ∈ Kε if εcot α2 ≤ tcosρ ≤ 23ℓ, in particular, if c1ε ≤ t ≤ c1ε + c2 (note c1ε < 3ℓ by the choice of ε0). □ Proof of Theorem 2. It is well-known that for any body W of constant width 1, the largest inscribed ball and the smallest circumscribed ball have the same centre and the sum of their radii is 1, see [30, Th. 3.4.1, p. 69]. By the Jung’s theorem [18], the radius of the circumball of W is less than R := √12, so the radius of the inscribed ball is at least r := 1 − √12. Thus, by convexity of W, for any x ∈ W, one can find ξ ∈ Sn−1 with K(x,ξ,α,r) ⊂ W and α = arcsin Rr . As sin(α/2) > 1/5, by standard sphere covering arguments ([5, Th. 1.1], (1)), for sufficiently large n0 we can find a set X ⊂ Sn−1 of N = 5n directions (independent of W) such that any spherical cap of radius α/2 contains a direction from X. Therefore, we can apply Theorem 4 (with α = arcsin Rr and ℓ = r) to obtain the following statement: for any body of constant width 1 in En, any x ∈ W, and any 0 < ε < ε0, there exists ρ ∈ X such that

x + εBn ⊂ T(ρ,c1ε,c1ε + c2,K(x,ξ,α,r)) ⊆ T(ρ,c1ε,c1ε + c2,W).

Since any minimal universal cover U is the union of a family of bodies of constant width 1, the above statement is true when W is replaced with U. Now we apply Theorem 3 for each ρ ∈ X and obtain

c1ε c2

Vol((U + εBn) \ U) ≤ N

Vol(U), which concludes the proof after the constants are tracked. □

- 2.3. General lower bound on covering in terms of measurable graphs. We now give a general probabilistic construction of cocliques in graphs that are hard to cover by sets from a given finite family. A graph Γ is a pair (V,E) where E ⊆ V × V is the set of edges of Γ; we always assume that Γ is unoriented, that is, (x,y) ∈ E if and only if (y,x) ∈ E. We will also denote by ∆(V ) the diagonal {(v,v): v ∈ V } ⊆ V × V .


Given a set Ω, a family Y of subsets of Ω, and X ⊂ Ω, we define the covering number as N(X,Y) := min |U| : X ⊂

Y, U ⊂ Y .

Y ∈U

In other words, N(X,Y) is the minimal number of sets from Y needed to cover X. Our key auxiliary result is the following lemma.

- Lemma 5. Let Γ = (V,E) be a graph and assume that V is equipped with a probability measure ν satisfying (ν × ν)(∆(V )) = 0. Let Y be a finite family of measurable subsets of V . Assume 0 < p < 12, M,k ∈ Z>0 and 1 ≤ k ≤ 21p. If


- (3) ν(Y ) ≤ p for all Y ∈ Y, |Y| ≤

- 1

- 2


(2ekp)−

M

- (4) 2k, and (ν × ν)(E) ≤

- 1

- 2M


- (5) , then there exists a coclique X ⊂ V such that


|X| ≥ M/2 and N(X,Y) > k .

Informally, the lemma asserts that one can construct a sufficiently large coclique X in a measurable graph Γ that is difficult to cover by members of Y. The sets in Y play the role of potential “covering pieces”, and the assumptions require only that each such set is not too “large” (3) and that the total number of these sets is controlled in a relatively “mild” way (4). The edges of Γ encode an “undesirable” relation between vertices — one that we want to avoid in our final set X. Thus, in order for a large coclique to exist, we require that the graph does not contain “too many” edges (5). The construction itself is probabilistic: we begin by randomly selecting M vertices of Γ, and then delete at most M/2 of them to remove all edges among the chosen vertices, leaving a coclique of the desired size.

Proof of Theorem 5. Let z1,...,zM be i.i.d. random variables in V distributed with respect to ν, and let Z = {z1,...,zM}. Since ∆(V ) has ν × ν measure 0, we have |Z| = M with probability 1.

Next, for any Y ∈ Y the cardinality |Z ∩ Y | has binomial distribution Bi(M,p˜) where p˜ = ν(Y ) ≤ p. Applying Chernoff’s bound [35, Th. 2.3.1] we have

M

P(|Z ∩ Y | ≥ M2k) < (2ekp)

2k .

Therefore, by the union bound, with probability > 1/2 we have |Z ∩ Y | < M2k for all Y ∈ Y. Finally, since P((zi,zj) ∈ E) ≤ 2M1 for all i < j, the expected number of edges in Z is at

most M2 2M 1 < M4 . Then by Markov’s inequality with probability > 1/2 the number of edges in Z is at most M/2, and so removing one vertex from each edge gives a coclique X with ≥ M/2

elements and with nonzero probability it satisfies |X ∩ Y | < M2k for all Y ∈ Y, completing the proof. □

- 2.4. Volume bound for universal covers. Now we apply the general bound for our geometric setting. Recall (see Section 2.1) that C(v,α) is the spherical cap of radius α centered at v ∈ Sn−1, and m(α) is the measure of such a cap.


- Lemma 6. Let 0 < α < π/2, 0 < p < 21k, k ∈ Z>0, and suppose that Y is a family of measurable sets in En such that

Vol(Y ∩ rBn) ≤ pVol(rBn) for all Y ∈ Y.

If N(X,Y) ≤ k for any subset X ⊂ rBn with diam(X) < 2r cos(α/2), then |Y| >

- 1

- 2


(2ekp)−1/(4m(α)k).

Proof. After rescaling we may assume that r = 1. We are going to apply Lemma 5 with V = Bn, E = {(x,y) ∈ V 2: ∥x − y∥ ≥ 2cos(α/2)}, and ν(A) = Vol(A∩B

n)

Vol(Bn) . The only thing that we need is an estimate on the measure of E. We claim that for any x ∈ Bn

(6) ν({y ∈ Bn : ∥x − y∥ ≥ 2cos(α/2)}) ≤ m(α). Note that 2cos(α/2) > √2, so (6) is trivial when x = 0. Assuming x ̸= 0, set v := −x/∥x∥. Then for any y ∈ Bn satisfying ∥x − y∥ ≥ 2cos(α/2), we have

−x · y ≥ 2cos2(α/2) −

∥x∥2 + ∥y∥2 2 ≥ cosα ≥ ∥x∥cosα,

i.e., v·y ≥ cosα. This means that such y must belong to the convex hull of C(v,α), hence, to the convex hull K of C(v,α) and the origin. It remains to observe that Vol(K) = m(α)Vol(Bn), and (6) follows. This clearly implies that (ν × ν)(E) ≤ m(α). Now taking M = 2m1(α) in Lemma 5 we complete the proof. □

Next we need a construction of an appropriate finite family of sets covering any congruent copy of a given set in En. For ε > 0 and bounded X ⊂ En we will denote the ε-covering number of X by N(X,ε) := N(X,Bε), where Bε is the collection of all closed balls of radius ε in En. In other words, N(X,ε) denotes the size of the smallest ε-covering of X.

- Lemma 7. Suppose D,ε > 0 and V ⊂ En is bounded. Then there exists a finite set T of isometries of En with


n(n−1)

|T| ≤ 2N(V, 2εD)(500εD)

2 ,

such that for any compact set K ⊂ En of diameter D containing the origin and any congruent copy K′ = AK + v with A ∈ O(n), v ∈ V , we have K′ ⊆ g(Kε) for some g ∈ T, where Kε = K + εBn is the ε-thickening of K.

Proof. Let G be the isometry group of En, with the metric d(f,g) = max∥x∥≤1 ∥f(x) − g(x)∥. Note that for f,g ∈ G we have f(K) ⊆ g(Kε) provided ρ(f(K),g(K)) ≤ ε, where ρ is the Hausdorff metric on compact subsets of En. Since K is contained in the ball of radius D, we have ρ(f(K),g(K)) ≤ D·d(f,g). Note that any f ∈ G can be uniquely written as f(x) = Ax+v with v = f(0) ∈ En and A ∈ O(n). Therefore, it suffices to take T to be an (ε/D)-covering in the set G′ = {f ∈ G: f(0) ∈ V }.

For f(x) = Ax + v and g(x) = Bx + w, where A,B ∈ O(n) and v,w ∈ En, we have d(f,g) ≤ ∥A−B∥op+∥v−w∥ with ∥·∥op denoting operator norm for matrices. By [34, Prop. 6]

### (see also [34, Cor. 4] for derivation of the constants) any minimal ε-net in O(n) has size at most 2(c/ε)

n(n−1)

2 , where c = 3πeπ < 220. Taking T consisting of f(x) = Ax+v with A running over an 2εD-net in O(n) and v over an 2εD-covering in V , we get the required bound on |T|. □

n(n+1)

As a corollary, if V is a ball of radius R one can find T with |T| ≤ Rn(500εD)

2 .

Proof of Theorem 1. Assume that U is a universal cover in En of minimal volume, n ≥ n0. By Lemma 2, if we take Uε = U + εBn with ε = 551·5

, we have Vol(Uε) ≤ 2Vol(U).

n

In the proof of [28, Th. 2], it is shown that diam(U) ≤ 2(1+vn)/vn, where vn = Vol((1−√12)Bn). Therefore, as n ≥ n0, we get diam(U) < nn/2−1. Thus, applying Lemma 7 with K = U and V a ball of radius nn/2 gives us a finite family T of isometries, with |T| ≤ n

n2(n+3)

n(n+1)

2 < 12nn3, such that any isometric copy of U intersecting Bn is contained in g(Uε) for some g ∈ T.

4 (500ε )

Applying Lemma 6 with r < rn, cos(α/2) = 21r, k = 1, and the family Y = {g(Uε): g ∈ T} with T constructed as above (so |Y| < 21nn3), we get that for p = Vol(U)/Vol(rnBn), Vol(Uε ∩ rBn) ≤ 2p(rn/r)nVol(rBn), and so for all sufficiently large n

- 1

- 2


- 1

- 2


3

(4ep(rn/r))−1/4m(α) ≤ |Y| <

nn

, or

3

- (7) 4ep ≥ (r/rn)nn−4m(α)n


.

We choose α so that sin(α) = 1−λlogn n. Then a simple calculation shows that cos(α) ∼ 2λlogn n, (rn/r)n ∼ exp( (λ/2)nlog n − 12), and using (1) we get 4m(α) ≤ c

nλ √logn. Plugging these estimates into (7) we obtain

1

p ≥ c2 exp(− (λ/2)nlog n − c1n3−λ log n), so for any λ > 5/2 we get p ≫ exp(− (λ/2)nlog n), proving the claim. □

Acknowledgement. We are grateful to Gil Kalai for several insightful comments and questions on his blog, most notably comment 3 of [21], which helped stimulate this work. We would also like to thank Beatrice-Helen Vritsiou for asking us a question on covering a set of diameter 1 by families of bodies of fixed diameter.

References

- [1] Andrii Arman, Andrii Bondarenko, and Andriy Prymak, Convex bodies of constant width with exponential illumination number, Discrete Comput. Geom. 74 (2025), no. 1, 196–202.
- [2] Shiri Artstein-Avidan, Apostolos Giannopoulos, and Vitali D. Milman, Asymptotic geometric analysis. Part I, Mathematical Surveys and Monographs, vol. 202, American Mathematical Society, Providence, RI, 2015.
- [3] John C. Baez, Karine Bagdasaryan, and Philip Gibbs, The Lebesgue universal covering problem, J. Comput. Geom. 6 (2015), no. 1, 288–299.


- [4] K´roly Bezdek and Robert Connelly, The minimum mean width translation cover for sets of diameter one, Beitr¨ge Algebra Geom. 39 (1998), no. 2, 473–479.
- [5] K. B¨r¨czky Jr. and G. Wintsche, Covering the sphere by equal spherical balls, Discrete and computational geometry, Algorithms Combin., vol. 25, Springer, Berlin, 2003, pp. 235–251.
- [6] Karol Borsuk, Drei S¨atze u¨ber die n-dimensionale euklidische Sph¨are, Fundamenta Mathematicae 20 (1933), no. 1, 177–190.
- [7] J. Bourgain and J. Lindenstrauss, On covering a set in RN by balls of the same diameter, Geometric aspects of functional analysis (1989–90), Lecture Notes in Math., vol. 1469, Springer, Berlin, 1991, pp. 138–144.
- [8] Peter Brass, William Moser, and J´nos Pach, Research problems in discrete geometry, Springer, New York, 2005.
- [9] Peter Brass and Mehrbod Sharifi, A lower bound for Lebesgue’s universal cover problem, Internat. J. Comput. Geom. Appl. 15 (2005), no. 5, 537–544.
- [10] Hallard T. Croft, Kenneth J. Falconer, and Richard K. Guy, Unsolved problems in geometry, Problem Books in Mathematics, Springer-Verlag, New York, 1994. Corrected reprint of the 1991 original [MR1107516 (92c:52001)]; Unsolved Problems in Intuitive Mathematics, II.
- [11] G. F. D. Duff, A smaller universal cover for sets of unit diameter, C. R. Math. Rep. Acad. Sci. Canada 2 (1980/81), no. 1, 37–42.
- [12] H.G. Eggleston, Covering a three-dimensional set with sets of smaller diameter, J. London Math. Soc. (2) 30 (1955), 11–24.
- [13] G. Elekes, Generalized breadths, circular Cantor sets, and the least area UCC, Discrete Comput. Geom. 12

(1994), no. 1, 439–449.

- [14] Philip Gibbs, An upper bound for Lebesgue’s covering problem, available at https://arxiv.org/abs/1810. 10089v1.
- [15] Branko Gru¨nbaum, A simple proof of Borsuk’s conjecture in three dimensions, Proc. Cambridge Philos. Soc. 53 (1957), 776–778.
- [16] H. Hansen, Small universal covers for sets of unit diameter, Geom. Dedicata 42 (1992), 205–213.
- [17] Tamas Hausel, Endre Jr. Makai, and Andr´s Szuˆcs, Inscribing cubes and covering by rhombic dodecahedra via equivariant topology, Mathematika 47 (2000), no. 1–2, 371–397.
- [18] Heinrich Jung, Ueber die kleinste Kugel, die eine r¨aumliche Figur einschliesst, J. Reine Angew. Math. 123

(1901), 241–257 (German).

- [19] Jeff Kahn and Gil Kalai, A counterexample to Borsuk’s conjecture, Bull. Amer. Math. Soc. (New Series) 29 (1993), no. 1, 60–62.
- [20] Gil Kalai, Some old and new problems in combinatorial geometry I: Around Borsuk’s problem, Surveys in Combinatorics 2015, 2015, pp. 147–174.
- [21] Gil Kalai, Progress Around Borsuk’s Problem (Blog post, 4 December 2023), available at https:// gilkalai.wordpress.com/2023/12/04/progress-around-borsuks-problem/.
- [22] M. D. Kovalev, The smallest Lebesgue covering exists, Mat. Zametki 40 (1986), no. 3, 401–406, 430 (russian).
- [23] Greg Kuperberg, Circumscribing Constant-Width Bodies with Polytopes, New York J. Math. 5 (1999), 91–100.
- [24] Marek Lassak, An estimate concerning Borsuk’s partition problem, Bull. Acad. Polon. Sci. Ser. Math. 30

(1982), 449–451.

- [25] V. V. Makeev, Universal coverings. I, Ukrain. Geom. Sb. 25 (1981), 70–79, iii (russian).
- [26] , Universal coverings. II, Ukrain. Geom. Sb. 25 (1982), 82–86, 142–143 (russian).

- [27] , Universal coverings and projections of bodies of constant width, Ukrain. Geom. Sb. 32 (1989), 84–88 (russian); English transl., J. Soviet Math. 59 (1992), no. 2, 750–752.


- [28] , Extremal coverings, Mat. Zametki 47 (1990), no. 6, 62–66, 159 (russian); English transl., Math. Notes 47 (1990), no. 5-6, 570–572.

- [29] V.V. Makeev, On affine images of a rhombo-dodecahedron circumscribed about a three-dimensional convex body, Geom. i Topol. 246 (1997), no. 2, 191–195, 200 (russian).
- [30] H. Martini, L. Montejano, and D. Oliveros, Bodies of constant width, Birkha¨user/Springer, Cham, 2019. An introduction to convex geometry with applications.
- [31] J. P´l, Uber¨ ein elementares Variations problem, Math.-fys. Medd., Danske Vid. Selsk. 3 (1920), 35 pp.
- [32] O. Schramm, Illuminating sets of constant width, Mathematika 35 (1988), no. 2, 180–189.
- [33] R. Sprague, Uber¨ ein elementares Variations problem, Mat. Tidsskr. Ser. B (1936), 96–98.
- [34] S. J. Szarek, Nets of Grassmann manifold and orthogonal group, Proceedings of Banach Space Workshop, 1981.
- [35] R. Vershynin, High-dimensional probability, Cambridge Series in Statistical and Probabilistic Mathematics, vol. 47, Cambridge University Press, Cambridge, 2018. An introduction with applications in data science; With a foreword by Sara van de Geer.


Department of Mathematics, University of Manitoba, Winnipeg, MB, R3T 2N2, Canada Email address: andrew0arman@gmail.com

Department of Mathematical Sciences, Norwegian University of Science and Technology,

NO-7491 Trondheim, Norway Email address: andriybond@gmail.com Department of Mathematics, University of Manitoba, Winnipeg, MB, R3T 2N2, Canada Email address: prymak@gmail.com Universite´ de Lille, CNRS, Laboratoire Paul Painleve,´ F-59655 Villeneuve d’Ascq, France Email address: danradchenko@gmail.com

